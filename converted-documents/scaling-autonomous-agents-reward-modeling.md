---
title: "Scaling Autonomous Agents Reward Modeling"
original_file: "./Scaling_Autonomous_Agents_Reward_Modeling.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["prompt-engineering", "llm", "rag", "chain-of-thought", "react"]
keywords: ["click", "search", "price", "armap", "page", "action", "arxiv", "you", "task", "reward"]
summary: "<!-- Page 1 -->

PublishedasaconferencepaperatICLR2025

## Armap: Scaling Autonomous Agents Via


## Automatic Reward Modeling And Planning


### ZhenfangChen∗ DelinChen∗ RuiSun∗

MIT-IBMWatsonAILab UMassAmherst UniversityofCalifornia,LosAngeles

### WenjunLiu∗ ChuangGan

UMassAmherst UMassAmherstandMIT-IBMWatsonAILab

## Abstract

Largelanguagemodels(LLMs)havedemonstratedremarkablecapabilitiesacross
a range of text-generation tasks. However, LLMs still struggle with problems
requiringmulti-step"
related_documents: []
---

# Scaling Autonomous Agents Reward Modeling

<!-- Page 1 -->

PublishedasaconferencepaperatICLR2025

## Armap: Scaling Autonomous Agents Via


## Automatic Reward Modeling And Planning


### ZhenfangChen∗ DelinChen∗ RuiSun∗

MIT-IBMWatsonAILab UMassAmherst UniversityofCalifornia,LosAngeles

### WenjunLiu∗ ChuangGan

UMassAmherst UMassAmherstandMIT-IBMWatsonAILab

## Abstract

Largelanguagemodels(LLMs)havedemonstratedremarkablecapabilitiesacross
a range of text-generation tasks. However, LLMs still struggle with problems
requiringmulti-stepdecision-makingandenvironmentalfeedback,suchasonline
shopping,scientificreasoning,andmathematicalproblem-solving.Unlikepuretext
data,collectinglarge-scaledecision-makingdataischallenging. Moreover,many
powerfulLLMsareonlyaccessiblethroughAPIs,whichhinderstheirfine-tuning
foragenttasksduetocostandcomplexity. ToaddressLLMagents’limitations,
we propose a framework that can automatically learn a reward model from the
environment without human annotations. This model can be used to evaluate
the action trajectories of LLM agents and provide heuristics for task planning.
Specifically,ourapproachinvolvesemployingoneLLM-basedagenttonavigate
an environment randomly, generating diverse action trajectories. Subsequently,
a separate LLM is leveraged to assign a task intent and synthesize a negative
responsealongsidethecorrectresponseforeachtrajectory. Thesetriplets(task
intent,positiveresponse,andnegativeresponse)arethenutilizedastrainingdata
to optimize a reward model capable of scoring action trajectories. This reward
modelcanbeintegratedwithLLM-basedagentsandvariousplanningalgorithms
toenhancetask-solvingperformance. Theeffectivenessandgeneralizabilityof
ourframeworkaredemonstratedthroughevaluationsconductedondifferentagent
benchmarks. Inconclusion,ourproposedframeworkrepresentsasignificantadvancementinenhancingLLMagents’decision-makingcapabilities. Byautomating
thelearningofrewardmodels,weovercomethechallengesofdatascarcityandAPI
limitations,potentiallyrevolutionizingtheapplicationofLLMsincomplexand
interactiveenvironments. ThisresearchpavesthewayformoresophisticatedAI
agentscapableoftacklingawiderangeofreal-worldproblemsrequiringmulti-step
decision-making.1

## 1 Introduction

