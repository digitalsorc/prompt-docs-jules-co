---
title: "KoMA Knowledge Multi Agent Framework"
original_file: "./KoMA_Knowledge_Multi_Agent_Framework.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["prompt-engineering", "llm", "rag", "chain-of-thought", "react"]
keywords: ["agent", "driving", "agents", "memory", "multi", "scenarios", "module", "llm", "scenario", "action"]
summary: "<!-- Page 1 -->

1
KoMA: Knowledge-driven Multi-agent Framework
for Autonomous Driving with Large Language

### Models

Kemou Jiang1, Xuan Cai1, Zhiyong Cui*1, Aoyong Li1, Yilong Ren1, Haiyang Yu1, Hao Yang2,

### Daocheng Fu3, Licheng Wen3, and Pinlong Cai*3

1State Key Laboratory of Intelligent Transportation Systems, School of Transportation Science and Engineering,
Beihang University, 100191, Beijing, P.R.China. 2Department of Civil and Systems Engineering, Johns Hopkins University, Baltimor"
related_documents: []
---

# KoMA Knowledge Multi Agent Framework

<!-- Page 1 -->

1
KoMA: Knowledge-driven Multi-agent Framework
for Autonomous Driving with Large Language

### Models

Kemou Jiang1, Xuan Cai1, Zhiyong Cui*1, Aoyong Li1, Yilong Ren1, Haiyang Yu1, Hao Yang2,

### Daocheng Fu3, Licheng Wen3, and Pinlong Cai*3

1State Key Laboratory of Intelligent Transportation Systems, School of Transportation Science and Engineering,
Beihang University, 100191, Beijing, P.R.China.
2Department of Civil and Systems Engineering, Johns Hopkins University, Baltimore, USA
3Shanghai Artificial Intelligence Laboratory, 200232, Shanghai, P.R.China.
Abstract—Large language models (LLMs) as autonomous predominantlybeendata-driven[1]–[4],relyingheavilyonthe
agents offer a novel avenue for tackling real-world challenges collection and analysis of vast datasets to train algorithms cathrough a knowledge-driven manner. These LLM-enhanced
pableofcomplexdrivingscenarios.Whilethesemethodshave
methodologies excel in generalization and interpretability. Howmadesignificantstrides,theyareoftenhamperedbychallenges
ever, the complexity of driving tasks often necessitates the
collaboration of multiple, heterogeneous agents, underscoring such as dataset bias [5], overfitting [6], [7], and a lack of
the need for such LLM-driven agents to engage in cooperative interpretability [8], [9], which can limit their effectiveness in
knowledgesharingandcognitivesynergy.Despitethepromiseof novel or unforeseen circumstances.

### LLMs,currentapplicationspredominantlycenteraroundsingle-


### In response to these challenges, there has been a paradigm

agent scenarios, which limits their scope in the face of intricate,
shift towards knowledge-driven approaches in autonomous
interconnected tasks. To broaden the horizons of knowledgedriven strategies and bolster the generalization capabilities of driving[10],[11].Thisshiftisunderpinnedbytherecognition
autonomous agents, we propose the KoMA framework con- thathumandriverscanrelyontheirrichexperienceandknowlsisting of the multi-agent interaction, the multi-step planning, edgecoupledwithlogicalreasoningabilitytomakereasonable
the shared-memory, and the ranking-based reflection modules
judgments and decisions when facing new scenarios. Large
to enhance multi-agents’ decision-making in complex driving

### Language Models (LLMs) are trained on large amounts of

scenarios. Based on the framework’s generated text descriptions
of driving scenarios, the multi-agent interaction module enables textdatatoprocess,understand,andgeneratenaturallanguage
LLM agents to analyze and infer the intentions of surrounding text. The LLM has a broad range of basic human knowledge
vehicles based on scene information, akin to human cognition. and superior reasoning abilities, making it a powerful tool in
The multi-step planning module enables LLM agents to analyze
thisnewknowledge-drivenparadigm[12],[13].Thesemodels,
and obtain final action decisions layer by layer to ensure consisexemplified by the likes of GPT3.5 and GPT4 [13] , have
tent goals for short-term action decisions. The shared memory
module can accumulate collective experience to make superior demonstrated unparalleled proficiency in understanding and
decisions, and the ranking-based reflection module can evaluate generatingnaturallanguagetextandcanquicklyadapttonew
and improve agent behavior with the aim of enhancing driving application scenarios with a small number of prompt words,
safety and efficiency. The KoMA framework not only enhances
suggestingtheirpotentialtoserveasagentswithinautonomous
therobustnessandadaptabilityofautonomousdrivingagentsbut
systems [14]–[16].
also significantly elevates their generalization capabilities across
diverse scenarios. Empirical results demonstrate the superiority Recent studies on LLM-based autonomous driving agents
of our approach over traditional methods, particularly in its have primarily been tested in simplistic scenarios, such as
ability to handle complex, unpredictable driving environments highwaymainroaddrivingscenariosandcirculartrackdriving
withoutextensiveretraining.ProjectPage:https://jkmhhh.github.
scenarios[10],[17],[18].Inthesecontexts,theimpactofother
io/KoMA/.
vehicles on the agent vehicle is negligible, placing the agent
Index Terms—Autonomous Driving, Large Language Models, vehicle in a safe and stable environment. However, real-world

### Multi agents, Shared Memory, Multi-Step Planning, Chain of

driving scenarios are complex and time-variant, reflected by
Thought.
two major aspects: 1) the diversity of driving scenarios, such
as ramp merging and roundabouts, increases the likelihood

## I. Introduction

of conflicts between vehicles due to their complexity. This

### The quest for autonomous driving system has long been at

diversity requires the vehicle agents to make reasonable and
theforefrontoftechnologicalinnovation,aimingtorevolutionrapid plans to ensure driving safety and efficiency. 2) The
ize transportation through improved safety, efficiency, and ac- second factor is the diversity of drivers determined by the
cessibility.Traditionalapproachestoautonomousdrivinghave
drivers’ unique charateristics and reflected by their driving
behaviors.Thisdiversitycontributestotheincreasedtemporal
*CorrespondingAuthor
variability ofscenarios. Therefore, autonomousdriving agents
4202
luJ
91
]IA.sc[
1v93241.7042:viXra

<!-- Page 2 -->

2
Information Update Single

### Recall Agent

Reflect Reason

### System

Environment Action Driver Agent Retrieve Memory
Information Driver Agent Update Multi-

### Interaction Agent

Environment Driver Agent Memory System

### Action Retrieve

Fig.1. Theknowledge-drivenparadigmforsingledrivingagentsystemandmultipledrivingagentssystem.Singleknowledge-drivenagentsystemincluding
aninteractiveenvironment,adriveragentwithrecall,reasoningandreflectionabilities,alongwithanindependentmemorymodule.Multipleknowledge-driven
drivingagentsystemshaveanadditionalinteractionmoduleforcommunicationandexchangeamongtheagents.
based on LLMs need further verification of their intelligence when faced with more complex driving scenarios, the former,
levels in complex and time-variant scenarios, especially when which makes decisions for the next frame solely based on the
those agents with different objectives influence with each currentscenedescription,ispronetofallingintolocaloptimal
other. solutions, lacking foresight, thereby making it difficult to
achieve a goal that requires continuous action across multiple

### In multiagent driving scenarios, vehicle agents based on

frames. In the face of more dynamic driving scenarios, the

### LLMs must account for both the impact of fixed driver model

latter, which plans multiple-step action decisions at once, is
vehicles and the influence of variable LLM-based agent vehisusceptible to plan failure due to sudden changes in the scene
clesontheirowndrivingdecisions.Byadoptingthisapproach,
conditions, thus failing to complete the scene goals smoothly.
the agents can more accurately simulate the complexities of

### To address this, the KoMA framework introduces a multi-step

real-world driving conditions, thereby advancing the frontier
reasoning module that achieves the final single-step action
of knowledge-driven agent technology. The well-established
decisionthroughathree-tieredreasoningprocessofgoal-planknowledge-drivenframework,DiLu[10],havesummarizedthe
action, ensuring the continuity of action decisions.
knowledge-driven paradigm of autonomous driving systems,
which comprises three components: 1) an environment with In the knowledge-driven autonomous driving setting, the
which the agent can interact; 2) a driving agent capable of currentreflectionmoduleisprimarilyactivatedafteracollision
memory, reasoning, and reflection; 3) a memory component occurs [10], [11], but this raises two issues: (1) In complex
to retain experience. As shown in Fig. 1, the knowledge- scenarios, the cause of an accident is often not the last action
driven paradigm can still be used within the multi-agent decision, but rather a critical decision made earlier in a long
framework after expanding the interactions among multiple sequence of decisions. Identifying the key erroneous decision
agents. However, due to the increased complexity of the and reflecting on it for correction is a critical challenge.
scenarios in both time and space, further expansion and im- (2) In reality, drivers need to ensure not only the safety
provement of some modules are required to better apply them of driving but also its efficiency. An agent that completely
in complex scenarios. To address these limitations, this study sacrifices efficiency for safety is impractical for real-world
introduce a knowledge-driven autonomous driving framework scenarios. Therefore, the KoMA framework proposes a score-
KoMAthatincorporatesmultipleagentsempoweredbyLLMs. based reflection module that includes assessments of safety
It encapsulates five integral modules: Environment, Multi- andefficiency.Itexpandstheconditionsforinitiatingreflection
agent Interaction, Multi-step Planning, Shared Memory, and to situations where there is a sudden drop or extremely low
Ranking-based Reflection. score, allowing for timely correction of erroneous decisions
and enhancing the quality of the memory fragments stored in
Atpresent,thereasoningmoduleofLLMsismainlydivided
the memory module.
into two approaches: making single-step decisions directly
for each frame [10] and formulating a plan that includes a Thememorymoduleservesasarepositoryforthehistorical
sequence of multiple-step decisions at once [19]. However, driving experiences of an agent, capable of retrieving similar

