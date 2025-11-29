---
title: "Dialogue State Tracking"
original_file: "./Dialogue_State_Tracking.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["llm", "rag", "chain-of-thought", "fine-tuning", "evaluation"]
keywords: ["cid", "style", "page", "image", "painting", "dublin", "ireland", "structure", "content", "appearance"]
summary: "<!-- Page 1 -->

DiffArtist: Towards Structure and Appearance Controllable Image

### Stylization


### RuixiangJiang ChangWenChen

rui-x.jiang@connect.polyu.hk chen.changwen@polyu.edu.hk
TheHongKongPolytechnicUniversity TheHongKongPolytechnicUniversity

### HongKong,China HongKong,China


### Abstract Structure style strength


### Artisticstylesaredefinedbyboththeirstructuralandappearance

elements.Existingneuralstylizationtechniquesprimarilyfocuson
transferringappearance-levelfeaturessuchasco"
related_documents: []
---

# Dialogue State Tracking

<!-- Page 1 -->

DiffArtist: Towards Structure and Appearance Controllable Image

### Stylization


### RuixiangJiang ChangWenChen

rui-x.jiang@connect.polyu.hk chen.changwen@polyu.edu.hk
TheHongKongPolytechnicUniversity TheHongKongPolytechnicUniversity

### HongKong,China HongKong,China


### Abstract Structure style strength


### Artisticstylesaredefinedbyboththeirstructuralandappearance

elements.Existingneuralstylizationtechniquesprimarilyfocuson
transferringappearance-levelfeaturessuchascolorandtexture,
oftenneglectingtheequallycrucialaspectofstructuralstylization.
Toaddressthisgap,weintroduceDiffArtist,thefirst2Dstylizationmethodtoofferfine-grained,simultaneouscontroloverboth
structureandappearancestylestrength.Thisdualcontrollability
isachievedbyrepresentingstructureandappearancegeneration
as separate diffusion processes, necessitating no further tuning
oradditionaladapters.Toproperlyevaluatethisnewcapability
ofdualstylization,wefurtherproposeaMultimodalLLM-based
stylizationevaluatorthatalignssignificantlybetterwithhuman
preferencesthanexistingmetrics.Extensiveanalysisshowsthat
DiffArtistachievessuperiorstylefidelityanddual-controllability
comparedtostate-of-the-artmethods.Itstext-driven,training-free
designandunprecedenteddualcontrollabilitymakeitapowerfulandinteractivetoolforvariouscreativeapplications.Project
homepage:https://diffusionartist.github.io.

### CCSConcepts

•Computingmethodologies→Appearanceandtexturerepresentations;Imagemanipulation;•Appliedcomputing→Fine
arts.

### Keywords

Generativeart;Text-drivenstylization;Structureandappearance;
Stylizationevaluation;MultimodalLLMapplications

### ACMReferenceFormat:

RuixiangJiangandChangWenChen.2025.DiffArtist:TowardsStructure
andAppearanceControllableImageStylization.InProceedingsofthe33rd
ACMInternationalConferenceonMultimedia(MM’25),October27–31,2025,
Dublin,Ireland.ACM,NewYork,NY,USA,24pages.https://doi.org/10.1145/
3746027.3755010
1 Introduction
Theessenceofanartisticstyleliesnotonlyinitsappearance—color
andtexture—butalsoitsstructure—geometryandcomposition[17,
18,30].Forexample,thefragmentationoffiguresinPicasso’sCubistworksandtheundulatingskyinVanGogh’s“StarryNight”,
eachcontributingdistinctlytotheirartisticexpression.Existing
ThisworkislicensedunderaCreativeCommonsAttribution4.0InternationalLicense.

### MM’25,Dublin,Ireland

©2025Copyrightheldbytheowner/author(s).

## Acmisbn979-8-4007-2035-2/2025/10

https://doi.org/10.1145/3746027.3755010
htgnerts
elyts
ecnaraeppA
Figure1:DiffArtistenablesdisentangledandfine-grained
controlofstylestrengthfromtwoorthogonalperspectives:
structureandappearance.Thestylepromptis“TheDream,
byPicasso.”
neuralstylizationapproaches[10,11,24,25,37,56]predominantly
focusonmanipulatingappearance-levelattributes.Thestructural
elementsinthesourceimage,however,areoftenviewedaspartof
“content”andareexplicitlypreserved[55,59,61,62].Thisfundamentallimitationpreventsthemfromcapturingthetrueessence
ofanartstyle,severelyrestrictingtheirexpressivepotentialand
customizability.

### Therootofthislimitationliesintheinherentcomplexityof

