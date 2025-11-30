---
title: "ToolExpNet Optimizing Multi Tool Selection"
original_file: "./ToolExpNet_Optimizing_Multi_Tool_Selection.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["prompt-engineering", "llm", "rag", "chain-of-thought", "react"]
keywords: ["tool", "movie", "tools", "get", "search", "similar", "page", "person", "toolexpnet", "error"]
summary: "<!-- Page 1 -->

ToolExpNet: Optimizing Multi-Tool Selection in LLMs with Similarity and

### Dependency-Aware Experience Networks

ZijingZhang1,2*,ZhanpengChen1,2*,HeZhu2,ZiyangChen1†,

### NanDu1,XiaolongLi1

1TencentHunyuan2PekingUniversity,
zijingzhang@stu.pku.edu.cn

### Abstract


### Please help me to find the final account balance

ToollearningenhancesLargeLanguageMod- from this bank statement. els’(LLMs)dynamicinteractionwithexternal
tools,improvingtheirabilitytosolvecomplex Visual Ques"
related_documents: []
---

# ToolExpNet Optimizing Multi Tool Selection

<!-- Page 1 -->

ToolExpNet: Optimizing Multi-Tool Selection in LLMs with Similarity and

### Dependency-Aware Experience Networks

ZijingZhang1,2*,ZhanpengChen1,2*,HeZhu2,ZiyangChen1†,

### NanDu1,XiaolongLi1

1TencentHunyuan2PekingUniversity,
zijingzhang@stu.pku.edu.cn

### Abstract


### Please help me to find the final account balance

ToollearningenhancesLargeLanguageMod- from this bank statement.
els’(LLMs)dynamicinteractionwithexternal
tools,improvingtheirabilitytosolvecomplex Visual Question Answering Doc Question Answering
problems.However,currentempiricalmethods, Visual Question Answering is DQA (also known as Document
the task of answering questions VQA) is the task of answering
whichprimarilyfocusonisolatedtoolslearn- based on an image. questions on document images.
ing,stillstrugglewithaccuratemulti-toolselectionduetoissueslikeconfusingsimilartools
andneglectingdependencies. Toaddressthese Too similar to distinguish... Visual Question Answering
might be the appropriate tool.
challenges, we propose the Tool Experience
Network(ToolExpNet),whichintegratestools Fail: VQA lacks the understanding of document structure and layout,
andtrial-and-errorexperiencesintoanetwork while DQA excels in comprehending document structure.
(a)
characterized by semantic similarity and dependencyrelationships. ToolExpNetiteratively
I just finished watching Titanic and I want some
conductssimulatedexperimentsusingadaptive
other movie recommendations.
samplingtoexploresubtledifferencesandconnectionsbetweentools,andsummarizesthese
experiencestoprovideinsightfulguidancefor Step1: Retrieve detailed information about the movie

### Titanic. Action: GET /movie/{movie_id}

LLMtoolselection. Ourexperimentsdemonstrate that learning the relationships between
Fail: Before using GET /movie/{movie_id}, it is necessary to use
toolshelpsachievemorecomprehensivetool GET /search/movie to retrieve the movie_id for Titanic.
learning. Evaluations on multiple real-world (b)

### APIdatasetsshowthatToolExpNeteffectively


### Figure 1: Two common failure modes in real-world

addressescommonchallengesinmulti-toolsetool invocation scenarios with existing methods: The
lection, significantly outperforming existing
topillustrationshowsanincorrecttoolselectiondueto
baselinesacrossdifferentfoundationLLMs.
semanticsimilarity,whilethebottomillustrationdemon-
1 Introduction stratesaplanningerrorduetooverlookingfunctional
dependency.

### Toollearning(Qinetal.,2024a;Quetal.,2025b)

empowers Large Language Models to dynamicallyinteractwithexternaltools,enhancingtheir typicallyconducttaskplanningandtoolselection,
problem-solving capabilities for complex tasks generating final answers based on tool execution
(Nakanoetal.,2021;Xuetal.,2023;Schicketal., results(Songetal.,2023;Shenetal.,2023).
2023; Zhao et al., 2024b). This paradigm signifi- Whiletuning-basedmethodseffectivelyenable
cantly boosts performance in knowledge acquisi- LLMstouseexternaltools(Luetal.,2023;Liang
tion (Gu et al., 2024; Schick et al., 2023), exper- etal.,2023;Qiaoetal.,2024),tuning-freemethods
tiseenhancement(Kadlcíketal.,2023;He-Yueya are irreplaceable due to their ability to learn new
et al., 2023; Bran et al., 2024), automation effi- toolswithoutparameterchangesandtheirapplicaciency(Schicketal.,2023;Yaoetal.,2022a),and bility to closed-source models (Liu et al., 2024c;
interactioncapabilities(Yangetal.,2023b;Wang Zhangetal.,2024;Liuetal.,2024b). Thesemethet al., 2024b). To invoke external tools, LLMs odsprimarilyrelyonfeedingtooldocumentation
ormemoryintotheLLM’scontexttoselectthecor-
*ThisworkisdoneduringtheinternshipatTencent.
†Correspondingauthor. recttoolsequence,highlightingtheimportanceof
15706
FindingsoftheAssociationforComputationalLinguistics:ACL2025,pages15706–15722
July27-August1,2025©2025AssociationforComputationalLinguistics

<!-- Page 2 -->

comprehensiveandaccuratetooldescriptions. Re- sampledbasedontwotypesoflinkswithadaptive
centstudieshaveimprovedtoolunderstandingby weights. Itgeneratessimulatedqueriestohighlight
rewritingdocumentation(Yuanetal.,2024;Chen functionaldifferencesanddependenciesbetween
etal.,2024)orincorporatingtrial-and-errorexperi- toolpairs,answersthesequeries,andupdatesthe
encesintothemodel’scontext(Zhaoetal.,2024a; weightsbasedonerrorrates. Inthesubsequenttool
Wang et al., 2024a; Qu et al., 2025a). However, insightrefinementstage,theLLMsummarizesthe
multi-toolselectionaccuracyremainsachallenge usage experiences of tools guided by these links,
inreal-worldcomplextasks. formingcomprehensivetoolguidancetoenhance
We observe that, with enhanced foundation thetoolselectionprocess.
model capabilities, the proportions of previously Ourcontributionsareasfollows: (1)Wepropose
identifiederrortypes(Songetal.,2023;Shietal., ToolExpNet, a novel tool network based on sim-
2024a),suchasAPIhallucinationandformatnon- ilarity and dependency relationships. It rewrites
compliance,havedecreased. However,LLMsstill toolguidancetoemphasizeinter-toolassociations,
facetwokeychallengesinselectingexternaltools: unlikeexistingmethodsfocusedonisolatedtools.
confusingsimilartoolsduetoambiguousdocumen- This approach highlights the importance of modtationandoverlookingtooldependencies. Figure1 elingtoolrelationshipsduringtoollearningphase
illustratesexamplesofthesechallenges. Previous andprovidesinsightsforfuturemethods. (2)We
workonLLMtoolunderstandinghastypicallyfo- introduceaholistictoollearningstrategythatsimcused on isolated tools (Wang et al., 2024a; Qu ulatesconfusinganddependencyqueriestoguide
etal.,2025a),neglectingpotentialinter-toolasso- LLMs through trial-and-error learning, forming
ciations in real scenarios. This limits the LLMs’ tool insights that significantly enhance the accuaccurateandcomprehensiveunderstandingoftools, racy of multi-tool invocation. (3) Through extenresultinginsuboptimalperformanceinaddressing sive experiments on multiple foundation models
thesechallenges. andreal-worlddatasets,wedemonstratethatTool-
Inspired by human cognitive learning theories ExpNetoutperformsexistingmethodsandprovide
(Smelseretal.,2001;Barsalou,2014),humansinte- anin-depthanalysisofitsmechanisms.
gratenewknowledgebyassociatingitwithexisting
knowledgesystems,formingstructuredcognitive 2 ToolExperienceNetwork
schemas. This associative mechanism is particu-
WeproposetheToolExperienceNetwork(ToolExlarly helpful in learning similar concepts, where
pNet),asshowninFigure2,whichorganizesthe
comparativeanalysisenableslearnerstograspsubavailable toolset into a network based on similartledifferencesmoreaccurately. Followingthisprinityanddependencyrelationships,facilitatingmore
ciple,wesuggestthatLLMs’toollearningstrategy
systematicandcomprehensivetoollearning.
shouldnotbelimitedtothefunctionalattributesof
individualtoolsbutshouldfocusonestablishinga
2.1 GraphStructure
networkofrelationshipsbetweentools.
Basedonthisconcept,weproposetheToolEx- Formally,wemodelthetoolecosystemasagraph
perienceNetwork(ToolExpNet),whichorganizes G = (V,E s E d ), where nodes represent indi-
∪
theavailabletoolsetandtrial-and-errorexperiences vidualtoolsandedgescapturecomplexinter-tool
intoanetworktoenhancecomprehensivetoollearn- relationships. Eachtoolnodev i V isdefinedasa
∈
ing. Specifically, ToolExpNet’s graph structure tuple(e i ,φ i ),wheree i includesAPImetadataand
includes two types of edges: semantic similar- φ i representsfunctionalinsightsdistilledthrough
ity edges (E ), which connect tools with similar LLM-basedexperiencesummarization. Theseins
functionaldescriptions,andfunctionaldependency sightscanserveasempiricalknowledgeforLLMs
edges(E ),representingthesequentialinvocation duringthetoolselectionphase. Theedgesexplicd
dependenciesbetweentools. Thisstructuresystem- itlycharacterizetwofundamentalrelationships:
aticallyaddressesthechallengesofdistinguishing SemanticSimilarityEdges(E s): Theseedges
between similar tools (via E s ) and captures the connect tool pairs (v i ,v j ) with partial functional
opportunitiesforcombiningtools(viaE ). overlap or semantically analogous descriptions,
d
ToolExpNet employs an iterative contrastive- whichmaymisleadLLMsintoconflatingtheirdisrelationtrialanderrorprocessandtoolinsightre- tinctcapabilitiesduringtoolselection.
finementtoexploretoolinteractions. Toolpairsare Functional Dependency Edges (E d): These
15707