DevelopingAIagentscapableofperceivingenvironments,understandinginstructions,andacting
to accomplish a wide range of tasks in interactive settings (Brooks, 1986) have many real-world
applications,includingvirtualhumanassistants(Reedetal.,2022;Casheekaretal.,2024),business
processmanagement(Kirchdorferetal.,2024),androboticprocessautomation(Ranaetal.,2023;
Ahnetal.,2022;Paloetal.,2023).
The recent advent of large generative models has revolutionized numerous applications, such as
questionanswering(Rajpurkaretal.,2016),textsummarization(Hermannetal.,2015),andmultimodalunderstanding(Chenetal.,2015;Goyaletal.,2017;Yuetal.,2016). However,whilethese
models excel in text comprehension and generation tasks, their performance in decision-making
scenarios—suchasonlineshoppingandscientificreasoningfallsrelativeshortofhumancapabilities.
∗Equalcontribution.
1Projectpage:https://armap-agent.github.io
1
5202
beF
71
]IA.sc[
1v03121.2052:viXra

<!-- Page 2 -->


### PublishedasaconferencepaperatICLR2025

(a)ExistingMethods Trajectory (c) Tree Planning

### Back to Search (Total results: 50)

I‘m looking for vans sport canvas Thought:I use search bar ...
G I e M n n p o e u d ra t e t l o i s o f n f s a iz s e h i 1 o 0 n . 5 s , n p e r a ic k e e r l o w w it e h r l t a h c a e n c 9 lo 0 s d u o r l e l a in rs . A fa c s t h io io n n : s s n ea e r a c k h e [ r v ] ans sport canvas B00JJGEU4I ... B08CD4CP2N A c S a t c a n ti t v o e a n V s : a f s l a e u s a e h r : i c o 0 h n .8 [ v s a n n e s a k s e p r o ] rt ...
Search … Search Default T A h c o ti u o g n h : t c : l I i c s k h [ o B u 0 l 0 d J J f G ilt E e U r 4 … I] Back to Search P S r i i z c e e : : $59 9 . 41. 1 to 0 $ 2 1 4 0 1 .5 .0 A St c a ti t o e n V : a c lu lic e k : [ 0 B . 0 7 8CD4CP2N] ... A St c a t t io e n V : a c lu lic e k : [ 0 B . 0 5 0JJGEU4I]
PolicyModel Thought: I should select size …Back to Search Price: $59.41. to $241.0 Action:click[9] Action:click[10.5]
Costly to fine-tune Policy Model (LLM) Action: click[10.5] Size: 9 10 10.5 StateValue:0.4 StateValue:0.7 ...
R M e a q n u y ir P e o m lic a y s M si o ve de h l u s m (L a L n M -a s n )a n r o e ta c t l e o d se d - a s t o a urced T A h c o ti u o g n h : t c : l I i c s k h [ o B u u l y d N c o lic w k ] on the…B ack to Search Buy Now A St c a t t io e n V : a c lu lic e k : [ 0 B .9 uy Now] T h h ig e h a li c g t h i t o e n d t b ra y j e g c re to e r n y
lines satisfies the goal.
(b)OurMethod Re 0 w .6 ard Guide … ... Trajectory ... S A u c N g t e i g o w e n s s t Tr E a v je a c lu to a r t i e e s
... ... TreePlanning Back to Search Default Automatic
Input Automatic 0.9 (Detailsonright) Default T A h c o ti u o g n h : t c : l I i c s k h [ o B u 0 l 8 d C fi D lt 4 e C r r P e 2 s N u ] lts… Pric S e iz : e $ : 7 1 8 0 . . 9 5 t o $79.9 PolicyModel RewardModel
Trajectories RewardModel PolicyModel ... ...
Figure1: InFig.1(a),weshowthatitisdifficultforLLMagentstogeneratemulti-stepplansinan
interactiveenvironmenttoachievetheinstructiongoal. However,itisrelativelyeasyforanLLMto
learnarewardmodelthatcanevaluatewhetherthetrajectoriesmeetthetaskinstructions,asshownin
Fig.1(b). InFig.1(c),weshowthatalearnedrewardmodelcanbeusedtoguidethedefaultpolicy
modelstoimproveactionplanning.
Thisdisparitylikelystemsfromthenatureofthetrainingdata. Largegenerativemodelsaretypically
pre-trainedonreadilyavailableimageandtextcorporafromtheinternet. Incontrast,trajectorydata
foragenttasks,whichrequiremulti-stepinteractionwiththeenvironment,ismorechallengingto
collectanddoesnotnaturallyoccurontheinternet. Furthermore,currentstate-of-the-artcommercial
LanguageLearningModels(LLMs),suchasGPT-4V(OpenAIetal.,2024)andGemini(Reidetal.,
2024),oftenprovideonlylimitedAPIsforgeneralusers. Thisrestrictionrendersiteitherinfeasible
orcost-prohibitivetofine-tunethesemodelsforspecificagenttasks,furtherimpedingprogressin
thisfield.
Previousstudieshaveexploredthedevelopmentofautonomousagentsfordecision-makingtasks
usinglargelanguagemodels(LLMs).Earlyresearch(Yaoetal.,2023a;Zhengetal.,2024;Dengetal.,
2024)utilizedinstructionpromptswithfew-shotexamplestodirectLLMsinhandlingvariousagent
tasks. Thesemethodsdonotrequiretask-specificfine-tuningbuthaveshownlimitedperformance
onbenchmarksrequiringinteractionwithenvironmentsandpreciseactionprediction. Adifferent
researchdirectioninvolvescollectinghumanpreferencedata(Hongetal.,2023)ordistillingtrajectory
datafromadvancedcommercialLLMAPIs(Zengetal.,2023;Dengetal.,2024)andfine-tuning
smalleropen-sourceLLMstocreatenewpolicymodelsforagenttasks. However,thisdistillation
processreliesonadvancedpre-trainedagentmodelsfortrajectorydataextraction,whichareoften
unavailable,expensive,orsubjecttocommercialrestrictions. Forinstance,datafrommodelssuchas
GPT-4orGeminicannotbeusedforcommercialpurposes.
Afundamentalpremiseofourapproachisthat,inmostagentapplications,evaluationiseasierthan
generation(Karp,1975;Naor,1996). AsillustratedinFig.1(a),generatingacorrectmulti-step
solutiontonavigatetothetargetpageischallengingsinceitneedstopredictmultipleactionsand
interactwiththeenvironment. However,itisrelativelysimpletoevaluatewhethertheoutputaction
trajectoriesandenvironmentstatesmeettheprovidedintenttofinda"vanssportcanvasfashion
sneaker". Buildingonthispremise,wesuggestthatdevelopingarewardmodelismorefeasiblethan
creatingapolicymodelforagenttasks. Withaneffectiverewardmodel,itbecomespossibletoguide
LLMsinplanningtasksbotheffectivelyandefficiently. Forinstance,asdepictedinFig.1(c),by
integratingtherewardmodelwithanLLM-basedagentandtheMonteCarloTreeSearch(MCTS)
algorithm (Silver et al., 2017; Coulom, 2006), we can simulate and evaluate the future states of
agenttasks,therebymakingbetterdecisionsforsubsequentactions. Thisapproachisanalogousto
mentalsimulation(Hegarty,2004;Lakeetal.,2017)incognitivescience,wherehumansenvisionthe
outcomesofpotentialactionstomakebetterdecisionsinproblem-solving.
WhilerewardmodelscanassistLLMagentsinplanning,developingtheserewardmodelspresents
significantchallenges.SomepriorstudieshaveutilizedpowerfulcommercialLLMAPIsasevaluators
fortasks(Kwonetal.,2023a). Althoughtheseapproacheshavedemonstratedeffectivenessincertain
applications,theyrelyonstate-of-the-artLLMmodelsforevaluation,whichareoftenexpensiveand
2

<!-- Page 3 -->


### PublishedasaconferencepaperatICLR2025

difficulttoscale.Inthispaper,weintroduceanautomatedmethodtolearnmulti-modalrewardmodels
withoutrelyingonstate-of-the-artLLMsforguidance.Furthermore,previousworkhasnotconsidered
integratingthelearnedrewardmodelswithvariousplanningalgorithmsforproblem-solving.
Theprocessoflearningtherewardmodelinvolvesthreesteps. Initially,weutilizeanLLM-based
agent (e.g., Dubey et al. (2024)) to navigate in the environments, aiming to achieve a randomly
proposedintentwhilecollectingextensiveactiontrajectorydemonstrations. Subsequently,theLLM
modelexaminesthecollectedtrajectoriesandproposesarefinedintentthatthesampledtrajectories
actuallyaccomplish. Additionally, weprompttheLLMtogeneratenegativetrajectoriesthatfail
toachievetheintendedtask. Finally,basedonthesyntheticdata(intents,positivetrajectories,and
negativetrajectories)collected,wetrainacustomizedrewardmodelusingwidelyadoptedvisionlanguage models such as VILA (Lin et al., 2023) to evaluate whether the user’s intent has been
fulfilledbytheactiontrajectories. Withthisautomaticrewardmodel,weenhancetheperformanceof
LLM-basedagentsinconjunctionwithvariousplanningalgorithmssuchasbestofn,reflexion,and

## Mcts.

Insummary,weintroduceanovelframeworkARMAP(autonomousAgentsfromautomaticReward
Modeling And Planning) for LLM-based agents incorporating an automatic reward model that
evaluatestaskcompletion,analogoustomentalsimulationinhumancognition.Thisframeworkoffers
severaladvantages: (1)Effectiveness: ItenhancestheperformanceofvariousLLMagentsacross
differenttasks. (2)Flexibility: Iteliminatestheneedforfine-tuningtheLLMsthemselvesandallows
foroptimizationofcustomrewardtargetsduringinference,enablingmorecontrollablegeneration.
(3)Practicality: Thetrainingoftheautomaticrewardmodeldoesnotrelyonlabor-intensivelabeling
orstate-of-the-artcommercialLLMs,makingitmorefeasibleandwidelyapplicable.

## 2 Related Work

LLMsforAgenttasks. Ourresearchisrelatedtodeployinglargelanguagemodels(LLMs)as
agentsfordecision-makingtasksininteractiveenvironments(Liuetal.,2023;Zhouetal.,2023;
Shridharetal.,2020;Toyamaetal.,2021). Earlierworks,suchas(Yaoetal.,2023a),fine-tuned
modelslikeBERT (Devlin etal., 2019)for decision-makinginsimplified environments, suchas
onlineshoppingormobilephonemanipulation. Withtheadventoflargelanguagemodels(Brown
et al., 2020; OpenAI et al., 2024), it became feasible to perform decision-making tasks through
zero-shotorfew-shotin-contextlearning. TobetterassessthecapabilitiesofLLMsasagents,several
modelshavebeendeveloped(Dengetal.,2024;Xiongetal.,2024;Hongetal.,2023;Yanetal.,
2023).Mostapproaches(Zhengetal.,2024;Dengetal.,2024)providetheagentwithobservationand
actionhistory,andthelanguagemodelpredictsthenextactionviain-contextlearning. Additionally,
somemethods(Zhangetal.,2023;Lietal.,2023;Songetal.,2024)attempttodistilltrajectories
fromstate-of-the-artlanguagemodelstotrainmoreeffectivepolicymodels. Incontrast,ourpaper
introducesanovelframeworkthatautomaticallylearnsarewardmodelfromLLMagentnavigation,
usingittoguidetheagentsinmakingmoreeffectiveplans.
LLM Planning. Our paper is also related to planning with large language models. Early researchers (Brown et al., 2020) often prompted large language models to directly perform agent
tasks. Later,Yaoetal.(2022)proposedReAct,whichcombinedLLMsforactionpredictionwith
chain-of-thoughtprompting(Weietal.,2022). Severalotherworks(Yaoetal.,2023b;Haoetal.,
2023;Zhaoetal.,2023;Qiaoetal.,2024)havefocusedonenhancingmulti-stepreasoningcapabilities
byintegratingLLMswithtreesearchmethods. Ourmodeldiffersfromthesepreviousstudiesin
several significant ways. First, rather than solely focusing on text generation tasks, our pipeline
addresses multi-step action planning tasks in interactive environments, where we must consider
not only historical input but also multimodal feedback from the environment. Additionally, our
pipelineinvolvesautomaticlearningoftherewardmodelfromtheenvironmentwithoutrelyingon
human-annotateddata,whereaspreviousworksrelyonprompting-basedframeworksthatrequire
largecommercialLLMslikeGPT-4(OpenAIetal.,2024)tolearnactionprediction. Furthermore,
ARMAPsupportsavarietyofplanningalgorithmsbeyondtreesearch.
LearningfromAIFeedback. IncontrasttopriorworkonLLMplanning,ourapproachalsodraws
on recent advances in learning from AI feedback (Bai et al., 2022; Lee et al., 2023; Yuan et al.,
2024; Sharma et al., 2024; Pan et al., 2024; Koh et al., 2024b). These studies initially prompt
state-of-the-artlargelanguagemodelstogeneratetextresponsesthatadheretopredefinedprinciples
3

<!-- Page 4 -->

PublishedasaconferencepaperatICLR2025

### AutomaticallyGeneratedDataset

Synthesize Initialized Task Instructions Sampled Trajectories

### PositiveTrajectories


### Iamlookingforjeanswith40wx34l TaskInstructions

size,andpricelowerthan200dollars. RefineTask Instructions NegativeTrajectories

### I am looking for straight leg jeans in

sandblast light color, also in 40w x 34l
Sample Trajectories size, and price lower than 170 dollars. Training TrainingPhase

### Data Reward

Actions Environment 1.0

### Search … Search

Sample NegativeTrajectories 0.0
... ...
search[…jeans…]

### Actions Environment


## B00K1E04Ec B000N8Rzkw

S $ tr 1 a 6 i . g 4 h 4 t t L o e g $ 4 Je 3 a .6 n 1 s, $ R 4 e 3 g .1 u 6 la t r o -F $ it 2 J 1 e 9 a . n 2 , 1 search[…jeans…] ... Infe D r a e t n a ce InferencePhase Reward
... ... 0 .. .9 .
click[B00K1E04EC] Price:$16.44 to $43.61 click[B00K1E04EC]
Size: 40wx32l 40wx34l… 0.1
click[40wx32l]

### Price:$16.44 to $43.61

click[40wx34l] Price:$16.44 to $43.61 Agent Reward Task
Size: 40wx32l 40wx34l… Size: 40wx32l 40wx34l… Model Model Instruction
click[BuyNow] Buy Now click[BuyNow] ... Tra P j o e s c i t t o iv r e ie s Tr N a e je g c a t t o iv ri e e s Tra Q je u c e to ry ri es
Figure2: ThepipelineofourARMAPframework. Wefirstgenerateaninitialtaskinstructionusing
LLMswithin-contextlearningandsampletrajectoriesalignedwiththeinitiallanguageinstructions
in the environment. Next, we use the LLM to summarize the sampled trajectories and generate
refinedtaskinstructionsthatbettermatchthesetrajectories. Wethenmodifyspecificactionswithin
thetrajectoriestoperformnewactionsintheenvironment, collectingnegativetrajectoriesinthe
process. Usingtherefinedtaskinstructions,alongwithbothpositiveandnegativetrajectories,we
trainalightweightrewardmodeltodistinguishbetweenmatchingandnon-matchingtrajectories. The
learnedrewardmodelcanthencollaboratewithvariousLLMagentstoimprovetaskplanning.
andthenpotentiallyfine-tunetheLLMswithreinforcementlearning. Likepreviousstudies,wealso
promptlargelanguagemodelstogeneratesyntheticdata. However,unlikethem,wefocusnoton
fine-tuningabettergenerativemodelbutondevelopingaclassificationmodelthatevaluateshowwell
actiontrajectoriesfulfilltheintendedinstructions. Thisapproachissimpler,requiresnorelianceon
state-of-the-artLLMs,andismoreefficient. Wealsodemonstratethatourlearnedrewardmodelcan
integratewithvariousLLMsandplanningalgorithms,consistentlyimprovingtheirperformance.
Inference-Time Scaling. Snell et al. (2024) validates the efficacy of inference-time scaling for
languagemodels. Basedoninference-timescaling,variousmethodshavebeenproposed,suchas
randomsampling(Wangetal.,2022b)andtree-searchmethods(Haoetal.,2023;Zhangetal.,2024a;
Guanetal.,2025). Concurrently,severalworkshavealsoleveragedinference-timescalingtoimprove
theperformanceofagentictasks. Kohetal.(2024b)adoptsatraining-freeapproach,employing
MCTStoenhancepolicymodelperformanceduringinferenceandpromptingtheLLMtoreturnthe
reward. Guetal.(2024)introducesanovelspeculativereasoningapproachtobypassirreversible
actions by leveraging LLMs or VLMs. It also employs tree search to improve performance and
promptsanLLMtooutputrewards. Yuetal.(2024)proposesReflective-MCTStoperformtree
searchandfine-tunetheGPTmodel,leadingtoimprovementsin Kohetal.(2024a). Puttaetal.
(2024)alsoutilizesMCTStoenhanceperformanceonweb-basedtaskssuchas Yaoetal.(2023a)
andreal-worldbookingenvironments. Linetal.(2025)utilizesthestepwiserewardtogiveeffective
intermediateguidanceacrossdifferentagentictasks. Ourworkdiffersfrompreviouseffortsintwo
keyaspects: (1)BroaderApplicationDomain. Unlikepriorstudiesthatprimarilyfocusontasksfrom
asingledomain,ourmethoddemonstratesstronggeneralizabilityacrosswebagents,mathematical
reasoning, and scientific discovery domains, further proving its effectiveness. (2) Flexible and
EffectiveRewardModeling. InsteadofsimplypromptinganLLMasarewardmodel,wefinetunea
smallscaleVLM(Linetal.,2023)toevaluateinputtrajectories.
4

<!-- Page 5 -->

PublishedasaconferencepaperatICLR2025

## 3 Model

In this section, we provide a detailed introduction to our framework, autonomous Agents from
automaticRewardModelingAndPlanning(ARMAP).Theframeworkincludesautomatedreward
data generation in section 3.2, reward model design in section 3.3, and planning algorithms in
section3.4.

## 1 Background

TheplanningtasksforLLMagentscanbetypicallyformulatedasaPartiallyObservableMarkov
DecisionProcess(POMDP):(X,S,A,O,T),where:
• X isthesetoftextinstructions;
• S isthesetofenvironmentstates;
• Aisthesetofavailableactionsateachstate;
• Orepresentstheobservationsavailabletotheagents,includingtextdescriptionsandvisual
informationabouttheenvironmentinoursetting;
• T :S×A→S isthetransitionfunctionofstatesaftertakingactions,whichisgivenby
theenvironmentinoursettings.
Givenataskinstructionx ∈X andtheinitialenvironmentstates ∈S,planningtasksrequirethe
0
LLMagentstoproposeasequenceofactions{a }N thataimtocompletethegiventask,where
n n=1
a ∈ Arepresentstheactiontakenattimestepn,andN isthetotalnumberofactionsexecuted
n
in a trajectory. Following the n-th action, the environment transitions to state s , and the agent
n
receivesanewobservationo . Basedontheaccumulatedstateandactionhistories,thetaskevaluator
n
determineswhetherthetaskiscompleted.
AnimportantcomponentofourframeworkisthelearnedrewardmodelR,whichestimateswhether
atrajectoryhhassuccessfullyaddressedthetask:
r =R(x,h), (1)
whereh={{a }N ,{o }N },{a }N aretheactionstakeninthetrajectory,{o }N arethe
n n=1 n n=0 n n=1 n n=0
correspondingenvironmentobservations,andristhepredictedrewardfromtherewardmodel. By
integratingthisrewardmodelwithLLMagents,wecanenhancetheirperformanceacrossvarious
environmentsusingdifferentplanningalgorithms.

## 2 Automaticrewarddatageneration.

To train a reward model capable of estimating the reward value of history trajectories, we first
needtocollectasetoftraininglanguageinstructions{x }M ,whereM representsthenumber
m m=1
of instruction goals. Each instruction corresponds to a set of positive trajectories {h+}M that
m m=1
match the instruction goals and a set of negative trajectories {h−}M that fail to meet the task
m m=1
requirements. Thisprocesstypicallyinvolveshumanannotatorsandistime-consumingandlaborintensive(Christianoetal.,2017;Rafailovetal.,2024). AsshowninFig.8oftheAppendix. we
automatedatacollectionbyusingLargeLanguageModel(LLM)agentstonavigateenvironments
andsummarizethenavigationgoalswithouthumanlabels.
InstructionSynthesis. Thefirststepindatagenerationistoproposeataskinstructionforagiven
observation. Weachievethisusingthein-contextlearningcapabilitiesofLLMs. Thepromptfor
instructiongenerationisshowninFig.9oftheAppendix. Specifically,weprovidesomefew-shot
examples in context along with the observation of an environment state to an LLM, asking it to
summarizetheobservationandproposeinstructiongoals. Inthisway,wecollectasetofsynthesized
languageinstructions{xraw}M ,whereM representsthetotalnumberofsynthesizedinstructions.
m m=1
TrajectoryCollection. Giventhesynthesizedinstructionsxraw andtheenvironment,anLLM-based
m
agent is instructed to take actions and navigate the environment to generate diverse trajectories
{xraw,h }M aimedataccomplishingthetaskinstructions. Here,h representsthem-thhistory
m m m=0 m
trajectory, which consists of N actions {a }N and N +1 environment observations {o }N .
n n=1 n n=0
DuetothelimitedcapabilitiesofcurrentLLMs,thegeneratedtrajectoriesh maynotalwaysalign
m
5

<!-- Page 6 -->


### PublishedasaconferencepaperatICLR2025

wellwiththesynthesizedtaskinstructionsx . Toaddressthis,weasktheLLMtosummarizethe
m
completedtrajectoryh andproposearefinedgoalxr . Thisprocessresultsinasetofsynthesized
m m
demonstrations{xr ,h }Mr ,whereM isthenumberofrefinedtaskinstructions.
m m m=0 r
PairwiseDataConstruction. Totrainarewardmodelcapableofdistinguishingbetweengoodand
poortrajectories,wealsoneedtrajectoriesthatdonotsatisfythetaskinstructions. Tocreatethese,
wesampleadditionaltrajectoriesthatdifferfrom{xr ,h }anddonotmeetthetaskrequirements
m m
bymodifyingactionsinh andgeneratingcorrespondingnegativetrajectories{h−}. Forclarity,
m m
werefertotherefinedsuccessfultrajectoriesas{x ,h+}andtheunsuccessfulonesas{x ,h−}.
m m m m
These paired data will be used to train the reward model described in Section 3.3, allowing it to
estimatetherewardvalueofanygiventrajectoryintheenvironment.

## 3 Rewardmodeldesign.

RewardModelArchitectures. Theoretically, wecanadoptanyvision-languagemodelthatcan
takeasequenceofvisualandtextinputsasthebackbonefortheproposedrewardmodel. Inour
implementation,weusetherecentVILAmodel(Linetal.,2023)asthebackboneforrewardmodeling
sinceithascarefullymaintainedopen-sourcecode,showsstrongperformanceonstandardvisionlanguagebenchmarkslike(Fuetal.,2023;Goyaletal.,2017;Hudson&Manning,2019),andsupport
multipleimageinput.
Thegoaloftherewardmodelistopredictarewardscoretoestimatewhetherthegiventrajectory
(x ,h )hassatisfiedthetaskinstructionornot,whichisdifferentfromtheoriginalgoalofVILA
m m
modelsthatgenerateaseriesoftexttokenstorespondtothetaskquery. Tohandlethisproblem,we
additionallyaddafully-connectedlayerforthemodel,whichlinearlymapsthehiddenstateofthe
lastlayerintoascalarvalue.
Optimazation Target. Given the pairwise data that is automatically synthesized from the environments in Section 3.2, we optimize the reward model by distinguishing the good trajectories
(x ,h+)frombadones(x ,h−). Followingstandardworksofreinforcementlearningfromhuman
m m m m
feedback (Bradley & Terry, 1952; Sun et al., 2023b;a), we treat the optimization problem of the
rewardmodelasabinaryclassificationproblemandadoptacross-entropyloss. Formally,wehave
L(θ)=−E [logσ(R (x ,h+)−R (x ,h−))], (2)
(xm,h+ m,h− m) θ m m θ m m
where σ is the sigmoid function and θ are the learnable parameters in the reward model R. By
optimizingthistarget,therewardmodelistrainedtogivehighervaluescorestothetrajectoriesthat
areclosertothegoaldescribedinthetaskinstruction.

## 4 Planningwithlargevision-Langaugerewardmodel.

After getting the reward model to estimate how well a sampled trajectory match the given task
instruction,weareabletocombineitwithdifferentplanningalgorithmstoimproveLLMagents’
performance. Here,wesummarizethetypicalalgorithmswecanadoptinthispaper.
BestofN.Thisisasimplealgorithmthatwecanadoptthelearnedrewardmodeltoimprovethe
LLM agents’ performances. We first prompt the LLM agent to generate n different trajectories
independently and choose the one with the highest predicted reward score as the prediction for
evaluation. Notethatthissimplemethodispreviouslyusedinnaturallanguagegeneration(Zhang
etal.,2024b)andweadoptitinthecontextofagenttaskstostudytheeffectivenessofthereward
modelforagenttasks.
Reflexion. Reflexion (Shinn et al., 2024) is a planning framework that enables large language
models (LLMs) to learn from trial-and-error without additional fine-tuning. Instead of updating
modelweights,Reflexionagentsuseverbalfeedbackderivedfromtaskoutcomes. Thisfeedbackis
convertedintoreflectivesummariesandstoredinanepisodicmemorybuffer,whichinformsfuture
decisions. Reflexionsupportsvariousfeedbacktypesandimprovesperformanceacrossdecisionmaking, coding, and reasoning tasks by providing linguistic reinforcement that mimics human
self-reflectionandlearning.
MCTS. We also consider tree search-based planning algorithms like Monte Carlo Tree Search
(MCTS) (Coulom, 2006; Silver et al., 2017) to find the optimal policy. There is a tree structure
6

<!-- Page 7 -->


### PublishedasaconferencepaperatICLR2025

constructedbythealgorithm,whereeachnoderepresentsastateandeachedgesignifiesanaction.
Beginningattheinitialstateoftherootnode,thealgorithmnavigatesthestatespacetoidentifyaction
andstatetrajectorieswithhighrewards,aspredictedbyourlearnedrewardmodel.
Thealgorithmtracks1)thefrequencyofvisitstoeachnodeand2)avaluefunctionthatrecordsthe
maximumpredictedrewardobtainedfromtakingactionainstates. MCTSwouldvisitandexpand
nodeswitheitherhighervalues(astheyleadtohighpredictedrewardtrajectory)orwithsmallervisit
numbers(astheyareunder-explored). Weprovidemoredetailsintheimplementationdetailsandthe
appendixsection.

## 4 Experiments

