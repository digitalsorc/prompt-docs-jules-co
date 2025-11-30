---
title: "SVFT Singular Vectors Fine Tuning"
original_file: "./SVFT_Singular_Vectors_Fine_Tuning.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["llm", "rag", "fine-tuning", "evaluation", "multimodal"]
keywords: ["svftp", "lora", "svftb", "page", "tuning", "dora", "svft", "rank", "params", "table"]
summary: "<!-- Page 1 -->

SVFT: Parameter-Efficient Fine-Tuning
with Singular Vectors

### VijayLingam†∗ AtulaTejaswi†∗ AdityaVavre†∗ AneeshShetty†∗

GauthamKrishnaGudur†∗ JoydeepGhosh† AlexDimakis† EunsolChoi†

### AleksandarBojchevski‡ SujaySanghavi†

†UniversityofTexasatAustin ‡UniversityofCologne

### Abstract

Popularparameter-efficientfine-tuning(PEFT)methods, suchasLoRAandits
variants,freezepre-trainedmodelweightsWandinjectlearnablematrices∆W. These ∆W matrices are structured for efficient paramet"
related_documents: []
---

# SVFT Singular Vectors Fine Tuning

<!-- Page 1 -->

SVFT: Parameter-Efficient Fine-Tuning
with Singular Vectors

### VijayLingam†∗ AtulaTejaswi†∗ AdityaVavre†∗ AneeshShetty†∗

GauthamKrishnaGudur†∗ JoydeepGhosh† AlexDimakis† EunsolChoi†

### AleksandarBojchevski‡ SujaySanghavi†

†UniversityofTexasatAustin ‡UniversityofCologne

### Abstract

