---
title: "Image Text Alignment"
original_file: "./Image_Text_Alignment.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["rag", "fine-tuning", "evaluation", "multimodal"]
keywords: ["motion", "mri", "fetal", "image", "slice", "learning", "brain", "deep", "these", "correction"]
summary: "<!-- Page 1 -->


### A Literature Review on

Fetus Brain Motion Correction in MRI

### Haoran Zhang1, Yun Wang2

1DepartmentofComputerScience,DukeUniversity,
2DepartmentofBiomedicalInformatics,EmoryUniversity

### Abstract

ThispaperprovidesacomprehensivereviewofthelatestadvancementsinfetalmotioncorrectioninMRI.Wedelveinto
variouscontemporarymethodologiesandtechnologicaladvancementsaimedatovercomingthesechallenges. Itincludes
traditional 3D fetal MRI correction methods like Slice to Volume Regi"
related_documents: []
---

# Image Text Alignment

<!-- Page 1 -->


### A Literature Review on

Fetus Brain Motion Correction in MRI

### Haoran Zhang1, Yun Wang2

1DepartmentofComputerScience,DukeUniversity,
2DepartmentofBiomedicalInformatics,EmoryUniversity

### Abstract

ThispaperprovidesacomprehensivereviewofthelatestadvancementsinfetalmotioncorrectioninMRI.Wedelveinto
variouscontemporarymethodologiesandtechnologicaladvancementsaimedatovercomingthesechallenges. Itincludes
traditional 3D fetal MRI correction methods like Slice to Volume Registration (SVR), deep learning-based techniques
suchasConvolutionalNeuralNetworks(CNNs),LongShort-TermMemory(LSTM)Networks,Transformers,Generative
AdversarialNetworks(GANs)andmostrecentadvancementsofDiffusionModels. Theinsightsderivedfromthisliterature
reviewreflectathoroughunderstandingofboththetechnicalintricaciesandpracticalimplicationsoffetalmotioninMRI
studies,offeringareasonedperspectiveonpotentialsolutionsandfutureimprovementsinthisfield.
Introduction significantprogressiontowardsfeasibleclinicalvalidation of fetal brain MRI motion correction [7, 8, 9,
10,11,12,13]. Whiledemonstratedeffectiveness,they
Observingfetalbraindevelopmentiscrucialfordiagarestillsubjecttochallengeslikelargemotionsand
nosingconditionssuchasautismandotherdevelopinitializationfailures[14]. Totacklethesechallenges,
mentalanomalies[1]. MagneticResonanceImaging
deep-learningbasedmethodshavebeenactivelypro- (MRI)offerssignificantadvantagesinthiscontext,beposedlikeConvolutionalNeuralNetworks(CNNs)
ingprecise,rapid,andexhibitingnoknownharmful
[15, 14, 16, 17, 18], Long Short-term Memory Neteffects in either the short or long term when examwork(LSTM)[19],Transformers[20,21],Generative
ining brain development [2]. However, the efficacy
AdversarialNetworks(GANs)[22,23]andDiffusion
ofMRIiscompromisedbychallengessuchasrapid
Models [24, 25]. To gain a comprehensive underfetalmovementsandmaternalbreathing[3]. These
standing of the various methodologies in this field,
factorsresultinrelativelylowsignal-to-noiseratios
wehaveconductedaliteraturereviewwithaspecific
in the obtained images. Moreover, unlike adults or
focus on algorithmic designs. Our review concenneonates,fetusesexhibitunrestrainedandpotentially
trates on the studies on the fetal brain, intending
largemovements. Beingencasedwithinmaternaltistonotonlyelucidatethecurrentstateoffetalbrain
sues,thefetalbrainoccupiesasmallerarearelative
MRI motion correction but also offer insights into
to these surrounding tissues. The above challenges
potentialfuturedirectioninthefield.
coupledwiththelowcontrastbetweenthefetalbrain
tissueandsurroundingmatter, rendersimaginginterpretationparticularlydifficult[4].

### Literature Search