Inthissection,weconductaseriesofexperimentstodemonstratetheeffectivenessoftheproposed
framework for agent tasks. First, we evaluate the framework’s performance on standard agent
benchmarks(Yaoetal.,2023a;Wangetal.,2022a;Yaoetal.,2023b),detailedinSection4.2. Next,
weshowhowcustomizingtherewardtargetduringinferenceallowsustogeneratemoretailored
actionplans,asdescribedinSection4.3. Finally,weconductablationstudiesinSection4.4. Before
delvingintotheexperimentalresults,weprovideanoverviewofourexperimentalsetup.

## 1 Experimentalsetup

Environments. WeevaluatetheARMAPframeworkinthreedifferentenvironments:
• Webshopisawell-knownenvironmentforonlineshopping(Yaoetal.,2023a),wherethe
agentmustsearchforandselectproductsonthewebsitetoobtainafinalresult. Following
thesetupofAgentBench(Liuetal.,2023)forLLMevaluation,wetestthemodelonthe
validationsplit,usingthedefaultmatchingrewardastheevaluationmetric.
• ScienceWorld (Wang et al., 2022a) is an interactive benchmark designed for embodied
scienceexperiments. Itplacesagentsinasimulatedtext-basedenvironmentwherethey
mustperformelementaryscienceexperimentsbynavigatingtheenvironment,manipulating
objects,andobservingoutcomes.TheaimistoassesswhetherAImodelscanapplyscientific
knowledge,ratherthanmerelyretrieveorassembleinformation. Weevaluatetheframework
onbothseenandunseensplits.
• Gameof24isamathematicalgamewheretheagentisgivenfournumbersandmustuse
arithmeticoperations(addition,subtraction,multiplication,anddivision)tomakethenumber

### Forinstance,giventheinput’3,5,7,11,’onepossiblesolutionis’(7−3)∗(11−5)=24’.

FollowingYaoetal.(2023b),weselected100challengingpuzzles,specificallythoseindexed
from 901 to 1,000, and the performance metric is the success rate across these puzzles.
As shown in Fig. 7 of the Appendix, we use the chain-of-thought prompting technique,
promptingtheLLMagentstooutputintermediatestepsfollowedbythefinalanswer. Each
stepofthesolutionisconsideredanaction.
LLM Setup. Our framework requires LLM models to act as agents, generating synthetic task
instructionsfromtheenvironmentalongwithfew-shotexamplesinthepromptcontext. Wealso
deployagentstoperformthesesynthetictasksintheenvironment, collectingdiversetrajectories
forfurtheranalysis. Inthispaper,weprimarilyusetheLlama3-70b-instructmodel(Dubeyetal.,
2024)tosynthesizetrainingdatafortheautomaticrewardmodels,asitisopen-source,easytodeploy
locally,anddeliversrobustperformance. Weavoidstate-of-the-artcommercialmodelslikeGPT-4or
Geminiduetotheirhighcostsandthecomplexityofreproducingresultscausedbyfrequentmodel
updates,makingthemlesssuitableforourresearchobjectives.
ToevaluatetheperformanceofvariousLLMagents, weservearepresentativesetofLLMAPIs
locally, balancing model diversity with affordable serving costs. We identify the LLMs by their
modelfamilyandsize. Specifically,theseareLlama70B,Llama8B,Mistral7B,andPhi3.8B.Wenote
thattheseopen-sourcemodelfamiliesarefrequentlyupdated,andweprovidethecurrentmodellinks
intheAppendixA.3. AllmodelscanbeeasilysetupusingthevLLMlibrary(Kwonetal.,2023b)
andasingleH100GPU.
7

<!-- Page 8 -->


### PublishedasaconferencepaperatICLR2025

Baselines. WeimplementourARMAPframeworkusingdifferentplanningalgorithms,including
Reflexion,Best-of-N,andMCTS,whichwedenoteasARMAP-R,ARMAP-B,andARMAP-M,
respectively. WelimitthemaximumnumberoftrajectoriesourARMAPcanexploreto10inthe
ScienceWorld and Webshop environments to systematically evaluate the pipeline’s effectiveness
acrossdifferentLLMagentbackbones. Wealsocomparethemodelwithtwobaselinesthatdonot
userewardmodelguidance: SamplingandGreedy. FortheGameof24environment,wefollowthe
setupofapreviousstudy(Yaoetal.,2023b)andsetthemaximumnumberofexploredtrajectories
to 100. For Sampling, we set the model temperature to 1 and sample action trajectories using
chain-of-thoughtprompting(Weietal.,2023). ForGreedy,wesetthetemperatureto0,generating
theactionsequencewiththehighestprobability. Furtherimplementationdetailsareprovidedinthe
Appendix. Wewillreleaseallthecode,model,anddataforeasyreproductionuponacceptance.

## 2 Effectivenessforrewardplanning.

In this section, we investigate the effectiveness of the framework across different language models(Dubeyetal.,2024;Jiangetal.,2023;Abdinetal.,2024)andvariousplanningalgorithms. The
results are shown in Table 1. Based on the table, we have the following observations. First, our
proposedpipelineiseffective,asitconsistentlyoutperformstheSamplingandGreedybaselines
acrossdifferentplanningalgorithms. Additionally,weobservethattheaverageimprovementismore
significantonweakermodels,suchasPhi(Abdinetal.,2024)andMistral-7B(Jiangetal.,2023),
comparedtostrongermodelslikeLlama3-1-70B(Dubeyetal.,2024). Webelievethisisbecause
weakermodelsexploremorelow-rewardtrajectories,providinggreateropportunitiesforthereward
modeltoimproveperformance.
Amongthethreeplanningalgorithms,MCTSperformsthebestonaverage,likelyduetoitssuperior
mechanismsforidentifyinghigher-rewardtrajectoriesandsearchingless-exploredtrajectories. We
alsonoticethatReflexionperformstheworstonweakermodelslikeMistral7BandPhi3.8B.We
suspectthisisbecauseReflexionwasdesignedforChatGPT-family-basedagentsandrequiresthe
LLM agent to possess strong capabilities for learning from trial and error. Finally, we present
qualitativeresultsofdifferentmethodsinFig.3,whereitisclearthatourARMAPgeneratesbetter
trajectoriesthanthebaselines,aidedbytheguidanceofautomaticrewardmodels. InAppendixA.5,
we analyze several failure cases, offer more detailed insights into the limitations of the current
approach,andsuggestpotentialimprovementsinrewardmodeling.

## 3 Controllablegeneration.

AnotherbenefitofourARMAPpipelineisthatwecancustomizeourrewardtargetsduringinference,
allowing us to generate more controllable action sequences, rather than solely maximizing the
predictedrewards. Agentfine-tuningmethods(Lietal.,2023;Zengetal.,2023)finditchallenging
to achieve this goal since agent behaviors are typically fixed during inference. We conducted
experiments in the Webshop environment to evaluate the impact of customizable reward targets.
InadditiontotheoriginalobjectiveofmaximizingthepredictedrewardR(x,h),wedefinedtwo
additionaloptimizationtargets. First,weaimedtominimizethenumberofactionsinthetrajectory
history,definingtherewardtargetasR(x,h)−NumberOfAction(h).Second,wesoughttominimize
thepriceofthetargetproduct,withacustomizedtargetofR(x,h)−PriceOfProduct(h). Table2
presentstheresults.ByapplyingalengthpenaltyontherewardtargetforARMAP-M,wereducedthe
averageactionlengthfrom4.5to4andtheaverageproductpricefrom97.9to69.0,whilemaintaining
comparableperformanceonthedefaultmatchingreward. Similarperformancewasobservedfor
ARMAP-B.Additionally,weprovideaqualitativeexampleinFig.4. Fromthisexample,wecan
seethatourcustomizedrewardtargetsuccessfullyguidedtheLLMagenttopurchaseproductswith
feweractionstepswhilestillfindingthetargetproduct.

## 4 Ablationstudies.

Weconductablationstudiestoinvestigatetheeffectivenessoftheframework. Specifically,weaim
toanswerthefollowingquestions: Q1. Canwetrainapolicymodelwithfullysupervisedlearning
tohandlemulti-steptasksfromthesynthesizedtrajectorydata? Q2. Canalarge,generallanguage
modelbeusedastherewardmodeltoperformguidancewithoutautomaticrewardlearning?
8

<!-- Page 9 -->

PublishedasaconferencepaperatICLR2025

### ScienceWorld

Backbone Algorithms Webshop Game24 Average
seen unseen
Sampling 52.0 53.9 50.6 9.6 38.0

### Greedy 50.4 57.2 55.1 6.0 37.5

Llama70B ARMAP-R 56.5 59.0 56.7 16.0 43.5

## Armap-B 62.0 57.3 57.0 19.0 46.1


## Armap-M 66.8 58.2 55.9 24.0 49.3

Sampling 56.4 24.5 20.6 2.0 27.0

### Greedy 57.7 29.9 23.8 2.0 28.9

Llama8B ARMAP-R 58.3 31.2 28.0 6.0 31.3

## Armap-B 59.3 35.7 28.1 11.0 34.1


## Armap-M 60.2 32.5 24.9 9.0 32.6

Sampling 17.7 18.4 17.1 1.0 12.2

### Greedy 37.2 21.1 19.6 1.0 19.5

Mistral7B ARMAP-R 54.1 21.7 19.7 2.0 25.6

## Armap-B 54.4 24.5 21.2 2.0 26.4


## Armap-M 58.2 30.0 23.4 4.0 29.6

Sampling 34.7 10.0 7.6 2.0 15.2

### Greedy 42.4 9.5 6.5 2.1 17.5

Phi3.8B ARMAP-R 53.3 9.6 7.2 4.0 21.9

## Armap-B 52.1 20.0 17.0 9.0 26.5


## Armap-M 53.7 28.3 24.3 10.0 30.0

Table1: Effectivenessoftheproposedmethodondifferentbenchmarks. OurARMAPframework
consistentlyoutperformsthebaselinesacrossdifferentlanguagemodels.
Algorithms Action↓ Price↓ Reward↑

### Greedy 4.6 102.4 50.4


## Armap-B 4.7 102.2 62.0


## Armap-M 4.5 97.9 66.8


### ARMAP-B+Length-Penalty 3.9 98.8 60.3

ARMAP-M+Length-penalty 4.0 102.1 65.5
ARMAP-B+Price-penalty 5.0 65.5 57.5

### ARMAP-M+Price-penalty 4.3 69.0 62.4

Table2: ControllableTrajectoryGeneration. Weshowthatwecangeneratecontrollabletrajectories
likeshorteractionlengthsandlowerpricesbycustomizingrewardtargets. WeuseLlama70Basthe
defaultAPIforactionprediction.
WeconductedexperimentsusingtheScienceWorldbenchmark,andtheresultsareshowninTable3.
When comparing our pipeline to the SFT model trained using our reward backbone VILA3B,
weobservedthatalthoughthepolicymodeltrainedthroughfullysupervisedlearningperformed
reasonablywell(18.6),itstilllaggedbehindtheperformanceofourplanningframework(28.3). This
suggeststhatlearningapolicymodelismorechallengingthanlearningarewardmodel,highlighting
theeffectivenessofourproposedARMAPpipeline(answeringQ1).
Next,wereplacedoursmaller3Brewardmodelwithamuchlargerlanguagemodel,Llama3-1-70B,
andusedfew-shotpromptingtopredicttherewardoftheextractedtrajectories. Wefoundthatthis
largermodelalsoimprovedperformancecomparedtothedefaultgreedymodel,demonstratingthe
effectivenessofourplanningframework. However,itstillperformedworsethanourpipelineusing
automaticrewardlearning,despitetheLlama3-1-70Bbeingabout20timeslarger,furthershowcasing
theefficiencyandeffectivenessofourapproach(answeringQ2).
WeprovideadditionalablationexperimentsintheAppendixA.2,includingthedataqualityfrom
variousLLMs,rewardmodelingtargetandcomputationalefficiency.
9

<!-- Page 10 -->


### PublishedasaconferencepaperatICLR2025

I'm looking for furniture to make my living room and Search … Search Default

### PolicyModel

dinning room so nice, and price lower than 300 dollars.
search[furniture] Back to S . e . a . rch ... Back to Sea . r . c . h ...
search[furniture]
click[back to search]

## B09Lsbcvqt B07D54V8Ht

search[living room dining ... ... click[B09LSBCVQT] ReadingRoomSet,RestroomMirror,
room furniture] $957.34 $2488.95
click[B09MQFMCL8] B09MQFMCL8 B08J9WPMJ8
Table Set for 4 Price: Table Set for 6 Price: click[Buy Now] Buy Now
click[Buy Now] $259.99 $853.29

### Automatic

I need a blue women coat, and price lower than 80 dollars. Search … Search RewardModel
search[blue women Back to Search search[blue sherpa wool Back to Search
... ... ... ...
coat price < 80.00] sweatshirt price < 80.00]
click[B09LRVC4K2] click[B09LRVC4K2]

## B09Lrvc4K2 B08J9Wpmj8 B09Lrvc4K2 B08J9Wpmj8

click[blue] Price: $9.19 to $10.96 click[large] Price: $9.19 to $10.96
click[Buy Now] Color: blue purple black click[Buy Now] Size: large medium
Figure3: TwoqualitativeresultsoftheWebshoptask. Thefigureshowstwoexamplesutilizingthe
advantagesofourARMAPframeworkandweareabletocorrecterrorsmadebyexistingmethods.
In the top example, when the search results do not meet the requirements, our ARMAP method
leveragestheadvantageofthetreestructuretobacktrackandsearchagain,therebyretrievingthe
appropriatetargetitem. Incontrast,existingmethodsfailtobacktrackwhenthetargetitemisnot
found. Inthebottomexample,byusingtheARMAPtoevaluatedifferentstatesintheenvironment,
ourmethodisabletoselectthecolorthatoffersahigherrewardandbettermeetstherequirements
whenchoosingbetweensizeandcolor,ratherthanmistakenlyselectingthewrongsize. Thesetwo
examplessufficientlydemonstratetheadvantagesofourmethodcomparedtotraditionalapproaches.
Instruction: Please select a 1 pound, certified organic Celtic Sea Salt Sea Seasoning Sea Seasonings Triple 10 Ounce Jar Delicious
sea salt shaker in the flavor triple blend flakes, and Resealable Bags Shakers – Organic Blend Flakes 1 Ounces Blend of Sea
price lower than 30.00 dollars. $25.04 $6.89 $100.0 $13.15

## B0713Tmd19 B0007Smlum B01Ggwdb8S B01Ggwdb8S


### Greedy ARMAP ARMAP + L-penalty

Action1: search[1 pound certified ... Action1: search[organic sea salt ... Action1: search[organic sea salt ...
organic sea salt shaker triple blend shaker triple blend flakes price < shaker triple blend flakes 1 pound
flakes price < 30.00] B0007SMLUM B0713TMD19 30.00] B0007SMLUM B07SH4ZFY9 price < 30.00] B0007SMLUM B01GGWDB8S
Acti ... on2: clic N k[ O B0 T 7 O 1 r 3 g T a M ni D c 1 ! 9] P $ S 2 i r z 1 i 5 c e l . e : b 0 : 4 2 lb Action2: c W lic r k o [ n b g 0 S 7 i s z h e 4 ! zfy9] P $1 ri 3 c . e 1 : 5 A A c c t t i i o o n n 3 2 : : c c l l i i c c k k [ [ 1 B 0 p 0 o 0 u 7 n S d M (p L a U c M k ] of 1)] Price:
A A c c t t i i o o n n 6 7 : : c se li a c r k c [b h a [c c e k r t t i o fi e se d a o r r c g h a ] nic … ... A A c ct t i i o o n n 4 3: : c se li a c r k c [b h a [o c r k g a to n i s c e … ar c fl h a ] kes 1 ... Action4: click[triple blend flakes] $ S F 1 l i z a 1 3 e v l . : o b 1 r 5 : 1 oz
flakes 1 pound price < 30.00] pound price < 30.00] B0007SMLUMB01GGWDB8S Action5: click[Buy Now] triple blend flakes