structuralstylization.Unlikeappearance-styletransfer,structural
stylizationrequiresadelicatebalancebetweenthreecompetingobjectives:(1)aligningwiththetargetstyle,(2)harmonizingwiththe
sourceimage’scomposition,and(3)preservingthecoresemantic
integrityofthecontent.Theseobjectivesoperateatahigh-level
semanticplane,exposingacriticalgapincurrentmethods.While
descriptors like AdaIN [25] and Gram loss [15] may suffice for
appearance-stylemodeling,thelackofadequatestructurerepresentationandstructure-styleevaluatorspresentssignificantobstacles
5202
guA
72
]VC.sc[
4v24851.7042:viXra

<!-- Page 2 -->

MM’25,October27–31,2025,Dublin,Ireland RuixiangJiangandChangWenChen
inthedevelopmentofstructuralstylizationtechniques.Thischal- (3) WepresentanovelMLLM-basedevaluatorforevaluating
lengeisamplifiedinrecentmultimodalgenerationscenarios,where structureandappearanceinartisticstylization,whichaligns
astylepromptoffersnoexplicitvisualtemplate[10,22,24,53]. betterwithhumanperception.
TheadventofDiffusionModels(DMs)offersapowerfulnew (4) ExtensiveexperimentsdemonstratethatDiffArtistachieves
paradigmforachievingthisdualcontrollability,astheirgenerative superiorstylizationfidelity,controleditability,anddisentansamplingprocessenablesfargreaterstructuralandappearance glementthanexistingapproaches.
diversitythanpriormethods.Thisreframesstylizationasaconditionalgenerationtask,guidedbyasourceimageandastyleprompt
2 RelatedWorks
(imageortext).However,thisgenerativepowercomeswithacritical,unaddressedchallenge:thediffusionprocessinherentlyentan- TheStylizationofStructureand/orAppearance.Structureand
glesthegenerationofstructureandappearance.Weidentifythis appearancecollectivelydefinethestyleofavisualrepresentation.
asafundamentalStructure-Appearance(S-A)Tradeoff:intensi- Existingneuralstylizationmethods[10,11,24,25,37,56]haveprefyingstructuralchangesinadvertentlycorruptsappearancestyle, dominantlyfocusedonappearancestylization,generallyachieved
whilestrengtheningappearancewashesoutstructuraltransforma- viaanencoder-decoderarchitecture.Onlyafewpapers[33,71]
tions.Thistradeoffdirectlyexplainsthecorefailuresofexisting focusontransferringstructuralstylecomponentsbetween2Dimdiffusion-basedmethods,whichareeitherpronetoseverecontent ages.Thisisusuallyaccomplishedbycalculatingacorrespondence
degradation[8,44,55]orsufferfromweak,constrainedstyliza- betweencontentandstyleimageandperforminganon-rigiddetion[58,62].Achievingdualcontrollabilityinthestylizationthus formation.However,thesemethodstypicallyoperateonimages
remainsanopenquestion. inspecificdomainslikeportraits,requiringanin-domainstylized
Tosolvethis,weintroduceDiffArtist,thefirstframeworkto reference.Moreover,theydonotenabledualcontrollability.Very
ourknowledgethatoffersexplicit,disentangledcontroloverboth recently,dualcontrollabilityhasbeenexploredinCtrl-X[42],but
structureandappearancein2Dstylization.Atitscore,DiffArtist itsframeworkisdesignedforlocalized,imageeditsratherthanthe
explicitlydisentanglesthestructuralandappearancegeneration global,harmoniousstyletransformations.Meanwhile,theconcept
asseparateddiffusionprocesses,withsharedsemanticinforma- ofdisentangledcontrolisexploredin3Dsynthesis,whereexplicit
tion.ThisdesigndirectlyovercomesthefundamentalS-Atradeoff representationsofshape(e.g.,meshes[45]andradiancefields[53])
andfunctionsasazero-shot,plug-and-playmoduleforanypre- andappearance(e.g.,texturemapping[5])makeseparationnatural.
trained U-Net-based DM, requiring no costly fine-tuning or ex- Thesuccessin3D,however,isnotdirectlytransferabletothe2D
ternaladapters [63, 66]. As evidencedin thispaper,this design domainduetothelackofexplicitgeometricpriorsinsingleimprovidestruedisentanglement—akeyadvantageoverControlNet- ages.Inthispaper,weexplorethefirstdualcontrollable2Dimage
basedmethods[42,54]whereadjustingonestylefactoradversely stylizationmethod.
impactstheother.AsdemonstratedinFig.1,thisunprecedented Text-Driven Image Stylization. Text-driven image stylizalevelofcontrolallowsDiffArtisttoachievestrong,semantically tion aims to stylize a source image according to style prompts.
coherentstylization,unleashingthefullcreativepotentialofdual- Earlymethodsachieveitbyoptimizingcertainimagerepresenstylecustomization. tation[13,32,37,45,53]withamultimodalalignmentobjective,
Evaluatingthisnovelcapabilityofdualcontrolrequiresunder- typicallyimplementedastheCLIPloss[48].Recently,itwasdisstandingonimagesemantics,whereexistingevaluationmetrics coveredthattext-to-image(T2I)DMscouldalsobeadaptedfor
obsolete.Thisexposesacriticalneedforanewevaluationpara- similaroptimizationschemes[20,29,31,47].Theseoptimizationdigm.Toaddressthis,weintroduceoursecondmajorcontribution: basedmethodsarecostlyandslow,motivatingrecentexploration
aMultimodalLLM(MLLM)-basedevaluatordesignedfordual ofthefeed-forwardparadigm.Instruct-Pix2Pix[4]tunesthedifstylization.Wearguethatanysuchevaluatormustsatisfythree fusionmodelalongwithalanguagemodelforgeneralizedediting
keycriteria:(1)operateatahigh-levelsemanticplanetoassess tasks.Diffstyler[24]learnacontentandstyle-specificdenoiserfor
structure,(2)possesscontextualawarenesstomaintainsemantic disentanglement.FreeStyle[19]modulatestheU-Netfeaturefor
integrity, and (3) perform robust cross-modal association be- training-freestylization.Concurrentwiththisexplorationisthe
tweentextpromptsandvisualforms.Byleveragingthezero-shot stylizedimagegeneration[7,14,22,54,55].Whilerelated,theyforeasoningofMLLMs,ourproposedmetricmeetsthesecriteria.We cusonadifferentsettingwherethestyleisextractedfromanimage
empirically show that it aligns significantly better with human andthecontentisaprompt.Inthiswork,wefocusonthestructure
artisticjudgmentthanexistingstylizationmetrics[34,48,57],es- andappearancecontrolintext-drivenstylizationscenarios.
tablishingamorereliableandhuman-centricstandardforfuture QuantitativeEvaluationofStyleTransfer.Quantitatively
stylizationresearch. evaluating style transfer is a long-standing problem. Initial ap-
Wesummarizeourcontributionsasfollows: proachesrepurposedlow-levelmetrics,includingGramLoss[16],
LPIPS[67],andFID[23].However,recentliteraturefoundthatthese
metricsarefundamentallyincapableofcapturingtheholisticand
semanticqualitiesofhumanartisticperception[3,6,27,50,60,64].
(1) WeidentifytheS-Atradeoffindiffusionmodelsasthekey Inresponsetotheseshortcomings,art-specificevaluatorslikeArtchallengefordisentangleddualcontrollability. FID[60]andArtScore[6]weredevelopedtobetterquantifythe
(2) WeproposeDiffArtist,thefirst2Dstylizationmethodthat abstract concept of "artness". Nevertheless, they cannot handle
enablesthedualcontrollabilityofstructureandappearance. open-vocabularytext-drivenstylizationandlackthemechanismto

<!-- Page 3 -->

DiffArtist:TowardsStructureandAppearanceControllableImageStylization MM’25,October27–31,2025,Dublin,Ireland
“Cartoon doodle
style, bold lines”
inject

### Appearance

Style prompt 𝑦 Delegation 𝜏−1 steps skip hidden skip hidden
𝜖~𝒩 𝟎,𝐈

### Appearance


### Sampled noise control Appearance

Reference Structure delegation Main branch
Structure Control

### Structure

Delegation 𝜏−1 steps

### Source image 𝐱"

DDIM inversion Structure Structure SelfAttn S2A SelfAttn SelfAttn

### Reference inject AdaIN

control 𝑄% 𝐾% 𝑉% 𝑉# 𝐾# 𝑄# 𝐾$ 𝑄$ 𝑉$

### Main Structure Appearance Main

Branch delegation delegation branch
𝜏−1 steps Appearance Control
Noised image 𝐱! Pretrained denoising U-Net(Shared Param) Controlled Stylization𝐼!
Figure2:OverviewofDiffArtist.Ourmethoddisentanglesstylizationbyprocessingstructureandappearancethroughtwo
independentdiffusiontrajectories(delegations).Ateachdenoisingstep,themainstylizationbranchisconditionedonsemanticlevelfeaturesfromthestructureandappearancedelegations.AllthreebranchessharethesamepretrainedU-Netparameters,
andperformfulldenoisingof𝜏 steps.Theentireframeworkoperateswithoutrequiringanyfine-tuningoradapters.
evaluatestructureandappearanceseparately.Thispaperpropose astyleprompt𝑦).Specifically,onemaystartwithanintermediate
asemantic-levelMLLM-basedevaluatortoassessthestructureand stepx𝜏 (i.e.,controlpoint),where𝜏 ∈ [1,𝑇] foriterativeDDIM
appearancefidelity,whichalignsbetterwithhumanperception. sampling.Eachdenoisingstepisformulatedasfollows:
3 Methodology √
3.1 Objective:DisentangledDualControllability x𝑡−1 =
√
𝛼 𝑡−1
(cid:18) x𝑡 − 1−
√
𝛼
𝛼
𝑡 𝜖 𝜃(x𝑡 ,𝑡;𝑦)(cid:19)
𝑡
Givenasourceimage𝐼,atext-basedstyleprompt𝑦,andapre-
+
√
1−𝛼 𝑡−1 𝜖 𝜃(x𝑡 ,𝑡;𝑦), (1)
traineddiffusionmodelG(·),ourprimaryobjectiveistogeneratea
stylizedimage𝐼ˆthatpreservesthesemanticcontentof𝐼 whilehar- where𝜖 𝜃 isthedenoiser,𝑡 isthetimestep,and𝛼 1:𝑇 isapredefined
moniouslyembodyingthestyledescribedby𝑦.Thecoreinnovation
noiseschedule.Theassumptionofthisparadigmisthatwitha
wepursueisdisentangleddualcontrol,meaningthatdecompos- proper𝜏,theresultingstylizedimage𝐼ˆ:=xˆ0harmoniouslyinteingthestyleprompt𝑦intotwoorthogonalcomponents—structure
gratesthestructureandappearanceofstyleinprompt𝑦withthe
andappearance—andcontrollingtheirstrengthindependently.Our sourceimage𝐼.
definitionofstructureandappearanceina2Dimageismainly
basedonfineart[17].Aformaldefinitionofthemischallengingas
3.3 StructureandAppearanceinNoiseSpace
itrelatestovisualsemiotics[18,52],extendingbeyondthescopeof
thispaper.Generallyspeaking,structurecorrespondstotheshapes, Prevailingneuralstylizationmethodsarebuiltonaparadigmthat
likecontoursandcurvatures,whileappearancecorrespondstolocal separatesanimageinto“content”and“style”[12,25,36,39,49,58,
patterns,likestrokesandcolorpalettes.Wealsoaimtodevelop 68,69].Inthisview,thestyleusuallyreferstothefeaturemaps
anevaluatorE,whichcanevaluatethefidelityofstructureand extractedfromcertainlayersofaneuralnetwork.Toadvancestylappearancestyleinawayalignedwithhumanperception. izationtowardsbothstructureandappearancecontrollability,we
Theremainingpartsofthissectionareorganizedasfollows.In adoptdifferentmodelingthatdecomposesanimageasitsstructure
Sec.3.2,wereviewthebasicsofinversion-basedimagemanipula- andappearancecomponent 𝑠 s:x0 = 𝑎 G 0 (z 𝑠 0 ,z 𝑎 0 ),where G 0 = (·,·)
tion.InSec.3.3,3.4,weexplainthemotivationanddesignofcontrol isacompositionfunction,z 0 andz 0 arethelatentstructureand
atahighlevel,anddetailsaredescribedinSec.3.5.Sec.3.6outlines appearancefactorization,respectively.Thisisa“static”,image-level
theproposedMLLM-basedstructureandappearanceevaluators. perspective.Inthediffusionprocess,thedistributionofimage𝑥 0is
tiedwiththeintermediatedistributionsinx1:𝑇,wherethedenoiser
3.2 Preliminary:DDIMInversion
𝜖
𝜃
learnsthetransition𝑞 𝜃(𝑥
𝑡−1
|𝑥
𝑡
,𝑦)via𝜖-prediction.Therefore,
wepositsimilarfactorizationofpredictednoiseresidual,whichis
Tostylizeasourceimagex0:=𝐼 usingDMs,inversion-basedmetha“dynamic”decompositionacrossthefullfrequencybands:
odsfirstapproximatethenoiselatentsx1:𝑇 of𝐼,achievedviatechniquessuchasDDIMinversion[51].Stylizationisthenperformed
throughre-generationwithalteredconditions(usuallyspecifiedas 𝜖 𝜃(x𝑡 ,𝑡;𝑦)=G𝑡 (𝜅 𝑡 ,𝜓 𝑡), 𝑡 ∈ [0,𝑇] (2)

<!-- Page 4 -->

MM’25,October27–31,2025,Dublin,Ireland RuixiangJiangandChangWenChen
where𝜅 𝑡and𝜓 𝑡denotethestructureandappearancerepresentation 0.8T 0.6T 0.4T 0.2T
atdiffusiontime-step𝑡 (detailedlater),respectively. G𝑡(·,·) isa
conceptualnoise-spacecompositionfunctionattime𝑡.
3.4 StructureandAppearanceasDelegate

### DiffusionProcess

We argue that the fundamental obstacle to achieving dual controlindiffusion-basedstylizationistheinherententanglementof
structureandappearance.Ouranalysis,detailedinAppendixD,
pinpointsthesourceofthisproblem:therelianceonasinglelatenttrajectoryx𝜏→− x0.Thismonolithicgenerationprocessforces
structuralandappearanceattributestocompeteforinfluenceat
everydenoisingstep,creatingtheS-Atradeoffthatfundamentally
limitscontrollability.

### Tobreakthisbottleneck,weproposeanovelmechanismthat

stylizesanimagewithseparatediffusiontrajectories,asillustrated
inFig.2.Specifically,weleveragetwosupplementarydiffusion
processeswithsharedinformation,calleddelegatebranches.We
initializethestructureandmainbranchfromtheinvertednoisex𝑇,
whileappearancedelegationstartsfromaGaussian𝜖 ∼ N(0,I).
Thesedelegationsenablecontrollingthestylizationovertheentire
diffusionprocess.Thecontrolledmainbranchcanbedenotedas:
𝜖 𝜃 𝑚 (x𝑡 ,𝑡;𝑦,𝜅 𝑡 𝑠,𝜓 𝑡 𝑎 )=G𝑡 (cid:0)𝜅 𝑡 𝑠 ◦𝜅 𝑡 𝑚,𝜓 𝑡 𝑎 ⋄𝜓 𝑡 𝑚(cid:1), 𝑡 ∈ [0,𝑇] (3)
wherethesuperscripts𝑠,𝑎,and𝑚denotethefactorizationextracted
fromthestructure,appearancedelegation,andmainbranch,respectively.The◦and⋄aretwonon-commutativecontroloperators.
3.5 StructureandAppearanceRepresentations
inDenoisingU-Net
HavingestablishedthecontrolmechanisminEq.3,wenowformulatethe𝜅 and𝜓 inaU-Net-baseddenoiserfordisentangling
structureandappearancecontrol.
PyramidalStructureRepresentation𝜅.Toeffectivelycontrol structural stylization, we require a representation that capturesimagesemanticsatmultiplelevelsofabstraction.Weidentify the hidden features in the ResBlock of denoising U-Net as the
idealsubstrateforthispurpose,whichrobustlyencodeappearanceinvariantimagesemanticsacrossvarying𝑡 (seeFig.3).Formally,
wedenotethehiddenfeatureofaResBlockasℎ 𝑖(x𝑡),where𝑖 ∈
{1,2,...,𝑁 𝑟𝑒𝑠}indexestheResBlocksupto𝑁 𝑟𝑒𝑠,withincreasing
spatialresolution.Stackingsuchfeaturefromalllayersformsa
pyramidalstructurerepresentationofx0at𝑡:
𝜅 𝑡 𝑠 :={ℎ 𝑖(xt )}𝑖∈𝑆𝑟𝑒𝑠 ,
whereℎ 𝑖 extractedfrom𝜖 𝜃 𝑠 (x𝑡 ,𝑡;∅), (4)
and𝑆 𝑟𝑒𝑠 ⊆{1,2,...,𝑁 𝑟𝑒𝑠}.
Ourrepresentationisdistinctasitcapturesmulti-scalesemanticsandprovidescontinuousguidanceacrossthefulldenoising
trajectory(𝑡 ∈ [0,𝑇]).Thisfundamentallydiffersfrommethods
relyingonsolitarycontrolpoints(e.g.,x𝜏)orsingle-scaleconditions
(e.g.,ControlNet,IP-Adapter).Suchapproachesareconstrainedto
afixedresolutionand/orSNR,whicharchitecturallylimitstheir
abilitytogeneratecomplexstructuralstyles.AsevidencedinSec.5,
thisconstraintoftenleadstoundesirablesemantictrade-offs.With
desioN
egami
tnetnoc
)𝑥(ℎ
)𝑥(𝑓
Figure3:ResBlockfeaturemapvisualization.Weapplyt-sne
tovisualizethefeaturemapofdifferentfeaturemapsinU-
Netdecoder.Thehiddenfeaturesℎ(x)betterpreservesthe
semanticsthantheResNetfeature𝑓(x)throughoutall𝑇.
thispyramidalrepresentation,weimplementthestructurecontrol
operator◦asinjection(i.e.,𝑎◦𝑏 =𝑎).
Semantic-awareAppearanceRepresentation𝜓.Werepresenttheappearanceofthetargetstyleasself-attentionmapsex- tractedfromalllayersof𝜖𝑠
.Forthestyletobeappliedharmoniously,
𝜃
itsgenerationmustbeguidedbytheimage’ssemantics.However,
untilnow,wedenoiseappearancedelegationfromGaussiannoise
andhencehasnoinformation-sharingwiththesourceimage.To
compensateforthis,weproposeStructure-to-Appearanceinjection(S2A)thatpropagatesthehigh-levelsemanticsintoappearancegeneration.Specifically,weinjecttheself-attentionvalue𝑉
fromearlylayersof𝜖 𝜃 𝑠 to𝜖 𝜃 𝑎 .Let𝑁 𝑎𝑡𝑡𝑛 denotethetotalnumberof
attentionblockswithintheU-Netdecoder,𝑆 𝑠2𝑎 ⊆{1,2,...,𝑁 𝑎𝑡𝑡𝑛}
betheselectedblocksforS2Ainjection.Theappearancerepresentationat𝑡 is:
𝜓 𝑡 𝑎 :={𝐴 𝑖 𝑎 } 𝑖 𝑁 = 𝑎 1 𝑡𝑡𝑛, where𝐴 𝑖 𝑎 isextractedfrom𝜖 𝜃 𝑎(cid:16) x𝑡 ,𝑡;𝑦,{𝑉 𝑗 𝑠 }𝑗∈𝑆𝑠2𝑎 (cid:17) ,
with{𝑉
𝑗
𝑠 }𝑗∈𝑆𝑠2𝑎 extractedfrom𝜖
𝜃
𝑠 (x𝑡 ,𝑡;∅).
(5)
InspiredbyStyleAligned[22]wedesigntheappearance-style
controloperator⋄astheAdaIN[25],
(cid:18)𝑎−𝜇(𝑎)(cid:19)
𝑎⋄𝑏 =𝜎(𝑏) +𝜇(𝑏). (6)
𝜎(𝑎)
WevisualizethefeatureinteractionsintherightpartofFig.2.
Adjustingthecontrollayerin𝑆 𝑟𝑒𝑠 andstylestrengthof𝜖 𝑡 𝑎 enables
disentangledcontrolforstructureandappearance,respectively.
3.6 StructureandAppearanceEvaluationvia

### MLLMs

Recentresearchdemonstratesthepowerfulsemantic-levelmultimodalunderstandingofMLLMs[35,38,40,65,70].Weleverage
state-of-the-artMLLMsasazero-shotevaluatortoassesstwokey
axesofourmethod:structurepreservationandappearancefidelity.

<!-- Page 5 -->

DiffArtist:TowardsStructureandAppearanceControllableImageStylization MM’25,October27–31,2025,Dublin,Ireland
“8-Bit
Pixel-art,
detailed”
“Rococo
painting”
Content Image StylePrompt Ours DDIM Prompt2Prompt Plug-and-play ControlNet InstructPix2Pix DiffStyler
sdohteM
nevirD-txeT
)a
sdohtem
desab-ecnerefeR
)b
CLIPStyler
“Vincent
van gogh,
Egon schiele
”
“Cubism
painting,
fragmented,
Picasso
”
Content Image StylePrompt Ours SD AdaIN ArtFlow StyTr2 StyleID StyleAligned InstantStyle
Figure4:Qualitativecomparisonwithexistingmethods.Wecompareourworkwithrepresentativetext-drivenimagemanipulationmethodin(a),andimage-basedstylizationmethodsin(b).StylizedimagesgeneratedbyDiffArtistproducehigh-fidelity
structuralandappearance-levelstylewithsemanticintegrity.WesuggestreadersformorevisualizationsinAppendixA.
Crucially,ourgoalistomeasurefidelityofstylizedimages,not tuning.However,itshouldbenotedthatuserscanadjustthese
subjectivequalitieslikevisualappeal.1. parametersforcustomization.
Giventheinherentsubjectivityandthedifficultyofassigning ComparedMethods.Wecompareourmethodagainstexistabsolutescores,wedesignarelativeevaluationframework.Specif- ingtext-drivenstylizationandmanipulationmethods:DDIMInically, we query MLLM with the tuple (Iˆ,𝐼,𝑦,𝑦 𝑖), where Iˆ = version[51],CLIPStyler(optimization-based)[37],DiffStyler[24],

