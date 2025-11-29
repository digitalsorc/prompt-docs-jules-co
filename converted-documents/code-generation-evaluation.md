---
title: "Code Generation Evaluation"
original_file: "./Code_Generation_Evaluation.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["llm", "rag", "evaluation", "multimodal"]
keywords: ["nomad", "martignac", "solute", "simulation", "workflow", "simulations", "free", "solvent", "data", "workflows"]
summary: "<!-- Page 1 -->

Martignac: Computational workflows for reproducible, traceable, and
composable coarse-grained Martini simulations
Tristan Bereau,1,a) Luis J. Rudzinski2
1)Institute for Theoretical Physics, Heidelberg University, 69120 Heidelberg, Germany
2)Physics Department and CSMB Adlershof, Humboldt-Universita¨t zu Berlin, 12489 Berlin,

### Germany

(Dated: 25 September 2024)
Despite their wide use and far-reaching implications, molecular dynamics (MD) simulations suffer from a
lack of bot"
related_documents: []
---

# Code Generation Evaluation

<!-- Page 1 -->

Martignac: Computational workflows for reproducible, traceable, and
composable coarse-grained Martini simulations
Tristan Bereau,1,a) Luis J. Walter,1 and Joseph F. Rudzinski2
1)Institute for Theoretical Physics, Heidelberg University, 69120 Heidelberg, Germany
2)Physics Department and CSMB Adlershof, Humboldt-Universita¨t zu Berlin, 12489 Berlin,

### Germany

(Dated: 25 September 2024)
Despite their wide use and far-reaching implications, molecular dynamics (MD) simulations suffer from a
lack of both traceability and reproducibility. We introduce Martignac: computational workflows for the
coarse-grained (CG) Martini force field. Martignac describes Martini CG MD simulations as an acyclic
directedgraph,providingtheentirehistoryofasimulation—fromsystempreparationtopropertycalculations.
Martignac connects to NOMAD, such that all simulation data generated are automatically normalized and
storedaccordingtotheFAIRprinciples. WepresentseveralprototypicalMartiniworkflows,includingsystem
generationofsimpleliquidsandbilayers,aswellasfree-energycalculationsforsolutesolvationinhomogeneous
liquids and drug permeation in lipid bilayers. By connecting to the NOMAD database to automatically
pull existing simulations and push any new simulation generated, Martignac contributes to improving the
sustainability and reproducibility of molecular simulations.

## I. Introduction

Despite ever-increasing attention and community efforts for the last half century, molecular dynamics
(MD) simulations remain poorly shared, deficiently reproducible, and often devoid of history or traceability.

### The sharing of MD data is made complex due to the

fragmentation of hardware, software code, force fields,
and simply the sheer diversity of systems of interest.1

### Efforts in this direction include the BioExcel Building

Blocks(BioBB)library,2theCOVID-19MolecularStructure and Therapeutics Hub,3 a general index of MD-
simulationrepositoriesfoundonline(MDverse),4 andthe

### Simulation Foundry.5 Yet, a recent document reiterated

