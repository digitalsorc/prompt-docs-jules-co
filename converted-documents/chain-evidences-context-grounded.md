---
title: "Chain Evidences Context Grounded"
original_file: "./Chain_Evidences_Context_Grounded.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["prompt-engineering", "llm", "rag", "chain-of-thought", "react"]
keywords: ["context", "step", "coe", "cot", "long", "output", "reasoning", "page", "evidence", "short"]
summary: "<!-- Page 1 -->

Chain of Evidences and Evidence to Generate: Prompting for Context Grounded
and Retrieval Augmented Reasoning

### MdRizwanParvez

QatarComputingResearchInstitute(QCRI)
mparvez@hbku.edu.qa
Query: How many years did the city suffer wars against

### Abstract

the Almoravid and Almohad Empires? ### Retrieved Ground-truth Answer: 127

Whilechain-of-thoughts(CoT)promptinghasrev- top-k docs
olutionized how LLMs perform reasoning tasks,

### Ans: 267

its current methods and variation"
related_documents: []
---

# Chain Evidences Context Grounded

<!-- Page 1 -->

Chain of Evidences and Evidence to Generate: Prompting for Context Grounded
and Retrieval Augmented Reasoning

### MdRizwanParvez

QatarComputingResearchInstitute(QCRI)
mparvez@hbku.edu.qa
Query: How many years did the city suffer wars against

### Abstract

the Almoravid and Almohad Empires?

### Retrieved Ground-truth Answer: 127

Whilechain-of-thoughts(CoT)promptinghasrev- top-k docs
olutionized how LLMs perform reasoning tasks,

### Ans: 267

its current methods and variations (e.g, Self-
Step-by-step reasoning: ... The context states that the city suffered
consistency,ReACT,Reflexion,Tree-of-Thoughts
wars against the Almoravid and the Almohad Empires from 1085
(ToT), Cumulative Reasoning (CR) etc.,) suffer until the Battle of Las Navas de Tolosa in 1212. Therefore the ...
from limitations like limited context grounding,
hallucination/inconsistent output generation, and Context Query: Companies with highest
iterative sluggishness. To overcome these chal- number of employees?

### Walmart


### Ground-truth Answer: Walmart

lenges,weintroduceanovelmono/dual-stepzero- is the largest private employer in the
world with 2.3 million employees..
shotpromptingframeworkbuiltupontwounique
strategies Chain of Evidences (COE) and Evi- Department of Defense..
dence to Generate (E2G). Instead of unverified

### Ans: Department of Defense (DoD)

reasoningclaims,ourinnovativeapproacheslever- Step-by-step reasoning: ... The United States Department of Defense
agethepowerof"evidencefordecisionmaking"by is the largest employer in the world with the total to over 2.8 million
employees...
firstfocusingexclusivelyonthethoughtsequences
explicitlymentionedinthecontextwhichthenserve
Figure1: CoT&variantsfalterincontext-awarereasoning.
as extracted evidence, guiding the LLM’s output
Top:Overwhelminglong-textcomplexityleadsmodels’failgenerationprocesswithgreaterprecisionandeffiureevenwhenitgeneratespartially/fullycorrectreasoning
ciency. This simple yet potent approach unlocks
(ingreen). Bottom: Ungroundedinternalreasoningfailsto
thefullpotentialofchain-of-thoughtsprompting,
graspcontext,confusing"DoD"(ungroundededprivateorg
facilitatingfaster,morereliable,andcontextually
inred)vsWalmart(ingreen).
aware reasoning in LLMs. Our framework consistently achieves remarkable results across variousknowledge-intensivereasoningandgeneration fiedwhendealingwithretrievedinformationthatare
tasks, surpassing baseline approaches with state- oftenlongandimperfecttextwithdistractivecontents.
of-the-artLLMs. Forinstance,(i)ontheLogiQA TobolsterLLM’sreasoningcapabilities,theChainbenchmarkusingGPT-4,COEachievesanewstate- of-Thought(CoT)promptingparadigmhasemergedas
of-the-art accuracy of 53.8%, surpassing CoT by
a potent tool (Wei et al., 2022). Subsequent meth-
18%,ToTby11%,andCRby9%;(ii)COEwith
ods, including Self-consistency (SC; (Wang et al.,

### PaLM-2outperformsthevariable-shotperformance

2022)), ReACT (Yao et al., 2022), Reflexion (Shinn
ofGeminiUltraby0.9F1points,achievinganF1
scoreof83.3onDROP.Wereleaseourpromptsand et al., 2023), Tree of Thoughts (ToT; (Yao et al.,
outputsonthesebenchmarksasanewinstruction 2023)),andCumulativeReasoning(CR;(Zhangetal.,
tuningdatasetforfutureresearchatHuggingFace1. 2023b)),generalizeCoTwithvariousmulti-objective,
ensemble-based, or tool-augmented, and trial & er-
1 Introduction rorapproachesbutdonotaddressthecomplexitiesof
context-groundedorretrievalaugmentedgenerations
Retrieval-augmented or context-based generation
(RAG).Wehighlighttwooftheirpivotalbottlenecks:
servesasameanforleveragingrelevantinformation,
(i)CoTfocusessolelyonexpandingstepswithoutverempoweringlargelanguagemodels(LLMs)toreduce
ifyinghypotheses;(ii)excessivelylongretrievedtext
the factual errors in their generation (Islam et al.,
canleadtoincorrectconclusionsevenwithvalidCoT
2024b; Asai et al., 2023a,b). However, despite the
reasonings(exampleinFigure1).
expansion in model and data size, LLMs struggle in

### Multi-step reasoning prompting has emerged as a

contextualreasoning. Thischallengeisfurtheramplipromising alternative to traditional chain-of-thought
1https://huggingface.co/datasets/kagnlp/Chain-of-Evidences/ (CoT)approachesbydecomposingcomplexproblems
5202
raM
71
]LC.sc[
2v78750.1042:viXra

<!-- Page 2 -->

Query: The football manager who recruited David Beckham
managed Manchester United during what timeframe?
CoT prompting E-Step using CoE

## C

to
o T
an
:
s

## G

w
i
e
v
r
e n
t h
a
e
c o n
q
t
u
e
e
x
s
t
t i
a
o
n
n
d a
b a
q
s
u
e
e
d
s t
o
io
n
n ,
t h
y
e
o u
c
r
o
ta
n
s
te
k
x
i
t
s
.
Context Context

## C

an
o
s

## E

w
:
e r

## G

t
i
h
v
e
e n
q u
a
e s
c
t
o
io
n
n
te
b
x
a
t
s
a
e
n
d
d
o n
a
t
q
h
u
e
e s
c
t
o
io
n
n
te
,
x
y
t.
o u

## G

r
e n
ta
e
s
r
k
a te
is
t h
to
e
Think step by step and generate the answer.
Retrieved answer with evidence and explanation
top-k docs

### Ans: 1995-1996 CoT Output Ans: Alex Ferguson CoE Output

Evidence & explanation: The context mentions several football

### Step-by-step reasoning: The context mentions that

managers, but the one who managed Manchester United during

### Manchester United won the Double of Premier League and FA

the timeframe when David Beckham was recruited is Sir Alex

### Cup in the 1995-1996 season. It also mentions that David

Ferguson. This is stated in the context: 'Instead, he had drafted in

### Beckham scored a goal in the 1996 FA Charity Shield match

young players like Nicky Butt, David Beckham, Paul Scholes and
played by Manchester United. Therefore, the football manager
the Neville brothers, Gary and Phil.' The 'he' in this sentence
who recruited David Beckham managed Manchester United
refers to Alex Ferguson, who was the manager of Manchester
during the 1995-1996.
United from 1986 to 2013.
CoT Variants: Self-consistency, ReACT,
Reflexion, ToT, Cumulative Reasoning

### Query


### Retrieved

top-k docs

### Context G-Step using CoE Context

CoT-V: Given a context and a question, your task is
to answer the question based on the context. CoE

### Think/plan step by step and generate the

answer. Evaluate your response, then reflect on CoE Output
mistakes and modify accordingly and repeat back.
CoT-V Output Evidence & explanation: Sir Alex Ferguson managed

### Manchester United during the timeframe when David

Plan/Trial-1: Beckham was recruited, which was from 1986 to 2013.
Thought-1: It asks about David Beckham. From context we
know that…Action-1: Search [David Beckham] Output-
1/Predction-1: 1995-1996.
Observation-1 & Reflection-1: ... Ans: 1986-2013

### Plan/Trial-2:


### Thought-2: Search [Manchester United ] (Continued) …

Figure2: (left)CoTandgenericviewofits(iterative)variants,(right)TheE2Gpipeline: InE-stepour"generateanswith
evidenceandexplanation"instructionextractstherationales,coupledwiththeans,groundedintheoriginalcontext,thenin
Gstepweusethesameinstructiontoderivethefinalanswersolelyfromthe"evidenceandexplanation"oralongwiththe
originalcontext.
intosequentialreasoningsubsteps(Dhuliawalaetal., verification-free zero-shot prompting framework for
2023; Wang et al., 2023a; Zhao et al., 2023; Trivedi context-groundedandretrievalaugmentedreasoning.
et al., 2023; Fu et al., 2022; Creswell et al., 2022;

### Ourframeworkconsistsoftwouniqueandreal-time

Li et al., 2023). However, these techniques typipromptingstrategiesparticularlytailoredforlongconcally require rigorous verification of each intermeditextreasoning. First,single-stepChain-of-Evidences
atestep. Althoughsimpleriterativeverificationstrate-
(COE):toaddresstheproblemofungroundedreasongies—suchasself-check(Miaoetal.,2023)andselfinghypotheses,ourdesignedpromptasksforspecific
refine (Madaan et al., 2024)—have been proposed,
thoughtsequencesthatareexplicitlymentionedinthe
they do not fully address the challenges inherent in
context. Wecallthisseriesofintermediatereasoning
long-context processing or retrieval-augmented gensteps,withdirectlyextractedrationalesfromthegiven
eration. Moreover, they often rely on disparate incontext, ’Evidence’ (as in human decision making).
termediate prompts—such as rationale selection and
Our key distinction from existing CoT approaches is
inference/premisederivation—thatnecessitatek-shot
that instead of mere "thinking step-by-step" (Kojima
annotatedin-contextexemplars,whichareoftendiffietal.,2022)ourpromptinstructionasksfor"step-byculttoconstruct(Islametal.,2025,2024a;Yasunaga
stepreasoningwithexplicitevidenceandexplanation".
etal.,2024). Therefore,unlockingCoT’struepotential