## {𝐼ˆ

1
,...,𝐼ˆ 𝑘}isthestylizationresultgeneratedby𝑘differentmodels, Plug-and-Play (PnP), Prompt2Prompt (with null text inversion)
𝐼 ≔x0isthesourceimage,and𝑦 𝑖 istheinstructiondedicatedfor (P2P)[21,46],ControlNet[66],andInstructPix2Pix[4].Additionstructureorappearancefidelityevaluation.TheMLLMistasked ally,weconsiderabaselinenamedSD,whichgeneratesimages
withrankingtheoutputsof𝑘differentmethodsforeachcriteria. withStableDiffusionaccordingto𝑦.
WeshowinSec.5.2thatthisdesignachievessuperioralignment Wealsoindirectlycompareourmethodwithreference-based
withhumanperceptioncomparedwithexistingmetrics. stylizationmethods,includingAdaIN[25],ArtFlow[1],StyTr2[11],
StyleID[8],StyleAligned[22](withControlNet),andInstantStyle[54]
4 Experiments (withControlNet).ImagesgeneratedbySDareusedasreference.
ConventionalMetrics:LPIPS[67]measuresthecontentpreser-
4.1 ExperimentSetup
vationbycalculatingthefeaturedistancebetweenthesourceand
ImplementationDetails. Ourexperimentsarebuiltuponthe stylizedimage.Forstylefidelity,weleverageCLIPScore[48]and
publiclyavailableStableDiffusion2.1model2.WeperformDDIM

### PickScore[34],bothofwhichquantifythealignmentbetween

samplingwith𝑇 =50steps.Duringtheinversion,werecordthe thestylizedimage𝐼ˆandprompt𝑦.Wealsoincludeahumanstudy
intermediatenoisepredictionstooverwritetheinputof𝜖 𝜃 𝑠 during crowd-sourcedfrom𝑛 1 =200usersandreporttheaveragepreferdenoising.FurtherimplementationdetailsareavailableinAppenencerateforourmethod.
dixB.ExperimentswereconductedwithasingleRTX4090-DGPU, MLLM-basedMetrics:WeprompttheMLLMtorankthefiwith an approximate runtime of 2 seconds for inversion and 8 delityof𝑘stylizedimagesfrombest(rank1)toworst(rank𝑘).We
secondsforthefinalstylization.
normalizetheintegerrankingandaverageitoverthewholeevalu-

### DefaultParameters.Inmainexperiment,wedefault𝑆 restobe

ationset.Therefore,ascorecloserto1indicatesastrongerfidelity.
thefirstfourResNetlayers([1, 2, 3, 4]),and𝑆 s2aasthefirsttwo WeuseGemini-v2.0-flashforitsstrongmultimodalcapability.
attentionlayerfeatures([1, 2]).Theclassifier-freeguidance(CFG)
ThefullprompttemplatescanbefoundinAppendixC.
scaleissetas7.5.Thesedefaultcontrolparameterscorrespondto
moderatestructuralandappearancevariations,usedtosetafair
comparison with existing works to avoid per-image parameter 4.2 Comparisons
1Notethatvisual-appealisalsonotequivalenttoaestheticquality[17,28] QualitativeComparisons.Wefirstprovideacomprehensivecom-
2https://huggingface.co/stabilityai/stable-diffusion-2-1 parisonagainstpreviousmethods,visualizedinFig.4-(a,b).(a):

<!-- Page 6 -->

MM’25,October27–31,2025,Dublin,Ireland RuixiangJiangandChangWenChen
Table1:Quantitativecomparisonagainstexistingmethods.Weshowconventional(ingrayfont)andMLLM-basedmetricsfor
representativemethods.Foreachmetric, indicatesthebestscore, indicatesthesecondbestscore,and indicatesthe
thirdbestscore(bestviewedincolor).Winratemeansthepercentagethatourmethodwinsinpair-wisecomparison.
Metric Ours DDIM SD PnP P2P InstructP2P ControlNet InstantStyle DiffStyler CLIPStyler
Inferencetime(sec) 10.5 9.7 3.9 55.3 29.1 9.2 7.8 7.8 18.2 24.2

### Training&adapterfree ✓ ✓ ✓ ✓ ✗ ✗ ✗ ✗ ✗ ✗


### Lpips↓ 0.52 0.57 0.76 0.67 0.47 0.42 0.65 0.59 0.71 0.46

CLIPScore[48]↑ 25.91 25.25 27.46 24.89 23.48 21.94 24.93 22.85 25.79 27.14
PickScore[34]↑ 20.51 20.58 20.68 20.34 20.50 20.06 20.46 19.97 19.24 20.13
Structure(MLLM)↑ 0.61 0.22 0.29 0.52 0.65 0.60 0.58 0.56 0.35 0.51
Appearance(MLLM)↑ 0.67 0.46 0.31 0.60 0.47 0.59 0.55 0.67 0.30 0.59
Avg.(MLLM)↑ 0.64 0.34 0.30 0.56 0.56 0.60 0.57 0.62 0.33 0.55
StructureWin(Human)↑ - 78.2% 62.4% 64.7% 57.3% 62.2% 71.2% 59.8% 81.3% 73.0%
AppearanceWin(Human)↑ - 74.2% 86.4% 62.0% 73.7% 68.7% 75.0% 60.1% 85.3% 76.3%
Comparedwithtext-drivenmethods,DiffArtististhebestatfol- 5 AnalysisandDiscussion
lowingthestylepromptwhilemaintainingsemanticintegrity.Our This section provide in-depth analysis on the proposed system.
methodenablesharmoniousstructuralvariations,suchaspixela- InSec.5.1,weanalyzethecontrollabilityofDiffArtistindetail.
tion,withoutcompromisingintricatedetailslikefacialidentityand Sec.5.2validatestheeffectivenessofMLLMsasstyleevaluators.
hair.Bycontrast,thecomparedmethodsmayproducemisaligned Sec.5.3providesablationsondelegationsandtheS2Ainjection.
styles(e.g.,CLIPStyler,Plug-and-Play)orintroduceundesiredmod- WeconcludewithadiscussioninSec.5.4.
ificationsthatviolatesemantics(e.g.,DiffStyler,ControlNet).(b):
Whenbroadlycomparedwithreference-basedmethods,DiffArtist 5.1 DiffArtisthasStrongControllability
stillstandsoutforitshighstylizationfidelityfromtwoperspectives.
Thissubsectionvalidatestheunprecedenteddualcontrollabilityof

### Tofullydemonstratethesuperiority,wehighlysuggestreaders

DiffArtist.Toachievethis,weconductafine-grainedcomparative
foradditionalvisualizationsinAppendixA.
analysisagainstrepresentativemethods,categorizingthembytheir

### QuantitativeComparison.Forourquantitativeevaluation,we

corecontrolmechanism:(a)Semanticpyramid:includeDiffArtist,
firstsample50artstylesfromWikiART,withbothabstract(e.g.,

### DiffArtistimplementedwithPlug-and-Playstructurerepresenta-

“Cubism”)andrealisticstyles(e.g.,“HighRenaissance”),whichare
tion,𝑓(x)(Ours+PnP),andCtrl-X;(b)Pixel-levelmap:include
furtherdiversifiedbyGPT-4ointermsofdescription.Thisdiversifi-
InstantStyle [10], which is based on ControlNet [66]; (c) Noise
cationsetsabroadspectrumofstylestoalignwithreal-worlduser
inversion,whichcorrespondstotheDDIMbaseline.Forstructure
inputs.Thecontentcomprises50imagesfromMSCOCO[43]and
control,wedefinefivelevelsfromweakesttostrongest.Forgroup(a)
50photorealisticimagesgeneratedbyanothermodel[26].Foreach
weusethefollowingcontrollayers:(∅,[1],[1-4],[1-6],[1-8]);
ofthe100contentimages,werandomlydraw10stylepromptsfrom
allpossiblestyles,resultinginatotalof1,000uniquecombinations forgroup(b),weevenlysampletheirrespectivecontrolstrengthparameters;andweuse𝜏 = [0,5,10,15,20]forgroup(c).Appearance
forcomparison.Tab.1presentstheresults.
strengthiscontrolledbysamplingCFGweightsin[2.5,5,7.5,10]

### Forconventionalmetrics,DiffArtistachievesanLPIPSof0.52,a

forallgroupsexceptforCtrl-X,whichisachievedbyadjustingits
CLIPScoreof25.91,andaPickScoreof20.51,outperformingmost
appearancescheduleparameter.
ofthecomparedmethods.However,thesemetricsdonotmeasure

### QualitativeComparisononControl.AsvisualizedinFig.5,

