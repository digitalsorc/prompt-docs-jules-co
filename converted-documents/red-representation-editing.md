---
title: "RED Representation Editing"
original_file: "./RED_Representation_Editing.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["llm", "rag", "fine-tuning", "evaluation", "multimodal"]
keywords: ["red", "large", "page", "tuning", "lora", "adapter", "arxiv", "learningrate", "base", "batchsize"]
summary: "<!-- Page 1 -->

Advancing Parameter Efficiency in Fine-tuning via Representation Editing

### MulingWu,WenhaoLiu,XiaohuaWang,TianlongLi,ChangzeLv

ZixuanLing,JianhaoZhu,CenyuanZhang,XiaoqingZheng*,XuanjingHuang

### SchoolofComputerScience,FudanUniversity,Shanghai,China

{mlwu22,whliu22,xiaohuawang22,tlli22,czlv22}@m.fudan.edu.cn
{zhengxq,xjhuang}@fudan.edu.cn
Abstract andincreasinglydauntingasmodelscalescontinue
togrow(Brownetal.,2020). Forinstance,BERT
ParameterEfficientFine-Tuning(PEFT)tech-"
related_documents: []
---

# RED Representation Editing

<!-- Page 1 -->

Advancing Parameter Efficiency in Fine-tuning via Representation Editing

### MulingWu,WenhaoLiu,XiaohuaWang,TianlongLi,ChangzeLv

ZixuanLing,JianhaoZhu,CenyuanZhang,XiaoqingZheng*,XuanjingHuang

### SchoolofComputerScience,FudanUniversity,Shanghai,China

