---
title: "Brittle Foundations ReAct"
original_file: "./Brittle_Foundations_ReAct.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["prompt-engineering", "llm", "rag", "chain-of-thought", "react"]
keywords: ["think", "spraybottle", "task", "put", "cabinet", "gpt", "page", "react", "next", "prompt"]
summary: "<!-- Page 1 -->

On the Brittle Foundations of ReAct Prompting for

### Agentic Large Language Models

MuditVerma* SiddhantBhambri* SubbaraoKambhampati
SchoolofComputingandAI

### ArizonaStateUniversity

{muditverma, sbhambr1, rao}@asu.edu

### Abstract

The reasoning abilities of Large Language Models (LLMs) remain a topic of
debate. SomemethodssuchasReAct-basedprompting,havegainedpopularity
for claiming to enhance sequential decision-making abilities of agentic LLMs. However, it is unclear wha"
related_documents: []
---

# Brittle Foundations ReAct

<!-- Page 1 -->

On the Brittle Foundations of ReAct Prompting for

### Agentic Large Language Models

MuditVerma* SiddhantBhambri* SubbaraoKambhampati
SchoolofComputingandAI

### ArizonaStateUniversity

{muditverma, sbhambr1, rao}@asu.edu

### Abstract

The reasoning abilities of Large Language Models (LLMs) remain a topic of
debate. SomemethodssuchasReAct-basedprompting,havegainedpopularity
for claiming to enhance sequential decision-making abilities of agentic LLMs.
However, it is unclear what is the source of improvement in LLM reasoning
with ReAct based prompting. In this paper we examine these claims of ReAct
basedpromptinginimprovingagenticLLMsforsequentialdecision-making. By
introducing systematic variations to the input prompt we perform a sensitivity
analysis along the claims of ReAct and find that the performance is minimally
influencedbythe"interleavingreasoningtracewithactionexecution"orthecontent
ofthegeneratedreasoningtracesinReAct,contrarytooriginalclaimsandcommon
usage. Instead,theperformanceofLLMsisdrivenbythesimilaritybetweeninput
example tasks and queries, implicitly forcing the prompt designer to provide
instance-specificexampleswhichsignificantlyincreasesthecognitiveburdenon
thehuman. OurinvestigationshowsthattheperceivedreasoningabilitiesofLLMs
stemfromtheexemplar-querysimilarityandapproximateretrievalratherthanany
inherentreasoningabilities.
1 Introduction
LargeLanguageModels(LLMs)haveseenrapidadvancementsspecificallyinNaturalLanguage
ProcessingandUnderstanding(NLP&NLU).LLMshaveunparalleledcapabilitiesintextgeneration,
summarization,translation,questionansweringtonameafew. [Bubecketal.,2023]. Motivatedby
thesecapabilitiesofLLMs,therehasalsobeenarushtolookforotheremergentabilities–especially
forreasoningandplanning. ApopularwayofenhancingLLMperformanceonreasoning/planning
taskshasbeenin-contextpromptingorprompt-engineering[Sahooetal.,2024]toincludeinstructions
[Giray,2023],syntaxstructure[Marvinetal.,2023],criticismandplanguidancewithverification
[Kambhampatietal.,2024]etc. Amongtheseapproaches,ReAct[Yaoetal.,2022]standsoutwhich
claimstoimproveLLMplanningabilitiesthroughtheuseofreasoningtracesinterleavedwithaction
executiongivenasplanguidance. Whiletheiroriginalstudyincludesmultipledomainstaskssuchas
questionansweringonHotPotQAandFEVERdatasets[Yangetal.,2018,Thorneetal.,2018],in
thispaperweareparticularlyinterestedinplanningtaskswhereReActclaimssuperiorperformance.
InourinitialexperimentswithReActforplanning,wefoundthatthesystemisoverlydependent
onthesyntacticsimilarityoftheexamplepromptandthequeryandisextremelybrittletominor
perturbations to the input prompt. For example, when provided with an explicit set of examples
ofpick-and-place-objecttaskandaskedtoplanforapick-and-place-two-objectstask,itshouldbe
trivialtogeneralizethesolutionoftheexamplestothequeriedtask. Unfortunately,evensuchaminor
variationtotheoriginalReActagentsetupdisruptsitsperformance.
Preprint.Underreview.
4202
yaM
22
]IA.sc[
1v66931.5042:viXra

<!-- Page 2 -->


### ReAct

Interact with a household to solve a task. Here are two examples.
<EXAMPLE 1 of same task as QUERY>
You are in the middle of a room ... <Task Description> Your task is to : put some spraybottle on toilet.
Act 1: think : To solve the task, I need to find and take a spraybottle, then put it on toilet.
Obs 1: OK.
Act 2: think : First, I need to find a spraybottle. A spraybottle is more likely to appear in cabinet (1-4),
countertop (1), toilet (1), sinkbasin (1-2), garbagecan (1).
I can check one by one, starting with cabinet 1.
Obs 2: OK.
Act 3: go to cabinet 1.
Obs 3: On the cabinet 1, you can see cloth 1, a soapboar 1, a soapbottle 1. Interleaved Think tag
... Reasoning Trace / Guidance
Act 6: think : Now I find a spraybottle (2), next I need to to take it.
Obs 6: OK. Example Task / Query Task
...
<EXAMPLE 2 of same task as QUERY>
...

## <Query>

Here is the task. You are in the middle of the room ... Your task is to put some soapbottle in toilet.
Figure 1: An example of ReAct in AlfWorld. We highlight the main components of ReAct, i.e.,
Interleavedreasoningandacting,thereasoningtrace/planguidanceandtheexampleandquerytask.
GiventheseeminglywidespreadadoptionofReActmethodology,thebrittlenesswewitnessedcalls
forasystematicstudyofthefactorscontributingtotheperformanceofReAct-basedLLMAgents.
Basedontheclaimsof[Yaoetal.,2022],weisolatethreepossiblereasonsfortheclaimedperformance
ofReActframework: 1)theutilityofinterleavingreasoningtraceduringactionexecution,2)the
utilityofprovidingplanguidance,and,3)thesignificanceofexamplepromptprovidedtothethe
LLM. However, the brittleness of ReAct becomes apparent when considering the variability in
promptdesigns. Dependingonthedomainandtask,promptdesignersmayprovideabstractguidance,
task-specificinstructionswithinthesamedomain,analogicalexamples,orglobalreasoningtraces.
ReAct’sinabilitytorobustlyadapttosuchvariationsunderscoresitslimitationsinhandlingdiverse
input prompts, thereby necessitating a closer examination of its design and implementation. In
thiswork,wesystematicallyevaluatethebrittlenessofReActbystudyingwhichpotentialfactors
contribute to its performance. This analysis is conducted through variations in input prompts to
understandhowaReActLLMAgentrespondsto(1)wheretheguidanceisprovided,(2)thedifferent
typesandstructureofthisguidance,andfinally,(3)onvaryingtheresemblanceofexampleprompt
tothequeriedproblem. Weinvestigatetheresearchquestions:
RQ1: Doestheagentperformancedependoninterleavingreasoningtracewithactionexecution?
RQ2: Howdoesthenatureofthereasoningtraceorguidanceinformationaffecttheperformanceof

### LLMAgents?

RQ3: Howdoesthesimilaritybetweentheexample〈problem,solution〉andthequery〈problem,? 〉,
whicharepresentintheprompt,affectLLMAgentperformance?
WeconductextensiveexperimentsontheAlfWorlddomainusingvariousLLMModels,including
GPT-3.5-turbo,GPT-3.5-instruct,GPT-4andClaude-Opus. Throughourcomprehensiveempirical
study, answer each of the research questions above. (RQ1) We find that LLM performance infactimproveswhenthereasoningtraceisnotinterleavedwithactionexecution. (RQ2)Moreover,
providingweakerguidanceorplacebo-guidance(wherethetextprovidesnoinformationaboutthe
task)hascomparableperformancetostrongreasoningtracebasedguidance. AnswerstoRQ1and
RQ2highlightthatthesourceofReActLLMagentperformanceisnottheinterleavingaspectorthe
contentofthereasoningtrace. Finally,(RQ3)weseethatvariationstotheexamplepromptsuchthat
itbelongstodifferenttaskwithinthesamedomain,orhasadifferentgoalorplanattributesthanthe
queriedproblem;causestheperformanceofReAct-LLMAgenttoplummet.
Our findings highlight that the benefits of ReAct-based LLM Agents are present when prompt
engineerscancurateinstance-specificexamples.Thisapproachmaynotscalefordomainswithalarge
numberofprobleminstanceclasses,anditplacesanundueburdenonpromptengineerstoprovide
instancespecificexamples. Finally,ourexperimentscallintoquestionclaimsofenhanced“emergent
reasoning"ofLLMswithpromptengineeringeffortssuchasReAct;corroboratingcontemporary
research[Vermaetal.,2024,Valmeekametal.,2024,Stechlyetal.,2024,Ullman,2023,Schaeffer
etal.,2023,McCoyetal.,2023]questioningreasoningabilitiesofLLMs.
2

<!-- Page 3 -->

