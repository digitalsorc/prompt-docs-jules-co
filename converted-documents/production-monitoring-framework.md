---
title: "Production Monitoring Framework"
original_file: "./Production_Monitoring_Framework.pdf"
document_type: "guide"
conversion_date: "2025-11-29"
topics: ["rag", "react", "fine-tuning", "evaluation", "multimodal"]
keywords: ["state", "experimental", "feature", "dynamics", "electron", "signatures", "diffraction", "time", "fig", "iam"]
summary: "<!-- Page 1 -->

Imaging the Photochemistry of Cyclobutanone using Ultrafast Electron

### Diffraction: Experimental Results

A. Wolf1,4,a)
1)Stanford PULSE Institute, SLAC National Accelerator Laboratory, 2575 Sand Hill Road, Menlo Park, CA 94025,

## Usa. 2)EaStCHEM School of Chemistry, University of Edinburgh, Edinburgh EH9 3FJ, U.K."
related_documents: []
---

# Production Monitoring Framework

<!-- Page 1 -->

Imaging the Photochemistry of Cyclobutanone using Ultrafast Electron

### Diffraction: Experimental Results

A. E. Green,1,2,3 Y. Liu,4 F. Allum,1 M. Graßl,1,4 P. Lenzen,1 M. N. R. Ashfold,5 S. Bhattacharyya,4 X. Cheng,4
M. Centurion,6 S. W. Crane,7 R. Forbes,4,8 N. A. Goff,7 L. Huang,7 B. Kaufman,4 M. F. Kling,1,4,9 P. L.
Kramer,4 H. V. S. Lam,10 K. A. Larsen,4 R. Lemons,4 M.-F. Lin,4 A. J. Orr-Ewing,5 D. Rolles,10 A. Rudenko,10
S. K. Saha,10 J. Searles,10 X. Shen,4 S. Weathersby,4 P. M. Weber,7 H. Zhao,6 and T. J. A. Wolf1,4,a)
1)Stanford PULSE Institute, SLAC National Accelerator Laboratory, 2575 Sand Hill Road, Menlo Park, CA 94025,

## Usa.

2)EaStCHEM School of Chemistry, University of Edinburgh, Edinburgh EH9 3FJ, U.K.
3)European XFEL, Holzkoppel 4, 22869 Schenefeld, Germany
4)Linac Coherent Light Source, SLAC National Accelerator Laboratory, 2575 Sand Hill Road, Menlo Park, CA

## 94025, Usa.

5)School of Chemistry, University of Bristol, Bristol BS8 1TS, U.K.
6)Department of Physics and Astronomy, University of Nebraska -Lincoln, Lincoln, NE 68588, USA
7)Department of Chemistry, Brown University, Providence, RI 02912, USA.
8)Department of Chemistry, University of California, Davis, One Shields Avenue, Davis, CA 95616, USA.
9)Applied Physics Department, Stanford University, 348 Via Pueblo, Stanford, CA 94305, USA.
10)Department of Physics, Kansas State University, Manhattan, KS 66506, USA.
(Dated: 15 April 2025)
We investigated the ultrafast structural dynamics of cyclobutanone following photoexcitation at λ=200 nm
usinggas-phasemegaelectronvoltultrafastelectrondiffraction. Ourinvestigationcomplementsthesimulation
studies of the same process within this special issue. It provides information about both electronic state
populationandstructuraldynamicsthroughwell-separableinelasticandelasticelectronscatteringsignatures.
We observe the depopulation of the photoexcited S state of cyclobutanone with n3s Rydberg character
2
throughitsinelasticelectronscatteringsignaturewithatimeconstantof(0.29±0.2)pstowardstheS state.
1
TheS statepopulationundergoesring-openingviaaNorrishType-Ireaction, likelywhilepassingthrougha
1
conicalintersectionwithS . Thecorrespondingstructuralchangescanbetrackedbyelasticelectronscattering
0
signatures. These changes appear with a delay of (0.14±0.05) ps with respect to the initial photoexcitation,
whichislessthantheS depopulationtimeconstant. Thisbehaviorprovidesevidencefortheballisticnature
2
ofthering-openingoncetheS stateisreached. Theresultingbiradicalspeciesreactfurtherwithin(1.2±0.2)
1
ps via two rival fragmentation channels yielding ketene and ethylene, or propene and carbon monoxide. Our
study showcases both the value of gas-phase ultrafast diffraction studies as an experimental benchmark for
nonadiabatic dynamics simulation methods and the limits in the interpretation of such experimental data
without comparison to such simulations.
I. INTRODUCTION calreactionmechanismsinvolvingsuchnonadiabaticdynamics. Due to the absence of an environment and the
Ultrafast dynamics in the excited states of organic resulting limited complexity of the system, experimental
molecules are well-known as key processes in many pho- observables can provide a detailed picture of the investochemicalreactions. Exampleswithbiologicalrelevance tigated process. Such studies also provide the opporare the photosynthesis reactions in plants1 and the pri- tunity for a direct comparison with the results of high
mary reaction in the human vision process.2 The un- level quantum chemical simulations of the nonadiabatic
derlying mechanisms of ultrafast charge and energy flow dynamics.4 This combination of experimental and simuare still not fully understood due to the molecular com- lation approaches is now well-established.5–20 It has the
plexity, compounded by the involvement of the poten- potential to lead to the development of a predictive untial energy surfaces of multiple electronic states. Ad- derstandingofultrafastphotochemicaldynamicsandthe
ditionally, population transfer between these states of- eventual control of reactive outcomes through the develten involves nonadiabatic dynamics through conical in- opmentofstructure-functionrelationshipsasdesignprintersections,wheretheBorn-Oppenheimerapproximation ciples for photochemistry.
is invalid.3 The development of such structure-function relation-
Studiesofisolated,smallorganicmodelsystemsinthe ships will require the exploration of large parameter
gasphasehaveemergedasapromisingapproachtogain- spaces, which is unfeasible by only experiments, given
ingafundamentalunderstandingofgeneralphotochemi- therequiredeffortforeachexperimentandtypicalexperimental cycles of months and years from their preparationtotheunderstandingandverificationoftheirresults.

### Instead, the majority of the survey of parameter spaces