### Second,dual-stepEvidencetoGenerate(E2G):to

for RAG & context driven reasoning remains unanfacilitate LLMs’ answering the query properly even
swered. Toaddress,inthispaper,weproposeasimple
with retrieval augmented long-text contexts, we split

<!-- Page 3 -->

the task into steps. In the first step (E), we adopt shotCoTpromptsLLMswithageneralinstructionlike
promptssimilarto COE andgenerateboththeAnswer “thinkstepbystep”toproduceintermediatereasoning
&Evidence. Theninnextstep(G),wepassonlythe steps(See Figure2).
Evidence as context for a second round of COE to
3 OurPromptingFramework
LLM.GStepAnswerispredictedasthefinalanswer.
IncontrasttocomplexlongoriginalcontextinEstep, Inthissection,wedevelopourpromptingframework
the Evidence is a concise short text that directly an- for context-grounding and retrieval augmented longswertheinputquery,Gstepisveryfast,andsimpler textreasoning. Wedesigntwounique(mono/dual-step)
forthemodeltogenerateanswer. prompts that does not require any exemplars and re-
In experiments with different LLMs, we show movesthehurdlesofchoosingmulti-objectiveinstructhatourpromptsconsistentlyoutperformexistingap- tions. Below we first present the prompt instruction
proachesinadiversesetofeightcontext-driventasks, fordefiningtheobjectiveforthetargettask(a.k.asysincludingnaturalQA,complexmulti-hop,long-form temprompt),nextthesingle-steppromptingtechnique
QA,factchecking,dialoggeneration,andreadingcom- ChainofEvidences(COE)andfinallydual-stepEviprehensiontasks. Since,evenwithsuchtechniques,it dencetoGenerate(E2G)thatuses COE twice.
isnon-trivialtocomprehendwhyandhowthisworks
3.1 System/ObjectiveInstruction
andhowtosetuptheprompttofunctioncorrectly,costeffectively,androbustly. Tothisend,weperformcase Ourproposedframeworkisasingle-intentsystem,havstudies, analyze different alternatives and reveal the ing only one target task to solve at a time. Given a
strengthsandweaknessesofourapproach. Weopen- targettaskT,ourobjective/systempromptis:
sourceourpromptsandoutputsonthesebenchmarks
asanewinstructiontuningdatasetforfutureresearch. # You are a/an [T] agent. Given a
context and a [T[x]] as input, please
2 RelatedWorksandPreliminaries
give a [T[y]] output based on the
context.
2.1 PromptingLLMs
Variouspromptingparadigmshavebeenstudiedinlit- T[x]andT[y]dependsonthetaskT.Examplesof
eraturetowardenhancingreasoninginLLMs. InSec- T,T[x]andT[y]are(QA,factverification,dialogue
tion 1, we provide a (non-exhaustive) list of CoT ap- generation),(question,claim,previousdialogue),and
proaches. Amongothers,search-based(Pryzantetal., (answer, judgement, next turn dialogue) respectively.
2023; Lu et al., 2021), Program-aided LLM genera- Anexampleforfactchecking:
tion (Liu et al., 2023a; Gao et al., 2023; Jung et al.,
2022;Zhuetal.,2022),selfgenerationofprompts(He # You are a text classification
et al., 2023; Yasunaga et al., 2023; Sun et al., 2022; agent. Given a context and a claim,
Kimetal.,2022;Lietal.,2022),selfevaluationbased please give a judgement to the claim
approaches(Madaanetal.,2023;Xieetal.,2023;Kim (’SUPPORTS’ or ’REFUTES’) based on the
etal.,2023;Pauletal.,2023)havebeenstudied. Other context.
works have also been extended with more complex
multi-stepreasoningprocedure(e.g.,usingadifferent 3.2 ChainofEvidences(COE)
fine-tuned model (Yu et al., 2023; Nye et al., 2021;

### Whilethe0-shotCoTinstruction(i.e.,Answertheques-


### Lesteretal.,2021))orfordomainspecificapplications

tion. Think step-by-step.) expands the query answer
(Parvezetal.,2023,2021;Ouyangetal.,2022;Sanh
generationintosmallreasoningsteps,itdoesnotfocus
etal.,2021;Weietal.,2021).
oncontext-groundingandgenerateimaginaryhypotheses. To address, our prompt asks for answering the
2.2 Chain-of-Thoughts(CoT)Prompting
queryspecificallywithevidenceandexplanationfrom
Chain-of-thoughts(CoT;(Weietal.,2022))isapromptcontext. We design two alternatives COE-SHORT &
ingframeworkthatguidesLLMstoproduceintermedi-

## Coe-Long.

atereasoningstepstowardsthefinalanswer,enhancing
itsreasoning. OriginalversionofCoTemploysafew- CoE-Short
shot version by providing multiple exemplars of the # Objective Instruction from Section
reasoningprocess(question–reasoning–answer),lever- 3.1
aging LLMs’ in-context learning abilities. However, # Generate the answer with evidence and
duetotherequirementoflabeledexemplars,itquickly explanation.
evolvedwitha0-shotinstance(Kojimaetal.,2022). 0-

<!-- Page 4 -->

|Context| Multi- Context- Cost- E-step G-step
>200 Query Aware Minimize Prompt Context Prompt Context
✗ ✗ ✗ ✗ CoE-Long - - -
✗ ✗ ✗ ✓ CoE-Short - - -
✗ ✗ ✓ ✗ CoE-Long OC - -
✗ ✗ ✓ ✓ CoE-Short OC - -
✗ ✓ ✗ ✗ CoE-Long - - -
✗ ✓ ✗ ✓ CoE-Short - - -
✗ ✓ ✓ ✗ CoE-Long OC CoE-Long E+OC
✗ ✓ ✓ ✓ CoE-Short OC CoE-Short E+OC
✓ ✗ ✓ ✗ CoE-Long OC CoE-Long E
✓ ✗ ✓ ✓ CoE-Short OC CoE-Short E
✓ ✓ ✓ ✗ CoE-Long OC CoE-Long E+OC
✓ ✓ ✓ ✓ CoE-Short OC CoE-Short E+OC
Table1:Recommendedalternativemono/2-stepprompts,&contextsineachstep.OC,Erefertooriginalcontext,Evidence.
CoE-Long (single or multi-question). Regarding objectives, we
prioritizecostoptimizationorperformancetriggering.
# Objective Instruction from Section
Ourdesignprinciplesaremainlythree-folds:
3.1
# Think step-by-step and generate the

## Single-stepCOEisgenerallysufficient,exceptfor

answer with evidence and explanation.
longercontextswhere E2Gisemployed.

## Cost-effectivenessistiedtothenumberofstepsor

AnoverviewisinFigure2. However,dependingon

### LLMAPIcalls. Thus,for E2G, COE-SHORT is

thetaskT,weaddoneortwoadditionalinstructionsto
more cost-effective in each step, while COE-
clarifyhowtheanswershouldbegenerated,andwhat
LONG offersgranularreasoningsteps,enhancing
shouldbetheoutputformat:
performance,particularlyincontext-lessreasoningtaskslikearithmeticandcommonsense.
# Your answer must be the either of
(’SUPPORTS’ or ’REFUTES’) based on the 3. The G-step context is typically derived from
claim and the context. EvidencefromtheE-step. However,forqueries
# Generate your response in a json involvingmultiplesub-queriesoranswers,abrief
output format with an ’answer’ tag and Evidencemayprovideonlypartialanswers. In
an ’evidence and explanation’ tag such cases, the G-step context should include
Evidenceconcatenatedwiththeoriginalcontext.
While both COE prompts generates more context- Table1summarizestheseprinciples.
driven reasonings which are often very concise w.r.t
Another objective, we consider is inference time.
the original context, COE-LONG prompt, which in-
Whiletheworst-caseruntimeofourapproachisapproxcludes"step-by-step"command,instructsthemodelto
imatelydoublethatofCoT,shorterEvidencereduces
generatemoreverboseandexpandedreasoningpaths
runtime(e.g.,1.5svsCoT’s1sonaverage),makingit
in compare to COE-SHORT. Hence, typically COE-
suitable for practical use cases. However, more con-
LONG tends to be more accurate (e.g., for commonstrainedinferencetimecanbeachievedviasingle-step
sense,multi-stepreasoning,orarithmeticcases)while

## Coe.

COE-SHORT ismorecost-effective.
4 ExperimentalSetup
3.3 Adaptation
Inthissection,weoutlinehowourframeworkadapts We evaluate our prompting framework across eight
tovarioustasksandobjectives. Ourframeworkoffers context-intensivelanguagetasks,requiringreasoning
choicesbetweenmono/dualstepprompting,COEalter- over given contexts, including those with distracting
natives,andcontextinputs. Consideringtaskcomplex- documentsandretrievalaugmentationforgeneration.
ity,weexaminethenatureofthetask(context-aware UsingthreeLLMs(ChatGPT,GPT-4,PaLM-2(540B))
orcontext-free),contextlength,andquerycomplexity viaAPIs,weconductcomprehensiveexperiments. Due

<!-- Page 5 -->

Dataset Size Reasoning ∣Context∣ Task Metric
LogiQA 651 77 LogicalReasoning Acc

## Mrc

DROP 500 196 ArithmeticReasoning F1

## Cg P

HotpotQA 7.41K /1.5K Distarctor 1106 Multi-hopQA

## Nq 500 Em,F1

Open-domainQA

## Tqa 1.5K

WOW 500 RAG 650-675 Know. GroundedDialougeGen.

## F1

ELI5 300 LongFormQA

## Cg P


### FEVER 10.1K /.1K FactVerification Acc

Table2: EvaluationDatasets. MRC,anddistractordenotemachinereadingcomprehension,andcontextwithdistracting
documents. |Context|denotesavgtokenlength. CG/P denoteswithChatGPTandPALM-2respectively.
to the size of the datasets, we use sampling and dev

### Backbone Method Acc Steps

splits for evaluation, following established practices.
a
WecompareourresultswithCoTbaselinesandother CoT 38.6 1
frameworks from the literature, reproducing 0-shot a

### CoT-SC 40.4 16

CoT where necessary. For retrieval tasks, we utilize GPT-4 ToT a 43.0 19.87
datasets from Wang et al. (2023b), comprising DPR
a

## Cr 45.3 17

(Karpukhin et al., 2020) retrieved top-5 context documents from Wikipedia. Benchmark summaries are COE-LONG 53.8% 1
in Table 2. By default, we use the single-step COE- CoT 35.0 1
LONG forLogiQA&DROP,andtwo-step E2G (with

### PaLM-2 CoT-SC 36.3 3

COE-SHORT)forothertaskswhereG-stepcontextsare

## Coe-Long 36.4 1

sourced from Evidence, unless otherwise specified.
b
WeuseDalvietal.(2024)inimplementation. PREVIOUS SOTA - 45.8 -

### Table3:

PerformanceonLogiQA.a−brefertoZhangetal.
5 MainResults
(2023b)andOuyangetal.(2021)respectively.

### Arithmetic/LogicalContextReasoning Weevaluate

our approach on the MRC tasks LogiQA and DROP,
decisionsforMCQoptionsdirectlyineverystep,COE-
knownforheavyarithmeticandlogicalreasoningcom-
LONG explains how the option can/not be inferred
plexities. LogiQAtasksinvolvechoosingamongfour
fromthecontext(example: AppendixFig5). Similarly,
options inferred from a small context, while DROP

### Table4showsanexamplehow COE providessuperior

tasksrequireansweringquestionswithcomplexarith-
2 reasoning w.r.t CoT (more in Appendix). On DROP,
meticcomputationsfromthecontext. Althoughrea-

### PaLM-2achieveshigherperformancesthanGPT-4in

soninginbothtasksislargelyindependent,LLMsstill
general,andwith COE-LONG itoutperformsthefewneed to align their reasoning with the context. Our
shotF1scoresofrecentperformerLLMGeminiUltra.
method, presented in Table 3 for LogiQA and Table
5 for DROP, robustly enhances real-time contextual Besides, in compare to the best performances of
reasoning in both benchmarks, achieving new state- COE-LONG in these two tasks, F1 performances of
of-the-art 0-shot results. In both benchmarks, COE- COE-SHORTare(LogiQA53.8vs51.8)and(83.3vs
LONG significantlyoutperformedexistingapproaches. 82.7)whichvalidatesourintuitionthatCOE-LONG ex-
For instance, in Table 3 using GPT-4 as backbone cels more when the task is based on arithmetic and
COE-LONG achieves9%and11%higherAccthanCR logical reasoning. In addition, replacing the COE-
andToTrespectivelyonLogiQAwhiletheiriterations LONG with COE-SHORT,weobserveaperformance
are much higher in number. This reveals that vari- drop of around 2% & 0.6% in LogiQA amd DROP
antsbuiltonCoTalsosufferfromgeneratingoutputs respectively–whichvalidatesourintuitionthatCOE-
inconsistent to context, and guiding their reasoning LONG reasoningisbothmorecontext-drivenandmodpaths with grounding precision can enhance CoT ap- ularcombiningboththeCOE-SHORT andCoT.Insimproachesbroadly. WefindthatwhileCoTpromptsgive plemathtasks(e.g.,GSM8K),ourmethodperformsas
goodasCoTastheyareoftencontext-free.
2Wecomparewithbaselineperformances(i.e.,CoT,CoT-SC)

### Multi-hopQAwithDistractingContexts Wetackle

reportedinpreviousworksiftheyarehigherthanourreproduced
ones. more complex QA challenges, evaluating on the dis-

<!-- Page 6 -->

Q: Howmanyfieldgoalsofatleast40yardsdidNeilRackersmake

### Ans: [‘2’,‘2’]

Context: .. In the fourth quarter, the Seahawks took the lead with Brown kicking another 28-yard field goal. However, Arizona rallied to tie the game on a
Rackers52-yard..ArizonaquicklymovedintofieldgoalrangeaftertheSeahawkTD,
but Rackershittheuprightfrom53yards astimeexpired. .. Arizonathendroveto
theSeahawks’25-yardline,where Rackerskickedagame-winning42-yardfieldgoal
with11secondsleft.
CoTReasonings: Thequestionisaskingforthenumberoffieldgoalsofatleast40yardsthatNeilRackers
made.ThecontextstatesthatRackersmadea 52yardfieldgoal,a 42-yardfieldgoal,
anda 53-yardfieldgoal.Therefore,theansweris3.
CoE-ShortReasonings: The question is asking for the number of field goals of at least 40 yards that Neil
Rackers made. The context states that Rackers made a 52yardfieldgoal and a
42-yardfieldgoal.Hence,theansweris2.
Table4: CoTdistractedbyfocusingonnumericalprecisiononly. COE-LONG providessuperiorreasoningbyconsidering
botharithmeticandvalidityofrationales.
Backbone Method EM F1 HotpotQA FEVER
Backbone Method

### EM F1 Acc

CoT 56.2 71.3

## Gpt-4

CoT 43.4 55.3 76.7

## Coe-Long 56.4 73.7

a ChatGPT Rct+Rfl3(t=2) 42 - -

### CoT - 82.0

PaLM-2 E2G 47.1 59.6 80.7

## Coe-Long 79.6 83.3

CoT 44.49 55.76 78.0
a b PaLM-2

## Few-Shotsota - 82.4 /83.0


## E2G 46.76 57.90 82.0


## Sota - 72.71 85.01 94.22


### Table5:


### ResultsonDROP.a−b

refertoGeminiTechnical
Report(Teametal.,2023)andHuangetal.(2022). Table6:PerformanceonHotpotQA.1−3referstoZhangetal.
(2023a),Wangetal.(2023b),Shinnetal.(2023)respectively.
t=2referstoourequivalent2trials. Rct,RfldenoteReACT,
tractor split of HotpotQA (Yang et al., 2018), where andReflexionrespectively.
eachqueryfacesalargecontextwithtworelevantand
eightirrelevantdocuments,withonly2-5far-apartsenapproach. WeemployChatGPTtoestablishoneagent
tencesservingasrationales. ResultsinTable6show
tasked with co-reference resolution, another as a rethatE2G ,usingbothChatGPTandPaLM-2,outpertriever model for sentence ranking, and a third as a
formsCoTandothervariantsbyalargemargin. With
QA agent for generating the final answer. However,

### ChatGPT,E2Gachievesa4%gaininbothEMandF1

thisapproachlagsbehindby10EMpointscompared
scoresoverCoT,whilewithPaLM-2,thegainsare2%.
to ours. We identify multiple issues, including each
OtheriterativebaselineslikeReACTandReflexionfind
agentcontributingtopropagatingitsownerrorssuch
therelevanttextsonebyone,leadingtolongertrialsor
asimperfectco-referenceresolutionandranking. We
failuretoutilizeallrelevanthopseffectively. Notethat
also find that the agents are overly sensitive to input
with PaLM-2, their literature reported performances
objectiveinstructions.
arefoundwithPaLM-1andwedonotreproducethem
astheyusefew-shotexamples,leverageexternaltools, Inaddition,akeybottleneckarisesfromtheretriever
and involve iterative generations. In contrast, both E agentasitisunawareofhowitsoutputswillbecomandGstepsofE2Gaddresstheentireproblemineach bined by the later QA agent, leading to sub-optimal
step,demonstratinggreaterefficiency. Asconnecting ranking. Forinstance,whenqueriedabouttwopersons,
the relevant texts distant apart is one of the key chal- alltop-k sentencespertainingtoonesamepersonmay
lengesinmulti-hopQA,tounderstandtheadvantages be ranked higher than those about the other, adding
ofextractingEvidencealongwiththeanswer(i.e.,sin- complexitytothetask. Inaddition,weobservesome
gleobjectiveinbothsteps),weperformanadditional interestinghallucinationtrendswithCoTwhentheconexperiment towards a multi-agent or multi-objective text contains distractions: LLMs’ hallucination even

<!-- Page 7 -->

Q: ArebothDafengDistrictandDazhoulocatedinthesameprovince?

### Ans: No

CoTReasonings: DafengDistrictandDazhouarebothlocatedinthesameprovince,whichisSichuan
province. Falseinformationisgiveninthecontext thatDafengandDazhouarelocated
indifferentprovinces.

### Ans: Yes

COE-SHORT Reasonings: Dafeng District and Dazhou are not located in the same province.
DafengDistrictisinJiangsuprovince while DazhouisinSichuanprovince.

### Ans: No

Table7: CoTreasoningdoesnotaccountforgrounding–evenoverridesthecontextualfactwithitspre-trainedknowledge(or
hallucinates). FindingEvidence,E2Genablesmorefactuallyverifiedreasoning.

## Nq Tqa Wow Eli5


### Backbone Method


## Em F1 Em F1 F1 F1

CoT 41.6 51.9 68.3 75.4 13.4 27.0

### ChatGPT


## E2G 42.8 53.0 69.5 76.9 15.0 25.1

CoT 28.4 36.6. 46.9 51.9 12.2 15.3

### PaLM-2


## E2G 31.2 39.5 46.7 52.1 12.4 17.4


## Sup. Sota1 61.8 - 71.1 68.3 73.9

Table8: ResultsonNQ,TQA,WOW,andELI5. 1&RedrefertoWangetal.(2023b)&aninferiorperformance.
overridethefactualinformationinthecontext. Table7 oftenjointorhasmultiplenamedentityanswers,and
illustratesthiswithanexamplewhere E2G construc- hence we choose to the analyze the affect of differtivelyemphasizesonevidencesandtacklesthis. Ina ent alternatives for the G-Step context. As shown in
furtherexperiment,wefindanincreaseof5pointsboth Table9,LLMsoutputscananswerpartiallyinE-step
EMandF1scorewhenusing COE-LONG insteadof andusingEvidence + Original ContextasG-step
COE-SHORT–validatingitshighereffectiveness. contextprovidesadditionalchancestothemodelforan-
RetrievalAugmentedGeneration Inadditiontothe sweringthequeryfully-consequentlyenhancesmodel
MRC and Distractor, we evaluate our framework on enhances. Tograspmoreonimproving E2G,investithefollowingfiveRAGtasksintheKILTbenchmark
(Petronietal.,2021). Context in G-step Vs Performance

### FactVerification: WeadopttheFactExtractionand 55

VERification (FEVER) dataset (Thorne et al., 2018). 50 51.75 53.02 53.25
Thetaskinvolvesdeterminingwhetheraclaimaligns
45
withfactsinaWikipediareference("SUPPORTS")or
40 41.6 42.8 43.2
contradictsthem("REFUTES"). AsshowninTable6,
E2G outperforms strong baselines by more than 4% 35

## Em F1

acrossbothLLMs. FurthercomparisonswithCoT-SC

### Evidence Evidence+Orginal Context Adaptive

(Self-consistency; (Wang et al., 2022)) validate that
performance gaps of over 2% persist. Our Evidence Figure 3: Reasoning with different "Context" in G-step.
capturesessentialrationalesforclaimevaluation,and Adaptivemeansselectingthemdynamicallyonthefly.
akin to HotpotQA, our global problem-solving approachprovidesadvantagesoveriterativeCoTvariants gatingthedatasetmore,wefurtherdevelopanadaptive
(FEVERreasoningexamplesareinAppendix). G-step context with a heuristic that the well formed
Open-Domain Question Answering: We adopt the questions(startswithwhwordsor"be/do/have/modal"
Natural Questions (NQ) (Kwiatkowski et al., 2019) words) are often from this multi-query type. Hence
and TriviaQA (TQA) (Joshi et al., 2017) benchmark usingEvidence + Original Contextforthemand
toanalyzeourpromptingframework. Foreachexam- usingonlyEvidence)forill-formedothers(e.g.,my
ple,thereisashortassociatedanswers(lessthanfive ageiswhat?)–leadingtoevenbetterperformances. Figtokens)togenerate. Wepresentmodelperformances ure3comparesthem.
w/ E2G inTable8. WenotethatquestionsinNQare Open-endedLongFormGeneration: Though,our