2 Preliminaries
2.1 AlfWorld
AlfWorld Shridhar et al. [2020] is a synthetic text-based game built on top of a PDDL domain
description. ReActYaoetal.[2022]definessixtasks(orproblemclasses)withinthisdomainnamely
-Put, Clean, Heat, Cool, Examine, andPutTwo. Eachproblemclassconsistsofseveralproblem
instances,suchasputaspraybottleontoilet(seeFig. 1isanexampleinstanceofPutclass. Since
AlfWorldisapartiallyobservableenvironment,eachoftheseprobleminstancescanbesolvedby
navigatingandinteractingwiththeenvironmentsimulatorviatextactions. Forexample,thistaskcan
besolvedbythefollowingactions-go to cabinet 2, take spraybottle 2 from cabinet
2, go to toilet 1, put spraybottle 2 in/on toilet 1.
2.2 ReAct
ThethinkactiontagprovidedbyReActisclaimedtocompriseofReasoning+Actiontracethatis
providedinthesolutionfortheexampleproblemsaspartoftheprompt. Duringexecution,when
theLLMagentisqueried,theexpectationisthatitcangenerateathinkactiontagforthequeried
probleminstancethatissemanticallysimilartotheoneprovidedfortheexamplesintheprompt.
LocationofTHINKtagInReAct,theintegrationofthethinktagwithinactionsservestoexpand
theactionspace. Thisallowsthelanguagemodel(LLM)agenttoexecuteathinkaction,prompting
an‘OK’response. ThroughanalysisofexamplepromptsinReActexperiments,weidentifyvarious
instancesofthethinkaction. Typically,itappearsafterstatingtheprobleminstance,reiteratingthe
task,andprovidingproblem-specificguidance. However,theauthorsoffernostructuredguidelines
foritsimplementation,placement,orguidance. Thisobservationalignswithfeedbackfromreviewers
[OpenReview,2024]citinginconsistenciesinthepromptingformat.
ContentofTHINKtagInReAct,thethinkactionconsistentlyprovidesthedecision-makingagent
withsuccess-orientedguidancefortaskcompletion.Forinstance,uponencounteringaspraybottle,
the prompt might include: think: Now I find a spraybottle (2). Next, I need to
take it. Thisguidanceexposesforthcomingactionsandsub-tasksfortheagent.
FewshotEXAMPLEsIntheAlfWorlddomain(wihchisaPDDLdomain),ReActauthors[Yao
etal.,2022]classifysixproblemclassesortasks:Put, Clean, Heat, Cool, Examine, PutTwo.
Despiterepresentingdifferenttasks,theysharethesameenvironmentdynamicsandactionspace,
allowingforverysimilarexecutiontrace.Forinstance,aHeattaskmightinvolvePuttinganiteminto
amicrowave. InReActexperiments,authorsprovidetwoexampleproblem-solutionpairs(referredto
asexemplarsinourwork)beforequeryingtheLLMagentwithaprobleminstance. Authorsforce
ReActagenttouseexamplesandqueriesbelongingtothesameproblemclasswithoutmotivatingthis
designdecision. However,thequeriedproblemmaydifferinobjectsorlocationsfromtheexemplars.
3 RelatedWork
LargeLanguageModelshavebeenshowntobesuccessfulinaplethoraofnaturallanguagetasks
[Kocon´ etal.,2023,Gilardietal.,2023,Zhuetal.,2023,Bubecketal.,2023,Bhattacharjeeetal.,
2024]. However,therearetwoschoolsofthoughtwhenitcomestoutilizingoff-the-shelfLLMsfor
planningandreasoningtasks. WorkssuchasChainofThought,ReAct,andothersthatfollowed
[Weietal.,2022,Yaoetal.,2023,Long,2023,Yaoetal.,2024,Bestaetal.,2024,Fuetal.,2024,
Aksitovetal.,2023],havearguedaboutthereasoningabilitiesofLLMsbyproposingprompting
methods. Ontheotherhand,[Valmeekametal.,2024,Stechlyetal.,2024]haverefutedtheseclaims
byshowingtheinabilityofLLMstosolvedeterministicplanningandclassicalreasoningproblems.
In particular, for investigating the use of LLMs in solving decision making problems, AlfWorld
[Shridhar et al., 2020] is a popular domain that was originally proposed for training text-based
ReinforcementLearningagents. Lately,workssuchasReAct,Reflexion,andtheirothervariants
[Yaoetal.,2022,Shinnetal.,2023]havearguedontheprowessofLLMs’reasoningabilitieson
AlfWorld. Furthermore,therehavebeenseveralextensionstoReActthatboosttheirgeneralization
abilitiesacrossmoredomainsincludingmulti-modaldomains[Yangetal.,2023,Castrejonetal.,
2024],autonomousvehicles[Cuietal.,2024],tablequestionanswering[Zhangetal.,2023],etc.
WhiletheeffectivenessofReActiscelebratedacrossdifferentareas,theseworksonlydependon
anthropomorphizationofLLMsforusingReActbasedpromptingwithnojustificationonthesource
3

<!-- Page 4 -->

(RQ1 a) Exemplar-CoT

## <Example 1>

You are in the middle of a room ... <Task Description>
Your task is to : put some spraybottle on toilet.
Act 1: think : To solve the task, I need to find and take a spraybottle, then put it on toilet. First, I need to
find a spraybottle. A spraybottle is more likely to appear in cabinet (1-4), countertop (1), toilet (1),
sinkbasin (1-2), garbagecan (1). I can check one by one, starting with cabinet 1.
Now Once I find a spraybottle (2), next I need to to take it.
Now Once I take a spraybottle (2), next I need to put it in/on toilet (1).
Obs 1: OK.
Act 2: go to cabinet 1.
Obs 2: On the cabinet 1, you can see cloth 1, a soapboar 1, a soapbottle 1.
...
(RQ1 b) Anonymized Exemplar-CoT

## <Example 1>

You are in the middle of a room ... <Task Description>
Your task is to : put some spraybottle on toilet.

### Act 1: think : To solve the task, I need to find and

take a spraybottle the object, then put it on toilet the desired location. First, I need to find a
spraybottle the object. A spraybottle The object is more likely to appear in cabinet (1-4), countertop
(1),toilet (1), sinkbasin (1-2), garbagecan (1). one of the different locations. I can check one by one,
starting with cabinet 1 the first location.
Now Once I find a spraybottle(2) the object, next I need to take it.
Now Once I take a spraybottle (2) the object, next I need to put it in/on toilet (1) the desired location.
Obs 1: OK.
Act 2: go to cabinet 1.
Obs 2: On the cabinet 1, you can see cloth 1, a soapboar 1, a soapbottle 1.
...
(RQ2 a) Failure (RQ2 c) Ordering
... ...

### Act 3: open cabinet 2 Act 3: open cabinet 2

Obs 3: You open the cabinet 2. The cabinet 2 is open. Obs 3: You open the cabinet 2. The cabinet 2 is open.
In it, you see a candle 1, and a spraybottle 2. In it, you see a candle 1, and a spraybottle 2.
Act 4: think : Now I find a spraybottle 2.
Act 4: think : Now I find a spraybottle 2.
Next, I need to take it.
Act 4: put spraybottle 2 in/on toilet. Next, I need to take it.
Obs 4: Nothing happens. Act 4: think : Next, I need to take the
spraybottle 2. Now I find a spraybottle 2.
...
...
(RQ2 b) Failure + Explanation
... (RQ2 d) Placebo Guidance
Act 3: open cabinet 2
...
Obs 3: You open the cabinet 2. The cabinet 2 is open.

### Act 3: open cabinet 2

In it, you see a candle 1, and a spraybottle 2.
Act 4: think : Now I find a spraybottle 2. Obs 3: You open the cabinet 2. The cabinet 2 is open.
Next, I need to take it. In it, you see a candle 1, and a spraybottle 2.
Act 4: put spraybottle 2 in/on toilet. Act 4: think : Now I find a spraybottle 2.
Obs 4: Nothing happens. Next, I need to take it.
Act 5: think : Nothing happens because I do not Act 4: think : Take a deep breadth and work on
have spraybottle 2. this problem step by step.
... ...
Figure2: ExampleofpromptvariationsconsideredforRQ1andRQ2.
ofimprovementinperformance. ThismotivatesourworkininvestigatingthecomponentsofReAct
withrespecttosequentialdecision-makingproblemsandanalyzingtheroleeachcomponentplays.
4 BrittlenessofReActbasedAgenticLLMs
WeexaminetheclaimsofReActtounderstandtheperformanceofReAct-basedLLMagents. Itis
crucialtoassesswhetherReAct’sfundamentalassertionshold,particularlyinsequentialdecision
making. AsoutlinedinSection2,ReActcomprisesthreemaincomponents: interleavingthethink
tagwithactions,planguidanceafterthethinktag,andtheselectionofexemplarproblemsforLLM
prompts. Weperformasensitvityanalysisbyproposingalternativesalongthesethreedimensions.
Thesubsequentsectionsexplorethedesignofexemplarpromptvariationstoinvestigateourresearch
questionsconcerningtheclaimsofReAct. EachvariationmodifiesthebaseReActexemplarprompts.
4.1 RQ1: Interleavingthinkingwithacting
Doestheagentperformancedependoninterleavingreasoningtracewithactionexecution?
Toanswerthisresearchquestion,weproposecollatingtheguidanceinformationcontainedwithinthe
multiplethinktagspresentintheexamplesoftheinputpromptintoasinglethinktagappendedafter
theexampleproblemisspecified. ThisapproachcanbeinterpretedasChain-of-ThoughtKojimaetal.
[2022],Weietal.[2022],whereguidanceinformationisgeneratedbeforeactionexecution.
4

<!-- Page 5 -->

Variation1: Exemplar-basedCoTAlfWorldisapartiallyobservableenvironmentwhereanagent
can only observe objects after reaching that location. Hence, we remove specific location and
objectidentifierstomodifythethinkactionsthatareoriginallyinterleavedwithotheractionsinthe
environment. Forexample,werewriteitas: think: Now Once I find a spraybottle (2),
next I need to take it.. Finally,weappendallthethinkactionstogetheratthebeginningof
theexampleproblem. Intuition: Problem-specificguidanceforasequentialdecision-makingagent
canbegivenstep-by-step(asinReAct)orallatonce.
Variation 2: Anonymized Exemplar-CoT We take one step further and modify the think
tag to remove references to specific locations and objects, making it more general. For
example, think: To solve the task, I need to find and take a spraybottle the
object, then put it on toilet the desired location. Intuition: Exemplars can be
made more general by providing abstract guidance and exploting LLMs ability to identify necessarysemanticentityrelations.
4.2 RQ2: PlanGuidancefollowingthinktag
HowdoesthenatureofthereasoningtraceorguidanceinformationaffecttheperformanceofLLM?
ReActclaimstousereasoningtraceastheguidanceinformationfollowingthethinktag. Forinstance,
inReAct thoughtsareto(1)decomposethegoal(2)tracksubgoalcompletion(3)determinethe
next subgoal and (4) reason via common-sense where to find and object and what to do with it.
It is, however, unclear what is the motivation to use these as the reasoning trace. The potential
anthropomorphizationoflargelanguagemodels(LLMs)maysuggestthattheirthoughtprocesses
aresimilartotheabstractplanshumansmake,andthattheymustbepromptedinthesamemanner.
However,itisunclearwhythisassumptionshouldholdtrue. Alternativescanbe,wecanpromptthe
LLMtoreflectonpastfailuresandprovidepossibleexplanations(hindsight-guidance)orWecan
substitutetask-relevantguidancewithplacebo-guidancebyusing"magicincantations".
Variation1:FailureFromtheexamplepromptsusedinReAct,wenotethatnoneoftheexamplesfor
anytaskconsistofinvalidactions. Weinjecttwoinvalidactionsintheexecutiontrace: thefirstthat
attemptstoexecutetheactionpertinenttothetask(suchasput spraybottle 2 in/on toilet)
whennotpossibleand,second,executessomeotherinvalidaction. Weincludetheexpectedsimulator
response,Nothing happens.,wheninvalidactionsaretaken. Intuition: Reasoningtracecanbe
aboutwhattodosuchassubgoalsofthefuture,orwhatnottodosuchasmistakesinhindsight. This
shouldbeweakerguidancethaninbaseReActastheexemplarsdonotpointoutwhattodonext.
Variation2: Failure+ExplanationWeplacethinkactionsafterinvalidactionsinjectedinFailure Variation which consist of explanations for the failure such as think: Nothing happens
because I do not have a spraybottle 2. Intuition: Wecanaugmentpointingoutmistakes
inhindsightwithexplanationstoavoidsimilarfailures. ThisisstrongerguidancesignalthanFailure,
however,theexemplarsstillnotprovideinformationonwhattodonext.
Variation 3: Guidance Ordering LLMs are known to be susceptible to minor syntactic perturbations to inputs. We test whether it is true for guidance information given as prompt as
well. We identify chain of subtasks in a reasoning trace S → S ···S and reverse it to
1 2 n
be S → S ···S . For instance, think: Now I find a spraybottle (2). Next,
n n−1 1
I need to take it. becomes think: Next, I need to take the spraybottle (2).
Now I find a spraybottle (2). Intuition: LLM agent should be invariant to the syntax of
reasoningtraceifthesemanticinformationispreserved. Thisdoesnotchangethereasoningtrace
fromtheperspectiveofinformationcontent.
Variation4: PlaceboGuidanceItisuncleartowhatextentLLMagentusesthesupposedhelpful
thoughtsforthedecisionmakingtask. Inthisvariationwereplacethinktagguidancewithaplacebo
thoughtthatdoesnotcontainanytaskrelevantinformation, buthasbeenwidelyusedasprompt
engineeringtrick[Kojimaetal.,2022]. Intuition: AccordingtoclaimsofReAct, weexpectthe
performancetogetworsewhentheguidancedoesnothaveanyinformationusefulfortasksuccess.
4.3 RQ3: SimilaritybetweenEXAMPLEsandQUERY
Howdoesthesimilaritybetweentheexample〈problem,solution〉andthequery〈problem,? 〉,which
arepresentintheprompt,affectLLMAgentperformance?
RQ3investigatestheroleofexamplesimilaritytothequeryinLLMagent’sperformance.Establishing
problemsimilaritycanbechallenging,especiallywhereminorvariationstotheproblemcanhave
5

<!-- Page 6 -->

Table1: AverageSuccess%ofLLMonBaseReActandpromptvariationsforRQ1andRQ2onsix
AlfWorldtasks.

## H1 H2


### Model/Prompt Base

CoT Anon. CoT Magic Order Failure Explanation

### GPT-3.5-Turbo 27.6 46.6 41 30 28.3 43.3 41.6

GPT-3.5-Instruct 44.7 61.9 50.7 41 42.5 47 44.7

## Gpt-4 23.3 43.3 33.3 36.6 30 50 36.6


### Claude-Opus 56.6 50 46.6 30 50 53.3 30

varied interpretations (such as an analogy to a different task altogether). Our work explores this
challenge in a systematic way. During example prompt construction, prompt designers may use
synonymstorefertoobjects(Domain),comeupwithexampleswheretheagenttaskisthesameas
querybutthegoalsaredifferent(Instance),orprovideoptimalsolutionsastheexamples(Optimal)
preventingLLMtoobtaininformationregardingexplorationstrategy. Furthermore,giventhatthe
domainhasthesameunderlyingactiondynamicsandthatthetasksreuseseveralactions,prompt
designersmaychoosetoprovidequeryspecificexampleprompts(asinbaseReAct),provideone
ofadifferenttaskandoneofthesametask(One),providebothexamplestobeofadifferenttask
(Both),ortakeanexhaustiveapproachandprovideoneexampleofalltasks(All).
Variation1:Synonyms-(Domain)Forthisvariation,wereplacetheobjectandlocationnamesinthe
examplepromptswiththeirsynonyms. Forexample,spraybottle → aerosolbottle,cabinet
→ cupboard,and,microwave → oven. Wemake36suchchangestoobjectandlocationnames
acrossalltheexamples. Notethattheobjectnames/locationareunchangedfortheproblemquery
andsubsequentinteractionwiththesimulator. Intuition: Exemplarguidancemaybespecifiedwith
alternatesynonymousobjectandlocationnames. Reasoningagentsshouldbeinvarianttovariable
namesubstitutionforclosedworlddynamicssuchasPDDLbasedAlfWorld.
Variation2: ProblemInstance-level-InstanceWeinjectinstance-levelchangestotheexamples
providedintheprompts. RecallthatweareupdatingthebaseReAct’sprompts,wheretheexemplar
tasksaresameasthequery. Wechangethegoallocationinexemplarproblemtoensurethatitdoes
notmatchwithanyofthegoallocationsinqueryproblem. Moreover,weaddrepetitiveyetfutile
actions in the exemplar execution trace which does not effect the solution. Intuition: Ensuring
a different goal location in exemplar from the queried problem is a natural usecase. Moreover,
exemplarsmaycontainarbitraryexplorationstrategiessuchasactionrepetition[Sharmaetal.,2017].
ByReAct’sclaims,LLMagentperformanceshouldnotbeaffected.
Variation3: ProblemLevel-Both, One, AllRecallthattheenvironmentdynamicsforallthe
tasksarethesame. Infact,severaltaskssubsumetheuseofourtaskssuchasHeatrequirestheagent
toPutanfoodinthemicrowave. Ingeneral,allthetaskssharealargeportionofactions(suchas
exploringcabinetsandlocations,pickingobjectsetc.). Motivatedbyhowtightrelationshipofthese
taskswecomeupwiththreevariations. First,One,usesoneexemplarofanarbitrarilypickedtask
andtheotherexemplarofthesametaskasthequery. Second,Both,usesbothexemplarsfroman
arbitrarilypickedtask. Finally,All,usesatotalofsixexemplars(thisistheonlyvariationwhere
we provide more than the standard two examples as in ReAct) corresponding to each task under
consideration. Remember, this includes the query task which is always present at the end in the
inputprompt. Intuition: Withaverysimilaractionexecutiontrace(suchasexploration,pickingand
placingobjects)acrosstasks,andshareddynamics,LLMagentshouldbeminimallyaffectedbythe
useofexemplarsofadifferenttask.
Variation4: ExplorationStrategy-OptimalAsnotedbefore,ReActdoesnotexplainthechoice
ofexemplarsused. Animportantingredienttotheexemplarsistheexplorationstrategyused. Inthis
variationweprovideexemplarswhichserendipitouslytaketheoptimalactions(asiftheenvironment
werefullyobservable)andthereforetheexampleplanistheshortestpossible. Intuition: Exploration
strategy exposed in exemplars (that too for the same problem task) should not impact ReAct’s
performanceiftheLLMagentisreasoninginsteadofretrieval(orpatternmatching).
5 Results
Inthefollowingsub-sections,wewillanswerourRQsthroughsensitivityanalysisusingtheproposed
promptvariationsalongthreedimensions,thelocationofthethinktag,thecontentofthethinktag,
6

<!-- Page 7 -->

GPT 3.5 Turbo GPT 3.5 Instruct GPT 4 Claude Opus
100 Put 100 Put 100 Put 100 Put
PutTwo 75 CleanPutTwo 75 CleanPutTwo 75 CleanPutTwo 75 Clean
50 50 50 50
25 25 25 25
0 0 0 0

### Heat Heat Heat Heat

Examine Examine Examine Examine

### Cool Cool Cool Cool

Figure3:TheradarchartshowsthefailureratesofvariousLLMswithdifferentReAct-basedprompt
settingsforRQ1(BaseReact,Global,Anonymized)acrosssixAlfworldtasks(hexagonvertices).
Highervalues/Largershadedregionindicateworseperformance.
GPT 3.5 Turbo GPT 3.5 Instruct GPT 4 Claude Opus
100 Put 100 Put 100 Put 100 Put
PutTwo 75 CleanPutTwo 75 CleanPutTwo 75 CleanPutTwo 75 Clean
50 50 50 50
25 25 25 25
0 0 0 0

### Heat Heat Heat Heat

Examine Examine Examine Examine

### Cool Cool Cool Cool

Figure4:TheradarchartshowsthefailureratesofvariousLLMswithdifferentReAct-basedprompt
settingsforRQ2(BaseReact,Magic,Failure,Failure+Explanation,Ordering)acrosssixAlfworld
tasks(hexagonvertices). Highervalues/Largershadedregionindicateworseperformance.
and the similarity between exemplars and queried problems. All the variations modify the base
ReActpromptsandwedonotpresentacrossbetweenvariationsunlessotherwisenoted. Weuse
GPT-3.5-Turbo,GPT-3.5-Instruct,GPT-4,andClaude-Opuswhichareallnewermodelsthanthose
benchmarkedinReAct[Yaoetal.,2022]. Asnoted,weuseAlfWorlddomainconsistentwiththe
setupin[Yaoetal.,2022]. GPT3.5(Turbo,Instruct)resultsareon134instancesacrosssixtasks,
GPT-4/Claude-Opuson60instances(10foreachtask)duetocostconsiderations.
5.1 Utilityofinterleavingreasoningtracewithactionexecution
From Table 1(RQ1) note that the exemplar CoT and the anonymized exemplar CoT performs
significantlybetterthanbaseReActforallGPT-Xfamilyofmodels. Moreover,theperformance
dips slightly for Claude-Opus along these variations. From Fig. 3 (larger area represents worse
performance),weobservethatbaseReActconsistentlyperformsworseinmostofthetasks. This
refutesReAct’sfirstclaimontheimportanceofinterleavingreasoningtracegenerationwithaction
execution. EveninthecaseoftheClaudewherethereisaslightdipinperformance,themodels
seemstobeperformingatreasonablyhighsuccessratewhichquestionstheimportanceofinterleaved
reasoningandactionexecution.
5.2 UtilityofGuidanceInformationfollowingthinktag
Recallthatreasoningtraceguidancepertainstotheprospectiveactionsorbehaviorsanagentshould
execute(foresightguidance). Thistypeofguidanceismoreinformativecomparedtoothervariations,
suchashindsightguidance,whichfocusesonpasterrorswithoutprovidingfuturesolutionsteps,and
placeboguidance,whichisentirelyunrelatedtothetask. ReActclaimsthatreasoningtraceiscrucial
7

<!-- Page 8 -->

Table2: AverageSuccess%ofLLMonBaseReActandpromptvariationsforRQ3onsixAlfWorld
tasks. OC:Outofcontextlimit

## Rq3


### Model/Prompt Base


### Domain Instance Optimal All One Both


### GPT-3.5-Turbo 27.6 1.6 30 20.1 32 28.3 1.6

GPT-3.5-Instruct 44.7 47.6 42.5 39.5 OC 17.9 5.2

## Gpt-4 23.3 13.3 23.3 50 23.3 16.6 0


### Claude-Opus 56.6 50 46.6 43.3 50 60 6.6

GPT 3.5 Turbo GPT 3.5 Instruct GPT 4 Claude Opus
100 Put 100 Put 100 Put 100 Put
PutTwo 75 CleanPutTwo 75 CleanPutTwo 75 CleanPutTwo 75 Clean
50 50 50 50
25 25 25 25
0 0 0 0

### Heat Heat Heat Heat

Examine Examine Examine Examine

### Cool Cool Cool Cool

Figure5:TheradarchartshowsthefailureratesofvariousLLMswithdifferentReAct-basedprompt
settingsforRQ3(BaseReact,Domain,Instance,All,Both,One)acrosssixAlfworldtasks(hexagon
vertices). Highervalues/Largershadedregionindicateworseperformance.
forLLMagentperformance,whichwouldpredictadeclineinperformancewithhindsightguidance
andacollapsewithplaceboguidance. Incontrast,ourfindingsinTable1indicatethathindsight
guidance(Failure, Explanation)actuallyimprovetheperformanceoftheGPTfamilyofmodels.
The Claude-Opus model’s performance remains stable with hindsight (Failure) guidance and
declineswithplaceboguidance. Figure4illustratesthesemodels’performanceacrosssixAlfWorld
tasksandvariations,showingthattheperformanceofLLMseitherimprovedorremainedconsistent
when provided with weaker or irrelevant guidance information. This refutes ReAct’s claim that
task-specificreasoningtraceisthesourceofLLMagentperformance.OurargumentthatLLMagent’s
performanceisonlyslightlyaffectedbythereasoningtraceexplainstheindifferencetoordering
perturbationaswell. IftheLLMisnotutilizingthereasoningtracefordecisionmaking,changein
orderingwouldnotaffecttheagent’sperformance. Finally,contrarytothegeneralperceptionthat
betterGPTmodelswouldimproveoverreasoning,wefindthatGPT-4’sperformanceistheworst
amongGPT-XfamilyfurtherhighlightingthebrittlenessofclaimsofReAct.
5.3 UtilityofExemplarsimilaritytoQuerytask
Intuitively,thesimilarityofDomainexamplesisclosestwithbaseReAct,followedbyInstance
and Optimal variations. Finally, All contains an overload of information followed by One and
Bothwhichhasthesameactionspacebutusesdifferenttasksasexemplars. RecallthatAlfWorld
beingaPDDLdomainhasasharedenvironmentdynamicsacrossalltaskswithupto 80%ofactions
sharedacrossexecutiontraces. WhileReActdoesnotinvestigateimpactofvariedexemplars,given
thepopularusageoneexpectsLLMstoberobusttosuchchangesespeciallyinacommon-sense
householddomain. Table2showstheseverebrittlenessofReActbasedLLMagenttoevenminor
variations(suchasDomain, Instance). Specifically,performanceofGPT-3.5-TurboandGPT-4
plummentsforDomain. Claude-OpuswhichwasmorerobustinRQ1,RQ2,isalsoimpactedseverely
byDomain, Instancevariations. Furthermore,whenwedonotexposetheexplorationstrategy
andonlyprovideOptimalexemplars,theperformanceofLLMagentsfurtherdrops(exceptinGPT4).
OverloadingtheLLMswithmoreexemplarsAlldoesnotimpactitsperformance. Weposit,thisis
becausethequery-taskexemplarisstillpartofthelargeinputprompt. Amongthetwoexemplars,as
providedinReAct,whenoneofthemisofadifferenttask(One)thentheperformancesignificantly
reducesforLLMs. Whenbothoftheexemplarsareofadifferenttaskthentheperformancecollapses
tosingledigitsuccessratesforallthemodels. Thisisakeyresultofthisworkhighlightingthesevere
8

<!-- Page 9 -->

dependenceofLLMsonthesimilarityoftheexemplarstothequerytask.Throughsensitivityanalysis
usingourRQ3variationswecouldfindpartsoftheinput(thetasksimilarityoftheexemplarwith
query)whichisthesourceofReActperformance. Essentially,theLLMismimicking/performing
approximateretrievalfromthecontextpresentedtoit. Moreover,ourresultscorroboratesthelineof
researchthatpointsouttheinabilityofLLMstoreasonorplan.
UnrollingandSubtaskSimilarityWeperformadditionalexperimentswherethequerytaskisto
essentiallyrepeatthetaskintheexemplar(Unrolling). Forinstance,theexemplarisPutandthe
queryisPutTwotoputtwoobjectsatgivenlocation. Inthiscase,theLLMhastounrollthegiven
adviceandrepeatexemplartaskexecutiontosolvethequery. ThesuccessrateofGPT-3.5-Instruct
(thebestperformingGPTmodelinourexperiments)dropsdownfrom52%to9%. Similarly,we
experimentwithaSubtask Similarityvariationwheretheexemplartasksubsumesexecution
of the query task. For instance, the Heat task requires the agent to pick and place object in the
microwave(whichisaninstantiationofPuttask). OnewouldexpectthatHeatisagoodexemplar
forPut, however, theperformanceofGPT-3.5-instructmodelgoesfrom18%to0%inthiscase.
Theseresultsfurtherunderscorethebrittlenessandtheneedforinstance-specificexemplarsinReAct.
ThoughtoperationalizationabilityofLLMsGiventhefreeformnatureofthoughtgenerationand
arbitrary nature ofthought (about subtask, common-sense nextsteps etc.), checkingwhether the
generatedthoughtsarein-factreasonableisachallengingproblem. Forcompleteness,wefindthat
40%ofthetimesaftergenerationofathinktag,subsequentenvironmentactiontakenbytheLLMwas
invalid(forGPT-3.5-instruct). Itismuchhigher(80%forGPT-3.5-Turbo, 90%forClaude-Haiku)
forweakerLLMmodels. ThisfurtherhighlightstheinabilityofLLMstooperationalizeitsgenerated
thoughtasalsoseenin[Royetal.,2024]. Frommanualinspectionwefindthatthetypicalthoughts
wouldenlistallpossiblelocationsasnextlocationstovisitformostofthetasks. Asdemonstratedin
Section5.2,theperformanceofLLMsactuallydecreaseswhenprovidedwithforesightguidance,as
seenwiththebaseReActmodel. Adetailedinvestigationintothevalidityofthegeneratedreasoning
tracesisbeyondthescopeofthisworkandissuggestedasfutureresearch.
6 Conclusion
ReActbasedpromptengineeringmethodshavebeenclaimedtoimproveplanningabilitiesofLarge
LanguageModels. Inthisstudy,wecriticallyexamineReActalongthreedimensions,informedbyits
claimsandourhypothesesregardingitsperformancesources.ContrarytoReAct’sclaims,ourfindings
revealthatitsperformanceisneitherduetointerleavingreasoningtraceandguidanceinformation
generationwithactionexecution,norduetothespecificnatureoftheguidanceinformation. Instead,
weidentifythatthetruesourceofLLMperformanceinsequentialdecision-makingtasks,suchas
AlfWorld,isthehighdegreeofsimilaritybetweenexemplarproblems(few-shot)andthequerytask.
WealsoshowedthatReActissusceptibletotrivialvariationsinexemplarprompts(suchaswiththe
useofsynonyms,orUnrollingandSubtask Similaritycases). Ourfindingscautionagainstan
uncriticaladoptionofReAct-styleframeworksfortheirputativeabilitiestoenhanceperformancein
domainsrequiringplanning.
7 BroaderImpact&Limitations
Thisworkhighlightstheneedforcriticalexaminationofprompt-engineeringmethodswhichclaim
emergentabilitiesofLLMs. Absenceorpresenceofsuchabilitiescanhavealargeimpactonseveral
sectorssuchaseconomics,healthcare,transporttonameafew. Wehopehighlightingthebrittleness
ofpopularlyusedtechniquesuchasReActwillimproveexperimentationstandardsfortheagentic
LLMcommunity.
We deliberately confined our experiments to be deep along a domain considered common-sense
planningdomainbythecontemporaryresearchcommunity. Moreover,werestrictedourdiscussion
to sequential decision making problem of AlfWorld and admit that other prompting solutions to
reasoningproblemsmustbere-evaluatedwithsimilarscrutiny. Whilethiscanbeseenasapotential
limitation, ourexaminationofReActcanbeeasilytranslatedtootherdomainsofinterestbythe
consumerofthisresearch.
9

<!-- Page 10 -->


### References

Renat Aksitov, Sobhan Miryoosefi, Zonglin Li, Daliang Li, Sheila Babayan, Kavya Kopparapu,
ZacharyFisher,RuiqiGuo,SushantPrakash,PraneshSrinivasan,etal. Restmeetsreact: Selfimprovementformulti-stepreasoningllmagent. arXivpreprintarXiv:2312.10003,2023.
MaciejBesta,NilsBlach,AlesKubicek,RobertGerstenberger,MichalPodstawski,LukasGianinazzi,
JoannaGajda,TomaszLehmann,HubertNiewiadomski,PiotrNyczyk,etal. Graphofthoughts:
Solvingelaborateproblemswithlargelanguagemodels. InProceedingsoftheAAAIConference
onArtificialIntelligence,volume38,pages17682–17690,2024.
AmritaBhattacharjee,RahaMoraffah,JoshuaGarland,andHuanLiu. Towardsllm-guidedcausal
explainabilityforblack-boxtextclassifiers. 2024.
SébastienBubeck,VarunChandrasekaran,RonenEldan,JohannesGehrke,EricHorvitz,EceKamar,
PeterLee,YinTatLee,YuanzhiLi,ScottLundberg,etal. Sparksofartificialgeneralintelligence:
Earlyexperimentswithgpt-4. arXivpreprintarXiv:2303.12712,2023.
LluisCastrejon,ThomasMensink,HowardZhou,VittorioFerrari,AndreAraujo,andJasperUijlings.
Hammr: Hierarchicalmultimodalreactagentsforgenericvqa. arXivpreprintarXiv:2404.05465,
2024.
CanCui,YunshengMa,XuCao,WenqianYe,andZiranWang. Receive,reason,andreact: Drive
asyousay,withlargelanguagemodelsinautonomousvehicles. IEEEIntelligentTransportation
SystemsMagazine,2024.
DayuanFu,JianzhaoHuang,SiyuanLu,GuantingDong,YejieWang,KeqingHe,andWeiranXu.Preact: Predictingfutureinreactenhancesagent’splanningability. arXivpreprintarXiv:2402.11534,
2024.
Fabrizio Gilardi, Meysam Alizadeh, and Maël Kubli. Chatgpt outperforms crowd workers for
text-annotationtasks. ProceedingsoftheNationalAcademyofSciences,120(30):e2305016120,
2023.
LouieGiray. Promptengineeringwithchatgpt: aguideforacademicwriters. Annalsofbiomedical
engineering,51(12):2629–2633,2023.
Subbarao Kambhampati, Karthik Valmeekam, Lin Guan, Kaya Stechly, Mudit Verma, Siddhant
Bhambri,LucasSaldyt,andAnilMurthy. Llmscan’tplan,butcanhelpplanninginllm-modulo
frameworks. arXivpreprintarXiv:2402.01817,2024.
JanKocon´,IgorCichecki,OliwierKaszyca,MateuszKochanek,DominikaSzydło,JoannaBaran,
JulitaBielaniewicz,MarcinGruza,ArkadiuszJanz,KamilKanclerz,etal. Chatgpt: Jackofall
trades,masterofnone. InformationFusion,99:101861,2023.
TakeshiKojima,ShixiangShaneGu,MachelReid,YutakaMatsuo,andYusukeIwasawa. Large
languagemodelsarezero-shotreasoners. Advancesinneuralinformationprocessingsystems,35:
22199–22213,2022.
JieyiLong. Largelanguagemodelguidedtree-of-thought. arXivpreprintarXiv:2305.08291,2023.
Ggaliwango Marvin, Nakayiza Hellen, Daudi Jjingo, and Joyce Nakatumba-Nabende. Prompt
engineering in large language models. In International Conference on Data Intelligence and
CognitiveInformatics,pages387–402.Springer,2023.
RThomasMcCoy,ShunyuYao,DanFriedman,MatthewHardy,andThomasLGriffiths. Embers
ofautoregression: Understandinglargelanguagemodelsthroughtheproblemtheyaretrainedto
solve. arXivpreprintarXiv:2309.13638,2023.
OpenReview. ReAct: Synergizing Reasoning and Acting in Language Models. https://
openreview.net/forum?id=WE_vluYUL-X,2024.
ShamikRoy,SailikSengupta,DanieleBonadiman,SaabMansour,andArshitGupta. Flap: Flow
adheringplanningwithconstraineddecodinginllms. arXivpreprintarXiv:2403.05766,2024.
10

<!-- Page 11 -->

PranabSahoo,AyushKumarSingh,SriparnaSaha,VinijaJain,SamratMondal,andAmanChadha.
Asystematicsurveyofpromptengineeringinlargelanguagemodels: Techniquesandapplications.
arXivpreprintarXiv:2402.07927,2024.
RylanSchaeffer,KaterynaPistunova,SamarKhanna,SarthakConsul,andSanmiKoyejo. Invalid
logic,equivalentgains: Thebizarrenessofreasoninginlanguagemodelprompting. arXivpreprint
arXiv:2307.10573,2023.
SahilSharma,AravindSrinivas,andBalaramanRavindran. Learningtorepeat: Finegrainedaction
repetitionfordeepreinforcementlearning. arXivpreprintarXiv:1702.06054,2017.
NoahShinn,BeckLabash,andAshwinGopinath. Reflexion: anautonomousagentwithdynamic
memoryandself-reflection. arXivpreprintarXiv:2303.11366,2023.
MohitShridhar,XingdiYuan,Marc-AlexandreCôté,YonatanBisk,AdamTrischler,andMatthew
Hausknecht. Alfworld: Aligningtextandembodiedenvironmentsforinteractivelearning. arXiv
preprintarXiv:2010.03768,2020.
KayaStechly,KarthikValmeekam,andSubbaraoKambhampati. Ontheself-verificationlimitations
oflargelanguagemodelsonreasoningandplanningtasks. arXivpreprintarXiv:2402.08115,2024.
JamesThorne,AndreasVlachos,ChristosChristodoulopoulos,andArpitMittal. Fever: alarge-scale
datasetforfactextractionandverification. arXivpreprintarXiv:1803.05355,2018.
Tomer Ullman. Large language models fail on trivial alterations to theory-of-mind tasks. arXiv
preprintarXiv:2302.08399,2023.
KarthikValmeekam,MatthewMarquez,SarathSreedharan,andSubbaraoKambhampati. Onthe
planningabilitiesoflargelanguagemodels-acriticalinvestigation.AdvancesinNeuralInformation
ProcessingSystems,36,2024.
MuditVerma,SiddhantBhambri,andSubbaraoKambhampati. Theoryofmindabilitiesoflarge
languagemodelsinhuman-robotinteraction: Anillusion? InCompanionofthe2024ACM/IEEE
InternationalConferenceonHuman-RobotInteraction,pages36–45,2024.
JasonWei,XuezhiWang,DaleSchuurmans,MaartenBosma,FeiXia,EdChi,QuocVLe,Denny
Zhou,etal. Chain-of-thoughtpromptingelicitsreasoninginlargelanguagemodels. Advancesin
neuralinformationprocessingsystems,35:24824–24837,2022.
ZhengyuanYang,LinjieLi,JianfengWang,KevinLin,EhsanAzarnasab,FaisalAhmed,ZichengLiu,
CeLiu,MichaelZeng,andLijuanWang. Mm-react: Promptingchatgptformultimodalreasoning
andaction. arXivpreprintarXiv:2303.11381,2023.
ZhilinYang,PengQi,SaizhengZhang,YoshuaBengio,WilliamWCohen,RuslanSalakhutdinov,
andChristopherDManning. Hotpotqa: Adatasetfordiverse, explainablemulti-hopquestion
answering. arXivpreprintarXiv:1809.09600,2018.
Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik R Narasimhan, and Yuan
Cao. React: Synergizingreasoningandactinginlanguagemodels. InTheEleventhInternational
ConferenceonLearningRepresentations,2022.
ShunyuYao,DianYu,JeffreyZhao,IzhakShafran,TomGriffiths,YuanCao,andKarthikNarasimhan.
Treeofthoughts: Deliberateproblemsolvingwithlargelanguagemodels. AdvancesinNeural
InformationProcessingSystems,36,2024.
YaoYao,ZuchaoLi,andHaiZhao. Beyondchain-of-thought,effectivegraph-of-thoughtreasoning
inlargelanguagemodels. arXivpreprintarXiv:2305.16582,2023.
YunjiaZhang,JordanHenkel,AvriliaFloratou,JoyceCahoon,ShaleenDeep,andJigneshMPatel.
Reactable: Enhancingreactfortablequestionanswering. arXivpreprintarXiv:2310.00815,2023.
YimingZhu, PeixianZhang, Ehsan-UlHaq, PanHui, andGarethTyson. Canchatgptreproduce
human-generated labels? a study of social computing tasks. arXiv preprint arXiv:2304.10145,
2023.
11

<!-- Page 12 -->


### A ResourcesUsed

In this work we leverage OpenAI API and Claude API for prompting the Language Models. We use gpt-4-0613 for GPT4, gpt-3.5-turbo-0125, gpt-3.5-turbo-instruct,
claude-3-opus-20240229, claude-3-sonnet-20240229 and claude-3-haiku-20240307
for all our experimentation in April-May 2024. ReAct and corresponding experiments use approximately14Minputtokens(duetorepeatedpromptingaftereachactionexecution)and150K
outputtokensfor134probleminstancesasusedbyReAct.
B AdditionalConsiderations

### B.1 FailureRates

WereportfailureratesintheradarchartasinFigs.3,4,5and6insteadofsuccessrates.Weattempted
tovisualizetheseverebrittlenessgivenbythelargerareaoftheshadedregion. Since,forvariousof
ourRQvariationstheLLMsperformancewasverylow,wedecidedtoreportfailurerategivenas
(100-SuccessRate%)instead.

### B.2 PerformanceofClaude-Haiku

WeskiponmentioningtheperformanceofClaude-Haiku,sinceitwasnotabletogeneratesyntacticallycorrectactionsforanyoftheinstances. Wefoundthatfollowingourinstructiontogenerate
specificactionsasintheexemplarwasdifficult. Weimprovedtheprompttohavespecificinstructions
forgeneratingactions(SeeD.3)butitdidnotyieldanyimprovementsforClaude-Haiku. However,
theinstructiondidhelpwithClaude-SonnetandClaude-Opus. WefindthatClaude-Sonnetfollowsa
similarpatternasGPT-3.5-Instructaspresentedinourresults,anddecidedtofocusourselvesonthe
strongest/largestClaudemodel(Claude-Opus)forourevaluation.

### B.3 ExtensiontootherModels

WeareintheprocessofexperimentingwithGPT-4oandGoogleGeminimodels,APIsforwhich
werereleasedinMay2024whichdoesnotallowenoughtimeforthoroughandverifiedevaluation
beforetheconferencesubmission. Forcompleteness,however,wewillexperimentwiththeseAPIs
astheybecomeaccessibleandappendourresults.

### B.4 MainResultsonExemplarCoTvariant

WhilethisworkdoesnotinvestigateseffectivenessofexemplarChainofThoughtaspresentedin
RQ1,wedohowevertestthemainresultsoftheworkwithExemplarCoTtoidentifywhetherour
findingsholdtruethereaswell. Thatis,wetestRQ3-Both, RQ3-One. ForGPT-3.5-Turbowefind
thattheaverageperformancedropsfrom46.6%(RQ3-ExemplarCoT)asinTable1to28.3%inOne
and10.4%inBothvariationcases,andremainsat40.3%forAllvariation.

### C ExperimentDesign

EachofthevariationsproposedalongRQ1, RQ2andRQ3modifiesthefew-shotexamplesonly.
Remaining aspects such as the query problem or the interaction with the simulator is directly
inheritedfromtheReActcode-baseYaoetal.[2022]atpubliclyavailableathttps://github.com/
ysymyth/ReAct. Ourcodecanbefoundintheattachedsupplementarymaterial.
ExceptAllRQ3variation,allothersettingsusethestandardtwoexamplarsforpromptingtheLLM.
Dependingonthevariationwechangethecontentoftheexemplar. Fullpromptscanbefoundinthe
attachedsupplementarycode.

### C.1 Runningtheexperiments

Inourexperiments,accordingtothevariationstylewetaketheexemplarpromptsandusethesame
exemplarpromptsacrosstheinstancesofthequerytask. OtherthanRQ3-Both, Oneweusethe
12

<!-- Page 13 -->

GPT-3.5-Turbo

## Put

100
75

## Puttwo 50 Clean

25
0

## Examine Heat


## Cool


### Exemplar-CoT Ex-One Ex-Both Ex-All

Figure6: TheradarchartshowsthefailureratesofGPT-3.5-TurbowithourRQ3variantsonReAct
acrosssixAlfworldtasks. Highervalues/Largershadedregionindicateworseperformance.
exemplarofthesametaskasthequeryasdoneinReAct(andstillfindbrittlenessofReAct). ForRQ3
- Both, Oneweuseexactlytwoexemplarsbutofadifferenttaskthanquery. Finally, RQ3-All
istheonlyvariationthatprovidessixexemplars(insteadoftwo)andweforcetheexemplarofthe
query-tasktobeappendedattheendintheprompt. Thiswasthebestperformingpromptingstrategy
(onGPT-3.5-Turbo)amongstwhenthequery-taskexemplarwasplacedatthebeginning,atposition
4(middle)andattheend.

### C.2 Hyperparameters

Weusetemperature=τ =0foralloftheGPTandClaudemodelsandsetmax-tokens = 100
whichisborrowedfromReAct’shyperparameters. Restoftheparametersarekepttobedefaultas
specifiedintherespectivemodel’sAPIdocumentation.

### D ExamplePrompts

The full list of curated variations can be found in the supplementary materials. However, for
completeness we reference the prompt used for base ReAct (as in [Yao et al., 2022]) and our
variationsalongRQ1,RQ2andRQ3forthePuttask.

### D.1 SynonymSubstitutionmappingforDomain

Wemakethefollowingsubstitutionstotheobjectnames/locationsintheexemplarpromptinthe
Domainvariation. Notethatthesesubstitutionsaredoneonlytotheexemplar,andthequeryproblem
andsubsequentinteractionwiththeAlfWorldsimulatorusestheoriginalvocabularymapping.
spraybottle -> aerosolbottle
cabinet -> cupboard
countertop -> worktop
sinkbasin -> sinkbowl
toilet -> lavatory
toiletpaperhanger -> toiletpaperholder
towelholder -> towelrack
microwave -> oven
shelf -> rack
drawer -> deskdrawer
stoveburner -> hob
diningtable -> table
garbagecan -> trashbin
13

<!-- Page 14 -->

fridge -> refrigerator
peppershaker -> pepperpot
room -> livingroom
bread -> breadloaf
pan -> fryingpan
pot -> saucepan
book -> notebook
creditcard -> amexcard
mirror -> lookingglass
dresser -> chestofdrawers
sofa -> couch
cellphone -> mobilephone
coffeemachine -> coffeemaker
knife -> kitchenknife
spatula -> turner
soapbottle -> liquidsoapdispenser
saltshaker -> saltpot
statue -> sculpture
vase -> flowerpot
dishsponge -> spongewipe
desklamp -> tablelamp
sidetable -> nightstand

### D.2 ForAll, Both, One

All: Wetaketheexemplarpromptforeachtaskandconcatenateittogether.
Both: Weusethefollowingmappinggeneratedarbitrarily,toreplacetheexemplarpromptforthe
querytask.

## Variation_Mapping = {

’put’:’examine’,
’clean’:’cool’,
’heat’:’put’,
’cool’:’puttwo’,
’examine’:’clean’,
’puttwo’:’heat’
}
One: Weusethefirstexamplefromtheabovemapping,andthesecondexamplefromthesametask
asthequery.