MRIdataacquisitionoccursintheFourierdomain,
knownask-space,whereeachdatapointrepresents
the frequency content of the image. Alterations to The literature review was conducted using search
evenasinglepointink-spacecanimpacttheentire termssuchas"fetalbrain,""motioncorrection,"and
image. MotionduringMRIscansintroduceserrors "MRI." This search encompassed the period from
into k-space, resulting in blurring and/or ghosting December15,2023,toJanuary20,2024,focusingon
artifactsintheimagedomain[5]. thelatestdevelopmentsinthisrapidlyevolvingfield.
Active research endeavors are underway to miti- In the subsequent sections of this paper, we will
gatethesemotion-relatedissues. Imagingtechniques methodicallyexamineavarietyofmethodologiesfor
such as Echo Planar Imaging (EPI) [6] have shown correctingmotioninfetalbrainMRIscans. Thestrucpromiseinmotionreductionbyemployingspecific tureofthepresentationisintentionallydesignedto
strategies within EPI. Fast snapshot imaging meth- facilitate a clear and logical understanding, beginods such as Single-Shot Fast Spin Echo (SSFSE) are ning with traditional methodologies and gradually
also commonly used to acquire thick stacks of 2D progressing to sophisticated neural network-based
slicesthatcanlargelyremovein-planemotion[7]. approaches.
In recent 15 years, the advancement of Slice to Thesemethodologiescanbedividedintotwopri-
VolumeRegistration(SVR)algorithmshasmarkeda marycategories: i. Slice-to-VolumeRegistration,and
4202
naJ
03
]VI.ssee[
1v28761.1042:viXra

<!-- Page 2 -->

ii. Deep Learning Methods. Within each category, improvingtheresolutionandclarityoftheresulting
variousstudiesandtechniquesareexamined. Some image.
of these studies may overlap in terms of their ap- The methodology adopts an iterative approach,
proachesorfindings;however,weaimtodifferentiate whereSteps1and2arealternatedrepeatedly. This
thembasedontheircoreattributes,suchasnetwork iterativeprocessiscrucialforachievingconvergence
featuresandstructures. Thisprogressionfromfoun- towardsastableandaccuratereconstructionofthe
dational techniques to cutting-edge advancements fetal brain. Throughout these steps, there is also a
willallowforacomprehensiveunderstandingofthe qualitycontrolmechanisminplace. Thismechanism
field. Eachmethodwillbebrieflyintroducedtopro- involves the exclusion of any slices that are either
vide a contextual framework, paving the way for misaligned or exhibit signs of corruption, ensuring
morein-depthdiscussioninthefollowingsections. theintegrityandreliabilityofthefinalreconstructed
image[10].
Slice-to-volumeregistrationisdefinedasthepro-

### Slice-to-Volume Registration

cessofaligningatwo-dimensional(2D)image I with
athree-dimensional(3D)volume J. Theobjectiveis
In the past 15 years, numerous studies in the field to determine a transformation function Θˆ that best
of SVR have tackled the challenge of fetal motion aligns the 2D tomographic slice I to the 3D voluthroughretrospectivecorrection[10]. Rousseauetal. metricimage J. Thisalignmentisachievedbymini-
[4]initiallyselectsalow-resolutionMRIstacktoes- mizinganobjectivefunctionasoutlinedinEquation
tablish a global coordinate system, and then aligns 1:
eachsubsequentstacktothisreference[4]. Following
thecorrectionofinter-slicemotions,ahigh-resolution Θˆ =argminM(I,J;Θ)+R(Θ) (1)
3Dvolumeisreconstructedusingscatteredinterpola- Θ
tion. Kimetal.[11]introducedamethodfor3Dvol- In the aforementioned equation, M signifies the
umereconstruction,whichinvolvesco-aligningmul- image similarity term, commonly known as the
tiple 2D stacks and employing Gaussian weighting matchingcriterion. Thistermevaluatesthesimilarity
forvolumetricreconstruction. Ebneretal.[13]devel- between the 2D image and its corresponding slice
opedatwo-stepiterativeSVRandoutlier-robustSRR inthe3Dvolume,predominantlybasedonintensity
method,facilitatingrapidhigh-resolutionreconstruc- informationordistinctivestructuralfeaturespresent
tioninstandardspace. Sobotkaetal.[9]introduced in I and J. Concurrently, R symbolizestheregularanautomatedmotioncorrectionandvolumetricre- izationterm,whichappliesconstraintstoguarantee
constructionframework,subsequentlyreleasingitas awell-definedsolution. Thistermisparticularlypivanopen-sourceprojectnamedNiftyMIC.Thisframe- otalingoverningthegeometriccharacteristicsofthe
workinitiallygeneratesahigh-resolutionreference transformationmodel,especiallycrucialinscenarios
through Outlier-robust SRR with L2 regularization involvingnon-rigidregistration[10].
[12],thenperformsslice-wisealignmentbetweenthe Theclassificationoftheregistrationprocessasei-
High-ResolutionVolumeandeachstack,culminating therrigidornon-rigidhingesonthepermissibledeinaxialstackvolumetricreconstructionusingHuber formationsinimage I oritscorrespondingreformed
L2regularization. slicefrom J. Inrigidslice-to-volumeregistration,the
Thepipelinefor3DSVRfetalbrainreconstruction transformationisconfinedtorigidmotions,typically
is comprehensively depicted in Figure 1 [10]. The incorporating six degrees of freedom. Conversely,
processinitiateswiththeglobalalignmentofinput non-rigidregistrationallowsformoreintricatetransimagestackswithinthedesignatedbrainregion,es- formations,encompassingdeformationsoradvanced
tablishingamaskedareaforfocusedanalysis. This lineartransformationssuchasaffinetransformations
initialphaseculminatesinthecreationofaprelimi- [8].
naryaverage3Dimage,designatedasStep0inthe Theselectionofaregularizerinthefunction R is
methodology. contingent upon the specific transformation model
Subsequently,theprocedureprogressestoStep1, employed. Whilesimplermodels,suchasrigidbody
where each 2D slice undergoes a process of rigid transformations, may be estimated even in the abregistration against the current estimate of the 3D senceofaregularizer,morecomplexnon-rigidmodimage. Thisstepensuresthateachsliceisaccurately elsnecessitatetheinclusionof R toensuretherealalignedinthree-dimensionalspace,contributingto ismofthetransformations. Inthecontextofslice-totheoverallfidelityofthereconstruction. volumeregistration,thisregularizercanimposepla-
Followingthis,Step2involvesthesuper-resolution narity constraints (in situations where out-of-plane
reconstruction of a new, enhanced 3D image. This deformations are restricted) or can limit the extent
isachievedbyintegratingallthealignedslices,thus ofout-of-planedeformationstoyieldplausibleout-
2

<!-- Page 3 -->

Figure1: 3DSVRreconstructionpipelineforfetalbrainMRI.ThisfigureisbasedontheMRIdatasetfromSt.Thomas’Hospital,
London[10],seetheoriginalpaperathttps://pubmed.ncbi.nlm.nih.gov/35834425.
comes[8]. Furthermore,whenrelevant,incorporat- However,theseapproachesarecomputationallydeing knowledge about the tissue’s elasticity into the mandingduetotheirrelianceoniterativenumerical
regularizer can enhance the model’s accuracy. The optimizationinthetestingphase. Alternatively,ageultimateobjectiveistooptimizetheenergyasdelin- matchedatlases,suchasthosereferencedin[27],can
eatedinEq. (1),identifyingthemostprecise Θˆ that beusedasreferencevolumes. Atlas-basedregistraaligns the 2D and 3D images both effectively and tion methods, detailed in [26, 28], are also possible,
realistically. buttheircomputationalintensitylimitstheirapplica-
Whiletraditionaliterativemethodsformotioncor- bilityinreal-timescenarios.
rectionandreconstructionhaveshowneffectiveness, Accurate motion correction remains a significant
theyarehinderedbytwomajorlimitations: theinabil- challengeinthefield. Supervisedlearninghasbeen
itytoaccuratelyestimatelargemotions,andaheavy explored in 2D/3D registration, with some studies
relianceonpreciselysettinginitialtransformationpa- proposing metric learning approaches to develop
rameters[14]. Furthermore,thesimilaritymeasures customizedsimilaritymeasuresthroughsupervised
optimizedintheseintensity-basedmethodsoftenex- learning[29,30].
hibitahighlynon-convexnature. Thisaspectgreatly
increasestheriskoftheoptimizerbeingtrappedin
local maxima, thus restricting the capture range of Deep Learning Methods
thesetechniques[18].
The capture range of SVR is notably limited, pri- Deep Learning-Based Motion Correction methods
marily because it depends on iteratively optimized treattheentireMRIscanningprocedureasaninputintensity-based similarity metrics. These metrics output system, as depicted in Figure 2. Typically,
servemerelyasproxiesforaligningslicestoarefer- these methods operate within the image domain,
ence volume, without ensuring accurate alignment. wherethetrainingprocessinvolvesusingamotion-
Thepresenceofamotion-freereferencevolumeisnot corrupted image as input and a motion-free image
always guaranteed. To broaden the capture range, as the target label. Crucially, since the characterisonecanemploystrategieslikegridsearchonrotation tics of motion artifacts vary depending on the moparameters along with multi-scale registration [26]. tiontype,moststudiesnarrowtheirfocustospecific
3

<!-- Page 4 -->

types of motion [31]. During the training phase, enhancingtheeffectivenessofmotioncorrection. The
thesetechniquesaredesignedtorecognizepatterns frameworkfeaturesamulti-outputnetworkdesigned
between images affected by motion and those free tosimultaneouslypredicttransformationparameters
from motion artifacts. When encountering a new, andsegmentationresults,whicharethenprocessed
motion-distortedimage,thesystemaimstopredict throughacommonencoderstructureandashared
and produce a corrected version [32]. Such meth- representationmoduletorefineboththepredictions
odsusuallyconcentrateonparticularmotionartifact andsegmentationoutcomes[17].
types,predominantlycategorizedintorigidandnonrigidmotions. Long Short-Term Memory Networks

### Non-rigidorelasticmotion,oftenduetophysiolog-


### Singh, Salehi, and Gholipour [19] firstly proposed

ical factors, can be classified into two main groups:
a deep predictive motion tracking framework utiperiodic/continuous motions (such as respiration,
lizingLongShort-TermMemory(LSTM)Networks.
cerebrospinalfluidflow,andperistalsis)andabrupt
This approach marks a departure from the static
involuntaryactions(likeswallowing)[31].
3D pose estimation methods commonly found in

### Conversely,rigidmotioniscausedbyinvoluntary

[16, 18], focusing instead on dynamic, real-time 3D
or deliberate movements of the subject, and is fremotion tracking within MRI contexts. In contrast
quently observed across various body parts, espeto traditional motion tracking methodologies, their
cially in the brain [33]. It is more commonly found
frameworkdirectlyaddressesthe3Drigidmotionof
innon-compliantsubjects,includingchildrenorinanatomyinthescannerorworldcoordinatesystem,
dividualswithdegenerativeneurologicaldisorders
usingtime-sequentiallyacquiredslicestacks.
likeParkinson’s[33]. Rigidmotionischaracterized
The process begins with the extraction of spatial
bysixparameters,encompassingthreetranslational
featuresfromsequencesofinputimagesusingConand three rotational movements. These motion pavolutionalNeuralNetworks(CNNs). Thesefeatures
rametersareinferabledirectlyfromtherawdataby
arethenencodedusingLSTM,whichsubsequently
minimizing motion-induced image quality metrics
estimates objectives for the given images. This proordataconsistencyerrors. However,applyingthese
cessresultsinthecreationofacontextvector,utilized
methods in clinical MRI settings poses challenges
by LSTM decoders to perform regression against
duetothenon-convexnatureoftheparameterestiangle-axisrepresentationandtranslationoffset,theremationprocessandtheextensivecomputationtime
fore enabling the accurate prediction of 3D rigid
involved[34].
body motion. To prevent overfitting to either rotationortranslationparameters,thenetworkincor-

### Convolutional Neural Networks

poratesmultiplerepresentationheads. Additionally,
Inrecentyears,toincreasethecapturedmotionrange theframeworkemploysamulti-steppredictionstratandacceleratefetalMRIvolumereconstruction,neu- egy,whereintheoutputofapreviousdecoderisfed
ralnetwork-basedmethodslikeCNNhavebeenpro- as input to the current decoder, combined with the
posed to predict the motion of fetal brain MRI 2D contextvector. Thenetworksweretrainedandtested
slices. Miao,Wang,andLiao[18]proposedaCNN- on sequences containing masked slices, which repbasedregressiontechnique,termedPoseEstimation resent slices lost due to intermittent fast intra-slice
via Hierarchical Learning (PEHL). This method is motion.
designedtofacilitatereal-time2-D/3-Dregistration,
boasting a broad capture range and high accuracy. Transformers

### WhileprimarilyfocusingonX-rayattenuationasob-

TheTransformerarchitecture,renownedforitsprofiservedinCTimaging,thisapproachisalsoadaptable
ciencyindynamicallyhighlightingrelevantfeatures
forMRIapplications.
ininputsequencesthroughtheself-attentionmecha-
Salehietal.[16]expandeduponthe3Dposeestinism,hasdemonstratedexceptionalabilityinmodelmationnetwork,adaptingitforusewitharbitrarily
inglong-distancedependenciesandcapturingglobal
oriented objects in slice-to-volume and volume-tocontext[35].
volumeregistrationtasks. Thisadaptationinvolved
Formally,thetransformerusestheconceptofselftheuseofCNNstrainedtopredicttheangle-axisrepattention[35],whichallowseachpositionintheinput
resentationof3-Drotationsandtranslations,based
sequence to attend to all positions in the previous
onimagefeatures,whichisparticularlyrelevantfor
layerofthesequence. ThisismathematicallyreprefetalbrainMRI.Meanwhile,Peietal.[17]introduced
sentedas:
amulti-tasklearningframeworkforfetalMRIstacks.
This framework combines the positional data and
(cid:18) QKT(cid:19)

### Attention(Q,K,V) =softmax √ V (2)

tissue segmentation maps of each 2D slice, thereby d
k
4

<!-- Page 5 -->

Figure 2: AflowchartdepictingCNN-basedmotioncorrectiontechniquesfromtheworkinChangetal.[32]. Initially, motioncorruptedimagesareinputintoanetwork,whichthenoutputsmotion-freeimages. Fortrainingthedeeplearningmodel,numerous
pairs of motion-corrupted and motion-free images are processed through the network. Subsequently, in the correction phase, a
motion-correctedimageisproducedbyinputtingamotion-corruptedimage. Thisprocessultimatelyresultsinthegenerationofa
motion-freeimage,seetheoriginalpaperathttps://www.sciencedirect.com/science/article/pii/S2950162823000012.
In this equation, Q, K, and V represent the queries, [21].
keys,andvalues,respectively. Theseareallvectors
obtainedbytransformingtheinputvectors. d isthe
k √

### Generative Adversarial Networks

dimensionofthekeyvectors. Thescalingfactor d
k
isusedtopreventthedotproductsfromgrowingtoo
CNNs,knownfortheirrobustfeatureextractioncalarge in magnitude, which could lead to instability
pabilities,havemadesubstantialcontributionstoreinthesoftmaxfunction.
ducingmotionartifactsinMRIimaging. However,a

### The output of the attention mechanism is then

limitationarisesintheformofblurredimages,aconpassedthroughaseriesoffeed-forwardneuralnetsequenceoftheirstrategytominimizetheEuclidean
works. Each of these networks is applied to each
distancebetweennoisyandground-truthimages[22].
positionseparatelyandidentically. Thispartofthe
Thisapproach,whilemathematicallysoundinpixel
transformerisrepresentedas:
space,oftenfallsshortintermsofvisualperception,
leadingtoless-than-optimalimagequality[23].

### FFN(x) =max(0,xW +b )W +b (3)

1 1 2 2 Toovercometheselimitations,GenerativeAdverwhere x istheinputtothefeed-forwardnetwork, sarial Networks (GANs) have been identified as a
W and W are weight matrices, and b and b are promisingtechnologicaladvancement. Arecentcon-
1 2 1 2
biasvectors. TheReLUactivationfunction(denoted tribution to this area is the work of Lim et al. [23],
asmax(0,·))isappliedelement-wise. Thistwo-layer whointroducedanovelGANarchitecturedesigned
feed-forward network is applied to each position’s specifically for correcting motion artifacts in fetal
outputfromtheattentionlayer,effectivelyallowing MRIimages.
the model to integrate information from different GANsfunctionthroughadual-networkstructure,
positionsoftheinputsequence. comprisingaGeneratorandaDiscriminator. These
This attention capability is particularly pertinent networks are trained sequentially and interactively.
inthecontextofSVRforfetalMRI,wheretheinput TheDiscriminator’sprimaryfunctionistodevelop
comprisesmultiplestacksofslices. Thesestackscan a loss function capable of distinguishing between
beconceptualizedasasequenceofimages,allowing authenticandartificialimages. Meanwhile,theGenfor the joint processing of multi-view information erator,operatingasagenerativemodel,aimstoprofromdifferentorientationstofacilitatetheSVRtask. duceartificialimagessoconvincinglyrealthatthey
Xu et al. [20] introduced the Slice-to-Volume Regis- deceivetheDiscriminator.
tration Transformer (SVoRT), which maps multiple InthecontextofLimetal.[23]work,theGenerastacks of fetal MR slices into a canonical 3D space. toristaskedwithtransformingamotion-corrupted
ThismappingservesasaninitializationstepforSVR image into a version free of motion artifacts. This
and 3D reconstruction. Building on this, NeSVoR isachievedbytheGeneratorproducingacorrected
hasfurtherenhancedthevolumetricreconstruction image, which is then combined with the original
processbyincorporatingimplicitneuralinformation motion-corruptedimagetocreatea"fake"imagepair.
5

<!-- Page 6 -->

Conversely,a"real"imagepairisformedbyconcate- asfollows:
natingagroundtruth(motion-free)imagewiththe

## T

sameoriginalmotion-corruptedimage. Thisprocess p θ (x 0:T ) = p(x T ) ∏ p θ (x t−1 |x t ) (5)
ofpairingtheimages,particularlytheintegrationof t=1
themotion-corruptedimage,servesacrucialrole. It
ScorePerspective ModelsemployingtheScorePerprovidesauxiliaryinformationtotheDiscriminator,
spective utilize a maximum likelihood-based estienablingittomoreeffectivelyidentifyandpenalize
mation approach, which involves using the score
inaccuraciesintheGenerator’soutput.
functionofthedata’slog-likelihoodtoestimateparameters in diffusion processes. Two notable sub-
Diffusion Model categorieswithinthisdomainareNoise-conditioned
Score Networks (NCSNs) [38] and Stochastic Dif-

### Diffusionmodelsrepresentapioneeringcategoryin

ferentialEquations(SDEs)[39]. NCSNsspecifically
generativemodeling,showcasingexceptionalefficacy
focusonestimatingthederivativeofthelogdensity
in capturing complex data distributions. Although
functionforperturbeddatadistributionsatvarying
a recent development in generative learning, these
noise levels. Conversely, SDEs represent a broader
modelshaveprovenbeneficialacrossavarietyofapgeneralizationofthesemethodologies,encompassing
plications. Basedondifferencesinapproaches,they
characteristicsofbothDDPMsandNCSNs.
canbebroadlycategorizedintotwotypes: theVariationalPerspective[36,24]andtheScorePerspective ApplicationinMotionCorrection Althoughdiffu-
[37,38,39,25]. Wewillexaminethemodelswithin sionmodelshavenotyetbeendirectlyimplemented
each category, including DDPMs under the Varia- infetalMRImotioncorrection,severalrelatedstudtionalPerspectiveandNCSNsandSDEsunderthe ies hold potential for such applications. Xie and Li
ScorePerspective. [24] developed ameasurement-conditioned denoisingprobabilisticmodel(MC-DDPM),anextensionof
Variational Perspective The Denoising Diffusion

### DDPM,whichdemonstratedimpressivecapabilities

Probabilistic Model (DDPM) [36] is an innovative
inreconstructingunder-sampledMRimages. Such
approach in the realm of unconditional generative
workcouldbepotentiallyadaptedforfetalbrainMRI
models. ItemploystwodistinctMarkovchains: aforvolumetric reconstruction. Levac, Jalal, and Tamir
wardchainthatprogressivelydistortsdataintonoise,
[25] employed a score-based generative model that
andareversechainthattransformsnoisebackinto
calculates the log probability of reconstruction for
data. Theforwardchainistypicallydesignedtoconthe motion-corrupted MR images. Both motion pavertanydatadistributionintoasimple,predefined
rametersandtheunderlyingimageareoptimizedto
priordistribution(suchasastandardGaussian). Conidentifyasolutionthatnotonlyalignswiththedata
versely, the reverse chain, powered by deep neural
butalsopossessesahighpriorprobabilityasperthe
networks,learnstoinverttheforwardchain’stransgenerativemodel’sframework.
formations. Generation of new data points begins
by sampling a random vector from the prior distribution,followedbyancestralsamplingthroughthe Conclusions
reverseMarkovchain[40].
Consider a data sample x 0 ∼ q(x 0 ). A for- The analysis of various methodologies reveals that
wardnoisingprocess p generateslatentvariables x 1 the issue of motion correction in MRI is inherthrough x T byincrementallyaddingGaussiannoise ently complex and can be approached from mulat each time step t. This process is mathematically tiple perspectives. While traditional methods such
definedas: as SVR have proven effective, deep learning-based
(cid:16) (cid:112) (cid:17) approaches have demonstrated superior precision
q(x t |x t−1 ) = N x t ; 1−β t ·x t−1 ,β t ·I (4) androbustnessinhandlingvarioustypesofmotion.

### Theyexcelatmodelingtheintricatenon-linearrela-

Here, T denotesthetotalnumberofdiffusionsteps, tionshipsbetweenmotion-corruptedandmotion-free
and β 1 ,...,β T ∈ [0,1) representsthevariancesched- images. Notably,generativemodelslikeGANsand
ule across these steps. I is the identity matrix, DiffusionModelsareadvancingtowardmoreaccuand N(x;µ,σ)signifiesthenormaldistributionwith rate reconstruction of corrupted images. However,
mean µ andcovariance σ. they often operate in a ’black-box’ manner, raising
Building on the aforementioned concepts, the re- concerns about their lack of transparency, an issue
verse process can be formulated to approximate thatwarrantsfurtherexplorationandresolution.
a sample from q(x ). Starting with p(x ) = Emerging deep learning models, like Transform-

## 0 T

N(x ;0,I),thereverseprocesscanbeparameterized ers,GenerativeAdversarialNetworks,andDiffusion

## T

6

<!-- Page 7 -->

Models,haveshownpromiseinthefieldofmedical [11] KioKimetal.“Intersectionbasedmotioncorimaging. DespitetheirinitialdevelopmentforMRI rectionofmultisliceMRIfor3-Dinuterofetal
reconstruction enhancement, there is potential for brain image formation”. In: IEEE transactions
theirapplicationinmotioncorrection. Especiallyfor onmedicalimaging29.1(2009),pp.146–158.
diffusionmodels,whichgeneratesamplesthrougha
[12] Michael Ebner. “Volumetric MRI ReconstruclengthyMarkovchainofdiffusionsteps,arepartictionfrom2DSlicesinthePresenceofMotion”.
ularly noteworthy. These innovative deep-learning

### PhDthesis.UCL(UniversityCollegeLondon),

models are likely to significantly enhance motion
2019.
correctiontechniquesinfutureresearchendeavors.
[13] Michael Ebner et al. “An automated frameworkforlocalization,segmentationandsuper-
References resolution reconstruction of fetal brain MRI”.
In:NeuroImage206(2020),p.116324.
[1] Naya Juul-Dam, Jeanne Townsend, and Eric
[14] Benjamin Hou et al. “3-D reconstruction in
Courchesne. “Prenatal, perinatal, and neonacanonical co-ordinate space from arbitrarily
talfactorsinautism,pervasivedevelopmental
oriented2-Dimages”.In:IEEEtransactionson
disorder-nototherwisespecified,andthegenmedicalimaging37.8(2018),pp.1737–1750.
eralpopulation”.In:Pediatrics107.4(2001),e63–
[15] Benjamin Hou et al. “Predicting slice-toe63.
volume transformation in presence of arbi-
[2] Penny Gowland. “Safety of fetal MRI scantrarysubjectmotion”.In:MedicalImageComputning”.In:FetalMRI (2011),pp.49–54.
ingandComputer-AssistedIntervention-MICCAI
[3] Shuzhou Jiang et al. “MRI of moving sub- 2017:20thInternationalConference,QuebecCity,
jects using multislice snapshot images with QC,Canada,September11-13,2017,Proceedings,
volume reconstruction (SVR): application to PartII20.Springer.2017,pp.296–304.
fetal, neonatal, and adult brain studies”. In:
[16] Seyed Sadegh Mohseni Salehi et al. “Real-
IEEEtransactionsonmedicalimaging26.7(2007),
timedeepposeestimationwithgeodesicloss
pp.967–980.
for image-to-template rigid registration”. In:
[4] Francois Rousseau et al. “Registration-based IEEEtransactionsonmedicalimaging38.2(2018),
approachforreconstructionofhigh-resolution pp.470–481.
inuterofetalMRbrainimages”.In:Academic
[17] Yuchen Pei et al. “Anatomy-guided convoluradiology13.9(2006),pp.1072–1081.
tional neural network for motion correction
[5] MarkHedleyandHongYan.“Motionartifact in fetal brain MRI”. In: Machine Learning in
suppression:areviewofpost-processingtech- Medical Imaging: 11th International Workshop,
niques”. In: Magnetic resonance imaging 10.4 MLMI2020,HeldinConjunctionwithMICCAI
(1992),pp.627–635. 2020,Lima,Peru,October4,2020,Proceedings11.
[6] Michael K Stehling, Robert Turner, and Peter Springer.2020,pp.384–393.
Mansfield.“Echo-planarimaging:magneticres- [18] Shun Miao, Z Jane Wang, and Rui Liao. “A
onanceimaginginafractionofasecond”.In: CNNregressionapproachforreal-time2D/3D
Science254.5028(1991),pp.43–50. registration”. In: IEEE transactions on medical
[7] Sahar N Saleem. “Fetal MRI: An approach to imaging35.5(2016),pp.1352–1363.
practice: A review”. In: Journal of advanced re- [19] Ayush Singh, Seyed Sadegh Mohseni Salehi,
search5.5(2014),pp.507–523. and Ali Gholipour. “Deep predictive motion
[8] Enzo Ferrante and Nikos Paragios. “Slice-to- trackinginmagneticresonanceimaging:applivolumemedicalimageregistration:Asurvey”. cation to fetal imaging”. In: IEEE transactions
In:Medicalimageanalysis39(2017),pp.101–123. onmedicalimaging39.11(2020),pp.3523–3534.
[9] Daniel Sobotka et al. “Motion correction and [20] JunshenXuetal.“SVoRT:iterativetransformer
volumetric reconstruction for fetal functional for slice-to-volume registration in fetal brain
magnetic resonance imaging data”. In: Neu- MRI”.In:InternationalConferenceonMedicalImroImage255(2022),p.119213. age Computing and Computer-Assisted Intervention.Springer.2022,pp.3–13.
[10] AlenaUUusetal.“Retrospectivemotioncorrection in foetal MRI for clinical applications: [21] Junshen Xu et al. “NeSVoR: Implicit Neural
existingmethods,applicationsandintegration RepresentationforSlice-to-VolumeReconstrucintoclinicalpractice”.In:TheBritishjournalof tion in MRI”. In: IEEETransactionsonMedical
radiology96.1147(2023),p.20220071. Imaging(2023).
7

<!-- Page 8 -->

[22] PhillipIsolaetal.“Image-to-imagetranslation [33] FrankGodenschwegeretal.“Motioncorrection
withconditionaladversarialnetworks”.In:Pro- inMRIofthebrain”.In:Physicsinmedicine&
ceedingsoftheIEEEconferenceoncomputervision biology61.5(2016),R32.
andpatternrecognition.2017,pp.1125–1134.
[34] KamleshPawaretal.“MoCoNet:Motioncor-
[23] AdamLimetal.“Motionartifactcorrectionin rectionin3DMPRAGEimagesusingaconvofetal MRI based on a Generative Adversarial lutional neural network approach”. In: arXiv
networkmethod”.In:BiomedicalSignalProcess- preprintarXiv:1807.10831(2018).
ingandControl81(2023),p.104484.
[35] Ashish Vaswani et al. “Attention is all you
[24] YutongXieandQuanzhengLi.“Measurement- need”. In: Advances in neural information proconditioned denoising diffusion probabilistic cessingsystems30(2017).
modelforunder-sampledmedicalimagerecon-
[36] JonathanHo,AjayJain,andPieterAbbeel.“Destruction”. In: InternationalConferenceonMednoisingdiffusionprobabilisticmodels”.In:AdicalImageComputingandComputer-AssistedInvancesinneuralinformationprocessingsystems33
tervention.Springer.2022,pp.655–664.
(2020),pp.6840–6851.
[25] Brett Levac, Ajil Jalal, and Jonathan I Tamir.
[37] AmirhosseinKazerounietal.“Diffusionmod-
“AcceleratedmotioncorrectionforMRIusing
elsformedicalimageanalysis:Acomprehenscore-basedgenerativemodels”.In:2023IEEE
sivesurvey”.In:arXivpreprintarXiv:2211.07804
20thInternationalSymposiumonBiomedicalImag-
(2022).
ing(ISBI).IEEE.2023,pp.1–5.
[38] Yang Song and Stefano Ermon. “Generative
[26] VahidTaimourietal.“Atemplate-to-sliceblock
modeling by estimating gradientsof the data
matchingapproachforautomaticlocalization
distribution”.In:Advancesinneuralinformation
ofbraininfetalMRI”.In:2015IEEE12thInterprocessingsystems32(2019).
nationalSymposiumonBiomedicalImaging(ISBI).
[39] YangSongetal.“Score-basedgenerativemod-
IEEE.2015,pp.144–147.
elingthroughstochasticdifferentialequations”.
[27] Ali Gholipour et al. “A normative spatiotem-
In:arXivpreprintarXiv:2011.13456(2020).
poral MRI atlas of the fetal brain for auto-
[40] DaphneKollerandNirFriedman.Probabilistic
maticsegmentationandanalysisofearlybrain
graphical models: principles and techniques. MIT
growth”.In:Scientificreports7.1(2017),p.476.
press,2009.
[28] SébastienTourbieretal.“Automatedtemplatebasedbrainlocalizationandextractionforfetal
brainMRIreconstruction”.In:NeuroImage155
(2017),pp.460–472.
[29] Michael M Bronstein et al. “Data fusion
throughcross-modalitymetriclearningusing
similarity-sensitivehashing”.In:2010IEEEcomputer society conference on computer vision and
patternrecognition.IEEE.2010,pp.3594–3601.
[30] FabriceMicheletal.“Boostedmetriclearning
for 3D multi-modal deformable registration”.
In:2011IEEEInternationalSymposiumonBiomedical Imaging: From Nano to Macro. IEEE. 2011,
pp.1209–1214.
[31] Seul Lee et al. “Deep learning in MR motion
correction: a brief review and a new motion
simulation tool (view2Dmotion)”. In: InvestigativeMagneticResonanceImaging24.4(2020),
pp.196–206.
[32] Yuchou Chang et al. “Deep learning-based
rigidmotioncorrectionformagneticresonance
imaging:Asurvey”.In:Meta-Radiology(2023),
p.100001.
8