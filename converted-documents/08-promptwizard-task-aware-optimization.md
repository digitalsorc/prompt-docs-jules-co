---
title: "PromptWizard Task Aware Optimization"
original_file: "./08_PromptWizard_Task_Aware_Optimization.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["prompt-engineering", "llm", "rag", "chain-of-thought", "agents"]
keywords: ["answer", "question", "page", "your", "name", "patient", "stamps", "symptoms", "you", "last"]
summary: "<!-- Page 1 -->


## Promptwizard:


## Task-Aware Prompt Optimization Framework

EshaanAgarwal,JoykiratSingh,VivekDani,RaghavMagazine,TanujaGanu,AkshayNambi

### MicrosoftResearchIndia

Correspondingauthor: akshayn@microsoft.com

## Abstract

Largelanguagemodels(LLMs)havetransformedAIacrossdiversedomains,with
promptingbeingcentraltotheirsuccessinguidingmodeloutputs. However,manualpromptengineeringisbothlabor-intensiveanddomain-specific,necessitating
the need for automated solutions. We introduc"
related_documents: []
---

# PromptWizard Task Aware Optimization

<!-- Page 1 -->


## Promptwizard:


## Task-Aware Prompt Optimization Framework

EshaanAgarwal,JoykiratSingh,VivekDani,RaghavMagazine,TanujaGanu,AkshayNambi

### MicrosoftResearchIndia

Correspondingauthor: akshayn@microsoft.com

## Abstract

Largelanguagemodels(LLMs)havetransformedAIacrossdiversedomains,with
promptingbeingcentraltotheirsuccessinguidingmodeloutputs. However,manualpromptengineeringisbothlabor-intensiveanddomain-specific,necessitating
the need for automated solutions. We introduce PromptWizard, a novel, fully
automatedframeworkfordiscretepromptoptimization,utilizingaself-evolving,
self-adaptingmechanism. Throughafeedback-drivencritiqueandsynthesisprocess, PromptWizard achieves an effective balance between exploration and exploitation,iterativelyrefiningbothpromptinstructionsandin-contextexamplesto
generatehuman-readable,task-specificprompts. Thisguidedapproachsystematicallyimprovespromptquality,resultinginsuperiorperformanceacross45tasks.
PromptWizardexcelsevenwithlimitedtrainingdata,smallerLLMs,andvarious
LLMarchitectures.Additionally,ourcostanalysisrevealsasubstantialreductionin
APIcalls,tokenusage,andoverallcost,demonstratingPromptWizard’sefficiency,
scalability,andadvantagesoverexistingpromptoptimizationstrategies.

## 1 Introduction

