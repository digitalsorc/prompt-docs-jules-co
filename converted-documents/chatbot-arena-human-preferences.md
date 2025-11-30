---
title: "Chatbot Arena Human Preferences"
original_file: "./Chatbot_Arena_Human_Preferences.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["llm", "rag", "react", "agents", "fine-tuning"]
keywords: ["cid", "gpt", "page", "word", "chatbotarena", "anopenplatformforevaluatingllmsbyhumanpreference", "turbo", "chat", "product", "game"]
summary: "<!-- Page 1 -->

Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference
Wei-LinChiang*1 LianminZheng*1 YingSheng2 AnastasiosN.Angelopoulos1 TianleLi1 DachengLi1
BanghuaZhu1 HaoZhang3 MichaelI.Jordan1 JosephE.Gonzalez1 IonStoica1
Abstract Question Source

### Static Live


### LargeLanguageModels(LLMs)haveunlocked

Evaluation Ground Truth MMLU, HellaSwag, GSM-8K Codeforces Weekly Contests
newcapabilitiesandapplications;however,evalu- Metric Human Preference MT-Bench, AlpacaEval C"
related_documents: []
---

# Chatbot Arena Human Preferences

<!-- Page 1 -->

Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference
Wei-LinChiang*1 LianminZheng*1 YingSheng2 AnastasiosN.Angelopoulos1 TianleLi1 DachengLi1
BanghuaZhu1 HaoZhang3 MichaelI.Jordan1 JosephE.Gonzalez1 IonStoica1
Abstract Question Source

### Static Live


### LargeLanguageModels(LLMs)haveunlocked

Evaluation Ground Truth MMLU, HellaSwag, GSM-8K Codeforces Weekly Contests
newcapabilitiesandapplications;however,evalu- Metric Human Preference MT-Bench, AlpacaEval Chatbot Arena
atingthealignmentwithhumanpreferencesstill

### Figure1.Classification of LLM benchmarks: We categorize

posessignificant challenges. To addressthisisalong twodimensions: whetherthe questionsare froma static
sue, we introduce Chatbot Arena, an open platdatasetoralive, freshsource, andwhethertheevaluationmetformforevaluatingLLMsbasedonhumanprefricreliesongroundtruthor(approximated)humanpreferences.
erences. Our methodology employs a pairwise MMLU(Hendrycksetal.,2020),HellaSwag(Zellersetal.,2019),
comparison approach and leverages input from GSM-8K(Cobbeetal.,2021),MT-Bench(Zhengetal.,2023b),
adiverseuserbasethroughcrowdsourcing. The andAlpacaEval(Lietal.,2023)arecommonexamplesofstatic
platformhasbeenoperationalforseveralmonths, benchmarks. Chatbot Arena is the platform introduced in this
amassingover240Kvotes. Thispaperdescribes paper.
theplatform,analyzesthedatawehavecollected
sofar,andexplainsthetried-and-truestatistical
preferencesinreal-world,open-endedtasks.
methodsweareusingforefficientandaccurate
evaluation and ranking of models. We confirm ToassesstheperformanceofLLMs,theresearchcommunity
thatthecrowdsourcedquestionsaresufficiently hasintroducedavarietyofbenchmarks. Thesebenchmarks
diverse and discriminating and that the crowd- canbecategorizedbasedontwofactors: thesourceofquessourcedhumanvotesareingoodagreementwith tions(eitherstaticorlive)andtheevaluationmetric(either
thoseofexpertraters. Theseanalysescollectively groundtruthorhumanpreference). Accordingtothesefacestablish a robust foundation for the credibility tors,benchmarkscanbeclassifiedintofourcategories,as
of Chatbot Arena. Because of its unique value showninFigure1. Whilearangeofbenchmarksisbenefiand openness, Chatbot Arena has emerged as cial,themostprevalentcurrentmethodforevaluatingLLMs
one of the most referenced LLM leaderboards, remainsastatic,ground-truth-basedevaluation,partlybewidely cited by leading LLM developers and causesuchevaluationsareinexpensiveandreproducible.
companies. Our demo is publicly available at
However,thesestatic,ground-truth-basedbenchmarksexhttps://chat.lmsys.org.
hibitseverallimitations. Firstly,thequestionswithinthese
benchmarks are not open-ended, hindering the ability to
capturetheflexibleandinteractiveusefoundinreal-world

## Introduction

settings (Zheng et al., 2023b). Secondly, the test sets in
thesebenchmarksarestatic,meaningtheycanbecomecon-

### Recent advancements in large language models (LLMs)

taminated over time, which undermines the reliability of
havesignificantlyexpandedtheircapabilitiesbeyondtraditheevaluationresults(Yangetal.,2023). Furthermore,for
tionalnaturallanguageprocessingboundaries,addressinga
manycomplextasks,establishingadefinitivegroundtruth
broadarrayofgeneraltasks(OpenAI,2023;Geminietal.,
isnotonlychallengingbutsometimesunattainable. Conse-
2023;Touvronetal.,2023).Thesedevelopmentsunderscore
quently,currentbenchmarksfailtoadequatelyaddressthe
thepotentialofLLMsbutalsohaveraisedconcernswithreneedsofstate-of-the-artLLMs,particularlyinevaluating
specttoperformanceevaluation. Currentbenchmarksoften
userpreferences. Thus,thereisanurgentnecessityforan
failtocapturethenuancedanddiverseaspectsofthesemodopen,liveevaluationplatformbasedonhumanpreference
els, particularly in assessing their alignment with human
thatcanmoreaccuratelymirrorreal-worldusage.
*Equalcontribution 1UCBerkeley2Stanford3UCSD.Corre-
Creatingsuchabenchmarkplatformentailssignificantchalspondenceto:Wei-LinChiang<weichiang@berkeley.edu>.
lenges. Itrequiresthecollectionoflive,fresh,anddiverse
userquestionstoaccuratelyrepresentreal-worldscenarios.
1
4202
raM
7
]IA.sc[
1v23140.3042:viXra

<!-- Page 2 -->

ChatbotArena:AnOpenPlatformforEvaluatingLLMsbyHumanPreference
Additionally,developingscalable,incremental,andefficient • Weconductanin-depthanalysisofthecollecteddata,
rankingsystemsisessentialforevaluatingalargenumber including prompt diversity, quality, vote quality, and
ofmodels. Moreover,ensuringthequalityofhumanevalua- insightsonhumanfeedback.
tionsiscrucialgiventhenoisynatureofhumanpreferences.
• Wewillpubliclyreleaseahumanpreferencedatasetwith
Tothisend,weintroduceChatbotArena,abenchmarking over100KpairwisevotescollectedfromChatbotArena.
platformforLLMsthatfeaturesanonymous,randomized
• Wedesignanefficientsamplingalgorithmthatactively
battlesinacrowdsourcedsetting. ChatbotArenaisafree
chooseswhichmodelpairstoshow,suchthatoursample
websiteopentoallusers.1 Onthiswebsite,ausercanaska
efficiencyimproves,sometimestoalargedegree.
questionandgetanswersfromtwoanonymousLLMs. Afterward,theusercastsavoteforthemodelthatdeliversthe

## RelatedWork

preferredresponse,withthemodels’identitiesrevealedonly
aftervoting. Thiscrowdsourcedmethodeffectivelygathers

### LLMBenchmarks. WebrieflyreviewthecommonLLM

adiversearrayoffreshuserprompts,accuratelyreflecting
benchmarks,followingtheclassificationpresentedinFigreal-world LLM applications. Armed with this data, we
ure1. Themostprevalentbenchmarksarestatic,groundemployasuiteofpowerfulstatisticaltechniques,ranging
truth-basedones,typicallyintheformofmultiple-choice
fromthestatisticalmodelofBradley&Terry(1952)tothe
questionsorquestion-answeringtaskswithpredefinedan-

### E-valuesofVovk&Wang(2021),toestimatetheranking

swersandtestcases. Thesebenchmarksencompassarange
overmodelsasreliablyandsample-efficientlyaspossible.
oftopicsincludinglanguageunderstanding,mathematics,
Withthesetoolsinhand,wehavedesignedefficientsamcoding, and logical reasoning. Prominent examples in
plingalgorithmsspecificallytoselectmodelpairsinaway
this category are MMLU (Hendrycks et al., 2020), Helthatacceleratestheconvergenceofrankingswhileretaining
laSwag(Zellersetal.,2019),GSM-8K(Cobbeetal.,2021),
statisticalvalidity.

### BigBench(Srivastavaetal.,2023),AGIEval(Zhongetal.,

Weconductathoroughanalysisofthecollecteddatatoen- 2023), and HumanEval (Chen et al., 2021). Benchmarks
surethecredibilityofourplatform. Wedemonstratethat focusing on safety, such as ToxicChat (Lin et al., 2023),
theuser-generatedquestionsaresufficientlydiversetoen- andcomprehensivesuiteslikeHELM(Liangetal.,2022),
compassawiderangeofLLMusecasesandaresufficiently also exist. In addition to closed-ended questions, benchchallengingtodifferentiatebetweenmodels. Furthermore, markscanincludeopen-endedquestionsthatareevaluated
weconfirmthatthecrowd-sourcedvotesarehighlyconsis- byhumanjudgment,whichcanberatedbyexpertsorcrowd
tentwithexpertevaluations. workerssuchasAmazonMechanicalTurk(Karpinskaetal.,
2021;Gengetal.,2023;Wangetal.,2023).Therecenttrend

### WehavebeenrunningoursystemsinceApr2023andhave

includes utilizing GPT-4 for approximating human judgreceived over 240K votes from about 90K users in over
ment(Chiang&Lee,2023),withnotableinstancesbeing
100differentlanguagesasofJan2024. Toencourageuser

### MT-Bench(Zhengetal.,2023b)andAlpacaEval(Lietal.,

engagement,wehavemadeover50state-of-the-artmodels
2023). Inadditiontostaticbenchmarks,livebenchmarks
availableforfree. Wealsocollaboratewithleadingmodel
thatincludefreshquestionsarealsoavailable. Thesequesdevelopers such as OpenAI, Google, Anthropic, Mistral,
tionscanbeobtainedfromannualexamsorweeklyonline
HuggingFace,andvariousuniversities,incorporatingtheir
contestssuchasCodeforces(Lietal.,2022;Huangetal.,
latestmodelsintoourplatform. Wekeepthecommunity
2023). Theycanalsobesourcedfromhumaninteraction.
engagedbyroutinelyupdatingtheleaderboard,publishing

### Somestudieshaveexploredusinglivehumaninteractionfor

analyticalblogs,releasingdatasets,andsharinginformation
reinforcementlearningfromhumanpreference(Baietal.,
viatweets. Becauseofitsuniqueandsignificantvalue,our
2022;Ouyangetal.,2022;Touvronetal.,2023). However,
leaderboardhasemergedasoneofthemostreferencedin
thesestudiesaretypicallylimitedtospecificorganizations.
theLLMfieldandhasbecomeabenchmarkfortheindustry.
Inthispaper, weintroduceChatbotArena, thefirstopen,

### Wecommittomakingourdataandcodeavailable,ensuring

large-scale,andcrowdsourcedbenchmarkplatformthatutithatthisplatformisopen-sourceandopen-accessible.
lizeslivehumaninteraction.

### Wemakethefollowingcontributions:

RisksofStaticBenchmarks. Staticbenchmarkshavecertainissues,includingcontamination,saturation,overfitting,
• Webuildthefirstlarge-scalecrowd-sourcedliveLLM and a lack of human alignment (Yang et al., 2023; Oren
evaluationplatformwithover1Musersvisit.2
etal.,2023). DynaBench(Kielaetal.,2021)identifiesthese
challenges and recommends the use of a live benchmark
1https://chat.lmsys.org
thatincorporatesahuman-in-the-loopapproachforclassical
2ThenumberwasestimatedbyGoogleAnalyticsasofMarch

## Notethatuservisitmaynotconverttovotesasourwebsite NLPbenchmarks. Oursystemadoptsasimilarspirit. Howalsooffers“directchat”mode. ever,ourfocusisonchattingwithLLMs,andweimplement

2

<!-- Page 3 -->

ChatbotArena:AnOpenPlatformforEvaluatingLLMsbyHumanPreference
thisonasignificantlylargeruserscale. usingourservice,usersarerequiredtoaccepttermsofuse,
whichgivesustheirconsenttoreleasethedatapublicly.
Ranking System. Ranking systems have been a wellstudiedtopicinstatistics. Relatedtopicsincludeprobability

### DataStatistics

models(Hunter,2004;Rao&Kupper,1967),rankelicitation (Szörényi et al., 2015; Busa-Fekete et al., 2014a;b), We began collecting data in April 2023. As of Jan 2024,
and online experiment design (Chernoff, 1992; Karimi wehavereceivedaround240Kvotesfromover90Kusers.
etal.,2021). TheEloratingsystemhasalsobeenusedfor Ourdatainvolvesmorethan50models,includingbothpro-
LLMs(Baietal.,2022;Boubdiretal.,2023). Contributing prietarymodelslikeGPT-4, Claude, andGemini, aswell
tothisliterature,weintroducetechniquesforaccelerating as open models such as LLaMA and Mistral. These conrankingconvergenceanddetectingabnormalities,specifi- versationscovermorethan100languages,with77%being
callyappliedtolarge-scale,real-worldsettingsofLLMs. in English, 5% in Chinese, and the remaining languages,
suchasRussian,German,Spanish,French,andJapanese,
Human Preference Dataset. Owing to the significance
eachrepresentinglessthan2%ofthetotal. Eachdatapoint
ofhumanpreferences,severaldatasetsandanalysesexist
includesmulti-turnconversationsbetweentheuserandtwo
that incorporate human preferences. These include Ope-
LLMs,andavotetoindicatewhichmodeltheuserprefers.
nAssistant(Köpfetal.,2023),HH-RLHF(Baietal.,2022),