a)thomas.wolf@slac.stanford.edu for structure-function relationships could be performed
5202
rpA
41
]hp-mehc.scisyhp[
2v65931.2052:viXra

<!-- Page 2 -->

2
in silico by quantum chemical simulations. However,
the accuracy of electronic structure methods for excited
states is in general lower than for the electronic ground
state. Additionally, thespecificlimitsandvalidityofthe
largenumberofavailablemethodsforcalculatingexcited
stateelectronicstructureandforpropagatingthenuclear
wavepacketonandbetweenexcitedstatesarelargelyunderexplored, except for a limited number of studies.21,22
Therefore, there is a clear need for dedicated efforts to
benchmark these simulation approaches.

### Akeyaspectofsuchbenchmarkstudiesisthechoiceof

the experimental observable, which needs to fulfill three
requirements: (1) It must provide meaningful informationaboutanimportantaspectoftheinvestigatedultrafastprocess,e.g. thelifetimeofaspecificexcitedstateor

### FIG. 1. Overview of possible intermediate and fragment

thetimescaleofabonddissociation. (2)Itmustbeinterstructures generated by cyclobutanone photolysis. Cyclobupretable without extensive theory input, to allow for an
tanone (left) can react via a Norrish Type-I reaction to form
independent experimental result. (3) It must be accessi- aring-openedbiradicalproduct(geometrytakenfromref.30).
blebysimulationswithhighfidelity. Otherwise,ambigu- This primary biradical compound can react further via three
itiescanariseinthecaseofdisagreementsbetweenexper- possible secondary dissociation channels, (1) to ketene and
imental and simulation results, as it is unclear whether ethylene,(2)carbonmonoxideandpropene,orto(3)carbon
the disagreement originates from an artifact in the sim- monoxide and cyclopropane.31–36 Examples for atomic disulation of the observable or from the underlying excited tances in the first (gold), second (blue), third (brown), and
state dynamics simulation. fourth(purple)coordinationspheresareshownbycolor-coded
lines. Carbonatomsareshownindarkgray,oxygenatomsin
UltrafastX-rayandelectrondiffraction23,24enabledby
red, and hydrogen atoms in light gray.
X-ray free electron lasers25 and novel electron sources26
are powerful techniques capable of generating valuable
new experimental observables.24 (1) Diffraction is selectivelysensitivetothemotionofthenuclei,providingun- bonyl group via hydrogen atom transfer, and roamingambiguous signatures e.g. from dissociation or isomer- type reactions.53,54
ization reactions. (2) Diffraction signatures can be in- This chemistry is triggered in the atmosphere by photuitively interpreted by transformation into real space. toabsorption into broad, weak bands peaking at λ≈280
The resulting atomic pair distribution functions (PDFs) nm.52 The bands correspond to weak transitions to exdirectly show relative motion of atoms as changes in cited states characterized by a single electron transition
distance-dependent pair density. (3) Diffraction can be from a carbonyl oxygen lone pair (n) orbital to the carsimply simulated with a high level of fidelity within the bonyl π∗ orbital (nπ∗ character). Their relevance for
independent atom model (IAM).5–8 the tropospheric chemistry of organic carbonyls despite
The IAM treats the atoms in a molecule as non- their weak absorption cross-sections comes from the fact
interacting, neglecting any distortion of the atomic that the long wavelength tail overlaps with the short
valence electron distribution from chemical bonding. wavelength end of the solar spectrum that reaches the
Therefore, IAM diffraction signatures can be simu- troposphere. However, similar photochemical processes
lated with minimal computational effort using a molec- can also be triggered by excitation to Rydberg states at
ular geometry and tabulated or computed scattering λ ≈ 200 nm with significantly larger absorption crossform factors. In cases where the IAM is not accurate section.32,55
enough,13,19,20,27 powerful approaches have been devel- The molecule cyclobutanone (CB) has a number of faoped to simulate the diffraction observable from the ex- vorable characteristics for use as a model system in a
plicitelectrondensitydistribution,whichcanbeobtained study focusing on the structural dynamics involved in
from an electronic structure calculation.28,29 carbonyl photochemistry: (1) It is a comparably small
Therefore, UED is an ideal observable for the present quantum system and is thus accessible to detailed study
study, which serves as the experimental complement to by contemporary high level quantum chemical methods.
thesimulationstudiespublishedinthisspecialissue.37–51 (2)Itsrigidstructurewiththestrainofafour-membered
We target the ultrafast photochemistry of organic car- ring provides a well-defined starting geometry for the rebonyls, which are important species in atmospheric action. (3) The ring structure prevents the formation of
chemistry.52 They exhibit rich photochemistry, includ- the conformations necessary for a hydrogen atom transing Norrish Type-I reactions leading to the dissociation fer to the carbonyl oxygen, which is the initial step of
of a carbon-carbon bond adjacent to the carbonyl group the Norrish Type-II reaction. Therefore, the dynamics
(see Fig. 1), Norrish Type-II reactions leading to cleav- are constrained to the Norrish Type-I pathway. (4) The
age of a carbon-carbon bond two removed from the car- NorrishType-Ireactioncorrespondstoanopeningofthe

<!-- Page 3 -->

3
four-membered ring, which provides clear and character- 0.74 ps for the parent, and 0.12 ps and 0.79 ps for the
istic diffraction signatures. (5) Its vapor pressure is high fragment, respectively. The time-resolved photoelectron
enough to make it accessible to a broad set of gas-phase spectroscopystudyidentifiedasignaturedisplayingabitime-resolved experimental methods exponentialdecaywithtimeconstantsof0.31psand0.74
TheCBmolecule(C H O)isnotcompletelyplanarin ps, suggesting depopulation of the n3s state on an ultra-
4 6
its ground state. Instead, the carbonyl bond is slightly fast timescale via internal conversion to the nπ∗ state.
bent out of the ring-plane reducing the symmetry to The decay of the photoelectron signature was observed
C .56–58 Themajorityofstudiesofthephotochemistryof tobemodulatedbothinpositionandintensitybyanoss
CB focus on its reactivity after excitation to the weakly cillatorycomponentwithaperiodof0.94ps,whichcould
absorbing nπ∗ state. Photolysis studies31–33,59 identified be associated with motion along a ring-puckering mode
three different fragmentation channels (see Fig. 1) pro- in the n3s state.65
ducing ethylene and ketene The evidence for ultrafast nonadiabatic dynamics betweenstatesofdifferentelectroniccharacterandtherich

## C H O →C H +Ch Co (1)

4 6 2 4 2 photochemistry,withseveralintermediatesandproducts,
makeCBanidealbenchmarkmoleculeforachallengefor
or carbon monoxide and either propene
theoreticianstopredictnon-adiabaticphotochemicaldy-
C H O →C H +CO (2) namics in advance of an experiment, as pursued in this
4 6 3 6
special issue.37–51
or cyclopropane Thus, the purpose of this study is to provide (1) an
experimental benchmark to the predictions published in

### C H O →cC H +CO. (3)

4 6 3 6 this special issue and (2) information about the mechanismandtimescaleofthephotochemicalreactiondynam-
Some of these photolysis studies32,33,59 suggest that the
ics of CB following photoexcitation. In the following, we
propene products (channel 2) arise via acyclization of
will discuss the results of our UED study of the phothe cyclopropane products generated in channel 3. The
tochemical dynamics of CB after excitation to the n3s
photochemistry triggered by nπ∗ excitation was also the
state at λ = 200 nm. Since our study is the experimensubject of a number of time-resolved mass spectrometry
tal complement to the companion simulation studies, we
studies from the Zewail group34,35,60 and a recent invesseek to isolate the analysis of the experimental data as
tigation in the solution phase using transient absorption
much as possible from the simulation results. Therefore,
spectroscopy.36
we will use only a basic level of quantum chemical cal-
The mechanistic picture of the photofragmentation
culations(geometryoptimizationsinthegroundstateat
fromthephotolysisandtime-resolvedspectroscopystudthe density functional theory (DFT) level) resulting in
ies is not completely clear, since both fragmentation
an interpretation of the experimental results, which is
via a Norrish Type-I reaction31–36 yielding a biradical
independent from more extensive simulations.
intermediate (see Fig. 1) and direct fragmentation via
concerted cleavage of two C-C bonds60 have been proposed. Thetwomechanismscouldnotbeunambiguously
differentiated by the time-resolved mass-spectrometry II. METHODS
studies,34,35,60 since they were unable to determine if
the observed ion fragments derived from neutral prod- The experiment is carried out at the SLAC megaucts formed before interaction with the photoionizing electronvoltultrafastelectrondiffractionfacility.26,66The
probe, or from fragmentation in the cations formed by setup for gas-phase ultrafast electron diffraction experiphotoionization.61 ments at the facility is described in detail in Refs.66,67.
Photolysis by excitation of the n3s Rydberg state at In short, we separate the output of a 800 nm, 50 fs
λ = 193 nm62 results in similar fragmentation channels Ti:Sapphire laser system into two beam paths. The
as observed after excitation of the nπ∗ state, suggesting pulses of the probe beam path are frequency tripled and
that population in the n3s state can access the nπ∗ state directed onto the photocathode of an S-band radio freviainternalconversioninaccordwithexpectationsbased quency(RF)gun. Theyejectanultrashortpulsecontainon Kasha’s rule.63 The relative yields from the fragmen- ing ≈ 104 electrons, which are subsequently accelerated
tation channels 2 and 3 were measured after photolysis to 4.3 MeV and focused to a spot size of 200 µm full
at200nmwithhydrogenflamedetectionanddetermined width at half maximum (FWHM) in the interaction reto be 2.4:1.32 gionofagas-phaseexperimentalchamber. Thepulsesof
The ultrafast dynamics of CB after excitation at λ = the second, pump beam path are frequency quadrupled
200nmhavebeeninvestigatedbyacombinationoftime- to a central wavelength of 200 nm. They are attenuated
resolved photoelectron spectroscopy and time-resolved to a pulse energy of 8.6 µJ, focused using reflective opmass spectrometry.64 The time-dependences of the par- tics,andoverlappedwiththeelectronpulsesata1◦angle
entionandafragmentmasscorrespondingtotheketene through an in-vacuum holey mirror into the interaction
andthecyclopropaneorpropenefragmentswerefittedto region of the experimental chamber. The diameter of
biexponential decays with time constants of 0.08 ps and these pump laser pulses in the interaction region is 490

<!-- Page 4 -->

4
µm x 250 µm FWHM to over-fill the electron spot. The III. RESULTS
experimental response function that includes the effects
of the optical and electron pulse length as well as the A. Static Structural Information
relative arrival time jitter is estimated based on a previous measurement5 and the pump pulse duration (130 fs
Figure 2 shows static structural information from the
FWHM) to be 190 fs.
reactantCBina)momentum-transferspaceasthemod-
Cyclobutanone(purity99%)ispurchasedfromSigma ified diffraction intensity sM(s) and b) real space as an
Millipore and used without further purification. The atomic pair distribution function PDF(r). The sM(s)
compound has a vapor pressure of 43 torr at room curve in Fig. 2 a) is compared to a simulation based on
temperature.31 This pressure is reduced with the help an optimized geometry of CB and the IAM (see sect. II
of a flow controller (MKS) to 1 torr. The resulting low- for details). The experimental sM(s) curve is truncated
pressure gas is delivered into a static-filler 3 mm flow below0.3˚A−1 duetothepresenceofaholeinthediffraccell with 500 µm diameter entrance and exit holes for tion detector through which the undiffracted electrons
the pump and probe beams.66 The experiment is per- pass. The agreement between experimental and simuformed at a repetition rate of 360 Hz. Diffracted elec- lated sM(s) is good in terms of the positions of all the
tronsaredetectedbyacombinationofaphosphorscreen maximaandminima. Discrepanciesintheamplitudecan
and an electron multiplying charge-coupled device (EM- havecontributionsfromuncompensateddeviationsinthe
CCD) camera. Based on the relative levels of static and s-dependenceoftheelectrondetectorresponse,thefinite
dynamic signal, we estimate that we excite about 0.3 widthofthegroundstategeometrydistribution, andde-
% of the molecules (see the Supplementary Information viations from the IAM.19,20,74
(SI), sect. S1 for details). Therefore, we do not expect Figure 2 b) shows the real-space representations of
to observe any contributions from multiphoton absorp- the two curves in Fig. 2 a) as experimental and simution. Time-dependent diffraction is measured at a series lated PDFs. They are compared with a histogram of
of time delay points between -4.7 ps and 2.1 ps in each the atomic distances in CB which is color-coded and
scan, where negative delays correspond to the electron scaled according to the involved elements and their elecprobe arriving before the optical pump in the sample. tron scattering cross-sections. The histogram excludes
The separation between time delay points is 0.05 ps, ex- the (H,H) distances due to the small electron scattering
cept for the earliest and latest delay points where it is cross-section of hydrogen atoms. The atomic distances
considerably larger. At each time delay point, we inte- of the histogram are generally reproduced well by the
grate the diffraction signal for 10 s (3600 shots). The PDFs.
full data set includes 393 such scans of all delays. The We will discuss the various (C,C) and (C,O) distances
processing of the raw diffraction patterns obtained is de- in the histogram within the framework of atomic coorscribed in detail in the SI, sect. S2. dination spheres. The (C-C) and (C-O) bond distances,
e.g. the (C -C ) distance of CB in Fig. 1, constitute the
1 2
For the simulation of the signatures of the secondary first coordination sphere. Signatures from the first cofragmentationproducts,theirgeometriesandthatofCB ordination sphere appear in the PDFs of Fig. 2 b) in a
are optimized using B3LYP/def2-SVP as implemented range between r =1 ˚A and r =2 ˚A, which is marked by
in ORCA.68–71 The geometry of the minimum energy a gold bar. Distances between atoms separated by two
conical intersection between the nπ∗ and ground states bonds, e.g. the (C ,C ) distance of CB in Fig. 1, consti-
2 4
from Ref.30 is used for the biradical geometry (see the tute the second coordination sphere with values ranging
SI, sect. S3 for further details). These geometries are from r = 2 ˚A to r = 2.7 ˚A as marked by a blue bar in
used to simulate electron diffraction signatures within Fig. 2 b). The third coordination sphere with distances
the IAM using a publicly available code72 with atomic betweenatomsseparatedbythreebonds,iscomprisedof
scattering cross-sections, which are evaluated by the asingledistance,(O,C )inCBinFig.1. Signaturesfrom
3
ELSEPA program.73 Momentum-transfer space ∆I/I(s) thethirdcoordinationsphereappearbeyondr =2.7˚Ain
signatures are simulated using the PDFs in Fig. 2 (marked by a light brown bar).

