---
title: "Knowledge Enhanced LLMs Scientific Research"
original_file: "./Knowledge_Enhanced_LLMs_Scientific_Research.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["prompt-engineering", "llm", "rag", "chain-of-thought", "react"]
keywords: ["perovskite", "llm", "chat", "page", "knowledge", "materials", "reasoning", "performance", "agent", "model"]
summary: "<!-- Page 1 -->

Perovskite-LLM: Knowledge-Enhanced Large Language Models for

### Perovskite Solar Cell Research

XiangLiu1,∗ PengleiSun1,∗ ShuyanChen1,2 LonghanZhang1,2
PeijieDong1 HuajieYou1 YongqiZhang1 ChangYan1,2

### XiaowenChu1,2,† Tong-yiZhang1,2,†

1TheHongKongUniversityofScienceandTechnology(Guangzhou)
2GuangzhouMunicipalKeyLaboratoryofMaterialsInformatics
Abstract makingitincreasinglychallengingforresearchers
toefficientlyaccessandutilizethevastamountof

### Therapidadvancementofpero"
related_documents: []
---

# Knowledge Enhanced LLMs Scientific Research

<!-- Page 1 -->

Perovskite-LLM: Knowledge-Enhanced Large Language Models for

### Perovskite Solar Cell Research

XiangLiu1,∗ PengleiSun1,∗ ShuyanChen1,2 LonghanZhang1,2
PeijieDong1 HuajieYou1 YongqiZhang1 ChangYan1,2

### XiaowenChu1,2,† Tong-yiZhang1,2,†

1TheHongKongUniversityofScienceandTechnology(Guangzhou)
2GuangzhouMunicipalKeyLaboratoryofMaterialsInformatics
Abstract makingitincreasinglychallengingforresearchers
toefficientlyaccessandutilizethevastamountof

### Therapidadvancementofperovskitesolarcells

