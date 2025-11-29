---
title: "HydraLoRA Asymmetric Architecture"
original_file: "./HydraLoRA_Asymmetric_Architecture.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["llm", "rag", "chain-of-thought", "agents", "fine-tuning"]
keywords: ["lora", "tuning", "page", "fine", "hydralora", "matrix", "editors", "moe", "parameter", "efficient"]
summary: "<!-- Page 1 -->

HydraLoRA: An Asymmetric LoRA Architecture for

### Efficient Fine-Tuning


### ChunlinTian† ZhanShi† ZhijiangGuo

UniversityofMacau UniversityofTexasatAustin UniversityofCambridge
yc27402@um.edu.mo zshi17@cs.utexas.edu zg283@cam.ac.uk

### LiLi* ChengzhongXu

UniversityofMacau UniversityofMacau
llili@um.edu.mo czxu@um.edu.mo

### Abstract

AdaptingLargeLanguageModels(LLMs)tonewtasksthroughfine-tuninghas
beenmademoreefficientbytheintroductionofParameter-EfficientFine-Tuning
(PEF"
related_documents: []
---

# HydraLoRA Asymmetric Architecture

<!-- Page 1 -->

HydraLoRA: An Asymmetric LoRA Architecture for

### Efficient Fine-Tuning


### ChunlinTian† ZhanShi† ZhijiangGuo

UniversityofMacau UniversityofTexasatAustin UniversityofCambridge
yc27402@um.edu.mo zshi17@cs.utexas.edu zg283@cam.ac.uk

### LiLi* ChengzhongXu

UniversityofMacau UniversityofMacau
llili@um.edu.mo czxu@um.edu.mo

### Abstract

AdaptingLargeLanguageModels(LLMs)tonewtasksthroughfine-tuninghas
beenmademoreefficientbytheintroductionofParameter-EfficientFine-Tuning
(PEFT)techniques,suchasLoRA.However,thesemethodsoftenunderperform
comparedtofullfine-tuning,particularlyinscenariosinvolvingcomplexdatasets.
Thisissuebecomesevenmorepronouncedincomplexdomains,highlightingthe
needforimprovedPEFTapproachesthatcanachievebetterperformance. Through
aseriesofexperiments, wehaveuncoveredtwocriticalinsightsthatshedlight
onthetrainingandparameterinefficiencyofLoRA.Buildingontheseinsights,
wehavedevelopedHydraLoRA,aLoRAframeworkwithanasymmetricstructure
thateliminatestheneedfordomainexpertise. Ourexperimentsdemonstratethat
HydraLoRAoutperformsotherPEFTapproaches,eventhosethatrelyondomain
knowledgeduringthetrainingandinferencephases.
1 Introduction
LargeLanguageModels(LLMs;[10,3,35,45,46,31,32])arenotablypowerful,yettheirtraining
involvessubstantialexpense. AdaptingasingleLLMformultipledownstreamapplicationsviafinetuninghasemergedasaprevalentmethodtocatertospecificdomainneeds,balancingperformance
withpracticality. Thisapproach,however,facesasignificantchallengeduetotheextensivememory
and computational resources required for full fine-tuning (FFT), i.e., fine-tuning all billions of
parameters. Asolutiontothishasbeenthedevelopmentofmoreselectiveadaptationtechniques,
involvingmodifyingonlyaportionoftheparametersorintegratingexternalmodulesdesignedfor
newtasks. KeymethodologiesinthissphereincludeLoRA[17],Adaptors[36,16,30],andmany
othervariants[24,23,9,13,51], allpartofwhatcanbegenerallytermedasParameter-Efficient
Fine-tuning(PEFT).PEFTstrategiesarecharacterizedbyfreezingthebackbonemodelparameters
whileonlyaminimalnumberoftask-specificparametersareintroducedandfine-tuned. Thismethod
substantiallyboostsefficiencyinthephasesoffine-tuningandsubsequentdeployment,markinga
significantadvancementinthepracticaluseofLLMs.
Whilefine-tuningasmallsubsetofparametersoffersastreamlinedapproachfordomainadaptation,
it’swell-recognizedthatmodelperformanceiscloselytiedtothenumberofparametersinvolved[21].
This intrinsic characteristic of methods like LoRA often results in them falling short of the FFT
baseline,whichupdatesallparameters,therebycreatingatrade-offbetweenefficiencyandmodel
quality.Thisissueofcompromisedqualityinalow-parametersettingbecomesevenmorepronounced
intargetdomainscharacterizedbycomplexsub-domainsanddiversetasks. Thissituationpresentsa
compellingresearchquestion:
Preprint.Underreview.
4202
yaM
32
]LC.sc[
2v54291.4042:viXra

<!-- Page 2 -->

...
...

’

(a) (b) (c)
(C) AutoLoRA: Split-fusion multi-LoRA framework.
Figure1: IllustrationofLoRAarchitecturechangesinHydraLoRA.Onlythetunableparameters Tasks
areshowninthisFigure. (a)LoRAarchitecturewithmatrixAtoachievelowrankandmatrixBAtouto-Router
recover. (b)underthesameparametercount,amonolithicLoRAissplitintomultiplesmallerAand
Bmatricestoavoidtraininginterference. (c)basedon(b),HydraLoRAhasanasymmetricstructure ...
thathasasharedAmatrixandmultipleBmatrices.


### A Shared A module

Whatistheoptimalarchitecturethatcandeliversuperiormodelperformancewhilestillcapitalizing
ontheefficiencybenefitsofareducedparameterfootprint? Auto Split Corpus
Inourresearch,wecarryoutaseriesofexploratoryexperiments,applyingLoRAtotheLLaMA2[46] ...
modeltoadaptittoanewdomainencompassingmultipledownstreamtasks. AsshowninFigure1(a),

LoRAaddstrainablepairsofrankdecompositionmatricesAandBinadditiontoexistingweight A
matrices. Our in-depth analysis of LoRA’s mechanics yields several insightful observations and

### Auto Init. # of LoRA

leads to the formulation of key hypotheses. First, rather than employing a single LoRA for the
...
entiredomain,itprovesmoreeffectivetodeploymultiple,smallerLoRAheads,eachdedicatedto
aspecificdownstreamtask(seeFigure1(b)). Thissuggeststhatdomainortaskinterferencemight

### Hybrid Corpus

harmfullyimpactthetrainingprocess. Wefurtherhypothesizethatthisinterferenceoriginatesfrom
“intrinsiccomponents”—sub-domainsordistincttasks—potentiallyunknowneventodomainexperts.
Additionally, upon visualizing the parameters of LoRA, we discern a pattern: some parameters
predominantlylearnthecommonalitiesacrossalldata,whileothersfocusontheuniqueaspectsof
each intrinsic component. From these observations, we posit that an optimal LoRA architecture
shouldembodyanexplicit,asymmetricstructure.
Building upon the observations, we propose an improved end-to-end LoRA framework, which
werefertoasHydraLoRA.Fromthearchitectureperspective,unlikeLoRA’ssymmetricstructure,
HydraLoRAhasanasymmetricstructurethathasasharedAmatrixandmultipleBmatrices(see
Figure1(c)). ThesharedAmatrixisusedbyallsamplesforparameterefficiency. Duringthefinetuningphase,HydraLoRAisdesignedtoautonomouslyidentify“intrinsiccomponents”andsegregate
trainingsamplesintodistinctBmatrices. Duringtheinferencephase,HydraLoRAleveragesmultiple
B matrices using Mixture-of-Experts (MoE; [19, 39]) manner. Unlike prior work, HydraLoRA
completelyeliminatestheneedforhumanexpertiseandassumptions,showingbetterperformance
thanusingdomainknowledgetoguidethefine-tuningprocess.
2 BackgroundandMotivation
2.1 LoRABasics
LoRA[17]achievescomparableperformancestofine-tuningonmanybenchmarksbyfreezingthe
pre-trainedmodelweightsW andinsertingtrainablerankdecompositionmatricesintoeachlayerof
0
thepre-trainedmodel. Inparticular,foreachlayer,LoRAusestwosequentiallow-rankmatricesA
andBtofittheresidualweightsforadaptation. Theforwardcomputationiswrittenasfollows:
y =y+∆y =W x+BAx (1)
0
′
where y R d is the output and the x R k denotes the input. B R d×r,A R r×k with
∈ ∈ ∈ ∈
r min(d,k). Normally matrix B is initialized with zeroes and matrix A is initialized with
≪
KaimingUniform[14]toforce∆y =0atthebeginning.
2.2 LoRA’sPracticalDilemma
Parametercounthasaclearimpactontheperformanceofneuralmodels[21,32]. Yet,Parameter-
EfficientFine-tuning(PEFT)methods,suchasAdapter[16]andprefix-tuning[24],focusonfine-
2

<!-- Page 3 -->

tuningalimitedsetofparameters. Theseapproachespresentapracticaldilemma: whilerestricting
thenumberoftunedparametersisessentialfortrainingefficiency,ithindersthemodel’sabilityto
learnfromdiversedatasets. Thistrade-offbecomesparticularlyevidentwhenconsideringcorpus
heterogeneity[2]. Figure2revealsanotableperformancedisparitybetweenPEFTtechniquesand
fullfine-tuning(FFT),withthegapwideninginscenariosinvolvingamorediverseorheterogeneous
trainingcorpus.
Corpus Heterogeneity
ecnamrofreP
Table1: Performanceoninstructiontuningwith

### Dolly-15K[8]andevaluatedwithMMLU[15]with

differentranks.ForLoRA(Split)decomposeshigh-

### Increased Gap

rankLoRAmodulesintosmaller,equivalentlowrankcomponents(r×n).nisthenumberofLoRAs,
Full Parameter Fine-Tuning rdenotestherankofeachLoRA.
Parameter-Efficient Fine-Tuning
Schemes r n MMLU %Parameter
× ↑
Figure2: Performanceimpactofcorpusheterogeneity LoRA 8 1 43.22 0.062
on full fine-tuning vs. parameter-efficient fine-tuning. LoRA 16× 1 45.45 0.124
Heterogeneitysignifiesthediversitywithinthedataset, LoRA 32× × 1 46.59 0.248
oftenleadingtointerferenceduetoitsvariedcontentand LoRA(Split) 16 2 46.82 0.248

### LoRA(Split) 8 ×4 46.94 0.248

style[2].Parameter-efficientapproachesareparticularly LoRA(Split) 4×8 46.83 0.248
sensitive,sufferinggreaterperformancelossesinhetero- ×
geneouscases.
2.3 Observations
In this work, we aim for a PEFT approach that strikes a better balance between maximizing the
learningcapabilityforheterogeneousdataandminimizingthenumberofparametersinvolved. A
keygoalistoensurethatourenhancedtechniqueexhibitsrobustgeneralizationacrossunseentasks,
independentofanypriortask-specificknowledge. Toachieveourobjectives,wefocusonLoRAand
conductaseriesofexperimentsasTable1togainadeeperunderstandingofitsmechanisms. Our
methodologyinvolvesleveragingdatafromdiversetaskswithinadomain,andtrainingdistinctLoRA
headsforeachdomain,leadingtoourfirstobservation:
ObservationI:Withthesameparametercount,ratherthanemployingasingleLoRAfortheentire
domaindataset,itprovesmoreeffectivetodeploymultiple,smallerLoRAheads,eachdedicatedtoa
specificdownstreamtask.
Thissuggeststhatinterferenceamongtasksmightharmfullyimpactthetrainingprocess.Furthermore,
wepositthatthisinterferenceisNOTexclusivetothisexplicitmulti-tasktraining. Thisinterference
couldhappeninanytrainingsettingsincealldatasetsinherentlyconsistofmultipleimplicitintrinsic
components,suchassub-domainsortaskswithinadomainthatisevenunknowntodomainexperts.
TobetterunderstandhowmultipleLoRAheadsmitigatetheinterferenceamongintrinsiccomponents,
inFigure3,weemploythet-SNEtechnique[47]tovisualizetheparametersofmatrixAandBacross
allheads. Thisanalysisyieldsanothercriticalobservation:
ObservationII:WhenmultipleLoRAheadsaretrainedindividuallyondifferentdata,theparameters
ofmatrixAfromdifferentheadstendtoconverge,whilethoseofmatrixBaredistinguishable.
Indetail,theparametersofmatrixAacrossallheadsexhibitahighdegreeofsimilarity,leadingto
theiroverlapsinthefigure. Conversely,theparametersofmatrixBfromdifferentheadsaredistinct
andeasilydistinguishable. Wepositthatthisdivergenceisanartifactoftheinitializationschemes,
withmatrixAinclinedtowardcapturingcommonalitiesacrossdomains,whilematrixBadaptsto
domain-specific diversities. The distinction between matrix A and B offers valuable insights for
enhancingbothparameterefficiencyandeffectiveness. Fromanefficiencystandpoint,ourhypothesis
suggeststhattheparametersofmatrixAcouldpotentiallybesharedacrossmultipleheads,thereby
reducingredundancy. Regardingeffectiveness,sincetheparametersofmatrixBofdifferentheads
aredispersed,suggestingthatusingasingleheadtoadapttomultipledomainsmightbelesseffective
thanusingindividualheadsforeachdomain,whichminimizestheinterferencebetweendomains.
Buildinguponourobservations,weproposeanoptimizedLoRAarchitecturedesignedtoenhance
cost-effectiveness. In this architecture, we share the parameters of A matrix across various subdomainsortaskstoimproveparameterefficiency,whiledeployingmultipleBmatrices,eachtailored
3

<!-- Page 4 -->

t-SNEVisualizationofBA-MatrixDiff.LoRAs t-SNEVisualizationofA-MatrixDiff.LoRAs t-SNEVisualizationofB-MatrixDiff.LoRAs
− − 1 1 5 5 0 0 0 0 0 0 0 1 5 0 1 2 0 0 1 4 1 7 0 1 6 2 4 1 0 0 6 5 1 6 1 4 8 5 6 9 2 1 5 2 8 8 1 4 0 0 2 4 0 0 6 8 1 1 1 6 3 1 7 6 9 6 9 3 0 2 8 0 0 1 3 9 5 2 0 2 3 1 7 8 6 9 2 6 4 0 7 5 4 1 7 2 6 1 2 5 1 35 3 7 6 6 9 2 6 11 1 11 6 3 1 4 3 3 3 7 1 1 5 6 0 1 7 1 1 8 1 2 0 0 6 8 1 9 07 0 1 91 1 1 5 2 43 2 1129 5 9 3 1 4 61 327 7 2 9 17 5 71 1 6 5 5 9 99 5 9 8 5 1 3 3 1 19 1 1 0 4 4 1 2 7 0 03 1 5 0 5 5 4 8 1 8 2 8 1 7 9 2 9 5 4 7 8 8 1 4 2 77 3 3 2 6 9 9 4 8 3 3 7 5 5 0 9 1 4 5 3 6 4 0 2 7 0 8 8 8 1 2 8 2 2 3 6 1 5 1 9 4 1 2 7 1 3 4 2 4 4 2 7 8 A S Q IE 1 7 U L A 2 4 8 1 L M 0 00 118 − − 1 1 0 0 5 5 0 0 0 0 0 1 5 0 1 2 0 0 1 4 1 7 0 1 6 2 4 1 0 0 6 5 1 6 1 4 8 5 6 2 5 2 8 8 1 4 0 4 0 0 6 6 3 7 6 0 2 8 0 9 2 0 2 1 8 2 6 0 2 6 2 1 6 6 2 6 3 1 4 3 3 6 0 0 0 6 8 9 1 6 5 1 0 4 7 0 10 4 8 2 8 1 9 2 4 8 1 4 2 6 9 4 8 7 5 0 4 5 6 4 0 2 0 8 8 8 1 2 8 2 2 3 6 1 1 9 4 1 2 1 4 2 4 4 2 8 S Q I A 1 7E U 2 L A 4 8 1 0 M 0 L 0 118 − − − 7 5 2 2 5 7 5 0 5 5 0 5 0 9 1 5 0 0 2 1 8 1 1 1 9 9 6 3 0 1 3 5 3 79 67 4 15 4 7 1 5 3 5 3 7 9 1 1 6 111 5 3 7 1 1 7 1 0 2 1 1 8 1 9 0 0 117 3 9 1 5 2 1 1 4 9 5 2 112 3 7 1 1 2 4 67 3 9 17 2 7 5 55 91 5 9 9 9 3 3 8 11 1 19 4 1 2 5 03 5 1 5 7 89 5 7 8 7 3 7 3 2 9 3 3 5 9 1 3 5 7 0 S Q I A 5 E U L A 7 3 M L7 65
− − − − −
Figure3: BreakdownanalysisofLoRAmodules.Comparefine-tunedLoRAmodulesofDolly-15K[8]with
threesubtasksofDolly-15Kincluding“summarization(Sum)”,“closedQA(QA)”and“informationextraction
(IE)”usingt-SNE.ConsiderLLaMA2-7B(randomseed=42),whichcontains32decoderlayers,corresponding
to32adaptivemodules.Eachmoduleconsistsof{0:q_projofA,1:q_projofB,2:v_projofA,3:v_projofB}
submodules. Thismakesatotalof32×4submodules. Leftdisplaysallsubmodules. Centershowsalleven
submodules,i.e.theAmatrix.Rightrepresentsalloddsubmodules,i.e.theBmatrix.Itcanbeseenthatthe
differencesinthefine-tunedLoRAmodulesfordifferenttasksarisemainlyfromtheBmatrix.
to handle different intrinsic components. This design allows for a more effective adaptation to
thespecificcharacteristicsofeachcomponent. Whiletheseintrinsiccomponentscanbemanually
identifiedusingpriorknowledgeofthetrainingdata,wealsointroduceend-to-endmethodsusing
Mixture-of-Experts(MoEs)[20],whichwillbedetailedinthemethodologysection. Thisautomatic
approachfacilitatesflexibilityandapplicability,particularlyinscenarioswherepriorknowledgeis
limitedorunavailable.
3 HydraLoRA
Inthissection,weintroducetheproposedHydraLoRA,anasymmetricLoRAarchitectureforefficient
fine-tuning,asillustratedinFigure1. Afterthat,weshowtheworkflowofHydraLoRAasFigure4.
3.1 AsymmetricLoRAarchitecture
TheLoRAmethodupdatestwolow-rankmatricesAandB,andusesABasthechangeofapretrained
andfrozenweightW ofalinearlayerasshowninEq. 1. Theintegralparametersarefine-tunedfor
0
thewholecorpusintheoriginalLoRA,whichcausesdifficultyinlearningthevariousknowledge
aspects. DrawingfromadetailedbreakdownanalysisofLoRA,apotentialsolutionistosegment
theentireLoRAinto“Hydra”structuredLoRAvariants,thatis,characterizedbyacentralshared
matrixAandseveraldistinctmatricesB, fosteringablendofsharedknowledgeandspecialized
functionalities.AsFigure1,HydraLoRAistofine-tuneLoRAstoachieverobustperformancewithout
redundancy,therebybenefitingtheentireheterogeneouscorpus. TheasymmetricLoRAarchitecture
canbeformulatedas:

## W =W +∆W

0
(cid:88) N (2)
=W + ω B A
0 i i
·
i=1
ThematricsB Rd×r andsharedA Rr×k. Thehyper-parameterN denotesthenumberofB
i
∈ ∈
matrices. Thetermω modulatesthesecontributionweightsforheadB .
i i
3.2 WorkflowofHydraLoRA
Figure 4 illustrates the workflow of HydraLoRA. Initially, HydraLoRA delves into the adaptive
identificationandinitializationofLoRAmoduleswithinaheterogeneouscorpus,aligningthemwith
taskrelevancethroughtheapplicationofk-meansordeveloper-specifiedsize. Subsequently, we
proposeaMixture-of-Experts(MoE)frameworkthathandlesBmatricesasexpertadapterstoensure
computationalefficiencythroughoutthefine-tuning(Section3.2.1)andinference(Section3.2.2)
stagesbyfreezingtherestoftheLLMparameters. Duringinference,itflexiblyanddynamically
mergesmultipleBmatricesthroughtheMoErouter.
4

<!-- Page 5 -->

A. Fine-Tuning B. Inference
Mixed-task Input

## Initialization


### Attention A

Identify intrinsic ... ...
components

### Heterogeneous LN

Corpus InitializedHydraLoRA FNN Router
∆ ∆ ∆

## Ln


## Tuning 3.Inference

...
Pretrained Routing LoRA Merge
Segregate training Weights
samples to intrinsic

### Router components by MoE Trained HydraLoRA Output

Figure4: ArchitectureandworkflowofHydraLoRA.Duringthefine-tuningstage,HydraLoRAfirstadaptively
identifies and initializes k of intrinsic components without specific domain knowledge. It then employs a
trainableMoErouterthattreatseachintrinsiccomponentasanexperttoautomaticallysegregatetrainingsamples
intointrinsiccomponentsforfine-tuning.Duringtheinferencestage,HydraLoRAmergesmultipleBmatrices
flexiblyanddynamicallythroughatrainedrouter.
3.2.1 Fine-tuning
MotivatedbyMixture-of-Experts(MoE;[19,39]),whereexpertsareselectivelyactivatedbyagating
mechanism(Router)inresponsetodifferentinputs. InHydraLoRA,wesubstituteeachexpertwitha
lightweightLoRAadapter. Duringfine-tuning,whileweightsofLLMsremainfrozen,theexpertsand
routerlayersaretrainedfromscratch. Inordertoachieveaunifiedapproachtothedistinctforward
processesofmultipleBmatrices,wedefineasetofexperts,denotedas(E ,...,E ),tolearnthe

## 1 N

updated matrix ∆W. As HydraLoRA fine-tunes the experts using the heterogeneous corpus, the
sharedmatrixAinherentlycapturescollaborativeknowledgetoaugmentintra-gains,anddifferent
matricesBfosterknowledgemodularitytomitigatefine-tuninginter-offsets. Basedonthisstructure,
theforwardprocessofHydraLoRAisexpressedas:

## N

(cid:88)
y =W x+ ω E Ax (MoE) (3)
0 i i
i=1
whereN denotesthenumberofexperts,i.e.,Bmatrices.Toregulatethesecontributions,weintroduce
a gate function (router network) commonly consisting of a dense layer with trainable weights
(transformationmatrix)W Rr×N followedbyasoftmaxfunctionwhichtakesanintermediate
g
∈
tokenrepresentationxasinputandcombinestheoutputofeachexpertbasedonthegatingscores
(ω ,...,ω ):

## 1 N

ω =softmax(WTx) (Router) (4)
i g
3.2.2 Inference
Duringinference,HydraLoRAmergesadaptersbyenablingroutingcomputationbasedontheinput.
Specifically,sincematricesBoperateaslinearfunctions,weinitiallycomputeaweightedaverage
oftheexperts. Followingthis,weapplyaPEFTtransformationusingthecombinedexpertise. The
HydraLoRAsignificantlyenhancestrainingefficiencythroughanextremelyparameter-efficientMoE
formulation. Additionally,theintrinsicstructuralmodularityofHydraLoRAfacilitatesrapidrecovery
andmergingofthetrainedparametersduringinference,leadingtosubstantialmemorysavings.
4 Experiments
Inthissection,wedetailtheprincipalexperiments. Webeginwithanoverviewoftheexperimental
setup and implementation intricacies. Following this, we share our findings and offer a succinct
interpretation.
4.1 ExperimentSetting
DatasetandBenchmarks ToexplorethepropertiesandcommonalitiesoftheLoRAasymmetric
structure,weconductexperimentsonbothsingleandmultipledomainstoevaluatetheeffectiveness
5

<!-- Page 6 -->

Table2: Comparativeperformanceofdifferenttuningschemesacrossmultiplebenchmarksonasingledomain.
8-shotforGSM8K,zero-shotforothers.#B¯referstotheaverageBmatrixnumber.
Schemes MMLU Medical Law HumanEval GSM8K %Param #A #B¯

## P@1 P@10


### LLaMA2-7B[46] 38.88 35.98 33.51 13.10 20.34 10.38 - - -


### FullFine-Tuning 49.91 46.78 46.08 20.24 32.93 25.70 100 - -

PromptTuning[23] 39.91 37.59 35.02 13.66 21.55 13.18 0.001 - -
P-Tuning [28] 41.11 39.81 36.72 13.60 21.13 15.56 0.193 - -
(256)
PrefixTuning[24] 41.78 40.28 36.54 13.23 22.56 16.89 0.077 - -
(IA)3[26] 40.45 37.12 35.25 13.54 23.17 13.98 0.009 - -
AdaLoRA [52] 44.32 42.83 39.36 14.81 23.78 19.51 0.093 1 1
(r=8)
LoRA [17] 43.22 41.59 37.85 15.67 22.95 18.24 0.062 1 1
(r=8)
LoRA 45.45 43.10 39.64 16.71 25.60 20.32 0.124 1 1
(r=16)
LoRA 46.59 44.32 40.81 17.12 25.89 20.67 0.248 1 1
(r=32)
LoRA-Split 46.94 45.28 41.35 18.20 26.85 21.92 0.248 4 4
(4×8)
HydraLoRA 47.22 45.71 42.18 18.31 27.43 22.27 0.124 1 3
(r=8)
ofHydraLoRAforprofilingintrinsiccomponents. Singledomain. 1)General: wefine-tunewith
•
thegeneralinstructiontuningdatabricks-dolly-15k[8]forgenericlanguagecapabilityandevaluate
withMMLU[15]. 2)Medical: wefine-tunewithGenMedGPTandclinic-10kfromChatDoctor[25]
formedicineapplicationsandevaluatemedicaltasksinMMLU.3)Law: wefine-tunewithtwolegal
instructiontuningdatasetsLawyer-Instruct[1]andUS-Terms[4]thenevaluatewithlawtasksin
MMLU.4)Math: wefine-tunewiththetrainingsplitofGSM8K[7]formathematicalreasoningand
evaluatewithtestsetofGSM8K.5)Code: wefine-tunewithCodeAlpaca[5]forcodegenerationand
evaluatewithHumanEval[6]. Multi-taskdomain. WeselectaportionoftheFlanv2[49]datasets
•
coveringNaturalLanguageUnderstanding(NLU)andNaturalLanguageGeneration(NLG),which
canbegroupedinto10distincttaskclusters. ThenweevaluateitwiththeBig-BenchHard(BBH)
[44]benchmark. AdetaileddescriptionofthebenchmarkscanbefoundinAppendixA.1.
Baselines First,wecompareHydraLoRAwithdifferentPEFTmethodsonsingledatasets: 1)
Full fine-tun • ing; 2) Prompt Tuning [23]; 3) P-Tuning [28]; 4) Prefix Tuning [24]; 5) IA3 [26]; 6)
AdaLoRA[52]. Second,weextendtheexperimentsexploringHydraLoRAonmultipledatasets
•
comparedwithmoreweightedaveragemethods: 1)Lorahub[18]employsblack-boxoptimization
tolearnweightsof20randomlyselectedLoRAsfornewtasks,usingweightedaveragingwithout
needinggradientcalculations. 2)LoRAMoE[50]combineslightweightexperts(LoRA)withMoE
architecture for high efficiency, generalizing to new tasks without prior knowledge. A detailed
descriptionofthebaselinemodelscanbefoundinAppendixA.2.
4.2 OverallPerformance
TheexperimentalresultsofHydraLoRAandthecompetingbaselinesarepresentedinTable2witha
singledomainandTable3withthemixedtaskdomain. Theevaluationofdiversetasksdemonstrates
that HydraLoRA consistently outperforms all other schemes. The performances rooted in LoRA
outperform those of conventional PEFT methodologies. Compared to the default single LoRA
configuration(rank=8),theHydraarchitecture,enrichedbytheintegrationofseveralBmatrices,
effectivelyaddressestheinherentconflictsamongintrinsiccomponentsofthecorpus. Furthermore,
withequivalentparameters(rank=16),themodelshowssuperiorperformance,confirmingtheeffectivenessoftheadoptedparameters. BasedonTable2andTable3, weproposethreeresearch
questionsthatconfirmtheaforementionedobservations.
RQ1: IsitmoreeffectivetousemultiplesmallerLoRAheadsforspecifictasksratherthanone
singleLoRAfortheentiredomaindataset,giventhesameparametercount? Comparingthe
high-dimensionalLoRAconfigurationwithr =32againstasegmentedversionusingLoRA-Split,a
variantintroducedbyHydraLoRA,whichdividesthemodelintofourdistinctcomponentseachwith
r =8. Thatis,multiplevanillaLoRAsaredirectlyutilizedtocapturethedifferencesbetweendata.
WeobserveanoteworthytrendintheperformanceacrossavarietyoftasksasdetailedinTable2. It
illustratesthesuperiorperformanceofLoRA-SplitincomparisontothetraditionalLoRAapproach,
acrossalltheevaluatedscenarios. Thisenhancementinperformanceisastrongindicationofthe
detrimentalimpactthattaskinterferencecanhaveonthetrainingprocess. Bysegregatingthetasks
6

