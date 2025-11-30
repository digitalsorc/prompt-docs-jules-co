---
title: "Efficient Generative LLM Serving"
original_file: "./Efficient_Generative_LLM_Serving.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["prompt-engineering", "llm", "rag", "chain-of-thought", "react"]
keywords: ["arxivpreprintarxiv", "inproc", "etal", "page", "https", "attention", "surv", "manuscriptsubmittedtoacmcomput", "submissiondate", "llm"]
summary: "<!-- Page 1 -->

1
Towards Efficient Generative Large Language Model Serving:
A Survey from Algorithms to Systems

### XUPENGMIAO,PurdueUniversity,USA

GABRIELEOLIARO,CarnegieMellonUniversity,USA
ZHIHAOZHANG,CarnegieMellonUniversity,USA
XINHAOCHENG,CarnegieMellonUniversity,USA

### HONGYIJIN,CarnegieMellonUniversity,USA

TIANQICHEN,CarnegieMellonUniversity,USA

### ZHIHAOJIA,CarnegieMellonUniversity,USA

Intherapidlyevolvinglandscapeofartificialintelligence(AI),generativelargelanguagemodels(LLMs"
related_documents: []
---

# Efficient Generative LLM Serving

<!-- Page 1 -->

1
Towards Efficient Generative Large Language Model Serving:
A Survey from Algorithms to Systems

### XUPENGMIAO,PurdueUniversity,USA

GABRIELEOLIARO,CarnegieMellonUniversity,USA
ZHIHAOZHANG,CarnegieMellonUniversity,USA
XINHAOCHENG,CarnegieMellonUniversity,USA

### HONGYIJIN,CarnegieMellonUniversity,USA

TIANQICHEN,CarnegieMellonUniversity,USA

### ZHIHAOJIA,CarnegieMellonUniversity,USA

Intherapidlyevolvinglandscapeofartificialintelligence(AI),generativelargelanguagemodels(LLMs)
standattheforefront,revolutionizinghowweinteractwithourdata.However,thecomputationalintensity
andmemoryconsumptionofdeployingthesemodelspresentsubstantialchallengesintermsofserving
efficiency,particularlyinscenariosdemandinglowlatencyandhighthroughput.Thissurveyaddressesthe
imperativeneedforefficientLLMservingmethodologiesfromamachinelearningsystem(MLSys)research
perspective,standingatthecruxofadvancedAIinnovationsandpracticalsystemoptimizations.Weprovide
in-depthanalysis,coveringaspectrumofsolutions,rangingfromcutting-edgealgorithmicmodificationsto
groundbreakingchangesinsystemdesigns.Thesurveyaimstoprovideacomprehensiveunderstandingof
thecurrentstateandfuturedirectionsinefficientLLMserving,offeringvaluableinsightsforresearchersand
practitionersinovercomingthebarriersofeffectiveLLMdeployment,therebyreshapingthefutureofAI.
CCSConcepts:•Computingmethodologies→Machinelearning;Parallelcomputingmethodologies;
Naturallanguageprocessing;•Generalandreference→Surveysandoverviews;•Hardware→
Analysisanddesignofemergingdevicesandsystems;Emergingtechnologies;•Computersystems
organization→Architectures;•Softwareanditsengineering→Operatingsystems.
AdditionalKeyWordsandPhrases:largelanguagemodel,efficiency,algorithm,system,inference,serving

### ACMReferenceFormat:

XupengMiao,GabrieleOliaro,ZhihaoZhang,XinhaoCheng,HongyiJin,TianqiChen,andZhihaoJia.2025.
TowardsEfficientGenerativeLargeLanguageModelServing:ASurveyfromAlgorithmstoSystems.ACM
Comput.Surv.1,1,Article1(January2025),35pages.https://doi.org/10.1145/3754448

## 1 Introduction

Generativelargelanguagemodels(LLMs)havebecomeadrivingforcebehindsignificantadvancementsinartificialintelligence(AI)andhavedemonstratedexceptionalperformanceacrossawide
rangeoflanguage-relatedtasks.Frommachinetranslationtosentimentanalysis,questionanswering,andtextgeneration,thesemodelshaveshowntheirprowessinunderstanding,generating,and
Authors’addresses:XupengMiao,xupeng@purdue.edu,PurdueUniversity,USA;GabrieleOliaro,goliaro@cs.cmu.edu,
CarnegieMellonUniversity,USA;ZhihaoZhang,zhihaoz3@cs.cmu.edu,CarnegieMellonUniversity,USA;XinhaoCheng,
xinhaoc@andrew.cmu.edu,CarnegieMellonUniversity,USA;HongyiJin,hongyij@cs.cmu.edu,CarnegieMellonUniversity,
USA;TianqiChen,tqchen@cmu.edu,CarnegieMellonUniversity,USA;ZhihaoJia,zhihao@cmu.edu,CarnegieMellon
University,USA.
Permissiontomakedigitalorhardcopiesofallorpartofthisworkforpersonalorclassroomuseisgrantedwithoutfee
providedthatcopiesarenotmadeordistributedforprofitorcommercialadvantageandthatcopiesbearthisnoticeand
thefullcitationonthefirstpage.CopyrightsforcomponentsofthisworkownedbyothersthanACMmustbehonored.
Abstractingwithcreditispermitted.Tocopyotherwise,orrepublish,topostonserversortoredistributetolists,requires
priorspecificpermissionand/orafee.Requestpermissionsfrompermissions@acm.org.
©2025AssociationforComputingMachinery.

## 0360-0300/2025/1-Art1

https://doi.org/10.1145/3754448
ManuscriptsubmittedtoACMComput.Surv..Submissiondate:January2025.
5202
luJ
32
]GL.sc[
2v43251.2132:viXra

<!-- Page 2 -->

1:2 Miao,etal.
manipulatinghumanlanguages.TheadventofTransformer-basedarchitectures,suchasGPT-family
(GenerativePre-trainedTransformer)[31],LLaMA-family[290],DeepSeek-family[121,190],and
otherlatestpublicLLMs(e.g.,OPT[354],BLOOM[305],Mistral[148],DeciLM[75],Baichuan[326],
GLM[343])hasplayedapivotalroleinthisparadigmshift,revolutionizingthewaynaturallanguage
processing(NLP)tasksareapproached.BeyondNLP,thesemodelsarealsotransformingawider
rangeofapplications,includingautomatedprogramming[57],sciencediscovery[156],personalizeddigitalassistants[84],creativearts[248],andnext-generationcomputingarchitecture[232],
demonstratingtheirversatilityandprofoundimpactacrossvariousindustries.
However,theunprecedentedsuccessofLLMshasalsogivenrisetoseveralchallenges,most
notably,theirformidablecomputationalrequirementsduringserving.Theimmensemodelsize
andcomplexity,coupledwiththeneedforextensivecomputationalresources,haveimpededtheir
widespreaddeploymentinreal-worldapplications.Theresource-intensivenatureofthesemodels
raisesconcernsoverenergyconsumption,scalability,andaccessibility,hinderingtheiradoptionin
broadercommunitieswithoutrichcomputeresourceslikelargecompanies.
ThissurveypaperaimstoaddressthecriticalneedforefficientLLMservingandpresentsan
exhaustiveexplorationoftheexistingmultifacetedstrategiesproposedbytheresearchcommunity
totacklethischallenge.Wepresentanin-depthexaminationoftheentirespectrumofsolutions,
spanningfromalgorithmicinnovationstonovelsystemarchitectures,allaimedatoptimizingthe
inferenceprocessforLLMs.
1.1 Objectives
TheprimaryobjectiveofthissurveyistoprovideacomprehensiveoverviewofthelatestadvancementsinLLMservingandinference.Wewillsystematicallyreviewandcategorizetheexisting
techniquesbasedontheirunderlyingapproaches,highlightingtheirstrengthsandlimitations.The
surveywillcoverabroadrangeofmethodologies,encompassingdecodingalgorithm,architecture
design, model compression, low-bit quantization, parallel computation, memory management,
requestscheduling,andkerneloptimization.
1.2 Structure
Thepaperisstructuredasfollows:Section2introducesthebackgroundinformationaboutLLM
serving.Section3includesourtaxonomyofexistingapproachesonefficientLLMservingandrevisits
theserelatedworksfromtwoaspects:algorithmicinnovations(§3.1)andsystemoptimizations
(§3.2).Afterthat,welistsomerepresentativeLLMservingframeworksandprovideanalysisin
Section4.Section5discussesbenchmarksofLLMservingsystems.Section6clarifiestheconnection
betweenthissurveyandotherrelatedliterature.Finally,weproposesomepromisingexploration
directionsinSection7forimprovinggenerativeLLMservingefficiencytomotivatefutureresearch.

## 2 Background

2.1 Transformer-basedLLM
Transformer-basedLargeLanguageModels(LLMs)havemarkedasignificantshiftinthefield
ofnaturallanguageprocessing,introducinganewparadigmforunderstandingandgenerating
humanlanguage.CentraltothisinnovationistheTransformerarchitecture,whichisbuiltupon
the concept of self-attention mechanisms [296], allowing the model to weigh the importance
ofdifferentpartsoftheinputdatawhenmakingpredictions.Mathematically,theself-attention
mechanisminTransformerscanbedescribedasfollows:Foraninputsequence𝑋 = [𝑥
1
,𝑥
2
,...,𝑥 𝑛],
theTransformercomputesasetofqueries𝑄,keys𝐾 andvalues𝑉 usinglineartransformationsof

### 𝑋.Theself-attentionscoresarethencomputedas:

ManuscriptsubmittedtoACMComput.Surv..Submissiondate:January2025.

<!-- Page 3 -->

TowardsEfficientGenerativeLargeLanguageModelServing:ASurveyfromAlgorithmstoSystems 1:3
(cid:18)𝑄𝐾𝑇(cid:19)
Attention(𝑄,𝐾,𝑉) =softmax √ 𝑉 (1)
𝑑
𝑘
where𝑑 𝑘 isthedimensionofthekeys.Thismechanismallowsthemodeltofocusondifferentparts
oftheinputsequenceforeachelementoftheoutput,capturingcomplexdependenciesregardless
oftheirdistanceintheinputsequence.
Another important structure in Transformers is the Feed-Forward Network (FFN), which is
presentineachlayeroftheTransformerandsignificantlycontributestoitscomputationalintensity.
TheFFNtypicallyconsistsoftwolineartransformationswithanon-linearactivationfunctionin
between,usuallyrepresentedas:
FFN(𝑥) =max(0,𝑥𝑊 +𝑏 )𝑊 +𝑏 (2)
1 1 2 2
Here,𝑊 ,𝑊 ,𝑏 ,and𝑏 arelearnableparametersoftheFFN,andthenon-linearfunctionmax(0,·)
1 2 1 2
(ReLU,inthiscase)introducesthenecessarynon-linearityintothemodel,allowingittolearnmore
complexpatterns.TheFFNisresponsibleforasignificantportionofthemodel’sparametercount
and,consequently,itsmemoryfootprintandcomputationalload.IneachTransformerlayer,after
themulti-headattention(MHA)aggregatesinformationfromdifferentpartsoftheinput,theFFN
processesthisaggregatedinformationindependentlyforeachposition.Thisparallelprocessing
capabilityisakeystrengthoftheTransformer,allowingittohandlesequenceseffectively.However,
italsomeansthatthecomputationalloadandmemoryrequirementsscalewiththelengthofthe
inputsequenceandthedepthofthenetwork.
Thecombinationofself-attentionandFFNinTransformer-basedLLMsenablesthesemodels
tocaptureawiderangeoflinguisticcontextsandnuances,settingnewbenchmarksinvarious
NLPtasks.However,thesubstantialcomputationalrequirementsfortrainingandinferencehave
become a critical area of research, focusing on optimizing these aspects without significantly
compromising performance. The Transformer model also includes other key components like
positionencoding,whichaddsinformationaboutthepositionofeachtokeninthesequence,and
themulti-headattentionmechanism,whichallowsthemodeltofocusondifferentpartsofthe
sequenceindifferentrepresentationalspaces.
2.2 GPUsandOtherAccelerators
The rapid advancement of LLMs owes much to the evolution of GPU architecture and other
accelerators,whichareintegraltoenhancingmodelperformanceandefficiency.GPUs(Graphics
ProcessingUnits)haveemergedasacornerstoneinthisfield,primarilyduetotheirsuperiorparallel
processingcapabilities.UnliketraditionalCPUs,whicharedesignedforsequentialprocessing,GPUs
consistofthousandsofsmall,efficientcoresdesignedforhandlingmultipletaskssimultaneously.
Thismakesthemexceptionallywell-suitedforthematrixandvectoroperationsthatareubiquitous
indeeplearningcomputations,especiallyforTransformer-basedmodels.
AtypicalGPUarchitecturecomprisesanarrayofStreamingMultiprocessors(SMs),eachcontainingseveralcoresthatshareacommoninstructionunitbutcanexecuteindependentthreadsin
parallel.Additionally,thesharedmemory(SRAM)withineachSMallowsforefficientdataexchange
andsynchronizationamongthreads,significantlyoptimizingthememoryaccesspatternsrequired
inLLMcomputations.Thisdesignisparticularlybeneficialforthecomputationallyintensivetasks
inLLMs,suchasthecalculationsofself-attentionandfeed-forwardnetworksinTransformers.
GPUsalsocomeequippedwithhigh-bandwidthmemory(HBM),whichallowsforfasterdatatransferrates,significantlyreducingthebottleneckassociatedwithmemoryaccessduringlarge-scale
computations. Moreover, the latest GPU architectures, such as NVIDIA’s Ampere and Hopper
ManuscriptsubmittedtoACMComput.Surv..Submissiondate:January2025.

<!-- Page 4 -->

1:4 Miao,etal.
architectures,continuetoofferenhancementsandpushtheboundariesofLLMcomputation,such
asimprovedmemorybandwidthandcapacity,higherfloating-pointoperationspersecond(FLOPS),
specializedmixed-precisioncomputingunits(i.e.,TensorCore)andmoreefficientutilizationof
resources, further accelerating the performance of LLMs. Some of them support various precisionformats,includingFP32(32-bitfloatingpoint),TF32(TensorFloat-32),FP16(16-bitfloating
point),BF16(BrainFloatingPoint),andevenINT8/INT4,allowingforflexibletrade-offsbetween
computationalspeedandnumericalprecision,essentialinoptimizingLLMperformance.
BeyondGPUs,avastarrayofhardwareplatformshavebeenexploredforLLMdeployment,
encompassingCPUs[19,262],mobileandedgedevices[79],ASICs[239,367],aswellasspecialized
acceleratorssuchasTPUs[157],FPGAs[336],andotheremergingAIchipsfromvariousmanufacturers(e.g.,AppleM2Ultra[172],AWSInferentia[6],SambaNova[28],Cerebras[81],Graphcore
IPUs[16]).ThissurveyprimarilyunderscoresresearchanchoredintheuseofGPUs,andseveral
technical motivations drive this emphasis. Due to their architectural innovations and superior
computationalpower,GPUshavedominatedtheresearchareaoflarge-scaledeeplearninginthe
pastfewyears[44].Furthermore,theprogramminglanguagesofGPUs,likeNVIDIA’sCUDAand
AMD’sROCm,facilitateafine-grainedcontroloverthreadhierarchies,allowingresearchersto
exploitthemassiveparallelisminherentinGPUs.Itattractsnumerousdeveloperstobuildmature
softwareecosystemsontopoftheseGPUs,fosteringamajorityoftheseminalandadvancedLLM
research.Whileotherhardwareplatformsindeedbringuniquestrengthstospecificcontexts,the
vastreservoirofresearch,development,anddeploymentcenteredaroundGPUsmakesthemanindispensablereferenceforanin-depthcomprehensionofLLMinferencemethodologies.Considering
thehardwaresimilarities,otherhardwareplatformscanalsobenefitfromthedesignphilosophies,
insights,andmethodologiesdiscussedinthissurvey.
2.3 LLMInference
LLMinference,particularlyinmodelslikeGPT(GenerativePre-trainedTransformer),oftenemploys
anauto-regressivedecodingapproach.Thismethodiscentraltohowthesemodelsgeneratetext,
ensuringthateachnewwordortokenproducedtakesintoaccounttheentiresequencegenerated
sofar.Auto-regressivedecodingoperatesundertheprincipleofsequentiallypredictingthenext
tokeninasequence,givenallthepreviousones,asshowninAlgorithm1.

### Algorithm1Auto-RegressiveDecodingforLLMInference

1: Initializetheinputsequence𝑋 0 withagivencontextorstarttoken
2: for𝑡 =1to𝑇 do
3: Predictthenexttoken𝑦 𝑡 =argmax 𝑦 𝑃(𝑦|𝑋 𝑡−1 )
4:
Updatetheinputsequence𝑋
𝑡

## =𝑋

𝑡−1
⊕𝑦
𝑡
5: if𝑦 𝑡 isEOSthen
6: break
Here,𝑃(𝑦|𝑋 𝑡−1 )representstheprobabilityofthenexttoken𝑦giventhecurrentsequence𝑋 𝑡−1 ,and
⊕denotestheconcatenationoperation.Theargmaxfunctionisusedtoselectthemostprobable
nexttokenateachstep.
Thisauto-regressiveapproachisfundamentalinLLMinferenceforgeneratingcoherentandcontextuallyappropriatetext.Itensuresthateachtokengeneratedisconditionedonacomprehensive
understandingofallpreviouslygeneratedcontent,allowingLLMstoproducehighlyrelevantand
fluenttextsequences.Priorstudieshaveprovidedin-depthanalysisonthealgorithmicintensityof
Transformer-basedLLMinference(e.g.,countingtheFLOPS,I/Oandmemoryconsumption)and
ManuscriptsubmittedtoACMComput.Surv..Submissiondate:January2025.

<!-- Page 5 -->

TowardsEfficientGenerativeLargeLanguageModelServing:ASurveyfromAlgorithmstoSystems 1:5
extensiveempiricalresultsoncostestimation(e.g.,modelingtheinferencelatency[53])according
totheauto-regressivedecodingalgorithmexecution.TheoptimizationofLLMinferenceisacomplexproblemastherecanbedifferentoptimalstrategieswithdifferentalgorithmconfigurations
andsystemsetups.
2.4 Challenges
ThissectiondescribesavarietyofchallengesforefficientLLMserving.
•LatencyandResponseTime. Efficientlargelanguagemodelinferencerequiresachieving
low-latency and fast response times, especially in real-time applications like chatbots, virtual
assistants,andinteractivesystems.Balancingmodelcomplexitywithinferencespeedisacritical
challengethatnecessitatesoptimizingalgorithmsandsystemarchitecturestominimizeresponse
timewithoutcompromisingaccuracy.
•MemoryFootprintandModelSize. Largelanguagemodelscomewithsignificantmemory
requirementsduetotheirsizeandthevastnumberofparameterstheycontain.Deployingsuch
modelsonmemory-constraineddevicesposesachallenge,demandingthedevelopmentofeffective
modelcompressiontechniquesandsystemoptimizationstoreducememoryfootprintwithout
sacrificingperformance.
•ScalabilityandThroughput. Inferencesystemsoftenfacevaryinglevelsofrequestloadsin
productionenvironments.Ensuringscalabilityandhighthroughputtohandlemultiplesimultaneous
requests efficiently requires parallel computation, request scheduling, and other system-level
optimizationstodistributecomputationalworkloadeffectivelyacrossresources.
•HardwareCompatibilityandAcceleration. Efficientlyleveraginghardwareresourcesis
crucialforlargelanguagemodelinference.AdaptingLLMmodelstodiversehardwareplatforms
andarchitectures,includingCPUs,GPUs,andspecializedaccelerators,demandshardware-aware
algorithmdesignandoptimizationtoexploitthefullpotentialoftheunderlyinghardware.
•Trade-offsbetweenAccuracyandEfficiency. OptimizingtheefficiencyofLLMinferencemay
sometimesinvolvetrade-offswithmodelaccuracy.Strikingtherightbalancebetweenmodelsize,
computationalcomplexity,andperformanceisachallengingtaskthatrequirescarefulconsideration
andevaluationofvariousalgorithmicandsystem-leveltechniques.

## 3 Taxonomy

Figure 1 illustrates our taxonomy of existing efforts on improving the LLM serving efficiency,
whichcanbebroadlyclassifiedintotwocategories,includingalgorithmicinnovationsandsystem
optimizations.Wewilldiscusseachcategoryindetailsindividually.
3.1 AlgorithmicInnovation
Thissectionpresentsacomprehensiveanalysisofthevariousalgorithmsandtechniquesproposed
tooptimizelanguagemodelinferenceefficiency.Theseworksareproposedtoaddressthenative
performanceflawsoflarge-scaleTransformermodelsthroughalgorithmicadvancements.
3.1.1 Decoding Algorithm. In this section, we review novel decoding algorithms as shown in
Figure2thatoptimizetheinferenceprocessofLLMs.Thesealgorithmsseektoreducecomputational
complexityandenhancetheoverallefficiencyoflanguagemodelinferenceduringgenerationtasks.
• Non-autoregressivedecoding.AmajorlimitationofexistingLLMsisthedefaultautoregressivedecodingmechanism,whichsequentiallygeneratesoutputtokensonebyone.To
ManuscriptsubmittedtoACMComput.Surv..Submissiondate:January2025.

<!-- Page 6 -->

1:6 Miao,etal.
Non-autoregressive

### Decoding


### Speculative

DecodingAlgorithm Decoding

### EarlyExiting

CascadeInference
ConfigDownsizing

### Attention

Simplification

### Algorithmic


### ArchitectureDesign

Innovations RecurrentUnit
ActivationSharing
Conditional
Computing

### Knowledge

LLM ModelCompression Distillation

### Serving NetworkPruning

Taxonomy ModelParallelism
Low-bitQuantization
SequenceParallelism
ParallelComputation

### CloudScaling

Decentralized

### System


### Inference


### Optimizations

MemoryManagement

### KernelFusion

RequestScheduling

### TailoredAttention

KernelOptimizations Variable
Sequencelength

### Automatic


### Compilation


### Fig.1. TaxonomyofLLMInferenceAdvancements

addressthisissue,onerepresentativelineofworkistoabandontheautoregressivegeneration
paradigmanddecodetheoutputtokensinparallel.Non-autoregressivedecoding[110,117,
122]isfirstproposedformachinetranslationaccelerationbybreakingtheworddependencies
duringdecodingandassumingacertaindegreeofconditionalindependence.Toalleviatethe
translationqualityreduction,somefollow-upstudieslikesemi-autoregressivedecoding[111],
furtherextendthesenon-autoregressivemethodstoreachauto-regressivemodelquality
by modeling output dependencies [118, 347] or iteratively refining output tokens [173].
Blockwise parallel decoding [272] inserts a single feedforward layer to the base LLM to
makepredictionsformultiplefuturepositionsinparallel,thenbacksofftothelongestprefix
validatedbythebasemodel.However,theseapproachesrequiretocostlyreproduceanew
LLMwiththenewdependenciesortunepartiallayersoftheoriginalLLM,whicharenot
alwayspossible.Somerecenteffortshavebeendedicatedtogeneratemultipletokensatone
ManuscriptsubmittedtoACMComput.Surv..Submissiondate:January2025.

<!-- Page 7 -->

TowardsEfficientGenerativeLargeLanguageModelServing:ASurveyfromAlgorithmstoSystems 1:7

### Input )# )$ )' )( Input )# )$ )' Input )# )$ )' )(


### Transformer Layer 1 Transformer Layer 1 Transformer Layer 1

Transfo.rm.e.r Layer 2 Transfo.rm.e.r Layer 2 Transfo.rm.e.r Layer 2
Transformer Layer L Transformer Layer L Transformer Layer L
)$ )' )( )) )$ )' )( )) )$ )' )( ))
(a) Auto-regressive decoding (b) Non-autoregressive decoding (c) Early exiting

