---
title: "AutoAgents Automatic Agent Generation"
original_file: "./AutoAgents_Automatic_Agent_Generation.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["prompt-engineering", "llm", "rag", "chain-of-thought", "react"]
keywords: ["expert", "you", "role", "should", "cid", "each", "task", "suggestions", "step", "roles"]
summary: "<!-- Page 1 -->

AutoAgents: A Framework for Automatic Agent

### Generation

GuangyaoChen1∗,SiweiDong1∗,YuShu1∗,GeZhang4,JawardSesay3,BörjeKarlsson3,
JieFu2†,YeminShi1†
1PekingUniversity
2HongKongUniversityofScienceandTechnology
3BeijingAcademyofArtificialIntelligence
4UniversityofWaterloo
gy.chen@pku.edu.cn, ymshi@pku.edu.cn, jiefu@ust.hk

### Abstract

Largelanguagemodels(LLMs)haveenabledremarkableadvancesinautomated
task-solvingwithmulti-agentsystems. However,mostexistingLLM-basedmultiagenta"
related_documents: []
---

# AutoAgents Automatic Agent Generation

<!-- Page 1 -->

AutoAgents: A Framework for Automatic Agent

### Generation

GuangyaoChen1∗,SiweiDong1∗,YuShu1∗,GeZhang4,JawardSesay3,BörjeKarlsson3,
JieFu2†,YeminShi1†
1PekingUniversity
2HongKongUniversityofScienceandTechnology
3BeijingAcademyofArtificialIntelligence
4UniversityofWaterloo
gy.chen@pku.edu.cn, ymshi@pku.edu.cn, jiefu@ust.hk

### Abstract

