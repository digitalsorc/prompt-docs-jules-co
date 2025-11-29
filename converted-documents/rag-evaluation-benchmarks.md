---
title: "RAG Evaluation Benchmarks"
original_file: "./RAG_Evaluation_Benchmarks.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["prompt-engineering", "llm", "rag", "chain-of-thought", "agents"]
keywords: ["arxiv", "org", "https", "abs", "graph", "retrieval", "vol", "acm", "page", "publicationdate"]
summary: "<!-- Page 1 -->

Graph Retrieval-Augmented Generation: A Survey

## Bocipeng∗,

SchoolofIntelligenceScienceandTechnology,PekingUniversity,China

## Yunzhu∗,

CollegeofComputerScienceandTechnology,ZhejiangUniversity,China

## Yongchaoliu,

AntGroup,China

## Xiaohebo,

GaolingSchoolofArtificialIntelligence,RenminUniversityofChina,China

## Haizhoushi,

RutgersUniversity,US

## Chuntaohong,

AntGroup,China

## Yanzhang†,

SchoolofIntelligenceScienceandTechnology,PekingUniversity,China

## Siliangt"
related_documents: []
---

# RAG Evaluation Benchmarks

<!-- Page 1 -->

Graph Retrieval-Augmented Generation: A Survey

## Bocipeng∗,

SchoolofIntelligenceScienceandTechnology,PekingUniversity,China

## Yunzhu∗,

CollegeofComputerScienceandTechnology,ZhejiangUniversity,China

## Yongchaoliu,

AntGroup,China

## Xiaohebo,

GaolingSchoolofArtificialIntelligence,RenminUniversityofChina,China

## Haizhoushi,

RutgersUniversity,US

## Chuntaohong,

AntGroup,China

## Yanzhang†,

SchoolofIntelligenceScienceandTechnology,PekingUniversity,China

## Siliangtang,

CollegeofComputerScienceandTechnology,ZhejiangUniversity,China
Recently,Retrieval-AugmentedGeneration(RAG)hasachievedremarkablesuccessinaddressingthechallenges
ofLargeLanguageModels(LLMs)withoutnecessitatingretraining.Byreferencinganexternalknowledge
base,RAGrefinesLLMoutputs,effectivelymitigatingissuessuchas“hallucination”,lackofdomain-specific
knowledge,andoutdatedinformation.However,thecomplexstructureofrelationshipsamongdifferent
entities in databases presents challenges for RAG systems. In response, GraphRAG leverages structural
informationacrossentitiestoenablemorepreciseandcomprehensiveretrieval,capturingrelationalknowledge
and facilitating more accurate, context-aware responses. Given the novelty and potential of GraphRAG,
a systematic review of current technologies is imperative. This paper provides the first comprehensive
overviewofGraphRAGmethodologies.WeformalizetheGraphRAGworkflow,encompassingGraph-Based
Indexing,Graph-GuidedRetrieval,andGraph-EnhancedGeneration.Wethenoutlinethecoretechnologiesand
trainingmethodsateachstage.Additionally,weexaminedownstreamtasks,applicationdomains,evaluation
methodologies,andindustrialusecasesofGraphRAG.Finally,weexplorefutureresearchdirectionstoinspire
furtherinquiriesandadvanceprogressinthefield.Inordertotrackrecentprogressinthisfield,wesetupa
repositoryathttps://github.com/pengboci/GraphRAG-Survey.
CCSConcepts:•Computingmethodologies→Knowledgerepresentationandreasoning;•Informationsystems→Informationretrieval;Datamining.
AdditionalKeyWordsandPhrases:LargeLanguageModels,GraphRetrieval-AugmentedGeneration,KnowledgeGraphs,GraphNeuralNetworks
∗Bothauthorscontributedequallytothisresearch.
†CorrespondingAuthor.
Authors’ContactInformation:BociPeng,SchoolofIntelligenceScienceandTechnology,PekingUniversity,Beijing,China,
bcpeng@stu.pku.edu.cn;YunZhu,CollegeofComputerScienceandTechnology,ZhejiangUniversity,Hangzhou,China,
zhuyun_dcd@zju.edu.cn;YongchaoLiu,AntGroup,Hangzhou,China,yongchao.ly@antgroup.com;XiaoheBo,Gaoling
SchoolofArtificialIntelligence,RenminUniversityofChina,Beijing,China,bellebxh@gmail.com;HaizhouShi,Rutgers
University,NewBrunswick,NewJersey,US,haizhou.shi@rutgers.edu;ChuntaoHong,AntGroup,Hangzhou,China,
chuntao.hct@antgroup.com;YanZhang,SchoolofIntelligenceScienceandTechnology,PekingUniversity,Beijing,China,
zhyzhy001@pku.edu.cn;SiliangTang,CollegeofComputerScienceandTechnology,ZhejiangUniversity,Hangzhou,China,
siliang@zju.edu.cn.
Permissiontomakedigitalorhardcopiesofallorpartofthisworkforpersonalorclassroomuseisgrantedwithoutfee
providedthatcopiesarenotmadeordistributedforprofitorcommercialadvantageandthatcopiesbearthisnoticeandthe
fullcitationonthefirstpage.Copyrightsforcomponentsofthisworkownedbyothersthantheauthor(s)mustbehonored.
Abstractingwithcreditispermitted.Tocopyotherwise,orrepublish,topostonserversortoredistributetolists,requires
priorspecificpermissionand/orafee.Requestpermissionsfrompermissions@acm.org.
©2024Copyrightheldbytheowner/author(s).PublicationrightslicensedtoACM.

## Acm1557-735X/2024/9-Art111