<!-- Page 3 -->


### Simulating Confusing Queries

① Sampling links from ToolExpNet for Similar Tool-Pairs
Instruction：You need to generate a set of Actor：(a) GET /tv/polular (b) GET /tv/latest
semantic similarity links dependency links confusing questions to simulate user queries to
d T i o s o ti l n A gu : i { s / h s e b a e r t c w h e /t e v n } t h e s e T o tw ol o B s : i m { / i t l v a / r l a to te o s ls t } ...... ② Contrastive-Relation Trial and Error &
Explorer：(a).Helper me find some popular Update Tool-Usage Experience
/tv/popular /tv/latest movies related to 'science fiction'. (b). Show me
/discover/tv the newest TV show and its reviews. /tv/popular /tv/latest
/discover/tv

### Simulating Queries for Tool-

/movie/popular reco / m tv m /{t e v n _ d id a } t / ions /search/tv u s I e n r s D q t e r u u p e c e ri t n e i d s o e n to n ： t s Y S im o c u e u l n a n a t e e r e i o t d h s e t o u s g e e n o e f r th a e te f o a l lo se w t i n o g f /movie/popular reco / m tv m /{t e v n _ d id a } t / ions /search/tv
two tools to explore whether there is any
dependency between them ......
/tv/top_rated /tv/{tv_id}/similar T E o x o p l l o A r : e { r ： /se R a e rc c h o / m tv m } e | n T d o o so lB m :{ e / t T v V /{ t s v h _ o id w }/ s s i s m im ila il r a } r /tv/top_rated /tv/{tv_id}/similar
to Friends. Dep: /search/tv → /tv/{tv_id}/similar
④Update Node's Tool Usage Insights ③Summarize Each Tool's Trial-and-Error
Tool Usage Insights Experience Considering Adjacent Tools

### Experience Summary Prompt

/tv/{tv_id}/similar finds TV shows similar to a
s d p is e c c o i v fi e e r d in o g n n e e w us i i n n t g e r k e e s y ts w . o .. rds and genres, ideal for > ba Y s o e u d o n n e e e d x i t s o ti n u g p d tr a ia te l- a th n e d- u er s r a o g r e e x o p f e t r h ie e n t c o e o s l /discover/tv /tv/popular /tv/latest
In contrast, /tv/{tv_id}/recommendations offers and tool adjacency information.
personalized suggestions based on viewing history, > Target Tool: /tv/{tv_id}/similar
n U o n t l i s k t e r ic /t t v s /t i o m p i _ la r r a it t y e d .. , . which lists shows by ratings, this > /tv S /{ e tv m _ a id n } t / i r c e c s o im m il m ar e it n y d a a d ti j o a n c s ent nodes: /movie/popular reco / m tv m /{t e v n _ d id a } t / ions /search/tv
tool focuses on similarity ... > Functional dependency adjacent nodes:
The /search/tv tool is often used first to find the /tv/top_rated, /search/tv,
necessary TV show IDs for /tv/{tv_id}/similar ... /tv/{tv_id}/recommendations /tv/top_rated /tv/{tv_id}/similar
...... > Pairwise trial-and-error experiences: ......
Figure2:TheToolExpNetframeworkenhancestoolusageinsightsbyleveragingsemanticsimilarityanddependency
linkstoguidetrial-and-errorexploration. Contrastive-relationtrialanderrorexperimentssimulateuserqueries,
revealing functional differences and dependencies. These experiences update the tool’s experiential network.
Insightsfromthesetrialsupdatenodeusageprofiles,highlightingfunctionaldifferencesandinterdependencies.
Thisstructuredapproachoptimizestoolusagethroughcomprehensiverelationalunderstanding.
edgesdenoterelationshipswhereonetool’sfunc- but also by its toolset-context. Therefore, during
tionalityextendsordependsonanother. Thisoften the tool learning phase, we iterate the processes
occurswhentheinputparametersofcertainAPIs of contrastive-relation trial-and-error and tool inare reliant on the outputs from the execution of sight refinement. This iterative process, similar
otherfunctions. to how humans learn through trial and error and
Thisdual-relationalstructureenablessystematic thensummarizetheirexperiences,helpsorganize
modelingofboththeselectionchallenges(viaE ) knowledgeintostructuredcognitionandmemory.
s
and compositional opportunities (via E ) inher- The prompts for this section are provided in Apd
entintool-augmentedLLMsystems. Theexplicit pendixA.
graphformulationfacilitatesstructuredreasoning
abouttoolrelationshipswhilemaintainingcompu- 3.1 Contrastive-RelationTrialandError
tationaltractability.
Prior studies (Shinn et al., 2024; Anokhin et al.,
2024; Zhao et al., 2024a) have demonstrated the
2.2 ToolExpNetInitialization
effectiveness of LLMs in learning through trial-

### GivenatoolsetΓ,weinstantiateeachtoolasanode

and-errorexperiences. Experiencelearningserves
v V,initializingitsfunctionalinsightφ directly
i i asaplug-and-playapproach,requiringnoexplicit
∈
fromrawAPIdocumentation,evenwhensuchdocgradientupdates,makingitcompatiblewithclosedumentationisverboseorincomplete(Yuanetal.,
sourceLLMs. However,existingworktypicallyfo-
2024;Quetal.,2025a). Semanticedges(E )are
s cusesonself-explorationwithsingletools,lacking
formed between tool pairs whose documentation
structuredpreservationofcross-toolusagepatterns
embeddings exceed a similaritythreshold Φ. Deandinter-toolrelationships.
pendencyedges(E )areestablishedbetweentools
d To address this, we propose a Pairwise Explowhere the output data types of one tool overlap
rationframeworktocaptureLLMs’cross-tooloperwiththeinputdatatypesofanothertool.
ationalknowledge. Eachself-explorationiteration
generatessimulateduserqueriesandgoldensolu-
3 ToolLearningStrategy
tions for targeted tool pairs, enabling systematic
Wesuggestthattheroleofatoolwithinatoolkit trial-and-errorlearning.
is determined not only by its intrinsic properties Explorer ( ): During each iteration, the ex-

## H

15708

<!-- Page 4 -->

plorer samples a subset of edges (maximum where p is a Chain-of-Thought prompt guiding
max_try) from E and E with initial sampling the LLM to: (1) Identify capability boundaries
s d
weights w0(e ) = 1. For edge e in iteration t, bycontrastingv withV ,analyzingfailure/success
ij ij i s
thesamplingprobabilityisproportionaltowt(e ). casesinE edgestoclarifyfunctionaldistinctions.
ij s
For semantic similarity edges (E ), generates (2)Discovercompositionalpatternsbyexamining
s

## H

contrastive user queries emphasizing functional V relationships,synthesizingmulti-toolworkflows
d
distinctions between tools v and v . For depen- fromE executiontraces.
i j d
dency edges (E ), it simulates queries requiring This graph-aware reflection enables dynamic
d
sequentialtoolinvocationwhilepruningspurious evolutionoftoolunderstandingwithoutmodelredependencies. This process outputs query-label training. The updated φt+1 is subsequently used
i
pairs(Q,L) = (p,v ,v ),wherepdenotestask- asadditionalcontextualinformationtoinformthe
i j

## H

specificprompts. Here,Qrepresentsthesimulated LLM’stoolselection.
queries,andLdenotesthecorrespondinglabels.
Actor ( ): The actor attempts to answer 4 ExperimentalSetup

## A

queries using tools Γ, producing responses A =
4.1 DatasetsandEvaluationMetrics
(p,Q,Γ). Execution traces and tool selection

## A

outcomesareloggedintoedge-specificexperience Datasets. We conducted experiments on two
pools. Theerrorrate1 ACC(A,L)updatesthe widely-usedbenchmarks: RestBench (Songetal.,
−
samplingweightwt+1(e ),prioritizingchalleng- 2023) and ToolBench (Qin et al., 2024b), across
ij
ing tool pairs in subsequent iterations. The sam- three scenarios. RestBench comprises two realpling probability is then determined by normal- worldscenarioswithmanuallycuratedhigh-quality
izing the weights of all edges of the same type: data. ItincludesTMDB,featuring54movie-related
P(e ) =
w(eij)
, where E denotes the set of
APIs, and Spotify, with 40 music-related APIs.
ij w(e)
e E ToolBenchisadatasetcollectedfromtheRapidAPI
all edges of th∈e same type. This formula ensures

### P and BMTools, containing over 16,000 real APIs