knowledge in this field. This challenge is partic-
(PSCs)hasledtoanexponentialgrowthinresearch publications, creating an urgent need ularlyacutegiventhecomplexinterplaybetween
forefficientknowledgemanagementandrea- material composition, fabrication processes, and
soning systems in this domain. We present devicestructurethatcharacterizesPSCresearch.
acomprehensiveknowledge-enhancedsystem Traditionalapproachestoscientificknowledge
forPSCsthatintegratesthreekeycomponents.
management, such as literature reviews and
First, we develop Perovskite-KG, a domaindatabases,whilevaluable,arelimitedintheirabilspecific knowledge graph constructed from
itytocapturetheintricaterelationshipsbetweendif-
1,517 research papers, containing 23,789 enferentaspectsofPSCresearch(Yangetal.,2024b;
tities and 22,272 relationships. Second, we
createtwocomplementarydatasets:Perovskite- Hanetal.,2025). Furthermore,existingartificial
Chat,comprising55,101high-qualityquestion- intelligencesystemsinmaterialssciencetypically
answerpairsgeneratedthroughanovelmulti- focusonspecificpredictiontasksorgeneralscienagent framework, and Perovskite-Reasoning, tificknowledge,lackingthespecializedcapability
containing 2,217 carefully curated materials
tohandletheuniquecharacteristicsoftheresearch
science problems. Third, we introduce two
of perovskite solar cells and more general matespecializedlargelanguagemodels: Perovskiterials science research (Han et al., 2025; Seifrid
Chat-LLMisusedfordomain-specificknowledge assistance, and Perovskite-Reasoning- etal.,2022;Mishraetal.,2024;Songetal.,2023a;
LLMisusedforscientificreasoningtasks. Ex- Schilling-Wilhelmi et al., 2025; Miret and Krishperimentalresultsdemonstratethatoursystem nan, 2024). This gap highlights the need for an
significantly outperforms existing models in integratedsystemthatcanbothsystematicallyordomain-specific knowledge retrieval and sciganizedomainknowledgeandprovideintelligent
entificreasoningtasks,providingresearchers
assistancetoresearchers.
witheffectivetoolsforliteraturereview,exper-
Toaddressthesechallenges,wepresentacomimentaldesign,andcomplexproblemsolving
prehensive knowledge-enhanced system specifiinPSCresearch.
callydesignedfortheperovskitesolarcelldomain,
consistingofthreekeycomponents. First,wede-
1 Introduction
velop Perovskite-KG, a domain-specific knowl-
Perovskitesolarcells(PSCs)haveemergedasone edge graph constructed from 1,517 research artiofthemostpromisingnext-generationphotovoltaic cles,containing23,789entitiesand22,272relationtechnologies,achievingremarkableprogresswith ships between manufacturing processes, paramepower conversion efficiencies (PCEs) exceeding ters,andperformancemetrics. Second,wecreatea
27.0% within just over a decade (National Re- multi-agentframeworkforgeneratinghigh-quality
newable Energy Laboratory, 2025; Snaith, 2018; instruction-tuning data, which not only reduces
Correa-Baena et al., 2017; Wu et al., 2021; Ang annotation costs but also ensures high reliability
etal.,2022;Sathayeetal.,2011;Bogdanovetal., andlowhallucinationthroughthesynergyofmul-
2019). TherapiddevelopmentofPSCshasgener- tiplespecializedagentsandexpertguidance. This
atedanexponentialgrowthinresearchpublications, frameworkgeneratestwocomplementarydatasets:
∗EqualContribution. (1)Perovskite-Chat,aninstruction-tuningdataset
†CorrespondingAuthor. comprising 55,101 high-quality question-answer
5202
tcO
9
]IA.sc[
3v96621.2052:viXra

<!-- Page 2 -->

pairs generated from 2,214 high-impact papers research thrusts have emerged: (1) structured inusing a novel multi-agent framework, and (2) formationextractionfromheterogeneouscorpora,
Perovskite-Reasoning,acollectionof2,217care- (2)knowledgegraphembeddingsforcompositionfullycuratedmaterialsscienceproblemsdesigned propertyrelationships,and(3)neurosymbolicreatoenhancescientificreasoningcapabilities. Third, soningforsynthesispathwayoptimization(Seifrid
weintroducetwospecializedlargelanguagemod- etal.,2022;Mishraetal.,2024;Songetal.,2023a;
els: Perovskite-Chat-LLM for domain-specific Schilling-Wilhelmi et al., 2025; Miret and KrishknowledgeassistanceandPerovskite-Reasoning- nan,2024).
LLMfortacklingcomplexmaterialssciencerea- Building upon these foundations, knowledgesoning tasks. Our work makes the following key enhanced systems have achieved state-of-thecontributions: art performance through two complementary
❶Constructionofacomprehensiveperovskite paradigms: graph-basedapproachesemployinghetknowledge graph. We construct the first com- erogeneousgraphneuralnetworks(HGNNs)now
prehensive knowledge graph for perovskite solar attain89.7%accuracyonmulti-hopmaterialpropcells, organizing domain knowledge into a struc- erty queries (An et al., 2024), while agent-based
turedformatthatcapturestherelationshipsbetween frameworks demonstrate 18.7% improvement in
materials,processes,anddeviceperformance. autonomousexperimentaldesignthroughchain-of-
❷Multi-agentframeworkforhigh-qualitydata thoughtprompting(Zhangetal.,2024a;Songetal.,
generation. Weproposeaneffectivemulti-agent 2023b;Guptaetal.,2022;Hiraetal.,2024).
frameworkforgeneratinghigh-qualityinstruction- The field’s maturation is further evidenced by
tuning data, resultingin two specialized datasets: systematicresourcedevelopment: (i)TheSciQAG
a diverse domain-specific dataset covering seven framework (Wan et al., 2024) introduces a novel
researchcategoriesandafocusedreasoningdataset curriculumlearningparadigmforgenerating120K
forenhancingscientificproblemsolvingcapabili- domain-specificQApairs,reducingexpertannotaties. tionrequirementsby78%;(ii)Standardizedeval-
❸ Specialized LLMs for perovskite research. uationnowspanschemicalsynthesis(ChemLLM-
Bench’sreactionyieldpredictiontask(Guoetal.,

### Wedevelopandevaluatetwospecializedlargelan-

2023)), biomedical applications (MultiMedQA’s
guagemodelsforperovskitesolarcellsthatdemontoxicitypredictionchallenge(Singhaletal.,2023)),
stratesuperiorperformancecomparedtobaseline
andcross-domainreasoning(SciEval’smaterialsmodels: oneoptimizedfordomain-specificqueries
deviceco-designtrack(Sunetal.,2023)).
andanotherforscientificreasoningtasks.
❹ Extensive experimental validation. We pro-
2.2 KnowledgeGraphinMaterialsScience
vide extensive experimental results showing the

### Domain-specificknowledgegraphshaveevolved

effectivenessofourintegratedsysteminsupportintostructuredsemanticframeworksthatsystemingvariousresearchtasks,fromliteraturereviewto
atically consolidate heterogeneous multi-source
experimentaldesignandcomplexproblemsolving
datathroughmachine-readablerepresentations,alinmaterialsscience.
lowingcross-domainknowledgeintegrationtoac-
2 RelatedWork celerate discovery pipelines (Pan et al., 2024c;
Song et al., 2024; Zhu et al., 2022; Bordes et al.,
2.1 LLMinMaterialsScience
2013; Galkin et al.). In materials informatics,
Theconvergenceoflanguagemodelingandcom- current implementations manifest two distinct
putationalmaterialssciencehasunlockedtransfor- paradigms: literature-derivedsystemsexemplified
mativepotentialforrapiddiscovery. Recentbreak- by MatKG (Venugopal and Olivetti, 2024) and
throughsindomain-specificarchitectures(e.g. hi- DISCOMAT (Gupta et al., 2023), which employ
erarchicalattentionmechanisms(Kononovaetal., NLPandgraphtechniquestoextractmaterialcom-
2021)andmultimodalfusionnetworks(Swainand positions from textual sources, while empirical
Cole,2016))haveaddressedcriticalchallengesin architectures represented by MatSciKB (Zhang
crystal structure prediction (Walker et al., 2021) etal.,2024b),Propnet(Mrdjenovichetal.,2020),
andphasediagramanalysis(Trewarthaetal.,2022). MekG(Stattetal.,2023),andMOF-KG(Anetal.,
AsevidencedbytheMaterialsGenomeInitiative 2022)focusonencodingexperimentalprovenance
benchmarks (Tshitoyan et al., 2019), three main and computational models through graph-based

<!-- Page 3 -->

representations of material lineages. However, zation(Mrdjenovichetal.,2020),asshowninthe
these approaches face the challenges that man- Appendix A.
ualcurationprocessesfacewithresourceburdens,
2.4 Reasoningalignment
whileexistingextractionmethodsexhibitlimited
granularityinresolvingcomplexsynthesis-process- Recentadvancesinparameter-efficientalignment
propertyrelationshipsfromunstructuredtext. To havewitnessedmultipleresearchteamspursuedifaddress these limitations, we propose an LLM- ferentmethodologiestoaligntheperformanceof
driven framework specifically optimized for per- o1(OpenAI,2024). Contemporaryapproachesbiovskitematerialsresearchthatfeaturesahybridar- furcatealongtwotechnicalaxes: (1)reinforcement
chitecturethatsynergizesdomainontologieswith learningparadigmsexemplifiedbyDeepSeek-R1’s
self-supervisedrelationshipextraction,augmented adversarial preference optimization (Guo et al.,
byautomatedqualitycontrolpipelinesthatenforce 2025)andK1.5’smulti-objectiverewardshaping
materialsscienceconstraints. (Team et al., 2025), versus (2) supervised finetuning strategies employing distilled datasets at
2.3 Multi-agentsystems scale(≥ 104 examples)asdemonstratedin(Team,
ThelandscapeofAIsystemarchitecturesencom- 2025; Xu et al., 2025; Labs, 2025). In particular,
passestwodistinctparadigms: multi-agentsystems S1(Muennighoffetal.,2025)andLIMO(Yeetal.,
andautonomousagents (Zhugeetal.,2023;Hong 2025)operationalizetheSuperficialAlignmentHyetal.,2024a;Zhangetal.,2024c;Wangetal.,2023; pothesis(Zhouetal.,2023a)throughcurriculum-
Suetal.,2025). Whileautonomousagentsrelyon basedsparsefine-tuning,achievingcomparablereaindependent decision-making capabilities, multi- soningcapabilitieswithmerely1,000-2,000careagentsystemsexcelthroughstructuredcollabora- fullycuratedexamples,a92%reductioninannotation between specialized components. The latter tioncostsrelativetoconventionalSFTapproaches.
approach offers practical advantages by building
3 Perovskite-KG
upon established expertise rather than requiring
complexbehavioralmodeling.
• Document Filtering. Drawing upon expert

### Researchinmulti-agentframeworkshasevolved

knowledge,wehavedevelopedtheschemaforperalong two primary trajectories. The first focuses
ovskitematerials. Thisschema,shownintheApon domain-agnostic systems that leverage collecpendix Table 6, integrates three ontologies {o |
i
tiveintelligenceforgeneralproblem-solving (Wei
o ∈ schema}: fabrication,parameters,andperfori
et al., 2022; Diao et al., 2024; Wang et al., 2022;
mance. Thefabricationontologyencompassesthe
Madaanetal.,2023;Wangetal.,2024). Thesecproceduresandconditionsrequiredtosynthesize
ondpathwayexploresdomain-specificapplications,
perovskitematerials. Theparametersontologydewithnotableimplementationsin: Codegeneration
fines the ingredients, structural components, and
anddebugging (Hongetal.,2024b;Ridniketal.,
other compositional aspects of the device. The
2024; Zhong et al., 2024a), Data analytics (Xie
performance ontology is concerned with the effietal.,2024;Yeetal.,2024;Lietal.,2024;Zhou
ciencyandfunctionalcharacteristicsofperovskite
et al., 2023b), Mathematical reasoning (Zhong
devices. Each ontology o is further divided into
i
et al., 2024b; Xu et al., 2024; Pan et al., 2024b), sub-ontologies so (j) , where o = Sni so (j) and
Knowledgeretrieval (Norietal.,2023;Zhouetal., i i j=1 i
n representsthenumberofsub-ontologieswithin
i
2024)
(j)
o . Each sub-ontology so provides a domain-
Despitesignificantprogressinidentifyingeffec- i i
(j)
specific description, denoted as d , along with
tiveagentconfigurationsforspecificusecases,the i
(j)
fieldstillfacesthechallengeofdevelopingsystem- acorrespondingdatatype,denotedast ,thatis
i
aticapproachesfornewdomains. Thishighlights relevanttoitsparticularscope.
(j) (j) (j)
theimportanceofresearchintoautomatedmethods For each sub-ontology [so ,d ,t ] (e.g.,
i i i
forframeworkdesignandoptimization. ”CoatingParameter”-”Detailsaboutthecoating
In this section, we collect 1,517 paper in per- methodusedinthematerialdepositionprocess”-
ovskite domain to build Perovskite-KG and de- ”Float”),wecreatethepromptstoquerydocuments
signtheautomaticknowledgegraphconstruction D = {D | k = 1,...,m}usingalargelanguage
k
pipelineincludingthreestagesdocumentfiltering, model. Thesepromptsfacilitatetheextractionof
knowledgeextractingandknowledgegraphorgani- relevant information for each sub-ontology. The

<!-- Page 4 -->

StageI: Document Filtering StageII: Knowledge Extracting StageIII: Knowledge Graph Organization

### Disambiguation

Documents Do F c il u te m re e d nts Do F c il u te m re e d nts Entity Entity

### LLM LLM Graph

Kn E o x w p l e e r d t ge De S s c c h r e ip m ti a on LLM Schema Relationship
Deduplication
Relationship

### Database


### LLMDatasetGeneration Perovskite-LLM

Collaborative Multi-Agent Construction of KG/RAGprovide Instruction Tuning Dataset
Perovskite Large Model Training Data citationdata Perovskite-Chat

### Information

Extraction Agent

### ReasoningDataset

Quality Perovskite-Reasoning
Validation Agent

### Document


### Summar. Agent

Figure1: ThepipelineofPerovskite-KGconstructionandPerovskite-LLM.
outputD (i,j) isdefinedas: identifyingandmergingredundantrelationsinthe
filtered
knowledgegraph. Forinstance,giventworelations
r = (e ,r,e )andr = (e′,r′,e′),iftheyconvey
i 1 2 j 1 2
D (i,j) = {D ∈ D | so (j) ⊂ D }, (1) thesamesemanticmeaning—thatis,if(e ,e )and
filtered k i k 1 2
(e′,e′)refertoidenticalentitiesandtherelations
1 2
where D (i,j) represents the set of filtered docu- r andr′ areequivalent.
filtered
mentscontainingpertinentdetailsforsub-ontology •KnowledgeGraphOrganization. Weconstruct
so (j) acrossthecollection. Thisapproachensures thePerovskiteKnowledgeGraph(Perovskite-KG)
i
a systematic and efficient retrieval of targeted in- using a graph database. The Perovskite-KG conformationforeachsub-ontology. sists of 23,789 entities and 22,272 relationships.
• Knowledge Extracting. We employ a prompt Byincorporatingcitationrelationshipsbetweenpafunction, denoted as f (·), to transform the pers,weenableourLLMtoprovidereferencesfor
prompt
(j) (j) (j) its responses, enhancing credibility and reducing
sub-ontology [so ,d ,t ] into a document
i i i
(j) (j) (j) hallucination.
prompt,representedasf (so ,d ,t ). To
prompt i i i
extractthepotentialdomainknowledgeK,weuti-
4 InstructionTuningDatasetGeneration
lize a pre-trained large language model (LLM),
expressedasLLM(·;θ),underazero-shotsetting
Inthissection,wecollect2,214thetoplevelpubliwhere the parameters θ remain fixed. The whole
cationspapersintheperovskitedomainanddesign
pipelinecanbeformulatedasbelow:
theinstructiontuningdatasetincludingquestionansweringandmultiplechoicequestions,containing
(j) (j) (j)

### K =search LLM(f (so ,d ,t );θ),

prompt i i i (2) 55,101instancesaround4.4milliontokens,named

### D(i,j)

filtered Perovskite-Chat. Ourexperimentsshowthatour
where the search function search(·) may involve perovskiteinstructiontuningdatasetcaneffectively
anargmaxoperationtoidentifythehighest-scoring improvetheperformanceofLLMsonperovskite
outputorasamplingapproachtogenerateoutputs relatedtasks.
accordingtotheprobabilitydistributionspecified Figure1illustratesthismulti-agentframework
bytheadoptedLLM(·;θ). forthegenerationofinstructiontuningdataset. The
After extracting knowledge, we conduct qual- processbeginswithexpertguidanceandacademic
ity control procedures to ensure accuracy and re- literaturefromvarioussources(includingScience,
liability. These procedures include entity disam- Nature, Elsevier, Springer, arXiv, and others) as
biguation and relationship deduplication. Entity input. Expertguidanceisprovidedbythedomain
disambiguation in a knowledge graph aims to re- expertfocusedon7researchcategories,21research
solve ambiguity by identifying the unique entity questions. Table1furtherexpandsthisclassificathatcorrespondstoanambiguousmention,denoted tion by presenting 21 specific research questions
ase ,withinasubgraph. Theobjectiveisto (Q1-Q21)organizedwithinthesesevencategories;
mention
determineadistinctentitye∗ thataccuratelyrepre- moredetailscanbefoundinAppendixC.1. These
sentse . Relationshipdeduplicationinvolves inputs feed into a multi-agent system: (1) an Inmention

<!-- Page 5 -->

formationExtractionAgentthatprocessestheraw
content, (2) a Quality Validation Agent that en- 43.9%
suresdataaccuracyandrelevance,and(3)aDocument Summarization Agent that condenses and

### Device Structure

structurestheinformation. Thisframeworkensures Perf. Enhancement

### Metrics

systematic, high-quality data processing through Stability
2.9% Defect & Recom.
multiplevalidationandrefinementstages. 20.4% 1.7% Interface

### Materials

Let D = {d ,...,d } represent the collection
1 n 13.1%
of academic literature from various sources, and
8.2%
E = {c ,...,c }denotetheexpertguidancecate- 9.8%
1 7
gorieswiththecorrespondingresearchquestions
(a) Thedistributionofquestioncategoriesintheinstruc-
Q = {q ,...,q }. The multi-agent framework
1 21 tiontuningdataset.
processes these inputs through three specialized
agents:

### InformationExtraction:

A (d ) = {x ,...,x } (3)
extract i 1 k
QualityValidation:
(
1, ifvalid
A (x ) = (4)
validate j
0, otherwise
(b) Thewordcloudoftheinstructiontuningdataset.
DocumentSummarization: Figure2: Thedistributionofquestioncategoriesinthe
instructiontuningdataset.

### A (X ) = y (5)

summarize valid
applyingkeyphysicalandchemicalprinciples,and
The final instruction tuning dataset D is conimplementingsystematicsolutionstrategieswith
structedas:
result validation. The resulting dataset features
detailedreasoningchainsthatdemonstratestep-by-

### D = {(q ,y ) | q ∈ Q,

i i i stepproblem-solvingprocesses,makingitvaluable
y = A (A (A (d )))} (6) fortrainingmodelsinscientificreasoningandmai summarize validate extract i
terialsscienceproblem-solving.

### Next, we introduce Perovskite-Reasoning, a

collectionof2,217high-qualityquestionsfrommaterialssciencetextbooks,designedtoenhancerea- TrainingDataset Figure2(a)presentsthedistrisoningcapabilitiesintheperovskiteandmaterials butionofthequestioncategoriesinthePerovskitesciencedomains. Thequestionsweresourcedfrom Chatinstructiontuningdataset. DeviceStructure
hundredsofwidelyusedmaterialsscienceandengi- dominates with 43.9% of all questions, followed
neeringtextbooks,withafocusonperovskitesolar byPerformanceEnhancementat20.4%. Device&
cellsandfundamentalmaterialsscienceconcepts. Recom. comprises13.1%,whileMetricsaccounts
Ourrigorousselectionprocessappliedthreekeycri- for8.2%. TheremainingcategoriesincludeStabilteria: clarityofproblemstatements,completeness ity(9.8%),Materials(2.9%),andInterface(1.7%).
ofsolution,andalignmentwithcorematerialssci- Figure2(b)displaysawordcloudvisualizationof
enceprinciples. Materialsscienceprofessorscon- thedataset’smostfrequentterms,with”perovskite
ductedexpertassessmentstocategorizequestions solar” and ”solar cell” appearing as predominant
bydifficultylevel,validatedthroughstudentperfor- phrases,reflectingthedataset’scorefocus. Other
mancedataandbaselinemodeltesting. Todevelop frequently occurring terms such as ”device struccomprehensive solution paths, we employed ad- ture,” ”configuration,” and ”stability” underscore
vancedlanguagemodelslikeDeepSeek-R1(Guo thekeytechnicalaspectsaddressed. Thisdistribuetal.,2025)andO1(OpenAI,2024)inamulti-step tiondemonstratesthedataset’sstrongemphasison
reasoning approach. This methodology involved devicestructuralaspects,withperformance-related
decomposingcomplexproblemsintologicalsteps, queriesformingthesecondlargestcategory.

<!-- Page 6 -->


### Category Rationale

DeviceStructure Fundamentalaspectsfocusingonhigh-efficiency(>25%PCE)device
architectureandfabricationprocesses(Q1-Q3)
Perf. Enhancement Analysisofproblem-solvingapproachesandstrategicchoicesinhighperformancedevices(Q4-Q5)
Metrics Keyperformanceindicators(V ,FF,J )andtheiroptimizationmeth-

## Oc Sc

ods(Q6-Q9)
Stability Criticalstabilityaspectsaddressingmaindegradationpathways: moisture,thermal,andlightstability(Q10-Q12)
Defect&Recom. Fundamental mechanisms affecting device efficiency through defect
passivationandrecombinationcontrol(Q13-Q14)
Interface Interfaceengineeringandchargetransportoptimization(Q15-Q17)
Materials Comprehensiveanalysisoffunctionalmaterialsandtheircharacteristics
indifferentdevicecomponents(Q18-Q21)
Table1: ClassificationofResearchQuestionsinPerovskiteSolarCellStudies
Evaluation Dataset For better evaluation, we Reasoning,weincorporatedMinerva(Lewkowycz
design the evaluation dataset including multiple etal.,2022)andGPQADiamond(Reinetal.,2023)
choicequestionsandquestionansweringintheper- asabenchmark. Thesecontainundergraduateand
ovskitedomain. Theevaluationdatasetalsoextract PhD level science questions from biology, chemfrom the top level publications in perovskite do- istry,andphysics.
main with our multi-agent framework and extral
expert double check. The evaluation dataset con- 5 Perovskite-LLM
tains1,103questionansweringnamedPerovskite
5.1 ExperimentDesign

### QA and 1,103 multiple choice questions named

PerovskiteMCQ. In this section, we conduct the instruction tuning experiments on the Perovskite-Chat and

### For question answering, we set the Rouge-L

Perovskite-Reasoning dataset. We select the
scoreandtheLLM-as-a-Judge(Zhengetal.,2023)

### LLaMA-3.1-8B-Instruct(Dubeyetal.,2024)and

scoreastheevaluationmetric. Inourexperiments,
Qwen-2.5-7B-Instruct(Yangetal.,2024a)asthe
wefindthatbothmetricscaneffectivelymeasure
baseline model, and Perovskite-Chat-LLM and
thequalityofquestionansweringandconsistency
Perovskite-Reasoning-LLM are fine-tuned verwitheachother.
sion of LLaMA-3.1-8B-Instruct and Qwen-2.5-

### Formultiplechoicequestions,wesettheaccu-

7B-InstructwithPerovskite-ChatandPerovskiteracyastheevaluationmetric. UsingLLaMA-3.1-

### Reasoningdataset. Forthetrainingmethodology,

8B-Instruct (Dubey et al., 2024) as the baseline
we employed a full fine-tuning approach. While
model,thedifficultylevelofeachquestionisdeter-

### Parameter-EfficientFine-Tuning(PEFT)methods

minedbyitszeroshotperformance. Specifically,
likeLoRA(Huetal.,2021)areprominentfortheir
ifLLaMA-3.1-8B-Instructcancorrectlyanswera
efficiency, some studies suggest they can exhibit
question in a zero-shot setting (without any taskweaker convergence on downstream tasks comspecifictrainingorpromptengineering),weclaspared to full fine-tuning (Pan et al., 2024a). As
sifyitasan”easy”question. Conversely,questions
our computational resources were sufficient, we
that LLaMA-3.1-8B-Instruct fails to answer coroptedforfullfine-tuningtomaximizemodelperrectly are categorized as ”Hard”. This classificaformanceandadaptationtoourspecializeddatasets.
tionmethodresultedin823easyquestionsand280
WeleavetheexplorationofPEFTmethodsforfuhardquestionsinourevaluationdataset,providing
turework,especiallywhenscalingtolargermodabalancedassessmentofmodelcapabilitiesacross
els.
differentdifficultylevels.

### Forthetrainingprocess,weusedthefullparam-

To evaluate the performance of Perovskite- eterfine-tuningmethodtofine-tunethePerovskite-

<!-- Page 7 -->

LLM.TheexperimentiscarriedoutontheA800 Model LLM-Judge↑ HumanExpert↑

### GPUserver,withflashattention(Dao,2024)and GPT-4o 1.41 1.73

mixedprecisiontrainingforefficienttraining. For LLaMA-3.1-8B 1.28 1.17

### Perovskite-Chat-LLM 2.97 3.12

moredetailsonthetrainingprocess,pleasereferto
Table 2: Comparison of automatic and human expert
AppendixD.
evaluationscoresonthePerovskiteQAdataset.

### Fortheevaluationprocess,weusetheperplexity

(PPL), Rouge-L score, LLM-Judge, and Human-

### PerovskiteQA

JudgescoretoevaluatetheperformanceonthePer- Model

### PPL↓ Rouge-L↑ LLM-Judge↑

ovskite QA benchmark, the accuracy to evaluate

### GPT-3.5-Turbo - 11.24 1.24

the performance on the Perovskite MCQ bench- GPT-4o-Mini - 11.90 1.34

### GPT-4o - 11.36 1.41

mark,andthepass@1rateonMinervaandGPQA
benchmarks to evaluate the performance on the LLaMA-3.1-8B 6.77 13.18 1.28

### LLaMA-3.1-70B 4.98 17.38 1.80

Perovskite-Reasoning-LLM.Allexperimentsare

### Qwen-2.5-7B 6.23 11.22 1.39

conductedwithzero-shotsettingsandthreetimes Qwen-2.5-72B 5.12 10.17 1.31
Perovskite-Chat-LLM 2.97 41.25 2.97
togettheaverageresults.
+Perovskite-KG 2.80 43.10 3.15
5.2 Resultsandanalysis Table 3: Performance of Perovskite-Chat-LLM on

### PerovskiteQA

Perovskite-Chat-LLM Table3presentstheevaluationresultsofvariousmodelsonthePerovskite
QA dataset. The baseline models include GPT- Table4presentstheevaluationresultsofvarious
3.5-Turbo, GPT-4o-Mini, GPT-4o, LLaMA-3.1- modelsonthePerovskiteMCQdataset,categorized
8B. Among these, Perovskite-Chat-LLM demon- intoEasy,Hard,andAlldifficultylevels. Among
strates superior performance across all metrics, these, GPT 4o achieves the highest overall score
achieving a perplexity of 2.97, a Rouge-L score of84.68,withscoresof91.37forEasyand65.00
of 41.25, and an LLM-Judge score of 2.97. This for Hard questions. Perovskite-Chat-LLM, highrepresentsasignificantimprovementoverthebase- lighted in red, shows strong performance with a
line LLaMA-3.1-8B model. The GPT family of score of 62.86 on Hard questions, the highest in
models,whilecompetitiveintermsofLLM-Judge thiscategory,andanoverallscoreof87.22.
scores, showed lower performance in Rouge-L
scores compared to Perovskite-Chat-LLM, with Perovskite MCQ

### Model


### GPT-4oachieving11.36forRouge-Land1.41for Easy Hard All↑

LLM-Judge. WiththecasestudyinFigure3,we GPT-3.5-Turbo 86.63 49.29 77.15
can see that Perovskite-Chat-LLM can generate GPT-4o-Mini 89.79 61.79 82.68
more accurate and consistent answers compared GPT-4o 91.37 65.00 84.68
to other models, and ChatGPT only can offer a LLaMA-3.1-8B 100.00 0.00 74.21
generalandnonspecificanswerwhichleadstolow LLaMA-3.1-70B 93.44 66.43 86.58

### Qwen-2.5-7B 92.22 55.36 82.86

performanceontheRouge-LandLLM-Judgemet-
Qwen-2.5-72B 93.07 64.29 85.77
rics.

### Perovskite-Chat-LLM 95.50 62.86 87.22

To further validate the effectiveness and cred- +Perovskite-KG 97.32 65.10 89.21
ibility of our model, we incorporated human ex-
Table 4: Performance of Perovskite-Chat-LLM on
pertevaluationintoourassessmentmethodology.

### PerovskiteMCQ.TheLLaMA-3.1-8Bbaselinemodel’s

Table 2 presents the results of this human expert
performancedefinesEasy/Hardquestioncategories.
evaluation alongside the automatic metrics. Notably,Perovskite-Chat-LLMachievedthehighest Perovskite-Reasoning-LLM Table 5 presents
scoresinbothLLM-Judge(2.97)andHumanEx- the evaluation results of Perovskite-Reasoningpert (3.12) assessments, outperforming baseline LLM compared against various baseline models
modelssuchasGPT-4oandLLaMA-3.1-8B.This ontheGPQAandMinervabenchmarks. Inthe7B-
consistency across both human and LLM-Judge scale model category, our Perovskite-Reasoningevaluationsdemonstratestherobustnessandrelia- LLM achieves state-of-the-art performance with
bilityofourmodel,aswellasitsabilitytogenerate remarkabledataefficiencyover7Bmodels,requirresponsesthatarenotonlyaccuratebutalsoalign ingonly2Ktrainingexamplescomparedto800K
withexpertexpectationsinthefield. for R1-Qwen2.5-7B and 114K for OpenThinker-

<!-- Page 8 -->

7B.Ourmodelachieves43.95onGPQAand44.49 this knowledge integration, demonstrates an enonMinerva. Comparedto32Bmodels,whileour hancedcapabilitytoaccessup-to-dateinformation
GPQAperformanceshowsroomforimprovement anddeliverfine-grained,domain-specificresponses
(suggestingGPQA’ssensitivitytomodelsize),our comparedtoitsbaselineversionlackingsuchinte-
Minerva score (44.49) is competitive with larger gration. Forinstance,whenpresentedwithaquery
models like LIMO-32B (44.90) and approaches suchas,“CanyoutellmewhatisCuO?Andgive
S1-32B(47.79). Thisshowsthatourefficienttrain- me 5 usage in perovskite?”, the enhanced model
ing approach can achieve strong performance on providestherequesteddetails,witheachstatedus-
STEMreasoningtasksevenwithasmallermodel ageaccompaniedbyacitationfromtheunderlying
architecture. knowledgesource.
5.4 CaseStudy

### Model #ex GPQA↑ Minerva↑ Avg↑

APIModels ToillustratethepracticaladvantagesofPerovskiteo1 - 77.30 - - LLM over existing models, Figure 3 presents
o1-preview - 73.30 47.10 60.20
a comparative analysis of the responses of
o1-mini - 60.00 - -
Deepseek-R1 - 71.50 - - Perovskite-Chat-LLM and ChatGPT to a ques-
32B tion about the fabrication of high-efficiency per-
Qwen2.5-32B-Instruct - 48.00 41.20 44.60 ovskite solar cells. The responses demonstrate

### QwQ-32B-preview - 65.10 39.00 52.05

a clear distinction in the depth and specificity

## Limo-32B* 0.8K 66.70 44.90 55.80

S1-32B* 1K 59.60 47.79 53.69 of knowledge provided by each model. For in-
7B stance,Perovskite-Chat-LLMspecifiesprecisecon-
LLaMA-3.1-8BInstruct - 30.40 13.97 22.18 ditions for the HTL preparation (150°C for 15
R1-Qwen2.5-7B* 800K 44.49 25.25 34.87 minutes)anddetailsatwo-stepspin-coatingproce-

### R1-LLaMA3-8B* 800K 19.19 30.51 24.85

OpenThinker-7B* 114K 42.90 41.10 42.00 dure(1,000rpmfor10seconds,followedby6,000
Perovskite-R-LLM 2K 43.95 44.49 44.22 rpmfor30seconds)withspecificprocessmodifi-
Table 5: We evaluate the performance of Perovskite- cations like anisole addition. This level of detail
Reasoning-LLM on the GPQA and Minerva benchreflectsPerovskite-Chat-LLM’sspecializedtrainmarks. *indicatestheresultsarefromourevaluation.
ingondomain-specificliteratureanditsabilityto
# ex = number of examples used for fine-tuning. #
providepractical,implementation-readyguidance

### Perovskite-R-LLM:Perovskite-Reasoning-LLM

forresearchersinthefield. Formoredetails,please
5.3 IntegratePerovskite-KGwith refertoAppendixE.
Perovskite-Chat-LLM
6 Conclusion

### To ensure the Perovskit-Chat-LLM possesses

current and specialized knowledge, we employ In this work, we present a comprehensive
retrieval-augmentedgeneration(RAG)todynam- knowledge-enhanced system for perovskite solar
ically integrate information from our Perovskite- cell research, integrating three key components:
KG.Akeyadvantageofthisapproachisthecontin- (1)Perovskite-KG,adomain-specificknowledge
uousandautomaticupdatingoftheLLM’sknowl- graph containing 23,789 entities and 22,272 reedgebase,whichisdirectlyfacilitatedbytheauto- lationships; (2) multi-agent system for generatmatedconstructionmethodologyofthePerovskite- ingtwocomplementarydatasets,Perovskite-Chat
KGitself. Thetechnicalimplementationofthisin- and Perovskite-Reasoning, designed for domaintegrationleveragestheLightRAGframework(Guo specific knowledge assistance and scientific reaet al., 2024). The performance improvements re- soningrespectively;and(3)twospecializedlarge
sultingfromtheintegrationofPerovskite-KGwith language models that demonstrate superior per-
Perovskite-Chat-LLM(”+Perovskite-KG”)arepre- formance in both knowledge retrieval and reasented in Table 3 and Table 4. When enhanced soning tasks. Our experimental results show
bythePerovskite-KG,thePerovskite-Chat-LLM significant improvements over existing models,
demonstratesimprovedscoresinbothPerovskite withPerovskite-Chat-LLMachievingstate-of-the-
QA(2.97 → 3.15)andPerovskiteMCQ(87.22 → art performance on domain-specific tasks and
89.21). Representative case studies illustrating Perovskite-Reasoning-LLMshowingcompetitive
thesebenefitsaredetailedinFigure4andFigure10. performance on scientific reasoning benchmarks
The Perovskit-Chat-LLM, when augmented with despite using substantially fewer training exam-

<!-- Page 9 -->


### Question: 7 Limitations


### Howtofabricatetheperovskitesolarcells

thosecanreachPCEover25%? Despitethepromisingresults,ourcurrentsystem
Perovskite-Chat-LLM: hasseverallimitationsthatwarrantfutureinvesti-
... gation:
Fortheholetransportlayer(HTL),materials
likePEDOT:PSSarecommonlyused. These
• KnowledgeCoverage: Whileourknowledge
materialsarespin-coatedontothesubstrate
andannealedatatemperatureof 150°Cfor graphcoversasubstantialportionofthePSC
15minutes. Theperovskiteprecursorsoluliterature,itmaynotcaptureallemergingretionisthenpreparedusingamixedcationand
halidecomposition,andspin-coatedontothe searchdirectionsandnovelexperimentaltech-
HTL.Thespin-coatingprocessinvolvesatwoniques. Future work should focus on develstepprocedure: firstat1,000rpmfor10seconds,followedby6,000rpmfor30seconds, opingmechanismsforautomaticknowledge
withanisoleaddedduringthesecondstepto
base expansion and updates to maintain its
facilitatecrystallization.
... relevance.

### ChatGPT:

• Model Size Trade-offs: While our 7B-
...
PerovskiteMaterialQuality: Thequalityof parametermodelsachievecompetitiveperfortheperovskitematerialiscrucialforachieving
mance,theremightbecertaincomplextasks
highefficiency. Usehigh-qualityperovskite
precursorsandoptimizethefabricationprocess that benefit from larger model architectures,
toensureuniformanddefect-freeperovskite
suggesting a potential trade-off between effilms.
... ficiency and capability. Future work will investigatemodelcompressiontechniquesand
Figure3: ComparisonofresponsesbetweenPerovskitemoreefficientarchitectures.

### LLMandChatGPT:Perovskite-LLMprovidesdetailed

operationalstepswithspecificparameters,whileChat-
To address these limitations, our future work
GPTonlyoffersgeneralconceptualguidance.
will focus on three main directions: (1) developingacontinuousknowledgeintegrationframework
thatcanautomaticallyupdatetheknowledgebase

### Question:

CanyoutellmewhatisCuO?Andgiveme5 withnewresearchfindings,(2)enhancingthereausageinperovskite. soningcapabilitiesthroughadvancedmodelarchitecturesandtrainingstrategies,and(3)improving

### Perovskite-Chat-LLM:

... thesystem’spracticalutilitythroughbettervalida-

## HoleTransportMaterial: CuOactsasan

tionmechanismsandmoreefficientmodeldesigns.
effectiveholetransportmaterial(HTM)due
toitssuitableworkfunctionandhighhole These improvements will make the system more
mobility. Itisoftenusedinconjunctionwith
robust, up-to-date, and accessible to the broader
othermaterials,suchasNiO ,toenhance
x
theperformanceofPSCsbyfacilitatingeffi- researchcommunity.
cientchargeextraction[1].
...
Acknowledgments

### References:

[1]InorganicMaterialsasHoleSelectiveContactsandIntermediateTunnelJunctionLayer This work was supported by the Advanced
forMonolithicPerovskite-CIGSeTandemSolar

### Materials-National Science and Technology Ma-

Cells,Wang,Yajie;Wenisch,Robert;Schlatman jorProject(GrantNo. 2025ZD0620100),Guang-
...
dong Basic and Applied Basic Research Founda-
Figure4: AcasestudyofPerovskite-Chat-LLM’sabil- tion2025A1515010304,GuangzhouScienceand
ity to provide detailed and accurate information with TechnologyPlanningProject2025A03J4491
references.

### References

ples. Thesystemprovidesresearcherswitheffec-
Yuan An, Jane Greenberg, Alex Kalinowski, Xintive tools to review the literature, design exper- tong Zhao, Xiaohua Hu, Fernando J. Uribe-Romo,
iments, and solve complex problems in PSC re- Kyle Langlois, Jacob Furst, and Diego A. Go´mezsearch. Our work demonstrates the potential of Gualdro´n.2024. Knowledgegraphquestionanswering for materials science (kgqa4mat): Developing

### LLMs to accelerate innovation and discovery in

naturallanguageinterfaceformetal-organicframematerialssciencebyenablingmoreefficientknowlworksknowledgegraph(mof-kg)usingllm. Preprint,
edgeaccessandreasoningcapabilities. arXiv:2309.11361.

<!-- Page 10 -->

Yuan An, Jane Greenberg, Xintong Zhao, Xiaohua Taicheng Guo, Kehan Guo, Bozhao Nan, Zhenwen
Hu,ScottMcCLellan,AlexKalinowski,FernandoJ Liang, Zhichun Guo, Nitesh V. Chawla, Olaf
Uribe-Romo,KyleLanglois,JacobFurst,DiegoA Wiest, and Xiangliang Zhang. 2023. What can
Go´mez-Gualdro´n,etal.2022. Buildingopenknowl- large language models do in chemistry? a comedge graph for metal-organic frameworks (mof- prehensive benchmark on eight tasks. Preprint,
kg): Challenges and case studies. In 28TH ACM. arXiv:2305.18365.

## Sigkdd.Conference.Onknowledgedis-

COVERY.ANDDATAMINING. Zirui Guo, Lianghao Xia, Yanhua Yu, Tu Ao, and

### Chao Huang. 2024. Lightrag: Simple and fast

Tze-ZhangAng,MohamedSalem,MohamadKamarol, retrieval-augmented generation. arXiv preprint
HimadryShekharDas,MohammadAlhuyiNazari, arXiv:2410.05779.
andNatarajanPrabaharan.2022. Acomprehensive
studyofrenewableenergysources: Classifications, Tanishq Gupta, Mohd Zaki, Devanshi Khatsuriya,
challengesandsuggestions. EnergyStrategyReviews, KausikHira,NMAnoopKrishnan,etal.2023. Dis-
43:100939. comat: Distantlysupervisedcompositionextraction
fromtablesinmaterialssciencearticles. InProceed-
DmitriiBogdanov,JavierFarfan,KristinaSadovskaia,
ingsofthe61stAnnualMeetingoftheAssociationfor

### ArmanAghahosseini,MichaelChild,AshishGulagi,

ComputationalLinguistics(Volume1: LongPapers),
Ayobami Solomon Oyewo, Larissa de Souza Noel
pages13465–13483.

### SimasBarbosa,andChristianBreyer.2019. Radical

transformationpathwaytowardssustainableelectric-

### TanishqGupta,MohdZaki,NMAnoopKrishnan,and

ityviaevolutionarysteps. Naturecommunications,
Mausam. 2022. Matscibert: A materials domain
10(1):1–16.
languagemodelfortextminingandinformationextraction. npjComputationalMaterials,8(1):102.
Antoine Bordes, Nicolas Usunier, Alberto Garcia-
Duran, Jason Weston, and Oksana Yakhnenko.
Jiye Han, Keonwoo Park, Shaun Tan, Yana Vaynzof,

## Translatingembeddingsformodelingmulti-


### Jingjing Xue, Eric Wei-Guang Diau, Moungi G

relationaldata. Advancesinneuralinformationpro-
Bawendi, Jin-Wook Lee, and Il Jeon. 2025. Percessingsystems,26.
ovskitesolarcells. NatureReviewsMethodsPrimers,
Juan-Pablo Correa-Baena, Michael Saliba, Tonio 5(1):3.
Buonassisi,MichaelGra¨tzel,AntonioAbate,Wolfgang Tress, and Anders Hagfeldt. 2017. Promises Kausik Hira, Mohd Zaki, Dhruvil Sheth, NM Anoop
and challenges of perovskite solar cells. Science, Krishnan, et al. 2024. Reconstructing the materi-
358(6364):739–744. alstetrahedron: challengesinmaterialsinformation
extraction. DigitalDiscovery,3(5):1021–1037.

### TriDao.2024. FlashAttention-2: Fasterattentionwith

better parallelism and work partitioning. In Inter- Sirui Hong, Yizhang Lin, Bang Liu, Bangbang Liu,
national Conference on Learning Representations Binhao Wu, Danyang Li, Jiaqi Chen, Jiayi Zhang,
(ICLR). JinlinWang,LiZhang,LingyaoZhang,MinYang,

### MingchenZhuge,TaichengGuo,TuoZhou,WeiTao,


### ShizheDiao,PengchengWang,YongLin,RuiPan,Xi-

Wenyi Wang, Xiangru Tang, Xiangtao Lu, Xiawu
angLiu,andTongZhang.2024. Activeprompting

### Zheng,XinbingLiang,YayingFei,YuhengCheng,

withchain-of-thoughtforlargelanguagemodels. In

### Zongze Xu, and Chenglin Wu. 2024a. Data inter-

Proceedingsofthe62ndAnnualMeetingoftheAspreter: An LLM agent for data science. CoRR,
sociationforComputationalLinguistics(Volume1:
abs/2402.18679.
LongPapers),pages1330–1350,Bangkok,Thailand.
AssociationforComputationalLinguistics.
SiruiHong,MingchenZhuge,JonathanChen,Xiawu

### Zheng,YuhengCheng,JinlinWang,CeyaoZhang,

AbhimanyuDubey,AbhinavJauhri,AbhinavPandey,
ZiliWang,StevenKaShingYau,ZijuanLin,Liyang

### AbhishekKadian,AhmadAl-Dahle,AieshaLetman,

Zhou, Chenyu Ran, Lingfeng Xiao, Chenglin Wu,

### Akhil Mathur, Alan Schelten, Amy Yang, Angela

andJu¨rgenSchmidhuber.2024b. Metagpt: Metapro-

### Fan,etal.2024. Thellama3herdofmodels. arXiv

grammingforAmulti-agentcollaborativeframework.
preprintarXiv:2407.21783.
InICLR.OpenReview.net.

### Mikhail Galkin, Xinyu Yuan, Hesham Mostafa, Jian

Tang,andZhaochengZhu. Towardsfoundationmod- Edward J Hu, Yelong Shen, Phillip Wallis, Zeyuan
elsforknowledgegraphreasoning. InTheTwelfth Allen-Zhu,YuanzhiLi,SheanWang,LuChen,Alex
International Conference on Learning Representa- Smola,andRobertKorbak.2021. Lora: Low-rank
tions. adaptationoflargelanguagemodels. arXivpreprint
arXiv:2106.09685.

### DayaGuo,DejianYang,HaoweiZhang,JunxiaoSong,

RuoyuZhang,RunxinXu,QihaoZhu,ShirongMa, OlgaKononova,TanjinHe,HaoyanHuo,AmalieTre-
PeiyiWang,XiaoBi,etal.2025. Deepseek-r1: In- wartha,ElsaAOlivetti,andGerbrandCeder.2021.
centivizingreasoningcapabilityinllmsviareinforce- Opportunitiesandchallengesoftextmininginmatementlearning. arXivpreprintarXiv:2501.12948. rialsresearch. Iscience,24(3).

<!-- Page 11 -->

BespokeLabs.2025. Bespoke-stratos: Theunreason- RuiPan,ShuoXing,ShizheDiao,WenheSun,Xiang
ableeffectivenessofreasoningdistillation. Accessed: Liu, KaShun Shum, Jipeng Zhang, Renjie Pi, and
2025-01-22. TongZhang.2024b. Plum: Promptlearningusing
metaheuristics. In Findings of the Association for
AitorLewkowycz,AndersAndreassen,DavidDohan, ComputationalLinguistics: ACL2024,pages2177–
EthanDyer,HenrykMichalewski,VinayRamasesh, 2197,Bangkok,Thailand.AssociationforComputa-
Ambrose Slone, Cem Anil, Imanol Schlag, Theo tionalLinguistics.
Gutman-Solo,etal.2022. Solvingquantitativereasoningproblemswithlanguagemodels. Advances Shirui Pan, Linhao Luo, Yufei Wang, Chen Chen, JiinNeuralInformationProcessingSystems,35:3843– apuWang,andXindongWu.2024c. Unifyinglarge
3857. languagemodelsandknowledgegraphs: Aroadmap.

### IEEE Transactions on Knowledge and Data Engi-

Boyan Li, Yuyu Luo, Chengliang Chai, Guoliang Li,
neering.
and Nan Tang. 2024. The dawn of natural language to sql: Are we fully ready? arXiv preprint
DavidRein,BettyLiHou,AsaCooperStickland,JackarXiv:2406.01265.
sonPetty,RichardYuanzhePang,JulienDirani,JulianMichael,andSamuelRBowman.2023. Gpqa:A

### AmanMadaan, NiketTandon,PrakharGupta,Skyler

graduate-levelgoogle-proofq&abenchmark. arXiv
Hallinan, Luyu Gao, Sarah Wiegreffe, Uri Alon,
preprintarXiv:2311.12022.

### Nouha Dziri, Shrimai Prabhumoye, Yiming Yang,

etal.2023. Self-refine:Iterativerefinementwithself-
Tal Ridnik, Dedy Kredo, and Itamar Friedman.
feedback. InThirty-seventhConferenceonNeural

## Code generation with alphacodium: From

InformationProcessingSystems.
prompt engineering to flow engineering. CoRR,
abs/2401.08500.
Santiago Miret and Nandan M Krishnan. 2024. Are
llmsreadyforreal-worldmaterialsdiscovery? arXiv
JayantSathaye,OswaldoLucon,AtiqRahman,JohnM
preprintarXiv:2402.05200.

### Christensen,FatimaDenton,JunichiFujino,Garvin

Vaibhav Mishra, Somaditya Singh, Dhruv Ahlawat, Heath, Monirul Mirza, Hugh Rudnick, August
MohdZaki,VaibhavBihani,HargunSinghGrover, Schlaepfer, et al. 2011. Renewable energy in the
BiswajitMishra,SantiagoMiret,NMKrishnan,etal. context of sustainable development. In IPCC spe-

## Foundationallargelanguagemodelsformate- cialreportonrenewableenergysourcesandclimate

rialsresearch. arXivpreprintarXiv:2412.09560. changemitigation.CambridgeUniversityPress.
DavidMrdjenovich,MatthewKHorton,JosephHMon- MaraSchilling-Wilhelmi,Martin˜oR´ıos-Garc´ıa,Shertoya,ChristianMLegaspi,ShyamDwaraknath,Vahe jeel Shabih, Mar´ıa Victoria Gil, Santiago Miret,
Tshitoyan, Anubhav Jain, and Kristin A Persson. ChristophTKoch,Jose´AMa´rquez,andKevinMaik

## Propnet: a knowledge graph for materials Jablonka.2025. Fromtexttoinsight: largelanguage

science. Matter,2(2):464–480. modelsforchemicaldataextraction. ChemicalSocietyReviews.
Niklas Muennighoff, Zitong Yang, Weijia Shi, XiangLisaLi,LiFei-Fei,HannanehHajishirzi,Luke MartinSeifrid,RobertPollice,AndresAguilar-Granda,
Zettlemoyer, PercyLiang, EmmanuelCande`s, and Zamyla Morgan Chan, Kazuhiro Hotta, Cher Tian
Tatsunori Hashimoto. 2025. s1: Simple test-time Ser, JenyaVestfrid, TonyCWu, andAlanAspuruscaling. arXivpreprintarXiv:2501.19393. Guzik. 2022. Autonomous chemical experiments:
Challenges and perspectives on establishing a self-
National Renewable Energy Laboratory. 2025. Best
driving lab. Accounts of Chemical Research,
research-cellefficiencychart. Photovoltaicresearch,
55(17):2454–2466.
NationalRenewableEnergyLaboratory(NREL).
Karan Singhal, Shekoofeh Azizi, Tao Tu, S. Sara
HarshaNori,YinTatLee,ShengZhang,DeanCarignan,

### Mahdavi, Jason Wei, Hyung Won Chung, Nathan

RichardEdgar,Nicolo` Fusi,NicholasKing,Jonathan

### Scales,AjayTanwani,HeatherCole-Lewis,Stephen

Larson, Yuanzhi Li, Weishung Liu, Renqian Luo,

### Pfohl,PerryPayne,MartinSeneviratne,PaulGam-

ScottMayerMcKinney,RobertOsazuwaNess,Hoible,ChrisKelly,AbubakrBabiker,NathanaelScha¨rli,
fungPoon,TaoQin,NaotoUsuyama,ChrisWhite,

### Aakanksha Chowdhery, Philip Mansfield, Dina

andEricHorvitz.2023. Cangeneralistfoundation
Demner-Fushman,BlaiseAgu¨erayArcas,DaleWebmodels outcompete special-purpose tuning? case
ster,GregS.Corrado,YossiMatias,KatherineChou,
studyinmedicine. CoRR,abs/2311.16452.

### JurajGottweis,NenadTomasev,YunLiu,AlvinRa-

OpenAI.2024. Learningtoreasonwithllms. jkomar, Joelle Barral, Christopher Semturs, Alan

### Karthikesalingam,andVivekNatarajan.2023. Large

Rui Pan, Xiang Liu, Shizhe Diao, Renjie Pi, Jipeng languagemodelsencodeclinicalknowledge. Nature,
Zhang,ChiHan,andTongZhang.2024a. Lisa: Lay- 620(7972):172–180.
erwise importance sampling for memory-efficient
large language model fine-tuning. Advances in Henry J Snaith. 2018. Present status and future
NeuralInformationProcessingSystems,37:57018– prospects of perovskite photovoltaics. Nature ma-
57049. terials,17(5):372–376.

<!-- Page 12 -->

YaoxianSong,PengleiSun,HaoyuLiu,ZhixuLi,Wei NovaSkyTeam.2025. Sky-t1: Fullyopen-sourcerea-
Song, Yanghua Xiao, and Xiaofang Zhou. 2024. soningmodelwitho1-previewperformancein$450
Scene-drivenmultimodalknowledgegraphconstruc- budget. Accessed: 2025-01-09.
tionforembodiedai. IEEETransactionsonKnowledgeandDataEngineering. Amalie Trewartha, Nicholas Walker, Haoyan Huo,

### SanghoonLee,KevinCruse,JohnDagdelen,Alexan-

YuSong,SantiagoMiret,andBangLiu.2023a. Matsci- derDunn,KristinA.Persson,GerbrandCeder,and
nlp: Evaluating scientific language models on ma- AnubhavJain.2022. Quantifyingtheadvantageof
terialssciencelanguagetasksusingtext-to-schema domain-specificpre-trainingonnamedentityrecogmodeling. arXivpreprintarXiv:2305.08264. nitiontasksinmaterialsscience. Patterns.
YuSong,SantiagoMiret,HuanZhang,andBangLiu. VaheTshitoyan,JohnDagdelen,LeighWeston,Alexan-
2023b. Honeybee: Progressiveinstructionfinetuning der Dunn, Ziqin Rong, Olga Kononova, Kristin A.
oflargelanguagemodelsformaterialsscience. arXiv Persson,GerbrandCeder,andAnubhavJain.2019.
preprintarXiv:2310.08511. Unsupervisedwordembeddingscapturelatentknowledgefrommaterialsscienceliterature. Nature.

### MichaelJStatt,BrianARohr,DanGuevarra,SantoshK

Suram, John M Gregoire, et al. 2023. The materi- VineethVenugopalandElsaOlivetti.2024. Matkg: An
alsexperimentknowledgegraph. DigitalDiscovery, autonomouslygeneratedknowledgegraphinmaterial
2(4):909–914. science. ScientificData,11(1):217.
Jiamin Su, Yibo Yan, Zhuoran Gao, Han Zhang, Nicholas Walker, Amalie Trewartha, Haoyan Huo,
Xiang Liu, and Xuming Hu. 2025. Cafes: A SanghoonLee,KevinCruse,JohnDagdelen,Alexancollaborative multi-agent framework for multi- der Dunn, Kristin Persson, Gerbrand Ceder, and
granularmultimodalessayscoring. arXivpreprint AnubhavJain.2021. Theimpactofdomain-specific
arXiv:2505.13965. pre-trainingonnamedentityrecognitiontasksinmaterialsscience. AvailableatSSRN3950755.

### LiangtaiSun,YangHan,ZihanZhao,DaMa,Zhennan

Shen,BaocaiChen,LuChen,andKaiYu.2023. Sci- YuweiWan,YixuanLiu,AswathyAjith,ClaraGrazian,
eval: Amulti-levellargelanguagemodelevaluation BramHoex,WenjieZhang,ChunyuKit,TongXie,
benchmark for scientific research. arXiv preprint andIanFoster.2024. Sciqag: AframeworkforautoarXiv:2308.13149. generated science question answering dataset with
fine-grainedevaluation. Preprint,arXiv:2405.09939.
MatthewCSwainandJacquelineMCole.2016. Chemdataextractor: a toolkit for automated extraction Guanzhi Wang, Yuqi Xie, Yunfan Jiang, Ajay Manof chemical information from the scientific litera- dlekar, Chaowei Xiao, Yuke Zhu, Linxi Fan, and
ture. Journalofchemicalinformationandmodeling, AnimaAnandkumar.2023. Voyager: Anopen-ended
56(10):1894–1904. embodiedagentwithlargelanguagemodels. arXiv
preprintarXiv:2305.16291.

### Kimi Team, Angang Du, Bofei Gao, Bowei Xing,

Changjiu Jiang, Cheng Chen, Cheng Li, Chenjun XuezhiWang,JasonWei,DaleSchuurmans,QuocVLe,
Xiao, Chenzhuang Du, Chonghua Liao, Chuning EdHChi, SharanNarang, AakankshaChowdhery,
Tang,CongcongWang,DehaoZhang,EnmingYuan, andDennyZhou.2022. Self-consistencyimproves
Enzhe Lu, Fengxiang Tang, Flood Sung, Guangda chainofthoughtreasoninginlanguagemodels. In
Wei, Guokun Lai, Haiqing Guo, Han Zhu, Hao TheEleventhInternationalConferenceonLearning
Ding,HaoHu,HaoYang,HaoZhang,HaotianYao, Representations.
Haotian Zhao, Haoyu Lu, Haoze Li, Haozhen Yu,

### ZhenhailongWang,ShaoguangMao,WenshanWu,Tao


### Hongcheng Gao, Huabin Zheng, Huan Yuan, Jia

Ge, Furu Wei, and Heng Ji. 2024. Unleashing the
Chen, Jianhang Guo, Jianlin Su, Jianzhou Wang,
emergentcognitivesynergyinlargelanguagemod-
JieZhao,JinZhang,JingyuanLiu,JunjieYan,Junels: Atask-solvingagentthroughmulti-personaselfyanWu, LidongShi, LingYe, LonghuiYu, Mengcollaboration. InProceedingsofthe2024Conference
nan Dong, Neo Zhang, Ningchen Ma, Qiwei Pan,
oftheNorthAmericanChapteroftheAssociationfor

### Qucheng Gong, Shaowei Liu, Shengling Ma, Shu-

ComputationalLinguistics: HumanLanguageTechpeng Wei, Sihan Cao, Siying Huang, Tao Jiang,
nologies(Volume1: LongPapers),pages257–279.
Weihao Gao, Weimin Xiong, Weiran He, Weixiao
Huang, Wenhao Wu, Wenyang He, Xianghui Wei,

### JasonWei,XuezhiWang,DaleSchuurmans,Maarten

Xianqing Jia, Xingzhe Wu, Xinran Xu, Xinxing

### Bosma,FeiXia,EdChi,QuocVLe,DennyZhou,


### Zu, XinyuZhou, XuehaiPan, Y.Charles, YangLi,

etal.2022. Chain-of-thoughtpromptingelicitsrea-
Yangyang Hu, Yangyang Liu, Yanru Chen, Yejie soninginlargelanguagemodels. AdvancesinNeural
Wang,YiboLiu,YidaoQin,YifengLiu,YingYang, InformationProcessingSystems,35:24824–24837.

### YipingBao,YulunDu,YuxinWu,YuzhiWang,Zaida

Zhou,ZhaojiWang,ZhaoweiLi,ZhenZhu,Zheng TianhaoWu, ZhenzhenQin, YanboWang, Yongzhen
Zhang,ZhexuWang,ZhilinYang,ZhiqiHuang,Zi- Wu, Wei Chen, Shufang Zhang, Molang Cai,
hao Huang, Ziyao Xu, and Zonghan Yang. 2025. SongyuanDai,JingZhang,JianLiu,etal.2021. The
Kimik1.5: Scalingreinforcementlearningwithllms. mainprogressofperovskitesolarcellsin2020–2021.
Preprint,arXiv:2501.12599. Nano-MicroLetters,13:1–18.

<!-- Page 13 -->

Yupeng Xie, Yuyu Luo, Guoliang Li, and Nan Tang. LiZhong,ZilongWang,andJingboShang.2024a. De-

## Haichart: HumanandAIpairedvisualization buglikeahuman: Alargelanguagemodeldebugger

system. Proc.VLDBEndow.,17(11):3178–3191. viaverifyingruntimeexecutionstepbystep. InACL
(Findings),pages851–870.AssociationforCompu-
Haotian Xu, Xing Wu, Weinong Wang, Zhongzhi Li, tationalLinguistics.

### Da Zheng, Boyuan Chen, Yi Hu, Shijia Kang, Ji-

Qihuang Zhong, Kang Wang, Ziyang Xu, Juhua Liu,
amingJi,YingyingZhang,ZhijiangGuo,Yaodong
Liang Ding, Bo Du, and Dacheng Tao. 2024b.
Yang,MuhanZhang,andDebingZhang.2025. Red-

### Achieving¿97%ongsm8k: Deeplyunderstanding

star: Doesscalinglong-cotdataunlockbetterslowreasoningsystems? Preprint,arXiv:2501.11284. the problems makes llms perfect reasoners. arXiv
preprintarXiv:2404.14963.
Yiheng Xu, SU Hongjin, Chen Xing, Boyu Mi, Qian
Andy Zhou, Kai Yan, Michal Shlapentokh-Rothman,
Liu,WeijiaShi,BinyuanHui,FanZhou,YitaoLiu,

### HaohanWang,andYu-XiongWang.2024. Language

TianbaoXie,etal.2024. Lemur: Harmonizingnatagenttreesearchunifiesreasoning,acting,andplanurallanguageandcodeforlanguageagents. InThe
ninginlanguagemodels. InForty-firstInternational
TwelfthInternationalConferenceonLearningRepre-
ConferenceonMachineLearning.
sentations.

### Chunting Zhou, Pengfei Liu, Puxin Xu, Srini Iyer,

AnYang,BaosongYang,BeichenZhang,BinyuanHui, Jiao Sun, Yuning Mao, Xuezhe Ma, Avia Efrat,
BoZheng,BowenYu,ChengyuanLi,DayihengLiu, PingYu,LiliYu,SusanZhang,GargiGhosh,Mike
Fei Huang, Haoran Wei, et al. 2024a. Qwen2. 5 Lewis, Luke Zettlemoyer, and Omer Levy. 2023a.
technicalreport. arXivpreprintarXiv:2412.15115. Lima: Less is more for alignment. Preprint,
arXiv:2305.11206.

### ChuangYang,WenjingHu,JialeLiu,ChuanzhouHan,

Qiaojiao Gao, Anyi Mei, Yinhua Zhou, Fengwan Xuanhe Zhou, Guoliang Li, and Zhiyuan Liu. 2023b.
Guo,andHongweiHan.2024b. Achievements,chal- Llmasdba. arXivpreprintarXiv:2308.05481.
lenges,andfutureprospectsforindustrializationof

### XiangruZhu,ZhixuLi,XiaodanWang,XueyaoJiang,

perovskitesolarcells. Light:Science&Applications,
Penglei Sun, Xuwu Wang, Yanghua Xiao, and
13(1):227.

### NicholasJingYuan.2022. Multi-modalknowledge

graphconstructionandapplication: Asurvey. IEEE
YilinYe,JianingHao,YihanHou,ZhanWang,Shishi
TransactionsonKnowledgeandDataEngineering,
Xiao,YuyuLuo,andWeiZeng.2024. GenerativeAI
36(2):715–735.
forvisualization:Stateoftheartandfuturedirections.
Vis.Informatics,8(1):43–66.
MingchenZhuge,HaozheLiu,FrancescoFaccio,DylanRAshley,Ro´bertCsorda´s,AnandGopalakrish-
YixinYe,ZhenHuang,YangXiao,EthanChern,Shijie
nan,AbdullahHamdi,HasanAbedAlKaderHam-

### Xia,andPengfeiLiu.2025. Limo: Lessismorefor

moud, Vincent Herrmann, Kazuki Irie, et al. 2023.
reasoning. arXivpreprintarXiv:2502.03387.
Mindstorms in natural language-based societies of
mind. arXivpreprintarXiv:2305.17066.

### HuanZhang,YuSong,ZiyuHou,SantiagoMiret,and


### Bang Liu. 2024a. HoneyComb: A flexible LLM-

based agent system for materials science. In FindingsoftheAssociationforComputationalLinguistics:
EMNLP 2024, pages 3369–3382, Miami, Florida,
USA.AssociationforComputationalLinguistics.

### HuanZhang,YuSong,ZiyuHou,SantiagoMiret,and


### BangLiu.2024b. Honeycomb: Aflexiblellm-based

agentsystemformaterialsscience. InFindingsofthe
AssociationforComputationalLinguistics: EMNLP
2024,pages3369–3382.
JiayiZhang,ChuangZhao,YihanZhao,ZhaoyangYu,

### MingHe,andJianpingFan.2024c. Mobileexperts:

Adynamictool-enabledagentteaminmobiledevices.
CoRR,abs/2407.03913.

### LianminZheng,Wei-LinChiang,YingSheng,Siyuan


### Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin,

Zhuohan Li, Dacheng Li, Eric Xing, et al. 2023.
Judging llm-as-a-judge with mt-bench and chatbot
arena. AdvancesinNeuralInformationProcessing
Systems,36:46595–46623.

<!-- Page 14 -->

A SchemainPerovskite-KG ForLLMusinginPerovskite-KGandPerovskite-

### Chat,wemainlyusingGPT-4oandGPT-4o-Mini

Table6presentsacomprehensiveschemaforthe
forextractionandverification.
Perovskite-KG, organized into three main ontological categories: Fabrication, Parameters, and C InstructionTuningDataset
Performance. The Fabrication ontology encom-

### C.1 DatasetStatistics

passesprocess-relatedattributessuchascoatingparameters,methods,andannealingconditions. The Theresearchquestionsinperovskitesolarcellstud-
Parametersontologycoversstructuralandcompo- iesaresystematicallycategorizedinTables1and
sitional aspects including solvents, device archi- 11. Table1providesahigh-leveloverviewofseven
tecture,andadditives. ThePerformanceontology majorresearchcategories,includingDeviceStruccapturesvariousstabilitymetricsandefficiencypa- ture and Fabrication, Performance Enhancement
rameterslikethermalstability,lightstability,and Strategies,PerformanceMetricsImprovement,Stapowerconversionefficiency. Eachcategoryisfur- bility Improvements, Defect and Recombination
ther detailed with specific data types and exam- Management, Interface and Extraction Layer Enples to ensure precise knowledge representation. hancements,andMaterialsUsedinPerovskiteSo-
Thisstructuredschemaenablessystematicorgani- lar Cells. Each category is accompanied by a dezation and retrieval of perovskite solar cell infor- tailedrationaleexplainingitsscopeandrelevance.
mationwhilemaintainingdataconsistencyacross Table11furtherexpandsthisclassificationbypretheknowledgegraph. senting 21 specific research questions (Q1-Q21)
organizedwithinthesesevencategories. Theques-
B Prompts tionscoverawiderangeoftechnicalaspects,from
devicearchitectureoptimizationandperformance

### Thesystememploysfourspecializedagents,each

enhancementstrategiestomaterialcharacteristics
with carefully designed prompts to perform speand stability improvements. Each research quescific tasks in the perovskite solar cell knowledge
tionispairedwithitscorrespondingtechnicalfoprocessingpipeline:
cus,providingacomprehensiveframeworkforun-

## Information Extraction Agent (Table 7): derstandingthekeyareasofinvestigationinhigh-

Processes research papers using a structured set performanceperovskitesolarcellresearch.
of 20 predefined questions across seven key cat-
Table12showsthedistributionofresearchcategories, including device structure, performance
egoriesinperovskitesolarcells. DeviceStructure
enhancement,stability,andmaterials. TheagentreandFabricationdominatesthefield,accountingfor
turnsanswersinastandardizedJSONformat,mark-
24,198entries(43.8%oftotal). PerformanceEningunavailableinformationas”Notmentioned”to
hancementStrategiesrepresentsthesecondlargest
maintaindataquality.
category with 11,233 entries (20.3%), followed

## Verification Agent (Table 8): Validates ex- by Defect and Recombination Management with

tracted information by comparing it with source 7,209entries(13.0%). StabilityImprovements,a
texts, focusing on maintaining accuracy of tech- crucialaspectofperovskitesolarcelldevelopment,
nical details like numerical values and material comprises5,399entries(9.8%),whilePerformance
names. Theagentprovidesbothcorrectedcontent Metrics Improvement accounts for 4,527 entries
andjustificationforanymodificationsmade. (8.2%). MaterialsUsedinPerovskiteSolarCells

## OrganizationAgent(Table9): Synthesizes andInterfaceandExtractionLayerEnhancements

verifiedinformationfrommultiplesourcesintoco- representsmallerbutsignificantportionsofthereherent,topic-focusedresponses. Thisagentensures search focus, with 1,586 (2.9%) and 952 (1.7%)
thatcomplextechnicalinformationispresentedin entriesrespectively.
alogicalandaccessiblemanner. Figure5showsthelengthdistributionpatterns

## LLM-Judge(Table10): Evaluatesresponse acrosscategoriesinourperovskiteinstructiontunqualityacrossfourkeycriteria: accuracy,complete- ingdataset. Allcategoriesdisplaysimilarcharacterness, relevance, and clarity. Using a 1-5 scoring istics,withsequencelengthspredominantlyrangsystem, this agent provides detailed assessments ingfrom100to500tokensandamedianlengthof

andexplanationsforeachcriterion,alongwithan 400tokens. Thisanalysisinformsourmodeldesign
overallevaluationsummary. decisions,particularlyregardingsequencelength

<!-- Page 15 -->

Ontology Sub-Category DataType Description Example
Coating Thespecificsofthecoatingmethodused

### Float 5000rpm,100µl

Parameter inthematerialdepositionprocess.

### Fabrication

Differentfabricationtechniques,

### Method String spincoating

involvingvariationsinmaterialdeposition.
Annealing Referstotheheatingconditionsappliedtotheperovskite,

### Float 120°C,10min

Parameter whichareessentialforcrystallizationandstability.
theliquidmediumusedtodissolveprecursors,
Solvent String Dimethylformamide(DMF)
helpingtoformauniformperovskitelayer

### Parameters

Device Patterned Thearchitectureofthedevice ITO/SAM/perovskite
Structure String (e.g.,layerorder,materialinterfaces) /C60/BCP/Cu
Additive String Anyadditionalmaterialsorchemicals potassiumions
>98%ofinitialefficiencyof>24%

### Thermal Thematerial’sabilityto


### String after1,500hoursofcontinuous

Stability withstandheatwithoutdegrading
maximumpowerpointtracking
>92%ofinitialperformancefor1,200hours
Performance Light Howresistantthematerialis

### String underthedamp-heattest

Stability toprolongedexposuretolight.
(85°Cand85%relativehumidity)
InitialPCEofcontrol,target-1andtarget-2

### Moisture Thematerial’sresilienceagainst

String devicesis21.73%,24.42%and24.11%,respectively.
Stability humidityorwaterexposure.
Degradedto78%ofinitialPCEafter1,500hoursat55±5°C

### FillFactor

Float Ameasureofthedevice’smaximumpoweroutput. 0.88

### Value

Open-Circuit Themaximumvoltagethedevicecan

### Float 1.2V

VoltageValue produceunderopen-circuitconditions.
Short-Circuit Float Thecurrentdensitywhenthecircuitisclosed. 25mA/cm2

### CurrentValue

PowerConversion Theefficiencywithwhichthedevice

### Float 25%

EfficiencyValue convertssunlightintoelectricity.
Table6: SchemainPerovskite-KG.
limitations and tokenization strategies. The distributions are independently normalized for each
category, enabling direct pattern comparison despitevaryingsamplesizes.
Figure 6 illustrates the length distribution patternsacrossdifferentcategoriesinourperovskite
instructiontuningdataset.

### D InstructionTuning

Table13presentsthetraininghyperparametersfor
Perovskite-LLM.
E MoreCaseStudy

### F License

GPQA (Rein et al., 2023) and Minerva (Lewkowycz et al., 2022) are under
MITlicense.

<!-- Page 16 -->

3.5
3.0
2.5
2.0
1.5
1.0
0.5
0.0
10 50 100 500 1000 2000
Word Count
ytisneD
e-3 Total Length Distribution by Category (Prompt + Response)

### Device Structure

Perf. Enhancement

### Metrics


### Stability

Defect & Recom.
Interface

### Materials

Figure5:Distributionofpromptandresponselengthsacrossdifferentcategoriesinourdataset.They-axisrepresents
density(e-3),andthex-axisshowsthewordcountinlogarithmicscale.Eachcategory’sdistributionisindependently
normalized.

<!-- Page 17 -->

Table7: PromptsforInformationExtractionAgent.

### PromptsforInformationExtractionAgent:

Answerthefollowingquestionsbasedontheprovidedtext.
{
”DeviceStructureandFabrication”:[
”Q1:SummarizethedevicestructuresorconfigurationsoftheperovskitesolarcellsthosecanreachPCEover25%.”,
”Q2:HowtopreparetheperovskiteprecursorsolutionsthosecanreachPCEover25%?”,
”Q3:HowtofabricatetheperovskitesolarcellsthosecanreachPCEover25%?”
],
”PerformanceEnhancementStrategies”:[
”Q4:WhatareproblemssolvedinliteraturesthatreportperovskitesolarcellsthosecanreachPCEover25%?”,
”Q5: What are the reasons to choose the strategies that can enhance performance of the perovskite solar cells in
literaturesthatreportperovskitesolarcellsthosecanreachPCEover25%?”
],
”PerformanceMetricsImprovement”:[
”Q6:HowtoimprovetheVOCofperovskitesolarcells?”,
”Q7:HowtoimprovetheFFofperovskitesolarcells?”,
”Q8:HowtoimprovetheJscofperovskitesolarcells?”
],
”StabilityImprovements”:[
”Q9:Howtoimprovethemoisturestabilityofperovskitesolarcells?”,
”Q10:Howtoimprovethethermalstabilityofperovskitesolarcells?”,
”Q11:Howtoimprovetheilluminationorlightstabilityofperovskitesolarcells?”
],
”DefectandRecombinationManagement”:[
”Q12:Howtopassivateorreducedefects/trapsofperovskitesolarcells?”,
”Q13:Howtoreducerecombinationofperovskitesolarcells?”
],
”InterfaceandExtractionLayerEnhancements”:[
”Q14:Howtoimprovethewettabilityoftheburiedinterfaceinperovskitesolarcells?”,
”Q15:HowtoimprovetheholeextractionabilityofHTLinperovskitesolarcells?”,
”Q16:HowtoimprovetheelectronextractionabilityofETLinperovskitesolarcells?”
],
”MaterialsUsedinPerovskiteSolarCells”:[
”Q17:WhataretheHTLmaterialsusedinperovskitesolarcellsandthecommonfeaturesofthem?”,
”Q18:WhataretheETLmaterialsusedinperovskitesolarcellsandtheirfeatures?”,
”Q19:Whataretheholeblockinglayermaterialsinperovskitesolarcellsandtheirfeatures?”,
”Q20:Whatarethepassivationmaterialsusedinperovskitesolarcellsandtheircommonfeatures?”
]
}

### Belowisthetext:{paper text}

Response:ReturnaJSONobjectwiththefollowingstructure,ifthetextdoesnotcontaintheanswer,return”Notmentioned”:
{
”questions”:[
{
”question”:”Q1”,
”answer”:”AnswertoQuestion1”
},
{
”question”:”Q2”,
”answer”:”Notmentioned”
},
...
]
}

<!-- Page 18 -->

Table8: PromptsforVerificationAgent.

### PromptsforVerificationAgent:

Youneedtoverifytheaccuracyoftheextractedinformationfromaperovskitepaper. Comparetheextracteddatawith
theoriginaltexttoensureconsistencyandcorrectness.Highlightanydiscrepanciesandfixthem.Moreover,maintainthe
originalmeaningofthetextandtheoriginalinformation,suchasnumbersandmaterialnames.

### Input:

Paragraph{Section name}:{Text of the section}

### Extracted:{Extracted information}

Output:Verifiedinformationwithnotesonanydiscrepanciesorconfirmationofaccuracy.
PleasereturnaJSONobjectwiththefollowingstructureonlyreturnoneitem:
{
”verified info”:{
”fixed content”:”Thefixedparagraph”,
”reason”:”Thereasonforthefix”
}
}
Table9: PromptsforOrganizationAgent.

### PromptsforOrganizationAgent:

Yourtaskistoorganizetheverifiedinformationfromaperovskitepaperrelatedtothequestion:{question}.
Belowistheinformationsplitintoparagraphsthatanswersthequestion:
{answers}
Output:Theorganizedandcontinuousanswertothequestion.
ReturnaJSONobjectwiththefollowingstructure:
{
”answer”:”Theorganizedandcontinuousanswertothequestion.”
}

<!-- Page 19 -->

Table10: PromptsforLLM-Judge.

### PromptsforLLM-Judge:

Youareanexpertevaluator.Yourtaskistocompareamodel’sresponsetothegroundtruthanswerandprovideadetailed
evaluation.
Model’sresponse:
{model response}

### Groundtruth:

{ground truth}
Pleaseevaluatethemodel’sresponsebasedonthefollowingcriteria:

## Accuracy:Howfactuallycorrectisthemodel’sresponsecomparedtothegroundtruth?


## Completeness:Doesthemodel’sresponsecoverallthekeypointsmentionedinthegroundtruth?


## Relevance:Howwelldoesthemodel’sresponseaddresstheimpliedquestionortask?


## Clarity:Isthemodel’sresponseclearandeasytounderstand?

Foreachcriterion,provideascorefrom1to5,where1isthelowestand5isthehighest.Also,provideabriefexplanation
foreachscore.
Finally,giveanoverallscorefrom1to5andasummaryofyourevaluation.
FormatyourresponseasaJSONobjectwiththefollowingstructure:
{
”accuracy”:{”score”:0,”explanation”:””},
”completeness”:{”score”:0,”explanation”:””},
”relevance”:{”score”:0,”explanation”:””},
”clarity”:{”score”:0,”explanation”:””},
”overall”:{”score”:0,”summary”:””}
}

<!-- Page 20 -->

ID ResearchQuestion TechnicalFocus

### I.DeviceStructureandFabrication

Q1 SummarizedevicestructuresforPCE>25% Devicearchitectureoptimization
Q2 PerovskiteprecursorsolutionpreparationforPCE Solutionchemistryandprocessing
>25%
Q3 FabricationmethodsforPCE>25% Manufacturingprocesses

### II.PerformanceEnhancementStrategies

Q4 Problems solved in high-efficiency (>25%) de- Criticalchallengesandsolutions
vices
Q5 Rationaleforperformanceenhancementstrategies Strategicapproachjustification

### III.PerformanceMetricsImprovement

Q6 V improvementmethods Open-circuitvoltageoptimization

## Oc


### Q7 FFimprovementmethods Fillfactorenhancement

Q8 J improvementmethods Short-circuit current density opti-

## Sc

mization
Q9 PLQY-iV relationship Photoluminescence quantum yield

## Oc

correlation

### IV.StabilityImprovements


### Q10 Moisturestabilityenhancement Waterresistancestrategies

Q11 Thermalstabilityenhancement Temperaturetolerancemethods
Q12 Lightstabilityenhancement Photo-stabilityimprovement

### V.DefectandRecombinationManagement


### Q13 Defect/trappassivationmethods Defectcontrolstrategies

Q14 Recombinationreductionapproaches Chargerecombinationsuppression

### VI.InterfaceandExtractionLayerEnhancements

Q15 Buriedinterfacewettabilityimprovement Interfaceengineering

### Q16 HTLholeextractionenhancement Holetransportoptimization

Q17 ETLelectronextractionenhancement Electrontransportoptimization

### VII.MaterialsUsedinPerovskiteSolarCells


### Q18 HTLmaterialsandfeatures Holetransportmaterials


### Q19 ETLmaterialsandfeatures Electrontransportmaterials


### Q20 Holeblockinglayermaterials Blockinglayercharacteristics

Q21 Passivationmaterialsandfeatures Surfacepassivationmaterials
Table11: SystematicClassificationofResearchQuestionsinHigh-PerformancePerovskiteSolarCellStudies

<!-- Page 21 -->


### AbbreviatedName FullName Count

Perf. Enhancement PerformanceEnhancementStrategies 11,233

### Stability StabilityImprovements 5,399

Defect&Recom. DefectandRecombinationManagement 7,209
DeviceStructure DeviceStructureandFabrication 24,198

### Metrics PerformanceMetricsImprovement 4,527


### Materials MaterialsUsedinPerovskiteSolarCells 1,586


### Interface InterfaceandExtractionLayerEnhancements 952

Table12: Correspondencebetweenabbreviatedandfullnamesofresearchcategoriesinperovskitesolarcells
Parameter Chat-LLM Reasoning-LLM
LearningRate 1e-6 5e-6

### BatchSize 8 32


### NumberofEpochs 3 15


### Optimizer AdamW AdamW

LearningRateScheduler Cosine Cosine

### WarmupSteps 20 20

Table13: TrainingHyperparametersforPerovskite-Chat-LLMandPerovskite-Reasoning-LLM

<!-- Page 22 -->

4.0
3.0
2.0
1.0
0.0
10 50 100 500 1000 2000
Word Count
ytisneD
e-3 Prompt Length Distribution by Category

### Device Structure

Perf. Enhancement

### Metrics


### Stability

Defect & Recom.
Interface
Materials
70.0
60.0
50.0
40.0
30.0
20.0
10.0
0.0
10 50 100 500 1000 2000
Word Count
ytisneD
e-3 Response Length Distribution by Category

### Device Structure

Perf. Enhancement

### Metrics


### Stability

Defect & Recom.
Interface

### Materials

Figure6:Distributionofpromptandresponselengthsacrossdifferentcategoriesinourdataset(top:prompt,bottom:
response).

<!-- Page 23 -->


### Question:

HowtofabricatetheperovskitesolarcellsthosecanreachPCEover25%?

### Perovskite-Chat-LLM:

Tofabricateperovskitesolarcellsthatcanachieveapowerconversionefficiency(PCE)over
25%,severalkeystepsandconsiderationsareessential. First,thefabricationprocessshould
startwithacleananddrysubstrate,typicallyglassorflexiblesubstrates,whicharecleaned
thoroughlyusingacombinationofdetergentsandsolvents. Thesubstratesarethentreated
withUVozonetoenhancetheirwettingproperties.
Fortheholetransportlayer(HTL),materialslikePEDOT:PSSarecommonlyused. These
materialsarespin-coatedontothesubstrateandannealedatatemperatureof 150°Cfor15
minutes. Theperovskiteprecursorsolutionisthenprepared,typicallyusingamixedcation
andhalidecomposition,andspin-coatedontotheHTL.Thespin-coatingprocessinvolvesa
two-stepprocedure: firstat1,000rpmfor10seconds,followedby6,000rpmfor30seconds,withanisoleaddedduringthesecondsteptofacilitatecrystallization.
Afterspin-coating,theperovskitefilmsareannealedat100°Cfor10minutes. Theelectron
transportlayer(ETL)isthendeposited,oftenusingasolutionofPC61BMinchlorobenzene,
whichisspin-coatedat1,000rpmfor30secondsandannealedat100°Cfor10minutes.
Finally,ametalelectrode,typicallygold,isdepositedthroughthermalevaporation. Theentireprocessisconductedinanitrogen-filledgloveboxtominimizeexposuretomoisture.

### ChatGPT:

Tofabricateperovskitesolarcellswithapowerconversionefficiency(PCE)over25%,several
keyfactorsneedtobeconsideredandoptimizedinthefabricationprocess. Herearesome
stepsthatcanhelpinachievinghigh-efficiencyperovskitesolarcells:

## PerovskiteMaterialQuality: Thequalityoftheperovskitematerialiscrucialforachieving

highefficiency. Usehigh-qualityperovskiteprecursorsandoptimizethefabricationprocessto
ensureuniformanddefect-freeperovskitefilms.

## OptimalPerovskiteLayerThickness: Thethicknessoftheperovskitelayerplaysasignificantroleindeterminingtheefficiencyofthesolarcell. Optimizethethicknessoftheperovskitelayertomaximizelightabsorptionandchargecarriergeneration.


## TuningtheBandgap: Byengineeringthecompositionoftheperovskitematerial,youcan

tunethebandgaptomatchthesolarspectrumforbetterlightabsorptionandimprovedefficiency.

## InterfaceEngineering: Payattentiontotheinterfacesbetweendifferentlayersinthesolar

cellstructure. Optimizetheinterfacestominimizerecombinationlossesandimprovecharge
carriertransport.

## PassivationLayers: Usepassivationlayerstoreducedefectsandtrapstatesintheperovskitelayer,whichcanimprovetheoverallperformanceofthesolarcell.


## ElectronandHoleTransportLayers: Choosesuitableelectronandholetransportmaterials

tofacilitateefficientchargeextractionandtransportwithinthesolarcell.
Figure7:AfullconversationbetweenPerovskite-LLMandChatGPT,Perovskite-LLMprovidesdetailedoperational
stepswithspecificparameters,whileChatGPTonlyoffersgeneralconceptualguidance.

<!-- Page 24 -->


### Question:

WhataretheETLmaterialsusedinperovskitesolarcellsandthefeaturesofthem?

### Perovskite-Chat-LLM:

Inperovskitesolarcells,variouselectrontransportlayer(ETL)materialsareutilized,each
withdistinctfeatures. CommonETLmaterialsinclude:

## TinOxide(SnO2): SnO2isapopularchoiceforETLsduetoitshighelectronmobility,

low-temperatureprocessability,andcompatibilitywithflexiblesubstrates. Itisoftenusedin
n-i-pstructuredperovskitesolarcells.

## ZincOxide(ZnO):ZnOisanotherwidelyusedETLmaterial,knownforitshighelectron

mobilityandlow-temperatureprocessing. Itiscommonlyusedinbothn-i-pandp-i-nstructuredperovskitesolarcells.

## TungstenOxide(WO3): WO3isutilizedasaninterlayerbetweentheperovskitelayerand

theETL,enhancingchargeextractionandimprovingdevicestability. Itisparticularlyeffectiveinp-i-nstructureddevices.

## Phenyl-C61-ButyricAcidMethylEster(PCBM):PCBMisafullerenederivativeusedasan

ETLinp-i-nstructuredperovskitesolarcells. Itoffershighelectronmobilityandiscompatiblewithvariousperovskitecompositions.

## TinOxideDopedwithFluorine(F-SnO2): ThismaterialisusedtoenhancetheperformanceofSnO2ETLs,improvingtheirelectronmobilityandstability,whichleadstohigher

efficiencyinperovskitesolarcells.

## CesiumLeadHalide(CsPbX3): CsPbX3isemployedasawide-bandgapETLinallinorganicperovskitesolarcells,contributingtoimprovedstabilityandefficiency.

...

### ChatGPT:

ETL(ElectronTransportLayer)materialsplayacrucialroleinperovskitesolarcellsbyfacilitatingtheefficientextractionandtransportofelectronsgeneratedbytheperovskitelayer.

### SomecommonlyusedETLmaterialsinperovskitesolarcellsinclude:


## TiO2(TitaniumDioxide): TiO2isoneofthemostwidelyusedETLmaterialsinperovskitesolarcells. Ithasgoodelectrontransportproperties,highelectronmobility,andis

chemicallystable. TiO2canbeeasilyprocessedintothinfilms,makingitsuitableforlargescaleproductionofsolarcells.

## SnO2(TinOxide): SnO2isanotherpopularETLmaterialinperovskitesolarcells. Ithas

ahighelectronmobility,goodtransparency,andcanbedepositedatlowtemperatures. SnO2
filmscanalsobeeasilydopedtoimprovetheirconductivityandelectronextractionefficiency.
...
Figure8:AfullconversationbetweenPerovskite-LLMandChatGPT,Perovskite-LLMprovidesdetailedinformation
abouttheETLmaterialsandtheirfeatures,whileChatGPTonlyoffersgeneralinformationabouttheETLmaterials.

### Question:

Howtoimprovethethermalstabilityofperovskitesolarcells?

### Perovskite-Chat-LLM:

Improvingthethermalstabilityofperovskitesolarcellsinvolvesseveralstrategies. Oneeffectiveapproachistheuseofthermallystablematerialsforthechargetransportinglayer,such
asnickeloxide(NiO)andcopperthiocyanate(CuSCN),whichcanenhancethethermalstabilityofthedevices. Additionally,theincorporationofadditiveslike1,8-diodoctane(DIO)
and1-chloronaphthalene(CN)hasbeenshowntoimprovethemorphologyofperovskitefilms,
leadingtobetterthermalstability. Furthermore,theuseofthermallystableholetransport
materials(HTMs)andelectrontransportmaterials(ETMs)iscrucial,astheycanwithstand
hightemperatureswithoutdegradingtheperovskitelayer. ThedevelopmentofnewHTMs,
suchaspoly(3-hexylthiophene)(P3HT),hasalsocontributedtoimprovedthermalstability.
Lastly,theintroductionofinterfaciallayers,likegrapheneoxide,canenhancethethermalstabilityoftheperovskitelayerbyreducingdefectsandimprovingchargetransport.
...

### ChatGPT:

Improvingthethermalstabilityofperovskitesolarcellsiscrucialfortheirlong-termperformanceandreliability. Herearesomestrategiestoenhancetheirthermalstability:

## Encapsulation: Oneofthemosteffectivewaystoimprovethethermalstabilityofperovskitesolarcellsistoencapsulatethemwithprotectivematerials. Encapsulationhelpsto

shieldthecellsfromenvironmentalfactorssuchasmoisture,oxygen,andheat,whichcandegradetheperovskitematerial.

## ImprovedPerovskiteComposition: Researchersareconstantlyworkingondevelopingnew

perovskitecompositionsthataremorestableathightemperatures. Bytweakingthechemical
compositionoftheperovskitematerial,itispossibletoenhanceitsthermalstability.
...
Figure9:AfullconversationbetweenPerovskite-LLMandChatGPT,Perovskite-LLMprovidesdetailedinformation
about the thermal stability of perovskite solar cells, while ChatGPT only offers general information about the
thermalstabilityofperovskitesolarcells.

<!-- Page 25 -->


### Question:

CanyoutellmewhatisCuO?Andgiveme5usageinperovskite.

### Perovskite-Chat-LLM:

CuOreferstocopper(II)oxide,achemicalcompoundthatplaysasignificantroleinvarious
applications,particularlyinperovskitesolarcells(PSCs). HerearefivekeyusagesofCuOin
perovskitetechnology:

## HoleTransportMaterial: CuOactsasaneffectiveholetransportmaterial(HTM)due

toitssuitableworkfunctionandhighholemobility. Itisoftenusedinconjunctionwithother
materials,suchasNiO ,toenhancetheperformanceofPSCsbyfacilitatingefficientcharge
x
extraction[1].

## InterfaceOptimization: TheuseofCuOhelpsinoptimizingtheinterfaceswithinperovskitesolarcells. BydepositingCuOfilmsontopofperovskitelayers,itcanimprovethe

interfacialpropertiesandreducerecombinationlossesatthesecriticaljunctions[2].

## ThermalStabilityEnhancement: Copperoxide(CuO)hasbeenshowntoprovidethermalstabilitytoperovskitematerials,whichiscrucialformaintaininghighefficiencyduring

prolongedoperationunderelevatedtemperatures. Thispropertymakesitanattractivechoice
forapplicationswhereenvironmentalstabilityisaconcern[3].

## DopingandPassivation: CuOcanbeutilizedasadopantinothermaterialsusedin

PSCs,suchasSnO2,enhancingtheirelectricalpropertieslikeconductivityandmobility. Additionally,thedopingeffectscanleadtoimprovedpassivationofdefectsattheperovskitelayer,
contributingtobetterperformancemetrics[4].

## IntegrationwithOtherMaterials: Inbifacialsolarcells,CuOhasbeenintegratedwith

materialssuchascarbonnanotubes(CNTs)tocreatehigh-performancearchitecturesthat
benefitfromsynergisticeffects. Thisintegrationnotonlyenhanceschargetransportbutalso
improvestheoverallefficiencyofthedevices[5].

### References:

[1]InorganicMaterialsasHoleSelectiveContactsandIntermediateTunnelJunctionLayerfor
MonolithicPerovskite-CIGSeTandemSolarCells,Wang,Yajie;Wenisch,Robert;Schlatman
[2]CriticalReviewofCu-BasedHoleTransportMaterialsforPerovskiteSolarCells: From
TheoreticalInsightstoExperimentalValidation,Sun,Qingde;Sadhu,Anupam;Lie,Stener;

### Wong,LydiaHelena,AdvancedMaterials,2024

[3]Processing-PerformanceEvolutionofPerovskiteSolarCells: FromLargeGrainPolycrystallineFilmstoSingleCrystals,Haque,MdAzimul;Troughton,Joel;Baran,Derya,Advanced

### EnergyMaterials,2020

[4]Air-ProcessedPerovskiteSolarCellswith¿25%EfficiencyandHighStabilityEnabledby
CrystallizationModulationandHolisticPassivation,Shi,Xiaoyu;Liu,Tianxiao;Dou,Yunjie;Hu,Xiaodong;Liu,Yangyang;Wang,Feifei;Wang,Lingyuan;Ren,Zhijun;Chen,Shangshang,AdvancedMaterials,2024
[5]CriticalReviewofCu-BasedHoleTransportMaterialsforPerovskiteSolarCells: From
TheoreticalInsightstoExperimentalValidation,Sun,Qingde;Sadhu,Anupam;Lie,Stener;

### Wong,LydiaHelena,AdvancedMaterials,2024

Figure 10: A case study of Perovskite-Chat-LLM’s ability to provide detailed and accurate information with
references.

## Tables

**Table (Page 7):**

| Perovskite-Chat-LLM | 2.97 | 41.25 | 2.97 |
|---|---|---|---|
| +Perovskite-KG | 2.80 | 43.10 | 3.15 |


**Table (Page 7):**

| Perovskite-Chat-LLM | 95.50 | 62.86 | 87.22 |
|---|---|---|---|
| +Perovskite-KG | 97.32 | 65.10 | 89.21 |


**Table (Page 8):**

|  | - 30.40 13.97 800K 44.49 25.25 800K 19.19 30.51 114K 42.90 41.10 |  |  |  |
|---|---|---|---|---|
| Perovskite-R-LLM | 2K | 43.95 | 44.49 | 44.22 |


**Table (Page 16):**

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Device Str Perf. Enhan Metrics | ucture cemen | t |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Stability Defect & R Interface | ecom. |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Materials |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |


**Table (Page 22):**

| e-3 Prompt Length Distribution by Category Device Structure Perf. Enhancement Metrics 4.0 Stability Defect & Recom. Interface Materials 3.0 ytisneD 2.0 1.0 0.0 10 50 100 500 1000 2000 Word Count |
|---|
| e-3 Response Length Distribution by Category 70.0 Device Structure Perf. Enhancement Metrics 60.0 Stability Defect & Recom. 50.0 Interface Materials ytisneD 40.0 30.0 20.0 10.0 0.0 10 50 100 500 1000 2000 Word Count |


**Table (Page 22):**

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | t |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Device Stru Perf. Enhan Metrics | cture cemen | t |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Stability Defect & Re Interface | com. |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Materials |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |


**Table (Page 22):**

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | D P M | ev erf et | ice . E ric | S nh s | tr a | u nc | ct e | ure ment |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | S D | ta ef | bili ect | ty & |  | Re | c | om. |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | I M | nte at | rfa eri | ce als |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
