---
title: "SCOOP Proactive Collaboration Social"
original_file: "./SCOOP_Proactive_Collaboration_Social.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["llm", "rag", "react", "agents", "fine-tuning"]
keywords: ["causal", "information", "making", "language", "user", "question", "llms", "planning", "act", "page"]
summary: "<!-- Page 1 -->

5202
raM
31
]AM.sc[
1v14201.3052:viXra

### SCOOP: A Framework for Proactive Collaboration and Social

Continual Learning through Natural Language Interaction and

### Causal Reasoning

DimitriOgnibene,SabrinaPatania,LucaAnnese,CansuKoyuturk,FrancaGarzotto,GiuseppeVizzari
UniversityofMilan-Bicocca

### Milan,Italy

dimitri.ognibene@unimib.it

### AzzurraRuggeri SimoneColombani

TUMSchoolofSocialSciencesandTechnology OversonicRobotics
Munich,Germany CarateBrianza,Italy
a.ruggeri@"
related_documents: []
---

# SCOOP Proactive Collaboration Social

<!-- Page 1 -->

5202
raM
31
]AM.sc[
1v14201.3052:viXra

### SCOOP: A Framework for Proactive Collaboration and Social

Continual Learning through Natural Language Interaction and

### Causal Reasoning

DimitriOgnibene,SabrinaPatania,LucaAnnese,CansuKoyuturk,FrancaGarzotto,GiuseppeVizzari
UniversityofMilan-Bicocca

### Milan,Italy

dimitri.ognibene@unimib.it

### AzzurraRuggeri SimoneColombani

TUMSchoolofSocialSciencesandTechnology OversonicRobotics
Munich,Germany CarateBrianza,Italy
a.ruggeri@tum.de

### Abstract

Multimodalinformation-gatheringsettings,whereuserscollaboratewithAIindynamicenvironments,areincreasingly
common. Thesescenariosinvolvecomplexprocesseswithtextualandmultimodalinteraction(e.g.,houserefurbishment
plans)andoftenrequireaccessingadditionalstructuralinformation(e.g.,regulations)viacost-incurringrequests. Moreover, AI helpers lack access to users’ true goals, beliefs, and preferencesand struggle to integrate diverse information
effectively.
Weproposeasocialcontinuallearningframeworkforcausalknowledgeacquisitionandcollaborativedecision-making.
Itfocusesonautonomousagentslearningthroughdialogues,question-asking,andinteractioninopen,partiallyobservableenvironments. Akeycomponentisanaturallanguageoraclethatanswerstheagent’squeriesaboutenvironmental
mechanisms and states, refining causal understanding while balancing exploration (learning) and exploitation (using
knowledge).
Evaluationtasks, inspiredbydevelopmentalpsychology, emphasizecausalreasoningandquestion-asking skills, complementing benchmarksbyassessingthe agent’sabilitytoidentifyknowledge gaps, generatemeaningfulqueries, and
incrementallyupdatereasoning. Theframeworkalsoevaluateshowthecostofacquiringknowledgeisamortizedacross
tasksinthesameenvironment.
Weproposetwoarchitectures: (1)asystemcombiningLargeLanguageModels(LLMs)withtheReActframeworkand
question-generation, and (2) anadvanced system with a causal world model (symbolic, graph-based, or subsymbolic)
forreasoninganddecision-making. Thelatterbuildsacausalknowledge graphforefficientinferenceandadaptability
underconstraints. ChallengesincludeintegratingcausalreasoningintoReActandoptimizingexplorationandquestionaskinginerror-pronescenarios.Beyondapplications,thisframeworkmodelsdevelopmentalprocessescombiningcausal
reasoning,questiongeneration,andsociallearning.
Keywords: sociallearning,questiongeneration,collaborativeAI,LLM,planning,continuallearning,cognitivedevelopment.

### Acknowledgements

WeacknowledgesupportfromtheVolkswagenFoundationfortheprojectDevelopinganArtificialSocialChildhood(ASC)
toimproveAIcausalreasoning,informationgatheringanddecisionmaking,Ref.: 9E530.

<!-- Page 2 -->

1 Introduction
WiththeadventofadvancedgenerativeAI,tasksinvolvingrichmultimodalandnaturallanguageinformation—where
userscollaboratewithAIhelpers—arebecomingincreasinglycommon. Thesesettingsofteninvolve:

## Sequential Collaborative Interactions: performing the task requires planning and executing of sequences of

interactions and independent by the user or the agent (e.g. collecting different elements and tools), with the
needtoaccountfortheirconsequencesovermultiplesteps.

## CostlySocialInformationAccess:usersandagentsmustmanagelimitedresourceswhenaccessinginformation

providedbyotheragents(e.g.,mechanismsdescriptions,regulationsoruserpreferencesorbeliefs[1]).

## Multimodal complexity: combining textual descriptions, visual representations, and structural information

(e.g.,houserefurbishmentplans).

## DynamicEnvironments: evolvingtaskswithshifting statesandrequirements(e.g.,bureaucraticprocesses,repairscenarios)[27].

Thesimultaneouspresenceoftheseconditionsandtheirinteractionmotivateourworktoformalizeandcreateeffective
solutions. Moreover,theyreflectimportantaspectsofhumandevelopmentalprocesses[3,6].
1.1 ExampleScenarios

### Example1: RepairingandShippingItems

A robot agent assists in repairing and shipping items to various international destinations. Tasks include adhering to
specificrepairrequirements,customsregulations, packagingstandards,andclimateconditions. Theagentcollaborates
with the user to clarify repairstrategies and queries a natural language oracle for regulatory or technical information.
During downtime, the agentexplorestools andequipment torefineits understandingofrepairtechniques, improving
futureperformance.

### Example2: CompilingDocumentsforOfficialRequests

An agent aidsa user in compiling documents for official applications, such asvisas or tax submissions. Tasks involve
identifyingrequireddocuments,extractingrelevantinformation,andvalidatingregulationsviaanaturallanguageoracle. Whenambiguitiesarise,theagentinteractswiththeuserforclarification. Inidleperiods,itautonomouslyexplores
documenttemplatesandregulatoryarchivestoimproveperformanceacrossmultipleprobleminstances.
2 RelatedWork
ReActFramework:TheReAct(Reason+Act)framework[26]integratesreasoningandactingcapabilitiesintoLLMs,enablingcontextualdecision-makingandblendingquestiongenerationwithaction-takingincollaborativeenvironments.
CausalReasoninginAI:Techniqueslikecausaldiscovery[12]andinferenceframeworkssuchasDoWhy[32]provide
essentialtoolsforreasoningindynamic,partiallyobservableenvironments.
IntegratingCausalGraphswithLLMs: RecentresearchintegratescausalgraphswithLLMstoenhancereasoningand
decision-making. EmbeddingcausalreasoningintoLLMworkflowsenablessystemstointerpretenvironments,predict
outcomes,andoptimizeactions. FrameworkscombiningLLMswithcausalworldmodels[11]andstudiesonautomating causal discovery [23] highlight the potential of causal representation learning for dynamically constructing world
models.
LLMs and Planning Systems: Combining LLMs with planning systems, such as symbolic planners or reinforcement
learning frameworks, supports structured decision-making. Hybrid approaches integrate LLMs for language understanding and planners for task execution, excelling in complex scenarios like multi-agent collaboration and robotics
[22,30].
CausalDiscoveryandQuestionGeneration: IntegratingLLMswithcausaldiscoverytoolsenhancesreasoningindynamicenvironments. Forinstance,PyWhy-LLMsupportscausalanalysis[9],whileDoWhy-GCMfacilitatesinferencein
graphicalcausalmodels[19]. ThesetoolsenableLLMstorefinecausalgraphsandresolveambiguities,closingtheloop
betweenknowledgeacquisitionandaction.
SymbolicandSubsymbolicIntegration: Hybrid architecturesbridgesymbolic causalreasoningwiththesubsymbolic
capabilitiesof LLMs, combining graph-basedreasoningwith unstructured dataprocessingfor robustdecision-making
agents[20,16].
2

<!-- Page 3 -->

ActiveInformationGathering:Researchonactivelearningandinformationgain[24,15,14,8,10]informsstrategiesfor
queryingtomaximizeutilitywhilebalancingexplorationandexploitationininteractivesystems.
Human-in-the-LoopSystems:Humanfeedbackintegrationhighlightsthevalueofinteractivelearning,enablingagents
todynamicallyqueryusersandadapttopreferences[21].
DevelopmentalPsychologyInsights:Insightsfromchildren’scausallearning[5,31]inspirebenchmarkstoevaluateAI
agents’abilitiesinquestiongenerationandcausalinference.
By synthesizing these elements, our framework advancesadaptive, interactive AI systems atthe intersection of causal
reasoning,sociallearning,andmultimodalinteraction.
3 The SCOOPframework: SocialContinual Object-OrientedPOMDP
FormalFramework. Weformalizeourrichinteractivesettingasanobject-orientedpartiallyobservableMarkovdecision
process (OO-POMDP), extended to incorporate a lingusistic world descriptor generating natural language observations
(e.g. theinitialtaskdescriptioninnaturallanguage),multipleprobleminstances,auserwithproblem-specificobjectives,
andanaturallanguageoraclethatprovidescausalinformation. Let
D=(cid:0)T O ,F O ,R O ,W O(cid:1)
denoteadomainspecification,where:
• T isasetofobjecttypes(e.g.,boxes,tools,containers);

## O

• F isthesetofallowedfeaturesorpredicatesrelevanttothedomain(e.g.,“contains(x,y)”or“isOpenable(x)”);

## O

• R isanevolvingsetofcausalrulescapturinghowthesefeaturesandobjecttypesinteract(e.g.,whetheropening

## O

acontainerallowsaccesstoitscontents),someofwhichmaybeunknownorpartiallyspecified;
• W isthefamilyofpossibleworldconfigurationsconsistentwithT ,F ,andR .

## O O O O

A problem instance θ refines D with a concrete set of objects, an initial state, and a user objective (defined by a problemspecificrewardfunctionr thatencodestheuser’sgoals). Thehelperagentinteractswithboththeuser,makingquestions
θ
toclarifyhisgoalsorpreferences,presentingresultsandsuggestions,orotherinteractiveactions,andanaturallanguage
oracle(toacquiremissingcausalrulesorenvironmentstates)acrosspotentiallymanyprobleminstances{θ }. Theoracle
i
respondsinmultipleformats:

## Language-baseddescriptionsofenvironmentdynamics,suchas“boxAmustbeopenedbeforeretrievingitemB”;


## Formalcausalchunks,wheretheoraclemaydirectlyproviderulesorgraphsparts(e.g.,“nodeOpen(Box)causes


### Accessible(Item)”),


## Observation-likefeedback,akintosensorreadingsorstateconfirmations.

TheoverallactionspaceA = Aa∪Au composedbytheagent’sactionspacebyAa andtheuser’sactionspacebyAu. We
denotetheagent’sactionspacebyAa =Aa ∪Aa ,whereA includesenvironment-orientedactions(e.g.,open,pick,
act query act
place)andA includesqueriestotheoracleortheuser. Theagentalsoobservestheuser’sfeedbackorclarifications
query
regardingthe task objectives and environment states. We denote the user’s action spaceby Au = Au ∪Au , where
act query
⊓
A includesenvironment-orientedactions(e.g.,open,pick,place)andA includesqueriestotheagent. Formally,
act query
eachprobleminstanceismodeledas:
(S ,A,Ω ,T ,O ,ru,ra,γ,β),
θ θ θ θ θ θ
mirroringaPOMDPwiththefollowingmodifications:
• S embedstheobject-basedstatesfromθandanypartialknowledgeofthecausalrulesR ;
θ O
• Ω isthespaceofpossibleobservations,spanningbothenvironmentalsignals(e.g.,sensorreadings,gripperstate,
θ
environmentmapchunk,etc)andlanguage-basedresponsesfromtheuserororacle;
• ru encodestheuser’sobjectivesforinstanceθ,whichthehelperagentaimstooptimize;
θ
• ra encodesthehelperagent’sactioncostsforinstanceθ,whichthehelperagentaimstooptimize;
θ
• β(·) defines the cost of querying (time, resources, or complexity) the oracle to obtain new causal information or
theuseraboutcurrentobjectiveandpreferences,i.e. ru.
θ
Crucially,theagentcanexplorethedomainoutsideactivetaskstorefineR (e.g.,byperformingexperimentsorasking

## O

domain-level questions). Any information gleaned is amortized across future tasks θ . This design enables continual
j
learningofdomainmechanics: astheagentaccumulatescausalknowledge(e.g.,“acertainboxcancontainitemsoftype
3

<!-- Page 4 -->

T”), it improves performance in subsequent problem instances. More formally this is obtained assuming that at each
instanceθ thespecificinstantiationofR ,ru andra areextractedfromthesamedistribution.
j O θ θ
Ultimately,thehelperagentobjectivefunctionsis:P θ P t T(θ)γt+T(−θ)(r θ u(s t ,au t )+r θ a(s t ,aa t )+β(aa t )). Balancingexploration
(question-asking,activeexperimentation)andexploitation(leveragingcurrentknowledgetosolvetasksefficiently)isthus
acentralchallengeinthissocialcontinuallearningframework.
4 DevelopmentalPsychology-Inspired Tasks for EvaluatingCausalReasoningand

### Question-Making

Drawing fromdevelopmental psychology, we design tasks to evaluate causalreasoning and question-making skills in
collaborativeAIsystems. Inspiredbychildren’slearningbehaviors,thesetasksassesstheagent’sabilityto:
Explore-Exploit Tradeoff: Balance between directed exploration and utilizing known information to reduce uncertainty
andachievegoalsefficiently[7]. ”Why”and”WhatIf”Questions: Formulatemeaningfulhypothesesandevaluatecounterfactualscenariostorefinecausalmodels[33]. EpistemicQuestionFormulation: Constructprecise,goal-directedqueries
toaddressknowledgegapsefficiently[25].CausalInferenceandLearning:EngageAIintaskswhereitobservesincomplete
sequences of eventsand must infer causalrelationships. For example, afterobservingthatcertaincomponents drivea
machine,theAIpredictsoutcomeswithoutdirecttrial-and-error[4,18]. GeneratingHypothesesfromConfoundedEvidence:
AssessesAI’sabilitytogenerateinterventionsthatareinformativeinresolvingthestructureofambiguouscausalsystem
[29].ThesetasksprovideamultidimensionalframeworktobenchmarkAIsystems,focusingoncognitive,linguistic,and
socialreasoningcapabilitiesessentialfordynamic,real-worldcollaboration.
5 Referencearchitectures
5.1 Base: Oracle-AidedReAct
The base architecture simply extends the ReAct framework introducing actions to ask state and the user about their
preference and objectives and the oracle about environment mechanics. However, as noted in the literature, complex
planning [17] and usage of declarative knowledge for decision making and execution [2] appear difficult for vanilla
LLMs.
5.2 Advanced:ReActFrameworkwithOracle-AidedCausalReasoning
Buildingonthebasearchitecture,theadvancedReAct(Reason+Act)[26]frameworkintroducesinformation-gathering
actionsandextendsitsfunctionalitywithaspecializedaction,CausalRefinementAndAction.Thisactionisinvoked
bytheLargeLanguageModel(LLM)whencomplexreasoningtasksarerequired,specificallyfor:
• Refiningorupdatingknowledgeaboutuserneedsandtheworld’smechanismsandstates(causalmodel),or
• Planningandexecutingstepstoachieveaspecifiedgoal.
CausalRefinementAndActionintegratesiterativecausalknowledgemanagement,utilizingbothexternaloraclesupport(e.g.,adomainexpertorautomatedsimulator)andestablishedcausalinferencelibrariessuchascausal-learn,DoWhy,
andTetrad[28,32,13]. Givenauser’sprompt,currentgoal,andcontextualinformation,theLLMinitiallymapsrelevant
knowledgetoacausalgraph,whichmaybeincomplete.
Theagentestimatestheexpectedvalueandcostofpotentialactionstorefineitsknowledge,usingmetricssuchasValue
ofInformation(VoI)orrobustoptimizationcriteria. Refinementactionsincludequeryingtheuseraboutpreferencesand
goals,askingtheoracleaboutspecificcausallinksoreffectsizes,orperforminginterventions. Iftherefinementisdeemed
beneficial(i.e.,costisbelowathreshold),thesuggestedstrategyisexecuted.Basedonresponsesfromtheuserororacle,
orresultsofinterventions,causalinferencelibrariesupdatethegraphanddeterminewhetheradditionalrefinementsare
necessary.
Oncethecausalgraphissufficientlyrefined,theReActagentinvokesplanningroutines—usinglibrariessuchasPyCID
orarobustMarkovDecisionProcess(MDP)solver—toderivepoliciesoractionsequencesthatmaximizethelikelihood
of achieving the user’s goals under the current causal knowledge. This combination of LLM-drivenreasoning, causal
knowledge management, and decision-making enable advanced reasoning and information-gathering capabilities are
activatedwhennecessarywhilemaintainingtheflexibilitytohandlediversescenariostypicalofLLMs.
4

<!-- Page 5 -->


### References

[1] F.BiancoandD.Ognibene. Frompsychologicalintentionrecognitiontheoriestoadaptivetheoryofmindforrobots:
Computationalmodels. InHRI,pages136–138,2020.
[2] A.Arabietal. Habitcoach: Customisingrag-basedchatbotstosupportbehaviorchange. arXiv,2024.
[3] A. Cangelosi et al. Integration of action and language knowledge: A roadmap for developmental robotics. IEEE
TransactionsonAutonomousMentalDevelopment,2(3):167–195,2010.
[4] A.Gopniketal. Causallearningmechanismsinveryyoungchildren: two-,three-,andfour-year-oldsinfercausal
relationsfrompatternsofvariationandcovariation. Dev.Psychol.,37(5):620,2001.
[5] A.Gopniketal. Atheoryofcausallearninginchildren: causalmapsandbayesnets. Psychol.Rev.,111(1):3,2004.
[6] A.Ruggerietal. Sourcesofdevelopmentalchangeintheefficiencyofinformationsearch. Developmentalpsychology,
52(12):2159,2016.
[7] B.Mederetal. Developmentofdirectedandrandomexplorationinchildren. Dev.Sci.,24(4):e13095,2021.
[8] D. Ognibene et al. Proactive intention recognition for joint human-robot search and rescue missions through
monte-carlo planning in pomdp environments. In Social Robotics: 11th International Conference, ICSR, pages 332–

### Springer,2019.

[9] E.Kıcımanetal. Causalreasoningandlargelanguagemodels: Openinganewfrontierforcausality. arXiv,2023.
[10] E.Masieroetal. Insearchofcompositionalmulti-taskdeeparchitecturesforinformationtheoreticfieldexploration.
In2024IEEE20thInternationalConferenceonAutomationScienceandEngineering(CASE),pages612–617.IEEE,2024.
[11] J.Gkountourasetal. Languageagentsmeetcausality–bridgingllmsandcausalworldmodels,2024.
[12] J.Petersetal. Elementsofcausalinference: foundationsandlearningalgorithms. MITPress,2017.
[13] J.Ramseyetal. Tetrad—atoolboxforcausaldiscovery. InClimateInformatics,pages1–4,2018.
[14] K.Fristonetal. Activeinferenceandepistemicvalue. Cogn.Neurosci.,6(4):187–214,2015.
[15] L. Bertolazziet al. Chatgpt’s information seeking strategy: Insights fromthe 20-questions game. In INLG, pages
153–162,2023.
[16] M. Ibrahim et al. Special session: Neuro-symbolic architecture meets large language models: A memory-centric
perspective. InCODES+ISSS,pages11–20,2024.
[17] M.Katzetal. Thoughtofsearch:Planningwithlanguagemodelsthroughthelensofefficiency. InNeurIPS,2024.
[18] M.Shavliketal. Contributionsofcausalreasoningtoearlyscientificliteracy. J.Exp.ChildPsychol.,224:105509,2022.
[19] P. Blo¨baum et al. Dowhy-gcm: An extension of dowhy for causal inference in graphical causal models. JMLR,
25(147):1–7,2024.
[20] P.Hitzleretal. Neuro-symbolicapproachesinartificialintelligence. Natl.Sci.Rev.,9(6):nwac035,2022.
[21] S.Amershietal. Powertothepeople: Theroleofhumansininteractivemachinelearning. AIMag.,35(4):105–120,
2014.
[22] S. Colombani etal. One to rule them all: naturallanguage tobind communication, perceptionand action. arXiv,
2024.
[23] S.Longetal. Canlargelanguagemodelsbuildcausalgraphs?,2024.
[24] S. Patania et al. Large language models as an active bayesian filter: information acquisition and integration. In
SemDial,2024.
[25] S.Ronfard etal. Question-asking inchildhood: A reviewof the literatureand aframeworkforunderstandingits
development. Dev.Rev.,49:21–39,2018.
[26] S.Yaoetal. React: Synergizingreasoningandactinginlanguagemodels,2023.
[27] T. Taniguchi et al. World models and predictive coding for cognitive and developmental robotics: Frontiers and
challenges. Adv.Robot.,37(13):780–806,2023.
[28] Y.Zhengetal. Causal-learn:Causaldiscoveryinpython. JMLR,25(60):1–8,2024.
[29] H.GweonandL.Schulz.Stretchingtolearn:Ambiguousevidenceandvariabilityinpreschoolers’exploratoryplay.
InCogSci,pages570–574,2008.
[30] SKambhampatiandetal. Llmscan’tplan. arXiv:2402.01817,2024.
[31] C.Legare. Thecontributions ofexplanationandexplorationtochildren’sscientific reasoning. ChildDev.Perspect.,
8(2):101–106,2014.
[32] A.SharmaandE.Kiciman. Dowhy: Anend-to-endlibraryforcausalinference. arXiv,2020.
[33] C.WalkerandA.Nyhout. Asking”why?”and”whatif?”: Theinfluence ofquestionsonchildren’sinferences. In
TheQuestioningChild,pages252–280.2020.
5