specific needs for the community, including persistent,
indexed, and open access to MD data, metadata annotation, application programming interfaces (APIs) for
data exchange, and comprehensive provenance information (i.e., history of the simulation).6 Here we propose
a concrete end-to-end solution for the popular coarsegrained (CG) Martini biomolecular force field.7,8 We introduce Martignac, a workflow manager that automatically connects to an online database, avoids redundant
calculations by downloading existing entries, runs missingsimulations,andsubsequentlyuploadsthemtoenrich
thedatabase(Fig.1). Martignacoffersatraceable,composable,andreproducibleframeworkforgeneral-purpose FIG. 1. Martignac implements Martini coarse-grained simand high-throughput CG Martini simulations. ulations as computational workflows. The library interacts
Toenablereproducibilityandprovenanceinformation, with the NOMAD web server to automatically fetch any excomputer simulations need a strict, specialized, and sys- isting simulation, and push any new contribution.
tematic workflow: a management system designed to
orchestrate activities and organize resources into processes. Scientific workflows typically compose individual Theyhaverapidlybecomeanessentialingredienttocapunits of calculations as a directed acyclic graph (DAG). ture provenance information in materials modeling (e.g.,
see AiiDA workflows9). Martignac makes integral use
of computational workflows. We will see that not only
does this offer reproducible and traceable MD simulaa)Electronicmail: bereau@uni-heidelberg.de tions, it also enables the composability of several MD
4202
peS
32
]hp-mehc.scisyhp[
1v87451.9042:viXra

<!-- Page 2 -->

2
workflowstogether,thusavoidingredundantcalculations workflows that is expected to be of general interest to
upon compound screening. the broader CG Martini community. We distinguish two
Martignac implements worklows via signac-flow, a categories of workflows: (i) system generation and (ii)
Pythonlibrarythatmanagesandautomatesworkflowsin free-energycalculation. ThesystemsthatMartignaccan
computational research.10,11 It organizes, executes, and generateconsistof: asoluteinthegas(i.e.,amoleculein
monitors data processing pipelines, making it easier to an empty simulation box); a solvent (i.e., homogeneous
handle complex and large-scale simulations and analy- fluid); a solute inserted in a solvent; and a phospholipid
ses. Theframeworkhasbeenappliedtoseveralprojects, bilayer. The free-energy-calculation workflows comprise
including the assembly of colloidal diamond,12 photonic the solvation of a solute in a solvent, and the potential
crystals,13 and lubricating monolayer films.14,15 The last of mean force of a small molecule in a phospholipid biapplication mentioned is the outcome of a larger consor- layer. Thereadermayalreadyforetelltheworkflowcomtium called MoSDeF, which offers a set of Python tools posability at play: for instance, calculating the solvation
to help initialize, assign force-field parameters, and sup- free energy of a solute requires to both generate the soportscreeningofsoft-mattersystems.16Severaloftheau- lute and the solvent independently, then combine them
thors of the last study have highlighted signac-flow as to generate the system, and finally run the free-energy
anessentialtooltoimprovethereproducibilityofmolec- calculations.
ular simulations, where they propose a set of principles The present article first describes the NOMAD
to create Transparent, Reproducible, Usable by others, database in Sec. II, followed by Martignac’s workflow
andExtensible(TRUE)molecularsimulations.17Though methodology in Sec III, including the contents of the
not mentioned in the article, the TRUE principles over- worfklows and how they connect to NOMAD. In Sec. IV
lap significantly with the much more widespread FAIR we summarize some of the MD simulation methods and
data principles: Findability, Accessibility, Interoperabil- parameters. Sec. V highlights a number of applications
ity, and Reuse of digital assets.18 madepossiblebyMartignac: howthecontentoftheDAG
TheaspirationtoworkwithFAIRdatahasseenrapid generated by Martignac is translated to NOMAD, the
and intense developments in many areas of science.19–21 composability of workflows, a reproducibility calculation
In materials science, NOMAD22 is one of the leading ef- ofoil/watertransferfreeenergies,andfinallyanotherreforts in building FAIR databases.23–25 Originally built producibility calculation for drug-membrane PMFs. We
as a repository for ab initio calculations, NOMAD has conclude with a number of final remarks and outlook in
been recently transformed into a versatile research data Sec. VI.
management platform for a wide variety of materials
science data.26 Specifically relevant for this work, the
openly-available NOMAD web-based platform provides II. NOMAD FUNCTIONALITIES
the following functionalities: (i) automated detection
andparsingofrawmolecularsimulationfilesfromGRO- This section on the NOMAD database is only a short
MACS,(ii)customworkflowsthatallowconnectionsbe- summary of the NOMAD documentation,34 with a focus
tween independently run simulations and analysis stored on aspects useful to Martignac.
in the database, and (iii) a full suite of API commands,
enabling scriptable communication with the database.
Martignac leverages these functionalities to not only fa- A. Processing and organization
cilitate transparent storage of the executed simulations
andworkflowsbutalsotoimproveefficiencyandprevent NOMAD ingests the raw input and output files from
redundancy, i.e., to provide a comprehensive FAIR data standard simulation software by first identifying a repmanagement solution. resentative file (e.g., the log file in the case of GRO-
Martignac places a specific emphasis on high- MACS) and then employing a parser code to extract relthroughput screening (HTS) applications. The Martini evant (meta)data from the associated files to that simmodel has been an invaluable model for HTS applica- ulation. The (meta)data are stored within a structured
tions due to its top-down parametrization: its building- schema—the NOMAD Metainfo—to provide context for
block approach of CG bead types effectively reduces the each quantity, enabling interoperability and comparison
sizeofchemicalcompoundspace.27,28 TheuseofMartini between simulation software. The compilation of all
for HTS has enabled a number of applications, including (meta)data obtained from this processing forms an enprotein-ligandbinding,29 theextensivescreeningofdrug- try—thefundamentalunitofstoragewithintheNOMAD
membrane permeation for 0.5 million compounds,30 the database—includingsimulationinput/output,authorinpotentials of mean force (PMFs) of all Martini dimers formation, and additional general overarching metadata
inserted in six phospholipid bilayers,31 the identifica- (e.g., references or comments). In addition, a NOMAD
tion of driving forces for generic anaesthetics,32 and the entryoffersuniqueidentifiers: bothanentry idtomanmolecular discovery of a molecular probe selective to age unpublished data and also a DOI once published.
cardiolipin.33 NOMAD entries can be organized hierarchically into
Martignac implements a select list of computational uploads, workflows, and datasets. Since the parsing exe-

<!-- Page 3 -->

3
cution is dependent on automated identification of rep- III. MARTIGNAC WORKFLOW METHODOLOGY
resentative files, users are free to arbitrarily group simulations together upon upload. In this case, multiple
Thepresentsectionfocusesontheconceptualideasbeentrieswillbecreatedwiththecorrespondingsimulation
hind Martignac. For a description of the Python library,
data. Anadditionaluniqueidentifier,upload id,willbe we refer the reader to the online documentation.36
provided for this group of entries. Although the group-
Workflowsarebuiltasdirectedacyclicgraphs(DAGs).
ing of entries into an upload is not necessarily scientif-
DAGs consist of nodes and single-directional edges.
ically meaningful, it is practically useful for submitting

### In our context, nodes are computational operations,

batches of files from multiple simulations to NOMAD.
e.g., generating a molecular configuration or running
Concretely,Martignacutilizesuploadstogroupallλcouan MD simulation. These operations are interlinked—
pling points of a thermodynamic-integration calculation.
one cannot analyze a trajectory that has not yet been

### ThisisparticularlyconvenientsinceNOMADretainsthe

simulated—leading to a required ordering of the operaoriginal directory structure when storing all the raw and
tions via directional connections, i.e., the DAG’s edges.
processed data.

### The Martignac implementation builds on the flexible

NOMAD offers flexibility in the construction of worksignac-flow library.10,11 signac-flow systematically
flows. First, a molecular dynamics simulation is a workmanages and distributes a set of operations (e.g., MD
flowinitself. The(meta)dataforthisstandardworkflow
simulations) repeated across many systems. This makes
are automatically stored during processing and entail all
signac-flow appealing for high-throughput screening,
relevantaspects: MDruntimeparametersandensemblewhereconsistencyisaparamountrequirement. Eachsysaveraged or time-dependent observables. Furthermore,
tem studied is called a state point, which signac-flow

### NOMAD also allows the creation of custom workflows,

associates to a unique and persistent job identifier (ID).
which are completely general directed graphs, allowing
Each job is thereby a collection of interdependent opusers to link NOMAD entries with one another in orerations, each implemented as a Python function. In
der to provide the provenance of the simulation data.
addition, the workflow requires label functions, which

### Customworkflowsarecontainedwithintheirownentries

determine whether the operation has already been run.
and, thus, have their own set of unique identifiers. To

### Finally, interdependences between operations (i.e., the

create a custom workflow, the user is required to upload
DAG’s edges) are specified by pre- and post-conditions
aworkflowyamlfiledescribingtheinputsandoutputsof
on other label functions.
each entry within the workflow, with respect to sections
Martignac workflows target various domain applicaof the NOMAD Metainfo schema. Martignac automatitions (e.g., generating a solvent or calculating the free
cally creates this file for its workflows, without the user
energyofasoluteinaphospholipidmembrane). Because
beingrequiredtounderstandanydetailsoftheNOMAD
these domain applications share a number of operations,
schema.
we separate workflows into two components:
At the highest level, NOMAD groups entries with the
use of datasets. A NOMAD dataset allows the user to

## Genericoperationsthatweapplyirrespectiveofthe

group a large number of entries, without any specificadomain application;
tion of links between individual entries. A DOI is also
generated when a dataset is published, providing a con-

## Domain-application specific operations;

venientrouteforreferencingalldatausedforaparticular
investigation within a publication.
as shown in Fig. 2.
B. Programmatic access, query, and interaction
symlinkITP/MDP uploadtoNOMAD

### In addition to its GUI interface, NOMAD supports

