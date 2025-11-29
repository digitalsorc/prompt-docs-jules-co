---
title: "Audio Language Integration"
original_file: "./Audio_Language_Integration.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["prompt-engineering", "llm", "rag", "agents", "fine-tuning"]
keywords: ["cid", "object", "org", "api", "semanticscholar", "corpusid", "clip", "urlhttps", "page", "view"]
summary: "<!-- Page 1 -->

3D Feature Distillation with Object-Centric Priors

### GeorgiosTziafas YuchengXu


### DepartmentofArtificialIntelligence SchoolofInformatics

UniversityofGroningen,theNeteherlands UniversityofEdinburgh,UnitedKingdom
g.t.tziafas@rug.nl Yucheng.Xu@ed.ac.uk

### ZhibinLi HamidrezaKasaei

DepartmentofComputerScience DepartmentofArtificialIntelligence
UniversityCollegeLondon,UnitedKingdom UniversityofGroningen,theNeteherlands
alex.li@ucl.ac.uk hamidreza.kasaei@rug.nl

### RGB Point"
related_documents: []
---

# Audio Language Integration

<!-- Page 1 -->

3D Feature Distillation with Object-Centric Priors

### GeorgiosTziafas YuchengXu


### DepartmentofArtificialIntelligence SchoolofInformatics

UniversityofGroningen,theNeteherlands UniversityofEdinburgh,UnitedKingdom
g.t.tziafas@rug.nl Yucheng.Xu@ed.ac.uk

### ZhibinLi HamidrezaKasaei

DepartmentofComputerScience DepartmentofArtificialIntelligence
UniversityCollegeLondon,UnitedKingdom UniversityofGroningen,theNeteherlands
alex.li@ucl.ac.uk hamidreza.kasaei@rug.nl

### RGB Point-Cloud knife teddy bear