stylizationqualityinstructureandappearance.Asasimplecounter-
DiffArtistdemonstratessuperiorcontrollability,withharmonious,
example,thebaselineSDhasthehighestCLIPScoreandPickScore,
consistent,anddisentangledinterpolationsacrossasequenceof
whereasitisnotevenperformingstylization.Weincludethese
controllevels.Itcorrectlycapturestheessentialgeometricprinciscoressolelyforreference.
plesofCubism,whereascompetingmethodsmerelyapplyasu-

### WhenevaluatedwithMLLM-basedmetrics,DiffArtistattainsthe

perficial texture (e.g., Ours+PnP) or fail to produce meaningful
highestaveragescoreof0.64.Specifically,ourmethodachievesthe
structuralvariations(e.g.,InstantStyle).Thisnuancedcontrolisfursecond-higheststructurescoreof0.61,demonstratingDiffArtist’s
therevidentwhenadjustingstylestrength;DiffArtistprovidesan
effectiveness in generating structural styles. While the editingartisticallymeaningfulinterpretationbyproducingbolderstrokes
focusedP2Pmethodscoreshigher,itdoessobysacrificingstylistic
accordingtostyleprompt,whileothermethodsresorttosimplistic
strength,evidencedinqualitativecomparisons.Besides,ourmethod
andoftenundesirableincreasesincolorsaturation.Mostcritically,
achievesthebestappearancefidelityscore,confirmingitssuperior
ourapproachpreservessemanticintegrity.Itavoidsthecatastrophic
abilitytorendertheappearancedetailsfromthetextprompt.In
failuresofpixel-mapmethodslikeInstantStyle,whichcanrender
humanevaluations,ourmethodispreferredbyanaverageof67.8%
thefaceunrecognizable,andalsopreventsthefacialstructurecorofusersinpairwisecomparison,furthervalidatingitssuperiority.
ruptionseenininversion-basedmethodsthatinherentlyentangle
formwithappearance.TheextendedvisualizationsinAppendixA

<!-- Page 7 -->

DiffArtist:TowardsStructureandAppearanceControllableImageStylization MM’25,October27–31,2025,Dublin,Ireland
sruO
PnP+sruO
X-lrtC

## Midd

Content Content
& Style & Style
Fauvism

### Cubism

painting,
painting,
bold brush
detailed
strokes
elytStnatsnI

### Structural Style Strength Appearance Style Strength

Figure5:DiffArtistoffersdisentangledandstrongercontrollability.(Left):DiffArtistenablessmoothandartisticallymeaningful
structuralstylizationatvaryingdegree,withoutviolatingappearancestylestrength.(Right):DiffArtistallowsfine-grained
controlofappearance-relatedstylestrengthwhilepreservingstructuralandsemanticintegrity.
withdiversestyleandcontentfurtherconfirmthesuperiorityof Table2:Fidelityofstructureandappearancecontrolviacross-
DiffArtist. methodcomparison.Thevaluescorrespondtothestructure
QuantitativeComparisonsonControl.Weprovidequantita- orappearancescore(MLLM,↑).Notethatthemagnitudesof
tiveexperimentstosubstantiateourvisualobservations,evaluat- scoresareonlycomparablewithineachcolumn.Thebest
ingcontrolbasedontwoproperties:fidelityandeditability.We resultforeachcolumnisinbold.
measurethefidelityasstructureandappearanceMLLMscoresat
differentcontrollevels.TheresultsarereportedinTab.2.DiffArtist —Structure→ —Appearance→

### Method

outperformsotherssignificantlyandconsistently,demonstrating lv.1 lv.2 lv.3 lv.4 lv.5 lv.1 lv.2 lv.3 lv.4
superiorcontrolfidelity.

### Ours 0.62 0.65 0.74 0.63 0.66 0.70 0.74 0.80 0.78

The editability defines the quality of the manipulation itself, Ours+PnP 0.43 0.38 0.28 0.42 0.34 0.21 0.26 0.27 0.32
whichweassessviathreecriteria:range,monotonicity,anddis- Ctrl-X 0.49 0.46 0.36 0.46 0.47 0.41 0.37 0.33 0.42
entanglement.Anidealcontrolofstylizationshouldcoverawide InstantStyle 0.42 0.42 0.33 0.43 0.35 0.34 0.34 0.35 0.60

### Ddim 0.49 0.52 0.52 0.51 0.55 0.59 0.53 0.50 0.52

rangeofstylisticeffects(alargespreadinMLLMscores),exhibitpredictablemonotonicity(Spearman’s𝜌 ≈1forthetargetattribute),
andmaintaindisentanglementfromotherattributes.Wemeasure
thedisentanglementusingKendall’s𝑊 ontheoff-targetscores, fromhumanfeedback.Toachievethis,wefirstconstructacomwhereastable,unaffectedscoresequenceyields𝑊 ≈ 0.Forinparisonsetof800stylizedimages3,andcomparehowhumanand
stance,whencontrollingstructuralstrength,𝑊 fortheappearance MLLMpreferencescorrelate.
Togatherhumanfeedback,weconsidertwogroupsofusers.For
scoreisdesiredtobenear0.AsshowninTab.2,thecontrolof
DiffArtististhemosteditable:itcoversthebroadestrangeofefthenon-expertgroup,werecruitedalarge-scalegroupof𝑛
1
=200
participantsthroughacrowdsourcingplatform.Eachparticipant
fects,demonstratesthestrongestmonotonicity,andachievesthe
performedaseriesofrandomlysampledrankingtasks.Toensure
bestdisentanglement,reaffirmingthesuperiorcontrolvisualized
theintegrityofthecollecteddata,weimplementedattentionchecks
inFig.5.
andconsistencyfilterstoremoveunreliableresponses.Wealso
recruitedanexpertgroupof𝑛
2
=12participantswithknowledge
offineart.
5.2 MLLMsareHuman-AlignedStylization We measured the alignment between each metric’s rankings
Evaluators andthehuman-derivedpreferencesusingSpearman’srankcorrelation(𝜌).Theaveraged(ofallcontent-stylepairs)𝜌 forboth
Weevaluatehoweachstylizationmetricalignswithhumanfeedbackbycalculatingthestatisticalcorrelationwiththerankings 3TheimagesevaluatedheredonotoverlapwiththemainexperimentinTab.1

<!-- Page 8 -->

MM’25,October27–31,2025,Dublin,Ireland RuixiangJiangandChangWenChen
Table3:Controleditabilityanddisentanglementviainter-methodcomparison.Higher𝜌indicatesstrongermonotonicitywhile
lower𝑊 meansranksareindistinguishable.Whencontrollingfromoneperspective,ahigh𝜌isdesiredforeditability,andalow
𝑊 fortheotheraspectisexpectedfordisentangledcontrol.ThecontrolsinDiffArtistarethemosteditableanddisentangled.
SequentialStructure-ControlOnly SequentialAppearance-ControlOnly
Ours Ours+PnP Ctrl-X InstantStyle DDIM Ours Ours+PnP Ctrl-X InstantStyle DDIM
𝜌(𝑆)↑ 0.82 0.54 0.32 0.39 0.70 𝑊(𝑆)↓ 0.37 0.32 0.36 0.45 0.69
𝑊(𝐴)↓ 0.32 0.44 0.45 0.34 0.72 𝜌(𝐴)↑ 0.71 0.42 0.35 0.26 0.68
Table4:Metricscorrelationwithhumanfeedback.Wereport
correlation𝜌andcombinedsignificance𝑝.TheMLLMscores
showstrongeralignmentwithbothexpertandnon-expert
users.
Corr.(Non-expert) Corr.(Expert)
Metrics 𝜌↑ p-value↓ 𝜌↑ p-value↓

## Ssim[57] 0.29 0.12 0.25 0.14

S MLLM(GPT-4o) 0.44 0.004 0.34 0.20
MLLM(Gemini2.0) 0.42 0.02 0.45 0.03

### CLIPScore 0.05 0.73 0.01 0.75

PickScore[34] 0.27 0.11 0.25 0.13

## A


### MLLM(GPT-4o) 0.25 0.05 0.22 0.06


### MLLM(Gemini2.0) 0.48 0.04 0.41 0.02

Table5:Ablationondelegationbranches.Theproposedtwo
delegationsarecomplementarytoeachother,andthefull
methodsachievesthehighestfidelity.

### Method

full w/ostructure w/oappearance

### Metric


## Lpips↓ 0.51 0.76 0.42


### CLIPScore↑ 25.91 27.69 21.75

PickScore[34]↑ 20.55 20.57 20.41

### Structure(MLLM)↑ 0.72 0.37 0.33


### Appearance(MLLM)↑ 0.62 0.59 0.22

groupsisreportedinTab.4.Asthetableshows,theMLLM-based
metricsarebetteralignedwithhumanperception,validating
itseffectivenessasanevaluationmetricforstyletransfer.
5.3 Ablations
Thedelegationsenabledualcontrollability.DiffArtist’scontrollabilitystemsfromdelegatingstructureandappearancegeneration
to separate processes. To test the necessity of each, we created
twoablatedvariantsforcomparisonwherethestructureorappearancedelegationisremoved.Tab.5presentstheresultofthis
ablation.Thefullmethodsachievesthebestresults,demonstrating
thesynergisticeffectofdelegationsfordualcontrollability.

### S2Ainjectionpromotessemantic-alignedspatialdistribution

ofstylestrengthinthestyledelegationprocess,therebyavoiding
artifactsinthefinalstylizationresult.Wevisualizethedenoised
styleimage(fromappearancedelegation)andthefinalstylization

## )A2S

o/w(
sruO
)lluF(
sruO
Content Appearance Stylization Content Appearance Stylization
& Style Delegation Result & Style Delegation) Result
Cartoon An 8-Bit
painting
pixel art,
using detailed
markers
Figure 6: Ablation on S2A injection. S2A injection propagatesthehigh-levelsemantictotheappearancegeneration.
Itavoidsspatialmisalignmentofappearance-stylestrength.
resultinFig.6.WithoutS2Ainjection,theappearancedelegation
failstoalignwithcontentsemantics,generatinganappearance
referenceimagewithundesiredpatternsandanuneventexture
distribution.Theseflawsmanifestdirectlyinthefinaloutputas
distractingvisualartifacts.Incontrast,thefullmodelleveragesS2A
toproduceacoherentstylerepresentation,resultinginacleanand
high-qualityfinalimage.
5.4 Limitations&Futurework
While DiffArtist marks a significant step towards disentangled
structureandappearancecontrol,weidentifyseverallimitations
thatopenexcitingavenuesforfutureresearch.Forinstance,the
structurecontrolinDiffArtistisatagloballevel,anditcannot
controlthestructureforeachobjectseparately.Manyartstyles
exhibitmixedstructurevariation,likeSurrealismandCollageart.
Developingdensestructureevaluatorswith2Dfeedbacksignals
isapromisingdirection[41],whichmaybefurtherutilizedasa
rewardmodelforreinforcementlearning[2,9].
6 Conclusion
We present the first exploration of structure- and appearancecontrollableimagestylization.OurcontributionsincludeDiffArtist,
astylerthatfullydisentanglesstructureandappearanceduringthe
diffusionprocess,andahuman-alignedevaluatortoassessstructuralandappearancefidelityatthesemanticlevel.Ourextensive
analysisprovesthatsemantically-richrepresentationsareessential
forbothstructureandappearancestyle.Wedemonstratedthatour
designallowsforhighstylefidelityandcontrollability,similarto
thatofahumanartist.Webelievetheobjectiveestablishedinthis
paper—tostylizeinbothstructureandappearance—offeraroadmap
forthenextgenerationofgenerativearttoolstoproduceartistically
meaningfulpaintings.

<!-- Page 9 -->

DiffArtist:TowardsStructureandAppearanceControllableImageStylization MM’25,October27–31,2025,Dublin,Ireland
7 Acknowledgment
text-drivenimagestylization.IEEETransactionsonNeuralNetworksandLearning
Systems(2024).

