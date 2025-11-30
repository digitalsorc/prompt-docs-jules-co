---
title: "From LLM Reasoning Autonomous Agents"
original_file: "./From_LLM_Reasoning_Autonomous_Agents.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["prompt-engineering", "llm", "rag", "chain-of-thought", "react"]
keywords: ["agent", "agents", "reasoning", "models", "llm", "multi", "language", "llms", "high", "arxivpreprintarxiv"]
summary: "<!-- Page 1 -->

1
From LLM Reasoning to Autonomous AI Agents:

### A Comprehensive Review

Mohamed Amine Ferrag∗¶, Norbert Tihanyi†‡, and Merouane Debbah§
∗Guelma University, Algeria
†Technology Innovation Institute, UAE
‡Eo¨tvo¨s Lora´nd University, Hungary
§Khalifa University of Science and Technology, UAE
¶Corresponding author: ferrag.mohamedamine@univ-guelma.dz
Abstract—Large language models and autonomous AI agents employing reflection, planning, and multi-agent collaboration
have evolved "
related_documents: []
---

# From LLM Reasoning Autonomous Agents

<!-- Page 1 -->

1
From LLM Reasoning to Autonomous AI Agents:

### A Comprehensive Review

Mohamed Amine Ferrag∗¶, Norbert Tihanyi†‡, and Merouane Debbah§
∗Guelma University, Algeria
†Technology Innovation Institute, UAE
‡Eo¨tvo¨s Lora´nd University, Hungary
§Khalifa University of Science and Technology, UAE
¶Corresponding author: ferrag.mohamedamine@univ-guelma.dz
Abstract—Large language models and autonomous AI agents employing reflection, planning, and multi-agent collaboration
have evolved rapidly, resulting in a diverse array of evaluation has given rise to Agentic RAG systems, which dynamically
benchmarks, frameworks and collaboration protocols. However,
orchestrate information retrieval and iterative refinement to
thelandscaperemainsfragmentedandlacksaunifiedtaxonomy
manage complex workflows effectively [11], [12].
or comprehensive survey. Therefore, we present a side-by-side
comparison of benchmarks developed between 2019 and 2025 Recent advances in large language models have paved the
that evaluate these models and agents across multiple domains. wayforhighlyautonomousAIsystemsthatcanindependently
In addition, we propose a taxonomy of approximately 60 bench- handle complex research tasks. These systems, often referred
marks that cover general and academic knowledge reasoning,
to as agentic AI, can generate hypotheses, conduct literature
mathematical problem-solving, code generation and software
reviews,designexperiments,analyzedata,acceleratescientific
engineering, factual grounding and retrieval, domain-specific
evaluations, multimodal and embodied tasks, task orchestration, discovery, and reduce research costs [13], [14], [15], [16].
and interactive assessments. Furthermore, we review AI-agent Several frameworks, such as LitSearch, ResearchArena, and
frameworks introduced between 2023 and 2025 that integrate Agent Laboratory, have been developed to automate various
large language models with modular toolkits to enable auresearch tasks, including citation management and academic
tonomous decision-making and multi-step reasoning. Moreover,
survey generation [17], [18], [19]. However, challenges per- we present real-world applications of autonomous AI agents
in materials science, biomedical research, academic ideation, sist, especially in executing domain-specific literature reviews
software engineering, synthetic data generation, chemical rea- and ensuring the reproducibility and reliability of automated
soning, mathematical problem-solving, geographic information processes[20],[21].Paralleltothesedevelopmentsinresearch
systems, multimedia, healthcare, and finance. We then survey
automation, large language model-based agents have also
key agent-to-agent collaboration protocols, namely the Agent
beguntotransformthemedicalfield[22].Theseagentsarein-

### Communication Protocol (ACP), the Model Context Protocol

(MCP), and the Agent-to-Agent Protocol (A2A). Finally, we creasinglyusedfordiagnosticsupport,patientcommunication,
discuss recommendations for future research, focusing on ad- andmedicaleducationbyintegratingclinicalguidelines,medvanced reasoning strategies, failure modes in multi-agent LLM ical knowledge bases, and healthcare systems. Despite their
systems,automatedscientificdiscovery,dynamictoolintegration
promise, these applications face significant hurdles, including
via reinforcement learning, integrated search capabilities, and
concerns over reliability, reproducibility, ethical governance,
security vulnerabilities in agent protocols.
and safety [23], [24], [25]. Addressing these issues is crucial

### Index Terms—Large Language Models, Autonomous AI

for ensuring that LLM-based agents can be effectively and
Agents, Agentic AI, Reasoning, Benchmarks.
responsibly incorporated into clinical practice, underscoring
the need for comprehensive evaluation frameworks that can

## I. Introduction

reliably measure their performance across various healthcare
Large Language Models (LLMs) such as OpenAI’s GPT- tasks [26], [27], [28].
4 [1], Qwen2.5-Omni [2], DeepSeek-R1 [3], and Meta’s LLM-based agents are emerging as a promising frontier in
LLaMA [4] have transformed AI by enabling human-like text AI, combining reasoning and action to interact with complex
generationandadvancednaturallanguageprocessing,spurring digitalenvironments[29],[30].Therefore,variousapproaches
innovation in conversational agents, automated content cre- have been explored to enhance LLM-based agents, from
ation,andreal-timetranslation[5].Recentenhancementshave combining reasoning and acting using techniques like React
extended their utility to multimodal tasks, including text-to- [31] and Monte Carlo Tree Search [32] to synthesizing highimage and text-to-video generation that broaden the scope quality data with methods like Learn-by-Interact [33], which
of generative AI applications [6]. However, their dependence sidestep assumptions such as state reversals. Other strategies
on static pre-training data can lead to outdated outputs and involvetrainingonhuman-labeledorGPT-4distilleddatawith
hallucinated responses [7], [8], a limitation that Retrieval- systemslikeAgentGen[34]andAgentTuning[35]togenerate
Augmented Generation (RAG) addresses by incorporating trajectory data. At the same time, reinforcement learning
real-time data from knowledge bases, APIs, or the web [9], methods utilize offline algorithms and iterative refinement
[10]. Building on this, the evolution of intelligent agents through reward models and feedback to enhance efficiency
5202
rpA
82
]IA.sc[
1v87691.4052:viXra

<!-- Page 2 -->

2
and performance in realistic environments [36], [37]. efforts across multiple domains. In this section, we review
LLM-basedMulti-Agentsharnessthecollectiveintelligence the most relevant studies that investigate the integration of
of multiple specialized agents, enabling advanced capabilities LLM-based agents into software engineering, propose agent
over single-agent systems by simulating complex real-world architectures and evaluation frameworks, explore the develenvironments through collaborative planning, discussion, and opment of multi-agent systems, and examine domain-specific
decision-making. This approach leverages the communicative applications, including healthcare, game-theoretic scenarios,
strengths and domain-specific expertise of LLMs, allowing GUIinteractions,personalassistance,scientificdiscovery,and
distinct agents to interact effectively, much like human teams chemistry.
tackling problem-solving tasks [38], [39]. Recent research
highlightspromisingapplicationsacrossvariousfields,includ- A. LLM-based Agents in Software Engineering
ingsoftwaredevelopment[40],[41],multi-robotsystems[42],
Wang et al. [47] present a survey that bridges Large Lan-
[43],societysimulation[44],policysimulation[45],andgame
guage Model (LLM)-based agent technologies with software
simulation [46].
engineering (SE). It highlights how LLMs have achieved

### The main contributions of this study are:

significant success in various domains and have been in-
• Wepresentacomparativetableofbenchmarksdeveloped tegrated into SE tasks, often under the agent paradigm,
between2019and2025thatrigorouslyevaluatelargelanwhetherexplicitlyorimplicitly.Thestudypresentsastructured
guage models and autonomous AI agents across multiple
framework for LLM-based agents in SE, comprising three
domains.
primary modules: perception, memory, and action. Jin et al.
• We propose a taxonomy of approximately 60 LLM [48] investigate the use of large language models (LLMs)
and AI-agent benchmarks, including general and acaandLLM-basedagentsinsoftwareengineering,distinguishing
demic knowledge reasoning, mathematical problem solvbetweenthetraditionalcapabilitiesofLLMsandtheenhanced
ing, code generation and software engineering, facfunctionalitiesofferedbyautonomousagents.Ithighlightsthe
tualgroundingandretrieval,domain-specificevaluations,
significant success of LLMs in tasks such as code generamultimodal and embodied tasks, task orchestration, and
tion and vulnerability detection, while also addressing their
interactive and agentic assessments.
limitations, specifically the issues of autonomy and self-
• We present prominent AI-agent frameworks from 2023 improvement that LLM-based agents aim to overcome. The
to 2025 that integrate large language models with modpaper provides an extensive review of current practices across
ular toolkits, enabling autonomous decision-making and
six key domains: requirement engineering, code generation,
multi-step reasoning.
autonomousdecision-making,softwaredesign,testgeneration,
• We provide applications of autonomous AI agents in and software maintenance. In a complementary study, Jin et
variousfields,includingmaterialsscienceandbiomedical
al. [48] investigate the use of large language models (LLMs)
research, academic ideation and software engineering,
andLLM-basedagentsinsoftwareengineering,distinguishing
syntheticdatagenerationandchemicalreasoning,mathebetweenthetraditionalcapabilitiesofLLMsandtheenhanced
maticalproblem-solvingandgeographicinformationsysfunctionalities offered by autonomous agents. It highlights
tems, as well as multimedia, healthcare, and finance.
the significant success of LLMs in tasks such as code gen-
• Wesurveyagent-to-agentcollaborationprotocols,namely eration and vulnerability detection, while also addressing
the Agent Communication Protocol (ACP), the Model
their limitations, specifically, issues of autonomy and self-
Context Protocol (MCP), and the Agent-to-Agent Proimprovement that LLM-based agents aim to overcome. The
tocol (A2A).
paper provides an extensive review of current practices across
• We outline recommendations for future research on au- six key domains: requirement engineering, code generation,
tonomous AI agents, specifically advanced reasoning
autonomousdecision-making,softwaredesign,testgeneration,
strategies, failure modes in multi-agent large language
and software maintenance.
model (LLM) systems, automated scientific discovery,
dynamictoolintegrationviareinforcementlearning,inte-

### B. Agent Architectures and Evaluation Frameworks

grated search capabilities, and security vulnerabilities in
agent protocols. Singh et al. [49] delves into Agentic Retrieval-Augmented
Generation (Agentic RAG), a sophisticated evolution of tra-

### Fig. 1 illustrates the structure of this survey. Section II

ditional Retrieval-Augmented Generation systems that enpresents the related works. Section III provides a side-byhances the capabilities of large language models (LLMs).
side tabular comparison of state-of-the-art LLM and Agentic

### While LLMs have transformed AI through human-like text


### AI benchmarks. Section IV reviews AI agent frameworks, AI

generation and language understanding, their dependence on
agent applications, AI agent protocols, and training datasets
static training data often results in outdated or imprecise
across various domains. Section V highlights several critical
responses. The paper addresses these limitations by embedresearch directions. Finally, Section VI concludes the paper.
dingautonomousagentswithintheRAGframework,enabling
dynamic, real-time data retrieval and adaptive workflows.

## Ii. Relatedworks


### It details how agentic design patterns such as reflection,

The growing field of autonomous AI agents powered by planning, tool utilization, and multi-agent collaboration equip
large language models has inspired a wide range of research thesesystemstomanagecomplextasksandsupportmulti-step

<!-- Page 3 -->

3

### LLM and Agentic AI

Introduction Related Works

### Benchmarks

How have recent advancements in LLMs What are the related surveys in the field What are the key LLM benchmarks
and agentic AI impacted autonomous AI of LLM-based agents and autonomous AI developed between 2019 and 2025 for
systems, and what are the main systems? evaluating large language models and
contributions of this study? agentic AI systems across various
domains?

### LLM-based Agents in Software

Recent advancements in LLMs Engineering
ComplexFuncBench
MMLU benchmark
benchmark

### Agent Architectures and Evaluation

Agentic AI Frameworks Humanity's Last FACTS Grounding
Exam (HLE)
benchmark
benchmark

### Multi-Agent Domain-Specific


### Collaborative Multi-Agent Systems

Systems Applications ProcessBench OmniDocBench
benchmark Benchmark
Main Contributions Organization of

### Comparison with Our Survey

of the Paper the Paper Agent-as-a-Judge ...
Challenges and and Open
AI Agents Conclusion

### Problems

What are the key AI agent frameworks and What are the key challenges and open What are the key conclusions and future
applications developed between 2024 and problems in advancing AI agents and directions for large language models
2025 for achieving autonomous decision- large language models? (LLMs) and autonomous AI agents?
making and dynamic reasoning in realworld tasks?
AI Agents Reasoning

### Key conclusions

AI Agent frameworks Why Do Multi-Agent LLM Systems

### Fail?

AI Agents in Automated Scientific
AI Agent applications

### Discovery


### Challenges

Dynamic Tool Integration for
Autonomous AI Agents

### AI Agents protocols


### Empowering LLM Agents with

Integrated Search via Reinforcement
Future directions

### Learning


### Training datasets

Vulnerabilities of AI Agents Protocols
Fig. 1: Survey Structure.
reasoning. The survey offers a comprehensive taxonomy of Moreover, the paper critically highlights existing deficiencies
Agentic RAG architectures, highlights key applications across in the field, notably the need for metrics that more effectively
various sectors, including healthcare, finance, and education, capture cost efficiency, safety, and robustness. In doing so,
and outlines practical implementation strategies. it maps the current landscape of agent evaluation and sets
forthcompellingdirectionsforfutureinquiry,underscoringthe
Complementing this architectural perspective, Yehudai et importance of scalable and fine-grained evaluation techniques
al. [50] mark a significant milestone in artificial intelligence in the rapidly evolving AI domain.
by surveying evaluation methodologies for agents powered
by large language models (LLMs). It thoroughly reviews Similarly, Chen et al. [51] focus on Role-Playing Agents
the capabilities of these agents, focusing on core functions (RPAs), a growing class of LLM-based agents that mimic
such as planning, tool utilization, self-reflection, and mem- humanbehavioracrossvarioustasks.Recognizingtheinherent
ory, while assessing specialized applications ranging from challengesinevaluatingsuchdiversesystems,theauthorssysweb interactions to software engineering and conversational tematically reviewed 1,676 papers published between January
tasks. The authors uncover a clear trend toward developing 2021 and December 2024. Their extensive analysis identifies
more rigorous, dynamically updated evaluation frameworks six key agent attributes, seven task attributes, and seven
by examining both targeted benchmarks for domain-specific evaluation metrics that are prevalent in the current literature.
applications and those designed for more generalist agents. Basedontheseinsights,thepaperproposesanevidence-based,

<!-- Page 4 -->

4
TABLE I: An overview of selected surveys on AI Agents.
Theme Reference Year KeyContribution Benchmark AIAgent AIAgent AI Challenges

### Frame- Applica- Agents & Open

works tions Protocols Problems
LLM-based Agents Wang et 2024 Survey of LLM-based agent technologies
in Software Engi- al.[47] in SE; proposes a perception–memory–action
neering framework.
LLM-based Agents Jinetal.[48] 2024 ReviewsLLMvs.autonomous-agentcapabiliin Software Engi- ties across six SE domains; highlights autonneering omygaps.
AgentArchitectures Singh et 2025 Introduces Agentic RAG: embedding au-
&Evaluation al.[49] tonomousagentsinRAGwithplanning,reflection,tooluse,andcollaboration.
AgentArchitectures Yehudai et 2025 Surveys evaluation methodologies and bench-
&Evaluation al.[50] marks for LLM agents, covering cost, safety,
androbustness.
AgentArchitectures Chen et 2025 Analyzes1,676RPAs,identifiescoreattributes,
&Evaluation al.[51] and proposes standardized evaluation guidelines.
Multi-Agent Yan et 2025 ComprehensivesurveyofLLM-poweredMAS;
Systems al.[52] focusesoncommunication,scalability,security,
andmultimodality.
Multi-Agent Guo et 2024 Traces evolution from single-agent LLM rea-
Systems al.[38] soningtocollaborativeMAS;examinesprofilingandcommunication.
Healthcare Wang et 2025 Reviews LLM-agent architectures for clinical
al.[28] decisionsupport,documentation,training;discussesethics.
Social Agents in Feng et 2024 SurveysLLM-basedsocialagentsingamethe-
GameTheory al.[53] ory; categorizes frameworks, agent attributes,
andevaluationprotocols.
GUIAgents Zhang et 2024 Chronicles evolution of LLM-driven GUI
al.[54] agents; covers multimodal understanding and
large-actionmodels.
Personal LLM Lietal.[55] 2024 Examines personal LLM agents integrating
Agents userdata/devices;surveysarchitecturesandsecuritychallenges.
ScientificDiscovery Gridach et 2025 Explores Agentic AI in automating research
al.[21] workflowsacrossdomains;highlightsreliabilityandethics.
Chemistry Ramos et 2025 Reviews LLM roles in molecule design and
al.[56] synthesis planning; introduces agents for lab
control.
OurSurvey Ferragetal. 2025 Unified end-to-end survey covering benchmarks,frameworks,applications,protocols,and
challenges.

### NotConsidered( );Partialdiscussion( );Considered( );

actionable, and generalizable evaluation guideline designed to enabled significant advances in complex problem-solving and
standardize the assessment of RPAs. world simulation. Key aspects of these systems are examined,
including the domains and environments they simulate, the
C. Multi-Agent Systems profiling and communication strategies employed by individualagents,andthemechanismsthatunderpintheenhancement
Yanetal.[52]providesacomprehensivesurveyonintegratof their collective capacities.
ing LLMs into multi-agent systems (MAS). Their work emphasizesthecommunication-centricaspectsthatenableagents
to engage in both cooperative and competitive interactions,

### D. Domain-Specific Applications

thereby tackling tasks that are unmanageable for individual
agents. The paper examines system-level features, internal 1) Healthcare: Wang et al. [28] explores the transformacommunication mechanisms, and challenges, including scala- tive impact of LLM-based agents on healthcare, presenting
bility, security, and multimodal integration. In a related study, a detailed review of their architectures, applications, and
Guo et al. [38] offer an extensive overview of LLM-based inherentchallenges.Itdissectsthecorecomponentsofmedical
multi-agent systems, charting the evolution from single-agent agent systems, such as system profiles, clinical planning
decision-making to collaborative frameworks that enhance mechanisms, and medical reasoning frameworks, while also
collective problem-solving and world simulation. In a related discussing methods to enhance external capacities. Major
study, Guo et al. [38] provide an extensive overview of large application areas include clinical decision support, medical
language model (LLM)-based multi-agent systems, building documentation, training simulations, and overall healthcare
on the success of LLMs in autonomous planning and reason- service optimization. The survey further evaluates the pering. The authors detail how the evolution from single-agent formance of these agents using established frameworks and
decision-making to collaborative multi-agent frameworks has metrics,identifyingpersistentchallengessuchashallucination

<!-- Page 5 -->

5
management, multimodal integration, and ethical considera- used in the field, offering valuable insights into current practions. tices.Moreover,thepapercriticallyaddressessignificantchal-
2) Social Agents in Game-Theoretic Scenarios: Feng et al. lenges,includingautomatingcomprehensiveliteraturereviews,
[53]provideareviewofresearchonLLM-basedsocialagents ensuring system reliability, and addressing ethical concerns.
in game-theoretic scenarios. This area has gained prominence It outlines future research directions, emphasizing the imfor assessing social intelligence in AI systems. The authors portance of human-AI collaboration and improved system
categorizetheliteratureintothreemaincomponents.First,the calibration.
gameframeworkisexamined,highlightingvariouschoice-and 6) Chemistry: Ramos et al. [56] examine the transformacommunication-focused scenarios. Second, the paper explores tive impact of large language models (LLMs) in chemistry,
the attributes of social agents, examining their preferences, focusingontheirrolesinmoleculedesign,propertyprediction,
beliefs, and reasoning capabilities. Third, it discusses evalua- and synthesis optimization. It highlights how LLMs not only
tion protocols incorporating game-agnostic and game-specific accelerate scientific discovery through automation but also
metricstoassessperformance.Bysynthesizingcurrentstudies discuss the advent of LLM-based autonomous agents. These
and outlining future research directions, the survey offers agents extend the functionality of LLMs by interfacing with
valuable insights to further the development and systematic their environment and performing tasks such as literature
evaluation of social agents within game-theoretic contexts. scraping, automated laboratory control, and synthesis plan-
3) GUI Agents: Zhang et al. [54] review LLM-brained ning. Expanding the discussion beyond chemistry, the review
GUI agents, marking a paradigm shift in human-computer also considers applications across other scientific domains.
interaction through integrating multimodal LLMs. It traces
the historical evolution of GUI automation, detailing how

### E. Comparison with Our Survey

advancements in natural language understanding, code gen-

### Table I presents a consolidated view of how existing works

eration, and visual processing have enabled these agents to
coverkeythemes,benchmarks,AIagentframeworks,AIagent
interpret complex graphical user interface (GUI) elements
applications,AIagentsprotocols,andchallenges&openproband execute multi-step tasks from conversational commands.
lems against our survey. While prior studies typically focus

### The survey systematically examines the core components of

on one or two aspects (e.g., Yehudai et al. [50] on evaluation
these systems, including existing frameworks, data collection
benchmarks, Singh et al. [49] on RAG architectures, Yan et
and utilization methods for training, and the development of
al.[52]onmulti-agentcommunication,orWangetal.[28]on
specialized large-scale action models for GUI tasks.
domain-specificapplications),noneintegratethefullspectrum
4) Personal LLM Agents: Li et al. [55] explore the evoluof developments in a single, unified treatment. In contrast,
tion of intelligent personal assistants (IPAs) by focusing on
our survey is the first to systematically combine state-of-
Personal LLM Agents LLM-based agents that deeply intethe-art benchmarks, framework design, application domains,
grate personal data and devices to provide enhanced personal
communicationprotocols,andaforward-lookingdiscussionof
assistance. The authors outline the limitations of traditional
challenges and open problems, thereby providing researchers
IPAs, including insufficient understanding of user intent, task
with a comprehensive roadmap for advancing LLM-based
planning,andtoolutilization,whichhavehinderedtheirpractiautonomous AI agents.
calityandscalability.Incontrast,theemergenceoffoundation
models like LLMs offer new possibilities by leveraging advancedsemanticunderstandingandreasoningforautonomous

## Iii. Llmandagenticaibenchmarks

problem-solving. The survey systematically reviews the archi- This section provides a comprehensive overview of benchtecture and design choices underlying Personal LLM Agents, marksdevelopedbetween2019and2025thatrigorouslyevalinformed by expert opinions, and examines key challenges uate large language models (LLMs) across diverse and chalrelatedtointelligence,efficiency,andsecurity.Furthermore,it lenging domains. For instance, ENIGMAEVAL [57] assesses
comprehensively analyzes representative solutions addressing complexmultimodalpuzzle-solvingbyrequiringthesynthesis
these challenges, laying the groundwork for Personal LLM of textual and visual clues, while ComplexFuncBench [59]
Agents to become a major paradigm in next-generation end- challenges models with multi-step function-calling tasks that
user software. mirror real-world scenarios. Humanity’s Last Exam (HLE)
5) Scientific Discovery: Gridach et al. [21] explore the [60] further raises the bar by presenting expert-level acatransformative role of Agentic AI in scientific discovery, demic questions across a broad spectrum of subjects, thereby
underscoring its potential to automate and enhance research reflecting the growing demand for deeper reasoning and
processes.Itreviewshowthesesystems,endowedwithreason- domain-specific proficiency. Additional frameworks such as
ing, planning, and autonomous decision-making capabilities, FACTS Grounding [61] and ProcessBench [62] scrutinize
are revolutionizing traditional research activities, including the models’ capacities for generating factually accurate longliteraturereviews,hypothesisgeneration,experimentaldesign, form responses and detecting errors in multi-step reasoning.
and data analysis. The paper highlights recent advancements Meanwhile, innovative evaluation paradigms like Agent-as-aacrossmultiplescientificdomains,suchaschemistry,biology, Judge [64], JudgeBench [65], and CyberMetric [75] provide
and materials science, by categorizing existing Agentic AI granular insights into cybersecurity competencies and errorsystems and tools. It provides a detailed discussion on key detection capabilities. Tables III, II present a comprehensive
evaluation metrics, implementation frameworks, and datasets overview of benchmarks developed between 2024 and 2025.

<!-- Page 6 -->

6

### TABLE II: Summary of LLM Benchmarks (Part 1)

Benchmark/ Year EvaluationFocus KeyFeatures/Metrics Innovations/Techniques Observations

### Dataset

ENIGMAEVAL 2025 Multimodal Contains1,184puzzlescombining Evaluatesmultimodaland Pushesmodelsintounstructured,
[57] Reasoning textandimages;state-of-the-art long-contextreasoningusing creativeproblem-solvingscenarios
systemsscoreonly∼7%onstandard challengingpuzzlesfromglobal requiringintegrationofvisualand
puzzlesandfailonthehardestones. competitions. semanticclues.
MMLU 2021 Multitask Comprises57diversetasks(from Assessesbroadworldknowledgeand Designedforgeneralmultitask
Benchmark Knowledge elementarymathtoprofessionallaw) problem-solvingskills;uncovers languageunderstandingwithout
[58] testingzero-shotandfew-shot calibrationchallengesandimbalances task-specificfine-tuning.
performance. betweenproceduralanddeclarative
knowledge.
ComplexFuncBench 2025 FunctionCalling Evaluatescomplexfunctioncalling Introducesanautomaticevaluation Highlightsperformancedifferences
[59] taskswithmulti-stepoperationsand framework(ComplexEval)for betweenclosedmodels(e.g.,Claude
inputlengthsupto128ktokensover functioncalling,testingreasoning 3.5,GPT-4)andopenmodels(e.g.,
morethan1,000scenarios. overimplicitparametersand Qwen2.5,Llama3.1).
constraints.
Humanity’s 2025 Academic Features3,000questionsspanning Developedthroughaglobal Exposessignificantperformancegaps
LastExam Reasoning over100subjects,including collaborativeeffortwithnearly1,000 asstate-of-the-artLLMsscorebelow
(HLE)[60] multi-modalchallenges. experts;includesbothmultiple-choice 10%,servingasacriticaltoolfor
andshort-answerformatswith assessingacademicreasoning.
verifiableanswers.
FACTS 2023 FactualGrounding Contains1,719examplesrequiring Usesatwo-phaseevaluation Focusesonfactualaccuracyand
Grounding detailedresponsesgroundedinsource (eligibilityandfactualgrounding) informationsynthesiswhileexcluding
[61] documents,withinputsreachingup withassessmentsfromfrontierLLM creativeorcomplexreasoningtasks.
to32,000tokens. judges.
ProcessBench 2024 ErrorDetection Comprises3,400mathproblemcases Evaluatesmodels’abilitytodetect Targetsgranularerrordetectionin
[62] withstep-by-stepsolutionsand theearliesterrorinreasoning; mathematicalproblemsolving.
human-annotatederrorlocations. comparesprocessrewardmodelswith
LLM-basedcritics.
OmniDocBench 2024 Document Amulti-sourcedatasetspanningnine Providesadetailed,multi-level Addresseschallengessuchasfuzzy
[63] Understanding documenttypeswith19layout evaluationframeworkfordocument scans,watermarks,andcomplex
categoriesand14attributelabels. contentextraction,contrasting layoutsindocumentprocessing.
modularpipelineswithend-to-end
methods.
Agent-as-a- 2024 Evaluation Evaluatedon55codegeneration Leveragesagenticsystemstoprovide Reducesevaluationcostandtimefor
Judge[64] Methodology taskswith365hierarchicaluser granular,intermediatefeedback; agenticsystems,particularlyincode
requirements. achievesupto90%alignmentwith generationtasks.
humanjudgments.
JudgeBench 2024 Judgment Consistsof350challengingresponse Transformsexistingdatasetsinto Aimstoobjectivelyassess
[65] Evaluation pairsacrossknowledge,reasoning, pairedcomparisonswithobjective LLM-basedjudges;fine-tuningcan
math,andcodingdomains. correctness,mitigatingpositionalbias boostjudgeaccuracysignificantly.
throughdoubleevaluation.
SimpleQA 2023 FactualQA Contains4,326fact-seekingquestions Focusesonevaluatingfactual Highlightscurrentlimitationsin
[66] acrossdomains;usesastrict accuracyandrevealsmodels’ handlingstraightforward,factual
three-tiergradingsystem. overconfidenceinincorrectresponses queries.
throughrepeatedtesting.
FineTasks[67] 2023 MultilingualTask Evaluates185candidatetasksacross Employsmetricssuchas Providesascalable,multilingual
Selection ninelanguages,ultimatelyselecting monotonicity,lownoise,non-random evaluationplatformthathighlightsthe
96reliabletasks;supportsover550 performance,andmodelordering impactoftaskformulation.
tasksoverall. consistencytoassesstaskquality.
FRAMES[68] 2024 Retrieval& Consistsof824multi-hopquestions Unifiesevaluationsoffactual Baselineexperimentsshow
Reasoning requiringintegrationof2–15 accuracy,retrieval,andreasoning; improvementsfrom40%(without
Wikipediaarticles. labelsquestionswithspecific retrieval)to66%(withmulti-step
reasoningtypes(e.g.,numerical, retrieval).
tabular).
DABStep[69] 2025 Step-Based Astep-basedapproachformulti-step Decomposescomplexproblem Highlightsthesignificantchallenges
Reasoning reasoningtasks;thebestmodel solvingintodiscretestepswith intrainingmodelsforcomplex,
achievesonlya16%successrate. iterativerefinementand iterativereasoning.
self-correction.

<!-- Page 7 -->

7

### TABLE III: Summary of LLM Benchmarks (Part 2)

Benchmark/ Year EvaluationFocus KeyFeatures/Metrics Innovations/Techniques Observations

### Dataset