that edges with higher error rates have a greater
spanningmultiplecategories. Duetobudgetconchance of being sampled in the next iteration, alstraints,wefocusedonthemostchallengingsubset
lowingthemodeltofocusonmorechallengingtool
ofToolBench,I3-Instruction,whichinvolvescompairs. Particularly, if confuses two tools with-
A plex user requests requiring multiple tools from
outexistinglinks,anewsemanticsimilaritylinkis
differentcategories.
added. Conversely,iftoolslinkedbyE showno
d
Evaluation metrics. Following Song et al.
actualdependenciesduringexecution,theedgeis
(2023);Yuanetal.(2024);Quetal.(2025a);Shi
removed.
et al. (2024b), we utilized two common metrics:
3.2 ToolInsightRefinement (1)CorrectPathRate(CP%),whichmeasuresthe
proportionofinstanceswherethemodel-generated
To systematically distill cross-tool operational
sequenceoftoolcallsincludesthegoldentoolpath
knowledge,weproposeanexperienceaggregation
as a subsequence, to assess the accuracy of the
mechanisminspiredbygraph-structuredmessage
passing. For each tool node v = (e ,φt), we model’s tool invocation. (2) Win Rate (WR%):
i i i
This metric evaluates the win rate of tool invocagather its local context from semantic neighbors
tionsequencesandplanningprocessesgeneratedby
V = v e E and dependency neighbors
s j ij s
{ | ∈ } differentmethodscomparedtoReAct. Theassess-

### V = v e E , along with their interacd k ik d

{ | ∈ } mentisconductedthroughpairwisecomparisons
tion histories. This contextualized experience is
usingaChatGPT-basedjudger.
processedthroughLLM-basedreflectiontoupdate
functionalinsightsφt+1.
i 4.2 Baselines

### Formally,theinsightrefinementprocessoperates

as: We primarily compare our method with wellestablished baselines, includint:(1) ReAct (Yao
φt+1 = Reflect p, φt v V V ,
i { j| j ∈ s ∪ d } et al., 2022b), which integrates CoT reasoning
(cid:16) Neighborinformations with action selection. It uses feedback to generate subsequent actions.(2) Easytool (Yuan et al.,
(Q| ,A,L){ez E } E
ij s d
{ | ∈ ∪ } 2024),whichaddressesissuesofinconsistency,re-
Relevanttrialexperience (cid:17) dundancy, and incompleteness in real-world tool
| {z } 15709

<!-- Page 5 -->

documentation. ItrewritesdocumentswithChat-
4% Others

### GPT and incorporates guidelines. This enhances

the Large Language Models’ understanding of 18% Dependency

### Neglect

toolfunctionalitiesandparameterrequirements.(3) Success
57%
DRAFT(Quetal.,2025a),atrial-and-error-based 13% Tool

### Misselection

approach that analyzes feedback from LLMs’ in-

### Incomplete

teractionswithexternaltoolsviathreestages: ex- 8% Invocation
periencecollection,learningfromexperience,and
Figure3: StatisticsofDifferentTypesofErrorsinthe
documentrewriting. Thismethoddynamicallyre-
ReAct Framework Based on GPT-4o on the TMDB
finestooldocumentationtopromoteadeeperun-
Dataset.
derstandingandmoreeffectiveutilizationoftools
byLLMs.

### Neglect: Ignoringdependenciesbetweenfunction

4.3 ImplementationDetails calls,leadingtoerrorsorparameterhallucinations.

### Weselectedseveralleadinglargelanguagemodels

(3)ToolMisselection: Selectingincorrectsimilar
toolsduetoambiguousdocumentationoroverlaptovalidatetheapplicabilityofourmethod. These
includethelarger-scaleGPT-4oandLLaMA3-70B,
ping functionalities. (4)Others: Miscellaneous
errors,suchasfailuresininstructionadherenceor
aswellasthesmaller-scaleQwen2.5-7B.Forthe
incorrectinvocationformats.Thestatisticsofthese
initializationofToolExpNet,wesetthesimilarity
failuresareillustratedinFigure3.
thresholdΦ = 0.8. Thetemperatureofallmodels
Wealsoobservedthatwiththeimprovementin
aresetto0.
foundation model capabilities, the proportion of
5 ResultsandAnalysis failuresduetoinstructionadherenceortoolhallucinationhasimprovedcomparedtopreviousobser-
5.1 OverallPerformance
vations(Shietal.,2024a;Songetal.,2023;Wang
We present our experimental results in Table 1. et al., 2024a). However, a substantial portion of
Our framework generally outperforms existing toolselectionfailuresstillstemmedfromneglectbaselinesacrossvariousreal-worldAPIscenarios. ingdependenciesorbeingconfusedbyambiguous
Specifically, it achieves superior performance on intentsandsimilartooldocumentation,withthese
theCPandWRmetricscomparedtotrial-and-error- twoerrortypesaccountingfor72.09%offailures
basedmethodsanddocument-driventoollearning onTMDB.AppendixBprovidesexamplesofthese
approaches. Thisindicatesbetteraccuracyintool errortypes.
selection and more effective multi-tool planning. Thisfindingsuggeststhatduringthetoollearn-
Furthermore,ourframeworkdemonstratesrobust ing phase, LLMs should place greater emphasis
adaptability to different foundation LLMs. Even onunderstandingtherelationshipsanddistinctions
when tested with a smaller model, Qwen2.5-7B, betweentoolstoenhancecomprehensionofcrosswhich has relatively limited tool comprehension tooldependenciesandsimilarities.
capabilities, it consistently delivers performance
5.3 WhyToolExpNetWorks
improvements. These improvements validate the
effectiveness of our model and suggest that our InSection5.2,wesummarizetwocommonerror
tool-learning methods, which summarize the dis- typesinLLMtoolusage. Inthissection,weexplain
tinctionsandconnectionsbetweentools,couldbe howToolExpNeteffectivelyaddressestheseissues
moreeffectiveinenhancinganLLM’sunderstand- toachieveoptimaloutcomes.
ingoftoolcapabilities. Whilemethodssuchasexperience-basedmemory(Zhaoetal.,2024a;Wangetal.,2024a)ortool
5.2 ErrorAnalysisforToolSelection
documentationrewriting(Hsiehetal.,2023;Yuan
Wemeticulouslyannotatedandanalyzedthefailure et al., 2024) have been shown to improve LLMs’
cases of the ReAct framework based on GPT-4o abilityintaskplanningandtoolselection,previous
intheTMDBtask. Thesefailuresarecategorized studiesoftenfocusonsummarizingtrial-and-error
intofourmaintypes: (1)IncompleteInvocation: processesforisolatedtools. However,inmostreal-
Missing critical tool calls due to overlooked user world complex scenarios, multiple tools must be
intents or flawed task planning. (2)Dependency invoked in a specific sequence, forming a unidi-
15710

<!-- Page 6 -->

RestBench-TMDB RestBench-Spotify ToolBench

### Model Method


## Cp% Wr% Cp% Wr% Cp% Wr%


### ReAct 72.00 50.00 49.12 50.00 41.00 50.00

EasyTool 76.00 58.00 57.89 59.65 46.00 55.00

### Llama3-70B


## Draft 86.00 59.00 66.67 63.16 53.00 61.50

ToolExpNet(Ours) 86.00 61.00 70.17 64.91 51.00 60.00

### ReAct 57.00 50.00 50.87 50.00 37.00 50.00

EasyTool 74.00 60.50 61.40 57.89 45.00 62.50

### GPT-4o


## Draft 86.00 63.00 70.17 64.91 51.00 65.00

ToolExpNet(Ours) 90.00 69.00 75.44 68.42 53.00 68.50

### ReAct 38.00 50.00 21.05 50.00 16.00 50.00

EasyTool 49.00 69.00 29.82 66.67 24.00 65.00

### Qwen-2.5-7B


## Draft 46.00 64.00 31.58 70.17 23.00 65.00


### ToolExpNet(Ours) 49.00 67.50 38.60 77.19 29.00 69.50

Table1: Performancecomparisonofdifferentmethodsacrossthreedatasets. CP%andWR%denotetheCorrect
PathRateandWinRate,respectively. ThebestresultforeachLLMishighlightedinbold.
ErrorType ReAct ToolExpNet ofedges,E s andE d ,toestablishrelationshipsbetweensimilaranddependenttools. Table2demon-

## D.N. 0.17 0.03

TMDB stratesthatourmodelsignificantlyreducestheerror

## T.M. 0.13 0.04

ratesintwocommoncategories: DependencyNe-
D.N. 0.30 0.09 glect and Tool Misselection. This indicates that

### Spotify

T.M. 0.14 0.08 ToolExpNet effectively optimizes these errors to
enhancethetool-usingcapabilitiesofLLMs.
Table 2: Proportion of two common failure types in In the self-explore stage of tool learning, tools
totalsamplecountacrossdifferentdatasetsandmethods.
withsimilarordependentfunctionsaregroupedto-

### D.N. and T.M. denote Dependency Neglect and Tool

getherfortargetedtrial-and-errorexperiences. Dur-
Misselection,respectively.
ingthereflectionandsummarystages,thesetools
arejointlyanalyzedtoidentifysubtledifferences
Method TMDB(∆SL) Spotify(∆SL) andexplorefunctionalextensionsthroughcombinationswithothertools. Thislearningprocesshelps

### ReAct +0.76 +0.53

extract insights from trial-and-error experiences,

### EasyTool +0.24 +0.25

highlighting the distinctions and connections be-

## Draft +0.22 +0.37

tweentools. Theseinsightsaretheninjectedinto

### ToolExpNet +0.17 +0.23

the LLM through in-context learning to guide its
planningandtoolselectionprocesses.

### Table 3: Comparison of ∆Solution Length (∆SL)

across different scenarios for various methods, repre- Following RestGPT (Song et al., 2023), we
sentingtheadditionalnumberofAPIcallsrelativeto adopt ∆SolutionLength(∆SL) to measure the
thegoldensolution. mean number of additional API calls required to
successfullyexecuteaninstruction:
rectional flow of information. Although revising 1 N
documentationforindividualtoolscanhelpLLMs

