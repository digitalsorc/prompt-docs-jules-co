---
title: "Scientific Literature Mining"
original_file: "./Scientific_Literature_Mining.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["llm", "rag", "fine-tuning", "evaluation", "multimodal"]
keywords: ["data", "page", "cvc", "kvasir", "table", "normdel", "uoim", "dataset", "pretrainingdata", "effective"]
summary: "<!-- Page 1 -->

A Medical Data-Effective Learning Benchmark for Highly
Efficient Pre-training of Foundation Models

### WenxuanYang∗ WeiminTan∗

ShanghaiKeyLaboratoryofIntelligentInformation ShanghaiKeyLaboratoryofIntelligentInformation
Processing,SchoolofComputerScience,FudanUniversity Processing,SchoolofComputerScience,FudanUniversity

### Shanghai,China Shanghai,China

wxyang23@m.fudan.edu.cn wmtan@fudan.edu.cn

### YuqiSun BoYan†

ShanghaiKeyLaboratoryofIntelligentInformation ShanghaiKeyLab"
related_documents: []
---

# Scientific Literature Mining

<!-- Page 1 -->

A Medical Data-Effective Learning Benchmark for Highly
Efficient Pre-training of Foundation Models

### WenxuanYang∗ WeiminTan∗

ShanghaiKeyLaboratoryofIntelligentInformation ShanghaiKeyLaboratoryofIntelligentInformation
Processing,SchoolofComputerScience,FudanUniversity Processing,SchoolofComputerScience,FudanUniversity

### Shanghai,China Shanghai,China

wxyang23@m.fudan.edu.cn wmtan@fudan.edu.cn

### YuqiSun BoYan†

ShanghaiKeyLaboratoryofIntelligentInformation ShanghaiKeyLaboratoryofIntelligentInformation
Processing,SchoolofComputerScience,FudanUniversity Processing,SchoolofComputerScience,FudanUniversity

### Shanghai,China Shanghai,China

yqsun22@m.fudan.edu.cn byan@fudan.edu.cn

### Abstract CCSConcepts

Foundationmodels,pre-trainedonmassivedatasets,haveachieved •Computingmethodologies→Computervision.
unprecedentedgeneralizability.However,isittrulynecessaryto
involvesuchvastamountsofdatainpre-training,consumingexten- Keywords
sivecomputationalresources?Thispaperintroducesdata-effective Medical benchmark, Data-Effective learning, Endoscopic Image
learning,aimingtousedatainthemostimpactfulwaytopre-train Processing,FoundationModel
foundationmodels.Thisinvolvesstrategiesthatfocusondataqual-

### ACMReferenceFormat:

ityratherthanquantity,ensuringthedatausedfortraininghas
WenxuanYang,WeiminTan,YuqiSun,andBoYan.2024.AMedicalDatahighinformationalvalue.Data-effectivelearningplaysaprofound
EffectiveLearningBenchmarkforHighlyEfficientPre-trainingofFounroleinacceleratingfoundationmodeltraining,reducingcompudationModels.InProceedingsofthe32ndACMInternationalConferenceon
tationalcosts,andsavingdatastorage,whichisveryimportant
Multimedia(MM’24),October28-November1,2024,Melbourne,VIC,Australia.
asthevolumeofmedicaldatainrecentyearshasgrownbeyond ACM,NewYork,NY,USA,10pages.https://doi.org/10.1145/3664647.3681313
manypeople’sexpectations.However,duetothelackofstandards
andcomprehensivebenchmark,researchonmedicaldata-effective a.
learningispoorlystudied.Toaddressthisgap,ourpaperintro- Large-Scale Data-Effective Compact Small

### Dataset Learning Dataset

ducesacomprehensivebenchmarkspecificallyforevaluatingdataeffectivelearninginthemedicalfield.Thisbenchmarkincludes
adatasetwithmillionsofdatasamplesfrom31medicalcenters Pre-train Pre-train

### Foundation ≈ Foundation

(DataDEL),abaselinemethodforcomparison(MedDEL),andanew Model Model
evaluationmetric(NormDEL)toobjectivelymeasuredata-effective b.
learningperformance.Ourextensiveexperimentalresultsshowthe A Comprehensive Medical Benchmark
baselineMedDELcanachieveperformancecomparabletotheorigi-

### DataDEL MedDEL NormDEL

nallargedatasetwithonly5%ofthedata.Establishingsuchanopen
d d a a t t a io -e n ff m ec o t d iv e e l l r e e a s r e n a i r n c g h b c e o n m c m hm un ar it k y is be c c ru au ci s a e l i f t or fa t c h i e lit m at e e d s ic e a ffi lf c o ie u n n t - (CC Mo lluu n ss ely ttee d c rr Do 11 m ,, E 22 pL ,, a 33 R ,, r e 44 a kr wd eem i p itu t h o d is v n ae td s a a d m up e li c c a lu te s s ter) 7 5 0 % . 9 da 5 t % a m≈IoU 1 7 0 2 0 . % 0 d 2 a % ta
d
d
a
ev
ta
el
u
o
s
p
e
m
,p
en
ro
t
m
of
o
c
te
o
s
st
c
-
o
e
l
ff
la
e
b
ct
o
i
r
v
a
e
t
,
iv
sc
e
a
b
la
r
b
e
l
a
e
k
,
t
a
h
n
r
d
ou
im
gh
p
s
a
,
c
a
t
n
fu
d
l
f
h
o
e
s
a
te
lt
r
h
s
c
t
a
h
r
e
e

### 𝑳𝑬𝑫𝒎𝒓𝒐𝑵 𝑳𝑬𝑫𝒎𝒓𝒐𝑵

solutions.ThebenchmarkcanbeaccessedatGitHubRepository. 66.26% > 56.59 %

### Dimension 1

• Million of data samples • Simple but effective • A comprehensive metric
∗WenxuanYangandWeiminTancontributedequallytothisworkandshouldbe • 31 medical centers • Only 5% original data • Integrating accuracy and
consideredco-firstauthors.BoYanisthecorrespondingauthor. data compactness

### Figure1:Data-EffectiveLearning(DEL)enablesmoreeffi-