### Input )#

Input )# )$ )' )( +
Input )#

### Not

Easy? %" %) %*
Speculation
Yes

## T


## T

r
r
a
a
n
n
s
s
f
f
o
o.
r
r
m
m.
e
e.
r
r

## L


## L

a
a
y
y
e
e
r
r
1
2
,# ,$ ,%

### Transformer Layer 1

)$ )' )( + Transfo . rm . e . r Layer 2

### Transformer Layer L Transformer Layer 1

Transfo.rm.e.r Layer 2 Transformer Layer L

### Transformer Layer L

Verification )$ ✓ )' ✓ )( ✗ ,# ,$ ,% ,& %" %) %* %+
(d) Speculative decoding (f) Cascade inference

### Fig.2. IllustrationofdifferentLLMdecodingalgorithms

decodingstepwithoutanytrainingormodificationtothemodel.Paralleldecoding[257]
reframesthegreedyauto-regressivedecodingasasystemofnonlinearequationssolvablein
parallelleveragingJacobiandGauss-Seidelfixed-pointiterationmethodsforfastinference.
Athoroughsurveyonnon-autoregressivetranslation[319]hasbeenproposedtosummarize
therecentadvancesinthisdirection.Untilnow,duetotheunawarenessoftheconditional
dependencebetweenoutputtokens,theoutputqualityofmostofnon-autoregressivemethods
has been still less reliable than the auto-regressive method despite an improvement in
decodingspeed.
• Speculativedecoding.Anotherlineofworkaddressesthesequentialexecutionlimitationby
leveragingspeculativeexecution[50]andimprovingdecodingparallelism.Eachdecodingstep
duringtheautoregressiveLLMinferenceprocesscanbetreatedastheexecutionofaprogram
with conditional branches, such as deciding which token to generate next. Speculative
decoding[54,177]hasbeenproposedtomakedecodingpredictionsofmultiplestepsfirst
in an efficient manner (e.g., using a smaller draft model with fewer model parameters)
andverifythesepredictionssimultaneouslywiththeLLM.However,therearestillseveral
practicalchallengesremainingwhenapplyingspeculativedecodingtoLLMs,e.g.,howto
makedecodingpredictionslight-weightandaccurateenoughandhowtoachieveefficient
parallelverificationusingLLMs.AsshowninFigure3,SpecInfer[211]firstaddressesthese
challengesbyintroducinganoveltree-basedspeculativeinferenceandtokenverification
mechanismandproposesalow-latencyLLMservingsystemimplementation(§4).Themain
advantageofspeculativedecodingisthatitincreasestheparallelismwithoutanychangesto
theoutputs.Suchguaranteecomesfromthefactthatthepredictedoutputisalwaysverified
bytheoriginalLLMandthefallbackmechanism[165]takeseffectwhenpredictiongoes
wrong.Thetree-basedspeculativedecodingdesignhasbeendirectlyadoptedbynumerous
subsequentworks,suchasMedusa[51],EAGLE[183],andsoon[38,132,197,219,229,271,
ManuscriptsubmittedtoACMComput.Surv..Submissiondate:January2025.

<!-- Page 8 -->

Triforce, CMU, Apr 2024

### OPT-Tree,THU,Jun2024


### SpecPrefill, Chicago, Feb 2025

1:8 LongSpec, Sea AI Lab, Feb 2025 Miao,etal.
Triforce AdaServe

## Rest Eagle

Speculative Decoding SpecInfer Medusa Ouroboros Hydra SpecServe

### Kangaroo

Lookahead

### LongSpec


### SpeculativeSampling

SpecTr Sequoia OPT-Tree
......
2022 2023 2023 2023 2023 2023 20242024 2024 20242024 2025 2025

### Nov Feb May Sep Oct Nov Jan Feb Apr Jun Oct Jan Feb

Sequence-based speculative decoding Tree-based speculative decoding

### Fig.3. Illustrationofdifferentspeculativedecodingapproaches

280,323,358,370].Somerecentefforts[61,137,185,297]furtherexplorehowtoadaptively
generatebetterdrafttokentreestructurestoimprovethespeculationefficiency.
• Earlyexiting.Someotherstudiesattempttoutilizethedeepmulti-layerarchitectureof
existingLLMsandleveragetheearlyexiting [286]mechanismtoacceleratethedecoding
process.Theintuitionisthattheoutputofearlymodellayershasthepotentialtoinferthe
targetdistributionconfidently.Theycanemitpredictionsbasedoninternalclassifiersinstead
ofrunningthewholeLLM,andvariousexitconditionshavebeenexplored[131,167,187,
196,278,321,333,344,368].Theyarealsocalledbyadaptivecomputation[76,259]sincethey
adjusttheamountofcomputationperrequesttoamortizethetotalinferencecost,i.e.,taking
less computation for easier inference requests. Kangaroo [191] applies this early exiting
strategytoutilizeLLM’ssub-networkandconstructaself-draftingmodelforspeculative
decoding.Broadly,theseapproachesaremostlyrestrictedtotheinsufficientinformation
carriedbyinternalrepresentationsandmaynotfaithfullymakingaccuratepredictions.
• CascadeinferenceDrivenbythevaryingcomplexitiesofinferencerequests,cascadeinferenceemploysasuiteofLLMsofdifferingscalestominimizeresponsetime.Insteadofdirectly
using a massive model for every query, CascadeBERT [179] involves a series of internal
classifierscorrespondingtodifferentmodeldepths,organizestheminacascadingmanner
andadaptivelyselectsproperonesbasedontheinstancedifficulty.Tabi[301]optimizesfor
servingdiscriminativemodels(i.e.,notgenerativeLLMs),butittakesasimilarapproach
toincorporatesmallmodelsandLLMstohandlequerieswithdifferentconfidence.Frugal-
GPT[56]leveragesalearning-basedapproachtoadaptivelyassignqueriestodifferentLLM
APIs,optimizingbothcostandperformance.Aconcurrentwork[372]jointlyoptimizesmodel
multiplexingandquerycachingandalsoanalyzestheoptimalityofminimizinginferencecost.
Mixture-of-thought[341]extendsthecascadeideatoLLMreasoningtasksforcost-saving,
whichsamplesanswersfrombothChain-of-Thought[303]andProgram-of-Thought[60]
prompts.Overall,cascadeinferenceisapromisingdirectionforenhancedinferenceefficiency,
butitisstillchallengingtodesignanaccuratedispatchingmechanismtoavoidcompromising
modelquality.
3.1.2 ArchitectureDesign. Thissubsectionexploresinnovativearchitecturedesignstailoredfor
largelanguagemodels.Researchershaveproposednovelmodelarchitectures[129]beyondthe
originalTransformerthatstrikeabalancebetweenmodelsize,performance,andefficiency,opening
newavenuesforfasterandresource-efficientinference.
ManuscriptsubmittedtoACMComput.Surv..Submissiondate:January2025.

<!-- Page 9 -->

TowardsEfficientGenerativeLargeLanguageModelServing:ASurveyfromAlgorithmstoSystems 1:9
Table1. ComparisonsofattentionsimplificationmethodsinpriorefficientTransformersandrecentLLMs.
AttentionType Selective Sliding+Dilated Globaltoken Hash-based
" "" """ """" """ " " "
! !! !!! !!!! !!! ! ! !

### SparsePattern × ×× × × ×× × × ×× × × ×× ×

References A T d o ap p t -𝑘 ive [1 [ 2 7 6 0 ] ] , , S I o n r fo ti r n m g e [ r 28 [3 3 6 ], 6] Spar L s o e n T g r F a o n r s m fo "e r r m [ ⊕e 4 r 3 ⊕ ] [⊖6 ⊕ ⊗ ⊗5 ⊖ ⊘ ⊗],⊕⊖⊕ "" St⊕a⊕r⊖T G ⊕ ⊗ r⊗ ⊖ ⊘ a M ⊗n⊕ A sf⊖ T o⊕r [ m 1"2" e 5 r ] ⊕[⊕12⊖4 ⊕ ⊗ ⊗] ⊖ ⊘ ,⊗⊕⊖⊕ " R " ⊕ef⊕ T o⊖ r r a m ⊕ ⊗ ⊗ n ⊖ ⊘ ⊗e s r⊕ fo [⊖ r 1 m ⊕66 e ] r" , [ R 2 o 5 u 1 t ] ing
LLM Scissorhands[199],H2O[355] Mistral-7B[148], StreamingLLM[317], Sparsehash
Applications [37,149,181,220,355] [317],LongNet[82] Summary[63],Landmark[218] attention[233]
! !! !! ! ! !
• Configurationdownsizing:ToreducethecomputationcostofLLMinference,astraightforward approach is to downsize the model configurations, such as using shallow encoders[114,217]ordecoders[158],weightsharing,andvocabularyshrinking[267].However,
reducingthenumberofmodelparametersalsoaffectsthedownstreamtasks’performance.
• Attentionsimplification:Oneprominentchallengeassociatedwithself-attentioncalculationsisthecomputationalcomplexity O(𝐿2),whichscalesquadraticallywiththeinput
sequencelength𝐿.NumerousTransformervariants[284]havebeenproposedtosimplify
thestandardattentionintomoreefficientalternativesforverylongsequencetasks,suchas
sparsification[342],kernelization[160],andfactorization[298].Recently,thereisatrendof
borrowingtheideasfrompriorattentionsimplificationapproaches,generalizingandcombiningthemtoshortenthecontextorreducethesizeofKVcache,aswellastheattentioncomplexity,withslightlydecodingqualitydegradation(e.g.,slidingwindowattention[148,353],
hash-basedattention[62,233],dilatedattention[82],productquantization[349]).Onecategory of these approaches is context compression by compressing the context into fewer
soft tokens(e.g.,replacingwithsummarytokens[63]orlandmarktokens[218],leveraging
additionalautoencoderschemes[108,198])ordirectlydroppingorrephrasingunimportant
contexttokensbasedondifferentimportanceguidance[94,149,181,220](orcalledsemantic
compression).Forexample,adaptivelysparseattention[37]takesalearning-basedapproach
toeliminateuninformativecontexttokensdynamicallyforeachtoken.Scissorhands[199]
and H O [355] select a few important tokens that might have a substantial influence for
2
future decoding process and save their KV cache. StreamingLLM [317] values the initial
tokensandmaintainsthemwiththeslidingwindow,whichisalsosimilartopriorwork[43].
TriForce[275]extendsthisideatoreducethedraftinglatencyandproposesahierarchical
speculativedecodingalgorithm.FastGen[107]allowsdifferentattentionheadstoemploy
differentemphasizingpatternsadaptively.Table1illustratesthesparseattentionpatterns
offourrepresentativecategoriesofapproachesandtheirapplications.However,duetothe
incompletecontext,theseapproachesmayfaceinevitableinformationlossinrealworkloads
withmorecomplexattentiondistributions.
• Activationsharing:Anotherdirectionissharingtheintermediateactivationstoimprove
theattentioncalculationefficiency.Attentionsharingapproaches[182,310,318]observethe
similarityamongdifferentlayers’attentionmatrixdistributionandreusetheseattention
matricestoreducethecomputationcosts.Multi-queryattention(MQA)[260]makesdifferent
headsshareasinglesetofkeysandvaluestoreducethememorybandwidthrequirementsin
theincrementalinference.Group-queryattention(GQA)[33]relaxesthesinglesetofkeysand
valuesrestrictiontomultiplesetsandeachsetiscoupledwithagroupofqueries.Multi-Head
LatentAttention(MLA)[190]jointlycompresseskeysandvaluesinalow-ranklatentvector,
ManuscriptsubmittedtoACMComput.Surv..Submissiondate:January2025.

<!-- Page 10 -->

1:10 Miao,etal.
leadingtosignificantmemoryreduction.Theyhavebeensuccessfullyadoptedbyseveral
recentpublicLLMsandshowntheirsuperiorperformance,including,MQA-basedmodels
suchasFalcon[375],PaLM[68],ChatGLM2-6B[7],GQA-basedmodelslikeLLaMA-2[290]
andMistral-7B[148],andMLA-basedmodelssuchasDeepSeekV2,V3,andR1[121].
• Conditionalcomputing:Thesparsely-activatedMixtureofExperts(MoE)[71,261]paradigmpartitionsamodel’scapacityacrossvarious“experts”,whicharesmallerneuralnetworks,
eachspecializingindifferentsubsetsofthedata.Itallowsthesystemtoonlyinvokethenecessaryexpertsforagiveninputbasedoncertainroutingmechanisms[92,176,226,250,258,369],
ratherthancomputingovertheentiremassivemodel,yieldingcomputationalandmemory
efficiency[87].Forexample,TaskMoE[169]illustratesthattask-levelroutingenablesmodel
increasecapacitycomparedwithtoken-levelcounterpart,whileimprovingtheinference
throughput. As LLMs continue to grow, the MoE architecture stands out as a promising
avenue to ensure both scalability and efficiency for future LLMs. In the meanwhile, the
dynamicnatureofMoEsalsodemandsspecialsystemoptimizationfrombothdistributed
communication[130,136,138,178,227,247,357]andGPUkernelimplementation[104,363]
tofacilitateMoEinferenceefficiency.
• Recurrent unit: Although recurrent neural networks (RNN) (e.g., LSTM [252]) tend to
strugglewithcapturinglong-termdependenciesinsequences[161],therearestillseveral
approachesusingrecurrentunitstoreplaceTransformermodulesandachievelinearcomputationalandmemorycomplexityduringinference,suchasRWKV[237]andRetNet[279].
Specifically,unlikepriorapproaches,theserecentexplorationsaremostlybuiltonthelinear
attention(i.e.,LinearTransformer[160],AttentionFreeTransformer[345])representation.
Afterthereformation,theyovercometheO(𝐿2)bottleneckofattentionbymodelinginteractionsbetweentokenswithlinearrecurrenceunits(e.g.,statespacemodels[100,115,116,206],
LRU[231]),whichareeasiertomaintainparallelizabletrainingproperty.Theirdesignisalso
composedofvariouspositionencodingmodules[273],exponentialdecaymechanisms[230]
andastackoftoken-wisenon-linearMLPs[288,339]orGLUs[74]toimprovethemodel
representationcapability.Recently,theyhaveshownpromisingresultsonbothmodelperformanceandcomputationefficiency.However,whetherrecurrentunitscansuccessfullyreplace
TransformersforLLMsstillremainsanopenproblem(i.e.,especiallyforlongsequences).
3.1.3 ModelCompression. Here,wedelveintotechniquesformodelcompression,whichaimto
reducethememoryfootprintandcomputationalrequirementsofLLMsbycreatingmoreefficient
andcompactmodelswithoutsignificantlossinperformance.
• KnowledgeDistillation:Onelineofworkisknowledgedistillation,whichtrainsasmall
studentmodelwiththesupervisionfromalargeteachermodel.Mostpreviousapproaches
inthisdirectionareexploringwhite-boxdistillation[119,153,254,277,299],whichrequire
accessingtheentireteachermodelparameters.DuetothearisingofAPI-basedLLMservices (e.g., ChatGPT), several black-box distilled models attract lots of attention, such as
Alpaca[282],Vicuna[64],WizardLM[322]andsoon[238,373].Thesemodelsusuallyhave
fewermodelparametersbuthaveshownpromisingperformanceonvariousdownstream
taskscomparedwiththeoriginalLLMs(e.g.,GPT-4[31]).
• Networkpruning:Networkpruningmethods[214,255,255]havebeenextensivelystudied
inthepastfewyearsbutnotallofthemcanbedirectlyappliedtoLLMs.Itisimperativeto
takeintoaccountthepotentiallyexorbitantcomputationalcostsassociatedwithretraining,
aswellasassesswhetherthepruningyieldsdiscerniblegainsininferenceefficiencybased
on the underlying system’s implementation. Some recent approaches [90, 170, 203, 256]
ManuscriptsubmittedtoACMComput.Surv..Submissiondate:January2025.

<!-- Page 11 -->

TowardsEfficientGenerativeLargeLanguageModelServing:ASurveyfromAlgorithmstoSystems 1:11
apply structural pruning methods on LLMs, which removes entire structured LLM components,facilitatingefficientGPUspeedups.Forexample,DejaVu[201]cutsoffspecific
attentionheadsandMLPparametersguidedbythecontextualsparsityhypothesiswithout
modifyingpre-trainedmodels.Therearealsosomerecentadvancementsinunstructured
methods[42,96,276,294,325],whichusuallyachieve50-60%sparsityforLLMcompression.
Itisnoteworthythattheycanfurthergeneralizetosemi-structuredN:Msparsity(i.e.,2:4and
4:8)[216],leadingtosignificantinferencespeedupwithNVIDIAsparsetensorcores’acceleration.LoSparse[184]andDSFormer[52]approximatemodelweightswithasmalldense
andasparsesemi-structuredmatrixusinglow-rankfactorization.Flash-LLM[315]relaxes
thisrequirementbyprovidingamemory-efficientSpMMimplementationforunstructured
pruningusingtensorcores.PowerInfer[270]assumesskewaccessofthesesparsely-activated
neuronsandproposesaGPU-CPUhybridinferenceengine,makingGPUandCPUhandle
differentneurons.
3.2 SystemOptimization
ThissectioninvestigatesLLMinferencesystemoptimizationtechniquestoaccelerateLLMinference
withoutmodifyingtheLLMcomputationsemantics.Thegoalofthislineofworkistoimprove
thesystemefficiencybyrefiningtheunderlyingsystemsandframeworksusedforlargelanguage
modelinference.
3.2.1 Low-bitQuantization. Thissectionexploresstate-of-the-artlow-bitquantizationtechniques
thatenableefficientrepresentationofmodelweightsandactivations.Byusingfewerbits(i.e.,less
than32)torepresentnumericalvalues,thesemethodssignificantlyreducememoryconsumption
andaccelerateinferenceonhardwareplatforms.OnelineofapproachistoquantizeLLM,and
thesequantizationmethodscanbebrieflycategorizedintotwodirections:Quantization-Aware
Training (QAT) and Post-Training Quantization (PTQ) [331]. PTQ reduces the computational
precision of model weights [77, 79, 97, 98, 141, 189] and even activations [316, 332, 340] into
eitherINT8orINT4byusingcustomCUDAkernels[180,235]orcompilations[359]forefficiency
benefits,suchasW8A16(i.e.,INT8weight-onlyquantizationandFP16orBF16activations),W4A16
in GPTQ [97], W8A8 in SmoothQuant [316] and W4A4 [314]. The evolution of hardware also
meets these requirements. One supporting evidence is that NVIDIA’s recent architectures like
TuringandAmperehaveincludedINT8andINT4tensorcores,andthelatestHopperarchitecture
hasdisabledINT4supportbutintroducedFP8tensorcoresforbetternumericalprecision(e.g.,
H100 GPU can reach 60× TFLOPS for FP8 as opposed to FP32). Existing approaches usually
adopt various quantization functions, including uniform methods (i.e., Round-to-Nearest) and
non-uniformmethods[163].Torelievetheperformancelossfromlow-precision,QATintegrates
quantization during model training [78, 200]. It is worth noting that due to challenges in the
underlyingsystemimplementation,low-precisionquantizationmethodsmaypotentiallyresult
inslowerinferencespeedscomparedtoconventionalprecisionlevelssuchasFP16[77].While
low-precisionmethodssignificantlyreducetheresourcerequirementsformodeldeployment,there
isalsoresearchindicatingthatquantizationmethodscanhaveanotableimpactonthemodel’s
inferenceperformanceduetothepresenceofscalinglaws[80].Inaddition,quantizationhasalso
beenappliedtocontextcompression(e.g.,CacheGen[198])andmemory-efficientfine-tuning(e.g.,
QLoRA[78],PEQA[162]),resultinginlowermemoryconsumptionforLLMinference.
3.2.2 ParallelComputation. Thissectionexaminesparallelcomputationstrategiestailoredforlarge
languagemodels.Leveragingparallelprocessingcapabilitiesofmodernhardwarearchitectures,
these methods distribute computation across multiple cores or devices, leading to substantial
speedupduringinference.
ManuscriptsubmittedtoACMComput.Surv..Submissiondate:January2025.

<!-- Page 12 -->

1:12 Miao,etal.
• Modelparallelism:Mostmodelparallelismapproachesarefirstproposedfordistributed
trainingoflarge-scaleDNNs,especiallyforTransformer-basedmodels.Forexample,tensor
modelparallelism[269](TP)splitsthemodellayers(e.g.,attention,FFN)intomultiplepieces
frominternaldimensions(e.g.,head,hidden)anddeployseachonaseparatedevice(e.g.,GPU).
Itcansignificantlyreduceinferencelatencythroughparallelcomputing,whichiswidelyused
formultipleGPUswithinthesamemachine,especiallyforscenarioswithhigh-speedNVLink
connections. PaLM inference [240] extends TP on large-scale Transformer inference by
involving2Dtensorparallelism[295]andclaimslowertheoreticalcommunicationcomplexity
forlargeclusters(morethan256devices).ForMQAwithonlyoneheadforkeysandvalues,
itfurtherinvolvesdataparallelismtothehybridtensorpartitionstrategy.Pipelinemodel
parallelism[145,223](PP)arrangesthemodellayersinasequenceacrossmultipledevices.
Eachdeviceisresponsibleforapipelinestagethatconsistsofmultipleconsecutivemodel
layers.WhilePPcansignificantlyincreasethenumberofinputsprocessedperunitoftime
(throughput),itdoesn’tinherentlydecreasethetimetakentoprocessasingleinputfrom
beginningtotheend(latency)likeTP.Differentparallelismtechniquesintroducevarying
degreesofcommunicationoverheadandcomputationallatency[140].Toachieveoptimal
performanceandresourceutilization,automaticparallelismhasbeenwidelystudiedbyprior
approachesfordistributedtraining(e.g.,Alpa[360],FlexFlow[147,293],Galvatron[213]).
Byreplacingtheircostmodeltofitthepredictableruntimeofauto-regressiveinferenceof
Transformermodelslike[224],it’seasytoapplypreviousautomaticsearchingalgorithms(e.g.,
dynamicprogramming,integerlinearprogramming)toLLMserving(e.g.,AlpaServe[186],
FlexFlow-Serve[12],SpotServe[212])anddeterminethemostefficientparallelismstrategy
withoutmanualintervention.
• Sequenceparallelism:AsLLMsincreasinglyhandletasksrequiringextensivecontext,such
as document analysis or conversational agents, processing lengthy sequences efficiently
becomescritical.Sequenceparallelism(SP)distributesthecomputationalandstorageload
by splitting the processing of long sequences across multiple GPUs along the sequence
lengthdimension.EachGPUprocessesaportionofthesequence,computeslocalattention
outputs,andthencommunicatesthenecessaryintermediateresults(usingtechniquessuch
asring-style[49,192]orall-gather[142,168]operations)toensurethatthefullsequence
context is incorporated into the final output. Meta further explores the implementation
detailsofcontextparallelism[327]andproposestworingattentionvariantsforlowerlatency
under varying context lengths and KV cache hit rates. To handling the growing context
window,LoongServe[306]introduceselasticsequenceparallelism,automaticallyscaling-up
andscaling-downaccordingtothecontextlengthchanges.
• Cloud scaling: Recent advancements in cloud scaling have significantly enhanced the
scalabilityandcost-effectivenessofservingLLMs.Onenotableapproachinvolvesutilizing
preemptible or spot instances — cost-effective cloud resources that can be reclaimed by
providerswithminimalnotice.SpotServe[212]isadistributedLLMservingsystemdesigned
tooperateonpreemptibleinstances,dynamicallyadjustingparallelizationconfigurations,
and migrating GPU context to maintain reliable performance despite potential instance
preemptions. Similarly, SkyServe [204] leverages a combination of spot instances across
various regions and clouds to enhance availability and mitigate correlated preemptions.
Another innovative direction is the application of serverless computing to LLM serving.
ServerlessLLM[103]thecoldstartchallengebyimplementingamultitiercheckpointloading
system,leveragingunderutilizedGPUmemoryandstoragetoreducethestartuplatency.
Collectively,theseadvancementsdemonstratethepotentialofintegratingcloudcomputing
paradigmstooptimizethescalability,reliability,andcost-efficiencyofLLMserving.
ManuscriptsubmittedtoACMComput.Surv..Submissiondate:January2025.