<!-- Page 3 -->

3
scenario experiences to assist the LLM-empowered agent in discussed by Xi et al., signified a pivotal transition towards
makingactiondecisions.Inearlyreinforcementlearningmulti- more integrated and autonomous systems [23]. Gao et al.
agent systems, each agent was trained independently [20]. introducedAssistGPT,whichemployedamethodoflinguistic
However, this may lead to the collective intelligence being reasoning called Plan, Do, Check, and Learn (PEIL). This
limited by an individual agent with poor training outcomes. methodology enhanced the integration of LLMs with vari-
Benefiting from the parameter sharing mechanism in rein- ous tools, pushing the boundaries of their application [24].
forcement learning [21], the KoMA framework incorporates Similarly, Shen et al. proposed HuggingGPT, a framework
a shared memory module, allowing all agents to share a designedtoleverageLLMsforconnectingdisparateAImodels
single vector database. This enables the sharing of driving within the machine learning community to address complex
experiences among agents, thereby enhancing the training AI tasks [25]. Furthermore, ViperGPT, as presented by Suris
speed and effectiveness of collective intelligence. et al., showcased a novel approach by utilizing an API to
In summary, this study proposes KoMA, a comprehensive accessandcomposemodulesthroughPythoncodegeneration,
framework that harnesses the power of LLMs to facilitate thereby offering solutions for an array of queries [26]. A
advanceddecision-makingincomplex,multi-agentdrivingen- significant evolution in the deployment of LLMs as agents
vironments. The KoMA framework is designed to address the was the transition from traditional, data-driven paradigms to
limitations of current single-agent approaches by integrating knowledge-driven methodologies. Li et al. emphasized this
several key components that work in concert to enhance the shift, advocating for a move towards active, cognition-based
capabilities of autonomous agents. Through a series of exper- understanding that leveraged the extensive general knowledge
iments and implementations, we demonstrate the feasibility and reasoning capabilities of LLMs [11]. This approach not
of our approach and its advantages over traditional methods, onlyenhancedtheagent’sabilitytointeractwithandcompreparticularly in terms of generalization, adaptability, and the hend the world, but also enabled the system to become more
ability to handle novel scenarios without extensive retraining. autonomous and intelligent with relevant domain knowledge
The contribution of this paper is listed as follows: and reasoning learning ability.
1) To the best of knowledge, we are the first to propose a
knowledge-driven autonomous driving framework with

### B. Multi agent with LLM

multiple LLM-empowered agents, where those driving
agents implicitly interact through estimating the inten- TheintegrationofLLMsinmulti-agentsystemshasbecome
tions of surrounding vehicles. an emerging research field for improving collective intelli-
2) We propose a three-layer structure of GPA (goal- gence and collaboration in various fields. The exploration
planning-action) for analyzing tasks step by step in of LLM-powered multi-agent systems revealed the future of
complex autonomous driving scenarios, ensuring the collaborative intelligence, where the cooperation of multiple
coherence of long-term decision-making. independent agents could enhance problem-solving capabil-
3) The framework also integrating safety and efficiency ities. Handler et al. proposed a multi-dimensional taxonindicators into the reflection module to accurately mea- omy to tackle the difficulties in categorize and understand
sure and locate erroneous decisions, thereby expanding the architectural complexities posed by LLM-powered multithe scope of reflection and enhancing the module’s agent systems which aimed at accomplishing complex tasks,
effectiveness. goals, or problems with the cognitive synergy of multiple
4) A memory sharing module is proposed to enable mul- autonomousLLM-poweredagents[27].Liuetal.proposedthe
tiple agents quickly accumulate experience of different Dynamic LLM-Agent Network (DyLAN), a novel approach
scenario at the same time and ensure that the memory for fostering LLM-agent collaboration on intricate tasks such
and learning procedures of multiple agents are consis- as reasoning and code generation. DyLAN created a stratetent. Experiments have demonstrated that this shared gic assembly of agents that communicate within a dynamic
memory module effectively enhances the generalization interaction architecture tailored to the specific requirements
capability of the agents. of the task query [28]. This model exemplified the potential
of context-aware collaboration among LLM-powered agents,
pushing the boundaries of collective problem-solving capabil-

## Ii. Literaturereview

ities. Chen et al. introduced AGENTVERSE, a multi-agent

### A. LLM as Agent

framework designed to orchestrate a collaborative group of
In the burgeoning field of artificial intelligence, the emer- expertagents,creatingasystemwhosecapabilitiesexceedthe
gence and integration of LLMs as agents have marked a sum of its parts. AGENTVERSE enhanced the efficiency and
significant pivot from conventional rule-based systems to effectiveness of task accomplishment, showcasing the power
knowledge-driven approaches. The LLMs demonstrate re- of agent collaboration in complex problem-solving scenarios
markableabilitiestoperformtasksbasedonuserpromptsand [29]. Gong et al. presented Mindagent, an infrastructure that
rapidly adapt to new scenarios through in-context learning. leveragesLLMsforinteractivemulti-agentplanning.Thissys-
Zhou et al. highlighted the intrinsic properties of LLMs tem not only demonstrated the in-context learning capabilities
that facilitate this adaptability, laying the groundwork for of LLMs in multi-agent planning but also offered several
their application as complex agents [22]. The shift towarded promptingtechniquestobolstertheirplanningproficiency.Itis
employing LLMs as the “brain” or controller of agents, as proposedforevaluatingplanningandcoordinationcapabilities

<!-- Page 4 -->

4
in the context of gaming interaction [30]. Zhang et al. devel- ory mechanism for task-related information organization and
oped the Cooperative Embodied Language Agent (CoELA), an expert-oriented black-box tuning to enhance performance
anagentcapableofplanning,communicating,andcooperating without the need for fine-tuning the LLMs. The application
with others to efficientlyaccomplish long-horizon tasks. Pow- of Co-Pilot in path tracking control and trajectory planning
ered by GPT4, CoELA surpassed traditional planning-based tasks showcased its versatility and effectiveness [18]. Shao et
methods, demonstrating emergent effective communication al.presentedLMDrive,aninnovativelanguage-guided,end-tostrategies. This advance highlighted the potential for LLM to end,closed-loopframeworkforautonomousdriving.Uniquely
conduct cooperative behavior and perform complex tasks in integrating multi-modal sensor data with natural language
multiple agents [31]. instructions, LMDrive facilitated interaction with humans and
navigation software in realistic settings [33].
C. LLM for Autonomous Driving The exploration of LLMs within autonomous driving systems unveiled a promising horizon where vehicles not only
The integration of LLMs into autonomous driving systems
mimicked human driving capabilities but also engaged in
signified a transformative leap towards embedding humancomplex decision-making and problem-solving tasks with
likeintelligenceforenhanceddecision-makingandinteraction
an unprecedented level of intelligence and adaptability. The
capabilities.Maoetal.emphasizedtheroleofLLMsascognireviewed literature underscored the shift towards leveraging
tive agents in autonomous driving systems, highlighting their
human-likeintelligenceandknowledge-drivenmethodologies,
capacity to integrate human-like intelligence across various
illustrating the potential of LLMs to redefine autonomous
functions such as perception, prediction, and planning [32].
driving.However, current research on LLM-empowered au-