<!-- Page 8 -->


### Q: Whowasindontworrybehappyvideo?


### Ans: [’BillIrwin’,’RobinWilliams’,’McFerrin’]

E-Step(CoE-Short)Reasonings: Thecomedicoriginalvideofor’Don’tWorryBeHappy’starsBobbyMcFerrin,Robin
Williams,andBillIrwin.

### Ans: RobinWilliams

G-Step(CoE-Short)Reasonings Thevideofor’Don’tWorryBeHappy’starsRobinWilliamsandBillIrwinalongwith
McFerrin.

### Ans: RobinWilliamsandBillIrwin

Table9: E-stepmayfocusonansweringpartiallywhenaskedjointquestionsormultiplenamedentityanswers. Hence,to
increaseourchances,insecondstep(G)Context,weusetheEvidence + Original Context.

### Q: Soundscomplicated.Howlongdidittakeyoutolearntodothat?

Ans: ItdependsonhowfastyoucanlearnthelanguagessuchasCOBOL,C,C++,C#,

### Java,Lisp,Python,etc

CoTReasonings: Thecontextprovideddiscussesvarioustopicssuchasgameprogramming..Theuser’s
claimdoesnotrelatetoanyofthesetopics.
Ans: Iamsorry,butyourclaimdoesnotrelatetothecontextprovided.
OurfinalG-StepReasonings: Basedonthecontext,itismentionedthatsoftwaredevelopmenttakesweeksormonths
tocomplete,butitdependsonthecomplexityofthesoftware.Somecomplexsoftware
mayrequiremorethanayearofwork,whileothersare..
Ans: Learningtocreatesoftwarecantakevaryingamountsoftimedependingonthe
complexityofthesoftwareandtheindividual’slearningability.
Table10: DialoguebyChatGPTusingCoTandE2G.
focusistowardthereasoningtasks,wealsoexploreits is very hard in reasoning (even for human) (b) when
potentialinopen-endedgenerationtasks. Weexamine relevanttextliesinthemiddleoratbottomofretrieved
two verbose QA tasks: (i) Knowledge-Grounded Di- context, as noted in (Liu et al., 2023b). (c) linguisalogGenerationusingtheWoWdataset(Dinanetal., tically or logically challenging questions with long
2019), where short dialog histories are provided as contexts(d)reasoningisnotmentionedinthecontext.
context for generating next-turn responses; (ii) Long Wefocusonc,andd. Forproblemc,amongtheerro-
FormQAontheELI5dataset(Fanetal.,2019),requir- neouswhquestions,in23%ofthem,thegoldanswer
ing detailed answers to open-ended questions. Table span is actually present in the reasoning, and for the
8 compares E2G with CoT baseline. Although the erroneous yes/no questions, 75% of their reasoning
performance difference is marginal due to verbosity, actuallyhypothesesoppositeofthepredictedanswer
E2G showsaslightgainoverCoTinWoW.Asmall- (e.g.,"yes"shouldbederivedfromreasoningbutthe
scale human evaluation also favored E2G responses predictedansweris"no"). Thisindicatesthatjustusing
by 71% for factual correctness, similarity to gold re- thereasoningtoanswerthequestioncanachievequite
sponses, and naturalness. Table 10 illustrates a dia- some improvements–justifying our intuition for twologueexample,wheretheoverallresponsesaresimilar stepE2Gprompt. Forproblemd,inouranalyses,23%
despiteverbosity. However,ourresultsinbothbench- oferroneouswhand25%ofyes/noquestionsareofthis
markslagbehindrecentSupervisedSOTAmodels. In category. This suggests a root change in the prompt-
AppendixA.1,weperformadditionalexperimentsand ing strategy to focus on verification of the reasoning
furtherdiscussthegeneralizability. rationalesandtoverify,COEshowsan8%lowererror
rate. Inadditiontoqualitativeanalysis,weemploythe
6 QualitativeCaseStudy: WhyandHow
self-reflectionapproach(Shinnetal.,2023)bydelib-