## ∆Sl =


## N


### Li

real−

### Li

gold ·
I(i,success)
s
betterunderstandwhenandhowtouseaparticular X i=0 (cid:0) (cid:1)
tool,itdoesnotenhancetheirabilitytodistinguish whereN isthenumberofsuccessfullycompleted
s
betweensimilartoolsorplandependenciesamong instructions,Li andLi aretheactualandgoldreal gold
toolsdirectly. Thislimitationoftenleadstotwokey standard API call counts for the i-th instruction,
errors: DependencyNeglectandToolMisselection. andI(i,success)isanindicatorfunctionthatequals
We adopt trial-and-error guided by two types 1ifthei-thinstructionissuccessfullycompleted,
15711

<!-- Page 7 -->

Tool Guidance ( /movie/{movie_id} ) Tool Invocation Sequence Model TMDB(CP) Spotify(CP)

### DRAFT ToolExpNet 90.00 75.44


### A Movie Details API allows developers to

retrieve comprehensive primary information w/oE s 85.00 70.17
about a specific movie by providing its 4 1 w/oE 83.00 63.16
unique movie_id. This includes metadata such d
as title, release date, genres, runtime, w/oTrial 82.00 70.17
production companies, languages, and m m i o s v s i i e n _ g i d 5 2
popularity. This api also supports the
append_to_response parameter, enabling no relevant 3 Table4: AblationStudyResultsonTMDBandSpotify.
information.
users to include additional related data in the
same request. ∆SL = 2

### ToolExpNet (Ours) 5.4 AblationStudy

> The ``/movie/{movie_id}`` tool retrieves
primary information about a movie, including 1 2 3
WeconductedablationstudiesonTMDBandSpoits title, overview, and ... It supports the
parameter 'append_to_response' to ... ∆SL = 0 tify,toevaluatetheimpactofdifferentcomponents
> In contrast, tools like /movie/{movie_id}/
Relevant APIs inToolExpNet. Specifically,weassessedtheconimages, /movie/{movie_id}/reviews offer
1 GET /search/movie
more specific information related to images, 2 GET /movie/{movie_id}/credits tributions of semantic similarity links E s , funcreviews... For example ...
> If the movie_id is not known, use /search/ 3 GET /person/{person_id}/images tional dependency links E d , and the contrastive-
4 GET /movie/{movie_id}
movie tool to find it first. This tool can be co
mbined with other tools like ... 5 GET /person/{person_id} relationtrial-and-errorphasetotheoverallperformance. TheresultsinTable4showthatremoving
any of these components leads to a performance

### Figure 4: Case Study: This figure compares the tool

guidanceandperformanceofDRAFTandToolExpNet drop. Tofurtherunderstandtheroleofthesecominsolvingthequery"WhatdoestheleadactorofTitanic ponents,weanalyzedhowthetoolusageinsights
look like?". DRAFT, lacking dependency modeling, generatedunderdifferentsettingsinfluencethereresultsinbacktrackingandanincreasedsequencelength sults.
(∆SL = 2). In contrast, ToolExpNet’s tool guidance
provides a detailed description of semantic similarity

### Semantic similarity links (E s) enhance the

LLM’s capacity to differentiate between simitoolsanddependencytoolstoefficientlyplanthetool
sequence,avoidingunnecessarystepsandachievingan lartools. Acomparisonofexperimentswithand
optimalsequencelength(∆SL=0). withoutE s revealsthattheabsenceofE s leadsto
a higher rate of Tool Misselection errors (4%
→
10%). WhenE isremovedfromToolExpNet,the
s
LLM, during the reflection phase, can only conotherwise0. sidertoolsdependencyrelationships. Italsocannot
leveragetheerrorexperienceswhereconfusionoc-

### We evaluate our approach on two real-world

curred between two similar tools. This hinders
datasets,TMDBandSpotify. AsshowninTable3,
thereflectiononsubtledifferencesbetweensimilar
ToolExpNetoutperformsexistingbaselinesonthe
tools,makingtheLLMmorepronetointerference
∆SL metric. This demonstrates that the insights
from similar tool documentation and more likely
generatedbyourmethodenhanceitsplanningand
to select the wrong tool during the tool selection
toolselectionprocesses,reducingunnecessaryAPI
phase.
callscausedbydependencyneglectandsubsequent
backtracking. Detailedexamplesofthisbehavior FunctionaldependencylinksE d improvethe
efficiency of tool planning. The use of certain
areprovidedinAppendixB.
tools often depends on the results obtained from
Figure4showsaconcreteexample. Itcompares other tools. This dependency may stem from the
the tool-calling process guided by our method’s inherent nature of the tools (e.g., parameter filltoolinsightswiththeprocessusingDRAFT’stool ingrelatedtoIDs)orthetasklogicimpliedbythe
documentation as context. Specifically, we com- user’s intent. When E is removed, it leads to a
d
parethetoolguidanceforthesameAPIendpoint higherrateofDependencyNeglecterrors(3%
→
movie/{movie_id}revisedbyDRAFTandToolEx- 12%). E enablestheLLMtoperformmoreeffecd
pNet,aswellastheirperformanceonagivenuser tive planning before executing a task. As shown
query. The case demonstrates that our model, by inTable3andtheexamples(Figure4),E encourd
summarizingthedistinctionsandconnectionsbe- agestheLLMtoplandependenciesbeforeinvoking
tweentoolsduringthetoollearningphase,achieves the target tool. A smaller ∆SL indicates a more
bettertaskplanningandtoolselection. efficienttoolinvocationprocess.
15712

<!-- Page 8 -->

5.5 FurtherAnalysis
52.5
50.0
47.5
45.0
1 2 3 4 5
Iterations

## )%(Pc

o4-TPGtahC
32
30
28
26
24

## )%(Pc


### B7-5.2newQ

Spotify TMDB ToolBench

## N 40 54 282

t

## N 137 108 716

e
d¯
3.45 2.00 2.54

### Table 5: Descriptive statistics of ToolExpNet: N det

notesthenumberoftoolnodes,N representsthenume berofedges,andd¯istheaveragedegree.

### ChatGPT-4o

Qwen2.5-7B 6 RelatedWork
6.1 LLMToollearning

### Recent studies have demonstrated that large lan-

Figure5: PerformanceofGPT-4oandQwen2.5-7Bon guagemodelscansignificantlyenhancetheircapatheI3subsetofToolBenchacrossdifferentiterations. bilities and tackle complex problems by leveraging external tools (Qu et al., 2025b; Shen et al.,
2023; Qin et al., 2024b). Specifically, with the

### Furthermore,wediscusstheimpactofdifferent

assistanceofexternaltools,LLMscanacquireuplearningiterrationsinthetoollearningstrategyon
to-dateinformation(Schicketal.,2023;Komeili
finalperformance. Weconductedexperimentsusetal.,2022;Gouetal.,2024),enhancetheirexperingthemodelsGPT-4oandQwen2.5-7B-Instruct
tise(Inabaetal.,2023;Branetal.,2024),andautoon the I3 subset of ToolBench. Each iteration almatevarioustasks(Schicketal.,2023;Yaoetal.,
lowsamaximumsamplesizeof100,withallpro-
2022a;Zhuangetal.,2023). Existingmethodsbe
cesses using greedy decoding. As illustrated in
broadlycategorizedintotwotypes: tuning-based
Figure 5, performance improves with more iteraandtuning-free(Quetal.,2025b). Tuning-based
tionsandsaturatesaroundthethirditeration.
methods involve further training LLMs on toolrelateddatasetstoimprovetheirtoolusagecapabilities(Liuetal.,2024a;Yangetal.,2023a;Haoetal.,
5.6 ComputationalComplexityAnalysis
2023;Patiletal.,2024). However,thesemethods
Wepresentanempiricalevaluationofthecompu- aretypicallyapplicableonlytoopen-sourcemodtationalcomplexityassociatedwithourToolExp- elsandrequiresubstantialcomputationalresources.
Netmodelinthissection. Despitetheoreticalpre- In contrast, non-fine-tuning methods rely on the
dictions that the number of edges might increase contextlearningabilityofLLMsbyprovidingtool
quadratically with the number of tools, Liu et al. documentationorasmallnumberofusageexam-
(2024b) indicates that tools typically have only a ples,enablingtheLLMstounderstandhowtouse
limited number of potential successor tools to in- thetools (Weietal.,2022;Hsiehetal.,2023;Qu
voke. Thissuggeststhatdependenciesamongtools etal.,2025a;Zhaoetal.,2024a). Thesemethods
areinherentlysparse. Ourobservationsalignwith offer greater flexibility but are prone to errors in
thisfinding,andwealsodiscoveredthatsimilari- tool selection and parameter filling due to insuftiesamongtoolsexhibitsimilarsparsity. Tofurther ficient tool understanding (Shi et al., 2024a; Qu
validatethis,weassessedthesparsityoftoolsimi- et al., 2025a). In this paper, we propose a novel
laritiesinpracticalapplications. Table5presents approach that organizes tools and trial-and-error
descriptivestatisticsforToolExpNet. Theresults experiences into a network structure to facilitate
show that even with a significant increase in the morecomprehensivetoolunderstandingbyLLMs.
numberoftools,theaveragedegreeoftoolnodes
6.2 ExperienceEnhencedLLM
remains stable across different scenarios. Specifically,intheToolBenchscenario,whichincludes Large Language Models face significant chalhundredsoftools,thecomputationalcostdoesnot lengesinmulti-toolcallingtasks(Quetal.,2025b;
explodeduetotheincreaseinrelationaledges. In- Anokhinetal.,2024). Toenhancetheperformance
stead,itgrowsproportionally. Thischaracteristic ofLLMsincomplexreal-worldtasks,researchers
makesthegraph-basedtoolstructurescalableand are exploring how to enable LLMs to learn from
mayinspirefutureresearch. theirownexperiencesandtherebystrengthentheir
15713

