---
title: "Prefix Tuning Conditional Generation"
original_file: "./Prefix_Tuning_Conditional_Generation.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["prompt-engineering", "llm", "rag", "chain-of-thought", "agents"]
keywords: ["task", "prompt", "tasks", "page", "tuning", "source", "language", "proceedings", "spot", "table"]
summary: "<!-- Page 1 -->

SPoT: Better Frozen Model Adaptation through Soft Prompt Transfer
TuVu1,2(cid:70) BrianLester1 NoahConstant1 RamiAl-Rfou1 DanielCer1

### GoogleResearch1


### UniversityofMassachusettsAmherst2

{ttvu,brianlester,nconstant,rmyeid,cer}@google.com
tuvu@cs.umass.edu

### Abstract 100

Therehasbeengrowinginterestinparameter-
90
efficient methods to apply pre-trained language models to downstream tasks. BuildingonthePROMPTTUNINGapproachofLester 80
et al. (2021), which learns task-spe"
related_documents: []
---

# Prefix Tuning Conditional Generation

<!-- Page 1 -->

SPoT: Better Frozen Model Adaptation through Soft Prompt Transfer
TuVu1,2(cid:70) BrianLester1 NoahConstant1 RamiAl-Rfou1 DanielCer1

### GoogleResearch1


### UniversityofMassachusettsAmherst2

{ttvu,brianlester,nconstant,rmyeid,cer}@google.com
tuvu@cs.umass.edu

### Abstract 100

Therehasbeengrowinginterestinparameter-
90
efficient methods to apply pre-trained language models to downstream tasks. BuildingonthePROMPTTUNINGapproachofLester 80
et al. (2021), which learns task-specific soft
prompts to condition a frozen pre-trained 70
modeltoperformdifferenttasks,weproposea
novelprompt-basedtransferlearningapproach
60
called SPOT: Soft Prompt Transfer. SPOT
first learns a prompt on one or more source
50
tasks and then uses it to initialize the prompt
108 109 1010 1011
for a target task. We show that SPOT sig- Model Parameters
nificantly boosts the performance of PROMPT-

### TUNING acrossmanytasks. Moreremarkably,

across all model sizes, SPOT matches or outperformsstandardMODELTUNING(whichfinetunes all model parameters) on the SUPER-

### GLUEbenchmark,whileusingupto27,000×

fewertask-specificparameters. Tounderstand
where SPOT is most effective, we conduct a
large-scale study on task transferability with
26NLPtasksin160combinations,anddemonstrate that many tasks can benefit each other
via prompt transfer. Finally, we propose an
efficientretrievalapproachthatinterpretstask
promptsastaskembeddingstoidentifysimilar
tasksandpredictthemosttransferablesource
tasksforanoveltargettask.
1 Introduction
The past few years have seen the rapid development of ever larger pre-trained language models,
where it has repeatedly been shown that scaling
up the model size is a key ingredient for achievingthebestperformance(Devlinetal.,2019;Raffel et al., 2020; Brown et al., 2020). While this
trendhascontinuedtopushtheboundariesofpossibilityacrossvariousNLPbenchmarks,thesheer
sizeofthesemodelspresentsachallengefortheir
practicalapplication. For100B+parametermodels,fine-tuninganddeployingaseparateinstance
(cid:70)WorkdoneduringaninternshipatGoogleResearch.
erocS

### EULGrepuS

P D s (GPT-3)

## M T


## P T


### M - s M T


### SP T (Ours)


### Figure 1: Our SPOT approach—which transfers a

prompt learned from a mixture of source tasks (here,

### GLUE)ontotargettasks—outperformsvanillaPROMT-

TUNING (Lester et al., 2021) and GPT-3 (Brown et al.,
2020)on SUPERGLUE byalargemargin,matchingor
outperforming MODELTUNING across all model sizes.

### AttheXXLmodelsize,SPOTevenoutperformsMULTI-


### TASKMODELTUNING,whichfine-tunestheentiremodel

on the GLUE mixture before fine-tuning it on individualSUPERGLUEtasks.SeeAppendixAforfullresults.
ofthemodel foreachdownstreamtaskwould be
prohibitivelyexpensive. Togetaroundtheinfeasibilityoffine-tuning,Brownetal.(2020)propose

### PROMPTDESIGN, where every downstream task is

castasalanguagemodelingtaskandthefrozenpretrainedmodelperformsdifferenttasksbyconditioningonmanualtextpromptsprovidedatinference
time. Theydemonstrateimpressivefew-shotperformancewithasinglefrozenGPT-3model,although
itsperformancedependshighlyonthechoiceofthe
prompt(Zhaoetal.,2021)andstilllagsfarbehind
state-of-the-artfine-tuningresults.

### More recent work has explored methods for

learning soft prompts (Liu et al., 2021b; Qin and

### Eisner, 2021; Li and Liang, 2021; Lester et al.,

2021),whichcanbeseenasadditionallearnableparametersinjectedintothelanguagemodel. Lester
et al. (2021) propose PROMPTTUNING, a simple
2202
raM
61
]LC.sc[
2v40970.0112:viXra

<!-- Page 2 -->

Source Prompt Tuning Target Prompt Tuning Target Source Task
Task Embeddings

### Source Prompt

Initialization Library
❄ ❄ Target Task Query
🔥 🔥 Embedding Keys Values

### Source Pre-trained Target Pre-trained

Prompt Model Prompt Model Source Task A
Prompt Value Source Task B

### Target Prompts

Task A Task Target Task C

### Initialization


### Unsupervised Task


### Task B Task 🔥 tuned

Task C ❄ frozen Target

### Prompt

Figure 2: An illustration of our generic (left) and targeted (right) SPOT approaches. Left: We learn a single
genericsourcepromptononeormoresourcetasks,whichisthenusedtoinitializethepromptforeachtargettask.
Right: Welearnseparatepromptsforvarioussourcetasks,savingearlycheckpointsastaskembeddingsandbest
checkpointsassourceprompts. Theseformthekeysandvaluesofourpromptlibrary. Givenanoveltargettask,
a user: (i) computes a task embedding, (ii) retrieves an optimal source prompt, and (iii) trains a target prompt,
initializedfromthesourceprompt(see§3fordetails).
methodthatlearnsasmalltask-specificprompt(a otherviaprompttransfer. Toaddress(b),weintersequenceoftunabletokensprependedtoeachex- pretthelearnedtaskpromptsastaskembeddingsto
ample)foreachdownstreamtaskduringadaptation constructasemanticspaceoftasksandformalize
toconditionthefrozenlanguagemodeltoperform thesimilaritybetweentasks. Wedesignanefficient
the task. Strikingly, as model capacity increases, retrievalalgorithmthatmeasurestaskembedding
PROMPTTUNING becomescompetitivewith MODEL- similarity,allowingpractitionerstoidentifysource
TUNING,whichfine-tunestheentiremodeloneach tasksthatwilllikelyyieldpositivetransfer.
downstreamtask. Nevertheless,atsmallermodel To summarize, our main contributions are:
sizes(below11Bparameters),therearestilllarge (1)WeproposeSPOT,anovelprompt-basedtransgapsbetweenPROMPTTUNINGandMODELTUNING. fer learning approach, and show that scale is not

### In this paper, we propose SPOT: Soft Prompt

necessary for PROMPTTUNING to match the perfor-
Transfer,anoveltransferlearningapproachinthe
mance of MODELTUNING; on SUPERGLUE, SPOT
contextofprompttuning. SPOTfirsttrainsaprompt
matches or beats MODELTUNING across all model
sizes. (2)Weconductalarge-scaleandsystematic
ononeormoresourcetasks,andthenusestherestudy on task transferability, demonstrating consultingprompttoinitializethepromptforatarget
ditions under which tasks can benefit each other
(downstream) task. Our experiments show that
viaprompttransfer. (3)Weproposeanefficientre-
SPOTofferssignificantimprovementsoverPROMPT-
trievalmethodthatinterpretstaskpromptsastask
TUNINGacrosstasksandmodelsizes. Forinstance,
embeddingstoconstructasemanticspaceoftasks,
ontheSUPERGLUEbenchmark(Wangetal.,2019b),
andmeasurestaskembeddingsimilaritytoidentify
weobtain+10.1and+2.4pointaverageaccuracy
which tasks could benefit each other. (4) To faimprovements using the T5 BASE (220M paramecilitatefutureworkonprompt-basedlearning,we
ter) and T5 XXL (11B parameter) models (Raffel
will release our library of task prompts and preetal.,2020),respectively. Moreimportantly,SPOT
trainedmodels,andprovidepracticalrecommendaiscompetitivewithoroutperforms MODELTUNING
tionsforadaptingourlibrarytoNLPpractitioners
acrossallmodelsizes(seeFigure1).
at https://github.com/google-research/
Motivatedbytheseresults,weinvestigatetransprompt-tuning/tree/main/prompt_tuning/
ferability between tasks, through the lens of soft spot.
taskprompts. Ourgoalistoanswertwoquestions:
(a)Foragiventargettask,whendoesinitializing 2 Improving PROMPTTUNING with SPOT
thepromptfromasourcetaskboostperformance?
(b)Canweusetaskpromptstoefficientlypredict To improve performance of PROMPTTUNING on a
whichsourcetaskswilltransferwellontoanovel targettask,SPOTintroducessourceprompttuning,
targettask? Toanswer(a),weconductasystem- an intermediate training stage between language
atic study of the T5 model using 26 NLP tasks in modelpre-trainingandtargetprompttuning(Fig-
160combinationsofsourceandtargettasks. Our ure2,left),tolearnapromptononeormoresource
results indicate that many tasks can benefit each tasks (while still keeping the base model frozen),

<!-- Page 3 -->

whichisthenusedtoinitializethepromptforthe SUPERGLUE(Wangetal.,2019b)benchmarks.4 We
target task.1 Our approach retains all the compu- trainforafixednumberofstepsandreportresults
tationalbenefitsofPROMPTTUNING: foreachtarget onthevalidationsetassociatedwitheachdataset.5
task,itonlyrequiresstoringasmalltask-specific
2.1.3 Dataforsourceprompttuning
prompt,enablingthereuseofasinglefrozenpretrainedmodelacrossalltasks. Inthissection,we Aswithlanguagemodelpre-training,thechoiceof
present a generic SPOT approach where a single trainingdataiscrucialforsuccessfulprompttranstransferred prompt is reused for all target tasks. fer. To investigate the impact of source training
In§3,weexploreatargetedapproachthatretrieves data on downstream performance, we compare a
differentsourcepromptsfordifferenttargettasks. diversesetofsourcetasks.
A single unsupervised learning task: We first
2.1 Experimentalsetup
consider training the prompt on a fraction of the

### Our frozen models are built on top of the pre-

C4(ColossalCleanCrawledCorpus)dataset(Raftrained T5 checkpoints of all sizes: SMALL, BASE, fel et al., 2020) using the “prefix LM” objective

### LARGE,XL,XXLwith60M,220M,770M,3B,and

discussed in Raffel et al. (2020). Although this
11Bparameters,respectively. Inourexperiments
taskwasusedtopre-trainourfrozenT5modelsalwithSPOT,weleveragetheLMadaptedversionof
ready,itcouldstillbehelpfulforlearningageneral-

## T5

2,whichwasfoundtobeeasiertooptimizefor
purposeprompt.
PROMPTTUNING(Lesteretal.,2021).

### A single supervised learning task: Alterna-

2.1.1 Baselines tively,wecantrainthepromptusingasupervised
WecompareSPOTtothefollowingbaselines: task. WeuseeitherMNLI(Williamsetal.,2018)or

### SQUAD(Rajpurkaretal.,2016)asasinglesource

PROMPTTUNING: The vanilla prompt tuning ap- task. MNLI was shown to be helpful for many
proach of Lester et al. (2021), where an indepen- sentence-level classification tasks (Phang et al.,
dentpromptisdirectlytrainedoneachtargettask. 2019),whileSQUADwasfoundtogeneralizewell
toQAtasks(TalmorandBerant,2019).

### MODELTUNING&MULTI-TASKMODELTUNING: We

compareprompttuningapproachestoMODELTUN- Amulti-taskmixture: Sofar,wehavebeenus-
ING, the standard fine-tuning approach (Devlin ingasinglesourcetask. Analternativeapproach
et al., 2019; Raffel et al., 2020), where all model ismulti-tasktraining. Within T5’sunifiedtext-toparametersarefine-tunedoneachtargettasksep- text framework, this simply corresponds to mixarately. For an apples-to-apples comparison, we ingdifferentdatasetstogether. Weexploremixing
includeMULTI-TASKMODELTUNING,amorecompeti- datasetsfromdifferentNLPbenchmarksorfamilies
tivebaselinethatfirstfine-tunestheentiremodel oftasks,includingGLUE,SUPERGLUE,naturallanonthesamemixtureofsourcetasksusedforSPOT guageinference(NLI),paraphrasing/semanticsimibeforefine-tuningitonindividualtargettasks.3 larity,sentimentanalysis,questionanswering(QA)
on MRQA (Fisch et al., 2019), commonsense rea-
2.1.2 Evaluationdatasets soningonRAINBOW(Lourieetal.,2021),machine
translation, summarization, and natural language

### Westudydownstreamperformanceonadiverseset

of tasks from the GLUE (Wang et al., 2019c) and 4Thesedatasetsincludegrammaticalacceptabilityjudgments (COLA (Warstadt et al., 2019)), sentiment analysis
1Thetargettaskcanbetreatedasoneofthesourcetasks (SST-2(Socheretal.,2013)),paraphrasing/semanticsimilarbeingmixedtogether. ity (MRPC (Dolan and Brockett, 2005), STS-B (Cer et al.,
2 T51.1checkpointstrainedforanadditional100Ksteps 2017), QQP (Iyer et al., 2017)), natural language inference
usingthe“prefixLM”objective(Raffeletal.,2020),avail- (MNLI (Williams et al., 2018), QNLI (Wang et al., 2019c),
able at https://github.com/google-research/ RTE (Dagan et al., 2005, et seq.), CB (De Marneffe et al.,
text-to-text-transfer-transformer/blob/ 2019)),coreferenceresolution(WSC(Levesqueetal.,2012)),
main/released_checkpoints.md sentencecompletion(COPA(Roemmeleetal.,2011)),word
3Inpreliminaryexperiments,wefoundthatusingtheorig- sensedisambiguation(WIC(PilehvarandCamacho-Collados,
inalversionofT51.1(whichwaspre-trainedexclusivelyon 2019)), and question answering (MULTIRC (Khashabi et al.,
spancorruption)formodeltuningapproachesresultsinbetter 2018), RECORD (Zhang et al., 2018), BOOLQ (Clark et al.,
performancethanusingtheLMadaptedversion.Wetherefore 2019)). WeexcludetheproblematicWNLI(Levesqueetal.,
reportresultscorrespondingtotheoriginalT51.1forMODEL- 2012)datasetfromGLUE,followingDevlinetal.(2019).
TUNINGandMULTI-TASKMODELTUNING. 5Fortaskswithmultiplemetrics,weaveragethemetrics.