### The differences in (C-O) and (C-C) bond distances in

the first coordination sphere are resolved in the double-
I (s)−I (s) peakstructureatr =1.2˚Aandr =1.6˚AinbothPDFs.
∆I/I(s)= P CB , (4)
I (s) Thepeakatr =1.2˚Ahasadditional,weakcontributions

## Cb

from (C-H) bond distances. The (C,C) and (C,O) distances in the second coordination sphere are too close to
beresolvedin the PDFs, which resultsin bothcases in a
where I and I are the simulated IAM diffraction in-
P CB single peak at r =2.3 ˚A. This peak position value is sigtensities of a specific product and CB, respectively.
nificantlysmallerthaninthePDFsofsix-memberedcar-
Experimental and simulated PDF and ∆PDF curves bon ring molecules (see e.g.6,75). Therefore, it provides
are evaluated using an approach which is detailed in the clearevidenceforthepresenceofthefour-memberedring
SI, sect. S4. structure of CB.

<!-- Page 5 -->

5
FIG. 2. Static structural information from electron diffraction. a) Comparison of the momentum-transfer space (sM(s))
signatureofCBwithasimulationwithintheindependentatommodel(IAM).b)Atomicpairdistributionfunctions(PDF(r))
from the real-space transformation of the experimental and IAM signatures of part a). They are compared with histograms
of the atomic distance distribution in the ground state equilibrium geometry of CB, which are color-coded with respect to
the involved elements and scaled with respect to the atomic scattering cross-sections of the involved atoms. Additionally, the
distancerangesofthefirstthreecoordinationspheresinthePDFaremarkedbyhorizontalbarsandcorrespondtocolor-coded
linesinFig.1. Errorbarsfortheexperimentalplotsofpartsa)andb)arebasedonabootstrappinganalysisandarerepresented
by shaded areas.
The area between r =2.7 ˚A and r =3.4 ˚A containing B. Signatures of the photoinduced structural dynamics of
distancesinthethirdcoordinationsphere(one(C,O)and CB
several(C,H)and(O,H)distances)showsthelargestdisagreements between experimental and simulated PDFs.

### Figure3showstime-dependentelectrondiffractionsig-


### The simulated PDF shows a strong peak in the area of

natures of the structural response of CB to photoexcitaa number of (C,H) and (O,H) distances whereas the extion at λ = 200 nm in momentum transfer space. An
perimental PDF only exhibits a shoulder. In turn, the
overview of the time-dependent signatures in the diffracsimulated PDF shows a much weaker peak in the area
tion signal containing both contributions from the phoof the (C,O) distance than the experimental PDF. The
toexcitedpopulationandthecorrespondinggroundstate
disagreement can be at least partially explained by a depopulation bleach is given by the false-color plot of the
ficiency in the IAM approximation. The assumption of
percentage difference diffraction (∆I/I(s) in Fig. 3 a).
atomic behavior made by the IAM is a good approxima-

### We identify four different transient features in the three

tion for inner-shell electrons, as they are not involved in
marked regions of Fig. 3 a). The strongest of them is a
chemical bonding. Hydrogen atoms lack inner-shell elecpositive and short-lived feature in the s-region below 1.5
trons. Thus, when hydrogens are involved in chemical ˚A−1, which is marked by a blue vertical line and labeled
bonds, their electron density distribution exhibits paras α. It is superimposed with a negative signature in
ticularly strong deviations from the assumptions by the
the same s-range. This signature appears at later delays

### IAM.76Therefore,theIAMdescriptionoverestimatesthe

and persists beyond 2 ps after optical excitation. This
localization of electron density at the hydrogen atoms,
behavior is visible in the time-dependent integrated inwhich leads to an overestimation of the amplitude of the
tensity of the α range plotted in Fig. 3 c)). We refer to
(C,H) and (O,H) contributions.
the short-lived positive feature in the α region as α and
1
the long-lived negative feature as α .
2
The α feature is accompanied by a positive feature
2
with similar time-dependence in the range between s =
1.6 ˚A−1 and s = 2.8 ˚A−1, which is marked by orange
vertical lines and labeled as β. It shows a delayed onset
Thesmallpeakbeyondr =4˚Aoriginatesfromthetwo with respect to the α feature (see the time-dependence
1
longest(O,H)distancesinthemolecule. Inthefollowing, of the integrated α and β regions in Fig. 3 c)) and shifts
wewillreducethediscussionofthetime-dependentstruc- slightly to lower s-values within the first 0.5 ps after opturalevolutionofphotoexcitedCBtothestrongersigna- tical excitation. This behavior is illustrated by orange
tures of (C,C) and (C,O) distances and neglect the rela- dots in Fig. 3 a), which represent the center of mass of
tively small contributions from (C,H), (O,H) and (H,H) the β feature. Due to the initial presence of the posidistances. tive α feature, it cannot be assessed if the α feature is
1 2

<!-- Page 6 -->

6
FIG. 3. Diffraction signatures of the UV-induceddynamics. a)False-color mapof the signatures represented as ∆I/I. Three
different s-ranges with time-dependent changes are marked by vertical lines and labeled as α, β, and γ. The time-dependent
center of mass of the positive contributions in the β range are marked by orange dots. b) ∆I/I signatures at different pumpprobedelays. Thecurvesareverticallyoffsetfromeachothertoreflecttheirdelaytime. Errorbarsarebasedonabootstrapping
analysisandarerepresentedbyshadedareas. c)Time-dependent∆I/I intensitiesintegratedovertheα,β,andγ ranges. The
experimental data are plotted together with error function fits. The centers of these error functions are marked by horizontal
lines, which are also extended into part a). The shaded areas around the horizontal lines represent the uncertainty of the fit.
The three plots are horizontally offset from each other. The respective zero levels are marked by dotted lines.
shiftingonthesametimescale. Thepositionofthenega- delay with respect to the α feature. It remains approxi-
1
tive α feature shifts at about 0.5 ps to smaller s-values. matelyconstantovertheinvestigateddelaytimewindow.
2
However, this shift is likely a result of the superposition The delay in the onset with respect to the α feature is
1
of the α and α contributions. clearly visible in the lineouts of Fig. 3 b): The lineout at
1 2
0.12 ps delay already shows a positive signature in the α

### Afourthdelay-dependentfeatureappearsintherange

between s = 7 ˚A−1 and s = 8 ˚A−1, which is marked by region, whereasasignatureinthe γ regiononlystarts to
appear in the subsequent lineout at 0.32 ps.
green vertical lines and labeled as γ. It appears close to
time zero, earlier than the β feature, but with a slight We quantify the delay in the onset of the γ feature

<!-- Page 7 -->