Back-projected Features PCA (OpenScene) 3D Features PCA (OpenScene) Query Similarity (OpenScene)
Back-projected Features PCA (Ours) 3D Features PCA (Ours) Query Similarity (Ours)
Figure1: Visualizationof3Dfeatures(middle),back-projected2Dfeatures(left)andquerysimilarityheatmaps
(right),forOpenSceneandourDROP-CLIP.OpenScenefusespixel-wise2Dfeatureswithaveragepooling,
leadingtogroundingfailuresandfuzzyobjectboundaries.Ourmethodtacklessuchissuesusingobject-centric
priorstofuseobject-level2Dfeaturesin3Dinstancemaskswithsemantics-informedviewselection.
Abstract: Groundingnaturallanguagetothephysicalworldisaubiquitoustopic
withawiderangeofapplicationsincomputervisionandrobotics. Recently,2D
vision-languagemodelssuchasCLIPhavebeenwidelypopularized,duetotheir
impressivecapabilitiesforopen-vocabularygroundingin2Dimages. Subsequent
worksaim toelevate2DCLIP featuresto3Dvia featuredistillation, buteither
learnneuralfieldsthatarescene-specificandhencelackgeneralization,orfocuson
indoorroomscandatathatrequireaccesstomultiplecameraviews,whichisnot
practicalinrobotmanipulationscenarios. Additionally,relatedmethodstypically
fusefeaturesatpixel-levelandassumethatallcameraviewsareequallyinformative.
Inthiswork,weshowthatthisapproachleadstosub-optimal3Dfeatures,bothin
termsofgroundingaccuracy,aswellassegmentationcrispness. Toalleviatethis,
weproposeamulti-viewfeaturefusionstrategythatemploysobject-centricpriors
toeliminateuninformativeviewsbasedonsemanticinformation,andfusefeatures
atobject-levelviainstancesegmentationmasks. Todistillourobject-centric3D
features,wegeneratealarge-scalesyntheticmulti-viewdatasetofclutteredtabletop
scenes,spawning15kscenesfromover3300uniqueobjectinstances,whichwe
makepubliclyavailable. Weshowthatourmethodreconstructs3DCLIPfeatures
withimprovedgroundingcapacityandspatialconsistency,whiledoingsofrom
single-viewRGB-D,thusdepartingfromtheassumptionofmultiplecameraviews
attesttime. Finally,weshowthatourapproachcangeneralizetonoveltabletop
domainsandbere-purposedfor3Dinstancesegmentationwithoutfine-tuning,and
demonstrateitsutilityforlanguage-guidedroboticgraspinginclutter.
5202
guA
52
]VC.sc[
5v24781.6042:viXra

<!-- Page 2 -->

1 Introduction
Languagegroundingin3Denvironmentsplaysacrucialroleinrealizingintelligentsystemsthat
caninteractnaturallywiththephysicalworld. Intheroboticsfield,beingabletopreciselysegment
desiredobjectsin3Dbasedonopenlanguagequeries(objectsemantics,visualattributes,affordances,
etc.) canserveasapowerfulproxyforenablingopen-endedrobotmanipulation. Asaresult,research
focus on 3D segmentation methods has seen growth in recent years [1, 2, 3, 4, 5, 6]. However,
relatedmethodsfallintheclosed-vocabularyregime,whereonlyafixedlistofclassescanbeused
as queries. Inspired by the success of open-vocabulary 2D methods [7, 8, 9, 10], recent efforts
elevate2Drepresentationsfrompretrainedimagemodels [7,11]to3Dviadistillationpipelines
[12,13,14,15,16,17,18,19]. Inthiswork,weidentifyseverallimitationsofexistingdistillation
approaches. Ontheonehand,field-basedmethods [13,20,16,17,18]offercontinuous3Dfeature
fields,butrequiretobetrainedonlineinspecificscenesandhencecannotgeneralizetonovelobject
instancesandcompositions,theyrequireafewminutestotrain,andneedtocollectmultiplecamera
viewsbeforetraining,allofwhichhindertheirreal-timeapplicability. Ontheotherhand,original3D
featuredistillationmethodsandfollowupwork[12,14,21]useroomscandatasets [22,23]todistill
2Dfeaturesfusedfrommultipleviewswithpoint-cloudencoders. Thedistilledfeaturesmaintain
theopen-setgeneralizabilityofthepretrainedmodel,thereforegrantingsuchmethodsapplicablein
novelsceneswithopenvocabularies. However,suchapproachesassumethat2Dfeaturesfromall
viewsareequallyinformative,whichisnotthecaseinnaturalindoorsscenes,whereduetopartial
visibilityandclutter,certainviewswillleadtonoisyrepresentations. 2Dfeaturesarealsotypically
fusedpoint-wisefromViTpatches [9,10,8]ormulti-scalecrops[13,6],thereforeleadingtotheso
called“patchyness”issue[24](seeFig.1),wherefeaturescomputedinpatches/cropsthatinvolve
multipleobjectsleadtofuzzysegmentationboundaries. Thelatterissueisespeciallyimpactfulin
robotmanipulation,whereprecise3Dsegmentationisvitalforspecifyingrobustactuationgoals.
Toaddresssuchlimitations,inthiswork,werevisit2D→3Dfeaturedistillationwithpoint-cloud
encoders,butrevisethemulti-viewfeaturefusionstrategytoenhancethequalityofthetarget3D
features. In particular, we inject both semantic and spatial object-centric priors into the fusion
strategy,inthreeways: (i)Weobtainobject-level2Dfeaturesbyisolatingobjectinstancesineach
camera view from their 2D segmentation masks, (ii) we fuse features only at corresponding 3D
object regions using their 3D segmentation masks, (iii) we leverage dense object-level semantic
informationtodeviseaninformativenessmetric,whichisusedtoweightthecontributionofviewsand
eliminateuninformativeones. Extensiveablationstudiesdemonstratetheadvantagesofourproposed
object-centricfusionstrategycomparedtovanillaapproaches. Totrainourmethod,werequirea
large-scaleclutteredindoorsdatasetwithdensenumberofviewsperscene,whichiscurrentlynot
existent. Tothatend,webuildMV-TOD(Multi-ViewTabletopObjectsDataset),consistingof∼15k
Blenderscenesfrommorethan3.3kunique3Dobjectmodels,forwhichweprovide73viewsper
scenewith360◦coverage,furtherequippedwith2D/3Dsegmentations,6-DoFgraspsandsemantic
object-levelannotations. WeuseMV-TODtodistilltheobject-centric3DCLIP [7]featuresacquired
viaourfusionstrategyintoa3Drepresentation,whichwecallDROP-CLIP(DistilledRepresentations
withObject-centricPriorsfromCLIP).Our3Dencoderoperatesinpartialpoint-cloudsfromasingle
RGB-Dview, thusdepartingfromtherequirementofmultiplecameraimagesattesttime, while
offeringreal-timeinferencecapabilities. Byimposingthesame3Dfeaturesasdistillationtargetsfora
largenumberofdiverseviews,weencourageDROP-CLIPtolearnaview-invariant3Drepresentation.
Wedemonstratethatourlearned3Dfeaturessurpassprevious3Dopen-vocabularyapproachesin
semanticandreferringsegmentationtasksinMV-TOD,bothintermsofgroundingaccuracyand
segmentationcrispness,whilesignificantlyoutperformingprevious2Dapproachesinthesingle-view
setting. Further,weshowthattheycanbeleveragedzero-shotinnoveltabletopdatasetsthatcontain
real-worldsceneswithunseenobjectsandnewvocabulary,aswellasbeusedout-of-the-boxfor3D
instancesegmentationtasks,performingcompetitivelywithestablishedsegmentationapproaches
withoutfine-tuning.
Insummary,ourcontributionsarefourfold: (i)wereleaseMV-TOD,alarge-scalesyntheticdataset
ofhouseholdobjectsinclutteredtabletopscenarios, featuringdensemulti-viewcoverageandsemantic/mask/grasp annotations, (ii) we identify limitations of current multi-view feature fusion
2

<!-- Page 3 -->

Multi-view RGB-D images Aggregated point cloud Semantic & spatial object annotations Per-object descriptive concepts generation

### Category: Beverage can

Color: Red, white, silver
Material: Aluminum

### State: Sealed


### Brand: Coca-cola

GPT4-Vision Utility: Used for containing and consuming

### Affordance:


### I need something refreshing

S S e p m at a ia n l t : i c: 2 6 6 H G I D w D a r D e / t a 3 P o y n D F o t h S s s a G e e o t g r m a m s e e p t n h s t i a n t g io s n tylish de C s o cr n i c p e ti p o t ns More I I C S A d w f o l o e u e d a k e m s e a n l c i t l r n c c i i k a p u a a e t m n n c i o h o n d a ld s r v i : n i d n k r g i n c a k a n soda
to wear on my head
Figure 2: MV-TODOverview: Examplegeneratedscene, sourcemulti-viewRGB=Dimagesandscene
annotations(left).AutomaticsemanticannotationgenerationwithVLMS(right).
approachesandillustratehowtoovercomethembyleveragingobject-centricpriors,(iii)werelease
DROP-CLIP,a3Dmodelthatreconstructsview-independent3DCLIPfeaturesfromsingle-view,
and(iv)weconductextensiveablationstudies,comparativeexperimentsandrobotdemonstrations
toshowcasetheeffectivenessoftheproposedmethodintermsof3Dsegmentationperformance,
generalizationtonoveldomainsandtasks,andapplicabilityinrobotmanipulationscenarios.
2 Multi-ViewTabletopObjectsDataset
Existing3Ddatasetsmainlyfocusonindoorscenesinroomlay- Dataset Layout M Vi u e l w ti Clutter V D is a i t o a n R A ef n .E n x o p t. r. A G n r n a o sp t. C N a u t m eg .O or b ie j s . S N c u en m e . s N Ex u p m r. . S O em b a j. n -l t v ic l s
outs[33,22,26]andrelatedan- ScanNet[22] indoor (cid:34) - RGB-D,3D (cid:37) (cid:37) 17 800 − (cid:37)
S3DIS[25] indoor (cid:34) - RGB-D,3D (cid:37) (cid:37) 13 6 − (cid:37)
notationstypicallycoverclosed- Replica[26] indoor (cid:34) - RGB-D,3D (cid:37) (cid:37) 88 − − (cid:34)
STPLS3D[25] outdoor (cid:34) - 3D (cid:37) (cid:37) 12 18 − (cid:34)
setobjectcategories(e.g. furni- ScanRefer[1] indoor (cid:34) (cid:37) RGB-D,3D 2D/3Dmask (cid:37) 18 800 51.5k (cid:37)
ReferIt-3D[2] indoor (cid:34) (cid:37) RGB-D,3D 2D/3Dmask (cid:37) 18 707 125.5k (cid:37)
ture) [1, 2, 27, 34, 28], which ReferIt-RGBD[27] indoor (cid:34) (cid:37) RGB-D 2Dbox (cid:37) - 7.6k 38.4k (cid:37)
SunSpot[28] indoor (cid:37) (cid:34) RGB-D 2Dbox (cid:37) 38 1.9k 7.0k (cid:37)
are not practical for robot ma- GraspNet[29] tabletop (cid:37) (cid:34) 3D (cid:37) 6-DoF 88 190 − (cid:37)
nipulationtasks,wherecluttered R O E C G ID R - A V D LG [3 [ 0 3 ] 1] t t a a b b l l e e t t o o p p (cid:34) (cid:37) (cid:34) (cid:34) R R G G B B - - D D , , 3 3 D D 2D (cid:37) mask 6 4 - - D D o o F F 5 3 5 1 1 4 . 7 7 k k 89 − .6k tem (cid:37) plate
tabletop scenarios and open- Grasp-Anything[32] tabletop (cid:37) (cid:37) RGB 2Dmask 4-DoF 236 1M − open
MV-TOD(ours) tabletop (cid:34) (cid:34) RGB-D,3D 3Dmask 6-DoF 149 15k 671.2k open
vocabulary language are of key
Table1: ComparisonsbetweenMV-TODandexistingdatasets.
importance. Alternatively, recent grasp-related research efforts collect cluttered tabletop scenes,
but either lack language annotations [30, 35, 29] or connect cluttered scenes with language but
onlyfor4-DoFgraspswithRGBdata [31,32],hencelackingcrucial3Dinformation. Further,all
existingdatasetslackdensemulti-viewscenecoverage,grantingthemnonapplicablefor2D→3D
featuredistillation,wherewerequiremultipleimagesfromeachscenetoextract2Dfeatureswith
afoundationmodel. Tocoverthisgap,weproposeMV-TOD,alarge-scalesyntheticdatasetwith
clutteredtabletopscenesfeaturingdensemulti-viewcoverage,segmentationmasks,6-DoFgrasps
andrichlanguageannotationsattheobjectlevel(seeFig.2). Table1summarizeskeydifferences
betweenMV-TODandexistinggrounding/graspingdatasets.
MV-TODcontainsapproximately15kscenesgeneratedinBlender[36],comprisingof3379unique
object models, 99 collected by us and the rest filtered from ShapeNet-Sem model set [37]. The
dataset enumerates 149 object categories featuring typical household objects (kitchenware, food,
electronics etc.), each of which includes multiple instances that vary in fine-grained details such
ascolor,texture,shapeetc. Foreachobjectinstance,weleveragemodernvision-languagemodels
such as GPT-4-Vision [38] to generate textual annotations referring to various object attributes,
includingcategory,color,material,state,utility,brand,etc.,spawningover670kuniquereferring
instance queries. We refer the reader to Appendix A.1 for details on object statistics and scene
generationimplementation. Foreachscene,weprovide73uniformlydistributedviews,2D/3D
instancesegmentationmasks,6Dobjectposes,aswellasasetofreferringexpressionssampledfrom
theobject-levelsemanticannotations. Additionally,weprovidecollision-free6-DoFgraspposes
foreachsceneobject, originatingfromtheACRONYMdataset [35]. Inthispaper, weleverage
thedensemulti-viewcoverageofMV-TODfor2D→3Dfeaturedistillation. However,giventhe
breadthoflabelsinMV-TOD,webelieveitcanserveasaresourceforseveral3Dvisionandrobotics
3

<!-- Page 4 -->

Figure3: MethodOverview:Givena3Dsceneandmultiplecameraviews,weemploythreeobject-centric
priors(inred)formulti-viewfeaturefusion: (i)extractCLIPfeaturesfrom2Dmaskedobjectcrops,(ii)use
semanticannotationstofuse2Dfeaturesacrossviews,(iii)applythefusedfeatureonallpointsintheobject’s
3Dmask.Thefusedfeature-cloudisdistilledwithasingle-viewposedRGB-Dencoderandcosinedistanceloss.
Duringinference,wecomputepoint-wisecosinesimilarityscoresinCLIPspace(highersimilaritytowardsred).
downstreamtasks,includinginstancesegmentation,6Dposeestimationand6-DoFgraspsynthesis.
To the best of our knowledge, MV-TOD is the first dataset to combine 3D cluttered scenes with
multi-viewimages,open-vocabularylanguageand6-DoFgraspannotations.
3 DistilledRepresentationswithObject-CentricPriors
Our goal is to distill multi-view 2D CLIP features into a 3D representation, while employing an
object-centric feature fusion strategy to ensure high quality 3D features. Our overall pipeline is
illustratedinFig3. Wefirstintroducetraditionalmulti-viewfeaturefusion(Sec.3.1),presentour
variantwithobject-centricpriors(Sec.3.2),discussfeaturedistillationtraining(Sec.3.3)anddescribe
howtoperforminferencefordownstreamopen-vocabulary3Dgroundingtasks(Sec.3.4).
3.1 Multi-viewFeatureFusion
We assume access to a dataset of 3D scenes, where each scene is represented through a set of
V posed RGB-D views (cid:8) I ∈RH×W×3, D ∈RH×W, T ∈R4×4(cid:9)V , with H ×W denoting
v v v v=1
the image resolution, V the total number of views, and T the transformation matrix from each
v
camera’sviewpointv withrespecttoaglobalreferenceframe, suchasthecenterofthetabletop.
A projection matrix K representing each camera’s intrinsic parameters is also given. For each
v
scene we reconstruct the full point-cloud P ∈ RM×3 by aggregating all depth images D , after
v
projectingthemto3DwiththecameraintrinsicsK andtransformingtoworldframewithT−1. To
v v
removeredundantpoints,wevoxelizetheaggregatedpoint-cloudwithafixedvoxelsizeresolution
d3,resultinginM totalpoints. Ourgoalistoobtainafeature-cloudZ3D ∈RM×C,whereC isthe
dimensionoftherepresentationsprovidedbythepretrainedimagemodel,fusedacrossallviews.
2DfeatureextractionWepasseachRGBviewtoapretrainedimagemodelf2D : RH×W×3 →
RH×W×C toobtainpixel-levelfeaturesZ2D =f2D(I ). AnyViT-basedvisionfoundationmodel
v v
(e.g. DINO-v2 [11])canbechosen,butwefocusonCLIP [7],sincewewantour3Drepresentation
tobeco-embeddedwithlanguage,astoenableopen-vocabularygrounding. However,vanillaCLIP
features are restrained to image-level, whereas we require dense pixel-level features to perform
multi-viewfusion. Toobtainpixel-wisefeatures,previousworksexplorefine-tunedCLIPmodels
[12,15]suchasOpenSeg [9]orLSeg [10],multi-scalecropsfromanchoredpointsintheimage
frame [13, 6, 21] or MaskCLIP [8, 16], which provides patch-level text-aligned features from
CLIP’sViTencoderwithoutadditionaltraining. Allapproachesarecompatiblewithourframework
(ablationsinSec.4.1).
2D-3D correspondence Given the i-th point in P, x = (x,y,z), i = 1,...,M, we first backi
.
projecttoeachcameraviewvusing: u˜ =M (x )=K ·T ·˜x ,whereu˜ =(u ,u ,u )T and
v,i v i v v i x y z
x˜ =(x,y,z,1)T homogeneouscoordinatesin2Dcameraframeand3Dworldframerespectively,
4

<!-- Page 5 -->

andu=(u ,u )T. The2Dfeatureforeachback-projectedpointz2D ∈RC isthengivenby:
x y v,i
z2D =f2D(I (u ))=f2D(I (M (x ))) (1)
v,i v v,i v v i
Foreachview,weeliminatepointsthatfalloutsideofacameraview’sFOVbyconsideringonlythe
(cid:110) (cid:111)
pixels: u˜ =(u ,u ,u )T ∈M (P)|u ̸=0, u /u ∈[0,W), u /u ∈[0,H) . Itisfurther
v x y z v z x z y z
important to maintain only points that are visible from each camera view, as a point might lie
within the camera’s FOV but in practise be occluded by a foreground object. To eliminate such
points, wefollow [12,6]andcomparetheback-projectedzcoordinateu withthesensordepth
z
readingD (u ,u ). Wemaintainonlypointsthatsatisfy: |u −D (u ,u )| ≤ c ,wherec
v x y z v x y thr thr
a fixed hyper-parameter. We compose the FOV and occlusion filtering to obtain a visibility map
Λ ∈{0,1}V×M,whichdetermineswhetherpointiisvisiblefromviewv.
v,i
Fusing point-wise features Obtaining a 3D feature for each point i = 1,...,M is achieved by
fusingback-projected2DfeaturesZ2D withweighted-averagepooling:
v
(cid:80)V z2D·ω
z3D = v=1 v,i v,i (2)
i (cid:80)V
ω
v=1 v,i
where ω ∈ R a scalar weight that represents the importance of view v for point i. In practise,
v,i
previousworksconsiderω =Λ [12],abinaryweightforthevisibilityofeachpoint. Inessence,
v,i v,i
thismethodassumesthatallviewsareequallyinformativeforeachpoint, aslongasthepointis
visiblefromthatview.
Wesuggestthatnaivelyaveragepooling2Dfeaturesforeachpointleadstosub-optimal3Dfeatures,
asnoisy, uninformativeviewscontributeequally, therefore“polluting"theoverallrepresentation.
Inourworkweproposetodecomposeω =Λ ·G ,whereG ∈RV×M aninformativeness
v,i v,i v,i v,i
weightthatmeasurestheimportanceofeachviewforeachpoint. Inthenextsubsection,wedescribe
how to use text data to dynamically compute an informativeness weight for each view based on
semanticobject-levelinformation,aswellashowtoperformobject-wiseinsteadofpoint-wisefusion.
3.2 EmployingObject-CentricPriors
Let (cid:8) S2D ∈{0,1}N×H×W(cid:9)V beview-aligned2Dinstance-wisesegmentationmasksforeach
v v=1
scene,whereN thetotalnumberofsceneobjects,providedfromthetrainingdataset.Weaggregatethe
2DmaskstoobtainS3D ∈{1,...,N}M,suchthatforeachpointiwecanretrievethecorresponding
objectinstancen =S3D.
i i
SemanticinformativenessmetricLetQ = {Q
k

## }K

k=1

## , Q

k
∈ RNk×C beasetofobject-specific
textualprompts, whereK thenumberofdatasetobjectinstancesandN thenumberofprompts
k
forobjectk. WeuseCLIP’stextencodertoembedthetextualpromptsinRC andaveragethem
toobtainanobject-specificpromptq =1/N ·
(cid:80)Nk
Q . Foreachscene,wemapeachobject
k k j=1 k,j .
instancen∈[1,N]toitspositivepromptq+,aswellasasetQ− =Q−{q+}ofnegativeprompts
n n n
correspondingtoallotherinstances. Wedefineoursemanticinformativenessmetricas:
G =cos(z2D,q+)−max cos(z2D,q) (3)
v,i v,i ni q∼Q−
ni
v,i
Intuitively, we want a 2D feature from view v to contribute to the overall 3D feature of point i
accordingtohowmuchitssimilaritywiththecorrectobjectinstanceishigherthanthemaximum
similaritytoanyofthenegativeobjectinstances,henceofferingaproxyforsemanticinformativeness.
Weclipthisweightto0toeliminateviewsthatdon’tsatisfytheconditionG ≥0. Plugginginour
v,i
metricinequation(2)alreadyprovidesimprovementsovervanillaaveragepooling(seeSec.4.1),
however,doesnotdealwith3Dspatialconsistency,forwhichweemployourspatialpriorsbelow.
Object-level2DCLIPfeaturesForobtainingobject-level2DCLIPfeatures,weisolatethepixels
foreachobjectnfromeachviewv fromS2D andcropaboundingboxaroundthemaskfromI :
v,n v
z2D =f2D(cid:0) cropmask(I , S2D) (cid:1) (seeAppendixA.3forablationsinCLIPvisualprompts). Here
v,n cls v v,n
5

<!-- Page 6 -->

weusef2D :Rhn×wn×3 →RC,i.e.,onlythe[CLS]featureofCLIP’sViTencoder,torepresentan
cls
objectcropofsizeh ×w . Wecannowdefineourmetricfromequation(3)alsoatobject-level:
n n
G =cos(z2D,q+)−max cos(z2D,q) (4)
v,n v,n n q∼Q−
n
v,n
whereG ∈RV×N nowrepresentsthesemanticinformativenessofviewvforobjectinstancen.
v,n
Fusingobject-wisefeaturesA3Dobject-levelfeaturecanbeobtainedbyfusing2Dobject-level
featuresacrossviewssimilartoequation(2):
(cid:80)V z2D ·ω (cid:80)V z2D ·Λ ·G
z3D = v=1 v,n v,n = v=1 v,n v,n v,n (5)
n (cid:80)V
ω
(cid:80)V

## Λ ·G

v=1 v,n v=1 v,n v,n
whereeachviewisweightedbyitssemanticinformativenessmetricG ,aswellasoptionallya
v,n
visibilitymetricΛ = (cid:80) S2D thatmeasuresthenumberofpixelsfromn-thobject’smaskthatare
v,n v,n
visiblefromviewv [6]. Wefinallyreconstructthefullfeature-cloudZ3D ∈ RM×C byequating
eachpoint’sfeaturetoitscorresponding3Dobject-levelonevia: z3D =z3D, n =S3D.
i ni i i
3.3 View-IndependentFeatureDistillation
Eventhoughtheabovefeature-cloudZ3D couldbedirectlyusedforopen-vocabularygroundingin
3D,itsconstructioniscomputationallyintensiveandrequiresalotofexpensiveresources,suchas
accesstomultiplecameraviews,view-aligned2Dinstancesegmentationmasks,aswellastextual
prompts to compute informativeness metrics. Such utilities are rarely available in open-ended
scenarios,especiallyinroboticapplications,whereusuallyonlysingle-viewRGB-Dimagesfrom
sensorsmountedontherobotareprovided. Totacklethis,wewishtodistillalltheaboveknowledge
fromthefeature-cloudZ3D withanencodernetworkthatreceivesonlyapartialpoint-cloudfrom
single-viewposedRGB-D.Hence,theonlyassumptionthatwemakeduringinferenceisaccessto
cameraintrinsicandextrinsicparameters,whichisamildrequirementinmostroboticpipelines.
Inparticular,givenapartialcoloredpoint-cloudfromviewv: P
v
∈ RMv×6,wetrainanencoder

## E

θ
: RMv×6 → RMv×C such that E
θ

## (P

v
) = Z3D. Notice that the distillation target Z3D is
independentofviewv. Following [12,15]weusecosinedistanceloss:
L(θ)=1−cos(E (P ), Z3D) (6)
θ v
SeeAppendixA.2fortrainingimplementationdetails. Withsuchasetup,wecanobtain3Dfeatures
that: (i)areco-embeddedinCLIPtextspace,sotheycanbeleveragedfor3Dsegmentationtasks
fromopen-vocabularyqueries, (ii)areensuredtobeoptimallyinformativeperobject, duetothe
usageofthesemanticinformativenessmetrictocomputeZ3D,(iii)maintain3Dspatialconsistency
inobjectboundaries,duetoperformingobject-wiseinsteadofpoint-wisefusionwhencomputing
Z3D, and (iv) are encouraged to be view-independent, as the same features Z3D are utilized as
distillationtargetsregardlessoftheinputviewv. Importantly,nolabels,prompts,orsegmentation
masksareneededattest-timetoreproducethefusedfeature-cloud,whileobtainingitamountstoa
singleforwardpassofour3Dencoder,henceofferingreal-timeperformance.
3.4 Open-Vocabulary3DSegmentation
Givenapredictedfeature-cloudZˆ3D = E (P ), wecanperform3Dgroundingtasksfromopen-
θ v
vocabulariesbycomputingcosinesimilaritiesbetweenCLIPtextembeddingsandZˆ3D.
Semantic segmentation In this task, the queries correspond to an open-set of textual prompts
Q={q }K describingKsemanticclasses. AclassforeachpointYˆ ∈{1,...,K}M isgivenby:
k k=1
Yˆ =argmax cos(Zˆ3D,q ).
k k
ReferringsegmentationHeretheuserprovidesanopen-vocabularyqueryq+referringtoaparticular
objectinstance,andoptionallyasetofnegativepromptsQ− ∈ RN−×C,whichinpractisecanbe
initialized from an open-set as above or with canonical phrases (e.g. ‘object’, ‘thing’ etc.) [13].
6

<!-- Page 7 -->

Figure4: Open-Vocabulary3DReferringSegmentationinMV-TOD.Examplesoflearned3Dfeaturesand
groundingheatmapsfromopen-endedlanguagequeries(classnames,attributes,useraffordances,andopen
instance-specificconcepts)inscenesfromMV-TODdataset.Pointsarecoloredbasedontheirquerysimilarity
(highertowardsred).Wenotethattablepointsareexcludedfromsimilaritycomputationinourvisualizations.
(cid:16) (cid:17)
Similarityscoresareconvertedtoprobabilities: P =softmax 1 ·cos(Zˆ3D, [q+,Q−]T) ,where
γ
γ atemperaturehyper-parameterandP = [ρ+,P−]probabilitiesofpositivematchingρ+ ∈ RM
andnegativematchingP− =[ρ−,...,ρ− ]∈RM×N− respectively. Thefinal3Dsegmentationis

## 1 N−

givenbySˆ = (cid:0) ρ+ >max P−(cid:1) ,orbythresholdingρ+withafixedthresholds (seeablations
i i j i,j thr
inAppendixA.3)
InstancesegmentationSinceourencoderhasbeendistilledwiththeaidofinstance-wisesegmentation masks, the obtained features can be utilized out-of-the-box for 3D instance segmentation
tasks. WedemonstratethatwithasimpleclusteringalgorithmoverZˆ3D wecanobtain3Dinstance
segmentationmasksforclutteredscenes,wherenaive3Dcoordinateclusteringwouldfail,performingcompetitivelywithpopularsegmentationmethodsinunseendatainthesingle-viewsetting(see
Sec.4.3). WereferthereadertoAppendixA.6.2forimplementationdetailsandrelatedvisualizations.
4 Experiments
Wedesignourexperimentstoexplorethefollowingquestions:(i)Sec.4.1:Whatarethecontributions
of our proposed object-centric priors for multi-view feature fusion? Does the dense number of
views of our proposed dataset also contribute? (ii) Sec. 4.2: How does our method compare to
state-of-the-artopen-vocabularyapproachesforsemanticandreferringsegmentationtasks,bothin
multi-andinsingle-viewsettings? Isitrobusttoopen-endedlanguage? (iii)Sec.4.3: Whatarethe
zero-shotgeneralizationcapabilitiesofourlearned3Drepresentationinnoveldatasetsthatcontain
real-worldscenes,aswellasforthenoveltaskof3Dinstancesegmentation? (v)Sec.4.4: Canwe
leverageDROP-CLIPforlanguage-guided6-DoFroboticgrasping?
4.1 Multi-viewFeatureFusionAblationStudies
Toevaluatethecontributionsofourproposedobject- Fusion f2D Λv,i Gv,i
mIoU Pr

## R

@
e
2
f.
5
Segm
Pr@
(%
5
)
0 Pr@75
centric priors, we conduct ablation studies on the
point patch (cid:33) 37.3 55.4 33.7 16.7
multi-view feature fusion pipeline, where we compoint patch (cid:33) 57.0 74.1 59.5 40.9
pare3Dreferringsegmentationresultsofobtained3D point patch (cid:33) (cid:33) 57.4 77.0 60.9 39.9
featuresinheld-outscenesofMV-TOD.Wehighlight obj obj 65.6 67.0 65.4 64.1
obj obj (cid:33) 67.3 68.7 67.1 65.8
thathereweaimtoestablishaperformanceupper- obj obj (cid:33) 83.1 83.9 83.1 82.4
boundthatthefeaturefusionmethodcanprovidefor obj obj (cid:33) (cid:33) 80.9 83.1 80.2 79.7
distillation,andnotthedistilledfeaturesthemselves.

### Table2: Multi-viewfeaturefusionablationstudy

Weablate: (i)patch-wisevs. object-wisefusion,(ii)
for3DreferringsegmentationinMV-TOD.
MaskCLIP[8]patch-levelvs. CLIP[7]maskedcrop
7

<!-- Page 8 -->

features, (iii) inclusion of visibility (Λ ) and semantic informativeness (G ) metrics for view
v,i v,i
selection. Wereport3DsegmentationmetricsmIoUandPr@X [39]. ResultsinTable2.
Effect of object-centric priors We observe that all components contribute positively to the quality of the 3D features.
OurproposedG metricboostsmIoUacrossbothpoint-and
v,i
object-wisefusion(57.0%vs. 44.2%and83.1%vs. 65.6%respectively). Further,weobservethattheusageofspatialpriors
forobject-wisefusionandobject-levelfeaturesleadstodrastic
improvements,bothinsegmentationcrispness(25.7%mIoU
delta),aswellasingroundingprecision(42.5%Pr@75delta).
Effect of the number of views We ablate the 3D referring Figure5: Referringsegmentationpresegmentationperformancebasedonthenumberofinputviews cisionvs.numberofutilizedviews.
in Fig. 5, where novel viewpoints are added incrementally.
Weobservethatinbothsetups(point-andobject-wise)fusingfeaturesfrommoreviewsleadsto
improvements,withasmallplateauingbehavioraround40views. Webelievethisisanencouraging
resultforleveragingdensemulti-viewcoverageinfeaturedistillationpipelines,asweproposewith
MV-TOD. Please see Appendix A.3 for extended ablation studies that justify the design choices
behindourfusionstrategy,andAppendixA.5forqualitativecomparisonswithvanillaapproaches.
4.2 Open-Vocabulary3DSegmentationResultsinMV-TOD
Inthissection,wecomparereferringandsemanticsegmentationperformanceofourdistilledfeatures
vs. previousopen-vocabularyapproaches,bothinmulti-viewandinsingle-viewsettings.
Formulti-view,wecompareourtrainedmodel

### Method #views Ref.Segm.(%) Sem.Segm(%)

with OpenScene [12] and OpenMask3D [6] mIoU Pr@25 Pr@50 Pr@75 mIoU mAcc25
methods, where the full point-cloud from all OpenScene† 73 29.3 44.0 24.5 11.3 21.8 32.1

### OpenMask3D∗† 73 65.4 73.1 64.0 57.4 59.5 66.5

73 views is given as input. We note that for DROP-CLIP∗† 73 82.7 86.1 82.4 79.2 75.4 80.0

## Drop-Clip 73 66.6 75.7 67.6 59.9 62.0 70.7

thesebaselinesweobtaintheupper-bound3D OpenSeg→3D 1 12.9 17.4 2.4 0.2 12.8 17.2

### MaskCLIP→3D 1 25.6 40.4 18.7 7.0 21.0 32.1

features as before, as we observed that our DROP-CLIP 1 62.3 72.0 62.8 53.9 54.5 64.4
trainedmodelalreadyoutperformsthem,sowe Table3: ReferringandSemanticsegmentationresults
refrainedfromalsodistillingfeaturesfrombase- onMV-TODtestsplit. Methodswith† denoteupperlines.Forsingle-view,wefeedournetworkwith bound3Dfeatures,whereasDROP-CLIPdenotesour
distilled model. Methods with →3D produce 2D prepartialpoint-cloudfromprojectedRGB-Dpair,
dictions that are projected to 3D to compute metrics.
andcomparewith2DbaselinesMaskCLIP[8]

### Methods with ∗ denote further usage of ground-truth

andOpenSeg[9](seeimplementationdetailsin segmentationmasks.
AppendixA.4). Ourmodelslightlyoutperforms
theOpenMask3Dupperboundbaselineinthe
multi-viewsetting(+1.18%inreferringand+2.57%insemanticsegmentation),whilesignificantly
outperforming2Dbaselinesinthesingle-viewsetting(>30%inbothtasks).Importantly,single-view
resultscloselymatchthemulti-viewones(∼ −4.0%),suggestingthatDROP-CLIPindeedlearns
view-independentfeatures. SeeAppendixA.5formorequalitativecomparisonswithbaselines.

### Open-endedqueriesWeevaluatetherobustnessofour

modelindifferenttypesofinputlanguagequeries,organized in 4 families (class name - e.g. “cereal", class +
attribute-e.g. “browncerealbox",open-e.g. “chocolateKellogs", andaffordance-e.g. “Iwantsomething
sweet‘). ComparativeresultsarepresentedinFig.6and
qualitativeinFig.4. Weobservethatsingle-viewperformancecloselyfollowsthatofupper-boundacrossquery
types,withmulti-wordaffordancequeriesbeingthehighestfamilyoffailures,potentiallyduetothe"bag-of-words"
Figure6: Referringsegmentationprecision
behaviorofCLIPtextembeddings[16].
vs.languagequerytypes.
8

<!-- Page 9 -->

Figure7: Zero-Shot3DSemanticSegmentationinRealScenes:ComparisonofdifferentreferringsegmentationmodelsforfiveexampleclutteredindoorscenesfromtheOCIDdataset.PCAfeaturesaredisplayedat
pixel-levelfor2DmethodsLSegandMaskCLIPandin3Dforourpoint-cloud-basedDROP-CLIP.Heatmaps
from2DmodelsLSegandMaskCLIPareprojectedto3DfordirectcomparisonwithDROP-CLIP.
4.3 GeneralizationtoNovelDomains/Tasks
Zero-shottransfertoreal-worldscenesInthissection,weevaluatethezero-shotgeneralization
capabilityofDROP-CLIPinreal-worldscenesthatcontainobjectsandvocabularyoutsidetheMV-
TOD distribution. We test in the validation split of the OCID-VLG [31] dataset, which contains
1249queriesfrom165uniqueclutteredtabletopscenes. Wecomparewith2DCLIP-basedbaselines
LSeg[10],OpenSeg[9]andMaskCLIP[8]andpopular2DgroundingmethodGroundedSAM[40]
forthesemanticsegmentationtaskinthesingle-viewsettingasbefore.

## Ocid-Vlg

ResultsarepresentedinTable4. Wefindthateventhoughfine- Method
tunedinrealdata,baselinesLSegandOpenSegunder-perform
mIoU mAcc50 mAcc75

### GroundedSAM 33.93 39.0 36.0

comparedtobothMaskCLIPandourDROP-CLIPwithamar-

### LSeg→3D 44.1 37.9 23.5

ginof>10%mIoU,whichweattributetothedistributiongap OpenSeg→3D 47.1 33.1 19.1
betweenthefine-tuningdatasetADE20K[41]andOCIDscenes. MaskCLIP→3D 57.1 59.4 31.0

## Drop-Clip 60.2 60.1 38.7


### Thesebaselinestendtogroundmultipleregionsinthescene,

Table4: Zero-shotsemanticsegmenwhileMaskCLIPandDROP-CLIPprovidestightersegmentatationresults(%)inthevalidationsplit
tions(seeFig.7). WhenconsideringthestrictermAcc 75 metric, oftheOCID-VLGreal-worlddataset.
ourapproachscoresadeltaof7.7%comparedtoMaskCLIP,
suggestingasignificantgainingroundingaccuracy,especiallyincaseswheretheobjectisheavily
occluded. Failurescaseswereobservedingroundingobjectsthatsignificantlyvaryingeometryand
semanticsfromtheMV-TODcatalog. PleaseseeAppendixA.6forfurtherzero-shotexperiments,
comparisonswithmodernNeRF/3DGSmethodsandmorequalitativeresults.
Zero-shot 3D instance segmentation We evaluate the OCID-VLG MV-TOD

### Method

potentialofDROP-CLIPforout-of-the-box3Dinstance mIoU AP25 mIoU AP25
segmentation via clustering the predicted features (see SAM 60.1 95.3 70.1 95.2

## Drop-Clip(S) 50.9 68.0 80.8 91.9

detailsinAppendixA.6.2). Weconductexperimentsfor

### Mask3D - - 14.4 18.7

boththemulti-viewsettinginMV-TOD,wherewecom-

## Drop-Clip(F) - - 88.3 93.3

parewithMask3D[42]transferredfromtheScanRefer[1]
Table 5: Zero-shot3Dinstancesegmentacheckpointprovidedbytheauthors, wherewefeedfull
tionresultsinOCID-VLG(real-world)and
point-clouds from 73 views, as well as in OCID-VLG, ourMV-TODdataset.
where we compare with SAM [43] ViT-L model with
single-view images. Results are summarized in Table 5. We observe that Mask3D struggles to
9

<!-- Page 10 -->

generalizetotabletopdomains,asithasbeentrainedinroomlayoutdatawithmostlyfurnitureobject
categories. DROP-CLIPachievesanAP of93.3%,illustratingthatthelearned3Dfeaturescan
25
providenear-perfectinstancesegmentationin-distribution,evenwithoutexplicitfine-tuning. When
movingout-of-distributioninthesingle-viewsetting,weobservethatDROP-CLIPachievesmIoU
thatiscompetitivewithfoundationsegmentationmethodSAM(50.9%vs. 60.1%). Failurecases
includeheavilyclutteredregionsofsimilarobjectswithsametexture(e.g. foodboxes),forwhich
DROP-CLIPassignsverysimilarfeaturesthatareidentifiedasasinglecluster.
4.4 Application: Language-guidedRoboticGrasping
Inthissection, wewishtoillustratetheapplicabilityof Pick the biscuit box Feature PCA
DROP-CLIPinalanguage-guidedroboticgraspingscenario. We integrate our method with a 6-DoF grasp detection network [44], which proposes gripper poses for

### Query Similarity & Grasp Proposal

pickingatargetobjectsegmentedbyDROP-CLIP.Werandomlyplace5-12objectsonatabletopwithdifferentlevels
of clutter, and query the robot to pick a specific object,
potentiallyamongstdistractorobjectsofthesamecategory.

### Figure8: Language.-guided6-DoFgrasp-

Theuserinstructionisopen-vocabularyandcaninvolve
ing: Examplerobottrial(left),3Dfeatures,
openobjectdescriptions, attributes, oruser-affordances. groundingandgraspproposal(right).

### Weconducted50trialsinGazebo[45]and10withareal

robot,andobservedgroundingaccuracyof84%and80%respectively,andafinalsuccessrateof64%
and60%. Motionfailuresweremostlyduetograspproposalsforwhichthemotionplanningledto
collisions. SimilartoOCID,groundingfailureswereduetounseenqueryconceptsand/orinstances.
ExampletrialsareshowninFig.8,moredetailsinAppendixA.7andarobotdemonstrationvideois
providedassupplementarymaterial.
5 Relatedwork
Webrieflydiscussrelatedeffortsinthissection,whileadetailedcomparisonisgiveninAppendixA.8.
3DSceneUnderstandingThere’salonglineofworksinclosed-set3Dsceneunderstanding[46,47,
48,49,50,51],appliedin3Dclassification[52,53],localization[54,1]andsegmentation[55,23,22],
using two-stage pipelines with instance proposals from point-clouds [56, 57] or RGB-D views
[58, 27], or single-stage methods [3] that leverage 3D-language cross attentions. [59] use CLIP
embeddingsforpretraininga3Dsegmentationmodel,butstillcannotbeappliedopen-vocabulary.
Open-VocabularyGroundingwithCLIPFollowingtheimpressiveresultsofCLIP[7]foropen-set
imagerecognition,followupworkstransferCLIP’spowerfulrepresentationsfromimage-topixellevel[60,61,62,63,64,65,66,9,10,8],extendingtodetection/segmentation,butlimitedto2D.
For3Dsegmentation,theclosestworkisperhapsOpenMask3D[6]thatextractsmulti-viewCLIP
featuresfromobjectproposalsfromMask3D[42]tocomputesimilaritieswithtextqueries.
3DCLIPFeatureDistillationRecentworksdistillfeaturesfrom2Dfoundationmodelswithpointcloud encoders [12, 14, 21] or neural fields [13, 19, 17, 18, 19, 24], with applications in robot
manipulation[20,16]andnavigation[67,68]. However,associatedworksextract2Dfeaturesfrom
OpenSeg[9],LSeg[10],MaskCLIP[8]ormulti-scalecropsfromCLIP[7]andfusepoint-wisewith
averagepooling,whileourapproachleveragessemantics-informedviewselectionandsegmentation
maskstodoobject-wisefusionwithobject-levelfeatures. Unlikeallabovefield-basedapproaches,
ourmethodcanbeusedreal-timewithouttheneedforcollectingmultiplecameraimagesattest-time.
6 Conclusion,Limitations&FutureWork
WeproposeDROP-CLIP,a2D→3DCLIPfeaturedistillationframeworkthatemploysobject-centric
priors to select views based on semantic informativeness and ensure crisp 3D segmentations via
10

<!-- Page 11 -->

leveragingsegmentationmasks. Ourmethodisdesignedtoworkfromsingle-viewRGB-D,encouragingview-independentfeaturesviadistillingfromdensemulti-viewscenecoverage. Wealsorelease
MV-TOD,alarge-scalesyntheticdatasetofmulti-viewtabletopsceneswithdensesemantic/mask/
graspannotations.Webelieveourworkcanbenefitthecommunity,bothintermsofreleasedresources
aswellasillustratingandovercomingtheoreticallimitationsofexisting3Dfeaturedistillationworks.
Whileourspatialobject-centricpriorsleadtoimprovedsegmentationquality,theycollapselocal
featuresinfavorofaglobalobject-levelfeature,andhencecannotbeappliedforsegmentingobject
parts. Inthefuture,weplantoaddobjectpartannotationsinourdatasetandfusewithbothobjectandpart-levelmasks. Second,DROP-CLIPcannotreconstruct3Dfeaturesthathavesignificantly
differentgeometryand/orsemanticsfromtheobjectcatalogusedduringdistillation. Inthefuture
weaimtoexploremoderngenerativetext-to-3Dmodelstofurtherscaleuptheobjectandconcept
varietyofMV-TOD.Finally, regardingroboticapplication, currentlyDROP-CLIPonlyprovides
languagegrounding,andatwo-stagepipelineisnecessaryforrobotgrasping,whileMV-TODalready
providesrich6-DoFgraspannotations. Anextstepwouldbetoalsodistillthem,optingforajoint
3Drepresentationforgroundingsemanticsandgraspaffordances.

### References

[1] D.Z.Chen,A.X.Chang,andM.Nießner. Scanrefer: 3dobjectlocalizationinrgb-dscans
usingnaturallanguage. InComputerVision–ECCV2020: 16thEuropeanConference,Glasgow,
UK,August23–28,2020,Proceedings,PartXX16,pages202–221.Springer,2020.
[2] P.Achlioptas,A.Abdelreheem,F.Xia,M.Elhoseiny,andL.Guibas. Referit3d:Neurallisteners
forfine-grained3dobjectidentificationinreal-worldscenes. 16thEuropeanConferenceon
ComputerVision(ECCV),2020.
[3] J.Luo,J.Fu,X.Kong,C.Gao,H.Ren,H.Shen,H.Xia,andS.Liu. 3d-sps: Single-stage3d
visualgroundingviareferredpointprogressiveselection. InProceedingsoftheIEEE/CVF
ConferenceonComputerVisionandPatternRecognition,pages16454–16463,2022.
[4] P.-H.Huang, H.-H.Lee, H.-T.Chen, andT.-L.Liu. Text-guidedgraphneuralnetworksfor
referring 3d instance segmentation. In Proceedings of the AAAI Conference on Artificial
Intelligence,volume35,pages1610–1618,2021.
[5] Z.Qian,Y.Ma,J.Ji,andX.Sun. X-refseg3d: Enhancingreferring3dinstancesegmentation
viastructuredcross-modalgraphneuralnetworks. InProceedingsoftheAAAIConferenceon
ArtificialIntelligence,volume38,pages4551–4559,2024.
[6] A.Takmaz,E.Fedele,R.W.Sumner,M.Pollefeys,F.Tombari,andF.Engelmann.Openmask3d:
Open-vocabulary 3d instance segmentation. ArXiv, abs/2306.13631, 2023. URL https:
//api.semanticscholar.org/CorpusID:259243888.
[7] A. Radford, J. W. Kim, C. Hallacy, A. Ramesh, G. Goh, S. Agarwal, G. Sastry, A. Askell,
P.Mishkin,J.Clark,G.Krueger,andI.Sutskever. Learningtransferablevisualmodelsfrom
naturallanguagesupervision. CoRR,abs/2103.00020,2021. URLhttps://arxiv.org/abs/
2103.00020.
[8] X. Dong, Y. Zheng, J. Bao, T. Zhang, D. Chen, H. Yang, M. Zeng, W. Zhang, L. Yuan,
D.Chen,F.Wen,andN.Yu. Maskclip: Maskedself-distillationadvancescontrastivelanguageimagepretraining. 2023IEEE/CVFConferenceonComputerVisionandPatternRecognition
(CVPR),pages10995–11005,2022.URLhttps://api.semanticscholar.org/CorpusID:
251799827.
[9] G.Ghiasi,X.Gu,Y.Cui,andT.-Y.Lin. Scalingopen-vocabularyimagesegmentationwith
image-levellabels. InEuropeanConferenceonComputerVision,2021. URLhttps://api.
semanticscholar.org/CorpusID:250895808.
11

<!-- Page 12 -->

[10] B.Li,K.Q.Weinberger,S.J.Belongie,V.Koltun,andR.Ranftl. Language-drivensemantic
segmentation. ArXiv,abs/2201.03546,2022. URLhttps://api.semanticscholar.org/
CorpusID:245836975.
[11] M. Oquab, T. Darcet, T. Moutakanni, H. Q. Vo, M. Szafraniec, V. Khalidov, P. Fernandez,
D. Haziza, F. Massa, A. El-Nouby, M. Assran, N. Ballas, W. Galuba, R. Howes, P.-Y. B.
Huang,S.-W.Li,I.Misra,M.G.Rabbat,V.Sharma,G.Synnaeve,H.Xu,H.Jégou,J.Mairal,
P. Labatut, A. Joulin, and P. Bojanowski. Dinov2: Learning robust visual features without
supervision. ArXiv, abs/2304.07193, 2023. URL https://api.semanticscholar.org/
CorpusID:258170077.
[12] S. Peng, K. Genova, ChiyuMaxJiang, A. Tagliasacchi, M. Pollefeys, and T.A. Funkhouser.
Openscene: 3d scene understanding with open vocabularies. 2023 IEEE/CVF Conference
on Computer Vision and Pattern Recognition (CVPR), pages 815–824, 2022. URL https:
//api.semanticscholar.org/CorpusID:254044069.
[13] J.Kerr,C.M.Kim,K.Goldberg,A.Kanazawa,andM.Tancik. Lerf: Languageembedded
radiancefields. 2023IEEE/CVFInternationalConferenceonComputerVision(ICCV),pages
19672–19682,2023. URLhttps://api.semanticscholar.org/CorpusID:257557329.
[14] P.D.Nguyen,T.Ngo,C.Gan,E.Kalogerakis,A.D.Tran,C.Pham,andK.Nguyen. Open3dis:
Open-vocabulary3dinstancesegmentationwith2dmaskguidance. ArXiv,abs/2312.10671,

## URLhttps://api.semanticscholar.org/CorpusID:266348609.

[15] S. Koch, N. Vaskevicius, M. Colosi, P. Hermosilla, and T. Ropinski. Open3dsg: Openvocabulary3dscenegraphsfrompointcloudswithqueryableobjectsandopen-setrelationships.
ArXiv, abs/2402.12259, 2024. URL https://api.semanticscholar.org/CorpusID:
267750890.
[16] B.W.Shen,G.Yang,A.Yu,J.R.Wong,L.P.Kaelbling,andP.Isola. Distilledfeaturefields
enablefew-shotlanguage-guidedmanipulation. InConferenceonRobotLearning,2023. URL
https://api.semanticscholar.org/CorpusID:260926035.
[17] V.Tschernezki,I.Laina,D.Larlus,andA.Vedaldi. Neuralfeaturefusionfields: 3ddistillation
ofself-supervised2dimagerepresentations.2022InternationalConferenceon3DVision(3DV),
pages443–453,2022. URLhttps://api.semanticscholar.org/CorpusID:252118532.
[18] S. Kobayashi, E. Matsumoto, and V. Sitzmann. Decomposing nerf for editing via feature
fielddistillation. ArXiv,abs/2205.15585,2022. URLhttps://api.semanticscholar.org/
CorpusID:249209811.
[19] F.Engelmann,F.Manhardt,M.Niemeyer,K.Tateno,M.Pollefeys,andF.Tombari. Opennerf:
Openset3dneuralscenesegmentationwithpixel-wisefeaturesandrenderednovelviews,2024.
[20] A.Rashid,S.Sharma,C.M.Kim,J.Kerr,L.Y.Chen,A.Kanazawa,andK.Goldberg.Language
embeddedradiancefieldsforzero-shottask-orientedgrasping.InConferenceonRobotLearning,

## URLhttps://api.semanticscholar.org/CorpusID:261882332.

[21] J.Zhang,R.Dong,andK.Ma. Clip-fo3d: Learningfreeopen-world3dscenerepresentations
from2ddenseclip. 2023IEEE/CVFInternationalConferenceonComputerVisionWorkshops
(ICCVW),pages2040–2051,2023. URLhttps://api.semanticscholar.org/CorpusID:
257404908.
[22] A.Dai,A.X.Chang,M.Savva,M.Halber,T.Funkhouser,andM.Nießner. Scannet: Richlyannotated 3d reconstructions of indoor scenes. In Proceedings of the IEEE Conference on
ComputerVisionandPatternRecognition,pages5828–5839,2017.
12

<!-- Page 13 -->

[23] S.K.Ramakrishnan, A.Gokaslan, E.Wijmans, O.Maksymets, A.Clegg, J.Turner, E.Undersander, W. Galuba, A. Westbury, A. X. Chang, M. Savva, Y. Zhao, and D. Batra.
Habitat-matterport 3d dataset (hm3d): 1000 large-scale 3d environments for embodied ai.
ArXiv, abs/2109.08238, 2021. URL https://api.semanticscholar.org/CorpusID:
237563216.
[24] M.Qin,W.Li,J.Zhou,H.Wang,andH.Pfister. Langsplat: 3dlanguagegaussiansplatting,
2024.
[25] M.Chen,Q.Hu,Z.Yu,H.Thomas,A.Feng,Y.Hou,K.McCullough,F.Ren,andL.Soibelman.
Stpls3d: Alarge-scalesyntheticandrealaerialphotogrammetry3dpointclouddataset. arXiv
preprintarXiv:2203.09065,2022.
[26] J.Straub,T.Whelan,L.Ma,Y.Chen,E.Wijmans,S.Green,J.J.Engel,R.Mur-Artal,C.Ren,
S. Verma, et al. The replica dataset: A digital replica of indoor spaces. arXiv preprint
arXiv:1906.05797,2019.
[27] H.Liu,A.Lin,X.Han,L.Yang,Y.Yu,andS.Cui. Refer-it-in-rgbd: Abottom-upapproach
for3dvisualgroundinginrgbdimages. 2021IEEE/CVFConferenceonComputerVisionand
PatternRecognition(CVPR),pages6028–6037,2021.
[28] C.Mauceri,M.Palmer,andC.Heckman. Sun-spot: Anrgb-ddatasetwithspatialreferring
expressions.2019IEEE/CVFInternationalConferenceonComputerVisionWorkshop(ICCVW),
pages1883–1886,2019.
[29] H.-S. Fang, C. Wang, M. Gou, and C. Lu. Graspnet-1billion: A large-scale benchmark for
generalobjectgrasping. InProceedingsoftheIEEE/CVFconferenceoncomputervisionand
patternrecognition,pages11444–11453,2020.
[30] H.Zhang,D.Yang,H.Wang,B.Zhao,X.Lan,J.Ding,andN.Zheng. Regrad: Alarge-scale
relationalgraspdatasetforsafeandobject-specificroboticgraspinginclutter. IEEERobotics
andAutomationLetters,7(2):2929–2936,2022.
[31] G.Tziafas,X.Yucheng,A.Goel,M.Kasaei,Z.Li,andH.Kasaei. Language-guidedrobot
grasping: Clip-basedreferringgraspsynthesisinclutter. In7thAnnualConferenceonRobot
Learning,2023.
[32] A.D.Vuong,M.N.Vu,H.Le,B.Huang,B.P.K.Huynh,T.D.Vo,A.Kugi,andA.Nguyen.
Grasp-anything: Large-scalegraspdatasetfromfoundationmodels. ArXiv,abs/2309.09818,

## URLhttps://api.semanticscholar.org/CorpusID:262045996.

[33] I.Armeni,O.Sener,A.R.Zamir,H.Jiang,I.Brilakis,M.Fischer,andS.Savarese. 3dsemantic
parsingoflarge-scaleindoorspaces. InProceedingsoftheIEEEconferenceoncomputervision
andpatternrecognition,pages1534–1543,2016.
[34] D.Rozenberszki,O.Litany,andA.Dai. Language-groundedindoor3dsemanticsegmentation
inthewild. InEuropeanConferenceonComputerVision,pages125–141.Springer,2022.
[35] C. Eppner, A. Mousavian, and D. Fox. ACRONYM: A large-scale grasp dataset based on
simulation. In2021IEEEInt.Conf.onRoboticsandAutomation,ICRA,2020.
[36] B. O. Community. Blender - a 3d modelling and rendering package. 2018. URL http:
//www.blender.org.
[37] A.X.Chang,T.Funkhouser,L.Guibas,P.Hanrahan,Q.Huang,Z.Li,S.Savarese,M.Savva,
S.Song,H.Su,J.Xiao,L.Yi,andF.Yu. ShapeNet:AnInformation-Rich3DModelRepository.
TechnicalReportarXiv:1512.03012[cs.GR],StanfordUniversity—PrincetonUniversity—
ToyotaTechnologicalInstituteatChicago,2015.
13

<!-- Page 14 -->

[38] Gpt-4v(ision)systemcard. 2023. URLhttps://api.semanticscholar.org/CorpusID:
263218031.
[39] C.Wu,Y.Liu,J.Ji,Y.Ma,H.Wang,G.Luo,H.Ding,X.Sun,andR.Ji. 3d-gres: Generalized
3d referring expression segmentation. ArXiv, abs/2407.20664, 2024. URL https://api.
semanticscholar.org/CorpusID:271544474.
[40] T.Ren,S.Liu,A.Zeng,J.Lin,K.Li,H.Cao,J.Chen,X.Huang,Y.Chen,F.Yan,Z.Zeng,
H.Zhang,F.Li,J.Yang,H.Li,Q.Jiang,andL.Zhang. Groundedsam:Assemblingopen-world
modelsfordiversevisualtasks,2024.
[41] B.Zhou, H.Zhao, X.Puig, S.Fidler, A.Barriuso, andA.Torralba. Sceneparsingthrough
ade20kdataset. 2017IEEEConferenceonComputerVisionandPatternRecognition(CVPR),
pages5122–5130,2017. URLhttps://api.semanticscholar.org/CorpusID:5636055.
[42] J. Schult, F. Engelmann, A. Hermans, O. Litany, S. Tang, and B. Leibe. Mask3D: Mask
Transformerfor3DSemanticInstanceSegmentation. 2023.
[43] A. Kirillov, E. Mintun, N. Ravi, H. Mao, C. Rolland, L. Gustafson, T. Xiao, S. Whitehead,
A. C. Berg, W.-Y. Lo, P. Dollár, and R. B. Girshick. Segment anything. 2023 IEEE/CVF
InternationalConferenceonComputerVision(ICCV),pages3992–4003,2023. URLhttps:
//api.semanticscholar.org/CorpusID:257952310.
[44] S.Chen,W.N.Tang,P.Xie,W.Yang,andG.Wang. Efficientheatmap-guided6-dofgrasp
detectioninclutteredscenes. IEEERoboticsandAutomationLetters,8:4895–4902,2023. URL
https://api.semanticscholar.org/CorpusID:259363869.
[45] N.P.KoenigandA.Howard. Designanduseparadigmsforgazebo,anopen-sourcemulti-robot
simulator. 2004IEEE/RSJInternationalConferenceonIntelligentRobotsandSystems(IROS)
(IEEECat.No.04CH37566),3:2149–2154vol.3,2004.
[46] C.B.Choy,J.Gwak,andS.Savarese. 4dspatio-temporalconvnets: Minkowskiconvolutional
neuralnetworks. 2019IEEE/CVFConferenceonComputerVisionandPatternRecognition
(CVPR),pages3070–3079,2019. URLhttps://api.semanticscholar.org/CorpusID:
121123422.
[47] L.Han,T.Zheng,L.Xu,andL.Fang. Occuseg: Occupancy-aware3dinstancesegmentation.
2020 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), pages
2937–2946,2020. URLhttps://api.semanticscholar.org/CorpusID:212725768.
[48] W.Hu,H.Zhao,L.Jiang,J.Jia,andT.-T.Wong. Bidirectionalprojectionnetworkforcross
dimensionsceneunderstanding. 2021IEEE/CVFConferenceonComputerVisionandPattern
Recognition (CVPR), pages 14368–14377, 2021. URL https://api.semanticscholar.
org/CorpusID:232379958.
[49] Z. Hu, X. Bai, J. Shang, R. Zhang, J. Dong, X. Wang, G. Sun, H. Fu, and C.-L. Tai. Vmnet: Voxel-mesh network for geodesic-aware 3d semantic segmentation. 2021 IEEE/CVF
International Conference on Computer Vision (ICCV), pages 15468–15478, 2021. URL
https://api.semanticscholar.org/CorpusID:236493200.
[50] J.Li,X.He,Y.Wen,Y.Gao,X.Cheng,andD.Zhang. Panoptic-phnet: Towardsreal-timeand
high-precisionlidarpanopticsegmentationviaclusteringpseudoheatmap. 2022IEEE/CVF
ConferenceonComputerVisionandPatternRecognition(CVPR),pages11799–11808,2022.
URLhttps://api.semanticscholar.org/CorpusID:248811224.
[51] D.Robert,B.Vallet,andL.Landrieu. Learningmulti-viewaggregationinthewildforlargescale3dsemanticsegmentation. 2022IEEE/CVFConferenceonComputerVisionandPattern
Recognition(CVPR),pages5565–5574,2022. URLhttps://api.semanticscholar.org/
CorpusID:248218804.
14