Popularparameter-efficientfine-tuning(PEFT)methods, suchasLoRAandits
variants,freezepre-trainedmodelweightsWandinjectlearnablematrices∆W.
These ∆W matrices are structured for efficient parameterization, often using
techniques like low-rank approximations or scaling vectors. However, these
methodstypicallyshowaperformancegapcomparedtofullfine-tuning. Although
recentPEFTmethodshavenarrowedthisgap,theydosoatthecostofadditional
learnableparameters. WeproposeSVFT,asimpleapproachthatfundamentally
differs from existing methods: the structure imposed on ∆W depends on the
specificweightmatrixW. Specifically,SVFTupdatesWasasparsecombination
of outer products of its singular vectors, training only the coefficients (scales)
of these sparse combinations. This approach allows fine-grained control over
expressivity through the number of coefficients. Extensive experiments on
language and vision benchmarks show that SVFT2 recovers up to 96% of full
fine-tuning performance while training only 0.006 to 0.25% of parameters,
outperformingexistingmethodsthatonlyrecoverupto85%performanceusing
0.03to0.8%ofthetrainableparameterbudget.
1 Introduction
Large-scalefoundationmodelsareoftenadaptedforspecificdownstreamtasksafterpre-training.
Parameter-efficientfine-tuning(PEFT)facilitatesthisadaptationefficientlybylearningaminimalset
ofnewparameters,thuscreatingan"expert"model. Forinstance,LargeLanguageModels(LLMs)
pre-trainedonvasttrainingcorporaarefine-tunedforspecializedtaskssuchastextsummarization[12,
34], sentiment analysis [25, 20], and code completion [26] using instruction fine-tuning datasets.
Although full fine-tuning (Full-FT) is a viable method to achieve this, it requires re-training and
storingallmodelweights,makingitimpracticalfordeploymentwithlargefoundationmodels.
Toaddressthesechallenges,PEFTtechniques[13](e.g.,LoRA[14])wereintroducedtosignificantly
reducethenumberoflearnableparameterscomparedtoFull-FT,thoughoftenatthecostofperformance. DoRA[18]bridgesthisperformancegapbyaddingmorelearnableparametersandbeing
moreexpressivethanLoRA.Almostallthesemethodsapplyalow-rankupdateadditivelytothe
frozenpre-trainedweights,potentiallylimitingtheirexpressivity. Furthermore,theseadaptersare
agnostictothestructureandgeometryoftheweightmatricestheymodify. Finally,moreexpressive
PEFTmethods(e.g.,LoRA,DoRA,BOFT[19])stillaccumulateaconsiderableportionoflearnable
parametersevenintheirmostefficientconfiguration(e.g.,settingrank=1inLoRAandDoRA).The
∗indicatesequalcontribution.
2codeisavailableathttps://github.com/VijayLingam95/SVFT/
Preprint.Underreview.
4202
yaM
03
]GL.sc[
1v79591.5042:viXra

<!-- Page 2 -->

55.0 70.0
5
5
0
2
.
.
0
5 Full Fine-Tuning (2500M params) SVFTRd=16
6
6
5
7
.
.
0
5 Full Fine-Tuning (2500M param

## S

s

## V

)

### FTBd=8

SVFTBd=16
DoRAr=16
47.5
SVFTBd=16 SVFTBd=4
4
4
2
5
.
.
5
0

## Svf


## S


## T


## V

Bd

## F

=

## T

2
Bd=4

## Sv


## D


## F

o

## T


## R

Bd

## A

=
r=
8
4
DoRAr=16
6
6
0
2
.
.
0
5
SVFTBd=2 DoRAr=4 LoRAr=32
40.0

## Svftp

VeRAr=2048 LoRAr=4 LoRAr=32 57.5 LoRAr=1 DoRAr=1
37.5 BOFTbm ==82 55.0 SVFTP
35.0
VeRAr=1024
DoRAr=1
52.5

### VeRAr=2048

32.5 LoRAr=1 50.0

### BOFTbm ==82

0.3 0.5 0.85 1.5 2.5 4 7 12 20.5 35 0.3 0.5 0.85 1.5 2.5 4 7 12 20.5 35
Number of Trainable Params (M) Number of Trainable Params (M)
)%(
ycaruccA
Figure1: PerformancevstotaltrainableparametersforGSM-8K(left)andCommonsenseReasoning
(right)onGemma-2B.SVFTB/R outperformsDoRA with75%lesstrainableparameters.
d=16 r=8/16
storage requirements for the learnable adapters can grow very quickly when adapting to a large
numberofdownstreamtasks[16].
IsitpossibletonarrowtheperformancegapbetweenSVFTandFull-FTwhilebeinghighlyparameterefficient?WeproposeSVFT:SingularVectorsguidedFine-Tuning—asimpleapproachthatinvolves
updatinganexistingweightmatrixbyaddingtoitasparseweightedcombinationofitsownsingular
vectors. ThestructureoftheinducedperturbationinSVFTdependsonthespecificmatrixbeingperturbed,settingitapartfromallpreviousapproaches. Ourcontributionscanbesummarizedasfollows:
• WeintroduceSVFT,anewPEFTmethod. GivenaweightmatrixW,SVFTinvolvesadapting
it with a matrix ∆W := (cid:80) m u vT where the {u } and {v } are the left and right
(i,j)∈Ω ij i j i j
singularvectorsofW,Ωisana-priorifixedsparsitypattern,andm for(i,j)∈Ωarelearnable
ij
parameters. Bycontrolling|Ω|wecanefficientlyexploretheaccuracyvsparameterstrade-off.
• SVFTachieveshigherdownstreamaccuracy,asafunctionofthenumberoftrainableparameters,
as compared to several popular PEFT methods (see Figure 1) and over several downstream
tasksacrossbothvisionandlanguagetasks. Ourmethodrecoversupto96%offullfine-tuning
performancewhiletrainingonly0.006to0.25%ofparameters,outperformingexistingmethods
thatonlyrecoverupto85%performanceusing0.03to0.8%thetrainableparameterbudget.
Weintroducefourvariantsforparameterizingweightupdates,namely: Plain,Random,Banded,and
Top-kinSVFT(whichdifferintheirchoicesofthefixedsparsitypatternΩ)andvalidatethesedesign
choicesempirically. Additionally,wetheoreticallyshowthatforanyfixedparametersbudget,SVFT
caninduceahigherrankperturbationcomparedtopreviousPEFTtechniques.
2 RelatedWork
Recentadvancementsinlargelanguagemodels(LLMs)haveemphasizedthedevelopmentofPEFT
techniquestoenhancetheadaptabilityandefficiencyoflargepre-trainedlanguagemodels.
LoRA.AnotablecontributioninthisfieldisLow-RankAdaptation(LoRA)[14],whichfreezesthe
weightsofpre-trainedmodelsandintegratestrainablelow-rankmatricesintoeachtransformerlayer.
Forapre-trainedweightmatrixW ∈Rd×n,LoRAconstraintstheweightupdate∆W toalow-rank
0
decomposition: h = W x+∆Wx = W x+BAx, where B ∈ Rd×r, A ∈ Rr×n and rank
0 0
r ≪min(d,n). Weunderlinethe(trainable)parametersthatareupdatedviagradientdescent.
LoRA variants. We highlight some recent approaches that further improve the vanilla LoRA
architecture. Vector-based Random Matrix Adaptation (VeRA) [16] minimizes the number of
trainable parameters by utilizing a pair of low-rank random matrices shared between layers and
learningcompactscalingvectorswhilemaintainingperformancecomparabletoLoRA.Formally,
2

<!-- Page 3 -->

Figure2: SchematiccomparisonofLoRA,VeRA,DoRA,andSVFT(lefttoright).
VeRAcanbeexpressedas:h=W x+∆Wx=W x+Λ BΛ Ax,whereAandBareinitialized
0 0 b d
randomly,frozen,andsharedacrosslayers,whileΛ andΛ aretrainablediagonalmatrices.
b d
Analternativeapproach,Weight-DecomposedLow-RankAdaptation(DoRA)[18],decomposespretrainedweightmatricesintomagnitudeanddirectioncomponents,andapplieslow-rankupdatesfor
directionalupdates,reducingtrainableparametersandenhancinglearningcapacityandtrainingstability. DoRAcanbeexpressedas: h=m ∥W W 0 0 + + ∆ ∆ W W ∥c x=m ∥W W 0 0 + + B B A A ∥c x,where∥·∥ c denotesthe
vector-wisenormofamatrixacrosseachcolumn. SimilartoLoRA,W remainsfrozen,whereasthe
0
magnitudevectorm(initializedto∥W ∥ )andlow-rankmatricesA,Bcontaintrainableparameters.
0 c
AdaLoRA[35]adaptivelydistributestheparameterbudgetacrossweightmatricesbasedontheir
importance scores and modulates the rank of incremental matrices to manage this allocation
effectively.PiSSA(PrincipalSingularValuesandSingularVectorsAdaptation)[21]isanothervariant
ofLoRA,wherematricesA,BareinitializedwithprincipalcomponentsofSVDandtheremaining
componentsareusedtoinitializeW . FLoRA[31]enhancesLoRAbyenablingeachexampleina
0
mini-batchtoutilizedistinctlow-rankweights,preservingexpressivepowerandfacilitatingefficient
batching,therebyextendingthedomainadaptationbenefitsofLoRAwithoutbatchinglimitations.
OtherPEFTvariants. OrthogonalFine-tuning(OFT)[24]modifiespre-trainedweightmatrices
throughorthogonalreparameterizationtopreserveessentialinformation. However,itstillrequires
a considerable number of trainable parameters due to the high dimensionality of these matrices.
ButterflyOrthogonalFine-tuning(BOFT)[19]extendsOFT’smethodologybyincorporatingButterfly
factorizationtherebypositioningOFTasaspecialcaseofBOFT.Unliketheadditivelow-rankweight
updates utilized in LoRA, BOFT applies multiplicative orthogonal weight updates, marking a
significantdivergenceintheapproachbutclaimstoimproveparameterefficiencyandfine-tuning
flexibility. BOFTcanbeformallyexpressedas: h=(R(m,b)·W )x,wheretheorthogonalmatrix
0
R(m,b) ∈ Rd×d is composed of a product of multiple orthogonal butterfly components. When
m = 1,BOFTreducestoblock-diagonalOFTwithblocksizeb. Whenm = 1andb = d,BOFT
reducestotheoriginalOFTwithanunconstrainedfullorthogonalmatrix.
3 Method
Inthissection,weintroduceSingularVectorsguidedFine-Tuning(SVFT).Themaininnovationin
SVFTliesinapplyingstructure/geometry-awareweightupdates.
3.1 SVFTFormulation
Wenowformallydescribeourmethod, SVFTforparameter-efficientfine-tuningofapre-trained
model. Let W
0
∈ Rd1×d2 denote a weight matrix in the pre-trained model. For instance, in a
transformerblock,thiscouldbethekeymatrix,thequerymatrix,amatrixintheMLP,etc. Weadda
structured,learned∆W tothismatrixasfollows.
Asafirststep,wecomputetheSingularValueDecomposition(SVD)ofthegivenmatrix: W =
0
UΣVT. Thatis,U isthed ×d matrixofleftsingularvectors(i.e.,itscolumnsareorthonormal),
1 1
VT isthed ×d matrixofrightsingularvectors(i.e.,itsrowsareorthonormal),andΣisad ×d
2 2 1 2
diagonalmatrix. Then,weparameterizeourweightupdateas∆W = UMVT,whereU,V are
3

<!-- Page 4 -->

Figure3: AnOverviewofSVFT.TheoriginalweightsW aredecomposedintoU,Σ,V. Here,M
containsallthetrainableparameters,whichcanbeconfiguredintopatternssuchasPlain,Random,
Banded,andTop-k,representedbypatternsoftrainable(orange)andzero(gray)elements.
fixedandfrozen,whileM isad ×d sparsetrainablematrixwithpre-determinedandfixed
1 2
sparsitypattern3. Thatis,wefirstpre-determineasmallfixedsetofelementsinM thatwillbe
allowedtobenon-zeroandtrainonlythoseelements. TheforwardpassforSVFTcanbewrittenas,
h=W x+∆Wx=U(Σ+M)VTx (1)
0
WeexplorefourchoicesforΩ,thea-priorifixedsparsitypatternofM.

### Plain

(cid:0) SVFTP(cid:1)
. Inthisvariant,weconstrainM tobeadiagonalmatrix,whichcanbeinterpreted
asadaptingsingularvaluesandreweightingthefrozensingularvectors. Sinceonlythediagonal
elementsarelearned,thisisthemostparameter-efficientSVFTvariant.

### Banded

(cid:0) SVFTB(cid:1)
. Inthisapproach,wepopulateM usingabandedmatrix,progressivelymaking
d
off-diagonalslearnable. Specifically,forconstantsz andz ,M =0ifj <i−z orj >i+z ,
1 2 ij 1 2
where z ,z ≥ 0. In our experiments, we set z = z = d to induce off-diagonal elements that
1 2 1 2
captureadditionalinteractionsbeyondthoserepresentedbysingularvalues. Thisbandedperturbation
induceslocalinteractions,allowingspecificsingularvaluestointeractwiththeirimmediateneighbors,
ensuringsmoothertransitions. Thismethod,althoughdeviatingfromthecanonicalformofSVD,
providesamechanismtocapturelocalizedinteractions.

### Random

(cid:0) SVFTR(cid:1)
. A straightforward heuristic for populating M involves randomly selecting
d
kelementstobelearnable.

### Top-k

(cid:0) SVFTT(cid:1)
. Thefinaldesignchoiceweexploreinvolvescomputingthealignmentbetween
d
the left and right singular vectors as uTv . We then select the top-k elements and make them
i j
learnable. However,notethatthisonlyworkswhenleftandrightsingularvectorshavethesame
size. Apossibleinterpretationofthisiswemakeonlythetop-kstronginteractionsbetweensingular
vectordirectionslearnable.
WeillustratetheseSVFTdesignchoicesinFigure3. Ourempiricalresultsdemonstratethatthese
simpledesignchoicessignificantlyenhanceperformancecomparedtostate-of-the-artPEFTmethods.
Note that SVFTP has a fixed number of learnable parameters, while the remaining variants are
configurable. Wehypothesizethatfurtherinnovationislikelyachievablethroughoptimizingthe
sparsitypatternofM,includingefficientlearned-sparsitymethods. Inthispaper,weexplorethese
fourchoicestovalidatetheoverallidea: determiningaperturbationusingthesingularvectorsofthe
matrixthatisbeingperturbed.
3.2 PropertiesofSVFT
Wehighlightsomepropertiesof SVFT inthefollowinglemmaandprovideinsightsintohowits
specificalgebraicstructurecomparesandcontrastswithbaselinePEFTmethods.
Lemma: LetW beamatrixofsized ×d withSVDgivenbyUΣVT. Consideranupdated
0 1 2
finalmatrixW +UMVT,whereM isamatrixofthesamesizeasΣ,whichmayormaynotbe
0
diagonal. Then,thefollowingholds:
3Learnableparametersareunderlined.
4

<!-- Page 5 -->

(a) Structure:IfM isalsodiagonal(i.e. theplainSVFT),thenthefinalmatrixW +UMVT
0
hasU asitsleftsingularvectorsandsign(Σ+M)VT asitsrightsingularvectors. That
is,itssingularvectorsareunchanged,exceptforpossiblesignflips. Conversely,ifM is
notdiagonal(i.e.,variantsofSVFTotherthanplain),thenU andV maynolongerbethe
singulardirectionsofthefinalmatrixW +UMVT.
0
(b) Expressivity: Given any target matrix P of size d ×d , there exists an M such that
1 2
P = W +UMVT. Thatis,ifM isfullytrainable,anytargetmatrixcanberealized
0
usingthismethod.
(c) Rank: If M has k non-zero elements, then the rank of the update UMVT is at most
min{k,min{d ,d }}. Forthesamenumberoftrainableparameters,SVFTcanproduce
1 2
a much higher rank perturbation than LoRA (eventually becoming full rank), but in a
constrainedstructuredsubspace.
WeprovideourproofsinAppendixA.Buildingonthislemma,wenowcomparetheformofthe
SVFTupdatewithLoRAandVeRA.
SVFT’s∆W canbewrittenasasumofrank-onematrices:
(cid:88)
∆W = m u vT (2)
ij i j
(i,j)∈Ω
whereu istheithleftsingularvector,v isthejthrightsingularvector,andΩisthesetofnon-zero
i j
elementsinM.
Thus,ourmethodinvolvesaddingaweightedcombinationofspecificrank-oneperturbationsofthe
formu vT.
i j
LoRAandVeRAupdatescanalsobeexpressedassumsofrank-onematrices.
r r
∆W = (cid:88) a b T and ∆W = (cid:88) α (aˆ ⊙β)bˆT (3)
LoRA i i VeRA i i i
i=1 i=1
wherea andb arethetrainablecolumnsofAandB matricesinLoRA.InVeRA,aˆ andbˆ are
i j i i
randomandfixedvectors,whileαandβrepresentthediagonalelementsofΛ andΛ respectively.
d b
NotethatLoRArequiresd +d trainableparametersperrank-onematrix,whileSVFTandVeRA
1 2
requireonlyone. AlthoughLoRAcanpotentiallycapturedirectionsdifferentfromthoseachievable
bythefixed{u ,vT}pairs,eachofthesedirectionsincursasignificantlyhigherparametercost.
i j
VeRAcapturesnewdirectionsataparametercostsimilartoSVFT;however,thereisakeydistinction:
inVeRA,eachvectoraˆ orbˆ appearsinonlyoneoftherank-onematrices. Incontrast,inSVFT,
i i
thesamevectoru canappearinmultipletermsinthesummation,dependingonthesparsitypattern
i
ofM. Thisresultsinanimportantdifference: unlikeSVFT,VeRAisnotuniversallyexpressive–it
cannotrepresentanytargetmatrixP. Moreover,aˆ ,bˆ arerandom,whileu ,v dependonW .
i i i j 0
Note. SVFTrequiresstoringbothleftandrightsingularvectorsduetoitscomputationoftheSVD
onpre-trainedweights. WhilethisincreasesmemoryusagecomparedtoLoRA(whichisroughly
double),itremainslowerthanBOFT.Wepartiallyaddressthisthroughsystem-leveloptimizations
likemixed-precisionweights(e.g.,bfloat16). Furtherexplorationofmemory-reductiontechniques,
suchasquantization,isplannedasfuturework.Importantly,inferencetimeandmemoryconsumption
remainthesameacrossallmethods,includingSVFT,astheweightscanbefused.
4 Experiments
4.1 BaseModels
Weadaptwidely-usedlanguagemodels,encoder-onlymodel(DeBERTaV3 [10])andtwodecoderbase
onlymodels(Gemma-2B/7B[29],LLaMA-3-8B[1]). Wealsoexperimentwithvisiontransformer
models(ViT-B/16andViT-L/16)[9])pre-trainedonImageNet-21k[8],followingpriorwork[16].
5