### D.3 Buildingtheinputprompt

WeinheritReAct’swayofstichingtogethertheexemplarsandthequeryusingthefollowingprompt
templateas:
Interact with a household to solve a task. Here are two examples.’ + eg1
+ eg2 + INSTRUCTION + Here is the task. (TASK)´
InthecaseofGPTmodelsINSTRUCTIONisanemptystring. ClaudeModelsgave0%successrate
(regardlessofthemodelsize,i.e. Haiku,SonnetandOpus)withtheoriginalReActpromptdesign.
WeidentifiedthatClauderequiredanexplicitinstructiontogenerateonlytheactionsforthesimulator.

### WeaddedataskindependentINSTRUCTIONpromptas:

INSTRUCTION = " Only provide the one action at a time. Be concise, and
do not provide any extra information. Always start with the action. For
example, ’pick up apple’ is correct, but ’I want to pick up the apple’ is
not."
14

<!-- Page 15 -->

Interestingly,GPT-3-Turboperformancedroppedto1%(averagedacross6independentrunsover134
examples)withtheinclusionofthisINSTRUCTIONtag. Thisfurtherhighlightshowbrittleprompt
engineering is, and cautions us against misplacing our trust with ReAct in enhancing reasoning
abilitiesofLLMs.

## D.4 Rq1


