---
title: "Content Moderation Systems"
original_file: "./Content_Moderation_Systems.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["llm", "rag", "agents", "evaluation", "multimodal"]
keywords: ["vrcp", "cid", "page", "rscp", "coverage", "vol", "set", "size", "ptt", "table"]
summary: "<!-- Page 1 -->

Verifiably Robust Conformal Prediction

### LinusJeary∗ TomKuipers∗

DepartmentofInformatics DepartmentofInformatics
King’sCollegeLondon,UK King’sCollegeLondon,UK
linus.jeary@kcl.ac.uk tom.kuipers@kcl.ac.uk

### MehranHosseini NicolaPaoletti

DepartmentofInformatics DepartmentofInformatics

### King’sCollegeLondon,UK King’sCollegeLondon,UK

mehran.hosseini@kcl.ac.uk nicola.paoletti@kcl.ac.uk

### Abstract

Conformal Prediction (CP) is a popular uncertainty quantification method "
related_documents: []
---

# Content Moderation Systems

<!-- Page 1 -->

Verifiably Robust Conformal Prediction

### LinusJeary∗ TomKuipers∗

DepartmentofInformatics DepartmentofInformatics
King’sCollegeLondon,UK King’sCollegeLondon,UK
linus.jeary@kcl.ac.uk tom.kuipers@kcl.ac.uk

### MehranHosseini NicolaPaoletti

DepartmentofInformatics DepartmentofInformatics

### King’sCollegeLondon,UK King’sCollegeLondon,UK

mehran.hosseini@kcl.ac.uk nicola.paoletti@kcl.ac.uk

### Abstract