<!-- Page 4 -->

generationonGEM(Gehrmannetal.,2021).6 We Method GLUE SUPERGLUE
createamixtureofsourcetasksfromeachofthe

## Baseline

NLP benchmarks/families of tasks above, and a PROMPTTUNING 81.2
0.4
66.6
0.2
mixture comprising all datasets (C4 +55 labeled −longertuning 78.4 63.1
1.7 1.1
datasets),usingtheexamples-proportionalmixing

### SPOTwithdifferentsourcemixtures

strategy in Raffel et al. (2020) with an artificial GLUE(8tasks) 82.8 73.2
0.2 0.3
datasetsizelimitK = 219 examples. −longertuning 82.0 70.7
0.2 0.4

## C4 82.0 67.7

0.2 0.3
2.1.4 Trainingdetails MNLI 82.5 72.6
0.0 0.8
WecloselyfollowthetrainingprocedureinLester SQUAD 82.2 0.1 72.0 0.4
etal.(2021). Specifically,theonlynewparameters
SUPERGLUE(8tasks) 82.0
0.1
66.6
0.2
NLI(7tasks) 82.6 71.4
0.1 0.2
introduced during both source and target prompt Paraphrasing/similarity(4tasks) 82.2 69.7
0.1 0.5
tuningareasharedpromptρ ∈ RL×E prepended Sentiment(5tasks) 81.1 68.6
0.2 0.1
to each (embedded) input sequence, where L, E MRQA(6tasks) 81.8 0.2 68.4 0.2

### RAINBOW(6tasks) 80.3 64.0

arethepromptlengthandtheembeddingsize,re- 0.6 0.4
Translation(3tasks) 82.4 65.3
0.2 0.1
spectively. In all cases, we set L = 100 tokens Summarization(9tasks) 80.9 67.1
0.3 1.0
and tune the prompt for a fixed number of steps GEM(8tasks) 81.9 70.5
0.2 0.5
S.7 WhileS issetto30KinLesteretal.(2021), All(C4+55supervisedtasks) 81.8 0.2 67.9 0.9
we find that additional tuning is helpful on large
datasets. Assuch,wesetS to218 = 262,144,fol- Table 1: GLUE and SUPERGLUE results achieved by
applying T5 BASE with different prompt tuning aplowingRaffeletal.(2020),withtheexceptionof
proaches. We report the mean and standard deviation
ablationexperiments(rows“−longertuning”)in
(in the subscript) across three random seeds. SPOT

### Table 1 which use S = 30K. For source prompt

significantly improves performance and stability of
tuning, the prompt token embeddings are initial- PROMPTTUNINGacrossthetwobenchmarks.
izedfromsampledvocabulary(i.e.,the5,000most
commontokens). Duringtargetprompttuning,we
ablationstudyindicatesthatlongertuningisalsoan
save a checkpoint every 500 steps and report reimportantingredientforachievingourbestperforsultsonthecheckpointwiththehighestvalidation
mance, and is complementary to prompt transfer.
performance. AppendixCcontainstrainingdetails
Additionally, when longer tuning is omitted, we
forPROMPTTUNINGandmodeltuningapproaches.
observethatSPOTimprovesstabilityacrossruns.
2.2 EffectofSPOT

### WithinSPOT,wecancomparetheeffectiveness

ofdifferentsourcemixtures(seeTable1). Source
We compare the results of SPOT and other apprompt tuning on GLUE performs best on both
proachesinTable1andFigure1. Below,wesum-

### GLUEandSUPERGLUE,obtainingaveragescoresof

marizeandanalyzeeachofourfindingsindetail.
82.8and73.2,respectively.8 Interestingly,unsupervised source prompt tuning on C4 (the same task

### SPOT significantly improves performance and

usedtopre-trainourfrozenmodels)stillyieldsconstability of PROMPTTUNING: Our results on the
siderableimprovements,evenoutperformingusing

### GLUE and SUPERGLUE benchmarks with T5BASE

(Table 1) suggest that prompt transfer provides

### SUPERGLUEforSUPERGLUEtasks. UsingMNLIor

aneffectivemeansofimprovingperformancefor
SQUADasasinglesourcedatasetisalsoparticularly
helpfulacrosstargettasks. Othersourcemixtures

### PROMPTTUNING. Forexample,thebest-performing

canleadtosignificantgains,withsomefamiliesof
variantofSPOToutperformsthevanillaPROMPTTUN-
tasks(e.g.,NLIandparaphrasing/semanticsimilar-

### INGapproachonbothGLUEandSUPERGLUEbya

ity)showingmorebenefitthanothers. Mixingall
substantialmargin,obtaining+4.4and+10.1point
thedatasetstogetherdoesnotyieldthebestresults,
averageaccuracyimprovements,respectively. Our
possiblyduetotaskinterference/negativetransfer
6SeeAppendixBfordetailsaboutdatasets. issues,whereachievinggoodperformanceonone
7WeusetheAdafactoroptimizer(ShazeerandStern,2018)
or more source tasks can hurt performance on a
withdefaultparametersexceptwithaconstantlearningrateof
targettask.
0.3,weightdecayof1e−5,andparameterscalingturnedoff.

### Wetrainwithabatchsizeof32. Thedropoutprobabilityis

alwayskeptat0.1.Allofourmodelsareimplementedusing 8 SUPERGLUEtasksbenefitlessfromsourceprompttuning
JAX(Bradburyetal.,2018)andFLAX(Heeketal.,2020). onSUPERGLUElikelyduetothesmallsizeofthesedatasets.

<!-- Page 5 -->

SPOT helps close the gap with MODELTUNING Name Tasktype |Train|
across all model sizes: Figure 1 shows our 16sourcetasks
SUPERGLUE results across model sizes (see Ap- C4 languagemodeling 365M

## Docnli Nli 942K

pendix A for full results). As shown in Lester

### YELP-2 sentimentanalysis 560K

et al. (2021), PROMPTTUNING becomes more com- MNLI NLI 393K
petitive with scale, and at the XXL size, it nearly QQP paraphrasedetection 364K

## Qnli Nli 105K

matchestheperformanceof MODELTUNING. How-

## Record Qa 101K

ever, at smaller model sizes, there are still large CXC semanticsimilarity 88K
gaps between the two approaches. We show that

## Squad Qa 88K


## Drop Qa 77K

SPOThelpsclosethesegapsandevenexceedsMOD-

### SST-2 sentimentanalysis 67K

ELTUNING’sperformancebyalargemarginatsev- WINOGRANDE commonsensereasoning 40K
eralmodelsizes,whileretainingallthecomputa-
HELLASWAG commonsensereasoning 40K

## Multirc Qa 27K

tionalbenefitsconferredbyPROMPTTUNING. Finally, COSMOSQA commonsensereasoning 25K
at the XXL size, SPOT achieves the best average RACE QA 25K
score of 91.2, +1.1 points better than the strong 10targettasks
MULTI-TASKMODELTUNINGbaseline,despitehaving BOOLQ QA 9K
27,000× fewer task-specific parameters in both
COLA grammaticalacceptability 9K

### STS-B semanticsimilarity 6K

multi-tasksourcetuningandtargettuning. WIC wordsensedisambiguation 5K
AsafinaltestofSPOT’seffectiveness,wesubmit- CR sentimentanalysis 4K

### MRPC paraphrasedetection 4K

tedourXXLmodel’spredictionstotheSUPERGLUE

## Rte Nli 2K

leaderboard, achieving a score of 89.2. This far WSC coreferenceresolution 554
exceedsallprevioussubmissionsusingparameter- COPA QA 400

## Cb Nli 250

efficient adaptation, such as GPT-3 (71.8), and almostmatchesfullyfine-tunedT5XXL(89.3),9 de-
Table 2: Tasks used in our task transferability experispite tuning 27,000× fewer parameters. To the ments,sortedbytrainingdatasetsize.
bestofourknowledge,SPOTisthefirstparameterefficient adaptation approach that is competitive
together(§3.2). Basedonthisobservation,weprowithmethodsthattunebillionsofparameters. See
posearetrievalalgorithm(§3.3)thatleveragestask
AppendixDfordetails.
embeddingsimilaritytochoosewhichsourcetasks
touseforagivennoveltargettask(Figure2,right).
3 Predictingtasktransferability

### Ourproposedapproachcaneliminate69%ofthe

Sofar,wehaveseenthatsoftprompttransfercan sourcetasksearchspacewhilekeeping90%ofthe
significantlyboosttheperformanceofprompttun- best-casequalitygain.
ing,butitiscriticaltopicktherightsourcetasksfor
transfer. Forinstance,throughanextensivesearch, 3.1 Measuringtransferability
we found that GLUE and MNLI provide excellent We study a diverse set of 16 source datasets and
source tasks for transferring to individual GLUE 10 target datasets (see Table 2).10 We consider
andSUPERGLUEtasks. Butwhataboutaresourceall 160 possible source-target pairs, and perform
constrained scenario where a user is not able to
transferfromeachsourcetasktoeachtargettask.
exhaustivelysearchforasetofsourcetasks? Can

### Allsourcetasksaredata-richorhavebeenshown

we predict which tasks will best transfer onto a
toyieldpositivetransferinpriorwork. Tosimulate
noveltargettaskwithouttestingthemonebyone?
arealisticscenario,weuselow-resourcetasks(less
Toinvestigatethis,weconductalarge-scaleem- than10Ktrainingexamples)astargettasks.11
piricalstudywith26NLPtasks. Wefirstmeasure
transferabilityacrossalltaskcombinations(§3.1). 10Beyondthedatasetsfrom§2,weuseDOCNLI(Yinetal.,

### Next, we show that by interpreting task prompts

2021),YELP-2(Zhangetal.,2015),CXC(Parekhetal.,2021),
DROP(Duaetal.,2019),WINOGRANDE(Sakaguchietal.,2020),
as task embeddings, we can construct a seman-

### HELLASWAG (Zellers et al., 2019), COSMOSQA (Huang et al.,

tic space of tasks, wherein similar tasks cluster 2019),RACE(Laietal.,2017),andCR(HuandLiu,2004).
11The source tasks comprise one unsupervised task (C4)
9NotethattheT5submissionusestheoriginalversionof and15supervisedtaskscoveringnaturallanguageinference
T5(whichwaspre-trainedonamulti-taskmixtureofunsuper- (NLI), paraphrasing/semantic similarity, sentiment analysis,
visedandsupervisedtasks)whileweuseT51.1(whichwas questionanswering(QA),andcommonsensereasoning.The
pre-trainedonC4onlywithoutmixinginsupervisedtasks). target tasks additionally include grammatical acceptability,

<!-- Page 6 -->


## C4 +25

DocNLI +20

### Yelp-2


## Mnli +15


## Qqp +10 Qnli