### Prompt 1: rq1-anon-exemplar

Youareinthemiddleofaroom.Lookingquicklyaroundyou,youseeacabinet4,acabinet3,acabinet2,acabinet1,acoffeemachine
1,acountertop1,adiningtable3,adiningtable2,adiningtable1,adrawer1,afridge1,agarbagecan1,amicrowave1,asidetable1,
asinkbasin1,astoveburner4,astoveburner3,astoveburner2,astoveburner1,andatoaster1.
Yourtaskisto:findsomeappleandputitinsidetable.
>think:Tosolvethetask,Ineedtofindandtaketheobject,thenputitonthedesiredlocation.FirstIneedtofindtheobject.The
objectismorelikelytoappearinoneofthedifferentlocations.Icancheckonebyone,startingwiththefirstlocation.OnceIfindthe
object,nextIneedtotakeit.OnceItaketheobject,nextIneedtoputitin/onthedesiredlocation.

## Ok.

>gotofridge1
Thefridge1isclosed.
>openfridge1
Youopenthefridge1.Thefridge1isopen.Init,youseealettuce2,amug2,apotato2,andatomato1.
>gotodiningtable1
Onthediningtable1,youseenothing.
>gotodiningtable2
Onthediningtable2,youseeapineapple1.
>gotodiningtable3
Onthediningtable3,youseeabowl2,abowl1,abread2,andabread1.
>gotosidetable1
Onthesidetable1,youseeacup1,alettuce1,apeppershaker3,apotato1,andasaltshaker1.
>gotocountertop1
Onthecountertop1,youseeabutterknife1,adishsponge1,andasoapbottle1.
>gotosinkbasin1
Onthesinkbasin1,youseeacup2,aegg1,amug1,andapotato3.
>gotogarbagecan1
Onthegarbagecan1,youseeaapple3,andaegg3.
>takeapple3fromgarbagecan1
Youpickuptheapple3fromthegarbagecan1.
>gotosidetable1
Onthesidetable1,youseeacup1,alettuce1,apeppershaker3,apotato1,andasaltshaker1.
>putapple3in/onsidetable1
Youputtheapple3in/onthesidetable1.
15