### ThisfoundationalapproachunderscoredthepotentialofLLMs

tonomous driving agents mainly focused on simple scenarios
to mimic human cognitive processes. Li et al. discussed the
lacking conflicts. We try to further explore and test the scope
employment of LLMs as foundation models for autonomous
of knowledge driven capabilities in scenarios with conflicts,
driving, capitalizing on their rich repository of human driving
in order to fill the gap in this field.
experience and common sense. These models actively understood,interactedwith,acquiredknowledgefrom,andreasoned
about driving scenarios [11]. Wen et al. introduced DiLu, III. METHODOLOGY
a framework combining reasoning and reflection modules to

### A. Overview

facilitatedecision-makingbasedoncommon-senseknowledge
while enabling continuous system evolution. DiLu’s extensive We introduce a knowledge-driven autonomous driving
experiments demonstrated its superior generalization ability framework KoMA that incorporates multiple agents empowover reinforcement learning-based methods, evidencing the ered by LLMs, comprising five integral modules: Environcapability of LLMs to accumulate experience and adaptively ment, Multi-agent Interaction, Multi-step Planning, Shared
improve [10]. Wang et al. proposed Co-Pilot, a universal Memory, and Ranking-based Reflection. Within this frameframework that incorporates LLMs as a vehicle’s “Co-Pilot”, work, all agents operate on an equal and independent basis,
adept at fulfilling specific driving tasks with human inten- as illustrated in Fig. 2.
tions in mind. This framework not only defined a workflow The environment module provides driving scenarios for the
for human-vehicle interaction but also introduced a mem- driving agent, which can be either a simulation environment

### Scenario Description Memory-based Enhancement

Environment Multi-step Planning Evaluation- Shared-Memory

### Reflection

Multi-step Planning Evaluation- E

### D Reflection M

E Interaction Goal Replanning B

## C E


### O Analyze D

D Intention Plan New action D

## E I

R Action Summarizing N

## G


### Evaluation-

Multi-step Planning

### Reflection

Environment Vehicle Vehicle Agent Driven by LLM Success Experience Revised Experience
Fig.2. Knowledge-drivenautonomousdrivingframeworkKoMAthatincorporatesmultipleagentsempoweredbyLLMs.KoMAconsistsoffivecoremodules:
theenvironmentmodule,themulti-stepplanningmodule,theinteractionmodule,theranking-basedreflectionmodule,andthesharedmemorymodule.

<!-- Page 5 -->

5
or a real-world scenario. It is mainly responsible for provid- Algorithm 1 Autonomous Driving with Multi-agent LLMs
ing a text description of the corresponding scene for each
Input:Simulationscenariosce,simulationdurationtimeT,
autonomous driving agent before making decisions.
current time t, decision interval time ∆t, reflection agent

### The multi-agent interaction module further processes the

RA, driving agent DA, driving agent list DA list, sharedtextual information returned by the environment module, primemory M
marily enables the LLMs to analyze the behavior of other
Initialize: t = 0, score list SL = [], decision list DL = [],
vehiclesinthescenariolikeahuman,infertheirintentions,and
document doc = [], plan = None
supportsubsequentactiondecisionswithrelevantinformation.
while t < T do
Chain of Thought (CoT) is a technique used in LLMs that
for DA in DA list :
promotescomplexreasoningandproblem-solvingcapabilities.
\\ Get the scenario description
The core idea behind this method is to break down a complex
sce des = sce.describe(DA)
problem into a series of smaller steps, known as intermediate
\\ Retrive similar experience from shared-memory
reasoning steps. This enabless the model to incrementally
few-shot = M.retriveMemory(sce des)
construct a complete solution by addressing each step in a
\\ Driving agent making action decision
logical and sequential manner [34]–[36]. The multi-step planaction, plan = DA.reason(sce des, few-shot,
ning module is an application of the CoT technique to guide
plan)
LLMmakethefinalactiondecision.TheLLMsfirstlyanalyze

### DL.append(action)

thegoalaccordingtothecurrentscenario,thenformulatesthe
\\ Execute the action decision in environment
plan, and finally makes an action decision. This structured
score, done = env.step(action)
planning process enables the LLM agent to maintain a clear

### SL.append(score)

goal for its actions and more effectively pursue long-term
doc.append([DA, sce des, plan, action, score])
goals. Based on the textual description of the current scene
t = t + ∆t
and the experiential playback of historical similar scenes, the
\\ Check whether the scene is finished
LLM ultimately selects an action through continuous analysis
if done:
andthenreturnstheactiondecisiontotheenvironmentmodule
break
for execution.
\\ Reflection agent correct the wrong action
The shared memory module utilizes a shared vector
corrected decision = RA.reflect(SL, DL)
database to store the successful driving experiences of all
\\ Update the memory
agents. Before each agent makes a decision, the module

### M.update(corrected decision)

retrievesanalogousdescriptionsrelevanttotheagent’scurrent

### Output: Document doc, updated shared-memory M

situation and then provides these experiences to the agent,
helpingtoformulateaninformedactiondecision.Thismodule
allows each agent to train, accumulate experience, and interaction decisions. After receiving the text description from the
act with the environment, continuously enhancing decisionenvironment module, the agent preliminarily processes the
making effectiveness.
informationusingthemulti-agentinteractionmodule,analyzes
To ensure the quality of experiences in the shared memory
andguessestheintentionsofothervehiclesbeforeproceeding
module, this framework introduces a ranking-based reflection
to the multi-step planning module with this information.
module that evaluates each driving decision after execution
based on efficiency and safety. After a scenario has been

### C. Multi-step Planning

concluded, the framework reviews the outcomes of those
decisions, especially those with low scores or collisions. Only The Multi-step Planning Module serves as the cornerstone
those experiences where decisions were corrected with high for LLMs’ reasoning within KoMA. The process is illustrated
scores are retained. The procedure is outlined in Algorithm 1. in Fig 3. Employing the Goal-Plan-Action methodology, this
More details about the Multi-agent Interaction, Multi-step module merges inputs from the current scenario description
Planning, Shared Memory, and Ranking-based Reflection withsimilarhistoricalexperiencestodeterminethebestcourse
modules will be elaborated in the following sections. of action, encompassing the following stages.

### Clarifygoalsbasedonthecurrentscenario:Drivershave

different goals to achieve in different scenarios. For example,

### B. Multi-agent Interaction Module

thegoalofanormalvehiclerunningonthehighwayistodrive
In KoMA, agents do not interact directly with each other; efficiently and quickly under the premise of ensuring safety.
instead, agents infer their intentions just like real human The main goal of vehicles on the freeway ramp is to merge
drivers by analyzing the history and current state information into the main road as soon as possible within a certain period
of other vehicles. For example, when the LLM-driven agent of time, so the driver’s goal is mainly related to the scenarios.
senses a vehicle on its left suddenly accelerating, it further Based on this, we divide the goals within the scenario into
analyzesandreasonsaboutthis,guessesthevehicle’sintention two categories: special scenario goals and general scenario
to overtake, and then analyzes these guesses along with goals. Special scenario goals refer to the tasks that need to
its own plan to determine if adjustments to its short-term be completed within a certain time in the scenario, such as
plan are needed. Ultimately, the agent aims to make rational ramp merging, intersection passage, etc. The general scenario

<!-- Page 6 -->

6

### Scenario Description Chained Decision Making