### ThisresearchwassupportedbytheHongKongResearchGrants

[25] XunHuangandSergeBelongie.2017. Arbitrarystyletransferinreal-time
Council(GRF-15229423). withadaptiveinstancenormalization.InProceedingsoftheIEEEinternational
conferenceoncomputervision.1501–1510.
References [26] Ideogram.2024. Ideogram:Explore. https://ideogram.ai/t/explore Accessed:
2024-03-20.
[1] JieAn,SiyuHuang,YibingSong,DejingDou,WeiLiu,andJieboLuo.2021. [27] EleftheriosIoannouandSteveMaddock.2024.EvaluationinNeuralStyleTransfer:
Artflow:Unbiasedimagestyletransferviareversibleneuralflows.InProceedings AReview.InComputerGraphicsForum.WileyOnlineLibrary,e15165.
oftheIEEE/CVFconferenceoncomputervisionandpatternrecognition.862–871. [28] RuixiangJiangandChangwenChen.2025.MultimodalLLMsCanReasonabout
[2] Kevin Black, Michael Janner, Yilun Du, Ilya Kostrikov, and Sergey Levine. AestheticsinZero-Shot.arXivpreprintarXiv:2501.09012(2025).

## Trainingdiffusionmodelswithreinforcementlearning. arXivpreprint [29] RuixiangJiang,CanWang,JingboZhang,MengleiChai,MingmingHe,Dongdong

arXiv:2305.13301(2023). Chen,andJingLiao.2023. Avatarcraft:Transformingtextintoneuralhuman
[3] YihangBo,JinhuiYu,andKangZhang.2018. Computationalaestheticsand avatarswithparameterizedshapeandposecontrol.InProceedingsoftheIEEE/CVF
applications.Visualcomputingforindustry,biomedicine,andart1(2018),1–19. InternationalConferenceonComputerVision.14371–14382.
[4] TimBrooks,AleksanderHolynski,andAlexeiAEfros.2023. Instructpix2pix: [30] HyunyoungJung,SeonghyeonNam,NikolaosSarafianos,SungjooYoo,Alexander
Learningtofollowimageeditinginstructions.InProceedingsoftheIEEE/CVF Sorkine-Hornung,andRakeshRanjan.2024. Geometrytransferforstylizing
ConferenceonComputerVisionandPatternRecognition.18392–18402. radiancefields.InproceedingsoftheIEEE/CVFConferenceonComputerVisionand
[5] Dave Zhenyu Chen, Yawar Siddiqui, Hsin-Ying Lee, Sergey Tulyakov, and PatternRecognition.8565–8575.
MatthiasNießner.2023. Text2tex:Text-driventexturesynthesisviadiffusion [31] BahjatKawar,ShiranZada,OranLang,OmerTov,HuiwenChang,TaliDekel,
models.InProceedingsoftheIEEE/CVFinternationalconferenceoncomputervision. InbarMosseri,andMichalIrani.2023.Imagic:Text-basedrealimageeditingwith
18558–18568. diffusionmodels.InProceedingsoftheIEEE/CVFConferenceonComputerVision
[6] JunyuChen,JieAn,HanjiaLyu,ChristopherKanan,andJieboLuo.2024.Learning andPatternRecognition.6007–6017.
toEvaluatetheArtnessofAI-generatedImages.IEEETransactionsonMultimedia [32] GwanghyunKim,TaesungKwon,andJongChulYe.2022.Diffusionclip:Text-
(2024). guideddiffusionmodelsforrobustimagemanipulation.InProceedingsofthe
[7] JingwenChen,YingweiPan,TingYao,andTaoMei.2023.Controlstyle:Text- IEEE/CVFconferenceoncomputervisionandpatternrecognition.2426–2435.
drivenstylizedimagegenerationusingdiffusionpriors.InProceedingsofthe31st [33] SunnieSYKim,NicholasKolkin,JasonSalavon,andGregoryShakhnarovich.
ACMInternationalConferenceonMultimedia.7540–7548. 2020. Deformablestyletransfer.InEuropeanConferenceonComputerVision.
[8] JiwooChung,SangeekHyun,andJae-PilHeo.2024.Styleinjectionindiffusion: Springer,246–261.
Atraining-freeapproachforadaptinglarge-scalediffusionmodelsforstyle [34] YuvalKirstain,AdamPolyak,UrielSinger,ShahbulandMatiana,JoePenna,and
transfer.InProceedingsoftheIEEE/CVFConferenceonComputerVisionandPattern OmerLevy.2023. Pick-a-pic:Anopendatasetofuserpreferencesfortext-to-
Recognition.8795–8805. imagegeneration.AdvancesinNeuralInformationProcessingSystems36(2023),
[9] KevinClark,PaulVicol,KevinSwersky,andDavidJFleet.2023.Directlyfine- 36652–36663.
tuningdiffusionmodelsondifferentiablerewards.arXivpreprintarXiv:2309.17400 [35] TakeshiKojima,ShixiangShaneGu,MachelReid,YutakaMatsuo,andYusuke
(2023). Iwasawa.2022. Largelanguagemodelsarezero-shotreasoners. Advancesin
[10] XingCui,ZekunLi,PeiPeiLi,HuaiboHuang,andZhaofengHe.2023.InstaStyle: neuralinformationprocessingsystems35(2022),22199–22213.
InversionNoiseofaStylizedImageisSecretlyaStyleAdviser.arXivpreprint [36] DmytroKotovenko,ArtsiomSanakoyeu,SabineLang,andBjornOmmer.2019.
arXiv:2311.15040(2023). Contentandstyledisentanglementforartisticstyletransfer.InProceedingsof
[11] YingyingDeng,FanTang,WeimingDong,ChongyangMa,XingjiaPan,LeiWang, theIEEE/CVFinternationalconferenceoncomputervision.4422–4431.
andChangshengXu.2022. Stytr2:Imagestyletransferwithtransformers.In [37] GihyunKwonandJongChulYe.2022. Clipstyler:Imagestyletransferwitha
ProceedingsoftheIEEE/CVFconferenceoncomputervisionandpatternrecognition. singletextcondition.InProceedingsoftheIEEE/CVFConferenceonComputer
11326–11336. VisionandPatternRecognition.18062–18071.
[12] GuanchenDing,LingboLiu,ZhenzhongChen,andChangwenChen.2024. [38] YanshuLi,HongyangHe,YiCao,QisenCheng,XiangFu,andRuixiangTang.
Domain-agnosticcrowdcountingviauncertainty-guidedstylediversityaugmen- 2025.M2iv:Towardsefficientandfine-grainedmultimodalin-contextlearning
tation.InProceedingsofthe32ndACMInternationalConferenceonMultimedia. inlargevision-languagemodels.arXivpreprintarXiv:2504.04633(2025).
1642–1651. [39] YanghaoLi,NaiyanWang,JiayingLiu,andXiaodiHou.2017. Demystifying
[13] RinonGal,OrPatashnik,HaggaiMaron,AmitHBermano,GalChechik,and neuralstyletransfer.arXivpreprintarXiv:1701.01036(2017).
DanielCohen-Or.2022.Stylegan-nada:Clip-guideddomainadaptationofimage [40] YanshuLi,TianYun,JianjiangYang,PinyuanFeng,JinfaHuang,andRuixiang
generators.ACMTransactionsonGraphics(TOG)41,4(2022),1–13. Tang.2025.TACO:EnhancingMultimodalIn-contextLearningviaTaskMapping-
[14] JunyaoGao,YanchenLiu,YananSun,YinhaoTang,YanhongZeng,KaiChen, GuidedSequenceConfiguration.arXivpreprintarXiv:2505.17098(2025).
andCairongZhao.2024. Styleshot:Asnapshotonanystyle. arXivpreprint [41] YouweiLiang,JunfengHe,GangLi,PeizhaoLi,ArseniyKlimovskiy,Nicholas
arXiv:2407.01414(2024). Carolan,JiaoSun,JordiPont-Tuset,SarahYoung,FengYang,etal.2024.Rich
[15] LeonAGatys,AlexanderSEcker,andMatthiasBethge.2015.Aneuralalgorithm humanfeedbackfortext-to-imagegeneration.InProceedingsoftheIEEE/CVF
ofartisticstyle.arXivpreprintarXiv:1508.06576(2015). ConferenceonComputerVisionandPatternRecognition.19401–19411.
[16] LeonAGatys,AlexanderSEcker,andMatthiasBethge.2016.Imagestyletransfer [42] KuanHengLin,SichengMo,BenKlingher,FangzhouMu,andBoleiZhou.2024.
usingconvolutionalneuralnetworks.InProceedingsoftheIEEEconferenceon Ctrl-x:Controllingstructureandappearancefortext-to-imagegenerationwithcomputervisionandpatternrecognition.2414–2423. outguidance. AdvancesinNeuralInformationProcessingSystems37(2024),
[17] ErnstHansGombrichandEHGombrich.1995.Thestoryofart.Vol.12.Phaidon 128911–128939.
London. [43] Tsung-YiLin,MichaelMaire,SergeBelongie,JamesHays,PietroPerona,Deva
[18] NelsonGoodman.1976. Languagesofart:Anapproachtoatheoryofsymbols. Ramanan,PiotrDollár,andCLawrenceZitnick.2014.Microsoftcoco:Common
Hackett. objectsincontext.InComputervision–ECCV2014:13thEuropeanconference,
[19] FeihongHe,GangLi,MengyuanZhang,LeileiYan,LingyuSi,FanzhangLi,and zurich,Switzerland,September6-12,2014,proceedings,partv13.Springer,740–
LiShen.2024.Freestyle:Freelunchfortext-guidedstyletransferusingdiffusion 755.
models.arXivpreprintarXiv:2401.15636(2024). [44] YuemingLyu,YueJiang,BoPeng,andJingDong.2023. InfoStyler:Disentan-
[20] AmirHertz,KfirAberman,andDanielCohen-Or.2023.Deltadenoisingscore.In glementinformationbottleneckforartisticstyletransfer.IEEETransactionson
ProceedingsoftheIEEE/CVFInternationalConferenceonComputerVision.2328– CircuitsandSystemsforVideoTechnology34,4(2023),2070–2082.
2337. [45] OscarMichel,RoiBar-On,RichardLiu,SagieBenaim,andRanaHanocka.2022.
[21] AmirHertz,RonMokady,JayTenenbaum,KfirAberman,YaelPritch,andDaniel Text2mesh:Text-drivenneuralstylizationformeshes.InProceedingsofthe
Cohen-Or.2022.Prompt-to-promptimageeditingwithcrossattentioncontrol. IEEE/CVFConferenceonComputerVisionandPatternRecognition.13492–13502.
arXivpreprintarXiv:2208.01626(2022). [46] RonMokady,AmirHertz,KfirAberman,YaelPritch,andDanielCohen-Or.2023.
[22] AmirHertz,AndreyVoynov,ShlomiFruchter,andDanielCohen-Or.2024.Style Null-textinversionforeditingrealimagesusingguideddiffusionmodels.In
alignedimagegenerationviasharedattention.InProceedingsoftheIEEE/CVF ProceedingsoftheIEEE/CVFConferenceonComputerVisionandPatternRecognition.
ConferenceonComputerVisionandPatternRecognition.4775–4785. 6038–6047.
[23] MartinHeusel,HubertRamsauer,ThomasUnterthiner,BernhardNessler,and [47] BenPoole,AjayJain,JonathanTBarron,andBenMildenhall.2022.Dreamfusion:
SeppHochreiter.2017.Ganstrainedbyatwotime-scaleupdateruleconvergeto Text-to-3dusing2ddiffusion.arXivpreprintarXiv:2209.14988(2022).
alocalnashequilibrium.Advancesinneuralinformationprocessingsystems30 [48] AlecRadford,JongWookKim,ChrisHallacy,AdityaRamesh,GabrielGoh,
(2017). SandhiniAgarwal,GirishSastry,AmandaAskell,PamelaMishkin,JackClark,
[24] NishaHuang,YuxinZhang,FanTang,ChongyangMa,HaibinHuang,Weiming
Dong,andChangshengXu.2024. Diffstyler:Controllabledualdiffusionfor

