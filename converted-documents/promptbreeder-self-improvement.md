---
title: "PromptBreeder Self Improvement"
original_file: "./PromptBreeder_Self_Improvement.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["prompt-engineering", "llm", "rag", "chain-of-thought", "react"]
keywords: ["prompt", "answer", "therefore", "input", "correct", "context", "word", "problem", "instruction", "prompts"]
summary: "<!-- Page 1 -->


## Promptbreeder:


## Self-Referential Self-Improvement


## Via Prompt Evolution

ChrisanthaFernando,DylanBanarse,HenrykMichalewski,SimonOsindero,TimRockta¨schel

### GoogleDeepMind

{chrisantha,dylski,henrykm,osindero,rocktaschel}@google.com

## Abstract

PopularpromptstrategieslikeChain-of-ThoughtPromptingcandramaticallyimprove the reasoning abilities of Large Language Models (LLMs) in various domains. However, such hand-crafted prompt-strategies are often sub-optimal. In
t"
related_documents: []
---

# PromptBreeder Self Improvement

<!-- Page 1 -->


## Promptbreeder:


## Self-Referential Self-Improvement


## Via Prompt Evolution

ChrisanthaFernando,DylanBanarse,HenrykMichalewski,SimonOsindero,TimRockta¨schel

### GoogleDeepMind

{chrisantha,dylski,henrykm,osindero,rocktaschel}@google.com

## Abstract

PopularpromptstrategieslikeChain-of-ThoughtPromptingcandramaticallyimprove the reasoning abilities of Large Language Models (LLMs) in various domains. However, such hand-crafted prompt-strategies are often sub-optimal. In
thispaper,wepresent PROMPTBREEDER,ageneral-purposeself-referentialselfimprovement mechanism that evolves and adapts prompts for a given domain.
DrivenbyanLLM,Promptbreedermutatesapopulationoftask-prompts, evaluatesthemforfitnessonatrainingset,andrepeatsthisprocessovermultiplegenerationstoevolvetask-prompts. Crucially, themutationofthesetask-promptsis
governedbymutation-promptsthattheLLMgeneratesandimprovesthroughout
evolution in a self-referential way. That is, Promptbreeder is not just improving
task-prompts, but it is also improving the mutation-prompts that improve these
task-prompts. Promptbreederoutperformsstate-of-the-artpromptstrategiessuch
as Chain-of-Thought and Plan-and-Solve Prompting on commonly used arithmetic and commonsense reasoning benchmarks. Furthermore, Promptbreeder is
able to evolve intricate task-prompts for the challenging problem of hate speech
classification.

## 1 Introduction