Y hi o g u h w ar a e y d a r n iv d i n h g av o e n r e th a e c h e e n d t r t a h n e c s e e r c a ti m on p w of h t e h re e My goal is to merge onto the highway safely in time
you can merge onto the highway. The end Clarify the goal
of the ramp is 115.50 meters ahead of you, Step 1: Brainstorming plans:
Driving task you must turn left to merge onto the highway - Accelerate to increase our speed and then merge ahead of Vehicle 96.
before reaching the end of ramp. - Maintain current speed (IDLE) and wait for a safe opportunity to merge,
possibly behind Vehicle 96 or Vehicle 488.
You are driving on a road with 3 lanes, and S - A te c p ce 2 le : r a E ti v n a g l t u o a in t c in re g a s t e h o e u r p s r p o e p ed o s a e n d d t p he la n n m s e : rge ahead of Vehicle 96: This
you are currently driving in the rightmost plan could allow us to take advantage of the small speed difference to merge
lane. Your current position is `(231.00, ahead of Vehicle 96. However, it increases the risk of getting too close to the
8.00)`, speed is 21.51 m/s, acceleration is maximum safe speed limit. Safety: 6, Efficiency: 8.
Ego vehicle 0.00 m/s^2. - m M erg ai e n : t T a h in is i n p g la c n u i r s r s e a n f t e r s p a e s e i d t r ( e I d D uc L e E s ) t h a e n d ri s w k a o i f t i e n x g c e f e o d r i n a g s t a h f e e s o a p fe p o sp rt e u e n d i l t i y m t i o t
and allows us to find a safe gap to merge, either behind Vehicle 96 or Vehicle
T yo h u e , r a e n a d r e b e o l t o h w e r is v t e h h e i i c r l b e a s s d ic r i in v f i o n r g m a a r t o io u n n : d LLM Make a plan 4 S 8 t 8 e . p S a 3 f : e t R y: a 9 n , k E i f n fic g i e t n h c e y : p 7 l . ans:
- Vehicle `96` is driving on the lane to your G op i p v o e r n t u th n e it y e v to a l m ua e t r i g o e n s is , t r h a e n k p e l d a n h i t g o h m er a d in u t e a t i o n i c t u s r h r i e g n h t e s r p s e a e fe d t y a n s d co w re a . it for a safe
left and is parallel to you. The center Step 4: Choosing the driving plan:
position of it is `(235.71, 4.00)`, length is 5.0 The chosen plan is to maintain our current speed (IDLE) and wait for a safe
meters, speed is 21.79 m/s, acceleration is opportunity to merge onto the highway, likely behind Vehicle 96 or Vehicle
0.00 m/s^2. 488, depending on the traffic flow and the development of a safe gap.
- Vehicle `488` is driving on the lane to your
Surrounding left and is ahead of you. The center position Considering the distance to the end of the ramp (115.50 meters) and our
Traffic Status o sp f e it e i d s ` i ( s 2 2 5 1 3. . 8 3 3 8 , 4 m .0 /s 0 , ) ` a , c le c n e g le th r a is ti 5 o . n 0 i m s e 0 te .0 rs 0 , Choose an c to u r p r r e e n p t a s r p e e e fo d r , m a s a a in fe t a m in e i r n g g e . o T u h r i c s u a r c r t e io n n t s e p n e s e u d re s s e e th m a s t w th e e d sa o f e n s o t t o r p is ti k o n a
m/s^2. Similar Experiences action c tr o a l f l f i i s c i o f n lo b w y f c o h r a a n s g a i f n e g m la e n rg es e p o r p e p m or a t t u u n r i e t l y y . and gives us time to assess the
Fig.3. Acaseofmulti-stepplanningmodulereasoningprocess.Themulti-stepplanningmodulereferstoathree-levelmulti-stepreasoningofgoal-plan-action,
which analyzes and breaks down the scene target tasks step by step to ensure the consistency of the purpose of the decision-making before and after the
action.Besides,italsoreferstothefour-stepprocessofplangeneration,planevaluation,plansorting,andplanselectionwhenformulatingaplan,toselect
thefinalplanthatbestfitsthedrivingcharacteristicsoftheLLM,ensuringthefeasibilityandpersonalizationoftheplan.
goal is a long-term objective, such as maintaining safe and beneficial experiences. These archived experiences serve as
efficient driving. Each agent first sets its objectives based exemplarstoassistLLMsintheplanninganddecision-making
on the scenario description to inform planning and action processes. Each experience is segmented into four critical
decisions. elements: the scenario description, the planning process, the
Make a plan based on the goals: The planning process finaldecision,andtheevaluationscore.Thetextualdescription
involves the LLMs devising a strategy that connects identified of scenarios is converted into vectors, serving as keys for
goalswithfutureactions,ensuringcoherentactionsovertime. gaugingsimilaritywithinthememorymodule.Theconceptof
Initially, the LLMs checks for a pre-established plan. If no shared memory implies a unified memory module accessible
suchplanexists,theLLMsformulatesanewstrategytoguide toallagentsempoweredbyLLM,fosteringconsistencyofexfuture actions. The planning process unfolds as follows: perienceandperformance.Thisapproachmirrorstheprinciple
1) The LLMs brainstorm all workable and distinct plans of parameter sharing observed in reinforcement learning.
based on the current scenario and goal. Theprimaryaimofsharedmemoryistoquicklyaccumulate
2) For each of the proposed plans, the LLMs will evaluate experiences in different scenarios simultaneously. Using the
the potential of them, consider their pros and cons, repository of past experiences, new agents can learn from
implementation difficulty, potential challenges and then the collective wisdom and insights of their predecessors. This
assign safety, efficiency score from 0 to 10 to each shared memory module enables agents to perform tasks with
option based on these factors. anawarenessofpreviouslysuccessfulstrategiesandoutcomes.
3) Based on the evaluations and scenarios, rank the plans. Essentially,sharedmemoryservesasaconduitforknowledge
4) A singular plan is selected to guide driving decisions. transfer, ensuring that the collective learning of agents is
preserved and utilized to enhance future decision making.

### If there is a pre-existing plan, the LLM evaluates other

vehicles’ intentions from the multi-agent interaction module.
Iftheplanisdeemedinfeasible,itcraftanewplan;otherwise, E. Ranking-based Reflection
it maintains the existing plan.
The reflection module, operational at the termination of

### Choose an action according to the plan: It’s time for

each scenario, is designed to revise action decisions. These

### LLMsmakingreasonableandsafeactionchoicesbasedonthe

rectified decisions, along with successful experiences, are
current scene information and the plan. There are five actions
then integrated into the memory module. When the reflection
in the action space:turn-left, IDLE (remain in the current lane
module updates the reflection results to the shared memory
with current speed), turn-right, acceleration, and deceleration.
module, it can be considered that the agent has completed
The LLMs select an action based on inference.
one round of training. To differentiate the efficacy of each
action decision, the system incorporates safety indicators and

### D. Shared Memory

efficiency scores, assessing the vehicle’s state post-execution
The shared memory module is an integral component of of LLM-generated instructions. In the following, we delineate
KoMA, encapsulating a vector database designed to archive the criteria for these evaluations.

<!-- Page 7 -->

7

### Scenario description Scenario description

You are driving on a highway. You are driving on the entrance
You need to avoid colliding with ramp of the highway and your
merging vehicles. goal is to merge onto the highway
You are driving on a road with 3 safely.You are driving on a road
lanes, and you are currently with 3 lanes, and you are currently
driving in the second lane from driving in the rightmost lane. Your
the left. Your current position is current position is `(275.52, 8.00)`,
`(304.21, 4.00)`, speed is 15.20 speed is 24.19 m/s, acceleration is
m/s, acceleration is -0.35 m/s^2, 1.38 m/s^2, and lane position is
and lane position is 74.21 m ...... 45.52 m ......

### Vectorize Vectorize

and search and search

### Recall Similar Recall Similar

experience Highway Driving Ramp Merging experience

### Experience Experience

Shared Memory Constructed by Vector Database

### LLM Agent 1 LLM Agent 2

Fig. 4. Different agents retrieve relevant experiences of their respective scenarios from shared memory modules. The shared memory module is a vector
databasethataccumulatesdrivingexperiencefragmentsfromallagents.Thesefragmentsarevectorizedandthenstoredinthesamedatabase.Whenmaking
decisions,theagentretrievessimilardrivingexperiencesfromanalogousscenariosusingvectorsearch,therebyaidinginthedecision-makingprocess.
Safety evaluation criteria: Safety is quantified on a scale between the agent’s speed and the average speed of surroundfrom 0 to 10, using Time To Collision (TTC) to measure ve- ing vehicles. An agent vehicle that matches or exceeds the
hicularsafetypost-action.TheTTCabove3secondsindicates averagespeedofsurroundingvehiclesreceivesafullefficiency
optimal safety, earning the highest score of 10. Below 1.5 score of 10. If the agent’s speed is below the average, the
seconds, TTC indicates a critical safety risk, scoring 0 [37]– efficiencyscoreistheratiooftheagent’sspeedtotheaverage
[39]. For TTC values between 1.5 and 3 seconds, the safety speed, scaled to 10.
score linearly scales from 0 to 10.
(cid:40)
10, if V (t)>V (t)
20(TTC(t)−1.5),
if 1.5s<TTC(t)<3s
Efficiency
score
(t)= LLM Avg
 3 0, otherwise.