### OurMethodsWork?

eratelyqueryingtwostate-of-the-artLLMs(ChatGPT
TounderstandmoreonwhyandhowCOEandE2Gen- andGeminiPro)abouttheinternaladvantagesofour
hanceCoTlikereasoninginRAGorwithlongcontext, designedinstructionoverCoT.Detailsareprovidedin
we conduct a case study on CoT reasoning on com- AppendixA.2.
plex multihop HotpotQA with a set of 50 examples.
We observe 4 types of errors: (a) when the question

<!-- Page 9 -->

Q: Whohasthemosttrophiesinthepremierleague?

### Ans: ManchesterUnited

CoTReasonings: ManchesterUnitedhaswonmoretrophiesthananyotherclubinEnglishfootball,witha
record20Leaguetitles,12FACups,5LeagueCupsanda...

### Ans: ManchesterUnited

OurfinalG-StepReasonings: FormerBlackburnRoversandNewcastleUnitedstrikerAlanShearerholdstherecord
formostPremierLeaguegoalswith260...

### Ans: AlanSheare

Table11: Overemphasizingongroundingcanhindermodelfromleveragingworldknowledge,commonsense,etc.,(e.g.,
ManchesterUnitedisateaminpremierleague).
7 ErrorAnalysisandChallenges LLMstodeliverrobust,andaccurate. FutureworkinvolvesLLMinstructionfine-tuningusingourprompted
outputs.
9 Limitations
Our proposed inference framework has achieved significantgainsoverbaselineapproachesacrossvarious
tasks,andinEnglish. However,incertaindatadomains
(e.g., bio-medical domain (Nentidis et al., 2023)), or
Figure4: F1scoresw/E2G&CoTvs(sorted)recall. language (e.g., low-resource languages (Parvez and
Apart from persisted hallucination to some extent, Chang, 2021)), under automatic evaluation metrics,
our experiments and ablations reveal two main limi- andwithsufficientcomputationalresourcesorLLMs,
tationsofourframework. Overemphasisincontext- itmaynotexhibitsuchtrends. Anotheraspectisthat
groundingSomeoveremphasisongroundingleading the performance scale in RAG tasks may also vary
to the model’s failure to infer simple common sense, if the retrieval accuracy is quite different than ours.
leverage generic world knowledge, arithmetic, logic, Our evaluation considers the EM, F1, Accuracy, and
and principles (See Table 11), and in many cases, it suchmatricesformethodcomparisons,andadifferent
causingthemodeltogenerateresponsessuchas"un- comparison outcomes may be found while using difknown,"or"cannotbedetermined". Specificexamples ferentsetsofmatrices. ForRAGtasks, weusetop-5
ofcategoricalmistakesareprovidedintheAppendix. retrieved documents with any context filtering (e.g.,
LowperformanceinlongformgenerationWefind (Parvezetal.,2023))andforalltasks,wedidnotadopt
that the retrieval recalls in WoW and ELI5 are lower anymodelfine-tuning. Underthesechangeinsettings,
than our other RAG tasks (See Figure 4) which may adifferentkindofresultsmaybeobtainedregarding
causethis. Uponinvestigatingmoreonaperformance which we do not conduct any experiments on. We
drop in ELI5: while the task is to generate verbose alsonoteanadditionalriskofgettingdifferentperforanswers,oursarestillshort(Wordlength130vs<100) mancesonadifferentnumberoftestinstancesinthe
andmayactuallynotfulfillingthetargetrequirements– benchmarkdatasetswereported.
suggestingafutureworkofmodelfine-tuning/domain
adaptation.

### Ethics

8 Conclusion

### In this paper, we conduct a small scale human evalu-

In this paper, we address the limitations of existing ation. All our participants were pre-informed about
promptingframeworksforcontext-awareandretrieval the voluntary nature of our survey, approximated reaugmentedreasoning. Wehighlightthechallengeofun- quired time, criteria of the feedback. An example
groundedreasoningrationalesleadingtopotentialhal- human evaluation screen-shot can be found: https:
lucinationsinLLMs. Ournovelframeworkintroduces //forms.gle/h6WJtC7TrDj9LUNc6. The participants
twonewpromptingmethodstoidentifyevidencesin spandifferentcontinents,andaskedthroughauthor’s
the context and generate answers based on that evi- researchchannels.
dence. Acrossvarioustasks,ourapproachempowers

<!-- Page 10 -->

References 62nd Annual Meeting of the Association for ComputationalLinguistics(Volume1: LongPapers),pages4912–
AkariAsai,SewonMin,ZexuanZhong,andDanqiChen.
4944,Bangkok,Thailand.AssociationforComputational
2023a. Retrieval-basedlanguagemodelsandapplications.
Linguistics.
InProceedingsofthe61stAnnualMeetingoftheAssociationforComputationalLinguistics(Volume6: Tutorial MdAshrafulIslam,MohammedEunusAli,andMdRizwan
Abstracts),pages41–46. Parvez.2025. Codesim: Multi-agentcodegenerationand
problemsolvingthroughsimulation-drivenplanningand
AkariAsai,ZeqiuWu,YizhongWang,AvirupSil,andHandebugging. arXivpreprintarXiv:2502.05664.
nanehHajishirzi.2023b. Self-rag: Learningtoretrieve,
generate, and critique through self-reflection. arXiv ShayekhBinIslam,MdAsibRahman,KSMTozammel
preprintarXiv:2310.11511. Hossain, Enamul Hoque, Shafiq Joty, and Md Rizwan

### Parvez. 2024b. Open-RAG: Enhanced retrieval aug-

Antonia Creswell, Murray Shanahan, and Irina Higgins. mentedreasoningwithopen-sourcelargelanguagemod-

## Selection-inference: Exploiting large language els. In Findings of the Association for Computational