https://doi.org/XXXXXXX.XXXXXXX
J.ACM,Vol.37,No.4,Article111.Publicationdate:September2024.
4202
peS
01
]IA.sc[
2v12980.8042:viXra

<!-- Page 2 -->

111:2 Pengetal.

### ACMReferenceFormat:

BociPeng,YunZhu,YongchaoLiu,XiaoheBo,HaizhouShi,ChuntaoHong,YanZhang,andSiliangTang.

#### GraphRetrieval-AugmentedGeneration:ASurvey.J.ACM37,4,Article111(September2024),41pages.

https://doi.org/XXXXXXX.XXXXXXX
1 Introduction
ThedevelopmentofLargeLanguageModelslikeGPT-4[127],Qwen2[184],andLLaMA[31]has
sparkedarevolutioninthefieldofartificialintelligence,fundamentallyalteringthelandscapeof
naturallanguageprocessing.Thesemodels,builtonTransformer[161]architecturesandtrained
ondiverseandextensivedatasets,havedemonstratedunprecedentedcapabilitiesinunderstanding,
interpreting, and generating human language. The impact of these advancements is profound,
stretchingacrossvarioussectorsincludinghealthcare[103,166,203],finance[93,125],andeducation[46,169],wheretheyfacilitatemorenuancedandefficientinteractionsbetweenhumansand
machines.
Despitetheirremarkablelanguagecomprehensionandtextgenerationcapabilities,LLMsmay
exhibitlimitationsduetoalackofdomain-specificknowledge,real-timeupdatedinformation,
andproprietaryknowledge,whichareoutsideLLMs’pre-trainingcorpus.Thesegapscanlead
toaphenomenonknownas“hallucination”[61]wherethemodelgeneratesinaccurateoreven
fabricatedinformation.Consequently,itisimperativetosupplementLLMswithexternalknowledge
to mitigate this problem. Retrieval-Augmented Generation (RAG) [34, 45, 59, 62, 178, 195, 202]
emergedasasignificantevolution,whichaimstoenhancethequalityandrelevanceofgenerated
contentbyintegratingaretrievalcomponentwithinthegenerationprocess.TheessenceofRAG
liesinitsabilitytodynamicallyqueryalargetextcorpustoincorporaterelevantfactualknowledge
intotheresponsesgeneratedbytheunderlyinglanguagemodels.Thisintegrationnotonlyenriches
thecontextualdepthoftheresponsesbutalsoensuresahigherdegreeoffactualaccuracyand
specificity.RAGhasgainedwidespreadattentionduetoitsexceptionalperformanceandbroad
applications,becomingakeyfocuswithinthefield.
Although RAG has achieved impressive results and has been widely applied across various
domains,itfaceslimitationsinreal-worldscenarios:(1)NeglectingRelationships:Inpractice,textual
contentisnotisolatedbutinterconnected.TraditionalRAGfailstocapturesignificantstructured
relationalknowledgethatcannotberepresentedthroughsemanticsimilarityalone.Forinstance,in
acitationnetworkwherepapersarelinkedbycitationrelationships,traditionalRAGmethodsfocus
onfindingtherelevantpapersbasedonthequerybutoverlookimportantcitationrelationships
betweenpapers.(2)RedundantInformation:RAGoftenrecountscontentintheformoftextual
snippetswhenconcatenatedasprompts.Thismakescontextbecomeexcessivelylengthy,leading
tothe“lostinthemiddle”dilemma[104].(3)LackingGlobalInformation:RAGcanonlyretrievea
subsetofdocumentsandfailstograspglobalinformationcomprehensively,andhencestruggles
withtaskssuchasQuery-FocusedSummarization(QFS).
Graph Retrieval-Augmented Generation (GraphRAG) [32, 58, 119] emerges as an innovative
solutiontoaddressthesechallenges.UnliketraditionalRAG,GraphRAGretrievesgraphelements
containingrelationalknowledgepertinenttoagivenqueryfromapre-constructedgraphdatabase,
asdepictedinFigure1.Theseelementsmayincludenodes,triples,paths,orsubgraphs,whichare
utilizedtogenerateresponses.GraphRAGconsiderstheinterconnectionsbetweentexts,enablinga
moreaccurateandcomprehensiveretrievalofrelationalinformation.Additionally,graphdata,such
asknowledgegraphs,offerabstractionandsummarizationoftextualdata,therebysignificantly
shorteningthelengthoftheinputtextandmitigatingconcernsofverbosity.Byretrievingsubgraphs
orgraphcommunities,wecanaccesscomprehensiveinformationtoeffectivelyaddresstheQFS
challengebycapturingthebroadercontextandinterconnectionswithinthegraphstructure.
J.ACM,Vol.37,No.4,Article111.Publicationdate:September2024.

<!-- Page 3 -->

GraphRetrieval-AugmentedGeneration:ASurvey 111:3

### Query Query Query

How did the artistic movements How did the artistic movements How did the artistic movements
of the 19th century impact the of the 19th century impact the of the 19th century impact the
d th e e v e 2 l 0 o t p h m c e e n n t t u o r f y m ? odern art in d th e e v e 2 l 0 o t p h m c e e n n t t u o r f y m ? odern art in Retriever d th e e v e 2 l 0 o t p h m c e e n n t t u o r f y m ? odern art in Retriever

## Impressionist artists like -(Claude Monet) - [introduced] →


### Claude Monet introduced new (new techniques)

techniques that revolutionized -(new techniques)–
the depiction of light and color. [revolutionized] → (depiction of

## TheImpressionist techniques light and color)

LLMs LLMs i 3 n . f P lu a e b n lo ce P d i c l a a s te so r a p r i t o n m e o e v r e e m d ents. LLMs - [i ( n Im flu p e r n e c s e s d io ] n → ist ( t la ec te h r n a iq r u t es) -

### Cubism, which radically movements)

transformed the approach to - (Pablo Picasso) - [pioneered] →
visual representation. (Cubism)

## Cubism emerged in the early - (Cubism) - [emerged in] → (early

Response 20th century and challenged 20th century)
traditional perspectives on art.
… …

### The artistic movements of

the 19th century influenced Retrieved Text Retrieved Triplets
modern art in the 20th
century by encouraging Response Response
experimentation with color,
form, and subject matter. Impressionist artists like Claude Monet in the 19th Monet introduced new techniques that revolutionized
These movements paved century introduced new techniques that influence the depiction of light and color. His Impressionist
the way for abstraction, later art movements. Pablo Picasso pioneered techniques influenced later art movements, including
expressionism, and other Cubism relativity in the early 20th century. Picasso's Cubism, which emerged in the early 20th
innovative. century. This influence helped shape Picasso’s
innovative approach to fragmented perspectives.
Fig.1. ComparisionbetweenDirectLLM,RAG,andGraphRAG.Givenauserquery,directansweringby
LLMsmaysufferfromshallowresponsesorlackofspecificity.RAGaddressesthisbyretrievingrelevant
textualinformation,somewhatalleviatingtheissue.However,duetothetext’slengthandflexiblenatural
languageexpressionsofentityrelationships,RAGstrugglestoemphasize“influence”relations,whichisthe
coreofthequestion.While,GraphRAGmethodsleverageexplicitentityandrelationshiprepresentationsin
graphdata,enablingpreciseanswersbyretrievingrelevantstructuredinformation.
In this paper, we are the first to provide a systematic survey of GraphRAG. Specifically, we
beginbyintroducingtheGraphRAGworkflow,alongwiththefoundationalbackgroundknowledge
thatunderpinsthefield.Then,wecategorizetheliteratureaccordingtotheprimarystagesofthe
GraphRAGprocess:Graph-BasedIndexing(G-Indexing),Graph-GuidedRetrieval(G-Retrieval),
andGraph-EnhancedGeneration(G-Generation)inSection5,Section6andSection7respectively,
detailingthecoretechnologiesandtrainingmethodswithineachphase.Furthermore,weinvestigate
downstream tasks, application domains, evaluation methodologies, and industrial use cases of
GraphRAG.ThisexplorationelucidateshowGraphRAGisbeingutilizedinpracticalsettingsand
reflectsitsversatilityandadaptabilityacrossvarioussectors.Finally,acknowledgingthatresearch
inGraphRAGisstillinitsearlystages,wedelveintopotentialfutureresearchdirections.This
prognosticdiscussionaimstopavethewayforforthcomingstudies,inspirenewlinesofinquiry,
andcatalyzeprogresswithinthefield,ultimatelypropellingGraphRAGtowardmorematureand
innovativehorizons.

### Ourcontributionscanbesummarizedasfollows:

• Weprovideacomprehensiveandsystematicreviewofexistingstate-of-the-artGraphRAG
methodologies.WeofferaformaldefinitionofGraphRAG,outliningitsuniversalworkflow
whichincludesG-Indexing,G-Retrieval,andG-Generation.
• WediscussthecoretechnologiesunderpinningexistingGraphRAGsystems,includingG-
Indexing,G-Retrieval,andG-Generation.Foreachcomponent,weanalyzethespectrumof
modelselection,methodologicaldesign,andenhancementstrategiescurrentlybeingexplored.
Additionally,wecontrastthediversetrainingmethodologiesemployedacrossthesemodules.
• Wedelineatethedownstreamtasks,benchmarks,applicationdomains,evaluationmetrics,
currentchallenges,andfutureresearchdirectionspertinenttoGraphRAG,discussingboth
J.ACM,Vol.37,No.4,Article111.Publicationdate:September2024.

<!-- Page 4 -->

111:4 Pengetal.

### InputQuery

How did the artistic movements of the 19th century impact the development of modern art in the 20th century?
G-Retrieval Retrieval GraphFormat G-Generation Output
Results Response
…
E Q D n

## O

u e G h e
p
c a r Q
e
o r y n Q
n
a m u c

## G

E u e p x e

## K

p e
r
p r o m
a
h
n
r y a y s
p o
e n i
h
t D
w
n s i
s
o i t
l
o a
e
s n n
d
ta
ge
ba re v e irte R se&

## S


## G

e

## E

G l
-
f
n
-

## K I

r C
n h
a
M n P a
o p
d r o e n
n
u
h
w e r c n
s
g

## D

l e x
t
i e i n
r
n m
a u
d i g g n
t
g
c
e
a t
e g n
e
t
d
s

### Su H


## T N P

b
r
y
o
g
a i … p
b
d
r
t … l
r
h
a
e e
id
s
p
s ts
hs
Adj N a

## G


## C


## N

a c o
r
t S e
o a
u d n
d
y
p
r e c a n
e h
- y t l L a

## S

/

## E

L i E k x
e
a
m
e d
q
T n g
b u
g r F e
e
e
e
u o e
d n
a T r
d
m
c
a g
i e
b
n
e s l
g
e P E M E

## P E

n r n i
n o
e d h h
s h
- - a a G
t

## G

a -
n n
n G
e e c c
c
n n
e
e e
e
e e
n
m m
m
r r
e
a a e e
r e
t t
a
n n i
n
i o o
t
t t
t i
s s n n
o s n

## G G


## G

e e
e
n n
n
e e
e
r r
r
a a
a
t t
t
o o
o
r r
r
ta h t s e u q in h c e t w e n d e c u
d o rtn i te n o M
d n a th g il fo n o itc ip e d e h t d
e z in o itu lo v e r
s e u q in h c e t ts in o is s e rp
m I s iH .ro lo
…
c
Fig.2. TheoverviewoftheGraphRAGframeworkforquestionansweringtask.Inthissurvey,wedivide
GraphRAGintothreestages:G-Indexing,G-Retrieval,andG-Generation.Wecategorizetheretrievalsources
intoopen-sourceknowledgegraphsandself-constructedgraphdata.Variousenhancingtechniqueslikequery
enhancementandknowledgeenhancementmaybeadoptedtoboosttherelevanceoftheresults.Unlike
RAG,whichusesretrievedtextdirectlyforgeneration,GraphRAGrequiresconvertingtheretrievedgraph
informationintopatternsacceptabletogeneratorstoenhancethetaskperformance.
theprogressandprospectsofthisfield.Furthermore,wecompileaninventoryofexisting
industryGraphRAGsystems,providinginsightsintothetranslationofacademicresearch
intoreal-worldindustrysolutions.
Organization. Therestofthesurveyisorganizedasfollows:Section2comparesrelatedtechniques,whileSection3outlinesthegeneralprocessofGraphRAG.Sections5to7categorizethe
techniquesassociatedwithGraphRAG’sthreestages:G-Indexing,G-Retrieval,andG-Generation.
Section8introducesthetrainingstrategiesofretrieversandgenerators.Section9summarizes
GraphRAG’sdownstreamtasks,correspondingbenchmarks,applicationdomains,evaluationmetrics,andindustrialGraphRAGsystems.Section10providesanoutlookonfuturedirections.Finally,
Section11concludesthecontentofthissurvey.
2 ComparisonwithRelatedTechniquesandSurveys
In this section, we compare Graph Retrieval-Augmented Generation (GraphRAG) with related
techniques and corresponding surveys, including RAG, LLMs on graphs, and Knowledge Base
QuestionAnswering(KBQA).

## 1 Rag

RAGcombinesexternalknowledgewithLLMsforimprovedtaskperformance,integratingdomainspecificinformationtoensurefactualityandcredibility.Inthepasttwoyears,researchershave
writtenmanycomprehensivesurveysaboutRAG[34,45,59,62,178,195,202].Forexample, Fan
etal.[34] andGaoetal.[45] categorizeRAGmethodsfromtheperspectivesofretrieval,generation,andaugmentation. Zhaoetal.[202] reviewRAGmethodsfordatabaseswithdifferent
modalities. Yuetal.[195] systematicallysummarizetheevaluationofRAGmethods.Theseworks
J.ACM,Vol.37,No.4,Article111.Publicationdate:September2024.

<!-- Page 5 -->


### GraphRetrieval-AugmentedGeneration:ASurvey 111:5

provideastructuredsynthesisofcurrentRAGmethodologies,fosteringadeeperunderstanding
andsuggestingfuturedirectionsofthearea.
Fromabroadperspective,GraphRAGcanbeseenasabranchofRAG,whichretrievesrelevant
relationalknowledgefromgraphdatabasesinsteadoftextcorpus.However,comparedtotextbasedRAG,GraphRAGtakesintoaccounttherelationshipsbetweentextsandincorporatesthe
structuralinformationasadditionalknowledgebeyondtext.Furthermore,duringtheconstruction
ofgraphdata,rawtextdatamayundergofilteringandsummarizationprocesses,enhancingthe
refinementofinformationwithinthegraphdata.AlthoughprevioussurveysonRAGhavetouched
uponGraphRAG,theypredominantlycenterontextualdataintegration.Thispaperdivergesby
placingaprimaryemphasisontheindexing,retrieval,andutilizationofstructuredgraphdata,
whichrepresentsasubstantialdeparturefromhandlingpurelytextualinformationandspursthe
emergenceofmanynewtechniques.
2.2 LLMsonGraphs
LLMsarerevolutionizingnaturallanguageprocessingduetotheirexcellenttextunderstanding,
reasoning, and generation capabilities, along with their generalization and zero-shot transfer
abilities. Although LLMs are primarily designed to process pure text and struggle with non-
Euclideandatacontainingcomplexstructuralinformation,suchasgraphs[49,165],numerous
studies[17,35,74,92,102,116,130,131,173,204]havebeenconductedinthesefields.Thesepapers
primarilyintegrateLLMswithGNNstoenhancemodelingcapabilitiesforgraphdata,thereby
improvingperformanceondownstreamtaskssuchasnodeclassification,edgeprediction,graph
classification,andothers.Forexample, Zhuetal.[204] proposeanefficientfine-tuningmethod
namedENGINE,whichcombinesLLMsandGNNsthroughasidestructureforenhancinggraph
representation.
Differentfromthesemethods,GraphRAGfocusesonretrievingrelevantgraphelementsusing
queriesfromanexternalgraph-structureddatabase.Inthispaper,weprovideadetailedintroduction
totherelevanttechnologiesandapplicationsofGraphRAG,whicharenotincludedinprevious
surveysofLLMsonGraphs.

## 3 Kbqa

KBQAisasignificanttaskinnaturallanguageprocessing,aimingtorespondtouserqueriesbasedon
externalknowledgebases[41,85,86,188],therebyachievinggoalssuchasfactverification,passage
retrieval enhancement, and text understanding. Previous surveys typically categorize existing
KBQAapproachesintotwomaintypes:InformationRetrieval(IR)-basedmethodsandSemantic
Parsing(SP)-basedmethods.Specifically,IR-basedmethods[69,70,112,113,154,167,182,196]
retrieveinformationrelatedtothequeryfromtheknowledgegraph(KG)anduseittoenhancethe
generationprocess.WhileSP-basedmethods[16,19,36,48,153,191]generatealogicalform(LF)
foreachqueryandexecuteitagainstknowledgebasestoobtaintheanswer.
GraphRAGandKBQAarecloselyrelated,withIR-basedKBQAmethodsrepresentingasubsetof
GraphRAGapproachesfocusedondownstreamapplications.Inthiswork,weextendthediscussion
beyondKBQAtoincludeGraphRAG’sapplicationsacrossvariousdownstreamtasks.Oursurvey
providesathoroughanddetailedexplorationofGraphRAGtechnology,offeringacomprehensive
understandingofexistingmethodsandpotentialimprovements.
3 Preliminaries
Inthissection,weintroducebackgroundknowledgeofGraphRAGforeasiercomprehensionof
oursurvey.First,weintroduceText-AttributedGraphswhichisauniversalandgeneralformatof
J.ACM,Vol.37,No.4,Article111.Publicationdate:September2024.

<!-- Page 6 -->

111:6 Pengetal.
graphdatausedinGraphRAG.Then,weprovideformaldefinitionsfortwotypesofmodelsthat
canbeusedintheretrievalandgenerationstages:GraphNeuralNetworksandLanguageModels.
3.1 Text-AttributedGraphs
ThegraphdatausedinGraphRAGcanberepresenteduniformlyasText-AttributedGraphs(TAGs),
wherenodesandedgespossesstextualattributes.Formally,atext-attributedgraphcanbedenoted
as G = (V,E,A,{x𝑣}𝑣∈V ,{e𝑖,𝑗}𝑖,𝑗∈E ), where V is the set of nodes, E ⊆ V ×V is the set of
edges,A ∈ {0,1}|V|×|V| istheadjacentmatrix.Additionally,{x𝑣}𝑣∈V and{e𝑖,𝑗}𝑖,𝑗∈E aretextual
attributesofnodesandedges,respectively.OnetypicalkindofTAGsisKnowledgeGraphs(KGs),
wherenodesareentities,edgesarerelationsamongentities,andtextattributesarethenamesof
entitiesandrelations.
3.2 GraphNeuralNetworks
GraphNeuralNetworks(GNNs)areakindofdeeplearningframeworktomodelthegraphdata.
ClassicalGNNs,e.g.,GCN[83],GAT[162],GraphSAGE[52],adoptamessage-passingmannerto
obtainnoderepresentations.Formally,eachnoderepresentationh (𝑙−1) inthe𝑙-thlayerisupdated
𝑖
byaggregatingtheinformationfromneighboringnodesandedges:
h
𝑖
(𝑙) =UPD(h
𝑖
(𝑙−1),AGG𝑗∈N(𝑖) MSG(h
𝑖
(𝑙−1),h (
𝑗
𝑙−1),e
𝑖
(
,
𝑙
𝑗
−1))), (1)
whereN (𝑖) representstheneighborsofnode𝑖.MSGdenotesthemessagefunction,whichcomputes
the message based on the node, its neighbor, and the edge between them. AGG refers to the
aggregationfunctionthatcombinesthereceivedmessagesusingapermutation-invariantmethod,
such as mean, sum, or max. UPD represents the update function, which updates each node’s
attributeswiththeaggregatedmessages.
Subsequently,areadoutfunction,e.g.,mean,sum,ormaxpooling,canbeappliedtoobtainthe
global-levelrepresentation:
h𝐺 =READOUT𝑖∈V𝐺 (h
𝑖

## (𝐿)).

(2)
InGraphRAG,GNNscanbeutilizedtoobtainrepresentationsofgraphdatafortheretrieval
phase,aswellastomodeltheretrievedgraphstructures.
3.3 LanguageModels
Languagemodels(LMs)excelinlanguageunderstandingandaremainlyclassifiedintotwotypes:
discriminativeandgenerative.Discriminativemodels,likeBERT[28],RoBERTa[107]andSentence-
BERT[140],focusonestimatingtheconditionalprobability𝑃(y|x)andareeffectiveintaskssuchas
textclassificationandsentimentanalysis.Incontrast,generativemodels,includingGPT-3[14]and
GPT-4[127],aimtomodelthejointprobability𝑃(x,y)fortaskslikemachinetranslationandtext
generation.Thesegenerativepre-trainedmodelshavesignificantlyadvancedthefieldofnatural
languageprocessing(NLP)byleveragingmassivedatasetsandbillionsofparameters,contributing
totheriseofLargeLanguageModels(LLMs)withoutstandingperformanceacrossvarioustasks.
In the early stages, RAG and GraphRAG focused on improving pre-training techniques for
discriminativelanguagemodels[28,107,140].Recently,LLMssuchasChatGPT[128],LLaMA[31],
andQwen2[184]haveshowngreatpotentialinlanguageunderstanding,demonstratingpowerful
in-contextlearningcapabilities.Subsequently,researchonRAGandGraphRAGshiftedtowards
enhancinginformationretrievalforlanguagemodels,addressingincreasinglycomplextasksand
mitigatinghallucinations,therebydrivingrapidadvancementsinthefield.
J.ACM,Vol.37,No.4,Article111.Publicationdate:September2024.

<!-- Page 7 -->

GraphRetrieval-AugmentedGeneration:ASurvey 111:7
4 OverviewofGraphRAG
GraphRAGisaframeworkthatleveragesexternalstructuredknowledgegraphstoimprovecontextualunderstandingofLMsandgeneratemoreinformedresponses,asdepictedinFigure2.The
goalofGraphRAGistoretrievethemostrelevantknowledgefromdatabases,therebyenhancing
theanswersofdownstreamtasks.Theprocesscanbedefinedas
𝑎∗ =argmax𝑝(𝑎|𝑞,G),
(3)
𝑎∈𝐴
where 𝑎∗ is the optimal answer of the query𝑞 given the TAG G, and 𝐴 is the set of possible
responses.After that,wejointlymodelthetargetdistribution𝑝(𝑎|𝑞,G) withagraphretriever
𝑝 𝜃(𝐺|𝑞,G)andananswergenerator𝑝 𝜙(𝑎|𝑞,𝐺)where𝜃,𝜙 arelearnableparameters,andutilizethe
totalprobabilityformulatodecompose𝑝(𝑎|𝑞,G),whichcanbeformulatedas
∑︁
𝑝(𝑎|𝑞,G) = 𝑝 𝜙(𝑎|𝑞,𝐺)𝑝 𝜃(𝐺|𝑞,G)

## 𝐺⊆G (4)

≈𝑝 𝜙(𝑎|𝑞,𝐺∗)𝑝 𝜃(𝐺∗|𝑞,G),
where𝐺∗ istheoptimalsubgraph.Becausethenumberofcandidatesubgraphscangrowexponentiallywiththesizeofthegraph,efficientapproximationmethodsarenecessary.Thefirstline
ofEquation4isthusapproximatedbythesecondline.Specifically,agraphretrieverisemployed
toextracttheoptimalsubgraph𝐺∗,afterwhichthegeneratorproducestheanswerbasedonthe
retrievedsubgraph.
Therefore,inthissurvey,wedecomposetheentireprocessofGraphRAGintothreemainstages:
Graph-BasedIndexing,Graph-GuidedRetrieval,andGraph-EnhancedGeneration.Theoverall
workflowofGraphRAGisillustratedinFigure2anddetailedintroductionsofeachstageareas
follows.
Graph-Based Indexing (G-Indexing). Graph-Based Indexing constitutes the initial phase of
GraphRAG,aimedatidentifyingorconstructingagraphdatabaseGthatalignswithdownstream
tasks and establishing indices on it. The graph database can originate from public knowledge
graphs[4,10,100,142,150,163],graphdata[123],orbeconstructedbasedonproprietarydata
sourcessuchastextual[32,51,89,172]orotherformsofdata[183].Theindexingprocesstypicallyincludesmappingnodeandedgeproperties,establishingpointersbetweenconnectednodes,
andorganizingdatatosupportfasttraversalandretrievaloperations.Indexingdeterminesthe
granularityofthesubsequentretrievalstage,playingacrucialroleinenhancingqueryefficiency.
Graph-GuidedRetrieval(G-Retrieval). Followinggraph-basedindexing,thegraph-guidedretrieval
phasefocusesonextractingpertinentinformationfromthegraphdatabaseinresponsetouser
queriesorinput.Specifically,givenauserquery𝑞 whichisexpressedinnaturallanguage,the
retrievalstageaimstoextractthemostrelevantelements(e.g.,entities,triplets,paths,subgraphs)
fromknowledgegraphs,whichcanbeformulatedas
𝐺∗ =G-Retriever(𝑞,G)
=argmax 𝑝 𝜃(𝐺|𝑞,G)

## 𝐺⊆R(G) (5)

=argmax Sim(𝑞,𝐺),

## 𝐺⊆R(G)

where𝐺∗ istheoptimalretrievedgraphelementsandSim(·,·) isafunctionthatmeasuresthe
semanticsimilaritybetweenuserqueriesandthegraphdata.R(·)representsafunctiontonarrow
downthesearchrangeofsubgraphs,consideringtheefficiency.
J.ACM,Vol.37,No.4,Article111.Publicationdate:September2024.

<!-- Page 8 -->

111:8 Pengetal.
Graph-Enhanced Generation (G-Generation). The graph-enhanced generation phase involves
synthesizing meaningful outputs or responses based on the retrieved graph data. This could
encompassansweringuserqueries,generatingreports,etc.Inthisstage,ageneratortakesthe
query,retrievedgraphelements,andanoptionalpromptasinputtogeneratearesponse,which
canbedenotedas
𝑎∗ =G-Generator(𝑞,𝐺∗)
=argmax𝑝 𝜙(𝑎|𝑞,𝐺∗)
𝑎∈𝐴 (6)
=argmax𝑝 𝜙(𝑎|F(𝑞,𝐺∗)),
𝑎∈𝐴
whereF(·,·)isafunctionthatconvertsgraphdataintoaformthegeneratorcanprocess.
5 Graph-BasedIndexing
The construction and indexing of graph databases form the foundation of GraphRAG, where
thequalityofthegraphdatabasedirectlyimpactsGraphRAG’sperformance.Inthissection,we
categorizeandsummarizetheselectionorconstructionofgraphdataandvariousindexingmethods
thathavebeenemployed.
5.1 GraphData
Various types of graph data are utilized in GraphRAG for retrieval and generation. Here, we
categorizethesedataintotwocategoriesbasedontheirsources,includingOpenKnowledgeGraphs
andSelf-ConstructedGraphData.
5.1.1 OpenKnowledgeGraphs. Openknowledgegraphsrefertographdatasourcedfrompublicly
availablerepositoriesordatabases[4,10,150,163].Usingtheseknowledgegraphscoulddramatically
reducethetimeandresourcesrequiredtodevelopandmaintain.Inthissurvey,wefurtherclassify
themintotwocategoriesaccordingtotheirscopes,i.e.,GeneralKnowledgeGraphsandDomain
KnowledgeGraphs.
(1)GeneralKnowledgeGraphs. Generalknowledgegraphsprimarilystoregeneral,structured
knowledge,andtypicallyrelyoncollectiveinputandupdatesfromaglobalcommunity,ensuringa
comprehensiveandcontinuallyrefreshedrepositoryofinformation.
Encyclopedicknowledgegraphsareatypicaltypeofgeneralknowledgegraph,whichcontains
large-scalereal-worldknowledgecollectedfromhumanexpertsandencyclopedias.Forexample,
Wikidata1 [163]isafreeandopenknowledgebasethatstoresstructureddataofitsWikimedia
sisterprojectslikeWikipedia,Wikivoyage,Wiktionary,andothers.Freebase2[10]isanextensive,
collaborativelyeditedknowledgebasethatcompilesdatafromvarioussources,includingindividual
contributionsandstructureddatafromdatabaseslikeWikipedia.DBpedia3[4]representsinformationaboutmillionsofentities,includingpeople,places,andthings,byleveragingtheinfoboxes
andcategoriespresentinWikipediaarticles.YAGO4 [150]collectsknowledgefromWikipedia,
WordNet,andGeoNames.
Commonsenseknowledgegraphsareanothertypeofgeneralknowledgegraph.Theyinclude
abstractcommonsenseknowledge,suchassemanticassociationsbetweenconceptsandcausal
relationshipsbetweenevents.TypicalCommonsenseKnowledgeGraphsinclude:ConceptNet5[100]
1https://www.wikidata.org/
2http://www.freebase.be/
3https://www.dbpedia.org/
4https://yago-knowledge.org/
5https://conceptnet.io/
J.ACM,Vol.37,No.4,Article111.Publicationdate:September2024.

<!-- Page 9 -->


### GraphRetrieval-AugmentedGeneration:ASurvey 111:9

isasemanticnetworkbuiltfromnodesrepresentingwordsorphrasesconnectedbyedgesdenoting
semanticrelationships.ATOMIC[64,142]modelsthecausalrelationshipsbetweenevents.
(2)DomainKnowledgeGraphs. AsdiscussedinSection1,domain-specificknowledgegraphsare
crucialforenhancingLLMsinaddressingdomain-specificquestions.TheseKGsofferspecialized
knowledgeinparticularfields,aidingmodelsingainingdeeperinsightsandamorecomprehensive
understandingofcomplexprofessionalrelationships.Inthebiomedicalfield,CMeKG6encompasses
awiderangeofdata,includingdiseases,symptoms,treatments,medications,andrelationships
betweenmedicalconcepts.CPubMed-KG7isamedicalknowledgedatabaseinChinese,buildingon
theextensiverepositoryofbiomedicalliteratureinPubMed.Inthemoviedomain,Wiki-Movies[121]
extracts structured information from Wikipedia articles related to films, compiling data about
movies,actors,directors,genres,andotherrelevantdetailsintoastructuredformat.Additionally, Jin
etal.[75] constructadatasetnamedGR-Bench,whichincludesfivedomainknowledgegraphs
spanningacademic,E-commerce,literature,healthcare,andlegalfields.Furthermore, Heetal.
[55] converttriplet-formatandJSONfilesfromExplaGraphsandSceneGraphsintoastandard
graphformatandselectsquestionsrequiring2-hopreasoningfromWebQSPtocreatetheuniversal
graph-formatdatasetGraphQAforevaluatingGraphRAGsystems.
5.1.2 Self-ConstructedGraphData. Self-ConstructedGraphDatafacilitatesthecustomizationand
integrationofproprietaryordomain-specificknowledgeintotheretrievalprocess.Fordownstream
tasksthatdonotinherentlyinvolvegraphdata,researchersoftenproposeconstructingagraph
frommultiplesources(e.g.,documents,tables,andotherdatabases)andleveragingGraphRAGto
enhancetaskperformance.Generally,theseself-constructedgraphsarecloselytiedtothespecific
designofthemethod,distinguishingthemfromtheopen-domaingraphdatapreviouslymentioned.
Tomodelthestructuralrelationshipsbetweenthedocuments, Munikotietal.[124] proposeto
constructaheterogeneousdocumentgraphcapturingmultipledocument-levelrelations,including
co-citation,co-topic,co-venue,etc. Lietal.[96] andWangetal.[172] establishrelationship
between passages according to shared keywords. To capture the relations between entities in
documents, Delileetal.[26] ,Edgeetal.[32] ,Gutiérrezetal.[51] andLietal.[89] utilizethe
namedentityrecognitiontoolstoextractentitiesfromdocumentsandlanguagemodelstofurther
extractrelationsbetweenentities,wheretheretrievedentitiesandrelationsthenformaknowledge
graph.Therearealsosomemappingmethodsfordownstreamtasksthatneedtobedesignedbased
onthecharacteristicsofthetaskitself.Forexample,tosolvethepatentphrasesimilarityinference
task, PengandYang[133] convertthepatentdatabaseintoapatent-phrasegraph.Connections
betweenpatentnodesandphrasenodesareestablishedifthephrasesappearinthepatents,while
connections between patent nodes are based on citation relations. Targeting customer service
technicalsupportscenarios, Xuetal.[183] proposetomodelhistoricalissuesintoaKG,which
transformstheissuesintotreerepresentationstomaintaintheintra-issuerelations,andutilize
semanticsimilaritiesandathresholdtopreserveinter-issuerelations.
5.2 Indexing
Graph-BasedIndexingplaysacrucialroleinenhancingtheefficiencyandspeedofqueryoperations
ongraphdatabases,directlyinfluencingsubsequentretrievalmethodsandgranularity.Common
graph-basedindexingmethodsincludegraphindexing,textindexing,andvectorindexing.
5.2.1 GraphIndexing. Graphindexingrepresentsthemostcommonlyusedapproach,preserving
theentirestructureofthegraph.Thismethodensuresthatforanygivennode,allitsedgesand
6https://cmekg.pcl.ac.cn/
7https://cpubmed.openi.org.cn/graph/wiki
J.ACM,Vol.37,No.4,Article111.Publicationdate:September2024.

<!-- Page 10 -->

111:10 Pengetal.
§5.2 Indexing
• GraphIndexing
§5.1GraphData • TextIndexing
• Self-constructedKnowledgeGraphs • VectorIndexing
• HybridIndexing
Data Source • OpenKnowledgeGraphs
• General Knowledge Graphs Graph
Wikipedia Tex.t.C.orpus Tables • Domain Knowledge Graphs Database
Fig.3. Theoverviewofgraph-basedindexing.
neighboringnodesareeasilyaccessible.Duringsubsequentretrievalstages,classicgraphsearch
algorithms such as BFS and Shortest Path Algorithms can be employed to facilitate retrieval
tasks[73,75,112,113,154,158,189].
5.2.2 TextIndexing. Textindexinginvolvesconvertinggraphdataintotextualdescriptionsto
optimizeretrievalprocesses.Thesedescriptionsarestoredinatextcorpus,wherevarioustext-based
retrievaltechniques,suchassparseretrievalanddenseretrieval,canbeapplied.Someapproaches
transformknowledgegraphsintohuman-readabletextusingpredefinedrulesortemplates.For
instance, Lietal.[90] ,Huangetal.[63] andLietal.[95] usepredefinedtemplatestoconvert
eachtripleinknowledgegraphsintonaturallanguage,while Yuetal.[193] mergetripletswith
thesameheadentityintopassages.Additionally,somemethodsconvertsubgraph-levelinformation
intotextualdescriptions.Forexample, Edgeetal.[32] performcommunitydetectiononthegraph
andgeneratesummariesforeachcommunityusingLLMs.
5.2.3 VectorIndexing. Vectorindexingtransformsgraphdataintovectorrepresentationstoenhanceretrievalefficiency,facilitatingrapidretrievalandeffectivequeryprocessing.Forexample,
entitylinkingcanbeseamlesslyappliedthroughqueryembeddings,andefficientvectorsearch
algorithms such as Locality Sensitive Hashing (LSH) [66] can be utilized. G-Retriever [55] employslanguagemodelstoencodetextualinformationassociatedwitheachnodeandedgewithin
the graph, while GRAG [58] uses language models to convert𝑘-hop ego networks into graph
embeddings,therebybetterpreservingstructuralinformation.
5.2.4 HybridIndexing. Eachoftheabovethreeindexingmethodsoffersdistinctadvantages:graph
indexing facilitates easy access to structural information, text indexing simplifies retrieval of
textualcontent,andvectorindexingenablesquickandefficientsearches.Therefore,inpractical
applications,ahybridapproachcombiningtheseindexingmethodsisoftenpreferredoverrelying
solelyonone.Forinstance,HybridRAG[144]retrievesbothvectorandgraphdatasimultaneously
toenhancethecontentretrieved.WhileEWEK-QA[24]usesbothtextandknowledgegraphs.
6 Graph-GuidedRetrieval
InGraphRAG,theretrievalprocessiscrucialforensuringthequalityandrelevanceofgenerated
outputsbyextractingpertinentandhigh-qualitygraphdatafromexternalgraphdatabases.However,
retrievinggraphdatapresentstwosignificantchallenges:(1)ExplosiveCandidateSubgraphs:Asthe
graphsizeincreases,thenumberofcandidatesubgraphsgrowsexponentially,requiringheuristic
searchalgorithmstoefficientlyexploreandretrieverelevantsubgraphs.(2)InsufficientSimilarity
Measurement:Accuratelymeasuringsimilaritybetweentextualqueriesandgraphdatanecessitates
thedevelopmentofalgorithmscapableofunderstandingbothtextualandstructuralinformation.
J.ACM,Vol.37,No.4,Article111.Publicationdate:September2024.

<!-- Page 11 -->

GraphRetrieval-AugmentedGeneration:ASurvey 111:11

### InputQuery

§6.4.1 QueryEnhancement
• Query Expansion
§6.2 Retrieval Paradigm
• Query Decomposition
• Multi-Stage Retrieval
§6.3 Retrieval • Iterative Retrieval
Granularity • Once Retrieval §6.4.2 Knowledge
• Nodes §6.1 Retriever Enhancement
• Triplets • Non-parametric Retriever
• Paths • KnowledgeMerging
Graph • Subgraphs • LM-Based Retriever
• KnowledgePruning

### Database • Hybrid • GNN-Based Retriever

Fig.4. Thegeneralarchitecturesofgraph-basedretrieval.
Considerableeffortshavepreviouslybeendedicatedtooptimizingtheretrievalprocesstoaddress
theabovechallenges.Thissurveyfocusesonexaminingvariousaspectsoftheretrievalprocess
withinGraphRAG,includingtheselectionoftheretriever,retrievalparadigm,retrievalgranularity,
andeffectiveenhancementtechniques.ThegeneralarchitecturesofGraph-GuidedRetrievalare
depictedinFigure4.
6.1 Retriever
In GraphRAG, various retrievers possess unique strengths for addressing different aspects of
retrievaltasks.Wecategorizeretrieversintothreetypesbasedontheirunderlyingmodels:NonparametricRetriever,LM-basedRetriever,andGNN-basedRetriever.Itisimportanttonotethat
modelsusedinpre-processingsteps,suchasqueryencodingandentitylinking,arenotconsidered
here,asthesemodelsvaryacrossdifferentmethodsandarenottheprimaryfocusofthispaper.
6.1.1 Non-parametricRetriever. Non-parametricretrievers,basedonheuristicrulesortraditional
graphsearchalgorithms,donotrelyondeep-learningmodels,therebyachievinghighretrieval
efficiency. For instance, Yasunaga et al. [189] and Taunk et al. [158] retrieve𝑘-hop paths
containingthetopicentitiesofeachquestion-choicepair.G-Retriever[55]enhancestheconventionalPrize-CollectingSteinerTree(PCST)algorithmbyincorporatingedgepricesandoptimizing
relevantsubgraphextraction. Delileetal.[26] andMavromatisandKarypis[119] firstextract
entitiesmentionedinthequeryandthenretrievetheshortestpathrelatedtotheseentities.These
methodsofteninvolveanentitylinkingpre-processingsteptoidentifynodesinthegraphbefore
retrieval.
6.1.2 LM-basedRetriever. LMsserveaseffectiveretrieversinGraphRAGduetotheirstrongnatural
languageunderstandingcapabilities.Thesemodelsexcelinprocessingandinterpretingdiverse
naturallanguagequeries,makingthemversatileforawiderangeofretrievaltaskswithingraphbasedframeworks.WeprimarilycategorizedLMsintotwotypes:discriminativeandgenerative
languagemodels.SubgraphRetriever[196]trainsRoBERTa[107]astheretriever,whichexpands
fromthetopicentityandretrievestherelevantpathsinasequentialdecisionprocess.KG-GPT[80]
adoptsLLMstogeneratethesetoftop-𝐾 relevantrelationsofthespecificentity. Woldetal.[176]
utilizefine-tunedGPT-2togeneratereasoningpaths.StructGPT[67]utilizesLLMstoautomatically
invokeseveralpre-definedfunctions,bywhichrelevantinformationcanberetrievedandcombined
toassistfurtherreasoning.
J.ACM,Vol.37,No.4,Article111.Publicationdate:September2024.

<!-- Page 12 -->

111:12 Pengetal.
6.1.3 GNN-based Retriever. GNNs are adept at understanding and leveraging complex graph
structures.GNN-basedretrieverstypicallyencodegraphdataandsubsequentlyscoredifferent
retrievalgranularitiesbasedontheirsimilaritytothequery.Forexample,GNN-RAG[119]first
encodesthegraph,assignsascoretoeachentity,andretrievesentitiesrelevanttothequerybased
onathreshold.EtD[99]iteratesmultipletimestoretrieverelevantpaths.Duringeachiteration,it
firstusesLLaMA2[160]toselectedgesconnectingthecurrentnode,thenemploysGNNstoobtain
embeddingsofthenewlayerofnodesforthenextroundofLLMselection.
6.1.4 Discussion. Duringtheretrievalprocess,non-parametricretrieversexhibitgoodretrieval
efficiency,buttheymaysufferfrominaccurateretrievalduetoalackoftrainingondownstream
tasks.Meanwhile,althoughLM-basedretrieversandGNN-basedretrieversofferhigherretrieval
accuracy,theyrequiresignificantcomputationaloverhead.Consideringthiscomplementarity,many
methodsproposehybridretrievalapproachestoimprovebothretrievalefficiencyandaccuracy.
Manyapproachesadoptamulti-stageretrievalstrategy,employingdifferentmodelsateachstage.
For example, RoG [112] first utilizes LLMs to generate planning paths and then extracts paths
satisfyingtheplanningpathsfromknowledgegraphs.GenTKGQA[44]inferscrucialrelationsand
constraintsfromthequeryusingLLMsandextractstripletsaccordingtotheseconstraints.
6.2 RetrievalParadigm
WithinGraphRAG,differentretrievalparadigms,includingonceretrieval,iterativeretrieval,and
multi-stage retrieval, play crucial roles in improving the relevance and depth of the retrieved
information.Onceretrievalaimstogatherallpertinentinformationinasingleoperation.Iterative
retrievalconductsfurthersearchesbasedonpreviouslyretrievedinformation,progressivelynarrowingdowntothemostrelevantresults.Herewefurtherdivideiterativeretrievalintoadaptive
retrievalandnon-adaptiveretrieval,withtheonlydifferencelyinginwhetherthestoppingofthe
retrievalisdeterminedbythemodel.Anotherretrievalparadigmismulti-stageretrieval,where
retrievalisdividedintomultiplestages.Differenttypesofretrieversmaybeemployedateachstage
formorepreciseanddiversifiedsearchresults.Below,wewillprovideadetailedintroductionto
thesetypesofretrievalparadigms.
6.2.1 OnceRetrieval. Onceretrievalaimstoretrievealltherelevantinformationinasinglequery.
Onecategoryofapproaches[51,58,90]utilizeembeddingsimilaritiestoretrievethemostrelevant
piecesofinformation.Anothercategoryofmethodsdesignpre-definedrulesorpatternstodirectly
extractspecificstructuredinformationsuchastriplets,pathsorsubgraphsfromgraphdatabases.
Forexample,G-Retriever[55]utilizesanextendedPCSTalgorithmtoretrievethemostrelevant
subgraph.KagNet[97]extractspathsbetweenallpairsoftopicentitieswithlengthsnotexceeding
𝑘. Yasunagaetal.[189] andTaunketal.[158] extractthesubgraphthatcontainsalltopicentities
alongwiththeir2-hopneighbors.
Furthermore,inthissubsection,wealsoincludesomemultipleretrievalmethodsthatinvolve
decoupledandindependentretrievals,allowingthemtobecomputedinparallelandexecutedonly
once.Forexample, Luoetal.[112] andChengetal.[20] firstinstructLLMstogeneratemultiple
reasoningpathsandthenuseaBFSretrievertosequentiallysearchforsubgraphsintheknowledge
graphsthatmatcheachpath.KG-GPT[80]decomposestheoriginalqueryintoseveralsub-queries,
retrievingrelevantinformationforeachsub-queryinasingleretrievalprocess.
6.2.2 Iterative Retrieval. In iterative retrieval, multiple retrieval steps are employed, with subsequentsearchesdependingontheresultsofpriorretrievals.Thesemethodsaimtodeepenthe
understanding or completeness of the retrieved information over successive iterations. In this
J.ACM,Vol.37,No.4,Article111.Publicationdate:September2024.

<!-- Page 13 -->


### GraphRetrieval-AugmentedGeneration:ASurvey 111:13

survey,wefurtherclassifyiterativeretrievalintotwocategories:(1)non-adaptiveand(2)adaptive
retrieval.Weprovideadetailedsummaryofthesetwocategoriesofmethodsbelow.
(1)Non-AdaptiveRetrieval. Non-adaptivemethodstypicallyfollowafixedsequenceofretrieval,
and the termination of retrieval is determined by setting a maximum time or a threshold. For
example,PullNet[151]retrievesproblem-relevantsubgraphsthrough𝑇 iterations.Ineachiteration,
thepaperdesignsaretrievalruletoselectasubsetofretrievedentities,andthenexpandsthese
entitiesbysearchingrelevantedgesintheknowledgegraph.Ineachiteration,KGP[172]first
selectsseednodesbasedonthesimilaritybetweenthecontextandthenodesinthegraph.Itthen
usesLLMstosummarizeandupdatethecontextoftheneighboringnodesoftheseednodes,which
isutilizedinthesubsequentiteration.
(2)AdaptiveRetrieval. Onedistinctivecharacteristicofadaptiveretrievalistoletmodelsautonomouslydeterminetheoptimalmomentstofinishtheretrievalactivities.Forinstance,[50,182]
leverageanLMforhopprediction,whichservesasanindicatortoendtheretrieval.Thereisalsoa
groupofresearcherswhoutilizemodel-generatedspecialtokensortextsasterminationsignalsfor
theretrievalprocess.Forexample,ToG[113,154]promptstheLLMagenttoexplorethemultiple
possiblereasoningpathsuntiltheLLMdeterminesthequestioncanbeansweredbasedonthe
currentreasoningpath.[196]trainsaRoBERTatoexpandapathfromeachtopicentity.Inthe
process,avirtualrelationnamedas“[END]”isintroducedtoterminatetheretrievalprocess.
Anothercommonapproachinvolvestreatingthelargemodelasanagent,enablingittodirectly
generateanswerstoquestionstosignaltheendofiteration.Forinstance,[67,69,75,155,170]
proposeLLM-basedagentstoreasonongraphs.Theseagentscouldautonomouslydeterminethe
informationforretrieval,invokethepre-definedretrievaltools,andceasetheretrievalprocess
basedontheretrievedinformation.
6.2.3 Multi-StageRetrieval. Multi-stageretrievaldividestheretrievalprocesslinearlyintomultiple
stages,withadditionalstepssuchasretrievalenhancement,andevengenerationprocessesoccurringbetweenthesestages.Inmulti-stageretrieval,differentstagesmayemployvarioustypesof
retrievers,whichenablesthesystemtoincorporatevariousretrievaltechniquestailoredtodifferent
aspectsofthequery.Forexample, Wangetal.[171] firstutilizeanon-parametricretrieverto
extract𝑛-hoppathsofentitiesinthequery’sreasoningchain,thenafterapruningstage,itfurther
retrievestheone-hopneighborsoftheentitiesintheprunedsubgraph.OpenCSR[53]dividesthe
retrievalprocessintotwostages.Inthefirststage,itretrievesall1-hopneighborsofthetopic
entity.Inthesecondstage,itcomparesthesimilaritybetweentheseneighbornodesandother
nodes,selectingthetop-𝑘 nodeswiththehighestsimilarityforretrieval.GNN-RAG[119]first
employsGNNstoretrievethetop-𝑘 nodesmostlikelytobetheanswer.Subsequently,itretrieves
allshortestpathsbetweenqueryentitiesandanswerentitiespairwise.
6.2.4 Discussion. InGraphRAG,onceretrievaltypicallyexhibitslowercomplexityandshorter
responsetimes,makingitsuitableforscenariosrequiringreal-timeresponsiveness.Incontrast,
iterative retrieval often involves higher time complexity, especially when employing LLMs as
retrievers,potentiallyleadingtolongerprocessingtimes.However,thisapproachcanyieldhigher
retrievalaccuracybyiterativelyrefiningretrievedinformationandgeneratingresponses.Therefore,
thechoiceofretrievalparadigmshouldbalanceaccuracyandtimecomplexitybasedonspecific
usecasesandrequirements.
6.3 RetrievalGranularity
According to different task scenarios and indexing types, researchers design distinct retrieval
granularities(i.e.,theformofrelatedknowledgeretrievedfromgraphdata),whichcanbedivided
J.ACM,Vol.37,No.4,Article111.Publicationdate:September2024.

<!-- Page 14 -->

111:14 Pengetal.
intonodes,triplets,paths,andsubgraphs.Eachretrievalgranularityhasitsownadvantages,making
itsuitablefordifferentpracticalscenarios.Wewillintroducethedetailsofthesegranularitiesin
thefollowingsections.
6.3.1 Nodes. Nodesallowforpreciseretrievalfocusedonindividualelementswithinthegraph,
whichisidealfortargetedqueriesandspecificinformationextraction.Ingeneral,forknowledge
graphs,nodesrefertoentities.Forothertypesoftextattributegraphs,nodesmayincludetextual
informationthatdescribesthenode’sattributes.Byretrievingnodeswithinthegraph,GraphRAG
systemscouldprovidedetailedinsightsintotheirattributes,relationships,andcontextualinformation.Forexample, Munikotietal.[124] ,Lietal.[96] andWangetal.[172] constructdocument
graphsandretrievesrelevantpassagenodes. Liuetal.[99] ,Sunetal.[151] andGutiérrezetal.
[51] retrieveentitiesfromconstructedknowledgegraphs.
6.3.2 Triplets. Generally,tripletsconsistofentitiesandtheirrelationshipsintheformofsubjectpredicate-objecttuples,providingastructuredrepresentationofrelationaldatawithinagraph.The
structuredformatoftripletsallowsforclearandorganizeddataretrieval,makingitadvantageous
in scenarios where understanding relationships and contextual relevance between entities is
critical. Yangetal.[185] retrievetripletscontainingtopicentitiesasrelevantinformation. Huang
etal.[63] ,Lietal.[90] andLietal.[95] firstconverteachtripletofgraphdataintotextual
sentencesusingpredefinedtemplatesandsubsequentlyadoptatextretrievertoextractrelevant
triplets.However,directlyretrievingtripletsfromgraphdatamaystilllackcontextualbreadth
anddepth,thusbeingunabletocaptureindirectrelationshipsorreasoningchains.Toaddressthis
challenge, Wangetal.[164] proposetogeneratethelogicalchainsbasedontheoriginalquestion,
andretrievetherelevanttripletsofeachlogicalchain.
6.3.3 Paths. Theretrievalofpath-granularitydatacanbeseenascapturingsequencesofrelationships between entities, enhancing contextual understanding and reasoning capabilities. In
GraphRAG, retrieving paths offers distinct advantages due to their ability to capture complex
relationshipsandcontextualdependencieswithinagraph.
However,pathretrievalcanbechallengingduetotheexponentialgrowthinpossiblepathsas
graphsizeincreases,whichescalatescomputationalcomplexity.Toaddressthis,somemethods
retrieverelevantpathsbasedonpre-definedrules.Forexample, Wangetal.[171] andLoand
Lim[108] firstselectentitypairsinthequeryandthentraversetofindallthepathsbetween
themwithin𝑛-hop.HyKGE[73]firstdefinesthreetypesofpaths:path,co-ancestorchain,and
co-occurrencechain,andthenutilizescorrespondingrulestoretrieveeachofthesethreetypesof
paths.Inaddition,somemethodsutilizemodelstoperformpathsearchingongraphs.ToG[113,154]
proposestoprompttheLLMagenttoperformthebeamsearchonKGsandfindmultiplepossible
reasoningpathsthathelpanswerthequestion. Luoetal.[112] ,Wuetal.[182] andGuoetal.
[50] firstutilizesthemodeltogeneratefaithfulreasoningplansandthenretrievesrelevantpaths
basedontheseplans.GNN-RAG[119]firstidentifiestheentitiesinthequestion.Subsequently,all
pathsbetweenentitiesthatsatisfyacertainlengthrelationshipareextracted.
6.3.4 Subgraphs. Retrievingsubgraphsofferssignificantadvantagesduetoitsabilitytocapture
comprehensiverelationalcontextswithinagraph.ThisgranularityenablesGraphRAGtoextract
andanalyzecomplexpatterns,sequences,anddependenciesembeddedwithinlargerstructures,
facilitatingdeeperinsightsandamorenuancedunderstandingofsemanticconnections.
Toensurebothinformationcompletenessandretrievalefficiency,somemethodsproposean
initialrule-basedapproachtoretrievecandidatesubgraphs,whicharesubsequentlyrefinedor
processed further. Peng and Yang [133] retrieve the ego graph of the patent phrase from the
self-constructedpatent-phrasegraph. Yasunagaetal.[189] ,Fengetal.[40] andTaunketal.
J.ACM,Vol.37,No.4,Article111.Publicationdate:September2024.

<!-- Page 15 -->


### GraphRetrieval-AugmentedGeneration:ASurvey 111:15

[158] firstselectthetopicentitiesandtheirtwo-hopneighborsasthenodeset,andthenchoose
theedgeswithheadandtailentitiesbothinthenodesettoformthesubgraph.Besides,thereare
alsosomeembedding-basedsubgraphretrievalmethods.Forexample, Huetal.[58] firstencode
allthe𝑘-hopegonetworksfromthegraphdatabase,thenretrievesubgraphsrelatedtothequery
basedonthesimilaritiesbetweenembeddings. Wenetal.[175] andLietal.[89] extracttwo
typesofgraphs,includingPathevidencesubgraphsandNeighborevidencesubgraphs,basedon
pre-definedrules.OpenCSR[53]startsfromafewinitialseednodesandgraduallyexpandstonew
nodes,eventuallyformingasubgraph.
Inadditiontotheaforementioneddirectsubgraphretrievalmethods,someworksproposefirst
retrievingrelevantpathsandthenconstructingrelatedsubgraphsfromthem.Forinstance, Zhang
et al. [196] train a RoBERTa model to identify multiple reasoning paths through a sequential
decisionprocess,subsequentlymergingidenticalentitiesfromdifferentpathstoinduceafinal
subgraph.
6.3.5 HybridGranularties. Consideringtheadvantagesanddisadvantagesofvariousretrievalgranularitiesmentionedabove,someresearchersproposeusinghybridgranularities,thatis,retrieving
relevantinformationofmultiplegranularitiesfromgraphdata.Thistypeofgranularityenhances
thesystem’sabilitytocapturebothdetailedrelationshipsandbroadercontextualunderstanding,
thusreducingnoisewhileimprovingtherelevanceoftheretrieveddata.Variouspreviousworks
proposetoutilizeLLMagentstoretrievecomplexhybridinformation. Jinetal.[75] ,Jiangetal.
[67] ,Jiangetal.[69] ,Wangetal.[170] andSunetal.[155] proposetoadoptLLM-basedagents
foradaptivelyselectingnodes,triplets,paths,andsubgraphs.
6.3.6 Discussion. (1)Inrealapplications,therearenoclearboundariesbetweentheseretrieval
granularities,assubgraphscanbecomposedofmultiplepaths,andpathscanbeformedbyseveral
triplets.(2)Variousgranularitiessuchasnodes,triplets,paths,andsubgraphsofferdistinctadvantagesintheGraphRAGprocess.Balancingbetweenretrievalcontentandefficiencyiscrucialwhen
selectingthegranularity,dependingonthespecificcontextofthetask.Forstraightforwardqueries
orwhenefficiencyisparamount,finergranularitiessuchasentitiesortripletsmaybepreferredto
optimizeretrievalspeedandrelevance.Incontrast,complexscenariosoftenbenefitfromahybrid
approach that combines multiple granularities. This approach ensures a more comprehensive
understanding of the graph structure and relationships, enhancing the depth and accuracy of
thegeneratedresponses.Thus,GraphRAG’sflexibilityingranularityselectionallowsittoadapt
effectivelytodiverseinformationretrievalneedsacrossvariousdomains.
6.4 RetrievalEnhancement
Toensurehighretrievalquality,researchersproposetechniquestoenhancebothuserqueriesand
theknowledgeretrieved.Inthispaper,wecategorizequeryenhancementintoqueryexpansionand
querydecomposition,andknowledgeenhancementintomergingandpruning.Thesestrategies
collectivelyoptimizetheretrievalprocess.Althoughothertechniquessuchasqueryrewriting[114,
117,132,137]arecommonlyusedinRAG,theyarelessfrequentlyappliedinGraphRAG.Wedo
notdelveintothesemethods,despitetheirpotentialadaptationforGraphRAG.
6.4.1 QueryEnhancement. Strategiesappliedtoqueriestypicallyinvolvepre-processingtechniques
that enrich the information for better retrieval. This may include query expansion and query
decomposition.
(1)QueryExpansion. Duetothegenerallyshortlengthofqueriesandtheirlimitedinformation
content,queryexpansionaimstoimprovesearchresultsbysupplementingorrefiningtheoriginal
querywithadditionalrelevanttermsorconcepts. Luoetal.[112] generaterelationpathsgrounded
J.ACM,Vol.37,No.4,Article111.Publicationdate:September2024.

<!-- Page 16 -->

111:16 Pengetal.
byKGswithLLMstoenhancetheretrievalquery. Chengetal.[20] adoptSPARQLtogetallthe
aliasesofthequeryentitiesfromWikidatatoaugmenttheretrievalqueries,whichcapturelexical
variationsofthesameentity. Huangetal.[63] proposeaconsensus-viewknowledgeretrieval
methodtoimproveretrievalaccuracy,whichfirstdiscoversemanticallyrelevantqueries,andthen
re-weighttheoriginalquerytermstoenhancetheretrievalperformance.HyKGE[73]utilizesa
largemodeltogeneratethehypothesisoutputofthequestion,concatenatingthehypothesisoutput
withthequeryasinputtotheretriever.Golden-Retriever[2]firstrecognizesthejargoninthe
queryandthenretrievesexplanationsofthejargonasasupplementtothequery.
(2)QueryDecomposition. Querydecompositiontechniquesbreakdownordecomposetheoriginal
userqueryintosmaller,morespecificsub-queries.Eachsub-querytypicallyfocusesonaparticular
aspect or component of the original query, which successfully alleviates the complexity and
ambiguityoflanguagequeries.Forinstance,[22,80]breaksdowntheprimaryquestionintosubsentences,eachrepresentingadistinctrelation,andsequentiallyretrievesthepertinenttripletsfor
eachsub-sentence.
6.4.2 KnowledgeEnhancement. Afterretrievinginitialresults,knowledgeenhancementstrategies
areemployedtorefineandimprovetheretriever’sresults.Thisphaseofteninvolvesknowledge
mergingandknowledgepruningprocessestopresentthemostpertinentinformationprominently.
Thesetechniquesaimtoensurethatthefinalsetofretrievedresultsisnotonlycomprehensivebut
alsohighlyrelevanttotheuser’sinformationneeds.
(1)KnowledgeMerging. Knowledgemergingretrievedinformationenablescompressionand
aggregationofinformation,whichassistsinobtainingamorecomprehensiveviewbyconsolidating
relevantdetailsfrommultiplesources.Thisapproachnotonlyenhancesthecompletenessand
coherenceoftheinformationbutalsomitigatesissuesrelatedtoinputlengthconstraintsinmodels.
KnowledgeNavigator[50]mergesnodesandcondensestheretrievedsub-graphthroughtriple
aggregationtoenhancethereasoningefficiency.InSubgraphRetrieval[196],afterretrievingtop-𝑘
pathsfromeachtopicentitytoformasinglesubgraph,researchersproposetomergethesame
entitiesfromdifferentsubgraphstoformthefinalsubgraph. Wenetal.[175] andLietal.[89]
mergeretrievedsubgraphsbasedonrelations,combiningheadentitiesandtailentitiesthatsatisfy
thesamerelationintotwodistinctentitysets,ultimatelyformingarelationpaths.
(2)KnowledgePruning. Knowledgepruninginvolvesfilteringoutlessrelevantorredundant
retrievedinformationtorefinetheresults.Previousapproachesforpruningencompasstwomain
categories:(re)-ranking-basedapproachesandLLM-basedapproaches.(Re)-rankingmethodsinvolvethereorderingorprioritizationofretrievedinformationusingtailoredmetricsorcriteria.
One line of methods introduces stronger models for reranking. For example, Li et al. [90]
concatenateeachretrievedtripletwiththequestion-choicepair,andadoptapre-trainedcrossencoder[140]tore-ranktheretrievedtriplets. Jiangetal.[73] utilizetheFlagEmbeddingtoencode
thetexttore-ranktop-kdocumentsreturnedbyembeddingmodel“bge_reranker_large”. Liuetal.
[101] trainaPLMto
Anothercategoryutilizesthesimilaritybetweenqueriesandretrievedinformationforranking.
Forinstance, Chengetal.[20] re-rankthecandidatesubgraphsbasedonthesimilarityforboth
relationandfine-grainedconceptbetweensubgraphsandthequery. Taunketal.[158] firstcluster
the2-hopneighborsandthendeletetheclusterwiththelowestsimilarityscorewiththeinput
query. Yasunagaetal.[189] prunetheretrievedsubgraphaccordingtotherelevancescorebetween
thequestioncontextandtheKGentitynodescalculatedbyapre-trainedlanguagemodel. Wang
etal.[171] ,Jiangetal.[70] ,Gutiérrezetal.[51] andLuoetal.[110] adoptPersonalizedPageRank
algorithmtoranktheretrievedcandidateinformationforfurtherfiltering. Liuetal.[101] trains
J.ACM,Vol.37,No.4,Article111.Publicationdate:September2024.

<!-- Page 17 -->


### GraphRetrieval-AugmentedGeneration:ASurvey 111:17

§7.3 Generation Pre-Generation Mid-Generation Post-Generation
Enhancement Enhancement Enhancement Enhancement
§7.2 GraphFormats §7.1 Generators

### Retrieval

• GraphLanguages • GNNs Response

### Results • LMs

• GraphEmbeddings
• HybridModels
Fig.5. Theoverviewofgraph-enhancedgeneration.
aPLMtoscorethesimilaritybetweentheretrievedinformationandthequery,andrerankthe
retrievedpathsbasedonthesimilarityscore.G-G-E[43]firstdividestheretrievedsubgraphinto
severalsmallersubgraphs,thencomparesthesimilaritybetweeneachsmallersubgraphandthe
query.Subgraphswithlowsimilarityareremoved,andtheremainingsmallersubgraphsaremerged
intoalargersubgraph.
Additionally,athirdcategoryofmethodsproposesnewmetricsforreranking.Forexample, Munikotietal.[124] proposeametricthatmeasuresboththeimpactandrecencyoftheretrievedtext
chunks.KagNet[97]decomposestheretrievedpathsintotripletsandreranksthepathsbasedon
theconfidencescoremeasuredbytheknowledgegraphembedding(KGE)techniques.LLM-based
methodsexcelincapturingcomplexlinguisticpatternsandsemanticnuances,whichenhances
theirabilitytoranksearchresultsorgenerateresponsesmoreaccurately.Toavoidintroducing
noisyinformation, Wangetal.[171] andKimetal.[80] proposetoprunetheirrelevantgraph
databycallingLLMstocheck.
7 Graph-EnhancedGeneration
ThegenerationstageisanothercrucialstepinGraphRAG,aimedatintegratingtheretrievedgraph
datawiththequerytoenhanceresponsequality.Inthisstage,suitablegenerationmodelsmust
beselectedbasedonthedownstreamtasks.Theretrievedgraphdataisthentransformedinto
formatscompatiblewiththegenerators.Thegeneratortakesboththequeryandthetransformed
graphdataasinputstoproducethefinalresponse.Beyondthesefundamentalprocesses,generative
enhancementtechniquescanfurtherimprovetheoutputbyintensifyingtheinteractionbetween
thequeryandthegraphdataandenrichingthecontentgenerationitself.Theorganizationofthis
sectionandtheoverviewofgraph-enhancedgenerationaredepictedinFigure5.
7.1 Generators
Theselectionofgeneratorsoftendependsonthetypeofdownstreamtaskathand.Fordiscriminativetasks(e.g.,multi-choicequestionanswering)orgenerativetasksthatcanbeformulatedas
discriminativetasks(e.g.,KBQA),onecanutilizeGNNsordiscriminativelanguagemodelstolearn
representationsofthedata.Theserepresentationscanthenbemappedtothelogitsassociated
withdifferentansweroptionstoprovideresponses.Alternatively,generativelanguagemodelscan
beemployedtodirectlygenerateanswers.Forgenerativetasks,however,theuseofGNNsand
discriminativelanguagemodelsaloneisinsufficient.Thesetasksrequirethegenerationoftext,
whichnecessitatesthedeploymentofdecoders.
7.1.1 GNNs. DuetothepowerfulrepresentationalcapabilitiesofGNNsforgraphdata,theyare
particularlyeffectivefordiscriminativetasks.GNNscandirectlyencodegraphdata,capturing
complexrelationshipsandnodefeaturesinherentinthegraphstructure.ThisencodingisthenprocessedthroughaMulti-LayerPerceptron(MLP)togeneratepredictiveoutcomes.Theseapproaches
J.ACM,Vol.37,No.4,Article111.Publicationdate:September2024.

<!-- Page 18 -->

111:18 Pengetal.
primarilyutilizeclassicalGNNmodels(e.g.,GCN[83],GAT[162],GraphSAGE[52],andGraph
Transformers[147]),eitherintheiroriginalformormodifiedtobetteralignwithdownstreamtasks.
Forexample,HamQA[30]designsahyperbolicGNNtolearntherepresentationsofretrievedgraph
data,whichlearnsfromthemutualhierarchicalinformationbetweenqueryandgraphs. Sunetal.
[152] computePageRankscoresforneighboringnodesandaggregatesthemweightedbythese
scores,duringmessage-passing.Thisapproachenhancesthecentralnode’sabilitytoassimilate
informationfromitsmostrelevantneighboringnodes. MavromatisandKarypis[118] decode
thequeryintoseveralvectors(instructions),andenhancesinstructiondecodingandexecution
foreffectivereasoningbyemulatingbreadth-firstsearch(BFS)withGNNstoimproveinstruction
executionandusingadaptivereasoningtoupdatetheinstructionswithKG-awareinformation.
7.1.2 LMs. LMs possess strong capabilities in text understanding, which also allows them to
functionasgenerators.InthecontextofintegratingLMswithgraphdata,itisnecessarytofirst
convert the retrieved graph data into specific graph formats. This conversion process ensures
thatthestructuredinformationiseffectivelyunderstoodandutilizedbytheLMs.Theseformats,
whichwillbeelaboratedoninSection7.2,arecrucialforpreservingtherelationalandhierarchical
structureofthegraphdata,therebyenhancingthemodel’sabilitytointerpretcomplexdatatypes.
Oncethegraphdataisformatted,itisthencombinedwithaqueryandfedintoanLM.
Forencoder-onlymodels,suchasBERT[28]andRoBERTa[107],theirprimaryuseisindiscriminativetasks.SimilartoGNNs,thesemodelsfirstencodetheinputtextandthenutilizeMLPstomap
ittotheanswerspace[63,70,90].Ontheotherhand,encoder-decoderanddecoder-onlymodels,
suchasT5[138],GPT-4[127],andLLaMA[31],areadeptatbothdiscriminativeandgenerative
tasks. These models excel in text understanding, generation, and reasoning, allowing them to
processtextualinputsdirectlyandgeneratetextualresponses[32,73,75,112,119,154,164,171].
7.1.3 HybridModels. ConsideringthestrengthsofGNNsatrepresentingthestructureofgraph
data,andtherobustunderstandingoftextdemonstratedbyLMs,manystudiesareexploringthe
integrationofthesetwotechnologiestogeneratecoherentresponses.Thispapercategorizesthe
hybridgenerativeapproachesintotwodistincttypes:cascadedparadigmandparallelparadigm.
(1)CascadedParadigm. Inthecascadedapproaches,theprocessinvolvesasequentialinteraction
wheretheoutputfromonemodelservesastheinputforthenext.Specifically,theGNNprocesses
thegraphdatafirst,encapsulatingitsstructuralandrelationalinformationintoaformthatthe
LMcanunderstand.Subsequently,thistransformeddataisfedintotheLM,whichthengenerates
thefinaltext-basedresponse.Thesemethodsleveragethestrengthsofeachmodelinastep-wise
fashion,ensuringdetailedattentiontobothstructuralandtextualdata.
In these methods, prompt tuning [88, 91, 105, 106] is a typical approach, where GNNs are
commonlyemployedtoencodetheretrievedgraphdata.Theencodedgraphdataissubsequently
pre-pendedasaprefixtotheinputtextembeddingsofanLM.TheGNNisthenoptimizedthrough
downstreamtaskstoproduceenhancedencodingsofthegraphdata[44,55,58,197].
(2)ParallelParadigm. Ontheotherhand,theparallelapproachoperatesbyconcurrentlyutilizing
thecapabilitiesofboththeGNNandtheLLM.Inthissetup,bothmodelsreceivetheinitialinputs
simultaneouslyandworkintandemtoprocessdifferentfacetsofthesamedata.Theoutputsare
thenmerged,oftenthroughanothermodelorasetofrules,toproduceaunifiedresponsethat
integratesinsightsfromboththegraphicalstructureandthetextualcontent.
Inthe parallelparadigm, atypical approachinvolvesseparately encodinginputs usingboth
GNNsandLMs,followedbyintegratingthesetworepresentations,ordirectlyintegratingtheir
outputresponses.Forinstance, Jiangetal.[68] aggregatepredictionsfromGNNsandLMsby
weightedsummationtoobtainthefinalanswer. Linetal.[97] andPahujaetal.[129] integrate
J.ACM,Vol.37,No.4,Article111.Publicationdate:September2024.

<!-- Page 19 -->


### GraphRetrieval-AugmentedGeneration:ASurvey 111:19

RetrievedGraphData Adjacency/Edge Table NaturalLanguage NodeSequence
decudortni C M la o u n d e e t ( t ( c
(
la
e C n
n
e
t
c e
e
n
e
la h w
w
t
r
u n u
a
d i r t
t
q e
e
y
r
e
t
u ) c
c
m
e h
h
M n
n
s
o
o ) i
i
v
q
q
n
e
u
u
e
m
e
e
t, s
s
e
i ,
,
n
n
r
e t
t
r
e
s
m o
v
)
d
o
e u
l
r
u
g c
t
e e
io
d d
n
, i
i
n n
z
,
e
e 1
d
w 9
,
th C t e
n a
e m
e r
l c
t
a
w
h e
m
u n r d
t o
g
e
i e q e
v c
u
e
d
h
M e
m n
i o s n
i e q
n . 1
n u
T e 9
e t
t h
s
t
s
i e
.
h n s
r
t c r
e
e o e
v
n d n
o
e u t
lu
u w c
t
r e
i
y
o
t d . e
n
T c n
iz
h h e
e
n e w
d
i s q e
l
u
a
e
te
s
r

## C → C

→
l l a a l
1
u u a
9
t d d e
t
e e
h
r M M a
ce
r o o t
n
n n m
tu
e e o
r
t t → →
y
ve m n n e e e w w n t t t s e e c c h h n n i i q q u u e e s s
new transform
techniques
Code-likeForms SyntaxTree

### Nodefeature:

0: Claude Monet
1: new techniques
0 2: 19th century
3: later art movements
traverse Edgefeature:
(0,1): introduced
19th later art 1 2 3 ( ( 0 0 , , 2 3 ) ) : : e re m v e o r lu g t e io d n i i n zed
century movements Structure:
Tree Construction center node: 0
1st-hop: 1
2nd-hop: 2, 3
Fig.6. Illustrationofthegraphlanguages.Giventheretrievedsubgraphontheleftpart,weshowhowto
transformitintoadjacency/edgetable,naturallanguage,nodesequence,code-likeformsandsyntaxtreesto
adapttheinputformrequirementsofdifferentgenerators.
thegraphrepresentationsderivedfromGNNsandthetextrepresentationsgeneratedbyLMsusing
attentionmechanisms. Yasunagaetal.[189] ,Munikotietal.[124] andTaunketal.[158] directly
concatenategraphrepresentationswithtextrepresentations.
AnotherapproachinvolvesdesigningdedicatedmodulesthatintegrateGNNswithLMs,enabling
theresultingrepresentationstoencapsulatebothstructuralandtextualinformation.Forinstance,
Zhangetal.[199]introduceamodulecalledtheGreaseLMLayer,whichincorporatesbothGNNand
LMlayers.Ateachlayer,thismoduleintegratestextualandgraphrepresentationsusingatwo-layer
MLPbeforepassingthemtothenextlayer.Similarly,ENGINE[204]proposesG-Ladders,which
combineLMsandGNNsthroughasidestructure,enhancingnoderepresentationsfordownstream
tasks.
Discussion. HybridmodelsthatharnessboththerepresentationcapabilitiesofGNNsforgraph
dataandLMsfortextdataholdpromisingapplications.However,effectivelyintegratinginformation
fromthesetwomodalitiesremainsasignificantchallenge.
7.2 GraphFormats
WhenusingGNNsasgenerators,thegraphdatacanbedirectlyencoded.However,whenutilizing
LMsasgenerators,thenon-Euclideannatureofgraphdataposesachallenge,asitcannotbedirectly
combinedwithtextualdataforinputintotheLMs.Toaddressthis,graphtranslatorsareemployedto
convertthegraphdataintoaformatcompatiblewithLMs.Thisconversionenhancesthegenerative
capabilitiesofLMsbyenablingthemtoeffectivelyprocessandutilizestructuredgraphinformation.
Inthissurvey,wesummarizetwodistinctgraphformats:graphlanguagesandgraphembeddings.
WeillustratethisprocesswithanexampleinFigure6,withdetailedintroductionsprovidedbelow.
7.2.1 GraphLanguages. Agraphdescriptionlanguageisaformalizedsystemofnotationthat
is specifically crafted to characterize and represent graph data. It prescribes a uniform syntax
and semantic framework that describes the components and interconnections within a graph.
Throughtheselanguages,userscanconsistentlygenerate,manipulate,andinterpretgraphdata
inacomprehensibleformattomachines.Theyenablethedefinitionofgrapharchitectures,the
specificationofattributesfornodesandedges,andtheimplementationofoperationsandqueries
J.ACM,Vol.37,No.4,Article111.Publicationdate:September2024.

<!-- Page 20 -->

111:20 Pengetal.
ongraphstructures.Next,wewillintroducefivetypesofgraphlanguagesseparately:Adjacency/
EdgeTable,NaturalLanguage,Codes,SyntaxTree,andNodeSequence.
(1)Adjacency/EdgeTable. Theadjacencytableandtheedgetablearewidelyusedmethods
fordescribinggraphstructures[38,49,94,165].Theadjacencytableenumeratestheimmediate
neighborsofeachvertex,offeringacompactwaytorepresentconnectionsinsparsegraphs.For
example,KG-GPT[80]linearizesthetriplesintheretrievedsubgraph,whicharethenconcatenated
andfedintotheLLMs.Conversely,theedgetabledetailsalltheedgeswithinthegraph,providing
astraightforwardrepresentationthatisparticularlyusefulforprocessingandanalyzinggraphsin
alinearformat.Bothtwomethodsarebrief,easytounderstand,andintuitive.
(2)NaturalLanguage. Giventhatuserqueriesaretypicallypresentedinnaturallanguage,and
consideringtheoutstandingnaturallanguagecomprehensioncapabilitiesofLMs,itbecomesa
compellingapproachtodescribetheretrievedgraphdatausingnaturallanguage.Bytranslating
graph data into descriptive, easily comprehensible language, LMs can bridge the gap between
raw data representation and user-friendly information, facilitating more effective interactions
withdata-drivenapplications.Forexample,someresearchers[63,90]proposedefininganatural
languagetemplateforeachtypeofedgeinadvanceandsubsequentlyfillingintheendpointsofeach
edgeintothecorrespondingtemplatebasedonitstype. Yeetal.[190] employnaturallanguageto
describetheinformationof1-hopand2-hopneighboringnodesofthecentralnode. Edgeetal.[32]
utilizeLLMstogeneratereport-likesummariesforeachdetectedgraphcommunity. Wuetal.[182]
andGuoetal.[50] adoptLMstorewritetheedgetableofretrievedsubgraphs,generatinganatural
languagedescription. Fatemietal.[38] exploredifferentrepresentationsofnodes(e.g.,Integer
encoding,alphabetletters,names,etc.)andedges(e.g.,parenthesis,arrows,incident,etc.). Jin
etal.[75] ,Jiangetal.[67] ,Jiangetal.[69] ,Wangetal.[170] andSunetal.[155] integrate
informationfromdifferentgranularitieswithinthegraphintopromptsthroughnaturallanguage
intheformofdialogue.
(3)Code-LikeForms. Consideringthatnaturallanguagedescriptionsandother1-Dsequencesare
inherentlyinadequatefordirectlyrepresentingthe2-Dstructureofgraphdata,andgiventherobust
codecomprehensioncapabilitiesofLMs,manyresearchers[49]exploreusingcode-likeformats
torepresentgraphstructures.Forexample, Guoetal.[49] examinetheuseofGraphModeling
Language (GML) [56] and Graph Markup Language (GraphML) [141] for representing graphs.
Thesestandardizedlanguagesarespecificallydesignedforgraphdata,providingcomprehensive
descriptionsthatencompassnodes,edges,andtheirinterrelationships.
(4)SyntaxTree. Comparedtodirectflatteningofgraphs,someresearch[201]proposetransforminggraphsintostructuresakintosyntaxtrees.Syntaxtreespossessahierarchicalstructureand,
beingtopologicalgraphs,alsomaintainatopologicalorder.Thismethodretainsmorestructural
information,enhancingtheunderstandingandanalysisofthegraph’sintrinsicproperties.Sucha
transformationnotonlypreservestherelationaldynamicsbetweendifferentgraphelementsbut
alsofacilitatesmoresophisticatedalgorithmsforgraphanalysisandprocessing.GRAPHTEXT[201]
proposestransformingtheegonetworkofacentralnodeintoagraph-syntaxtreeformat.This
formatnotonlyencapsulatesstructuralinformationbutalsointegratesthefeaturesofthenodes.By
traversingthissyntaxtree,itispossibletoobtainanodesequencethatmaintainsbothtopological
orderandhierarchicalstructure.
(5)NodeSequence. Somestudies[18,119]proposerepresentinggraphsthroughsequencesof
nodes,whichareoftengeneratedusingpredefinedrules.Comparedtonaturallanguagedescriptions,
thesenodesequencesaremoreconciseandincorporatepriorknowledge,specificallythestructural
J.ACM,Vol.37,No.4,Article111.Publicationdate:September2024.

<!-- Page 21 -->


### GraphRetrieval-AugmentedGeneration:ASurvey 111:21

informationemphasizedbytherules. Luoetal.[112] andSunetal.[154] transformtheretrieved
pathsintonodesequencesandinputthemintoanLLMtoenhancethetaskperformance.LLaGA[18]
proposestwotemplatesthatcantransformgraphsintonodesequences.Thefirsttemplate,known
astheNeighborhoodDetailTemplate,offersadetailedexaminationofthecentralnodealongwith
itsimmediatesurroundings.Thesecond,termedtheHop-FieldOverviewTemplate,providesa
summarizedperspectiveofanode’sneighborhood,whichcanbeexpandedtoencompassbroader
areas.GNN-RAG[119]inputstheretrievedreasoningpathsintoLMsintheformofnodesequences
asprompts.
Discussion. Goodgraphlanguagesshouldbecomplete,concise,andcomprehensible.Completenessentailscapturingallessentialinformationwithinthegraphstructure,ensuringnocritical
detailsareomitted.Concisenessreferstothenecessityofkeepingtextualdescriptionsbrieftoavoid
the“lostinthemiddle”phenomenon[104]orexceedingthelengthlimitationsofLMs.Lengthy
inputscanhinderLMs’processingcapabilities,potentiallycausinglossofcontextortruncateddata
interpretation.ComprehensibilityensuresthatthelanguageusediseasilyunderstoodbyLLMs,
facilitatingaccuraterepresentationofthegraph’sstructure.Duetothecharacteristicsofdifferent
graphlanguages,theirchoicecansignificantlyimpacttheperformanceofdownstreamtasks[38].
7.2.2 Graph Embeddings. The above graph language methods transform graph data into text
sequences,whichmayresultinoverlylengthycontexts,incurringhighcomputationalcostsand
potentiallyexceedingtheprocessinglimitsofLLMs.Additionally,LLMscurrentlystruggletofully
comprehendgraphstructuresevenwithgraphlanguages[49].Thus,usingGNNstorepresent
graphsasembeddingspresentsapromisingalternative.Thecorechallengeliesinintegratinggraph
embeddingswithtextualrepresentationsintoaunifiedsemanticspace.Currentresearchfocuses
onutilizingprompttuningmethodologies,asdiscussedearlier.Therearealsosomemethodsthat
adoptFiD(Fusion-in-Decoder)[65,194],whichfirstconvertthegraphdataintotext,thenencode
itusinganLM-basedencoderandinputitintothedecoders[29,37,193].Notably,feedinggraph
representationsintoLMsisfeasibleprimarilywithopen-sourceLMs,notclosed-sourcemodelslike
GPT-4[127].Whilegraphembeddingmethodsavoidhandlinglongtextinputs,theyfaceother
challenges,suchasdifficultyinpreservingpreciseinformationlikespecificentitynamesandpoor
generalization.
7.3 GenerationEnhancement
Inthegenerationphase,besidesconvertingtheretrievedgraphdataintoformatsacceptablebythe
generatorandinputtingittogetherwiththequerytogeneratethefinalresponse,manyresearchers
explorevariousmethodsofgenerationenhancementtechniquestoimprovethequalityofoutput
responses.Thesemethodscanbeclassifiedintothreecategoriesbasedontheirapplicationstages:
pre-generationenhancement,mid-generationenhancement,andpost-generationenhancement.
7.3.1 Pre-GenerationEnhancement. Pre-generationenhancementtechniquesfocusonimproving
thequalityofinputdataorrepresentationsbeforefeedingthemintothegenerator.Infact,there
is no clear boundary between Pre-Generation Enhancement and Retrieval. In this survey, we
categorizetheretrievalstageastheprocessofretrievingknowledgefromtheoriginalgraph,and
mergingandpruningretrievedknowledge.SubsequentoperationsareconsideredPre-Generation
Enhancements.
Commonlyusedpre-generationenhancementapproachesprimarilyinvolvesemanticallyenrichingtheretrievedgraphdatatoachievetighterintegrationbetweenthegraphdataandtextual
query. Wuetal.[182] employLLMstorewriteretrievedgraphdata,enhancingthenaturalnessand
semanticrichnessofthetransformednaturallanguageoutput.Thismethodnotonlyensuresthat
J.ACM,Vol.37,No.4,Article111.Publicationdate:September2024.

<!-- Page 22 -->

111:22 Pengetal.
graphdataisconvertedintomorefluentandnaturallanguagebutalsoenrichesitssemanticcontent.
Conversely,DALK[89]utilizestheretrievedgraphdatatorewritethequery. Chengetal.[20]
firstleverageLLMstogenerateareasoningplanandanswerqueriesaccordingtotheplan. Taunk
et al. [158] and Yasunaga et al. [189] aim to enhance GNNs by enabling them to learn graph
representationsrelevanttoqueries.TheyachievethisbyextractingallnounsfromtheQApairs(or
theQApairsthemselves)andinsertingthemasnodesintotheretrievedsubgraph. Mavromatis
andKarypis[118] proposeamethodwhere,priortogeneration,therepresentationofthequery
isdecomposedintomultiplevectorstermed“instructions”,eachrepresentingdifferentfeatures
ofthequery.Theseinstructionsareusedasconditionsduringmessagepassingwhenapplying
GNNstolearnfromretrievedsubgraphs.Inaddition,therearemethodsthatincorporateadditional
informationbeyondgraphdata.Forexample,PullNet[151]incorporatesdocumentsrelevantto
entitiesandMVP-Tuning[63]retrievesotherrelatedquestions.
7.3.2 Mid-GenerationEnhancement. Mid-generationenhancementinvolvestechniquesapplied
duringthegenerationprocess.Thesemethodstypicallyadjustthegenerationstrategiesbasedon
intermediateresultsorcontextualcues.TIARA[148]introducesconstraineddecodingtocontrol
theoutputspaceandreducegenerationerrors.Whengeneratinglogicalforms,iftheconstrained
decoderdetectsthatitiscurrentlygeneratingapatternitem,itrestrictsthenextgeneratedtoken
tooptionsthatexistintriescontainingKBclassesandrelations.ComparedwiththeBeamSearch,
thisapproachensuresthatpatternitemsgeneratedareguaranteedtoexistintheknowledgegraph,
therebyreducinggenerationerrors.ThereareothermethodsadjustingthepromptsofLLMsto
achievemulti-stepreasoning.Forexample,MindMap[175]notonlyproducesanswersbutalso
generatesthereasoningprocess.
7.3.3 Post-GenerationEnhancement. Post-generationenhancementoccursaftertheinitialresponse
isgenerated.Post-generationenhancementmethodsprimarilyinvolveintegratingmultiplegeneratedresponsestoobtainthefinalresponse.Somemethodsfocusonintegratingoutputsfrom
thesamegeneratorunderdifferentconditionsorinputs.Forexample, Edgeetal.[32] generatea
summaryforeachgraphcommunity,followedbygeneratingresponsestoqueriesbasedonthe
summary,andthenscoringtheseresponsesusinganLLM.Ultimately,theresponsesaresortedin
descendingorderaccordingtotheirscoresandsequentiallyincorporatedintothepromptuntil
the token limit is reached. Subsequently, the LLM generates the final response. Wang et al.
[164] andKimetal.[80] firstdecomposethequeryintoseveralsub-questions,thengenerate
answersforeachsub-question,andfinallymergetheanswersofallsub-questionstoobtainthe
final answer. Alternatively, other methods combine or select responses generated by different
models. Linetal.[97] andJiangetal.[68] combinetheoutputsgeneratedbybothGNNsand
LLMstoreachasynergisticeffect.UniOQA[95]explorestwomethodsforgeneratinganswers:
oneinvolvesgeneratingqueriesinCypherQueryLanguage(CQL)toexecuteandobtainresults,
whiletheothermethoddirectlygeneratesanswersbasedonretrievedtriplets.Thefinalansweris
determinedthroughadynamicselectionmechanism.InEmbedKGQA[145],besidesthelearned
scoringfunction,researchersadditionallydesignarule-basedscorebasedonthegraphstructures.
Thesetwoscoresarecombinedtofindtheanswerentity. Lietal.[94] combineanswersbasedon
retrievedgraphdatawithresponsesgeneratedaccordingtotheLLM’sownknowledge.Inaddition
tointegratingmultipleresponses,KALMV[7]trainsaverifiertojudgewhetherthegenerated
answeriscorrect,andifitisnot,tofurtherdeterminewhethertheerrorisduetogenerationor
retrieval.
J.ACM,Vol.37,No.4,Article111.Publicationdate:September2024.

<!-- Page 23 -->

GraphRetrieval-AugmentedGeneration:ASurvey 111:23
8 Training
In this section, we summarize the individual training of retrievers, generators, and their joint
training.WecategorizepreviousworksintoTraining-FreeandTraining-Basedapproachesbased
onwhetherexplicittrainingisrequired.Training-Freemethodsarecommonlyemployedwhen
usingclosed-sourceLLMssuchasGPT-4[127]asretrieversorgenerators.Thesemethodsprimarily
rely on carefully crafted prompts to control the retrieval and generation capabilities of LLMs.
DespiteLLMs’strongabilitiesintextcomprehensionandreasoning,achallengeofTraining-Free
methodsliesinthepotentialsub-optimalityofresultsduetothelackofspecificoptimizationfor
downstreamtasks.Conversely,Training-Basedmethodsinvolvetrainingorfine-tuningmodels
usingsupervisedsignals.Theseapproachesenhancethemodelperformancebyadaptingthem
tospecifictaskobjectives,therebypotentiallyimprovingthequalityandrelevanceofretrieved
orgeneratedcontent.Jointtrainingofretrieversandgeneratorsaimstoenhancetheirsynergy,
therebyboostingperformanceondownstreamtasks.Thiscollaborativeapproachleveragesthe
complementary strengths of both components to achieve more robust and effective results in
informationretrievalandcontentgenerationapplications.
8.1 TrainingStrategiesofRetriever
8.1.1 Training-Free. TherearetwoprimarytypesofTraining-FreeRetrieverscurrentlyinuse.
Thefirsttypeconsistsofnon-parametricretrievers.Theseretrieversrelyonpre-definedrulesor
traditionalgraphsearchalgorithmsratherthanspecificmodels[158,189].Thesecondtypeutilizes
pre-trained LMs as retrievers. Specifically, one group of works utilizes pre-trained embedding
modelstoencodethequeriesandperformretrievaldirectlybasedonthesimilaritybetweenthe
queryandgraphelements[90].Anothergroupofworksadoptsgenerativelanguagemodelsfor
training-freeretrieval.Candidategraphelementssuchasentities,triples,paths,orsubgraphsare
includedaspartofthepromptinputtotheLLMs.TheLLMsthenleveragesemanticassociations
toselectappropriategraphelementsbasedontheprovidedprompt[32,75,80,119,154,164,171].
ThesemethodsharnessthepowerfulsemanticunderstandingcapabilitiesofLMstoretrieverelevant
graphelementswithouttheneedforexplicittraining.
8.1.2 Training-Based. Whentheretrievalgranularityisnodesortriplets,manymethodstrain
retrieverstomaximizethesimilaritybetweentheretrievalgroundtruthandthequery.Forinstance,
MemNNs[12]leveragesmetriclearningtocloselyalignthegroundtruthwiththequeryinsemantic
spacewhiledifferentiatingunrelatedfactsfromthequery.Onthecontrary,whentheretrieval
granularityispaths,trainingretrieversoftenadoptsanautoregressiveapproach,wheretheprevious
relationshippathisconcatenatedtotheendofthequery.Themodelthenpredictsthenextrelation
basedontheconcatenatedinput[50,182].
However, the lack of ground truth for retrieval content in the majority of datasets poses a
significantchallenge.Toaddressthisissue,manymethodsattempttoconstructreasoningpaths
basedondistantsupervisiontoguideretrievertraining.Forexample, Zhangetal.[196] ,Feng
etal.[39] andLuoetal.[112] extractallpaths(orshortestpaths)betweenentitiesinthequeries
andentitiesintheanswers,usingthemastrainingdatafortheretriever.Inaddition, Zhangetal.
[196] alsoemployarelationshipextractiondatasetfordistantsupervisioninunsupervisedsettings.
Thereisanothercategoryofmethodsthatutilizeimplicitintermediatesupervisionsignalstotrain
Retrievers.Forinstance,NSM[54]employsabidirectionalsearchstrategy,wheretworetrieversstart
searchingfromtheheadentityandtailentity,respectively.Thesupervisedobjectiveistoensure
thatthepathssearchedbythetworetrieversconvergeascloselyaspossible.KnowGPT[198]and
MINERVA[23]treattheselectionofadjacentnodestobuildpathsorsubgraphsasaMarkovprocess.
J.ACM,Vol.37,No.4,Article111.Publicationdate:September2024.

<!-- Page 24 -->

111:24 Pengetal.
Theydesigntherewardfunctionaroundtheinclusionoftheanswerintheretrievedinformation
andadoptreinforcementlearningmethodse.g.policygradienttooptimizetheretriever.
Somemethodsarguethatdistantsupervisionsignalsorimplicitintermediatesupervisionsignals
maycontainconsiderablenoise,makingitchallengingtotraineffectiveretrievers.Therefore,they
consideremployingself-supervisedmethodsforpre-trainingretrievers.SKP[29]pre-trainsthe
DPR(DensePassageRetrieval)model[78].Initially,itconductsrandomsamplingonsubgraphs
andtransformsthesampledsubgraphsintopassages.Subsequently,itrandomlymaskspassages,
trainsthemodelusingaMaskedLanguageModel(MLM),andemployscontrastivelearningby
treatingthemaskedpassagesandoriginalpassagesaspositivepairsforcomparison.
8.2 TrainingofGenerator
8.2.1 Training-Free. Training-FreeGeneratorsprimarilycatertoclosed-sourceLLMsorscenarios
whereavoidinghightrainingcostsisessential.Inthesemethods,theretrievedgraphdataisfed
intotheLLMalongsidethequery.TheLLMsthengenerateresponsesbasedonthetaskdescription
providedintheprompt,heavilyrelyingontheirinherentabilitytounderstandboththequeryand
thegraphdata.
8.2.2 Training-Based. Trainingthegeneratorcandirectlyreceivesupervisedsignalsfromdownstreamtasks.ForgenerativeLLMs,fine-tuningcanbeachievedusingsupervisedfine-tuning(SFT),
wheretaskdescriptions,queries,andgraphdataareinputted,andtheoutputiscomparedagainst
thegroundtruthforthedownstreamtask[55,58,112].Ontheotherhand,forGNNsordiscriminativemodelsfunctioningasgenerators,specializedlossfunctionstailoredtothedownstreamtasks
areemployedtotrainthemodelseffectively[68,90,158,189,199].
8.3 JointTraining
Jointlytrainingretrieversandgeneratorssimultaneouslyenhancesperformanceondownstream
tasksbyleveragingtheircomplementarystrengths.Someapproachesunifyretrieversandgenerators
intoasinglemodel,typicallyLLMs,andtrainthemwithbothretrievalandgenerationobjectives
simultaneously[112].Thismethodcapitalizesonthecohesivecapabilitiesofaunifiedarchitecture,
enablingthemodeltoseamlesslyretrieverelevantinformationandgeneratecoherentresponses
withinasingleframework.
Othermethodologiesinvolveinitiallytrainingretrieversandgeneratorsseparately,followedby
jointtrainingtechniquestofine-tunebothcomponents.Forinstance,SubgraphRetriever[196]
adopts an alternating training paradigm, where the retriever’s parameters are fixed to use the
graph data for training the generator. Subsequently, the generator’s parameters are fixed, and
feedbackfromthegeneratorisusedtoguidetheretriever’straining.Thisiterativeprocesshelps
bothcomponentsrefinetheirperformanceinacoordinatedmanner.
9 ApplicationsandEvaluation
Inthissection,wewillsummarizethedownstreamtasks,applicationdomains,benchmarksand
metrics, and industrial applications related to GraphRAG. Table 1 collects existing GraphRAG
techniques,categorizingthembydownstreamtasks,benchmarks,methods,andevaluationmetrics.
Thistableservesasacomprehensiveoverview,highlightingthevariousaspectsandapplications
ofGraphRAGtechnologiesacrossdifferentdomains.
9.1 DownstreamTasks
GraphRAG is applied in various downstream tasks (especially NLP tasks), including Question
Answering,InformationExtraction,andothers.
J.ACM,Vol.37,No.4,Article111.Publicationdate:September2024.

<!-- Page 25 -->


### GraphRetrieval-AugmentedGeneration:ASurvey 111:25

Table1. Thetasks,benchmarks,methods,andmetricsofGraphRAG.

### Tasks Benchmarks Methods Metrics

WebQSP[192] [112],[154],[113],[196],[182],[50],[167],[67],[69],[111],[164],[5],[148],
[99],[119],[151],[193],[29],[43],[110],[6],[145],[54],[70],[21],[152],
[71],[7],[24]

### WebQ[8] [171],[154],[60],[182],[118],[71],[12],[24]

CWQ[156] [112],[154],[60],[196],[167],[69],[111],[118],[87],[99],[119],[151],[193],
[43],[110],[70],[94],[54],[21],[24]
KBQA GrailQA[47] [154],[69],[148],[24]

### QALD10-en[134] [154],[113],[94],[155]

SimpleQuestions[13] [154],[5],[12],[24] Accuracy,

## Cmcqa8 [171] Em,

QA MetaQA[200] [112],[182],[50],[80],[164],[118],[151],[145],[67],[99],[54],[70],[21],[101] Recall,
NaturalQuestion[84] [60],[7],[24] F1,

### TriviaQA[77] [60],[70] BERTScore,

HotpotQA[187] [60],[51],[113],[7],[24] GPT-4AverageRanking
Mintaka[146] [5],[94],[6],[7]

### FreebaseQA[72] [193],[110]


## Csqa[157] [158],[189],[63],[90],[97],[39],[30]


## Obqa[120] [158],[189],[63],[90],[39],[53],[30]

MedQA[76] [158],[39],[89]
CSQA SocialIQA[143] [63]

## Piqa[9] [63]


### RiddleSenseQA[98] [63]

EntityLinking ZESHEL[109] [180] Recall@𝐾

### CoNLL[57] [180]


### IE T-Rex[33] [155],[154]

RelationExtraction ZsRE[135] [94],[155],[154],[113] Hits@1
Creak[126] [94],[155],[154],[113]
FactVerification Accuracy,F1

## Factkg[82] [80],[87],[101]


## Fb15K-237[159] [22],[129]

Others LinkPrediction W F N B 1 1 8 5 R k R [1 [ 1 2 ] 7] [ [ 2 1 2 2 ] 9] MRR,Hits@𝐾

## Nell995[15] [22]

DialogueSystems OpenDialKG[122] [5] MRR,Hits@𝐾

### Recommendation Yelp9 [168] NDCG@𝐾,Recall@𝐾

9.1.1 QuestionAnswering. TheQAtasksspecificallyincludeKnowledgeBaseQuestionAnswering
(KBQA)andCommonSenseQuestionAnswering(CSQA).
(1)KBQA. KBQAservesasacornerstonedownstreamtaskforGraphRAG.InKBQA,questions
typicallypertaintospecificknowledgegraphs,andanswersofteninvolveentities,relationships,or
operationsbetweensetsofentitieswithintheknowledgegraph.Thetaskteststhesystems’ability
toretrieveandreasonoverstructuredknowledgebases,whichiscrucialinfacilitatingcomplex
queryresponses.
(2)CSQA. DistinguishedfromKBQA,CSQAprimarilytakestheformofmultiple-choicequestions.
Commonsensereasoningtypicallypresentsacommonsensequestionalongwithseveralanswer
options,eachpotentiallyrepresentingeitherthenameofanentityorastatement.Theobjective
isformachinestoutilizeexternalcommonsenseknowledgegraphs,suchasConceptNet,tofind
relevantknowledgepertainingtothequestionandoptions,andtoengageinappropriatereasoning
andderivethecorrectanswer.
9.1.2 InformationRetrieval. InformationRetrievaltasksconsistoftwocategories:EntityLinking
(EL)andRelationExtraction(RE).
(1)EntityLinking. EntityLinking(EL)isacriticaltaskinthefieldofnaturallanguageprocessing
thatinvolvesidentifyingentitiesmentionedintextsegmentsandlinkingthemtotheircorrespondingentitiesinaknowledgegraph.ByleveragingasystemsuchasGraphRAG,itispossibleto
retrieverelevantinformationfromtheknowledgegraph,whichfacilitatestheaccurateinferenceof
thespecificentitiesthatmatchthementionsinthetext[180].
J.ACM,Vol.37,No.4,Article111.Publicationdate:September2024.

<!-- Page 26 -->

111:26 Pengetal.
(2)RelationExtraction. RelationExtraction(RE)aimsatidentifyingandclassifyingsemantic
relationships between entities within a text. GraphRAG can significantly enhance this task by
usinggraph-basedstructurestoencodeandexploittheinterdependenciesamongentities,thus
facilitatingmoreaccurateandcontextuallynuancedextractionofrelationaldatafromdiversetext
sources[94,154,155].
9.1.3 Others. Inadditiontotheaforementioneddownstreamtasks,GraphRAGcanbeapplied
tovariousothertasksintherealmofnaturallanguageprocessingsuchasfactverification,link
prediction,dialoguesystems,andrecommendation.
(1)FactVerification. Thefactverificationtasktypicallyinvolvesassessingthetruthfulnessofa
factualstatementusingknowledgegraphs.Modelsaretaskedwithdeterminingthevalidityofa
givenfactualassertionbyleveragingstructuredknowledgerepositories.GraphRAGtechniquescan
beutilizedtoextractevidentialconnectionsbetweenentitiestoenhancethesystem’sefficiency
andaccuracy[94,136,154,155].
(2)LinkPrediction. Linkpredictioninvolvespredictingmissingrelationshipsorpotentialconnectionsbetweenentitiesinagraph.GraphRAGisappliedtothistask[22,129]byleveragingits
abilitytoretrieveandanalyzestructuredinformationfromgraphs,enhancingpredictionaccuracy
byuncoveringlatentrelationshipsandpatternswithinthegraphdata.
(3) Dialogue Systems. Dialogue Systems is designed to converse with humans using natural
language,handlingvarioustaskssuchasansweringquestions,providinginformation,orfacilitating
userinteractions.Bystructuringconversationhistoriesandcontextualrelationshipsinagraphbasedframework,GraphRAGsystems[5]canimprovethemodel’sabilitytogeneratecoherentand
contextuallyrelevantresponses.
(4)Recommendation. InthecontextofE-commerceplatforms,thepurchaserelationshipsbetween
usersandproductsnaturallyformanetworkgraph.Theprimaryobjectiveofrecommendation
withintheseplatformsistopredictthefuturepurchasingintentionsofusers,effectivelyforecasting
thepotentialconnectionswithinthisgraph[168].
9.2 ApplicationDomains
GraphRAGiswidelyappliedinE-commerceandbiomedical,academic,literature,legal,andother
applicationscenariosforitsoutstandingabilitytointegratestructuredknowledgegraphswith
naturallanguageprocessing,whichwillbeintroducedbelow.
9.2.1 E-Commerce. TheprimarygoalintheE-commerceareainvolvesimprovingcustomershopping experiences and increasing sales through personalized recommendations and intelligent
customerservices.Inthisarea,historicalinteractionsbetweenusersandproductscannaturally
formagraph,whichimplicitlyencapsulatesusers’behavioralpatternsandpreferenceinformation.
However,duetotheincreasingnumberofE-commerceplatformsandthegrowingvolumeofuser
interaction data, using GraphRAG technology to extract key subgraphs is crucial. Wang et al.
[168] ensemblemultipleretrieversunderdifferenttypesorwithdifferentparameterstoextract
relevantsubgraphs,whicharethenencodedfortemporaluseractionprediction.Toimprovethe
modelperformanceofcustomerservicequestionansweringsystems, Xuetal.[183] construct
apast-issuegraphwithintra-issueandinter-issuerelations.Foreachgivenquery,subgraphsof
similarpastissuesareretrievedtoenhancethesystem’sresponsequality.
9.2.2 Biomedical. Recently,GraphRAGtechniquesareincreasinglyappliedinbiomedicalquestionansweringsystems,achievingadvancedmedicaldecision-makingperformance.Inthisarea,
J.ACM,Vol.37,No.4,Article111.Publicationdate:September2024.

<!-- Page 27 -->


### GraphRetrieval-AugmentedGeneration:ASurvey 111:27

eachdiseaseisassociatedwithspecificsymptoms,andeverymedicationcontainscertainactive
ingredientsthattargetandtreatparticulardiseases.Someresearchers[26,89,177]constructKGs
forspecifictaskscenarios,whileothers[73,175,185]utilizeopen-sourceknowledgegraphssuch
asCMeKGandCPubMed-KGasretrievalsources.Existingmethodsgenerallybeginwithnonparametricretrieversforinitialsearch,followedbydesigningmethodstofilterretrievedcontent
throughre-ranking[26,73,89,175,185].Additionally,someapproachesproposerewritingmodel
inputsusingretrievedinformationtoenhancegenerationeffectiveness[89].
9.2.3 Academic. In the academic research domain, each paper is authored by one or more researchersandisassociatedwithafieldofstudy.Authorsareaffiliatedwithinstitutions,andthere
existrelationshipsamongauthors,suchascollaborationorsharedinstitutionalaffiliations.These
elementscanbestructuredintoagraphformat.UtilizingGraphRAGonthisgraphcanfacilitate
academicexploration,includingpredictingpotentialcollaboratorsforanauthor,identifyingtrends
withinaspecificfield,etc.
9.2.4 Literature. Similartoacademicresearch,aknowledgegraphcanbeconstructedintherealm
ofliterature,withnodesrepresentingbooks,authors,publishers,andseries,andedgeslabeled
“written-by”, “published-in”, and “book-series”. GraphRAG can be utilized to enhance realistic
applicationslikesmartlibraries.
9.2.5 Legal. In legal contexts, extensive citation connections exist between cases and judicial
opinions, as judges frequently reference previous opinions when making new decisions. This
naturallycreatesastructuredgraphwherenodesrepresentopinions,opinionclusters,dockets,and
courts,andedgesencompassrelationshipssuchas“opinion-citation”,“opinion-cluster”,“clusterdocket”,and“docket-court”.TheapplicationofGraphRAGinlegalscenarioscouldaidlawyersand
legalresearchersinvarioustaskssuchascaseanalysisandlegalconsultation.
9.2.6 Others. Inadditiontotheaboveapplications,GraphRAGisalsoappliedtootherreal-world
scenariossuchasintelligencereportgeneration[139],patentphrasesimilaritydetection[133]and
softwareunderstanding[1]. RanadeandJoshi[139] firstconstructanEventPlotGraph(EPG)
andretrievethecriticalaspectsoftheeventstoaidthegenerationofintelligencereports. Peng
andYang[133] createapatent-phrasegraphandretrievetheegonetworkofthegivenpatent
phrasetoassistthejudgmentofphrasesimilarity. Alhanahnahetal.[1] proposeaChatbotto
understandpropertiesaboutdependenciesinagivensoftwarepackage,whichfirstautomatically
constructsthedependencygraphandthentheusercanaskquestionsaboutthedependenciesin
thedependencygraph.
9.3 BenchmarksandMetrics
9.3.1 Benchmarks. ThebenchmarksusedtoevaluatetheperformanceoftheGraphRAGsystem
canbedividedintotwocategories.Thefirstcategoryisthecorrespondingdatasetsofdownstream
tasks.Wesummarizethebenchmarksandpaperstestedwiththemaccordingtotheclassification
in Section 9.1, details of which are shown in Table 1. The second category consists of benchmarksspecificallydesignedfortheGraphRAGsystems.Thesebenchmarksusuallycovermultiple
task domains to provide a comprehensive test result. For example, STARK [179] benchmarks
LLMRetrievalonsemi-structuredknowledgebasescoveringthreedomains,includingproduct
search,academicpapersearch,andqueriesinprecisionmedicinetoaccessthecapacityofcurrent
GraphRAGsystems. Heetal.[55] proposeaflexiblequestion-answeringbenchmarktargeting
real-worldtextualgraphs,namedGraphQA,whichisapplicabletomultipleapplicationsincluding
scene graph understanding, commonsense reasoning, and knowledge graph reasoning. Graph
ReasoningBenchmark(GRBENCH)[75]isconstructedtofacilitatetheresearchofaugmenting
J.ACM,Vol.37,No.4,Article111.Publicationdate:September2024.

<!-- Page 28 -->

111:28 Pengetal.
LLMswithgraphs,whichcontains1,740questionsthatcanbeansweredwiththeknowledgefrom
10domaingraphs.CRAG[186]providesastructuredquerydataset,withadditionalmockAPIsto
accessinformationfromunderlyingmockKGstoachievefaircomparison.
9.3.2 Metrics. TheevaluationmetricsforGraphRAGcanbebroadlycategorizedintotwomain
types:downstreamtaskevaluation(generationquality)andretrievalquality.
(1)DownstreamTaskEvaluation(GenerationQuality). Inthemajorityofresearchstudies,downstreamtaskevaluationmetricsserveastheprimarymethodforassessingGraphRAG’sperformance.
Forexample,inKBQA,ExactMatch(EM)andF1scorearecommonlyusedtomeasuretheaccuracy
ofansweringentities.Inaddition,manyresearchersutilizeBERT4ScoreandGPT4Scoretomitigate
instanceswhereLLMsgenerateentitiesthataresynonymouswiththegroundtruthbutnotexact
matches.InCSQA,Accuracyisthemostcommonlyusedevaluationmetric.Forgenerativetasks
suchasQAsystems,metricslikeBLEU,ROUGE-L,METEOR,andothersarecommonlyemployed
toassessthequalityofthetextgeneratedbythemodel.
(2)RetrievalQualityEvaluation. WhileevaluatingGraphRAGbasedondownstreamtaskperformanceisfeasible,directlymeasuringtheaccuracyofretrievedcontentposeschallenges.Therefore,
manystudiesemployspecificmetricstogaugetheprecisionofretrievedcontent.Forinstance,
whengroundtruthentitiesareavailable,retrievalsystemsfaceabalancebetweenthequantityof
retrievedinformationandthecoverageofanswers.Hence,somestudiesutilizetheratiobetween
answercoverageandthesizeoftheretrievalsubgraphtoevaluatetheperformanceoftheretrieval
system.Inaddition,severalstudieshaveexploredmetricssuchasqueryrelevance,diversity,and
faithfulnessscoretorespectivelyassessthesimilaritybetweenretrievedcontentandqueries,the
diversityofretrievedcontent,andthefaithfulnessoftheinformationretrieved.
9.4 GraphRAGinIndustry
Inthissection,wemainlyfocusonindustrialGraphRAGsystems.Thesesystemsarecharacterized
bytheirrelianceonindustrialgraphdatabasesystemsortheirfocusonlarge-scalegraphdata,
detailsofwhichareasfollows.
•GraphRAG(byMicrosoft)10:ThesystemusesLLMstoconstructentity-basedknowledgegraphs
andpre-generatecommunitysummariesofrelatedentitygroups,whichenablesthecaptureofboth
localandglobalrelationshipswithinadocumentcollection,therebyenhancingQuery-Focused
Summarization(QFS)task[32].Theprojectcanalsoutilizeopen-sourceRAGtoolkitsforrapid
implementation,suchasLlamaIndex11,LangChain12,etc.
•GraphRAG(byNebulaGraph)13:TheprojectisthefirstindustrialGraphRAGsystem,which
isdevelopedbyNebulaGraphCorporation.TheprojectintegratesLLMsintotheNebulaGraph
database,whichaimstodelivermoreintelligentandprecisesearchresults.
• GraphRAG (by Antgroup)14: The framework is developed on the foundation of several AI
engineeringframeworkssuchasDB-GPT,knowledgegraphengineOpenSPG,andgraphdatabase
TuGraph.Specifically,thesystembeginsbyextractingtriplesfromdocumentsusingLLMs,which
arethenstoredinthegraphdatabase.Duringtheretrievalphase,itidentifieskeywordsfromthe
query,locatescorrespondingnodesinthegraphdatabase,andtraversesthesubgraphusingBFS
10https://github.com/microsoft/graphrag
11https://docs.llamaindex.ai/en/stable/examples/indexstructs/knowledgegraph/KnowledgeGraphDemo.html
12https://python.langchain.com/docs/use_cases/graph
13https://www.nebula-graph.io/posts/graph-RAG
14https://github.com/eosphoros-ai/DB-GPT
J.ACM,Vol.37,No.4,Article111.Publicationdate:September2024.

<!-- Page 29 -->


### GraphRetrieval-AugmentedGeneration:ASurvey 111:29

orDFS.Inthegenerationphase,theretrievedsubgraphdataisformattedintotextandsubmitted
alongwiththecontextandqueryforprocessingbyLLMs.
•NallM(byNeo4j)15:TheNaLLM(Neo4jandLargeLanguageModels)frameworkintegrates
Neo4j graph database technology with LLMs. It aims to explore and demonstrate the synergy
betweenNeo4jandLLMs,focusingonthreeprimaryusecases:NaturalLanguageInterfacetoa
KnowledgeGraph,CreatingaKnowledgeGraphfromUnstructuredData,andGenerateReports
UsingBothStaticDataandLLMData.
•LLMGraphBuilder(byNeo4j)16:ItisaprojectdevelopedbyNeo4jforautomaticallyconstructingknowledgegraphs,suitablefortheGraphRAG’sGraphDatabaseConstructionandIndexing
phase.TheprojectprimarilyutilizesLLMstoextractnodes,relationships,andtheirpropertiesfrom
unstructureddata,andutilizestheLangChainframeworktocreatestructuredknowledgegraphs.
10 FutureProspects
WhileGraphRAGtechnologyhasmadesubstantialstrides,itcontinuestofaceenduringchallenges
thatdemandcomprehensiveexploration.Thissectionwilldelveintotheprevalentobstaclesand
outlineprospectiveavenuesforfutureresearchinthefieldofGraphRAG.
10.1 DynamicandAdaptiveGraphs
Most GraphRAG methods [32, 41, 85, 86, 111, 188] are built upon static databases; however, as
timeprogresses,newentitiesandrelationshipsinevitablyemerge[20,44,181].Rapidlyupdating
thesechangesisbothpromisingandchallenging.Incorporatingupdatedinformationiscrucial
forachievingbetterresultsandaddressingemergingtrendsthatrequirecurrentdata.Developing
efficient methods for dynamic updates and real-time integration of new data will significantly
enhancetheeffectivenessandrelevanceofGraphRAGsystems.
10.2 Multi-ModalityInformationIntegration
Mostknowledgegraphsprimarilyencompasstextualinformation,therebylackingtheinclusionof
othermodalitiessuchasimages,audio,andvideos,whichholdthepotentialtosignificantlyenhance
theoverallqualityandrichnessofthedatabase[174].Theincorporationofthesediversemodalities
couldprovideamorecomprehensiveandnuancedunderstandingofthestoredknowledge.However,
the integration of such multi-modal data presents considerable challenges. As the volume of
informationincreases,thegraph’scomplexityandsizegrowexponentially,renderingitincreasingly
difficulttomanageandmaintain.Thisescalationinscalenecessitatesthedevelopmentofadvanced
methodologiesandsophisticatedtoolstoefficientlyhandleandseamlesslyintegratethediverse
datatypesintotheexistinggraphstructure,ensuringboththeaccuracyandaccessibilityofthe
enrichedknowledgegraph.
10.3 ScalableandEfficientRetrievalMechanisms
Knowledgegraphsintheindustrialsettingmayencompassmillionsorevenbillionsofentities,
representing a vast and intricate scale. However, most contemporary methods are tailored for
small-scaleknowledgegraphs[32],whichmayonlycomprisethousandsofentities.Efficientlyand
effectivelyretrievingpertinententitieswithinlarge-scaleknowledgegraphsremainsapractical
andsignificantchallenge.Developingadvancedretrievalalgorithmsandscalableinfrastructure
isessentialtoaddressthisissue,ensuringthatthesystemcanmanagetheextensivedatavolume
whilemaintaininghighperformanceandaccuracyinentityretrieval.
15https://github.com/neo4j/NaLLM
16https://github.com/neo4j-labs/llm-graph-builder
J.ACM,Vol.37,No.4,Article111.Publicationdate:September2024.

<!-- Page 30 -->

111:30 Pengetal.
10.4 CombinationwithGraphFoundationModel
Recently,graphfoundationmodels[42,115],whichcaneffectivelyaddressawiderangeofgraph
tasks,haveachievedsignificantsuccess.DeployingthesemodelstoenhancethecurrentGraphRAG
pipelineisanessentialproblem.Theinputdataforgraphfoundationmodelsisinherentlygraphstructured,enablingthemtohandlesuchdatamoreefficientlythanLLMmodels.Integratingthese
advancedmodelsintotheGraphRAGframeworkcouldgreatlyimprovethesystem’sabilityto
process and utilize graph-structured information, thereby enhancing overall performance and
capability.
10.5 LosslessCompressionofRetrievedContext
InGraphRAG,theretrievedinformationisorganizedintoagraphstructurecontainingentitiesand
theirinterrelations.Thisinformationisthentransformedintoasequencethatcanbeunderstood
byLLMs,resultinginaverylongcontext.Therearetwoissueswithinputtingsuchlongcontexts:
LLMscannothandleverylongsequences,andextensivecomputationduringinferencecanbea
hindranceforindividuals.Toaddresstheseproblems,losslesscompressionoflongcontextsiscrucial.
Thisapproachremovesredundantinformationandcompresseslengthysentencesintoshorter,yet
meaningfulones.IthelpsLLMscapturetheessentialpartsofthecontextandacceleratesinference.
However,designingalosslesscompressiontechniqueischallenging.Currentworks[41,86]make
a trade-off between compression and preserving information. Developing an effective lossless
compressiontechniqueiscrucialbutchallengingforGraphRAG.
10.6 StandardBenchmarks
GraphRAGisarelativelynewfieldthatlacksunifiedandstandardbenchmarksforevaluating
differentmethods.Establishingastandardbenchmarkiscrucialforthisareaasitcanprovidea
consistentframeworkforcomparison,facilitateobjectiveassessmentsofvariousapproaches,and
driveprogressbyidentifyingstrengthsandweaknesses.Thisbenchmarkshouldencompassdiverse
andrepresentativedatasets,well-definedevaluationmetrics,andcomprehensivetestscenariosto
ensurerobustandmeaningfulevaluationsofGraphRAGmethods.
10.7 BroaderApplications
CurrentGraphRAGapplicationsprimarilyfocusoncommontaskssuchascustomerservicesystems[183],recommendationsystems[25],andKBQA[41].ExtendingGraphRAGtobroaderapplicationssuchashealthcare[79],financialservices[3],legalandcompliance[81],smartcitiesand
IoT[149],andmore,involvesincorporatingmorecomplextechniques.Forinstance,inhealthcare,
GraphRAGcansupportmedicaldiagnosis,patientrecordanalysis,andpersonalizedtreatment
plansbyintegratingmedicalliterature,patienthistories,andreal-timehealthdata.Infinancial
services,GraphRAGcanbeutilizedforfrauddetection,riskassessment,andpersonalizedfinancial
advicebyanalyzingtransactionaldata,markettrends,andcustomerprofiles.Legalandcompliance
applicationscanbenefitfromGraphRAGbyenablingcomprehensivelegalresearch,contractanalysis,andregulatorycompliancemonitoringthroughtheintegrationoflegaldocuments,caselaw,
andregulatoryupdates.ExpandingGraphRAGtothesediverseandcomplexdomainswillenhance
itsutilityandimpact,providingmoresophisticatedandtargetedsolutionsacrossvariousfields.
11 Conclusion
Insummary,thissurveyoffersacomprehensiveretrospectiveofGraphRAGtechnology,systematically categorizing and organizing its fundamental techniques, training methodologies, and
J.ACM,Vol.37,No.4,Article111.Publicationdate:September2024.

<!-- Page 31 -->


### GraphRetrieval-AugmentedGeneration:ASurvey 111:31

applicationscenarios.GraphRAGsignificantlyenhancestherelevance,accuracy,andcomprehensivenessofinformationretrievalbyleveragingpivotalrelationalknowledgederivedfromgraph
datasets,therebyaddressingcriticallimitationsassociatedwithtraditionalRetrieval-Augmented
Generationapproaches.Furthermore,asGraphRAGrepresentsarelativelynascentfieldofstudy,
wedelineatethebenchmarks,analyzeprevailingchallenges,andilluminateprospectivefuture
researchdirectionswithinthisdomain.

### Acknowledgments

ThisworkissupportedbyAntGroupthroughAntResearchInternProgram.

### References

[1] MohannadAlhanahnah,YazanBoshmaf,andBenoitBaudry.2024.DepsRAG:TowardsManagingSoftwareDependenciesusingLargeLanguageModels. arXiv:2405.20455[cs.SE] https://arxiv.org/abs/2405.20455
[2] ZhiyuAn,XianzhongDing,Yen-ChunFu,Cheng-ChungChu,YanLi,andWanDu.2024.Golden-Retriever:High-
FidelityAgenticRetrievalAugmentedGenerationforIndustrialKnowledgeBase. arXiv:2408.00798[cs.IR] https:
//arxiv.org/abs/2408.00798
[3] MuhammadArslanandChristopheCruz.2024.Business-RAG:InformationExtractionforBusinessInsights.ICSBT
2024(2024),88.
[4] SörenAuer,ChristianBizer,GeorgiKobilarov,JensLehmann,RichardCyganiak,andZacharyG.Ives.2007.DBpedia:
ANucleusforaWebofOpenData.InTheSemanticWeb,6thInternationalSemanticWebConference,2ndAsian
SemanticWebConference,ISWC2007+ASWC2007,Busan,Korea,November11-15,2007(LectureNotesinComputer
Science,Vol.4825).722–735.
[5] JinheonBaek,AlhamFikriAji,JensLehmann,andSungJuHwang.2023.DirectFactRetrievalfromKnowledgeGraphs
withoutEntityLinking.InProceedingsofthe61stAnnualMeetingoftheAssociationforComputationalLinguistics
(Volume1:LongPapers),ACL2023,Toronto,Canada,July9-14,2023.10038–10055.
[6] JinheonBaek,AlhamFikriAji,andAmirSaffari.2023. Knowledge-AugmentedLanguageModelPromptingfor
Zero-ShotKnowledgeGraphQuestionAnswering. arXiv:2306.04136[cs.CL] https://arxiv.org/abs/2306.04136
[7] JinheonBaek,SoyeongJeong,MinkiKang,JongC.Park,andSungJuHwang.2023.Knowledge-AugmentedLanguage
ModelVerification.InProceedingsofthe2023ConferenceonEmpiricalMethodsinNaturalLanguageProcessing,EMNLP
2023,Singapore,December6-10,2023.1720–1736.
[8] JonathanBerant,AndrewChou,RoyFrostig,andPercyLiang.2013.SemanticParsingonFreebasefromQuestion-
AnswerPairs.InProceedingsofthe2013ConferenceonEmpiricalMethodsinNaturalLanguageProcessing,EMNLP
2013,18-21October2013,GrandHyattSeattle,Seattle,Washington,USA,AmeetingofSIGDAT,aSpecialInterestGroup
oftheACL.1533–1544.
[9] YonatanBisk,RowanZellers,RonanLeBras,JianfengGao,andYejinChoi.2020.PIQA:ReasoningaboutPhysical
CommonsenseinNaturalLanguage.InTheThirty-FourthAAAIConferenceonArtificialIntelligence,AAAI2020,The
Thirty-SecondInnovativeApplicationsofArtificialIntelligenceConference,IAAI2020,TheTenthAAAISymposiumon
EducationalAdvancesinArtificialIntelligence,EAAI2020,NewYork,NY,USA,February7-12,2020.7432–7439.
[10] KurtBollacker,ColinEvans,PraveenParitosh,TimSturge,andJamieTaylor.2008.Freebase:acollaborativelycreated
graphdatabaseforstructuringhumanknowledge.InProceedingsofthe2008ACMSIGMODinternationalconference
onManagementofdata.1247–1250.
[11] KurtD.Bollacker,ColinEvans,PraveenK.Paritosh,TimSturge,andJamieTaylor.2008.Freebase:acollaboratively
createdgraphdatabaseforstructuringhumanknowledge.InProceedingsoftheACMSIGMODInternationalConference
onManagementofData,SIGMOD2008,Vancouver,BC,Canada,June10-12,2008.1247–1250.
[12] AntoineBordes,NicolasUsunier,SumitChopra,andJasonWeston.2015.Large-scaleSimpleQuestionAnswering
withMemoryNetworks. arXiv:1506.02075[cs.LG] https://arxiv.org/abs/1506.02075
[13] AntoineBordes,NicolasUsunier,SumitChopra,andJasonWeston.2015.Large-scaleSimpleQuestionAnswering
withMemoryNetworks. arXiv:1506.02075[cs.LG] https://arxiv.org/abs/1506.02075
[14] TomBrown,BenjaminMann,NickRyder,MelanieSubbiah,JaredDKaplan,PrafullaDhariwal,ArvindNeelakantan,
PranavShyam,GirishSastry,AmandaAskell,etal.2020.Languagemodelsarefew-shotlearners.Advancesinneural
informationprocessingsystems33(2020),1877–1901.
[15] AndrewCarlson,JustinBetteridge,BryanKisiel,BurrSettles,EstevamR.HruschkaJr.,andTomM.Mitchell.2010.
TowardanArchitectureforNever-EndingLanguageLearning.InProceedingsoftheTwenty-FourthAAAIConference
onArtificialIntelligence,AAAI2010,Atlanta,Georgia,USA,July11-15,2010.1306–1313.
J.ACM,Vol.37,No.4,Article111.Publicationdate:September2024.

<!-- Page 32 -->

111:32 Pengetal.
[16] AbirChakraborty.2024. Multi-hopQuestionAnsweringoverKnowledgeGraphsusingLargeLanguageModels.
arXiv:2404.19234[cs.AI] https://arxiv.org/abs/2404.19234
[17] HuajunChen.2024. LargeKnowledgeModel:PerspectivesandChallenges. arXiv:2312.02706[cs.AI] https:
//arxiv.org/abs/2312.02706
[18] RunjinChen,TongZhao,AjayJaiswal,NeilShah,andZhangyangWang.2024.LLaGA:LargeLanguageandGraph
Assistant. arXiv:2402.08170[cs.LG] https://arxiv.org/abs/2402.08170
[19] ShuangChen,QianLiu,ZhiweiYu,Chin-YewLin,Jian-GuangLou,andFengJiang.2021. ReTraCk:Aflexible
andefficientframeworkforknowledgebasequestionanswering.InProceedingsofthe59thannualmeetingofthe
associationforcomputationallinguisticsandthe11thinternationaljointconferenceonnaturallanguageprocessing:
systemdemonstrations.325–336.
[20] KeyuanCheng,GangLin,HaoyangFei,Yuxuanzhai,LuYu,MuhammadAsifAli,LijieHu,andDiWang.2024.
Multi-hopQuestionAnsweringunderTemporalKnowledgeEditing. arXiv:2404.00492[cs.CL] https://arxiv.org/abs/
2404.00492
[21] HyeongKyuChoi,SeunghunLee,JaewonChu,andHyunwooJ.Kim.2023.NuTrea:NeuralTreeSearchforContextguidedMulti-hopKGQA.InAdvancesinNeuralInformationProcessingSystems36:AnnualConferenceonNeural
InformationProcessingSystems2023,NeurIPS2023,NewOrleans,LA,USA,December10-16,2023.
[22] NurendraChoudharyandChandanK.Reddy.2024.ComplexLogicalReasoningoverKnowledgeGraphsusingLarge
LanguageModels. arXiv:2305.01157[cs.LO] https://arxiv.org/abs/2305.01157
[23] RajarshiDas,ShehzaadDhuliawala,ManzilZaheer,LukeVilnis,IshanDurugkar,AkshayKrishnamurthy,AlexSmola,
andAndrewMcCallum.2018.GoforaWalkandArriveattheAnswer:ReasoningOverPathsinKnowledgeBases
usingReinforcementLearning.In6thInternationalConferenceonLearningRepresentations,ICLR2018,Vancouver,BC,
Canada,April30-May3,2018,ConferenceTrackProceedings.
[24] MohammadDehghan,MohammadAliAlomrani,SunyamBagga,DavidAlfonso-Hermelo,KhalilBibi,AbbasGhaddar,
YingxueZhang,XiaoguangLi,JianyeHao,QunLiu,JimmyLin,BoxingChen,PrasannaParthasarathi,MahdiBiparva,
andMehdiRezagholizadeh.2024.EWEK-QA:EnhancedWebandEfficientKnowledgeGraphRetrievalforCitationbasedQuestionAnsweringSystems.InProceedingsofthe62ndAnnualMeetingoftheAssociationforComputational
Linguistics(Volume1:LongPapers),ACL2024,Bangkok,Thailand,August11-16,2024.14169–14187.
[25] YasharDeldjoo,ZhankuiHe,JulianMcAuley,AntonKorikov,ScottSanner,ArnauRamisa,RenéVidal,Maheswaran
Sathiamoorthy,AtoosaKasirzadeh,andSilviaMilano.2024. AReviewofModernRecommenderSystemsUsing
GenerativeModels(Gen-RecSys). arXiv:2404.00579[cs.IR] https://arxiv.org/abs/2404.00579
[26] JulienDelile,SrayantaMukherjee,AntonVanPamel,andLeonidZhukov.2024.Graph-BasedRetrieverCapturesthe
LongTailofBiomedicalKnowledge. arXiv:2402.12352[cs.CL] https://arxiv.org/abs/2402.12352
[27] TimDettmers,PasqualeMinervini,PontusStenetorp,andSebastianRiedel.2018. Convolutional2DKnowledge
GraphEmbeddings.InProceedingsoftheThirty-SecondAAAIConferenceonArtificialIntelligence,(AAAI-18),the30th
innovativeApplicationsofArtificialIntelligence(IAAI-18),andthe8thAAAISymposiumonEducationalAdvancesin
ArtificialIntelligence(EAAI-18),NewOrleans,Louisiana,USA,February2-7,2018.1811–1818.
[28] JacobDevlin,Ming-WeiChang,KentonLee,andKristinaToutanova.2019.BERT:Pre-trainingofDeepBidirectional
TransformersforLanguageUnderstanding.InProceedingsofthe2019ConferenceoftheNorthAmericanChapter
oftheAssociationforComputationalLinguistics:HumanLanguageTechnologies,Volume1(LongandShortPapers).
4171–4186.
[29] GuantingDong,RumeiLi,SiruiWang,YupengZhang,YunsenXian,andWeiranXu.2023. BridgingtheKB-Text
Gap:LeveragingStructuredKnowledge-awarePre-trainingforKBQA.InProceedingsofthe32ndACMInternational
ConferenceonInformationandKnowledgeManagement,CIKM2023,Birmingham,UnitedKingdom,October21-25,2023.
3854–3859.
[30] JunnanDong,QinggangZhang,XiaoHuang,KeyuDuan,QiaoyuTan,andZhimengJiang.2023.Hierarchy-Aware
Multi-HopQuestionAnsweringoverKnowledgeGraphs.InProceedingsoftheACMWebConference2023,WWW
2023,Austin,TX,USA,30April2023-4May2023.ACM,2519–2527.
[31] AbhimanyuDubey,AbhinavJauhri,andetal.2024. TheLlama3HerdofModels. arXiv:2407.21783[cs.AI]
https://arxiv.org/abs/2407.21783
[32] DarrenEdge,HaTrinh,NewmanCheng,JoshuaBradley,AlexChao,ApurvaMody,StevenTruitt,andJonathanLarson.

### FromLocaltoGlobal:AGraphRAGApproachtoQuery-FocusedSummarization. arXiv:2404.16130[cs.CL]

https://arxiv.org/abs/2404.16130
[33] HadyElSahar,PavlosVougiouklis,ArslenRemaci,ChristopheGravier,JonathonS.Hare,FrédériqueLaforest,and
ElenaSimperl.2018.T-REx:ALargeScaleAlignmentofNaturalLanguagewithKnowledgeBaseTriples.InProceedings
oftheEleventhInternationalConferenceonLanguageResourcesandEvaluation,LREC2018,Miyazaki,Japan,May7-12,
2018.
J.ACM,Vol.37,No.4,Article111.Publicationdate:September2024.

<!-- Page 33 -->


### GraphRetrieval-AugmentedGeneration:ASurvey 111:33

[34] WenqiFan,YujuanDing,LiangboNing,ShijieWang,HengyunLi,DaweiYin,Tat-SengChua,andQingLi.2024.A
SurveyonRAGMeetingLLMs:TowardsRetrieval-AugmentedLargeLanguageModels. arXiv:2405.06211[cs.CL]
https://arxiv.org/abs/2405.06211
[35] WenqiFan,ShijieWang,JianiHuang,ZhikaiChen,YuSong,WenzhuoTang,HaitaoMao,HuiLiu,XiaoruiLiu,Dawei
Yin,andQingLi.2024.GraphMachineLearningintheEraofLargeLanguageModels(LLMs).arXiv:2404.14928[cs.LG]
https://arxiv.org/abs/2404.14928
[36] HaishuoFang,XiaodanZhu,andIrynaGurevych.2024.DARA:Decomposition-Alignment-ReasoningAutonomous
LanguageAgentforQuestionAnsweringoverKnowledgeGraphs. arXiv:2406.07080[cs.CL] https://arxiv.org/abs/
2406.07080
[37] JinyuanFang,ZaiqiaoMeng,andCraigMacDonald.2024.REANO:OptimisingRetrieval-AugmentedReaderModels
throughKnowledgeGraphGeneration.InProceedingsofthe62ndAnnualMeetingoftheAssociationforComputational
Linguistics(Volume1:LongPapers),ACL2024,Bangkok,Thailand,August11-16,2024.2094–2112.
[38] BahareFatemi,JonathanHalcrow,andBryanPerozzi.2023.TalklikeaGraph:EncodingGraphsforLargeLanguage
Models. arXiv:2310.04560[cs.LG] https://arxiv.org/abs/2310.04560
[39] ChaoFeng,XinyuZhang,andZichuFei.2023.KnowledgeSolver:TeachingLLMstoSearchforDomainKnowledge
fromKnowledgeGraphs. arXiv:2309.03118[cs.CL] https://arxiv.org/abs/2309.03118
[40] YanlinFeng,XinyueChen,BillYuchenLin,PeifengWang,JunYan,andXiangRen.2020.ScalableMulti-HopRelational
ReasoningforKnowledge-AwareQuestionAnswering.InProceedingsofthe2020ConferenceonEmpiricalMethodsin
NaturalLanguageProcessing,EMNLP2020,Online,November16-20,2020.1295–1309.
[41] BinFu,YunqiQiu,ChengguangTang,YangLi,HaiyangYu,andJianSun.2020. ASurveyonComplexQuestion
AnsweringoverKnowledgeBase:RecentAdvancesandChallenges. arXiv:2007.13069[cs.CL] https://arxiv.org/abs/
2007.13069
[42] MikhailGalkin,XinyuYuan,HeshamMostafa,JianTang,andZhaochengZhu.2023.TowardsFoundationModelsfor
KnowledgeGraphReasoning.InTheTwelfthInternationalConferenceonLearningRepresentations.
[43] HanningGao,LingfeiWu,PoHu,ZhihuaWei,FangliXu,andBoLong.2022.Graph-augmentedLearningtoRank
forQueryingLarge-scaleKnowledgeGraph.InProceedingsofthe2ndConferenceoftheAsia-PacificChapterofthe
AssociationforComputationalLinguisticsandthe12thInternationalJointConferenceonNaturalLanguageProcessing,
AACL/IJCNLP2022-Volume1:LongPapers,OnlineOnly,November20-23,2022.82–92.
[44] YifuGao,LinboQiao,ZhigangKan,ZhihuaWen,YongquanHe,andDongshengLi.2024. Two-stageGenerative
QuestionAnsweringonTemporalKnowledgeGraphUsingLargeLanguageModels. arXiv:2402.16568[cs.CL]
https://arxiv.org/abs/2402.16568
[45] YunfanGao,YunXiong,XinyuGao,KangxiangJia,JinliuPan,YuxiBi,YiDai,JiaweiSun,MengWang,andHaofen
Wang.2024. Retrieval-AugmentedGenerationforLargeLanguageModels:ASurvey. arXiv:2312.10997[cs.CL]
https://arxiv.org/abs/2312.10997
[46] AashishGhimire,JamesPrather,andJohnEdwards.2024. GenerativeAIinEducation:AStudyofEducators’
Awareness,Sentiments,andInfluencingFactors. arXiv:2403.15586[cs.AI] https://arxiv.org/abs/2403.15586
[47] YuGu,SueKase,MichelleVanni,BrianM.Sadler,PercyLiang,XifengYan,andYuSu.2021. BeyondI.I.D.:Three
LevelsofGeneralizationforQuestionAnsweringonKnowledgeBases.InWWW’21:TheWebConference2021,Virtual
Event/Ljubljana,Slovenia,April19-23,2021.3477–3488.
[48] YuGuandYuSu.2022.ArcaneQA:DynamicProgramInductionandContextualizedEncodingforKnowledgeBase
QuestionAnswering.InProceedingsofthe29thInternationalConferenceonComputationalLinguistics.1718–1731.
[49] JiayanGuo,LunDu,HengyuLiu,MengyuZhou,XinyiHe,andShiHan.2023.GPT4Graph:CanLargeLanguage
ModelsUnderstandGraphStructuredData?AnEmpiricalEvaluationandBenchmarking. arXiv:2305.15066[cs.AI]
https://arxiv.org/abs/2305.15066
[50] Tiezheng Guo, Qingwen Yang, Chen Wang, Yanyi Liu, Pan Li, Jiawei Tang, Dapeng Li, and Yingyou Wen.

### KnowledgeNavigator:LeveragingLargeLanguageModelsforEnhancedReasoningoverKnowledgeGraph.

arXiv:2312.15880[cs.CL] https://arxiv.org/abs/2312.15880
[51] BernalJiménezGutiérrez,YihengShu,YuGu,MichihiroYasunaga,andYuSu.2024.HippoRAG:Neurobiologically
InspiredLong-TermMemoryforLargeLanguageModels. arXiv:2405.14831[cs.CL] https://arxiv.org/abs/2405.14831
[52] WilliamL.Hamilton,ZhitaoYing,andJureLeskovec.2017.InductiveRepresentationLearningonLargeGraphs.In
AdvancesinNeuralInformationProcessingSystems30:AnnualConferenceonNeuralInformationProcessingSystems
2017,December4-9,2017,LongBeach,CA,USA.1024–1034.
[53] ZhenHan,YueFeng,andMingmingSun.2023.AGraph-GuidedReasoningApproachforOpen-endedCommonsense
QuestionAnswering. arXiv:2303.10395[cs.CL] https://arxiv.org/abs/2303.10395
[54] GaoleHe,YunshiLan,JingJiang,WayneXinZhao,andJi-RongWen.2021.ImprovingMulti-hopKnowledgeBase
QuestionAnsweringbyLearningIntermediateSupervisionSignals.InWSDM’21,TheFourteenthACMInternational
ConferenceonWebSearchandDataMining,VirtualEvent,Israel,March8-12,2021.553–561.
J.ACM,Vol.37,No.4,Article111.Publicationdate:September2024.

<!-- Page 34 -->

111:34 Pengetal.
[55] XiaoxinHe,YijunTian,YifeiSun,NiteshV.Chawla,ThomasLaurent,YannLeCun,XavierBresson,andBryanHooi.

## G-Retriever:Retrieval-AugmentedGenerationforTextualGraphUnderstandingandQuestionAnswering.

arXiv:2402.07630[cs.LG] https://arxiv.org/abs/2402.07630
[56] MichaelHimsolt.1996.GML:GraphModellingLanguage.UniversityofPassau(1996).
[57] JohannesHoffart,MohamedAmirYosef,IlariaBordino,HagenFürstenau,ManfredPinkal,MarcSpaniol,Bilyana
Taneva,StefanThater,andGerhardWeikum.2011.RobustDisambiguationofNamedEntitiesinText.InProceedingsof
the2011ConferenceonEmpiricalMethodsinNaturalLanguageProcessing,EMNLP2011,27-31July2011,JohnMcIntyre
ConferenceCentre,Edinburgh,UK,AmeetingofSIGDAT,aSpecialInterestGroupoftheACL.782–792.
[58] YuntongHu,ZhihanLei,ZhengZhang,BoPan,ChenLing,andLiangZhao.2024.GRAG:GraphRetrieval-Augmented
Generation. arXiv:2405.16506[cs.LG] https://arxiv.org/abs/2405.16506
[59] YuchengHuandYuxingLu.2024.RAGandRAU:ASurveyonRetrieval-AugmentedLanguageModelinNatural
LanguageProcessing. arXiv:2404.19543[cs.CL] https://arxiv.org/abs/2404.19543
[60] ZiniuHu,YichongXu,WenhaoYu,ShuohangWang,ZiyiYang,ChenguangZhu,Kai-WeiChang,andYizhouSun.

### EmpoweringLanguageModelswithKnowledgeGraphReasoningforOpen-DomainQuestionAnswering.In

Proceedingsofthe2022ConferenceonEmpiricalMethodsinNaturalLanguageProcessing,EMNLP2022,AbuDhabi,
UnitedArabEmirates,December7-11,2022.9562–9581.
[61] LeiHuang,WeijiangYu,WeitaoMa,WeihongZhong,ZhangyinFeng,HaotianWang,QianglongChen,WeihuaPeng,
XiaochengFeng,BingQin,andTingLiu.2023. ASurveyonHallucinationinLargeLanguageModels:Principles,
Taxonomy,Challenges,andOpenQuestions. arXiv:2311.05232[cs.CL] https://arxiv.org/abs/2311.05232
[62] YizhengHuangandJimmyHuang.2024.ASurveyonRetrieval-AugmentedTextGenerationforLargeLanguage
Models. arXiv:2404.10981[cs.IR] https://arxiv.org/abs/2404.10981
[63] YongfengHuang,YanyangLi,YichongXu,LinZhang,RuyiGan,JiaxingZhang,andLiweiWang.2023.MVP-Tuning:
Multi-ViewKnowledgeRetrievalwithPromptTuningforCommonsenseReasoning.InProceedingsofthe61stAnnual
MeetingoftheAssociationforComputationalLinguistics(Volume1:LongPapers),ACL2023,Toronto,Canada,July9-14,
2023.13417–13432.
[64] JenaD.Hwang,ChandraBhagavatula,RonanLeBras,JeffDa,KeisukeSakaguchi,AntoineBosselut,andYejin
Choi.2021. (Comet-)Atomic2020:OnSymbolicandNeuralCommonsenseKnowledgeGraphs.InThirty-Fifth
AAAIConferenceonArtificialIntelligence,AAAI2021,Thirty-ThirdConferenceonInnovativeApplicationsofArtificial
Intelligence,IAAI2021,TheEleventhSymposiumonEducationalAdvancesinArtificialIntelligence,EAAI2021,Virtual
Event,February2-9,2021.6384–6392.
[65] GautierIzacardandEdouardGrave.2021.LeveragingPassageRetrievalwithGenerativeModelsforOpenDomain
QuestionAnswering.InProceedingsofthe16thConferenceoftheEuropeanChapteroftheAssociationforComputational
Linguistics:MainVolume,EACL2021,Online,April19-23,2021.874–880.
[66] OmidJafari,PreetiMaurya,ParthNagarkar,KhandkerMushfiqulIslam,andChidambaramCrushev.2021.ASurvey
onLocalitySensitiveHashingAlgorithmsandtheirApplications. arXiv:2102.08942[cs.DB] https://arxiv.org/abs/
2102.08942
[67] JinhaoJiang,KunZhou,ZicanDong,KemingYe,XinZhao,andJi-RongWen.2023.StructGPT:AGeneralFramework
forLargeLanguageModeltoReasonoverStructuredData.InProceedingsofthe2023ConferenceonEmpiricalMethods
inNaturalLanguageProcessing,EMNLP2023,Singapore,December6-10,2023.9237–9251.
[68] JinhaoJiang,KunZhou,Ji-RongWen,andWayneXinZhao.2022. $GreatTruthsareAlwaysSimple:$ARather
SimpleKnowledgeEncoderforEnhancingtheCommonsenseReasoningCapacityofPre-TrainedModels.InFindings
oftheAssociationforComputationalLinguistics:NAACL2022,Seattle,WA,UnitedStates,July10-15,2022.1730–1741.
[69] JinhaoJiang,KunZhou,WayneXinZhao,YangSong,ChenZhu,HengshuZhu,andJi-RongWen.2024.KG-Agent:An
EfficientAutonomousAgentFrameworkforComplexReasoningoverKnowledgeGraph. arXiv:2402.11163[cs.CL]
https://arxiv.org/abs/2402.11163
[70] JinhaoJiang,KunZhou,XinZhao,andJi-RongWen.2023. UniKGQA:UnifiedRetrievalandReasoningforSolvingMulti-hopQuestionAnsweringOverKnowledgeGraph.InTheEleventhInternationalConferenceonLearning
Representations,ICLR2023,Kigali,Rwanda,May1-5,2023.
[71] JinhaoJiang,KunZhou,XinZhao,andJi-RongWen.2023. UniKGQA:UnifiedRetrievalandReasoningforSolvingMulti-hopQuestionAnsweringOverKnowledgeGraph.InTheEleventhInternationalConferenceonLearning
Representations,ICLR2023,Kigali,Rwanda,May1-5,2023.
[72] KelvinJiang,DekunWu,andHuiJiang.2019. FreebaseQA:ANewFactoidQADataSetMatchingTrivia-Style
Question-AnswerPairswithFreebase.InProceedingsofthe2019ConferenceoftheNorthAmericanChapterofthe
AssociationforComputationalLinguistics:HumanLanguageTechnologies,NAACL-HLT2019,Minneapolis,MN,USA,
June2-7,2019,Volume1(LongandShortPapers).318–323.
[73] XinkeJiang,RuizheZhang,YongxinXu,RihongQiu,YueFang,ZhiyuanWang,JinyiTang,HongxinDing,XuChu,
JunfengZhao,andYashaWang.2024.HyKGE:AHypothesisKnowledgeGraphEnhancedFrameworkforAccurate
J.ACM,Vol.37,No.4,Article111.Publicationdate:September2024.

<!-- Page 35 -->


### GraphRetrieval-AugmentedGeneration:ASurvey 111:35

andReliableMedicalLLMsResponses. arXiv:2312.15883[cs.CL] https://arxiv.org/abs/2312.15883
[74] BowenJin,GangLiu,ChiHan,MengJiang,HengJi,andJiaweiHan.2024.LargeLanguageModelsonGraphs:A
ComprehensiveSurvey. arXiv:2312.02783[cs.CL] https://arxiv.org/abs/2312.02783
[75] BowenJin,ChulinXie,JiaweiZhang,KashobKumarRoy,YuZhang,ZhengLi,RuiruiLi,XianfengTang,Suhang
Wang,YuMeng,andJiaweiHan.2024.GraphChain-of-Thought:AugmentingLargeLanguageModelsbyReasoning
onGraphs. arXiv:2404.07103[cs.CL] https://arxiv.org/abs/2404.07103
[76] DiJin,EileenPan,NassimOufattole,Wei-HungWeng,HanyiFang,andPeterSzolovits.2020.WhatDiseasedoesthis
PatientHave?ALarge-scaleOpenDomainQuestionAnsweringDatasetfromMedicalExams.arXiv:2009.13081[cs.CL]
https://arxiv.org/abs/2009.13081
[77] MandarJoshi,EunsolChoi,DanielS.Weld,andLukeZettlemoyer.2017.TriviaQA:ALargeScaleDistantlySupervised
ChallengeDatasetforReadingComprehension.InProceedingsofthe55thAnnualMeetingoftheAssociationfor
ComputationalLinguistics,ACL2017,Vancouver,Canada,July30-August4,Volume1:LongPapers.1601–1611.
[78] VladimirKarpukhin,BarlasOguz,SewonMin,PatrickS.H.Lewis,LedellWu,SergeyEdunov,DanqiChen,andWentauYih.2020.DensePassageRetrievalforOpen-DomainQuestionAnswering.InProceedingsofthe2020Conference
onEmpiricalMethodsinNaturalLanguageProcessing,EMNLP2020,Online,November16-20,2020.6769–6781.
[79] SohumKashyapetal.2024.KnowledgeGraphAssistedLargeLanguageModels.(2024).
[80] JihoKim,YeonsuKwon,YohanJo,andEdwardChoi.2023. KG-GPT:AGeneralFrameworkforReasoningon
KnowledgeGraphsUsingLargeLanguageModels.InFindingsoftheAssociationforComputationalLinguistics:EMNLP
2023,Singapore,December6-10,2023.9410–9421.
[81] JaewoongKimandMoohongMin.2024. FromRAGtoQA-RAG:IntegratingGenerativeAIforPharmaceutical
RegulatoryComplianceProcess. arXiv:2402.01717[cs.CL] https://arxiv.org/abs/2402.01717
[82] JihoKim,SungjinPark,YeonsuKwon,YohanJo,JamesThorne,andEdwardChoi.2023.FactKG:FactVerification
viaReasoningonKnowledgeGraphs.InProceedingsofthe61stAnnualMeetingoftheAssociationforComputational
Linguistics(Volume1:LongPapers),ACL2023,Toronto,Canada,July9-14,2023.16190–16206.
[83] ThomasN.KipfandMaxWelling.2017.Semi-SupervisedClassificationwithGraphConvolutionalNetworks.In5th
InternationalConferenceonLearningRepresentations,ICLR2017,Toulon,France,April24-26,2017,ConferenceTrack
Proceedings.
[84] TomKwiatkowski,JennimariaPalomaki,OliviaRedfield,MichaelCollins,AnkurP.Parikh,ChrisAlberti,Danielle
Epstein,IlliaPolosukhin,JacobDevlin,KentonLee,KristinaToutanova,LlionJones,MatthewKelcey,Ming-Wei
Chang,AndrewM.Dai,JakobUszkoreit,QuocLe,andSlavPetrov.2019.NaturalQuestions:aBenchmarkforQuestion
AnsweringResearch.Trans.Assoc.Comput.Linguistics7(2019),452–466.
[85] YunshiLan,GaoleHe,JinhaoJiang,JingJiang,WayneXinZhao,andJi-RongWen.2021. ASurveyonComplex
KnowledgeBaseQuestionAnswering:Methods,ChallengesandSolutions.InProceedingsoftheThirtiethInternational
JointConferenceonArtificialIntelligence,IJCAI2021,VirtualEvent/Montreal,Canada,19-27August2021.4483–4491.
[86] YunshiLan,GaoleHe,JinhaoJiang,JingJiang,WayneXinZhao,andJi-RongWen.2023.ComplexKnowledgeBase
QuestionAnswering:ASurvey.IEEETrans.Knowl.DataEng.35,11(2023),11196–11215.
[87] YunshiLanandJingJiang.2020. QueryGraphGenerationforAnsweringMulti-hopComplexQuestionsfrom
KnowledgeBases.InProceedingsofthe58thAnnualMeetingoftheAssociationforComputationalLinguistics,ACL
2020,Online,July5-10,2020.969–974.
[88] BrianLester,RamiAl-Rfou,andNoahConstant.2021.ThePowerofScaleforParameter-EfficientPromptTuning.In
Proceedingsofthe2021ConferenceonEmpiricalMethodsinNaturalLanguageProcessing,EMNLP2021,VirtualEvent/
PuntaCana,DominicanRepublic,7-11November,2021.3045–3059.
[89] DaweiLi,ShuYang,ZhenTan,JaeYoungBaik,SukwonYun,JosephLee,AaronChacko,BojianHou,DuyDuong-Tran,
YingDing,HuanLiu,LiShen,andTianlongChen.2024.DALK:DynamicCo-AugmentationofLLMsandKGtoanswer
Alzheimer’sDiseaseQuestionswithScientificLiterature. arXiv:2405.04819[cs.CL] https://arxiv.org/abs/2405.04819
[90] ShiyangLi,YifanGao,HaomingJiang,QingyuYin,ZhengLi,XifengYan,ChaoZhang,andBingYin.2023.Graph
ReasoningforQuestionAnsweringwithTripletRetrieval.InFindingsoftheAssociationforComputationalLinguistics:
ACL2023,Toronto,Canada,July9-14,2023.3366–3375.
[91] XiangLisaLiandPercyLiang.2021.Prefix-Tuning:OptimizingContinuousPromptsforGeneration.InProceedingsof
the59thAnnualMeetingoftheAssociationforComputationalLinguisticsandthe11thInternationalJointConferenceon
NaturalLanguageProcessing,ACL/IJCNLP2021,(Volume1:LongPapers),VirtualEvent,August1-6,2021.4582–4597.
[92] YuhanLi,ZhixunLi,PeisongWang,JiaLi,XiangguoSun,HongCheng,andJeffreyXuYu.2024.ASurveyofGraph
MeetsLargeLanguageModel:ProgressandFutureDirections. arXiv:2311.12399[cs.LG] https://arxiv.org/abs/2311.
12399
[93] Yinheng Li, Shaofei Wang, Han Ding, and Hang Chen. 2024. Large Language Models in Finance: A Survey.
arXiv:2311.10723[q-fin.GN] https://arxiv.org/abs/2311.10723
J.ACM,Vol.37,No.4,Article111.Publicationdate:September2024.

<!-- Page 36 -->

111:36 Pengetal.
[94] YihaoLi,RuZhang,andJianyiLiu.2024. AnEnhancedPrompt-BasedLLMReasoningSchemeviaKnowledge
Graph-IntegratedCollaboration. arXiv:2402.04978[cs.CL] https://arxiv.org/abs/2402.04978
[95] ZhuoyangLi,LiranDeng,HuiLiu,QiaoqiaoLiu,andJunzhaoDu.2024.UniOQA:AUnifiedFrameworkforKnowledge
GraphQuestionAnsweringwithLargeLanguageModels. arXiv:2406.02110[cs.CL] https://arxiv.org/abs/2406.02110
[96] ZijianLi,QingyanGuo,JiaweiShao,LeiSong,JiangBian,JunZhang,andRuiWang.2024.GraphNeuralNetwork
EnhancedRetrievalforQuestionAnsweringofLLMs. arXiv:2406.06572[cs.CL] https://arxiv.org/abs/2406.06572
[97] BillYuchenLin,XinyueChen,JaminChen,andXiangRen.2019.KagNet:Knowledge-AwareGraphNetworksfor
CommonsenseReasoning.InProceedingsofthe2019ConferenceonEmpiricalMethodsinNaturalLanguageProcessing
andthe9thInternationalJointConferenceonNaturalLanguageProcessing,EMNLP-IJCNLP2019,HongKong,China,
November3-7,2019.2829–2839.
[98] BillYuchenLin,ZiyiWu,YichiYang,Dong-HoLee,andXiangRen.2021.RiddleSense:ReasoningaboutRiddleQuestionsFeaturingLinguisticCreativityandCommonsenseKnowledge.InFindingsoftheAssociationforComputational
Linguistics:ACL/IJCNLP2021,OnlineEvent,August1-6,2021(FindingsofACL,Vol.ACL/IJCNLP2021).1504–1515.
[99] GuangyiLiu,YongqiZhang,YongLi,andQuanmingYao.2024. ExplorethenDetermine:AGNN-LLMSynergy
FrameworkforReasoningoverKnowledgeGraph. arXiv:2406.01145[cs.CL] https://arxiv.org/abs/2406.01145
[100] HLiuandPSingh.2004.ConceptNet—apracticalcommonsensereasoningtool-kit.BTtechnologyjournal22,4(2004),
211–226.
[101] HaochenLiu,SongWang,YaochenZhu,YushunDong,andJundongLi.2024.KnowledgeGraph-EnhancedLarge
LanguageModelsviaPathSelection.InFindingsoftheAssociationforComputationalLinguistics,ACL2024,Bangkok,
Thailandandvirtualmeeting,August11-16,2024.6311–6321.
[102] JiaweiLiu,ChengYang,ZhiyuanLu,JunzeChen,YiboLi,MengmeiZhang,TingBai,YuanFang,LichaoSun,PhilipS.
Yu,andChuanShi.2024. TowardsGraphFoundationModels:ASurveyandBeyond. arXiv:2310.11829[cs.LG]
https://arxiv.org/abs/2310.11829
[103] LeiLiu,XiaoyanYang,JunchiLei,XiaoyangLiu,YueShen,ZhiqiangZhang,PengWei,JinjieGu,ZhixuanChu,Zhan
Qin,andKuiRen.2024.ASurveyonMedicalLargeLanguageModels:Technology,Application,Trustworthiness,
andFutureDirections. arXiv:2406.03712[cs.CL] https://arxiv.org/abs/2406.03712
[104] NelsonF.Liu,KevinLin,JohnHewitt,AshwinParanjape,MicheleBevilacqua,FabioPetroni,andPercyLiang.2024.
LostintheMiddle:HowLanguageModelsUseLongContexts.Trans.Assoc.Comput.Linguistics12(2024),157–173.
[105] XiaoLiu,KaixuanJi,YichengFu,WengTam,ZhengxiaoDu,ZhilinYang,andJieTang.2022. P-Tuning:Prompt
TuningCanBeComparabletoFine-tuningAcrossScalesandTasks.InProceedingsofthe60thAnnualMeetingofthe
AssociationforComputationalLinguistics(Volume2:ShortPapers).61–68.
[106] XiaoLiu,YananZheng,ZhengxiaoDu,MingDing,YujieQian,ZhilinYang,andJieTang.2023.GPTUnderstands,
Too. arXiv:2103.10385[cs.CL] https://arxiv.org/abs/2103.10385
[107] YinhanLiu,MyleOtt,NamanGoyal,JingfeiDu,MandarJoshi,DanqiChen,OmerLevy,MikeLewis,LukeZettlemoyer,
andVeselinStoyanov.2019.RoBERTa:ARobustlyOptimizedBERTPretrainingApproach. arXiv:1907.11692[cs.CL]
https://arxiv.org/abs/1907.11692
[108] Pei-ChiLoandEe-PengLim.2023. ContextualPathRetrieval:AContextualEntityRelationEmbedding-based
Approach.ACMTrans.Inf.Syst.41,1(2023),1:1–1:38.
[109] LajanugenLogeswaran,Ming-WeiChang,KentonLee,KristinaToutanova,JacobDevlin,andHonglakLee.2019.
Zero-ShotEntityLinkingbyReadingEntityDescriptions.InProceedingsofthe57thConferenceoftheAssociationfor
ComputationalLinguistics,ACL2019,Florence,Italy,July28-August2,2019,Volume1:LongPapers.3449–3460.
[110] DanLuo,JiaweiSheng,HongboXu,LihongWang,andBinWang.2023.ImprovingComplexKnowledgeBaseQuestion
AnsweringwithRelation-AwareSubgraphRetrievalandReasoningNetwork.InInternationalJointConferenceon
NeuralNetworks,IJCNN2023,GoldCoast,Australia,June18-23,2023.1–8.
[111] HaoranLuo,HaihongE,ZichenTang,ShiyaoPeng,YikaiGuo,WentaiZhang,ChenghaoMa,GuantingDong,
MeinaSong,WeiLin,YifanZhu,andLuuAnhTuan.2024. ChatKBQA:AGenerate-then-RetrieveFramework
forKnowledgeBaseQuestionAnsweringwithFine-tunedLargeLanguageModels. arXiv:2310.08975[cs.CL]
https://arxiv.org/abs/2310.08975
[112] LinhaoLuo,Yuan-FangLi,GholamrezaHaffari,andShiruiPan.2024.ReasoningonGraphs:FaithfulandInterpretable
LargeLanguageModelReasoning. arXiv:2310.01061[cs.CL] https://arxiv.org/abs/2310.01061
[113] ShengjieMa,ChengjinXu,XuhuiJiang,MuzhiLi,HuarenQu,andJianGuo.2024.Think-on-Graph2.0:Deepand
InterpretableLargeLanguageModelReasoningwithKnowledgeGraph-guidedRetrieval. arXiv:2407.10805[cs.CL]
https://arxiv.org/abs/2407.10805
[114] XinbeiMa,YeyunGong,PengchengHe,HaiZhao,andNanDuan.2023.QueryRewritingforRetrieval-Augmented
LargeLanguageModels. arXiv:2305.14283[cs.CL] https://arxiv.org/abs/2305.14283
[115] HaitaoMao,ZhikaiChen,WenzhuoTang,JiananZhao,YaoMa,TongZhao,NeilShah,MikhailGalkin,andJiliang
Tang.2024.Position:GraphFoundationModelsAreAlreadyHere.InForty-firstInternationalConferenceonMachine
J.ACM,Vol.37,No.4,Article111.Publicationdate:September2024.

<!-- Page 37 -->

GraphRetrieval-AugmentedGeneration:ASurvey 111:37
Learning.
[116] QihengMao,ZeminLiu,ChenghaoLiu,ZhuoLi,andJianlingSun.2024.AdvancingGraphRepresentationLearning
withLargeLanguageModels:AComprehensiveSurveyofTechniques. arXiv:2402.05952[cs.LG] https://arxiv.org/
abs/2402.05952
[117] ShengyuMao,YongJiang,BoliChen,XiaoLi,PengWang,XinyuWang,PengjunXie,FeiHuang,HuajunChen,
andNingyuZhang.2024.RaFe:RankingFeedbackImprovesQueryRewritingforRAG. arXiv:2405.14431[cs.CL]
https://arxiv.org/abs/2405.14431
[118] CostasMavromatisandGeorgeKarypis.2022.ReaRev:AdaptiveReasoningforQuestionAnsweringoverKnowledge
Graphs.InFindingsoftheAssociationforComputationalLinguistics:EMNLP2022,AbuDhabi,UnitedArabEmirates,
December7-11,2022.2447–2458.
[119] CostasMavromatisandGeorgeKarypis.2024. GNN-RAG:GraphNeuralRetrievalforLargeLanguageModel
Reasoning. arXiv:2405.20139[cs.CL] https://arxiv.org/abs/2405.20139
[120] TodorMihaylov,PeterClark,TusharKhot,andAshishSabharwal.2018.CanaSuitofArmorConductElectricity?
ANewDatasetforOpenBookQuestionAnswering.InProceedingsofthe2018ConferenceonEmpiricalMethodsin
NaturalLanguageProcessing,Brussels,Belgium,October31-November4,2018.2381–2391.
[121] AlexanderH.Miller,AdamFisch,JesseDodge,Amir-HosseinKarimi,AntoineBordes,andJasonWeston.2016.
Key-ValueMemoryNetworksforDirectlyReadingDocuments.InProceedingsofthe2016ConferenceonEmpirical
MethodsinNaturalLanguageProcessing,EMNLP2016,Austin,Texas,USA,November1-4,2016.1400–1409.
[122] SeungwhanMoon,PararthShah,AnujKumar,andRajenSubba.2019. OpenDialKG:ExplainableConversational
ReasoningwithAttention-basedWalksoverKnowledgeGraphs.InProceedingsofthe57thConferenceoftheAssociation
forComputationalLinguistics,ACL2019,Florence,Italy,July28-August2,2019,Volume1:LongPapers.845–854.
[123] ChristopherMorris,NilsM.Kriege,FrankaBause,KristianKersting,PetraMutzel,andMarionNeumann.2020.TU-
Dataset:Acollectionofbenchmarkdatasetsforlearningwithgraphs.InICML2020WorkshoponGraphRepresentation
LearningandBeyond(GRL+2020).
[124] SaiMunikoti,AnuragAcharya,SrideviWagle,andSameeraHorawalavithana.2023.ATLANTIC:Structure-Aware
Retrieval-AugmentedLanguageModelforInterdisciplinaryScience. arXiv:2311.12289[cs.CL] https://arxiv.org/abs/
2311.12289
[125] YuqiNie,YaxuanKong,XiaowenDong,JohnM.Mulvey,H.VincentPoor,QingsongWen,andStefanZohren.2024.A
SurveyofLargeLanguageModelsforFinancialApplications:Progress,ProspectsandChallenges.arXiv:2406.11903[qfin.GN] https://arxiv.org/abs/2406.11903
[126] YasumasaOnoe,MichaelJ.Q.Zhang,EunsolChoi,andGregDurrett.2021.CREAK:ADatasetforCommonsense
ReasoningoverEntityKnowledge.InProceedingsoftheNeuralInformationProcessingSystemsTrackonDatasetsand
Benchmarks1,NeurIPSDatasetsandBenchmarks2021,December2021,virtual.
[127] OpenAI.2024.GPT-4TechnicalReport. arXiv:2303.08774[cs.CL] https://arxiv.org/abs/2303.08774
[128] LongOuyang,JeffreyWu,XuJiang,DiogoAlmeida,CarrollWainwright,PamelaMishkin,ChongZhang,Sandhini
Agarwal,KatarinaSlama,AlexRay,etal.2022.Traininglanguagemodelstofollowinstructionswithhumanfeedback.
Advancesinneuralinformationprocessingsystems35(2022),27730–27744.
[129] VardaanPahuja,BoshiWang,HugoLatapie,JayanthSrinivasa,andYuSu.2023.ARetrieve-and-ReadFramework
forKnowledgeGraphLinkPrediction.InProceedingsofthe32ndACMInternationalConferenceonInformationand
KnowledgeManagement,CIKM2023,Birmingham,UnitedKingdom,October21-25,2023.1992–2002.
[130] JeffZ.Pan,SimonRazniewski,Jan-ChristophKalo,SnehaSinghania,JiaoyanChen,StefanDietze,HajiraJabeen,Janna
Omeliyanenko,WenZhang,MatteoLissandrini,RussaBiswas,GerarddeMelo,AngelaBonifati,EdliraVakaj,Mauro
Dragoni,andDamienGraux.2023.LargeLanguageModelsandKnowledgeGraphs:OpportunitiesandChallenges.

## Tgdk1,1(2023),2:1–2:38.

[131] ShiruiPan,LinhaoLuo,YufeiWang,ChenChen,JiapuWang,andXindongWu.2024. UnifyingLargeLanguage
ModelsandKnowledgeGraphs:ARoadmap.IEEETrans.Knowl.DataEng.36,7(2024),3580–3599.
[132] WenjunPeng,GuiyangLi,YueJiang,ZilongWang,DanOu,XiaoyiZeng,DerongXu,TongXu,andEnhongChen.

### LargeLanguageModelbasedLong-tailQueryRewritinginTaobaoSearch.InCompanionProceedingsofthe

ACMonWebConference2024,WWW2024,Singapore,Singapore,May13-17,2024.20–28.
[133] ZhuoyiPengandYiYang.2024. ConnectingtheDots:InferringPatentPhraseSimilaritywithRetrievedPhrase
Graphs. arXiv:2403.16265[cs.CL] https://arxiv.org/abs/2403.16265
[134] AleksandrPerevalov,DennisDiefenbach,RicardoUsbeck,andAndreasBoth.2022.QALD-9-plus:AMultilingual
DatasetforQuestionAnsweringoverDBpediaandWikidataTranslatedbyNativeSpeakers.In16thIEEEInternational
ConferenceonSemanticComputing,ICSC2022,LagunaHills,CA,USA,January26-28,2022.229–234.
[135] FabioPetroni,AleksandraPiktus,AngelaFan,PatrickS.H.Lewis,MajidYazdani,NicolaDeCao,JamesThorne,
YacineJernite,VladimirKarpukhin,JeanMaillard,VassilisPlachouras,TimRocktäschel,andSebastianRiedel.2021.
KILT:aBenchmarkforKnowledgeIntensiveLanguageTasks.InProceedingsofthe2021ConferenceoftheNorth
J.ACM,Vol.37,No.4,Article111.Publicationdate:September2024.

<!-- Page 38 -->

111:38 Pengetal.
AmericanChapteroftheAssociationforComputationalLinguistics:HumanLanguageTechnologies,NAACL-HLT2021,
Online,June6-11,2021.2523–2544.
[136] ZhixiaoQi,YijiongYu,MeiqiTu,JunyiTan,andYongfengHuang.2023. FoodGPT:ALargeLanguageModelin
FoodTestingDomainwithIncrementalPre-trainingandKnowledgeGraphPrompt. arXiv:2308.10173[cs.CL]
https://arxiv.org/abs/2308.10173
[137] ZileQiao,WeiYe,YongJiang,TongMo,PengjunXie,WeipingLi,FeiHuang,andShikunZhang.2024.SupportivenessbasedKnowledgeRewritingforRetrieval-augmentedLanguageModeling. arXiv:2406.08116[cs.CL] https://arxiv.
org/abs/2406.08116
[138] ColinRaffel,NoamShazeer,AdamRoberts,KatherineLee,SharanNarang,MichaelMatena,YanqiZhou,WeiLi,and
PeterJ.Liu.2020.ExploringtheLimitsofTransferLearningwithaUnifiedText-to-TextTransformer.J.Mach.Learn.
Res.21(2020),140:1–140:67.
[139] PriyankaRanadeandAnupamJoshi.2023. FABULA:IntelligenceReportGenerationUsingRetrieval-Augmented
NarrativeConstruction.InProceedingsoftheInternationalConferenceonAdvancesinSocialNetworksAnalysisand
Mining,ASONAM2023,Kusadasi,Turkey,November6-9,2023.603–610.
[140] NilsReimersandIrynaGurevych.2019.Sentence-BERT:SentenceEmbeddingsusingSiameseBERT-Networks.In
Proceedingsofthe2019ConferenceonEmpiricalMethodsinNaturalLanguageProcessingandthe9thInternationalJoint
ConferenceonNaturalLanguageProcessing,EMNLP-IJCNLP2019,HongKong,China,November3-7,2019.3980–3990.
[141] YuRong,WenbingHuang,TingyangXu,andJunzhouHuang.2020.DropEdge:TowardsDeepGraphConvolutional
NetworksonNodeClassification.In8thInternationalConferenceonLearningRepresentations,ICLR2020,AddisAbaba,
Ethiopia,April26-30,2020.
[142] MaartenSap,RonanLeBras,EmilyAllaway,ChandraBhagavatula,NicholasLourie,HannahRashkin,BrendanRoof,
NoahA.Smith,andYejinChoi.2019.ATOMIC:AnAtlasofMachineCommonsenseforIf-ThenReasoning.InThe
Thirty-ThirdAAAIConferenceonArtificialIntelligence,AAAI2019,TheThirty-FirstInnovativeApplicationsofArtificial
IntelligenceConference,IAAI2019,TheNinthAAAISymposiumonEducationalAdvancesinArtificialIntelligence,EAAI
2019,Honolulu,Hawaii,USA,January27-February1,2019.3027–3035.
[143] MaartenSap,HannahRashkin,DerekChen,RonanLeBras,andYejinChoi.2019.SocialIQA:CommonsenseReasoning
aboutSocialInteractions. arXiv:1904.09728[cs.CL] https://arxiv.org/abs/1904.09728
[144] BhaskarjitSarmah,BenikaHall,RohanRao,SunilPatel,StefanoPasquali,andDhagashMehta.2024.HybridRAG:
IntegratingKnowledgeGraphsandVectorRetrievalAugmentedGenerationforEfficientInformationExtraction.
arXiv:2408.04948[cs.CL] https://arxiv.org/abs/2408.04948
[145] ApoorvSaxena,AditayTripathi,andParthaP.Talukdar.2020. ImprovingMulti-hopQuestionAnsweringover
KnowledgeGraphsusingKnowledgeBaseEmbeddings.InProceedingsofthe58thAnnualMeetingoftheAssociation
forComputationalLinguistics,ACL2020,Online,July5-10,2020.4498–4507.
[146] PriyankaSen,AlhamFikriAji,andAmirSaffari.2022.Mintaka:AComplex,Natural,andMultilingualDatasetfor
End-to-EndQuestionAnswering.InProceedingsofthe29thInternationalConferenceonComputationalLinguistics,
COLING2022,Gyeongju,RepublicofKorea,October12-17,2022.1604–1619.
[147] AhsanShehzad,FengXia,ShaguftaAbid,CiyuanPeng,ShuoYu,DongyuZhang,andKarinVerspoor.2024.Graph
Transformers:ASurvey. arXiv:2407.09777[cs.LG] https://arxiv.org/abs/2407.09777
[148] YihengShu,ZhiweiYu,YuhanLi,BörjeF.Karlsson,TingtingMa,YuzhongQu,andChin-YewLin.2022. TIARA:
Multi-grainedRetrievalforRobustQuestionAnsweringoverLargeKnowledgeBases. arXiv:2210.12925[cs.CL]
https://arxiv.org/abs/2210.12925
[149] SaurabhSrivastava,MilindDJain,HarshitaJain,KritikJaroli,VJMayankPatel,andLKhan.2020.IOTmonitoring
binforsmartcities.In3rdSmartCitiesSymposium(SCS2020),Vol.2020.IET,533–536.
[150] FabianMSuchanek,GjergjiKasneci,andGerhardWeikum.2007.Yago:acoreofsemanticknowledge.InProceedings
ofthe16thinternationalconferenceonWorldWideWeb.697–706.
[151] HaitianSun,TaniaBedrax-Weiss,andWilliamW.Cohen.2019.PullNet:OpenDomainQuestionAnsweringwith
IterativeRetrievalonKnowledgeBasesandText.InProceedingsofthe2019ConferenceonEmpiricalMethodsinNatural
LanguageProcessingandthe9thInternationalJointConferenceonNaturalLanguageProcessing,EMNLP-IJCNLP2019,
HongKong,China,November3-7,2019.2380–2390.
[152] HaitianSun,BhuwanDhingra,ManzilZaheer,KathrynMazaitis,RuslanSalakhutdinov,andWilliamW.Cohen.2018.
OpenDomainQuestionAnsweringUsingEarlyFusionofKnowledgeBasesandText.InProceedingsofthe2018
ConferenceonEmpiricalMethodsinNaturalLanguageProcessing,Brussels,Belgium,October31-November4,2018.
4231–4242.
[153] HaoSun,YangLi,LiweiDeng,BowenLi,BinyuanHui,BinhuaLi,YunshiLan,YanZhang,andYongbinLi.2023.
HistorySemanticGraphEnhancedConversationalKBQAwithTemporalInformationModeling.InProceedingsof
the61stAnnualMeetingoftheAssociationforComputationalLinguistics(Volume1:LongPapers),ACL2023,Toronto,
Canada,July9-14,2023.3521–3533.
J.ACM,Vol.37,No.4,Article111.Publicationdate:September2024.

<!-- Page 39 -->


### GraphRetrieval-AugmentedGeneration:ASurvey 111:39

[154] JiashuoSun,ChengjinXu,LumingyuanTang,SaizhuoWang,ChenLin,YeyunGong,LionelM.Ni,Heung-Yeung
Shum,andJianGuo.2024.Think-on-Graph:DeepandResponsibleReasoningofLargeLanguageModelonKnowledge
Graph. arXiv:2307.07697[cs.CL] https://arxiv.org/abs/2307.07697
[155] LeiSun,ZhengweiTao,YoudiLi,andHiroshiArakawa.2024.ODA:Observation-DrivenAgentforintegratingLLMs
andKnowledgeGraphs. arXiv:2404.07677[cs.CL] https://arxiv.org/abs/2404.07677
[156] AlonTalmorandJonathanBerant.2018. TheWebasaKnowledge-BaseforAnsweringComplexQuestions.In
Proceedingsofthe2018ConferenceoftheNorthAmericanChapteroftheAssociationforComputationalLinguistics:
HumanLanguageTechnologies,NAACL-HLT2018,NewOrleans,Louisiana,USA,June1-6,2018,Volume1(LongPapers).
641–651.
[157] AlonTalmor,JonathanHerzig,NicholasLourie,andJonathanBerant.2019.CommonsenseQA:AQuestionAnswering
ChallengeTargetingCommonsenseKnowledge.InProceedingsofthe2019ConferenceoftheNorthAmericanChapter
oftheAssociationforComputationalLinguistics:HumanLanguageTechnologies,NAACL-HLT2019,Minneapolis,MN,
USA,June2-7,2019,Volume1(LongandShortPapers).4149–4158.
[158] DhavalTaunk,LakshyaKhanna,SiriVenkataPavanKumarKandru,VasudevaVarma,CharuSharma,andMakarand
Tapaswi.2023. GrapeQA:GRaphAugmentationandPruningtoEnhanceQuestion-Answering.InCompanion
ProceedingsoftheACMWebConference2023,WWW2023,Austin,TX,USA,30April2023-4May2023.1138–1144.
[159] KristinaToutanova,DanqiChen,PatrickPantel,HoifungPoon,PallaviChoudhury,andMichaelGamon.2015.
RepresentingTextforJointEmbeddingofTextandKnowledgeBases.InProceedingsofthe2015Conferenceon
EmpiricalMethodsinNaturalLanguageProcessing,EMNLP2015,Lisbon,Portugal,September17-21,2015.1499–1509.
[160] Hugo Touvron, Louis Martin, and et al. 2023. Llama 2: Open Foundation and Fine-Tuned Chat Models.
arXiv:2307.09288[cs.CL] https://arxiv.org/abs/2307.09288
[161] AshishVaswani,NoamShazeer,NikiParmar,JakobUszkoreit,LlionJones,AidanN.Gomez,LukaszKaiser,and
IlliaPolosukhin.2017.AttentionisAllyouNeed.InAdvancesinNeuralInformationProcessingSystems30:Annual
ConferenceonNeuralInformationProcessingSystems2017,December4-9,2017,LongBeach,CA,USA.5998–6008.
[162] PetarVeličković,GuillemCucurull,ArantxaCasanova,AdrianaRomero,PietroLiò,andYoshuaBengio.2018.Graph
AttentionNetworks. arXiv:1710.10903[stat.ML] https://arxiv.org/abs/1710.10903
[163] DennyVrandečićandMarkusKrötzsch.2014.Wikidata:afreecollaborativeknowledgebase.Commun.ACM57,10
(2014),78–85.
[164] ChaojieWang,YishiXu,ZhongPeng,ChenxiZhang,BoChen,XinrunWang,LeiFeng,andBoAn.2023.keqing:
knowledge-basedquestionansweringisanaturechain-of-thoughtmentorofLLM. arXiv:2401.00426[cs.CL]
https://arxiv.org/abs/2401.00426
[165] HengWang,ShangbinFeng,TianxingHe,ZhaoxuanTan,XiaochuangHan,andYuliaTsvetkov.2023.CanLanguage
ModelsSolveGraphProblemsinNaturalLanguage?.InAdvancesinNeuralInformationProcessingSystems36:Annual
ConferenceonNeuralInformationProcessingSystems2023,NeurIPS2023,NewOrleans,LA,USA,December10-16,2023.
[166] JinqiangWang,HuanshengNing,YiPeng,QikaiWei,DanielTesfai,WenweiMao,TaoZhu,andRunheHuang.2024.
ASurveyonLargeLanguageModelsfromGeneralPurposetoMedicalApplications:Datasets,Methodologies,and
Evaluations. arXiv:2406.10303[cs.CL] https://arxiv.org/abs/2406.10303
[167] KehengWang,FeiyuDuan,SiruiWang,PeiguangLi,YunsenXian,ChuantaoYin,WengeRong,andZhangXiong.

### Knowledge-DrivenCoT:ExploringFaithfulReasoninginLLMsforKnowledge-intensiveQuestionAnswering.

arXiv:2308.13259[cs.CL] https://arxiv.org/abs/2308.13259
[168] RuijieWang,ZhengLi,DanqingZhang,QingyuYin,TongZhao,BingYin,andTarekF.Abdelzaher.2022. RETE:
Retrieval-EnhancedTemporalEventForecastingonUnifiedQueryProductEvolutionaryGraph.InWWW’22:The
ACMWebConference2022,VirtualEvent,Lyon,France,April25-29,2022.462–472.
[169] ShenWang,TianlongXu,HangLi,ChaoliZhang,JoleenLiang,JiliangTang,PhilipS.Yu,andQingsongWen.2024.
LargeLanguageModelsforEducation:ASurveyandOutlook. arXiv:2403.18105[cs.CL] https://arxiv.org/abs/2403.
18105
[170] XintaoWang,QianwenYang,YongtingQiu,JiaqingLiang,QianyuHe,ZhouhongGu,YanghuaXiao,andWeiWang.

## KnowledGPT:EnhancingLargeLanguageModelswithRetrievalandStorageAccessonKnowledgeBases.

arXiv:2308.11761[cs.CL] https://arxiv.org/abs/2308.11761
[171] YuqiWang,BoranJiang,YiLuo,DaweiHe,PengCheng,andLiangcaiGao.2024.ReasoningonEfficientKnowledge
Paths:KnowledgeGraphGuidesLargeLanguageModelforDomainQuestionAnswering. arXiv:2404.10384[cs.CL]
https://arxiv.org/abs/2404.10384
[172] YuWang,NedimLipka,RyanA.Rossi,AlexaF.Siu,RuiyiZhang,andTylerDerr.2024.KnowledgeGraphPrompting
forMulti-DocumentQuestionAnswering.InThirty-EighthAAAIConferenceonArtificialIntelligence,AAAI2024,
Thirty-SixthConferenceonInnovativeApplicationsofArtificialIntelligence,IAAI2024,FourteenthSymposiumon
EducationalAdvancesinArtificialIntelligence,EAAI2014,February20-27,2024,Vancouver,Canada.19206–19214.
J.ACM,Vol.37,No.4,Article111.Publicationdate:September2024.

<!-- Page 40 -->

111:40 Pengetal.
[173] YaokeWang,YunZhu,WenqiaoZhang,YuetingZhuang,YunfeiLi,andSiliangTang.2024.BridgingLocalDetails
andGlobalContextinText-AttributedGraphs. arXiv:2406.12608[cs.CL] https://arxiv.org/abs/2406.12608
[174] YinweiWei,XiangWang,LiqiangNie,XiangnanHe,RichangHong,andTat-SengChua.2019. MMGCN:Multimodalgraphconvolutionnetworkforpersonalizedrecommendationofmicro-video.InProceedingsofthe27thACM
internationalconferenceonmultimedia.1437–1445.
[175] YilinWen,ZifengWang,andJimengSun.2024.MindMap:KnowledgeGraphPromptingSparksGraphofThoughts
inLargeLanguageModels. arXiv:2308.09729[cs.AI] https://arxiv.org/abs/2308.09729
[176] SondreWold,LiljaØvrelid,andErikVelldal.2023.Text-To-KGAlignment:ComparingCurrentMethodsonClassificationTasks. arXiv:2306.02871[cs.CL] https://arxiv.org/abs/2306.02871
[177] JundeWu,JiayuanZhu,andYunliQi.2024.MedicalGraphRAG:TowardsSafeMedicalLargeLanguageModelvia
GraphRetrieval-AugmentedGeneration. arXiv:2408.04187[cs.CV] https://arxiv.org/abs/2408.04187
[178] ShangyuWu,YingXiong,YufeiCui,HaolunWu,CanChen,YeYuan,LianmingHuang,XueLiu,Tei-WeiKuo,Nan
Guan,andChunJasonXue.2024. Retrieval-AugmentedGenerationforNaturalLanguageProcessing:ASurvey.
arXiv:2407.13193[cs.CL] https://arxiv.org/abs/2407.13193
[179] ShirleyWu,ShiyuZhao,MichihiroYasunaga,KexinHuang,KaidiCao,QianHuang,VassilisN.Ioannidis,Karthik
Subbian,JamesZou,andJureLeskovec.2024. STaRK:BenchmarkingLLMRetrievalonTextualandRelational
KnowledgeBases. arXiv:2404.13207[cs.IR] https://arxiv.org/abs/2404.13207
[180] TaiqiangWu,XingyuBai,WeigangGuo,WeijieLiu,SihengLi,andYujiuYang.2023. ModelingFine-grained
InformationviaKnowledge-awareHierarchicalGraphforZero-shotEntityRetrieval.InProceedingsoftheSixteenth
ACMInternationalConferenceonWebSearchandDataMining,WSDM2023,Singapore,27February2023-3March
2023.1021–1029.
[181] Yuxia Wu, Yuan Fang, and Lizi Liao. 2024. Retrieval Augmented Generation for Dynamic Graph Modeling.
arXiv:2408.14523[cs.LG] https://arxiv.org/abs/2408.14523
[182] YikeWu,NanHu,ShengBi,GuilinQi,JieRen,AnhuanXie,andWeiSong.2023. Retrieve-Rewrite-Answer:A
KG-to-TextEnhancedLLMsFrameworkforKnowledgeGraphQuestionAnswering. arXiv:2309.11206[cs.CL]
https://arxiv.org/abs/2309.11206
[183] ZhentaoXu,MarkJeromeCruz,MatthewGuevara,TieWang,ManasiDeshpande,XiaofengWang,andZhengLi.2024.
Retrieval-AugmentedGenerationwithKnowledgeGraphsforCustomerServiceQuestionAnswering.InProceedings
ofthe47thInternationalACMSIGIRConferenceonResearchandDevelopmentinInformationRetrieval,SIGIR2024,
WashingtonDC,USA,July14-18,2024.2905–2909.
[184] AnYang,BaosongYang,andetal.2024.Qwen2TechnicalReport. arXiv:2407.10671[cs.CL] https://arxiv.org/abs/
2407.10671
[185] RuiYang,HaoranLiu,EdisonMarrese-Taylor,QingchengZeng,YuHeKe,WanxinLi,LechaoCheng,QingyuChen,
JamesCaverlee,YutakaMatsuo,andIreneLi.2024.KG-Rank:EnhancingLargeLanguageModelsforMedicalQA
withKnowledgeGraphsandRankingTechniques. arXiv:2403.05881[cs.CL] https://arxiv.org/abs/2403.05881
[186] XiaoYang,KaiSun,HaoXin,YushiSun,NikitaBhalla,XiangsenChen,SajalChoudhary,RongzeDanielGui,ZiranWill
Jiang,ZiyuJiang,LingkunKong,BrianMoran,JiaqiWang,YifanEthanXu,AnYan,ChenyuYang,EtingYuan,Hanwen
Zha,NanTang,LeiChen,NicolasScheffer,YueLiu,NiravShah,RakeshWanga,AnujKumar,WentauYih,andXinLuna
Dong.2024.CRAG–ComprehensiveRAGBenchmark. arXiv:2406.04744[cs.CL] https://arxiv.org/abs/2406.04744
[187] ZhilinYang,PengQi,SaizhengZhang,YoshuaBengio,WilliamW.Cohen,RuslanSalakhutdinov,andChristopherD.
Manning.2018.HotpotQA:ADatasetforDiverse,ExplainableMulti-hopQuestionAnswering.InProceedingsofthe
2018ConferenceonEmpiricalMethodsinNaturalLanguageProcessing,Brussels,Belgium,October31-November4,
2018.2369–2380.
[188] MohammadYaniandAdilaAlfaKrisnadhi.2021.Challenges,Techniques,andTrendsofSimpleKnowledgeGraph
QuestionAnswering:ASurvey.Inf.12,7(2021),271.
[189] MichihiroYasunaga,HongyuRen,AntoineBosselut,PercyLiang,andJureLeskovec.2021.QA-GNN:Reasoningwith
LanguageModelsandKnowledgeGraphsforQuestionAnswering.InProceedingsofthe2021ConferenceoftheNorth
AmericanChapteroftheAssociationforComputationalLinguistics:HumanLanguageTechnologies,NAACL-HLT2021,
Online,June6-11,2021.535–546.
[190] RuosongYe,CaiqiZhang,RunhuiWang,ShuyuanXu,andYongfengZhang.2024.LanguageisAllaGraphNeeds.
arXiv:2308.07134[cs.CL] https://arxiv.org/abs/2308.07134
[191] XiYe,SemihYavuz,KazumaHashimoto,YingboZhou,andCaimingXiong.2021.Rng-kbqa:Generationaugmented
iterativerankingforknowledgebasequestionanswering.arXivpreprintarXiv:2109.08678(2021).
[192] Wen-tauYih,MatthewRichardson,ChristopherMeek,Ming-WeiChang,andJinaSuh.2016.TheValueofSemantic
ParseLabelingforKnowledgeBaseQuestionAnswering.InProceedingsofthe54thAnnualMeetingoftheAssociation
forComputationalLinguistics,ACL2016,August7-12,2016,Berlin,Germany,Volume2:ShortPapers.
J.ACM,Vol.37,No.4,Article111.Publicationdate:September2024.

<!-- Page 41 -->


### GraphRetrieval-AugmentedGeneration:ASurvey 111:41

[193] DonghanYu,ShengZhang,PatrickNg,HenghuiZhu,AlexanderHanboLi,JunWang,YiqunHu,WilliamYang
Wang,ZhiguoWang,andBingXiang.2023. DecAF:JointDecodingofAnswersandLogicalFormsforQuestion
AnsweringoverKnowledgeBases.InTheEleventhInternationalConferenceonLearningRepresentations,ICLR2023,
Kigali,Rwanda,May1-5,2023.
[194] DonghanYu,ChenguangZhu,YuweiFang,WenhaoYu,ShuohangWang,YichongXu,XiangRen,YimingYang,
andMichaelZeng.2022. KG-FiD:InfusingKnowledgeGraphinFusion-in-DecoderforOpen-DomainQuestion
Answering.InProceedingsofthe60thAnnualMeetingoftheAssociationforComputationalLinguistics(Volume1:Long
Papers),ACL2022,Dublin,Ireland,May22-27,2022.4961–4974.
[195] HaoYu,AoranGan,KaiZhang,ShiweiTong,QiLiu,andZhaofengLiu.2024.EvaluationofRetrieval-Augmented
Generation:ASurvey. arXiv:2405.07437[cs.CL] https://arxiv.org/abs/2405.07437
[196] JingZhang,XiaokangZhang,JifanYu,JianTang,JieTang,CuipingLi,andHongChen.2022.SubgraphRetrieval
EnhancedModelforMulti-hopKnowledgeBaseQuestionAnswering.InProceedingsofthe60thAnnualMeetingof
theAssociationforComputationalLinguistics(Volume1:LongPapers),ACL2022,Dublin,Ireland,May22-27,2022.
5773–5784.
[197] MengmeiZhang,MingweiSun,PengWang,ShenFan,YanhuMo,XiaoxiaoXu,HongLiu,ChengYang,andChuan
Shi.2024.GraphTranslator:AligningGraphModeltoLargeLanguageModelforOpen-endedTasks.InProceedingsof
theACMonWebConference2024,WWW2024,Singapore,May13-17,2024.1003–1014.
[198] QinggangZhang,JunnanDong,HaoChen,DaochenZha,ZailiangYu,andXiaoHuang.2024.KnowGPT:Knowledge
GraphbasedPromptingforLargeLanguageModels. arXiv:2312.06185[cs.CL] https://arxiv.org/abs/2312.06185
[199] XikunZhang,AntoineBosselut,MichihiroYasunaga,HongyuRen,PercyLiang,ChristopherD.Manning,andJure
Leskovec.2022.GreaseLM:GraphREASoningEnhancedLanguageModels.InTheTenthInternationalConferenceon
LearningRepresentations,ICLR2022,VirtualEvent,April25-29,2022.
[200] YuyuZhang,HanjunDai,ZornitsaKozareva,AlexanderJ.Smola,andLeSong.2018. VariationalReasoningfor
QuestionAnsweringWithKnowledgeGraph.InProceedingsoftheThirty-SecondAAAIConferenceonArtificial
Intelligence,(AAAI-18),the30thinnovativeApplicationsofArtificialIntelligence(IAAI-18),andthe8thAAAISymposium
onEducationalAdvancesinArtificialIntelligence(EAAI-18),NewOrleans,Louisiana,USA,February2-7,2018.6069–6076.
[201] JiananZhao,LeZhuo,YikangShen,MengQu,KaiLiu,MichaelBronstein,ZhaochengZhu,andJianTang.2023.
GraphText:GraphReasoninginTextSpace. arXiv:2310.01089[cs.CL] https://arxiv.org/abs/2310.01089
[202] PenghaoZhao,HailinZhang,QinhanYu,ZhengrenWang,YuntengGeng,FangchengFu,LingYang,Wentao
Zhang, Jie Jiang, and Bin Cui. 2024. Retrieval-Augmented Generation for AI-Generated Content: A Survey.
arXiv:2402.19473[cs.CV] https://arxiv.org/abs/2402.19473
[203] YanxinZheng,WenshengGan,ZefengChen,ZhenlianQi,QianLiang,andPhilipS.Yu.2024.LargeLanguageModels
forMedicine:ASurvey. arXiv:2405.13055[cs.CL] https://arxiv.org/abs/2405.13055
[204] YunZhu,YaokeWang,HaizhouShi,andSiliangTang.2024. EfficientTuningandInferenceforLargeLanguage
ModelsonTextualGraphs. arXiv:2401.15569[cs.CL] https://arxiv.org/abs/2401.15569
J.ACM,Vol.37,No.4,Article111.Publicationdate:September2024.