ReCoRD +5
CxC
0

### SQuAD


## Drop 5


## Sst-2 10


### WinoGrande

HellaSWAG 15

### MultiRC

CosmosQA 20

## Race 25


### CoLASTS-B CR MRPC RTE BoolQ WiC WSC COPA CB

Figure3: Aheatmapofourtasktransferabilityresults.
Eachcellshowstherelativeerrorreductiononthetarget task of the transferred prompt from the associated
sourcetask(row)totheassociatedtargettask(column).

### Tolimitcomputationalcosts,weuseT5BASEin

allofourtasktransferabilityexperiments. Weperform262,144prompttuningstepsoneachsource
task. The prompt checkpoint with the highest
source task validation performance is selected to
initializepromptsfordifferenttargettasks. Since
thetargetdatasetsaresmall,weonlyperform100K
prompttuningstepsoneachtargettask. Werepeat
eachexperimentthreetimeswithdifferentrandom
seeds. Othertrainingdetailsmatch§2.1.4.
Tasks can benefit each other via prompt transfer: Figure3showsaheatmapofourresults(see

### AppendixEforfullresults). Inmanycases,prompt

transfer provides a significant gain on the target
task. The transfer MNLI → CB yields the largest
relativeerrorreductionof58.9%(fromanaverage
scoreof92.7to97.0),followedbyMNLI→COPA
(29.1%)andRECORD→WSC(20.0%). Usingthe
bestsourceprompt(outof48)foreachtargettask
dramaticallyimprovestheaveragescoreacross10
targettasksfrom74.7to80.7. Overall,ourresults
showeffectivetransferfromlargesourcetasksthat
involvehigh-levelreasoningaboutsemanticrelationshipsamongsentences(e.g., MNLI),orwhen
thesourceandtargettasksaresimilar(e.g.,CXC→
STS-B). Interestingly, positive transfer can occur
betweenrelativelydissimilartasks(e.g.,RECORD

## →Wsc,Squad→Mrpc,Cxc→Wic).12

3.2 Definingtasksimilaritythroughprompts
Since only prompt parameters are updated during prompt tuning on specific tasks, the learned
prompts likely encode task-specific knowledge.

### This suggests that they could be used to reason

wordsensedisambiguation,andcoreferenceresolution.
12Table7inAppendixEcontainsmorecases.
4C CSW DAuQS DRoCeR PORD ALoC APOC 2-pleY 2-TSS RC ILNM BC ILNcoD ETR CxC B-STS CPRM PQQ ILNQ CiW CRitluM QlooB ECAR ednarGoniW GAWSalleH AQsomsoC
1.00
0.75
0.50
0.25

## 00 C4 Wsc


### SQuAD

ReCoRD

## Drop

CoLA

## Copa

Yelp-2 SST-2

## Cr


## Mnli Cb

DocNLI

## Rte


### CxC


## Sts-B


## Mrpc


## Qqp


## Qnli


### WiC

MultiRC
BoolQ

## Race


### WinoGrande


### HellaSWAG CosmosQA

Figure 4: A clustered heatmap of cosine similarities
between the task embeddings of the 26 NLP tasks we
study. Ourprompt-basedtaskembeddingscapturetask
relationships: similartasksclustertogether.
aboutthenatureoftasksandtheirrelationships. To
testthisidea,weinterprettaskpromptsastaskembeddingsandconstructasemanticspaceoftasks.

### Moreconcretely,wedefineatask’sembeddingas

thepromptcheckpointaftertrainingfor10Ksteps
on that task.13 Note that using early checkpoints
allowsforquickcomputationoftaskembeddings
for novel target tasks. We estimate the similarity
betweentwotaskst1,t2 bymeasuringthesimilaritybetweentheircorrespondingtaskembeddings
e1,e2,usingthefollowingmetrics:

### COSINE SIMILARITY OF AVERAGE TOKENS: We

computethecosinesimilaritybetweentheaverage
pooledrepresentationsoftheprompttokens:
1 (cid:88) 1 (cid:88)
sim(t1,t2) = cos( e1, e2),
L i L j
i j
wheree1,e2 denotetherespectiveprompttokens
i j
ofe1,e2,andcosdenotesthecosinesimilarity.

### PER-TOKEN AVERAGE COSINE SIMILARITY: We

computetheaveragecosinesimilaritybetweeneveryprompttokenpair(e1,e2):
i j
1 (cid:88)(cid:88)
sim(t1,t2) = cos(e1,e2).
L2 i j
i j
13Ourpreliminaryexperimentswithothercheckpointalternatives (in the range 1K to 100K) yielded worse performance. Wealsofoundthatmeasuringtasksimilarityusing
taskembeddingsderivedfromafixedpromptcheckpoint(10K
steps) gave better results than those derived from the bestperformingpromptcheckpointpertask. Thissuggeststhat
promptstrainedforadifferingnumberofstepsmaybeless
directlycomparablethanthosetrainedforthesamelength.

<!-- Page 7 -->

Task embeddings capture task relationships: STS-B RTE
(r = 0.708, p = 1.853e-08) (r = 0.290, p = 0.046)

### Figure4showsahierarchically-clusteredheatmap

of cosine similarities between the task embeddingsusingtheCOSINESIMILARITYOFAVERAGETO-

### KENS metric.14 We observe that our learned task

embeddings capture many intuitive task relationships. Specifically, similar tasks group together
intoclusters,includingQA(SQUAD,RECORD,and

### WiC WSC


### DROP; MULTIRC and BOOLQ), sentiment analysis

(r = 0.163, p = 0.270) (r = 0.428, p = 0.002)
(YELP-2, SST-2,and CR), NLI (MNLI and CB; DOC-
NLIandRTE),semanticsimilarity(STS-BandCXC),
paraphrasing(MRPCandQQP),andcommonsense
reasoning (WINOGRANDE, HELLASWAG, and COS-

### MOSQA).WenotethatQNLI,whichisanNLItask

builtfromtheSQUADdataset,isnotcloselylinked
toSQUAD;thissuggeststhatourtaskembeddings
aremoresensitivetothetypeoftaskthandomain
similarity. Interestingly, theyalsocapturetheunintuitivecaseof RECORD’shightransferabilityto
WSC. Additionally, task embeddings that are derivedfromdifferentpromptsofthesametaskhave
highsimilarityscores(seeAppendixF).
3.3 Predictingtransferabilityviasimilarity

### We leverage our task embeddings to predict and

exploittasktransferability. Specifically,weexplore
methodstopredictthemostbeneficialsourcetasks
foragiventargettaskandthenmakeuseoftheir
promptstoimproveperformanceonthetargettask.
To enlarge our set of source prompts, we use the
prompts from each of the three different prompt
tuning runs on each source task, resulting in 48
sourceprompts. Givenatargettasktwithtaskembeddinget,werankallthesourcepromptsρs with
associatedembeddingses indescendingorderby
the similarity sim(es,et). We denote the ranked
listofsourcepromptsasρsr,wherer denotesthe
rank(r = 1,2,...,48). Weexperimentwiththree
methodsforexploitingtherankedsourceprompts:

### BEST OF TOP-k: We select the top-k source

promptsanduseeachofthemindividuallytoinitializethetargetprompt. Thisprocedurerequires
prompttuningktimesonthetargettaskt. Thebest
individual result is used for evaluating the effectivenessofthismethod.
TOP-kWEIGHTEDAVERAGE: Weinitializethetarget prompt with a weighted average of the top-k
14Toobtainthehighestresolutionofsimilaritybetweentwo
tasks,weusetheaverageofcosinesimilaritiesbetweentheir
taskembeddingsobtainedwithallthethreedifferentprompt
tuningruns(9combinations).
noitcuder
rorre
evitaler
cosine similarity

### Figure5: Correlationbetweentasksimilarityandtask

transferability. Each point represents a source prompt.
Thex-axisshowsthecosinesimilaritybetweentheassociated source and target task embeddings, averaged
overthreerunsforthetargettask(orangetitle). Theyaxismeasurestherelativeerrorreductiononthetarget
task achieved by each source prompt. We include the
Pearsoncorrelationcoefficient(r)andp-value.
source prompts (cid:80)k
r=1
α
r
ρsr so that we only performprompttuningonthetargettasktonce. The
weightsα arecomputedas:
r
sim(esr,et)
α = ,
r (cid:80)k sim(es l,et)
l=1
whereesr denotesthecorrespondingtaskembeddingofρsr.

### TOP-k MULTI-TASK MIXTURE: We first identify

the source tasks whose prompts are in the top-k
prompts and mix their datasets and the target
datasettogether,usingtheexamples-proportional
mixingstrategyofRaffeletal.(2020). Then, we
perform source prompt tuning on this multi-task
mixtureandusethefinalpromptcheckpointtoinitializethepromptfortargetprompttuning.

### We report the average score across all target

tasks achieved by each method. For comparison,
wemeasuretheabsoluteandrelativeimprovements
overBASELINE—prompttuningoneachtargettask
fromscratch(i.e.,withoutanyprompttransfer).15
Additionally, we include ORACLE—the oracle results achieved by a brute-force search to identify
15Foreachtargettaskt,wereporttheaverageandstandard
deviationofperformanceacrossthreeprompttuningruns.

<!-- Page 8 -->

thebestpossibleoutof48sourcepromptsforeach Change

### Method Avg.score

targettask. Abs. Rel.
Correlation between task similarity and task

## Baseline - - 74.7

0.7
transferability: Figure5showshowtherelative BRUTE-FORCESEARCH(k=48)

## Oracle 6.0

0.5
26.5
1.1
80.7
0.0
errorreductiononatargettaskchangesasafunctionofthesimilaritybetweenthesourceandtarget

## Cosinesimilarityofaveragetokens


### BESTOFTOP-k

task embeddings. Overall, we observe a signifi- k=1 1.5 11.7 76.2
0.5 1.1 0.1
k=3 2.7 16.6 77.4
cantpositivecorrelationbetweentaskembedding 0.6 1.1 0.3
k=6 3.8 20.0 78.5
0.1 1.1 0.5
similarity and task transferability on four (out of k=9 4.5 0.4 22.2 1.1 79.2 0.1
k=12 5.0 23.6 79.7
10)targettasks,includingSTS-B(p < 0.001),CB
k=15 5.4
0.9
24.9
2.2
80.1
0.4
0.8 1.8 0.3
(p < 0.001),WSC(p < 0.01),andRTE(p < 0.05),

## Per-Tokenaveragecosinesimilarity

whileitislesssignificantontheothertasks.16 In BESTOFTOP-k
somecases(e.g.,onBOOLQ),weobservealargerel- k
k
=
=
1
3
2
2
.
.
0
9
0.4 1
1
2
7
.
.
1
0
1.1 7
7
6
7
.
.
7
5
0.7
0.6 0.6 0.4
ativeerrorreduction(19.0%,achievedbyasource k=6 4.5 22.1 79.2
0.5 1.2 0.1
k=9 4.6 22.6 79.5
prompt of MNLI) despite a low cosine similarity 0.5 0.9 0.2
k=12 5.0 23.5 79.6
0.6 1.4 0.1
(0.4). This suggests that factors other than task k=15 5.3 24.5 80.0
0.9 2.2 0.4
similarity (data size, task difficulty, domain sim- TOP-kWEIGHTEDAVERAGE
bestk=3 1.9 11.5 76.6
ilarity, etc.) may also play a role in determining 0.5 2.7 0.1
transferability.
TOP-kMULTI-TASKMIXTURE
bestk=12 3.1 15.3 77.8
0.5 2.8 0.1

### Retrieving targeted source tasks via task em-


### Table 3: Task embeddings provide an effective means

beddings is helpful: Table 3 compares differof predicting and exploiting task transferability. Usentmethodsforidentifyingwhichsourceprompts ing BEST OF TOP-k with k = 3 improves over BASE-
could be beneficial for a given target task. Over- LINE (PROMPTTUNING on each task from scratch) by
all, our results show the effectiveness of BEST OF +2.8 points. With larger values of k (≤ 15), we can
TOP-k: simply choosing the source prompt with retain most of the benefits conferred by oracle selecthehighesttaskembeddingsimilaritytothetarget
tion. ForTOP-kWEIGHTEDAVERAGEandTOP-kMULTI-
task using PER-TOKEN AVERAGE COSINE SIMILARITY
TASKMIXTURE,weexperimentwithdifferentvaluesof
k ∈{3,6,9,12}andreportthebestresults.
improvesoverthebaselinebyalargemargin(from
anaveragescoreof74.7to76.7,a12.1%average
toexhibitremarkableperformanceonmanyNLP
relativeerrorreduction). Tryingallthetop-3(out
tasks(Devlinetal.,2019;Liuetal.,2019b;Yang
of48)sourcepromptsforeachtargettaskyieldsan
et al., 2019; Lan et al., 2020; Raffel et al., 2020;
averagescoreof77.5. Withlargervaluesofk,we
Brown et al., 2020; He et al., 2021). To improve
canretainmostofthebenefitsoforacleselection
practicalapplicabilityofthesemodels,earlywork
(80% of the gain in terms of average score with
uses compression techniques (Sanh et al., 2019;
k = 9 and 90% with k = 15), while still elimi-
Jiao et al., 2020; Fan et al., 2020; Sanh et al.,
nating over 2/3 of the candidate source prompts.
2020) to obtain lightweight models. Other work
TOP-kWEIGHTEDAVERAGE hassimilaraverageperinvolvesupdatingonlysmallpartsofthemodel(ZaformancetoBESTOFTOP-kwithk = 1,butachieves
kenetal.,2021)ortask-specificmodules,suchas
lowervariance. Thus,thismaybeanappealingaladapters(Houlsbyetal.,2019;KarimiMahabadi
ternativetoBESTOFTOP-kinscenarioswheretrying
etal.,2021)orlow-rankstructures(Mahabadietal.,
multiple prompt tuning runs on the target task is
2021; Hu et al., 2021), while keeping the rest of
prohibited. Finally,TOP-kMULTI-TASKMIXTUREalso
themodelfixed.
providesameansofobtainingstrongperformance
Recently, Brown et al. (2020) demonstrate imwithanaveragescoreof77.8,evenoutperforming
BESTOFTOP-kwithk ≤ 3.
pressivefew-shotperformancewithPROMPTDESIGN,
where their model is conditioned on a manual
4 RelatedWork text prompt at inference time to perform different tasks. Several efforts have since focused on
Parameter-efficient transfer learning: Largedevelopingprompt-basedlearningapproacheswith
scalepre-trainedlanguagemodelshavebeenshown
carefullyhandcraftedprompts(SchickandSchütze,
16SeeAppendixGforfullresults. 2021), prompt mining and paraphrasing (Jiang

<!-- Page 9 -->

etal.,2020b),gradient-basedsearchforimproved parameters, PROMPTTUNING is the most parameter
prompts(Shinetal.,2020),andautomaticprompt efficient,requiringlessthan0.01%task-specificpageneration (Gao et al., 2021). The use of hard rametersformostmodelsizes. (2)PROMPTTUNING
prompts,however,wasfoundtobesub-optimaland issimplerthanothermethods,asitdoesnotmodsensitivetothechoiceoftheprompt(Zhaoetal., ifytheinternalmodelarchitecture(cf.thePREFIX-
2021;Liuetal.,2021b). Assuch,morerecentwork TUNING method of Li and Liang (2021), which
hasshiftedtowardlearningsoftprompts(Liuetal., addsaprefixtoeachlayerofboththeTransformer
2021b;QinandEisner,2021;LiandLiang,2021; encoderanddecoder); assuch, PROMPTTUNING al-
Lester et al., 2021), which can be seen as learn- lowsmixed-taskinferenceandfacilitatestransfer
ableparametersinjectedintothemodel. Werefer learningbetweentasks. (3)AsmodelcapacityinreaderstoLiuetal.(2021a)forarecentsurveyon creases,PROMPTTUNINGbecomesmorecompetitive
prompt-basedlearningresearch. with MODELTUNING; tothebestofourknowledge,
Inconcurrentwork,Guetal.(2021)alsoexplore thishasnotbeenshownforothermethods. (4)Soft
theeffectivenessofprompttransfer. Theirmethod prompts could possibly be interpreted as natural
useshand-craftedpre-trainingtaskstailoredtospe- languageinstructions.
cific types of downstream task, and thus may be Additionally, since our prompt-based task emlessextensibletonoveldownstreamtasks. Incon- beddingapproachdoesnotcaptureallofthefactors
trast, we use existing tasks as source tasks and thatinfluencetasktransferability,weleavefurther
showthatprompttransfercanconferbenefitseven exploration of other task embedding methods to
when there are mismatches (e.g., in task type or futurework.
input/outputformat)betweenthesourceandtarget.
6 Conclusion

### Task transferability We also build on existing

work on task transferability (Wang et al., 2019a; Inthispaper,westudytransferlearninginthecon-
Liuetal.,2019a;TalmorandBerant,2019;Pruk- text of prompt tuning. We show that scale is not
sachatkunetal.,2020;Vuetal.,2020,2021). Prior necessary for PROMPTTUNING to match the perforworkshowseffectivetransferfromdata-richsource manceofMODELTUNING. OnSUPERGLUE,ourSPOT
tasks(Phangetal.,2019),thosethatrequirecom- approachmatchesorevenexceedstheperformance
plexreasoningandinference(Pruksachatkunetal., of MODELTUNING by a large margin across model
2020),orthosethataresimilartothetargettask(Vu sizes while being more parameter-efficient. Our
etal.,2020). Therehavealsobeeneffortstopredict large-scale study on task transferability indicates
tasktransferability(BingelandSøgaard,2017;Vu thattaskscanbenefiteachotherviaprompttransfer
et al., 2020; Poth et al., 2021). Vu et al. (2020) invariousscenarios. Finally,wedemonstratethat
usetaskembeddingsderivedfromeithertheinput taskpromptscanbeinterpretedastaskembeddings
text or the diagonal Fisher information matrix of toformalizethesimilaritybetweentasks. Weprothemodel,whilePothetal.(2021)exploreadapter- poseasimpleyetefficientretrievalapproachthat
basedalternatives. Here,ouruseofthesamemodel measurestasksimilaritytoidentifywhichsource
(without task-specific components) and a unified tasks could confer benefits to a novel target task.
text-to-text format allows us to better model the Takenasawhole,wehopethatourworkwillspur
space of tasks. Additionally, prompt-based task moreresearchintoprompt-basedtransferlearning.
embeddingsarecomparativelycheapertoobtain.

### Acknowledgements

5 Limitations&Futurework

### WethankMohitIyyer, SebastianRuder, Kalpesh

As other parameter-efficient adaptation methods Krishna,ThangLuong,QuocLe,andthemembers
(see§4)mayoutperformPROMPTTUNINGinspecific oftheDescartesteamandtheUMassNLPgroup
situations,itwouldbeinterestingtotestwhetheran for helpful discussion and feedback. We would
approachsimilartoSPOTcouldextendsuccessfully alsoliketothankGradySimon,LucasDixon,Slav
tothesemethods. Atthesametime,webelievethat Petrov,NaderAkoury,Haw-ShiuanChang,Kather-
PROMPTTUNING has its own merit. As pre-trained ineThai,MarzenaKarpinska,andShufanWangfor
languagemodelsbecomelargerandlarger, some theircommentsonthismanuscript. Finally,weare
advantages of PROMPTTUNING over other methods gratefultoVamsiAribandiforhisworkonpreproare: (1) Among current methods with learnable cessingseveraldatasetsusedinourexperiments.

<!-- Page 10 -->

References Tom Brown, Benjamin Mann, Nick Ryder, Melanie

### Subbiah, Jared D Kaplan, Prafulla Dhariwal,


### Chandra Bhagavatula, Ronan Le Bras, Chaitanya

Arvind Neelakantan, Pranav Shyam, Girish Sastry,

### Malaviya, Keisuke Sakaguchi, Ari Holtzman, Han-

Amanda Askell, Sandhini Agarwal, Ariel HerbertnahRashkin,DougDowney,ScottWen-tauYih,and

### Voss, Gretchen Krueger, Tom Henighan, Rewon


### Yejin Choi. 2020. Abductive commonsense reason-

Child, Aditya Ramesh, Daniel Ziegler, Jeffrey Wu,
ing. InProceedingsofthe8thInternationalConfer-
Clemens Winter, Chris Hesse, Mark Chen, Eric
enceonLearningRepresentations(ICLR2020).

### Sigler,MateuszLitwin,ScottGray,BenjaminChess,


### Jack Clark, Christopher Berner, Sam McCandlish,

Joachim Bingel and Anders Søgaard. 2017. Identify-
Alec Radford, Ilya Sutskever, and Dario Amodei.
ing beneficial task relations for multi-task learning

## Language models are few-shot learners. In

indeepneuralnetworks. InProceedingsoftheCon-
Proceedings of the 34th Conference on Neural InferenceoftheEuropeanChapteroftheAssociation
formationProcessingSystems (NeurIPS 2020), volfor Computational Linguistics (EACL 2017), pages
ume33,pages1877–1901.
164–169.
Daniel Cer, Mona Diab, Eneko Agirre, Iñigo Lopez-
YonatanBisk,RowanZellers,RonanLebras,Jianfeng
Gazpio, and Lucia Specia. 2017. SemEval-2017

### Gao, andYejinChoi.2020. Piqa: Reasoningabout

task1: Semantictextualsimilaritymultilingualand
physical commonsense in natural language. Procrosslingual focused evaluation. In Proceedings of
ceedingsoftheAAAIConferenceonArtificialIntelthe11thInternationalWorkshoponSemanticEvaluligence(AAAI2020),34(05):7432–7439.
ation(SemEval2017),pages1–14.
Ondˇrej Bojar, Christian Buck, Christian Federmann,

### Christopher Clark, Kenton Lee, Ming-Wei Chang,

Barry Haddow, Philipp Koehn, Johannes Leveling,
Tom Kwiatkowski, Michael Collins, and Kristina

### Christof Monz, Pavel Pecina, Matt Post, Herve

Toutanova. 2019. BoolQ: Exploring the surprising

### Saint-Amand,RaduSoricut,LuciaSpecia,andAleš

difficulty of natural yes/no questions. In Proceed-

### Tamchyna.2014. Findingsofthe2014workshopon

ings of the 2019 Conference of the North Ameristatisticalmachinetranslation. InProceedingsofthe
can Chapter of the Association for Computational
Ninth Workshop on Statistical Machine Translation
Linguistics: Human Language Technologies (ACL
(WMT2014),pages12–58.
2019),pages2924–2936.

### Ondˇrej Bojar, Rajen Chatterjee, Christian Federmann,

YvetteGraham,BarryHaddow,MatthiasHuck,An- Ido Dagan, Oren Glickman, and Bernardo Magnini.
tonio Jimeno Yepes, Philipp Koehn, Varvara Lo- 2005. The pascal recognising textual entailment
gacheva, Christof Monz, Matteo Negri, Aurélie challenge. In Proceedings of the 1st International

### ConferenceonMachineLearningChallenges: Eval-


### Névéol, Mariana Neves, Martin Popel, Matt Post,

uatingPredictiveUncertaintyVisualObjectClassifi-
Raphael Rubino, Carolina Scarton, Lucia Specation,andRecognizingTextualEntailment(MLCW
cia, Marco Turchi, Karin Verspoor, and Marcos
Zampieri. 2016. Findings of the 2016 conference
2005),page177–190.
onmachinetranslation. InProceedingsoftheFirst
Conference on Machine Translation (WMT 2016), Marie-Catherine De Marneffe, Mandy Simons, and
Judith Tonhauser. 2019. The CommitmentBank:
pages131–198.

### Investigating projection in naturally occurring dis-

Ondˇrej Bojar, Rajen Chatterjee, Christian Federmann, course. In Proceedings of Sinn und Bedeutung 23
Barry Haddow, Matthias Huck, Chris Hokamp, (SuB2018),volume23,pages107–124.

### Philipp Koehn, Varvara Logacheva, Christof Monz,

Matteo Negri, Matt Post, Carolina Scarton, Lucia Dorottya Demszky, Dana Movshovitz-Attias, Jeong-
Specia, and Marco Turchi. 2015. Findings of the woo Ko, Alan Cowen, Gaurav Nemade, and Sujith
2015workshoponstatisticalmachinetranslation. In Ravi.2020. GoEmotions: Adatasetoffine-grained
Proceedings of the Tenth Workshop on Statistical emotions. InProceedingsofthe58thAnnualMeet-
MachineTranslation(WMT2015),pages1–46. ingoftheAssociationforComputationalLinguistics
(ACL2020),pages4040–4054.

### Samuel R. Bowman, Gabor Angeli, Christopher Potts,

and Christopher D. Manning. 2015. A large anno- Jacob Devlin, Ming-Wei Chang, Kenton Lee, and
tatedcorpusforlearningnaturallanguageinference. Kristina Toutanova. 2019. BERT: Pre-training of
InProceedingsofthe2015ConferenceonEmpirical deep bidirectional transformers for language under-
Methods in Natural Language Processing (EMNLP standing. InProceedingsofthe2019Conferenceof
2015),pages632–642. the North American Chapter of the Association for

### ComputationalLinguistics: HumanLanguageTech-

James Bradbury, Roy Frostig, Peter Hawkins, nologies(NAACL2019),pages4171–4186.

### Matthew James Johnson, Chris Leary, Dougal

Maclaurin, George Necula, Adam Paszke, Jake WilliamB.DolanandChrisBrockett.2005. Automati-
VanderPlas, Skye Wanderman-Milne, and Qiao callyconstructingacorpusofsententialparaphrases.
Zhang. 2018. JAX: composable transformations of InProceedingsoftheThirdInternationalWorkshop
Python+NumPyprograms. onParaphrasing(IWP2005).

<!-- Page 11 -->

Dheeru Dua, Yizhong Wang, Pradeep Dasigi, Gabriel Madaan, Mounica Maddela, Khyati Mahajan,
Stanovsky, Sameer Singh, and Matt Gardner. 2019. Saad Mahamood, Bodhisattwa Prasad Majumder,
DROP:Areadingcomprehensionbenchmarkrequir- Pedro Henrique Martins, Angelina McMillaningdiscretereasoningoverparagraphs. InProceed- Major, Simon Mille, Emiel van Miltenburg, Moin
ingsoftheConferenceoftheNorthAmericanChap- Nadeem, Shashi Narayan, Vitaly Nikolaev, Andre
ter of the Association for Computational Linguis- Niyongabo Rubungo, Salomey Osei, Ankur Parikh,
tics:HumanLanguageTechnologies(NAACL2019), Laura Perez-Beltrachini, Niranjan Ramesh Rao,
pages2368–2378. Vikas Raunak, Juan Diego Rodriguez, Sashank

### Santhanam, João Sedoc, Thibault Sellam, Samira

MatthewDunn, LeventSagun, MikeHiggins, VUgur Shaikh, Anastasia Shimorina, Marco Antonio
Guney, Volkan Cirik, and Kyunghyun Cho. 2017. Sobrevilla Cabezudo, Hendrik Strobelt, Nishant
Searchqa: A new q&a dataset augmented with Subramani, Wei Xu, Diyi Yang, Akhila Yerukola,
context from a search engine. arXiv preprint and Jiawei Zhou. 2021. The GEM benchmark:
arXiv:1704.05179.
Natural language generation, its evaluation and
metrics. In Proceedings of the 1st Workshop on
OndˇrejDušek,DavidM.Howcroft,andVerenaRieser.

### Natural Language Generation, Evaluation, and


## Semanticnoisemattersforneuralnaturallan-

Metrics(GEM2021),pages96–120.
guagegeneration. InProceedingsofthe12thInternational Conference on Natural Language Genera-
Bogdan Gliwa, Iwona Mochol, Maciej Biesek, and
tion(INLG2019),pages421–426.

### Aleksander Wawer. 2019. SAMSum corpus: A

AlexanderFabbri,IreneLi,TianweiShe,SuyiLi,and human-annotated dialogue dataset for abstractive
Dragomir Radev. 2019. Multi-news: A large-scale summarization. InProceedingsofthe2ndWorkshop
multi-document summarization dataset and abstrac- onNewFrontiersinSummarization(NewSum2019),
tivehierarchicalmodel. InProceedingsofthe57th pages70–79.
Annual Meeting of the Association for ComputationalLinguistics(ACL2019),pages1074–1084. Alec Go, Richa Bhayani, and Lei Huang. 2009. Twittersentimentclassificationusingdistantsupervision.
AngelaFan,EdouardGrave,andArmandJoulin.2020. CS224NProjectReport,Stanford.
Reducing transformer depth on demand with structured dropout. In Proceedings of the 8th Inter-

### David Graff, Junbo Kong, Ke Chen, and Kazuaki

national Conference on Learning Representations
Maeda. 2003. English gigaword. Linguistic Data

## (Iclr2020).

Consortium,Philadelphia,4(1):34.
AdamFisch,AlonTalmor,RobinJia,MinjoonSeo,Eunsol Choi, and Danqi Chen. 2019. MRQA 2019 Max Grusky, Mor Naaman, and Yoav Artzi. 2018.
shared task: Evaluating generalization in reading Newsroom:Adatasetof1.3millionsummarieswith
comprehension. In Proceedings of the 2nd Work- diverse extractive strategies. In Proceedings of the
shop on Machine Reading for Question Answering 2018ConferenceoftheNorthAmericanChapterof
(MRQA2019),pages1–13. the Association for Computational Linguistics: Human Language Technologies (NAACL 2018), pages
Tianyu Gao, Adam Fisch, and Danqi Chen. 2021. 708–719.

### Makingpre-trainedlanguagemodelsbetterfew-shot

learners. In Proceedings of the 59th Annual Meet- Yuxian Gu, Xu Han, Zhiyuan Liu, and Minlie Huang.
ingoftheAssociationforComputationalLinguistics 2021. PPT: Pre-trainedprompt tuning for few-shot
andthe11thInternationalJointConferenceonNat- learning. arXivpreprintarXiv:2109.04332.
uralLanguageProcessing(ACL2021),pages3816–

## Karen Hambardzumyan, Hrant Khachatrian, and


### Jonathan May. 2021. WARP: Word-level Adver-

ClaireGardent, AnastasiaShimorina, ShashiNarayan,
sarial ReProgramming. In Proceedings of the 59th
and Laura Perez-Beltrachini. 2017. Creating train-
Annual Meeting of the Association for Computaing corpora for NLG micro-planners. In Proceedtional Linguistics and the 11th International Joint
ings of the 55th Annual Meeting of the Association

### ConferenceonNaturalLanguageProcessing(ACL-

for Computational Linguistics (ACL 2017), pages
IJCNLP2021),pages4921–4933.
179–188.
Sebastian Gehrmann, Tosin Adewumi, Karmanya Pengcheng He, Xiaodong Liu, Jianfeng Gao, and
Aggarwal, Pawan Sasanka Ammanamanchi, Weizhu Chen. 2021. Deberta: Decoding-enhanced
Anuoluwapo Aremu, Antoine Bosselut, Khy- bert with disentangled attention. In Proceedings of
athi Raghavi Chandu, Miruna-Adriana Clinciu, the9thInternationalConferenceonLearningRepre-
Dipanjan Das, Kaustubh Dhole, Wanyu Du, sentations(ICLR2021).

### Esin Durmus, Ondˇrej Dušek, Chris Chinenye

Emezue, Varun Gangal, Cristina Garbacea, Tat- Jonathan Heek, Anselm Levskaya, Avital Oliver, Marsunori Hashimoto, Yufang Hou, Yacine Jernite, vin Ritter, Bertrand Rondepierre, Andreas Steiner,
Harsh Jhamtani, Yangfeng Ji, Shailza Jolly, Mi- and Marc van Zee. 2020. Flax: A neural network
hir Kale, Dhruv Kumar, Faisal Ladhak, Aman libraryandecosystemforJAX.

<!-- Page 12 -->

KarlMoritzHermann,TomasKocisky,EdwardGrefen- Rabeeh Karimi Mahabadi, Sebastian Ruder, Mostafa
stette,LasseEspeholt,WillKay,MustafaSuleyman, Dehghani, and James Henderson. 2021. ParameterandPhilBlunsom.2015. Teachingmachinestoread efficient multi-task fine-tuning for transformers via
and comprehend. In Proceedings of the 29th Con- shared hypernetworks. In Proceedings of the 59th
ference on Neural Information Processing Systems Annual Meeting of the Association for Computa-
(NeurIPS2020),volume28. tional Linguistics and the 11th International Joint

### ConferenceonNaturalLanguageProcessing(ACL-

Neil Houlsby, Andrei Giurgiu, Stanislaw Jastrzebski, IJCNLP2021),pages565–576.

### Bruna Morrone, Quentin De Laroussilhe, Andrea

Gesmundo, Mona Attariyan, and Sylvain Gelly. Daniel Khashabi, Snigdha Chaturvedi, Michael Roth,

## Parameter-efficienttransferlearningforNLP. ShyamUpadhyay,andDanRoth.2018. Lookingbe-

InProceedingsofthe36thInternationalConference yond the surface: A challenge set for reading comon Machine Learning (PMLR 2019), volume 97, prehensionovermultiplesentences. InProceedings
pages2790–2799. ofthe2018ConferenceoftheNorthAmericanChapter of the Association for Computational Linguis-
Edward J Hu, Yelong Shen, Phillip Wallis, Zeyuan tics:HumanLanguageTechnologies(NAACL2018),
Allen-Zhu, Yuanzhi Li, Shean Wang, and Weizhu pages252–262.
Chen.2021. Lora:Low-rankadaptationoflargelanguagemodels. arXivpreprintarXiv:2106.09685. Anastassia Kornilova and Vladimir Eidelman. 2019.

### BillSum: A corpus for automatic summarization of

MinqingHuandBingLiu.2004. Miningandsumma- USlegislation. InProceedingsofthe2ndWorkshop
rizingcustomerreviews. InProceedingsofthe10th onNewFrontiersinSummarization(NewSum2019),
ACMSIGKDDInternationalConferenceonKnowl- pages48–56.
edgeDiscoveryandDataMining(KDD2004),page
168–177. Tom Kwiatkowski, Jennimaria Palomaki, Olivia Redfield, Michael Collins, Ankur Parikh, Chris Al-
LifuHuang,RonanLeBras,ChandraBhagavatula,and berti, Danielle Epstein, Illia Polosukhin, Jacob De-
Yejin Choi. 2019. Cosmos QA: Machine reading vlin, Kenton Lee, Kristina Toutanova, Llion Jones,
comprehension with contextual commonsense rea- MatthewKelcey,Ming-WeiChang,AndrewM.Dai,
soning. In Proceedings of the 2019 Conference on Jakob Uszkoreit, Quoc Le, and Slav Petrov. 2019.
EmpiricalMethodsinNaturalLanguageProcessing Natural questions: A benchmark for question anand the 9th International Joint Conference on Nat- swering research. Transactions of the Association
uralLanguageProcessing(EMNLP-IJCNLP2019), forComputationalLinguistics(TACL2019),7:452–
pages2391–2401. 466.
Shankar Iyer, Nikhil Dandekar, and Kornél Csernai. FaisalLadhak, EsinDurmus, ClaireCardie, andKath-

## FirstQuoraDatasetRelease: Questionpairs. leen McKeown. 2020. WikiLingua: A new benchmark dataset for cross-lingual abstractive summa-

Chao Jiang, Mounica Maddela, Wuwei Lan, Yang rization. In Findings of the Association for Com-
Zhong,andWeiXu.2020a. NeuralCRFmodelfor putational Linguistics (Findings of EMNLP 2020),
sentence alignment in text simplification. In Pro- pages4034–4048.
ceedings of the 58th Annual Meeting of the Association for Computational Linguistics (ACL 2020), Guokun Lai, Qizhe Xie, Hanxiao Liu, Yiming Yang,
pages7943–7960. andEduardHovy.2017. RACE:Large-scaleReAding comprehension dataset from examinations. In
ZhengbaoJiang, FrankF.Xu, JunAraki, andGraham Proceedings of the 2017 Conference on Empirical
Neubig. 2020b. How can we know what language Methods in Natural Language Processing (EMNLP
models know? Transactions of the Association 2017),pages785–794.
forComputationalLinguistics(TACL2020),8:423–

## Zhenzhong Lan, Mingda Chen, Sebastian Goodman,

Kevin Gimpel, Piyush Sharma, and Radu Soricut.
Xiaoqi Jiao, Yichun Yin, Lifeng Shang, Xin Jiang, 2020. ALBERT: A lite BERT for self-supervised
Xiao Chen, Linlin Li, Fang Wang, and Qun Liu. learning of language representations. In Proceed-

## TinyBERT: Distilling BERT for natural lan- ings of the 8th International Conference on Learnguageunderstanding. InFindingsoftheAssociation ingRepresentations(ICLR2020).

forComputationalLinguistics(FindingsofEMNLP
2020),pages4163–4174. BrianLester,RamiAl-Rfou,andNoahConstant.2021.

### The power of scale for parameter-efficient prompt

Mandar Joshi, Eunsol Choi, Daniel Weld, and Luke tuning. In Proceedings of the 2021 Conference on
Zettlemoyer. 2017. TriviaQA: A large scale dis- EmpiricalMethodsinNaturalLanguageProcessing
tantlysupervisedchallengedatasetforreadingcom- (EMNLP2021),pages3045–3059.
prehension. InProceedingsofthe55thAnnualMeetingoftheAssociationforComputationalLinguistics Hector J. Levesque, Ernest Davis, and Leora Morgen-
(ACL2017),pages1601–1611. stern. 2012. The winograd schema challenge. In

<!-- Page 13 -->

Proceedings of the Thirteenth International Confer- NorthAmericanChapteroftheAssociationforComence on Principles of Knowledge Representation putationalLinguistics: HumanLanguageTechnoloandReasoning(KR2012),page552–561. gies(NAACL2021),pages432–447.
Xiang Lisa Li and Percy Liang. 2021. Prefix-tuning: Shashi Narayan, Shay B. Cohen, and Mirella Lapata.
Optimizing continuous prompts for generation. In 2018. Don’t give me the details, just the sum-
Proceedings of the 59th Annual Meeting of the mary! topic-aware convolutional neural networks
Association for Computational Linguistics and the for extreme summarization. In Proceedings of the
11thInternationalJointConferenceonNaturalLan- 2018 Conference on Empirical Methods in Natural
guageProcessing(ACL2021),pages4582–4597. Language Processing (EMNLP 2018), pages 1797–
1807.

### BillYuchenLin, WangchunshuZhou, MingShen, Pei

Zhou,ChandraBhagavatula,YejinChoi,andXiang Yixin Nie, Adina Williams, Emily Dinan, Mohit
Ren. 2020. CommonGen: A constrained text gen- Bansal,JasonWeston,andDouweKiela.2020. Aderation challenge for generative commonsense rea- versarial NLI: A new benchmark for natural lansoning. InFindingsoftheAssociationforComputa- guageunderstanding. InProceedingsofthe58thAntionalLinguistics(FindingsofEMNLP2020),pages nual Meeting of the Association for Computational
1823–1840. Linguistics(ACL2020),pages4885–4901.
Nelson F. Liu, Matt Gardner, Yonatan Belinkov, Zarana Parekh, Jason Baldridge, Daniel Cer, Austin
MatthewE.Peters,andNoahA.Smith.2019a. Lin- Waters, and Yinfei Yang. 2021. Crisscrossed capguistic knowledge and transferability of contextual tions: Extended intramodal and intermodal semanrepresentations. InProceedingsoftheConferenceof ticsimilarityjudgmentsforMS-COCO. InProceedthe North American Chapter of the Association for ings of the 16th Conference of the European Chap-
ComputationalLinguistics: HumanLanguageTech- teroftheAssociationforComputationalLinguistics
nologies(NAACL2019),pages1073–1094. (EACL2021),pages2855–2870.
PengfeiLiu,WeizheYuan,JinlanFu,ZhengbaoJiang, Jason Phang, Thibault Févry, and Samuel R Bowman.
Hiroaki Hayashi, and Graham Neubig. 2021a. Pre- 2019. Sentence encoders on stilts: Supplementary
train, prompt, and predict: A systematic survey of training on intermediate labeled-data tasks. arXiv
prompting methods in natural language processing. preprintarXiv:1811.01088.
arXivpreprintarXiv:2107.13586.

### Mohammad Taher Pilehvar and Jose Camacho-

Xiao Liu, Yanan Zheng, Zhengxiao Du, Ming Ding, Collados. 2019. WiC: the word-in-context dataset
Yujie Qian, Zhilin Yang, and Jie Tang. 2021b. Gpt forevaluatingcontext-sensitivemeaningrepresentaunderstands,too. arXivpreprintarXiv:2103.10385. tions. InProceedingsofthe2019Conferenceofthe

### NorthAmericanChapteroftheAssociationforCom-

YinhanLiu,MyleOtt,NamanGoyal,JingfeiDu,Man- putationalLinguistics: HumanLanguageTechnolodar Joshi, Danqi Chen, Omer Levy, Mike Lewis, gies(NAACL2019),pages1267–1273.
Luke Zettlemoyer, and Veselin Stoyanov. 2019b.
Roberta: A robustly optimized bert pretraining ap- CliftonPoth,JonasPfeiffer,AndreasRücklé,andIryna
proach. arXivpreprintarXiv:1907.11692. Gurevych. 2021. What to pre-train on? Efficient
intermediate task selection. In Proceedings of the
Nicholas Lourie, Ronan Le Bras, Chandra Bhagavat- 2021 Conference on Empirical Methods in Natural
ula, and Yejin Choi. 2021. Unicorn on rainbow: LanguageProcessing(EMNLP2021),pages10585–
A universal commonsense reasoning model on a 10605.
newmultitaskbenchmark. ProceedingsoftheAAAI
Conference on Artificial Intelligence (AAAI 2021), Yada Pruksachatkun, Jason Phang, Haokun Liu,
35(15):13480–13488. Phu Mon Htut, Xiaoyi Zhang, Richard Yuanzhe
Pang, Clara Vania, Katharina Kann, and Samuel R.
Rabeeh Karimi Mahabadi, James Henderson, and Se- Bowman.2020. Intermediate-tasktransferlearning
bastian Ruder. 2021. Compacter: Efficient low- with pretrained language models: When and why
rank hypercomplex adapter layers. arXiv preprint does it work? In Proceedings of the 58th Annual
arXiv:2106.04647. Meeting of the Association for Computational Linguistics(ACL2020),pages5231–5247.

### Linyong Nan, Dragomir Radev, Rui Zhang, Amrit

Rau, Abhinand Sivaprasad, Chiachun Hsieh, Xian- Guanghui Qin and Jason Eisner. 2021. Learning how
gru Tang, Aadit Vyas, Neha Verma, Pranav Kr- toask:QueryingLMswithmixturesofsoftprompts.
ishna, Yangxiaokang Liu, Nadia Irwanto, Jessica InProceedingsofthe2021ConferenceoftheNorth
Pan, Faiaz Rahman, Ahmad Zaidi, Mutethia Mu- American Chapter of the Association for Computatuma,YasinTarabar,AnkitGupta,TaoYu,YiChern tional Linguistics: Human Language Technologies
Tan, Xi Victoria Lin, Caiming Xiong, Richard (NAACL2021),pages5203–5212.

### Socher, and Nazneen Fatema Rajani. 2021. DART:

Open-domain structured data record to text genera- ColinRaffel,NoamShazeer,AdamRoberts,Katherine
tion. In Proceedings of the 2021 Conference of the Lee, Sharan Narang, Michael Matena, Yanqi Zhou,

<!-- Page 14 -->

Wei Li, and Peter J. Liu. 2020. Exploring the lim- LanguageTechnologies(NAACL2021),pages2339–
its of transfer learning with a unified text-to-text 2352.
transformer. JournalofMachineLearningResearch
(JMLR2020),21(140):1–67. AbigailSee,PeterJ.Liu,andChristopherD.Manning.

## Gettothepoint: Summarizationwithpointer-

PranavRajpurkar,JianZhang,KonstantinLopyrev,and generatornetworks. InProceedingsofthe55thAn-
Percy Liang. 2016. SQuAD: 100,000+ questions nual Meeting of the Association for Computational
formachinecomprehensionoftext. InProceedings Linguistics(ACL2017),pages1073–1083.
oftheConferenceonEmpiricalMethodsinNatural
Language Processing (EMNLP 2016), pages 2383– Noam Shazeer and Mitchell Stern. 2018. Adafactor:

## Adaptivelearningrateswithsublinearmemorycost.

arXivpreprintarXiv:1804.04235.

### Abhinav Rastogi, Xiaoxue Zang, Srinivas Sunkara,

RaghavGupta,andPranavKhaitan.2020. Towards Taylor Shin, Yasaman Razeghi, Robert L. Logan IV,
scalable multi-domain conversational agents: The EricWallace,andSameerSingh.2020. AutoPrompt:
schema-guideddialoguedataset. Proceedingsofthe Eliciting Knowledge from Language Models with
AAAI Conference on Artificial Intelligence (AAAI Automatically Generated Prompts. In Proceed-
2020),34(05):8689–8696. ings of the 2020 Conference on Empirical Methods
in Natural Language Processing (EMNLP 2020),
Melissa Roemmele, Cosmin Adrian Bejan, and An- pages4222–4235.
drew S Gordon. 2011. Choice of plausible alternatives: Anevaluationofcommonsensecausalreason- Richard Socher, Alex Perelygin, Jean Wu, Jason
ing. InProceedingsofthe25thAAAISpringSympo- Chuang, ChristopherD.Manning, AndrewNg, and
sium: LogicalFormalizationsofCommonsenseRea- Christopher Potts. 2013. Recursive deep models
soning(AAAISpringSymposium2011). forsemanticcompositionalityoverasentimenttreebank. In Proceedings of the 2013 Conference on
AlexanderM.Rush,SumitChopra,andJasonWeston. EmpiricalMethodsinNaturalLanguageProcessing

## A neural attention model for abstractive sen- (EMNLP2013),pages1631–1642.

tence summarization. In Proceedings of the 2015
Conference on Empirical Methods in Natural Lan- AlonTalmorandJonathanBerant.2019. MultiQA:An
guageProcessing(EMNLP2015),pages379–389. empiricalinvestigationofgeneralizationandtransfer
inreadingcomprehension. InProceedingsoftheAn-
Keisuke Sakaguchi, Ronan Le Bras, Chandra Bhaga- nual Meeting of the Association for Computational
vatula, and Yejin Choi. 2020. Winogrande: An ad- Linguistics(ACL2019),pages4911–4921.
versarial winograd schema challenge at scale. ProceedingsoftheAAAIConferenceonArtificialIntel- AdamTrischler,TongWang,XingdiYuan,JustinHarligence(AAAI2020),34(05):8732–8740. ris, Alessandro Sordoni, Philip Bachman, and KaheerSuleman.2017. NewsQA:Amachinecompre-
Victor Sanh, Lysandre Debut, Julien Chaumond, and hension dataset. In Proceedings of the Workshop
ThomasWolf.2019. Distilbert,adistilledversionof on Representation Learning for NLP (RepL4NLP
bert:smaller,faster,cheaperandlighter. InProceed- 2017),pages191–200.
ings of the 5th Workshop on Energy Efficient Machine Learning and Cognitive Computing (EMC2 Tu Vu, Minh-Thang Luong, Quoc Le, Grady Simon,
2019). and Mohit Iyyer. 2021. STraTA: Self-training with
task augmentation for better few-shot learning. In
Victor Sanh, Thomas Wolf, and Alexander Rush. Proceedings of the 2021 Conference on Empirical

## Movementpruning:Adaptivesparsitybyfine- Methods in Natural Language Processing (EMNLP

tuning. In Proceedings of the 34th Conference on 2021),pages5715–5731.

### Neural Information Processing Systems (NeurIPS

2020),volume33,pages20378–20389. TuVu, TongWang, TsendsurenMunkhdalai, Alessandro Sordoni, Adam Trischler, Andrew Mattarella-
Maarten Sap, Hannah Rashkin, Derek Chen, Ronan Micke,SubhransuMaji,andMohitIyyer.2020. Ex-
Le Bras, and Yejin Choi. 2019. Social IQa: Com- ploring and predicting transferability across NLP
monsense reasoning about social interactions. In tasks. In Proceedings of the 2020 Conference on
Proceedings of the 2019 Conference on Empirical EmpiricalMethodsinNaturalLanguageProcessing
Methods in Natural Language Processing and the (EMNLP2020),pages7882–7926.
9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP 2019), pages Alex Wang, Jan Hula, Patrick Xia, Raghavendra Pap-
4463–4473. pagari, R. Thomas McCoy, Roma Patel, Najoung