Largelanguagemodels(LLMs)haveenabledremarkableadvancesinautomated
task-solvingwithmulti-agentsystems. However,mostexistingLLM-basedmultiagentapproachesrelyonpredefinedagentstohandlesimpletasks, limitingthe
adaptability of multi-agent collaboration to different scenarios. Therefore, we
introduce AutoAgents, an innovative framework that adaptively generates and
coordinatesmultiplespecializedagentstobuildanAIteamaccordingtodifferent
tasks. Specifically,AutoAgentscouplestherelationshipbetweentasksandrolesby
dynamicallygeneratingmultiplerequiredagentsbasedontaskcontentandplanning
solutions for the current task based on the generated expert agents. Multiple
specialized agents collaborate with each other to efficiently accomplish tasks.
Concurrently,anobserverroleisincorporatedintotheframeworktoreflectonthe
designatedplansandagents’responsesandimproveuponthem. Ourexperiments
onvariousbenchmarksdemonstratethatAutoAgentsgeneratesmorecoherentand
accurate solutions than the existing multi-agent methods. This underscores the
significanceofassigningdifferentrolestodifferenttasksandofteamcooperation,
offeringnewperspectivesfortacklingcomplextasks. Therepositoryofthisproject
isavailableathttps://github.com/Link-AGI/AutoAgents.
1 Introduction
Large language models (LLMs) have exhibited astounding capabilities [26, 22, 29] as versatile
task-solvingagents,endowedwitharichblendofknowledgeandskills. Nevertheless,theystillface
difficulties[26,22,2]intacklingvarioustasksthatrequireintensiveknowledgeandreasoning,such
asavoidinghallucination[19],employingslow-thinkingstrategies[30],ensuringtrustworthiness[32],
andincombiningdiversedomainknowledgeandlong-horizonplanning. Incontrast,humansoften
exploitthebenefitsofcollaborativeproblemsolving,whichenablesthemtoworktogethereffectively
to solve non-routine problems in diverse domains and enhance the quality and reliability of the
solutionsbydistributingtheworkloadamongspecialtiesandapplyingadiversityofperspectivesand
expertise[21,27,1].
Inspiredbycollaborativeproblemsolving,severalrecentworks[34,7,17,11]haveimprovedthe
task-solvingcapabilitiesofLLMsbyintegratingmulti-agentdiscussion.However,mostofthesemultiagentsystemsdependonhandcraftedoruser-specifiedagents,withspecificrolesandnecessitating
humansupervision,whichoftenrestrictsthescopeofcollaborativeapplications. Moreover,manually
∗Equalcontribution
†Correspondingauthor.
4202
rpA
92
]IA.sc[
3v88271.9032:viXra

<!-- Page 2 -->

Table1: ComparisonofexistingandproposedframeworksforLLM-basedAgentframework.
DynamicAgent Numberof Multi-agent Self-Refinement Collaborative

### Framework

GenerationMethod Agent Conversation Action RefinementAction
AutoGPT[10] (cid:37) 1 (cid:37) (cid:33) (cid:37)

### BabyAGI[20] (cid:37) 3 (cid:33) (cid:37) (cid:37)

GenerativeAgents[23] (cid:37) 25 (cid:33) (cid:33) (cid:37)

### Camel[16] (cid:37) 2 (cid:33) (cid:37) (cid:37)


### GPT-bargaining[8] (cid:37) 3 (cid:33) (cid:33) (cid:37)

MetaGPT[12] (cid:37) Unlimited (cid:33) (cid:37) (cid:37)

### AutoGen[37] (cid:37) Unlimited (cid:33) (cid:37) (cid:37)

SocialSimulacra[24] SingleAgent Unlimited (cid:33) (cid:37) (cid:37)
EpidemicModeling[35] SingleAgent Unlimited (cid:33) (cid:37) (cid:37)
ExpertPrompting[38] SingleAgent 1 (cid:37) (cid:37) (cid:37)

### SSP[34] SingleAgent Unlimited (cid:33) (cid:37) (cid:37)

AgentVerse[5] SingleAgent Unlimited (cid:33) (cid:37) (cid:37)
AutoAgents Multi-agentDiscussion Unlimited (cid:33) (cid:33) (cid:33)
creatingalargenumberofexpertsoftenconsumesalotofresources. Inordertoadaptivelysolve
morecomplexproblems,thispaperaimstoexploreamethodofadaptivelygeneratingtaskexperts
andcompletingdifferenttasksthroughmulti-levelcollaborativecooperationamongmultipleexperts.
In this paper, we propose AutoAgents, an innovative framework that adaptively generates and
coordinatesmultiplespecializedagentstoconstructanAIteamaccordingtodifferenttasks. Figure1
providesahigh-leveloverviewofAutoAgents. Bygeneratingmultipleagentswithdistinctexpert
roles,weaimtoformacollaborativeentitythatcanaccomplishcomplextasksbyleveragingthe
complementary strengths of each agent. As shown in Figure 2, the process of AutoAgents is
dividedintotwocriticalstages: DraftingStageandExecutionStage. Thedraftingstageinvolves
a collaborative discussion among three predefined agents (Planner, Agent Observer, and Plan
Observer)tosynthesizeacustomizedagentteamandanexecutionplanthatsuittheinputproblem
ortask. Theexecutionstagerefinestheplanthroughinter-agentcollaborationandfeedback,and
produces the final outcome. We propose self-refinement by individual agents and collaborative
refinementbymultipleagentstoenhanceagentproficiencyandpromoteknowledge-sharingamong
agents. To facilitate the specific division of labor among the agents in the synthesized team, we
introduce a predefined agent (Action Observer) to assist the agent team in sharing information,
coordinatingactions,reachingconsensus,andadaptingtotheenvironment.
Tosynthesizeheterogeneousinformationfromdiversedomainsisoftenacrucialrequirementincreativeindustriesandotherreal-worldscenarios. WeillustrateaconcreteexampleofhowAutoAgents
tacklesthechallengingtaskofwritinganovelabouttheawakeningofartificialintelligenceinFigure1.
TheStoryPlannerandResearchercollaboratetodevisetheplotofthestorywiththeirrespective
expertise,whiletheCharacterDeveloperandWriterenrichthenovelcontentthroughimagination
basedonthestory. Moreover,weconductquantitativeexperimentsandcasestudiesincomplextasks
to demonstrate the effectiveness of AutoAgents. We also conduct a comprehensive analysis and
demonstratetheimportanceofdynamicagentsforhandlingcomplextasks,theindispensabilityof
self-refinementforproficientagents,andtheeffectivenessofcollaborativeconversation.
Tosummarize,thispapermakesthefollowingnovelcontributions: First,weproposeAutoAgents,
a novel framework that dynamically synthesizes and coordinates multiple expert agents to form
customizedAIteamsfordiversetasks. Second,weconductrigorousquantitativeexperimentson
two challenging tasks and demonstrate that AutoAgents significantly improves both knowledge
acquisitionandreasoningabilityinLLMsandoutperformsothergenerated-agentframeworks. Third,
weshowcaseAutoAgents’abilitytoadapttocomplextasksbyapplyingitinvariousscenariossuch
assoftwaredevelopment. Finally,weconductathoroughinvestigationandrevealtheimportanceof
dynamicagentsforaccommodatingcomplextasksandthenecessityofself-refinementforproficient
agents,andtheefficacyofcollaborativeconversation.
2 RelatedWork
LLM-basedAutonomousAgents. LLMshavebeenwidelyusedascorecontrollersforautonomous
agentsthatcanaccomplishspecificobjectives. Auto-GPT[10]isanearlyworkthatleveragesan
2

<!-- Page 3 -->

Figure1: AschematicdiagramofAutoAgents. Thesystemtakestheuserinputasastartingpoint
andgeneratesasetofspecializedagentsfornovelwriting,alongwithacorrespondingexecution
plan. Theagentscollaborativelycarryoutthetasksaccordingtotheplanandproducethefinalnovel.
Meanwhile,anobservermonitorsthegenerationandexecutionoftheAgentsandtheplan,ensuring
thequalityandcoherenceoftheprocess.
LLM as an AI agent that can autonomously achieve a given goal with the help of several tools.
However,Auto-GPTdoesnotsupportmulti-agentcollaborationandcanonlyworkinisolation. One
waytoenhancethetask-solvingcapabilitiesofLLMsistoassigndifferentrolesandresponsibilities
tomultipleLLMsandletthemcoordinatetheiractionstoachieveacommongoal. Forexample,
BabyAGI[20]isanAI-poweredtaskmanagementsystemwithmultipleLLM-basedagents. One
agentcreatesnewtasksbasedontheprevioustask’sobjectiveandresult,anotheragentprioritizes
the task list, and another agent completes tasks. BabyAGI is a multi-agent system with a fixed
orderofagentcommunication. MetaGPT[12]isamulti-agentframeworkforassigningdifferent
rolestoGPTstoformacollaborativesoftwareentityforcomplextasks. ItisaspecializedLLM-
basedmulti-agentframeworkforcollaborativesoftwaredevelopment. Camel[16]isanLLM-based
communicative agent framework that demonstrates how role-playing can be used to enable chat
agents to communicate with each other for task completion. However, Camel does not support
tool-using. Severalrecentworks[34,7,17,11,31,15]haveenhancedthetask-solvingcapabilitiesof
LLMsbyintegratingmulti-agentdiscussion. Forinstance, [34]proposesamulti-agentdebatesystem
thatallowsLLMstoarguefororagainstagivenclaimandgenerateadebatesummary. [7]introduce
amulti-agentdialoguesystemthatenablesLLMstoexchangeinformationandopinionsonagiven
topicandgenerateadialoguereport. AutoGen[37]isaframeworkthatenablesthedevelopmentof
LLMapplicationsusingmultipleagentsthatcanconversewitheachothertosolvetasks. However,
mostofthesemulti-agentsystemsrelyonhandcraftedoruser-specifiedagentswithspecificroles
3

<!-- Page 4 -->

Figure2: TheexecutionprocessofAutoAgents. DuringtheDraftingStage,threepredefinedagents
collaborativelydeterminethelistofagentsandtheexecutionplan. DuringtheExecutionStage,a
predefinedagentfacilitatescoordinationandcommunicationamongthegeneratedagentteams,and
theindividualgeneratedagentsenhancetheirexecutionefficiencythroughself-refinement.
anddonotsupporttheautomaticgenerationofagents,whichoftenlimitsthescopeofcollaborative
applications.
AgentGeneralization.Severalstudies [24,35]employLLMstogenerateagentsforsocialsimulacra
andepidemicmodeling,demonstratinghowthistechniquecanfacilitatedesignersinassessingand
improvingtheirmodelingdesignspriortodeployingthemtorealusers. Likewise,ExpertPrompting[38]devisedamethodtogeneratediverseprofilesofagentsthatcancooperatewithhumanusers
toaccomplishtaskswithminimalsupervision. However,thismethodstilldependsonarestricted
setofpredefinedagents, andthegeneratedagentsvaryonlyintheirprofiles. Recently, SSP[34]
andAgentVerse[5]haveproposedframeworksforautomaticallygeneratingunlimitedagents. SSP
enablesLLMstogenerateagentsforprobleminputbyprovidingsomeagentsamples,andhasthese
agentssolvetheproblem. AgentVersegeneratestheexecutionplanthroughthegeneratedagents’
discussionsandaddsevaluationstrategiesforcyclicexecution. Unliketheprevioustwomethods,
AutoAgentsplacesaheightenedemphasisonthereliabilityofitsgeneratedagentsandstrategicplans,
therebyenhancingtaskexecutioneffectthroughtheutilizationofcollaborativerefinementactions
andtheintegrationofself-refinementactions,asillustratedinTable1.
3 TheFrameworkforAutomaticAgentGeneration
Toenhancetheeffectivenessofautonomousmulti-agentgroupsinaccomplishingtheirgoals,the
process of AutoAgents consists of two critical stages: Drafting Stage and Execution Stage, as
illustrated in Figure 2. The drafting stage synthesizes an agent team and an execution plan that
arecustomizedtothetaskbyanalyzingtheinputproblemortask. Theexecutionstagerefinesthe
plan by enabling inter-agent collaboration and feedback, and delivers the final result. The interagentcollaborationisbasedonsomeprinciplesofmulti-agentcooperation,suchascommunication,
coordination,andconsensus.Theseprincipleshelptheagentstoshareinformation,aligntheiractions,
reachagreements,andadapttotheenvironment.
4

<!-- Page 5 -->

3.1 DraftingStage
Empiricalevidence [36]suggeststhatdiversitywithinhumangroupsfostersdiverseperspectives,
whichenhancesthegroup’sperformanceacrossvarioustasks. Thedraftingstage,whichdetermines
thecompositionofamulti-agentgroup,playsacrucialroleinsettingtheupperlimitsofthegroup’s
capabilities. Therefore,itisimperativetogeneratetheoptimalagentteamandexecutionplanthat
canmaximizethegroup’spotential.
Predominant methodologies [10, 12, 37] for assigning role descriptions to autonomous agents
relyheavilyonhumanintuitionandpriorknowledge,requiringmanualassignmentbasedontask
understanding. Consistentwithseveralparallelfindings[38,34,5],dynamicallydesigningagents
withdifferentrolescansignificantlyenhancetheirefficacy. However,thescalabilityandrationality
of agent and plan generation are still unclear, especially in the face of various complex problem
environments.
Ontheonehand,thegeneratedagentsshouldexhibitdiversitytoaccommodatevarioustasks. On
theotherhand,theagentandtheplangenerationshouldadheretocertainprinciples,renderingtheir
roleallocationmorerational. Therefore,wedevisethreeartificiallypredefinedagentstoproduce
agentteamsandexecutionplans,integratingartificialpriorknowledgeandthedynamicadaptation
capabilityofLLMstogeneratemoresensibleagentteamsandexecutionplans. Thethreeartificially
predefinedagentscomprisePlanner,AgentObserver,andPlanObserver:
• PlannerP generatesandrefinesanagentteamandanexecutionplanbasedonthecontent
ofthetask.
• AgentObserverO providessuggestionsontherationalityoftheagentteammembers
agent
andtheirmatchingdegreewiththetask.
• PlanObserverO providessuggestionsontherationalityoftheexecutionplanandits
plan
matchingdegreewiththetaskandtheagentteam.
ThePlannergeneratesinitialagentteammembersandaspecificplan,andimprovestheagentteam
andexecutionplanbasedoncontinuouscommunicationwiththeAgentObserverandPlanObserver.
AgentGeneration. ThePlannergeneratestheagentteamandfacilitatesitscontinuousimprovement
throughreciprocalcommunicationwiththeAgentObserver. ToenablePlannertoproducerational
agents, we have devised a standard format for the essential elements of a single agent. For each
agentA = {P,D,T,S},thePlannerneedstospecifyitspromptP,descriptionD,toolsetT,and
suggestionsS.
• Prompt P provides a detailed and customized depiction of the expert identity for each
specificagent,whichcomprisesprofile,goal,andconstraints. Profilereflectsthedomain
expertiseoftheroleorjobtitle. Goalindicatestheprimaryresponsibilityorobjectivethat
theroleaimstoachieve. Constraintsspecifylimitationsorprinciplestherolemustadhere
towhenperformingactions.
• DescriptionDgivesadditionalconcreteidentitytohelpestablishamorecomprehensive
role,developanexecutionplan,andinspectproblems.
• ToolsetTequipstheAgentwithtoolsthatitcanuse,selectedfromapredefinedsetoftools.
Therationalefornotusingallthetoolsforeachagenthereistopreventdecision-making
confusioncausedbyexcessivetools.
• SuggestionsSsuppliessomesuggestionsforeachagenttoexecutethecurrenttask,including
butnotlimitedtoaclearoutput,extractionofhistoricalinformation,andsuggestionsfor
executionsteps.
Basedontheagentlist{A ,A ,··· ,A }generatedbyPlanner,theAgentObserverevaluatesthe
1 2 n
qualityandsuitabilityofeachagent. TheAgentObserverfirstverifieswhethereveryagentconforms
totheaforementionedspecificationsandidentifiesanymissingelements{P,descriptionD,toolset
T}. Secondly,theAgentObserverassessesthecompatibilityofeachagentwiththetask,according
totheirdescriptioninformationandtaskcontent. Finally,theAgentObserverexaminestheagentlist
foranyredundantormissingrolesandeliminatesoraddsthemaccordingly.
AfternroundsofbidirectionalcommunicationbetweenthePlannerandtheAgentObserver,the
optimalagentlistforaccomplishingthetaskisestablished. Giventhevitalroleoftheagentlistinthe
5

<!-- Page 6 -->


### Story Planner Researcher

Task: Write engaging and coherent Task: The Story Planner collaborates with the Researcher to understand
chapters based on the outline and AI concepts and create a detailed outline for the novel. This includes a
character profiles. This will form the high-level overview of the story, a breakdown of the story into chapters,
main body of the novel. and a breakdown of each chapter into scenes.
(a) Self-refinement by a single agent (b) Collaborative refinement by multiple agents
Figure3: Twotypesofactionsforexecutingtasks: Self-refinementenablesanindividualagentto
enhanceitscompetenceinperformingsomespecializedtasks. Collaborativerefinementfacilitates
knowledgeexchangeamongmultipleagentsandaccomplishestasksthatdemandinterdisciplinary
expertise.
taskexecution,thisframeworkemploysapredefinedagentandmultipleroundsofiterativedialogue
amongmultipleagentstofinalizetheagentlist,therebyenhancingthestabilityandreliabilityofthe
executionphase.
PlanGeneration. Inparalleltoagentgeneration, thePlannerformulatestheexecutionplanand
promotesitsprogressiveimprovementthroughreciprocalcommunicationwiththePlanObserver.
Foragiventask, thePlannerdelineatesthespecificsteps{S ,S ,···S }toaccomplishitinthe
1 2 n
executionplanP. EachstepS entailsaclearidentificationoftheagentA responsibleforit,aswell
i j
astheinputinformationandexpectedoutputrequiredforit.
ThePlanObserversubsequentlyvalidatestheexecutionplanP ={S ,S ,···S }accordingtothe
1 2 n
agentlist{A ,A ,··· ,A }andthetaskcontent.Itfirstlyensuresthateachstephasacorresponding
1 2 n
agentandthatthestepcontentiscoherentandconcise. Itsecondlyassesseswhetherallthesteps
aresufficient,whetherthetaskcanbeaccomplished,andwhetherthereareanygapsthatneedtobe
filled. ItfinallyprovidesfeedbacktothePlanner,whofurtherrefinestheexecutionplanaccordingly.
AfternroundsofdialoguebetweenthePlannerandthePlanObserver,theultimateexecutionplan
forachievingthetaskisestablished.
Task Execution Actions. The Planner devises an execution plan that automatically assigns the
requisiteagentsfordiversetasks. Theexecutionplancomprisestwoactionsoftaskexecution: selfrefinementbyasingleagentandcollaborativerefinementbymultipleagents,asshowninFigure3.
Self-refinementempowersanindividualagenttoaugmentitsproficiencyinaccomplishingsome
specializedtasks. Collaborativerefinementfostersknowledgesharingamongmultipleagentsand
achievestasksrequiringinterdisciplinaryexpertise.
3.2 ExecutionStage
In the drafting phase, the framework generates an agent list and an execution plan based on the
task requirements. Then, the framework creates corresponding roles and executes the plans in
theexecutionenvironment3. Thecommunicationandcooperationamongmulti-agentsystemsare
essential for accomplishing the tasks effectively. This section elaborates on the communication
amongmultipleagents,thetaskexecutionstrategies,andtheknowledge-sharingmechanisms.
Communication of Multiple Agent. The communication structures among agents have been
investigated by many studies [5, 34, 25, 3] to examine their impact on task performance. In this
framework,weadopttheverticalcommunicationparadigm,whichassignsdifferenttaskstoagents
accordingtotheirroles. Tofacilitatethespecificdivisionoflaboramongtheagentsinthegenerated
team,weintroduceapredefinedActionObserverastheteamleadertocoordinatetheexecutionplan.

### Specifically,

3ExecutionenvironmentofAutoAgentsisbuiltbasedonMetaGPT’senvironmentandworkspace[12].
6

<!-- Page 7 -->

Figure 4: Legend of Three Knowledge Sharing Mechanisms. (a) Long-term memory focuses on
chroniclingthehistoricaltrajectoryofmultipleactions. (b)Short-termmemoryrecordsthehistoryof
theself-refinementorcollaborativerefinementphasesofanindividualaction. (c)Dynamicmemory
servesactionsnecessitatingspecializedattentionextractedfromthelong-termmemory.
• Action Observer O acts as the task manager for the different agents, allocating
action
differenttaskstothem,verifyingtheexecutionoutcomesofeachagent,anddynamically
adaptingtheexecutionplanbasedontheexecutionstatus.
ThismechanismofrefinementandcommunicationrecursuntiltheActionObserverattainsaunanimousagreementontheexecutionresponses, ortheprocessreachesitsmaximumiterationlimit.
Forscenariosthatdemanditerativedecision-makingtowardsspecificobjectives,suchassoftware
development,verticalcommunicationwouldbeapreferableoption.
Self-refinementAgent. Besidestheinter-agentcommunication,theperformanceofasingleagent
also exerts a significant impact on the overall quality of feedback results. Hence, drawing on
mechanismssuchasAutoGPT[10]andReAct[40],wehavedevisedaself-refinementmechanism
foranindividualagent.
ForasingleagentA,theactionatsteptisata =l ∪p ∪o ,wherel denotesthethoughtorthe
t t t t t
reasoningtraceinthelanguagespace,whichdoesnotaltertheexternalenvironment,andthusyields
noobservationalfeedback,p representstheexecutionplanfortaskcompletion,o comprisesthe
t t
completionstepsandexecutionoutputforthistime.
AsillustratedinFigure 2,varioustypesofusefulthoughtscanassistindevisingarefinementplan.
The execution plan enables the agent to anticipate the steps they need to undertake in the future,
andtheobservationalcontentoftheexecutionresultconstructionallowstheagenttoreevaluateand
enhancetheplanarrangement,therebyconstructingmorerefinedandcompleteactions. Througha
cycleofself-continuousthinking,planning,execution,andfeedback,asingleagentcaneffectively
executeandaccomplishtaskcontent.
CollaborativeRefinementAction. Inthecollaborativerefinementaction,theagentscollaboratively
refine and execute the tasks in a sequential manner. Each round of the collaboration involves a
fixed order of turn-taking among the agents, who generate their responses based on the current
observation. Thechathistoryslotofeachagentisupdatedbyconcatenatingthepreviousutterances
oftheotheragents. Thecollaborationterminatesautomaticallywhentheagentsreachaconsensusor
themaximumnumberofdiscussionsisreached.
KnowledgeSharingMechanism. AutoAgentsalsofacilitatesthesharingofexecutionresultsamong
variousagentsforimprovedcommunicationandfeedback. However,whenthenumberofagentsis
largeandasingleagenthasmoreself-iterations,itwillgeneratemorehistoricalinformation. Due
tothetokenlimitationofLLMmodels,theyoftencannotencompassallinformation. Hence,this
frameworkprovidesshort-termmemory,long-termmemory,anddynamicmemory.
7

<!-- Page 8 -->

Short-termmemoryischieflyconcentratedonasingularaction,encompassingthegamutofintermediarynotions,strategies,andoutcomesthatemergeduringtheself-refinementorcollaborative
refinementphasesofanindividualaction. Itissalienttonotethattheseactionsfrequentlyculminate
inadistilledsummaryofcriticalinformation,epitomizingthefinalphaseoftherefinementtrajectory.
Long-termmemoryprincipallyfocusesonchroniclingthehistoricaltrajectoryofmultifariousactions,
predominantly documenting the executed results of each task along with the synthesis of vital
feedback information. This aspect is imperative for evaluating the comprehensive extent of task
completion.
Dynamic memory predominantly serves actions necessitating specialized attention. The Action
Observer, having access to long-term memory archives, adeptly extracts ancillary information,
dynamicallytailoringittothespecificrequirementsoftheactionfortaskexecution. Thisprocess
significantlyaugmentstheefficiencyofasingleactionintaskfulfillment.
Algorithm1:AutoAgentsExecutionProcess.

### Input: Usertask/Question

Output: Tasksolution/Answer
1: DraftingStage
2: InitializePlannerP,AgentObserverO ,andPlanObserverO .
agent plan
3: P generatesinitialagentteam{A 1 ,A 2 ,··· ,A n }andexecutionplanP ={S 1 ,S 2 ,···S n }.
4: repeat
5: O providesfeedbackonagentteam.
agent
6: P refinesagentteambasedonfeedback.
7: O providesfeedbackonexecutionplan.
plan
8: P refinesexecutionplanbasedonfeedback.
9: untilNofeedbackorreachedthemaximumiterationlimit.
10: ExecutionStage:
11: InitializeActionObserverO action andlong-termmemoryM L .
12: for{S 1 ,S 2 ,···S n }do
13: O action generatedynamicmemoryM D .
14: O action assigntaskS k andM D tocorrespondingagents{A i ,··· ,A j }.
15: Initializeshort-termmemoryM S .
16: repeat
17: for{A i ,··· ,A j }do
18: AgentA m analyzesS k ,M S andM D .
19: AgentA m plansthecurrentstepandexecutesthisstep.
20: TheexecutionresultisstoredinM S .
21: endfor
22: untilNosteporreachedthemaximumiterationlimit.
23: TheexecutionresultsoftaskS k arestoredinM L .
24: O action coordinates{S 1 ,S 2 ,···S n }andmonitorsexecution.
25: endfor
26: returnExecutionresultsoffinalstep.
4 Experiments
InordertodemonstratethecapabilitiesandperformanceofAutoAgentsinorchestratingautonomous
agentgroupstocollaborativelyaccomplishtasks,wehaveperformedextensivequantitativeexperimentsonbenchmarktasksandthoroughcasestudiesonmorecomplexandrealisticapplications.
Inthequantitativeanalysis,wemainlypresentresultsfortheOpen-endedQuestionAnswertask
(detailedinSection4.1)andtheTriviaCreativeWritingtask(detailedinSection4.2)toevaluate
the framework effectiveness under distinct settings. The Case Studies, discussed in Section 4.4,
illustratethepotentialofamulti-agentgrouptacklingintricatepracticalscenarioscooperatively.
ImplementationDetails: WeconductallexperimentsusingtheGPT-4API4andsetthetemperature
to0toensurereproducibility. Therationalebehindthisselectionistheexceptionalperformancethese
4Thespecificmodelversionemployedis“GPT-4-0613”.
8

<!-- Page 9 -->

modelsoffer,providingmoreaccurateandstandardizedoutput. Additionally,theiraccessibilityand
easeofusethroughAPIsenableustodirectlycallandinteractwiththemodelsduringourresearch,
significantlysimplifyingtheprocess. Themaximumnumberofdiscussionsduringthedraftingphase
is3,andthemaximumnumberofself-refinementbyasingleagentandcollaborativerefinementby
multipleagentsduringtheexecutionphaseis5.
4.1 Open-endedQuestionAnswer
TaskDescription. Open-endedQuestionAnsweringisacrucialandchallengingtaskinthedomain
ofNLPandgenerativeAI.ItrequiresanAIsystemtoproducecoherent,elaborate,andhuman-like
responsestoquestionsthathavenopredeterminedorfixedsetofpossibleanswers. [41]proposed
MT-bench,abenchmarkconsistingof80high-qualitycollectedopen-endedquestionsfromvarious
categoriessuchascommonsense,counterfactual,coding,etc. WethenutilizeAutoAgentstoproduce
collaborativeanswersbasedonmultiplegeneratedagentsandcomparethemwiththeresponsesgiven
byVicuna-13B,ChatGPT,andGPT-4.
Table 2: Win Rate of AutoAgents over other models on Open-ended Question Answer, with
FairEval[33]andHumanEvalservingasevaluators.
Evaluator v.s. ChatGPT v.s. Vicuna-13B v.s. GPT-4
FairEval[33] 96.3% 96.3% 76.3%

### HumanEval 75% 75% 62.5%

EvaluationMetrics. Tomeasurethequalityofopen-endedresponseswithminimalevaluationbias,
we adopt FairEval [33] and HumanEval as the evaluation metrics for both the single agent and
AutoAgents. FairEvalincorporatesseveralmethodstomitigatetheimpactofvarioussourcesofbias,
resultinginabetteralignmentwithhumanjudgment. ForHumanEval,weenlistseveralvolunteers
toratetheresponsesfromdifferentmodelsbasedontheirhelpfulness,reliability,accuracy,andlevel
ofdetail.
Results. Table2demonstratesthatAutoAgentsoutperformsindividualLLMmodelsinbothFairEval
basedonLLMandHumanevaluations. AutoAgentcanproducemorecomprehensiveandnuanced
answerstoopenquestionsbysynthesizingmultipleexpertmodels. Itcanalsoprovidemoreelaborate
explanationsandjustificationsforitsanswers. MoreexamplesaregivenintheAppendixA.
4.2 TriviaCreativeWriting
TaskDescription. TheTriviaCreativeWritingtask[34]challengesthecapabilitiesoflargelanguage
modelstoretrieveandintegratediverseinformationfromtheirinternalself-compressedknowledge.
Thistaskrequiresamodeltocraftacoherentstoryaroundagiventopicwhileincorporatingthe
answerstoN triviaquestions.Weevaluatethemodelsundertwosettings,N =5andN =10,where
ahigherN entailsmoretriviaquestionsandthusdemandsthemodeltoexhibitmoreextensivedomain
knowledge. Weconstructedabenchmarkconsistingof100instancesforeachN,encompassinga
totalof1000triviaquestions.
Table 3: The results of Trivia Creative Writing task. ∆ indicates the differences compared with
StandardPrompting(firstrow).
N(#triviaquestions)=5 N(#triviaquestions)=10

### Methods

Score(%) ∆(v.sStandard%) Score(%) ∆(v.sStandard%)

### Standard 74.6 0.0% 77.0 0.0%


### CoT[39] 67.1 -10.0% 68.5 -11.1%

SPP-Profile[34] 79.1 +5.9% 83.0 +7.8%

## Spp[34] 79.9 +7.1% 84.7 +10.0%


### AutoAgents 82.0 +9.9% 85.3 +10.8%

Evaluation Metrics. Drawing on the approach of [34], we adopt an automatic metric to identify factual errors and measure a model’s capacity to integrate diverse domain knowledge. We
9

<!-- Page 10 -->

conduct string matching with the veridical target answers for each question on the generated
output. The target answers are supplied from the TriviaQA dataset [14], and each question can
have a list of answer variants. A match to any of the answer variants of a question is regarded
as a correct mention. The metric score is calculated as TriviaCreativeWritingMetricScore =
# correctanswermentions/#triviaquestions.
Results.Table3demonstratesthesuperiorperformanceofAutoAgentsinknowledgeacquisitionover
theexistingmethods. ComparedtotheStandardmethod,whichdoesnotemployAgentGeneration,
AutoAgentsachievesaremarkable10%improvementacrossallexperiments. Moreover,AutoAgents
alsosurpassesSSP[34],whichutilizesagentgenerationbutwithadifferentapproach. Theenhanced
performanceofAutoAgentscanbeattributedtoitselaboratemethodsofagentgenerationdiscussions
andtaskexecutionincludingcollaborativerefinementandself-refinement. Moreexamplesaregiven
intheAppendixA.
4.3 FurtherAnalysis
ThissectiondelvesintothesignificanceofkeycomponentswithinAutoAgentsbyseparatelyanalyzingtheself-refinementaction,collaborativerefinementaction,dynamicmemory,andobserversinthe
draftstageacross20instances5oftheTriviaCreativeWritingtaskandadditionalcasestudies.
Table 4: The ablation studies of AutoAgents on 20 instances of Trivia Creative Writing task. ∆
indicatesthedifferencescomparedwithStandardPrompting(firstrow).
N(#triviaquestions)=5

### Methods

Score(%) ∆(v.sStandard%)

### Standard 74.6 0.0%


### CoT[39] 66.0 -11.5%

SPP-Profile[34] 74.0 -0.01%

## Spp[34] 84.4 +13.1%


### AutoAgentsw/oobservers 87.0 +16.6%


### AutoAgentsw/oself-refinement 87.0 +16.6%

AutoAgentsw/ocollaborativerefinement 88.0 +18.0%
AutoAgentsw/odynamicmemory 89.0 +19.3%

### AutoAgents 90.0 +20.6%

Collaborativediscussioniscrucialforrationalagentgenerationandplanallocation. Duringthe
DraftingStage,thePlannerinAutoAgentsengagesincollaborativediscussionswithtwoObserversto
determinetheoptimallistofagentsandtheexecutionplan. Figure5illustratesthecontrastbetween
agentgenerationwithandwithoutcollaborativediscussion. IntheabsenceofObserverfeedback,
thePlannertendstogenerateprogrammersexclusivelytoaccomplishgamedevelopment,neglecting
theholisticprocessofgamecreation. WiththeinputandcoordinationoftheObservers,thePlanner
incorporates game design experts, UI design experts, and testing experts into the agent list. It is
evidentthattheagentgenerationundercollaborativediscussionsismorecomprehensiveandmore
alignedwiththerealisticscenariosofgamedevelopment. Thisalsocorroboratesthesignificanceof
collaborativediscussionsforagentgenerationandplanallocation,whichwillsubsequentlyinfluence
theexecutionoutcomes. Concurrently,Table4elucidatesthatintheabsenceofobservers,thereisa
marked3%reductionintheoverallperformanceofAutoAgents. Thissubstantiatestheimperative
role of collaborative discussions in agent generation. AutoAgent markedly enhances the caliber
ofagentgenerationviacollaborativediscussions, afacetnotablyoverlookedbyothergenerative
frameworksintheirconsiderationofagentgenerationquality. TheempiricaldatapresentedinTable2
and 3furtheraccentuatethesuperiorityofAutoAgentswhenjuxtaposedagainstcounterpartslike
AgentVerseandSPP.
Enhancing single-agent through self-refinement. Self-Refinement [18, 28, 9, 6, 13, 40] is a
technique that enables LLMs to “converse” with themselves, evaluate their own generation, and
iterativelyimprovetheiranswers. Self-refinementhasbeenshowntoenhancetheaccuracyofLLMs’
outputsinvariousdomains[18,28,9,6,13,40].AlthoughAutoAgentsisaframeworkformulti-agent
5Thelast20samplesfromadatasetof100samplesareusedastestinstances.
10

<!-- Page 11 -->

We also need game We need to create Game

### We need to create

experts to design Design Expert, UI/UX
a Programming
games and UI Design Expert

### Expert to write the

experts to design Programming Expert,
game
game interfaces, ….. Debugging Expert ……

### Planner Agent Observer Planner

(a) w/o Collaborative Discussion (b) w/ Collaborative Discussion
Figure5: ComparisonofwhetherthereisacollaborativediscussionintheDraftingStageinthetask
thatdevelopingPython-basedsoftwarefortheTetrisgame.
collaboration,italsorequiresself-refinementagentstoperformspecializedrolesforindividualtasks.
AsshownintheresultsinTable4,theperformanceofAutoAgentsdecreasesby3%intheabsence
of the self-refinement action. This observation corroborates the assertion that self-refinement is
instrumentalinaugmentingproficiencyintriviacreativewritingtasks. Furthermore,theenhancement
ofsingleagentsviaself-refinementplaysapivotalroleinfortifyingtheintegrityoftheoverarching
multi-agentframework.
Enhancingmulti-agentcollaborationthroughcollaborativerefinementaction. Forcollaborative
refinement,theprocessresemblesthecollaborativedialoguementionedabove,whichinvolvesintegratingknowledgefromdifferentdomainstoaccomplishtasksthatdemandcross-domainknowledge
fusion. TheresultsinTable4demonstratetheperformancewhencollaborativerefinementisabsent.
It’sobservablethatcomparedtothescenariowithAutoAgents,thereisadeclineof2%. Sincethe
necessityformultipleagentstocollaborateonasingletaskisentirelydependentonthedecisionmade
bytheagentinthedraftingphase,notallproblemsnecessarilyinvolvetasksthatrequirecollaborative
refinement. However,it’sevidentthatwhenthisprincipleisomittedfromtheprompt’sdesign,there’s
anoticeableperformancedecrease.
Improve the effectiveness of actions by dynamic memory. Dynamic memory predominantly
addressestherequisitesofspecializedagents.AsshowninFigure4,theActionObserveramalgamates
pivotaldataforforthcomingtasks,utilizingthehistoricalactionrecordsarchivedinlong-termmemory.
Table 4 elucidates a 1% diminution in the efficacy of AutoAgents bereft of dynamic memory.
Quintessential insights derived from dynamic memory are assimilated into the prompt, thereby
augmentingthecomprehensionofcriticalinformationandbolsteringtheoperationalproficiencyof
actions.
4.4 CaseStudy
TodemonstratetheapplicabilityofAutoAgentstomoresophisticatedandrealisticscenarios,we
conduct a case study in the software engineering domain. Software engineering is a complex
collaborativeendeavorthatinvolvesdiverserolesandresponsibilities. Fromdeveloperswhocreate
theunderlyingcode,toUIdesignerswhoprioritizeuserexperience,andsoftwaretesterswhoensure
thesoftware’squality,expertscollaborativelyworktoenhanceandrefinetheapplication,ensuring
thatitmeetsbothfunctionalanduser-centriccriteria.
AsanillustrationinFigure6,aTetrisgamehasbeendevelopedbyemployingAutoAgents,which
hasgeneratedvariousexpertroles,suchasgamedesignexpert,UIdesignexpert,programmer,and
debuggingexpert,toaccomplishthegamedevelopmenttask. Thegamedesignexpertsprovidethe
gamelogicdocumentsthatspecifytherulesandmechanicsofthegame.TheUIdesignexpertsdesign
theUIcomponentsthatcreatethevisualinterfaceofthegame.Theprogrammersimplementthegame
designbasedontheaforementioneddocumentsanduseappropriateprogramminglanguagesand
tools. Finally,thedebuggingexpertteststhegameanddebugestheprogramtoensureitsfunctionality
andquality. Thegamedevelopmentprocessisbasedonthecollaborationofmultipleexpertroles,
withmoreelaboratedocumentationandprograms,makingiteasierforuserstocomprehend.
5 Conclusion
This paper introduces AutoAgents, an innovative framework for automatically synthesizing collaborative specialized agents. AutoAgents mimics the collaborative process of human teams by
11

<!-- Page 12 -->

Figure6: Theillustrationofanexampleprocessofsoftwaredevelopment. Thetaskistodevelop
Python-basedsoftwarefortheTetrisgame.
decomposingtasksintodraftingandexecutionphasesanddelegatingdifferentsubtaskstodifferent
agents. OurexperimentalandempiricalevaluationvalidatestheadvantagesofAutoAgents, asit
surpasses single agents and other groupings in various tasks that demand diverse skills. Furthermore, our case study in software development illustrates the versatility and potential benefits of
ourproposedframework. AutoAgentsopensupnewpossibilitiesforenhancingtheinteractionand
cooperationamongagentsandtransformsthelandscapeofcomplexproblem-solving. Weenvisage
thatitsprinciplescanbefurthergeneralizedandrefinedtodealwithabroaderrangeoftasks,paving
thewaytowardsmoreusefulassistiveAI.
6 Acknowledgements
ThisworkwaspartiallysupportedbytheNationalKeyR&DProgramofChina(2022YFC2009600
and2022YFC2009606)andthePostdoctoralFellowshipProgramofCPSFunderGrantNumber

## Gzb20230024.


### References

[1] BrigidBarron. Achievingcoordinationincollaborativeproblem-solvinggroups. Thejournalof
thelearningsciences,9(4):403–436,2000. 1
[2] SébastienBubeck,VarunChandrasekaran,RonenEldan,JohannesGehrke,EricHorvitz,Ece
Kamar,PeterLee,YinTatLee,YuanzhiLi,ScottLundberg,etal. Sparksofartificialgeneral
intelligence: Earlyexperimentswithgpt-4. arXivpreprintarXiv:2303.12712,2023. 1
[3] Chi-MinChan,WeizeChen,YushengSu,JianxuanYu,WeiXue,ShanghangZhang,JieFu,
andZhiyuanLiu. Chateval: Towardsbetterllm-basedevaluatorsthroughmulti-agentdebate.
arXivpreprintarXiv:2308.07201,2023. 6
[4] GuangyaoChen,PeixiPeng,YangruHuang,MengyueGeng,andYonghongTian. Adaptive
discoveringandmergingforincrementalnovelclassdiscovery. InProceedingsoftheAAAI
ConferenceonArtificialIntelligence,volume38,pages11276–11284,2024. 21
[5] WeizeChen,YushengSu,JingweiZuo,ChengYang,ChenfeiYuan,ChenQian,Chi-MinChan,
YujiaQin,YaxiLu,RuobingXie,etal. Agentverse: Facilitatingmulti-agentcollaborationand
exploringemergentbehaviorsinagents. arXivpreprintarXiv:2308.10848,2023. 2,4,5,6,17
[6] XinyunChen, MaxwellLin, NathanaelSchärli, andDennyZhou. Teachinglargelanguage
modelstoself-debug. arXivpreprintarXiv:2304.05128,2023. 10
[7] YilunDu,ShuangLi,AntonioTorralba,JoshuaBTenenbaum,andIgorMordatch. Improving factuality and reasoning in language models through multiagent debate. arXiv preprint
arXiv:2305.14325,2023. 1,3
12

<!-- Page 13 -->

[8] YaoFu,HaoPeng,TusharKhot,andMirellaLapata. Improvinglanguagemodelnegotiation
withself-playandin-contextlearningfromaifeedback. arXivpreprintarXiv:2305.10142,2023.
2
[9] ZhibinGou,ZhihongShao,YeyunGong,YelongShen,YujiuYang,NanDuan,andWeizhu
Chen. Critic: Largelanguagemodelscanself-correctwithtool-interactivecritiquing,2023. 10
[10] SignificantGravitas. Auto-gpt: Anautonomousgpt-4experiment,2023. URLhttps://github.
com/Significant-Gravitas/Auto-GPT,2023. 2,5,7
[11] RuiHao,LinmeiHu,WeijianQi,QingliuWu,YiruiZhang,andLiqiangNie. Chatllmnetwork:
Morebrains,moreintelligence. arXivpreprintarXiv:2304.12998,2023. 1,3
[12] SiruiHong,XiawuZheng,JonathanChen,YuhengCheng,CeyaoZhang,ZiliWang,Steven
KaShingYau,ZijuanLin,LiyangZhou,ChenyuRan,etal. Metagpt: Metaprogrammingfor
multi-agentcollaborativeframework. arXivpreprintarXiv:2308.00352,2023. 2,3,5,6
[13] Wenlong Huang, Fei Xia, Ted Xiao, Harris Chan, Jacky Liang, Pete Florence, Andy Zeng,
Jonathan Tompson, Igor Mordatch, Yevgen Chebotar, et al. Inner monologue: Embodied
reasoningthroughplanningwithlanguagemodels. arXivpreprintarXiv:2207.05608,2022. 10
[14] Mandar Joshi, Eunsol Choi, Daniel Weld, and Luke Zettlemoyer. TriviaQA: A large scale
distantlysupervisedchallengedatasetforreadingcomprehension. InProceedingsofthe55th
AnnualMeetingoftheAssociationforComputationalLinguistics,pages1601–1611.Association
forComputationalLinguistics,July2017. 10
[15] MartinJosifoski,LarsKlein,MaximePeyrard,YifeiLi,SaiboGeng,JulianPaulSchnitzler,
YuxingYao,JihengWei,DebjitPaul,andRobertWest. Flows: Buildingblocksofreasoning
andcollaboratingai. arXivpreprintarXiv:2308.01285,2023. 3
[16] Guohao Li, Hasan Abed Al Kader Hammoud, Hani Itani, Dmitrii Khizbullin, and Bernard
Ghanem. Camel: Communicativeagentsfor"mind"explorationoflargescalelanguagemodel
society. arXivpreprintarXiv:2303.17760,2023. 2,3
[17] Tian Liang, Zhiwei He, Wenxiang Jiao, Xing Wang, Yan Wang, Rui Wang, Yujiu Yang,
ZhaopengTu, andShumingShi. Encouragingdivergentthinkinginlargelanguagemodels
throughmulti-agentdebate. arXivpreprintarXiv:2305.19118,2023. 1,3
[18] AmanMadaan,NiketTandon,PrakharGupta,SkylerHallinan,LuyuGao,SarahWiegreffe,Uri
Alon,NouhaDziri,ShrimaiPrabhumoye,YimingYang,etal. Self-refine: Iterativerefinement
withself-feedback. arXivpreprintarXiv:2303.17651,2023. 10
[19] JoshuaMaynez,ShashiNarayan,BerndBohnet,andRyanMcDonald. Onfaithfulnessand
factuality in abstractive summarization. In Proceedings of the 58th Annual Meeting of the
AssociationforComputationalLinguistics,pages1906–1919,Online,July2020.Association
forComputationalLinguistics. 1
[20] YNakajima. Task-drivenautonomousagentutilizinggpt-4,pinecone,andlangchainfordiverse
applications. Seehttps://yoheinakajima.com/task-driven-autonomous-agent-utilizing-gpt-4-
pinecone-and-langchain-for-diverse-applications(accessed18April2023),2023. 2,3
[21] LaurieMillerNelson. Collaborativeproblemsolving. InInstructional-designtheoriesand
models,pages241–267.Routledge,2013. 1
[22] OpenAI. Gpt-4technicalreport,2023. 1
[23] JoonSungPark,JosephCO’Brien,CarrieJCai,MeredithRingelMorris,PercyLiang,and
Michael S Bernstein. Generative agents: Interactive simulacra of human behavior. arXiv
preprintarXiv:2304.03442,2023. 2
[24] Joon Sung Park, Lindsay Popowski, Carrie Cai, Meredith Ringel Morris, Percy Liang, and
MichaelSBernstein. Socialsimulacra: Creatingpopulatedprototypesforsocialcomputing
systems. InProceedingsofthe35thAnnualACMSymposiumonUserInterfaceSoftwareand

### Technology,pages1–18,2022. 2,4,17

[25] Chen Qian, Xin Cong, Cheng Yang, Weize Chen, Yusheng Su, Juyuan Xu, Zhiyuan Liu,
and Maosong Sun. Communicative agents for software development. arXiv preprint
arXiv:2307.07924,2023. 6
[26] ChengweiQin,AstonZhang,ZhuoshengZhang,JiaaoChen,MichihiroYasunaga,andDiyi
Yang. Ischatgptageneral-purposenaturallanguageprocessingtasksolver? arXivpreprint
arXiv:2302.06476,2023. 1
13

<!-- Page 14 -->

[27] JeremyRoschelleandStephanieDTeasley. Theconstructionofsharedknowledgeincollaborativeproblemsolving. InComputersupportedcollaborativelearning,pages69–97.Springer,
1995. 1
[28] Noah Shinn, Beck Labash, and Ashwin Gopinath. Reflexion: an autonomous agent with
dynamicmemoryandself-reflection. arXivpreprintarXiv:2303.11366,2023. 10
[29] YuShu,SiweiDong,GuangyaoChen,WenhaoHuang,RuihuaZhang,DaochenShi,QiqiXiang,
andYeminShi. Llasm: Largelanguageandspeechmodel. arXivpreprintarXiv:2308.15930,
2023. 1
[30] StevenASloman. Theempiricalcasefortwosystemsofreasoning. Psychologicalbulletin,
119(1):3,1996. 1
[31] YasharTalebiradandAmirhosseinNadiri. Multi-agentcollaboration: Harnessingthepowerof
intelligentllmagents. arXivpreprintarXiv:2306.03314,2023. 3
[32] BoxinWang,WeixinChen,HengzhiPei,ChulinXie,MintongKang,ChenhuiZhang,Chejian
Xu,ZidiXiong,RitikDutta,RylanSchaeffer,etal.Decodingtrust:Acomprehensiveassessment
oftrustworthinessingptmodels. arXivpreprintarXiv:2306.11698,2023. 1
[33] PeiyiWang,LeiLi,LiangChen,DaweiZhu,BinghuaiLin,YunboCao,QiLiu,TianyuLiu,and
ZhifangSui. Largelanguagemodelsarenotfairevaluators. arXivpreprintarXiv:2305.17926,
2023. 9
[34] ZhenhailongWang,ShaoguangMao,WenshanWu,TaoGe,FuruWei,andHengJi. Unleashing
cognitivesynergyinlargelanguagemodels: Atask-solvingagentthroughmulti-personaselfcollaboration. arXivpreprintarXiv:2307.05300,2023. 1,2,3,4,5,6,9,10,17
[35] RossWilliams,NiyoushaHosseinichimeh,AritraMajumdar,andNavidGhaffarzadegan. Epidemicmodelingwithgenerativeagents. arXivpreprintarXiv:2307.04986,2023. 2,4,17
[36] AnitaWilliamsWoolley,IshaniAggarwal,andThomasWMalone. Collectiveintelligenceand
groupperformance. CurrentDirectionsinPsychologicalScience,24(6):420–424,2015. 5
[37] QingyunWu,GaganBansal,JieyuZhang,YiranWu,ShaokunZhang,ErkangZhu,BeibinLi,
LiJiang,XiaoyunZhang,andChiWang. Autogen: Enablingnext-genllmapplicationsvia
multi-agentconversationframework. arXivpreprintarXiv:2308.08155,2023. 2,3,5
[38] BenfengXu,AnYang,JunyangLin,QuanWang,ChangZhou,YongdongZhang,andZhendong
Mao. Expertprompting: Instructinglargelanguagemodelstobedistinguishedexperts. arXiv
preprintarXiv:2305.14688,2023. 2,4,5
[39] ShunyuYao,DianYu,JeffreyZhao,IzhakShafran,ThomasLGriffiths,YuanCao,andKarthik
Narasimhan. Treeofthoughts: Deliberateproblemsolvingwithlargelanguagemodels. arXiv
preprintarXiv:2305.10601,2023. 9,10
[40] ShunyuYao,JeffreyZhao,DianYu,NanDu,IzhakShafran,KarthikNarasimhan,andYuanCao.
React: Synergizingreasoningandactinginlanguagemodels. arXivpreprintarXiv:2210.03629,
2022. 7,10
[41] LianminZheng,Wei-LinChiang,YingSheng,SiyuanZhuang,ZhanghaoWu,YonghaoZhuang,
ZiLin,ZhuohanLi,DachengLi,EricXing,etal. Judgingllm-as-a-judgewithmt-benchand
chatbotarena. arXivpreprintarXiv:2306.05685,2023. 9

### A MoreExamples

Enhancing single-agent through self-refinement. Figure 7 depicts the self-refinement process
ofprogrammers’coding. Theyfirstwriteapseudocodefileandthengeneratethecorresponding
programfilesbasedonit. Thisrefinementprocesssignificantlyensuresthevalidityoftheoutputfile.
AlthoughAutoAgentsisaframeworkformulti-agentcollaboration,italsorequiresself-refinement
agentstoperformspecializedrolesforindividualtasks.
ImprovingTeamworkinMulti-AgentSystemswithCollaborativeRefinement. Incollaborative
refinement, the method is similar to the team discussions we talked about earlier. This involves
bringingtogetherinformationfromvariousfieldstocompletetasksthatrequireblendingknowledge
fromdifferentareas. AsillustratedinFigure8,duringthisprocess,thetwoagentsworktogetherto
14

<!-- Page 15 -->

Figure7: Anexampleoftheself-refinementprocessofprogrammers’coding
makesurethestorytheyproducemakessenseandisconsistentlyimprovedupon. Thisalsosupports
theideathatworkingtogetherinthiswayishelpfulwhendealingwithcomplicatedtasks.
Dynamicagentsenhancetheadaptabilityofcomplextasks.Theabilitytogeneratedynamicagents
forvarioustasksiscrucialforenhancingtheiradaptabilitytodiversescenarios. Figure9illustrates
the contrast between GPT4 and AutoAgents’ responses to open-ended questions. Unlike GPT-4,
AutoAgents can produce agents from three distinct domains, which can provide more elaborate
answers. ForthetriviacreativewritingtaskinFigure10and11,AutoAgentsemploysafour-step
approachfortaskdecomposition. Initially,itsourcestheanswertothegivenquestionusingadomainspecificagent,followedbytheconstructionofanarrative. Concurrently,theLanguageExpertAgent
playsapivotalrole,conductingmultiplecheckstoverifythecoherencebetweenthenarrativeandthe
question,thusguaranteeingthenarrative’saccuracy.
Furthermore,asillustratedinFigure12,theActionObserverorchestratestheinteractionamongmultiplegenerativeagents. Itprovidesaconcisesummaryofessentialinformation,provinginstrumental
infosteringcollaborationbetweenvariousintelligentagents. Thiscoordinationiskeytoensuring
theseamlessflowofthetaskexecutionprocess. Collectively,theseinstancesvividlyshowcasethe
adaptabilityandefficiencyofourdynamicagentgenerationframeworkinhandlingcomplextasks.
Conversely,thepromptemployedbyAutoAgentsexhibitsamoreuniversalnature,signifyingits
capacity to acclimate to diverse tasks without necessitating bespoke customization. As Table 5
15

<!-- Page 16 -->

Figure8: Anexampleofthecollaborativerefinementprocessoftriviacreativewriting.
16

<!-- Page 17 -->

Figure9: AnexampleoftheOpen-endedQuestionAnswer.
Table5: Comparisonofexistingandproposedframeworksformulti-agentgenerationmethods.

### AgentGeneralization

Framework Application PromptGeneralization
byMulti-AgentDiscussion

### SocialSimulacra[24] SocialSimulation (cid:37) (cid:37)

EpidemicModeling[35] SocialSimulation (cid:37) (cid:37)

### SSP[34] GeneralAutonomousAgents (cid:37) (cid:37)

AgentVerse[5] GeneralAutonomousAgents (cid:37) (cid:37)

### AutoAgents GeneralAutonomousAgents (cid:33) (cid:33)

delineates,bothAgentVerse6andSSP7haveimplementedtask-specificenhancementsforvariedtask
evaluations.Incontrast,ourmethodologyleveragesasingular,unifiedpromptformattoaccommodate
an array of tasks. The commendable efficacy in open-ended question-answer and trivia creative
writingtasksfurthercorroboratesthewide-rangingapplicabilityandversatilityofpromptdesign
withintheAutoAgentsframework.

### B HumanEvaluation

Inthissection,wepresentthecriteriaforhumanevaluation. Weinstructedthevolunteers,whoare
responsibleforassessingthequalityofdifferentfeedback,toadheretothesestandards.
[Text]HumanEvaluation
We would like to request your feedback on the response to the user question
displayed above. Please rate the helpfulness, relevance, accuracy, level of
details of their responses.
Each response receives an overall score on a scale of 1 to 10, where a higher
6https://github.com/OpenBMB/AgentVerse/tree/minecraft/agentverse/tasks
7https://github.com/MikeWangWZHL/Solo-Performance-Prompting/tree/main/prompts
17

<!-- Page 18 -->

Figure10: (Page1)AnexampleoftheTriviaCreativeWritingtask.
score indicates better overall performance. Please first provide a
comprehensive explanation of your evaluation, avoiding any potential bias and
ensuring that the order in which the responses were presented does not affect
your judgment.

### Output with the following format:

Evaluation evidence: <your evluation explanation here>
Score: <score>

### C Discussion

Limitations. AutoAgentsexhibitremarkableknowledgeacquisitionandadaptabilityintackling
complex tasks, but they are not flawless. One of the limitations is that they may still produce
erroneousoutcomesevenwithdynamicrolegeneration. Thiscouldbeascribedtotherationality
of role generation and planning arrangements. Although this framework employs collaborative
discussionstoenhancethequalityofrolegenerationandplanningarrangements,itstillnecessitatesa
18

<!-- Page 19 -->

Figure11: (Page2)AnexampleoftheTriviaCreativeWritingtask.
19

<!-- Page 20 -->

Figure12: AnexampleofthecoordinationprocessfortheActonObserveragent.
20

<!-- Page 21 -->

moreeffectivemethodforrecruitingteamsanddevisingplans,andfurtheramelioratesthequalityof
rolegenerationandplanningarrangements.
Furthermore,thedifferencesbetweendifferentrolesinthisframeworkmainlyhingeonvariationsin
promptandtoolusage,butthisdoesnotaccentuatethedistinctionsbetweendifferentexpertroles.
Inthefuture,itisimperativetoexplorehowtoincorporatemoreexpertknowledgeandcreatemore
professionalroleagents,inordertoimprovetheadaptabilityofprofessionalagentstoprofessional
problems.
Currently,AutoAgentsrelyheavilyonthepowerfullogicalandtextualcapabilitiesofGPT-4,and
theiradaptabilitytosomeearlierLLMsispoor.Inthefuture,itisessentialtoexploremorereasonable
promptstoimprovetheadaptabilityofAutoAgentstodifferentLLMs.
FutureWork. Cooperationamongmultipleagentsrequiresdynamicadaptationandcommunication.
TheinitialplangeneratedbyLLMsmaynotsufficetoachievethedesiredoutcomes[4],resultingin
erroneousfinaloutputresults. Hence,futuremulti-agentsystemsneedtoswiftlydetectandrectify
errorsandadjusttheirplansdynamicallytoalignwiththedesiredoutcomes.
ThememorycapacityofexistingagentsislimitedbythenumberoftokensinLLMs. Howtodevise
ahigh-qualitymemorymechanismthatenablesefficientretrievalandstorageofmemorybyagents
remainsanopenquestion.
Theprofessionalskillsofthegeneratedagentsareeffective,buttheycanbeimprovedbyretraining
orothermechanisms. Alternatively,anAgentBankcanbeestablishedtoenabletheinvocationof
professionalagentsondemand. Moreprofessionalagentconstructionisstillworthyofexploration.

### D Prompts

Inthissection,wepresentthepromptsoffivecomponentsinourframework: Planner,PlanObserver,
RoleObserver,ActionObserver,andCustomAgent. Thesepromptsaredesignedtoelicitthedesired
behaviorsandresponsesfromtheagentsindifferentscenariosandtasks.

### D.1 Planner

Thepromptdesignprinciplesoutlinedinthetemplatefocusoncreatingandutilizingspecialized
LLM-basedagentrolestosolvecomplextasksandproblems. Here’sasummaryoftheseprinciples:

## UnderstandingandBreakingDownTasks: Thefirststepinvolvescomprehensivelyunderstanding,analyzing,anddeconstructingthegiventaskorproblem.


## UtilizationofExistingExpertRoles:

• Fullyleverageexistingexpertrolessuitedtotheproblem.
• Ensurethattheseroleshavecooperativeordependentrelationships.
• OutputthedetailsofselectedrolesinJSONformat,includingtheiroriginalinformation.

## CreationofNewExpertRoles:

• Avoidduplicationoffunctionsinnewroles.
• Newrolesshouldhaveclearnames,detaileddescriptions,domainexpertise,availabletools,
executionsuggestions,andprompttemplates.
• Ensureeachnewexpertrolehasadistinctresponsibilityanddomainofexpertise.
• Specifythegoals,constraints,andtoolsetforeachnewrole.
• Provideexecutionsuggestionsanddevelopprompttemplatesforeachnewrole.
• OutputdetailsofnewrolesinJSONformat,followingaspecificstructure.

## CreationofDetailedExecutionPlan:

• Developacomprehensiveplanwithmultiplestepsaddressingtheproblem.
• Assignatleastoneexpertroletoeachstep,detailingtheircontributionsandcollaborations.
21

<!-- Page 22 -->

• Provide detailed descriptions for each step, including expected outputs and inputs for
subsequentsteps.
• Includeafinalindependentstepforalanguageexperttoprovideadetailedresponsetothe
user’squestion.
• Presenttheexecutionplanasanumberedlist,indicatingtheexpertrolesinvolvedineach
step.
Thisstructuredapproachensuresasystematicanddetailedresolutionoftasks,leveragingthespecializedexpertiseofvariousLLMagents.
[Prompt]Planner

## Prompt_Template = ’’’

-----
You are a manager and an expert-level ChatGPT prompt engineer with expertise
in multiple fields. Your goal is to break down tasks by creating multiple LLM
agents, assign them roles, analyze their dependencies, and provide a detailed
execution plan. You should continuously improve the role list and plan based
on the suggestions in the History section.
# Question or Task
{context}
# Existing Expert Roles
{existing_roles}
# History
{history}
# Steps
You will come up with solutions for any task or problem by following these steps:

## You should first understand, analyze, and break down the human’s problem/task.


## According to the problem, existing expert roles and the toolset ({tools}), you

will select the existing expert roles that are needed to solve the problem. You
should act as an expert-level ChatGPT prompt engineer and planner with expertise
in multiple fields, so that you can better develop a problem-solving plan and
provide
the best answer. You should follow these principles when selecting existing expert
roles:

### Make full use of the existing expert roles to solve the problem.


### Follow the requirements of the existing expert roles. Make sure to select the

existing expert roles that have cooperative or dependent relationships.

### You MUST output the details of the selected existing expert roles in JSON blob

format. Specifically, the JSON of each selected existing expert role should include
its original information.

## According to the problem, existing expert roles and the toolset ({tools}), you

will create additional expert roles that are needed to solve the problem. You
should act as an expert-level ChatGPT prompt engineer and planner with expertise in
multiple fields, so that you can better develop a problem-solving plan and provide
the best answer.
You should follow these principles when creating additional expert roles:

### The newly created expert role should not have duplicate functions with any

existing expert role. If there are duplicates, you do not need to create this role.

### Each new expert role should include a name, a detailed description of their

area of expertise, available tools, execution suggestions, and prompt templates.

### Determine the number and domains of expertise of each new expert role based on

the content of the problem. Please make sure each expert has a clear responsibility
and do not let one expert do too many tasks. The description of their area of
expertise should be detailed so that the role understands what they are capable of
doing.

### Determine the names of each new expert role based on their domains of

expertise. The name should express the characteristics of expert roles.

### Determine the goals of each new expert role based on their domains of

expertise. The goal MUST indicate the primary responsibility or objective that the
22

<!-- Page 23 -->

role aims to achieve.

### Determine the constraints of each new expert role based on their domains of

expertise. The constraints MUST specify limitations or principles that the role
must adhere to when performing actions.

### Determine the list of tools that each new expert needs to use based on the

existing tool set. Each new expert role can have multiple tools or no tool at all.
You should NEVER create any new tool and only use existing tools.

### Provide some suggestions for each agent to execute the task, including but not

limited to a clear output, extraction of historical information, and suggestions
for execution steps.

### Generate the prompt template required for calling each new expert role

according to its name, description, goal, constraints, tools and suggestions. A
good prompt template should first explain the role it needs to play (name), its
area of expertise (description), the primary responsibility or objective that the
role aims to achieve (goal), limitations or principles that the role must adhere to
when performing actions (constraints), and suggestions for agent to execute the
task (suggestions). The prompt MUST follow the following format "You are
[description], named [name]. Your goal is [goal], and your constraints are
[constraints]. You could follow these execution suggestions: [suggestions].".

### You must add a language expert role who does not require any tools and is

responsible for summarizing the results of all steps.

### You MUST output the details of created new expert roles in JSON blob format.

Specifically, The JSON of new expert roles should have a ‘name‘ key (the expert
role name), a ‘description‘ key (the description of the expert role’s expertise
domain), a ‘tools‘ key (with the name of the tools used by the expert role), a
‘suggestions‘ key (some suggestions for each agent to execute the task), and a
‘prompt‘ key (the prompt template required to call the expert role). Each JSON blob
should only contain one expert role, and do NOT return a list of multiple expert
roles. Here is an example of a valid JSON blob:
{{{{
"name": “ROLE NAME",
"description": "ROLE DESCRIPTONS",
"tools": ["ROLE TOOL"],
"suggestions": "EXECUTION SUGGESTIONS",
"prompt": "ROLE PROMPT",
}}}}

## Finally, based on the content of the problem/task and the expert roles, provide

a detailed execution plan with the required steps to solve the problem.

### The execution plan should consist of multiple steps that solve the problem

progressively. Make the plan as detailed as possible to ensure the accuracy and
completeness of the task. You need to make sure that the summary of all the steps
can answer the question or complete the task.

### Each step should assign at least one expert role to carry it out. If a step

involves multiple expert roles, you need to specify the contributions of each
expert role and how they collaborate to produce integrated results.

### The description of each step should provide sufficient details and explain how

the steps are connected to each other.

### The description of each step must also include the expected output of that

step and indicate what inputs are needed for the next step. The expected output of
the current step and the required input for the next step must be consistent with
each other. Sometimes, you may need to extract information or values before using
them. Otherwise, the next step will lack the necessary input.

### The final step should always be an independent step that says ‘Language

Expert: Based on the previous steps, please provide a helpful, relevant, accurate,
and detailed response to the user’s original question: XXX‘.

### Output the execution plan as a numbered list of steps. For each step, please

begin with a list of the expert roles that are involved in performing it.
# Format example
Your final output should ALWAYS in the following format:
{format_example}
# Suggestions
{suggestions}
23

<!-- Page 24 -->

-----
’’’

### D.2 AgentObserver

Theprompt’sdesignprinciplesfortheAgentObserverarecenteredonevaluatingandrefiningexpert
rolesforproblem-solving. Keyaspectsinclude:

## UnderstandingandAnalyzingtheTask: Comprehensiveanalysisoftheproblemortask.


## EvaluationofSelectedExpertRoles: Ensuringselectedrolesareeffective,meettheproblem’s

requirements,andtheirinformation(name,description,requirements)isaccuratelyrepresentedina
JSONformat.

## ReviewofCreatedExpertRoles:

• Avoidcreatingroleswithoverlappingfunctionswithexistingones.
• Includecompleteinformationforeachnewrole: name,detailedexpertisearea,toolsneeded,
executionsuggestions,andaprompttemplate.
• Assignclear, specificexpertisedomainstonewroles, avoidingoverlybroadormultiple
responsibilities.
• Namenewrolesmeaningfully,reflectingtheirdomainandfunction.
• Definecleargoalsandconstraintsforeachnewrole,alignedwiththeirexpertiseandthe
problem’srequirements.
• Selectappropriateexistingtoolsforeachrole,withoutcreatingnewones.
• Provideeffectiveexecutionsuggestionsandcreatestructuredprompttemplatesforeach
role.
• Includealanguageexpertroleforsummarizingresults.
• ReportingInspectionResults:Summarizefindings,clearlystatinganyerrorsorimprovement
suggestions,orindicate’NoSuggestions’ifnonearefound.
Thisapproachensuresathoroughandsystematicevaluationofexpertrolesforenhancedproblemsolvingefficiency.
[Prompt]AgentObserver

## Prompt_Template = ’’’

-----
You are a ChatGPT executive observer expert skilled in identifying problem-solving
plans and errors in the execution process. Your goal is to check if the created
Expert Roles following the requirements and give your improvement suggestions. You
can refer to historical suggestions in the History section, but try not to repeat
them.
# Question or Task
{question}
# Existing Expert Roles
{existing_roles}
# Selected Roles List
{selected_roles}
# Created Roles List
{created_roles}
# History
{history}
# Steps
You will check the selected roles list and created roles list by following these
24

<!-- Page 25 -->

steps:

## You should first understand, analyze, and break down the human’s problem/task.


## According to the problem, existing expert roles and the toolset ({tools}), you

should check the selected expert roles.

### You should make sure that the selected expert roles can help you solve the

problem effectively and efficiently.

### You should make sure that the selected expert roles meet the requirements of

the problem and have cooperative or dependent relationships with each other.

### You should make sure that the JSON blob of each selected expert role contains

its original information, such as name, description, and requirements.

## According to the problem, existing expert roles and the toolset ({tools}), you

should check the new expert roles that you have created.

### You should avoid creating any new expert role that has duplicate functions

with any existing expert role. If there are duplicates, you should use the existing
expert role instead.

### You should include the following information for each new expert role: a name,

a detailed description of their area of expertise, a list of tools that they need
to use, some suggestions for executing the task, and a prompt template for calling
them.

### You should assign a clear and specific domain of expertise to each new expert

role based on the content of the problem. You should not let one expert role do too
many tasks or have vague responsibilities. The description of their area of
expertise should be detailed enough to let them know what they are capable of
doing.

### You should give a meaningful and expressive name to each new expert role based

on their domain of expertise. The name should reflect the characteristics and
functions of the expert role.

### You should state a clear and concise goal for each new expert role based on

their domain of expertise. The goal must indicate the primary responsibility or
objective that the expert role aims to achieve.

### You should specify any limitations or principles that each new expert role

must adhere to when performing actions. These are called constraints and they must
be consistent with the problem requirements and the domain of expertise.

### You should select the appropriate tools that each new expert role needs to use

from the existing tool set. Each new expert role can have multiple tools or no tool
at all, depending on their functions and needs. You should never create any new
tool and only use the existing ones.

### You should provide some helpful suggestions for each new expert role to

execute the task effectively and efficiently. The suggestions should include but
not limited to a clear output format, extraction of relevant information from
previous steps, and guidance for execution steps.

### You should create a prompt template for calling each new expert role according

to its name, description, goal, constraints, tools and suggestions. A good prompt
template should first explain the role it needs to play (name), its area of
expertise (description), the primary responsibility or objective that it aims to
achieve (goal), any limitations or principles that it must adhere to when
performing actions (constraints), and some helpful suggestions for executing the
task (suggestions). The prompt must follow this format: “You are [description],
named [name]. Your goal is [goal], and your constraints are [constraints]. You
could follow these execution suggestions: [suggestions].”.

### You should always have a language expert role who does not require any tools

and is responsible for summarizing the results of all steps in natural language.

### You should follow the JSON blob format for creating new expert roles.

Specifically, The JSON of new expert roles should have a ‘name‘ key (the expert
role name), a ‘description‘ key (the description of the expert role’s expertise
domain), a ‘tools‘ key (with the name of the tools used by the expert role), a
‘suggestions‘ key (some suggestions for each agent to execute the task), and a
‘prompt‘ key (the prompt template required to call the expert role). Each JSON blob
should only contain one expert role, and do NOT return a list of multiple expert
roles. Here is an example of a valid JSON blob:
{{{{
"name": “ROLE NAME",
"description": "ROLE DESCRIPTONS",
"tools": ["ROLE TOOL"],
"suggestions": "EXECUTION SUGGESTIONS",
25

<!-- Page 26 -->

"prompt": "ROLE PROMPT",
}}}}

### You need to check if the tool contains other tools that are not in the tool

({tools}), and if they do, they should be removed.

## Output a summary of the inspection results above. If you find any errors or have

any suggestions, please state them clearly in the Suggestions section. If there are
no errors or suggestions, you MUST write ’No Suggestions’ in the Suggestions
section.
# Format example
Your final output should ALWAYS in the following format:
{format_example}
-----
’’’

### D.3 PlanObserver

ThedesignprinciplesforthePlanObserverinthispromptfocusonevaluatingandimprovingan

### ExecutionPlan. Thekeyelementsinclude:


## UnderstandingtheProblem: Beginwithathoroughunderstandingandanalysisofthehuman’s

problem.

## ReviewingtheExecutionPlan:

• Ensuretheplancontainsmultipledetailedstepsthatprogressivelysolvetheproblem,witha
summarythataddressesthetaskorquestion.
• Verify that each step assigns at least one expert role, detailing their contributions and
collaborationforintegratedresults.
• Providesufficientdetailsineachstep,explaininghowthestepsinterconnect.
• Includeineachstep’sdescriptionitsexpectedoutputandtheinputsneededforthenextstep,
ensuringconsistencyandcompleteness.
• Confirmthatthefinalstepinvolvesalanguageexpertrespondingtotheoriginalquestion.
• Outputting Inspection Results: Summarize the inspection findings, stating any errors or
improvementsuggestionsclearly,orindicate’NoSuggestions’ifnonearefound.
This approach ensures a systematic and thorough evaluation of the Execution Plan to enhance
problem-solvingeffectiveness.
[Prompt]PlanObserver

## Prompt_Template = ’’’

-----
You are a ChatGPT executive observer expert skilled in identifying problem-solving
plans and errors in the execution process. Your goal is to check if the Execution
Plan following the requirements and give your improvement suggestions. You can
refer to historical suggestions in the History section, but try not to repeat them.
# Question or Task
{context}
# Role List
{roles}
# Execution Plan
{plan}
# History
{history}
# Steps
26

<!-- Page 27 -->


### You will check the Execution Plan by following these steps:


## You should first understand, analyze, and disassemble the human’s problem.


## You should check if the execution plan meets the following requirements:


### The execution plan should consist of multiple steps that solve the problem

progressively. Make the plan as detailed as possible to ensure the accuracy and
completeness of the task. You need to make sure that the summary of all the steps
can answer the question or complete the task.

### Each step should assign at least one expert role to carry it out. If a step

involves multiple expert roles, you need to specify the contributions of each
expert role and how they collaborate to produce integrated results.

### The description of each step should provide sufficient details and explain how

the steps are connected to each other.

### The description of each step must also include the expected output of that

step and indicate what inputs are needed for the next step. The expected output of
the current step and the required input for the next step must be consistent with
each other. Sometimes, you may need to extract information or values before using
them. Otherwise, the next step will lack the necessary input.

### The final step should ALWAYS be an independent step that says ‘Language

Expert: Based on the previous steps, please respond to the user’s original
question: XXX‘.

## Output a summary of the inspection results above. If you find any errors or have

any suggestions, please state them clearly in the Suggestions section. If there are
no errors or suggestions, you MUST write ’No Suggestions’ in the Suggestions
section.
# Format example
Your final output should ALWAYS in the following format:
{format_example}
-----
’’’

### D.4 ActionObserver

ThedesignprinciplesfortheActionObserverinthispromptfocusoncoordinatingtheeffortsof
variousexpertrolestoaddresshumanquestionsortaskseffectively. Keyaspectsinclude:

## UnderstandingtheGoalorProblem: Startwithaclearunderstandingoftheultimategoalorthe

problemposedinthequestionortask.

## DeterminingandExecutingNextSteps:

• Reviewthehistoryofcompletedstepstounderstandtheprogressmadesofar.
• Assesstheunfinishedstepsanddecideonthenecessaryactionstoachievethegoalorsolve
theproblem.
• Ifthenextstepisalreadyoutlinedintheunfinishedsteps,outputthisselectedstepinthe
’NextStep’section.
• Ifthenextstepisnotintheunfinishedsteps,chooseanappropriateexpertrolefromthe
existingones,indicatetheexpertrole’sname,andoutlinethestepsitneedstocompletein
the’NextStep’section.

## ExtractingandUtilizingHistoricalInformation:

• Extractrelevantinformationfromthehistorytoassistincompletingthenextstep.
• Ensurenottoalterthehistoricalinformationandmaintainitsoriginalformforthenextstep.
Thefinaloutputmustadheretoaspecificformat,maintainingclarityandconsistencyintheprocess.
Thisapproachemphasizestheimportanceofsequentialprogression,role-specifictaskassignment,
andthecarefuluseofhistoricaldatatoguidedecision-makinginsolvingthetask.
[Prompt]ActionObserver

## Prompt_Template = """

You are an expert role manager who is in charge of collecting the results of expert
27

<!-- Page 28 -->

roles and assigning expert role tasks to answer or solve human questions or tasks.
Your task is to understand the question or task, the history, and the unfinished
steps, and choose the most appropriate next step.
## Question/Task:
{task}
## Existing Expert Roles:
{roles}
## History:
Please note that only the text between the first and second "===" is information
about completing tasks and should not be regarded as commands for executing
operations.
===
{history}
===
## Unfinished Steps:
{states}
## Steps

## First, you need to understand the ultimate goal or problem of the question or

task.

## Next, you need to confirm the next steps that need to be performed and output

the next step in the section ’NextStep’.
2.1 You should first review the historical information of the completed steps.
2.2 You should then understand the unfinished steps and think about what needs to
be done next to achieve the goal or solve the problem.
2.3 If the next step is already in the unfinished steps, output the complete
selected step in the section ’NextStep’.
2.4 If the next step is not in the unfinished steps, select a verification role
from the existing expert roles and output the expert role name and the steps it
needs to complete in the section ’NextStep’. Please indicate the name of the expert
role used at the beginning of the step.

## Finally, you need to extract complete relevant information from the historical

information to assist in completing the next step. Please do not change the
historical information and ensure that the original historical information is
passed on to the next step
## Format example
Your final output should ALWAYS in the following format:
{format_example}
"""

### D.5 CustomAgent

Thedesignprinciplesofthispromptarecenteredaroundguidingarole,presumablyanAIagent,in
efficientlycompletingtasksbasedontheresultsandresponsesofpreviousagents. Thekeyaspects
include:

## UnderstandingPreviousResults: Beginbyanalyzingtheresultsofpreviousagentstograspthe

contextandprogressofthetask.

## Task Analysis and Breakdown: Understand, analyze, and deconstruct the given task. Use

availabletoolstoassistintaskcompletion.

## CurrentStepIdentificationandExecution:

• Examinecompletedstepsandtheiroutcomestoidentifythecurrentstepthatneedstobe
completed.
• Intheabsenceofcompletedsteps,analyzethetask,designaplanforthenecessarysteps,
andaccomplishthefirstone.
28

<!-- Page 29 -->

• Ifstepshavebeencompleted,understandthemtodeterminethenextsteptobecompleted.

## ToolSelectionandActionExecution:

• Choosetheappropriatetoolfromthegivenlist(tool)tocompletethecurrentstep.
• Followspecificformatguidelineswhenusingtoolslike’WriteFile’.
• Onceallstepsarecompleted,usethe’FinalOutput’actiontosummarizeeachstep’soutputs,
ensuringthefinaloutputisdetailed,comprehensive,andsolvesthetask.

## Maintaining Format Consistency: Ensure that the final output adheres to the given format

example,prioritizinghelpfulness,relevance,accuracy,anddetail.
Thisapproachemphasizessystematicprogressionthroughtasks,leveragingtoolsandpriorwork,and
producingcomprehensiveanddetailedfinaloutputs.
[Prompt]CustomAgent

## Prompt_Template = ’’’

-----
{role} Base on the following execution result of the previous agents and completed
steps and their responses, complete the following tasks as best you can.
# Task {context}
# Suggestions
{suggestions}
# Execution Result of Previous Agents {previous}
# Completed Steps and Responses {completed_steps}
You have access to the following tools:
# Tools {tool}
# Steps

## You should understand and analyze the execution result of the previous agents.


## You should understand, analyze, and break down the task and use tools to assist

you in completing it.

## You should analyze the completed steps and their outputs and identify the

current step to be completed, then output the current step in the section
’CurrentStep’.
3.1 If there are no completed steps, you need to analyze, examine, and decompose
this task. Then, you should solve the above tasks step by step and design a plan
for the necessary steps, and accomplish the first one.
3.2 If there are completed steps, you should grasp the completed steps and
determine the current step to be completed.

## You need to choose which Action (one of the [{tool}]) to complete the current

step.
4.1 If you need use the tool ’Write File’, the ’ActionInput’ MUST ALWAYS in the
following format:
‘‘‘
>>>file name<<<
>>>>>
file content
<<<<<
‘‘‘
4.2 If you have completed all the steps required to finish the task, use the action
’Final Output’ and summarize the outputs of each step in the section ’ActionInput’.
Provide a detailed and comprehensive final output that solves the task in this
section. Please try to retain the information from each step in the section
’ActionInput’. The final output in this section should be helpful, relevant,
accurate, and detailed.
29

<!-- Page 30 -->

# Format example
Your final output should ALWAYS in the following format:
{format_example}
-----
’’’
Building upon the custom agent’s framework, a critical aspect of the refinement process is the
configurationof’completedsteps’instep3.1. Thespecificproceduralstepsforself-refinementand
collaborativerefinementareoutlinedasfollows:
Self-refinementAction: Duringitsfirstexecution,eachcustomagentomitstheoutlinedstep3.1and
proceedstocompletetheremainingsteps. Ifthetask’scriteriaarenotmetorthesteplimithasnot
beenreached,theoutcomesfromthisexecutionareincorporatedas’completedsteps’intheprompt
forthenextiterationofthetask. Insubsequentexecutions,thecustomagentwillexecuteallsteps,
continuingthisprocessuntilthetaskisdeemedsuccessfullycompleted.
Collaborative Refinement Action: This mirrors the self-refinement action, yet involves active
collaborationbetweenmultipleagents. Forinstance,whenagentsAandBcollaborateonatask,
Ainitiallybypassesstep3.1initsfirstexecution. Uponcompletion,BincorporatesA’sresultsas
’completedsteps’andthenexecutesallsteps. Inlatercycles,AandBalternatetheirrolesinthetask,
perpetuatingthiscollaborativecycleuntilajointconclusionisreached.
30