<!-- Page 16 -->


### Prompt 2: rq1-exemplar

Youareinthemiddleofaroom.Lookingquicklyaroundyou,youseeacabinet4,acabinet3,acabinet2,acabinet1,acoffeemachine
1,acountertop1,adiningtable3,adiningtable2,adiningtable1,adrawer1,afridge1,agarbagecan1,amicrowave1,asidetable1,
asinkbasin1,astoveburner4,astoveburner3,astoveburner2,astoveburner1,andatoaster1.
Yourtaskisto:findsomeappleandputitinsidetable.
>think:Tosolvethetask,Ineedtofindandtakeanapple,thenputitinsidetable.FirstIneedtofindanapple.Anappleismore
likelytoappearinfridges(1),diningtables(1-3),sidetables(1),countertops(1),sinkbasins(1),garbagecan(1).Icancheckoneby
one,startingwithfridge1.OnceIfindanapple,nextIneedtotakeit.OnceIfindanapple,nextIneedtoputitin/onsidetable.

## Ok.

>gotofridge1
Thefridge1isclosed.
>openfridge1
Youopenthefridge1.Thefridge1isopen.Init,youseealettuce2,amug2,apotato2,andatomato1.
>gotodiningtable1
Onthediningtable1,youseenothing.
>gotodiningtable2
Onthediningtable2,youseeapineapple1.
>gotodiningtable3
Onthediningtable3,youseeabowl2,abowl1,abread2,andabread1.
>gotosidetable1
Onthesidetable1,youseeacup1,alettuce1,apeppershaker3,apotato1,andasaltshaker1.
>gotocountertop1
Onthecountertop1,youseeabutterknife1,adishsponge1,andasoapbottle1.
>gotosinkbasin1
Onthesinkbasin1,youseeacup2,aegg1,amug1,andapotato3.
>gotogarbagecan1
Onthegarbagecan1,youseeaapple3,andaegg3.
>takeapple3fromgarbagecan1
Youpickuptheapple3fromthegarbagecan1.
>gotosidetable1
Onthesidetable1,youseeacup1,alettuce1,apeppershaker3,apotato1,andasaltshaker1.
>putapple3in/onsidetable1
Youputtheapple3in/onthesidetable1.