### Kim, Ian Tenney, Yinghui Huang, Katherin Yu,

Timo Schick and Hinrich Schütze. 2021. It’s not just Shuning Jin, Berlin Chen, Benjamin Van Durme,
size that matters: Small language models are also Edouard Grave, Ellie Pavlick, and Samuel R. Bowfew-shotlearners. InProceedingsofthe2021Con- man.2019a. Canyoutellmehowtogetpastsesame
ference of the North American Chapter of the As- street? sentence-level pretraining beyond language
sociation for Computational Linguistics: Human modeling. InProceedingsoftheAnnualMeetingof

<!-- Page 15 -->

theAssociationforComputationalLinguistics(ACL RuiZhangandJoelTetreault.2019. Thisemailcould
2019),pages4465–4476. saveyourlife: Introducingthetaskofemailsubject
line generation. In Proceedings of the 57th Annual
Alex Wang, Yada Pruksachatkun, Nikita Nangia, Meeting of the Association for Computational Lin-
AmanpreetSingh, JulianMichael, FelixHill, Omer guistics(ACL2019),pages446–456.

### Levy, and Samuel Bowman. 2019b. Superglue: A

stickierbenchmarkforgeneral-purposelanguageun- Sheng Zhang, Xiaodong Liu, Jingjing Liu, Jianfeng
derstandingsystems. InProceedingsofthe33rdIn- Gao, Kevin Duh, and Benjamin Van Durme. 2018.
ternational Conference on Neural Information Pro- Record: Bridging the gap between human and macessing Systems (NeurIPS2019), volume 32, pages chinecommonsensereadingcomprehension. arXiv
3266–3280. preprintarXiv:1810.12885.
Xiang Zhang, Junbo Zhao, and Yann LeCun. 2015.
Alex Wang, Amanpreet Singh, Julian Michael, Felix
Character-levelconvolutionalnetworksfortextclas-
Hill, Omer Levy, and Samuel R Bowman. 2019c.
sification. InProceedingsofthe29thConferenceon