7
with respect to α feature by fitting error functions to Figure 4 b) shows the corresponding comparison be-
1
the integrated signal S tween experimental and simulated product signatures
in their real-space representation. An atomic distance
(cid:20) (cid:18) (cid:19)(cid:21)
S(t)=A +A 1+erf 2 (cid:112) 2ln(2) t−t 0 (5) change during an isomerization reaction such as the pri-
0 τ maryring-openingreactionofCB,appearsina∆PDF(t)
curve as a combination of a negative contribution at the
for the integrated ranges in Fig. 3 c). S(t) is the inte- pair distance of the reactant and a positive contribution
grated intensity in the respective regions, A accounts at the new distance at time t. The positive ∆PDF con-
0
for small baseline offsets at negative pump-probe delays, tribution from a distance change can be missing if the
A is a scaling factor, t is the center of the error func- distancevalueisoutside(>5˚A)theconsidereddistance
0
tion, and τ its width. For the α region, only early time range, e.g. in the case of fragmentation.
delays are included in the fit since the later intensity The intense negative contributions of the experimenevolution shows a trend towards negative values which tal ∆PDF plot show clear signatures of the dissolution
cannot be modeled by the simple fit function. The fitted of the four-membered ring: the negative peak at r =1.5
error function center to the γ feature shows a delay with ˚A agrees well with typical C-C bond lengths, and is sigrespect to the center of the fit to the α 1 feature of (0.14 nificantly longer than the C-O bond length (1.2 ˚A), as
± 0.05) ps. The difference in onset times is further vi- discussed previously in relation to Fig. 2. This dissociasualized by the color-coded horizontal lines in Fig. 3 a), tionofa(C-C)bondinthefirstcoordinationspheremust
which correspond to the fit centers. The growth of the for geometric reasons also affect the ∆PDF in the region
β range is qualitatively different from that of the other of the second (C,C) coordination sphere of the reactant.
two features, which can be quantified by the center and Accordingly,the∆PDFplotshowsadepletionatr =2.2
the width of the error function fit. The center shows a ˚A, i.e. at r values significantly smaller than the corredelayof(0.58±0.06)pswithrespecttotheα 1 onset. Its spondingsecondcoordinationsphere(C,O)distance(2.5
width is (1.2±0.2) ps compared to (0.1±0.1) ps for the ˚A,seeFig.2). Enhancementsintheexperimental∆PDF
γ range. are observed at short distances (r <1.3 ˚A) arising from
Weadditionallyquantifythedecaytimescaleoftheα 1 new atomic distances in the photoproducts. The origin
feature by a global biexponential fit resulting in a time of the small positive contributions in the experimental
constantof(0.29±0.2)ps(seetheSI,sect.S5),i.e.with ∆PDF at r values beyond 3 ˚A are further discussed in
an uncertainty in the range of the instrument response the SI, sect. 4.2.
function (190 fs).

### Further information content from the experimental

∆PDF signature can be extracted by comparison with
the simulated product ∆PDFs. The ∆PDF signature of
C. Comparison to simulated product signatures the primary biradical product shows qualitatively similar effects of the dissolution of the four-membered ring
We start our analysis of the difference diffraction re- with negative peaks at r = 1.6 ˚A and r = 2.2 ˚A for the
sults by comparing an experimental signature averaged same representative structure used above. In contrast
across a delay range of 1.3 ps to 2.1 ps, when the dif- to the experimental ∆PDF, however, it also shows two
ference signal is approximately constant in both inten- strong positive peaks at r = 2.8 ˚A and r = 3.7 ˚A. Both
sity and shape, to IAM simulations of static equilibrium peaks can be related to the ring-opening reaction: The
product structures in Fig. 4 a) in momentum transfer 2.8 ˚A peak results from the transformation of a first cospace. TheIAMsimulationsarebasedonthegeometries ordinationshell(C-C)distance(ofthebrokenC-Cbond)
oftheprimary,biradicalproductoftheNorrishtype-Ire- into a third coordination shell (C,C) distance. The peak
action and the products of the secondary fragmentation at r =3.7 ˚A results from the transformation of a second
channels(1)-(3),whicharevisualizedinFig.1. Theyare coordinationshell(C,O)distanceintoafourthcoordinarescaled to fit the peak intensity of the β feature in the tion shell (C,O) distance. The latter is beyond the highexperimental signature. est reactant coordination sphere (see color-coded ranges
The overall agreement between the experimental data in Fig. 4 b)). The shapes and positions of these posiand simulated product signatures is good. In agreement tive contributions might be different if a different model
with the experimental results, all IAM simulations show thanasinglegeometryisemployedforthesimulation(see
negative contributions in the α region, positive contri- sect. IVA), but any ring-opened structure will generate
butions in the β region, and positive contributions in positive contributions in this distance range.
the γ region. The signatures of all secondary fragmen- While the simulated ∆PDFs of the fragmentation
tation channels are rather similar. The biradical simula- channels again show the negative fingerprint peaks of
tion differs most from the experimental signal, showing the ring dissolution, the two positive peaks of the priweaker negative contributions in the α region. Addition- mary channel are missing. Based on the considerations
ally, only the biradical has significant positive contribu- aboutpositiveandnegativecontributionsto∆PDFs(see
tions (at s = 5.5 ˚A−1) in the area between the β and γ above), the corresponding distance values must be beregions. yond r = 5 ˚A. Thus, the missing positive peaks are a

<!-- Page 8 -->

8
FIG. 4. Comparisons of experimental signatures at different delays with simulations. a) Comparison of the averaged ∆I/I
signatureinmomentum-transferspaceoveradelayrangeof1.3psto2.1ps(blue)withindependentatommodelsimulationsof
thebiradicalprimaryproduct(green)andthethreesecondaryfragmentationchannels(red,purple,andbrown,seeFig.1). The
α,β,andγ rangesarelabeledandmarkedwithvertical,color-codedlines. Thesimulationsarerescaledtomatchtheintensity
of the peak in the β range of the experimental signal. b) Analogous comparison to a), but after real-space transformation.
The simulations are rescaled to match the negative peak at r=2.3 ˚A in the experimental difference pair distribution function
(∆PDF).ThesamehorizontalbarsasinFig.2markingthereactantcoordinationspheresareshownonthetop. c)Analogous
comparisontoa), butwithanexperimentalsignatureaveragedoveradelayrangeof0.2psto0.5ps(orange). d)Comparison
of peak positions and intensities of the averaged experimental signatures from a) and c) with the simulations. The left y-axis
corresponds to the simulations, the right y-axis to the experimental plots.
direct signature of the fragmentation reaction. An addi- not surprising, since the number of distances between
tional, more subtle effect of the fragmentation is evident carbon and oxygen atoms in each of the coordination
from the small positive peak at r = 1 ˚A, which is a spheresareidentical: Inbothcases,two(C-C)bondsare
signature of an overall (C-C) and (C-O) bond distance broken leading to negative signatures at r = 1.5 ˚A. The
reductionduetotheformationofπ bondsinsomeofthe fragmentation also eliminates in both cases two of the
secondary products. Since the simulated signatures of second coordination sphere distances and the only third
the fragmentation product channels fit the experimental coordination sphere distance in CB providing negative
∆PDFsubstantiallybetterthanthesignaturesofthepri- contributions at r =2.2 ˚A and r =3.5 ˚A.
marybiradicalproduct,specificallyintheregionbetween
r = 2.5 ˚A and r = 5 ˚A, we conclude that fragmentation Notably, channel 3 shows a lower level of agreement
occurs within 1.3 ps after photoexcitation. thanchannels1and2,specificallyaroundr =1.5˚A and
r =3˚A.Thesedifferencescanbetracedbacktothegen-
Considering the level of agreement of the simulated eration of the cyclopropane fragment, where the loss of
∆PDFsofthethreepossiblefragmentationchannelswith the two (C-C) bond distances to the carbonyl carbon is
the experimental ∆PDF, we find a high and approxi- partially compensated by the generation of a new (C-
mately equal level of agreement for channels 1 and 2. C) bond through the formation of the three-membered
The similarities in the signatures of channels 1 and 2 are ring. Inturn, thefragmentsdonotexhibitanydistances

<!-- Page 9 -->

9
in the second coordination sphere leading to the differ- energy conical intersection geometry from Ref.30 for the
ences between r = 2.5 ˚A and r = 3.5 ˚A. Based on the conicalintersectionbetweenthenπ∗stateandtheground
agreementofthe∆PDFsignatures,weconcludethatthe stateofCB.Thisgeometryresemblesmorecloselyapoint
distribution of secondary fragments after 1.3 ps is domi- on the (C -C ) dissociation coordinate than the biradi-
1 2
natedbychannels(1)and(2), butcannotexcludeminor cal minimum geometry (see the SI, sect. S3). However,
contributions from channel (3). The ∆PDF signatures the IAM signatures from the minimum geometry lead to
of channels (1) and (2) are too similar to make further qualitatively similar conclusions (see the SI, sect. S3).
claims about their relative populations. Nevertheless, previous studies of ring-opening reactions
Figure4c)showsacomparisonofthesamesimulations demonstrate the validity of comparisons with product
as in Fig. 4 a) with an experimental signal averaged be- signatures for qualitative assessments.5–7 However, this
tween 0.2 ps and 0.5 ps delay. Again, the simulations is an area where more advanced theoretical models of
are rescaled to fit the peak intensity of the experimental the photodynamics could lead to more detailed insight.
β feature. This is the delay range in which a shift of Thefragmentationproductgeometriesfromsecondary
theβ signaturetolowers-valuesisobservable(seeFig.3 channels (1)-(3) are much more rigid. Additionally, the
a)). While the signal-to-noise level of the experimental secondaryreactionsallowthemolecularsystemtotranssignature in the β region in Fig. 4 is rather poor due to form a part of the photoabsorbed excess energy from
the proximity to the signal onset, the position of the β theinteratomicdegreesoffreedomintotranslationaland
peak is best matched by the simulated biradical signa- rotational energy of the fragments. Therefore, we exture. This indicates the observation of the ring-opened pecttheapproximationoftheIAMsignaturesofthesecstructure prior to secondary fragmentation. Notably, all ondary channel products to be of substantially higher
simulations qualitatively disagree with the experimental quality than the primary reaction product. Based on
signature in the α region, the origin of which will be these considerations, we are confident about our assigndiscussed in sect. IVB. The presence of the α feature ment of the experimental ∆PDF signatures after 1.3 ps
1
prevents a similar analysis in real-space as in Fig. 4 b) to fragmentation channels (1) and (2).
(see below). A comparison of the experimental signatures from Fig. 4 a) and c) with the IAM simulations
without intensity rescaling in Fig. 4 d) shows that both
B. The origin of the α feature and the onset of the
1
the experimental signature at early times and the IAM structural dynamics
simulationofthebiradicalgeometryhavelowerintensity
(as well as peaks at higher ˚A) in the β region than the