<!-- Page 13 -->

TowardsEfficientGenerativeLargeLanguageModelServing:ASurveyfromAlgorithmstoSystems 1:13
• Decentralized inference: Serving LLMs in decentralized environments leverages geodistributed or even heterogeneous resources to perform inference tasks. This approach
utilizesidleGPUresourcesacrossanetworkofdevices,allowingforefficientprocessingof
LLMworkloadswithoutrelyingonanexpensivecentralizedinfrastructure.Decentralized
LLMservingaddresseschallengessuchashighcostsandlimitedavailabilityofGPUresources,
makingitaviablealternativetotraditionalcentralizedsystems.Inspiredbycrowdsourced
computing,Petals[46]servesaBLOOM-176BmodelusingcollaboratedcommodityGPUsover
theInternet.Helix[207]optimizesthemodelplacementandrequestschedulingundergeodistributedheterogeneousenvironmentswithamax-flow-basedapproachformoreaffordable
LLMserving.Decentralizedinferenceopensupanewdirectiononunlockingtheoverlooked
consumer-levelGPUsforrunningLLMs,butalsosuffersfromseveralpracticalchallenges,
suchasdeviceheterogeneity[152],limitedcomputationalandmemorycapacity[151],lowbandwidthnetwork[47],faulttoleranceandprivacyprotection[281].
3.2.3 MemoryManagement. Efficientmemorymanagementremainsattheforefrontofchallenges
inLLMserving,especiallygiventheinherentmemory-intensivenatureoftransformerarchitectures.
Withthegrowingneedforlong-sequenceinference,thememoryfootprintoftheKVcachestands
outasaprimeoptimizationtargetcomparedwithmodelweightsandthenecessaryworkspacefor
otheractivations.AstheKVcachememorygrowsandshrinksdynamicallyandunpredictablyduring
incrementaldecoding,thenaiveapproach(e.g.,FasterTransformer)pre-allocatesacontiguouspiece
ofmemorywithamaximumsequencelengthassumption.Itwastesmemoryseverelyfor1)input
batcheswithvariedrequestlengthsand2)complexdecodingscenariosgeneratingmultipleoutput
sequencesinparallel(e.g.,beamsearch,paralleldecoding).vLLM[171]proposespagedattention
thatpartitionstheKVcacheintonon-contiguousmemoryblocksandsignificantlyimprovesthe
batchsizeaswellasthroughput.vAttention[241]decouplestheallocationofvirtualandphysical
memoryusingtheCUDAvirtualmemorymanagementapproachandmitigatesfragmentationwhile
hidingthelatencycostofondemandmemoryallocation.LightLLM[21]takesamoregranular
token-levelmemorymanagementmechanismtofurtherdiminishmemoryusage.However,the
overheadsofsuchfragmentedmemorymanagingmechanismsposenewchallenges.Especiallyfor
caseswhereotheroptimizationsareemployedtoboostthebatchsize,thesefine-grainedmemory
managementmethodsmightofferonlymarginalthroughputbenefitswhilesubstantiallyamplifying
theinferencelatency.It’sevidentthatmemoryreductioninLLMinferenceisintricatelytiedwith
otheralgorithmicinnovationsandsystem-leveloptimizations.Whilesomemightworkwellfor
specificworkloads,theymightcounteractoneanother,leadingtoadegradedoverallperformance.
StrikingtherightbalancebetweenmemoryefficiencyandcomputationalperformanceofLLM
inferencesystemsremainsanopenandpressingchallengeinthefield.
Therearealsosomeapproaches[35,36,123,211,266]enablingoffloadingtechniquestouse
larger but slower memory (e.g., CPU DRAM, SSD) to save model parameters or KV cache in
additiontothelimiteddevicememory(e.g.,GPUDRAM).Forinstance,systemslikeInfiniGen[174]
andHCache[106]dynamicallymanageandoffloadKVcachetoexternalmemorytiers,thereby
reducingGPUmemorypressureandacceleratingstaterestoration.Similarly,architecturessuch
as Pensieve [338] and Mooncake [244] disaggregate the inference pipeline to enable efficient
migration and restoration of model states, while methods like CachedAttention [105] exploit
offloading to reuse attention computations across multi-turn conversations, striking a balance
betweenperformanceandcost-efficiencyinLLMserving.
3.2.4 RequestScheduling. EfficientlyschedulingincominginferencerequestsiscrucialforoptimizingLLMserving.Thissectionreviewsrequestschedulingalgorithmsthatmaximizeresource
ManuscriptsubmittedtoACMComput.Surv..Submissiondate:January2025.

<!-- Page 14 -->

1:14 Miao,etal.
utilization,guaranteeresponsetimewithinlatencyservicelevelobjective(SLO),andhandlevarying request loads effectively. Request scheduling for LLM serving shares commonalities with
generalMLservingtechniques,asbothaimtoefficientlymanageincomingrequestsandoptimize
resourceutilization.Thesecommonaspectsincludedynamicbatching[34],preemption[128],priority[225],fairness[265],swapping[41],modelselection[120],costefficiency[348],loadbalancing
andresourceallocation[304].However,LLMservingalsointroducesuniquechallengesdueto
itsdistinctivecharacteristics,suchasthemassivemodelsize,iterativeautoregressivedecoding
mechanism,unknownvariableoutputlengthandstatemanagementforcontextinformation.
EarlyLLMservingsystems(e.g.,FasterTransformeroverNVIDIATriton)onlysupportrequestlevelschedulingwhichissimilartopriorapproaches.Orca[337]firstnoticesthegapbetween
generativeLLMsandtherequest-levelschedulingofpreviousMLinferencesystems.Considering
thevariableoutputsequencelength,itschedulestheexecutionoftheengineatthegranularityof
iterationwithafirst-come-first-serve(FCFS)orderandenablesbatchingaselectedsetofoperations
forbetterhardwareutilization.Plentyoffollowingapproachesinherittheselective-batchingand
iteration-levelscheduling policy,suchascontinuousbatching invLLMandRayLLM[27]andinflightbatching inTensorRT-LLM[25].Moreover,SpecInferextendstospeculativedecodingby
iteratively selecting a batch of requests to perform one iteration of speculative inference and
verification.FastServe[307]concentratesonthejobcompletiontime(JCT)andinvolvesiterationlevelpreemptiontoprioritizerequestswithshorterinputlength,insteadofFCFS.Sarathi-Serve[32]
targets the pipeline bubbles in distributed inference caused by the initial iteration of varying
length input requests. To saturate the GPU compute, it splits the input prompts into uniform
chunksandpiggybacksthechunkslotwithotherrequests’decodingiterationsifpossible,which
isalsoadoptedbyDeepSpeed-FastGencalledDynamicSplitFuse[9].S3[155]involvesanoutput
sequencelengthpredictorandhelpstoschedulemoreconcurrentrequestswithintheGPUmemory
constraintforlargerbatchsizeandhigherinferencethroughput.Theprefill-decodedisaggregation
schemewasfirstproposedbySplitwise[236]tosplitprefillfromdecodeintodifferentGPUs,while
someconcurrentwork(e.g.,DistServe[364],ExeGPT[228])haveproposedsimilararchitectures.
LLM microserving [154] introduces a request-level programmable router to support dynamic
reconfigurationofmultipledisaggregationorchestrationstrategies.
MixedLLMservingworkloadoftenmakesrequestschedulingmorecomplex.Forexample,Tetri-
Infer[135]identifiestheinterferenceissuewhenservingheterogeneousdownstreamworkloads
(e.g., conversation, summarization, writing) with different length distribution. To address this
problem,itutilizesthechunkedprefilltechnique,appliesthedisaggregatedarchitecture,andincorporatesatwo-levelschedulingalgorithmaugmentedwithalengthpredictionmodel.Andes[194]
considers users’ diverse Quality-of-Experience metrics for LLM-based text streaming services
andintroducesapreemptiverequestschedulingapproach.ConServe[243]executesonlineand
offlineLLMinferencetaskssimultaneouslyandleveragesapriority-basedschedulertoimprove
theoverallresourceutilization.Llumnix[274]reschedulestheheterogeneousrequestsreactto
theunpredictableworkloaddynamicsatruntimebasedonaload-balancingschedulingpolicyand
implementsontopofinferenceengines.
3.2.5 Kernel Optimization. In this subsection, we delve into kernel-level optimizations, which
targettheperformanceofspecificoperationswithinthelanguagemodelinferencepipeline.These
optimizationsleveragehardware-specificfeaturesandsoftwaretechniquestoacceleratecritical
computationkernels.
• Kernelfusion:Toreduceoverheadsfromkernellaunchingandmemoryaccessing,kernel
fusioniswidelyadaptedbypreviousDNNframeworksandcompilers.Sincethebackward
ManuscriptsubmittedtoACMComput.Surv..Submissiondate:January2025.

<!-- Page 15 -->

TowardsEfficientGenerativeLargeLanguageModelServing:ASurveyfromAlgorithmstoSystems 1:15
computationisnotrequiredforLLMinference,morekernelfusionchancesexist.SeveralcontemporaryTransformerinferenceengines(e.g.,FasterTransformer[2],TenTrans[309],Turbo-
Transformers[91],LightSeq[300],ByteTransformer[346])andcompilers(e.g.Welder[268])
proposetofuse1)GEMMswiththesameshape(e.g.,thethreelineartransformationsfor
query,keyandvalue)and2)AddBiaswiththeothernon-GEMMkernels,suchasresidual
connection, layer normalization and activation functions (e.g., ReLU). Among these, the
optimizationoffusedmulti-headattentionkernelhasbeenextensivelyexploredandwillbe
discussedinthefollowingaspect.
• Tailoredattention:TomaketheattentionoperationsrunefficientlyonaGPU,customizing
ortailoringtheGPUkernelsspecificallyfortheattentioncalculationiscrucial.Forexample,
cuDNNhasprovidedafusedmulti-headattentionkernelAPI[23].Meanwhile,severalimplementationshavebeenopen-sourcedformoreperformancegains.Thesecanberoughly
classifiedintotwocategoriesduetothespecialautoregressivedecodingmechanism.Oneis
forthefirstiteration(i.e.,theinitial/prefill/context/promptphase),whichprocessesalltokens
fromtheinputpromptinparallel.Forexample,xFormers[175]extendstheonlinesoftmax
trick[67,215,246]tothewholeattentioncalculationusingCUTLASS[24].Theotherisfor
thefollowingiterations(i.e.,theincremental/decode/generationphase)andthekernelonly
generatesoneoutputtokenperiteration.Forautoregressivedecoding,acommonpracticeis
tosavethepreviouslycomputedkeysandvaluessothatonlyasinglequeryisrequiredto
computewhengeneratinganewtokeninsteadofrerunningtheentiresequence.Themain
directionofoptimizationsinthisfieldismaximizingthreadoccupancyandminimizingthe
on-devicehigh-bandwidthmemory(HBM)access(i.e.,usingsharedmemoryorregisters[58]).
Theyusuallyparallelizeacrossthebatchsizeandnumberofheadsdimension(e.g.,Faster-
Transformer)todistributeworkloads.Somefurtherenableparallelizingthesequencelength
dimensionbypartitioningtheKVcacheintochunksbutrequirereducingthechunk-wise
results at last, such as FlashDecoding [292]. A subsequent work FlashDecoding++ [133]
removessuchsynchronizationforpartialsoftmaxbyintroducingaunifiedmaximumvalue
knowninadvance.Itisnecessarytoselecttheappropriateparalleldimensionbasedonthe
workloadsforbetterthreadutilization.FlashInfer[334]utilizestheblock-sparseformatto
unify diverse KV-Cache patterns, provides a customizable attention template to support
differentattentionvariants,andleveragesCUDAGraphtomaximizeGPUutilization.
• Variablesequencelength:AnotheruniquechallengeofLLMinferenceisthatthesequences
canvaryinbothinputlengthandoutputlength,andthelatterisunknowninadvance.One
way to speed up inference is to process multiple sequences in a batch at once (§3.2.4).
However,whenabatchofsequenceshasvariableinputlengths,paddingisoftenusedto
makethemallthesamelengthforbatchprocessing,wastingcomputationalandmemory
resources. To alleviate some of these inefficiencies, various strategies can be employed.
Packingtechnique[1,346]storesthesequencesintoacontinuousmemoryspacewithout
paddingandonlyunpacksbeforeattentioncalculation.Raggedtensor[93]furthersupports
computationwithminimalpaddingusingcompiler-generatedkernels.Bucketingthesequence
intoasmallercomputationgranularity(e.g.,chunks[86])isalsoapossiblesolutiontoalleviate
memory usage of padding tokens. Due to the mixed execution of the initial phase and
incrementalphase,bucketinginputprompts[32]alsobringsnewchallengestothememory
managementandrequestscheduling(§3.2.4).
• Automaticcompilation:MostexistingLLMinferencesystemsutilizevendor-specificlibrariesastheirbackend,suchascuBLAS,cuDNNandCUTLASS,whichprovideoptimized
kernelimplementations.Tofurtherimprovetheinferenceefficiency,theyalsotakegreat
effortsonoptimizingmanually-writtenkernelsforspecificLLMoperators(e.g.,attention)
ManuscriptsubmittedtoACMComput.Surv..Submissiondate:January2025.

<!-- Page 16 -->

1:16 Miao,etal.
Table2. Comparisonofstate-of-the-artopen-sourcedGPU-basedLLMservingsystems.
Name Parallel Itera- Attention Prioritized

### Github Computation tion- Kernel Opt.Target

Ref. TP PP Offload Sche. Initial Incremental 𝐿𝑎𝑡 𝑇𝑝𝑡 MainFeatures
FasterTrans- √ √ cuBLAS Fused √ •Manually-writtenkernel
former[2] GEMM attention •Lightweightruntime
FlexFlow- √ √ √ √ cuBLAS Tree √ •SpecInfer[211]
Serve[12] GEMM attention •Extremelylow𝐿 𝑎𝑡
√ √ √ Paged √ •Block-levelKVcache[171]
vLLM[29] xFormers
attention •Enlargingbatchsize&𝑇 𝑝𝑡
√ √ torch. torch. √ •CPU&DiskOffload[266]

### FlexGen[13]

bmm bmm •MaximizingsingleGPU𝑇 𝑝𝑡
√ √ Flash Paged √
TGI[18] •Huggingfaceintegration
attention attention
DeepSpeed- √ √ cuBLAS cuBLAS √ •Kernelauto-injection[10]

### Inference[3] GEMM GEMM •Multi-GPU&Multi-Node

ZeRO- √ √ √ cuBLAS cuBLAS √ •CPU&NVMeOffload[36]
Inference[3] GEMM GEMM •MaximizingsingleGPU𝑇 𝑝𝑡

### Light- √ √ Flash Token √ •Token-levelKVcache

LLM[21] attention attention •Enlargingbatchsize&𝑇 𝑝𝑡
MLC- √ √ compiled Paged √ •Universaldeployment

### LLM[285] MatMul attention •MultipletypesofGPUs

TensorRT- √ √ √ √ cuBLAS/ Paged √ •NVIDIATritonintegration

### LLM[25] Flash-attn attention •Richfeaturessupported

overNVIDIAGPUs.Despiteofthesework,thetrendofusingautomatedDNNcompilers
stillexists,suchasTVM(i.e.,Unity[253],Relax[172]andTensorIR[95,335]),MLIR[159],
JAX [99], OpenAI Triton [287], TASO [146], Mirage [311], and TorchInductor [312]. The
compilationapproachcanhelpdiscoverpotentiallymoreefficientoperatorimplementations
(e.g.,expressionderivation[361]),andmoreimportantly,facilitateadaptationtoalternative
hardwareplatforms,includingmobileandedgedevices,CPUs,DLaccelerators,andother
typesofGPUs(e.g.,AMDGPUsandAppleM2Ultra).
Insummary,ourtaxonomycategorizestheadvancementsinefficientLLMservingintotwokey
dimensions:algorithmicinnovationsandsystemoptimizations.Bothdimensionsplayacriticalrole
inreducinginferencelatencyandenhancingthroughput,thoughtheyapproachthesegoalsfrom
differentangles.Thealgorithmicsidetechniquesstreamlinethegenerationprocesstoaccelerate
inferencewhilecarefullymanagingthebalancebetweenspeedandaccuracy.Similarly,system-level
optimizationsrefinetheunderlyingcomputationalframeworktooptimizeresourceutilizationand
furtherboostperformance.Whendeployingthesetechniquesinreal-worldapplications,tradeoffs between efficiency and accuracy must be carefully considered. For example, in real-time
conversationalsystemsmaytolerateslightaccuracylossesbyusinglow-bitquantizationforfaster
responsetimes,whereashigh-stakesapplicationslikemedicaldiagnosticsdemandtheprecision
affordedbymorecomputationallyintensivemethods.

## 4 Softwareframeworks

GenerativeLLMservingrequiresafullstackofoptimizationsandmanyrecentworkshavestarted
todevelopsoftwareframeworkstoprovideefficientLLMinferencedeploymentservice.Inthe
ManuscriptsubmittedtoACMComput.Surv..Submissiondate:January2025.

<!-- Page 17 -->

TowardsEfficientGenerativeLargeLanguageModelServing:ASurveyfromAlgorithmstoSystems 1:17
following,werevisitthesesystemsandinvestigateacomprehensiveanalysisofseveralrepresentativeopen-sourcedGPU-basedLLMservingsystemsinTable2.Theanalysisdoesnotcontain
somepopularrelatedprojects,including1)specializedsolutionsforotherhardware(e.g.,PopTransformer[17],CTranslate2[8],lammap.cppandggml[14])and2)deploymentsolutionsbuiltontop
oftheothersystems,likeOpenLLM[26](vLLM),Xinference[30](ggml+vLLM+xFormers),LMDeploy[20](FasterTransformer),gpt-fast[15](PyTorch),DeepSpeed-MIIandDeepSpeed-FastGen[11]
(DeepSpeed-Inference),andRayLLMandRayServe[27](vLLM).
Wecomparethesestate-of-the-artLLMservingsystemsandsummarizetheirdifferencesinseveralaspects.First,mostofthesesystemssupporttensorparallelismtoenablemulti-GPUinference
andimprovethesystemperformance.Andsomeofthemfuturesupportpipelineparallelismor
offloadingtosupportinferenceovermulti-nodeorresource-constrainedenvironmentsindividually.
Second,partialsystemslearnfromOrcaandimplementtheiteration-levelscheduling.Third,we
investigatetheattentionkernelsofthesesystemsandintroducetheirimplementationsintermsof
theinitialandincrementalphasesrespectively.Fortheinitialphase,theyusuallyadaptabatched
generalmatrixmultiply(GEMM)approach(e.g.,cuBLAS,torch,Relay)andsomeutilizetheonline
softmaxtricktoreduceHBMaccess(e.g.,Flash-attention,xFormers).Theincrementalphaseismore
challengingbecausetheper-tokengenerationschemeresultsinlowercomputationalintensity.To
improvetheGPUutilization,FasterTransformermanuallyfusestheattentioncalculations(e.g.,
linearprojection,positionalbias,dotproduct,softmax,etc)intoasinglehigh-performancekernel
templateandinvolvesseveralkerneloptimizationtechniques,suchascachingwithshardmemory,
warp-shuffleinstructionforreduction,halfmatrixmultiplicationandaccumulation(HMMA)with
tensorcoreandmultiple-precisionsupport.FlexFlow-Serveenablesspeculativedecodingandprovidesatree-basedparalleldecodingkerneltoverifythespeculatedtokensfrommultiplesequences
(i.e.,frommultiplesmallmodelsordifferentbeamsorparallelsampling)withzero-memoryredundancyandmaximumthreadparallelism.vLLMextendsthefusedmutli-headattention(MHA)
kernelfromfromFasterTransformerbypartitioningtheKVcacheintopagestoeliminateredundant
memoryusage,especiallyforparallelsamplingscenarios.LightLLMtakesafollow-upapproachby
partitioningtheKVcacheintomorefine-grainedtoken-wisepieces.
Note that, there still remain some other notable aspects that are not covered by the above
discussions.Forexample,evenforthemostpopularFlashandPagedattentionkernels,theyare
usually implemented in different ways across these systems. TGI directly imports the original
Flash/Pagedattentionlibraries,LightLLMadoptskernelsimplementedbyOpenAITriton,MLC-LLM
generateskernelsbyTVM,andTensorRT-LLMmodifiesfromFasterTransformer’sfusedattention
kerneltosupportpagedattention.Anotherexampleisabouttheinput-awarekernelselection.For
theinitialphase,TensorRT-LLMselectsfromcuBLASandFlashattentionbasedonthecontext
length.Besidestheattentioncalculation,forthelinearprojectionoperators,thereisalsoarecent
trendofreplacingGEMMwithgeneralmatrix-vectorproduct(GEMV)tohandlethecasesofsmall
batchsize(i.e.,1)moreefficiently.Andthesesystemsalsohavemanyotherdifferentfeatures,such
asprogramminglanguage(i.e.,C++,Python),low-precisionsupport(i.e.,FP16,INT8),supported
hardwareandmodels.Insummary,thesedifferentchoicesofdesignandimplementationarelargely
determinedbytheirprioritizedoptimizationtarget.Forexample,vLLMproposespagedattention
toimprovethebatchsizeforhigherthroughput (𝑇 𝑝𝑡),whileFlexFlow-ServeleveragesSpecInferto
acceleratedecodingforlowerlatency (𝐿 𝑎𝑡).Basically,lowlatencyandhighthroughputaredual
optimizationtargetsinLLMservingsystems,representingcomplementarybutoftenconflicting
objectives,necessitatingabalancedstrategytooptimizethetrade-offbetweenrapidresponsefor
individualtasksandmaximizingthevolumeoftasksprocessedoveraspecifiedtimeframe.Some
recentstudies[73]furtherdecomposetheresponselatencybyTTFT+TPOT×outputsequence
length,whereTTFTrepresentsTimeToFirstTokenandTPOTrepresentsTimePerOutputToken.
ManuscriptsubmittedtoACMComput.Surv..Submissiondate:January2025.

<!-- Page 18 -->