modelsforinterpretablelogicalreasoning. arXivpreprint Linguistics: EMNLP2024,pages14231–14244,Miami,
arXiv:2205.09712. Florida,USA.AssociationforComputationalLinguistics.
Fahim Dalvi, Maram Hasanain, Sabri Boughorbel, Basel MandarJoshi,EunsolChoi,DanielWeld,andLukeZettle-
Mousi, SamirAbdaljalil, NiziNazar, AhmedAbdelali, moyer. 2017. TriviaQA: A large scale distantly super-
ShammurAbsarChowdhury,HamdyMubarak,Ahmed vised challenge dataset for reading comprehension. In
Ali,MajdHawasly,NadirDurrani,andFirojAlam.2024. Proceedings of the 55th Annual Meeting of the Associ-
LLMeBench: Aflexibleframeworkforacceleratingllms ation for Computational Linguistics (Volume 1: Long
benchmarking. Papers),pages1601–1611,Vancouver,Canada.AssociationforComputationalLinguistics.

### ShehzaadDhuliawala,MojtabaKomeili,JingXu,Roberta

Raileanu,XianLi,AsliCelikyilmaz,andJasonWeston. Jaehun Jung, Lianhui Qin, Sean Welleck, Faeze Brah-

## Chain-of-verificationreduceshallucinationinlarge man, Chandra Bhagavatula, Ronan Le Bras, and Yejin

languagemodels. arXivpreprintarXiv:2309.11495. Choi.2022. Maieuticprompting: Logicallyconsistent
reasoning with recursive explanations. arXiv preprint
Emily Dinan, Stephen Roller, Kurt Shuster, Angela Fan, arXiv:2205.11822.

### Michael Auli, and Jason Weston. 2019. Wizard of

Wikipedia: Knowledge-poweredconversationalagents. Vladimir Karpukhin, Barlas Oguz, Sewon Min, Patrick
In International Conference on Learning Representa- Lewis, Ledell Wu, Sergey Edunov, Danqi Chen, and
tions. Wen-tau Yih. 2020. Dense passage retrieval for opendomainquestionanswering. InProceedingsofthe2020
AngelaFan,YacineJernite,EthanPerez,DavidGrangier, ConferenceonEmpiricalMethodsinNaturalLanguage
JasonWeston,andMichaelAuli.2019. ELI5: Longform Processing(EMNLP),pages6769–6781,Online.Associquestionanswering. InProceedingsofthe57thAnnual ationforComputationalLinguistics.
Meeting of the Association for Computational Linguistics, pages3558–3567, Florence, Italy.Associationfor GeunwooKim,PierreBaldi,andStephenMcAleer.2023.
ComputationalLinguistics. Language models can solve computer tasks. arXiv
preprintarXiv:2303.17491.

### Yao Fu, Hao Peng, Ashish Sabharwal, Peter Clark, and

Tushar Khot. 2022. Complexity-based prompting for HyuhngJoonKim,HyunsooCho,JunyeobKim,TaeukKim,
multi-stepreasoning. InTheEleventhInternationalCon- KangMinYoo,andSang-gooLee.2022. Self-generated
ferenceonLearningRepresentations. in-contextlearning: Leveragingauto-regressivelanguage
models as a demonstration generator. arXiv preprint
LuyuGao,AmanMadaan,ShuyanZhou,UriAlon,Pengfei arXiv:2206.08082.
Liu, Yiming Yang, Jamie Callan, and Graham Neubig.

## Pal: Program-aidedlanguagemodels. InInterna- TakeshiKojima,ShixiangShaneGu,MachelReid,Yutaka

tionalConferenceonMachineLearning,pages10764– Matsuo, and Yusuke Iwasawa. 2022. Large language

### PMLR. modelsarezero-shotreasoners. Advancesinneuralinformationprocessingsystems,35:22199–22213.


### ZhiweiHe,TianLiang,WenxiangJiao,ZhuoshengZhang,

YujiuYang,RuiWang,ZhaopengTu,ShumingShi,and TomKwiatkowski,JennimariaPalomaki,OliviaRedfield,
Xing Wang. 2023. Exploring human-like translation MichaelCollins,AnkurParikh,ChrisAlberti,Danielle
strategy with large language models. arXiv preprint Epstein, Illia Polosukhin, Jacob Devlin, Kenton Lee,
arXiv:2305.04118. KristinaToutanova,LlionJones,MatthewKelcey,Ming-

### WeiChang,AndrewM.Dai,JakobUszkoreit,QuocLe,

Jiaxin Huang, Shixiang Shane Gu, Le Hou, Yuexin Wu, andSlavPetrov.2019. Naturalquestions: Abenchmark
Xuezhi Wang, Hongkun Yu, and Jiawei Han. 2022. for question answering research. Transactions of the
Largelanguagemodelscanself-improve. arXivpreprint AssociationforComputationalLinguistics,7:452–466.
arXiv:2210.11610.

### BrianLester,RamiAl-Rfou,andNoahConstant.2021. The

Md.AshrafulIslam,MohammedEunusAli,andMdRizwan powerofscaleforparameter-efficientprompttuning. In
Parvez.2024a. MapCoder: Multi-agentcodegeneration Proceedingsofthe2021ConferenceonEmpiricalMethforcompetitiveproblemsolving. InProceedingsofthe odsinNaturalLanguageProcessing,pages3045–3059,

<!-- Page 11 -->

OnlineandPuntaCana,DominicanRepublic.Associa- Md Rizwan Parvez, Wasi Ahmad, Saikat Chakraborty,
tionforComputationalLinguistics. Baishakhi Ray, and Kai-Wei Chang. 2021. Retrieval
augmentedcodegenerationandsummarization. InFind-
JunlongLi,ZhuoshengZhang,andHaiZhao.2022. Self- ings of the Association for Computational Linguistics:
prompting large language models for open-domain qa. EMNLP2021,pages2719–2734,PuntaCana,Dominican
arXivpreprintarXiv:2212.08635. Republic.AssociationforComputationalLinguistics.
XingxuanLi,RuochenZhao,YewKenChia,BoshengDing, MdRizwanParvezandKai-WeiChang.2021. Evaluating
Lidong Bing, Shafiq Joty, and Soujanya Poria. 2023. thevaluesofsourcesintransferlearning. InProceedings
Chainofknowledge: Aframeworkforgroundinglarge ofthe2021ConferenceoftheNorthAmericanChapterof
languagemodelswithstructuredknowledgebases. arXiv theAssociationforComputationalLinguistics: Human
preprintarXiv:2305.13269. LanguageTechnologies,pages5084–5116.
Bo Liu, Yuqian Jiang, Xiaohan Zhang, Qiang Liu, Shiqi MdRizwanParvez,JianfengChi,WasiUddinAhmad,Yuan
Zhang,JoydeepBiswas,andPeterStone.2023a. Llm+ Tian,andKai-WeiChang.2023. Retrievalenhanceddata
p: Empoweringlargelanguagemodelswithoptimalplan- augmentationforquestionansweringonprivacypolicies.
ningproficiency. arXivpreprintarXiv:2304.11477. InProceedingsofthe17thConferenceoftheEuropean

### Chapter of the Association for Computational Linguis-

NelsonFLiu,KevinLin,JohnHewitt,AshwinParanjape, tics,pages201–210,Dubrovnik,Croatia.Associationfor
Michele Bevilacqua, Fabio Petroni, and Percy Liang. ComputationalLinguistics.
2023b. Lost in the middle: How language models use
longcontexts. arXivpreprintarXiv:2307.03172. Debjit Paul, Mete Ismayilzada, Maxime Peyrard, Beatriz

### Borges, Antoine Bosselut, Robert West, and Boi Falt-

XimingLu,SeanWelleck,PeterWest,LiweiJiang,Jungo ings.2023. Refiner: Reasoningfeedbackonintermediate
Kasai, Daniel Khashabi, Ronan Le Bras, Lianhui Qin, representations. arXivpreprintarXiv:2304.01904.

### YoungjaeYu,RowanZellers,etal.2021. Neurologica*

esquedecoding: Constrainedtextgenerationwithlooka- FabioPetroni,AleksandraPiktus,AngelaFan,PatrickLewis,
headheuristics. arXivpreprintarXiv:2112.08726. Majid Yazdani, Nicola De Cao, James Thorne, Yacine

### Jernite,VladimirKarpukhin,JeanMaillard,VassilisPla-

AmanMadaan,NiketTandon,PrakharGupta,SkylerHalli- chouras,TimRocktäschel,andSebastianRiedel.2021.
nan,LuyuGao,SarahWiegreffe,UriAlon,NouhaDziri, KILT: a benchmark for knowledge intensive language
Shrimai Prabhumoye, Yiming Yang, et al. 2023. Self- tasks. In Proceedings of the 2021 Conference of the
refine: Iterative refinement with self-feedback. arXiv NorthAmericanChapteroftheAssociationforComputapreprintarXiv:2303.17651. tionalLinguistics:HumanLanguageTechnologies,pages
2523–2544,Online.AssociationforComputationalLin-
AmanMadaan,NiketTandon,PrakharGupta,SkylerHalli- guistics.
nan,LuyuGao,SarahWiegreffe,UriAlon,NouhaDziri,
Shrimai Prabhumoye, Yiming Yang, et al. 2024. Self- ReidPryzant,DanIter,JerryLi,YinTatLee,Chenguang
refine: Iterativerefinementwithself-feedback. Advances Zhu,andMichaelZeng.2023. AutomaticpromptoptiinNeuralInformationProcessingSystems,36. mizationwith"gradientdescent"andbeamsearch. arXiv
preprintarXiv:2305.03495.
NingMiao,YeeWhyeTeh,andTomRainforth.2023. Selfcheck: Usingllmstozero-shotchecktheirownstep-by- VictorSanh,AlbertWebson,ColinRaffel,StephenHBach,
stepreasoning. arXivpreprintarXiv:2308.00436. Lintang Sutawika, Zaid Alyafeai, Antoine Chaffin, Arnaud Stiegler, Teven Le Scao, Arun Raja, et al. 2021.
AnastasiosNentidis,AnastasiaKrithara,GeorgiosPaliouras, Multitaskpromptedtrainingenableszero-shottaskgener-
EulàliaFarré-Maduell,SalvadorLima-López,andMar- alization. arXivpreprintarXiv:2110.08207.
tinKrallinger.2023. Bioasqatclef2023: Theeleventh
editionofthelarge-scalebiomedicalsemanticindexing Noah Shinn, Beck Labash, and Ashwin Gopinath. 2023.
andquestionansweringchallenge. InAdvancesinInfor- Reflexion: anautonomousagentwithdynamicmemory
mationRetrieval. andself-reflection. arXivpreprintarXiv:2303.11366.
MaxwellNye,AndersJohanAndreassen,GuyGur-Ari,Hen- Zhiqing Sun, Xuezhi Wang, Yi Tay, Yiming Yang, and
rykMichalewski,JacobAustin,DavidBieber,DavidDo- DennyZhou.2022. Recitation-augmentedlanguagemodhan, Aitor Lewkowycz, Maarten Bosma, David Luan, els. arXivpreprintarXiv:2210.01296.
etal.2021. Showyourwork: Scratchpadsforintermediatecomputationwithlanguagemodels. arXivpreprint Gemini Team, Rohan Anil, Sebastian Borgeaud, JeanarXiv:2112.00114. BaptisteAlayrac,JiahuiYu,RaduSoricut,JohanSchalkwyk,AndrewMDai,AnjaHauth,KatieMillican,etal.
LongOuyang,JeffreyWu,XuJiang,DiogoAlmeida,Car- 2023. Gemini: a family of highly capable multimodal
rollWainwright,PamelaMishkin,ChongZhang,Sand- models. arXivpreprintarXiv:2312.11805.
hini Agarwal, Katarina Slama, Alex Ray, et al. 2022.
Traininglanguagemodelstofollowinstructionswithhu- JamesThorne,AndreasVlachos,ChristosChristodoulopoumanfeedback. AdvancesinNeuralInformationProcess- los,andArpitMittal.2018. FEVER:alarge-scaledataset
ingSystems,35:27730–27744. forfactextractionandVERification. InProceedingsof
the2018ConferenceoftheNorthAmericanChapterof
SiruOuyang,ZhuoshengZhang,andHaiZhao.2021. Fact- theAssociationforComputationalLinguistics: Human
drivenlogicalreasoning. CoRR,abs/2105.10334. LanguageTechnologies,Volume1(LongPapers),pages