<!-- Page 9 -->

tool-callingcapabilities(Shinnetal.,2024;Zhao Limitations
et al., 2024a; Wang et al., 2024a). For instance,

### Althoughourmethodsignificantlyreducesthenum-

Reflexion(Shinnetal.,2024)allowsLLMstoreberoftokensintoolusageguidelinescomparedto
flectontheiractionsaftertaskcompletion,identify
redundant original documents (Yuan et al., 2024;
thecausesoffailures,andimprovesubsequentat-
Quetal.,2025a),itresultsinalargertokenlength
tempts. ExpeL(Zhaoetal.,2024a)enablesLLMs
thansingle-tool-focusedtrial-and-erroranddocutogatherexperiencesthroughtrialanderroracross
mentrewritingmethods(e.g.,+42.86%compared
multipletasks,extractlessonsfrombothsuccesses
toDRAFT(Quetal.,2025a)usingtheQwen2.5-
and failures, and use these insights to optimize
7B-Instructtokenizer). Thisincreaseisduetothe
decision-makinginsubsequenttasks. Wangetal.
detailedtooldistinctionsanddependencyinforma-
(2024a) enhance LLMs’ understanding of tools
tionthatourmethodincorporatestoenhancetool
byincorporatingtrialanderror,imagination,and
selectionandinvocationaccuracy. Whiletheseenmemory mechanisms. Other methods often inhancementsimprovetoolinvocationoutcomes,the
volve summarizing and updating tool documenlargercontextlengthmayposechallengesforLarge
tationfromtrialexperiences,transformingambigu-
Language Models with limited context windows.
ous,redundant,orincompletetooldocumentation
Futureworkwillfocusonoptimizingthegeneraintomorestructuredtoolmemorieswithmodelintionoftoolguidelinestoachievehigherinformasights(Yuanetal.,2024;Quetal.,2025a;Wuetal.,
tiondensityandexploringtheuseofrewrittentool
2024). Such approaches exhibit enhanced adaptguidelines in the tool retrieval phase (Qu et al.,
abilitytonewtools. However,priorworkhaspre-
2025b)toimproveefficiency. Theseadvancements
dominantlyfocusedonsingle-tooltrial-and-error
aimtobalancethetrade-offbetweendetailedtool
processes. Inreal-worldmulti-tooltaskscenarios,
descriptionsandthepracticalconstraintsoflarge

### LLMsarerequiredtoaccuratelyselectandexecute

languagemodels,ultimatelyenhancingtheapplicatoolsinsequencefromapoolofinterdependentand
bilityandperformanceofourmethodinreal-world
potentiallyconfusingtools(Luetal.,2023;Lietal.,
scenarios.
2023;Gaoetal.,2024). Thisraiseshigherdemands
ontheLLM’sabilitytocomprehendcross-toolinteractions. To address this, we explicitly model
two common types of tool relationships, namely
dependencyandsimilarity,toenhanceLLMs’comprehensiveunderstandingofcross-toolutilization
inreal-worldscenarios.
7 Conclusion
In this paper, we propose ToolExpNet, a novel
frameworkthatorganizestoolusageinsightsand
trial-and-error experiences into a network based
on semantic similarity and dependency relations,
addressingthelimitationsofexistingmethodsthat
focusonisolatedtoolslearning. Experimentalresultsonvariousfoundationmodelsandreal-world
datasetsdemonstratethatToolExpNetoutperforms
existingmethods,providingacomprehensiveunderstandingoftoolusageandimprovingmulti-tool
invocationaccuracy.
15714

<!-- Page 10 -->

References Cheng-YuHsieh,Si-AnChen,Chun-LiangLi,Yasuhisa

### Fujii, Alexander Ratner, Chen-Yu Lee, Ranjay Kr-

PetrAnokhin,NikitaSemenov,ArtyomSorokin,Dmitry ishna, and Tomas Pfister. 2023. Tool documenta-
Evseev,MikhailBurtsev,andEvgenyBurnaev.2024. tionenableszero-shottool-usagewithlargelanguage
Arigraph: Learning knowledge graph world mod- models. Preprint,arXiv:2308.00675.
elswithepisodicmemoryforllmagents. Preprint,
arXiv:2407.04363. Tatsuro Inaba, Hirokazu Kiyomaru, Fei Cheng, and

### SadaoKurohashi.2023. Multitool-cot: GPT-3can

LawrenceWBarsalou.2014. Cognitivepsychology: An use multiple external tools with chain of thought
overviewforcognitivescientists. PsychologyPress. prompting. InProceedingsofthe61stAnnualMeeting of the Association for Computational Linguistics(Volume2: ShortPapers), ACL2023, Toronto,

### AndresM.Bran,SamCox,OliverSchilter,CarloBal-

Canada,July9-14,2023,pages1522–1532.Associadassari,AndrewD.White,andPhilippeSchwaller.
tionforComputationalLinguistics.

## Augmentinglargelanguagemodelswithchemistrytools. Nat.Mac.Intell.,6(5):525–535.

MarekKadlcík,MichalStefánik,OndrejSotolár,and

### VlastimilMartinek.2023. Calc-xandcalcformers:

Yanfei Chen, Jinsung Yoon, Devendra Singh Sachan, Empoweringarithmeticalchain-of-thoughtthrough
QingzeWang,VincentCohen-Addad,Mohammad- interactionwithsymbolicsystems. InProceedings
Hossein Bateni, Chen-Yu Lee, and Tomas Pfister. of the 2023 Conference on Empirical Methods in

## Re-invoke: Toolinvocationrewritingforzero- Natural Language Processing, EMNLP 2023, Sinshottoolretrieval. InFindingsoftheAssociationfor gapore,December6-10,2023,pages12101–12108.

Computational Linguistics: EMNLP 2024, Miami, AssociationforComputationalLinguistics.

### Florida,USA,November12-16,2024,pages4705–


### AssociationforComputationalLinguistics. MojtabaKomeili,KurtShuster,andJasonWeston.2022.


### Internet-augmenteddialoguegeneration. InProceed-

ShenGao,ZhengliangShi,MinghangZhu,BowenFang, ingsofthe60thAnnualMeetingoftheAssociation
XinXin, PengjieRen, ZhuminChen, JunMa, and forComputationalLinguistics(Volume1: LongPa-
ZhaochunRen.2024. Confucius: Iterativetoollearn- pers),ACL2022,Dublin,Ireland,May22-27,2022,
ingfromintrospectionfeedbackbyeasy-to-difficult pages 8460–8478. Association for Computational
curriculum. InProceedingsoftheAAAIConference Linguistics.
onArtificialIntelligence,volume38,pages18030–
Minghao Li, Yingxiu Zhao, Bowen Yu, Feifan Song,
18038.
Hangyu Li, Haiyang Yu, Zhoujun Li, Fei Huang,
andYongbinLi.2023. Api-bank: Acomprehensive

### ZhibinGou,ZhihongShao,YeyunGong,YelongShen,

benchmarkfortool-augmentedllms. InProceedings
Yujiu Yang, Nan Duan, and Weizhu Chen. 2024.
ofthe2023ConferenceonEmpiricalMethodsinNat-
CRITIC:largelanguagemodelscanself-correctwith
uralLanguageProcessing,EMNLP2023,Singapore,
tool-interactive critiquing. In The Twelfth Inter-

### December6-10,2023,pages3102–3116.Association

national Conference on Learning Representations,
forComputationalLinguistics.

### ICLR2024,Vienna,Austria,May7-11,2024.Open-

Review.net. Yaobo Liang, Chenfei Wu, Ting Song, Wenshan Wu,

### Yan Xia, Yu Liu, Yang Ou, Shuai Lu, Lei Ji,

YuGu,YihengShu,HaoYu,XiaoLiu,YuxiaoDong, Shaoguang Mao, Yun Wang, Linjun Shou, Ming
JieTang,JayanthSrinivasa,HugoLatapie,andYuSu. Gong, and Nan Duan. 2023. Taskmatrix.ai: Com-

## Middlewareforllms: Toolsareinstrumental pletingtasksbyconnectingfoundationmodelswith

for language agents in complex environments. In millionsofapis. Preprint,arXiv:2303.16434.

### Proceedings of the 2024 Conference on Empirical

MethodsinNaturalLanguageProcessing,EMNLP WeiwenLiu,XuHuang,XingshanZeng,XinlongHao,
2024,Miami,FL,USA,November12-16,2024,pages Shuai Yu, Dexun Li, Shuai Wang, Weinan Gan,
7646–7663.AssociationforComputationalLinguis- ZhengyingLiu,YuanqingYu,ZezhongWang,Yuxtics. ianWang,WuNing,YutaiHou,BinWang,Chuhan

### Wu,XinzhiWang,YongLiu,YashengWang,Duyu


### Tang,DandanTu,LifengShang,XinJiang,Ruiming

ShiboHao,TianyangLiu,ZhenWang,andZhitingHu.
Tang,DefuLian,QunLiu,andEnhongChen.2024a.

## Toolkengpt: Augmenting frozen language