1:18 Miao,etal.
Theformerisdrivenbytheinitialphaseprocessingspeedwhilethelatterdirectlydependson
per-iterationexecutiontimeduringincrementaldecoding.Distinguishingthesetwometricsis
beneficialtoLLMserviceproviders,leadingtodifferentsystemdesignchoicesanduserexperience
(e.g.,fasterapplicationresponsiveness[198],longerprompts[9]).Somerecentkernellibrariesand
compilers(e.g.,FlashInfer[334],Mirage[311],FlexAttention[83])providemoreflexibleprogram
interfacesandgenerateoptimizedkernelsadaptivelyaccordingtotheinputconfigurations,which
arealsointegratedwithmainstreamLLMservingengines.Althoughitunlikelytohaveaonesize-fits-allsolution,webelievethatfutureLLMservingsystemswillcontinuallyintegratethese
differentiatedfeatures,therebycontinuouslyimprovingsystemefficiencyandhardwareutilization.

## 5 Benchmarks

Most existing work evaluate their system performance under real-world traces by leveraging
thedynamicrequestarrivalpatternsfrompublicproductiondatasets(e.g.,BurstGPT[302]and
Azure[236].)BuildingacomprehensiveandreproduciblebenchmarkforcomparingtheperformanceofvariousLLMservingsystemlikeMLPerf[249]isacriticalendeavorforbothacademic
andindustrialcommunitiesinthisfield.ItwillnotonlyhelpLLMusersselecttherightsystem
solutions but also encourage researchers and developers to keep pace with the advanced optimizations.Unfortunately,despiteofsomepriorreports[5,22],uptothispoint,thecommunity
has not yet launched a convincing enough benchmark that takes into account all influencing
factors.Thisismainlybecauseofthenumerousevaluationsettings,includingmodelconfiguration,
hardwareenvironment,andrequestload,amongothers.Mostrelatedbenchmarks(e.g.,LLM-Perf
Leaderboard[139])aredesignedforcomparingtheperformanceofdifferentLLMsunderthesame
infrastructure.LLM-Inference-Bench[66]hasbeenproposedtoevaluatethehardwareinference
performanceofLLMs,includingGPUsfromNVIDIAandAMDandspecializedAIaccelerators,
IntelHabanaandSambaNova.Testingunderalimitednumberofsettingcombinationscannotyield
conclusionswithcredibility.Forexample,certainsystemoptimizationtechniquescanonlyachieve
performanceadvantagesunderhighorlowloadconditions,andconversely,theymightevenbe
detrimental.Besides,whenmeasuringinferencelatency,howtoexcludeadditionaloverheadsnot
relatedtoGPUinference(suchasrequestschedulingoverhead,inherentnetworklatency,etc.)due
todifferencesinsystemdesignisalsoachallengingtopic.Additionally,afairbenchmarktestneeds
toconsiderthestrictalignmentofmodeloutputcontent,whichisoftenoverlookedinmanytests.
Furthermore, designing such benchmarks demands careful calibration of trade-offs among
throughput,latency,andcost-efficiencyacrossaspectrumofworkloadscenarios—frombursty
andunpredictabletraffictosustainedhigh-loadconditions.Atrulycomprehensiveevaluationmust
incorporatevariedrequestpatterns,diversehardwareconfigurations,anddetailedmeasurements
thatisolatecoreinferenceperformancefromextraneoussystemoverheads.Moreover,itisessential
toaccountfordifferencesinresourceallocation,schedulingstrategies,andcommunicationlatencies,
ensuringthatanyperformancegainsareattributabletotheunderlyingoptimizationsratherthan
artifactsofthetestingenvironment.Establishingsuchastandardbenchmarkwillprovidevaluable
guidanceforbothpractitionersandresearchers,facilitatingtransparentcomparisonsanddriving
furtherinnovationinLLMservingsystems.

## 6 Connectionwithothersurveys

OursurveyonefficientgenerativeLLMservingandinferencecomplementsandextendsthescope
ofexistingliteratureinthefield,whilemaintainingadistinctfocus.Amongtherelatedworks,
[164]comesclosestinsubjectmatterexploringthedesignofmoregeneralTransformermodels
anddomain-specificaccelerators.However,oursurveydifferentiatesitselfbyfocusingspecifically
ongenerativeLLMserving,anuancedareathathasnotbeenthecentralfocusofotherstudies.
ManuscriptsubmittedtoACMComput.Surv..Submissiondate:January2025.

<!-- Page 19 -->

TowardsEfficientGenerativeLargeLanguageModelServing:ASurveyfromAlgorithmstoSystems 1:19
Moreover, some studies delve into experimental investigations of LLM inference efficiency on
GPUs[224,351]andnovelaccelerators[88],offeringvaluableempiricalinsightsthataredirectly
relevanttoourfocusonservingefficiency.Additionally,LLMCarbon[89]addressesanincreasingly
importantaspectofLLMdeployment–itsenvironmentalimpact(e.g.,carbonfootprints).Whileour
survey’sprimaryfocusisefficiencyfromaperformancestandpoint,theenvironmentallensprovided
by such studies is undeniably relevant and respected in our broader discussion. Some surveys
and benchmarks [143] offer valuable insights into model compression [127, 291, 374, 374] and
quantization[112,331].Thesestudieslayagroundworkthatindirectlysupportsourexploration
of related directions. Some studies [72, 221] provide essential context for understanding LLM
effectiveness(e.g.,accuracy,perplexity,factualityandsoon),whichisbeyondthescopeofthis
survey.Oursurveyalsoacknowledgesthecontributionsofpriorsurveys[44,205]focusingon
distributedtrainingoflarge-scaleDNNmodels,astheyinformthebackdropagainstwhichLLM
servingmustbeconsidered.Inessence,oursurveysituatesitselfamidstadiversearrayofstudies,
drawingfromandcontributingtoamoreholisticunderstandingofLLMservingefficiency,including
bothalgorithmicinnovationsandsystemoptimizations.Byintegratinginsightsfromthesevarious
areas,weaimtoprovideanuancedandcomprehensiveoverviewofthelatestadvancementsand
challengesinthefield.

## 7 Futuredirection

As we stand at the forefront of LLM advancements, it becomes increasingly important to not
only understand the current state of these technologies but also to anticipate and shape their
futuretrajectory.ParticularlyintherealmofgenerativeLLMserving,thereisavastlandscapeof
unexploredpossibilitiesandemergingchallenges.Therapidevolutionofthisfieldnecessitatesa
forward-lookingapproach,whereidentifyingpotentialavenuesforinnovationandimprovement
iscrucial.Thisforesightnotonlypreparesustoadapttoupcomingtechnologicalshiftsbutalso
guidestheresearchcommunitytowardaddressingthemostpertinentandimpactfulareas.Inthis
context,weoutlineseveralpromisingdirectionsforfutureresearchanddevelopment,eachoffering
thepotentialtosignificantlyenhancetheefficiencyofservinggenerativeLLMs.
•DevelopmentandEnhancementofHardwareAccelerators. Futureprogressinenhancing
generativeLLMservingefficiencycouldbesignificantlydrivenbythedevelopmentandrefinement
ofspecializedhardwareaccelerators,complementedbyaco-designapproachthatalignshardware
andsoftwareoptimizations.Forinstance,integratingmemoryclosertoprocessingunitsoroptimizingchiparchitecturestobetteralignwiththedataflowofLLMalgorithmscanleadtosubstantial
reductionsinlatencyandenergyconsumption.ThisapproachhasbeenexemplifiedinrecentGPU
advancements,likeNVIDIA’sHopperarchitecture[4],whichdemonstratesimprovementsinHBM
andSRAMcapacity,memorybandwidth,computingunitsandbisectionbandwidth,directlybenefitingtheprocessingofLLMs.Continuedinnovationinthisareacouldinvolvedesigninghardware
thatisinherentlytunedtothecomputationalpatternsofgenerativeLLMs,suchasoptimizingfor
thespecificdemandsofattentionmechanismsandtensoroperationsthatareprevalentinthese
models,eventuallyinfluencingthedesignandimplementationofLLMservingsystems.
•EfficientandEffectiveDecodingAlgorithms. Thedevelopmentofmoreefficientdecoding
algorithms could substantially improve serving efficiency. Motivated by the demand for more
resource-efficient ways to utilize the vast knowledge encapsulated within LLMs, future work
couldexplorealternativeapproachestothetraditionalauto-regressivemethodsandunlockthe
generationspeedforreal-timeapplicationswhilemaintainingthedecodingquality.Onepromising
directionisgeneralizedspeculativeinferenceasitenablespreservingthesamegenerationquality.
Specifically,thesmallspeculativemodelcanbegeneralizedtoanyotherformsofmethodsthatcan
ManuscriptsubmittedtoACMComput.Surv..Submissiondate:January2025.

<!-- Page 20 -->

1:20 Miao,etal.
generatedrafttokensmoreefficientlythanLLMs,suchasknowledgeretrieveranduser-defined
functions[211,328].Forexample,somesubsequentworksaroserecently,replacingthedraftmodel
with early exiting [39, 134, 330, 350] or non-autoregressive decoding [101, 109]. Some further
generalizespeculativedecodingtohandleothertypesofworkloads,suchasretrieval-augmented
generation[356],longinputsequences[193,329],anddiffusionmodels[69,144].Insummary,the
developmentofefficientdecodingalgorithmslikespeculativedecodingcoupledwiththeunderlying
systemoptimizationsrepresentsasignificantopportunitytoenhancetheservingefficiencyof
generativeLLMs.
•LongContext/SequenceScenariosOptimization. AstheapplicationofLLMscontinuesto
expandintomoresophisticatedscenarios,thedemandforprocessinglongercontextsorsequences
issteadilygrowing.ServingLLMswithlong-sequenceworkloadsrequiresresolvingthechallenges
fromboththealgorithmandsystemsides.IntermsofLLMs,theyoftensufferfromlengthgeneralizationfailurewhensequencesgetlongerthanwhatwasobservedduringtraining[242]even
enablingrelativepositionalencoding[59]orafterfine-tuningonlongercorpora[40].Evenfor
somemodelsthatclaimtosupportultra-longcontexts,studieshavefoundthattheyencountera
situationof“lossinthemiddle”[195].Currentapproachesattempttoalleviatesuchlimitations
byreducingthecomputationalsequencelengthwhilepreservingrelevantinformation,suchas
retrievalaugmentation[324],sequencecompression[150]andcaching[113].FortheLLMserving
systems,longersequencebringscriticalchallenges,includingmorememoryconsumptionand
accessofKVcacheandquadraticincreasingcomputationalcomplexityofself-attention.
•InvestigatingAlternativeArchitectures. AlthoughTransformermodelsandself-attention
mechanismscurrentlydominatethelandscapeofLLMs,exploringalternativearchitecturesisa
promisingdirectionforfutureresearch.ThefieldofDLhashistoricallyseenaconstantalternation
ofdominantarchitectures,witheachnewparadigmshiftbringingaboutsignificantadvancements.
Giventhistrend,it’simportanttoconsiderotherarchitecturalapproachesthatcouldofferdistinct
advantages,especiallyforimprovedcomputationalefficiency.Forinstance,somerecentstudies
explore attention-free methods [48], using pure MLP (Multi-Layer Perceptron) architectures to
replace attention mechanisms. These changes also bring new innovation opportunities of the
underlyinginferenceengine,suchasKVcachemanagement[234].TheevolutionofDNNmodel
architectureisnotonlyanaturalprogression,butalsoanecessaryexplorationtouncovermore
efficientandeffectivewaysofstructuringLLMs.
•ExplorationofDeploymentinComplexEnvironments. AstheapplicationofLLMsexpands,
acrucialfuturedirectioninvolvesexploringandoptimizingtheirdeploymentacrossvariouscomplexenvironments.Thisexplorationgoesbeyondtraditionalcloud-baseddeploymentstoinclude
scenarioslikeedgecomputing,hybridcomputing(combiningcloudandedgecomputing),decentralizedcomputing,andtheutilizationofmoreaffordableresourceslikespotinstances.Eachofthese
environmentspresentsuniquechallengesandopportunitiesforLLMserving.Forinstance,edge
computingallowsforfasterresponsetimesandreducedbandwidthusagebyprocessingdatacloser
tothesource,butitalsoposeschallengesintermsoflimitedcomputationalresourcesandstorage
capacity.Hybridcomputing[245]offersabalancedapproachbutrequiresadvancedmanagement
todistributecomputationaltasksefficiently.Decentralizedcomputingpresentsapromisingavenue
forcrowdsourcingcomputationalresources,butitalsobringsadditionalconsiderationsregarding
dataprivacyandsecurity[202,352].LLMservingoverpreemptiveresources[212]cansignificantly
reducemonetarycostsbutrequiresfaulttolerancemechanismstohandletheirinherentunpredictabilityandvariability,ensuringconsistentperformanceandsystemreliability.Successfully
ManuscriptsubmittedtoACMComput.Surv..Submissiondate:January2025.

<!-- Page 21 -->

TowardsEfficientGenerativeLargeLanguageModelServing:ASurveyfromAlgorithmstoSystems 1:21
navigatingthechallengesfromthesecomplexenvironmentswillbekeyformorerobust,scalable,
andefficientLLMapplications.
•AutomaticAdaptationtoSpecificRequirements. Thediverseapplication-specificrequirementscreateawiderangeofinnovativeLLMservingoptimizationopportunities,suchasparameterefficientfine-tuning[55,210,264,308,371],reinforcementoronlinelearningandknowledgeupdates[208,263,365],retrievalfromexternalvectorstorage[45],multi-roundconversation[188],
reasoningandplanning[102],multi-modalworkloads,structuredgeneration[85,362],andchainingtogetherdifferentLLMs’capabilities[313](e.g.,multi-agentsimulation[320]).Theseunique
challengesalsodemandautomaticandsmoothintegrationofLLMservingtechniquesintoexisting
ITinfrastructuresbyextendingtheoptimizationspacetothewholeLLMlifetime,includingdata
acquisitionandprocessing[209],AutoML[289]andmodelmanagement[222],resourceallocations,
andperformancemonitoring.

## 8 Conclusion

EfficientLLMservingisafundamentalsteptowardsdemocratizingaccesstoadvancedAItechnologies.Thissurveyaimstoprovideresearchers,practitioners,anddeveloperswithacomprehensive
understandingoftheexistingmethodologies,enablingthemtomakeinformeddecisionswhen
deploying LLMs in real-world environments. By consolidating the latest research findings on
algorithmsandsystems,thissurveypaperhopestoaccelerateprogressandfosterinnovationin
thepursuitofhighlyefficientLLMservingsolutions.

## References

[1] 2020. NVIDIAEffectiveTransformer. https://github.com/bytedance/effective_transformer. Commit:e406421,
Accessedon:2023-11-25.
[2] 2021.NVIDIAFasterTransformer.https://github.com/NVIDIA/FasterTransformer. Commit:df4a753,Accessedon:
2023-11-25.
[3] 2022.DeepSpeedInference.https://github.com/microsoft/DeepSpeed. Commit:2afa1c7,Accessedon:2023-11-25.
[4] 2022. NVIDIA H100 Tensor Core GPU Architecture. https://resources.nvidia.com/en-us-tensor-core/gtc22-
whitepaper-hopper. Accessedon:2023-11-25.
[5] 2023.AnyScaleLLMPerfleaderboard.https://github.com/ray-project/llmperf-leaderboard. Accessedon:2023-12-23.
[6] 2023. AWSInferentia. https://aws.amazon.com/blogs/machine-learning/deploy-large-language-models-on-awsinferentia2-using-large-model-inference-containers/.
[7] 2023.ChatGLM2-6B.https://huggingface.co/THUDM/chatglm2-6b.
[8] 2023.CTranslate2.https://github.com/OpenNMT/CTranslate2. Commit:d963499,Accessedon:2023-11-25.
[9] 2023.DeepSpeed-FastGen.https://github.com/microsoft/DeepSpeed/tree/master/blogs/deepspeed-fastgen. Accessed
on:2023-11-25.
[10] 2023.DeepSpeed-Inferencev.s.ZeRO-Inference.https://github.com/microsoft/DeepSpeed/issues/4234. Accessedon:
2023-11-25.
[11] 2023.DeepSpeed-MII.https://github.com/microsoft/DeepSpeed-MII. Commit:f34b772,Accessedon:2023-11-25.
[12] 2023.FlexFlow-Serve.https://github.com/Flexflow/FlexFlow/tree/inference. Commit:672cdad,Accessedon:2023-11-
25.
[13] 2023.FlexGen.https://github.com/FMInference/FlexGen. Commit:d34f7b4,Accessedon:2023-11-25.
[14] 2023.ggml.https://github.com/ggerganov/ggml. Commit:a5e4560,Accessedon:2023-11-25.
[15] 2023.gpt-fast.https://github.com/pytorch-labs/gpt-fast. Commit:8c8c463,Accessedon:2023-12-23.
[16] 2023. Graphcore. https://www.graphcore.ai/posts/dolly-2.0-open-source-language-model-with-chatgpt-likeinteractivity.
[17] 2023.GraphcorePopTransformer.https://github.com/graphcore/PopTransformer. Commit:1314598,Accessedon:
2023-11-25.
[18] 2023.HuggingfaceTextGenerationInference.https://github.com/huggingface/text-generation-inference. Commit:
3c02262,Accessedon:2023-11-25.
[19] 2023.IntelExtensionforTransformers.https://github.com/intel/intel-extension-for-transformers. Commit:37d4007,
Accessedon:2023-12-23.
ManuscriptsubmittedtoACMComput.Surv..Submissiondate:January2025.

<!-- Page 22 -->

1:22 Miao,etal.
[20] 2023.InterLMLMDeploy.https://github.com/InternLM/lmdeploy. Commit:c07f60f,Accessedon:2023-11-25.
[21] 2023.LightLLM.https://github.com/ModelTC/lightllm. Commit:84671a7,Accessedon:2023-11-25.
[22] 2023.Llama-v2-7bbenchmark.https://hamel.dev/notes/llm/inference/03_inference.html. Accessedon:2023-11-25.
[23] 2023. NVIDIA cuDNN MultiHeadAttn. https://docs.nvidia.com/deeplearning/cudnn/api/index.html#
cudnnMultiHeadAttnForward. Accessedon:2023-11-25.
[24] 2023.NVIDIACUTLASS.https://github.com/NVIDIA/cutlass. Commit:b5d8a5d,Accessedon:2023-11-25.
[25] 2023.NVIDIATensorRT-LLM.https://github.com/NVIDIA/TensorRT-LLM. Commit:6837c81,Accessedon:2023-11-
25.
[26] 2023.OpenLLM.https://github.com/bentoml/OpenLLM. Commit:b4ea4b3,Accessedon:2023-11-25.
[27] 2023.RayLLM.https://github.com/ray-project/ray-llm. Commit:fa3a766,Accessedon:2023-11-25.
[28] 2023.Sambanova.https://sambanova.ai/press/sambanova-unveils-new-chip-the-sn40l/.
[29] 2023.vLLM.https://github.com/vllm-project/vllm. Commit:7c60044,Accessedon:2023-11-25.
[30] 2023. XorbitsInference(Xinference). https://github.com/xorbitsai/inference. Commit:22732d8,Accessedon:
2023-11-25.
[31] JoshAchiam,StevenAdler,SandhiniAgarwal,LamaAhmad,IlgeAkkaya,FlorenciaLeoniAleman,DiogoAlmeida,
JankoAltenschmidt,SamAltman,ShyamalAnadkat,etal.2023.Gpt-4technicalreport.arXivpreprintarXiv:2303.08774
(2023).
[32] AmeyAgrawal,NitinKedia,AshishPanwar,JayashreeMohan,NipunKwatra,BhargavGulavani,AlexeyTumanov,
andRamachandranRamjee.2024.TamingThroughput-LatencytradeoffinLLMinferencewithSarathi-Serve.InProc.
ofOSDI2024.117–134.
[33] JoshuaAinslie,JamesLee-Thorp,MichieldeJong,YuryZemlyanskiy,FedericoLebrón,andSumitSanghai.2023.
GQA:TrainingGeneralizedMulti-QueryTransformerModelsfromMulti-HeadCheckpoints.InProc.ofEMNLP2023.
[34] AhsanAli,RiccardoPinciroli,FengYan,andEvgeniaSmirni.2020.Batch:machinelearninginferenceservingon
serverlessplatformswithadaptivebatching.InProc.ofSC2020.1–15.
[35] KeivanAlizadeh,ImanMirzadeh,DmitryBelenko,KarenKhatamifard,MinsikCho,CarloCDelMundo,Mohammad
Rastegari,andMehrdadFarajtabar.2023. LLMinaflash:EfficientLargeLanguageModelInferencewithLimited
Memory.arXivpreprintarXiv:2312.11514(2023).
[36] RezaYazdaniAminabadi,SamyamRajbhandari,MinjiaZhang,AmmarAhmadAwan,ChengLi,DuLi,EltonZheng,
JeffRasley,ShadenSmith,OlatunjiRuwase,etal.2022.Deepspeedinference:Enablingefficientinferenceoftransformer
modelsatunprecedentedscale.arXivpreprintarXiv:2207.00032(2022).
[37] SotirisAnagnostidis,DarioPavllo,LucaBiggio,LorenzoNoci,AurelienLucchi,andThomasHoffmann.2023.Dynamic
ContextPruningforEfficientandInterpretableAutoregressiveTransformers.arXivpreprintarXiv:2305.15805(2023).
[38] ZacharyAnkner,RishabParthasarathy,AniruddhaNrusimha,ChristopherRinard,JonathanRagan-Kelley,and
WilliamBrandon.2024.Hydra:Sequentially-DependentDraftHeadsforMedusaDecoding.InCOLM2024.
[39] SangminBae,JongwooKo,HwanjunSong,andSe-YoungYun.2023.FastandRobustEarly-ExitingFrameworkfor
AutoregressiveLanguageModelswithSynchronizedParallelDecoding.arXivpreprintarXiv:2310.05424(2023).
[40] YushiBai,XinLv,JiajieZhang,HongchangLyu,JiankaiTang,ZhidianHuang,ZhengxiaoDu,XiaoLiu,etal.2024.
LongBench:ABilingual,MultitaskBenchmarkforLongContextUnderstanding.InProc.ofACL2024.
[41] ZhihaoBai,ZhenZhang,YiboZhu,andXinJin.2020.PipeSwitch:Fastpipelinedcontextswitchingfordeeplearning
applications.InProc.ofOSDI2020.499–514.
[42] PeterBelcakandRogerWattenhofer.2023.ExponentiallyFasterLanguageModelling.arXivpreprintarXiv:2311.10770
(2023).
[43] IzBeltagy,MatthewEPeters,andArmanCohan.2020.Longformer:Thelong-documenttransformer.arXivpreprint
arXiv:2004.05150(2020).
[44] TalBen-NunandTorstenHoefler.2019.Demystifyingparallelanddistributeddeeplearning:Anin-depthconcurrency
analysis.ACMComputingSurveys(CSUR)(2019),1–43.
[45] SebastianBorgeaud,ArthurMensch,JordanHoffmann,TrevorCai,ElizaRutherford,KatieMillican,GeorgeBm
VanDenDriessche,Jean-BaptisteLespiau,BogdanDamoc,AidanClark,etal.2022.Improvinglanguagemodelsby
retrievingfromtrillionsoftokens.InProc.ofICML.2206–2240.
[46] AlexanderBorzunov,DmitryBaranchuk,TimDettmers,MaxRyabinin,YounesBelkada,ArtemChumachenko,Pavel
Samygin,andColinRaffel.2023.Petals:Collaborativeinferenceandfine-tuningoflargemodels.InProc.ofACL2023.
[47] AlexanderBorzunov,MaxRyabinin,ArtemChumachenko,DmitryBaranchuk,TimDettmers,YounesBelkada,Pavel
Samygin,andColinRaffel.2023.DistributedInferenceandFine-tuningofLargeLanguageModelsOverTheInternet.
arXivpreprintarXiv:2312.08361(2023).
[48] VukasinBozic,DaniloDordevic,DanieleCoppola,andJosephThommes.2023. RethinkingAttention:Exploring
ShallowFeed-ForwardNeuralNetworksasanAlternativetoAttentionLayersinTransformers. arXivpreprint
arXiv:2311.10642(2023).
ManuscriptsubmittedtoACMComput.Surv..Submissiondate:January2025.

