---
title: "New Solutions LLM Acceleration"
original_file: "./New_Solutions_LLM_Acceleration.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["prompt-engineering", "llm", "rag", "chain-of-thought", "react"]
keywords: ["conv", "llm", "hls", "design", "page", "arxiv", "add", "tile", "memory", "table"]
summary: "<!-- Page 1 -->

New Solutions on LLM Acceleration, Optimization, and

### Application

YingbingHuang1,LilyJiaxinWan1,HanchenYe1,ManviJha1,JinghuaWang1,YuhongLi1,

### XiaofanZhang2,DemingChen1

{yh21,wan25,hanchen8,manvij2,jinghua3,leeyh,dchen}@illinois.edu,xiaofanz@google.com
1UniversityofIllinoisUrbana-Champaign,2Google
Abstract textdata,demonstrateunparalleledproficiencyintaskssuch
LargeLanguageModels(LLMs)havebecomeextremelypo- as text generation, translation, summarization, sentiment
tent "
related_documents: []
---

# New Solutions LLM Acceleration

<!-- Page 1 -->

New Solutions on LLM Acceleration, Optimization, and

### Application

YingbingHuang1,LilyJiaxinWan1,HanchenYe1,ManviJha1,JinghuaWang1,YuhongLi1,

### XiaofanZhang2,DemingChen1

{yh21,wan25,hanchen8,manvij2,jinghua3,leeyh,dchen}@illinois.edu,xiaofanz@google.com
1UniversityofIllinoisUrbana-Champaign,2Google
Abstract textdata,demonstrateunparalleledproficiencyintaskssuch
LargeLanguageModels(LLMs)havebecomeextremelypo- as text generation, translation, summarization, sentiment
tent instruments with exceptional capacities for compre- analysis,andmore[47][36].Additionally,thereareongoing
hendingandproducinghuman-liketextinawiderangeof effortstotrainLLMswithgroundbreakingmultimodalcapaapplications.However,theincreasingsizeandcomplexity bilities,encompassingbothvisualandspeechunderstandofLLMspresentsignificantchallengesinbothtrainingand ing[27,28,55,56].Theyhavebeensuccessfullyappliedin
deployment,leadingtosubstantialcomputationalandstor- various applications, including virtual assistants, content
agecostsaswellasheightenedenergyconsumption.Inthis generation,question-answeringsystems,andrecommendapaper,weprovideareviewofrecentadvancementsandre- tionsystems.TheversatilityandeffectivenessofLLMshave
searchdirectionsaimedataddressingthesechallengesand madethemindispensabletoolsinvariousindustries,driving
enhancingtheefficiencyofLLM-basedsystems.Webeginby innovationandacceleratingprogressinartificialintelligence.
discussingalgorithm-levelaccelerationtechniquesfocused In domains such as LLM-aided design, large language
onoptimizingLLMinferencespeedandresourceutilization. modelshavebeenutilizedforavarietyoftasks,including
WealsoexploreLLM-hardwareco-designstrategieswitha high-levelsynthesis,hardwaredescriptiongeneration,and
visiontoimprovesystemefficiencybytailoringhardware functionalverification,significantlystreamliningthedesign
architecturestoLLMrequirements.Further,wedelveinto processandreducingtime-to-marketforhardwaredesigns
LLM-to-acceleratorcompilationapproaches,whichinvolve [38].Forinstance,ChipNeMo[32]enhancesLLaMA2with
customizinghardwareacceleratorsforefficientLLMdeploy- domain-specificoptimizationsformoreefficienthardware
ment.Finally,asacasestudytoleverageLLMsforassisting design.AutoChip[48]focusesonautomatingHDLgeneracircuitdesign,weexamineLLM-aideddesignmethodologies tionusingfeedbackfromLLMs,therebyimprovingtheiteraforanimportanttask:High-LevelSynthesis(HLS)functional tivedesignprocess.ChatEDA[53]leveragesLLMstocreate
verification,bycreatinganewdatasetthatcontainsalarge anautonomousagentforEDA,whileVeriGen[49]specialnumberofbuggyandbug-freecodes,whichcanbeessential izes in generating Verilog code. Additionally, DIVAS [41]
fortrainingLLMstospecializeonHLSverificationandde- providesanend-to-endframeworkforSoCsecurityanalysis,
bugging.Foreachaspectmentionedabove,webeginwitha andanotherapproachutilizesLLMstofixhardwaresecurity
detailedbackgroundstudy,followedbythepresentationof bugs [1]. Moreover, large language models are also being
severalnovelsolutionsproposedtoovercomespecificchal- utilizedforautomatedcodegenerationforinformationtechlenges.Wethenoutlinefutureresearchdirectionstodrive nologytasksinYAML,furthershowcasingtheirversatility
furtheradvancements.Throughtheseefforts,weaimtopave andefficiency[42].
thewayformoreefficientandscalabledeploymentofLLMs However,thewidespreadadoptionofthesemodelshas
acrossadiverserangeofapplications. beenhinderedbytheirdemandingcomputationalrequirements,whichoftenresultinslowresponsetimesandhigh
costsforhardwareandenergy.Addressingthesechallenges
1 Introduction
iscrucialtofullyharnessingthepotentialofLLMsandun-

### Inrecentyears,LargeLanguageModels(LLMs)haveemerged

lockingtheirbenefitsinreal-worldapplications.Toaddress
aspowerfultoolsacrossvariousdomains,revolutionizing
thesechallenges,thisresearchpaperexploresacomprehennatural language processing, information retrieval, LLM-
siveapproachtooptimizeLLMsatalgorithm,hardware,comaideddesign,andothers.TheabilityofLLMstounderstand,
piler,anddesign-automationlevels,aimingtoenhancetheir
generate, and manipulate human language has propelled
efficiencyandperformanceacrossdiverseapplications.
themtotheforefrontofresearchandapplicationsinvari-

### Previous works explore various algorithmic strategies