<!-- Page 12 -->

809–819,NewOrleans,Louisiana.AssociationforCom- LogiQA DROP
putationalLinguistics. Method

### Acc EM F1

Harsh Trivedi, Niranjan Balasubramanian, Tushar Khot,

### CoT 35.0 51.0 62.06

and Ashish Sabharwal. 2023. Interleaving retrieval
withchain-of-thoughtreasoningforknowledge-intensive COE-LONG 41.0 52.0 63.77
multi-stepquestions. InProceedingsofthe61stAnnual
MeetingoftheAssociationforComputationalLinguistics
Table12: ResultsonLogiQAandDROPusingGemini-Pro.
(Volume1: LongPapers),pages10014–10037,Toronto,
Canada.AssociationforComputationalLinguistics.

### Method ReCLOR(Acc)

Jianing Wang, Qiushi Sun, Nuo Chen, Xiang Li, and

### CoT 46

Ming Gao. 2023a. Boosting language models reasoningwithchain-of-knowledgeprompting. arXivpreprint

### CoT-SC 49

arXiv:2306.06427.

## Coe-Long 53.0


### Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc Le,

Ed Chi, Sharan Narang, Aakanksha Chowdhery, and Table13: ResultsonReCLORusingChatGPT.
Denny Zhou. 2022. Self-consistency improves chain
ofthoughtreasoninginlanguagemodels. arXivpreprint
arXiv:2203.11171.
Zhou.2024. Largelanguagemodelsasanalogicalreasoners. InTheTwelfthInternationalConferenceonLearning
Zhiruo Wang, Jun Araki, Zhengbao Jiang, Md Rizwan
Representations.
Parvez, and Graham Neubig. 2023b. Learning to filter context for retrieval-augmented generation. arXiv
preprintarXiv:2311.08377. Weihao Yu, Zihang Jiang, Yanfei Dong, and Jiashi Feng.

## Reclor:Areadingcomprehensiondatasetrequiring

JasonWei,MaartenBosma,VincentYZhao,KelvinGuu, logicalreasoning. arXivpreprintarXiv:2002.04326.

### AdamsWeiYu,BrianLester,NanDu,AndrewMDai,

andQuocVLe.2021. Finetunedlanguagemodelsare WenhaoYu,HongmingZhang,XiaomanPan,KaixinMa,
zero-shotlearners. arXivpreprintarXiv:2109.01652. Hongwei Wang, and Dong Yu. 2023. Chain-of-note:

### Enhancing robustness in retrieval-augmented language

Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten models. arXivpreprintarXiv:2311.09210.
Bosma,FeiXia,EdChi,QuocVLe,DennyZhou,etal.

## Chain-of-thoughtpromptingelicitsreasoningin JiahaoZhang,HaiyangZhang,DongmeiZhang,YongLiu,

largelanguagemodels. AdvancesinNeuralInformation andShenHuang.2023a. Beamretrieval: Generalend-
ProcessingSystems,35:24824–24837. to-endretrievalformulti-hopquestionanswering. arXiv
preprintarXiv:2308.08973.
YuxiXie,KenjiKawaguchi,YiranZhao,XuZhao,Min-Yen

### Kan,JunxianHe,andQizheXie.2023. Decomposition

YifanZhang,JingqinYang,YangYuan,andAndrewChienhancesreasoningviaself-evaluationguideddecoding.
ChihYao.2023b. CumulativereasoningwithlargelanarXivpreprintarXiv:2305.00633.
guagemodels. arXivpreprintarXiv:2308.04371.
Zhilin Yang, Peng Qi, Saizheng Zhang, Yoshua Bengio,
RuochenZhao, XingxuanLi, ShafiqJoty, ChengweiQin,
WilliamCohen,RuslanSalakhutdinov,andChristopherD.
andLidongBing.2023. Verify-and-edit: Aknowledge-
Manning. 2018. HotpotQA: A dataset for diverse, exenhanced chain-of-thought framework. arXiv preprint
plainablemulti-hopquestionanswering. InProceedings
arXiv:2305.03268.
of the 2018 Conference on Empirical Methods in NaturalLanguageProcessing,pages2369–2380,Brussels,

### XinyuZhu,JunjieWang,LinZhang,YuxiangZhang,Ruyi

Belgium.AssociationforComputationalLinguistics.

### Gan, Jiaxing Zhang, and Yujiu Yang. 2022. Solving

math word problem via cooperative reasoning induced
Shunyu Yao, Dian Yu, Jeffrey Zhao, Izhak Shafran,
languagemodels. arXivpreprintarXiv:2210.16257.
ThomasLGriffiths,YuanCao,andKarthikNarasimhan.

## Treeofthoughts: Deliberateproblemsolvingwith

largelanguagemodels. arXivpreprintarXiv:2305.10601. A Appendix
ShunyuYao,JeffreyZhao,DianYu,NanDu,IzhakShafran,

### A.1 AdditionalExperimentsonGeneralizability

KarthikNarasimhan,andYuanCao.2022. React: Synergizingreasoningandactinginlanguagemodels. arXiv Tofurtherdiscussthegeneralizabilityofourapproach
preprintarXiv:2210.03629.
withnewLLMmodelsandonnewbenchmarkdatasets,
we consider two additional experiments on logical/-
MichihiroYasunaga,XinyunChen,YujiaLi,PanupongPasupat,JureLeskovec,PercyLiang,EdHChi,andDenny factual reasoning tasks on a randomly sampled 100
Zhou.2023. Largelanguagemodelsasanalogicalreason- examples from (i) LogiQA and DROP dataset using
ers. arXivpreprintarXiv:2310.01714.
Gemini-ProasbackbonefoundationmodelinTable12
(ii)ReCLORdataset(Yuetal.,2020)usingChatGPT
MichihiroYasunaga,XinyunChen,YujiaLi,PanupongPasupat,JureLeskovec,PercyLiang,EdH.Chi,andDenny asbackboneLLMinTable13.

<!-- Page 13 -->

Question: Which of the following can be the order of recording these 7 records from 1 to 7?
context: A producer is recording 7 albums one after another? F, G, H, J, K, L and M, but it is not necessary to record in this order. When
arranging the sequence of recording these 7 albums, the following conditions must be met? (l) F must be ranked second. (2) J cannot be
ranked seventh. (3) G can neither be directly in front of H nor immediately after H. (4) H must be somewhere in front of L. (5) L must be
somewhere before M
options': ['F, K, G, L, H, J, M.', 'G, F, H, K, L, J, M.', 'G, F, H, K, L, M, J.', 'K, F, G, H, J, L, M.’]

### Answer: 1

cot ans: {
"answer": 0,
"step_by_step_reasoning": [
"Step 1: F must be ranked second. This eliminates option 2 and 3 as they have F in the wrong position.",
"Step 2: J cannot be ranked seventh. This eliminates option 3.",
"Step 3: G can neither be directly in front of H nor immediately after H. This eliminates option 4 as G is immediately afterH.",
"Step 4: H must be somewhere in front of L. Option 1 satisfies this condition.",
"Step 5: L must be somewhere before M. Option 1 satisfies this condition.",
"Conclusion: Option 0 (F, K, G, L, H, J, M) is the correct order of recording the albums."
]
}
e2g: {
"answer": 1,
"step_by_step_reasoning_with_evidence_and_explanation": [
"Step 1: F must be ranked second. We can eliminate option 3 because F is not in the second position.",
"Step 2: J cannot be ranked seventh. We can eliminate option 2 because J is in the seventh position.",
"Step 3: G can neither be directly in front of H nor immediately after H. We can eliminate option 4 because G is immediatelyafter H.",
"Step 4: H must be somewhere in front of L. Option 1 meets this condition.",
"Step 5: L must be somewhere before M. Option 1 meets this condition.",
"Based on the given conditions, option 1 ('G, F, H, K, L, J, M.') is the correct order of recording the 7 albums."
]
}
Figure 5: Example-1 w/ different prompting for LogiQA
benchmarks

### A.2 Self-Reflection: Why COE Works?


### Alongwithstatisticalmotivation,tofurtherunderstand

why it works, we consider the self-reflection (Shinn
etal.,2023)approach–deliberatelyaskingtwodifferent

### SoTALLMs(ChaTGPTandGeminiPro)theinternal

advantagesofourdesignedinstructionoverCoT.Belowwesummarizethem.

## LogicalReasoning:promotesmorestructuredandlogical

thoughtprocess,reducingunsupportedstatements.

## FactualBasis: Explicitlyaskingtofocusonjustifyingits

answerbyprovidingevidence&explanationencouragesthe
LLMtogrounditsreasoninginthecontextandrelevantfacts,
makingitlesslikelytoresorttoimaginaryorunsupported
claims.