Safety (t)= 10, else if TTC(t)>3s
score
0, otherwise. Upon the conclusion of a scenario, the LLM undertakes an
analysis of the scoring list to pinpoint actions that deviated
Efficiency evaluation criteria:Efficiencyissimilarlyrated from expected outcomes and requires reflection. This process
onascalefrom0to10andusesspeedastheefficiencymetric. mandates the correction of previously unsafe decisions, fa-
Thismetricconsiderstheimpactofsurroundingvehiclespeeds cilitating a cycle of continuous enhancement in the agent’s
on the agent’s vehicle, measuring efficiency by the difference capabilities. The utilization of interpretable chain-of-thought

### High

Action Safety Efficiency score update #0
# 0 #1 #4
# 0 10 10
# 1
# 1 2.8 10
Reflection Agent
# 2 #2
# 2 4.4 8.9 Replanning
# 3 #3 update #3
# 3 6.7 8.2 New action
。
Low
。
# 4 8.1 6.3 score 。 Summarize #4

### Score List Memory

Fig. 5. The ranking-based reflection module evaluates decisions, identifies those with low scores, and corrects them. It then updates the shared memory
modulewiththeserefineddecisions,alongwiththehigh-scoringexperiences.

<!-- Page 8 -->

8
responses significantly aids in uncovering the root causes of
potentially hazardous scenarios.
In an effort to foster autonomous learning from past mistakes,ourmethodologyemploysthedetaileddescriptionofthe (a) Anexampleofinitializationscenario
driving scenario in which the erroneous decision was made,
alongsidethecorrespondingreasoningoutput,asinputsforthe
LLM. This approach prompts the LLM to elucidate the underlying reasons for the flawed decisions, thereby guiding the
(b) Afailurescenariowhereacollisionoccursonarampmerge
agent towards more accurate and safer future decisions. Additionally,theLLMistaskedwithdevisingstrategiestomitigate
therecurrenceofsimilarerrors,enhancingitsdecision-making
framework.Thisreflectiveprocessincorporatesrefinedreasoning and revised decisions learned from error correction into (c) Afailurescenariowheretherampmergeisnotcompletedintime
memory modules. This ensures the preservation of enhanced
knowledgeandunderliestheagent’sabilitytolearnadaptively
in a variety of driving environments.
(d) Asuccessfulscenarioforsafelycompletingrampmerges

## Iv. Experiments

Fig.6. Examplesofdifferentphasesinthetestingscenarios

### A. Experimental Settings

Simulation Environment: We leverage the “highway-env” the agent reaches the endpoint or collides with other vehicles,
as the simulation platform, which furnishes a realistic multi- it is considered as the end of the scenario. The reflection
vehicleinteractiveenvironment[40].Thisenvironmentpermits module will then update the shared-memory module. When
the customization of various parameters including vehicle the update is completed, the agent completes a round of
positioning, velocity, count, and lane specifics, offering a training in that scene. After every 20 rounds of training, 20
versatile setting for conducting our studies. The focal point randomlygeneratedscenariosareselectedandfixedfortesting
of our scenario selection is the on-ramp merging challenge the trained agents in KoMA.
withinahighwaycontext.Thisparticularscenariounderscores
the exigency of accomplishing merging objectives within a TABLEII
constrainedtimeframe,therebyservingasanaptrepresentation THEPARAMETERSOFTHEINITIALIZATIONSCENARIOS
of the agent’s decision-making acumen.

### Parameter Value

Large Language Model: GPT-4 [13] was mainly used Thelanecountofthehighwaymainroad 2
in experiments to verify the validity of the KoMA frame- Thelanecountoftheon-rampmergingroad 1

### Thelengthofon-rampmergingroad 120m

work. This model plays a pivotal role in both the Multi-step

### Theinitializationspeedofvehicles rangefrom20to25m/s

Planning and Rank-based Reflection modules of our architec-

### Thespacingofthespawnpoints 40m

ture, showcasing its versatility and advanced understanding Theinitiallocationnoise rangefrom-10to10m
capabilities. For the Memory module, integral to our frame- ThecountofLLMcontrolledvehicles 2

### Thecountofintelligentdrivermodelvehicles 5

work, we incorporate “Chroma” an open-source embedded

### Policyfrequency 2Hz

vector database. This choice is instrumental in facilitating
the conversion of scene descriptions into vectors, for which Baseline MARL-based model: The baseline MARL
we employ OpenAI’s “text-embeddings-ada-002” model. This method is “deep multi-agent reinforcement learning for highcomprehensive setup not only exemplifies the integration of way on-ramp merging in mixed traffic” [41], which develop
cutting-edge AI technologies but also highlights our innova- anefficientandscalableMARLframeworkthatcanbeusedin
tive approach towards enhancing autonomous driving systems dynamic traffic where the communication topology could be
throughnuancedunderstandingandreflection.TABLEIshows time-varying. We have adjusted the MARL parameter Policy
the parameters and components related to KoMA. frequency from 5Hz to 2Hz to maintain consistency with the

### Policy frequency during training in KoMA. Concurrently, we

TABLEI have adapted the MARL training scenarios to focus on the
THEPARAMETERSANDCOMPONENTSRELATEDTOKoMA two-lanehighwayon-rampmergingcontextandhaveinitiated
the training process accordingly.

### Parameter Value


### Simulationenvironment highway-env[40]

Largelanguagemodel GPT-4[13] B. Performance of the proposed framework

### Textembeddingmodel text-embeddings-ada-002

Vectordatabase Chroma In this section, we conducted comparative experiments on
KoMA and deep multi-agent reinforcement learning (MARL).
Testing Scenario: The testing scenario locates at an on- To maintain consistency with the test scenarios of the MARL
ramp entrance on the highway with two main lanes. The methods, we conducted comparative tests in scenarios where
scenarioincorporatestwoLLM-drivenagents,oneonthemain both the main road and the highway ramp are configured as
road and the other on the on-ramp, as shown in Fig 6. When single lanes.

<!-- Page 9 -->

9
Performance: In the untrained state, the success rate of the

### KoMA framework is 30%, while the success rate of MARL

reaches 45%. The success rate of MARL is slightly higher
thanthatoftheKoMAframework.Thisisbecausetheselected

### GPT4 model is a general LLM that has not been extensively

trained with corpora in the driving domain, resulting in a
less clear understanding of driving tasks. However, after 20
rounds of training and accumulating driving experience, the

### KoMA framework has achieved a success rate of 50%, which

is essentially on par with the 51% success rate achieved by
the MARL algorithm after 20,000 rounds of training. When
the KoMA framework has undergone 40 rounds of training,
it has already achieved a success rate of 70%, successfully
surpassing the 65% success rate achieved by the MARL
algorithmafter40,000roundsoftraining.Thisexperimentnot
only demonstrates the effectiveness of the KoMA framework Fig.8. Experimentalresultstestedintheinitialscenariowithdifferentmemory
in closed-loop learning within scenarios but also highlights modulesafter20and40roundsoftraining.
that,comparedtotraditionaldata-drivenmethods,knowledgedriven agents possess higher learning efficiency and better
The non-shared memory module exhibits poorer perfortraining outcomes.
manceduringtraining;after40roundsoftraining,thesuccess
rate is only 45%, which is worse than the performance of the
sharedmemorymoduleafterjust20roundsoftraining.Thisis

### C. The validation of the framework