BFCLv2[70] 2025 FunctionCalling Contains2,251 Leveragesreal-world, Demonstratesthatmodelssuchas
question-function-answerpairs user-contributeddatatoaddress Claude3.5andGPT-4outperform
coveringsimpletoparallelfunction issueslikedatacontaminationand others,whilesomeopenmodels
calls. biasinfunctioncallingevaluation. struggle.
SWE-Lancer 2025 Software Consistsofover1,400freelance Usestriple-verifiedtestsfor Indicatesthatevenadvancedmodels
[71] Engineering softwareengineeringtasks,including independenttasksandbenchmarks (e.g.,Claude3.5Sonnet)havelow
independentandmanagerialtasks managerialdecisionsagainsthiring passrates(26.2%)onimplementation
withreal-worldpayoutdata. managerselections. tasks.
CRAG 2024 Retrieval- Comprises4,409question-answer Evaluatesthegenerativecomponent Highlightsperformancedropsfor
Benchmark Augmented pairsacross5domains;simulates ofRAGpipelines;shows questionsinvolvinghighlydynamic
[72] Generation retrievalwithmockAPIs. improvementfrom34%to63% orlesspopularfacts.
accuracywithadvancedRAG
methods.
OCCULT 2025 Cybersecurity Alightweightframeworkfor Simulatesreal-worldthreatscenarios Preliminaryresultsindicatemodels
Benchmark operationalevaluationof toassessLLMcapabilitiesin likeDeepSeek-R1achieveover90%
[73] cybersecurityrisks;includesthree offensivecyberoperations. inThreatActorCompetencyTests.
distinctOCObenchmarks.
DIA 2024 DynamicProblem Usesdynamicquestiontemplates Introducesinnovativemetricsfor Revealsgapsinhandlingcomplex
Benchmark Solving withmutableparametersacross reliabilityandconfidenceover tasksandcomparesmodels’
[74] domains(math,cryptography, multipleattempts;emphasizes self-assessmentabilities.
cybersecurity,computerscience). adaptiveintelligence.
CyberMetric 2024 Cybersecurity Asuiteofmultiple-choiceQ&A GeneratedusingGPT-3.5andRAG,it Demonstratesthatlarger,
Benchmark Knowledge datasets(CyberMetric-80,-500, benchmarkscybersecurityknowledge domain-specificmodelsoutperform
[75] -2000,-10000)validatedover200 againsthumanperformance. smalleronesincybersecurity
humanexperthours. understanding.
BIG-Bench 2025 Challenging Anelevated-difficultyvariantof ReplaceseachBBHtaskwithamore Emphasizessubstantialroomfor
ExtraHard Reasoning BIG-BenchHard;averageaccuracyis challengingvarianttoprobe improvementingeneral-purpose
[76] 9.8%forgeneralmodelsand44.8% reasoningcapabilitiesrobustly. reasoningskills.
forreasoning-specializedmodels.
MultiAgentBench 2025 Multi-Agent Encompassessixdomains:research Investigatesvariouscoordination GPT-4o-miniachievesthehighest
[77] proposalwriting,Minecraftstructure protocols(star,chain,tree,graph); averagetaskscore;highlightssynergy
building,databaseerroranalysis, peer-to-peercommunicationplus vs.complexitytrade-offsin
collaborativecoding,competitive cognitiveplanningyieldsa3% multi-agentLLMsettings.
Werewolfgameplay,andresource improvementinmilestone
bargaining. achievement.Graph-basedprotocols
outperformothersinresearchtasks.
GAIA[78] 2024 GeneralAI 466curatedquestionswithreference Emphasizeseverydayreasoningtasks Highlightsthelargeperformancegap
Assistants answers;humansachieve92% involvingmulti-modality,web betweenhumansandSOTAmodels;
accuracywhileGPT-4withplugins browsing,andtooluse.TargetsAI aimstomeasuretruly
onlyreaches15%. robustnessoverspecializedskills. general-purposeAIcapabilities.
CASTLE[79] 2025 Vulnerability 250hand-craftedmicro-benchmark Integratesevaluationsacross13static Formalverificationtools(e.g.,
detectioninsource programscovering25common analysistools,10LLMs,andtwo ESBMC)minimizefalsepositivesbut
code CWEs;introducesthenovelCASTLE formalverificationtools;providesa missvulnerabilitiesbeyondmodel
Scoremetric unifiedframeworkforcomparing checking;staticanalyzersgenerate
diversemethods excessivefalsepositives;LLMs
performwellonsmallcodesnippets,
butaccuracydeclinesand
hallucinationsincreaseascodesize
grows
SPIN-Bench 2025 StrategicPlanning, Evaluatesreasoningandstrategic Systematicallyvariesactionspaces, RevealsthatwhileLLMsperform
[80] Interaction,and behaviorindiversesocialsettingsby statecomplexity,andthenumberof basicfactretrievalandshort-range
Negotiation combiningclassicalPDDLtasks, interactingagentstosimulaterealistic planningreasonablywell,they
competitiveboardgames,cooperative socialinteractions,providingbotha strugglewithdeepmulti-hop
cardgames,andmulti-agent benchmarkandanarenafor reasoningandsociallyadept
negotiationscenarios. multi-agentevaluation. coordination,highlightinga
significantgapinrobustmulti-agent
planningandhuman–AIteaming.
τ-bench[81] 2024 Conversational Evaluatesdynamic,multi-turn Integratesdomain-specificAPItool Revealsthatevenstate-of-the-art
AgentEvaluation conversationsbycomparingthefinal usageandstrictpolicyadherence agents(e.g.,GPT-4o)succeedonless
databasestatewithanannotatedgoal withinsimulateduserinteractionsto than50%oftasks,withmarked
stateusinganovelpassk metric. assessagentreliabilityovermultiple inconsistency(e.g.,pass8<25%in
trials. retail),highlightingtheneedfor
improvedconsistencyand
rule-following.

<!-- Page 8 -->

8
A. ENIGMAEVAL benchmark 90% accuracy, HLE presents a significantly more demanding
test, featuring 3,000 questions spanning over 100 subjects

### ENIGMAEVAL[57]isabenchmarkdesignedtorigorously

including mathematics, humanities, and the natural sciences.
evaluate advanced language models’ multimodal and long-

### This benchmark is the product of a global collaborative

context reasoning capabilities using challenging puzzles deeffort, with nearly 1,000 subject matter experts from over 500
rived from global competitions. The dataset comprises 1,184
institutions contributing questions that are both multi-modal
complexpuzzlesthatcombinetextandimages,requiringmodand resistant to quick internet retrieval, ensuring that only
elstosynthesizedisparateclues,performmulti-stepdeductive
genuinedeepacademicunderstandingcanleadtosuccess.The
reasoning, and integrate visual and semantic information to
tasks, which include both multiple-choice and short-answer
arrive at unambiguous, verifiable solutions. Unlike convenformatswithclearlydefined,verifiableanswers,exposeasubtionalbenchmarksfocusingonwell-structuredacademictasks,
stantial performance gap: current state-of-the-art LLMs, such
ENIGMAEVAL pushes models into unstructured, creative
asDeepSeekR1,OpenAI’smodels,GoogleDeepMindGemini
problem-solvingscenarioswhereevenstate-of-the-artsystems

### Thinking,andAnthropicSonnet3.5,performatlessthan10%

achieve only about 7% accuracy on standard puzzles and fail
accuracy and suffer from high calibration errors, indicating
on the hardest ones.
overconfidence in incorrect responses. The results underscore
that while existing benchmarks may no longer provide a

### B. MMLU Benchmark

meaningful measure of progress, HLE serves as a critical
Measuring Massive Multitask Language Understanding tool for assessing the true academic reasoning capabilities of
(MMLU) [58] is a comprehensive benchmark designed by LLMs, potentially heralding a new era in benchmark design
Hendrycks et al. (2021) to evaluate large language models as the field moves toward more challenging and nuanced
across a diverse range of subjects, from elementary mathe- evaluations in the pursuit of artificial general intelligence.
maticstoprofessionallaw.Thebenchmarkcomprises57tasks
that test models’ ability to apply broad world knowledge and
problem-solving skills in zero-shot and few-shot settings, em- E. FACTS Grounding benchmark
phasizinggeneralizationwithouttask-specificfine-tuning.The Google DeepMind introduced FACTS Grounding [61], a
studyalsouncoverschallengesrelatedtomodelcalibrationand comprehensive benchmark designed to evaluate how accuthe imbalance between procedural and declarative knowledge, rately LLMs ground their long-form responses in provided
highlighting critical areas where current models fall short of source documents while avoiding hallucinations. The benchexpert-level proficiency. mark comprises 1,719 meticulously crafted examples split
into 860 public and 859 private cases that require models to
C. ComplexFuncBench Benchmark generate detailed answers strictly based on a corresponding
context document, with inputs reaching up to 32,000 tokens.

### Zhong et al. [59] introduced ComplexFuncBench, a novel

Covering diverse domains such as medicine, law, technology,
benchmark designed to evaluate large language models
finance, and retail, FACTS Grounding excludes tasks that re-
(LLMs) on complex function calling tasks in real-world setquire creativity, mathematics, or complex reasoning, focusing
tings. Unlike previous benchmarks, ComplexFuncBench chalsquarely on factual accuracy and information synthesis. To
lenges models with multi-step operations within a single turn,
ensure robust and unbiased evaluation, responses are assessed
adherencetouser-imposedconstraints,reasoningoverimplicit
in two phases: eligibility and factual grounding using a panel
parameter values, and managing extensive input lengths that
of three frontier LLM judges (Gemini 1.5 Pro, GPT-4o,
canexceed500tokens,includingscenarioswithacontextwinand Claude 3.5 Sonnet), with final scores derived from the
dowofupto128ktokens.Complementingthebenchmark,the
aggregation of these assessments. With an online leaderboard
authorspresentanautomaticevaluationframework,ComplexhostedonKagglealreadypopulatedwithinitialresultswhere,
Eval, which quantitatively assesses performance across over
for instance, Gemini 2.0 Flash leads with 83.6% accuracy
1,000 scenarios derived from five distinct aspects of function

### FACTS Grounding aims to drive industry-wide advancements

calling. Experimental results reveal significant limitations in
in grounding and factuality, ultimately fostering greater trust
current state-of-the-art LLMs, with closed models like Claude
and reliability in LLM applications.
3.5 and OpenAI’s GPT-4 outperforming open models such as
Qwen 2.5 and Llama 3.1. Notably, the study identifies prevalent issues, including value errors and premature termination F. ProcessBench benchmark
in multi-step function calls, underscoring the need for further
Qwen team [62] introduced ProcessBench, a novel benchresearch to enhance the function-calling capabilities of LLMs
mark specifically designed to evaluate the ability of language
in practical applications.
models to detect errors within the reasoning process for
mathematicalproblemsolving.ProcessBenchcomprises3,400

### D. Humanity’s Last Exam (HLE) Benchmark

test cases, primarily drawn from competition- and Olympiad-
Phanetal.[60]introducedHumanity’sLastExam(HLE),a level math problems, where each case includes a detailed,
benchmark designed to push the limits of LLMs by challeng- step-by-step solution with human-annotated error locations.
ing them with expert-level academic tasks. Unlike traditional Models are tasked with identifying the earliest erroneous step
benchmarkssuchasMMLU,whereLLMshaveachievedover or confirming that all steps are correct, thereby providing a

<!-- Page 9 -->

9
granular assessment of their reasoning accuracy. The bench- Additionally, this method offers substantial cost and time
mark is employed to evaluate two classes of models: process savings, reducing evaluation costs to approximately 2.29%
reward models (PRMs) and critic models, the latter involving ($30.58 vs. $1,297.50) and cutting evaluation time down to
general large language models (LLMs) that are prompted to 118.43 minutes compared to 86.5 hours for human assesscritique each solution step. Experimental results reveal two ments.
key findings. First, existing PRMs generally fail to generalize
to more challenging math problems beyond standard datasets I. JudgeBench Benchmark
like GSM8K and MATH, often underperforming relative to

### Tan et al. [65] proposed JudgeBench, a novel benchmark

both prompted LLM-based critics and a PRM fine-tuned on
designed to objectively evaluate LLM-based judges models
a larger, more complex PRM800K dataset. Second, the best
that are increasingly employed to assess and improve the
open-source model tested, QwQ-32B-Preview, demonstrates
outputs of large language models by focusing on their ability
error detection capabilities that rival those of the proprietary
toaccuratelydiscernfactualandlogicalcorrectnessratherthan
GPT-4o, although it still falls short compared to reasoningmerelyaligningwithhumanstylisticpreferences.Unlikeprior
specialized models like o1-mini.
benchmarksthatrelyprimarilyoncrowdsourcedhumanevaluations,JudgeBenchleveragesacarefullyconstructedsetof350
G. OmniDocBench Benchmark challenging response pairs spanning knowledge, reasoning,
Ouyang et al. [63] introduced OmniDocBench, a compre- math, and coding domains. The benchmark employs a novel
hensive multi-source benchmark designed to advance auto- pipeline to transform challenging existing datasets into paired
mated document content extraction a critical component for comparisonswithpreferencelabelsbasedonobjectivecorrecthigh-quality data needs in LLMs and RAG systems. Om- nesswhilemitigatingpositionalbiasthroughdoubleevaluation
niDocBench features a meticulously curated and annotated with swapped order. Comprehensive testing across various
dataset spanning nine diverse document types including aca- judge architectures, including prompted, fine-tuned, multidemicpapers,textbooks,slides,notes,andfinancialdocuments agent judges, and reward models, reveals that even strong
and utilizes a detailed evaluation framework with 19 layout models,suchasGPT-4o,oftenperformonlymarginallybetter
categories and 14 attribute labels to facilitate multi-level as- thanrandomguessing,particularlyontasksrequiringrigorous
sessments.Throughextensivecomparativeanalysisofexisting errordetectioninintermediatereasoningsteps.Moreover,finemodular pipelines and multimodal end-to-end methods, the tuning can significantly boost performance, as evidenced by
benchmarkrevealsthatwhilespecializedmodels(e.g.,Nougat) a 14% improvement observed in Llama 3.1 8B, and reward
outperform general vision-language models (VLMs) on stan- models achieve accuracies in the 59–64% range.
darddocuments,generalVLMsexhibitsuperiorresilienceand
adaptability in challenging scenarios, such as those involving J. SimpleQA Benchmark
fuzzy scans, watermarks, or colorful backgrounds. Moreover, SimpleQA [66] is a benchmark introduced by OpenAI to
fine-tuning general VLMs with domain-specific data leads to assess and improve the factual accuracy of large language
enhanced performance, as evidenced by high accuracy scores models on short, fact-seeking questions. Comprising 4,326
intaskslikeformularecognition(withmodelssuchasGPT-4o, questions spanning domains such as science/tech, politics,
Mathpix, and UniMERNet achieving around 85–86.8% accu- art, and geography, SimpleQA challenges models to deliver a
racy) and table recognition (RapidTable at 82.5%). Nonethe- single correct answer under a strict three-tier grading system
less, the findings also highlight persistent challenges, notably (”correct,” ”incorrect,” or ”not attempted”). While built on
thatcomplexcolumnlayoutscontinuetodegradereadingorder foundationaldatasetssuchasTriviaQAandNaturalQuestions,
accuracy across all evaluated models. SimpleQA presents a more challenging task for LLMs. Early
results indicate that even advanced models, such as OpenAI
H. Agent-as-a-Judge o1-preview, achieve only 42.7% accuracy (with Claude 3.5
Sonnet trailing at 28.9%), and models tend to exhibit over-

### Meta team proposed the Agent-as-a-Judge framework [64],

confidenceintheirincorrectresponses.Moreover,experiments
an innovative evaluation approach explicitly designed for
that repeated the same question 100 times revealed a strong
agentic systems that overcome the limitations of traditional
correlation between higher answer frequency and overall acmethods, which either focus solely on outcomes or require
curacy.Thisbenchmarkthusprovidescriticalinsightsintothe
extensive manual labor. This framework provides granular,
current limitations of LLMs in handling straightforward, facintermediate feedback throughout the task-solving process by
tual queries. It underscores the need for further improvements
leveraging agentic systems to evaluate other agentic systems.
in grounding model outputs in reliable, factual data.
The authors demonstrate its effectiveness on code generation
tasks using DevAI, a new benchmark comprising 55 real-

### K. FineTasks

istic automated AI development tasks annotated with 365
hierarchical user requirements. Their evaluation shows that FineTasks [67] is a data-driven evaluation framework de-
Agent-as-a-Judge not only dramatically outperforms the con- signed to systematically select reliable tasks for assessing
ventionalLLM-as-a-Judgeapproach(whichtypicallyachieves LLMs across diverse languages. Developed as the first step
a 60–70% alignment rate with human assessment) but also toward the broader FineWeb Multilingual initiative, Finereaches an impressive 90% alignment with human judgments. Tasks evaluates candidate tasks based on four critical metrics:

<!-- Page 10 -->

10
TABLE IV: LLM Benchmark Comparison: Multimodal, Task Diversity, Reasoning & Agentic AI Evaluation
Benchmark Year Multimodal Task Diversity Reasoning AgenticAI
DROP[82] 2019 No Englishdiscretereasoningcomprehension High High No

### MMLU[58] 2020 No Academic/generalknowledge High Moderate No

MATH[83] 2021 No Evaluatingmathematicalreasoning High High No
Codex[84] 2021 No EvaluatingLLMstrainedoncode Medium Medium No
MGSM[85] 2022 No Multilingualgrade-schoolmathproblems High High No
FACTSGrounding[61] 2023 No Factualgroundinginlongresponses High Low No

### SimpleQA[66] 2023 No FactualQ&A High Low No

PersonaGym[86] 2024 No Dynamicevaluationframeworkforpersonaagents High High Yes
FineTasks[67] 2023 No Multilingualtaskselection High Medium No

### GAIA[78] 2023 Yes GeneralAIassistanttasks High High No

OmniDocBench[63] 2024 Yes Documentcontentextraction High Medium No
ProcessBench[62] 2024 No Errordetectioninmathsolutions Low High No
MIRAI[87] 2024 No Evaluatingllmagentsforeventforecasting High High Yes
AppWorld[88] 2025 No BenchmarkingInteractiveCodingAgents High High Yes
VisualAgentBench[89] 2024 Yes BenchmarkforevaluatingLargeMultimodalModels High High Yes
ScienceAgentBench[90] 2024 No EvaluationoflanguageagentsforScientificDiscovery High High Yes
Agent-SafetyBench[91] 2024 No SafetyevaluationofLLMagents High High Yes
DiscoveryBench[92] 2024 No Data-DrivenDiscovery High High Yes
BLADE[93] 2024 No Benchmarkfordata-drivenscientificdiscovery High High Yes
Dyn-VQA[8] 2024 Yes AdaptiveVQAmultimodalbenchmark High High Yes
Agent-as-a-Judge[64] 2024 No Codegenerationevaluation Low Low Yes
JudgeBench[65] 2024 No EvaluationofLLM-basedjudges High High No

### FRAMES[68] 2024 No Factuality&retrievalforRAG High High No

MedChain[94] 2024 No Interactiveclinicaldecisionadaptation High High Yes
CRAG[72] 2024 No FactualQ&AforRAGsystems High High No
DIA[74] 2024 Yes Dynamicproblemsolving High High No

### CyberMetric[75] 2024 No CybersecurityQ&A Low Low No

TeamCraft[95] 2024 Yes CollaborativeMinecraftmultimodalevaluation High High Yes
AgentHarm[96] 2024 No LLMjailbreakrobustnessevaluation High High Yes
τ-bench[81] 2024 No ConversationalAgentEvaluation High High Yes
LegalAgentBench[97] 2024 No EvaluatingLLMAgentsinLegalDomain High High Yes

### GPQA[98] 2024 No Biology,physics,andchemistry High High No

ENIGMAEVAL[57] 2025 Yes Complexmultimodalpuzzles Low High No
ComplexFuncBench[59] 2025 No Functioncallingtasks Medium High No
MedAgentsBench[99] 2025 No Complexmedicalreasoning&treatmentplanning High High Yes
Humanity’sLastExam[60] 2025 Yes Expert-levelacademictasks High High No
DABStep[69] 2025 No Step-basedmulti-stepreasoning Low High No

### BFCLv2[70] 2025 No Functioncallingevaluation High High No

SWE-Lancer[71] 2025 No Freelancesoftwareengineeringtasks High Moderate No
OCCULT[73] 2025 No Cybersecurityoperationaltasks Medium High No
BIG-BenchExtraHard[76] 2025 No Challengingreasoningtasks High High No
MultiAgentBench[77] 2025 Yes Multi-agentcoordinationtasks High High Yes
CASTLE[79] 2025 No Softwarevulnerabilitydetection Low Medium No
EmbodiedEval[100] 2025 Yes 3Dembodiedtasksbenchmark Medium High Yes
SPIN-Bench[80] 2025 Yes Strategicplanning&socialreasoning High High Yes
OlympicArena[101] 2025 Yes Olympiccompetitionproblems Medium High No
SciReplicate-Bench[102] 2025 No Algorithm-drivencodegeneration High High Yes
EconAgentBench[103] 2025 No Decision-makingtasksineconomicenvironments High High Yes
VeriLA[104] 2025 No Human-centeredLLMfailureverification High High Yes
CapaBench[105] 2025 No EvaluationofmodularcontributionsinLLMagents High High Yes
AgentOrca[106] 2025 No Dual-systemagentcomplianceevaluation High High Yes
ProjectEval[107] 2025 No Project-levelcodegenerationevaluation Medium High Yes
RefactorBench[108] 2025 No Autonomousmulti-filerefactoringevaluation High High Yes
BEARCUBS[109] 2025 Yes Multimodalwebagentsevaluation High Medium Yes
Robotouille[110] 2025 No AsynchronousPlanningBenchmark High High Yes
DSGBench[111] 2025 No Strategicgamesdecisionevaluation Medium High Yes
TheoremExplainBench[112] 2025 Yes STEMtheoremanimationvideos Medium High Yes
RefuteBench2.0[113] 2025 No Multi-turnLLMfeedbackevaluation High High Yes

### MLGym[114] 2025 Yes MLagentsautomateresearch High High Yes

DataSciBench[115] 2025 No LLMDataScienceBenchmark High High Yes
EmbodiedBench[116] 2025 Yes Vision-drivenembodiedagentevaluation High High Yes
BrowseComp[117] 2025 No BenchmarkforBrowsingAgents High High Yes
Vending-Bench[118] 2025 No Long-horizonbusinesssimulation Medium High Yes
MLE-bench[119] 2025 No MLengineering-relatedcompetitionsfromKaggle Medium High Yes
SWE-PolyBench[120] 2025 No Evaluationofcodingagents High High Yes
Multi-SWE-bench[121] 2025 No MultilingualBenchmarkforIssueResolving High High No

<!-- Page 11 -->

11
monotonicity,lownoise,non-randomperformance,andmodel improvements, experimental results reveal that even the bestordering consistency to ensure robustness and reliability. In performing model under this framework only achieves a 16%
an extensive study, the Hugging Face team tested 185 candi- success rate on the evaluated tasks. This modest accuracy undate tasks across nine languages (including Chinese, French, derscores the significant challenges that remain in effectively
Arabic, Russian, Thai, Hindi, Turkish, Swahili, and Telugu), trainingmodelsforcomplex,iterativereasoningandhighlights
ultimately selecting 96 final tasks that cover domains such the need for further research and optimization.
as reading comprehension, general knowledge, language understanding, and reasoning. The work further reveals that the

### N. BFCL v2 benchmark

formulation of tasks has a significant impact on performance;

### Mao et al. [70] propose BFCL v2, a novel benchmark and

for instance, Cloze format tasks are more effective during
leaderboarddesignedtoevaluatelargelanguagemodels’funcearly training phases, while multiple-choice formats yield
tion calling abilities using real-world, user-contributed data.
better evaluation results. Recommended evaluation metrics

### The benchmark comprises 2,251 question-function-answer

include length normalization for most tasks and pointwise
pairs, enabling comprehensive assessments across a range of
mutual information (PMI) for complex reasoning challenges.
scenarios from multiple and straightforward function calls to

### Benchmarking35openandclosed-sourceLLMsdemonstrated

parallel executions and irrelevance detection. By leveraging
that open models are narrowing the gap with their proprietary
authentic user interactions, BFCL v2 addresses prevalent iscounterparts,withQwen2modelsexcellinginhigh-andmidsues such as data contamination, bias, and limited generresource languages and Gemma-2 particularly strong in lowalization in previous evaluation methods. Initial evaluations
resourcesettings.Moreover,theFineTasksframeworksupports
reveal that models like Claude 3.5 and GPT-4 consistently
over 550 tasks across various languages, providing a scalable
outperform others, with Mistral, Llama 3.1 FT, and Gemini
and comprehensive platform for advancing multilingual large
following in performance. However, some open models, such
language model (LLM) evaluation.
asHermes,struggleduetopotentialpromptingandformatting
challenges. Overall, BFCL v2 offers a rigorous and diverse
L. FRAMES benchmark platform for benchmarking the practical capabilities of LLMs
in interfacing with external tools and APIs, thereby providing

### Google team [68] propose FRAMES (Factuality, Retrieval,

valuable insights for future advancements in function calling
andReasoningMEasurementSet),acomprehensiveevaluation
and interactive AI systems.
dataset specifically designed to assess the capabilities of
retrieval-augmentedgeneration(RAG)systemsbuiltonLLMs.
FRAMES addresses a critical need by unifying evaluations of O. SWE-Lancer benchmark
factual accuracy, retrieval effectiveness, and reasoning abil-

### OpenAI team [71] presents SWE-Lancer, an innovative

ity in an end-to-end framework, rather than assessing these
benchmark comprised of over 1,400 freelance software engifacets in isolation. The dataset comprises 824 challenging
neering tasks collected from Upwork, representing more than
multi-hopquestionsspanningdiversetopics,includinghistory,
$1 million in real-world payouts. This benchmark encomsports, science, and health, each requiring the integration of
passesbothindependentengineeringtasks,rangingfromminor
information from between two and fifteen Wikipedia articles.
bug fixes to substantial feature implementations valued up to
By labeling questions with specific reasoning types, such as
$32,000, and managerial tasks, where models must select the
numericalortabular.FRAMESprovidesanuancedbenchmark
besttechnicalproposals.Independenttasksarerigorouslyevalto identify the strengths and weaknesses of current RAG
uated using end-to-end tests that have been triple-verified by
implementations. Baseline experiments reveal that state-ofexperiencedengineers.Atthesametime,managerialdecisions
the-art models like Gemini-Pro-1.5-0514 achieve only 40%
are benchmarked against the selections made by the original
accuracy when operating without retrieval mechanisms, but
hiring managers. Experimental results indicate that state-oftheir performance increases significantly to 66% with a multithe-art models, such as Claude 3.5 Sonnet, still struggle with
step retrieval pipeline, representing a greater than 50% imthe majority of these tasks, achieving a 26.2% pass rate on
provement.
independent tasks and 44.9% on managerial tasks, which
translatestoanestimatedearningof$403Kafigurewellbelow
the total available value. Notably, the analysis highlights that

### M. DABStep benchmark

while models tend to perform better in evaluative managerial

### DabStep [69] is a new framework from Hugging Face that

rolesthanindirectcodeimplementation,increasinginferencepioneers a step-based approach to enhance the performance
time computing can enhance performance.
and efficiency of language models on multi-step reasoning
tasks. DabStep addresses the challenges of traditional end-

### P. Comprehensive RAG Benchmark (CRAG)

to-end inference by decomposing complex problem-solving
into discrete, manageable steps, enabling models to refine Yang et al. [72] propose the Comprehensive RAG Benchtheiroutputsthroughstep-levelfeedbackanditerativedynamic mark(CRAG),anoveldatasetdesignedtoevaluatethefactual
adjustments.Thismethodisdesignedtoenablemodelstoself- question-answering capabilities of Retrieval-Augmented Gencorrect and navigate the complexities of multi-step reasoning eration systems rigorously. CRAG comprises 4,409 questionprocesses more effectively. However, despite these innovative answer pairs across five domains and eight distinct question

<!-- Page 12 -->

12
categories. It incorporates mock APIs to simulate web and S. CyberMetric benchmark
KnowledgeGraphretrieval,therebyreflectingthevariedlevels

### Tihanyi et al. [75] introduces a suite of novel

of entity popularity and temporal dynamism encountered in
multiple-choice Q&A benchmark datasets CyberMetric-80,
real-world scenarios. Empirical results show that state-of-the-
CyberMetric-500, CyberMetric-2000, and CyberMetric-10000
art large language models without grounding achieve only
designed to evaluate the cybersecurity knowledge of LLMs
around34%accuracyonCRAG,andthatincorporatingsimple
rigorously. By leveraging GPT-3.5 and Retrieval-Augmented
RAG methods improves this to just 44%, whereas industry-

### Generation (RAG), the authors generated questions from

leading RAG systems can reach 63% accuracy without haldiversecybersecuritysourcessuchasNISTstandards,research
lucination. The benchmark also highlights significant perforpapers, publicly accessible books, and RFCs. Complete with
mance drops for questions involving highly dynamic, lowerfour possible answers, each question underwent extensive
popularity, or more complex facts. Notably, CRAG focuses
rounds of error checking and refinement, with over 200 hours
solely on evaluating the generative component of the RAG
of human expert validation to ensure accuracy and domain
pipeline, and early findings indicate that Llama 3 70B nearly
relevance. Evaluations were conducted on 25 state-of-the-art
matches GPT-4 Turbo across these tasks.
large language models (LLMs), and the results were further
benchmarked against human performance on CyberMetric-80
in a closed-book scenario. Findings reveal that models like

### Q. OCCULT Benchmark

GPT-4o, GPT-4-turbo, Mixtral-8x7 B-Instruct, Falcon-180

### Kouremetis et al. [73] present OCCULT, a novel and


### B-Chat, and GEMINI-pro 1.0 exhibit superior cybersecurity

lightweight operational evaluation framework that rigorously
understanding, outperforming humans on CyberMetric-80,
measures the cybersecurity risks associated with using large
while smaller models such as Llama-3-8B, Phi-2, and
language models (LLMs) for offensive cyber operations
Gemma-7b lag behind, underscoring the value of model scale
(OCO).Traditionally,evaluatingAIincybersecurityhasrelied
and domain-specific data in this challenging field.
onsimplistic,all-or-nothingtestssuchascapture-the-flagexercises, which fail to capture the nuanced threats faced by moderninfrastructure.Incontrast,OCCULTenablescybersecurity T. BIG-Bench Extra Hard
experts to craft repeatable and contextualized benchmarks by A team from Google DeepMind [76] addresses a critical
simulatingreal-worldthreatscenarios.Theauthorsdetailthree gap in evaluating large language models by tackling the limidistinct OCO benchmarks designed to assess the capability tationsofcurrentreasoningbenchmarks,whichhaveprimarily
of LLMs to execute adversarial tactics, providing preliminary focused on mathematical and coding tasks. While the BIG-
evaluation results that indicate a significant advancement in Benchdataset[122]anditsmorecomplexvariant,BIG-Bench
AI-enabled cyber threats. Most notably, the DeepSeek-R1 Hard (BBH) [123], have provided comprehensive assessments
modelcorrectlyansweredover90%ofquestionsintheThreat of general reasoning abilities, recent advances in LLMs have
Actor Competency Test for LLMs (TACTL). led to saturation, with state-of-the-art models achieving nearperfect scores on many BBH tasks. To overcome this, the
authors introduce BIG-Bench Extra Hard (BBEH). This novel

### R. DIA benchmark

benchmark replaces each BBH task with a more challenging
Dynamic Intelligence Assessment (DIA) [74] is introduced variant designed to probe similar reasoning capabilities at an
as a novel methodology to more rigorously test and compare elevated difficulty level. Evaluations on BBEH reveal that
the problem-solving abilities of AI models across diverse do- eventhebestgeneral-purposemodelsonlyachieveanaverage
mains such as mathematics, cryptography, cybersecurity, and accuracy of 9.8%, while reasoning-specialized models reach
computer science. Unlike traditional benchmarks that rely on 44.8%, highlighting substantial room for improvement and
static question-answer pairs often allowing models to perform underscoring the ongoing challenge of developing LLMs with
uniformlywellorrelyonmemorizationDIAemploysdynamic robust, versatile reasoning skills.
question templates with mutable parameters, presented in
variousformatsincludingtext,PDFs,compiledbinaries,visual

### U. MultiAgentBench benchmark

puzzles,andCTF-stylechallenges.Thisframeworkalsointroduces four innovative metrics to evaluate a model’s reliability Zhu et al. [77] introduce MultiAgentBench, a benchmark
and confidence across multiple attempts, revealing that even specifically designed to evaluate the capabilities of multisimple questions are frequently answered incorrectly when agent systems powered by LLMs in dynamic, interactive
posed in different forms. Notably, the evaluation shows that environments. Unlike traditional benchmarks that focus on
while API models like GPT-4o may overestimate their math- single-agent performance or narrow domains, MultiAgentematical capabilities, models such as ChatGPT-4o perform Bench encompasses six diverse domains, including research
betterduetopracticaltoolusage,andOpenAI’so1-miniexcels proposal writing, Minecraft structure building, database error
in self-assessment of task suitability. Testing 25 state-of-the- analysis, collaborative coding, competitive Werewolf gameartLLMswithDIA-Benchrevealssignificantgapsinhandling play, and resource bargaining to measure both task complecomplex tasks and in adaptive intelligence, establishing a new tion and the quality of agent coordination using milestonestandardforevaluatingbothproblem-solvingperformanceand based performance indicators. The study investigates various
a model’s ability to recognize its own limitations. coordination protocols, such as star, chain, tree, and graph

<!-- Page 13 -->

13
topologies, and finds that direct peer-to-peer communication performance bottlenecks in current large language models
and cognitive planning are particularly effective evidenced by (LLMs), which, while adept at factual retrieval and shorta 3% improvement in milestone achievement when planning range planning, struggle with deep multi-hop reasoning, spais employed while also noting that adding more agents can tial inference, and socially coordinated decision-making. For
decrease performance. Among the models evaluated (GPT- instance,modelsperformreasonablywellonsimpletaskslike
4o-mini, 3.5, and Llama), GPT-4o-mini achieved the highest Tic-Tac-ToebutfalterincomplexenvironmentssuchasChess
average task score, and graph-based coordination protocols or Diplomacy, and even the best models achieve only around
outperformed other structures in research scenarios. 58.59% accuracy on classical planning tasks.

### V. GAIA Benchmark Y. τ-bench

GAIA [78] is a groundbreaking benchmark designed to Yao et al. [81] present τ-bench, a benchmark designed
assess General AI Assistants on real-world questions that to evaluate language agents in realistic, dynamic, multi-turn
tap into fundamental abilities like reasoning, multi-modality conversational settings that emulate real-world environments.
handling, web browsing, and tool use. Unlike traditional In τ-bench, agents are challenged to interact with a simulated
benchmarksthatfocusonincreasinglyspecializedtasks,GAIA user to understand needs, utilize domain-specific API tools
features conceptually simple questions solvable by humans (such as booking flights or returning items), and adhere to
at 92% accuracy that current systems, such as GPT-4 with providedpolicyguidelines,whileperformanceismeasuredby
plugins, struggle with, achieving only 15%. Comprising 466 comparingthefinaldatabasestatewithanannotatedgoalstate.
meticulously curated questions with reference answers, GAIA A novel metric, passk, is introduced to assess reliability over
shiftstheevaluationparadigmtowardmeasuringAIrobustness multiple trials. Experimental findings reveal that even statein everyday reasoning tasks, a critical step toward achieving of-the-art function-calling agents like GPT-4o succeed on less
true Artificial General Intelligence (AGI). This substantial than50%oftasks,withsignificantinconsistency(forexample,
performance gap between humans and state-of-the-art models pass8 scoresbelow25%inretaildomains)andmarkedlylower
emphasizes the need for AI systems that can mimic the success rates for tasks requiring multiple database writes.
general-purpose, resilient reasoning exhibited by average hu- These results underscore the need for enhanced methods that
man problem solvers. improveconsistency,adherencetorules,andoverallreliability
in language agents for real-world applications.