<!-- Page 15 -->

[52] Z. Wu, S. Song, A. Khosla, F. Yu, L. Zhang, X. Tang, and J. Xiao. 3d shapenets: A deep
representationforvolumetricshapes. 2015IEEEConferenceonComputerVisionandPattern
Recognition(CVPR),pages1912–1920,2014. URLhttps://api.semanticscholar.org/
CorpusID:206592833.
[53] R.Zhang,Z.Guo,W.Zhang,K.Li,X.Miao,B.Cui,Y.J.Qiao,P.Gao,andH.Li. Pointclip:
Pointcloudunderstandingbyclip.2022IEEE/CVFConferenceonComputerVisionandPattern
Recognition(CVPR),pages8542–8552,2021. URLhttps://api.semanticscholar.org/
CorpusID:244909021.
[54] H.Caesar,V.Bankiti,A.H.Lang,S.Vora,V.E.Liong,Q.Xu,A.Krishnan,Y.Pan,G.Baldan,
andO.Beijbom. nuscenes: Amultimodaldatasetforautonomousdriving. 2020IEEE/CVF
ConferenceonComputerVisionandPatternRecognition(CVPR),pages11618–11628,2019.
URLhttps://api.semanticscholar.org/CorpusID:85517967.
[55] J. Behley, M. Garbade, A. Milioto, J. Quenzel, S. Behnke, C. Stachniss, and J. Gall. Semantickitti: Adatasetforsemanticsceneunderstandingoflidarsequences. 2019IEEE/CVF
International Conference on Computer Vision (ICCV), pages 9296–9306, 2019. URL
https://api.semanticscholar.org/CorpusID:199441943.
[56] P. Achlioptas, A. Abdelreheem, F. Xia, M. Elhoseiny, and L. J. Guibas. Referit3d: Neural
listenersforfine-grained3dobjectidentificationinreal-worldscenes. InEuropeanConference
onComputerVision,2020.
[57] L. Zhao, D. Cai, L. Sheng, and D. Xu. 3dvg-transformer: Relation modeling for visual
groundingonpointclouds. 2021IEEE/CVFInternationalConferenceonComputerVision
(ICCV),pages2908–2917,2021.
[58] S. Huang, Y. Chen, J. Jia, and L. Wang. Multi-view transformer for 3d visual grounding.
2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), pages
15503–15512,2022.
[59] D.Rozenberszki,O.Litany,andA.Dai. Language-groundedindoor3dsemanticsegmentation
in the wild. ArXiv, abs/2204.07761, 2022. URL https://api.semanticscholar.org/
CorpusID:248227627.
[60] X.Gu,T.-Y.Lin,W.Kuo,andY.Cui. Open-vocabularyobjectdetectionviavisionandlanguage
knowledgedistillation. InInternationalConferenceonLearningRepresentations,2021. URL
https://api.semanticscholar.org/CorpusID:238744187.
[61] Y. Zhong, J. Yang, P. Zhang, C. Li, N. C. F. Codella, L. H. Li, L. Zhou, X. Dai, L. Yuan,
Y.Li, andJ.Gao. Regionclip: Region-basedlanguage-imagepretraining. 2022IEEE/CVF
ConferenceonComputerVisionandPatternRecognition(CVPR),pages16772–16782,2021.
URLhttps://api.semanticscholar.org/CorpusID:245218534.
[62] M. Minderer, A. A. Gritsenko, A. Stone, M. Neumann, D. Weissenborn, A. Dosovitskiy,
A.Mahendran,A.Arnab,M.Dehghani,Z.Shen,X.Wang,X.Zhai,T.Kipf,andN.Houlsby.
Simple open-vocabulary object detection with vision transformers. ArXiv, abs/2205.06230,