### Glue:Amulti-taskbenchmarkandanalysisplatform

Neural Information Processing Systems (NeurIPS
fornaturallanguageunderstanding. Proceedingsof
2015),volume28,pages649–657.
the7thInternationalConferenceonLearningRepresentations(ICLR2019).
Zihao Zhao, Eric Wallace, Shi Feng, Dan Klein, and

### SameerSingh.2021. Calibratebeforeuse: Improv-

AlexWarstadt,AmanpreetSingh,andSamuelR.Bowing few-shot performance of language models. In
man.2019. Neuralnetworkacceptabilityjudgments.

### Proceedings of the 38th International Conference

Transactions of the Association for Computational
onMachineLearning(ICML2021),volume139of
Linguistics(TACL2019),7:625–641.
PMLR,pages12697–12706.
Adina Williams, Nikita Nangia, and Samuel Bowman.

## A broad-coverage challenge corpus for sentenceunderstandingthroughinference. InProceedingsoftheConferenceoftheNorthAmericanChapter of the Association for Computational Linguistics:HumanLanguageTechnologies(NAACL2018),

pages1112–1122.
Zhilin Yang, Zihang Dai, Yiming Yang, Jaime Carbonell,RussRSalakhutdinov,andQuocVLe.2019.
Xlnet: Generalized autoregressive pretraining for
languageunderstanding. InProceedingsofthe33th
Conference on Neural Information Processing Systems(NeurIPS2019),volume32,pages5753–5763.