### W. CASTLE Benchmark


### Z. Discussion and Comparison of LLM Benchmarks


### Dubniczky et al. [79] introduce CASTLE, a novel bench-

TableIVpresentsanextensiveoverviewofbenchmarksdemarking framework for evaluating software vulnerability
velopedfrom2019to2025forevaluatinglargelanguagemoddetection methods, addressing existing approaches’ critical
els (LLMs) concerning multimodal capabilities, task scope,
weaknesses. CASTLE assesses 13 static analysis tools, 10
diversity,reasoning,andagenticbehaviors.Earlybenchmarks,
LLMs, and two formal verification tools using a meticulously
such as DROP [82], MMLU [58], MATH [83], Codex [84],
curated dataset of 250 micro-benchmark programs that cover
MGSM [85], FACTS Grounding [61], and SimpleQA [66],
25commonCWEs.Theframeworkproposesanewevaluation
concentrated on core competencies like discrete reasoning,
metric, the CASTLE Score, to enable fair comparisons across
academic knowledge, mathematical problem solving, and facdifferentmethods.Resultsrevealthatwhileformalverification
tual grounding. These pioneering efforts lay the groundwork
toolslikeESBMCminimizefalsepositives,theystrugglewith
for performance evaluation in language understanding and
vulnerabilitiesbeyondthescopeofmodelchecking.Staticanreasoning tasks, setting a baseline against which later, more
alyzers often generate excessive false positives, which burden
sophisticated benchmarks have been compared.
developers with manual validation. LLMs perform strongly

### A notable progression in benchmark design is observed

on small code snippets; however, their accuracy declines, and
with the emergence of frameworks that target more complex
hallucinations increase as code size grows. These findings
agentic and multimodal tasks. For instance, PersonaGym [86]
suggestthat,despitecurrentlimitations,LLMsholdsignificant
and FineTasks [67] introduce dynamic persona evaluation and
promise for integration into code completion frameworks,
multilingual task selection. GAIA [78] expands the evaluative
providing real-time vulnerability prevention and marking an
scopetogeneralAIassistanttaskswhileOmniDocBench[63]
important step toward more secure software systems.
and ProcessBench [62] address document extraction and error
detection in mathematical solutions. Further, MIRAI [87],

### X. SPIN-Bench Benchmark


### AppWorld [88], VisualAgentBench [89], and ScienceAgent-

Yaoetal.[80]introduceacomprehensiveevaluationframe- Bench[90]explorevariousfacetsofmultimodalandscientific
work, SPIN-Bench, highlighting the challenges of strategic discovery tasks. This decade-spanning evolution is compleplanning and social reasoning in AI agents. Unlike traditional mented by additional evaluations focusing on safety (Agentbenchmarks focused on isolated tasks, SPIN-Bench combines SafetyBench [91]), discovery (DiscoveryBench [92]), code
classical planning, competitive board games, cooperative card generation (BLADE [93], Dyn-VQA [8], and Agent-as-agames,andnegotiationscenariostosimulatereal-worldsocial Judge[64]),judicialreasoning(JudgeBench[65]),andclinical
interactions. This multifaceted approach reveals significant decision making (MedChain [94]), among others including

<!-- Page 14 -->

14
Multi- Fin [ e 6 T 7 a ] sks Em [ b 1 o 1 d 6 i ] edBencEhm [ b 1 o 0 d 0 i ] edEval BEARCUBS

## Swe- Enigmaeval [109]

b [1 e 2 n 1 ch ] [57] Oly [ m 10 p 1 ic ] Arena
TheoremExplainBench
[112]

## Dia

[74]
VisualAgentBench
[89]
Dyn-VQA
[8]

### Multimodal,


### Task Visual&

Tea [ m 95 C ] raft Judg [6 eB 5] ench BLADE Selection E E v m al b u o a d ti i o e n d s Omn [6 iD 3] ocBench EconAgentBench

### AgentHarm [93] [103]

[96] DiscoveryBench OCCULT

## [92] Gaia [73]

τ-bench [78]
[81] Sa A fe [ g t 9 y e 1 B n ] t e - nch Cyb [ e 7 r 5 M ] etric
MultiAgentBench
[77]
ScienceAgentBench MedAgentsBench
[90] [99]

## Spin-


### Bench Agentic& Domain-

[80] Interactive Specific
Evaluations M [ I 8 R 7 A ] I Evaluations Lega [9 lA 7] gentBench
VeriLA
[104]
PBerroswosneaCGoymmp MedChain
[[18167]] [94]
CapaBench
[105]
DataSciBench
[115]

### Ag [ e 1 n 0 t 6 O ] rca MLGym LLMBenchmark

Rob [1 o 1 to 0 u ] ille DSGBench Refu 2 te .0 Bench [114]
[111] [113]

## Drop Gpqa

[82] Academic [98]
& Factual

### General Grounding

M [ M 58 L ] U K R n e o a w so l n e i d n g g e Retr & ieval C [ R 7 A 2] G
B Ex IG tr [ - a 7 B 6 H e ] n a c rd h FR [ A 6 M 8] ES

### BFCLv2

H L u as m [ t 6 a E 0 n x ] it a y m ’s [70] Sim [ p 6 l 6 e ] QA
DA [ B 69 S ] tep Com [5 p 9 le ] xFuncBench G F ro A [ u 6 C n 1 T d ] i S ng

### Mathematical Code&


### Problem Software MLE-

Solving Engineering bench
[119]
Codex
[84]

## Swe-


### PolyBench

Agent-as- [120]
a-Judge

## [64] Castle

[79]

### MATH AppWorld


## [83] [88] Swe-

M [ G 85 S ] M Proc [ e 6 s 2 s ] Bench Sci B R [1 e e 0 n p 2 c l ] h icate- Pro [ j 1 e 0 ct 7 E ] val Ref [ a 1 c 0 to 8 r ] Bench L [ a 7 n 1 c ] er
Fig. 2: Classification of LLM Benchmarks for AI Agents Applications
FRAMES [68], CRAG [72], DIA [74], CyberMetric [75], TheoremExplainBench [112], RefuteBench 2.0 [113], ML-
TeamCraft [95], AgentHarm [96], τ-bench [81], LegalAgent- Gym [114], DataSciBench [115], EmbodiedBench [116],
Bench [97], and GPQA [98]. BrowseComp[117],andMLE-bench[119].Collectively,these
benchmarks exemplify the field’s shift towards more compre-
Recent benchmarks from 2025 further indicate a subhensive and nuanced evaluation metrics, supporting the destantial expansion in the depth and breadth of large lanvelopment of LLMs that can tackle increasingly multifaceted,
guage model (LLM) evaluations. ENIGMAEVAL [57] and
real-world challenges.
ComplexFuncBench [59] target complex puzzles and func-

### Fig.2groupsbenchmarksintocategoriessuchasAcademic

tion calling tasks, while MedAgentsBench [99] and Hu-
& General Knowledge Reasoning, Mathematical Problem
manity’s Last Exam [60] focus on advanced medical rea-

### Solving, Code & Software Engineering, Factual Grounding

soning and expert-level academic tasks. Additional bench-
& Retrieval, Domain-Specific Evaluations, Multimodal/Visual
marks such as DABStep [69], BFCL v2 [70], SWE-
& Embodied Evaluations, Task Selection, and Agentic &

### Lancer [71], and OCCULT [73] further diversify evalua-


### InteractiveEvaluations,illustratingthefullrangeoftasksused

tive criteria by incorporating multi-step reasoning, cyberseto assess LLMs in AI agent settings.
curity, and freelance software engineering challenges. The
table also includes BIG-Bench Extra Hard [76], MultiA-
gentBench [77], CASTLE [79], EmbodiedEval [100], SPIN-

## Iv. Aiagents


### Bench [80], OlympicArena [101], SciReplicate-Bench [102],

EconAgentBench [103], VeriLA [104], CapaBench [105], ThissectionpresentsacomprehensiveoverviewofAIagent
AgentOrca [106], ProjectEval [107], RefactorBench [108], frameworks and applications developed between 2024 and
BEARCUBS [109], Robotouille [110], DSGBench [111], 2025, highlighting transformative approaches that integrate

<!-- Page 15 -->

15
TABLE V: Overview of AI Agent Frameworks: Core Concepts, Workflow, and Advantages

### AgentFramework CoreIdea Workflow&Components KeyAdvantages

LangChain[124] IntegratesLLMswithdiversetoolstobuild CombinesconversationalLLMs,search Customizablerolesandstreamlinedagent
autonomousagents. integrations,andutilityfunctionsinto prototyping.
iterativeworkflows.
LlamaIndex[125] Enablesautonomousagentcreationvia WrapsfunctionsintoFunctionTool Simplifiesagentdevelopmentwitha
externaltoolintegration. objectsandemploysaReActAgentfor dynamic,modularpipeline.
stepwisetoolselection.
CrewAI[126] OrchestratesteamsofspecializedAIagents StructuressystemsintoCrew(oversight),AI Mimicshumanteamcollaborationwith
forcomplextasks. Agents(specializedroles),Process flexible,parallelworkflows.
(collaboration),andTasks(assignments).
Swarm[127] Providesalightweight,statelessabstraction Definesmultipleagentswithspecific Fine-grainedcontrolandcompatibilitywith
formulti-agentsystems. instructionsandroles;enablesdynamic variousbackends.
handoffsandcontextmanagement.
GUIAgent[128] Facilitatescomputercontrolvianatural Translatesuserinstructionsandscreenshots Demonstratesend-to-endperformancein
languageandvisualinputs. intodesktopactions(e.g.,cursormovements, real-worlddesktopworkflows.
clicks).
AgenticReasoning[129] Enhancesreasoningbyintegrating Leveragesweb-search,coding,andMind Achievesimprovedmulti-step
specializedexternaltool-usingagents. Mapagentstoiterativelyrefinemulti-step problem-solvingandstructuredknowledge
reasoning. synthesis.
OctoTools[130] EmpowersLLMsforcomplexreasoningvia Combinesstandardizedtoolcards,astrategic Outperformssimilarframeworksbyupto
training-freetoolintegration. planner,andanexecutorforeffectivetool 10.6%onvariedtasks.
usage.
AgentsSDK[131] Providesamodularframeworkforbuilding OfferscoreprimitivessuchasAgents(LLMs Streamlinesdevelopmentwithanextensible,
autonomousagentapplicationsthatintegrate withinstructions,tools,handoffs,and robustarchitecturethatenhances
LLMswithexternaltoolsandadvanced guardrails),Tools(wrappedfunctions/APIs), debuggabilityandscalability,enablingrapid
features. Contextforstatemanagement,alongwith prototypingandseamlessintegrationof
supportforStreaming,Tracing,and complex,multi-agentworkflows.
Guardrailstomanagemulti-turninteractions.
large language models with modular tools to achieve autonomous decision-making and dynamic multi-step reason-

### Thinking (Reasoning) & Utility Functions &

ing. The frameworks discussed include LangChain [124], Prompt (Instructions) Knowledge Store

### LlamaIndex [125], CrewAI [126], and Swarm [127], which

abstractcomplexfunctionalitiesintoreusablecomponentsthat
enable context management, tool integration, and iterative Strategy Development Task (Assigned AI Query Engines
(Planning) Objective)
refinement of outputs. Additionally, pioneering efforts in GUI
control [128] and agentic reasoning [129], [130] demonstrate
the increasing capabilities of these systems to interact with
external environments and tools in real-time. Knowledge Store

### Self-Evaluation Designated Function


### In parallel, this section presents a diverse range of AI

agent applications that span materials science, biomedical

### Agent Execution Environment

research, academic ideation, software engineering, synthetic
data generation, and chemical reasoning. Systems such as
Fig. 3: Core Elements of AI Agents.
the StarWhisper Telescope System [132] and HoneyComb
[133] have revolutionized operational workflows by automating observational and analytical tasks in materials science. In
large language models with modular tools and utilities to
the biomedical domain, platforms like GeneAgent [134] and
buildautonomoussoftwareagents.Theseframeworksabstract
frameworks such as PRefLexOR [135] demonstrate enhanced
complex functionalities such as natural language understandreliability through self-verification and iterative refinement.
ing, multi-step reasoning, and dynamic decision-making into
Moreover, innovative solutions for research ideation, exemreusable components that streamline prototyping, iterative
plified by SurveyX [136] and Chain-of-Ideas [137], as well
refinement, and deployment. By integrating advanced LLMs
as specialized frameworks for synthetic data generation [138]
with external tools and specialized functions, developers can
and chemical reasoning [139], collectively underscore the
create agents that process and generate language and adapt to
significant strides made in leveraging autonomous AI agents
complex workflows and diverse operational contexts [140].
for complex, real-world tasks. Table V presents an overview
Fig. 3 illustrates a comprehensive AI agent framework
of AI Agent frameworks.
where each component plays a crucial role in achieving
adaptive, autonomous decision-making. An assigned task is

### A. AI Agent frameworks

first approached through a designated function that defines
AI agent frameworks represent a transformative paradigm the agent’s role, followed by strategy development essentially
in developing intelligent systems, combining the power of the planning phase where the agent breaks down complex

<!-- Page 16 -->

16
Fig. 4: What are Agentic Workflows?.
objectives into actionable steps. This is supported by an
iterative thinking process, driven by reasoning and guided
by prompts, which enables the agent to reflect on its actions and refine its approach. Core operational support comes
from AI query engines and utility functions that interface
with an integrated knowledge store, ensuring that both static
and real-time information are readily accessible. Ultimately,
theseelementsoperatewithinanagentexecutionenvironment,
seamlessly combining planning, reasoning, and execution into Fig. 5: Agent-Driven RAG Framework.
a responsive and self-evolving system.

### Agentic workflows transform traditional, rigid processes

into dynamic, adaptive systems. As illustrated in Fig. 4, these its internal knowledge store to determine whether the query
workflows begin at the user interface, where a user query is has been addressed or needs more data. When necessary, the
submitted and receives a system reply. Unlike deterministic query is decomposed into smaller, manageable sub-questions
workflows that follow fixed, unchanging rules, an agent- that are individually routed and processed through retrieval
based process involves AI agents who actively formulate a utilities [142]. These utilities fetch relevant external data,
strategy,carryouttasksusingavailabletools,andevaluatethe and the system evaluates whether the retrieved information
outcomes. This cycle, ranging fromplanning to execution and is applicable before producing a final output. This layered,
ultimatelytoassessment,whereoutcomesaremarkedaseither agentic approach ensures that responses are accurate, contextsatisfactoryorunsatisfactory,empowersthesystemtorespond aware, and continuously refined throughout the process [143].
to real-world challenges more flexibly and autonomously Tab. VI demonstrates that retrieval-augmented generation
[141]. (RAG) is highly effective at producing up-to-date, accurate
Agentic Retrieval-Augmented Generation (RAG) integrates responses, making it ideal for fields like healthcare or law,
a language model’s advanced capabilities with dynamic data where precise, domain-specific information is critical. In conretrieval and processing. As shown in Fig. 5, the process trast, AI Agents distinguish themselves with their continubegins at the user interface, where a query is submitted ous learning and autonomous decision-making capabilities,
and a system reply is generated. The system first checks which make them adaptable to evolving contexts. When these

<!-- Page 17 -->

17
TABLE VI: Comparative Analysis of LLM Strategies in RAG, AI Agents, and Agentic RAG
Feature LLMPre-trained LLMPostTraining& RAG AIAgents AgenticRAG

### FineTuning

CoreFunction UsesLLMfortext Appliestask-specific Retrievesdataand Automatestasksand Integratesretrievalwith
generation. tuning. generatestext. decisions. adaptivereasoning.
Autonomy Basiclanguage Enhancesautonomy Limited;user-driven. Moderatelyautonomous. Highlyautonomous.
understanding. throughtuning.
Learning Reliesonpre-training. Usesfinetuningfor Staticpre-trained Incorporatesuser Adaptsusingreal-time
precision. knowledge. feedback. data.
UseCases Generalapplications. Domain-specific Q&A,summaries, Chatbots,automation, Complex
enhancements. guidance. workflow. decision-makingtasks.
Complexity Providesbaseline Addsrefined Simpleintegration. Moresophisticated. Highlycomplex.
complexity. capabilities.
Reliability Dependsonstatic Improvesconsistency Consistentforknown Mayvarywithdynamic Reliabilityboostedby
trainingdata. withupdates. queries. inputs. adaptivemethods.
Scalability Scaleswithmodelsize. Scaleswith Easilyscalableforstatic Scalesmoderatelywith Scalableforcomplex
domain-specifictuning. tasks. addedfeatures. systems(withextra
resources).
Integration Easilyintegrablewith Requiresdomain Integrateswellwith Connectswith Supportsadvanced
variousapps. customization. retrievalsystems. operationalworkflows. decisionframeworks.
illustratesthearchitectureofaLangChain-poweredscheduling
Tools agentthatprocessesemailrequeststoperformcalendar-related
operations [144]. Incoming emails are first parsed to extract
- initiateBooking relevant content and convert unstructured text into structured
- removeBooking
Email A f C er a r n a g y . o m u o b h o a o m k e a d a m m e i e n t e in @ g u w n i i t v h - - - c re h t e ri c e k v A e v B a o il o a k b in ili g ty s data. This data is then passed to the chat model, guided
guelma.dz sometime tomorrow? - dispatchBookingLink
- modifyBooking by a contextual prompt that defines the assistant’s role. The
agent uses a scratchpad to reason through the request and
determine the appropriate tool from a predefined set (such as

### Email B

Tool checkAvailability, initiateBooking, or modifyBooking). These
Agent Chat Model checkAvailability tools interact with the backend booking API to execute the
requested actions, enabling seamless AI-driven scheduling.
You are a bleeding-edge 2) LlamaIndex: TheLlamaIndexframework[125]provides
scheduling assistant that
interfaces via email...etc. a powerful and flexible platform for building autonomous AI
Email Parser - - . . . . . . . for B A o P ok I ings agents by seamlessly integrating large language models with
external tools. In this framework, a basic AI agent is defined
Convert unstructured email asasemi-autonomoussoftwarecomponentthatreceivesatask
content into structured data
for easier processing and Scratchpad and a set of tools ranging from simple Python functions to
automation. Prompting
complete query engines and iteratively selects the appropriate
tool to process each step of the task. To build such an
agent, developers first set up a clean Python environment
Fig. 6: Agent architecture using Langchain framework.
and install LlamaIndex along with necessary dependencies,
then configure an LLM (for example, GPT-4 via an API
key). Next, they wrap simple functions (such as addition and
two approaches are combined into Agentic RAG, the model multiplication) into FunctionTool objects that the agent can
benefits from RAG’s fact-based grounding and AI Agents’ call, and instantiate a ReActAgent with these tools. When
dynamic adaptability, resulting in a system that minimizes promptedwithatask,theagentevaluatesitsreasoningprocess,
errors and remains current by leveraging the best aspects of chooses a tool to execute the necessary operations, and loops
each methodology. through these steps until the final answer is generated. This
1) LangChain: LangChain [124] is a robust framework structured yet dynamic approach allows for the creation of
designed to simplify the development of autonomous AI customizable, agentic workflows capable of tackling complex
agentsbyseamlesslyintegratinglargelanguagemodelswitha tasks.
diverse array of tools and data sources. In LangChain, agents 3) CrewAI: CrewAI [126] is a framework designed to
combine prepackaged components, such as conversational orchestrate autonomous teams of AI agents, each with spelarge language models (LLMs), search engine integrations, cialized roles, tools, and objectives, to collaboratively tackle
and specialized utility functions, into coherent workflows that complex tasks. The system is organized around four key
enable multi-step reasoning and decision-making. Developers components: the Crew, which oversees the overall operation
can build custom agents by defining specific roles, tasks, and workflow; AI Agents, which serve as specialized team
and tools, allowing the agent to analyze a given prompt, members such as researchers, writers, and analysts that make
select the appropriate tool for each subtask, and iteratively autonomous decisions and delegate tasks; the Process, which
refine its response until a final answer is produced. Fig. 6 managescollaborationpatternsandtaskassignmentstoensure

<!-- Page 18 -->

18
efficient execution; and Tasks, which are individual assign- ofLLMstocontrolcomputersviaGUI,whilealsoidentifying
ments with clear objectives that contribute to a larger goal. the need for more comprehensive, multimodal datasets to
Key features of CrewAI include role-based agent specializa- capture real-world complexities.
tion, flexible integration of custom tools and APIs, intelligent The paper by Sun et al. [145] tackles a major challenge
collaboration that mimics natural human interaction, and ro- in training GUI agents powered by Vision-Language Models
bust task management supporting both sequential and parallel (VLMs): collecting high-quality trajectory data. Traditional
workflows. Together, these elements enable the creation of methods relying on human supervision or synthetic data
dynamic, production-ready AI teams capable of achieving generation via pre-defined tasks are either resource-intensive
sophisticated, multi-step objectives in real-world applications. or fail to capture the complexity and diversity of real-world
4) Swarm: Swarm [127] is a lightweight, experimental environments. The authors propose OS-Genesis, a novel data
library from OpenAI designed to build and manage multi- synthesis pipeline that reverses the conventional trajectory
agent systems without relying on the Assistants API. Swarm collection process to overcome these limitations. Rather than
provides a stateless abstraction that orchestrates a continu- startingwithfixedtasks,OS-Genesisenablesagentstoexplore
ous loop of agent interactions, function calls, and dynamic environmentsthroughstep-by-stepinteractionsandthenderive
handoffs, offering fine-grained control and transparency. Key high-quality tasks retrospectively, with a trajectory reward
features include: model ensuring data quality.
6) Agentic Reasoning: Wu et al. [129] presents a novel
• Agent Definition: Developers can define multiple agents, framework that significantly enhances the reasoning capaeachequippedwithitsownsetofinstructions,designated
bilities of large language models by integrating external
role (e.g., ”Sales Agent”), and available functions, which
tool-using agents into the inference process. The approach
are converted into standardized JSON structures.
leverages three key agents: a web-search agent for real-time
• DynamicHandoffs:Agentscantransfercontroltoonean- retrievalofpertinentinformation,acodingagentforexecuting
other based on the conversation flow or specific function
computational tasks, and a Mind Map agent that constructs
criteria, simply by returning the next agent to call.
structured knowledge graphs to track and organize logical
• Context Management: Context variables are used to ini- relationshipsduringreasoning.Bydynamicallyengagingthese
tialize and update state throughout the conversation, enspecialized agents, the framework enables LLMs to perform
suringcontinuityandeffectiveinformationsharingacross
multi-step, expert-level problem solving and deep research,
agents.
addressing limitations in conventional internal reasoning ap-
• Client Orchestration: The Client.run() function initiates proaches. Evaluations on challenging benchmarks such as
andmanagesthemulti-agentdialoguebytakinganinitial
the GPQA dataset and domain-specific deep research tasks
agent, user messages, and context, and then returning
demonstratethatAgenticReasoningsubstantiallyoutperforms
updated messages, context variables, and the last active
traditionalretrieval-augmentedgenerationsystemsandclosedagent.
source models, highlighting its potential for improved knowl-
• Direct Function Calling & Streaming: Swarm supports edge synthesis, test-time scalability, and structured problemdirect Python function calls within agents and provides
solving.
streaming responses for real-time interactions.
OctoTools [130] is a robust, training-free, and user-friendly
• Flexibility: The framework is designed to be agnostic to framework designed to empower large language models to
the underlying OpenAI client, working seamlessly with
tackle complex reasoning tasks across diverse domains. By
toolssuchasHuggingFaceTGIorvLLMhostedmodels.
integrating standardized tool cards that encapsulate various
5) GUI Agent: Hu et al. [128] introduced Claude 3.5 toolfunctionalities,aplannerfororchestratingbothhigh-level
Computer Use, marking a significant milestone as the first and low-level strategies, and an executor for effective tool usfrontier AI model to offer computer control via a graphical age,OctoToolsovercomesthelimitationsofpriormethodsthat
user interface in a public beta setting. The study assembles a wereconfinedtospecializeddomainsorrequiredextratraining
diversesetoftasks,rangingfromwebsearchandproductivity data. Validated across 16 varied tasks including MathVista,
workflows to gaming and file management, to rigorously MMLU-Pro, MedQA, and GAIA-Text OctoTools achieves an
evaluate the model’s ability to translate natural language average accuracy improvement of 9.3% over GPT-4o and
instructionsandscreenshotsintoprecisedesktopactions,such outperforms frameworks like AutoGen, GPT-Functions, and
as cursor movements, clicks, and keystrokes. The evaluation LangChain by up to 10.6% when using the same toolset.
framework not only demonstrates Claude 3.5’s unprecedented Comprehensive analysis and ablation studies demonstrate its
end-to-end performance, with a success rate of 16 out of advantages in task planning, effective tool integration, and
20 test cases, but also highlights critical areas for future multi-step problem solving, positioning it as a significant
refinement, including improved planning, action execution, advancement for general-purpose, complex reasoning appliand self-critique capabilities. Moreover, the performance is cations.
shown to be influenced by factors like screen resolution, and 7) AgentsSDK: TheOpenAIAgentsSDK[131]providesa
the study reveals that while the model can perform a wide comprehensiveframeworkforbuildingautonomous,multi-step
range of operations, it still struggles with replicating subtle agent applications that harness the power of large language
human-like behaviors such as natural scrolling and browsing. models alongside external tools. This SDK abstracts the core
Overall, this preliminary exploration underscores the potential componentsnecessaryforagenticworkflows,includingagents

<!-- Page 19 -->

19
themselves which are LLMs configured with instructions, cardiologists. Designed to address the limitations of generaltools, handoffs, and guardrails as well as the tools that enable purpose large language models (LLMs) in clinical settings,
these agents to perform external actions (such as API calls ZODIAC leverages a multi-agent collaboration architecture to
or computations). It also supports context management to process patient data across multiple modalities. Each agent
maintain state over multi-turn interactions, structured output is fine-tuned using real-world patient data adjudicated by
types for reliable data exchange, and advanced features like cardiologists,ensuringthesystem’sdiagnosticoutputs,suchas
streaming,tracing,andguardrailstoensuresafetyanddebuga- the extraction of clinically relevant characteristics, arrhythmia
bility. detection, and preliminary report generation, are accurate
and reliable. Rigorous clinical validation, conducted by independent cardiologists and evaluated across eight metrics

### B. AI Agent applications

addressing clinical effectiveness and security, demonstrates
AI Agents are autonomous systems that combine large that ZODIAC outperforms industry-leading models, including
language models (LLMs), data retrieval mechanisms, and GPT-4o, Llama-3.1-405B, Gemini-pro, and even specialized
decision-making pipelines to tackle a wide array of tasks medical LLMs like BioGPT. Notably, the successful inteacross industries. In healthcare, they assist with clinical di- gration of ZODIAC into electrocardiography (ECG) devices
agnosis and personalized treatment planning; in finance, they underscores its potential to transform healthcare delivery,
support forecasting and risk analysis; in scientific research, exemplifying the emerging trend of embedding LLMs within
they automate literature review and experimental design; and Software-as-Medical-Device (SaMD) solutions.
in software engineering, they generate, analyze, and repair Wang et al. [148] introduce MedAgent-Pro, an evidencecode. Using domain-specific fine-tuning and structured data based, agentic system designed to enhance multi-modal medsources, AI agents can also drive the generation of syn- ical diagnosis by addressing key limitations of current Multitheticdata,facilitatechemicalreasoning,supportmathematical modal Large Language Models (MLLMs). While MLLMs
problem-solving, and enable creative multimedia production, havedemonstratedstrongreasoningandtask-performingcapathereby expanding the reach of AI-powered automation and bilities,theyoftenstrugglewithdetailedvisualperceptionand
insight generation. Fig. 7 presents both the architectural back- exhibit reasoninginconsistencies, both ofwhich arecritical in
bone and the application landscape of AI Agents. clinical settings. MedAgent-Pro employs a hierarchical work-
1) Healthcare Applications: The healthcare sector has wit- flow:atthetasklevel,itleveragesknowledge-basedreasoning
nessed significant advancements through the integration of to generate reliable diagnostic plans grounded in retrieved
large language model-based agents across a wide range of clinical criteria, and at the case level, it utilizes multiple
applications. In this subsection, we present recent develop- tool agents to process multi-modal inputs and analyze diverse
mentsorganizedintokeycategories,aspresentedinFig.8,in- indicators. The final diagnosis is derived from a synthesis of
cluding clinical diagnosis and decision support, mental health quantitative and qualitative evidence. Comprehensive experiand therapy agents, general medical assistants for workflow mentsonboth2Dand3Dmedicaldiagnosistasksdemonstrate
optimization, and pharmaceutical and drug discovery agents. thatMedAgent-Pronotonlyoutperformsexistingmethodsbut
TheseworksdemonstratehowAIagentsareincreasinglysup- also offers enhanced reliability and interpretability, marking a
porting medical professionals, enhancing diagnostic accuracy, significant step forward in AI-assisted clinical diagnostics.
improving patient care, and accelerating research in diverse Feng et al. [150] introduce M3Builder. This novel multihealthcare domains. Tab. reviews AI agent applications for agent system automates machine learning workflows in the
Healthcare. medical imaging domain, a field that has traditionally needed
a) Clinical Diagnosis, Imaging & Decision Support: specialized models and tools. M3Builder is structured around
Chenetal.[146]introduceChain-of-Diagnosis(CoD),anovel four specialized agents that collaboratively manage complex,
approach designed to enhance the interpretability of LLM- multi-step ML tasks, including automated data processing,
based medical diagnostics. By transforming the diagnostic environmentconfiguration,self-containedauto-debugging,and
process into a transparent, step-by-step chain that mirrors a model training, all within a dedicated medical imaging ML
physician’s reasoning, CoD provides a clear reasoning path- workspace.Toassessprogressinthisarea,theauthorspropose
way alongside a disease confidence distribution, which aids M3Bench, a comprehensive benchmark featuring four general
in identifying critical symptoms through entropy reduction. tasksacross14trainingdatasets,coveringfiveanatomies,three
This transparent methodology not only makes the diagnostic imaging modalities, and both 2D and 3D data. Evaluations
process controllable but also boosts rigor in decision-making. using seven state-of-the-art large language models as agent
Leveraging CoD, the authors developed DiagnosisGPT, an cores, such as the Claude series, GPT-4o, and DeepSeek-V3,
advancedsystemcapableofdiagnosing9,604diseases.Exper- demonstratethatM3Buildersignificantlyoutperformsexisting
imental results demonstrate that DiagnosisGPT outperforms MLagentdesigns,achievingaremarkable94.29%successrate
existing large language models (LLMs) on diagnostic bench- with Claude-3.7-Sonnet.
marks, achieving both high diagnostic accuracy and enhanced Rose et al. [151] tackles the complexities of differential
interpretability. diagnosis(DDx)byintroducingtheModularExplainableDDx
Zhou et al. [147] present ZODIAC, an innovative LLM- Agent (MEDDxAgent) framework, which facilitates interacpowered framework that elevates cardiological diagnostics tive,iterativediagnosticreasoningratherthanrelyingoncomto a level of professionalism comparable to that of expert plete patient profiles from the outset. Addressing limitations

<!-- Page 20 -->

20

### TABLE VII: Overview of AI Agent Applications for Healthcare