partially because sharing a common memory module leads to
1) Shared Memory: In this section, an ablation study is a richer and more abundant vector database, allowing for the
conducted on the Shared Memory module. We have set up simultaneous accumulation of training effects from multiple
three different types of memory modules for comparative agents. After the vehicles driving on ramp merge onto the
testingtoverifythesuperiorityofthesharedmemorymodule. highway, they still need to travel on the main road for some
The first type is the no-memory module, which means that time, which requires the agent to have a certain amount of
no vector database is set up to accumulate and store histor- highway driving experience. However, most of the experience
ical experiences. The second type is the non-shared memory of agents on the ramp is confined to the ramp scenario, with
module, where each agent has its own vector database, and lessexperiencedrivingonthemainroad,whichrequiresmore
the accumulated experience fragments are not shared with training rounds. Therefore, the shared memory module not
other agents, only used to assist in their own action decisions. onlyeffectivelyenhancesthetrainingeffectivenessofmultiple
The third type is the shared memory module, where each agents, improvingcollective intelligence,but alsoensures that
agent shares a common vector database, and the experiences all agents are at the same level of intelligence, preventing the
accumulated by an agent can be called upon by other agents group’s performance from being adversely affected by poorly
to assist in their action decisions, thus achieving sharing. The trained agents.
testing results are shown in Fig. 8. 2) Multi-step Planning: In this section, we will compare
the training results of agents with and without the multi-step
planning module to verify the effectiveness of KoMA. The
agents under these two frameworks are both trained for 40
rounds.ThetestingresultsaredisplayedviaaboxplotinTable

### III.Itshowsthesuccessratesofagentsatthedifferenttraining

stages, including agents without training, agents trained with
20 rounds and agents trained with 40 rounds.

## Tableiii


## Thesuccessrateofexperimentalresultsintheinitial


## Scenariowasevaluatedusingdifferentframeworks,With


## Testingconductedafter0,20,And40Roundsoftraining.

Trainingepisodes DiLu KoMA
0 40% 30%
20 50% 50%
40 50% 70%

### We found that agents with multi-step planning modules

Fig. 7. The performance of KoMA after 0, 20, and 40 training episodes is
comparedwiththeperformanceofMARLafter0,20,000,and40,000training performed worse without training, with a success rate of
episodes,respectively. only 30%. However, during 20 rounds of training, the effect

<!-- Page 10 -->

10
Fig. 9. The average efficiency score and safety score of successful testing Fig. 10. The experimental results for different generalization scenarios are
scenariosafter40roundsoftraining. evaluated with and without the memory, which has been trained on a main
roadwaywithtwolanes.
was on par with that of agents without multi-step planning
modules, achieving a success rate of 50%. After 40 rounds of module.Wethentestedthismoduleinscenarioswithonemore
training, the agent with multi-step planning modules achieved or one less lane on the main roadway, at the same density. As
a success rate of 70%. This indicates that agents with multi- the memory module lacks content for these new scenarios,
step planning modules have better training effects and faster this setup tests the LLM agents’ ability to generalize. The
convergence in ramp merging scenarios. The Fig. 9 shows the resultsareshowninFig.10.Wefoundthattheshared-memory
averagescoreofsuccessfultestingscenariosafter40roundsof trained in the initial scenario still affects and yields good
training. Agents with multi-step planning modules have better resultswhengeneralizingtoscenarioswithvaryingmainroad
efficiency and safety scores, indicating that they can complete lanes, indicating superior generalization ability in knowledgescenario testing more safely and efficiently. This may be driven agents compared to traditional data-driven ones.
because the three-layer progressive reasoning thinking chain
2) Generalizing to roundabout scenarios: Continuing with
ofgoal-plan-actioncanbetterassisttheLLMinmakingaction
theuseofthesamememorymoduleasintheprevioussection,
decisions with consistent goals when completing urgent tasks
we shifted the scenario from ramp merging to roundabouts.
in complex and time-varying scenarios.When there is a clear

### OuraimwastotestwhethertheLLMagentscouldlearnfrom

short-term goal, action decisions become more purposeful,
previousscenariosandenhancetheirdecision-makingabilities
avoidingmeaninglessactiondecisionsofrepeatedacceleration
bygeneralizingtocompletelydifferentscenarios.Additionally,
and deceleration, which improves the efficiency of the agent.
this shift aimed to demonstrate the value of a shared memory
Meanwhile, the inspection part of the plan ensures that the
moduleinenhancingthegeneralizationcapabilitiesofmultiple
agent can timely reformulate the plan when the old plan is no
agents.
longer safe and feasible in time-varying scenarios, avoiding

### TheroundaboutscenariosetupisdepictedinFig.11.There

the continued execution of high-risk old plans and improving
isasinglelaneforeachofthefourentryandexitroadsofthe
the security of the agent.
roundabout. Within the roundabout itself, there is a two-lane
circular road. Roundabout scenarios can be mainly divided

### D. Generalization under different Scenarios

into three phases: 1. Roundabout entry phase: Merging into
Data-drivenagentsoftentendtooverfittotrainingscenarios, the roundabout from the entry road. 2. Roundabout internal
leading to poor generalization capabilities and limited appli- driving phase: Driving within the roundabout until approachcability [6], [7], [11]. Therefore, in this section, we conduct a ingthetargetexitroad.3.Roundaboutexitphase:Exitingfrom
seriesoftestsonthegeneralizationcapabilitiesofknowledge- the roundabout to the exit road and leaving the roundabout.
drivenagentswithintheframeworktoexaminewhetherLLMs There are four vehicles modeled as intelligent driver model
can learn knowledge from experiential fragments and apply it (IDM) on the western entry road of the roundabout, with
to different scenarios. theirdestinationbeingtheeasternexitroad.Theagentvehicle
1) Altering the number of lanes on the main roadway: controlledbytheLLMisonthesouthernentryroad,followed
Initially, we conducted tests with minor variations in scenario by an IDM environmental vehicle. There are a total of six
complexity by changing the number of lanes on the merging vehicles in the entire roundabout scenario, and their actual
main roadway. Despite these minor changes, these scenarios generation positions still follow the form of fixed coordinate
still pose challenges for data-driven agents in generalizing. points plus random fluctuations to reflect randomness. In this
We trained the LLM agents on scenarios with two-lane main scenario, the agent vehicle controlled by the LLM needs to
roadways and single-lane ramps. After training, we obtained safely merge into the roundabout from the southern entry and
an experience-rich vector database, known as the memory smoothly exit from the eastern side of the roundabout, which

<!-- Page 11 -->

11
(a) The first phase of the roundabout driving scenario: Gradually
approach the roundabout and observe the traffic conditions within it,
lookingfortherightmomenttoentertheroundabout.
Fig.12. Thegeneralizationabilityofthememory,trainedfor40episodesin
theinitialscenario,isspecificallytestedintheroundaboutscenario.
(b) Thesecondphaseoftheroundaboutdrivingscenario:Thevehicle E. Performance under different LLMs
successfully enters the roundabout and drives within it. The vehicle
needs to identify its exit within the roundabout and merge out in a In this section, we will employ various LLMs to verify
timelymanneratthedesignatedexit. the efficacy of KoMA framework. By comparing their performance during training, we aim to ascertain which model is
better suited for our KoMA framework.

## Tableiv


## Thesuccessrateofexperimentalresultswithdifferentllms


## After0,20,40Roundsoftraininginthekomaframework

episodes GPT3.5 GPT4 Llama3-8B Llama2-7B Qwen2-7B
0 20% 30% 25% 20% 25%
20 30% 50% 35% 25% 30%
(c) The third phase of the roundabout driving scenario: The vehicle 40 35% 70% 40% 35% 40%
successfully merges out from the exit and leaves the roundabout,
completingtheroundaboutscenario.

### Our research findings demonstrate that a range of Large

Fig.11. Illustrationsofthethreestagesoftheroundaboutscenario.
LanguageModels(LLMs),includingGPT3.5[42],GPT4[13],

### LLaMA2-7B [12], LLaMA3-8B [43], and QWEN2-7B [44],

can be effectively trained within the KoMA framework. This
is considered a successful completion of the scenario. If a trainingsignificantlyimprovestheirdecision-makingcapabilicollision occurs or the vehicle fails to exit from the eastern ties,therebyvalidatingtheframework’suniversalapplicability
sideoftheroundaboutintime,itisconsideredafailureofthe andeffectivenessacrossdifferentmodels.GPT-4performsbest
scenario. The result are shown in Fig. 12 within the KoMA framework, with better training outcomes
and faster convergence speed. GPT-3.5 underperforms within

### In the initial ramp merging scenario on a two-lane main


### KoMA, particularly in handling lengthy scenario texts. The