### ZhilinYang,PengQi,SaizhengZhang,YoshuaBengio,

WilliamCohen, RuslanSalakhutdinov, andChristopher D. Manning. 2018. HotpotQA: A dataset
for diverse, explainable multi-hop question answering. InProceedingsoftheConferenceonEmpirical
Methods in Natural Language Processing (EMNLP
2018),pages2369–2380.
Wenpeng Yin, Dragomir Radev, and Caiming Xiong.

## DocNLI:Alarge-scaledatasetfordocumentlevelnaturallanguageinference. InFindingsofthe

AssociationforComputationalLinguistics(Findings
ofACL-IJCNLP2021),pages4913–4922.
Elad Ben Zaken, Shauli Ravfogel, and Yoav Goldberg. 2021. Bitfit: Simple parameter-efficient
fine-tuningfortransformer-basedmaskedlanguagemodels. arXivpreprintarXiv:2106.10199.

### Rowan Zellers, Ari Holtzman, Yonatan Bisk, Ali


### Farhadi, and Yejin Choi. 2019. HellaSwag: Can a

machine really finish your sentence? In Proceedings of the 57th Annual Meeting of the Association
for Computational Linguistics (ACL 2019), pages
4791–4800.

<!-- Page 16 -->

Appendices Modelsize

### Method