<!-- Page 23 -->

TowardsEfficientGenerativeLargeLanguageModelServing:ASurveyfromAlgorithmstoSystems 1:23
[49] WilliamBrandon,AniruddhaNrusimha,KevinQian,ZacharyAnkner,TianJin,ZhiyeSong,andJonathanRagan-
Kelley.2023.Stripedattention:Fasterringattentionforcausaltransformers.arXivpreprintarXiv:2311.09431(2023).
[50] FWarrenBurton.1985. Speculativecomputation,parallelism,andfunctionalprogramming. IEEETrans.Comput.
(1985),1190–1193.
[51] TianleCai,YuhongLi,ZhengyangGeng,HongwuPeng,andTriDao.2023.Medusa:Simpleframeworkforaccelerating
llmgenerationwithmultipledecodingheads.https://github.com/FasterDecoding/Medusa.Commit:dd9c8a5,Accessed
on:2023-11-25.
[52] RahulChand,YashotejaPrabhu,andPratyushKumar.2023.DSFormer:EffectiveCompressionofText-Transformers
byDense-SparseWeightFactorization.arXivpreprintarXiv:2312.13211(2023).
[53] CarolChen.2022.TransformerInferenceArithmetic.https://kipp.ly/blog/transformer-inference-arithmetic/.Accessed
on:2023-11-25.
[54] CharlieChen,SebastianBorgeaud,GeoffreyIrving,Jean-BaptisteLespiau,LaurentSifre,andJohnJumper.2023.
Acceleratinglargelanguagemodeldecodingwithspeculativesampling.arXivpreprintarXiv:2302.01318(2023).
[55] LequnChen,ZihaoYe,YongjiWu,DanyangZhuo,LuisCeze,andArvindKrishnamurthy.2023.Punica:Multi-Tenant
LoRAServing.arXivpreprintarXiv:2310.18547(2023).
[56] LingjiaoChen,MateiZaharia,andJamesZou.2023.FrugalGPT:HowtoUseLargeLanguageModelsWhileReducing
CostandImprovingPerformance.arXivpreprintarXiv:2305.05176(2023).
[57] MarkChen,JerryTworek,HeewooJun,QimingYuan,HenriquePondedeOliveiraPinto,JaredKaplan,HarriEdwards,
YuriBurda,NicholasJoseph,GregBrockman,etal.2021.Evaluatinglargelanguagemodelstrainedoncode.arXiv
preprintarXiv:2107.03374(2021).
[58] ShiyangChen,ShaoyiHuang,SantoshPandey,BingbingLi,GuangRGao,LongZheng,CaiwenDing,andHangLiu.

#### Et:re-thinkingself-attentionfortransformermodelsongpus.InProc.ofHPCA2021.1–18.

[59] ShouyuanChen,ShermanWong,LiangjianChen,andYuandongTian.2023. Extendingcontextwindowoflarge
languagemodelsviapositionalinterpolation.arXivpreprintarXiv:2306.15595(2023).
[60] WenhuChen,XueguangMa,XinyiWang,andWilliamWCohen.2022.Programofthoughtsprompting:Disentangling
computationfromreasoningfornumericalreasoningtasks.arXivpreprintarXiv:2211.12588(2022).
[61] ZhuomingChen,AvnerMay,RuslanSvirschevski,Yu-HsunHuang,MaxRyabinin,ZhihaoJia,andBeidiChen.2024.
Sequoia:Scalableandrobustspeculativedecoding.Proc.ofNeurIPS(2024),129531–129563.
[62] ZhuomingChen,RanajoySadhukhan,ZihaoYe,YangZhou,JianyuZhang,NiklasNolte,YuandongTian,Matthijs
Douze,LeonBottou,ZhihaoJia,etal.2024.Magicpig:Lshsamplingforefficientllmgeneration.InProc.ofICLR2024.
[63] AlexisChevalier,AlexanderWettig,AnirudhAjith,andDanqiChen.2023.AdaptingLanguageModelstoCompress
Contexts.arXivpreprintarXiv:2305.14788(2023).
[64] Wei-LinChiang,ZhuohanLi,ZiLin,YingSheng,ZhanghaoWu,HaoZhang,LianminZheng,SiyuanZhuang,Yonghao
Zhuang,JosephE.Gonzalez,IonStoica,andEricP.Xing.2023.Vicuna:AnOpen-SourceChatbotImpressingGPT-4
with90%*ChatGPTQuality. https://lmsys.org/blog/2023-03-30-vicuna/
[65] RewonChild,ScottGray,AlecRadford,andIlyaSutskever.2019.Generatinglongsequenceswithsparsetransformers.
arXivpreprintarXiv:1904.10509(2019).
[66] KrishnaTejaChitty-Venkata,SiddhisanketRaskar,BharatKale,FarahFerdaus,AdityaTanikanti,KenRaffenetti,
ValerieTaylor,MuraliEmani,andVenkatramVishwanath.2024.LLM-Inference-Bench:InferenceBenchmarkingof
LargeLanguageModelsonAIAccelerators.InWorkshopsofSC2024.1362–1379.
[67] JaewanChoi,HailongLi,ByeonghoKim,SeunghwanHwang,andJungHoAhn.2022. Acceleratingtransformer
networksthroughrecomposingsoftmaxlayers.InIISWC2022.92–103.
[68] AakankshaChowdhery,SharanNarang,JacobDevlin,MaartenBosma,GauravMishra,AdamRoberts,PaulBarham,
HyungWonChung,CharlesSutton,SebastianGehrmann,etal.2022.Palm:Scalinglanguagemodelingwithpathways.
arXivpreprintarXiv:2204.02311(2022).
[69] Jacob K Christopher, Brian R Bartoldson, Tal Ben-Nun, Michael Cardei, Bhavya Kailkhura, and Ferdinando
Fioretto.2024.Speculativediffusiondecoding:Acceleratinglanguagegenerationthroughdiffusion.arXivpreprint
arXiv:2408.05636(2024).
[70] GonçaloMCorreia,VladNiculae,andAndréFTMartins.2019.AdaptivelySparseTransformers.InProc.ofEMNLP-

## Ijcnlp2019.

[71] RóbertCsordás,PiotrPiękos,andKazukiIrie.2023.SwitchHead:AcceleratingTransformerswithMixture-of-Experts
Attention.arXivpreprintarXiv:2312.07987(2023).
[72] FahimDalvi,MaramHasanain,SabriBoughorbel,BaselMousi,SamirAbdaljalil,NiziNazar,AhmedAbdelali,
ShammurAbsarChowdhury,HamdyMubarak,AhmedAli,etal.2023. LLMeBench:AFlexibleFrameworkfor
AcceleratingLLMsBenchmarking.arXivpreprintarXiv:2308.04945(2023).
[73] Databricks.2023.LLMInferencePerformanceEngineering:BestPractices. https://www.databricks.com/blog/llminference-performance-engineering-best-practicesAccessedon:2023-11-25.
ManuscriptsubmittedtoACMComput.Surv..Submissiondate:January2025.

<!-- Page 24 -->