## URLhttps://api.semanticscholar.org/CorpusID:248721818.

[63] X. Zhou, R. Girdhar, A. Joulin, P. Krahenbuhl, and I. Misra. Detecting twenty-thousand
classes using image-level supervision. ArXiv, abs/2201.02605, 2022. URL https://api.
semanticscholar.org/CorpusID:245827815.
[64] M. Minderer, A. A. Gritsenko, and N. Houlsby. Scaling open-vocabulary object detection. ArXiv,abs/2306.09683,2023. URLhttps://api.semanticscholar.org/CorpusID:
259187664.
15

<!-- Page 16 -->

[65] Z. Wang, Y. Lu, Q. Li, X. Tao, Y. Guo, M. Gong, and T. Liu. Cris: Clip-driven referring
imagesegmentation. 2022IEEE/CVFConferenceonComputerVisionandPatternRecognition
(CVPR),pages11676–11685,2021.URLhttps://api.semanticscholar.org/CorpusID:
244729320.
[66] T. Lüddecke and A. S. Ecker. Image segmentation using text and image prompts. 2022
IEEE/CVFConferenceonComputerVisionandPatternRecognition(CVPR),pages7076–7086,

## URLhttps://api.semanticscholar.org/CorpusID:247794227.

[67] N. M. M. Shafiullah, C. Paxton, L. Pinto, S. Chintala, and A. Szlam. Clip-fields: Weakly
supervisedsemanticfieldsforroboticmemory. ArXiv,abs/2210.05663,2022. URLhttps:
//api.semanticscholar.org/CorpusID:252815898.
[68] B.Bolte,A.S.Wang,J.Yang,M.Mukadam,M.Kalakrishnan,andC.Paxton. Usa-net: Unified
semantic and affordance representations for robot memory. 2023 IEEE/RSJ International
ConferenceonIntelligentRobotsandSystems(IROS),pages1–8,2023. URLhttps://api.
semanticscholar.org/CorpusID:258298248.
[69] T.-Y.Lin,M.Maire,S.Belongie,J.Hays,P.Perona,D.Ramanan,P.Dollár,andC.L.Zitnick.
Microsoftcoco: Commonobjectsincontext. InComputerVision–ECCV2014: 13thEuropean
Conference,Zurich,Switzerland,September6-12,2014,Proceedings,PartV13,pages740–755.
Springer,2014.
[70] P. Khosla, P. Teterwak, C. Wang, A. Sarna, Y. Tian, P. Isola, A. Maschinot, C. Liu, and
D.Krishnan. Supervisedcontrastivelearning. CoRR,abs/2004.11362, 2020. URLhttps:
//arxiv.org/abs/2004.11362.
[71] H. Oki, M. Abe, J. Miyao, and T. Kurita. Triplet loss for knowledge distillation. 2020
InternationalJointConferenceonNeuralNetworks(IJCNN),pages1–7,2020. URLhttps:
//api.semanticscholar.org/CorpusID:215814195.
[72] L. Yang, Y. Wang, X. Li, X. Wang, and J. Yang. Fine-grained visual prompting.
ArXiv, abs/2306.04356, 2023. URL https://api.semanticscholar.org/CorpusID:
259096008.
[73] A.Shtedritski,C.Rupprecht,andA.Vedaldi. Whatdoesclipknowaboutaredcircle? visual
promptengineeringforvlms. 2023IEEE/CVFInternationalConferenceonComputerVision
(ICCV),pages11953–11963,2023. URLhttps://api.semanticscholar.org/CorpusID:
258108138.
[74] S. Ainetter and F. Fraundorfer. End-to-end trainable deep neural network for robotic grasp
detectionandsemanticsegmentationfromrgb. InIEEEInternationalConferenceonRobotics
andAutomation(ICRA),pages13452–13458,2021.
[75] J. Guo, X. Ma, Y. Fan, H. Liu, and Q. Li. Semantic gaussians: Open-vocabulary scene
understandingwith3dgaussiansplatting. ArXiv,abs/2403.15624,2024. URLhttps://api.
semanticscholar.org/CorpusID:268680548.
[76] R.-Z. Qiu, G. Yang, W. Zeng, and X. Wang. Feature splatting: Language-driven physicsbased scene synthesis and editing. ArXiv, abs/2404.01223, 2024. URL https://api.
semanticscholar.org/CorpusID:268819312.
[77] S.Zhou,H.Chang,S.Jiang,Z.Fan,Z.Zhu,D.Xu,P.Chari,S.You,Z.Wang,andA.Kadambi.
Feature 3dgs: Supercharging 3d gaussian splatting to enable distilled feature fields. 2024
IEEE/CVFConferenceonComputerVisionandPatternRecognition(CVPR),pages21676–
21685,2023. URLhttps://api.semanticscholar.org/CorpusID:265722936.
16