Conformal Prediction (CP) is a popular uncertainty quantification method that
providesdistribution-free,statisticallyvalidpredictionsets,assumingthattraining
andtestdataareexchangeable.Insuchacase,CP’spredictionsetsareguaranteedto
coverthe(unknown)truetestoutputwithauser-specifiedprobability.Nevertheless,
thisguaranteeisviolatedwhenthedataissubjectedtoadversarialattacks,which
oftenresultinasignificantlossofcoverage.Recently,severalapproacheshavebeen
putforwardtorecoverCPguaranteesinthissetting. Theseapproachesleverage
variationsofrandomisedsmoothingtoproduceconservativesetswhichaccount
fortheeffectoftheadversarialperturbations. Theyare,however,limitedinthat
theyonlysupportℓ -boundedperturbationsandclassificationtasks. Thispaper
2
introduces VRCP (Verifiably Robust Conformal Prediction), a new framework
that leverages recent neural network verification methods to recover coverage
guarantees under adversarial attacks. Our VRCP method is the first to support
perturbations bounded by arbitrary norms including ℓ , ℓ , and ℓ , as well as
1 2 ∞
regressiontasks. Weevaluateandcompareourapproachonimageclassification
tasks(CIFAR10, CIFAR100, andTinyImageNet)andregressiontasksfordeep
reinforcementlearningenvironments.Ineverycase,VRCPachievesabovenominal
coverageandyieldssignificantlymoreefficientandinformativepredictionregions
thantheSotA.
1 Introduction
ConformalPrediction(CP)(Vovketal.,2005;AngelopoulosandBates,2021)isapopularuncertainty
quantificationmethod. Inessence,itisamodel-agnostic,distribution-freeframeworkthatallowsone
toconstructpredictionsetsthatareguaranteedtoincludethetrue(unknown)outputwithprobability
greaterthan1−α,whereα∈(0,1)isauser-specifiedmiscoverage/errorrate. Inotherwords,for
atestpoint(x ,y ),CPseekstoconstructapredictionsetC(x )suchthatthefollowing
n+1 n+1 n+1
coverage(a.k.a. validity)guaranteeholds:
P [y ∈C(x )]≥1−α. (1)
xn+1,yn+1 n+1 n+1
Importantly,theaboveguaranteeholdswhenthecalibrationdata,usedtoconstructC(x ),and
n+1
thetestpointareexchangeable(aspecialcaseiswhencalibrationandtestdataarei.i.d.).
∗Authorscontributedequally.
38thConferenceonNeuralInformationProcessingSystems(NeurIPS2024).
4202
voN
61
]OL.sc[
3v24981.5042:viXra

<!-- Page 2 -->

2000
1500
1000
500
0
0 1 2 3 4 5 6 7 8 910

### Set Size

ycneuqerF

### Vanilla

0 1 2 3 4 5 6 7 8 910

### Set Size

ycneuqerF

## Vrcp_I

0 1 2 3 4 5 6 7 8 910

### Set Size

ycneuqerF

## Vrcp_C

0 1 2 3 4 5 6 7 8 910

### Set Size

ycneuqerF

## Rscp+

0 1 2 3 4 5 6 7 8 910

### Set Size

ycneuqerF

## Rscp+ (Ptt)

Figure1: Distributionofpredictionsetsizesforvanillaconformalprediction(vanillaCP)which
violatesEq.(2),aswellasforourproposedrobustalgorithms(VRCP–IandVRCP–C)alongwiththe
SotA(RSCP+andRSCP+(PTT),seeSection3)ontheCIFAR10dataset. Asweobserve,VRCP–I
andVRCP–CcloselyresemblethespreadofvanillaCPpredictionsetsizes,whilsttheSotAfalls
shortofachievingthis. Hereweuseanadversarialperturbationofradiusϵ=0.02,errorrateα=0.1,
numberofsplitsn =50andsmoothingparameter(usedinRSCP+andRSCP+(PTT))σ =2ϵ.
splits
Whenexchangeabilityisviolated,e.g.,inthepresenceoftest-timedistributionshifts,CP’scoverage
guarantee(1)ceasestohold, andwecannotrelyonthepredictionsetsitproduces. Inthiswork,
weaddressshiftsinducedbyadversarialperturbationsonthetestinputs. Inparticular,wefocuson
perturbationsintheformofadditiveℓ -boundednoise.
p
Torecoverguaranteesunderadversarialinputs,thegeneralmechanismistoinflatetheprediction
settopermitlargerdegreesofuncertainty. However,specialcaremustbetakentoavoidproducing
overly large or even trivial sets – i.e. those containing all possible outputs – as such sets do not
provideanyusefulinference.
Contributions WeproposeaCPframeworkthatprovidesstatisticallyvalidpredictionsetsdespite
thepresenceofℓ -boundedadversarialperturbationsatinferencetime.Formally,foranyadversarially
p
perturbedtestpointx˜ =x +δ,ourmethodproducesadversariallyrobustsetsC thatenjoy
n+1 n+1 ϵ
thefollowingguarantee:
P[y ∈C (x˜ )]≥1−α ∀δ s.t. ∥δ∥ ≤ϵ. (2)
n+1 ϵ n+1 p
WhileCPusesanunderlyingpredictorf,oftenaneuralnetwork(NN),toconstructpredictionregions,
thenoveltyofourapproachistoleverageNNverificationalgorithmstocomputeupperandlower
outputboundsoff(x′)foranyx′ ∈B (x)={x′ :∥x′−x∥ ≤ϵ}. Weusetheseboundstoinflate
ϵ p
theCPregions,resultinginprovablyrobustandefficientpredictionsets.Tothebestofourknowledge,
this is the first work that combines NN verification algorithms and CP to construct adversarially
robustpredictionsets. WecallourmethodVRCP(VerifiablyRobustConformalPrediction).
Recent work (discussed in Section 3) achieves adversarially robust coverage using probabilistic
methods,specifically,randomisedsmoothing(Cohenetal.,2019). Ourapproachovercomessomeof
thetheoreticalandempiricaldrawbacksofthesepriormethods,whicharerestrictedtoclassification
taskswithℓ -normboundedguaranteesandareoverlyconservativeinpractice.
2
Thankstoourverification-basedapproach,VRCPisthefirsttoextendadversariallyrobustconformal
predictiontoregressiontasksandthefirsttogobeyondℓ -normboundedguarantees.InSection4,we
2
introducetwoversionsofVRCPthatapplyverificationatcalibrationandinferencetime,respectively.
Further,inSection5,weempiricallyvalidateourtheoreticalguaranteesanddemonstrateadirect
improvementoverpreviousworkintermsofpredictionsetefficiency(i.e.,averagesetsize)compared
topriorwork. Fig.1showsanextractofourresultsonCIFAR10,demonstratingthatVRCPyields
moreinformative(tighter)predictionregions,atrendthatweobserveexperimentallyacrossallour
benchmarks.
2 Preliminaries
WedenotewithR thesetofpositiverealnumbers. Vectorsx ∈ Rd areshowninbolditalicand
+
scalarsx∈Rinitalictypeface. WedenotethenormusedtomakeRdanormedvectorspaceby∥·∥.
Thiscouldforinstancebeℓ ,ℓ ,orℓ -norm. Wheneveraspecificnormisintended,weindicateit
1 2 ∞
usinganindex,e.g.,∥·∥ indicatestheℓ -norm. Wedenotetheϵ-ballaroundapointx∈Rd with
2 2
respecttotheusednormbyB (x).
ϵ
2

<!-- Page 3 -->

2.1 ConformalPrediction
We provide a brief overview of the inductive (or split) vanilla CP approach. Suppose we have a
datasetDcontainingpairs(x,y)sampledi.i.d.froman(unknown)data-generatingdistributionover
afeaturespaceX ⊆RdandlabelspaceY suchthatD ={(x ,y ),...,(x ,y )}.
1 1 m m
WepartitionthedatasetintodisjointtrainingandcalibrationsetsD andD ,lettingn=|D |.
train cal cal
We fit a predictor f on D and define a score function S : (X ×Y) → R as some notion of
train
predictionerror,suchasS(x,y)=∥f(x)−y∥whenf isaregressor,orS(x,y)=1−f(x) when
y
f isaclassifierwithf(·) beingy’spredictedlikelihood.
y
After applying the score function to all calibration points, we construct the score distribution as
F =δ∞/(n+1)+
(cid:80)n
i=1
δsi /n+1,whereδ
s
istheDiracdistributionwithparameters,s
i
=S(x
i
,y
i
)
andδ representstheunknownscore(potentiallyinfinite)ofthetestpoint.
∞
Givenamiscoverage/errorrateαandatestpoint(x ,y ),wedefinethepredictionsetC(x )
n+1 n+1 n+1
byincludingalllabelsthatappearsufficientlylikelyw.r.t.thescoredistribution: C(x )={y ∈
n+1
Y : S(x ,y) ≤ Q (F)}, whereQ (F)isthe1−αquantileofF. Thissetsatisfiesthe
n+1 1−α 1−α
marginalcoverageguaranteeinEq.(1)ifthetestpointandthecalibrationpointsareexchangeable.
2.2 AdversarialAttacks
Neuralnetworkshavebeenshowntobevulnerabletoadversarialattacks,i.e.,smallchangestotheir
inputthatjeopardisetheprediction(Szegedyetal.,2014;BiggioandRoli,2018). Thisnotioncan
beformallydefinedasmaximisinganadversarialobjectivefunction(e.g.,thelossofthetruelabel)
subjectto∥x−x˜∥≤ϵ. Alternatively,itcanbedefinedasfindinganadversarialexamplex˜ ∈Rm,
suchthat∥x−x˜∥≤ϵand∥f(x˜)−y∥≥δforagivenneuralnetworkf :Rd →Rn.
2.3 NeuralNetworkVerification
VariousapproacheshavebeenproposedtoverifytherobustnessofNNsagainstadversarialattacks.
Theseapproachescanbedividedintocompleteandincompletealgorithms. Givenaneuralnetwork
f,averifieriscompleteifitallowscomputingexactboundsf⊥andf⊤fortheimagef(B (x))=
ϵ
{f(x′):x′ ∈B (x)},i.e.,suchthat
ϵ
f⊥ = min {f(x′)}, f⊤ = max {f(x′)}, (3)
x′∈Bϵ(x) x′∈Bϵ(x)
whereminandmaxarecomputedcoordinate-wiseforvector-valuedNNs. Averifierisincomplete,
butsound,ifitcomputesboundsthatarevalidbutnotexact,i.e.,suchthat:
f⊥ ≤ min {f(x′)}, f⊤ ≥ max {f(x′)}. (4)
x′∈Bϵ(x) x′∈Bϵ(x)
Ourresultsareverifier-agnostic,meaningthattheyarevalidforanyverifierthatcanproduceexact
bounds (as in Eq. (3)) or conservative bounds (as in Eq. (4)), depending on the completeness or
incompletenessoftheverifierused. ThefastestandsimplestwaytocomputetheboundsinEq.(4)
istopropagatetheboundsontheinputB (x)throughthenetworktocomputetheoutputbounds.
ϵ
Severalmethodsbasedonthisapproachhavebeenproposed(Gowaletal.,2018;Wangetal.,2018;
Zhangetal.,2018a;Battenetal.,2024;Lopezetal.,2023). Attheexpenseoffastcomputationspeed,
thesemethodsmayresultinlooseboundsinEq.(4). Ontheotherhand,severalcompletemethods
(PulinaandTacchella,2010;Katzetal.,2017;HosseiniandLomuscio,2023)forNNverification
havebeenputforward. Eventhoughthesemethodscomputeexactbounds,theirdownsideistheir
highcomputationalcost.
3 RelatedWork
Adversarially Robust Conformal Prediction Gendler et al. (2021) introduced an algorithm
calledRandomlySmoothedConformalPrediction(RSCP)thatintegratesrandomisedsmoothing
(Duchietal.,2012;Cohenetal.,2019;Salmanetal.,2019)withCPtoproviderobustcoverage
under adversarial attacks. RSCP replaces the CP score function S(x,y) with a smoothed score
S(cid:101)(x,y)obtainedbyaveragingthevaluesofS(x+v,y)overn

## Mc

realisationsofaGaussiannoise
3

<!-- Page 4 -->

vectorv ∼ N(0,σ2I),foragivensmoothinglevelσ. Tocorrectforpotentialℓ -normboundedϵ
2
perturbationsatinferencetime,thecriticalvaluecomputedoverthesmoothedscoresisinflatedby
ϵ/σ. Thismethodproducesempiricallysoundresults,buttheprovidedformalguaranteeswerefound
tobeinvalidinalaterwork(Yanetal.,2023),asdiscussedbelow.
ProvablyRobustConformalPrediction Yanetal.(2023)addresstheissuewiththerobustness
guaranteeofGendleretal.(2021)bycorrectlyboundingtheestimationerrorcausedbytheMonte-
Carlo sampling used when generating the smoothed scores. The bound introduces an additional
hyperparameterβ suchthattheynowfindtheQ ofsmoothcalibratedscoresandinflateby
1−α+2β
(cid:112)
Hoeffding’sbound −ln(β)/2nMC beforecorrectingbyϵ/σ. Furthermore,thesmoothedscoresofthe
testpointsaredecreasedbyanempiricalBernsteinbound. Thisfurtherinflationofthecriticalvalue
anddeflationofsmoothscoresforeachtestpointoftencausetheiramendedalgorithm,so-called
RSCP+,togeneratetrivialpredictionsets.
Toaddressthisissue,theauthorsintroducetwomethodstoimprovetheefficiencyofRSCP+. Firstly,
theyuserobustlycalibratedtraining(RCT),atraining-timeregularisationtechniquethatpenalisesNN
parametersthatcontributetohighscoresforthetruelabel. Ourapproachassumesthattheunderlying
classifierisgiven;hence,wedonotevaluateRCTinourexperiments.
Secondly,theyimplementapost-trainingtransformation(PTT),whichaimstodecreasethevalues
ofthesmoothedcalibrationscoresthatliebetweenQ (thecriticalvalueofthebasescores)and
1−α
Q(cid:101)1−α (thatofthesmoothedscores). Tothispurpose,theytransformtheCDFofthesmoothedscores
S(cid:101)bycomposinglearnedrankingandsigmoidtransformationswithhyperparametersbandT usinga
holdoutsetD sampledi.i.dfromD . PTThoweverisnottheoreticallyguaranteedtoimprovethe
hold cal
averagesetsizescomputedbyRSCP+and,inmanycases,itsefficacyislargelydependentonhow
representativethesampledholdoutsetisofathecalibrationset. WedemonstratetheeffectofPTT’s
sampledependenceempiricallyinSection5.1.
ProbabilisticallyRobustConformalPrediction Ghoshetal.(2023)alsofocusontheadversarial
settingbutmaintainarelaxedformofrobustcoverage,whereinputperturbationsδaredrawnfrom
a specific distribution and only a proportion of such perturbations are sought to be covered. In
contrast,wedonotmakeassumptionsaboutthenoisedistribution,andweaccountforanyϵ-bounded
perturbation.
Alltheworks2 discussedhererelyonrandomisedsmoothingDuchietal.(2012)andassuchare
limitedtotheℓ -norm. Incontrast,ourVRCPapproachreliesonNNverifiers,canbeusedwithany
2
ℓ -normssupportedbytheverificationmethod,anddoesnotrequiresmoothinghyperparametersor
p
holdoutsets.
4 VerifiablyRobustConformalPrediction(VRCP)
Inthissection,weformallyintroducetwovariantsofVRCP.Bothmethodsallowustoconstruct
adversariallyrobustpredictionsetsatinferencetime.
Thefirstvariant,VRCPviaRobustInference(VRCP–I),employsNNverificationatinferencetime
tocomputealowerboundofthescoreforthegiventestinput(best-casescore),therebyobtaining
moreconservativeregions. ThecalibrationprocedureiscomputedasinstandardCP.Thesecond
variant,VRCPviaRobustCalibration(VRCP–C),insteadusesNNverificationatcalibrationtimeto
deriveupperboundsforthecalibrationscores(worst-case),therebyobtainingamoreconservative
calibration threshold (critical value). This allows us to use the regular scores at inference time,
withoutrequiringNNverification.
4.1 VerifiablyRobustConformalPredictionviaRobustInference(VRCP–I)
GivenacalibrationsetD ,atestinputx ,andscorefunctionS(·,·),wecomputetheprediction
cal n+1
setforx asfollows.
n+1
2WeareawareofrelatedcontemporaneousworkbyZargarbashietal.(2024).However,atthetimeofwriting,
neitherthemanuscriptnorthecodewereavailable.
4

<!-- Page 5 -->


## Foreachy ∈Y wecompute,

s⊥(x ,y)≤ inf S(x′,y). (5)
n+1
x′∈Bϵ(xn+1)

## Therobustpredictionsetisthendefinedas

C (x )={y :s⊥(x ,y)≤Q (F)}. (6)
ϵ n+1 n+1 1−α
Below,weshowthatweareabletomaintainthemarginalcoverageguaranteefromEq.(2)forany
ℓ -normboundedadversarialattack.
p
Theorem1. Letx˜ =x +δforacleantestsamplex and∥δ∥ ≤ϵ. Thepredictionset
n+1 n+1 n+1 p
C (x˜ )definedinEq.(6)satisfiesP[y ∈C (x˜ )]≥1−α.
ϵ n+1 n+1 ϵ n+1

### Proof. Weobtainthat

P[y ∈C (x˜ )]=P(cid:2) s⊥(x˜ ,y )≤Q (F) (cid:3)
n+1 ϵ n+1 n+1 n+1 1−α
(cid:20) (cid:21)
≥P inf S(x′,y )≤Q (F) byEq.(5)
n+1 1−α
x′∈Bϵ(x˜n+1)
≥P[S(x ,y )≤Q (F)] ≥ 1−α.
n+1 n+1 1−α
4.2 VerifiablyRobustConformalPredictionviaRobustCalibration
GivenacalibrationsetD ,atestinputx ,andscorefunctionS(·,·),wecomputetherobustly
cal n+1
calibratedpredictionsetforx asfollows.
n+1

## Wecomputetheupper-boundcalibrationdistributionas:

F⊤ = δ ∞ + (cid:88) n δ s⊤ i ,wheres⊤ ≥ sup S(x′,y ). (7)
(n+1) n+1 i i
i=1
x′∈Bϵ(xi)

## Therobustpost-calibrationpredictionsetisthendefinedas

C (x )={y :S(x ,y)≤Q (F⊤)}. (8)
ϵ n+1 n+1 1−α
Theorem2. Letx˜ =x +δforacleantestsamplex and∥δ∥ ≤ϵ. Thepredictionset
n+1 n+1 n+1 p
C (x˜ )definedinEq.(8)satisfiesP[y ∈C (x˜ )]≥1−α.
ϵ n+1 n+1 ϵ n+1

### Proof. Wehavethat

P[y ∈C (x˜ )]=P(cid:2) S(x˜ ,y )≤Q (cid:0) F⊤(cid:1)(cid:3)
n+1 ϵ n+1 n+1 n+1 1−α
(cid:34) (cid:32)(cid:40) (cid:41)n (cid:33)(cid:35)
≥P S(x˜ ,y )≤Q sup S(x′,y ) ∪{∞}
n+1 n+1 1−α i
x′∈Bϵ(xi)
i=1
(cid:34) (cid:32)(cid:40) (cid:41)n (cid:33)(cid:35)
≥P sup S(x′,y )≤Q sup S(x′,y ) ∪{∞}
n+1 1−α i
x′∈Bϵ(xn+1) x′∈Bϵ(xi)
i=1
≥1−α
Let P⊤ denote the distribution of (x⊤,y) where x⊤ = argsup S(x′,y) and (x,y) ∼ P.
x′∈Bϵ(x)
ThefinalinequalityaboveholdssinceitisequivalenttoconstructingaCPpredictionsetusingn
i.i.drealisationsofP⊤andevaluatingitonx ∼P⊤. Theresultingsetwillincludethetruetest
n+1
outputy withprobabilityatleast1−α.
n+1
4.3 Computationofscorebounds
Classification Intheclassificationsetting,weusethescorefunctionproposedin(Leietal.,2013;
Gendleretal.,2021):
S(x,y)=1−f(x) , (9)
y
5

<!-- Page 6 -->

wheref(x) ∈(0,1)isthemodel-predictedlikelihoodforlabely. Inthissetting,tocomputes⊥and
y
s⊤(requiredbyVRCP–IandVRCP–C,respectively),itsufficestouseNNverificationalgorithms
toderivetheoutputboundsforf(x). Specifically,inVRCP–I,foratestinputx andforeach
n+1
y ∈Y wederives⊥(x ,y)as
n+1
s⊥(x ,y)=1−f(x )⊤, (10)
n+1 n+1 y
wheref(x )⊤ denotestheupperboundcomputedbytheneuralnetworkverifierforthemodeln+1 y
predictedlikelihoodoflabely ∈Y andinputx .
n+1
InVRCP–C,foreachcalibrationpoint(x ,y )wecomputes⊤(x ,y )as
i i i i
s⊤(x ,y )=1−f(x )⊥, (11)
i i i yi
wheref(x )⊥ denotesthelowerboundofthemodeloutputforlabely giveninputx .
i yi i i
Regression Intheregressiontasks,wefollowtheconformalizedquantileregression(CQR)methodologyproposedby(Romanoetal.,2019). Wetrainquantileregressorsf andf toestimatethe
αlow αhigh
α =α/2andα =1−α/2quantilesofy |x. InCQR,weusethefollowingscorefunction:
low high
S(x,y)=max{f (x)−y,y−f (x)}. (12)
αlow αhigh
Unlikeclassification,wherethelabelspaceisdiscrete,wecannotconstructtheregionexplicitlyby
enumeratingallpossibleoutputsy. Instead,thepredictionregionforagiventestpointC(x )is
n+1
constructedimplicitly,byadjustingthequantilepredictionsbythecriticalvalueofthecalibration
distributionQ (F),asfollows:
1−α
(cid:2) (cid:3)
C(x )= f (x )−Q (F),f (x )+Q (F) (13)
n+1 αlow n+1 1−α αhigh n+1 1−α
InbothVRCP–CandVRCP–I,thescorefunctionleveragesanNNverifiertoderivetheboundsover
theupperandlowerquantilesofthemodel. InVRCP–C,wecomputetheworst-casecalibration
scoresas:
s⊤(x ,y )=max{f⊤ (x )−y ,y −f⊥ (x )}. (14)
i i αlow i i i αhigh i
InVRCP–Iforclassification,foreachoutputwecheckinclusioninC byusingthebest-casescore
ϵ
s⊥. Asexplainedabove,explicitenumerationisinfeasibleforregression,andsoweconstructour
robustregionbyreplacingpredictedquantilesinEq.(13)withtheirconservativeapproximations,as
follows:
(cid:104) (cid:105)
C (x )= f⊥ (x )−Q (F),f⊤ (x )+Q (F) (15)
ϵ n+1 αlow n+1 1−α αhigh n+1 1−α
Theabove-definedregionisequivalenttoenumeratingallpossibleoutputsy,andforeach,considering
thebest-casescores⊥(x ,y)=max{f⊥ (x )−y,y−f⊤ (x )}. Aproofisavailable
n+1 αlow n+1 αhigh n+1
inAppendixA.
AnicepropertyofbothVRCP–IandVRCP–Cisthattheyguaranteethattheycanonlyincreasethe
sizeofthepredictionsetforanyinputxcomparedtovanillaCP,thuswillalwaysattainatleastas
muchcoverageasthevanillaCPprocedure. Moreover,asweshowinSection5,bothalgorithmsdo
nottriviallyinflatethesizeofthepredictionsetsandmaintainasimilardistributionofsetsizes. This
isformalisedintheProposition1,whichisprovedinAppendixA.
Proposition1. LetC(x)andC (x)bethepredictionsetsobtainedusingvanillaCPandVRCP
ϵ
(usingVRCP–IorVRCP–C),respectively. Foranyinputx,wehavethatC(x)⊆C (x).
ϵ
5 Evaluation
WeevaluateVRCP–IandVRCP–Conclassification(image)andregression(RL)benchmarks,and
comparethemagainsttheSotAapproachesoneachbenchmark. Forallthenetworksused,wedid
notperformadversarialtrainingasweassumethattheattackbudgetϵisunknownattrainingtime.
Nonetheless,bothourapproachescanbenefitfromadversarialtraining,asitresultsinmodelsthat
aremoreverifiableandhavetighterboundsforthesameattackbudget.3
3Codefortheexperimentsisavailableat:https://github.com/ddv-lab/Verifiably_Robust_CP
6

<!-- Page 7 -->

5.1 ClassificationExperiments
Weevaluateeachmethodusinganominalcoverageof1−α=0.9andreportthe95%confidence
intervalsforcoverageandaveragesetsizescomputedover50splits(n =50)ofthecalibration,
splits
holdoutandtestset.
Bounds Weusetheverificationlibraryauto_LiRPA(Xuetal.,2020a)tocomputetheoutputbounds
for f(x) required in Eq. (10) and Eq. (11) for VRCP–I and VRCP–C respectively. In particular,
weusetwoSotAGPU-parallelisedincompleteNNverificationalgorithms,CROWNZhangetal.
(2018b)andα-CROWNXuetal.(2020b). Inbrief,CROWNperformslinearboundpropagationand
α-CROWNemploysabranch-and-boundalgorithmtotightentheCROWNboundsattheexpense
of slower verification times. Therefore, we use CROWN to compute the output bounds for the
TinyImageNetmodelandα-CROWNforthesmallerCIFAR10andCIFAR100models.
OurCIFAR10modelwithα-CROWNtakes≈ 0.5sperimagetocomputeboundswithϵ = 0.03,
whereasourlargerCIFAR100modeltakes≈ 7.2swithϵ = 0.02. Comparatively,computingthe
smoothedscorestakes≈0.09sperimagetocomputeonbothmodelsunderthesamerespectiveϵ
values. ThelargestmodelfortheTinyImageNetdatasetusesCROWNtocomputeboundsatarate
of≈0.2sperimagewhereasthesmoothedscorestake≈0.24s. Allmeasurementsaremadewith
respecttothehardwaredetailslistedinAppendixB.
Attacks WeusethePGDattackalgorithm(Madryetal.,2017),whichisapopularwhite-boxattack
algorithmtogenerateadversarialinputswithrespecttoeithertheℓ orℓ -norm.
2 ∞
Models For all datasets, we train a CNN model on training set images with random crop and
horizontalflipaugmentations. Fullmodeldetailsareoutlinedintheappendix.
Hyperparameters RSCP+ based approaches use σ = 2ϵ, β = 0.001 and those with PTT use
|D | = 500, b = 0.9 and T = 1/400. ForPGD, we choose a step size of 1/255 and compute
hold
100stepsforeachattack. ForCIFAR10andCIFAR100|D | = 50,000andforTinyImageNet
train
|D |=100,000. Foralldatasets|D |=4,500and|D |=5,000.
train cal test
Results In Table 1, we benchmark both our methods against the baseline vanilla CP (which is
agnosticoftheattack),RSCP+andRSCP+withPTT.Atinferencetime,imagesareattackedusing
PGDtogenerateℓ -normboundedattackswithϵ = 0.02forCIFAR100andTinyImageNet, and
2
ϵ=0.03forCIFAR10.
Inalldomains,thevanillaCPmethodfailstoconstructvalidpredictionsetswithnominalmarginal
coverage,asexpected. RSCP+maintainsrobustmarginalcoveragebutproducestrivialpredictionsets
inallsettingsduetothehighlyconservativeinflationofthethresholdwithrespecttothecalibration
scores. UsingPTTimprovesRSCP+’sperformancebutintroducessignificantvarianceinthesetsizes:
inmanycases,PTTstillproducestrivialpredictionsetsandisheavilydependentonthesampled
holdoutsetforRSCP+togenerateusefulpredictions.
Bothofourmethodshaveminimalsampledependence,asdemonstratedbyaverysmallvariability
incoverageandsizeoverthe50splits. Weobtainpredictionsetswithsubstantiallysmalleraverage
sizesthantheotherrobustapproaches,andhence,theyprovidemoreinformativeuncertaintyestimates. VRCP–IprovidesslightlymoreefficientregionsthanVRCP–C.Still,itimpliesadditional
computationaloverheadatinferencetimebecauseitrequirescomputingboundsviaNNverification
foreachtestsample. Incontrast,inVRCP–C,boundsarecomputedonlyonceatcalibrationtime.
Ontheotherhand,inanenvironmentwherewemaywanttochangeϵfordifferenttestpointsat
inferencetime,VRCP–Iwouldbeasoundchoice,whileVRCP–Cwouldrequirere-calibration.
Effectofincreasingadversarialnoise Fig.2bshowstheimpactofincreasingϵacrossallevaluated
robust methods. Our methods consistently produce smaller average set sizes with minor sample
dependence,andsimultaneouslyprovideamoreconservativemarginalcoveragethanRSCP+(PTT).
Weremarkthat,unlikeRSCP+,wedonotrequireaholdoutsetoranyscorefunctiontransformations.
EffectofincreasingMonte-Carlosamples Fig.2adisplaystheinfluenceofthen hyperparame-

## Mc

terontheRSCP+basedmethodswithrespecttoourCIFAR10model. Whilstincreasingsamples
7

<!-- Page 8 -->

Table1: MarginalCoverageandAverageSetSizesfordifferentmethodsonCIFAR10,CIFAR100
andTinyImageNet. Allresultsrecorda95%confidenceintervalwithn =50,α=0.1,σ =2ϵ,
splits
n =1024,ϵ=0.03forCIFAR10andϵ=0.02otherwise.

## Mc


### CIFAR10 CIFAR100 TinyImageNet


### Method Coverage Size Coverage Size Coverage Size

Vanilla 0.878±0.002 1.721±0.008 0.890±0.002 6.702±0.058 0.886±0.002 38.200±0.252
RSCP+ 1.000±0.000 10.000±0.000 1.000±0.000 100.000±0.000 1.000±0.000 200.000±0.000
RSCP+(PTT) 0.983±0.008 8.357±0.780 0.925±0.010 26.375±9.675 0.931±0.013 90.644±20.063
VRCP–I 0.986±0.000 4.451±0.011 0.971±0.001 22.530±0.107 0.958±0.001 72.486±0.311
VRCP–C 0.995±0.000 5.021±0.010 0.983±0.000 23.676±0.131 0.965±0.001 77.761±0.352
1.00
0.99
0.98
0.97
0.96
0.95
0.94
256 512 1024 2048 4096
nMC
egarevoClanigraM
10
9
8
7

## Vrcp-I 6


## Vrcp-C


## Rscp+ 5


## Rscp+(Ptt)

256 512 1024 2048 4096
nMC
eziSteSegarevA
(a)Varyingn forn =50,ϵ=0.03,α=0.1,andσ=2ϵ.
MC splits
1.00
0.98
0.96
0.94
0.92
0.90
0.01 0.02 0.03 0.04 0.05
(cid:15)
egarevoClanigraM
10
8
6

## Vrcp-I 4


## Vrcp-C


## Rscp+


## Rscp+(Ptt) 2

0.01 0.02 0.03 0.04 0.05
(cid:15)
eziSteSegarevA
(b)Varyingthevalueofϵforn =50,σ=2ϵ,α=0.1,andn =1024.
splits MC
Figure2: MarginalCoverageandAverageSetSizesonCIFAR100with95%confidenceintervals.
8

<!-- Page 9 -->

improvestheperformancesofrandomisedsmoothingapproaches,weincuralargecomputational
overheadwhencomputingthesmoothedscores. InourexperimentsinTable1wefixn =1024

## Mc

whichisfourtimeslargerthanthevalueforn usedinpreviouswork(Gendleretal.,2021;Yan

## Mc

etal.,2023)asatrade-offbetweenpredictionqualityandcomputation.
Beyondℓ -normboundedattacks Table2demon-
2
stratesthatbothofourmethodsgeneralisetootherℓ p - Table 2: Marginal Coverage and Average
boundedperturbationsotherthanforwhenp=2which Set Sizes for ϵ perturbations with respect
RSCP+islimitedto. Inparticular,weexaminetheℓ ∞ , to the ℓ ∞ -norm on the CIFAR10 dataset.
whereevenasmallϵcancausemisclassification. We Allresultsrecorda95%confidenceinterval
experimentusingCIFAR10anduseϵ = 0.001. PGD withn =50,α=0.1andϵ=0.001.
splits
isusedtogenerateℓ -boundedadversarialexamples.
∞

## Cifar10

Set size distribution From Fig. 1 we can visually

### Method Coverage Size

examinethesampledependencyissuethatthePTTintroduces. Inthesplitswheretheholdoutsetallowsthe Vanilla 0.872±0.002 1.737±0.007
PTTtomakeaninformativetransformation,RSCP+is VRCP–I 0.947±0.001 2.262±0.008
abletomakequitereasonablepredictions,otherwise, VRCP–C 0.931±0.001 2.342±0.008
RSCP+justreturnstrivialsets. Thisisclearlyanundesirablepropertyandaddssignificantvariancetothe
predictions.
Both of our methods increase the spread of the average set sizes to account for the presence of
adversarialexampleswhilststillmaintainingaconsistentdistribution.
5.2 RegressionExperiments
WeevaluateourVRCPframeworkonregressiontasksfromthePettingZooMulti-ParticleEnvironment(MPE)libraryTerryetal.(2021)fordeepreinforcementlearning. Intheseenvironments,the
worldisa2Dspacecontainingnagents(ofwhichsomemaybeadversarial)andmlandmarks,which
aredefinedascirclesoffixedradii. Thepositionofthelandmarksisfixed,andagentstraversethe
spaceaccordingtosecond-ordermotionlaws. Weevaluateourmethodonthreetasks:
• Adversary The good agents must try to reach a specific goal landmark whilst avoiding the
adversaries. Weuse2goodagents,1adversaryand2landmarks.
• SpreadAllagentscollaborateandminimisethedistancetoeachlandmark. Wesetthenumberof
agentsandlandmarksequalto3.
• PushInthistask,thereisasinglegoodagent,adversaryandlandmark.Thetaskisfortheadversary
tomaximisethedistancebetweenthelandmarkandthegoodagent.
Inourexperiments,fordata-generationweselect5,000randominitialworldconfigurationsand,for
each,simulate25Monte-Carlotrajectoriesoflengthk =5. Theregressiontaskforallenvironments
istopredicttheupperandlowerquantilesofthetotalcumulativerewardovertheksteps,givenas
inputtheinitialworldstate. Asintheclassificationexperiments,wepartitionthedatasetintothe
followingpartitions: |D |=1,000,|D |=2,000and|D |=2,000.
train cal test
Forcomputingthebounds,weuseCROWNZhangetal.(2018b)withℓ -boundedperturbations. To
∞
generatetheadversariallyperturbedtestpoints,weusetheFastGradientSignMethodasgivenin
(Goodfellowetal.,2015).
AsseeninTable3,bothVRCPmethodsrecoverthemarginalcoverageguaranteesinthepresence
of adversarial perturbations, whereas vanilla CP fails drastically after ϵ = 0.02. We note that
the performance of VRCP–C and VRCP–I are similar, although VRCP–I tends to produce more
conservativeintervals(withoutsacrificingefficiency).
6 Limitations
VRCP’sscalabilitydependsonthatoftheunderlyingneuralnetworkverifier. WeevaluatedVRCPon
smalltomedium-sizedneuralnetworks. Forlargenetworks,existingcompleteverificationmethods
9

<!-- Page 10 -->

Table3: MarginalcoverageandaverageintervallengthsforeachMPEregressiontaskforvariousϵ
perturbationsboundedbyanℓ -norm. Allresultsrecorda95%confidenceintervalwithn =50.
∞ splits

### Perturbation ϵ=0.01 ϵ=0.02 ϵ=0.04


### Method Coverage Length Coverage Length Coverage Length

yrasrevdA Vanilla 0.871±0.006 0.480±0.006 0.834±0.007 0.484±0.006 0.745±0.009 0.490±0.006

## Vrcp–I 0.928±0.004 0.605±0.006 0.951±0.003 0.673±0.006 0.985±0.002 0.855±0.006


## Vrcp–C 0.910±0.005 0.534±0.006 0.923±0.005 0.606±0.006 0.966±0.003 0.806±0.005

daerpS
Vanilla 0.864±0.005 0.595±0.005 0.834±0.005 0.602±0.005 0.768±0.006 0.612±0.005

## Vrcp–I 0.929±0.004 0.690±0.006 0.958±0.003 0.769±0.006 0.991±0.001 0.992±0.006


## Vrcp–C 0.908±0.005 0.663±0.006 0.935±0.004 0.762±0.005 0.977±0.002 1.054±0.006

hsuP
Vanilla 0.891±0.006 0.643±0.006 0.875±0.007 0.646±0.006 0.841±0.008 0.652±0.006

## Vrcp–I 0.917±0.006 0.687±0.006 0.934±0.005 0.721±0.006 0.961±0.003 0.800±0.006


## Vrcp–C 0.905±0.005 0.674±0.006 0.910±0.005 0.711±0.005 0.924±0.005 0.795±0.005

wouldbecomecomputationallyinfeasible,whileincompletemethodswouldproduceboundsthatare
tooloosetobeuseful. However,itisimportanttonotethatsinceVRCPisagnosticofthespecific
verificationtoolused,itwoulddirectlybenefitfromanyfutureadvancesinneuralnetworkverification.
Thus,asneuralnetworkverificationtoolscontinuetoevolveandimprove,sodoesVRCP.
7 Conclusion
WeintroducedVerifiablyRobustConformalPrediction(VRCP),anovelframeworkthatleverages
conformalpredictionandneuralnetworkverificationtoproducepredictionsetsthatmaintainmarginal
coverage under adversarial perturbations. We presented two variants: VRCP–C, which applies
verificationatcalibrationtime,andVRCP–I,whichappliesverificationatinferencetime.
Extensive experiments on classification and regression tasks demonstrated that VRCP recovers
validmarginalcoverageinthepresenceofℓ ,ℓ ,andℓ -normboundedadversarialattackswhile
1 2 ∞
producing more accurate prediction sets than existing methods. VRCP is the first adversarially
robustCPframeworksupportingregressiontasksandperturbationsbeyondtheℓ -norm,achieving
2
strongresultswithoutrelyingonprobabilisticsmoothingorposthoccorrections. VRCP’stheoretical
guaranteesandempiricalperformanceshowcasethepotentialofleveragingverificationtoolsfor
uncertaintyquantificationofmachinelearningmodelsunderattack.

### AcknowledgmentsandDisclosureofFunding

Thisworkissupportedbythe“REXASI-PRO”H-EUproject,callHORIZON-CL4-2021-HUMAN-
01-01,GrantagreementID:101070028.

### References

V.Vovk,A.Gammerman,andG.Shafer,Algorithmiclearninginarandomworld. Springer,2005,
vol.29.
A.N.AngelopoulosandS.Bates,“Agentleintroductiontoconformalpredictionanddistribution-free
uncertaintyquantification,”arXivpreprintarXiv:2107.07511,2021.
J.Cohen,E.Rosenfeld,andZ.Kolter,“Certifiedadversarialrobustnessviarandomizedsmoothing,”
ininternationalconferenceonmachinelearning. PMLR,2019,pp.1310–1320.
C.Szegedy,W.Zaremba,I.Sutskever,J.Bruna,D.Erhan,I.J.Goodfellow,andR.Fergus,“Intriguing
properties of neural networks,” in 2nd International Conference on Learning Representations,

## Iclr,2014.

B.BiggioandF.Roli,“Wildpatterns: Tenyearsaftertheriseofadversarialmachinelearning,”in
Proceedingsofthe2018ACMSIGSACConferenceonComputerandCommunicationsSecurity,
2018,pp.2154–2156.
10

<!-- Page 11 -->

S.Gowal,K.Dvijotham,R.Stanforthetal.,“Ontheeffectivenessofintervalboundpropagationfor
trainingverifiablyrobustmodels,”2018,arXivpreprintarXiv:1810.12715.
S.Wang,K.Pei,J.Whitehouse,J.Yang,andS.Jana,“Formalsecurityanalysisofneuralnetworks
usingsymbolicintervals,” in USENIXSecuritySymposium. USENIXAssociation, 2018, pp.
1599–1614.
H.Zhang,T.-W.Weng,P.-Y.Chen,C.-J.Hsieh,andL.Daniel,“Efficientneuralnetworkrobustness
certificationwithgeneralactivationfunctions,” inAdvancesinNeuralInformationProcessing
Systems,NuerIPS,2018.
B.Batten,M.Hosseini,andA.Lomuscio,“Tightverificationofprobabilisticrobustnessinbayesian
neuralnetworks,”inThe27thInternationalConferenceonArtificialIntelligenceandStatistics,
AISTATS,vol.238,2024.
D.M.Lopez,S.W.Choi,H.Tran,andT.T.Johnson,“NNV2.0: Theneuralnetworkverification
tool,”inComputerAidedVerification-35thInternationalConference,CAV,ser.LectureNotesin
ComputerScience,C.EneaandA.Lal,Eds.,vol.13965. Springer,2023,pp.397–412.
L.PulinaandA.Tacchella,“Anabstraction-refinementapproachtoverificationofartificialneural
networks,” in Computer Aided Verification, 22nd International Conference, CAV, ser. Lecture
NotesinComputerScience,vol.6174. Springer,2010,pp.243–257.
G.Katz,C.W.Barrett,D.L.Dill,K.Julian,andM.J.Kochenderfer,“Reluplex: AnefficientSMT
solverforverifyingdeepneuralnetworks,”inComputerAidedVerification-29thInternational
Conference, CAV, ser. Lecture Notes in Computer Science, vol. 10426. Springer, 2017, pp.
97–117.
M.HosseiniandA.Lomuscio,“Boundedandunboundedverificationofrnn-basedagentsinnondeterministicenvironments,”inInternationalConferenceonAutonomousAgentsandMultiagent
Systems,AAMAS. IFAAMAS,2023,pp.2382–2384.
A.Gendler,T.-W.Weng,L.Daniel,andY.Romano,“Adversariallyrobustconformalprediction,”in
InternationalConferenceonLearningRepresentations,2021.
J.C.Duchi,P.L.Bartlett,andM.J.Wainwright,“Randomizedsmoothingforstochasticoptimization,”
SIAMJournalonOptimization,vol.22,no.2,pp.674–701,2012.
H.Salman,J.Li,I.Razenshteyn,P.Zhang,H.Zhang,S.Bubeck,andG.Yang,“Provablyrobustdeep
learningviaadversariallytrainedsmoothedclassifiers,”Advancesinneuralinformationprocessing
systems,vol.32,2019.
G.Yan,Y.Romano,andT.-W.Weng,“Provablyrobustconformalpredictionwithimprovedefficiency,”
inTheTwelfthInternationalConferenceonLearningRepresentations,2023.
S.Ghosh,Y.Shi,T.Belkhouja,Y.Yan,J.Doppa,andB.Jones,“Probabilisticallyrobustconformal
prediction,”inUncertaintyinArtificialIntelligence. PMLR,2023,pp.681–690.
S.H.Zargarbashi,M.S.Akhondzadeh,andA.Bojchevski,“Robustyetefficientconformalprediction
sets,”in41stInternationalConferenceonMachineLearning,ICML,ser.ProceedingsofMachine
LearningResearch,vol.235. PMLR,21–27Jul2024,pp.17123–17147.
J.Lei,J.Robins,andL.Wasserman,“Distribution-freepredictionsets,”JournaloftheAmerican
StatisticalAssociation,vol.108,no.501,pp.278–287,2013.
Y.Romano,E.Patterson,andE.Candes,“Conformalizedquantileregression,”Advancesinneural
informationprocessingsystems,vol.32,2019.
K.Xu,Z.Shi,H.Zhang,Y.Wang,K.-W.Chang,M.Huang,B.Kailkhura,X.Lin,andC.-J.Hsieh,
“Automaticperturbationanalysisforscalablecertifiedrobustnessandbeyond,”AdvancesinNeural
InformationProcessingSystems,vol.33,2020.
H.Zhang,T.-W.Weng,P.-Y.Chen,C.-J.Hsieh,andL.Daniel,“Efficientneuralnetworkrobustness
certificationwithgeneralactivationfunctions,”Advancesinneuralinformationprocessingsystems,
vol.31,2018.
11

<!-- Page 12 -->

K.Xu,H.Zhang,S.Wang,Y.Wang,S.Jana,X.Lin,andC.-J.Hsieh,“Fastandcomplete: Enabling
completeneuralnetworkverificationwithrapidandmassivelyparallelincompleteverifiers,”arXiv
preprintarXiv:2011.13824,2020.
A. Madry, A. Makelov, L. Schmidt, D. Tsipras, and A. Vladu, “Towards deep learning models
resistanttoadversarialattacks,”arXivpreprintarXiv:1706.06083,2017.
J.Terry,B.Black,N.Grammel,M.Jayakumar,A.Hari,R.Sullivan,L.S.Santos,C.Dieffendahl,
C.Horsch, R.Perez-Vicenteetal., “Pettingzoo: Gymformulti-agentreinforcementlearning,”
AdvancesinNeuralInformationProcessingSystems,vol.34,pp.15032–15043,2021.
I.J.Goodfellow,J.Shlens,andC.Szegedy,“Explainingandharnessingadversarialexamples,”2015.
12

<!-- Page 13 -->


### A AdditionalProofDetails

HereweproveProposition1regardingthepredictionsetsobtainedfromVRCP–IandVRCP–C.
ProofofProposition1. ToproveC(x)⊆C (x)forVRCP–Iitsufficestoobservethat
ϵ
(cid:91)
C (x)={y ∈Y :s⊥(x,y)≤Q (F)}⊇ {y ∈Y :S(x′,y)≤Q (F)}
ϵ 1−α 1−α
x′∈Bϵ(xn+1)
(cid:91)
= C(x′)⊇C(x).
x′∈Bϵ(xn+1)
ToprovethesameforVRCP–C,weobservethatsinceQ (F⊤)≥Q (F),wehavethat
1−α 1−α
C (x)={y ∈Y :S(x,y)≤Q (F⊤)}⊇{y ∈Y :S(x,y)≤Q (F)}=C(x).
ϵ 1−α 1−α
Next,weprovethevalidityoftheVRCP–Iregionfortheregressioncase,definedinEq.(15).
Proof. It suffices to show that all y ∈ C (x ) = [f⊥ − q,f⊤ + q] satisfy s⊥(x ,y) =
ϵ n+1 n+1
max{f⊥−y,y−f⊤}≤qandally ̸∈C (x )donot.Forsimplicityofnotation,weabbreviated
ϵ n+1
f⊤ (x )withf⊤,f⊥ (x )withf⊥andQ (F)withq.
αhigh n+1 αlow n+1 1−α
Assumey ∈C (x ). Wedividetheproofintotwocases:
ϵ n+1
1. s⊥(x ,y) = f⊥ − y, which implies that y ∈ [f⊥ − q,f⊤+f⊥ ]. It suffices to show that
n+1 2
f⊥−y ≤qfory =f⊥−q,whichisclearlysatisfied.
2. s⊥(x ,y) = y − f⊤, which implies that y ∈ [f⊤+f⊥ ,f⊤ + q]. It suffices to show that
n+1 2
y−f⊤ ≤qfory =f⊤+q,whichisclearlysatisfied.
Finally, we show that y ̸∈ C (x ) implies s⊥(x ,y) > q: if y < f⊥ −q, we have that
ϵ n+1 n+1
s⊥(x ,y)=f⊥−y >q.Similarly,ify >f⊥+q,wehavethats⊥(x ,y)=y−f⊤ >q.
n+1 n+1

### B ModelDetails

AllexperimentalresultswereobtainedfromrunningthecodeprovidedinourGitHubrepositoryona
serverwith2xIntelXeonPlatinum8360Y(36cores,72threads,2.4GHz),512GBofRAMandan
NVIDIAA4048GBGPU.Allpre-trainedmodelsaswellasthetrainingscriptsarealsoprovidedin
theGitHubrepository. Insummary,themodels’trainandtestperformancesareprovidedinTables4
and5.
Table4: Trainandtestaccuracies(%)fortheclassificationsmodelsonCIFAR10,CIFAR100,and
TinyImageNetdatasets. Itshouldbenotedthatthemodel’saccuracyhasnoeffectonVRCP’svalidity
andonlyaffectstheefficiencyofthepredictionsets(moreaccuratemodels,tighterpredictionregions)
Metric CIFAR10 CIFAR100 TinyImageNet
TrainTop-5 98.77 90.49 78.44
TrainTop-1 77.80 67.12 52.81
TestTop-5 98.27 82.87 55.72
TestTop-1 76.52 55.73 29.65

### B.1 Classification

CIFAR10 Weuse2convolutionlayerswithaveragepoolinganddropout,followedby2linear
layers. ReLUactivationsacrossalllayers.
CIFAR100 Weuse1convolutionlayerwithaveragepooling,2furtherconvolutionlayerswith
averagepoolinganddropoutfollowedby2linearlayers. ReLUactivationsacrossalllayers.
13

<!-- Page 14 -->

TinyImageNet Weuse4convolutionlayerswithdropoutfollowedby2linearlayerswithdropout.

### LeakyReLUactivationfunctionwitha=0.1

Forallmodelswetrainusingimagesaugmentedwithrandomcropwith4pixelsofpaddingand
randomhorizontalflip. WestandardisetheTinyImageNetmodelswithµ=0.5andσ =0.5overall
3RGBchannels.
Aspreviouslymentioned,wedonotmakeanyassumptionsduringtrainingabouttheperturbations
weexpecttoseeatinferencetime. Assuch,unliketheexistingSotAmethods,wedonottrainon
smoothedoradversariallyattackedimages.
Allmodelsaretrainedfor200epochswithabatchsizeof128usingthestochasticgradientdescent
optimiser with momentum set to 0.9. We also employ a weight decay of 5×10−4 and a cosine
annealinglearningratescheduler.

### B.2 Regression

For the MPE datasets, we train Deep Q-Net policies for the RL tasks for the sole purposes of
generatingtheappropriatedatasetsandprovidethesepoliciesintheGitHubrepository.
The model used for the quantile regressors is a simple linear architecture consisting of 3 layers,
separatedwithReLUactivationfunctionsanddropout. Wetrainedthemodeltoestimatetheα/2and
1−α/2quantiles,whereα=0.1,asintheotherexperiments.
TheexactparametersfortheRLpoliciescanbefoundintheconfigfileswithintheGitHubrepository,
howeverhavelittlebearingontheefficiencyofourresults,beingusedonlyforthedata-generating
process.Thequantileregressorsareeachtrainedfor400epochs,withalearningrateof10−5,dropout
of0.1andadecayof10−5.
Table5:Trainandtestlossfortheregressionmodelsintheadversary,spread,andpushenvironments.
Metric Adversary Spread Push
Train 0.066 0.075 0.075
Test 0.051 0.053 0.068
14

## Tables

**Table (Page 2):**

|  |  |
|---|---|
|  |  |


**Table (Page 2):**

|  |  |
|---|---|
|  |  |


**Table (Page 2):**

|  |  |  |
|---|---|---|
|  |  |  |


**Table (Page 2):**

|  |  |
|---|---|
|  |  |


**Table (Page 2):**

|  |  |
|---|---|
|  |  |


**Table (Page 8):**

|  |  |  |  |  |  |
|---|---|---|---|---|---|
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  | VRCP- VRCP- | I C |  |  |  |
|  | RSCP+ RSCP+ | (PTT) |  |  |  |
|  |  |  |  |  |  |


**Table (Page 8):**

|  |  |  |  |  |  |
|---|---|---|---|---|---|
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |


**Table (Page 8):**

|  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  | VR VR |  |  |  |
|  |  |  |  |  | VR VR | CP-I CP-C |  |
|  |  |  |  | RS RS |  | CP+ CP+(PTT | ) |


**Table (Page 8):**

|  |  |  |  |  |  |
|---|---|---|---|---|---|
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