Toolace: Winningthepointsofllmfunctioncalling.
modelswithmassivetoolsviatoolembeddings. In
Preprint,arXiv:2409.00920.
AdvancesinNeuralInformationProcessingSystems
36: AnnualConferenceonNeuralInformationPro-
Xukun Liu, Zhiyuan Peng, Xiaoyuan Yi, Xing Xie,
cessingSystems2023,NeurIPS2023,NewOrleans,
Lirong Xiang, Yuchen Liu, and Dongkuan Xu.
LA,USA,December10-16,2023.
2024b. Toolnet: Connecting large language modelswithmassivetoolsviatoolgraph. arXivpreprint
Joy He-Yueya, Gabriel Poesia, Rose E Wang, and arXiv:2403.00839.
NoahDGoodman.2023. Solvingmathwordproblemsbycombininglanguagemodelswithsymbolic YanmingLiu,XinyuePeng,YuweiZhang,JiannanCao,
solvers. arXivpreprintarXiv:2304.09102. XuhongZhang,ShengCheng,XunWang,Jianwei
15715

<!-- Page 11 -->

Yin,andTianyuDu.2024c. Tool-planner: Dynamic TimoSchick,JaneDwivedi-Yu,RobertoDessì,Roberta
solutiontreeplanningforlargelanguagemodelwith Raileanu,MariaLomeli,EricHambro,LukeZettletoolclustering. arXivpreprintarXiv:2406.03807. moyer,NicolaCancedda,andThomasScialom.2023.

### Toolformer: Languagemodelscanteachthemselves

PanLu,BaolinPeng,HaoCheng,MichelGalley,Kai- tousetools. InAdvancesinNeuralInformationPro-
Wei Chang, Ying Nian Wu, Song-Chun Zhu, and cessingSystems36: AnnualConferenceonNeural
JianfengGao.2023. Chameleon:Plug-and-playcom- InformationProcessingSystems2023,NeurIPS2023,
positionalreasoningwithlargelanguagemodels. In NewOrleans,LA,USA,December10-16,2023.

### AdvancesinNeuralInformationProcessingSystems

36: AnnualConferenceonNeuralInformationPro- YongliangShen,KaitaoSong,XuTan,DongshengLi,
cessingSystems2023,NeurIPS2023,NewOrleans, WeimingLu,andYuetingZhuang.2023. Hugging-
LA,USA,December10-16,2023. gpt: SolvingAItaskswithchatgptanditsfriendsin
hugging face. In Advances in Neural Information
ReiichiroNakano,JacobHilton,SuchirBalaji,JeffWu, ProcessingSystems36: AnnualConferenceonNeu-
Long Ouyang, Christina Kim, Christopher Hesse, ralInformationProcessingSystems2023,NeurIPS
ShantanuJain,VineetKosaraju,WilliamSaunders, 2023, New Orleans, LA, USA, December 10 - 16,
et al. 2021. Webgpt: Browser-assisted question- 2023.
answering with human feedback. arXiv preprint
arXiv:2112.09332. Zhengliang Shi, Shen Gao, Xiuyi Chen, Yue Feng,

### LingyongYan,HaiboShi,DaweiYin,ZhuminChen,

Shishir G. Patil, Tianjun Zhang, Xin Wang, and SuzanVerberne,andZhaochunRen.2024a. Chain
JosephE.Gonzalez.2024. Gorilla: Largelanguage oftools:Largelanguagemodelisanautomaticmultimodelconnectedwithmassiveapis. InAdvancesin toollearner. arXivpreprintarXiv:2405.16533.

### NeuralInformationProcessingSystems38: Annual

Zhengliang Shi, Shen Gao, Xiuyi Chen, Yue Feng,
ConferenceonNeuralInformationProcessingSys-
LingyongYan,HaiboShi,DaweiYin,PengjieRen,
tems2024,NeurIPS2024,Vancouver,BC,Canada,
SuzanVerberne,andZhaochunRen.2024b. Learn-
December10-15,2024.
ingtousetoolsviacooperativeandinteractiveagents.
ShuofeiQiao,HonghaoGui,ChengfeiLv,Qianghuai In Findings of the Association for Computational
Jia,HuajunChen,andNingyuZhang.2024. Making Linguistics: EMNLP 2024, Miami, Florida, USA,
languagemodelsbettertoollearnerswithexecution November12-16,2024,pages10642–10657.Associfeedback. In Proceedings of the 2024 Conference ationforComputationalLinguistics.
of the North American Chapter of the Association
Noah Shinn, Federico Cassano, Ashwin Gopinath,
for Computational Linguistics: Human Language
Karthik Narasimhan, and Shunyu Yao. 2024. Re-

### Technologies(Volume1:LongPapers),NAACL2024,

flexion: Languageagentswithverbalreinforcement

### MexicoCity,Mexico,June16-21,2024,pages3550–

learning. AdvancesinNeuralInformationProcess-

### AssociationforComputationalLinguistics.

ingSystems,36.

### Yujia Qin, Shengding Hu, Yankai Lin, Weize Chen,

NeilJSmelser,PaulBBaltes,etal.2001. International

### NingDing,GanquCui,ZheniZeng,XuanheZhou,

encyclopedia of the social & behavioral sciences,
YufeiHuang,ChaojunXiao,etal.2024a. Toollearnvolume11. ElsevierAmsterdam.
ingwithfoundationmodels. ACMComputingSurveys,57(4):1–40.

### YifanSong,WeiminXiong,DaweiZhu,WenhaoWu,


### HanQian,MingboSong,HailiangHuang,ChengLi,

YujiaQin,ShihaoLiang,YiningYe,KunlunZhu,Lan
KeWang,RongYao,YeTian,andSujianLi.2023.

### Yan,YaxiLu,YankaiLin,XinCong,XiangruTang,

Restgpt:Connectinglargelanguagemodelswithreal-

### BillQian,SihanZhao,LaurenHong,RunchuTian,

worldrestfulapis. Preprint,arXiv:2306.06624.

### Ruobing Xie, Jie Zhou, Mark Gerstein, Dahai Li,