scriptable access to its database and functionalities
through an extensive application programming interface fetchfromNOMAD buildNOMADworkflow
(API).26 A REST API queries the server by a combination of GET and POST requests. Martignac uses this

### APIthroughavarietyofpythonfunctionsthatlowerthe

barrier for use by conveniently combining multiple API
application-specificsubgraph
callsintoasingleroutineandperformvalidationtests. In
particular Martignac uses Marshmallow schemas to validatetheinputdatathatisreceived,aswellasdeserialize FIG.2. TheMartignacworkflowstructureissplitintwosubthe input data to Python objects.35 Read-only requests graphs: (i)genericoperationscommontoallsimulationworkflows(yellow);(ii)domain-applicationspecificoperations(see
of publicly available entries can be made without NO-
Fig. 4).

### MAD credentials. Otherwise, a NOMAD username and

password is required to authenticate the API request.

<!-- Page 4 -->

4

### A. Generic subgraph

{’job_id’: ’3e793a7b2a1e83233c40458fddf958ab’,
’itp_files’: ’a52590b1d87d122ba1e376b83c3d6bee’
,
The generic operations consist of the following:
’mdp_files’: ’2d7a9e52d14d23e0dfb97192d75a3463’
,
• symlink ITP/MDP: Force-field-definition files ’state_point’: {
’solute_name’: ’P5’, ’type’: ’solute’
are extremely redundant: the same sets of *.itp
},
files are necessary to run any Martini simulation. ’workflow_name’: ’SoluteGenFlow’}
Similarly, high-throughput workflows will typically
work with identical *.mdp input-parameter files to

### FIG. 3. Comment of an example job upload. The respective

obtain systematic simulations. A systematic upkeyscorrespondtothesignac-flowjobID,thehashesofthe
load of these files creates an unnecessary burden
collection of *.itp and *.mdp files, respectively, state-point
on storage requirements. To this end, Martignac dependent information, including the solute name and type,
makes use of symbolic links to mitigate local stor- and finally the workflow Python-class name.
age footprint and avoids uploading said files to the
server. However,reproducibilityremains: standard
Martiniforce-fieldfilesareavailableonline.37While B. Application-specific subgraphs
input *.mdp parameter files are not saved, Martignac does store the (equivalent) output *.mdp
Hereweshortlydescribethedirectedacyclicsubgraphs
files generated by the GROMACS preprocessor,
that are application specific, and contained within the
grompp.
larger Martignac DAG (see Fig. 2). This implies that all
application-specific subgraphs described below are both
• fetch from NOMAD: Martignac queries the preceded and followed by the node operations described
user’sNOMADdatasettolookforanexistingsim- in the generic subgraph above.
ulation already stored online. Martignac checks
whetherthesimulationqueriedexactly corresponds
to the one to be attempted. Comparison is made 1. Solute generation
onthebasisof(i)theworkflowPython-classname,
(ii)thesignac-flowjobID,and(iii)ahashofall Generating a solute in the gas phase (i.e., an empty
input *.mdp files involved. The information is con- box, Fig. 4a) consists of three steps
tained as a JSON-formatted comment of the simulationupload,whichisautomaticallygeneratedand 1. build: From the name of the solute molecule, genpushed with any upload (see below). For instance, erate a structure, particle-definition, and topology
Fig.3isacommentforasimulationuploadofasin- files, gro, itp, and top, respectively.
gle solute generation. This check ensures integrity
beyond the mere desired workflow and chemistry, 2. minimize: Energy minimization.
but also in the exact input files used.
3. equilibrate: Equilibration MD simulation.
• build NOMAD workflow: The chain of opera- Theonlystate-pointparameteristhenameofthesolute.
tions implemented in Martignac form a DAG. Said

### DAG is converted and serialized into a NOMAD-

compatible workflow yaml file, for subsequent sim- 2. Solvent generation
ulation upload.

### We consider the generation of a homogeneous liquid

• upload to NOMAD: All files generated during that fills the simulation box (Fig. 4b)
a Martignac workflow (except for the *.itp Martini definition files and input *.mdps) are zipped 1. generate solvent molecule: Generate a single
together with the yaml NOMAD workflow file and solvent molecule. This step is analogous to the
uploaded to the NOMAD webserver via an API build part of the solute-generation workflow.
POST request. A comment is attached to every up-
2. build solvent box: build a box of solvent
load containing a JSON-formatted string containmolecules by means of the PACKMOL program.38
ing identifiable information about the content of
the job.
3. convert box to gro: The preceding PACKMOL
operation yields a pdb file. The present operation
The generic operations are arranged as shown in Fig. 2: simply converts the pdb to a gro structure file.
a linear chain of operations with the application-specific
subgraph in the middle. 4. minimize: Energy minimization.

<!-- Page 5 -->

5
FIG. 4. Martignac workflows. System generation: (a) Solute; (b) solvent; (c) solute in solvent; (e) phospholipid bilayer. Freeenergy calculations: (d) solute-in-solvent free energy; (f) solute-in-bilayer potential of mean force. Blue and green operations
distinguishMDsimulationsfromtheothers,respectively. Thecomposabilityofworkflowsishighlightedbyentiregraphsbeing
part of others. Aggregation of λ states or umbrella collective variables, z, recycles common operations and makes use of all
relevant information for analysis. The outcome of each workflow is illustrated: either a generated system or a free energy.
5. equilibrate: Equilibration MD simulation. For 4. minimize: Energy minimization.
instance, this could be run at constant pressure
5. equilibrate: Equilibration MD simulation.
with a forgiving barostat, such as Berendsen or C-
rescale. 6. production: Production MD simulation.
6. production: Production MD simulation. The state-point parameters are the solute and solvent
names.
Theonlystate-pointparameteristhenameofthesolvent
molecule.

## Solute-in-solvent alchemical transformation


## Solute-in-solvent generation Composability is leveraged once again here (Fig. 4d).


### Wemakeuseofthesolute-in-solventsystemgeneratedin

The solute-in-solvent generation (Fig. 4c) makes use thelastworkflow. Free-energycalculationsareemployed
of the composability of the Martignac workflows: it first to compute the free energy of coupling the solute in the
generates the solute and the solvent using the above- solvent. We make use of thermodynamic integration,
mentioned workflows, and subsequently joins them to whereaseriesofHamiltoniansinterpolatingbetweenthe
yield the desired system. As such the DAG is not linear, two end states, denoted by the parameter λ ∈ [0,1], inbut contains branches to link the individual components creasingly couple the solute in the simulation box. As
together. such the DAG needs to be run not only once for the system of interest, but n times, indicative of the number of
1. generate solute: fetch or run the solute generainterpolating Hamiltonians. The present workflow DAG
tion workflow (Sec. IIIB1).
istherebynonlinear: itwillrunMDsimulationsforeach
λ state in parallel. However, both the system initializa-
2. generate solvent: fetch or run the solvent genertion and the final free-energy calculation ought to occur
ation workflow (Sec. IIIB2).
only once. This is illustrated in Fig. 4 (d). Concretely,
3. solvate: solvate the solute using the GROMACS this is implemented by means of an aggregator function
gmx solvate program. decorator.