Permissiontomakedigitalorhardcopiesofallorpartofthisworkforpersonalor
classroomuseisgrantedwithoutfeeprovidedthatcopiesarenotmadeordistributed cientpre-trainingoffoundationalmodels.(a)Data-effective
forprofitorcommercialadvantageandthatcopiesbearthisnoticeandthefullcitation learningaimstoobtainacompactsmalldatasetfromalargeonthefirstpage.Copyrightsforcomponentsofthisworkownedbyothersthanthe
scalepre-trainingdataset,butthetwodatasetshavesimilar
author(s)mustbehonored.Abstractingwithcreditispermitted.Tocopyotherwise,or
republish,topostonserversortoredistributetolists,requirespriorspecificpermission effectsonfoundationmodelpre-training.(b)Demonstration
and/orafee.Requestpermissionsfrompermissions@acm.org. ofourcomprehensivebenchmarkforDEL.Thebenchmark
MM’24,October28-November1,2024,Melbourne,VIC,Australia
includesadatasetofmillionsofdatasamplesfrom31med-
©2024Copyrightheldbytheowner/author(s).PublicationrightslicensedtoACM.
ACMISBN979-8-4007-0686-8/24/10 icalcenters(DataDEL),abaselinemethodforcomparison
https://doi.org/10.1145/3664647.3681313 (MedDEL),andanewevaluationmetric(NormDEL).
4202
guA
61
]GL.sc[
3v24571.1042:viXra

<!-- Page 2 -->

MM’24,October28-November1,2024,Melbourne,VIC,Australia WenxuanYang,WeiminTan,YuqiSunandBoYan
Table1:OverviewoftheproposedDataDELinourbenchmark.Weintegrate31medicalcenters,includingdataonthescaleof
millions,tobuildahigh-quality,large-scale,multi-diseasecomprehensivedataset,aimingtoprovideresearcherswithabetter
dataplatform.

### Division Dataset Task Medicalcenters Videos Frames Disease

ModelPre-training Gastrovision[29] Detectionandclassification 2 None 8,000 GI

### Hyper-Kvasir[8] Classification 1 374 110,079 GI


### Kvasir-Capsule[52] Classification 1 117 47,238 GI

Modeldownstreamtesting CVC-12k(CVC-ClinicDB)[6] Segmentation 1 None 612 polyp

### CVC-300[55] Segmentation Notmentioned None 60 polyp

CVC-ColonDB[7] Segmentation Notmentioned None 380 polyp

### EAD2019[5] Endoscopicartifacts 6 None 2,991 cancers

EDD2020[3] Segmentation,detection,andlocalization 4 None 380 polyp

### ETIS[51] Segmentation Notmentioned None 196 polyp


### ImageCLEFmed[27] Polypsegmentation 1 None 66,662 polyp

Kvasir-Instrument[28] Segmentation,detection,andlocalization 1 None 590 polyp
Kvasir-SEG[31] Segmentation,detection,andlocalization 4 None 1,000 polyp
Kvasir-Sessile[30] Segmentation,detection,andlocalization 4 None 196 polyp

### PolypGen2021[4] Polypsegmentation 6 None 3,762 polyp

1 Introduction Theissueofdata-effectivelearningisnotexclusivetoendoscopy
Theeffectivenessoffoundationmodelsdependsontheabundance datasets;itisalsoevidentinothertypesofmedicaldatasets.With
ofpre-trainingdata,anotionseeminglysupportedbyconsensus: therapidexpansionoffuturemedicaldata,efficientlyhandling
morepre-trainingdataleadstoenhancedmodelperformance.How- medicaldatasetsisthenextcrucialresearchproblemindata-driven
ever,isthisassumptiontrulyaccurate?Toexplorethisissue,we learningmethods[47].
introducetheconceptofdata-effectivelearning,whichplaysasig- Inrecentyears,therehasbeenrelevantresearchondata-effective
nificantroleinthefieldofmedicaldata,acceleratingfoundation learninginnaturalimagedatasetssuchasadversarialsamples[20],
modeltrainingandreducingstorageburdenintheeraofbigdata anddatabiases[56],aimingtoenhancetherobustnessandgen-
(Figure 1(a)). The global endoscopy surgery market is undergo- eralizationcapabilitiesofdeeplearningmodels.Theseworksin
ingsignificantdevelopment,withanestimateddailyadditionof naturaldatasetshaveshownpreliminaryeffectiveness,indicating
22,546,800,000videoframes[1].However,asubstantialpresence significantpotentialadvantagessuchasdatastorage,computational
ofdisruptiveandinvaliddata[45]significantlyhamperstraining resourcesavings,andefficientmodeltraining.However,despite
efficiencyandoccupiesaconsiderableamountofstoragespace[60]. theexponentialgrowthofmedicaldatasets,thereiscurrentlya
Therefore,achievingdata-effectiveinendoscopydatasetsholdsthe lackofsuchexplorationinthemedicalfield[58].Thisisattribfollowingspecialadvantages: utedtotheabsenceofrelevantbenchmarks,encompassingunified
datasets,baselinemethods,andcomprehensiveevaluationmetrics,
• Storage Savings: Assuming the use of traditional high- providingtheacademiccommunitywithabasisfordevelopingand
definitionendoscopes(1080p)[26],thedailyuncompressed comparingadvancedmethods.
endoscopy examination videos would require 12,756,493 Inadditiontotheabsenceofbenchmark,achievingdata-effective
TB(about13.06exabytes)ofstoragespace.Condensingen- inthefieldofendoscopyremainsahugechallenge[50]andisworth
doscopydatasetscanresultinsubstantialstoragesavings. exploringindepth.Traditionaldata-effectivetechniquesmaystrug-
• EnhancedModelEfficiency:[8]releasedthelargestdi- gletoworkeffectivelywithdatasetsthathavehigh-dimensional
gestive system image dataset (Hyper-Kvasir) to date and featuresorsparsedata.Inendoscopydatasets,thechallengelies
showedthatuponanalyzingdatasources,over90%ofvideo more in identifying subtle differences in images, which can be
framesconsistofdisruptiveandinvaliddata.Corecritical crucialformedicaldiagnosis.Therefore,accuratelydetermining
datacomprisesonly2%oftheentiredataset[30,31].Effi- thesimilarityofimagesinendoscopydatasetsisatoppriorityin
cientutilizationofcorecriticaldatacansignificantlyimprove research.Maintainingdataqualityandintegrityisakeyissuein
theefficiencyofmodeltraining,inordertoachieverapid data-effectivelearning[18],asitdirectlyaffectstheusabilityand
convergence. accuracyofthedataset.
• ComputationalResourceSavings:Withtheuseofasin- Ourresearchcontributionscanbesummarizedasfollows:
gleRTX3090graphicscardandtheVGG16model[33](approximately138millionparameters)for32-bitfloating-point • Weintroducetheconceptofdata-effectivelearningandpro-
(FP32)calculations,processing325.6imagespersecondis videacorrespondingmedicalbenchmark(Figure1(b))to
achievable[35].Inthisconfiguration,trainingonthedaily guidedata-effectivealgorithmresearchinthemedicalfield.
addedvideoframeswouldrequire19,200hours.Utilizing Furthermore, we integrate an open-source dataset called
onlycorecriticaldatacouldsavenearly18,816hourswithout DataDEL,sourcedfromamillion-leveldatasetspanning31
compromisingprecision. medicalcenters.

<!-- Page 3 -->

AMedicalData-EffectiveLearningBenchmarkforHighlyEfficientPre-trainingofFoundationModels MM’24,October28-November1,2024,Melbourne,VIC,Australia

### Norm

Attention Multi-Head
+ Norm MLP

### Embeddings

Dimension 1

### Stage i

Position Embedding

### Reshape +

Element-wise Add
Feature Map

### Position

Embedding
2
noisnemiD

### MedDEL Radius

(only compare within same cluster)

### Cluster 1, 2, 3, 4 kept data

Cluster 1, 2, 3, 4 removed duplicates

### Encoder

Vision Transformer
Patch

### Emb


### Linear Norm

Figure2:Pipelineofthebaselinemethod(MedDEL)fordata-effectivelearninginourbenchmark.Itillustrateseffectiveremoval
ofdisruptiveandinvaliddatafromthedataset,aimingtosavestoragespaceandcomputationalresourceswhileenhancing
modelefficiency.
• Inourbenchmark,weintroduceabaselinemethodcalled workeffectively.MFDedup[61]surpassesexistingtechnologiesin
MedDELfordata-effectivelearning,whichcanoutperform improvingdatareductionratesandrecoverythroughput,while
theuseof100%ofthedataindownstreamtaskswith5%of alsoreducingthecostofgarbagecollection.Storageandmemory
thepretrainingdatainextremecases. capacity[13]canalsobecomelimitingfactors.[24]discusseshow
• WedevelopanewmetriccalledNormDEL,toassesstheper- toaccuratelyestimatethedatareductionratioachievedthrough
formanceofdata-effectiveindatasets,whichconsidersthe data effective and compression techniques for specific datasets.
relationshipbetweentheproportionofthedatasetretained Hashmethods[46]indeedhaveawideapplicationindataeffective
andtheperformanceofdownstreamtasks. processing.TheCE-Dedup[38]frameworkcombineshash-based
imagedata-effectivetechniqueswithdeeplearningimageclassifi-
2 RelatedWork cationtasks.Byadjustingthededuplicationthreshold,effectively
Inthenaturalimagedomain,benchmarksforassessingdata-effective balancesthetrade-offbetweendatareductionrateandmodelacculearningtypicallyinvolvevarioustechniquessuchasstructuralsim- racy[21].[40]proposesadeepsupervisedhashalgorithmforimage
ilarityindex[17],convolutionalneuralnetworks[39],andlocal retrievalbyprovidingthemodelwithpairsofimageslabeledas
featuredescriptors[36].Thesemethods[44,57]areevaluatedon similar/dissimilar.[14]proposedaCore-setselectionmethodbased
widelyusedimagedatasetslikeImageNet[15,49]andCIFAR[34], onmetricexplanations(CSUME)fortheclassificationofmulti-class
orspecializeddatasets.PXDedup[59]explorestheissueofdata- electrocardiograms.Thisworkoffersusaneffectivemethodfor
effective learning in JPEG images, pointing out that traditional selectingrepresentativedatasetswithinanunsupervisedlearning
binarystream-basedtechniquesdonotworkwellforcompressed framework, which holds significant importance in the fields of
JPEGimages.[9]introducesahigh-precisionimagedataeffective medicalimagecomputingandhealthinformatics.
methodthatidentifiesandeliminatesduplicateimagesthrough However,inthemedicalfield,therecurrentlyexistsnosuch
featureextractionandhigh-dimensionalindexing[32].[10]uses benchmarkfortheresearchofdata-effectivelearningalgorithms.
waveletdecomposition[43]toextractfeaturevectorsfromimages
3 Data-EffectiveLearningMedicalBenchmark
andcalculatetheManhattandistancetodetermineimagesimilarity,
thusachievingthedetectionandremovalofduplicateimages.How- Inthissection,weintroducethedefinitionofbenchmarktasks.Dataever,whenhandlingdatasetswithhigh-dimensionalfeatures[48] effectivelearningreferstothepracticeofusingalimitedamount
orsparsedata[59],traditionaldata-effectivetechniquesmightnot ofdataforthepre-trainingphase[19].Therefore,thisbenchmark

<!-- Page 4 -->

MM’24,October28-November1,2024,Melbourne,VIC,Australia WenxuanYang,WeiminTan,YuqiSunandBoYan
encouragesresearcherstodevelopadvanceddata-effectivelearning Algorithm1PseudoCodeforMedDEL
methodstogenerateacompactversionoftheoriginallycollected Input:Imagesequence{𝐼
1

## ,𝐼

2
,...,𝐼 𝑛}
large-scaledataset,therebyobtainingacompactsmall-scalenew Parameter:Thresholds𝜖and𝜂
datasetforpre-trainingfoundationalmodels. 1: Let𝑡 =0
Intheeraofbigdata,largemodelsoftenrequiremassivepre-
2:
while𝑡 <max_iterationsdo
trainingdata[11].However,ourperspectivechallengesthiscon-
3:
for𝑐𝑙𝑢𝑠𝑡𝑒𝑟
𝑖
∈𝑐𝑙𝑢𝑠𝑡𝑒𝑟𝑠do
ventionalthinking,andwehaveundertakenthefollowingworkto 4: for𝑗 =1tosize(𝑐𝑙𝑢𝑠𝑡𝑒𝑟 𝑖)do
explorethisissueindepth. 5: ifdis(𝐹 𝑥,𝑗 ,𝑐𝑒𝑛𝑡𝑒𝑟𝑠 𝑖) >𝜖then
Ourbenchmarkconsistsofthreeparts,adatasetwithmillionsof
6:
Delete𝐼
𝑗
datasamples(DataDEL),abaselinemethodforcomparison(Med- 7: else
DEL)andanewevaluationmetric(NormDEL). 8: for𝑘 = 𝑗 toSize(𝑐𝑙𝑢𝑠𝑡𝑒𝑟 𝑖)do
9: ifcos(𝐹 𝑗 ,𝐹 𝑘) >𝜂then
3.1 Thebenchmarkdataset:DataDEL 10: ifdis(𝐹 𝑗 ,𝐶 𝑖) >dis(𝐹 𝑘 ,𝐶 𝑖)then
Giventheurgentdemandforacomprehensivebenchmarkinthe 11: Delete𝐼 𝑘
medicalfield,wearefacingthepressingtaskofintegratingdiverse 12: else
largedatasets.Currently,prevailingchallengeswithinexistingmed- 13: Delete𝐼 𝑗
icaldatasetsencompassissuesliketheuniformityofdatasources, 14: endif
thestandardizationoftaskexecution,thelimitedscopeofcovered 15: endif
diseasetypes,imbalancesindatasetcategories,andtheuniformity 16: endfor
ofmodalities[37]. 17: endif
Theselimitationshinderthecomprehensivedevelopmentofmed- 18: endfor
icalresearch.Therefore,thereisanurgentneedforustoconstruct 19: endfor
acomprehensivemedicaldataset.Oureffortsfocusonintegrating 20: Incrementiterationcounter:𝑡 ←𝑡+1
datasetsfromover31differentcentersand23differentcountries, 21: endwhile
spanningmultiplemodalitiessuchasimagesandvideos.Furthermore,ourdatasetsurpassesthemillion-scalemark,becominga Table2:Experimentalsettingfortheparameterof𝜂inAlgolarge-scalecollectionthatencompassesmultipletasks,modalities, rithm1thatcontrolsthedataremainingratio.Wesetseveral
sources,anddiseases.Thisdatasetcanproviderichanddiverse differentratiostofullyassesstheperformanceofMedDEL
supportforsubsequentresearch,offeringsignificantconvenience undervariousproportionsofremainingdata.Additionally,
forhealthcareprofessionalsandresearchinstitutions. wealsocalculatethenumberoftrainingepochsrequiredfor
differentratiosofdataatthesamecomputationalpowerfor
3.2 Thebenchmarkbaseline:MedDEL
faircomparison.
Weintroduceabenchmarkbaselinemethod(MedDEL)intheendoscopic medical field, which is based on the principles of the 𝜂 Remainingdata ratio Epochs
SemDeDupmethod[2].Endoscopicdataholdssignificantimpor- 1.0 88,282 100% 200
tanceinmedicaldiagnosisandtreatment.However,duetovarious 0.9 43,484 50% 400
factorssuchasorganmorphologicalchanges[53],lightingcon- 0.85 28,352 33% 600
ditions[12],andnoiseinterference[23],theanalysisofthisdata 0.8 16,789 20% 1,000
becomescomplexandchallenging. 0.75 9,055 10% 2,000
Specifically,theMedDELmethodtakesanimage𝐼 asan𝑖𝑡ℎ ex- 0.7 4,461 5% 4,000
ample,theencoderofVisionTransformer(ViT)[16]extractsdeep
featuresfromtheimage,ultimatelyproducinga768-dimensional
featureoutput.Thisoutputservesasourinformationembedding. {𝐹(𝑥,1),𝐹(𝑥,2),...,𝐹(𝑥,𝑛)}. For typical data-effective methods,
Thehigh-dimensionalrepresentationnotonlycapturestheseman- wehavetocalculatethesimilaritybetweenanytwopairsofembedticinformationoftheimagemoreeffectivelybutalsoaddresses
dings,resultinginanoveralltimecomplexityof𝑂(𝑛2).Takingour
semanticrepetitivenessissuesthatarechallengingtoresolvein proposedupstreamdatasetasanexample,whichincludes88,282
low-dimensionalspaces.Consideringtheencodingprocessofim- images,thetotalnumberofcalculationsreaches744million.
age𝐼throughtheViTmodel,wecanrepresentitwiththefollowing However,byintroducingtheK-meansalgorithm[42],theoverformula:
allcomputationalcomplexityisreducedfrom𝑂(𝑛2)to𝑂(𝑁2/𝑘),
where𝑘 is the number of clusters. After applying the K-means

### 𝐹 𝑥 =𝑉𝑖𝑇(𝐼) (1)

algorithm,weobtain𝑘clusters.Assumingthatthefeature𝐹(𝑥,𝑖)
belongstothe𝑘cluster,wecanderivethefollowing𝑘sequences:
Where𝑥 representsthefinallayerofthe𝑉𝑖𝑇 encoder.

### Afterobtainingthefeatureembeddingsforeachimageinthe

dataset,wecanexplorethesimilaritybetweenimagesinahigh- 𝐶 𝑘 ={𝐹(𝑥,𝑖) |𝑖 ∈𝑁∗,𝐹(𝑥,𝑖) ∈𝑐𝑙𝑢𝑠𝑡𝑒𝑟 𝑘} (2)
dimensionalspace.Lettheembeddingcorrespondingtothe𝑖𝑡ℎ

### Ineachcluster,datapointsthatarefarfromtheclustercentroid

image be denoted as 𝐹(𝑥,𝑖), representing all image features as areconsidereddisruptiveorinvaliddata.Tofilteroutinterference

<!-- Page 5 -->

AMedicalData-EffectiveLearningBenchmarkforHighlyEfficientPre-trainingofFoundationModels MM’24,October28-November1,2024,Melbourne,VIC,Australia
andinvaliddata,weintroduceapredefinedthreshold𝜖.Specifically, Duringthetrainingofallmodels,weselectivelyfilterthepreineachcluster𝐶
𝑗
wedefinethedistancefromimage𝑖tothecluster trainingdatasetcapacitybasedondifferentthresholdsof𝜖and𝜂.
centroidas𝑑 𝑖𝑗.Byusingthefollowinginequality,weclassifyimage Specifically,weset𝜖to0.9and𝜂from0.7to0.9withastepsizeof
𝑖aspotentiallyaffectedbydisruptiveorinvaliddata. 0.05.Consequently,weobtainthedatasetquantitiesaspresented
Specifically,weintroduceasimilaritythreshold𝜂,whichisused inTable2.Thebatchsizeissetto16,andthetrainingisconducted
todefinesemanticduplicateinformation.Incategory 𝑗,weper- usingAdamW[41]andacosinelearningrate[22].Themodelmainformsimilaritycalculationsforeachpairofembeddingsusingthe tainsapeaklearningrateof1.5×10−4 throughoutthetraining
followingformula: process.Inthevalidationofdownstreamtasks,weimplementa
simpleMulti-LayerPerceptron(MLP)[54]toachievesegmentation
𝑆(𝑝,𝑞)=𝑐𝑜𝑠(𝐹(𝑥,𝑝),𝐹(𝑥,𝑞)) (3) heads.
Throughthissimilaritycalculation,weretainasetoffeatures
4.2 EffectiveDataUtilizationwithMedDEL
thatareclosertotheclustercenter,achievingthegoaloffiltering
effectiveandcore-importantdata.Thepseudocodeforasimplified Figure 3 demonstrates that, under equivalent computational realgorithmregardingdataeffectivenessispresentedinAlgorithm1. sources,theMedDELmethodwhichoperatesonareduceddataset
(utilizingonly5%ofthedata,indicatedbytheredcurve),generally
3.3 Thebenchmarkevaluationmetric: performscomparablytothefulldataset(using100%ofthedata,
NormDEL indicated by the black curve) across various downstream tasks.

### Moreover,incertainspecificscenarios,duetoitssmallerdataset

Currently,thereisnocomprehensiveobjectivemetricforevaluatsizeandhigherdataquality,theMedDELmethodexhibitssuperior
ingtheperformanceofdata-effectivelearningalgorithms,where
performancewhentrainedonjust5%ofthedata.Thisadvantage
comprehensivereferstointegratingboththetestaccuracyofdownisparticularlypronounced,asseeninthecaseofCVC-300,highstreamtasksandthecompactnessofpre-trainingdata.Hence,We
lightingitseffectivenessinefficientlyleveragingasmallamountof
proposeanewdata-effectivemetric,theNormalizedData-Effective
high-qualitydata.ThisunderscorestheMedDELmethod’scharac-

### LearningIndex(NormDEL).Ourobjectiveisthatwithinthesame

teristicfocusandrefinementduringthelearningprocess,enabling
task,ifamodelcanachievethesamelevelofperformanceindownittomoreeffectivelycapturecrucialtaskfeatures,resultinginimstreamtasksusingfewerpre-trainingdata,itsdata-effectiveperforprovedperformanceinlow-datascenarios.Thisresultemphasizes
manceshouldbeconsideredsuperior.Takingthecommonlyused
thesignificanceofMedDELmethodinenhancingdataeffectiveness,
segmentationtaskinendoscopyasanexample,wherethegeneral
particularlyintheeraofbigdatawhenhigh-performancemodels
metricformeasuringperformanceisoftenmIoU(meanIntersection
areneeded,showcasingitscapabilityforeffectivedatautilization.
overUnion),wecanformulatethefollowingequation:

### 𝐷𝐸𝐿=𝑚𝐼𝑜𝑈 ·𝑒−𝛼·𝑅 (4) 4.3 StorageSavingAnalysis

Table3presentstheimpactofdifferentamountsofpre-training
Where𝛼servesasapositiveweightparameterusedtoadjustthe
dataonmIoUandNormDELacross8downstreamdatasets.Itis
influenceofmIoUandtheretentionratioinDEL,and𝑅represents
worthnoting,inthemajorityoftasks,themIoUachievedwithonly
theproportionoftheretaineddataset.
5%ofthedataiscomparabletothatachievedwith100%ofthedata.

### Subsequently,weaimtonormalizeDELtoarangebetween0

Toclearlyassesstheinfluenceofpre-trainingdatasetproportion
and1foraclearerdefinitionofdata-effectiveperformance.Thus,
onperformance,wecomputedNormDELforeachproportion.The
weobtainthedefinitionofNormDEL:
resultsindicatethatinsometasks,althoughthemIoUattainedwith
1 5%ofthedatamaynotbethehighestwhenconsideringdataset
𝑁𝑜𝑟𝑚𝐷𝐸𝐿= 1+𝑒−𝐷𝐸𝐿 (5) sizecomprehensively,itsNormDELreachesthehighest.

### Furthermore,Toanalyzeandevaluatetheaccuracyandrobust-

ThroughNormDEL,wecancomprehensivelyevaluatetheadaptness of the baseline method under the same time performance,
abilityofthedata-effectivemodelwithlimitedtrainingdata,em-
Figure4illustratesaboxplotofdifferentproportionsofpre-trained
phasizingthecriticalfactorsofmodeldata-effectiveinlarge-scale
datainvariousdownstreamdatasets,basedonthemIoUprobabilidatasets.
ties.Eachboxrepresentsthepredictiveperformanceofthemodel
duringtheseveralfinalepochs,employingthemedian,approximate
4 Experiment
quartiles,andthelowestandhighestprobabilitiestointuitively
ToassessthecapabilityofMedDEL,wetraintheFoundationModel displaythelevel,spread,andsymmetryofthemIoUdistribution.
onthreepre-trainingdatasetsaspresentedinTable1.Subsequently, Figure 4 demonstrates a unique trend in the performance of
weconductfinetuningondownstreamtaskdatasetstoevaluate models(measuredbythemedianmIoU)acrossmostdownstream
performance. tasks,inrelationtotheincreaseinthevolumeofpre-trainingdata.
Initially,performanceimproveswithanincreaseindatavolume,
4.1 Settings
reachingapeak,andthenstartstodeclineasdatavolumecontinues
ToachievethepretrainingoftheFoundationModel,enablingitto togrow.Specifically,whenasmallervolumeofdataisused(asin
provideabetterinitialvalueforthemajorityofendoscopytasks,we thecaseofthe5%datavolume),despitethelimitedquantity,the
usetheunsupervisedMaskedAutoEncoder(MAE-ViT-Base)[25]. averageinformationcontentperimageishigher,enablingthemodel

<!-- Page 6 -->

MM’24,October28-November1,2024,Melbourne,VIC,Australia WenxuanYang,WeiminTan,YuqiSunandBoYan
0.7
0.6
0.5
0.4
0.3
0.2
0.1
0 0 50 100 150 200 250 300 350 400 450 500
TrainingEpochs
UoIm
tseT
0.8
0.7
0.6
0.5
0.4
0.3
0.2

## Cvc300 0.1

5% data 100% data 0 0 50 100 150 200 250 300
TrainingEpochs
UoIm
tseT
0.7
0.6
0.5
0.4
0.3
0.2

### CVC-ClinicDB 0.1

5% data 100% data 0 50 100 150 200 250 300 350 400 450 500
TrainingEpochs
UoIm
tseT
0.5
0.45
0.4
0.35
0.3
0.25
0.2
0.15

### CVC-ColonDB 0.1

5% data 100% data 0.05 0 50 100 150 200 250 300
TrainingEpochs
UoIm
tseT

## Etis

5% data 100% data
0.8
0.7
0.6
0.5
0.4
0.3
0.2
0.1
0 20 40 60 80 100 120 140 160 180 200
TrainingEpochs
UoIm
tseT
0.8
0.7
0.6
0.5
0.4
0.3
0.2
ImageCLEFMed 0.1
5% data
100% data 0
0 20 40 60 80 100 120 140 160 180 200
Training Epochs
UoIm
tseT
0.7
0.6
0.5
0.4
0.3
0.2
Kvasir-Instrument 0.1
5% data
100% data 0
0 50 100 150 200 250 300 350 400 450 500
TrainingEpochs
UoIm
tseT
0.8
0.7
0.6
0.5
0.4
0.3
PolyGen2021 0.2
5% data
100% data 0.1
0 20 40 60 80 100 120 140 160 180 200
TrainingEpochs
UoIm
tseT
Kvasir-SEG
5% data
100% data
Figure3:Demonstrationofthefeasibilityofdata-effectivelearning.Wecomparedtheperformancedifferencesbetweenusing
only5%ofthepre-trainingdata(inred)andusing100%ofthedata(inblack)in8datasets.Theresultsindicatethatusingonly
5%ofthepre-trainingdatacanachieveresultscomparabletousing100%ofthepre-trainingdata,whichfullydemonstratesthe
validityoftheMedDELmethod.
Table3:DemonstrationoftherationalityofNormDEL.Thetableshowstheperformanceofdifferentproportionsofpre-trained
dataonmIoU(↑)aswellasNormDEL(↑)ineightdifferentdatasets.TheresultsindicatethattheperformanceofmIoUis
almostcomparableindifferentscales,suggestingthatitprimarilymeasuresperformancewithoutconsideringthescaleofthe
pre-trainingdataused.Incontrast,NormDELincorporatesthefactorofdatascale,andcanevaluatedatacompactnesseven
withonly5%ofthedataused.ThisdemonstratestherationalityoftheNormDELmethod,asitnotonlyassessesperformance
butalsoeffectivelyutilizesthedatascale.
5%pretrainingdata 10%pretrainingdata 20%pretrainingdata 30%pretrainingdata 50%pretrainingdata 100%pretrainingdata

### Dataset

mIoU NormDEL mIoU NormDEL mIoU NormDEL mIoU NormDEL mIoU NormDEL mIoU NormDEL
Kvasir-Instrument 79.38 68.03 79.52 67.25 80.22 65.85 80.38 64.06 80.48 61.97 79.70 57.28
Kvasir-SEG 75.45 67.21 75.74 66.49 76.37 65.14 76.03 63.33 76.77 61.43 76.02 56.95
ImageCLEFmed 70.95 66.26 71.80 65.69 71.44 64.22 72.58 62.76 71.23 60.64 72.02 56.59
ETIS 47.50 61.11 49.44 61.00 50.20 60.13 50.28 58.94 49.62 57.47 49.13 54.51
PolypGen2021 60.93 64.10 61.61 63.59 61.47 62.32 62.28 61.01 62.20 59.32 60.89 55.58
CVC-300 63.67 64.69 56.69 62.55 61.40 62.31 62.85 61.11 61.97 59.29 61.16 55.60
CVC-ClinicDB 75.24 67.16 74.58 66.26 75.27 64.94 75.50 63.25 75.49 61.25 74.95 56.85
CVC-ColonDB 69.52 65.96 68.58 65.03 69.90 63.93 71.60 62.59 69.72 60.42 69.48 56.36
toachieverelativelydecentresults.However,asthedatavolume ThisalsoreflectsthelimitationsoftheMedDELmethod.These
increases,redundancyininformationalsogrows.Atacertainpoint, fluctuationsmayarisefromdifferencesindatacharacteristics,task
abalanceisreachedbetweeninformationcontentandredundancy, complexities, or other factors. It is precisely this diversity that
culminatinginpeakmodelperformance.Beyondthispoint,further complicatestheoptimizationofdataeffectiveness,requiringinincreasesindatavolumeleadtoadeclineinperformance.This depthresearchandfine-tuning.
trendisreflectedinthelengthoftheboxesintheplot,wherethe Nevertheless,thesefindingsstillunderscoretheeffectivenessof
boxlengthfirstincreaseswiththedatavolume,reachesapeak,and MedDELinreducingstorageburdenandachievinggoodresults
thenstartstoshorten. withsmallerproportionsofdata.Weencouragemoreresearchers
However,intheresultsfromFigure4,thetrendsarenotasstable, toengagewithourstudyandproposemorerefinedmethodsto
andthereisfluctuationobservedinsomeofthedownstreamtasks. makethemostoflimiteddataresources.

<!-- Page 7 -->

AMedicalData-EffectiveLearningBenchmarkforHighlyEfficientPre-trainingofFoundationModels MM’24,October28-November1,2024,Melbourne,VIC,Australia
0.805
0.8
0.795
0.79
0.785
0.78
0.775
0.77
0.765
5% 10% 20% 33% 50% 100% ImageNet
Percentage of Data Used
UoIm
0.77
0.765
0.76
0.755
0.75
0.745
0.74
0.735
0.73
0.725
0.72
5% 10% 20% 33% 50% 100% ImageNet
Percentage of Data Used
(a)Box-plotofKvasir-INS
UoIm
0.73
0.72
0.71
0.7
0.69
0.68
5% 10% 20% 33% 50% 100% ImageNet
Percentage of Data Used
(b)Box-plotofKvasir-SEG
UoIm
0.5
0.48
0.46
0.44
0.42
0.4
5% 10% 20% 33% 50% 100% ImageNet

### Percentage of Data Used

(c)Box-plotofImageCLEFMed

### UoIm

(d)Box-plotofETIS
0.65
0.6
0.55
0.5
0.45
0.4
0.35
5% 10% 20% 33% 50% 100% ImageNet
Percentage of Data Used
UoIm
0.65
0.6
0.55
0.5
0.45
0.4
0.35
5% 10% 20% 33% 50% 100% ImageNet

### Percentage of Data Used

(e)Box-plotofPolyGen2021

### UoIm

0.755
0.75
0.745
0.74
0.735
0.73
5% 10% 20% 33% 50% 100% ImageNet
Percentage of Data Used
(f)Box-plotofCVC-300
UoIm
0.72
0.71
0.7
0.69
0.68
0.67
0.66
0.65
5% 10% 20% 33% 50% 100% ImageNet

### Percentage of Data Used

(g)Box-plotofCVC-ClinicDB

### UoIm

(h)Box-plotofCVC-ColonDB
Figure4:Boxplotofthebaselinemethod(MedDEL)fortestingmIoUunderretainingdifferentdataratios.Underthesame
computationalresources,weplottheimpactofvaryingproportionsofpre-trainingdataondownstreamtaskperformance,
usingthedataproportionsfromTable2andmodelspre-trainedonImageNetforreference.Theresultsdemonstratethatthe
performanceofdownstreamtasksinitiallyimproveswithanincreaseinpre-trainingdatabuteventuallydecreases.Thisis
becausetheinitiallyaddeddataiseffective,however,asmoredataisintroducedbeyondacertainpoint,itincludesredundancy
orerroneousinformation,whichadverselyaffectsthemodel’sperformance.
Table4:Illustratingtheimpactofdifferentpre-trainingtime(epochs)onperformancemetrics(mIoU)using20%and33%of
pretrainingdata.Theresultsindicatethattheoptimalperformanceisoftennotachievedwiththestandardpretrainingduration
(1,000epochsfor20%and600epochsfor33%)butratheroccurswithearlypretrainingtime,demonstratingtheeffectivenessof
MedDELinreducingcomputationalresourceconsumption.

### PretrainingTime 20%pretrainingdata 33%pretrainingdata

Dataset 200 300 400 500 700 800 900 1,000 240 360 420 480 540 600
Kvasir-Instrument 80.21 79.73 79.98 80.01 80.06 80.11 80.22 80.22 80.25 80.50 80.32 80.39 80.41 80.38
Kvasir-SEG 75.80 75.69 76.13 75.90 76.25 76.33 76.39 76.37 75.73 75.94 75.84 76.07 75.78 76.03
ImageCLEFmed 71.44 71.60 71.44 72.91 71.51 71.52 71.84 71.44 72.59 72.32 72.34 72.54 72.19 72.58
ETIS 49.07 49.70 50.88 51.11 50.96 51.13 51.01 50.20 49.54 51.23 51.30 50.28 50.79 50.28
PolypGen2021 61.64 61.32 61.54 61.00 61.47 61.15 61.30 61.47 61.15 61.62 62.10 62.28 62.29 62.28
CVC-300 58.66 57.52 56.81 60.59 61.51 60.78 60.00 61.40 62.09 62.34 64.40 61.40 63.34 62.85
CVC-ClinicDB 74.66 75.56 75.48 75.29 75.11 74.83 75.41 75.27 75.44 75.11 75.24 75.17 75.28 75.50
CVC-ColonDB 69.83 70.17 70.68 69.65 70.62 70.10 69.89 69.90 72.09 71.62 70.89 71.43 71.95 71.60
4.4 ComputingPowerSavingAnalysis performance metrics (mIoU values) across various downstream
Section4.3demonstratesthatMedDELeffectivelyenhancesstorage datasetsatdifferentpretrainingtimes(epochs).
performanceandachievesresultscomparabletolarge-scaledatasets Remarkably,weobservethatoptimalperformanceisnotconsisbyusingfewerdata.Buildinguponthis,wefurtherexplorethe tentlyachievedwithmodelstrainedusing100%ofthepretraining
optimizationofMedDEL’stimeperformance.Table4presentsmod- timeacrossnearlyalldatasets.Instead,wenotethepresenceofa
elstrainedwith20%and33%ofpretrainingdata,usingtheepoch complexuncertaintyandfluctuation,wheretheoptimalresultmay
numbersfromTable2asareference.Weprogressivelydecreasethe bedistributedamongdifferentpretrainingtimepointsindiverse
pretrainingtimein10%increments,aimingtoexploreMedDEL’s datasetsandwithvaryingproportionsofpretrainingdata.ThisunderscorestheeffectivenessofMedDELinconservingcomputational

<!-- Page 8 -->

MM’24,October28-November1,2024,Melbourne,VIC,Australia WenxuanYang,WeiminTan,YuqiSunandBoYan
Figure5:DemonstrationofimagesdeletedbyMedDEL.ThisfigureshowsMedDELdeletingsemanticallysimilarimages,which
appeartohavenosignificantdifferencesbetweenthemfromaperceptualperspective,
/ 0.58 0.56 0.41
0.65 / 0.50 0.34
0.53 0.47 / 0.45
0.51 0.32 0.52 /
Test Dataset
tesataD
niarT

## D0 D0 / 0.58 0.67 0.51


## D1 D1 0.75 / 0.61 0.47


## D2 D2 0.64 0.46 / 0.50


## D3 D3 0.56 0.39 0.52 /


## D0 D1 D2 D3


### Test Dataset


## D0 / 0.60 0.59 0.44


## D1 0.67 / 0.58 0.35


## D2 0.60 0.44 / 0.50


## D3 0.54 0.34 0.53 /

Test Dataset
tesataD
niarT
tesataD
niarT

## D0 / 0.59 0.68 0.51


## D1 0.76 / 0.64 0.48


## D2 0.65 0.49 / 0.50


## D3 0.58 0.42 0.58 /

Test Dataset
tesataD
niarT

## D0 / 0.61 0.69 0.55


## D1 0.76 / 0.65 0.50


## D2 0.67 0.49 / 0.52


## D3 0.60 0.43 0.55 /

Test Dataset
tesataD
niarT

## D0 / 0.61 0.67 0.57


## D1 0.75 / 0.67 0.47


## D2 0.68 0.49 / 0.51


## D3 0.61 0.41 0.56 /


## D0 D1 D2 D3


### Test Dataset

D0 D1 D2 D3 D0 D1 D2 D3 D0 D1 D2 D3
tesataD
niarT
significantportionofredundantdatawithhighlysimilarfeatures
fromthedataset.Consideringtheirsimilarity,wesupposeremoving
suchredundantdataisareasonablestrategytooptimizethedataset
structure,enhancingdatasetquality.Thisoptimizationimproves
D0 D1 D2 D3 themodel’sunderstandingofendoscopicimages,makingitmore
(a) 5% Pretraining data (Random) (b) 5% Pretraining data (MedDEL) (c) 50% Pretraining data (MedDEL) targetedandinterpretable,andprovidingrobustsupportformedical
imageanalysis[16].
4.6 AblationStudy

### Tovalidatetheeffectivenessofourmodel,wesupplementthefol-

(d) 20% Pretraining data (Random) (e) 20% Pretraining data (MedDEL) (f) 100% Pretraining data (All) lowinggeneralizationexperimentsinFig6.Specifically,weselect
D0:Kvasir-SEG D1:ImageCLEFmed D2:CVC-ClinicDB D3:CVC-ColonDB
5%,20%,and50%ofthedataandcomparethetestperformance
Figure6:Modelgeneralizationexperimentsacrossdifferent ofrandomselectionandMedDEL.Wefindthatwhetherusingthe
datasetswithdifferentdatavolumes.Theexperimentsin- randomselectionmethodorMedDEL,astheamountofdataincludedfourdistinctdatasets:Kvasir-SEG,ImageCLEFmed, creases,themodel’sgeneralizationabilityimproves.Furthermore,
CVC-ClinicDB,andCVC-ColonDB.Theresultsindicatethe atthesamedatavolume,MedDELshowssuperiorperformance
performance of the model at different volumes of pre- totherandommethod.Additionally,MedDELshowscomparable
training data (5%, 20%, 50%, and 100%), and compared the generalizationperformancewhenselecting50%datacomparedto
outcomesbetweenrandomlyselecteddataanddataselected usingfulldata.
usingtheMedDELmethod.
5 Conclusion
resources.However,italsosuggeststhatoptimizingpretraining Intheeraoffoundationmodels,wearethefirsttoproposewhether
timemayrequiredifferentstrategiesforvarioustasksanddata largerpre-trainingdatanecessarilyleadstoimprovedmodelpercontexts.Ourstudyhasnotyetuncoveredthespecificrelationships formance.Inordertoinvestigatethisissue,weproposethefirst
betweenthesestrategies,indicatingtheneedformorein-depth medicaldata-effectiveBenchmark,whichinvolvesamillion-level
researchinthefuture. dataset from 31 medical centers (DataDEL), a data-effective approach(MedDEL),andacomprehensivemetricforevaluatingpre-
4.5 VisualizationofMedDEL(DEL) trainingdatavolume(NormDEL).Theestablishmentofanopen
TheMedDELalgorithm,asabenchmarkmethodinthefieldofen- benchmarkfordata-effectivelearningiscrucialforthemedical
doscopic,isbasedontheVisionTransformer(ViT)model[16]for artificialintelligenceresearchcommunity,whichisanencouraging
extractingimagefeatures,generatinga768-dimensionalfeatureout- foundationforsubsequentresearchendeavors.
put.ByintroducingK-meansclustering[42],itsuccessfullyreduces
computationalcomplexityandfurthereffectivelyaddressesirrele-

### Acknowledgement

vantdataintheendoscopicdatasetbysettingsimilaritythresholds
andfilteringconditions. ThisworkwassupportedinpartbyNSFC(No.U2001209,62372117).
Figure5visualizestheresultsoftheMedDEL(DEL)algorithm, ThecomputationsinthisresearchwereperformedusingtheCFFF
whereuponobservation,itisevidentthatMedDELeliminatesa platformofFudanUniversity.

<!-- Page 9 -->

AMedicalData-EffectiveLearningBenchmarkforHighlyEfficientPre-trainingofFoundationModels MM’24,October28-November1,2024,Melbourne,VIC,Australia

### References

[23] OleksandraGulenko,HyunmoYang,KiSikKim,JinYoungYoum,MinjaeKim,
[1] 2023.EndoscopyProceduresEstimatesMarketVolume,Share&TrendsAnalysis YunhoKim,WoonggyuJung,andJoon-MoYang.2022.Deep-Learning-BasedAl-
Report.ReportID:GVR-4-68039-915-0,NumberofPages:118,Format:Electronic gorithmfortheRemovalofElectromagneticInterferenceNoiseinPhotoacoustic
(PDF),HistoricalRange:2016-2021,Industry:Healthcare. SegmentForecasts, EndoscopicImageProcessing.Sensors22,10(2022),3961.
2023-2030. [24] DannyHarnik,OdedMargalit,DalitNaor,DmitrySotnikov,andGilVernik.2012.
[2] AmroAbbas,KushalTirumala,DánielSimig,SuryaGanguli,andAriSMor- Estimationofdeduplicationratiosinlargedatasets.In2012IEEE28thSymposium
cos.2023. SemDeDup:Data-efficientlearningatweb-scalethroughsemantic onMassStorageSystemsandTechnologies(MSST).IEEE,1–11.
deduplication.arXivpreprintarXiv:2303.09540(2023). [25] KaimingHe,XinleiChen,SainingXie,YanghaoLi,PiotrDollár,andRossGirshick.
[3] SharibAli,NohaGhatwary,BarbaraBraden,DominiqueLamarque,AdamBai- 2021.MaskedAutoencodersAreScalableVisionLearners.(2021).
ley,StefanoRealdon,RenatoCannizzaro,JensRittscher,ChristianDaul,and [26] ZhongyuHe,PengWang,YuelongLiang,ZuomingFu,andXuesongYe.2021.
JamesEast.2020.Endoscopydiseasedetectionchallenge2020.arXivpreprint Clinicallyavailableopticalimagingtechnologiesinendoscopiclesiondetection:
arXiv:2003.03376(2020). currentstatusandfutureperspective. JournalofHealthcareEngineering2021
[4] SharibAli,DebeshJha,NohaGhatwary,StefanoRealdon,RenatoCannizzaro, (2021),1–27.
OsamaESalem,DominiqueLamarque,ChristianDaul,MichaelARiegler,KimV [27] WilliamHersh,HenningM¨"uller,andJayashreeKalpathy-Cramer.2009. The
Anonsen,etal.2021.PolypGen:Amulti-centerpolypdetectionandsegmentation ImageCLEFmedmedicalimageretrievaltasktestcollection.JournalofDigital
datasetforgeneralisabilityassessment.arXivpreprintarXiv:2106.04463(2021). Imaging22(2009),648–655.
[5] SharibAli,FelixZhou,ChristianDaul,BarbaraBraden,AdamBailey,Stefano [28] DebeshJha,SharibAli,KristerEmanuelsen,StevenAHicks,VajiraThambawita,
Realdon,JamesEast,GeorgesWagnieres,VictorLoschenov,EnricoGrisan,etal. EnriqueGarcia-Ceja,MichaelARiegler,ThomasdeLange,PeterTSchmidt,

### Endoscopyartifactdetection(EAD2019)challengedataset.arXivpreprint HåvardDJohansen,etal.2021.Kvasir-instrument:Diagnosticandtherapeutic

arXiv:1905.03209(2019). toolsegmentationdatasetingastrointestinalendoscopy.InMultiMediaModeling:
[6] JorgeBernal,FJavierSánchez,GloriaFernández-Esparrach,DeboraGil,Cristina 27thInternationalConference,MMM2021,Prague,CzechRepublic,June22–24,
Rodríguez,andFernandoVilariño.2015.WM-DOVAmapsforaccuratepolyp 2021,Proceedings,PartII27.Springer,218–229.
highlightingincolonoscopy:Validationvs.saliencymapsfromphysicians.Com- [29] DebeshJha,VanshaliSharma,NeethiDasu,NikhilKumarTomar,StevenHicks,
puterizedmedicalimagingandgraphics43(2015),99–111. MKBhuyan,PradipKDas,MichaelARiegler,PålHalvorsen,UlasBagci,etal.
[7] JorgeBernal,JavierSánchez,andFernandoVilarino.2012.Towardsautomatic 2023.GastroVision:AMulti-classEndoscopyImageDatasetforComputerAided
polypdetectionwithapolypappearancemodel.PatternRecognition45,9(2012), GastrointestinalDiseaseDetection.InWorkshoponMachineLearningforMulti-
3166–3182. modalHealthcareData.Springer,125–140.
[8] HannaBorgli,VajiraThambawita,PiaHSmedsrud,StevenHicks,DebeshJha, [30] DebeshJha,PiaHSmedsrud,DagJohansen,ThomasdeLange,HåvardDJo-
SigrunLEskeland,KristinRanheimRandel,KonstantinPogorelov,MathiasLux, hansen,PålHalvorsen,andMichaelARiegler.2021.Acomprehensivestudyon
DucTienDangNguyen,etal.2020.HyperKvasir,acomprehensivemulti-class colorectalpolypsegmentationwithResUNet++,conditionalrandomfieldand
imageandvideodatasetforgastrointestinalendoscopy.Scientificdata7,1(2020), test-timeaugmentation.IEEEjournalofbiomedicalandhealthinformatics25,6
283. (2021),2029–2040.
[9] MingChen,ShupengWang,andLiangTian.2013.AHigh-precisionDuplicate [31] DebeshJha,PiaHSmedsrud,MichaelARiegler,PålHalvorsen,Thomasde
ImageDeduplicationApproach.J.Comput.8,11(2013),2768–2775. Lange,DagJohansen,andHåvardDJohansen.2020.Kvasir-seg:Asegmented
[10] MingChen,YangWang,XiaoxiangZou,ShupengWang,andGuangjunWu.2012. polypdataset.InMultiMediaModeling:26thInternationalConference,MMM2020,
AduplicateimagededuplicationapproachviaHaarwavelettechnology.In2012 Daejeon,SouthKorea,January5–8,2020,Proceedings,PartII26.Springer,451–462.
IEEE2ndInternationalConferenceonCloudComputingandIntelligenceSystems, [32] LuisOJimenez-Rodriguez,EmmanuelArzuaga-Cruz,andMiguelVélez-Reyes.
Vol.2.IEEE,624–628. 2007. Unsupervisedlinearfeature-extractionmethodsandtheireffectsinthe
[11] Xue-WenChenandXiaotongLin.2014.Bigdatadeeplearning:challengesand classificationofhigh-dimensionaldata. IEEETransactionsongeoscienceand
perspectives.IEEEaccess2(2014),514–525. remotesensing45,2(2007),469–483.
[12] NeilTClancy,RuiLi,KevinRogers,PaulDriscoll,PeterExcel,RonYandle,George [33] JiwonKim,JungKwonLee,andKyoungMuLee.2016.Accurateimagesuper-
Hanna,NigelCopner,andDanielSElson.2012. Developmentandevaluation resolutionusingverydeepconvolutionalnetworks.InProceedingsoftheIEEE
ofalight-emittingdiodeendoscopiclightsource.InAdvancedBiomedicaland conferenceoncomputervisionandpatternrecognition.1646–1654.
ClinicalDiagnosticSystemsX,Vol.8214.SPIE,105–111. [34] AlexKrizhevsky,GeoffreyHinton,etal.2009.Learningmultiplelayersoffeatures
[13] NelsonCowan.2001.Metatheoryofstoragecapacitylimits.Behavioralandbrain fromtinyimages.(2009).
sciences24,1(2001),154–176. [35] RafalKwasny,DanielFriar,andGiuseppePapallo.2020. BenchmarkingDeep
[14] SagnikDakshit,BarbaraMukamiMaweu,SristiDakshit,andBalakrishnanPrab- LearningWorkloadswithTensorFlowontheNVIDIAGeForceRTX3090.
hakaran.2022. Core-setselectionusingmetrics-basedexplanations(CSUME) [36] ChengcaiLeng,HaiZhang,BoLi,GuorongCai,ZhaoPei,andLiHe.2018.Local
formulticlassECG.In2022IEEE10thInternationalConferenceonHealthcare featuredescriptorforimagematching:Asurvey.IEEEAccess7(2018),6424–6434.
Informatics(ICHI).IEEE,217–225. [37] MengfangLi,YuanyuanJiang,YanzhouZhang,andHaishengZhu.2023.Medical
[15] JiaDeng,WeiDong,RichardSocher,Li-JiaLi,KaiLi,andLiFei-Fei.2009.Imagenet: imageanalysisusingdeeplearningalgorithms. FrontiersinPublicHealth11
Alarge-scalehierarchicalimagedatabase.In2009IEEEconferenceoncomputer (2023),1273253.
visionandpatternrecognition.Ieee,248–255. [38] XuanLi,LiqiongChang,andXueLiu.2021.CE-Dedup:Cost-effectiveconvolu-
[16] AlexeyDosovitskiy,LucasBeyer,AlexanderKolesnikov,DirkWeissenborn,Xi- tionalneuralnetstrainingbasedonimagededuplication.In2021IEEEIntlConf
aohuaZhai,ThomasUnterthiner,MostafaDehghani,MatthiasMinderer,Georg onParallel&DistributedProcessingwithApplications,BigData&CloudComput-
Heigold,SylvainGelly,etal.2020.Animageisworth16x16words:Transformers ing,SustainableComputing&Communications,SocialComputing&Networking
forimagerecognitionatscale.arXivpreprintarXiv:2010.11929(2020). (ISPA/BDCloud/SocialCom/SustainCom).IEEE,11–18.
[17] RichardDosselmannandXueDongYang.2011.Acomprehensiveassessment [39] ZewenLi,FanLiu,WenjieYang,ShouhengPeng,andJunZhou.2022.ASurvey
ofthestructuralsimilarityindex. Signal,ImageandVideoProcessing5(2011), ofConvolutionalNeuralNetworks:Analysis,Applications,andProspects.IEEE
81–91. TransactionsonNeuralNetworksandLearningSystems33,12(2022),6999–7019.
[18] WayneWEckerson.2002.Dataqualityandthebottomline.TDWIReport,The https://doi.org/10.1109/TNNLS.2021.3084827
DataWarehouseInstitute(2002),1–32. [40] HaomiaoLiu,RuipingWang,ShiguangShan,andXilinChen.2016.Deepsuper-
[19] DumitruErhan,AaronCourville,YoshuaBengio,andPascalVincent.2010.Why visedhashingforfastimageretrieval.InProceedingsoftheIEEEconferenceon
doesunsupervisedpre-traininghelpdeeplearning?.InProceedingsofthethir- computervisionandpatternrecognition.2064–2072.
teenthinternationalconferenceonartificialintelligenceandstatistics.JMLRWork- [41] IlyaLoshchilovandFrankHutter.2017.DecoupledWeightDecayRegularization.
shopandConferenceProceedings,201–208. (2017).
[20] ReubenFeinman,RyanRCurtin,SaurabhShintre,andAndrewBGardner.2017. [42] J.Macqueen.1967.Somemethodsforclassificationandanalysisofmultivariate
Detectingadversarialsamplesfromartifacts. arXivpreprintarXiv:1703.00410 observations.Proc.Symp.Math.Statist.andProbability,5th1(1967).
(2017). [43] StephaneGMallat.1989. Atheoryformultiresolutionsignaldecomposition:
[21] PedroFurtadoandHenriqueMadeira.1999.Analysisofaccuracyofdatareduction thewaveletrepresentation.IEEEtransactionsonpatternanalysisandmachine
techniques.InDataWarehousingandKnowledgeDiscovery:FirstInternational intelligence11,7(1989),674–693.
Conference,DaWaK’99Florence,Italy,August30–September1,1999Proceedings1. [44] DutchTMeyerandWilliamJBolosky.2012.Astudyofpracticaldeduplication.
Springer,377–388. ACMTransactionsonStorage(ToS)7,4(2012),1–20.
[22] AkhileshGotmare,NitishShirishKeskar,CaimingXiong,andRichardSocher. [45] HussainNyeem,WageehBoles,andColinBoyd.2013. Areviewofmedical

## Acloserlookatdeeplearningheuristics:Learningraterestarts,warmup imagewatermarkingrequirementsforteleradiology.Journalofdigitalimaging

anddistillation.arXivpreprintarXiv:1810.13243(2018). 26(2013),326–343.

<!-- Page 10 -->

MM’24,October28-November1,2024,Melbourne,VIC,Australia WenxuanYang,WeiminTan,YuqiSunandBoYan
[46] JKPeriasamyandBLatha.2021. Efficienthashfunction–basedduplication InternationalJournalofDevelopmentalBiology39,1(2003),153–161.
detectionalgorithmfordataDeduplicationdeductionandreduction.Concurrency [54] IlyaTolstikhin,NeilHoulsby,AlexanderKolesnikov,LucasBeyer,andAlexey
andComputation:PracticeandExperience33,3(2021),e5213. Dosovitskiy.2021.MLP-Mixer:Anall-MLPArchitectureforVision.(2021).
[47] MMostafizurRahmanandDarrylNDavis.2013.Addressingtheclassimbalance [55] DavidVázquez,JorgeBernal,FJavierSánchez,GloriaFernández-Esparrach,
probleminmedicaldatasets. InternationalJournalofMachineLearningand AntonioMLópez,AdrianaRomero,MichalDrozdzal,AaronCourville,etal.
Computing3,2(2013),224. 2017.Abenchmarkforendoluminalscenesegmentationofcolonoscopyimages.
[48] PapiaRay,SSurenderReddy,andTuhinaBanerjee.2021. Variousdimension Journalofhealthcareengineering2017(2017).
reductiontechniquesforhighdimensionaldataanalysis:areview. Artificial [56] TianluWang,JieyuZhao,MarkYatskar,Kai-WeiChang,andVicenteOrdonez.
IntelligenceReview54,5(2021),3473–3515. 2019. Balanceddatasetsarenotenough:Estimatingandmitigatinggender
[49] OlgaRussakovsky,JiaDeng,HaoSu,JonathanKrause,SanjeevSatheesh,Sean biasindeepimagerepresentations.InProceedingsoftheIEEE/CVFinternational
Ma,ZhihengHuang,AndrejKarpathy,AdityaKhosla,MichaelBernstein,etal. conferenceoncomputervision.5310–5319.

### Imagenetlargescalevisualrecognitionchallenge.Internationaljournalof [57] WenXia,HongJiang,DanFeng,FredDouglis,PhilipShilane,YuHua,MinFu,

computervision115(2015),211–252. YuchengZhang,andYukunZhou.2016. Acomprehensivestudyofthepast,
[50] PrakashChandraSharma,SulabhBansal,RohitRaja,PhyuMyoThwe,MoeMoe present,andfutureofdatadeduplication.Proc.IEEE104,9(2016),1681–1710.
Htay,andSuSuHlaing.2021. Concepts,strategies,andchallengesofdata [58] LingXiao,BeijiZou,ChengzhangZhu,andFanboNie.2023. ESDedup:An
deduplication.InDataDeduplicationApproaches.Elsevier,37–55. efficientandsecurededuplicationschemebasedondatasimilarityandblockchain
[51] JuanSilva,AymericHistace,OlivierRomain,XavierDray,andBertrandGranado. forcloud-assistedmedicalstoragesystems.TheJournalofSupercomputing79,3

## Towardembeddeddetectionofpolypsinwceimagesforearlydiagnosisof (2023),2932–2960.

colorectalcancer.Internationaljournalofcomputerassistedradiologyandsurgery [59] HengxiangXie,YuhuiDeng,HaoFeng,andLeiSi.2021.Pxdedup:Deduplicating
9(2014),283–293. massivevisuallyidenticaljpegimagedata.BigDataResearch23(2021),100171.
[52] PiaHSmedsrud,VajiraThambawita,StevenAHicks,HenrikGjestang,OdaOlsen [60] MartinJYaffe.2019. Emergenceof“bigdata”anditspotentialandcurrent
Nedrejord,EspenNæss,HannaBorgli,DebeshJha,TorJanDerekBerstad, limitationsinmedicalimaging.InSeminarsinNuclearMedicine,Vol.49.Elsevier,
SigrunLEskeland,etal.2021.Kvasir-Capsule,avideocapsuleendoscopydataset. 94–104.
ScientificData8,1(2021),142. [61] XiangyuZou,JingsongYuan,PhilipShilane,WenXia,HaijunZhang,andXuan
[53] CHARLESESmithandANTONIONanci.2003. Overviewofmorphological Wang.2022.FromHyper-DimensionalStructurestoLinearStructures:Maintainchangesinenamelorgancellsassociatedwithmajoreventsinamelogenesis. ingDeduplicatedData’sLocality.18,3(2022).

## Tables

**Table (Page 1):**

| 5% data 70.95% |  | m≈IoU | 100% data 72.02% |  |
|---|---|---|---|---|
|  | 𝑳𝑬𝑫𝒎𝒓𝒐𝑵 |  |  | 𝑳𝑬𝑫𝒎𝒓𝒐𝑵 |


**Table (Page 6):**

|  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  | CVC | 300 |


**Table (Page 6):**

|  |  |  |  |  |  |
|---|---|---|---|---|---|
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  | CV | C-ClinicDB |


**Table (Page 6):**

|  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  | CVC-C 5% | olonDB data |


**Table (Page 6):**

|  |  |  |  |  |  |
|---|---|---|---|---|---|
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  | ETIS 5% data |


**Table (Page 6):**

|  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  | I | mageCL 5% 100 | EFMed data % data |


**Table (Page 6):**

|  |  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  | Kv | asir-Inst 5% 100 | rument data % data |


**Table (Page 6):**

|  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  | PolyGe 5% 10 | n2021 data 0% data |


**Table (Page 6):**

|  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  | Kvasir 5% 10 | -SEG data 0% data |


**Table (Page 6):**

| Dataset | 5%pretrainingdata |  | 10%pretrainingdata |  | 20%pretrainingdata |  | 30%pretrainingdata |  | 50%pretrainingdata |  | 100%pretrainingdata |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | mIoU | NormDEL | mIoU | NormDEL | mIoU | NormDEL | mIoU | NormDEL | mIoU | NormDEL | mIoU | NormDEL |
| Kvasir-Instrument | 79.38 | 68.03 | 79.52 | 67.25 | 80.22 | 65.85 | 80.38 | 64.06 | 80.48 | 61.97 | 79.70 | 57.28 |
| Kvasir-SEG | 75.45 | 67.21 | 75.74 | 66.49 | 76.37 | 65.14 | 76.03 | 63.33 | 76.77 | 61.43 | 76.02 | 56.95 |
| ImageCLEFmed | 70.95 | 66.26 | 71.80 | 65.69 | 71.44 | 64.22 | 72.58 | 62.76 | 71.23 | 60.64 | 72.02 | 56.59 |
| ETIS | 47.50 | 61.11 | 49.44 | 61.00 | 50.20 | 60.13 | 50.28 | 58.94 | 49.62 | 57.47 | 49.13 | 54.51 |
| PolypGen2021 | 60.93 | 64.10 | 61.61 | 63.59 | 61.47 | 62.32 | 62.28 | 61.01 | 62.20 | 59.32 | 60.89 | 55.58 |
| CVC-300 | 63.67 | 64.69 | 56.69 | 62.55 | 61.40 | 62.31 | 62.85 | 61.11 | 61.97 | 59.29 | 61.16 | 55.60 |
| CVC-ClinicDB | 75.24 | 67.16 | 74.58 | 66.26 | 75.27 | 64.94 | 75.50 | 63.25 | 75.49 | 61.25 | 74.95 | 56.85 |
| CVC-ColonDB | 69.52 | 65.96 | 68.58 | 65.03 | 69.90 | 63.93 | 71.60 | 62.59 | 69.72 | 60.42 | 69.48 | 56.36 |


**Table (Page 7):**

|  |  |  |  |  |  |  | 0.65 0.6 0.55 0.5 UoIm 0.45 0.4 0.35 et 5 |  |  |  |  |  |  |  | 0.755 0.75 0.745 UoIm 0.74 0.735 0.73 5% 10% 20% 33% 50% 100% Imag Percentage of Data Used |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  | % 10% 20% 33% 50% 100% ImageNet Percentage of Data Used |  |  |  |  |  |  |  |  |  |  |  |  |  |


**Table (Page 7):**

|  |  |  |  |  |  |
|---|---|---|---|---|---|
|  |  |  |  |  |  |


**Table (Page 7):**

| PretrainingTime Dataset | 20%pretrainingdata 200 300 400 500 700 800 900 1,000 |  |  |  |  |  |  |  | 33%pretrainingdata |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  | 300 | 400 | 500 | 700 | 800 | 900 | 1,000 | 240 | 360 | 420 | 480 | 540 | 600 |
| Kvasir-Instrument | 80.21 | 79.73 | 79.98 | 80.01 | 80.06 | 80.11 | 80.22 | 80.22 | 80.25 | 80.50 | 80.32 | 80.39 | 80.41 | 80.38 |
| Kvasir-SEG | 75.80 | 75.69 | 76.13 | 75.90 | 76.25 | 76.33 | 76.39 | 76.37 | 75.73 | 75.94 | 75.84 | 76.07 | 75.78 | 76.03 |
| ImageCLEFmed | 71.44 | 71.60 | 71.44 | 72.91 | 71.51 | 71.52 | 71.84 | 71.44 | 72.59 | 72.32 | 72.34 | 72.54 | 72.19 | 72.58 |
| ETIS | 49.07 | 49.70 | 50.88 | 51.11 | 50.96 | 51.13 | 51.01 | 50.20 | 49.54 | 51.23 | 51.30 | 50.28 | 50.79 | 50.28 |
| PolypGen2021 | 61.64 | 61.32 | 61.54 | 61.00 | 61.47 | 61.15 | 61.30 | 61.47 | 61.15 | 61.62 | 62.10 | 62.28 | 62.29 | 62.28 |
| CVC-300 | 58.66 | 57.52 | 56.81 | 60.59 | 61.51 | 60.78 | 60.00 | 61.40 | 62.09 | 62.34 | 64.40 | 61.40 | 63.34 | 62.85 |
| CVC-ClinicDB | 74.66 | 75.56 | 75.48 | 75.29 | 75.11 | 74.83 | 75.41 | 75.27 | 75.44 | 75.11 | 75.24 | 75.17 | 75.28 | 75.50 |
| CVC-ColonDB | 69.83 | 70.17 | 70.68 | 69.65 | 70.62 | 70.10 | 69.89 | 69.90 | 72.09 | 71.62 | 70.89 | 71.43 | 71.95 | 71.60 |


**Table (Page 8):**

|  |  |  |  |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |


**Table (Page 8):**

|  |  |  |  |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |


**Table (Page 8):**

| / | 0.58 | 0.56 | 0.41 |
|---|---|---|---|
| 0.65 | / | 0.50 | 0.34 |
| 0.53 | 0.47 | / | 0.45 |
| 0.51 | 0.32 | 0.52 | / |


**Table (Page 8):**

| / | 0.58 | 0.67 | 0.51 |
|---|---|---|---|
| 0.75 | / | 0.61 | 0.47 |
| 0.64 | 0.46 | / | 0.50 |
| 0.56 | 0.39 | 0.52 | / |


**Table (Page 8):**

| / | 0.61 | 0.67 | 0.57 |
|---|---|---|---|
| 0.75 | / | 0.67 | 0.47 |
| 0.68 | 0.49 | / | 0.51 |
| 0.61 | 0.41 | 0.56 | / |


**Table (Page 8):**

| / | 0.60 | 0.59 | 0.44 |
|---|---|---|---|
| 0.67 | / | 0.58 | 0.35 |
| 0.60 | 0.44 | / | 0.50 |
| 0.54 | 0.34 | 0.53 | / |


**Table (Page 8):**

| / | 0.59 | 0.68 | 0.51 |
|---|---|---|---|
| 0.76 | / | 0.64 | 0.48 |
| 0.65 | 0.49 | / | 0.50 |
| 0.58 | 0.42 | 0.58 | / |


**Table (Page 8):**

| / | 0.61 | 0.69 | 0.55 |
|---|---|---|---|
| 0.76 | / | 0.65 | 0.50 |
| 0.67 | 0.49 | / | 0.52 |
| 0.60 | 0.43 | 0.55 | / |