## ReducedSpeculation:Promptingforevidenceencourages

torelyonwhatisknownorcanbereasonablyinferredfrom
existinginformation.

## Accountability:Whenpromptedtoprovideevidence,modelsareheldaccountablefortheaccuracyandreliabilityof

theirresponses.
A.3 QualitativeExamples

<!-- Page 14 -->

context: July 16, 2013, Snowden, the whistleblower of the US "Prism Gate" incident, formally submitted an application for asylum to
Russia. The United States has been hunting for Snowden. If Russia accepts Snowden\'s application, it will surely lead to the
deterioration of Russia-US relations. However, there are high voices in Russia and other countries in the world that Snowden is a
defender of the rights of the people of the world. If he refuses his application, Russia will suffer moral and national
dignity.
Q: If the above statement is true, which of the following statements must be true?

### Gold answer: 3

Options : ['Russia does not want the Snowden incident to harm Russia-US relations.', 'Russia will not give Snowden to the United
States, but may send him to a third country.', "If Snowden's asylum application is accepted, Russia will not be compromised morally or
nationally.", 'If Russia does not want to worsen relations between Russia and the United States, it will suffer morally and national
dignity.’],
cot ans: {
"answer": 0,
"step_by_step_reasoning": [
"The context states that if Russia accepts Snowden's application, it will lead to the deterioration of Russia-US relations.",
"The context also mentions that if Russia refuses his application, it will suffer moral and national dignity.",
"Option 0 states that Russia does not want the Snowden incident to harm Russia-US relations, which aligns with the context.",
"Option 1 is not supported by the context.",
"Option 2 is not supported by the context.",
"Option 3 is partially true but does not fully capture the situation described in the context.",
"Therefore, the best answer is option 0."
]
}

## E2G: {

"answer": 3,
"step_by_step_reasoning_with_evidence_and_explanation": [
"Step 1: Identify the key points in the context. The context states that if Russia accepts Snowden's application, it will lead to the
deterioration of Russia-US relations
. If Russia refuses his application, it will suffer moral and national dignity.",
"Step 2: Evaluate each option based on the context.",
"Option 0: 'Russia does not want the Snowden incident to harm Russia-US relations.' - This statement is true, but it does not
necessarily follow from the context that it
must be true.",
"Option 1: 'Russia will not give Snowden to the United States, but may send him to a third country.' - This statement is a possible
outcome, but it is not mentioned in th
e context and therefore cannot be considered as a must-be-true statement.",
"Option 2: \"If Snowden's asylum application is accepted, Russia will not be compromised morally or nationally.\" - This statement is
not true, as the context states that
if Russia accepts Snowden's application, it will lead to the deterioration of Russia-US relations.",
"Option 3: 'If Russia does not want to worsen relations between Russia and the United States, it will suffer morally and national
dignity.' - This statement is true and f
ollows directly from the context, as it states that if Russia refuses Snowden's application, it will suffer moral and national dignity.",
"Step 3: Select the index of the option that must be true based on the context. In this case, the correct answer is option 3."
]
}
Figure6: Example-2w/differentpromptingforLogiQAbenchmarks

<!-- Page 15 -->


### HotpotQA

Q1: Are both DafengDistrict and Dazhoulocated in the same province? A: No
(CoT) Step by step reasoning: DafengDistrict and Dazhouare both located in the same province, which is Sichuan province. False information is given in the context that
Dafengand Dazhouare located indifferent provinces. (CoT) Output: Yes.
(E2G) Evidence & explanation: DafengDistrict and Dazhouare not located in the same province. DafengDistrict is in Jiangsu province while Dazhouis in Sichuan province.
(E2G) Output: No.
Q2: This Celtic ruler who was born in AD 43 ruled southeastern Britain prior to conquest by which empire? A: Roman
(CoT) Step by step reasoning: The Celtic ruler who was born in AD 43 ruled southeastern Britain prior to conquest by the Catuvellaunitribe, as mentioned in the context.
(CoT) Output: Catuvellauni
(E2G) Evidence & explanation: The context mentions that the Celtic ruler ruled southeastern Britain prior to conquest by the Roman Empire, so the answer isRoman.
(E2G) Output: Roman

## Drop

Q1: What ancestries were self-identified by fewer than 7% of the population?
A: ["English", "Polish", "French", "English", "Polish", "French"]
(CoT) Step by step reasoning: The context states that the top ancestries self-identified by people on the census are talian(13.6%), Guyanese (12.3%), Irish (12.1%),
Puerto Rican (10.1%), German (8.7%), English (6.0%), Polish (5.4%), French (4.4%). Therefore, the ancestries that were self-identified by fewer than 7% of the
population are Race (United States Census), two or more races, Asian (U.S. Census), Native American (U.S.Census), and Pacific Islander (U.S. Census).
(CoT) Output:Asian (U.S. Census), Native American (U.S.Census), and Pacific Islander (U.S. Census).
E2G) Evidence & explanation: The context states that the top ancestries self-identified by people on the census are Italian (13.6%), Guyanese (12.3%), Irish (12.1%),
Puerto Rican (10.1%), German (8.7%), English (6.0%), Polish (5.4%), French (4.4%). (E2G) Output: English, Polish, French
Q2:How many years was it in between when Ava ceded to Mohnyin all northern Avan territory down to present-day Shweboand the confederation wiping out Ava's
defencesin Shwebo? A: [17, 20]
(CoT) Step by step reasoning: n 1507, Ava ceded to Mohnyinall northern Avan territory down to present-day Shwebo. heconfederation wiped out Ava's defencesin

### Shweboin 1524. 1524-1507=7 (CoT) Output: 7

(E2G) Evidence & explanation: In 1507, Ava ceded to Mohnyinall northern Avan territory down to present-day Shweboin the vain hope that the raids would stop. It
did not. The confederation wiped out Ava's defencesin Shweboin 1524. (E2G) Output: 17

### WoW

Q: I am a retired computer programmer. I enjoyed my life as a person who creates computer software.\nThatsounds interesting, what kind of software did you create?\nI
create all sort of software as long aslong it is an executable code consisting of machine language instructions\nThatsounds complicated. How long did it take you to learn
to do that?
A: It depends on how fast you can learn the languages such as COBOL, C, C++, C#, Java, Lisp, Python, etc
(CoT) Step by step reasoning: The context provided discusses various topics such as game programming, software maintenance, and computer-aided maintenance. The
user's claim does not relate to any of these topics. However, it is interesting to know that the user enjoyed creating all sortsof software as a retired computer programmer.
(CoT) Output: I am sorry, but your claim does not relate to the context provided. However, it is interesting to know that you enjoyed creatingall sorts of software as a
retired computer programmer.
(E2G) Evidence & explanation: Based on the context, it is mentioned that software development takes weeks or months to complete, but it depends on the complexity of
the software. Some complex software may require more than a year of work, while others are never considered 'complete' but rather are continuously improved as long as
they stay in use. Therefore, the time it takes to learn to create software may vary depending on the complexity of the software and the individual's learning ability.
(E2G) Output: Learning to create software can take varying amounts of time depending on the complexity of the software and the individual'slearning ability.

### WoW

Q: Target always felt like the slightly classier walmart.
A:They have certainly always seemed to have a better reputation, considering all the protest from small-town advocates, labor unions, and the like.
(CoT) Step by step reasoning: Based on the context, Target is known for offering more upscale, trend-forward merchandise at lower costs, which differentiates it from its
competitors like Walmart. This concept attracts younger customers than Walmart, and the median Target shopper is 40, the youngest of all major discount retailers that
Target competes directly against. Additionally, the median household income of Target's customer base is roughly $64,000. It is also worth noting that roughly 76% of
Target customers are female. Lastly, Target has acquired the San Francisco-based jeweler Shreve & Co., which it merged with previously acquired J.B. Hudson & Son to
become Dayton Jewelers.
(CoT) Output: Target is known for offering more upscale, trend-forward merchandise at lower costs, which attracts younger customers than Walmart. The median Target
shopper is 40, the youngest of all major discount retailers that Target competes directly against. The median household income of Target's customer base is roughly
$64,000. Roughly 76% of Target customers are female, and more than 43% have acquired the San Francisco-based jeweler Shreve & Co., which it merged with previously
acquired J.B. Hudson & Son to become Dayton Jewelers.
(E2G) Evidence & explanation: As mentioned in the context, Target has intended to differentiate its stores from its competitors by offering what it believes is more upscale,
trend-forward merchandise at lower costs, rather than the traditional concept of focusing on low-priced goods. This has resultedin Target stores attracting younger
customers than Walmart, among other competitors. Additionally, the median household income of Target's customer base is roughly $64,000, which is higher than
Walmart's customer base. While Walmart is a discount department store that carries general merchandise and limited groceries,Target is often considered a slightly
classier version of Walmart due to its focus on more upscale merchandise and attracting a slightly more affluent customer base.
(E2G) Output: Yes, Target is often considered a slightly classier version of Walmart.

## Fever

Q: There is not a computer game that goes by the name of Firefox. A:SUPPORTS
(CoT) Step by step reasoning: The context states that Firefox is a web browser. The context does not mention anything about a computer game that goes by the
name of Firefox. (CoT) output: REFUTES. (E2G) Evidence & explanation: The context states that Firefox is a web browser, not a computer game. (E2G) Output:

## Supports

Q: There exists a punk band called The Times.

### True answer and e2g answer: REFUTES

(CoT) Step by step reasoning: The first context states that The Times are a British indie band. Therefore, the claim is supported.(CoT) output: SUPPORTS
(E2G) Evidence & explanation: The first context states that The Times are a British indie band. (E2G) Output: REFUTES
Q: The English Wikipedia is definitely notan edition of a free online almanac.

### True answer and e2g answer: SUPPORTS

(CoT) Step by step reasoning: English Wikipedia is not an edition of a free online almanac. The English Wikipedia is a free encyclopedia. An almanac is a reference
book that contains information about the year, such as weather forecasts, astronomical events, and sports schedules. The EnglishWikipedia does not contain
information about the year, such as weather forecasts, astronomical events, and sports schedules.(CoT) output: REFUTES
(E2G) Evidence & explanation: The context states that the English Wikipedia is not an edition of a free online almanac. This supports the claim that the English
Wikipedia is definitely not an edition of a free online almanac. (E2G) Output: SUPPORTS
Figure7: ExampleModelI/O(E2GvsCoT)

<!-- Page 16 -->


## Nq