### B0007SMLUM B01GGWDB8S Action5: click[B0007SMLUM]

Action8: clic P k[ r B ic 0 e 1 > G 3 G 0 W $ D ! B8S] P $1 ri 0 c 0 e . : 0 Action6: click[1 pound (pack of 1)] P $1 ri 3 c . e 1 : 5

### Action7: click[triple blend flakes] S i z 1 e l : b 1 oz

Action9: click[back to search] Search … Search Action8: click[Buy Now] F l a t v ri o p r l : e blend flakes
Failed with Reward = 0.0, Steps = 9 Succeed with Reward = 1.0, Steps = 8 Succeed with Reward = 1.0, Steps = 5
Figure4: Atypicalexampleofcustomizedrewardtargetforshortertrajectorygeneration. Onthe
left, we show the default greedy decoding generates a long trajectory without finding the target
product. Inthemiddle,weshowourdefaultrewardcanguidetheLLMagenttogenerateacorrect
butlongtrajectory. Ontheright,weshowourframeworkwithacustomizedrewardtargetforshorter
trajectories,whichfindsacorrectandshorttrajectoryforthetargetproduct.

## 5 Conclusion

Weproposeaframework,ARMAP,forlargelanguagemodel(LLM)agentstomanagetasksthat
requiremulti-stepdecision-makingandenvironmentalfeedback,suchasonlineshoppingorscientific
10

<!-- Page 11 -->

PublishedasaconferencepaperatICLR2025
Models ModelBase ScienceWorld(seen)

### Greedy Phi3.8B 9.6

SFT-Policy VILA3B 18.6

### ARMAP-Bw/oR 16.0

Llama70BandPhi3.8B
ARMAP-Mw/oR 26.5

## Armap-B 20.0

VILA3BandPhi3.8B

## Armap-M 28.3

Table3: Ablationstudyoftheproposedframework. OurARMAPframeworkismoreeffectivethan
directlyfindingapolicymodelandusingthegeneralLLMforrewardgeneration.
reasoning. ThisframeworkallowsLLM-basedagentstoenhancetaskplanningbyautonomously
learningarewardmodelfromtheenvironment,withouttheneedforhumanlabeling. Themethod
utilizespre-trainedLLMagentstogeneratediverseactiontrajectorieswithinanenvironment,which
are then evaluated by a separate LLM based on the task’s intent. These evaluations help train a
rewardmodelthatstrengthenstheagents’decision-makingcapabilities. Theframeworkenhancesthe
performanceofLLMagentsinaddressingcomplextasksandmitigatesissuesrelatedtodatascarcity
andAPIlimitations. Itseffectivenessisdemonstratedacrossvariousbenchmarks,representinga
significantadvancementinthedevelopmentofAIagentsforreal-world,multi-stepproblem-solving.

## References

MarahAbdin,JyotiAneja,HanyAwadalla,AhmedAwadallah,AmmarAhmadAwan,NguyenBach,
AmitBahree,andetal. Phi-3technicalreport: Ahighlycapablelanguagemodellocallyonyour
phone,2024. URLhttps://arxiv.org/abs/2404.14219.
MichaelAhn,AnthonyBrohan,NoahBrown,YevgenChebotar,OmarCortes,ByronDavid,and
etal. Doasicanandnotasisay: Groundinglanguageinroboticaffordances. InarXivpreprint
arXiv:2204.01691,2022.
YuntaoBai,SauravKadavath,SandipanKundu,AmandaAskell,JacksonKernion,AndyJones,Anna
Chen,AnnaGoldie,AzaliaMirhoseini,CameronMcKinnon,etal. Constitutionalai:Harmlessness
fromaifeedback. arXivpreprintarXiv:2212.08073,2022.
RalphAllanBradleyandMiltonETerry. Rankanalysisofincompleteblockdesigns: I.themethod
ofpairedcomparisons. Biometrika,1952.
R. Brooks. A robust layered control system for a mobile robot. IEEE Journal on Robotics and
Automation,2(1):14–23,1986. doi: 10.1109/JRA.1986.1087032.
TomB.Brown,BenjaminMann,NickRyder,MelanieSubbiah,JaredKaplan,PrafullaDhariwal,and
etal. Languagemodelsarefew-shotlearners,2020. URLhttps://arxiv.org/abs/2005.14165.
AvyayCasheekar,ArchitLahiri,KanishkRath,KaushikSanjayPrabhakar,andKathiravanSrinivasan.
A contemporary review on chatbots, ai-powered virtual conversational agents, chatgpt: Applications,openchallengesandfutureresearchdirections. ComputerScienceReview,52:100632,
2024.
XinleiChen,HaoFang,Tsung-YiLin,RamakrishnaVedantam,SaurabhGupta,PiotrDollar,and
C.LawrenceZitnick. Microsoftcococaptions: Datacollectionandevaluationserver,2015. URL
https://arxiv.org/abs/1504.00325.
PaulFChristiano,JanLeike,TomBrown,MiljanMartic,ShaneLegg,andDarioAmodei. Deep
reinforcement learning from human preferences. Advances in neural information processing
systems,2017.
RémiCoulom. Efficientselectivityandbackupoperatorsinmonte-carlotreesearch. InInternational
conferenceoncomputersandgames.Springer,2006.
11

<!-- Page 12 -->


### PublishedasaconferencepaperatICLR2025

XiangDeng,YuGu,BoyuanZheng,ShijieChen,SamStevens,BoshiWang,HuanSun,andYuSu.
Mind2web: Towardsageneralistagentfortheweb. AdvancesinNeuralInformationProcessing
Systems,2024.
JacobDevlin,Ming-WeiChang,KentonLee,andKristinaToutanova. Bert: Pre-trainingofdeep
bidirectionaltransformersforlanguageunderstanding,2019.
AbhimanyuDubey,AbhinavJauhri,AbhinavPandey,AbhishekKadian,AhmadAl-Dahle,andetal.
Thellama3herdofmodels,2024. URLhttps://arxiv.org/abs/2407.21783.
ChaoyouFu,PeixianChen,YunhangShen,YuleiQin,MengdanZhang,XuLin,JinruiYang,Xiawu
Zheng,KeLi,XingSun,etal. Mme: Acomprehensiveevaluationbenchmarkformultimodal
largelanguagemodels. arXivpreprintarXiv:2306.13394,2023.
Yash Goyal, Tejas Khot, Douglas Summers-Stay, Dhruv Batra, and Devi Parikh. Making the V
in VQA matter: Elevating the role of image understanding in Visual Question Answering. In
ConferenceonComputerVisionandPatternRecognition(CVPR),2017.
YuGu,BoyuanZheng,BoyuGou,KaiZhang,ChengChang,SanjariSrivastava,YananXie,PengQi,
HuanSun,andYuSu. Isyourllmsecretlyaworldmodeloftheinternet? model-basedplanning
forwebagents. arXivpreprintarXiv:2411.06559,2024.
XinyuGuan,LiLynaZhang,YifeiLiu,NingShang,YouranSun,YiZhu,FanYang,andMaoYang.
rstar-math: Smallllmscanmastermathreasoningwithself-evolveddeepthinking. arXivpreprint
arXiv:2501.04519,2025.
ShiboHao,YiGu,HaodiMa,JoshuaJiahuaHong,ZhenWang,DaisyZheWang,andZhitingHu.
Reasoningwithlanguagemodelisplanningwithworldmodel. arXiv,2023.
MaryHegarty. Mechanicalreasoningbymentalsimulation. Trendsincognitivesciences,2004.
KarlMoritzHermann,TomasKocisky,EdwardGrefenstette,LasseEspeholt,WillKay,MustafaSuleyman,andPhilBlunsom.Teachingmachinestoreadandcomprehend.InC.Cortes,N.Lawrence,
D.Lee,M.Sugiyama,andR.Garnett(eds.),AdvancesinNeuralInformationProcessingSystems,
volume 28. Curran Associates, Inc., 2015. URL https://proceedings.neurips.cc/paper_
files/paper/2015/file/afdec7005cc9f14302cd0474fd0f3c96-Paper.pdf.
WenyiHong,WeihanWang,QingsongLv,JiazhengXu,WenmengYu,JunhuiJi,YanWang,Zihan
Wang,YuxiaoDong,MingDing,andJieTang. Cogagent: Avisuallanguagemodelforguiagents,
2023.
DrewAHudsonandChristopherDManning. Gqa: Anewdatasetforreal-worldvisualreasoning
andcompositionalquestionanswering. ConferenceonComputerVisionandPatternRecognition

## (Cvpr),2019.

AlbertQ.Jiang,AlexandreSablayrolles,ArthurMensch,ChrisBamford,DevendraSinghChaplot,
Diego de las Casas, Florian Bressand, Gianna Lengyel, Guillaume Lample, Lucile Saulnier,
LélioRenardLavaud,Marie-AnneLachaux,PierreStock,TevenLeScao,ThibautLavril,Thomas
Wang,TimothéeLacroix,andWilliamElSayed. Mistral7b,2023. URLhttps://arxiv.org/
abs/2310.06825.
RichardMKarp. Onthecomputationalcomplexityofcombinatorialproblems. Networks,1975.
LukasKirchdorfer,RobertBlümel,TimotheusKampik,HanVanderAa,andHeinerStuckenschmidt.
Agentsimulator: Anagent-basedapproachfordata-drivenbusinessprocesssimulation. In2024
6thInternationalConferenceonProcessMining(ICPM),pp.97–104.IEEE,2024.
JingYuKoh,RobertLo,LawrenceJang,VikramDuvvur,MingChongLim,Po-YuHuang,Graham
Neubig, Shuyan Zhou, Ruslan Salakhutdinov, and Daniel Fried. Visualwebarena: Evaluating
multimodalagentsonrealisticvisualwebtasks. arXivpreprintarXiv:2401.13649,2024a.
JingYuKoh,StephenMcAleer,DanielFried,andRuslanSalakhutdinov. Treesearchforlanguage
modelagents. arXiv,2024b.
12

<!-- Page 13 -->


### PublishedasaconferencepaperatICLR2025

MinaeKwon,SangMichaelXie,KaleshaBullard,andDorsaSadigh. Rewarddesignwithlanguage
models,2023a. URLhttps://arxiv.org/abs/2303.00001.
WoosukKwon,ZhuohanLi,SiyuanZhuang,YingSheng,LianminZheng,CodyHaoYu,JosephE.
Gonzalez,HaoZhang,andIonStoica. Efficientmemorymanagementforlargelanguagemodel
servingwithpagedattention. InProceedingsoftheACMSIGOPS29thSymposiumonOperating
SystemsPrinciples,2023b.
Brenden M Lake, Tomer D Ullman, Joshua B Tenenbaum, and Samuel J Gershman. Building
machinesthatlearnandthinklikepeople. Behavioralandbrainsciences,2017.
HarrisonLee,SamratPhatale,HassanMansoor,KellieLu,ThomasMesnard,ColtonBishop,Victor
Carbune,andAbhinavRastogi. Rlaif: Scalingreinforcementlearningfromhumanfeedbackwith
aifeedback. arXiv,2023.
GuohaoLi,HasanAbedAlKaderHammoud,HaniItani,DmitriiKhizbullin,andBernardGhanem.
Camel: Communicativeagentsfor"mind"explorationoflargelanguagemodelsociety. InThirtyseventhConferenceonNeuralInformationProcessingSystems,2023.
Ji Lin, Hongxu Yin, Wei Ping, Yao Lu, Pavlo Molchanov, Andrew Tao, Huizi Mao, Jan Kautz,
MohammadShoeybi,andSongHan. Vila: Onpre-trainingforvisuallanguagemodels,2023.
ZongyuLin,YaoTang,XingchengYao,DaYin,ZiniuHu,YizhouSun,andKai-WeiChang. Qlass:
Boostinglanguageagentinferenceviaq-guidedstepwisesearch. arXivpreprintarXiv:2502.02584,
2025.
XiaoLiu, HaoYu, HanchenZhang, YifanXu, XuanyuLei, HanyuLai, YuGu, HangliangDing,
KaiwenMen,KejuanYang,ShudanZhang,XiangDeng,AohanZeng,ZhengxiaoDu,Chenhui
Zhang,ShengShen,TianjunZhang,YuSu,HuanSun,MinlieHuang,YuxiaoDong,andJieTang.
Agentbench: Evaluatingllmsasagents. arXivpreprintarXiv: 2308.03688,2023.
MoniNaor. Evaluationmaybeeasierthangeneration. InProceedingsofthetwenty-eighthannual
ACMsymposiumonTheoryofcomputing,pp.74–83,1996.
OpenAI,JoshAchiam,StevenAdler,SandhiniAgarwal,LamaAhmad,andetal. Gpt-4technical
report,2024.
NormanDiPalo, ArunkumarByravan, LeonardHasenclever, MarkusWulfmeier, NicolasHeess,
and Martin Riedmiller. Towards a unified agent with foundation models, 2023. URL https:
//arxiv.org/abs/2307.09668.
JiayiPan,YichiZhang,NicholasTomlin,YifeiZhou,SergeyLevine,andAlaneSuhr. Autonomous
evaluationandrefinementofdigitalagents,2024.
PranavPutta,EdmundMills,NamanGarg,SumeetMotwani,ChelseaFinn,DivyanshGarg,and
Rafael Rafailov. Agent q: Advanced reasoning and learning for autonomous ai agents. arXiv
preprintarXiv:2408.07199,2024.
Shuofei Qiao, Runnan Fang, Ningyu Zhang, Yuqi Zhu, Xiang Chen, Shumin Deng, Yong Jiang,
PengjunXie,FeiHuang,andHuajunChen. Agentplanningwithworldknowledgemodel,2024.
URLhttps://arxiv.org/abs/2405.14205.
RafaelRafailov,ArchitSharma,EricMitchell,ChristopherDManning,StefanoErmon,andChelsea
Finn. Directpreferenceoptimization: Yourlanguagemodelissecretlyarewardmodel. Advances
inNeuralInformationProcessingSystems,2024.
PranavRajpurkar,JianZhang,KonstantinLopyrev,andPercyLiang. Squad: 100,000+questionsfor
machinecomprehensionoftext,2016. URLhttps://arxiv.org/abs/1606.05250.
KrishanRana, JesseHaviland, SouravGarg, JadAbou-Chakra, IanReid, andNikoSuenderhauf.
Sayplan: Groundinglargelanguagemodelsusing3dscenegraphsforscalabletaskplanning. In
7thAnnualConferenceonRobotLearning,2023. URLhttps://openreview.net/forum?id=
wMpOMO0Ss7a.
13

<!-- Page 14 -->


### PublishedasaconferencepaperatICLR2025