## Small Base Large Xl Xxl


### A FullresultsforFigure1


## Promptdesign(Gpt-3) 40.6 43.4 45.1 47.8 52.8


## Modeltuning 62.80.8 73.70.6 81.30.6 83.10.2 89.90.2

Table4showstheperformanceofdifferentmodel P M R U O L M T P I- T T T A U SK N M IN O G DELTUNING 5 6 9 4 . . 8 6 0 0 . . 8 2 6 7 3 9 . . 1 2 1 0 . . 1 3 7 8 4 4 . . 5 5 2 0 . . 2 1 8 7 8 9 . . 0 2 0 0 . .9 5 8 9 8 0 . . 8 1 0 0 . . 2 2
tuning and prompt tuning methods (described

## Spot(Ours) 64.50.3 73.20.3 82.70.2 88.70.3 91.20.1

in§2.1.1)ontheSUPERGLUEbenchmark.
Table4: SUPERGLUE performanceofdifferentmodel
tuningandprompttuningmethodsacrossmodelsizes.
B Sourcedatasetsusedinour SPOT Wereportthemeanandstandarddeviation(inthesubexperimentsin§2 script) across three random seeds. SPOT outperforms
vanilla PROMTTUNING and GPT-3 by a large margin,
Figure 6 displays the datasets used in our SPOT matching or outperforming MODELTUNING across all
experimentsin§2. InadditiontotheC4unlabeled modelsizes.AttheXXLmodelsize,SPOTevenoutperdataset (Raffel et al., 2020), we use 55 labeled formsMULTI-TASKMODELTUNING,whichfine-tunesthe
datasets. ThesedatasetscomefromcommonNLP entire model on the GLUE mixture before fine-tuning
benchmarks/familiesoftasks,namely: itonindividualSUPERGLUEtasks.
• GLUE (Wang et al., 2019c), including
• Commonsense reasoning on RAIN-

### COLA (Warstadt et al., 2019), SST-2 (Socher

BOW (Lourie et al., 2021) includet al., 2013), MRPC (Dolan and Brockett,
ing αNLI (Bhagavatula et al., 2020),
2005), QQP (Iyer et al., 2017), STS-B (Cer
et al., 2017), MNLI (Williams et al., 2018),

### COSMOSQA (Huang et al., 2019), HEL-

QNLI (Wang et al., 2019c), and RTE (Dagan
LASWAG (Zellers et al., 2019), PIQA (Bisk
etal.,2005,etseq.).
et al., 2020), SOCIALIQA (Sap et al., 2019),
andWINOGRANDE(Sakaguchietal.,2020).
• SUPERGLUE (Wang et al., 2019b), including
BOOLQ (Clark et al., 2019), CB (De Marn- • Machine translation, including WMT
effe et al., 2019), COPA (Roemmele et al., ENDE (Bojaretal.,2014), WMTENFR (Bojar
2011), MULTIRC (Khashabi et al., 2018), et al., 2015), and WMT ENRO (Bojar et al.,
2016).
RECORD(Zhangetal.,2018),RTE,WIC(Pilehvar and Camacho-Collados, 2019), and
• Summarization,includingAESLC(Zhangand
WSC(Levesqueetal.,2012).

### Tetreault,2019),BILLSUM(KornilovaandEi-

• Natural language inference (NLI), including delman, 2019), CNN/DAILYMAIL (Hermann
ANLI(Nieetal.,2020),CB,DOCNLI(Yinetal., et al., 2015; See et al., 2017), WIKILIN-
2021),MNLI,QNLI,RTE,andSNLI(Bowman GUA (Ladhak et al., 2020), GIGAWORD (Graff
etal.,2015). et al., 2003; Rush et al., 2015), MULTI-

### NEWS(Fabbrietal.,2019),NEWSROOM(Grusky

• Paraphrasing/semantic similarity, including et al., 2018), SAMSUM (Gliwa et al., 2019),
CXC (Parekh et al., 2021), MRPC, QQP, and andXSUM(Narayanetal.,2018).

## Sts-B.

• Natural language generation on
• Sentimentanalysis,includingCR(HuandLiu, GEM (Gehrmann et al., 2021), including
2004), GOEMOTIONS (Demszky et al., 2020), COMMONGEN (Lin et al., 2020), DART (Nan
SENTIMENT140 (Go et al., 2009), SST-2, and et al., 2021), E2E (Dušek et al., 2019),
YELP-2(Zhangetal.,2015). SGD(Rastogietal.,2020),WEBNLG(Gardent
et al., 2017), WIKIAUTO (Jiang et al., 2020a),
• Question answering (QA) on MRQA (Fisch
XSUM,andWIKILINGUA.
et al., 2019), including SQUAD (Rajpurkar et al., 2016), NEWSQA (Trischler
et al., 2017), TRIVIAQA (Joshi et al., C Additionaltrainingdetails
2017), SEARCHQA (Dunn et al., 2017),
HOTPOTQA (Yang et al., 2018), and NAT- ForPROMPTTUNING,followingLesteretal.(2021),
URALQUESTIONS (NQ (Kwiatkowski et al., we initialize the prompt tokens with embeddings
2019)). thatrepresentanenumerationoftheoutputclasses

<!-- Page 17 -->


### Translation

GLUE NLI Paraphrasing/

### WMT EnDe WMT EnFr

CoLA SST-2 ANLI CB Similarity RAINBOW

### WMT EnRo


### MRPC QQP DocNLI MNLI CxC MRPC αNLI CosmosQA

STS-B MNLI QNLI RTE QQP STS-B HellaSWAG PIQA

### Summarization

QNLI RTE SNLI SocialIQa WinoGrande
Aeslc BillSum

## C4

CNN/Dailymail Wikilingua
SuperGLUE Sentiment GEM

### MRQA Gigaword MultiNews

BBoooolQlQ CB CR Goemotions CommonGen DART

### SQuAD NewsQA Newsroom SAMSum

CCOOPPAA MultiRC Sentiment140 SST-2 E2E SGD

### TriviaQA SearchQA XSum

RReeCCooRRDD RTE Yelp-2 WebNLG WikiAuto

### HotpotQA NQ


### WWiCiC WSC XSum Wikilingua

Figure6: Datasetsusedinour SPOT experimentsin§2. C4, MNLI,and SQUAD wereallusedbythemselvesas
singlesourcetasksinadditiontobeingmixedinwithothertasks.
Total Tuned

### Model

parameters parameters

## Score Boolq Cb Copa Multirc Record Rte Wic Wsc

ST-MOE-32B 269B 269B 91.2 92.4 96.9/98.0 99.2 89.6/65.8 95.1/94.4 93.5 77.7 96.6
Top-7 TURINGNLRV5 5.4B 5.4B 90.9 92.0 95.9/97.6 98.2 88.4/63.0 96.4/95.9 94.1 77.1 97.3
submissions ERNIE3.0 12B 12B 90.6 91.0 98.6/99.2 97.4 88.6/63.2 94.7/94.2 92.6 77.4 97.3
T5+UDG 11B 11B 90.4 91.4 95.8/97.6 98.0 88.3/63.0 94.2/93.5 93.0 77.9 96.6
DEBERTA/TURINGNLRV4 3.1B 3.1B 90.3 90.4 95.7/97.6 98.4 88.2/63.7 94.5/94.1 93.2 77.5 95.9
HUMANBASELINES - - 89.8 89.0 95.8/98.9 100.0 81.8/51.9 91.7/91.3 93.6 80.0 100.0
T5 11B 11B 89.3 91.2 93.9/96.8 94.8 88.1/63.3 94.1/93.4 92.5 76.9 93.8
FROZENT51.1+SPOT 11B 410K 89.2 91.1 95.8/97.6 95.6 87.9/61.9 93.3/92.4 92.9 75.8 93.8
Parameterefficient GPT-3FEW-SHOT 175B 0 71.8 76.4 52.0/75.6 92.0 75.4/30.5 91.1/90.2 69.0 49.4 80.1
adaptation WARPFEW-SHOT 223M 25K 48.7 62.2 70.2/82.4 51.6 0.0/0.5 14.0/13.6 69.1 53.1 63.7
CBOW 15M 33K 44.5 62.2 49.0/71.2 51.6 0.0/0.5 14.0/13.6 49.7 53.1 65.1
Table5: SUPERGLUEresultsofourSPOT XXLsubmission(ingreen)andcompetitorsfromtheleaderboardasof
2022/02/09.
with a back off to sampled vocabulary to fill any Our SPOT submissionachievesa scoreof89.2,
remainingpromptpositions. which far exceeds all other parameter-efficient
For model tuning approaches, we use the de- adaptation methods, including GPT-3, which benfaulthyperparametersfor T5 (Raffeletal.,2020), efits from over 10× more frozen parameters (ali.e.,learningrate0.001,Adafactoroptimizerwith thoughitusesnotunedparameters). Comparedto
pre-trainingparameterstatesrestored,anddropout WARP(Hambardzumyanetal.,2021),ourSPOTapprobability0.1. Toimprovethemodeltuningbase- proachtunes16×moreparameters(410Kvs.25K),
lines,weperformasweepoverthebatchsizehy- andbenefitsfrom50×morefrozenparameters.
perparameterandselect216 tokensperbatch,fol- To the best of our knowledge, SPOT is the first
lowingLesteretal.(2021). parameter-efficientadaptationapproachthatiscompetitivewithmethodsthattunebillionsofparam-
D Detailsofour SUPERGLUE submission eters. Most notably, SPOT’s performance almost
matchesthatoffullyfine-tunedT5XXL(89.3),de-
Table 5 shows the performance of our SPOT XXL
spitebuildingonthesameunderlyingmodel,and

### SUPERGLUEsubmission,alongwithseveralstrong

tuning 27,000× fewer parameters. We note that
competitors from the public SUPERGLUE leaderboard. Apart from the human baseline, the top-7
SPOToutperformsT5onthreeofeightSUPERGLUE
tasks(namely,CB,COPA,RTE).
submissionsalltune>3Bparametersdirectlyonthe
final tasks. Only three previous SUPERGLUE sub- E Tasktransferabilityresults
missionsuseparameterefficientadaptation,inthe
senseoftuning<1Mparametersonthefinaltasks; The full results of our task transferability experallothersubmissionstune>50Mparameters.17 iments can be found in Table 6. We show that
inmanycases,initializingtheprompttothatofa
17The“AILabsTeam,Transformers”submissionislisted
astuning3Mparameters,butwesuspectthisisinerror,asthe submissionmentionsusingtheT5-3BandT5-LARGEmodels.

<!-- Page 18 -->

sourcetaskcanprovidesignificantgainonatarget
task. Table7displayspositivetransferswithmore
than10%relativeerrorreductiononthetargettask.