<!-- Page 6 -->

Thecompletedetailsofourexperimentalsetupandhyperparameterconfigurationsareprovidedin
AppendixC.
Baselines. WecomparewithFullFine-Tuning(FT)updatingalllearnableparametersinalllayers,
alongwithLoRA[14],DoRA[18],BOFT[19]andVeRA[16].4
4.2 Datasets
Language. For natural language generation (NLG) tasks, we evaluate on GSM-8K [7] and
MATH [11] by fine-tuning on MetaMathQA-40K [32], following [19]. We also evaluate on 8
commonsense reasoning benchmarks (BoolQ [5], PIQA [3], SIQA [28], HellaSwag [33], Winogrande[27],ARC-easy/challenge[6],andOpenBookQA[22]). Wefollowthesettingoutlinedin
prior work [18, 15], where the training sets of all benchmarks are amalgamated for fine-tuning.
Wefine-tuneon15Kexamplesfromthistrainingset. Fornaturallanguageunderstanding(NLU),
weevaluateontheGeneralLanguageUnderstandingEvaluation(GLUE)benchmarkconsistingof
classificationandregressiontasks,inlinewith[16,14].
Vision. Ourexperimentsonvisiontasksconsistof4benchmarks: CIFAR-100[17],Food101[4],
RESISC45[30],andFlowers102[23]. Wefollowthesetupfrom [16],andfine-tuneonasubset
comprising10samplesfromeachclass.
Table 1: Performance (Accuracy) on Mathematical Reasoning (GSM-8K and MATH). #Params
denote the number of trainable parameters. bold and underline represent best and second best
performingPEFTmethod, respectively. SVFT offerssuperior/competitiveperformanceatmuch
lower#Params. ForSVFTR,wesetd=16forGemmaandd=12forLLaMA-3models.
d
Gemma-2B Gemma-7B LLaMA-3-8B

### Method

# ParamsGSM-8KMATH#ParamsGSM-8KMATH#ParamsGSM-8KMATH
Full-FT 2.5B 52.69 17.94 8.5B 74.67 25.70 8.0B 64.13 16.24
LoRA 26.2M 43.06 15.50 68.8M 76.57 29.34 56.6M 75.89 24.74
r=32
DoRA 13.5M 44.27 16.18 35.5M 74.52 29.84 29.1M 75.66 24.72
r=16
BOFTb=8 1.22M 36.01 12.13 2.90M 71.79 28.98 4.35M 67.09 21.64
m=2
DoRA 1.19M 35.25 13.04 3.26M 74.37 26.28 2.55M 68.30 21.96
r=1
LoRA 0.82M 32.97 13.04 0.82M 72.4 26.28 1.77M 68.84 20.94
r=1
VeRA 0.63M 36.77 14.12 0.43M 71.11 27.04 0.98M 63.76 20.28
r=1024
SVFTP 0.19M 40.34 14.38 0.43M 73.50 27.30 0.48M 69.22 20.44
SVFTR 6.35M 50.03 15.56 19.8M 76.81 29.98 13.1M 75.90 24.22
d
5 Results
5.1 PerformanceonLanguageTasks
NaturalLanguageGeneration. Wepresentresultsonmathematicalquestionansweringagainst
baselinePEFTtechniquesacrossthreebasemodels–varyingfrom2Bto8BparametersinTable1.
Toensureacomprehensivecomparison,wetestbaselinetechniques(LoRA,DoRA)withdifferent
configurations, and varying hyper-parameters like rank to cover a range of learnable parameters
fromlowtohigh. Notethatevenwhentherankisaslowas1,bothmethodsyieldmoretrainable
parameters than SVFTP. SVFTP (∼0.2M) shows as much as 18% relative improvement over
techniquesthatuse6×moretrainableparameters(BOFTb=8 ,LoRA ). Againsttechniquesof
m=2 r=1
comparablesizes(VeRA),SVFTP achieves15.5%relativeimprovementonaverage. Eveninthe
defaultregime, SVFTR matchestechniqueswithatleast3×moretrainableparameters. Notably,
d
4BOFTisapproximatelythreetimesslowerthanLoRA.ThesharedmatricesinVERAcanbecomealimiting
factorformodelswithnon-uniforminternaldimensions,suchasLLaMA-3.
6

<!-- Page 7 -->