<!-- Page 6 -->

6
1. prepare system: Fetch or run the solute genera- 3. generate bilayer: fetch or run the phospholipidtion, solvent generation, and solute-in-solvent gen- bilayer generation workflow (Sec. IIIB5). (Aggreeration workflows. (Aggregated operation.) gated operation.)
2. production: Production MD simulation at a spe-
4. insert solute in box: use PACKMOL to place
cificλvalue,additionallyevaluatingandstoringthe
the solute in the bilayer box.
energyfromallinterpolatingHamiltonians,U ,for
λ
later use in the free-energy calculations.
5. convert box to gro: Convert PACKMOL’s output pdb file to gro format.
3. compute free energy: Compute the free energy
by means of the multi-Bennett acceptance ratio
6. update topology file: Combinethetopologyfiles
(MBAR)39 via the alchemlyb library.40 (Aggreof the solute and bilayer systems.
gated operation.)
The state-point parameters are the solute name, solvent 7. minimize energy minimization.
name, and Hamiltonian-coupling λ value.
8. equilibrate MD-based equilibration simulation.

## Phospholipid-bilayer generation 9. production Production MD simulation.

Here we consider the generation of a phospholipid bi- 10. compute WHAM: Use GROMACS’ implemenlayer (Fig. 4e). The implementation not only allows for tation of the weighted histogram analysis method
a variety of single-composition (Martini-supported) lipid (WHAM) to compute the PMF.43 (Aggregated
bilayers,italsosupportsthegenerationoflipidmixtures. function.)
1. generate initial bilayer: Generation of an ini- 11. analyze WHAM: Convert and store the GRO-
tial phospholipid-bilayer structure by means of the MACS WHAM output xvg files to numpy arrays.

### INSANE tool.41

2. minimize Energy minimization.

## Iv. Simulation Methods

3. equilibrate Equilibration MD simulation.
Moleculardynamics(MD)simulationswereperformed
4. production Production MD simulation.
with GROMACS 2023.1.44 Unless specified, we relied on
theMartini3force-fieldparameters8 withanintegration

### The relevant state-point parameters are the name and

time step of δt = 0.02 τ, where τ is the model’s natufractional composition of each phospholipid name.
ral unit of time. Simulations targeted an NPT ensemble: constant number of particles, pressure (P =1 bar),
and temperature (T =298 K). The latter was controlled

## Solute-in-bilayer umbrella sampling

by means of a stochastic velocity-rescaling thermostat.45
Equilibration MD simulations typically made use of the

### We consider the thermodynamics of insertion of a so-

Berendsen or C-rescale barostats, while production simlute molecule in a phospholipid bilayer (Fig. 4f). We
ulations relied on the more accurate, but also more sencompute the potential of mean force (PMF) by means of
sitive, Parrinello-Rahman barostat.46
umbrella sampling.42 We consider the PMF of insertion

### To generate solvent boxes, we used the PACKMOL

against a typical collective variable: the depth normal
program,38 and INSANE was used to generate phosphoto the bilayer, z. This last workflow is again a comlipid bilayers.41 Various tools of the GROMACS suite
bination of composability and state-point aggregation:
were used to generate gro structures and topology files,

### Composabilityofthesolutegeneration(Sec.IIIB1)with

solvate a solute, or run the weighted histogram analyphospholipid-bilayer generation (Sec. IIIB5); and statesis method (WHAM). Alchemical free energies were calpoint aggregation when collecting umbrella-sampling reculated by means of the multi-Bennett acceptance ratio
straints placed at various intervals of the collective vari-
(MBAR)39 via the alchemlyb library.40
able, z.

### Because of variations in the exact protocol used in the

1. generate solute: fetch or run the solute gener- various workflows, we refer the reader to the Martignac
ation workflow (Sec. IIIB1). (Aggregated opera- implementation or published NOMAD entries for more
tion.) detailed information. In particular, the full set of parsed
simulation input parameters can be easily browsed via
2. translate solute: move the solute to the origin of NOMAD’sMetaInfoviewer,foundunderthe“Data”tab
the simulation box. (Aggregated operation.) of each entry page.

<!-- Page 7 -->

7
V. RESULTS workflow by referencing the elementary upload ID. This
referencing of existing workflows enables a hierarchical
This section highlights a number of features enabled structure and reusability of simulations. We check that
by Martignac’s computational-workflow design. To ac- when running a high-throughput calculation of solutecompany the results, we systematically refer to the hy- in-a-solvent generation, a given chemistry for a solute is
perlinked NOMAD upload ID for easy access to each ever calculated and stored only once. Case in point: the
computationalworkflowandunderlyingsimulations. We alchemical calculation for the solute bead P6 in a homoalso provide a graphical user interface to the NOMAD geneous liquid of hexadecane is stored in a single upload
uploaded Martignac uploads in a web-based app on with (hyperlinked) ID PCQSjL2wQsCptzZhHal96Q. Every
Streamlit.47 The Streamlit app dynamically queries NO- λ-point simulation relies on the same solute system gen-
MAD, and features application-specific properties, such eration oT0F5qP9RY6AFDiDQrJ2ug, which is built from a
as the underlying DAG, free energies, and potentials of single solute generation, 7YU8feV SQ6h6M7aIUCdQg, and
mean force. a single solvent generation, uzssztc-SrGcz49GuSVlqQ.
A. The Martignac directed graph translates to NOMAD C. Reproducibility of oil/water transfer free energies
metadata

### Martignacfacilitatesreproducibilitybythesystematic