<!-- Page 17 -->

[78] R.Ding,J.Yang,C.Xue,W.Zhang,S.Bai,andX.Qi.Pla:Language-drivenopen-vocabulary3d
sceneunderstanding. 2023IEEE/CVFConferenceonComputerVisionandPatternRecognition
(CVPR),pages7010–7019,2022. URLhttps://api.semanticscholar.org/CorpusID:
254069374.
[79] J. Yang, R. Ding, Z. Wang, and X. Qi. Regionplc: Regional point-language contrastive
learningforopen-world3dsceneunderstanding. ArXiv,abs/2304.00962,2023. URLhttps:
//api.semanticscholar.org/CorpusID:257913360.
[80] R.Ding,J.Yang,C.Xue,W.Zhang,S.Bai,andX.Qi. Lowis3d: Language-drivenopen-world
instance-level3dsceneunderstanding. IEEEtransactionsonpatternanalysisandmachine
intelligence,PP,2023. URLhttps://api.semanticscholar.org/CorpusID:260351247.
[81] D.Hegde,J.M.J.Valanarasu,andV.M.Patel. Clipgoes3d: Leveragingprompttuningfor
languagegrounded3drecognition. 2023IEEE/CVFInternationalConferenceonComputer
VisionWorkshops(ICCVW),pages2020–2030,2023.URLhttps://api.semanticscholar.
org/CorpusID:257632366.
[82] Z.Huang,X.Wu,X.Chen,H.Zhao,L.Zhu,andJ.Lasenby. Openins3d: Snapandlookup
for3dopen-vocabularyinstancesegmentation. ArXiv,abs/2309.00616,2023. URLhttps:
//api.semanticscholar.org/CorpusID:261494064.
[83] S. Lu, H. Chang, E. P. Jing, A. Boularias, and K. E. Bekris. Ovir-3d: Open-vocabulary 3d
instance retrieval without training on 3d data. ArXiv, abs/2311.02873, 2023. URL https:
//api.semanticscholar.org/CorpusID:262072783.
[84] Y. nuo Yang, X. Wu, T. He, H. Zhao, and X. Liu. Sam3d: Segment anything in 3d scenes.
ArXiv, abs/2306.03908, 2023. URL https://api.semanticscholar.org/CorpusID:
259088699.
[85] M.Yan,J.Zhang,Y.Zhu,andH.R.Wang. Maskclustering: Viewconsensusbasedmaskgraph
clusteringforopen-vocabulary3dinstancesegmentation. ArXiv,abs/2401.07745,2024. URL
https://api.semanticscholar.org/CorpusID:266999755.
[86] Y.Yin,Y.Liu,Y.Xiao,D.Cohen-Or,J.Huang,andB.Chen. Sai3d: Segmentanyinstance
in3dscenes. ArXiv,abs/2312.11557,2023. URLhttps://api.semanticscholar.org/
CorpusID:266362709.
[87] W. Dai, J. Li, D. Li, A. M. H. Tiong, J. Zhao, W. Wang, B. A. Li, P. Fung, and S. C. H.
Hoi. Instructblip: Towards general-purpose vision-language models with instruction tuning. ArXiv,abs/2305.06500,2023. URLhttps://api.semanticscholar.org/CorpusID:
258615266.
[88] B.Kerbl,G.Kopanas,T.Leimkuehler,andG.Drettakis. 3dgaussiansplattingforreal-time
radiance field rendering. ACM Transactions on Graphics (TOG), 42:1 – 14, 2023. URL
https://api.semanticscholar.org/CorpusID:259267917.
17