{mlwu22,whliu22,xiaohuawang22,tlli22,czlv22}@m.fudan.edu.cn
{zhengxq,xjhuang}@fudan.edu.cn
Abstract andincreasinglydauntingasmodelscalescontinue
togrow(Brownetal.,2020). Forinstance,BERT
ParameterEfficientFine-Tuning(PEFT)tech- comprisesupto220millionparameters,T5scales
niqueshavedrawnsignificantattentiondueto
upto11billionparameters,andGPT-3boastsanastheirabilitytoyieldcompetitiveresultswhile
tounding175billionparameters. Consequently,the
updatingonlyasmallportionoftheadjustable
efficientand effectiveadaptationof large models
parameters. However,existingPEFTmethods
tospecificdownstreamtaskspresentsanintriguing
pose challenges in hyperparameter selection,
suchaschoosingtherankforLoRAorAdapter, researchchallenge(Heetal.,2021).
or specifying the length of soft prompts. To In response to this challenge, researchers have
addressthesechallenges,weproposeanovel put forward three main lines of Parameter Effifine-tuningapproachforneuralmodels,named
cientFine-Tuning(PEFT)techniques(Dingetal.,

### RepresentationEDiting(RED),whichmodifies

2022). Firstly,addition-basedmethodsinvolvethe
the representations generated at some layers
introduction of additional trainable neural modthroughtheapplicationofscalingandbiasing
ules or parameters that were not present in the
operations. WhileexistingPEFTmethodsstill
demonstrateover-parameterizationthatcould originalmodel(Houlsbyetal.,2019;KarimiMapotentiallyunderminethegeneralizationability habadi et al., 2021; Li and Liang, 2021a; Lester
acquiredfrompre-training,REDcansubstan- et al., 2021a). Specification-based methods, on
tially reduce the number of trainable param- the other hand, identify certain parameters in the
eters by a factor of 25,700 compared to full
original model to be trainable, while the rest are
parameterfine-tuningandbyafactorof32relkeptfrozen(Zakenetal.,2021;Guoetal.,2020).
ativetoLoRA.Remarkably,REDachievesre-
Lastly, reparameterization-based methods reconsultscomparableorsuperiortobothfullparamfiguretrainableparametersintoamoreparametereterfine-tuningandotherPEFTmethods. Extensiveexperimentsacrossvariousmodelarchi- efficientformthroughcertaintransformations(Hu
tecturesandscales,includingRoBERTa,GPT- etal.,2021;Zhangetal.,2023a;Dingetal.,2023).
2, T5, andLLaMA-2, havedemonstratedthe AmongthesePEFTmethods,Low-RankAdapeffectivenessandefficiencyofRED1,thereby
tation (LoRA) stands out as one of the most effipositioningitasapromisingPEFTstrategyfor
cienttechniqueswithitseffectivenessempirically
large-scaleneuralmodels.
validatedacrossvariousmodelsofdiversescales.
Despiteitsimpressiveperformance,LoRAstillde-
1 Introduction
mands a significant number of trainable parame-
Pre-trainingonlarge-scaleunlabeleddatasetsfol- ters. Recent studies by Aghajanyan et al. (2020)
lowed by fine-tuning on task-specific dataset has and Kopiczko et al. (2023) indicate that the updemonstrated remarkable efficacy across various perboundforintrinsicdimensionsissubstantially
natural language processing (NLP) tasks, estab- smallerthanwhatistypicallyusedinsuchmethods.
lishing itself as the prevailing training paradigm Forexample,thed value(theminimumnumber
90
(Devlin et al., 2018; Raffel et al., 2020; Radford of trainable parameters required to reach 90% of
etal.,2018). However,conductingfullparameter theperformanceofthefully-parameterfine-tuned
fine-tuningforeachtaskcanbeexceedinglycostly model)fortheRoBERTabaseisreportedtobe896.
However,whenLoRAisappliedtofine-tunethis
*Correspondingauthor.
model, the number of trainable parameters esca-
1Thecodeisaccessibleathttps://github.com/mlwu22/
RED. lates to 0.3 million, suggesting the potential for
4202
nuJ
2
]GL.sc[
3v97151.2042:viXra

<!-- Page 2 -->

furtherreductioninparametercount. tersandmaintainingeaseofimplementation.
Inadditiontotheissueofrequiringtoomanyad- • Acomprehensiveablationstudyisconducted
justableparameters,existingPEFTmethods(Mao todissecttheindividualcomponentsofRED
etal.,2021;Heetal.,2021;Dingetal.,2022)pri- andunderstandtheirimpactsonperformance.
marilyfocusonthedesignoflightweightmodules
and their integration (or placement) within base
2 RelatedWork
models. Nonetheless,theimplementationofthese
PEFTtechniquesintroducesadditionalcomplexi- ExistingPEFTmethodscanbebroadlyclassified
tiesinhyperparameterselection,suchaschoosing intothreecategories(Dingetal.,2022),eachchartherankofLoRAandAdapter,ordecidingonthe acterizedbytheparticularpartsofparametersthat
lengthofSoftPromptandPrefix. theytuneefficiently: addition-based,specification-
Inspired by the concept of representation engi- based,andreparameterization-basedmethods.
neering(Zouetal.,2023),weshiftourfocusaway Addition-basedmethodsperformfine-tuningby
fromtheweightsofmodelsandturnourattention integrating additional lightweight learnable comtotheirrepresentations. Intheneuralarchitecture, ponents into foundational models. More specifinetworkweightsgovernneuralactivities(orrepre- cally,Houlsbyetal.(2019);SticklandandMurray
sentations),whichinturndeterminethenetworks’ (2019);KarimiMahabadietal.(2021)andRücklé
output,andthenetworks’outputultimatelyshapes etal.(2020)proposedtheintegrationoflearnable
thenetworks’behavior. Ratherthanconcentrating bottleneckneuralmodulesintothetransformerlayonneuronsandtheirinterconnections(orweights), ers. Brown et al. (2020) and Shin et al. (2020)
we explored to achieve control over network be- found that the models’ performance could be enhaviorbymanipulatingitsinternalrepresentations. hancedbyappendingdiscretetokens(orprompts)
Specifically, wefine-tuneneuralnetworkmodels atthebeginningoftheinputtextswithoutmodifybydirectlyeditingtherepresentationgeneratedat ingthemodels’parameters. However,themanual
eachlayerwhilemaintainingthemodelparameters creation of such prompts demands substantial effrozen,asillustratedinFigure1(b). Itisworthnot- fort,andoptimizationinadiscretespaceiscomparingthatthenumberofparametersrequiredtoedit ativelymorechallenging. Consequently,laterstudrepresentationsissubstantiallyfewerthanthatof iessubstitutedthesediscretetokenswithcontinuweightswithinneuralnetworks. TakingLLaMA-2 ousvectors,alsoreferredtoassoftprompts,which
(7B) as an example, the proposed representation canbeoptimizedusingthegradientdescentalgoediting(RED)methodachievescompetitiveperfor- rithm (Lester et al., 2021b; Li and Liang, 2021b;
mancebyadjustingonly0.26Mparameters. This Wuetal.,2023;Wangetal.,2023).
is approximately 25,700 times less than what is Specification-basedmethodsachieveparameterrequiredforfull-parameterfine-tuning,rendering efficientfine-tuningbydesignatingasubsetofpathemethodbothstorageandcomputationefficient. rametersformodificationwhileleavingtheremain-
Thecontributionsofthisstudyaresummarized ing parameters untouched. Within this category,
asfollows: Leeetal.(2019)suggestedamethodtoexclusively
updatetheparametersincertaintoplayersofBERT
• Weproposeanovelperspectiveonfine-tuning andRoBERTa. BitFit(Ben-Zakenetal.,2021),on
bydirectlyeditingmodelrepresentations,di- theotherhand,fine-tunesamodelbyonlyoptimizverging from exiting PEFT methods that fo- ingthebiastermsusedinthemodel. Contraryto
cusedonadjustingthemodel’sweights. Our thesemethodsthatpre-determinewhichparameters
proposedPEFTtechnique,termedRED,em- shouldbealtered,Guoetal.(2020)andZhaoetal.
bodiesthisnewperspective. (2020)implementedalearnablemaskingstrategy
• Extensiveexperimentsareconductedacross toautomaticallychoosetheparametersfortuning.
models of varying structures and scales, in- Reparameterization-basedmethodsaimtoopticludingRoBERTa,GPT-2,T5,andLLaMA-2. mizesomeparameterswithinamodel,typicallyin
TheeffectivenessofREDisvalidatedacrossa theirlow-dimensionalsubspace. Huetal.(2021)
rangeofnaturallanguageunderstandingand introduces the use of low-rank matrices, termed
generationtasks. Notably,REDdemonstrates LoRA, to approximate the weight modifications
both efficacy and efficiency while requiring duringthefine-tuningprocess. QLoRA(Dettmers
onlyaminimalnumberoftrainableparame- et al., 2023) combines low-rank adaptation with

<!-- Page 3 -->

Figure1: ComparisonofpreviousrepresentativePEFTmethodswiththeproposedRED.(a)LoRAincorporates
learnable bottleneck-shaped modules (highlighted in orange) by integrating additional connections parallel to
theW andW matricesofattentionblocks,alongwithmodifyingtheweightsofthesematricesinalow-rank
q v
fashion. Adapter,ontheotherhand,introduceslearnablemoduleswithinsimilarstructures(alsohighlightedin
orange)byincorporatingadditionalconnectionsfollowingboththeattentionandfeed-forwardsub-layers. (b)RED
introducestwolearnablevectors,l andl ,todirectlyedittherepresentations(markedingreen)generatedby
scaling bias
feed-forwardsub-layers,whichsignificantlyreducesthenumberofparametersrequiredforfine-tuning.
modelquantizationtofurtherreducestorageusage IA3(Liuetal.,2022)andSSF(Lianetal.,2022).
during the fine-tuning phase. AdaLoRA (Zhang To fulfill the in-context learning capability with
etal.,2023b)proposestouseSVDdecomposition lower computational costs, Liu et al. (2022) protoapproximatethechangesinweights,whichallo- posed to modify the key and value vectors of the
catesmoretrainableparameterstomoreimportant multi-headattentionsandthosegeneratedbyfeedweightmatrices,leadingtoabetterperformance. forwardnetworks(FFNs)byscalingoperations. In
Zouetal.(2023)proposedanapproachtoana- thedomainofcomputervision,Lianetal.(2022)
lyzingandmanipulatingthebehaviorofneuralnet- presentedasimilarmethod,calledSSF,whichwas
worksthroughrepresentationengineering,thereby motivated by batch and layer normalization techshiftingthefocusfromneuronsandtheircircuits niques. Toensurefeaturesfallinadiscriminative
torepresentationsandthetransformationsamong spaceforbetterclassification,SSFalsonecessitates
them. Liuetal.(2023)extendedthisworktoalign theadjustmentoffeaturevectorsacrossnearlyall
large language models with human preferences, transformerlayers,includingmulti-headattentions,
achievingresultscomparableorsuperiortoRLHF FFNs, and normalization layers. As a result, the
(Ouyangetal.,2022),butatalowercomputational sizeofparametersadjustedintheirmethodapproxicost. Subramanietal.(2022)investigatedtheex- matesthosemanipulatedinotherPEFTtechniques,
tractionof“steervectors”fromthehiddenlayers suchasAdapterandVPT(Jiaetal.,2022).
andperformedunsupervisedtextstyletransferby Incontrast,ourREDmethodrequiresonlythe
alteringthehiddenrepresentationsusingthesevec- modification of activation patterns generated by
tors. Tocontrolthestyleandsentimentexpressed FFNsub-layers,constitutingasignificantlysmaller
inamodel’soutputs,Turneretal.(2023)integrated portionoftheentireneuralnetwork’sparameters
asimilar“steervector”intotherepresentationof formodelfine-tuning. WhileSSFachievesareduceachhiddenlayerattheinferencetime. Inspiredby tioninthenumberoffine-tuningparametersbya
the recent advance in representation engineering factor of 300 compared to original models, RED
Zouetal.(2023),wesuggestedanovelperspective accomplishesareductionofapproximately25,700
forfine-tuningmodelsbydirectlyeditingtheirrep- times. Moreover,SSF’sevaluationwasrestricted
resentations. Thisnewperspectivewasembodied to a limited range of simple image classification
intheREDtrainingmethod,whichdemonstrated tasks using relatively small models (under 100M
both effectiveness and efficiency while requiring parameters), whereas RED has demonstrated its
onlyaminimalnumberoftrainableparameters. effectivenessacrossavarietyofnaturallanguage
Thisstudyiscloselyrelatedtotworecentworks: understanding and generation tasks, with signifi-

<!-- Page 4 -->

cantlylargermodelsofupto7Bparameters. spacewithapre-specifieddimensionalityr. Subsequently, this dimensionally reduced vector un-
3 Method
dergoesanonlinearactivationfunctionf(·)andan
Weinthissectiongiveaconciseoverviewofprevi- additionalup-projectionmatrixW up ∈ Rr×d toreousPEFTmethodsandintroduceanew,parameter- vertittoitsoriginaldimensiond. Theadaptermodefficient fine-tuning method known as Represen- ule also incorporates a residual connection. The
tation Editing (RED) by highlighting its distinc- resultantoutputh 2 ∈ Rd generatedbythismodule
tivefeaturescomparedtoexistingPEFTmethods. canbeformallyrepresentedasfollows:
REDfacilitatestheadaptationofpre-trainedneural
h = h +f(h W )W (2)
network models to downstream tasks by directly 2 1 1 down up
editingthemodel’srepresentations.

### Expandingonthisresearch,Pfeifferetal.(2020)

3.1 RecapofPEFTMethods proposed a more efficient variant of the Adapter
thatisonlyappliedfollowingtheFFNsub-layer.
The predominant large language models (LLMs)
havebeenconstructedbasedonthetransformerar-
3.2 RepresentationEditing
chitectureproposedinaseminalworkonattention
mechanisms(Vaswanietal.,2017). Thisarchitec- PreviousPEFTmethodsrefinepre-trainedmodels
tureischaracterizedbyaseriesoflayeredblocks, byupdatingtheirweightsinaparameter-efficient
each incorporating two fundamental sub-layers: manner,typicallywithinalow-dimensionalspace.
multi-headself-attentionandfullyconnectedfeed- Toapproximatetheeffectoffull-parametertuning,
forwardnetworks. ManyexistingPEFTmethods theyarerequiredtochoosethevaluesofhyperpausuallyachievefine-tuningbyadjustingtheparam- rameters properly for one downstream task or a
eters of these two sub-layers in some parameter- setoftasks. However,itcouldbetroublesometo
efficient manner. Figure 1 (a) illustrates two ex- chooseasuitablevalueforahyperparameter,such
emplarPEFTmethods: AdapterandLoRA.With astheranksofweightmatricesinEquations(1)and
theexceptionofafewadditionalparametersthat (2)forLoRAandAdapterrespectively. Enhancing
require tuning, the parameters of the pre-trained their modeling capacities by using a higher rank

### LLMremainfixed. r coulddemandtoomuchcomputationresources

Specifically,LoRA(Huetal.,2021)incorporates and tend to overfit, while aggressively setting r
learnablebottleneck-shapedmodulesthroughthe smallermaydegrademodelperformanceandlead
connectionsparalleltotheW andW matricesof tofrom-scratchre-training(Dingetal.,2023).
q v
attentionblocks,asillustratedinFigure1(a),and Ourhypothesispositsthatbyalteringtheinternal
modelstheweightchangesofthesetwomatrices representationsofneuralmodelsratherthantheir
inalow-rankmanner. Givenapre-trainedweight connected weights, the fine-tuning process could
matrixW ∈ Rd×k,LoRArepresentsitschanges, besignificantlymoreefficient. Thisisbecausethat
denotedas∆W,throughtwolow-rankdecompo- direct manipulation of the representations necessition matrices: ∆W = α · W W , where sitates O(n) parameters, whereas adjusting their
down up
W ∈ Rd×r and W ∈ Rr×k (the value of r weightstheoreticallydemandsO(n2)parameters,
down up
istypicallymuchsmallerthanbothdandk). The withndenotingthedimensionalityofhiddenreprecoefficientαisahyperparameterthatdetermines sentations. Turneretal.(2023)havedemonstrated
thesignificanceof∆WrelativetotheoriginalW. that the behaviors of neural models can be influ-
Givenaninputx,LoRAproducestheresultofthe enced by adding a “steer vector” to each hidden
forwardpassasfollows: layerduringinference. Wepostulatethatsuchsteer
vectorscanbelearnedduringthefine-tuningphase.
h = xW+α·xW W (1)
down up Inspiredbythisconceptandtheemergingfieldof
In the initial version of the Adapter, Houlsby representation engineering Zou et al. (2023), we
et al. (2019) suggested the insertion of trainable introduceanovelPEFTmethodthatfine-tunesthe
adaptermodulesbetweentwosub-layerswithinthe modelbydirectlyalteringtherepresentationwith
transformer architecture. These adapter modules twolearnablevectors,asdepictedinFigure1(b).
arestructuredtoincludeadown-projectionmatrix, Specifically,wefirstincorporatealearnablescaldenotedasW ∈ Rd×r,whichtransformsahid- ingvectorl ∈ Rd andapplyittoperformthe
down scaling
denrepresentationh ∈ Rdtoalower-dimensional Hadamardproductwithahiddenrepresentationh
1 1

<!-- Page 5 -->

Method #Param MNLI SST-2 MRPC CoLA QNLI QQP RTE STS-B Avg.

### FT(base) 125M 87.3 94.4 87.9 62.4 92.5 91.7 78.3 90.6 85.6

Adapter(base) 0.4M 87.0 93.3 88.4 60.9 92.5 90.5 76.5 90.5 85.0
LoRA(base) 0.3M 86.6 93.9 88.7 59.7 92.6 90.4 75.3 90.3 84.7
Adapter-FFN(base) 0.3M 87.1 93.0 88.8 58.5 92.0 90.2 77.7 90.4 84.7
BitFit(base) 0.1M 84.7 94.0 88.1 54.0 91.0 87.3 69.8 89.5 82.3
IA3(base) 0.06M 85.4 93.4 86.4 57.8 91.1 88.5 73.5 88.5 83.1
RED(base) 0.02M 83.9 93.9 89.2 61.0 90.7 87.2 78.0 90.4 84.3

### FT(large) 355M 88.8 96.0 91.7 68.2 93.8 91.5 85.8 92.6 88.5

Adapter(large) 0.9M 90.1 95.2 90.5 65.4 94.6 91.4 85.3 91.5 88.0
LoRA(large) 0.8M 90.2 96.0 89.8 65.5 94.7 90.7 86.3 91.7 88.1
Adapter-FFN(large) 0.8M 90.3 96.1 90.5 64.4 94.3 91.3 84.8 90.2 87.7
IA3(large) 0.15M 90.1 94.5 87.1 63.2 93.9 89.3 85.3 91.5 86.9
RED(large) 0.05M 89.5 96.0 90.3 68.1 93.5 88.8 86.2 91.3 87.9
Table1: PerformancecomparisonofRoBERTabaseandlargemodelsfine-tunedbyREDandotherPEFTbaseline
methodsontheGLUEbenchmark. ThestandarddeviationsofresultsacrossdifferentmethodsaregiveninTable17.

### Method #Param BLEU NIST MET ROUGE-L CIDEr


### FT(medium) 355M 65.95 8.52 45.95 69.13 2.35

FTtop2(medium) 25.2M 65.94 8.53 44.28 68.83 2.23
Adapter(medium) 0.9M 64.31 8.29 44.91 67.72 2.28

### LoRA(medium) 0.8M 67.43 8.65 46.01 69.64 2.42


### Adapter-FFN(medium) 0.8M 64.41 8.30 44.74 67.53 2.29

PrefixTuning(medium) 0.8M 63.92 8.26 41.81 66.86 2.03
IA3(medium) 0.17M 63.63 7.99 40.49 66.36 1.89
RED(medium) 0.05M 64.86 8.36 44.99 67.62 2.28

### FT(large) 774M 65.56 8.50 45.40 68.38 2.27

Adapter(large) 1.8M 65.94 8.46 45.78 68.65 2.34

### LoRA(large) 1.5M 68.24 8.76 46.23 69.92 2.42


### Adapter-FFN(large) 1.5M 65.53 8.41 45.65 68.46 2.33

PrefixTuning(large) 1.5M 65.50 8.45 43.97 67.32 2.23

### IA3(large) 0.32M 65.08 8.5 42.72 66.80 2.15


### RED(large) 0.09M 65.77 8.42 46.12 69.03 2.36

Table2: PerformancecomparisonofGPT-2mediumandlargemodelsfine-tunedbyREDandotherPEFTbaseline
methodsontheE2ENLGChallenge. ThestandarddeviationsofresultsacrossdifferentmethodsaregiveninTable
18.
byscalingthefeatureofeachdimensionwithinh understandingandgenerationtasks,employinga
1
viaelement-wisemultiplication. Additionally,we range of foundational models spanning different
introduceanotherlearnablebiasvectorl ∈ Rd scales. ThesemodelsincludeRoBERTa(Liuetal.,
bias
thatissubsequentlyaddedtothescaledvector. This 2019), T5 (Raffel et al., 2020), GPT-2 (Radford
processcanbeformalizedasfollows: etal.,2019),andLLaMA-2(Touvronetal.,2023).

### Specifically, we evaluated RED and the baseline

h 2 = l scaling ⊙h 1 +l bias (3) methods on the GLUE benchmark (Wang et al.,
2018) with RoBERTa and T5, as previously conwhere ⊙ represents element-wise multiplication,
ductedin(Huetal.,2021)andAsaietal.(2022).
alsoknownastheHadamardproduct. Here,h ∈
1 Toensureconsistencywithpreviousstudies,wead-
Rd denotesahiddenrepresentationgeneratedbya
heredtotheexperimentalsetupoutlinedin(Liand
certainlayer,andh ∈ Rd representstheresultant
2 Liang, 2021a) and (Hu et al., 2021) for comparaeditedrepresentation. Duringimplementation,we
tiveanalysiswithGPT-2. Moreover,weconducted
initializethescalingvectorsl asunitvectors
scaling instructiontuningexperimentsonLLaMA-2using
(i.e.,withallelementssetto1)andthebiasvectors
theUltraFeedbackdataset(Cuietal.,2023)tofurl as zero vectors. This initialization approach
bias therassesstheapplicabilityofourproposedRED
ensuresthattheintroductionofthese“editvectors”
ongenerativelargelanguagemodels. Forfurther
does notinitially alterthe hidden representations
detailsonthedatasetsandevaluationmetricsused,
ofaneuralmodel.
pleaserefertoAppendixA.
4 Experiments
4.1 Baselines

### Extensiveexperimentationwasconductedtoassess

theefficacyofourRepresentationEditing(RED) WeensuredthatdifferentPEFTmethodswerecommethodacrossadiversearrayofnaturallanguage paredsystematicallyinamorefairsetting. There-

<!-- Page 6 -->

Method #Param MNLI SST-2 MRPC CoLA QNLI QQP RTE STS-B Avg.

### FT(base)* 220M 86.8 94.6 90.2 61.8 93.0 91.6 71.9 89.7 84.9

Adapter(base)* 1.9M 86.5 93.8 85.3 64.0 93.2 90.2 71.9 90.7 84.5
AdapterDrop(base)* 1.1M 86.3 93.6 86.3 62.7 93.2 90.2 71.2 91.4 84.4
BitFit(base)* 0.3M 85.3 94.2 86.8 58.2 93.0 90.1 67.6 90.9 83.3
PT(base)* 0.08M 81.3 90.9 68.1 10.6 92.8 89.7 54.7 89.5 72.2
RED(base) 0.04M 85.9 93.0 91.7 61.1 91.2 89.2 72.7 88.2 84.1
Table3: PerformancecomparisonofT5basefine-tunedbyREDandotherPEFTbaselinemethodsontheGLUE
benchmark. Resultsmarkedwithanasterisk(*)areexcerptedfrompublishedliterature.
fore,westrictlyfollowedthewell-establishedtrain- proposedbyRückléetal.(2020),whichincoringprotocol,evaluatingonthevalidationsetafter poratesastrategyofomittingcertainadapter
eachepochtraining,andselectingthecheckpoint layers,therebyenhancingoverallefficiency.
withthebestperformanceonthevalidationsetas • Low-Rank Adaption (LoRA) employs a
thefinalmodelfortestingonthetestset. Thefol- low-rankdecompositiononthematrix∆W,
lowingbaselinemethodswereusedforcomparison therebymodelingweightupdatesastheprodwiththeproposedRED: uctoftwolow-rankmatrices. Thesetwolearnablematricesarealignedinparallelwiththe
correspondingmatricesinpre-trainedmodels.
• Fine-Tuning(FT)trainsmodelsbyupdating

### Theyprocessinputsinparallelandcombine

alltheirparameters. AvariantofFTwasprotheir results to generate the final outputs in
posedbyLeeetal.(2019),whichselectively
eachtransformerblock(Huetal.,2021).
updates certain layers while freezing others.
• PromptTuning(PT)prefixesasetofcontinu-
Weincorporateabaselineestablishedinprior
ousvectorsattheembeddinglayer,whichare
researchbyLiandLiang(2021a)withGPT-2,
subjected to learning during the fine-tuning
which specifically adapts only the final two
layers,denotedasFTtop2. phase(Lesteretal.,2021b).
• Prefix Tuning is a generalized version of
• Bias-termsFine-tuning(BitFit)involvesthe
prompttuning(PT),whichincorporateslearnselective freezing of a majority of the transablecontinuousvectorsateveryhiddenstate.
formerparameters,withthetrainingprocess

### These continuous vectors also contribute to

focused exclusively on the bias-terms (Benthecomputationofattention,servingasboth
Zakenetal.,2021).
keyandvaluevectors(LiandLiang,2021b).
• IA3introducesscalingoperationstomodify
thekeyandvaluevectorsofthemulti-headat-
4.2 ResultswithRoBERTa
tentionsandthosegeneratedbyfeed-forward
networks(FFNs)(Liuetal.,2022). Weconductedfine-tuningexperimentsonboththe
• Adapterintroducesalearnable,lightweight RoBERTabase(125M)andlarge(355M)models
modulesituatedbetweentwosub-layersofthe byusingREDanditscompetingbaselines. Subsetransformer. Duringtheforwardpass,inputs quently,weevaluatedthesefine-tunedmodelson
areprocessedinsequencebythesub-layersof thewidely-adoptedGLUEbenchmark,renowned
thefoundationmodelsandtheadapters,yield- for its comprehensive evaluation of natural laningthefinaloutput. However,duringtheback- guageunderstandingcapabilities. Thepretrained
propagationphase,onlytheseadaptersreceive RoBERTamodelsweresourcedfromtheHugginggradients for parameter updates, while the FaceTransformersLibrary(Wolfetal.,2019).
remaining parameters of the model are kept Wenoticedthatthepreviousevaluationsettings
fixedandunaltered(Houlsbyetal.,2019). ofPEFTmethodsencounteredtwoissues. Firstly,
• Adapter-FFNisavariantofAdaptermethod fordatasetssuchasMRPC,RTE,andSTS-B,they
proposedbyPfeifferetal.(2020). Contrasting trained the models on the MNLI dataset first and
withtheoriginalAdapter,whichnecessitates selectingthebestperformancecheckpointonthe
theinsertionofthelearnablemodulebetween MNLIdatasetasinitializationfortransferlearning
allsub-layers,Adapter-FFNonlyrequiresthe to improve the performance of the model trained
applicationofanadapterfollowingeachFeed- onthesedatasets(Liuetal.,2019;Huetal.,2021).
ForwardNetwork(FFN)sub-layer. However,suchapipelineaddscomplexitythatcan
• AdapterDrop is another variant of Adapter be challenging for other researchers to replicate.

<!-- Page 7 -->

Secondly,thereisnosplitbetweenthevalidation modelswerealsoobtainedfromtheHuggingFace
setandthetestset. Instead,aftereachepochtrain- TransformersLibrary. Toensureafaircomparison,
ingiscompleted,evaluationisdirectlyconducted wereproducedotherPEFTmethodsfollowingthe
onthetestset,andthebesttestresultisselectedas settings defined by Li and Liang (2021a) and Hu
thefinalevaluationresultofthemodel,whichvio- etal.(2021). PleaserefertoAppendixB.2forthe
latestheestablishedstandardthatthetestsetshould comprehensivedetailsofourimplementation.
not influence model selection during the training ThedatapresentedinTable2revealsthatRED
phase. In this study, we ensured a more system- achievedperformancecomparabletootherPEFT
atic comparison of different PEFT methods in a baselinesacrossallmetricsintheE2ENLGChalfairersetting. Toachievethis,weadheredstrictly lenge. This highlights the efficacy of fine-tuning
toawell-establishedtrainingprotocol. Aftereach throughrepresentationediting,notonlyfornatural
epochoftraining,evaluationwasconductedonthe languageunderstandingtasksbutalsoforlanguage
validation set, and the checkpoint demonstrating generationtasks. Remarkably,REDaccomplished
thebestperformanceonthevalidationsetwasse- thisperformancewhilestillnecessitatingminimal
lectedasthefinalmodelfortestingonthetestset. fine-tuningofparameters. TocompareREDwith
Forcomprehensivedetailsregardingourreimple- themostparameter-efficientvariantsofotherPEFT
mentation,pleaserefertoAppendixB.1. methods, we set the rank of LoRA and Adapter
AspresentedinTable1,boththeRoBERTabase to1. Undertheseconditions,REDoutperformed
andlargemodelsfine-tunedbyREDyieldedaccu- allsuchvariantswhilestillemployingthefewest
raciescomparabletothoseachievedbyotherPEFT numberofparameters(seeSection5.3fordetails).
methodsacrossalltaskswithintheGLUEbenchmark. Forinstance,RED’sperformancewasonly
marginally inferior to that of LoRA, differing by
anegligible0.2%withtheRoBERTalargeandby
0.4% with the RoBERTa base on average, while
requiringthetuningofsignificantlyfewerparameters. ItisnoteworthythatREDdemonstratedsuperiorperformanceontaskssuchasSST-2,MRPC,

### CoLA,STS-B,andRTE,allofwhichhaddatasizes

less than 100k. This suggests that RED helps to
maintainthegeneralizationcapabilityacquiredduringthepre-trainingphaseandcandeliverenhanced
performance when the volume of training data is
relativelysmall.
Figure 2: Performance scores achieved by RED and

### Moreover,REDexhibitsanunprecedentedlevel

otherPEFTmethodsontheMT-Bench. RefertoTable
ofparameterefficiency. Althoughhavingsubstan-
19andAppendixDforrawscoresandadditionaldetails.
tiallyfewertrainableparameters—approximately
7,200timesfewerthanfullparameterfine-tuning

### Method #Param AlpacaEval(win%)

and16timesfewerthanLoRA—itmaintainscom- FT 6739M 80.93
parable performance. This observation suggests LoRA 8.39M 81.48

## Red 0.26M 81.69

thatthereisstillpotentialforfurtherreductionin
thenumberoftrainableparametersandthisfinding

### Table4:Winratesagainstreferenceresponsesevaluated

alignswithconclusionsdrawnbyAghajanyanetal. byGPT-4onAlpacaEval. Higherwinratesindicatesu-
(2020)andKopiczkoetal.(2023). periorgeneratedresponses,reflectingbetteralignment
withhumanpreferences. Exampleresponsesgenerated
4.3 ResultswithGPT-2 byREDandotherPEFTbaselinescanbefoundinFigures3and4aswellasinAppendixD.
Beyondnaturallanguageunderstandingtasks,our
studyexpandedtoincludeexperimentsonnatural
4.4 ResultswithT5
languagegenerationtasks. Theseexperimentswere
conducted using the GPT-2 medium (355M) and InordertoassesstheversatilityofRED,weconlarge(774M)modelsontheE2ENLGChallenge ductedexperimentsusingtheencoder-decoderar-
(Novikova et al., 2017). The pre-trained GPT-2 chitecture. Morespecifically,weobtainedthepre-

<!-- Page 8 -->


### Method #Param BLEU NIST MET ROUGE-L CIDEr


### Adapter(rank1) 0.25M 63.76 8.37 42.74 66.70 2.09

Adapter-FFN(rank1) 0.07M 62.99 8.09 40.88 66.39 1.98
LoRA(rank1) 0.10M 64.51 8.38 44.78 67.35 2.28

## Red 0.05M 64.86 8.36 44.99 67.62 2.28

Table5: ComparisonofGPT-2fine-tunedbyREDandotherPEFTbaselines(rank1)ontheE2ENLGChallenge.
trainedT5-basemodel(220M)fromtheHugging- thatofLoRA.ThissuggeststhattheREDmethod,
FaceTransformersLibraryandevaluatedmodels whichdirectlyeditshiddenrepresentationsduring
fine-tunedwithREDandotherPEFTbaselineson thefine-tuningphase,continuestobeeffectivefor
theGLUEbenchmark. AsshowninTable3,RED largelanguagemodels,andthetrainedmodelsare
achieved accuracies that were on par with other capableofgeneratinghigh-qualityresponses.
PEFTmethodsacrossalltasksintheGLUEbench- Moreover,Figure2illustratestheperformance
mark, indicating its versatility across diverse net- scoresachievedbythreetrainingmethodsonthe1-
workarchitectures. Weexcerptedtheresultsfrom turnquestion-answerdatasetfromMT-Bench. The
thestudyof(Asaietal.,2022)astheyconducted overall performance of RED is on par with other
experimentsunderthesettingssimilartoours. The baselinemethods,anditnotablyexcelsinassessing
inclusion of their results does not undermine the the capabilities of humanities and reasoning. As
fairnessoroutcomeofthecomparison. Pleaserefer presentedinTable12,REDalsodeliverscompetitoAppendixB.3fortheimplementationdetails. tiveresultsonsixdistinctdatasetsfromtheOpen
ItisnoteworthythatREDsurpassedtheprompt LLMLeaderboard.
tuning (PT) baseline with a significant margin of
Method MRPC CoLA QQP Avg.
11.9%onaverage. DespitePTmethodsnecessitat-

## Red 90.3 68.1 88.7 82.4

ingthefewestparametersduringfine-tuningamong w/oscaling 89.8 65.9 87.6 81.1
w/obias 75.8 46.9 87.2 70.0
other PEFT baselines, they still require a modification of parameters that is twice as large as that
Table6: Resultsoftheablationstudiesonthreedifferrequired by RED. This finding indicates that alentdatasetsfromtheGLUEbenchmark. Theterm“w/o
locatingafewnumberoflearnableparametersto scaling”denotestheremovalofscalingoperations,with
eachlayerforrepresentationeditingisbothmore representationeditingperformedonlybybiasvectors.
parameter-efficientandeffectivecomparedtothe In contrast, “w/o bias” indicates the omission of bias
PTmethod,whichassignsalllearnableparameters vectors, with representation editing conducted exclusivelythroughtheuseofscalingvectors.
tothemodel’sembeddinglayer.
5 AblationStudy
4.5 ResultswithLLaMA-2

### In this section, we conducted a series of ablation

We are interested in exploring whether RED can studiestoexaminetheimpactofdifferentediting
beeffectivelyscaledtolargeneuralnetworkscon- operationsusedinREDandtoexplorepotentialaptainingbillionsofparameters. Therefore,weeval- plicationpointswithintransformer-basednetworks.
uatedREDandcompareditagainstfullparameter WealsoevaluatedtheparameterefficiencyofRED
fine-tuningandLoRAusingLLaMA-2upto7bil- bycomparingitwiththemostparameter-efficient
lionparameters. Ourassessmentswereconducted variantsofotherPEFTmethods.
acrossthreewidely-usedbenchmarks: OpenLLM
Leaderboard(Beechingetal.,2023),AlpacaEval 5.1 ImpactofDifferentEditingOperators
(Li et al., 2023), and MT-Bench (Zheng et al., Weintroducetwooperatorstoeditthehiddenrep-
2023). Theimplementationdetailsofthisexperi- resentationsofneuralnetworkmodels: onescalesa
mentcanbefoundinAppendixB.4. hiddenrepresentationusingalearnablevector,and
Table 4 presents the win rates obtained by dif- theotheraddsabiasvectortothehiddenrepresenferentfine-tuningmethods,comparedagainstthe tation. Toassessthecontributionofeachoperator,
referenceresponsesgeneratedbytext-davinci-003 we performed ablation studies by removing one
ontheAlpacaEval. Remarkably,REDyieldedthe operatoratatimeandexaminingtheimpactonthe
highestwinrate,eventhoughitsnumberoftrain- models’performance.
ableparameterswas25,700timeslessthanthatof FromTable6,itisevidentthatbotheditingoperfull parameter fine-tuning and 32 times less than atorsarecrucialforenhancingmodelperformance.

<!-- Page 9 -->

Method #Param MNLI SST-2 MRPC CoLA QNLI QQP RTE STS-B Avg.
LoRA(base) 0.29M 86.6 93.9 88.7 59.7 92.6 90.4 75.3 90.3 84.7
RED(base) 0.02M 83.9 93.9 89.2 61.0 90.7 87.2 78.0 90.4 84.3
RED+(base) 0.09M 85.9 93.2 88.9 62.4 90.9 89.1 78.6 90.9 85.0
LoRA(large) 0.79M 90.2 96.0 89.8 65.5 94.7 90.7 86.3 91.7 88.1
RED(large) 0.05M 89.5 96.0 90.3 68.1 93.5 88.8 86.2 91.3 87.9
RED+(large) 0.25M 90.6 95.6 89.2 69.6 94.0 90.2 85.6 91.4 88.3
Table7: PerformancecomparisonofRoBERTabaseandlargemodelsfine-tunedbyRED,RED+andotherPEFT
baselinesontheGLUEbenchmark. RED+denotesanenhancedvariantofREDwheretherepresentationvectorsof
Q,K,andV inattentionblocksarealsomodifiedviarepresentationeditinginadditiontoFFNsub-layers.

### Method #Param BLEU NIST MET ROUGE-L CIDEr

LoRA(medium) 0.79M 67.43 8.65 46.01 69.64 2.42

### RED(medium) 0.05M 64.86 8.36 44.99 67.62 2.28

RED+(medium) 0.25M 66.68 8.53 46.28 69.63 2.38
LoRA(large) 1.47M 68.24 8.76 46.23 69.92 2.42

### RED(large) 0.09M 65.77 8.42 46.12 69.03 2.36


### RED+(large) 0.46M 68.31 8.78 46.12 69.80 2.41

Table8: PerformancecomparisonofGPT-2mediumandlargemodelsfine-tunedbyRED,RED+andotherPEFT
baselinesontheE2ENLGChallenge. RED+denotesanenhancedvariantofREDwheretherepresentationvectors
ofQ,K,andV inattentionblocksarealsomodifiedviarepresentationeditinginadditiontoFFNsub-layers.
Analyzingresultsfromthreedifferentdatasetsfrom ondatasetswithfewertrainingexamples.
the GLUE benchmark, we found that the scaling
operatorboostedaccuracybyanaverageof1.3%, 5.3 ParameterEfficiencyandEfficacy
whilethebiasingoperatorcontributedtoasignifi-

### WhenusingAdaptororLoRAforfine-tuning,the

cant12.4%increaseinaccuracy. Comparedtothe
ranks of their decomposition matrices were typiscaling operator, the addition of a learnable bias
cally set to 8 or 16. These ranks can be reduced
vectortotheoriginalrepresentationplaysamore
to decrease the number of parameters used dursubstantialroleinthefine-tuningofneuralmodels.
ing fine-tuning. To compare RED with the most
parameter-efficientversionsofAdpatororLoRA,
5.2 ImpactofEditingPositions
we adjusted the rank of their decomposition ma-
Themotivationofthisstudyistoexplorethefeasitricesto1. Wethenmadeacomparativeanalysis
bilityoffine-tuninglargelanguagemodelswithas
withGPT-2mediumontheE2ENLGChallenge.
fewparametersaspossible. Therefore,inourcur-
Table 5 shows that RED outperformed all the
rentimplementation,weonlyconsidermodifying
baselinesonfouroutoffivetasks,whileitslightly
the representations produced by FFN sub-layers.
underperformedLoRAbyanegligibledifference
However,itisstillpossibletofurtherimprovethe
of0.02ontheNISTdataset. Itisworthynotingthat
performanceofthemodelbyincreasingthenum-

### REDaccomplishedthiswiththeminimalnumber

ber of trainable parameters if the representation
ofparameters,demonstratingthatREDisnotonly
vectors of Q (query), K (key), and V (value) in
parameter-efficientbutalsoparameter-effective.
attentionblocksareallowedtobemodifiedviarepresentationediting. Todemonstratethispossibility,
6 Conclusion
weconductedadditionalexperimentsinwhichthe
representationsofQ,K,andV werealsomodified. Inthisstudy,weproposedanovelperspectiveon
TheexperimentalresultsreportedinTable7and fine-tuningbyeditingmodelrepresentationsrather
Table8showthattheperformanceofREDhasbeen thanadjustingthemodel’sweights. Throughextenimproved on all these datasets but with slightly siveexperimentationacrossvariousNLPtasksand
moretrainableparameters(increasingfrom0.07M neuralmodelsofvaryingstructuresandscales,we
to0.37M).Itsuggeststhatitisfeasibletoincrease demonstrated that RED can deliver performance
thenumberoftrainableparameterstofurtherboost comparableorsuperiortoexistingPEFTmethods
theperformancebyeditingadditionalfeaturerepre- while employing a minimal number of trainable
sentations. Thisstrategyisparticularlyeffectivefor parameters. Wearehopefulthatthisstudycouldindatasetswithalargernumberoftraininginstances, spirenovelmethodsforfine-tuningLLMs,thereby
suchasMNLI,QNLI,QQP,andE2Ewhiletheper- contributingtotheadvancementofbotheffective
formancedidnotexhibitsignificantimprovement andcomputationallyefficientPEFTtechniques.

<!-- Page 10 -->

Limitations Elad Ben-Zaken, Shauli Ravfogel, and Yoav Goldberg. 2021. Bitfit: Simple parameter-efficient
Wehavedemonstratedtheefficacyofanewpromis- fine-tuningfortransformer-basedmaskedlanguageingPEFTapproachforfine-tuningmodelsthrough models. ArXiv,abs/2106.10199.
directmanipulationofrepresentationsacrossvari-
Tom Brown, Benjamin Mann, Nick Ryder, Melanie
ousNLPtaskswithnetworksofvaryingstructures

### Subbiah,JaredDKaplan,PrafullaDhariwal,Arvind

and scales. It would be intriguing to extend this Neelakantan,PranavShyam,GirishSastry,Amanda
methodtoothermodalities,suchasimage,speech, Askell,etal.2020. Languagemodelsarefew-shot
learners. Advancesinneuralinformationprocessing
andvideo. Recentadvancementsinrepresentation
systems,33:1877–1901.
engineeringhaveindicatedthatonlyaveryfewexamplesaresufficientforachievingprecisecontrol DanielMatthewCer,MonaT.Diab,EnekoAgirre,Iñigo
overthemodel’soutputthroughrepresentationma- Lopez-Gazpio, and Lucia Specia. 2017. Semevalnipulations. WeplantoapplytheproposedREDto 2017task1: Semantictextualsimilaritymultilingual
andcrosslingualfocusedevaluation. InInternational
few-shotscenariosinthefuture.
WorkshoponSemanticEvaluation.

### ReproducibilityStatement

Ganqu Cui, Lifan Yuan, Ning Ding, Guanming Yao,
WeiZhu,YuanNi,GuotongXie,ZhiyuanLiu,and

### Wehavemadeourcodepubliclyaccessibleviaa

MaosongSun.2023. Ultrafeedback: BoostinglanrepositoryonGitHub(github.com/mlwu22/RED). guage models with high-quality feedback. ArXiv,
Tofurtherensurereplicability,wehadacolleague abs/2310.01377.
unfamiliar with our method install and test RED.
Dorottya Demszky, Kelvin Guu, and Percy Liang.

### Theexperimentyieldedresultsnearlyidenticalto


## Transforming question answering datasets

ours,whichstrengthensourconfidencethatother into natural language inference datasets. ArXiv,
researcherswillsuccessfullyexecuteourcodeand abs/1809.02922.
reproduceourfindings.
Tim Dettmers, Artidoro Pagnoni, Ari Holtzman, and
LukeZettlemoyer.2023. Qlora: Efficientfinetuning
ofquantizedllms. ArXiv,abs/2305.14314.

### References

Jacob Devlin, Ming-Wei Chang, Kenton Lee, and

### Armen Aghajanyan, Luke Zettlemoyer, and Sonal

KristinaToutanova.2018. Bert: Pre-trainingofdeep

### Gupta.2020. Intrinsicdimensionalityexplainsthe

bidirectionaltransformersforlanguageunderstandeffectivenessoflanguagemodelfine-tuning. arXiv
ing. arXivpreprintarXiv:1810.04805.
preprintarXiv:2012.13255.
Ning Ding, Xingtai Lv, Qiaosen Wang, Yulin Chen,
AkariAsai,MohammadrezaSalehi,MatthewE.Peters,
BowenZhou,ZhiyuanLiu,andMaosongSun.2023.
andHannanehHajishirzi.2022. Attempt: Parameter-

### Sparselow-rankadaptationofpre-trainedlanguage

efficientmulti-tasktuningviaattentionalmixturesof
models. arXivpreprintarXiv:2311.11696.
softprompts. InConferenceonEmpiricalMethods
inNaturalLanguageProcessing.
NingDing,YujiaQin,GuangYang,FuchaoWei,ZonghanYang,YushengSu,ShengdingHu,YulinChen,
SatanjeevBanerjeeandAlonLavie.2005. Meteor: An

### Chi-MinChan,WeizeChen,etal.2022. Deltatuning:

automatic metric for mt evaluation with improved
correlation with human judgments. In IEEvalua- Acomprehensivestudyofparameterefficientmethtion@ACL. odsforpre-trainedlanguagemodels. arXivpreprint
arXiv:2203.06904.

### Roy Bar-Haim, Ido Dagan, Bill Dolan, Lisa Ferro,

Danilo Giampiccolo, Bernardo Magnini, and Idan WilliamB.DolanandChrisBrockett.2005. Automati-
Szpektor.2006. Thesecondpascalrecognisingtex- callyconstructingacorpusofsententialparaphrases.
tualentailmentchallenge. In International Joint Conference on Natural LanguageProcessing.

### EdwardBeeching,ClémentineFourrier,NathanHabib,

SheonHan,NathanLambert,NazneenRajani,Omar LeoGao,JonathanTow,BaberAbbasi,StellaBiderman,
Sanseviero,LewisTunstall,andThomasWolf.2023. SidBlack,AnthonyDiPofi,CharlesFoster,Laurence
Openllmleaderboard. https://huggingface.co/ Golding,JeffreyHsu,AlainLeNoac’h,HaonanLi,
spaces/HuggingFaceH4/open_llm_leaderboard. KyleMcDonell,NiklasMuennighoff,ChrisOciepa,

### Jason Phang, Laria Reynolds, Hailey Schoelkopf,

AnjaBelzandEhudReiter.2006. Comparingautomatic Aviya Skowron, Lintang Sutawika, Eric Tang, Anandhumanevaluationofnlgsystems. InConference ishThite, BenWang, KevinWang, andAndyZou.
oftheEuropeanChapteroftheAssociationforCom- 2023. A framework for few-shot language model
putationalLinguistics. evaluation.

<!-- Page 11 -->

DemiGuo,AlexanderMRush,andYoonKim.2020. Gunjan Chhablani, Bhavitvya Malik, Simon Bran-
Parameter-efficienttransferlearningwithdiffprun- deis, Teven Le Scao, Victor Sanh, Canwen Xu,
ing. arXivpreprintarXiv:2012.07463. Nicolas Patry, Angelina McMillan-Major, Philipp

### Schmid,SylvainGugger,ClementDelangue,Th’eo

JunxianHe,ChuntingZhou,XuezheMa,TaylorBerg- Matussiere, LysandreDebut, StasBekman, Pierric
Kirkpatrick,andGrahamNeubig.2021. Towardsa Cistac,ThibaultGoehringer,VictorMustar,François
unifiedviewofparameter-efficienttransferlearning. Lagunas, Alexander M. Rush, and Thomas Wolf.
ArXiv,abs/2110.04366. 2021. Datasets: A community library for natural
languageprocessing. ArXiv,abs/2109.02846.

### Dan Hendrycks, Collin Burns, Steven Basart, Andy

Zou, Mantas Mazeika, Dawn Xiaodong Song, and XiangLisaLiandPercyLiang.2021a. Prefix-tuning:
JacobSteinhardt.2020. Measuringmassivemultitask Optimizingcontinuouspromptsforgeneration. arXiv
languageunderstanding. ArXiv,abs/2009.03300. preprintarXiv:2101.00190.
DanHendrycks,CollinBurns,SauravKadavath,Akul XiangLisaLiandPercyLiang.2021b. Prefix-tuning:
Arora, Steven Basart, Eric Tang, Dawn Xiaodong Optimizingcontinuouspromptsforgeneration. Pro-
Song,andJacobSteinhardt.2021. Measuringmath- ceedingsofthe59thAnnualMeetingoftheAssociaematical problem solving with the math dataset. tionforComputationalLinguisticsandthe11thInter-
ArXiv,abs/2103.03874. nationalJointConferenceonNaturalLanguageProcessing(Volume1: LongPapers),abs/2101.00190.
Neil Houlsby, Andrei Giurgiu, Stanislaw Jastrzebski,
Bruna Morrone, Quentin De Laroussilhe, Andrea
XuechenLi,TianyiZhang,YannDubois,RohanTaori,
Gesmundo,MonaAttariyan,andSylvainGelly.2019.

### IshaanGulrajani,CarlosGuestrin,PercyLiang,and


### Parameter-efficienttransferlearningfornlp. InIn-

TatsunoriBHashimoto.2023. Alpacaeval: AnautoternationalConferenceonMachineLearning,pages
maticevaluatorofinstruction-followingmodels.

## 2790–2799.Pmlr.


### Dongze Lian, Daquan Zhou, Jiashi Feng, and Xin-

Edward J Hu, Yelong Shen, Phillip Wallis, Zeyuan
chaoWang.2022. Scaling&shiftingyourfeatures:

### Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang,


### A new baseline for efficient model tuning. ArXiv,

and Weizhu Chen. 2021. Lora: Low-rank adapabs/2210.08823.
tation of large language models. arXiv preprint
arXiv:2106.09685.
Chin-YewLin.2004. Rouge: Apackageforautomatic
evaluationofsummaries. InAnnualMeetingofthe
Menglin Jia, Luming Tang, Bor-Chun Chen, Claire
AssociationforComputationalLinguistics.
Cardie,SergeBelongie,BharathHariharan,andSer-

### Nam Lim. 2022. Visual prompt tuning. In Euro-

StephanieC.Lin,JacobHilton,andOwainEvans.2021.
pean Conference on Computer Vision, pages 709–
Truthfulqa: Measuring how models mimic human

### Springer.

falsehoods. InAnnualMeetingoftheAssociationfor
ComputationalLinguistics.
RabeehKarimiMahabadi, JamesHenderson, andSebastianRuder.2021. Compacter: Efficientlow-rank
HaokunLiu,DerekTam,MohammedMuqeeth,JayMohypercomplex adapter layers. Advances in Neural
hta,TenghaoHuang,MohitBansal,andColinRaffel.
InformationProcessingSystems,34:1022–1035.

## Few-shot parameter-efficient fine-tuning is

betterandcheaperthanin-contextlearning. ArXiv,
Dawid Jan Kopiczko, Tijmen Blankevoort, and
abs/2205.05638.
YukiMarkusAsano.2023. Vera: Vector-basedrandommatrixadaptation. ArXiv,abs/2310.11454.

### WenhaoLiu,XiaohuaWang,MulingWu,TianlongLi,

Jaejun Lee, Raphael Tang, and Jimmy J. Lin. 2019. Changze Lv, Zixuan Ling, Jianhao Zhu, Cenyuan
What would elsa do? freezing layers during trans- Zhang,XiaoqingZheng,andXuanjingHuang.2023.
formerfine-tuning. ArXiv,abs/1911.03090. Aligninglargelanguagemodelswithhumanpreferencesthroughrepresentationengineering.
BrianLester,RamiAl-Rfou,andNoahConstant.2021a.
The power of scale for parameter-efficient prompt YinhanLiu,MyleOtt,NamanGoyal,JingfeiDu,Mantuning. arXivpreprintarXiv:2104.08691. dar Joshi, Danqi Chen, Omer Levy, Mike Lewis,
Luke Zettlemoyer, and Veselin Stoyanov. 2019.
BrianLester,RamiAl-Rfou,andNoahConstant.2021b. Roberta: A robustly optimized bert pretraining ap-
The power of scale for parameter-efficient prompt proach. ArXiv,abs/1907.11692.
tuning. InConferenceonEmpiricalMethodsinNaturalLanguageProcessing. YuningMao,LambertMathias,RuiHou,AmjadAlmahairi,HaoMa,JiaweiHan,WentauYih,andMadian
Quentin Lhoest, Albert Villanova del Moral, Yacine Khabsa. 2021. Unipelt: A unified framework for
Jernite,AbhishekThakur,PatrickvonPlaten,Suraj parameter-efficient language model tuning. In An-
Patil, Julien Chaumond, Mariama Drame, Julien nualMeetingoftheAssociationforComputational
Plu, Lewis Tunstall, Joe Davison, Mario vSavsko, Linguistics.

<!-- Page 12 -->

TodorMihaylov,PeterClark,TusharKhot,andAshish Richard Socher, Alex Perelygin, Jean Wu, Jason
Sabharwal.2018. Canasuitofarmorconductelec- Chuang, Christopher D. Manning, A. Ng, and
tricity? anewdatasetforopenbookquestionanswer- ChristopherPotts.2013. Recursivedeepmodelsfor
ing. InConferenceonEmpiricalMethodsinNatural semanticcompositionalityoverasentimenttreebank.
LanguageProcessing. InConferenceonEmpiricalMethodsinNaturalLanguageProcessing.
JekaterinaNovikova,OndrejDusek,andVerenaRieser.

### AsaCooperSticklandandIainMurray.2019. Bertand


## Thee2edataset: Newchallengesforend-topals: Projectedattentionlayersforefficientadaptaendgeneration. ArXiv,abs/1706.09254.

tion in multi-task learning. In International Conference on Machine Learning, pages 5986–5995.
OpenAI. 2023. GPT-4 technical report. CoRR,

## Pmlr.

abs/2303.08774.
NishantSubramani, NiveditaSuresh, andMatthewE.
LongOuyang,JeffWu,XuJiang,DiogoAlmeida,Car- Peters.2022. Extractinglatentsteeringvectorsfrom
rollL.Wainwright,PamelaMishkin,ChongZhang, pretrainedlanguagemodels. ArXiv,abs/2205.05124.

### SandhiniAgarwal,KatarinaSlama,AlexRay,John

Schulman,JacobHilton,FraserKelton,LukeMiller, Hugo Touvron, Louis Martin, Kevin R. Stone, Peter
Maddie Simens, Amanda Askell, Peter Welinder, Albert, Amjad Almahairi, Yasmine Babaei, Niko-
Paul Christiano, Jan Leike, and Ryan Lowe. 2022. lay Bashlykov, Soumya Batra, Prajjwal Bhargava,
Traininglanguagemodelstofollowinstructionswith ShrutiBhosale,DanielM.Bikel,LukasBlecher,Crishumanfeedback. InProceedingsoftheConference tianCantónFerrer, MoyaChen, GuillemCucurull,
onNeuralInformationProcessingSystems(NeurIPS DavidEsiobu,JudeFernandes,JeremyFu,Wenyin
2022). Fu, Brian Fuller, Cynthia Gao, Vedanuj Goswami,

### NamanGoyal, AnthonyS.Hartshorn, SagharHos-

KishorePapineni,SalimRoukos,ToddWard,andWei- seini,RuiHou,HakanInan,MarcinKardas,Viktor
JingZhu.2002. Bleu: amethodforautomaticevalu- Kerkez,MadianKhabsa,IsabelM.Kloumann,A.V.
ationofmachinetranslation. InAnnualMeetingof Korenev,PunitSinghKoura,Marie-AnneLachaux,
theAssociationforComputationalLinguistics. ThibautLavril,JenyaLee,DianaLiskovich,Yinghai

### Lu,YuningMao,XavierMartinet,TodorMihaylov,

Jonas Pfeiffer, Aishwarya Kamath, Andreas Rücklé, PushkarMishra,IgorMolybog,YixinNie,Andrew
Kyunghyun Cho, and Iryna Gurevych. 2020. Poulton,JeremyReizenstein,RashiRungta,Kalyan
Adapterfusion: Non-destructivetaskcompositionfor Saladi, Alan Schelten, Ruan Silva, Eric Michael
transferlearning. ArXiv,abs/2005.00247. Smith,R.Subramanian,XiaTan,BinhTang,Ross
Taylor, Adina Williams, Jian Xiang Kuan, Puxin

### Xu,ZhengxuYan,IliyanZarov,YuchenZhang,An-

AlecRadford,KarthikNarasimhan,TimSalimans,Ilya
gelaFan,MelanieKambadur,SharanNarang,Aure-
Sutskever, et al. 2018. Improving language underlienRodriguez,RobertStojnic,SergeyEdunov,and
standingbygenerativepre-training.

### ThomasScialom.2023. Llama2: Openfoundation

andfine-tunedchatmodels. ArXiv,abs/2307.09288.
Alec Radford, Jeff Wu, Rewon Child, David Luan,

### DarioAmodei,andIlyaSutskever.2019. Language

Alexander Matt Turner, Lisa Thiergart, David S.
modelsareunsupervisedmultitasklearners.
Udell, Gavin Leech, Ulisse Mini, and Monte Stuart MacDiarmid.2023. Activation addition: Steer-
ColinRaffel,NoamShazeer,AdamRoberts,Katherine ing language models without optimization. ArXiv,
Lee,SharanNarang,MichaelMatena,YanqiZhou, abs/2308.10248.

### WeiLi,andPeterJLiu.2020. Exploringthelimits

oftransferlearningwithaunifiedtext-to-texttrans- AshishVaswani,NoamM.Shazeer,NikiParmar,Jakob
former. TheJournalofMachineLearningResearch, Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz
21(1):5485–5551. Kaiser,andIlliaPolosukhin.2017. Attentionisall
youneed. InNeuralInformationProcessingSystems.
AndreasRücklé,GregorGeigle,MaxGlockner,Tilman
RamakrishnaVedantam,C.LawrenceZitnick,andDevi

### Beck, Jonas Pfeiffer, Nils Reimers, and Iryna

Parikh.2014. Cider:Consensus-basedimagedescrip-
Gurevych. 2020. Adapterdrop: On the efficiency
tionevaluation. 2015IEEEConferenceonComputer
ofadaptersintransformers. InConferenceonEmpir-
VisionandPatternRecognition(CVPR),pages4566–
icalMethodsinNaturalLanguageProcessing.
4575.

### KeisukeSakaguchi,RonanLeBras,ChandraBhagavat-

Alex Wang, Amanpreet Singh, Julian Michael, Felix
ula,andYejinChoi.2019. Anadversarialwinograd
Hill, Omer Levy, and Samuel R. Bowman. 2018.
schemachallengeatscale.
Glue: A multi-task benchmark and analysis platformfornaturallanguageunderstanding. InBlack-
TaylorShin,YasamanRazeghi,RobertLLoganIV,Eric boxNLP@EMNLP.
Wallace,andSameerSingh.2020. Elicitingknowledgefromlanguagemodelsusingautomaticallygen- Zhen Wang, Rameswar Panda, Leonid Karlinsky,
eratedprompts. ArXiv,abs/2010.15980. Rogério Schmidt Feris, Huan Sun, and Yoon Kim.

<!-- Page 13 -->


## Multitask prompt tuning enables parameter- Shashwat Goel, Nathaniel Li, Michael J. Byun,

efficienttransferlearning. ArXiv,abs/2303.02861. Zifan Wang, Alex Mallen, Steven Basart, Sanmi

### Koyejo,DawnSong,MattFredrikson,ZicoKolter,

AlexWarstadt,AmanpreetSingh,andSamuelR.Bow- andDanHendrycks.2023. Representationengineerman.2018. Neuralnetworkacceptabilityjudgments. ing: Atop-downapproachtoaitransparency. ArXiv,
TransactionsoftheAssociationforComputational abs/2310.01405.
Linguistics,7:625–641.
Adina Williams, Nikita Nangia, and Samuel R. Bowman.2017. Abroad-coveragechallengecorpusfor
sentenceunderstandingthroughinference. InNorth
AmericanChapteroftheAssociationforComputationalLinguistics.

### Thomas Wolf, Lysandre Debut, Victor Sanh, Julien

Chaumond,ClementDelangue,AnthonyMoi,PierricCistac,TimRault,RémiLouf,MorganFuntowicz,
andJamieBrew.2019. Huggingface’stransformers:
State-of-the-artnaturallanguageprocessing. ArXiv,
abs/1910.03771.
MulingWu,WenhaoLiu,JianhanXu,ChangzeLv,Zixuan Ling, Tianlong Li, Longtao Huang, Xiaoqing
Zheng,andXuanjingHuang.2023. Parameterefficient multi-task fine-tuning by learning to transfer
token-wise prompts. In Conference on Empirical
MethodsinNaturalLanguageProcessing.
Elad Ben Zaken, Shauli Ravfogel, and Yoav Goldberg. 2021. Bitfit: Simple parameter-efficient
fine-tuningfortransformer-basedmaskedlanguagemodels. arXivpreprintarXiv:2106.10199.

### Rowan Zellers, Ari Holtzman, Yonatan Bisk, Ali

Farhadi,andYejinChoi.2019. Hellaswag:Canamachinereallyfinishyoursentence? InAnnualMeeting
oftheAssociationforComputationalLinguistics.
Qingru Zhang, Minshuo Chen, Alexander Bukharin,

### Pengcheng He, Yu Cheng, Weizhu Chen, and


### Tuo Zhao. 2023a. Adaptive budget allocation

for parameter-efficient fine-tuning. arXiv preprint
arXiv:2303.10512.
QingruZhang,MinshuoChen,AlexanderW.Bukharin,

### Pengcheng He, Yu Cheng, Weizhu Chen, and

Tuo Zhao. 2023b. Adaptive budget allocation for parameter-efficient fine-tuning. ArXiv,
abs/2303.10512.
Mengjie Zhao, Tao Lin, Martin Jaggi, and Hinrich

### Schütze.2020. Maskingasanefficientalternativeto

finetuningforpretrainedlanguagemodels. InConferenceonEmpiricalMethodsinNaturalLanguage
Processing.

### LianminZheng,Wei-LinChiang,YingSheng,Siyuan


### Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin,


### Zhuohan Li, Dacheng Li, Eric P. Xing, Haotong

Zhang,JosephGonzalez,andIonStoica.2023. Judgingllm-as-a-judgewithmt-benchandchatbotarena.
ArXiv,abs/2306.05685.
AndyZou,LongPhan,SarahChen,JamesCampbell,

### PhillipGuo,RichardRen,AlexanderPan,Xuwang

Yin, Mantas Mazeika, Ann-Kathrin Dombrowski,

<!-- Page 14 -->

A Datasets Dataset #Train #Validation #Test Metric

### CoLA 8.5K 522 521 MCC

A.1 GLUEBenchmark SST-2 67K 436 436 ACC

## Mrpc 3.7K 204 204 Acc

TheGeneralLanguageUnderstandingEvaluation QQP 364K 1K 39K ACC
(GLUE)benchmarkcomprisesavarietyofdatasets, STS-B 5.7K 750 750 CORR

## Mnli 393K 1K 8K Acc

including CoLA (Warstadt et al., 2018), SST-2

## Qnli 105K 1K 4.5K Acc

(Socher et al., 2013), MRPC (Dolan and Brock- RTE 2.5K 139 138 ACC
ett,2005), QQP(Wangetal.,2018), STS-B(Cer
Table9: Thesizesofthetraining,validation,andtest
etal.,2017),MNLI(Williamsetal.,2017),QNLI
sets, along with their corresponding metrics for all
(Demszkyetal.,2018),andRTE(Bar-Haimetal.,
datasetsintheGLUEbenchmark. “MCC”,“ACC”and
2006). These datasets have been widely-used to
“CORR”denoteMatthewscorrelationcoefficient,accumeasuretheperformanceoflanguageunderstand- racy,andPearsoncorrelationcoefficientrespectively.
ing models. The GLUE benchmark was sourced
from Huggingface Datasets (Lhoest et al., 2021), Thisbenchmarkincludes42.1Ktraininginstances,
and all datasets within this benchmark were em- 4.67K validation instances, and 4.69K testing inployedforourevaluation. stances. Following previous studies, we used the
Following (Ding et al., 2023) and (Hu et al., official evaluation script to compute BLEU (Pap-
2021),weevaluatedmodelstrainedwithdifferent inenietal.,2002),NIST(BelzandReiter,2006),
PEFTmethodsonthevalidationdataset. Toensure METEOR (Banerjee and Lavie, 2005), ROUGE-
afairandsystematiccomparisonofdifferentPEFT L(Lin,2004)andCIDEr(Vedantametal.,2014)
methods, we randomly sampled 1,000 instances scores. For evaluations using GPT-2, we ran exfrom the validation set to form a new validation periment for 3 times using distinct random seeds
setifthevalidationsetcontainsmorethan2,000 andreportedtheaverageresults. Therandomseeds
instances(otherwise,werandomlyselectedhalfof usedfortheseexperimentswere42,43,and44.
the instances for the new validation set), and the
remaininginstanceswereusedasthetestset. This A.3 UltraFeedback
allowedustoadhererigorouslytotheestablished UltraFeedback(Cuietal.,2023)comprises64,000
trainingprotocol,whichinvolvesevaluatingonthe prompts,eachofthemaccompaniedbyfourLLM
newvalidationsetaftereachepochoftrainingand responses evaluated by GPT-4 based on criteria
selectingthecheckpointthatyieldsthebestperfor- such as instruction-following, honesty, and helpmanceonthevalidationsetasthefinalmodelfor fulness. ToconstructthetrainingdatasetfromUltestingonthetestset. Thesizesofthetraining,val- traFeedback, we selected the responses with the
idation,andtestsetsaswellastheircorresponding highestmeanscores3.
metricsforalldatasetsaregiveninTable9.
ForalltheexperimentswithRoBERTa,weran A.4 OpenLLMLeaderboard
experiment 5 times for each PEFT method using

### TheOpenLLMLeaderboardincludessixdatasets

distinct random seeds to initialize the trainable
thatassessvariouscapabilitiessuchassciencequesweights and reported the average results. During
tions,commonsenseinference,multitaskaccuracy,
theevaluationoftheRTEandCoLAdatasets,some
mathematical reasoning, and the truthfulness of
researchers reported that specific random seeds
generatedanswers. ItconsistsofARC(Mihaylov
couldpotentiallyleadtoanomalousexperimental
et al., 2018), HellaSwag (Zellers et al., 2019),
outcomes2. Therefore, we randomly chose other

### WinoGrande (Sakaguchi et al., 2019), MMLU

fivedifferentrandomseeds(i.e.,42,43,44,45,and
(Hendrycks et al., 2020), TruthfulQA (Lin et al.,
46)toconducttheexperiments.
2021),andGSM8K(Hendrycksetal.,2021). We
usedtheEleutherAILanguageModelEvaluation

### A.2 E2ENLGChallenge


### Harnesslibrary(Gaoetal.,2023)toevaluatelan-

The E2E NLG Challenge was first introduced by
guagemodelstrainedusingvariousmethods. Table

### Novikovaetal.(2017)totrainandevaluateend-to-

11detailstheleaderboardevaluationconfiguration
end,data-drivennaturallanguagegenerationmodandtheexperimentalsettingsappliedinthisstudy.
elsandsystems. AlldatasetsintheE2ENLGChallenge were sourced from Huggingface Datasets. 3Theconstructeddatasetcanbeaccessedat:
huggingface.co/datasets/argilla/
2Refertogithub.com/microsoft/LoRA/issues. \ultrafeedback-binarized-preferences-cleaned.

<!-- Page 15 -->

A.5 AlpacaEval length across all baseline methods. The hyperparametersusedforLLaMA-2arelistedinTable10.

### AlpacaEvalisanautomatedevaluationbenchmark

WeevaluatedtheperformanceofmodelsonTruthforLLMs,employingGPT-4(OpenAI,2023)asan
fulQAaftereachtrainingepoch,andthecheckpoint
annotator to compare the responses generated by
demonstratingthebestperformancewasselected
themodelsagainstreferenceanswersproducedby
forfinaltestingonotherdatasets. Agreedydecodtext-davinci-003. Thebenchmarkconsistsof805
ingstrategywasemployedforgenerationforallthe
samples focused on simple instruction-following
models. Tomitigaterepetitionissues,weapplied
tasks. Previous research has shown a high cora repetition penalty of 1.1 and set the no-repeat
relationbetweenGPT-4’sannotationsandhuman
n-gramsizeto5.
evaluatorassessments(Lietal.,2023).

### C ResultsofStandardDeviations

A.6 MT-Bench Wepresentedtheaverageresultsinthemaintext.
MT-Bench(Zhengetal.,2023)comprises80chal- To provide a quantifiable measure of uncertainty
lenging questions, each structured as a two-turn in the measurement or prediction and help other
dialogue. GPT-4wasalsousedtoevaluatethere- researchersreplicateourexperiments,wealsoresponsesgeneratedbythemodels,assigningascore portedthestandarddeviationswithRoBERTamodfrom1to10foreachturn. elsontheGLUEbenchmarkinTable17,andthe
standarddeviationswithGPT-2ontheE2ENLG
B Hyperparameters ChallengeinTable18.
D AdditionalResultswithLLaMA-2

### B.1 ExperimentswithRoBERTa

Example responses generated by models trained

### WetrainedthemodelsusingAdamWwithalinear

with RAD, full-parameter fine-tuning (FT) and
learningratedecayschedule. Toensureafaircom-
LoRA are presented in Figures 3 and 4. Tables
parison,wemaintainedthesamesequencelength
19and12providetheresultsontheMT-Benchand
across all baseline PEFT methods. The hyperpa-
OpenLLMLeaderboardrespectively.
rameters used in our experiments for RoBERTa

### Method Hyperparameter Value

base are detailed in Table 13, and for RoBERTa

### BatchSize 128

largeinTable15. MicroBatchSize 2
Optimizer Adamw

## All

B.2 ExperimentswithGPT-2 LRSchedulerType Cosine

### WarmupRatio 0.1

WetrainedthemodelsusingAdamWwithalinear MaximumSequenceLength 768

### LearningRate 2e−5

learningratedecayschedule. Toensureafaircom- FT

### NumberofEpochs 3

parison,wemaintainedthesamesequencelength

### LearningRate 3e−4

across all baseline PEFT methods. We used the NumberofEpochs 3

### LoRA BatchSize 128

HuggingfacePEFTpackagetoreplicatePrefixTun-

### Coefficientα 16

ingandLoRA,andtheOpenDeltapackagetorepli- Dropout 0.1
cateAdapterandAdapter-FFN.Thehyperparam- Rank 16

### LearningRate 1e−3

etersusedinourexperimentsforGPT-2medium RED

### NumberofEpochs 10

andGPT-2largearedetailedinTable16s.
Table10: HyperparametersusedfortrainingLLaMA-2.

### B.3 ExperimentswithT5

Dataset #Few-shot Metric

## Arc 25 Acc-Norm

WetrainedthemodelsusingAdamWwithalinear

### TruthfulQA 0 MC2

learning rate decay. We conducted experiments Winogrande 5 ACC
on T5 following the settings established by Asai GSM8K 5 ACC

### HellaSwag 10 ACC-NORM

et al. (2022). The hyperparameters used in our

## Mmlu 10 Acc

experimentsforT5basearedetailedinTable14.

### Table 11: Number of few-shot examples and metrics

used for evaluation on the datasets in the Open LLM

### B.4 ExperimentswithLLaMA-2


### Leaderboard. “MC2”denotesthenormalizedtotalprob-

WeemployedAdamWwithacosinelearningrate abilityassignedtothesetoftrueanswers,and“ACC-
decayscheduleduringthefine-tuning. Toensurea NORM”denotesthenormalizedaccuracyusedinsetfaircomparison,wemaintainedthesamesequence tingswhereresponselengthscanvarysignificantly.

<!-- Page 16 -->

Method #Param ARC TruthfulQA Winogrande GSM8k HellaSwag MMLU Average

## Ft 6739M 73.34 47.07 74.03 16.22 79.95 46.55 56.19

LoRA 8.39M 72.07 44.84 75.85 15.01 78.60 44.42 55.13

## Red 0.26M 72.04 47.59 72.85 11.90 77.86 42.27 54.09

Table12: ResultsachievedbyRED,LoRAandfull-parameterfine-tuning(FT)ontheOpenLLMLeaderboard.
Method Dataset MNLI SST-2 MRPC CoLA QNLI QQP RTE STS-B
Optimizer AdamW

## All


### LRSchedule Linear


### BatchSize 32 32 32 32 32 32 32 32


### NumberofEpochs 20 40 40 40 20 20 40 40

FT LearningRate 1e−05 1e−05 1e−05 1e−05 1e−05 1e−05 1e−05 1e−05
WarmupRatio 6e−02 6e−02 6e−02 6e−02 6e−02 6e−02 6e−02 6e−02

### WeightDecay 1e−04


### MaximumSequenceLength 256


### BatchSize 32 32 32 32 32 32 32 32


### NumberofEpochs 20 40 40 40 20 20 40 40

LoRA LearningRate 5e−04 5e−04 4e−04 4e−04 4e−04 5e−04 5e−04 4e−04
WarmupRatio 6e−02 6e−02 6e−02 6e−02 6e−02 6e−02 6e−02 6e−02

### Rank 8


### Coefficientα 8


### MaximumSequenceLength 256


### BatchSize 32 32 32 32 32 32 32 32


### NumberofEpochs 20 40 40 40 20 20 40 40

Adapter LearningRate 1e−04 1e−04 1e−04 1e−04 1e−04 1e−04 1e−04 1e−04
WarmupRatio 6e−02 6e−02 6e−02 6e−02 6e−02 6e−02 6e−02 6e−02

### Rank 8


### MaximumSequenceLength 256


### BatchSize 32 32 32 32 32 32 32 32


### NumberfoEpochs 20 40 40 40 20 20 40 40

Adapter-FFN LearningRate 1e−04 1e−04 1e−04 1e−04 1e−04 1e−04 1e−04 1e−04
WarmupRatio 6e−02 6e−02 6e−02 6e−02 6e−02 6e−02 6e−02 6e−02

### Rank 16


### MaximumSequenceLength 256


### BatchSize 32 32 32 32 32 32 32 32


### NumberofEpochs 20 40 40 40 20 20 40 40

BitFit LearningRate 1e−04 1e−04 1e−04 1e−04 1e−04 1e−04 1e−04 1e−04
WarmupRatio 6e−02 6e−02 6e−02 6e−02 6e−02 6e−02 6e−02 6e−02

### MaximumSequenceLength 256


### BatchSize 32 32 32 32 32 32 32 32


### NumberofEpochs 20 40 40 40 20 20 40 40

RED Learningrate 1e−03 1e−03 5e−03 5e−03 3e−03 1e−03 8e−03 3e−03
WarmupRatio 6e−02 6e−02 6e−02 6e−02 6e−02 6e−02 6e−02 6e−02

### MaximumSequenceLength 256

Table13: HyperparametervaluesfortrainingRoBERTabaseontheGLUEbenchmark.
Method Dataset MNLI SST-2 MRPC CoLA QNLI QQP RTE STS-B
Optimizer AdamW

## All


### LRSchedule Linear


### BatchSize 32 32 32 32 32 32 32 32


### NumberofEpochs 10 10 20 60 10 10 30 50

RED Learningrate 5e−02 3e−02 1e−01 4e−02 2e−02 5e−03 7e−02 4e−02
WarmupRatio 1e−02 6e−02 1e−02 1e−02 0e−00 1e−02 1e−02 6e−02

### MaximumSequenceLengt 256

Table14: HyperparametervaluesfortrainingT5baseontheGLUEbenchmark.

<!-- Page 17 -->

Method Dataset MNLI SST-2 MRPC CoLA QNLI QQP RTE STS-B
Optimizer AdamW

## All


### LRSchedule Linear


### BatchSize 16 32 32 32 16 16 16 32


### NumberofEpochs 10 10 20 20 10 10 20 10

FT Learningrate 2e−05 2e−05 2e−05 2e−05 2e−05 1e−05 1e−05 2e−05
WarmupRatio 6e−02 6e−02 6e−02 6e−02 6e−02 6e−02 6e−02 6e−02

### WeightDecay 1e−01


### MaximumSequenceLength 256


### BatchSize 32 32 32 32 32 32 32 32


### NumberofEpochs 10 10 20 20 10 10 20 10

LoRA Learningrate 3e−04 4e−04 3e−04 2e−04 2e−04 3e−04 4e−04 2e−04
WarmupRatio 6e−02 6e−02 6e−02 6e−02 6e−02 6e−02 6e−02 6e−02

### Rank 8


### Coefficientα 16


### MaximumSequenceLength 256


### BatchSize 32 32 32 32 32 32 32 32


### NumberofEpochs 10 10 20 20 10 10 20 10

Adapter Learningrate 3e−04 3e−04 3e−04 3e−04 3e−04 3e−04 3e−04 3e−04
WarmupRatio 6e−02 6e−02 6e−02 6e−02 6e−02 6e−02 6e−02 6e−02

### Rank 8


### MaximumSequenceLength 256


### BatchSize 32 32 32 32 32 32 32 32


### NumberofEpochs 10 10 20 20 10 10 20 10

Adapter-FFN Learningrate 3e−04 3e−04 3e−04 3e−04 3e−04 3e−04 3e−04 3e−04
WarmupRatio 6e−02 6e−02 6e−02 6e−02 6e−02 6e−02 6e−02 6e−02

### Rank 16


### MaximumSequenceLength 256


### BatchSize 32 32 32 32 32 32 32 32


### NumberofEpochs 10 10 20 20 10 10 20 10

RED Learningrate 1e−03 1e−03 2e−03 1e−03 1e−03 1e−03 5e−03 5e−03

### WeightDecay 0.0 0.0 0.0 0.0 0.0 0.0 1e−04 0.0

WarmupRatio 6e−02 6e−02 0 6e−02 6e−02 6e−02 1e−02 6e−02

### MaximumSequenceLength 256

Table15: HyperparametervaluesfortrainingRoBERTalargeontheGLUEbenchmark.
Dataset FT FTtop2 Adapter Apapter-FFN LoRA PrefixTuning RED(medium) RED(large)

### Training


### Optimizer AdamW

WeightDecay 0.0 0.0 0.0 0.0 1e−02 0.0 1e−04 0.0
NumberofEpochs 5 5 5 5 5 5 5 10

### LearningRateSchedule Linear


### LabelSmooth 0.0 0.0 0.0 0.0 0.1 0.0 0.0 0.0

LearningRate 5e−05 5e−05 8e−05 8e−05 2e−04 8e−05 6e−02 6e−03
RankorPrefixLength −− −− 8 16 8 16 −− −−
Coefficientα −− −− −− −− 32 −− −− −−
Adaption −− −− −− −− 8 −− −− −−
WarmupSteps 500
BatchSize 10

### Inference


### BeamSize 10


### LengthPenalty 0.9


### No-repeatn-gramSize 4

Table16: HyperparametervaluesfortrainingGPT-2ontheE2ENLGChallenge. “RED(medium)”denotesthe
valuesofhyperparametersusedbyREDtofine-tuneGPT-2mediumand“RED(large)”thevaluestoGPT-2large.

<!-- Page 18 -->

Methods #Param MNLI SST-2 MRPC CoLA QNLI QQP RTE STS-B Avg.
FT(base) 125M87.3 94.4 87.9 62.4 92.5 91.7 78.3 90.6 85.6
±0.34 ±0.96 ±0.91 ±3.29 ±0.22 ±0.19 ±3.20 ±0.59
Adapter(base) 0.4M87.0 93.3 88.4 60.9 92.5 90.5 76.6 90.5 85.0
±0.28 ±0.40 ±1.54 ±3.09 ±0.02 ±0.08 ±2.26 ±0.35
Adapter-FFN(base) 0.3M87.1 93.0 88.8 58.5 92.1 90.2 77.7 90.4 84.7
±0.10 ±0.50 ±1.38 ±1.69 ±0.28 ±0.07 ±1.93 ±0.31
LoRA(base) 0.3M86.6 93.9 88.7 59.7 92.6 90.4 75.3 90.3 84.7
±0.26 ±0.49 ±0.76 ±4.36 ±0.10 ±0.08 ±2.79 ±0.54
BitFit(base) 0.1M84.7 94.0 88.1 54.0 91.0 87.3 69.8 89.5 82.3
±0.08 ±0.87 ±1.57 ±3.07 ±0.05 ±0.02 ±1.51 ±0.35
RED(base) 0.02M83.9 93.9 89.2 61.0 90.7 87.2 78.0 90.4 84.7
±0.14 ±0.31 ±0.98 ±2.96 ±0.35 ±0.17 ±2.06 ±0.32
FT(large) 355M88.8 96.0 91.7 68.2 93.8 91.5 85.8 92.6 88.5
±0.45 ±0.66 ±1.73 ±2.62 ±0.33 ±1.28 ±1.40 ±0.16
LoRA(large) 0.8M90.2 96.0 89.8 65.5 94.7 90.7 86.3 91.7 88.1
±0.25 ±0.85 ±2.09 ±2.02 ±0.21 ±0.91 ±2.41 ±0.44
Adapter(large) 0.9M90.1 95.2 90.5 65.4 94.6 91.4 85.3 91.5 88.0
±0.12 ±0.48 ±0.59 ±2.24 ±0.17 ±0.13 ±1.34 ±0.33
Adapter-FFN(large) 0.8M90.3 96.1 90.5 64.4 94.3 91.3 84.8 90.2 87.7
±0.15 ±0.75 ±1.26 ±1.56 ±0.39 ±0.24 ±2.01 ±0.24
RED(large) 0.05M89.5 96.0 90.3 68.1 93.5 88.8 86.2 91.3 87.9
±0.38 ±0.48 ±1.40 ±1.69 ±0.33 ±0.11 ±1.40 ±0.21
Table17:PerformancecomparisonofRoBERTabaseandlargemodelsfine-tunedbyREDandotherPEFTbaselines
ontheGLUEbenchmark.

### Method #Param BLEU NIST MET ROUGE-L CIDEr

FT(medium) 355M 65.95 8.52 45.95 69.13 2.35
±0.26 ±0.03 ±0.07 ±0.30 ±0.01
FTtop2(medium) 25.2M 65.94 8.53 44.28 68.83 2.23
±0.33 ±0.03 ±0.09 ±0.17 ±0.02
Adapter(medium) 0.9M 64.31 8.29 44.91 67.72 2.28
±0.17 ±0.01 ±0.29 ±0.26 ±0.01
Adapter-FFN(medium) 0.8M 64.41 8.30 44.74 67.53 2.29
±0.17 ±0.02 ±0.11 ±0.02 ±0.01
LoRA(medium) 0.8M 67.43 8.65 46.01 69.64 2.42
±0.39 ±0.05 ±0.07 ±0.14 ±0.01
PrefixTuning(medium) 0.8M 63.92 8.26 41.81 66.86 2.03
±0.27 ±0.11 ±0.62 ±0.22 ±0.05
RED(medium) 0.05M 64.86 8.36 44.99 67.62 2.28
±0.40 ±0.03 ±0.02 ±0.22 ±0.01
FT(large) 774M 65.56 8.50 45.40 68.38 2.27
±0.47 ±0.05 ±0.29 ±0.23 ±0.02
Adapter(large) 1.8M 65.94 8.46 45.78 68.65 2.34
±0.35 ±0.05 ±0.11 ±0.35 ±0.01
Adapter-FFN(large) 1.5M 65.53 8.41 45.65 68.46 2.33
±0.61 ±0.07 ±0.12 ±0.16 ±0.01
LoRA(large) 1.5M 68.24 8.76 46.23 69.92 2.42
±0.28 ±0.04 ±0.04 ±0.16 ±0.01
PrefixTuning(large) 1.5M 65.50 8.45 43.97 67.32 2.23
±0.63 ±0.05 ±0.21 ±0.38 ±0.02
RED(large) 0.09M 65.77 8.42 46.12 69.03 2.36
±0.48 ±0.06 ±0.10 ±0.09 ±0.02
Table18:PerformancecomparisonofGPT-2mediumandlargemodelsfine-tunedbyREDandotherPEFTbaselines
ontheE2ENLGChallenge.
Method #Param Writing Roleplay Reasoning Math Coding Extraction Stem Humanities Average

### Turn-1

FT 6739M 9.111 6.500 4.778 1.444 2.700 4.800 7.944 8.833 5.688
LoRA 8.39M 8.600 7.900 4.000 1.600 2.350 4.750 8.700 8.950 5.856
RED 0.26M 8.778 7.278 4.875 1.300 2.625 4.125 7.400 9.167 5.732

### Turn-2

FT 6739M 1.667 5.938 2.222 1.700 2.000 2.111 3.200 5.300 3.021
LoRA 8.39M 1.900 5.800 2.100 1.600 2.550 1.222 3.100 5.500 2.994
RED 0.26M 1.375 5.500 2.444 1.444 2.125 1.750 3.000 5.875 2.946

### Average

FT 6739M 5.389 6.200 3.500 1.579 2.412 3.526 5.447 6.974 4.354
LoRA 8.39M 5.250 6.850 3.050 1.600 2.450 3.079 5.900 7.225 4.434
RED 0.26M 5.294 6.389 3.588 1.368 2.375 2.938 5.750 7.618 4.401
Table19: PerformancecomparisonofLLaMA-2fine-tunedbyREDandotherPEFTbaselinesontheMT-Bench.

<!-- Page 19 -->

Prompt Can you help me figure out how to sew a button on a shirt?
FT 1.Gatherthematerialsneededforsewingabutton,whichincludethread,needle,andbutton.

### Threadtheneedlewiththedesiredcolorofthread.


### Placethebuttonthroughtheholeintheshirtwhereitismissingorneedsreplacing.


### Holdingthebuttoninplace,threadtheneedlethroughthefabricfromthebacksideoftheshirt.


### Pullthethreadtightlytosecurethebuttoninplace.


### Cutoffanyexcessthread.


### Sewthebuttonontotheshirtbyhandorusingasewingmachine.


### Irontheshirttosmoothoutanycreasescausedduringthesewingprocess.


## Enjoyyournewlyrepairedshirt!

LoRA 1. Gather the necessary materials: You will need a shirt, thread, a needle, and a button. If your
shirthas abuttonhole, youcanusethat; otherwise, you'llhave tocreateoneusingabuttonhole
templateorapattern.

## Markthelocationofthebuttonhole:Useamarkerorchalktomarkthelocationwhereyouwant

toplacethebuttonhole.Thisshouldbecenteredonthefrontoftheshirt,justbelowthecollar.

### Createthebuttonhole:Ifyoudon'thaveabuttonholealready,you'llneedtomakeone.Todo

this,foldthefabricoversothatitformsatriangleshape.Then,usearulerandapenciltodrawa
linealongtheedgeofthetriangle.Cutalongthislinewithscissors.

## Sewthebuttonhole:Threadtheneedlewiththethreadandinserttheneedlethroughthefabric

atthetopofthebuttonhole.Pullthethreadtightlytocreateasmallholeinthefabric.Continue
sewing around the perimeter of the buttonhole, leaving about an inch of thread unsewn at the
bottom.

### Insertthebutton:Placethebuttonontheshirt,right-sideup,withtheholefacingdown.Line

upthebuttonholewiththeholeinthebuttonandpushthebuttonthroughthebuttonhole.

## Tieoffthethread:Oncethebuttonissecurelyattached,tieoffthethreadbyknottingitnearthe

beginningofthebuttonholestitching.Trimanyexcessthread.

## Finish thebuttonhole: Foldthefabric overthebuttonholeandpress it flat with aniron. This

willhelptosecurethebuttonandpreventitfromcomingloose.

## Repeatforadditionalbuttons:Ifyouneedtoaddmorebuttons,repeatsteps4-7foreachnew

button.

### Testfit:Tryontheshirttoensurethatthebuttonsareevenlyspacedandthattheylookgood.

Adjustasneeded.

## Enjoyyournewlybuttonedshirt!

RED 1. Gather the necessary materials: You will need a shirt, thread, a needle, and a button. If your
shirthasbuttonsthatarealreadymissingordamaged,youcanpurchasereplacementbuttonsat
mostcraftstores.

### Preparetheshirt:Laytheshirtflatwiththebackfacingupwards.Makesuretheareawhereyou

wanttosewthebuttoniscleanandfreeofanydebrisorwrinkles.

## Threadtheneedle:Insertoneendofthethreadintotheeyeoftheneedleandpullitthrough

theotherside.Tieaknotintheendofthethreadtosecureit.

## Placethebuttonontheshirt:Positionthebuttononthedesiredlocationontheshirt,making

sureit'scenteredandalignedproperly.

## Sewthebutton:Holdingtheshirtsteadywithonehand,usetheotherhandtoguidetheneedle

through the fabric from the backside of the shirt. Inject the thread into the fabric by pushing
down gently with your thumb while pulling the needle through. Continue sewing around the
perimeterofthebutton,makingsuretokeepthestitchesevenandconsistent.

## Trim the excess thread: Once you have finished sewing the button, cut off any excess thread

thatextendsbeyondtheedgeofthebutton.

## Test the button: Try fastening the button onto the shirt to make sure it's securely attached. If

needed,adjustthepositionofthebuttonorre-sewifit'snotproperlyattached.

## Repeatforadditionalbuttons:Iftherearemultiplebuttonsontheshirtthatneedtobesewn,

repeatsteps1-7foreachbutton.

## Cleanup:Aftercompletingallthebuttons,carefullyremoveanyloosethreadsorlintfromthe

shirt.
Remember to always use caution when handling sharp objects like needlesand thread. Always
wearprotectiveglovesandfollowpropersafetyprecautionstoavoidinjury.
Figure 3: The model fine-tuned with RED generates a thorough, sequential guide that offers accurate details,
facilitating comprehension even for novices. This guide encompasses elements such as preparation, threading,
positioning,sewingtechniques,andpost-sewingcleanup,whilealsoprovidingsafetyadviceandpromotingtesting
forsecureattachment. Incontrast,theLoRA-trainedresponseinaccuratelyconcentratesonbuttonholecreation
ratherthanbuttonsewing,potentiallyleadingtoconfusionforindividualsseekingbuttonattachmentguidance. The
responsegeneratedbythefull-parametertrainedmodelpresentsasimplifiedsummary,butitlacksthein-depth
explanationandprecisionofRED,renderingitlessinformativeforthoseunfamiliarwiththesewingprocess.

<!-- Page 20 -->

Prompt Hi,mycatjustchewedonasmallweedoutsidethatlookedlikehairybittercress.

### Couldyoucheckifthisistoxicforcats?

Pleasealsolookforplantsfromthesamefamily,asI'mnot100%sureIidentifieditcorrectly.
FT Hello! I'm here to help answer your question about whether or not the plant your cat
chewedonistoxicforthem.However,beforeIcanprovideanaccurateresponse,Ineedmore
information about the plant in question. Could you please describe the plant in detail,
including its appearance, size, and any unique characteristics it may have? Additionally,
couldyoutellmewhatpartoftheplantyourcatingested(e.g.,leaves,stems,flowers)?This
willhelpmeidentifythecorrectplantanddetermineifitissafeorharmfulforcats.
AsaresponsibleAIassistant,IwanttoensurethatIprovideaccurateandhelpfulinformation
whileprioritizingthesafetyandwell-beingofbothyouandyourfurryfriend.So,pleasetake
amomenttoshareanyadditionaldetailsyoucanabouttheplantyourcathaschewedon,and
I'lldomybesttoassistyou.
LoRA Hello! I'm here to help answer your question about whether or not the plant your cat
chewedonistoxicforthem.However,beforeIcanprovideanaccurateresponse,Ineedsome
moreinformation.Canyoupleasetellmewhatkindofplantitwasandwhereitwasfound?
This will help me identify the species and determine if it's safe for cats to consume.
Additionally,Iwouldappreciateitifyoucouldprovideanyotherdetailsyouhaveaboutthe
plant, such as its appearance, smell, and location. Thank you for your patience and
understanding!
RED Hello! I'm here to help you with your question about whether or not your cat has eaten
something potentially harmful. As an AI language model, I can provide information and
resourcesbasedonthebestavailableevidence.However,it'simportanttonotethatIamnota
veterinarian and cannot diagnose or treat any medical conditions in animals. If you have
concernsaboutyourpet'shealth,pleaseconsultalicensedveterinarian.
Now,let'sfocusonyourspecificquestion.Basedonwhatyoudescribed,itsoundslikeyour
catmayhaveeatensometypeofplantmaterial.It'salwaysagoodideatokeepaneyeonyour
petaftertheyeatsomethingnew,especiallyifit'saplant.Somecommonsignsofpoisoning
in cats include vomiting, diarrhea, drooling, lethargy, weakness, seizures, and difficulty
breathing. If you notice any of these symptoms, it's essential to seek immediate veterinary
care.
As forthe plantitself, it'sdifficultto identify without moredetails. Bittercress (Ranunculus
spp.) is a genus of flowering plants that includes several species, including buttercup,
crowfoot, and spearwort. These plants are generally considered safe for cats, but there are
other members of the Ranunculaceae family that could be toxic, such as aconite (Aconitum
spp.),monkshood(Aconitellaspp.),andwolfsbane(Aconitine).
Tobeonthesafeside,Irecommendtakingyourcattothevetforathoroughexaminationand
possible testing if necessary. The vet will be able to determine if the plant your cat ate was
indeedtoxicandprovideappropriatetreatmentifneeded.Theymayalsoadviseyouonhow
topreventfutureexposuretopotentiallyharmfulplants.
Inconclusion,whilemostplantsaresafeforcatstoconsume,it'salwaysbettertoerronthe
side of caution and seek professional advice when in doubt. Please take your cat to the
veterinarianforaproperevaluationandfollowtheirinstructionsaccordingly.
Figure4: Themodelfine-tunedusingREDgeneratesacomprehensiveandproactivestrategy,addressingimmediate
issues, potentialsymptomstomonitor, andthesignificanceofveterinaryconsultation. Itoffersanoverarching
safetyevaluationoftheRanunculaceaefamily,indicatingpotentiallytoxicmembersandhighlightingthenecessity
forprofessionalassessment. Thisresponsestrikesabalancebetweeninformativecontentandpracticalguidance,
empoweringpetownerstoactintheirpet’sbestinterests,evenintheabsenceofspecificplantidentification. In
contrast,theresponsesproducedbythemodelstrainedwithfullparametersandLoRAplaceagreateremphasis
oncollectingfurtherinformationbeforeofferingadvice,whichcouldinadvertentlypostponecriticalcareinan
emergentsituation.