road, the success rate was 30% without prior training, and it
model’s difficulty in accurately capturing critical details, such
reached a 70% success rate after 40 rounds of training. An
as vehicle spacing and speed variations, often leads to the
agentwithoutanymemoryrepositoryachieveda60%success
exclusion of essential information during decision-making
rate in the roundabout scenario. When the memory repository
processes. This oversight can result in collisions involving
from40roundsoftrainingintheinitialrampmergingscenario
the agent vehicles, highlighting the need for enhanced model
was applied to the agent in the roundabout scenario, the
training and attention to detail recognition.
successrateincreasedto80%,demonstratingtheeffectiveness
of knowledge-driven generalization capabilities of the agent.
The reason for the roundabout scenario still having a 60%

## V. Conclusion

success rate without experience is mainly twofold: firstly,
because there is only one LLM controlling the agent in the The advent of LLMs as autonomous agents has marked a
scenario, which reduces the overall collision risk of the LLM significantshiftintheapproachtoknowledge-drivenproblemagent; secondly, because the roundabout scenario is simpler, solving, particularly within the autonomous driving sector.
with only longitudinal acceleration and deceleration control This study presents the KoMA framework, a comprehenbefore merging, without the need to consider lane-changing sive system designed to transcend the limitations of current
behavior. single-agent models by facilitating multi-agent collaboration,

<!-- Page 12 -->