ScottReed,KonradZolna,EmilioParisotto,SergioGomezColmenarejo,AlexanderNovikov,and
etal. Ageneralistagent,2022. URLhttps://arxiv.org/abs/2205.06175.
MachelReid,NikolaySavinov,DenisTeplyashin,DmitryLepikhin,TimothyLillicrap,Jean-baptiste
Alayrac,RaduSoricut,AngelikiLazaridou,OrhanFirat,JulianSchrittwieser,etal. Gemini1.5:
Unlockingmultimodalunderstandingacrossmillionsoftokensofcontext. arXiv,2024.
Samuel Schmidgall, Rojin Ziaei, Carl Harris, Eduardo Reis, Jeffrey Jopling, and Michael Moor.
Agentclinic: a multimodal agent benchmark to evaluate ai in simulated clinical environments,
2024.
Archit Sharma, Sedrick Keh, Eric Mitchell, Chelsea Finn, Kushal Arora, and Thomas Kollar. A
criticalevaluationofaifeedbackforaligninglargelanguagemodels. arXiv,2024.
NoahShinn,FedericoCassano,AshwinGopinath,KarthikNarasimhan,andShunyuYao. Reflexion:
Languageagentswithverbalreinforcementlearning. AdvancesinNeuralInformationProcessing
Systems,36,2024.
MohitShridhar,JesseThomason,DanielGordon,YonatanBisk,WinsonHan,RoozbehMottaghi,
LukeZettlemoyer,andDieterFox. Alfred: Abenchmarkforinterpretinggroundedinstructions
foreverydaytasks. InProceedingsoftheIEEE/CVFconferenceoncomputervisionandpattern
recognition,pp.10740–10749,2020.
MohitShridhar,XingdiYuan,Marc-AlexandreCôté,YonatanBisk,AdamTrischler,andMatthew
Hausknecht. ALFWorld: AligningTextandEmbodiedEnvironmentsforInteractiveLearning. In
ProceedingsoftheInternationalConferenceonLearningRepresentations(ICLR),2021. URL
https://arxiv.org/abs/2010.03768.
DavidSilver,ThomasHubert,JulianSchrittwieser,IoannisAntonoglou,MatthewLai,ArthurGuez,
MarcLanctot,LaurentSifre,DharshanKumaran,ThoreGraepel,etal. Masteringchessandshogi
byself-playwithageneralreinforcementlearningalgorithm. arXiv,2017.
CharlieSnell,JaehoonLee,KelvinXu,andAviralKumar. Scalingllmtest-timecomputeoptimally
canbemoreeffectivethanscalingmodelparameters. arXivpreprintarXiv:2408.03314,2024.
Yifan Song, Da Yin, Xiang Yue, Jie Huang, Sujian Li, and Bill Yuchen Lin. Trial and error:
Exploration-basedtrajectoryoptimizationofLLMagents. InLun-WeiKu,AndreMartins,and
VivekSrikumar(eds.),Proceedingsofthe62ndAnnualMeetingoftheAssociationforComputationalLinguistics.AssociationforComputationalLinguistics,2024.
ZhiqingSun,ShengShen,ShengcaoCao,HaotianLiu,ChunyuanLi,YikangShen,ChuangGan,
Liang-YanGui, Yu-XiongWang, YimingYang, etal. Aligninglargemultimodalmodelswith
factuallyaugmentedrlhf. arXiv,2023a.
ZhiqingSun,YikangShen,HongxinZhang,QinhongZhou,ZhenfangChen,DavidCox,Yiming
Yang,andChuangGan. Salmon: Self-alignmentwithprinciple-followingrewardmodels. arXiv,
2023b.
DanielToyama,PhilippeHamel,AnitaGergely,GheorgheComanici,AmeliaGlaese,ZafaraliAhmed,
TylerJackson,ShiblMourad,andDoinaPrecup. Androidenv: Areinforcementlearningplatform
forandroid. arXiv,2021.
RuoyaoWang,PeterJansen,Marc-AlexandreCôté,andPrithvirajAmmanabrolu. Scienceworld: Is
youragentsmarterthana5thgrader?,2022a. URLhttps://arxiv.org/abs/2203.07540.
XuezhiWang,JasonWei,DaleSchuurmans,QuocLe,EdChi,SharanNarang,AakankshaChowdhery,andDennyZhou. Self-consistencyimproveschainofthoughtreasoninginlanguagemodels.
arXivpreprintarXiv:2203.11171,2022b.
JasonWei,XuezhiWang,DaleSchuurmans,MaartenBosma,FeiXia,EdChi,QuocVLe,Denny
Zhou,etal. Chain-of-thoughtpromptingelicitsreasoninginlargelanguagemodels. Advancesin
neuralinformationprocessingsystems,2022.
14

<!-- Page 15 -->


### PublishedasaconferencepaperatICLR2025

JasonWei,XuezhiWang,DaleSchuurmans,MaartenBosma,BrianIchter,FeiXia,EdChi,QuocLe,
andDennyZhou. Chain-of-thoughtpromptingelicitsreasoninginlargelanguagemodels,2023.
URLhttps://arxiv.org/abs/2201.11903.
WeiminXiong,YifanSong,XiutianZhao,WenhaoWu,XunWang,KeWang,ChengLi,WeiPeng,
andSujianLi. Watcheverystep! llmagentlearningviaiterativestep-levelprocessrefinement.
arXiv,2024.
AnYan,ZhengyuanYang,WanrongZhu,KevinLin,LinjieLi,JianfengWang,JianweiYang,Yiwu
Zhong,JulianMcAuley,JianfengGao,etal. Gpt-4vinwonderland: Largemultimodalmodelsfor
zero-shotsmartphoneguinavigation. arXiv,2023.
ShunyuYao,JeffreyZhao,DianYu,NanDu,IzhakShafran,KarthikNarasimhan,andYuanCao.
React: Synergizingreasoningandactinginlanguagemodels. arXiv,2022.
Shunyu Yao, Howard Chen, John Yang, and Karthik Narasimhan. Webshop: Towards scalable
real-worldwebinteractionwithgroundedlanguageagents,2023a. URLhttps://arxiv.org/
abs/2207.01206.
ShunyuYao, DianYu, JeffreyZhao, IzhakShafran, ThomasL.Griffiths, YuanCao, andKarthik
Narasimhan. Treeofthoughts: Deliberateproblemsolvingwithlargelanguagemodels,2023b.
URLhttps://arxiv.org/abs/2305.10601.
LichengYu,PatrickPoirson,ShanYang,AlexanderC.Berg,andTamaraL.Berg. Modelingcontext
inreferringexpressions,2016. URLhttps://arxiv.org/abs/1608.00272.
XiaoYu, BaolinPeng, VineethVajipey, HaoCheng, MichelGalley, JianfengGao, andZhouYu.
Exact: Teachingaiagentstoexplorewithreflective-mctsandexploratorylearning. arXivpreprint
arXiv:2410.02052,2024.
WeizheYuan,RichardYuanzhePang,KyunghyunCho,SainbayarSukhbaatar,JingXu,andJason
Weston. Self-rewardinglanguagemodels. arXiv,2024.
AohanZeng,MingdaoLiu,RuiLu,BowenWang,XiaoLiu,YuxiaoDong,andJieTang.Agenttuning:
Enablinggeneralizedagentabilitiesforllms. arXiv,2023.
DiZhang,XiaoshuiHuang,DongzhanZhou,YuqiangLi,andWanliOuyang. Accessinggpt-4level
mathematicalolympiadsolutionsviamontecarlotreeself-refinewithllama-38b. arXivpreprint
arXiv:2406.07394,2024a.
HongxinZhang,WeihuaDu,JiamingShan,QinhongZhou,YilunDu,JoshuaBTenenbaum,Tianmin
Shu, and Chuang Gan. Building cooperative embodied agents modularly with large language
models. arXiv,2023.
ShunZhang,ZhenfangChen,SunliChen,YikangShen,ZhiqingSun,andChuangGan. Improving
reinforcementlearningfromhumanfeedbackwithefficientrewardmodelensemble. arXiv,2024b.
ZiruiZhao,WeeSunLee,andDavidHsu. Largelanguagemodelsascommonsenseknowledgefor
large-scaletaskplanning. InThirty-seventhConferenceonNeuralInformationProcessingSystems,
2023.
BoyuanZheng,BoyuGou,JihyungKil,HuanSun,andYuSu. Gpt-4v(ision)isageneralistweb
agent,ifgrounded. InForty-firstInternationalConferenceonMachineLearning,2024.
Shuyan Zhou, Frank F Xu, Hao Zhu, Xuhui Zhou, Robert Lo, Abishek Sridhar, Xianyi Cheng,
YonatanBisk,DanielFried,UriAlon,etal. Webarena: Arealisticwebenvironmentforbuilding
autonomousagents. arXivpreprintarXiv:2307.13854,2023. URLhttps://webarena.dev.
15

<!-- Page 16 -->

PublishedasaconferencepaperatICLR2025

## A Appendix

Inthissection,weprovidesupplementarymaterialforthemainpaper.

## A.1 Experimentsonalfworldandagentclinic.

WeextendourexperimentonALFWorld(Shridharetal.,2021),aclassicenvironmentforHouse-
Holding, where the agent must accomplish tasks in physical house-holding environments, like
“Put a pan on the dining table”. Following the setup of AgentBench (Liu et al., 2023) for LLM
evaluation,wetestthemodelonthedevandstdsplit,usingthedefaultsuccessrateastheevaluation
metric. Specifically,weusedLLaMa-3.1-70Btogeneratearound1600pairsofpositiveandnegative
sampleswithourdatagenerationpipeline. Thenwetrainarewardmodelwiththesesynthesizeddata.
WeevaluateourARMAPframeworkonALFWorldusingvariousplanningalgorithms,including
ReflexionandBest-of-N,whichwerefertoasARMAP-RandARMAP-B,respectively. Additionally,
wecompareourapproachwithtwobaselinemethodsthatdonotincorporaterewardmodelguidance:
SamplingandGreedy. Theresultsareshownbelow. AsshowninTable4,ourmodelstillperforms
wellinthischallengingenvironment,whichcontainsdiversescenesandlong-horizonplanningtasks.
Models ALFWorld-std ALFWorld-dev
Sampling 0.13 0.14

### Greedy 0.18 0.30


## Armap-R 0.22 0.35


## Armap-B 0.30 0.45

Table4: ExperimentalResultsonALFWorld.
We also extended our experiments to ClinicalAgent (Schmidgall et al., 2024), an environment
designed for medical decision-making tasks. ClinicalAgent evaluates models on their ability to
interpretclinicalscenariosandmakeaccurate,high-stakesdecisions. ResultsofClinicalAgentare
provided in Table 5, further supporting the versatility of ARMAP in domains requiring precise
reasoning.
Models AgentClinic-MedQA
Sampling 11.89

### Greedy 14.02


## Armap-B 44.33

Table5: ExperimentsResultsonAgentClinic.

## A.2 Ablationstudy.

DependenceonQualityofSyntheticDatafromVariousLLMs. WechooseScienceWorldand
conductexperimentstostudytheeffectivenessofdifferentrewardmodels. AsshowninTable6,the
leftcolumnrepresentstheresultsofusingLLaMA-8BgreedydirectlyandtheBestofNresultsof
LLaMA-8BwiththerewardmodeltrainedbythedatageneratedfromLLaMA-70B,LLaMA-8B,
Mistral-7B,andPhi-3.8B,respectively. Greedyisourbaselineresultanditcanbeobservedthat
usingtherewardmodelleadstobetterexperimentaloutcomes. Amongalltheresults,LLaMA-70B
achievesthebestperformance. Comparedtotheotherthreemodels,LLaMA-70Bhasthelargest
scaleandisnaturallythemostcapablemodel. LLaMA-8BandMistral-7Bhaveasimilarnumberof
parameters,andintheScienceWorldtask,Mistral-7BperformsbetterthanLLaMA-8B.Phi-3.8B
is the smallest of these models, yet it still achieved very good results. Notably, compared to the
larger-scale LLaMA-8B and Mistral-7B, Phi-3.8B still scored better. These results indicate that
our method exhibits good robustness when faced with LLMs of different scales and capabilities.
Evenwiththesmallestmodel,ourmethodcanstillachievegoodresults. Fromtheseexperimental
16

<!-- Page 17 -->

PublishedasaconferencepaperatICLR2025
Models SciWorld-seen SciWorld-unseen

### Greedy 29.9 23.8

Llama70B 35.7 28.1

### Llama8B 32.2 24.7

Mistral7B 33.7 26.5

### Phi3.8B 34.7 26.9

Table6: ExperimentsoftrainingdatageneratedfromvariousLLMs.
outcomes,itisclearthatourmethoddoesnotoverlyrelyonthecapabilitiesoflanguagemodels. In
otherwords,ourmethodishighlyefficientandrobust.
RewardModelingTarget. Tofurtherinvestigatetheoptimizationtargetoftherewardmodel,we
conductexperimentstocomparetheperformanceofpairwisecomparisonandbinaryclassification
aslearningmethodsfortherewardmodel. Specifically,intheclassificationsetting: eachinputpair
is treated as a positive and a negative example. The model is trained to predict a score of 1 for
positiveexamplesand0fornegativeexamples. ThecomparativeresultsareshowninTable7. Across
allsettings,pairwisecomparisonconsistentlyoutperformsbinaryclassification. Thisconfirmsthat
pairwisecomparisoncapturesnuancedpreferencesmoreeffectivelythanbinaryclassification,leading
tobetterrewardmodelingandoveralltaskperformance.
Classification Comparative

### Backbone Algorithms


### Seen Unseen Seen Unseen


## Armap-R 57.0 55.4 59.0 56.7


### LLaMA-70B


## Armap-B 47.2 43.3 57.3 57.0


## Armap-R 29.0 24.2 31.2 28.0


### LLaMA-8B


## Armap-B 27.5 22.2 35.7 28.1


## Armap-R 17.8 18.2 21.7 19.7


### Mistral-7B


## Armap-B 19.1 17.3 24.5 21.1


## Armap-R 8.6 4.8 9.6 7.2


### Phi-3.8B


## Armap-B 17.7 13.7 20.0 17.0

Table7: ComparisonoftheClassificationtargetandComparisontargetonScienceWorld.
ComputationalEfficiencyAnalysis. Wefurtherstudythedatademandsoftherewardmodelings.
Weshowtheperformanceofusingdifferentamountsoftrainingdata. InTable8andTable9,we
selectedScienceWorldandusedARMAP-Bastheexperimentalsetting. Intheleftmostcolumn,we
listedthedifferentLLMsusedinourstudy. Inthefirstrow,weintroducedVILA-3B,VILA-13B,
andLLaVA-13B,tocomparetheimpactofdifferentsizesandtypesofrewardmodelsonthefinal
outcomes. Inthelasttwocolumns,wetrainedtherewardmodelsusing1/5and1/25oftheoriginal
trainingdatasetsize,respectively,toassesshowvaryingamountsoftrainingdataaffectourmethod.
(1)Asseen, theeffectivenessofourmethodcontinuestoimprovewithincreasingrewardmodel
sizes. However,intheexperimentswithLLaMA-8BandPhi-3.8B,despiteusingmorepotentreward
models, there was no improvement in results. We believe that in the processes of planning and
reasoning,thecapabilityofthepolicymodelstillplaysadominantrole. Ifthepolicymodelismore
robust, andconcurrently, ifweenhancethecapabilityoftherewardmodel, wecancontinuously
achieve better results. (2) We also observe that the performance of LLaVA-13B is not as good
asVILA-13B.WeattributethistoVILAbeinganimprovedversionofLLaVA,anditutilizesan
interleavedimage-textdatasetinitstraining,whichbetteraidsthemodelinperceiving,understanding,
andhandlingmultimodalinformation. Hence,VILAoutperformsLLaVA.(3)FromtheTable8and
Table9,itisevidentthatregardlessofwhetherthedataisseenorunseen,increasingthemodelsize
improvesthefinalexperimentalresults. IfweusetheresultsoftheVILA-3Bmodelasabenchmark
andcompareitwiththetwosettings,1/5dataand1/25data,itisclearthatincreasingthetraining
dataenhancestheoutcomes. Conversely,evenwhenusingextremelylimiteddataamountslike1/5
17