<!-- Page 7 -->

Table3: Comparativeperformanceofdifferenttuningschemes,includingbasemodel(Base),LoRAtuning
(LoRA),LoraHublearning,multi-LoRAtuningwithMoEinference(LoRAMoE)andourproposedHydraLoRA
learningacrossmix-taskdomainontheBBHbenchmarkwithLLaMA2-7B,LLaMA2-13BasthebaseLLM
(3-shot).RefertoAppendixDfordetails.
Metrics Base[46] LoRA[17] Lorahub[18] LoRAMoE[50] HydraLoRA

## 7B 31.6 36.8 39.7 40.3 41.5


### Performance


## 13B 38.4 40.1 41.9 43.7 44.1

# ofA/Bfortraining 0/0 1/1 48/48 48/48 1/10
# ofA/Bforinference 0/0 1/1 20/20 48/48 1/10
%Params - 0.062 1.240 2.976 0.341
intodiscretecomponents,LoRA-Spliteffectivelyminimizestheconflictandinterferencebetween
tasks,therebypromotingamoreefficientandfocusedenvironment.
TheconceptofLoRA-Splithingesontheconstructionofdifferentintrinsiccomponentcompositions,
employingLoRAasafoundationaltechniquetostrategicallymitigatetheinterferenceconflict. This
architecturalinnovationhasproventobeapivotalfactorinenhancingmodelperformance. However,
it’simportanttonotethatwhileLoRA-Splitmarksasignificantadvancementinmodelefficiencyand
taskhandling,italsointroducesacertainlevelofparameterredundancy. Thesegmentedapproachof
LoRA-Splitinevitablyleadstoanincreaseintheoverallmodelparameters,whichcanbemanifoldin
comparisontothetraditional,singularLoRAmodel. Thisincreaseinparameters,whilecontributing
tothemodel’srobustnessandcapabilitytohandlemultipletaskssimultaneously, alsoposesnew
challengesintermsofcomputationalresourcesandmodeloptimization.
RQ2: WillmultipleLoRAheads,individuallytrainedondifferentdata,improveefficiencyby
distinguishingmatrixBparameters? WeevaluatedtheHydrastructureLoRA—HydraLoRA
that is characterized by a shared LoRA A matrix, while maintaining distinct B matrices that are
trainedseparately. ThisconfigurationwasmeticulouslycomparedwithboththestandardLoRAand
theLoRA-Splitapproaches,emphasizingefficiencyparameters.
AccordingtotheresultspresentedinTable2,unlikesplitwhichstraightforwardlyadoptsmultiple
vanillaLoRAs,HydraLoRAadoptsanasymmetricLoRAstructurethatnotonlyimprovesparameter
efficiencybyseparatingtheusesofAmatrixforcommonalitiesandBmatricesfordiversitieswitha
notablysmalleradapterparameterset,butalsoemploysatrainableroutertoimprovethecomposition
ofmultipleBmatricesthatoutperformstheLoRA-Splitapproach. Thisfindingissignificantasit
suggeststhatHydraLoRAnotonlyenhancesperformanceefficiencybutalsoboostsoverallsystem
effectiveness. This may be driven by 1) different B matrices capturing different features of the
data-intrinsic knowledge, mitigating mutual interferences, and avoiding performance offsets. 2)
ModuleAmaintainsthecollaborativeknowledgebytakingthestrengthsofeachandintegrating
themtoimprovethemodelperformance.
RQ3: HowdoesHydraLoRAfareagainstothermergemethodsincomplex,multi-taskdomains,
considering scalability and robustness? While we hypothesize that the asymmetry is mainly
rootedinthedifferentinitializationmethodsofAandBmatrices,itispossiblethatthisbehavior
varies on different model architectures and datasets. To the best of our ability, we extended the
experimentsexploringHydraLoRAonmultipledatasets. LoRAMoEandtheirvariantstypically
aimattacklingmulti-tasksbyemployingmultipleindependentLoRAs. Thismakesthemsuitable
for handling various domains. However, for a single dataset like ours, a “default” MoE method
mightnotbeoptimal. HydraLoRAaddressesthisbyconstructingasymmetricstructuresandutilizing
multipleBmatricestocapturethespecificnuanceswithinthesingledataset. Theeffectivenessofthis
approachisdemonstratedbytheexperimentalresultsinTable3.
4.3 EnergyandThroughputAnalysis
RQ4: Howdoesthe“Hydra”structureinHydraLoRAenhancesystemefficiency,particularly
inreducingtrainingenergyconsumptionandlatency? Weevaluatethesystemefficiencyof
HydraLoRAfromtwoperspectives: trainingenergyconsumptionandlatency. ThefollowingexperimentswereexecutedonaGPUinfrastructureconsistingof4NVIDIAA40GPUsandaCPUpowered
byanIntel(R)Xeon(R)Gold6330CPUclockedat2.00GHz. Powerconsumptionmeasurements
7