12
shared knowledge, and cognitive synergy. The KoMA frame- [9] L.H.Gilpin,D.Bau,B.Z.Yuan,A.Bajwa,M.Specter,andL.Kagal,
work’s multi-faceted approach, integrating interaction, plan- “Explaining explanations: An overview of interpretability of machine
learning,” in IEEE 5th International Conference on data science and
ning,memory,andreflectionmodules,hasproveninstrumental
advancedanalytics. IEEE,2018,pp.80–89.
in enhancing decision-making in complex driving scenarios. [10] L.Wen,D.Fu,X.Li,X.Cai,M.Tao,P.Cai,M.Dou,B.Shi,L.He,
Our empirical evaluations have confirmed the KoMA frame- andY.Qiao,“Dilu:Aknowledge-drivenapproachtoautonomousdriving
with large language models,” in The Twelfth International Conference
work’s superiority over traditional methods, showcasing its
onLearningRepresentations.
robustness in unpredictable environments and its ability to [11] X.Li,Y.Bai,P.Cai,L.Wen,D.Fu,B.Zhang,X.Yang,X.Cai,T.Ma,
generalize across a wide array of driving situations without J. Guo et al., “Towards knowledge-driven autonomous driving,” arXiv
preprintarXiv:2312.04316,2023.
theneedforextensiveretraining.Theframework’ssuccesslies
[12] H. Touvron, T. Lavril, G. Izacard, X. Martinet, M.-A. Lachaux,
in its human-like cognition, where LLM agents can discern T. Lacroix, B. Rozie`re, N. Goyal, E. Hambro, F. Azhar et al.,
and respond to the intentions of surrounding vehicles, and “Llama:Openandefficientfoundationlanguagemodels,”arXivpreprint
arXiv:2302.13971,2023.
its layered planning ensures strategic consistency in action
[13] J.Achiam,S.Adler,S.Agarwal,L.Ahmad,I.Akkaya,F.L.Aleman,
decisions.
D. Almeida, J. Altenschmidt, S. Altman, S. Anadkat et al., “Gpt-4
The KoMA framework is a preliminary test of the po- technicalreport,”arXivpreprintarXiv:2303.08774,2023.
tential of LLMs in revolutionizing autonomous systems. It [14] C.H.Song,J.Wu,C.Washington,B.M.Sadler,W.-L.Chao,andY.Su,
“Llm-planner: Few-shot grounded planning for embodied agents with
opens a new frontier for research, suggesting that the future
largelanguagemodels,”inProceedingsoftheIEEE/CVFInternational
of autonomous driving lies in the seamless integration and ConferenceonComputerVision,2023,pp.2998–3009.
collaboration of multiple agents. As we continue to refine [15] J. Mai, J. Chen, G. Qian, M. Elhoseiny, B. Ghanem et al., “Llm as a
roboticbrain:Unifyingegocentricmemoryandcontrol,”2023.
and expand upon this framework, we envision a future where
[16] J.Pan,“Whatin-contextlearning“learns”in-context:Disentanglingtask
autonomousdrivingsystemsarenotonlyhighlyadaptableand recognitionandtasklearning,”Ph.D.dissertation,PrincetonUniversity,
safe but also capable of learning and improving continuously 2023.
[17] C. Cui, Y. Ma, X. Cao, W. Ye, and Z. Wang, “Drive as you speak:
from shared experiences and insights.
Enabling human-like interaction with large language models in autonomousvehicles,”inProceedingsoftheIEEE/CVFWinterConference
onApplicationsofComputerVision,2024,pp.902–909.

## Acknowledgments

[18] S. Wang, Y. Zhu, Z. Li, Y. Wang, L. Li, and Z. He, “Chatgpt as your
vehicle co-pilot: An initial attempt,” IEEE Transactions on Intelligent
This work was also partially supported by the Na-
Vehicles,2023.
tional Natural Science Foundation of China (project num- [19] C.Cui,Y.Ma,X.Cao,W.Ye,andZ.Wang,“Receive,reason,andreact:
ber: 52202378), Beijing Natural Science Foundation (project Driveasyousay,withlargelanguagemodelsinautonomousvehicles,”
IEEEIntelligentTransportationSystemsMagazine,2024.
number: L243008), the Open Research Project Program
[20] A. Tampuu, T. Matiisen, D. Kodelja, I. Kuzovkin, K. Korjus, J. Aru,
of the State Key Laboratory of Internet of Things J. Aru, and R. Vicente, “Multiagent cooperation and competition with
for Smart City (project number: SKL-IoTSC(UM)-2021- deep reinforcement learning,” PloS one, vol. 12, no. 4, p. e0172395,
2017.
2023/ORP/GA08/2022), and the Ministry of Transport of
[21] J.K.Gupta,M.Egorov,andM.Kochenderfer,“Cooperativemulti-agent
PRC Key Laboratory of Transport Industry of Comprehensive controlusingdeepreinforcementlearning,”inAutonomousAgentsand
Transportation Theory (Grant No. MTF2023002). MultiagentSystems:AAMAS2017Workshops,BestPapers,Sa˜oPaulo,
Brazil,May8-12,2017,RevisedSelectedPapers16. Springer,2017,
pp.66–83.
REFERENCES [22] A.Zhou,K.Yan,M.Shlapentokh-Rothman,H.Wang,andY.-X.Wang,
“Languageagenttreesearchunifiesreasoning,acting,andplanningin
[1] A.Amini,I.Gilitschenski,J.Phillips,J.Moseyko,R.Banerjee,S.Kara- language models,” in Forty-first International Conference on Machine
man, and D. Rus, “Learning robust control policies for end-to-end Learning.
autonomous driving from data-driven simulation,” IEEE Robotics and [23] Z.Xi,W.Chen,X.Guo,W.He,Y.Ding,B.Hong,M.Zhang,J.Wang,
AutomationLetters,vol.5,no.2,pp.1143–1150,2020. S.Jin,E.Zhouetal.,“Theriseandpotentialoflargelanguagemodel
[2] K.Xu,X.Xiao,J.Miao,andQ.Luo,“Datadrivenpredictionarchitec- basedagents:Asurvey,”arXivpreprintarXiv:2309.07864,2023.
tureforautonomousdrivinganditsapplicationonapolloplatform,”in [24] D. Gao, L. Ji, L. Zhou, K. Q. Lin, J. Chen, Z. Fan, and M. Z.
IEEEIntelligentVehiclesSymposium. IEEE,2020,pp.175–181. Shou,“Assistgpt:Ageneralmulti-modalassistantthatcanplan,execute,
[3] D.Bogdoll,J.Breitenstein,F.Heidecker,M.Bieshaar,B.Sick,T.Fin- inspect,andlearn,”arXivpreprintarXiv:2306.08640,2023.
gscheidt, and M. Zo¨llner, “Description of corner cases in automated [25] Y.Shen,K.Song,X.Tan,D.Li,W.Lu,andY.Zhuang,“Hugginggpt:
driving:Goalsandchallenges,”inProceedingsoftheIEEE/CVFInter- Solvingaitaskswithchatgptanditsfriendsinhuggingface,”Advances
nationalConferenceonComputerVision,2021,pp.1023–1028. inNeuralInformationProcessingSystems,vol.36,2024.
[4] L. Chen, Y. Li, C. Huang, Y. Xing, D. Tian, L. Li, Z. Hu, S. Teng, [26] D. Sur´ıs, S. Menon, and C. Vondrick, “Vipergpt: Visual inference
C.Lv,J.Wangetal.,“Milestonesinautonomousdrivingandintelligent via python execution for reasoning,” in Proceedings of the IEEE/CVF
vehicles—part 1: Control, computing system design, communication, InternationalConferenceonComputerVision,2023,pp.11888–11898.
hdmap,testing,andhumanbehaviors,”IEEETransactionsonSystems, [27] T. Ha¨ndler, “Balancing autonomy and alignment: A multi-dimensional
Man,andCybernetics:Systems,2023. taxonomyforautonomousllm-poweredmulti-agentarchitectures,”arXiv
[5] N. Jaipuria, X. Zhang, R. Bhasin, M. Arafa, P. Chakravarty, S. Shri- preprintarXiv:2310.03659,2023.
vastava, S. Manglani, and V. N. Murali, “Deflating dataset bias using [28] Z. Liu, Y. Zhang, P. Li, Y. Liu, and D. Yang, “Dynamic llm-agent
syntheticdataaugmentation,”inProceedingsoftheIEEE/CVFConfer- network: An llm-agent collaboration framework with agent team openceonComputerVisionandPatternRecognitionWorkshops,2020,pp. timization,”arXivpreprintarXiv:2310.02170,2023.
772–773. [29] W. Chen, Y. Su, J. Zuo, C. Yang, C. Yuan, C.-M. Chan, H. Yu,
[6] X. Ying, “An overview of overfitting and its solutions,” in Journal of Y. Lu, Y.-H. Hung, C. Qian et al., “Agentverse: Facilitating multiphysics:Conferenceseries,vol.1168. IOPPublishing,2019,p.022022. agent collaboration and exploring emergent behaviors,” in The Twelfth
[7] D. M. Hawkins, “The problem of overfitting,” Journal of chemical InternationalConferenceonLearningRepresentations,2023.
informationandcomputersciences,vol.44,no.1,pp.1–12,2004. [30] R. Gong, Q. Huang, X. Ma, Y. Noda, Z. Durante, Z. Zheng, D. Ter-
[8] Y. Zhang, P. Tinˇo, A. Leonardis, and K. Tang, “A survey on neural zopoulos,L.Fei-Fei,J.Gao,andH.Vo,“Mindagent:Emergentgaming
network interpretability,” IEEE Transactions on Emerging Topics in interaction,”inFindingsoftheAssociationforComputationalLinguis-
ComputationalIntelligence,vol.5,no.5,pp.726–742,2021. tics:NAACL2024,2024,pp.3154–3183.

<!-- Page 13 -->

13
[31] H.Zhang,W.Du,J.Shan,Q.Zhou,Y.Du,J.B.Tenenbaum,T.Shu,and
C. Gan, “Building cooperative embodied agents modularly with large
languagemodels,”inTheTwelfthInternationalConferenceonLearning
Representations.
[32] J.Mao,J.Ye,Y.Qian,M.Pavone,andY.Wang,“Alanguageagentfor
autonomousdriving,”arXivpreprintarXiv:2311.10813,2023.
[33] H.Shao,Y.Hu,L.Wang,G.Song,S.L.Waslander,Y.Liu,andH.Li,
“Lmdrive:Closed-loopend-to-enddrivingwithlargelanguagemodels,”
in Proceedings of the IEEE/CVF Conference on Computer Vision and
PatternRecognition,2024,pp.15120–15130.
[34] J.Wei,X.Wang,D.Schuurmans,M.Bosma,F.Xia,E.Chi,Q.V.Le,
D. Zhou et al., “Chain-of-thought prompting elicits reasoning in large
languagemodels,”Advancesinneuralinformationprocessingsystems,
vol.35,pp.24824–24837,2022.
[35] Q.Lyu,S.Havaldar,A.Stein,L.Zhang,D.Rao,E.Wong,M.Apidianaki,andC.Callison-Burch,“Faithfulchain-of-thoughtreasoning,”in
The13thInternationalJointConferenceonNaturalLanguageProcessingandthe3rdConferenceoftheAsia-PacificChapteroftheAssociation
forComputationalLinguistics(IJCNLP-AACL2023),2023.
[36] Z.Zhang,A.Zhang,M.Li,G.Karypis,A.Smolaetal.,“Multimodal
chain-of-thought reasoning in language models,” Transactions on MachineLearningResearch.
[37] A. Papadoulis, M. Quddus, and M. Imprialou, “Evaluating the safety
impactofconnectedandautonomousvehiclesonmotorways,”Accident
Analysis&Prevention,vol.124,pp.12–22,2019.
[38] M. M. Morando, Q. Tian, L. T. Truong, and H. L. Vu, “Studying the
safetyimpactofautonomousvehiclesusingsimulation-basedsurrogate
safetymeasures,”Journalofadvancedtransportation,vol.2018,no.1,
p.6135183,2018.
[39] N.Virdi,H.Grzybowska,S.T.Waller,andV.Dixit,“Asafetyassessmentofmixedfleetswithconnectedandautonomousvehiclesusingthe
surrogate safety assessment module,” Accident Analysis & Prevention,
vol.131,pp.95–111,2019.
[40] E. Leurent et al., “An environment for autonomous driving decisionmaking,”2018.
[41] D. Chen, M. R. Hajidavalloo, Z. Li, K. Chen, Y. Wang, L. Jiang,
and Y. Wang, “Deep multi-agent reinforcement learning for highway
on-ramp merging in mixed traffic,” IEEE Transactions on Intelligent
TransportationSystems,vol.24,no.11,pp.11623–11638,2023.
[42] T.Brown,B.Mann,N.Ryder,M.Subbiah,J.D.Kaplan,P.Dhariwal,
A.Neelakantan,P.Shyam,G.Sastry,A.Askelletal.,“Languagemodels are few-shot learners,” Advances in neural information processing
systems,vol.33,pp.1877–1901,2020.
[43] M. L. Team. (2024) Introducing meta llama 3: The most capable
openly available llm to date. [Online]. Available: https://ai.meta.com/
blog/meta-llama-3/
[44] J. Bai, S. Bai, Y. Chu, Z. Cui, K. Dang, X. Deng, Y. Fan, W. Ge,
Y. Han, F. Huang et al., “Qwen technical report,” arXiv preprint
arXiv:2309.16609,2023.

## Tables

**Table (Page 7):**

| Action | Safety | Efficiency |
|---|---|---|
| #0 | 10 | 10 |
| #1 | 2.8 | 10 |
| #2 | 4.4 | 8.9 |
| #3 | 6.7 | 8.2 |
| #4 | 8.1 | 6.3 |


**Table (Page 8):**

| Parameter | Value |
|---|---|
| Thelanecountofthehighwaymainroad | 2 |
| Thelanecountoftheon-rampmergingroad | 1 |
| Thelengthofon-rampmergingroad | 120m |
| Theinitializationspeedofvehicles | rangefrom20to25m/s |
| Thespacingofthespawnpoints | 40m |
| Theinitiallocationnoise | rangefrom-10to10m |
| ThecountofLLMcontrolledvehicles | 2 |
| Thecountofintelligentdrivermodelvehicles | 5 |
| Policyfrequency | 2Hz |


**Table (Page 8):**

| Parameter | Value |
|---|---|
| Simulationenvironment | highway-env[40] |
| Largelanguagemodel | GPT-4[13] |
| Textembeddingmodel | text-embeddings-ada-002 |
| Vectordatabase | Chroma |


**Table (Page 9):**

| Trainingepisodes | DiLu | KoMA |
|---|---|---|
| 0 | 40% | 30% |
| 20 | 50% | 50% |
| 40 | 50% | 70% |


**Table (Page 11):**

| episodes | GPT3.5 | GPT4 | Llama3-8B | Llama2-7B | Qwen2-7B |
|---|---|---|---|---|---|
| 0 | 20% | 30% | 25% | 20% | 25% |
| 20 | 30% | 50% | 35% | 25% | 30% |
| 40 | 35% | 70% | 40% | 35% | 40% |