## Tables

**Table (Page 5):**

|  | #Param | MNLI SST-2 MRPC CoLA QNLI QQP RTE STS-B |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|
|  | 125M 0.4M 0.3M 0.3M 0.1M 0.06M | 87.3 94.4 87.9 62.4 92.5 91.7 78.3 90.6 87.0 93.3 88.4 60.9 92.5 90.5 76.5 90.5 86.6 93.9 88.7 59.7 92.6 90.4 75.3 90.3 87.1 93.0 88.8 58.5 92.0 90.2 77.7 90.4 84.7 94.0 88.1 54.0 91.0 87.3 69.8 89.5 85.4 93.4 86.4 57.8 91.1 88.5 73.5 88.5 |  |  |  |  |  |  |  |  |
| RED(base) | 0.02M | 83.9 | 93.9 | 89.2 | 61.0 | 90.7 | 87.2 | 78.0 | 90.4 | 84.3 |
|  | 355M 0.9M 0.8M 0.8M 0.15M | 88.8 96.0 91.7 68.2 93.8 91.5 85.8 92.6 90.1 95.2 90.5 65.4 94.6 91.4 85.3 91.5 90.2 96.0 89.8 65.5 94.7 90.7 86.3 91.7 90.3 96.1 90.5 64.4 94.3 91.3 84.8 90.2 90.1 94.5 87.1 63.2 93.9 89.3 85.3 91.5 |  |  |  |  |  |  |  |  |
| RED(large) | 0.05M | 89.5 | 96.0 | 90.3 | 68.1 | 93.5 | 88.8 | 86.2 | 91.3 | 87.9 |