### WesummarizestatisticsinTable1alongwithotherexisting

LMSYS-Chat-1M(Zhengetal.,2023a),andsyntheticaphumanpreferencedatasets.
proximationsofhumanpreferenceslikeUltraFeedback(Cui
etal.,2023)andNectar(Zhuetal.,2023). Ourpriordata Figure10intheAppendixshowsthevotecountpermodel.
release,LMSYS-Chat-1M(Zhengetal.,2023a),issimilarly Onaverage,8Kvotesarecollectedforeachmodel. InFigcollectedviacrowdsourcing. However,LMSYS-Chat-1M ure2,weselectasetofrepresentativemodelsandpresent
comprisessolelyconversationsandlackshumanpreference theirwinrateandthenumberofbattles. Notethatweemdata,renderingitunsuitablefordirectuseinrankingstudies. ploynon-uniformsamplingtoconcentratevotesonmodel
This paper focuses on the analysis of preference data for pairs that have similar performance due to higher uncerrankingpurposes. tainty. Thishelpsusreducethenumberofvotesrequiredto
reachstableresults. Welaterdevelopanadaptivesampling

## HumanPreferenceDataCollection methodanddemonstrateitseffectivenessagainstrandom

sampling. SeeSection5forfurtheranalysis.

### In this section, we discuss our interface design to collect

To ensure anonymity, we use keywords to filter out conhumanpreferencesandpresentsummarystatistics.
versationscontainingmodelidentitysuchasmodelname
(e.g.,GPT,Claude)orcompanies(e.g.,OpenAI,Anthropic).

### Interface


### Toavoidmisuse,weadoptOpenAImoderationAPItoflag

Chatbot Arena crowd-sources feedback from users for conversationsthatcontainunsafecontent. Theflaggeduser
modelevaluation. Ourgoalistodesignanease-of-usein- requestsaccountfor3%ofthetotalrequests. Figure9in
terfacetoreducefrictionforuserstocontributedata. Since the Appendix shows the number of valid user votes over
wecollectfeedbackfrommanyusers, itisdifficulttoset time,whereweget1-2Kvotesperdayinrecentmonthsand
aconsistentgradingrubricacrossdifferentpeople. Hence, spikesasweintroducenewmodelsorleaderboardupdates.
we adopt a pairwise comparison mechanism where users
onlyneedtocomparetwomodelresponsesandvoteforthe 4.FromPairwiseComparisonstoRankings
betterone,insteadofrequiringuserstoprovideanabsolute
score. Ourdataconsistsofpairwisecomparisons—buthowcanwe
usethesecomparisonstorecoverarankingoverallM mod-

### In each battle, two anonymous models are sampled. To

els? Thisisawell-studiedtopicintheliteratureonlearning
encouragedatadiversity,wedonotpresetanyinputprompt
torank(Liuetal.,2009), andwepresentourperspective
onthewebsite. Usersarefreetoinputanyprompttothe
here. WeletA = {(m,m′) : m < m′andm,m′ ∈ [M]}
twomodels. Webelievethiscreatesincentivesforuserendenoteourcomparativedataset.
gagement, particularly given that we offer a free service.
Italsohelpsuscollectadiversesetofinputsrepresenting Weconsiderasequentialsetting,whereattimet∈N,we
real-worldusage. Aftermodelsprovidetheiranswers,user servethehumanapairofmodelsA ∈A(whichwepick),
t
compare them side-by-side and vote for the preferred an- andinturnweobservethehuman’sresponseH ∈ [0,1].
t
swer. Ifausercannotchooseinthefirstturn,theusercan Asanexample,wemighthavethatA =(1,2)andH =1,
t t
continuechattinguntilidentifyingawinner. Forthosewho indicatingthatthehumanprefersmodel2overmodel1. In
areunsure,wealsopresenttwobuttons,“tie”or“bothare theensuingtext,wewillprimarilyfocusonthebinarycase—
bad.” Figure8showsascreenshotofourinterface. Before where H ∈ {0,1}—but our approach will generalize to
t
3

<!-- Page 4 -->

ChatbotArena:AnOpenPlatformforEvaluatingLLMsbyHumanPreference
Table1.Statisticsofhumanpreferencedatasets,includingAnthropicHH(Baietal.,2022),OpenAssistantConversations(Köpfetal.,
2023),andChatbotArena(asof2024/1/21).ThetokensarecountedbyLlama2’stokenizer.“Conv”=Conversation.“Lang”=Language.

### Avg.#Turns Avg.#Tokens Avg.#Tokens

Dataset #Convs #Models #Users #Langs
perSample perPrompt perResponse

### AnthropicHH 338,704 - 143 1 2.3 18.9 78.9


### OpenAssistant 66,497 - 13,500 35 - 36.9 214.2

ChatbotArena(20240121) 243,329 50 90,051 149 1.3 94.9 269.0
Model B Model B
m m
gp t-4 -tu rb o gp t-4 -0 6 1 3 m istra l-m e d iu m
ixtra
l-8
x7 b -in stru ct-v0 .1
ge
m in i-p ro -d e v-a p i cla u d e -2 .1
gp
t-3 .5 -tu rb o -0 6 1 3 cla u d e -in sta n t-1 lla m a -2 -7 0 b -ch a t lla m a -2 -1 3 b -ch a t lla m a -2 -7 b -ch a t
m
istra l-7 b -in stru ct gp t-4 -tu rb o gp t-4 -0 6 1 3 m istra l-m e d iu m
ixtra
l-8
x7 b -in stru ct-v0 .1
ge
m in i-p ro -d e v-a p i cla u d e -2 .1
gp
t-3 .5 -tu rb o -0 6 1 3 cla u d e -in sta n t-1 lla m a -2 -7 0 b -ch a t lla m a -2 -1 3 b -ch a t lla m a -2 -7 b -ch a t
m
istra l-7 b -in stru ct
gpt-4-turbo0.000.680.69 0.750.710.76 0.770.750.76 0.790.860.90 0.9 gpt-4-turbo 0 25641189119285830531991270 141 157 106 144 3000
gpt-4-06130.320.000.50 0.590.610.59 0.590.590.62 0.720.700.80 0.8 gpt-4-06132564 0 566 263 75622271025355 414 409 264 197 2500
mistral-medium0.310.500.00 0.540.560.50 0.570.520.69 0.730.600.87 mistral-medium1189566 0 775 371 382 773 103 45 51 40 52
mixtral-8x7b-instruct-v0.10.250.410.46 0.000.540.48 0.510.560.58 0.530.730.84 0.7 mixtral-8x7b-instruct-v0.11192263 775 0 71 744 869 136 862 66 45 61
2000
M o d el
A g
g
e
p
m
t-3
in
.5
i-
-
p
tu c
ro
l r a b
-
u
d
o d
e
- e 0
v-
- 6
a
2 1
p
. 3 1
i0
0 0
.
. .
2
2 2
9
4 3
0
0 0
.
. .
3
4 4
9
1 1
0
0 0
.
. .
4
5 4
4
0 3
0
0 0
.
. .
4
5 4
6
2 9
0
0 0
.
. .
0
5 4
0
8 6
0
0 0
.
. .
4
0 5
2
0 1
0
0 0
.
. .
5
4 0
4
9 0
0
0 0
.
. .
5
5 5
5
5 6
0
0 0
.
. .
5
5 5
8
8 8
0
0 0
.
. .
6
6 6
3
1 3
0
0 0
.
. .
6
6 7
7
4 2
0
0 0
.
. .
7
7 7
6
3 1 0
0
.
.
5
6
M o d el
A g
g
e
p
m
t-3
in
.5
i-
-
p
tu c
ro
l r a b
-
u
d
o d
e
- e 0
v-
- 6
a
2 1
p
. 3 1
i
3 1
8
0 9
5
5 9
8
3 1 2 1
7
2 0
5
2 2
6
7 5
3
3 7
7
8 7
1
2 3 7 8
7
4 6
1
4 9 5 7
0
6 4 4 3
7
0 5
4
1
5
3 0
6
5
4
1 6 8
5
5 4
3
0 2 1 5
3
1 7
1
3 2 1 3
3
1 8
0
7 8 2
3
7 8
0
5 3 1 1
3
1 5
7
4 5 1500
claude-instant-10.250.410.48 0.440.450.45 0.440.000.54 0.680.650.62 0.4 claude-instant-1270 355 103 136 53 650 842 0 459 241 202 101 1000
llama-2-70b-chat0.240.380.31 0.420.420.42 0.420.460.00 0.610.580.61 0.3 llama-2-70b-chat141 414 45 862 31 113 572 459 0 383 134 369
llama-2-13b-chat0.210.280.27 0.470.370.39 0.370.320.39 0.000.530.57 llama-2-13b-chat157 409 51 66 30 117 388 241 383 0 251 621 500
llama-2-7b-chat0.140.300.40 0.270.330.36 0.280.350.42 0.470.000.52 0.2 llama-2-7b-chat106 264 40 45 30 75 283 202 134 251 0 521
mistral-7b-instruct144 197 52 61 37 114 155 101 369 621 521 0
mistral-7b-instruct0.100.200.13 0.160.240.27 0.290.380.39 0.430.480.00 0.1 0
Figure2. Win-rate(left)andbattlecount(right)betweenasubsetofmodelsinChatbotArena.
anyformoffeedback,includingthepossibilityofallowing logisticrelationship:
thehumantoexpressdifferentdegreesofpreferenceorto
1
saythemodelsaretied. P(H t =1)= 1+eξ m′−ξm , (2)
One critical goal is to estimate the win matrix: θ∗(a) = whereξisanM-lengthvectorofso-calledBTcoefficients.

## E[H

t

## |A

t
=a],foralla∈A;seetheleftpanelofFigure2
Withoutlossofgenerality,wetakeξ =0(sincethemodel
1
for an illustration of the (empirical) win matrix. In the isinvarianttoadditioninξ). Ourgoalistoestimatethepopbinary case, the a entry in the win matrix corresponds to
ulationBradley-Terrycoefficients,i.e.,thosethatminimize
the probability the human prefers model a to a when
2 1 thebinarycross-entropy:
shown the pair a. Finding the win matrix is a relatively
(cid:20) (cid:18) (cid:19)(cid:21)
1
s
d
t
e
r
t
a
a
i
i
g
ls
ht
i
f
n
or

## S

w
e
a
c
r
ti
d
on
m
5
e
.
an-estimationproblem;wewillprovide s(P)=arg
ξ
minE (A,H)∼P ℓ H,
1+eξA2 −ξA1
, (3)
Formally,considerascores(P) ∈ RM,wherePisajoint where ℓ is the binary cross-entropy loss, ℓ(h,p) =
distributionoverAandH (bydefault,wewilltargetauni- −(hlog(p)+(1−h)log(1−p)).
form distribution over A). Each model has a true score

### AlthoughtheBTmodeltechnicallyassumesaparametric

s(P) ,andbettermodelswillhavehigherscores. Inparticm formforthemodelwinrates,theseminalresultsofHuber
ular,wehavetherankofmodelm:
etal.(1967);White(1982)showthatmaximumlikelihood
(cid:88)
rank(P) =1+ 1{s(P) >s(P) }. (1) estimatorsarestillasymptoticallynormalevenwhenthese
m m′ m
assumptionsdonothold,solongastheso-called“sandwich”
m′∈[M]
covariancematrixisused;seeSection5fordetails,andsee

### Thebestmodelhasrank1. Ifthereisanothermodeltiedfor

AppendixBforanonparametricextensionoftheBradleybest,theywillbothgetassignedrank1.

### Terrymodel. Finally,weremarkthatpreviousevolutionsof

Pickingascore. Astandardscorefunctioninthissetting ouronlineinterfacehavereporteddifferentrankingscores,
isthevectorofBradley-Terry(BT)coefficients(Bradley& suchastheEloscore(Elo,1967)insteadoftheBTcoeffi-
Terry,1952). IntheBradley-Terrymodel,H ∈{0,1},and cients. WemadethischangebecausetheBTcoefficients
t
theprobabilitymodelmbeatsmodelm′ ismodeledviaa arebetterforthepurposeofstatisticalestimation.
4

<!-- Page 5 -->

ChatbotArena:AnOpenPlatformforEvaluatingLLMsbyHumanPreference

## EfficientApproximateRanking we extract an approximate ranking R = 1 +

m
(cid:80) 1{infC >supC }. Theuniformvalidityof
InSection4wedescribedhowtocalculatethewinmatrix, m′∈[M] m′ m

### C directly implies that P(∃m : R > rank(P) ) ≤ α—

score, and rank. Now we describe our estimation proce- m m
i.e., withhighprobability, nomodel’sperformanceisundures.
derstated. Aguaranteeontheotherside—thatnomodel’s
Win matrix estimation. Estimation of the win ma- performanceisoverstated—ispossiblebyinterchangingthe
trix is relatively straightforward. Define X (a) = infandsup.Togettheuniformconfidenceset,weconstruct
t
1 H 1{A =a},whereP (a)istheprobabilityofsam- thechi-squaredintervalimpliedbythecentrallimittheo-

### Pt(a) t t t