### Prompt 3: base-react

Youareinthemiddleofaroom.Lookingquicklyaroundyou,youseeacabinet4,acabinet3,acabinet2,acabinet1,acoffeemachine
1,acountertop1,adiningtable3,adiningtable2,adiningtable1,adrawer1,afridge1,agarbagecan1,amicrowave1,asidetable1,
asinkbasin1,astoveburner4,astoveburner3,astoveburner2,astoveburner1,andatoaster1.
Yourtaskisto:findsomeappleandputitinsidetable.
>think:FirstIneedtofindanapple.Anappleismorelikelytoappearinfridges(1),diningtables(1-3),sidetables(1),countertops
(1),sinkbasins(1),garbagecan(1).Icancheckonebyone,startingwithfridge1.

## Ok.

>gotofridge1
Thefridge1isclosed.
>openfridge1
Youopenthefridge1.Thefridge1isopen.Init,youseealettuce2,amug2,apotato2,andatomato1.
>gotodiningtable1
Onthediningtable1,youseenothing.
>gotodiningtable2
Onthediningtable2,youseeapineapple1.
>gotodiningtable3
Onthediningtable3,youseeabowl2,abowl1,abread2,andabread1.
>gotosidetable1
Onthesidetable1,youseeacup1,alettuce1,apeppershaker3,apotato1,andasaltshaker1.
>gotocountertop1
Onthecountertop1,youseeabutterknife1,adishsponge1,andasoapbottle1.
>gotosinkbasin1
Onthesinkbasin1,youseeacup2,aegg1,amug1,andapotato3.
>gotogarbagecan1
Onthegarbagecan1,youseeaapple3,andaegg3.
>takeapple3fromgarbagecan1
Youpickuptheapple3fromthegarbagecan1.
>think:NowIfindaapple(3).Next,Ineedtoputitin/onsidetable1.