Table 2: Evaluation results on eight commonsense reasoning benchmarks with Gemma-7B. We
follow[18]forhyperparameterconfigurations,andreportaccuracyforalltasks. HSandWGdenote
HellaSwag[33]andWinoGrande[27],respectively. SVFTP offerscompetitiveperformanceata
fractionof#Params. SVFTB canmatchLoRA with∼7xfewerparameters.
d=8 r=32
Method #Params BoolQ PIQA SIQA HS WG ARC-e ARC-c OBQA Average
Full-FT 8.5B 72.32 87.32 76.86 91.07 81.76 92.46 82.76 89.00 84.19
LoRA 68.8M 71.55 87.95 77.27 91.80 79.71 92.67 82.16 86.40 83.69
r=32
DoRA 35.5M 71.46 87.59 76.35 92.11 78.29 92.00 80.63 85.60 83.00
r=16
DoRA 3.31M 68.22 86.72 75.23 91.14 78.13 91.87 83.19 86.20 82.59
r=1
VeRA 1.49M 64.25 86.28 74.04 86.96 69.00 92.76 82.33 82.00 79.70
r=2048
LoRA 0.82M 65.44 86.28 75.02 89.91 75.92 91.79 81.91 85.40 81.46
r=1
SVFTP 0.51M 67.92 86.45 75.47 86.92 74.03 91.80 81.23 83.00 80.85
SVFTB 9.80M 71.90 86.98 76.28 91.55 78.76 92.80 83.11 85.40 83.35
d=8
Table3: DeBERTaV3 withdifferentadaptationmethodsontheGLUEbenchmark. Wereport
base
matchedaccuracyforMNLI,Matthew’scorrelationforCoLA,PearsoncorrelationforSTS-B,and
accuracyforothertasks. Higherisbetterforalltasks. *indicatesnumberspublishedinpriorwork.
Method #Params MNLI SST-2 MRPC CoLA QNLI QQP RTE STS-B Avg.
Full-FT* 184M 89.90 95.63 89.46 69.19 94.03 92.40 83.75 91.60 88.25
LoRA* 1.33M 90.65 94.95 89.95 69.82 93.87 91.99 85.20 91.60 88.50
r=8
DoRA 0.75M 89.92 95.41 89.10 69.37 94.14 91.53 87.00 91.80 88.53
r=4
BOFT*b=8 0.75M 90.25 96.44 92.40 72.95 94.23 92.10 88.81 91.92 89.89
m=2
LoRA 0.17M 90.12 95.64 86.43 69.13 94.18 91.43 87.36 91.52 88.23
r=1
VeRA 0.09M 89.93 95.53 87.94 69.06 93.24 90.4 87.00 88.71 87.73
r=1024
SVFTP 0.06M 89.69 95.41 88.77 70.95 94.27 90.16 87.24 91.80 88.54
SVFTR 0.28M 89.97 95.99 88.99 72.61 93.90 91.50 88.09 91.73 89.10
d=2
onGSM-8K, SVFTR againachieves96%ofthefullfine-tuningperformance, whileDoRA
d r=16
recovers86%with2×moreparametersthanSVFTR.
d
Commonsense Reasoning. In Table 2, we compare performance on commonsense reasoning
benchmarkswithGemma-7B,andobservesimilartrends. Inthelowerandmoderatelyparameterizedregime(∼0.43M),SVFTP showscompetitiveperformanceincomparisontoLORA
r=1
and
DoRA ,whichhave1.9×and7.7×moreparameters,respectively. AgainstVeRA,whichtrains
r=1
3.5×moreparameters,SVFTP showsarelativeimprovementof∼1.16%. Similarly,SVFTB also
d=8
matchesorexceedsmethodsthatuseupto7×moretrainableparameters. Forinstance,SVFTB
d=8
attainsanaverageperformanceof83.35%withonly9.8Mparameters,closelymatchingLoRA
r=16
(83.69%,68.8Mparameters). WeobservesimilartrendswithGemma-2B(referTable8).
NaturalLanguageUnderstanding. ResultsontheGLUEbenchmarkaresummarizedinTable3.
SVFTmatchesLoRA andDoRA whichuse12-22×moretrainableparameters. Similarly,
r=8 r=4
whencomparedtoOFTandBOFT,SVFTP maintainsacomparableaverageperformancedespite
being12×smaller. TheseresultshighlightSVFT’sabilitytostrikeabalancebetweenparameter
efficiencyandperformance,makingitanattractivePEFTchoiceforsimpleclassificationtasks.
Parameterefficiency. InFigure1,weplottheperformanceofSVFTonmathematicalreasoning
andcommonsensereasoningagainstotherPEFTtechniquesacrossarangeofconfigurations. Across
7

<!-- Page 8 -->

Table4: Performanceonimageclassificationbenchmarks. ForLoRA,DoRAandSVFTB,weadapt
{Q,K,V,U,D}modulesofthetransformer.ForSVFTP,weadaptonly{Q,V}tokeepitcomparable
withVeRA.Wereportaccuracyforalltasks.
ViT-B ViT-L

### Method

# Params CIFAR100 Flowers102 #Params Food101 Resisc45

### Head - 78.25 98.42 - 75.57 64.10

Full-FT 85.8M 85.35 98.37 303.3M 77.83 76.83
LoRA 1.32M 84.10 99.23 3.54M 77.13 79.62
r=8
DoRA 1.41M 85.03 99.30 3.76M 76.41 78.32
r=8
BOFTb=4 0.11M 85.54 98.59 2.95M 78.42 74.70
m=4
LoRA 0.16M 84.86 96.88 0.44M 75.97 78.02
r=1
DoRA 0.25M 84.46 99.15 0.66M 75.90 78.02
r=1
VeRA 24.6K 83.38 98.59 0.06M 75.97 72.44
r=256

## Svftp 18.5K 83.85 98.93 0.05M 75.95 71.97


## Svftb 0.27M 84.72 99.28 0.74M 77.94 79.70

d=2

## Svftb 0.93M 85.69 98.88 2.5M 78.36 73.83