<!-- Page 18 -->


### PublishedasaconferencepaperatICLR2025

or1/25oftheoriginaldataset,wecanstillachieveacapablemodel,andtheperformancedoesnot
dramaticallydecrease.
Theseresultsdemonstratethatourmethodcanstillyieldgoodresultsinalow-resourceenvironment.
Inotherwords,ourapproachdoesnotrelyonlargevolumesofdataandthestrongcapabilityoflarge
models;itissuccinctandefficient,capableofperformingwellinextremelylow-resourcesettings.
Backbone VILA-3B VILA-13B LLaVA-13B 1/5Data 1/25Data
LLaMA-70B 57.3 61.2 44.3 52.1 50.6

### LLaMA-8B 35.7 34.3 26.0 31.4 29.3

Mistral-7B 24.5 26.0 19.5 22.6 21.7

### Phi-3.8B 20.0 19.5 16.7 17.9 13.9

Table8: ComparisonofrewardmodelselectionanddatademandsonScienceWorldseenset.
Backbone VILA-3B VILA-13B LLaVA-13B 1/5Data 1/25Data
LLaMA-70B 57.0 60.7 48.2 50.0 47.7

### LLaMA-8B 28.1 27.5 22.2 26.8 24.2

Mistral-7B 21.1 22.9 19.2 21.6 19.7

### Phi-3.8B 17.0 15.3 13.7 14.2 11.7

Table9: ComparisonofrewardmodelselectionanddatademandsonScienceWorldunseenset.
AblationonVisualInput. Wealsotrainanewrewardmodelwithoutvisualinformation. Asshown
inTable10,wecanseethat,indifferentsettings,therewardmodelwithvisualinformationperforms
betterthanthemodelwithoutvisualinformation,whichshowstheimportanceofvisualcontextin
theWebshoptask.
Backbone Algorithms w/ovisual w/visual

## Armap-R 56.1 56.5


### LLaMA-70B


## Armap-B 61.6 62.0


## Armap-R 53.6 54.1


### Mistral-7B


## Armap-B 51.3 54.4

Table10: Ablationofthevisualinput.
OverheadinDataSynthesis. Wecalculatethetokenswehaveusedfortaskinstructiongeneration
andtrajectoryexploration. WesummarizetheseoverheadsinTable11. Toprovideamoreintuitive
comparison,wefirstcalculatedtheaveragetokenspersampleforthesedifferenttasks. Wefoundthat
althoughGameof24overallconsumesthemosttokens,theaveragenumberoftokensspentperGame
of24sampleisrelativelytheleast. Incontrast,Webshophasthefewesttotalsamplesbutthehighest
averagenumberoftokensspentpersample. ScienceWorldfallsinbetweenthesetwo. Thereason
WebshophasahigheraveragenumberoftokenscomparedtoGameof24isthattheenvironment
requiredforWebshopismorecomplex,involvingmorediverseelementsandpossibilities.
Tasks Samples Tokens TokensperSample
ScienceWorld 4064 2541255 625

### Webshop 2436 6645746 2728


### Gameof24 37885 12846182 339

Table11: Tokensofdatagenerationinthreedifferenttasks.
ProprietaryModelsasTrainingDataGeneratorsandPolicyModels. Inthemaincontent,we
mainlyconsiderusingopen-sourcemodelstoactastrainingdatageneratorsandpolicymodels. In
18

<!-- Page 19 -->


### PublishedasaconferencepaperatICLR2025

ordertoinvestigatetheupperboundsofourproposedmethod,wealsoconductsomeexperiments
by using powerful proprietary models. However, to serve as the training data generator, closedsourcemodelshaveseveraldrawbacks,includinghighcosts,limitedcommercialaccess,andlackof
reproducibility. Incontrast,ourapproachachievesstrongresultswithoutrelyingonclosed-source
models. GiventheexpenseassociatedwithAPI-basedmodelslikeGPT-4oforgeneratingtraining
datasets,wehaveoptednottopursuethismethodfornow.
ForAPI-basedproprietarymodelsservingaspolicymodels,thehighcostofGPT-4oandAPIaccess
ratelimitationspromptedustofocusourexperimentsprimarilyonALFWorld. Specifically,weused
GPT-4o-2024-08-06tosamplefivetrajectorieseachonALFWorld’sDevandStdsets,thenconducted
experimentsusingourautomaticrewardmodel. AsshowninTable12,ourrewardmodelisableto
helpthepowerfulGPT-4ogainbetterperformance,demonstratingtheeffectivenessofourframework.

### GPT-4o Std Dev

Sampling 0.74 0.88

### Greedy 0.82 0.90


## Armap-B 0.84 0.95

Table12: ExperimentsofusingtheproprietarymodelonALFWorld

## A.3 Implementationdetails.

LargePretrainModelSetup. Weserveadiversesetofopen-sourceLLMAPIstoevaluatethe
effectiveness of the proposed pipeline. We list all the open-source models and their weights on
huggingface in table 13. All these models can be easily setup and reproduced with the VLLM
libarary(Kwonetal.,2023b). WeprovetheeffectivenessofourARMAPframeworkacrossdifferent
LLMAPIs.

### Acronym Modeldescriptionandweightonhuggingfacewebsites

Llama70B https://huggingface.co/hugging-quants/Meta-Llama-3.1-70B-Instruct-AWQ-INT4
Llama8B https://huggingface.co/meta-llama/Meta-Llama-3.1-8B-Instruct
Mistral7B https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3
Phi3.8B https://huggingface.co/microsoft/Phi-3.5-mini-instruct
VILA3B https://huggingface.co/Efficient-Large-Model/VILA1.5-3b
Table13: Agentmodels,therewardmodel,andtheirassociateddescriptiononhuggingfacewebsites.
EnvironmentSetup. Webuildourenvironmentsbasedontheenvironmentsetupoftheprevious
works (Liu et al., 2023; Song et al., 2024; Yao et al., 2023b; Shridhar et al., 2021; Schmidgall
etal.,2024). ForWebshopandALFWorldenvironment,westartthesedockerenvironmentsfrom
AgentBench(Liuetal.,2023)andimplementdifferentplanningalgorithms,Reflexion,Best-of-N
andMCTSonit. Similarly,webuildourScienceWorld,Gameof24andAgentClinicenvironments
from Songetal.(2024), Yaoetal.(2023b)andSchmidgalletal.(2024),respectively.
PlanningAlgorithmDetails. Wecomparetheperformanceofdifferentplanningalgorithmsby
limiting their maximum explored trajectory number. We set the maximum number to be 10 on
WebshopandScieneWorldinconsiderationofeffectivenessandefficiency. Wesetthemaximum
numbertobe100onGameof24followingthesetupof Yaoetal.(2023b).InWebshop,ScienceWorld,
ALFWorldandAgentClinicbenchmarks,weonlyconsiderthetop10availableactionssuggestedby
theLLMagentateachstatetoreducesearchspace. Wealsosetatrajectory’smaximalactionnumber
lengthto10forsimplicity.
ForReflexion,wesetthemaximumtrialnumbertobe10foralltasks. Fordifferenttasksandmodels,
wesetthethresholdofReflexionseparately. Duringtheiterationprocess,iftherewardofthecurrent
19

<!-- Page 20 -->


### PublishedasaconferencepaperatICLR2025

trail’strajectoryexceedsthethreshold,theiterationwillstop,andthecurrenttrailwillbetakenas
theresult. Ifthemaximumnumberoftrialsisreached,thelasttrialwillbetakenastheresultin
WebshopandGameof24,whilethefirsttrialwillbetakenastheresultinScienceWorld.
Data Generation. In total, we generate 2,436, 4,064 and 37,885 pairs of data for Webshop,
ScienceWorld and Game of 24, respectively. Sampled synthesized data sample can be seen in
Fig.5,Fig.6andFig.7. WeprovidethesampledpromptweusefordatagenerationfromFig.8to
Fig.11. InFig.8,weshowanexamplehowweprompttheLLMtogeneratelanguageinstructionfor
ScienceWorld.InFig.9,weshowhowwerefinethelanguageinstructiontorefinetheinstructiongoal.
InFig.10andFig.11,weshowtheprompthowtheLLMagentsynthesizespositiveandnegative
trajectories,respectively.
20

<!-- Page 21 -->

PublishedasaconferencepaperatICLR2025

### TrainingDataExampleforWebshop

TaskInstruction: Ineed2long-lastingbluetoothradiospeakerunitsforasoundbarwith
4ohmimpedanceand6wpower,andpricelowerthan50.00dollars.
PositiveExample:
Thought: ...
Action: ...
CurrentScreenshot: ...
Observation: ...
Thought: TheoptionB09STMXYR5matchestherequiredcharacteristics. Ishouldselectit.
Action: click[B09STMXYR5]

### CurrentScreenshot:


### Back to Search Instruction:

I need 2 long-lasting bluetoothradio speaker units for asoundbar with 4ohm impedance and
< Prev 6w power, and price lower than 50.00 dollars
JUSTQIJUN 2pcs 1.5 Inch Bluetooth Radio Speaker Unit
4 Ohm 6W Sound Bar Horn 18 Core 45mm Music

### Portable Loudspeaker Rubber Edge Compatible with

AltavocesBookshelf Speakers (Color : 40mm 4 ohm 6W)
Price: $28.36
Rating: N.A.

### Description Features Reviews Buy Now

Observation: Instruction: [SEP]ineed2long-lastingbluetoothradiospeakerunitsfora
soundbarwith4ohmimpedanceand6wpower,andpricelowerthan50.00dollars[SEP]
BacktoSearch[SEP]<Prev[SEP]JUSTQIJUN2pcs1.5InchBluetoothRadioSpeaker
Unit4Ohm6WSoundBarHorn18Core45mmMusicPortableLoudspeakerRubberEdge
Compatible with Altavoces Bookshelf Speakers (Color : 40mm 4 ohm 6W) [SEP] Price:
$28.36[SEP]Rating: N.A.[SEP]Description[SEP]Features[SEP]Reviews[SEP]Buy

### Now

Thought: Ishouldclickonthe’BuyNow’buttontoproceedwiththepurchase.
Action: click[buynow]
NegativeExample:
Thought: ...
Action: ...
CurrentScreenshot: ...
Observation: ...
Thought: IthinkIshouldclickontheproductIneed,whichisB09SWKXBY5,sinceit
matchestherequirementsof4ohmimpedanceand6wpowerandthepriceislowerthan50.00
dollars.
Action: click[B09SWKXBY5]

### CurrentScreenshot:


### Back to Search Instruction:

I need 2 long-lasting bluetoothradio speaker units for a soundbar with 4ohm impedance and
< Prev 6w power, and price lower than 50.00 dollars
JUSTQIJUN 2pcs Full Range 2 Inch Speaker 15W DIY

### Soundbar Boombox Unit Portable Radio 10W 20w 4

Ohm Speaker HiFi Bluetooth Speakers 55mm Bookshelf
Speakers (Color : 4 ohm 20W)
Price: $42.66
Rating: N.A.
Description Features Reviews Buy Now

### Color: 4 ohm 10w 4 ohm 15w 4 ohm 20w

Observation: Instruction: [SEP]ineed2long-lastingbluetoothradiospeakerunitsfora
soundbarwith4ohmimpedanceand6wpower,andpricelowerthan50.00dollars[SEP]
BacktoSearch[SEP]<Prev[SEP]color[SEP]4ohm10w[SEP]4ohm15w[SEP]4ohm
20w [SEP] JUSTQIJUN 2pcs Full Range 2 Inch Speaker 15W DIY Soundbar Boombox
21

<!-- Page 22 -->


### PublishedasaconferencepaperatICLR2025

UnitPortableRadio10W20w4OhmSpeakerHiFiBluetoothSpeakers55mmBookshelf
Speakers(Color: 4ohm20W)[SEP]Price: $42.66[SEP]Rating: N.A.[SEP]Description
[SEP]Features[SEP]Reviews[SEP]BuyNow
Thought: IthinkIshouldclickonthe’BuyNow’buttontopurchasetheproduct.

### Action: click[buynow]

Figure5: TrainingDataExampleforWebshop.

### TrainingDataExampleforScienceWorld

Task Instruction: You are a helpful assistant to do some scientific experiments in an
environment. In the environment, there are several rooms: kitchen, foundry, workshop,
bathroom,outside,livingroom,bedroom,greenhouse,artstudio,hallwayYoushouldexplore
theenvironmentandfindtheitemsyouneedtocompletetheexperiment. Youcanteleportto
anyroominonestep. Allcontainersintheenvironmenthavealreadybeenopened,youcan
directlygetitemsfromthecontainers.
Theavailableactionsare:
openOBJ:openacontainer
closeOBJ:closeacontainer
...
wait1: tasknoactionforastep
TaskDescription: Yourtaskistofindanon-livingthingintheenvironment. Focusonthejug
inthegreenhouse. Whenyouaredone,movethejugtothegreenboxinthekitchen.

### PositiveExample:


### Action: lookaround

Observation:Thisroomiscalledthehallway. Init,yousee:
theagent,asubstancecalledair,apicture

### Youalsosee:

Adoortotheartstudio(thatisopen),Adoortothebedroom(thatisopen),Adoortothe
greenhouse(thatisopen),Adoortothekitchen(thatisopen),Adoortothelivingroom(that
isopen),Adoortotheworkshop(thatisopen)

### Action: teleporttothegreenhouse

Observation: Youteleporttothegreenhouse.

### Action: lookaround


### Observation: Thisroomiscalledthegreenhouse. Init,yousee:

theagent,asubstancecalledair,aadultbee,aadultbee,aadultbee,aadultbee,abeehive.
Thebeehivedoorisopen. Inthebeehiveis: aadultbee. aflowerpot2(containingapeach
treeintheadultstage,soil),aflowerpot4(containingasubstancecalledwater),aflowerpot
5(containingasubstancecalledwater),aflowerpot6(containingabananatreeintheadult
stage,soil),aflowerpot7(containingaappletreeintheadultstage,soil),ajug(containing
nothing),ashovel,asink,whichisturnedoff. Inthesinkis: nothing.

### Youalsosee:

Adoortothehallway(thatisopen),Adoortotheoutside(thatisopen)

### Action: focusonthejug

Observation: Youfocusonthejug.

### NegativeExample:


### Action: lookaround

Observation:Thisroomiscalledthehallway. Init,yousee:
theagent,asubstancecalledair,apicture

### Youalsosee:

Adoortotheartstudio(thatisopen),Adoortothebedroom(thatisopen),Adoortothe
greenhouse(thatisopen),Adoortothekitchen(thatisopen),Adoortothelivingroom(that
isopen),Adoortotheworkshop(thatisopen)

### Action: teleporttothegreenhouse