<!-- Page 10 -->

MM’25,October27–31,2025,Dublin,Ireland RuixiangJiangandChangWenChen
etal.2021.Learningtransferablevisualmodelsfromnaturallanguagesupervision. [61] JinchaoYang,FeiGuo,ShuoChen,JunLi,andJianYang.2022.Industrialstyle
InInternationalconferenceonmachinelearning.PMLR,8748–8763. transferwithlarge-scalegeometricwarpingandcontentpreservation.InPro-
[49] ArtsiomSanakoyeu,DmytroKotovenko,SabineLang,andBjornOmmer.2018. ceedingsoftheIEEE/CVFconferenceoncomputervisionandpatternrecognition.
Astyle-awarecontentlossforreal-timehdstyletransfer.Inproceedingsofthe 7834–7843.
Europeanconferenceoncomputervision(ECCV).698–714. [62] SerinYang,HyunminHwang,andJongChulYe.2023. Zero-shotcontrastive
[50] ChaehanSo.2023.Measuringaestheticpreferencesofneuralstyletransfer:More lossfortext-guideddiffusionimagestyletransfer.InProceedingsoftheIEEE/CVF
precisionwiththetwo-alternative-forced-choicetask.InternationalJournalof InternationalConferenceonComputerVision.22873–22882.
Human–ComputerInteraction39,4(2023),755–775. [63] HuYe,JunZhang,SiboLiu,XiaoHan,andWeiYang.2023. Ip-adapter:Text
[51] JiamingSong,ChenlinMeng,andStefanoErmon.2020. Denoisingdiffusion compatibleimagepromptadapterfortext-to-imagediffusionmodels. arXiv
implicitmodels.arXivpreprintarXiv:2010.02502(2020). preprintarXiv:2308.06721(2023).
[52] TheoVanLeeuwenandCareyJewitt.2000.Thehandbookofvisualanalysis.Sage. [64] RanYi,HaoyuanTian,ZhihaoGu,Yu-KunLai,andPaulLRosin.2023.Towards
[53] CanWang,RuixiangJiang,MengleiChai,MingmingHe,DongdongChen,and artisticimageaestheticsassessment:alarge-scaledatasetandanewmethod.In
JingLiao.2023. Nerf-art:Text-drivenneuralradiancefieldsstylization. IEEE ProceedingsoftheIEEE/CVFConferenceonComputerVisionandPatternRecognition.
TransactionsonVisualizationandComputerGraphics(2023). 22388–22397.
[54] HaofanWang,QixunWang,XuBai,ZekuiQin,andAnthonyChen.2024. In- [65] DuzhenZhang,YahanYu,JiahuaDong,ChenxingLi,DanSu,ChenhuiChu,and
stantstyle:Freelunchtowardsstyle-preservingintext-to-imagegeneration.arXiv DongYu.2024.Mm-llms:Recentadvancesinmultimodallargelanguagemodels.
preprintarXiv:2404.02733(2024). arXivpreprintarXiv:2401.13601(2024).
[55] HaofanWang,PengXing,RenyuanHuang,HaoAi,QixunWang,andXuBai. [66] LvminZhang,AnyiRao,andManeeshAgrawala.2023.Addingconditionalcon-

## Instantstyle-plus:Styletransferwithcontent-preservingintext-to-image troltotext-to-imagediffusionmodels.InProceedingsoftheIEEE/CVFInternational

generation.arXivpreprintarXiv:2407.00788(2024). ConferenceonComputerVision.3836–3847.
[56] XinhaoWang,WenjingWang,ShuaiYang,andJiayingLiu.2022.CLAST:Con- [67] RichardZhang,PhillipIsola,AlexeiAEfros,EliShechtman,andOliverWang.
trastivelearningforarbitrarystyletransfer.IEEETransactionsonImageProcessing 2018. Theunreasonableeffectivenessofdeepfeaturesasaperceptualmetric.
31(2022),6761–6772. InProceedingsoftheIEEEconferenceoncomputervisionandpatternrecognition.
[57] ZhouWang,AlanCBovik,HamidRSheikh,andEeroPSimoncelli.2004.Image 586–595.
qualityassessment:fromerrorvisibilitytostructuralsimilarity.IEEEtransactions [68] YuxinZhang,FanTang,WeimingDong,HaibinHuang,ChongyangMa,Tong-Yee
onimageprocessing13,4(2004),600–612. Lee,andChangshengXu.2023.Aunifiedarbitrarystyletransferframeworkvia
[58] ZhizhongWang,LeiZhao,andWeiXing.2023. Stylediffusion:Controllable adaptivecontrastivelearning.ACMTransactionsonGraphics42,5(2023),1–16.
disentangledstyletransferviadiffusionmodels.InProceedingsoftheIEEE/CVF [69] YexunZhang,YaZhang,andWenbinCai.2020.Aunifiedframeworkforgener-
InternationalConferenceonComputerVision.7677–7689. alizablestyletransfer:Styleandcontentseparation.IEEETransactionsonImage
[59] LinfengWen,ChengyingGao,andChangqingZou.2023.CAP-VSTNet:Content Processing29(2020),4085–4098.
affinitypreservedversatilestyletransfer.InProceedingsoftheIEEE/CVFconference [70] ZhuoshengZhang,AstonZhang,MuLi,HaiZhao,GeorgeKarypis,andAlex
oncomputervisionandpatternrecognition.18300–18309. Smola.2023.Multimodalchain-of-thoughtreasoninginlanguagemodels.arXiv
[60] MatthiasWrightandBjörnOmmer.2022.Artfid:Quantitativeevaluationofneural preprintarXiv:2302.00923(2023).
styletransfer.InDAGMGermanConferenceonPatternRecognition.Springer,560– [71] YangZhou,ZichongChen,andHuiHuang.2024. Deformableone-shotface
576. stylizationviadinosemanticguidance.InProceedingsoftheIEEE/CVFConference
onComputerVisionandPatternRecognition.7787–7796.

<!-- Page 11 -->

DiffArtist:TowardsStructureandAppearanceControllableImageStylization MM’25,October27–31,2025,Dublin,Ireland
Figure9:Exampleoffailurecases.
StructuralVariation(experiment)

### Style Variation (experiment)

Structural Variation (Simulation)

### Style Variation (Simulation)


### Figure7:TradeoffbetweenStructureandAppearanceStyle

Control.Wepresenttheexperimental(solidlines)andsimulation(dottedlines)trendsofstructuralandappearance
variationinthediffusionprocess.Duetoquadraticgrowth,
highly noisy steps are required to achieve strong appearancestyles,whichareassociatedwithsignificantstructural
variation,whichcanviolatesemantics.Top:Examplestylizationresultsstartingfromdifferentsteps,usingtheprompt:
“Fauvismpainting”.Whentheappearancestrengthishigh
(𝑡 =0.8𝑇),thestructure(legsofthehorse)isincorrectlymodified.

### Sunflower by

Vincent van Gogh
egamitnetnoC
tpmorp
elytS
noisuffiDelbatS
dnuorgyalP

### AppendixA AdditionalQualitativeResults

VisualizationAdditionalappearancestylizationisinFig.10,the
sourceimageisinFig.11.Agridofdifferentimageswithdifferent
stylesisinFig.12.AdditionalstructurecontrolisinFig.13and
Fig.14.

### Additionalqualitativecomparisonsonstylization.Weshow

anextendedcomparisonwiththepreviousreference-basedmethod
inFig.15.Morequalitativecomparisonswithexistingtext-driven
imagestylizationandmanipulationmethodscanbefoundinFig.16
andFig.17.
Additionalcomparisonsonfine-grainedcontrol.WeprovideadditionalcomparisonswithothercontrolmethodsinFig.18
andFig.19.TheseresultsdemonstratetheadvantageofDiffArtist
inprovidingdisentangledstructuralandappearance-levelstylecontrol.Inparticular,theCtrl-X,asanimageeditingmethod,produces
lessvisuallypleasingresultswhenappliedtoimagestylization.
Thisisbecausetheyhaveadifferentdefinitionofappearanceand
structureforeditingrealphotos.
AppendixB OntheStructureandAppearance
EntanglementinDiffusionProcess

### B.1 Theoreticalanalysis


### Wenowexplorehowthefactorizationofstructureandappearance

factorization,definedinEq.2,interactandevolvethroughoutthe
denoisingtrajectory𝑝 𝜃(x0 ,x1 ,...,x𝑇−1 ,|x𝑇).Specifically,suppose
thecontentimage𝐼 𝑐 isinvertedintox1:𝑇,inversion-basedstylizationstartsfromanintermediatestepx𝜏 ,𝜏 <𝑇 forDDIMdenoising
process.ByrearrangingEqn.1,weobtain:
√ 𝛼
x𝑡−1 =A𝑡x𝑡 +B𝑡 𝜖 𝜃(x𝑡 ,𝑡;𝑦), A𝑡 := √
𝛼
𝑡−1
𝑡
(7)
B𝑡 :=
√
1−𝛼 𝑡−1 −
√︁𝛼 𝑡−1
√
(1
𝛼
−𝛼 𝑡−1 )
𝑡
Basedonaboveformulation,thefullstylizationprocesscould
beexpressedas:
𝑇 𝑇  𝑘−1  xˆ0 = (cid:214) A𝑗 ·x𝑇 + ∑︁  B𝑘 (cid:214) A𝑗   𝜖′(x𝑘−1 ,𝑘)
 
𝑗=1 𝑘=𝜏+1 𝑗=𝜏+1 
(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32) (cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)
(cid:124) (cid:123)(cid:122) (cid:125)
A fauvism A traditional Post- Socialist preserveoriginalstructureandappearance (8)
painting, watercolor impressionist realism 𝜏  𝑘−1 
d s co t e r l t o o a r k i s l e e s d , v b i r v u i s d h p co a l i o n r t f i u n l g, p P a a i u n l t C in ez g a , n by n e. p d a et i a n i t l i e n d g, + 𝑘 ∑︁ =1     B𝑘 (cid:214) 𝑗=1 A𝑗     𝜖 𝜃(x𝑘−1 ,𝑘;𝑦),
(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32) (cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)
(cid:124) (cid:123)(cid:122) (cid:125)
generatenewstructureandappearance
where𝜖′denotesanidealdenoiserthatperfectlymodelsthetransitiondistribution𝑞(x𝑡−1 |x𝑡).InEq.8,theconceptualdenoising
termfromx𝑇 tox𝜏 preservesthestructureandappearancein𝐼 𝑐.
Thestylizationtrajectoryfromx𝜏tox𝑡iswhatisactuallycomputed,
whichintroducesthedesiredappearancebasedontheprompt𝑦but
Figure 8: DiffArtist implemented with different diffusion
architecture.WeimplementDiffArtistontheplayground-v2
diffusionmodel.Similarstylizationresultscouldbeachieved,
demonstratingthegeneralizabilityofproposedmethod.

<!-- Page 12 -->

MM’25,October27–31,2025,Dublin,Ireland RuixiangJiangandChangWenChen
Figure10:AdditionresultsforDiffArtist(withdefaultcontrolparameters).Theimagesemanticsarepreservedwithstrongand
high-fidelitystylesharmoniouslyintegrated.

<!-- Page 13 -->

DiffArtist:TowardsStructureandAppearanceControllableImageStylization MM’25,October27–31,2025,Dublin,Ireland
Figure11:ThecorrespondingsourceimagesofFigure10.

<!-- Page 14 -->