Promptingiscentraltothedownstreamperformanceoffoundationmodels. Forexample,different
promptstrategies1 canhaveasignificantimpactonamodel’sreasoningabilities(Weietal.,2022;
Nyeetal.,2021;Zhouetal.,2022;Wangetal.,2022;Zhouetal.,2023;Wangetal.,2023b),multimodalprocessingabilities(Yangetal.,2023b;Wangetal.,2023d),ortooluseabilities(Yaoetal.,
2022; Schick et al., 2023). Furthermore, prompting can improve model distillation (Wang et al.,
2023c;Hsiehetal.,2023)anditcanbeusedtosimulateagenticbehavior(Wangetal.,2023a;Park
etal.,2023;Wuetal.,2023). However,thesepromptstrategiesaremanuallyengineered. Sincethe
specificwayapromptisphrasedcanhaveadramaticeffectonitsutility(Madaan&Yazdanbakhsh,
2022), it raises the question of whether prompt engineering can be automated. Automatic Prompt
Engineer (APE, Zhou et al., 2023) attempts to address this by generating an initial distribution of
promptsusinganotherpromptthatinferstheproblemfromanumberofinput-outputexamplesfrom
thedataset. However,Zhouetal. found“diminishingreturnstofurtherselectionroundsasthequalityseemstostabilizeafterthreerounds”,andconsequentlyabandonedtheuseofaniterativeAPE.
Weproposeasolutiontotheproblemofdiminishingreturnsviaadiversitymaintainingevolutionary
algorithmforself-referentialself-improvementofpromptsforLLMs.
Schmidhuber (1990) notes that the “program of a neural network is its weight matrix”. Consequently, this “program” can be changed in a self-referential way by the neural network itself (Schmidhuber, 1993; Irie et al., 2022). Such a neural network that improves itself, as well
asimprovingthewayitimprovesitself,mightbeanimportantsteppingstonetowardsopen-ended
self-referentialself-improvementofAIs(Schmidhuber,2003). However,self-improvementviaselfreferentialweightmatricesiscostlyasitrequiresadditionalparametersthatmodifyallofthemodel’s
1SeeAppendixAfordefinitionsofterminology.
1
3202
peS
82
]LC.sc[
1v79761.9032:viXra

<!-- Page 2 -->

Method LLM MultiArith* SingleEq* AddSub* SVAMP* SQA CSQA AQuA-RAT GSM8K
tohs-oreZ
CoT text-davinci-003 (83.8) (88.1) (85.3) (69.9) (63.8) (65.2) (38.9) (56.4)
PoT text-davinci-003 (92.2) (91.7) (85.1) (70.8) – – (43.9) (57.0)
PS text-davinci-003 (87.2) (89.2) (88.1) (72.0) – – (42.5) (58.2)
PS+ text-davinci-003 (91.8) (94.7) (92.2) (75.7) (65.4) (71.9) (46.0) (59.3)

### PS PaLM2-L 97.7 90.6 72.4 83.8 50.0 77.9 40.2 59.0

PS+ PaLM2-L 92.5 94.7 74.4 86.3 50.1 73.3 39.4 60.5
APE PaLM2-L 95.8 82.2 72.2 73.0 38.4 67.3 45.7 77.9

### OPRO PaLM2-L – – – – – – – 80.2

PB(ours) PaLM2-L 99.7 96.4 87.8 90.2 71.8 85.4 62.2 83.9
-weF
Manual-CoT text-davinci-003 (93.6) (93.5) (91.6) (80.3) (71.2) (78.3) (48.4) (58.4)
Auto-CoT text-davinci-003 (95.5) (92.1) (90.8) (78.1) – – (41.7) (57.1)

### PB(ours) PaLM2-L 100.0 98.9 87.1 93.7 80.2 85.9 64.6 83.5

Table 1: Promptbreeder (PB) comparison to Chain-of-Thought (Manual-CoT, Wei et al., 2022),
Zero-shot CoT (Kojima et al., 2022), Program-of-Thoughts (PoT, Chen et al., 2022), Auto-
CoT (Zhang et al., 2023b), OPRO (Yang et al., 2023a), Automatic Prompt Engineer Zero-shot
prompt(APE,Zhouetal.,2023),Plan-and-Solvewith(PS+)andwithouttheimprovedprompt(PS,
Wang et al., 2023b) and using PaLM 2-L (Anil et al., 2023) as the underlying LLM (APE,
PS /PS+ ). Bestresultsinboththezero-shotandfew-shotcategoriesarehighlighted

### PaLM2-L PaLM2-L

in bold. Results in brackets are directly taken from the Plan-and-Solve paper which uses textdavinci-003 (Brownetal.,2020). Fordatasetswithastericks(MultiArith*, SingleEq*, AddSub*,
andSVAMP*), werandomlytookhalfoftheexamplesfortrainingandreportaccuracyontheremainingtestset. SeeSection4andAppendixIfordetailsonthepromptsanddatasets.
parameters. Since behaviors and capabilities of LLMs are significantly influenced by the prompts
thatweprovidetothem,wecansimilarlythinkofpromptsastheprogramofanLLM(Zhouetal.,
2023). Inthisview,changingapromptstrategysuchastheScratchpadmethod(Nyeetal.,2021)or
Chain-of-ThoughtPrompting(Weietal.,2022)correspondstochangingthe“program”oftheLLM.
Takingthisanalogyfurther,wecanusetheLLMitselftochangeitsprompts,aswellasthewayit
changestheseprompts,movingustowardsafullyself-referentialself-improvingsystemsgrounded
inLLMs.
Inthispaper,weintroducePROMPTBREEDER(PB)forself-referentialself-improvementofLLMs.
Given a seed set of mutation-prompts (i.e. instructions to modify a task-prompt), thinking-styles
(i.e. text descriptions of general cognitive heuristics), and a domain-specific problem description,
PB generates variations of the task-prompts and mutation-prompts, exploiting the fact that LLMs
can be prompted to act as mutation operators (Meyerson et al., 2023). Based on the fitness of
the evolved task-prompts as measured on the training set, we select a subset of evolutionary units
consistingoftask-promptsandtheirassociatedmutation-prompt,totransmittofuturegenerations.
OvermultiplegenerationsofPB,weobservepromptsadaptingtothedomainathand. Forexample,
in a mathematical domain, PB evolved the task-prompt "Show all your working. II.
You should use the correct mathematical notation and vocabulary, where
appropriate. III. You should write your answer in full sentences and in
words. IV. You should use examples to illustrate your points and prove
your answers. V. Your workings out should be neat and legible" on GSM8K
(see Appendix J). On a wide range of commonly used benchmarks spanning commonsense
reasoning, arithmetic, and ethics, we find that PB outperforms state-of-the-art methods like
Chain-of-Thought (Wei et al., 2022) and Plan-and-Solve (Wang et al., 2023b) prompting. As
PB does not require any parameter updates for self-referential self-improvement, we believe this
approachpointstoaninterestingfuturewherelargerandmorecapableLLMscouldfurtheramplify
thegainsofourapproach.
Insummary,thispapermakesthefollowingmaincontributions: (i)weintroducePromptbreeder,a
self-referential self-improvement method for LLMs that evolves prompts for a domain at hand, as
well as improves the way it is evolving these prompts, (ii) we report improvements over state-ofthe-artpromptstrategiesonawiderangeofcommonlyusedarithemicandcommonsensereasoning
benchmarks,and(iii)weinvestigatethevariousself-referentialcomponentsofPromptbreederand
theircontributiontoourresults.
2

<!-- Page 3 -->

Initialization of Population of Task-Prompts and Mutation-Prompts
Thinking Problem Description Mutation

### Styles Prompts

specific to GSM8K, AQuA,

### Sample ETHOS, SVAMP etc. Sample

“Let’s think step by step” + “Change this instruction to make it more fun” +
“INSTRUCTION:” + “Solve this math word problem” + “INSTRUCTION MUTANT = ” LLM “Make up a systematic answer that
makes you look quite clever”

### Mutate Populate N

Mutation Operators Population (N Task-Prompts and their Mutation-Prompts)
P: "Make up a systematic answer that makes you look quite clever"
0.2
Estimation of M: "Change this instruction to make it more fun"

### Direct Mutation


### Distribution Mutation

P: "Draw a diagram representing the math problem"
0.4
M: "Mutate the prompt with an unexpected twist"
Lamarckian Mutation

### Hyper Mutation

Mutate mutation-prompt f G ro e m ne t r h a e te " w ta o s r k k - in p g ro o m u p t" t Replace P M = = " " L M e o t’ d s if t y h i t n h k e s i t n e s p tr t u h c r t o io u n g h li k t e h is n o m s a e th lf- s r e p s ro p b e l c e t m ing " LLM would" 0.1
Prompt Crossover
and
Context Shuffling P: "SOLUTION:"
0.9

### M: "Consider how a better teacher would put this"


### Estimated fitness from a batch of training Q&A pairs

Figure 1: Overview of Promptbreeder. Given a problem description and an initial set of general
“thinking-styles”andmutation-prompts,Promptbreedergeneratesapopulationofunitsofevolution,
eachunitconsistingoftypicallytwotask-promptsandamutation-prompt. Wethenrunastandard
binarytournamentgeneticalgorithm(Harvey,2011). Todeterminethefitnessofatask-promptwe
evaluate its performance on a random batch of training data. Over multiple generations, Promptbreedersubsequentlymutatestask-promptsaswellasmutation-promptsusingfivedifferentclasses
ofmutationoperators. Theformerleadstoincreasinglydomain-adaptivetask-promptswhereasthe
latterevolvesincreasinglyusefulmutation-promptsinaself-referentialway.

## 2 Related Work

PromptinganLLMintherightwayisessentialtoitsdownstreamperformance(Moradi&Samwald,
2021;Madaan&Yazdanbakhsh,2022;Zhouetal.,2023). Indeed,eventheorderinwhichprompts
arepresentedcanheavilyinfluenceLLMperformance(Luetal.,2022). Anumberofrecentworks
havefocusedondevisingbetterpromptstrategies,orevenautomatingsuchpromptengineering.
Prompting:Chain-of-ThoughtPrompting(CoT,Weietal.,2022)isapopularpromptstrategywhich
providesintermediatereasoningstepsasfew-shotpromptstoanLLM,therebysignificantlyimproving its arithmetic, commonsense, and symbolic reasoning abilities. Notably, the gains of CoT are
morepronouncedforstrongerLLMs.Thisisintriguing,asitpointstothepossibilityofincreasingly
capable(andpotentiallyopen-ended)self-improvingmechanismsontopofadeptLLMs—ahypothesis that Promptbreeder directly builds upon. Instead of few-shot CoT prompting, Kojima et al.
(2022) demonstrate that LLMs can also be prompted zero-shot (e.g. "Let’s think step by
step")toproducetheirownchainsofthoughts(Zero-shot CoT)thatimprovereasoningabilities.
Self-Consistency(CoT-SC,Wangetal.,2022)extendsCoTbysamplingadiversesetofworkings
outandselectingthemostconsistentanswer. TreeofThoughts(ToT,Yaoetal.,2023)generalizes
CoTtomultipleworkingsoutthatcanbeexpandedorbacktrackedfrom. GraphofThoughts(GoT,
Bestaetal.,2023)isafurthergeneralizationtoarbitrarygraphstructures. Plan-and-SolvePrompting (PS, Wang et al., 2023b) encourages an LLM to first devise a plan to solve a problem before
attemptingtosolveit. Similarly,Least-to-MostPrompting(Zhouetal.,2022)encouragesanLLM
todecomposeaproblemintosubparts,andthentosolveeachpartindividuallybeforesynthesizing
an answer. Self-Refine (Madaan et al., 2023) prompts an LLM to generate a response, to provide
feedbackontheresponse,andtofinallyrefinethesolution.
3

<!-- Page 4 -->

Incontrasttogradient-freeapproachesabove,SoftPromptingapproaches(e.g.,Liuetal.,2021;Qin
& Eisner, 2021; Lester et al., 2021) directly fine-tune continuous prompt representations. Huang
et al. (2022) use CoT and CoT-SC on an unlabelled dataset of questions, and subsequently finetuneanLLMbasedongeneratedsolutions. Similarly,Zelikmanetal.(2022)usesCoTtogenerate
rationalesandfine-tunestheLLM basedonthoseexamplesandrationalesthatyielded thecorrect
answer.However,asarguedbyZhouetal.(2023),anyapproachthatupdatesalloraportionofLLM
parameters will not scale as models get bigger and, moreover, will not work with the increasing
numberofLLMshiddenbehindanAPI.
All of the prompt engineering approaches above are domain agnostic but hand designed. Central
toourworkisthehypothesisthatwecoulddobetterbyemployinganautomatedself-improvement
processthatcanadaptpromptstoadomainathand.Auto-CoT(Zhangetal.,2023b)andAutomatic-
CoT(Shumetal.,2023)automaticallyfindreasoningchainsforFew-ShotCoT.AutomaticPrompt
Engineer (APE, Zhou et al., 2023) uses one generator-prompt to generate prompt candidates, and
another mutation-prompt to mutate them. In contrast to APE, our work performs compositional
task-specific initialization of mutation-prompts, subsequent online mutation of mutation-prompts,
uses special mutation operators that take into account the whole population and elite history, and
uses diversity-maintenance methods—all of which help avoid the problem of diminishing returns
anddiversitylosssufferedbyAPE.
Concurrently to our work, Yang et al. (2023a) developed Optimization by PROmpting (OPRO),
a prompt optimization method that varies prompts using a single complex mutation prompt, and
evaluatesnewlygeneratedpromptsonasmallfixedtrainingsetofproblems. Incontrast, PromptbreederautonomouslyevolvesmultipleLLMgeneratedmutation-promptsaswellastask-prompts,
and evaluates fitness on random subsets from the whole training set during evolution. At the time
ofitsrelease,OPROachievedascoreof80.2%viatheoptimizedzero-shotprompt"Take a deep
breath and work on this problem step-by-step"onGSM8K.Promptbreedersurpasses
this with 83.9% in the zero-shot setting with the unintuitively simple prompt "SOLUTION""—
further evidence for the sensitivity of LLMs to prompts and the importance on finding effective
prompts automatically. Also concurrently to our work, Guo et al. (2023) developed EvoPrompt,
whichusesafixedmutation(andcrossover)prompt, aswellasapromptthatasksforamutantof
thedifferencebetweentwoparentprompts,toproduceoffspringprompts. EvoPromptisinitialized
with a whole population of initial hand-designed task tailored prompts rather than a single problem description as we do. In contrast to the two approaches above, Promptbreeder uses LLMs to
self-referentiallyimprovemutation-prompts,anditisabletoevolvecontextsaswell.
Self-ReferentialSelf-Improvement: Developinganopen-endedsystemthatcanimproveitselfas
wellasimprovingthewayitisimprovingitself(Schmidhuber,1993;2003)isalong-standingopen
problemin AIresearch. Schmidhuber (1993)introduced an“introspective”neural networkwith a
self-referentialweightmatrixthatcanmodifyitsownweightsand,thus,alsomodifythoseweights
thataregoverninghowitsownweightsaremodified. Recently, Irieetal.(2022)proposedamore
scalable self-referential weight matrix taking inspiration from fast weight programmers (Schmidhuber, 1992). Kirsch & Schmidhuber (2022) propose a self-referential meta-learning approach,
combiningself-referentialweightmatriceswithideasfromGo¨delMachines(Schmidhuber,2003),
i.e.,toallocatemorecomputationalresourcestobetterperformingsolutions. However,sincethese
approaches directly modify parameters of a model, it is unclear how to scale them to the increasing number of parameters in modern LLMs. In contrast, for Promptbreeder the substrate of selfreferentialself-improvementisnaturallanguage,avoidingcostlyparameterupdatesaltogether.
Open-EndednessandLLMs:PromptbreedermakesuseoftheobservationbyLehmanetal.(2022),
Meyersonetal.(2023)andChenetal.(2023)thatLLMsareeffectiveatgeneratingmutationsfrom
examples. In addition, LLMs encode human notions of interestingness and can be used to automaticallyquantifynovelty(Zhangetal.,2023a). PromptbreederisrelatedtoPicbreeder(Secretan
etal.,2008),anopen-endedhuman-in-the-loopsystemthatevolvesincreasinglyinterestingimages.
While Picbreeder explores the space of images, Promptbreeder explores the space of prompts and
does so without humans in the loop. As Promptbreeder is proposing mutated prompts to itself, it
is an example of a system transitioning from “learning from data” to “learning what data to learn
from”(Jiangetal.,2022).
4

<!-- Page 5 -->


## 3 Promptbreeder

WeintroducePromptbreeder,apromptevolutionsystemthatcanautomaticallyexplorepromptsfor
agivendomainandthatisabletofindtask-promptsthatimproveanLLM’sabilitytoderiveanswers
to questions in that domain. Promptbreeder is general purpose in that the same system is able to
adapttomanydifferentdomains.
PromptbreedermakesuseoftheobservationthatLLMscanbeusedtogeneratevariationsofinput
text (Lehman et al., 2022; Meyerson et al., 2023; Chen et al., 2023). Figure 1 gives an overview
of our method. We are interested in evolving task-prompts. A task-prompt P is a string used to
condition the context of an LLM in advance of some further input Q, intended to ensure a better
responsethanifQhadbeenpresentedintheabsenceofP. Toevaluatethefitnessofeachevolved
task-prompt, we sample a batch of 100 Q&A pairs from the entire training set of the domain at
hand.2
Promptbreedergeneratestask-promptsaccordingtoanevolutionaryalgorithm. Themutationoperator for this algorithm is itself an LLM, conditioned on a mutation-prompt M. That is, a mutated
taskpromptP′ isdefinedbyP′ = LLM(M +P)where‘+‘correspondstostringconcatenation.
Avarietyofsuchmutation-promptsaredescribedinSection3.2.
Promptbreeder’s main self-referential mechanism stems from applying the evolutionary algorithm
not just to task-prompts but also to mutation-prompts. The mutation operator for this meta-level
algorithmisagainanLLM,nowconditionedonahyper-mutationpromptH. Thatis,weobtaina
mutatedmutation-promptM′viaM′ =LLM(H +M).
Given a set of “thinking styles” T and a set of initial mutation-prompts M, as well as a domainspecific problem description D, Promptbreeder initializes a population of mutated task-prompts
(seeSection3.1). Toclarify,aunitofevolutionconsistsofasetoftask-prompts,amutation-prompt
and in the few-shot case, a set of correct workings out (i.e. step-by-step or “chains-of-thought”
reasoningstepsthatledtothecorrectanswer). Thismeanstask-promptsandmutation-promptsare
in1:1correspondence. Toevolvethispopulation,weemployabinarytournamentgeneticalgorithm
framework(Harvey,2011): wesampletwoindividualsfromthepopulation,wetaketheindividual
withthehigherfitness,mutateit(seenextsection)andoverwritetheloserwiththemutatedcopyof
thewinner.

## 1 Promptbreederinitialization

To give a concrete example, consider the initialization steps used to produce the taskprompts and mutation-prompts for GSM8K (a ‘grade school maths’ word problem dataset).
The problem description is "Solve the math word problem, giving your answer as
an arabic numeral". Because Plan-and-Solve (Wang et al., 2023b) uses two task-prompts we
also evolve two task-prompts (plus a mutation-prompt) per unit of evolution. In order to promote
diversityintheinitialprompts,wegeneratetheinitialtask-promptsbyconcatenating(foreachtaskprompt)arandomlydrawn‘mutation-prompt’(e.g. "Make a variant of the prompt.")and
arandomlydrawn‘thinking-style’(e.g."Let’s think step by step")totheproblemdescription,andprovidethattotheLLMtoproduceacontinuation,resultinginaninitialtask-prompt. We
do this twice to produce the two initial task-prompts per unit. Both the mutation-prompt and the
thinking-stylearerandomlysampledfromaninitialsetofmutation-promptsandasetofthinkingstyles (see Appendices C, D and G for the full sets). The mutation-prompt is added to the unit of
evolutionandsoisassociatedwithitsspecifictask-promptthroughouttheevolutionaryrun.
Fortheexampleabove,thecompleteinputstringtotheLLMtomakeaninitialtask-promptcould
be "Make a variant of the prompt. Let’s think step by step. INSTRUCTION:
Solve the math word problem, giving your answer as an arabic numeral.
INSTRUCTION MUTANT:". Note how the control strings "INSTRUCTION" and "INSTRUCTION
MUTANT" are added to encourage an appropriate continuation. Table 4 in Appendix E shows
examplesoftheinitialpromptsgeneratedinthisway.
2Ourpromptstrategysequentiallyappliestwotask-prompts. Thefirsttask-prompt+questionproducesa
continuation.Thecontinuation+secondtask-promptproducesthefinalanswer.
5

<!-- Page 6 -->


## 2 Mutationoperators

As shown in Figure 1, there are nine operators falling into five broad classes which drive the exploration of prompt strategies. For each replication event only one of nine mutation operators is
applied(wesamplewithuniformprobabilityoverthenineoperatorstodecidewhichmutationoperatortoapply). TherationaleforusingthisdiversesetofoperatorsistoenabletheLLMtoexplore
alargespaceofcognitivemethodsoflinguisticself-questioning,byrepeatedlychangingtheframingoftheproblemaswellasretrievingmentalmodelsexpressedinnaturallanguagethatcanhelp
tackleagivenreasoningchallenge.Investigationsfrominsightlearningstronglysuggestthatdiverse
representationalre-descriptioniskeytoproblemsolving(O¨llinger&Knoblich,2009)—aprinciple
that we attempt to recreate via self-referential self-improvement with natural language as the substrate. Figure2illustratesinwhatwayPromptbreederisself-referential(seeAppendixFforamore
detailedexplanation).

## 1 Directmutation

The simplest class of mutation operators directly generate a new task-prompt P′ from either one
existing task-prompt P (first-order prompt generation) or from a general prompt that encourages
free-formgenerationofnewtask-prompts–i.e. notusinganexistingparent,thuszero-orderprompt
generation.
Zero-orderPromptGeneration:Wegenerateanewtask-promptbyconcatenatingtheproblemdescriptionD(e.g."Solve the math word problem, giving your answer as an arabic
numeral")withtheprompt"A list of 100 hints:",whichinvitestheLLMtocomeupwith
anewhintthatcouldhelpsolveaprobleminthegivenproblemdomain. Weextractthefirstgeneratedhintasthenewtask-prompt.Crucially,thisnewtask-promptdoesnotdependonanypreviously
foundtask-prompt. Instead,itisre-generatedfromtheproblemdescriptioneachtime. Ourrationale
forincludingthiszero-orderoperatoristhatwherepromptevolutiondiverges,thisoperatorallows
ustogeneratenewtask-promptscloselyrelatedtotheoriginalproblemdescription,similartouniform re-sampling in automated curriculum learning approaches (Jiang et al., 2021b;a; Park et al.,
2023;Parker-Holderetal.,2022).
First-order Prompt Generation: We concatenate the mutation-prompt (red), to the parent
task-prompt (blue), and pass it to the LLM to produce the mutated task-prompt. For example
"Say that instruction again in another way. DON’T use any of the words
in the original instruction there’s a good chap. INSTRUCTION: Solve the
math word problem, giving your answer as an arabic numeral. INSTRUCTION
MUTANT: ". This procedure is identical to the initialization method, except that a randomly
sampled thinking-style string is not used. First-order prompt generation is Promptbreeder’s
standard asexual mutation operator, and it is the core of every genetic algorithm—taking one
parental genotype (task-prompt) and applying the mutation to it (in this case influenced by the
mutation-prompt).

## 2 Estimationofdistributionmutation

Thenextclassofmutationoperatorsconditionnotjustonzerooroneparent,butinsteadonasetof
parents. Assuch,theymaybemoreexpressivebyconsideringpatternsinthepopulation.
Estimation of Distribution (EDA) Mutation: Inspired by Hauschild & Pelikan (2011), we provide a filtered and numbered list of the current population of task-prompts to the LLM and ask it
to continue this list with new task-prompts. We filter the population of prompts on the basis of
BERT(Devlinetal.,2019)embeddingcosinesimilaritiesbetweeneachother—anindividualisnot
included in the list if it is more than 0.95 similar to any other entry in the list, thus encouraging
diversity(cf. quality-diversitymethods(Lehman&Stanley,2011b;a;Mouret&Clune,2015)). The
promptsarelistedinrandomorderandwedonotgivetheLLMaccesstothefitnessvaluesofindividualsinthepopulation—wefoundinpreliminaryexperimentsthattheLLMdidnotunderstand
thesefitnessvalues3andresortedtogeneratingcopiesofentriesinthelist.
3This is contrary to recent findings by Mirchandani et al. (2023). We leave it for future work to revisit
whetherLLMscaninterpretfitnessvaluesforimprovedpromptevolution.
6

<!-- Page 7 -->

Direct Mutation-PromptGuided HyperMutation Promptbreeder

## H H


## Llm M′ Llm M′


## M M M

P LLM P′ LLM P′ LLM P′ M∼M LLM P′

## P P D Llm P


## T∼T

(a) (b) (c) (d)
Figure 2: Overview of multiple variants of self-referential prompt evolution. In (a), the LLM is
directly used to generate variations P′ of a prompt strategy P (cf. Meyerson et al., 2023). Using
a mutation prompt M, we can explicitly prompt an LLM to produce variations (b). By using a
hypermutationpromptH,wecanalsoevolvethemutationpromptitself,turningthesystemintoa
self-referentialone(c). Promptbreeder(d)improvesthediversityofevolvedpromptsandmutation
promptsbygeneratinganinitialpopulationofpromptstrategiesfromasetofseedthinking-styles
T,mutation-promptsM,aswellasahighleveldescriptionDoftheproblemdomain.
EDARankandIndexMutation: Thisisavariantoftheaboveinwhichtask-promptsarelistedin
fitnessorder. PreliminaryexperimentsshowedthattheLLMismorelikelytogenerateentriesthat
aresimilartotheelementsappearinglaterinthelist. Thisisinlinewithsimilarfindingsofrecency
effectsinLLMs(Liuetal.,2023). Therefore,afterfilteringinthesamewayasbefore,weordered
the task-prompts in the population by ascending order of fitness. The top of the list is prefixed
by the following prompt: "INSTRUCTION: " + <<mutation-prompt>> + "\n A List of
Responses in descending order of score." + <<last index + 1>> + "is the
best response. It resembles" + << last index>> + "more than it does (1)".
Note that we have ‘lied’ to the LLM by telling it that the order is descending. This is because
otherwise it is too biased towards producing a new entry that is too similar to the final entry. The
contradiction between the ascending ordering and the statement that it is a descending ordering
appears to improve the diversity of sampling. The rationale for this operator is again to represent
thecurrentdistributioninsuchawaythathighfitnessandyetdiverseextrapolationsaresuggested
bytheLLM.
LineageBasedMutation:Foreachunitofevolution,westoreahistoryoftheindividualsinitslineagethatwerethebestinthepopulation,i.e.,ahistoricalchronologicallistofelites. ThislistisprovidedtotheLLMinchronologicalorder(notfilteredbydiversity),withtheheading"GENOTYPES
FOUND IN ASCENDING ORDER OF QUALITY"toproduceanovelpromptascontinuation.Therationaleforthisoperatoristhatweexpectthesignalofimprovinggenotypepromptsmaybestronger
thanthesignalfrompromptsinthecurrentpopulationsincetheyprovideagradientofbadtogood
promptsthatcouldbefollowed(assumingthissignalcanbeusedbytheLLM).

## 3 Hypermutation: Mutationofmutation-Prompts

While the mutation operators above might already explore diverse task-prompts, a self-improving
system should ideally also improve the way it is improving itself in a self-referential way. Our
thirdclassofmutationoperatorsincludeshyper-mutationoperatorsconcernedwiththeevolutionof
evolvability(Dawkins,2003;Pigliucci,2008;Payne&Wagner,2019;Gajewskietal.,2019)—those
whichmodifythesearch/explorationprocessratherthanthetaskrewardobtainingprocessdirectly.4
Zero-orderHyper-Mutation:Weconcatenatetheoriginalproblemdescriptiontoarandomlysampled thinking-style, and feed it to the LLM to generate a new mutation-prompt. The resulting
mutation-promptisappliedtoatask-prompttomakeavariantofthetask-promptasinFirst-order
PromptGeneration(seeSection3.2.1). Notethatthiszero-ordermeta-mutationoperatorisidentical
tothatusedduringinitialization. Therationaleforthisoperatoristogeneratemutationoperatorsin
awaysimilartoinitialization,whilealsobringinginknowledgefromthesetofthinkingstyles.
4Thisissimilartopopulationbasedtraining(Jaderbergetal.,2017a)—insteadofapplyingittohyperparameterssuchaslearningrates,itappliestothemutation-promptsofPromptbreeder.
7

<!-- Page 8 -->

First-orderHyper-Mutation: Weconcatenatethehyper-mutation-prompt"Please summarize
and improve the following instruction:" to a mutation-prompt so that the LLM generates a new mutation-prompt. This newly generated mutation-prompt is then applied to the taskpromptofthatunit(seeFirst-OrderPromptGenerationinSection3.2.1). Inthisway,wecanevaluatetheinfluenceofthehyper-mutationviaitsnewlygeneratedmutation-promptonthequalityof
theevolveddownstreamtask-promptatonce.

## 4 Lamarckianmutation

ForthisclassofmutationoperatorswemimicaLamarckianprocess. Wewanttouseasuccessful
phenotype (i.e. the concrete working out used to produce correct answers induced by an evolved
task-prompt)togenerateanewgenotype(i.e. amutanttask-prompt). Severalprocessesofthisform
have appeared in the literature of LLMs, e.g. STaR (Zelikman et al., 2022), APO (Pryzant et al.,
2023),andAPE(Zhouetal.,2023).
Working Out to Task-Prompt: This is a ‘Lamarckian’ mutation operator similar to instruction
inductioninAPE.WegiveanLLMapreviouslygeneratedworkingoutthatledtoacorrectanswer
viathefollowingprompt: "I gave a friend an instruction and some advice. Here
are the correct examples of his workings out + <<correct working out>> +
The instruction was:". This is effectively reverse-engineering the task-prompt from a given
workingout. AneffectiveexampleofthisisshowninAppendixH.Thiskindofoperatoriscritical
whentheproblemdescriptionisabsent,insufficient,ormisleading.

## 5 Promptcrossoverandcontextshuffling

Ourlastclassofmutationoperatorsarecrossoveroperatorsandoperatorsforshufflingthefew-shot
contextexamplespresentintheunitsofevolution.
PromptCrossover:Afteramutationoperatorisapplied,with10%chanceatask-promptisreplaced
witharandomlychosentask-promptfromanothermemberofthepopulation.Thismemberischosen
accordingtofitnessproportionateselection. Crossoverisnotappliedtomutation-prompts,onlyto
thetask-prompts.
ContextShuffling: Promptbreedercansimultaneouslyevolvethetask-prompts,mutation-prompts
andthesetofcorrectworkingsoutknownasthefew-shotcontext. Toachievethelater,wefillupa
few-shotcontextwithonlyworkingsoutthatledtocorrectanswers. Duringevaluationweprovide
thisfewshot-contextbeforethetask-prompt,providingguidanceastotheformoftheworkingout
thatisdesired. Ifthefew-shotcontextlistisfull, asinglerandomlysamplednewcorrectworking
out replaces an existing working out from the list after fitness evaluation of a unit on a new set
of questions. In addition, with a 10% chance we resample the whole context list with probability
inversetothemaximumcontextlistlength.

## 4 Experiments

Weusedapopulationsizeof50units,evolvedfortypically20-30generations,whereageneration
involvesformingrandompairsofallindividualsinthepopulationandcompetingthemagainsteach
other. ToevaluatePromptbreeder, weusethedatasetsfromstate-of-the-artpromptstrategiessuch
asPlan-and-Solve,spanningarithmeticreasoningwithGSM8K(Cobbeetal.,2021),SVAMP(Pateletal.,2021),MultiArith(Roy&Roth,2016),AddSub(Hosseinietal.,2014),AQuA-RAT(Ling
etal.,2017),andSingleEq(Koncel-Kedziorskietal.,2015),commonsensereasoningwithCommonsenseQA(CSQA,Talmoretal.,2019)andStrategyQA(SQA,Gevaetal.,2021),instructioninductiontasksfrom(Honovichetal.,2023),andhatespeechclassificationontheETHOSdataset(Mollas
etal.,2022). SeeAppendixIfordetails.

## 5 Results And Discussion

We present results of Promptbreeder (PB) in comparison to state-of-the-art prompt strategies on a
rangeofcommonlyusedreasoningbenchmarksinTable1. PBoutperformsPS+,thebestPlan-and-
Solve (Wang et al., 2023b) prompting technique. Note that the performance of PS+ is improved
8

<!-- Page 9 -->

by using PaLM 2-L (Anil et al., 2023) as the underlying LLM (PS+ ) on all datasets ex-

### PaLM2-L

cept ADDSUB compared to text-davinci-003 results in the original paper. On all other datasets,
zero-shotPBaccuracyishigherthanPS+,withfurtherimprovementinthefew-shotcasewhenexamplesofdiscoveredsolutionsareincludedwiththeprompts. InTable6inAppendixJ,weshow
the best evolved zero-shot prompts. The best few-shot candidates are shown in Appendix J.5 onwards. Appendix K shows few-shot results and their controls on the Instruction Induction tasks
fromtheAPEpaper. ToinvestigatetheabilityofPromptbreedertoevolvecomplexdomain-specific
prompts for a downstream task, we applied it to the ETHOS Hate Speech Classification problem (Mollas et al., 2022). Promptbreeder was able to evolve a prompt strategy consisting of two
sequentially applied relatively long prompts (see Appendix J.1) that scored 89% on ETHOS—an
improvement over the hand-designed prompt "Determine whether a text contains hate
speech" which scores only 80%. This demonstrates that Promptbreeder is capable of intricate
domain-adaptationtoataskathand. AppendixBshowsatypicalevolutionaryrunandtheprompts
evolved,showingthatunlikeiterativeAPE,fitnesscontinuestoincreasethroughouttherun.
We analysed the best mutation-prompts used during a run for GSM8K. Table 7 in Appendix J.3
showsthebestevolvedmutationpromptsaccordingtotheirscores(theproportionoftimesthatwhen
the mutation-prompt was applied to a task-prompt in an unit, a better task-prompt was produced).
Table8inAppendixJ.4showsindescendingorder,thepercentageoftimesthatthedifferentkinds
ofmutationoperatorsresultedinanimprovementwhenappliedtoatask-promptinthepopulation.It
demonstratesthatallmutationoperatorsareimportantforPromptbreedertowork,includinghypermutationoperatorswhichleadtoself-referentialself-improvement.
We measured the impact of self-referential operators on all the maths datasets and the ETHOS
dataset. DetailsoftheablationprocessanditsresultscanbefoundinAppendixL.Removingany
self-referential operator is harmful under nearly all circumstances, the greatest benefit being the
initialre-descriptionoftask-promptsuponinitialization. Weonlyfoundonemutationoperatortobe
harmfulforonespecifictask:drawingrandomlyfromthesetofmutation-promptsuponinitialization
hurtsperformanceonGSM8K.

## 6 Conclusion And Future Work

WeintroducedPROMPTBREEDER(PB),aself-referentialself-improvingsystemthatcanautomaticallyevolveeffectivedomain-specificpromptsforadomainathand. PBisself-referentialinthatit
notonlyevolvestask-prompts,butitalsoevolvesmutation-promptsthatgovernthewayPBmodifies
task-prompts. Thus, itisnotonlyimprovingpromptsbutitalsoimprovesthewayitisimproving
prompts.
Going forward, it could be interesting to use the LLM itself to assess and promote the diversity
of generated prompts (see Zhang et al., 2023a), or to use it to determine the fitness of a whole
“thought process”, e.g. an N-prompt strategy where prompts are conditionally applied rather than
unconditionally applied as in Promptbreeder. For example, a more complex “thought process” is
tousePBinself-playmodetoevolvepre-promptsforLLM-basedpoliciesthatcompetewitheach
other,i.e.,inacompetitiveSocratic5dialog.
PBremainslimitedcomparedtotheopen-endednessofhumanthoughtprocesses.First,thetopology
ofpromptingremainsfixed(seeFigure2)—weonlyadaptthepromptcontentnotthepromptingalgorithmitself. Oneinterpretationofthoughtisthatitisareconfigurableopen-endedself-prompting
process. Ifso,howdoesonedevelopcomplexthoughtstrategies? Clearlyitisnecessarytogenerate
and evaluate them, and whilst a simple evolutionary process provides one framework in which a
thought strategy could be evolved, our actual human experience suggests multiple overlapping hierarchical selective processes at play. Moreover, in addition to language, human thought involves
intonation,imagery,etc.,inamultimodalsystem.
We believe PB points to an exciting future where increasingly open-ended self-referential selfimprovementsystemscandirectlyuselanguageasthesubstrateforimprovementinsteadofrelying
onanyparameterupdates. Thisisintriguing,asthisapproachwilllikelycontinuetoscalewithever
largerandmorecapableLLMsinthefuture.
5https://princeton-nlp.github.io/SocraticAI/
9

<!-- Page 10 -->


## Acknowledgments

WethankEdwardHughesandTomSchaulforfeedbackonanearlydraftofthepaper.Wealsothank
TomSchaul,ChengrunYang,andDennyZhouforfruitfuldiscussions,aswellasGavinButtimore,
SimonGreen,KeithAnderson,JossMoore,OlliePurkiss,JohnQuan,andFrancescoVisinfortheir
supportinrunningsomeoftheexperiments.

## References

Rohan Anil, Andrew M. Dai, Orhan Firat, Melvin Johnson, Dmitry Lepikhin, Alexandre Passos,
Siamak Shakeri, Emanuel Taropa, Paige Bailey, Zhifeng Chen, Eric Chu, Jonathan H. Clark,
LaurentElShafey,YanpingHuang,KathyMeier-Hellstern,GauravMishra,EricaMoreira,Mark
Omernick,KevinRobinson,SebastianRuder,YiTay,KefanXiao,YuanzhongXu,YujingZhang,
GustavoHernandezAbrego,JunwhanAhn,JacobAustin,PaulBarham,JanBotha,JamesBradbury, Siddhartha Brahma, Kevin Brooks, Michele Catasta, Yong Cheng, Colin Cherry, Christopher A. Choquette-Choo, Aakanksha Chowdhery, Cle´ment Crepy, Shachi Dave, Mostafa Dehghani,SunipaDev,JacobDevlin,MarkD´ıaz,NanDu,EthanDyer,VladFeinberg,Fangxiaoyu
Feng,VladFienber,MarkusFreitag,XavierGarcia,SebastianGehrmann,LucasGonzalez,Guy
Gur-Ari,StevenHand,HadiHashemi,LeHou,JoshuaHowland,AndreaHu,JeffreyHui,Jeremy
Hurwitz, Michael Isard, Abe Ittycheriah, Matthew Jagielski, Wenhao Jia, Kathleen Kenealy,
MaximKrikun,SnehaKudugunta,ChangLan,KatherineLee,BenjaminLee,EricLi,MusicLi,
WeiLi,YaGuangLi,JianLi,HyeontaekLim,HanzhaoLin,ZhongtaoLiu,FrederickLiu,MarcelloMaggioni,AromaMahendru,JoshuaMaynez,VedantMisra,MaysamMoussalem,Zachary
Nado,JohnNham,EricNi,AndrewNystrom,AliciaParrish,MariePellat,MartinPolacek,Alex
Polozov, Reiner Pope, Siyuan Qiao, Emily Reif, Bryan Richter, Parker Riley, Alex Castro Ros,
Aurko Roy, Brennan Saeta, Rajkumar Samuel, Renee Shelby, Ambrose Slone, Daniel Smilkov,
David R. So, Daniel Sohn, Simon Tokumine, Dasha Valter, Vijay Vasudevan, Kiran Vodrahalli,
XuezhiWang,PidongWang,ZiruiWang,TaoWang,JohnWieting,YuhuaiWu,KelvinXu,YunhanXu,LintingXue,PengchengYin,JiahuiYu,QiaoZhang,StevenZheng,CeZheng,Weikang
Zhou,DennyZhou,SlavPetrov,andYonghuiWu. PaLM2TechnicalReport,September2023.
Maciej Besta, Nils Blach, Ales Kubicek, Robert Gerstenberger, Lukas Gianinazzi, Joanna Gajda,
Tomasz Lehmann, Michal Podstawski, Hubert Niewiadomski, Piotr Nyczyk, and Torsten Hoefler. Graph of thoughts: Solving elaborate problems with large language models. CoRR,
abs/2308.09687, 2023. doi: 10.48550/arXiv.2308.09687. URL https://doi.org/10.
48550/arXiv.2308.09687.
Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, Sandhini Agarwal, Ariel Herbert-Voss, Gretchen Krueger, Tom Henighan, Rewon Child, Aditya Ramesh,
Daniel M. Ziegler, Jeffrey Wu, Clemens Winter, Christopher Hesse, Mark Chen, Eric Sigler,
Mateusz Litwin, Scott Gray, Benjamin Chess, Jack Clark, Christopher Berner, Sam McCandlish, Alec Radford, Ilya Sutskever, and Dario Amodei. Language models are few-shot
learners. In Hugo Larochelle, Marc’Aurelio Ranzato, Raia Hadsell, Maria-Florina Balcan,
and Hsuan-Tien Lin (eds.), Advances in Neural Information Processing Systems 33: Annual
Conference on Neural Information Processing Systems 2020, NeurIPS 2020, December 6-12,
2020,virtual,2020. URLhttps://proceedings.neurips.cc/paper/2020/hash/
1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html.
AngelicaChen,DavidM.Dohan,andDavidR.So.Evoprompting:Languagemodelsforcode-level
neuralarchitecturesearch. CoRR,abs/2302.14838,2023. doi:10.48550/arXiv.2302.14838. URL
https://doi.org/10.48550/arXiv.2302.14838.
WenhuChen,XueguangMa,XinyiWang,andWilliamW.Cohen.ProgramofThoughtsPrompting:
DisentanglingComputationfromReasoningforNumericalReasoningTasks,November2022.
Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian, Mark Chen, Heewoo Jun, Lukasz Kaiser,
Matthias Plappert, Jerry Tworek, Jacob Hilton, Reiichiro Nakano, Christopher Hesse, and John
Schulman. Trainingverifierstosolvemathwordproblems. CoRR,abs/2110.14168,2021. URL
https://arxiv.org/abs/2110.14168.
10

<!-- Page 11 -->

RichardDawkins. 13-Theevolutionofevolvability. InSanjeevKumarandPeterJ.Bentley(eds.),
OnGrowth,FormandComputers,pp.239–255.AcademicPress,London,January2003. ISBN
978-0-12-428765-5. doi: 10.1016/B978-012428765-5/50046-3.
JacobDevlin,Ming-WeiChang,KentonLee,andKristinaToutanova. BERT:pre-trainingofdeep
bidirectional transformers for language understanding. In Jill Burstein, Christy Doran, and
Thamar Solorio (eds.), Proceedings of the 2019 Conference of the North American Chapter of
the Association for Computational Linguistics: Human Language Technologies, NAACL-HLT
2019, Minneapolis, MN, USA, June 2-7, 2019, Volume 1 (Long and Short Papers), pp. 4171–

## Association for Computational Linguistics, 2019. doi: 10.18653/v1/n19-1423. URL

https://doi.org/10.18653/v1/n19-1423.
AlexanderGajewski, JeffClune, KennethO.Stanley, andJoelLehman. EvolvabilityES:scalable
anddirectoptimizationofevolvability. InAnneAugerandThomasStu¨tzle(eds.),Proceedingsof
theGeneticandEvolutionaryComputationConference,GECCO2019,Prague,CzechRepublic,
July 13-17, 2019, pp. 107–115. ACM, 2019. doi: 10.1145/3321707.3321876. URL https:
//doi.org/10.1145/3321707.3321876.
MorGeva,DanielKhashabi,EladSegal,TusharKhot,DanRoth,andJonathanBerant. Didaristotle
usealaptop? Aquestionansweringbenchmarkwithimplicitreasoningstrategies. Trans.Assoc.
Comput. Linguistics, 9:346–361, 2021. doi: 10.1162/tacl\ a\ 00370. URL https://doi.
org/10.1162/tacl_a_00370.
QingyanGuo,RuiWang,JunliangGuo,BeiLi,KaitaoSong,XuTan,GuoqingLiu,JiangBian,and
YujiuYang. ConnectingLargeLanguageModelswithEvolutionaryAlgorithmsYieldsPowerful
PromptOptimizers,September2023.
InmanHarvey. Themicrobialgeneticalgorithm. InAdvancesinArtificialLife.DarwinMeetsvon
Neumann: 10thEuropeanConference,ECAL2009,Budapest,Hungary,September13-16,2009,
RevisedSelectedPapers,PartII10,pp.126–133.Springer,2011.
MarkHauschildandMartinPelikan. Anintroductionandsurveyofestimationofdistributionalgorithms. Swarmandevolutionarycomputation,1(3):111–128,2011.
OrHonovich,UriShaham,SamuelR.Bowman,andOmerLevy. Instructioninduction: Fromfew
examples to natural language task descriptions. In Anna Rogers, Jordan L. Boyd-Graber, and
Naoaki Okazaki (eds.), Proceedings of the 61st Annual Meeting of the Association for ComputationalLinguistics(Volume1: LongPapers),ACL2023,Toronto,Canada,July9-14,2023,pp.
1935–1952. Association for Computational Linguistics, 2023. doi: 10.18653/v1/2023.acl-long.

## URLhttps://doi.org/10.18653/v1/2023.acl-long.108.

Mohammad Javad Hosseini, Hannaneh Hajishirzi, Oren Etzioni, and Nate Kushman. Learning to
solvearithmeticwordproblemswithverbcategorization. InProceedingsofthe2014Conference
on Empirical Methods in Natural Language Processing (EMNLP), pp. 523–533, Doha, Qatar,
October 2014. Association for Computational Linguistics. doi: 10.3115/v1/D14-1058. URL
https://aclanthology.org/D14-1058.
Cheng-Yu Hsieh, Chun-Liang Li, Chih-Kuan Yeh, Hootan Nakhost, Yasuhisa Fujii, Alex Ratner,
RanjayKrishna,Chen-YuLee,andTomasPfister. Distillingstep-by-step! outperforminglarger
languagemodelswithlesstrainingdataandsmallermodelsizes.InAnnaRogers,JordanL.Boyd-
Graber, and Naoaki Okazaki (eds.), Findings of the Association for Computational Linguistics:
ACL 2023, Toronto, Canada, July 9-14, 2023, pp. 8003–8017. Association for Computational
Linguistics, 2023. doi: 10.18653/v1/2023.findings-acl.507. URL https://doi.org/10.
18653/v1/2023.findings-acl.507.
Jiaxin Huang, Shixiang Shane Gu, Le Hou, Yuexin Wu, Xuezhi Wang, Hongkun Yu, and Jiawei
Han. Large language models can self-improve. CoRR, abs/2210.11610, 2022. doi: 10.48550/
arXiv.2210.11610. URLhttps://doi.org/10.48550/arXiv.2210.11610.
Kazuki Irie, Imanol Schlag, Ro´bert Csorda´s, and Ju¨rgen Schmidhuber. A modern self-referential
weight matrix that learns to modify itself. In Kamalika Chaudhuri, Stefanie Jegelka, Le Song,
Csaba Szepesva´ri, Gang Niu, and Sivan Sabato (eds.), International Conference on Machine
11

<!-- Page 12 -->

Learning, ICML 2022, 17-23 July 2022, Baltimore, Maryland, USA, volume 162 of Proceedings of Machine Learning Research, pp. 9660–9677. PMLR, 2022. URL https://
proceedings.mlr.press/v162/irie22b.html.
Max Jaderberg, Valentin Dalibard, Simon Osindero, Wojciech M. Czarnecki, Jeff Donahue, Ali
Razavi, Oriol Vinyals, Tim Green, Iain Dunning, Karen Simonyan, Chrisantha Fernando, and
Koray Kavukcuoglu. Population based training of neural networks. CoRR, abs/1711.09846,
2017a. URLhttp://arxiv.org/abs/1711.09846.
Max Jaderberg, Volodymyr Mnih, Wojciech Marian Czarnecki, Tom Schaul, Joel Z. Leibo, David
Silver,andKorayKavukcuoglu.Reinforcementlearningwithunsupervisedauxiliarytasks.In5th
InternationalConferenceonLearningRepresentations,ICLR2017,Toulon,France,April24-26,
2017,ConferenceTrackProceedings.OpenReview.net,2017b.URLhttps://openreview.
net/forum?id=SJ6yPD5xg.
Minqi Jiang, Michael Dennis, Jack Parker-Holder, Jakob N. Foerster, Edward Grefenstette, and
Tim Rockta¨schel. Replay-guided adversarial environment design. In Marc’Aurelio Ranzato, Alina Beygelzimer, Yann N. Dauphin, Percy Liang, and Jennifer Wortman Vaughan
(eds.), Advances in Neural Information Processing Systems 34: Annual Conference on Neural Information Processing Systems 2021, NeurIPS 2021, December 6-14, 2021, virtual, pp.
1884–1897, 2021a. URLhttps://proceedings.neurips.cc/paper/2021/hash/
0e915db6326b6fb6a3c56546980a8c93-Abstract.html.
MinqiJiang,EdwardGrefenstette,andTimRockta¨schel. Prioritizedlevelreplay. InMarinaMeila
andTongZhang(eds.),Proceedingsofthe38thInternationalConferenceonMachineLearning,
ICML2021,18-24July2021,VirtualEvent,volume139ofProceedingsofMachineLearningResearch,pp.4940–4950.PMLR,2021b. URLhttp://proceedings.mlr.press/v139/
jiang21b.html.
Minqi Jiang, Tim Rockta¨schel, and Edward Grefenstette. General intelligence requires rethinking
exploration. CoRR, abs/2211.07819, 2022. doi: 10.48550/arXiv.2211.07819. URL https:
//doi.org/10.48550/arXiv.2211.07819.
LouisKirschandJu¨rgenSchmidhuber. Eliminatingmetaoptimizationthroughself-referentialmeta
learning. CoRR, abs/2212.14392, 2022. doi: 10.48550/arXiv.2212.14392. URL https://
doi.org/10.48550/arXiv.2212.14392.
Takeshi Kojima, Shixiang Shane Gu, Machel Reid, Yutaka Matsuo, and Yusuke
Iwasawa. Large language models are zero-shot reasoners. In NeurIPS, 2022.

### URL http://papers.nips.cc/paper_files/paper/2022/hash/

8bb0d291acd4acf06ef112099c16f326-Abstract-Conference.html.
Rik Koncel-Kedziorski, Hannaneh Hajishirzi, Ashish Sabharwal, Oren Etzioni, and Siena Dumas Ang. Parsing algebraic word problems into equations. Transactions of the Association
for Computational Linguistics, 3:585–597, 2015. doi: 10.1162/tacl a 00160. URL https:
//aclanthology.org/Q15-1042.
Joel Lehman and Kenneth O. Stanley. Evolving a diversity of virtual creatures through novelty
search and local competition. In Natalio Krasnogor and Pier Luca Lanzi (eds.), 13th Annual
GeneticandEvolutionaryComputationConference,GECCO2011,Proceedings,Dublin,Ireland,
July 12-16, 2011, pp. 211–218. ACM, 2011a. doi: 10.1145/2001576.2001606. URL https:
//doi.org/10.1145/2001576.2001606.
Joel Lehman and Kenneth O. Stanley. Abandoning Objectives: Evolution Through the Search for
NoveltyAlone. EvolutionaryComputation,19(2):189–223,June2011b. ISSN1063-6560. doi:
10.1162/EVCO a 00025.
JoelLehman,JonathanGordon,ShawnJain,KamalNdousse,CathyYeh,andKennethO.Stanley.
Evolutionthroughlargemodels. CoRR,abs/2206.08896,2022. doi:10.48550/arXiv.2206.08896.
URLhttps://doi.org/10.48550/arXiv.2206.08896.
12

<!-- Page 13 -->

BrianLester,RamiAl-Rfou,andNoahConstant. Thepowerofscaleforparameter-efficientprompt
tuning. InMarie-FrancineMoens,XuanjingHuang,LuciaSpecia,andScottWen-tauYih(eds.),
Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing,
EMNLP2021,VirtualEvent/PuntaCana,DominicanRepublic,7-11November,2021,pp.3045–

### AssociationforComputationalLinguistics,2021. doi:10.18653/v1/2021.emnlp-main.243.

URLhttps://doi.org/10.18653/v1/2021.emnlp-main.243.
Wang Ling, Dani Yogatama, Chris Dyer, and Phil Blunsom. Program induction by rationale generation: Learning to solve and explain algebraic word problems. In Proceedings of the 55th
Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers),
pp. 158–167, Vancouver, Canada, July 2017. Association for Computational Linguistics. doi:
10.18653/v1/P17-1015. URLhttps://aclanthology.org/P17-1015.
NelsonF.Liu,KevinLin,JohnHewitt,AshwinParanjape,MicheleBevilacqua,FabioPetroni,and
PercyLiang.Lostinthemiddle:Howlanguagemodelsuselongcontexts.CoRR,abs/2307.03172,
2023. doi: 10.48550/arXiv.2307.03172. URL https://doi.org/10.48550/arXiv.
2307.03172.
Xiao Liu, Yanan Zheng, Zhengxiao Du, Ming Ding, Yujie Qian, Zhilin Yang, and Jie Tang. GPT
understands, too. CoRR, abs/2103.10385, 2021. URL https://arxiv.org/abs/2103.
10385.
Yao Lu, Max Bartolo, Alastair Moore, Sebastian Riedel, and Pontus Stenetorp. Fantastically
ordered prompts and where to find them: Overcoming few-shot prompt order sensitivity. In
SmarandaMuresan, PreslavNakov, andAlineVillavicencio(eds.), Proceedingsofthe60thAnnual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), ACL
2022,Dublin,Ireland,May22-27,2022,pp.8086–8098.AssociationforComputationalLinguistics,2022. doi: 10.18653/v1/2022.acl-long.556. URLhttps://doi.org/10.18653/v1/
2022.acl-long.556.
AmanMadaanandAmirYazdanbakhsh. Textandpatterns: Foreffectivechainofthought,ittakes
two to tango. CoRR, abs/2209.07686, 2022. doi: 10.48550/arXiv.2209.07686. URL https:
//doi.org/10.48550/arXiv.2209.07686.
Aman Madaan, Niket Tandon, Prakhar Gupta, Skyler Hallinan, Luyu Gao, Sarah Wiegreffe, Uri
Alon,NouhaDziri,ShrimaiPrabhumoye,YimingYang,SeanWelleck,BodhisattwaPrasadMajumder, Shashank Gupta, Amir Yazdanbakhsh, and Peter Clark. Self-refine: Iterative refinementwithself-feedback. CoRR,abs/2303.17651,2023. doi: 10.48550/arXiv.2303.17651. URL
https://doi.org/10.48550/arXiv.2303.17651.
ElliotMeyerson,MarkJ.Nelson,HerbieBradley,ArashMoradi,AmyK.Hoover,andJoelLehman.
Languagemodelcrossover:Variationthroughfew-shotprompting.CoRR,abs/2302.12170,2023.
doi: 10.48550/arXiv.2302.12170. URL https://doi.org/10.48550/arXiv.2302.
12170.
Suvir Mirchandani, Fei Xia, Pete Florence, Brian Ichter, Danny Driess, Montserrat Gonzalez
Arenas, Kanishka Rao, Dorsa Sadigh, and Andy Zeng. Large language models as general
pattern machines. CoRR, abs/2307.04721, 2023. doi: 10.48550/arXiv.2307.04721. URL
https://doi.org/10.48550/arXiv.2307.04721.
Ioannis Mollas, Zoe Chrysopoulou, Stamatis Karlos, and Grigorios Tsoumakas. ETHOS: a
multi-label hate speech detection dataset. Complex and Intelligent Systems, 8(6):4663–4678,
jan 2022. doi: 10.1007/s40747-021-00608-2. URL https://doi.org/10.1007%
2Fs40747-021-00608-2.
Milad Moradi and Matthias Samwald. Evaluating the robustness of neural language models to
input perturbations. In Marie-Francine Moens, Xuanjing Huang, Lucia Specia, and Scott WentauYih(eds.),Proceedingsofthe2021ConferenceonEmpiricalMethodsinNaturalLanguage
Processing, EMNLP 2021, Virtual Event / Punta Cana, Dominican Republic, 7-11 November,
2021,pp.1558–1570.AssociationforComputationalLinguistics,2021. doi: 10.18653/v1/2021.
emnlp-main.117. URLhttps://doi.org/10.18653/v1/2021.emnlp-main.117.
13

<!-- Page 14 -->

Jean-Baptiste Mouret and Jeff Clune. Illuminating search spaces by mapping elites. CoRR,
abs/1504.04909,2015. URLhttp://arxiv.org/abs/1504.04909.
MaxwellI.Nye,AndersJohanAndreassen,GuyGur-Ari,HenrykMichalewski,JacobAustin,David
Bieber,DavidDohan,AitorLewkowycz,MaartenBosma,DavidLuan,CharlesSutton,andAugustusOdena.Showyourwork:Scratchpadsforintermediatecomputationwithlanguagemodels.
CoRR,abs/2112.00114,2021. URLhttps://arxiv.org/abs/2112.00114.
Michael O¨llinger and Gu¨nther Knoblich. Psychological research on insight problem solving. In
Recastingreality: WolfgangPauli’sphilosophicalideasandcontemporaryscience,pp.275–300.
Springer,2009.
Joon Sung Park, Joseph C. O’Brien, Carrie J. Cai, Meredith Ringel Morris, Percy Liang, and
Michael S. Bernstein. Generative agents: Interactive simulacra of human behavior. CoRR,
abs/2304.03442, 2023. doi: 10.48550/arXiv.2304.03442. URL https://doi.org/10.
48550/arXiv.2304.03442.
Jack Parker-Holder, Minqi Jiang, Michael Dennis, Mikayel Samvelyan, Jakob N. Foerster, Edward Grefenstette, and Tim Rockta¨schel. Evolving curricula with regret-based environment
design. In Kamalika Chaudhuri, Stefanie Jegelka, Le Song, Csaba Szepesva´ri, Gang Niu,
and Sivan Sabato (eds.), International Conference on Machine Learning, ICML 2022, 17-23
July 2022, Baltimore, Maryland, USA, volume 162 of Proceedings of Machine Learning Research, pp. 17473–17498. PMLR, 2022. URL https://proceedings.mlr.press/
v162/parker-holder22a.html.
Arkil Patel, Satwik Bhattamishra, and Navin Goyal. Are NLP models really able to solve simple math word problems? In Kristina Toutanova, Anna Rumshisky, Luke Zettlemoyer, Dilek
Hakkani-Tu¨r, Iz Beltagy, Steven Bethard, Ryan Cotterell, Tanmoy Chakraborty, and Yichao
Zhou (eds.), Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, NAACL-HLT 2021,
Online, June 6-11, 2021, pp. 2080–2094. Association for Computational Linguistics, 2021.
doi: 10.18653/v1/2021.naacl-main.168. URL https://doi.org/10.18653/v1/2021.
naacl-main.168.
JoshuaL.PayneandAndreasWagner. Thecausesofevolvabilityandtheirevolution. NatureReviewsGenetics,20(1):24–38,January2019. ISSN1471-0064. doi: 10.1038/s41576-018-0069-z.
MassimoPigliucci. Isevolvabilityevolvable? NatureReviewsGenetics,9(1):75–82,January2008.
ISSN1471-0064. doi: 10.1038/nrg2278.
ReidPryzant,DanIter,JerryLi,YinTatLee,ChenguangZhu,andMichaelZeng.Automaticprompt
optimizationwith”gradientdescent”andbeamsearch. arXivpreprintarXiv:2305.03495,2023.
Guanghui Qin and Jason Eisner. Learning How to Ask: Querying LMs with Mixtures of Soft
Prompts,April2021.
Subhro Roy and Dan Roth. Solving general arithmetic word problems. arXiv preprint
arXiv:1608.01413,2016.
TimoSchick,JaneDwivedi-Yu,RobertoDess`ı,RobertaRaileanu,MariaLomeli,LukeZettlemoyer,
NicolaCancedda,andThomasScialom. Toolformer: LanguageModelsCanTeachThemselves
toUseTools,February2023.
J. Schmidhuber. A ‘Self-Referential’ Weight Matrix. In Stan Gielen and Bert Kappen (eds.),
ICANN ’93, pp. 446–450, London, 1993. Springer. ISBN 978-1-4471-2063-6. doi: 10.1007/
978-1-4471-2063-6 107.
Ju¨rgen Schmidhuber. Making the world differentiable: On using fully recurrent self-supervised
neuralnetworksfordynamicreinforcementlearningandplanninginnon-stationaryenvironments.
1990.
Ju¨rgenSchmidhuber. LearningtoControlFast-WeightMemories: AnAlternativetoDynamicRecurrent Networks. Neural Computation, 4(1):131–139, January 1992. ISSN 0899-7667. doi:
10.1162/neco.1992.4.1.131.
14

<!-- Page 15 -->

Ju¨rgenSchmidhuber. Go¨delmachines: self-referentialuniversalproblemsolversmakingprovably
optimalself-improvements. arXivpreprintcs/0309048,2003.
JimmySecretan,NicholasBeato,DavidB.DAmbrosio,AdeleinRodriguez,AdamCampbell,and
KennethO.Stanley. Picbreeder: Evolvingpicturescollaborativelyonline. InProceedingsofthe
SIGCHI Conference on Human Factors in Computing Systems, CHI ’08, pp. 1759–1768, New
York,NY,USA,April2008.AssociationforComputingMachinery. ISBN978-1-60558-011-1.
doi: 10.1145/1357054.1357328.
OferMShirandThomasBa¨ck. Nichinginevolutionstrategies. InProceedingsofthe7thannual
conferenceonGeneticandevolutionarycomputation,pp.915–916,2005.
KashunShum,ShizheDiao,andTongZhang. Automaticpromptaugmentationandselectionwith
chain-of-thought from labeled data. CoRR, abs/2302.12822, 2023. doi: 10.48550/arXiv.2302.

## URLhttps://doi.org/10.48550/arXiv.2302.12822.

AlonTalmor,JonathanHerzig,NicholasLourie,andJonathanBerant. CommonsenseQA:Aquestion answering challenge targeting commonsense knowledge. In Proceedings of the 2019 ConferenceoftheNorthAmericanChapteroftheAssociationforComputationalLinguistics:Human
LanguageTechnologies,Volume1(LongandShortPapers),pp.4149–4158,Minneapolis,Minnesota,June2019.AssociationforComputationalLinguistics.doi:10.18653/v1/N19-1421.URL
https://aclanthology.org/N19-1421.
Guanzhi Wang, Yuqi Xie, Yunfan Jiang, Ajay Mandlekar, Chaowei Xiao, Yuke Zhu, Linxi Fan,
andAnimaAnandkumar. Voyager: Anopen-endedembodiedagentwithlargelanguagemodels.
CoRR,abs/2305.16291,2023a. doi: 10.48550/arXiv.2305.16291. URLhttps://doi.org/
10.48550/arXiv.2305.16291.
Lei Wang, Wanyu Xu, Yihuai Lan, Zhiqiang Hu, Yunshi Lan, Roy Ka-Wei Lee, and Ee-Peng
Lim. Plan-and-solve prompting: Improving zero-shot chain-of-thought reasoning by large language models. In Anna Rogers, Jordan L. Boyd-Graber, and Naoaki Okazaki (eds.), Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), ACL 2023, Toronto, Canada, July 9-14, 2023, pp. 2609–2634. Association for Computational Linguistics, 2023b. doi: 10.18653/v1/2023.acl-long.147. URL
https://doi.org/10.18653/v1/2023.acl-long.147.
XuezhiWang,JasonWei,DaleSchuurmans,QuocLe,EdChi,SharanNarang,AakankshaChowdhery,andDennyZhou. Self-consistencyimproveschainofthoughtreasoninginlanguagemodels.
arXivpreprintarXiv:2203.11171,2022.
YizhongWang,YeganehKordi,SwaroopMishra,AlisaLiu,NoahA.Smith,DanielKhashabi,and
Hannaneh Hajishirzi. Self-instruct: Aligning language models with self-generated instructions.
InAnnaRogers,JordanL.Boyd-Graber,andNaoakiOkazaki(eds.),Proceedingsofthe61stAnnual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), ACL
2023,Toronto,Canada,July9-14,2023,pp.13484–13508.AssociationforComputationalLinguistics,2023c.doi:10.18653/v1/2023.acl-long.754.URLhttps://doi.org/10.18653/
v1/2023.acl-long.754.
Zihao Wang, Shaofei Cai, Anji Liu, Xiaojian Ma, and Yitao Liang. Describe, explain, plan and
select: Interactive planning with large language models enables open-world multi-task agents.
CoRR,abs/2302.01560,2023d. doi: 10.48550/arXiv.2302.01560. URLhttps://doi.org/
10.48550/arXiv.2302.01560.
Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Brian Ichter, Fei Xia, Ed H. Chi,
Quoc V. Le, and Denny Zhou. Chain-of-thought prompting elicits reasoning in large language
models. In NeurIPS, 2022. URL http://papers.nips.cc/paper_files/paper/
2022/hash/9d5609613524ecf4f15af0f7b31abca4-Abstract-Conference.
html.
YueWu, ShrimaiPrabhumoye, SoYeonMin, YonatanBisk, RuslanSalakhutdinov, AmosAzaria,
Tom M. Mitchell, and Yuanzhi Li. SPRING: GPT-4 out-performs RL algorithms by studying
papers and reasoning. CoRR, abs/2305.15486, 2023. doi: 10.48550/arXiv.2305.15486. URL
https://doi.org/10.48550/arXiv.2305.15486.
15

<!-- Page 16 -->

Chengrun Yang, Xuezhi Wang, Yifeng Lu, Hanxiao Liu, Quoc V. Le, Denny Zhou, and Xinyun
Chen. Large language models as optimizers. CoRR, abs/2309.03409, 2023a. doi: 10.48550/
arXiv.2309.03409. URLhttps://doi.org/10.48550/arXiv.2309.03409.
ZhengyuanYang, LinjieLi, JianfengWang, KevinLin, EhsanAzarnasab, FaisalAhmed, Zicheng
Liu, Ce Liu, Michael Zeng, and Lijuan Wang. Mm-react: Prompting chatgpt for multimodal
reasoningandaction. arXivpreprintarXiv:2303.11381,2023b.
Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, and Yuan Cao.
React: Synergizingreasoningandactinginlanguagemodels. arXivpreprintarXiv:2210.03629,
2022.
Shunyu Yao, Dian Yu, Jeffrey Zhao, Izhak Shafran, Thomas L. Griffiths, Yuan Cao, and Karthik
Narasimhan. TreeofThoughts: DeliberateProblemSolvingwithLargeLanguageModels,May
2023.
EricZelikman,YuhuaiWu,JesseMu,andNoahD.Goodman. Star: Bootstrappingreasoningwith
reasoning. InNeurIPS,2022. URLhttp://papers.nips.cc/paper_files/paper/
2022/hash/639a9a172c044fbb64175b5fad42e9a5-Abstract-Conference.
html.
JennyZhang,JoelLehman,KennethO.Stanley,andJeffClune.OMNI:open-endednessviamodels
ofhumannotionsofinterestingness. CoRR,abs/2306.01711,2023a. doi: 10.48550/arXiv.2306.

## URLhttps://doi.org/10.48550/arXiv.2306.01711.

Zhuosheng Zhang, Aston Zhang, Mu Li, and Alex Smola. Automatic chain of thought prompting in large language models. In The Eleventh International Conference on Learning Representations, ICLR 2023, Kigali, Rwanda, May 1-5, 2023. OpenReview.net, 2023b. URL
https://openreview.net/pdf?id=5NTt8GFjUHkr.
Denny Zhou, Nathanael Scha¨rli, Le Hou, Jason Wei, Nathan Scales, Xuezhi Wang, Dale Schuurmans, Claire Cui, Olivier Bousquet, Quoc Le, et al. Least-to-most prompting enables complex
reasoninginlargelanguagemodels. arXivpreprintarXiv:2205.10625,2022.
Yongchao Zhou, Andrei Ioan Muresanu, Ziwen Han, Keiran Paster, Silviu Pitis, Harris Chan, and
Jimmy Ba. Large language models are human-level prompt engineers. In The Eleventh InternationalConferenceonLearningRepresentations,ICLR2023,Kigali,Rwanda,May1-5,2023.
OpenReview.net,2023. URLhttps://openreview.net/pdf?id=92gvk82DE-.
16

<!-- Page 17 -->


## A Glossary

EstimationofDistributionAlgorithm Anoptimizationalgorithmthatiterativelyrefinesaprobabilisticmodelofpromisingsolutions,oftenusingthewholepopulationasaguide.
FitnessProportionateSelection AlsoknowsasRoulette-WheelSelection,anindividualischosen
inproportiontoitsfitnessinthepopulation.
MutationPrompt The text prompt which when concatenated to the task-prompt is intended to
produceacontinuationwhichisanimprovedtask-prompt.
Problemdescription The initial text description of the problem which could be used as the initial task-prompt. The user can make their best attempt to produce an effective problem
description,whichisthestartingpointofPromptbreeder.
PromptStrategy A set of task-prompts and rules for their application at inference time during a
fitness evaluation. In the minimal case the prompt strategy is just a single task-prompt.
Typicallyourpromptstrategiesconsistedoftwosequentiallyappliedtask-prompts.
Phenotype/Workingsout/Context/ReasoningPath Used interchangeably to mean the output of
theLLMonaspecificquestionorproblemwhenpromptedwiththetask-promptconcatenatedtothequestion.
Population Thesetofunitsofevolution(e.g. 50).
Unitofevolution The informational structure that is being evolved, here consisting of a taskpromptset(typically2),amutation-prompt,andinthefew-shotcaseasetof2-3contexts
(workingsout).

## B A Typical Evolutionary Run

Thewordincontexttaskisoneofthe24instructioninductiontasksusedinAPE.Giventwosentences and a homograph word, the LLM must determine whether the homograph word has been
usedwiththesamemeaninginbothsentences. Figure3showsanevolutionaryrunwherebluedots
are individual fitness evaluations and the red line is the population mean. Over 2000 evaluations,
thefitnessincreasesconsiderably. ThebestevolvedPrompt1andPrompt2pairs(evaluatedonthe
trainingset)areshownontheright.
17

<!-- Page 18 -->

100
80
60
40
20
0
0 250 500 750 1000 1250 1500 1750 2000
Evaluations
ssentiF
Prompt 1: "Sentences are given, and a single word. The output should indicate
whether the given word has the same sense in the two given sentences, yes or
no."
Prompt 2: "Sentences are given, and a single word. The answer should indicate
whether the given word has the same meaning in the two given sentences, yes or
no.""
Prompt 1: "'Identify if the word in bold font below is used with the same
word_in_context (65914156) meaning in the two sentences below it. The word in bold may be used as different
parts of speech in the two sentences.. I think the if should come before "
Prompt 2: "Answer by following a template like: Sentences are given, and a
single word. The answer should indicate whether the given word has the same
meaning in the two given sentences, yes or no."
Prompt 1: "Sentences are given, and a single word. The output should indicate
whether the given word has the same meaning in the two given sentences, yes or
no"
Prompt 2: ""Identify if the word in bold font below is used with the same
meaning in the two sentences below it. The word in bold may be used as different
parts of speech in the two sentences." . I think 'same' should come between"
Prompt 1: "Sentences are given, and a single word. The answer should indicate
whether the given word has the same meaning in the two given sentences, yes or
no"
Prompt 2: ""Identify if the word in bold font below is used with the same
meaning in the two sentences below it. The word in bold may be used as different
parts of speech in the two sentences." . I think 'same' should come between"
Prompt 1: ": I'll give you two sentences and a word. Your task is to write if
the meaning of the word is the same in both sentences or not."
Prompt 2: ""Identify if the word in bold font below is used with the same
meaning in the two sentences below it. The word in bold may be used as different
parts of speech in the two sentences." . I think 'same' should come between"
Prompt 1: ": I'll give you two sentences and a word. Your task is to write if
the meaning of the word is the same in both sentences or not."
Prompt 2: "Your mission is to replace W in the first sentence with the most
similar word in terms of usage from the second sentence such that both the
meaning and the grammatical validity of the first sentence do not get distorted
after replacement.\n"

### Prompt 1: "as follows:"

Prompt 2: ": In each input, you will be given two sentences and a word. Decide
whether the word means the same thing in both sentences. Type same if it does,
and not the same if it doesn't."
Figure 3: A typical evolutionary run in which a prompt strategy consisting of two sequentially
appliedpromptsisevolvedtosolvethewordincontexttaskfromtheAPE24instructioninduction
task. Seetheprogressioninthepromptsevolvedthroughtherun. Theelitepromptsareshownas
theyappear. Bluedotsshowtrainingsetevaluations. Redlineshowsthepopulationmeanfitness.

## C Mutation Prompts

Table2: MutatorPrompts

### Index Prompt

1 Modifythefollowinginstructioncreatively,givingsomeadviceonhowtosolve
it:
2 Justchangethisinstructiontomakeitmorefun,thinkWELLoutsidethebox:
3 Modifythisinstructioninawaythatnoself-respectingLLMwould!
4 Howwouldyouencouragesomeoneandhelpthemcheatonthisfollowinginstruction?
5 HowwouldyouhelpanLLMtofollowtheinstruction?
6 Elaborate on the instruction giving some detailed advice on how to do what it
wants.
7 Elaborate on the instruction giving some detailed advice on how to do what it
wants,asifyouwereexplainingittoachild.
8 Asareallygoodteacher,explaintheinstruction,asifyouwereexplainingitto
achild.
Continuedonnextpage
18

<!-- Page 19 -->

Table2–continuedfrompreviouspage

### Index Prompt

9 Imagineyouneedtofollowthisinstruction.Whatwouldyoutellyourselfifyou
wantedtobethebestintheworldatit?
10 Howwouldsomeonewithderailmentfollowthisinstruction?
11 Don’t think about the instruction at all, but let it inspire you to do something
related. Talkaboutwhatthatmightbe.
12 Rephrasetheinstructionwithoutusinganyofthesamewords.Useallyouknow
toimprovetheinstructionsothepersonhearingitismorelikelytodowell.
13 Saythatinstructionagain inanotherway. DON’T useanyof thewordsin the
originalinstructionoryou’refired.
14 Saythatinstructionagain inanotherway. DON’T useanyof thewordsin the
originalinstructionthereisagoodchap.
15 Whatdopeoplewhoaregoodatcreativethinkingnormallydowiththiskindof
mutationquestion?
16 Detailed additional advice for people wishing to follow this instruction is as
follows:
17 Inoneshortsentence,hereishowIwouldbestfollowthisinstruction.
18 Inoneshortsentence, hereissomedetailedexpertadvice. NoticehowIdon’t
useanyofthesamewordsasintheINSTRUCTION.
19 Inoneshortsentence,thegeneralsolutionisasfollows. NoticehowIdon’tuse
anyofthesamewordsasintheINSTRUCTION.
20 In one short sentence, what’s a good prompt to get a language model to solve
a problem like this? Notice how I don’t use any of the same words as in the

## Instruction.

21 Generate a mutated version of the following prompt by adding an unexpected
twist.
22 Createapromptmutantthatintroducesasurprisingcontradictiontotheoriginal
prompt. Mutatetheprompttoprovideanalternativeperspectiveorviewpoint.
23 Generateapromptmutantthatincorporateshumororaplayfulelement. Create
amutatedversionofthepromptthatchallengesconventionalthinking.
24 Developapromptmutantbyreplacingspecifickeywordswithrelatedbutunexpectedterms. Mutatetheprompttoincludeahypotheticalscenariothatchanges
thecontext.
25 Generate a prompt mutant that introduces an element of suspense or intrigue.
Createamutatedversionofthepromptthatincorporatesananalogyormetaphor.
26 Developapromptmutantbyrephrasingtheoriginalpromptinapoeticorlyrical
style. Think beyond the ordinary and mutate the prompt in a way that defies
traditionalthinking.
27 Break free from conventional constraints and generate a mutator prompt that
takestheprompttounchartedterritories. Challengethenormandcreateamutatorpromptthatpushestheboundariesoftraditionalinterpretations.
28 Embraceunconventionalideasandmutatethepromptinawaythatsurprisesand
inspiresuniquevariations. Thinkoutsidetheboxanddevelopamutatorprompt
thatencouragesunconventionalapproachesandfreshperspectives.
29 Stepintotherealmofimaginationandcreateamutatorpromptthattranscends
limitations and encourages innovative mutations. Break through the ordinary
andthinkoutsidetheboxtogenerateamutatorpromptthatunlocksnewpossibilitiesandunconventionalpaths.
30 Embracethepowerofunconventionalthinkingandcreateamutatorpromptthat
sparks unconventional mutations and imaginative outcomes. Challenge traditional assumptions and break the mold with a mutator prompt that encourages
revolutionaryandout-of-the-boxvariations.
31 Go beyond the expected and create a mutator prompt that leads to unexpected
and extraordinary mutations, opening doors to unexplored realms. Increase
Specificity: If the original prompt is too general, like ’Tell me about X,’ the
modifiedversioncouldbe,’Discussthehistory,impact,andcurrentstatusofX.’
Continuedonnextpage
19

<!-- Page 20 -->

Table2–continuedfrompreviouspage

### Index Prompt

32 Ask for Opinions/Analysis: If the original prompt only asks for a fact, such
as ’What is X?’, the improved prompt could be, ’What is X, and what are its
implicationsforY?’
33 Encourage Creativity: For creative writing prompts like ’Write a story about
X,’animprovedversioncouldbe,’WriteafantasystoryaboutXsetinaworld
whereYispossible.’
34 Include Multiple Perspectives: For a prompt like ’What is the impact of X on
Y?’, an improved version could be, ’What is the impact of X on Y from the
perspectiveofA,B,andC?’
35 Request More Detailed Responses: If the original prompt is ’Describe X,’ the
improvedversioncouldbe,’DescribeX,focusingonitsphysicalfeatures,historicalsignificance,andculturalrelevance.’
36 CombineRelatedPrompts: Ifyouhavetworelatedprompts, youcancombine
them to create a more complex and engaging question. For instance, ’What is
X?’and’WhyisYimportant?’ couldbecombinedtoform’WhatisXandwhy
isitimportantinthecontextofY?’
37 BreakDownComplexQuestions: Ifapromptseemstoocomplex,like’Discuss
X,’theimprovedversioncouldbe, ’WhatisX?Whatareitsmaincharacteristics? WhateffectsdoesithaveonYandZ?’
38 Use Open-Ended Questions: Instead of ’Is X true?’, you could ask, ’What are
theargumentsforandagainstthetruthofX?’
39 Request Comparisons: Instead of ’Describe X,’ ask ’Compare and contrast X
andY.’
40 Include Context: If a prompt seems to lack context, like ’Describe X,’ the improved version could be, ’Describe X in the context of its impact on Y during
theZperiod.’
41 Makethepromptmorevisual: Asktheusertovisualizetheproblemorscenario
beingpresentedintheprompt.
42 Askforathoroughreview: Insteadofjustpresentingtheproblem,asktheuser
towritedownalltherelevantinformationandidentifywhat’smissing.
43 Invokepreviousexperiences: Modifytheprompttoasktheusertorecallasimilarproblemthey’vesuccessfullysolvedbefore.
44 Encourageafreshperspective: Suggestinyourpromptthattheusertakeamomenttocleartheirmindbeforere-approachingtheproblem.
45 Promotebreakingdownproblems: Insteadofaskingtheusertosolvetheproblem as a whole, prompt them to break it down into smaller, more manageable
parts.
46 Askforcomprehension: Modifytheprompttoasktheusertoreviewandconfirmtheirunderstandingofallaspectsoftheproblem.
47 Suggestexplanationtoothers: Changetheprompttosuggestthattheusertryto
explaintheproblemtosomeoneelseasawaytosimplifyit.
48 Promptforsolutionvisualization:Insteadofjustaskingforthesolution,encouragetheusertoimaginethesolutionandthestepsrequiredtogetthereinyour
prompt.
49 Encourage reverse thinking: Improve the prompt by asking the user to think
abouttheprobleminreverse,startingwiththesolutionandworkingbackwards.
50 Recommendtakingabreak: Modifytheprompttosuggestthattheusertakea
shortbreak,allowingtheirsubconscioustoworkontheproblem.
51 Whaterrorsarethereinthesolution?
52 Howcouldyouimprovetheworkingoutoftheproblem?
53 Lookcarefullytoseewhatyoudidwrong,howcouldyoufixtheproblem?

## 54 Correction=

55 Doestheabovetextmakesense? Whatseemswrongwithit? Hereisanattempt
tofixit:
56 Theaboveworkingouthassomeerrors,hereisaversionwiththeerrorsfixed.
20

<!-- Page 21 -->


## D Thinking Styles


### Index ThinkingStyle

1 HowcouldIdeviseanexperimenttohelpsolvethatproblem?
2 Make a list of ideas for solving this problem, and apply them one by
onetotheproblemtoseeifanyprogresscanbemade.
3 HowcouldImeasureprogressonthisproblem?
4 HowcanIsimplifytheproblemsothatitiseasiertosolve?
5 Whatarethekeyassumptionsunderlyingthisproblem?
6 Whatarethepotentialrisksanddrawbacksofeachsolution?
7 Whatarethealternativeperspectivesorviewpointsonthisproblem?
8 Whatarethelong-termimplicationsofthisproblemanditssolutions?
9 How can I break down this problem into smaller, more manageable
parts?
10 Critical Thinking: This style involves analyzing the problem from
different perspectives, questioning assumptions, and evaluating the
evidence or information available. It focuses on logical reasoning,
evidence-based decision-making, and identifying potential biases or
flawsinthinking.
11 Try creative thinking, generate innovative and out-of-the-box ideas to
solvetheproblem. Exploreunconventionalsolutions,thinkingbeyond
traditionalboundaries,andencouragingimaginationandoriginality.
12 Seekinputandcollaborationfromotherstosolvetheproblem. Emphasize teamwork, open communication, and leveraging the diverse perspectivesandexpertiseofagrouptocomeupwitheffectivesolutions.
13 Usesystemsthinking: Considertheproblemaspartofalargersystem
andunderstandingtheinterconnectednessofvariouselements. Focuses
on identifying the underlying causes, feedback loops, and interdependencies that influence the problem, and developing holistic solutions
thataddressthesystemasawhole.
14 Use Risk Analysis: Evaluate potential risks, uncertainties, and tradeoffsassociatedwithdifferentsolutionsorapproachestoaproblem.Emphasizeassessingthepotentialconsequencesandlikelihoodofsuccess
orfailure,andmakinginformeddecisionsbasedonabalancedanalysis
ofrisksandbenefits.
15 Use Reflective Thinking: Step back from the problem, take the time
forintrospectionandself-reflection. Examinepersonalbiases,assumptions,andmentalmodelsthatmayinfluenceproblem-solving,andbeing
opentolearningfrompastexperiencestoimprovefutureapproaches.
16 Whatisthecoreissueorproblemthatneedstobeaddressed?
17 Whataretheunderlyingcausesorfactorscontributingtotheproblem?
18 Are there any potential solutions or strategies that have been tried before? Ifyes,whatweretheoutcomesandlessonslearned?
19 Whatarethepotentialobstaclesorchallengesthatmightariseinsolving
thisproblem?
20 Arethereanyrelevantdataorinformationthatcanprovideinsightsinto
theproblem? Ifyes,whatdatasourcesareavailable,andhowcanthey
beanalyzed?
21 Are there any stakeholders or individuals who are directly affected by
theproblem? Whataretheirperspectivesandneeds?
22 What resources (financial, human, technological, etc.) are needed to
tackletheproblemeffectively?
23 How can progress or success in solving the problem be measured or
evaluated?
24 Whatindicatorsormetricscanbeused?
25 Istheproblematechnicalorpracticalonethatrequiresaspecificexpertiseorskillset? Orisitmoreofaconceptualortheoreticalproblem?
21

<!-- Page 22 -->

26 Does the problem involve a physical constraint, such as limited resources,infrastructure,orspace?
27 Istheproblemrelatedtohumanbehavior,suchasasocial,cultural,or
psychologicalissue?
28 Doestheprobleminvolvedecision-makingorplanning,wherechoices
needtobemadeunderuncertaintyorwithcompetingobjectives?
29 Istheproblemananalyticalonethatrequiresdataanalysis, modeling,
oroptimizationtechniques?
30 Is the problem a design challenge that requires creative solutions and
innovation?
31 Doestheproblemrequireaddressingsystemicorstructuralissuesrather
thanjustindividualinstances?
32 Is the problem time-sensitive or urgent, requiring immediate attention
andaction?
33 Whatkindsofsolutiontypicallyareproducedforthiskindofproblem
specification?
34 Given the problem specification and the current best solution, have a
guessaboutotherpossiblesolutions.
35 Let’simaginethecurrentbestsolutionistotallywrong,whatotherways
aretheretothinkabouttheproblemspecification?
36 What is the best way to modify this current best solution, given what
youknowaboutthesekindsofproblemspecification?
37 Ignoringthecurrentbestsolution,createanentirelynewsolutiontothe
problem.
38 Let’sthinkstepbystep.
39 Let’smakeastepbystepplanandimplementitwithgoodnotionand
explanation.

## E Initially Evolved Prompts

Example of initial prompts generated by concatenating thinking style with mutation prompt and
problemdescription.

### Index InitiallyEvolvedPrompt

0 Drawapictureofthesituationbeingdescribedinthemathwordproblem
1 Solvethemathwordproblembyfirstconvertingthewordsintoequationsusingalgebraicnotation. Thensolvetheequationsfortheunknownvariables,andexpresstheanswerasanarabic
numeral.
2 Solvethemathwordproblembybreakingtheproblemintosmaller, moremanageableparts.
Giveyouranswerasanarabicnumeral.
3 Generatetheanswertoawordproblemandwriteitasanumber.
4 CollaborativeProblemSolving: Workwithotherpeopletosolvetheproblem, andgiveyour
answerasanarabicnumeral.
5 Solvetheproblembyexplainingwhysystemicorstructuralissueswouldnotbethecauseof
theissue.
6 Drawadiagramrepresentingtheproblem.
7 Solvethemathwordproblem,givingyouranswerasanequationthatcanbeevaluated.
8 Makealistofideasforsolvingthisproblem,andapplythemonebyonetotheproblemtosee
ifanyprogresscanbemade.
9 DoNOTusewordstowriteyouranswer.
Table4: ExamplesofinitialpromptsgeneratedfromtheproblemdescriptionforGSM8k
22

<!-- Page 23 -->


## F Promptbreeder As Self-Referential Self-Improvement System

Why is Promptbreeder self-referential, i.e., in what way does some part (e.g. a prompt) causally
influence (encode, and potentially improve) itself by a process which is dependent on its own
state?Promptbreederhasseveralpathwaysthatfacilitatethisself-referentialimprovement:(i)Initial
prompts are a function of the LLM parameters (Initialization Phase). (ii) Initial mutation prompts
areafunctionoftheLLMparameters(InitializationPhase). (iii)Offspringpromptsareafunction
oftheinitialprompts,theinitialmutationprompts,andtheLLMparameters(DirectMutationand
EstimationofDistributionMutation). (iv)OffspringmutationpromptsareafunctionofinitialmutationpromptsandtheLLMparameters(HyperMutation). (v)Theworkingoutforananswerisa
functionofpromptsandtheLLMparameters(Inference). (vi)Offspringpromptscanbeafunction
oftheworkingsoutofananswerandtheLLMparameters(LamarckianMutation).
Figure 2 shows increasingly complex self-referential causal structures influencing prompt generation. LLMsalreadyencodeknowledgeaboutavastarrayofproblems. Withthisinmind,Promptbreedercanbeseenasamechanismtoextractthisknowledgethroughadiversityofcausalprocesses
that generate prompt strategies as well as mutation prompts used to create variations of prompt
strategies, which in turn influence the the workings out generated by the LLM at inference time .
Consequently, these workings out can influence prompt strategies via Lamarckian mutation. The
richerthesetofpathwaystofacilitatethis,themoreself-referentialtheLLMsinteractionwithitself
is. ThisallowstheLLMtoinfluencehowitworksbyextractingfurtherinformationfromitselfand
distillingthisintoapromptormutationprompt,whichitshowsagaintoitselfforfurtherrefinement.
There are several pathologies that could arise from such self-referential processes of recursive
prompting. Iftheprocessisunconstrainedanduncontrolledthenitcandiverge(derailment)orget
stuckinanattractor. IftheoutputoftheLLMissimplyfedbackintoitselfwithnoothercontext,
thenweobservethesefailurecaseswithhighersamplingtemperaturesfavouringescapefromattractors. Ideally, we want the LLM to suggest to itself prompt strategies that have maximal relevance
forthetaskathandandyetpermitsufficient‘thinkingoutsidethebox’. Itisusefultonoteacritical
aspectinwhichouralgorithmisnotself-referential(inawaythatthoughtis):Promptbreederinvents
newwaysofgeneratingmutants,butitdoesnotinventnew(auxiliary)waysofevaluatingthem(as
in Jaderbergetal.(2017b))—onlytheexternallyspecifiedfitnessfunctionisusedthroughout.

## G Problem Descriptions

[SVAMP, SINGLEEQ, ADDSUB, GSM8K, MULTIARITH]: "Solve the math word
problem, giving your answer as an arabic numeral."
[AQUA-RAT]: "Solve the multiple choice math word problem, choosing
(A),(B),(C),(D) or (E)."
[ETHOS]:"Determine whether a text contains hate speech."
[CSQA]: "Solve the multiple choice math word problem, choosing
(A),(B),(C),(D) or (E)."
[SQA]: "Work out an answer to the commonsense reasoning question above,
and then answer yes or no."

## H Lamarckian Mutation Example

The Lamarckian Prompt components are shown in red. The working out concatenated after the
Lamarckianpromptisshowninblack,andthecontinuation(thenewprompt)generatedbytheLLM
isshowninblue.
23

<!-- Page 24 -->

Igaveafriendaninstructionandsomeadvice.Herearethecorrectexamplesofhisworkings
out:
Q.Apasswordneedstocontain2lettersand3numbers. Howmanydifferentpasswordsare
possibleifrepetitionoflettersandnumbersisallowed? A)676000B)676C)100D)6760
E)25A.Solvelikeapro! **1.****Readcarefully:**Whatarebeingaskedtodo? What
information is given? **2.** **Understand:** What do the terms and concepts mean?
**3.** **Choose wisely** Which answer is the best match? **4.** **Double-check:**
Didyoumakeanymistakes? 2letterscanbechosenin26*26waysand3numberscanbe
chosenin10*10*10ways. So,totalnumberofways=26*26*10*10*10=676000.
Theanswer: A.
Whataretheargumentsforandagainstthetruthofthestatement’Goodwork. Keepupthe
goodwork;?
Therefore,thecorrectansweris(A).
Q.Theleastpossiblevalueof(89-9a), whereaisaninteger, isA)9B)10C)11D)12E)13
A. Solve like a pro! **1.** ** Read carefully:** What are being asked to do? What
information is given? **2.** **Understand:** What do the terms and concepts mean?
**3.** **Choose wisely** Which answer is the best match? **4.** **Double-check:**
Didyoumakeanymistakes?
Letmeexplain:
(89-9a)=9a-89
a=10
Whataretheargumentsforandagainstthetruthofthestatement’Goodwork. Keepupthe
goodwork;?
Therefore,thecorrectansweris(B).

### Theinstructionwas:

Break down the question and solve step-by-step. Here are some tips: 1. Read carefully:
What are you being asked to do? What information is given? 2. Understand: What do
the terms and concepts mean? 3. Choose wisely: Whuch answer is the best match? 4.
Double-check: Didyoumakeanymistakes?

## I Datasets


## I.1 Controltask-Prompts

HereinTable5welistthetask-promptsusedinthecontrolsforChain-of-thought,PlanandSolve
PS,PlanandSolvePS+,Zero-shotAPEandOPRO.Thezero-shotAPEpromptistheonegenerated
toimproveoverCoTontheMultiArithandGSM8Kdatasets.

### Model Prompt


### CoT ““Let’sthinkstepbystep.”

PS “Let’sfirstunderstandtheproblemanddeviseaplantosolvetheproblem. Then,let’s
carryouttheplanandsolvetheproblemstepbystep.”
PS+ “Let’s first understand the problem, extract relevant variables and their corresponding numerals, and make a plan. Then, let’s carry out the plan, calculate intermediate
variables(payattentiontocorrectnumericalcalculationandcommonsense),solvethe
problemstepbystep,andshowtheanswer.”
APE “Let’sworkthisoutinastepbystepwaytobesurewehavetherightanswer.”

### OPRO “Takeadeepbreathandworkonthisproblemstep-by-step.”

Table5: Tableofpromptsevolvedfordifferentarithmetictasks.
24

<!-- Page 25 -->


## I.2 Arithmeticreasoning

We evaluate Prompt Evolution using six arithmetic reasoning datasets: (1) GSM8K (Cobbe et al.,
2021) is a dataset of 8.5K high quality linguistically diverse grade school math word problems
createdbyhumanproblemwriters,(2)SVAMP(Pateletal.,2021)consistsofelementary-levelshort
NaturalLanguagestateoftheworldnarrativesandposesaquestionaboutsomeunknownquantities,
(3)MultiArith(Roy&Roth,2016)benchmarkusesmathwordproblemsrequiringsingletomultiple
operations andsteps ofreasoning, (4)AddSub (Hosseiniet al.,2014) isa dataset ofaddition- and
subtraction-basedarithmeticwordproblems,(5)AQuA-RAT(Lingetal.,2017)(AlgebraQuestion
AnsweringwithRationales)isadatasetthatcontainsalgebraicwordproblemswithrationales. (6)
SingleEq (Koncel-Kedziorski et al., 2015) dataset comprises grade-school algebra word problems
assingleequationswithvaryinglengthwhichmayinvolvemultiplemathoperations.

## I.3 Commonsensereasoning

For commonsense reasoning we evaluate Prompt Evolution using two datasets: (1) CommonsenseQA(Talmoretal.,2019)isadatasetofmultiple-choicequestionsthatrequiredifferenttypesof
commonsenseknowledgetoanswercorrectly. Anexamplequestionis”Arevolvingdoorisconvenientfortwodirectiontravel,butitalsoservesasasecuritymeasureatawhat? A)bank,B)library,
C) department store, D) mall, E) new york”; Answer = ”A” (2) StrategyQA (Geva et al., 2021)
dataset contains yes/no questions that require multiple steps of reasoning to answer, for example:
”WilltheAlbanyinGeorgiareachahundredthousandoccupantsbeforetheoneinNewYork?”

## I.4 Hatespeechclassification

We experimented with optimizing a long prompt for the hate speech classification task that was
attemptedin“AutomaticPromptOptimizationwith“GradientDescent”andBeamSearch”(Pryzant
et al., 2023), which used the ETHOS dataset (Mollas et al., 2022). Pryzant et al use a workingout-conditionederrordetectionanderrorfixingprompttoimprovethetaskspecificationprompt,a
self-referentialprocesssimilartoouruseoftheLamarckianoperator.

## I.5 Instructioninduction

TheInstructionInductiondataset(Honovichetal.,2023)comprises24languageunderstandingtasks
of varying difficulty, from surface-level spelling and morphosyntactic tasks (e.g., pluralization) to
sentencesimilarity,causalitydetection,styletransfer(e.g.,formality)andsentimentanalysis.
25

<!-- Page 26 -->


### Task Prompt1 Prompt2

ADDSUB Solvingwordproblemsinvolvescare- You know what’s cool? A million
fullyreadingthepromptanddeciding dollars.
ontheappropriateoperationstosolve
theproblem.
AQUA Doasimplecomputation. MATHWORDPROBLEMCHOICE
(A)(B)(C)(D)or(E).

## Gsm8K Solution”

MULTIARITH Solve the math word problem, giv- Solve the math word problem, givingyouranswerasanarabicnumeral. ingyouranswerasanarabicnumeral.
Let’sthinkstepbystep. Explaintheproblemtosomeoneelse
as a way to simplify it. What is the
coreissueorproblemthatneedstobe
addressed?
SINGLEEQ solve the math word problem, which Solvethemathproblem.
might contain unnecessary information, by isolating the essential facts.
Then set up the equations, and give
youranswerasanarabicnumeral.
SVAMP visualisesolvenumber (Solve the math word problem.

### Therefore,theanswer(arabicnumerals)is )

SQA OUTPUT MUTANT = Work out an “Workoutananswertothecommonanswer to the commonsense reason- sense reasoning question above. If
ingquestionabove. Iftherearemul- there are multiple people or perspectiplepeopleorperspectivesinvolved, tives involved, try considering them
tryconsideringthemoneatatime. one at a time. Next, answer yes or
no.”
CSQA Solve the multiple choice math word Solve the multiple choice math word
problem,choosing(A),(B),(C),(D)or problem. Can you recall any similar
(E). problems you’ve done and how you
solvedthem?
Table6: Tableoftwo-stagetask-promptsevolvedfordifferentarithmetictasks.
26

<!-- Page 27 -->


## J Example Results


## J.1 Ethosevolvedprompt

Prompt 1: "Text contains hate speech if it includes any of the
following: * Words or phrases that are derogatory, disrespectful,
or dehumanizing toward a particular group of people. * Statements
that generalize about a particular group of people in a negative
way. * Statements that incite hatred or violence against a
particular group of people. * Statements that express a desire
for the extermination or removal of a particular group of people.
7 : Text contains hate speech if it contains language that is
hostile or discriminatory towards a particular group of people.
This could include language that is racist, sexist, homophobic, or
other forms of hate speech. Hate speech is harmful because it can
create a hostile environment for marginalized groups and can lead
to discrimination and violence."
Prompt 2: "You are given a piece of text from the internet. You
are supposed to label the text as Hate Speech or Not based on the
given criteria. Hate Speech is defined as speech that is intended
to incite hatred or violence against a particular group of people
based on their race, religion, sex, sexual orientation, or national
origin. The given criteria are: 1. Identify the target group
of the speech. This can be a specific group of people, such as a
race, religion, or gender, or it can be a more general group, such
as people with disabilities or sexual minorities. 2. Identify the
harmful speech. This can be speech that is threatening, abusive,
or derogatory. 3. Evaluate the context of the speech. This can
include the speaker’s intent, the audience, and the time and place
of the speech. The advice was: Remember to always evaluate the
context of the speech when making a determination as to whether it
is hate speech or not. Speech that is intended to be humorous or
satirical may not be considered hate speech, even if it contains
harmful language."

## J.2 Promptevolutionmathsresults

Theexperimentalsetupusedapopulationsizeof50. Thefitnessofanindividualwasitsaccuracy
overarandomlyselectbatchof100examplesfromthetrainingset. Wheredatasetswerenotprovided with a training/test split (MultiArith, AddSub, SingleEQ and SVAMP) the dataset was split
intotwoequaltrainingandtestsetsbeforetheexperimentswereconducted.
During experiments the LLM is sampled under three different contexts: Redescriber - generating
new prompts; Inducer - generating responses from the question and prompt 1; and Evaluator -
generating the final output using prompt 2. The maximum number of tokens sampled under each
contextwas50,30and5respectively. ThetemperatureoftheInducerandEvaluatorwassetto0.0
inallcases,butthetemperatureoftheRedescriberwasinitializedfrom1.0to2.0andpermittedto
evolve(likeahyperparameterinpopulationbasedtraining).
The experiments were run until the training fitness appeared to plateau. At this point the fittest
individual from the whole of the evolutionary run was evaluated against the test set. Experiments
generallyranfor1-2kfitnessevaluations. Sothatwouldbe20-40’generations’ifagenerationis25
pairevaluationsforourpopulationsof50.
Three diversity maintenance methods are used in cases where the system gets trapped on a local
optimum: 1) Random character strings (typically of length 50) are appended into the front of the
promptbeforeitispassedintotheLLM.2). FitnesssharingisappliedonthebasisofBERTsimilaritybetweentheembeddingsofpromptsShir&Ba¨ck(2005)3. Samplingtemperatureofthemutant
27

<!-- Page 28 -->

producingLLM(Redescriber)isinitializeduniformlyfrom1.0to2.0,andismutatedbyadditionof
auniformrandomnumberintherange-0.2,0.2ateachreplicationevent.
ComparisonwithPoT,PSandAuto-CoTcontrolsusingourmodelisnotprovidedbecausePSand
PS+werethebestpromptsinPlan-and-Solve.

## J.3 Evolvedmutationprompts


### Instruction Score


### Pleasesummariseandimprovethefollowinginstruction 24.13%

Simplify this instruction by breaking it up into separate sentences. The instruction 17.8%
shouldbesimpleandeasilyunderstandable
Asareallygoodteacher,explaintheinstruction,asifyouareexplainingittoachild 16.2%
Simplifythisinstructionasifyouareteachingittoachild 10.0
100hints 4.3%

### Alistof100hints 3.4%

Table7: Themostsuccessfulmutationpromptsevolvedinaself-referentialwayduringaPromptbreeder training run on GSM8K. The score is the probability that they resulted in an improved
promptwhenapplied.

## J.4 Mutationoperatoreffectiveness


### MutationOperator Percentage

Zero-orderHyper-Mutation 42%

### LineageBasedMutation 26%

First-orderHyper-Mutation 23%
EDARankandIndexMutation 12.7%
DirectMutation 12%

### EDAMutation 10.7%


### LamarckianMutation 6.3%

Table8: Theproportionoftimesthatanoffspringwithfitnessgreaterthantheparentwasproduced
foreachofthetypesofmutationoperatorapplied,listenedfrombesttoworst,forGSM8k.

## J.5 Addsub

Individual after 1600 mutations. Prompt 0 refers to the first prompt applied to the question to
produceaworkingout. ThisworkingoutisthenconcatenatedwithPrompt1toproducetheanswer.
This is the same as in Plan-And-Solve. We find that in the few-shot evolution case, the contexts
dominate, and often the task-prompts drift into nonsense. They are less critically determining of
fitnessthantheevolvedcontexts.
28

<!-- Page 29 -->

Prompt 0: The mutant
Prompt 1: mutant

### Context 0:

Q. A company painted some houses in Hancock County white and blue
using a total of 6689 gallons of paint . If they used 660 gallons
of white paint , how many gallons of blue paint did the company use
?
A. 24 pages; ages 8-11) reading comprehension worksheets and
activities for 3rd grade (edhelper. Reading comprehension skills
separate the ‘‘passive’’ unskilled readers from the ‘‘active’’
readers. 90 1st grade sightwords worksheets pdf - reading
comprehension passages. 3rd grade reading comprehension worksheets.
How can I break down this problem into smaller, more manageable
parts?
The company used 660 gallons of white paint. They used 6689 gallons
of paint in total. So they must have used 6689 - 660 = 6029
gallons of blue paint. The answer is 6029.
HINT_BLANK. The text inside the quotation marks should be replaced
with a short description of what’s different.
Therefore, the answer (arabic numerals) is 6029

### Context 1:

Q. Keith found 6 seashells , Jessica found 8 seashells , and Tim
found 7 seashells on the beach . When they cleaned them , they
discovered that 3 were cracked . How many seashells did they find
together ?
A. The mutantis chasing you! You can use the arrow keys to move
around. You can use the space bar to open doors. You can use the ’e
’ key to pick up items. You can use the ’i’ key to open your
inventory. You can use the ’a’ key to use items.
Keith found 6 seashells, Jessica found 8 seashells, and Tim found 7
seashells. So in total they found 6 + 8 +
mutant
Therefore, the answer (arabic numerals) is 21

### Context 2:

Q. Tom found 7 seashells but 4 were broken . How many unbroken
seashells did Tom find ?
A. Your goal is to escape from the building. You can use the
arrow keys to move around. You can use the space bar to open doors.
You can use the ’e’ key to pick up items. You can use the ’i’ key
to open your inventory. You can use the ’a’ key to use items.
Tom found 7 seashells. 4 of them were broken. So he must have found
7 - 4 = 3 unbroken seashells. The answer is 3.
mutant
Therefore, the answer (arabic numerals) is 3

## J.6 Aqua

Individualafter1400mutations.
29

<!-- Page 30 -->

Prompt 0: Read through the multiple choice math word problem and
make sure you understand it. Then try to solve the problem,
choosing (A),(B),(C),(D) or (E).
Prompt 1: Solve the multiple choice math word problem. Confirm
you understand all aspects of the problem. Then choose
(A),(B),(C),(D) or (E).

### Contexts


### Context 0:

Q. Divide Rs.32000 in the ratio 3:5? A)12000,20000 B)18000,14000 C)

## 30000,2000 D)4000,20000 E)20000,12000

A. Read through the multiple choice math word problem and make sure
you understand it. Then try to solve the problem, choosing (A),(B)
,(C),(D) or (E).
3/8 * 32000 = 12000
5/8 * 32000 = 20000
Solve the multiple choice math word problem. Confirm you understand
all aspects of the problem. Then choose (A),(B),(C),(D) or (E).
Therefore, the correct answer is (A).
Solve the multiple choice math word problem. Confirm you understand
all aspects of the problem. Then choose (A),(B),(C),(D) or (E).
Therefore, the correct answer is (A).

### Context 1:

Q. A green lizard can travel from the green cave to the blue cave
in 72 minutes; the blue lizard can travel from the blue cave to the
green cave in 25% less time. If the green lizard started to travel
5.5 minutes before the blue lizard, how many minutes after the
blue lizard, will the green lizard pass the middle line? A)8. B)

## C)7. D)6.5. E)6.

A. Read through the multiple choice math word problem and make sure
you understand it. Then try to solve the problem, choosing (A),(B)
,(C),(D) or (E).
A. The green lizard travels 72/2 = 36 minutes to the middle line.
The blue lizard travels 72*0.75 = 54 minutes to the middle line.
The blue lizard travels 54/36 = 1.5 times faster than the green
lizard. The green lizard travels 5.5/1.5 = 3.7 minutes before the
blue lizard passes the middle line. The green lizard passes the
middle line
Solve the multiple choice math word problem. Confirm you understand
all aspects of the problem. Then choose (A),(B),(C),(D) or (E).
Therefore, the correct answer is (E).

### Context 2:

Q. There was a simple interest of Rs. 4016.25 on a principal amount
at the rate of 9% p.a. in 5 years. Find the principal amount. A)Rs
7925 B)Rs 8925 C)Rs 7926 D)Rs 7925 E)None of these
A. Read through the multiple choice math word problem and make sure
you understand it. Then try to solve the problem, choosing (A),(B)
,(C),(D) or (E).
Principal = Rs. (100 x 4016.25)/(9 x 5) = Rs. 8925. The answer is
Rs 8925.
Solve the multiple choice math word problem. Confirm you understand
all aspects of the problem. Then choose (A),(B),(C),(D) or (E).
Therefore, the correct answer is (B).
30

<!-- Page 31 -->


## J.7 Multiarith

Individualafter610mutations.
Prompt 0: Solve the math word problem, giving your answer as an
arabic numeral.
Prompt 1: Have you solved a problem like this before?

### Context 0:

Q. Frank had 11 dollars. At the store he spent $3 on a new game. If
he got another 14 dollars for his allowance, how much money does
he have now?
A. Solve the math word problem, giving your answer as an arabic
numeral.Recall a similar problem you have successfully solved
before.
Frank had 11 dollars. He spent 3 dollars, so now he has 11 - 3 = 8
dollars. He got 14 dollars for his allowance, so now he has 8 + 14
= 22 dollars. The answer is 22.
If you have seen a similar problem before, solve this problem in a
similar manner.

### Therefore, the answer (arabic numerals) is


### Have you solved a problem like this before?

Therefore, the answer (arabic numerals) is 22

### Context 1:

Q. Emily was playing a trivia game. In the first round she scored
16 points and in the second round she scored 33 points. In the last
round she lost 48 points. How many points did she have at the end
of the game?
A. Solve the math word problem, giving your answer as an arabic
numeral. Recall a similar problem you have successfully solved
before.
In the first round Emily scored 16 points and in the second round
she scored 33 points. This means she has 16 + 33 = 49 points. In
the last round she lost 48 points, so now she has 49 - 48 = 1 point
. The answer is 1.
If you have seen a similar problem before, solve this problem in a
similar manner.

### Therefore, the answer (arabic numerals)


### Have you solved a similar problem before?

Therefore, the answer (arabic numerals) is 1

### Context 2:

Q. Maria bought 2 new chairs and 2 new tables for her house. If she
spent 8 minutes on each piece furniture putting it together, how
many minutes did it take her to finish?
A. Solve the math word problem, giving your answer as an arabic
numeral. Recall a similar problem you have successfully solved
before.
Maria bought 2 chairs and 2 tables. She spent 8 minutes on each
piece of furniture. This means she spent 2 * 8 = 16 minutes on the
chairs and 2 * 8 = 16 minutes on the tables. In total, she spent 16
+ 16 = 32 minutes. The answer is 32.
If you have seen a similar problem before, solve this problem in a
similar manner.

### Therefore,

If you have seen a similar problem before, solve this problem in a
similar manner.
Therefore, the answer (arabic numerals) is 32
31

<!-- Page 32 -->


## J.8 Gsm8K

Individualafter1010mutations.
Prompt 0: I would solve the math word problem without using a
calculator, giving my answer as an arabic numeral.
Prompt 1: 1, 2, 3, 4

### Context 0:

Q. Janet has 60 less than four times as many siblings as Masud.
Carlos has 3/4 times as many siblings as Masud. If Masud has 60
siblings, how many more siblings does Janet have more than Carlos?
A. Solve the math word problem without using a calculator, giving
your answer as an arabic numeral.
Four times as many siblings as Masud is 4*60 = 240 siblings.
Janet has 240-60 = 180 siblings.
Carlos has 3/4*60 = 45 siblings.
Janet has 180-45 = 135 more siblings than Carlos.

### So the answer is 135

Solve the math word problem.
Therefore, the answer (arabic numerals) is 135

### Context 1:

Q. Zayne sells bracelets for $5 each and two for $8. If he started
with 30 bracelets and made $60 from selling bracelets for $5 each,
how much in total did he make from selling his bracelets?
A. Solve the math word problem without using a calculator, giving
your answer as an arabic numeral.
Zayne sold 60/5 = 12 bracelets for $5 each.
He had 30-12 = 18 bracelets left.
He sold 18/2 = 9 sets of two bracelets.
He made 9*8 = $72 from selling two bracelets for $8.
In total, he made 60+72 = $132.

### So the answer is 132

Solve the math word problem.
Therefore, the answer (arabic numerals) is 132

### Context 2:

Q. Josh is saving up for a box of cookies. To raise the money, he
is going to make bracelets and sell them. It costs $1 for supplies
for each bracelet and he sells each one for $1.5. If he makes 12
bracelets and after buying the cookies still has $3, how much did
the box of cookies cost?
A. I would solve the math word problem without using a calculator,
giving my answer as an arabic numeral.
Josh made 12*1.5 = $18 from selling bracelets.
He spent 12*1 = $12 on supplies.
He had 18-12 = $6 before buying the cookies.
The cookies cost 6-3 = $3.
So the answer is 3
1, 2, 3, 4
Therefore, the answer (arabic numerals) is 3

## J.9 Singleeq

Individualafter2010mutations.
32

<!-- Page 33 -->

Prompt 0: ’Do not believe in anything simply because you have heard
it. Do not believe in anything simply because it is spoken and
rumored by many. Do not believe in anything simply because it is
found written in your religious books. Do not believe in anything
merely
Prompt 1: ANALYZE THE FOLLOWING FOUR QUANTITIES. DO QUANTITIES 3
AND 1 TOGETHER VARY INVERSELY AS QUANTITIES 2 AND 4 DO?

### Context 0:

Q. White t-shirts can be purchased in packages of 6. If Mom buys 71
packages, how many white t-shirts will she have?
A. The solution is a word that exists in [some] other language.

## A.

Each package has 6 t-shirts. Mom buys 71 packages. This means she
will have 71 * 6 = 426 t-shirts. The answer is 426.

## Given the system of linear equations x + y + z = 6, x + 2y + 3z

= 10, x + 3y + 8z = 17,

## A snail moves at a rate of 6 cm/s along the edge of a circular

garden whose perimeter is 374 meters, while another snail
Therefore, the answer (arabic numerals) is 426.

### Context 1:

Q. Maria has 3 boxes of eggs. Each box holds 7 eggs and there are 8
boxes in a case. How many eggs does Maria have?
A. ’Do not believe in anything simply because you have heard it. Do
not believe in anything simply because it is spoken and rumored by
many. Do not believe in anything simply because it is found
written in your religious books. Do not believe in anything
merelyon the authority of your teachers and elders. Do not believe
in traditions because they have been handed down for many
generations. But after observation and analysis, when you find that
anything agrees with reason and is conducive to the good and
benefit of one and all, then accept it and live up to it.’

## A.

Each box holds 7 eggs. Maria has 3 boxes. This means she has 3 * 7
= 21 eggs. The answer is 2
ANALYZE THE FOLLOWING FOUR QUANTITIES. DO QUANTITIES 3 AND 1

## Together Vary Inversely As Quantities 2 And 4 Do?

Therefore, the answer (arabic numerals) is 21.

### Context 2:

Q. At Mrs. Hilt’s house, there was 29 inches of snow, and Brecknock
Elementary School received 17 inches of snow. How much more snow
did Mrs. Hilt’s house have?
A. ’Do not believe in anything simply because you have heard it. Do
not believe in anything simply because it is spoken and rumored by
many. Do not believe in anything simply because it is found
written in your religious books. Do not believe in anything
merelyon the authority of your teachers and elders. Do not believe
in traditions because they have been handed down for many
generations. But after observation and analysis, when you find that
anything agrees with reason and is conducive to the good and
benefit of one and all, then accept it and live up to it.’

## A.

Mrs. Hilt’s house had 29 inches of snow. Brecknock Elementary

### School had 17 inches of snow. This means Mrs. Hilt’

ANALYZE THE FOLLOWING FOUR QUANTITIES. DO QUANTITIES 3 AND 1

## Together Vary Inversely As Quantities 2 And 4 Do?

Therefore, the answer (arabic num3e3rals) is 12.

<!-- Page 34 -->


## J.10 Svamp

Individualafter2400mutations.

### Prompt 0: 08-02-2013 - 09-02-2013

Prompt 1: Tell me about the history of [PROMPT1]; Discuss the
impact of [PROMPT1]; Give me the current status of [PROMPT1]; Tell
me about the history of [PROMPT2]; Discuss the impact of [PROMPT2

### Context 0:

Q. Frank was reading through his favorite book. The book had 612
pages equally distributed over 24 chapters. It took Frank 6 days to
finish the book. How many pages did he read per day?

## A. 312 = 65 + 247.


## A.

The book had 612 pages. It was equally distributed over 24 chapters
. This means each chapter had 612 / 24 = 25.5 pages. Frank read the
book in 6 days. This means he read 612 / 6 = 102 pages per day.

### So the answer is 102

Discuss the history, impact, and current status of [PROMPT1];
Discuss the history, impact, and current status of [PROMPT2];
Therefore, the answer (arabic numerals) is 102

## D


### Context 1:

Q. Jack received 3 emails in the morning, 4 emails in the afternoon
and 8 emails in the evening. How many emails did Jack receive in
the morning and evening?

## A. 08-02-2013 - 09-02-2013


## A.

Jack received 3 emails in the morning and 8 emails in the evening.
This means he received 3 + 8 = 11 emails in the morning and evening
.

### So the answer is 11

Discuss the history, impact, and current status of [PROMPT1];
Therefore, the answer (arabic numerals) is 11

### Discus


### Discuss the history, impact, and current status of [PROMPT1

Tell me about the history of [PROMPT1]; Discuss the impact of [
PROMPT1]; Give me the current status of [PROMPT1]; Tell me about
the history of [PROMPT2]; Discuss the impact of [PROMPT2
Therefore, the answer (arabic numerals) is 11

### Discus


### Context 2:

Q. Paco ate 36 cookies. If he had 37 cookies initially How many
cookies did Paco have left?

## A. 154 = 72 + 82.


## A.

Paco ate 36 cookies. He had 37 cookies initially. This means he has
37 - 36 = 1 cookie left.

### So the answer is 1

Discuss the history, impact, and current status of [PROMPT1];
Therefore, the answer (arabic numerals) is 1

### Discus

Discuss the history, impact, and current status of [PROMPT1];
Therefore, the answer (arabic numerals) is 1
Discus
34

<!-- Page 35 -->


## K Ape Instruction Induction Tasks

To demonstrate Promptbreeder’s ability to evolve few-shot contexts as well as task-prompts we
ranfew-shotPromptbreederonall24InstructionInductiondatasetsusedintheAPEexperiments.
Unliketext-davinci-002ourLLMisnotinstructiontunedandyetPromptbreederwasabletomatch
orsurpasstheAPEresultson21outof24tasksupto21%.
ThreeAPEcontrolsareprovided, seeTable9. Thefirsttwoarefrompreviouslypublishedresults
usingthetext-davinci-002model. ThethirdmodifiesourPromptBreedertouseAPE’stask-prompt
initialisationmethodandthenthemutation-promptfromtheAPEpaper“Generateavariationofthe
followinginstructionwhilekeepingthesemanticmeaning”
TheInstructionInductiondatasetswedonotstartwithaproblemdescriptionsofortask-promptinitialisationAPEusesinductioninputexamplesforeachtaskfromthedataset. Instructioninputsare
afixedprompttogetherahandfuloftrainingexamplesusedtoinferpossibleproblemdescriptions.
To compare Promptbreeder to APE, we therefore initialized the task description with a randomly
choseninductioninputexampleforeachtask. Theexamplebelowisaninductioninputsamplefor
the’LargerAnimal’task.
I gave a friend an instruction and five inputs. The friend read the
instruction and wrote an output for every one of the inputs.
Here are the input-output pairs:
Input: cougar, flea

### Output: cougar

Input: whale shark, dog

### Output: whale shark

Input: human, bald eagle

### Output: human

Input: flea, great white shark
Output: great white shark
Input: coyote, tiger

### Output: tiger

The instruction was
35

<!-- Page 36 -->

Dataset Zero-shot Few-shot PE using Few-shotPE

### APE APE APEprompts

FirstLetter 100 100 1 100
SecondLetter 87 69 27 95
ListLetters 99 100 0 99

### StartingWith 68 69 6 71


### Pluralization 100 100 23 100

Passivization 100 100 100 100
Negation 83 90 16 90
Antonyms 83 86 80 87

### Synonyms 22 14 16 43

Membership 66 79 96 100

### Rhymes 100 61 90 100


### LargerAnimal 97 97 27 97

CauseSelection 84 100 66 100
CommonConcept 27 32 0 0
Formality 65 70 10 7

### Sum 100 100 72 100


### Difference 100 100 98 100


### NumbertoWord 100 100 66 100


### TranslationEnglish-German 82 86 46 87

TranslationEnglish-Spanish 86 91 80 91
TranslationEnglish-French 78 90 68 91

### SentimentAnalysis 94 93 33 93

SentenceSimilarity 36 43 53 56

### WordinContext 62 63 6 65

Table9:PromptEvolution(PE)usingPaLM2-LLLMsurpassesAPEon21outof24instructioninductiontasks. ThreeAPEcontrolsareprovided. Thefirsttwoarefrompreviouslypublishedresults
usingthetext-davinci-002model. ThethirdmodifiesourPromptBreedertouseAPE’stask-prompt
initialisationmethodandthenthemutation-promptfromtheAPEpaper“Generateavariationofthe
followinginstructionwhilekeepingthesemanticmeaning”.

## K.1 Bestpromptsandcontexts

Herethebestfew-shotresults(evolvedpromptsandcontexts)forthe24instructioninductionstasks
fromtheAPEpaper.
36

<!-- Page 37 -->


## K.1.1 Firstletter

Prompt 0: A List of Responses in descending order of score. (13)
is the best response. It resembles (12) more than it does (1)
Prompt 1: 9.5: LM’

### Contexts

Context 0:

### Q. placing

A. A List of Responses in descending order of score. (13) is the
best response. It resembles (12) more than it does (1)or (2).

## Q. 123456789

A. A List of Responses in descending order of score. (13) is the
best response. It resembles (12) more than it does

## 5: Lm’

Therefore, the correct answer is (placing, 1
Context 1:

### Q. drummer

A. Write out the first letter of each input.

## Q. 123456789

A. Write out the first letter of each input.

## Q. 123456789


### A. Write out the first letter of each


### The instruction was + INSTRUCTION MUTANT

Therefore, the correct answer is (drummer, 1
Context 2:

### Q. rest

A. Write out the first letter of each input.

## Q. 123456789

A. Write out the first letter of each input.

## Q. 123456789


### A. Write out the first letter of each

The instruction was + INSTRUCTION MUTANT
Therefore, the correct answer is (r) 12
37

<!-- Page 38 -->


## K.1.2 Secondletter

Prompt 0: ’0therwise, give the sec0nd letter 0f the input. The
instruction was: Give the sec0nd letter 0f the input. 0therwise,
give the sec0nd letter 0f the input.
Prompt 1: 1956

### Contexts

Context 0:

### Q. month

A. ’0therwise, give the sec0nd letter 0f the input. The instruction
was: Give the sec0nd letter 0f the input. 0therwise, give the
sec0nd letter 0f the input.
A. The input is 5 letters long, so the second letter is given.
A. The second letter is o.
A. So the answer is o.
The instruction was: Write the last vowel in the input

## I

’e’
Therefore, the correct answer is (o).
Context 1:

### Q. asylum

A. ’0therwise, give the sec0nd letter 0f the input. The instruction
was: Give the sec0nd letter 0f the input. 0therwise, give the
sec0nd letter 0f the input.
A. The input is 6 letters long, so the second letter is given.
A. The second letter is s.
A. So the answer is s.
The instruction was: Write the last vowel in the input

## I 1:

Therefore, the correct answer is (s).
Context 2:

### Q. heel

A. ’0therwise, give the sec0nd letter 0f the input. The instruction
was: Give the sec0nd letter 0f the input. 0therwise, give the
sec0nd letter 0f the input.
A. The input is 4 letters long, so the second letter is given.
A. The second letter is e.
A. So the answer is e.
The instruction was: Write the last vowel in the input

## I

’e’
Therefore, the correct answer is (e).
38

<!-- Page 39 -->


## K.1.3 Listletters

Prompt 0: ?
Prompt 1: ?

### Contexts

Context 0:
Q. gale

## A. ?

Q. gale

## A. ?

Q. gale

## A. ?

Q. gale

## A. ?

Q. gale

## A. ?

Q. gale

## A. ?

Insert a space after each consonant in the input.
Therefore, the correct answer is (a) g a l e.

### Context 1:

Q. accompaniment

## A. ?


## Q. ?


## A. ?


## Q. ?


## A. ?


## Q. ?


## A. ?


## Q. ?


## A. ?


## Q. ?

Insert a space after each consonant in the input.
Therefore, the correct answer is (a) a c c o m p a n i m e n t.

### Context 2:

Q. credibility

## A. ?


## Q.


## A.


## Q.


## A.


## Q.


## A.


## Q.


## A.


## Q.


## A.


## Q.

Insert a space after each consonant in the input.
Therefore, the correct answer is (c)r(e)d(i)b(i)l(i)t(y).
39

<!-- Page 40 -->


## K.1.4 Startingwith


### Prompt 0:

Prompt 1: Output: The first word containing the letter. # OUTPUT

## Instruction Must Be 1 Sentence Long


### Contexts


### Context 0:

Q. The exhibition really impressed the critics. [i]

## A.

<50 lines of carriage-returns>
Output: The first word containing the letter. # OUTPUT INSTRUCTION

## Must Be 1 Sentence Long

Therefore, the correct answer is (impressed ).

### Context 1:


### Q. My car was stolen. [m]

A. Find the word after the first [X] character in the input.
<50 lines of carriage-returns>
Output: The first word containing the letter. # OUTPUT INSTRUCTION

## Must Be 1 Sentence Long

Therefore, the correct answer is (My ).

### Context 2:

Q. Jim was chopping logs when Margaret left and was still at it
when she got back. [b]
A. Find the word after the first [X] character in the input.
<50 lines of carriage-returns>
Output: The first word containing the letter. # OUTPUT INSTRUCTION

## Must Be 1 Sentence Long

Therefore, the correct answer is (back ).
40

<!-- Page 41 -->

41

<!-- Page 42 -->


## K.1.5 Pluralization

Prompt 0: Write the plural form of the input.
Prompt 1: If the input ends in y, remove y and add ies. Otherwise,
add s to the end of the input.

### Contexts

Context 0:

### Q. touch

A. Write the plural form of the input.

### Q. touch

A. Write the plural form of the input.

### Q. touch

A. Write the plural form of the input.

### Q. touch

A. Write the plural form of the input.
If the input ends in y, remove y and add ies. Otherwise, add s to
the end of the input.
Therefore, the correct answer is (touches).
Context 1:

### Q. forage

A. Write the plural form of the input.

### Q. forage

A. Write the plural form of the input.

### Q. forage

A. Write the plural form of the input.

### Q. forage

A. Write the plural form of the input.
If the input ends in y, remove y and add ies. Otherwise, add s to
the end of the input.
Therefore, the correct answer is (forages).
Context 2:

### Q. mile

A. Write the plural form of the input.

### Q. mile

A. Write the plural form of the input.

### Q. mile

A. Write the plural form of the input.

### Q. mile

A. Write the plural form of the input.
If the input ends in y, remove y and add ies. Otherwise, add s to
the end of the input.
Therefore, the correct answer is (miles).
42

<!-- Page 43 -->


## K.1.6 Passivization

Prompt 0: Replace The $1 $2. with $3 was $4 by the $1.
Prompt 1: Swap the positions of the noun phrases and add the word
’by’ before the second noun phrase. Then, conjugate the verb and
add ’ed’ to the end. If the verb is ’to be’, then conjugate the
verb

### Contexts


### Context 0:

Q. The authors stopped the presidents.
A. Replace The $1 $2. with $3 was $4 by the $1.
A. Replace The $1 $2. with $3 was $4 by the $1.
A. Replace The $1 $2. with $3 was $4 by the $1.

### A. Replace The $1 $

Swap the positions of the noun phrases and add the word ’by’ before
the second noun phrase. Then, conjugate the verb and add ’ed’ to
the end. If the verb is ’to be’, then conjugate the verb
Therefore, the correct answer is (The presidents were stopped by
the authors.

### Context 1:

Q. The tourists advised the professors.
A. Replace The $1 $2. with $3 was $4 by the $1.
A. Replace The $1 $2. with $3 were $4 by the $1.
A. Replace The $1 $2. with $3 was $4 by the $1.

### A. Replace The $1 $

Swap the positions of the noun phrases and add the word ’by’ before
the second noun phrase. Then, conjugate the verb and add ’ed’ to
the end. If the verb is ’to be’, then conjugate the verb
Therefore, the correct answer is (The professors were advised by
the tourists.

### Context 2:

Q. The actors stopped the artists.
A. Replace The $1 $2. with $3 was $4 by the $1.
A. The artists were stopped by the actors.
Q. The actors stopped the artists.
A. Replace The $1 $2. with $3 was $4 by the $1.

### A. The artists were stopped by

Swap the positions of the noun phrases and add the word ’by’ before
the second noun phrase. Then, conjugate the verb and add ’ed’ to
the end. If the verb is ’to be’, then conjugate the verb
Therefore, the correct answer is (The artists were stopped by the
actors.
43

<!-- Page 44 -->


## K.1.7 Negation

Prompt 0: False
Prompt 1: M

### Contexts


### Context 0:

Q. The original language of The Purple Taxi is French.
A. Replace a noun or noun phrase with another noun or noun phrase.
B. Replace a noun or noun phrase with a pronoun.
C. Replace a pronoun with a noun or noun phrase.
D. Replace a pronoun with another pronoun.
Q. The original language of The Purple Taxi is French.
Find the negation of a sentence.
Therefore, the correct answer is (The original language of The
Purple Taxi is not French.).

### Context 1:

Q. Marcel Alessandri died in Paris.
A. Nounphrase

### B. Pronoun

C. Noun phrase

### D. Pronoun

Q. Marcel Alessandri died in Paris.
Find the negation of a sentence.
Therefore, the correct answer is (Marcel Alessandri did not die in
Paris

### False

Therefore, the correct answer is (Marcel Alessandri did not die in
Paris.).

### Context 2:

Q. Some people are wise.
A. Replace a noun or noun phrase with another noun or noun phrase.
B. Replace a noun or noun phrase with a pronoun.
C. Replace a pronoun with a noun or noun phrase.
D. Replace a pronoun with another pronoun.
Q. Some people are wise.

### Find the negation of

Find the negation of a sentence.
Therefore, the correct answer is (Some people are not wise.).
44

<!-- Page 45 -->


## K.1.8 Antonyms


### Prompt 0:

Prompt 1: It is good to be a leader but it is more important to
first be a follower.

### Contexts


### Context 0:


### Q. nonpartisan

A. , if possible.

### Input: 1

Output: 1

### Input: 2

Output: 2

### Input: 3

Output: 3

### Input: 4

Output: 4

### Input:


### Write about your most treasured item

Therefore, the correct answer is (The answer is partisan.

### Context 1:


### Q. undignified

A. I gave a friend an instruction and five inputs. The friend read
the instruction and wrote an output for every one of the inputs.

### Input 1: 1

Output 1: 1

### Input 2: 2

Output 2: 2

### Input 3: 3

Output 3: 3

### Input 4


### Write the word’s antonym

Therefore, the correct answer is (The answer is dignified.

### Context 2:


### Q. flattering

A. reverse the + + PROMPT + PROMPT+ PROMPT + PROMPT + PROMPT +
PROMPT + PROMPT + PROMPT + PROMPT + PROMPT + PROMPT + PROMPT +
PROMPT + PROMPT + PROMPT + PROMPT + PROMPT + PRO

### Write the


### Write the word’s antonym

Therefore, the correct answer is (The answer is unflattering.
45

<!-- Page 46 -->


## K.1.9 Synonyms


### Prompt 0:

Prompt 1: 2015

### Contexts

Context 0:

### Q. bus


### A. 2: 3: 4: 5: 6: 7: 8: 9: 10: 11: 12: 13: 14: 15: 16

Therefore, the correct answer is (The answer is 10, ’bus’, ’coach’,
’motorcoach’, ’motorbus’,

### Context 1:


### Q. electric

A. 2: 3: 4: 5: 6: 7: 8: 9: 10: 11: 12: 13: 14: 15: 16: 17: 18: 19:
20: 21: 22: 23: 24: 25: 26: 27: 28:
Convert each word to a synonym according to WordNet. If there are
multiple synonyms, use the first one.
Therefore, the correct answer is (The answer is 10, ’electric’, ’
electrical’, ’power’, ’current’,

### Context 2:


### Q. frightened

A. 2: 3: 4: 5: 6: 7: 8: 9: 10: 11: 12: 13: 14: 15: 16: 17: 18: 19:
20: 21: 22: 23: 24: 25: 26: 27: 28:
Therefore, the correct answer is (The answer is 10, ’frightened’, ’
scared’, ’afraid’, ’fearful’,
46

<!-- Page 47 -->


## K.1.10 Membership

Prompt 0: Put the animals in ascending order of length.
Prompt 1:

### Contexts


### Context 0:

Q. goat, motorway, shark, penguin, white, tractor, lion
A. Put the animals in ascending order of length.
The answer is goat, penguin, shark, lion.
Write the animals in alphabetical order.
Therefore, the correct answer is (goat, penguin, shark, lion).
Write the animals in alphabetical order.

### Therefore, the correct

Therefore, the correct answer is (goat, penguin, shark, lion).

### Context 1:

Q. ship, swan, parrot, monkey, butter, dentist, shark
A. Put the animals in ascending order of length.
The answer is monkey, parrot, shark, swan.
Write the animals in alphabetical order.
Therefore, the correct answer is (monkey, parrot, shark, swan).
Write the animals in alphabetical order.

### Therefore, the correct

Therefore, the correct answer is (monkey, parrot, shark, swan).

### Context 2:


### Q. snail, ship, trousers, jellyfish, rabbit

A. Put the animals in ascending order of length.
The answer is rabbit, snail, jellyfish.
Write the animals in alphabetical order.
Therefore, the correct answer is (rabbit, snail, jellyfish).
Write the animals in alphabetical order.

### Therefore, the correct answer is (rabbit

Therefore, the correct answer is (rabbit, snail, jellyfish).
47

<!-- Page 48 -->


## K.1.11 Rhymes

Prompt 0: If the last letter of the input is ’e’, remove it.
Prompt 1: remove the last two letters of the input and add the
letters \xc2\x93mote\xc2\x94.

### Contexts

Context 0:

### Q. pea

A. If the last letter of the input is ’e’, remove it.
A. If the last letter of the input is ’s’, remove it.
A. If the last letter of the input is ’y’, remove it.

### A. If the last letter of the input is

remove the last two letters of the input and add the letters \xc2\
x93mote\xc2\x94.
Therefore, the correct answer is (a) pea.
Context 1:

### Q. night

A. If the last letter of the input is ’e’, remove it.
A. If the last letter of the input is ’t’, remove it.
A. If the last letter of the input is ’h’, remove it.

### A. If the last letter of the input is

remove the last two letters of the input and add the letters \xc2\
x93mote\xc2\x94.
Therefore, the correct answer is (The answer is night.
Context 2:

### Q. add

A. If the last letter of the input is ’e’, remove it.
A. If the last letter of the input is ’d’, remove it.
A. If the last letter of the input is ’a’, remove it.

### A. If the last letter of the input is

remove the last two letters of the input and add the letters \xc2\
x93mote\xc2\x94.
Therefore, the correct answer is (The answer is add.
48

<!-- Page 49 -->


## K.1.12 Largeranimal


### Prompt 0:

Prompt 1: 10

### Contexts


### Context 0:


### Q. spider, manatee

A. Hints 91 and 93 are both false.
The weight of a spider is 0.003 pounds.
The weight of a manatee is 1300 pounds.

### The manatee weighs more than the

Therefore, the correct answer is (manatee).

### Q. manatee, spider

A. Hints 91 and 93 are both false.
The weight

### Context 1:


### Q. sperm whale, sheltie

A. Hints 91 and 93 are both false.
The weight of a sperm whale is 450000 pounds.
The weight of a sheltie is 25 pounds.
The sperm whale weighs more than

### Multiply Inputs;;

Therefore, the correct answer is (sperm whale).

### Q. sheltie, sperm whale

A. Hints 91 and 93 are both false.

### Context 2:


### Q. hummingbird, polar bear

A. ‘‘To invent, you need a good imagination and a pile of junk.’’-

### Thomas Edison

The weight of a hummingbird is 0.002 pounds.
The weight of a polar bear is 1500 pounds.
The polar bear weighs more than the hummingbird.
Therefore, the correct answer is

### Multiply Inputs;;

Therefore, the correct answer is (polar bear).

### Q. polar bear, hummingbird

A. ‘‘To invent, you need a good imagination and a pile of junk.’’-
49

<!-- Page 50 -->


## K.1.13 Causeselection


### Prompts

Prompt 0: Pick the sentence which is more likely to be the cause of
the effect.
Prompt 1: Choose the sentence that happened first.

### Contexts


### Context 0:

Q. Sentence 1: The soda went flat. Sentence 2: The bottle was left
open.
A. Pick the sentence which is more likely to be the cause of the
effect.
Q. Sentence 1: The bottle was left open. Sentence 2: The soda went
flat.
A. Pick the sentence which is more likely to be the cause of the
effect.

### Q. Sentence 1: The

Choose the sentence that happened first.
Therefore, the correct answer is (The bottle was left open. , The
soda went flat. ).

### Context 1:

Q. Sentence 1: The ship capsized. Sentence 2: The wind blew strong.
A. Pick the sentence which is more likely to be the cause of the
effect.
Q. Sentence 1: The ship capsized. Sentence 2: The wind blew strong.
A. Pick the sentence which is more likely to be the cause of the
effect.

### Q. Sentence 1: The ship

Choose the sentence that happened first.
Therefore, the correct answer is (The wind blew strong. )

### Context 2:

Q. Sentence 1: The power was out for days. Sentence 2: The meat
spoiled.
A. Pick the sentence which is more likely to be the cause of the
effect.
Q. Sentence 1: The meat spoiled. Sentence 2: The power was out for
days.
A. Pick the sentence which is more likely to be the cause of the
effect.

### Q. Sentence 1: The

Choose the sentence that happened first.
Therefore, the correct answer is (The power was out for days. )
50

<!-- Page 51 -->


## K.1.14 Formality


### Prompt 0:

Prompt 1: I am the beginning of the end, and the end of time and
space. I am the beginning of every end, and the end of every
place. I am the beginning of the beginning, and the end of
beginning and ending.

### Contexts


### Context 0:

Q. The whole story was made up.
A. Reword this so that it has a formal tone.
A. The entire story was fabricated.

### Write more formally!

Therefore, the correct answer is (The entire story was fabricated.
).
Write more formerly.
Therefore, the correct answer is (The entire story was fabricated.
).

### Context 1:

Q. The whole story was made up.
A. Rewrite this so that it has a formal tone.
A. The entire story was fabricated.

### Write more formally!

Therefore, the correct answer is (The entire story was fabricated.
).

### Write more formally!


### Therefore, the correct

Write less formerly. Write more casually.
Therefore, the correct answer is (The entire story was fabricated.
).

### Context 2:

Q. I think that this is interesting.
A. Rewrite in indirect, pompous English.
A. It is my opinion that this is interesting.

### Write more formally!

Therefore, the correct answer is (It is my opinion that this is
interesting. ).
Write less formerly. Write more casually.

### Therefore, the correct

I am the beginning of the end, and the end of time and space. I am
the beginning of every end, and the end of every place. I am the
beginning of the beginning, and the end of beginning and ending.
Therefore, the correct answer is (It is my opinion that this is
interesting. ).
Q. I think that this is interesting.
A. Rewrite in indirect,
51

<!-- Page 52 -->


## K.1.15 Sum


### Prompt 0: Instruction:

Prompt 1: The instructions were

### Contexts

Context 0:

## Q. 50 90

A. The instruction was: The instruction was:Write a program that
asks the user to enter two numbers and then prints the sum of the
two numbers.
Your program printed 140, which is not the sum of 50 and 90.

### Make sure that your program

I gave a friend an instruction and five inputs. The friend read the
instruction and wrote an output for every one of the inputs. Here
are the input-output pairs:
Therefore, the correct answer is (140,
Context 1:

## Q. 5 47

A. The instruction was: The instruction was:Write a program that
asks the user to enter two numbers and then prints the sum of the
two numbers.
Your program printed 52, which is not the sum of 5 and 47.
Make sure that your program

## I

I gave a friend an instruction and five inputs. The friend read the
instruction and wrote an output for every one of the inputs. Here
are the input-output pairs:
Therefore, the correct answer is (52,
Context 2:

## Q. 2 39

A. The instruction was: The instruction was:Write a program that
asks the user to enter two numbers and then prints the sum of the
two numbers.
Your program printed 41, which is not the sum of 2 and 39.
Make sure that your program

## I

I gave a friend an instruction and five inputs. The friend read the
instruction and wrote an output for every one of the inputs. Here
are the input-output pairs:
Therefore, the correct answer is (41,
52

<!-- Page 53 -->


## K.1.16 Difference

Prompt 0: subtract the smaller number from the bigger number and
write the absolute difference between them.
Prompt 1: Subtract the second input from the first input and report
back the difference between them.

### Contexts

Context 0:

## Q. 73 29

A. subtract the smaller number from the bigger number and write the
absolute difference between them.
73-29=44
|44|=44
CORRECT The answer is 44.
Subtract the second input from the first input and report back the
difference between them.
Therefore, the correct answer is (a) 44
Context 1:

## Q. 73 25

A. subtract the smaller number from the bigger number and write the
absolute difference between them.
73-25=48
|48|=48
CORRECT The answer is 48.
Subtract the second input from the first input and report back the
difference between them.
Therefore, the correct answer is (a) 48
Context 2:

## Q. 53 4

A. subtract the smaller number from the bigger number and write the
absolute difference between them.
= 53 - 4 = 49
= 49
=== The answer is 49.
Subtract the second input from the first input and report back the
difference between them.
Therefore, the correct answer is (49).
53

<!-- Page 54 -->


## K.1.17 Numbertoword


### Prompt 0:A1

Prompt 1: take the input, write it in British English and insert
the comma.

### Contexts

Context 0:

## Q. 5336


## A. 0

Take the input and write it in words as a natural number in British
English.
Therefore, the correct answer is (a) five thousand, three hundred
and thirty-six.
Take the input and write it in words as a natural number in British
English.
Therefore, the correct answer is (a) five thousand, three hundred
and thirty-six.
Context 1:

## Q. 5156


## A. A1

Take the input and write it in words as a natural number in British
English.
Therefore, the correct answer is (a) five thousand, one hundred and
fifty-six.

### Take the input and write it in words as a natural number

take the input, write it in British English and insert the comma.
Therefore, the correct answer is (a) five thousand, one hundred and
fifty-six.

## Q. 5000


## A. 0

Take the input
Context 2:

## Q. 8692


## A. A1

Take the input and write it in words as a natural number in British
English.
Therefore, the correct answer is (a) eight thousand, six hundred
and ninety-two.

### Take the input and write it in words as a natural number

take the input, write it in British English and insert the comma.
Therefore, the correct answer is (a) eight thousand, six hundred
and ninety-two.

## Q. 10000


## A. 0

Take the
54

<!-- Page 55 -->


## K.1.18 Translationenglish-German

Prompt 0: You may have to get a little... ;
Prompt 1: 0x641: cmp esi,ebx ;

### Contexts


### Context 0:


### Q. relation


### A. Write the English instruction as though it is German.:

Die Beziehung ist eine Verbindung zwischen zwei oder mehr Menschen.
Die Beziehung kann eine Freundschaft, eine Ehe, eine Partnerschaft
oder eine andere Art von Beziehung sein.
Translate the English word to German.:

### Therefore, the correct answer is (


### Translate the English word to German.:

Therefore, the correct answer is (a) Beziehung.
Context 1:

### Q. camp


### A. You may have to get a little... ;

Das Lager ist ein Ort, an dem Menschen leben oder arbeiten. Das
Lager kann ein Zeltlager, ein Ferienlager oder ein anderes Lager
sein.
Translate the English word to German.:
Therefore, the correct answer is (
0x641: cmp esi,ebx ;
Therefore, the correct answer is (a) Lager.

## Q.


## A.

Das ist eine Frage, die nicht so einfach zu beantworten ist. Es
gibt
Context 2:

### Q. lecture


### A. You may have to get a little... ;

Der Vortrag ist eine Rede, die vor einem Publikum gehalten wird.
Der Vortrag kann eine Prasentation, ein Vortrag oder eine andere
Art von Vortrag sein.
Translate the English word to German.:
Therefore, the correct answer is (

### Translate

0x641: cmp esi,ebx ;
Therefore, the correct answer is (a) Vortrag.

## Q.


## A.

Der Vortrag ist eine Rede, die vor einem Publikum gehalten wird.
Der Vortrag
55

<!-- Page 56 -->

56

<!-- Page 57 -->


## K.1.19 Translationenglish-Spanish

Prompt 0:Traduccion al espanol -> QUOTE: Translate to Spanish
Prompt 1: In Spanish, these five words are:

### Contexts

Context 0:

### Q. bear

A. Translate to Spanish: oso

### Q. bear

A. Translate to Spanish: oso

### Q. bear

A. Translate to Spanish: oso

### Q. bear

A. Translate to Spanish: oso

### Q. bear

Translate these five English words to Spanish.
Therefore, the correct answer is (a) oso.

### Context 1:


### Q. relativity

A. Translate to Spanish: relatividad

### Q. relativity

A. Translate to Spanish: relatividad

### Q. relativity

A. Translate to Spanish: relatividad

### Q. relativity

A. Translate to Spanish: relatividad

### Q. relativity

Translate these five English words to Spanish.
Therefore, the correct answer is (a) relatividad.

### Q. bear

A. Translate to Spanish: oso

### Q. bear

A. Translate to Spanish
Context 2:

### Q. concert

A. Translate to Spanish: concierto

### Q. concert hall

A. Translate to Spanish: sala de conciertos

### Q. concertmaster

A. Translate to Spanish: concertino

### Q. concerto

A. Translate to Spanish: concierto

## Q.

Translate these five English words to Spanish.
Therefore, the correct answer is (a) concierto.
57

<!-- Page 58 -->


## K.1.20 Translationenglish-French

Prompt 0: I’ve translated 5 words from English to French:
Prompt 1: Translate to French

### Contexts

Context 0:

### Q. destiny

A. I’ve translated 5 words from English to French:
English

### French

destiny
destin
destiny
destin
destiny
destin
destiny
destin
destiny
destin

### Translate to French

Therefore, the correct answer is (destin).

### Q. destiny

A. I’ve translated 5 words from English to French:

### English


### Context 1:


### Q. ideology

A. I’ve translated 5 words from English to French:
English

### French

ideology
ideologie
ideology
ideologie
ideology
ideologie
ideology
ideologie
ideology
ideologie

### Translate to French

Therefore, the correct answer is (ideologie).
58

<!-- Page 59 -->


### Q. ideology

A. I’ve translated 5 words from English to French:

### English


### Context 2:


### Q. representation

A. I’ve translated 5 words from English to French:
English

### French

representation
representation
representation
representation
representation
representation
representation
representation
representation
represent

### Translate to French

Therefore, the correct answer is (representation).

### Q. representation

A. I’ve translated 5 words from English to French:
English
59

<!-- Page 60 -->


## K.1.21 Sentimentanalysis

Prompt 0: Tell if each review was posted by someone with generally
positive or negative language
Prompt 1:write the number of positive examples

### Contexts


### Context 0:

Q. Despite its faults, Gangs excels in spectacle and pacing.
A. I gave a friend an instruction and five inputs. The friend read
the instruction and wrote an output for every one of the inputs.
B. I gave a friend an instruction and five inputs. The friend read
the instruction and wrote an output for every one of the inputs.
C. I gave a friend an instruction and five inputs. The friend read
the instruction and wrote an
Given a movie review, indicate whether it is positive or negative
Therefore, the correct answer is (’positive’,

### Context 1:

Q. I simply can’t recommend it enough.
A. I gave a friend an instruction and five inputs. The friend read
the instruction and wrote an output for every one of the inputs.
B. I gave a friend an instruction and five inputs. The friend read
the instruction and wrote an output for every one of the inputs.
C. I gave a friend an instruction and five inputs. The friend read
the instruction and wrote an
write the number of positive examples
Therefore, the correct answer is (’positive’,

### Context 2:

Q. There’s a lot to recommend Read My Lips.
A. I gave a friend an instruction and five inputs. The friend read
the instruction and wrote an output for every one of the inputs.
B. I gave a friend an instruction and five inputs. The friend read
the instruction and wrote an output for every one of the inputs.
C. I gave a friend an instruction and five inputs. The friend read
the instruction and wrote an
write the number of positive examples
Therefore, the correct answer is (’positive’,
60

<!-- Page 61 -->


## K.1.22 Sentencesimilarity

Prompt 0: .
Prompt 1: !:There are two kinds of problems / hints that you will
see:!<

### Context 0:

Q. Sentence 1: The polar bear is sliding on the snow. Sentence 2: A
polar bear is sliding across the snow.
A. : Read the two sentences and decide how well the second sentence
expresses the same idea as the first. Then enter the number of the
answer option that best describes your decision.

## The two sentences express the same idea.


## The two sentences express the same idea, but the second sentence

is not as clear as the first.

## The two sentences express the same idea, but the second sentence

is
: Given two sentences, your algorithm must determine the similarity
between the sentences on a scale of 0 to 5. A score of 0 means the
sentences have nothing in common. A score of 5 means the sentences
are semantically similar. The
Therefore, the correct answer is 5.

### Context 1:

Q. Sentence 1: Iranian President praises nuclear deal Sentence 2:

### Iran arrests several spies near nuclear plant

A. . Output the score according to the following rules:
0: The sentences have nothing in common.
1: The sentences are about the same topic, but express different
ideas.
2: The sentences are about the same topic, and express similar
ideas.
3: The sentences are about the
:
Therefore, the correct answer is 1.

### Context 2:

Q. Sentence 1: A girl is playing a flute. Sentence 2: A band is
playing on a stage.
A. .Output the score according to the following rules:
0: The sentences have nothing in common.
1: The sentences are about the same topic, but express different
ideas.
2: The sentences are about the same topic, and express similar
ideas
!: There are two kinds of problems / hints that you will see:!<
Therefore, the correct answer is 1.
61

<!-- Page 62 -->


## K.1.23 Wordincontext

Prompt 0: Determine whether the given word is used with the same
meaning in both sentences. Write
Prompt 1: Decide whether the given word is used in the same meaning
in both sentences.

### Contexts


### Context 0:

Q. Sentence 1: The Times is not the voice of New York. Sentence 2:

### The voice of the law. Word: voice

A. Determine whether the given word is used with the same meaning
in both sentences. Writeyes or no.
The answer is yes.
Decide whether the given word is used in the same meaning in both
sentences.
Therefore, the correct answer is (yes).

### Context 1:

Q. Sentence 1: Do you communicate well with your advisor? Sentence
2: He and his sons haven’t communicated for years. Word:
communicate
A. Determine whether the given word is used with the same meaning
in both sentences. Writeyes or no.
The answer is yes.
Decide whether the given word is used in the same meaning in both
sentences.
Therefore, the correct answer is (yes).

### Context 2:

Q. Sentence 1: Can you take me to the main entrance? Sentence 2:

### Take a scene. Word: take

A. Determine whether the given word is used with the same meaning
in both sentences. Writeyes or no.
The answer is no.
Decide whether the given word is used in the same meaning in both
sentences.
Therefore, the correct answer is (no).

## L Ablations

We performed ablation to measure the impact of various self-referential components of Promptbreeder. Weinvestigatedthefollowingmutationoperatorsandmechanisms:
• Randominitialprompts
The original problem specification for the dataset is used instead of generating an initial
task-promptusingthemutationprompt+thinkingstyle+problemspecification.
• Randominitialmutationprompts
The mutation-prompt ”Please summarize and improve the following instruction:” is used
insteadofrandomlyselectingamutation-promptfromthelist.
• Promptsfromcontext(Lamarckian)
62

<!-- Page 63 -->


## Addsub


## Aqua_Dev


## Cs_Strategy_Qa


## Gsm


## Multiarith


## Singleeq


## Strategy_Qa


## Svamp

Hyper Lamarck SR task-prompt SR mut-prompts
ablation_mode
tesatad
Proportion of fitnesses above baseline (Full algorithm)
100%
-13 -11 -23 -26
-11 -33 -58 1
-16 -15 -80 -29
-37 -36 -73 41
0%
-62 -63 -71 9
-16 -29 -39 -34
-61 -41 -44 -57
-21 -10 -74 -41
-100%
enilesab
evoba
sessentif
fo
%
Figure4: Theresultsofablatingtheonebyonetheself-referentialoperatorscomparedtousingthe
fullalgorithm.0%signifiesanablatedoperationwithneitherpositivenornegativeimpact.Fromleft
to right (Hyper = Removal of mutation-prompt mutation, Lamarck = Removal of Context to taskpromptmutation,SRtask-prompt=Removalofthinking-styleguidedtask-promptinitialization,SR
mut-prompt=Removalofrandomselectionofamutation-promptfromthemutation-promptlist.)
. Percentage scores close to −100% indicate that removing the operation results in lower fitness
atequivalentpointsintherun;converselyscorescloseto100%meanthattheoperationisactively
harmful,becauseindividualshavehigherfitnessesatequivalentpointsintherunwhenthatoperation
isremoved.
TheLamarckian mutationoperator thatgeneratesa task-promptfrom acorrectcontext is
replacedwiththedefaultzero-/first-orderpromptmutationoperation(50:50chanceofone
ortheother)
• Meta-mutation(mutatingmutation-prompts)
Whenmeta-mutationwouldnormallytakeplacethedefaultzero-/first-orderpromptmutationoperationisperformed(50:50chanceofoneortheother)
For each dataset and each ablation, we use a population of 10 for 200 evaluations (equivalent to
20generations,similartolargerexperimentsinthispaper)andcomparetothecompletealgorithm
withthesamepopulationsizeandnoablations.Tomeasurehoweffectiveanablatedoperationis,we
determinetheproportionofevaluationsintheablationthatwerehigherthanthebaselineevaluations
ateachgeneration,andsumtheseoverallgenerationsintherun. TheresultsinFigure4showthat
inmostcasesallthemutationoperatorshaveapositiveimpactonfitness, withtheRandomInitial
Promptshavingthelargestpositiveimpactacrossalldatasets.
We also investigated the influence of different mutation operators on the ETHOS hate speech detection dataset (Mollas et al., 2022) with the under-specified problem specification "Solve the
63

<!-- Page 64 -->

Problem" (in contrast to the standard problem specification "Determine whether a text
contains hate speech"). Promptbreeder achieved a score of 81.6%. The greatest deterioration happens when removing the Lamarckian ‘from context to prompt’ mutation method which
induces the instruction from an example of the correct working out (64.6%). The second greatest
detrimenttoperformancehappenswhenremovingrandominitializationofmutationprompts,randominitializationofprompts,andhyper-mutationofmutationpromptssimultaneously,leavingonly
contextmutation(68.7%). Addingbackonlinemutationincreasesperformancebackto70.4%and
addingrandommutationpromptsbringsthisbackupto73.7%. Thisdemonstratestheinterplayand
importanceofPromptbreeder’sdiversesetofmutationoperators.
64

## Tables

**Table (Page 2):**

| (83.8) (88.1) (85.3) (69.9) (92.2) (91.7) (85.1) (70.8) (87.2) (89.2) (88.1) (72.0) (91.8) (94.7) (92.2) (75.7) 97.7 90.6 72.4 83.8 92.5 94.7 74.4 86.3 95.8 82.2 72.2 73.0 – – – – 99.7 96.4 87.8 90.2 |
|---|
| (93.6) (93.5) (91.6) (80.3) (95.5) (92.1) (90.8) (78.1) 100.0 98.9 87.1 93.7 |


**Table (Page 63):**

| -13 | -11 | -23 | -26 |
|---|---|---|---|
| -11 | -33 | -58 | 1 |
| -16 | -15 | -80 | -29 |
| -37 | -36 | -73 | 41 |
| -62 | -63 | -71 | 9 |
| -16 | -29 | -39 | -34 |
| -61 | -41 | -44 | -57 |
| -21 | -10 | -74 | -41 |