<!-- Page 18 -->


### A Appendix


### A.1 MV-TODDetails

InthissectionweprovidedetailsforgeneratingourMV-TODscenesandtheirannotations(Sec.A.1.1)
andpresentsomestatisticsfortheobjectandquerycatalogofMV-TOD(Sec.A.1.2).

### A.1.1 DatasetGeneration

Figure9:AwordcloudandT-SNEembeddingprojectionvisualizationoftextualconceptsincludedinMV-TOD.
WegeneratetheMV-TODdatasetinBlender[36]enginewithfollowingsteps:
RandomobjectspawnForeachscene, firstly, asupportplaneisspawnedattheoriginposition.
Then,randomobjectsareselectedtosetupthemulti-objecttabletopscene. Thenumberofobjects
rangesfrom4to12, tomakesurethatourdatasetcoversbothisolatedandclutteredscenes. All
selectedobjectsarethenspawnedabovethesupportplanewithrandompositionandrandomrotation.
ItisimportanttonotethatduetothelimitationofBlenderphysicalengine,anadditionalcollision
checkisneededwhenanobjectisspawnedintothescenetoavoidinitialcollision. SinceBlender
doesnotprovideuserswiththeAPIstodothecollisioncheck,wecheckthecollisionbycalculating
the3DIoUbetweenobjectboundingboxes. Afterspawningobject,theinternalphysicalsimulatoris
launchedtosimulationthefallingofallthespawnedobjectontotheplane. Oncetheobjectsarestill,
theenginewillstartrenderingimages.
Multi-viewrenderingIntotal73camerasaresetineachsceneforrendingimagesfromdifferent
views. Oneofthemarespawnedrightontopoftheoriginpositionforrenderingatop-downimage,
whiletherestareuniformlydistributedonthesurfaceofthetophemisphere. AnRGBimage,adepth
image(withtherawdepthinformationinmeters),andaninstancesegmentationmaskarerenderedat
eachview. AlltheannotationsaresavedintheCOCO [69]JSONformatforeachscene.
Data augmentation In order to diversify the generated data, several augmentation methods are
applied. Firstly,differenttexturesandmaterialsarerandomlyappliedtothesupportplane,aswellas
thescenebackground,tosimulatedifferenttypesoftablesurfacesandbackgroundenvironments.
Second,whentheobjectsarespawned,theirsizesandmaterialsarerandomlyjittered. Thirdly,we
also randomly slighlty modify the position of cameras towards the radial direction. Finally, the
positionandintensityofthelightobjectineachscenearealsorandomlyset.
SemanticobjectannotationgenerationToofferthefunctionalityofqueryingtargetobjectsinour
datasetbyusinghigh-levelconceptsanddistinguishsimilarobjectsusingfine-grainedattributes,we
alsoprovideper-objectsemanticconceptsgeneratedwiththeaidoflargevision-languagemodels.
ForeachobjectCADmodel,werender10observationimagesfromdifferentviewsinBlender. Then,
theseimages,togetherwithaninstructionpromptarefedtoGPT-4V[38]togeneratearesponse
18

<!-- Page 19 -->