As a first example of the interaction between Mar- nature of its computational workflows. As a first examtignac and NOMAD, we consider the generation of a ple, we focus on oil/water transfer free energies. The rebox of hexadecane molecules—one of the standard Mar- cent Martini 3 force field provides an extensive reference
tini solvents. Fig. 5 (a) shows a DAG that is automati- of free-energy calculations as supporting information.8
cally generated by reading Martignac’s set of operations Parts of these reference thermodynamic calculations inand pre/post-conditions. The DAG contains all generic clude oil/water transfer free energies for the majority of
and application-specific operations. Though this DAG CG beads defined by the Martini model. Here we reprois linear, others in this work have non-trivial connectiv- duceasubsetofthesecalculationsbymeansoftheSoluteity, owing to loading several other workflows as part of in-solvent alchemical transformation workflow (Fig. 4d).
the early system setup, or aggregation of simulations for Because the workflow incorporates not only system genfree-energy calculations. eration and MD simulations, but also the calculations
IncomparisontotheMartignacDAG,wealsoshowin of the free energies themselves, these are straightforward
Fig.5(b)anillustrationoftheworkflowthatisgenerated to store as metadata in NOMAD. As such, we directly
and interpreted by NOMAD. NOMAD correctly identi- querythefreeenergiesfromNOMADtofetcheasily-and
fiesalloperations,andevendistinguishesoperationsthat permanently-available thermodynamic properties.
consist of MD simulations from the others. NOMAD’s
correct visualization of the workflow validates the pro- Solute Solvent Martignac Reference
grammatic transfer of the DAG into simulation meta- HD → W -27.45 -27.20

## Clf → W -11.98 -11.90

data. An example can be found for the (hyperlinked)

## P6 Eth → W -10.96 -11.20

NOMAD upload ID uzssztc-SrGcz49GuSVlqQ.

## Chex → W -18.86 -19.00


## W 17.98 18.00

B. Workflow composability TABLE I. Reproducibility of solute-in-solvent free energies
against the Martini 3 publication.8 Solvents with and with-
Avoiding unnecessary redundancies is an important outaright-pointingarrowdenotetransferandhydrationfree
featureofhigh-throughputcalculations,becausetheycan energies, respectively. All free energies in units of kJ/mol.
save significant compute and storage resources. For instance, the screening of the insertion of a solute in a sol- Tab. I shows a comparison of the free energies we obvent involves compounding combinatorics: each solute tain from Martignac, and the reference values from the
against each solvent. We avoid generating the same sys- Martini 3 study. Though the hydration free energy (i.e.,
tem twice by enforcing composability. Several workflows solvation in water) is readily calculated from Martignac,
start with the generation of the elementary parts, e.g., the other fields consist of transfer free energies from oil
soluteandsolventinasolute-in-solventsystem,orsolute to water. These are simply computed by subtracting the
and lipid bilayer in drug permeation. Each elementary two individual solvation free energies. All values are in
step reliesona “fetch-or-run” mechanism: wefirst check excellent agreement of one another, within 0.3 kJ/mol
whether the system has been previously run by means for each one of them. To further demonstrate the ability
of an API call. If so, we download it, otherwise, we run to fetch the free energies from the data directly, we refer
the system. If downloaded, Martignac locally stores the the reader to our Streamlit app, which fetches metadata
NOMAD upload ID of the elementary workflow. The from NOMAD to display the free energy resulting from
elementary workflow is included in the final NOMAD each computational workflow.47

<!-- Page 8 -->

8
FIG. 5. Workflow graph for solvent generation. (a) Workflow generated from Martignac. Color coding follows Fig. 2. (b)
Workflow generated from NOMAD. Green and dark-blue rectangles display operations, and distinguish those that involve an
MD simulation.
The NOMAD upload IDs for the alchem- prevents missing parameter information. Martignac upical calculations of P6 in the solvents HD, loads all simulation input and output files pertaining to
CLF, ETH, CHEX, and W are, respectively: eachPMFcalculationasasingleuploadtoNOMAD.As
PCQSjL2wQsCptzZhHal96Q, GAugbmarSJmlADe8rHK4AQ, the workflow also incorporates WHAM calculations, the
HKHmUObpQ a-SwaMVXvSeQ, w4sPShVOStm9Yc-bVuFvYw, resulting PMF curves are included in the NOMAD upand ZwcN37wMSyidNQeQPBQbAw. load. For the dimer and the trimer, the corresponding
NOMAD upload IDs are VpbwP6VpS4ucuwqVBHPzeg and
N51F6fmXRl6BHpNEQNBpTQ, respectively.
D. Reproducibility of drug-membrane potentials of mean
force 10
As a second example of reproducibility, we consider 0
the potentials of mean force (PMFs) of small Martini
molecules inserted into a phospholipid bilayer. We perform PMF calculations for the C1–P4 dimer and SC1– 10
−
SP2–SC1 trimer in a 1-palmitoyl-2-oleoyl-sn-glycero-3-
phosphocholine(POPC)bilayer,foundoriginallyinHoff-
20
mann et al.31 and Potter et al.,48 respectively. Both −
studiesrelyontheMartini2forcefield.7,49,50 ThePMFs
are calculated using the Solute-in-bilayer umbrella sam- 30
−
pling workflow (Fig. 4f). Fig. 6 shows the original 0.0 0.5 1.0 1.5 2.0 2.5 3.0 3.5 4.0

### Distancetobilayercenter z /nm

and Martignac PMFs in dashed and solid lines, respectively. The PMFs of the C1–P4 dimer show excellent
agreement, with only a slight deviation around the first
bead of the lipid tail region. As Hoffmann et al. provided simulation input files, reproducing the simulations
was straightforward. The update to a more recent version of GROMACS together with statistical convergence
likely explain the slight variations between the PMFs.
For the SC1–SP2–SC1 trimer, the Martignac PMF generally matches the result of the original study, but is
slightly shifted down due to deviations in the water region (z ≳ 2.6nm) used as the zero reference. Although

### Potter et al. do not provide simulation input files, they

include all essential parameters in their method description. We utilized their specified parameters in conjunction with defaults for the unspecified parameters.

### However, in contrast to extracting parameters from the

method description, providing a complete input file facilitates the reproduction of a simulation and generally
1 −lomJk/FMP

### C1-P4dimer


### SC1-SP2-SC1trimer

FIG. 6. Drug-membrane potentials of mean force (PMFs)
for a C1–P4 dimer and an SC1–SP2–SC1 trimer inserted
in a POPC bilayer. Solid and dashed lines correspond to
Martignac and the original studies,31,48, respectively. Error
estimates from bootstrapping (not available for the original
trimer result) are shown as (relatively small) shaded areas.
We now consider the reproducibility of polyethylene,
mapped to a C1–C1 dimer, in a POPC membrane
from Bochicchio et al.51 As the original study did not
provideallessentialsimulationparameters, wecouldnot
precisely reproduce the simulation setup. While relevant
parameters for the umbrella sampling, the temperature
coupling, and the barostat are specified, information
about the treatment of non-bonded interactions is
missing. We investigate the impact of different methods
for handling electrostatic and van der Waals (VdW)