MM’25,October27–31,2025,Dublin,Ireland RuixiangJiangandChangWenChen
“Pencil sketch, “Cyberpunk “Starry-night “Futurism “Neo- “Cubism
detailed cross- style concept “American comic, style painting, “Painting by painting, expressionism painting,
Content image hatching” art, detailed” western style” by van Gogh” Edvard Munch” detailed” painting ” detailed
Figure12:Agridexperimentwithdifferentcontentandstyles.
mayalsoleadtouncontrolledstructuregeneration.Inthisparadigm, unweighteddenoisingstep𝜖(x𝑡 ,𝑡;𝑦) onthefinalstylizedimage
preservingoriginalappearanceandgeneratingnewstructureare remainsconsistentacrossdifferenttimestepsforbothstructureand
undesirablesideeffects.Intuitively,alarger𝜏 leadstoashortertra- appearance.Inotherwords,weassumetheSNRofstructureand
jectoryofx𝑇 →x𝜏,resultinginastrongerappearanceinxˆ0with appearancehasalinearrelationshipwiththatofthex𝑡 attime𝑡 as
weakerstructurepreservation(uncontrolledstructurestylization), characterizedbythenoiseschedule𝛼 1:𝑇:
w
pr
h
e
i
s
le
er
a
v
l
a
o
t
w
io
e
n
r
.
𝜏
In
sa
o
c
t
r
h
ifi
e
c
r
e
w
s
o
st
r
y
d
l
s
iz
,
a
o
t
n
io
e
n
c
s
a
t
n
re
n
n
o
g
t
th
ar
fo
b
r
it
s
r
t
a
r
r
o
i
n
ly
ge
c
r
on
st
t
r
r
u
o
c
l
t
t
u
h
r
e
e SNR(z 𝑐 𝑡)∝
1−
𝛼 𝑡
𝛼 𝑡
;SNR(z 𝑠 𝑡)∝
1−
𝛼 𝑡
𝛼 𝑡
, (10)
strengthofappearanceandstructurewithoutaffectingtheother. Itisimportanttonotethatwedonotassumethattherelativepro-
BycombiningEqn.2andEqn.8,wecanquantitativelyassess portionsofstructureandappearanceareidenticalateachdenoising
thestrengthofcontentpreservationandstylizationinthediffusion step.
process under a particular noise schedule𝛼 1:𝑇. Specifically, we Withtheaboveassumption,theeffectofvarying𝜏 onthestrucfurtherassumetheSNRofstructureandappearancehasalinear tureandappearanceofthefinalstylizedimagecouldbederived
relationshipwiththatofthex𝑡 for𝑡: inclosedform.Inpractice,weusethefollowingcodetocalculate
𝛼 𝛼
SNR(z 𝑐 𝑡)∝
1−
𝑡
𝛼 𝑡
;SNR(z 𝑠 𝑡)∝
1−
𝑡
𝛼 𝑡
(9) i
d
t
e
e
f
rat
c
i
u
v
m
e
_
ly
s
:
core(low_t, hi_t, alphas):
res = 0

### B.2 Simulation

for k in range(low_t + 1, hi_t):
Toderivethetheoreticaltrendsofstructureandappearancestrength for j in range(low_t + 1, k - 1):
res += A_t(j, alphas) * B_t(k, alphas)
duringthediffusionprocess,weintroduceanadditionalassumpreturn res
tion.Specifically,weassumethattherelativesignificanceofeach

<!-- Page 15 -->

DiffArtist:TowardsStructureandAppearanceControllableImageStylization MM’25,October27–31,2025,Dublin,Ireland
Figure13:Additionalresultonstructurecontrol-1.
struct_scores = [] • "pointillismstyle"
appear_scores = [] • "artdecostyle"
• "impressionismstyle"
for tau in range(0, 50):
• "surrealismstyle"
crt_struct = cum_score(50 - tau, 50, sampled_alphas)
crt_appear = cum_score(0, tau, sampled_alphas) • "popartstyle"
struct.append(crt_struct) • "cubismstyle"
appear_scores.append(crt_appear) • "abstractexpressionismstyle"
TheresultsforbothsimulationandempiricalresultsareinFig.7.

### B.3 EmpiricalResult

The result shows a good fit, and it turns out that the structure
DuetotheinherentinaccuracyofDDIMinversion,theestimation modification appears to be linear, with the stylization strength
ofx𝜏maybeimperfect,resultinginunintendedmodificationsinthe being quadratic with respect to𝜏. Moreover, this result further
finalsampledimageevenifnostyleprompt𝑦isused.Toaddress evidencedtheissueofS-Aentanglementinthediffusionprocess.
thisissue,weadoptanalternativestrategybyrandomlysampling
500Gaussiannoiseasthex𝑇 ofcontent,whicharepairedwith AppendixC DetailsonMLLM-basedmetrics
500contentprompts.Wetreattheimagesdenoisedusingcontent C.1 ImplementationDetails
promptsfor𝜏 =𝑇 stepsasthecontentimage,whichsimulatesa
Thestylizedimages,styleprompt,andtheinstructionpromptsare
perfectinversiontechnique.Tostylizeanimage,wefirstdenoise
thex𝑇 withthecontentpromptfor𝜏 steps,whichissubsequently fedtoMLLMforinference.Wecomposestylizedimagesasagrid
denoisedwiththestylepromptfor𝑇 −𝜏 steps.TheLPIPSbetween imagewithnumbersatthetop-leftcorner.Thefullprompttemplate
forstructureandappearancescoreisavailableinTab.6.
thestylizedimageandthecontentimageisusedastheempirical
structuralstrength.Incontrast,theCLIPDeceptionscore(correct

### C.2 CorrelationwithHumanPreference

classificationrateamongasetofstyles)isusedastheempirical
appearancestrength.Thefollowing10stylepromptsareused: HumanQuestionCollectionWedistributedthequestionnaireon
acrowd-sourcingplatform,whereeachparticipantwasrequiredto
• "watercolorstyle"
completeupto20randomlysampledrankingtasks.Anexampleof
• "fauvismstyle"
theuserinterfaceisprovidedinFig.20.Atotalof200participants
• "pencilsketchstyle"
took part in this study. To ensure the validity of the responses,

<!-- Page 16 -->

MM’25,October27–31,2025,Dublin,Ireland RuixiangJiangandChangWenChen
Figure14:Additionalresultonstructurecontrol-2.
weincludedattention-checkquestions.Ifaparticipantanswersan AppendixD AdditionalDiscussionand
attention-checkquestionincorrectly,alloftheirresponseswillbe Analysis
markedinvalid.Responsesthataremadewithlessthan20seconds
D.1 GeneralizabilityofDiffArtist
arealsoremoved.
TodemonstratethegeneralizabilityofDiffArtistacrossdifferent

### U-Net-baseddiffusionarchitectures,weimplementourmethodon

Playgroundv24,whichutilizestheSDXLarchitecture,distinctfrom

### StableDiffusion2.1.SeveralresultsareprovidedinFig.8.These

4https://huggingface.co/playgroundai/playground-v2-1024px-aesthetic

<!-- Page 17 -->

DiffArtist:TowardsStructureandAppearanceControllableImageStylization MM’25,October27–31,2025,Dublin,Ireland

### By pascal

campion and

### Rembrandt,

pastel colors,
Futurism
painting
Manga
comic
illustration
artwork by
Nicholas

### Roerich

Content imageStyleprompt Ours SD (reference) AdaIN ArtFlow StyTr2 StyleID StyleAligned InstantStyle
Figure15:Extendedcomparisonwithreference-basedstyletransfermethods.
resultsvalidatethatDiffArtistservesasaversatilecontrolmethod low-frequencystylefeaturessuchastonesandsmallobjects,while
applicabletovariousU-Net-baseddiffusionmodels,regardlessof addingmorelayersfacilitatesthecreationofhigh-frequencystyle
theirunderlyingarchitecturaldifferences. detailslikestrokeshapes.Empirically,wesettheS2Ainjection
layersto[1, 2]bydefault,asusingadditionallayerstypically
D.2 AdditionalAblationsonS2AInjection resultsinblurrinessinthestylizedoutputs.
Inthissection,weprovideadditionalablationstostudytheeffect

### D.3 FailureCase

ofproposedS2Adesign.
AblationonS2Alayers𝑆 𝑆2𝐴.Weablatethenumberofinjection Inourexperiment,weidentifyarare(<1%)andspecialfailurecase
layerusedintheS2Ainjection(i.e.,𝑆 𝑆2𝐴).AsillustratedinFig.21, intheproposedmethods.Specifically,forcertaincontentimage,
theS2Alayersinfluencethefrequencybandsofstyledelegation. its stylization result will consistently contains black and white
Incorporatingonlyearlylayers(e.g.,[1, 2])focusesongenerating chessboard-patternartifacts.WeprovideoneexampleinFig.9.

<!-- Page 18 -->

MM’25,October27–31,2025,Dublin,Ireland RuixiangJiangandChangWenChen
Postimpressionist,
van Gogh

### Ink-wash

gradient,
traditional
Regency era
painting,

### Thomas


### Gainsborough


### Art Brut style

Content image Styleprompt Ours DDIM Prompt2Prompt Plug-and-play CLIPStyler ControlNet InstructPix2Pix DiffStyler
Figure16:Extendedcomparisonwithexistingtext-drivenstylizationandmanipulationmethods.

<!-- Page 19 -->

DiffArtist:TowardsStructureandAppearanceControllableImageStylization MM’25,October27–31,2025,Dublin,Ireland

### Pixel-art,


### Retrospective

Minimalist art,
monochrome
Comic book,

### Retro vibe


### Neo-classical

Illustrative art,
retrospective
palette

### Magazine

vintage cover
illustration

### Gothic

intricate
patterns and
dark tones
Art Deco artwork
elegant,
streamlined lines,
with bold color
palette inspired by
Tamara de

### Lempicka

Content image Styleprompt Ours DDIM Prompt2Prompt Plug-and-play CLIPStyler ControlNet InstructPix2Pix DiffStyler
Figure17:Extendedcomparisonwithexistingtext-drivenstylizationandmanipulationmethods.

<!-- Page 20 -->

MM’25,October27–31,2025,Dublin,Ireland RuixiangJiangandChangWenChen
sruO
PnP+sruO

### X-lrtC

relytsffiD
Content Content
& Style & Style
Traditional

### Chinese

landscape
painting
elytStnatsnI
Structural Style Strength Appearance Style Strength
sruO
PnP+sruO

### X-lrtC

elytStnatsnI
relytsffiD
Still-Life
painting,
Cezanne
Starry

### Rococo

Nightstyle,
painting
van Gogh
Figure18:Extendedcomparisononfine-grainedstructuralandappearance-basedstylecontrol

<!-- Page 21 -->

DiffArtist:TowardsStructureandAppearanceControllableImageStylization MM’25,October27–31,2025,Dublin,Ireland
sruO
PnP+sruO

### X-lrtC

relytsffiD
Content Content
& Style & Style

### Cartoon

painting
using
markers.
Art Deco,
Geometric
design
elytStnatsnI
Structural Style Strength Appearance Style Strength
Neoexpressionist
painting,
bold stokes

### Medieval

portrait, oil
on canvas
sruO
PnP+sruO

### X-lrtC

elytStnatsnI
relytsffiD
Figure19:Extendedcomparisononfine-grainedstructuralandappearance-basedstylecontrol

<!-- Page 22 -->

MM’25,October27–31,2025,Dublin,Ireland RuixiangJiangandChangWenChen
Table6:PrompttemplatesforMLLM-basedmetrics.[IMG],[STYLE]and[NUM_METHOD]istheplaceholderforcombined
image,styleandnumberofmethods,respectively.

### StructureScore AppearanceScore