**Table (Page 5):**

|  | #Param |  |  |  |  |  |
|---|---|---|---|---|---|---|
|  | 355M 25.2M |  |  |  |  |  |
|  | 0.9M 0.8M 0.8M 0.8M 0.17M |  |  |  |  |  |
| RED(medium) | 0.05M | 64.86 | 8.36 | 44.99 | 67.62 | 2.28 |
|  | 774M 1.8M 1.5M 1.5M 1.5M 0.32M |  |  |  |  |  |
| RED(large) | 0.09M | 65.77 | 8.42 | 46.12 | 69.03 | 2.36 |


**Table (Page 6):**

|  | #Param | MNLI SST-2 MRPC CoLA QNLI QQP RTE STS-B |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|
|  | 220M 1.9M 1.1M 0.3M 0.08M | 86.8 94.6 90.2 61.8 93.0 91.6 71.9 89.7 86.5 93.8 85.3 64.0 93.2 90.2 71.9 90.7 86.3 93.6 86.3 62.7 93.2 90.2 71.2 91.4 85.3 94.2 86.8 58.2 93.0 90.1 67.6 90.9 81.3 90.9 68.1 10.6 92.8 89.7 54.7 89.5 |  |  |  |  |  |  |  |  |
| RED(base) | 0.04M | 85.9 | 93.0 | 91.7 | 61.1 | 91.2 | 89.2 | 72.7 | 88.2 | 84.1 |