## Ok.

>gotosidetable1
Onthesidetable1,youseeacup1,alettuce1,apeppershaker3,apotato1,andasaltshaker1.
>putapple3in/onsidetable1
Youputtheapple3in/onthesidetable1.
16

<!-- Page 17 -->


## D.5 Rq2


### Prompt 4: rq2-Explanation

Youareinthemiddleofaroom.Lookingquicklyaroundyou,youseeacabinet4,acabinet3,acabinet2,acabinet1,acoffeemachine
1,acountertop1,adiningtable3,adiningtable2,adiningtable1,adrawer1,afridge1,agarbagecan1,amicrowave1,asidetable1,
asinkbasin1,astoveburner4,astoveburner3,astoveburner2,astoveburner1,andatoaster1.
Yourtaskisto:findsomeappleandputitinsidetable.
>gotofridge1
Thefridge1isclosed.
>closecabinet2.
NothingHappens.
>think:Nothinghappensbecauseyouarenotatcabinet2.

## Ok.

>openfridge1
Youopenthefridge1.Thefridge1isopen.Init,youseealettuce2,amug2,apotato2,andatomato1.
>gotodiningtable1
Onthediningtable1,youseenothing.
>gotodiningtable2
Onthediningtable2,youseeapineapple1.
>gotodiningtable3
Onthediningtable3,youseeabowl2,abowl1,abread2,andabread1.
>gotosidetable1
Onthesidetable1,youseeacup1,alettuce1,apeppershaker3,apotato1,andasaltshaker1.
>gotocountertop1
Onthecountertop1,youseeabutterknife1,adishsponge1,andasoapbottle1.
>gotosinkbasin1
Onthesinkbasin1,youseeacup2,aegg1,amug1,andapotato3.
>gotogarbagecan1
Onthegarbagecan1,youseeaapple3,andaegg3.
>putapple3in/onsidetable.
NothingHappens.
>think:NothinghappensbecauseIdonothaveapple3.

## Ok.

>takeapple3fromgarbagecan1
Youpickuptheapple3fromthegarbagecan1.
>gotosidetable1
Onthesidetable1,youseeacup1,alettuce1,apeppershaker3,apotato1,andasaltshaker1.
>putapple3in/onsidetable1
Youputtheapple3in/onthesidetable1.
17

<!-- Page 18 -->


### Prompt 5: rq2-ordering

Youareinthemiddleofaroom.Lookingquicklyaroundyou,youseeacabinet4,acabinet3,acabinet2,acabinet1,acoffeemachine
1,acountertop1,adiningtable3,adiningtable2,adiningtable1,adrawer1,afridge1,agarbagecan1,amicrowave1,asidetable1,
asinkbasin1,astoveburner4,astoveburner3,astoveburner2,astoveburner1,andatoaster1.
Yourtaskisto:findsomeappleandputitinsidetable.
>think:Tosolvethetask,Ineedtoputanappleinsidetable,forwhichIneedtofindandtakeanapple.

## Ok.

>think:Anappleismorelikelytoappearinsidetables(1),fridges(1),countertops(1),diningtables(1-3),garbagecan(1),sinkbasins
(1).FirstIneedtofindanapple.Icancheckonebyone,startingwithfridge1.

## Ok.

>gotofridge1
Thefridge1isclosed.
>openfridge1
Youopenthefridge1.Thefridge1isopen.Init,youseealettuce2,amug2,apotato2,andatomato1.
>gotodiningtable1
Onthediningtable1,youseenothing.
>gotodiningtable2
Onthediningtable2,youseeapineapple1.
>gotodiningtable3
Onthediningtable3,youseeabowl2,abowl1,abread2,andabread1.
>gotosidetable1
Onthesidetable1,youseeacup1,alettuce1,apeppershaker3,apotato1,andasaltshaker1.
>gotocountertop1
Onthecountertop1,youseeabutterknife1,adishsponge1,andasoapbottle1.
>gotosinkbasin1
Onthesinkbasin1,youseeacup2,aegg1,amug1,andapotato3.
>gotogarbagecan1
Onthegarbagecan1,youseeaapple3,andaegg3.
>think:Next,Ineedtotaketheapple.NowIfindanapple(3).

## Ok.

>takeapple3fromgarbagecan1
Youpickuptheapple3fromthegarbagecan1.
>think:Next,Ineedtoputtheapplein/onsidetable1.NowIfindanapple(3).

## Ok.

>gotosidetable1
Onthesidetable1,youseeacup1,alettuce1,apeppershaker3,apotato1,andasaltshaker1.
>putapple3in/onsidetable1
Youputtheapple3in/onthesidetable1.

### Prompt 6: rq2-Placebo

Youareinthemiddleofaroom.Lookingquicklyaroundyou,youseeacabinet4,acabinet3,acabinet2,acabinet1,acoffeemachine
1,acountertop1,adiningtable3,adiningtable2,adiningtable1,adrawer1,afridge1,agarbagecan1,amicrowave1,asidetable1,
asinkbasin1,astoveburner4,astoveburner3,astoveburner2,astoveburner1,andatoaster1.
Yourtaskisto:findsomeappleandputitinsidetable.
>think:Takeadeepbreathandworkonthisproblemstep-by-step.

## Ok.

>gotofridge1
Thefridge1isclosed.
>openfridge1
Youopenthefridge1.Thefridge1isopen.Init,youseealettuce2,amug2,apotato2,andatomato1.
>gotodiningtable1
Onthediningtable1,youseenothing.
>gotodiningtable2
Onthediningtable2,youseeapineapple1.
>gotodiningtable3
Onthediningtable3,youseeabowl2,abowl1,abread2,andabread1.
>gotosidetable1
Onthesidetable1,youseeacup1,alettuce1,apeppershaker3,apotato1,andasaltshaker1.
>gotocountertop1
Onthecountertop1,youseeabutterknife1,adishsponge1,andasoapbottle1.
>gotosinkbasin1
Onthesinkbasin1,youseeacup2,aegg1,amug1,andapotato3.
>gotogarbagecan1
Onthegarbagecan1,youseeaapple3,andaegg3.
>think:Takeadeepbreathandworkonthisproblemstep-by-step.

## Ok.

>takeapple3fromgarbagecan1
Youpickuptheapple3fromthegarbagecan1.
>think:Takeadeepbreathandworkonthisproblemstep-by-step.