Application Year Category CoreObjective Workflow&Components KeyBenefits/Results C W R
DiagnosisGPT 2024 Medical Enhanceinterpretabilityviaa ImplementsCoDtoyield Diagnoses9,604diseases;
[146] Diagnos- transparent,step-by-stepchain. confidencescoresandentropy outperformsexistingLLMs.
tics reduction.
ZODIAC 2024 Cardiology Deliverexpert-level Multi-agentLLMfine-tunedon Outperformsleadingmodels;
[147] cardiologicaldiagnostics. adjudicatedpatientdata. integratedintoECGdevices.
MedAgent- 2025 Medical Enhancemulti-modaldiagnosis Hierarchicalworkflowwith Outperformsexistingmethods
Pro[148] Diagnosis byaddressingvisualand knowledge-basedreasoningand on2D/3Dtaskswithimproved
reasoninggaps. multi-modalagents. reliability.
Steenstraet 2025 Therapeutic Improvecounselingtraining LLM-poweredsimulated Highusabilityandsatisfaction;
al.[149] Counsel- withcontinuous,detailed patientswithturn-by-turn enhanceslearningvs.traditional
ing feedback. visualizations. methods.
M3Builder 2025 Medical AutomateMLworkflowsin Fouragentsmanagedata Achieves94.29%successwith
[150] Imaging medicalimaging. processing,configuration, state-of-the-artLLMcores.
ML debugging,andtraining.
MEDDxAgent 2025 Differential Enableiterative,interactive IntegratesaDDxDriver,history Boostsdiagnosticaccuracyby
[151] Diagnosis differentialdiagnosis. simulator,andspecialized over10%withenhanced
retrieval/diagnosisagents. explainability.
PathFinder 2025 AI- ReplicateholisticWSIanalysis Fouragentscollaboratively Outperformsstate-of-the-artby
[152] assisted asdonebyexpertpathologists. generateimportancemapsand 8%,exceedingaverage
Diagnos- diagnoses. pathologistperformanceby9%.
tics
HamRaz 2025 Therapeutic ProvidethefirstPersianPCT Combinesscripteddialogues Producesmoreempathetic,
[153] Counsel- datasetforLLMswithculturally andadaptiveLLMrole-play. nuanced,andrealistic
ing adaptedtherapysessions. counselinginteractions.
CAMI 2025 Therapeutic AutomateMI-basedcounseling STARframeworkwiththree OutperformsbaselinesinMI
[154] Counsel- withclientstateinference,topic LLMmodulesforstate,topic, competencyandcounseling
ing exploration,andempathetic andresponse. realism.
responsegeneration.
AutoCBT 2025 Therapeutic DeliverdynamicCBTvia Usessingle-turnagentsand Generateshigher-qualityCBT
[155] Counsel- multi-agentroutingand dynamicsupervisoryroutingfor responsesvs.fixedsystems.
ing supervision. tailoredinterventions.
PSYCHE 2025 Psychiatric BenchmarkPACAswith Usesdetailedpsychiatric Validatedforclinical
[156] Assess- simulatedpatientprofilesand constructsandboard-certified appropriatenessandsafety.
ment multi-turninteractions. psychiatristevaluations.
PsyDraw 2024 Mental AnalyzeHTPdrawingswith Two-stagefeatureextractionand 71.03%highconsistencywith
[157] Health multimodalagentsforearly reportgeneration;evaluatedon experts;scalablescreeningtool.
Screening screeningofLBCs. 290submissions;pilot
deploymentinschools.
EvoPatient 2024 Medical Simulatepatient–doctor Iterativemulti-turnconsultations Improvesrequirementalignment
[158] Training dialoguesfortrainingvia refinepatientresponsesand by>10%andachieveshigher
unsupervisedLLMagents. physicianquestionsover200 humanpreference.
casesimulations.
Scripted 2024 Therapeutic ConstrainLLMresponsesvia Twopromptingvariantsexecute Demonstratesreliablescript
Therapy Counsel- expert-writtenscriptsandfinite 100simulatedsessions adherenceandtransparent
Agents ing conversationalstates. followingdeterministic decisionpaths.
[159] therapeuticscripts.
LIDDiA 2025 Drug Automateend-to-enddrug OrchestratesLLM-driven Generatesvalidcandidates
[160] Discov- discoveryfromtargetselection reasoningacrossallpipeline >70%ofcases;identifiesnovel
ery toleadoptimization. steps;evaluatedon30targets. EGFRinhibitors.
PatentAgent 2024 PharmaceuticaSltreamlinepatentanalysiswith PA-QA,PA-Img2Mol, Improvesimage-to-molecule
[161] Patents LLM-drivenQA, PA-CoreIdmodulesfor accuracybyupto8.37%and
image-to-molecule,andscaffold comprehensivepatentinsights. scaffoldIDbyupto7.62%.

## Id.

DrugAgent 2024 DrugRe- Acceleratedrugrepurposingvia CombinesDTImodeling,KG Improvespredictionaccuracy
[162] purposing multi-agentMLandknowledge extraction,andliteraturemining andreducesdiscoverytime/cost.
integration. agents.
MAP[163] 2025 Inpatient Supportcomplexinpatient UsesIPDSbenchmark; +25.10%diagnosticaccuracy
Decision pathwayswithspecialized coordinatedbyachiefagentfor vs.HuatuoGPT2-13B;+10–12%
Support triage,diagnosis,andtreatment end-to-endcareplanning. clinicalcomplianceover
agents. clinicians.
SynthUserEval 2025 Health Generatesyntheticusersfor Createsstructuredprofilesand Enablesrealistic,
[164] Coaching evaluatingbehavior-change simulatesinteractionswith health-groundeddialogues;
agents. coachingagents. validatedbyexpertevaluations.
C:ClinicalValidation;W:WorkflowIntegration;R:RegulatoryCompliance; :Partial; :NotSupported; :Supported.

<!-- Page 21 -->

21

### Sub - AI Agent

applications Agentic AI

### Mental Health, Counseling & Therapy Agents

Pharmaceutical & Drug-Related Agents Customized
LLM model Vector

### Database


### Agents for Astronomical Observations

Gene Set Knowledge Discovery AI Agent

### LLM model


### Biomedical AI Scientist Agents

Mathematical Reasoning and Problem Solving Users
.......

### Action Database


### AI Agent applications

Healthcare Materials Science Biomedical Science Research Software Engineering

### Applications Applications

Synthetic data Finance Applications Chemical Reasoning Solving mathematical Geography Multimedia
generation problems Applications Applications
Fig. 7: Architecture and Application Domains of AI Agents.
in previous approaches such as evaluations on single datasets, indicate that PathFinder outperforms state-of-the-art methods
isolated component optimization, and single-attempt diag- inskinmelanomadiagnosisby8%and,notably,surpassesthe
noses MEDDxAgent integrates three modular components: averageperformanceofpathologistsby9%,establishinganew
an orchestrator (DDxDriver), a history-taking simulator, and benchmarkforaccurate,efficient,andinterpretableAI-assisted
two specialized agents for knowledge retrieval and diagnosis diagnostics in pathology.
strategy. To ensure robust evaluation, the authors also present b) Mental Health, Counseling & Therapy Agents:
a comprehensive DDx benchmark covering respiratory, skin, Wasenmu¨ller et al. [159] present a script-based dialog policy
andrarediseases.Theirfindingsrevealthatiterativerefinement planning paradigm that enables LLM-powered conversational
significantly enhances diagnostic accuracy, with MEDDxA- agents to function as AI therapists by adhering to expertgent achieving over a 10% improvement across both large written therapeutic scripts and transitioning through a finite
and small LLMs while providing critical explainability in its set of conversational states. By treating the script as a deterreasoning process. ministic guide, the approach constrains the model’s responses
Ghezloo et al. [152] introduce Pathfinder, a novel multi- toalignwithadefinedtherapeuticframework,makingdecision
modal, multi-agent framework designed to replicate the holis- paths transparent for clinical evaluation and risk management.
tic diagnostic process of expert pathologists when analyz- Theauthorsimplementtwovariantsofthisparadigm,utilizing
ing whole-slide images (WSIs). Recognizing that WSIs are different prompting strategies, and generate 100 simulated
characterized by their gigapixel scale and complex structure, therapy sessions with LLM-driven patient agents. Experimen-
PathFinder employs four specialized agents a Triage Agent, tal results demonstrate that both implementations can reliably
Navigation Agent, Description Agent, and Diagnosis Agent followthescriptedpolicy,providinginsightsintotheirrelative
that collaboratively navigate and interpret the image data. efficiencyandeffectiveness,andunderscoringthefeasibilityof
The Triage Agent first determines whether a slide is benign building inspectable, rule-aligned AI therapy systems.
or risky; if deemed risky, the Navigation and Description Du et al. [158] introduce EvoPatient, a framework for gen-
Agents iteratively focus on and characterize significant re- eratingsimulatedpatientsusinglargelanguagemodelstotrain
gions, generating importance maps and detailed natural lan- medical personnel through multi-turn diagnostic dialogues.
guage descriptions. Finally, the Diagnosis Agent synthesizes Existingapproachesfocusondataretrievalaccuracyorprompt
these findings to provide a comprehensive diagnostic classi- tuning, but EvoPatient emphasizes unsupervised simulation to
fication that is inherently explainable. Experimental results teach patient agents standardized presentation patterns. In this

<!-- Page 22 -->

22
system, a patient agent and doctor agents engage in iterative Yang et al. [154] present CAMI, an automated conversaconsultations, with each dialogue cycle serving to both train tional counselor agent grounded in Motivational Interviewing
theagentsandgatherexperiencethatrefinespatientresponses (MI), a client-centered approach designed to resolve ambivaand physician questions. Extensive experiments across di- lence and promote behavior change. CAMI’s novel STAR
verse clinical scenarios show that EvoPatient improves re- frameworkintegratesthreeLLM-poweredmodulesclientState
quirement alignment by more than 10 percent compared to inference, motivation Topic exploration, and response gEnerstate-of-the-artmethodsandachieveshigherhumanpreference ation to evoke “change talk” in line with MI principles. By
ratings. After evolving through 200 case simulations over a accuratelyinferringaclient’semotionalandmotivationalstate,
periodoftenhours,theframeworkachievesanoptimalbalance exploring relevanttopics, and generatingempathetic, directive
between resource efficiency and performance, demonstrating responses, CAMI facilitates more effective counseling across
strong generalizability for scalable medical training. diverse populations. The authors evaluate CAMI using both
Zhang et al. [157] present PsyDraw, a multimodal LLM- automated metrics and manual assessments with simulated
driven multi-agent system designed to support mental health clients, measuring MI skill competency, state inference acprofessionalsinanalyzingHouse-Tree-Person(HTP)drawings curacy, topic exploration proficiency, and overall counseling
for early screening of left-behind children (LBCs) in rural success. Results demonstrate that CAMI outperforms existing
China. Recognizing the acute shortage of clinicians, PsyDraw methods and exhibits counselor-like realism, while ablation
employs specialized agents for detailed feature extraction studies highlight the essential contributions of the state inand psychologicalinterpretation intwo stages:comprehensive ference and topic exploration modules to its superior perforanalysis of drawing elements and automated generation of mance.
professional reports. Evaluated on 290 primary-school HTP Steenstra et al. [149] address the challenges in therapeutic
submissions,PsyDrawachievedHighConsistencywithexpert counselingtraining byproposingan innovativeLLM-powered
evaluations in 71.03% of cases and Moderate Consistency system that provides continuous, detailed feedback during
in 26.21%, flagging 31.03% of children as needing further simulated patient interactions. Focusing on motivational inattention. Deployed in pilot schools, PsyDraw demonstrates terviewing a counseling approach emphasizing empathy and
strong potential as a scalable, preliminary screening tool that collaborative behavior change the framework features a simmaintains high professional standards and addresses critical ulated patient and visualizations of turn-by-turn performance
mental health gaps in resource-limited settings. to guide counselors through role-play scenarios. The system
Leeetal.[156]introducePSYCHE,acomprehensiveframe- was evaluated with both professional and student counselors,
work for benchmarking psychiatric assessment conversational who reported high usability and satisfaction, indicating that
agents (PACAs) built on large language models. Recognizing frequent and granular feedback can significantly enhance the
that psychiatric evaluations rely on nuanced, multi-turn inter- learningprocesscomparedtotraditional,intermittentmethods.
actions between clinicians and patients, PSYCHE simulates Abbasi et al. [153] introduce HamRaz, the first Persianpatients using a detailed psychiatric construct that specifies language dataset tailored for Person-Centered Therapy (PCT)
theirprofiles,histories,andbehavioralpatterns.Thisapproach with large language models (LLMs), addressing a critical
enables clinically relevant assessments, ensures ethical safety gap in culturally and linguistically appropriate mental health
checks, facilitates cost-efficient deployment, and provides resources. Recognizing that existing counseling datasets are
quantitative evaluation metrics. The framework was validated largely confined to Western and East Asian contexts, the
in a study involving ten board-certified psychiatrists who authors design HamRaz by blending scripted therapeutic diareviewed and rated the simulated interactions, demonstrating logueswithadaptiveLLM-drivenrole-playingtofostercoher-
PSYCHE’s ability to rigorously evaluate PACAs’ clinical ent, dynamic therapy sessions in Persian. To rigorously assess
appropriateness and safety. performance, they propose HamRazEval, a dual evaluation
Xu et al. [155] addresses the limitations of existing LLM- framework combining general dialogue quality metrics with
based Cognitive Behavioral Therapy (CBT) systems, namely theBarrett–LennardRelationshipInventory(BLRI)tomeasure
theirrigidagentstructuresandtendencytowardredundant,un- therapeutic rapport and effectiveness. Experimental comparhelpfulsuggestions,byproposingAutoCBT,adynamicmulti- isons demonstrate that LLMs trained on HamRaz generate
agentframeworkforautomatedpsychologicalcounseling.Ini- more empathetic, contextually nuanced, and realistic counseltially, the authors develop a general single-turn consultation ing interactions than conventional Script Mode or Two-Agent
agent using Quora-like and YiXinLi models, evaluated on Mode approaches.
a bilingual dataset to benchmark response quality in single- c) General Medical Assistants, Clinical Workflow & Deround interactions. Building on these insights, they introduce cision Making: Yun et al. [164] introduce an end-to-end
dynamic routing and supervisory mechanisms modeled af- framework for generating synthetic users to evaluate interter real-world counseling practices, enabling agents to self- active agents aimed at promoting positive behavior change,
optimizeandtailorinterventionsmoreeffectively.Experimen- focusing on sleep and diabetes management. The framework
tal results demonstrate that AutoCBT generates higher-quality first generates structured data based on real-world health and
CBT-oriented responses compared to fixed-structure systems, lifestylefactors,demographics,andbehavioralattributes.Next,
highlighting its potential to deliver scalable, empathetic, and itcreatescompleteuserprofilesconditionedonthisstructured
contextually appropriate psychological support for users who data.Interactionsbetweensyntheticusersandhealthcoaching
might otherwise avoid in-person therapy. agents are simulated using generative agent models such as

<!-- Page 23 -->

23
Concordia or by directly prompting a language model. Case PA-Img2Mol for converting chemical structure images into
studies with sleep and diabetes coaching agents demonstrate molecular representations, and PA-CoreId for identifying core
that the synthetic users enable realistic dialogue by accurately chemical scaffolds. PA-Img2Mol achieves accuracy gains of
reflecting users’ needs and challenges. Blinded evaluations by 2.46 to 8.37 percent across CLEF, JPO, UOB, and USPTO
human experts confirm that these health-grounded synthetic patent image benchmarks, while PA-CoreId delivers improveusers portray real human users more faithfully than generic ments of 7.15 to 7.62 percent on the PatentNetML scaffold
syntheticusers.Thisapproachprovidesascalableandrealistic identification task. By combining these modules within a
testing ground for developing and refining conversational unified framework, PatentAgent addresses the full spectrum
agents in health and lifestyle coaching. ofpatentanalysisneeds,fromextractingdetailedexperimental
Chenetal.[163]addressthecomplexityofclinicaldecision- insights to pinpointing key molecular structures, and offers a
making in inpatient pathways by introducing both a new powerful tool to accelerate research and innovation in drug
benchmarkandamulti-agentAIframework.Theauthorscon- discovery.
struct the Inpatient Pathway Decision Support (IPDS) bench- Averly et al. [160] introduce LIDDiA, an autonomous in
mark from the MIMIC-IV database, comprising 51,274 cases silico agent designed to navigate the entire drug discovery
across nine triage departments, 17 disease categories, and 16 pipeline by leveraging the reasoning capabilities of large
standardized treatment options to capture the multifaceted na- languagemodels.UnlikepriorAItoolsthataddressindividual
ture of inpatient care. Building on this resource, they propose steps such as molecule generation or property prediction,
theMulti-AgentInpatientPathways(MAP)framework,which LIDDiAorchestratestheend-to-endprocessfromtargetselecemploysatriageagentforpatientadmission,adiagnosisagent tion through lead optimization. The authors evaluate LIDDiA
for department-level decision-making, and a treatment agent on 30 clinically relevant targets and show that it generates
forcareplanning,allcoordinatedbyachiefagentthatoversees candidate molecules satisfying key pharmaceutical criteria in
the entire pathway. In extensive experiments, MAP achieves over 70 percent of cases. Furthermore, LIDDiA demonstrates
a 25.10% improvement in diagnostic accuracy over the state- anintelligentbalancebetweenexploringnovelchemicalspace
of-the-art LLM HuatuoGPT2-13B and surpasses three board- and exploiting known scaffolds and successfully identifies
certified clinicians in clinical compliance by 10–12%. These promising new inhibitors for the epidermal growth factor
results demonstrate the potential of multi-agent systems to receptor (EGFR), a major oncology target.
support complex inpatient workflows and lay the groundwork Inoueetal.[162]presentamulti-agentframeworkdesigned
for future AI-driven decision support in hospital settings. toacceleratedrugrepurposingbycombiningmachinelearning
and knowledge integration. The system includes three specialized agents: an AI Agent that trains robust drug–target
PatentAgent interaction (DTI) models, a Knowledge Graph Agent that

## [161] Map

LIDDiA Fra [ m 16 ew 3] ork extractsDTIsfromdatabasessuchasDGIdb,DrugBank,CTD
[160]
Synthetic and STITCH, and a Search Agent that mines biomedical

### Users

Drug [164] literaturetovalidatecomputationalpredictions.Byintegrating

### Repurposing

[162] outputs from these agents, the framework leverages diverse
Ph D ar r m u A g a g - c R e e n u e t l t s a ic te a d l& & C G l D i e n e n A i c c e s i a r s s a l i i l o s W t M n a o n M e r t d k s a , i fl c k o a i w n l g d P a re ta lim so i u n r a c r e y s e to va i l d u e a n ti t o if n y s p i r n o d m ic i a s t i e ng th c a a t nd th id is ate a s pp f r o o r a r c e h pu n r o p t os o i n n l g y .
enhances the accuracy of drug–disease interaction predictions
compared to existing methods but also reduces the time
Healthcare and cost associated with traditional drug discovery. The in-
Applications H [ a 1 m 5 R 3] az terpretable results and scalable architecture demonstrate the
potential of multi-agent systems to drive innovation and effi-

### CoD Scaffolding

[146] [149] ciency in biomedical research.
ClinicalDiagnosis, MentalHealth, 2) Materials Science: Materials science has recently ben-

### Imaging& Counseling&

ZODIAC DecisionSupport TherapyAgents CAMI efited from the integration of LLM-based agents, which are
[147] [154]
helpingtoautomatecomplexscientificworkflowsandenhance
MedAgent-Pro AutoCBT research efficiency. In this subsection, we highlight two no-
[148] [155]
Script table developments, including the application of AI agents

### Planning

M3Builder [159] PSYCHE in astronomical observations to streamline data collection and
[150] MED [1 D 5 x 1 A ] gent Pat [ h 1 F 5 i 2 n ] der Evo [1 P 5 a 8 ti ] ent Ps [ y 1 D 57 ra ] w [156] analysis,andthecreationofspecializedagentsystemstailored
toaddresstheuniquechallengesofmaterialsscienceresearch.
Fig. 8: Agent LLM Applications for Healthcare a) LLM-Based Agents for Astronomical Observations:

### The StarWhisper Telescope System [132] leverages LLM-

d) Pharmaceutical & Drug-Related Agents: Wang et al. based agents to streamline the complex workflow of astro-
[161] introduce PatentAgent, the first end-to-end intelligent nomical observations within the Nearby Galaxy Supernovae
agent designed to streamline pharmaceutical patent analysis Survey(NGSS)project.Thisinnovativesystemautomatescritby leveraging large language models. PatentAgent integrates ical tasks including generating customized observation lists,
three core modules: PA-QA for patent question answering, initiatingtelescopeobservations,real-timeimageanalysis,and

<!-- Page 24 -->

24
formulating follow-up proposals to reduce the operational steps, all within a thinking token framework that fosters
burdenonastronomersandlowertrainingcosts.Byintegrating iterative feedback loops.
these agents into the observation process, the system can effi- c) BiomedicalAIScientistAgents: Linetal.[165]introciently verify and dispatch observation lists, analyze transient duce BioKGBench, a novel benchmark designed to evaluate
phenomena in near real-time, and seamlessly communicate biomedical AI scientist agents from the perspective of literaresults to observatory teams for subsequent scheduling. ture understanding. Unlike traditional evaluation methods that
b) Materials Science Research: HoneyComb [133] is rely solely on direct QA or biomedical experiments, BioKG-
introduced as the first LLM-based agent system tailored ex- Bench decomposes the critical ability of “understanding literplicitlyformaterialsscience,addressingtheuniquechallenges ature”intotwoatomictasks:onethatverifiesscientificclaims
posed by complex computational tasks and outdated implicit in unstructured text from research papers and another that inknowledge that often lead to inaccuracies and hallucinations volves interacting with structured knowledge-graph questioningeneral-purposeLLMs.Thesystemleveragesanovel,high- answering(KGQA)forliteraturegrounding.Buildingonthese
qualitymaterialsscienceknowledgebase(MatSciKB)curated components, the authors propose a new agent task called
from reliable literature and a sophisticated tool hub (Tool- KGCheck,whichusesdomain-basedretrieval-augmentedgen-
Hub) that employs an Inductive Tool Construction method eration to identify factual errors in large-scale knowledge
to generate, decompose, and refine specialized API tools. graph databases. With a dataset of over 2,000 examples for
Additionally, the retriever module adaptively selects the most the atomic tasks and 225 high-quality annotated samples for
relevant knowledge sources and tools for each task, ensuring the agent task, the study reveals that state-of-the-art agents
high accuracy and contextual relevance. both in everyday and biomedical settings perform poorly or
3) Biomedical Science: The biomedical field has seen suboptimally on this benchmark.
important progress through the development of LLM-based 4) Research Applications: LLM-based agents are increasagents designed to support knowledge discovery, enhance inglybeingdevelopedtosupportandautomatevariousaspects
reasoning capabilities, and evaluate scientific literature. In of the scientific research process. This subsection presents
this subsection, we review recent contributions that focus on a selection of recent applications, including collaborative regene set analysis, iterative learning for improved reasoning, search environments, automated survey generation, structured
and the evaluation of AI scientist agents through specialized literature analysis for ideation, workflow management in data
biomedical benchmarks. science, and AI-driven hypothesis generation.
a) Gene Set Knowledge Discovery: Gene set knowl- a) Collaborative Research Among LLM Agents:
edge discovery is crucial for advancing human functional Schmidgall and Moor [166] introduces AgentRxiv, a framegenomics, yet traditional LLM approaches often suffer from work designed to enable collaborative research among auissues like hallucinations. To address this, Wang et al. [134] tonomous LLM agent laboratories by leveraging a shared
introduce GeneAgent a pioneering language agent with self- preprint server. Recognizing that scientific discovery is inherverification capabilities that autonomously interacts with bio- ently incremental and collaborative, AgentRxiv allows agents
logicaldatabasesandleveragesspecializeddomainknowledge to upload and retrieve research reports, thereby sharing into enhance accuracy. Benchmarking on 1,106 gene sets from sightsandbuildinguponpreviousworkinaniterativemanner.
diversesources,GeneAgentconsistentlyoutperformsstandard The study demonstrates that agents with access to prior
GPT-4, and a detailed manual review confirms that its self- research achieve a significant performance boost an 11.4%
verification module effectively minimizes hallucinations and relative improvement on the MATH-500 dataset compared to
produces more reliable analytical narratives. Moreover, when those operating in isolation. Furthermore, the best-performing
applied to seven novel gene sets derived from mouse B2905 collaborative strategy generalizes to other domains with an
melanomacelllines,expertevaluationsrevealthatGeneAgent average improvement of 3.3%, and when multiple agent laboffers novel insights into gene functions, significantly ex- oratories share their findings, overall accuracy increases by
pediting the process of knowledge discovery in functional 13.7% relative to the baseline. These findings highlight the
genomics. potential of autonomous agents to collaborate with humans,
b) Reasoning with Recursive Learning: Buehler et al. paving the way for more efficient and accelerated scientific
[135] proposed a framework, named PRefLexOR, that fuses discovery.
preference optimization with reinforcement learning concepts b) Automated Survey Generation: Liang et al. [136]
to enable language models to self-improve through iterative, developed the SurveyX platform, which leverages the excepmulti-stepreasoning.Theapproachemploysarecursivelearn- tional comprehension and knowledge capabilities of LLMs
ingstrategyinwhichthemodelrepeatedlyrevisitsandrefines to overcome critical limitations in automated survey generintermediate reasoning steps before producing a final output, ation, including finite context windows, superficial content
both during training and inference. Initially, the model aligns discussions,andthelackofsystematicevaluationframeworks.
its reasoning with accurate decision paths by optimizing the Inspired by human writing processes, SurveyX decomposes
logoddsbetweenpreferredandnon-preferredresponseswhile the survey composition process into two distinct phases:
constructing a dynamic knowledge graph through question Preparation and Generation. During the preparation phase,
generation and retrieval augmentation. In a subsequent stage, the system incorporates online reference retrieval and applies
rejection sampling is employed to refine the reasoning quality a novel preprocessing method, AttributeTree, to effectively
by generating in-situ training data and masking intermediate structure the survey’s content. In the subsequent Generation

<!-- Page 25 -->

25

### TABLE VIII: Overview of AI Agent Applications for Research

Agent/Tool Year UseCase PrimaryAim Methodology& KeyFindings& Eval. Collab. OpenSci.
Workflow Metrics Frame- Platform
work
AgentRxiv[166] 2025 Collaborative Shareandbuildupon Upload/retrievevia +11.4%on MATH-500 AgentRxiv Preprint
Research preprintsacross sharedpreprintserver MATH-500;+3.3% benchmark server sharing
autonomousLLM withiterativeupdates. cross-domain;+13.7%
labs. multi-lab.
SurveyX[136] 2025 Survey Automatesystematic Preparation(retrieval +0.259content Content& Bibliographic Structured
Generation literaturesurveyswith +AttributeTree)+ quality;+1.76citation citation APIs citations
highquality. Generation precisionvs.baselines. scoring
(repolishing).
CoIAgent[137] 2024 Research Structureliterature Sequential Expert-comparable IdeaArena CoI Cost-efficient
Ideation intoprogressiveidea Chain-of-Ideas+Idea ideaqualityat$0.50 framework ideation
chains. Arenaevaluation peridea.
protocol.
DataInterpreter 2024 Data Manageend-to-end, HierarchicalGraph +25%on InfiAgent PipelineAPIs Reproducible
[167] Science dynamicDSpipelines Modeling+ InfiAgent-DABench DABench workflows
Workflows robustly. ProgrammableNode (75.9→94.9%);ML&
Generation. MATHgains.
AICo-Scientist 2025 Scientific Generateandrefine Sevenspecialized +300Elohypothesis Elo& Multi-agent Hypothesis
[168] Discovery researchhypotheses agentswithElo quality;+27%novelty novelty pipeline publication
autonomously. tournamentsand scores. scoring
meta-review.
Eval.Framework:EvaluationFramework;Collab.Platform:CollaborationPlatform;OpenSci.:OpenScienceSupport.
phase, a repolishing process refines the output to enhance verifies each subproblem to boost the robustness of code
the depth and accuracy of the study generated, particularly generation.Extensiveexperimentsdemonstratesignificantperimprovingcontentqualityandcitationprecision.Experimental formance gains achieving up to a 25% boost on InfiAgentevaluations reveal that SurveyX achieves a content quality DABench (increasing accuracy from 75.9% to 94.9%), as
improvement of 0.259 and a citation quality enhancement of well as improvements on machine learning, open-ended tasks,
1.76 over existing systems, bringing its performance close to and the MATH dataset highlighting its superior capability
that of human experts across multiple evaluation dimensions. in managing evolving task dependencies and real-time data
c) Structuring Literature for Research Ideation: Li et adjustments.
al. [137] introduce the Chain-of-Ideas (CoI) agent, a novel e) Automating Scientific Discovery: Google [168] intro-
LLM-based framework for automating research ideation by ducedtheAIco-scientist,amulti-agentsystembuiltonGoogle
structuring relevant literature into a chain that mirrors the DeepMind Gemini 2.0, designed to automate scientific disprogressive development within a research domain. The CoI covery by generating and refining novel research hypotheses.
agentaddressesthechallengeposedbytheexponentialgrowth TheframeworkcomprisessevenspecializedagentsSupervisor,
of scientific literature, which overwhelms traditional idea- Generation, Reflection, Ranking, Evolution, Proximity, and
generation methods that rely on simple prompts or expose Meta-review that collaboratively manage tasks ranging from
models to raw, unfiltered text. By organizing information in a parsing research goals to conducting simulated debates and
sequential chain, the CoI agent enables LLMs to capture cur- organizing hypotheses. For example, the system employs a
rent advancements more effectively, enhancing their ability to Ranking Agent that uses pairwise Elo tournaments, boosting
generateinnovativeresearchideas.Complementingthisframe- hypothesis quality by over 300 Elo points. At the same time,
work is the Idea Arena, an evaluation protocol that assesses theMeta-reviewAgent’sfeedbackhasbeenshowntoincrease
the quality of generated ideas from multiple perspectives, hypothesis novelty scores by 27%. In practical applications,
aligning closely with the preferences of human researchers. suchasdrugrepurposingforacutemyeloidleukemiaandnovel
Experimental results indicate that the CoI agent outperforms targetdiscoveryforliverfibrosis,theframeworkdemonstrates
existing methods and achieves quality comparable to human significant performance improvements, paving the way for
experts, all while maintaining a low cost approximately $0.50 AI systems that can generate and iteratively refine scientific
per candidate idea and corresponding experimental design. hypotheses with expert-level precision.
d) ManagingDataScienceWorkflows: Hongetal.[167] 5) Software Engineering: Software engineering has bepropose Data Interpreter, an LLM-based agent that tackles come a significant area of application for LLM-based agents,
end-to-end data science workflows by addressing challenges with innovations spanning architecture design and verification
in solving long-term, interconnected tasks and adapting to systems, adaptive control, software analytics, and multi-agent
dynamic data environments. Unlike previous methods that collaboration. This subsection presents recent developments
focus on individual tasks, Data Interpreter leverages two key across a wide range of tasks, including agent programming
modules: Hierarchical Graph Modeling, which decomposes frameworks, tutoring systems, automated environment configcomplex problems into manageable subproblems through dy- uration, usability testing, and multilingual code generation.
namic node generation and graph optimization, and Pro- Fig. 9 presents a classification of Agent LLM Applications
grammable Node Generation, which iteratively refines and for Software Engineering.

<!-- Page 26 -->

26
TABLE IX: Overview of AI Agent Applications for Software Engineering
Agent/ Year SE PrimaryObjective Architecture&Workflow KeyOutcomes&Metrics Bench. Intgr. Std.

### Tool Domain