### F Taskembeddingsimilarity


### InFigure7,weshowaclusteredheatmapofcosine

similarities between the task embeddings of the
26 NLP tasks we study in our task transferability
experiments. Foreachtask,weincludetheresulting task embeddings from all the three different
prompttuningrunsonthetask. Ascanbeseen,our
taskembeddingscapturetaskrelationships: similar
tasks cluster together. Additionally, task embeddingsthatarederivedfromdifferentpromptsofthe
sametaskarelinkedtogether.
G Correlationbetweentasksimilarity
andtasktransferability

### Figure8showshowtherelativeerrorreductionon

atargettaskchangesasafunctionofthesimilarity
betweenthesourceandtargettaskembeddings.

<!-- Page 19 -->


### Boolq Cola Sts-B Wic Cr Mrpc Rte Wsc Copa Cb

BASELINE 73.0 1.2 52.9 1.2 88.1 0.6 63.6 1.6 93.5 0.2 86.1 0.7 68.7 1.2 71.5 1.7 56.7 1.7 92.7 1.9
C4 75.8 0.5 54.8 1.1 87.8 0.6 66.3 0.8 93.9 0.1 88.0 0.6 69.1 1.9 68.0 0.5 54.3 0.9 83.1 5.7
DOCNLI 72.7 1.4 52.7 0.9 87.3 0.9 64.7 0.3 93.6 0.4 86.2 0.8 67.4 2.6 71.1 3.6 56.0 5.9 87.2 1.7
YELP-2 74.8 0.7 53.9 0.2 88.1 0.3 64.7 0.5 93.8 0.3 86.6 0.8 69.2 1.1 70.8 1.2 55.0 0.0 87.8 1.6
MNLI 77.6 0.4 54.2 0.7 89.5 0.3 69.5 0.5 93.9 0.4 88.4 0.6 74.7 1.3 71.8 3.3 69.3 2.1 97.0 1.1
QQP 75.9 0.5 55.6 1.3 89.4 0.2 67.9 0.2 93.7 0.5 88.1 0.7 72.0 0.5 71.5 0.9 62.0 2.2 88.7 4.2
QNLI 75.6 0.5 55.5 2.0 89.2 0.2 69.6 1.3 93.8 0.2 87.8 0.1 71.1 0.8 71.5 2.5 59.7 3.9 92.5 1.1
RECORD 73.1 0.9 54.7 1.3 87.7 0.7 65.5 0.9 93.7 0.1 88.7 0.3 67.5 1.3 77.2 2.3 59.3 1.2 74.1 5.2
CXC 75.9 0.4 55.0 0.2 90.0 0.0 70.2 0.1 93.9 0.2 88.0 0.4 70.3 0.5 68.6 2.5 60.3 3.9 89.3 2.4
SQUAD 76.0 0.7 54.9 1.2 87.6 0.1 66.8 0.3 93.9 0.5 88.7 0.7 71.2 0.4 72.4 0.5 63.0 1.6 91.3 1.3
DROP 73.6 1.3 53.0 1.0 86.9 0.9 67.5 1.2 93.7 0.2 88.2 0.3 65.7 3.1 73.4 2.0 60.0 3.6 78.5 8.6
SST-2 73.3 0.5 52.3 0.3 87.9 0.3 63.8 1.7 93.8 0.5 85.6 0.9 66.9 1.1 68.6 0.4 57.0 2.2 92.9 1.3
WINOGRANDE 74.1 0.8 52.8 1.6 87.8 0.3 62.4 2.5 93.7 0.1 86.1 0.5 67.9 1.3 71.5 2.5 56.7 1.2 83.9 0.8
HELLASWAG 70.0 2.6 32.7 23.6 87.5 0.2 60.1 3.9 93.6 0.0 86.6 1.4 63.9 5.4 70.2 2.1 58.0 2.2 85.5 2.6
MULTIRC 74.0 0.5 50.0 4.6 88.2 0.2 66.4 0.5 93.4 0.1 86.4 1.3 67.6 1.0 69.2 4.1 56.0 4.1 80.0 8.6
COSMOSQA 73.4 1.3 52.1 2.3 87.7 0.5 65.9 1.0 93.6 0.3 87.9 0.8 68.7 1.6 69.6 3.2 62.3 5.0 83.9 8.8
RACE 73.6 0.5 52.5 2.8 87.5 0.5 63.1 5.3 93.4 0.2 86.5 0.8 66.5 2.0 68.9 1.2 57.3 1.2 84.8 3.4
Table 6: Many tasks can benefit each other via prompt transfer. The orange-colored row shows the results of
prompttuningT5BASEonthetargettasksfromscratch(i.e.,withoutanyprompttransfer). Eachcellintheother
rowsrepresentsthetargettaskperformancewhentransferringthepromptfromtheassociatedsourcetask(row)to
the associated target task (column). Positive transfers are shown in green and the best results are highlighted in
bold(green). Numbersinthesubscriptindicatethestandarddeviationacross3randomseeds.
Transfer Increase(relative)

## Mnli→Cb 58.9


## Mnli→Copa 29.1


## Record→Wsc 20.0


## Mnli→Rte 19.2


## Record→Mrpc 18.7


## Squad→Mrpc 18.7


## Cxc→Wic 18.1


## Mnli→Boolq 17.0


## Mnli→Mrpc 16.5


## Qnli→Wic 16.5


## Mnli→Wic 16.2


## Cxc→Sts-B 16.0


## Drop→Mrpc 15.1


## Squad→Copa 14.5


## Qqp→Mrpc 14.4


## Cxc→Mrpc 13.7


## C4→Mrpc 13.7


## Cosmosqa→Mrpc 12.9


## Cosmosqa→Copa 12.9


## Qqp→Copa 12.2


## Qnli→Mrpc 12.2


## Qqp→Wic 11.8


## Mnli→Sts-B 11.8


## Squad→Boolq 11.1


## Qqp→Sts-B 10.9


## Qqp→Boolq 10.7


## Cxc→Boolq 10.7


## Drop→Wic 10.7


## Qqp→Rte 10.5


## C4→Boolq 10.4

Table 7: Positive transfers with more than 10% relative error reduction on the target task. s → t denotes the
transferfromsourcetaskstotargettaskt.

<!-- Page 20 -->

1_4C 2_4C 3_4C 1_CSW 2_CSW 3_CSW 3_DAuQS 1_DAuQS 2_DAuQS 1_PORD 2_PORD 3_PORD 2_DRoCeR 1_DRoCeR 3_DRoCeR 2_ALoC 1_ALoC 3_ALoC 3_ETR 3_ILNcoD 1_ILNcoD 2_ILNcoD 2_BC 1_BC 3_BC 2_ILNM 1_ILNM 3_ILNM 2_CxC 1_CxC 3_CxC 1_B-STS 2_B-STS 3_B-STS 1_ETR 2_ETR 2_CPRM 1_CPRM 3_CPRM 3_PQQ 1_PQQ 2_PQQ 1_ILNQ 2_ILNQ 3_ILNQ 2_APOC 1_APOC 3_APOC 2_2-pleY 1_2-pleY 3_2-pleY 2_2-TSS 1_2-TSS 3_2-TSS 3_RC 1_RC 2_RC 1_CiW 2_CiW 3_CiW 1_CRitluM 2_CRitluM 3_CRitluM 1_QlooB 2_QlooB 3_QlooB 3_ECAR 1_ECAR 2_ECAR 1_AQsomsoC 2_GAWSalleH 3_GAWSalleH 2_AQsomsoC 1_GAWSalleH 3_AQsomsoC 3_ednarGoniW 1_ednarGoniW 2_ednarGoniW
1.0
0.8
0.6
0.4
0.2

## 0 C C 4 4 _ _ 1 2


## C4_3


## Wsc_1


## Wsc_2


## Wsc_3

SQuAD_3
SQuAD_1
SQuAD_2

## Drop_1


## Drop_2


## Drop_3

ReCoRD_2
ReCoRD_1
ReCoRD_3
CoLA_2
CoLA_1
CoLA_3

## Rte_3

DocNLI_3
DocNLI_1
DocNLI_2

## Cb_2


## Cb_1


## Cb_3


## Mnli_2


## Mnli_1


## Mnli_3

CxC_2
CxC_1

### CxC_3


## Sts-B_1


## Sts-B_2


## Sts-B_3


## Rte_1


## Rte_2


## Mrpc_2


## Mrpc_1


## Mrpc_3


## Qqp_3


## Qqp_1


## Qqp_2


## Qnli_1


## Qnli_2


## Qnli_3


## Copa_2


## Copa_1


## Copa_3

Yelp-2_2
Yelp-2_1
Yelp-2_3

## Sst-2_2


## Sst-2_1


## Sst-2_3


## Cr_3


## Cr_1


## Cr_2

WiC_1
WiC_2

### WiC_3

MultiRC_1
MultiRC_2
MultiRC_3
BoolQ_1
BoolQ_2
BoolQ_3

## Race_3


## Race_1


## Race_2


### CosmosQA_1

HellaSWAG_2
HellaSWAG_3

### CosmosQA_2

HellaSWAG_1

### CosmosQA_3

WinoGrande_3
WinoGrande_1

### WinoGrande_2

Figure7: Ourprompt-basedtaskembeddingscapturetaskrelationships: similartasksgrouptogetherintoclusters.
Additionally,taskembeddingsthatarederivedfromdifferentpromptsofthesametaskarelinkedtogether.t_1,t_2,
t_3correspondtothreedifferentprompttuningrunsontaskt.

<!-- Page 21 -->


### BoolQ CoLA STS-B WiC CR

(r = -0.070, p = 0.635) (r = 0.028, p = 0.852) (r = 0.708, p = 1.853e-08) (r = 0.163, p = 0.270) (r = 0.234, p =0.110)

## Mrpc Rte Wsc Copa Cb

(r = 0.243, p = 0.096) (r = 0.290, p = 0.046) (r = 0.428, p = 0.002) (r = 0.140, p = 0.343) (r = 0.490, p = 0.000)
cosine similarity
noitcuder
rorre
evitaler
Figure8: Correlationbetweentasksimilarityandtasktransferability. Eachpointrepresentsasourceprompt. The
x-axisshowsthecosinesimilaritybetweentheassociatedsourceandtargettaskembeddings,averagedoverthree
runsforthetargettask(orangetitle). They-axismeasurestherelativeerrorreductiononthetargettaskachieved
byeachsourceprompt. WeincludethePearsoncorrelationcoefficient(r)andp-value.

## Tables

**Table (Page 1):**

|  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  | P |  | D s (GPT- | 3) |  |
|  |  |  | M P M SP | T T - s M T T (Ours) |  |  |
|  |  |  |  |  |  |  |


**Table (Page 2):**

|  |  |  |  |
|---|---|---|---|
| Source Prompt Tuning |  |  | Target Prompt Tuning |
|  | Initialization |  |  |


**Table (Page 2):**

| 🔥 tuned |
|---|
| ❄ frozen |


**Table (Page 2):**

|  |  |  |
|---|---|---|
|  |  |  |


**Table (Page 7):**

| (r = 0.708, p = 1.853e-08) WiC |  |  |  | (r = 0.290, p = 0.046) WSC |
|---|---|---|---|---|
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  | WSC |
|  |  |  |  |  |
|  |  |  |  |  |


**Table (Page 7):**

|  |  |  |
|---|---|---|
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |


**Table (Page 7):**

|  |  |  |  | (r = 0.428, p = 0.002) similarity |
|---|---|---|---|---|
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
| cosine |  |  |  | similarity |


**Table (Page 7):**

|  |  |  |
|---|---|---|
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |


**Table (Page 21):**

| (r = -0.070, p = 0.635) |  | (r = 0.028, p = 0.852) | (r = 0.708, p = 1.853e-08) | (r = 0.163, p = 0.270) |  |  |  |  | (r = 0.234, p =0.110) |
|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
| MRPC RTE WSC COPA CB |  |  |  |  |  |  |  |  |  |


**Table (Page 21):**

|  |  |  |
|---|---|---|
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |


**Table (Page 21):**

|  |  |  |
|---|---|---|
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |


**Table (Page 21):**

|  |  |  |
|---|---|---|
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |


**Table (Page 21):**

|  |  |  |
|---|---|---|
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |


**Table (Page 21):**

| (r = 0.243, p = 0.096) | (r = 0.290, p = 0.046) | (r = 0.428, p = 0.002) | (r = 0.140, p = 0.343) |  |  |  |  | (r = 0.490, p = 0.000) |
|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
| cosine similarity |  |  |  |  |  |  |  |  |


**Table (Page 21):**

|  |  |  |
|---|---|---|
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |


**Table (Page 21):**

|  |  |  |
|---|---|---|
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |


**Table (Page 21):**

|  |  |  |
|---|---|---|
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |


**Table (Page 21):**

|  |  |  |
|---|---|---|
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