d=8
trainableparameterbudgetsrangingfromlowesttohighest,SVFTobtainsthebestoverallperformance,matchingmethodsthatrequiresignificantlymoretrainableparameters. Theseresultsestablish
SVFTasaPareto-dominantapproachforparameter-efficientfine-tuning.
5.2 PerformanceonVisionTasks
48
46
44
42
40
38
36
34
32
30
0.05 0.1 0.2 0.4 0.8 1.6 3 5.5
Number of Trainable Params (M)
)%(
ycaruccA
Table4contrastsSVFTagainstotherPEFTtechniqueson
imageclassificationbenchmarksusingViT-BandViT-L
models. ForViT-B,SVFTB surpassesfullfine-tuning Weight Types
d=8 Q,V
performance along with LoRA and DoRA on Q,K,V
r=8 r=8 U,D
CIFAR-100. SVFTB matchesLoRA andDoRA Q,K,V,U,D d=2 r=8 r=8 Q,K,V,U,D,G,O
onFlowers102withupto5×fewerparameters.ForViT-L,
SVFTB alsodemonstratessuperiororcompetitiveperford
manceonbothFood101andResisc45,withsignificantly
lower trainable parameters compared to both fully fine- Configuration
P tunedmodelsandotherstate-of-the-artPEFTapproaches. d=2
d=4
d=8
5.3 ContributionofEachWeightType

### Figure 4: Performance variation with

InFigure4,weinvestigatethecontributionofeachweight SVFTB based on the adapted weight
d
type. Starting with the base configuration, we apply matrices – GSM-8K with Gemma-2B.
SVFTBtotheQandV weightsineachtransformerblock Adapting more target weight types red
andreporttheperformance. Wethenincrementallyadd sultsingreatergainsinperformance. Intheremainingweightmodules(K,U,D,O,G)andob- terestingly,forafixedparameterbudget,
servethechangesinperformance. Foreachconfiguration, adapting U and D weight types gives
wealsovarythetrainableparametersbyincrementingthe greaterliftsthanadaptingQandV.
totallearnableoff-diagonals.
NotethatapplyingSVFTB toU,D,O,andGdoesnotincreasetrainableparametersasmuchas
d
applyingLoRA/DoRAtothesemodules(Table7). Forexample,foralargematrixofshaped ×d ,
1 2
LoRA learns d +d parameters, while SVFTP learns min(d ,d ) parameters. We observe
r=1 1 2 1 2
thatadaptingonlyU andD with SVFT yieldsuptoa10%relativeimprovementoveradapting
8

<!-- Page 9 -->

QandV forthesameparameterbudget(∼0.8M). Ourfindingsindicatethatadaptingmoreweight
typesenhancesperformance.

### Table5:Resultsonfine-tuningGemma-2Bwith

Table 6: Impact of pre-trained weight qual-
SVFTusingdifferentM parameterizations.
ity. Results on GSM-8K after fine-tuning on
Pythia-2.8B checkpoints at different stages of

### Structure#Params GSM-8K MATH

pre-training (PT). Compared to LoRA, SVFT
benefits more from better pre-trained weights.
Plain 0.2M 40.34 14.38 SVFToutperformsLoRAinbothcases.

## 3M 46.47 16.04


### Banded PTSteps

6.4M 47.84 15.68 Method #Params ∆Perf

## 39K 143K


## 3M 47.76 15.98


### Random

6.4M 50.03 15.56 Full-FT 2.5B 21.00 30.09 9.09
LoRA 5.24M 11.22 18.95 7.73

## 3M 48.00 15.80

Top-k SVFT 5.56M 15.08 23.19 8.11

## 4M 49.65 15.32

5.4 ImpactofM’sStructureonPerformance
We analyze the impact of different parameterizations of M (Plain, Banded, Random, Top-k) on
downstreamperformance. Toensureafaircomparison,wematchthenumberoftrainablecoefficients
acrossallvariants. AsshowninTable5,bothRandomandTop-kvariantsoutperformBandedonthe
GSM-8Kdataset. However,thisimprovementcomesatthecostofperformanceonMATH.Thisobservationsuggeststhatthechoiceofparameterizationhasasignificantimpactonmodelperformance,
andtheeffectivenessofaparticularstructuremayvarydependingonthedownstreamtask.
5.5 ImpactofPre-trainedWeightQuality
AkeyfeatureofSVFTisthattheweightupdatedependsonthepre-trainedweightsW. Wetherefore
askthefollowingquestion: Doesthequalityofpre-trainedweightshaveadisproportionateimpact
onSVFT?Toanswerthis,weconsidertwocheckpointsfromthePythiasuite[2]atdifferentstages
oftraining, i.e., 39Kstepsand143Ksteps, respectively. Wefine-tuneeachofthesecheckpoints
independentlywithFull-FT,LoRA,andSVFT.Wethencomparetheincreaseinperformance(∆Perf).
AsshowninTable6,comparedtoLoRA,SVFTbenefitsmorefrombetterpre-trainedweights. We
alsonotethatSVFToutperformsLoRAinbothsettings,suggestingthatthebenefitsofinducinga
∆W thatexplicitlydependsonW arebeneficialevenwhenW issub-optimal.
6 Discussion
Limitations. Despitesignificantlyreducinglearnableparametersandboostingperformance,SVFT
incurs some additional GPU memory usage. Unlike LoRA and its variants, SVFT necessitates
computingtheSVDandstoringbothleftandrightsingularvectors. Whilememoryconsumption
remains lower than BOFT, it’s roughly double that of LoRA. We mitigate this in our work by
employingsystem-leveloptimizationslikemixed-precisionweights(e.g.,bfloat16). However,similar
tothescalingexploredin[31],memoryusageshouldamortizewiththeincreasingscaleofadaptation
tasks. Infutureworkwewillexplorequantizationandothertechniquestoaddressmemoryconcerns.
BroaderImpact. Ourworkenableseasierpersonalizationoffoundationalmodels,whichcanhave
bothpositiveandnegativesocietalimpacts. Sinceourmethodprovidescomputationalefficiency
(smallerparameterfootprint),itwillbelessexpensivetoenablepersonalization.
9

<!-- Page 10 -->

7 Conclusion
ThisworkintroducesSVFT,anovelandefficientPEFTapproachthatleveragesthestructureofpretrainedweightstodetermineweightupdateperturbations.Weproposefoursimpleyeteffectivesparse
parameterizationpatterns,offeringflexibilityincontrollingthemodel’sexpressivityandthenumber
oflearnableparameters. ExtensiveexperimentsonlanguageandvisiontasksdemonstrateSVFT’s
effectivenessasaPEFTmethodacrossdiverseparameterbudgets. Furthermore,wetheoretically
showthatSVFTcaninducehigher-rankperturbationupdatescomparedtoexistingmethods,fora
fixedparameterbudget. Infuturework,weaimtodevelopprincipledmethodstogeneratesparsity
patterns,potentiallyleadingtofurtherperformanceimprovements.

### Acknowledgements

WethankCISPAHelmholtzCenterforInformationSecurityandGregKuhlmannfortheirinvaluable
supportinfacilitatingthisresearch. WealsoappreciateAnubhavGoelforhishelpfuldiscussionsand
support.

### References

[1] MetaAI. Introducingmetallama3: Themostcapableopenlyavailablellmtodate. April2024.
[2] StellaBiderman,HaileySchoelkopf,QuentinAnthony,HerbieBradley,KyleO’Brien,Eric
Hallahan,MohammadAflahKhan,ShivanshuPurohit,USVSNSaiPrashanth,EdwardRaff,
AviyaSkowron,LintangSutawika,andOskarvanderWal. Pythia: Asuiteforanalyzinglarge
languagemodelsacrosstrainingandscaling,2023.
[3] YonatanBisk,RowanZellers,RonanLeBras,JianfengGao,andYejinChoi. Piqa: Reasoning
about physical commonsense in natural language. In Thirty-Fourth AAAI Conference on
ArtificialIntelligence,2020.
[4] LukasBossard,MatthieuGuillaumin,andLucVanGool. Food-101–miningdiscriminative
componentswithrandomforests. InEuropeanConferenceonComputerVision,2014.
[5] ChristopherClark,KentonLee,Ming-WeiChang,TomKwiatkowski,MichaelCollins,and
Kristina Toutanova. Boolq: Exploring the surprising difficulty of natural yes/no questions,
2019.
[6] PeterClark,IsaacCowhey,OrenEtzioni,TusharKhot,AshishSabharwal,CarissaSchoenick,
andOyvindTafjord. Thinkyouhavesolvedquestionanswering? tryarc,theai2reasoning
challenge,2018.
[7] KarlCobbe,VineetKosaraju,MohammadBavarian,MarkChen,HeewooJun,LukaszKaiser,
MatthiasPlappert,JerryTworek,JacobHilton,ReiichiroNakano,ChristopherHesse,andJohn
Schulman. Trainingverifierstosolvemathwordproblems. arXivpreprintarXiv:2110.14168,
2021.
[8] JiaDeng, WeiDong, RichardSocher, Li-JiaLi, KaiLi, andLiFei-Fei. Imagenet: Alargescalehierarchicalimagedatabase. In2009IEEEconferenceoncomputervisionandpattern
recognition,pages248–255.Ieee,2009.
[9] AlexeyDosovitskiy,LucasBeyer,AlexanderKolesnikov,DirkWeissenborn,XiaohuaZhai,
Thomas Unterthiner, Mostafa Dehghani, Matthias Minderer, Georg Heigold, Sylvain Gelly,
JakobUszkoreit,andNeilHoulsby. Animageisworth16x16words: Transformersforimage
recognitionatscale. InInternationalConferenceonLearningRepresentations,2021.
[10] PengchengHe,JianfengGao,andWeizhuChen. Debertav3: Improvingdebertausingelectrastylepre-trainingwithgradient-disentangledembeddingsharing,2023.
[11] DanHendrycks,CollinBurns,SauravKadavath,AkulArora,StevenBasart,EricTang,Dawn
Song,andJacobSteinhardt. Measuringmathematicalproblemsolvingwiththemathdataset,
2021.
10

<!-- Page 11 -->

[12] KarlMoritzHermann,TomášKocˇiský,EdwardGrefenstette,LasseEspeholt,WillKay,Mustafa
Suleyman,andPhilBlunsom. Teachingmachinestoreadandcomprehend. InProceedingsof
the28thInternationalConferenceonNeuralInformationProcessingSystems,NIPS’15,page
1693–1701.MITPress,2015.
[13] NeilHoulsby,AndreiGiurgiu,StanislawJastrzebski,BrunaMorrone,QuentinDeLaroussilhe,
AndreaGesmundo,MonaAttariyan,andSylvainGelly. Parameter-efficienttransferlearningfor
NLP. InProceedingsofthe36thInternationalConferenceonMachineLearning,Proceedings
ofMachineLearningResearch.PMLR,2019.
[14] Edward J Hu, Yelong Shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean Wang,
Lu Wang, and Weizhu Chen. LoRA: Low-rank adaptation of large language models. In
InternationalConferenceonLearningRepresentations,2022.
[15] ZhiqiangHu,LeiWang,YihuaiLan,WanyuXu,Ee-PengLim,LidongBing,XingXu,Soujanya
Poria,andRoyKa-WeiLee.Llm-adapters:Anadapterfamilyforparameter-efficientfine-tuning
oflargelanguagemodels,2023.
[16] DawidJanKopiczko, TijmenBlankevoort, andYukiMAsano. ELoRA:Efficientlow-rank
adaptationwithrandommatrices. InTheTwelfthInternationalConferenceonLearningRepresentations,2024.
[17] AlexKrizhevsky,GeoffreyHinton,etal. Learningmultiplelayersoffeaturesfromtinyimages.
2009.
[18] Shih-Yang Liu, Chien-Yi Wang, Hongxu Yin, Pavlo Molchanov, Yu-Chiang Frank Wang,
Kwang-TingCheng,andMin-HungChen. Dora: Weight-decomposedlow-rankadaptation,
2024.
[19] WeiyangLiu,ZejuQiu,YaoFeng,YuliangXiu,YuxuanXue,LonghuiYu,HaiwenFeng,Zhen
Liu,JuyeonHeo,SongyouPeng,YandongWen,MichaelJ.Black,AdrianWeller,andBernhard
Schölkopf. Parameter-efficientorthogonalfinetuningviabutterflyfactorization. InTheTwelfth
InternationalConferenceonLearningRepresentations,2024.
[20] YinhanLiu,MyleOtt,NamanGoyal,JingfeiDu,MandarJoshi,DanqiChen,OmerLevy,Mike
Lewis,LukeZettlemoyer,andVeselinStoyanov. Roberta: Arobustlyoptimizedbertpretraining
approach,2019.
[21] FanxuMeng,ZhaohuiWang,andMuhanZhang. Pissa: Principalsingularvaluesandsingular
vectorsadaptationoflargelanguagemodels. arXivpreprintarXiv:2404.02948,2024.
[22] TodorMihaylov,PeterClark,TusharKhot,andAshishSabharwal. Canasuitofarmorconduct
electricity? anewdatasetforopenbookquestionanswering,2018.
[23] Maria-ElenaNilsbackandAndrewZisserman. Automatedflowerclassificationoveralarge
numberofclasses. InIndianConferenceonComputerVision,GraphicsandImageProcessing,
Dec2008.
[24] ZejuQiu,WeiyangLiu,HaiwenFeng,YuxuanXue,YaoFeng,ZhenLiu,DanZhang,Adrian
Weller,andBernhardSchölkopf. Controllingtext-to-imagediffusionbyorthogonalfinetuning.
InThirty-seventhConferenceonNeuralInformationProcessingSystems,volume36,pages
79320–79362,2023.
[25] ColinRaffel,NoamShazeer,AdamRoberts,KatherineLee,SharanNarang,MichaelMatena,
YanqiZhou,WeiLi,andPeterJ.Liu. Exploringthelimitsoftransferlearningwithaunified
text-to-texttransformer. JournalofMachineLearningResearch,21(140):1–67,2020.
[26] BaptisteRozière,JonasGehring,FabianGloeckle,StenSootla,ItaiGat,XiaoqingEllenTan,
YossiAdi,JingyuLiu,RomainSauvestre,TalRemez,JérémyRapin,ArtyomKozhevnikov,
IvanEvtimov,JoannaBitton,ManishBhatt,CristianCantonFerrer,AaronGrattafiori,Wenhan
Xiong,AlexandreDéfossez,JadeCopet,FaisalAzhar,HugoTouvron,LouisMartin,Nicolas
Usunier,ThomasScialom,andGabrielSynnaeve. Codellama: Openfoundationmodelsfor
code,2024.
11

<!-- Page 12 -->

[27] KeisukeSakaguchi,RonanLeBras,ChandraBhagavatula,andYejinChoi. Winogrande: An
adversarialwinogradschemachallengeatscale,2019.
[28] MaartenSap,HannahRashkin,DerekChen,RonanLeBras,andYejinChoi. Socialiqa: Commonsensereasoningaboutsocialinteractions,2019.
[29] GemmaTeam,ThomasMesnard,CassidyHardin,RobertDadashi,SuryaBhupatiraju,Shreya
Pathak,LaurentSifre,MorganeRivière,MihirSanjayKale,JulietteLove,etal. Gemma: Open
modelsbasedongeminiresearchandtechnology. arXivpreprintarXiv:2403.08295,2024.
[30] IhsanUllah,DustinCarrion,SergioEscalera,IsabelleMGuyon,MikeHuisman,FelixMohr,
Jan N van Rijn, Haozhe Sun, Joaquin Vanschoren, and Phan Anh Vu. Meta-album: Multidomainmeta-datasetforfew-shotimageclassification. InThirty-sixthConferenceonNeural
InformationProcessingSystemsDatasetsandBenchmarksTrack,2022.
[31] YemingWenandSwaratChaudhuri. Batchedlow-rankadaptationoffoundationmodels. In
TheTwelfthInternationalConferenceonLearningRepresentations,2024.
[32] LonghuiYu,WeisenJiang,HanShi,JinchengYu,ZhengyingLiu,YuZhang,JamesT.Kwok,
ZhenguoLi,AdrianWeller,andWeiyangLiu. Metamath: Bootstrapyourownmathematical
questionsforlargelanguagemodels,2023.
[33] RowanZellers,AriHoltzman,YonatanBisk,AliFarhadi,andYejinChoi. Hellaswag: Can
a machine really finish your sentence? In Proceedings of the 57th Annual Meeting of the
AssociationforComputationalLinguistics,2019.
[34] JingqingZhang,YaoZhao,MohammadSaleh,andPeterLiu. PEGASUS:Pre-trainingwith
extractedgap-sentencesforabstractivesummarization. InProceedingsofthe37thInternational
ConferenceonMachineLearning,volume119ofProceedingsofMachineLearningResearch,
pages11328–11339.PMLR,13–18Jul2020.
[35] QingruZhang,MinshuoChen,AlexanderBukharin,PengchengHe,YuCheng,WeizhuChen,
andTuoZhao. Adaptivebudgetallocationforparameter-efficientfine-tuning. InTheEleventh
InternationalConferenceonLearningRepresentations,2023.
12

<!-- Page 13 -->


### Appendix

Theappendixisorganizedasfollows.
• In AppendixA,wegiveproofsforthelemmasoutlinedin 3.2.
• In AppendixB,wecomparehowthetrainableparameterscountfordifferentPEFTtechniques(LoRA,DoRA,VeRA)versusourmethodSVFT.
• In AppendixC,wedescriberesultsforadditionalexperimentsandprovideimplementation
detailsforalltheexperiments.

### A Proofs

WeprovidebriefproofsfortheStructure,ExpressivityandtheRanklemmasforSVFT:
(a) Structure: IfM isdiagonal,thenthefinalmatrixW +UMVT canbewrittenas
0
U(Σ+M)VT since W = UΣVT, where (Σ+M) is also a diagonal matrix. Thus,
0
U(Σ+M)VT isavalidanduniqueSVDofW +UMVT uptosignflipsinthesingular
0
vectors.
(b) Expressivity: Finding M for any target matrix P of size d ×d such that P = W +
1 2 0
UMVT is the same as finding M for a new target matrix P′ = P − W such that
0
P′ =UMVT. ForafullSVD,thedimensionofM isd ×d andsincethedimensionof
1 2
P′isalsod ×d ,P′ =UMVT isabijectionandM =UT(P −W )V (sinceU andV
1 2 0
areorthogonal).
(c) Rank: IfM hask non-zeroelements,thentherankoftheupdateUMVT willbeupper
boundedbyk(sincebyGaussianelimination,korlesselementswillremain,thebestcase
being all k elements in the diagonal). We also know that the rank is upper bounded by
min{d ,d },givinganachievableupperboundontherankasmin{k,min{d ,d }}.
1 2 1 2

### B ParameterCountAnalysis

Table 7: Parameter count analysis. L , D , r, k denote total layers being adapted, hidden
tuned model
dimension,rank,andadditionaloff-diagonalsrespectively.
Method TrainableParameterCount
LoRA 2×L ×D ×r
tuned model
DoRA L ×D ×(2r+1)
tuned model
VeRA L ×(D +r)
tuned model

## Svftp L ×D

tuned model
SVFTB L ×(D ×k+(D −k)(k+1))
d=k tuned model model

### C AdditionalExperimentsandImplementationDetails

AllofourexperimentsareconductedonaLinuxmachine(DebianGNU)withthefollowingspecifications: 2xA10080GB,IntelXeonCPU@2.20GHzwith12cores,and192GBRAM.Forallour
experiments(includingbaselineexperiments),weutilizehardware-leveloptimizationslikemixed
weightprecision(e.g.,bfloat16)wheneverpossible.

### C.1 CommonsenseReasoningGemma-2B

WeevaluateandcompareSVFTvariantsagainstbaselinePEFTmethodsoncommonsensereasoning
taskswithGemma-2BmodelandtabulateresultsinTable8.
13

<!-- Page 14 -->

Table8: ResultswithGemma-2Boneightcommonsensereasoningbenchmarks. Wefollow[18]for
hyperparameterconfigurations,andreportaccuracyforalltasks.
Method #ParamsBOOLQPIQASIQAHellaSwagWinograndeARC-EARC-COBQAAverage
Full-FT 2.5B 63.57 74.1 65.86 70.00 61.95 75.36 59.72 69 67.45
LoRA 26.2M 63.11 73.44 63.20 47.79 52.95 74.78 57.16 67.00 62.43
r=32
LoRA 13.5M 62.87 73.93 65.34 53.16 55.51 76.43 59.55 68.4 64.40
r=16
BOFTb=8 1.22M 59.23 63.65 47.90 29.93 50.35 59.04 42.66 41.00 49.22
m=2
VeRA 0.66M 62.11 64.31 49.18 32.00 50.74 58.08 42.83 42.6 50.23
r=2048
LoRA 0.82M 62.2 69.31 56.24 32.47 51.53 69.52 48.8 56.4 55.81
r=1
DoRA 1.19M 62.17 68.77 55.93 32.95 51.22 68.81 48.72 55.6 55.52
r=1
SVFTP 0.19M 62.26 70.18 56.7 32.47 47.04 69.31 50.08 58.4 55.81
SVFTB 6.35M 63.42 73.72 63.86 71.21 59.58 73.69 54.77 66.6 65.86
d=16
Table9: Performanceonimageclassificationbenchmarks. ForLoRA,DoRAandSVFTB,weadapt
d
{Q,K,V,U,D}modulesofthetransformer.ForSVFTP,weadaptonly{Q,V}tokeepitcomparable
withVeRA.Wereportaccuracyforalltasks.
ViT-B ViT-L

### Method

# Params CIFAR100 Flowers102 Food101 Resisc45 #Params CIFAR100 Flowers102 Food101 Resisc45

### Head - 78.25 98.42 74.93 59.95 - 82.95 98.75 75.57 64.10

Full-FT 85.8M 85.35 98.37 76.32 68.03 303.3M 86.56 97.87 77.83 76.83
LoRAr=8 1.32M 84.41 99.23 76.02 76.86 0.35M 86.00 97.93 77.13 79.62
DoRAr=8 1.41M 85.03 99.30 75.88 76.95 3.76M 83.55 98.00 76.41 78.32
BOFTb=2 0.07M 85.55 98.54 76.06 67.70 0.20M 87.84 97.95 77.90 73.97
m=2
BOFTb=4 0.11M 85.54 98.59 76.51 69.44 0.30M 87.72 97.95 78.42 74.70
m=4
LoRAr=1 0.16M 84.86 96.88 73.35 76.33 0.44M 85.97 98.28 75.97 78.02
DoRAr=1 0.25M 84.46 99.15 74.80 77.06 0.66M 84.06 98.11 75.90 78.02
VeRA 24.6K 83.38 98.59 75.99 70.43 61.4K 86.77 98.94 75.97 72.44
SVFTP 18.5K 83.85 98.93 75.68 67.19 49.2K 86.74 97.56 75.95 71.97
SVFTB 0.28M 84.72 99.28 75.64 72.49 0.74M 86.59 98.24 77.94 79.70
d=2
SVFTB 0.50M 83.17 98.52 76.54 66.65 1.32M 87.10 97.71 76.67 71.10
d=4
SVFTB 0.94M 85.69 98.88 76.70 70.41 2.50M 87.26 97.89 78.36 73.83
d=8

### C.2 AdditionalVisionExperiments

For vision tasks, we compare the SVFT banded variants and SVFT plain with baseline PEFT
methodsonclassificationvisiontasksusingViT-BaseandViT-Largemodelsin Table9.

### C.3 AreAllSingularVectorsImportant?

To determine the importance of considering all singular vectors and singular values during finetuning, we reduce the rank of U and V, and truncate Σ and M to an effective rank of r. If the
originalweightmatrixW ∈Rm×n,thenaftertruncation,U ∈Rm×r,V ∈Rn×r. Thistruncation
significantlyreducesthenumberoftrainableparameters,sowecompensatebyincreasingthenumber
ofoff-diagonalcoefficients(d)inM.
Ourresults,withfourdifferentconfigurationsofrandd,arepresentedinTable10.Thefindingsshow
thataverylowrank(r = 128)leadstopoorperformance,evenwhenparametersarematched. A
reasonablyhighrankofr =1536,whichis75%ofthefullrank,stillfailstomatchtheperformance
ofthefull-rankvariantthathas0.25×thetrainableparameters. Thisindicatesthatallsingularvectors
14

<!-- Page 15 -->

significantlycontributetotheendtaskperformancewhenfine-tuningwithSVFT,andthatimportant
informationislostevenwhentruncatingsparingly.
Table 10: Performance with varying rank (r) and the off-diagonal elements (d) of M. When
r =2048,theupdateisfull-rank.
Rank(r) Diags(d) #Params GSM-8K MATH

## 128 64 1.55M 0.98 0.21


## 1536 - 0.15M 16.37 3.64


## 1536 2 0.74M 25.01 6.04


## 2048 - 0.19M 40.34 14.38


### C.4 PerformancevsTotalTrainableParameters

InadditiontotheexperimentsperformedinFigure1forGemma-2Bonchallengingnaturallanguage
generation(NLG)taskslikeGSM-8KandCommonsenseReasoning,wealsoplottheperformance
vstotaltrainableparametersforlargerstate-of-the-artmodelslikeGemma-7BandLLaMA-3-8Bon
GSM-8K.Figure5furtherdemonstratesSVFT’sPereto-dominance. Onlargermodels,weobserve
thatfull-finetuningoverfits,leadingtosub-optimalperformanceincomparisontoPEFTmethods.
78 80
77 SVFTRd=16 78
SVFTBd=12 LoRAr=32
76 LoRAr=32 76
75 Full Fine-Tuning (8500M params) DoRAr=4 DoRAr=16
7
7
2
4 SVFTBd=2 SVFTBd=8
DoRAr=16
7
7
3
4

## Svftp

SVFTBd=2

### DoRAr=1

LoRAr=4 70 LoRAr=1
DoRAr=1

### LoRAr=4

72 LoRAr=1
BOFTbm ==82
6
6
6

## 8 Svftp


### BOFTbm ==82

71 64 Full Fine-Tuning (2500M params)

### VeRAr=1024

70 62 VeRAr=1024
0.5 0.75 1.2 2 3 5 8 12.5 20 32 50 84 0.5 0.75 1.2 2 3 5 8 12.5 20 32 50 81
Number of Trainable Params (M) Number of Trainable Params (M)
)%(
ycaruccA
Figure 5: Performance versus total trainable parameters for GSM-8K on Gemma-7B (left) and
LLaMA-3-8B(right).

### C.5 SettingsforLanguageTasks

NaturalLanguageUnderstanding. Wefine-tunetheDeBERTaV3 [10]modelandapplySVFT
base
toalllinearlayersineverytransformerblockofthemodel. Weonlymoderatelytunethebatchsize,
learningrate,andnumberoftrainingepochs. Weusethesamemodelsequencelengthsusedby [19]
tokeepourcomparisonsfair. Thehyperparametersusedinourexperimentscanbefoundin Table11.
NaturalLanguageGeneration. Seethehyperparametersusedinourexperimentsin Table12. For
LoRA,DoRA,weadaptQ,K,V,U,Dmatrices. WeapplyBOFTonQ,V matricessinceapplying
onmultiplemodulesiscomputationallyexpensive. ForVeRA,whichenforcesaconstraintofuniform
internaldimensionsforsharedmatrices,weapplyonG,U projectionmatricesasityieldsthehighest
numberoflearnableparameters. WeapplySVFTonQ,K,V,U,D,O,GfortheGemmafamilyof
models, and U,D,O,G for LLaMA-3-8B.Note that applying SVFT on thesemodules does not
increasetrainableparametersatthesamerateasapplyingLoRAorDoRAonthemwould. Weadopt
the code base from https://github.com/meta-math/MetaMath.git for training scripts and
evaluationsetupsandusethefine-tuningdataavailableathttps://huggingface.co/datasets/
meta-math/MetaMathQA-40K.
15

<!-- Page 16 -->

Table11: HyperparametersetupusedforDeBERTaV3 ontheGLUEbenchmark.
base
Method Dataset MNLI SST-2 MRPC CoLA QNLI QQP RTE STS-B
Optimizer AdamW

### WarmupRatio 0.1


### LRSchedule Linear


### LearningRate(Head) 6E-03

MaxSeq.Len. 256 128 320 64 512 320 320 128
# Epochs 10 10 30 20 10 6 15 15
BatchSize 32 32 16 16 32 16 4 32

## Svftp

LearningRate 5E-02 5E-02 5E-02 8E-02 8E-02 5E-02 5E-02 5E-02
BatchSize 32 32 16 16 32 32 16 32

## Svftr

d=2 LearningRate 1E-02 1E-02 1E-02 1E-02 3E-02 1E-02 3E-02 1E-02
Table12: Hyperparametersetupusedforfine-tuningonMetaMathQA-40K.
Gemma-2B Gemma-7B LLaMA-3-8B

### Hyperparameter


## Svftp Svftr Svftp Svftr Svftp Svftr

d=16 d=16 d=12
Optimizer AdamW

### WarmupRatio 0.1


### LRSchedule Cosine

LearningRate 5E-02 1E-03 5E-02 1E-03 5E-02 1E-03
MaxSeq. Len. 512
# Epochs 2

### BatchSize 64

CommonsenseReasoning. Seethehyperparametersusedinourexperimentsin Table13. We
adoptthesamesetofmatricesasthatofnaturallanguagegenerationtasks. Weusethecodebasefrom
https://github.com/AGI-Edgerunners/LLM-Adapters,whichalsocontainsthetrainingand
evaluationdata.
Table13: Hyperparametersetupusedforfine-tuningoncommonsense-15K.
Gemma-2B Gemma-7B

### Hyperparameter


## Svftp Svftb Svftp Svftb

d=8 d=8
Optimizer AdamW

### WarmupSteps 100

LRSchedule Linear
MaxSeq. Len. 512
# Epochs 3

### BatchSize 64

LearningRate 5E-02 5E-03 5E-02 1E-03
16

<!-- Page 17 -->

Table14: Hyperparametersetupusedforfine-tuningonallvisiontasks.
Hyperparameter ViT-B ViT-L
Optimizer AdamW

### WarmupRatio 0.1


### WeightDecay 0.01

LRSchedule Linear
# Epochs 10

### BatchSize 64

SVFTP LearningRate(Head) 4E-03

### SVFTP LearningRate 5E-02

SVFTB LearningRate(Head) 4E-03
d=2
SVFTB LearningRate 5E-02
d=2
SVFTB LearningRate(Head) 4E-03
d=8
SVFTB LearningRate 5E-03
d=8

### C.6 SettingsforVisionTasks

Foreachdatasetinthevisiontasks,wetrainon10samplesperclass,using2examplesperclassfor
validation,andtestonthefulltestset. Similartopreviousliterature,wealwaystraintheclassifier
headforthesemethodssincethenumberofclassesislarge. Theparametercountsdonotincludethe
numberofparametersintheclassificationhead. Thehyperparametersarementionedin Table14.
WetunethelearningratesforSVFTandBOFTselectlearningratesforothermethodsfrom[16],run
trainingfor10epochs,andreporttestaccuracyforthebestvalidationmodel. Forallmethods,since
classificationheadhastobefullytrained,wereporttheparametercountotherthantheclassification
head.
17

## Tables

**Table (Page 2):**

| Full |  | Fine-T | uning | (2500M |  | param | s) |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  | SVFTRd= | 16 |  |
|  |  |  |  |  |  |  |  |  |  | SVFTBd | =16 |  |
|  |  |  |  | SVF |  | TBd=4 | S |  | VFTBd= | 8 | DoRA | r |
|  |  |  |  | SVFTBd |  | =2 |  |  |  |  |  | =16 |
|  |  |  |  |  |  |  |  |  | DoRAr | =4 | Lo | RAr=32 |
|  |  |  |  |  |  |  |  |  |  |  |  |  |
| SVFT |  | P | VeR | Ar=204 |  | 8 | L |  | oRAr= | 4 |  |  |
|  |  | VeRA |  | B |  | OFTbm ==82 |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | r | =1024 |  |  | DoRAr= | 1 |  |  |  |  |  |
|  |  |  |  | LoRAr |  | =1 |  |  |  |  |  |  |


**Table (Page 2):**

| Full |  | Fine-T | uning | (2500M |  | param |  | s) |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  | S |  | VFTBd= | SV 8 | FTBd=16 | DoRA | r=16 |
|  |  |  |  | SVF |  | TBd | =4 |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  | SVFT | Bd= | 2 |  |  |  | DoRAr= | 4 | Lo | RAr=32 |
|  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | P | LoRAr | =1 D |  | oRAr=1 |  |  |  |  |  |  |
| SVFT |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | Ve | RAr=2 | 048 B |  | OFTbm ==82 |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |


**Table (Page 6):**

| SVFTP | 0.19M | 40.34 | 14.38 | 0.43M | 73.50 | 27.30 | 0.48M | 69.22 | 20.44 |
|---|---|---|---|---|---|---|---|---|---|
| SVFTR d | 6.35M | 50.03 | 15.56 | 19.8M | 76.81 | 29.98 | 13.1M | 75.90 | 24.22 |


**Table (Page 7):**

| SVFTP | 0.51M | 67.92 | 86.45 | 75.47 | 86.92 | 74.03 | 91.80 | 81.23 | 83.00 | 80.85 |
|---|---|---|---|---|---|---|---|---|---|---|
| SVFTB d=8 | 9.80M | 71.90 | 86.98 | 76.28 | 91.55 | 78.76 | 92.80 | 83.11 | 85.40 | 83.35 |


**Table (Page 7):**

| SVFTP | 0.06M | 89.69 | 95.41 | 88.77 | 70.95 | 94.27 | 90.16 | 87.24 | 91.80 | 88.54 |
|---|---|---|---|---|---|---|---|---|---|---|
| SVFTR d=2 | 0.28M | 89.97 | 95.99 | 88.99 | 72.61 | 93.90 | 91.50 | 88.09 | 91.73 | 89.10 |


**Table (Page 8):**

| SVFTP | 18.5K | 83.85 | 98.93 | 0.05M | 75.95 | 71.97 |
|---|---|---|---|---|---|---|
| SVFTB d=2 | 0.27M | 84.72 | 99.28 | 0.74M | 77.94 | 79.70 |
| SVFTB d=8 | 0.93M | 85.69 | 98.88 | 2.5M | 78.36 | 73.83 |


**Table (Page 8):**

| Wei | ght Types |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|
| Q Q | ,V ,K,V |  |  |  |  |  |  |  |  |
| U Q | ,D ,K,V,U,D |  |  |  |  |  |  |  |  |
| Q | ,K,V,U,D, | G,O |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  | Configu | ration P |
|  |  |  |  |  |  |  |  |  | d=2 d |
|  |  |  |  |  |  |  |  |  | =4 d=8 |


**Table (Page 13):**

| SVFTP | L ×D tuned model |
|---|---|
| SVFTB d=k | L ×(D ×k+(D −k)(k+1)) tuned model model |


**Table (Page 14):**

| SVFTP | 0.19M | 62.26 | 70.18 | 56.7 | 32.47 | 47.04 | 69.31 | 50.08 | 58.4 | 55.81 |
|---|---|---|---|---|---|---|---|---|---|---|
| SVFTB d=16 | 6.35M | 63.42 | 73.72 | 63.86 | 71.21 | 59.58 | 73.69 | 54.77 | 66.6 | 65.86 |


**Table (Page 14):**

| SVFTP | 18.5K | 83.85 | 98.93 | 75.68 | 67.19 | 49.2K | 86.74 | 97.56 | 75.95 | 71.97 |
|---|---|---|---|---|---|---|---|---|---|---|
| SVFTB d=2 | 0.28M | 84.72 | 99.28 | 75.64 | 72.49 | 0.74M | 86.59 | 98.24 | 77.94 | 79.70 |
| SVFTB d=4 | 0.50M | 83.17 | 98.52 | 76.54 | 66.65 | 1.32M | 87.10 | 97.71 | 76.67 | 71.10 |
| SVFTB d=8 | 0.94M | 85.69 | 98.88 | 76.70 | 70.41 | 2.50M | 87.26 | 97.89 | 78.36 | 73.83 |


**Table (Page 15):**

|  |  |  |  |  |  |  |  |  |  |  | SVFTRd | =16 |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  | D | oRAr= | 4 | LoR | Ar=32 |
| Ful | l Fine | -Tu | ni | ng (85 | 00M p |  | aram | s) |  |  |  | DoR | Ar=16 |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| S | VFTP | SV |  | FTBd=2 | DoR |  | Ar=1 |  | Lo | RAr=4 |  |  |  |
|  |  | Lo |  | RAr=1 |  |  | BOFTbm | ==82 |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Ve | RAr= | 1024 |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |


**Table (Page 15):**

|  |  |  |  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  | SVF | TBd=12 |  | LoR | Ar=32 |
|  |  |  |  |  |  |  |  |  |  | DoRAr | =16 |  |
|  |  |  |  | SVF | TBd= | 2 |  | SVFT | Bd=8 |  |  |  |
|  |  |  |  |  |  |  | LoRAr | =4 |  |  |  |  |
|  | SVFT | P | LoRAr= | 1 D | oRAr= |  | 1 |  |  |  |  |  |
|  |  |  |  |  |  |  | BOFTb | m ==82 |  |  |  |  |
| Ful | l Fin | e-Tuni | ng (25 | 00M | param |  | s) |  |  |  |  |  |
|  |  | VeR | Ar=10 | 24 |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |
