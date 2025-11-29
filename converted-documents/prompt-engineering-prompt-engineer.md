---
title: "Prompt Engineering Prompt Engineer"
original_file: "./Prompt_Engineering_Prompt_Engineer.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["prompt-engineering", "llm", "rag", "chain-of-thought", "react"]
keywords: ["prompt", "let", "step", "apo", "page", "task", "table", "reasoning", "model", "text"]
summary: "<!-- Page 1 -->


### Prompt Engineering a Prompt Engineer

QinyuanYe1† MaxamedAxmed2 ReidPryzant2 FereshteKhani2
1UniversityofSouthernCalifornia 2Microsoft
qinyuany@usc.edu fkhani@microsoft.com

### Abstract

Inspect a prompt and a batch of failure examples
when this prompt is used. Prompt engineering is a challenging yet cru-
Prompt: Let’s think step by step. cial task for optimizing the performance of

### Example 1: George had 28 socks …

large language models on customized tasks."
related_documents: []
---

# Prompt Engineering Prompt Engineer

<!-- Page 1 -->


### Prompt Engineering a Prompt Engineer

QinyuanYe1† MaxamedAxmed2 ReidPryzant2 FereshteKhani2
1UniversityofSouthernCalifornia 2Microsoft
qinyuany@usc.edu fkhani@microsoft.com

### Abstract

Inspect a prompt and a batch of failure examples
when this prompt is used. Then provide feedback.
Prompt engineering is a challenging yet cru-
Prompt: Let’s think step by step.
cial task for optimizing the performance of

### Example 1: George had 28 socks …

large language models on customized tasks. Example 2: Judy teaches 5 dance classes …

### Itrequirescomplexreasoningtoexaminethe