### Similar features like the short-lived α feature have

experimental signature at late times and the IAM signa- 1
been previously observed at low s-values.19,20 In both
tures of the fragmentation channels, respectively, which
cases,theycouldbeexplainedbasedonab initio scatterprovidesfurthersupportfortheassignmentoftheexperingsimulationsasoriginatingfromthechangeintheelecimentalsignaturesatearlytimestoincludecontributions
tronic structure induced by the photoexcitation. Thus,
from biradical geometries.
the features cannot be described by the IAM. Previous
ab initio scatteringsimulationssuggestthattheyexhibit
significant contributions from inelastic electron scatter-

## Iv. Discussion

ing, which does not contain structural information due
to its incoherent nature and is known to appear concen-
A. Reaction product signatures trated at low s-values.78 The qualitative mismatch betweentheexperimentalandsimulatedsignaturesatearly
The approximation of photochemical product signa- delaysintheαregion(Fig.4c))isadditionalevidencein
tures by ∆PDFs based on IAM simulations from single favor of an assignment of the α feature to the non-IAM
1
reactantandproductgeometriesfacesknownlimits. The signature of an electronic excitation in CB.
static PDFs of gas-phase molecules agree with reason- These non-IAM signatures were in the two previous
ableaccuracywithPDFsbasedonIAMsimulationsfrom studiesattributedtostates withn3sandnπ∗ characters.
single geometries, effectively ignoring the geometry blur- Thepreviousfindingssuggestthatweobservepopulation
ring effect of vibrational wavefunctions.77 These effects dynamics in one or several electronic states with n-hole
are strongly increased in the case of photochemical re- character in our present study. Two electronic states of
action products, where typically a significant amount of CB with n-hole character exist in the energy range of
the photoabsorbed energy(of 6.2eV inthe present case) current interest, the initially excited n3s Rydberg state
is redistributed into the vibrational degrees of freedom and a lower-lying nπ∗ state. The latter is likely popuof the molecules. Due to its lack of rigidity, the actual lated from the n3s state through nonadiabatic dynamics
∆PDF signature of the primary, biradical photoproduct on the sub-ps timescale.64 The relative timing of the oncan be expected to show the largest deviations from the set of the α feature, which precedes those of the other
1
approximation by a single geometry. The employed ge- observedfeatures,suggeststhatitatleastinitiallycorreometryfortheIAMsimulationsisinfactnotaminimum spondstopopulationofthen3sstatebyphotoexcitation.
geometry of the biradical photoproduct, but a minimum Since it originates from a change in the electronic wave-

<!-- Page 10 -->

10
functionofthemoleculeinducedbythephotoexcitation, sitions in the α and β regions show the largest variance,
itsonsetisquasi-instantaneousattimezero. Incontrast, while the peak position in the γ region is much more
signaturesfromstructuraldynamicstypicallyexperience stable. Based on this observation, we expect that the
some delay with respect to the optical excitation, since experimental signature of the primary photoproduct is
the nuclei need to move a sufficient amount to generate much less pronounced than the secondary products in
a difference diffraction signal. Thus, the onset of the α the β region, which could explain the slow onset of the
1
feature provides an unambiguous signature of time zero. β feature. Additionally, due to its transitory nature, its
Without more advanced simulation of the observable, populationatallbuttheearlypump-probedelayscanbe
wecannotexcludethepossibilitythattheα featurealso expectedtobelowcontributingtotheobservedweakness
1
contains contributions from population in the nπ∗ state in the β region.
at later delays. However, the fitted decay time constant
(0.29 ps, more details in SI sect. S5) of the α feature
1
agreesverywellwiththefasterofthetwotimeconstants D. Proposed reaction mechanism based on the UED
of the biexponential fit (0.31 ps and 0.74 ps) to the n3s results
feature in the time-resolved photoelectron spectra from
Ref.64. Therefore, the α feature is likely predominantly
1 All above findings and considerations lead us to the
caused by population in the n3s state.
following mechanism for the photochemical reaction dy-

### Since inelastic electron scattering signatures are

namics of CB within the first 2 ps after photoexcitation
strongly localized at small s-values, it is highly unlikely
at λ = 200 nm: The photoexcitation populates an n3s
that the γ region is a non-IAM signature. Additionally,
Rydberg state which can be followed in the onset of the
the IAM simulations of primary and secondary reaction
α feature. The n3s state is largely depopulated within
1
products all show positive peaks in the γ region. There- 0.29 ps via internal convsersion to the nπ∗ state, which
fore, we interpret the onset of the signal in the γ region
can be observed with the decay of the α feature.
1
astheonsetofthestructuraldynamics. Accordingly,the

### Themolecularstructurerespondswithin0.14±0.05ps

delay between the α and γ signatures of 0.14 ± 0.05 ps
1 byaNorrishType-Ireactionopeningthefour-membered
is the delay between optical excitation and the onset of
ring and resulting in the biradical primary product. The
significant structural dynamics.
timescale for the onset of this ring-opening reaction is
set by the delay of the γ feature with respect to the α
1
feature. The value of the delay is below the instrument
C. Delay and shift in the β feature response function of the experiment. However, it occurs
betweentwofeaturesinclearlyseparateds-regions,which
The onset of the γ feature does not give evidence for makes it well-observable.
the specific nature of the structural change, since it is The lifetime of the α feature (0.29 ± 0.2 ps) is larger
1
sharedbyboththeprimaryandsecondaryproducts. The than the difference in onset between the α and the γ
1
slower onset of the β feature and its shift to lower s- features. However, according to previous time-resolved
values provide more conclusive insights into this issue. photoelectron spectroscopy results, the main structural
The signature of the biradical geometry shows a posi- motion enabling depopulation of the n3s state is ringtive contribution to higher s-values with respect to the puckering,65 which can be expected to provide a negsecondary products in the beta region. Thus, a trans- ligibly weak signature in the difference diffraction patformation from the biradical to the secondary products terns. Thus, having traversed the n3s/nπ∗ conical inwould result in the observed shift in the β feature to tersection, molecules on the nπ∗ potential must undergo
lower s-values. Hence, the experimental signature at de- quasi-instantaneous (C -C ) bond extension and access
1 4
laysbetween0.2psand0.5psinFig.4c)canbeassigned the conical intersection of the nπ∗ state with the ground
tothebiradicalphotoproduct. Thisassignmentcouldbe state. Accordingly, the diffraction patterns show the onmore obvious after real-space transformation. However, set of structural dynamics in the nπ∗ state (onset of the
the α feature dominates the ∆I/I signal at these early γ feature) while the population dynamics out of the n3s
1
delays. Due to its suspected inelastic scattering nature, state (decay of the α feature) are still ongoing. Inter-
1
a real-space transformation would not yield meaningful nal conversion through the conical intersection with the
results. ground state results in vibrationally hot ground state
One would intuitively expect to observe the onset of molecules.
the β feature to be co-timed with the onset of the γ AccordingtoRef.30, theNorrishType-Ireactioncoorfeature at slightly higher s-values. Instead, it slowly in- dinate exhibits an energy barrier of 0.29 eV relative to
creases in intensity while also shifting in s. This behav- thepotentialminimumofthenπ∗state. Wecanestimate
ior can be explained by considering the much less well- theamountofenergyavailableinthevibrationaldegrees
defined geometry (see sect. IVA) of the primary pho- of freedom of CB after internal conversion from the n3s
toproduct compared to the secondary products. In the state based on the excitation photon energy and the pocomparison of the ∆I/I signatures of different possible sition of the nπ∗ transition in its absorption spectrum
biradical geometries (see the SI, sect. S3), the peak po- (λ = 280 nm) to be ≈ 1.8 eV. Since this value is sub-

<!-- Page 11 -->

11
stantially higher than the barrier, the barrier is unlikely ondaryproductchannelscreatingketeneandethylene,or
to play a significant role in slowing down the reaction. propeneandCO.Thecomplementarysensitivityofultra-
Thus, the topology of the nπ∗ potential energy surface fast electron diffraction to electronic structure changes
isconsistentwithquasi-instantaneous(C-C)bondexten- and nuclear structure changes is instrumental in assignsion (ring-opening) towards the conical intersection with ing the reaction mechanism. The observation of easily
the ground state. Given the reported minimum coni- separable signatures of both electronic state population
cal intersection (ref.30), we can estimate that the vibra- dynamicsandstructuraldynamicsprovidesrichinformational energy content within the dissociating molecules tion content for comparison to simulations of the nonawill have increased to ≈2.7 eV at this point. diabatic dynamics. Additionally, our study emphasizes
Reference30 suggests that the ring-opening reaction is the limits to the accurate interpretation of experimenaccompaniedbyinternalconversionthroughaconicalin- tal data from gas-phase UED without the comparison to
tersection between the nπ∗ state and the ground state. trajectory simulations.

### Thus, in the case of a quasi-instantaneous ring-opening

reaction after reaching the nπ∗ state, the relative population in the nπ∗ state would be small and accordingly VI. ACKNOWLEDGEMENT
would have negligible contributions to the α feature.
1
Previous studies also proposed reaction mechanisms in-

### This work was primarily supported by the AMOS