Zhiyuan Liu, and Maosong Sun. 2024b. Toolllm: Boshi Wang, Hao Fang, Jason Eisner, Benjamin Van
Facilitatinglargelanguagemodelstomaster16000+ Durme,andYuSu.2024a. Llmsintheimaginarium:
real-world apis. In The Twelfth International Con- Toollearningthroughsimulatedtrialanderror. In
ference on Learning Representations, ICLR 2024, Proceedingsofthe62ndAnnualMeetingoftheAs-
Vienna,Austria,May7-11,2024.OpenReview.net. sociationforComputationalLinguistics(Volume1:

### LongPapers),ACL2024,Bangkok,Thailand,August

Changle Qu, Sunhao Dai, Xiaochi Wei, Hengyi Cai,
11-16, 2024, pages 10583–10604. Association for
ShuaiqiangWang,DaweiYin,JunXu,andJi-Rong
ComputationalLinguistics.

### Wen.2025a. Fromexplorationtomastery: Enabling

LLMstomastertoolsviaself-driveninteractions. In Chenyu Wang, Weixin Luo, Qianyu Chen, Haonan
TheThirteenthInternationalConferenceonLearning Mai,JindiGuo,SixunDong,ZhengxinLi,LinMa,
Representations. Shenghua Gao, et al. 2024b. Tool-lmm: A large
multi-modal model for tool agent learning. arXiv
Changle Qu, Sunhao Dai, Xiaochi Wei, Hengyi Cai, preprintarXiv:2401.10727.

### ShuaiqiangWang,DaweiYin,JunXu,andJi-rong

Wen.2025b. Toollearningwithlargelanguagemod- JasonWei,XuezhiWang,DaleSchuurmans,Maarten
els: asurvey. FrontiersofComputerScience,19(8). Bosma,FeiXia,EdChi,QuocVLe,DennyZhou,
15716

<!-- Page 12 -->

etal.2022. Chain-of-thoughtpromptingelicitsrea- Symposium on Educational Advances in Artificial
soninginlargelanguagemodels. Advancesinneural Intelligence,EAAI2014,February20-27,2024,Vaninformationprocessingsystems,35:24824–24837. couver,Canada,pages19632–19642.AAAIPress.
Shirley Wu, Shiyu Zhao, Qian Huang, Kexin Huang, Yuyue Zhao, Jiancan Wu, Xiang Wang, Wei Tang,
MichihiroYasunaga,KaidiCao,VassilisNIoanni- DingxianWang,andMaartenDeRijke.2024b. Let
dis,KarthikSubbian,JureLeskovec,andJamesZou. me do it for you: Towards llm empowered recom-

## Avatar: Optimizingllmagentsfortoolusage mendationviatoollearning. InProceedingsofthe

viacontrastivereasoning. InTheThirty-eighthAn- 47th International ACM SIGIR Conference on RenualConferenceonNeuralInformationProcessing search and Development in Information Retrieval,
Systems. pages1796–1806.
Qiantong Xu, Fenglu Hong, Bo Li, Changran Hu, YuchenZhuang,YueYu,KuanWang,HaotianSun,and
ZhengyuChen,andJianZhang.2023. Onthetool ChaoZhang.2023. Toolqa: AdatasetforLLMquesmanipulation capability of open-source large lan- tionansweringwithexternaltools. InAdvancesin
guagemodels. arXivpreprintarXiv:2305.16504. NeuralInformationProcessingSystems36: Annual

### ConferenceonNeuralInformationProcessingSys-

RuiYang,LinSong,YanweiLi,SijieZhao,YixiaoGe,
tems2023, NeurIPS2023, NewOrleans, LA,USA,
XiuLi,andYingShan.2023a. Gpt4tools: Teaching
December10-16,2023.
largelanguagemodeltousetoolsviaself-instruction.
InAdvancesinNeuralInformationProcessingSystems36: AnnualConferenceonNeuralInformation
Processing Systems 2023, NeurIPS 2023, New Orleans,LA,USA,December10-16,2023.
Zhengyuan Yang, Linjie Li, Jianfeng Wang, Kevin

### Lin,EhsanAzarnasab,FaisalAhmed,ZichengLiu,

Ce Liu, Michael Zeng, and Lijuan Wang. 2023b.
Mm-react: Prompting chatgpt for multimodal reasoningandaction. Preprint,arXiv:2303.11381.
Shunyu Yao, Howard Chen, John Yang, and Karthik
Narasimhan. 2022a. Webshop: Towards scalable
real-worldwebinteractionwithgroundedlanguage
agents. InAdvancesinNeuralInformationProcessing Systems 35: Annual Conference on Neural InformationProcessingSystems2022,NeurIPS2022,
NewOrleans,LA,USA,November28-December9,
2022.
Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak
Shafran,KarthikNarasimhan,andYuanCao.2022b.
React: Synergizingreasoningandactinginlanguage
models. arXivpreprintarXiv:2210.03629.

### Siyu Yuan, Kaitao Song, Jiangjie Chen, Xu Tan,

YongliangShen, KanRen, DongshengLi, andDeqing Yang. 2024. EASYTOOL: Enhancing LLM-
basedagentswithconcisetoolinstruction. InICLR
2024 Workshop on Large Language Model (LLM)
Agents.
Yinger Zhang, Hui Cai, Xierui Song, Yicheng Chen,

### RuiSun, andJingZheng.2024. Reversechain: A

generic-ruleforllmstomastermulti-apiplanning. In
FindingsoftheAssociationforComputationalLinguistics: NAACL2024, MexicoCity, Mexico, June
16-21,2024,pages302–325.AssociationforComputationalLinguistics.
AndrewZhao,DanielHuang,QuentinXu,MatthieuLin,

### Yong-JinLiu,andGaoHuang.2024a. Expel: LLM

agents are experiential learners. In Thirty-Eighth

### AAAI Conference on Artificial Intelligence, AAAI

2024,Thirty-SixthConferenceonInnovativeApplicationsofArtificialIntelligence,IAAI2024,Fourteenth
15717

<!-- Page 13 -->


### A PromptsinToolLearningStrategy

users might use these tools and generate
simulatedsubtasks. Subtasksarepartofa
Here,wepresenttheprimarypromptsusedinthe
taskplanningdecomposition.
Tool Learning Strategy. These prompts are de-
# ToolPair
signed to guide the Explorer in generating sim-

### Belowaretwopotentiallydependenttools

ulatedqueriesinvolvingpairsofsimilartools,creandtheirdescriptions:
ating queries that require multiple tools to solve
1. {tool1_info}
aproblemtoexplorepotentialdependencies,and
2. {tool2_info}
facilitatingthereflectionprocessofsummarizing
# Requirements
tool usage experience to form concise tool guid-
- Generate a set of subtasks for these two
ancethroughaChainofThoughtprocess.
tools to simulate their usage scenarios.
SimulatingConfusingQueriesforSeman- Theseproblemsmustbesolvedusingboth
ticSimilarTool-Pairs tools. Note that user requests typically do
not mention the specific name of the tool,
# Instruction
asthetoolisabstractedfromtheuser’sper-
Youhaveanopportunitytofurtherexplore
spective.
the subtle differences between the follow-
-Thegenerateduserrequestsshouldbeas
ingtwosimilartools. Youneedtoimagine
diverseaspossible,coveringdifferentusage
scenarioswhereusersmightusethesetools
scenariosandinput-outputconditions.
andproducesimulatedqueries.
-Additionally,youneedtoindicatewhether
# ToolPair
there is a parameter dependency or func-
Below are two similar tools and their detional expansion relationship between the
scriptions:
twotools,andwhethertheymustbecalled
1. {tool1_info}
insequence.
2. {tool2_info}
-Providethespecificparametersnecessary
# Requirements
forcallingtheAPI,especiallyiftheparam-
-Createadiversesetofuserrequestexameter cannot be obtained from the result of
ples (at least 5) for each tool to simulate
anyAPI.
itsusagescenarios. Notethatuserrequests
# OutputFormat
typicallydonotmentionthespecificname

### The user request examples should be a

ofthetool,asthetoolisabstractedfromthe
JSON,indicatingthesequenceoftoolcalls.
user’sperspective.

### Forexample: {output_format}

-Thegenerateduserrequestsshouldbeas
diverseaspossible,coveringdifferentusage
ProcessofToolGuidanceRefinement
scenarios.
-Thereshouldbeacertainlevelofcomplex- #Instruction
ityandpotentialforconfusionbetweenthe You need to leverage existing tools’ trialtwosetsofsimulatedqueries,highlighting and-error experience and related informathesubtledifferencesbetweenthetwotools. tion to optimize the guidance for the tool
# OutputFormat {tool_name}.

### Theoutputuserrequestexamplesshouldbe #Background

inaJSONformat,asintheexamplebelow: -Tooldocumentation: {tool_doc}
{output_example} - Potentially dependent adjacent tools:
{composition_tools}
-Functionallysimilaradjacenttools: {simi-
SimulatingQueriesforTool-Dependent
lar_tools}

### Scenarios

-Trial-and-errorexperience,eachrecordin-
# Instruction cludes the user question (question), your
Youhaveanopportunitytofurtherexplore decisionresult(pred),andthegoldenpath:
thedependenciesbetweenthefollowingtwo {trial_exp}
tools. Youneedtoimaginescenarioswhere #CoTGuideline
15718

<!-- Page 14 -->

edgeleadstoadeclineintheoverallperformance

## Analyzethesubtledifferencesbetween

ofmulti-toolinvocationandanincreaseinthefailthistoolandsimilartools,determineunder
ureraterelatedtothosespecificerrortypes. This
whatcircumstancestousewhichtool,and
indicatestheeffectiveroleofmodelinginter-tool
howtodistinguishthem.
relationshipsinfacilitatingtoollearning.

## Analyzehowthistoolformsmorecomplex functions with dependent tools and

whether it needs to depend on other tools
beforebeingcalled.

## Summarizethetypicalscenariosinwhich

thistoolisusedinuserrequests.

## Rewriteandoptimizethetool’sdescriptiontomakeitmoreconciseandclear. Remove redundancy, distinguish easily confusedtools,explaindependenciesonother

tools,andpossibleusecases.
# OutputFormat
GenerateaJSONdictionaryinthefollowingformat: {output_example}

### B ErrorTypeExamples

Table6showsspecificcasescorrespondingtoseveral types of errors in the tool selection phase of

### LLMs. Note that IDs and other parameters have

been anonymized to protect privacy. To enhance
readability, we have only presented the effective
tool invocation paths, omitting the intermediate
thoughtprocessesandretriescausedbyissuessuch
asAPIcallexceptions.

### C ToolInsightRefinementExamples

In Table 7, we present several specific examples.

### Duringthetoolinsightrefinementphase,theLLM

identifiestoolsthatsharesemanticsimilaritiesand
dependencieswiththetoolthatrequiresrefinement.

### It also reviews related trial-and-error records to

facilitate reflection and synthesis, leading to the
creationoftoolguidance.

### D AblationStudies

Table8showsthedifferencesintheinsightsformed
fortoolusageafterremovingsemanticdependency
linksanddependencylinksintheablationexperiments.

### Removingatypeofedgeimpliesthatinboththe

trial-and-error phase and the Tool Insight Refinementphase,theLLMcannotperceivethepresence
ofothertoolsthathaverelevantassociationswith
the given tool. This results in a fragmented tool
usageinsight,whereonlytheretainedtypeofconnection can be perceived. Removing any type of
15719

<!-- Page 15 -->


### ErrorType: DependencyNeglect

Question: I’mwatchingthetvseriesTheLastofUsandIneedsomemorerecommendations.
GoldenPath: "GET/search/tv" "GET/tv/{tv_id=1024}/recommendations"
→
LLMPath: "GET/tv/{tv_id=3566}/recommendations" "GET/tv/{tv_id=3566}"
→
Reason: Thefunctionof/search/tvistosearchforaTVshow,while/tv/{tv_id}retrievesashow’s
detailsbyID.TofindtheIDfor"TheLastofUs",theprocessshouldstartwith/search/tv. However,
theLLMignoredthisdependency,hallucinatedafictionaltv_id,andproducedanincorrectresult.

### ErrorType: ToolConfusion

Question: PleaserecommendmesomeTVshowssimilartoBreakingBad.
GoldenPath: "GET/search/tv" "GET/tv/{tv_id}/similar"
→
LLMPath: "GET/search/tv" "GET/tv/{tv_id}/recommendations"
→
Reason: The failure occurred because the LLM confused two similar tools. The endpoint
/tv/{tv_id}/similarisintendedtofindTVshowssimilartoagivenshowbyanalyzingkeywords
andgenres,while/tv/{tv_id}/recommendationsisusedforgettingrecommendationsbasedonthe
show’s existing data. The LLM incorrectly used the recommendations endpoint instead of the
similarendpoint.

### ErrorType: IncompleteInvocation


### Question: WhenistheleadactorofTheMandalorianborn?

GoldenPath: "GET/search/tv" "GET/tv/{tv_id}/credits" "GET/person/{person_id}"
→ →
LLMPath: "GET/search/tv" "GET/person/{person_id}"
→
Reason: TheLLMoverlookedtheuser’simplicitneedtofindtheleadactor’sinformation. This
requiredretrievingtheTVshow’screditstoidentifytheleadactor’sperson_id. Byskippingthis
step,theLLMfailedtogathersufficientinformationtocorrectlyanswerthequestion.

### ErrorType: Others

Question: AddthefirstsongofTheDarkSideoftheMooninmyplaybackqueue.
GoldenPath: "/search" "/albums/{id}/tracks" "/me/player/queue"
→ →

### LLMPath: None

Reason: TheLLMmisunderstoodthetask,producinganincorrectandunparsablecallformatthat
cannotbeexecuted.
Table6: ExamplesoffailuretypesforReActusingGPT-4oasthebackbonemodelontheTMDBandSpotify
datasets.Notethatforprivacyreasons,allsensitivefunctionparameters,suchasspecificIDs,havebeenanonymized.
Theparametersintheexamplesarefictional. Placeholderssuchas{id}representspecificparameters.
15720

<!-- Page 16 -->

Table7: Examplesoftooltrial-and-errorexperiencesummaries. TheprocessofChain-of-Thought(CoT)reflection
andforminginsightfultoolguidanceduringthetoolinsightrefinementstage.

### ToolName: /search/collection

>Semanticsimilarity: The/search/collectiontoolisusedtosearchforcollectionsbasedonatextquery,
whichisusefulwhenyoudon´thavespecificcollectionIDs. Incontrast,/collection/{collection_id}and
/collection/{collection_id}/imagesareusedwhenyoualreadyknowthecollectionIDandneeddetailed
informationorimagesforthatspecificcollection. Use/search/collectiontofindcollectionsbykeywords,
andusetheothertwotoolstogetdetailedinformationorimagesonceyouhavethecollectionID.
>Dependencyandcomposition: Toperformacomprehensivesearchandretrievedetailedinformation
about collections, you can first use /search/collection to find collections based on a query. Once you
havethecollectionIDsfromthesearchresults,youcanuse/collection/{collection_id}togetdetailed
informationabouteachcollectionand/collection/{collection_id}/imagestogetimagesassociatedwith
thecollections. Typically,userscanprovidethequeryfor/search/collection,buttheywillneedtousethe
searchresultstoobtainthecollectionIDsrequiredfortheothertwotools.
>Examples: 1. Iwanttofindcollectionsrelatedtomodernart. 2. Ineeddetailedinformationaboutthe
collectionwithA.3. CanyoushowmetheimagesforthecollectionwithA?
>Toolguidance: The/search/collectiontoolallowsyoutosearchforcollectionsusingatextquery. This
tool is particularly useful when you do not have specific collection IDs and need to find collections
based on keywords. The query parameter is required and should be URI encoded. You can also
specify the page number for paginated results. Once you have the collection IDs from the search
results,youcanuse/collection/{collection_id}togetdetailedinformationaboutaspecificcollectionand
/collection/{collection_id}/imagestoretrieveimagesassociatedwiththatcollection.

### ToolName: /movie/{movie_id}/similar

> Semantic similarity: The /movie/{movie_id}/similar tool is specifically designed to fetch a list of
movies that are similar to a given movie based on keywords and genres. This is different from the
/movie/{movie_id}/keywordstool,whichonlyretrievesthekeywordsassociatedwithamovie,andthe
/search/movietool,whichallowsforabroadersearchofmoviesbasedonatextqueryandvariousfilters.
The/movie/{movie_id}toolprovidescomprehensiveinformationaboutaspecificmovie,butdoesnot
focusonfindingsimilarmovies.
>Dependencyandcomposition: Tousethe/movie/{movie_id}/similartooleffectively,youmayneed
tofirstretrievethemovieIDusingthe/search/movietoolifyoudonotalreadyhaveit. Onceyouhave
the movie ID, you can use it to get similar movies. This tool does not directly depend on other tools,
butcombiningitwith/movie/{movie_id}/keywordscanprovideadeeperunderstandingofwhycertain
moviesareconsideredsimilar.
>Examples: 1. CanyoushowmemoviessimilartoInception? (First,use/search/movietofindthemovie
IDforInception,thenuse/movie/{movie_id}/similarwiththeobtainedID)

## IwanttofindmovieslikeTheMatrix. Whataresomerecommendations? (First,use/search/movieto

gettheIDforTheMatrix,thenuse/movie/{movie_id}/similarwiththeobtainedID)
>Toolguidance: Fetchalistofmoviessimilartoaspecifiedmoviebasedonkeywordsandgenres. This
toolisdistinctfromtherecommendationsystemandfocusesonsimilarityintermsofcontent. Tousethis
tool,youneedthemovieID,whichcanbeobtainedusingthe/search/movietoolifnotalreadyknown.
Theresponseincludesapaginatedlistofsimilarmovies. Exampleusage: "FindmoviessimilartoThe
Godfather."
15721