<!-- Page 9 -->

9
interactions on the resulting PMFs. Fig. 7 shows the
resultfromtheoriginalstudytogetherwithfivedifferent
variants obtained with the Martignac workflow. The
NOMAD upload IDs are ordered from top to bottom:
UkYrTZTDRUG0rTpsuJzd7Q, Eiatr72XQu6X03u0w6Tl5A,
4x-JwH IQIqqHevHf5LABQ, owgFZkssRd6kttrlKitsTQ,
and XmFAOFG1Q3qd7KDBsF9mCw. While various methods
for handling electrostatic interactions do not significantly impact the PMF curve, the VdW treatment
causes greater differences in our results. Despite testing
multiple parameters for treating non-bonded interactions, we unfortunately could not reproduce the result
from Bochicchio et al. Notably, our PMF from simulations using a VdW cutoff are in excellent agreement
with the C1–C1 dimer results from Hoffmann et al.31
Additionally, our PMF more closely resembles the atomistic calculation provided as part of the original study.51

### In particular, the PMF peak near the membrane–water

interfaceisclosertothebilayercenterfortheiratomistic
result, aligning more closely with our findings. In
general, the discrepancies observed may be attributed
to factors such as unsatisfactory simulation convergence
or further differences in the simulation setup. For
instance, the use of the polarizable water model might
shift the membrane thickness, but it is unfortunately
not supported by Martignac at the moment. Overall
this makes a strong point for the broad and systematic
use of FAIR data storage for molecular simulations.
10
0
10
−
20
−
30
−
0.0 0.5 1.0 1.5 2.0 2.5 3.0 3.5 4.0
Distancetobilayercenter z /nm
1
−lomJk/FMP

### NOMAD database to list all systems correponding to

a Martignac workflow. In Fig. 8, we show the solutein-bilayer umbrella sampling subpage of the app. The
toppartofthefiguredisplaystheMartignacDAG,highlighting the branching upon system generation. Further,
the bottom part shows a list of systems found in the
database. For each, various information extracted from
the NOMAD entry are reported. Notably, this enables
us to report and display simulation outputs: here the
app systematically constructs the PMF of the workflow.
Such online, interactive, and visually appealing aspects
are likely to promote FAIR molecular-simulation data
storage.
Bochicchioetal.

### Coulomb VdW

Cutoff Shift

### PME Shift

RF Shift FIG.8. SnapshotoftheStreamlitwebapp. Top: Illustration
RF Cutoff of the solute-in-bilayer umbrella sampling. Bottom: systems
Cutoff Cutoff found in the NOMAD database OtN- 2jSv6fs7fg7o0 w.
The query fetches the results of the WHAM calculations to
automatically display the PMFs in small format.
FIG. 7. Comparison of multiple computations of drugmembrane potentials of mean force (PMFs) for a C1–C1

## Vi. Conclusion

dimer inserted in a POPC bilayer with results reported by
Bochicchio et al.51 We employed various combinations of

### WeintroduceMartignac: computationalworkflowsfor

methods to address electrostatic (Coulomb) and van der
Waals (VdW) interactions as implemented in GROMACS. thecoarse-grained(CG)Martinibiomolecularforcefield.
ResultsusingthesameVdWinteractionhandlingoverlapal- LegacyBashscriptswitherror-pronecopy/pastingmake
most entirely due to excellent agreement. We show error es- way for a more robust approach by means of workflows.
timatesfrombootstrappingas(realtivelysmall)shadedareas The set of operations relevant to a particular objective
for our simulation results. (e.g.,generatingaboxofsolventorcalculatingafreeenergy) are connected in an acyclic directed graph (DAG).
A notable benefit of storing simulation worfklows on- The DAG links said operations to offer a traceable hisline is the ability to both query and display scientific tory fromsystemgeneration,toMDsimulations,toanalinformation in a user-friendly fashion—here illustrated ysis and estimation of material/thermodynamic properwith the Martignac Streamlit app.47 The app queries a ties. The history offers anyone the ability to inspect,

<!-- Page 10 -->

10
check, and reproduce the content at each step. More- motte,etal.,“Sharingdatafrommolecularsimulations,”Journal
over,thedefinitionofelementaryworkflowsenablestheir ofchemicalinformationandmodeling59,4093–4099(2019).
composability: separating system generation from fur- 2P. Andrio, A. Hospital, J. Conejero, L. Jord´a, M. Del Pino,
L. Codo, S. Soiland-Reyes, C. Goble, D. Lezzi, R. M. Badia,
ther analysis means that a single instance of the former
et al., “Bioexcel building blocks, a software library for interopcan be applied to a variety of downstream calculations.
erablebiomolecularsimulationworkflows,”Scientificdata6,169
Here, we not only separate system generation from free- (2019).
energy calculations, we split system generation in terms 3TheMolecularSciencesSoftwareInstitute(MolSSI)andBioExof their basic components: solutes, homogeneous liquids, cel, “COVID-19 Molecular Structure and Therapeutics Hub,”
https://covid.molssi.org/,accessed: 2024-08-06.
andlipidbilayers. WeshowthatMartignacgreatlyfacil-
4J.K.Tiemann,M.Szczuka,L.Bouarroudj,M.Oussaren,S.Garitates both reproducibility and composability by means cia, R. J. Howard, L. Delemotte, E. Lindahl, M. Baaden,
of several examples pertaining to oil/water transfer free K.Lindorff-Larsen,etal.,“Mdverse: Sheddinglightonthedark
energies and drug-membrane thermodynamics. matterofmoleculardynamicssimulations,”eLife12(2023).
5G. Gygli and J. Pleiss, “Simulation foundry: Automated and

### ThedeepinterconnectionbetweenMartignacandNO-