volving intersystem crossing to the triplet manifold.35,62
program within the U.S. Department of Energy Office
Since our observable is not directly sensitive to the mulof Science, Basic Energy Sciences, Chemical Sciences,
tiplicity of the populated electronic states, we cannot
Geosciences, and Biosciences Division. A.G. was supdefinitivelyruleoutthepresenceofreactionpathwaysinported by the European Union, through Horizon Euvolving triplet states. However, the observed timescales,
rope project 123-CO: 101067645. Views and opinions
which would be extremely fast for intersystem crossing,
expressed are however those of the authors only and do
suggest a reaction mechanism in the singlet manifold.
notnecessarilyreflectthoseoftheEuropeanUnion. Nei-

### Kuhlman et al.64 observed a biexponential decay of

ther the European Union nor the granting authority can
then3sstatefeatureintheirtime-resolvedphotoelectron
be held responsible for them. NG, LH and PMW were
spectra. We would not expect to observe the same defunded by the US Department of Energy under grant
cay of the n3s state feature (α ) due to a superposition
1 no. DE-SC0017995. Funding for the collaboration inwith negative contributions from the ring-opening and
cluding PMW and MC, which also supported SWC and
fragmentation signatures (α ). Since the superposition
2 SKS, was provided by the U.S. Department of Energy,
occurs between a feature with sensitivity to population

### Office of Science, Basic Energy Sciences, under award

dynamics and one with sensitivity to structural dynamnumber DE-SC0020276. AJOE is grateful for support
ics,itisdifficulttodisentangletheminameaningfulway.
from EPSRC grant EP/V026690/1. JS, HVSL, DR,

### The primary ring-opened photoproduct reacts further

and AR were supported by the Chemical Sciences, Geoby fragmentation into secondary product channels (1)
sciences, and Biosciences Division, Office of Basic Enand (2) yielding ketene and ethylene and propene and
ergy Sciences, Office of Science, US Department of En-
CO, respectively. The dominance of channel (2) over
ergy, grant no. DE-FG02-86ER13491. The experiment
channel(3)isconsistentwithaphotolysisstudyafter200
was performed at SLAC MeV-UED, which is supported
nm excitation, which deduced a ratio between channels
in part by the Department of Energy Basic Energy Sci-
(2) and (3) of 2.4:1.32 The same study showed evidence
ences’ Scientific User Facility Division Accelerator and
that after excitation to the nπ∗ state the formation of

### Detector research and development program, the LCLS

the channel (2) products was the result of a tertiary iso-

### Facility, and SLAC under Contract Nos. DE-AC02-05-

merization reaction from channel (3). However, the sub-
CH11231 and DEAC02-76SF00515.
stantially higher level of vibrational energy available to
the secondary fragmentation reaction after excitation to 1Y.-C.ChengandG.R.Fleming,“DynamicsofLightHarvesting
the n3s state, might well lead to a different final product in Photosynthesis,” Annual Review of Physical Chemistry 60,
distribution than that observed after nπ∗ excitation. 241–262(2009).
2D. Polli, P. Altoe, O. Weingart, K. M. Spillane, C. Manzoni,
D. Brida, G. Tomasello, G. Orlandi, P. Kukura, R. A. Mathies,
M. Garavelli, and G. Cerullo, “Conical intersection dynamics
V. CONCLUSION oftheprimaryphotoisomerizationeventinvision,”Nature467,
440–443(2010).
3M.S.SchuurmanandA.Stolow,“DynamicsatConicalIntersec-
In our investigation of the ultrafast structural dynamtions,”AnnualReviewofPhysicalChemistry69,427–450(2018).
icsofcyclobutanone, withoutadvancedtheoreticalinput 4B. F. E. Curchod and T. J. Mart´ınez, “Ab Initio Nonadiabatic
weobservethedepopulationofthephotoexcitedn3sRy- Quantum Molecular Dynamics,” Chemical Reviews 118, 3305–
dbergstatewithin0.29pstowardsthenπ∗state,followed 3336(2018).
5T. J. A. Wolf, D. M. Sanchez, J. Yang, R. M. Parrish,
byrapidring-openingviaaNorrishType-Ireaction. The
J.P.F.Nunes, M.Centurion, R.Coffee, J.P.Cryan, M.Gu¨hr,
primarybiradicalring-openingproductfurtherfragments
K.Hegazy,A.Kirrander,R.K.Li,J.Ruddock,X.Shen,T.Vecwithintheinvestigatedtimewindowmainlyintotwosec- chione, S. P. Weathersby, P. M. Weber, K. Wilkin, H. Yong,

<!-- Page 12 -->