AnnArbor 2025 Agent TreatLLMsasautomata, IntroducestheAnnArbor Earlyexperimentsshow
Architec- Program- enablingprogrammingvia conceptualframeworkand improvedin-contextlearning.
ture[169] ming formalandnaturallanguages. Postlineplatform.
Arch.
AgentGym 2025 Verification ScalabletrainingofSWE-agents LeveragesSYNGENsynthetic Achieves51%passrateon
[170] &Super- viaSYNGENdatacurationand dataandHybridTest-time SWE-BenchVerified.
vision HybridTest-timeScaling. ScalingonSWE-Gym;trained
onSWE-BenchVerified.
TRAVER&DICT2025 Intelligent Trace-and-Verifyworkflowfor Combinesknowledgetracing Significantimprovementsin
[171] Tutoring stepwisecodingguidance; withturn-by-turnverification; coding-tutoringsuccessrates.
DICTevaluationprotocol. evaluatedviaDICTprotocol.
CURA 2025 Code VerbalProcessSupervisionfor IntegratesVPSmoduleswith +3.65%onBigCodeBenchwith
[172] Reason- codeunderstandingand LLMtoguidereasoningover o3-mini.
ing reasoning. code.
DARS 2025 Performance DynamicActionRe-Sampling Branchesonexecutionfeedback 55%pass@kand47%pass@1
[173] Enhance- tobranchinferenceatdecision toexplorealternativeactions. onSWE-BenchLite(Claude3.5
ment points. SonnetV2).
LocAgent 2025 CodeLo- Graph-basedcoderepresentation Parsescodeintoheterogeneous 92.7%file-levelaccuracy;+12%
[174] calization formulti-hoplocalization. graphsforreasoningover GitHubissueresolution.
dependencies.
GateLens 2025 Release NL→Relational-Algebra Automatesquerytranslationand 80%reductioninanalysistime
[175] Valida- conversionandPythoncode optimizedcodefordata (automotivesoftware).
tion generationfortest-dataanalysis. processing.
Repo2Run 2025 Env.Con- AtomicDockersetupsynthesis Synthesizesandtests 86.0%successon420Python
[176] figuration withdual-environmentrollback. Dockerfiles;isolatesfailuresvia repos;+63.9%vs.baselines.
dualenvironments.
UXAgent 2025 Usability LLM-agentwithbrowser Generatesqualitativeinsights, AcceleratesUXiterationand
[177] Testing connectortosimulatethousands actionlogs,andrecordings reducesupfrontuser
ofusers. beforeuserstudies. recruitment.
SWE-Gym 2024 Training RealisticPythontasksandunit Providesexecutable +19%resolverate;32.0%on
[178] Environ- testsforSWE-agenttraining. environmentswithtestsand SWE-BenchVerified;26.0%on
ment naturallanguagedescriptions. Lite.
Qwen2.5-xCoder2025 Multi-Agent Multilingualinstructiontuning Agentscollaboratetogenerate Outperformsonmultilingual
[179] Collabo- vialanguage-specificagents andrefinemultilingual programmingbenchmarks.
ration withmemory. instructions.
SyncMind 2025 CollaborationDefinesandbenchmarks IntroducesSyncBenchwith24 Exposesperformancegapsand
[180] Simula- out-of-syncscenariosto kreal-worldinstances. guidesimprovements.
tion improveagentcoordination.
CodeSim 2025 Code PlanverificationandI/O Incorporatesplanverification SOTAonHumanEval,MBPP,
[181] Genera- simulationformulti-agent andinternaldebuggingvia APPS,CodeContests.
tion synthesis&debugging. input/outputsimulation.
Bench.:Benchmarking;Intgr.:Integration&Deployment;Std.:StandardsCompliance; :Partial; :NotSupported; :Supported.
a) Agent Programming Architectures: Dong et al. [169] b) Verification&SupervisionAgents: ThepapersbyJain
explorepromptengineeringforlargelanguagemodels(LLMs) etal.[170],Wangetal.[171],andChenetal.[172]contribute
from the perspective of automata theory, arguing that LLMs toadvancingtheuseoflargelanguagemodels(LLMs)forrealcan be viewed as automata. They assert that just as automata world software engineering (SWE) tasks, intelligent tutoring,
must be programmed using the languages they accept, LLMs and code generation. Jain et al. [170] introduce AgentGym, a
should similarly be programmed within the scope of both comprehensiveenvironmentfortrainingSWE-agents,addressnatural and formal languages. This insight challenges tradi- ingchallengesinscalablecurationofexecutableenvironments
tional software engineering practices, which often distinguish andtest-timecomputescaling.TheirapproachleveragesSYN-
between programming and natural languages. The paper in- GEN, a synthetic data curation method, and Hybrid Test-time
troducestheAnnArborArchitecture,aconceptualframework Scaling to improve performance on the SWE-Bench Verified
designedforagent-orientedprogrammingoflanguagemodels, benchmark, achieving a state-of-the-art pass rate of 51%.
which serves as a higher-level abstraction to enhance in- Wang et al. [171] propose a novel coding tutoring framework,
context learning beyond basic token generation. The authors Trace-and-Verify (TRAVER), combining knowledge tracing
also present Postline, their agent platform, and discuss early and turn-by-turn verification to enhance tutor agents’ guidresults from experiments conducted to train agents within this ance toward task completion. Their work introduces DICT, a
framework. holistic evaluation protocol for tutoring agents, demonstrating
significant improvements in coding tutoring success rates.

<!-- Page 27 -->

27
significant advancement in optimizing coding agent perfor-

### SyncMind Multi-Agent

[180] Collab mance, reducing the need for extensive manual intervention

### Framework


## [179] Traver

Co [1 d 8 eS 1] im SW [1 E 7 -G 8] ym & [1 D 7 I 1 C ] T and improving overall efficiency.
d) Code Localization & Software Analytics: The works
UXAgent
[177]
by Chen et al. [174] and Gholamzadeh et al. [175] contribute

### Multi-Agent

Collab- significantadvancementsintheapplicationofLargeLanguage
oration
Simu & lation Dom SW ain E -Specific Re [ p 1 o 7 2 6 R ] un Models (LLMs) to improve software engineering tasks, such
Agents as code localization and release validation. Chen et al. [174]
introduce LocAgent, a framework for code localization that
Ga [1 te 7 L 5 e ] ns utilizes graph-based representations of codebases. By parsing
code into directed heterogeneous graphs, LocAgent captures
Code the relationships between various code structures and their

### Localiza- LocAgent

tion& [174] dependencies, enabling more efficient and accurate local-

### Software

Analytics ization through multi-hop reasoning. Their approach, when
applied to real-world benchmarks, demonstrates substantial
Software improvements in localization accuracy, achieving up to 92.7%

### Engineering

on file-level localization and enhancing GitHub issue resolution success rates by 12%. In comparison to state-of-
Adaptive the-art models, LocAgent provides similar performance at a

### Control&

Performance significantly lower cost. On the other hand, Gholamzadeh
Enhancement et al. [175] present GateLens, an LLM-based tool designed

## Dars

[173] to improve release validation in safety-critical systems like
automotive software. GateLens automates the analysis of test
data by converting natural language queries into Relational

### Verification

& Algebra expressions and generating optimized Python code,

### Supervision

AgentPro- Agents which significantly accelerates data processing. In industrial
gramming
Architectures C (V U P R S A ) evaluations, GateLens reduced analysis time by over 80%,
[172]
demonstrating strong robustness and generalization across
TRAVER different query types. This tool improves decision-making in

## &Dict

AnnArbor Ag [ e 1 n 7 tG 0] ym [171] safety-criticalenvironmentsbyautomatingtestresultanalysis,
Architecture Postline thereby enhancing the scalability and reliability of software
[169] Platform
[169]
systems in automotive applications.
Fig. 9: Agent LLM Applications in Software Engineering e) Domain-Specific SWE Agents: Hu et al. [176] introduce Repo2Run, a novel LLM-based agent aimed at automating the environment configuration process in software
Finally, Chen et al. present CURA, a code understanding and development.Traditionalmethodsforsettingupenvironments
reasoning system augmented with verbal process supervision often involve manual work or rely on fragile scripts, which
(VPS).CURAachievesa3.65%improvementonbenchmarks can lead to inefficiencies and errors. Repo2Run addresses
like BigCodeBench and demonstrates enhanced performance these challenges by fully automating the configuration of
whenpairedwiththeo3-minimodel.Theseworkscollectively Docker containers for Python repositories. The key innovapushtheboundariesofLLMapplicationsincomplexsoftware tions of Repo2Run are its atomic configuration synthesis and
engineering tasks, intelligent tutoring, and reasoning-driven a dual-environment architecture, which isolates internal and
code generation. external environments to prevent contamination from failed
c) Adaptive Control & Performance Enhancement: Ag- commands. A rollback mechanism ensures that only fully
garwal et al. [173] introduce Dynamic Action Re-Sampling executed configurations are applied, and the agent generates
(DARS), a novel approach for scaling compute during infer- executable Dockerfiles from successful configurations. Evalence in coding agents, aimed at improving their decision- uated on a benchmark of 420 Python repositories with unit
making capabilities. While existing methods often rely on tests,Repo2Runachievedanimpressivesuccessrateof86.0%,
linear trajectories or random sampling, DARS enhances agent outperforming existing baselines by 63.9%.
performance by branching out at key decision points and Lu et al. [177] developed UXAgent, a tool that uses
selecting alternative actions based on the history of previous LLM-Agent technology and a universal browser connector to
attempts and execution feedback. This enables coding agents simulate thousands of users for automated usability testing.
to recover more effectively from sub-optimal decisions, lead- It enables user experience (UX) researchers to quickly iterate
ing to faster and more efficient problem-solving. The authors onstudydesignsbyprovidingqualitativeinsights,quantitative
evaluateDARSontheSWE-BenchLitebenchmark,achieving actiondata,andvideorecordingsbeforeengagingparticipants.
an impressive pass@k score of 55% with Claude 3.5 Sonnet Wang et al. [171] introduce TRAVER (Trace-and-Verify),
V2 and a pass@1 rate of 47%, surpassing current state-of- a novel agent workflow that combines knowledge tracing
the-art open-source frameworks. This approach provides a estimating a student’s evolving knowledge state with turn-

<!-- Page 28 -->

28
by-turn verification to ensure effective step-by-step guidance over 100 subcategories, and iterative instruction refinement
toward task completion. Alongside TRAVER, they propose via suggester-editor pairs. This process yields a dataset of
DICT,anautomaticevaluationprotocolthatutilizescontrolled 25 million prompt-response pairs covering diverse skills such
student simulation and code generation tests to assess the as text editing, coding, creative writing, and reading compreperformanceoftutoringagentsholistically.SWE-Gym[178]is hension. When applied to fine-tune a Mistral-7B model, the
introducedasthefirstdedicatedenvironmentfortrainingreal- resulting Orca-3 model demonstrated significant performance
world software engineering (SWE) agents, designed around improvements ranging from 19% to 54% across benchmarks
2,438 Python task instances that include complete code- likeMMLU,AGIEval,GSM8K,BBH,andAlpacaEvalaswell
bases,executableruntimeenvironments,unittests,andnatural as a notable reduction in hallucinations for summarization
language task descriptions. This realistic setup allows for tasks. These findings underscore the potential of automated,
training language model–based SWE agents that significantly agentic synthetic data generation to enhance model capabiliimprove performance achieving up to 19% absolute gains in ties while reducing reliance on labor-intensive data curation,
resolve rate on popular test sets like SWE-Bench Verified and positioning AgentInstruct as a promising tool for advancing
Lite. Furthermore, the authors explore inference-time scaling LLM instruction tuning.
by employing verifiers trained on agent trajectories sampled
from SWE-Gym, which, when combined with their fine-

### MarketSenseAI

tuned agents, achieve state-of-the-art performance of 32.0% AgenticCrews [189] FinSphere
[190] [188]
on SWE-Bench Verified and 26.0% on SWE-Bench Lite.

### Multi-Agent

f) Multi-Agent Collaboration & Simulation: The works Coll [ a 1 b 8 o 7 r ] ation
by Yang et al. [179], Guo et al. [180], and Islam et al. [181]
contributesignificantadvancementstotheapplicationofLarge

### AgenticFinancial

Language Models (LLMs) in code understanding, collabora- M & od R e i l s in k g Stoc E k va A lu n a a t l i y o s n is&

### Citation-Enhanced Management Multi-Agent

tive software engineering, and code generation. Yang et al. [ C 1 S 91 A ] Fina [ n 1 c 8 i 6 al ] QA
[180] propose a novel multi-agent collaboration framework to

### Trustworthy Financial

bridge the gap between different programming languages. By S C ho o p n p v i e n r g sa A tio g n e a n l ts Re & aso Q n A ing
leveraging language-specific agents that collaborate and share

### Finance

knowledge, their approach enhances multilingual instruction Applications
t l u an n g in u g a , ge e s n . ab T l h in e g Q t w he en e 2 f . fi 5 c -x ie C n o t d t e r r an m sf o e d r e o l f de k m no o w ns le tr d a g te e s a s c u ro p s e s - A F S u i t n r t u o a c m n t c u a e r ti e & o d n C B o S e M m h tr a a a p v r t e k e io t e g i r t t i s i c v in e
r s e i h t o o r a w l p . c e a [ r s 1 f i 8 o n 0 r g m ] a i i t n n s c tr e p o o d i t u n e c n e m tia u S l l y ti t n l o i c n M g re u i d n a u d l c , p e a ro c g f r r o r a a s m m s- e m l w in i o n g r g u k al b t e h g n a a c t p h s d m . e a fi G r n k u e s o s , A S u F tr t [ i u o 1 n c m 8 a t n 2 u a c ] r ti e e o d n Si M mu ar la k t e i t on Dec I S i n s e v i q o e u s n e t - m n M t e i a a n k l t ing B St e [ r 1 h a 8 a te v 5 g i ] o ic r
the out-of-sync problem in collaborative software engineering. Through their SyncBench benchmark, which includes
over 24,000 instances of out-of-sync scenarios from realworld codebases, they highlight performance gaps in current TwinMarket FinCon
[183] [184]
LLM agents and emphasize the need for better collaboration and resource-awareness in AI systems. Finally, Islam Fig. 10: Agent LLM Applications in Finance
et al. [181] present CodeSim, a multi-agent code generation
framework that addresses program synthesis, coding, and 7) Finance Applications: Finance is a dynamic domain
debugging through a human-like perception approach. By where the adoption of LLM-based agents has opened new
incorporating plan verification and internal debugging via avenues for automation, simulation, analysis, and decision
input/outputsimulation,CodeSimachievesstate-of-the-artper- support. This subsection presents recent innovations that span
formance across multiple competitive benchmarks, including structured finance automation, market simulation, investment
HumanEval,MBPP,APPS,andCodeContests.Theirapproach decision-making, financial reasoning, stock analysis, and risk
demonstratesthepotentialforfurtherenhancementwhencou- management. Fig. 10 presents a classification of Agent LLM
pled with external debuggers, advancing the effectiveness of Applications for Finance.
code generation systems. a) Structured Finance and Automation: Wan et al. [182]
6) Synthetic data generation: Mitra et al. [138] propose investigate the integration of artificial intelligence into struc-
AgentInstruct,anovelframeworkthatleveragessyntheticdata tured finance, where the process of restructuring diverse asfor post-training large language models through a process sets into securities such as MBS, ABS, and CDOs presents
termed ”Generative Teaching.” Recognizing the challenges substantial due diligence challenges. The authors demonstrate
posedbythevaryingqualityanddiversityofsyntheticdataand thatAI,specificallylargelanguagemodels(LLMs),caneffectheextensivemanualcurationtypicallyrequiredAgentInstruct tively automate the verification of information between loan
automates the creation of high-quality instructional datasets applications and bank statements. While close-sourced modusing a multi-agent workflow. Starting from raw unstructured els like GPT-4 achieve superior performance, open-sourced
textandsourcecode,theframeworkemployssuccessivestages alternatives such as LLAMA3 provide a more cost-effective
of content transformation, seed instruction generation across option. Furthermore, implementing dual-agent systems has

<!-- Page 29 -->

29
been shown to further increase accuracy, albeit with higher agent approach significantly boosts performance, with an avoperational costs. erageincreaseof15%fortheLLaMA3-8Bmodeland5%for
b) MarketSimulation: Yangetal.[183]introduceTwin- the LLaMA3-70B model, compared to single-agent systems.
Market,amulti-agentframeworkthatharnesseslargelanguage Moreover, the proposed system performs comparably to and
models(LLMs)tosimulatecomplexsocio-economicsystems, sometimesexceedsthecapabilitiesofmuchlargersingle-agent
addressinglongstandingchallengesinmodelinghumanbehav- models such as LLaMA3.1-405B and GPT-4o-mini, although
ior. Traditional rule-based agent-based models often fall short it slightly lags behind Claude-3.5 Sonnet.
in capturing the irrational and emotionally driven aspects of f) Stock Analysis and Evaluation: Han et al. [187]
decision-making emphasized in behavioral economics. Twin- present a novel multi-agent collaboration system designed to
Market leverages the cognitive biases and dynamic emotional enhance financial analysis and investment decision-making by
responses inherent in LLMs to create more realistic simula- leveraging the collaborative potential of multiple AI agents.
tionsofsocio-economicinteractions.Thestudyillustrateshow Moving beyond traditional single-agent models, the system
individual agent behaviors can lead to emergent phenomena features configurable agent groups with diverse collaboration
such as financial bubbles and recessions when combined structuresthatdynamicallyadapttovaryingmarketconditions
throughfeedbackmechanismsthroughexperimentsconducted and investment scenarios through a sub-optimal combination
in a simulated stock market environment. strategy. The study focuses on three key sub-tasks fundac) Sequential Investment Decision-Making: Yu et al. mentals, market sentiment, and risk analysis applied to the
[184] propose FinCon, an LLM-based multi-agent framework 2023 SEC 10-K forms of 30 companies from the Dow Jones
designed to tackle the complexities of sequential financial Index. Experimental findings reveal significant performance
investment decision-making. Recognizing that effective in- improvements with multi-agent configurations compared to
vestment requires dynamic interaction with volatile environ- single-agent approaches, demonstrating enhanced accuracy,
ments, FinCon draws inspiration from real-world investment efficiency, and adaptability.
firm structures by establishing a manager-analyst communi- In a related study, Han et al. [188] introduce FinSphere,
cation hierarchy. This design facilitates synchronized, cross- a conversational stock analysis agent designed to overcome
functional collaboration through natural language interactions two major challenges faced by current financial LLMs: their
whileendowingeachagentwithenhancedmemorycapacity.A insufficient depth in stock analysis and the lack of objeckey component is the risk-control module, which periodically tive metrics for evaluating the quality of analysis reports.
triggers a self-critiquing mechanism to update systematic The authors make three significant contributions. First, they
investment beliefs, thereby reinforcing future agent behavior present Stocksis, a dataset curated by industry experts to
and reducing unnecessary communication overhead. FinCon enhance the stock analysis capabilities of LLMs. Second,
exhibits strong generalization across various financial tasks, they propose Analyscore, a systematic evaluation framework
such as stock trading and portfolio management, and offers a that objectively assesses the quality of stock analysis reports.
promising approach to synthesizing multi-source information Third, they develop FinSphere, an AI agent that leverages
for optimized decision-making in dynamic financial markets. real-time data feeds, quantitative tools, and an instructiond) Strategic Behavior in Competitive Markets: Li et al. tunedLLMtogeneratehigh-qualitystockanalysisinresponse
[185] investigate the strategic behavior of large language to user queries. Experimental results indicate that FinSphere
models (LLMs) when deployed as autonomous agents in outperforms general and domain-specific LLMs and existing
multi-commodity markets within the framework of Cournot agent-based systems, even when these systems are enhanced
competition. The authors examine whether these models can with real-time data and few-shot guidance.
independently engage in anti-competitive practices, such as Fatouros et al. [189] introduce MarketSenseAI, an innocollusion or market division, without explicit human interven- vative framework for comprehensive stock analysis that hartion. Their findings reveal that LLMs can monopolize specific nesses large language models (LLMs) to integrate diverse
commodities by dynamically adjusting pricing and resource financial data sources ranging from financial news, historical
allocation strategies, thereby maximizing profitability through prices, and company fundamentals to macroeconomic indicaself-directed strategic decisions. These results present signif- tors. Leveraging a novel architecture that combines Retrievalicant challenges and potential opportunities for businesses Augmented Generation with LLM agents, MarketSenseAI
incorporating AI into strategic roles and regulatory bodies processes SEC filings, earnings calls, and institutional reports
responsible for maintaining fair market competition. to enhance macroeconomic analysis. The latest advancements
e) Financial Reasoning and QA: Fatemi et al. [186] in the framework yield significant improvements in fundaaddress the limitations of large language models (LLMs) in mentalanalysisaccuracyoveritspreviousiteration.Empirical
financial question-answering (QA) tasks that require complex evaluationsonS&P100stocks(2023–2024)revealcumulative
numerical reasoning. Recognizing that multi-step reasoning returns of 125.9% versus the index’s 73.5%, while tests on
is essential for extracting and processing information from S&P 500 stocks in 2024 show a 33.8% higher Sortino ratio,
tables and text, the authors propose a multi-agent framework underscoringthescalabilityandrobustnessofthisLLM-driven
incorporatingacriticalagenttoevaluatethereasoningprocess investment strategy.
and final answers. The framework is further enhanced with g) Agentic Financial Modeling and Risk Management:
multiple critic agents specializing in distinct aspects of the Okpalaetal.[190]examineintegratinglargelanguagemodels
answer evaluation. Experimental results show that this multi- into agentic systems within the financial services industry,

<!-- Page 30 -->

30
focusing on automating complex modeling and model risk into manageable sub-tasks and compiling them into a strucmanagement (MRM) tasks. The authors introduce the concept tured memory library that can be referenced and refined in
of agentic crews, where teams of specialized agents, coordi- future queries. The framework incorporates three types of
natedbyamanager,collaborativelyexecutedistinctfunctions. memory and a library-enhanced reasoning component, en-
The modeling crew handles tasks such as exploratory data abling the system to improve over time through experience.
analysis,featureengineering,modelselection,hyperparameter Evaluations on four SciBench chemical reasoning datasets
tuning, training, evaluation, and documentation, while the reveal that ChemAgent achieves performance gains of up to
MRM crew focuses on compliance checks, model replication, 46%withGPT-4,significantlyoutperformingexistingmethods
conceptual validation, outcome analysis, and documentation. and suggesting promising applications in fields such as drug
The effectiveness and robustness of these agentic workflows discovery and materials science.
are demonstrated through numerical examples applied to b) MaterialsDiscovery&Design: Bycollaboratingwith
datasets in credit card fraud detection, credit card approval, materials science experts, Kumbhar et al. [193] curate a novel
and portfolio credit risk modeling, highlighting the potential dataset from recent journal publications that encapsulate realfor autonomous decision-making in financial applications. world design goals, constraints, and methodologies. Using
h) Trustworthy Conversational Shopping Agents: Zeng this dataset, they test LLM-based agents to generate viable
etal.[191]focusesonenhancingthetrustworthinessofLLM- hypotheses to achieve specified objectives under given conbased Conversational Shopping Agents (CSAs) by addressing straints.Torigorouslyassesstherelevanceandqualityofthese
two key challenges: the generation of hallucinated or unsup- hypotheses, a novel scalable evaluation metric is proposed
portedclaimsandthelackofknowledgesourceattribution.To that mirrors the critical assessment process of materials sciencombat these issues, the authors propose a production-ready tists. Together, the curated dataset, the hypothesis generation
solution that integrates a ”citation experience” through In- method, and the evaluation framework provide a promising
context Learning (ICL) and Multi-UX-Inference (MUI). This foundationforfutureresearchtoacceleratematerialsdiscovery
approach enables CSAs to include citation marks linked to and design using LLM. ChemAgent is a novel framework
relevant product information without disrupting user experi- that aims to enhance chemical reasoning by leveraging large
ence features. Additionally, the work introduces automated language models through a dynamic, self-updating library.
metricsandscalablebenchmarkstoevaluatethegroundingand
attribution capabilities of LLM responses holistically. Experimental results on real-world data indicate that incorporating Agen A t r T en ra a ding
[202]
thiscitationgenerationparadigmenhancesresponsegrounding
by 13.83%, ultimately improving transparency and building
customer trust in conversational AI within the e-commerce
domain.
8) ChemicalReasoning: Thedomainofchemicalreasoning R N e u a m so e n ri i c n a g l
poses complex challenges for large language models, including precise information processing, task decomposition, and
integrating scientific knowledge and code. In this subsection, PACE
[201]
wehighlightrecentadvancesindevelopingLLM-basedagents Solving

### Educational&

for chemical reasoning and materials discovery. M P at r h o e b m le a m ti s cal Ap T p u l t i o c r a i t n io g ns
a) Chemical Reasoning & Information Processing: The MATHVC
[200]
paperbyChoetal.[192]addressesthechallengesofdeploying
large language model (LLM)–powered agents in resource- MACM
[194]
constrainedenvironments,particularlyforspecializeddomains
Mathematical

### Reasoning

andless-commonlanguages,byintroducingTox-chataKorean &ProblemSolving
chemical toxicity information agent. It presents a context- MathLearner
[195]
efficient architecture utilizing hierarchical section search to
r g e e d n u e c r e atio to n ke m n et c h o o n d s o u l m og p y tio t n hat an d d ist a ills sce to n o a l r - i u o s - i b n a g sed cap d a i b a i l l o i g ti u e e s S P a [ m r 1 o 9 p m 6 li p ] n t g M [ A 19 -L 9 o ] T
from larger models. Experimental evaluations reveal that the F [1 lo 9 w 7] s KG [ - 1 P 9 r 8 o ] ofs
fine-tuned8B-parametermodelsignificantlysurpassesuntuned
models and baseline approaches in database faithfulness and Fig. 11: Agent LLM Applications in Solving Mathematical
user preference, offering promising strategies for developing Problems
efficient,domain-specificlanguageagentsunderpracticalconstraints. 9) Solvingmathematicalproblems: Mathematicalproblem-
Chemical reasoning tasks, which involve complex multi- solving remains a fundamental challenge for large language
step processes and require precise calculations, pose unique models due to the need for structured reasoning, formal logic,
challenges for LLMs especially in handling domain-specific and precise numerical computation. In this subsection, we
formulas and integrating code accurately. ChemAgent [139] presentrecenteffortstoenhancethemathematicalcapabilities
addresses these challenges by decomposing chemical tasks of LLM-based agents through novel prompting strategies,

<!-- Page 31 -->

31
TABLE X: Overview of AI Agent Applications for Mathematical Problem Solving
Agent/Tool Year MathTask PrimaryObjective Architecture& KeyOutcomes& ProofVal. SolverIntegr. NotationSup.

### Workflow Metrics

MACM[194] 2024 Advanced Solvemulti-stepmath Multi-Agent MATHlevel5
Reasoning problemswithrobust ConditionalMining accuracyincreasefrom
generalization. promptingforiterative 54.68%to76.73%on
refinement. GPT-4Turbo.
MathLearner 2024 Inductive EnhanceLLM Retrievalmoduleplus +20.96%global
[195] Reasoning reasoningvia proceduralknowledge accuracy;solves
inductiveretrievaland injectionininductive 17.54%previously
application. loop. unsolvedproblems.
PromptSampling 2024 Search Combinediverse Uniformsampling 43%fewerrunsfor
[196] Space promptingmethodsto overmultipleprompt MATH-hardwith
Expansion expandsearchspace strategies;fewer maximalcoverage.
efficiently. inferenceruns.
Flows[197] 2024 Reasoning Generatedetailed CollaborativeLLM Significant
Trace mathreasoningtraces ensemblewithonline improvementin
online. DPOandrollouts. reasoningquality
versusdirectinference.
KG-ProofAgent 2025 ProofCon- Automate IntegratesconceptKG 34%successon
[198] struction formalizationof withLLMtostructure MUSTARDSAUCE;
proofsusing lemmasandsteps. 2–11%improvement
knowledgegraphs. overbaselines.

### MA-LoT[199] 2025 Theorem Synergize Multi-agent 61.07%on

Proving natural-language chain-of-thoughtplus MiniF2F-Test(Lean4)
reasoningwithLean4 LoT-Transferpipeline versus22.95%for
verificationfeedback. inLean4. GPT-4.
MATHVC[200] 2024 Educational Simulategroup Virtualclassroomwith Realisticdialog;
Modeling discussionsfor diversestudent-agents improvesmodeling
mathematical andmetaplanning. taskperformance.
modelingskills.
PACE[201] 2025 Personalized Tailormathinstruction Felder-Silverman Higherengagement
Tutoring tolearningstyleswith personasplusSocratic andoutcomesversus
Socraticfeedback. methodandtailored traditionaltutors.
data.
AgentTrading 2025 Numerical Improvenumeric Virtualstockgame Enhancedgeometric
Arena[202] Reasoning inferencewithvisual plusanalysisover reasoning;validated
dataandreflection. plotsandcharts. onNASDAQdataset.
ProofVal.:ProofValidation;SolverIntegr.:Solver&AssistantIntegration;NotationSup.:Notation&FormalismSupport: :Partial; :NotSupported; :Supported.
collaborative agent systems, theorem proving, and knowledge ing information and applying prior knowledge to new tasks,
integration. Fig. 11 presents a classification of agent LLM the framework significantly outperforms traditional chain-ofapplications for solving mathematical problems. thought approaches. Specifically, it improves global accuracy
a) Mathematical Reasoning and Problem Solving: The by 20.96% and can solve 17.54% of mathematical problems
paper by Lei et al. [194] tackles the challenge of ad- thatthebaselinefailstoaddress.Akeyframeworkcomponent
vanced mathematical problem-solving in large language mod- is its efficient retrieval method, which enables the model to
els (LLMs), where performance significantly declines despite effectively incorporate external knowledge and support mathrecent advancements like GPT-4. While methods such as Tree ematical computations based on explicit written procedures.
of Thought and Graph of Thought have been explored to Lee et al. [196] investigate the limitations of traditional
enhance logical reasoning, they face notable limitations: their single prompting methods in large language models (LLMs)
effectiveness on complex problems is limited, and the need for mathematical reasoning and explore alternative prompting
forcustompromptsforeachproblemrestrictsgeneralizability. strategies.Itexperimentallydemonstratesthatdistinctprompt-
In response, the authors introduce the Multi-Agent System ingmethodseachprobeuniquesearchspaces,adifferentiation
for Conditional Mining (MACM) prompting method. MACM that becomes more pronounced with increased problem comsuccessfully addresses intricate, multi-step mathematical chal- plexity. To capitalize on this diversity, the study introduces
lengesandexhibitsrobustgeneralizationacrossdiversemathe- anefficientsamplingprocessthatuniformlycombinesoutputs
maticalcontexts.Notably,usingMACM,theaccuracyofGPT- from these varied methods, thereby expanding the overall
4TurboonlevelfiveproblemsintheMATHdatasetimproves search space and achieving improved performance with fewer
markedly from 54.68% to 76.73%, demonstrating its potential inference runs. Notably, for the particularly challenging probto elevate LLM inferential capabilities substantially. lemsintheMATH-hardsubset,theapproachreachedmaximal
Xie et al. [195] present an agent framework designed to search space utilization with approximately 43% fewer runs
enhance the mathematical reasoning abilities of large lan- compared to individual methods.
guage models (LLMs) through inductive reasoning. Drawing Deng et al. [197] introduce a novel approach to enhance
inspiration from the human learning process of generaliz- the generation of detailed and accurate reasoning traces in

<!-- Page 32 -->