fair molecular modeling,” Journal of chemical information and
MAD carries interesting benefits. First, the systematic
modeling60,1922–1927(2020).
pulling of existing workflows greatly improves sustain- 6R.Amaro,J.˚Aqvist,I.Bahar,F.Battistini,A.Bellaiche,D.Belability: the community can download existing Martini tran,P.C.Biggin,M.Bonomi,G.R.Bowman,R.Bryce,et al.,
simulations, insteadofsimulatingthem(again). Theau- “The need to implement fair principles in biomolecular simulations,”arXivpreprintarXiv:2407.16584 (2024).
tomatic pushing of missing workflows removes any fric-
7S. J.Marrink, H. J. Risselada, S. Yefimov, D.P. Tieleman,and
tion or efforts associated with publishing MD simula- A. H. De Vries, “The martini force field: coarse grained model
tions. In this way, the user helps the community by forbiomolecularsimulations,”Thejournalofphysicalchemistry
enriching the corpus of Martini simulations available on- B111,7812–7824(2007).
8P.C.Souza,R.Alessandri,J.Barnoud,S.Thallmair,I.Faustino,
line. Finally, we find that publishing entire computa-
F. Gru¨newald, I. Patmanidis, H. Abdizadeh, B. M. Bruininks,
tional workflows offers a solution to the recent increase
T. A. Wassenaar, et al., “Martini 3: a general purpose force
in the volume of scientific articles’ supplementary infor- field for coarse-grained molecular dynamics,” Nature methods
mation: all relevant data and metadata is stored and 18,382–388(2021).
accessible in the NOMAD entries. 9M.Uhrin,S.P.Huber,J.Yu,N.Marzari,andG.Pizzi,“WorkflowsinAiiDA:Engineeringahigh-throughput,event-baseden-
The connection to NOMAD also means that all simugineforrobustandmodularcomputationalworkflows,”Compulationmetadata ispersistentlyavailableonline. We refer
tationalMaterialsScience187,110086(2021).
the reader to the Martignac Streamlit app.47 The app 10C.S.Adorf,P.M.Dodd,V.Ramasubramani,andS.C.Glotzer,
fetches all published Martignac simulations. The con- “Simpledataandworkflowmanagementwiththesignacframenection to the NOMAD API means that the entries are work,”ComputationalMaterialsScience146,220–229(2018).
11V.Ramasubramani,C.Adorf,P.Dodd,B.Dice,andS.Glotzer,
constantly updated with added simulations. Similar to
“signac: A python framework for data and workflow manage-
MDverse, the app offers an intuitive user interface to ment,” in Proceedings of the Python in Science Conference
browse through simulations. The added benefit of Mar- (2018).
tignac is the access to the simulation metadata, allowing 12Y.Zhou,R.K.Cersonsky,andS.C.Glotzer,“Aroutetohierarchical assembly of colloidal diamond,” Soft Matter 18, 304–311
us to automatically sort between workflows and extract
(2022).
scientifically meaningful information, such as free ener- 13R. K. Cersonsky, J. Antonaglia, B. D. Dice, and S. C. Glotzer,
gies. Looking ahead, the incorporation of workflows for “The diversity of three-dimensional photonic crystals,” Nature
more biomolecular simulations of interest is straightfor- communications12,2543(2021).
ward, and will further help move the field to more sys- 14A.Z.Summers, J.B.Gilmer, C.R.Iacovella, P.T.Cummings,
and C. McCabe, “Mosdef, a python framework enabling largetematic practices.
scale computational screening of soft matter: Application to
chemistry-propertyrelationshipsinlubricatingmonolayerfilms,”
Journal of Chemical Theory and Computation 16, 1779–1793
(2020).

## Acknowledgments

15C. D. Quach, J. B. Gilmer, D. Pert, A. Mason-Hogans, C. R.

### Iacovella, P. T. Cummings, and C. McCabe, “High-throughput

WethankBrandonButlerandCorwinKerrfordiscus- screening of tribological properties of monolayer films using
molecular dynamics and machine learning,” The Journal of
sion about the signac workflow library. T.B. acknowl-
ChemicalPhysics156(2022).
edges support by the Deutsche Forschungsgemeinschaft
16MoSDeF,“MolecularSimulationDesignFramework(MoSDeF),”
(DFG, German Research Foundation) under Germany’s https://mosdef.org/index.html,accessed: 2024-08-06.
Excellence Strategy EXC 2181/1 - 390900948 (the Hei- 17M.W.Thompson,J.B.Gilmer,R.A.Matsumoto,C.D.Quach,
delberg STRUCTURES Excellence Cluster). J.F.R.’s P. Shamaprasad, A. H. Yang, C. R. Iacovella, C. McCabe, and
P.T.Cummings,“Towardsmolecularsimulationsthataretranscontribution was funded by the NFDI consortium FAIR-
parent, reproducible, usable by others, and extensible (true),”
mat-DeutscheForschungsgemeinschaft(DFG)-Project
Molecularphysics118,e1742938(2020).

## Icons on figure 1 made by Freepik and Haca 18M. D. Wilkinson, M. Dumontier, I. J. Aalbersberg, G. Apple-

Studio from www.flaticon.com. ton, M. Axton, A. Baak, N. Blomberg, J.-W. Boiten, L. B.
daSilvaSantos,P.E.Bourne,etal.,“Thefairguidingprinciples
forscientificdatamanagementandstewardship,”Scientificdata
1M.Abraham,R.Apostolov,J.Barnoud,P.Bauer,C.Blau,A.M.
3,1–9(2016).
Bonvin, M. Chavent, J. Chodera, K. Cˇondi´c Jurki´c, L. Dele-

<!-- Page 11 -->