Q: when does not going out series 9 start?A: ['8 March 2018']
(CoT) Step by step reasoning:The eighth series of 'Not Going Out' began airing on 13 January 2017 and ended on 3 March 2017. Therefore, the ninth series did
not start before 8 January 2017 (CoT) output: 8 January 2017 (E2G) Evidence & explanation: Series 9 of 'Not Going Out' began on 8 March 2018.(E2G) Output: 8

### March 2018


### Q: when did honolulubecome the capital of Hawaii?A:['1845’]

(CoT) Step by step reasoning:In 1850, Kamehameha III declared Honolulu to be the official capital of the Kingdom of Hawaiʻi. (CoT) output: 1850 (E2G) Evidence
& explanation: In 1845, Kamehameha III moved the permanent capital of the Hawaiian Kingdom from Lahaina on Maui to Honolulu. (E2G) Output: 1845

## Tqa

Q: In which Formula One team did Damon Hill replace Nigel Mansell? A: ['Williams (disambiguation)', 'Williams (company)', 'Williams']
(CoT) Step by step reasoning:"Damon Hill replaced Alain Prost in Williams team in 1994. In the previous season, Nigel Mansell was the driver for Williams.So,
Damon Hill replaced Nigel Mansell in Williams team."
(CoT) output:"Nigel Mansell
(E2G) Evidence & explanation: Damon Hill replaced Nigel Mansell in the Williams team." ", (E2G) output: Williams",
Q: Before breaking up, how was the Union of Soviet Socialist Rebublicsabbreviated in Russian, using the Russian Cyrillic alphabet? A: ['C C C P', 'The C. C. C. P.',
'The C–C–C–P', 'U.-S.-S.-R.', 'СССР', 'The U.–S.–S.–R.', 'Советской Социалистической Республикаослэн Союззы', 'Совет, Ушем', 'The Soviet–Union', 'The Soviet-

### Union’, ]

(CoT) Step by step reasoning: The abbreviation for the Russian Soviet Federative Socialist Republic (Russian SFSR) was commonly used as RSFSR. This abbreviation
was used until the Soviet Union officially ceased to exist on December 26, 1991. During 1992, it was allowed to use the old nameof the RSFSR for official business
(forms, seals and stamps).
(CoT) output:RSFSR (E2G) Evidence & explanation: The abbreviation for the Union of Soviet Socialist Republics (USSR) in Russian Cyrillic alphabet was 'CCCP’.
(E2G) output: CCCP

### Negative Results NQ

Q: who has the most trophies in the premier league? (Gen knowledge)

### A: ['Manchester United]

(CoT) Step by step reasoning:Manchester United has won more trophies than any other club in English football, with a record 20 League titles, 12 FA Cups, 5

### League Cups and a

(CoT) output: 'Manchester United (E2G) Evidence & explanation: Former Blackburn Rovers and Newcastle United striker Alan Shearer holds the record for most
Premier League goals with 260.. (E2G) Output: Alan Shearer

### Negative Results HotpotQA

Q: who is younger Keith Bostic or Jerry Glanville ? (Low conf. and hallucinate)

### A: [Keith Bostic]

(CoT) Step by step reasoning:We do not have any information about the age of Jerry Glanville or Keith Bostic in the given context except for their
birth years. Therefore, we cannot determine who is younger based on the given context.
(CoT) output: Keith Bostic (E2G) Evidence & explanation: The context does not provide information about who is younger between Keith Bostic
and Jerry Glanville. (E2G) Output: Unknown
Q: Which Australian city founded in 1838 contains a boarding school opened by a Prime Minister of Australia and named after a school in London of the same name.

### A: [Marion, South Australia]

(CoT) Step by step reasoning:The only city mentioned in the context that can fit the query is Marion.
(CoT) output: Marion (E2G) Evidence & explanation: The Australian city founded in 1838 that contains a boarding school opened by a Prime Minister of Australia and
named after a school in London of the same name is Melbourne. The boarding school is called Melbourne Grammar School and was opened by Prime Minister James H.
Scullin in 1930. It was named after the prestigious school in London, Westminster School. E2G) Output: Melbourne

### Negative Results FEVER

Q: Brian De Palma is a writer. (Commonsense)

## A: ['Supports']

(CoT) Step by step reasoning:The context states that Brian De Palma is a director. The context also states that Brian De Palma is a graduate student in their
theater department. The context also states that Brian De Palma is a composer. Therefore, the claim that Brian De Palma is a writer is supported by the
context.'(CoT) output: SUPPORTS (E2G) Evidence & explanation: The context does not mention that Brian De Palma is a writer. (E2G) Output: REFUTES

### Negative Results DROP

Q: How many percent combined did the smallest three racial groups have? (Arithmetic)

## A: 3.45

(CoT) Step by step reasoning:the smallest three racial groups are Asian, Native American, and Pacific Islander.', 'The percentage of Asian people in the cityis
2.62%.', 'The percentage of Native American people in the city is 0.69%.', 'The percentage of Pacific Islander people in the city is 0.14%.', 'Adding these three
percentages together, we get 3.45%.CoT) output: 3.45 (E2G) Evidence & explanation: The smallest three racial groups are Asian, Native American, and Pacific
Islander. The percentage of people in these groups combined is 3.55%.(E2G) Output: 3.55%

### Q: How many points did the Ravens have at the half? A: 17

(CoT) Step by step reasoning:The game was tied 3-3 with 4:32 remaining in the first half. Quarterback Joe Flacco struck quickly, however, completing touchdown
passes of 65 yards and 10 yards, to Todd Heap and Derrick Mason respectively, just before half time.', 'So the Ravens had 3 +7 + 7 = 17 points at the half.
CoT) output: 3.17 (E2G) Evidence & explanation: The Ravens scored two touchdowns just before half time, giving them 10 points.(E2G) Output: 10
Figure8: ExampleModelI/O(correctandincorrectoutcome)

## Tables

**Table (Page 1):**

|  |  | The context states that the city suffered |
|---|---|---|
| wars against the | Almoravid | and the Almohad Empires from 1085 |
| until the Battle of | Las Navas | de Tolosa in 1212. Therefore the |


**Table (Page 1):**

| Walmart |
|---|
| is the largest private employer |


**Table (Page 2):**

| Manchester United won the Double of Premier League and FA |
|---|
| Cup in the 1995-1996 season. It also mentions that David |
| Beckham scored a goal in the 1996 FA Charity Shield match |
| played by Manchester United. |


**Table (Page 2):**

|  | 'Instead, he had drafted in |
|---|---|
| young players like Nicky Butt, David Beckham, Paul Scholes and |  |
| the Neville brothers, Gary and Phil.' The 'he' in this sentence |  |
| refers to Alex Ferguson, who was the manager of Manchester |  |
| United from 1986 to 2013 |  |


**Table (Page 3):**

| CoE-Short |
|---|
| # Objective Instruction from Section 3.1 # Generate the answer with evidence and explanation. |


**Table (Page 4):**

| \|Context\| | Multi- | Context- | Cost- | E-step |  | G-step |  |
|---|---|---|---|---|---|---|---|
| >200 | Query | Aware | Minimize | Prompt | Context | Prompt | Context |
| ✗ | ✗ | ✗ | ✗ | CoE-Long | - | - | - |
| ✗ | ✗ | ✗ | ✓ | CoE-Short | - | - | - |
| ✗ | ✗ | ✓ | ✗ | CoE-Long | OC | - | - |
| ✗ | ✗ | ✓ | ✓ | CoE-Short | OC | - | - |
| ✗ | ✓ | ✗ | ✗ | CoE-Long | - | - | - |
| ✗ | ✓ | ✗ | ✓ | CoE-Short | - | - | - |
| ✗ | ✓ | ✓ | ✗ | CoE-Long | OC | CoE-Long | E+OC |
| ✗ | ✓ | ✓ | ✓ | CoE-Short | OC | CoE-Short | E+OC |
| ✓ | ✗ | ✓ | ✗ | CoE-Long | OC | CoE-Long | E |
| ✓ | ✗ | ✓ | ✓ | CoE-Short | OC | CoE-Short | E |
| ✓ | ✓ | ✓ | ✗ | CoE-Long | OC | CoE-Long | E+OC |
| ✓ | ✓ | ✓ | ✓ | CoE-Short | OC | CoE-Short | E+OC |


**Table (Page 4):**

| CoE-Long |
|---|
| # Objective Instruction from Section 3.1 # Think step-by-step and generate the answer with evidence and explanation. |


**Table (Page 5):**

| Size | Reasoning | ∣Context∣ | Task |
|---|---|---|---|
| 651 500 | MRC | 77 196 | LogicalReasoning ArithmeticReasoning |
| CG P 7.41K /1.5K | Distarctor | 1106 | Multi-hopQA |
| 500 1.5K 500 300 CG P 10.1K /.1K | RAG | 650-675 | Open-domainQA |
|  |  |  | Know. GroundedDialougeGen. LongFormQA |
|  |  |  | FactVerification |


**Table (Page 5):**

| CoT CoT-SC COE-LONG | 35.0 36.3 36.4 |
|---|---|
| - | 45.8 |


**Table (Page 6):**

| CoT COE-LONG | - 79.6 |
|---|---|
|  | - |


**Table (Page 6):**

| CoT E2G | 44.49 46.76 | 55.76 57.90 |
|---|---|---|
| - | 72.71 | 85.01 |


**Table (Page 7):**

| DafengDistrictisinJiangsuprovince |
|---|
| No |


**Table (Page 7):**

| CoT E2G | 28.4 31.2 | 36.6. 39.5 | 46.9 46.7 | 51.9 52.1 | 12.2 12.4 |
|---|---|---|---|---|---|
|  |  | 61.8 | - | 71.1 | 68.3 |


**Table (Page 7):**

|  |  | 53.02 |  | 53.25 |
|---|---|---|---|---|
|  |  |  |  |  |
| 51.75 |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |


**Table (Page 7):**

| 42.8 |
|---|
|  |


**Table (Page 7):**

| 43.2 |
|---|
|  |


**Table (Page 7):**

|  |
|---|
| 41.6 |


**Table (Page 8):**

| ItdependsonhowfastyoucanlearnthelanguagessuchasCOBOL,C,C++,C#, |
|---|
| Java,Lisp,Python,etc |


**Table (Page 8):**

| Learningtocreatesoftwarecantakevaryingamountsoftimedependingonthe |
|---|
| complexityofthesoftwareandtheindividual’slearningability. |


**Table (Page 15):**

|  |
|---|
| HotpotQA |


**Table (Page 15):**

|  |
|---|
| DROP |


**Table (Page 15):**

|  |
|---|
| WoW |


**Table (Page 16):**

|  |
|---|
| NQ |


**Table (Page 16):**

|  |
|---|
| TQA |