**Table (Page 7):**

|  | #Param |  |
|---|---|---|
|  | 6739M 8.39M |  |
| RED | 0.26M | 81.69 |


**Table (Page 8):**

|  | #Param |  |  |  |  |  |
|---|---|---|---|---|---|---|
|  | 0.25M 0.07M 0.10M |  |  |  |  |  |
| RED | 0.05M | 64.86 | 8.36 | 44.99 | 67.62 | 2.28 |


**Table (Page 9):**

|  | #Param | MNLI SST-2 MRPC CoLA QNLI QQP RTE STS-B |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|
|  | 0.29M 0.02M | 86.6 93.9 88.7 59.7 92.6 90.4 75.3 90.3 83.9 93.9 89.2 61.0 90.7 87.2 78.0 90.4 |  |  |  |  |  |  |  |  |
| RED+(base) | 0.09M | 85.9 | 93.2 | 88.9 | 62.4 | 90.9 | 89.1 | 78.6 | 90.9 | 85.0 |
|  | 0.79M 0.05M | 90.2 96.0 89.8 65.5 94.7 90.7 86.3 91.7 89.5 96.0 90.3 68.1 93.5 88.8 86.2 91.3 |  |  |  |  |  |  |  |  |
| RED+(large) | 0.25M | 90.6 | 95.6 | 89.2 | 69.6 | 94.0 | 90.2 | 85.6 | 91.4 | 88.3 |