11
19T. Tanhua, S. Pouliquen, J. Hausman, K. O’brien, P. Bricher, 36MARTIGNAC, “Martignac: Coarse-grained Martini simulation
T. De Bruin, J. J. Buck, E. F. Burger, T. Carval, K. S. Casey, worfklows,” https://tbereau.github.io/martignac/, accessed:
et al.,“Oceanfairdataservices,”FrontiersinMarineScience6, 2024-09-23.
440(2019). 37Martini, “Martini: General Purpose Coarse-Grained
20N. Jeliazkova, M. D. Apostolova, C. Andreoli, F. Barone, Force Field,” http://www.cgmartini.nl/index.php/
A. Barrick, C. Battistelli, C. Bossa, A. Botea-Petcu, A. Chˆatel, force-field-parameters,accessed: 2024-08-06.
I. De Angelis, et al., “Towards fair nanosafety data,” Nature 38L. Mart´ınez, R. Andrade, E. G. Birgin, and J. M. Mart´ınez,
Nanotechnology16,644–654(2021). “Packmol: A package for building initial configurations for
21T. J. Jacobsson, A. Hultqvist, A. Garc´ıa-Fern´andez, A. Anand, molecular dynamics simulations,” Journal of computational
A.Al-Ashouri,A.Hagfeldt,A.Crovetto,A.Abate,A.G.Riccia- chemistry30,2157–2164(2009).
rdulli,A.Vijayan,etal.,“Anopen-accessdatabaseandanalysis 39M. R. Shirts and J. D. Chodera, “Statistically optimal analytoolforperovskitesolarcellsbasedonthefairdataprinciples,” sisofsamplesfrommultipleequilibriumstates,”TheJournalof
NatureEnergy7,107–115(2022). chemicalphysics129(2008).
22NOMAD,“NOMADHomepage,”https://nomad-lab.eu(),ac- 40O.Beckstein,D.L.Dotson,Z.Wu,D.Wille,D.Marson,I.Kencessed: 2024-08-06. ney, shuail, H. Lee, trje3733, V. Lim, A. Schlaich, I. Alibay,
23C. Draxl and M. Scheffler, “Nomad: The fair concept for big J.H´enin,M.S.Barhaghi,P.Merz,T.Joseph,W.-T.Hsu,helmut
data-drivenmaterialsscience,”MrsBulletin43,676–682(2018). carter,andhl2500,“alchemistry/alchemlyb: 2.3.1,” (2024).
24C. Draxl and M. Scheffler, “The nomad laboratory: from data 41T.A.Wassenaar,H.I.Ing´olfsson,R.A.Bockmann,D.P.Tielesharing to artificial intelligence,” Journal of Physics: Materials man,andS.J.Marrink,“Computationallipidomicswithinsane:
2,036001(2019). a versatile tool for generating custom membranes for molecular
25M. Scheffler, M. Aeschlimann, M. Albrecht, T. Bereau, H.-J. simulations,” Journal of chemical theory and computation 11,
Bungartz, C. Felser, M. Greiner, A. Groß, C. T. Koch, K. Kre- 2144–2155(2015).
mer, et al., “Fair data enabling new horizons for materials re- 42G.M.TorrieandJ.P.Valleau,“Nonphysicalsamplingdistribusearch,”Nature604,635–642(2022). tionsinmontecarlofree-energyestimation: Umbrellasampling,”
26M.Scheidgen,L.Himanen,A.N.Ladines,D.Sikter,M.Nakhaee,
Journalofcomputationalphysics23,187–199(1977).
A´. Fekete, T. Chang, A. Golparvar, J. A. Ma´rquez, S. Brock- 43S. Kumar, J. M. Rosenberg, D. Bouzida, R. H. Swendsen, and
hauser, et al., “Nomad: A distributed web-based platform for P. A. Kollman, “The weighted histogram analysis method for
managing materials science research data,” Journal of Open free-energycalculationsonbiomolecules.i.themethod,”Journal
SourceSoftware8,5388(2023). ofcomputationalchemistry13,1011–1021(1992).
27K. H. Kanekal and T. Bereau, “Resolution limit of data-driven 44M. J. Abraham, T. Murtola, R. Schulz, S. Pa´ll, J. C. Smith,
coarse-grainedmodelsspanningchemicalspace,”TheJournalof B. Hess, and E. Lindahl, “Gromacs: High performance molecchemicalphysics151(2019). ular simulations through multi-level parallelism from laptops to
28T.Bereau,“Computationalcompoundscreeningofbiomolecules
supercomputers,”SoftwareX1,19–25(2015).
andsoftmaterialsbymolecularsimulations,”ModellingandSim- 45G. Bussi, D. Donadio, and M. Parrinello, “Canonical sampling
ulationinMaterialsScienceandEngineering29,023001(2021). throughvelocityrescaling,”TheJournalofchemicalphysics126
29P. C. Souza, S. Thallmair, P. Conflitti, C. Ram´ırez-Palacios, (2007).
R. Alessandri, S. Raniolo, V. Limongelli, and S. J. Marrink, 46M.ParrinelloandA.Rahman,“Polymorphictransitionsinsingle
“Protein–ligandbindingwiththecoarse-grainedmartinimodel,” crystals: Anewmoleculardynamicsmethod,”JournalofApplied
Naturecommunications11,3714(2020). physics52,7182–7190(1981).
30R.Menichetti,K.H.Kanekal,andT.Bereau,“Drug–membrane 47TristanBereau,“MartignacStreamlitapp,”https://martignac.
permeabilityacrosschemicalspace,”ACScentralscience5,290– streamlit.app/,accessed: 2024-08-22.
298(2019). 48T.D.Potter,E.L.Barrett,andM.A.Miller,“Automatedcoarse-
31C.Hoffmann,A.Centi,R.Menichetti,andT.Bereau,“Molecugrainedmappingalgorithmforthemartiniforcefieldandbenchlardynamicstrajectoriesfor630coarse-graineddrug-membrane marks for membrane–water partitioning,” Journal of Chemical
permeations,”ScientificData7,51(2020). TheoryandComputation17,5777–5791(2021).
32A.Centi,A.Dutta,S.H.Parekh,andT.Bereau,“Insertingsmall 49S.J.Marrink,A.H.deVries,andA.E.Mark,“Coarsegrained
moleculesacrossmembranemixtures: Insightfromthepotential model for semiquantitative lipid simulations,” The Journal of
ofmeanforce,”BiophysicalJournal118,1321–1332(2020). PhysicalChemistryB108,750–760(2003).
33B.Mohr,K.Shmilovich,I.S.Kleinw¨achter,D.Schneider,A.L. 50D. H. de Jong, G. Singh, W. F. D. Bennett, C. Arnarez, T. A.
Ferguson,andT.Bereau,“Data-drivendiscoveryofcardiolipin- Wassenaar, L. V. Sch¨afer, X. Periole, D. P. Tieleman, and S. J.
selective small molecules by computational active learning,” Marrink, “Improved parameters for the martini coarse-grained
ChemicalScience13,4498–4511(2022). protein force field,” Journal of Chemical Theory and Computa-
34NOMAD, “NOMAD How-to guides,” https://nomad-lab.eu/ tion9,687–697(2012).
prod/v1/docs/index.html(),accessed: 2024-08-06. 51D. Bochicchio, E. Panizon, R. Ferrando, L. Monticelli, and
35marshmallow, “marshmallow: simplified object serialization,” G.Rossi,“Calculatingthefreeenergyoftransferofsmallsolutes
https://marshmallow.readthedocs.io/en/stable/index.html, intoamodellipidmembrane: Comparisonbetweenmetadynamaccessed: 2024-07-22. icsandumbrellasampling,”TheJournalofchemicalphysics143
(2015).

## Tables

**Table (Page 8):**

|  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
|  |  |  |  | S |  |  |  |  |
|  |  |  |  |  | S | C1-P4d C1-SP | imer 2-SC1 | trimer |


**Table (Page 9):**

|  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  | Boch | icchioe | tal. |
|  |  |  |  |  |  | Coul Cuto | omb ff | VdW Shift |
|  |  |  |  |  |  | PME RF |  | Shift Shift |
|  |  |  |  |  |  | RF Cuto | ff | Cutoff Cutoff |
