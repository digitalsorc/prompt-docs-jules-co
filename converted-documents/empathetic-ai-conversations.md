---
title: "Empathetic AI Conversations"
original_file: "./Empathetic_AI_Conversations.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["llm", "rag", "fine-tuning", "evaluation", "multimodal"]
keywords: ["rtm", "mogi", "page", "outer", "torch", "model", "gnss", "bias", "mse", "blue"]
summary: "<!-- Page 1 -->

MAGIC: Modular Auto-encoder for Generalisable

### Model Inversion with Bias Corrections


### YihangShe ClementAtzberger AndrewBlake

UniversityofCambridge MantleLabs UniversityofCambridge
ys611@cam.ac.uk clement@mantle-labs.com ab@ablake.ai

### AdrianoGualandi SrinivasanKeshav

UniversityofCambridge UniversityofCambridge
ag2347@cam.ac.uk sk818@cam.ac.uk

### Abstract

Scientists often model physical processes to understand the natural world and
uncover the causation behind ob"
related_documents: []
---

# Empathetic AI Conversations

<!-- Page 1 -->

MAGIC: Modular Auto-encoder for Generalisable

### Model Inversion with Bias Corrections


### YihangShe ClementAtzberger AndrewBlake

UniversityofCambridge MantleLabs UniversityofCambridge
ys611@cam.ac.uk clement@mantle-labs.com ab@ablake.ai

### AdrianoGualandi SrinivasanKeshav

UniversityofCambridge UniversityofCambridge
ag2347@cam.ac.uk sk818@cam.ac.uk

### Abstract