1:24 Miao,etal.
[74] YannNDauphin,AngelaFan,MichaelAuli,andDavidGrangier.2017.Languagemodelingwithgatedconvolutional
networks.InProc.ofICML.933–941.
[75] DeciAI.2023.DeciLM6B. [https://huggingface.co/Deci/DeciLM-6b](https://huggingface.co/Deci/DeciLM-6b)
[76] LucianoDelCorro,AllieDelGiorno,SahajAgarwal,BinYu,AhmedAwadallah,andSubhabrataMukherjee.2023.
SkipDecode:AutoregressiveSkipDecodingwithBatchingandCachingforEfficientLLMInference.arXivpreprint
arXiv:2307.02628(2023).
[77] TimDettmers,MikeLewis,YounesBelkada,andLukeZettlemoyer.2022.LLM.int8():8-bitMatrixMultiplicationfor
TransformersatScale.arXivpreprintarXiv:2208.07339(2022).
[78] TimDettmers,ArtidoroPagnoni,AriHoltzman,andLukeZettlemoyer.2023.Qlora:Efficientfinetuningofquantized
llms.arXivpreprintarXiv:2305.14314(2023).
[79] TimDettmers,RuslanSvirschevski,VageEgiazarian,DenisKuznedelev,EliasFrantar,SalehAshkboos,Alexander
Borzunov,TorstenHoefler,andDanAlistarh.2023.SpQR:ASparse-QuantizedRepresentationforNear-LosslessLLM
WeightCompression.arXivpreprintarXiv:2306.03078(2023).
[80] TimDettmersandLukeZettlemoyer.2023.Thecasefor4-bitprecision:k-bitInferenceScalingLaws.InICLR2023.
[81] NolanDey,GurpreetGosal,HemantKhachane,WilliamMarshall,RibhuPathria,MarvinTom,JoelHestness,etal.

## Cerebras-GPT:Opencompute-optimallanguagemodelstrainedontheCerebraswafer-scalecluster. arXiv

preprintarXiv:2304.03208(2023).
[82] JiayuDing,ShumingMa,LiDong,XingxingZhang,ShaohanHuang,WenhuiWang,andFuruWei.2023.Longnet:
Scalingtransformersto1,000,000,000tokens.arXivpreprintarXiv:2307.02486(2023).
[83] JuechuDong,BoyuanFeng,DrissGuessous,YanboLiang,andHoraceHe.2024. FlexAttention:AProgramming
ModelforGeneratingOptimizedAttentionKernels.arXivpreprintarXiv:2412.05496(2024).
[84] XinLunaDong,SeungwhanMoon,YifanEthanXu,KshitizMalik,andZhouYu.2023.TowardsNext-Generation
IntelligentAssistantsLeveragingLLMTechniques.InProc.ofKDD.5792–5793.
[85] YixinDong,CharlieFRuan,YaxingCai,RuihangLai,ZiyiXu,YilongZhao,andTianqiChen.2024. Xgrammar:
Flexibleandefficientstructuredgenerationengineforlargelanguagemodels.arXivpreprintarXiv:2411.15100(2024).
[86] JiangsuDu,JiazhiJiang,JiangZheng,HongbinZhang,DanHuang,andYutongLu.2023.ImprovingComputation
andMemoryEfficiencyforReal-worldTransformerInferenceonGPUs.ACMTACO(2023),1–22.
[87] NanDu,YanpingHuang,AndrewMDai,SimonTong,DmitryLepikhin,YuanzhongXu,MaximKrikun,YanqiZhou,
etal.2022.Glam:Efficientscalingoflanguagemodelswithmixture-of-experts.InProc.ofICML2022.5547–5569.
[88] MuraliEmani,SamForeman,VaruniSastry,ZhenXie,SiddhisanketRaskar,WilliamArnold,RajeevThakur,Venkatram
Vishwanath,andMichaelEPapka.2023.AComprehensivePerformanceStudyofLargeLanguageModelsonNovel
AIAccelerators.arXivpreprintarXiv:2310.04607(2023).
[89] AhmadFaiz,SotaroKaneda,RuhanWang,RitaOsi,ParteekSharma,FanChen,andLeiJiang.2023. LLMCarbon:
Modelingtheend-to-endCarbonFootprintofLargeLanguageModels.arXivpreprintarXiv:2309.14393(2023).
[90] AngelaFan,EdouardGrave,andArmandJoulin.2019.ReducingTransformerDepthonDemandwithStructured
Dropout.InProc.ofICLR2019.
[91] JiaruiFang,YangYu,ChengduoZhao,andJieZhou.2021.Turbotransformers:anefficientgpuservingsystemfor
transformermodels.InProc.ofPPoPP2021.389–402.
[92] WilliamFedus,BarretZoph,andNoamShazeer.2022.Switchtransformers:Scalingtotrillionparametermodelswith
simpleandefficientsparsity.TheJournalofMachineLearningResearch(2022),5232–5270.
[93] PratikFegade,TianqiChen,PhillipGibbons,andToddMowry.2022. TheCoRatensorcompiler:Compilationfor
raggedtensorswithminimalpadding.ProceedingsofMachineLearningandSystems(2022),721–747.
[94] WeizhiFei,XueyanNiu,PingyiZhou,LuHou,BoBai,LeiDeng,andWeiHan.2023.ExtendingContextWindowof
LargeLanguageModelsviaSemanticCompression.arXivpreprintarXiv:2312.09571(2023).
[95] SiyuanFeng,BohanHou,HongyiJin,WuweiLin,JunruShao,RuihangLai,ZihaoYe,LianminZheng,etal.2023.
Tensorir:Anabstractionforautomatictensorizedprogramoptimization.InProc.ofASPLOS2023.804–817.
[96] EliasFrantarandDanAlistarh.2023.SparseGPT:MassiveLanguageModelsCanBeAccuratelyPrunedinOne-Shot.
InProc.ofICML2023.10323–10337.
[97] EliasFrantar,SalehAshkboos,TorstenHoefler,andDanAlistarh.2022.Gptq:Accuratepost-trainingquantizationfor
generativepre-trainedtransformers.arXivpreprintarXiv:2210.17323(2022).
[98] EliasFrantar,SalehAshkboos,TorstenHoefler,andDanAlistarh.2022.OPTQ:Accuratequantizationforgenerative
pre-trainedtransformers.InProc.ofICLR2022.
[99] RoyFrostig,MatthewJamesJohnson,andChrisLeary.2018.Compilingmachinelearningprogramsviahigh-level
tracing.SystemsforMachineLearning(2018).
[100] DanielYFu,TriDao,KhaledKamalSaab,ArminWThomas,AtriRudra,andChristopherRe.2022.HungryHungry
Hippos:TowardsLanguageModelingwithStateSpaceModels.InProc.ofICLR2022.
ManuscriptsubmittedtoACMComput.Surv..Submissiondate:January2025.

<!-- Page 25 -->

TowardsEfficientGenerativeLargeLanguageModelServing:ASurveyfromAlgorithmstoSystems 1:25
[101] YichaoFu,PeterBailis,IonStoica,andHaoZhang.2024.BreakthesequentialdependencyofLLMinferenceusing
LOOKAHEADDECODING.InProc.ofICML2024.14060–14079.
[102] YichaoFu,JundaChen,SiqiZhu,ZheyuFu,ZhongdongmingDai,AurickQiao,andHaoZhang.2024. Efficiently
ServingLLMReasoningProgramswithCertaindex.arXivpreprintarXiv:2412.20993(2024).
[103] YaoFu,LeyangXue,YeqiHuang,Andrei-OctavianBrabete,DmitriiUstiugov,YuvrajPatel,andLuoMai.2024.
ServerlessLLM:Low-Latencyserverlessinferenceforlargelanguagemodels.InProc.ofOSDI2024.135–153.
[104] TrevorGale,DeepakNarayanan,CliffYoung,andMateiZaharia.2023.MegaBlocks:EfficientSparseTrainingwith
Mixture-of-Experts.ProceedingsofMachineLearningandSystems(2023).
[105] BinGao,ZhuominHe,PuruSharma,QingxuanKang,DjordjeJevdjic,JunboDeng,XingkunYang,ZhouYu,and
PengfeiZuo.2024.Cost-Efficientlargelanguagemodelservingformulti-turnconversationswithCachedAttention.
InProc.ofUSENIXATC2024.111–126.
[106] ShiweiGao,YouminChen,andJiwuShu.2025.FaststaterestorationinLLMservingwithhcache.InEuroSys2025.
[107] SuyuGe,YunanZhang,LiyuanLiu,MinjiaZhang,JiaweiHan,andJianfengGao.2023. ModelTellsYouWhatto
Discard:AdaptiveKVCacheCompressionforLLMs.InWANT@NeurIPS2023.
[108] TaoGe,JingHu,XunWang,Si-QingChen,andFuruWei.2023.In-contextautoencoderforcontextcompressionina
largelanguagemodel.arXivpreprintarXiv:2307.06945(2023).
[109] TaoGe,HemingXia,XinSun,Si-QingChen,andFuruWei.2022.LosslessaccelerationforSeq2seqgenerationwith
aggressivedecoding.arXivpreprintarXiv:2205.10350(2022).
[110] MarjanGhazvininejad,OmerLevy,YinhanLiu,andLukeZettlemoyer.2019. Mask-Predict:ParallelDecodingof
ConditionalMaskedLanguageModels.InEMNLP-IJCNLP2019.6112–6121.
[111] MarjanGhazvininejad,OmerLevy,andLukeZettlemoyer.2020.Semi-autoregressivetrainingimprovesmask-predict
decoding.arXivpreprintarXiv:2001.08785(2020).
[112] AmirGholami,SehoonKim,ZhenDong,ZheweiYao,MichaelWMahoney,andKurtKeutzer.2022. Asurveyof
quantizationmethodsforefficientneuralnetworkinference.InLow-PowerComputerVision.291–326.
[113] InGim,GuojunChen,Seung-seobLee,NikhilSarda,AnuragKhandelwal,andLinZhong.2023. PromptCache:
ModularAttentionReuseforLow-LatencyInference.arXivpreprintarXiv:2311.04934(2023).
[114] SaurabhGoyal,AnamitraRoyChoudhury,SaurabhRaje,VenkatesanChakaravarthy,YogishSabharwal,andAshish
Verma.2020.PoWER-BERT:AcceleratingBERTinferenceviaprogressiveword-vectorelimination.InICML2020.
[115] AlbertGuandTriDao.2023.Mamba:Linear-TimeSequenceModelingwithSelectiveStateSpaces.InCOLM2024.
[116] AlbertGu,KaranGoel,andChristopherRe.2021.EfficientlyModelingLongSequenceswithStructuredStateSpaces.
InProc.ofICLR2021.
[117] JGu,JBradbury,CXiong,VOKLi,andRSocher.2018.Non-autoregressiveneuralmachinetranslation.InICLR2018.
[118] JiataoGuandXiangKong.2021.FullyNon-autoregressiveNeuralMachineTranslation:TricksoftheTrade.InProc.
ofACLFindings.120–133.
[119] YuxianGu,LiDong,FuruWei,andMinlieHuang.2024.MiniLLM:KnowledgeDistillationofLargeLanguageModels.
InProc.ofICLR2024.
[120] JashwantRajGunasekaran,CyanSubhraMishra,PrashanthThinakaran,BikashSharma,MahmutTaylanKandemir,
andChitaRDas.2022.Cocktail:Amultidimensionaloptimizationformodelservingincloud.InProc.ofNSDI2022.
1041–1057.
[121] DayaGuo,DejianYang,HaoweiZhang,JunxiaoSong,RuoyuZhang,RunxinXu,QihaoZhu,ShirongMa,PeiyiWang,
XiaoBi,etal.2025.Deepseek-r1:Incentivizingreasoningcapabilityinllmsviareinforcementlearning.arXivpreprint
arXiv:2501.12948(2025).
[122] JunliangGuo,XuTan,DiHe,TaoQin,LinliXu,andTie-YanLiu.2019.Non-autoregressiveneuralmachinetranslation
withenhanceddecoderinput.InProc.ofAAAI.3723–3730.
[123] LiweiGuo,WonkyoChoe,andFelixXiaozhuLin.2023. STI:TurbochargeNLPInferenceattheEdgeviaElastic
Pipelining.InProc.ofASPLOS.791–803.
[124] QipengGuo,XipengQiu,PengfeiLiu,YunfanShao,XiangyangXue,andZhengZhang.2019.Star-Transformer.In
Proc.ofNAACL-HLT.1315–1325.
[125] AnkitGuptaandJonathanBerant.2020. Gmat:Globalmemoryaugmentationfortransformers. arXivpreprint
arXiv:2006.03274(2020).
[126] AnkitGupta,GuyDar,ShayaGoodman,DavidCiprut,andJonathanBerant.2021.Memory-efficientTransformersvia
Top-kAttention.InProceedingsoftheSecondWorkshoponSimpleandEfficientNaturalLanguageProcessing.39–52.
[127] ManishGuptaandPuneetAgrawal.2022.Compressionofdeeplearningmodelsfortext:Asurvey.ACMTransactions
onKnowledgeDiscoveryfromData(TKDD)(2022),1–55.
[128] MingcongHan,HanzeZhang,RongChen,andHaiboChen.2022. Microsecond-scalepreemptionforconcurrent
GPU-acceleratedDNNinferences.InProc.ofOSDI2022.539–558.
[129] BobbyHeandThomasHofmann.2023.SimplifyingTransformerBlocks.arXivpreprintarXiv:2311.01906(2023).
ManuscriptsubmittedtoACMComput.Surv..Submissiondate:January2025.

<!-- Page 26 -->

1:26 Miao,etal.
[130] JiaaoHe,JidongZhai,TiagoAntunes,HaojieWang,FuwenLuo,ShangfengShi,andQinLi.2022.FasterMoE:modeling
andoptimizingtrainingoflarge-scaledynamicpre-trainedmodels.InProc.ofPPoPP2022.120–134.
[131] XuanliHe,ImanKeivanloo,YiXu,XiangHe,BelindaZeng,SantoshRajagopalan,andTrishulChilimbi.2021.Magic
pyramid:Acceleratinginferencewithearlyexitingandtokenpruning.arXivpreprintarXiv:2111.00230(2021).
[132] ZhenyuHe,ZexuanZhong,TianleCai,JasonDLee,andDiHe.2023.REST:Retrieval-BasedSpeculativeDecoding.
arXivpreprintarXiv:2311.08252(2023).
[133] KeHong,GuohaoDai,JiamingXu,QiuliMao,XiuhongLi,JunLiu,KangdiChen,HanyuDong,andYuWang.2023.
FlashDecoding++:FasterLargeLanguageModelInferenceonGPUs.arXivpreprintarXiv:2311.01282(2023).
[134] ColemanHooper,SehoonKim,HivaMohammadzadeh,HasanGenc,KurtKeutzer,AmirGholami,andSophiaShao.

#### SPEED:SpeculativePipelinedExecutionforEfficientDecoding.arXivpreprintarXiv:2310.12072(2023).

[135] CunchenHu,HeyangHuang,LiangliangXu,XushengChen,JiangXu,ShuangChen,HaoFeng,ChenxiWang,Sa
Wang,YungangBao,etal.2024.Inferencewithoutinterference:Disaggregatellminferenceformixeddownstream
workloads.arXivpreprintarXiv:2401.11181(2024).
[136] HaiyangHuang,NewshaArdalani,AnnaSun,LiuKe,Hsien-HsinSLee,AnjaliSridhar,ShrutiBhosale,Carole-Jean
Wu,andBenjaminLee.2023. TowardsMoEDeployment:MitigatingInefficienciesinMixture-of-Expert(MoE)
Inference.arXivpreprintarXiv:2303.06182(2023).
[137] KaiyuHuang,HaoWu,ZhuboShi,HanZou,MinchenYu,andQingjiangShi.2025.SpecServe:EfficientandSLO-Aware
LargeLanguageModelServingwithAdaptiveSpeculativeDecoding.arXivpreprintarXiv:2503.05096(2025).
[138] ChanghoHwang,WeiCui,YifanXiong,ZiyueYang,ZeLiu,HanHu,ZilongWang,RafaelSalas,JithinJose,Prabhat
Ram,etal.2023.Tutel:Adaptivemixture-of-expertsatscale.ProceedingsofMachineLearningandSystems(2023).
[139] RégisPierrardIlyasMoutawwakil.2023.LLM-PerfLeaderboard.https://huggingface.co/spaces/optimum/llm-perfleaderboard.
[140] MikhailIsaev,NicMcdonald,LarryDennison,andRichardVuduc.2023. Calculon:amethodologyandtoolfor
high-levelco-designofsystemsandlargelanguagemodels.InProc.ofSC2023.1–14.
[141] BerivanIsik,HermannKumbong,WanyiNing,XiaozheYao,SanmiKoyejo,andCeZhang.2023. GPT-Zip:Deep
CompressionofFinetunedLargeLanguageModels.InWorkshoponEfficientSystemsforFoundationModels@ICML2023.
[142] SamAdeJacobs,MasahiroTanaka,ChengmingZhang,MinjiaZhang,ShuaiwenLeonSong,SamyamRajbhandari,
andYuxiongHe.2023. Deepspeedulysses:Systemoptimizationsforenablingtrainingofextremelongsequence
transformermodels.arXivpreprintarXiv:2309.14509(2023).
[143] AjayJaiswal,ZheGan,XianzhiDu,BowenZhang,ZhangyangWang,andYinfeiYang.2023.CompressingLLMs:The
TruthisRarelyPureandNeverSimple.arXivpreprintarXiv:2310.01382(2023).
[144] DoohyukJang,SihwanPark,JuneYongYang,YeonsungJung,JihunYun,SouvikKundu,Sung-YubKim,andEunho
Yang.2024.LANTERN:AcceleratingVisualAutoregressiveModelswithRelaxedSpeculativeDecoding.InProc.of

## Iclr2024.

[145] ByungsooJeon,MengdiWu,ShiyiCao,SunghyunKim,SunghyunPark,NeerajAggarwal,ColinUnger,Daiyaan
Arfeen,PeiyuanLiao,XupengMiao,etal.2025.GraphPipe:ImprovingPerformanceandScalabilityofDNNTraining
withGraphPipelineParallelism.InProc.ofASPLOS2025.557–571.
[146] ZhihaoJia,OdedPadon,JamesThomas,ToddWarszawski,MateiZaharia,andAlexAiken.2019.TASO:optimizing
deeplearningcomputationwithautomaticgenerationofgraphsubstitutions.InProc.ofSOSP2019.47–62.
[147] ZhihaoJia,MateiZaharia,andAlexAiken.2019. BeyondDataandModelParallelismforDeepNeuralNetworks.
ProceedingsofMachineLearningandSystems(2019),1–13.
[148] AlbertQJiang,AlexandreSablayrolles,ArthurMensch,ChrisBamford,DevendraSinghChaplot,Diegodelas
Casas,FlorianBressand,GiannaLengyel,GuillaumeLample,LucileSaulnier,etal.2023.Mistral7B.arXivpreprint
arXiv:2310.06825(2023).
[149] HuiqiangJiang,QianhuiWu,Chin-YewLin,YuqingYang,andLiliQiu.2023.Llmlingua:Compressingpromptsfor
acceleratedinferenceoflargelanguagemodels.arXivpreprintarXiv:2310.05736(2023).
[150] HuiqiangJiang,QianhuiWu,XufangLuo,DongshengLi,Chin-YewLin,YuqingYang,andLiliQiu.2024.LongLLM-
Lingua:AcceleratingandEnhancingLLMsinLongContextScenariosviaPromptCompression.InACL2024.
[151] YouheJiang,FangchengFu,XiaozheYao,GuoliangHe,XupengMiao,AnaKlimovic,BinCui,BinhangYuan,andEiko
Yoneki.2025.DemystifyingCost-EfficiencyinLLMServingoverHeterogeneousGPUs.arXivpreprintarXiv:2502.00722
(2025).
[152] YouheJiang,RanYan,XiaozheYao,BeidiChen,andBinhangYuan.2023.HexGen:GenerativeInferenceofFoundation
ModeloverHeterogeneousDecentralizedEnvironment.arXivpreprintarXiv:2311.11514(2023).
[153] XiaoqiJiao,YichunYin,LifengShang,XinJiang,XiaoChen,LinlinLi,FangWang,andQunLiu.2020.TinyBERT:
DistillingBERTforNaturalLanguageUnderstanding.InProc.ofEMNLPFindings.4163–4174.
[154] HongyiJin,RuihangLai,CharlieFRuan,YingchengWang,ToddCMowry,XupengMiao,ZhihaoJia,andTianqi
Chen.2024.ASystemforMicroservingofLLMs.arXivpreprintarXiv:2412.12488(2024).
ManuscriptsubmittedtoACMComput.Surv..Submissiondate:January2025.

<!-- Page 27 -->

TowardsEfficientGenerativeLargeLanguageModelServing:ASurveyfromAlgorithmstoSystems 1:27
[155] YunhoJin,Chun-FengWu,DavidBrooks,andGu-YeonWei.2023.S3:IncreasingGPUUtilizationduringGenerative
InferenceforHigherThroughput.arXivpreprintarXiv:2306.06000(2023).
[156] AJo.2023.ThepromiseandperilofgenerativeAI.Nature(2023),214–216.
[157] NormJouppi,GeorgeKurian,ShengLi,PeterMa,RahulNagarajan,LifengNai,NishantPatil,SuvinaySubramanian,
AndySwing,BrianTowles,etal.2023.Tpuv4:Anopticallyreconfigurablesupercomputerformachinelearningwith
hardwaresupportforembeddings.InProc.ofISCA2023.1–14.
[158] JungoKasai,NikolaosPappas,HaoPeng,JamesCross,andNoahSmith.2020. DeepEncoder,ShallowDecoder:
ReevaluatingNon-autoregressiveMachineTranslation.InProc.ofICLR2020.
[159] NavdeepKatel,VivekKhandelwal,andUdayBondhugula.2022.MLIR-basedcodegenerationforGPUtensorcores.
InProceedingsofthe31stACMSIGPLANInternationalConferenceonCompilerConstruction.117–128.
[160] AngelosKatharopoulos,ApoorvVyas,NikolaosPappas,andFrançoisFleuret.2020. Transformersarernns:Fast
autoregressivetransformerswithlinearattention.InProc.ofICML2020.5156–5165.
[161] UrvashiKhandelwal,HeHe,PengQi,andDanJurafsky.2018.SharpNearby,FuzzyFarAway:HowNeuralLanguage
ModelsUseContext.InProc.ofACL2018.284–294.
[162] JeonghoonKim,JungHyunLee,SungdongKim,JoonsukPark,KangMinYoo,SeJungKwon,andDongsooLee.2023.
Memory-EfficientFine-TuningofCompressedLargeLanguageModelsviasub-4-bitIntegerQuantization. arXiv
preprintarXiv:2305.14152(2023).
[163] SehoonKim,ColemanHooper,AmirGholami,ZhenDong,XiuyuLi,ShengShen,MichaelWMahoney,andKurt
Keutzer.2023.SqueezeLLM:Dense-and-SparseQuantization.arXivpreprintarXiv:2306.07629(2023).
[164] SehoonKim,ColemanHooper,ThanakulWattanawong,MinwooKang,RuohanYan,HasanGenc,GraceDinh,Qijing
Huang,KurtKeutzer,MichaelWMahoney,etal.2023.Fullstackoptimizationoftransformerinference:asurvey.
arXivpreprintarXiv:2302.14017(2023).
[165] SehoonKim,KarttikeyaMangalam,JitendraMalik,MichaelWMahoney,AmirGholami,andKurtKeutzer.2023.Big
littletransformerdecoder.arXivpreprintarXiv:2302.07863(2023).
[166] NikitaKitaev,LukaszKaiser,andAnselmLevskaya.2019.Reformer:TheEfficientTransformer.InProc.ofICLR2019.
[167] JunKong,JinWang,Liang-ChihYu,andXuejieZhang.2022.AcceleratingInferenceforPretrainedLanguageModels
byUnifiedMulti-PerspectiveEarlyExiting.InProc.ofCOLING.4677–4686.
[168] VijayAnandKorthikanti,JaredCasper,SangkugLym,LawrenceMcAfee,MichaelAndersch,MohammadShoeybi,
andBryanCatanzaro.2023.Reducingactivationrecomputationinlargetransformermodels.ProceedingsofMachine
LearningandSystems(2023),341–353.
[169] SnehaKudugunta,YanpingHuang,AnkurBapna,MaximKrikun,DmitryLepikhin,Minh-ThangLuong,andOrhan
Firat.2021.BeyondDistillation:Task-levelMixture-of-ExpertsforEfficientInference.InProc.ofEMNLPFindings.
3577–3599.
[170] EldarKurtic,EliasFrantar,andDanAlistarh.2023.Ziplm:Hardware-awarestructuredpruningoflanguagemodels.
arXivpreprintarXiv:2302.04089(2023).
[171] WoosukKwon,ZhuohanLi,SiyuanZhuang,YingSheng,LianminZheng,CodyHaoYu,JosephGonzalez,HaoZhang,
andIonStoica.2023.EfficientMemoryManagementforLargeLanguageModelServingwithPagedAttention.InProc.
ofSOSP2023.611–626.
[172] RuihangLai,JunruShao,SiyuanFeng,StevenSLyubomirsky,BohanHou,WuweiLin,ZihaoYe,HongyiJin,etal.

#### Relax:ComposableAbstractionsforEnd-to-EndDynamicMachineLearning.InProc.ofASPLOS2025.

[173] JasonLee,ElmanMansimov,andKyunghyunCho.2018.DeterministicNon-AutoregressiveNeuralSequenceModeling
byIterativeRefinement.InProc.ofEMNLP2018.
[174] WonbeomLee,JungiLee,JunghwanSeo,andJaewoongSim.2024.InfiniGen:Efficientgenerativeinferenceoflarge
languagemodelswithdynamicKVcachemanagement.InProc.ofOSDI2024.155–172.
[175] BenjaminLefaudeux,FranciscoMassa,DianaLiskovich,WenhanXiong,VittorioCaggiano,SeanNaren,MinXu,
JieruHu,MartaTintore,SusanZhang,PatrickLabatut,andDanielHaziza.2022.xFormers:Amodularandhackable
Transformermodellinglibrary. https://github.com/facebookresearch/xformers. Commit:fbf349a,Accessedon:
2023-11-25.
[176] DmitryLepikhin,HyoukJoongLee,YuanzhongXu,DehaoChen,OrhanFirat,YanpingHuang,MaximKrikun,Noam
Shazeer,andZhifengChen.2020. GShard:ScalingGiantModelswithConditionalComputationandAutomatic
Sharding.InProc.ofICLR2020.
[177] YanivLeviathan,MatanKalman,andYossiMatias.2023.Fastinferencefromtransformersviaspeculativedecoding.
InProc.ofICML2023.19274–19286.
[178] JiaminLi,YiminJiang,YiboZhu,CongWang,andHongXu.2023. AcceleratingDistributedMoETrainingand
InferencewithLina.InProc.ofUSENIXATC2023.945–959.
[179] LeiLi,YankaiLin,DeliChen,ShuhuaiRen,PengLi,JieZhou,andXuSun.2020.Cascadebert:Acceleratinginference
ofpre-trainedlanguagemodelsviacalibratedcompletemodelscascade.arXivpreprintarXiv:2012.14682(2020).
ManuscriptsubmittedtoACMComput.Surv..Submissiondate:January2025.

<!-- Page 28 -->

1:28 Miao,etal.
[180] QingyuanLi,RanMeng,YiduoLi,BoZhang,LiangLi,YifanLu,XiangxiangChu,YeruiSun,andYuchenXie.2023.A
SpeedOdysseyforDeployableQuantizationofLLMs.arXivpreprintarXiv:2311.09550(2023).
[181] YuchengLi,BoDong,FrankGuerin,andChenghuaLin.2023.CompressingContexttoEnhanceInferenceEfficiency
ofLargeLanguageModels.InProc.ofEMNLP2023.6342–6353.
[182] YanyangLi,YeLin,TongXiao,andJingboZhu.2021.Anefficienttransformerdecoderwithcompressedsub-layers.
InProc.ofAAAI2021.13315–13323.
[183] YuhuiLi,FangyunWei,ChaoZhang,andHongyangZhang.2024.EAGLE:speculativesamplingrequiresrethinking
featureuncertainty.InProc.ofICML2024.28935–28948.
[184] YixiaoLi,YifanYu,QingruZhang,ChenLiang,PengchengHe,WeizhuChen,andTuoZhao.2023. LoSparse:
StructuredCompressionofLargeLanguageModelsbasedonLow-RankandSparseApproximation.InICML2023.
[185] ZikunLi,ZhuofuChen,RemiDelacourt,GabrieleOliaro,ZeyuWang,QinghanChen,ShuhuaiLin,AprilYang,
ZhihaoZhang,ZhuomingChen,etal.2025.AdaServe:SLO-CustomizedLLMServingwithFine-GrainedSpeculative
Decoding.arXivpreprintarXiv:2501.12162(2025).
[186] ZhuohanLi,LianminZheng,YinminZhong,VincentLiu,YingSheng,XinJin,YanpingHuang,ZhifengChen,Hao
Zhang,JosephEGonzalez,etal.2023.AlpaServe:StatisticalMultiplexingwithModelParallelismforDeepLearning
Serving.InProc.ofOSDI2023.663–679.
[187] KaiyuanLiao,YiZhang,XuanchengRen,QiSu,XuSun,andBinHe.2021.Aglobalpast-futureearlyexitmethodfor
acceleratinginferenceofpre-trainedlanguagemodels.InProc.ofNAACL2021.2013–2023.
[188] ChaofanLin,ZhenhuaHan,ChengruidongZhang,YuqingYang,FanYang,ChenChen,andLiliQiu.2024.Parrot:
EfficientServingofLLM-basedApplicationswithSemanticVariable.InProc.ofOSDI2024.929–945.
[189] JiLin,JiamingTang,HaotianTang,ShangYang,Wei-MingChen,Wei-ChenWang,GuangxuanXiao,XingyuDang,
ChuangGan,andSongHan.2024.Awq:Activation-awareweightquantizationforon-devicellmcompressionand
acceleration.ProceedingsofMachineLearningandSystems6(2024),87–100.
[190] AixinLiu,BeiFeng,BinWang,BingxuanWang,BoLiu,ChenggangZhao,ChengqiDengr,ChongRuan,DamaiDai,
DayaGuo,etal.2024.Deepseek-v2:Astrong,economical,andefficientmixture-of-expertslanguagemodel.arXiv
preprintarXiv:2405.04434(2024).
[191] FangchengLiu,YehuiTang,ZhenhuaLiu,YunshengNi,DuyuTang,KaiHan,andYunheWang.2024. Kangaroo:
Losslessself-speculativedecodingforacceleratingLLMsviadoubleearlyexiting.Proc.ofNeurIPS(2024),11946–11965.
[192] HaoLiu,MateiZaharia,andPieterAbbeel.2023. RingAttentionwithBlockwiseTransformersforNear-Infinite
Context.arXivpreprintarXiv:2310.01889(2023).
[193] JingyuLiu,BeidiChen,andCeZhang.2025.SpeculativePrefill:TurbochargingTTFTwithLightweightandTraining-
FreeTokenImportanceEstimation.arXivpreprintarXiv:2502.02789(2025).
[194] JiachenLiu,Jae-WonChung,ZhiyuWu,FanLai,MyungjinLee,andMosharafChowdhury.2024.Andes:Defining
andenhancingquality-of-experienceinllm-basedtextstreamingservices.arXivpreprintarXiv:2404.16283(2024).
[195] NelsonFLiu,KevinLin,JohnHewitt,AshwinParanjape,MicheleBevilacqua,FabioPetroni,andPercyLiang.2023.
Lostinthemiddle:Howlanguagemodelsuselongcontexts.arXivpreprintarXiv:2307.03172(2023).
[196] WeijieLiu,PengZhou,ZhiruoWang,ZheZhao,HaotangDeng,andQiJu.2020.FastBERT:aSelf-distillingBERT
withAdaptiveInferenceTime.InProc.ofACL2020.6035–6044.
[197] XiaoxuanLiu,LanxiangHu,PeterBailis,IonStoica,ZhijieDeng,AlvinCheung,andHaoZhang.2023. Online
SpeculativeDecoding.arXivpreprintarXiv:2310.07177(2023).
[198] YuhanLiu,HanchenLi,KuntaiDu,JiayiYao,YihuaCheng,YuyangHuang,ShanLu,MichaelMaire,HenryHoffmann,
AriHoltzman,etal.2024.CacheGen:FastContextLoadingforLanguageModelApplications.InSIGCOMM2024.
[199] ZichangLiu,AdityaDesai,FangshuoLiao,WeitaoWang,VictorXie,ZhaozhuoXu,AnastasiosKyrillidis,and
AnshumaliShrivastava.2023.Scissorhands:ExploitingthePersistenceofImportanceHypothesisforLLMKVCache
CompressionatTestTime.arXivpreprintarXiv:2305.17118(2023).
[200] ZechunLiu,BarlasOguz,ChangshengZhao,ErnieChang,PierreStock,YasharMehdad,YangyangShi,Raghuraman
Krishnamoorthi,andVikasChandra.2023.LLM-QAT:Data-FreeQuantizationAwareTrainingforLargeLanguage
Models.arXivpreprintarXiv:2305.17888(2023).
[201] ZichangLiu,JueWang,TriDao,TianyiZhou,BinhangYuan,ZhaoSong,AnshumaliShrivastava,CeZhang,Yuandong
Tian,ChristopherRe,etal.2023.Dejavu:Contextualsparsityforefficientllmsatinferencetime.InICML2023.
[202] Wen-jieLu,ZhicongHuang,ZhenGu,JingyuLi,JianLiu,KuiRen,ChengHong,TaoWei,andWenGuangChen.

#### BumbleBee:SecureTwo-partyInferenceFrameworkforLargeTransformers.CryptologyePrintArchive(2023).

[203] XinyinMa,GongfanFang,andXinchaoWang.2023. LLM-Pruner:OntheStructuralPruningofLargeLanguage
Models.arXivpreprintarXiv:2305.11627(2023).
[204] ZimingMao,TianXia,ZhanghaoWu,Wei-LinChiang,TylerGriggs,RomilBhardwaj,ZonghengYang,ScottShenker,
andIonStoica.2024. Skyserve:Servingaimodelsacrossregionsandcloudswithspotinstances. arXivpreprint
arXiv:2411.01438(2024).
ManuscriptsubmittedtoACMComput.Surv..Submissiondate:January2025.

<!-- Page 29 -->

TowardsEfficientGenerativeLargeLanguageModelServing:ASurveyfromAlgorithmstoSystems 1:29
[205] RubenMayerandHans-ArnoJacobsen.2020. Scalabledeeplearningondistributedinfrastructures:Challenges,
techniques,andtools.ACMComputingSurveys(CSUR)(2020),1–37.
[206] HarshMehta,AnkitGupta,AshokCutkosky,andBehnamNeyshabur.2022. LongRangeLanguageModelingvia
GatedStateSpaces.InProc.ofICLR2022.
[207] YixuanMei,YonghaoZhuang,XupengMiao,JunchengYang,ZhihaoJia,andRashmiVinayak.2025.Helix:Serving
LargeLanguageModelsoverHeterogeneousGPUsandNetworkviaMax-Flow.InProc.ofASPLOS2025.586–602.
[208] ZhiyuMei,WeiFu,KaiweiLi,GuangjuWang,HuanchenZhang,andYiWu.2024.Realhf:Optimizedrlhftrainingfor
largelanguagemodelsthroughparameterreallocation.arXivpreprintarXiv:2406.14088(2024).
[209] XupengMiao,ZhihaoJia,andBinCui.2024.Demystifyingdatamanagementforlargelanguagemodels.InCompanion
ofthe2024InternationalConferenceonManagementofData.547–555.
[210] XupengMiao,GabrieleOliaro,XinhaoCheng,MengdiWu,ColinUnger,andZhihaoJia.2024.FlexLLM:ASystem
forCo-ServingLargeLanguageModelInferenceandParameter-EfficientFinetuning.arXivpreprintarXiv:2402.18789
(2024).
[211] XupengMiao,GabrieleOliaro,ZhihaoZhang,XinhaoCheng,etal.2024. Specinfer:Acceleratinglargelanguage
modelservingwithtree-basedspeculativeinferenceandverification.InProc.ofASPLOS2024.932–949.
[212] XupengMiao,ChunanShi,JiangfeiDuan,XiaoliXi,DahuaLin,BinCui,andZhihaoJia.2024.SpotServe:Serving
GenerativeLargeLanguageModelsonPreemptibleInstances.InProc.ofASPLOS2024.1112–1127.
[213] XupengMiao,YujieWang,YouheJiang,ChunanShi,XiaonanNie,HailinZhang,andBinCui.2023. Galvatron:
EfficientTransformerTrainingoverMultipleGPUsUsingAutomaticParallelism.Proc.VLDBEndow.(2023),470–479.
[214] PaulMichel,OmerLevy,andGrahamNeubig.2019.Aresixteenheadsreallybetterthanone?Proc.ofNeurIPS(2019).
[215] Maxim Milakov and Natalia Gimelshein. 2018. Online normalizer calculation for softmax. arXiv preprint
arXiv:1805.02867(2018).
[216] AsitMishra,JorgeAlbericioLatorre,JeffPool,DarkoStosic,DusanStosic,GaneshVenkatesh,ChongYu,andPaulius
Micikevicius.2021.Acceleratingsparsedeepneuralnetworks.arXivpreprintarXiv:2104.08378(2021).
[217] AliModarressi,HoseinMohebbi,andMohammadTaherPilehvar.2022.Adapler:Speedingupinferencebyadaptive
lengthreduction.arXivpreprintarXiv:2203.08991(2022).
[218] AmirkeivanMohtashamiandMartinJaggi.2023.LandmarkAttention:Random-AccessInfiniteContextLengthfor
Transformers.arXivpreprintarXiv:2305.16300(2023).
[219] GiovanniMonea,ArmandJoulin,andEdouardGrave.2023. PaSS:ParallelSpeculativeSampling. arXivpreprint
arXiv:2311.13581(2023).
[220] JesseMu,XiangLisaLi,andNoahGoodman.2023.Learningtocompresspromptswithgisttokens.InNeurIPS2023.
[221] DorMuhlgay,OriRam,InbalMagar,YoavLevine,NirRatner,YonatanBelinkov,OmriAbend,KevinLeyton-Brown,
AmnonShashua,andYoavShoham.2023. Generatingbenchmarksforfactualityevaluationoflanguagemodels.
arXivpreprintarXiv:2307.06908(2023).
[222] KabirNagrechaandArunKumar.2023.Saturn:AnOptimizedDataSystemforLargeModelDeepLearningWorkloads.
arXivpreprintarXiv:2309.01226(2023).
[223] DeepakNarayanan,AmarPhanishayee,KaiyuShi,XieChen,andMateiZaharia.2021.Memory-efficientpipelineparalleldnntraining.InProc.ofICML2021.7937–7947.
[224] DeepakNarayanan,KeshavSanthanam,PeterHenderson,RishiBommasani,TonyLee,andPercyLiang.2023.Cheaply
EstimatingInferenceEfficiencyMetricsforAutoregressiveTransformerModels.InProc.ofNeurIPS2023.
[225] KelvinKWNg,HenriMaximeDemoulin,andVincentLiu.2023.Paella:Low-latencyModelServingwithSoftwaredefinedGPUScheduling.InProc.ofSOSP2023.595–610.
[226] XiaonanNie,XupengMiao,ShijieCao,LingxiaoMa,QibinLiu,JilongXue,YoushanMiao,YiLiu,ZhiYang,andBin
Cui.2021.Evomoe:Anevolutionalmixture-of-expertstrainingframeworkviadense-to-sparsegate.arXivpreprint
arXiv:2112.14397(2021).
[227] XiaonanNie,XupengMiao,ZilongWang,ZichaoYang,JilongXue,LingxiaoMa,GangCao,andBinCui.2023.
FlexMoE:ScalingLarge-scaleSparsePre-trainedModelTrainingviaDynamicDevicePlacement.Proceedingsofthe
ACMonManagementofData(2023),1–19.
[228] HyungjunOh,KihongKim,JaeminKim,SungkyunKim,JunyeolLee,Du-seongChang,andJiwonSeo.2024.Exegpt:
Constraint-awareresourceschedulingforllminference.InProc.ofASPLOS2024.369–384.
[229] GabrieleOliaro,ZhihaoJia,DanielCampos,andAurickQiao.2024. SuffixDecoding:AModel-FreeApproachto
SpeedingUpLargeLanguageModelInference.arXivpreprintarXiv:2411.04975(2024).
[230] JunierBOliva,BarnabásPóczos,andJeffSchneider.2017.Thestatisticalrecurrentunit.InProc.ofICML.2671–2680.
[231] AntonioOrvieto,SamuelLSmith,AlbertGu,AnushanFernando,CaglarGulcehre,RazvanPascanu,andSohamDe.

#### Resurrectingrecurrentneuralnetworksforlongsequences.arXivpreprintarXiv:2303.06349(2023).

[232] CharlesPacker,VivianFang,ShishirGPatil,KevinLin,SarahWooders,andJosephEGonzalez.2023. MemGPT:
TowardsLLMsasOperatingSystems.arXivpreprintarXiv:2310.08560(2023).
ManuscriptsubmittedtoACMComput.Surv..Submissiondate:January2025.

<!-- Page 30 -->

1:30 Miao,etal.
[233] MatteoPagliardini,DanielePaliotta,MartinJaggi,andFrançoisFleuret.2023.FasterCausalAttentionOverLarge
SequencesThroughSparseFlashAttention.arXivpreprintarXiv:2306.01160(2023).
[234] RuiPan,ZhuangWang,ZhenJia,CanKarakus,LucaZancato,TriDao,YidaWang,andRaviNetravali.2024.Marconi:
Prefixcachingfortheeraofhybridllms.arXivpreprintarXiv:2411.19379(2024).
[235] GunhoPark,MinsubKim,SungjaeLee,JeonghoonKim,BeomseokKwon,SeJungKwon,ByeongwookKim,Youngjoo
Lee,DongsooLee,etal.2022.LUT-GEMM:QuantizedMatrixMultiplicationbasedonLUTsforEfficientInferencein
Large-ScaleGenerativeLanguageModels.InProc.ofICLR2022.
[236] PratyushPatel,EshaChoukse,ChaojieZhang,AashakaShah,ÍñigoGoiri,SaeedMaleki,andRicardoBianchini.2024.
Splitwise:Efficientgenerativellminferenceusingphasesplitting.InProc.ofISCA2024.118–132.
[237] BoPeng,EricAlcaide,QuentinAnthony,AlonAlbalak,SamuelArcadinho,HuanqiCao,XinCheng,MichaelChung,
MatteoGrella,etal.2023.RWKV:ReinventingRNNsfortheTransformerEra.InFindingsofACL:EMNLP2023.
[238] BaolinPeng,ChunyuanLi,PengchengHe,MichelGalley,andJianfengGao.2023. Instructiontuningwithgpt-4.
arXivpreprintarXiv:2304.03277(2023).
[239] HuwanPeng,ScottDavidson,RichardShi,ShuaiwenLeonSong,andMichaelTaylor.2023.ChipletCloud:Building
AISupercomputersforServingLargeGenerativeLanguageModels.arXivpreprintarXiv:2307.02666(2023).
[240] ReinerPope,SholtoDouglas,AakankshaChowdhery,JacobDevlin,JamesBradbury,JonathanHeek,KefanXiao,
ShivaniAgrawal,andJeffDean.2023.Efficientlyscalingtransformerinference.ProceedingsofMachineLearningand
Systems(2023).
[241] RamyaPrabhu,AjayNayak,JayashreeMohan,RamachandranRamjee,andAshishPanwar.2025.vAttention:Dynamic
MemoryManagementforServingLLMswithoutPagedAttention.InProc.ofASPLOS2025.1133–1150.
[242] OfirPress,NoahSmith,andMikeLewis.2021.TrainShort,TestLong:AttentionwithLinearBiasesEnablesInput
LengthExtrapolation.InProc.ofICLR2021.
[243] YifanQiao,ShuAnzai,ShanYu,HaoranMa,YangWang,MiryungKim,andHarryXu.2024.ConServe:Harvesting
GPUsforLow-LatencyandHigh-ThroughputLargeLanguageModelServing.arXivpreprintarXiv:2410.01228(2024).
[244] RuoyuQin,ZhemingLi,WeiranHe,MingxingZhang,YongweiWu,WeiminZheng,andXinranXu.2024.Mooncake:
Akvcache-centricdisaggregatedarchitectureforllmserving.arXivpreprintarXiv:2407.00079(2024).
[245] Qualcomm.2023. ThefutureofAIishybrid. https://www.qualcomm.com/content/dam/qcomm-martech/dmassets/documents/Whitepaper-The-future-of-AI-is-hybrid-Part-2-Qualcomm-is-uniquely-positioned-to-scalehybrid-AI.pdf. Accessedon:2023-11-25.
[246] MarkusNRabeandCharlesStaats.2021.Self-attentionDoesNotNeedO(𝑛2)Memory.arXivpreprintarXiv:2112.05682
(2021).
[247] SamyamRajbhandari,ConglongLi,ZheweiYao,MinjiaZhang,RezaYazdaniAminabadi,AmmarAhmadAwan,
JeffRasley,andYuxiongHe.2022.Deepspeed-moe:Advancingmixture-of-expertsinferenceandtrainingtopower
next-generationaiscale.InProc.ofICML2022.18332–18346.
[248] AdityaRamesh,MikhailPavlov,GabrielGoh,ScottGray,ChelseaVoss,AlecRadford,MarkChen,andIlyaSutskever.

#### Zero-shottext-to-imagegeneration.InProc.ofICML2021.8821–8831.

[249] VijayJanapaReddi,ChristineCheng,DavidKanter,PeterMattson,GuentherSchmuelling,Carole-JeanWu,Brian
Anderson,MaximilienBreughe,MarkCharlebois,WilliamChou,etal.2020.Mlperfinferencebenchmark.InProc.of

## Isca2020.446–459.

[250] StephenRoller,SainbayarSukhbaatar,JasonWeston,etal.2021.Hashlayersforlargesparsemodels.Proc.ofNeurIPS
(2021),17555–17566.
[251] AurkoRoy,MohammadSaffar,AshishVaswani,andDavidGrangier.2021.Efficientcontent-basedsparseattention
withroutingtransformers.TACL(2021),53–68.
[252] HasimSak,AndrewWSenior,andFrançoiseBeaufays.2014.Longshort-termmemoryrecurrentneuralnetwork
architecturesforlargescaleacousticmodeling.InInterspeech,Vol.2014.338–342.
[253] AdrianSampson,TianqiChen,andJaredRoesch.2022.ApacheTVMUnity:avisionfortheMLsoftwareandhardware
ecosystem.
[254] VictorSanh,LysandreDebut,JulienChaumond,andThomasWolf.2019. DistilBERT,adistilledversionofBERT:
smaller,faster,cheaperandlighter.arXivpreprintarXiv:1910.01108(2019).
[255] VictorSanh,ThomasWolf,andAlexanderRush.2020.Movementpruning:Adaptivesparsitybyfine-tuning.Proc.of
NeurIPS(2020),20378–20389.
[256] MichaelSantacroce,ZixinWen,YelongShen,andYuanzhiLi.2023. WhatMattersInTheStructuredPruningof
GenerativeLanguageModels?arXivpreprintarXiv:2302.03773(2023).
[257] AndreaSantilli,SilvioSeverino,EmilianPostolache,ValentinoMaiorca,MicheleMancusi,RiccardoMarin,and
EmanueleRodolà.2023.AcceleratingTransformerInferenceforTranslationviaParallelDecoding.InACL2023.
[258] CiceroNogueiradosSantos,JamesLee-Thorp,IsaacNoble,Chung-ChingChang,andDavidUthus.2023.Memory
AugmentedLanguageModelsthroughMixtureofWordExperts.arXivpreprintarXiv:2311.10768(2023).
ManuscriptsubmittedtoACMComput.Surv..Submissiondate:January2025.

<!-- Page 31 -->

TowardsEfficientGenerativeLargeLanguageModelServing:ASurveyfromAlgorithmstoSystems 1:31
[259] TalSchuster,AdamFisch,TommiJaakkola,andReginaBarzilay.2021.ConsistentAcceleratedInferenceviaConfident
AdaptiveTransformers.InProc.ofEMNLP2021.4962–4979.
[260] NoamShazeer.2019. Fasttransformerdecoding:Onewrite-headisallyouneed. arXivpreprintarXiv:1911.02150
(2019).
[261] NoamShazeer,AzaliaMirhoseini,KrzysztofMaziarz,AndyDavis,QuocLe,GeoffreyHinton,andJeffDean.2017.
Outrageouslylargeneuralnetworks:Thesparsely-gatedmixture-of-expertslayer.InProc.ofICLR2017.
[262] HaihaoShen,HanwenChang,BoDong,YuLuo,andHengyuMeng.2023.EfficientLLMInferenceonCPUs.arXiv
preprintarXiv:2311.00502(2023).
[263] GuangmingSheng,ChiZhang,ZilingfengYe,XibinWu,WangZhang,RuZhang,YanghuaPeng,HaibinLin,and
ChuanWu.2024.Hybridflow:Aflexibleandefficientrlhfframework.arXivpreprintarXiv:2409.19256(2024).
[264] YingSheng,ShiyiCao,DachengLi,ColemanHooper,NicholasLee,ShuoYang,ChristopherChou,BanghuaZhu,
LianminZheng,KurtKeutzer,etal.2023.S-LoRA:ServingThousandsofConcurrentLoRAAdapters.arXivpreprint
arXiv:2311.03285(2023).
[265] YingSheng,ShiyiCao,DachengLi,BanghuaZhu,ZhuohanLi,DanyangZhuo,JosephEGonzalez,andIonStoica.

#### Fairnessinservinglargelanguagemodels.InProc.ofOSDI2024.965–988.

[266] YingSheng,LianminZheng,BinhangYuan,ZhuohanLi,MaxRyabinin,BeidiChen,PercyLiang,ChristopherRé,
IonStoica,andCeZhang.2023.FlexGen:High-ThroughputGenerativeInferenceofLargeLanguageModelswitha
SingleGPU.InProc.ofICML2023.31094–31116.
[267] XingShiandKevinKnight.2017.Speedingupneuralmachinetranslationdecodingbyshrinkingrun-timevocabulary.
InProc.ofACL2017.574–579.
[268] YiningShi,ZhiYang,JilongXue,LingxiaoMa,YuqingXia,ZimingMiao,YuxiaoGuo,FanYang,andLidongZhou.

#### Welder:SchedulingDeepLearningMemoryAccessviaTile-graph.InProc.ofOSDI2023.701–718.

[269] MohammadShoeybi,MostofaPatwary,RaulPuri,PatrickLeGresley,JaredCasper,andBryanCatanzaro.2019.
Megatron-lm: Training multi-billion parameter language models using model parallelism. arXiv preprint
arXiv:1909.08053(2019).
[270] YixinSong,ZeyuMi,HaotongXie,andHaiboChen.2023.PowerInfer:FastLargeLanguageModelServingwitha
Consumer-gradeGPU.arXivpreprintarXiv:2312.12456(2023).
[271] BenjaminSpectorandChrisRe.2023.Acceleratingllminferencewithstagedspeculativedecoding.arXivpreprint
arXiv:2308.04623(2023).
[272] MitchellStern,NoamShazeer,andJakobUszkoreit.2018.Blockwiseparalleldecodingfordeepautoregressivemodels.
Proc.ofNeurIPS(2018).
[273] JianlinSu,YuLu,ShengfengPan,AhmedMurtadha,BoWen,andYunfengLiu.2021.Roformer:Enhancedtransformer
withrotarypositionembedding.arXivpreprintarXiv:2104.09864(2021).
[274] BiaoSun,ZimingHuang,HanyuZhao,WencongXiao,XinyiZhang,YongLi,andWeiLin.2024.Llumnix:Dynamic
schedulingforlargelanguagemodelserving.InProc.ofOSDI2024.173–191.
[275] HanshiSun,ZhuomingChen,XinyuYang,YuandongTian,andBeidiChen.2024.TriForce:LosslessAccelerationof
LongSequenceGenerationwithHierarchicalSpeculativeDecoding.InCOLM2024.
[276] MingjieSun,ZhuangLiu,AnnaBair,andJZicoKolter.2023.ASimpleandEffectivePruningApproachforLarge
LanguageModels.arXivpreprintarXiv:2306.11695(2023).
[277] SiqiSun,YuCheng,ZheGan,andJingjingLiu.2019.PatientKnowledgeDistillationforBERTModelCompression.
InProc.ofEMNLP-IJCNLP2019.4323–4332.
[278] TianxiangSun,XiangyangLiu,WeiZhu,ZhichaoGeng,LinglingWu,YilongHe,YuanNi,GuotongXie,Xuanjing
Huang,andXipengQiu.2022.Asimplehash-basedearlyexitingapproachforlanguageunderstandingandgeneration.
arXivpreprintarXiv:2203.01670(2022).
[279] YutaoSun,LiDong,ShaohanHuang,ShumingMa,YuqingXia,JilongXue,JianyongWang,andFuruWei.2023.
RetentiveNetwork:ASuccessortoTransformerforLargeLanguageModels.arXivpreprintarXiv:2307.08621(2023).
[280] ZitengSun,AnandaTheerthaSuresh,JaeHunRo,AhmadBeirami,HimanshuJain,FelixYu,MichaelRiley,andSanjiv
Kumar.2023.Spectr:Fastspeculativedecodingviaoptimaltransport.InWorkshoponEfficientSystemsforFoundation
Models@ICML2023.
[281] ZhenhengTang,YuxinWang,XinHe,LongtengZhang,XinglinPan,QiangWang,RongfeiZeng,KaiyongZhao,
ShaohuaiShi,BingshengHe,etal.2023. FusionAI:DecentralizedTrainingandDeployingLLMswithMassive
Consumer-LevelGPUs.arXivpreprintarXiv:2309.01172(2023).
[282] RohanTaori,IshaanGulrajani,TianyiZhang,YannDubois,XuechenLi,CarlosGuestrin,PercyLiang,andTatsunoriB
Hashimoto.2023.Stanfordalpaca:Aninstruction-followingllamamodel.
[283] YiTay,DaraBahri,LiuYang,DonaldMetzler,andDa-ChengJuan.2020.Sparsesinkhornattention.InICML2020.
[284] YiTay,MostafaDehghani,DaraBahri,andDonaldMetzler.2023.EfficientTransformers:ASurvey.ACMComput.
Surv.(2023),109:1–109:28.
ManuscriptsubmittedtoACMComput.Surv..Submissiondate:January2025.

<!-- Page 32 -->

1:32 Miao,etal.
[285] MLCteam.2023.MLC-LLM. https://github.com/mlc-ai/mlc-llmCommit:3358029,Accessedon:2023-11-25.
[286] SuratTeerapittayanon,BradleyMcDanel,andHsiang-TsungKung.2016.Branchynet:Fastinferenceviaearlyexiting
fromdeepneuralnetworks.InProc.ofICPR2016.2464–2469.
[287] PhilippeTillet,Hsiang-TsungKung,andDavidCox.2019.Triton:anintermediatelanguageandcompilerfortiled
neuralnetworkcomputations.InProceedingsofthe3rdACMSIGPLANInternationalWorkshoponMachineLearning
andProgrammingLanguages.10–19.
[288] IlyaOTolstikhin,NeilHoulsby,AlexanderKolesnikov,LucasBeyer,XiaohuaZhai,ThomasUnterthiner,JessicaYung,
etal.2021.Mlp-mixer:Anall-mlparchitectureforvision.Proc.ofNeurIPS(2021),24261–24272.
[289] AlexanderTornede,DifanDeng,TheresaEimer,JosephGiovanelli,AdityaMohan,TimRuhkopf,SarahSegel,Daphne
Theodorakopoulos,TanjaTornede,HenningWachsmuth,etal.2023.AutoMLintheAgeofLargeLanguageModels:
CurrentChallenges,FutureOpportunitiesandRisks.arXivpreprintarXiv:2306.08107(2023).
[290] HugoTouvron,LouisMartin,KevinStone,PeterAlbert,AmjadAlmahairi,YasmineBabaei,NikolayBashlykov,
SoumyaBatra,PrajjwalBhargava,ShrutiBhosale,etal.2023.Llama2:Openfoundationandfine-tunedchatmodels.
arXivpreprintarXiv:2307.09288(2023).
[291] MarcosTreviso,Ji-UngLee,TianchuJi,BettyvanAken,QingqingCao,ManuelRCiosici,MichaelHassid,Kenneth
Heafield,SaraHooker,ColinRaffel,etal.2023.Efficientmethodsfornaturallanguageprocessing:Asurvey.TACL
(2023),826–860.
[292] FranciscoMassaGrigorySizovTriDao,DanielHaziza.2023. Flash-Decodingforlong-contextinference. https:
//pytorch.org/blog/flash-decoding/
[293] ColinUnger,ZhihaoJia,WeiWu,SinaLin,MandeepBaines,CarlosEfrainQuinteroNarvaez,VinayRamakrishnaiah,
NirmalPrajapati,PatMcCormick,JamaludinMohd-Yusof,etal.2022. Unity:AcceleratingDNNtrainingthrough
jointoptimizationofalgebraictransformationsandparallelization.InProc.ofOSDI2022.267–284.
[294] TimValicenti,JusticeVidal,andRitikPatnaik.2023.Mini-GPTs:EfficientLargeLanguageModelsthroughContextual
Pruning.arXivpreprintarXiv:2312.12682(2023).
[295] RobertAVanDeGeijnandJerrellWatts.1997. SUMMA:Scalableuniversalmatrixmultiplicationalgorithm.
Concurrency:PracticeandExperience(1997),255–274.
[296] AshishVaswani,NoamShazeer,NikiParmar,JakobUszkoreit,LlionJones,AidanNGomez,ŁukaszKaiser,andIllia
Polosukhin.2017.Attentionisallyouneed.InProc.ofNeurIPS2017.
[297] JikaiWang,YiSu,JuntaoLi,QingrongXia,ZiYe,XinyuDuan,ZhefengWang,andMinZhang.2025. Opt-tree:
Speculativedecodingwithadaptivedrafttreestructure.TACL(2025),188–199.
[298] SinongWang,BelindaZLi,MadianKhabsa,HanFang,andHaoMa.2020. Linformer:Self-attentionwithlinear
complexity.arXivpreprintarXiv:2006.04768(2020).
[299] WenhuiWang,FuruWei,LiDong,HangboBao,NanYang,andMingZhou.2020. Minilm:Deepself-attention
distillationfortask-agnosticcompressionofpre-trainedtransformers.Proc.ofNeurIPS(2020),5776–5788.
[300] XiaohuiWang,YingXiong,YangWei,MingxuanWang,andLeiLi.2020.LightSeq:Ahighperformanceinference
libraryfortransformers.arXivpreprintarXiv:2010.13887(2020).
[301] YidingWang,KaiChen,HaishengTan,andKunGuo.2023.Tabi:AnEfficientMulti-LevelInferenceSystemforLarge
LanguageModels.InProc.ofEuroSys2023.233–248.
[302] YuxinWang,YuhanChen,ZeyuLi,XuezeKang,ZhenhengTang,XinHe,RuiGuo,XinWang,QiangWang,AmelieChi
Zhou,etal.2024. BurstGPT:AReal-worldWorkloadDatasettoOptimizeLLMServingSystems. arXivpreprint
arXiv:2401.17644(2024).
[303] JasonWei,XuezhiWang,DaleSchuurmans,MaartenBosma,FeiXia,EdChi,QuocVLe,DennyZhou,etal.2022.
Chain-of-thoughtpromptingelicitsreasoninginlargelanguagemodels.Proc.ofNeurIPS(2022),24824–24837.
[304] QizhenWeng,WencongXiao,YinghaoYu,WeiWang,ChengWang,JianHe,YongLi,LipingZhang,WeiLin,andYu
Ding.2022.MLaaSinthewild:WorkloadanalysisandschedulinginLarge-ScaleheterogeneousGPUclusters.InProc.
ofNSDI2022.945–960.
[305] BigScienceWorkshop,TevenLeScao,AngelaFan,ChristopherAkiki,ElliePavlick,SuzanaIlić,DanielHesslow,
RomanCastagné,AlexandraSashaLuccioni,FrançoisYvon,etal.2022. Bloom:A176b-parameteropen-access
multilinguallanguagemodel.arXivpreprintarXiv:2211.05100(2022).
[306] BingyangWu,ShengyuLiu,YinminZhong,PengSun,XuanzheLiu,andXinJin.2024.Loongserve:Efficientlyserving
long-contextlargelanguagemodelswithelasticsequenceparallelism.InProc.ofSOSP2024.640–654.
[307] BingyangWu,YinminZhong,ZiliZhang,GangHuang,XuanzheLiu,andXinJin.2023.FastDistributedInference
ServingforLargeLanguageModels.arXivpreprintarXiv:2305.05920(2023).
[308] BingyangWu,RuidongZhu,ZiliZhang,PengSun,XuanzheLiu,andXinJin.2024.dLoRA:Dynamicallyorchestrating
requestsandadaptersforLoRALLMserving.InProc.ofOSDI2024.911–927.
[309] KaixinWu,BojieHu,andQiJu.2021.TenTransHigh-PerformanceInferenceToolkitforWMT2021EfficiencyTask.
InProceedingsoftheSixthConferenceonMachineTranslation.795–798.
ManuscriptsubmittedtoACMComput.Surv..Submissiondate:January2025.

<!-- Page 33 -->

TowardsEfficientGenerativeLargeLanguageModelServing:ASurveyfromAlgorithmstoSystems 1:33
[310] KaixinWu,YueZhang,BojieHu,andTongZhang.2022. SpeedingupTransformerDecodingviaanAttention
RefinementNetwork.InProc.ofCOLING2022.5109–5118.
[311] MengdiWu,XinhaoCheng,ShengyuLiu,ChunanShi,JiananJi,KitAo,PraveenVelliengiri,XupengMiao,OdedPadon,
andZhihaoJia.2024.Mirage:AMulti-LevelSuperoptimizerforTensorPrograms.arXivpreprintarXiv:2405.05751
(2024).
[312] PengWu.2023.PyTorch2.0:TheJourneytoBringingCompilerTechnologiestotheCoreofPyTorch(Keynote).In
Proceedingsofthe21stACM/IEEEInternationalSymposiumonCodeGenerationandOptimization.1–1.
[313] QingyunWu,GaganBansal,JieyuZhang,YiranWu,ShaokunZhang,ErkangZhu,BeibinLi,LiJiang,XiaoyunZhang,
andChiWang.2023.Autogen:Enablingnext-genllmapplicationsviamulti-agentconversationframework.arXiv
preprintarXiv:2308.08155(2023).
[314] XiaoxiaWu,ChengLi,RezaYazdaniAminabadi,ZheweiYao,andYuxiongHe.2023.UnderstandingINT4Quantization
forTransformerModels:LatencySpeedup,Composability,andFailureCases.arXivpreprintarXiv:2301.12017(2023).
[315] HaojunXia,ZhenZheng,YuchaoLi,DonglinZhuang,ZhongzhuZhou,XiafeiQiu,YongLi,WeiLin,andShuaiwenLeonSong.2023.Flash-LLM:EnablingCost-EffectiveandHighly-EfficientLargeGenerativeModelInference
withUnstructuredSparsity.arXivpreprintarXiv:2309.10285(2023).
[316] GuangxuanXiao,JiLin,MickaelSeznec,JulienDemouth,andSongHan.2022.Smoothquant:Accurateandefficient
post-trainingquantizationforlargelanguagemodels.arXivpreprintarXiv:2211.10438(2022).
[317] GuangxuanXiao,YuandongTian,BeidiChen,SongHan,andMikeLewis.2023.EfficientStreamingLanguageModels
withAttentionSinks.arXivpreprintarXiv:2309.17453(2023).
[318] TongXiao,YinqiaoLi,JingboZhu,ZhengtaoYu,andTongranLiu.2019. SharingAttentionWeightsforFast
Transformer.InProc.ofIJCAI2019.5292–5298.
[319] YishengXiao,LijunWu,JunliangGuo,JuntaoLi,MinZhang,TaoQin,andTie-yanLiu.2023. Asurveyonnonautoregressivegenerationforneuralmachinetranslationandbeyond.IEEETPAMI(2023).
[320] ZhiqiangXie,HaoKang,YingSheng,TusharKrishna,KayvonFatahalian,andChristosKozyrakis.2024. AIMetropolis:ScalingLargeLanguageModel-basedMulti-AgentSimulationwithOut-of-orderExecution.arXivpreprint
arXiv:2411.03519(2024).
[321] JiXin,RaphaelTang,JaejunLee,YaoliangYu,andJimmyLin.2020.DeeBERT:DynamicEarlyExitingforAccelerating
BERTInference.InProc.ofACL2020.2246–2251.
[322] CanXu,QingfengSun,KaiZheng,XiuboGeng,PuZhao,JiazhanFeng,ChongyangTao,andDaxinJiang.2023.
Wizardlm:Empoweringlargelanguagemodelstofollowcomplexinstructions.arXivpreprintarXiv:2304.12244(2023).
[323] DaliangXu,WangsongYin,XinJin,YingZhang,ShiyunWei,MengweiXu,andXuanzheLiu.2023.LLMCad:Fast
andScalableOn-deviceLargeLanguageModelInference.arXivpreprintarXiv:2309.04255(2023).
[324] PengXu,WeiPing,XianchaoWu,LawrenceMcAfee,ChenZhu,ZihanLiu,SandeepSubramanian,EvelinaBakhturina,
MohammadShoeybi,andBryanCatanzaro.2023. RetrievalmeetsLongContextLargeLanguageModels. arXiv
preprintarXiv:2310.03025(2023).
[325] ZhaozhuoXu,ZiruiLiu,BeidiChen,YuxinTang,JueWang,KaixiongZhou,XiaHu,andAnshumaliShrivastava.

### Compress,ThenPrompt:ImprovingAccuracy-EfficiencyTrade-offofLLMInferencewithTransferablePrompt.

arXivpreprintarXiv:2305.11186(2023).
[326] AiyuanYang,BinXiao,BingningWang,BorongZhang,ChaoYin,ChenxuLv,DaPan,DianWang,DongYan,Fan
Yang,etal.2023.Baichuan2:Openlarge-scalelanguagemodels.arXivpreprintarXiv:2309.10305(2023).
[327] AmyYang,JingyiYang,AyaIbrahim,XinfengXie,BangshengTang,GrigorySizov,JeremyReizenstein,JongsooPark,
andJianyuHuang.2024.ContextParallelismforScalableMillion-TokenInference.arXivpreprintarXiv:2411.01783
(2024).
[328] NanYang,TaoGe,LiangWang,BinxingJiao,DaxinJiang,LinjunYang,RanganMajumder,andFuruWei.2023.
Inferencewithreference:Losslessaccelerationoflargelanguagemodels.arXivpreprintarXiv:2304.04487(2023).
[329] PenghuiYang,CunxiaoDu,FengzhuoZhang,HaonanWang,TianyuPang,ChaoDu,andBoAn.2025.LongSpec:
Long-ContextSpeculativeDecodingwithEfficientDraftingandVerification.arXivpreprintarXiv:2502.17421(2025).
[330] SeongjunYang,GibbeumLee,JaewoongCho,DimitrisPapailiopoulos,andKangwookLee.2023.PredictivePipelined
Decoding:ACompute-LatencyTrade-offforExactLLMDecoding.arXivpreprintarXiv:2307.05908(2023).
[331] ZheweiYao,ChengLi,XiaoxiaWu,StephenYoun,andYuxiongHe.2023.Acomprehensivestudyonpost-training
quantizationforlargelanguagemodels.arXivpreprintarXiv:2303.08302(2023).
[332] ZheweiYao,RezaYazdaniAminabadi,MinjiaZhang,XiaoxiaWu,ConglongLi,andYuxiongHe.2022.Zeroquant:
Efficientandaffordablepost-trainingquantizationforlarge-scaletransformers.Proc.ofNeurIPS(2022),27168–27183.
[333] DemingYe,YankaiLin,YufeiHuang,andMaosongSun.2021.TR-BERT:DynamicTokenReductionforAccelerating
BERTInference.InProc.ofNAACL2021.5798–5809.
[334] ZihaoYe,LequnChen,RuihangLai,WuweiLin,YinengZhang,StephanieWang,TianqiChen,BarisKasikci,Vinod
Grover,ArvindKrishnamurthy,etal.2025.Flashinfer:Efficientandcustomizableattentionengineforllminference
ManuscriptsubmittedtoACMComput.Surv..Submissiondate:January2025.

<!-- Page 34 -->

1:34 Miao,etal.
serving.arXivpreprintarXiv:2501.01005(2025).
[335] ZihaoYe,RuihangLai,JunruShao,TianqiChen,andLuisCeze.2023.SparseTIR:Composableabstractionsforsparse
compilationindeeplearning.InProc.ofASPLOS2023.660–678.
[336] AnilYemmeandShayanSrinivasaGarani.2023.AScalableGPT-2InferenceHardwareArchitectureonFPGA.In
Proc.ofIJCNN2023.1–8.
[337] Gyeong-InYu,JooSeongJeong,Geon-WooKim,SoojeongKim,andByung-GonChun.2022.Orca:ADistributed
ServingSystemforTransformer-BasedGenerativeModels.InProc.ofOSDI2022.521–538.
[338] LingfanYu,JinkunLin,andJinyangLi.2023.Statefullargelanguagemodelservingwithpensieve.arXivpreprint
arXiv:2312.05516(2023).
[339] WeihaoYu,MiLuo,PanZhou,ChenyangSi,YichenZhou,XinchaoWang,JiashiFeng,andShuichengYan.2022.
Metaformerisactuallywhatyouneedforvision.InProc.ofCVPR2022.10819–10829.
[340] ZhihangYuan,LinNiu,JiaweiLiu,WenyuLiu,XinggangWang,YuzhangShang,GuangyuSun,QiangWu,Jiaxiang
Wu,andBingzheWu.2023. RPTQ:Reorder-basedPost-trainingQuantizationforLargeLanguageModels. arXiv
preprintarXiv:2304.01089(2023).
[341] MurongYue,JieZhao,MinZhang,DuLiang,andZiyuYao.2024.Largelanguagemodelcascadeswithmixtureof
thoughtsrepresentationsforcost-efficientreasoning.InProc.ofICLR2024.
[342] ManzilZaheer,GuruGuruganesh,KumarAvinavaDubey,JoshuaAinslie,ChrisAlberti,SantiagoOntanon,Philip
Pham,AnirudhRavula,QifanWang,LiYang,etal.2020.Bigbird:Transformersforlongersequences.Proc.ofNeurIPS
(2020),17283–17297.
[343] AohanZeng,XiaoLiu,ZhengxiaoDu,ZihanWang,HanyuLai,MingDing,ZhuoyiYang,YifanXu,WendiZheng,
XiaoXia,etal.2022.Glm-130b:Anopenbilingualpre-trainedmodel.arXivpreprintarXiv:2210.02414(2022).
[344] DewenZeng,NanDu,TaoWang,YuanzhongXu,TaoLei,ZhifengChen,andClaireCui.2023.LearningtoSkipfor
LanguageModeling.arXivpreprintarXiv:2311.15436(2023).
[345] ShuangfeiZhai,WalterTalbott,NitishSrivastava,ChenHuang,HanlinGoh,RuixiangZhang,andJoshSusskind.

#### Anattentionfreetransformer.arXivpreprintarXiv:2105.14103(2021).

[346] YujiaZhai,ChengquanJiang,LeyuanWang,XiaoyingJia,ShangZhang,ZizhongChen,XinLiu,andYiboZhu.2023.
Bytetransformer:Ahigh-performancetransformerboostedforvariable-lengthinputs.InIPDPS2023.344–355.
[347] JiaaoZhan,QianChen,BoxingChen,WenWang,YuBai,andYangGao.2023.DePA:ImprovingNon-autoregressive
TranslationwithDependency-AwareDecoder.InProc.ofIWSLT2023).478–490.
[348] ChengliangZhang,MinchenYu,WeiWang,andFengYan.2019.MArk:ExploitingCloudServicesforCost-Effective,
SLO-AwareMachineLearningInferenceServing.InProc.ofUSENIXATC2019.1049–1062.
[349] HailinZhang,XiaodongJi,YilinChen,FangchengFu,XupengMiao,XiaonanNie,WeipengChen,andBinCui.2024.
Pqcache:Productquantization-basedkvcacheforlongcontextllminference.arXivpreprintarXiv:2407.12820(2024).
[350] JunZhang,JueWang,HuanLi,LidanShou,KeChen,GangChen,andSharadMehrotra.2024.Draft&Verify:Lossless
LargeLanguageModelAccelerationviaSelf-SpeculativeDecoding.InProc.ofACL2024.11263–11282.
[351] LongtengZhang,XiangLiu,ZeyuLi,XinglinPan,PeijieDong,RuiboFan,RuiGuo,XinWang,QiongLuo,Shaohuai
Shi,etal.2023.DissectingtheRuntimePerformanceoftheTraining,Fine-tuning,andInferenceofLargeLanguage
Models.arXivpreprintarXiv:2311.03687(2023).
[352] MengkeZhang,TianxingHe,TianleWang,FatemehsadatMireshghallah,BinyiChen,HaoWang,andYuliaTsvetkov.