Largelanguagemodels(LLMs)likeGPT-4(OpenAIetal.,2024)haveachievedremarkableperformanceacrossdiversetasks(Colomboetal.,2024;Nguyenetal.,2023;Zhangetal.,2024). At
thecoreofthissuccessisprompting—theprocessofprovidinginputinstructionstoguidemodels
towarddesiredoutputs. StudieshaveshownthatpromptingsignificantlyinfluencesLLMperformance,makingpromptengineering—thedesignandrefinementofprompts—criticalformaximizing
accuracy(Wangetal.,2023c;b;Norietal.,2023). However,craftingeffectivepromptsremainsa
labor-intensiveanddomain-specifictask,requiringhumanexpertiseandsubjectivejudgment. As
modelsevolveandtasksvary,theneedtorepeatedlydesignpromptsraisesanimportantquestion:
Canpromptengineeringbeautomatedtostreamlinethisprocessandenhancescalability?
Automatically generating optimal prompts is a key challenge in the era of LLMs (Pryzant et al.,
2023; Zhou et al., 2023). Some approaches, such as gradient-based methods, have been used to
optimizepromptsbyleveragingtokenprobabilitiesandmodelgradients(Dengetal.,2022;Zhang
etal.,2022a). However,thesemethodsarelimitedtowhite-box(open-source)models,astheyrequire
directaccesstothemodel’sinternalmechanics(Liuetal.,2023). ThemostpowerfulLLMstoday,
likeGPT-4andGemini,aretypicallyblack-box(closed-source)andaccessibleonlythroughAPIs,
makingsuchtechniquesimpracticalandareoftenresource-intensive.
Thisnecessitatesgradient-freepromptoptimizationstrategies. Recentmethodshavefocusedonenumeratingdiversepromptsorrefiningexistingonestooptimizeinstructionsforblack-boxLLMs(Zhou
et al., 2023; Lin et al., 2024; Chen et al., 2023; Fernando et al., 2023; Guo et al., 2024). These
strategies can be broadly classified into two types: continuous and discrete prompt optimization.
Continuousapproaches,likeInstructZero(Chenetal.,2023)andInstinct(Linetal.,2024),convert
promptoptimizationintoacontinuousproblembyusingsoftprompts. Thesesoftpromptsarefedto
open-sourceLLMstogenerateinstructions,whicharethenevaluatedbythetargetblack-boxLLM.
ThefeedbackisusedtotrainaBayesianoptimizer(BO)orneuralnetwork(NN)topredictbetter
instructions. However,thesemethodsrequireadditionaltrainingofNNsandtheirperformanceoften
variesbasedontheopen-sourcemodelandtaskcomplexity. Formorecomplextasks,learningtheoptimalprompt-performancemappingbecomeschallenging. Ontheotherhand,discretemethodslike
PromptBreeder(Fernandoetal.,2023)andEvoPrompt(Guoetal.,2024)generatemultipleprompt
1
4202
tcO
3
]LC.sc[
2v96381.5042:viXra

<!-- Page 2 -->

Input PromptWizard Final Prompt
Sequential

### Problem

Problem Optimization Description

### Description

Iterative Modified Prompt Instruction Optimized Optimized

### Refinement Instruction Optimization Prompt Prompt

In P st r r o u m ct p io t n of Prompt R S e e a lf s -g o e n n in e g ra a te n d d Optimized

### Instructions Validation Few-shot with


### Diverse Synthetic Synthesized reasoning

Training Examples Example Examples Task Intent +
Examples Selection Generation Expert Persona
Figure1: OverviewofPromptWizardframework.
versionsusingevolutionaryorself-referentialstrategies. Whilethesemethodsexpandexplorationby
scoringprompts,theylackfeedbackmechanisms,leadingtoinefficientandsuboptimalexploration.
Inthispaper, weproposePromptWizard(PW),adiscretepromptoptimizationframeworkfor
black-boxLLMs. PromptWizardemploysaself-evolvingmechanismwheretheLLMgenerates,
critiques, and refines its own prompts and examples, continuously improving through iterative
feedbackandsynthesis. Thisself-adaptiveapproachensuresholisticoptimizationbyevolvingboth
the instructions and in-context learning examples for better task performance. PromptWizard
operatesintwophases: (i)Promptgeneration(one-time),whereitprocessesahigh-levelproblem
description and training samples, using LLMs to mutate, score, critique, synthesize, reason, and
validate prompts and examples; (ii) Inference (test-time), where the final optimized prompt and
examplesareappliedtotestsamples.
PW’s approach follows a structured strategy (See Figure 1): ➊ First, starting with a problem
descriptionandinitialpromptinstruction,PWgeneratesvariationsoftheinstructionbyprompting
LLMstomutateit.Basedonperformance,thebestpromptisselected.Unlikeuncontrolledevolutions
inpriormethods(Fernandoetal.,2023;Guoetal.,2024),PWincorporatesacritiquecomponent
thatprovidesfeedback,thusguidingandrefiningthepromptovermultipleiterations. ➋Unlikeother
discreteapproaches,PWalsooptimizesin-contextexamples. PWselectsadiversesetofexamples
fromthetrainingdata,identifyingpositiveandnegativeexamplesbasedontheirperformancewith
themodifiedprompt. Negativeexampleshelpinformfurtherpromptrefinements. ➌Examplesand
instructionsaresequentiallyoptimized,usingthecritiquetogeneratesyntheticexamplesthataddress
thecurrentprompt’sweaknesses. Theseexamplesareintegratedtofurtherrefinetheprompt. ➍PW
generatesdetailedreasoningchainsviaChain-of-Thought(CoT),enrichingtheprompt’scapacityfor
problem-solving. ➎PWalignspromptswithhumanreasoningbyintegratingtaskintentandexpert
personas,enhancingbothmodelperformanceandinterpretability.
Ourworkdistinguishesitselffrompreviousapproachesinseveralkeyaspects: 1. GuidedExploration: PromptWizardintroducesafeedback-drivencritique-and-synthesismechanism,refining
promptsbasedonperformanceinsights. Thisguidedexplorationsystematicallyimprovesprompt
quality,overcomingtherandomnessandinefficienciesinmethodslikePromptBreeder(Fernando
etal.,2023),OPRO(Yangetal.,2024),andEvoPrompt(Guoetal.,2024)(Section3.1). 2. SequentialOptimizationofInstructionsandExamples: PromptWizarddynamicallyanditeratively
optimizesbothpromptinstructionsandin-contextexamplesintandem,outperformingmethodsthat
optimizethesecomponentsinisolation. Thisstrategyallowsdeeperexploitationoftask-specific
nuances,leadingtosuperiorpromptquality(Section3.3). 3. EfficientExampleSynthesis&Error
Analysis: PromptWizardenhancesefficiencybyutilizingacompactsetofdiverseexamples(up
to25)andleveragingerror-drivenself-reflectiontogeneratesyntheticexamples. Combinedwith
Chain-of-Thoughtreasoning,thisapproachoffersrobustandscalablepromptrefinement,settingit
apartfromexistingmethods(Section3.4).
WeevaluatetheeffectivenessofPromptWizardonthewidely-usedBigBenchInstructionInduction (BBII), Big Bench Hard (BBH), and arithmetic reasoning datasets, covering over 45 tasks
ranging from general reasoning to domain-specific challenges (Section 4). As shown in Figure 2, PromptWizard consistently outperforms state-of-the-art approaches, including Instinct,
InstructZero,APE,PromptBreeder,andEvoPromptontheBBIIdataset.
Through extensive experimentation, we demonstrate that PromptWizard consistently outperforms SOTA baselines in both zero-shot and few-shot scenarios, while maintaining superior efficiency (Section 5.1). Our comprehensive cost analysis highlights the significant reduction in
2

<!-- Page 3 -->

API calls, token usage, and overall expenses, showcasing PW’s ability to deliver high-quality
prompts with minimal computational cost (Section 5.2). Furthermore, we conduct numerous experimentstoshowcasePromptWizard’sefficacywithlimitedtrainingdataandsmallerLLMs,
along with ablation studies that assess its performance across different base LLMs (Section 6).
1.0
0.8
0.6
0.4
0.2
0.0 0.1 0.2 0.3
)
(

### Our main contributions are: (i) we introduce


### PromptWizard, a novel framework for automatic

discrete prompt optimization using a self-evolving,
self-adapting mechanism. Through feedback-driven
critique and synthesis process, PW strikes an effective
balancebetweenexplorationandexploitation,iteratively APE

### InstructZero

refiningbothpromptinstructionsandin-contextexamples. PromptBreeder
Thusgeneratinghuman-readable,task-specificprompts, EvoPrompt

## Instinct

(ii) we demonstrate PW’s superior performance and PromptWizard
efficiencyacross45tasks,outperformingSOTAmethods.

### Figure2: Performanceprofilecurveof

2 RELATED WORK PromptWizard over other baselines
(Section5.1,Appendix11).
Researchinpromptoptimizationhasincreasinglyshifted
towardautomatingpromptcreationduetothelimitations
ofhandcraftedprompts(Moradi&Samwald,2021;Madaan&Yazdanbakhsh,2022;Weietal.,2022).
Recentworkhasintroducedvarioustechniquesforautomatingpromptgeneration,broadlyclassified
intocontinuousanddiscrete(Yangetal.,2024;Guoetal.,2024). Below,weexaminethesemethods,
theirlimitations,andhowPromptWizard(PW)advancesthefield.
ContinuousPromptOptimization. Continuousmethods,suchasInstructZero(Chenetal.,2023)
andInstinct(Linetal.,2024),treatpromptoptimizationasacontinuouslearningproblemusingsoft
prompts—trainablevectorsthatfine-tuneresponsesfromopen-sourceLLMs. Thesesoftpromptsare
usedtogenerateresponses,withfeedbackguidingtheoptimizationthroughmodelslikeBayesian
optimizersorneuralnetworks. Whileflexible,thesemethodsfaceseveralkeylimitations: (i)They
requireadditionalneuralnetworktraining,leadingtohighcomputationalcosts,(ii)Theiradaptability
tocomplextasksthatneednuancedpromptsislimited,assoftpromptsarenothuman-interpretable
andstruggletocapturethedepthoftask-specificreasoning,(iii)Formoreintricatetasks,suchas
arithmeticreasoning,mappingtherelationshipbetweenpromptstructureandperformancebecomes
challenging,oftenleadingtosuboptimalorinconsistentresults. Thus,whilecontinuousmethods
improvepromptgeneration,theirscalabilityandinterpretabilityincomplextasksremainnon-trivial.
Discrete Prompt Optimization. Discrete methods focus on exploration by generating multiple
promptversionsandselectingthebestamongcandidates.ThesemethodsrelyonstrategieslikeMonte
Carlosearchesorevolutionaryprocesses. Forexample,APE(Zhouetal.,2023)iterativelyproposes
andselectsoptimalpromptsthroughaMonteCarlosearch,whilePromptBreeder(Fernandoetal.,
2023)mutatespromptsusingdifferentthinkingstyles,evolvingpromptsinaself-referentialmanner.
Othermethods,suchasOPRO(Yangetal.,2024)andEvoPrompt(Guoetal.,2024),relyonprompt
mutations, evolutionaryalgorithmsandevaluationsonfixedtrainingsamples. However, discrete
methodshavenotabledrawbacks: (i)Theyareoftenquery-inefficientduetotheirrelianceonlocal
searchtechniques,whichfailtobalanceexplorationandexploitationeffectively,(ii)Thesemethods
tendtoexplorethepromptspacerandomlyorthroughmutationswithoutastructuredmechanismfor
feedback,resultinginsuboptimalandunguidedrefinementofprompts. Recentmethodsoptimize
both instructions and examples in prompting, emphasizing the importance of example selection
throughrandomordiversity-basedoradversarialtechniques(Doetal.,2024;Wanetal.,2024). In
contrast,PWusesaLLMtoanalyzeandsynthesizeexamples,dynamicallyenhancingpromptquality
andoutperformingtraditionalfixed-criteriastrategies.
ComparisonandMotivationforPromptWizard. PromptWizard(PW)advancesbeyondthese
limitationsbyintroducingaself-evolvingandself-adaptivemechanismthatbetterbalancesexplorationandexploitation. Unlikepriormethods,PWutilizesafeedback-drivencritique-and-synthesis
process,whichiterativelyrefinesbothpromptinstructionsandin-contextexamples. Thisfeedback
loop,guidedbyperformanceinsights,leadstomoresystematicandefficientexplorationcomparedto
randomormutation-basedstrategieslikethoseemployedbyPromptBreederandEvoPrompt. Key
advantagesofPWinclude: (i)DeeperExploitationofTaskNuances: Byoptimizingpromptsand
examples together, PW can capture the nuanced requirements of complex tasks that continuous
anddiscretemethodsoftenmiss,(ii)Human-InterpretableandScalable: Unlikesoftprompts,PW
3

<!-- Page 4 -->

Thinking SEQUENTIAL OPTIMIZATION OF INSTRUCTION AND EXAMPLES
Styles Training ITERATIVE Negative Examples Synthesized Examples

### How can I simplify Examples

the problem ? Mini Batch of OPTIMIZATION OF Critique /
Problem K Examples INSTRUCTION Feedback

### Description

Critique Synthesize

### Top Prompts Score

Prompt Instruction Mutate In N s t M ru u c ta ti t o e n d s Score T A h n i a n l k y s o e f a th n i s a p p r p o r b o l a e c m h . . . . . . . . 0 0 .7 .8 5 Critique /
Solve the given problem.. 0.6 Feedback

### Improved Critique /

Prompt Feedback Lets approach this logically 0.85 Synthesize Critique
Instruction Lets think step by step .... 0.4 Optimized Modified Instruction

### Synthesize Critique Instruction

Figure3: IterativeOptimizationofPromptInstruction. Figure4: SequentialOptimization.
generates human-readable prompts that align with task intent, making it more interpretable and
easiertoscaleacrossdiverseapplications,(iii)Efficiency: PWissignificantlycost-efficient,reducing
thenumberofAPIcallsandtokenusagewhiledeliveringsuperiorperformance. Evaluatedacross
over45complextasks,PWconsistentlyoutperformsstate-of-the-artapproaches,suchasInstinct,
InstructZero,APE,EvoPromptandPromptBreeder.
In summary, PW advances prompting by addressing the exploration-exploitation trade-off more
effectivelythanpriorapproaches,deliveringhigher-qualitypromptswithlesscomputationaloverhead.

## 3 Promptwizard Framework

WeintroducePromptWizard(PW),ageneral-purposeframeworkdesignedtooptimizeprompts
throughaself-evolvingandself-adaptingmechanism(seeFigure1). PWharnessesthecapabilitiesof
LLMstoiterativelysynthesize,critique,andrefinebothpromptinstructionsandin-contextexamples,
tailoringthemtospecifictasksacrossdiversedomains. Thefivekeystepsaredescribednext.
ProblemFormulation. Inourapproach,westartwithaninitialpromptinstructionP e.g.,“Let’s
thinkstepbysteptoarriveatthesolutionofthismathematicalproblem"), alongwithaproblem
descriptionandasetoftrainingsamplesrepresentedas(Q,A)={(q ,a )}N ,whereq anda are
i i i=1 i i
input-outputpairs(questionsandanswers). TheLLMmodelLgeneratesoutputswithprobabilities
p (a | q ,P,a ,q ), whereq anda arethefew-shotexamples. ThegoalofPromptWizard
l i i f f f f
istoiterativelyoptimizeboththepromptandthefew-shotexamplestomaximizetaskaccuracyA,
whichrepresentsthemodel’sperformanceonthetargettask. TherefinedpromptPˆ shouldimprove
themodel’sabilitytogenerateaccurateoutputs.

## 1 Iterativerefinementofpromptinstructions

ThefirststepofthePromptWizardframeworkfocusesonrefiningpromptinstructionsthrougha
systematic,feedback-drivenprocess. Thisensuresthepromptevolvesinatargetedway,addressing
specifictaskneedswhileavoidingunnecessarychanges(seeFigure3).

## MutateComponent: PW starts with an initial problem description and generates prompt

variationsusingpredefinedcognitiveheuristicsorthinkingstyles. TheseheuristicsguidetheLLM
tocreatediverseperspectivesontheproblem,ensuringvariedandrichpromptinstructions. For
example,thethinkingstylesmightencouragequestionslike"HowcanIsimplifytheproblem?"or
"Whatalternativeperspectivesexist?"Thistargetedgenerationofmutationsimprovesthediversity
ofpromptinstructionscomparedtorandomapproaches. ByusingasingleLLMcalltogenerate
several mutated prompts, PW ensures computational efficiency. Figure 5 shows examples of
mutatedpromptsforaninitialproblemdescriptionontheGSM8K.

## ScoringComponent: Next,PWemploysascoringmechanismtoevaluatetheperformanceof

thegeneratedmutatedprompts. Thescoringisbasedonhowwelleachpromptperformsagainst
a mini-batch of 5 training examples with ground truth. The scoring mechanism can be either
usingtraditionalmetricslikeF1scoreoranLLMasanevaluator,PWsupportsboth. Thishelps
systematicallyidentifythemosteffectivepromptwhilefilteringoutunderperformingones. The
useofmultiplemini-batchesensuresrobustnessintheevaluation. Examplesofmutatedprompts
withtheirscoresareshowninFigure3and5.

## CritiqueComponent: Oncethebest-performingmutatedpromptisselected,PWintroduces

auniquefeedbackmechanismthroughitscritiquecomponent. Thecritiquereviewswherethe
promptsucceededandfailedbyanalyzingcaseswheretheLLMstruggled,suchasinterpreting
4

<!-- Page 5 -->


## Examples:

TOP 3 MUTATED PROMPTS : [Question]: Albert is wondering how much pizza he can eat in one day. He buys 2
large pizzas and 2 small pizzas. A large pizza has 16 slices and a small pizza has 8
" Let's devise a step-by-step experiment to reach the solution of this mathematical problem." slices. If he eats it all, how many pieces does he eat that day?
" Let's simplify and tackle this mathematical problem step by step to make it easier to solve. " [Answer]: He eats 32 from the largest pizzas because 2 x 16 = <<2*16=32>>32. He
" Let's list out ideas and apply them one by one, thinking step by step, to solve mathematical e b a e t c s a u 1 s 6 e f 3 r 2 o m + 1 th 6 e = s < m <3 a 2 ll + p 1 i 6 zz = a 4 8 b > e > c 4 a 8 u . s T e h e 2 a x n s 8 w e = r i < s < 4 2 8 * . 8=16>>16. He eats 48 pieces
problems. "

## Critique/Feedback :

TOP SCORED PROMPT: This example is simple and straightforward, involving basic multiplication and addition.
It's relevant and relatable to students. However, it could be improved by adding a bit
"Provide question answering on mathematical school grade questions that require multi-step more complexity, such as introducing fractions or percentages.\n\n
reasoning. The problems should take between 2 and 8 steps to solve, and solutions

## Synthetic Examples:

primarily involve performing a sequence of elementary calculations using basic arithmetic [Question]: Albert buys a pizza that is cut into 8 slices. He eats 3 slices and gives 2
operations (+ - / *) to reach the final answer.\nLets think step by step to arrive at the solution slices to his friend. He then buys another pizza that is cut into 12 slices and eats half of
of this mathematical problem", i [ t A . n H s o w w e m r] a : n F y r o s m lic e th s e o f f i p rs iz t z p a iz d z o a e , s A A lb l e b r e t r t h h a a s v 8 e - le 3 ft ? - 2 = <<8-3-2=3>>3 slices left. From
the second pizza, Albert eats 12 / 2 = <<12/2=6>>6 slices, so he has 12 - 6 = <<12-
CRITIQUE/FEEDBACK : 6=6>>6 slices left.\nIn total, Albert has 3 + 6 = <<3+6=9>>9 slices of pizza left. The
Firstly, the instruction doesn't specify the need for the agent to understand the problem answer is 9.
context, such as interpreting relationships. Secondly, the instruction lacks clarity on the
agent's ability to handle percentages and real-world scenarios. Understanding sequences of Figure6: SyntheticExampleGeneration.
actions and their impact are crucial. Lastly, the instruction doesn't mention the agent's ability
to handle time conversions, such as converting an hourly rate to a per-minute rate.

## Expert Identity :

You are a mathematics educator with a deep understanding of elementary and middle
REFINED PROMPT: school mathematics. You are experienced in teaching multi-step problem-solving
techniques and have a knack for breaking down complex problems into manageable
Provide question answering on mathematical school grade problems that require multi-step steps. Your expertise lies in basic arithmetic operations such as addition, subtraction,
reasoning and understanding of the problem's context. The problems should take between 2 multiplication, and division. You can provide clear, step-by-step solutions to
mathematical problems that require multi-step reasoning. You are patient and thorough,
and 8 steps to solve, and solutions primarily involve performing a sequence of elementary ensuring that each step is clearly explained and understood. Your ability to simplify
calculations using basic arithmetic operations (+ - / *), handling percentages, and converting complex problems and guide students through the problem-solving process makes you
an excellent resource for answering school-grade mathematical questions.
them into numbers. The agent should be able to interpret real-world scenarios and
understand the implications of the problem, including handling time conversions. The agent INTENT :M Op a e th r e a m tio a n t s ic , a D l a R t e a a A s n o a n l i y n s g i , s , M S u o lt l i u -s ti t o e n p V P e r r o if b ic le a m tio S n olving, Basic Arithmetic
should also be able to follow a sequence of actions and their impact on the final answer. Let's
think step by step to arrive at the solution of this mathematical problem.
Figure7: TaskIntentandExpertPersona.
Figure5: IterativePromptRefinement.
relationshipsortimeconversionsinGSM8kexample. Thistargetedfeedbackiscriticalinrefining
theprompt,asitprovidesinsightsintospecificweaknesses,allowingforfocusedimprovements
ratherthangeneralchanges. ExampleofcritiquefeedbackonthemutatedpromptareinFigure5.

## SynthesizeComponent: Finally,PWsynthesizecomponentusesthecritique’sfeedbackto

refinethebestprompt. Itrephrasesandenhancestheinstructionbasedonthecritique,producing
a more task-specific and optimized prompt. For example, the feedback indicated issues with
interpretingspecificrelationships,thesynthesizedpromptwouldaddressthatdirectly,leadingtoa
clearer,moreeffectiveinstruction(seeFigure5).
Bycombiningthesesteps—mutation,scoring,critique,andsynthesis—PWensuresthattheprompts
arenotonlydiverseandcreativebutalsohighlytailoredtothespecifictaskathand,outperforming
priormethodsthatlackthisguidedrefinementprocess.

## 2 Identificationofdiverseexamples

Next,wefocusonidentifyingadiversesetofcandidateexamplestoenhanceprompteffectiveness.
Thechoiceofexamplesiscritical,asdiverserepresentationsallowLLMstobettergraspvarious
aspectsoftheinformationpresented(Rubinetal.,2022;Zhangetal.,2022b;Liuetal.,2022;Chen
etal.,2024). Webeginbyextractingcandidateexamplesfromthedatasetandemployascoring
mechanismtoassessthecurrentprompt’seffectivenessagainsttheseexamples,classifyingtheminto
positiveandnegativecategories. Positiveexamplesdemonstratewherethepromptsucceeds,while
negativeexampleshighlightareasforimprovement. Werandomlyselect25examplesanditerate
throughthemtofindatargetednumberofeffectivefew-shotexamples,typicallytakingfiveiterations.
Ifthisprocessdoesnotyieldthedesiredcount,werandomlyselectfiveexamplesfromtheinitial25.
Thistargetedapproachmaximizesefficiencybyminimizingtheneedtoevaluatetheentiredataset,
ensuringthatthechosenexampleseffectivelycontributetorefiningtheprompt. Theuseofboth
positiveandnegativeexamplesallowsforcomprehensiveunderstandingandrefinementofprompts.

## 3 Sequentialoptimizationofpromptinstructionsandfew-Shotexamples

Mostexistingpromptoptimizationmethodsfocusoneitherpromptinstructionsorfew-shotexamples.
Incontrast,PromptWizard(PW)employsasequentialoptimizationapproachthatintegratesboth,
enhancingtaskperformancebyoptimizingthemintandem.
Few-shot example optimization follows critique-and-synthesis process: (i)
CritiqueComponent: PW analyzes previously selected examples, utilizing critique to
providedetailedfeedback. Thisfeedbackisbasedonerror-drivenself-reflection,thatdetermineshow
examplesshouldevolvetobemorediverseandtask-relevant. (ii)SynthesizeComponent: This
incorporatesfeedbackfromtheCritiquetogeneratenewsyntheticexamplesthataremorediverse,
robust,andtask-relevant. Figure6demonstratesthecritique’sfeedbackonaexamplealongsidethe
newlygeneratedsyntheticexamples.
5

<!-- Page 6 -->

Prompt optimization follows critique-and-synthesis process: (i) CritiqueComponent:
The newly generated synthetic examples are evaluated alongside the current prompt. The
CritiqueComponent identifies weaknesses and gaps that require addressing to further refine
thepromptinstruction. (ii)SynthesizeComponent: Thisleveragesfeedbackfromthecritique
tosynthesizeandrefinethepromptinstruction. Thisiterativefeedbackloopfacilitatescontinuous
refinementofboththepromptandthesyntheticfew-shotexamples,ensuringtheyremainaligned
withtask-specificnuances.

## 4 Self-Generatedreasoningandvalidation

Withtheoptimizedpromptandfew-shotexamples,wefurtherenhancemodelperformancebyincorporating chain-of-thought(CoT) reasoning. Building onthe hypothesis that reasoning chains
improve problem-solving abilities of the model (Wei et al., 2023; Wang et al., 2023a; Ye et al.,
2023). Specifically,weautomaticallygenerateadetailedreasoningchainforeachselectedfew-shot
examples. (i)ReasoningComponent: Thistakestheselectedfew-shotexamplesandgeneratesa
detailedreasoningchainforeachexampletofacilitateproblem-solving.(ii)ValidateComponent:
ThevalidationcomponentusesanLLMtocheckthecoherenceandrelevanceofexamples(questions,reasoning). Thisprocesseffectivelyfiltersoutincorrectexamplesand/orhallucinatedreasoning.

## 5 Integrationoftaskintentandexpertpersona

Toenhancetaskperformance,PWintegratestaskintentandanexpertpersonaintoprompts(Figure7).
(i)Task Intent: Thisensuresthatthemodelstaysalignedwithtaskrequirements,particularly
in specialized domains. By incorporating specific hints or keywords (Sun et al., 2023), derived
from the problem description, PW guides the model to apply relevant approaches. We generate
thesecuesusingSynthesizeComponent,informedbyinitialproblemdescription. (ii)Expert
Persona: TomaintainconsistencyandrelevanceinLLMinteractions,weincorporateanexpert
personaintoprompts(Xuetal.,2023). Tomaintainconsistency,PWintroducesanexpertpersona,
preventing response variability. This persona is generated based on the problem description and
ensuresconsistent,domain-relevantoutputs. AllPWcomponentsutilizeLLMs,withtheirprompt
templatesprovidedinAppendix16andalgorithmicdetailsinAppendix14.

## 4 Experiments And Implementation Details

WeevaluatePromptWizardasatooltogenerateinstructionsandexamplesthatsteerablack-box
LLMtowarddesiredbehaviorforagiventargettask.
Tasks&Datasets. WeassesstheeffectivenessofPromptWizardonthewidely-usedBIG-Bench
InstructionInduction(BBII)dataset,abenchmarkforpromptoptimizationinrecentworkssuchas
Instinct(Linetal.,2024),InstructZero(Chenetal.,2023),andAPE(Zhouetal.,2023). Thedataset
coversadiverserangeoflanguageunderstandingscenarios(Appendix8).
In addition to BBII, we evaluate PromptWizard on three arithmetic reasoning datasets:
GSM8k(Cobbe et al., 2021), AQUARAT (Ling et al., 2017), and SVAMP (Patel et al., 2021),
aswellasdomain-specifictasksfromBigBenchHard(BBH)(Suzgunetal.,2022),whichincludes
23challengingtasks. Thisbringsthetotalto45tasks(19BBII,23BBH,3mathtasks),coveringboth
generalanddomain-specificproblemsettings. AdditionaldetailsofalldatasetsareinAppendix9.
Baselines. We compare our PromptWizard with five representative SOTA discrete and continuous methods: Instinct (Lin et al., 2024), InstructZero (Chen et al., 2023), PromptBreeder
(PB)(Fernandoetal.,2023),EvoPrompt(Guoetal.,2024),andAPE(Zhouetal.,2023).
ImplementationDetails. WeexperimentwithbothChatGPT(GPT3.5Turbo)andGPT-4asthe
black-boxLLMsforpromptoptimizationinPromptWizard.Alltheindividualcomponentssuchas
mutate,score,critique,reason,synthesizeandvalidate,relyonthesameLLMeitherGPT3.5Turbo
or GPT-4, accordingly. For all experiments, we use only 25 examples from the training data to
optimizethepromptsandin-contextexamples,withevaluationsconductedonthefulltestdataset.
Toensurerobustness,allreportedresultsareaveragedoverthreeexperimentalruns. Detailsofthe
hyperparametersusedinthepaperareprovidedinAppendix10. Specifically,werestrictthenumber
ofmutatedprompts&mutationroundsto3,diverseexamplesto25,sequentialoptimizationrounds
to5. ThesourcecodeofPromptWizardisavailableforreproducibility.
6

<!-- Page 7 -->

Table1: AveragetestaccuracyachievedbybestinstructiongeneratedbydifferentSOTAalgorithms.
InsZero: InstructZero,PB:PromptBreeder,EvoP:EvoPrompt,PW:PromptWizard(ours).
Task APE InsZero PB EvoP Instinct PW Instinct PW
LLM:GPT3.5Turbo Zero-shotsetting One-shotsetting
antonyms 0.64 0.83 0.80 0.80 0.85 0.56 0.85 0.78
auto-categorization 0.25 0.26 0.22 0.26 0.25 0.28 0.30 0.40
causeandeffect 0.57 0.81 0.75 0.83 0.59 0.88 0.63 0.92
commonconcept 0.07 0.09 0.10 0.12 0.21 0.10 0.25 0.19
diff 0.67 0.69 1.00 1.00 1.00 1.00 1.00 1.00
informaltoformal 0.57 0.53 0.58 0.62 0.55 0.62 0.52 0.56
letterslist 1.00 0.59 0.99 1.00 1.00 0.95 1.00 1.00
negation 0.75 0.78 0.77 0.79 0.82 0.73 0.86 0.84
objectcounting 0.36 0.36 0.34 0.12 0.34 0.60 0.36 0.52
oddoneout 0.63 0.61 0.64 0.65 0.70 0.78 0.63 0.92
orthographystartswith 0.46 0.51 0.56 0.60 0.67 0.75 0.67 0.92
rhymes 0.16 1.00 0.54 0.61 1.00 0.89 0.75 0.90
secondwordletter 0.75 0.43 0.57 0.41 0.10 0.93 0.24 0.99
sentencesimilarity 0.00 0.00 0.01 0.28 0.14 0.29 0.16 0.30
sum 0.67 1.00 1.00 1.00 1.00 1.00 1.00 1.00
synonyms 0.36 0.28 0.36 0.14 0.31 0.37 0.37 0.44
taxonomyanimal 0.35 0.72 0.72 0.72 0.86 0.92 0.90 0.94
wordsorting 0.33 0.31 0.56 0.52 0.51 0.56 0.62 0.74
wordunscrambling 0.44 0.55 0.61 0.60 0.63 0.52 0.58 0.58
# bestperformingtasks 1 2 3 4 8 13 7 16

## 5 Experimental Results And Analysis


## 1 Performanceanalysisagainstvariouspromptingbaselines

Zero-shotaccuracy. Weevaluatethezero-shottestaccuracyofChatGPT(GPT3.5Turbo)using
instructionsgeneratedbyfivemethods: APE,InstructZero,PromptBreeder,EvoPrompt,andInstinct.
Table1presentsresultson19challengingtasksfromBIG-BenchInstructionInduction(BBII)dataset,
selectedwheretheaveragetestaccuracyacrossallmethodsisbelow0.8,followingtheevaluationprotocolinInstinct(Linetal.,2024). Allexperimentsusethesameblack-boxLLM(GPT3.5Turbo)
underazero-shotsetting,ensuringafairandconsistentcomparisonacrossmethods.
PromptWizard outperforms the baselines, achieving the highest accuracy on 13 out of 19
tasks (68%), compared to Instinct’s 8 tasks (42%). This significant improvement demonstrates
PromptWizard’sstrengthintacklingcomplexinstructioninductiontasks.
OverallPerformance. Figure2showstheperformanceprofilecurvefortheinstructioninduction
tasksfromTable1. Theperformanceprofilecurve(Dolan&Moré,2002)visualizeshowfrequently
differentapproaches’performanceiswithinagivendistanceofthebestperformance. Inthiscurve,
thex-axis(τ)representstheperformanceratiorelativetothebest-performingmethod,andthey-axis
(p(τ))reflectsthefractionoftaskswhereamethod’sperformanceiswithinthisratio. Soforagiven
method,thecurvetellswhatpercentageofthetasksarewithinτ distancetothebestperformance
(amongdifferentmethods). PromptWizardconsistentlyoutperformsothermethodsacrossvarious
thresholds,maintainingthehighestp(τ)values,indicatingthatitconsistentlyperformsnearthebest
possibleaccuracyacrossalltasks. AdditionalanalysisisavailableinAppendix11.
One-shot Accuracy. To evaluate the effectiveness of PW’s in-context example generation, we
compare the one-shot test accuracy of ChatGPT (GPT3.5Turbo) when using instructions generated by Instinct and PW. The results, presented in the last two columns of Table 1, show that
PromptWizardachievesthehighestaccuracyon16outof19tasks(84%),whileInstinctperforms
bestononly7outof19tasks(36%). Thisimprovementislargelyattributedtotherobustin-context
learningexamplesgeneratedbyPW,combinedwithitsiterativepromptinstructionoptimization. By
refiningboththepromptinstructionsandexamplesthroughmultipleiterations,PWensuresthatthe
task-specificknowledgeiseffectivelycaptured. TheoptimalpromptsareinAppendix15.
GPT-4 as Base model. Table 1 presents results using GPT3.5Turbo as the base model. In
additionalexperimentswithGPT-4asthebasemodelonBBII,PWachievedthehighestaccuracyin
15outof19tasks(79%),comparedtoInstinct’s6outof19(31%),demonstratingPW’ssuperior
performanceevenwithachangeinbasemodels(Appendix12Table12hasthedetailedresults).
Arithmetic Datasets. Table 2 compares performance of PW with Instinct and InstructZero on
threearithmeticreasoningtasks: GSM8k,AQUARAT,andSVAMP,allusingGPT3.5Turboin
a zero-shot setting. The results clearly show that PromptWizard consistently outperforms all
7

<!-- Page 8 -->

Table3: Perf. onBBH. Table4: Costanalysis.
Table2: Perf. onarithmetictasks.

### API IO Total Cost

Dataset BBH(23) calls Tokens tokens ($)

### Dataset GSM8k AQUARAT SVAMP

Approach Zero-shotwithGPT3.5Turbo Approach Accuracy Instinct 1730 67 115910 0.23

### InsZero 74.2 54.3 79.5 APE 71.85 InsZero

Instinct 74.5 54.7 81 EvoP 75.03 PB 18600 80 1488000 2.9
PW 90 58.2 82.3 PW 88.1 EvoP 5000 80 400000 0.8

## Pw 69 362 24978 0.05

baselinesacrossthesedatasets,achievingsignificantgainsinaccuracyonarithmeticreasoningtasks.
Thesetasks,oftenrequiringdetailedmulti-stepreasoning,whichPWaddressesthroughitsiterative
synthesisofpromptsenrichedwithintermediatereasoningstepsandexamples.
Comparison with BBH tasks. In Table 3, we report the average accuracy across 23 tasks from
theBIG-BenchHard(BBH)dataset. Duetothehighcostandcomputerequirementsinvolvedin
evaluatingallbaselinesonthisextensivesetoftasks,welimitthecomparisontoEvoPromptandAPE.
PromptWizardachievesaremarkableimprovement,increasingtheaverageaccuracybyover13%
comparedtoEvoPromptandAPE,underscoringitseffectivenessinhandlingcomplextasks.

## 2 Costanalysisagainstvariouspromptingbaselines

Whilehighaccuracyiscrucial,theefficiencyofgeneratingpromptsisequallyimportant. Wepresent
a detailed cost analysis demonstrating that PW not only outperforms baselines in terms of task
accuracybutdoessowithminimalcomputationaloverhead. Weconductacomprehensiveevaluation
bycomputingthetotalnumberofAPIcalls,tokensprocessed,andthecorrespondingcost(Table4).
InstinctandInstructZero. InstinctandInstructZerouseamixofwhite-boxandblack-boxmodels
tocontinuouslyoptimizesoftprompts,withthenumberofAPIcallslinkedtotheiterativeprocess
needed for convergence. According to their respective papers, the best performance is typically
achievedafteramaximumof165iterations. Onaverage,acrossalltasks,weobserved1,730API
callstotheblack-boxmodelpertask,withapproximately67inputandoutput(IO)tokenspercall
for the BBII dataset. Given the token billing structure of the GPT3.5Turbo API ($0.002 per
1,000tokens),thetotalcostpertaskisestimatedtobearound$0.23. DetailedAPIcallandtoken
breakdownspertaskareprovidedinAppendix13.2.
PromptBreeder (PB). PromptBreeder (PB) uses a discrete optimization approach through selfreferentialimprovement,evolvingpromptsover20–30generationswithapopulationsizeof20. This
resultsinsignificantAPIusage,withanestimated18,600APIcallspertask(30generations×(20
mutations+20×30evaluations))(Fernandoetal.,2023). Withanaverageof80input/outputtokens
percall,thetotalcostpertaskfortheBBIIdatasetisapproximately$2.9,makingPBoneofthemost
expensivemethodsamongthebaselines.
EvoPrompt. EvoPrompt, a discrete optimization method, uses evolutionary algorithms to find
optimalprompts. ThenumberofAPIcallsfollowstheformula: APIcalls=N(populationsize)×T
(iterations)×(1+D(developmentsize)). ForBBIItasks,withapopulationsizeof10,10iterations,
andadevelopmentsetsizeof50,thisresultsin: APIcalls=10×10×(1+50)=5,000APIcalls. With
anaverageof80input/outputtokenspercall,EvoPromptincursatotalcostof$0.8pertask,which
islowerthanPBbutstillconsiderablecomparedtoothermethods.
PromptWizard(PW).PWemploysadiscreteoptimization,similartoPBandEvoPrompt,but
introduceskeycomponents-feedback-drivenguidedexploration,critiqueandsynthesisprocess,and
sequentialoptimizationofinstructionandexamples-thatstreamlinepromptexplorationandfocuson
meaningfulevolution. Theseinnovationsreduceunnecessarymutations,strikinganeffectivebalance
betweenexplorationandexploitation. TheAPIcallsinPWarebrokendowninto48forprompt
refinement,5forexampleselection,12forsequentialoptimizations,and4forreasoning,validation,
intentrefinement,andexpertidentity(Algo.1). Thistotals69APIcalls,substantiallyfewerthan
PB’s18,600andEvoPrompt’s5,000. Theaverageinput/outputtokenspertaskisaround360,slightly
higherduetotheadditionofCOTreasoningandexpertidentityduringpromptoptimization. Despite
this,PromptWizardcostsjust$0.05pertaskwith5-60xreductioninoveralltokens,significantly
lowerthanothertechniques. Notethat,duringinference,PW’saverageinputtokensare∼200,which
iscomparabletootherapproaches. Appendix13.2showsthedetailedtasklevelcomputations.
PromptWizard’s efficiency is highlighted by being 5x cheaper than continuous methods like
InstinctandInstructZero,and16-60xcheapercomparedtodiscretemethodslikeEvoPromptand
PromptBreeder,whileachievingsuperiorperformance.
8

<!-- Page 9 -->

Datasets 5(eg) 25(eg) Datasets Ll-70B GPT-4 Models WithPW w/oPW
MMLU 80.4 89.5 GSM8k 94.6 95.4 GPT-4 95.4 92

### GSM8k 94.0 95.4

Ethos 89.2 89.4 GPT3.5 75.6 57.1

### Ethos 86.4 89.4

Average 91.9 92.4 Ll-70B 90.2 56.8
PubMedQA 68.0 78.2

### MedQA 80.4 82.9

Table 6: Perf. with smaller Table 7: Perf. with different

### Average 81.9 87.0

LLM for prompt generation. Base LLMs on GSM8k. Ll-
Table5: Perf. with5examples.
Ll-70B:Llama-70B 70B:Llama-70B

## 6 Promptwizard Ablation Study


## 1 Promptwizardefficacywithfewertrainingexamples

PromptWizardassessesprompteffectivenessusingavailabletrainingexampleswhilealsosynthesizingnewfew-shotexamples. Inreal-worldscenarios,wheredatamaybescarceortasksevolve
withoutcurateddatasets,generatingeffectivepromptswithminimalexamplesbecomesessential. To
evaluatePromptWizard’sperformanceunderdata-constrainedconditions,wesimulateafew-shot
learningscenariobyrandomlyselectingonly5examplesfromeachdatasetasthetrainingset(instead
of 25). PW utilizes these examples for all evaluations, critique feedback, and the generation of
diversesyntheticexamples. Thissetupteststheframework’sabilitytogeneralizeandcreaterobust,
task-relevantpromptswithminimaldata.
Table5showcasesPromptWizard’sperformanceacrossfivediversedatasets(seeAppendix9)
whentrainedwithonly5examples(5eg)comparedto25examples(25eg). Despitethedrastic
reductionintrainingdata,PromptWizarddemonstratesimpressiveresilience,exhibitingonlya
marginal5%dropinaccuracyonaverage. Thisresilienceunderscoresthemodel’sadaptability,
drivenbytwokeymechanisms: (i)SyntheticExampleGenerationusingcritique-and-synthesize,
which produces diverse, high-quality examples from limited inputs, reducing the impact of data
scarcity;and(ii)ReasoningChainGuidance,wherestructuredreasoningchainsenhancetheLLM’s
abilitytogenerateaccurate,contextuallyrelevantresponses.

## 2 Promptwizardwithsmallerllmsforpromptoptimization

Inpriorexperiments,GPT3.5Turbowasusedforbothpromptgenerationandoptimization. Inthis
section,weexplorethefeasibilityofemployingasmallerLLM,suchasLlama-70B,forprompt
generationwhilereservingamorecapablemodellikeGPT-4forinference. Thisapproachreduce
computational costs during prompt optimization by leveraging the efficiency of smaller models
whilestillmaximizingtaskaccuracywithpowerfulmodelduringinference. Thisstrategyoffers
twokeyadvantages: (i)ComputationalEfficiency: SmallerLLMslikeLlama-70Brequirefewer
resources,makingthemidealforgeneratingpromptsinresource-constrainedenvironments. (ii)Task
Performance: Despiteusingasmallermodelforpromptgeneration,inferencebenefitsfromthelarger
GPT-4model’sabilitytointerpretandexecutetheoptimizedprompt,ensuringminimaldegradation.
Table 6 compares task accuracy across multiple datasets when Llama-70B is used for prompt
generationversusthedefaultGPT-4. Impressively,thefinalpromptsgeneratedbyPromptWizard
using Llama-70B show a negligible <1% drop in accuracy compared to those generated with
GPT-4, highlighting PromptWizard ’s effectiveness even with smaller models. While we experimentedwithsmallermodelslikeLlama-3-8B,theystruggledtogeneratecomplexinstructions,
leadingtosignificantperformancedegradation. Thus,mid-sizedLLMslikeLlama-70Barerecommendedforpromptoptimization,strikingabalancebetweencomputationalefficiencyandtask
performance. ThesefindingsdemonstratePromptWizard’sadaptabilityanditsabilitytomaintain
highperformanceacrossdifferentmodelsizeswithminimalloss.

## 3 Assessingperformancewithdifferentbasellms

Weperformtwotypesofablationanalysis: (i)evaluatingtheeffectofdifferentbaseLLMsduring
promptoptimizationandinference,and(ii)measuringthecontributionofeachcomponentwithinthe
PromptWizardframeworktooverallperformance.
AblationonDifferentBaseLLMs. ToassessPromptWizard’sadaptabilityandefficacyacross
variousLLMs,weexperimentwiththreesettings: usingGPT-4,GPT3.5Turbo,andLlama-70B
as both the base LLM for prompt optimization and during inference. The goal is to understand
whetherthechoiceofbasemodelimpactstheperformancegainsachievedthroughPromptWizard.
9

<!-- Page 10 -->

Table 7 summarizes the results for the GSM8k dataset. In case of without PW, we use few-shot
learningwithChain-of-Thought(COT)prompting(Touvronetal.,2023)asthebaseline. Weobserve
substantialperformanceimprovementsacrossallmodelswhenoptimizedpromptsaregeneratedby
PW.Specifically,forGPT3.5Turbo,thetaskaccuracyincreasesby+18%,whileforLlama-70B,
theimprovementisevenmorepronounced,reaching+33%. Incontrast,modelswhennotusingPW
promptshowsignificantperformancedegradation,reaffirmingthevalueofpromptoptimization.

### Effectiveness of different stages of PromptWizard. We

conductedanablationstudytoassessthecontributionofeach GSM8k Ethos
stageinthePWpipeline,usingtheGSM8kandEthosdatasets. All 95.4 89.4

### NoMutationandScoring 95.2 87.1


### NoCritiqueandSynthesize 90.9 86.9

Table8presentstheresultsofthisablationstudy: (i)Mutation

### Nointent&Expert 95 88.7

andScoring: Theinitialstageofiterativepromptrefinement NoReasoning 45.9 87.6
alone yields an accuracy boost of 1-2%, demonstrating the

### Table8: AbaltionStudy

baseline value of exploring prompt variations. (ii) Critique

### FeedbackandRefinement: Addingstructuredfeedbackviathe

critiquemechanismimprovesaccuracyby3-5 highlightingtheimpactoftargetedrefinementon
promptquality. (iii)TaskIntentandExpertPersonaModeling: Tailoringpromptstotask-specific
nuancescontributesanadditional0.5-1%improvement. Althoughsmaller,thisstepplaysacrucial
roleinaligningthepromptwithtask-specificbehavior. (iv)ReasoningonFew-shotExamples: This
emergesasoneofthemostsignificantcontributors,indicatingthatgeneratingdetailedreasoning
chains for few-shot examples is critical for task accuracy. This ablation study underscores the
significance of individual components within the PromptWizard, as they work collectively to
enhancepromptandmodelperformance.

## 7 Conclusions

ThisworkintroducesPromptWizard,ageneral-purposeframeworkforautomatingpromptand
examplesynthesis. Bystrikingabalancebetweenexplorationandexploitationthroughafeedbackdrivencritiqueandsynthesisprocess,PWsystematicallyrefinespromptsandin-contextexamples
toenhancetaskperformance.Extensiveevaluationsacrossdiversedatasetsshowitconsistentlyoutperformsstate-of-the-artmethods,demonstratingstrongefficacyevenwithlimitedtrainingdataand
smallerLLMs,withonlyamarginaldropinaccuracy. Ablationstudieshighlighttheimportance
of each stage in refining prompts, generating diverse examples, and improving reasoning. Our
comprehensivecostanalysishighlightssignificantreductionsinAPIcalls,tokenusage,andoverall
expenses,showcasingPW’scost-effectiveness—itis5xcheaperthancontinuousoptimizationmethodsand16-60xcheaperthandiscretemethods,allwhiledeliveringsuperiorperformance. Thiswork
democratizesaccesstoeffectivepromptengineering,enablingmoreefficientandaccurateutilization
ofLLMsacrossvariousdomainsandapplications. Futureworkwillfocusonrefiningthevalidation
ofsyntheticexamplesandapplyingPWtoreal-world,resource-constrainedenvironments.
Limitations: Whilewehaveconductedextensiveexperimentsacrossadiversesetoftasks,careful
validationisrequiredfornewtaskstoensureadaptability. Promptresponsetestingisessentialbefore
real-worlddeploymenttoverifyeffectiveness. Additionally,whilePromptWizardautomatesprompt
engineering,humanexpertiseremainsindispensableinguidingandrefiningtheoptimizationprocess.
10

<!-- Page 11 -->


## References

LichangChen,JiuhaiChen,TomGoldstein,HengHuang,andTianyiZhou. Instructzero: Efficient
instructionoptimizationforblack-boxlargelanguagemodels,2023. URLhttps://arxiv.
org/abs/2306.03082.
Yanda Chen, Chen Zhao, Zhou Yu, Kathleen McKeown, and He He. On the relation between
sensitivityandaccuracyinin-contextlearning,2024.
Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian, Mark Chen, Heewoo Jun, Lukasz Kaiser,
MatthiasPlappert,JerryTworek,JacobHilton,ReiichiroNakano,ChristopherHesse,andJohn
Schulman. Trainingverifierstosolvemathwordproblems,2021.
PierreColombo,TelmoPessoaPires,MalikBoudiaf,DominicCulver,RuiMelo,CaioCorro,Andre
F.T.Martins,FabrizioEsposito,VeraLúciaRaposo,SofiaMorgado,andMichaelDesa. Saullm-7b:
Apioneeringlargelanguagemodelforlaw,2024.
MingkaiDeng,JianyuWang,Cheng-PingHsieh,YihanWang,HanGuo,TianminShu,MengSong,
Eric Xing, and Zhiting Hu. RLPrompt: Optimizing discrete text prompts with reinforcement
learning.InYoavGoldberg,ZornitsaKozareva,andYueZhang(eds.),Proceedingsofthe2022ConferenceonEmpiricalMethodsinNaturalLanguageProcessing,pp.3369–3391,AbuDhabi,United
ArabEmirates,December2022.AssociationforComputationalLinguistics. doi: 10.18653/v1/
2022.emnlp-main.222. URLhttps://aclanthology.org/2022.emnlp-main.222.
Xuan Long Do, Yiran Zhao, Hannah Brown, Yuxi Xie, James Xu Zhao, Nancy F. Chen, Kenji
Kawaguchi, Michael Shieh, and Junxian He. Prompt optimization via adversarial in-context
learning,2024. URLhttps://arxiv.org/abs/2312.02614.
ElizabethDDolanandJorgeJMoré. Benchmarkingoptimizationsoftwarewithperformanceprofiles.
Mathematicalprogramming,91:201–213,2002.
ChrisanthaFernando,DylanBanarse,HenrykMichalewski,SimonOsindero,andTimRocktäschel.
Promptbreeder: Self-referentialself-improvementviapromptevolution,2023.
QingyanGuo, RuiWang, JunliangGuo, BeiLi, KaitaoSong, XuTan, GuoqingLiu, JiangBian,
andYujiuYang. Connectinglargelanguagemodelswithevolutionaryalgorithmsyieldspowerful
promptoptimizers,2024.
XiaoqiangLin,ZhaoxuanWu,ZhongxiangDai,WenyangHu,YaoShu,See-KiongNg,PatrickJaillet,
andBryanKianHsiangLow. Useyourinstinct: Instructionoptimizationforllmsusingneural
banditscoupledwithtransformers,2024. URLhttps://arxiv.org/abs/2310.02905.
WangLing,DaniYogatama,ChrisDyer,andPhilBlunsom. Programinductionbyrationalegeneration: Learningtosolveandexplainalgebraicwordproblems. arXivpreprintarXiv:1705.04146,
2017.
JiachangLiu,DinghanShen,YizheZhang,BillDolan,LawrenceCarin,andWeizhuChen. What
makesgoodin-contextexamplesforGPT-3? InEnekoAgirre,MariannaApidianaki,andIvanVulic´
(eds.),ProceedingsofDeepLearningInsideOut(DeeLIO2022):The3rdWorkshoponKnowledge
ExtractionandIntegrationforDeepLearningArchitectures,pp.100–114,Dublin,Irelandand
Online,May2022.AssociationforComputationalLinguistics. doi: 10.18653/v1/2022.deelio-1.10.
URLhttps://aclanthology.org/2022.deelio-1.10.
XiaoLiu, YananZheng, ZhengxiaoDu, MingDing, YujieQian, ZhilinYang, andJieTang. Gpt
understands,too,2023.
AmanMadaanandAmirYazdanbakhsh. Textandpatterns: Foreffectivechainofthought,ittakes
twototango,2022.
MiladMoradiandMatthiasSamwald. Evaluatingtherobustnessofneurallanguagemodelstoinput
perturbations. In Marie-Francine Moens, Xuanjing Huang, Lucia Specia, and Scott Wen-tau
Yih (eds.), Proceedings of the 2021 Conference on Empirical Methods in Natural Language
Processing, pp. 1558–1570, Online and Punta Cana, Dominican Republic, November 2021.
AssociationforComputationalLinguistics.doi:10.18653/v1/2021.emnlp-main.117.URLhttps:
//aclanthology.org/2021.emnlp-main.117.
11

<!-- Page 12 -->

Ha-ThanhNguyen,RandyGoebel,FrancescaToni,KostasStathis,andKenSatoh. Howwelldosota
legalreasoningmodelssupportabductivereasoning?,2023.
HarshaNori,YinTatLee,ShengZhang,DeanCarignan,RichardEdgar,NicoloFusi,NicholasKing,
JonathanLarson,YuanzhiLi,WeishungLiu,RenqianLuo,ScottMayerMcKinney,RobertOsazuwa Ness, Hoifung Poon, Tao Qin, Naoto Usuyama, Chris White, and Eric Horvitz. Can
generalistfoundationmodelsoutcompetespecial-purposetuning? casestudyinmedicine,2023.
OpenAI,R,andotheret.al. Gpt-4technicalreport,2024.
ArkilPatel,SatwikBhattamishra,andNavinGoyal. Arenlpmodelsreallyabletosolvesimplemath
wordproblems? arXivpreprintarXiv:2103.07191,2021.
ReidPryzant,DanIter,JerryLi,YinTatLee,ChenguangZhu,andMichaelZeng. Automaticprompt
optimizationwith"gradientdescent"andbeamsearch,2023.
OhadRubin, JonathanHerzig, andJonathanBerant. Learningtoretrievepromptsforin-context
learning,2022.
HongSun,XueLi,YinchuanXu,YoukowHomma,QiCao,MinWu,JianJiao,andDenisCharles.
Autohint: Automaticpromptoptimizationwithhintgeneration,2023.
MiracSuzgun,NathanScales,NathanaelSchärli,SebastianGehrmann,YiTay,HyungWonChung,
Aakanksha Chowdhery, Quoc V. Le, Ed H. Chi, Denny Zhou, and Jason Wei. Challenging
big-benchtasksandwhetherchain-of-thoughtcansolvethem,2022.
HugoTouvron,ThibautLavril,GautierIzacard,XavierMartinet,Marie-AnneLachaux,Timothée
Lacroix,BaptisteRozière,NamanGoyal,EricHambro,FaisalAzhar,AurelienRodriguez,Armand
Joulin,EdouardGrave,andGuillaumeLample. Llama: Openandefficientfoundationlanguage
models,2023.
XingchenWan,RuoxiSun,HootanNakhost,andSercanO.Arik. Teachbetterorshowsmarter?
oninstructionsandexemplarsinautomaticpromptoptimization,2024. URLhttps://arxiv.
org/abs/2406.15708.
BoshiWang,SewonMin,XiangDeng,JiamingShen,YouWu,LukeZettlemoyer,andHuanSun.
Towardsunderstandingchain-of-thoughtprompting: Anempiricalstudyofwhatmatters,2023a.
LeiWang,WanyuXu,YihuaiLan,ZhiqiangHu,YunshiLan,RoyKa-WeiLee,andEe-PengLim.
Plan-and-solveprompting: Improvingzero-shotchain-of-thoughtreasoningbylargelanguage
models,2023b.
XuezhiWang,JasonWei,DaleSchuurmans,QuocLe,EdChi,SharanNarang,AakankshaChowdhery,andDennyZhou. Self-consistencyimproveschainofthoughtreasoninginlanguagemodels,
2023c.
JasonWei,MaartenBosma,VincentY.Zhao,KelvinGuu,AdamsWeiYu,BrianLester,NanDu,
AndrewM.Dai,andQuocV.Le. Finetunedlanguagemodelsarezero-shotlearners,2022.
JasonWei,XuezhiWang,DaleSchuurmans,MaartenBosma,BrianIchter,FeiXia,EdChi,QuocLe,
andDennyZhou. Chain-of-thoughtpromptingelicitsreasoninginlargelanguagemodels,2023.
BenfengXu,AnYang,JunyangLin,QuanWang,ChangZhou,YongdongZhang,andZhendong
Mao. Expertprompting: Instructinglargelanguagemodelstobedistinguishedexperts,2023.
ChengrunYang,XuezhiWang,YifengLu,HanxiaoLiu,QuocV.Le,DennyZhou,andXinyunChen.
Largelanguagemodelsasoptimizers,2024.
XiYe, SrinivasanIyer, AsliCelikyilmaz, VesStoyanov, GregDurrett, andRamakanthPasunuru.
Complementaryexplanationsforeffectivein-contextlearning,2023.
TianjunZhang,XuezhiWang,DennyZhou,DaleSchuurmans,andJosephE.Gonzalez. Tempera:
Test-timepromptingviareinforcementlearning,2022a.
12

<!-- Page 13 -->

Xinlu Zhang, Chenxin Tian, Xianjun Yang, Lichang Chen, Zekun Li, and Linda Ruth Petzold.
Alpacare:instruction-tunedlargelanguagemodelsformedicalapplication,2024.
YimingZhang,ShiFeng,andChenhaoTan. Activeexampleselectionforin-contextlearning. In
YoavGoldberg,ZornitsaKozareva,andYueZhang(eds.),Proceedingsofthe2022Conferenceon
EmpiricalMethodsinNaturalLanguageProcessing,pp.9134–9148,AbuDhabi,UnitedArab
Emirates,December2022b.AssociationforComputationalLinguistics. doi: 10.18653/v1/2022.
emnlp-main.622. URLhttps://aclanthology.org/2022.emnlp-main.622.
YongchaoZhou,AndreiIoanMuresanu,ZiwenHan,KeiranPaster,SilviuPitis,HarrisChan,and
JimmyBa. Largelanguagemodelsarehuman-levelpromptengineers,2023.

## Appendix


## 8 Big Bench Instruction Induction (Bbii) Dataset Details

Table9describesthenumeroustasksinBBIIdatasetalongwiththedescriptionofthetask. Thisis
apopulardatasetandtheselectedtaskscovermanyfacetsoflanguageunderstandingandincludes
allninesuchproblemsfromtheBigBench-HardSubset. Inparticular,itincludesemotionalunderstanding,context-freequestionanswering,readingcomprehension,summarization,algorithms,and
variousreasoningtasks(e.g.,arithmetic,commonsense,symbolic,andotherlogicalreasoningtasks).
Weselectedtasksforwhichthedatawaspubliclyavailable.
Table9: BigBenchInstructionInductionDataset

### Task Description

antonyms Makethepairsofwordsopposite.
autocategorization Createalistofthingsthattheinputcouldbeassociatedwith,andthe
outputwouldbethecategorythattheinputbelongsto
causeandeffect identifythesentencethatisthecauseoftheeffectintheinputsentence
pair
commonconcept ”involve”theobjectsmentionedintheinput, sotheanswerwouldbe
”involveoscillations”fortheinput”guitars,pendulums”
diff Findthedifferencebetweenthetwonumbers
informaltoformal converttheinputsentenceintoanoutputsentencethatisgrammatically
correctandidiomaticinEnglish
letterslist outputtheinputwithaspaceaftereachletter
negation maketheoutputfalsebyaddingtheword”not”totheinput
objectcounting outputthenumberofobjectsintheinputlist
oddoneout findthewordthatismostdissimilartotheothersinthegroup
orthographystartswith outputthewordthatstartswiththeletterthatwasinputted
rhymes outputthefirstwordthatappearedintheinputtext
secondwordletter takesastringasinputandreturnsthefirstcharacterthatisavowel.
sentencesimilarity Findthedifferencebetweenthetwosentencesandtheoutputwas4-
almostperfectly
sum addthenumbersofthetwoinputnumbers
synonyms createalistofwordsthatcouldbeusedinthesamewayastheoriginal
words
taxonomyanimal outputthenameofananimalthatstartswiththeletter
wordsorting sorttheinputwordsalphabetically
wordunscrambling outputthewordthatisformedbyrearrangingthelettersofthegiven
word
9 DATASET DETAILS: TRAIN/TEST SPLIT FOR DATASETS & FEW-SHOT COUNT
Belowarethedetailsofthedatasetsusedforevaluation.
13

<!-- Page 14 -->

Datasets Testdatasetsize Few-shotcount

### GSM8k 1319 5


## Aquarat 254 0


## Svamp 254 0


### Ethos 799 3

PubMedQA 500 5
MedQA 1273 5

## Csqa 1140 5


## Sqa 224 5

BBH[’snarks’,’penguinsinatable’,’causaljudgement’] 153,121,162 3
BBHallexcept[’snarks’,’penguinsinatable’,’causaljudgement’] 225 3
MMLU[clinicalknowledge,collegebiology,collegemedicine,anatomy,medicalgenetics,professionalmedicine] 65,144,173,135,100,272 5

### Table10: Train/Testsplitfordatasets&Few-shotcount

GSM8K: This dataset contains 8.5K high-quality, linguistically diverse grade school math word
problemscreatedbyhumanproblemwriters. Thefinalanswerisanintegervalue.
AQUARAT:Alarge-scaledatasetconsistingofapproximately100,000algebraicwordproblems. The
solutiontoeachquestionisexplainedstep-by-stepusingnaturallanguage. Thetestdataincludes254
questions.
SVAMP:SVAMP(SimpleVariationsonArithmeticMathwordProblems)datasetisaone-unknown
arithmeticwordproblemswithgradelevelupto4byapplyingsimplevariationsoverwordproblems
inanexistingdataset.
Ethos: ThishatespeechdetectiondatasetisbuiltfromYouTubeandRedditcomments. Itincludes
twotasks: binaryclassificationandmulti-labelclassification. Weevaluateourapproachonthebinary
classificationtask,whichconsistsof998questions. Thefinalansweriseither"yes"or"no."
MedQA:Thisdatasetincludesmultiple-choicequestionssimilartothoseintheMedicalLicensing
Examination. WeusetheEnglishsubsetwith11,450trainingand1,273testquestions,styledlikethe
UnitedStatesMedicalLicensingExam(USMLE).Thefinalansweristhecorrectoptionfromthe
availablechoices.
MMLU:MeasuringMassiveMultitaskLanguageUnderstanding(MMLU)includesmultiple-choice
exam questions from 57 domains. We use 6 medical datasets, viz., Clinical knowledge, Medical
genetics,Anatomy,ProfessionalMedicine,CollegeBiology,andCollegeMedicine.
BBH:BIG-BenchHard(BBH)includes23tasksfromdifferentdomains. Answerscanbeintheform
ofmultiple-choicequestions,boolean,orstringresponses.
Forallthedatasets,inPromptWizardwerandomlyselectonly25samplesfromavailabletraining
data. Wedonotuseentiretrainingdatasetintraining-phase. Testdatasetsizeforeachdatasetis
specifiedbelow. Howeverforthebaselineapproaches, wefollowtheirtrain/testsplits. Table10
providesdetailsofthetestsetalongwiththefew-shotsusedineachdataset.

## 10 Hyper Parameters

PWreliesonseveralparameterstocontrolthelevelofexplorationandevolutionateachstage. We
nowprovidecomprehensivedetailsofallparametersandassociatedvalues(seeTable11).

## 11 Performance Profile Curve - Additional Details

InSection5.1wepresentedthePerformanceProfileCurvecomparingPromptWizard’sperformanceagainstallbaselinesacrossalltasksinBBIIdataset.
TheperformanceprofilecurveDolan&Moré(2002)visualizeshowfrequentlydifferentapproaches’
performanceiswithinagivendistanceofthebestperformance. Inthiscurve,thex-axis(τ)represents
the performance ratio relative to the best-performing method, and the y-axis (p(τ)) reflects the
fractionoftaskswhereamethod’sperformanceiswithinthisratio. PromptWizardconsistently
14

<!-- Page 15 -->

Hyper- Description DefaultValue
parameter
mutate_refine Number of rounds of call to MutateComponent fol- 3
rounds lowedbyrefinementoverbestpromptamonggenerated
byMutateComponentinpreviousstep.
mutate_rounds NumberoftimesMutateComponentwouldbecalled. 3
style_variation NumberofvariationsMutateComponentgeneratesin 3
a single call. i.e. one variation corresponding to each
thinkingstyleprovided.
min_example Minimum number of questions the 3
correct_count ScoringComponent should answer correctly
foraprompttogetqualifiedfornextstage.
max_example Maximum number of attempts/questions the 6
count ScoringComponent would be asked asked to
answer.
max_seq_iter NumberofroundsofcalltoCritiqueComponentfol- 5
lowedbycalltoSynthesizeComponent
few_shot_count Total number of few shot examples to be provided in DefinedinTaprompt. ble10
ex_critique NumberofLLMcallsmadebyCritiqueComponent 1
forgettingcritiqueforimprovingexamplespassedasfewshots.
synthesize Number of LLM calls made by 1
SynthesizeComponent to generate synthetic
examples.
inst_critique NumberofLLMcallsmadebyCritiqueComponent 1
for getting critique for improving instruction passed as
few-shots.
synthesize Number of LLM calls made by 1
SynthesizeComponent to created improved
versionofinstruction.
reasoning + Number of LLM calls made 2
validation by ReasoningComponent and
ValidateComponentrespectively.
intent + per- NumberofLLMcallsmadetogetkeywordsthatexpress 2
sona theintentandtogenerateexpertpersonarespectively.

### Table11: Descriptionforhyperparametersandtheirdefaultvalues

outperformsothermethodsacrossvariousthresholds,maintainingthehighestp(τ)values,indicating
thatitconsistentlyperformsnearthebestpossibleaccuracyacrossalltasks.
Inthiscurve,thex-axis(τ)representstheperformanceratiorelativetothebest-performingmethod,
andthey-axis(p(τ))reflectsthefractionoftaskswhereamethod’sperformanceiswithinthisratio.
Itisasuitablemeasurefortheperformanceofmethodsoveralargenumberoftasks. Todrawthe
performanceprofilecurveforamethod,foreachtaski,wecheckwhethertheperformanceofthis
methodintaskiiswithinτ distancetothebestperformance(amongdifferentmethods)intaski,and
defineanindicatorfunctionI(). Next,weaveragethisindicatorfunctionacrossalln tasks,which
p
yieldsavaluep(τ)(equation1). Finally,theperformanceprofilecurveforthismethodisobtainedby
varyingthevalueofτ andcalculatingthecorrespondingp(τ).
(cid:80)np I(Bestperformanceoftaski−Performanceoftheapproachontaski≤τ)
ρ(τ)= i=1 (1)
n
p
Forexampleatτ =0.0,thevaluesofp(τ)areapproximately0.05(APE),0.105(InstructZero),0.157
(PromptBreeder),0.210(EvoPrompt),0.421(INSTINCT),0.68(PromptWizard). Thisshowsthat
PromptWizardisthebestperformingmethod,bettingalltheothermethodsat68%ofthetasks.
15

<!-- Page 16 -->

Table12: AveragetestaccuracyachievedbybestinstructiongeneratedbyInstinctandPWusing
GPT4asbasemodelonBBIIdataset.
Task Instinct PromptWizard
LLM:GPT4 Zero-shotsetting
antonyms 0.79 0.77
autocategorization 0.3 0.38
causeandeffect 0.96 0.88
commonconcept 0.2 0.15
diff 1 1
informaltoformal 0.6 0.75
letterslist 1 1
negation 0.7 0.85
objectcounting 0.6 0.82
oddoneout 0.54 0.87
orthographystartswith 0.75 0.92
rhymes 1 0.88
secondwordletter 0.57 0.97
sentencesimilarity 0.3 0.43
sum 0.99 1
synonyms 0.3 0.42
taxonomyanimal 0.9 1
wordsorting 0.5 0.65
wordunscrambling 0.54 0.77
# bestperformingtasks 6 15

### Algorithm1TotalLLMCallsCalculation

1: Calculation: Input: Hyperparameters,Result: TotalLLMCalls
2: refine_instructions_component ← mutate_refine_rounds × (mutate_rounds ×
style_variations+min_example_correct_count+critique+synthesize)
3: seq_iter_component ← max_seq_iter × (ex_critique + ex_synthesize + inst_critique +
inst_synthesize)
4: other_components←max_example_count+reasoning+validation+intent+persona
5: TotalLLMCalls ← refine_instructions_component + seq_iter_component +
other_components
(cid:8) (cid:0) (cid:1)(cid:9) (cid:8) (cid:9) (cid:8) (cid:0) (cid:1)(cid:9) (cid:8)
6: TotalLLMcalls = 3× (3×3)+5+1+1 + 5 + 3× (1+1)+(1+1) + 1+
(cid:9) (cid:8) (cid:9)
1 + 1+1 =48+5+12+2+2
7: Prompt_refinement=48;example_selection=5;seq_opt=12;
8: reason+validate=2;intent+expert=2
9: TotalLLMcalls=69

## 12 Additional Results: Bbii Dataset

Table12showsadditionalexperimentswithGPT-4asthebasemodel, PWachievedthehighest
accuracy in 15 out of 19 tasks, compared to Instinct’s 6 out of 19, demonstrating PW’s superior
performanceevenwithachangeinbasemodels.

## 13 Cost Analysis: Additional Details


## 1 Promptwizard Llmapicallscalculation

WecomputethetotalLLMcallsmadebyPromptWizardduringpromptgeneration(one-time),
which derives the most effective prompt and few-shot examples. The algorithm provides more
details: Algorithm1describesthetotalLLMcallsmadebyPromptWizardduringpreprocessing
(one-time),whichderivesthemosteffectivepromptandfew-shotexamples(seeAppendix10.for
parameterdescription). Notethatduringinference,eachqueryusesonlythedefaultoneLLMcall.
16

<!-- Page 17 -->

Table13: CostanalysisofInstinctandPromptWizardonBBIIdatasetwithGPT3.5Turboasthe
basemodel.

### Instinct PromptWizard

Dataset APICalls IOTokens APICalls IOTokens
antonyms 2200 39 69 334
auto-categorization 1740 86 69 341
causeandeffect 1352 61 69 390
commonconcept 639 94 69 386
diff 1820 58 69 381
informaltoformal 880 90 69 271
letterslist 2240 58 69 256
negation 2180 60 69 305
objectcounting 1340 69 69 470
oddoneout 840 50 69 372
orthographystartswith 1800 82 69 339
rhymes 1920 41 69 391
secondwordletter 1840 48 69 257
sentencesimilarity 2140 78 69 626
sum 2180 66 69 367
synonyms 2100 51 69 452
taxonomyanimal 1900 72 69 225
wordsorting 1680 110 69 426
wordunscrambling 2060 58 69 306

### Average 1729 67 69 362


## 2 Comparisonofapicalls,Numberoftokensforbbiidataset

Table13showsthecomparisonofAPIcalls,numberoftokensforBBIIdatasetforbothInstinctand
PromptWizardusingGPT3.5Turbomodel. WecanseethatPWhassignificantlowernumber
ofAPIcallscomparedtoInstinct,thusresultingin5xreductioninoveralltokenspertask. Similar
trendswiththeAPIcalls,numberoftokensused,wereseenwhenthebasemodelinInstinctandPW
waschangedtoGPT-4.

## 14 Promptwizard Algorithm

Algorithm2providespseudocodeforentirePromptWizardframework. Algorithm3provides
pseudocodeformutatingpromptinstructionandfurtherrefiningthebestpromptinstructionamong
allthemutatedpromptinstructions. i.e. Section3.1. Algorithm4and5providepseudocodefor
Sections3.2and3.3respectively.

### Algorithm2PromptWizardFramework

1: Input: L: large language model; D: problem description; S: set of training samples
{(q ,a )}N ; T: thinking styles; N: mutate_refine_rounds; k: few-shot count ; N :
i i i=1 1
max_seq_iter
2: Output: OptimizedpromptPˆ opt andfew-shotexamples{(q fi ,a fi )}k i=1
3: procedurePROMPTWIZARD(L,D,S,T,k,N,N 1 )
4: InitializeP ←initialpromptinstruction
5: Pˆ ←RefineInstructions(L,D,S,T,N)
6: E diverse ={(q di ,a di )}k i=1 ←DiverseExampleSelection(L,D,S,Pˆ)
7: Pˆ opt ,E syn ={(q si ,a si )}k i=1 ←SequentialOptimization(L,Pˆ,E diverse ,N 1 )
8: E ←ReasoningComponent(E ) ▷generatereasoningchains
syn,r syn
9: {(q fi ,a fi )}k i=1 ←ValidateComponent(E syn,r ) ▷validateexamples
10: τ ←SynthesizeComponent(D) ▷generatetaskintent
intent
11: π ←SynthesizeComponent(D) ▷generateexpertpersona
expert
12: returnπ expert ,Pˆ opt ,{(q fi ,a fi )}k i=1 ,τ intent
13: endprocedure
17

<!-- Page 18 -->


### Algorithm3RefineInstructionsProcedure

1: Input: L: large language model; D: problem description; S: set of training samples
{(q ,a )}N ; T: thinking styles; N: mutate_refine_rounds; b: batch size (default: 5); v:
i i i=1
numberofthinkingstylestoselect;M: mutate_rounds
2: Output: OptimizedpromptPˆ
3: procedureREFINEINSTRUCTIONS(L,D,S,T,N,b,v,M)
4: InitializeP ←initialpromptinstruction
5: OptimizedpromptPˆ ←P
6: forrefinement_round=1toN do
7: T 1 ←RandomlySelect(v,T) ▷SelectvthinkingstylesfromT

## 8: F ←∅

9: form=1toM do
10: M←MutateComponent(D,P,T 1 )
11: forp∈Mdo
12: s←ScoringComponent(p,S,b)
13: ifs>0.5then
14: F ←F ∪{(p,s)}
15: endif
16: endfor
17: endfor
18: top_scored_prompt←argmax p∈F {s(p)}
19: feedback←CritiqueComponent(top_scored_prompt)
20: Pˆ ←SynthesizeComponent(top_scored_prompt,feedback)
21: endfor
22:
returnPˆ
23: endprocedure

### Algorithm4DiverseExampleSelectionProcedure

1: Input: L: largelanguagemodel;D: problemdescription;S: trainingdataset{(q i ,a i )}N i=1 ;k:
few-shotcount
2: Output: SelecteddiverseexamplesE diverse ={(q di ,a di )}k i=1
3: procedureDIVERSEEXAMPLESELECTION(L,D,S,k)
4: S′ ←RandomSample(S,25)

## 5: E ←∅

diverse
6: count←0
7: for(q,a)∈S′do
8: a ←L(q) ▷LLM’sanswerforq
pred
9:
10: ifa ̸=athen
pred
11: E ←E ∪{(q,a)}
diverse diverse
12: count←count+1
13: endif
14: ifcount=kthen
15: break
16: endif
17: endfor
18: ifcount<kthen ▷SampleRandomCorrectExamples
19: E ←E ∪random.sample(S,k−count)
diverse diverse
20: endif
21: returnE
diverse
22: endprocedure
18

<!-- Page 19 -->


### Algorithm5SequentialOptimizationProcedure

1: Input: L: large language model; D: problem description; Pˆ: optimized prompt; E =
diverse
{(q ,a )}k : diverseexamples;n: max_seq_iter
di di i=1
2: Output: Final optimized task instruction Pˆ and synthetic few-shot examples E =
opt syn
{(q ,a )}k
si si i=1
3: procedureSEQUENTIALOPTIMIZATION(L,Pˆ,E
diverse
,n)

## 4: E ←E

syn diverse
5: forround=1tondo
6: feedback←CritiqueComponent(Pˆ,E ) ▷Examplesoptimizationstep
syn
7: E syn ={(q si ,a si )}k i=1 ←SynthesizeComponent(E diverse ,feedback)
8:
9: feedback←CritiqueComponent(Pˆ,E ) ▷Promptoptimizationstep
syn
10: Pˆ ←SynthesizeComponent(Pˆ,E ,feedback)
syn
11: endfor
12:
returnPˆ ←Pˆ,E
opt syn
13: endprocedure

## 15 Best Prompts For Bbii Tasks

BelowarethebestpromptobtainedusingPromptWizardforsomeofthetasksinBBIIdataset.
antonyms Yourtaskistoprovideanantonymforeachwordpresentedtoyou,keepinginmind
thattheoppositewordcanoftenbeformedbyusingprefixesorsuffixes. Ifit’snotpossibletodo
sowithoutalteringtherootword,chooseastandaloneantonymthatwidelyresonatestheopposite
meaningincommoncontexts. Theaimhereisnottoruleoutstandardmethodsofformingantonyms
ortoseekcontext-freeopposites,butrathertofindstraightforward,widelyacceptedoppositesbased
on every day usage and understanding. Regarding adverbs, note that some can have more than
oneantithesisdependingoncontext,soprovidethemostgenerallyapplicableone. Ensurethatthe
antonymsofferedreflectcommonlyunderstoodoppositions,withoutventuringintolessacceptedor
contextuallydelicatenuances. Remember,thefocushereisonprovidingclear,generallysuitable
oppositesratherthanunusualorhighlysituationalcounterparts.
Foreachinputwordpresentthereasoningfollowedbythecorrectword. Wraponlyyourfinalanswer,
withoutreasonforeachquestionseparatelybetween<ANS_START>and<ANS_END>.
negation Initiatetextinversionbytransformingthesentimentoftheinputsentencetoitsexact
reverse, while maintaining syntactic and grammatical accuracy and ensuring the output clearly
communicatestheopposingsentiment. Sticktoinputsentencesthatexpressopinions,feelings,or
subjectivejudgmentsinsteadoffactual,real-worldinformationorhistoricalevents.
Ifthesentencecontainsanauxiliaryverb,addthenegation’not’immediatelyafterit. Forsentences
withoutanauxiliary,add’not’beforethemainverb. Iftheinputsentenceincludesanegativeterm,
eliminateittoachievethereversesentiment.
Examineanyclauseswithmodalverbsclosely,keepinginmindtoswitch’can’to’can’t’andso
forthtoreversemeaning. Becautiouswhilealteringrelativeclauses,indirectspeech,oridiomatic
expressions. Theirsentimentinversionshouldbehandledcarefullywhilestillpreservinglinguistic
coherence.
Considerimplicitsentimentssuchasrhetoricalquestions,formsofirony,orsarcasm. Remember,
alteringthesedoesn’tmerelymeanskewingnegativetopositiveorviceversa. Thekeyistoensure
clarityandcomprehensionofthereversedsentiment.
Avoidchangingthetruthvalueofobjectivefactsorhistoricalevents,andifthemainverbofasentence
doesn’t carry the sentiment, consider implementing changes to other parts of the sentence—like
the subject or object—to successfully reverse the meaning. Regularly assess the result of your
modificationsforprecisionandunderstanding."
Foreachinputsentence,negatethemeaningbyadding’not’totheinputsentence. Wraponlyyour
finalanswer,withoutreasonforeachquestionseparatelybetween<ANS_START>and<ANS_END>.
19

<!-- Page 20 -->

secondwordletter Fortheprovidedword,yourtaskistospecificallyoutputthesecondletter.
For each input word, output only the extracted letter (only single letter) wrapped between
<ANS_START>and<ANS_END>tags.
sentencesimilarity Foreachinput,youwillfindtwosentences(Sentence1andSentence2). Your
taskistoevaluatetheirsimilaritybasedontwoelements: overallmeaningandspecificnumericalor
factualdetails.
Theimportanceofeachelementisweightedasfollows: 70%overallmeaningand30%numerical/-
factualdetails.

### Theevaluationscaleisnow:

0 - Definitely not: The sentences not only differ in overall meaning but also show significant
discrepancies in factual details. 1 - Probably not: There are minor similarities in meaning, but
significant differences in factual details are prevalent. 2 - Possibly: The sentences share some
elementsofmeaningbutshowdifferencesincertaindetailsornumericaldata. 3-Probably: The
sentencesexpresslargelysimilarmeaningsbuthavenoticeabledifferencesordiscrepanciesinspecific
detailsornumericaldata. 4-Almostperfectly: Thesentencesareverysimilarinmeaningwithonly
slightdiscrepanciesinfactualornumericaldetails. 5-Perfectly: Thesentencesareidenticalinterms
ofoverallmeaningandfactual/numericaldetails.
Incaseofconflictsbetweenoverallmeaningandfactualdetails,theweightingsystemwillguideyour
evaluation. Resultantratingshouldbeseparatedwith"-"forclarity,andshouldbeaccompaniedby
abrieftextualdescriptionofyourrating.
Provideyourratingandbrieftextualdescriptionforeachpairofsentencesfromthe6options. (0-
Definitelynot,1-Probablynot,2-Possibly,3-Probably,4-Almostperfectly,5-Perfectly)Wrap
onlyyourfinalanswer,withoutreasonforeachquestionseparatelybetween<ANS_START>and
<ANS_END>tags.
synonyms Yourassignmentinvolvesidentifyingalistofsynonymsforaprovidedword. These
synonymshouldnotonlysharethesamebasicmeaningwiththegivenword,butshouldalsobeable
toreplacetheoriginalwordinmostofitsusecaseswithoutresultinginlossofmeaningorcausing
thesentencetosoundstrange. Forexample,"report"couldbeasynonymfor"account"asbothcan
beusedinsimilarbusinessandfinancialsituationswhilepreservingtheessenceoftheoriginaluse.
Payattentiontothepartofspeech;asuitablesynonymforanounshouldalsobeanoun. Bewareof
falsefriendsthatevokesimilarthemesbutarenottruesynonyms;"rest"seemsrelatedto"pillow,"but
oneisatangibleobjectandtheotheranactionorstate,makingthemnon-interchangeable. Prioritize
synonymsthatmaintainthesemanticrichnessoftheoriginalterm,employthemregularlyinsimilar
contexts,andensuretheyhavethesameconnotation. Simplifyyourtaskbyrejectingwordsthathave
onlyaminorrelationshiporthosethatarebroaderinmeaning.
Foreachinputword,outputalistofsynonymwords. Wraponlyyourfinalanswer,withoutreason
foreachquestionseparatelybetween<ANS_START>and<ANS_END>tags.
wordsorting Givenaseriesofwordsinthetask,yourassignmentistoreordertheminalphabetical
order,prioritizingbythefirstletterofeveryword. Thinkstep-by-stepandconsiderthemostefficient
waytosortthewords. Wrapthelistofsortedwordsbetween<ANS_START>and<ANS_END>.

## 16 Prompt Templates

The prompt template for MutateComponent is: <problem description> <thinking
style pool> <#style_variation_number> < instruction>,where<instruction>
guidesMutateComponenttogeneratenewmutatedpromptsbycombiningtheproblemdescription
withthinkingstyles.
The prompt template for ScoringComponent is: <mutated/improved prompts>
<mini batch examples> < instruction>, where < instruction> guides
ScoringComponenttoevaluateallmutatedpromptsagainsttheexamplesinthemini-batch.
20

<!-- Page 21 -->

TheprompttemplateforCritiqueComponenttogetcritiqueoverpromptinstructionis: <best
mutated prompt> <selected mini batch examples> < instruction>, where
<instruction>guidesCritiqueComponenttoprovidefeedbackonhowtoimprovetheprompt
instructionbasedontheselectedexamples.
The prompt template for SynthesizeComponent to refine prompt instruction is: <best
mutated prompt> <critique feedback> < instruction>, where < instruction>
guidesSynthesizeComponenttogenerateanimprovedpromptusingthecritiquefeedback.
TheprompttemplateforCritiqueComponenttogetcritiqueoverfew-shotexamplesis: The
prompttemplateforCritiqueComponentisstructuredasfollows: <negativeexamples><improvedprompt><instruction>. ThisguidestheCritiqueComponenttoprovidedetailedfeedbackforimprovingexamples. ForSynthesizeComponent,theprompttemplateis<synthesized
examples><improvedprompt><instruction>,aidinginthesynthesisandrefinementofnewexamples.
TheprompttemplateforCritiqueComponentfollowsthisstructure: <synthesizedexamples>
<improvedprompt><instruction>,guidingtheCritiqueComponenttoprovidedetailedfeedbackforpromptimprovement.ForSynthesizeComponent,theprompttemplateis<synthesized
examples> <improved prompt> < instruction>, assisting in the synthesis and refinement of new
optimizedpromptsforthesyntheticexamples. Figure6demonstratesthecritiquefeedbackonthe
promptalongsidetherefinedoptimizedprompt. PromptTemplatesusedbydifferentcomponentsare
showninFig. 8

## 17 Best Prompts

Bestpromptfoundforeachdatasetareshownbelow:

## 1 Gsm8Kprompt

1 <the optimized prompt instruction>
2
3 Analyze the given real-world mathematical problem step-by-step,
identifying key information, relationships between different pieces
of data, and the context. Understand the structure of the problem,
whether it involves a sequence of events or a comparison between
different quantities. Keep track of all variables and quantities
mentioned in the problem. Use appropriate mathematical operations and
formulas, including addition, subtraction, multiplication, division,
and more complex operations if required. Understand and handle
indirect relationships and different units of measurement. Apply
specific rules or conditions given in the problem. Make assumptions
when information is not explicitly provided. Consider the order of
operations when performing calculations. Understand the structure and
properties of the data in the problem. Finally, verify your answer
against the original problem to ensure it is logical and accurate.
1 <synthesized examples + reasoning chain>
2
3 [Question] Tim rides his bike back and forth to work for each of his 5
workdays. His work is 20 miles away. He also goes for a weekend
bike ride of 200 miles. If he can bike at 25 mph how much time
does he spend biking a week?
4 [Answer] 1. Identify the key pieces of information: Tim bikes to work and
back for 5 days, his work is 20 miles away, he goes for a 200-mile
bike ride on the weekend, and his biking speed is 25 mph.
5 2. Understand that the problem involves a sequence of events: Tim’s daily
commute to work and back, and his weekend bike ride.
6 3. Calculate the total distance Tim bikes to work and back in a week: 20
miles to work * 2 (for the return trip) = 40 miles per day. Multiply
this by 5 days: 40 miles/day * 5 days = 200 miles.
7 4. Add the distance of Tim’s weekend bike ride to the total distance he
bikes to work: 200 miles (work) + 200 miles (weekend) = 400 miles.
21

<!-- Page 22 -->

Figure8: PromptTemplatesfordifferentcomponentsofPromptWizard.
22

<!-- Page 23 -->

8 5. Understand that the problem asks for the total time Tim spends biking
in a week, and that time can be calculated by dividing distance by
speed.
9 6. Calculate the total time Tim spends biking in a week: 400 miles / 25
mph = 16 hours.
10 7. Verify that the answer is logical: Tim spends 16 hours biking in a
week, which is reasonable given the distances and speed provided.
11 8. The final answer is 16 hours. <ANS_START>16<ANS_END>
12
13
14 [Question] Tobias is buying a new pair of shoes that costs $95. He has
been saving up his money each month for the past three months. He
gets a $5 allowance a month. He also mows lawns and shovels driveways
. He charges $15 to mow a lawn and $7 to shovel. After buying the
shoes, he has $15 in change. If he mows 4 lawns, how many driveways
did he shovel?
15 [Answer] 1. Identify the total amount of money Tobias had before buying
the shoes. This is given by the cost of the shoes plus the change he
has left, which is $95 + $15 = $110.
16 2. Calculate the total amount of money Tobias earned from his allowance.
He gets $5 a month and has been saving for three months, so he earned
$5 * 3 = $15 from his allowance.
17 3. Calculate the total amount of money Tobias earned from mowing lawns.
He charges $15 to mow a lawn and he mowed 4 lawns, so he earned $15 *
4 = $60 from mowing lawns.
18 4. Subtract the money Tobias earned from his allowance and mowing lawns
from the total amount of money he had before buying the shoes. This
will give us the amount of money he earned from shoveling driveways.
So, $110 - $15 - $60 = $35 is the amount he earned from shoveling
driveways.
19 5. Finally, divide the total amount of money Tobias earned from shoveling
driveways by the amount he charges to shovel one driveway. This will
give us the number of driveways he shoveled. So, $35 / $7 = 5
driveways. <ANS_START>5<ANS_END>
20
21 [Question] Bella bought stamps at the post office. Some of the stamps had
a snowflake design, some had a truck design, and some had a rose
design. Bella bought 11 snowflake stamps. She bought 9 more truck
stamps than snowflake stamps, and 13 fewer rose stamps than truck
stamps. How many stamps did Bella buy in all?
22 [Answer] 1. Identify the quantities given in the problem: Bella bought 11
snowflake stamps.
23 2. Understand the relationships between the different types of stamps:
She bought 9 more truck stamps than snowflake stamps, and 13 fewer
rose stamps than truck stamps.
24 3. Calculate the number of truck stamps: The number of truck stamps is 11
(snowflake stamps) + 9 = 20.
25 4. Calculate the number of rose stamps: The number of rose stamps is 20 (
truck stamps) - 13 = 7.
26 5. Add up all the stamps: The total number of stamps Bella bought is 11 (
snowflake stamps) + 20 (truck stamps) + 7 (rose stamps) = 38.
27 6. Verify the answer: Check that the total number of stamps (38) matches
the sum of the individual quantities of each type of stamp (11
snowflake stamps, 20 truck stamps, 7 rose stamps). The answer is
correct. <ANS_START>38<ANS_END>
28
29 [Question] Tina makes $18.00 an hour. If she works more than 8 hours per
shift, she is eligible for overtime, which is paid by your hourly
wage + 1/2 your hourly wage. If she works 10 hours every day for 5
days, how much money does she make?
30 [Answer] 1. Identify the key information: Tina’s hourly wage is \$18.00,
she works 10 hours a day for 5 days, and overtime is calculated as
the hourly wage plus half the hourly wage for hours worked over 8
hours in a shift.
23

<!-- Page 24 -->

31 2. Calculate the regular pay: Tina works 10 hours a day, but only 8 hours
are considered regular hours. So, for 5 days, she works 8 hours/day
* 5 days = 40 hours.
32 3. Multiply the regular hours by the hourly wage to get the regular pay:
40 hours * $18.00/hour = $720.00.
33 4. Calculate the overtime hours: Tina works 10 hours a day, so she has 10
hours/day - 8 hours/day = 2 hours/day of overtime. Over 5 days, this
is 2 hours/day * 5 days = 10 hours of overtime.
34 5. Calculate the overtime wage: The overtime wage is the hourly wage plus
half the hourly wage, so $18.00/hour + 0.5 * $18.00/hour = $27.00/
hour.
35 6. Multiply the overtime hours by the overtime wage to get the overtime
pay: 10 hours * $27.00/hour = $270.00.
36 7. Add the regular pay and the overtime pay to get the total pay: $720.00
+ $270.00 = $990.00.
37 8. Verify the answer: Tina makes $990.00 if she works 10 hours a day for
5 days, with overtime pay for hours worked over 8 hours in a shift.
This is logical and matches the original problem. <ANS_START>990<

## Ans_End>

38
39 [Question] Samantha’s last name has three fewer letters than Bobbie’s
last name. If Bobbie took two letters off her last name, she would
have a last name twice the length of Jamie’s. Jamie’s full name is

### Jamie Grey. How many letters are in Samantha’s last name?

40 [Answer] 1. Start by identifying the key pieces of information from the
problem: Samantha’s last name has three fewer letters than Bobbie’s
last name, and if Bobbie took two letters off her last name, she
would have a last name twice the length of Jamie’s. Jamie’s full name
is Jamie Grey.
41 2. From the information given, we know that Jamie’s last name is Grey,
which has 4 letters.
42 3. Since Bobbie’s last name, after removing two letters, is twice the
length of Jamie’s last name, we can set up the equation: (Bobbie’s
last name length - 2) = 2 * Jamie’s last name length.
43 4. Substituting the known value of Jamie’s last name length (4) into the
equation gives: (Bobbie’s last name length - 2) = 2 * 4, which
simplifies to Bobbie’s last name length - 2 = 8.
44 5. Solving for Bobbie’s last name length gives: Bobbie’s last name length
= 8 + 2 = 10.
45 6. We know that Samantha’s last name has three fewer letters than Bobbie’
s last name. So, we can set up the equation: Samantha’s last name
length = Bobbie’s last name length - 3.
46 7. Substituting the known value of Bobbie’s last name length (10) into
the equation gives: Samantha’s last name length = 10 - 3.
47 8. Solving for Samantha’s last name length gives: Samantha’s last name
length = 7.
48 9. Therefore, Samantha’s last name has 7 letters. <ANS_START>7<ANS_END>
1 <human intent>
2
3 Mathematical Reasoning, Multi-step Problem Solving, Basic Arithmetic
Operations, Data Analysis, Solution Verification
4
5 <expert persona>
6
7 You are a mathematics educator with a deep understanding of elementary
and middle school mathematics. You are experienced in teaching multistep problem-solving techniques and have a knack for breaking down
complex problems into manageable steps. Your expertise lies in basic
arithmetic operations such as addition, subtraction, multiplication,
and division. You can provide clear, step-by-step solutions to
mathematical problems that require multi-step reasoning. You are
patient and thorough, ensuring that each step is clearly explained
and understood. Your ability to simplify complex problems and guide
24

<!-- Page 25 -->

students through the problem-solving process makes you an excellent
resource for answering school-grade mathematical questions.
8
9 <prompt guidelines for desired output format>
10
11 You need to answer each of the questions separately. Arabic numeral
should be at the end in the format Wrap your only the final answer,
without reason for each question separately between <ANS_START> and <
ANS_END> tags.

## 2 Ethosprompt

1 <the optimized prompt instruction>
2
3 Carefully examine the provided text and determine if it constitutes hate
speech. Hate speech is defined as language that is derogatory,
offensive, or discriminatory towards a specific group of people based
on their race, gender, or other characteristics, with the intent to
harm or degrade. Even if the statement appears factual or sarcastic,
if it uses aggressive language or personal attacks aimed at a
specific group, it should be classified as hate speech.
1 <synthesized examples + reasoning chain>
2
3 [Question] While I appreciate the hard work of some immigrants, others
are just here to exploit our system and take our jobs.
4 [Answer] 1. Start by reading the provided text to understand its content.
5 2. The task requires identifying if the text contains hate speech.
According to the task description, hate speech is language that is
derogatory, offensive, or discriminatory towards a specific group of
people based on their race, gender, or other characteristics, with
the intent to harm or degrade.
6 3. The text states, "While I appreciate the hard work of some immigrants,
others are just here to exploit our system and take our jobs."
7 4. This statement is making a generalization about a specific group of
people, in this case, immigrants. It suggests that some immigrants
are exploiting the system and taking jobs, which is a negative
stereotype.
8 5. Even though the text acknowledges the hard work of some immigrants, it
still uses derogatory language towards others, implying they are
here to exploit the system.
9 6. This statement can be seen as offensive and discriminatory towards
immigrants, as it negatively stereotypes them and can potentially
harm or degrade them.
10 7. Therefore, according to the task description and instruction, this
text can be classified as hate speech.\newline
11 8. As per the task instruction, if the text contains hate speech, the
output should be 1.
12 9. Hence, the final answer is 1. <ANS_START>1<ANS_END>
13
14 [Question] I’ve noticed that female politicians are more corrupt and only
care about their own interests.\newline
15 [Answer] 1. Start by reading the provided text: "I’ve noticed that female
politicians are more corrupt and only care about their own interests
."
16 2. Identify the subject of the text: The subject is "female politicians."
17 3. Analyze the language used in the text: The language used is derogatory
and offensive, as it generalizes all female politicians as being "
more corrupt" and only caring about their own interests.
18 4. Determine if the language is discriminatory: The language
discriminates against a specific group, in this case, female
politicians, by making a negative generalization about them.
25

<!-- Page 26 -->

19 5. Check if the language has the intent to harm or degrade: The language
used seems to degrade the reputation of female politicians by
portraying them as corrupt and self-interested.
20 6. Based on the task description and instruction, the text is considered
hate speech if it is derogatory, offensive, or discriminatory towards
a specific group of people with the intent to harm or degrade.
21 7. Since the text meets all these criteria, it is classified as hate
speech.
22 8. According to the task instruction, if the text contains hate speech,
the output should be 1.
23 9. Therefore, the final answer is 1. <ANS_START>1<ANS_END>
24
25 [Question] I don’t get why we have to accept people who choose to be
transgender. It’s unnatural and against our values.
26 [Answer] 1. Start by reading the provided text.
27 2. Identify the subject of the text. In this case, the subject is "people
who choose to be transgender."
28 3. Analyze the language used in the text. The text uses phrases like "It’
s unnatural" and "against our values," which are derogatory and
offensive.
29 4. Determine if the language is aimed at a specific group. Here, the
language is targeted towards transgender people, a specific group.
30 5. Check if the language is intended to harm or degrade the specific
group. The text implies that being transgender is unnatural and
against societal values, which can be seen as an attempt to degrade
or harm the transgender community.\newline
31 6. Since the text uses offensive language against a specific group with
the intent to harm or degrade, it can be classified as hate speech.
32 7. Therefore, the correct answer is 1, indicating that the text contains
hate speech. <ANS_START>1<ANS_END>
1 <human intent>
2
3 Text Analysis, Hate Speech Identification, Discriminatory Language
Detection, Offensive Content Recognition, Derogatory Language
Classification
4
5 <expert persona>
6
7 You are a machine learning engineer with a specialization in natural
language processing and text analysis. You have developed and trained
algorithms to detect and classify different types of text, including
hate speech. Your algorithm can analyze the given text, identify
patterns, and determine whether it contains hate speech or not. You
are equipped with a deep understanding of the nuances of language,
and you can differentiate between offensive language, strong
criticism, and actual hate speech. Your algorithm is designed to be
fair and unbiased, and it respects the principles of freedom of
speech while also recognizing the harm caused by hate speech. Your
expertise in text analysis and machine learning is highly valuable in
moderating online content and creating a safer digital environment.
8
9 <prompt guidelines for desired output format>
10 You need to answer each of the questions separately with 1 if its a hate
speech and 0 if its not a hate speech. Wrap your only the final
answer, without reason for each question separately between <
ANS_START> and <ANS_END> tags.

## 3 Pubmedqaprompt

1 <the optimized prompt instruction>
2
3 Carefully read the abstract and identify the key points that directly
address the biomedical research question. Based on these key points,
26

<!-- Page 27 -->

provide a clear and concise answer in a "Yes" or "No" format,
followed by a brief explanation that correlates the research question
with the findings in the abstract.
1 <synthesized examples + reasoning chain>
2
3 [Question] Does the process of photosynthesis under varying light
intensities and temperature play a significant role in the growth of
different species of algae?\newline
4 [Abstract] : Photosynthesis is a process used by plants and other
organisms to convert light energy into chemical energy that can later
be released to fuel the organisms’ activities. This study
investigates the impact of varying light intensities and temperature
on the photosynthetic process in different species of algae. The
algae were exposed to different light intensities and temperatures,
and their growth rate was monitored over a period of time. The
results showed a direct correlation between light intensity,
temperature and the growth rate of algae.
5 [Answer] 1. The question asks whether the process of photosynthesis under
varying light intensities and temperature plays a significant role
in the growth of different species of algae.
6 2. The abstract provides information about a study that investigates the
impact of varying light intensities and temperature on the
photosynthetic process in different species of algae.
7 3. The abstract mentions that the algae were exposed to different light
intensities and temperatures, and their growth rate was monitored
over a period of time.\newline
8 4. The results of the study, as mentioned in the abstract, showed a
direct correlation between light intensity, temperature and the
growth rate of algae.
9 5. This direct correlation indicates that the process of photosynthesis
under varying light intensities and temperature does indeed play a
significant role in the growth of different species of algae.
10 6. Therefore, based on the information provided in the abstract, the
answer to the question is "Yes". <ANS_START>yes<ANS_END>
11
12
13 [Question] Is the use of antiviral drugs effective in treating influenza,
a common viral infection?
14 [Abstract] : Antiviral drugs are medicines used to prevent and treat
viral infections. Influenza, on the other hand, is a viral infection.
This study investigates the effectiveness of antiviral drugs in
treating influenza. The study involved patients suffering from
influenza who were treated with antiviral drugs. The results showed
significant improvement in the condition of the patients.
15 [Answer] 1. The question asks about the effectiveness of antiviral drugs
in treating influenza, a common viral infection.
16 2. The abstract provides information about a study that investigates the
effectiveness of antiviral drugs in treating influenza.
17 3. The study involved patients suffering from influenza who were treated
with antiviral drugs.\newline
18 4. The results of the study showed significant improvement in the
condition of the patients after they were treated with antiviral
drugs.
19 5. Therefore, based on the results of the study mentioned in the abstract
, it can be concluded that the use of antiviral drugs is effective in
treating influenza.
20 6. Hence, the answer to the question is "Yes". <ANS_START>yes<ANS_END>
21
22
23 [Question] Are intensive care units more beneficial than general wards
for the treatment of severe pneumonia in children with underlying
health conditions?
24 [Abstract] : Pneumonia is a common illness in children that can become
severe if not properly treated. Intensive care units (ICUs) provide
27

<!-- Page 28 -->

specialized care for patients with severe or life-threatening
illnesses. This study examines the impact of ICU treatment on
children with severe pneumonia and underlying health conditions. The
study compared the recovery rates of children treated in ICUs with
those treated in general wards. The results showed a higher recovery
rate in children with underlying health conditions treated in ICUs.\
newline
25 [Answer] 1. The question asks whether intensive care units (ICUs) are
more beneficial than general wards for the treatment of severe
pneumonia in children with underlying health conditions.
26 2. The abstract provides information about a study that examined the
impact of ICU treatment on children with severe pneumonia and
underlying health conditions.\newline
27 3. The study compared the recovery rates of children treated in ICUs with
those treated in general wards.
28 4. The results of the study showed a higher recovery rate in children
with underlying health conditions treated in ICUs.
29 5. Therefore, based on the results of the study presented in the abstract
, the answer to the question is "Yes". ICUs are more beneficial than
general wards for the treatment of severe pneumonia in children with
underlying health conditions. <ANS_START>yes<ANS_END>
30
31 [Question] Is the blood glucose level a more reliable marker than HbA1c
for diagnosing Diabetes?
32 [Abstract] : Diabetes is a chronic disease that affects the body’s
ability to process sugar. Blood glucose levels and HbA1c are commonly
used markers for diagnosing diabetes. This study investigates the
reliability of blood glucose levels and HbA1c as markers for
diagnosing Diabetes. The study involved patients diagnosed with
Diabetes and their blood glucose and HbA1c levels were measured. The
results showed a significant correlation between high blood glucose
levels and Diabetes diagnosis, but not with HbA1c levels.
33 [Answer] 1. The question asks whether blood glucose level is a more
reliable marker than HbA1c for diagnosing Diabetes.\newline
34 2. The abstract provides information about a study that investigates the
reliability of blood glucose levels and HbA1c as markers for
diagnosing Diabetes.
35 3. The abstract mentions that the study involved patients diagnosed with
Diabetes and their blood glucose and HbA1c levels were measured.
36 4. The key point in the abstract is the results of the study, which
showed a significant correlation between high blood glucose levels
and Diabetes diagnosis, but not with HbA1c levels.
37 5. This indicates that blood glucose levels are a more reliable marker
for diagnosing Diabetes than HbA1c levels, according to the study.
38 6. Therefore, based on the information provided in the abstract, the
answer to the question is "Yes". <ANS_START>yes<ANS_END>
39
40
41 [Question] Can regular strength training reduce the risk of osteoporosis
in adults over 60?
42 [Abstract] : Osteoporosis is a major health issue globally, especially in
adults over 60. Regular strength training is known to have various
health benefits, including improving bone health. This study
investigates the impact of regular strength training on the risk of
osteoporosis in adults over 60. The study involved participants who
engaged in regular strength training and their bone health was
monitored over a period of time. The results showed a lower incidence
of osteoporosis in participants who engaged in regular strength
training.
43 [Answer] 1. The question asks whether regular strength training can
reduce the risk of osteoporosis in adults over 60.
44 2. The abstract provides information about a study that investigates the
impact of regular strength training on the risk of osteoporosis in
adults over 60.
28

<!-- Page 29 -->

45 3. The abstract mentions that regular strength training is known to have
various health benefits, including improving bone health.
46 4. The study involved participants who engaged in regular strength
training and their bone health was monitored over a period of time.
47 5. The results of the study, as mentioned in the abstract, showed a lower
incidence of osteoporosis in participants who engaged in regular
strength training.
48 6. Therefore, based on the results of the study mentioned in the abstract
, it can be concluded that regular strength training can reduce the
risk of osteoporosis in adults over 60.
49 7. Hence, the answer to the question is "Yes". <ANS_START>yes<ANS_END>
1 <human intent>
2 Biomedical Research Understanding, Abstract Analysis, Key Point
Identification, Concise Answering, Explanation Correlation
3
4 <expert persona>
5
6 You are a biomedical researcher with a deep understanding of medical and
scientific literature. You have a strong background in reading and
interpreting scientific abstracts, and you are skilled at extracting
key information from complex texts. You can accurately answer
biomedical research questions based on the information provided in
the corresponding abstracts. Your expertise in biomedical research
allows you to understand the nuances and implications of the findings
presented in the abstracts, and you can provide clear, concise, and
accurate answers to the questions. Your ability to critically analyze
and interpret scientific literature makes you an invaluable resource
in the field of biomedical research.
7
8 <prompt guidelines for desired output format>
9
10 You need to answer each of the questions separately with yes/ no/ maybe.
Wrap your only the final answer, without reason for each question
separately between <ANS_START> and <ANS_END> tags.

## 4 Medqaprompt

1 <the optimized prompt instruction>
2
3 Analyze the patient’s age, symptoms, duration and onset of symptoms,
history of present illness, lifestyle factors, physical examination
findings, and any diagnostic test results presented in the Medical
Licensing Examination question. Use your knowledge of medicine to
identify the most likely diagnosis or appropriate treatment. Consider
the progression, severity, and duration of the patient’s symptoms in
relation to the answer options. Eliminate incorrect answer options
based on your medical knowledge and ensure your final choice is the
most appropriate given the specifics of the question. Validate your
answer by ensuring it aligns with all the information provided in the
question, including the patient’s age, lifestyle factors, and
specific diagnostic test results.
1 <synthesized examples + reasoning chain>
2
3 [Question] A 50-year-old man with a history of hypertension and type 2
diabetes presents with a 3-day history of chest pain radiating to the
left arm. He also reports shortness of breath and fatigue. Physical
examination reveals a blood pressure of 150/90 mmHg, heart rate of
90/min, and an irregular pulse. An ECG shows ST-segment elevation in
leads II, III, and aVF. Which of the following is the most
appropriate initial treatment?
4 Options:
5 A: Aspirin and clopidogrel
29

<!-- Page 30 -->

6 B: Metformin
7 C: Lisinopril
8 D: Atorvastatin
9
10 [Answer] 1. Start by analyzing the patient’s age, symptoms, and medical
history. The patient is a 50-year-old man with a history of
hypertension and type 2 diabetes. He presents with chest pain
radiating to the left arm, shortness of breath, and fatigue. These
symptoms are indicative of a cardiovascular event.
11 2. Consider the physical examination findings. The patient has a blood
pressure of 150/90 mmHg, heart rate of 90/min, and an irregular pulse
. These findings further support the likelihood of a cardiovascular
event.
12 3. Review the diagnostic test results. The ECG shows ST-segment elevation
in leads II, III, and aVF. This is a classic sign of an ST-segment
elevation myocardial infarction (STEMI), a type of heart attack.
13 4. Given the diagnosis of STEMI, consider the most appropriate initial
treatment. The options are Aspirin and clopidogrel (A), Metformin (B)
, Lisinopril (C), and Atorvastatin (D).
14 5. Eliminate incorrect answer options based on medical knowledge.
Metformin (B) is a medication for diabetes, Lisinopril (C) is an
antihypertensive medication, and Atorvastatin (D) is a cholesterollowering medication. While these medications may be part of the
patient’s long-term management, they are not the most appropriate
initial treatment for a STEMI.
15 6. Aspirin and clopidogrel (A) are antiplatelet medications. They work by
preventing blood clots, which is crucial in the initial management
of a STEMI to restore blood flow to the heart muscle.
16 7. Therefore, the most appropriate initial treatment for this patient,
given his symptoms, physical examination findings, and ECG results,
is Aspirin and clopidogrel (A). This aligns with all the information
provided in the question and is the most appropriate given the
specifics of the question.
17 8. Validate the final choice (A) as it is the most appropriate initial
treatment for a patient presenting with a STEMI. <ANS_START>A<ANS_END
>
18
19
20 [Question] A 6-month-old girl is brought to the physician by her mother
because of a 2-day history of fever and irritability. She also has a
rash on her cheeks. Physical examination reveals a temperature of
38.5C (101.3F), a heart rate of 120/min, and a respiratory rate of
30/min. Examination of the skin shows erythema of the cheeks with
sparing of the nasal bridge and perioral area. Which of the following
is the most likely diagnosis?
21 Options:
22 A: Measles
23 B: Fifth disease
24 C: Roseola
25 D: Scarlet fever
26
27 [Answer] 1. Start by analyzing the patient’s age, symptoms, duration and
onset of symptoms, and physical examination findings. The patient is
a 6-month-old girl with a 2-day history of fever and irritability.
She also has a rash on her cheeks. Her temperature is 38.5C (101.3F),
a heart rate of 120/min, and a respiratory rate of 30/min. The skin
examination shows erythema of the cheeks with sparing of the nasal
bridge and perioral area.
28 2. Use your medical knowledge to identify the most likely diagnosis. The
symptoms presented are indicative of a viral exanthem, a rash that
appears due to a viral infection.
29 3. Consider the answer options. The options are Measles, Fifth disease,
Roseola, and Scarlet fever. All of these are diseases that can
present with a rash.
30

<!-- Page 31 -->

30 4. Eliminate incorrect answer options based on your medical knowledge.
Measles typically presents with a rash that starts at the hairline
and moves down, along with Koplik spots in the mouth, which are not
mentioned in the question. Scarlet fever typically presents with a
sandpaper-like rash and a strawberry tongue, which are also not
mentioned. Roseola typically presents with a high fever that suddenly
drops as a rash appears, which does not match the patient’s symptoms
.
31 5. The remaining option is Fifth disease, also known as erythema
infectiosum. This disease is common in children and presents with a "
slapped cheek" rash, fever, and irritability, which aligns with the
patient’s symptoms.
32 6. Validate your answer by ensuring it aligns with all the information
provided in the question. The patient’s age, symptoms, and physical
examination findings all align with a diagnosis of Fifth disease.
33 7. Therefore, the correct answer is B: Fifth disease. <ANS_START>B<

## Ans_End>

34
35
36 [Question] A 70-year-old man presents with a 1-year history of
progressive memory loss, difficulty finding words, and getting lost
in familiar places. Neurologic examination shows impaired recall and
disorientation to time and place. MRI of the brain shows cortical
atrophy and enlarged ventricles. Which of the following is the most
likely diagnosis?
37 Options:
38 A: Alzheimer’s disease
39 B: Vascular dementia
40 C: Lewy body dementia
41 D: Frontotemporal dementia
42
43 [Answer] 1. Start by analyzing the patient’s age, symptoms, duration and
onset of symptoms, and the results of the physical examination and
diagnostic tests. The patient is a 70-year-old man with a 1-year
history of progressive memory loss, difficulty finding words, and
getting lost in familiar places. The neurologic examination shows
impaired recall and disorientation to time and place. The MRI of the
brain shows cortical atrophy and enlarged ventricles.
44 2. Consider the progression, severity, and duration of the patient’s
symptoms. The symptoms have been progressing over a year, which
indicates a chronic condition.
45 3. Use your medical knowledge to identify the most likely diagnosis. The
symptoms of progressive memory loss, difficulty finding words, and
getting lost in familiar places, along with impaired recall and
disorientation to time and place, are characteristic of a
neurodegenerative disease.
46 4. Look at the answer options and eliminate incorrect ones based on your
medical knowledge. Vascular dementia (Option B) typically presents
with stepwise deterioration of cognitive function, which is not the
case here. Lewy body dementia (Option C) is usually accompanied by
visual hallucinations, parkinsonism, or fluctuating cognition, none
of which are mentioned in the question. Frontotemporal dementia (
Option D) often presents with changes in personality and behavior,
which is also not mentioned in the question.
47 5. The remaining option is Alzheimer’s disease (Option A), which is a
neurodegenerative disease that commonly presents with progressive
memory loss, difficulty finding words, and getting lost in familiar
places, especially in older adults. The MRI findings of cortical
atrophy and enlarged ventricles are also consistent with Alzheimer’s
disease.
48 6. Validate your answer by ensuring it aligns with all the information
provided in the question. Alzheimer’s disease fits with the patient’s
age, the chronic and progressive nature of the symptoms, the
neurologic examination findings, and the MRI results.
31

<!-- Page 32 -->

49 7. Therefore, the correct answer is A: Alzheimer’s disease. <ANS_START>A<

## Ans_End>

50
51
52 [Question] A 35-year-old woman presents with a 2-week history of severe
headache, fever, and photophobia. She also reports a rash on her
lower extremities. Physical examination reveals a temperature of 38.2
C (100.8F), a heart rate of 110/min, and a petechial rash on her
lower extremities. Lumbar puncture shows increased white blood cells
with a predominance of lymphocytes, increased protein, and normal
glucose. Which of the following is the most appropriate
pharmacotherapy?
53 Options:
54 A: Ceftriaxone and vancomycin
55 B: Acyclovir
56 C: Amphotericin B
57 D: Doxycycline
58
59 [Answer] 1. Start by analyzing the patient’s symptoms: severe headache,
fever, photophobia, and a petechial rash on her lower extremities.
These symptoms suggest a systemic infection, possibly involving the
central nervous system given the presence of headache and photophobia
.
60 2. Consider the patient’s age and duration of symptoms. A 35-year-old
woman with a 2-week history of these symptoms suggests an acute
infection rather than a chronic condition.
61 3. Review the physical examination findings and diagnostic test results.
The patient has a fever and tachycardia, further supporting the
presence of a systemic infection. The lumbar puncture results show
increased white blood cells with a predominance of lymphocytes,
increased protein, and normal glucose. These findings are indicative
of viral meningitis.
62 4. Evaluate the answer options in relation to the most likely diagnosis.
Viral meningitis is typically caused by enteroviruses, herpes simplex
virus, or arboviruses.
63 5. Option A (Ceftriaxone and vancomycin) is used to treat bacterial
meningitis, which is not consistent with the lumbar puncture results.
Eliminate this option.
64 6. Option B (Acyclovir) is an antiviral medication used to treat
infections caused by herpes viruses, including herpes simplex virus
meningitis. This option aligns with the diagnosis.
65 7. Option C (Amphotericin B) is an antifungal medication, which is not
consistent with the diagnosis of viral meningitis. Eliminate this
option.
66 8. Option D (Doxycycline) is an antibiotic used to treat bacterial
infections, including certain types of bacterial meningitis, but it
is not the first-line treatment for viral meningitis. Eliminate this
option.
67 9. Validate the final choice (Option B: Acyclovir) by ensuring it aligns
with all the information provided in the question, including the
patient’s age, symptoms, physical examination findings, and specific
diagnostic test results.
68 10. Therefore, the correct answer is B: Acyclovir. <ANS_START>B<ANS_END>
69
70
71 [Question] A 40-year-old man with a history of alcohol abuse presents
with a 1-day history of severe abdominal pain, nausea, and vomiting.
Physical examination reveals a distended abdomen, decreased bowel
sounds, and tenderness to palpation in the upper abdomen. Laboratory
tests show an elevated serum amylase and lipase. Which of the
following is the most likely diagnosis?
72 Options:
73 A: Acute pancreatitis
74 B: Peptic ulcer disease
75 C: Gastric cancer
32

<!-- Page 33 -->

76 D: Gastroenteritis
77
78 [Answer] 1. Start by analyzing the patient’s age, symptoms, duration and
onset of symptoms, history of present illness, lifestyle factors,
physical examination findings, and any diagnostic test results
presented in the question. The patient is a 40-year-old man with a
history of alcohol abuse. He has been experiencing severe abdominal
pain, nausea, and vomiting for 1 day. His abdomen is distended, bowel
sounds are decreased, and there is tenderness in the upper abdomen.
His serum amylase and lipase levels are elevated.
79 2. Use your knowledge of medicine to identify the most likely diagnosis.
The patient’s history of alcohol abuse, the sudden onset and severity
of his symptoms, and his physical examination findings are all
indicative of a pancreatic condition. The elevated serum amylase and
lipase levels further support this, as these enzymes are produced by
the pancreas and their levels increase in the blood when the pancreas
is inflamed or damaged.
80 3. Consider the answer options in relation to the patient’s symptoms and
test results. Acute pancreatitis, peptic ulcer disease, gastric
cancer, and gastroenteritis are all potential diagnoses.
81 4. Eliminate incorrect answer options based on your medical knowledge.
Peptic ulcer disease typically presents with a burning pain in the
middle or upper stomach between meals or at night, not with a
distended abdomen and decreased bowel sounds. Gastric cancer usually
develops slowly over many years, and its symptoms often only appear
in the advanced stages of the disease. Gastroenteritis, while it can
cause abdominal pain, nausea, and vomiting, does not typically result
in a distended abdomen, decreased bowel sounds, or elevated serum
amylase and lipase levels.
82 5. The remaining option, acute pancreatitis, aligns with all the
information provided in the question. The patient’s history of
alcohol abuse is a common risk factor for acute pancreatitis. The
sudden onset and severity of his symptoms, his physical examination
findings, and his elevated serum amylase and lipase levels are all
characteristic of this condition.
83 6. Therefore, the most likely diagnosis for this patient is acute
pancreatitis, making option A the correct answer. <ANS_START>A<

## Ans_End>

1
2 <human intent>
3 Medical Knowledge, Analytical Skills, English Proficiency, Reasoning
Skills, Attention to Detail
4
5 <expert persona>
6 You are a medical professional with extensive experience in the field and
a deep understanding of the United States Medical Licensing Exam (
USMLE). You have successfully passed the USMLE and have a thorough
understanding of the format and style of the questions. You are wellversed in a wide range of medical topics, from anatomy and physiology
to pathology and pharmacology. You have the ability to analyze
complex medical scenarios, apply your knowledge, and make informed
decisions. You can accurately interpret the questions and the
provided options, and select the correct answer based on your medical
knowledge and reasoning. Your expertise and experience make you
highly capable of answering these questions correctly and efficiently
7
8 <prompt guidelines for desired output format>
9 You need to output the correct option among [A/B/C/D] for each question
separately using your medical knowledge and reasoning. Wrap your only
the final answer, without reason for each question separately
between <ANS_START> and <ANS_END> tags.
33

## Tables

**Table (Page 2):**

| Sequential Optimization |  |  |  |  |
|---|---|---|---|---|
|  |  | Optimized Prompt |  |  |
|  |  |  |  | Self-generated Reasoning and Validation |
|  |  |  |  |  |
|  |  |  | ed |  |


**Table (Page 2):**

|  |  | Iterative Refinement of Prompt Instructions | Modified Prompt Instruction |
|---|---|---|---|
|  |  |  |  |
| Prompt Instruction |  |  |  |
|  |  |  |  |


**Table (Page 2):**

|  |
|---|
| Optimized Prompt |
| Optimized Few-shot with reasoning |
| Task Intent + Expert Persona |


**Table (Page 3):**

| APE InstructZero PromptBreeder EvoPrompt INSTINCT PromptWizard |  |
|---|---|
|  | APE InstructZero PromptBreeder EvoPrompt INSTINCT PromptWizard |


**Table (Page 4):**

| Think of an approach .... | 0.8 |
|---|---|
| Analyse this problem .... | 0.75 |
| Solve the given problem.. | 0.6 |
| Lets approach this logically Lets think step by step .... | 0.85 0.4 |


**Table (Page 7):**

| Task APE InsZero PB EvoP Instinct PW | Instinct PW |
|---|---|
| LLM:GPT3.5Turbo Zero-shotsetting | One-shotsetting |
| antonyms 0.64 0.83 0.80 0.80 0.85 0.56 auto-categorization 0.25 0.26 0.22 0.26 0.25 0.28 causeandeffect 0.57 0.81 0.75 0.83 0.59 0.88 commonconcept 0.07 0.09 0.10 0.12 0.21 0.10 diff 0.67 0.69 1.00 1.00 1.00 1.00 informaltoformal 0.57 0.53 0.58 0.62 0.55 0.62 letterslist 1.00 0.59 0.99 1.00 1.00 0.95 negation 0.75 0.78 0.77 0.79 0.82 0.73 objectcounting 0.36 0.36 0.34 0.12 0.34 0.60 oddoneout 0.63 0.61 0.64 0.65 0.70 0.78 orthographystartswith 0.46 0.51 0.56 0.60 0.67 0.75 rhymes 0.16 1.00 0.54 0.61 1.00 0.89 secondwordletter 0.75 0.43 0.57 0.41 0.10 0.93 sentencesimilarity 0.00 0.00 0.01 0.28 0.14 0.29 sum 0.67 1.00 1.00 1.00 1.00 1.00 synonyms 0.36 0.28 0.36 0.14 0.31 0.37 taxonomyanimal 0.35 0.72 0.72 0.72 0.86 0.92 wordsorting 0.33 0.31 0.56 0.52 0.51 0.56 wordunscrambling 0.44 0.55 0.61 0.60 0.63 0.52 | 0.85 0.78 0.30 0.40 0.63 0.92 0.25 0.19 1.00 1.00 0.52 0.56 1.00 1.00 0.86 0.84 0.36 0.52 0.63 0.92 0.67 0.92 0.75 0.90 0.24 0.99 0.16 0.30 1.00 1.00 0.37 0.44 0.90 0.94 0.62 0.74 0.58 0.58 |
| #bestperformingtasks 1 2 3 4 8 13 | 7 16 |


**Table (Page 15):**

| Hyper- parameter | Description | DefaultValue |
|---|---|---|
| mutate_refine rounds mutate_rounds style_variation min_example correct_count max_example count max_seq_iter few_shot_count ex_critique synthesize inst_critique synthesize reasoning + validation intent + per- sona | Number of rounds of call to MutateComponent fol- lowedbyrefinementoverbestpromptamonggenerated byMutateComponentinpreviousstep. NumberoftimesMutateComponentwouldbecalled. NumberofvariationsMutateComponentgeneratesin a single call. i.e. one variation corresponding to each thinkingstyleprovided. Minimum number of questions the ScoringComponent should answer correctly foraprompttogetqualifiedfornextstage. Maximum number of attempts/questions the ScoringComponent would be asked asked to answer. NumberofroundsofcalltoCritiqueComponentfol- lowedbycalltoSynthesizeComponent Total number of few shot examples to be provided in prompt. NumberofLLMcallsmadebyCritiqueComponent forgettingcritiqueforimprovingexamplespassedasfew- shots. Number of LLM calls made by SynthesizeComponent to generate synthetic examples. NumberofLLMcallsmadebyCritiqueComponent for getting critique for improving instruction passed as few-shots. Number of LLM calls made by SynthesizeComponent to created improved versionofinstruction. Number of LLM calls made by ReasoningComponent and ValidateComponentrespectively. NumberofLLMcallsmadetogetkeywordsthatexpress theintentandtogenerateexpertpersonarespectively. | 3 3 3 3 6 5 DefinedinTa- ble10 1 1 1 1 2 2 |


**Table (Page 16):**

| Task | Instinct PromptWizard |
|---|---|
| LLM:GPT4 | Zero-shotsetting |
| antonyms autocategorization causeandeffect commonconcept diff informaltoformal letterslist negation objectcounting oddoneout orthographystartswith rhymes secondwordletter sentencesimilarity sum synonyms taxonomyanimal wordsorting wordunscrambling | 0.79 0.77 0.3 0.38 0.96 0.88 0.2 0.15 1 1 0.6 0.75 1 1 0.7 0.85 0.6 0.82 0.54 0.87 0.75 0.92 1 0.88 0.57 0.97 0.3 0.43 0.99 1 0.3 0.42 0.9 1 0.5 0.65 0.54 0.77 |
| #bestperformingtasks | 6 15 |


**Table (Page 17):**

|  | Instinct | PromptWizard |
|---|---|---|
| Dataset | APICalls IOTokens | APICalls IOTokens |
| antonyms auto-categorization causeandeffect commonconcept diff informaltoformal letterslist negation objectcounting oddoneout orthographystartswith rhymes secondwordletter sentencesimilarity sum synonyms taxonomyanimal wordsorting wordunscrambling | 2200 39 1740 86 1352 61 639 94 1820 58 880 90 2240 58 2180 60 1340 69 840 50 1800 82 1920 41 1840 48 2140 78 2180 66 2100 51 1900 72 1680 110 2060 58 | 69 334 69 341 69 390 69 386 69 381 69 271 69 256 69 305 69 470 69 372 69 339 69 391 69 257 69 626 69 367 69 452 69 225 69 426 69 306 |
| Average | 1729 67 | 69 362 |


**Table (Page 21):**

| <the optimized prompt instruction> |
|---|
|  |
| Analyze the given real-world mathematical problem step-by-step, |
| identifying key information, relationships between different pieces |
| of data, and the context. Understand the structure of the problem, |
| whether it involves a sequence of events or a comparison between |
| different quantities. Keep track of all variables and quantities |
| mentioned in the problem. Use appropriate mathematical operations and |
| formulas, including addition, subtraction, multiplication, division, |
| and more complex operations if required. Understand and handle |
| indirect relationships and different units of measurement. Apply |
| specific rules or conditions given in the problem. Make assumptions |
| when information is not explicitly provided. Consider the order of |
| operations when performing calculations. Understand the structure and |
| properties of the data in the problem. Finally, verify your answer |
| against the original problem to ensure it is logical and accurate. |


**Table (Page 21):**

| <synthesized examples + reasoning chain> |
|---|
|  |
| [Question] Tim rides his bike back and forth to work for each of his 5 |
| workdays. His work is 20 miles away. He also goes for a weekend |
| bike ride of 200 miles. If he can bike at 25 mph how much time |
| does he spend biking a week? |
| [Answer] 1. Identify the key pieces of information: Tim bikes to work and |
| back for 5 days, his work is 20 miles away, he goes for a 200-mile |
| bike ride on the weekend, and his biking speed is 25 mph. |
| 2. Understand that the problem involves a sequence of events: Tim’s daily |
| commute to work and back, and his weekend bike ride. |
| 3. Calculate the total distance Tim bikes to work and back in a week: 20 |
| miles to work * 2 (for the return trip) = 40 miles per day. Multiply |
| this by 5 days: 40 miles/day * 5 days = 200 miles. |
| 4. Add the distance of Tim’s weekend bike ride to the total distance he |
| bikes to work: 200 miles (work) + 200 miles (weekend) = 400 miles. |


**Table (Page 23):**

| 5. Understand that the problem asks for the total time Tim spends biking |
|---|
| in a week, and that time can be calculated by dividing distance by |
| speed. |
| 6. Calculate the total time Tim spends biking in a week: 400 miles / 25 |
| mph = 16 hours. |
| 7. Verify that the answer is logical: Tim spends 16 hours biking in a |
| week, which is reasonable given the distances and speed provided. |
| 8. The final answer is 16 hours. <ANS_START>16<ANS_END> |
|  |
|  |
| [Question] Tobias is buying a new pair of shoes that costs $95. He has |
| been saving up his money each month for the past three months. He |
| gets a $5 allowance a month. He also mows lawns and shovels driveways |
| . He charges $15 to mow a lawn and $7 to shovel. After buying the |
| shoes, he has $15 in change. If he mows 4 lawns, how many driveways |
| did he shovel? |
| [Answer] 1. Identify the total amount of money Tobias had before buying |
| the shoes. This is given by the cost of the shoes plus the change he |
| has left, which is $95 + $15 = $110. |
| 2. Calculate the total amount of money Tobias earned from his allowance. |
| He gets $5 a month and has been saving for three months, so he earned |
| $5 * 3 = $15 from his allowance. |
| 3. Calculate the total amount of money Tobias earned from mowing lawns. |
| He charges $15 to mow a lawn and he mowed 4 lawns, so he earned $15 * |
| 4 = $60 from mowing lawns. |
| 4. Subtract the money Tobias earned from his allowance and mowing lawns |
| from the total amount of money he had before buying the shoes. This |
| will give us the amount of money he earned from shoveling driveways. |
| So, $110 - $15 - $60 = $35 is the amount he earned from shoveling |
| driveways. |
| 5. Finally, divide the total amount of money Tobias earned from shoveling |
| driveways by the amount he charges to shovel one driveway. This will |
| give us the number of driveways he shoveled. So, $35 / $7 = 5 |
| driveways. <ANS_START>5<ANS_END> |
|  |
| [Question] Bella bought stamps at the post office. Some of the stamps had |
| a snowflake design, some had a truck design, and some had a rose |
| design. Bella bought 11 snowflake stamps. She bought 9 more truck |
| stamps than snowflake stamps, and 13 fewer rose stamps than truck |
| stamps. How many stamps did Bella buy in all? |
| [Answer] 1. Identify the quantities given in the problem: Bella bought 11 |
| snowflake stamps. |
| 2. Understand the relationships between the different types of stamps: |
| She bought 9 more truck stamps than snowflake stamps, and 13 fewer |
| rose stamps than truck stamps. |
| 3. Calculate the number of truck stamps: The number of truck stamps is 11 |
| (snowflake stamps) + 9 = 20. |
| 4. Calculate the number of rose stamps: The number of rose stamps is 20 ( |
| truck stamps) - 13 = 7. |
| 5. Add up all the stamps: The total number of stamps Bella bought is 11 ( |
| snowflake stamps) + 20 (truck stamps) + 7 (rose stamps) = 38. |
| 6. Verify the answer: Check that the total number of stamps (38) matches |
| the sum of the individual quantities of each type of stamp (11 |
| snowflake stamps, 20 truck stamps, 7 rose stamps). The answer is |
| correct. <ANS_START>38<ANS_END> |
|  |
| [Question] Tina makes $18.00 an hour. If she works more than 8 hours per |
| shift, she is eligible for overtime, which is paid by your hourly |
| wage + 1/2 your hourly wage. If she works 10 hours every day for 5 |
| days, how much money does she make? |
| [Answer] 1. Identify the key information: Tina’s hourly wage is \$18.00, |
| she works 10 hours a day for 5 days, and overtime is calculated as |
| the hourly wage plus half the hourly wage for hours worked over 8 |
| hours in a shift. |


**Table (Page 24):**

| 2. Calculate the regular pay: Tina works 10 hours a day, but only 8 hours |
|---|
| are considered regular hours. So, for 5 days, she works 8 hours/day |
| * 5 days = 40 hours. |
| 3. Multiply the regular hours by the hourly wage to get the regular pay: |
| 40 hours * $18.00/hour = $720.00. |
| 4. Calculate the overtime hours: Tina works 10 hours a day, so she has 10 |
| hours/day - 8 hours/day = 2 hours/day of overtime. Over 5 days, this |
| is 2 hours/day * 5 days = 10 hours of overtime. |
| 5. Calculate the overtime wage: The overtime wage is the hourly wage plus |
| half the hourly wage, so $18.00/hour + 0.5 * $18.00/hour = $27.00/ |
| hour. |
| 6. Multiply the overtime hours by the overtime wage to get the overtime |
| pay: 10 hours * $27.00/hour = $270.00. |
| 7. Add the regular pay and the overtime pay to get the total pay: $720.00 |
| + $270.00 = $990.00. |
| 8. Verify the answer: Tina makes $990.00 if she works 10 hours a day for |
| 5 days, with overtime pay for hours worked over 8 hours in a shift. |
| This is logical and matches the original problem. <ANS_START>990< |
| ANS_END> |
|  |
| [Question] Samantha’s last name has three fewer letters than Bobbie’s |
| last name. If Bobbie took two letters off her last name, she would |
| have a last name twice the length of Jamie’s. Jamie’s full name is |
| Jamie Grey. How many letters are in Samantha’s last name? |
| [Answer] 1. Start by identifying the key pieces of information from the |
| problem: Samantha’s last name has three fewer letters than Bobbie’s |
| last name, and if Bobbie took two letters off her last name, she |
| would have a last name twice the length of Jamie’s. Jamie’s full name |
| is Jamie Grey. |
| 2. From the information given, we know that Jamie’s last name is Grey, |
| which has 4 letters. |
| 3. Since Bobbie’s last name, after removing two letters, is twice the |
| length of Jamie’s last name, we can set up the equation: (Bobbie’s |
| last name length - 2) = 2 * Jamie’s last name length. |
| 4. Substituting the known value of Jamie’s last name length (4) into the |
| equation gives: (Bobbie’s last name length - 2) = 2 * 4, which |
| simplifies to Bobbie’s last name length - 2 = 8. |
| 5. Solving for Bobbie’s last name length gives: Bobbie’s last name length |
| = 8 + 2 = 10. |
| 6. We know that Samantha’s last name has three fewer letters than Bobbie’ |
| s last name. So, we can set up the equation: Samantha’s last name |
| length = Bobbie’s last name length - 3. |
| 7. Substituting the known value of Bobbie’s last name length (10) into |
| the equation gives: Samantha’s last name length = 10 - 3. |
| 8. Solving for Samantha’s last name length gives: Samantha’s last name |
| length = 7. |
| 9. Therefore, Samantha’s last name has 7 letters. <ANS_START>7<ANS_END> |


**Table (Page 24):**

| <human intent> |
|---|
|  |
| Mathematical Reasoning, Multi-step Problem Solving, Basic Arithmetic |
| Operations, Data Analysis, Solution Verification |
|  |
| <expert persona> |
|  |
| You are a mathematics educator with a deep understanding of elementary |
| and middle school mathematics. You are experienced in teaching multi- |
| step problem-solving techniques and have a knack for breaking down |
| complex problems into manageable steps. Your expertise lies in basic |
| arithmetic operations such as addition, subtraction, multiplication, |
| and division. You can provide clear, step-by-step solutions to |
| mathematical problems that require multi-step reasoning. You are |
| patient and thorough, ensuring that each step is clearly explained |
| and understood. Your ability to simplify complex problems and guide |


**Table (Page 25):**

| students through the problem-solving process makes you an excellent |
|---|
| resource for answering school-grade mathematical questions. |
|  |
| <prompt guidelines for desired output format> |
|  |
| You need to answer each of the questions separately. Arabic numeral |
| should be at the end in the format Wrap your only the final answer, |
| without reason for each question separately between <ANS_START> and < |
| ANS_END> tags. |


**Table (Page 25):**

| <the optimized prompt instruction> |
|---|
|  |
| Carefully examine the provided text and determine if it constitutes hate |
| speech. Hate speech is defined as language that is derogatory, |
| offensive, or discriminatory towards a specific group of people based |
| on their race, gender, or other characteristics, with the intent to |
| harm or degrade. Even if the statement appears factual or sarcastic, |
| if it uses aggressive language or personal attacks aimed at a |
| specific group, it should be classified as hate speech. |


**Table (Page 25):**

| <synthesized examples + reasoning chain> |
|---|
|  |
| [Question] While I appreciate the hard work of some immigrants, others |
| are just here to exploit our system and take our jobs. |
| [Answer] 1. Start by reading the provided text to understand its content. |
| 2. The task requires identifying if the text contains hate speech. |
| According to the task description, hate speech is language that is |
| derogatory, offensive, or discriminatory towards a specific group of |
| people based on their race, gender, or other characteristics, with |
| the intent to harm or degrade. |
| 3. The text states, "While I appreciate the hard work of some immigrants, |
| others are just here to exploit our system and take our jobs." |
| 4. This statement is making a generalization about a specific group of |
| people, in this case, immigrants. It suggests that some immigrants |
| are exploiting the system and taking jobs, which is a negative |
| stereotype. |
| 5. Even though the text acknowledges the hard work of some immigrants, it |
| still uses derogatory language towards others, implying they are |
| here to exploit the system. |
| 6. This statement can be seen as offensive and discriminatory towards |
| immigrants, as it negatively stereotypes them and can potentially |
| harm or degrade them. |
| 7. Therefore, according to the task description and instruction, this |
| text can be classified as hate speech.\newline |
| 8. As per the task instruction, if the text contains hate speech, the |
| output should be 1. |
| 9. Hence, the final answer is 1. <ANS_START>1<ANS_END> |
|  |
| [Question] I’ve noticed that female politicians are more corrupt and only |
| care about their own interests.\newline |
| [Answer] 1. Start by reading the provided text: "I’ve noticed that female |
| politicians are more corrupt and only care about their own interests |
| ." |
| 2. Identify the subject of the text: The subject is "female politicians." |
| 3. Analyze the language used in the text: The language used is derogatory |
| and offensive, as it generalizes all female politicians as being " |
| more corrupt" and only caring about their own interests. |
| 4. Determine if the language is discriminatory: The language |
| discriminates against a specific group, in this case, female |
| politicians, by making a negative generalization about them. |


**Table (Page 26):**

| 5. Check if the language has the intent to harm or degrade: The language |
|---|
| used seems to degrade the reputation of female politicians by |
| portraying them as corrupt and self-interested. |
| 6. Based on the task description and instruction, the text is considered |
| hate speech if it is derogatory, offensive, or discriminatory towards |
| a specific group of people with the intent to harm or degrade. |
| 7. Since the text meets all these criteria, it is classified as hate |
| speech. |
| 8. According to the task instruction, if the text contains hate speech, |
| the output should be 1. |
| 9. Therefore, the final answer is 1. <ANS_START>1<ANS_END> |
|  |
| [Question] I don’t get why we have to accept people who choose to be |
| transgender. It’s unnatural and against our values. |
| [Answer] 1. Start by reading the provided text. |
| 2. Identify the subject of the text. In this case, the subject is "people |
| who choose to be transgender." |
| 3. Analyze the language used in the text. The text uses phrases like "It’ |
| s unnatural" and "against our values," which are derogatory and |
| offensive. |
| 4. Determine if the language is aimed at a specific group. Here, the |
| language is targeted towards transgender people, a specific group. |
| 5. Check if the language is intended to harm or degrade the specific |
| group. The text implies that being transgender is unnatural and |
| against societal values, which can be seen as an attempt to degrade |
| or harm the transgender community.\newline |
| 6. Since the text uses offensive language against a specific group with |
| the intent to harm or degrade, it can be classified as hate speech. |
| 7. Therefore, the correct answer is 1, indicating that the text contains |
| hate speech. <ANS_START>1<ANS_END> |


**Table (Page 26):**

| <human intent> |
|---|
|  |
| Text Analysis, Hate Speech Identification, Discriminatory Language |
| Detection, Offensive Content Recognition, Derogatory Language |
| Classification |
|  |
| <expert persona> |
|  |
| You are a machine learning engineer with a specialization in natural |
| language processing and text analysis. You have developed and trained |
| algorithms to detect and classify different types of text, including |
| hate speech. Your algorithm can analyze the given text, identify |
| patterns, and determine whether it contains hate speech or not. You |
| are equipped with a deep understanding of the nuances of language, |
| and you can differentiate between offensive language, strong |
| criticism, and actual hate speech. Your algorithm is designed to be |
| fair and unbiased, and it respects the principles of freedom of |
| speech while also recognizing the harm caused by hate speech. Your |
| expertise in text analysis and machine learning is highly valuable in |
| moderating online content and creating a safer digital environment. |
|  |
| <prompt guidelines for desired output format> |
| You need to answer each of the questions separately with 1 if its a hate |
| speech and 0 if its not a hate speech. Wrap your only the final |
| answer, without reason for each question separately between < |
| ANS_START> and <ANS_END> tags. |


**Table (Page 26):**

| <the optimized prompt instruction> |
|---|
|  |
| Carefully read the abstract and identify the key points that directly |
| address the biomedical research question. Based on these key points, |


**Table (Page 27):**

| provide a clear and concise answer in a "Yes" or "No" format, |
|---|
| followed by a brief explanation that correlates the research question |
| with the findings in the abstract. |


**Table (Page 27):**

| <synthesized examples + reasoning chain> |
|---|
|  |
| [Question] Does the process of photosynthesis under varying light |
| intensities and temperature play a significant role in the growth of |
| different species of algae?\newline |
| [Abstract] : Photosynthesis is a process used by plants and other |
| organisms to convert light energy into chemical energy that can later |
| be released to fuel the organisms’ activities. This study |
| investigates the impact of varying light intensities and temperature |
| on the photosynthetic process in different species of algae. The |
| algae were exposed to different light intensities and temperatures, |
| and their growth rate was monitored over a period of time. The |
| results showed a direct correlation between light intensity, |
| temperature and the growth rate of algae. |
| [Answer] 1. The question asks whether the process of photosynthesis under |
| varying light intensities and temperature plays a significant role |
| in the growth of different species of algae. |
| 2. The abstract provides information about a study that investigates the |
| impact of varying light intensities and temperature on the |
| photosynthetic process in different species of algae. |
| 3. The abstract mentions that the algae were exposed to different light |
| intensities and temperatures, and their growth rate was monitored |
| over a period of time.\newline |
| 4. The results of the study, as mentioned in the abstract, showed a |
| direct correlation between light intensity, temperature and the |
| growth rate of algae. |
| 5. This direct correlation indicates that the process of photosynthesis |
| under varying light intensities and temperature does indeed play a |
| significant role in the growth of different species of algae. |
| 6. Therefore, based on the information provided in the abstract, the |
| answer to the question is "Yes". <ANS_START>yes<ANS_END> |
|  |
|  |
| [Question] Is the use of antiviral drugs effective in treating influenza, |
| a common viral infection? |
| [Abstract] : Antiviral drugs are medicines used to prevent and treat |
| viral infections. Influenza, on the other hand, is a viral infection. |
| This study investigates the effectiveness of antiviral drugs in |
| treating influenza. The study involved patients suffering from |
| influenza who were treated with antiviral drugs. The results showed |
| significant improvement in the condition of the patients. |
| [Answer] 1. The question asks about the effectiveness of antiviral drugs |
| in treating influenza, a common viral infection. |
| 2. The abstract provides information about a study that investigates the |
| effectiveness of antiviral drugs in treating influenza. |
| 3. The study involved patients suffering from influenza who were treated |
| with antiviral drugs.\newline |
| 4. The results of the study showed significant improvement in the |
| condition of the patients after they were treated with antiviral |
| drugs. |
| 5. Therefore, based on the results of the study mentioned in the abstract |
| , it can be concluded that the use of antiviral drugs is effective in |
| treating influenza. |
| 6. Hence, the answer to the question is "Yes". <ANS_START>yes<ANS_END> |
|  |
|  |
| [Question] Are intensive care units more beneficial than general wards |
| for the treatment of severe pneumonia in children with underlying |
| health conditions? |
| [Abstract] : Pneumonia is a common illness in children that can become |
| severe if not properly treated. Intensive care units (ICUs) provide |


**Table (Page 28):**

| specialized care for patients with severe or life-threatening |
|---|
| illnesses. This study examines the impact of ICU treatment on |
| children with severe pneumonia and underlying health conditions. The |
| study compared the recovery rates of children treated in ICUs with |
| those treated in general wards. The results showed a higher recovery |
| rate in children with underlying health conditions treated in ICUs.\ |
| newline |
| [Answer] 1. The question asks whether intensive care units (ICUs) are |
| more beneficial than general wards for the treatment of severe |
| pneumonia in children with underlying health conditions. |
| 2. The abstract provides information about a study that examined the |
| impact of ICU treatment on children with severe pneumonia and |
| underlying health conditions.\newline |
| 3. The study compared the recovery rates of children treated in ICUs with |
| those treated in general wards. |
| 4. The results of the study showed a higher recovery rate in children |
| with underlying health conditions treated in ICUs. |
| 5. Therefore, based on the results of the study presented in the abstract |
| , the answer to the question is "Yes". ICUs are more beneficial than |
| general wards for the treatment of severe pneumonia in children with |
| underlying health conditions. <ANS_START>yes<ANS_END> |
|  |
| [Question] Is the blood glucose level a more reliable marker than HbA1c |
| for diagnosing Diabetes? |
| [Abstract] : Diabetes is a chronic disease that affects the body’s |
| ability to process sugar. Blood glucose levels and HbA1c are commonly |
| used markers for diagnosing diabetes. This study investigates the |
| reliability of blood glucose levels and HbA1c as markers for |
| diagnosing Diabetes. The study involved patients diagnosed with |
| Diabetes and their blood glucose and HbA1c levels were measured. The |
| results showed a significant correlation between high blood glucose |
| levels and Diabetes diagnosis, but not with HbA1c levels. |
| [Answer] 1. The question asks whether blood glucose level is a more |
| reliable marker than HbA1c for diagnosing Diabetes.\newline |
| 2. The abstract provides information about a study that investigates the |
| reliability of blood glucose levels and HbA1c as markers for |
| diagnosing Diabetes. |
| 3. The abstract mentions that the study involved patients diagnosed with |
| Diabetes and their blood glucose and HbA1c levels were measured. |
| 4. The key point in the abstract is the results of the study, which |
| showed a significant correlation between high blood glucose levels |
| and Diabetes diagnosis, but not with HbA1c levels. |
| 5. This indicates that blood glucose levels are a more reliable marker |
| for diagnosing Diabetes than HbA1c levels, according to the study. |
| 6. Therefore, based on the information provided in the abstract, the |
| answer to the question is "Yes". <ANS_START>yes<ANS_END> |
|  |
|  |
| [Question] Can regular strength training reduce the risk of osteoporosis |
| in adults over 60? |
| [Abstract] : Osteoporosis is a major health issue globally, especially in |
| adults over 60. Regular strength training is known to have various |
| health benefits, including improving bone health. This study |
| investigates the impact of regular strength training on the risk of |
| osteoporosis in adults over 60. The study involved participants who |
| engaged in regular strength training and their bone health was |
| monitored over a period of time. The results showed a lower incidence |
| of osteoporosis in participants who engaged in regular strength |
| training. |
| [Answer] 1. The question asks whether regular strength training can |
| reduce the risk of osteoporosis in adults over 60. |
| 2. The abstract provides information about a study that investigates the |
| impact of regular strength training on the risk of osteoporosis in |
| adults over 60. |


**Table (Page 29):**

| 3. The abstract mentions that regular strength training is known to have |
|---|
| various health benefits, including improving bone health. |
| 4. The study involved participants who engaged in regular strength |
| training and their bone health was monitored over a period of time. |
| 5. The results of the study, as mentioned in the abstract, showed a lower |
| incidence of osteoporosis in participants who engaged in regular |
| strength training. |
| 6. Therefore, based on the results of the study mentioned in the abstract |
| , it can be concluded that regular strength training can reduce the |
| risk of osteoporosis in adults over 60. |
| 7. Hence, the answer to the question is "Yes". <ANS_START>yes<ANS_END> |


**Table (Page 29):**

| <human intent> |
|---|
| Biomedical Research Understanding, Abstract Analysis, Key Point |
| Identification, Concise Answering, Explanation Correlation |
|  |
| <expert persona> |
|  |
| You are a biomedical researcher with a deep understanding of medical and |
| scientific literature. You have a strong background in reading and |
| interpreting scientific abstracts, and you are skilled at extracting |
| key information from complex texts. You can accurately answer |
| biomedical research questions based on the information provided in |
| the corresponding abstracts. Your expertise in biomedical research |
| allows you to understand the nuances and implications of the findings |
| presented in the abstracts, and you can provide clear, concise, and |
| accurate answers to the questions. Your ability to critically analyze |
| and interpret scientific literature makes you an invaluable resource |
| in the field of biomedical research. |
|  |
| <prompt guidelines for desired output format> |
|  |
| You need to answer each of the questions separately with yes/ no/ maybe. |
| Wrap your only the final answer, without reason for each question |
| separately between <ANS_START> and <ANS_END> tags. |


**Table (Page 29):**

| <the optimized prompt instruction> |
|---|
|  |
| Analyze the patient’s age, symptoms, duration and onset of symptoms, |
| history of present illness, lifestyle factors, physical examination |
| findings, and any diagnostic test results presented in the Medical |
| Licensing Examination question. Use your knowledge of medicine to |
| identify the most likely diagnosis or appropriate treatment. Consider |
| the progression, severity, and duration of the patient’s symptoms in |
| relation to the answer options. Eliminate incorrect answer options |
| based on your medical knowledge and ensure your final choice is the |
| most appropriate given the specifics of the question. Validate your |
| answer by ensuring it aligns with all the information provided in the |
| question, including the patient’s age, lifestyle factors, and |
| specific diagnostic test results. |


**Table (Page 29):**

| <synthesized examples + reasoning chain> |
|---|
|  |
| [Question] A 50-year-old man with a history of hypertension and type 2 |
| diabetes presents with a 3-day history of chest pain radiating to the |
| left arm. He also reports shortness of breath and fatigue. Physical |
| examination reveals a blood pressure of 150/90 mmHg, heart rate of |
| 90/min, and an irregular pulse. An ECG shows ST-segment elevation in |
| leads II, III, and aVF. Which of the following is the most |
| appropriate initial treatment? |
| Options: |
| A: Aspirin and clopidogrel |


**Table (Page 30):**

| B: Metformin |
|---|
| C: Lisinopril |
| D: Atorvastatin |
|  |
| [Answer] 1. Start by analyzing the patient’s age, symptoms, and medical |
| history. The patient is a 50-year-old man with a history of |
| hypertension and type 2 diabetes. He presents with chest pain |
| radiating to the left arm, shortness of breath, and fatigue. These |
| symptoms are indicative of a cardiovascular event. |
| 2. Consider the physical examination findings. The patient has a blood |
| pressure of 150/90 mmHg, heart rate of 90/min, and an irregular pulse |
| . These findings further support the likelihood of a cardiovascular |
| event. |
| 3. Review the diagnostic test results. The ECG shows ST-segment elevation |
| in leads II, III, and aVF. This is a classic sign of an ST-segment |
| elevation myocardial infarction (STEMI), a type of heart attack. |
| 4. Given the diagnosis of STEMI, consider the most appropriate initial |
| treatment. The options are Aspirin and clopidogrel (A), Metformin (B) |
| , Lisinopril (C), and Atorvastatin (D). |
| 5. Eliminate incorrect answer options based on medical knowledge. |
| Metformin (B) is a medication for diabetes, Lisinopril (C) is an |
| antihypertensive medication, and Atorvastatin (D) is a cholesterol- |
| lowering medication. While these medications may be part of the |
| patient’s long-term management, they are not the most appropriate |
| initial treatment for a STEMI. |
| 6. Aspirin and clopidogrel (A) are antiplatelet medications. They work by |
| preventing blood clots, which is crucial in the initial management |
| of a STEMI to restore blood flow to the heart muscle. |
| 7. Therefore, the most appropriate initial treatment for this patient, |
| given his symptoms, physical examination findings, and ECG results, |
| is Aspirin and clopidogrel (A). This aligns with all the information |
| provided in the question and is the most appropriate given the |
| specifics of the question. |
| 8. Validate the final choice (A) as it is the most appropriate initial |
| treatment for a patient presenting with a STEMI. <ANS_START>A<ANS_END |
| > |
|  |
|  |
| [Question] A 6-month-old girl is brought to the physician by her mother |
| because of a 2-day history of fever and irritability. She also has a |
| rash on her cheeks. Physical examination reveals a temperature of |
| 38.5C (101.3F), a heart rate of 120/min, and a respiratory rate of |
| 30/min. Examination of the skin shows erythema of the cheeks with |
| sparing of the nasal bridge and perioral area. Which of the following |
| is the most likely diagnosis? |
| Options: |
| A: Measles |
| B: Fifth disease |
| C: Roseola |
| D: Scarlet fever |
|  |
| [Answer] 1. Start by analyzing the patient’s age, symptoms, duration and |
| onset of symptoms, and physical examination findings. The patient is |
| a 6-month-old girl with a 2-day history of fever and irritability. |
| She also has a rash on her cheeks. Her temperature is 38.5C (101.3F), |
| a heart rate of 120/min, and a respiratory rate of 30/min. The skin |
| examination shows erythema of the cheeks with sparing of the nasal |
| bridge and perioral area. |
| 2. Use your medical knowledge to identify the most likely diagnosis. The |
| symptoms presented are indicative of a viral exanthem, a rash that |
| appears due to a viral infection. |
| 3. Consider the answer options. The options are Measles, Fifth disease, |
| Roseola, and Scarlet fever. All of these are diseases that can |
| present with a rash. |


**Table (Page 31):**

| 4. Eliminate incorrect answer options based on your medical knowledge. |
|---|
| Measles typically presents with a rash that starts at the hairline |
| and moves down, along with Koplik spots in the mouth, which are not |
| mentioned in the question. Scarlet fever typically presents with a |
| sandpaper-like rash and a strawberry tongue, which are also not |
| mentioned. Roseola typically presents with a high fever that suddenly |
| drops as a rash appears, which does not match the patient’s symptoms |
| . |
| 5. The remaining option is Fifth disease, also known as erythema |
| infectiosum. This disease is common in children and presents with a " |
| slapped cheek" rash, fever, and irritability, which aligns with the |
| patient’s symptoms. |
| 6. Validate your answer by ensuring it aligns with all the information |
| provided in the question. The patient’s age, symptoms, and physical |
| examination findings all align with a diagnosis of Fifth disease. |
| 7. Therefore, the correct answer is B: Fifth disease. <ANS_START>B< |
| ANS_END> |
|  |
|  |
| [Question] A 70-year-old man presents with a 1-year history of |
| progressive memory loss, difficulty finding words, and getting lost |
| in familiar places. Neurologic examination shows impaired recall and |
| disorientation to time and place. MRI of the brain shows cortical |
| atrophy and enlarged ventricles. Which of the following is the most |
| likely diagnosis? |
| Options: |
| A: Alzheimer’s disease |
| B: Vascular dementia |
| C: Lewy body dementia |
| D: Frontotemporal dementia |
|  |
| [Answer] 1. Start by analyzing the patient’s age, symptoms, duration and |
| onset of symptoms, and the results of the physical examination and |
| diagnostic tests. The patient is a 70-year-old man with a 1-year |
| history of progressive memory loss, difficulty finding words, and |
| getting lost in familiar places. The neurologic examination shows |
| impaired recall and disorientation to time and place. The MRI of the |
| brain shows cortical atrophy and enlarged ventricles. |
| 2. Consider the progression, severity, and duration of the patient’s |
| symptoms. The symptoms have been progressing over a year, which |
| indicates a chronic condition. |
| 3. Use your medical knowledge to identify the most likely diagnosis. The |
| symptoms of progressive memory loss, difficulty finding words, and |
| getting lost in familiar places, along with impaired recall and |
| disorientation to time and place, are characteristic of a |
| neurodegenerative disease. |
| 4. Look at the answer options and eliminate incorrect ones based on your |
| medical knowledge. Vascular dementia (Option B) typically presents |
| with stepwise deterioration of cognitive function, which is not the |
| case here. Lewy body dementia (Option C) is usually accompanied by |
| visual hallucinations, parkinsonism, or fluctuating cognition, none |
| of which are mentioned in the question. Frontotemporal dementia ( |
| Option D) often presents with changes in personality and behavior, |
| which is also not mentioned in the question. |
| 5. The remaining option is Alzheimer’s disease (Option A), which is a |
| neurodegenerative disease that commonly presents with progressive |
| memory loss, difficulty finding words, and getting lost in familiar |
| places, especially in older adults. The MRI findings of cortical |
| atrophy and enlarged ventricles are also consistent with Alzheimer’s |
| disease. |
| 6. Validate your answer by ensuring it aligns with all the information |
| provided in the question. Alzheimer’s disease fits with the patient’s |
| age, the chronic and progressive nature of the symptoms, the |
| neurologic examination findings, and the MRI results. |


**Table (Page 32):**

| 7. Therefore, the correct answer is A: Alzheimer’s disease. <ANS_START>A< |
|---|
| ANS_END> |
|  |
|  |
| [Question] A 35-year-old woman presents with a 2-week history of severe |
| headache, fever, and photophobia. She also reports a rash on her |
| lower extremities. Physical examination reveals a temperature of 38.2 |
| C (100.8F), a heart rate of 110/min, and a petechial rash on her |
| lower extremities. Lumbar puncture shows increased white blood cells |
| with a predominance of lymphocytes, increased protein, and normal |
| glucose. Which of the following is the most appropriate |
| pharmacotherapy? |
| Options: |
| A: Ceftriaxone and vancomycin |
| B: Acyclovir |
| C: Amphotericin B |
| D: Doxycycline |
|  |
| [Answer] 1. Start by analyzing the patient’s symptoms: severe headache, |
| fever, photophobia, and a petechial rash on her lower extremities. |
| These symptoms suggest a systemic infection, possibly involving the |
| central nervous system given the presence of headache and photophobia |
| . |
| 2. Consider the patient’s age and duration of symptoms. A 35-year-old |
| woman with a 2-week history of these symptoms suggests an acute |
| infection rather than a chronic condition. |
| 3. Review the physical examination findings and diagnostic test results. |
| The patient has a fever and tachycardia, further supporting the |
| presence of a systemic infection. The lumbar puncture results show |
| increased white blood cells with a predominance of lymphocytes, |
| increased protein, and normal glucose. These findings are indicative |
| of viral meningitis. |
| 4. Evaluate the answer options in relation to the most likely diagnosis. |
| Viral meningitis is typically caused by enteroviruses, herpes simplex |
| virus, or arboviruses. |
| 5. Option A (Ceftriaxone and vancomycin) is used to treat bacterial |
| meningitis, which is not consistent with the lumbar puncture results. |
| Eliminate this option. |
| 6. Option B (Acyclovir) is an antiviral medication used to treat |
| infections caused by herpes viruses, including herpes simplex virus |
| meningitis. This option aligns with the diagnosis. |
| 7. Option C (Amphotericin B) is an antifungal medication, which is not |
| consistent with the diagnosis of viral meningitis. Eliminate this |
| option. |
| 8. Option D (Doxycycline) is an antibiotic used to treat bacterial |
| infections, including certain types of bacterial meningitis, but it |
| is not the first-line treatment for viral meningitis. Eliminate this |
| option. |
| 9. Validate the final choice (Option B: Acyclovir) by ensuring it aligns |
| with all the information provided in the question, including the |
| patient’s age, symptoms, physical examination findings, and specific |
| diagnostic test results. |
| 10. Therefore, the correct answer is B: Acyclovir. <ANS_START>B<ANS_END> |
|  |
|  |
| [Question] A 40-year-old man with a history of alcohol abuse presents |
| with a 1-day history of severe abdominal pain, nausea, and vomiting. |
| Physical examination reveals a distended abdomen, decreased bowel |
| sounds, and tenderness to palpation in the upper abdomen. Laboratory |
| tests show an elevated serum amylase and lipase. Which of the |
| following is the most likely diagnosis? |
| Options: |
| A: Acute pancreatitis |
| B: Peptic ulcer disease |
| C: Gastric cancer |


**Table (Page 33):**

| D: Gastroenteritis |
|---|
|  |
| [Answer] 1. Start by analyzing the patient’s age, symptoms, duration and |
| onset of symptoms, history of present illness, lifestyle factors, |
| physical examination findings, and any diagnostic test results |
| presented in the question. The patient is a 40-year-old man with a |
| history of alcohol abuse. He has been experiencing severe abdominal |
| pain, nausea, and vomiting for 1 day. His abdomen is distended, bowel |
| sounds are decreased, and there is tenderness in the upper abdomen. |
| His serum amylase and lipase levels are elevated. |
| 2. Use your knowledge of medicine to identify the most likely diagnosis. |
| The patient’s history of alcohol abuse, the sudden onset and severity |
| of his symptoms, and his physical examination findings are all |
| indicative of a pancreatic condition. The elevated serum amylase and |
| lipase levels further support this, as these enzymes are produced by |
| the pancreas and their levels increase in the blood when the pancreas |
| is inflamed or damaged. |
| 3. Consider the answer options in relation to the patient’s symptoms and |
| test results. Acute pancreatitis, peptic ulcer disease, gastric |
| cancer, and gastroenteritis are all potential diagnoses. |
| 4. Eliminate incorrect answer options based on your medical knowledge. |
| Peptic ulcer disease typically presents with a burning pain in the |
| middle or upper stomach between meals or at night, not with a |
| distended abdomen and decreased bowel sounds. Gastric cancer usually |
| develops slowly over many years, and its symptoms often only appear |
| in the advanced stages of the disease. Gastroenteritis, while it can |
| cause abdominal pain, nausea, and vomiting, does not typically result |
| in a distended abdomen, decreased bowel sounds, or elevated serum |
| amylase and lipase levels. |
| 5. The remaining option, acute pancreatitis, aligns with all the |
| information provided in the question. The patient’s history of |
| alcohol abuse is a common risk factor for acute pancreatitis. The |
| sudden onset and severity of his symptoms, his physical examination |
| findings, and his elevated serum amylase and lipase levels are all |
| characteristic of this condition. |
| 6. Therefore, the most likely diagnosis for this patient is acute |
| pancreatitis, making option A the correct answer. <ANS_START>A< |
| ANS_END> |


**Table (Page 33):**

|  |
|---|
| <human intent> |
| Medical Knowledge, Analytical Skills, English Proficiency, Reasoning |
| Skills, Attention to Detail |
|  |
| <expert persona> |
| You are a medical professional with extensive experience in the field and |
| a deep understanding of the United States Medical Licensing Exam ( |
| USMLE). You have successfully passed the USMLE and have a thorough |
| understanding of the format and style of the questions. You are well- |
| versed in a wide range of medical topics, from anatomy and physiology |
| to pathology and pharmacology. You have the ability to analyze |
| complex medical scenarios, apply your knowledge, and make informed |
| decisions. You can accurately interpret the questions and the |
| provided options, and select the correct answer based on your medical |
| knowledge and reasoning. Your expertise and experience make you |
| highly capable of answering these questions correctly and efficiently |
|  |
| <prompt guidelines for desired output format> |
| You need to output the correct option among [A/B/C/D] for each question |
| separately using your medical knowledge and reasoning. Wrap your only |
| the final answer, without reason for each question separately |
| between <ANS_START> and <ANS_END> tags. |