Scientists often model physical processes to understand the natural world and
uncover the causation behind observations. Due to unavoidable simplification,
discrepanciesoftenarisebetweenmodelpredictionsandactualobservations,inthe
formofsystematicbiases,whoseimpactvarieswithmodelcompleteness.Classical
modelinversionmethodssuchasBayesianinferenceorregressiveneuralnetworks
tend either to overlook biases or make assumptions about their nature during
datapreprocessing,potentiallyleadingtoimplausibleresults. Inspiredbyrecent
workininversegraphics,wereplacethedecoderstageofastandardautoencoder
with a physical model followed by a bias-correction layer. This generalisable
approachsimultaneouslyinvertsthemodelandcorrectsitsbiasesinanend-to-end
mannerwithout makingstrong assumptions aboutthe natureofthe biases. We
demonstrate the effectiveness of our approach using two physical models from
disparatedomains: acomplexradiativetransfermodelfromremotesensing;and
avolcanicdeformationmodelfromgeodesy. Ourmethodmatchesorsurpasses
resultsfromclassicalapproacheswithoutrequiringbiasestobeexplicitlyfiltered
out,suggestinganeffectivepathwayforunderstandingthecausationofvarious
physical processes. The code is available on https://github.com/yihshe/
MAGIC.git.
1 Introduction
Thequantitativeandmathematicalmodelingofnaturalphenomenaisafoundationaltaskinscience.
Invertingaphysicalmodel,todeduceunderlyingcausalvariablesfromobservations,isapowerful
techniquethathasbeenusedwidely[AdlerandHolder,2021,LahozandSchneider,2014,Zhdanov,
2015]. Priorattemptsatmodelinversionhavestruggledwiththeissueofmodelincompleteness,
whereoutcomespredictedbyamodeldifferfromactualoutcomes[GroetschandGroetsch,1993,
Zhdanov,2015]. Theseapproacheseitheroverlookmodelbiasesormakeassumptionsaboutthem
duringdatapreprocessing,leadingtosignificanterrorininferredvariablevalues.
Twomajorrecentadvancesencourageustorevisitthislong-standingproblem. First,modernsensor
technologies have made available extensive data-sets of measured observations [Claverie et al.,
2018]. Second,althoughstandardstatisticalapproachesinmachinelearningmaybeunabletoyield
interpretablerepresentationsofthatdata[Chenetal.,2016],inrecentyearsauto-encodershavebeen
usedtouncoverdisentangledrepresentationsinlowdimensions[Locatelloetal.,2019]. However
these approaches lack an effective inference mechanism to obtain variables with clearly defined
physicalmeanings[Kumaretal.,2018].
Preprint.Underreview.
4202
yaM
92
]GL.sc[
1v35981.5042:viXra

<!-- Page 2 -->

Itisnotablethatresearchersingraphicshaveexploredincorporatingadifferentiablerendererintoan
auto-encodertorecoverinterpretablerepresentationsfromvisualdata[LoperandBlack,2014,Kato
andHarada,2019]. Similarapproacheshavealsobeenusedinsomespecificphysicsproblems[Lu
etal.,2020,Zérahetal.,2022]butitisunclearwhethertheseapproachescanbegeneralized. This
isbecauseauto-encodergradientsneedtobackpropagatethroughthephysicalmodelbutexisting
physicalmodelsareoftenwritteninlegacycode,andnotdesignedtobedifferentiableinthewaythat
deeplearningdemands.
Afurtherissueisthatexistingautocoder-basedapproachesrarelycompensateforsystematicbiasesin
physicalmodels. Ideally,aphysicalmodel’soutputsexhibitnosystematicbiaswhencomparedwith
measuredobservations. However,real-worldmodelsmayexhibitparticularlyprominentsystematic
biases because they only approximately represent a complex, and often noisy, physical system
[Abramowitzetal.,2007,Zhdanov,2015,Widlowskietal.,2013]. Thisrequiresbiascorrection,
withthecomplexityofthebiascorrectiondependingontheincompletenessofthephysicalmodel.
Unfortunately,theadditionofabiascorrectionlayercanmodifythecausalrelationshipbetweenthe
physicalmodel’scausalvariablesandthecorrectedoutput. Thus,thereisafinebalancebetweenthe
complexityofbiascorrectionandinterpretabilityofthecausalvariablesextractedbyinversionofthe
biascorrectedmodel.
Toaddresstheseissues,wefirstdemonstratehowtoaugmentadeterministicphysicalmodelwith
abiascorrectionlayerthatlearnsatransformationfrommodeloutputtoobservedoutcomes. This
greatlyincreasesmodelpredictionaccuracy. Second,weuseanautoencoder-likenetworktoinvert
thisaugmentedmodeltoextractcausalvariablesfromobservations. Wedothisintwodisparate
physicalsciencedomains: aradiativetransfermodel(RTM)[Atzberger,2000]thatcomputesspectral
signaturesfrombiophysicalvariablesandisnotinherentlydifferentiable;andavolcanicdeformation
model [Mogi, 1958] that computes surface deformations due to magma chamber activity. We
demonstratethegeneralisabilityofourapproachbymakingthecomplexRTMfullydifferentiableand
stableduringtraining,usingthepowerofLargeLanguageModels(LLMs),anapproachthatcould
beappliedmoregenerallytoinvertinglegacyimplementationsofcomplexphysicalmodels. Finally,
weusetwophysicalmodelswithdifferentlevelsofcompletenesstoinvestigatethecomplexityofthe
correspondingbiascorrection.
Bydetailedcomparisonoflearningoutcomesagainstbaselinesderivedfromclassicalmethods,we
demonstrate that auto-encoders can be used as a generalizable approach for simultaneous model
inversionandbiascorrection. Thissuggestsapathwayforamoreaccurateunderstandingofthe
causationofdiversephysicalprocesses,bymeansofend-to-endlearning.
2 RelatedWork
2.1 Disentangledrepresentationlearning
Akeyaspectofourapproachisoninterpretabilityanddisentanglement. Thisrelatestotheconcept
ofdisentangledrepresentationlearning,whichseekstouncoverlower-dimensional,semantically
meaningfulfactorsofvariationfromhigh-dimensionaldata[Locatelloetal.,2019]. Intheparadigm
ofunsupervisedlearningofdisentangledrepresentations,VariationalAutoencoders(VAEs)[Kingma
andWelling,2013]andtheirvariants,suchasβ-VAE[Higginsetal.,2017],arebasedonprobabilistic
modeling. Theseapproachesallowdisentangledvariablestoemergefromlearning[Kumaretal.,
2018]. Alternatively,GenerativeAdversarialNetworks(GANs)[Goodfellowetal.,2014]havealso
demonstratedsuccessinlearninginterpretableanddisentangledrepresentationsforimagesynthesis,
asseeninInfoGAN[Chenetal.,2016]andStyleGAN[Karrasetal.,2019]. However,asgenerative
models, the disentangled variables typically emerge only during learning and lack an effective
inferencemechanism[Kumaretal.,2018]. Moreover,asLocatelloetal.[2019]suggested,inductive
biasesareessentialforunsupervisedapproachestolearningdisentangledrepresentations.Forphysical
models, the situation is simplified because the forward model is deterministic and benefits from
havingapredeterminedsetofinterpretablevariables,namelythephysicalinputparameterstothe
model.
2

<!-- Page 3 -->

2.2 Inverseproblemsinphysicalsciences
Across various domains in natural sciences, forward numerical models are developed based on
physicalprinciplesandinvertingthemhasledtosignificantapplicationse.g. electricalimpedance
tomographyinhealthcare[AdlerandHolder,2021],dataassimilationinclimatescience[Lahozand
Schneider,2014],andunderstandingtheEarth’sstructureingeophysics[Zhdanov,2015]. Wetestour
approachontwodomains(seesection3.2). First,RadiativeTransferModels(RTMs)fromremote
sensing[Suits,1971,Atzberger,2000]belongtoafamilyofcanopyreflectancemodelsthatsimulate
spectralbidirectionalforestreflectance,giveninputsofimportantforestcharacteristics[Widlowski
etal., 2013,Liand Strahler,1985,Suits, 1971,Atzberger, 2000]. Second, volcanicdeformation
modelsfromgeodesysimulatesurfacedeformationduetomagmachamberactivity[Segall,2013,
Mogi,1958]andcomefromabroaderfamilyofgeophysicalmodelswhereinversionisakeyproblem
[Zhdanov,2015]. ClassicalinversionapproachesincludeBayesianinference,numericaloptimization,
andlook-uptables[GroetschandGroetsch,1993,Goel,1988,Combaletal.,2003]. Morerecently,
neuralnetworkregressorshavealsobeenused[Gong,1999,SchlerfandAtzberger,2006,Mousavi
etal.,2024].
2.3 Autoencoderasanapproachtoinversion
Wedonotclaimoriginalitysimplyforusingauto-encoderstoinvertphysicalmodels;thathasbeen
extensivelyinvestigatedincomputerscience,especiallyininversegraphics[Katoetal.,2020]. A
seminalcontributionisOpenDR[LoperandBlack,2014],whichproposesdifferentiablerendering
to invert a graphics renderer by learning with backpropagation. Since then, auto-encoders have
beenapopularchoicetoincorporateadifferentiablerendererintoself-supervisedlearningpipelines
[Katoetal.,2020],andhavebeenappliedto3Dreconstruction,andhumanposeestimationfrom
single-viewimages[KatoandHarada,2019,Pavlakosetal.,2018]. Thisapproachhasbeenapplied
to a few scientific domains [Lu et al., 2020, Zérah et al., 2022], and recently, specifically for a
canopy-reflectancemodel[Zérahetal.,2023]. Howevernoneofthesestudiesaddressessystematic
bias,andthatiswhatisespeciallydistinctiveaboutourapproach.
3 Methods
3.1 Learningtheinverseofphysicalmodels
ToinferphysicalvariablesZ frommeasuredobservationsX,weuseanauto-encoderarchitecture
withbiascorrectiontotrainanencoderthatmapsmeasuredobservationstophysicalvariables(Fig.1).
ThephysicalprocessthatgeneratestheobservationsX iswritten:

### X =F(Z)+B(Q)+η (1)

whereFisthemodelledprocessactingonphysicalvariablesZ;B(Q)isthesystematicbiasbetween
F(Z)andX resultingfromunmodeledprocessesB,anddependingonacollectionofothervariables
Q;andηrepresentsrandomnoise.
Aclassicalauto-encoderM consistsofanencoderE andadecoderD (eq.(2)).

## A A A


## X =D (E (X)) (2)


## A A A

Given a sufficiently sophisticated network architecture, M can minimize Mean Squared Error

## A

L (θ )betweenXandX ,butthelatentcodesZ computedasE (X)neednotbesemantically

## Mse Ea A A A

interpretableintermsofwelldefinedphysicalproperties. ReplacingD ineq.(2)withthephysical

## A

modelFhoweverensuresthatanencoderE embedsX asinterpretablephysicalvariablesZ =

## B B

E (X),whicharethenpassedtoFtoreconstructobservations(autoencoderM ):

## B B


## X =F(E (X)) (3)


## B B

Ideally,whenFisperfectlybuilttoaccountfullyforthephysicalprocesses,thereisnoneedfor
B(Q)ineq.(1). Inthatcase,L (θ )shouldbeonaparwithL (θ ). Inrealitytherigidity

## Mse Eb Mse Ea

andoversimplificationofFgivesappreciablereconstructionmismatchbetweenX andX soweadd

## B

additionalnon-linearbias-correctionlayersCafterF(autoencoderM ,alsoseeFig.1):

## C


## X =C(F(E (X))). (4)


## C C

3

<!-- Page 4 -->

ThecorrectionlayerCincreasestheflexibilityofFanddecreasesL (θ ,θ )toimprovethe

## Mse Ec C

learning outcome of Z . The risk, though, is that input variables Z are no longer anchored as

## C C

strongly,especiallyifwithappreciableflexibilityinC,allowingZ toentangleanddriftawayfrom

## C

physicalinterpretations. AsolutionistolimitthecomplexityofCtotwolineartransformationswith
asingleReLUactivationσbetweenthem:
X =W σ(W F(E (X))+b )+b . (5)

## C 2 1 C 1 2

Here,W expandstheinputtofourtimesitsoriginaldimension,andW reducesitbacktoitsoriginal
1 2
size. Thisdesignmirrorsthefeed-forwardheadinTransformers[Vaswanietal.,2017],whichhas
allowedjustenoughflexibilityinnon-lineartransformations—exactlywhatweneed(seesection4).
Figure1: Learningtheinverse,end-to-end,inanautoencoderthatincludescorrectionlayersC.
3.2 Physicalmodelsforinversion
INFORM:TheINFORMradiativetransfermodelfromremotesensing(denotedbyF ),developed

## Rtm

byAtzberger[2000],consistsofasetofsub-modelsdesignedtosimulatethereflectanceofforest
canopiesgivenparametersrepresentingtheirbiophysicalandgeometricproperties. Despitedecades
ofresearch,thecomplexityofforeststructuresleadstodiscrepanciesbetweensimulatedandmeasured
spectra. Thesebiasesstemfromover-simplificationofthephysicsandsignificantlyaffectaccuracyof
inferredvariableswithclassicalapproaches[Widlowskietal.,2013]. Weaimtoestimatecertainset
ofthebiophysicalvariables,whoseplausiblerangesareknown(Tab.1),whilefixingothervariables
at typical values for the study area (see Appendix A.3). In practice, F is implemented with

## Rtm

NumPyandcomprisesapproximately1700linesofcode,andisnotexplicitlydifferentiable.
Mogi: TheMogimodel(denotedbyF )isamodelusedingeodesytodescribethedisplacement

### Mogi

fieldatthesurfaceoftheEarthresultingfromasphericalpressuresource,typicallyamagmachamber,
atdepth[Mogi,1958]. TheinverseproblemforF involvesestimatingthelocationandvolume

### Mogi

changeofmagmachamberactivityfromobservedsurfacedisplacements(Tab.2andAppendixA.5).
Compared with F , F is built on simple assumptions, with the complexity of the Earth’s

### RTM Mogi

crustbeingcrudelyapproximatedbyanelastichalf-space. Despiteitssimplicity,theMogimodelis
abletocapturethefirst-orderpatternsofsurfacedeformationassociatedwithvolcanicsources. The
challengeisthat,thevolcanicdeformationcanbesmallifcomparedtoothersourcesofdeformation
(e.g. hydrologicalloading),posingchallengestothebiascorrection(seeAppendixA.6.2).
Table1: BiophysicalvariablesofF tolearn. BoundrangesofZ andZ aremarkedwith

### RTM h cd

*,astheywillbeinferredfromZ andfixedstemdensityusingallometricequations[Juckeretal.,
fc
2017]tomitigatetheill-posednatureoftheinverseproblem(seeAppendixA.3).

### Sub-model LeafModel CanopyModel ForestModel

Structure Chlorophyll Water Dry LeafArea Undergrowth Fractional Tree Crown

### Variable

Parameter A+B Content Matter Index LAI Coverage Height Diameter

### Acronym N cab cw cm LAI LAIu fc h cd

Min 1 10 0.001 0.005 0.01 0.01 0.1 * *
Max 3 80 0.02 0.05 5 1 1 * *
4

<!-- Page 5 -->

Table2: GeophysicalvariablesofF tolearn. Thesourcecenter(x ,y )isassumedtolie

### Mogi m m

withintheGNSSstations’boundaries(section3.4),withdepthandvolumerangesmatchingthose
usedin[Walweretal.,2016].
Variable Epicenter-X(km) Epicenter-Y(km) Depth(km) VolumeChange(106m3)
Acronym x y d ∆V
m m
Min -9.33 -5.80 2 -10

### Max 14.35 7.62 20 10

3.3 End-to-endlearningwithphysicalmodels
Differentiabilityisrequiredforauto-encoderworkflowandtheimplementationofF inPyTorch

### Mogi

isstraightforwardasitonlyinvolvesafewlinesofequations(AppendixA.5). TheRTMF is

## Rtm

complexandallitsNumPyoperationsneedconversiontoPyTorch,identifyingfunctionsthatarenot
differentiable,andconstructingbackwardfunctionforeachtoobtainapproximatedderivatives.
RecentdevelopmentsinLLMswouldsuggestusingGPT-4[OpenAI,2023]sothatcommonoperationsgetautomaticallyconvertedtoPyTorch,andothersareflaggedforcustomtreatment. Inthisway,
weconverted1,742linesofcodeinlessthanaweek(seeAppendixA.1).Inpractice,canopy-radiation
interactionneedsexponential,logarithm,andsquarerootfunctionswhichcanleadtonumerically
unstablederivatives. Thisishandledbybypassinginstabilitypointsduringbackpropagation(see
AppendixA.2).
3.4 Datasets
ThedatasetforF consistsof17692individualspectraX ={x ,i=1,...,11},extracted

### RTM S2 S2,i

from1283individualsitesacrossAustriaobservedbySentinel-2[Druschetal.,2012]. SpectraX

## S2

formatemporalsequencecoveringApriltoOctober2018—bothconiferousanddeciduousforests
—consistingof12species. Spectracomprise11bands(seeAppendixA.4).
ForF ,thedatasetcomesfrom12GlobalNavigationSatelliteSystem(GNSS)stationsaroundthe

### Mogi

AkutanVolcano,oneofthemostactivevolcanoesintheAleutianIslands(Alaska,USA).Everyday,
eachGNSSstationrecordsitspositionatthesurfaceineast,northandverticaldirections(denoted
X ={x ,x ,x ,i=1,...,12}). Intotal,wehaveobservationsfrom6525consecutivedays

### GNSS e,i n,i v,i

from2006untilearly2024(http://geodesy.unr.edu,[Blewittetal.,2018])(seeAppendixA.6).
Forbothproblems,collectinggroundtruthdataislargelyimpractical. Theinterpretationofresults
hastorelyonplausibilitychecksonvariabledistributionsandtemporalevolutionpatterns. ForF ,

## Rtm

weusepriorknowledgeoftreespeciesandtemporaldatatovalidatebiophysicalestimates. ForF ,

### Mogi

geophysicalestimatesofamagmasourceandreconstructedtransientGNSSsignalsarevalidated
againstexistingliterature[JiandHerring,2011,Walweretal.,2016].
3.5 Baseline
InadditiontocomparingM ,M ,andM ,wehavealsocomparedwithclassicalapproachbaselines.

## A B C

FurtherimplementationdetailscanbefoundinAppendixA.8.
ForF ,wetrainedaneuralnetworkregressorM usingsampledvariablesandspectrafrom

## Rtm D,Rtm

F —aclassicalapproachforinversion[Gong,1999]asabaseline. ModelM sharesthe

## Rtm D,Rtm

samearchitectureastheencoderofM . Itisfirsttrainedtoregressthesampledvariablesfrom

## C,Rtm

thesyntheticspectraandthenappliedtotherealspectraX topredictphysicalvariables(Z ).

## S2 D,Rtm

ToobtainthespectralreconstructionX ,Z ispassedtoF .

## D,Rtm D,Rtm Rtm

For F , we compared our inversion results with classical results [Walwer et al., 2016] which

### Mogi

preprocessedtheGNSStimeseriesover2006-2014asfollows. FirsttheyusedSingularSpectrum
Analysistodetectlikelytransientsignalsbyinspectingtheprocessedtimeseriesacrossstationsand
directions. Then,theyperformedagridsearchofparameterstoinvertF byfittingitsestimatesto

### Mogi

theextractedtransientsignals. TheyfixedthelocationoftheMogisourceandestimatedthedepth
andvolumechangeforperiodslikelyduetomagmamovement. Notablytheydetectedsignificant
5

<!-- Page 6 -->

volcanicinflationofAkutaninearly2008,alsoreportedbyJiandHerring[2011].Thusforvalidation,
wehavesavedtheGNSStimeseriesfrom2006to2009asatestsettocoverthe2008event.
4 Results
4.1 Effectsofbiascorrection
The systematic bias of F is evident comparing the input spectra X with the reconstruction

## Rtm S2

X fromM trainedwithoutbiascorrection(Fig.2a). Furtherillustrationsofbiascorrections

## S2,B B,Rtm

aredetailedinAppendixA.9.
Similarly F shows systematic bias comparing X with the reconstruction from M

### Mogi GNSS B,Mogi

(Fig.2b). BiascorrectionusingM achievessomeimprovementinreconstructionofGNSS

### C,Mogi

signals(Tab.4)thoughlessdramaticallythanM ,asindicatedbytheR2values(Figs.2aand2b).

## C,Rtm

TheRTMisamorecomplexmodel,presentinggreaterchallengesininversion,butimposesastrong
priorandcapturesphysicalprocesseseffectively. Incontrast,F makessimplerassumptions—

### Mogi

consideringonlyapoint-likepressuresourceforsurfacedeformation—formingalessinformative
bottleneckinthedecoderandsoposesagreaterchallengeforbiascorrection. Howeverourcorrection
layer is still able to capture most of the systematic bias and improves the learned inverse. Bias
Table3: RTM:Thereconstructionlossofmodelsunderdifferentstepsoftheinversion. L

## Mse

underM iscomparabletotheclassicalauto-encoderM ,andisreducedbymorethan

## C,Rtm A,Rtm

anorderofmagnitudecomparedtotheregressorbaselineM .

## D,Rtm


### Model Ablation L L L


### MSE,train MSE,val MSE,test

M w/oF ,w/oC 0.0193 0.0219 0.0191

## A,Rtm Rtm Rtm

M w/F ,w/oC 0.0875 0.0833 0.0856

## B,Rtm Rtm Rtm

M w/F ,w/C 0.0210 0.0235 0.0217

## C,Rtm Rtm Rtm


## M N/A - - 0.6676


## D,Rtm

Table4: Mogi: Thereconstructionlossunderdifferentsteps. L forM outperforms

### MSE C,Mogi

M andmatchesM ,butthebiascorrectionislesspronouncedcomparedtotheRTM

### B,Mogi D,Mogi

model—amorecompletemodelwithlesscomplexbiasestoaddress(seeFig.2).

### Model Ablation L L L


### MSE,train MSE,val MSE,test

M w/oF ,w/oC 0.4389 0.9119 0.6324

### A,Mogi Mogi Mogi

M w/F ,w/oC 0.6998 0.9721 0.8095

### B,Mogi Mogi Mogi

M w/F ,w/C 0.4803 0.9338 0.7110

### C,Mogi Mogi Mogi

correctionalsoenhancesthelearningofvariablesinlatentspaceforF andforF —compare

### RTM Mogi

retrievedvariableswithandwithoutabiascorrection(Fig.3)—forF thedistributionsofseveral

## Rtm

variablesaredistortedtoextremesifbiasisnotcorrected(Fig.3a).
SimilarlyforF biaspushesthecenteroftheMogisourcetoextremes(Fig.3b)ifnotcorrected,

### Mogi

andalthoughZ andZ followunimodalorbimodaldistributions,theyhaveimplausiblevalue
d ∆V
rangeswithoutbiascorrection. BothJiandHerring[2011]andWalweretal.[2016]havesuggested
that the depth Z less than 10 km and the volume change Z range rarely exceed −5·106 m3
d ∆V
to5·106 m3 fortheevaluatedperiodattheAkutanvolcano[Walweretal.,2016]. Indeed,ifZ
d
exceeds 10 km, then the volume change required to reproduce the observed displacement would
beunreasonablylarge. Itispossiblethat,withoutbiascorrection,themodelattemptstoreplicate
acommonmodesignalputtingthesourceatgreaterdepthandthusgeneratingalargewavelength
signalatthesurface.
4.2 Evaluationofphysicalvariables
WeclusteredRTMvariablesbyforesttype. Coniferousanddeciduousforestshavedistinctdistributionsandtheco-distributionofvariablesZ appearspositivelycorrelatedwithZ ,andnegatively
LAI cw
6

<!-- Page 7 -->

(a)RTM:Reconstructionaccuracyillustratedfor2ofthespectralbands.
(b)Mogi:Reconstructionaccuracyofverticaldisplacementsillustratedfor2oftheGNSSstations.
Figure2: Reconstructionaccuracywithoutbiascorrectionmoduledisplaysclearbias. Blue:
M . Red: M . Afterbiascorrection,reconstructionforMogiisnotaslinearasforRTM,likelydue

## C B

toitssimplicitywhichactsasaninformationbottleneckinthedecoder,highlightingthetrade-off
betweenmodelsimplicityandbiascorrectioncomplexity.
(a)Distributionsofvariables:Z vs.Z

## B,Rtm C,Rtm

(b)Distributionsofvariables:Z vs.Z

### B,Mogi C,Mogi

Figure3: Biascorrectiontighteneddistributionsofvariables. Withoutbiascorrection,variable
distributions(red)areimplausible,breakingoutfrompresetboundedranges. Withbiascorrection
(blue)learneddistributionsaremorealignedwiththephysicalsense.
(a)Co-distributions:Z (b)Co-distributions:Z

## D,Rtm C,Rtm

Figure4: Pairwiseco-distributionsofvariablesillustratedforZ . Red: coniferousforest. Blue:

## Lai

deciduousforest. Ourmodelcanlearndistinctphysicalpatterns.
7

<!-- Page 8 -->

with Z under M (Fig. 4b). Without bias correction no correlation patterns are visible

### LAIu C,RTM

(Fig. 4a). This makes sense: higher leaf area at the canopy level (Z ) indicates plant growth

## Lai

andhencehigherwatercontent(Z )andchlorophyllcontent(Z )butreduceslightpenetration,
cw cab
reducingplantgrowthintheunderstory,hencelowerZ . Furtherillustrationsofphysicalvariables

### LAIu

aredetailedinAppendixA.10.
Figure 5: Temporal variations of inferred physical parameters Z illustrated for Z ,

## C,Rtm Lai

Z ,andZ . M effectivelycapturesdistinct,temporallysmooth,andplausiblevariations

### LAIu fc C,RTM

fordifferentforesttypes,whilethosefromM appeartobelesssmooth(seeAppendixA.10.1).

## D,Rtm

Temporalvariationexhibitsmoreconsistentandclearerpatternsforsomevariables(Fig.5). Understoryplantgrowth(Z )declinesfromAprilduetoreducedlightpenetrationfromincreased

### LAIu

canopygrowth(Z ). Coniferousforestsexhibitdifferentpatternsthandeciduousones,withhigher

## Lai

fractionalcoverage(Z )andlessvariationovertime,aswouldbeexpected. Temporalvariations
fc
learnedbytheM appearlessconsistent(seeAppendixA.10.1).

## D,Rtm

The 7 inferred variables are clustered by species and Jeffereys-Matusita (JM) distance, varying
between0and2,iscalculatedtoassessseparabilityofthe12species. AsshowninFig.6,ourmodel
achievesclearseparationbetweendifferentforesttypes(deciduousvs. coniferous),andimproved
separabilitywithinforesttype,suggestingadegreeofdisentanglementofinferredvariables. Note
thattheconiferousspecies‘LarixDecidua’(EuropeanLarch)appearsclosetothedeciduousgroup,
butactuallythatmakessenseasitisoneofthefewconifersthatshedsitsneedlesinthefall.
(a)JMdistancebasedonZ (b)JMdistancebasedonZ

## D,Rtm C,Rtm

Figure6:PairwiseJeffreys-Matusita(JM)distancebetweenspeciesbasedonthelearnedvariables.
Red: coniferousspecies. Blue: deciduousspecies. Speciesdistributionsfromdifferentforestgroups
becomemoredisentangledafterbiascorrection.
FortheMogimodel,classicalsignalprocessingofthetimeseriesandMogiinversionsfor2006–2009
show a transient deformation event due to the inflation of a magma source in early 2008 [Ji and
Herring, 2011, Walwer et al., 2016]. It lasts about half a year and is characterized by the uplift
andradialextensionofthesurfacearoundtheMogisource. Thisisconsistentwiththetemporal
variation of Z learned by our model. The magnitude of Z and the estimated values of Z
∆V ∆V d
(rangingfrom6to9km)andtheepicenter(locatedroughlybeneathAkutanvolcano),whichremain
relativelyconstantovertime,alignwithpreviousestimatesWalweretal.[2016]whichestimated
MogiparametersusinggridsearchtofitthemodeltotheprocessedGNSSsignals.
8

<!-- Page 9 -->

Examining two GNSS stations, AV08 and AV12, located on opposite sides of the volcano, we
comparetheirGNSSdisplacementsasreconstructedbyF undertheM model. Themodel

### Mogi C,Mogi

successfullyreconstructsthetransientsignalsofthe2008inflationandthesubsequentslowdeflation,
characterisedbyspecificdirectionalmovements,withconsistencyacrossstationsanddirectionsthat
alignwithJiandHerring[2011]andWalweretal.[2016]. Notethatclassicalmethods[Walweretal.,
2016]requiredtheGNSSsignalstobefilteredforassumedbiases,andtransientsignalsidentifiedby
comparingprocessedsignalsacrossGNSSstations,followedbygridsearchtoinverttheMogimodel.
Incontrast,ourauto-encoderapproachallowsM tocapturetransientsignals,estimateMogi

## C,Rtm

parameters,andcorrectbiasesinasinglestagewithoutrelyingonadditionaldatafilteringorstrong
biasassumptions. Furthermore,thisinferenceisachievedthroughasingleforwardpassofM ,

## C,Rtm

whichistrainedondatasetswithnooverlapwiththetestperiod.
Figure7: Timeseriesofinferredphysicalparameters. TheredcurveisfittedbyaKalmanfilter
toindicatethetemporalvariationsmoreclearly. ThevolumechangeZ successfullycaptureda

## ∆V

majorvolcanicinflationeventin2008,reachingapeakofapproximately5·106m3atadepthofjust
lessthan10km,consistentwithpreviousfindings[Walweretal.,2016].
Figure8: TimeseriesofGNSSdisplacementsillustratedfortwoGNSSstations, locatedatthe
oppositesideoftheMogisource. Orange: X . Blue: MogireconstructionsusingZ . Red:

### GNSS C,Mogi

MogireconstructionsfittedbyaKalmanfilter. Ourmodelsuccessfullyreconstructsthe2008volcanic
inflationtransientsignals,characterizedbyradialexpansionandverticaluplift,withdisplacement
magnitudesof10mm,alignedwithpriorfindings[JiandHerring,2011,Walweretal.,2016].
5 ConclusionandLimitations
Wehavedevelopedanend-to-endapproachtolearntheinverseofdeterministicphysicalmodels
whilecorrectingforbiases. Wedemonstratedthegeneralisabilityofourapproachbyapplyingitto
physicalmodelsfromverydifferentdomains,eachwithdistinctcomplexities,differentiabilityissues,
anddatadynamics. Extensiveanalysisshowsthatourapproachhasimprovedreconstructionlossand
stronglysuggeststheplausibilityoftherecoveredphysicalvariables.
9

<!-- Page 10 -->

Ourworksuffersfromsomelimitations. First, ourapproachdoesnotextendtophysicalmodels
withstochasticoutcomes,wherethesameinputscanleadtodifferentoutputs,amuchmorecomplex
inversionproblem. Second,wehaveonlystudiedtworepresentativephysicalmodels. However,we
anticipatethatourapproachcanbeappliedtomodelsinotherphysicaldomains. Finally,weusethe
samebiascorrectionindependentofthephysicalmodel. Whilewefoundthistobeeffective,given
thetrade-offbetweenmodelcompletenessandcomplexitynecessaryforbiascorrection,futurework
coulduseneuralarchitecturesearch[Renetal.,2021]toidentifytheoptimalbiascorrectionlayerfor
aspecificinverseproblem.
Acknowledgement: ThisworkwassupportedbytheUKRICentreforDoctoralTraininginApplicationofArtificialIntelligencetothestudyofEnvironmentalRisks(referenceEP/S022961/1)and
CambridgeCentreforCarbonCredits. WewouldalsoliketothankMarkusImmitzerfromMantle
LabsforsharingtheSentinel-2datawithus.
10

<!-- Page 11 -->


### References

AndyAdlerandDavidHolder. Electricalimpedancetomography: methods,historyandapplications.
CRCPress,2021.
William A Lahoz and Philipp Schneider. Data assimilation: making sense of earth observation.
FrontiersinEnvironmentalScience,2:16,2014.
MichaelSZhdanov. Inversetheoryandapplicationsingeophysics,volume36. Elsevier,2015.
CharlesWGroetschandCWGroetsch. Inverseproblemsinthemathematicalsciences,volume52.
Springer,1993.
MartinClaverie,JunchangJu,JeffreyGMasek,JenniferLDungan,EricFVermote,Jean-Claude
Roger,SergiiVSkakun,andChristopherJustice. Theharmonizedlandsatandsentinel-2surface
reflectancedataset. Remotesensingofenvironment,219:145–161,2018.
Xi Chen, Yan Duan, Rein Houthooft, John Schulman, Ilya Sutskever, and Pieter Abbeel. Infogan: Interpretablerepresentationlearningbyinformationmaximizinggenerativeadversarialnets.
Advancesinneuralinformationprocessingsystems,29,2016.
FrancescoLocatello,StefanBauer,MarioLucic,GunnarRätsch,SylvainGelly,BernhardSchölkopf,
andOlivierBachem. Challengingcommonassumptionsintheunsupervisedlearningofdisentangledrepresentations,2019.
AbhishekKumar,PrasannaSattigeri,andAvinashBalakrishnan.Variationalinferenceofdisentangled
latentconceptsfromunlabeledobservations,2018.
Matthew M Loper and Michael J Black. Opendr: An approximate differentiable renderer. In
ComputerVision–ECCV2014: 13thEuropeanConference,Zurich,Switzerland,September6-12,
2014,Proceedings,PartVII13,pages154–169.Springer,2014.
Hiroharu Kato and Tatsuya Harada. Learning view priors for single-view 3d reconstruction. In
Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, pages
9778–9787,2019.
PeterYLu,SamuelKim,andMarinSoljacˇic´. Extractinginterpretablephysicalparametersfrom
spatiotemporalsystemsusingunsupervisedlearning. PhysicalReviewX,10(3):031056,2020.
YoëlZérah,SilviaValero,andJordiInglada. Physics-guidedinterpretableprobabilisticrepresentation
learningforhighresolutionimagetimeseries. IEEETransactionsonGeoscienceandRemote
Sensing,2022.
GabAbramowitz,AndyPitman,HoshinGupta,EvaKowalczyk,andYingpingWang. Systematic
biasinlandsurfacemodels. JournalofHydrometeorology,8(5):989–1001,2007.
J-LWidlowski,BPinty,MLopatka,CAtzberger,DBuzica,MichaëlChelle,MDisney,J-PGastellu-
Etchegorry,MGerboles,NGobron,etal. Thefourthradiationtransfermodelintercomparison
(rami-iv):Proficiencytestingofcanopyreflectancemodelswithiso-13528. JournalofGeophysical
Research: Atmospheres,118(13):6869–6890,2013.
ClementAtzberger. Developmentofaninvertibleforestreflectancemodel: Theinfor-model. InA
decadeoftrans-europeanremotesensingcooperation.Proceedingsofthe20thEARSeLSymposium
Dresden,Germany,volume14,pages39–44,2000.
Kiyoo Mogi. Relations between the eruptions of various volcanoes and the deformations of the
groundsurfacesaroundthem. EarthqResInst,36:99–134,1958.
Diederik P Kingma and Max Welling. Auto-encoding variational bayes. arXiv preprint
arXiv:1312.6114,2013.
Irina Higgins, Loic Matthey, Arka Pal, Christopher Burgess, Xavier Glorot, Matthew Botvinick,
Shakir Mohamed, and Alexander Lerchner. beta-vae: Learning basic visual concepts with a
constrainedvariationalframework. InInternationalconferenceonlearningrepresentations,2017.
11

<!-- Page 12 -->

IanGoodfellow,JeanPouget-Abadie,MehdiMirza,BingXu,DavidWarde-Farley,SherjilOzair,
AaronCourville,andYoshuaBengio. Generativeadversarialnets. Advancesinneuralinformation
processingsystems,27,2014.
Tero Karras, Samuli Laine, and Timo Aila. A style-based generator architecture for generative
adversarialnetworks. InProceedingsoftheIEEE/CVFconferenceoncomputervisionandpattern
recognition,pages4401–4410,2019.
GwynnHSuits. Thecalculationofthedirectionalreflectanceofavegetativecanopy. RemoteSensing
ofEnvironment,2:117–125,1971.
Xiaowen Li and Alan H Strahler. Geometric-optical modeling of a conifer forest canopy. IEEE
TransactionsonGeoscienceandRemoteSensing,(5):705–721,1985.
PaulSegall. Volcanodeformationanderuptionforecasting. GeologicalSociety,London,Special
Publications,380(1):85–106,2013.
NarendraSGoel. Modelsofvegetationcanopyreflectanceandtheiruseinestimationofbiophysical
parametersfromreflectancedata. Remotesensingreviews,4(1):1–212,1988.
BCombal,FrédéricBaret,MWeiss,AlainTrubuil,DMace,APragnere,RMyneni,YKnyazikhin,
andLWang. Retrievalofcanopybiophysicalvariablesfrombidirectionalreflectance: Usingprior
informationtosolvetheill-posedinverseproblem. Remotesensingofenvironment,84(1):1–15,
2003.
P Gong. Inverting a canopy reflectance model using a neural network. International Journal of
RemoteSensing,20(1):111–122,1999.
MartinSchlerfandClementAtzberger. Inversionofaforestreflectancemodeltoestimatestructural
canopyvariablesfromhyperspectralremotesensingdata. Remotesensingofenvironment,100(3):
281–294,2006.
SMostafaMousavi, GregoryCBeroza, TapanMukerji, andMajidRasht-Behesht. Applications
of deep neural networks in exploration seismology: A technical survey. Geophysics, 89(1):

## Wa95–Wa115,2024.

Hiroharu Kato, Deniz Beker, Mihai Morariu, Takahiro Ando, Toru Matsuoka, Wadim Kehl, and
AdrienGaidon. Differentiablerendering: Asurvey. arXivpreprintarXiv:2006.12057,2020.
Georgios Pavlakos, Luyang Zhu, Xiaowei Zhou, and Kostas Daniilidis. Learning to estimate 3d
human pose and shape from a single color image. In Proceedings of the IEEE conference on
computervisionandpatternrecognition,pages459–468,2018.
Yoël Zérah, Silvia Valero, and Jordi Inglada. Physics-constrained deep learning for biophysical
parameterretrievalfromsentinel-2images: inversionoftheprosailmodel. AvailableatSSRN
4671923,2023.
AshishVaswani,NoamShazeer,NikiParmar,JakobUszkoreit,LlionJones,AidanNGomez,Łukasz
Kaiser,andIlliaPolosukhin. Attentionisallyouneed. Advancesinneuralinformationprocessing
systems,30,2017.
TommasoJucker, JohnCaspersen, JérômeChave, CécileAntin, NicolasBarbier, FransBongers,
Michele Dalponte, Karin Y van Ewijk, David I Forrester, Matthias Haeni, et al. Allometric
equations for integrating remote sensing imagery into forest monitoring programmes. Global
changebiology,23(1):177–190,2017.
DamianWalwer,EricCalais,andMichaelGhil. Data-adaptivedetectionoftransientdeformationin
geodeticnetworks. JournalofGeophysicalResearch: SolidEarth,121(3):2129–2152,2016.
OpenAI. Gpt-4technicalreport,2023.
MatthiasDrusch,UmbertoDelBello,SébastienCarlier,OlivierColin,VeronicaFernandez,Ferran
Gascon,BiancaHoersch,ClaudiaIsola,PaoloLaberinti,PhilippeMartimort,etal. Sentinel-2:
Esa’sopticalhigh-resolutionmissionforgmesoperationalservices.RemotesensingofEnvironment,
120:25–36,2012.
12

<!-- Page 13 -->

GeoffreyBlewitt,WilliamHammond,etal. Harnessingthegpsdataexplosionforinterdisciplinary
science. Eos,99,2018.
KangHyeunJiandThomasAHerring. Transientsignaldetectionusinggpsmeasurements:Transient
inflationatakutanvolcano,alaska,duringearly2008. GeophysicalResearchLetters,38(6),2011.
PengzhenRen,YunXiao,XiaojunChang,Po-YaoHuang,ZhihuiLi,XiaojiangChen,andXinWang.
Acomprehensivesurveyofneuralarchitecturesearch: Challengesandsolutions. ACMComputing
Surveys(CSUR),54(4):1–34,2021.
AdrianoGualandi,EnricoSerpelloni,andMariaElinaBelardinelli. Blindsourceseparationproblem
ingpstimeseries. JournalofGeodesy,90(4):323–341,2016.
13

<!-- Page 14 -->


### Contents

1 Introduction 1
2 RelatedWork 2
2.1 Disentangledrepresentationlearning . . . . . . . . . . . . . . . . . . . . . . . . . 2
2.2 Inverseproblemsinphysicalsciences . . . . . . . . . . . . . . . . . . . . . . . . 3
2.3 Autoencoderasanapproachtoinversion . . . . . . . . . . . . . . . . . . . . . . . 3
3 Methods 3
3.1 Learningtheinverseofphysicalmodels . . . . . . . . . . . . . . . . . . . . . . . 3
3.2 Physicalmodelsforinversion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
3.3 End-to-endlearningwithphysicalmodels . . . . . . . . . . . . . . . . . . . . . . 5
3.4 Datasets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
3.5 Baseline . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
4 Results 6
4.1 Effectsofbiascorrection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
4.2 Evaluationofphysicalvariables . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
5 ConclusionandLimitations 9

### A Appendix 15

A.1 Makingafullydifferentiablephysicalmodelfordeeplearning . . . . . . . . . . . 15
A.1.1 ConversionofF toPyTorchassistedbyGPT-4 . . . . . . . . . . . . . 15

## Rtm

A.1.2 ValidatingthePyTorchimplementationofF . . . . . . . . . . . . . . 16

## Rtm

A.2 Bypassinginstabilitypointsinthetrainingloop . . . . . . . . . . . . . . . . . . . 16
A.2.1 NumericalinstabilityofF . . . . . . . . . . . . . . . . . . . . . . . . 16

## Rtm

A.2.2 Forwardpass . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
A.2.3 Backpropagation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
A.2.4 Stabilizedtrainingprocess . . . . . . . . . . . . . . . . . . . . . . . . . . 17
A.3 BiophysicalvariablesofF . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18

## Rtm

A.4 Sentinel-2dataset: spectralbands,temporal,andspeciesinformation . . . . . . . . 18
A.5 MathematicalformulationsofF . . . . . . . . . . . . . . . . . . . . . . . . . 19

### Mogi

A.6 GNSSdataset . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
A.6.1 GNSSstationsaroundtheAkutanvolcano. . . . . . . . . . . . . . . . . . 20
A.6.2 AssumedcomponentsofGNSStimeseries . . . . . . . . . . . . . . . . . 20
A.7 SmoothnesstermaddedtoMSElossforMogiinversion. . . . . . . . . . . . . . . 21
A.8 Implementationdetails . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
A.9 Extendedresultsforbiascorrection . . . . . . . . . . . . . . . . . . . . . . . . . 22
A.9.1 BiascorrectionforF . . . . . . . . . . . . . . . . . . . . . . . . . . 22

## Rtm

A.9.2 BiascorrectionforF . . . . . . . . . . . . . . . . . . . . . . . . . . 24
Mogi
14

<!-- Page 15 -->

A.10 Extendedresultsfortheevaluationofphysicalvariables . . . . . . . . . . . . . . . 28
A.10.1 RetrievedbiophysicalvariablesofF . . . . . . . . . . . . . . . . . . 28

## Rtm

A.10.2 ReconstructedGNSSsignalsbasedonZ . . . . . . . . . . . . . . . 32

### C,Mogi


### A Appendix

A.1 Makingafullydifferentiablephysicalmodelfordeeplearning
A.1.1 ConversionofF toPyTorchassistedbyGPT-4

## Rtm

TheoriginalmodulesofF areextractedfromavegetationappcalledEnMap. Itisimplemented

## Rtm

usingNumpyarraysandoperations. Totrackthecomputationalgraphandenablegradientbackpropagation, it was reimplemented using PyTorch operations. However, F is not inherently

## Rtm

differentiable,andasacomplicatedphysicalmodel,convertingitinPyTorchmanuallywaschallenging. Inlightoftherecentdevelopmentoflargelanguagemodels(LLMs),wedecidedtoutilize
GPT-4[OpenAI,2023]toassistintheconversionfromNumPytoPyTorch. WhileGPT-4reduceda
significantamountofrepetitivework,weranintothefollowinglimitations:
GPT-4 is useful for converting common operations from NumPy into PyTorch. We used it to
successfully convert 1,742 lines of code across various scripts from the original implementation
toPyTorch(e.g. Listing1andListing2). However,someoperationse.g. theexponentialintegral
functionfromSciPy,havenoequivalentinPyTorch(Listing2). Tocalculatetheirderivative,we
implementedourownbackwardfunctionstodefinederivatives.
Additionally,GPT-4onlyacceptstextinputoflimitedlength,whichmeansitcanonlyconvertascript
snippetpiecebypiece. Astheconversationlengthens,itmademistakes. Forinstance,itconverted
numpy.radianstotorch.radians,whichdoesnotexistinPyTorch. Thus,itwasstillimportant
to carefully check the conversion, run unit tests, and work on compiling all the scripts together.
Interestingly,GPTallowsforpromptengineering,whichmeanswecanprovidefeedbacktorefineits
conversions,suchasrequestingittohighlightuncertainpartsforreviewinsubsequentconversions.
1 n = PD_refractive
2 k = (np.outer(Cab, PD_k_Cab) + np.outer(Car, PD_k_Car) + np.outer(Anth
, PD_k_Anth) +
3 np.outer(Cbrown, PD_k_Brown) + np.outer(Cw, PD_k_Cw) + np.outer(
Cm, PD_k_Cm)) / N[:, np.newaxis]
4
5 ind_k0_row, ind_k0_col = np.where(k == 0)
6
7 if len(ind_k0_row) > 0:
8 k[ind_k0_row, ind_k0_col] = np.finfo(float).eps
9 trans = (1 - k) * np.exp(-k) + (k ** 2) * exp1(k)
Listing1: ExamplecodeofF initiallyimplementedusingNumPy. Itfeaturesanexponential

## Rtm

integralfunctionexp1inline9. Additionally,it’simportanttohighlightthatinline3,thestructure
parameterN functionsasadenominatorinthecalculation,therefore,itcannotbezero.
1 n = PD_refractive
2 k = (torch.outer(Cab, PD_k_Cab) + torch.outer(Car, PD_k_Car) + torch.
outer(Anth, PD_k_Anth) +
3 torch.outer(Cbrown, PD_k_Brown) + torch.outer(Cw, PD_k_Cw) +
torch.outer(Cm, PD_k_Cm)) / N.unsqueeze(-1)
4
5 ind_k0_row, ind_k0_col = torch.where(k == 0)
6
7 if len(ind_k0_row) > 0:
8 k[ind_k0_row, ind_k0_col] = torch.finfo(float).eps
15

<!-- Page 16 -->

9 trans = (1 - k) * torch.exp(-k) + (k ** 2) * torch.from_numpy(exp1(k.
numpy()))
Listing2: ConversionofF toPyTorchbyGPT.Itisfollowedbyfeedbackonexp1toraise

## Rtm

user’sattention. Hereisanexcerpt: "Pleasenotethattheexp1functionisnotavailableinPyTorch
asofmylasttrainingcut-offinSeptember2021. Wecanimportitfromthescipy.speciallibrary,but
wehavetoconvertthetensortonumpybeforeusingitandconverttheresultbacktoatensor. It’snot
idealintermsofperformance,butI’mafraidthere’snootheroptionfornow. Pleasecheckifthereis
anupdatedversionofPyTorchthatincludesthisfunction."
ThisexperimentwasdoneinMay2023,whenGPTwasstillinitsearlyphaseofdevelopment. Ithas
hadseveralfeaturesupdatedsincethen.Forinstance,itcannowacceptlongertextinputs.Nonetheless,
webelievethelimitationsdiscussedabovestilllargelyholdtrueandareworthconsideringwhen
convertinglegacyimplementationsofothercomplexphysicalmodels.
A.1.2 ValidatingthePyTorchimplementationofF

## Rtm

To validate the implementation of F in PyTorch against its original version in NumPy, we

## Rtm

randomlysampled10,000setsofvariables,passedthemthrougheachimplementation,andcompared
theiroutputs(Tab.5). Themismatchrateoftheoutputsis0.457%whentheabsolutetoleranceis
set to 1e-5. The maximum absolute difference over all 130000 output reflectances from the two
implementationsis3.050e-5whereinthephysicalunitofreflectancehereis1. Thisindicatesthat
F implementedinPyTorchissubstantiallyequivalenttoitsoriginalversionand,thereforecan

## Rtm

beusedinsubsequenttasks. ThePyTorchimplementationfortheRTMhasbeenreleasedonGitHub
(https://github.com/yihshe/MAGIC.git)asapublicPythonlibrarytofacilitateitsintegration
intootherdeep-learningworkflows.
Table5: UnittestoftheoutputsofourPyTorchimplementationofF againsttheoriginal

## Rtm

NumPyversion. Thetotalnumberofelementstocompareis130000aswesimulatethesamesetof
10000samplesforbothimplementations,eachwith13spectralbandsofSentinel-2.
TotalElements MismatchedElements AbsoluteTolerance MismatchRatio MaxAbsoluteDifference
130000 594 1e-5 0.457% 3.050e-5
A.2 Bypassinginstabilitypointsinthetrainingloop
A.2.1 NumericalinstabilityofF

## Rtm

WithF nowimplementedinPyTorch,wecanbackpropagategradientsthroughthisphysical

## Rtm

model. However,themodelissensitivetoinputvariablerangesandisnon-differentiableatcertain
points. Furthermore,complexoperationslikeexponential,logarithm,andsquareroot,oftenleadto
numericalinstabilityduringderivativecomputation,eventhoughtheseoperationsaretheoretically
differentiable. Tosolvetheseissues,wehavedevelopedthefollowingmethodstostabilizetraining
whenusingacomplexphysicalmodellikeF .

## Rtm


### A.2.2 Forwardpass

Bydefinition,inputvariablesZ arenon-negativevalueswithphysicalmeanings(Tab.1). In

## Rtm

practice,F canfailintheforwardpasswhenZ fromothervaluerangesareprovided(e.g.

## Rtm Rtm

structureparameterZ inListing1). ThesameconceptappliestoF . Thus,forbothmodels,

### N Mogi

wechoosetoinitiallyinfernormalizedvariablesΛ∈[0,1]andsubsequentlymapthesetovariables
Z ∈[Z ,Z ]intheiroriginalscale,accordingtotheirvalueranges(Tabs.1and2).
min max

## Z =(Z −Z )·Λ+Z (6)

max min min
Thisapproachnotonlyfacilitatesasuccessfulforwardpassofphysicalmodelsbutalsonarrows
downthesearchspaceforoptimization.
16

<!-- Page 17 -->


### A.2.3 Backpropagation

Despiteencodingtheforwardpasssuccessfully,backpropagationremainedunstableforF . For

## Rtm

successful learning, it is necessary to backpropagate gradients through the physical model. The
aforementionedcaveatsofF resultedinbackpropagationfailures,leadingtoNaNgradientand

## Rtm

thenNaNloss. Duringexperimentstostabilizethebackpropagation,wenoticedthatNaNgradients,
whentheyinitiallyappear,arealwaysinassociationwithspecificsetsofF variables. Ideally,

## Rtm

onewouldapplyconstraintstospecificF operationscausingtheseNaNgradients. However,

## Rtm

workingoutsuchconstraintsseemedchallengingunlessweunderstoodthesemanticsofF and

## Rtm

itsdifferentiabilitythoroughly,acomplextask.
We,therefore,introducedasimpleworkaround: sinceitistheNaNgradientsthatcausesubsequent
learningfailure,wereplacethemwithasmallrandomvalue,sampledfromauniform[0,1]distribution
andscaledby1e-7,wheneverthesegradientsfirstappear. Thespecificworkflowofthealgorithmis
describedinalgorithm1
Algorithm1Gradientstabilization

### Calculategradients

Initializelistgrads,containinggradientsofallmodelparameterswheregradientsexistandcontain
anyNaNvalues
ifgradsisnotemptythen
Setasmallconstantepsilonequalto1e-7
foreachvingradsdo
Generaterandomvaluesofthesameshapeasv,scaledbyepsilon

### CreateamaskwherevisNaNorequals0

ReplacevaluesinvwherethemaskisTruewithcorrespondingrandomvalues
endfor
endif

### Updategradients


### A.2.4 Stabilizedtrainingprocess

OurmethodseffectivelystabilizedthelearningofM andM intheautoencoderframe-

## B,Rtm C,Rtm

work,despiteinstabilityofF duringbackpropagation. AscanbeseeninFig.9,bothtrainingand

## Rtm

validationlossesofM convergeovertheepochs. Therefore,bypreventingthepropagationof

## C,Rtm

NaNgradientstoearlierlayersandallowingthenormalprogressionoftheforwardpass,thestabilizer
haseffectivelyenabledthetrainingprocesstobypassinstabilitypointsintheoptimizationspaceand
allowedacontinuoussearchforoptimalpoints.
Figure9: StabilizedtrainingofM . Ouralgorithmtoupdatethegradientshasovercomethe

## C,Rtm

instabilityofF duringbackpropagationandallowedtheconvergenceoftrainingloss.

## Rtm

17

<!-- Page 18 -->

A.3 BiophysicalvariablesofF

## Rtm

TheinputofF consistsofbiophysicalvariablesofthreehierarchicallevels.Notethattheoriginal

## Rtm

F doesnothavefractionalcoverageZ asaninputvariable. WeincludeZ asoneoftheseven

### RTM fc fc

variablestobelearneddirectlybyourmodel,whichwillbeusedtoinfercrowndiameterZ and
cd
height Z based on derived equations. As the fractional coverage is jointly defined by the stem
h
densityandcrowndiameterwithineachunithector(or10,000m2),Z canbederivedgivenZ and
cd fc
Z usingeq.(7). Furthermore,toderiveZ ,wefitanallometricequation(Fig.10,eq.(8))using
cd h
thesamplesoftemperateforestsfromtheglobalallometricdatabase[Juckeretal.,2017]. R2ofthe
derivedequationbetweenZ andZ is0.383(eq.(8)).
h cd
Table6: OverviewofthebiophysicalvariablesofF . Thesevariablescanbeattributedtothree

## Rtm

hierarchicallevels. 7variablesarelearneddirectly. *Z andZ willbeinferredfromfcusing
cd h
eq.(7)andeq.(8),respectively.

### SampleRange

Group Variable Acronym ToLearn DefaultValue

### Min Max

Background Soilbrightnessfactor psoil ✗ 0.8 - -
StructureParameter N ✓ - 1 3

### ChlorophyllA+B cab ✓ - 10 80

WaterContent cw ✓ - 0.001 0.02

### DryMatter cm ✓ - 0.005 0.05

LeafModel Carotenoids car ✗ 10 - -
BrownPigments cbrown ✗ 0.25 - -
Anthocyanins anth ✗ 2 - -

### Proteins cp ✗ 0.0015 - -

Cabon-basedConstituents cbc ✗ 0.01 - -

### LeafAreaIndex LAI ✓ - 0.01 5

LeafAngleDistribution typeLIDF ✗ BetaDistribution - -

### HotSpotSize hspot ✗ 0.01 - -

CanopyModel ObservationZenithAngle tto ✗ 0 - -

### SunZenithAngle tts ✗ 30 - -

RelativeAzimuthAngle psi ✗ 0 - -
UndergrowthLAI LAIu ✓ - 0.01 1

### StemDensity sd ✗ 500 - -

ForestModel FractionalCoverage fc ✓ - 0.1 1

### TreeHeight h ✓ * * *

CrownDiameter cd ✓ * * *
(cid:114)

## Z ·10000

Z =2· fc (7)
cd π·Z
sd
Z =exp(2.117+0.507·ln(Z )) (8)
h cd
A.4 Sentinel-2dataset: spectralbands,temporal,andspeciesinformation
ThedetailedinformationofthespectralbandsofX canbeviewedinTab.7. StatisticsoftheX

## S2 S2

canbeviewedinTab.8. Thesespectraweresampledfromindividualsitescoveringatimesequence
of14timestamps. NotethatourcurrentapproachtoinvertingF doesnotintegratetemporal

## Rtm

informationintothelearningprocess,althoughtemporalvariationsareevaluated. Suchtemporal
informationcouldserveasusefulpriorknowledgetoboostthemodel’sperformance,especiallyto
ensuretheconsistencyoftemporalvariations,whichwewillconsiderinfutureworks.
AllsamplesfromX coverbothconiferousanddeciduousforestsconsistingof5and7species,

## S2

respectively:
• Coniferousforest: PseudotsugaMenziesii,PiceaAbies,PinusNigra,LarixDecidua,Pinus
Sylvestris.
18

<!-- Page 19 -->

Figure10: AllometricrelationshipbetweencanopyheightZ andcrowndiameterZ . Wefitan
h cd
allometricequationbetweenZ andZ (eq.(8)). R2ofthefittedequationis0.383.
h cd
Table7: Sentinel-2bandstouse. VNIRstandsforVisibleandNearInfrared. SWIRstandsforShort
WaveInfrared.

### Band B2 B3 B4 B5 B6 B7 B8 B8a B9 B11 B12


### Resolution 10m 10m 10m 20m 20m 20m 10m 20m 60m 20m 20m

CentralWavelength 490nm 560nm 665nm 705nm 740nm 783nm 842nm 865nm 940nm 1610nm 2190nm
Description Blue Green Red VNIR VNIR VNIR VNIR VNIR SWIR SWIR SWIR
• Deciduous forest: Prunus Spp, Fagus Sylvatica, Carpinus Betulus, Quercus Spp, Acer
Pseudoplatanus,FraxinusExcelsior,AlnusGlutinosa.
A.5 MathematicalformulationsofF

### Mogi

F describesthedisplacement field onthesurfaceresulting fromasphericalpressuresource,

### Mogi

typically a magma chamber, at depth. The inverse problem of F deals with estimating the

### Mogi

locationandvolumechangeofmagmachamberactivitiesgiventheobserveddisplacementsatground
stations. Inthisproject,F touseisfurthersimplifiedbyassumingonlyapointpressuresource.

### Mogi

Specifically, for N ground stations located at {x ,y ,z ,i = 1,··· ,N}, the displacement field
i i i
X ={x ,x ,x ,i=1,··· ,N}atthesurfacealongtheeast,north,andverticaldirections

### GNSS e,i n,i v,i

duetothesubsurfacevolumetricchangeofaMogisourceisestimatedby:
α(x −Z )
xˆ = i xm , (9)
e,i R3
i
α(y −Z )
xˆ = i ym , (10)
n,i R3
i
α(z −Z )
xˆ = i d (11)
v,i R3
i
whereZ andZ arethehorizontalcoordinatesoftheMogisource,andZ isitsdepth. αisthe
xm ym d
scalingfactorthatincludesthevolumechangeZ andthematerialproperties(Poisson’sratioof

## ∆V

themedium),givenby:
(1−ν)Z
α= ∆V (12)
π
Table8: InformationoftheSentinel-2datasetX

## S2

TotalNumberofSpectra NumberofIndividualSites NumberofDates NumberofSpecies
17962 1283 14 12
19

<!-- Page 20 -->

andR istheradialdistancefromtheMogisourcepointtothestationat(x ,y ,0)(theequationsare
i i i
validforahalf-space,soelevationisneglected):
(cid:113)
R = (x −x )2+(y −y )2+Z2 (13)
i i m i m d
Fortheinversionproblem,weassumethefollowingparametersareknown:
• ν,Poisson’sratio,usuallysetat0.25,atypicalvaluefortheEarth’scrust.
• {x ,y i=1,··· ,N},locationsoftheGNSSstations.
i i
Thus,ourgoalistoestimatethelocation(Z ,Z ,Z )andvolumechangeZ oftheMogisource,
xm ym d ∆V
giventhemeasureddisplacementsrecordedbytheGNSSstationsX = {u ,u ,u ,i =
GNSS e,i n,i v,i

## 1,··· ,N}.


### A.6 GNSSdataset


### A.6.1 GNSSstationsaroundtheAkutanvolcano

Surface displacement is monitored via continuous GNSS (Global Navigation Satellite System)
stationsthatproducedailypositiontimeseries(http://geodesy.unr.edu,Blewittetal.[2018].
FortheAkutanvolcano,wehave12GNSSstationswithintheregion(Fig.11). Fromthesestations,
wehavecompileddailytime-seriesGNSSdisplacementdataspanningfrom2006to2024,whichwe
willusetotestourinversionapproach. ItiscommonforGNSSstationstooccasionallymissdatadue
tovariousissuessuchaspoweroutagesorinstrumentreplacements. Approximately20%ofourraw
timeseriesdataismissing,which,althoughsignificant,isstillconsideredgoodintermsofGNSS
observations. WehaveemployedavariationalBayesianIndependentComponentAnalysis[Gualandi
etal.,2016]tofillupthesedatagapsusingexistingobservationstomakesurewehaveacomplete
dailytimeseries.
Ourmodeltakesthedisplacementfieldobservedateachsingledayasatrainingsample. However,
wecanchecktheplausibilityoftheinversionbyevaluatingthetemporalvariationsoftheretrieved
variablesandreconstructedsignalscomparingthemagainstexistingliterature[JiandHerring,2011,
Walweretal.,2016].
Figure11: Locationsofthe12GNSSstationsaroundtheAkutanVolcano.

### A.6.2 AssumedcomponentsofGNSStimeseries

InadditiontodeformationsduetoaMogisource,thesurfacedisplacementobservedbyaGNSS
station can be influenced by other physical processes and noise sources. In simplified form, a
20

<!-- Page 21 -->

displacementu(t)ofastationalongcertaindirectionattimetcanbemodeledas[Walweretal.,
2016]:
u(t)=S (t)+S (t)+S (t)+S (t)+ϵ +ϵ (14)
linear annual semiannual eruption pink white

### Where:

S (t)=q+m·t (15)
linear
(cid:18) (cid:19) (cid:18) (cid:19)
2πt 2πt
S (t)=A ·sin +B ·cos (16)
annual 1 T 1 T
1 1
(cid:18) (cid:19) (cid:18) (cid:19)
2πt 2πt
S (t)=A ·sin +B ·cos (17)
semiannual 2 T 2 T
2 2
S (t)=C·Z (18)
eruption ∆V,t
S representsthelineartrend, oftenduetotectonicplatemovement; S andS
linear annual semiannual
represent the annual and semiannual seasonality of the signal, potentially due to hydrological
processes;andS accountsforthedeformationduetoMogisourcesincetheeruptionevent
eruption
happeningatt anddependsonthevolumechangeZ attimestept. ϵ andϵ arepink
s ∆V,t pink white
andwhitenoises,respectively,commonlyobservedinnaturalphenomena.
The volcanic deformation S (t) can be small (usually at mm level) if compared to other
eruption
sourcesofdeformationineq.(14)(mmtocmlevel),makingthebiascorrectionbothanessential
ingredienttogetaccurateresultsandachallengingtaskduetotheincompletenessofF .

### Mogi


### A.7 SmoothnesstermaddedtoMSElossforMogiinversion

ComparedtoX ,X exhibitsstrongertemporaldynamicsasadailytimeseries. Whileour

## S2 Gnss

model takes the displacement field of each day as input, enhancing the smoothness of the Mogi
reconstructionsalongthetemporaldimensionwillaligntheresultsmorecloselywiththeexpectation
thatthedeformationfromthevolcanicsource(S )shoulddemonstratetemporalcontinuity,
eruption
ratherthanbeinginfluencedbythepatternsofsystematicbiasesfromothercomponentsineq.(14).
To enhance the temporal continuity of the Mogi reconstructions, we structure the data such that
eachbatchcontainsmini-sequencessampledfromT consecutivedays. Wehavealsointroducedan
additionalsmoothnesstermtoM ,whichisexpressedasfollows:
C,Mogi

## B T−1

L (θ ,θ )=L (θ ,θ )+λ (cid:88)(cid:88) ∥x(t+1)−x(t) ∥2 (19)
total EC C MSE EC C F,C,j F,C,j
j=1 t=1
wherethesequencesizeT isthenumberoftimestepsineachsequence, andthebatchsizeB is
thenumberofsequencesineachbatch. Inourcase,T = 5andB = 12,leadingtoatotalof60
samplesperbatch,matchingthetrainingsetupusedfortheclassicalauto-encoderM . The

### A,Mogi

parameterλissetat0.01toensureminimaldramaticchangeswithinthe5-daywindow,reducing
noiseandensuringcontinuityintheMogireconstruction(Fig.12). Thesamesmoothnesstermis
appliedduringthetrainingprocessofM .

### B,Mogi


### A.8 Implementationdetails

Both X and X are further split into the train, validation, and test sets. For X , samples

## S2 Gnss S2

fromthesameindividualsiteareplacedinthesamesettoavoiddataleakage. ForX ,wehave

## Gnss

savedtheGNSStimeseriesfrom2006to2009asatestsettocoverthe2008eventforvalidation.
Thebatchsizeissetto64forloadingX and60forloadingX . TraininglossisMSEand

## S2 Gnss

forM andM withanaddedregularizertosmooththereconstructedtimeseriesfrom

### B,Mogi C,Mogi

M (eq.(19)). WeusedtheAdamoptimization,settingtheinitiallearningrateat0.001and

### C,Mogi

weightdecayat0.0001. Themaximumnumberofepochsis100andthelearningrateisreducedbya
factorof10after50epochs;trainingstopsifL onthevalidationsetdoesnotimproveafteran

## Mse

additional10epochs. AllexperimentswereconductedonasystemequippedwithanAMDEPYC
770264-CoreProcessorand1TBofRAM.Trainingtimesvarieddependingonthemodelcomplexity.
Specifically,modelsthatrequirebackpropagationthroughF (suchasM andM )

## Rtm B,Rtm C,Rtm

tookapproximately3hourstotrain. Incontrast,trainingtimesforallothermodelsdidnotexceed
halfanhour.
21

<!-- Page 22 -->

Figure12: ThesmoothnesstermhasenhancedthetemporalcontinuityofMogireconstruction
illustratedforAV08. Orange: X . Blue: MogireconstructionsusingZ .

### GNSS C,Mogi

A.9 Extendedresultsforbiascorrection
A.9.1 BiascorrectionforF

## Rtm

Figure 13: Reconstruction accuracy of X displays clear bias without bias correction

## B,Rtm

module.
22

<!-- Page 23 -->

Figure 14: Reconstruction accuracy of X displays clear bias without bias correction

## D,Rtm

module,showingasimilarpatternofbiasasFig.14.
Figure15: ReconstructionaccuracyofX significantlyimprovedafterbiascorrection.

## C,Rtm

23

<!-- Page 24 -->

Figure16: ReconstructedspectralsignaturesbasedonZ andclusteredbyspecies,which

## C,Rtm

display distinct patterns between forest types. Notably, the bias correction for ‘Larix decidua’
displaysapatternsimilartothoseofdeciduousforest,whichisconsistentwithourfindingsinFig.6b.
A.9.2 BiascorrectionforF

### Mogi

Figure17: ReconstructionaccuracyofX illustratedforverticaldisplacements,which

### B,Mogi

displaysclearbiasandismorecomplexthanthoseshownbyF .

## Rtm

24

<!-- Page 25 -->

Figure18: ReconstructionaccuracyofX illustratedforverticaldisplacements. Thebias

### C,Mogi

correction has improved the reconstruction but its as not as linear as for RTM, highlighting the
trade-offbetweenmodelsimplicityandbiascorrectioncomplexity.
25

<!-- Page 26 -->

Figure19: ReconstructedGNSSsignalsandcorrectedbiasesillustratedfornorthdisplacements
forthefirsthalfof12GNSSstations. Orange: measuredobservationsX . Blue: Mogioutput

## S2

X (first column); Corrected biases B(Q) = X −X (second column);

### FMogi,C C,Mogi C,Mogi FMogi,C

CorrectedoutputX (thirdcolumn). X clearlycapturesthetransientsignalsin2008,

### C,Mogi FMogi,C

characterizedbytheradialextensionalonghorizontaldirections. Incontrast,B(Q) mainly

### C,Mogi

capturestheseasonalcomponentsandnoisesassuggestedineq.(14),anditstemporalvariations
acrossstationsdonotcontainprominenttransientsignals,whichisalignedwithourexpectations
abouttheseasonalcomponentsandrandomnoises. Ontheleftpartoftheblacklinearevalidations
onthetestset,andontherightpartarevalidationsonthetrainingset. Thepredictionsareconsistent
throughoutthetrainingandtestsets.
26

<!-- Page 27 -->

Figure20: ReconstructedGNSSsignalsandcorrectedbiasesillustratedfornorthdisplacements
forthesecondhalfof12GNSSstations. Orange: measuredobservationsX . Blue: Mogioutput

## S2

X (first column); Corrected biases B(Q) = X −X (second column);

### FMogi,C C,Mogi C,Mogi FMogi,C

CorrectedoutputX (thirdcolumn). X clearlycapturesthetransientsignalsin2008,

### C,Mogi FMogi,C

characterizedbytheradialextensionalonghorizontaldirections. Incontrast,B(Q) mainly

### C,Mogi

capturestheseasonalcomponentsandnoisesassuggestedineq.(14),anditstemporalvariations
acrossstationsdonotcontainprominenttransientsignals,whichisalignedwithourexpectations
abouttheseasonalcomponentsandrandomnoises. Ontheleftpartoftheblacklinearevalidations
onthetestset,andontherightpartarevalidationsonthetrainingset. Thepredictionsareconsistent
throughoutthetrainingandtestsets.
27

<!-- Page 28 -->

A.10 Extendedresultsfortheevaluationofphysicalvariables
A.10.1 RetrievedbiophysicalvariablesofF

## Rtm

Figure21: DistributionsofvariablesaretightenedupbybiascorrectionillustratedforZ

## C,Rtm

vs. Z . Without bias correction the variable distributions (red) are implausible, tending to

## B,Rtm

breakoutbeyondthepresetboundedranges. Withbiascorrection(blue),themodelisabletolearn
moreplausibledistributions.
Figure22: ApplicationoftheregressorbaselineM toX leadstoimplausibleparameter

## D,Rtm S2

distributionsofZ thattendtobreakoutofthepresentparameterranges.

## D,Rtm

28

<!-- Page 29 -->

Figure23: Z learnedbyourmodelareplausibleanddistinguishbetweenforesttypes.

## C,Rtm

Figure24: Pairwiseco-distributionsofZ learnedbytheregressorbaselineshownoclear

## D,Rtm

physicalpatterns. Red: coniferousforest. Blue: deciduousforest.
29

<!-- Page 30 -->

Figure25:Pairwiseco-distributionsofZ learnedbyourmodelshowdistinctandplausible

## C,Rtm

physicalpatterns. Red: coniferousforest. Blue: deciduousforest.
Table9: StatisticsofZ learnedbyM . WehavealsousedZ tocalculatetheJM

## D,Rtm D,Rtm D,Rtm

distancebetweenspeciesdistributions,whicharelessdisentangledcomparedtoZ .

## C,Rtm


### Species N cab cw cm LAI LAIu fc

Pseudotsugamenziesii 1.43±0.54 38.31±14.87 1.79±0.25 1.91±1.02 2.15±1.24 0.72±0.34 0.61±0.19
Piceaabies 1.36±0.44 39.49±13.24 1.87±0.17 2.15±0.98 1.72±1.25 0.84±0.25 0.58±0.13
Pinusnigra 1.56±0.55 39.50±15.81 1.86±0.20 2.47±1.13 2.32±1.42 0.54±0.37 0.62±0.19
Larixdecidua 1.50±0.50 38.26±13.85 1.61±0.42 1.43±0.69 1.90±1.04 0.56±0.40 0.67±0.21
Pinussylvestris 1.56±0.58 42.34±15.68 1.90±0.11 1.99±1.01 2.40±1.25 0.67±0.37 0.59±0.18
Prunusspp 1.90±0.84 43.22±22.17 1.35±0.57 1.60±1.04 1.79±0.82 0.46±0.34 0.71±0.25
Fagussylvatica 1.98±0.76 46.75±20.22 1.71±0.42 1.21±0.79 2.17±0.92 0.33±0.37 0.82±0.23
Carpinusbetulus 1.96±0.71 47.55±19.40 1.67±0.36 1.36±0.84 1.91±0.91 0.55±0.40 0.75±0.21
Quercusspp 1.91±0.69 48.59±18.28 1.73±0.41 1.46±0.83 2.09±0.94 0.55±0.40 0.75±0.21
Acerpseudoplatanus 2.21±0.75 51.34±20.31 1.72±0.45 1.51±0.79 2.01±0.99 0.27±0.33 0.86±0.18
Fraxinusexcelsior 2.16±0.71 51.67±18.05 1.76±0.37 1.93±1.17 2.05±1.07 0.44±0.39 0.78±0.21
Alnusglutinosa 2.22±0.72 55.01±18.09 1.78±0.34 2.03±0.97 2.04±1.03 0.46±0.41 0.76±0.20
30

<!-- Page 31 -->

Figure26: TemporalvariationsofinferredphysicalparametersZ arelessconsistentover

## D,Rtm

time.
Table10: StatisticsofZ learnedbyM . WehavealsousedZ tocalculatethe

## C,Rtm C,Rtm C,Rtm

JMdistancebetweenspeciesdistributionsandourmodelcanlearndisentangledrepresentations.

### Species N cab cw cm LAI LAIu fc

Pseudotsugamenziesii 1.65±0.16 39.96±5.33 1.00±0.24 2.36±0.23 2.66±0.43 0.49±0.07 0.66±0.04
Piceaabies 1.53±0.16 43.33±4.89 0.99±0.24 2.37±0.21 2.70±0.43 0.50±0.07 0.68±0.04
Pinusnigra 1.75±0.16 42.71±5.63 0.96±0.19 1.97±0.28 2.73±0.37 0.48±0.06 0.64±0.04
Larixdecidua 1.86±0.13 36.52±7.50 0.88±0.25 2.28±0.33 2.34±0.48 0.49±0.08 0.59±0.05
Pinussylvestris 1.71±0.14 39.87±5.18 0.99±0.18 2.24±0.24 2.68±0.34 0.48±0.05 0.66±0.03
Prunusspp 1.93±0.12 34.71±8.65 0.80±0.30 2.26±0.37 2.13±0.54 0.50±0.10 0.53±0.05
Fagussylvatica 1.98±0.17 29.76±10.71 0.94±0.33 2.24±0.53 2.32±0.69 0.43±0.11 0.54±0.06
Carpinusbetulus 1.90±0.11 33.38±9.65 0.99±0.31 2.37±0.48 2.42±0.61 0.45±0.10 0.56±0.05
Quercusspp 1.87±0.11 33.46±8.55 1.06±0.33 2.35±0.48 2.56±0.63 0.44±0.10 0.59±0.06
Acerpseudoplatanus 1.99±0.14 30.82±10.09 0.99±0.34 2.12±0.49 2.45±0.68 0.42±0.12 0.54±0.05
Fraxinusexcelsior 1.90±0.12 34.73±8.27 1.02±0.32 2.19±0.39 2.57±0.56 0.45±0.10 0.58±0.05
Alnusglutinosa 1.89±0.13 35.02±8.37 0.99±0.27 2.22±0.30 2.52±0.48 0.46±0.08 0.59±0.05
31

<!-- Page 32 -->

Figure27: TemporalvariationsofinferredphysicalparametersZ . M effectively

## C,Rtm C,Rtm

capturesdistinct,temporallysmoothandplausiblevariationsfordifferentforesttypes.
A.10.2 ReconstructedGNSSsignalsbasedonZ
C,Mogi
32

<!-- Page 33 -->

Figure28: TimeseriesofGNSSdisplacementsillustratedforthefirsthalfof12GNSSstations,
locatedaroundtheMogisource. Orange: X . Blue: MogireconstructionsusingZ . Red:

### GNSS C,Mogi

MogireconstructionsfittedbyaKalmanfilter. Ourmodelsuccessfullyreconstructsthe2008volcanic
inflationtransientsignals,characterizedbyradialexpansionandverticaluplift,withdisplacement
magnitudesof10mm,alignedwithpriorfindings[JiandHerring,2011,Walweretal.,2016].
33

<!-- Page 34 -->

Figure29: TimeseriesofGNSSdisplacementsillustratedforthesecondhalfof12GNSSstations,
locatedaroundtheMogisource. Orange: X . Blue: MogireconstructionsusingZ . Red:

### GNSS C,Mogi

MogireconstructionsfittedbyaKalmanfilter. Ourmodelsuccessfullyreconstructsthe2008volcanic
inflationtransientsignals,characterizedbyradialexpansionandverticaluplift,withdisplacement
magnitudesof10mm,alignedwithpriorfindings[JiandHerring,2011,Walweretal.,2016].
34

## Tables

**Table (Page 15):**

| n = PD_refractive |
|---|
| k = (np.outer(Cab, PD_k_Cab) + np.outer(Car, PD_k_Car) + np.outer(Anth |
| , PD_k_Anth) + |
| np.outer(Cbrown, PD_k_Brown) + np.outer(Cw, PD_k_Cw) + np.outer( |
| Cm, PD_k_Cm)) / N[:, np.newaxis] |
|  |
| ind_k0_row, ind_k0_col = np.where(k == 0) |
|  |
| if len(ind_k0_row) > 0: |
| k[ind_k0_row, ind_k0_col] = np.finfo(float).eps |
| trans = (1 - k) * np.exp(-k) + (k ** 2) * exp1(k) |


**Table (Page 15):**

| n = PD_refractive |
|---|
| k = (torch.outer(Cab, PD_k_Cab) + torch.outer(Car, PD_k_Car) + torch. |
| outer(Anth, PD_k_Anth) + |
| torch.outer(Cbrown, PD_k_Brown) + torch.outer(Cw, PD_k_Cw) + |
| torch.outer(Cm, PD_k_Cm)) / N.unsqueeze(-1) |
|  |
| ind_k0_row, ind_k0_col = torch.where(k == 0) |
|  |
| if len(ind_k0_row) > 0: |
| k[ind_k0_row, ind_k0_col] = torch.finfo(float).eps |


**Table (Page 16):**

| trans = (1 - k) * torch.exp(-k) + (k ** 2) * torch.from_numpy(exp1(k. |
|---|
| numpy())) |