32
large language models (LLMs), particularly for mathemati- toindividuallearnercharacteristics.PACEleveragestheFelder
cal reasoning tasks. The authors propose an online learning andSilvermanlearningstylemodeltosimulatedistinctstudent
framework termed ”Flows,” where component LLMs work personas, enabling the system to tailor teaching strategies
collaboratively and iteratively, engaging in incremental output to diverse learning styles a crucial factor for enhancing enproductiontobuildcoherentsolutions.Centraltotheapproach gagement and comprehension in mathematics. Integrating the
is online Direct Preference Optimization (DPO) with rollouts, Socratic teaching method, PACE provides instant, reflective
which generates DPO pairs for each training example and feedback that encourages deeper cognitive processing and
updates the models in real-time. By directly comparing the critical thinking. The framework also involves constructing
quality of reasoning traces produced by this method against personalized teaching datasets and training specialized modthose generated by standard direct model inference, the study els, which facilitate identifying and adapting each student’s
demonstrates that the proposed Flow framework significantly uniqueneeds.Extensiveevaluationsusingmulti-aspectcriteria
improves LLM performance in mathematical reasoning. demonstrate that PACE outperforms traditional methods in
Li et al. [198] introduce a novel framework that augments personalizing the educational experience and boosting student
large language models (LLMs) with knowledge graphs to motivation and learning outcomes.
improve the construction and formalization of mathematical c) Numerical Reasoning: Ma et al. [202] investigate
proofs. The proposed approach tackles persistent challenges the limitations of large language models (LLMs) in handling
inautomatingtheidentificationofkeymathematicalconcepts, dynamic and unseen numerical reasoning tasks, mainly when
understanding their relationships, and embedding them within operating on plain-text data. To address this, the authors
rigorous logical frameworks. Experimental results show sig- introduce the Agent Trading Arena a virtual numerical game
nificant performance gains, with the framework achieving up simulating complex economic systems via zero-sum stock
to a 34% success rate on the MUSTARDSAUCE dataset on portfolioinvestmentswhichbetterreflectsreal-worldscenarios
o1-mini and consistently outperforming baseline models by where optimal solutions are not clearly defined. Experimental
2–11% across various benchmarks. results indicate that LLMs, including GPT-4o, face challenges
Wang et al. [199] introduce MA-LoT, a novel multi-agent with algebraic reasoning in textual formats, often focusing on
frameworkdesignedfortheLean4theoremprovingthatitsyn- local details at the expense of broader trends. In contrast,
ergizeshigh-levelnaturallanguagereasoningwithformallan- when LLMs are provided with visual data representations,
guageverificationfeedback.Unliketraditionalsingle-agentap- suchasscatterplotsorK-linecharts,theyexhibitsignificantly
proaches that either generate complete proofs or perform tree enhanced geometric reasoning capabilities. This improvement
searches, MA-LoT leverages structured interactions among is further enhanced by incorporating a reflection module that
multiple agents to maintain long-term coherence and deeper facilitates the analysis and interpretation of complex data.
insight during proof generation. The framework employs a ThesefindingsarevalidatedusingtheNASDAQStockdataset,
novel LoT-Transfer Learning training-inference pipeline that underscoring the value of visual inputs for bolstering numerharnesses long chain-of-thought processes’ emergent formal ical reasoning in LLMs.
reasoning abilities. Extensive experiments demonstrate that 10) Geography Applications: Yu et al. [203] introduce
MA-LoT achieves a 61.07% accuracy on the Lean4 ver- MineAgent, a modular framework designed to enhance the
sion of the MiniF2F-Test dataset, significantly outperforming capabilities of multimodal large language models (MLLMs)
baselines such as GPT-4 (22.95%), single-agent tree search in the domain of remote-sensing mineral exploration. This
methods (50.70%), and whole-proof generation techniques field presents significant challenges, including the need for
(55.33%).Theseresultsunderscorethepotentialofintegrating domain-specific geological knowledge and the complexity of
long chain-of-thought reasoning with formal verification to reasoning across multiple remote-sensing images, which is
enhance automated theorem proving. further complicated by long-context issues. MineAgent adb) Educational and Tutoring Applications: Yue et al. dresses these challenges by incorporating hierarchical judg-
[200] introduce MATHVC, a pioneering virtual classroom ing and decision-making modules to improve multi-image
powered by large language models (LLMs) designed to en- reasoning and spatial-spectral integration. In addition, the
hance students’ mathematical modeling (MM) skills through authors propose MineBench, a specialized benchmark to evalcollaborative group discussions. Recognizing that traditional uate MLLMs on mineral exploration tasks using geological
MM practice often suffers from uneven access to qualified and hyperspectral data. Extensive experiments demonstrate
teachers and resources, the authors leverage LLMs’ capabil- the effectiveness of MineAgent, showcasing its potential to
ities to simulate diverse student characters, each embody- significantlyadvancetheuseofMLLMsinthecriticalareaof
ing distinct math-relevant properties. To ensure that these remote-sensing mineral exploration
simulated interactions mirror authentic student discussions, Ning et al. [204] introduce an autonomous geographic
the framework incorporates three key innovations: integrating information system (GIS) agent framework that utilizes large
domain-specific MM knowledge into the simulation, defining language models (LLMs) to perform spatial analyses and
a symbolic schema to ground character behaviors, and em- cartographic tasks. A significant research gap in the field has
ploying a meta planner to guide the conversational flow. been the ability of these agents to autonomously discover
Liu et al. [201] introduce the Personalized Conversational and retrieve the necessary geospatial data. The proposed
Tutoring Agent (PACE) for mathematics instruction, address- framework addresses this by generating, executing, and deingacriticalgapinintelligenteducationalsystemsbyadapting bugging programs to select data sources from a predefined

<!-- Page 33 -->

33
list, using source-specific handbooks that document metadata filmproduction,musicandpoetrygeneration,dramascripting,
and retrieval details. The framework is designed in a plug- fashion assistance, and lyric composition. Fig. 12 presents a
and-play style, allowing users or automated crawlers to easily classification of agent LLM applications for Multimedia.
add new data sources by creating additional handbooks. A a) Film Automation Agents: Xu et al. [205] introduce
prototype of the agent has been developed as a QGIS plugin FilmAgent, an innovative LLM-based multi-agent collaboraand Python program. Experimental results demonstrate its tive framework designed to automate end-to-end film procapability to retrieve data from various sources, including duction within 3D virtual spaces. Virtual film production
OpenStreetMap,U.S.CensusBureaudemographicdata,satel- involves complex decision-making, including scriptwriting,
litebasemapsfromESRI,globaldigitalelevationmodelsfrom cinematography, and actor positioning. FilmAgent simulates
OpenTopography,weatherdata,andCOVID-19casedatafrom various crew roles such as directors, screenwriters, actors,
the NYTimes GitHub. This work is one of the first efforts to and cinematographers, covering crucial stages of the film
create an autonomous GIS agent for geospatial data retrieval, production process. These stages include idea development,
marking a significant advancement in spatial data automation. where brainstormed ideas are transformed into structured
story outlines; scriptwriting, which generates dialogues and
Melody-Lyric character actions; and cinematography, which determines the
Agents camerasetupsforeachshot.Theagentscollaborateiteratively,
[212]
providingfeedbackandrevisionstoverifyintermediatescripts
Multi-Agent andreducehallucinations.Evaluationsofthegeneratedvideos

### Poetry

Framework on 15 ideas across four key aspects show that FilmAgent
[211] outperforms all baselines, achieving an average score of 3.98
Lyric out of 5. Despite using the GPT-4o model, FilmAgent sur-

### Generation

Agents passes the single-agent o1, demonstrating the benefits of a
Poetry coordinated multi-agent system.

### Generation MusicAgent

Agents [210] b) Story-to-Video Production Agents: Wang et al. [206]
introduce AesopAgent, an Agent-driven Evolutionary Sys-

### Music

Under- tem designed for story-to-video production, leveraging the
standing&
Generation advancements in Agent and Artificial Intelligence Generated
Agents Content(AIGC)technologies.AesopAgentintegratesmultiple
ComposerX generative capabilities within a unified framework, enabling
Sy M m u b s o ic lic [209] users to easily convert story proposals into scripts, images,
Composition audio, and videos. The system orchestrates the entire video

### Agents

Multimedia generation workflow, ensuring that the generated content is
Applications both rich and coherent. The system consists of two layers:

### Fashion-Domain

the Horizontal Layer and the Utility Layer. The Horizontal

### Conver- Fashion

sational Assis- Layer incorporates a novel RAG-based evolutionary system

### Agents tant

that continuously optimizes the video production process by
Eval.
[208] accumulating expert knowledge and refining workflow steps,

### Drama


### Script suchasLLMpromptoptimization.TheUtilityLayerprovides

Generation essentialtoolsforconsistentimagegeneration,ensuringvisual

### Agents

coherenceintermsofcomposition,characters,andstyle,while
Story-to-Video IBSEN also integrating audio and special effects.
Pr A od g u e c n t t i s on [207] c) Drama Script Generation Agents: Han et al. [207]
FilmAu- introduce IBSEN, a director-actor coordination agent frametomation
work designed to generate drama scripts and provide greater

### Agents

control over the plot development, especially in scenarios
AesopAgent where human players are involved. While current language
[206]
model agents excel at creating individual behaviors for characters, they often struggle with maintaining consistency and
FilmAgent coherence at the storyline level. IBSEN addresses this by
[205]
introducing a director agent that writes plot outlines based on
Fig. 12: Agent LLM Applications in Multimedia user input, instructs actor agents to role-play their respective
characters, and adjusts the plot as needed to ensure that
11) Multimedia Applications: Multimedia is an emerging the narrative progresses toward the intended objective. The
frontierforLLM-basedagents,wherecreativeandinterpretive framework was evaluated using a novel drama plot involving
tasksrequirecoordinationacrossdiversemodalities,including multiple actor agents, where the interactions were guided by
text, audio, image, and video. In this subsection, we present the director agent. The results demonstrate that IBSEN is carecent advancements in applying agent-based language learn- pableofgeneratingdiverseandcompletedramascriptsfroma
ing and machine learning (LLM) systems to domains such as rough plot outline, while preserving the unique characteristics

<!-- Page 34 -->

34

### TABLE XI: Overview of AI Agent Applications for Multimedia

Agent/Tool Year Domain PrimaryObjective Architecture& KeyOutcomes& Eval.Metrics Pipeline Fmt.Compat.
Workflow Metrics Integr.
FilmAgent[205] 2025 Film Fullyautomate Multi-agentroles Outperforms Meanuser Virtualstudio Exports
Automation end-to-end3Dvirtual (director, single-agentbaselines score3.98/5 pipeline MP4/WebM
filmproduction. screenwriter,actors, withcoherentvideo support
cinematographer) across15scenarios.
withiterative
feedbackloops.
AesopAgent 2024 Story→Video Convertstorydrafts Two-layer Rich,coherent Workflow Integrateswith Supports
[206] intoscripts,images, RAG-evolutionary multimodaloutputs convergence AIGCasset PNG,WAV,
audio,andvideo. workflowplusutility withcontinuous rate≈85% generators MP4
layerfor optimization.
image/audio/effects.
IBSEN[207] 2024 Drama Generatecoherent Directoragent Diverse,complete Narrative Scriptwriting Plain-text
Scripts dramascriptsvia outlinesplot;actor scriptspreserving coherence¿ toolchain scriptoutput
director–actor agentsrole-playand charactertraits. 90%(human compatible
coordination. adjustnarrative. eval)
Fashion-Agent 2024 Conversational Enhanceonline LLMfront-end 4000-dialogdataset; Precision@5: E-commerce JSON/
[208] Retail fashiondiscovery connectstosearch& improvesretrieval 78% API HTMLwidget
withLLMdialogue recommendation relevanceby18%. integration
agents. backends.
ComposerX[209] 2024 Music Multi-agentsymbolic Agentsspecializein Coherentpolyphonic Subjective MIDIpipeline Standard
Composi- musicgenerationwith melody,harmony,and piecesratedhighon rating4.2/5 plugin MIDIfiles
tion harmonyconstraints. structureusingLLM musicality.
reasoning.
MusicAgent 2023 Music Orchestratediverse Autonomoustask Simplifiestooluse; Task Integrates WAV,MP3,
[210] Processing musictasksvia decompositionand reducesdevelopment completion FFmpeg, MIDI
unifiedLLMagent. toolinvocationover effortby40%. time↓40% Librosa,Web

### HF/GitHub/APIs. APIs

PoetryAgents 2024 Poetry Boostdiversity& Cooperative& +3.0–3.7ppdiversity; Distinct Textpipeline UTF-8text
[211] Generation noveltyin non-cooperativeagent +5.6–11.3ppnovelty. n-gram↑11% integration

### LLM-generated interactionson

poetryviamulti-agent GPT-2/3/4.
sociallearning.
LyricAgents 2024 Lyric Melody-to-lyric Agentsforrhyme, Listeningtest Alignment Singing-synth LRC/JSON
[212] Generation alignmentintonal syllable,alignment& accuracy85%. score0.87 pipelineready lyricfiles
languageswith consistency;evaluated
multi-agentsub-tasks. viasingingsynth.
Eval.Metrics:EvaluationMetrics;PipelineIntegr.:PipelineIntegration;Fmt.Compat.:FormatCompatibility.
of each character, showing the effectiveness of the framework LLMs have demonstrated impressive performance in STEM
in producing controlled, dynamic narrative content. domains, they often struggle with music composition, pard) Fashion-Domain Conversational Agents: Maroniko- ticularly when dealing with long dependencies and harmony
lakis et al. [208] focus on the potential of Large Language constraints. Even when equipped with advanced techniques
Models (LLMs) to revolutionize online fashion retail by en- like In-Context Learning and Chain-of-Thought, LLMs typihancing customer experiences and improving product discov- cally generate poorly structured music. ComposerX aims to
erythroughconversationalagents.TheseLLM-poweredagents address this by leveraging the reasoning abilities of LLMs
allow customers to interact naturally, refining their needs andtheirextensiveknowledgeofmusichistoryandtheory.By
and receiving personalized fashion and shopping advice. For employingamulti-agentapproach,theframeworksignificantly
taskslikefindingspecificproducts,conversationalagentsmust enhancesthemusiccompositionqualityofGPT-4.Theresults
translate customer interactions into calls to various backend show that ComposerX is capable of generating coherent,
systems, such as search engines, to display relevant product polyphonic music compositions with engaging melodies that
options. The authors emphasize the importance of evaluating followuserinstructions,markingasubstantialimprovementin
thecapabilitiesofLLMsinthesetasks,particularlyinintegrat- the application of LLMs to creative music composition tasks.
ing with backend systems. However, existing evaluations are f) Music Understanding & Generation Agents: Yu et al.
oftencomplexduetothelackofhigh-quality,relevantdatasets [210] present MusicAgent, a system designed to streamline
that align with business needs. To address this, the authors AI-powered music processing by organizing and integratdeveloped a multilingual evaluation dataset comprising 4,000 ing diverse music-related tasks. Music processing spans a
conversations between customers and a fashion assistant on a wide range of activities, from generation tasks like timbre
large e-commerce platform. synthesis to comprehension tasks like music classification.
e) Symbolic Music Composition Agents: Deng et al. However, developers and amateurs often struggle to navigate
[209] introduce ComposerX, an agent-based symbolic music the complexity of these tasks, particularly due to the varying
generation framework designed to enhance the music compo- representationsofmusicdataandtheapplicabilityofdifferent
sition capabilities of Large Language Models (LLMs). While modelsacrossplatforms.MusicAgentaddressesthischallenge

<!-- Page 35 -->

35
by offering an integrated solution that simplifies the process C. AI Agents Protocols
for users. The system includes a comprehensive toolset that
Recent advances in autonomous AI systems have undergathers music tools from diverse sources such as Hugging
scored the importance of standardized communication proto-
Face, GitHub, and Web APIs. Additionally, it incorporates an
cols in facilitating seamless interaction among agents, tools,
autonomous workflow powered by Large Language Models
and external services. In this subsection, we present three
(LLMs), like ChatGPT, which organizes these tools and auprominentprotocolsdevelopedbetween2024and2025:Agent
tomatically decomposes user requests into sub-tasks, invoking

### Communication Protocol (ACP), Model Context Protocol

the appropriate tools. The primary goal of MusicAgent is to
(MCP), and Agent-to-Agent Protocol (A2A).
alleviateusersfromthetechnicalitiesofusingAI-basedmusic
1) Agent Communication Protocol (ACP): In 2025, IBM
tools,allowingthemtofocusonthecreativeaspectsofmusic.

### Researchproposedtheagent-to-agentcommunicationprotocol

g) Poetry Generation Agents: Zhang et al. [211] intro- named ACP, which is central to the operation of BeeAI1,
duces a framework for enhancing the diversity and novelty of an experimental platform designed to streamline the orchespoetry generated by Large Language Models (LLMs) by in- tration and execution of open-source AI agents, regardless
corporatingsociallearningprinciples.WhileLLMshavemade of their underlying framework or code base. The primary
significantstridesinautomaticpoetrygeneration,theiroutputs goalofACPistostandardizecommunicationbetweenagents,
oftenlackthediversityandcreativityseeninhuman-generated addressing challenges posed by inconsistent interfaces and
poetry. The proposed framework emphasizes both cooperative enabling seamless interaction across diverse agents and client
and non-cooperative interactions among multiple agents to systems. Inspired by Anthropic’s MCP, ACP initially aimed
foster diversity in generated poetry. This is the first attempt to to connect agents to data and tools but has since evolved to
applymulti-agentsystemsinnon-cooperativeenvironmentsfor include advanced features such as discovery, delegation, and
poetry generation, utilizing both TRAINING-BASED agents multi-agent orchestration. Core components of BeeAI include
(GPT-2) and PROMPTING-BASED agents (GPT-3 and GPT- the BeeAI Server, which orchestrates agent processes in a
4). Experiments based on 96k generated poems show sig- local-first environment and provides a unified REST endpoint
nificant improvements, particularly for TRAINING-BASED for external apps and UIs, and the ACP SDKs, which offer
agents, with a 3.0–3.7 percentage point increase in diver- librariesinPythonandTypeScript,alongwithacommand-line
sity and a 5.6–11.3 percentage point increase in novelty, as interface and UI for easy agent discovery and launch [214].
measured by distinct and novel n-grams. The results also
2) ModelContextProtocol(MCP): Inlate2024,Anthropic
reveal that poetry generated by these agents shows increased
introduced the Model Context Protocol (MCP), an open and
divergence in terms of lexicons, styles, and semantics. For
flexible protocol that standardizes how AI systems interact
PROMPTING-BASED agents, the non-cooperative environwith external tools and data sources, much like a USB-C
ment helps enhance diversity, with an increase of 7.0–17.5
port provides a universal connection for devices. Inspired by
percentage points, though these agents showed a decrease in
the Language Server Protocol, MCP enables AI agents to
lexical diversity over time and did not exhibit the desired
autonomouslyidentify,select,andmanageawiderangeofsergroup-based divergence.
vices based on the specific context of each task. The protocol
h) Lyric Generation Agents: Liu et al. [212] address facilitates the development of complex workflows by offering
the challenges of melody-to-lyric generation by leveraging a growing catalog of pre-built integrations, the flexibility to
Generative Large Language Models (LLMs) and multi-agent switch between different LLM providers, and best practices
systems. Previous research in this area has been constrained forsecuringdatawithinanorganization’sinfrastructure[216].
by limited high-quality aligned data and unclear standards for Anexpandingecosystemofservershighlightstheprotocol’s
creativity.Manystudiesfocusedonbroadthemesoremotions, potential. For example, official reference servers demonstrate
which have limited value given the advanced capabilities MCP’s core capabilities through secure file management and
of current language models. In tonal contour languages like database access, utilizing PostgreSQL, SQLite, and Google
Mandarin,wherepitchcontoursareinfluencedbybothmelody Drive. At the same time, development environments benefit
and tone, achieving a good fit between lyrics and melody from integration with tools such as Git, GitHub, and GitLab.
becomesmorecomplex.Thestudy,validatedbytheMpop600 Moreover, MCP supports productivity and communication
dataset, demonstrates that lyricists and melody writers care- enhancements via integrations with platforms like Slack and
fully consider this fit during their composition process. To GoogleMapsandevenextendstospecializedAItools,includtacklethis,theauthorsdevelopedamulti-agentsystemthatde- ing image generators and sophisticated search APIs2.
composesthemelody-to-lyrictaskintospecificsub-tasks,with MCP is designed around a client-server architecture in
individual agents managing aspects such as rhyme, syllable whichhostapplicationsconnecttomultiplelightweightservers
count,lyric-melodyalignment,andconsistency.Thequalityof [213]. This allows secure access to local data sources such as
thegeneratedlyricswasevaluatedthroughlisteningtestsusing files and databases and remote services available through web
a diffusion-based singing voice synthesizer, assessing how APIs. By unifying these interfaces, MCP transforms everyday
different agent groups performed in terms of lyric creation. platforms into versatile, multi-modal AI agents, simplifying
This work introduces a more structured approach to melodyto-lyric generation, offering a deeper understanding of the 1https://github.com/i-am-bee/beeai-framework
interaction between melody and lyrics in tonal languages. 2https://github.com/modelcontextprotocol/servers

<!-- Page 36 -->

36
tneilC

## A2A

tneilC

## A2A

tneilC

## A2A

tneilC

## A2A

Remote

### Agent

Remote

### Agent

Remote

### Agent

Remote

### Agent

revreS

## A2A

CrewAI

### Agent

revreS

## A2A

LangChain

### Agent

revreS

## A2A

Haystack

### Agent

revreS

## A2A

A2A protocol
A2A protocol

## Mcp Mcp

Client protocol

### A2A protocol

Microsoft AutoGen

### Agent

,.g.e(
ledoM
egaugnaL
egraL
krowemarF
tnegA
).cte...
,newQ
,keeSpeeD

## Ipa

retuoRnepO
tiK
tnempoleveD
tnegA
Allow a diverse selection of MCP Enabling dynamic, multimodal interactions among Enable agents to interface with tools, APIs,
servers to be integrated with various agents without requiring shared memory, and resources using standardized structured
agents. Agent A resources, or tools. Agent B inputs and outputs.

### MCP Host MCP Host


## Mcp Mcp Mcp Mcp Mcp Mcp

Server protocol Client Client protocol Server
Local Data Local Data
Source 1 Source 3

## Mcp Mcp Mcp Mcp

Server protocol Client Server

### Local Data

Local Data Source 4

### Source 2

MCP MCP MCP MCP MCP MCP Server protocol Client Client protocol Server A2A protocol

### Remote

Remote Service

### Service


### Front-End Front-End


### Web Browser - User Web Browser - User

Fig. 13: Multi-Agent Integration Framework: Enabling dynamic collaboration through the A2A and MCP Protocols.
the creation of AI-native applications and accelerating inno- crosoft AutoGen, which communicate via the A2A protocol.
vation across diverse domains. This communication method allows agents to collaborate
3) Agent-to-Agent Protocol (A2A): In 2025, Google intro- dynamically without sharing internal memories, resources, or
duced the Agent2Agent (A2A) protocol to usher in a new tools, ensuring secure and efficient inter-agent exchanges. In
eraofseamlessinteroperabilityamongAIagents,significantly parallel, the framework utilizes the MCP protocol to stanenhancing workplace productivity and automation [215]. The dardize interactions with various tools, APIs, and resources,
protocol is designed to facilitate dynamic collaboration be- enabling agents to connect with both local data sources and
tween autonomous agents, enabling them to work together remote services through structured inputs and outputs.
across isolated data systems and diverse applications regard- Tab. XII provides a comparative analysis of three agent
lessoftheirunderlyingframeworksorvendors.Usingfamiliar communication protocols: MCP, ACP, and A2A. It highlights
standardssuchasHTTP,SSE,andJSON-RPC,A2Asimplifies their primary purpose, typical setup, core features, and ideal
integrationwithexistingITinfrastructureswhilealsoensuring use cases. MCP (Model Context Protocol) focuses on inrobust enterprise-grade security through proven authentication tegrating data and tools into LLM workflows, providing a
and authorization practices. A2A supports both swift and standardized interface for delivering context. ACP (Agent
long-duration tasks by allowing agents to exchange real-time Communication Protocol), a component of the BeeAI platupdates, negotiate user interface requirements, and perform form, enables communication among multiple agents in a
capability discovery via structured ”Agent Cards. local-first setup, providing tools for agent discovery and
MCP is designed to connect agents with tools, APIs, and telemetry.Incontrast,A2A(Agent-to-AgentProtocol)enables
resources through structured inputs and outputs. It is fully interoperability between agents across different frameworks,
supported by Google’s ADK, which enables a wide range of allowing them to exchange tasks and collaborate. The table
MCP servers to be seamlessly integrated with AI agents. In highlights the distinct roles these protocols play in agentparallel, A2A 3 provides a dynamic, multimodal framework based systems, with MCP focusing on data integration for
foragent-to-agentcommunication,allowingdifferentagentsto LLMs, ACP concentrating on local agent orchestration, and
collaborate without sharing memory, resources, or tools. Fig. A2A facilitating cross-platform collaboration among agents.
13 presents a sophisticated multi-agent integration framework

### D. Training datasets

that leverages two key protocols A2A and MCP to enable
seamless interactions among diverse agents and services. It High-quality training datasets are crucial for enhancing
depicts multiple remote agents, including those branded as the reasoning, multilingual understanding, and instruction-
CrewAI Agent, LangChain Agent, Haystack Agent, and Mi- followingabilitiesoflargelanguagemodels.Inthissubsection,
we present three recently developed datasets: NaturalReason-
3https://google.github.io/A2A/ ing, FineWeb2, and MagPie-Ultra. Each dataset addresses

<!-- Page 37 -->

37

### TABLE XII: Comparison of MCP, ACP, and A2A Protocols

Feature MCP (Model Context Protocol) ACP (Agent Communication A2A (Agent-to-Agent
[213] Protocol)[214] Protocol)[215]
MainPurpose Facilitates access to context and Enables communication between multiple Facilitates communication and
dataforLLMs agentswithinBeeAI task-sharingbetweenagentsacross
frameworks
CommonSetup Distributed servers providing spe- BeeAI Server coordinates and manages Agents from different frameworks
cific data, connected via an MCP multipleagentswithinalocalenvironment discover and connect through
hub HTTPinterfaces
KeyCapabilities Standardizedinterfaceforconnect- Simplifiesagentdeployment,discovery,and Allows agents to discover each
ingdataandservicestoLLMs offersdeeptelemetrywithinBeeAI other’scapabilitiesandsharetasks
withupdates
TypicalApplication Managing context for LLMs and Managing multiple agents within BeeAI’s Enablinginteractionandcollaboraintegratingdatastreams environment tion between agents from diverse
systems
CoreObjective Uniformly managing how LLMs Standardizing communication between Creatingastandardizedmethodfor
receivecontextandexternaltools BeeAIagentsandexternalsystems agents from different systems to
communicateandcollaborate
Architecture Client-server model where LLMs BeeAIServerorchestratestheinteractionof Agents connect through agent
hookintoserversfordataandtools local agents and integrates external frame- cardsandHTTPfortaskexecution
works andcommunication
KeyDifferences Focuses on integrating tools and Primarily focused on internal coordination Aims at linking agents across difdataintoasingleLLMprocess ofagentswithinBeeAI ferentecosystemstocollaborateeffectively
IdealUsageScenario Integratingmultipledatasourcesor Running and managing various agents Connecting agents from different
servicesintoanLLMworkflow withinBeeAI’senvironment platforms to enable collaboration
andtask-sharing
CommonUseCases Implementing controlled, secure Orchestrating multi-agent environments Enabling task sharing and agent
LLMworkflowswithexternaldata withBeeAI’splatform communication across different
vendorsystems
different aspects of model training, ranging from expanding configurations, FineWeb2 employs innovative techniques such
reasoning across multiple domains to enhancing multilingual as”re-hydration”deduplicationandlanguage-specificfiltering
capabilities and advancing the generation of synthetic instruc- to ensure high data quality. Extensive ablation experiments,
tions. conducted with a 1.45 billion-parameter model trained on
1) NaturalReasoning dataset: Scaling reasoning capabili- 30 billion tokens, further validate the dataset’s robustness.
ties beyond traditional domains such as math and coding has In comparative evaluations against established datasets like
been challenging due to the scarcity of diverse, high-quality CC-100, mC4, CulturaX, and HPLT, FineWeb2 consistently
questions. In response, [217] introduces NaturalReasoning a outperforms across diverse languages. Additionally, specialcomprehensive dataset comprising 2.8 million questions that ized evaluations using the FineTasks benchmark on 9 varied
span multiple domains, including STEM fields (like Physics languages underscore its potential for advancing multilingual
andComputerScience),Economics,andSocialSciences,com- natural language processing and retrieval-augmented generapletewithreferenceanswers.Thedatasetisdesignednotonly tion applications.
to serve as a resource for knowledge distillation experiments, 3) MagPie-Ultradataset: MagPie-Ultra[219]isasynthetic
where it effectively transfers reasoning capabilities from a dataset generated using Meta Llama 3.1 405 B-Instruct FP8,
strong teacher model, but also for unsupervised self-training representing the first open dataset of its kind. It comprises
using external reward models. When training the Llama3.1- 50,000 synthetic instruction pairs, created by prompting the
8B-Instruct model, NaturalReasoning demonstrates superior language model with minimal ”empty” prompts (only initial
scaling effects, achieving notably higher average performance special tokens) that allow it to generate both user queries and
on benchmarks such as MATH, GPQA, and MMLU-Pro corresponding responses auto-regressively. These generated
compared to other datasets. This work highlights the potential pairs, filtered according to the MagPie recipe and refined via
of a large, diverse question dataset to expand the boundaries Argilla distilabel, cover a diverse range of challenging tasks,
of LLM reasoning across a broader range of fields. includingcoding,mathematics,dataanalysis,creativewriting,
2) FineWeb2 dataset: Hugging Face’s team introduced advice seeking, and brainstorming. In addition to the raw
[218] FineWeb2, a groundbreaking multilingual dataset com- instructionpairs,thedatasetincludesdetailedmetadataquality
prising 8TB of meticulously cleaned text data with over and difficulty scores, embeddings, topic labels, and safety as-
3 trillion non-English words drawn from more than 1,000 sessments from tools like ArmorRM and LlamaGuard, which
languages.FineWeb2supportsatotalof1,893languages,with furthersupportitsuseintrainingandevaluatinglargelanguage
substantial coverage 486 languages include more than 1MB models across complex instruction-following scenarios.
of data and 80 languages boast over 1GB each demonstrating
its extensive linguistic diversity. Built upon 96 snapshots of V. CHALLENGESANDOPENPROBLEMS
CommonCrawl data spanning 2013 to 2024 and processed As the capabilities of AI agents and large language models
usingthe”datatrove”alongsidesophisticatedfilteringcodeand continue to grow, new challenges and open problems emerge

<!-- Page 38 -->

38
that limit their effectiveness, reliability, and security [220]. In questions, background surveys, inspirations, and hypotheses,
this section, we highlight several critical research directions, across 12 disciplines. Expert validation ensures the reliability
including advancing the reasoning abilities of AI agents, of this framework. By exclusively using papers published in
understanding the failure modes of multi-agent systems, sup- 2024, the study minimizes data contamination from large lanporting automated scientific discovery, enabling dynamic tool guagemodel(LLM)pretrainingdatasets,revealingthatLLMs
integration, reinforcing autonomous search capabilities, and perform notably well in retrieving novel inspirations. This
addressing the vulnerabilities of emerging communication positions LLMs as promising “research hypothesis mines”
protocols. that can facilitate the automation of scientific discovery by
generating innovative hypotheses at scale.
A. AI Agents Reasoning Despitetheseadvances,significantchallengesremainforAI
agents employing LLMs toautomate scientific discovery. One

### The primary challenge addressed in [221] is the inherent

key obstacle is ensuring that these agents generate novel and
limitation of traditional Chain-of-Thought (CoT) methods,
scientifically valid hypotheses, as they must navigate the risk
which only reveal the final reasoning steps without explicitly
ofproducingbiasedorspuriousassociationswithoutsufficient
modeling the underlying cognitive process that leads to those
human oversight. Furthermore, the complexity and diversity
steps. Meta Chain-of-Thought (Meta-CoT) aims to fill this
of scientific literature across various disciplines demand that
gap by capturing and formalizing the latent reasoning that
these agents not only understand domain-specific nuances but
underlies a Chain-of-Thought (CoT). This involves not only
alsoadaptdynamicallytoevolvingresearchcontexts.Therisk
generating the visible chain of thought but also understanding
of data contamination, particularly when recent publications
the in-context search behavior and iterative reasoning steps
might overlap with pretraining data, further complicates the
thatcontributetoit.Toovercomethesechallenges,theauthors
extraction of truly innovative insights. In addition, scaling
explore innovative approaches, including process supervision,
these systems while preserving transparency, interpretability,
synthetic data generation, and search algorithms, to produce
andethicalstandardsposesamultifacetedchallengethatmust
robust Meta-CoTs. Moreover, they propose a concrete trainbe addressed to harness the potential of AI-driven scientific
ing pipeline that integrates instruction tuning with linearized
discovery fully.
search traces and reinforcement learning post-training. Open
research questions remain regarding scaling laws, the role of
verifiers, and the discovery of novel reasoning algorithms,
underscoring the complexity and potential of advancing more
human-like reasoning in large language models. D. Dynamic Tool Integration for Autonomous AI Agents
B. Why Do Multi-Agent LLM Systems Fail? Wu et al. [224] introduce Chain-of-Tools, a novel tool
learningapproachthatleveragestherobustsemanticrepresen-

### Pan et al. [222] present a critical examination of why

tation capabilities of frozen large language models (LLMs) to
multi-agent LLM systems, despite the theoretical benefits of
perform tool calling as part of a chain-of-thought reasoning
collaboration, continue to underperform compared to their
process. By utilizing a vast and flexible tool pool that can
single-agent counterparts. Through a rigorous study of five
include previously unseen tools, this method addresses the
open-source frameworks across 150 tasks, the authors enlist
inefficiencies and highlights key challenges, including manexpert human annotators to identify fourteen distinct failure
aging vast prompt-based demonstrations. The authors validate
modes ranging from ignoring task or role specifications and
their approach on a range of datasets, including a newly
unnecessaryrepetition,tolapsesinmemoryandflawedverificonstructeddataset,SimpleToolQuestions,aswellasGSM8K-
cation processes. These issues are systematically grouped into
XL, FuncQA, and KAMEL, demonstrating that Chain-ofthree categories: design and specification shortcomings, inter-
Tools outperforms conventional baselines. Additionally, the
agent misalignment, and challenges in task verification and
methodholdspromiseforenhancingautonomousAIagentsby
termination. Moreover, the study explores interventions such
enabling them to select and utilize external tools dynamically,
as refining agent role definitions and orchestration strategies,
thereby broadening their capability to solve complex, multibut finds that these measures alone are insufficient; thereby,
steptasksindependently.Thisworkpromptsseveralquestions:
it outlines a clear roadmap for future research to address the

### HowcantheintegrationofunseentoolsfurtherenhanceLLM