**Table (Page 9):**

|  | #Param |  |  |  |  |  |
|---|---|---|---|---|---|---|
|  | 0.79M 0.05M |  |  |  |  |  |
| RED+(medium) | 0.25M | 66.68 | 8.53 | 46.28 | 69.63 | 2.38 |
|  | 1.47M 0.09M |  |  |  |  |  |
| RED+(large) | 0.46M | 68.31 | 8.78 | 46.12 | 69.80 | 2.41 |


**Table (Page 15):**

| Hyperparameter |
|---|
| BatchSize MicroBatchSize Optimizer LRSchedulerType WarmupRatio MaximumSequenceLength |
| LearningRate NumberofEpochs |
| LearningRate NumberofEpochs BatchSize Coefficientα Dropout Rank |
| LearningRate NumberofEpochs |


**Table (Page 15):**

| #Few-shot |
|---|
| 25 0 5 5 10 10 |


**Table (Page 16):**

|  | #Param | ARC TruthfulQA Winogrande GSM8k HellaSwag MMLU |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|
|  | 6739M 8.39M | 73.34 47.07 74.03 16.22 79.95 46.55 72.07 44.84 75.85 15.01 78.60 44.42 |  |  |  |  |  |  |
| RED | 0.26M | 72.04 | 47.59 | 72.85 | 11.90 | 77.86 | 42.27 | 54.09 |