12
Q.Zheng,X.J.Wang,M.P.Minitti, andT.J.Mart´ınez,“The tronDiffraction,”PhysicalReviewX10,021016(2020).
photochemicalring-openingof1,3-cyclohexadieneimagedbyul- 16M.R.Coates,M.A.B.Larsen,R.Forbes,S.P.Neville,A.E.Botrafast electron diffraction,” Nature Chemistry 11, 504 – 509 guslavskiy,I.Wilkinson,T.I.Sølling,R.Lausten,A.Stolow, and
(2019). M.S.Schuurman,“Vacuumultravioletexcitedstatedynamicsof
6E.G.Champenois,D.M.Sanchez,J.Yang,J.P.FigueiraNunes, thesmallestring,cyclopropane.II.Time-resolvedphotoelectron
A. Attar, M. Centurion, R. Forbes, M. Gu¨hr, K. Hegazy, F. Ji, spectroscopyandabinitiodynamics,”TheJournalofChemical
S. K. Saha, Y. Liu, M.-F. Lin, D. Luo, B. Moore, X. Shen, Physics149,144311(2018).
M. R. Ware, X. J. Wang, T. J. Mart´ınez, and T. J. A. Wolf, 17S.P.Neville,Y.Wang,A.E.Boguslavskiy,A.Stolow, andM.S.
“Conformer-specific photochemistry imaged in real space and Schuurman, “Substituent effects on dynamics at conical intertime,”Science374,178–182(2021). sections: Allene and methyl allenes,” The Journal of Chemical
7Y.Liu,D.M.Sanchez,M.R.Ware,E.G.Champenois,J.Yang, Physics144,014305(2016).
J.P.F.Nunes,A.Attar,M.Centurion,J.P.Cryan,R.Forbes, 18T.J.A.Wolf,T.S.Kuhlman,O.Schalk,T.J.Martinez,K.B.
K. Hegazy, M. C. Hoffmann, F. Ji, M.-F. Lin, D. Luo, S. K. Moller,A.Stolow, andA.-N.Unterreiner,“Hexamethylcyclopen-
Saha,X.Shen,X.J.Wang,T.J.Mart´ınez, andT.J.A.Wolf, tadiene: time-resolved photoelectron spectroscopy and ab initio
“Rehybridization dynamics into the pericyclic minimum of an multiple spawning simulations,” Physical Chemistry Chemical
electrocyclicreactionimagedinreal-time,”NatureCommunica- Physics16,11770–11779(2014).
tions14,2795(2023). 19J. Yang, X. Zhu, J. P. F. Nunes, J. K. Yu, R. M. Parrish,
8Y. Liu, R. Xu, D. Sanchez, T. Martinez, and T. Wolf, “Ultra- T.J.A.Wolf,M.Centurion,M.Gu¨hr,R.Li,Y.Liu,B.Moore,
fastEventsinElectrocyclicRing-OpeningReactions,”ChemRxiv M.Niebuhr,S.Park,X.Shen,S.Weathersby,T.Weinacht,T.J.
(2024),10.26434/chemrxiv-2024-jw2x3. Martinez, and X. Wang, “Simultaneous observation of nuclear
9P. Chakraborty and S. Matsika, “Time-resolved photoelectron and electronic dynamics by ultrafast electron diffraction,” Scispectroscopyviatrajectorysurfacehopping,”WIREsComputa- ence368,885–889(2020).
tionalMolecularScience14,e1715(2024). 20E.G.Champenois,N.H.List,M.Ware,M.Britton,P.H.Bucks-
10J. P. Figueira Nunes, L. M. Ibele, S. Pathak, A. R. Attar, baum,X.Cheng,M.Centurion,J.P.Cryan,R.Forbes,I.Gabal-
S.Bhattacharyya,R.Boll,K.Borne,M.Centurion,B.Erk,M.- ski,K.Hegazy,M.C.Hoffmann,A.J.Howard,F.Ji,M.-F.Lin,
F. Lin, R. J. G. Forbes, N. Goff, C. S. Hansen, M. Hoffmann, J.P.F.Nunes,X.Shen,J.Yang,X.Wang,T.J.Martinez, and
D.M.P.Holland,R.A.Ingle,D.Luo,S.B.Muvva,A.H.Reid, T. J. Wolf, “Femtosecond Electronic and Hydrogen Structural
A.Rouz´ee,A.Rudenko,S.K.Saha,X.Shen,A.S.Venkatacha- Dynamics in Ammonia Imaged with Ultrafast Electron Diffraclam,X.Wang,M.R.Ware,S.P.Weathersby,K.Wilkin,T.J.A. tion,”PhysicalReviewLetters131,143001(2023).
Wolf, Y. Xiong, J. Yang, M. N. R. Ashfold, D. Rolles, and 21P.Chakraborty,Y.Liu,S.McClung,T.Weinacht, andS.Mat-
B.F.E.Curchod,“MonitoringtheEvolutionofRelativeProduct sika, “Nonadiabatic Excited State Dynamics of Organic Chro-
Populations at Early Times during a Photochemical Reaction,” mophores: Take-Home Messages,” The Journal of Physical
JournaloftheAmericanChemicalSociety146,4234(2024). ChemistryA126,6021–6031(2022).
11S. Pathak, L. M. Ibele, R. Boll, C. Callegari, A. Demidovich, 22P.Chakraborty,Y.Liu,S.McClung,T.Weinacht, andS.Mat-
B. Erk, R. Feifel, R. Forbes, M. Di Fraia, L. Giannessi, C. S. sika, “Time Resolved Photoelectron Spectroscopy as a Test of
Hansen, D. M. P. Holland, R. A. Ingle, R. Mason, O. Plekan, ElectronicStructureandNonadiabaticDynamics,”TheJournal
K. C. Prince, A. Rouz´ee, R. J. Squibb, J. Tross, M. N. R. Ash- ofPhysicalChemistryLetters12,5099–5104(2021).
fold,B.F.E.Curchod, andD.Rolles,“Trackingtheultraviolet- 23H.Yong,A.Kirrander, andP.M.Weber,“Time-resolvedX-ray
inducedphotochemistryofthiophenoneduringandafterultrafast Scattering of Excited State Structure and Dynamics,” in Strucringopening,”NatureChemistry12,795–800(2020). tural Dynamics with X-ray and Electron Scattering (RSC Pub-
12K. D. Borne, J. C. Cooper, M. N. R. Ashfold, J. Bachmann, lishing,2023).
S.Bhattacharyya,R.Boll,M.Bonanomi,M.Bosch,C.Callegari, 24M. Centurion, T. J. Wolf, and J. Yang, “Ultrafast Imaging of
M. Centurion, M. Coreno, B. F. E. Curchod, M. B. Danailov, MoleculeswithElectronDiffraction,”AnnualReviewofPhysical
A. Demidovich, M. Di Fraia, B. Erk, D. Faccial`a, R. Feifel, Chemistry73,21–42(2022).
R. J. G. Forbes, C. S. Hansen, D. M. P. Holland, R. A. Ingle, 25M. Dunne, R. W. Schoenlein, J. P. Cryan, and T. J. A. Wolf,
R. Lindh, L. Ma, H. G. McGhee, S. B. Muvva, J. P. F. Nunes, “Free Electron Lasers for X-ray Scattering and Diffraction,” in
A. Odate, S. Pathak, O. Plekan, K. C. Prince, P. Rebernik, Structural Dynamics with X-ray and Electron Scattering (RSC
A.Rouz´ee,A.Rudenko,A.Simoncig,R.J.Squibb,A.S.Venkat- Publishing,2023).
achalam, C. Vozzi, P. M. Weber, A. Kirrander, and D. Rolles, 26S.P.Weathersby,G.Brown,M.Centurion,T.F.Chase,R.Cof-
“Ultrafast electronic relaxation pathways of the molecular pho- fee, J. Corbett, J. P. Eichner, J. C. Frisch, A. R. Fry, M. Gu¨hr,
toswitchquadricyclane,”NatureChemistry16,499–505(2024). N.Hartmann,C.Hast,R.Hettel,R.K.Jobe,E.N.Jongewaard,
13B.Stankus,H.Yong,N.Zotev,J.M.Ruddock,D.Bellshaw,T.J. J. R. Lewandowski, R. K. Li, A. M. Lindenberg, I. Makasyuk,
Lane, M. Liang, S. Boutet, S. Carbajo, J. S. Robinson, W. Du, J.E.May, D.McCormick, M.N.Nguyen, A.H.Reid, X.Shen,
N. Goff, Y. Chang, J. E. Koglin, M. P. Minitti, A. Kirrander, K.Sokolowski-Tinten,T.Vecchione,S.L.Vetter,J.Wu,J.Yang,
andP.M.Weber,“UltrafastX-rayscatteringrevealsvibrational H.A.Du¨rr, andX.J.Wang,“Mega-electron-voltultrafasteleccoherencefollowingRydbergexcitation,”NatureChemistry 11, trondiffractionatSLACNationalAcceleratorLaboratory,”Re-
716–721(2019). viewofScientificInstruments86,073702(2015).
14M. P. Minitti, J. M. Budarz, A. Kirrander, J. S. Robinson, 27H. Yong, N. Zotev, J. M. Ruddock, B. Stankus, M. Simmerma-
D.Ratner,T.J.Lane,D.Zhu,J.M.Glownia,M.Kozina,H.T. cher,A.M.Carrascosa,W.Du,N.Goff,Y.Chang,D.Bellshaw,
Lemke, M. Sikorski, Y. Feng, S. Nelson, K. Saita, B. Stankus, M. Liang, S. Carbajo, J. E. Koglin, J. S. Robinson, S. Boutet,
T.Northey,J.B.Hastings, andP.M.Weber,“ImagingMolec- M.P.Minitti,A.Kirrander, andP.M.Weber,“Observationof
ular Motion: Femtosecond X-Ray Scattering of an Electro- the molecular response to light upon photoexcitation,” Nature
cyclicChemicalReaction,”PhysicalReviewLetters114,255501 Communications11,2157(2020).
(2015). 28R. M. Parrish and T. J. Mart´ınez, “Ab Initio Computation of
15Y. Liu, S. L. Horton, J. Yang, J. P. F. Nunes, X. Shen, Rotationally-AveragedPump-ProbeX-RayandElectronDiffrac-
T. J. A. Wolf, R. Forbes, C. Cheng, B. Moore, M. Centurion, tionSignals,”JournalofChemicalTheoryandComputation15,
K.Hegazy,R.Li,M.-F.Lin,A.Stolow,P.Hockett,T.Rozgonyi, 1523–1537(2019).
P.Marquetand,X.Wang, andT.Weinacht,“Spectroscopicand 29T. Northey, N. Zotev, and A. Kirrander, “Ab Initio Calcula-
Structural Probing of Excited-State Molecular Dynamics with tionofMolecularDiffraction,”JournalofChemicalTheoryand
Time-Resolved Photoelectron Spectroscopy and Ultrafast Elec- Computation10,4911–4920(2014).

<!-- Page 13 -->

13
30S.-H. Xia, X.-Y. Liu, Q. Fang, and G. Cui, “Excited- (2024).
State Ring-Opening Mechanism of Cyclic Ketones: A MS- 47J.Suchan,F.Liang,A.S.Durden, andB.G.Levine,“Prediction
CASPT2//CASSCFStudy,”TheJournalofPhysicalChemistry challenge: First principles simulation of the ultrafast electron
A119,3569–3576(2015). diffractionspectrumofcyclobutanone,”TheJournalofChemical
31S.W.BensonandG.B.Kistiakowsky,“ThePhotochemicalDe- Physics160,134310(2024).
compositionofCyclicKetones,”JournaloftheAmericanChem- 48E.R.Miller,S.J.Hoehn,A.Kumar,D.Jiang, andS.M.Parker,
icalSociety64,80–86(1942). “Ultrafast photochemistry and electron diffraction for cyclobu-
32R. J. Campbell, E. W. Schlag, and B. W. Ristow, “Mecha- tanone in the S2 state: Surface hopping with time-dependent
nistic consequences of curved Stern-Volmer plots. Photolysis of densityfunctionaltheory,”TheJournalofChemicalPhysics161,
cyclobutanone,” Journal of the American Chemical Society 89, 034105(2024).
5098–5102(1967). 49S.Mukherjee,R.S.Mattos,J.M.Toldo,H.Lischka, andM.Bar-
33E. K. C. Lee, “Laser photochemistry of selected vibronic and batti, “Prediction Challenge: Simulating Rydberg photoexcited
rotational states,” Accounts of Chemical Research 10, 319–326 cyclobutanonewithsurfacehoppingdynamicsbasedondifferent
(1977). electronicstructuremethods,”TheJournalofChemicalPhysics
34E.W.-G.Diau,J.L.Herek,Z.H.Kim, andA.H.Zewail,“Fem- 160,154306(2024).
tosecondActivationofReactionsandtheConceptofNonergodic 50J. Peng, H. Liu, and Z. Lan, “The photodissociation dynamics
Molecules,”Science279,847–851(1998). and ultrafast electron diffraction image of cyclobutanone from
35E.W.-G.Diau,C.K¨otting, andA.H.Zewail,“Femtochemistry thesurfacehoppingdynamicssimulation,”TheJournalofChemofNorrishType-IReactions: II.TheAnomalousPredissociation icalPhysics160,224305(2024).
DynamicsofCyclobutanoneontheS1Surface,”ChemPhysChem 51P.Vindel-ZandbergenandJ.Gonz´alez-Va´zquez,“Non-adiabatic
2,294–309(2001). dynamics of photoexcited cyclobutanone: Predicting struc-
36M.-H.Kao,R.K.Venkatraman,M.N.R.Ashfold, andA.J.Orr- turalmeasurementsfromtrajectorysurfacehoppingwithXMS-
Ewing,“Effectsofring-strainontheultrafastphotochemistryof CASPT2 simulations,” The Journal of Chemical Physics 161,
cyclicketones,”ChemicalScience11,1991–2000(2020). 024104(2024).
37O.Bennett,A.Freibert,K.E.Spinlove, andG.A.Worth,“Pre- 52H.Akimoto,AtmosphericReactionChemistry (Springer,Berlin,
diction through quantum dynamics simulations: Photo-excited Heidelberg,2016).
cyclobutanone,” The Journal of Chemical Physics 160, 174305 53M. L. Hause, N. Herath, R. Zhu, M. C. Lin, and A. G. Suits,
(2024). “Roaming-mediatedisomerizationinthephotodissociationofni-
38J.Eng,C.D.Rankine, andT.J.Penfold,“Thephotochemistry trobenzene,”NatChem3,932–937(2011).
of Rydberg-excited cyclobutanone: Photoinduced processes and 54T. Endo, S. P. Neville, V. Wanie, S. Beaulieu, C. Qu, J. Deground state dynamics,” The Journal of Chemical Physics 160, schamps, P. Lassonde, B. E. Schmidt, H. Fujise, M. Fushitani,
154301(2024). A.Hishikawa,P.L.Houston,J.M.Bowman,M.S.Schuurman,
39D. Hait, D. Lahana, O. J. Fajen, A. S. P. Paz, P. A. Unzueta, F.L´egar´e, andH.Ibrahim,“Capturingroamingmolecularfrag-
B. Rana, L. Lu, Y. Wang, E. F. Kjønstad, H. Koch, and T. J. mentsinrealtime,”Science370,1072–1077(2020).
Mart´ınez, “Prediction of photodynamics of 200 nm excited cy- 55L.O’Toole,P.Brint,C.Kosmidis,G.Boulakis, andP.Tsekeris,
clobutanonewithlinearresponseelectronicstructureandabini- “Vacuum-ultravioletabsorptionspectraofpropanone,butanone
tio multiple spawning,” The Journal of Chemical Physics 160, andthecyclicketonesCnH2n−2O(n=4,5,6,7),”Journalofthe
244101(2024). ChemicalSociety,FaradayTransactions87,3343–3351(1991).
40L. Hutton, A. Moreno Carrascosa, A. W. Prentice, M. Simmer- 56T.S.Kuhlman,S.P.A.Sauer,T.I.Sølling, andK.B.Møller,
macher,J.E.Runeson,M.J.Paterson, andA.Kirrander,“Using “Symmetry, vibrational energy redistribution and vibronic couamultistatemappingapproachtosurfacehoppingtopredictthe pling: The internal conversion processes of cycloketones,” The
ultrafastelectrondiffractionsignalofgas-phasecyclobutanone,” JournalofChemicalPhysics137,22A522(2012).
TheJournalofChemicalPhysics160,204307(2024). 57K. Tamagawa and R. L. Hilderbrandt, “Molecular structure of
41V. K. Jaiswal, F. Montorsi, F. Aleotti, F. Segatta, D. Keefer, cyclobutanone as determined by combined analysis of electron
S. Mukamel, A. Nenov, I. Conti, and M. Garavelli, “Ultrafast diffraction and spectroscopic data,” The Journal of Physical
photochemistryandelectron-diffractionspectrainn→(3s)Ry- Chemistry87,5508–5516(1983).
dberg excited cyclobutanone resolved at the multireference per- 58W.M.Stigliani,V.W.Laurie, andL.H.Scharpen,“Structure
turbative level,” The Journal of Chemical Physics 160, 164316 ofcyclobutanone,”JournalofMolecularSpectroscopy62,85–89
(2024). (1976).
42J. Janoˇs, J. P. Figueira Nunes, D. Hollas, P. Slav´ıˇcek, and 59J.C.HemmingerandE.K.C.Lee,“FluorescenceExcitationand
B. F. E. Curchod, “Predicting the photodynamics of cyclobu- PhotodecompositionoftheFirstExcitedSingletCyclobutanone
tanone triggered by a laser pulse at 200 nm and its MeV-UED (1A2): A Study of Predissociation of and Collisional Energy
signals—A trajectory surface hopping and XMS-CASPT2 per- Transfer from the Vibronically Selected Species,” The Journal
spective,”TheJournalofChemicalPhysics160,144305(2024). ofChemicalPhysics56,5284–5295(1972).
43J. E. Lawrence, I. M. Ansari, J. R. Mannouch, M. A. Manae, 60S. Pedersen, J. L. Herek, and A. H. Zewail, “The Validity of
K.Asnaashari,A.Kelly, andJ.O.Richardson,“AMASHsim- the ”Diradical” Hypothesis: Direct Femtoscond Studies of the
ulation of the photoexcited dynamics of cyclobutanone,” The Transition-StateStructures,”Science266,1359–1364(1994).
JournalofChemicalPhysics160,174306(2024). 61M.Koch,T.J.A.Wolf, andM.Gu¨hr,“Understandingthemod-
44D.V.Makhov,L.Hutton,A.Kirrander, andD.V.Shalashilin, ulation mechanism in resonance-enhanced multiphoton prob-
“Ultrafastelectrondiffractionofphotoexcitedgas-phasecyclobu- ing of molecular dynamics,” Physical Review A 91, 031403(R)
tanonepredictedbyabinitiomultiplecloningsimulations,”The (2015).
JournalofChemicalPhysics160,164310(2024). 62K.A.Trentelman,D.B.Moss,S.H.Kable, andP.L.Houston,
45A. Mart´ın Santa Dar´ıa, J. Hern´andez-Rodr´ıguez, L. M. Ibele, “The 193-nm photodissociation of cyclobutanone: dynamics of
andS.G´omez,“Photofragmentationofcyclobutanoneat200nm: the C2 and C3 channels,” The Journal of Physical Chemistry
TDDFTvsCASSCFelectrondiffraction,”TheJournalofChem- 94,3031–3039(1990).
icalPhysics160,114303(2024). 63M.Kasha,“Characterizationofelectronictransitionsincomplex
46X. Miao, K. Diemer, and R. Mitri´c, “A CASSCF/MRCI tra- molecules,”Discuss.FaradaySoc.9,14–19(1950).
jectorysurfacehoppingsimulationofthephotochemicaldynam- 64T.S.Kuhlman,T.I.Sølling, andK.B.Møller,“CoherentMoics and the gas phase ultrafast electron diffraction patterns of tionRevealsNon-ErgodicNatureofInternalConversionbetween
cyclobutanone,” The Journal of Chemical Physics 160, 124309 ExcitedStates,”ChemPhysChem13,820–827(2012).

<!-- Page 14 -->

14
65T. S. Kuhlman, M. Pittelkow, T. I. Sølling, and K. B. Møller, 72T. J. A. Wolf, “Diffraction simulation
“PullingtheLeversofPhotophysics: HowStructureControlsthe https://github.com/thomasjawolf/diffraction simulation,”
RateofEnergyDissipation,”AngewandteChemieInternational .
Edition52,2247–2250(2013). 73F. Salvat, A. Jablonski, and C. J. Powell, “ELSEPA—Dirac
66M.-F. Lin, A. H. Reid, X. Shen, and T. J. A. Wolf, “Imaging partial-wave calculation of elastic scattering of electrons and
Ultrafast Structural Dynamics with Megaelectronvolt Ultrafast positrons by atoms, positive ions and molecules,” Computer
Electron Diffraction,” in Structural Dynamics with X-ray and PhysicsCommunications165,157–190(2005).
Electron Scattering (RSCPublishing,2023). 74L. S. Bartell and R. M. Gavin, “Effects of Electron Correlation
67X. Shen, J. P. F. Nunes, J. Yang, R. K. Jobe, R. K. Li, M.-F. in X-Ray and Electron Diffraction,” Journal of the American
Lin, B. Moore, M. Niebuhr, S. P. Weathersby, T. J. A. Wolf, ChemicalSociety86,3493–3498(1964).
C. Yoneda, M. Guehr, M. Centurion, and X. J. Wang, “Fem- 75J.P.F.Nunes,M.Williams,J.Yang,T.J.A.Wolf,C.D.Ranktosecondgas-phase mega-electron-volt ultrafast electrondiffrac- ine, R. Parrish, B. Moore, K. Wilkin, X. Shen, M.-F. Lin,
tion,”StructuralDynamics6,054305(2019). K. Hegazy, R. Li, S. Weathersby, T. J. Martinez, X. J. Wang,
68F. Neese, “Software update: The ORCA program sys- and M. Centurion, “Photo-induced structural dynamics of o -
tem—Version5.0,”WIREsComputationalMolecularScience12, nitrophenolbyultrafastelectrondiffraction,”PhysicalChemistry
e1606(2022). ChemicalPhysics26,17991–17998(2024).
69F. Neese, F. Wennmohs, A. Hansen, and U. Becker, “Efficient, 76A. L. Bennani, A. Duguet, and H. F. Wellenstein, “Differenapproximate and parallel Hartree–Fock and hybrid DFT calcu- tialcrosssectionsfor35keVelectronselasticallyscatteredfrom
lations. A ‘chain-of-spheres’ algorithm for the Hartree–Fock ex- NH3,”JournalofPhysicsB:AtomicandMolecularPhysics12,
change,”ChemicalPhysicsMovingFrontiersinQuantumChem- 461–472(1979).
istry:,356,98–109(2009). 77I. Hargittai and M. Hargittai, Stereochemical Applications of
70B. Helmich-Paris, B. de Souza, F. Neese, and R. Izsa´k, “An Gas-Phase Electron Diffraction, Part A (John Wiley & Sons,
improvedchainofspheresforexchangealgorithm,”TheJournal 1988).
ofChemicalPhysics155,104109(2021). 78A.Duguet,A.Lahmam-Bennani, andM.Rouault,“Highenergy
71F. Neese, “The SHARK integral generation and digestion sys- elastic and inelastic electron scattering by the NH3 moleculetem,”JournalofComputationalChemistry44,381–396(2023). bindingeffect,”TheJournalofChemicalPhysics78,6595–6597
(1983).