intricate challenges inherent in multi-agent coordination.
adaptability in diverse scenarios? What critical dimensions
of the model output influence effective tool selection, and

### C. AI Agents in Automated Scientific Discovery

how can they be optimized for greater interpretability? More-
Liu et al. [223] introduce a large-scale benchmark for over, how might this methodology be extended to enable
evaluating the capability of large language models (LLMs) in more robust autonomous decision-making in AI agents facing
generating high-quality scientific research hypotheses. It tack- increasingly complex reasoning challenges? Notably, these
les this gap by focusing on three pivotal sub-tasks: inspiration questions also underscore key challenges such as managing
retrieval,hypothesiscomposition,andhypothesisranking.The a huge tool pool, ensuring efficient tool selection, enhancing
authors have developed an automated framework that extracts model interpretability, and integrating autonomous AI agents
key components from scientific papers, including research capable of dynamic, independent operation.

<!-- Page 39 -->

39
E. Empowering LLM Agents with Integrated Search via Rein- Researchers have developed various training and inferforcement Learning ence strategies to cultivate these reasoning abilities, including
inference-time scaling, pure reinforcement learning (for ex-
ReSearch [225] represents a significant step toward endowample, DeepSeek-R1-Zero), supervised fine-tuning combined
ingLLM-basedagentswiththeabilitytodecideautonomously
withreinforcementlearning,anddistillation-basedfine-tuning.
when and how to consult external knowledge sources, seam-

### Adaptations of Qwen-32B and Llama-based architectures

lessly weaving search operations into their reasoning chains
show that a balanced combination of these methods yields
via reinforcement learning. By framing search as an actionemergentreasoningbehaviorswhilereducingoverthinkingand
able tokenized operation rather than a separate retrieval step
verbosity.
ReSearch trains models like Qwen2.5 through a reward signal
We also provided a unified comparison of state-of-the-art
that emphasizes final-answer accuracy and adherence to a
benchmarks from 2019 to 2025, together with a taxonomy of
structuredthink/search/resultformat.Thisparadigmeliminates
approximately60evaluationsuites.Ouranalysisencompasses
the need for painstakingly annotated reasoning traces and
training frameworks, including mixture-of-experts, retrievalyields strong multi-hop question–answering performance and
augmented generation, and reinforcement learning, as well as
cross-domain generalization. Yet, several challenges remain
architectural enhancements that drive performance improvefor deploying such agents in the wild: how to scale the apments. In addition, we reviewed AI agent frameworks develproachtoricher,real-timetoolsets(e.g.,calculators,databases,
opedbetween2023and2025andillustratedtheirapplications
code execution environments) without blowing up action
in domains including materials science, biomedical research,
spaces; how to design more nuanced reward functions that
synthetic data generation, and financial forecasting.
capture partial credit for intermediate reasoning or mitigate
reward hacking; how to ensure robustness and interpretability Despite these successes, several challenges remain. Key
when agents autonomously interleave reasoning and tool use; open problems include automating multi-step reasoning withandhowtobalanceexplorationofnoveltoolsequencesagainst out human oversight, balancing structured guidance with
exploitation of known effective patterns. Addressing these model flexibility, and integrating long-context retrieval at
questions will be crucial for realizing truly versatile, trust- scale.Futureresearchmustaddressthesechallengestounlock
worthy LLM agents capable of complex, multi-step problem- the full potential of autonomous AI agents.
solving. Looking ahead, we anticipate an increasing focus on
domain- and application-specific optimization. Early examples, such as DeepSeek-R1-Distill, Sky-T1, and TinyZero,

### F. Vulnerabilities of AI Agents Protocols

demonstrate how specialized reasoning systems can achieve
MCP protocol standardizes how AI applications provide a favorable trade-off between performance and computational
context to LLMs. The MCP protocol faces critical vulnera- cost. Continued innovation in training methodologies, model
bilities in Agent AI communications due to its fundamentally architectures,andbenchmarkingwilldrivethenextgeneration
decentralized design [216]. Without a central authority over- of high-efficiency, high-accuracy AI reasoning systems.
seeingsecurity,disparateimplementationpracticescanleadto
unevendefenses,makingiteasierforattackerstoexploitweak
links. In particular, the absence of a standardized authentica- REFERENCES
tionmechanismacrossdifferentnodeshindersreliableidentity
verification,therebyincreasingtheriskofunauthorizedaccess [1] A. Jaech, A. Kalai, A. Lerer, A. Richardson, A. El-Kishky, A. Low,
and potential data breaches. Moreover, deficiencies in robust
A.Helyar,A.Madry,A.Beutel,A.Carneyetal.,“Openaio1system
card,”arXivpreprintarXiv:2412.16720,2024.
logging and debugging tools further complicate the timely
[2] J. Xu, Z. Guo, J. He, H. Hu, T. He, S. Bai, K. Chen,
detectionofanomaliesanderrors,whichisvitalforpreventing J. Wang, Y. Fan, K. Dang, B. Zhang, X. Wang, Y. Chu, and
andmitigatingattacks.Additionally,thecomplexityinherentin J. Lin, “Qwen2.5-omni technical report,” 2025. [Online]. Available:
https://arxiv.org/abs/2503.20215
managing multi-step, distributed workflows can lead to state
[3] D.Guo,D.Yang,H.Zhang,J.Song,R.Zhang,R.Xu,Q.Zhu,S.Ma,
inconsistencies and operational glitches, amplifying the po- P.Wang,X.Bietal.,“Deepseek-r1:Incentivizingreasoningcapability
tential impact of a security compromise across interconnected inllmsviareinforcementlearning,”arXivpreprintarXiv:2501.12948,
2025.
systems.
[4] A.Grattafiori,A.Dubey,A.Jauhri,A.Pandey,A.Kadian,A.Al-Dahle,
A.Letman,A.Mathur,A.Schelten,A.Vaughanetal.,“Thellama3
herdofmodels,”arXivpreprintarXiv:2407.21783,2024.

## Vi. Conclusion

[5] X. Huang, W. Liu, X. Chen, X. Wang, H. Wang, D. Lian, Y. Wang,
R.Tang,andE.Chen,“Understandingtheplanningofllmagents:A
In this paper, we have surveyed recent advances in the
survey,”arXivpreprintarXiv:2402.02716,2024.
reasoning capabilities of large language models (LLMs) and
[6] J. Gu, X. Jiang, Z. Shi, H. Tan, X. Zhai, C. Xu, W. Li, Y. Shen,
autonomous AI agents and highlighted the benefits of multi- S. Ma, H. Liu et al., “A survey on llm-as-a-judge,” arXiv preprint
step, intermediate processing for solving complex tasks in arXiv:2411.15594,2024.
[7] Q. Wang, R. Ding, Z. Chen, W. Wu, S. Wang, P. Xie, and F. Zhao,
advancedmathematics,codegeneration,andlogicalreasoning.
“Vidorag:Visualdocumentretrieval-augmentedgenerationviadynamic
By exposing their internal reasoning through intermediate iterativereasoningagents,”arXivpreprintarXiv:2502.18017,2025.
steps, models such as DeepSeek-R1, OpenAI o1 and o3, and [8] Y.Li,Y.Li,X.Wang,Y.Jiang,Z.Zhang,X.Zheng,H.Wang,H.-T.
Zheng, P. Xie, P. S. Yu et al., “Benchmarking multimodal retrieval

### GPT-4o achieve greater accuracy and reliability compared to

augmented generation with dynamic vqa dataset and self-adaptive
direct-response approaches. planningagent,”arXivpreprintarXiv:2411.02937,2024.

<!-- Page 40 -->

40
[9] H.Q.YuandF.McQuade,“Rag-kg-il:Amulti-agenthybridframework [32] A.Zhou,K.Yan,M.Shlapentokh-Rothman,H.Wang,andY.-X.Wang,
for reducing hallucinations and enhancing llm reasoning through rag “Languageagenttreesearchunifiesreasoningactingandplanningin
andincrementalknowledgegraphlearningintegration,”arXivpreprint languagemodels,”arXivpreprintarXiv:2310.04406,2023.
arXiv:2503.13514,2025. [33] H. Su and Others, “Learn-by-interact: A data-centric framework
[10] S.AteiaandU.Kruschwitz,“Bioragent:Aretrieval-augmentedgener- for self-adaptive agents in realistic environments,” arXiv preprint
ationsystemforshowcasinggenerativequeryexpansionanddomain- arXiv:2501.10893,2025.
specific search for scientific q&a,” arXiv preprint arXiv:2412.12358, [34] M. Hu, P. Zhao, C. Xu, Q. Sun, J. Lou, Q. Lin, P. Luo, and S. Ra-
2024. jmohan, “Agentgen: Enhancing planning abilities for large language
[11] H. Shimadzu, T. Utsuro, and D. Kitayama, “Retrieval-augmented modelbasedagentviaenvironmentandtaskgeneration,”arXivpreprint
simulacra: Generative agents for up-to-date and knowledge-adaptive arXiv:2408.00764,2024.
simulations,”arXivpreprintarXiv:2503.14620,2025. [35] A. Zeng, M. Liu, R. Lu, B. Wang, X. Liu, Y. Dong, and J. Tang,
[12] G.Xiong,Q.Jin,X.Wang,Y.Fang,H.Liu,Y.Yang,F.Chen,Z.Song, “Agenttuning: Enabling generalized agent abilities for llms,” arXiv
D.Wang,M.Zhangetal.,“Rag-gym:Optimizingreasoningandsearch preprintarXiv:2310.12823,2023.
agents with process supervision,” arXiv preprint arXiv:2502.13957,
[36] C. Gulcehre, T. L. Paine, S. Srinivasan, K. Konyushkova, L. Weerts,
2025.
A. Sharma, A. Siddhant, A. Ahern, M. Wang, C. Gu et al., “Re-
[13] M.A.Ferrag,N.Tihanyi,andM.Debbah,“Reasoningbeyondlimits:
inforced self-training (rest) for language modeling,” arXiv preprint
Advances and open problems for llms,” 2025. [Online]. Available:
arXiv:2308.08998,2023.
https://arxiv.org/abs/2503.22732
[37] R. Aksitov, S. Miryoosefi, Z. Li, D. Li, S. Babayan, K. Kopparapu,
[14] J.Achiam,S.Adler,S.Agarwal,L.Ahmad,I.Akkaya,F.L.Aleman,

### Z.Fisher,R.Guo,S.Prakash,P.Srinivasanetal.,“Restmeetsreact:

D. Almeida, J. Altenschmidt, S. Altman, S. Anadkat et al., “Gpt-4
Self-improvement for multi-step reasoning llm agent,” arXiv preprint
technicalreport,”arXivpreprintarXiv:2303.08774,2023.
arXiv:2312.10003,2023.
[15] G. Team, R. Anil, S. Borgeaud, J.-B. Alayrac, J. Yu, R. Soricut,
[38] T.Guo,X.Chen,Y.Wang,R.Chang,S.Pei,N.V.Chawla,O.Wiest,
J. Schalkwyk, A. M. Dai, A. Hauth, K. Millican et al., “Gemand X. Zhang, “Large language model based multi-agents: A survey
ini: a family of highly capable multimodal models,” arXiv preprint
ofprogressandchallenges,”arXivpreprintarXiv:2402.01680,2024.
arXiv:2312.11805,2023.
[16] H. Touvron,L. Martin, K.Stone, P. Albert, A. Almahairi,Y. Babaei, [39] A. Goldie, A. Mirhoseini, H. Zhou, I. Cai, and C. D. Manning,
N. Bashlykov, S. Batra, P. Bhargava, S. Bhosale et al., “Llama “Synthetic data generation & multi-step rl for reasoning & tool use,”
2: Open foundation and fine-tuned chat models,” arXiv preprint arXivpreprintarXiv:2504.04736,2025.
arXiv:2307.09288,2023. [40] S. Hong, X. Zheng, J. Chen, Y. Cheng, J. Wang, C. Zhang,
[17] S.Schmidgall,Y.Su,Z.Wang,X.Sun,J.Wu,X.Yu,J.Liu,Z.Liu, Z. Wang, S. K. S. Yau, Z. Lin, L. Zhou et al., “Metagpt: Meta
and E. Barsoum, “Agent laboratory: Using llm agents as research programmingformulti-agentcollaborativeframework,”arXivpreprint
assistants,”arXivpreprintarXiv:2501.04227,2025. arXiv:2308.00352,vol.3,no.4,p.6,2023.
[18] A. Ajith, M. Xia, A. Chevalier, T. Goyal, D. Chen, and T. Gao, [41] C. Qian, X. Cong, C. Yang, W. Chen, Y. Su, J. Xu, Z. Liu, and
“Litsearch:Aretrievalbenchmarkforscientificliteraturesearch,”arXiv M. Sun, “Communicative agents for software development,” arXiv
preprintarXiv:2407.18940,2024. preprintarXiv:2307.07924,vol.6,no.3,2023.
[19] H. Kang and C. Xiong, “Researcharena: Benchmarking llms’ ability [42] Z. Mandi, S. Jain, and S. Song, “Roco: Dialectic multi-robot coltocollectandorganizeinformationasresearchagents,”arXivpreprint laboration with large language models,” in 2024 IEEE International
arXiv:2406.10291,2024. Conference on Robotics and Automation (ICRA). IEEE, 2024, pp.
[20] J.Baek,S.K.Jauhar,S.Cucerzan,andS.J.Hwang,“Researchagent: 286–299.
Iterative research idea generation over scientific literature with large [43] H.Zhang,W.Du,J.Shan,Q.Zhou,Y.Du,J.B.Tenenbaum,T.Shu,
languagemodels,”arXivpreprintarXiv:2404.07738,2024. and C. Gan, “Building cooperative embodied agents modularly with
[21] M.Gridach,J.Nanavati,K.Z.E.Abidine,L.Mendes,andC.Mack, largelanguagemodels,”arXivpreprintarXiv:2307.02485,2023.
“Agenticaiforscientificdiscovery:Asurveyofprogress,challenges, [44] J. S. Park, J. O’Brien, C. J. Cai, M. R. Morris, P. Liang, and
andfuturedirections,”arXivpreprintarXiv:2503.08979,2025. M. S. Bernstein, “Generative agents: Interactive simulacra of human
[22] Y. Kim, C. Park, H. Jeong, Y. S. Chan, X. Xu, D. McDuff, H. Lee, behavior,”inProceedingsofthe36thannualacmsymposiumonuser
M. Ghassemi, C. Breazeal, H. Park et al., “Mdagents: An adaptive interfacesoftwareandtechnology,2023,pp.1–22.
collaborationofllmsformedicaldecision-making,”AdvancesinNeural [45] B.Xiao,Z.Yin,andZ.Shan,“Simulatingpublicadministrationcrisis:
InformationProcessingSystems,vol.37,pp.79410–79452,2024. Anovelgenerativeagent-basedsimulationsystemtolowertechnology
[23] S. Mukherjee, P. Gamble, M. S. Ausin, N. Kant, K. Aggarwal, barriersinsocialscienceresearch,”arXivpreprintarXiv:2311.06957,
N. Manjunath, D. Datta, Z. Liu, J. Ding, S. Busacca et al., “Polaris: 2023.
A safety-focused llm constellation architecture for healthcare,” arXiv [46] S. Wang, C. Liu, Z. Zheng, S. Qi, S. Chen, Q. Yang, A. Zhao,
preprintarXiv:2403.13313,2024.

### C.Wang,S.Song,andG.Huang,“Avalon’sgameofthoughts:Battle

[24] T.Yuan,Z.He,L.Dong,Y.Wang,R.Zhao,T.Xia,L.Xu,B.Zhou, against deception through recursive contemplation,” arXiv preprint
F.Li,Z.Zhangetal.,“R-judge:Benchmarkingsafetyriskawareness arXiv:2310.01320,2023.
forllmagents,”arXivpreprintarXiv:2401.10019,2024.
[47] Y.Wang,W.Zhong,Y.Huang,E.Shi,M.Yang,J.Chen,H.Li,Y.Ma,
[25] W.YAN,J.HU,H.ZENG,M.LIU,andW.LIANG,“Theapplication
Q. Wang, and Z. Zheng, “Agents in software engineering: Survey,
of large language models in primary healthcare services and the
landscape,andvision,”arXivpreprintarXiv:2409.09030,2024.
challenges,”ChineseGeneralPractice,vol.28,no.01,p.1,2025.
[48] H.Jin,L.Huang,H.Cai,J.Yan,B.Li,andH.Chen,“Fromllmstollm-
[26] H. Yu, J. Zhou, L. Li, S. Chen, J. Gallifant, A. Shi, X. Li, W. Hua,
basedagentsforsoftwareengineering:Asurveyofcurrent,challenges
M.Jin,G.Chenetal.,“Aipatient:Simulatingpatientswithehrsandllm
andfuture,”arXivpreprintarXiv:2408.02479,2024.
poweredagenticworkflow,”arXivpreprintarXiv:2409.18924,2024.
[49] A.Singh,A.Ehtesham,S.Kumar,andT.T.Khoei,“Agenticretrieval-
[27] S.Schmidgall,R.Ziaei,C.Harris,E.Reis,J.Jopling,andM.Moor,
augmented generation: A survey on agentic rag,” arXiv preprint
“Agentclinic:amultimodalagentbenchmarktoevaluateaiinsimulated
arXiv:2501.09136,2025.
clinicalenvironments,”arXivpreprintarXiv:2405.07960,2024.
[28] W.Wang,Z.Ma,Z.Wang,C.Wu,W.Chen,X.Li,andY.Yuan,“A [50] A.Yehudai,L.Eden,A.Li,G.Uziel,Y.Zhao,R.Bar-Haim,A.Cohan,
surveyofllm-basedagentsinmedicine:Howfararewefrombaymax?” andM.Shmueli-Scheuer,“Surveyonevaluationofllm-basedagents,”
arXivpreprintarXiv:2502.11211,2025. 2025.[Online].Available:https://arxiv.org/abs/2503.16416
[29] X.Wang,Y.Chen,L.Yuan,Y.Zhang,Y.Li,H.Peng,andH.Ji,“Exe- [51] Q.Chen,L.Qin,J.Liu,D.Peng,J.Guan,P.Wang,M.Hu,Y.Zhou,
cutablecodeactionselicitbetterllmagents,”inForty-firstInternational T. Gao, and W. Che, “Towards reasoning era: A survey of long
ConferenceonMachineLearning,2024. chain-of-thoughtforreasoninglargelanguagemodels,”arXivpreprint
[30] N. Shinn, F. Cassano, A. Gopinath, K. Narasimhan, and S. Yao, arXiv:2503.09567,2025.
“Reflexion: Language agents with verbal reinforcement learning,” [52] B.Yan,X.Zhang,L.Zhang,L.Zhang,Z.Zhou,D.Miao,andC.Li,
AdvancesinNeuralInformationProcessingSystems,vol.36,pp.8634– “Beyondself-talk:Acommunication-centricsurveyofllm-basedmulti-
8652,2023. agentsystems,”arXivpreprintarXiv:2502.14321,2025.
[31] S.Yao,J.Zhao,D.Yu,N.Du,I.Shafran,K.Narasimhan,andY.Cao, [53] X. Feng, L. Dou, E. Li, Q. Wang, H. Wang, Y. Guo, C. Ma, and
“React: Synergizing reasoning and acting in language models,” in L. Kong, “A survey on large language model-based social agents in
InternationalConferenceonLearningRepresentations(ICLR),2023. game-theoreticscenarios,”arXivpreprintarXiv:2412.03920,2024.

<!-- Page 41 -->

41
[54] C.Zhang,S.He,J.Qian,B.Li,L.Li,S.Qin,Y.Kang,M.Ma,G.Liu, [76] M. Kazemi, B. Fatemi, H. Bansal, J. Palowitch, C. Anastasiou, S. V.
Q. Lin et al., “Large language model-brained gui agents: A survey,” Mehta, L. K. Jain, V. Aglietti, D. Jindal, P. Chen et al., “Big-bench
arXivpreprintarXiv:2411.18279,2024. extrahard,”arXivpreprintarXiv:2502.19187,2025.
[55] Y. Li, H. Wen, W. Wang, X. Li, Y. Yuan, G. Liu, J. Liu, W. Xu, [77] K.Zhu,H.Du,Z.Hong,X.Yang,S.Guo,Z.Wang,Z.Wang,C.Qian,
X. Wang, Y. Sun et al., “Personal llm agents: Insights and sur- X. Tang, H. Ji et al., “Multiagentbench: Evaluating the collaboration
vey about the capability, efficiency and security,” arXiv preprint andcompetitionofllmagents,”arXivpreprintarXiv:2503.01935,2025.
arXiv:2401.05459,2024. [78] G. Mialon, C. Fourrier, T. Wolf, Y. LeCun, and T. Scialom, “Gaia:
[56] M. C. Ramos, C. J. Collison, and A. D. White, “A review of large a benchmark for general ai assistants,” in The Twelfth International
language models and autonomous agents in chemistry,” Chemical ConferenceonLearningRepresentations,2023.
Science,2025. [79] R. A. Dubniczky, K. Z. Horva´t, T. Bisztray, M. A. Ferrag, L. C.
[57] C. J. Wang, D. Lee, C. Menghini, J. Mols, J. Doughty, A. Khoja, Cordeiro, and N. Tihanyi, “Castle: Benchmarking dataset for static
J. Lynch, S. Hendryx, S. Yue, and D. Hendrycks, “Enigmaeval: A code analyzers and llms towards cwe detection,” arXiv preprint
benchmark of long multimodal reasoning challenges,” arXiv preprint arXiv:2503.09433,2025.
arXiv:2502.08859,2025. [80] J.Yao,K.Wang,R.Hsieh,H.Zhou,T.Zou,Z.Cheng,Z.Wang,and
[58] D.Hendrycks,C.Burns,S.Basart,A.Zou,M.Mazeika,D.Song,and P. Viswanath, “Spin-bench: How well do llms plan strategically and
J.Steinhardt,“Measuringmassivemultitasklanguageunderstanding,” reasonsocially?”arXivpreprintarXiv:2503.12349,2025.
arXivpreprintarXiv:2009.03300,2020. [81] S. Yao, N. Shinn, P. Razavi, and K. Narasimhan, “A benchmark
[59] L.Zhong,Z.Du,X.Zhang,H.Hu,andJ.Tang,“Complexfuncbench: for tool-agent-user interaction in real-world domains,” arXiv preprint
Exploring multi-step and constrained function calling under long- arXiv:2406.12045,2024.
contextscenario,”arXivpreprintarXiv:2501.10132,2025.
[82] D.Dua,Y.Wang,P.Dasigi,G.Stanovsky,S.Singh,andM.Gardner,
[60] L. Phan, A. Gatti, Z. Han, N. Li, J. Hu, H. Zhang, S. Shi, M. Choi, “Drop:Areadingcomprehensionbenchmarkrequiringdiscretereason-
A.Agrawal,A.Chopraetal.,“Humanity’slastexam,”arXivpreprint ingoverparagraphs,”arXivpreprintarXiv:1903.00161,2019.
arXiv:2501.14249,2025.
[83] D. Hendrycks, C. Burns, S. Kadavath, A. Arora, S. Basart, E. Tang,
[61] DeepMind, “Facts & grounding: A new benchmark for evaluating D.Song,andJ.Steinhardt,“Measuringmathematicalproblemsolving
the factuality of large language models,” 2023, accessed: 2025- withthemathdataset,”arXivpreprintarXiv:2103.03874,2021.
02-03. [Online]. Available: https://deepmind.google/discover/blog/
[84] M. Chen, J. Tworek, H. Jun, Q. Yuan, H. P. D. O. Pinto, J. Kaplan,
facts-grounding-a-new-benchmark-for-evaluating-the-factuality-of-\
H.Edwards,Y.Burda,N.Joseph,G.Brockmanetal.,“Evaluatinglarge
large-language-models/
language models trained on code,” arXiv preprint arXiv:2107.03374,
[62] C.Zheng,Z.Zhang,B.Zhang,R.Lin,K.Lu,B.Yu,D.Liu,J.Zhou,
2021.
andJ.Lin,“Processbench:Identifyingprocesserrorsinmathematical
[85] F.Shi,M.Suzgun,M.Freitag,X.Wang,S.Srivats,S.Vosoughi,H.W.
reasoning,”arXivpreprintarXiv:2412.06559,2024.

### Chung,Y.Tay,S.Ruder,D.Zhouetal.,“Languagemodelsaremulti-

[63] L. Ouyang, Y. Qu, H. Zhou, J. Zhu, R. Zhang, Q. Lin, B. Wang,
lingualchain-of-thoughtreasoners,”arXivpreprintarXiv:2210.03057,
Z. Zhao, M. Jiang, X. Zhao et al., “Omnidocbench: Benchmarking
2022.
diversepdfdocumentparsingwithcomprehensiveannotations,”arXiv
[86] V.Samuel,H.P.Zou,Y.Zhou,S.Chaudhari,A.Kalyan,T.Rajpurohit,
preprintarXiv:2412.07626,2024.

### A.Deshpande,K.Narasimhan,andV.Murahari,“Personagym:Evalu-

[64] M. Zhuge, C. Zhao, D. Ashley, W. Wang, D. Khizbullin, Y. Xiong,
atingpersonaagentsandllms,”arXivpreprintarXiv:2407.18416,2024.
Z.Liu,E.Chang,R.Krishnamoorthi,Y.Tianetal.,“Agent-as-a-judge:
[87] C.Ye,Z.Hu,Y.Deng,Z.Huang,M.D.Ma,Y.Zhu,andW.Wang,
Evaluateagentswithagents,”arXivpreprintarXiv:2410.10934,2024.
“Mirai: Evaluating llm agents for event forecasting,” arXiv preprint
[65] S.Tan,S.Zhuang,K.Montgomery,W.Y.Tang,A.Cuadron,C.Wang,
arXiv:2407.01231,2024.
R. A. Popa, and I. Stoica, “Judgebench: A benchmark for evaluating
[88] H.Trivedi,T.Khot,M.Hartmann,R.Manku,V.Dong,E.Li,S.Gupta,
llm-basedjudges,”arXivpreprintarXiv:2410.12784,2024.
A. Sabharwal, and N. Balasubramanian, “Appworld: A controllable
[66] OpenAI, “Introducing simpleqa,” 2024, accessed: 2025-02-03.
worldofappsandpeopleforbenchmarkinginteractivecodingagents,”
[Online].Available:https://openai.com/index/introducing-simpleqa/
arXivpreprintarXiv:2407.18901,2024.
[67] HuggingFaceFW, “Fine tasks,” 2024, accessed: 2025-02-03.
[89] X.Liu,T.Zhang,Y.Gu,I.L.Iong,Y.Xu,X.Song,S.Zhang,H.Lai,
[Online]. Available: https://huggingface.co/spaces/HuggingFaceFW/
X.Liu,H.Zhaoetal.,“Visualagentbench:Towardslargemultimodal
blogpost-fine-tasks
modelsasvisualfoundationagents,”arXivpreprintarXiv:2408.06327,
[68] S. Krishna, K. Krishna, A. Mohananey, S. Schwarcz, A. Stam-
2024.
bler, S. Upadhyay, and M. Faruqui, “Fact, fetch, and reason: A
unified evaluation of retrieval-augmented generation,” arXiv preprint [90] Z.Chen,S.Chen,Y.Ning,Q.Zhang,B.Wang,B.Yu,Y.Li,Z.Liao,
arXiv:2409.12941,2024. C.Wei,Z.Luetal.,“Scienceagentbench:Towardrigorousassessment
oflanguageagentsfordata-drivenscientificdiscovery,”arXivpreprint
[69] Hugging Face, “Dabstep,” 2025, accessed: 2025-02-03. [Online].
arXiv:2410.05080,2024.

### Available:https://huggingface.co/blog/dabstep

[70] H. Mao, C. C.-J. Ji, F. Yan, T. Zhang, and S. G. Patil, “Bfcl v2 [91] Z. Zhang, S. Cui, Y. Lu, J. Zhou, J. Yang, H. Wang, and M. Huang,
live,” https://gorilla.cs.berkeley.edu/blogs/12 bfcl v2 live.html, 2024, “Agent-safetybench: Evaluating the safety of llm agents,” arXiv
accessed:February16,2025.
preprintarXiv:2412.14470,2024.
[71] S. Miserendino, M. Wang, T. Patwardhan, and J. Heidecke, [92] B. P. Majumder, H. Surana, D. Agarwal, B. D. Mishra, A. Meena,
“Swe-lancer: Can frontier llms earn $1 million from real world A. Prakhar, T. Vora, T. Khot, A. Sabharwal, and P. Clark, “Discovfreelance software engineering?” 2025. [Online]. Available: https: erybench:Towardsdata-drivendiscoverywithlargelanguagemodels,”
//arxiv.org/abs/2502.12115 arXivpreprintarXiv:2407.01725,2024.
[72] X.Yang,K.Sun,H.Xin,Y.Sun,N.Bhalla,X.Chen,S.Choudhary, [93] K.Gu,R.Shang,R.Jiang,K.Kuang,R.-J.Lin,D.Lyu,Y.Mao,Y.Pan,
R. D. Gui, Z. W. Jiang, Z. Jiang et al., “Crag–comprehensive rag T.Wu,J.Yuetal.,“Blade:Benchmarkinglanguagemodelagentsfor
benchmark,”arXivpreprintarXiv:2406.04744,2024. data-drivenscience,”arXivpreprintarXiv:2408.09667,2024.
[73] M. Kouremetis, M. Dotter, A. Byrne, D. Martin, E. Michalak, [94] J.Liu,W.Wang,Z.Ma,G.Huang,Y.SU,K.-J.Chang,W.Chen,H.Li,
G. Russo, M. Threet, and G. Zarrella, “Occult: Evaluating large L.Shen,andM.Lyu,“Medchain:Bridgingthegapbetweenllmagents
language models for offensive cyber operation capabilities,” 2025. and clinical practice through interactive sequential benchmarking,”
[Online].Available:https://arxiv.org/abs/2502.15797 arXivpreprintarXiv:2412.01605,2024.
[74] N.Tihanyi,T.Bisztray,R.A.Dubniczky,R.Toth,B.Borsos,B.Cherif, [95] Q. Long, Z. Li, R. Gong, Y. N. Wu, D. Terzopoulos, and X. Gao,
R. Jain, L. Muzsai, M. A. Ferrag, R. Marinelli et al., “Dynamic “Teamcraft: A benchmark for multi-modal multi-agent systems in
intelligence assessment: Benchmarking llms on the road to agi with minecraft,”arXivpreprintarXiv:2412.05255,2024.
afocusonmodelconfidence,”in2024IEEEInternationalConference [96] M. Andriushchenko, A. Souly, M. Dziemian, D. Duenas, M. Lin,
onBigData(BigData). IEEE,2024,pp.3313–3321. J. Wang, D. Hendrycks, A. Zou, Z. Kolter, M. Fredrikson et al.,
[75] N. Tihanyi, M. A. Ferrag, R. Jain, T. Bisztray, and M. Debbah, “Agentharm:Abenchmarkformeasuringharmfulnessofllmagents,”
“Cybermetric:abenchmarkdatasetbasedonretrieval-augmentedgen- arXivpreprintarXiv:2410.09024,2024.
erationforevaluatingllmsincybersecurityknowledge,”in2024IEEE [97] H.Li,J.Chen,J.Yang,Q.Ai,W.Jia,Y.Liu,K.Lin,Y.Wu,G.Yuan,
International Conference on Cyber Security and Resilience (CSR). Y.Huetal.,“Legalagentbench:Evaluatingllmagentsinlegaldomain,”
IEEE,2024,pp.296–302. arXivpreprintarXiv:2412.17259,2024.

<!-- Page 42 -->