Observation: Youteleporttothegreenhouse.
22

<!-- Page 23 -->

PublishedasaconferencepaperatICLR2025

### Action: connectpaintingtokitchen

Observation: terminal1onpaintingisnowconnectedtoterminal1onkitchen

### Action: connectagenttobathtub

Observation: Noknownactionmatchesthatinput.
Figure6: TrainingDataExampleforScienceWorld.

### TrainingDataExampleforGameof24

TaskInstruction: YouareastartagentandgeneratedataforGame24. Game24requires
userstousenumbersandbasicarithmeticoperations(+-*/)toobtain24.
Youtaskistogenerateanewinput(4digitalnumber)forGame24.
1. eachnewinputnumbershouldbeintherangeof1to13.

## Peoplecanusenumbersandbasicarithmeticoperations(+-*/)toobtain24. Ateachstep,

peopleareonlyallowedtochoosetwooftheremainingnumberstoobtainanewnumber.
Herearethefew-shotexamples.
3. sincethereisonlyfournumberinputandtheintermediatestepsshouldonlybethree.

### Input: 121084


### PositiveExample:

Steps: 10-8=2(left: 2412)
12/2=6(left: 46)
6*4=24(left: 24)
Answer: (12/(10-8))*4=24

### NegativeExample:

Steps: 10-12=-2(left: -248)
8/4=2(left: -22)
-2*2=4(left: 4)

### Answer: ((10-12)*(8/4))=4

Figure7: TrainingDataExampleforGameof24.

### InstructionGenerationPromptforScienceWorld

Task Instruction: You are a helpful assistant to do some scientific experiments in an
environment.
In the environment, there are several rooms: kitchen, foundry, workshop, bathroom,
outside,livingroom,bedroom,greenhouse,artstudio,andhallway.
Theavailableactionsare:
openOBJ:openacontainer
...
You will be given a dialogue between you (assistant) and a human user. You need
togeneratethetaskdescriptionafterunderstandingthedialoguegiventoyou. Inorderto
helpyoubettergeneratethetaskdescription,Iwillgiveyouanexamplebelow.
In this example, a human user gives a Task Description at first. Then you work as
anassistantandtalkwithusertofinishthetaskstepbystepusingtheavailableactionsabove.
ThoughtandActionareyourreasoningandtheactionsyoutakeateachstep. Observationis
providedbythehumanuser;itisanobservationofthesurroundingenvironmentafteryou
haveexecutedtheaction. Intheend,youneedtorestoretheTaskDescriptionbasedonthe
23

<!-- Page 24 -->

PublishedasaconferencepaperatICLR2025
wholedialogue.
Example:

### User

TaskDescription

### Assistant

Thought: Ineedtofindmaterialstocreategreenpaint,whicharelikelytobefoundinanart
studio.
Action: lookaround

### User

Observation: Thisroomiscalledthebedroom. Init,yousee:
...

### User

Observation: Blueandyellowpaintmixtoproducegreenpaint.

### Assistant

Thought: The task is to create green paint and then focus on it. Now that the green
paintismade,Ishouldconcentrateonthefinalproduct.

### Action: focusongreenpaint

Task Description: Your task is to use chemistry to create green paint. When you
aredone,focusonthegreenpaint.
Hereisthetaskyouneedtodo:
...
You should generate the Task Description following the format like examples below
andgenerateitbasedonthedialogueabovewithoutanyotherwords.

### Examples:

Your task is to boil ice cream. For compounds without a boiling point, combusting the
substanceisalsoacceptable. First,focusonthesubstance. Then,takeactionsthatwillcause
ittochangeitsstateofmatter.
Yourtaskistousechemistrytocreatevioletpaint. Whenyouaredone,focusontheviolet
paint.
Yourtaskistofinda(n)livingthing. First,focusonthething. Then,moveittotheredboxin
thebathroom.

### TaskDescription:

Figure8: InstructionGenerationPromptforScienceWorld.

### InstructionRefinementPromptforScienceWorld

Task Instruction: You are a helpful assistant to do some scientific experiments in an
environment.
Intheenvironment,thereareseveralrooms: kitchen,foundry,workshop,bathroom,outside,
livingroom,bedroom,greenhouse,artstudio,andhallway.
Theavailableactionsare:
openOBJ:openacontainer
...
You will be given a task description and a corresponding trajectory. The task description concludes what you have done in this trajectory. You need to elaborate this
descriptionbasedonthisenvironmentbyaddingmoredetails.
24

<!-- Page 25 -->

PublishedasaconferencepaperatICLR2025

### Example:

TaskDescription: Yourtaskistogrowanapple. Youcanfindseedsinthekitchen. You
shouldfocusonthegrownapple.
CorrespondingTrajectory:
lookaround
Thisroomiscalledthehallway. Init,yousee:
...
opendoortokitchen
Thedoorisalreadyopen.
gotokitchen
Youmovetothekitchen.
...
Refined Task Description: Your task is to grow an apple. This will require growingseveralplants,andthembeingcrosspollinatedtoproducefruit. Seedscanbefoundinthe
kitchen. Tocompletethetask,focusonthegrownapple.
Here is the task description you need to refine, and the corresponding trajectory is
alsoprovided:
...

### RefinedTaskDescription:

Figure9: InstructionRefinementPromptforScienceWorld.

### PositiveTrajectorySynthesisPromptforScienceWorld

Task Instruction: You are a helpful assistant to do some scientific experiments in an
environment.
In the environment, there are several rooms: kitchen, foundry, workshop, bathroom,
outside,livingroom,bedroom,greenhouse,artstudio,andhallway.
Theavailableactionsare:
openOBJ:openacontainer
...
Based on this environment, you need to randomly propose a Task Description, which
concludeswhatyouhavedoneinthisenvironment.

### Herearesomeexamples:

Yourtaskistousechemistrytocreategreenpaint. Whenyouaredone,focusonthegreen
paint.
Yourtaskistodeterminewhethertallplantheightisadominantorrecessivetraitinthepea
plant. Ifthetraitisdominant,focusontheredbox. Ifthetraitisrecessive,focusonthegreen
box.
...
Once you obtain the Task Description, you need to navigate through the environment to
completetheinstructionandgenerateatrajectory.

### Example:

TaskDescription: Yourtaskistousechemistrytocreategreenpaint. Whenyouaredone,
focusonthegreenpaint.
25

<!-- Page 26 -->

PublishedasaconferencepaperatICLR2025

### Trajectory:

Thought: Ineedtofindmaterialstocreategreenpaint,whicharelikelytobefoundinanart
studio.
Action: lookaround
...

### GeneratedTrajectory:

Figure10: PositiveTrajectoriesSynthesisPromptforScienceWorld.

### NegativeTrajectorySynthesisPromptforScienceWorld

Task Instruction: You are a helpful assistant to do some scientific experiments in an
environment.
In the environment, there are several rooms: kitchen, foundry, workshop, bathroom,
outside,livingroom,bedroom,greenhouse,artstudio,andhallway.
Theavailableactionsare:
openOBJ:openacontainer
...
You will be given a task description and a corresponding trajectory. Based on them,
youneedtogenerateanegativesamplethatissimilartothecorrecttrajectorybutdifferent
fromit. Thegeneratedtrajectoryshouldnotmeetallrequirementsofthetaskdescription.
Moreover,thegeneratedtrajectoryshouldsatisfyallrequirementsoftheenvironment.

### Example:

TaskDescription: Yourtaskistofocusonthelifestagesoftheappleplant,startingfrom
earliesttolatest. Theplantsarelocatedoutside.
PositiveTrajectory:
lookaround
Thisroomiscalledthehallway. Init,yousee:
...
opendoortooutside
Thedoorisalreadyopen
...
NegativeTrajectory:
lookaround
Thisroomiscalledthehallway. Init,yousee:
...
opendoortokitchen
Thedoorisalreadyopen.
gotokitchen
Youmovetothekitchen.
...
Hereisthetaskyouneedtodo:
...
NegativeTrajectory:
26

<!-- Page 27 -->


### PublishedasaconferencepaperatICLR2025

Figure11: NegativeTrajectoriesSynthesisPromptforScienceWorld.
RewardModelTrainingDetails. Thedetailedhyperparametersweuseforrewardmodelduring
training and inference are shown in Table 14. We employ identical hyperparameters for reward
modelsofdifferentenvironments. ForWebshop,weusecheckpointof1100stepsinARMAP-B,and
checkpointof1200stepsinARMAP-RandARMAP-M.
Name ScienceWorld Webshop Gameof24
lorar 64
loraalpha 16
loradropout 0.0
loratargetmodules q_proj,k_proj,v_proj,o_proj,gate_proj,up_proj,down_proj
epochs 10 3 10
batchsize 8 1 4
batchsizeperdevice 1 1 1
gradientaccumulationsteps 16 4 16
learningrate 1e-5 2e-5 1e-5
warmupratio 0.2 0.1 0.25
checkpointsteps 160 1100,1200 1500
temperature 0.0 0.0 0.0
Table14: Detailedhyperparametersusedinrewardmodel.
ImplementationDetailsofAblationbaselines. ForSFT,weuseallpositiveexamplesfromthe
rewardmodeltrainingasthetrainingdata. Thetrainingobjectiveistoenablethemodeltopredictthe
outputoftheLLMinthepositiveexamples.
Forusingfew-shotpromptingtoguidetheLLMstopredicttherewardofhistoricaltrajectories,we
usethefollowingformatofthefew-shotprompt:
Few-shotPromptforLLMsDirectlyServingasScienceWorldRewardModel
Task Instruction: You are an autonomous intelligent agent tasked with evaluating the
trajectories of the past experience. You will be given the history of a past experience
in which you were placed in an environment and given a task to complete. These
tasks will be accomplished through the use of specific actions. Now you are trying to
evaluate the performance on a past task. You will be given the objective of the task, the
historyofinteractionincludingtheobservationsyouhadandtheactionsyouissued, and
the status of the task. Your goal is to think about the strategy and provided path to produceascorerangingfrom0to1tomeasurewhethertheobjectiveofthetaskhasbeenreached.
Hereare2examples:

### Example1:

Human: You are a helpful assistant to do some scientific experiment in an environment. Intheenvironment,thereareseveralrooms: kitchen,foundry,workshop,bathroom,
outside, living room, bedroom, greenhouse, art studio, hallway. You should explore the
environmentandfindtheitemsyouneedtocompletetheexperiment. Youcanteleporttoany
roominonestep. Allcontainersintheenvironmenthavealreadybeenopened, youcan
directlygetitemsfromthecontainers. Theavailableactionsare: openOBJ:openacontainer,
closeOBJ:closeacontainer,activateOBJ:activateadevice,deactivateOBJ:deactivatea
device, connectOBJtoOBJ:connectelectricalcomponents, disconnectOBJ:disconnect
electrical components, use OBJ [on OBJ]: use a device/item, look around: describe the
27

<!-- Page 28 -->


### PublishedasaconferencepaperatICLR2025

currentroom,examineOBJ:describeanobjectindetail,lookatOBJ:describeacontainer’s
contents,readOBJ:readanoteorbook,moveOBJtoOBJ:moveanobjecttoacontainer,
pick up OBJ: move an object to the inventory, pour OBJ into OBJ: pour a liquid into a
container,mixOBJ:chemicallymixacontainer,teleporttoLOC:teleporttoaspecificroom,
focusonOBJ:signalintentonataskobject,wait: tasknoactionfor10steps,wait1: taskno
actionforastep
TaskDescription: Yourtaskistofinda(n)non-livingthing. First,focusonthething. Then,
moveittothepurpleboxinthelivingroom. PleaseonlyoutputoneThoughtandoneAction.
Theavailableactionsare: openOBJ:openacontainer,closeOBJ:closeacontainer,activate
OBJ:activateadevice,deactivateOBJ:deactivateadevice,connectOBJtoOBJ:connect
electricalcomponents,disconnectOBJ:disconnectelectricalcomponents,useOBJ[onOBJ]:
useadevice/item,lookaround: describethecurrentroom,examineOBJ:describeanobject
indetail,lookatOBJ:describeacontainer’scontents,readOBJ:readanoteorbook,move
OBJtoOBJ:moveanobjecttoacontainer,pickupOBJ:moveanobjecttotheinventory,
pourOBJintoOBJ:pouraliquidintoacontainer, mixOBJ:chemicallymixacontainer,
teleporttoLOC:teleporttoaspecificroom, focusonOBJ:signalintentonataskobject,
wait: tasknoactionfor10steps,wait1: tasknoactionforastep. Pleasestrictlyfollowthe
formatoftheactions.
Assistant: Thought: Ineedtofindanon-livingthing,whichcouldbeanobjectinanyroom,
soIshouldstartbylookingaroundthecurrentroom. Action: lookaround
Human:Observation:Thisroomiscalledthebathroom. Init,yousee:theagent,asubstance
calledair,abathtub,whichisturnedoff. Inthebathtubis: nothing. adrawing,aglasscup
(containingnothing),asink,whichisturnedoff. Inthesinkis: nothing. atoilet. Inthetoilet
is: Adrain, whichisopen, asubstancecalledwater. Youalsosee: Adoortothekitchen
(thatisopen). PleaseonlyoutputoneThoughtandoneAction. Theavailableactionsare:
openOBJ:openacontainer,closeOBJ:closeacontainer,activateOBJ:activateadevice,
deactivateOBJ:deactivateadevice,connectOBJtoOBJ:connectelectricalcomponents,
disconnectOBJ:disconnectelectricalcomponents, useOBJ[onOBJ]:useadevice/item,
lookaround: describethecurrentroom,examineOBJ:describeanobjectindetail,lookat
OBJ: describe a container’s contents, read OBJ: read a note or book, move OBJ to OBJ:
moveanobjecttoacontainer,pickupOBJ:moveanobjecttotheinventory,pourOBJinto
OBJ:pouraliquidintoacontainer,mixOBJ:chemicallymixacontainer,teleporttoLOC:
teleporttoaspecificroom,focusonOBJ:signalintentonataskobject,wait: tasknoaction
for10steps,wait1: tasknoactionforastep. Pleasestrictlyfollowtheformatoftheactions.
Assistant: Thought: Theglasscupinthebathroomisanon-livingthing,soIshouldfocus
onit. Action: focusonglasscup.
...
Assistant: Thought: I’vefoundthepurplebox,andnowIneedtomovetheglasscupintoit.
Action: moveglasscuptopurplebox.
Human: Observation: Noknownactionmatchesthatinput.
Human: Pleaseevaluatewhetheryoucompletethe’TaskDescription’ornot.
Followingyourdefinitions,thetaskcompletionscoreis<0.750>
Example2: ...

### Nowisyourturn:

Figure12: Few-shotPromptforLLMsDirectlyServingasScienceWorldRewardModel.

## A.4 Morequalitativeresults.

WeshowmorequalitativeresultsofourARMAPinFig.13andFig.14. Basedontheexamples,we
canseethattheautomaticrewardmodelsinourpipelinecandistinguishgoodtrajectoriesfrombad
onesandguideLLMstogeneratebettertrajectoriestofinishthetasks.
28

<!-- Page 29 -->


### PublishedasaconferencepaperatICLR2025


### QualitativeVisualizationforScienceWorld

TaskDescription: TaskDescription: Yourtaskistofinda(n)non-livingthing. First,focus
onthething. Then,moveittotheorangeboxinthelivingroom.

### TrajectoryA:

Observation: Youteleporttothelivingroom.
Thought: NowthatI’minthelivingroom,Ishouldlookaroundtofindanon-livingthing
thatIcanmovetotheorangebox. Action: lookaround

### Observation: Thisroomiscalledthelivingroom. Init,yousee:

theagent,asubstancecalledair,achair. Onthechairis: nothing. acouch. Onthecouchis: a
whitepillow. afingerpaintingaorangebox(containingnothing)atable. Onthetableis:
nothing.
Youalsosee: Adoortothehallway(thatisopen).
Thought: Iseeseveralobjectsinthelivingroom,butIneedtofindanon-livingthingthatI
canmovetotheorangebox. Action: examinewhitepillow
ARMAPAborted

### TrajectoryB:


### Observation: Thisroomiscalledtheworkshop. Init,yousee:

theagent, asubstancecalledair, atable. Onthetableis: abattery, abluewire, aorange
lightbulb,whichisoff,aredlightbulb,whichisoff,aredwire,aswitch,whichisoff,a
yellowlightbulb,whichisoff,ayellowwire. aultralowtemperaturefreezer. Theultralow
temperaturefreezerdoorisopen. Intheultralowtemperaturefreezeris: nothing. Youalso
see:

### Adoortothehallway(thatisopen)

Thought: Iseeseveralobjectsintheworkshopthatcouldbeconsiderednon-livingthings,
such as the battery, blue wire, or light bulbs. I should focus on one of these objects to
completethetask. Action: focusonbattery
Observation:Youfocusonthebattery.
Thought: NowthatI’vefocusedonthebattery,Ineedtomoveittotheorangeboxinthe
livingroom. Action: teleporttolivingroom
Observation:Youteleporttothelivingroom.
Thought: NowthatI’minthelivingroom,Ishouldlookaroundtofindtheorangeboxand
movethebatteryintoit. Action: lookaround

### Observation: Thisroomiscalledthelivingroom. Init,yousee:

theagent,asubstancecalledair,achair. Onthechairis: nothing. acouch. Onthecouchis: a
whitepillow. afingerpaintingaorangebox(containingnothing)atable. Onthetableis:
nothing.

### Youalsosee: Adoortothehallway(thatisopen)

Thought: I’vefoundtheorangeboxinthelivingroom,andnowIcanmovethebatteryinto
it. Action: movebatterytoorangebox

### ARMAPSelected

Figure 13: Qualitative Visualization for ScienceWorld. Based on the comparison of the two
trajectories,itisevidentthatthefinalactionoftrajectoryBbringstheresultingstateclosertothetask
objective. Therefore,ourmodelidentifiestrajectoryBasthesuperioroption.
29

<!-- Page 30 -->

PublishedasaconferencepaperatICLR2025
QualitativeVisualizationforGameof24

### InputA:25811 InputB:2369


### TrajectoryA1: TrajectoryB1:

Steps: 8*2=16(left: 51116) Steps: 9-3=6(left: 266)
11+5=16(left: 1616) 6+6=12(left: 212)
16+16=32(not24,notvalid) 2*12=24(left: 24)
11-5=6(left: 268) Answer: 2*(6+(9-3))=24
8/2=4(left: 46) ARMAPSelected
4*6=24(left: 24)
Answer: (8/2)*(11-5)=24

### ARMAPSelected

TrajectoryA2: TrajectoryB2:

### Steps: Steps:

8-5=3(left: 2311) 9-3=6(left: 266)
11-3=8(left: 28) 6-2=4(left: 46)
2*8=16(left: 16) 6*4=24(left: 24)
16+8=24(left: 24) Answer: (6*(9-3))=24
Answer: (((8-5)-8)*2)+8=24 ARMAPAborted

### ARMAPAborted

Figure14: QualitativeVisualizationforGameof24. TrajectoryAandTrajectoryBcorrespondto
inputAandinputBrespectively. ResultsshowthatourARMAPcanaccuratelypickoutthecorrect
trajectory.

## A.5 Failurecaseanalysis

Inthissection,weinvestigatethecommonfailurecasesofourframework,aimingtoprovidedata
pointsandinsightsforfutureresearch.
Themostcommonerroroccurswhentherearemultiplerestrictionsintheinstruction,thereward
modeloverlookssomeofthesekeyconditions. ArepresentativeexampleisillustratedinFig.15,
themodelfocusesonpriceandsizebutignoresthedetailsabout’Fluoride’hiddenintheproduct
description.
Anothercommonfailuremodeoccurswhencommonsenseknowledgeisinvolved. Asdemonstrated
inFig.16,theagentwastaskedwithbuyingablackoutshadebutfailedtochooseboththecolor
andthesize. While,ineverydaylife,sizeisgenerallymoreimportant,therewardmodelprioritized
colorinstead. InFig.17,therewardmodelcannotassessthelifespanofdragonfliesandchipmunks
becauseitlacksthenecessarybiologicalknowledge.
Discussion. Theanalysisoffailuremodeshighlightsthesignificantpotentialofourframework. To
improveitsperformance,weproposetwopossiblestrategiesforimprovementsinrewardmodeling:
(a)ConstructingDatawithFocusonComplexandDetailedConditions: enhancingthedatasetto
include scenarios with higher complexity and more nuanced conditions will help the framework
betterhandleintricatesituationsandedgecases. (b)InterveninginRewardScoringwithExternal
Knowledge: incorporatingexternalknowledgebycombiningapromptedLargeLanguageModel
withthetrainedrewardmodel. ThisapproachallowstheLLM’sgeneralizedknowledgetocalibrate
therewardscoresinacontrollablemanner,improvingtheoverallaccuracyandrobustnessofthe
rewardmodel.
30

<!-- Page 31 -->


### PublishedasaconferencepaperatICLR2025

Instruction: I need a fluoride free toothpaste for fresh breath. I will need a pack of 4 in 3.5 ounce
size, and price lower than 50.00 dollars.
Action1: search[fluoride free ... Action1: search[toothpaste fresh ...
toothpaste 3.5 oz pack of 4 price < breath fluoride free 4 pack 3.5 oz
50.00] price < 50.00]

## B07L2L64Xl B08Dr4Sdlj B08Dqs3T87 B07L2Ln685

Action2: click[b07l2l64xl] P $1 ri 2 c . e 6 : 9 Action2: click[B08DQS3T87] P $2 ri 3 c . e 2 : 7

### Size: Size:

SprinJene Natural Fluoride Free Toothpaste 3.5 ounce (pack of 2) SprinJene Natural Toothpaste with Fluoride 3.5 ounce (pack of 2)
for Clean and Strong Teeth 3.5 ounce (pack of 4) for Cavity Protection of Teeth 3.5 ounce (pack of 4)
Action3: click[pack of 4] P $1 ri 2 c . e 6 : 9 Action3: click[pack of 4] Price:

### Size: $23.27

Action4: click[Buy Now] 3 3 . . 5 5 o o u u n n c c e e ( ( p p a a c c k k o o f f 2 4 ) ) Action4: click[Buy Now] S iz 3 e .5 : ounce (pack of 2)
3.5 ounce (pack of 4)
GT Reward = 1.0 GT Reward = 0.75

### ARMAP Aborted ARMAP Selected

Figure15: FailureExamplefromWebshop. Therewardmodelignorescertainkeyconditionsin
thetaskinstruction.
Instruction: I want to find white blackout shades that are 66 inches in width and 66 inches in
height. they need to be easy to install, and price lower than 90.00 dollars
Action1: search[white blackout ... Action1: search[white blackout ...
shades 66 x 66 easy install price < shades 66x66 easy install price <
90.00] 90.00]

## B097Kxcwp7 B09Gp34Tdr B08Gftcmqh B08R8H4R4B

Action2: click[B097KXCWP7] P $7 ri 8 c . e 4 : 9 Action2: click[B08GFTCMQH] P $8 ri 9 c . e 9 : 9

### Size: Color:

Missing color! Co 6 l 6 o " r w : x 66"h … Missing size! Black White …

### Black White …

Action3: click[66"w x 66"h] P $7 ri 8 c . e 4 : 9 Action3: click[white] Price:

### Size: $89.99

Action4: click[Buy Now] Co 6 l 6 o " r w : x 66"h … Action4: click[Buy Now] C o B l l o a r c : k White …

### Black White …

GT Reward = 0.8 GT Reward = 0.4

### ARMAP Aborted ARMAP Selected

Figure 16: Failure Example from Webshop. The reward model misjudged the importance of
differentconditions,suchasthesizeandcolorinthiscase.
31

<!-- Page 32 -->


### PublishedasaconferencepaperatICLR2025

Instruction: Your task is to find the animal with the longest life span, then the shortest life span.
First, focus on the animal with the longest life span. Then, focus on the animal with the shortest life
span. The animals are in the 'outside' location.

### Action1: look around Action1: look around

Observation1: This room is called the art studio. In it, you Observation1: This room is called the art studio. In it, you
see: the agent, a substance called air, a large cupboard. see: the agent, a substance called air, a large cupboard.

### Action2: teleport to outside Action2: teleport to outside

Observation2: You teleport to the outside. Observation2: You teleport to the outside.

### Action3: look around Action3: look around

Observation3: Here you see: … an axe, a baby chipmunk, Observation3: Here you see: … an axe, a baby chipmunk,
a baby dragonfly … a parrot egg a baby dragonfly … a parrot egg
Action4: focus on parrot egg (Thought: A parrot is a type of bird, and Action4: focus on parrot egg (Thought: A parrot is a type of bird, and
birds are known to live for many years. The life span of a parrot can be quite birds are known to live for many years. The life span of a parrot can be quite
long, often exceeding 30 years in some species. ) long, often exceeding 30 years in some species. )
Observation4: You focus on the parrot egg. Observation4: You focus on the parrot egg.
Action5: focus on baby dragonfly (Thought: Dragonflies are Action5: focus on baby chipmunk (Thought: I need to focus on
known to have a relatively short life span, typically ranging from a few weeks the animal with the shortest life span, which is the baby chipmunk.)
to a few months.) Observation5: You focus on the baby chipmunk .
Observation5: You focus on the baby dragonfly.
GT Reward = 1.0 GT Reward = 0.83

### ARMAP Aborted ARMAP Selected

Figure17: FailureExamplefromScienceWorld. Rewardmodelshaveproblemswhencommonsenseknowledgeisinvolved,suchastheinabilitytodeterminetheshortestlifespan.
32

## Tables

**Table (Page 4):**

| PositiveTrajectories |
|---|
| NegativeTrajectories |


**Table (Page 4):**

|  |
|---|
|  |


**Table (Page 4):**

| Search … Search ... ... search[…jeans…] B00K1E04EC B000N8RZKW Straight Leg Jeans, Regular-Fit Jean, $16.44 to $43.61 $43.16 to $219.21 |
|---|
| Price:$16.44 to $43.61 click[B00K1E04EC] Size: 40wx32l 40wx34l… |
| Price:$16.44 to $43.61 click[40wx34l] Size: 40wx32l 40wx34l… |


**Table (Page 10):**

| I'm looking for furniture to make my living room and Search … Search Default PolicyModel dinning room so nice, and price lower than 300 dollars. search[furniture] Back to S . e . a . rch ... Back to Sea . r . c . h ... search[furniture] click[back to search] B09LSBCVQT B07D54V8HT search[living room dining ... ... click[B09LSBCVQT] ReadingRoomSet,RestroomMirror, room furniture] $957.34 $2488.95 click[B09MQFMCL8] B09MQFMCL8 B08J9WPMJ8 Table Set for 4 Price: Table Set for 6 Price: click[Buy Now] Buy Now click[Buy Now] $259.99 $853.29 Automatic I need a blue women coat, and price lower than 80 dollars. Search … Search RewardModel search[blue women Back to Search search[blue sherpa wool Back to Search ... ... ... ... coat price < 80.00] sweatshirt price < 80.00] click[B09LRVC4K2] click[B09LRVC4K2] B09LRVC4K2 B08J9WPMJ8 B09LRVC4K2 B08J9WPMJ8 click[blue] Price: $9.19 to $10.96 click[large] Price: $9.19 to $10.96 click[Buy Now] Color: blue purple black click[Buy Now] Size: large medium |  |
|---|---|
|  | Back to Search search[blue sherpa wool ... ... sweatshirt price < 80.00] click[B09LRVC4K2] B09LRVC4K2 B08J9WPMJ8 |
|  | click[large] Price: $9.19 to $10.96 click[Buy Now] Size: large medium |


**Table (Page 10):**

| Action1: search[1 pound certified ... organic sea salt shaker triple blend flakes price < 30.00] B0007SMLUM B0713TMD19 | Action1: search[organic sea salt ... shaker triple blend flakes price < 30.00] B0007SMLUM B07SH4ZFY9 | Action1: search[organic sea salt ... shaker triple blend flakes 1 pound price < 30.00] B0007SMLUM B01GGWDB8S |
|---|---|---|
|  | Action2: click[b07sh4zfy9] Price: Wrong Size! $13.15 |  |
|  |  | Action3: click[1 pound (pack of 1)] Price: $13.15 Action4: click[triple blend flakes] Size: 1 lb 1 oz Flavor: Action5: click[Buy Now] triple blend flakes |
|  | Action3: click[back to search] ... Action4: search[organic … flakes 1 pound price < 30.00] B0007SMLUMB01GGWDB8S |  |
|  | Action5: click[B0007SMLUM] |  |
|  | Action6: click[1 pound (pack of 1)] P $1 ri 3 c . e 1 : 5 Action7: click[triple blend flakes] S i z 1 e l : b 1 oz Action8: click[Buy Now] F l a t v ri o p r l : e blend flakes |  |
| Action9: click[back to search] Search … Search |  |  |


**Table (Page 21):**

| Back to Search |
|---|
| < Prev |


**Table (Page 21):**

| Back to Search |
|---|
| < Prev |


**Table (Page 31):**

| Instruction: I need a fluoride free toothpaste for fresh breath. I will need a pack of 4 in 3.5 ounce size, and price lower than 50.00 dollars. Action1: search[fluoride free ... Action1: search[toothpaste fresh ... toothpaste 3.5 oz pack of 4 price < breath fluoride free 4 pack 3.5 oz 50.00] price < 50.00] B07L2L64XL B08DR4SDLJ B08DQS3T87 B07L2LN685 Action2: click[b07l2l64xl] P $1 ri 2 c . e 6 : 9 Action2: click[B08DQS3T87] P $2 ri 3 c . e 2 : 7 Size: Size: SprinJene Natural Fluoride Free Toothpaste 3.5 ounce (pack of 2) SprinJene Natural Toothpaste with Fluoride 3.5 ounce (pack of 2) for Clean and Strong Teeth 3.5 ounce (pack of 4) for Cavity Protection of Teeth 3.5 ounce (pack of 4) Action3: click[pack of 4] P $1 ri 2 c . e 6 : 9 Action3: click[pack of 4] Price: Size: $23.27 Action4: click[Buy Now] 3 3 . . 5 5 o o u u n n c c e e ( ( p p a a c c k k o o f f 2 4 ) ) Action4: click[Buy Now] S iz 3 e .5 : ounce (pack of 2) 3.5 ounce (pack of 4) GT Reward = 1.0 GT Reward = 0.75 ARMAP Aborted ARMAP Selected Figure15: FailureExamplefromWebshop. Therewardmodelignorescertainkeyconditionsin thetaskinstruction. |
|---|
|  |