**Table (Page 16):**

| Dataset |
|---|
| Optimizer LRSchedule |
| BatchSize NumberofEpochs LearningRate WarmupRatio WeightDecay MaximumSequenceLength |
| BatchSize NumberofEpochs LearningRate WarmupRatio Rank Coefficientα MaximumSequenceLength |
| BatchSize NumberofEpochs LearningRate WarmupRatio Rank MaximumSequenceLength |
| BatchSize NumberfoEpochs LearningRate WarmupRatio Rank MaximumSequenceLength |
| BatchSize NumberofEpochs LearningRate WarmupRatio MaximumSequenceLength |
| BatchSize NumberofEpochs Learningrate WarmupRatio MaximumSequenceLength |


**Table (Page 16):**

| Dataset |
|---|
| Optimizer LRSchedule |
| BatchSize NumberofEpochs Learningrate WarmupRatio MaximumSequenceLengt |


**Table (Page 17):**

| Dataset |
|---|
| Optimizer LRSchedule |
| BatchSize NumberofEpochs Learningrate WarmupRatio WeightDecay MaximumSequenceLength |
| BatchSize NumberofEpochs Learningrate WarmupRatio Rank Coefficientα MaximumSequenceLength |
| BatchSize NumberofEpochs Learningrate WarmupRatio Rank MaximumSequenceLength |
| BatchSize NumberofEpochs Learningrate WarmupRatio Rank MaximumSequenceLength |
| BatchSize NumberofEpochs Learningrate WeightDecay WarmupRatio MaximumSequenceLength |