ous industries. These models, trained on vast amounts of
aimedatdecreasingtheinferencelatencyofLLMs.Webe-
Alltheauthorscontributedequally. gin by examining various methods for optimizing param-
Thepresentedworkisanexpandedandmorecomprehensivestudybased eter utilization in large language models. These methods
onourinvitedDAC’24paperwiththesametitleandco-authors.
includetechniquessuchasearlyexitingandlayerskipping
4202
nuJ
61
]GL.sc[
1v30901.6042:viXra

<!-- Page 2 -->

[13],whichhelpreducecomputationaloverhead,aswellas codethatcanthenbetranslatedintoRTLcodeforhardware
contextualsparsity,whichdynamicallyprunesirrelevantpa- implementation.HIDA,builtontopoftheScaleHLSframerametersduringinference[33].Additionally,previousworks work,automatestheconversionofalgorithmichardwaredeexplore a Mixture of Experts (MoE) approach, which dis- scriptionsintoefficientdataflowarchitectures,alsodirectly
tributecomputationacrossmultiplesub-modelstoenhance generatingHLSacceleratorsfromPyTorchmodels.Looking
efficiencyandscalability[12].Wethendelveintooptimiza- forward,wediscussfuturedirections,includingspatialarchitiontechniquesforKey-Value(KV)cache,whichiscrucial tectureexploration,runtimereconfigurationforscalability,
forcomplextaskslikechain-of-thoughtreasoningandin- andheterogeneouscomputingsolutions,tofurtherenhance
formationretrieval.Additionally,wediscussadvancements theefficiencyandscalabilityofhardwareacceleratorsfor
inparalleldecoding[29],includingtechniquesforaligning LLMs.Throughtheseadvancements,weaimtoaddressthe
smallandlargemodelpredictions,multi-tokenpredictions, computationalandmemorychallengesassociatedwithLLM
andparallelprocessingcapabilities.Buildinguponthisback- acceleration,ultimatelyimprovingtheperformanceandengroundstudy,weproposetwonovelapproaches:aparallel ergyefficiencyofhardwareimplementations.
decodingframeworkcalledMedusa[5],whichemploysmul- Therehasrecentlybeenagrowinginterestinleveraging
tipledecodingheadscoupledwithanoptimizedtree-based LLMstoenhanceElectronicDesignAutomation(EDA)prodecodingstrategy,andSnapKV,amethodforeffectivelyre- cesses,offeringsignificantpotentialforimprovingdesign
ducingKVcachesize[31].Ourexperimentalresultsdemon- productivity,codegeneration,andverification[53].Existing
stratesignificantspeedupsininferencetimewithoutcom- researchinthisdomainencompassesvariousapplications,inpromisinggenerationquality,alongwithimprovedmemory cludingassistantchatbotsfordesignworkflowenhancement,
efficiency.Finally,weoutlinefuturedirectionsfortailored Verilog and script generation, and Hardware Description
algorithmicoptimization,advancementsinKVcompression, Language(HDL)verificationandanalysis.Despitetheseadand tackling the computational load from speculative de- vancements,severalchallengespersist,notablythescarcity
coding,aimingtoboostLLMefficiencyandeffectivenessin ofhigh-quality,domain-specificdatasetsandtheneedfor
practicalapplications. morespecializedLLMstailoredtograsptheintricaciesof
LLM-hardwareco-designaimstocustomizehardwarear- electronicdesignlanguagesandprocesses.Asacasestudy
chitecturestomeetthedemandsofLLMswhileproviding toleverageLLMsforassistingcircuitdesign,wefocuson
insightstooptimizeLLMarchitectures[15].Previously,we animportanttask:High-LevelSynthesis(HLS)functional
proposedanLLM-hardwareco-designframeworkcalledAu- verification.Wepursuethistaskthroughtheconstruction
toDistill[64],whichintegratesmodelcompression,trans- oftheChrysalisdataset,anextensivecollectionofHLSdeformer architecture exploration, and multi-objective opti- signsembeddedwithdiversesetsofrealisticbugs,andthe
mizationtoproducestudentmodelswithlowerinference developmentofanHLS-specificdebuggingassistant.Adelatencyandsmallersizeswhilemaintaininghighaccuracy. buggingassistantcanbebuiltbytraininganLLMfine-tuned
Moreover,apruning-awarequantizationstrategythatcom- ontheChrysalisdatasetwhichaimstosignificantlyexpedite
binestwoeffectiveLLMcompressionmethods,pruning,and theverificationprocess,enhanceproductivity,andreduce
quantization,tooptimizeLLMarchitecturesforhardware time-to-marketforhardwaredesigns.Additionally,weoutefficiencyhasbeenproposed[51].Furthermore,weexplore linefutureresearchdirections,includingLLM-aidedformal
thepotentialofreconfigurableandheterogeneoushardware verification and the integration of LLMs into multi-agent
forLLMs,aimingtodynamicallyadjusthardwarearchitec- systemsforhardware/softwaredesignautomation,offering
tures to accommodate the latest LLM advancements and atransformativeapproachtostreamliningthedesign,verifimodelcompressionmethods,therebyenhancingbothmodel cation,anddebuggingprocessesinEDA.
qualityandhardwareefficiency. Intherestofthepaper,Section2delvesintoalgorithm-
Thedemandforefficienthardwareacceleratorsfordeep level acceleration for LLMs, while Section 3 provides an
neuralnetworkshasledtoanewdirectionofusingHigh- overviewofhardwareco-designtailoredforLLMs.Section
LevelSynthesis(HLS)frameworks[7][9]toquicklytranslate 4focusesonthecompilerformappingLLMstoaccelerators,
modelarchitecturesintohardwareimplementations.How- andSection5exploresLLMaideddesigns.Finally,Section6
ever,exploringthevastdesignspaceeffectivelytoachieve presentstheconclusionofthestudy.
optimalsolutionsremainsasignificantchallenge.Wesummarizetwonovelcompilationframeworkspublishedpreviously
byus:ScaleHLS[21,57]andHIDA[60].ScaleHLSleverages
2 LLMAlgorithm-LevelAcceleration
theMLIRinfrastructure[26]forscalableHigh-LevelSynthesis,optimizinghardwaredesignswithaDesignSpaceEx- 2.1 BackgroundStudy
plorationenginebyperformingmulti-leveltransformations. LLMsexcelintaskssuchascodingcopilot,questionanswer-
Asfarasweknow,ScaleHLSwasthefirstflowthatcould ing,andsummarization.However,theirautoregressivenatakeaPyTorchmodelandtransformitintosynthesizableC ture,whereeachtokendependsonallpreviousones,makes

<!-- Page 3 -->

decodingmemory-intensiveandhardtoparallelize.ThisresultsinsignificantlatencyduetothemassivesizeofLLM
parameters,impactingapplicationsrequiringfastresponses ❄/🔥

### Original Model 🔝Top-k Predictions

like chatbots. Addressing the challenge of reducing inferencelatencyinLLMsisbecomingincreasinglycritical.This LM Head It, I, As
section primarily explores previous methods aimed at de- 🔥Medusa Heads
creasingtheinferencelatencyofLLMsfromanalgorithmic Last Hidden

### Medusa Head 1 is, ', the

standpoint,whichcouldfacilitatestraightforwardimplemen-

### Transformer

tationandintegrationacrossvariousplatforms. Layers Medusa Head 2 difficult, is, '
2.1.1 EfficientParameterUtilization. Theearlystudy

### Medusa Head 3 not, difficult, a

[45]showsonlyanecessarysubsetofparametersisused Embedding
perinputtokentoreducelanguagemodelinferencelatency
while preserving accuracy. The concepts of early exiting
andlayerskipping[13,44]indecoderarchitectures,allow 📝Input 📜Candidates  Single step prediction
foranefficientgenerationofsequencesbypotentiallyex- What will happen if It is difficult not ✅ It is difficult

### Medusa meets a llama? It' difficult a ❌

iting the decoding process early based on certain criteria, It is' not ❌ ...
thussavingoncomputationalresourceswhilemaintaining
outputquality.Onanotherperspective,contextualsparsity, Figure 1. The proposed parallel decoding framework
asinvestigatedbyLiuetal.[33],leveragestheinsightthat Medusa. During inference, each head generates multiple
asignificantportionofmodelweightscanbedynamically toppredictionsforitsdesignatedposition.Thesepredictions
omittedwithoutaffectingperformance,capitalizingonthe areassembledintocandidatesprocessedinparallelusinga
variabilityofimportanceacrossdifferentweightsfordiffer- tree-basedattentionmechanism.Thentheframeworkverifies
entinputs.Lastly,theMixtureofExperts(MoE)[12,19,68] thecandidatesandacceptsacontinuation[4].
approachdecouplesmodelsizefromcomputationaldemands,
enablingsignificantscalingofmodelcapacitywithminimal
impactoninferenceefficiency,offeringapathwaytoenhancisspecificallyadaptedforLLMefficiency.Recentadvanceingmodelperformancewithoutproportionalincreasesin
mentsinparalleldecodingforLLMsincludetechniquesby
computationalburden.

### Leviathanetal.[29]andChenetal.[6],whichintroduceare-

2.1.2 KVCacheOptimization. KVCacheinLLMsstores samplingstrategytoalignsmallandlargemodelpredictions
previouslycomputedattentionvaluesandkeys.Thiscaching
with the LLM’s distribution, ensuring output consistency.
provesparticularlyeffectiveforcomplextaskslikechain-of-

### Sternetal.[46]exploremulti-tokenpredictionsfromasingle

thought[52]reasoningorinformationretrieval[30].Howforwardpassusingalinearprojectionlayerandatree-based
ever,itintroducesoverheadslikesetuptime,extramemory
decodingstructuretoimprovedecodedsequenceacceptance.
for cache storage, and the complexity of managing cache
Additionally,Santillietal.[43]andFuetal.[14]adaptJavaliditywhenthesequencelengthorbatchsizeincreases.
cobiandGaussian-Seidelalgorithms[40]forparallelizing
SeveralstrategieshavebeendevelopedtoenhanceKVCache
decoding,incorporatingn-gramreuseandattentionmasks
efficiency.OnekeyapproachisthroughadvancedKVCache
toenhanceLLMefficiency.
managementtechniques.Forinstance,theVLLM[25]introducesPagedAttentionwhichstoreskeysandvaluesinseg-
2.2 ProposedWorks
mentedmemoryblocks,allowingformoreefficientretrieval

### LLMinferenceispredominantlymemory-bandwidth-bound

during attention calculations. Additionally, solutions like
withthemainlatencybottleneckstemmingfromaccelera-

### Hydragen[22]employaShared-prefixKVCachestrategy,

tors’memorybandwidthratherthanarithmeticcomputagreatlyimprovingcachereuseratesbyleveragingcommon
tions.Thisbottleneckisinherenttothesequentialnature
sequences.AnothersignificantadvancementistheuseofKV
of auto-regressive decoding, where each forward pass re-

### Cachecompression[65],whichimplementsevictionpolicies

quires transferring the complete model parameters from
toselectivelyretaintokensinthecache,guidedbyascoring
High-BandwidthMemory(HBM)totheaccelerator’scache.
functionbasedoncumulativeattention.

### Thisprocess,whichgeneratesonlyasingletoken,under-

2.1.3 Parallel Decoding. Parallel decoding presents a utilizesthearithmeticcomputationpotentialofmodernacuniqueapproachbyexecutingmultipledecodingstepssi- celerators,leadingtoinefficiency.Inourproposedwork[4],
multaneously to reduce the overall steps needed, diverg- namedasMedusa,werevisittheconceptofparalleldecoding
ingfromtraditionalmethods.Ittypicallyinvolvesasmaller withanewperspective,notingthatcurrentresearchprimar-
"draft"modelpredictingseveralupcomingwords,whichare ilyaimstoboostgenerationspeedthroughdraftmodels.Yet,
thencollectivelyassessedbythemainLLM.Thistechnique obtaininganappropriatedraftmodeleitherfromscratchor

<!-- Page 4 -->

fromdistillationisnon-trivial.Also,hostingdual-sizedmod- bothcloudandedgedevices,accuratelypredictingtheperforelsonaserverpresentschallenges,andit’sevenharderto manceofparalleldecodingmodelshasbecomeincreasingly
integratethedraftmodelintoadistributedsystem.Totackle complex. A universal solution for LLM performance optithis,wepresentanovelapproach(showninFig.1)using mizationremainselusive.Withoutaccuratepredictionbefore
multipledecodingheadsastheadapterforprediction,cou- traininganddeployment,thereisariskofwastingcomputapledwithanoptimizedtree-baseddecodingstrategy,enhanc- tionalresourcesandfailingtomeetperformancetargets.We
ingtheefficiencyofthemethod.Ourproposedtechnique focusonmodelingandpredictingvariousscenarios,utilizing
doesnotneedaseparatedraftmodelandallowsforseam- ananalyticmodeltoachievepreciseperformanceestimalessintegrationintoexistingLLMsystems.Ourexperiments tions.Ourobjectiveistocreatepredictiveframeworksthat
demonstratethatlimited-resourcefine-tuningcanachieve aid in selecting optimal parallel decoding algorithms and
over2.2×speedupwithoutcompromisinggenerationqual- theirhyperparameterstailoredtomodelsize,taskcomplexity,whilefullfine-tuningfurtherimprovesthespeedupto ity,andperformancegoals.Thisaimstoenhanceefficiency,
2.3-2.8×onmodelswithvarioussizes.Furthermore,paral- adaptability,andoverallmodelperformance.
leldecodingimprovesresourceutilizationduetoincreased
2.3.2 CombiningKVCompressionandParallelDematrix operations for multi-token validation per step. By
coding. LeveragingKVcompression,weseeopportunities
employing an optimized tree-based attention mechanism,
fornotableimprovementsintaskswithlargeinputprompts,
westrivetominimizetheoverheadintroducedbyparallel
like summarization and multi-round chats, where precise
decoding.Ourfocusonoptimizationofbothfine-tuningand
promptcompressionwillbecrucialformaintainingretrieval
inferencewiththedecodingadapterinthecontextofspecaccuracyandunderstanding.Inlong-contextscenarios,diulativedecodingpresentsanoveldirectionforenhancing
rectlyprocessingtheentirepromptandperforminginference
LLMperformance.
withparalleldecodingintroducessignificantinferenceover-
Furthermore, our method, SnapKV [31], effectively rehead due to the increased computational complexity and
ducesKVcachesize,addressingthecomputationalandmemmemoryrequirements.Toaddressthis,weexploreeffective
orybottlenecksinscenariosinvolvinglongsequenceinputs.
attentionmechanismssuchasGroupQueryAttention[2]

### Ourfindingsdemonstratetheconsistentattentionallocation

andtechniqueslikequantizingtheKVcachetoreducecompatternsofimportantfeaturesinpromptsusedthroughout
putationalload.TheserefinementsareintendedtoboostLLM
thegenerationprocess,independentofpromptformats.This
efficiencyandeffectivenessinpracticaluseswhilemaintainobservationhighlightsthepotentialonKVcachecompresingthegenerationquality.
sionforlongsequenceinput,whichcouldreducethecomputationalandmemoryoverheadinattentioncalculationdur-
3 LLM-Hardwareco-design
inggenerationsteps.Leveragingthisinsight,ourinnovative
approachintelligentlyidentifiestheseattentionallocation 3.1 BackgroundStudy
patternsbyusingthewindowoffeaturesattheendoflong TheexceptionalcapabilitiesofLLMsarecounteredbytheir
sequenceinput,asshowninFig.2,andcompressestheKV significantmemoryandcomputationaloverheads.Addresscacheaccordingly.Thisproposedworkachievesconsistent ingthese,LLM-hardwareco-design,inspiredbytheDNN-
decodingspeeds,significantlyenhancinggenerationspeed accelerator co-design methodology [15] [16], customizes
by3.6xandimprovingmemoryefficiencyby8.2xcompared hardwaretomeetthesedemandsandprovidesinsightsto
tothebaseline,whenprocessinginputsof16ktokens. optimize LLM architectures. Specialized accelerators, like

### GPUs,TPUs,andFPGAs,enhanceparallelprocessingand

memorycapacityandprovideefficientLLMexecution.At
Input Sequence KVs
H r
C m
e
a
e
y
p
n
l o p
e
r
y m
m t
o
o
a u
e f
i l h
a t
?
h
e
n
…
i
l
a s
p
l c y
m
z o e
e
m t
r
p h
e
a e
p
n
h
Q y
r
… 4
a se
sreyaL
I V m o p t o in r g ta & n t S F e

## P

e le a
r
c
e
tu t
f
i r
i
n e
x
g s x W
w
A e
O i
t i
n
g t
b
e h
d
n
s
t
o
t
.

## C

w
i o a n lc . R th & e D

## T

fo
h
e u
e
x r p
c
t e h
o
n
m
q s u
p
e a
a
s r
n
t f e o
y’
r r
s t
ti
h
o
e
n,
sa
p
m
ru
e
ni
t
n
im
g,
e
a
,
n
s
d
of
q
tw
ua
a
n
re
tiz
s
a
t
t
r
i
a
o
t
n
e
,
g
c
ie
a
s
n
,
e
s
ff
uc
e
h
cti
a
v
s
el
m
y
o
r
d
ed
el
uc
d
e
is

## L

ti

## L

ll

## M

a-
I want to buy a gift for my of 2023 is xxx.xx size and complexity, making them adaptable to hardware
mom… Obs. billion. This figure
I K C d V a o n c n a y ’t c o u h u n e t d e in e ll r L m s L t e M a n t s h d … e w d h e a t t a i i s ls Conca C te lu n s a t t e in ri g n g F e & atures w O in b d s o . w c c a o n n t b e e xt s o e f e … n in the constraints.
of R&D expense of Q4? window Wehaveseencustomizedhardwareacceleratorsarebuilt
“Snap” ! Compressed KVs
forLLMworkloads.Forexample,TensorProcessingUnits
Figure 2. The graph shows the simplified workflow of (TPUs)[20]aredesignedtoefficientlyhandlematrixopera-
SnapKV,wheretheorangearearepresentsthegroupofpo- tionswhicharefundamentalforLLMattentionandlinear
sitionsperheadclusteredandselectedbySnapKV. layers.TheseacceleratordesignsenhanceLLMsupportby
integratingHighBandwidthMemory(HBM),reconfigurable
high-speedinterconnects,andmulti-typeparallelcomputa-
2.3 FutureDirections tionsupport,offeringcost-effectiveLLMtrainingandserving
2.3.1 EnhancedVersatilityinParallelDecoding. With solutions.BeyondASICs,FPGA-basedacceleratorsarebethegrowthinthesizeofLLMsandtheirdeploymentacross ingactivelyinvestigatedfortheirpotentialtoprovidemore

<!-- Page 5 -->

Table1.TheresultsonSQuADv1.1.Ours-1andOurs-2deflexibleandfasterturnaroundsolutions.Forexample,DFX notetwomodelsdesignedwithAutodistill[64].
[17]utilizesmodelparallelismandenablesrapidconcurrent
executionoftransformer-basedworkloads,whileFlightLLM
[62]introducesaconfigurablecomputeunitandaLLMmap-
# Param Latency F1 EM
pingflowtosupportLLMinference.
ForLLMdesigns,researchershaveinvestigatedhardware- BERT BASE 109M - 88.5 80.8

### DistilBERT 67M - 85.8 77.1

awaremodelcompressiontechnologiestooptimizeLLMar-

### DistilBERT* 67M - 86.9 79.1

chitecture.FlashAttention[10]reducesthenumberofHigh

### TinyBERT * 67M - 87.5 79.7

Bandwidth Memory (HBM) accesses by using tiling tech- 6

## Nas-Bert* 60M - 88.0 80.5

niques in attention computations and extends it to block-

## Nas-Bert*† 60M - 88.4 81.2

sparseattention.PagedAttention[25]dividestheKVcache

### MobileBERT 25.3M 0.65ms 90.0 82.9

into blocks and manages blocks as pages in OS’s virtual MobileBERT‡ 25.3M 0.65ms 87.7 80.0
memory,reducingtheinternalandexternalfragmentation Ours-1 22.8M 0.59ms 88.4 80.8
andthusincreasingtheefficiencywithinasinglerequest. Ours-2 20.6M 0.49ms 88.1 80.5

### In addition, model distillation, pruning, and quantization

haveproventoimprovehardwareefficiencyforLLMdeployment.MLFS[24]freezesabasemodelandstoresmanysmall
low-rank adapter matrices, which maintains high quality
encodermodelsonedgeapplicationsandreducestraining
time.LLM.int8[11]developsatwo-partvector-wisequantizationprocedureandanewmixed-precisiondecomposition scheme, enabling models like OPT-175B on a single
serverwithconsumerGPUs.SmoothQuant[54]usesaperchannelsmoothingfactortohandleoutliersinactivations
and achieves up to 1.56x speedup and 2x memory reduc-
Figure3.TheproposedAutoDistillframework[64].
tion.ViTCoD[61]prunesattentionmapstoeitherdenseor
sparsepatternsanddesignsanacceleratorthatcoordinates methods,pruningandquantization,forLLM-hardwarecobetweenthesetwoworkloadstoboosthardwareutilization design[51].Weobserveasimilarsparsitydistributionpatwhileintegratingon-chipencoderanddecoderengines. ternofattentionheadsacrossvariousdatasetsasshownin
Fig. 4, which could potentially be used to smartly choose
eithercompletelypruning(0bit)ordifferentquantization
precision(4,8,16bits)forattentionheadsonindividuallay-
3.2 ProposedWorks
erswithoutadditionaloverhead,basedonthehardwarelevel
Following the LLM-hardware co-design method, we pro- objective. Moreover, pruning-aware quantization method
poseAutoDistill[64],anend-to-endmodeldistillationframe- couldalsobecombinedwithotherstate-of-the-arthardwareworktodeliverhardware-efficientmodels.AsshowninFig. awareLLMaccelerationframeworks,suchasflashattention
3,AutoDistill introducesathree-stage solution,which in- inFig.5,andgivehigherthroughput.
cludesmodelarchitectureexploration,modelcompression,
andmodelevaluationtodeliverefficientmodelsgiventhe 3.3 FutureDirections
target hardware and hardware-software tradeoff require- 3.3.1 System-awarealgorithmicoptimization. AsLLMs
ments. To facilitate the hardware/software co-design pro- continuetogrowinsizeandcomplexity,itisbecomingincess, these stages are tightly connected and continuously creasinglycriticaltodesignthemwithhardwaresystemin
iteratedinaquality-performancespace.Duringtheevalu- mind.Itmeansthemodeldevelopersshouldconsiderthe
ation stage, model quality and its hardware performance hardwaresystemconfigurations,includingacceleratorarchiresultsarepassedbacktothemodelexplorationtoguide tecture,computepower,memorycapacity,systemtopology,
the search engine for finding a better model architecture networkbandwidth,modelparallelismstrategies,inaddition
thatcouldfulfillbothsoftwareandhardwarerequirements. totheLLMdesignparameters.
Results show that AutoDistill can efficiently produce stu- Thisfuturedirectionwillcreatemultipleoptimizationopdentmodelswithlowerinferencelatencyandsmallersizes, portunitiestoexplorethecombineddesignspaceconsisting
whilemaintaininghighaccuracyonmultipledownstream ofhardwareandsoftwareconfigurations.Modelqualitywill
tasks,suchasSQuADforquestionansweringandreading notbetheonlyoptimizationobjectivewhilehardwarepercomprehensioninTable1. formanceandefficiencymetrics,suchasQueriespersecond
Wealsoproposeapruning-awarequantizationstrategy (QPS)andlatency,willalsobeconsideredandexploredas
bycombiningtwoofthemosteffectiveLLMcompression parts of the LLM designs. With such an enhanced design

<!-- Page 6 -->

fastdevelopmentofhardwareacceleratorstoefficientlyhandlekeyLLMoperations,includingmatrixmultiplicationand
attentionmechanisms.Additionally,itcanbecombinedwith
heterogeneoushardwaretoexplorenewcomputeparadigms,
suchasadoptingin-memorycomputing,toaddressmemoryboundoperations.Thisdirectionenablestrade-offsbetween
modelqualityandhardwareefficiency.
3.3.3 Co-design for edge LLM applications. The codesign for edge LLM applications is crucial, given the intricatechallengesposedbyedgecomputing’senergyand
resourcelimitations.LLM-hardwareco-designemergesasa
promisingsolutiontothesechallenges,aimingtoharmonize
software and hardware to optimize LLM performance on
edgedevices.Futureresearchwillfocusoncreatingtailored
architecturesandalgorithmsthatefficientlymanagecomputationalresources,ensuringthatthequalityofLLMservices
Figure4.Theprofilingresultsontheactivityofheadsacross
remainshigh.Thiscouldinvolveexploringadaptivepower
different datasets by measuring each head’s contribution
managementtechniques,optimizingmemoryusage,andenbasedonitsvarianceovertheinputsequence.Headsthat
hancingprocessingspeedswithoutsacrificingtheaccuracy
showlowvarianceareconsideredinactive,leadingtoconorresponsivenessofLLMapplications.
textualsparsity.
4 LLM-to-AcceleratorCompiler
4.1 BackgroundStudy
High-LevelSynthesis(HLS)[7][9]isvitalforrapidlydevelopingefficient,high-densityhardwareaccelerators,enabling
quickevaluationofdifferentalgorithmicchoices.Thechallenge of enabling scalable compiler from LLM models to
HLS-basedacceleratorsliesineffectivelyexploringthevast
designspace,whichcanleadtosub-optimalsolutionsifnot
donewell,underminingtheproductivitybenefitsofHLS.To
tacklethischallenge,inthissection,wewillintroducetwo
compilationframeworks,ScaleHLSandHIDA,whichcan
generateHLSacceleratorsdirectlyfromPyTorchmodels.
4.2 ProposedWorks
Figure5.Thepreliminaryresultfromforwardthroughput ... HLS C/C++ PyTorch
improvement.Flash2_hmaskistheresultfromthecombina- F P r o o l n yg t- e e i n s d t T F o r r o c n h t - - M en L d IR Graph-level IR A T n ra a n ly s s f i o s r L m ib a ra n r d y ScaleHLS
tionofFlashAttention2[10]andourpruning-awarequanti-

### Graph


### TOSA Linalg Tensor

zationapproach[51]. Opt. Passes

### Loop-level IR


### Loop Automated


### A ne Vector MemRef


### Opt. Passes DSE Engine

space,LLMscanbespecificallytailoredtotheunderlying

### Directive-level IR

systemandhardwarearchitectureandweanticipatefurther

### Directive


### A ne Vector MemRef HLSCpp

innovationsinmodelsizereduction,efficientshardingstrate- Opt. Passes

### Translate

gies,optimizeddatalayouts,andothertechniquestofully Lowering

### HLS C/C++ HLS QoR

utilizethefullpotentialoftargetsystems. Emitter Estimator Transform

## Circt

3.3.2 Reconfiguratbleandheterogeneoushardware Framework
for LLMs. Reconfigurable hardware, such as FPGAs, is a ... Verilog HLS C/C++ ScaleHLS Tool ScaleHLS Dialect Existing Dialect
promisingsolutiontoaddressthecontinuouslyevolvingLLM
designs.Itofferstheabilitytoadapttothespecificcomputa-
Figure6.ScaleHLSframeworkarchitecture[57].
tionalpatternsofdifferentLLMworkloads,whichallowsa

<!-- Page 7 -->

4.2.1 ScaleHLS. ScaleHLS[21,57–59]isascalableHLS
framework based on Multi-Level Intermediate Representation (MLIR) [26]. Fig. 6 shows the overall architecture.
ScaleHLS supports C/C++ and PyTorch as design entries.

### Oncetheinputsareparsed,ScaleHLSsupportsthreelevels

ofIR,graph,loop,anddirective,toapplytheHLS-orientedoptimizationsprogressively.Atthegraphandlooplevel,graph
optimizations(e.g.,nodefusionandcoarse-grainedpipelining)andloopoptimizationscanbeperformedefficiently.At
the lowest directive level, HLS-specific optimizations are
appliedtofine-tunethehardwaremicro-architecture.
OntopofeachlevelofIR,ScaleHLSprovidesasetoftransformpassestooptimizeHLSdesigns.Byperformingeach
transformpassatthe"correct"levelofabstraction,ScaleHLS
is able to leverage the intrinsic hierarchy of HLS designs
andreducethealgorithmiccomplexityoftransforms.Meanwhile,weproposeaDesignSpaceExploration(DSE)engine
toautomaticallyoptimizetheconfigurabledesignparametersandsearchforthePareto-dominatingdesignpointsin
thelatency-resourceutilizationspace.Finally,theoptimized

### IRisemittedassynthesizableHLSC/C++code.Experimental

resultsshowthat,comparingtothebaselinedesignswithoutmanualdirectivesinsertionandcode-rewriting,thatare
onlysynthesizedbyVitisHLS,ScaleHLSimprovestheperformanceswithupto3825.0×onrepresentativeneuralnetwork
models.
Schedule0
Node0

### Add


### Node1

. Conv.

### Dispatch0

Task0 Node2
Add Conv.

### Task1

. Conv. Node3 Node6 Conv. Task2 Add

### Conv. Schedule6-0

T A as d k d 3 D Ta is s p k a 6 t c C h o 6 n - v 0 . N C o o d n e v 4 . T N i o le d L e o 6 a -0 d

### Task4 Task6-0

Conv. Tile Load Node6-1
Node5 Node6 Tile Comp.
Task5 Task6 Task6-1 Conv. Conv.
Conv. Conv. Tile Comp.

### Task6-2 Node6-2

Task7 Tile Store Node7 Tile Store Add Add
Functional Dataflow Structural Dataflow
gnirewoL
woflataD

### HIDA-IR,whichisdesignedformodelingdataflowattwo

distinct abstraction levels: Functional and Structural. This
dual-levelapproachiscriticalforcapturingthedataflow’s
characteristicsanditsmulti-levelhierarchy,therebyfacilitatingeffectiveoptimizations.

### AnotherimportantaspectofHIDAistheintroductionof

HIDA-OPT, a new dataflow optimizer. This optimizer utilizesapattern-driventaskfusionalgorithmcoupledwithan
intensity-andconnection-awaredataflowparallelizationalgorithm,whichcancapturethecomputationcomplexityand
interconnectiontopologyofthedataflownodesduringthe
parallelizationprocess.Furthermore,HIDAisdesignedtobe
end-to-endandextensible,supportingbothPyTorchandC++
inputs.Thisflexibilityempowersuserstorapidlyexperiment
withvariousdesignparametersandprototypenewdataflow
architectures,broadeningtheframework’sapplicabilityand
easeofuse.Despitebeingfullyautomatedandabletohandlevariousapplications,HIDAachievedthroughputsthat
were 8.54× and 1.29× higher than those of ScaleHLS and
RTL-basedneuralnetworkaccelerators[63],respectively.
4.3 FutureDirections
4.3.1 Spatial Architecture. Due to the substantial volumeofparametersandintermediatecomputationsinvolved
inLLMs,thebottleneckinhardwareaccelerationfrequently
residesintheexternalmemorybandwidth.Contrarytothe
VonNeumannarchitecture,whichconsistentlybattlesthe

### Inputs Outputs

HIDA "memorywall,"spatialarchitecturescanleverageon-chip

### PyTorch HLS C++ Vitis HLS,

etc. communicationamongtaskstominimizefrequentexternal
Node1 Conv.
T M or L c IR h- Polygeist O H p L t S im C iz + e + d … 0 5 … 1 6 … 2 7 … 3 8 … 4 9 … … … m LL e M mo la r y y e a r c s c a e n ss d e b s. u B ff y er o in ve g r o la n p l p y in a g su th b e se e t x o e f cu in ti t o er n m o e f d d i i a s t t e in r c e t -
sultson-chip,spatialarchitecturescanmarkedlydecrease
HLS C++ Node2 Conv.
Emitter on-chipmemoryrequirementsandoveralllatency.Thisap-

### Token 0 1 2 3 4 …

5 6 7 8 9 … External … … … … … … proach presents a compelling solution for LLM inference.

### Memory Nonetheless,theautomaticgenerationofspatialarchitec-

AXI turesremainschallenging,openingvastavenuesforinnovationincompilationandarchitecturedesign.
4.3.2 RuntimeReconfiguration. Toachievespatialparallelization,tasksmustbeinstantiatedsimultaneouslyonchip. However, due to constrained computational and onchip memory resources, it is infeasible to simultaneously
mapalllayersofemergingLLMson-chip,whichsignificantly
limitsthescalabilityofspatialarchitectures.Consequently,
runtime reconfiguration emerges as a crucial strategy for
Tensor or Memory Ref. Passing Memory Accessing Streaming Memory
enablingscalablespatialsolutions.Themainchallengelies
Figure7.HIDAframeworkarchitecture[60]. inautomatingthebalancebetweenspatialandsequential
execution—thatis,addressingtheschedulingproblem—to
4.2.2 HIDA. HIDA[60]isanHLSframeworkbuiltupon optimizetheperformance-energytrade-off.
ScaleHLSwithhierarchicaldataflowintermediaterepresentations(IR)andoptimizations,enablingtheautomatedtrans- 4.3.3 HeterogeneousComputation. AcceleratingLLMs
formationofalgorithmichardwaredescriptionstoefficient presentsauniquechallengeduetotheirdualnature,being
dataflowarchitectures.Fig.7showstheHIDA’soverallar- both computation-bound and memory-bound. The prefill
chitecture.ThecoreofHIDAisitsnoveldataflowIR,named phase of LLMs is dominated by General Matrix Multiply

<!-- Page 8 -->

(GEMM)operators,makingitcomputation-intensive.Incon- methodologywhereLLMs,particularlyGPT-4,areprompted
trast,thegenerationphaseisdominatedbyGeneralMatrix- withrefinedrulesandRTLcodetogenerateSVA,whichis
Vector(GEMV)operations,demandingsubstantialmemory thenevaluatedforcorrectnessandcompletenessthrougha
bandwidthtokeepthecomputationunitsengaged(referto seriesoftestbenchsimulationsandrevisions.
Section 2.2). This dual nature of LLMs unveils significant DespitethepromisingdevelopmentsinLLM-aideddesign
opportunitiesforheterogeneouscomputingsolutions,where withinEDA,severalchallengesremain:(1)DataQualityand
compilersassumeanimportantroleinthecodegeneration Availability:TheefficacyofLLMsinEDAcriticallyhingeson
forheterogeneousplatformsandfacilitatingefficientcom- theavailabilityofhigh-quality,domain-specificdatasetsfor
municationbetweenthem. theirtrainingandrefinement.Unfortunately,theproprietary
nature of many electronic designs and the tools used for
4.3.4 AdvancedHIDA. AlthoughtheHIDAframework

### EDAsignificantlylimitaccesstosuchdatasets.Thebulkof

can conduct effective dataflow-aware design space explodetailedhardwaredesigncodes,primarilydevelopedwithin
ration, optimizing streaming buffers in LLM accelerators
corporatesettings,arenotmadepublic.Thisrestrictionleads
remains a formidable challenge due to the self-attention
toascarcityofaccessible,high-gradedatasets,thushindermechanismandcomplexinter-layerconnectionsinLLMs.
ingthedevelopmentandoptimizationofLLMsspecifically

### EnhancementsintheHIDAframeworkcouldaddressmore

engineeredforEDAapplications;(2)DevelopmentofSpecomplicatedstreamoptimizationstoreduceon-chipmemcializedLLMs:Thereisacriticalneedforthedevelopmentof
ory consumption. Additionally, recent works [8, 67] have

### LLMsthatarespecificallytailoredtograspthecomplexities

demonstratedtheabilitytogenerateefficientkerneldesigns
ofelectronicdesignlanguagesandprocesses.Thegeneric
through customized scheduling. We propose to integrate
models,whileuseful,oftenlackthenuancedunderstanding
thesehighly-optimizedkernelsintotheHIDAexplorerto
requiredtoeffectivelygenerate,verify,andanalyzehardware
furtherimprovetheefficiencyofLLMaccelerators.Wealso
codeandtointeractwithEDAtoolsatalevelthatmatches
proposetoenhancethecodegenerationofHIDAtosupport
humanexperts.Thisnecessitatesaconcertedefforttocreate
morehardwareplatformswithdataflowarchitecture,such
morespecializedmodelsthatcancomprehendandmanipasAMDVersalACAP[3].
ulatetheintricatedetailsofelectronicdesignswithahigh
degreeofaccuracyandefficiency.
5 LLM-aideddesign
5.1 BackgroundStudy 5.2 ProposedWorks
TheexistingrelatedworkregardingleveragingLLMsinthe OneusecaseofLLM-aideddesignistoharnessLLMsfor
fieldofEDAcouldbedividedintothreecategories[66]:(1) enhancingtheverificationanddebuggingprocessesforHLS
Assistant Chatbot for Enhanced Design Workflow: Chip- codedevelopment.HLS,withitshigherlevelofabstraction,
Nemo [32] leverages domain adaptation techniques such cansignificantlyimprovedesignproductivityasexplained
ascustomtokenizers,domain-adaptivecontinuedpretrain- inSection4.1.
ing,andSupervisedFine-Tuning(SFT)atopthefoundation 5.2.1 ChrysalisDataset. Thecornerstoneofourproposed
modelLLaMA2[37].Thisintegrationfacilitatesinstantac- workistheChrysalisdataset,anextensivecollectionofHLS
cesstoknowledge,streamlinesthequery-responseprocess, designsembeddedwithadiversesetofrealisticbugs[51].
and diminishes reliance on conventional search methods Thisdatasetismeticulouslycuratedfromawiderangeof
andassociateddelays.(2)HDLandScriptGeneration:LLMs, open-sourceHLSbenchmarksuites,featuringover1,500desuchasthoseinAutoChip[48]andVeriGen[49],haveshown signs,withboththeversionembeddedwithbugsandthe
theireffectivenessingeneratingVerilogcodesandEDAtool correspondingbug-freeversion.Fig.8outlinesourmethodscriptsfromnaturallanguageinstructions;(3)HDLVerifica- ologyforconstructingtheChrysalisdataset.Webeginby
tionandAnalysis:RTLFixer[50]exemplifiesthisbyintro- gatheringopen-sourcebenchmarksuitesanddifficultbug
ducingaframeworkaimedatcorrectingVerilogcodeerrors types(bugsalsoincludenon-idealHLSPragmainsertions),
utilizingtoolslikeOpenAIGPT-3.5/GPT-4,supplementedby whichcompilersoftenstruggletoidentify.Thesesuitesare
RetrievalAugmentedGeneration(RAG)andReActprompt- thenconvertedtothefunction-leveldesigns.UsingtheMaxiingtechniques.Additionaleffortsinthisareafocusongener- malMarginalRelevance(MMR)algorithm,weselectthetopatingSystemVerilogAssertions(SVA)forsecuritypurposes ksimilardesignsfromtheRAGdatabaseforbuginjection
[23][35][41],illustratingthewide-rangingpotentialofLLMs prompts.Thepromptgenerationchoosesonestrategybased
inbolsteringHDLverificationandanalysisprocesses.CHI- onbugtypestatistics:onecombiningIn-ContextLearning
RAAG [34] is proposed to generate SVA assertions from (ICL),Retrieval-augmentedGeneration(RAG),andChainnatural language specification based on GPT-4. For those of-Thoughts(CoT);theotherusingjustRAGandICL.After
assertionswithsyntaxerrororsimulationerror,LLMscould integration,thepromptsareprocessedbyanLLM(GPT-4
receivetheautomaticfeedbackoflogfileandthenregener- inourcase)togeneratebug(ornon-idealPragma)injection
atetheSVAforretest.Orenes-Vera[39]proposedaniterative solutions,whicharethenvalidatedthroughbothautomatic

<!-- Page 9 -->

Bug Types Benchmark Prompt P D r e o b p u o g s g e i d n g H F L l S o w

### Suites Context: I am exploring HW programming… LLM

Steps[CoT]: (1) Identify an array; (2) … Debugging Potential Refined

### Bugs HLS Design

Requirements: The reply structure should be… Assistant

### Bug Code


### Examples[RAG+ICL]: Here are examples: HLS

Selection Converter Example 1: {…}, Example 2: {…}, Design Test

### Complementary Rules: Under Test Vectors

RAG Database Designs 1. The bug only appears inside the function… (DUT) Bug-free
Testbench C Simulation Bugs HLS

### Designs Design


### MMR Top-k Prompting with

Bug Injections Comparator Examples ICL+RAG +CoT Gen R e T ra L t ion Sim C ul o a - tion I D n e d b u u s g tr g ia in l g H F L l S o w
or
Iterative Prompting with
√
Update ICL+RAG Figure9.LLM-basedHLSDebuggingFlowsWorkingTogetherwithTraditionalFlows:ByincorporatingourLLM

### Automatic Check


### LLM debuggingassistant,thenumberofbugsrequiringverifica-

Manual Check Codeline Exists? tionbytestcasescanbesignificantlyreduced.
Valid Injection? Bug Type is Output

### Correct?

I /P m e p r a fo c r t m R a e n su c l e t ? s Pr F a u g n m c a ti o In n s s i ? de Sp I e n c j i e f c i t c i o B n ug open-sourceLLMsanddevelopingadomain-specificRTL
debuggerthroughfine-tuning.Toeffectivelytransitionto
thisnewapplication,wemusttacklediversebugtypesspe-

### Figure8.OverviewoftheChrysalisDatasetConstruction

cifictoRTL,suchasthoserelatedtotimingconstraints,race
andIterativeUpgradeProcess:Foreachcheckiteration,it
conditions,andsynthesis-simulationmismatches.Particuinvolvesevaluatingthedataset’svalidityandexpandingthe
larly,theinherenttimingcharacteristicsofRTLdesignscan
RAGdatasetaccordingly.Throughtheseiterations,thequalleadtomorecomplexbugs,oftenmanifestingasissuesin
ityofthedatasetprogressivelyimproves.
timinganalysisthatarenotpresentinhigher-levelabstractions.GiventhecomplexityofRTLcode,oneambitiousgoal
proceduresaswellasmanualchecksbyhardwareengineers.
is to reduce manual debugging and verification effort by
SuccessfulsolutionsareaddedtotheRAGdatabasetoenbuildinganadvancedandautomatedRTLverificationand
hanceitsdiversityandvolume,improvingfuturesolutions.
debuggingflow.Thiswouldinvolveenrichingourdatasetto
Our evaluations show 88% validity for all the bugs. This
includeRTLdesigns(canbegeneratedthroughHLSworking
dataset serves not only as a tool for training our domainwithourChrysalisdataset)togetherwithtestbenchesand
specific LLM, but also as a benchmark for evaluating the
test vectors. A flow similar to Fig. 8 can be developed to
model’sproficiencyinidentifyingandsuggestingfixesfor
assessandimprovethevalidityofsuchbuginjections.FurcommonandcomplexHLSbugs.
thermore,seamlessintegrationwithEDAtoolsiscrucialto
5.2.2 HLS-specificDebuggingAssistant. Buildingupon enablereal-timeanalysisandcorrectionwithintheexisting
theChrysalisdataset,ournextstepinvolvesthecreationof designframeworks.
anHLS-specificdebuggingassistant,asFig.9shows.Engineerstypicallydesigntestvectorsandcreatetestbenches 5.3 FutureDirections
manually,thenperformCsimulationsandco-simulationsto 5.3.1 LLM-Aided Debugging. Our research highlights
analyzeandidentifypotentialbugs,whichistime-consuming. challengesinusingLLMstoinjectcertainHLSbugtypes,
Toimprovetheefficiencyofthedebuggingprocess,wepro- such as operator precedence errors and incorrect data acposedanovelflowleveragingthecapabilitiesofLLMson cesspatternsforinterfacepragmas.Thesedifficultiesstem
top of the traditional HLS debugging flow. This LLM will fromsparsecodepatternsandthecomplexitiesoftheexistbefine-tunedtounderstandtheintricaciesofHLScode,en- ingcodebase,necessitatingfurtherinvestigationandrefined
ablingittoidentifyerrors,suggestcorrections,andprovide methodologiesforeffectivebuginjection.Additionally,as
guidancedirectlywithinthedevelopers’workflow.Theassis- manualverificationofbuginjectionsremainsnecessaryin
tantaimstointegrateseamlesslywithpopulardevelopment ourcurrentflow,creatinganautomatedflowtoestimateperenvironments, offering real-time support to engineers as formancecouldspeeduptheidentificationandresolution
theynavigatethecomplexitiesofHLSdesigns.Byproviding ofnon-idealPragmaissues,thusenhancingthequalityand
context-awaresuggestionsandcorrections,thedebugging quantityofthedataset.Furthermore,fortheHLS-specific
assistantwillsignificantlyexpeditetheverificationprocess, debuggingassistant,wewillemployLow-RankAdaptation
enhancingproductivityandreducingthetime-to-marketfor (LoRA)[18]forsupervisedfine-tuningonstate-of-the-art
hardwaredesigns. open-sourceLLMssuchasLLaMA3[36],utilizingcommer-
TheentiremethodologycouldbeadaptedtoRTLdebug- cialHLSdocumentationfordesignguidelinesandrulestoging as well, starting from the bug injection stage, using getherwithourChrysalisdataset.

<!-- Page 10 -->

5.3.2 LLM-Aided Formal Verification. LLMs can en- datasetthatcanbeusedtotrainanLLM-basedHLS-specific
hance the formal verification process in hardware design debuggingassistant.Asimilarstrategycanbeadoptedfor
bygeneratingpreciseassertionsfortheproofofcorrectness. buildinganRTL-specificdebuggingassistantaswell.These
Byintegratingtheseassertionsintotheformalverification methodsarepromisingforstreamliningthedebuggingand
workflow,LLMscansubstantiallyincreasehardwaredesign verificationprocessofthehardwarecodedevelopment.
productivity.Onepromisingdirectionistoexploreaniter- Foreachaspectmentionedabove,wealsooutlinedpromisativeprocess:aftertheinitialproofattempts,thetheorem ingfuturedirectionsforfurtherresearchandexploration.
prover’sfeedbackisutilizedtorefinetheLLM’soutput.This
feedbackloopenablestheLLMtoadjustitsgeneratedproofs Acknowledgments
iterativelyuntiltheassertionsarefullyverifiable.Through ThisworkissupportedinpartbytheIBM-IllinoisDiscovery
thisdynamicinteractionbetweenLLMsandtheoremprovers, AcceleratorInstitute,AMDCenterofExcellenceatUIUC,
thegenerationofprogramproofsbecomesbothfasterand AMD Heterogeneous Adaptive Compute Cluster (HACC)
moreachievable.Thismethodologynotonlyspeedsupthe initiative, NSF 2117997 grant through the A3D3 institute,
verificationprocessbutalsoensuresahigherdegreeofrelia- andSemiconductorResearchCorporation(SRC)2023-CT-
bilityinhardwaredesignverification. 3175grant.
5.3.3 LLM-AidedHardware/SoftwareDesignAutoma-

### References

tion. IntherealmofEDA,employingLLMmulti-agentsystemspromisesatransformativeapproachtostreamlining [1] BaleeghAhmadetal.2023. Fixinghardwaresecuritybugs
thedesign,verification,anddebuggingprocesses.Thesesowithlargelanguagemodels. arXiv:2302.01215.
[2] Joshua Ainslie, James Lee-Thorp, Michiel de Jong, Yury
phisticatedsystemsautonomouslymanagevariousphases
Zemlyanskiy,FedericoLebrón,andSumitSanghai.2023. Gqa:
oftheworkflow,seamlesslytransitioningfromdesigntover-

### Traininggeneralizedmulti-querytransformermodelsfrom

ificationanddebugging.Bydeployingmultiplespecialized
multi-headcheckpoints. arXivpreprintarXiv:2305.13245.

### LLMagents—eachadeptindistinctfacetsofthedesignpro-

[3] AMD/Xilinx.[n.d.]. VersalAdaptiveComputeAcceleration
cesssuchascodegeneration,verification,errordetection, Platform. https://www.xilinx.com/products/silicon-devices/
andperformanceoptimization—ahighlyefficientpipeline
acap/versal.html
iscrafted.Thisorchestratedintegrationallowstheagents [4] Tianle Cai et al. 2024. Medusa: Simple llm inference
tocollaborativelyrefineandoptimizethedesigniteratively, acceleration framework with multiple decoding heads.
leveragingreal-timefeedbackandcomprehensiveverifica- arXiv:2401.10774.
tionresults.Throughouttheprocess,hardwareengineers [5] TianleCai,YuhongLi,ZhengyangGeng,HongwuPeng,JasonD.Lee,DemingChen,andTriDao.2024. Medusa:Simple
areonlytaskedwithoverseeingtheinitialspecificationand
LLM Inference Acceleration Framework with Multiple DeperiodicallyreviewingtheoutputsfromtheLLMstoensure
codingHeads.InICML. https://openreview.net/forum?id=
thattheyalignwiththedesignintentionsandconfirmthe

### PEpbUobfJv

reliabilityoftheLLMs’outputs.
[6] CharlieChenetal.2023. Acceleratinglargelanguagemodel
decodingwithspeculativesampling. arXiv:2302.01318.
6 Conclusion [7] DemingChenetal.2005.xPilot:APlatform-BasedBehavioral
Inourstudy,wefocusedonoptimizingLLMstoreduceinfer-
SynthesisSystem.InSRCTechcon.
[8] Hongzheng Chen et al. 2024. Allo: A Programming
encelatencyandimproveefficiencyacrossvariousapplica-
ModelforComposableAcceleratorDesign. arXivpreprint
tions.Wepresentedanewmethod,Medusa,tousemultiple
arXiv:2404.04815.
decodingheadsforprediction,coupledwithanoptimized
[9] JasonCong,JasonLau,GaiLiu,StephenNeuendorffer,Petree-baseddecodingstrategyforparalleltokenprocessingto ichen Pan, Kees Vissers, and Zhiru Zhang. 2022. FPGA
speeduptheexecutionofLLMs.Wealsoproposedanovel HLSToday:Successes,Challenges,andOpportunities. ACM
method, SnapKV, that effectively reduced KV cache size, Trans.ReconfigurableTechnol.Syst.15,4,Article51,42pages.
addressingthecomputationalandmemorybottlenecksin https://doi.org/10.1145/3530775
scenariosinvolvinglongsequenceinputs. [10] TriDaoetal.2022. Flashattention:Fastandmemory-efficient
WediscussedLLM/hardwareco-designtointegrateboth exactattentionwithio-awareness. AdvancesinNeuralInforhardwareoptimizationforefficientexecutionandmodelar- mationProcessingSystems.
[11] TimDettmersetal.2022. Llm.int8():8-bitmatrixmultiplicachitectureexplorationforimprovedsystemefficiencywhile
maintainingLLMaccuracy.HLSframeworkslikeScaleHLS
tionfortransformersatscale.arXivpreprintarXiv:2208.07339.
[12] NanDuetal.2022.Glam:Efficientscalingoflanguagemodels
andHIDAwereexploredforacceleratingLLMsdirectlyfrom
withmixture-of-experts.InICML.

### PyTorchmodels,envisioningautomatedgenerationofspatial

[13] Maha Elbayad et al. 2019. Depth-adaptive transformer.
architecturesandheterogeneouscomputingsolutions. arXiv:1910.10073.
WealsoexploredtheadvancementsinLLM-aideddesign [14] YichaoFuetal.2024. Breakthesequentialdependencyofllm
forEDAanddiscussedanovelflowtocreatetheChrysalis inferenceusinglookaheaddecoding. arXiv:2402.02057.

<!-- Page 11 -->

[15] CongHaoetal.2018. DeepneuralnetworkmodelandFPGA arXiv:2402.00093.
acceleratorco-design:Opportunitiesandchallenges.InIC- [35] XingyuMengetal.2023. Unlockinghardwaresecurityassur-
SICT. ance:Thepotentialofllms. arXiv:2308.11042.
[16] Cong Hao et al. 2019. FPGA/DNN co-design: An efficient [36] Meta. 2024. Introducing Meta Llama 3: The most capable
designmethodologyforIoTintelligenceontheedge.InDAC. openlyavailableLLMtodate. https://ai.meta.com/blog/meta-
[17] SeongminHongetal.2022. DFX:Alow-latencymulti-FPGA llama-3/
applianceforacceleratingtransformer-basedtextgeneration. [37] Meta.2024. Llama2:opensource,freeforresearchandcom-

### InMICRO. mercialuse. https://llama.meta.com/llama2/

[18] EdwardJHuetal.2021. Lora:Low-rankadaptationoflarge [38] Md Rakib Hossain Misu et al. 2024. Towards AI-Assisted
languagemodels. arXivpreprintarXiv:2106.09685. SynthesisofVerifiedDafnyMethods. Proc.ACMSoftw.Eng.1,
[19] AlbertQJiangetal.2024.Mixtralofexperts.arXiv:2401.04088. FSE. https://doi.org/10.1145/3643763
[20] NormJouppietal.2023. Tpuv4:Anopticallyreconfigurable [39] MarceloOrenes-Veraetal.2023.Usingllmstofacilitateformal
supercomputerformachinelearningwithhardwaresupport verificationofrtl. arXive-prints,arXiv–2309.
forembeddings.InISCA. [40] JamesMOrtegaandWernerCRheinboldt.2000. Iterative
[21] HyegangJunetal.2023. AutoScaleDSE:Ascalabledesign solutionofnonlinearequationsinseveralvariables. Classics
spaceexplorationengineforhigh-levelsynthesis.InTRETS. inAppliedMathematics.
[22] JordanJuravskyetal.2024.Hydragen:High-ThroughputLLM [41] Sudipta Paria et al. 2023. Divas: An llm-based end-to-end
InferencewithSharedPrefixes. arXiv:2402.05099. frameworkforsocsecurityanalysisandpolicy-basedprotec-
[23] RahulKandeetal.2023. Llm-assistedgenerationofhardware tion. arXiv:2308.06932.
assertions. arXiv:2306.14027. [42] SaurabhPujar,LucaBuratti,XiaojieGuo,NicolasDupuis,Burn
[24] AchintyaKunduetal.2024. EfficientlyDistillingLLMsfor Lewis,SahilSuneja,AtinSood,GaneshNalawade,MattJones,
EdgeApplications. arXivpreprintarXiv:2404.01353. AlessandroMorari,andRuchirPuri.2023.Invited:Automated
[25] WoosukKwonetal.2023. EfficientMemoryManagement CodegenerationforInformationTechnologyTasksinYAML
forLargeLanguageModelServingwithPagedAttention.In throughLargeLanguageModels.In202360thACM/IEEEDe-
SOSP. signAutomationConference(DAC).1–4. https://doi.org/10.
[26] ChrisLattner,MehdiAmini,UdayBondhugula,AlbertCohen, 1109/DAC56929.2023.10247987
AndyDavis,JacquesPienaar,RiverRiddle,TatianaShpeisman, [43] AndreaSantillietal.2023.Acceleratingtransformerinference
NicolasVasilache,andOleksandrZinenko.2021.MLIR:Scaling fortranslationviaparalleldecoding. arXiv:2305.10427.
compilerinfrastructurefordomainspecificcomputation.In [44] TalSchusteretal.2022.Confidentadaptivelanguagemodeling.
2021IEEE/ACMInternationalSymposiumonCodeGeneration AdvancesinNeuralInformationProcessingSystems.
andOptimization(CGO).IEEE,2–14. [45] AntoineSimoulinetal.2021. Howmanylayersandwhy?
[27] ZhihongLei,ErnestPusateri,ShiyiHan,LeoLiu,Mingbin Ananalysisofthemodeldepthintransformers.InIJCNLP
Xu,TimNg,RuchirTravadi,YouyuanZhang,MirkoHanne- StudentResearchWorkshop.
mann,Man-HungSiu,etal.2024.Personalizationofctc-based [46] MitchellSternetal.2018. Blockwiseparalleldecodingfor
end-to-endspeechrecognitionusingpronunciation-driven deepautoregressivemodels. AdvancesinNeuralInformation
subwordtokenization.InICASSP2024-2024IEEEInternational ProcessingSystems.
ConferenceonAcoustics,SpeechandSignalProcessing(ICASSP). [47] GeminiTeametal.2024. Gemini:AFamilyofHighlyCapable

### IEEE,10096–10100. MultimodalModels. arXiv:2312.11805[cs.CL]

[28] ZhihongLei,MingbinXu,ShiyiHan,LeoLiu,ZhenHuang, [48] ShailjaThakuretal.2023. Autochip:Automatinghdlgenera-
TimNg,YuanyuanZhang,ErnestPusateri,MirkoHannemann, tionusingllmfeedback. arXiv:2311.04887.
Yaqiao Deng, et al. 2023. Acoustic Model Fusion For End- [49] ShailjaThakuretal.2023. Verigen:Alargelanguagemodel
to-EndSpeechRecognition.In2023IEEEAutomaticSpeech forverilogcodegeneration.InTRETS.
RecognitionandUnderstandingWorkshop(ASRU).IEEE,1–7. [50] YunDaTsaietal.2023.Rtlfixer:Automaticallyfixingrtlsyntax
[29] YanivLeviathanetal.2023. Fastinferencefromtransformers errorswithlargelanguagemodels. arXiv:2311.16543.
viaspeculativedecoding.InICML. [51] LilyJiaxinWanetal.2024. Software/HardwareCo-designfor
[30] PatrickLewisetal.2020. Retrieval-augmentedgenerationfor LLMandItsApplicationforDesignVerification.InASP-DAC.
knowledge-intensivenlptasks.AdvancesinNeuralInformation [52] Jason Wei et al. 2022. Chain-of-thought prompting elicits
ProcessingSystems. reasoninginlargelanguagemodels. Advancesinneuralinfor-
[31] YuhongLi,YingbingHuang,BowenYang,BharatVenkitesh, mationprocessingsystems.
AcyrLocatelli,HanchenYe,TianleCai,PatrickLewis,and [53] HaoyuanWuetal.2024. ChatEDA:ALargeLanguageModel
DemingChen.2024.SnapKV:LLMKnowsWhatYouareLook- PoweredAutonomousAgentforEDA. IEEETransactionson
ingforBeforeGeneration. arXivpreprintarXiv:2404.14469. Computer-AidedDesignofIntegratedCircuitsandSystems,1–1.
[32] MingjieLiuetal.2023. Chipnemo:Domain-adaptedllmsfor https://doi.org/10.1109/TCAD.2024.3383347
chipdesign. arXiv:2311.00176. [54] Guangxuan Xiao et al. 2023. Smoothquant: Accurate and
[33] Zichang Liu et al. 2023. Deja vu: Contextual sparsity for efficientpost-trainingquantizationforlargelanguagemodels.
efficientllmsatinferencetime.InICML. InICML.
[34] Bhabesh Mali et al. 2024. ChIRAAG: ChatGPT Informed [55] MingbinXu,AlexJin,SichengWang,MuSu,TimNg,Henry
RapidandAutomatedAssertionGeneration. arXivpreprint Mason,ShiyiHan,YaqiaoDeng,ZhenHuang,andMahesh

<!-- Page 12 -->

Krishnamoorthy. 2023. Conformer-Based Speech Recogni- [62] ShulinZengetal.2024. FlightLLM:EfficientLargeLanguage
tionOnExtremeEdge-ComputingDevices. arXivpreprint ModelInferencewithaCompleteMappingFlowonFPGA.
arXiv:2312.10359. arXiv:2401.03868.
[56] MingbinXu,CongzhengSong,YeTian,NehaAgrawal,Filip [63] XiaofanZhangetal.2018. DNNBuilder:Anautomatedtool
Granqvist,RogiervanDalen,XiaoZhang,ArturoArgueta, forbuildinghigh-performanceDNNhardwareaccelerators
ShiyiHan,YaqiaoDeng,etal.2023.Traininglarge-vocabulary forFPGAs.InICCAD.
neural language models by private federated learning for [64] XiaofanZhangetal.2022. AutoDistill:Anend-to-endframeresource-constraineddevices.InICASSP2023-2023IEEEInter- worktoexploreanddistillhardware-efficientlanguagemodels.
nationalConferenceonAcoustics,SpeechandSignalProcessing arXiv:2201.08539.
(ICASSP).IEEE,1–5. [65] Zhenyu Zhang et al. 2023. H2o: Heavy-hitter oracle for
[57] HanchenYeetal.2022. ScaleHLS:Anewscalablehigh-level efficient generative inference of large language models.
synthesisframeworkonmulti-levelintermediaterepresenta- arXiv:2306.14048.
tion.InHPCA. [66] RuizheZhongetal.2023. LLM4EDA:EmergingProgressin
[58] HanchenYeetal.2022. ScaleHLS:ascalablehigh-levelsyn- LargeLanguageModelsforElectronicDesignAutomation.
thesisframeworkwithmulti-leveltransformationsandopti- arXiv:2401.12224.
mizations.InDAC. [67] JinmingZhuang,JasonLau,HanchenYe,ZhuopingYang,Yubo
[59] Hanchen Ye et al. 2023. High-level Synthesis for Domain Du,JackLo,KristofDenolf,StephenNeuendorffer,AlexJones,
SpecificComputing.InISPD. JingtongHu,etal.2023.CHARM:ComposingHeterogeneous
[60] HanchenYeetal.2024. HIDA:AHierarchicalDataflowCom- AcceleRatorsforMatrixMultiplyonVersalACAPArchipilerforHigh-LevelSynthesis.InASPLOS. tecture.InProceedingsofthe2023ACM/SIGDAInternational
[61] HaoranYouetal.2023.Vitcod:Visiontransformeracceleration SymposiumonFieldProgrammableGateArrays.153–164.
viadedicatedalgorithmandacceleratorco-design.InHPCA. [68] BarretZophetal.2022. Designingeffectivesparseexpert
models. arXiv:2202.08906.

## Tables

**Table (Page 6):**

| Transform and |
|---|
| Analysis Library Graph Opt. Passes Loop Opt. Passes Directive Opt. Passes HLS QoR Estimator |


**Table (Page 7):**

| Inputs Outputs Schedule0 HIDA PyTorch HLS C++ Vitis HLS, Node0 etc. Add Node1 Conv. Node1 T M or L c IR h- Polygeist O H p L t S im C iz + e + d … 0 5 … 1 6 … 2 7 … 3 8 … 4 9 … … … . Conv. Dispatch0 HLS C++ Node2 Conv. Emitter Task0 Node2 Token 0 1 2 3 4 … Add Conv. 5 6 7 8 9 … External … … … … … … Task1 Memory . Conv. Node3 Node6 Conv. AXI Task2 Add Conv. Schedule6-0 T A as d k d 3 D Ta is s p k a 6 t c C h o 6 n - v 0 . N C o o d n e v 4 . T N i o le d L e o 6 a -0 d Task4 Task6-0 Conv. Tile Load Node6-1 gnirewoL Node5 Node6 Tile Comp. Task5 Task6 Task6-1 Conv. Conv. Conv. Conv. Tile Comp. woflataD Task6-2 Node6-2 Task7 Tile Store Node7 Tile Store Add Add Functional Dataflow Structural Dataflow Tensor or Memory Ref. Passing Memory Accessing Streaming Memory |  |
|---|---|
|  | Memory |


**Table (Page 7):**

|  |  |  | Schedule0 Node0 Add Node1 . Conv. |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  | . |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  | Token Node2 Conv. AXI Node3 Add Node4 Conv. Node5 Node6 Conv. Conv. Node7 Add |  |  |  |  | Node2 Conv. 0 1 2 3 4 … |  |
|  | Task6 Conv. Dispatch6-0 |  |  |  |  |  |  |  |  |
|  | Task6-0 Tile Load Task6-1 Tile Comp. Task6-2 Tile Store | gnirewoL woflataD |  |  |  |  |  |  |  |
|  |  |  | Structural Dataflow |  |  |  |  |  |  |


**Table (Page 7):**

| Schedule0 |
|---|
| Node0 Add |


**Table (Page 7):**

| Node1 Conv. |  |  |  |  |  |  |
|---|---|---|---|---|---|---|
| 0 | 1 | 2 | 3 | 4 | … |  |
| 5 … | 6 … | 7 … | 8 … | 9 … | … … |  |


**Table (Page 7):**

| Dispatch0 Task0 Add Task1 . Conv. Task2 Conv. Task3 Add Task4 Conv. Task5 Task6 Conv. Conv. Task7 Add |  |  |
|---|---|---|
|  | Task3 Add |  |
| Task4 Conv. Task5 Task6 Conv. Conv. Task7 Add |  |  |
| Functional Dataflow |  |  |


**Table (Page 7):**

| Node6 Conv. Schedule6-0 |  |
|---|---|
| Node6-0 Tile Load Node6-1 Tile Comp. Node6-2 Tile Store |  |


**Table (Page 9):**

|  |
|---|
| Proposed HLS Debugging Flow LLM Potential Refined Debugging Bugs HLS Design Assistant HLS Design Test Under Test Vectors (DUT) Bug-free Testbench C Simulation Bugs HLS Design RTL Co- Industrial HLS Generation Simulation Debugging Flow Figure9.LLM-basedHLSDebuggingFlowsWorkingTo getherwithTraditionalFlows:ByincorporatingourLLM debuggingassistant,thenumberofbugsrequiringverifica |


**Table (Page 9):**

| Proposed HLS Debugging Flow LLM Potential Refined Debugging Bugs HLS Design Assistant HLS Design Test Under Test Vectors (DUT) Bug-free Testbench C Simulation Bugs HLS Design RTL Co- Industrial HLS Generation Simulation Debugging Flow |
|---|
|  |


**Table (Page 9):**

|  | LLM Debugging Assistant |
|---|---|
|  |  |


**Table (Page 9):**

| Refined HLS Design |  |
|---|---|
|  |  |


**Table (Page 9):**

| Output |
|---|
| Specific Bug Injection |