plingpairaattimet,andX astheaccordingvector. Then remusingthesandwichestimateofthevariance. Inother
t (cid:13) (cid:13)
theestimatoris words,weconstructtheinterval{ξ :T (cid:13)Vˆ−1/2(ξˆ−ξ)(cid:13)≤
(cid:13) (cid:13)

## T

θˆ = 1 (cid:88) X . (4) χ2 ,whereξˆisourMLEoftheBTcoefficientsand

### T T t 1−α,M−1

t=1 Vˆ isthesandwichvarianceofthelogisticregression.
ξ

### Note that E[X (a)] = θ∗(a) for all t, and thus θˆ is an

t T Active sampling rule. Our sampling rule was to choose
unbiasedestimatorofθ∗. Wewillfurthermoreestimatethe
the model pair a ∈ A proportionally to the reduction in
covariancematrixas
confidenceintervalsizebysamplingthatpair:

## T

Σ(cid:98)T =

## T

1 (cid:88) (X
t
−θˆ

## T


## )(X

t
−θˆ

## T

)⊤. (5)

### P (a)∝

(cid:115) Σˆ
t,a,a −
(cid:115) Σˆ
t,a,a . (9)
t=1 t |{t:A =a}| |{t:A =a}|+1
t t
Undertheappropriateregularityconditions,wehavethat
√
TΣ(cid:98) −1/2(θˆ−θ∗)→N(0,I
d
), (6) 5.1.DetectingAnomalousUsers
On a different note, we take a first step towards identifyand we construct confidence intervals accordingly. For
ing anomalous IP addresses in our dataset. In a dataset
anunderstandingoftheappropriateregularityconditions,
of U unique IPs, we let IP = {1,...,U} be the set
seeDurrett(2019),Theorem8.2.8,wherecondition(ii)is
of all IP addresses. Consider a “test” user, outside this
triviallysatisfiedsolongasP (a)>ϵ>0,andcondition
t database, who gives ratings H′,...,H′ when presented
(i)isimpliedbythealmost-sureconvergenceofP (a)toa 1 n
t actionsA′,...,A′ . TheideaofourprocedureistocomlimitingdistributionP(a). 1 n
parethedistributionofratingsforthenewusertothehis-
EstimatingtheBTscores. ToestimatetheBTcoefficients, torical distribution of ratings for a given action. We let
mirroring (3), we perform (reweighted) maximum likeli- H ={H :A =a}andeverytimeausersubmitsavote,
a t t
hoodestimationonourdatapoints: wecalculatethefollowingnumber:

### T (cid:18) (cid:19)  

s(Pˆ)=arg ξ min (cid:88) t=1 P( 1 A t ) ℓ H t , 1+eξA 1 t,2 −ξAt,1 , p i = |H 1 |+1   1+ (cid:88) 1{h≥H i ′}  . (10)

## (7) A′

whereA ∼P.WeperformtheinverseweightingbyP(A )
i h∈H A′
i
t t
because this allows us to target a score with a uniform UnderthenullhypothesisthatH isexchangeablewith

## A′

distributionoverA. H′,p isavalidp-value(seeAppen i dixCforaproof). Furi i
thermore,thedependenceofthesep-valuesasymptotically
TocomputeconfidenceintervalsontheBTcoefficients,we
isnegligible.
employtwostrategies: (1)thepivotbootstrap(DiCiccio&
Efron,1996),and(2)the“sandwich”robuststandarderrors With this p-value in hand, we can test against this null
outlinedinHuberetal.(1967)(seealsoFreedman(2006) hypothesis sequentially by using Fisher’s combination
foranoutlineofthenecessarytechnicalassumptions). Ulti- test(Fisher,1928)alongwithavariantoftheBonferroni
mately,basedontheresultsofasimulationstudydescribed correction. Inparticular,foreachuser,aftertheirjthvote,
inAppendixA,wechoosetodeploythesandwichintervals j
(cid:80)
we compute M = −2 log(p ). At 5 randomly choduetotheirsmallersizeinlargesamples. j i
i=1
sen values of j between 1 and 100, we identify a user as
Approximaterankings. Finally,wereportanapproximate
anomalous if M ≥ χ2 . (The times are randomly
ranking for each model that accounts for the uncertainty j 2j,1−α/5
chosen,astoavoidanomaloususersstrategizingtohackthis
in the estimation of the score. Given an M-dimensional
p-value.) Despitetheheuristicapplicationofthisprocedure,
confidencesetC satisfying
it seems to work well in our small-scale tests reported in
P(s(P)∈C)≥1−α, (8) Table5.
5

<!-- Page 6 -->

ChatbotArena:AnOpenPlatformforEvaluatingLLMsbyHumanPreference

### Table2.GPT-4-0613’swin-rateagainstLlama-2-70b-chaton30

Word Play and Phonetics (1.0%) Sim 1 ilarity samplepromptsfromvarioustopicclusters.WeuseGPT-4-turbo
Poetry Writing & Styles (0.8%) asjudgetoevaluatemodelresponsesinpairwisecomparison.

### Original Joke Requests (0.5%) 0.9

AI Impact and Applications (0.9%) TopicCluster Win-rate Size

### Philosophical Texts & Concepts (0.4%)


### Advanced Mathematical Concepts (0.4%) 0.8

Sports and Athletics Queries (0.8%) PythonGameProgrammingChallenge 96.7% 0.2%
Operations & Fleet Management (0.8%) 0.7 C/C++ProcessMulti-Threading 86.7% 0.3%

### Email and Letter Writing Assistance (0.8%)

Cooking and Recipes (0.7%) 0.6 SQLQueryDatabaseAssistance 73.3% 0.2%
Animal Be W h e a b v i D or e v a e n l d o p P m et e C n a t r E e s Q se u n e t r i i a e ls s ( ( 0 0 . . 7 4 % % ) ) 0.5 PoetryWritingPrompts 66.7% 1.1%
SQL Database Table Queries (0.5%) PythonCodingBasics 65.0% 0.2%

### Movie Reviews and Discussions (0.5%) 0.4

Role-Playing Games (0.4%) LinguisticAnalysis&Wordplay 58.3% 0.7%
Medical Queries and Information (0.4%) 0.3 TravelItineraryPlanning 58.3% 0.4%
Figure3.Similaritymatrixoftop-16topicclusters. Thenumber MovieRecommendations&Ratings 53.3% 0.2%
followedbythetopiclabelrepresentstheclustersizeinpercentage.

### Notethatsimilarityiscomputedbycluster’scentroidembeddings,

hencediagonalsarealwaysone. fastgrowingcapabilities. Forexample,openmodelssuchas

### Llama-2-70b-chatcanlikelyanswerinquiriesaboutmovie

or travel recommendation as good as GPT-4, but not in

## DataAnalysis

other domains such as reasoning or coding. To demonstrate,wesample30promptsfromseventopicclustersand
To examine whether Arena’s crowdsourced data reflects
comparetheperformanceofLlama-2-70b-chatandGPT-4.
real-world use cases, we conduct topic modeling on the
Tocontrolvariables,wefactoroutuservotesandconsider
userprompts. Weshowhoweffectivearethesepromptsin
LLM-as-judge(Zhengetal.,2023b)toevaluatemodelredistinguishingmodels. Lastly,wevalidatethevotequality
sponse. ResultsareshowninTable2,whereweseeGPT-4
byrelabelingdatawithexperts.
hassignificantlyhigherwin-rate(upto97%)inclustersthat
requirecodingandreasoningskills. Ontheotherhand,for

### TopicModelingonUserPrompts

clusters with less problem-solving tasks, GPT-4 win-rate
To study the prompt diversity, we build a topic modeling dropstobelow60%. WeshowexamplesinAppendixD.1.
pipeline with BERTopic3 (Grootendorst, 2022). We start Thisresultshowsmodelsmayexhibitvaryingstrengthsin
withtransforminguserpromptsintorepresentationvectors differentareas,butalsohighlightssomeofthetopicclusters
usingOpenAI’stextembeddingmodel(text-embedding-3- inChatbotArenaareeffectiveindifferentiatemodels.
small). To mitigate the curse of dimensionality for data

### BuildingChallengingBenchmark. Tofurtherdemonstrate

clustering,weemployUMAP(UniformManifoldApproxthepromptquality,weshowitispossibletoconstructachalimation and Projection) (McInnes et al., 2020) to reduce
lengingbenchmarkwithcrowd-sourceduserprompts. To
the embedding dimension from 1,536 to 5. We then use
ensurebothtopiccoverageandquality,wefirstrunthetopic
thehierarchicaldensity-basedclusteringalgorithm,HDB-
modelingpipelineandfollowasimilarprocedureinZheng

### SCAN,toidentifytopicclusterswithminimumclustersize

etal.(2023a)toselectchallengingquestionssampledfrom

## Finally,toobtaintopiclabels,wesample10prompts

eachtopiccluster. ExamplespromptsandevaluationprocefromeachtopicclusterandfeedintoGPT-4-Turbofortopic
durescanbefoundintheAppendixD.2andAppendixD.3,
summarization.
respectively. Weobservetheselectedpromptsarehighly
Thepipelineidentifies600clusterscoveringawiderangeof effectiveindifferentiatingmodels. InFigure4,wecompare
topicsincludingpoetrywriting,coding,math,andmedical ArenabenchagainstawidelyusedLLMbenchmark,MT-
queries. We present the top-16 topic clusters in Figure 3. Bench(Zhengetal.,2023b). WecanseethatArenaBench
We observe that the largest cluster only accounts for 1% effectivelyrevealsasignificantgapinperformancebetween
of the entire set and the rest quickly drop to <0.5%, and proprietaryandthestrongestopenmodels.
thesimilaritybetweenclustersissmall,showingalong-tail
anddiversedistribution. Duetospacelimit,wepresentthe 6.3.ValidatingVoteQuality
similaritymatrixandclusterhierarchyoftop-64clustersin
Toassessthequalityofcrowdsourcedvotes,werandomly
Figure11and12inAppendix.
selected 160 battles between GPT-4-Turbo and Llama-2-
13B,aswellasGPT-4-TurboandGPT-3.5-Turbo-0613. We

### CanArenaPromptsDistinguishModels?

thenaskedexperts4tolabeltheirpreferencepercomparison.
Next, we study how effective are these topic clusters in The experts were given the prompts and answers blindly,
distinguishingmodelsstrengths. Constructingchallenging andaskedtocarefullyfact-checkmodel’sanswerwithexprompts has become increasingly difficult due to LLMs’ ternalresourceslikesearchengine. Manuallylabelingeach
3https://github.com/MaartenGr/BERTopic 4ThelaborersaregraduatestudentsatUCBerkeley.
6

<!-- Page 7 -->

ChatbotArena:AnOpenPlatformforEvaluatingLLMsbyHumanPreference
Table4.GPT-4-Turbo’swin-rateacrosscrowd-user,gpt-4judge,
andexpertsonpairwisebattlesagainstLlama-2-13bandGPT-3.5-
GPT-4-Turbo Arena Bench Turbo-0613.

### MT Bench

GPT-4-0314 Baseline ArenaUser Expert1 Expert2 GPT-4

## Gpt-4-0613


### Llama-2-13b 81.2% 89.4% 86.9% 78.8%

GPT-3.5-Turbo-0613 GPT-3.5-Turbo 76.3% 82.5% 89.4% 79.4%
Claude-2.1
l
e
d Mixtral-8x7B-Instruct

### M o gpt-4-turbo (#1) corrected

Starling-LM-7B-alpha uncorrected
gpt-4-0314 (#2)
OpenChat-3.5 gpt-4-0613 (#3-7)
mistral-medium (#3-8)

### Vicuna-33b-v1.3 claude-1 (#3-8)

Llama-2-70B-Chat claude-2.0 (#3-14)
gemini-pro-dev-api (#3-18)
Llama-2-7B-Chat mixtral-8x7b-instruct-v0.1 (#4-18)
0 2 4 6 8 claude-2.1 (#6-18)

### Score gpt-3.5-turbo-0613 (#6-18)

Figure4.Model’s performance between Arena Bench and MT- gemini-pro (#6-18)
Bench,showinganincreasedgapbetweenopenandproprietary claude-instant-1 (#6-19)
yi-34b-chat (#6-19)
models.BothusesGPT-4asjudge.
tulu-2-dpo-70b (#6-21)
wizardlm-70b (#7-22)
gpt-3.5-turbo-0314 (#7-22)
starling-lm-7b-alpha (#7-26)
Table3.Pairwiseagreementratebetweencrowd-user,gpt-4judge, vicuna-33b (#7-25)
andexpertsonpairwisebattles.Thetoppartofthetableisbetween openhermes-2.5-mistral-7b (#12-28)
llama-2-70b-chat (#14-28)
GPT-4-TurboandLlama-2-13b-chat.ThebottomisbetweenGPT-
openchat-3.5 (#14-29)
4-TurboandGPT-3.5-Turbo-0613. gpt-3.5-turbo-1106 (#15-29)
Llama-2-13b Expert1 Expert2 GPT-4 pplx-70b-online (#17-31)
dolphin-2.2.1-mistral-7b (#17-37)
Crowd 72.8% 77.8% 75.6% solar-10.7b-instruct-v1.0 (#18-36)
Expert1 - 89.8% 81.0% llama2-70b-steerlm-chat (#17-37)
Expert2 - - 78.5% wizardlm-13b (#19-37)
zephyr-7b-beta (#19-37)

### GPT-3.5-Turbo Expert1 Expert2 GPT-4 0.0 0.5 1.0 1.5 2.0 2.5

Crowd 73.8% 83.1% 75.6% Figure5.IntervalsfortheBTcoefficientswithandwithoutmul-
Expert1 - 79.4% 76.3% tiplicity correction. The multiplicity correction, in this case a
Expert2 - - 79.3% chi-squareCLTinterval,istechnicallyrequiredforthepurposeof
calculatingtheranking,becauseitensuresallscoresaresimultaneouslycontainedintheirintervals(andtherankingisafunction
ofallthescores).However,itinducesextraconservatism,sowe
datapointtookonaverage3-5minutes. Forreference,we
reportbothintervals.
alsouseGPT-4asajudgeforpairwisecomparisons. The
agreementratebetweencrowd-users,experts,andGPT-4-

## Experiments

judgearepresentedinTable3. Thecorresponsingwin-rate
areshowninTable4.

### Rankingsystem


### Tosummarize, weobservehighagreementrates(72%to

Computing the rank on real data. In this section, we
83%)betweenArenacrowd-userandexpertsinbothsetup.
reportresultsfromourexperimentsonapproximateranking.

### Notethatagreementratesbetweentwoexpertsarearound

Forthisexperiment,weranareplayofT = 213,576hissimilar levels (79.4% and 89.8%). As for the 10%-20%
toricalvotesfromouronlineplatformandcalculatetheBT
disagreementbetweenexperts,itismostlyduetosomeuser
coefficientsusingourearlier-describedestimationalgorithm
promptsdon’thaveagroundtruthanswer. Dependingon
withconfidenceintervals;seeFigure5fortheseintervals
the preference of the evaluator, sometimes both answers
(withandwithoutmultiplicitycorrection;theformalnotion
can be argued as being better than the other one, such as
of approximate ranking technically requires multiplicity
theexamplesinAppendix D.4. Thegapbetweencrowdcorrection,butitmakestheintervalslooser).
vs-expert agreement rate and expert-vs-expert agreement
rate(5%-10%)ismostlyattributedtocrowdusermaking Evaluatingthecoverageoftheintervals.Anaturalfollowmistakesoroverlookingfactualerrorsinmodel’sresponse. upquestioniswhetherornottheintervalsaredoingtheirjob
Overall,theagreementratespresentedinTable3validate correctly: whethertheycoverthetrueBTcoefficientswith
thedecentqualityofcrowd-sourcedvotesinChatbotArena. probabilityatleast(andalmostexactly)1−α. Ofcourse,
7

<!-- Page 8 -->

ChatbotArena:AnOpenPlatformforEvaluatingLLMsbyHumanPreference
0.9
0.8
0 20000 40000 60000 80000 100000
n
egarevoC
Coverage
1.5
1.0
0.5
0.0
0 20000 40000 60000 80000 100000
n
htdiW
lavretnI
egarevA
30000
20000
10000
0
0.10 0.12 0.14 0.16 0.18 0.20 0.22 0.24
average width ( )
Average Interval Width

## M

4
7
10
15
20
Figure6.Intervals for the BT coefficients as a function of the
numberofsamplesandthenumberofmodelsM.
thiscannotbeevaluatedonrealdata,sowerunasimulation.

### AvectorofBTcoefficientsisdrawn,witheachcoordinate

sampledi.i.d.fromadistributionbeta(1/γ,1/γ);wetake
γ = 2inFigure6(andwevaryγ inAppendixA).Given
thesecoefficients,adatasetissynthesized,andthecoverage
andaveragewidtharecomputedforeachof20trials. The
resultscanbeseeninFigure6fortheuncorrectedintervals

### Thecoverageoftheintervalsbehavesasexpected,centering

around1−α,regardlessofthenumberofmodels. Meanwhile,themoremodelsareincluded,thelargertheintervals
become.
Evaluatingtheactivesamplingrule. Next,wediscussthe
evaluationofouractivesamplingruleasEquation(9)for
winmatrixestimation. Weevaluatethissamplingruleby
takingthebestfitBTcoefficientstoour213,576pointsized
holdoutset,andthensamplingfromthatdistributionusing
our active sampling algorithm. The results are displayed
in Figure 7. It is hard to tell by looking at plots, but the
improvementissubstantial: Toestimateθ∗toaprecisionof
0.2,randomneeds6,800samplesandadaptiveneeds4,400
samples; meanwhile to estimate the score to a precision
of0.3, randomneeds17,200samplesandadaptiveneeds
16,400samples. Thus,therandombaselinerequires54%
and5%moredatatoachievethesamelevelofprecision,
respectively. One can see from the plots in Figure 7 that
theseresultsarenotcherry-picked: thesample-efficiencyof
ourmethodisbetteratallvaluesonthehorizontalaxis.

### AnomalousUsersDetection

We evaluate the outlier detection method in Section 5.1.
We construct the evaluation set by manually identifying
25anomaloususerswhoseinputsarehighlyrepetitiveor
meaningless (e.g., asking “hi” for 100 times or inputting
garbledtexts). Werandomlysample25normaluserswith
n
random
pairwise adaptive
30000
20000
10000
0
0.25 0.30 0.35 0.40 0.45 0.50
average width (s)
n
Figure7.Intervalwidthsonthewinmatrix(upperfigure)andon
theBTcoefficients(lowerfigure)asafunctionofthenumberof
samples,forrandomsamplingandalsoadaptivesampling. Improvements from adaptive sampling can be seen in both cases,
althoughtheyaremoresubtleonthescaleofthescore.
Table5.Confusionmatrixofdifferentα.“Pred.”meanspredicted.
Positivemeansanomalousandnegativemeansnormal.
α=0.1 Pred. Positive Pred. Negative
ActualPositive 13/14 12/36

### ActualNegative 1/14 24/36

α=0.3 Pred. Positive Pred. Negative
ActualPositive 21/29 4/21

### ActualNegative 8/29 17/21

atleast50votes,andinspecttheirinputpromptstoensure
noabnormalbehaviors. AsmentionedinSection5.1,per
userwecomputefiveM andidentifytheuserasanomalous
j
ifM ≥ χ2 . Wepresentresultsoftwodifferentα
j 2j,1−α/5
(i.e.,thesignificanceleval)inTable5. Wefindthedetectionmethodeffective(e.g.,reaching90%truepositiveand
60-70%truenegativerate). Weinspectthefalsenegative
errorsandfindthosearefromusersdonotalwaysbehave
abnormally,makingthemhardertodetect.

## Discussion

Limitations. Althoughouruserbaseisextensive,weanticipatethatitwillprimarilyconsistofLLMhobbyistsand
researcherswhoareeagertoexperimentwithandevaluate
the latest LLMs. This inclination may result in a biased
distributionofusers. Additionally,despitethewidearrayof
topicsencompassedbythepromptsdiscussedinprevious
sections, the data predominantly comes from our online
chatinterface. Thissourcemightnotaccuratelyreflectthe
real-worldusageofLLMsinproductionenvironmentsor
specializeddomains,potentiallyleadingtoaskewedprompt
distribution. Moreover,ourstudyconcentratesonassessing
thehelpfulnessofLLMsbutoverlookstheirsafetyaspects.
We recognize the possibility and necessity of a parallel
8

<!-- Page 9 -->

ChatbotArena:AnOpenPlatformforEvaluatingLLMsbyHumanPreference
mechanismtoevaluatethesafetyofthesemodels. LearningResearch,pp.1071–1079,Bejing,China,22–
24Jun2014a.PMLR.URLhttps://proceedings.
FutureDirections. Inourfuturework,weplantodevelop
mlr.press/v32/busa-fekete14.html.
comprehensivetopicleaderboardsandestablishadedicated
sectionformultimodalandagent-basedLLMsinmoredy- Busa-Fekete, R., Huellermeier, E., and Szörényi, B.
namic,gamifiedsettings,cateringtomorecomplextasks. Preference-basedrankelicitationusingstatisticalmodels:
We also believe our approach to detecting harmful users Thecaseofmallows. InXing,E.P.andJebara,T.(eds.),
could be improved and made more formally rigorous by Proceedingsofthe31stInternationalConferenceonMausing the theory of nonnegative supermartingales and E- chineLearning,volume32ofProceedingsofMachine
values (Howard et al., 2020; Waudby-Smith & Ramdas, LearningResearch,pp.1071–1079,Bejing,China,22–24
2020;Vovk&Wang,2021;Ramdasetal.,2023);thiswould Jun 2014b. PMLR. URL https://proceedings.
dealwiththedependence,butthevariantswetrieddidnot mlr.press/v32/busa-fekete14.html.
performwellintermsofpower.

### Chen,M.,Tworek,J.,Jun,H.,Yuan,Q.,Pinto,H.P.d.O.,

Kaplan,J.,Edwards,H.,Burda,Y.,Joseph,N.,Brockman,

## Conclusion

G., etal. Evaluatinglargelanguagemodelstrainedon
code. arXivpreprintarXiv:2107.03374,2021.

### Inthispaper,wepresentChatbotArena,anopenplatform

forevaluatingLLMsthroughcrowdsourced, pairwisehu- Chernoff, H. Sequential Design of Experiments, pp.
manpreferences. Weconductanin-depthanalysisofthe 345–360. Springer New York, New York, NY,
crowdsourceduserpromptsandpreferencevotestovalidate 1992. ISBN 978-1-4612-4380-9. doi: 10.1007/
the diversity and quality. We develop an efficient model 978-1-4612-4380-9_27. URL https://doi.org/
sampling and ranking algorithm. Our dataset including 10.1007/978-1-4612-4380-9_27.
100Kpairwisepreferencevoteswillbereleasedforfuture
research. Chiang, C.-H. and Lee, H.-y. Can large language modelsbeanalternativetohumanevaluations? InRogers,
A., Boyd-Graber, J., and Okazaki, N. (eds.), Proceed-

### Acknowledgments

ings of the 61st Annual Meeting of the Association for
This project is supported by sponsorship from Kaggle, ComputationalLinguistics(Volume1: LongPapers),pp.
MBZUAI,a16z,TogetherAI,Anyscale,andHuggingFace. 15607–15631,Toronto,Canada,July2023.Association
ThisprojectisalsopartlysupportedbyAccenture,AMD, forComputationalLinguistics. doi: 10.18653/v1/2023.
Google,IBM,Intel,Microsoft,SamsungSDS,SAP,Uber,
acl-long.870.URLhttps://aclanthology.org/
and VMware. The authors would like to thank Siyuan
2023.acl-long.870.
ZhuangforinsightfuldiscussionandTijanaZrnic´forhelpful
Cobbe,K.,Kosaraju,V.,Bavarian,M.,Chen,M.,Jun,H.,
feedbackonthemanuscript.

### Kaiser,L.,Plappert,M.,Tworek,J.,Hilton,J.,Nakano,

R.,etal. Trainingverifierstosolvemathwordproblems.
References arXivpreprintarXiv:2110.14168,2021.
Bai,Y.,Jones,A.,Ndousse,K.,Askell,A.,Chen,A.,Das- Cui,G.,Yuan,L.,Ding,N.,Yao,G.,Zhu,W.,Ni,Y.,Xie,G.,
Sarma,N.,Drain,D.,Fort,S.,Ganguli,D.,Henighan,T., Liu,Z.,andSun,M. Ultrafeedback: Boostinglanguage
etal. Trainingahelpfulandharmlessassistantwithrein- modelswithhigh-qualityfeedback,2023.
forcementlearningfromhumanfeedback. arXivpreprint
DiCiccio,T.J.andEfron,B. Bootstrapconfidenceintervals.
arXiv:2204.05862,2022.
Statisticalscience,11(3):189–228,1996.
Boubdir,M.,Kim,E.,Ermis,B.,Hooker,S.,andFadaee,M.
Durrett,R. Probability: theoryandexamples,volume49.
Elouncovered:Robustnessandbestpracticesinlanguage
Cambridgeuniversitypress,2019.
modelevaluation,2023.

### Elo, A. E. The proposed uscf rating system, its develop-

Bradley, R.A.andTerry, M.E. Rankanalysisofincomment, theory, and applications. Chess Life, 22(8):242–
pleteblockdesigns: I.themethodofpairedcomparisons.
247,1967.
Biometrika,39(3/4):324–345,1952.
Fisher,R.A.Statisticalmethodsforresearchworkers.Num-
Busa-Fekete, R., Huellermeier, E., and Szörényi, B.
ber5.OliverandBoyd,1928.

### Preference-basedrankelicitationusingstatisticalmodels:

Thecaseofmallows. InXing,E.P.andJebara,T.(eds.), Freedman, D. A. On the so-called “huber sandwich esti-
Proceedingsofthe31stInternationalConferenceonMa- mator”’ and “robust standard errors”’. The American
chineLearning,volume32ofProceedingsofMachine Statistician,60(4):299–302,2006.
9

<!-- Page 10 -->

ChatbotArena:AnOpenPlatformforEvaluatingLLMsbyHumanPreference
Gemini,T.,Anil,R.,Borgeaud,S.,Wu,Y.,Alayrac,J.-B., Kiela,D.,Bartolo,M.,Nie,Y.,Kaushik,D.,Geiger,A.,Wu,
Yu,J.,Soricut,R.,Schalkwyk,J.,Dai,A.M.,Hauth,A., Z.,Vidgen,B.,Prasad,G.,Singh,A.,Ringshia,P.,etal.
et al. Gemini: a family of highly capable multimodal Dynabench: Rethinking benchmarking in nlp. In Promodels. arXivpreprintarXiv:2312.11805,2023. ceedingsofthe2021ConferenceoftheNorthAmerican

### ChapteroftheAssociationforComputationalLinguistics:

Geng, X., Gudibande, A., Liu, H., Wallace, E., Abbeel, HumanLanguageTechnologies,pp.4110–4124,2021.
P., Levine, S., and Song, D. Koala: A dialogue model for academic research. Blog post, Köpf, A., Kilcher, Y., von Rütte, D., Anagnostidis, S.,
April2023. URLhttps://bair.berkeley.edu/ Tam,Z.-R.,Stevens,K.,Barhoum,A.,Duc,N.M.,Stanblog/2023/04/03/koala/. ley, O., Nagyfi, R., etal. Openassistantconversations–
democratizing large language model alignment. arXiv
Grootendorst, M. Bertopic: Neural topic modeling
preprintarXiv:2304.07327,2023.
with a class-based tf-idf procedure. arXiv preprint
arXiv:2203.05794,2022. Langley,P.Craftingpapersonmachinelearning.InLangley,
P.(ed.),Proceedingsofthe17thInternationalConference
Hendrycks,D.,Burns,C.,Basart,S.,Zou,A.,Mazeika,M.,
onMachineLearning(ICML2000),pp.1207–1216,Stan-
Song,D.,andSteinhardt,J. Measuringmassivemultitask
ford,CA,2000.MorganKaufmann.
languageunderstanding. InInternationalConferenceon
LearningRepresentations,2020.
Li, X., Zhang, T., Dubois, Y., Taori, R., Gulrajani, I.,

### Guestrin,C.,Liang,P.,andHashimoto,T.B. Alpacae-

Howard, S. R., Ramdas, A., McAuliffe, J., and Sekhon,
val: An automatic evaluator of instruction-following
J. Time-uniformchernoffboundsvianonnegativesupermodels. https://github.com/tatsu-lab/
martingales. 2020.
alpaca_eval,2023.

### Huang,Y.,Lin,Z.,Liu,X.,Gong,Y.,Lu,S.,Lei,F.,Liang,

Li,Y.,Choi,D.,Chung,J.,Kushman,N.,Schrittwieser,J.,

### Y.,Shen,Y.,Lin,C.,Duan,N.,etal. Competition-level


### Leblond,R.,Eccles,T.,Keeling,J.,Gimeno,F.,DalLago,

problems are effective llm evaluators. arXiv preprint
A.,etal. Competition-levelcodegenerationwithalphaarXiv:2312.02143,2023.
code. Science,378(6624):1092–1097,2022.

### Huber, P. J. et al. The behavior of maximum likelihood

estimatesundernonstandardconditions. InProceedings Liang,P.,Bommasani,R.,Lee,T.,Tsipras,D.,Soylu,D.,
ofthefifthBerkeleysymposiumonmathematicalstatistics Yasunaga,M.,Zhang,Y.,Narayanan,D.,Wu,Y.,Kumar,
andprobability,volume1,pp.221–233.Berkeley,CA: A.,etal. Holisticevaluationoflanguagemodels. arXiv
preprintarXiv:2211.09110,2022.
UniversityofCaliforniaPress,1967.
Hunter, D. R. MM algorithms for generalized Bradley- Lin, Z., Wang, Z., Tong, Y., Wang, Y., Guo, Y., Wang,
Terrymodels. TheAnnalsofStatistics,32(1):384–406, Y., and Shang, J. ToxicChat: Unveiling hidden chal-
2004. doi: 10.1214/aos/1079120141. URL https: lenges of toxicity detection in real-world user-AI con-
//doi.org/10.1214/aos/1079120141. versation. In Bouamor, H., Pino, J., and Bali, K.
(eds.), Findings of the Association for Computational
Karimi,M.R.,Gürel,N.M.,Karlaš,B.,Rausch,J.,Zhang, Linguistics: EMNLP 2023, pp. 4694–4702, Singa-
C., and Krause, A. Online active model selection for pore, December 2023. Association for Computational
pre-trained classifiers. In International Conference on Linguistics. doi: 10.18653/v1/2023.findings-emnlp.
ArtificialIntelligenceandStatistics,pp.307–315.PMLR, 311. URL https://aclanthology.org/2023.
2021. findings-emnlp.311.
Karpinska, M., Akoury, N., and Iyyer, M. The perils of Liu,T.-Y.etal. Learningtorankforinformationretrieval.
usingMechanicalTurktoevaluateopen-endedtextgen- FoundationsandTrends®inInformationRetrieval,3(3):
eration. In Moens, M.-F., Huang, X., Specia, L., and 225–331,2009.
Yih, S. W.-t. (eds.), Proceedings of the 2021 Conference on Empirical Methods in Natural Language Pro- McInnes, L., Healy, J., and Melville, J. Umap: Uniform
cessing,pp.1265–1285,OnlineandPuntaCana,Domini- manifold approximation and projection for dimension
canRepublic,November2021.AssociationforComputa- reduction,2020.
tionalLinguistics. doi: 10.18653/v1/2021.emnlp-main.

## URL https://aclanthology.org/2021. OpenAI. Gpt-4 technical report. arXiv preprint

emnlp-main.97. arXiv:2303.08774,2023.
10

<!-- Page 11 -->

ChatbotArena:AnOpenPlatformforEvaluatingLLMsbyHumanPreference
Oren, Y., Meister, N., Chatterji, N., Ladhak, F., and 2023.acl-long.754. URLhttps://aclanthology.
Hashimoto,T.B. Provingtestsetcontaminationinblack org/2023.acl-long.754.
boxlanguagemodels. arXivpreprintarXiv:2310.17623,
Waudby-Smith, I. and Ramdas, A. Estimating means of
2023.
bounded random variables by betting. arXiv preprint
Ouyang, L., Wu, J., Jiang, X., Almeida, D., Wainwright, arXiv:2010.09686,2020.
C. L., Mishkin, P., Zhang, C., Agarwal, S., Slama, K.,
White, H. Maximum likelihood estimation of misspeci-
Ray,A.,Schulman,J.,Hilton,J.,Kelton,F.,Miller,L.,
fiedmodels. Econometrica: Journaloftheeconometric
Simens,M.,Askell,A.,Welinder,P.,Christiano,P.,Leike,
society,pp.1–25,1982.
J., and Lowe, R. Training language models to follow
instructionswithhumanfeedback,2022.
Yang, S., Chiang, W.-L., Zheng, L., Gonzalez, J. E., and

### Stoica,I. Rethinkingbenchmarkandcontaminationfor

Ramdas,A.,Grünwald,P.,Vovk,V.,andShafer,G. Gamelanguagemodelswithrephrasedsamples. arXivpreprint
theoreticstatisticsandsafeanytime-validinference. StaarXiv:2311.04850,2023.
tisticalScience,38(4):576–601,2023.

### Zellers,R.,Holtzman,A.,Bisk,Y.,Farhadi,A.,andChoi,

Rao, P. V. and Kupper, L. L. Ties in paired-comparison

### Y. Hellaswag:Canamachinereallyfinishyoursentence?

experiments: Ageneralizationofthebradley-terrymodel.

### InProceedingsofthe57thAnnualMeetingoftheAsso-


### JournaloftheAmericanStatisticalAssociation,62(317):

ciation for Computational Linguistics, pp. 4791–4800,
194–204,1967. doi: 10.1080/01621459.1967.10482901.
2019.
Srivastava,A.,Rastogi,A.,Rao,A.,Shoeb,A.A.M.,Abid,

### Zheng,L.,Chiang,W.-L.,Sheng,Y.,Li,T.,Zhuang,S.,Wu,

A., Fisch, A., Brown, A. R., Santoro, A., Gupta, A.,

### Z.,Zhuang,Y.,Li,Z.,Lin,Z.,Xing,E.P.,Gonzalez,J.E.,

Garriga-Alonso, A., et al. Beyond the imitation game:

### Stoica,I.,andZhang,H. Lmsys-chat-1m: Alarge-scale

Quantifyingandextrapolatingthecapabilitiesoflanguage
real-worldllmconversationdataset,2023a.
models. Transactions on Machine Learning Research,
2023.
Zheng,L.,Chiang,W.-L.,Sheng,Y.,Zhuang,S.,Wu,Z.,

### Zhuang,Y.,Lin,Z.,Li,Z.,Li,D.,Xing,E.,Zhang,H.,

Szörényi, B., Busa-Fekete, R., Paul, A., and Hüller-

### Gonzalez,J.E.,andStoica,I. JudgingLLM-as-a-judge

meier, E. Online rank elicitation for plackettwith MT-bench and chatbot arena. In Thirty-seventh
luce: A dueling bandits approach. In Cortes, C.,

### ConferenceonNeuralInformationProcessingSystems

Lawrence, N., Lee, D., Sugiyama, M., and Garnett,

### DatasetsandBenchmarksTrack,2023b. URLhttps:

R. (eds.), Advances in Neural Information Process-
//openreview.net/forum?id=uccHPGDlao.
ing Systems, volume 28. Curran Associates, Inc.,

## URL https://proceedings.neurips.

Zhong, W., Cui, R., Guo, Y., Liang, Y., Lu, S., Wang,
cc/paper_files/paper/2015/file/
Y., Saied, A., Chen, W., and Duan, N. Agieval: A
7eacb532570ff6858afd2723755ff790-Paper.
human-centricbenchmarkforevaluatingfoundationmodpdf.
els. arXivpreprintarXiv:2304.06364,2023.
Touvron, H., Martin, L., Stone, K., Albert, P., Almahairi,
Zhu, B., Frick, E., Wu, T., Zhu, H., andJiao, J. Starling-
A., Babaei, Y., Bashlykov, N., Batra, S., Bhargava, P.,
7b: Improvingllmhelpfulness&harmlessnesswithrlaif,
Bhosale,S.,etal. Llama2: Openfoundationandfine-
November2023.
tuned chat models. arXiv preprint arXiv:2307.09288,
2023.
Vovk,V.andWang,R. E-values: Calibration,combination
andapplications. TheAnnalsofStatistics,49(3):1736–
1754,2021.

### Wang, Y., Kordi, Y., Mishra, S., Liu, A., Smith, N. A.,

Khashabi, D., and Hajishirzi, H. Self-instruct: Aligninglanguagemodelswithself-generatedinstructions. In
Rogers,A.,Boyd-Graber,J.,andOkazaki,N.(eds.),Proceedingsofthe61stAnnualMeetingoftheAssociation
forComputationalLinguistics(Volume1: LongPapers),
pp.13484–13508,Toronto,Canada,July2023.AssociationforComputationalLinguistics. doi: 10.18653/v1/
11

<!-- Page 12 -->

ChatbotArena:AnOpenPlatformforEvaluatingLLMsbyHumanPreference
Figure8. ScreenshotofChatbotArena.
4000 4350
4708
4320
1 2 3 0 0 0 0 0 0 0 0 0 0

## M

966
a
1014743441
y
472408 223228
2
194 667
0
1719 2223 1513
2
1107970848
3
1573 2138 1144786651 12561128813825729768525 779786

## J

627
u
12121121
n
548627476 650
2
549442439
0
293285396
2
428425382
3
309246323418337326368380186184290357393412

## J

489301
u
372482
l
535 384327
2
326222
0
199293266
2
296324278
3
216205245312359405216134131206 340406 932 421191

## A

172 343366
u
256288
g
22596149 222
2
220184200
0
1441111252 65248
3
233138103921018913913412098609712510

## S

6123112124e 56338
p
480 613404 409
2
431239310
0
377439472
2
444341
3
325354 539580529481352326310 657684657626

## O

628340299 504
c
501514
t
566506 301
2
362 537625
0
509465
2
531537364
3
708536563598515394321328 483 688535439432469

## N

662548530
o
516 722
v
518640 961
3706
2
2934 1767 1177
0
805 1035 1393
2
1092 1233
3
13251252 724705 1143 1242951874 12041108782 1056 1265

## D

1200 16311284
e
1081 1322 2058
c
22522245 1656
2
155414351433
0
157316201556
2
1435 1571
3
1268 1529 1920
3794
3412 2336 3201 3295
3838
2882 2423 1729

## J

1316
a
1653 1974
n
17701585 2480 2101
2
16441491 1612
0
2294 18921681
2
17581578
4
18551783 2760 3144 2701 1846 1163 2506 16321657 1832 19191587 1176

### Dates

Figure9. Thenumberofvotesovertime
12

<!-- Page 13 -->

ChatbotArena:AnOpenPlatformforEvaluatingLLMsbyHumanPreference
30k
1
2
0
0
0
k
k
29779 29181
27726
22849
17756 17562 17513 16968
15684 14784 13890 13852
11826 11720 11209 10471 9562
8135 7929 7686 7420 7329 7309 7266 7018 7008 6711 6206 6018 5985 5961 5688
gpt-3.5 g - p tu t- r 4 b - o t g u - p 0 r t b 6 - o 4 1 - 3 0 c 6 la 1 u 3 de g -2 p . t 1 -4-0 c 3 la 1 u 4 de c - l i a n u st d a e n v - t 1 ic -1 una v -3 ic 3 u b na l - l 1 am 3b a-2 m - i 7 x 0 tr b a - g c l- p h 8 t a x - t 7 3 b .5 c - - i l n a tu s u r t d b r e u o l - c l - a 2 1 t m - . 1 0 v 0 0 a 6 . - 1 2 ze -1 p 3 h b y - r m c -7 h i b s a t - t r b a e p l t - a m a lm ed -2 i w um izard w lm iz - a 7 r 0 d b v lm ic - u 1 n 3 a b k -7 oa b la-1 o 3 p b ench m a i t s - t 3 r . a 5 l l l - a 7 m b- a in -2 g s - e t 7 r m u b c i - n c t c i h - o p a d r t o ella o m as a s - t 3 -p 4 a y b lp t - h a in c ia s a t - p - r 1 1 p u 2 3 l c b x b t -7 g 0 e b m -o i n n l g i i - n p p e t r - o 3 - . d 5 y e - i v t -3 u -a 4 rb p b o i -c -0 h 3 a 1 t 4
Figure10. Thenumberofvotespermodel.
Similarity Matrix
Similarity Score
1
0.9

### Song Lyrics Analysis


### Requesting Original Jokes

Linguistic Analysis & Wordplay
Magic & Fantasy RPG Campaigns
0.8

### Erotic Short Stories


### Potter & Rings Crossover


### C/C++ Process Multi-Threading

Python Game Programming Challenges
Python Coding Basics
0.7
Game Engines and Player Movement
Travel Itinerary Planning

### Jupiter's Moons Astronomy


### AI Image Generation Prompts

Complex AI Roleplay Guidelines 0.6

### LLM Prompt Optimization

High-Performance Computing Hardware

### PyTorch AutoEncoder Training Issues

Videogame Recommendations & Insights
Chess Notation Magnus vs Hikaru 0.5
Chemical Reactions and Calorimetry

### Apple Quantity Calculations


### Triangle Angle Bisector Area


### Overcoming Emotional Paralysis


### Market Innovation & Platforms 0.4

Sustainable Mobility and Solar Energy

### Simplifying Quantum Mechanics

Biblical Interpretation and Theology
Alternate WWI Victorious Germany
0.3
Israel-Hamas Conflict Dynamics

### SQL Query Database Assistance

Docker Syslog Service Configuration
Inflation & Monetary Policy
0.2
0.1
Figure11. Similaritymatrixoftop-64topicclusters.
13

<!-- Page 14 -->

ChatbotArena:AnOpenPlatformforEvaluatingLLMsbyHumanPreference

### Hierarchical Clustering

Unique Social Gaming Branding
YouTube Content Strategy

### Simulated Unfiltered AIs

AGI Research and Progress Prediction
Trade Reporting and UAT Coordination

### Operations & Fleet Management

Educational Assessment Strategies

### Meaning of Life Inquiry

Philosophical Texts & Concepts
Biblical Theology & Doctrines

### Medical Case Summaries

Understanding Depression Varieties

### Greetings and Personal Inquiries

Relationship Communication Issues

### Cats and Dog Breeds


### Jessica's Resilient Romance

Medieval Fantasy Quest Narrative

### Cyberpunk Sci-Fi Narratives

Movie Reviews and Discussions

### AI Image Prompt Crafting

Anime Evolution & Relationships

### Israel-Hamas Conflict Analysis

Antisemitism and Historical Inaccuracies

### US Presidents Inquiry


### Global Geography & Demographics

Simplified Quantum Mechanics Explained

### Advanced Mathematical Concepts

Chemical Reactions and Calorimetry
Regression Analysis Essentials

### Math Order of Operations

Sports Rankings and Analysis

### Fed Inflation Rate Decisions

Automotive Insights and Comparisons

### PC Components & Upgrades

Determining Today's Day Puzzles

### Trip Itinerary Planning

Weight Comparison Bricks Feathers
Body Recomposition Weekly Workout

### Cooking and Recipes


### Horticulture & Plant Care

Societal Ideologies & Welfare

### Apple Count After Eating

Music Discovery & Recommendations
Guitar Chords and Music Theory

### Chess Gameplay and Strategies

Riddles Creation and Solutions
Poetry Writing & Styles

### Original Joke Requests

Japanese Language Translation

### Word Play and Phonetics


### German Language Practice

Hexadecimal Message Decryption

### ASCII Art Creations


### Linux vs Windows Comparison

Linux Terminal Command Simulation
Rust Programming Essentials
SQL Database Table Queries

### Web Development Essentials

AWS Terraform Deployment & Services
Pandas DataFrame Operations

### PyTorch Neural Networks

Transformer Attention Mechanisms

### Large Language Models Analysis

Understanding LLMs and Training
0 0.2 0.4 0.6 0.8 1 1.2
Figure12.Top-64clustersvisualizedinhierarchy.x-axisrepresentsthecosinesimilaritydistance.y-axisshowsthetopictitlepercluster
summarizedbygpt-4-turbo.
14

<!-- Page 15 -->

ChatbotArena:AnOpenPlatformforEvaluatingLLMsbyHumanPreference
Intervals (n=23968)
1.00 1.25

### Sandwich 0.98

1.00 Bootstrap 0.96
0.75 0.94
0.50 0.92
0.25 0.90
0.00 0.88
lla ma-2 l - l 7 a b m -c a h -2 a - t 1 l ( l 3 a # b m 7 -c - a 7 h - ) 2 a g - t p 7 ( t 0 # -3 b 6 . - 5 c -7 h -t ) a u t r
m
b ( # o ix - 3 t 0 r - 6 4 a 1 ) l c - 3 8 la x ( u # 7 d b 3 e - - i - 3 n 2 ) s .1 tr u ( # ct 3 -v -3 0 g ) .1 p t ( - # 4- 3 0 - 6 3 g 1 ) p 3 t - ( 4 # - 2 tu -2 rb ) o ( #1-1) 12000 n 18000 24000
egarevoC
Coverage
0.28
0.26
0.24
0.22
0.20
0.18
12000 18000 24000 n
htdiW
lavretnI
egarevA
Average Interval Width
method
sandwich
bootstrap
Figure13.Replayexperimentshowingtheintervals,coverage,andaverageintervalsizesofthebootstrapandofthesandwichintervals.
Thesandwichintervals,thoughlargerinsmallsamples,aremorestable,andinlargesamples,theyactuallybecomesmaller.Weusethe
multiplicitycorrectedversionofbothintervals,sotheybothhaveacoverageof1.(CoveragehereiscalculatedwithrespecttotheBT
coefficientsolutiononthefulldataset,soitisnotasmeaningfulasinthesimulationplotbelow.)
Intervals (n=100000)
2.0 0.975

### Standard

Bootstrap 0.950
1.5
0.925
0.900
1.0
0.875
0.850
0.5
0.825
0.0 0.800
1 5 9 13 17 0 20000 40000 60000 80000 100000

### M n

egarevoC
Coverage
1.6
1.4
1.2
1.0
0.8
0.6
0.4
0.2
0 20000 40000 60000 80000 100000
n
htdiW
lavretnI
egarevA
Average Interval Width
method
sandwich
bootstrap
Figure14.Syntheticexperiment.CoefficientsaredrawnfromtheBT-coefficientdistributionxontheleft.Coverageoftheuncorrected
intervalsisshowninthemiddle.Lineplotsofsetwidthareshownontheright,andtheyalmostperfectlymatch.

### A.ConfidenceIntervalSimulationStudy

Weconductasimulationstudytoevaluatethebootstrapconfidenceintervalsversusthesandwichestimator. Toalargeextent,
bothintervalsarethesame—indeed,theirintervalsareoftenidenticaltothenakedeye. Nonetheless,inourexperiments,
therearesomedifferences. First,inFigure13,weconductareplaystudyusingthesame213576datapointsmentionedin
themaintext.
Wealsodoasuiteofexperimentsinsimulationusingthesamebetageneratingprocessasinthemaintext,withγ = 2.
TheresultisshowninFigure14;resultsaresimilaracrossmanychoicesoftheparameterγ andthemodelstrength,which
indicatesthatbothintervalswillhavegoodcoverageandwidthinthepracticalconditionswewouldexposethemto.

### B.TheNonparametricBradley-TerryModel

NonparametricBradley-Terry. WenextconsideranonparametricextensionoftheBradley-Terry(BT)model(Bradley&
Terry,1952)tothecasewheretherankingisnotnecessarilytransitive. LetG(m)denotethesetofallpathstothemodelm,
i.e.,
G(m)= (cid:8) g ∈BM−1 :g ̸=g , ∀i̸=j, andg =m (cid:9) , (11)
i,1 j,1 M−1,2
whereB = A∪{(a ,a ) : a ∈ A}. EachelementofG(m)isachainofmodelpairingsthatleadstom;forexample,if
2 1
m=5andM =6,oneelementofG(m)is((1,2),(2,4),(4,3),(3,6),(6,5)). Ourscorefunctionisgivenbytheaverage
15

<!-- Page 16 -->

ChatbotArena:AnOpenPlatformforEvaluatingLLMsbyHumanPreference
path-sumofthelogoddsofthesecondmodelwinning,overtheentiretyofG(m):
(cid:32) (cid:33)
s(θ) = 1 (cid:88) log θ′((1,g 1,1 )) + (cid:88) log θ′(a) , (12)
m |G(m)| 1−θ′((1,g )) 1−θ′(a)
1,1
g∈G(m) a∈g
whereθ′(a)=θ(a)1{a∈A}+(1−θ((a ,a )))1{a∈/ A},withtheconventionthatθ((m,m))=1/2forallm. Note
2 1
thatforanyg ∈G(m)wherea∈gandm∈/ a,wealsohavesomeg′ ∈G(m)suchthat(a ,a )∈g. Meanwhile,ifa∈g
2 1
andm∈a,thena=(m′,m)forsomem′. Thus,wecancompute
s(θ) = (cid:88) 1 (cid:18) log θ′(a) +log θ′((a 2 ,a 1 )) (cid:19) + (cid:88) (cid:18) log θ′((m′,m)) + θ′((1,m′)) (cid:19)
m 2 1−θ′(a) 1−θ′((a ,a )) 1−θ′((m′,m)) 1−θ′((1,m′))
2 1
a∈A m′∈[M]\{m}
m∈/a
(13)
(cid:88) 1 (cid:18) θ(a) 1−θ(a) (cid:19) (cid:88) (cid:18) θ′((m′,m)) θ′((1,m′)) (cid:19)
= log +log + log + (14)
2 1−θ(a) θ(a) 1−θ′((m′,m)) 1−θ′((1,m′))
a∈A m′∈[M]\{m}
m∈/a
(cid:88) (cid:18) θ′((m′,m)) θ′((1,m′)) (cid:19)
= log + (15)
1−θ′((m′,m)) 1−θ′((1,m′))
m′∈[M]\{m}
(cid:88) (cid:18) θ((m′,m)) θ((1,m′)) (cid:19)
= (1−21{m′ >m})log + . (16)
1−θ((m′,m)) 1−θ((1,m′))
m′∈[M]\{m}
Thisscoreisalwayswell-defined,andisasimple,smoothfunctionofθ. Itsderivativeis,foralla∈A,
∂ 1 1
s(θ) =1{a =m}(1−21{a >m}) +1{a =1, a ̸=m} . (17)
∂θ(a) m 2 1 θ(a)(1−θ(a)) 1 2 θ(a)(1−θ(a))
HowistheBTscorerelatedtotheoriginalBradley-Terrymodel? IntheoriginalBradley-Terrymodel,H ∈{0,1},andthe
t
probabilityofmodelmbeatingmodelm′isassumedtobegivenby
eξm
θ((m′,m))= , (18)
eξm +eξ m′
forsomeunknownparametersξ ,...,ξ —theBradley-Terrycoefficients. ThebasicgoaloftheBradley-Terrymodelisto

## 1 M

estimatetheseparametersfromtheobservedoutcomes. Inoursetting,however,weusetheoutcomestogetaCLTonθ,and
thencanimmediatelyrecoverthecoefficients. Takingwithoutlossofgeneralityξ =0,wehavethat
1
θ((1,m′)) θ((m′,m)) θ((1,m′)) θ((m′,m))
log +log =log +log (19)
1−θ((1,m′)) 1−θ((m′,m)) θ((m′,1)) θ((m,m′))
eξ m′(eξ m′ +1) eξm(eξ m′ +eξm)
=log +log (20)
eξ m′ +1 eξ m′(eξ m′ +eξm)
=ξ +ξ −ξ =ξ (21)
m′ m m′ m
Thus,allthesumsoverpathsin(12)areequaltoξ −ξ .
m g1,1
log θ′((1,g 1,1 )) + (cid:88) log θ′(a) (22)
1−θ′((1,g )) 1−θ′(a)
1,1
a∈g
=ξ +ξ −ξ +ξ −ξ +···+ξ −ξ (23)
g1,1 g1,2 g1,1 g2,2 g2,1 gM−1,2 gM−1,1
=ξ =ξ . (24)
gM−1,2 m
Thus, if the parametric BT model is well-specified, the nonparametric version will exactly recover the Bradley-Terry
coefficients. However,ournonparametricanalogueoftheBTmodelhasmajoradvantagesovertheoriginal: itwillretain
statisticalvalidityevenifH isnotbinary,ifthewinrateisnon-transitive,andifthelogisticmodelassumedbytheBT
t
modelismisspecified. Inpractice,thenonparametricBTcoefficientcanbeeasilycomputedby(16).
16

<!-- Page 17 -->

ChatbotArena:AnOpenPlatformforEvaluatingLLMsbyHumanPreference

### C.ValidP-Value

Considerthep-value
 
1 (cid:88)
p = 1+ 1{h≥H′}. (25)
i |H |+1 i 

## A′

i h∈H A′
i
Wewillprovethatthisp-valueisvalid,i.e.,thatP(p ≤t)≤t,underthenullhypothesisthatthevectorH′ =(H :A =
i t t
A′)∥(H′)isexchangeable,where∥denotestheconcatenationoperator. First,noticethatwecanequivalentlywrite
i i
1 (cid:88)
p = 1{h≥H′}. (26)
i |H′| i
h∈H′
WealsohavethatP(p ≤t)≤P(p ≤ k ),wherek =⌊t|H′|⌋/|H′|. Then,sincethedatapointsareexchangeable,we
i i |H′|
havethatH′isuniformlydistributedamongtheranksofH′,soP(p ≤ k )≤ k ≤t,completingtheproof.
i i |H′| |H′|
17

<!-- Page 18 -->

ChatbotArena:AnOpenPlatformforEvaluatingLLMsbyHumanPreference

### D.SamplePrompts


### D.1.PromptExamplesFromDifferentClusters

Example1: Anexampleuserpromptfromthecluster"PythonGameProgrammingChallenge". Thispromptdistinctively
separatesGPT-4-0613performancefromLlama-2-70b-chat. Theuserrequest"higherqualitycode“fromeachassistant.
WhileGPT-4-Turboprovidesacorrectimplementationalongwithhelpfulexplanation,Llama-2-70b-chatfailtoprovideany
programandprovidedalesshelpfulresponseoverall.
<|User Prompt|>
Develop a snowman game similar to the Hangman game but draws a snowman
figure standing on the snow instead of a hangman. It also downloads (or
uses library) the complete English dictionary to select words for three
levels of difficulty. Think step-by-step, take a deep breath and choose
a higher quality code for each step.
<|GPT-4-0613’s Answer|>
Sure, here’s a step-by-step guide on how to create a Snowman game similar to
Hangman. We’ll use Python for this example.
Step 1: Import necessary libraries
‘‘‘python
import random
import urllib.request
‘‘‘
Step 2: Download the English dictionary
‘‘‘python
url = "https://raw.githubusercontent.com/dwyl/english-words/master/words.txt
"
urllib.request.urlretrieve(url, ’words.txt’)
‘‘‘
Step 3: Load the words from the dictionary and categorize them into three
levels of difficulty
‘‘‘python
with open(’words.txt’) as word_file:
english_words = word_file.read().split()
easy_words = [word for word in english_words if 4 <= len(word) <= 6]
medium_words = [word for word in english_words if 7 <= len(word) <= 9]
hard_words = [word for word in english_words if len(word) >= 10]
‘‘‘
Step 4: Create a function to randomly select a word based on the difficulty
level
‘‘‘python
def get_random_word(difficulty):
if difficulty == ’easy’:
word = random.choice(easy_words)
elif difficulty == ’medium’:
word = random.choice(medium_words)
else:
word = random.choice(hard_words)
return word.upper()
‘‘‘
Step 5: Create a function to print the snowman
18

<!-- Page 19 -->

ChatbotArena:AnOpenPlatformforEvaluatingLLMsbyHumanPreference
‘‘‘python
def print_snowman(guesses):
snowman = [’ _____ ’, ’ ( ) ’, ’ ( ( ) ) ’, ’(___(___)_)’, ’
( ) ’, ’ ( ) ’, ’ ( ) ’, ’ ( ) ’, ’(
)’, ’ _______ ’]
for i in range(guesses):
print(snowman[i])
‘‘‘
Step 6: Create the main function for the game
‘‘‘python
def play_snowman():
difficulty = input("Choose difficulty (easy, medium, hard): ")
word = get_random_word(difficulty)
guessed_letters = []
guesses = 0
print(’The word contains’, len(word), ’letters.’)
while guesses < 10:
guess = input("Guess a letter: ").upper()
if guess in guessed_letters:
print("You already guessed that letter.")
elif guess in word:
guessed_letters.append(guess)
print("Good job! The word contains that letter.")
else:
guesses += 1
print_snowman(guesses)
print("Sorry, the word does not contain that letter.")
print(’ ’.join(letter if letter in guessed_letters else ’_’ for
letter in word))
if set(guessed_letters) == set(word):
print("Congratulations! You’ve successfully guessed the word.")
break
else:
print("Sorry, you didn’t guess the word. The word was", word)
‘‘‘
Step 7: Run the game
‘‘‘python
play_snowman()
‘‘‘
This is a simple version of the game. You can enhance it by adding more
features like scoring, time limit, etc.
‘‘‘
19

<!-- Page 20 -->

ChatbotArena:AnOpenPlatformforEvaluatingLLMsbyHumanPreference
<|Llama-2-70b-chat’s Answer|>
Sure! Here’s a step-by-step guide to developing a snowman game similar to
Hangman, using the complete English dictionary for three levels of
difficulty.

### Step 1: Setting up the project

* Create a new Python project directory and initialize it with Git.
* Install the necessary libraries:
+ ‘numpy‘ for generating random numbers
+ ‘nltk‘ for accessing the English dictionary
+ ‘pygame‘ for creating the game graphics
+ ‘pydub‘ for playing sound effects (optional)
* Download the English dictionary dataset (e.g., from Kaggle) and store it
in a file named ‘dictionary.txt‘.

### Step 2: Loading the dictionary and generating words

* Use the ‘nltk‘ library to read the dictionary file and store the words in
a list.
* Split the list into three parts: easy, medium, and hard words, based on
their length and frequency of use.
* Shuffle the lists to randomize the order of the words.

### Step 3: Creating the game graphics

* Use ‘pygame‘ to create a window for the game, with a white background to
represent the snow.
* Draw a snowman figure on the background, using black rectangles for the
body, hat, and scarf.
* Add buttons for the player to submit their guesses.

### Step 4: Implementing the game logic

* Create a function to generate a random word from the appropriate
difficulty level and display it on the screen with missing letters (e.g
., _ _ _ _ _ _).
* Create a function to check if a guessed letter appears in the word, and
update the display accordingly (e.g., _ _ _ X _ _).
* Create a function to handle incorrect guesses, such as displaying a
warning message or playing a sound effect.
* Create a function to win the game, such as displaying a congratulations
message or playing a victory sound effect.

### Step 5: Adding sound effects (optional)

* Use ‘pydub‘ to play sound effects for various actions in the game, such as
guessing a letter correctly or incorrectly.
* Consider using a library like ‘pygame_mixer‘ to simplify the process of
playing sound effects in pygame.
20

<!-- Page 21 -->

ChatbotArena:AnOpenPlatformforEvaluatingLLMsbyHumanPreference

### Step 6: Testing and refining the game

* Test the game thoroughly to ensure that it works as expected, with no bugs
or errors.
* Refine the game mechanics and graphics as needed, based on player feedback
or personal preference.
* Consider adding additional features, such as keeping track of the player’s
score or implementing a time limit for each guess.

### Step 7: Packaging and distributing the game

* Package the game as a standalone executable file using a tool like
PyInstaller.
* Distribute the game to friends, family, or online communities, and gather
feedback for future improvements.
This is a high-level overview of the steps involved in creating a snowman
game similar to Hangman. Of course, the details will depend on your
specific implementation and the tools you choose to use. Good luck with
your project!
<|GPT-4-Turbo’s Judgment Verdict|>

### GPT-4-0613 Wins

ProgramOutput: BelowistheterminaloutputofthesnowmangameprogrammedbyGPT-4-0613,demonstratingits
correctness. ItisclearthatGPT-4-0613’sresponseismorehelpfulandrelevanttotheuser’srequest.
>>> python snowman.py
Choose difficulty (easy, medium, hard): easy
The word contains 6 letters.
Good job! The word contains that letter.

## _ A _ _ _ _


### Guess a letter: e

Good job! The word contains that letter.

## _ A _ _ _ E

Guess a letter: d
_____
( )
Sorry, the word does not contain that letter.

## _ A _ _ _ E

Guess a letter: g
_____
( )
( ( ) )
21

<!-- Page 22 -->

ChatbotArena:AnOpenPlatformforEvaluatingLLMsbyHumanPreference
Example2: Anexampleuserpromptfromthecluster"PythonGameProgrammingChallenge". Thispromptdistinctively
separatesGPT-4-0613performancefromLlama-2-70b-chat. Duetolimitedspace,thecodefromeachassistant’sresponseis
omitted.
<|User Prompt|>
Write a python function that prints a christmas tree in the form of a
triangle of asterisks, where the only input is size.
<|GPT-4-0613’s Code Output|>
>>> print_christmas_tree(5)
∗
∗∗∗
∗∗∗∗∗
∗∗∗∗∗∗∗
∗∗∗∗∗∗∗∗∗
<|Llama-2-70b-chat’s Code Output|>
>>> print_christmas_tree(5)
* * * * *
* * * *
* * *
* *
*
<|GPT-4-Turbo Verdict|>

### GPT-4-0613 Wins

Example3: Anexampleuserpromptfromthecluster"MovieRecommendations&Rating". Bothassistantretrievethe
correctmovieinformationandgaveanalmostidenticalexplanation. Therefore,thispromptcannotdistinguishGPT-4-0613’s
performancefromLlama-2-70b-chat.
<|User Prompt|>
Which film came out first, Blind Shaft or The Mask Of Fu Manchu?
<|GPT-4-0613’s Answer|>
The Mask of Fu Manchu was released in 1932, and Blind Shaft was released in

## Therefore, The Mask of Fu Manchu came out first.

<|Llama-2-70b-chat’s Answer|>
The Mask Of Fu Manchu came out first. It was released in 1932, while Blind
Shaft was released in 2003.
<|GPT-4-Turbo Verdict|>
Tie
22

<!-- Page 23 -->

ChatbotArena:AnOpenPlatformforEvaluatingLLMsbyHumanPreference
Example4: Anexampleuserpromptfromthecluster"TravelItineraryPlanning". Bothassistantprovidedanequally
helpfulitinerary. Therefore,thispromptcannotdistinguishGPT-4-0613’sperformancefromLlama-2-70b-chat.
<|User Prompt|>
Can you make a list of things I could do with my girlfriend in Lille,

### France?

<|GPT-4-0613’s Answer|>
Absolutely, here are some suggestions for activities you and your girlfriend
can enjoy in Lille, France:

## Visit the Palais des Beaux-Arts: This is one of France’s largest museums

and it’s right in the heart of Lille. It houses collections of European
paintings, a medieval and Renaissance collection, ceramics, French
sculptures and more.

## Explore the Vieux Lille: Stroll through the charming old town with its

Flemish influenced architecture, chic boutiques, and delightful eateries
.

## Visit the Lille Cathedral (Basilique-cathedrale Notre-Dame-de-la-Treille)

: This beautiful cathedral is a mix of modern and traditional
architecture.

## Enjoy a picnic at the Citadel Park: This is a great place to relax, have

a picnic, and enjoy the outdoors.

## Visit the LaM (Lille Metropole Musee d’art moderne, d’art contemporain et

d’art brut): This museum is home to a unique collection of modern and
contemporary art.

## Take a boat tour on the Deule River: This is a romantic way to see the

city and its surroundings.

## Visit the Maison Natale de Charles de Gaulle: This is the birthplace of

Charles de Gaulle and it’s now a museum dedicated to his life and work.

## Explore the Marche de Wazemmes: This is one of the largest markets in

France and it’s a great place to buy local products.

## Enjoy a meal at a local restaurant: Lille is known for its delicious

cuisine, so make sure to try some local dishes.

## Visit the Lille Zoo: This is a small but well-kept zoo that houses about

70 different species.

## Take a romantic walk through the Jardin des Plantes de Lille: This

botanical garden is a peaceful place to enjoy nature.

## Visit the Musee de l’Hospice Comtesse: This museum is located in a

former hospital and it’s home to a collection of art and artifacts from
the Middle Ages.

## Enjoy a performance at the Lille Opera: Check the schedule and book

tickets for a romantic night out.

## Take a day trip to the nearby city of Bruges: This charming Belgian city

is just a short train ride away.

## Visit the Le Palais Rihour: This palace houses the Lille Tourist Office

and it’s also home to the Salle du Conclave, which has a beautiful
Gothic fireplace.
Remember to check the opening times and any COVID-19 restrictions before you
visit. Enjoy your trip!
<|Llama-2-70b-chat’s Answer|>
Sure! Lille is a beautiful city in northern France that offers a variety of
activities for couples to enjoy. Here are some ideas for things you could
23

<!-- Page 24 -->

ChatbotArena:AnOpenPlatformforEvaluatingLLMsbyHumanPreference
do with your girlfriend in Lille:

## Explore the city’s charming streets and historic landmarks, such as the

Grand Place, the Vieille Bourse, and the Cathedral of Lille.

## Visit one of the many museums, such as the Palais des Beaux-Arts de Lille

, the Musee d’Art Moderne, d’Art Contemporain et d’Art Brut, or the
Musee de l’Hospice Comtesse.

## Take a stroll along the canal and enjoy the views of the city from the

waterfront.

## Visit the famous Lille Christmas market, which takes place every year in

December and features festive stalls, food, and drinks.

## Go shopping at the city’s many boutiques and galleries, or at the large

shopping centers such as the Euralille or the Lille Europe.

## Enjoy a romantic dinner at one of Lille’s many excellent restaurants,

such as the Michelin-starred Le Comptoir du Relais or the cozy Le
Bistrot d’Alsace.

## Take a day trip to the nearby city of Bruges, Belgium, which is known for

its picturesque canals and medieval architecture.

## Go to a show or concert at the Lille Opera or the Le Zenith concert hall.


## Visit the nearby town of Roubaix, which is famous for its textile

industry and its beautiful Art Deco architecture.

## Take a walk in the beautiful Parc de la Citadelle, which offers a

peaceful escape from the city and features a pond, a botanical garden,
and a zoo.

## Go on a bike ride or a hike in the surrounding countryside, such as the

Parc Naturel Regional Nord-Pas de Calais.

## Visit the famous Lille flea market, which takes place every Sunday and

offers a wide range of antiques, vintage items, and second-hand goods.

## Take a cooking class together and learn how to make some of the region’s

delicious specialties, such as carbonnade flamande (beef stew) or tarte
au maroilles (cheese tart).

## Go on a wine tasting tour and discover the region’s excellent wines,

such as the Chablis or the Champagne.

## Take a hot air balloon ride over the city and enjoy a bird’s-eye view of

Lille’s beautiful architecture and surroundings.
These are just a few ideas to get you started. Lille is a vibrant and
romantic city that offers many opportunities for couples to have a great
time together. Bon voyage !
<|GPT-4-Turbo Verdict|>
Tie
24

<!-- Page 25 -->

ChatbotArena:AnOpenPlatformforEvaluatingLLMsbyHumanPreference

### D.2.ArenaBenchPrompt

Example1: AnpromptfromArenaBenchrequiringaveryhighlevelofcomplexproblem-solvingskillandreasoningwhile
adheringtoreal-worldapplication.
Create a flutter app for habit tracking that tracks daily habits for a user.
The user should be able create multiple daily tasks that he wants to track.
And he should be able to group the habits into a set of groups. One the
user completes a task, he is rewarded a number of points per task. The
app should have a page that summarize the total score per group. And the
aggregate score of all the groups of habits. This flutter app needs to be
compilable for both andriod and iOS.
Example2: AnpromptfromArenaBenchrequiringaveryhighlevelofcomplexproblem-solvingskillandreasoningwhile
adheringtoreal-worldapplication.
I want to set up a remote raspberry pi zero, powered by a solar panel
with simple wiring. I want to power a small 2W pump, a simple electet
microphone, a custom python script running on the raspberry pi that is used
to classify audio detected by the microphone. What components will I need
to optimise for cost and minimise any electrical work (e.g. soldering)?
What size solar panel will I need to power this whole system?
25

<!-- Page 26 -->

ChatbotArena:AnOpenPlatformforEvaluatingLLMsbyHumanPreference

### D.3.ArenaBenchSystemPrompt

Thenovelevaluationprocedureisasfollow: wepromptGPT-4-Turbowiththesystempromptdisplayedbelowalongside
auserprompt, areferenceanswer, and2assistant’sanswers. Forreferenceanswer, wepresenttheuserpromptwith3
assistants’answers,GPT-4-Turbo,GPT-4-0314,andClaude-1,toGPT-4-TurboandaskGPT-4-Turbotogenerateananswer
totheprompt. Toensureconsistentpairwisejudgment,wesetupGPT-3.5-Turbo-0301asthebaselineanswerforallmodels
tobecomparedagainst. Toavoidpositionalbias,weconducttwojudgmentsperprompt: thefirstjudgmentpresentsthe
baselineanswerasAssistantAwhilethesecondjudgmentpresentsthebaselineanswerasAssistantB.Intotal,weconduct
700pairwisecomparisonsbetweeneachmodelagainstGPT-3.5-Turbo-0301across350userpromptstocalculateawin-rate
againstthebaseline. Thenweprojectthewin-rateonascalefrom0to10byassigningwinswithascoreof10,tieswitha
scoreof5,andlosseswithascoreof0. Further,weassignasignificantwinorlossas3winsor3losses,respectively,and
keepingtheotherverdictsasasinglewin,loss,ortie. Finally,wecalculatethefinalscorebyaveragingacrossthewins,
losses,andties.
<|System Prompt|>
Please act as an impartial judge and evaluate the quality of the responses
provided by two AI assistants to the user prompt displayed below. Your job
is to evaluate which assistant’s answer is better.
When evaluating the assistants’ answers, compare both assistants’ answers.
You must identify and correct any mistakes or inaccurate information.
Then consider if the assistant’s answers are helpful, relevant, and concise.
Helpful means the answer correctly responds to the prompt or follows the
instructions. Note when user prompt has any ambiguity or more than one
interpretation, it is more helpful and appropriate to ask for clarifications
or more information from the user than providing an answer based on
assumptions. Relevant means all parts of the response closely connect or
are appropriate to what is being asked. Concise means the response is clear
and not verbose or excessive.
Then consider the creativity and novelty of the assistant’s answers when
needed. Finally, identify any missing important information in the
assistants’ answers that would be beneficial to include when responding to
the user prompt.
After providing your explanation, you must output only one of the following
choices as your final verdict with a label:

## Assistant A is significantly better: [[A>>B]]


## Assistant A is slightly better: [[A>B]]


## Tie, relatively the same: [[A=B]]


## Assistant B is slightly better: [[B>A]]


## Assistant B is significantly better: [[B>>A]]

Example output: "My final verdict is tie: [[A=B]]".
26

<!-- Page 27 -->

ChatbotArena:AnOpenPlatformforEvaluatingLLMsbyHumanPreference

### D.4.ArenaBattleswithNoGroundTruth

Example1: AnexampleofanArenaBattlebetweenGPT-4-TurboandLlama-2-13B-chat,wheredependingondifferent
preferences,eitheranswercanbearguedasbetterthantheother. Whilebothanswersarecorrect,GPT-4-Turbo’sansweris
conciseandappropriatetotheformatofmultiplechoicequestion. Ontheotherhand,Llama-2-13B-chatprovideshelpful
explanationforthemultiplechoiceanswer.
<|User Prompt|>

### Multiple Choice Question

All plants have both a haploid and a diploid form. As the plant changes
from one form to another, this is called:
Multiple choice question.
alternative life cycle
succession
an alternation of generations
<|GPT-4-Turbo’s Answer|>
an alternation of generations
<|Llama-2-13B-chat’s Answer|>
The correct answer is: an alternation of generations.
Plants, like other organisms, have different life cycle stages, and they
can exist in two different forms: haploid and diploid. The haploid form
is a single set of chromosomes, while the diploid form is two sets of
chromosomes. As the plant changes from one form to another, this is called
an alternation of generations. This process involves the alternation of
haploid and diploid phases, and it is a fundamental aspect of the life cycle
of plants.
Alternative life cycle and succession are not correct descriptions of this
process, as they refer to different concepts. Alternative life cycle refers
to the different stages of life an organism may go through, such as larva,
pupa, and adult in insects, while succession refers to the process of one
species replacing another in a particular environment or niche.
Example2: AnexampleofanArenaBattlebetweenGPT-4-TurboandLlama-2-13B-chat,wheredependingondifferent
preferences,eitheranswercanbearguedasbetterthantheother.
<|User Prompt|>
What are critical elements of a Product Mindset for startup founders?
<|GPT-4-Turbo’s Answer|>
Adopting a Product Mindset is crucial for startup founders as it helps them
focus on creating products that deliver value to customers while achieving
business objectives. Here are some critical elements of a Product Mindset
for startup founders:

## Customer Centricity:

- Understand and empathize with your customers’ needs, problems, and
motivations.
27

<!-- Page 28 -->

ChatbotArena:AnOpenPlatformforEvaluatingLLMsbyHumanPreference
- Continuously gather and incorporate customer feedback into the product
development process.
- Prioritize features and improvements that directly address customer pain
points and enhance their experience.

## Value Proposition:

- Clearly define the unique value your product offers to the market.
- Align your product’s features and capabilities with its value proposition
to ensure it meets the expectations of your target audience.

## Problem-Solving Focus:

- Identify and focus on solving real problems for users rather than just
creating features for the sake of innovation.
- Validate assumptions and hypotheses through experimentation and user
testing.

## Iterative Development:

- Embrace an agile development approach, where you build, measure, and learn
in iterative cycles.
- Be open to pivoting or making significant changes based on feedback and
market response.

## Data-Driven Decision Making:

- Use data to inform decisions about product development, marketing, and
growth strategies.
- Establish key performance indicators (KPIs) to measure the success of the
product and track progress over time.
...
By internalizing these elements, startup founders can develop a strong
Product Mindset that guides their decisions and strategies, ultimately
leading to a product that customers love and that contributes to the
startup’s success.
<|Llama-2-13B-chat’s Answer|>
A product mindset is a way of thinking and approaching product development
that is critical for startup founders. Here are some essential elements of
a product mindset for startup founders:

## Customer-centricity: A product mindset starts with understanding the

customer’s needs, desires, and pain points. Founders must be obsessed with
their customers and be willing to put in the effort to understand their
needs.

## Iteration and experimentation: A product mindset is all about

experimentation and iteration. Founders must be willing to try new things,
test hypotheses, and iterate on their product based on customer feedback.

## Focus on value: A product mindset is focused on delivering value to

the customer. Founders must be able to identify and prioritize the most
important features and functionality that deliver the most value to their
customers.
28

<!-- Page 29 -->

ChatbotArena:AnOpenPlatformforEvaluatingLLMsbyHumanPreference

## Collaboration: A product mindset requires collaboration between

cross-functional teams, including engineering, design, and product
management. Founders must be able to work effectively with these teams to
develop a product that meets customer needs.

## Data-driven decision making: A product mindset is data-driven, and

founders must be comfortable using data to make informed decisions about
their product. This includes analyzing customer feedback, usage data, and
other metrics to inform product development.
...
By embracing these elements of a product mindset, startup founders can
develop a product that meets customer needs, delivers value, and sets their
company up for long-term success.
29

## Tables

**Table (Page 1):**

| Question Source Static Live Evaluation Ground Truth MMLU, HellaSwag, GSM-8K Codeforces Weekly Contests Metric Human Preference MT-Bench, AlpacaEval Chatbot Arena |  |  |  |
|---|---|---|---|
|  |  | Static | Live |
|  | Ground Truth | MMLU, HellaSwag, GSM-8K | Codeforces Weekly Contests |
|  | Human Preference | MT-Bench, AlpacaEval | Chatbot Arena |


**Table (Page 4):**

|  |  |  |  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0. | 000. | 680. | 69 0. | 750. | 710. | 76 0. | 770. | 750. | 76 0. | 790. | 860. | 90 |
| 0. | 320. | 000. | 50 0. | 590. | 610. | 59 0. | 590. | 590. | 62 0. | 720. | 700. | 80 |
| 0. | 310. | 500. | 00 0. | 540. | 560. | 50 0. | 570. | 520. | 69 0. | 730. | 600. | 87 |
| 0. | 250. | 410. | 46 0. | 000. | 540. | 48 0. | 510. | 560. | 58 0. | 530. | 730. | 84 |
| 0. | 290. | 390. | 44 0. | 460. | 000. | 42 0. | 540. | 550. | 58 0. | 630. | 670. | 76 |
| 0. | 240. | 410. | 50 0. | 520. | 580. | 00 0. | 490. | 550. | 58 0. | 610. | 640. | 73 |
| 0. | 230. | 410. | 43 0. | 490. | 460. | 51 0. | 000. | 560. | 58 0. | 630. | 720. | 71 |
| 0. | 250. | 410. | 48 0. | 440. | 450. | 45 0. | 440. | 000. | 54 0. | 680. | 650. | 62 |
| 0. | 240. | 380. | 31 0. | 420. | 420. | 42 0. | 420. | 460. | 00 0. | 610. | 580. | 61 |
| 0. | 210. | 280. | 27 0. | 470. | 370. | 39 0. | 370. | 320. | 39 0. | 000. | 530. | 57 |
| 0. 0. | 140. 100. | 300. 200. | 40 0. 13 0. | 270. 160. | 330. 240. | 36 0. 27 0. | 280. 290. | 350. 380. | 42 0. 39 0. | 470. 430. | 000. 480. | 52 00 |
|  |  |  |  |  |  |  |  |  |  |  |  |  |


**Table (Page 4):**

|  |  |  |  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 25 | 6411 | 8911 | 928 | 5830 | 5319 | 912 | 70 1 | 41 15 | 7 1 | 06 1 | 44 |
| 25 | 64 | 0 5 | 66 26 | 3 7 | 5622 | 2710 | 253 | 55 4 | 14 40 | 9 2 | 64 1 | 97 |
| 11 11 | 895 922 | 66 63 7 | 0 77 75 0 | 5 3 7 | 71 3 1 7 | 82 77 44 86 | 3 1 9 1 | 03 4 36 8 | 5 5 62 6 | 1 4 6 4 | 0 5 5 6 | 2 1 |
| 85 | 8 7 | 56 3 | 71 7 | 1 | 0 7 | 4 56 | 4 5 | 3 3 | 1 3 | 0 3 | 0 3 | 7 |
| 30 | 5322 | 273 | 82 74 | 4 7 | 4 | 0 35 | 1 6 | 50 1 | 13 11 | 7 7 | 5 1 | 14 |
| 19 | 9110 | 257 | 73 86 | 9 5 | 64 3 | 51 0 | 8 | 42 5 | 72 38 | 8 2 | 83 1 | 55 |
| 27 | 0 3 | 55 1 | 03 13 | 6 5 | 3 6 | 50 84 | 2 | 0 4 | 59 24 | 1 2 | 02 1 | 01 |
|  |  |  |  |  |  |  |  |  |  |  |  |  |
| 14 | 1 4 | 14 4 | 5 86 | 2 3 | 1 1 | 13 57 | 2 4 | 59 | 0 38 | 3 1 | 34 3 | 69 |
| 15 | 7 4 | 09 5 | 1 6 | 6 3 | 0 1 | 17 38 | 8 2 | 41 3 | 83 0 | 2 | 51 6 | 21 |
| 10 | 6 2 | 64 4 | 0 4 | 5 3 | 0 7 | 5 28 | 3 2 | 02 1 | 34 25 | 1 | 0 5 | 21 |
| 14 | 4 1 | 97 5 | 2 6 | 1 3 | 7 1 | 14 15 | 5 1 | 01 3 | 69 62 | 1 5 | 21 | 0 |


**Table (Page 6):**

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |


**Table (Page 7):**

|  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |


**Table (Page 8):**

|  |
|---|
|  |


**Table (Page 13):**

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 29779 | 29181 | 27726 22 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | 27726 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  | 22 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  | 849 | 17756 17562 17513 16968 1568 147 13 13 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  | 17756 | 17562 | 17513 | 16968 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  | 568 | 147 | 13 | 13 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  | 4 | 84 | 890 | 852 | 11826 | 11720 | 11209 | 10471 | 9562 8135 7929 7686 7420 7329 7309 7266 7018 7008 6711 6206 6018 5985 5961 5688 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 135 | 7929 | 7686 | 7420 | 7329 | 7309 | 7266 | 7018 | 7008 | 6711 | 6206 | 6018 | 5985 | 5961 | 5688 |


**Table (Page 13):**

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |


**Table (Page 14):**

|  |
|---|
|  |


**Table (Page 14):**

|  |
|---|
|  |
|  |
|  |


**Table (Page 14):**

|  |
|---|
|  |
|  |
|  |
|  |
|  |


**Table (Page 15):**

|  |
|---|
|  |


**Table (Page 15):**

|  |
|---|
|  |