**Table (Page 18):**

|  | #Param | MNLI SST-2 MRPC CoLA QNLI QQP RTE STS-B |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|
|  | 125M 0.4M 0.3M 0.3M 0.1M | 87.3 94.4 87.9 62.4 92.5 91.7 78.3 90.6 ±0.34 ±0.96 ±0.91 ±3.29 ±0.22 ±0.19 ±3.20 ±0.59 87.0 93.3 88.4 60.9 92.5 90.5 76.6 90.5 ±0.28 ±0.40 ±1.54 ±3.09 ±0.02 ±0.08 ±2.26 ±0.35 87.1 93.0 88.8 58.5 92.1 90.2 77.7 90.4 ±0.10 ±0.50 ±1.38 ±1.69 ±0.28 ±0.07 ±1.93 ±0.31 86.6 93.9 88.7 59.7 92.6 90.4 75.3 90.3 ±0.26 ±0.49 ±0.76 ±4.36 ±0.10 ±0.08 ±2.79 ±0.54 84.7 94.0 88.1 54.0 91.0 87.3 69.8 89.5 ±0.08 ±0.87 ±1.57 ±3.07 ±0.05 ±0.02 ±1.51 ±0.35 |  |  |  |  |  |  |  |  |
| RED(base) | 0.02M | 83.9 ±0.14 | 93.9 ±0.31 | 89.2 ±0.98 | 61.0 ±2.96 | 90.7 ±0.35 | 87.2 ±0.17 | 78.0 ±2.06 | 90.4 ±0.32 | 84.7 |
|  | 355M 0.8M 0.9M 0.8M | 88.8 96.0 91.7 68.2 93.8 91.5 85.8 92.6 ±0.45 ±0.66 ±1.73 ±2.62 ±0.33 ±1.28 ±1.40 ±0.16 90.2 96.0 89.8 65.5 94.7 90.7 86.3 91.7 ±0.25 ±0.85 ±2.09 ±2.02 ±0.21 ±0.91 ±2.41 ±0.44 90.1 95.2 90.5 65.4 94.6 91.4 85.3 91.5 ±0.12 ±0.48 ±0.59 ±2.24 ±0.17 ±0.13 ±1.34 ±0.33 90.3 96.1 90.5 64.4 94.3 91.3 84.8 90.2 ±0.15 ±0.75 ±1.26 ±1.56 ±0.39 ±0.24 ±2.01 ±0.24 |  |  |  |  |  |  |  |  |
| RED(large) | 0.05M | 89.5 ±0.38 | 96.0 ±0.48 | 90.3 ±1.40 | 68.1 ±1.69 | 93.5 ±0.33 | 88.8 ±0.11 | 86.2 ±1.40 | 91.3 ±0.21 | 87.9 |


**Table (Page 18):**

|  | #Param |  |  |  |  |  |
|---|---|---|---|---|---|---|
|  | 355M 25.2M 0.9M 0.8M 0.8M 0.8M |  |  |  |  |  |
| RED(medium) | 0.05M | 64.86 ±0.40 | 8.36 ±0.03 | 44.99 ±0.02 | 67.62 ±0.22 | 2.28 ±0.01 |
|  | 774M 1.8M 1.5M 1.5M 1.5M |  |  |  |  |  |
| RED(large) | 0.09M | 65.77 ±0.48 | 8.42 ±0.06 | 46.12 ±0.10 | 69.03 ±0.09 | 2.36 ±0.02 |


**Table (Page 18):**

|  | 6739M 8.39M | 9.111 6.500 4.778 1.444 2.700 4.800 7.944 8.833 8.600 7.900 4.000 1.600 2.350 4.750 8.700 8.950 |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|
| RED | 0.26M | 8.778 | 7.278 | 4.875 | 1.300 | 2.625 | 4.125 | 7.400 | 9.167 | 5.732 |


**Table (Page 18):**

|  | 6739M 8.39M | 1.667 5.938 2.222 1.700 2.000 2.111 3.200 5.300 1.900 5.800 2.100 1.600 2.550 1.222 3.100 5.500 |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|
| RED | 0.26M | 1.375 | 5.500 | 2.444 | 1.444 | 2.125 | 1.750 | 3.000 | 5.875 | 2.946 |


**Table (Page 18):**

|  | 6739M 8.39M | 5.389 6.200 3.500 1.579 2.412 3.526 5.447 6.974 5.250 6.850 3.050 1.600 2.450 3.079 5.900 7.225 |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|
| RED | 0.26M | 5.294 | 6.389 | 3.588 | 1.368 | 2.375 | 2.938 | 5.750 | 7.618 | 4.401 |


**Table (Page 19):**

| Prompt | Can you help me figure out how to sew a button on a shirt? |
|---|---|
| FT | 1.Gatherthematerialsneededforsewingabutton,whichincludethread,needle,andbutton. 2.Threadtheneedlewiththedesiredcolorofthread. 3.Placethebuttonthroughtheholeintheshirtwhereitismissingorneedsreplacing. 4.Holdingthebuttoninplace,threadtheneedlethroughthefabricfromthebacksideoftheshirt. 5.Pullthethreadtightlytosecurethebuttoninplace. 6.Cutoffanyexcessthread. 7.Sewthebuttonontotheshirtbyhandorusingasewingmachine. 8.Irontheshirttosmoothoutanycreasescausedduringthesewingprocess. 9.Enjoyyournewlyrepairedshirt! |
| LoRA | 1. Gather the necessary materials: You will need a shirt, thread, a needle, and a button. If your shirthas abuttonhole, youcanusethat; otherwise, you'llhave tocreateoneusingabuttonhole templateorapattern. 2.Markthelocationofthebuttonhole:Useamarkerorchalktomarkthelocationwhereyouwant toplacethebuttonhole.Thisshouldbecenteredonthefrontoftheshirt,justbelowthecollar. 3.Createthebuttonhole:Ifyoudon'thaveabuttonholealready,you'llneedtomakeone.Todo this,foldthefabricoversothatitformsatriangleshape.Then,usearulerandapenciltodrawa linealongtheedgeofthetriangle.Cutalongthislinewithscissors. 4.Sewthebuttonhole:Threadtheneedlewiththethreadandinserttheneedlethroughthefabric atthetopofthebuttonhole.Pullthethreadtightlytocreateasmallholeinthefabric.Continue sewing around the perimeter of the buttonhole, leaving about an inch of thread unsewn at the bottom. 5.Insertthebutton:Placethebuttonontheshirt,right-sideup,withtheholefacingdown.Line upthebuttonholewiththeholeinthebuttonandpushthebuttonthroughthebuttonhole. 6.Tieoffthethread:Oncethebuttonissecurelyattached,tieoffthethreadbyknottingitnearthe beginningofthebuttonholestitching.Trimanyexcessthread. 7. Finish thebuttonhole: Foldthefabric overthebuttonholeandpress it flat with aniron. This willhelptosecurethebuttonandpreventitfromcomingloose. 8.Repeatforadditionalbuttons:Ifyouneedtoaddmorebuttons,repeatsteps4-7foreachnew button. 9.Testfit:Tryontheshirttoensurethatthebuttonsareevenlyspacedandthattheylookgood. Adjustasneeded. 10.Enjoyyournewlybuttonedshirt! |
| RED | 1. Gather the necessary materials: You will need a shirt, thread, a needle, and a button. If your shirthasbuttonsthatarealreadymissingordamaged,youcanpurchasereplacementbuttonsat mostcraftstores. 2.Preparetheshirt:Laytheshirtflatwiththebackfacingupwards.Makesuretheareawhereyou wanttosewthebuttoniscleanandfreeofanydebrisorwrinkles. 3.Threadtheneedle:Insertoneendofthethreadintotheeyeoftheneedleandpullitthrough theotherside.Tieaknotintheendofthethreadtosecureit. 4.Placethebuttonontheshirt:Positionthebuttononthedesiredlocationontheshirt,making sureit'scenteredandalignedproperly. 5.Sewthebutton:Holdingtheshirtsteadywithonehand,usetheotherhandtoguidetheneedle through the fabric from the backside of the shirt. Inject the thread into the fabric by pushing down gently with your thumb while pulling the needle through. Continue sewing around the perimeterofthebutton,makingsuretokeepthestitchesevenandconsistent. 6. Trim the excess thread: Once you have finished sewing the button, cut off any excess thread thatextendsbeyondtheedgeofthebutton. 7. Test the button: Try fastening the button onto the shirt to make sure it's securely attached. If needed,adjustthepositionofthebuttonorre-sewifit'snotproperlyattached. 8.Repeatforadditionalbuttons:Iftherearemultiplebuttonsontheshirtthatneedtobesewn, repeatsteps1-7foreachbutton. 9.Cleanup:Aftercompletingallthebuttons,carefullyremoveanyloosethreadsorlintfromthe shirt. Remember to always use caution when handling sharp objects like needlesand thread. Always wearprotectiveglovesandfollowpropersafetyprecautionstoavoidinjury. |


**Table (Page 20):**

| Prompt | Hi,mycatjustchewedonasmallweedoutsidethatlookedlikehairybittercress. Couldyoucheckifthisistoxicforcats? Pleasealsolookforplantsfromthesamefamily,asI'mnot100%sureIidentifieditcorrectly. |
|---|---|
| FT | Hello! I'm here to help answer your question about whether or not the plant your cat chewedonistoxicforthem.However,beforeIcanprovideanaccurateresponse,Ineedmore information about the plant in question. Could you please describe the plant in detail, including its appearance, size, and any unique characteristics it may have? Additionally, couldyoutellmewhatpartoftheplantyourcatingested(e.g.,leaves,stems,flowers)?This willhelpmeidentifythecorrectplantanddetermineifitissafeorharmfulforcats. AsaresponsibleAIassistant,IwanttoensurethatIprovideaccurateandhelpfulinformation whileprioritizingthesafetyandwell-beingofbothyouandyourfurryfriend.So,pleasetake amomenttoshareanyadditionaldetailsyoucanabouttheplantyourcathaschewedon,and I'lldomybesttoassistyou. |
| LoRA | Hello! I'm here to help answer your question about whether or not the plant your cat chewedonistoxicforthem.However,beforeIcanprovideanaccurateresponse,Ineedsome moreinformation.Canyoupleasetellmewhatkindofplantitwasandwhereitwasfound? This will help me identify the species and determine if it's safe for cats to consume. Additionally,Iwouldappreciateitifyoucouldprovideanyotherdetailsyouhaveaboutthe plant, such as its appearance, smell, and location. Thank you for your patience and understanding! |
| RED | Hello! I'm here to help you with your question about whether or not your cat has eaten something potentially harmful. As an AI language model, I can provide information and resourcesbasedonthebestavailableevidence.However,it'simportanttonotethatIamnota veterinarian and cannot diagnose or treat any medical conditions in animals. If you have concernsaboutyourpet'shealth,pleaseconsultalicensedveterinarian. Now,let'sfocusonyourspecificquestion.Basedonwhatyoudescribed,itsoundslikeyour catmayhaveeatensometypeofplantmaterial.It'salwaysagoodideatokeepaneyeonyour petaftertheyeatsomethingnew,especiallyifit'saplant.Somecommonsignsofpoisoning in cats include vomiting, diarrhea, drooling, lethargy, weakness, seizures, and difficulty breathing. If you notice any of these symptoms, it's essential to seek immediate veterinary care. As forthe plantitself, it'sdifficultto identify without moredetails. Bittercress (Ranunculus spp.) is a genus of flowering plants that includes several species, including buttercup, crowfoot, and spearwort. These plants are generally considered safe for cats, but there are other members of the Ranunculaceae family that could be toxic, such as aconite (Aconitum spp.),monkshood(Aconitellaspp.),andwolfsbane(Aconitine). Tobeonthesafeside,Irecommendtakingyourcattothevetforathoroughexaminationand possible testing if necessary. The vet will be able to determine if the plant your cat ate was indeedtoxicandprovideappropriatetreatmentifneeded.Theymayalsoadviseyouonhow topreventfutureexposuretopotentiallyharmfulplants. Inconclusion,whilemostplantsaresafeforcatstoconsume,it'salwaysbettertoerronthe side of caution and seek professional advice when in doubt. Please take your cat to the veterinarianforaproperevaluationandfollowtheirinstructionsaccordingly. |