"[IMAGE] A content (source) image (top left) and "[IMAGE] A content (source) image (top left) and
[NUM_METHOD] stylized images in the style of [STYLE] [NUM_METHOD]stylizedimagesinthestyleof[STYLE]are
areplacedasagrid.""Thestylizedimagesareindexedfrom placedasagrid.""Thestylizedimagesareindexedfromleftto
left to right, and from top to bottom. " "Compare, analyze right,andfromtoptobottom.""Compare,analyzeanddiscrimand discriminately rank the fidelity to which the structure inatelyrankthefidelitytowhichtheappearancedescribedin
describedinthestyleof[STYLE]istransferredtothesource thestyleof[STYLE]istransferredandtothesourceimage."
image.""Youshouldfocusonthefidelityofstructure-related "Youshouldfocusonthefidelityofappearance-relatedartstyle
style component only, such as the lines, shapes, geometry, componentonly,suchasthetexture,color,stroke,andpattern.
layout, and perspective. You should not consider the style Notethatitdoesnotsimplymeanscolorpalletteandsaturation.
relatedtoappearance(e.g.,texture,color,stroke,andpattern). Youshouldnotconsiderthestylerelatedtostructure(e.g.,lines,
You should also consider how the structure of [STYLE] is shapes,geometry,layout,andperspective),unlesstheoriginal
integrated with the source image." "Stylized image that has scenebecomeunrecognizable.Youshouldalsoconsiderhow
(1) limited style strength, (2) structure that is mis-aligned theappearanceof[STYLE]isintegratedwiththesourceimage."
with the style, or (3) significant artifacts and distortions of "Stylizedimagethathas(1)limitedstylestrength,(2)visual
the semantic integrity (e.g., the original object and scene appearancethatismis-alignedwiththestyle,(3)significant
become unrecognizable) unless the distortion is explicitly artifacts and distortions of the semantic integrity (e.g., the
intended by the style of [STYLE], and (4) un-harmonious originalobjectandscenebecomeunrecognizable)unlessthe
integration with the source image should be considered of distortionisexplicitlyintendedbythestyleof[STYLE]and
in lower rank. In other words, if a stylized image is not an (4)un-harmoniousintegrationwiththesourceimageshould
artisticallymeaningfulpaintingofthesourceimageintarget beconsideredofinlowerrank.Inotherwords,ifastylized
style,thenitshouldberatedlower.Imagesthatharmoniously imageisnotanartisticallymeaningfulpaintingofthesource
integrate the structure of [STYLE] with the source image image in target style, then it should be rated lower. Images
shouldberatedhigher.""Rankthe[NUM_METHOD]images thatharmoniouslyintegratetexture,color,stroke,andpattern
in ascending order from 1 to [NUM_METHOD], where the shouldberatedhigher.""Rankthe[NUM_METHOD]images
highestrankof[NUM_METHOD]meansthebeststructural in ascending order from 1 to [NUM_METHOD], where the
fidelity.Noimagesshallhavethesameranking.""Asanexpert highestrankof[NUM_METHOD]meansthebestappearance
inart,returnyourthinkinginshort(whatstructureisdesired, fidelity.Noimagesshallhavethesameranking.""Asanexpert
and how the ranking is decided for each image in short), inart,returnyourthinking(whatappearanceisdesired,and
andranksforeachimageidinaPythonDict,[’thinking’:str, how the ranking is decided for each image in short), and
’rank’:List[[NUM_METHOD]]]. Do not include any other ranks for each image id in a Python Dict, [’thinking’:str,
stringinyourresponse." ’rank’:List[[NUM_METHOD]]]. Do not include any other
stringinyourresponse."

<!-- Page 23 -->

DiffArtist:TowardsStructureandAppearanceControllableImageStylization MM’25,October27–31,2025,Dublin,Ireland
Figure20:Exampleuserinterfaceincollectinghumanpreference.Thesystemwillpreventuserfromselectingthesame
ranking.

<!-- Page 24 -->

MM’25,October27–31,2025,Dublin,Ireland RuixiangJiangandChangWenChen
[1] [1,2] [1,2,3,4] [1,2,3,4,5,6] [1,2,3,4,5,6,7,8]
noitageled
elytS
hcnarb
niaM
noitageled
elytS
hcnarb
niaM

### C2S layer

Traditional

### Chinese

painting
Pointillism
painting
Figure21:AblationStudyonS2ALayers𝑆 𝑆2𝐴.IncreasingthenumberofS2Alayerscompelstheappearancedelegationto
generatehigher-frequencystylefeatures(stokes,points)whilediminishinglow-frequencytonalcomponents(largecolor
fields).Empirically,ourdefaultconfiguration[1,2]strikesanoptimalbalancebetweenenhancingstyledetailandpreserving
essentialcontentstructure.

## Tables

**Table (Page 1):**

|  |  |  |
|---|---|---|
|  | Structure style strength |  |
|  |  |  |


**Table (Page 1):**

|  |  |
|---|---|
| htgnerts elyts ecnaraeppA |  |


**Table (Page 5):**

| “8-Bit Pixel-art, detailed” |
|---|
| “Rococo painting” |


**Table (Page 5):**

| “Vincent van gogh, Egon schiele ” |
|---|
| “Cubism painting, fragmented, Picasso |


**Table (Page 6):**

| 0.46 |
|---|
| 27.14 |


**Table (Page 6):**

| 25.91 |  | 27.46 |  |  |  |  |  |
|---|---|---|---|---|---|---|---|
| 20.51 | 20.58 | 20.68 |  |  |  |  |  |
| 0.61 | 0.22 0.29 0.52 0.65 0.60 0.46 0.31 0.60 0.47 0.59 0.34 0.30 0.56 0.56 0.60 |  |  | 0.65 | 0.60 |  |  |
| 0.67 |  |  | 0.60 |  | 0.59 |  | 0.67 |
| 0.64 |  |  |  |  |  | 0.57 | 0.62 |


**Table (Page 7):**

|  |  |  |
|---|---|---|
|  | Structural Style Strength |  |
|  |  |  |


**Table (Page 7):**

|  | Appearance Style Strength |
|---|---|
|  |  |


**Table (Page 8):**

| Content Appearance Stylization Content Appearance Stylization & Style Delegation Result & Style Delegation) Result )A2S o/w( sruO )lluF( Cartoon An 8-Bit painting pixel art, sruO using detailed markers |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
|  | Cartoon painting using markers |  |  | An 8-Bit pixel art, detailed |  |  |  |  |


**Table (Page 8):**

| 0.29 0.12 0.44 0.004 0.42 0.02 |
|---|
| 0.05 0.73 0.27 0.11 0.25 0.05 0.48 0.04 |


**Table (Page 14):**

| “Pencil sketch, “Cyberpunk “Starry-night “Futurism “Neo- “Cubism detailed cross- style concept “American comic, style painting, “Painting by painting, expressionism painting, Content image hatching” art, detailed” western style” by van Gogh” Edvard Munch” detailed” painting ” detailed |
|---|
|  |
|  |
|  |
|  |
|  |
|  |


**Table (Page 14):**

| def cum_score(low_t, hi_t, alphas): |
|---|
| res = 0 |
| for k in range(low_t + 1, hi_t): |
| for j in range(low_t + 1, k - 1): |
| res += A_t(j, alphas) * B_t(k, alphas) |
| return res |
|  |


**Table (Page 15):**

| struct_scores = [] |
|---|
| appear_scores = [] |
|  |
| for tau in range(0, 50): |
| crt_struct = cum_score(50 - tau, 50, sampled_alphas) |
| crt_appear = cum_score(0, tau, sampled_alphas) |
| struct.append(crt_struct) |
| appear_scores.append(crt_appear) |


**Table (Page 18):**

|  |
|---|
| Post- impressionist, van Gogh |


**Table (Page 18):**

|  |  |
|---|---|
| Ink-wash gradient, traditional |  |


**Table (Page 18):**

|  |
|---|
| Regency era painting, Thomas Gainsborough |


**Table (Page 18):**

|  |  |
|---|---|
| Art Brut style |  |


**Table (Page 20):**

|  |  |
|---|---|
|  | Structural Style Strength |
|  |  |


**Table (Page 20):**

|  |  |
|---|---|
|  | Appearance Style Strength |
|  |  |


**Table (Page 21):**

|  |  |
|---|---|
|  | Structural Style Strength |
|  |  |


**Table (Page 21):**

|  |  |
|---|---|
|  | Appearance Style Strength |
|  |  |


**Table (Page 22):**

| StructureScore | AppearanceScore |
|---|---|
| "[IMAGE] A content (source) image (top left) and [NUM_METHOD] stylized images in the style of [STYLE] areplacedasagrid.""Thestylizedimagesareindexedfrom left to right, and from top to bottom. " "Compare, analyze and discriminately rank the fidelity to which the structure describedinthestyleof[STYLE]istransferredtothesource image.""Youshouldfocusonthefidelityofstructure-related style component only, such as the lines, shapes, geometry, layout, and perspective. You should not consider the style relatedtoappearance(e.g.,texture,color,stroke,andpattern). You should also consider how the structure of [STYLE] is integrated with the source image." "Stylized image that has (1) limited style strength, (2) structure that is mis-aligned with the style, or (3) significant artifacts and distortions of the semantic integrity (e.g., the original object and scene become unrecognizable) unless the distortion is explicitly intended by the style of [STYLE], and (4) un-harmonious integration with the source image should be considered of in lower rank. In other words, if a stylized image is not an artisticallymeaningfulpaintingofthesourceimageintarget style,thenitshouldberatedlower.Imagesthatharmoniously integrate the structure of [STYLE] with the source image shouldberatedhigher.""Rankthe[NUM_METHOD]images in ascending order from 1 to [NUM_METHOD], where the highestrankof[NUM_METHOD]meansthebeststructural fidelity.Noimagesshallhavethesameranking.""Asanexpert inart,returnyourthinkinginshort(whatstructureisdesired, and how the ranking is decided for each image in short), andranksforeachimageidinaPythonDict,[’thinking’:str, ’rank’:List[[NUM_METHOD]]]. Do not include any other stringinyourresponse." | "[IMAGE] A content (source) image (top left) and [NUM_METHOD]stylizedimagesinthestyleof[STYLE]are placedasagrid.""Thestylizedimagesareindexedfromleftto right,andfromtoptobottom.""Compare,analyzeanddiscrim- inatelyrankthefidelitytowhichtheappearancedescribedin thestyleof[STYLE]istransferredandtothesourceimage." "Youshouldfocusonthefidelityofappearance-relatedartstyle componentonly,suchasthetexture,color,stroke,andpattern. Notethatitdoesnotsimplymeanscolorpalletteandsaturation. Youshouldnotconsiderthestylerelatedtostructure(e.g.,lines, shapes,geometry,layout,andperspective),unlesstheoriginal scenebecomeunrecognizable.Youshouldalsoconsiderhow theappearanceof[STYLE]isintegratedwiththesourceimage." "Stylizedimagethathas(1)limitedstylestrength,(2)visual appearancethatismis-alignedwiththestyle,(3)significant artifacts and distortions of the semantic integrity (e.g., the originalobjectandscenebecomeunrecognizable)unlessthe distortionisexplicitlyintendedbythestyleof[STYLE]and (4)un-harmoniousintegrationwiththesourceimageshould beconsideredofinlowerrank.Inotherwords,ifastylized imageisnotanartisticallymeaningfulpaintingofthesource image in target style, then it should be rated lower. Images thatharmoniouslyintegratetexture,color,stroke,andpattern shouldberatedhigher.""Rankthe[NUM_METHOD]images in ascending order from 1 to [NUM_METHOD], where the highestrankof[NUM_METHOD]meansthebestappearance fidelity.Noimagesshallhavethesameranking.""Asanexpert inart,returnyourthinking(whatappearanceisdesired,and how the ranking is decided for each image in short), and ranks for each image id in a Python Dict, [’thinking’:str, ’rank’:List[[NUM_METHOD]]]. Do not include any other stringinyourresponse." |


**Table (Page 24):**

| [1] C2S layer noitageled Traditional Chinese painting elytS hcnarb niaM noitageled Pointillism painting elytS hcnarb niaM | [1,2] | [1,2,3,4] [1,2,3,4,5,6] [1,2,3,4,5,6,7,8] |
|---|---|---|
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