Please provide a set of text descriptions for the object shown in the input images. The input images are multiview observation of the object. The descriptions should describe
the object color, material, stateF (ei.gg. uif Ir geive1 y0ou: thNe imuagme obf ae browol, fyoou sbhojueldc tetlsl if ithne beowal cemhptyc oar tfuell)g, aos rwyell aisn utiMlity (Ve.g-. Tif I OgivDe yo.u the image of a hammer, you
should say: "Something to do general carpentry, framing, nail pulling, cabinet making, assembling furniture, upholstering, finishing, riveting, bending or shaping metal, striking
masonry drills and steel chisels, and so on"). Finally, provide a list of specific object descriptions that would be commonly used to refer to that object (e.g. If I give you an
image of a coca-cola can, you could return: "[Coke, Coke-can, Coca-Cola, Cola, Cola-can, Cola-drink, ...]". If the object is a product, please try to identify and give its brand
(e.g. "Coca-cola, "Fanta" etc.). Also provide a few `affordance` descriptions, which is what a user would say if they desired that object (e.g. If I give you an image of an apple,
say: "I'm hungry", "I want to eat something healthy", etc.). Please reply with the following format:

## Response_Format:

---
Category: [give object category]

### Color: [give object color]

Material: [give object material]

### State: [give object state]


### Brand: [optional - give product brand]

Title: [optional - give the title for object ONLY]

### Utility: [give object utility]


### Affordance: [give user instructions]

More descriptions: [give a list of specific object descriptions]
---
Please in your descriptions avoid words like "Appears to be [...]", "Appears [...]", "The object is [...]" etc., just give the noun/adjective descriptions.

### Provide descriptions for the following {label} object

Figure11: ThetextpromptweusedforinstructingGPT-4V.The{label}tokenwillbereplacedbytheclass
nameofthecurrentobject.
describingthecurrentobjectindifferentperspectives,includingcategory,color,material,state,utility,
affordance,title(ifapplicable),andbrand(ifapplicable).ThetextpromptweusedtoinstructGPT-4V
ispresentedinFigure11.
6-DoFgraspannotationsSinceourmodelsetoriginatesfromShapeNet-Sem[37], weleverage
theobject-wise6-DoFgraspproposalsgeneratedpreviouslyintheACRONYMdataset[35]. These
graspswereexecutedandevaluatedinasimulationenvironment,leadingtoatotalof2000grasp
candidatesperobject. Wefilterthesucessfullgraspsandconnectthemwitheachobjectinstancein
eachofourscenes,bytransformingthegraspannotationaccordingtotherecordedobject’s6Dpose
fromBlender. Wefurtherfiltergraspsbyrenderingagrippermeshandremovingallgraspposesthat
leadtocollisionswiththetableorotherobjects.

### A.1.2 DatasetAnalysis

WevisualizeawordcloudoftheconceptvocabularyofMV-TOD,togetherwithtSNEprojectionsof
theirCLIPtextembeddingsinFigure.9. Certainobjectnames(e.g."plant","computer","phone",
"vase")appearmorefrequently,asthosearetheobjectsthataremostfrequentinMV-TODobject
catalog, hence they spawn a lot of expressions referring to them. Besides common class names,
the wordcloud demonstrates that the most frequent concepts used to disambiguate objects are
19

<!-- Page 20 -->


### Type Train Test


### Class 66.8k 19.2k


### Class+Attr 76.5k 21.8k

Affordance 151.1k 44.7k

### Open 356.8k 102.1k


### Table6: NumberofreferringexpressionsinMV-TODorganizedbytype

supplementaryattributes(e.g.decorative,potted,portable,etc). Finally,colorsandmaterialsappear
alsofrequently,astheyareacommondiscriminatingattributebetweenobjectsofthesamecategory.
WefurtherprovidestatisticalanalysisofMV-TODinTable6andFigure10. Thenumberofreferring
expressionscategorizedbytheirtypesarelistedinTable6. Weproviderichopenexpressions,which
stemsfromopenvocabularyconceptsthatcandescribethereferredobjectsinvariousaspects. As
itcanbeseenFigure10,thereexistsatypicallong-taildistributioninourdatasetintermsofthe
numberofobjectsper-category,wherelaptop,phone,andplanthavethemostvariantinstances.
A.2 DistillationImplementationDetails
WeusetheViT-L/14@336pxvariantofCLIP’s

### Hyper-parameter Value

visionencoder,whichprovidesfeaturesofsize
voxel_size 0.05
C = 768 from 336×448 image inputs with feat_dim 768
color_trans_ratio 0.01
patch size 14. We distill with a Minkowsk- color_jitter_std 0.02
hue_max 0.01
iNet14D[46]sparse3D-UNetbackbone,which saturation_max 0.1
elastic_distortion_granularity_min 0.1
consistsof8sparseResNetblockswithoutput elastic_distortion_granularity_max 0.3
elastic_distortion_magnitude_min 0.4
sizes of (32,64,128,256,384,384,384,384) elastic_distortion_magnitude_max 0.8
n_blob_min 1
andafinal1×1convolutionheadto768chan- n_blob_max 2
blob_size_min 50
nels. Toincreasethe3Dcoordinatesresolution, blob_size_max 101
random_euler_order True
we upscale the input point-clouds to ×10 and random_rot_chance 0.6
rotate_min_x -0.1309
voxelize with original dimension of d = 0.02 rotate_max_x 0.1309
(forfeaturefusion),andavoxelgridd = 0.05 rotate_min_y -0.1309
rotate_max_y 0.1309
fortrainingwiththeMinkowskiframework. To rotate_min_z -0.1309
rotate_max_z 0.1309
reduce the input dimensionality and speedup arch_3d MinkUNet14D
batch_size 8
trainingandinferencetime,weremovethetable batch_size_val 8
base_lr 0.0003
points via filtering out the table’s 3D mask. 1 weight_decay 0.00001
min_lr 0.0001
WetrainusingAdamWwithinitiallearningrate loss_type cosine
use_aux_loss False
3·10−4andcosineannealingto10−4over300 use_cls_head False
loss_weight_aux 1.0
epochs, and a weight decay of 10−4. In each loss_weight_cls 0.1
dropout_rate 0.0
ResNetblock,weincludesparsebatchnormal- epochs 300
power 0.9
izationlayerswithmomentumof0.1. Wetrain momentum 0.9
max_norm 5.0
usingtwoRTX4090GPUs,whichtakesabout sync_bn True
4days. Following [12,6]weusespatialaug- Table7: Traininghyper-parameters
mentationssuchaselasticdistortion,horizontal
flippingandsmallrandomtranslationsandrotations. We also employ color-based augmentationsuchaschromaticauto-contrast,random
colortranslation,jitterandhuesaturationtranslation. Tobetteremulatepartialviewswithgreater
diversity, wetrainwithfullpoint-cloudsbutfurtheraddaper-objectblobremovalaugmentation
methodthatremovesconsistentblobsofpointsfromeachobjectinstance. Aftertrainingfor300
epochs,wefine-tuneourobtainedcheckpointononlypartialpoint-cloudsfromrandomlysampled
views for each scene in our dataset. We experimented with several auxiliary losses to reinforce
within-objectfeaturesimilarity,suchassupervisedcontrastiveloss[70]aswellasKLtripletloss[71],

### Duringinference,weemployRANSACtoremovetablepointswithoutaccesstosegmentationmasks.

20

<!-- Page 21 -->

butfoundthattheydonotsignificantlycontributetoconvergencecomparedtousingonlythemain
cosinedistanceloss. SeeTable7forafulloverviewoftrainingandaugmentationhyper-parameters.

### A.3 ExtendedMulti-ViewFeatureFusionAblations

Ourobject-centricfusionpipelineconsidersseveraldesignchoicesbesidestheonesdiscussedinthe
mainpaper. Inparticular,westudy: (i)Whymaskedcropsasinputtoobject-level2DCLIPfeature
computation? HowdoesitcomparewithotherpopularvisualpromptstoCLIP?,(ii)Whyequations
(3)and(4)inthesemanticinformativenessmetriccomputation? Howtosamplenegatives?,and(iii)
Whatisthebeststrategyandhyper-parametersfordoinginference?

### CLIPvisualpromptsPreviousworkshave

crop crop-mask mask-blur mask-gray mask-out #crops crop-ratio mIoU(%)
extensively studied how to prompt CLIP to (cid:37) 1 - 81.9
(cid:37) 3 0.1 81.0
make it focus in a particular entity in the (cid:37) 3 0.15 80.6
(cid:37) 3 0.2 80.3
scene [72, 73]. We study the potential of (cid:37) 1 - 84.0
visual prompting for obtaining object-level (cid:37) (cid:37) 3 3 0 0 .1 .2 5 8 8 2 2 . . 4 0
CLIP features in our object-centric feature (cid:37) (cid:37) 1 - 81.7
(cid:37) - - 74.6
fusionpipeline,viameasuringtheirfinalre- (cid:37) - - 57.4
(cid:37) - - 79.7
ferring segmentation mIoU in a subset of (cid:37) (cid:37) (cid:37) - - 70.2
MV-TOD validation split. We compile the Table8: CLIPvisualpromptablationstudies.
following visual prompt options: (a) crop,
wherewecropaboundingboxaroundeach
object [13, 6], (b) crop-mask, where we crop a bounding box but only leave the pixels of the
object’s2Dinstancemaskinsideanduniformypaintthebackground(black,whiteorgray,based
onthemask’smeancolor),(c)mask-{blur,gray,out},whereweusetheentireimagewiththe
targetobjectinstancehighlighted[72]andtherestcompletelyremovedasbefore(out),converted
tograyscale(gray)orappliedamedianblurfilter(blur). Forthecropoptions, wefurtherablate
the numberof multi-scalecrops usedand their relative expansion ratio. Results aresummarized
inTable8. Weobservethefollowing: (a)image-levelvisualpromptsusedpreviously[72]donot
performaswellascroppedboundingboxes,(b)usingmulti-scalecrops [13,6]doesn’timprove
overusingasingleobjectcrop,(c)maskedcropsoutperformnon-maskedcropsbyasmallmargin
of2.1%. Thedifferenceisduetocasesofheavyclutter,whentheboundingboxofthenon-masked
cropalsoincludesneighboringobjects,makingtherepresentationobtainedbyCLIPalsogivehigh
similaritieswiththeneighbor’sprompt. Thiseffectismorepronouncedwhenusingmultiplecrops
withlargerexpansionratios,asmoreandmoreneighboringobjectsareincludedinthecrops.
SemanticinformativenessmetricWeablate

### Ref.Segm.(%) Sem.Segm(%)

thefollowingcomponentswhencomputing Prompts Operator Negatives
mIoU Pr@25 mIoU mAcc
semanticinformativenessmetricG : (i)the
v,n cls mean scene 82.2 83.1 73.1 75.1
type of prompts used as q+,Q−, i.e. cls cls max scene 82.8 84.0 74.9 76.7
cls mean all 80.9 81.0 71.6 73.9
forcategory-levelpromptsandopenwhere cls max all 72.6 75.1 60.7 63.2
open mean scene 76.4 78.8 68.3 70.3
we use all instance-level descriptions annoopen max scene 83.9 85.5 75.6 77.2
tatedwithGPT-4V,(ii)theoperatorusedto open mean all 81.0 81.8 71.6 74.0
open max all 72.9 74.2 63.8 64.6
reducethenegativepromptstosinglefeature
Table9: Semanticinformativenessmetricablationstudies.
dimension,i.e.maxandmean,and(iii)howto
ResultsinMV-TODvalidationsubset.
samplenegativesforQ−,i.e. includingonly
negativepromptsforobjectsinthescene,or
includingallotherdatasetobjects. ResultsareshowninTable9. First,weobservethatmaxoperator
generally outperforms mean, with the exception of when using all negatives. However, the best
configurationwasusingmaxoperatorwithscenenegatives. Second,usingopenpromptsprovides
marginalimprovementsoverclsinallothersettings. Finally,usingscenenegativesoutperforms
usingallinmostcases. Thisisbecausewhenusingallnegativesfromthedataset,somesemantic
conceptswillbehighlysimilarwiththepositiveprompt,makingthemetrictoo‘strict’,asonlyfew
viewswillpasstheconditionG ≥0.
v,n
21

<!-- Page 22 -->

Inference strategies As discussed in Sec. 3.4 there are

### Ref.Segm.(%)


### Method Negatives

two methods for performing referring segmentation in- mIoU Pr@25 Pr@50 Pr@75
ference: (a) selecting all points with higher probability ρ+>P− scene 73.7 77.4 73.0 69.8
ρ+>P− canonical 53.4 57.4 52.6 49.7
for positive vs. maximum negative prompt ρ+ > P−, ρ+>P− all 30.8 31.0 31.0 30.8
or(b)thresholdingρ+ withahyper-parameters . Ad- sthr@0.95 scene 82.8 84.0 83.2 82.0
thr sthr@0.95 canonical 75.2 77.6 74.7 72.9
ditionally, we compare the final referring segmentation sthr@0.95 all 74.9 76.6 75.4 73.0
sthr@0.95 - 70.2 70.6 69.9 69.5
performancebasedonthenegativepromptsusedattest sthr@0.9 scene 82.1 83.6 82.8 79.8
time: (a)promptsfromobjectinstanceswithinthescene, sthr@0.8 scene 79.9 83.0 80.4 75.7
(b)promptsfromalldatasetobjectinstances(similarto
Table10:Inferencemethodablationstudies.
semanticsegmentationtask),(c)fixedcanonicalphrases
{“object”,“thing”,“texture”,“stuff”}[13],and(d)nonegativeprompts(-),wherewethresholdthe
rawcosinesimilaritieswiththepositivequery. ResultsinTable10. Weobservethatthresholding
providesbetterresultsthanthefirstmethodwhentherightthresholdischosen,aresultwhichwe
foundholdsalsoforourdistilledmodel. Ahighthresholdof0.95wasfoundoptimalforupperbound
experiments,whileathresholdof0.7forourdistilledmodel,althoughwefurtherfine-tuneditfor
zero-shotandrobotexperiments(seeSec.A.6). Regardingnegativeprompts,asexpected,providing
in-scenenegativesgivesthebestresults,withasignificantdeltafromcanonical(7.6%),all(7.9%)
andnonegatives(12.6%). However,weobservethatevenwithoutsuchprior,theperformanceisstill
competitive,evenwhenentirelyskippingnegativeprompts.

### A.4 BaselineImplementations

OpenSeg[9]extendsCLIP’simage-levelvisualrepresentationstopixel-level, byfirstproposing
instancesegmentationmasksandthenaligningthemtomatchedtextcaptions. Givenatextquery,
withOpenSegwecanobtaina2Dinstancesegmentationmask. Forextendingto3D,weproject
the2Dmaskpixelsto3Daccordingtothemaskregion’sdepthvaluesandcameraintrinsicsand
transformtoworldframe.
LSeg[10]similarlytrainsanimageencodertobealignedwithCLIPtextembeddingsatpixel-level
with dense contranstive loss, therefore allowing open-vocabulary queries at test-time. Similar to
OpenSeg,weproject2Dpredictionsto3Daccordingtodepthandcameraintrinsicsandtransformto
worldframetocomputemetrics.
MaskCLIP[8]providesadrop-inreparameterizationtrickintheattentionpoolinglayerofCLIP’s
ViTencoder,enablingtext-alignedpatchfeaturesthatcanbedirectlyusedforgroundingtasks. We
usebicubicinterpolationtoupsamplethepatch-levelfeaturestopixel-levelbeforecomputingcosine
similaritieswithtextqueries. SimilartoOpenSegandLSeg,weprojectandtransformthepredicted
2Dmasktocalculate3Dmetrics.
OpenScene[12]isthefirstmethodtointroducethe3Dfeaturedistillationmethodologyforroom
scandatasets.ItutilizesOpenSeg[9]toextractpixel-level2Dfeaturesandfusesthempoint-wisewith
vanillaaveragepooling,asformulatedinSec.3.1. Toprovidefaircomparisonswithourapproach,
andaswefoundthatMaskCLIP’sfeaturesperformfavourablyvs. OpenSeg’s,weusepatch-wise
MaskCLIPfeatures,interpolatedtooriginalimagesize. Weaggregateall73views,performvanilla
featurefusioninthefullpoint-cloud,andmeasurethefinalfused3Dfeature’sperformanceasthe
OpenScene performance. We highlight that this setup represents the upper-bound performance
OpenScenecanprovide,asweusethetarget3Dfeaturesandnotdistilledonesobtainedthrough
training,whichwerefrainedfromdoing,asourresultsalreadyoutperformOpenScene’supperbound.
OpenMask3D[6]isarecenttwo-stagemethodforreferringsegmentationinpoint-clouddata. Inthe
firststage,Mask3D[42]isusedfor3Dinstancesegmentation,providingasetofobjectproposals. In
thesecondstage,multi-scalecropsareextractedfromrenderedviewsaroundeachproposedinstance
andpassedtoCLIPtoobtainobject-levelfeatures. Forourimplementation,similartoabove,wewish
toestablishanupper-boundofperformanceOpenMask3Dcanobtain. Tothatend,weskipMask3D
inthefirststageandprovideground-truth3Dsegmentationmasks. Werepresenteachinstancewitha
22

<!-- Page 23 -->

Figure12: PCAfeatureandreferringgroundingvisualizationofbaselinemethodsandDROP-CLIP.Foreach
scene,wepresentresultsforOpenScene,OpenMask3D,andourDROP-CLIP(fromtoptobottom).Theblue
rectangledenotescaseswhereOpenMask3Dsuffersfromdistractorobjects,whileDROP-CLIPdoesn’t.Thered
rectangledenotescaseswhereOpenMask3Dtotallyfailstogroundthetarget,whileDROP-CLIPsucceeds.
pooledCLIPfeaturefrom3multi-scalecropsof0.1expansionratio,obtainedthroughallofour73
viewsandweightedaccordingtothevisibilitymapΛ (seeSec.3.2),asintheoriginalpaper.
v,n

### A.5 QualitativeResults

Wepresentqualitativeresultsinseveralaspectstoillustrate(1)Howtheobject-centricpriorshelp
in multi-view feature fusion (Section A.5.1); (2) How do the distilled 3D features perform from
single-viewsettinginMV-TODsemantic/referringsegmentationtasks? (SectionA.5.2).
23

<!-- Page 24 -->

Figure13: PCAfeatureandreferringgroundingvisualizationofbaselinemethodsandDROP-CLIP.Foreach
scene,wepresentresultsforOpenScene,OpenMask3D,andourDROP-CLIP(fromtoptobottom).Theblue
rectangledenotescaseswhereOpenMask3Dsuffersfromdistractorobjects,whileDROP-CLIPdoesn’t.Thered
rectangledenotescaseswhereOpenMask3Dtotallyfailstogroundthetarget,whileDROP-CLIPsucceeds.

### A.5.1 EffectofObject-CentricPriorsinMulti-ViewFeatureFusion

We present more visualizations to demonstrate the difference between our method and previous
multi-viewfeaturefusionapproaches,highlightingtheeffectivenessofinjectingobject-centricpriors
infusingprocess. TheresultsinFig.12andFig.13showtheupperboundfeaturesofOpenScene[12],
OpenMask3D[6],andourDROP-CLIP.Itcanbeseenthatbyintroducingthesegmentationmask
spatialpriors,bothOpenMask3DandDROP-CLIPcanobtainmorecrispyfeaturesinthelatentspace
andalsoachievebetterlanguagegroundingresults. Todemonstratethebenefitofintroducingthe
24

<!-- Page 25 -->

Figure14: Semantic/ReferringsegmentationwithourDROP-CLIP.IntheSem@columns,thesamecolors
denote the same object category. The white parts mean that this part of the object is not activated by the
correspondingclassnamequery.
semanticinformativenessmetricinfeaturefusion,weaddextraannotationinFig.12andFig.13.
ThebluerectangledenotesthecaseswhereOpenMask3Dsuffersfromthedistractors(i.e. multiple
objects have high similarity score with the given query), while our DROP-CLIP is not. The red
rectangledenotesthecaseswhereOpenMask3Dtotallyfailedtogroundthecorrectobject,whileour
DROP-CLIPsucceed. Inconclusion,introducingsemanticinformativenessresultsinmorerobust
object-levelembeddingsthatinturnleadtohighergroundingaccuracy.

### A.5.2 Referring/SemanticSegmentationQualitativeResults

ReferringsegmentationSinceDROP-CLIPisnottrainedonclosed-setvocabularydatasetbutrather
toreconstructthefusedmulti-viewCLIPfeatures,thedistilledfeaturesnaturallyliveinCLIPtext
space. Asaresult,wecanconductreferringexpressionsegmentationin3Dwithopenvocabularies.
WedemonstratethisabilityinFig.14byshowingthegroundingresultsofthetrainedDROP-CLIP
queriedwithdifferentlanguageexpression,includingclassname,classname+attribute,affordance,
andopeninstance-specificqueries.
SemanticsegmentationWepresentsemanticsegmentationresultsofourDROP-CLIPinFig.14.
ThewhitepartsinFig.14meanthatthispartoftheobjectisnotactivatedbythecorrespondingclass
namequery.
25

<!-- Page 26 -->

Figure 15: Visualization of referring segmentation examples in OCID-VLG ((left) and REGRAD (right)
datasets.

### A.6 Zero-ShotTransferExperimentsDetails

To study the transferability of our learned 3D features in novel tabletop domains, in Sec. 4.3 we
conductedsingle-viewsemanticsegmentationexperimentsintheOCID-VLGdataset. Inthissetup,
similartooursingle-viewMV-TODexperiments,weprojecttheinputRGB-Dimagetoobtaina
partialpoint-cloudandfeedittoDROP-CLIPtoreconstruct3DCLIPfeatures. Torepresentthe
point-clouds in the same scale as our MV-TOD training scenes, we sweep over multiple scaling
factorsandreporttheoneswiththebestrecordedperformance. For2Dbaselines, themIoU and
mAcc@Xmetricswerecomputedbasedontheground-truth2Dinstancesegmentationmasksofeach
scene,afterprojectedto3Dwiththedepthimageandcameraintrinsicsandtransformedtoworld
frame,fixedatthecenterofthetabletopofeachdataset.

### A.6.1 Zero-ShotReferringSegmentationExperiments

SincemethodsLSegandOpenSegwerefine-tunedforsemanticsegmentation,theyarenotsuitable
forgroundingarbitraryreferringexpressions,butonlycategorynamesasqueries,whichiswhywe
conductedsemanticsegmentationexperimentsinourmainpaper. Tofurtherstudyzero-shotreferring
segmentation generalization, we conducted additional experiments in both OCID-VLG [31] and
REGRAD[30]datasets. WecomparewiththeMaskCLIPbaseline,projectedto3Dsimilartoabove.
ForboththeMaskCLIPbaselineandDROP-CLIP,weusethresholdinginferencestrategy,sweep
overthresholds{0.4,...,0.9}andrecordthebestconfigurationforbothmethods. Weanalyzethe
utiliseddatasetsbelow:
OCID-VLG[31]connects4-DoFgraspannotationsfromOCID-Grasp[74]datasetwithsingle-view
RGBsceneimagesandlanguagedatageneratedautomaticallywithtemplatedreferringexpressions.
Weevaluateinonereferringexpressionpersceneforatotalof490scenes,165fromthevalidation
and325fromthetestsetoftheuniquesplitprovidedbytheauthors. Weusethedataset’sreferring
expressionsfromnametypeasqueries,afterparsingouttheverb(i.e. “pickthe”),whichcontains
open descriptions for 58 unique object instances, incl. concepts such as brand, flavor etc. (e.g.
“Kleenextissues”,“ChocoKrispiescornflakes”,“Colgate”). Forremovingthetablepoints,weuse
theprovidedground-truth2Dsegmentationmasktoprojectonlyinstancepointsto3DforDROP-
CLIP.Wesweepoverscalingfactors{8,...,16}inthevalidationsetandreportthebestobtained
results.
REGRAD[30]focuseson6-DoFgraspannotationsandmanipulationrelationsforclutteredtabletop
scenes. Scenesarerenderedfromapoolof50kuniqueShapeNet[37]3Dmodelsfrom55categories
with9RGB-Dviewsfromafixedheight. Wetestin1000randomscenesfromseen-valsplit,using
ShapeNet category names as queries. We note that as REGRAD doesn’t focus on semantics but
26

<!-- Page 27 -->

Figure16: Zero-shotinstancesegmentationwithourDROP-CLIP.IntheGT andPredcolumns,thesame
colorsdenotethesameinstance.
grasping, most of its objects are not typical household objects, but furniture objects (e.g. tables,
benches,closetsetc.) scaleddownandplacedinthetabletop. Wefilteroutquerieswithsuchobject
instances and experiment with the remaining 16 categories that represent household objects (e.g.
“bottle”,“mug”,“camera”etc.). Wesweepoverscalingfactors{6,...,20}. Weusethefilteredfull
point-cloudsprovidedbytheauthorstoidentifythetablepointsandremovethemfromeachview.
More qualitative results for both datasets are illustrated

## Ocid-Vlg Regrad


### Method

inFig.15,whilecomparativeresultswithMaskCLIPare
mIoU Pr@25 mIoU Pr@25
giveninTable11. Weobservethatourmethodprovidesa MaskCLIP→3D 40.4 45.2 33.2 39.0
significantperformanceboostacrossbothdomains(5.8% DROP-CLIP 46.2 48.9 59.1 63.0
mIoU deltainOCID-VLGand25.9%inREGRAD),es- Table11: Zero-shotreferringsegmentation
resultsinOCID-VLGandREGRADdatasets
peciallyinREGRADscenes,whereobjectsmostlymiss
fine texture and have plain colors, thus leading to poor
MaskCLIPpredictionscomparedtoDROP-CLIP,whichconsidersthe3Dgeometryofthescene.
FailureswereobservedincasesofveryuniquereferringqueriesinOCID-VLG(e.g. "Kehpackage")
andincasesofveryheavilyoccludedobjectinstancesinbothdatasets.

### A.6.2 Zero-Shot3DInstanceSegmentationExperiments

Integrating spatial object priors via segmentation masks when fusing multi-view features grants
separabilityintheembeddingspace. Toillustratethat,weconductedzero-shotinstancesegmentation
withourDROP-CLIPbydirectlyapplyingDBSCANclusteringintheoutputfeaturespace. Inour
experiments,weusethevanillaimplementationofDBSCANfromscikit-learnpackageandset
ϵ=0.01, min_samples=2forDROP-CLIPandϵ=0.01, min_samples=276forOpenScene
respectively. Weobservedthatthepointsthatbelongtothesameobjectinstanceareclosetoeach
otherinthefeaturespace,whilesignificantlydifferfromthepointsthatbelongtootherinstances. We
visualizeseveralexamplesinFig.16,wherewealsoconductat-SNEvisualizationtodemonstrate
theinstance-levelseparabilityintheDROP-CLIPfeaturespace.
27

<!-- Page 28 -->


### A.6.3 ComparisonswithSfMmethods

In this section we compare DROP with mod-

### Method Modality Num. Train Segm. Results

ern2D→3Dfeaturedistillationmethodsbased Views Time Model Loc. Sem.Segm.
on Structure-from-Motion (SfM), obtained via L L E an R g F Splat S S f f M M 1 1 7 7 1 1 1 3 1 7 2 .5 .5 m m i i n n . . SA - M 8 8 4 8 . . 8 1 4 6 5 5 . . 0 1
SemanticGaussians SfM 171 >2hrs. SAM 89.8 -
trainingNeRFs[13,19,16,18]or3DGaussian

### LSeg RGB 1 0 - 33.9 21.7

Splatting(3DGS)[24,75,76,77]. Wehighlight DROP-CLIP RGB-D 1 0 - 66.1 39.1
howeverthatthisisnotreallyan“applestoap- Table12: Localizationaccuracy(%)and3Dsemantic
segmentationmIoU(%)onthe‘teatime’sceneofLERF
ples"comparison,sinceSfMapproachesdiffer
dataset. Wereportnumberofviews,trainingtimeand
from our method in philosophy and scope of
whether/whichexternalmodelsareneededtoobtain
application. Inparticular,SfMapproachesper- therepresentation.Trainingtimesareconvertedtov100
formonlinedistillationinspecificscenes,and hoursfromreportednumbersincorrespondingpapers.
thusrequiremultiplecameraimagestodistill,as
wellassignificanttimetodotraining/inference.
The obtained scene representation cannot be applied in new scenes, for which a new multi-view
imagesdatasethastobeconstructedandanewNeRF/3DGSbetrainedfromscratch. Incontrast,our
approachreliesondepthsensorstoacquire3DanddoesnotneedSfMreconstruction. Thefeature
distillationisperformedofflineonce,intheMV-TODdataset,andthuscanbeappliedzero-shotin
novelscenes. Further,itdoesnotrequiremultiplecameraimages(worksfromsingle-view),does
notrequiretrainingandsupportsreal-timeinference. Nevertheless,wewanttoquantifytherelative
performanceofDROP-CLIPwithSfMmethodsthathavebeendistilledforspecificscenes.
WereplicatethesetupofthelocalizationtaskfromLERF[13]andthesemanticsegmentationtask
fromLangSplat[24]forthe‘teatime’sceneoftheLERFdataset. ResultsarepresentedinTable12,
wherenumbersforrepresentativebaselinesLSeg[10], LERF[13], LangSplat[24]andSemantic
Gaussians [75] are taken from corresponding papers. To signify the aforementioned differences
in scope, in our table we also report number of views and training time required to obtain the
representation(convertedinv100hoursfromtimereportedincorrespondingpapers)andwhether
/ which external segmentation models (e.g. SAM [43]) is needed during test-time to deal with
the‘patchyness’issue. Theabovedemonstratethepracticalbenefitsofourapproachcomparedto
SfMmethods, asmentionedbefore, workingfromsingle-view, real-timeperformance, zero-shot
applicationandnoneedforexternalsegmentors. Regardingtestresults,wefindthatDROPscores
lowertoSfMbaselinesinbothtaskvariants,butsignificantlyoutperformsLSeg,whichistheonly
otherzero-shotbaseline. TheperformancemarginbetweenDROPandobject-centric3DGSmethods
LangSplat and SemanticGaussians is significant, albeit the fact that these methods require SAM
attest-timetoinjectthesegmentationpriors, whereasDROPdoesn’t. Thisgapisjustifiedwhen
consideringthatourapproachiszero-shotanddidn’thaveaccesstothe171trainingsceneslikethe
SfMbaselines,aswellasthatthedatasetqueriesareoftenreferringtoobjectparts(e.g. hooves,bear
noseetc.),whichDROPhasnotbeendesignedfor. QualitativevisualizationsofDROPintheLERF
scenearegiveninFig.17.

### A.7 RobotExperiments

Setup Our robot setup consists of two UR5e arms with Robotiq 2F-140 grippers and an ASUS
Xtiondepthcameramountedfromanelevatedviewbetweenthearms. Weconducted50trialsinthe
Gazebosimulator[45]and10witharealrobot. Forsimulation,weused29uniqueobjectinstances
from 9 categories (i.e. soda cans, fruit, bowls, juice boxes, milk boxes, bottles, cans, books and
edibleproducts). Forrealrobotexperiments,wemostlyusedpackagedproductsandedibles. Ineach
trial,weplace5-12objectsinadesignatedworkspacearea. Objectsareeitherscatteredacrossthe
workspace, packedtogetherinthecenterorpartiallyplacedinthesameareainordertoemulate
differentlevelsofclutter. Weprovideaqueryindicatingatargetobjectusingeithercategoryname,
color/material/stateattribute,useraffordance(e.g. “I’mthirsty”),oropeninstance-leveldescription,
typicallyreferringtotheobject’sbrand(e.g. “Pepsi”, “Fanta”etc.) orflavor(e.g. “strawberry
juice”,“mangojuice”etc.) Wenotethatdistractorobjectinstancesofthesamecategoryasthetarget
objectareincludedintrialswherequeryisnotthecategoryname.
28

<!-- Page 29 -->

Figure17: Visualizationsofpartialpoint-clouds,3DDROP-CLIPfeatures(PCA)andsimilarityheatmapsfor
threedifferentqueriesinthe‘teatime’sceneofLERFdataset.
Figure 18: Illustration of robot system for language-guided 6-DoF grasping, using our DROP-CLIP for
grounding(top),andHGGDnetwork[44]forgraspdetection(bottom).
Figure19: VisualizationofrobotexperimentsinGazebo(top)andwitharealrobot(bottom).
ImplementationWedevelopourlanguage-guidedgraspingbehaviorinROS,usingDROP-CLIP
for grounding the user’s query and RGB-D grasp detection network, HGGD [44], for generating
29

<!-- Page 30 -->

6-DoFgraspproposals. OurpipelineisshowninFig.18. Weprocesstherawsensorpoint-cloud
withRANSACfromopen3dlibrarywithdistancethreshold0.1,ransac_n=3and1000iterations
to segment out the table points, and then upscale to ×10. We use in-scene category names as
negativepromptsanddoinferencewithathresholdof0.7. Tomatchthegroundedobjectpoints
withgraspproposals, wetransformpredictedgraspstoworldframeandmovetheircenteratthe
gripper’stip. Wethencalculateeuclideandistancesbetweenthegripper’stipandthethresholded
prediction’scenter. Inrealrobotexperiments,werunstatisticaloutlierremovalfromopen3dwith
neighbor_size=25andstd_ratio=2.0toremovenoisypointsfromtheprediction’scenter. The
top-3closestgraspsaregivenasgoalforaninversekinematicsmotionplanner. Wemanuallymark
graspattemptsassuccess/failureinrealrobotandleveragethesimulatorstatetodoitautomatically
inGazebo. Visualizationsofsimulated/realrobottrialsareillustratedinFig.19,experimentswith
groundingdifferentobjectswithfine-grainedattributesinFig.20,whilerelatedvideosareincluded
assupplemetarymaterial.

### A.8 DetailedRelatedWork

Inthissectionweprovideamorecomprehensiveoverviewofcomparisonswithrelatedwork.
Semantic priors for CLIP in 3D A line of works aim to learn 3D representations that are coembedded in text space by leveraging textual data, typically with contrastive losses [78, 79, 80].
CG3D[81]aimstolearnamulti-modalembeddingspacebyapplyingcontrastivelosson3Dfeatures
frompoint-cloudsandcorrespondingmulti-viewimageandtextualdata,whileusingprompttuning
tomitigatethe3D-imagedomaingap. MostabovemethodsleadtoadegradationinCLIP’sopenvocabularycapabilitiesduetothefine-tuningstages. Incontrast,ourworkleveragestextualdatanot
fortrainingbutforguidingmulti-viewvisualfeaturefusion,henceleavingthelearnedembedding
spaceintactfromCLIPpretraining.
SpatialpriorsforCLIPin3DSeveralworksproposetoleveragespatialobject-levelinformationto
guideCLIPfeaturecomputationin3Dsceneunderstandingcontext. OpenMask3D[6]leveragesa
pretrainedinstancesegmentationmethodtoprovideobjectproposals,andthenextractsanobjectlevelfeaturebyfusingCLIPfeaturesfrommulti-scalecrops. Similarly,OpenIns3D[82]generates
objectproposalsandemploysaMask-Snap-Lookupmoduletoutilizesynthetic-sceneimagesacross
multiple scales. In similar vein, works such as Open3DIS [14], OVIR-3D [83], SAM3D [84],
MaskClustering[85]andSAI3D[86]leveragepretrained2Dmodelstogenerate2Dinstance-wise
masks,whicharethenback-projectedontotheassociated3Dpointcloud. Allaboveapproachesare
two-stageapproachesthatrelyontheinstancesegmentationperformanceofthepretrainedmodel
inthefirststage,thussufferingfromcascadingeffectswhensegmentationsarenotaccurateorwell
alignedacrossviews. Incontrast,ourmethodleveragesspatialpriorsduringthemulti-viewfeature
Figure20: Visualizationofgroundingqueriesinrealrobottrials,forbaselinemethodMaskCLIP→3D(bottom)
andourDROP-CLIP(top),whereweensemblethepredictionsofourmethodwiththe2Dbaseline.DROP-CLIP
producesmorerobustfeatures(middlecolumn)whichleadtocrispiersegmentation(rightcolumn.)
30

<!-- Page 31 -->

fusion process, and then distills the final features with a point-cloud encoder, and therefore is a
single-stagemethodthatdoesnotrequireobjectproposalsattesttime.
Offline3DCLIPFeatureDistillationOpenScene[12]distillsOpenSeg[9]multi-viewfeatureswith
apoint-cloudencoder,whilefollow-upworkOpen3DSG[15]extendstoscenegraphgenerationby
furtherdistillingobject-pairrepresentationsfromothervision-languagefoundationmodels[87]as
graphedges. CLIP-FO3D[21]replacesOpenSegpixel-wisefeatureswithmulti-scalecropsfrom
CLIPtofurtherenhancegeneralization. Allaboveworksusedense2Dfeaturesandfusepoint-wise,
thus suffering from ‘patchyness’ issue. Further, these works distill features using 3D room scan
data[22,1],whichlackdiverseobjectcatalogsanddonothavetodealwiththeeffectsofclutterin
themulti-viewfusionprocess,aswedowiththeintroductionofMV-TOD.
Online3DCLIPFeatureDistillationLERF[13]replacespoint-cloudencoderswithneuralfields,
anddistilsmulti-scalecropCLIPfeaturesintoacontinuousfeaturefieldthatcanprovidefeaturesin
anyregionoftheinputspace. Theauthorsdealwiththe‘patchyness’issueusingDINOregularization.
SimilarworksOpenNeRF[19]andF3RM[16]useMaskCLIPtoextractfeaturesandavoidDINO-
regularization. All above works make the assumption that all views are equally informative and
rely on dense number of views at test-time to resolve the noise in the distilled features. A more
recentlineofworksreplaceNeRFswith3DGaussianSplatting(3DGS)[88]toimproveinference
time and memory consumption and perform similar feature distillation from LSeg, OpenSeg or
CLIPmulti-scalecrops. Similartoourwork,some3DGSapproaches[24,75,76,77]alsoexploit
spatial priors (i.e. segmentation masks) to distill object-level CLIP features, but do not perform
view selection based on semantics. Further, 3DGS approaches lie in the same general family of
works as fields, i.e., online distillation in specific scenes, requiring multiple camera images and
computationalresourcestoworkattest-time. Incontrast,ourmethodisdistilledofflineinMV-TOD
toreconstructsemantically-informed,view-independent3Dfeaturesfromsingle-viewRGB-Dinputs,
canbeappliedzero-shotinnovelsceneswithouttraining,andenablesreal-timeinference.
31

## Tables

**Table (Page 3):**

| Category: Beverage can Color: Red, white, silver Material: Aluminum State: Sealed Brand: Coca-cola GPT4-Vision Utility: Used for containing and consuming Affordance: I need something refreshing I want a cold drink I feel like having a soda Concept More descriptions: descriptions C So o d ke a c c a a n n sh Aluminum drink can |
|---|
|  |


**Table (Page 8):**

|  |  |  |  |  |
|---|---|---|---|---|
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |


**Table (Page 8):**

|  |  |  |  |  |
|---|---|---|---|---|
|  |  |  |  |  |
|  |  |  |  |  |
|  | entat |  | np | reci |


**Table (Page 19):**

|  |
|---|
|  |
| Please provide a set of text descriptions for the object shown in the input images. The input images are multiview observation of the object. The descriptions should describe the object color, material, stateF (ei.gg. uif Ir geive1 y0ou: thNe imuagme obf ae browol, fyoou sbhojueldc tetlsl if ithne beowal cemhptyc oar tfuell)g, aos rwyell aisn utiMlity (Ve.g-. Tif I OgivDe yo.u the image of a hammer, you should say: "Something to do general carpentry, framing, nail pulling, cabinet making, assembling furniture, upholstering, finishing, riveting, bending or shaping metal, striking masonry drills and steel chisels, and so on"). Finally, provide a list of specific object descriptions that would be commonly used to refer to that object (e.g. If I give you an image of a coca-cola can, you could return: "[Coke, Coke-can, Coca-Cola, Cola, Cola-can, Cola-drink, ...]". If the object is a product, please try to identify and give its brand (e.g. "Coca-cola, "Fanta" etc.). Also provide a few `affordance` descriptions, which is what a user would say if they desired that object (e.g. If I give you an image of an apple, say: "I'm hungry", "I want to eat something healthy", etc.). Please reply with the following format: RESPONSE_FORMAT: --- Category: [give object category] Color: [give object color] Material: [give object material] State: [give object state] Brand: [optional - give product brand] Title: [optional - give the title for object ONLY] Utility: [give object utility] Affordance: [give user instructions] More descriptions: [give a list of specific object descriptions] --- Please in your descriptions avoid words like "Appears to be [...]", "Appears [...]", "The object is [...]" etc., just give the noun/adjective descriptions. Provide descriptions for the following {label} object |