model’s errors, hypothesize what is missing The prompt should be edited to guide the model to
perform subtraction.
ormisleadinginthecurrentprompt,andcommunicate the task with clarity. While recent Propose a new prompt.
worksindicatethatlargelanguagemodelscan
bemeta-promptedtoperformautomaticprompt Let’s solve this problem step by step. Remember to add
engineering, we argue that their potential is or subtract as needed.
limited due to insufficient guidance for complex reasoning in the meta-prompt. We fill Figure1: LLM-poweredautomaticpromptengineering
thisgapbyinfusingintothemeta-promptthree methods typically use a meta-prompt that guides an
key components: detailed descriptions, con- LLMtoinspectthe currentprompt,provide feedback
textspecification,andastep-by-stepreasoning (sometimesreferedtoastextual“gradients”)andthen
template. The resulting method, named PE2, generatean updatedprompt. Inthispaper,wedesign
exhibitsremarkableversatilityacrossdiverse andinvestigate meta-prompt variantstoguideLLMsto
language tasks. It finds prompts that outper- performautomaticpromptengineeringmoreeffectively.
form“let’sthinkstepbystep”by6.3%onMultiArithand3.1%onGSM8K,andoutperforms
competitivebaselinesoncounterfactualtasks
tunisticallyratherthansystematically(Zamfirescuby6.9%. Further,weshowthatPE2canmake

### Pereiraetal.,2023). Addingtothischallenge,once

targetedandhighlyspecificpromptedits,recahigh-qualitypromptisfoundanddeployedinto
tifyerroneousprompts,andinducemulti-step
plansforcomplextasks. production,unforeseenedgecasescanarise,necessitatingmoreroundsofmanualefforts. Allthese
1 Introduction challengesgiverisetoanemergingresearchfieldof
automaticpromptengineering. Withinthisfield,a

### Largelanguagemodels(LLMs)arepowerfultools

notablelineofmethodsinvolvesleveragingthecaformanynaturallanguageprocessingtasks,when
pabilitiesofLLMsthemselves(Zhouetal.,2023b;
providedwiththerightprompts.1 However,LLMs

### Pryzantetal.,2023). Thisentailsmeta-prompting

are also notoriously sensitive to prompt design

### LLMswithinstructionssuchas“inspectthecurrent

(Jiang et al., 2020; Zhao et al., 2021; Reynolds
promptandabatchofexamples,providefeedback,
andMcDonell,2021;Luetal.,2022),andfinding
thenproposeanewprompt.” (SeeFigure1)
therightpromptsoftenrequiresextensivemanual
Whilethesemethodsachieveimpressiveperforeffortsreferredtoas“promptengineering.” Nonmance,asubsequentquestionarises: Whatmakes

### AIexperts,inparticular,maystruggletoeffectively

a good meta-prompt for automatic prompt engicommunicatethetaskofinteresttoLLMs,resultneering? Toanswerthisquestion,weconnecttwo
inginpromptengineeringbeingperformedopporkey observations: (1) Prompt engineering, at its
†WorkdonewhileinterningatMicrosoft.
core, is a language generation task that requires
1Inthispaper,wefocusontextualpromptsoftaskdescripcomplexreasoning: itinvolvescloselyexamining
tion(e.g.,“TranslateEnglishtoFrench”)orinstruction(e.g.,
“Let’sthinkstepbystep”). themodel’serrors,hypothesizingwhatismissing
1
4202
luJ
3
]LC.sc[
3v16650.1132:viXra

<!-- Page 2 -->

100
75
50
25
MultiArith GSM8K
ycaruccA
+6.3 100
75
+3.1
50
25
Instruction Induction BIG-Bench Hard Counterfactual Eval
(14 Tasks) (27 Tasks) (12 Tasks)
ycaruccA
)egarevA(

### Initialization APO

Iterative APE PE2 (This Work)
+7.4
+5.9
+15.9
Production
Prompt
erocS

## 1F

+8.0
Figure2: ResultsOverview. OurmethodPE2consistentlybringsimprovementsoverthepromptinitialization
(markedwithorangetext). ItmatchesoroutperformspromptoptimizationbaselinesIterativeAPE(Zhouetal.,
2023b)andAPO(Pryzantetal.,2023)acrossawiderangeoflanguagetasks,withmostsignificantperformance
gainobservedonConterfactualEval(Wuetal.,2024). SeedetailedperformancebreakdowninFig.10-13.
ormisleadinginthecurrentprompt,andcommuni- examiningthepromptedithistory(§5.3),wefind
catingthetaskmoreclearlytoLLMs. (2)Complex that PE2 consistently offers meaningful prompt
reasoningcapabilitiesinLLMscanbeelicitedby edits(Table6). Itisabletoamenderroneousorinpromptingthemodelto“thinkstepbystep”(Wei completepromptsandenrichthepromptswithaddietal.,2022a;Kojimaetal.,2022)andcanbefur- tionaldetails,whichleadstoimprovedfinalperfortherimprovedbyinstructingthemtoreflectontheir mance. Itisalsoabletodevisemulti-stepplansfor
outputs(Madaanetal.,2023;Chenetal.,2024). complextasks. Forexample,inthetaskofmovie
Bridging these two observations, in this work, recommendation,PE2makestheplanto“consider
we prompt engineer a prompt engineer—we aim factorssuchasgenre,plotandstyle”intheprompt.
to construct a meta-prompt that guide LLMs to Interestingly,whenuninformedaboutperforming
performautomaticpromptengineeringmoreeffec- additioninbase-8,PE2formulatespartially-correct
tively. We argue that prior works do not provide arithmeticrulesfromexamplesbyitself: “Ifboth
sufficientguidanceinthemeta-prompt,therebylim- numbersarelessthan50,add2tothesum. Ifeither
itingthepotentialofLLMsforautomaticprompt numberis50orgreater,add22tothesum.2” This
engineering. To address this, we introduce new demonstrates PE2’s remarkable ability to reason
meta-promptcomponentssuchasdetailedtwo-step and adapt in non-standard situations, while also
taskdescriptions,contextspecification,andastep- raises concerns of “shortcut learning” in prompt
by-stepreasoningtemplate,tobetterequipLLMs optimization.
throughouttheprocess(§3;Fig.3).
2 Background

### The resulting method, named PE2, achieves

strongempiricalperformance(§5.1). Whenusing
In this section, we provide a formal formulation
text-davinci-003asthetaskmodel,theprompts
ofthepromptengineeringproblem(§2.1),anddeproduced by PE2 surpass the zero-shot chain-ofscribe a general framework of automatic prompt
thoughtprompt“let’sthinkstepbystep"(Kojima
engineeringusingLLMsandmeta-prompts(§2.2).
etal.,2022)by6.3%onMultiArithand3.1%on
Building on this foundation, we introduce new
GSM8K.Moreover,PE2matchesoroutperforms
meta-promptcomponentsusedinPE2in§3.
twoautomaticpromptengineeringbaselines,IterativeAPE(Zhouetal.,2023b)andAPO(Pryzant
2.1 PromptEngineering
et al., 2023) in multiple settings (Fig. 2). PE2 is

### Thegoalofpromptengineeringistofindthetextual

most effective on counterfactual tasks (Wu et al.,
promptp∗ thatachievesthebestperformanceona
2024),wheretheautomaticpromptengineerisangivendatasetD whenusingagivenLLMM
ticipated to reason about non-standard situations task
asthetaskmodel. Morespecifically,weassumeall
(e.g.,doadditioninbase-8insteadofbase-10)and
datasets can be formatted as textual input-output
explain such situation to the task model through
pairs, i.e., D = {(x,y)}. Wearegivenatraining
the prompt. Beyond academic datasets, we show
setD foroptimizingtheprompt,D forvalthatPE2canimproveanexpert-writtenproduction train dev
idation,andD forfinalevaluation. Following
promptconsistingofover5,000tokens,resulting test
the notations in Zhou et al. (2023b), the prompt
inan8.0%increaseinF1score.

### Wefurtherprovideadetailedanalysisonthebe-

2Both the base-8 addition rules and the model-induced
haviors,advantages,andlimitationsofPE2. Upon rulesholdtrueforexampleslike75+7=104and5+6=13.
2

<!-- Page 3 -->

engineeringproblemcanbedescribedas: Iter.APE APO PE2
InspectModelFailures (cid:37) (cid:33) (cid:33)
(cid:88)
p∗ = argmax f(M (x;p),y) (1) (a)TaskDescription
task
p -Length Short Short Long
(x,y)∈D
dev -#Steps One-step Two-step Two-step
-Position Beginning On-the-fly Both
whereM task (x;p)istheoutputgeneratedbythe (b)ContextSpecification (cid:37) (cid:37) (cid:33)
task model when conditioning on the prompt p, (c)Step-by-stepTemplate (cid:37) (cid:37) (cid:33)
and f is a per-example evaluation function. For

### Table1:ComparisonofMeta-promptComponentsUsed

example, if the evaluation metric is exact match,
inBaselineMethodsandPE2.
f(M (x;p),y) = 1[M (x;p) = y].
task task
2.2 AutomaticPromptEngineeringwith Constructing a better meta-prompt pmeta to im-

### LLMs provethequalityoftheproposedpromptp(t+1) is

Toalleviatetheintensiveeffortsofmanualprompt the main focus of this study. We will describe in
engineering,recentworksexploreautomatingthis moredetailsin§3.
process by meta-prompting LLMs to paraphrase
SearchProcedure. AsLLMsaresensitivetotrivtheprompt(Zhouetal.,2023b)orrefinetheprompt
ialpromptvariations,itispossiblethatthenewly
by inspecting failure examples (Pryzant et al., proposedpromptp(t+1) under-performstheorigi-
2023). Inthefollowing,wedescribeaframework nalpromptp(t). Therefore,automaticpromptengithatencapsulatesthesepriorworksandisemployed
neeringistypicallycombinedwithaback-tracking
inourdevelopmentofPE2inlatersections. Ithas
enabledsearchprocedure. Attimestampt,wesethreeparts: promptinitialization,newpromptprolect n best-performing prompts from all prompt
posal,andthesearchprocedure.
candidates obtained in previous timestamps (i.e.,

### P(0)∪P(1)∪...∪P(t)). Foreachofthesenprompts,

Prompt Initialization. To start the prompt engineeringprocess, asetofinitialpromptsP(0) is wesamplemdifferentbatchesB ofmodelerrors,
andrunthemeta-promptinEq.2toproducemnew
needed. We consider two initialization methods:
prompts. Thisresultsinm×nnewprompts,which
(1) Manual initialization is applicable for tasks
we denote as P(t+1) collectively and are used at
that has pre-existing prompts written by humans
thenexttimestampt+1. Thesearchalgorithmis
experts. Forexample,“Let’sthinkstepbystep”is
describedmoreformallyinAlgorithm1.
effectiveonmathematicalreasoningtasksandcan
be used as the initialization for prompt optimiza-
3 PromptEngineeringaPromptEngineer
tion. In (2) Induction Initialization, we follow
Zhouetal.(2023b)byusingabatchofexamples Muchlikehowthepromptplaysanimportantrole
{(x,y)}fromD andapromptpinit(“Hereare for the end task performance, the meta-prompt
train
the input-output pairs. What is the instruction?”) pmeta introducedinEq.2playsanimportantrole
togenerateasetofinitialpromptsP(0). in the quality of newly proposed prompts, and
theoverallqualityofautomaticpromptengineer-
New Prompt Proposal. Given a set of iniing. In this work, we focus on prompt engineertial prompts, the automatic prompt engineer will ing the meta-prompt pmeta—we develop metacontinuously propose new and potentially better
prompt components that can potentially help imprompts. At timestamp t, the prompt engineer is
proveLLMs’promptengineeringquality.
given a prompt p(t) and expected to write a new
In the following, we reflect on the limitations
prompt p(t+1). Optionally, a batch of examples
of prior works and subsequently introduce three

### B = {(x,y,y′)} may be inspected in the new

meta-prompt components targeting these limitapromptproposalprocess. Herey′ = M (x;p)
task tions. We visualize these components in Fig. 3
representsoutputgeneratedbythetaskmodeland
andprovideasummaryinTable1. Wenameour
y representstheground-truthlabel. Weusepmeta
method using these three components as PE2, a
todenoteameta-promptthatisusedtoinstructthe
promptengineeredpromptengineer.
promptproposalmodelM toproposenew
proposal
prompts. Therefore, (a) Two-step Task Description. In APO
(Pryzant et al., 2023) the task of prompt engip(t+1) = M (p(t),B;pmeta) (2) neering is decomposed into two steps (Fig. 1):
proposal
3

<!-- Page 4 -->

(a) two-step task instruction (c) step-by-step reasoning template
A prompt is a text paragraph that outlines the expected actions # Instruction
and instructs the model. In our collaboration, we'll work For each example, provide reasoning according to the
together to refine a prompt. The process consists of two steps: following template
# Step 1 * Output is correct?
Examine the prompt and a batch of examples * Necessary to edit the prompt?
# Step 2 * If yes, suggestions on prompt editing?
Propose a new prompt based on your reasoning
## Example 1
Sure! I'd be happy to help you. Output is correct? No.
Reasoning: the model didn't subtract the socks he threw away.
# Current Prompt Prompt describing the task correctly? Yes.
Let’s think step by step. Necessary to edit the prompt? Yes.

### Suggestions: The prompt should be edited to guide the model

# Full Template (b) context specification to perform subtraction.
``` [More examples …]

### Question: <input>

Answer: Let’s think step by step.
Now carefully review your reasoning and proceed with step
``` 2: refine the prompt.
# Examples # Current Prompt
## Example 1 Let’s think step by step.
Input: George had 28 socks. If he threw away 4 socks …

### Output: 64 # Instructions

Reasoning: Step 1: George had 28 socks. Step 2: … * The total length should be less than 50 words
Label: 60 * Reply with the prompt. Do not include other text.
[More examples …]

### Let’s solve this problem step by step. Remember to add or

Legend Meta-Prompt Components Prompt Feedback (“Gradients”) subtract as needed.
Figure3: Anredactedexampletoillustratethemeta-promptcomponentsintroducedin§3.
In step 1, the model is expected to inspect the size, step size and momentum, we considered
currentpromptandabatch. Instep2,themodelis adding their verbalized counterparts to the metaexpectedtogenerateanimprovedprompt. promptandinvestigatetheireffects. Wealsocon-
However,inAPO,eachstepisexplainedbriefly sideredaddingapromptengineeringtutorialinthe
and on the fly. In contrast, we consider clarify- meta-prompt to help the LLM better understand
ingthestepsandexpectationsupfrontinthemeta- the task. Our observations on these components
prompt,andalsoguidingthemodelwithspecific aremixed. WereporttheseresultsinAppendixB.
stepson-the-fly.
4 ExperimentSetting
(b)ContextSpecification. Inpractice,howthe
4.1 Tasks
promptandtheinputtextareformattedtogetheris
flexible. Itmayappearbeforetheinputtexttode- Weusethefollowingfivegroupsoftaskstoevalscribethetask,e.g.,“TranslateEnglishtoFrench.” uatetheeffectivenessofPE2. Detailsoftheused
Itmayappearaftertheinputtext,e.g.,“Let’sthink datasets(e.g.,datasetsizes,train-testsplits,license)
stepbystep”toelicitreasoningcapabilities. Recog- aredeferredinAppendixD.4.
nizingthesevaryingcontexts,weexplicitlyspecify
(1) Math Reasoning. We use MultiArith (Roy
thelayoutofthepromptandtheinput.
andRoth,2015)andGSM8K(Cobbeetal.,2021),
which contain grade school math problems that
(c) Step-by-step Reasoning Template. To enrequiresmultiplestepsofarithmeticoperations.
couragethemodeltoexamineeachexampleinthe
batch B closely and reflect on the limitations in (2)InstructionInduction. InstructionInduction
thecurrentprompt,weguidethepromptproposal (Honovichetal.,2023)isabenchmarkforinferring
modelM proposal withalistofquestions. Forex- theunderlyinginstructionfromfew-shotexamples.
ample: Isthepromptcorrectlydescribingthetask? We use 14 selected tasks that cover a wide range
Isitnecessarytoedittheprompt? Ifyes,provide ofusecases,e.g.,“Formality”isataskthataimsat
actionablesuggestionsonpromptediting. rephrasingasentencetobemoreformal.
Other Meta-prompt Components We Tried. (3)BIG-benchHard. BIG-benchHard(Suzgun
Inspired by optimization concepts such as batch etal.,2023)isacollectionof23tasks(27subtasks)
4

<!-- Page 5 -->

thatarechallengingtoLLMsbuttheperformance ofLLMs(M andM )whenevaluating
proposal task
maybeimprovedwithadvancedpromptingtech- PE2againstotherpromptoptimizationmethods.
niques (Wei et al., 2022b). Some of BIG-bench

### PromptInitialization. ForMathReasoningand


### Hardtasksarecloselyrelatedtoreal-worldappli-

BIG-bench Hard tasks, we use “Let’s think step
cations(e.g.,movierecommendation).
bystep.” (Kojimaetal.,2022)astheinitialization
(4) Counterfactual Evaluation. We use the prompt, which can elicit multi-step reasoning in
arithmetic,chess,andsyntaxtasksandtheircoun- LLMs to perform these tasks. For Instruction InterfactualvariantsintroducedinWuetal.(2024). duction,wefollowthesettinginpriorworks(Zhou
Forarithmetic,theoriginaltaskisbase-10addition, etal.,2023b)anduseinductioninitialization. For
andthecounterfactualtasksarebase-8/9/11/16ad- CounterfactualEval,weexperimentwithboth. For
dition. Forchess,thestartingpositionsforknights theproductiontask,weusethepromptwrittenby
andbishopsareswappedinthecounterfactualtask. anexperiencedengineer.
WeusethissetoftaskstoinvestigatewhetherPE2

### SearchBudget. Weusethesamesearchbudget

canreasonaboutnon-standardsituationsandcomfor all prompt optimization methods. For experimunicatethemtothetaskmodel.
mentsusinginductioninitialization,30promptsare
(5)ProductionPrompt. Lastly,weoptimizean generated by pinit and form the initial candidate
internalproductionpromptforahierarchical,multi- setP(0). Duetobudgetconstraints,thenumberof
label classification task. The task is to classify a optimizationstepsT issettobe3. Ateachtimesuserqueryintodomains,intentsandslots,andthen tamp, we select n = 4 best-performing prompts,
outputanesteddictionaryastheresult. Theinitial- andproposem = 4promptsfromeachofthem.
izationpromptiscarefullydesignedbyexperienced
WedeferotherexperimentdetailsinAppendixD.
engineersandhasmorethan5,000tokens.
5 ResultsandAnalysis
4.2 ComparedMethods
We compare PE2 with the following automatic 5.1 MainResults
prompt engineering methods. (a) APE (Zhou
Improved baselines with more recent LLMs.
et al., 2023b): The base version of APE is an

### In Zero-shot CoT (Kojima et al., 2022) and APE

initialization-only method and does not involve
(Zhou et al., 2023b), the results were obtained
newpromptproposalsteps. Itusesaninitialization with a earlier text-davinci-002 model. We
prompt pinit to generate multiple prompt candifirst rerun the prompts in these two works with
datesfromafewexamples,andselectthebestone text-davinci-003, an upgraded model. In TaamongthembasedonD performance. (b)Iterdev ble2,weobserveasignificantperformanceboost
ativeAPE(Zhouetal.,2023b): Afterinitialization, by using text-davinci-003, suggesting that it
pmeta instructsthemodeltoproduceaparaphrase
is more capable of solving math reasoning probof p(t) and use it as p(t+1). (c) APO (Pryzant
lemswithZero-shotCoT.Moreover,thegapsbeetal.,2023): pmeta containsshortinstructionson
tweenthetwopromptsarenarrowed(MultiArith:
inspecting the batch B, generating textual “gra-
3.3% → 1.0%,GSM8K:2.3% → 0.6%),indicatdients” (feedback), and producing a new prompt ing text-davinci-003 has a reduced sensitivity
p(t+1). Weincludethepinitandpmetausedinthese
topromptparaphrasing. Giventhis,methodsthat
baselinemethodsinAppendixF.
relyonsimpleparaphrasing,suchasIterativeAPE,
maynotimprovethefinalaccuracyaseffectively.
4.3 ExpeirmentDetails
More specific and targeted edits are necessary to
LLMs. By default, we use gpt-4 (OpenAI,
improvetheperformance.
2023) as prompt proposal model M and
proposal
use text-davinci-003 (Ouyang et al., 2022) as PE2 outperforms Iterative APE and APO on
thetaskmodelM performingtheunderlying varioustasks. PE2isabletofindapromptthat
task
task. Experiments on BIG-bench Hard are con- achieves 92.3% accuracy on MultiArith (+6.3%
ducted at a later stage, and we use gpt-4-turbo compared to Zero-shot CoT) and 64.0% on
and gpt-3.5-turbo-instruct to save costs and GSM8K(+3.1%). Additionally, wedemonstrate
demonstratethecompatibilityofourmethods. To thewideapplicablityofPE2onawiderangeoflanensurefaircomparison,wealwaysusethesameset guagetasks. InFig.2wesummarizetheresultsand
5

<!-- Page 6 -->

Task Proposal MultiArith GSM8K Method MultiArithPrompt

### Method

Model Model Test Test

### FixedPrompt

FixedPrompt,ReportedbyZhouetal.(2023b)
Zero-shotCoT Let’sthinkstepbystep.

### Zero-shotCoT TD002 - 78.7 40.7

Let’sworkthisoutinastepbystepwaytobesure

## Ape Td002 Td002 82.0 43.0 Ape

wehavetherightanswer.
FixedPrompt,Reproduced

### PromptOptimization


### Zero-shotCoT TD003 - 86.0 60.9

IterativeAPE Let’sproceedinamethodical,step-by-stepmanner.

## Ape Td003 - 87.0 61.5

Giventhescenario,performthenecessarycalcula-

### PromptOptimization


### APO tionsstepbysteptofindthefinalresult.Considerall

IterativeAPE TD003 GPT-4 88.5 62.7 partsoftheinputandthesequenceofevents.

## Apo Td003 Gpt-4 88.5 63.1

Let’ssolvethisproblembyconsideringallthedetails.

### PE2(thiswork) TD003 GPT-4 92.3 64.0 PE2

Payattentiontoeachpieceofinformation,remem-
(thiswork)
bertoaddorsubtractasneeded,andperformthe
Table2: PerformanceComparisononMathReasoning calculationsstepbystep.
Tasks. TD002/003standfortext-davinci-002/003.
SeeTable4forthefinalprompts. Table4:MultiArithpromptsfoundbycomparedprompt
optimizationmethods. Weusetext-davinci-003as
thetaskmodelandgpt-4asthepromptproposalmodel.
Method GSM8k MultiA. Date Hyper. Temp. Word

### Init. 48.1 71.5 36 52 50 4

Iter.APE 49.7 73.5 48 48 42 20

## Apo 51.0 73.5 48 72 52 16 1.00


## Pe2 50.5 74.3 56 74 62 28

0.75
TasksfromBIG-BenchHard:Date=DateUnderstanding;
0.50
Hyper.=Hyperbaton;Temp.=TemporalSequence,Word=WordSorting.
0.25

### Table 3: Results on six selected tasks when using

Mistral-7B-Instruct-v0.2(Jiangetal.,2023)asthe 0.00

### Start 1 2 3

task model and gpt-4-turbo as the prompt proposal Timestamp
model. SeeTable26forthefinalprompts.
show that PE2 outperforms Iterative APE (Zhou
et al., 2023b) and APO (Pryzant et al., 2023) in
multiplecases. Mostnotably,wheninductioninitializationisused,PE2outperformsAPOon11out
of 12 counterfactual tasks (Fig. 11), exhibiting a
6.9%averageincreaseinaccuracy. Thishighlights

### PE2’scapabilityinreasoningaboutcontradictions

and unconventional situations. We defer experimentdetailsandperformancebreakdownforthese
benchmarksinAppendixE.
PE2generatestargetedprompteditsandhighquality prompts. In Fig. 4 we plot the quality
ofpromptproposalsoverthecourseofpromptoptimization. We observe very distinct patterns for
the three prompt optimization methods: Iterative
APEisbasedonparaphrasing,sothenewlygeneratedpromptshavesmallervariance. APOmakes
drasticallylargeprompteditsandthustheperformance drops in the first step. Among the three
methods,PE2hasabetterbalancebetweenexplorationandstability. InTable4,welisttheoptimal
promptsfoundbythesemethods. BothAPOand
PE2areabletoprovideinstructionson“consideringallparts/details”. Inaddition,PE2isdesigned
toinspectthebatchclosely,enablingitmakevery
.ccA
veD
htirAitluM
Comparing Prompt Optimization Methods
Iteratvie APE APO PE2

### Best Prompt


### Figure 4: Prompt optimization dynamics of Iterative

APE,APOandPE2onMultiArith. Theviolinsrepresentthequalitydistributionsofnewlyproposedprompts
ateachoptimizationstep. PE2hasabetterbalancebetweenexplorationandstability.
specificprompteditssuchas“remembertoaddor
subtractasneeded”.
PE2 is widely applicable to various LLMs, includingopen-weightmodels. Ourpreviousexperimentsettingemploysdifferentcombinationsof
closed-sourcemodelsasthetaskmodelT and
task
thepromptproposalmodelT (§4.3). Tofurproposal
therdemonstratePE2’smodel-agnosticnature,we
introduce Mistral-7B-Instruct-v0.2, a recent
open-weight model, as the task model, and uses
gpt-4-turbo as the prompt proposal model. We
reporttheresultsinTable3andthefinaloptimized
prompts in Table 26. Consistent with our experimentswithclosed-sourcemodels,resultsinTable3
demonstratethatPE2performscompetitivelywith
orsurpassesotherautomatedpromptengineering
methods. Asrecentresearchsuggests,LLMsstill
exhibitsurprisingsensitivitytopromptdesignand
formatting(Sclaretal.,2024;Mizrahietal.,2023),
highlighting the importance of investigating why
certainpromptssucceedorfail. WehopePE2em-
6

<!-- Page 7 -->

powersresearcherstodiscovereffectiveandinef- MultiArith GSM8K

### Method

fectiveprompts,whichlayempiricalfoundations Dev Dev
forfutureexplorationintopromptsensitivitywith PE2(default) 92.0 68.0
open-weightmodels. Baselines

### IterativeAPE 89.0 66.0

5.2 AblationStudy APO 86.0 60.0

### Ablation:Meta-promptComponents

Todemonstratetheeffectivenessofthethreenew
-two-steptaskdescription 89.0 66.0
meta-prompt components introduced in PE2, we
-step-by-stepreasoningtemplate 87.0 61.0
runablationexperimentsbyremovingthesecom- -contextspecification 93.0 63.0
ponentsduringpromptoptimizationonMultiArith Ablation:SearchAlgorithmConfigurations
andGSM8K.Intheseexperiments,wemakesure -back-tracking 90.0 66.0
thatthemeta-promptstillcontainssufficientinfor- -hardnegativesampling 90.0 68.0
mationaboutthetaskofpromptengineering. From
Table5: Ablationstudyonmeta-promptcomponents.
the results in Table 5, we show that these three
componentscontributesignificantlytothefinalaccuracy. In Fig. 5, we visualize the optimization
1.0
dynamicsoftheseablationexperiments. Wefind
0.8
thattheexclusionofanyoneofthesecomponents
0.6
resultsinahighervarianceinthequalitydistribu-
0.4
tionofnewly-proposedprompts. Moreover,with-
0.2
out these components, the proposal model more Start 1 2 3

### Timestamp

frequentlysuggestslow-qualityprompts.
We also conduct an ablation study on backtracking(i.e.,attimestampt,selecttop-performing
promptsfrom∪t P(i) versusonlyP(t))andhard
i=0
negative sampling (i.e., the batch B is sampled
from the model’s errors, versus being randomly
sampledfromD ). Sincebothtechniquesshow
train
slightlypositiveeffectsonPE2’sperformance,they
areretainedinthefinalversionofPE2.
We encourage readers to refer to §B for additionalmeta-promptcomponentsthatweexplored
duringPE2’sdevelopment,suchasverbalized“momentum”, “step size”, and a tutorial on prompt
engineering. Although these elements were not
includedinthefinalversionofPE2,wedocument
themtoencouragefurtherexplorationasmorecapablelanguagemodelsemergeinthefuture.
5.3 CaseStudy
PE2 amends erroneous or incomplete instructions,anddevisesmulti-stepplansforcomplex
tasks. Tables 6 and 16 present notable prompt
editsmadebyPE2. Inthetaskoffindingrhyming
words (e.g. “car” rhymes with “bar”), induction
initializationmistakenlysuggeststhetaskisabout
changingthefirstletterofaword. PE2successfully
correctthisafteroneoptimizationstep. Inthetask
ofmovierecommendation,PE2isabletodecomposethecomplextaskintoconcretecriteria,such
asgenre,plotandactor,whendeterminingmovie
similarities. Indateunderstanding,PE2identifies
.ccA
veD
htirAitluM

### Ablation on Meta-prompt Components

default - task desc - reasoning - context

### Best Prompt

Figure5: PromptoptimizationdynamicsonMultiArith
whenremovingmeta-promptcomponents.Byremoving
onecomponent,thenewpromptshavelargervariance
intheirquality.
the crucial step of referencing information about
“today”. TheseexamplesdemonstratePE2’sability
tolearnbysummarizingkeystepsfromfailuresand
incorporatingthemintoimprovedprompts,aligningwithrecentwork(Zhangetal.,2024).
Limitationsinmeta-promptfollowingandhallucination. DespitethesuccessesmadebyPE2,we
noteseveralfactorsthat’slimitingitsperformance
whenappliedtochallengingcounterfactualtasks.
WeproviderepresentativecasesinTable7. Occasionally,PE2refusestoproposeanewpromptand
insiststhat“thepromptiscorrect,butthelabelis
incorrect,” even when we explicitly state "the labelsareabsolutelycorrect"withinthemeta-prompt.
In another example, we attempt to guide it with
hints(e.g.,suggestingadifferentnumericalbase),
butthiscanunfortunatelyleadPE2togenerateincorrect solutions (e.g., base-80) and even create
justificationsfortheseimaginedsolutions. These
observations highlight the importance of improving LLMs’ abilities to follow (meta-)instructions
accuratelyandaddressinghallucinationissues.
Discussionon“shortcutlearning.” Wefindinterestingyetconcerningprompteditsonthecoun-
7

<!-- Page 8 -->

Task t Prompt DevAcc.

### Correctwrongorincompletetaskinstructions

0 Removethefirstletterfromeachinputwordandthenreplacethatfirstletterwithasimilar 0.35
Rhymes soundingletterorgroupofletterstoformanewword.
1 Generateawordthatrhymeswiththeinputword. 0.45
Layouttailoredmulti-stepplansforcomplexproblems
0 Let’sthinkstepbystep. 0.58
1 Considerthegenre,plot,andstyleoftheinputmovies.Usingthisinformation,thinkstepby 0.74
Movie steptoidentifywhichofthefollowingoptionsismostsimilartothegivenmovies.
Recommendation 2 Consideringfactorssuchasgenre,director,actors,releaseperiod,audiencetarget,animation 0.82
style,andhumor,analyzethesimilaritiesamongthegivenmoviesandidentifythemoviefrom
theoptionsthatsharesthemostsimilarities.
0 Let’sthinkstepbystep. 0.39

### Date

2 Analyzingthegiveninformation,let’scalculatethesolution.Remembertoconsiderthecontext 0.54

### Understanding

provided,suchasreferencesto’today’orspecificdates.

### Produceshortcutsolutionsincounterfactualtasks

0 Addthetwonumbersgivenasinputtogettheoutput. 0.0
Base-8Addition 3 Addthetwonumbersprovidedintheinput.Then,adjustthissumbasedonthefollowingrule: 0.35
(InductionInit.) ifbothnumbersarelessthan50,add2tothesum.Ifeithernumberis50orgreater,add22to
thesum.Thefinalresultistheoutput.
Table6: NotableprompteditsmadebyPE2. See§5.3fordiscussion. SeeTable16foradditionalexamples.
terfactualtaskofbase-8addition. Wheninduction initialization. (2) We experiment with induction
initializationisused(i.e.,PE2isuninformedwith initialization. Inthiscase,PE2isabletodiscovera
theinformationofbase-8andmustinferitfromthe highqualitypromptfromscratchthatmatcheswith
examples),PE2isabletodeviseitsownheuristic “Let’sthinkstepbystep”onMultiArith.
that is partially correct (“... if both numbers are
EffectofTaskFormat/Difficulty. (§A.2) Weexless than 50, add 2 to the sum. If either number
perimentwithusingagenerativeformat(i.e.,generis50orgreater,add22tothesum”; seeTable6).
atingtheanswerstring)andamulti-choiceformat

### Thisheuristicholdstrueforasubsetoftestcases

(i.e.,selectingfromgivenchoicesA/B/C/D)onthe
like 75+7=104 and 5+6=13, but is ultimately not
DateUnderstandingtaskinBIG-benchHard. We
theintendedsolution.
observethatautomaticpromptengineeringmeth-
Onthepositiveside,itdemonstratesPE2’sabilodshaslimitedeffectonthemulti-choiceformat,
itytoadaptinunseenscenariosandengageinsobutbringsignificantgainsonthegenerativeformat.
phisticatedcounterfactualreasoning. However,it
isconcerningthatmodelspromptedwiththeseself-

### Do optimized prompts generalize to other

inducedshortcutsolutionsachieveatestaccuracy
LLMs? (§A.3) We evaluate prompts optiof 37% (average over 5 runs), which outperform mized for text-davinci-003 on other modmodelsexplicitlypromptedtoperformbase-8ad- els such as mpt-7b-instruct, yi-6b and
dition (test acc: 17%/28% before/after PE2 opti- mistral-7b-instruct. We do not observe conmization). Shortcutlearning(Geirhosetal.,2020)
sistent cross-model generalization trends. This
hasbeenstudiedextensivelyforgradient-basedopsuggests that, although PE2 is a model-agnostic
timization. Our experiments suggest that similar
promptoptimizationmethod(i.e., canbeapplied
failuremodesmaybepresentinautomaticprompt
tovariousM ),thefinaloptimizedpromptsare
task
optimization.
specifictotheunderlyingtaskmodel.
5.4 AdditionalAnalysis
6 RelatedWork

### Duetospacelimit, wesummarizeourotherfind-

Automatic Prompt Engineering. To alleviate
ingsbelowanddeferthedetailstoAppendixA.
the intensive trial-and-error efforts in manual
EffectofInitialization. (§A.1) (1)PE2isable promptengineering,theresearchcommunityhas
to recover from misleading or irrelevant prompt developedvariousstrategiestoautomatethisproinitializations,howeverthefinalpromptafteropti- cess with techniques such as incremental editing
mization is worse thanwhen using an instructive (Prasadetal.,2023),reinforcementlearning(Deng
8

<!-- Page 9 -->


### Task Meta-promptandReasoningSnippets


### Neglectinginstructionsinthemeta-prompt

Meta-prompt:...Notethattheground-truthlabelsare__absolutelycorrect__,buttheprompts(taskdescriptions)
maybeincorrectandneedmodification....

### Base-9Addition

Reasoning:No,itisnotnecessarytoedittheprompt.Thepromptiscorrect,butthelabelisincorrect....Theissue
seemstobewiththelabel,nottheprompt.

### Hallucination(whenhintsareprovidedinthemeta-prompt)

Hint:Thecalculationmaybeperformedinadifferentnumericalbase.
Reasoning:...Giventhis,it’spossiblethatthenumbersarebeingaddedinbase80,notbase10.Inbase80,adding
Base-8Addition 20tothesumoftwonumberswouldbeequivalenttoadding1inbase10.
NewPrompt:Theinputsaretwonumbersseparatedbya’+’.Addthesetwonumberstogetherinbase80,thenadd
1togivetheoutputinbase10.
Table7: LimitationsandfailurecasesofPE2. See§5.3fordiscussion.
etal.,2022;Zhangetal.,2022),algorithmicsearch employingLLMstogeneratehigh-qualityreason-
(Xuetal.,2022),generatingin-contextdemonstra- ingchains,followedbymodelfine-tuningonthese
tionsadaptively(Wanetal.,2023a,b),amongoth- chains,cansignificantlyimprovethemodel’sreaers. Alineofworkfocusonmeta-promptingLLMs soningcapabilities. Inthiswork,weconsidertexthemselvesforautomaticpromptengineering(Hon- tualpromptsasthe“parameters”ofLLMs,andwe
ovichetal.,2023;Zhouetal.,2023b;Pryzantetal., optimizethese“parameters”withLLMs. Thismay
2023). In our work, we discuss potential limita- becategorizedasacaseofself-improving(Goodtionsinthesemethodsandsubsequentlyintroduce man,2023). MorediscussioninAppendixC.1.
newmeta-promptcomponentsinPE2.
7 Conclusion
PromptingLLMsforComplexReasoningTasks.
RecentresearchworkssuggestthatLLMscanper- In this paper, we introduced three meta-prompt
formcomplexreasoningtasks,e.g.,grade-school components that lead to improved performance
math problems (Cobbe et al., 2021). There are on automatic prompt engineering. The resulting
twomajortechniquestoboostLLMs’performance methodPE2refinespromptswrittenbyhumanexon this: (1) prompting methods that guide the pertsandsurpassesestablishedautomaticprompt
model to produce intermediate reasoning steps, engineeringbaselinesacrossvariousscenarios,noeither with few-shot demonstrations (Nye et al., tablyoncounterfactualtasksandaproductionap-
2021;Weietal.,2022a;Yaoetal.,2023)orwith plication. Through comprehensive analysis and
zero-shot prompts (Kojima et al., 2022); (2) self- case studies, we illustrate PE2’s ability to make
reflection methods that progressively guide the targeted prompt edits and generate high-quality
model to inspect its current output and refine it prompts,anddemonstrateitsgeneralapplicability
(Chenetal.,2024;Madaanetal.,2023;Pauletal., withdifferentLLMs.
2023; Kim et al., 2023a). At its core, prompt en- Thechallengeofpromptengineeringaprompt
gineering is a language generation task requiring engineerremainsongoing. Ashighlightedinour
complexreasoning. Humanpromptengineersusu- case study, we believe improving the LLM’s inallyexaminethefailurecasesproducedbythecur- struction following abilities and mitigating hallurent prompt closely, make hypotheses, and com- cination issues will be crucial for improving auposeanewprompt. Inthiswork,weexplorevari- tomatic prompt engineering. As the capabilities
ouspromptingstrategieswhenbuildinganLLM- ofLLMcontinuetoevolve,theirpotentialinvolvepoweredautomaticpromptengineer. mentinoptimizationorfeedbackloopsnecessitates
a deeper empirical understanding of their failure
Self-training and Self-improving for LLMs. modes(Panetal.,2024),includingshortcutlearn-
Self-trainingreferstothetechniqueofusingaweak ing discovered in this study. Looking ahead, we
modeltoannotateinput-labelpairsandusingthem arealsoexcitedaboutapplyingPE2tooptimizeits
for further training (Rosenberg et al., 2005). In ownmeta-promptinaself-referentialway,inline
thecontextofLLMs,STaR(Zelikmanetal.,2022) withMetzetal.(2020);Irieetal.(2022);Fernando
and Self-Improve (Huang et al., 2023) show that etal.(2023);Zelikmanetal.(2023).
9

<!-- Page 10 -->

Limitations tion with language constraints. arXiv preprint
arXiv:2212.10466.

### Firstly,weoptforarelativelysmallpromptsearch

Xinyun Chen, Maxwell Lin, Nathanael Schärli, and
budget (T = 3, m = 4, n = 4; see §4.3) due to

### DennyZhou.2024. Teachinglargelanguagemodels

cost considerations. In most of our experiments,
toself-debug. InTheTwelfthInternationalConfertheperformancetendstoplateauafterT = 3opti- enceonLearningRepresentations.
mizationsteps. However,it’simportanttoconsider
Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian,
thattheuseoftheinitializationprompt"let’sthink
MarkChen,HeewooJun,LukaszKaiser,Matthias
stepbystep"inmanycasesmightintroduceapo-

### Plappert, Jerry Tworek, Jacob Hilton, Reiichiro

tentialconfoundingfactor. Thispromptcouldbe Nakano,etal.2021. Trainingverifierstosolvemath
alreadynear-optimal,leadingtofastconvergence wordproblems. arXivpreprintarXiv:2110.14168.
during prompt optimization. Given the stochas-
Mingkai Deng, Jianyu Wang, Cheng-Ping Hsieh, Yiticnatureofnaturallanguagegenerationsampling
hanWang,HanGuo,TianminShu,MengSong,Eric
and prompt optimization dynamics, it is possible Xing,andZhitingHu.2022. RLPrompt: Optimizing
thatalargerpromptsearchbudgetordifferentex- discrete text prompts with reinforcement learning.
In Proceedings of the 2022 Conference on Empiriperimental settings could yield new insights and
calMethodsinNaturalLanguageProcessing,pages
conclusions.
3369–3391,AbuDhabi,UnitedArabEmirates.As-
Secondly, our study uses proprietary models sociationforComputationalLinguistics.
such as gpt-4 and text-davinci-003. (1) It

### Chrisantha Fernando, Dylan Banarse, Henryk

raisesreproducibilityconcernsasproprietarymod-
Michalewski, Simon Osindero, and Tim Rockelsmayundergoupgradesordiscontinuationover täschel. 2023. Promptbreeder: Self-referential
time. However, we believe the core concepts in- self-improvement via prompt evolution. arXiv
troduced in this paper is model-agnostic. This is preprintarXiv:2309.16797.
supported by our experiments where we use two

### Luyu Gao, Aman Madaan, Shuyan Zhou, Uri Alon,

differentsetsof(M proposal ,M task )(see§4.3)and PengfeiLiu, YimingYang, JamieCallan, andGraexperiments using Mistral-7B-Instruct-v0.2 ham Neubig. 2023. Pal: Program-aided language
modelasthetaskmodel. (2)Italsoraisesconcerns models. In International Conference on Machine
Learning,pages10764–10799.PMLR.
on data contamination, as the tasks and prompts
included in our study may or may not have been Robert Geirhos, Jörn-Henrik Jacobsen, Claudio
partofthemodel’strainingdata. Michaelis, Richard Zemel, Wieland Brendel,
Matthias Bethge, and Felix A Wichmann. 2020.

### Lastly,apartfromthethreetranslationtasksin


### Shortcutlearningindeepneuralnetworks. Nature

theInstructionInductionbenchmark,ourstudypre-
MachineIntelligence,2(11):665–673.
dominantly focuses on tasks in English. We recognize the importance of inclusivity in language Noah Goodman. 2023. Meta-prompt: A simple selfimprovinglanguageagent.
technology and acknowledge the need to extend
ourresearchtoamultilingualsettinginthefuture. Or Honovich, Uri Shaham, Samuel R. Bowman, and

### OmerLevy.2023. Instructioninduction: Fromfew

Acknowledgments examplestonaturallanguagetaskdescriptions. In
Proceedings of the 61st Annual Meeting of the As-

### Wethankanonymousreviewers,membersofUSC

sociationforComputationalLinguistics(Volume1:
NLP,andmembersofMicrosoftOfficeofApplied Long Papers), pages 1935–1952, Toronto, Canada.
Researchfortheirvaluablefeedback. Inparticular, AssociationforComputationalLinguistics.

### QinyuanYewouldliketothankMayeeChen,Zhuo-

Xinyu Hu, Pengfei Tang, Simiao Zuo, Zihan Wang,
ranLu,OnkarKulkarni,JakobSchoeffer,Connor

### Bowen Song, Qiang Lou, Jian Jiao, and Denis X

LawlessandMariosPapachristoufortheinsightful Charles. 2024. Evoke: Evoking critical thinking
conversationsandformakingherinternshipatruly abilitiesinLLMsviareviewer-authorpromptediting.
memorableexperience. QinyuanYewassupported InTheTwelfthInternationalConferenceonLearning
Representations.
byaUSCAnnenbergFellowship.

### JiaxinHuang,ShixiangGu,LeHou,YuexinWu,Xuezhi


### Wang, Hongkun Yu, and Jiawei Han. 2023. Large

References languagemodelscanself-improve. InProceedings
ofthe2023ConferenceonEmpiricalMethodsinNat-
Howard Chen, Huihan Li, Danqi Chen, and Karthik uralLanguageProcessing,pages1051–1068,Singa-
Narasimhan. 2022. Controllable text genera- pore.AssociationforComputationalLinguistics.
10

<!-- Page 11 -->

Kazuki Irie, Imanol Schlag, Róbert Csordás, and Jür- Katherine Hermann, Sean Welleck, Amir YazdangenSchmidhuber.2022. Amodernself-referential bakhsh, and Peter Clark. 2023. Self-refine: Iteraweightmatrixthatlearnstomodifyitself. InProc. tiverefinementwithself-feedback. InThirty-seventh
Int.Conf.onMachineLearning(ICML),Baltimore, ConferenceonNeuralInformationProcessingSys-
MD,USA. tems.
Albert Q Jiang, Alexandre Sablayrolles, Arthur Men- LukeMetz,NiruMaheswaranathan,CDanielFreeman,
sch,ChrisBamford,DevendraSinghChaplot,Diego BenPoole,andJaschaSohl-Dickstein.2020. Tasks,
delasCasas,FlorianBressand,GiannaLengyel,Guil- stability,architecture,andcompute: Trainingmore
laumeLample,LucileSaulnier,etal.2023. Mistral effectivelearnedoptimizers,andusingthemtotrain
7b. arXivpreprintarXiv:2310.06825. themselves. arXivpreprintarXiv:2009.11243.
ZhengbaoJiang,FrankF.Xu,JunAraki,andGraham MoranMizrahi,GuyKaplan,DanMalkin,RotemDror,
Neubig. 2020. How can we know what language DafnaShahaf, andGabrielStanovsky.2023. State
modelsknow? TransactionsoftheAssociationfor ofwhatart? acallformulti-promptllmevaluation.
ComputationalLinguistics,8:423–438. arXivpreprintarXiv:2401.00595.
Geunwoo Kim, Pierre Baldi, and Stephen McAleer. MaxwellNye,AndersJohanAndreassen,GuyGur-Ari,
2023a. Languagemodelscansolvecomputertasks. Henryk Michalewski, Jacob Austin, David Bieber,
arXivpreprintarXiv:2303.17491. David Dohan, Aitor Lewkowycz, Maarten Bosma,

### DavidLuan,etal.2021. Showyourwork: Scratch-

Seungone Kim, Se Joo, Doyoung Kim, Joel Jang, pads for intermediate computation with language
Seonghyeon Ye, Jamin Shin, and Minjoon Seo. models. arXivpreprintarXiv:2112.00114.
2023b. The CoT collection: Improving zero-shot
andfew-shotlearningoflanguagemodelsviachain- OpenAI. 2023. Gpt-4 technical report. ArXiv,
of-thoughtfine-tuning. InProceedingsofthe2023 abs/2303.08774.
Conference on Empirical Methods in Natural LanguageProcessing, pages12685–12708, Singapore. LongOuyang,JeffreyWu,XuJiang,DiogoAlmeida,
AssociationforComputationalLinguistics. CarrollWainwright,PamelaMishkin,ChongZhang,
SandhiniAgarwal,KatarinaSlama,AlexRay,etal.
TakeshiKojima,ShixiangShaneGu,MachelReid,Yu- 2022. Training languagemodelsto followinstructakaMatsuo,andYusukeIwasawa.2022. Largelan- tions with human feedback. Advances in Neural
guagemodelsarezero-shotreasoners. InAdvances InformationProcessingSystems,35:27730–27744.
inNeuralInformationProcessingSystems.

### Alexander Pan, Erik Jones, Meena Jagadeesan, and

Woosuk Kwon, Zhuohan Li, Siyuan Zhuang, Ying Jacob Steinhardt. 2024. Feedback loops with lan-
Sheng, Lianmin Zheng, Cody Hao Yu, Joseph E. guagemodelsdrivein-contextrewardhacking. arXiv
Gonzalez, Hao Zhang, and Ion Stoica. 2023. Effi- preprintarXiv:2402.06627.
cientmemorymanagementforlargelanguagemodel
servingwithpagedattention. InProceedingsofthe DebjitPaul,MeteIsmayilzada,MaximePeyrard,Beat-
ACMSIGOPS29thSymposiumonOperatingSystems riz Borges, Antoine Bosselut, Robert West, and
Principles. Boi Faltings. 2023. Refiner: Reasoning feedback
on intermediate representations. arXiv preprint
Moxin Li, Wenjie Wang, Fuli Feng, Yixin Cao, Jizhi arXiv:2304.01904.

### Zhang, and Tat-Seng Chua. 2023. Robust prompt

optimizationforlargelanguagemodelsagainstdistri- Archiki Prasad, Peter Hase, Xiang Zhou, and Mohit
butionshifts. InProceedingsofthe2023Conference Bansal. 2023. GrIPS: Gradient-free, edit-based inonEmpiricalMethodsinNaturalLanguageProcess- structionsearchforpromptinglargelanguagemodels.
ing, pages 1539–1554, Singapore. Association for InProceedingsofthe17thConferenceoftheEuro-
ComputationalLinguistics. peanChapteroftheAssociationforComputational
Linguistics, pages3845–3864, Dubrovnik, Croatia.
YaoLu,MaxBartolo,AlastairMoore,SebastianRiedel, AssociationforComputationalLinguistics.
and Pontus Stenetorp. 2022. Fantastically ordered
promptsandwheretofindthem: Overcomingfew- ReidPryzant,DanIter,JerryLi,YinLee,Chenguang
shotpromptordersensitivity. InProceedingsofthe Zhu,andMichaelZeng.2023. Automaticpromptop-
60thAnnualMeetingoftheAssociationforCompu- timizationwith“gradientdescent”andbeamsearch.
tationalLinguistics(Volume1: LongPapers),pages In Proceedings of the 2023 Conference on Empiri-
8086–8098,Dublin,Ireland.AssociationforCompu- calMethodsinNaturalLanguageProcessing,pages
tationalLinguistics. 7957–7968, Singapore. Association for ComputationalLinguistics.

### AmanMadaan, NiketTandon,PrakharGupta,Skyler

Hallinan, Luyu Gao, Sarah Wiegreffe, Uri Alon, Ning Qian. 1999. On the momentum term in gradi-
Nouha Dziri, Shrimai Prabhumoye, Yiming Yang, ent descent learning algorithms. Neural networks,
Shashank Gupta, Bodhisattwa Prasad Majumder, 12(1):145–151.
11

<!-- Page 12 -->

LariaReynoldsandKyleMcDonell.2021. Promptpro- withlanguagemodelsenablesexpert-levelpromptopgramming for large language models: Beyond the timization. InTheTwelfthInternationalConference
few-shot paradigm. In Extended Abstracts of the onLearningRepresentations.
2021CHIConferenceonHumanFactorsinComputingSystems,pages1–7. JasonWei,XuezhiWang,DaleSchuurmans,Maarten

### Bosma, brian ichter, Fei Xia, Ed Chi, Quoc V Le,

ChuckRosenberg,MartialHebert,andHenrySchnei- andDennyZhou.2022a. Chain-of-thoughtpromptderman.2005. Semi-supervisedself-trainingofob- ing elicits reasoning in large language models. In
ject detection models. 2005 Seventh IEEE Work- AdvancesinNeuralInformationProcessingSystems,
shopsonApplicationsofComputerVision(WACV/- volume35,pages24824–24837.CurranAssociates,
MOTION’05)-Volume1,1:29–36. Inc.
SubhroRoyandDanRoth.2015. Solvinggeneralarith- JasonWei,XuezhiWang,DaleSchuurmans,Maarten
metic word problems. In Proceedings of the 2015 Bosma, brian ichter, Fei Xia, Ed Chi, Quoc V Le,
Conference on Empirical Methods in Natural Lan- andDennyZhou.2022b. Chain-of-thoughtpromptguageProcessing,pages1743–1752,Lisbon,Portu- ing elicits reasoning in large language models. In
gal.AssociationforComputationalLinguistics. AdvancesinNeuralInformationProcessingSystems,
volume35,pages24824–24837.CurranAssociates,
MelanieSclar,YejinChoi,YuliaTsvetkov,andAlane Inc.
Suhr.2024. Quantifyinglanguagemodels’sensitivitytospuriousfeaturesinpromptdesignor: Howi ZhaofengWu,LinluQiu,AlexisRoss,EkinAkyürek,
learned to start worrying about prompt formatting. BoyuanChen,BailinWang,NajoungKim,JacobAn-
InTheTwelfthInternationalConferenceonLearning dreas,andYoonKim.2024. Reasoningorreciting?
Representations. exploringthecapabilitiesandlimitationsoflanguage
models through counterfactual tasks. In Proceed-
Noah Shinn, Federico Cassano, Beck Labash, Ash- ingsofthe2024ConferenceoftheNorthAmerican
win Gopinath, Karthik Narasimhan, and Shunyu Chapter of the Association for Computational Lin-
Yao. 2023. Reflexion: Language agents with guistics: Human Language Technologies (Volume
verbal reinforcement learning. arXiv preprint 1: Long Papers), pages 1819–1862, Mexico City,
arXiv:2303.11366. Mexico.AssociationforComputationalLinguistics.
JiaoSun,YufeiTian,WangchunshuZhou,NanXu,Qian HanweiXu,YujunChen,YulunDu,NanShao,Yang-
Hu,RahulGupta,JohnWieting,NanyunPeng,and gangWang,HaiyuLi,andZhilinYang.2022. Gps:
XuezheMa.2023. Evaluatinglargelanguagemodels Geneticpromptsearchforefficientfew-shotlearning.
oncontrolledgenerationtasks. InProceedingsofthe arXivpreprintarXiv:2210.17041.
2023ConferenceonEmpiricalMethodsinNatural
LanguageProcessing,pages3155–3168,Singapore. Chengrun Yang, Xuezhi Wang, Yifeng Lu, Hanxiao
AssociationforComputationalLinguistics. Liu, Quoc V Le, Denny Zhou, and Xinyun Chen.

## Large language models as optimizers. In

Mirac Suzgun, Nathan Scales, Nathanael Schärli, Se- The Twelfth International Conference on Learning
bastian Gehrmann, Yi Tay, Hyung Won Chung, Representations.

### Aakanksha Chowdhery, Quoc Le, Ed Chi, Denny

Zhou,andJasonWei.2023. ChallengingBIG-bench Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak
tasksandwhetherchain-of-thoughtcansolvethem. Shafran,KarthikRNarasimhan,andYuanCao.2023.
InFindingsoftheAssociationforComputationalLin- React: Synergizingreasoningandactinginlanguage
guistics: ACL 2023, pages 13003–13051, Toronto, models. InTheEleventhInternationalConference
Canada.AssociationforComputationalLinguistics. onLearningRepresentations.
XingchenWan,RuoxiSun,HanjunDai,SercanArik, J.D. Zamfirescu-Pereira, Richmond Y. Wong, Bjoern
andTomasPfister.2023a. Betterzero-shotreasoning Hartmann,andQianYang.2023. Whyjohnnycan’t
withself-adaptiveprompting. InFindingsoftheAs- prompt: Hownon-aiexpertstry(andfail)todesign
sociationforComputationalLinguistics: ACL2023, llmprompts. InProceedingsofthe2023CHIConferpages3493–3514,Toronto,Canada.Associationfor enceonHumanFactorsinComputingSystems,CHI
ComputationalLinguistics. ’23,NewYork,NY,USA.AssociationforComputing
Machinery.

### XingchenWan, RuoxiSun, HootanNakhost, Hanjun

Dai, Julian Eisenschlos, Sercan Arik, and Tomas Eric Zelikman, Eliana Lorch, Lester Mackey, and
Pfister. 2023b. Universal self-adaptive prompting. Adam Tauman Kalai. 2023. Self-taught optimizer
In Proceedings of the 2023 Conference on Empiri- (stop): Recursivelyself-improvingcodegeneration.
calMethodsinNaturalLanguageProcessing,pages arXivpreprintarXiv:2310.02304.
7437–7462, Singapore. Association for ComputationalLinguistics. EricZelikman,YuhuaiWu,JesseMu,andNoahGoodman.2022. Star: Bootstrappingreasoningwithrea-
XinyuanWang,ChenxiLi,ZhenWang,FanBai,Hao- soning. InAdvancesinNeuralInformationProcesstianLuo,JiayouZhang,NebojsaJojic,EricXing,and ingSystems,volume35,pages15476–15488.Curran
ZhitingHu.2024. Promptagent: Strategicplanning Associates,Inc.
12

<!-- Page 13 -->

Tianjun Zhang, Aman Madaan, Luyu Gao, Steven A AdditionalResultsandAnalysis
Zheng, SwaroopMishra, YimingYang, NiketTandon,andUriAlon.2024. In-contextprinciplelearn- A.1 EffectofInitialization
ingfrommistakes. arXivpreprintarXiv:2402.05403.
Previously, we use “Let’s think step by step” as

### Tianjun Zhang, Xuezhi Wang, Denny Zhou, Dale

theinitializationformathreasoningtasks. Wefur-
Schuurmans, and Joseph E Gonzalez. 2022. Tempera:Test-timepromptingviareinforcementlearning. ther experiment with using a misleading prompt,
arXivpreprintarXiv:2211.11890. an irrelevant prompt and induction initialization
(inductionfromafewexamples). Theresultsare
Tony Zhao, Eric Wallace, Shi Feng, Dan Klein, and
presentedinTable8andtheoptimizationdynamics
SameerSingh.2021. Calibratebeforeuse: Improving few-shot performance of language models. In arevisualizedinFig.6.
InternationalConferenceonMachineLearning.
PeiZhou,JayPujara,XiangRen,XinyunChen,Heng- MultiArith GSM8K
Initialization

### Dev Dev

TzeCheng,QuocVLe,EdHChi,DennyZhou,SwaroopMishra,andHuaixiuStevenZheng.2024. Self- default(Let’sthinkstepbystep.) 92.0 68.0
discover: Largelanguagemodelsself-composerea- misleading†(Don’tthink.Justfeel.) 81.0 50.0
soningstructures. arXivpreprintarXiv:2402.03620. irrelevant†(It’sabeautifulday.) 73.0 49.0
inductionfromfew-shotexamples 84.0 43.0
Wangchunshu Zhou, Yuchen Eleanor Jiang, Ethan
no-op(Let’sthinkstepbystep.) 85.0 57.0
Wilcox, Ryan Cotterell, and Mrinmaya Sachan.
2023a. Controlledtextgenerationwithnaturallan- Table 8: Effect of Initialization. † The prompts are
guageinstructions. InProceedingsofthe40thInteroriginallyfrom(Kojimaetal.,2022).
nationalConferenceonMachineLearning,volume
202ofProceedingsofMachineLearningResearch,
pages42602–42613.PMLR.
Yongchao Zhou, Andrei Ioan Muresanu, Ziwen Han,
1.00
KeiranPaster,SilviuPitis,HarrisChan,andJimmy
0.75

### Ba.2023b. Largelanguagemodelsarehuman-level

prompt engineers. In The Eleventh International 0.50
ConferenceonLearningRepresentations. 0.25
0.00
Start 1 2 3
Timestamp
.ccA
veD
htirAitluM

### Effect of Prompt Initialization

default irrelevant misleading induction

### Best Prompt

Figure6: PromptoptimizationdynamicsonMultiArith
whendifferentpromptinitializationsareused.

### Ingeneral,performancedropswhenalternative

initialization methods are used, which highlights
theimportanceofhigh-qualityinitialization. Still,

### PE2isabletooverridetheirrelevantormisleading

prompts and gradually improve the performance
(Fig.6). Remarkably,PE2isabletodiscoverahigh
qualityprompt3 byitselfusinginductioninitialization(84%onMultiArith-Dev)thatalmostmatches
with “Let’s think step by step” (85%) designed
by highly-experienced human prompt engineers.
ThisdemonstratestheimpressivepromptengineeringcapabilityofPE2andsuggestsitspotentialfor
findingevenbetterpromptswhengivenadditional
computationalresources.
3MultiArithpromptfoundbyPE2usinginductioninitialization:“Analyzetheproblemandperformthecalculations.
Consideraddition,subtraction,division,multiplicationand
performthemintheordertheyappear.Ifrequired,roundup
resultstothenearestwholenumber.Subtractdonetasksfrom
totalwhennecessary.”
13

<!-- Page 14 -->


### A.2 EffectofTaskFormat

For Date Understanding from BIG-bench Hard,
weexperimentwithbothagenerativeformat(i.e.,
generating the answer string; used in Gao et al.
(2023)) and a discriminative/multi-choice format
(i.e.,selectingfromgivenchoicesA/B/C/D;used
inSuzgunetal.(2023)). ForMovieRecommendation,weexperimentwithtwodifferentmulti-choice
formats. SeeTable9fortheformatsthatweused.

### Task Example

DateUnderstanding Today is 9/7. Jane is watching NFL 2003.
(multi-choice) WhatisthedatetomorrowinMM/DD/YYYY?

### Options: (A)09/08/1916(B)09/13/2003(C)


## 08/18/2003(D)09/08/2003(E)09/15/2003(F)


## 09/01/2003(D)

DateUnderstanding May6,1992islikeyesterdaytoJane,butthatis
(generative) actuallytenyearsago.Whatisthedateamonth
agoinMM/DD/YYYY?04/06/2002
MovieRecommendation Find a movie similar to Rocky, Star Wars
(multi-choice1) EpisodeIV-ANewHope, ToyStory, The

### Terminator: Options: (A)DraculaDeadand

LovingIt(B)IndependenceDay(C)TheExtraordinaryAdventuresofAdèleBlanc-Sec(D)

### TheAmericanPresident(B)

MovieRecommendation WhatmovieissimlartoApollo13,Jurassic
(multi-choice2) Park, Die Hard With a Vengeance, Forrest
Gump? Choose from the following: Killer
Movie,Stealth,TheLastManonEarth,True

### Lies.TrueLies

Table9:DifferentTaskFormatsforDateUnderstanding
and Movie Recommendation. The correct answer is
markedinblue.
100
80
60
40
20
0

### Date Date Movie Movie

(Multi-choice) (Generative) (Multi-choice 1) (Multi-choice 2)
ycaruccA
tseT
genre, director, ...), which boost the task performance. Minor formatting decisions such as outputting the option letter or the option string can
stillmildlyaffectthefinalaccuracy.
Overall, the question of “when is automatic
promptoptimizationmosteffective”isdependent
onmanyfactors,includingtaskformat,taskdifficulty, output space size, task model’s instruction
followingabilities,etc.
A.3 Dooptimizedpromptsgeneralizetoother

### LLMs?


### We evaluate 5 GSM8K prompts for our prompt

generalization study (see Table 10). Note that
the APO and PE2 prompts are optimized for
text-davinci-003. The two prompts reported
in OPRO (Yang et al., 2024) are optimized
for PaLM 2-L. We investigate the generalization of optimized prompts by evaluating them
on four models: gpt-3.5-turbo-instruct,
mistral-7b-instruct-v0.2, yi-6b, and
mpt-7b-instruct. WereporttheresultsinFig.8.

### Method GSM8KPrompt

Zero-shotCoT Let’sthinkstepbystep.

### Giventhescenario,performnecessarycalculationsand

APO provideastep-by-stepexplanationtoarriveatthecorrect
numericalanswer.Considerallinformationprovided.
Let’ssolvetheproblemstep-by-stepandcalculatethe

## Pe2

requiredtotalvaluecorrectly.
OPRO(1) Takeadeepbreathandworkonthisproblemstep-by-step.
Let’scombineournumericalcommandandclearthinking
Zeroshot CoT Iterative APE APO PE2 OPRO(2)
toquicklyandaccuratelydeciphertheanswer.
Table10:PromptsusedintransferabilitystudyinFig.8.
80
Figure 7: Effect of Task Format. See Table 9 for the 60
formatsused. 40
20
We report the results in Fig. 7. For Date Un-
0
text-davinci gpt-3.5-turbo mistral-7b yi-6b mpt-7b
derstanding, themulti-choiceformatnarrowsthe 003 instruct instruct-v0.2 instruct
output space and thus lower the difficulty of the
task. We hypothesize that in combination with
Zero-shotCoT,thetaskperformanceisclosetosaturationandautomaticpromptengineeringmethod
does not provide extra benefit. The task is more
challenging in the generative format and the detailed instructions in the optimized prompt bring
significantperformancegains.

### For Movie Recommendation, we found that

promptoptimizationmethodsbringsignificantperformance gains in both cases. The optimized
prompts contain multi-step plans (e.g., consider
ycaruccA
tseT

## K8Msg

elbaliavA
toN
Zeroshot CoT

## Apo


## Pe2


## Opro (1)


## Opro (2)

Figure8:Analysisongeneralizabilityofpromptsacross
models. SeeTable10forthepromptsusedinthisstudy.
Our results do not exhibit consistent generalization trends. Optimized prompts
generally outperforms the original zeroshot CoT prompt on text-davinci-003,
mistral-7b-instruct-v0.2, yi-6b. However,
with gpt-3.5-turbo-instruct, the original
CoT prompt outperforms all optimized prompts.

### Our hypothesis is that “Let’s think step by

step” is included in public instruction tuning
14

<!-- Page 15 -->

collections (Kim et al., 2023b) and thus models trained on these collections may perform
better with this special prompt. However the
instruction tuning mixture used for training
gpt-3.5-turbo-instructarenotdisclosed,and
thuswecannotfurtherinvestigatethis.
Overall, our results suggest that current automatic prompt optimization methods tend to find
model-specificpromptsthatdonotreliablygeneralizetoalternativemodels. Thisconclusioncontrasts
with the findings in PromptAgent (Wang et al.,
2024),whichweattributetodiscrepanciesinexperimentalsetup. Tomaintainconsistencywithprior
research(Zhouetal.,2023b),wehavelimitedthe
promptlengthtobe50or200tokens. Theconclusionmaydifferwhenthisconstraintisremoved.
Future work may develop robust prompt optimizationmethodsthatoperateacrossmultipletask
models,inawaysimilartoLietal.(2023)which
operates across domains. This may help identify
high-quality prompts invariant to the underlying
taskmodel,sothatwhennewandmorepowerful
models (e.g., GPT-5) are released, the optimized
promptmaybeuseddirectly.
(Continuedonnextpage)
15

<!-- Page 16 -->


### B OtherMeta-PromptComponentsWeTried

Inadditiontothemeta-promptcomponentsstudiesinthemainpaper,wealsotriedothercomponentsin
theearlystageofPE2’sdevelopment. Astheresultsaremixedandinconclusiveonthesecomponents,we
reportthemhereintheappendix. WeillustratethesecomponentsinFig.9.
(d) prompt engineering tutorial (c) step-by-step reasoning template
Let’s read a blogpost on prompt engineering: # Instruction

### For each example, provide reasoning according to the

Prompt engineering is a relatively new discipline for following template
developing and optimizing prompts to efficiently use * Output is correct?
language models (LMs) … * Prompt describing the task correctly?
* Necessary to edit the prompt?
(a) two-step task instruction * If yes, suggestions on prompt editing?
A prompt is a text paragraph that outlines the expected actions ## Example 1
and instructs the model. In our collaboration, we'll work Output is correct? No.
together to refine a prompt. The process consists of two steps: Reasoning: the model didn't subtract the socks he threw
# Step 1 away.
Examine the prompt and a batch of examples Prompt describing the task correctly? Yes.
# Step 2 Necessary to edit the prompt? Yes.
Propose a new prompt based on your reasoning Suggestions: The prompt should be edited to guide the
model to perform subtraction.
[More examples …]
Sure! I'd be happy to help you.
# Current Prompt Now carefully review your reasoning and proceed with step
Let’s think step by step. 2: refine the prompt.
# Full Template (b) context specification # Current Prompt
``` Let’s think step by step.

### Question: <input>

Answer: Let’s think step by step. # Optimization History (g) optim history
``` At time 0, the prompt was “…”, it was edited …
# Examples (e) batch size # Instructions (f) step size
## Example 1 * You are allowed to change up to 10 words
Input: George had 28 socks. If he threw away 4 socks … * The total length should be less than 50 words
Output: 64 * Reply with the prompt. Do not include other text.
Reasoning: Step 1: George had 28 socks. Step 2: …

### Label: 60

Let’s solve this problem step by step. Remember to add or
[More examples …] subtract as needed.
Meta-Prompt: Instruction and Context Meta-Prompt: Optimizer Concepts Prompt Feedback (“Gradients”)
Figure9: Illustrationofmeta-promptcomponentsdiscussedinAppendixB.
ProvidingDetailedInstructionsandContext.
(d) PromptEngineeringTutorial. TohelptheLLMbetterunderstandthetaskofpromptengineering,
weprovideanonlinetutorialofpromptengineeringinthemeta-prompt.4
IncorporatingCommonOptimizerConcepts. ThepromptengineeringproblemdescribedinEq.1
is essentially an optimization problem, and the prompt proposal in Eq. 2 can be considered as doing
one optimization step. Thus, we consider the following concepts commonly used in gradient-based
optimizationanddeveloptheirverbalizedcounterpartstobeusedinourmeta-prompt.
(e) Batch Size. Batch size is the number of (failure) examples that is used in each prompt proposal
step (Eq. 2). By default PE2 uses a batch size of 2. We experiment with batch sizes of {1,4,8}
additionallyinthissection.
(f) StepSize. Ingradient-basedoptimization,thestepsizedeterminestheextenttowhichthemodel’s
weightsareupdated. Inpromptengineering,thecounterpartwouldbethenumberofwords(tokens)
4https://www.promptingguide.ai/introduction.PublishedunderMITlicense.
16

<!-- Page 17 -->

MultiArith GSM8K

### Method


### Dev Dev

PE2(default) 92.0 68.0

### Meta-promptComponents

+promptengineeringtutorial 90.0 63.0
+tunebatchsize{1,2,4,8} 92.0 68.0
+tunestepsize{5,10,15,None} 95.0 68.0
+optimhistoryandmomentum 93.0 67.0
Table11: Investigationonmeta-promptcomponentsandconfigurations(Appendix).
that can be modified. We directly specify that “You are allowed to change up to s words in the
originalprompt”inthemeta-prompt,wheres ∈ {5,10,15,None}.5
(g) Optimization History and Momentum. Momentum (Qian, 1999) is a technique to accelerate
optimizationandavoidoscillationsbymaintainingthemovingaverageofpastgradients. Todevelop
theverbalizedcounterpartofmomentum,weincludeallpastprompts(attimestamp0,1,...,t−1),
theirperformanceonthedevset,andasummaryofpromptedits.
Results and discussion. We report the results when these components are used in Table 11. We do
not observe significant improvement by incorporating prompt engineering tutorial. As the tutorial is
excessivelylong(2500+tokens)andslowsdowntheruntime,wedonotincludeitinthefinalversion
of PE2. The optimizer-inspired concepts can improve the performance occasionally, but the current
experimentsdonotgiveaconsistentconclusionregardingtheirutilities.
Similartothechallengesencounteredingradient-basedoptimization,theprocessofhyperparameter
selection is inherently noisy and often varies depending on the task at hand. For discrete prompt
optimization, thiscomplexityisfurthercompoundedbyfactorssuchasthetaskmodel’ssensitivityto
promptsandtheproposalmodel’scapabilitytofollowinstructionsinthemeta-prompt. Forexample,Sun
etal.(2023)pointoutthatLLMsstruggledatmeetingfine-grainedconstraintssuchas“generateexactly5
words,”whichcouldpotentiallydiminishtheeffectivenessofthe(f)stepsizecomponent. Additionally,
(g)momentumrequiresmultipleoptimizationstepstoaccumulate,yetourexperimentsarerestrictedto
threestepsduetocostconstraints.
Althoughthesemeta-promptcomponentsdonotcurrentlytakeeffectconsistentlywithexistingLLMs
and experimental settings, their potential justifies re-examination in the future, particularly as models
become more capable, and the efficiency and scalability of automatic prompt engineering methods
improve.
C AdditionalDiscussion

### C.1 RecentWorks

A recent work (Yang et al., 2024) introduced the concept of large language models as optimizers and
proposedoptimizationbyprompting(OPRO).Inthefollowing,wediscussthedifferencesandconnections
betweenOPROandourwork.
(1) Focus of the work. Both OPRO and our work conduct experiments on prompt optimization; the
focusofthetwoworksdiffer. OPROcanbeappliedtogeneraloptimizationproblems,includinglinear
regressionandtravelingsalesmanproblem. Inourworkwelimitthescopetopromptoptimization,witha
specificfocusonproposingandinvestigatingdifferentcomponentsinthemeta-prompt.
(2) Optimization strategy. The optimization strategies of the two works are different. PE2 is largely
inspiredbytheconceptsinAPO(Pryzantetal.,2023),instructingthemodeltoproducetextualfeedback
(“gradient”)explicitly. Itismoreanalogoustogradientdescent. OPROusestheexecutionaccuracyas
rewardstoguidetheoptimizationindirectly,which,inourunderstanding,ismoreanalogoustoin-context
5Chenetal.(2022)andZhouetal.(2023a)showedthatLLMscouldfollowtextgenerationconstraintsspecifiedinnatural
language.
17

<!-- Page 18 -->

RLmethods(Shinnetal.,2023). Forfuturework,itwouldbeinterestingtocomparetheeffectivenessand
efficiencyofbothmethodsinacontrolledsetup.
(3) Challenges in making direct comparison. Yang et al. (2024) mainly uses PaLM 2-L model and
text-bisonmodelasthetaskmodel(scorer),andoptimizesthepromptforupto200steps. Inourwork,
wemainlyusetext-davinci-003andGPT-4, andoptimizethepromptfor3stepsbydefault. Dueto
accessandbudgetconstraints,weareunabletomakedirectcomparisonwithOPRO.
InadditiontoOPRO,severalrecentworkshaveexploredautomaticpromptengineeringusingdiverse
strategies. PromptBreeder(Fernandoetal.,2023)adoptsaself-referentialpromptevolutionframework,
employingmutationprompts(similartotheconceptof“meta-prompts”discussedinthispaper)toedittask
prompts,andhyper-mutationpromptstoeditmutationprompts. PromptAgent(Wangetal.,2024)adopts
the Monte Carlo Tree Search algorithm that iteratively performs selection, expansion, simulation and
back-propagationforstrategicpromptediting. Evoke(Huetal.,2024)introducesacollaborativeapproach
whereanLLM-reviewerandanLLM-authorworktogethertorefinethepromptusingcriticalthinking.
Inparalleltotheseworks,wefocusonthedesignandevaluationofthemeta-promptinLLM-powered
automaticpromptengineeringinthispaper.
Our work is also related to Self-Discover (Zhou et al., 2024), a framework for LLMs to compose
reasoning structures, such as “break down into sub-tasks” for complex tasks. PE2 demonstrates task
decompositionbehaviorsasdiscussedin§5.3andTable6,whichcanbeseenaspresenceofrudimentary
meta-reasoningcapabilitiesinLLMs.

### C.2 DiscussiononusingPE2tooptimizeitsownmeta-prompt

Conceptually,PE2maybeappliedtonotonlyoptimizeprompts,butalsometa-prompts. Wecanreplace
p(t) andp(t+1) inEq.2withthemeta-promptpmeta directlytoenablePE2tooptimizethemeta-prompt.
Webelievethisisanexcitingdirectiontopursue. However,threechallenges(andbroaderquestions)arise
ifwepursuethisdirection,andwelookforwardtoaddressingthesechallengesinthefuture:

## How to collect data for such a study? To ensure this meta-prompt is general we may need a large

collectionoftasksalongwithpromptoptimizationhistoryassociatedwiththem. Creatingaresource
likethiswillbealargeeffort.

## How to automatically optimize the meta-prompt when there are no ground truth labels for prompt

engineering? Math problems have ground-truth answers so that PE2 can inspect them and provide
feedbackforpromptrefinement. Thetaskofpromptengineeringdoesnothavegroundtruthlabels,
andthispotentiallymakesthemeta-promptoptimizationprocessmorenoisy.

## It would be very costly to run and even evaluate a system like this. To evaluate one meta-prompt

candidateandshowitoutperformsothermeta-promptcandidates,wewillneedtouseitforprompt
optimizationonvarioustasks. Wewouldexpecttheoptimizationprocessofthemeta-prompttobea
magnitudemorecostly.
D AdditionalExperimentDetails
D.1 PromptSearchAlgorithm
SeeAlgorithm1.

### D.2 ControllingPromptLength

Bydefaultthemaxlengthofpromptsissettobe50tokens,followingZhouetal.(2023b). Forcounterfactualtasks,toallowmorespacetoexplainthecounterfactualsituations,themaxlengthissettobe200
tokens.

### D.3 InfrastructureandRuntime

Infrastructure. We use OpenAI API6 to access text-davinici-003, gpt-3.5-turbo-instruct,
gpt-4, gpt-4-turbo. For prompt generalization experiments using mistral-7b-instruct,
6https://openai.com/blog/openai-api
18

<!-- Page 19 -->


### Algorithm1SearchProcedure

1: P(0) =P orP(0) =M (x ,y ,...,x ,y ;pinit) ▷Manualinit.orinductioninit.
init init 1 1 n n
2: fort=0,...,T −1do
3: P(t+1) =∅
4: forp(t) ∈Select-Best(∪t P(i),n)do ▷SelectbestnpromptsbasedonD
i=0 dev
5: forj =1...mdo
6: B =Sample(D ) ▷Sampleabatch(randomorfailureexamples)
train
7: p(t+1) =M (p(t),B;pmeta) ▷Newpromptproposal
optim
8: P(t+1) =P(t+1)∪{p(t+1)}
9: endfor
10: endfor
11: endfor
12: returnSelect-Best(∪T P(i),1) ▷ReturnthefinalbestpromptbasedonD
i=0 dev
mpt-7b-instruct and yi-6b, we run experiments locally using one Nvidia RTX A6000 GPU and
thevLLMtoolkit(Kwonetal.,2023).
Runtime. One prompt optimization experiment using gpt-4/text-davinici-003 as task/proposal
modeltakesabout90minutes. ThisisalsosubjecttoAPIratelimits.
Costs. When using gpt-4/text-davinci-003 it costs about $25 USD for one prompt optimization
experiment. Inthelaterstageofthisproject,weusegpt-4-turbo/gpt-3.5-turbo-instructwhichare
newerandcheaper,andthecostisreducedtoabout$3USDperexperiment.

### D.4 TasksandData

We summarize the dataset size and data split information in Table 12. We summarize the source and
licenseinformationofthedatasetsinTable13. Tothebestofourknowledge,ourusageofthesedatasets
areconsistentwiththeirintendeduse;thedataweusedonotcontainpersonalorsensitiveinformation.
MostofthedatasetsareinEnglishandnotdomain-specific.
Dataset Subtasks |T train | |T dev | |T test | #RandomSamples
MultiArith(RoyandRoth,2015) - 100 100 400 1

### GSM8K(Cobbeetal.,2021) - 100 100 1319 1

InstructionInduction(Honovichetal.,2023) 14Subtasks 100 20 100 5

### CounterfactualEval(Wuetal.,2024) 12Subtasks 100 20 100 5

BIG-BenchHard(BBHformatusedinSuzgunetal.(2023)) 27Subtasks 100 100 50 1
BIG-BenchHard(Alternativeformat;see§A.2) 2Subtasks 100 100 500 1
Table12: Datasetsizesanddatasplits.

### Dataset License Source

MultiArith(RoyandRoth,2015) Unknown https://github.com/wangxr14/Algebraic-Word-Problem-Solver/
GSM8K(Cobbeetal.,2021) MIT https://github.com/openai/grade-school-math
InstructionInduction(Honovichetal.,2023) Apache-2.0 https://github.com/orhonovich/instruction-induction
CounterfactualEval(Wuetal.,2024) Unknown https://github.com/ZhaofengWu/counterfactual-evaluation
BIG-benchHard(Suzgunetal.,2023) Apache-2.0 https://github.com/google/BIG-bench(original)
https://github.com/suzgunmirac/BIG-Bench-Hard(reformatted)
Table13: LicenseandSourceofthedatasetsusedinthisstudy.
(1)MathematicalReasoning. TheMultiArithdataset(RoyandRoth,2015)contains600examples.
As our prompt optimization method requires a training set, we randomly split into 100/100/400 for
train/dev/test. Thiscreatesaslightdiscrepancywhencomparingtheresultswithpastreportedresults. We
ensureourreproductionisfairacrossdifferentmethodsbyusingthisfixedsplit. TheGSM8Kdataset
(Cobbeetal.,2021)hasaprovidedtestsplit(1319examples). Werandomlyselected200examplesfor
theoriginaltrainsplit,anduse100asD and100asD .
train dev
19

<!-- Page 20 -->

Task Instruction Demonstration

### Subtasksusedinthiswork(14)


### SecondLetter Extractthefirstletteroftheinputword. cat→a

StartingWith Extractthewordsstartingwithagivenletterfrom ThemanwhosecarIhitlastweeksuedme.[m]→
theinputsentence. man,me
Negation Negatetheinputsentence. Timeisfinite→Timeisnotfinite.
Antonyms Writeawordthatmeanstheoppositeoftheinput won→lost
word.
Synonyms Writeawordwithasimilarmeaningtotheinput alleged→supposed
word.
Membership Writealltheanimalsthatappearinthegivenlist. cat,helicopter,cook,whale,frog,lion→frog,cat,
lion,whale

### Rhymes Writeawordthatrhymeswiththeinputword. sing→ring

InformaltoFormal Rephrasethesentenceinformallanguage. Pleasecallonceyougetthere→Pleasecallupon
yourarrival.

### TranslationEN-DE TranslatethewordintoGerman. game→spiel

TranslationEN-ES TranslatethewordintoSpanish. game→jeugo

### TranslationEN-FR TranslatethewordintoFrench. game→jeu

Sentiment Determine whether a movie review is positive or Thefilmissmallinscope,yetperfectlyformed.→
negative. positive
SentenceSimilarity Ratethesemanticsimilarityoftwosentencesona Sentence1:Amanissmoking.Sentence2:Aman
scaleof0to5 isskating.→0-definitelynot
WordinContext Determinewhetheraninputwordhasthesamemean- Sentence1: Approachatask. Sentence2: Toapinginthetwosentences. proachthecity.Word:approach→notthesame
Subtasksremovedduetonear-perfectaccuracy(95%+)withbaselinemethod(8)

### FirstLetter Extractthefirstletteroftheinputword. cat→c

ListLetters Breaktheinputwordintoletters,separatedbyspaces. cat→cat
SingulartoPlural Converttheinputwordtoitspluralform. cat→cats
ActivetoPassive Writetheinputsentenceinpassiveform. Theartistintroducedthescientist. →Thescientist
wasintroducedbytheartist.
LargerAnimal Writethelargerofthetwogivenanimals. koala,snail→koala

### Sum Sumthetwogivennumbers. 2210→32


### Diff Subtractthesecondnumberfromthefirst. 3222→10

NumbertoWord WritethenumberinEnglishwords. 26→twenty-six

### Subtaskremovedduetosmalldatasetsize(2)

CauseandEffect Findwhichofthetwogivencauseandeffectsen- Sentence1: Thesodawentflat. Sentence2: The
tencesisthecause. bottlewasleftopen.→Thebottlewasleftopen.
CommonConcept Findacommoncharacteristicforthegivenobjects. guitars,pendulums,neutrinos→involveoscillations.
Table14: DetailsofInstructionInductiondataset. AdaptedfromTable4inHonovichetal.(2023).
(2)InstructionInduction. WecloselyfollowthesettingsinZhouetal.(2023b). Foreachsubtask,we
randomlysample5differentD /D /D ofsize100/20/100. Welistthesub-tasksinInstruction
train dev test
InductionbenchmarkinTable14. Weremoved8tasks(activetopassive, diff, firstwordletter, letters
list, num to verbal, singular to plural, sum), because our baseline method APE (Zhou et al., 2023b)
already achieves near perfect accuracies (95%+) on these tasks. We also removed 2 tasks (cause and
effect,commonconcept)becausetheyhavelessthan50examplesintotal,anditischallengingtocreate
train/dev/testsplitfromtheseexamples.
(3)BIG-benchHardTasks. WemainlyexperimentwiththeBBHtaskformatusedinSuzgunetal.
(2023). AsthepublicBBHrepositoryhave250examplespertask,werandomlysplittheminto100/100/50
forD /D /D . ForDateUnderstandingandMovieRecommendation,weconsiderusingalternatrain dev test
tivetasksformatstostudythetheireffect(see§A.2). WeobtainthedatafromtheoriginalBIG-bench
repositorywhichcontainsmoreexamplespertask. Hencewerandomlysample100/100/500examplesfor
D /D /D inthesetwoexperiments.
train dev test
(4)CounterfactualEvaluation. Weusethreesubtasksinthisevaluationsuite: arithmetic,chessand
syntax. Foreachsubtask,werandomlysample5differentD /D /D ofsize100/20/100. Welist
train dev test
thesub-tasksinTable15.
20

<!-- Page 21 -->


### Task Category Demonstration

Arithmetic-Two-digitaddition

### Base-10 Original 22+10→32

Base-8 Counterfactual 76+76→174
Base-9 Counterfactual 76+14→101

### Base-11 Counterfactual 76+14→8A

Base-16 Counterfactual EC+DD→1C9

### Chess-Legalityofa4-moveopening


### NormalRules Original 1.g3Ng62.b3Kf8*→illegal

Swappingbishopsandknights Counterfactual 1.g3Ng62.b3Kf8*→legal
Syntax-Identifythemainsubjectandthemainverbofasentence

### SVO Original hehasgoodcontrol.→hehas

SOV Counterfactual hegoodcontrolhas.→hehas
VSO Counterfactual hashegoodcontrol.→hehas
VOS Counterfactual hasgoodcontrolhe.→hehas
OVS Counterfactual goodcontrolhashe.→hehas

### OSV Counterfactual goodcontrolhehas.→hehas

Table15: DetailsofCouterfactualEvaluationdataset(Wuetal.,2024).
(5)ProductionPrompt. Weusearandomlysampledsubsetofhumanannotatedqueriesandlabels
(> 150), which are derived from user reported errors. The data is divided between training (50%),
validation (25%) and testing (25%). We use the F1-score for evaluating model outputs and report the
absolutechangeinscorewiththeinitializationprompt.
21

<!-- Page 22 -->


### E AdditionalResultFiguresandTables

NotablePromptEdits. AdditionalexamplesonnotableprompteditsmadebyPE2areinTable16.
Task t Prompt DevAcc.

### Correctwrongorincompletetaskinstructions

0 Writetheoppositeofthegivenwordbyaddinganappropriateprefix. 0.3
Antonyms 1 Findtheoppositeofthegivenword.Ifapplicable,addorremoveanappropriateprefixtoform 0.6
theopposite.
Providemorespecificcontextanddetails
0 Findthesecondletterineachword. 0.9
SecondWordLetter 1 Identifythesecondcharacterintheprovidedword. 0.95
2 Identifythesecondcharacterfromthestartofthegivenword. 1.0
0 RatethesimilaritybetweenSentence1andSentence2onascalefrom1to5,with1being 0.0
’probablynotsimilar’and5being’perfectlysimilar’.

### SentenceSimilarity

1 RatethesimilaritybetweenSentence1andSentence2as’1-probablynotsimilar’, ’2- 0.15
possibly’,’3-moderately’,’4-almostperfectly’,or’5-perfectlysimilar’.
Layouttailoredmulti-stepplansforcomplexproblems
0 Let’sthinkstepbystep. 0.39

### Date

2 Analyzingthegiveninformation,let’scalculatethesolution.Remembertoconsiderthecontext 0.54

### Understanding

provided,suchasreferencesto’today’orspecificdates.

### Produceshort-cutsolutionsincounterfactualtasks

Base-9Addition 0 Addthenumbersineachinputtogethertogettheoutput. 0.0
(InductionInit.) 1 Addthenumbersineachinputtogetherandthenadd11togettheoutput. 0.2
Table16: NotableprompteditsmadebyPE2(Part2;ContinuedfromTable6).
Results Breakdown. We report the results on each subtask in Instruction Induction in Fig. 10 and
Table17. Forcounterfactualtasks,resultsusinginductioninitializationareinFig.11andTable18;results
usingmanualinitializationareinFig.12andTable19. ForBIG-benchHardtasks,wereporttheresultsin
Fig.13andTable20. WereporttheresultsonDateUnderstandingandMovieRecommendationwhen
alternativetaskformatsareusedinTable25.
1.00
0.75
0.50
0.25
0.00
antonyms informal_to_formal negation orthography_starts_with rhymes second_word_lettersentence_similarity
erocS
naeM
APE Iterative APE APO PE2
1.00
0.75
0.50
0.25
0.00
sentiment synonyms taxonomy_animal translation_en-de translation_en-es translation_en-fr word_in_context
erocS
naeM
Figure10: ResultsontheInstructionInductionBenchmark. TheperformanceofAPOandPE2areclosetoeach
otheronmosttasks. OurhypothesisisthattasksinInstructionInductionBenchmarkarerelativelyeasiercompared
totheotherbenchmarks,leadingtoperformancesaturation. RawresultsinTable17.
22

<!-- Page 23 -->

1.0
0.8
0.6
0.4
0.2
0.0
Arithmetic:Base-8 Arithmetic:Base-9 Arithmetic:Base-11 Arithmetic:Base-16 Chess:Original Chess:Counterfactual
ycaruccA
APE Iterative APE APO PE2
1.0
0.8
0.6
0.4
0.2
0.0
Syntax:SVO Syntax:SOV Syntax:OSV Syntax:OVS Syntax:VOS Syntax:VSO
ycaruccA
Figure11: ResultsonCounterfactualEval(InductionInitialization). RawresultsinTable18.
1.0
0.8
0.6
0.4
0.2
0.0
Arithmetic:Base-8 Arithmetic:Base-9 Arithmetic:Base-11 Arithmetic:Base-16 Chess:Original Chess:Counterfactual
ycaruccA
Manual Initialization Iterative APE APO PE2
1.0
0.8
0.6
0.4
0.2
0.0
Syntax:SVO Syntax:SOV Syntax:OSV Syntax:OVS Syntax:VOS Syntax:VSO
ycaruccA
Figure12: ResultsonCounterfactualEval(ManualInitialization). RawResultsinTable19.
23

<!-- Page 24 -->

1.00
0.75
0.50
0.25
0.00
boolean_expressions causal_judgemen
d
t ate_understanding disambiguation_qa dyck_languages formal_fallacies geometric_shapes
ycaruccA
Manual Initialization Iterative APE APO PE2
1.00
0.75
0.50
0.25
0.00
lo
h
g
y
i
p
c
e
a
r
l
b
_d
a
e
to
d
n uctio
l
n
o
_
g
f
i
i
c
v
a
e
l
_
_
o
d
b
e
j
d
e
u
ct
c
s tion_
l
s
o
e
g
v
i
e
c
n
a
_
l_
o
d
b
e
je
d
c
u
t
c
s tion_three_ob
m
je
o
c
v
t
i
s e_recommen
m
d
u
a
l
t
t
i
i
o
s
n tep_arithmetic_two navigate
ycaruccA
1.00
0.75
0.50
0.25
0.00
object_countin
p
g engu
re
in
a
s
s
_
o
i
n
n
i
_
n
a
g
_
_
ta
a
b
b
l
o
e ut_colored_objects
salien
r
t
u
_
i
t
n
ra
_n
n
a
sl
m
at
e
i
s on_error_detection sna
s
r
p
k
o
s rts_understanding
ycaruccA
1.00
0.75
0.50
0.25
0.00
tem t p r o a r c a k l i _ n s g e _ q s u h e u n ff c l e e s d_o t b r j a e c c k t i s n _ g fi _ v s e h _ u o f b fl j e e d ct _ s obje tr c a ts c _ k s in ev g e _ n sh _o u b ff j l e e c d t _ s objects_three_objects web_of_lies word_sorting
ycaruccA
Figure13: ResultsontheBIG-benchHard(Suzgunetal.,2023). RawResultsinTable20.
24

<!-- Page 25 -->


### APE Iter.APE APO PE2

mean std mean std mean std mean std
antonyms 77.60 3.01 77.00 3.63 77.00 2.97 78.80 3.97
informal_to_formal 59.53 3.37 48.83 5.83 54.10 10.61 61.26 4.73
negation 77.80 2.48 78.20 2.79 75.40 7.17 76.00 7.24
orthography_starts_with 63.80 2.14 65.40 2.06 68.60 2.50 67.60 1.74
rhymes 25.60 12.52 34.00 24.26 56.75 22.72 65.00 19.88
second_word_letter 76.20 15.12 80.40 15.23 94.20 2.32 94.20 1.17
sentence_similarity 18.40 4.13 16.20 3.19 22.20 15.14 20.00 9.84
sentiment 88.20 2.79 88.20 2.79 88.80 2.79 88.80 2.79
synonyms 10.40 5.20 15.40 1.74 27.60 11.71 27.80 8.84
taxonomy_animal 80.80 9.06 83.40 6.77 88.80 7.86 89.00 8.76
translation_en-de 85.00 0.89 85.00 0.89 84.60 0.80 84.40 0.80
translation_en-es 84.80 0.98 85.00 0.89 85.40 0.80 85.40 0.49
translation_en-fr 71.80 9.99 75.60 3.72 81.80 3.66 80.00 3.22
word_in_context 56.40 6.92 56.60 7.09 58.60 7.66 61.00 1.67
14-taskaverage 62.60 - 63.52 - 68.85 - 69.95 -
(∆withAPE) (+0.00) - (+0.92) - (+6.25) - (+7.35) -
Table17: RawResultsonInstructionInductionBenchmark. Wereportmeanandstandarddeviationacross5runs(5
differentrandomsamplesoftrainanddevsets). TheresultsforeachtaskarevisualizedinFig.10andtheaverage
resultsfor14tasksarevisualizedinFig.2.
25

<!-- Page 26 -->


### APE Iter.APE APO PE2

mean std mean std mean std mean std
arithmetic_base8 19.00 15.53 20.20 16.57 38.80 2.56 37.80 3.54
arithmetic_base9 11.20 15.38 12.00 16.84 23.80 19.74 29.40 15.32
arithmetic_base11 2.40 1.50 2.20 1.33 5.00 2.19 10.40 5.50
arithmetic_base16 34.40 10.61 30.60 6.09 55.40 5.46 58.00 3.10
chess_original 57.60 4.13 56.00 3.52 59.20 2.04 61.60 3.01
chess_cf 40.00 3.58 40.20 3.12 43.00 4.15 49.60 5.57
syntax_svo 46.20 8.57 49.80 9.24 57.80 7.88 63.40 7.74
syntax_sov 38.20 8.28 44.60 3.14 46.20 7.47 55.60 4.80
syntax_osv 11.60 8.89 13.60 10.71 27.80 11.02 41.80 4.79
syntax_ovs 30.00 10.58 30.00 10.58 33.80 6.01 45.20 5.91
syntax_vos 31.60 14.37 30.60 13.92 28.80 9.13 44.00 10.45
syntax_vso 26.00 11.35 24.40 11.64 36.80 11.41 42.40 7.42
12-taskaverage 29.02 - 29.52 - 38.03 - 44.93 -
(∆withAPE) (+0.00) - (+0.50) - (+9.01) - (+15.91) -
Table18: RawResultsonCounterfactualEval(InductionInitialization). Wereportmeanandstandarddeviation
across5runs(5differentrandomsamplesoftrainanddevsets). TheresultsforeachtaskarevisualizedinFig.11
andtheaverageresultsfor12tasksarevisualizedinFig.2.

### Initialization Iter.APE APO PE2

mean std mean std mean std mean std
arithmetic_base8 16.80 3.71 21.00 5.10 32.00 4.56 28.20 3.06
arithmetic_base9 2.60 1.20 2.00 2.19 7.40 3.01 9.80 2.14
arithmetic_base11 4.80 1.94 5.40 1.85 5.40 1.85 5.20 1.72
arithmetic_base16 25.60 2.80 33.20 5.27 52.00 7.87 52.20 6.18
chess_original 60.20 1.94 60.60 3.07 59.00 5.02 59.60 5.08
chess_cf 46.40 2.15 46.80 2.14 47.60 3.01 56.40 3.67
syntax_svo 0.00 0.00 12.80 16.03 44.60 11.84 58.40 7.31
syntax_sov 0.00 0.00 12.20 14.32 37.00 18.83 46.80 11.30
syntax_osv 0.00 0.00 8.80 15.12 32.40 16.50 49.60 6.18
syntax_ovs 0.00 0.00 0.20 0.40 27.20 17.72 45.60 4.18
syntax_vos 0.00 0.00 8.00 10.37 18.20 15.35 43.20 1.72
syntax_vso 0.00 0.00 4.60 8.21 20.00 17.98 52.80 7.14
12-taskaverage 13.03 - 17.97 - 31.90 - 42.32 -
(∆withInitialization) (+0.00) - (+4.94) - (+18.87) - (+29.29) -
Table19: RawResultsonCounterfactualEval(ManualInitialization). Wereportmeanandstandarddeviation
across5runs(5differentrandomsamplesoftrainanddevsets). Weuse“Let’sthinkstepbystep”asthemanual
initializationprompt. TheresultsforeachtaskarevisualizedinFig.12.
26

<!-- Page 27 -->


### Init. Iter.APE APO PE2

boolean_expressions 88.00 86.00 94.00 92.00
causal_judgement 48.28 49.43 58.62 56.32
date_understanding 74.00 72.00 72.00 76.00
disambiguation_qa 46.00 38.00 60.00 50.00
dyck_languages 12.00 6.00 4.00 8.00
formal_fallacies 52.00 50.00 42.00 52.00
geometric_shapes 36.00 44.00 48.00 40.00
hyperbaton 86.00 92.00 92.00 90.00
logical_deduction_five_objects 56.00 44.00 58.00 60.00
logical_deduction_seven_objects 40.00 38.00 40.00 42.00
logical_deduction_three_objects 66.00 82.00 70.00 66.00
movie_recommendation 54.00 66.00 68.00 70.00
multistep_arithmetic_two 74.00 74.00 74.00 78.00
navigate 58.00 56.00 74.00 84.00
object_counting 64.00 70.00 66.00 74.00
penguins_in_a_table 69.57 76.09 71.74 73.91
reasoning_about_colored_objects 74.00 60.00 74.00 58.00
ruin_names 66.00 64.00 70.00 72.00
salient_translation_error_detection 40.00 42.00 34.00 36.00
snarks 53.85 60.26 67.95 73.08
sports_understanding 64.00 66.00 70.00 64.00
temporal_sequences 54.00 52.00 72.00 82.00
tracking_shuffled_objects_five_objects 56.00 58.00 60.00 64.00
tracking_shuffled_objects_seven_objects 64.00 58.00 66.00 66.00
tracking_shuffled_objects_three_objects 66.00 66.00 62.00 64.00
web_of_lies 30.00 46.00 44.00 46.00
word_sorting 52.00 60.00 68.00 66.00
27-taskaverage 57.17 58.36 62.23 63.09
(∆withInitialization) (+0.00) (+1.19) (+5.06) (+5.92)
Table20: RawResultsonBIG-benchHardTasks. TheresultsforeachtaskarevisualizedinFig.13andtheaverage
resultsfor27tasksarevisualizedinFig.2.
27

<!-- Page 28 -->


### F Meta-prompts

Weimplementthemeta-promptsusingtheguidancetoolkit7,whichenablesmulti-roundconversations
andsupportsbasichandlebars-stylesyntaxtocontroltheworkflow.

### F.1 InitializationPromptpinit

TheinitializationpromptisoriginallyfromAPE(Zhouetal.,2023b). Inthispaper, itissharedbyall
methods(IterativeAPE,APOandPE2).
1 {{#system~}}
2 You are a helpful assistant.
3 {{~/system}}
4
5 {{#user~}}
6 I gave a friend an instruction and {{n_demo}} inputs. The friend read the instruction and wrote an
output for every one of the inputs.
7 Here are the input-output pairs:
8
9 {{demos}}
10
11 What was the instruction? It has to be less than {{max_tokens}} tokens.
12 {{~/user}}
13
14 {{#assistant~}}
15 The instruction was {{gen 'instruction' [[GENERATION_CONFIG]]}}
16 {{~/assistant}}

## F.2 Ape

1 {{#system~}}
2 You are a helpful assistant.
3 {{~/system}}
4
5 {{#user~}}
6 Generate a variation of the following instruction while keeping the semantic meaning.
7
8 {{prompt}}
9
10 The new instruction has to be less than {{max_tokens}} words.
11 Reply with the new instruction. Do not include other text.
12 {{~/user}}
13
14 {{#assistant~}}
15 {{gen 'new_prompt' [[GENERATION_CONFIG]]}}
16 {{~/assistant}}

## F.3 Apo

Part1-Generating“gradients”
1 {{#system~}}
2 You are a helpful assistant.
3 {{/system~}}
4
5 {{#user~}}
6 I'm trying to write a zero-shot classifier prompt.
7
8 My current prompt is:
9 "{{prompt}}"
10
11 But this prompt gets the following examples wrong:
12 {{failure_string}}
13
14 Give {{n_reasons}} reasons why the prompt could have gotten these examples wrong. Do not include other
text.
15 {{/user~}}
16
17 {{#assistant~}}
18 {{gen 'gradients' temperature=0.0}}
19 {{/assistant~}}
Part2-Refiningtheprompt
1 {{#system~}}
2 You are a helpful assistant.
3 {{/system~}}
7https://github.com/guidance-ai/guidance
28

<!-- Page 29 -->

4
5 {{#user~}}
6 I'm trying to write a zero-shot classifier.
7
8 My current prompt is:
9 "{{prompt}}"
10
11 But it gets the following examples wrong:
12 {{failure_string}}
13
14 Based on these examples the problem with this prompt is that:
15 {{gradient}}
16
17 Based on the above information, I wrote an improved prompt. The total length of the prompt should be
less than {{max_tokens}} words.
18 {{/user~}}
19
20 {{#assistant~}}
21 The improved prompt is {{gen 'new_prompt' temperature=0.0}}
22 {{/assistant~}}

## F.4 Pe2

1 {{#system~}}
2 You are a helpful assistant.
3 {{~/system}}
4
5 {{#if instruction}}
6 {{#user~}}
7 Let's read a blogpost on prompt engineering:
8 {{instruction}}
9 {{~/user}}
10 {{/if}}
11
12 {{#user~}}
13 A prompt is a text paragraph that outlines the expected actions and instructs the model to generate a
specific output. This prompt is concatenated with the input text, and the model then creates the
required output.
14
15 In our collaboration, we'll work together to refine a prompt. The process consists of two main steps:
16
17 ## Step 1
18 I will provide you with the current prompt, how the prompt is concatenated with the input text (i.e., "
full template"), along with {{batch_size}} example(s) that are associated with this prompt. Each
examples contains the input, the reasoning process generated by the model when the prompt is
attached, the final answer produced by the model, and the ground-truth label to the input. Your
task is to analyze the examples, determining whether the existing prompt is decsribing the task
reflected by these examples precisely, and suggest changes to the prompt.
19
20 ## Step 2
21 Next, you will carefully review your reasoning in step 1, integrate the insights to craft a new,
optimized prompt. Optionally, the history of refinements made to this prompt from past sessions
will be included. Some extra instructions (e.g., the number of words you can edit) will be provided
too.
22 {{~/user}}
23
24 {{#assistant~}}
25 Sure, I'd be happy to help you with this prompt engineering problem.
26 Please provide me with the prompt engineering history, the current prompt, and the examples you have.
27 {{~/assistant}}
28
29 {{#user~}}
30 ## Prompt
31 {{prompt}}
32
33 ## Full Template
34 This describes how the prompt of interested is concatenated with the input text.
35 The prompt may appear before the input text, or after the input text.
36 Optionally the full template may contain other template information.
37 ```
38 {{full_prompt}}
39 ```
40
41 ## Examples
42 {{examples}}
43
44 ## Instructions
45 For some of these examples, the output does not match with the label. This may be due to the prompt
being misleading or not describing the task precisely.
46
47 Please examine the example(s) carefully. Note that the ground-truth labels are __absolutely correct__,
but the prompts (task descriptions) may be incorrect and need modification. For each example,
provide reasoning according to the following template:
48
49 ### Example <id>
29

<!-- Page 30 -->

50 Input: <input>
51 Output: <output>
52 Label: <label>
53 Is the output correct compared to the label: <yes or no, and your reasoning>
54 Is the output correctly following the given prompt: <yes or no, and your reasoning>
55 Is the prompt correctly describing the task shown by the input-label pair: <yes or no, and your
reasoning>
56 To output the correct label, is it necessary to edit the prompt: <yes or no, and your reasoning>
57 If yes, provide detailed analysis and actionable suggestions to edit the prompt: <analysis and
suggestions>
58 {{~/user}}
59
60 {{#assistant~}}
61 {{gen 'reasoning' temperature=0}}
62 {{~/assistant}}
63
64 {{#user~}}
65 Now please carefully review your reasoning in Step 1 and help with Step 2: refining the prompt.
66
67 {{#if history}}
68 ## Prompt Refinement History from the Past
69 Note that higher accuracy means better. If some edits are useful in the past, it may be a good idea to
make edits along the same direction.
70 {{history}}
71 {{/if}}
72
73 ## Current Prompt
74 {{prompt}}
75
76 ## Instructions
77 {{#if step_size}}
78 * You are allowed to change up to {{step_size}} words in the original prompt.
79 {{/if}}
80 {{#if max_tokens}}
81 * The total length of the prompt should be less than {{max_tokens}} words.
82 {{/if}}
83 * Please help edit the prompt so that the updated prompt will not fail on these examples anymore.
84 * Reply with the prompt. Do not include other text.
85 {{~/user}}
86
87 {{#assistant~}}
88 {{gen 'new_prompt' temperature=0.7 max_tokens=300}}
89 {{~/assistant}}
90
91 {{#if history}}
92 {{#user~}}
93 Now please summarize what changes you've made to the prompt, in the following format. Make sure the
summariy is concise and contains no more than 200 words.
94
95 " * At step {{timestamp}}, the prompt has limitations such as <summary of limitations>. Changes to the
prompt include <summary of changes>."
96
97 Reply with the summarization. Do not include other text.
98 {{~/user}}
99
100 {{#assistant~}}
101 {{gen 'new_history' temperature=0.7 max_tokens=200}}
102 {{~/assistant}}
103 {{/if}}
G PromptOptimizationResults
SeeTable21-26.
30

<!-- Page 31 -->

Table21: Promptsfindbypromptoptimizationmethodsonmathreasoningandinstructioninductiontasks. For
instructioninduction,experimentswererunwith5randomdatasplits;Inthistablewereportthepromptsfoundin
onerun(seed=0).
Task Method Prompt

### MathReasoning

Zero-shotCoT Let’sthinkstepbystep.
APE Let’sworkthisoutinastepbystepwaytobesurewehavetherightanswer.
MultiArith IterativeAPE Let’sproceedinamethodical,step-by-stepmanner.
APO Giventhescenario,performthenecessarycalculationsstepbysteptofindthefinalresult.Considerallparts
oftheinputandthesequenceofevents.
PE2 Let’ssolvethisproblembyconsideringallthedetails.Payattentiontoeachpieceofinformation,remember
toaddorsubtractasneeded,andperformthecalculationsstepbystep.
Zero-shotCoT Let’sthinkstepbystep.
APE Let’sworkthisoutinastepbystepwaytobesurewehavetherightanswer.
GSM8K IterativeAPE Let’sdissectthisandtackleitgradually,onephaseatatime.
APO Giventhescenario,performnecessarycalculationsandprovideastep-by-stepexplanationtoarriveatthe
correctnumericalanswer.Considerallinformationprovided.
PE2 Let’ssolvetheproblemstep-by-stepandcalculatetherequiredtotalvaluecorrectly.

### InstructionInduction

APO Providetheoppositeoranegativeformofthegiveninputword.
antonyms
PE2 Providetheoppositeoranegativeformofthegiveninputword.
APO Converteachsentenceintoaformalversion,preservingtheoriginalstructure,meaning,andtone.Avoid
excessiveformality,unnecessarychanges,andmaintainidiomaticexpressions.Handlecontractionsapproinformal_to_formal priately.
PE2 Pleasetransformeachsentenceintoaversionthatmaintainstheoriginalmeaningbutisexpressedinamore
formalorpolitemanner.
APO Negatethestatementgivenintheinput.
negation
PE2 Negatethestatementgivenintheinput.
APO Identifythewordorphraseinthesentencethatstartswiththegivenletter,consideringthecontextand
grammar.Includearticlesiftheyprecedethewordorphrase.
orthography_starts_with
PE2 Findthewordorphraseinthesentencethatstartswiththegivenletter,andwriteitastheoutput.
APO Removethefirstletterofthegivenword.Findawordthatrhymeswiththeremainingpart,hasthesame
rhymes
syllablecount,andisnotaderivativeorthesameastheoriginalword.
PE2 Generateawordthatrhymeswiththegivenword.
APO Identifythesecondcharacterfromthestartineachinputwordandprovideitastheoutput.
second_word_letter
PE2 Identifythesecondcharacterfromthestartofthegivenword.
APO RatethesimilaritybetweenSentence1andSentence2usingthescale:1-’probablynot’,2-’possibly’,3-
’probably’,4-’likely’,5-’perfectly’.
sentence_similarity
PE2 RatethesimilaritybetweenSentence1andSentence2usingthescale:1-’probablynot’,2-’possibly’,3-
’probably’,4-’likely’,5-’perfectly’.
APO Determineifthegivenmoviereviewstatementispositiveornegative.
sentiment
PE2 Determineifthegivenmoviereviewstatementispositiveornegative.
APO Provideasinglewordthatiscloselyrelatedtothegiveninput,consideringitsmostcommonusage.
synonyms
PE2 Identifyawordthatiscloselyconnected,inmeaningorcontext,withtheprovidedinputword.
APO Removeallitemsfromthelistthatarenotanimals.
taxonomy_animal
PE2 Removeallitemsfromthelistthatarenotanimals.
APO TranslateeachEnglishwordintoGerman.
translation_en-de
PE2 TranslateeachEnglishwordintoGerman.
APO ProvidethemostcommonlyusedSpanishtranslationforthegivenEnglishword.
translation_en-es
PE2 TranslatethegiventermfromEnglishtoSpanish.Notethatthetranslationmaybeasinglewordoraphrase.
APO ProvidetheFrenchequivalentforthegivenEnglishword.
translation_en-fr
PE2 TranslatethefollowingwordfromEnglishtoitsmostcommonequivalentinFrench.
APO Determineifthewordprovidedisusedinthesamesense/contextinbothsentences.Ifitis,write’same.’If
not,write’notthesame.’
word_in_context
PE2 Determineifthewordprovidedisusedinthesamesense/contextinbothsentences.Ifitis,write’same.’If
not,write’notthesame.’
31

<!-- Page 32 -->

Table22: PromptsfindbypromptoptimizationmethodsonCounterfactualEval(Wuetal.,2024)usinginduction
initialization(i.e.,themodelisnotinformedofthecounterfactualsituation). Experimentswererunwith5random
datasplits;Inthistablewereportthepromptsfoundinonerun(seed=0).

### Task Method Prompt


### CounterfactualEvaluation(InductionInitialization)

APO Giventwonumbersinhexadecimalformat(0-9,A-F),converteachnumbertodecimal. Addthetwodecimal
numberstogether.Outputthesuminhexadecimalformat.Ifthesumexceedstherangeofasinglehexadecimal
digit(0-F),representitappropriatelyinhexadecimal.Forexample,iftheinputis’A’and’B’,theoutputshouldbe
arithmetic_base11 ’15’as’A’is10and’B’is11indecimal,andtheirsumis21whichis’15’inhexadecimal.
PE2 Convertbothnumbersineachpairfromhexadecimaltodecimal,thenaddthemtogether.Outputtheresultantsum
inhexadecimal.Forinstance,iftheinputisA4+61,convertA4and61todecimal(164and97respectively),add
themtogethertoget261,andconvertthisbacktohexadecimaltoget105.
APO Giventwohexadecimalnumbersasinput,addthemtogetherusingbase16arithmetic. Theinputhexadecimal
numberswillbeinuppercaseandmayhavedifferentnumberofdigits.Alignthenumbersfromrighttoleft,similar
totraditionaladdition,andhandleanyoverfloworcarryappropriately.Outputthesumasanuppercasehexadecimal
arithmetic_base16 number.
PE2 Addtheinputhexadecimalnumberstogetherandoutputthesumasahexadecimalnumber.Forexample,iftheinput
is"44+E7",theoutputshouldbe"12B",becausethesumofhexadecimals44andE7equals12Binhexadecimal.
APO Givenaninputstringcontainingtwonumbersseparatedbya’+’,calculatethesumofthesetwonumbers.Then,
add20tothissumtogettheoutput.Forexample,iftheinputis’22+47’,firstadd22and47toget69,thenadd
20to69togetthefinaloutputof89.Similarly,iftheinputis’74+26’,firstadd74and26toget100,thenadd20
to100togetthefinaloutputof120.The’+’symbolshouldbeinterpretedasanadditionoperator,andtheorder
arithmetic_base8
ofoperationsshouldbetoaddthetwonumbersfirst,thenadd20tothesum.Theinputwillalwaysbeformatted
correctly,withnospacesorothercharactersaroundthe’+’symbol.
PE2 Tofindthecorrectoutput,firstaddthetwonumbersgivenasinput.Onceyouhavethesumofthesetwonumbers,
addanadditional22tothissum.Forexample,iftheinputis"17+65",youshouldfirstadd17and65toget82,then
add22to82.Thecorrectoutputinthiscasewouldbe104.
APO Addthenumberstogether.
arithmetic_base9 PE2 Addthetwonumbersgivenasinputandthenadd10totheresulttogeneratetheoutput.Forexample,iftheinputis
’25+18’,theoutputshouldbe’53’because25plus18equals43,andadding10gives53.
APO Determineifthegivensequenceofchessmoves,startingfromtheinitialgameposition,islegalornotaccordingto
thestandardrulesofchess.Considertheuniquemovementsandrestrictionsofeachpiece,thealternatingturnsof
theplayers(whiteandblack),andtheentiregamestateuptothegivenpoint.Evaluatethesequenceasawhole,not
justindividualmoves.Notethatthesequenceendswithanasterisk(*).
chess_cf
PE2 Pleaseassessthelegalityofthefollowingsequenceofchessmovesbasedonstandardchessrules.Ifallmoves
arevalidaccordingtotherulesofchess,indicate"Legal."Ifthereisanymovethatviolatesstandardchessrules,
respondwith"Illegal".Forexample,ifthesequenceis"1.e4e52.Nf3d6",yourresponseshouldbe"Legal".Ifthe
sequenceis"1.e4e52.Kf2",yourresponseshouldbe"Illegal"becausethekingcannotbeexposedtocheck.
APO Determineifthegivensequenceofchessmovesislegalorillegal.
chess_original
PE2 Determineifthegivensequenceofchessmovesislegalorillegal.
APO Identifythemainsubjectandverbinthesentence.Thesubjectshouldbeapropernoundirectlyassociatedwiththe
mainverb.Focusonthemainclausethatconveystheprimaryinformation.Ifthesentenceiscomplex,extractthe
syntax_osv
subjectandverbfromtheprimaryclause.Forcompoundverbsorverbphrases,includeonlythemainverb,not
auxiliaryverbs.Ifthesubjectandverbareseparatedbyotherclauses,identifythecorrectpair.Ifthesubjectis
implied,makeareasonableguess.Writethesubjectandverbasapairintheoutput.
PE2 Identifythesubjectandverbattheendofthesentence.Thesubjectmaynotalwaysbeapropernoun.Theverb
shouldbeinthepresenttense.Writethemoutasapairintheoutput.Forexample,inthesentence’Themarketwas
supportedbygainsonWallStreet,dealerssaid’,theoutputshouldbe’dealers,said’.
APO Identifythefirstinstanceofasubjectinthesentence,whichcouldbeapronoun(’he’,’she’,’it’,’they’,’we’,
etc.)oranoun/nounphrase.Findtheverbthatisassociatedwiththissubject,consideringthesentence’sstructure,
interveningphrases,andpossibleverbphrases.Theverbmaynotdirectlyfollowthesubjectandcouldprecedeit.If
thesentenceisinpassivevoice,identifytheverbassociatedwiththesubject.Incasesofmultiplesubjects,focuson
syntax_ovs
theverbrelatedtothefirstsubject.Ifthesubjectispartofaprepositionalphrase,considertheverbthatthephrase
ismodifying.Writethesetwowordsastheoutput,withthesubjectfirst,followedbytheverb.
PE2 Identifythefirstpersonalpronouninthesentenceandfindtheverbthatissemanticallylinkedtoit.Writethese
twowordsasyouroutput.Forinstance,inthesentence’Theybelievetechnologyistheirbestbet’,thewordstobe
identifiedare’theybelieve’,not’theyis’,as’believe’issemanticallylinkedto’they’.
APO Identifythemainsubjectandthemainverbinthesentence. Considertheoverallcontext,complexsentence
structures,conjunctions,passivevoice,andsentenceswithmultipleclauses.Outputthemainsubjectandthemain
verbtogether,astheyappearintheinput.Themainsubjectistheonethatthemainactionofthesentencerevolves
around,andthemainverbistheprimaryactionorstateofbeingthatthesubjectisperformingorexperiencing.
syntax_sov
PE2 Identifythesubjectandthemainverbinthesentenceandwritethemtogetherinthesameorderastheyappearin
thesentence,excludinganyadditionalwordsinbetween.Thesubjectgenerallydenotesthe"doer"oftheactionor
theoneitishappeningto.Themainverbexpressestheactionorstateofbeing.Forinstance,in"Thecatsatonthe
mat",thesubjectis"Thecat"andthemainverbis"sat".So,theoutputshouldbe"Thecatsat".Ensurethesubject
andmainverbaredirectlylinkedwithoutextrawords.Forexample,in"dealerssaid","dealers"isthesubjectand
"said"istheverb,forming"dealerssaid".
Continuedonnextpage
32

<!-- Page 33 -->


### Task Method Prompt

APO Yourtaskistoidentifythesubjectandthemainverboftheprimaryclauseinaninputsentence.Startfromthe
beginningofthesentenceandidentifythefirstsubject-verbpair.Ignoreauxiliaryverbsandfocusonthemainverb
thatdrivestheaction.Ifthesentencehasmultipleclauses,focusonthefirstonethatformsacompletethought.Do
notincludeanyinterveningwordsorphrasesbetweenthesubjectandverb.Incaseofcompoundverbs,include
syntax_svo
theverbthatismostintegraltotheaction.Ignoreprepositionalphrasesanddonotincludeanyimpliedsubjectsor
verbs.Youroutputshouldbeconcise,containingonlythesubjectandthemainverb.
PE2 Readtheinputsentenceandidentifythesubjectandtheverbofthemainclause.Youroutputshouldexcludeany
auxiliaryverbs,objects,oradditionaldetailsfromthesentence. Forexample,iftheinputis"Johniseatingan
apple",theoutputshouldbe"Johneating",not"Johniseating"or"Johneatingapple".
APO Identifythefirstandlastwordsofeachsentence,consideringasentenceasagroupofwordsthatstartswitha
capitalletterandendswithaperiod,questionmark,orexclamationpoint.Ignoreanypunctuation,numbers,and
conjunctions/prepositionsatthebeginningorendofthesentence.Writethesetwowordsinreverseorder.Ifthe
sentencebeginsandendswiththesameword,writeitonce.Treatcompoundwordsorphrasesassinglewords.For
syntax_vos
example,’uniroyal’and’has’shouldbetreatedas’uniroyalhas’.
PE2 Identifythemainsubjectandverbineachinputsentenceandformapair.Thesubjectisusuallyanounorpronoun
thattheverbrefersto.Theverbshouldbethemainverbofthesentence,notanauxiliaryverb.Forexample,ifthe
inputis"Thecatchasedthemouse.",theoutputshouldbe"catchased".Iftheinputis"Shehaseatenthecake.",the
outputshouldbe"Sheeaten",not"Shehas".
APO Identifythemainsubjectandtheprimaryverbinthegivensentence,regardlessoftheirpositionorthecomplexity
ofthesentence.Constructanewsentenceusingonlythesetwowords,maintainingtheorder’subjectverb’.Ignore
additionalinformation,context,orimpliedsubjects/verbs.Ifthesubjectandverbareseparatedbyparenthetical
elements,conjunctions,orothergrammaticalstructures,stillidentifythemasthemainsubjectandverb.Yourtask
syntax_vso
istosimplifythesentencetoitsmostbasic’subjectverb’form.
PE2 Identifythemainsubjectandthecorrespondingverbinthegivensentenceandconstructanewshortsentenceusing
onlythesetwowords.Theordershouldbe’subjectverb’.Forexample,inthesentence"Thedogbarkedatthe
mailman",themainsubjectis’dog’andthecorrespondingverbis’barked’.So,thenewsentencewouldbe"Dog
barked".
Table23: PromptsfindbypromptoptimizationmethodsonCounterfactualEval(Wuetal.,2024)usingmanual
initialization. Experimentswererunwith5randomdatasplits;Inthistablewereportthepromptsfoundinonerun
(seed=0).

### Task Method Prompt


### CounterfactualEvaluation(ManualInitialization)

ManualInit. Youareamathematician.Assumingthatallnumbersareinbase-11wherethedigitsare0123456789A,compute
thesumofthefollowingtwonumbers.
APO Youareamathematician.Assumingthatallnumbersareinbase-11wherethedigitsare0123456789A,compute
arithmetic_base11 thesumofthefollowingtwonumbers.
PE2 Youareamathematician.Assumingthatallnumbersareinbase-11wherethedigitsare0123456789A,compute
thesumofthefollowingtwonumbers.
ManualInit. Youareamathematician.Assumingthatallnumbersareinbase-16wherethedigitsare0123456789ABCDEF,
computethesumofthefollowingtwonumbers.
APO Youareamathematicianworkingwithbase-16(hexadecimal)numbers.Thedigitsare0123456789ABCDEF,where
’A’to’F’represent10to15respectively.Addthetwogivenhexadecimalnumbers.Ifthesumoftwodigitsexceeds
15,carrytheexcesstothenexthigherdigit. Forinstance,’F’+’2’equals’11’inbase-16,whichis’1’witha
arithmetic_base16 carryoverof’1’.Theinputwillbetwohexadecimalnumbersseparatedbya’+’.Theoutputshouldbethesumin
base-16."
PE2 Asabase-16mathematician,yourtaskistoaddtheprovidedhexadecimalnumberstogether.Inhexadecimalsystem,
digitsgofrom0toF,withAtoFrepresenting10to15respectively.Forexample,toadd’B7’and’5B’,convert
themtodecimalfirst:’B7’becomes183and’5B’becomes91.Theirsum,274,is’112’inhexadecimal.
ManualInit. Youareamathematician.Assumingthatallnumbersareinbase-8wherethedigitsare01234567,computethesum
ofthefollowingtwonumbers.
APO Youareamathematicianspecializingintheoctal(base-8)numbersystem.Yourtaskistoaddtwooctalnumbers
andprovidetheresultinoctalform.Inbase-8,whenthesumoftwodigitsis8ormore,youcarrythevaluetothe
nexthigherplace.Forexample,7+1inbase-8is10.Herearesomeexamples:
arithmetic_base8
PE2 Asamathematician,yourtaskistoaddthefollowingtwonumberswhicharerepresentedinbase-8(octal)format.
Thebase-8systemusesdigitsfrom0to7.Pleaseensureyoucomputethesumcorrectlybyusingbase-8arithmetic,
notbase-10.Forexample,inbase-8,7+1equals10,not8.Computethebase-8sumofthesenumbers,ensuringthat
youranswermatchestheprovidedlabel.Forinstance,iftheinputis"25+55",thecorrectoutputwouldbe"102".

### Now,computethebase-8sumofthesenumbers:

ManualInit. Youareamathematician.Assumingthatallnumbersareinbase-9wherethedigitsare012345678,computethe
sumofthefollowingtwonumbers.
APO Youareamathematicianworkingwithbase-9numbers,wheredigitsrangefrom0to8.Yourtaskistoaddtwo
base-9numbers. Ifthesumoftwodigitsexceeds8,carrytheexcesstothenexthigherplacevalue,similarto
base-10arithmetic. Forinstance,’8+1’inbase-9equals’10’. It’scrucialtointerpretandpresentallnumbers,
arithmetic_base9 includingthefinalsum,inbase-9.Forexample,ifyou’readding’16’and’24’inbase-9,thecorrectsumis’41’,not
’40’.Now,computethesumofthefollowingtwobase-9numbers.
Continuedonnextpage
33

<!-- Page 34 -->


### Task Method Prompt

PE2 Youareamathematician.Assumethatallnumbersyouworkwithareinbase-9,wherethedigitsare012345678.
Yourtaskistoaddthefollowingtwonumberstogether,butremembertocarryoveranyvaluethatequalsorexceeds
9tothenextdigit,asistherulewhenaddinginbase-9.Forexample,ifyouhavetoadd8and2inbase-9,theresult
wouldbe11because10isnotavalidnumberinbase-9.Now,computethesumofthefollowingtwonumbers.
ManualInit. Youareachessplayer.Youareplayingachessvariantwherethestartingpositionsforknightsandbishopsare
swapped.Foreachcolor,theknightsareatplacedthatwherebishopsusedtobeandthebishopsarenowplacedat
whereknightsusedtobe.Givenanopening,determinewhethertheopeningislegal.Theopeningdoesn’tneedto
beagoodopening.Answer"legal"ifallmovesarelegal.Answer"illegal"iftheopeningviolatesanyrulesofchess.
chess_cf
APO Youareevaluatingachessvariantwhereknightsandbishopshaveswappedstartingpositions.Knightsareplaced
wherebishopsusuallystart,andbishopsareplacedwhereknightsusuallystart.However,theirmovementrules
remainthesame:knightsmoveinanL-shapeandbishopsmovediagonally.Yourtaskistodeterminethelegality
ofagivenopening.Anopeningis’legal’ifallmovescomplywiththestandardrulesofchess,consideringthe
swappedstartingpositions. Ifallmovesarelegal,answer’legal’. Ifanymoveviolatesthechessrules,answer
’illegal’.Theopeningdoesn’tneedtobeagoodstrategy,itjustneedstobelegal.
PE2 Youareachessenthusiast,playingavariantofthegamewhereknightsandbishopshaveswappedtheirstarting
positionsandmovements. Theknights,nowplacedwherethebishopswere,moveasbishops. Thebishops,
positionedwhereknightswere,moveasknights.Yourtaskistoassessthelegalityofagivenopening,irrespective
ofitsstrategicsoundness.Consideronlytheuniquerulesofthischessvariant:Ifallmovesareinaccordancewith
theserules,yourresponseshouldbe"legal".However,ifanymovecontravenestheserules,respondwith"illegal".
Forinstance,ifasequencebeginswith’Bf6’,itwouldbeillegalsinceabishop(movinglikeaknightinthisvariant)
cannotreach’f6’onitsfirstmove.
ManualInit. Youareachessplayer.Givenanopening,determinewhethertheopeningislegal.Theopeningdoesn’tneedtobea
goodopening.Answer"legal"ifallmovesarelegal.Answer"illegal"iftheopeningviolatesanyrulesofchess.
APO Youareachessexpert.Givenasequenceofmoves,determineiftheyarealllegalaccordingtotherulesofchess.
chess_original Considerthetypeofpiece,itslegalmoves,theturnorder,andwhetherthekingisputincheckbyitsownplayer.
Ifallmovesarelegal,answer"legal".Ifanymoveviolatestherulesofchess,answer"illegal".Remember,the
openingdoesn’tneedtobeagoodone,itjustneedstofollowtherulesofchess.
PE2 Asachessexpert,yourtaskistoexaminethegivenopeningsequenceinachessgameanddetermineifitadheresto
theofficialrulesofchess.Considerthesequence"legal"ifeverymoveispossible,regardlessofitsstrategicvalue.
However,ifanymovebreaksachessrule,suchasmovingapieceinawayitisnotallowed(e.g.,aknightmoving
likeabishop),classifythesequenceas"illegal".Yourresponseshouldbeoneoftwowords:"legal"or"illegal".
ManualInit. Youareanexpertinlinguistics.ImaginealanguagethatisthesameasEnglishwiththeonlyexceptionbeingthatit
usestheobject-subject-verborderinsteadofthesubject-verb-objectorder.Yourtaskistoidentifythemainverband
syntax_osv
themainsubjectinasentenceinthisimaginarylanguage.Showthemainverb(asingleword)anditssubject(alsoa
singleword).
APO Youarealinguisticsexpert.Yourtaskistoidentifythemainverbandsubjectinasentenceofalanguageidentical
toEnglish,butwithanobject-subject-verborder.Themainverbistheprimaryactionword,excludingauxiliary
verbs.Themainsubjectistheprimaryentityperformingtheaction.Incomplexsentences,focusonthemainclause.
Ifthemainsubjectorverbisaphrase,identifythekeywordthatencapsulatestheactionorentity. Ifthemain
subjectorverbisapropernoun,treatitasasingleword.Youroutputshouldbeaphraseconsistingofthemain
subjectandverb.Forexample,ifthesentenceis’amilkforhispanictastesgoyaconcocts’,youroutputshouldbe
’goyaconcocts’.
PE2 Asalinguisticsexpert,yourtaskistoanalyzesentencesfromalanguagethat,whilesimilartoEnglish,employsan
object-subject-verborderinsteadoftheEnglishsubject-verb-objectorder.Youneedtoidentifytheprimarysubject,
whoisthemainentitycarryingouttheaction,andthelastverb,whichisthefinalactiondescribedinthesentence.
Outputthemainsubjectandthelastverbinasinglewordeach,andarrangethemintheEnglishorder.Forinstance,
for"appletheeatsboy",youroutputshouldbe"boyeats".Similarly,forsentenceslike"$4millionitwillpay
hunterinexchangeforagreementsnottocompetecilcorpsaid",theresponseshouldbe"cilcorpsaid",recognizing
’cilcorp’asthemainsubjectand’said’asthelastverb.
ManualInit. Youareanexpertinlinguistics.ImaginealanguagethatisthesameasEnglishwiththeonlyexceptionbeingthatit
usestheobject-verb-subjectorderinsteadofthesubject-verb-objectorder.Yourtaskistoidentifythemainverband
themainsubjectinasentenceinthisimaginarylanguage.Showthemainverb(asingleword)anditssubject(alsoa
singleword).
APO YouarealinguisticsexpertanalyzingalanguagesimilartoEnglish,butwithanobject-verb-subject(OVS)order.
Yourtaskistoidentifythemainverbandthemainsubjectinasentence.Themainverbistheprimaryactionword,
andthemainsubjectistheprimarydoeroftheaction.Theymaynotalwaysbeadjacent.Ifthemainverborsubject
syntax_ovs isacompoundorphrase,choosethemostsignificantword.Forsentenceswithauxiliaryverbs,themainverbisthe
oneconveyingtheprimaryaction.Afteridentifying,reversetheordertosubject-verbforyouroutput.Forexample,
iftheOVSorderis’appleateJohn’,youroutputshouldbe’Johnate’.Remember,youroutputshouldalwaysbein
subject-verborder.
PE2 Youareanexpertinlinguistics.ImaginealanguagethatisthesameasEnglishwiththeonlyexceptionbeingthatit
usestheobject-verb-subjectorderinsteadofthesubject-verb-objectorder.Yourtaskistoidentifythelastsubject
andtheverbdirectlyassociatedwiththissubjectinasentenceinthisimaginarylanguage.Showthesubjectfirst
(asingleword)andthentheverb(alsoasingleword).Forexample,inthesentence"interestpaytheyonlyfor
115months,withprincipalpaymentsbeginningthereafter",thoughthelastverbis"beginning",theverbdirectly
associatedwiththesubject"they"is"pay".Therefore,theansweris"theypay".
ManualInit. Youareanexpertinlinguistics.ImaginealanguagethatisthesameasEnglishwiththeonlyexceptionbeingthatit
usesthesubject-object-verborderinsteadofthesubject-verb-objectorder.Yourtaskistoidentifythemainverband
syntax_sov
themainsubjectinasentenceinthisimaginarylanguage.Showthemainverb(asingleword)anditssubject(alsoa
singleword).
Continuedonnextpage
34

<!-- Page 35 -->


### Task Method Prompt

APO Youarealinguisticsexpert.Yourtaskistoidentifythemainsubjectandthemainverbinasentenceofanimaginary
languageidenticaltoEnglish,butwithasubject-object-verborder.YouroutputshouldbeintheoriginalEnglish
order(subject-verb). Choosethemostcrucialwordifthesubjectorverbisaphrase. Ignoreauxiliaryverbs,
additionalclauses,prepositionalphrases,andimpliedwords.Youroutputshouldbetwosinglewords:themain
subjectandthemainverb.Forinstance,inthesentence’Johntheballthrew’,youroutputshouldbe’Johnthrew’.
Incomplexsentences,focusontheprimaryclause.Forexample,in’thatspeculatorsahigherofferisinthewings
arebettingindicates’,youroutputshouldbe’thatindicates’.
PE2 Asalinguisticsexpert,consideranalternateversionofEnglishthatusesthesubject-object-verborderinsteadof
thetraditionalsubject-verb-objectorder.Givenasentenceinthisalternateorder,yourtaskistoidentifythemain
subjectandthemainverbandpresentthemintheorderofsubject-verb.Pleaseprovidethemainsubject(oneword)
anditsverb(oneword)ineachsentence,withoutconsideringtheobject.Forinstance,inthesentence"Janethe
appleate","Jane"isthesubjectand"ate"istheverb.Therefore,theanswerwouldbe"Janeate".
ManualInit. Youareanexpertinlinguistics.Yourtaskistoidentifythemainverbandthemainsubjectinasentence.Showthe
mainverb(asingleword)anditssubject(alsoasingleword).
APO Youarealanguageanalyst.Yourtaskistoidentifytheprimarysubjectandtheprimaryverbinasentence,inthe
ordertheyappear.Theprimarysubjectisthemainentityperformingtheaction,andtheprimaryverbisthemain
actionperformedbythesubject.Theyshouldbepartofthesameclause.Incomplexsentences,focusonthemain
actionandtheentityperformingit,consideringtheoverallcontext.Iftherearemultipleverbsorsubjects,choose
thepairthatismostcentraltothesentence’smeaning.Ignoreconjunctions,prepositions,orotherlinkingwordsthat
syntax_svo mightseparatetheprimarysubjectfromtheprimaryverb.Iftheprimarysubjectorverbisimplied,inferitfromthe
context.Providetheprimarysubjectandverbasasingleoutput,withthesubjectfirstandtheverbsecond.Both
shouldbesinglewords.Donotincludepunctuationinyouroutput.
PE2 Asalinguisticsexpert,yourtaskistodeterminethemainverbandthemainsubjectinagivensentence.Identify
themasasinglewordeach.Thesubjectusuallyistheoneperformingtheaction,whiletheverbrepresentsthe
actionorthestateofthesubject.Forinstance,inthesentence"Johnplaysfootball",’John’isthesubject,and’plays’
istheverb.Pleaseprovidethesubjectfirst,followedbytheverb.
ManualInit. Youareanexpertinlinguistics.ImaginealanguagethatisthesameasEnglishwiththeonlyexceptionbeingthatit
usestheverb-object-subjectorderinsteadofthesubject-verb-objectorder.Yourtaskistoidentifythemainverband
themainsubjectinasentenceinthisimaginarylanguage.Showthemainverb(asingleword)anditssubject(alsoa
singleword).
APO Youarealinguisticsexpert.Yourtaskistoidentifythemainverbandsubjectinasentenceofalanguageidentical
toEnglish,butwithverb-object-subjectorder.Focusontheverbandsubjectthatcarrythemainactionoridea.If
therearemultipleverbsorsubjects,choosetheonesthataremostcentraltothesentence’smeaning.Iftheverbor
syntax_vos subjectispartofacomplexstructureorisimplied,stateitexplicitly.Iftheverborsubjectisaphrase,identifythe
entirephrase.Youroutputshouldbeintheformat:’SubjectVerb’.Remember,thesubjectandverbmaynotbe
adjacentorsinglewords.Useyourlinguisticexpertisetodeterminethemainverbandsubject.
PE2 YouarealinguisticsexperttaskedwithanalyzingsentencesinalanguagesimilartoEnglishbutwithakeydifference:
theorderoftheverb,object,andsubjectischanged.Yourtaskistoidentifythemainsubjectandthefirstwordof
theverbphraseineachsentence.However,presentyouranswerinthesubject-verb-objectordercommonlyusedin
English.Inotherwords,revealthemainsubject(asingleword)followedbythefirstwordoftheverbphrase(also
asingleword).Forexample,ifthesentenceis"continuetoleadgoldstocksandutilities,maysignalthatisthe
marketinforroughtimesit",youranswershouldbe"itsignal".
ManualInit. Youareanexpertinlinguistics.ImaginealanguagethatisthesameasEnglishwiththeonlyexceptionbeingthatit
usestheverb-subject-objectorderinsteadofthesubject-verb-objectorder.Yourtaskistoidentifythemainverband
syntax_vso
themainsubjectinasentenceinthisimaginarylanguage.Showthemainverb(asingleword)anditssubject(alsoa
singleword).
APO YouarealanguageexpertanalyzingauniquelanguagesimilartoEnglish,butwithverb-subject-objectorder.Your
taskistoidentifythemainverbandsubjectinasentence.Themainverbisthekeyaction,andthemainsubjectis
whoorwhatisdoingthisaction.Incomplexsentences,focusonthemostimportantaction.Ifmultipleverbsor
subjectsexist,choosethemostcentraltothesentence’smeaning.Treatauxiliaryorcompoundverbsasoneunit
withtheirmainverb.Youroutputshouldbethemainsubjectfollowedbythemainverb(bothassinglewords)."
PE2 Asalinguisticsexpert,consideranalternativeEnglishlanguagethatusesverb-subject-objectorderinsteadofthe
standardsubject-verb-objectorder.Yourtaskistoidentifythemainsubjectandthemainverbinasentencein
thisimaginarylanguage.Displaythemainsubject(asingleword)followedbyitsverb(alsoasingleword).For
instance,iftheinputis"comparesthatwith3.5%butterfatforwholemilk",theoutputshouldbe"thatcompares".
Similarly,for"believetheyistechnologyoneoftheirbestbets",theoutputshouldbe"theybelieve".
Table24: PromptsfindbypromptoptimizationmethodsonBIG-benchHardtasks. Hereweusethetaskformatsin
(Suzgunetal.,2023). Intheseexperiments,weusegpt-3.5-turbo-instructasthetaskmodelandgpt-4asthe
promptproposalmodel. SeeTable25whenalternativeformatsareused.

### Task Method Prompt


### BIG-benchHard(ManualInitialization-“Let’sthinkstepbystep.”)

IterativeAPE Considerapproachingthismethodically,onestepatatime.
boolean_expressions APO First,resolve’not’immediatelybeforeit.Thenevaluateexpressionswithinparentheses.Next,perform’and’
operations,andfinally’or’.Determinethetruthvaluestepbystep.
PE2 Evaluatethelogicalexpressionstepbystepfollowingprecedence:’not’,’and’,’or’.Concludebyaffirmingthe
truthofthefullstatement.
causal_judgement IterativeAPE Approacheachstagesequentially.
Continuedonnextpage
35

<!-- Page 36 -->


### Task Method Prompt

APO Identifythedirectcauseoftheoutcome:wasittheimmediateactionorconditionwithoutwhichtheevent
wouldn’thaveoccurred?
PE2 Determineiftheactionwasintentionalandacontributingfactortotheoutcome.Answer’Yes’ifintentionaland
causative,’No’otherwise.
IterativeAPE Considereachphaseonebyone.
disambiguation_qa APO Ineachsentence,determinethepronoun’santecedentbasedontypicalrolesandactions.Ifunclear,markas
ambiguous."
PE2 Let’sthinkstepbystep,usinggrammaticalstructureandcontexttoidentifytheantecedentofthepronounor
determineifitisambiguous.
IterativeAPE Considertheprocessinasequentialmanner.
date_understanding APO Let’sthinkstepbystep.
PE2 Determinethedatereferredtoas’today’fromthecontextgiven,thencalculatethespecifieddatestepbystepin
MM/DD/YYYYformat.
IterativeAPE Let’sthinkstepbystep.
dyck_languages APO Outputthesequenceofclosingbracketsneededtoproperlycloseallopenbracketsinthegivenorder:parentheses
’()’,square’[]’,curly’’,andangle’<>’.Ignoreallothercharacters.
PE2 Givenanincompletesequenceofbrackets,outputonlythemissingclosingbracketsrequiredtocompletethe
sequence.Excludeanypartoftheoriginalsequence.
IterativeAPE Considereachphaseoneatatime.
formal_fallacies APO Determineiftheconclusionnecessarilyfollowsfromthepremisesusingdeductivelogic.Identifyanylogical
fallaciesoroverlookedcounterexamples.Istheargumentvalidorinvalid?
PE2 Toassessifanargumentisdeductivelyvalid,examineiftheconclusionlogicallyfollowsfromthepremises
withoutexception.
IterativeAPE Considerouractionsinasequentialmanner.
geometric_shapes APO ClassifytheshapeformedbytheSVGpath’s’d’attribute,analyzingvertices,linesegments,andclosureto
distinguishpolygonsandfigures.
PE2 AnalyzetheSVGpathcommandstodeterminetheshapetheydraw.Considereachcommandandvisualizethe
pathstepbystep.
IterativeAPE Approachthisgradually,stepbystep.
hyperbaton APO Choosethesentencewithadjectivesinthecorrectorder: opinion,size,age,shape,color,origin,material,
purpose,noun."
PE2 Let’sthinkstepbystep,consideringthestandardorderofadjectivesinEnglish:opinion,size,age,shape,color,
origin,material,purpose.
IterativeAPE Let’sproceedwithamethodical,step-by-stepapproach.
logical_deduction APO Let’sthinkstepbystep.
_five_objects
PE2 Let’sthinkstepbystep.
IterativeAPE Considereachphaseoneatatime.
logical_deduction APO Arrangesevenobjectsinorderusingthecluesprovided.Identifythecorrectpositionforeachobjectfromthe
_seven_objects optionslisted,ensuringlogicalconsistency."
PE2 Let’sanalyzetheinformationprovidedstepbystep,ensuringeachdeductionfollowslogicallyfromthestatements
giventoarriveatthecorrectanswer.
IterativeAPE Let’sproceedwithamethodical,stepwiseapproach.
logical_deduction APO Let’sthinkstepbystep.
_three_objects
PE2 Let’scarefullyanalyzetheinformationtodeterminetheaccuraterankingofobjectsbasedontheirattributes.
IterativeAPE Approachthisstep-by-step,tacklingeachphasesequentially.
multistep_arithmetic APO Let’sthinkstepbystep.
_two
PE2 Let’smeticulouslysolvethemathproblembysimplifyingeachpartoftheequation,verifyingourcalculationsat
everystepbeforemovingforward.
IterativeAPE Considereachphasemethodically.
movie APO Selectthemoviethatbestmatchesthereferenceintermsofgenreandculturalsignificance,ignoringminor
_recommendation details.Choosetheclosestmatch:"
PE2 Evaluatethegivenmoviesforgenres,themes,narrativestyles,tone,andcharacterstoselectthemostsimilarone
fromtheoptions.
IterativeAPE Let’scarefullyassesseachstageofourplaninsequence.
navigate APO Calculatethenetdistancefromthestartingpointafterfollowingthesestep-by-stepinstructions,considering
’forward’aspositiveand’backward’asnegativemovement.
PE2 Let’scalculateeachmovement’seffectonourposition.Startatzeroandaddorsubtractstepsasinstructed,
consideringthedirectioneachtimetoensureaccuracy.
Continuedonnextpage
36

<!-- Page 37 -->


### Task Method Prompt

IterativeAPE Let’scontinuebytakingsystematic,sequentialsteps.
object_counting APO Let’sthinkstepbystep.
PE2 Let’sidentifyandcounttheinstancesofthespecifiedcategoryofitemsmentioned,tallyingmultiples,to
determinetheirtotalquantity.
IterativeAPE Considertheprocedureprogressively.
penguins_in_a_table APO Let’sthinkstepbystep.
PE2 Let’sthinkstepbystep.
IterativeAPE Considereachphasemethodically.
reasoning_about APO Let’sthinkstepbystep.
_colored_objects
PE2 Let’sthinkstepbystepandpaycloseattentiontodetailssuchascolorsandquantities.
IterativeAPE Let’sproceedwithourtasksonebyone.
ruin_names APO Identifythefunniesteditofthegivennamebyselectingtheoptionthatbestincorporatesapunorplayfultwist
relatedtotheoriginal.
PE2 Identifythemosthumorouseditbyconsideringonlypunsorcleverwordplaythatcreatesawittyvariationofthe
originalname,excludingmisspellingsorsimplepluralizations.
IterativeAPE Let’stakethisgradually,stepbystep.
salient_translation APO Let’sthinkstepbystep.
_error_detection
PE2 Let’sanalyzethesourceandtranslationforerrors.CheckifthereareanychangesorinaccuraciesinNamed
Entities,NumericalValues,Modifiers,Negation,Facts,ormissingdetails.Identifywhichtypeoferroroccurs.
IterativeAPE Evaluateeachstagesequentially.
snarks APO Identifythesarcasticstatementbyconsideringthereversalofexpectationsandsocietalnorms.Lookforirony
andimpliedmeaningscontrarytotheliteralwords.
PE2 Toidentifywhichstatementissarcastic,considerthatsarcasmoftenmeanssayingtheoppositeofwhat’struein
amockingway.
IterativeAPE Let’sthinkstepbystep.
sports_understanding APO Determineifthesentenceisplausible:Matchtheathlete’sknownsport,currentactivitystatus,andsport-specific
termstoassessaccuracyincontext.
PE2 Let’sthinkstepbystep.
IterativeAPE Considereachstagemethodically.
temporal_sequences APO Identifythetimeperiodwhenthepersonwasnotseenandthelocationwasopen.Excludetimeswhentheperson
wasobservedelsewhereorthelocationwasclosed.
PE2 Analyzethetimelinetopinpointtimeslotswhentheindividualwasnotseen,whichindicatewheneventscould
haveoccurred.
IterativeAPE We’lltacklethissystematically,onestageatatime.
tracking_shuffled APO Trackballswapsandpositionchangesseparately.Listeachswap,updatepositionsandballownershipafter
_objects_five_objects each,anddeterminefinalstatesforboth.
PE2 Let’scarefullytrackeachplayer’spositionswapsstepbysteptodeterminetheirfinalpositions.
IterativeAPE Approacheachstagewithsystematicthought.
tracking_shuffled APO Let’sthinkstepbystep.
_objects_seven_objects
PE2 Let’scarefullytrackeachbookexchangestepbysteptodeterminethefinalownerofeachbook.
IterativeAPE Reflectoneachstageindividually.
tracking_shuffled APO Let’sthinkstepbystep.
_objects_three_objects
PE2 Let’sanalyzeeachpositionswapinsequencetodeterminethefinalpositions.Confirmthelastknownpositions
ofallplayersbeforeconcluding.
IterativeAPE Let’sproceedwithamethodical,stepwiseapproach.
web_of_lies APO Givenasequenceofpeople’sstatementsaboutothers’truthfulness,determinethetruthstatusofthefinalperson.
Assumethefirststatement’struthisknown.Applylogicalnegationforeachliar’sstatement.
PE2 Todeterminewhoistruthful,inverttheclaimofaliarandtrustatruthfulperson’sclaim.Applythislogicuntil
thelastclaim.
IterativeAPE Progressthrougheachstagesequentially.
word_sorting APO Sortwordsalphabetically,ignoringcase. Exclude’List:’label.Forsamefirstletters,sortremainingletters.
Outputinlowercase.
PE2 Let’sanalyzeandsortwords. Ignorewordsthatarepartofinstructions,like"List:",andthenarrangethe
remainingwordsinalphabeticalorder.
37

<!-- Page 38 -->

Method FinalPrompt TestAcc.

### DateUnderstanding(Generative)


### Zero-shotCoT Let’sthinkstepbystep. 0.391


### IterativeAPE Let’sdissectitandponderovereachphase. 0.467

APO Determinetheexactdatefromthescenario,consideringculturaldateformats,timezones,andperiods. 0.450
Usetheprovideddateasareference.Accountforleadingzeros,leapyears,relativedates,andevent-based
timereferences.ProvidetheresultinMM/DD/YYYYformat.
PE2 Analyzingthegiveninformation,let’scalculatethesolution.Remembertoconsiderthecontextprovided, 0.544
suchasreferencesto’today’orspecificdates.

### MovieRecommendation(Multi-choice2)


### Zero-shotCoT Let’sthinkstepbystep. 0.570

IterativeAPE Let’sdissectitandconsidereverystepinorder. 0.673
APO Identifythemoviethatsharesthemostsignificantthemesandnarrativestructurewiththegivenmovies. 0.750
Prioritizethesefactorsovertoneandpacing.Choosethemostsimilarmoviefromtheoptions,explaining
yourchoice.
PE2 Consideringfactorssuchasgenre,director,actors,releaseperiod,audiencetarget,animationstyle,and 0.790
humor,analyzethesimilaritiesamongthegivenmoviesandidentifythemoviefromtheoptionsthat
sharesthemostsimilarities.
Table25: ResultsonDateUnderstandingandMovieRecommendationfromBIG-benchHard(Suzgunetal.,2023).
Intheseexperiments,weuseaformatdifferentfromthosein(Suzgunetal.,2023). See§A.2fordetaileddiscussion
ontheeffectoftaskformat. Weusegpt-3.5-turbo-instructasthetaskmodelandgpt-4asthepromptproposal
model.
38

<!-- Page 39 -->

Method FinalPrompt TestAcc.

### GSM8k


### Zero-shotCoT Let’sthinkstepbystep. 0.481

IterativeAPE We’llapproachthismethodically,proceedingonestepatatime. 0.497
APO Carefullyanalyzethedetailsandperformprecisearithmeticoperationsstepbystep,ensuringtoapplythe 0.510
correctmathematicalprinciplesforaccuratecalculations.
PE2 Carefullycalculatestepbystep,consideringalldetails,includinguniquecountsandoverlaps.Accurately 0.505
applyarithmetictofindthenumericalanswer,ensuringlogicaloperationsarecorrectlyfollowed.

### MultiArith


### Zero-shotCoT Let’sthinkstepbystep. 0.715


### IterativeAPE Proceedgradually,onestepatatime. 0.735

APO Calculatetheanswerusingarithmetic. Rounddownwherenecessary. Correctanylogicalerrorsin 0.735
reasoning.Providetheexactnumber.
PE2 Focusonaccuratelycalculatingtotalsanddifferences,consideringfactorslikeitemconditionsorgroupings 0.743
forprecision.Roundonlyifnecessary,whendealingwithpracticalfractions.

### BIG-benchHard-DateUnderstanding


### Zero-shotCoT Let’sthinkstepbystep. 0.36

IterativeAPE Let’smoveforwardbydividingitintomanageablesteps. 0.48
APO Accuratelycalculatedatesfromgiveninputs,consideringthecurrentreferencepoint(e.g.,’yesterday’, 0.48
’today’)andapplyingcorrectcalendararithmetic,includingmonthlengthsandleapyears.Ignoreirrelevant
detailsandassumptionsbeyondprovidedinformation.
PE2 Let’sthinkstepbystep.Fordatequestions,calculatefromthegivendate,thenchoosetheclosestmatching 0.56
option.Ignoreirrelevantinfo.

### BIG-benchHard-Hyperbaton


### Zero-shotCoT Let’sthinkstepbystep. 0.52


### IterativeAPE Let’ssystematicallygothrougheverystep. 0.48

APO Classifyadjectiveorder: opinion,size,age,shape,color,origin,material,purpose. Forwordsfitting 0.72
multiplecategories,prioritizepurpose,thenmaterial.Ignorerareexceptions.
PE2 Choosethecorrectsentenceusingadjectiveorder: opinion,size,age,shape,color,origin,material, 0.74
purpose.Note:’purpose’adjectives,like’hiking’,oftencomelast.

### BIG-benchHard-TemporalSequences


### Zero-shotCoT Let’sthinkstepbystep. 0.50

IterativeAPE Let’sprogressbybreakingitdownintosmaller,manageableparts. 0.42
APO Identifywhenapersonvisitedaplacebyexcludingtimestheywereseenelsewhere,consideringtheir 0.52
schedule,eyewitnesssightings,andtheplace’shours.Onlyincludeunaccountedtimes.
PE2 Let’sanalyzethetimelineandothers’observationstodeducetheonlytimeslotsnotaccountedfor, 0.62
indicatingwhenthevisitcouldhaveoccurred.

### BIG-benchHard-WordSorting


### Zero-shotCoT Let’sthinkstepbystep. 0.04

IterativeAPE Let’stacklethissystematically,advancingstepbystep. 0.20
APO Alphabeticallysortthewordsbelow,correctinganytypos.Ignorecapitalization,treatabbreviationsand 0.16
possessivesnormally.Exclude’List:’fromitems.
PE2 Sortthegivenwordsalphabetically,butexclude’List:’orsimilarformattingelements.Ensureeveryword 0.28
isconsidered.
Table26: Resultsonsixselectedtasks. WeuseMistral-7B-Instruct-v0.2asthetaskmodelandgpt-4-turbo
asthepromptproposalmodel.
39

## Tables

**Table (Page 1):**

| Inspect a prompt and a batch of failure examples |
|---|
| when this prompt is used. Then provide feedback. |


**Table (Page 1):**

| The prompt should be edited to guide the model to |
|---|
| perform subtraction. |


**Table (Page 1):**

| Let’s solve this problem step by step. Remember to add |
|---|
| or subtract as needed. |


**Table (Page 1):**

| updatedprompt |  |
|---|---|
|  | meta-prompt |


**Table (Page 2):**

| 100 +6.3 100 Initialization APO ycaruccA Iterative APE PE2 (This Work) 75 ycaruccA 75 +7.4 erocS +3.1 +5.9 )egarevA( +8.0 1F 50 50 +15.9 25 25 MultiArith GSM8K Instruction Induction BIG-Bench Hard Counterfactual Eval Production (14 Tasks) (27 Tasks) (12 Tasks) Prompt | +8.0 |  |  |  |
|---|---|---|---|---|
|  |  |  |  |  |
|  |  |  |  |  |
|  |  | od Pro | ucti mp | on t |
|  |  |  |  |  |


**Table (Page 2):**

|  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
| M | ulti | Ari | th |  |  | GS | M8K |  |
|  |  |  |  |  |  |  |  |  |


**Table (Page 2):**

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| uc (1 | tion 4 T | In ask | duc s) | tion BI | G- (2 | Ben 7 T | ch ask | Ha s) | rd Co | unte (1 | rfa 2 T | ctu ask | al s) |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |


**Table (Page 4):**

| (a) two-step task instruction |
|---|
| A prompt is a text paragraph that outlines the expected actions and instructs the model. In our collaboration, we'll work together to refine a prompt. The process consists of two steps: # Step 1 Examine the prompt and a batch of examples # Step 2 Propose a new prompt based on your reasoning |


**Table (Page 4):**

| (c) step-by-step reasoning template |
|---|
| # Instruction For each example, provide reasoning according to the following template * Output is correct? * Necessary to edit the prompt? * If yes, suggestions on prompt editing? |


**Table (Page 4):**

| # Current Prompt Let’s think step by step. |  |
|---|---|
| # Full Template (b) context specification ``` Question: <input> Answer: Let’s think step by step. ``` | (b) context specification |
| # Examples ## Example 1 Input: George had 28 socks. If he threw away 4 socks … Output: 64 Reasoning: Step 1: George had 28 socks. Step 2: … Label: 60 [More examples …] |  |


**Table (Page 4):**

| Let’s solve this problem step by step. Remember to add or |
|---|
| subtract as needed. |


**Table (Page 14):**

| Zeroshot CoT Iterative APE APO PE2 80 ycaruccA 60 40 tseT 20 0 Date Date Movie Movie (Multi-choice) (Generative) (Multi-choice 1) (Multi-choice 2) | Zeroshot CoT Iterative APE APO PE2 |  |  |  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |


**Table (Page 14):**

| caruccA Zeroshot CoT 60 APO PE2 40 tseT elbaliavA OPRO (1) OPRO (2) K8MSG 20 toN 0 text-davinci gpt-3.5-turbo mistral-7b yi-6b mpt-7b 003 instruct instruct-v0.2 instruct | elbaliavA toN |  |  |  |  |  |  | Zeroshot CoT APO PE2 OPRO (1) OPRO (2) |
|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |


**Table (Page 16):**

| (d) prompt engineering tutorial |
|---|
| Let’s read a blogpost on prompt engineering: Prompt engineering is a relatively new discipline for developing and optimizing prompts to efficiently use language models (LMs) … |


**Table (Page 16):**

| (c) step-by-step reasoning template |
|---|
| # Instruction For each example, provide reasoning according to the following template * Output is correct? * Prompt describing the task correctly? * Necessary to edit the prompt? * If yes, suggestions on prompt editing? |


**Table (Page 16):**

| (a) two-step task instruction |
|---|
| A prompt is a text paragraph that outlines the expected actions and instructs the model. In our collaboration, we'll work together to refine a prompt. The process consists of two steps: # Step 1 Examine the prompt and a batch of examples # Step 2 Propose a new prompt based on your reasoning |


**Table (Page 16):**

| # Current Prompt Let’s think step by step. |  |
|---|---|
| # Full Template (b) context specification ``` Question: <input> Answer: Let’s think step by step. ``` | (b) context specification |
|  |  |
| # Examples (e) batch size ## Example 1 Input: George had 28 socks. If he threw away 4 socks … Output: 64 Reasoning: Step 1: George had 28 socks. Step 2: … Label: 60 [More examples …] | (e) batch size |


**Table (Page 16):**

| Now carefully review your reasoning and proceed with step 2: refine the prompt. # Current Prompt Let’s think step by step. |  |
|---|---|
| # Optimization History (g) optim history At time 0, the prompt was “…”, it was edited … | (g) optim history |
|  |  |
| # Instructions (f) step size * You are allowed to change up to 10 words | (f) step size |
| * The total length should be less than 50 words * Reply with the prompt. Do not include other text. |  |


**Table (Page 16):**

| Let’s solve this problem step by step. Remember to add or |
|---|
| subtract as needed |


**Table (Page 22):**

|  |  |  |  |
|---|---|---|---|
|  |  |  |  |


**Table (Page 22):**

|  |  |  |  |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |


**Table (Page 22):**

|  |  |  |  |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |


**Table (Page 23):**

|  |  |  |  |
|---|---|---|---|
|  |  |  |  |


**Table (Page 23):**

|  |  |  |  |
|---|---|---|---|
|  |  |  |  |


**Table (Page 23):**

|  |  |  |  |  |  |
|---|---|---|---|---|---|
|  |  |  |  |  |  |


**Table (Page 23):**

|  |  |  |  |  |
|---|---|---|---|---|
|  |  |  |  |  |


**Table (Page 23):**

|  |  |  |  |
|---|---|---|---|
|  |  |  |  |


**Table (Page 23):**

|  |  |  |  |
|---|---|---|---|
|  |  |  |  |


**Table (Page 23):**

|  |  |  |  |
|---|---|---|---|
|  |  |  |  |


**Table (Page 23):**

|  |  |  |  |
|---|---|---|---|
|  |  |  |  |


**Table (Page 23):**

|  |  |
|---|---|
|  |  |


**Table (Page 23):**

|  |  |
|---|---|
|  |  |


**Table (Page 23):**

|  |  |
|---|---|
|  |  |


**Table (Page 23):**

|  |  |  |
|---|---|---|
|  |  |  |


**Table (Page 23):**

|  |  |  |
|---|---|---|
|  |  |  |


**Table (Page 24):**

|  |  |  |  |
|---|---|---|---|
|  |  |  |  |


**Table (Page 24):**

|  |  |  |  |
|---|---|---|---|
|  |  |  |  |


**Table (Page 24):**

|  |  |
|---|---|
|  |  |


**Table (Page 28):**

|  |
|---|
| {{#system~}} |
| You are a helpful assistant. |
| {{~/system}} |
|  |
| {{#user~}} |
| I gave a friend an instruction and {{n_demo}} inputs. The friend read the instruction and wrote an |
| output for every one of the inputs. |
| Here are the input-output pairs: |
|  |
| {{demos}} |
|  |
| What was the instruction? It has to be less than {{max_tokens}} tokens. |
| {{~/user}} |
|  |
| {{#assistant~}} |
| The instruction was {{gen 'instruction' [[GENERATION_CONFIG]]}} |
| {{~/assistant}} |
|  |


**Table (Page 28):**

|  |
|---|
| {{#system~}} |
| You are a helpful assistant. |
| {{~/system}} |
|  |
| {{#user~}} |
| Generate a variation of the following instruction while keeping the semantic meaning. |
|  |
| {{prompt}} |
|  |
| The new instruction has to be less than {{max_tokens}} words. |
| Reply with the new instruction. Do not include other text. |
| {{~/user}} |
|  |
| {{#assistant~}} |
| {{gen 'new_prompt' [[GENERATION_CONFIG]]}} |
| {{~/assistant}} |
|  |


**Table (Page 28):**

|  |
|---|
| {{#system~}} |
| You are a helpful assistant. |
| {{/system~}} |
|  |
| {{#user~}} |
| I'm trying to write a zero-shot classifier prompt. |
|  |
| My current prompt is: |
| "{{prompt}}" |
|  |
| But this prompt gets the following examples wrong: |
| {{failure_string}} |
|  |
| Give {{n_reasons}} reasons why the prompt could have gotten these examples wrong. Do not include other |
| text. |
| {{/user~}} |
|  |
| {{#assistant~}} |
| {{gen 'gradients' temperature=0.0}} |
| {{/assistant~}} |
|  |


**Table (Page 28):**

|  |
|---|
| {{#system~}} |
| You are a helpful assistant. |
| {{/system~}} |


**Table (Page 29):**

|  |
|---|
| {{#user~}} |
| I'm trying to write a zero-shot classifier. |
|  |
| My current prompt is: |
| "{{prompt}}" |
|  |
| But it gets the following examples wrong: |
| {{failure_string}} |
|  |
| Based on these examples the problem with this prompt is that: |
| {{gradient}} |
|  |
| Based on the above information, I wrote an improved prompt. The total length of the prompt should be |
| less than {{max_tokens}} words. |
| {{/user~}} |
|  |
| {{#assistant~}} |
| The improved prompt is {{gen 'new_prompt' temperature=0.0}} |
| {{/assistant~}} |
|  |


**Table (Page 29):**

|  |
|---|
| {{#system~}} |
| You are a helpful assistant. |
| {{~/system}} |
|  |
| {{#if instruction}} |
| {{#user~}} |
| Let's read a blogpost on prompt engineering: |
| {{instruction}} |
| {{~/user}} |
| {{/if}} |
|  |
| {{#user~}} |
| A prompt is a text paragraph that outlines the expected actions and instructs the model to generate a |
| specific output. This prompt is concatenated with the input text, and the model then creates the |
| required output. |
|  |
| In our collaboration, we'll work together to refine a prompt. The process consists of two main steps: |
|  |
| ## Step 1 |
| I will provide you with the current prompt, how the prompt is concatenated with the input text (i.e., " |
| full template"), along with {{batch_size}} example(s) that are associated with this prompt. Each |
| examples contains the input, the reasoning process generated by the model when the prompt is |
| attached, the final answer produced by the model, and the ground-truth label to the input. Your |
| task is to analyze the examples, determining whether the existing prompt is decsribing the task |
| reflected by these examples precisely, and suggest changes to the prompt. |
|  |
| ## Step 2 |
| Next, you will carefully review your reasoning in step 1, integrate the insights to craft a new, |
| optimized prompt. Optionally, the history of refinements made to this prompt from past sessions |
| will be included. Some extra instructions (e.g., the number of words you can edit) will be provided |
| too. |
| {{~/user}} |
|  |
| {{#assistant~}} |
| Sure, I'd be happy to help you with this prompt engineering problem. |
| Please provide me with the prompt engineering history, the current prompt, and the examples you have. |
| {{~/assistant}} |
|  |
| {{#user~}} |
| ## Prompt |
| {{prompt}} |
|  |
| ## Full Template |
| This describes how the prompt of interested is concatenated with the input text. |
| The prompt may appear before the input text, or after the input text. |
| Optionally the full template may contain other template information. |
| ``` |
| {{full_prompt}} |
| ``` |
|  |
| ## Examples |
| {{examples}} |
|  |
| ## Instructions |
| For some of these examples, the output does not match with the label. This may be due to the prompt |
| being misleading or not describing the task precisely. |
|  |
| Please examine the example(s) carefully. Note that the ground-truth labels are __absolutely correct__, |
| but the prompts (task descriptions) may be incorrect and need modification. For each example, |
| provide reasoning according to the following template: |
|  |
| ### Example <id> |


**Table (Page 30):**

| Input: <input> |
|---|
| Output: <output> |
| Label: <label> |
| Is the output correct compared to the label: <yes or no, and your reasoning> |
| Is the output correctly following the given prompt: <yes or no, and your reasoning> |
| Is the prompt correctly describing the task shown by the input-label pair: <yes or no, and your |
| reasoning> |
| To output the correct label, is it necessary to edit the prompt: <yes or no, and your reasoning> |
| If yes, provide detailed analysis and actionable suggestions to edit the prompt: <analysis and |
| suggestions> |
| {{~/user}} |
|  |
| {{#assistant~}} |
| {{gen 'reasoning' temperature=0}} |
| {{~/assistant}} |
|  |
| {{#user~}} |
| Now please carefully review your reasoning in Step 1 and help with Step 2: refining the prompt. |
|  |
| {{#if history}} |
| ## Prompt Refinement History from the Past |
| Note that higher accuracy means better. If some edits are useful in the past, it may be a good idea to |
| make edits along the same direction. |
| {{history}} |
| {{/if}} |
|  |
| ## Current Prompt |
| {{prompt}} |
|  |
| ## Instructions |
| {{#if step_size}} |
| * You are allowed to change up to {{step_size}} words in the original prompt. |
| {{/if}} |
| {{#if max_tokens}} |
| * The total length of the prompt should be less than {{max_tokens}} words. |
| {{/if}} |
| * Please help edit the prompt so that the updated prompt will not fail on these examples anymore. |
| * Reply with the prompt. Do not include other text. |
| {{~/user}} |
|  |
| {{#assistant~}} |
| {{gen 'new_prompt' temperature=0.7 max_tokens=300}} |
| {{~/assistant}} |
|  |
| {{#if history}} |
| {{#user~}} |
| Now please summarize what changes you've made to the prompt, in the following format. Make sure the |
| summariy is concise and contains no more than 200 words. |
|  |
| " * At step {{timestamp}}, the prompt has limitations such as <summary of limitations>. Changes to the |
| prompt include <summary of changes>." |
|  |
| Reply with the summarization. Do not include other text. |
| {{~/user}} |
|  |
| {{#assistant~}} |
| {{gen 'new_history' temperature=0.7 max_tokens=200}} |
| {{~/assistant}} |
| {{/if}} |
|  |


**Table (Page 38):**

| Let’sdissectitandponderovereachphase. |
|---|
| Determinetheexactdatefromthescenario,consideringculturaldateformats,timezones,andperiods. Usetheprovideddateasareference.Accountforleadingzeros,leapyears,relativedates,andevent-based timereferences.ProvidetheresultinMM/DD/YYYYformat. |
| Analyzingthegiveninformation,let’scalculatethesolution.Remembertoconsiderthecontextprovided, suchasreferencesto’today’orspecificdates. |


**Table (Page 38):**

| Let’sdissectitandconsidereverystepinorder. |
|---|
| Identifythemoviethatsharesthemostsignificantthemesandnarrativestructurewiththegivenmovies. Prioritizethesefactorsovertoneandpacing.Choosethemostsimilarmoviefromtheoptions,explaining yourchoice. |
| Consideringfactorssuchasgenre,director,actors,releaseperiod,audiencetarget,animationstyle,and humor,analyzethesimilaritiesamongthegivenmoviesandidentifythemoviefromtheoptionsthat sharesthemostsimilarities. |


**Table (Page 39):**

| We’llapproachthismethodically,proceedingonestepatatime. |
|---|
| Carefullyanalyzethedetailsandperformprecisearithmeticoperationsstepbystep,ensuringtoapplythe correctmathematicalprinciplesforaccuratecalculations. |
| Carefullycalculatestepbystep,consideringalldetails,includinguniquecountsandoverlaps.Accurately applyarithmetictofindthenumericalanswer,ensuringlogicaloperationsarecorrectlyfollowed. |


**Table (Page 39):**

| Proceedgradually,onestepatatime. |
|---|
| Calculatetheanswerusingarithmetic. Rounddownwherenecessary. Correctanylogicalerrorsin reasoning.Providetheexactnumber. |
| Focusonaccuratelycalculatingtotalsanddifferences,consideringfactorslikeitemconditionsorgroupings forprecision.Roundonlyifnecessary,whendealingwithpracticalfractions. |


**Table (Page 39):**

| Let’smoveforwardbydividingitintomanageablesteps. |
|---|
| Accuratelycalculatedatesfromgiveninputs,consideringthecurrentreferencepoint(e.g.,’yesterday’, ’today’)andapplyingcorrectcalendararithmetic,includingmonthlengthsandleapyears.Ignoreirrelevant detailsandassumptionsbeyondprovidedinformation. |
| Let’sthinkstepbystep.Fordatequestions,calculatefromthegivendate,thenchoosetheclosestmatching option.Ignoreirrelevantinfo. |


**Table (Page 39):**

| Let’ssystematicallygothrougheverystep. |
|---|
| Classifyadjectiveorder: opinion,size,age,shape,color,origin,material,purpose. Forwordsfitting multiplecategories,prioritizepurpose,thenmaterial.Ignorerareexceptions. |
| Choosethecorrectsentenceusingadjectiveorder: opinion,size,age,shape,color,origin,material, purpose.Note:’purpose’adjectives,like’hiking’,oftencomelast. |


**Table (Page 39):**

| Let’sprogressbybreakingitdownintosmaller,manageableparts. |
|---|
| Identifywhenapersonvisitedaplacebyexcludingtimestheywereseenelsewhere,consideringtheir schedule,eyewitnesssightings,andtheplace’shours.Onlyincludeunaccountedtimes. |
| Let’sanalyzethetimelineandothers’observationstodeducetheonlytimeslotsnotaccountedfor, indicatingwhenthevisitcouldhaveoccurred. |


**Table (Page 39):**

| Let’stacklethissystematically,advancingstepbystep. |
|---|
| Alphabeticallysortthewordsbelow,correctinganytypos.Ignorecapitalization,treatabbreviationsand possessivesnormally.Exclude’List:’fromitems. |
| Sortthegivenwordsalphabetically,butexclude’List:’orsimilarformattingelements.Ensureeveryword isconsidered. |