42
[98] D. Rein, B. L. Hou, A. C. Stickland, J. Petty, R. Y. Pang, J. Dirani, [120] M.S.Rashid,C.Bock,Y.Zhuang,A.Buccholz,T.Esler,S.Valentin,
J.Michael,andS.R.Bowman,“Gpqa:Agraduate-levelgoogle-proof L. Franceschi, M. Wistuba, P. T. Sivaprasad, W. J. Kim, A. Deoras,
q&abenchmark,”inFirstConferenceonLanguageModeling,2024. G.Zappella,andL.Callot,“Swe-polybench:Amulti-languagebench-
[99] X.Tang,D.Shao,J.Sohn,J.Chen,J.Zhang,J.Xiang,F.Wu,Y.Zhao, markforrepositorylevelevaluationofcodingagents,”2025.
C.Wu,W.Shietal.,“Medagentsbench:Benchmarkingthinkingmodels [121] D.Zan,Z.Huang,W.Liu,H.Chen,L.Zhang,S.Xin,L.Chen,Q.Liu,
andagentframeworksforcomplexmedicalreasoning,”arXivpreprint X. Zhong, A. Li et al., “Multi-swe-bench: A multilingual benchmark
arXiv:2503.07459,2025. forissueresolving,”arXivpreprintarXiv:2504.02605,2025.
[100] Z. Cheng, Y. Tu, R. Li, S. Dai, J. Hu, S. Hu, J. Li, Y. Shi, T. Yu, [122] A.Srivastava,A.Rastogi,A.Rao,A.A.M.Shoeb,A.Abid,A.Fisch,
W.Chenetal.,“Embodiedeval:Evaluatemultimodalllmsasembodied A.R.Brown,A.Santoro,A.Gupta,A.Garriga-Alonsoetal.,“Beyond
agents,”arXivpreprintarXiv:2501.11858,2025. the imitation game: Quantifying and extrapolating the capabilities of
[101] Z. Huang, Z. Wang, S. Xia, X. Li, H. Zou, R. Xu, R.-Z. Fan, languagemodels,”arXivpreprintarXiv:2206.04615,2022.
L. Ye, E. Chern, Y. Ye et al., “Olympicarena: Benchmarking multi- [123] M.Suzgun,N.Scales,N.Scha¨rli,S.Gehrmann,Y.Tay,H.W.Chung,
discipline cognitive reasoning for superintelligent ai,” Advances in A. Chowdhery, Q. V. Le, E. H. Chi, D. Zhou et al., “Challenging
Neural Information Processing Systems, vol. 37, pp. 19209–19253, big-benchtasksandwhetherchain-of-thoughtcansolvethem,”arXiv
2024. preprintarXiv:2210.09261,2022.
[102] Y. Xiang, H. Yan, S. Ouyang, L. Gui, and Y. He, “Scireplicate- [124] Langchain agents tutorial. Accessed: February 23, 2025. [Online].
bench: Benchmarking llms in agent-driven algorithmic reproduction Available:https://python.langchain.com/docs/tutorials/agents/
fromresearchpapers,”arXivpreprintarXiv:2504.00255,2025. [125] Building a basic agent. Accessed: February 23, 2025. [Online].
[103] S. Fish, J. Shephard, M. Li, R. I. Shorrer, and Y. A. Gonczarowski, Available:https://docs.llamaindex.ai/en/stable/understanding/agent/
“Econevals: Benchmarks and litmus tests for llm agents in unknown [126] Crewai. Accessed: February 23, 2025. [Online]. Available: https:
environments,”arXivpreprintarXiv:2503.18825,2025. //www.crewai.com/
[104] Y. Y. Sung, H. Kim, and D. Zhang, “Verila: A human-centered eval- [127] OpenAI, “swarm,” 2024, accessed: 2025-02-03. [Online]. Available:
uation framework for interpretable verification of llm agent failures,” https://github.com/openai/swarm/tree/main
arXivpreprintarXiv:2503.12651,2025.
[128] S.Hu,M.Ouyang,D.Gao,andM.Z.Shou,“Thedawnofguiagent:
[105] Y. Yang, B. Huang, S. Qi, C. Feng, H. Hu, Y. Zhu, J. Hu, H. Zhao, Apreliminarycasestudywithclaude3.5computeruse,”arXivpreprint
Z. He, X. Liu et al., “Who’s the mvp? a game-theoretic evaluation arXiv:2411.10323,2024.
benchmark for modular attribution in llm agents,” arXiv preprint
[129] J. Wu, J. Zhu, and Y. Liu, “Agentic reasoning: Reasoning llms with
arXiv:2502.00510,2025.
toolsforthedeepresearch,”arXivpreprintarXiv:2502.04644,2025.
[106] Z.Li,S.Huang,J.Wang,N.Zhang,A.Antoniades,W.Hua,K.Zhu,
[130] P.Lu,B.Chen,S.Liu,R.Thapa,J.Boen,andJ.Zou,“Octotools:An
S.Zeng,W.Y.Wang,andX.Yan,“Agentorca:Adual-systemframeagenticframeworkwithextensibletoolsforcomplexreasoning,”arXiv
worktoevaluatelanguageagentsonoperationalroutineandconstraint
preprintarXiv:2502.11271,2025.
adherence,”arXivpreprintarXiv:2503.08669,2025.
[131] OpenAI, “Agents sdk,” https://platform.openai.com/docs/guides/
[107] K.Liu,Y.Pan,J.Li,D.He,Y.Xiang,Y.Du,andT.Gao,“Projecteval:
agents-sdk,accessed:March18,2025.

### Abenchmarkforprogrammingagentsautomatedevaluationonproject-

[132] C. Wang, X. Hu, Y. Zhang, X. Chen, P. Du, Y. Mao, R. Wang,
levelcodegeneration,”arXivpreprintarXiv:2503.07010,2025.
Y. Li, Y. Wu, H. Yang et al., “Starwhisper telescope: Agent-based
[108] D. Gautam, S. Garg, J. Jang, N. Sundaresan, and R. Z. Moghadobservation assistant system to approach ai astrophysicist,” arXiv
dam,“Refactorbench:Evaluatingstatefulreasoninginlanguageagents
preprintarXiv:2412.06412,2024.
throughcode,”arXivpreprintarXiv:2503.07832,2025.
[133] H. Zhang, Y. Song, Z. Hou, S. Miret, and B. Liu, “Honeycomb: A
[109] Y. Song, K. Thai, C. M. Pham, Y. Chang, M. Nadaf, and M. Iyyer,
flexiblellm-basedagentsystemformaterialsscience,”arXivpreprint
“Bearcubs: A benchmark for computer-using web agents,” arXiv
arXiv:2409.00135,2024.
preprintarXiv:2503.07919,2025.
[134] Z. Wang, Q. Jin, C.-H. Wei, S. Tian, P.-T. Lai, Q. Zhu, C.-P. Day,
[110] G. Gonzalez-Pumariega, L. S. Yean, N. Sunkara, and S. Choudhury,
C. Ross, and Z. Lu, “Geneagent: self-verification language agent for
“Robotouille: An asynchronous planning benchmark for llm agents,”
genesetknowledgediscoveryusingdomaindatabases,”arXivpreprint
arXivpreprintarXiv:2502.05227,2025.
arXiv:2405.16205,2024.
[111] W. Tang, Y. Zhou, E. Xu, K. Cheng, M. Li, and L. Xiao, “Dsg-
[135] M. J. Buehler, “Preflexor: Preference-based recursive language modbench: A diverse strategic game benchmark for evaluating llm-based
agents in complex decision-making environments,” arXiv preprint elingforexploratoryoptimizationofreasoningandagenticthinking,”
arXiv:2503.06047,2025.
arXivpreprintarXiv:2410.12375,2024.
[112] M. Ku, T. Chong, J. Leung, K. Shah, A. Yu, and W. Chen, “The- [136] X. Liang, J. Yang, Y. Wang, C. Tang, Z. Zheng, S. Niu, S. Song,
oremexplainagent: Towards multimodal explanations for llm theorem H. Wang, B. Tang, F. Xiong et al., “Surveyx: Academic survey auunderstanding,”arXivpreprintarXiv:2502.19400,2025. tomationvialargelanguagemodels,”arXivpreprintarXiv:2502.14776,
[113] J.Yan,Y.Luo,andY.Zhang,“Refutebench2.0–agenticbenchmarkfor 2025.
dynamic evaluation of llm responses to refutation instruction,” arXiv [137] L. Li, W. Xu, J. Guo, R. Zhao, X. Li, Y. Yuan, B. Zhang,
preprintarXiv:2502.18308,2025. Y. Jiang, Y. Xin, R. Dang et al., “Chain of ideas: Revolutionizing
[114] D. Nathani, L. Madaan, N. Roberts, N. Bashlykov, A. Menon, research via novel idea development with llm agents,” arXiv preprint
V.Moens,A.Budhiraja,D.Magka,V.Vorotilov,G.Chaurasiaetal., arXiv:2410.13185,2024.
“Mlgym:Anewframeworkandbenchmarkforadvancingairesearch [138] A. Mitra, L. Del Corro, G. Zheng, S. Mahajan, D. Rouhana, A. Coagents,”arXivpreprintarXiv:2502.14499,2025. das, Y. Lu, W.-g. Chen, O. Vrousgos, C. Rosset et al., “Agentin-
[115] D. Zhang, S. Zhoubian, M. Cai, F. Li, L. Yang, W. Wang, T. Dong, struct:Towardgenerativeteachingwithagenticflows,”arXivpreprint
Z. Hu, J. Tang, and Y. Yue, “Datascibench: An llm agent benchmark arXiv:2407.03502,2024.
fordatascience,”arXivpreprintarXiv:2502.13897,2025. [139] X. Tang, T. Hu, M. Ye, Y. Shao, X. Yin, S. Ouyang, W. Zhou,
[116] R. Yang, H. Chen, J. Zhang, M. Zhao, C. Qian, K. Wang, Q. Wang, P.Lu,Z.Zhang,Y.Zhaoetal.,“Chemagent:Self-updatinglibraryin
T.V.Koripella,M.Movahedi,M.Lietal.,“Embodiedbench:Compre- large language models improves chemical reasoning,” arXiv preprint
hensivebenchmarkingmulti-modallargelanguagemodelsforvision- arXiv:2501.06590,2025.
drivenembodiedagents,”arXivpreprintarXiv:2502.09560,2025. [140] B.Liu,J.Zhang,F.Lin,X.Jia,andM.Peng,“\textit{OneSizedoesn’t
[117] J.Wei,Z.Sun,S.Papay,S.McKinney,J.Han,I.Fulford,H.W.Chung, FitAll}:Apersonalizedconversationaltutoringagentformathematics
A.Tachard,Passos,W.Fedus,andA.Glaese,“Browsecomp:Asimple instruction,”arXivpreprintarXiv:2502.12633,2025.
yet challenging benchmark for browsing agents,” https://cdn.openai. [141] Z. Zhang, X. Bo, C. Ma, R. Li, X. Chen, Q. Dai, J. Zhu, Z. Dong,
com/pdf/5e10f4ab-d6f7-442e-9508-59515c65e35d/browsecomp.pdf, andJ.-R.Wen,“Asurveyonthememorymechanismoflargelanguage
2025,accessed:2025-04-13. modelbasedagents,”arXivpreprintarXiv:2404.13501,2024.
[118] A. Backlund and L. Petersson, “Vending-bench: A benchmark [142] P.Zhao,H.Zhang,Q.Yu,Z.Wang,Y.Geng,F.Fu,L.Yang,W.Zhang,
for long-term coherence of autonomous agents,” arXiv preprint J.Jiang,andB.Cui,“Retrieval-augmentedgenerationforai-generated
arXiv:2502.15840,2025. content:Asurvey,”arXivpreprintarXiv:2402.19473,2024.
[119] J. S. Chan, N. Chowdhury, O. Jaffe, J. Aung, D. Sherburn, E. Mays, [143] Y. Liu, S. K. Lo, Q. Lu, L. Zhu, D. Zhao, X. Xu, S. Harrer, and
G. Starace, K. Liu, L. Maksin, T. Patwardhan et al., “Mle-bench: J. Whittle, “Agent design pattern catalogue: A collection of architec-
Evaluatingmachinelearningagentsonmachinelearningengineering,” turalpatternsforfoundationmodelbasedagents,”JournalofSystems
arXivpreprintarXiv:2410.07095,2025. andSoftware,vol.220,p.112278,2025.

<!-- Page 43 -->

43
[144] “How to design an agent for production,” ac- [167] S. Hong, Y. Lin, B. Liu, B. Liu, B. Wu, C. Zhang, C. Wei, D. Li,
cessed: 2025-04-14. [Online]. Available: https://blog.langchain.dev/ J. Chen, J. Zhang et al., “Data interpreter: An llm agent for data
how-to-design-an-agent-for-production/ science,”arXivpreprintarXiv:2402.18679,2024.
[145] Q. Sun, K. Cheng, Z. Ding, C. Jin, Y. Wang, F. Xu, Z. Wu, [168] J. Gottweis, W.-H. Weng, A. Daryin, T. Tu, A. Palepu, P. Sirkovic,
C. Jia, L. Chen, Z. Liu et al., “Os-genesis: Automating gui agent A.Myaskovsky,F.Weissenberger,K.Rong,R.Tannoetal.,“Towards
trajectory construction via reverse task synthesis,” arXiv preprint anaico-scientist,”arXivpreprintarXiv:2502.18864,2025.
arXiv:2412.19723,2024. [169] W.Dong,“Theannarborarchitectureforagent-orientedprogramming,”
[146] J.Chen,C.Gui,A.Gao,K.Ji,X.Wang,X.Wan,andB.Wang,“Cod, arXivpreprintarXiv:2502.09903,2025.
towardsaninterpretablemedicalagentusingchainofdiagnosis,”arXiv [170] N.Jain,J.Singh,M.Shetty,L.Zheng,K.Sen,andI.Stoica,“R2e-gym:
preprintarXiv:2407.13301,2024. Proceduralenvironmentsandhybridverifiersforscalingopen-weights
[147] Y. Zhou, P. Zhang, M. Song, A. Zheng, Y. Lu, Z. Liu, Y. Chen, and sweagents,”arXivpreprintarXiv:2504.07164,2025.
Z. Xi, “Zodiac: A cardiologist-level llm framework for multi-agent [171] J.Wang,Y.Dai,Y.Zhang,Z.Ma,W.Li,andJ.Chai,“Trainingturndiagnostics,”arXivpreprintarXiv:2410.02026,2024. by-turnverifiersfordialoguetutoringagents:Thecuriouscaseofllms
[148] Z. Wang, J. Wu, C. H. Low, and Y. Jin, “Medagent-pro: Towards asyourcodingtutors,”arXivpreprintarXiv:2502.13311,2025.
multi-modal evidence-based medical diagnosis via reasoning agentic [172] H.-Y.Chen,C.-P.Huang,andJ.-M.Yao,“Verbalprocesssupervision
workflow,”arXivpreprintarXiv:2503.18968,2025. elicitsbettercodingagents,”arXivpreprintarXiv:2503.18494,2025.
[149] I. Steenstra, F. Nouraei, and T. W. Bickmore, “Scaffolding empathy: [173] V. Aggarwal, O. Kamal, A. Japesh, Z. Jin, and B. Scho¨lkopf, “Dars:
Trainingcounselorswithsimulatedpatientsandutterance-levelperfor- Dynamicactionre-samplingtoenhancecodingagentperformanceby
mancevisualizations,”arXivpreprintarXiv:2502.18673,2025. adaptivetreetraversal,”arXivpreprintarXiv:2503.14269,2025.
[150] J.Feng,Q.Zheng,C.Wu,Z.Zhao,Y.Zhang,Y.Wang,andW.Xie, [174] Z. Chen, X. Tang, G. Deng, F. Wu, J. Wu, Z. Jiang, V. Prasanna,
“Mˆ 3builder: A multi-agent system for automated machine learning A.Cohan,andX.Wang,“Locagent:Graph-guidedllmagentsforcode
inmedicalimaging,”arXivpreprintarXiv:2502.20301,2025. localization,”arXivpreprintarXiv:2503.09089,2025.
[151] D. Rose, C.-C. Hung, M. Lepri, I. Alqassem, K. Gashteovski,
[175] A. Gholamzadeh Khoee, S. Wang, Y. Yu, R. Feldt, and
and C. Lawrence, “Meddxagent: A unified modular agent frame-
D. Parthasarathy, “Gatelens: A reasoning-enhanced llm agent for
work for explainable automatic differential diagnosis,” arXiv preprint automotive software release analytics,” arXiv e-prints, pp. arXiv–
arXiv:2502.19175,2025.
2503,2025.
[152] F. Ghezloo, M. S. Seyfioglu, R. Soraki, W. O. Ikezogwo, B. Li,
[176] R.Hu,C.Peng,X.Wang,andC.Gao,“Anllm-basedagentforreliable
T.Vivekanandan,J.G.Elmore,R.Krishna,andL.Shapiro,“Pathfinder:
docker environment configuration,” arXiv preprint arXiv:2502.13681,
A multi-modal multi-agent system for medical diagnostic decision-
2025.
making applied to histopathology,” arXiv preprint arXiv:2502.08916,
[177] Y.Lu,B.Yao,H.Gu,J.Huang,J.Wang,L.Li,J.Gesi,Q.He,T.J.-
2025.
J. Li, and D. Wang, “Uxagent: An llm agent-based usability testing
[153] M. A. Abbasi, F. S. Mirnezami, and H. Naderi, “Hamraz: A cultureframeworkforwebdesign,”arXivpreprintarXiv:2502.12561,2025.
based persian conversation dataset for person-centered therapy using
[178] J.Pan,X.Wang,G.Neubig,N.Jaitly,H.Ji,A.Suhr,andY.Zhang,
llmagents,”arXivpreprintarXiv:2502.05982,2025.
“Training software engineering agents and verifiers with swe-gym,”
[154] Y.Yang,P.Achananuparp,H.Huang,J.Jiang,K.P.Leng,N.G.Lim,
arXivpreprintarXiv:2412.21139,2024.

### C.T.S.Ern,andE.-p.Lim,“Cami:Acounseloragentsupportingmo-

[179] J.Yang,W.Zhang,J.Yang,Y.Miao,S.Quan,Z.Wu,Q.Peng,L.Yang,
tivational interviewing through state inference and topic exploration,”
T.Liu,Z.Cuietal.,“Multi-agentcollaborationformultilingualcode
arXivpreprintarXiv:2502.02807,2025.
instructiontuning,”arXivpreprintarXiv:2502.07487,2025.
[155] A. Xu, D. Yang, R. Li, J. Zhu, M. Tan, M. Yang, W. Qiu, M. Ma,
[180] X. Guo, X. Wang, Y. Chen, S. Li, C. Han, M. Li, and H. Ji,

### H.Wu,B.Lietal.,“Autocbt:Anautonomousmulti-agentframework

“Syncmind: Measuring agent out-of-sync recovery in collaborative
for cognitive behavioral therapy in psychological counseling,” arXiv
softwareengineering,”arXivpreprintarXiv:2502.06994,2025.
preprintarXiv:2501.09426,2025.
[181] M.A.Islam,M.E.Ali,andM.R.Parvez,“Codesim:Multi-agentcode
[156] J.Lee,K.Lim,Y.-C.Jung,andB.-H.Kim,“Psyche:Amulti-faceted
generationandproblemsolvingthroughsimulation-drivenplanningand
patientsimulationframeworkforevaluationofpsychiatricassessment
debugging,”arXivpreprintarXiv:2502.05664,2025.
conversationalagents,”arXivpreprintarXiv:2501.01594,2025.
[182] X.Wan,H.Deng,K.Zou,andS.Xu,“Enhancingtheefficiencyand
[157] Y. Zhang, X. Yang, X. Li, S. Yu, Y. Luan, S. Feng, D. Wang,
accuracyofunderlyingassetreviewsinstructuredfinance:Theappliand Y. Zhang, “Psydraw: A multi-agent multimodal system for
mental health screening in left-behind children,” arXiv preprint cation of multi-agent framework,” arXiv preprint arXiv:2405.04294,
arXiv:2412.14769,2024. 2024.
[158] Z. Du, L. Zheng, R. Hu, Y. Xu, X. Li, Y. Sun, W. Chen, J. Wu, [183] Y. Yang, Y. Zhang, M. Wu, K. Zhang, Y. Zhang, H. Yu, Y. Hu, and
H. Cai, and H. Ying, “Llms can simulate standardized patients via B.Wang,“Twinmarket:Ascalablebehavioralandsocialsimulationfor
agentcoevolution,”arXivpreprintarXiv:2412.11716,2024. financialmarkets,”arXivpreprintarXiv:2502.01506,2025.
[159] R. Wasenmu¨ller, K. Hilbert, and C. Benzmu¨ller, “Script-based dialog [184] Y.Yu,Z.Yao,H.Li,Z.Deng,Y.Jiang,Y.Cao,Z.Chen,J.Suchow,
policyplanningforllm-poweredconversationalagents:Abasicarchi- Z. Cui, R. Liu et al., “Fincon: A synthesized llm multi-agent system
tectureforan”aitherapist”,”arXivpreprintarXiv:2412.15242,2024. with conceptual verbal reinforcement for enhanced financial decision
[160] R.Averly,F.N.Baker,andX.Ning,“Liddia:Language-basedintelli- making,”AdvancesinNeuralInformationProcessingSystems,vol.37,
gentdrugdiscoveryagent,”arXivpreprintarXiv:2502.13959,2025. pp.137010–137045,2024.
[161] X. Wang, Y. Zhang, X. Zhang, L. Yu, X. Lin, J. Jiang, B. Ma, and [185] R. Y. Lin, S. Ojha, K. Cai, and M. F. Chen, “Strategic collusion of
K. Yu, “Patentagent: Intelligent agent for automated pharmaceutical llm agents: Market division in multi-commodity competitions,” arXiv
patentanalysis,”arXivpreprintarXiv:2410.21312,2024. preprintarXiv:2410.00031,2024.
[162] Y.Inoue,T.Song,andT.Fu,“Drugagent:Explainabledrugrepurposing [186] S. Fatemi and Y. Hu, “Enhancing financial question answering with
agent with large language model-based reasoning,” arXiv preprint a multi-agent reflection framework,” in Proceedings of the 5th ACM
arXiv:2408.13378,2024. InternationalConferenceonAIinFinance,2024,pp.530–537.
[163] Z. Chen, Z. Peng, X. Liang, C. Wang, P. Liang, L. Zeng, [187] X.Han,N.Wang,S.Che,H.Yang,K.Zhang,andS.X.Xu,“Enhanc-
M. Ju, and Y. Yuan, “Map: Evaluation and multi-agent enhancement inginvestmentanalysis:Optimizingai-agentcollaborationinfinancial
of large language models for inpatient pathways,” arXiv preprint research,”inProceedingsofthe5thACMInternationalConferenceon
arXiv:2503.13205,2025. AIinFinance,2024,pp.538–546.
[164] T.Yun,E.Yang,M.Safdari,J.H.Lee,V.V.Kumar,S.S.Mahdavi, [188] S.Han,C.Zhou,Y.Shen,T.Sun,Y.Zhou,X.Wang,Z.Yang,J.Zhang,
J. Amar, D. Peyton, R. Aharony, A. Michaelides et al., “Sleepless andH.Li,“Finsphere:Aconversationalstockanalysisagentequipped
nights,sugarydays:Creatingsyntheticuserswithhealthconditionsfor with quantitative tools based on real-time database,” arXiv preprint
realisticcoachingagentinteractions,”arXivpreprintarXiv:2502.13135, arXiv:2501.12399,2025.
2025. [189] G. Fatouros, K. Metaxas, J. Soldatos, and M. Karathanassis, “Mar-
[165] X. Lin, S. Ma, J. Shan, X. Zhang, S. X. Hu, T. Guo, S. Z. Li, and ketsenseai 2.0: Enhancing stock analysis through llm agents,” arXiv
K. Yu, “Biokgbench: A knowledge graph checking benchmark of ai preprintarXiv:2502.00415,2025.
agentforbiomedicalscience,”arXivpreprintarXiv:2407.00466,2024. [190] I.Okpala,A.Golgoon,andA.R.Kannan,“Agenticaisystemsapplied
[166] S. Schmidgall and M. Moor, “Agentrxiv: Towards collaborative au- to tasks in financial services: Modeling and model risk management
tonomousresearch,”arXivpreprintarXiv:2503.18102,2025. crews,”arXivpreprintarXiv:2502.05439,2025.

<!-- Page 44 -->

44
[191] J. Zeng, H. Liu, Z. Dai, X. Tang, C. Luo, S. Varshney, Z. Li, [214] “Beeai now has multiple agents, and a standardized way for
and Q. He, “Cite before you speak: Enhancing context-response them to talk,” accessed: 2025-04-14. [Online]. Available: https:
grounding in e-commerce conversational llm-agents,” arXiv preprint //research.ibm.com/blog/multiagent-bee-ai
arXiv:2503.04830,2025. [215] “A2A: A New Era of Agent Interoperability,” accessed: 2025-
[192] H. Cho, D. Kim, S. Yang, C. Lee, H. Lee, and J. Choo, “Building 04-14. [Online]. Available: https://developers.googleblog.com/en/
resource-constrainedlanguageagents:Akoreancasestudyonchemical a2a-a-new-era-of-agent-interoperability/
toxicityinformation,”arXivpreprintarXiv:2503.17753,2025. [216] X. Hou, Y. Zhao, S. Wang, and H. Wang, “Model context protocol
[193] S. Kumbhar, V. Mishra, K. Coutinho, D. Handa, A. Iquebal, and (mcp): Landscape, security threats, and future research directions,”
C. Baral, “Hypothesis generation for materials discovery and design arXivpreprintarXiv:2503.23278,2025.
using goal-driven and constraint-guided llm agents,” arXiv preprint [217] W.Yuan,J.Yu,S.Jiang,K.Padthe,Y.Li,D.Wang,I.Kulikov,K.Cho,
arXiv:2501.13299,2025. Y.Tian,J.E.Westonetal.,“Naturalreasoning:Reasoninginthewild
[194] B. Lei,Y. Zhang, S. Zuo, A.Payani, and C. Ding,“Macm: Utilizing with 2.8 m challenging questions,” arXiv preprint arXiv:2502.13124,
amulti-agentsystemforconditionmininginsolvingcomplexmathe- 2025.
maticalproblems,”arXivpreprintarXiv:2404.04735,2024. [218] G. Penedo, H. Kydl´ıcˇek, V. Sabolcˇec, B. Messmer, N. Foroutan,
[195] W. Xie, D. Liu, H. Yan, W. Wu, and Z. Liu, “Mathlearner: A large M. Jaggi, L. von Werra, and T. Wolf, “Fineweb2: A sparkling
language model agent framework for learning to solve mathematical update with 1000s of languages,” Dec. 2024. [Online]. Available:
problems,”arXivpreprintarXiv:2408.01779,2024. https://huggingface.co/datasets/HuggingFaceFW/fineweb-2
[196] G. Lee, S. Park, J. Park, A. Chung, S. Park, Y. Park, B. Kim, and [219] Argilla,“Magpieultrav0.1[dataset],”https://huggingface.co/datasets/
M.-g. Cho, “Expanding search space with diverse prompting agents: argilla/magpie-ultra-v0.1,2024,accessed:February16,2025.
Anefficientsamplingapproachforllmmathematicalreasoning,”arXiv [220] C. Costello, S. Guo, A. Goldie, and A. Mirhoseini, “Think, prune,
preprintarXiv:2410.09780,2024. train, improve: Scaling reasoning without scaling models,” 2025.
[197] Y. Deng and P. Mineiro, “Flow-dpo: Improving llm mathemati- [Online].Available:https://arxiv.org/abs/2504.18116
cal reasoning through online multi-agent learning,” arXiv preprint [221] V. Xiang, C. Snell, K. Gandhi, A. Albalak, A. Singh, C. Blagden,
arXiv:2410.22304,2024. D. Phung, R. Rafailov, N. Lile, D. Mahan et al., “Towards system 2
[198] V.Li,Y.Fu,T.Knappe,K.Han,andK.Zhu,“Automatingmathemati- reasoninginllms:Learninghowtothinkwithmetachain-of-though,”
calproofgenerationusinglargelanguagemodelagentsandknowledge arXivpreprintarXiv:2501.04682,2025.
graphs,”arXivpreprintarXiv:2503.11657,2025. [222] M.Z.Pan,M.Cemri,L.A.Agrawal,S.Yang,B.Chopra,R.Tiwari,
[199] R. Wang, R. Pan, Y. Li, J. Zhang, Y. Jia, S. Diao, R. Pi, K.Keutzer,A.Parameswaran,K.Ramchandran,D.Kleinetal.,“Why
J. Hu, and T. Zhang, “Ma-lot: Multi-agent lean-based long chain-of- domultiagentsystemsfail?”inICLR2025WorkshoponBuildingTrust
thought reasoning enhances formal theorem proving,” arXiv preprint inLanguageModelsandApplications.
arXiv:2503.03205,2025. [223] Y. Liu, Z. Yang, T. Xie, J. Ni, B. Gao, Y. Li, S. Tang, W. Ouyang,
[200] M.Yue,W.Lyu,W.Mifdal,J.Suh,Y.Zhang,andZ.Yao,“Mathvc: E. Cambria, and D. Zhou, “Researchbench: Benchmarking llms in
An llm-simulated multi-character virtual classroom for mathematics scientific discovery via inspiration-based task decomposition,” 2025.
education,”arXivpreprintarXiv:2404.06711,2024. [Online].Available:https://arxiv.org/abs/2503.21248
[201] B.Liu,J.Zhang,F.Lin,X.Jia,andM.Peng,“Onesizedoesn’tfitall:A [224] M. Wu, T. Zhu, H. Han, X. Zhang, W. Shao, and W. Chen, “Chainpersonalizedconversationaltutoringagentformathematicsinstruction,” of-tools:Utilizingmassiveunseentoolsinthecotreasoningoffrozen
2025.[Online].Available:https://arxiv.org/abs/2502.12633 languagemodels,”arXivpreprintarXiv:2503.16779,2025.
[202] T.Ma,J.Du,W.Huang,W.Wang,L.Xie,X.Zhong,andJ.T.Zhou, [225] M.Chen,T.Li,H.Sun,Y.Zhou,C.Zhu,F.Yang,Z.Zhou,W.Chen,
“Llmknowsgeometrybetterthanalgebra:Numericalunderstandingof H.Wang,J.Z.Panetal.,“Learningtoreasonwithsearchforllmsvia
llm-basedagentsinatradingarena,”arXivpreprintarXiv:2502.17967, reinforcementlearning,”arXivpreprintarXiv:2503.19470,2025.
2025.
[203] B. Yu, T. Shen, H. Na, L. Chen, and D. Li, “Mineagent: Towards
remote-sensing mineral exploration with multimodal large language
models,”arXivpreprintarXiv:2412.17339,2024.
[204] H.Ning,Z.Li,T.Akinboyewa,andM.N.Lessani,“Anautonomousgis
agentframeworkforgeospatialdataretrieval,”InternationalJournalof
DigitalEarth,vol.18,no.1,p.2458688,2025.
[205] Z.Xu,L.Wang,J.Wang,Z.Li,S.Shi,X.Yang,Y.Wang,B.Hu,J.Yu,
and M. Zhang, “Filmagent: A multi-agent framework for end-to-end
filmautomationinvirtual3dspaces,”arXivpreprintarXiv:2501.12909,
2025.
[206] J.Wang,Z.Du,Y.Zhao,B.Yuan,K.Wang,J.Liang,Y.Zhao,Y.Lu,
G.Li,J.Gaoetal.,“Aesopagent:Agent-drivenevolutionarysystemon
story-to-videoproduction,”arXivpreprintarXiv:2403.07952,2024.
[207] S. Han, L. Chen, L.-M. Lin, Z. Xu, and K. Yu, “Ibsen: Directoractoragentcollaborationforcontrollableandinteractivedramascript
generation,”arXivpreprintarXiv:2407.01093,2024.
[208] A. Maronikolakis, A. P. Ramallo, W. Cheng, and T. Kober, “What
should i wear to a party in a greek taverna? evaluation for conversationalagentsinthefashiondomain,”arXivpreprintarXiv:2408.08907,
2024.
[209] Q. Deng, Q. Yang, R. Yuan, Y. Huang, Y. Wang, X. Liu, Z. Tian,
J. Pan, G. Zhang, H. Lin et al., “Composerx: Multi-agent symbolic
musiccompositionwithllms,”arXivpreprintarXiv:2404.18081,2024.
[210] D.Yu,K.Song,P.Lu,T.He,X.Tan,W.Ye,S.Zhang,andJ.Bian,
“Musicagent:Anaiagentformusicunderstandingandgenerationwith
largelanguagemodels,”arXivpreprintarXiv:2310.11954,2023.
[211] R. Zhang and S. Eger, “Llm-based multi-agent poetry generation
in non-cooperative environments,” arXiv preprint arXiv:2409.03659,
2024.
[212] H.-H. Liu and Y.-W. Liu, “Agent-driven large language models for
mandarin lyric generation,” in 2024 27th Conference of the Oriental COCOSDA International Committee for the Co-ordination and
Standardisation of Speech Databases and Assessment Techniques (O-
COCOSDA). IEEE,2024,pp.1–6.
[213] “Introduction to mcp,” accessed: 2025-04-14. [Online]. Available:
https://modelcontextprotocol.io/introduction

## Tables

**Table (Page 36):**

|  |
|---|
| A2A protocol |
|  |


**Table (Page 36):**

|  |
|---|
| A2A protocol |
|  |


**Table (Page 36):**

|  |
|---|
| A2A protocol |
|  |