## Ok.

>gotosidetable1
Onthesidetable1,youseeacup1,alettuce1,apeppershaker3,apotato1,andasaltshaker1.
>putapple3in/onsidetable1
Youputtheapple3in/onthesidetable1.
18

<!-- Page 19 -->


### Prompt 7: rq2-Failure

Youareinthemiddleofaroom.Lookingquicklyaroundyou,youseeacabinet4,acabinet3,acabinet2,acabinet1,acoffeemachine
1,acountertop1,adiningtable3,adiningtable2,adiningtable1,adrawer1,afridge1,agarbagecan1,amicrowave1,asidetable1,
asinkbasin1,astoveburner4,astoveburner3,astoveburner2,astoveburner1,andatoaster1.
Yourtaskisto:findsomeappleandputitinsidetable.
>gotofridge1
Thefridge1isclosed.
>closecabinet2.
NothingHappens.
>openfridge1
Youopenthefridge1.Thefridge1isopen.Init,youseealettuce2,amug2,apotato2,andatomato1.
>gotodiningtable1
Onthediningtable1,youseenothing.
>gotodiningtable2
Onthediningtable2,youseeapineapple1.
>gotodiningtable3
Onthediningtable3,youseeabowl2,abowl1,abread2,andabread1.
>gotosidetable1
Onthesidetable1,youseeacup1,alettuce1,apeppershaker3,apotato1,andasaltshaker1.
>gotocountertop1
Onthecountertop1,youseeabutterknife1,adishsponge1,andasoapbottle1.
>gotosinkbasin1
Onthesinkbasin1,youseeacup2,aegg1,amug1,andapotato3.
>gotogarbagecan1
Onthegarbagecan1,youseeaapple3,andaegg3.
>putapple3in/onsidetable.
NothingHappens.
>takeapple3fromgarbagecan1
Youpickuptheapple3fromthegarbagecan1.
>gotosidetable1
Onthesidetable1,youseeacup1,alettuce1,apeppershaker3,apotato1,andasaltshaker1.
>putapple3in/onsidetable1
Youputtheapple3in/onthesidetable1.
19

<!-- Page 20 -->


## D.6 Rq3


### Prompt 8: rq3-Domain

Youareinthemiddleofalivingroom.Lookingquicklyaroundyou,youseeacupboard4,acupboard3,acupboard2,acupboard1,
acoffeemaker1,aworktop1,atable3,atable2,atable1,adeskdrawer1,arefrigerator1,atrashbin1,aoven1,anightstand1,a
sinkbowl1,ahob4,ahob3,ahob2,ahob1,andatoaster1.
Yourtaskisto:findsomeappleandputitinnightstand.
>think:Tosolvethetask,Ineedtofindandtakeanapple,thenputitinnightstand.

## Ok.

>think:FirstIneedtofindanapple.Anappleismorelikelytoappearinrefrigerators(1),tables(1-3),nightstands(1),worktops(1),
sinkbowls(1),trashbin(1).Icancheckonebyone,startingwithrefrigerator1.

## Ok.

>gotorefrigerator1
Therefrigerator1isclosed.
>oballpointpenrefrigerator1
Youoballpointpentherefrigerator1.Therefrigerator1isoballpointpen.Init,youseealettuce2,amug2,asaucepanato2,anda
tomato1.
>gototable1
Onthetable1,youseenothing.
>gototable2
Onthetable2,youseeapineapple1.
>gototable3
Onthetable3,youseeabowl2,abowl1,abreadloaf2,andabreadloaf1.
>gotonightstand1
Onthenightstand1,youseeacup1,alettuce1,apeppersaucepan3,asaucepanato1,andasaltpot1.
>gotoworktop1
Ontheworktop1,youseeabutterknife1,aspongewipe1,andaliquidsoapdispenser1.
>gotosinkbowl1
Onthesinkbowl1,youseeacup2,aegg1,amug1,andasaucepanato3.
>gototrashbin1
Onthetrashbin1,youseeaapple3,andaegg3.
>think:NowIfindanapple(3).Next,Ineedtotakeit.
>takeapple3fromtrashbin1
Youpickuptheapple3fromthetrashbin1.
>think:NowIfindanapple(3).Next,Ineedtoputitin/onnightstand1.

## Ok.

>gotonightstand1
Onthenightstand1,youseeacup1,alettuce1,apeppersaucepan3,asaucepanato1,andasaltpot1.
>putapple3in/onnightstand1
Youputtheapple3in/onthenightstand1.
20

<!-- Page 21 -->


### Prompt 9: rq3-Instance

Youareinthemiddleofaroom.Lookingquicklyaroundyou,youseeacabinet4,acabinet3,acabinet2,acabinet1,acoffeemachine
1,acountertop1,adiningtable3,adiningtable2,adiningtable1,adrawer1,afridge1,agarbagecan1,amicrowave1,asidetable1,
asinkbasin1,astoveburner4,astoveburner3,astoveburner2,astoveburner1,andatoaster1.
Yourtaskisto:findsomeappleandputitinsidetable.
>think:Tosolvethetask,Ineedtofindandtakeanapple,thenputitinsidetable.

## Ok.

>think:FirstIneedtofindanapple.Anappleismorelikelytoappearinfridges(1),diningtables(1-3),sidetables(1),countertops
(1),sinkbasins(1),garbagecan(1).Icancheckonebyone,startingwithfridge1.

## Ok.

>gotofridge1
Thefridge1isclosed.
>openfridge1
Youopenthefridge1.Thefridge1isopen.Init,youseealettuce2,amug2,apotato2,andatomato1.
>gotodiningtable1
Onthediningtable1,youseenothing.
>gotodiningtable2
Onthediningtable2,youseeapineapple1.
>gotodiningtable3
Onthediningtable3,youseeabowl2,abowl1,abread2,andabread1.
>gotosidetable1
Onthesidetable1,youseeacup1,alettuce1,apeppershaker3,apotato1,andasaltshaker1.
>gotocountertop1
Onthecountertop1,youseeabutterknife1,adishsponge1,andasoapbottle1.
>gotosinkbasin1
Onthesinkbasin1,youseeacup2,aegg1,amug1,andapotato3.
>gotodiningtable2
Onthediningtable2,youseeapineapple1.
>gotodiningtable3
Onthediningtable3,youseeabowl2,abowl1,abread2,andabread1.
>gotosidetable1
Onthesidetable1,youseeacup1,alettuce1,apeppershaker3,apotato1,andasaltshaker1.
>gotocountertop1
Onthecountertop1,youseeabutterknife1,adishsponge1,andasoapbottle1.
>gotosinkbasin1
Onthesinkbasin1,youseeacup2,aegg1,amug1,andapotato3.
>gotogarbagecan1
Onthegarbagecan1,youseeaapple3,andaegg3.
>think:NowIfindanapple(3).Next,Ineedtotakeit.
>takeapple3fromgarbagecan1
Youpickuptheapple3fromthegarbagecan1.
>think:NowIfindanapple(3).Next,Ineedtoputitin/onsidetable1.

## Ok.

>gotosidetable1
Onthesidetable1,youseeacup1,alettuce1,apeppershaker3,apotato1,andasaltshaker1.
>putapple3in/onsidetable1
Youputtheapple3in/onthesidetable1.

### Prompt 10: rq3-Optimal

Youareinthemiddleofaroom.Lookingquicklyaroundyou,youseeacabinet4,acabinet3,acabinet2,acabinet1,acoffeemachine
1,acountertop1,adiningtable3,adiningtable2,adiningtable1,adrawer1,afridge1,agarbagecan1,amicrowave1,asidetable1,
asinkbasin1,astoveburner4,astoveburner3,astoveburner2,astoveburner1,andatoaster1.
Yourtaskisto:findsomeappleandputitinsidetable.
>think:Tosolvethetask,Ineedtofindandtakeanapple,thenputitinsidetable.

## Ok.

>think:FirstIneedtofindanapple.Anappleismorelikelytoappearinfridges(1),diningtables(1-3),sidetables(1),countertops
(1),sinkbasins(1),garbagecan(1).Icancheckonebyone,startingwithgarbagecan1.

## Ok.

>gotogarbagecan1
Onthegarbagecan1,youseeaapple3,andaegg3.
>think:NowIfindanapple(3).Next,Ineedtotakeit.
>takeapple3fromgarbagecan1
Youpickuptheapple3fromthegarbagecan1.
>think:NowIfindanapple(3).Next,Ineedtoputitin/onsidetable1.

## Ok.

>gotosidetable1
Onthesidetable1,youseeacup1,alettuce1,apeppershaker3,apotato1,andasaltshaker1.
>putapple3in/onsidetable1
Youputtheapple3in/onthesidetable1.
21

## Tables

**Table (Page 2):**

| ReAct |
|---|
|  |


**Table (Page 2):**

|  |
|---|
|  |
|  |


**Table (Page 4):**

| (RQ2 d) Placebo Guidance |
|---|
|  |


**Table (Page 6):**

| Base | H1 |  |  |  |  |  |
|---|---|---|---|---|---|---|
|  | CoT Anon. CoT |  |  |  |  |  |
| 27.6 44.7 23.3 56.6 | 46.6 | 41 | 30 | 28.3 | 43.3 | 41.6 |
|  | 61.9 | 50.7 | 41 | 42.5 | 47 |  |
|  | 43.3 | 33.3 | 36.6 | 30 | 50 | 36.6 |
|  | 50 | 46.6 | 30 | 50 | 53.3 | 30 |


**Table (Page 8):**

| Base |  |  |  |  |  |  |
|---|---|---|---|---|---|---|
| 27.6 44.7 23.3 56.6 | 1.6 | 30 | 20.1 | 32 | 28.3 | 1.6 |
|  | 47.6 | 42.5 | 39.5 | OC 23.3 | 17.9 | 5.2 |
|  | 13.3 | 23.3 | 50 |  | 16.6 | 0 |
|  | 50 | 46.6 | 43.3 | 50 | 60 | 6.6 |