<!-- Page 17 -->

ToolExpNetw/oE
s

### ToolName:/person/{person_id}

Experience Insights:Retrieve primary details of a person using their ID. This tool supports
the /append_to_response parameter for additional data. It can be used in conjunction with
other tools like /search/person to find the person ID, and /person/{person_id}/tv_credits, /person/{person_id}/movie_credits,and/person/{person_id}/imagesformoredetailedinformation.
Recentupdatesincludetheadditionofthe/known_for_departmentfieldandsupportfortranslations.
Cases: The tool /person/{person_id} can be used in combination with other tools to provide
comprehensivedetailsaboutaperson. Forinstance,togetaperson’sTVshowcredits,youcan
use/person/{person_id}/tv_credits. Ifyouneedtofindaperson’sID,youcanuse/search/person
withaqueryparametertosearchforthepersonbyname. OnceyouhavethepersonID,youcan
use /person/{person_id} to getprimary details, /person/{person_id}/images toget images, and
/person/{person_id}/movie_creditstogetmoviecredits.
ToolExpNetw/oE
d

### ToolName: /movie/{movie_id}/reviews

ExperienceInsights: Fetchuserreviewsforaspecificmovieusingitsmovie_id. Thistoolallows
youtoretrievedetailedfeedbackandopinionsfromusersaboutaparticularmovie. Itisuseful
forunderstandingaudiencereceptionandsentiments. Tospecifywhichpageofreviewstoquery,
usethepageparameter. Thistoolisdistinctfrom/search/movie,whichisusedforfindingmovies
basedonsearchcriteria.
Cases: Thetool/movie/{movie_id}/reviewsisspecificallydesignedtofetchuserreviewsfora
particularmovieidentifiedbyitsmovie_id. Incontrast,the/search/movietoolisusedtosearchfor
moviesbasedonvariouscriteriasuchastitle,releaseyear,andotherfilters. While/search/movie
helpsinfindingmovies,/movie/{movie_id}/reviewsprovidesdetaileduserfeedbackforaspecific
movie. Use/movie/{movie_id}/reviewswhenyouneedtogatheropinionsandreviewsabouta
particularmovie,anduse/search/moviewhenyouneedtofindmoviesthatmatchcertainsearch
criteria.
Table8: ExamplescomparingthetoolusageexperiencesandinsightsformedbytheLLMafterremovingthetwo
differenttypesofedges,E andE fromToolExpNet.
s d
15722

## Tables

**Table (Page 1):**

| Please help me to find the final account balance from this bank statement. Visual Question Answering Doc Question Answering Visual Question Answering is DQA (also known as Document the task of answering questions VQA) is the task of answering based on an image. questions on document images. Too similar to distinguish... Visual Question Answering might be the appropriate tool. Fail: VQA lacks the understanding of document structure and layout, while DQA excels in comprehending document structure. (a) |
|---|
| I just finished watching Titanic and I want some other movie recommendations. Step1: Retrieve detailed information about the movie Titanic. Action: GET /movie/{movie_id} Fail: Before using GET /movie/{movie_id}, it is necessary to use GET /search/movie to retrieve the movie_id for Titanic. (b) |


**Table (Page 5):**

| 4% |
|---|
| 18% |
| 13% |
| 8% |


**Table (Page 7):**

| Tool Guidance ( /movie/{movie_id} ) Tool Invocation Sequence |
|---|
| DRAFT A Movie Details API allows developers to retrieve comprehensive primary information about a specific movie by providing its 4 1 unique movie_id. This includes metadata such as title, release date, genres, runtime, production companies, languages, and m m i o s v s i i e n _ g i d 5 2 popularity. This api also supports the append_to_response parameter, enabling no relevant 3 information. users to include additional related data in the same request. ∆SL = 2 |
| ToolExpNet (Ours) > The ``/movie/{movie_id}`` tool retrieves primary information about a movie, including 1 2 3 its title, overview, and ... It supports the parameter 'append_to_response' to ... ∆SL = 0 > In contrast, tools like /movie/{movie_id}/ Relevant APIs images, /movie/{movie_id}/reviews offer 1 GET /search/movie more specific information related to images, 2 GET /movie/{movie_id}/credits reviews... For example ... 3 GET /person/{person_id}/images > If the movie_id is not known, use /search/ 4 GET /movie/{movie_id} movie tool to find it first. This tool can be co mbined with other tools like ... 5 GET /person/{person_id} |
|  |


**Table (Page 7):**

| Relevant APIs 1 GET /search/movie 2 GET /movie/{movie_id}/credits 3 GET /person/{person_id}/images 4 GET /movie/{movie_id} 5 GET /person/{person_id} |  |
|---|---|
|  | GET /search/movie |
|  | GET /movie/{movie_id}/credits |
|  | GET /person/{person_id}/images |
|  | GET /movie/{movie_id} |
|  | GET /person/{person_id} |


**Table (Page 8):**

|  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  | Cha | tGPT-4o |  |
|  |  |  |  | Qwe | n2.5-7B |  |
|  |  |  |  |  |  |  |