<!-- Page 8 -->

   
   
   
   
   
   
   
 & 3 8  * 3 8  5 $ 0
)hWK(
ygrenE

##  / R 5 $  U      


##  / R 5 $  U     


##    / R 5 $  U     


##  / R 5 $  6 S O L W   [    


##  + \ G U D / R 5 $  

 
 

##  5     5      5      6 S O L W + \ G U D / R 5 $

)h(
ycnetaL
Figure 5: Energy consumption and latency during fine-tuning with different LoRA approaches
(fine-tuningLLaMA2-7BwithGSM-8K).
50.0
47.5
45.0
42.5
40.0
37.5
35.0

##  0 P O X  0 H G L F D O  / D Z

)%(
ecnamrofreP
46.9447.22 w/o MoE
45.2845.71 w/o Gate
w/o Hydra
43.2242.81 HydraLoRA
42.18
41.59 40.92 41.35
37.85
37.12
Figure6: ComparativeperformanceofablationstudyforHydraLoRAacrossmultiplebenchmarks.
wererecordedusingCodeCarbon[33]. Figure5showstheresultsofvariousfine-tuningapproaches
forGSM-8KusingtheLLaMA2-7Bmodel. wecanseethatHydraLoRAeffectivelyspeedsupthe
trainingprocess1.96 andreduces49.6%energycostcomparedtoLoRA(rank=32). Whilethe
×
energyconsumptionandlatencyofLoRA-SplitexceedstheLoRA(rank=32). Thisisforthereason
thatHydraLoRAjointlyconsidersinherentknowledgemodularityandcollaboration,whichutilizes
the“Hydra”structurewithasharedAmatrixanddifferentBmatrix. Inthisway,itonlyemploys
rank=16trainingoverheadbutexpandstoaperformanceenhancementofmorethanrank=32. Overall,
thisexperimentdemonstratestheparametereffectivenessofHydraLoRA.
4.4 AblationStudy
RQ6: What impact do the MoE architecture and the gate function have on the fine-tuning
process? TodelvedeeperintounderstandingthecontributionsofeachcomponentinHydraLoRA.
wepresenttheresultsofourablationstudyinFigure6. Thevariantw/oMoE(essentiallyrevertsto
LoRA)excludestheMoEarchitecture.Similarly,thew/ogatevariantemploysuniformexpertweights
bypassingthegatefunction. Thew/ohydraadoptsmultiplevanillaLoRAsinastraightforwardway.
Figure6indicatesthatthefullHydraLoRAmodeloutperformsitsvariants,showingthatboththeMoE
architectureandgatefunctionsignificantlycontributetoitseffectivenessacrossvariouslanguage
understandingdomains.
4.5 Hyper-parameterAnalysis
RQ7: HowdothenumberofintrinsiccomponentofHydraLoRAinfluenceperformanceoutcomes? AsFigure8shown,weconductacomprehensiveandmeticulousanalysisbyfine-tuning
theDolly-15KmodelontheLLaMA2-7Bdatasetandsubsequentlyevaluatingitsperformanceon
theMMLUbenchmarktorigorouslyexaminetheimpactofvariationsintheintrinsiccomponent,
symbolized by the variable k, on the model’s overall performance. Empirically we find that the
numberkofclustersisnotasensitiveparameterforHydraLoRA,withawiderangeofreasonable
numberkofclusters(e.g. 2to4)performingdecentlywellinallsettingsinourexperiments. Specifically,theperformancelossofk=3vs. theoptimalk=4isonly0.42%. Meanwhile,asillustrated
inFigure7,weemploythreedistinctmethodstogeneratethenumberofcorpusclusters15-fold,
andtheresultsdemonstratethatthek-means[29]yieldscomparableoutcomeswithDBSCAN[38].
Therefore,basedonthisobservation,wechoosek-meansbecauseitissimplebuteffective,more
sophisticatedhyperparametersearchapproaches(e.g. DBSCAN,parametersweepandBayesian
optimization) will be unnecessarily costly. It’s noteworthy that HydraLoRA is adeptly designed
toorchestrateitscomponentsinawaythatitcanautomaticallycalibrateandnavigatetowardthe
optimalperformanceconfigurationacrossvariousparameters. Thisintelligentauto-tuningisachieved
throughtheapplicationofthek-meansclusteringalgorithm. Thisstrategiccomponentorchestration
notonlyenhancesperformancebutalsoensuresamoreefficientandeffectiveutilizationofresources,
8

<!-- Page 9 -->

 
 
 
 
 
 
                  
sretsulC
fo
rebmuN
    
    
    
    

##  6 W D W L F     


##  .  P H D Q V     

 ' % 6 & $ 1     

##       N           

Figure7: Numberofclustersgeneratedbydifferentapproaches
includingdeveloper-specific(static),k-means,andDBSCAN.
)%(
ecnamrofreP
Figure8: Theresultsofexperimentsfor
hyper-parametersnumberofclusters.
underpinningthemodel’scapabilitytoadaptandperformefficientlyinadynamiccomputational
environment.
5 Relatedwork
Parameter-Efficient Fine-tuning LLMs are becoming increasingly powerful, but fine-tuning
themoftenrequiressignificantcomputationalresources. Thishasspurredresearchonparameterefficient fine-tuning (PEFT) techniques that reduce memory and storage costs during adaptation.
OneprominentPEFTapproachisadapters[16,36]. Itintroducesnew,trainabledenselayerswithin
the existing model, keeping the original parameters frozen. This concept has proven successful
across various domains [34, 41, 42, 53]. Further improvements on adapter compactness involve
constructing parameter matrices using Kronecker products of low-rank matrices [30]. Another
PEFTstrategydirectlymanipulatesactivationswithlearnedvectors. Thiscanbeachievedthrough
concatenation[28,24,23],multiplication(IA3;[26]),oraddition(BitFit;[51]).Prefix-tuning[24]and
prompt-tuning[23]arenoteworthyexamplesthatfine-tunecontinuouspromptsinsteadofdesigning
discreteones[9]. Interestingly,astudysuggeststhatmanyPEFTmethodscanbeviewedasaform
of adapter, providing a unified perspective [13]. Beyond adding new parameters or altering the
computationalgraph,researchersalsoexploresparse[12,43]orlow-rankupdates(LoRA;[17]).
Multi-LoRA Architecture LoRA has notably garnered increasing interest recently, becoming
a standard approach for adapting LLMs such as LLaMA [45, 46] under limited computational
resources. Recognizing its potential, researchers have delved deeper, exploring the benefits of
employing multiple LoRAs. LoraHub [18] takes this multi-LoRA approach by training several
adaptersandstrategicallypickingcombinationsbasedonthedomainduringinference. Meanwhile,
MultiLoRA[48]focusesonhorizontalscaling,aimingtoreduceLoRA’sparameterdependence. This
involvessplittingLoRAmodulesalongtherankdimensionandintroducinglearnablescalingfactors
forenhancedexpressiveness. Addressingscalingchallengesfromadifferentangle,themixtureof
LoRAconceptisfurtherproposed[50].Thismitigatesresourceconsumptionwhenscalinginstructiontuned LLMs. Recognizing the potential for conflict during instruction tuning, LoRAMoE [11]
leveragestheMixture-of-Experts(MoE;[19])structuretosafeguardthepre-trainedLLM’sknowledge
from excessive corruption by instruction data. Similarly, MOELoRA [27] incorporates a MoE
framework into LLMs, thereby improving their multitasking capabilities in the medical domain.
Shiftingthefocustothesystemperspective,S-LoRA[40]providesaframeworkforefficientlyserving
multipleLoRAadapters. UnlikepreviousmethodsthatreliedonchoosingLoRAcombinationsbased
ontheirtrainingdomains,HydraLoRAbreaksfreefromthedependenceondomainknowledgeduring
inference. Additionally,HydraLoRA’sasymmetricstructurefurtherenhancesparameterefficiency
comparedtoexistingsymmetricapproaches.
6 Conclusion
In this work, we start by conducting exploratory experiments applying the LoRA technique to
LLaMA2,aimingtoadaptittoanewdomainacrossvarioustasks. Thisstudyunveilsthelimitations
ofemployingasingleLoRAfortheentiredomain,highlightingthedetrimentaleffectsofdomain
interference. Inresponse,weintroduceanovelarchitectureHydraLoRAthatfeaturesanasymmetric
structurewithasharedmatrixforallsamplesanddistinctmatricesforeachintrinsiccomponent. This
designimprovesdomainadaptationbyselectivelyfocusingondistinctcomponents,enhancingboth
fine-tuningandinferenceefficiency. Ourresearchhighlightstheimportanceofbalancinglearning
capabilities for diverse datasets against the need for a lean model, offering a viable pathway for
9

<!-- Page 10 -->

improvingLLMswithminimalparametergrowth. Morediscussionaboutlimitationandbroader
impactsareavailableinAppendixEandF.

### References

[1] Alignment-Lab-AI. Lawyer-instruct,2024.
[2] SaraBabakniya,AhmedRoushdyElkordy,YahyaH.Ezzeldin,QingfengLiu,Kee-BongSong,
MostafaEl-Khamy,andSalmanAvestimehr. Slora: Federatedparameterefficientfine-tuningof
languagemodels. CoRR,abs/2308.06522,2023.
[3] TomB.Brown,BenjaminMann,NickRyder,MelanieSubbiah,JaredKaplan,PrafullaDhariwal,
ArvindNeelakantan,PranavShyam,GirishSastry,AmandaAskell,SandhiniAgarwal,Ariel
Herbert-Voss, Gretchen Krueger, Tom Henighan, Rewon Child, Aditya Ramesh, Daniel M.
Ziegler, Jeffrey Wu, Clemens Winter, Christopher Hesse, Mark Chen, Eric Sigler, Mateusz
Litwin,ScottGray,BenjaminChess,JackClark,ChristopherBerner,SamMcCandlish,Alec
Radford,IlyaSutskever,andDarioAmodei. Languagemodelsarefew-shotlearners. InHugo
Larochelle,Marc’AurelioRanzato,RaiaHadsell,Maria-FlorinaBalcan,andHsuan-TienLin,
editors,AdvancesinNeuralInformationProcessingSystems33: AnnualConferenceonNeural
InformationProcessingSystems2020,NeurIPS2020,December6-12,2020,virtual,2020.
[4] IliasChalkidis,NicolasGarneau,CatalinaGoanta,DanielKatz,andAndersSøgaard. LeXFiles
andLegalLAMA:FacilitatingEnglishmultinationallegallanguagemodeldevelopment. In
Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics
(Volume1: LongPapers),pages15513–15535,Toronto,Canada,July2023.Associationfor
ComputationalLinguistics.
[5] Sahil Chaudhary. Code alpaca: An instruction-following llama model for code generation.
https://github.com/sahil280114/codealpaca,2023.
[6] MarkChen,JerryTworek,HeewooJun,QimingYuan,HenriquePondedeOliveiraPinto,Jared
Kaplan,HarriEdwards,YuriBurda,NicholasJoseph,GregBrockman,etal. Evaluatinglarge
languagemodelstrainedoncode. arXivpreprintarXiv:2107.03374,2021.
[7] KarlCobbe,VineetKosaraju,MohammadBavarian,MarkChen,HeewooJun,LukaszKaiser,
MatthiasPlappert,JerryTworek,JacobHilton,ReiichiroNakano,ChristopherHesse,andJohn
Schulman. Trainingverifierstosolvemathwordproblems. arXivpreprintarXiv:2110.14168,
2021.
[8] MikeConover,MattHayes,AnkitMathur,XiangruiMeng,JianweiXie,JunWan,SamShah,
AliGhodsi,PatrickWendell,MateiZaharia,etal. Freedolly: Introducingtheworld’sfirsttruly
openinstruction-tunedllm,2023.
[9] MingkaiDeng,JianyuWang,Cheng-PingHsieh,YihanWang,HanGuo,TianminShu,Meng
Song,EricP.Xing,andZhitingHu. Rlprompt: Optimizingdiscretetextpromptswithreinforcementlearning. InYoavGoldberg,ZornitsaKozareva,andYueZhang,editors,Proceedingsof
the2022ConferenceonEmpiricalMethodsinNaturalLanguageProcessing,EMNLP2022,
AbuDhabi,UnitedArabEmirates,December7-11,2022,pages3369–3391.Associationfor
ComputationalLinguistics,2022.
[10] JacobDevlin,Ming-WeiChang,KentonLee,andKristinaToutanova. BERT:pre-trainingof
deepbidirectionaltransformersforlanguageunderstanding. InJillBurstein,ChristyDoran,and
ThamarSolorio,editors,Proceedingsofthe2019ConferenceoftheNorthAmericanChapterof
theAssociationforComputationalLinguistics: HumanLanguageTechnologies,NAACL-HLT
2019, Minneapolis, MN, USA, June 2-7, 2019, Volume 1 (Long and Short Papers), pages
4171–4186.AssociationforComputationalLinguistics,2019.
[11] ShihanDou,EnyuZhou,YanLiu,SongyangGao,JunZhao,WeiShen,YuhaoZhou,ZhihengXi,
XiaoWang,XiaoranFan,ShiliangPu,JiangZhu,RuiZheng,TaoGui,QiZhang,andXuanjing
Huang. Loramoe: Revolutionizing mixture of experts for maintaining world knowledge in
languagemodelalignment. CoRR,abs/2312.09979,2023.
10

<!-- Page 11 -->

[12] DemiGuo,AlexanderM.Rush,andYoonKim. Parameter-efficienttransferlearningwithdiff
pruning. InChengqingZong,FeiXia,WenjieLi,andRobertoNavigli,editors,Proceedings
of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th
InternationalJointConferenceonNaturalLanguageProcessing,ACL/IJCNLP2021,(Volume1:
LongPapers),VirtualEvent,August1-6,2021,pages4884–4896.AssociationforComputational
Linguistics,2021.
[13] JunxianHe,ChuntingZhou,XuezheMa,TaylorBerg-Kirkpatrick,andGrahamNeubig. Towards a unified view of parameter-efficient transfer learning. In The Tenth International
ConferenceonLearningRepresentations,ICLR2022,VirtualEvent,April25-29,2022.Open-
Review.net,2022.
[14] Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun. Delving deep into rectifiers:
Surpassinghuman-levelperformanceonimagenetclassification. InProceedingsoftheIEEE
internationalconferenceoncomputervision,pages1026–1034,2015.
[15] DanHendrycks,CollinBurns,StevenBasart,AndyZou,MantasMazeika,DawnSong,and
Jacob Steinhardt. Measuring massive multitask language understanding. arXiv preprint
arXiv:2009.03300,2020.
[16] NeilHoulsby,AndreiGiurgiu,StanislawJastrzebski,BrunaMorrone,QuentindeLaroussilhe,
AndreaGesmundo,MonaAttariyan,andSylvainGelly. Parameter-efficienttransferlearning
forNLP. InKamalikaChaudhuriandRuslanSalakhutdinov,editors,Proceedingsofthe36th
International Conference on Machine Learning, ICML 2019, 9-15 June 2019, Long Beach,
California,USA,volume97ofProceedingsofMachineLearningResearch,pages2790–2799.

## Pmlr,2019.

[17] Edward J. Hu, Yelong Shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean Wang,
LuWang,andWeizhuChen. Lora: Low-rankadaptationoflargelanguagemodels. InThe
TenthInternationalConferenceonLearningRepresentations,ICLR2022,VirtualEvent,April
25-29,2022.OpenReview.net,2022.
[18] ChengsongHuang,QianLiu,BillYuchenLin,TianyuPang,ChaoDu,andMinLin. Lorahub:
Efficientcross-taskgeneralizationviadynamicloracomposition. CoRR,abs/2307.13269,2023.
[19] Robert A. Jacobs, Michael I. Jordan, Steven J. Nowlan, and Geoffrey E. Hinton. Adaptive
mixturesoflocalexperts. NeuralComput.,3(1):79–87,1991.
[20] MichaelIJordanandRobertAJacobs. Hierarchicalmixturesofexpertsandtheemalgorithm.
Neuralcomputation,6(2):181–214,1994.
[21] JaredKaplan,SamMcCandlish,TomHenighan,TomBBrown,BenjaminChess,RewonChild,
ScottGray,AlecRadford,JeffreyWu,andDarioAmodei. Scalinglawsforneurallanguage
models. arXivpreprintarXiv:2001.08361,2020.
[22] David J Ketchen and Christopher L Shook. The application of cluster analysis in strategic
managementresearch: ananalysisandcritique. Strategicmanagementjournal,17(6):441–458,
1996.
[23] BrianLester,RamiAl-Rfou,andNoahConstant. Thepowerofscaleforparameter-efficient
prompttuning. InMarie-FrancineMoens,XuanjingHuang,LuciaSpecia,andScottWen-tau
Yih,editors,Proceedingsofthe2021ConferenceonEmpiricalMethodsinNaturalLanguage
Processing,EMNLP2021,VirtualEvent/PuntaCana,DominicanRepublic,7-11November,
2021,pages3045–3059.AssociationforComputationalLinguistics,2021.
[24] XiangLisaLiandPercyLiang. Prefix-tuning: Optimizingcontinuouspromptsforgeneration.
InChengqingZong,FeiXia,WenjieLi,andRobertoNavigli,editors,Proceedingsofthe59th
AnnualMeetingoftheAssociationforComputationalLinguisticsandthe11thInternational
Joint Conference on Natural Language Processing, ACL/IJCNLP 2021, (Volume 1: Long
Papers),VirtualEvent,August1-6,2021,pages4582–4597.AssociationforComputational
Linguistics,2021.
11

<!-- Page 12 -->

[25] YunxiangLi,ZihanLi,KaiZhang,RuilongDan,SteveJiang,andYouZhang. Chatdoctor: A
medicalchatmodelfine-tunedonalargelanguagemodelmeta-ai(llama)usingmedicaldomain
knowledge. Cureus,15(6),2023.
[26] HaokunLiu,DerekTam,MohammedMuqeeth,JayMohta,TenghaoHuang,MohitBansal,and
ColinRaffel. Few-shotparameter-efficientfine-tuningisbetterandcheaperthanin-context
learning. InSanmiKoyejo,S.Mohamed,A.Agarwal,DanielleBelgrave,K.Cho,andA.Oh,
editors,AdvancesinNeuralInformationProcessingSystems35: AnnualConferenceonNeural
InformationProcessingSystems2022,NeurIPS2022,NewOrleans,LA,USA,November28-
December9,2022,2022.
[27] Qidong Liu, Xian Wu, Xiangyu Zhao, Yuanshao Zhu, Derong Xu, Feng Tian, and Yefeng
Zheng. Moelora: Anmoe-basedparameterefficientfine-tuningmethodformulti-taskmedical
applications. CoRR,abs/2310.18339,2023.
[28] XiaoLiu, YananZheng, ZhengxiaoDu, MingDing, YujieQian, ZhilinYang, andJieTang.
GPTunderstands,too. CoRR,abs/2103.10385,2021.
[29] StuartLloyd. Leastsquaresquantizationinpcm. IEEEtransactionsoninformationtheory,
28(2):129–137,1982.
[30] Rabeeh Karimi Mahabadi, James Henderson, and Sebastian Ruder. Compacter: Efficient
low-rankhypercomplexadapterlayers. InMarc’AurelioRanzato,AlinaBeygelzimer,YannN.
Dauphin,PercyLiang,andJenniferWortmanVaughan,editors,AdvancesinNeuralInformation
ProcessingSystems34: AnnualConferenceonNeuralInformationProcessingSystems2021,
NeurIPS2021,December6-14,2021,virtual,pages1022–1035,2021.
[31] OpenAI. ChatGPT,2022.
[32] OpenAI. GPT-4TechnicalReport. CoRR,abs/2303.08774,2023.
[33] David Patterson, Joseph Gonzalez, Quoc Le, Chen Liang, Lluis-Miquel Munguia, Daniel
Rothchild,DavidSo,MaudTexier,andJeffDean. Carbonemissionsandlargeneuralnetwork
training. arXivpreprintarXiv:2104.10350,2021.
[34] Jonas Pfeiffer, Aishwarya Kamath, Andreas Rücklé, Kyunghyun Cho, and Iryna Gurevych.
Adapterfusion: Non-destructivetaskcompositionfortransferlearning. InPaolaMerlo,Jörg
Tiedemann,andReutTsarfaty,editors,Proceedingsofthe16thConferenceoftheEuropean
ChapteroftheAssociationforComputationalLinguistics: MainVolume,EACL2021,Online,
April19-23,2021,pages487–503.AssociationforComputationalLinguistics,2021.
[35] ColinRaffel,NoamShazeer,AdamRoberts,KatherineLee,SharanNarang,MichaelMatena,
YanqiZhou,WeiLi,andPeterJ.Liu. Exploringthelimitsoftransferlearningwithaunified
text-to-texttransformer. J.Mach.Learn.Res.,21:140:1–140:67,2020.
[36] Sylvestre-AlviseRebuffi,HakanBilen,andAndreaVedaldi. Learningmultiplevisualdomains
with residual adapters. In Isabelle Guyon, Ulrike von Luxburg, Samy Bengio, Hanna M.
Wallach,RobFergus,S.V.N.Vishwanathan,andRomanGarnett,editors,AdvancesinNeural
Information Processing Systems 30: Annual Conference on Neural Information Processing
Systems2017,December4-9,2017,LongBeach,CA,USA,pages506–516,2017.
[37] GerardSaltonandChristopherBuckley. Term-weightingapproachesinautomatictextretrieval.
Informationprocessing&management,24(5):513–523,1988.
[38] ErichSchubert,JörgSander,MartinEster,Hans-PeterKriegel,andXiaoweiXu. DBSCAN
revisited,revisited: Whyandhowyoushould(still)useDBSCAN. ACMTrans.DatabaseSyst.,
42(3):19:1–19:21,2017.
[39] NoamShazeer,AzaliaMirhoseini,KrzysztofMaziarz,AndyDavis,QuocV.Le,GeoffreyE.
Hinton,andJeffDean. Outrageouslylargeneuralnetworks: Thesparsely-gatedmixture-ofexpertslayer. In5thInternationalConferenceonLearningRepresentations,ICLR2017,Toulon,
France,April24-26,2017,ConferenceTrackProceedings.OpenReview.net,2017.
12

<!-- Page 13 -->

[40] YingSheng,ShiyiCao,DachengLi,ColemanHooper,NicholasLee,ShuoYang,Christopher
Chou,BanghuaZhu,LianminZheng,KurtKeutzer,JosephE.Gonzalez,andIonStoica. S-lora:
Servingthousandsofconcurrentloraadapters. CoRR,abs/2311.03285,2023.
[41] AsaCooperSticklandandIainMurray. BERTandpals: Projectedattentionlayersforefficient
adaptationinmulti-tasklearning. InKamalikaChaudhuriandRuslanSalakhutdinov,editors,
Proceedingsofthe36thInternationalConferenceonMachineLearning,ICML2019,9-15June
2019,LongBeach,California,USA,volume97ofProceedingsofMachineLearningResearch,
pages5986–5995.PMLR,2019.
[42] Yi-Lin Sung, Jaemin Cho, and Mohit Bansal. VL-ADAPTER: parameter-efficient transfer
learning for vision-and-language tasks. In IEEE/CVF Conference on Computer Vision and
PatternRecognition,CVPR2022,NewOrleans,LA,USA,June18-24,2022,pages5217–5227.

## Ieee,2022.

[43] Yi-LinSung,VarunNair,andColinRaffel.Trainingneuralnetworkswithfixedsparsemasks.In
Marc’AurelioRanzato,AlinaBeygelzimer,YannN.Dauphin,PercyLiang,andJenniferWortmanVaughan,editors,AdvancesinNeuralInformationProcessingSystems34: AnnualConferenceonNeuralInformationProcessingSystems2021,NeurIPS2021,December6-14,2021,
virtual,pages24193–24205,2021.
[44] MiracSuzgun,NathanScales,NathanaelSchärli,SebastianGehrmann,YiTay,HyungWon
Chung,AakankshaChowdhery,QuocV.Le,EdH.Chi,DennyZhou,andJasonWei. Challengingbig-benchtasksandwhetherchain-of-thoughtcansolvethem. InAnnaRogers,JordanL.
Boyd-Graber, and Naoaki Okazaki, editors, Findings of the Association for Computational
Linguistics: ACL2023,Toronto,Canada,July9-14,2023,pages13003–13051.Associationfor
ComputationalLinguistics,2023.
[45] HugoTouvron,ThibautLavril,GautierIzacard,XavierMartinet,Marie-AnneLachaux,TimothéeLacroix,BaptisteRozière,NamanGoyal,EricHambro,FaisalAzhar,AurélienRodriguez,
ArmandJoulin,EdouardGrave,andGuillaumeLample. Llama: Openandefficientfoundation
languagemodels. CoRR,abs/2302.13971,2023.
[46] HugoTouvron,LouisMartin,KevinStone,PeterAlbert,AmjadAlmahairi,YasmineBabaei,
Nikolay Bashlykov, Soumya Batra, Prajjwal Bhargava, Shruti Bhosale, Dan Bikel, Lukas
Blecher,CristianCanton-Ferrer,MoyaChen,GuillemCucurull,DavidEsiobu,JudeFernandes,
JeremyFu,WenyinFu,BrianFuller,CynthiaGao,VedanujGoswami,NamanGoyal,Anthony
Hartshorn, Saghar Hosseini, Rui Hou, Hakan Inan, Marcin Kardas, Viktor Kerkez, Madian
Khabsa,IsabelKloumann,ArtemKorenev,PunitSinghKoura,Marie-AnneLachaux,Thibaut
Lavril,JenyaLee,DianaLiskovich,YinghaiLu,YuningMao,XavierMartinet,TodorMihaylov,
PushkarMishra,IgorMolybog,YixinNie,AndrewPoulton,JeremyReizenstein,RashiRungta,
KalyanSaladi,AlanSchelten,RuanSilva,EricMichaelSmith,RanjanSubramanian,XiaoqingEllenTan,BinhTang,RossTaylor,AdinaWilliams,JianXiangKuan,PuxinXu,Zheng
Yan,IliyanZarov,YuchenZhang,AngelaFan,MelanieKambadur,SharanNarang,Aurélien
Rodriguez,RobertStojnic,SergeyEdunov,andThomasScialom. Llama2: Openfoundation
andfine-tunedchatmodels. CoRR,abs/2307.09288,2023.
[47] LaurensVanderMaatenandGeoffreyHinton. Visualizingdatausingt-sne. Journalofmachine
learningresearch,9(11),2008.
[48] YimingWang,YuLin,XiaodongZeng,andGuannanZhang. Multilora: Democratizinglorafor
bettermulti-tasklearning. CoRR,abs/2311.11501,2023.
[49] JasonWei,MaartenBosma,VincentY.Zhao,KelvinGuu,AdamsWeiYu,BrianLester,Nan
Du,AndrewM.Dai,andQuocV.Le. Finetunedlanguagemodelsarezero-shotlearners. InThe
TenthInternationalConferenceonLearningRepresentations,ICLR2022,VirtualEvent,April
25-29,2022.OpenReview.net,2022.
[50] TedZadouri,AhmetÜstün,ArashAhmadian,BeyzaErmis,AcyrLocatelli,andSaraHooker.
Pushing mixture of experts to the limit: Extremely parameter efficient moe for instruction
tuning. CoRR,abs/2309.05444,2023.
13

<!-- Page 14 -->

[51] EladBenZaken,YoavGoldberg,andShauliRavfogel. Bitfit: Simpleparameter-efficientfinetuningfortransformer-basedmaskedlanguage-models. InSmarandaMuresan,PreslavNakov,
andAlineVillavicencio,editors,Proceedingsofthe60thAnnualMeetingoftheAssociationfor
ComputationalLinguistics(Volume2: ShortPapers),ACL2022,Dublin,Ireland,May22-27,
2022,pages1–9.AssociationforComputationalLinguistics,2022.
[52] QingruZhang,MinshuoChen,AlexanderBukharin,PengchengHe,YuCheng,WeizhuChen,
andTuoZhao. Adaptivebudgetallocationforparameter-efficientfine-tuning. InTheEleventh
InternationalConferenceonLearningRepresentations,ICLR2023,Kigali,Rwanda,May1-5,

#### OpenReview.net,2023.

[53] HanZhou,XingchenWan,IvanVulic,andAnnaKorhonen. Autopeft: Automaticconfiguration
searchforparameter-efficientfine-tuning. CoRR,abs/2301.12132,2023.
14

<!-- Page 15 -->

A DatasetsandBaselines
A.1 Datasets

### SingleDomain


## General: wefine-tunewiththegeneralinstructiontuningdatabricks-dolly-15kforgeneric

languagecapabilityandevaluatewithMMLU.

## Medical: wefine-tunewithGenMedGPTandclinic-10kfromChatDoctorformedicine

applicationsandevaluatemedicaltasksinMMLUincludingthreerelatedtasks: “clinical
knowledge”,“professionalmedicine”and“collegemedicine”.

## Law: wefine-tunewithtwolegalinstructiontuningdatasetsLawyer-InstructandUS-Terms

thenevaluatewithlawtasksinMMLUincludingtworelatedtasks: “professionallaw”and
“internationallaw”.

## Math: we fine-tune with the training split of GSM8K for mathematical reasoning and

evaluatewithtestsetofGSM8K.

## Code: wefine-tunewithCodeAlpacaforcodegenerationandevaluatewithHumanEval.

Multi-task Domain As well for complex mixed multi-task/domain, we select a portion of the
Flanv2datasetscoveringNaturalLanguageUnderstanding(NLU)andNaturalLanguageGeneration
(NLG),whichcanbegroupedinto10distincttaskclusters. ThenweevaluateitwiththeBig-Bench
Hard(BBH)benchmark.

### Wesummarizethedetailsoftheuseddatasetsasfollows:


## Struct-to-TextConversion: Thistaskevaluatesthecapabilitytogeneratenaturallanguage

descriptionsfromstructureddatainputs. Weusethefollowingdatasets: (1)CommonGen;
(2)DART;(3)E2ENLG;(4)WebNLG;

## Translation:Translationinvolvesconvertingtextfromonelanguagetoanother,maintaining

theoriginalmeaningandnuances. Weusethefollowingdatasets: (1)En-FrfromWMT’14;
EnDe,En-Tr,En-Ru,En-Fi,En-RofromWMT’16;(3)En-EsfromParacrawl.

## CommonsenseReasoning:Thisinvolvesassessingtheabilitytoapplyphysicalorscientific

principlesalongsidecommonsenseinreasoningtasks. Weusethefollowingdatasets: (1)
COPA,(2)HellaSwag,(3)PiQA,and(4)StoryCloze.

## SentimentAnalysis: Afundamentaltaskinnaturallanguageprocessing(NLP)thatdeterminesthesentimentpolarity(positiveornegative)ofagiventext. Weusethefollowing

datasets: (1)IMDB,(2)Sentiment140,(3)SST-2,and(4)Yelp. informationsources. We
usethefollowingdatasets: (1)ARC,(2)NQ,and(3)TriviaQA.

## ParaphraseDetection:Thistaskrequiresmodelstoascertainwhethertwosentencesconvey

the same meaning, indicating semantic equivalence. We use the following datasets: (1)
MRPC,(2)QQP,and(3)PawsWiki.

## CoreferenceResolution: Involvesidentifyinginstanceswithinatextthatrefertothesame

entity,demonstratinganunderstandingoftextualcontext. Weusethefollowingdatasets: (1)
DPRand(2)WSC273.

## Readingcomprehension: Assessesthecapabilitytoderiveanswerstoquestionsfroma

providedtextcontainingrelevantinformation. Weusethefollowingdatasets: (1)BoolQ,(2)
DROP,(3)MultiRC,(4)OBQA,(5)SQuADv1,(6)SQuADv2.

## ReadingComprehensionwithCommonsense: Mergestraditionalreadingcomprehension

skillswithcommonsensereasoning,requiringunderstandingbeyondtheexplicittext. We
usethefollowingdatasets: (1)CosmosQA;(2)ReCoRD.

## NaturalLanguageInference:Focusesondeducingtherelationshipbetweentwosentences,

determiningifthesecondsentencelogicallyfollowsfrom,contradicts,orisunrelatedtothe
firstsentence. Weusethefollowingdatasets: (1)ANLI,(2)CB;(3)MNLI;(4)QNLI;(5)

## Snli;(6)Wnli;(7)Rte.


## Closed-BookQuestionAnswering: Thistaskchallengesmodelstoanswerquestionsabout

generalknowledgewithoutdirectaccesstoexternal
15

<!-- Page 16 -->

A.2 Baselines

### PEFTmethods


## FullFine-tuningisthedefaultstrategyforadaptation. Duringfine-tuning,themodelis

initializedwithpretrainedweightsandbiases,andallmodelparametersundergogradient
updates.

## PromptTuningaddstask-specificpromptstotheinput,andthesepromptparametersare

updatedindependentlyofthepretrainedmodelparameterswhicharefrozen.

## P-Tuning adds trainable prompt embeddings to the input that is optimized by a prompt

encoder to find a better prompt, eliminating the need to manually design prompts. The
prompttokenscanbeaddedanywhereintheinputsequence,andP-Tuningalsointroduces
anchortokensforimprovingperformance.

## PrefixTuningprefixesaseriesoftask-specificvectorstotheinputsequencethatcanbe

learnedwhilekeepingthepretrainedmodelfrozen. Theprefixparametersareinsertedinall
ofthemodellayers.

## IA3enhancesefficiencybyinfusinglearnedvectorsintotransformerarchitectures,drasticallycuttingtrainableparameterswhilepreservingperformanceandminimizinginference

latency.

## AdaLoRAisamethodforoptimizingthenumberoftrainableparameterstoassigntoweight

matricesandlayers,unlikeLoRA,whichdistributesparametersevenlyacrossallmodules.
Moreparametersarebudgetedforimportantweightmatricesandlayerswhilelessimportant
onesreceivefewerparameters.

### MultipleLoRAweightedaveragemethods


## LoRAMoE.Acollectionofnparameterizedexperts,denotedasE ,...,E ,isorchestrated

1 n
byarouternetworkR. ThisnetworkfeaturesadenselayerwithadjustableweightsW
g
fromRdm×n. Asoftmaxfunctionthenprocessesanintermediatetokenrepresentationx,
yieldinggatingscoress ,...,s thatdeterminetheweightedcontributionofeachexpert’s
1 n
output:
s =R(x) =softmax(WTx) (Router) (5)
i i g
Subsequently,theoveralloutputyissynthesizedbyaggregatingtheexperts’outputs,each
modulatedbyitsrespectivegatingscore:
n
(cid:88)
y = s E (x) (MoE) (6)
i i
·
i=1
Thisresultsinadynamicallocationofthemodel’scapacity,enablingspecializedprocessing
byexpertsasdirectedbytherouter’sgatingmechanism.

## LoraHubaggregates20LoRAsatrandomfornewdownstreamtasks. Tomastertheweight

ofeachLoRA,itutilizesablack-boxoptimizationtechnique,bypassingtheneedforgradient
calculationsofthelargemodel. Thisprocessinvolvesweightedaveragingattheparameter
level. MirroringtheMoEtrainingapproach,weselect20randomsamplesforeachtask,
creatingacohesivetrainingdatasetoptimizedthroughthisblack-boxmethod.

### B Initializationviak-means

Inthecaseofconsideringheterogeneouscorpora,itiscrucialtoselecttheappropriatenumberN
ofmatrixB,toensureconsistentperformanceandminimizeunnecessarycomputationaloverhead.
Thischoiceisusuallycloselyrelatedtothetrainingcorpus. Inthiswork,weproposeinitializing
HydraLoRAmodulesviak-means[29]algorithmforadaptiveinitialization. Specifically,k-meansis
utilizedtoprocesstheheterogeneouscorpustoidentifythebest-fittaxonomyofthecorpus,i.e.,the
optimalk. First,weextractkeyfeaturesfromthecorpusbyapplyingtheTermFrequency-Inverse
DocumentFrequency(TF-IDF;[37])algorithmandtransformthetextualinformationintonumerical
16

<!-- Page 17 -->

featurevectors. Weintegratetheelbowmethod[22]todeterminetheoptimalvalueofK. Initially,
K clustercentersarerandomlyselectedforpreliminaryclusteringasEq.7,followedbyupdating
theclustercenterstoaccuratelyreflectthedatawithineachclusterasEq.8. whereC isthecluster
j
centertowhichdatapointX isassignedandd(, )istheEuclideandistancefunction. S istheset
i j
· ·
ofdatapointsinthej-thcluster.
C =argmind(X ,C ) (7)
j i j

### Cj

1 (cid:88)

## C = X (8)

j S i
j
| |Xi∈Sj
Byanalyzingtherelationshipbetweenthesumofsquaresoferrors(SSE)anddifferentK values,we
observethatSSEdecreasesasK increases. IdentifyingtheelbowpointontheSSEcurve—where
therateofdecreaseinSSEslowsdown—iscrucial. TheelbowpointrepresentstheoptimalK value,
beyondwhichincreasingthenumberofclustersdoesnotsignificantlyenhanceperformance,thereby
achievinganidealbalancebetweenmodelcomplexityandperformance.

### C LoRABreakdown

t-SNE Visualization of BA-Matrix Diff. LoRAs t-SNE Visualization of A-Matrix Diff. LoRAs t-SNE Visualization of B-Matrix Diff. LoRAs
− 2 2 4 0 0 0 0 7 1 1 2 0 1 4 6 5 3 1 5 8 9 2 2 4 1 2 4 4 2 4 4 2 6 8 4 4 0 7 1 8 6 8 6 1 4 1 7 0 2 1 1 5 1 1 8 6 8 2 7 1 1 8 8 4 0 1 1 1 69 1 1 6 5 2 1 1 7 8 0 1 5 0 1 75 9 7 5 3 4 4 9 1 77 0 7 1 2 1 5 5 5 9 4 3 5 9 63 0 0 1 3 5 4 1 1 2 35 9 4 1 6 7 1 1 1 2 1 1 9 297 9 7 1 1 3 2 0 2 5 2 0 73 9 0 1 1 4 2 7 2 54 1 9 9 13 1 5 9 4 3 4 7 1 0 7 1 2 2 5 1 37 1 3 0 3 8 3 73 3 8 0 3 9 3 3 6 2 7 5 1 8 9 1 3 6 5 0 3 1 1 7 5 0 9 9 6 4 2 1 2 1 0 2 8 1 3 9 6 0 6 1 9 5 7 9 8 2 0 8 8 5 5 6 8 0 3 L L L G 8 8 6 6 9 8 8 6 1 o o o 1 S 6 2 R R R 2 M 2 2 6 1 7 1 6 2 A A A 2 1 8 1 1 4 K 4 1 2 30 6 4 0 6 8 − 2 2 4 0 0 0 0 7 1 1 2 0 1 4 6 5 3 1 5 8 9 2 2 4 1 2 4 4 2 4 4 2 6 8 4 4 0 7 1 8 6 6 1 4 1 0 2 1 1 5 1 8 6 8 2 7 8 4 1 1 1 3 4 0 2 9 4 0 0 4 1 1 2 9 2 0 0 1 2 1 4 7 2 2 0 3 8 0 6 2 1 3 0 0 6 4 2 0 2 8 6 0 6 1 9 7 8 2 0 8 8 5 5 6 8 0 3 L L L G 8 8 6 6 9 8 8 6 1 o o o S 6 2 R R R M 2 2 6 1 6 2 A A A 1 8 1 4 4 K 2 1 30 6 4 0 6 8 − 1 1 2 3 0 0 0 0 0 87 11 1 1 8 0 9 1 1 6 5 1 1 2 6 1 7 0 0 8 5 5 9 5 7 7 1 1 9 7 4 7 7 5 1 5 3 5 9 5 1 6 3 5 3 1 3 5 1 2 1 9 4 1 6 7 1 9 7 9 7 1 1 3 2 7 1 20 1 5 2 3 9 4 792 5 9 3 5 4 1 1 3 9 4 1 0 1 7 7 5 1 3 3 3 1 3 7 3 9 3 3 8 3 7 5 8 9 1 6 3 5 1 5 1 7 9 9 2 1 1 3 1 9 5 9 L L L G o o o S R R R M A A A 8 K 2 1 3 121
40 20 0 20 40 40 20 0 20 40 20 10 0 10 20 30
− − − − − −
(a) Comparefine-tunedLoRAmodulesofGSM8K[7]withitssubsetsusingT-SNE.WeemploytheIndependent
andIdenticallyDistributed(IID)segmentationschemetodivideGSM8Kintothreesubsetsandfine-tunethem
usingdifferentLoRAs.
t-SNE Visualization of BA-Matrix Diff. LoRAs t-SNE Visualization of A-Matrix Diff. LoRAs t-SNE Visualization of B-Matrix Diff. LoRAs
− 2 2 4 0 0 0 0 7 1 1 2 0 1 4 6 5 3 1 5 8 9 2 2 4 1 2 4 4 2 4 4 2 6 8 4 4 0 7 1 8 6 8 6 1 4 1 7 0 2 1 1 5 1 1 8 6 8 2 7 1 1 8 8 4 0 1 1 1 69 1 1 6 5 2 1 1 7 8 0 1 5 0 1 75 9 7 5 3 4 4 9 1 77 0 7 1 2 1 5 5 5 9 4 3 5 9 63 0 0 1 3 5 4 1 1 2 35 9 4 1 6 7 1 1 1 2 1 1 9 297 9 7 1 1 3 2 0 2 5 2 0 73 9 0 1 1 4 2 7 2 54 1 9 9 13 1 5 9 4 3 4 7 1 0 7 1 2 2 5 1 37 1 3 0 3 8 3 73 3 8 0 3 9 3 3 6 2 7 5 1 8 9 1 3 6 5 0 3 1 1 7 5 0 9 9 6 4 2 1 2 1 0 2 8 1 3 9 6 0 6 1 9 5 7 9 8 2 0 8 8 5 5 6 8 0 3 L L L G 8 8 6 6 9 8 8 6 1 o o o 1 S 6 2 R R R 2 M 2 2 6 1 7 1 6 2 A A A 2 1 8 1 1 4 K 4 1 2 30 6 4 0 6 8 − 2 2 4 0 0 0 0 7 1 1 2 0 1 4 6 5 3 1 5 8 9 2 2 4 1 2 4 4 2 4 4 2 6 8 4 4 0 7 1 8 6 6 1 4 1 0 2 1 1 5 1 8 6 8 2 7 8 4 1 1 1 3 4 0 2 9 4 0 0 4 1 1 2 9 2 0 0 1 2 1 4 7 2 2 0 3 8 0 6 2 1 3 0 0 6 4 2 0 2 8 6 0 6 1 9 7 8 2 0 8 8 5 5 6 8 0 3 L L L G 8 8 6 6 9 8 8 6 1 o o o S 6 2 R R R M 2 2 6 1 6 2 A A A 1 8 1 4 4 K 2 1 30 6 4 0 6 8 − 1 1 2 3 0 0 0 0 0 87 11 1 1 8 0 9 1 1 6 5 1 1 2 6 1 7 0 0 8 5 5 9 5 7 7 1 1 9 7 4 7 7 5 1 5 3 5 9 5 1 6 3 5 3 1 3 5 1 2 1 9 4 1 6 7 1 9 7 9 7 1 1 3 2 7 1 20 1 5 2 3 9 4 792 5 9 3 5 4 1 1 3 9 4 1 0 1 7 7 5 1 3 3 3 1 3 7 3 9 3 3 8 3 7 5 8 9 1 6 3 5 1 5 1 7 9 9 2 1 1 3 1 9 5 9 L L L G o o o S R R R M A A A 8 K 2 1 3 121
40 20 0 20 40 40 20 0 20 40 20 10 0 10 20 30
− − − − − −
(b) Specifictasks.
Figure 9: Breakdown analysis of LoRA modules. Compare fine-tuned LoRA modules of GSM-
8K[7]withitssubsetsusingT-SNE.WeemploytheIndependentandIdenticallyDistributed(IID)
segmentationschemetodivideGSM8Kintothreesubsetsandfine-tunethemusingdifferentLoRAs.
ConsiderLLaMA2-7B(randomseed=42),whichcontains32decoderlayers,correspondingto32
adaptivemodules. Eachmoduleconsistsof{0: q_proj_A,1: q_proj_B,2: v_proj_A,3: v_proj_B}
submodules. Thismakesatotalof32 4submodules. (a,b)leftdisplaysallsubmodules. (a,b)center
×
showsallevensubmodules, i.e. theA-matrix. (a,b)rightrepresentsalloddsubmodules, i.e. the
B-matrix. Itcanbeseenthatthedifferencesinthefine-tunedLoRAmodulesfordifferenttasksarise
mainlyfromtheBmatrix.

### D MoreResults

Tabel 4showsComparativeperformanceofdifferenttuningschemes,includingbasemodel(Base),
LoRAtuning(LoRA),LoraHublearning,multi-LoRAtuningwithMoEinference(LoRAMoE)and
17

<!-- Page 18 -->

t-SNE Visualization of Matrix Diff. LoRAs
100
44

## Sum


## Qa


## 50 91 8733 91Ie

43

## 33 All

87 43 118
0 43
91 87 87 91
33 33
50 110 43
−
38
100
− 100 50 0 50 100
− −
Figure 10: Breakdown analysis of LoRA modules (Dolly-15K) with its subsets using T-SNE on
differentlayer.
Table4: Comparativeperformanceofdifferenttuningschemes,includingbasemodel(Base),LoRA
tuning(LoRA),LoraHublearning,multi-LoRAtuningwithMoEinference(LoRAMoE)andour
proposedHydraLoRAlearningacrossmix-taskdomainontheBBHbenchmarkwithLLaMA2-7Bas
thebaseLLM(3-shot).

### Task Base LoRA LoraHub LoRAMoE HydraLoRA

BooleanExpressions 61.9 67.1 72.9 68.0 73.7

### CausalJudgement 52.2 54.9 50.1 51.4 53.2

DateUnderstanding 30.4 35.2 36.0 33.9 36.0
Disambiguation 34.8 45.2 49.1 47.2 50.3

### DyckLanguages 15.8 18.7 14.5 16.8 19.8

FormalFallacies 49.0 62.2 64.5 67.6 65.3
GeometricShapes 9.7 17.7 18.7 17.7 19.7

### Hyperbaton 51.8 74.3 74.3 68.9 77.2


### LogicalDeduction(fiveobjects) 21.9 33.3 38.7 40.0 42.2

LogicalDeduction(sevenobjects) 15.0 36.4 37.3 40.7 40.7
LogicalDeduction(threeobjects) 32.8 41.4 38.5 43.7 42.9
MovieRecommendation 34.4 53.5 56.0 56.8 58.3
MultistepArithmetic 1.2 1.2 1.9 1.9 1.8

### Navigate 53.8 52.7 56.2 58.0 57.1


### ObjectCounting 40.1 40.5 42.3 44.7 42.3


### PenguinsinaTable 21.7 23.2 25.0 23.2 25.9

ReasoningaboutColoredObjects 19.4 28.0 32.7 38.3 38.3

### RuinNames 24.3 28.7 34.3 34.3 36.7

SalientTranslationErrorDetection 11.3 11.1 17.1 16.2 20.1

### Snarks 44.0 47.9 54.9 53.6 56.9

SportsUnderstanding 57.5 59.0 61.2 59.0 60.2

### TemporalSequences 21.1 32.6 28.9 34.1 30.4

TrackingShuffledObjects(fiveobjects) 21.9 23.7 23.7 28.0 29.3
TrackingShuffledObjects(sevenobjects) 14.6 15.3 16.6 15.3 15.3
TrackingShuffledObjects(threeobjects) 32.4 38.4 39.0 38.4 40.7

### WebofLies 51.4 52.8 53.2 50.1 52.0


### WordSorting 29.6 33.6 33.6 31.2 34.0


### AvgPerformance 31.6 36.8 39.7 40.3 41.5

# ofA/Bfortraining 0/0 1/1 48/48 48/48 1/10
# ofA/Bforinference 0/0 1/1 20/20 48/48 1/10
%Params - 0.062 1.240 2.976 0.341
ourproposedHydraLoRAlearningacrossmix-taskdomainontheBBHbenchmarkwithLLaMA2-7B
asthebaseLLM(3-shot).
18

<!-- Page 19 -->


### E Limitation

HydraLoRAiscomputationallydemanding,primarilyduetothenecessityoffine-tuninglarge-scale
languagemodels. ItincursahighertrainingexpenditurethanconventionalPEFTmethods,attributed
totheemploymentofmultipleadaptercopies. EmpiricaldatasuggestthatHydraLoRArequires1
to2timesmoretrainingiterationscomparedtotypicalPEFTmethods,whichadverselyaffectsthe
environmental footprint of model training. The HydraLoRA framework, distinct from prevailing
PEFTapproaches,holdspromiseforenhancingtheefficacyofexistingPEFTstrategies.Inourcurrent
study,weexamineestablishedPEFTtechniques—LoRA.However,wehavenottestedadditional
configurationssuchasprompt-tuningandadapter,deferringtheseexplorationstosubsequentresearch.
Additionally, our assessment is exclusively within the context of fine-tuning. Exploration of its
efficacyduringthepre-trainingphaseremainsanavenueforfutureresearch.

### F BroaderImpacts

PositiveSocietalImpacts TheproposedHydraLoRAframework,withitsasymmetricstructure
andparameter-efficientfine-tuningapproach,hasthepotentialtomakeLLMsmoreaccessibleand
efficient. ThiscoulddemocratizeAI,enablingmoreresearchers,developers,andorganizationsto
leveragethepowerofLLMsforvariousapplications,ultimatelydrivinginnovationandprogress.
Moreover,byeffectivelyaddressingthechallengeofdomainortaskinterference,HydraLoRAcould
significantlyenhancetheperformanceofLLMsincomplex,multi-taskdomains. Thiscouldleadto
moreaccurateandreliableAI-poweredtoolsandservicesinareaslikehealthcare,education,and
finance, ultimatelyimprovingthequalityoflifeformanypeople. Lastly, theparameter-efficient
approachofHydraLoRAcouldhelpreducethecomputationalresourcesrequiredfortrainingand
fine-tuningLLMs,therebylesseningtheenvironmentalimpactofAI.
NegativeSocietalImpacts AswithanyAItechnology,therearepotentialnegativesocietalimpacts
toconsider. Theriskofmisuseisasignificantconcern,asHydraLoRAcouldbeusedformalicious
purposes,suchascreatingmoresophisticatedandconvincingdeepfakesorspreadingmisinformation
and propaganda. Additionally, the increased efficiency and accessibility of AI brought about by
HydraLoRA could lead to job displacement in certain sectors, as AI-powered tools and services
becomecapableofperformingtaskstraditionallydonebyhumans. Lastly,theuseofLLMsinvarious
applicationscouldpotentiallyleadtoprivacyandsecurityissues,especiallyifthesemodelsareused
toprocessorgeneratesensitiveinformation. TheproposedHydraLoRAframework,whilenotdirectly
relatedtotheseissues,couldinadvertentlycontributetothembymakingiteasiertodeployLLMsin
variousapplications.
19

## Tables

**Table (Page 3):**

| Schemes | r n | MMLU | %Pa | rameter |
|---|---|---|---|---|
|  | × 8 1 16× 1 32×1 × | ↑ 43.22 45.45 46.59 | 0 0 0 |  |
|  | 16 2 8 ×4 4×8 × | 46.82 46.94 46.83 | 0 0 0 |  |


**Table (Page 5):**

| Attention |
|---|
| LN |
|  |
| FNN |
| LN Pretrained Weights |


**Table (Page 6):**

| Schemes | MMLU | Medical | Law | HumanEval |  | GSM8K | %Param | #A | #B¯ |
|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  | P@1 | P@10 |  |  |  |  |


**Table (Page 6):**

| 39.91 37.59 35.02 13.66 21.55 13.18 41.11 39.81 36.72 13.60 21.13 15.56 41.78 40.28 36.54 13.23 22.56 16.89 40.45 37.12 35.25 13.54 23.17 13.98 44.32 42.83 39.36 14.81 23.78 19.51 | 0.001 0.193 0.077 0.009 0.093 |
|---|---|
| 43.22 41.59 37.85 15.67 22.95 18.24 45.45 43.10 39.64 16.71 25.60 20.32 46.59 44.32 40.81 17.12 25.89 20.67 46.94 45.28 41.35 18.20 26.85 21.92 | 0.062 0.124 0.248 0.248 |
| 47.22 45.71 42.18 18.31 27.43 22.27 | 0.124 |


**Table (Page 8):**

|     )hWK(  / R 5 $  U          / R 5 $  U           / R 5 $  U          ygrenE  / R 5 $  6 S O L W   [        + \ G U D / R 5 $          & 3 8  * 3 8  5 $ 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  / |  R 5 $  U     |   )h(   ycnetaL          5     5      5      6 S O L W + \ G U D / R 5 $ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  / |  R 5 $  U      |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  /  / |  R 5 $  U       R 5 $  6 S O L W   [   |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  + |  \ G U D / R 5 $ |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |


**Table (Page 8):**

|  |  |  |  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |


**Table (Page 8):**

| 50.0 47.5 )%( 46.9447.22 w/o MoE 45.2845.71 w/o Gate 45.0 ecnamrofreP w/o Hydra 43.2242.81 HydraLoRA 42.18 42.5 41.59 40.92 41.35 40.0 37.85 37.5 37.12 35.0  0 P O X  0 H G L F D O  / D Z |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  0 |  P O X |  | 41.59 40.92  0 H |  |  |  G L F D O |  | 37.85 37.12  / D |  |  | 41.35  Z |  |
|  | erf eC La and lat con ith db rat th per ou | orm arb MA red enc sid ash ute esth e M int rab | anc on[ 2-7 uce yof ers are xpa ep oE oun lati | eo 33] B s4 Lo inh dA nds ara ar der ons |  | ons 5s we ner ite ow an for fec ure gth Fig | tud ho can gy xce led dd ma tive an ec ure | yfo wst see cost eds gem iffe nce nes d t ontr 6. | rH he th co the od ren enh so he ibu Th |  | RA fv aLo to (ra and rix. nto Lo nct ea tw | acr ario RA Lo nk= col In fm RA. ion chc /oM | oss usfi eff RA 32). labo this ore hav om oE | mu ne ecti (ra Th rat wa tha e o pon (es |


**Table (Page 9):**

|  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |
|  6 W |  |  D W L F |  |  |  |  |  |  |
|  |  6 W |  D W L F |  |  |  |  |  |  |
|  |  . |   P H D Q V |  |  |  |  |  |  |
|  ' |  ' |  % 6 & $ 1 |  |  |  |  |  |  |


**Table (Page 9):**

|      )%(           ecnamrofreP                           N            |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  N    |  |  |   |  |  |   |  |  |   |  |  |   |  |  |
|  |  | : ra i l u ra t on ad ra T t; p ho w a g u e ap d ’s uc if pt ti p R li m in o n yi s de A a c or ff |  |  | re rs dy w re o b h r ma an ). pt a a pd e li pl ac i m ea nt wh un ai 7] in rk R m es h y e fe tr o e g |  |  | of be ic l, c u n ro p es ac x te vi rs ( ce d g t en de le le ca L LL or m ef m kn a R il ef es c s, al ab |  |  | eri cl mp fi p a y s es ]. e n f d alt A; , b mp b in M de li m in A k te ca nt ti ed r c li o as o an ng at |  |  | ts s. io n e at it ss vo ot o ] gn fo g ]) m io ts v wh T ct re ct [ le M m rv ba ur ie ue ti m e T b rn y |  |  |


**Table (Page 18):**

|  | 91 | 4 87 | SU QA 91IE | M |
|---|---|---|---|---|
|  | 43 33 87 43 | 33 | AL | L |
|  |  |  | 43 | 118 |
|  | 91 87 33 | 87 33 | 91 |  |
| 110 | 3 | 43 8 |  |  |


**Table (Page 18):**

| Base LoRA LoraHub LoRAMoE | HydraLoRA |
|---|---|
| 61.9 67.1 72.9 68.0 52.2 54.9 50.1 51.4 30.4 35.2 36.0 33.9 34.8 45.2 49.1 47.2 15.8 18.7 14.5 16.8 49.0 62.2 64.5 67.6 9.7 17.7 18.7 17.7 51.8 74.3 74.3 68.9 21.9 33.3 38.7 40.0 15.0 36.4 37.3 40.7 32.8 41.4 38.5 43.7 34.4 53.5 56.0 56.8 1.2 1.2 1.9 1.9 53.8 52.7 56.2 58.0 40.1 40.5 42.3 44.7 21.7 23.2 25.0 23.2 19.4 28.0 32.7 38.3 24.3 28.7 34.3 34.3 11.3 11.1 17.1 16.2 44.0 47.9 54.9 53.6 57.5 59.0 61.2 59.0 21.1 32.6 28.9 34.1 21.9 23.7 23.7 28.0 14.6 15.3 16.6 15.3 32.4 38.4 39.0 38.4 51.4 52.8 53.2 50.1 29.6 33.6 33.6 31.2 | 73.7 |
|  | 53.2 |
|  | 36.0 |
|  | 50.3 |
|  | 19.8 |
|  | 65.3 |
|  | 19.7 |
|  | 77.2 |
|  | 42.2 |
|  | 40.7 |
|  | 42.9 |
|  | 58.3 |
|  | 1.8 |
|  | 57.1 |
|  | 42.3 |
|  | 25.9 |
|  | 38.3 |
|  | 36.7 |
|  | 20.1 |
|  | 56.9 |
|  | 60.2 |
|  | 30.4 |
|  | 29.3 |
|  | 15.3 |
|  | 40.7 |
|  | 52.0 |
|  | 34.0 |
| 31.6 36.8 39.7 40.3 0/0 1/1 48/48 48/48 0/0 1/1 20/20 48/48 - 0.062 1.240 2.976 | 41.5 |
|  | 1/10 |
|  | 1/10 |
|  | 0.341 |