## LatticeGen:ACooperativeFrameworkwhichHidesGeneratedTextinaLatticeforPrivacy-AwareGeneration

onCloud.arXivpreprintarXiv:2309.17157(2023).
[353] QingruZhang,DhananjayRam,ColeHawkins,ShengZha,andTuoZhao.2023.EfficientLong-RangeTransformers:
YouNeedtoAttendMore,butNotNecessarilyatEveryLayer.InProc.ofEMNLPFindings.2775–2786.
[354] SusanZhang,StephenRoller,NamanGoyal,MikelArtetxe,MoyaChen,ShuohuiChen,ChristopherDewan,Mona
Diab,XianLi,XiVictoriaLin,etal.2022. Opt:Openpre-trainedtransformerlanguagemodels. arXivpreprint
arXiv:2205.01068(2022).
[355] ZhenyuZhang,YingSheng,TianyiZhou,TianlongChen,LianminZheng,RuisiCai,ZhaoSong,YuandongTian,
ChristopherRé,ClarkBarrett,etal.2023.H_2O:Heavy-HitterOracleforEfficientGenerativeInferenceofLarge
LanguageModels.arXivpreprintarXiv:2306.14048(2023).
[356] ZhihaoZhang,AlanZhu,LijieYang,YihuaXu,LantingLi,PhitchayaMangpoPhothilimthana,andZhihaoJia.2024.
Acceleratingiterativeretrieval-augmentedlanguagemodelservingwithspeculation.InProc.ofICML2024.
[357] ChenggangZhao,ShangyanZhou,LiyueZhang,ChengqiDeng,ZheanXu,YuxuanLiu,KuaiYu,JiashiLi,andLiang
Zhao.2025.DeepEP:anefficientexpert-parallelcommunicationlibrary.https://github.com/deepseek-ai/DeepEP.
[358] WeilinZhao,YuxiangHuang,XuHan,WangXu,ChaojunXiao,XinrongZhang,YeweiFang,KaihuoZhang,Zhiyuan
Liu,andMaosongSun.2024.Ouroboros:GeneratingLongerDraftsPhrasebyPhraseforFasterSpeculativeDecoding.
InProc.ofEMNLP2024.13378–13393.
ManuscriptsubmittedtoACMComput.Surv..Submissiondate:January2025.

<!-- Page 35 -->

TowardsEfficientGenerativeLargeLanguageModelServing:ASurveyfromAlgorithmstoSystems 1:35
[359] YilongZhao,Chien-YuLin,KanZhu,ZihaoYe,LequnChen,SizeZheng,LuisCeze,ArvindKrishnamurthy,Tianqi
Chen,andBarisKasikci.2024. Atom:Low-bitquantizationforefficientandaccuratellmserving. Proceedingsof
MachineLearningandSystems6(2024),196–209.
[360] LianminZheng,ZhuohanLi,HaoZhang,YonghaoZhuang,ZhifengChen,YanpingHuang,YidaWang,Yuanzhong
Xu,DanyangZhuo,EricPXing,etal.2022.Alpa:Automatinginter-andIntra-Operatorparallelismfordistributed
deeplearning.InProc.ofOSDI2022.559–578.
[361] LiyanZheng,HaojieWang,JidongZhai,MuyanHu,ZixuanMa,TuoweiWang,ShuhongHuang,XupengMiao,Shizhi
Tang,KezhaoHuang,etal.2023.EINNET:OptimizingTensorProgramswithDerivation-BasedTransformations.In
Proc.ofOSDI2023.739–755.
[362] LianminZheng,LiangshengYin,ZhiqiangXie,JeffHuang,ChuyueSun,Cody_HaoYu,ShiyiCao,ChristosKozyrakis,
IonStoica,JosephEGonzalez,etal.2023.EfficientlyProgrammingLargeLanguageModelsusingSGLang.(2023).
[363] NingxinZheng,HuiqiangJiang,QuanluZhang,ZhenhuaHan,LingxiaoMa,YuqingYang,FanYang,Chengruidong
Zhang,LiliQiu,MaoYang,etal.2023.PIT:OptimizationofDynamicSparseDeepLearningModelsviaPermutation
InvariantTransformation.InProc.ofSOSP2023.331–347.
[364] YinminZhong,ShengyuLiu,JundaChen,JianboHu,YiboZhu,XuanzheLiu,XinJin,andHaoZhang.2024.DistServe:
Disaggregatingprefillanddecodingforgoodput-optimizedlargelanguagemodelserving.InProc.ofOSDI2024.
193–210.
[365] YinminZhong,ZiliZhang,BingyangWu,ShengyuLiu,YukunChen,ChangyiWan,HanpengHu,LeiXia,Ranchen
Ming,YiboZhu,etal.2024.Rlhfuse:Efficientrlhftrainingforlargelanguagemodelswithinter-andintra-stagefusion.
arXivpreprintarXiv:2409.13221(2024).
[366] HaoyiZhou,ShanghangZhang,JieqiPeng,ShuaiZhang,JianxinLi,HuiXiong,andWancaiZhang.2021.Informer:
Beyondefficienttransformerforlongsequencetime-seriesforecasting.InProc.ofAAAI2021.11106–11115.
[367] MinxuanZhou,WeihongXu,JaeyoungKang,andTajanaRosing.2022.Transpim:Amemory-basedaccelerationvia
software-hardwareco-designfortransformer.InProc.ofHPCA2022.1071–1085.
[368] WangchunshuZhou,CanwenXu,TaoGe,JulianMcAuley,KeXu,andFuruWei.2020.Bertlosespatience:Fastand
robustinferencewithearlyexit.Proc.ofNeurIPS(2020),18330–18341.
[369] YanqiZhou,TaoLei,HanxiaoLiu,NanDu,YanpingHuang,VincentZhao,AndrewMDai,QuocVLe,JamesLaudon,
etal.2022.Mixture-of-expertswithexpertchoicerouting.Proc.ofNeurIPS(2022),7103–7114.
[370] YongchaoZhou,KaifengLyu,AnkitSinghRawat,AdityaKrishnaMenon,AfshinRostamizadeh,SanjivKumar,Jean-
FrançoisKagy,andRishabhAgarwal.2023.DistillSpec:ImprovingSpeculativeDecodingviaKnowledgeDistillation.
arXivpreprintarXiv:2310.08461(2023).
[371] ZheZhou,XuechaoWei,JiejingZhang,andGuangyuSun.2022.PetS:AUnifiedFrameworkforParameter-Efficient
TransformersServing.InProc.ofUSENIXATC2022.489–504.
[372] BanghuaZhu,YingSheng,LianminZheng,ClarkBarrett,MichaelIJordan,andJiantaoJiao.2023. OnOptimal
CachingandModelMultiplexingforLargeModelInference.arXivpreprintarXiv:2306.02003(2023).
[373] DeyaoZhu,JunChen,XiaoqianShen,XiangLi,andMohamedElhoseiny.2023.Minigpt-4:Enhancingvision-language
understandingwithadvancedlargelanguagemodels.arXivpreprintarXiv:2304.10592(2023).
[374] XunyuZhu,JianLi,YongLiu,CanMa,andWeipingWang.2023.Asurveyonmodelcompressionforlargelanguage
models.arXivpreprintarXiv:2308.07633(2023).
[375] YoshuaXZXhang,YannMHaxo,andYingXMat.2023.FalconLLM:ANewFrontierinNaturalLanguageProcessing.
ACInvestmentResearchJournal(2023).

### Received23December2023;accepted16July2025

ManuscriptsubmittedtoACMComput.Surv..Submissiondate:January2025.

## Tables

**Table (Page 6):**

| Attention Simplification |
|---|
| RecurrentUnit |


**Table (Page 6):**

| ModelParallelism |
|---|
| SequenceParallelism |
| CloudScaling |


**Table (Page 6):**

| TailoredAttention |
|---|
| Variable Sequencelength |


**Table (Page 7):**

|  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|
|  |  | Transform |  | er Layer 1 |  |  |  |
|  |  | Transfo.rm |  | .e.r Layer 2 |  |  |  |
|  |  | Transfo | rm | er | Layer L |  |  |


**Table (Page 7):**

|  |  |
|---|---|
| Transformer | Layer 1 |
| Transfo.rm.e.r Layer 2 |  |


**Table (Page 7):**

|  |  | mer Layer 1 |  |
|---|---|---|---|
|  |  | m.e.r Layer 2 |  |
| Tran | sfor | mer | Layer L |


**Table (Page 7):**

|  |  |  |
|---|---|---|
| Transfor . Transfor Transfor | mer Layer 1 .. mer Layer 2 mer Layer L |  |


**Table (Page 9):**

| Selective |  |  | Sliding+Dilated |  | Globaltoken |  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | " ! × ×× × | " !! × × | " "" !!! × × × | " "" !!!! ×× × × × | "" """ !!! × × | " " ! ! ! | " |  |  |  |  |  |  |  |  |
| Top- Adapt | 𝑘[126],Sorting ive[70],Inform | [283], er[366] | SparseTransf LongForm | orm⊕er⊕[⊖6⊗5⊗],⊕⊖⊕ "er[43]⊕ ⊖ ⊗ ⊘ | St⊕a⊕r⊖Tr⊗a⊗n⊕sf⊖o⊕rmer⊕[⊕ ⊕⊖ "" G⊗⊘MAT[1"2"5] | 12⊖4⊗],⊗⊕⊖⊕ R⊕ef⊕o⊖rm⊗⊗er⊕[⊖1⊕ ⊕⊖ ⊕⊖ ⊗⊘ " " Tra⊗n⊘sfor | 66],Routi mer"[251] |  |  |  |  |  |  |  |  |
| Scissor [37 | hands[199],H ,149,181,220, | 2O[355] 355] | Mistral-7 [317],Long | B[148], Net[82] S |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  | StreamingLLM[3 | 17], Sparse | hash |  |  |  |  |  |  |  |  |
|  |  |  |  |  | ummary[63],Landma | rk[218] attentio | n[233] |  |  |  |  |  |  |  |  |
|  |  |  |  |  | !! | ! ! ! |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |


**Table (Page 16):**

| Name Github Ref. | Parallel Computation TP PP Offload |  |  | Itera- tion- Sche. | Attention Kernel Initial Incremental |  | Prioritized Opt.Target 𝐿𝑎𝑡 𝑇𝑝𝑡 |  | MainFeatures |
|---|---|---|---|---|---|---|---|---|---|
| FasterTrans- former[2] | √ | √ |  |  | cuBLAS GEMM | Fused attention | √ |  | •Manually-writtenkernel •Lightweightruntime |
| FlexFlow- Serve[12] | √ | √ | √ | √ | cuBLAS GEMM | Tree attention | √ |  | •SpecInfer[211] •Extremelylow𝐿 𝑎𝑡 |
| vLLM[29] | √ |  | √ | √ | xFormers | Paged attention |  | √ | •Block-levelKVcache[171] •Enlargingbatchsize&𝑇 𝑝𝑡 |
| FlexGen[13] |  | √ | √ |  | torch. bmm | torch. bmm |  | √ | •CPU&DiskOffload[266] •MaximizingsingleGPU𝑇 𝑝𝑡 |
| TGI[18] | √ |  |  | √ | Flash attention | Paged attention |  | √ | •Huggingfaceintegration |
| DeepSpeed- Inference[3] | √ | √ |  |  | cuBLAS GEMM | cuBLAS GEMM | √ |  | •Kernelauto-injection[10] •Multi-GPU&Multi-Node |
| ZeRO- Inference[3] | √ | √ | √ |  | cuBLAS GEMM | cuBLAS GEMM |  | √ | •CPU&NVMeOffload[36] •MaximizingsingleGPU𝑇 𝑝𝑡 |
| Light- LLM[21] | √ |  |  | √ | Flash attention | Token attention |  | √ | •Token-levelKVcache •Enlargingbatchsize&𝑇 𝑝𝑡 |
| MLC- LLM[285] | √ |  |  | √ | compiled MatMul | Paged attention | √ |  | •Universaldeployment •MultipletypesofGPUs |
| TensorRT- LLM[25] | √ | √ | √ | √ | cuBLAS/ Flash-attn | Paged attention | √ |  | •NVIDIATritonintegration •Richfeaturessupported |
