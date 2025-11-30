---
title: "Re Reading Improves Reasoning"
original_file: "./Re_Reading_Improves_Reasoning.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["prompt-engineering", "llm", "rag", "chain-of-thought", "fine-tuning"]
keywords: ["cot", "answer", "let", "question", "page", "reading", "vanilla", "input", "reasoning", "llms"]
summary: "<!-- Page 1 -->

Re-Reading Improves Reasoning in Large Language Models

### XiaohanXu1,ChongyangTao2*,TaoShen3,CanXu4,


### HongboXu1,GuodongLong3,Jian-guangLou4,ShuaiMa2

1InstituteofInformationEngineering,CAS 2SKLSDELab,BeihangUniversity
3UniversityofTechnologySydney 4MicrosoftCorporation
shawnxxh@gmail.com, {chongyang, mashuai}@buaa.edu.cn, hbxu@iie.ac.cn
{caxu,jlou}@microsoft.com, {tao.shen,guodong.long}@uts.edu.au
Abstract CoT

### Input


### Q: Roger has 5 tennis balls. He buys 2 more c"
related_documents: []
---

# Re Reading Improves Reasoning

<!-- Page 1 -->

Re-Reading Improves Reasoning in Large Language Models

### XiaohanXu1,ChongyangTao2*,TaoShen3,CanXu4,


### HongboXu1,GuodongLong3,Jian-guangLou4,ShuaiMa2

1InstituteofInformationEngineering,CAS 2SKLSDELab,BeihangUniversity
3UniversityofTechnologySydney 4MicrosoftCorporation
shawnxxh@gmail.com, {chongyang, mashuai}@buaa.edu.cn, hbxu@iie.ac.cn
{caxu,jlou}@microsoft.com, {tao.shen,guodong.long}@uts.edu.au
Abstract CoT

### Input


### Q: Roger has 5 tennis balls. He buys 2 more cans of tennis

To enhance the reasoning capabilities of off- balls. Each can has 3 tennis balls. How many tennis balls OnePass
does he have now?
the-shelf Large Language Models (LLMs),
we introduce a simple, yet general and effec- A:Let’sthinkstepbystep.
tivepromptingmethod,RE2,i.e.,Re-Reading CoT+RE2

### Input

the question as input. Unlike most thought-

### Q: Roger has 5 tennis balls. He buys 2 more cans of tennis

elicitingpromptingmethods,suchasChain-of- balls. Each can has 3 tennis balls. How many tennis balls FirstPass
does he have now?
Thought(CoT),whichaimtoelicitthereason- Read the question again: Roger has 5 tennis balls. He buys
ing process in the output, RE2 shifts the fo- 2
H o
m
w
o r
m
e
a
c
n
a
y
n s
te
o
n
f
n
t
i
e
s
n
b
n
a
is
lls
b
d
a
o
lls
e
.
s

## E

h
a
e
c
h
h
a
c
v
a
e
n
n
h
o
a
w
s
?
3 tennis balls. Second Pass
custotheinputbyprocessingquestionstwice,
A:Let’sthinkstepbystep.
therebyenhancingtheunderstandingprocess.
Consequently, RE2 demonstrates strong gen- Figure1:ExampleinputsofCoTpromptingversusCoT
erality and compatibility with most thought- promptingwith RE2. InoriginalCoT,everytokenin
eliciting prompting methods, including CoT. thequestioncannotseeitslatertokenssincemostLLMs
Crucially,RE2facilitatesa"bidirectional"en- are autoregressive models (the top figure). RE2 is a
coding in unidirectional decoder-only LLMs simplepromptingmethodthatrepeatsthequestionas
becausethefirstpasscouldprovideglobalin- input. LLMswithRE2allowseachtokeninthesecond
formationforthesecondpass. Webeginwith pass,e.g. "tennisballs",toseeitslatertokensfromthe
a preliminary empirical study as the founda- firstpass,e.g. "Howmany...",achievinganeffectofa
tionofRE2,illustratingitspotentialtoenable "bidirectional"understanding(thebottomfigure).
"bidirectional"attentionmechanisms. Wethen
evaluate RE2 on extensive reasoning benchhuman intelligence, allowing us to infer, deduce,
marksacross14datasets,spanning112experiments,tovalidateitseffectivenessandgener- andsolveproblems. InLLMs,thisskilliscrucial
ality. Our findings indicate that, with the ex- for improving their practical use. Despite their
ceptionofafewscenariosonvanillaChatGPT, impressive abilities, LLMs often have difficulty
RE2consistentlyenhancesthereasoningper- withreasoningtasks(Blair-Staneketal.,2023;ArkformanceofLLMsthroughasimplere-reading
oudas,2023),urgingresearcherstoexploremore
strategy. FurtheranalysesrevealRE2’sadaptstrategies to bolster reasoning ability (Wei et al.,
ability,showinghowitcanbeeffectivelyinte-
2022b;Gaoetal.,2023;Bestaetal.,2023).
gratedwithdifferentLLMs,thought-eliciting
prompting,andensemblestrategies.1 Existing research on reasoning has predominantlyconcentratedondesigningdiversethought-
1 Introduction
eliciting prompting strategies to elicit reasoning
In the ever-evolving landscape of artificial in- processes in the output phase, such as Chaintelligence, large language models (LLMs) have of-Thought (CoT) (Wei et al., 2022b), Programemergedasakeystoneofnaturallanguageunder- AidedLanguageModel(PAL)(Gaoetal.,2023),
standingandgeneration(Brownetal.,2020;Tou- etc. (Yao et al., 2023a; Besta et al., 2023; Wang
vronetal.,2023a,a;OpenAI,2023;Xuetal.,2024). etal.,2023a). Incontrast,scantattentionhasbeen
AsLLMshavebecomemoreadvanced,akeychal- paidtotheunderstandingoftheinputphase. Infact,
lengehasemerged: teachingthemtoreasoneffec- comprehensionisthefirststepbeforesolvingthe
tively. Theabilitytoreasonwellisakeyaspectof problem, which is crucially important. However,
intheeraofgenerativeAI,mostLLMsadoptthe
*Correspondingauthor
1OurcodeisavailableatGithub. decoder-onlyLLMswithunidirectionalattention,
4202
voN
91
]LC.sc[
4v57260.9032:viXra

<!-- Page 2 -->


## Q

Roger
First

### Pass

Second

### Pass

First Second
Pass Pass
……
:
have
now
?

## Q

Roger
……
:
have
now
? Q regoR …… : evah won ? Q regoR …… : evah won ?
yeteffectiveandgeneralreasoningpromptingstrategy, RE2, i.e., Re-Reading the question as input
(see the illustration in Figure 1). While our RE2
is simple, it offers several advantages for LLMs’
reasoningscenarios. (1)Thisapproachmirrorsthe
human strategy of problem-solving. LLMs with
RE2 show potential for a "bidirectional" understanding of questions. (2) Repeating questions
allows LLMs to allocate more computational resourcestoinputencoding,similarto"horizontally"
increasingthedepthofneuralnetworks. (3) RE2
emphasizesunderstandingduringtheinputphase,
makingitorthogonaltoandcompatiblewithmost
thought-elicitingpromptingmethodsthatfocuson
theoutputphase,suchasCoTandPAL.
Figure 2: Illustration of the attention distribution in To validate the efficacy and generality of RE2,
LLaMA-2 by repeating the question as the input (a weconductedextensiveexperimentsspanningarithdarkercellindicateshigherattention).Theregionwithin metic,commonsense,andsymbolicreasoningtasks
thereddasheduppertriangledemonstratesthatevery
across 14 datasets and 112 experiments. The
tokeninthesecondpasshasobviousattentiontoitslater
results show that, with the exception of certain
tokens in the first pass. This suggests that re-reading
in LLMs is promising for achieving a "bidirectional"
scenarios on vanilla ChatGPT, our RE2 with a
understandingofthequestion. simple re-reading strategy consistently enhances
the reasoning performance of LLMs. RE2 exhibits versatility across various LLMs, such as
likeGPT-3(Brownetal.,2020)andLLaMA(Tou- Text-Davinci-003,ChatGPT,LLaMA-2-13B,and
vron et al., 2023b). This unidirectional attention LLaMA-2-70B, spanning both instruction finelimitseverytoken’svisibilitytoonlypreviousto- tuning (IFT) and non-IFT models. We also exkenswhenencodingaquestion,potentiallyimpair- plore RE2 in task settings of zero-shot and fewingthebidirectionalunderstandingofeachwordin shot,thought-elicitingpromptingmethods,andthe
thequestion(Duetal.,2022). InFigure1,thelast self-consistency setting, highlighting its generalsentence,"Howmany...",highlightsthequestion’s ity.
mainfocus,whichiscrucialfortheunderstanding
of the preceding words. However, LLMs cannot 2 Methodology
seethesubsequentwordswhenencodingatoken
2.1 VanillaChain-of-ThoughtforReasoning
duetotheirunidirectionalvision.
We begin with a unified formulation to leverage
Fortunately,manycognitivesciencestudieshave
LLMswithCoTpromptingtosolvereasoningtasks.
revealedthathumanstendtore-readquestionsdur-

### Informal,givenaninputxandatargety,aLLM

ing learning and problem-solving to enhance the
pwithCoTpromptingcanbeformulatedas
comprehension process (Dowhower, 1987, 1989;
Ozek and Civelek, 2006). The first reading pro-
(cid:88)
videsanoverallunderstanding,whichbenefitsthe y ∼ p(y|C ,z)·p(z|C ),
x x
secondreading. Motivatedbythis,wealsoconduct
z∼p(z|Cx)
apreliminaryempiricalstudyforLLaMA-2(TouwhereC = c(cot)(x). (1)
x
vron et al., 2023b) by repeating the question two
timesastheinputusingtheGSM8Kdataset(Cobbe Inthisformulation,C denotesthepromptedinput.
x
et al., 2021). The attention heatmap in Figure 2 c(cot)(·)representsthetemplatewithCoTpromptshowsthatthere-readingstrategyallowsLLaMA-2 inginstructions, suchas ‘let’sthink stepbystep’.
to achieve a "bidirectional" understanding of the z stands for a latent variable of rationale, and z
question,whichisexpectedtofurtherimprovethe denotes a sampled rationale in natural language.
reasoningperformance. Consequently,theLLMscanbreakdowncomplex
Based on the observation and inspired by the tasksintomoremanageablereasoningsteps,treathumanstrategyofre-reading,wepresentasimple ingeachstepasacomponentoftheoverallsolution

<!-- Page 3 -->

chain. WeemployCoTasabaselinetosolverea- thought-eliciting prompting, τ, designed to elicit
soningtaskswithoutcompromisingitsgenerality. thoughtsfromtheLLMs,Eq. (3)isrewrittenas:
InadditiontoCoT,ourproposedsimple RE2 can
(cid:88)
serveasa"plug&play"moduleadaptabletomost y ∼ p(y|C ,z)·p(z|C ),
x x
otherpromptingmethods(§2.3). z∼p(z|Cx)
whereC = c(τ)(re2(x)). (3)
2.2 Re-Reading(RE2)ImprovesReasoning x

### Drawing inspiration from the human strategy of

Here,τ denotesvariousthought-elicitingpromptre-reading,weintroducethisstrategyforLLMreaingsbeyondCoT,suchasPlan-and-Solve(Wang
soning,dubbed RE2,toenhanceunderstandingin
et al., 2023a), and Program-Aided Prompt (Gao
theinputphase. With RE2,thepromptingprocess
etal.,2023),etc. WealsoconductedlotsofexperiinEq. 1canbereadilyrephrasedas:
mentstovalidatethegeneralityof RE2 in§3.4.
(cid:88)
y ∼ p(y|C x ,z)·p(z|C x ), 3 Experiments
z∼p(z|Cx)
3.1 Benchmarks
whereC = c(cot)(re2(x)). (2)
x

### We assess RE2 prompting across three key cat-

Inthisformulation,re2(·)isthere-readingopera- egories of reasoning benchmarks. Details of all
tion of the input. We don’t seek complex adjust- datasetsareshowninAppendixA
mentsforLLMsbutaimforageneralimplementa-
Arithmetic Reasoning We consider the foltionofre2(x)thatisassimpleasfollows:
lowing seven arithmetic reasoning benchmarks:
RE2Prompting the GSM8K benchmark of math word problems(Cobbeetal.,2021),theSVAMPdatasetof

### Q: {Input Query}

Read the question again: {Input Query} mathwordproblemswithvaryingstructures(Patel
# Thought-eliciting prompt (e.g.,“Let’s et al., 2021), the ASDiv dataset of diverse math
think step by step") #
word problems (Miao et al., 2020), the AQuA
dataset of algebraic word problems (Ling et al.,
where‘{InputQuery}‘isaplaceholderforthein-
2017),theAddSub (Hosseinietal.,2014)ofmath
putquery,x. Theleftpartofthispromptingcould
wordproblemsonadditionandsubtractionforthird
incorporate other thought-eliciting prompts. Into fifth grader, MultiArith (Roy and Roth, 2015)
tuitively, RE2 offers two advantages to enhance
datasetofmathproblemswithmultiplesteps,and
the understanding process: (1) it allocates more
theSingelEQ(Royetal.,2015)datasetofelemencomputational resources to the input, and (2) it
tarymathwordproblemswithsingleoperation.
facilitates a "bidirectional" understanding of the
question,wherethefirstpassprovidesglobalinfor- Commonsense and Symbolic Reasoning For
mationforthesecondpass. commonsense reasoning, we use CSQA (Talmor
etal.,2019),StrategyQA(Gevaetal.,2021),and
2.3 Generalityof RE2
theARC(Clarketal.,2018). CSQAdatasetcon-
Dueto RE2’ssimplicityandemphasisontheinput sistsofquestionsthatnecessitatevariouscommonphase,itcanbeseamlesslyintegratedwithawide sense knowledge. The StrategyQA dataset comrangeofLLMsandalgorithms,includingfew-shot prisesquestionsthatdemandmulti-stepreasoning.
settings,self-consistency,variousthought-eliciting The ARC dataset (denoted as ARC-t) is divided
promptingstrategies,andmore. Weofferinsights into two sets: a Challenge Set (denoted as ARC-
into the integration of RE2 with other thought- c), containing questions that both retrieval-based
elicitingpromptingstrategiesasanillustration. and word co-occurrence algorithms answered in-
Comparedwiththosethought-elicitingprompt- correctly,andanEasySet(denotedasARC-e). We
ingstrategiesthatfocusontheoutputphase,RE2 evaluatetwosymbolicreasoningtasks: dateundershiftstheemphasistowardsunderstandingthein- standing(Suzgunetal.,2023a)andCoinflip(Wei
put. Therefore, RE2 exhibitssignificantcompati- et al., 2022b). Date understanding is a subset of
bilitywiththem,actingasa“plug&play”module. BigBench datasets (Suzgun et al., 2023a), which
This synergy has the potential to further enhance haveposedchallengesforpreviousfine-tuningefthe reasoning abilities of LLMs. With a specific forts. Coinflipisadatasetofquestionsonwhether

<!-- Page 4 -->

LLMs Methods GSM SVAMP ASDIV AQUA MultiArith SingleEQ AddSub

### Vanilla 19.48 67.60 69.00 28.74 31.33 86.22 89.87

davinci-003 Vanilla+RE2 24.79↑5.31 70.90↑3.30 71.20↑2.20 30.31↑1.57 42.33↑11.00 87.20↑0.98 92.15↑2.28

### CoT 58.98 78.30 77.60 40.55 89.33 92.32 91.39

CoT+RE2 61.64↑2.68 81.00↑2.70 78.60↑1.00 44.49↑3.94 93.33↑4.00 93.31↑0.99 91.65↑0.26

### Vanilla 77.79 81.50∗ 87.00∗ 63.78∗ 97.83∗ 95.28∗ 92.41∗

ChatGPT Vanilla+RE2 79.45↑1.66 84.20↑2.70 88.40↑1.40 59.45↓4.33 96.67↓1.16 94.49↓0.79 91.65↓0.76

### CoT 78.77 78.70 85.60 55.51 95.50 93.70 88.61

CoT+RE2 80.59↑1.82 80.00↑1.30 86.00↑0.40 59.45↑3.94 96.50↑1.00 95.28↑1.58 89.87↑1.26
Table1: Resultsonarithmeticreasoningbenchmarks. ∗denotesthatVanillaisevensuperiortoCoTprompting.
Commonsense Symbolic

### LLMs Methods


### CSQA StrategyQA ARC-e ARC-c ARC-t Date Coin

Vanilla 74.20∗ 59.74 84.81 72.01 80.58 40.92 49.80
davinci-003
Vanilla+RE2 76.99↑2.79 59.91↑0.17 88.22↑3.41 75.68↑3.67 84.07↑3.49 42.01↑1.09 52.40↑2.60

### CoT 71.66 67.55 85.69 73.21 81.57 46.07 95.60

CoT+RE2 73.05↑1.39 66.24↓1.31 87.84↑2.15 76.02↑2.81 83.94↑2.37 52.57↑6.50 99.60↑4.00
Vanilla 76.66∗ 62.36 94.32∗ 85.41∗ 91.37∗ 47.43∗ 52.00

### ChatGPT

Vanilla+RE2 78.38↑1.72 66.99↑4.63 93.81↓0.51 83.19↓2.22 90.30↓1.07 47.97↑0.54 57.20↑5.20

### CoT 69.94 67.82 93.35 83.53 90.11 43.63 88.80

CoT+RE2 71.66↑1.72 69.34↑1.52 93.14↓0.21 84.47↑0.94 90.27↑0.16 47.15↑3.52 95.20↑6.40
Table2: Resultsoncommonsenseandsymbolicreasoningbenchmarks. ∗denotesthatVanillaisevensuperiorto
CoTprompting.
acoinisstillheadsupafteritisflippedornotbased 0, thus leading to deterministic outputs. For
onstepsgiveninthequestions. theseexperiments,weemploytwopowerfulbackbones: ChatGPT (gpt-3.5-turbo-0613) (OpenAI,
3.2 LanguageModelsandImplementations 2022)anddavinci-003(text-davinci-003)2 ,across
all prompting methods, including Vanilla, CoT,

### BaselinePrompting. Inourimplementation,we


### Vanilla+RE2, and CoT+RE2. We also test RE2

rigorously evaluate the performance of our RE2
onmoreadvancedGPT-4o-miniinAppendixC.
modelontwobaselinepromptingmethods: Vanilla
and CoT. The Vanilla approach aligns with the
3.3 EvaluationResults
standardpromptingmethodoutlinedin(Weietal.,

### Table1presentstheresultsonarithmeticreasoning

2022b; Kojima et al., 2022), wherein no specific
datasets,andTable2oncommonsensereasoning
prompts are employed to elicit thoughts from
and symbolic reasoning. In almost all scenarios,
LLMs. Conversely, the CoT method guides the
modelthroughastep-by-stepthoughtprocess.
LLMswith RE2 achieveconsistentimprovements
acrossbothLLMs(davinci-003andChatGPT)and

### RE2 Prompting. Weincorporate RE2 intothese

promptingmethods(VanillaandCoT).Specifically,
baselinemethodstoassessitsimpact,denotedas
davinci-003withVanilla+RE2 showsaverageim-

### Vanilla+RE2andCoT+RE2. Toavoidtheimpact

provements of 3.81, 2.51, and 1.85 in arithmetic,
of randomness introduced by the demonstrations
commonsense, and symbolic tasks, respectively.
inafew-shotsetting,wemainlyassessourmethod
WithCoT,davinci-003generatesintermediatereainazero-shotsetting,following(Chenetal.,2023;
soningsteps,significantlyenhancingthereasoning
Wang et al., 2023a; Du et al., 2023). AdditionperformanceofLLMs. Byapplying RE2,davincially,fordifferenttasks,wedesignanswer-format
003withCoT+RE2demonstratesfurtherimproveinstructions in prompts to regulate the format of
ment, with average gains of 2.22, 1.23, and 5.25
thefinalanswer,facilitatingpreciseanswerextracinthesamecategories,respectively. Theseresults
tion. Detailedinformationregardingthebaseline
indicatethatRE2canbenefitLLMsindirectlygenprompting,RE2prompting,andanswer-formatinerating answers and improve the performance of
structionscanbefoundintheAppendixB.
CoTleadingtocorrectanswers.

### Implementations. Our decoding strategy uses

greedy decoding with a temperature setting of 2https://platform.openai.com/docs/models/gpt-3-5

<!-- Page 5 -->

81
80
79
78
77
1 2 3 4 5
Times of reading
ycaruccA
ChatGPT Vanilla ChatGPT CoT davinci-003 Vanilla davinci-003 CoT LLMs Methods GSM
61.64

## 89 6058.98 60.12 58.83 57.47 Ps 75.59


## 59 Ps+Re2 76.27

80.29 80.29 ChatGPT
50

## Pal 75.59


## 45 Pal+Re2 79.38

79.15 40

## 77 78.77 Ps 55.65


## 30 Ps+Re2 58.68

davinci-003
77.79 24.79
77.56 2019.48 18.8 18.35 17.06 P P A A L L+RE2 6 7 8 0 . . 6 2 1 0
1 2 3 4 5

### Times of reading

Table 3: Evaluation results of some thought-eliciting
promptingsbeyondCoTwithRE2.

### Figure3: Evaluationresultsofthetimesofreadingon

GSMbenchmark. reaches2or3,afterwhichitbeginstodeclinewith
furtherincreasesinquestionre-readingtimes. The
WhenappliedtoChatGPT, RE2exhibitsconsispotential reasons for inferior performance when
tent improvement on most datasets, except for a
readingthequestionmultipletimesaretwo-fold: i)
slightdropinperformanceonafewdatasets,e.g.,
appropriatereadingtimesincreaseLLMs’ability
AQUAandMultiArith,whenusingVanilla+RE2.
togeneratecorrectanswers. However,excessively
This exception could be due to ChatGPT’s exporepeatingquestionsmayserveasdemonstrations,
suretothesedatasetswithCoToutputsduringincausing the LLMs to repeat the questions themstructionfine-tuning(IFT)(Chenetal.,2023). On
selves(seeAppendixEfordetailedanalysis). and
suchdatasets,ChatGPTwithVanillastillproduces
ii)repeatingthequestionsignificantlyincreasethe
CoT-likeoutput(seeexamplesinAppendixG)and
inconsistencyoftheLLMsbetweenourinference
evenoutperformsChatGPTwithCoT(asindicated
andpretraining/alignment(intuitivelyinthelearnby the ∗ results in Tables 1 and 2). Chen et al.
ing corpora, we usually repeat a question twice).
(2023) obtained similar experimental results and
It’snoteworthythatreadingthequestiontwiceis
suggestedthatthisoccursbecauseChatGPTmay
optimalinmostscenarios,whichiswhywerefer
havebeen exposed to thesetask datasetscontaintoitas“re-reading”inourpaper.
ingCoTexplanationswithoutexplicitprompting.
Therefore,additionalexplicitinstructions,likeCoT Compatibility with Thought-Eliciting Prompt
orRE2,mightdisruptthislearnedpatterninChat- Strategies Compared to previous methods at-
GPT, possibly leading to decreased performance. tempting to elicit thoughts in the output from
Nonetheless, on some datasets like SVAMP, AS- LLMs,ourRE2 emphasizestheunderstandingof
DIV, CSQA, and Date, RE2 still manages to im- the input. Therefore, we are intrigued to explore
provethebaselineVanillaprompting. Moreover,in whether RE2 is effective with various thoughtdatasetswhereCoTpromptingnormallysurpasses eliciting prompting strategies other than CoT. To
Vanillaprompting,suchasGSM,StrategyQA,and investigatethis,weapplyRE2totwootherrecently
Coin,RE2significantlyenhancesVanillaprompt- introducedpromptingmethods,namely,Plan-anding(↑4.63onStrategyQAand↑5.20ontheCoin Solve (PS) (Wang et al., 2023a) and Programdataset). Overall, our RE2 method still achieves AidedLanguagemodels(PAL)(Gaoetal.,2023).
improvementsin71%oftheexperimentsonChat- Theformermodeldevisesaplantodividetheen-
GPT.Moreexamplesfromtheexperimentresults tiretaskintosmallersubtasks,andthencarriesout
canbefoundinAppendixG. thesubtasksaccordingtotheplan,whilethelatter
generatesprogramsastheintermediatereasoning
3.4 Discussions
steps. We directly apply our RE2 to these two
Times of Question Reading We delve deeper methodsbymakingasimplealterationtotheinput
intotheimpactofthetimesofquestionre-reading by repeating the question. Table 3 presents the
onreasoningperformance. Figure3illustrateshow evaluationfindingsontheGSMbenchmark. Our
theperformanceoftwodistinctLLMsevolvescon- observationsrevealaconsistenttrend,akintowhat
cerning various times of question re-reading. An wasobservedwithCoTprompting. Theseresults
overarchingpatternemergesacrossallmodels: per- suggestthattheeffectivenessofour RE2generally
formance improves until the number of re-reads extendsacrossvariouspromptingmethodologies.

<!-- Page 6 -->

LLMs Methods GSM SVAMP ASDIV AQUA MultiArith SingleEQ AddSub
Vanilla 16.98 69.10 70.56 28.34 38.67 83.46 88.86
davinci-003
Vanilla+RE2 19.02↑2.04 73.60↑4.50 73.23↑2.67 27.95↓0.39 46.00↑7.33 84.06↑0.60 89.37↑0.51

### CoT 56.63 78.90 79.96 46.45 96.16 90.94 88.60

CoT+RE2 60.12↑3.49 79.80↑0.90 81.21↑1.25 44.89↓1.56 96.83↑0.67 91.14↑0.20 89.37↑0.77
Table4: Evaluationresultsonarithmeticreasoningbenchmarksunderfew-shotsetting.
LLMs Methods GSM SVAMP ASDIV AQUA MultiArith SingleEQ AddSub
Vanilla 5.76 43.90 52.91 22.44 6.33 68.11 66.58

### Llama-2-13B

Vanilla+RE2 6.82↑1.06 47.90↑4.00 53.15↑0.24 17.32↓5.12 6.50↑0.17 69.68↑1.57 70.12↑3.54

### CoT 21.99 41.60 45.18 22.83 56.83 58.46 58.99

CoT+RE2 22.37↑0.38 46.50↑4.90 48.81↑3.63 24.80↑1.97 55.83↓0.99 66.34↑7.88 60.76↑1.77
Vanilla 11.60 56.60 61.31 20.08 24.67 77.17 80.25

### Llama-2-70B

Vanilla+RE2 13.50↑1.90 63.60↑7.00 64.66↑3.35 22.05↑1.97 25.00↑0.33 80.31↑3.14 84.05↑3.80

### CoT 49.73 66.90 68.08 37.80 79.83 80.51 74.18

CoT+RE2 56.71↑6.98 70.40↑3.50 70.42↑2.34 38.58↑0.78 88.83↑9.00 81.10↑0.59 69.37↓4.81
Table5: EvaluationresultsofLLAMA-2onarithmeticreasoningbenchmarks
CompatibilitywithFew-ShotPrompting Itis LLMs Methods GSM SVAMP
noteworthy that our proposed re-reading mecha-

### Vanilla 77.79 81.50

nism is compatible with few-shot prompting. To Vanilla+SC 85.60 87.37
demonstrate this compatibility, we conducted ex- ChatGPT Vanilla+RE2+SC 86.35† 87.74
perimentsonarithmeticreasoningtasksusingthe CoT 78.77 78.70

### CoT+SC 85.75 84.90

davinci-003 model, employing both Vanilla and

### CoT+RE2+SC 86.88† 87.70†

CoT prompting methods. The few-shot prompting strategy and exemplars used align with those
Table 6: Evaluation results of re-reading with selfpresented in (Wei et al., 2022b). For both the consistency(t-test,†denotep-value<0.05).

### Vanilla+RE2andCoT+RE2methods,weapplied

there-readingmechanismtotheexemplarsaswell. following(Kojimaetal.,2022). Theresultsarepre-
The resultsof these experiments arepresented in sentedinTable5. Theresultsclearlyindicatethat
Table4. Wecanobservethattheinclusionofthe the re-reading mechanism consistently enhances
re-reading mechanism consistently enhances the theperformanceofbothVanillaandCoTpromptperformance of both prompting methods, mirror- ing methods across most tasks when applied to
ingourfindingsinthezero-shotsetting. Llama-2models. Thisobservationunderscoresthe
generality of our approach and dispels concerns
Effect on Non-IFT Models In our primary ex- aboutpotentialdataleakagefromIFTduringtrainperiments,weemployedtheChatGPTanddavinci- ing. Thisalsounderscorestheversatilityof RE2,
003 models, which had undergone IFT training. whichcanbeeffectivelyemployedacrossvarious
Thesemodels,beingalignedwithhuman-likebe- modelscalesandtypes,regardlessofwhetherthey
havior, are better equipped to follow instructions haveundergoneIFTtrainingorarenon-IFTLLM.
effectively. Additionally, theymayhavebeenexposedtodatasetswithCoTpromptingduringtheir Compatibility with Self-consistency Existing
training,makingthe“re-reading”mechanismpo- researchindicatesthatthechain-of-thoughtprompttentiallymorebeneficialinrecallingexplanations. ingapproachcanbeenhancedbyadoptingtheself-
Togaugethebroaderapplicabilityofourapproach consistency method, which involves aggregating
andtoeliminateanyIFT-relatedimpacts,wecon- the majority final answer from multiple sampled
ductedexperimentsonnon-IFTpretrainedmodels: generations. We are also intrigued by the poten-
Llama-2-13B and Llama-2-70B (Touvron et al., tialforfurtherenhancingtheproposedre-reading
2023b). Llama-2 is an open-source model pre- mechanismusingthismethod. Consequently,we
trained on publicly available data without IFT or conductexperimentstestingtheintegrationof RE2
RLHFfine-tuning. WeevaluatedLlama-2onarith- with the self-consistency approach on the GSM
metic reasoning tasks under a zero-shot setting, benchmarkbyusingChatGPT.Thetemperatureis

<!-- Page 7 -->

400
350
300
250
200
150
100
50
0
<=3 4 5 6 7 >=8
Complexity (number of steps)
selpmas
eht
fo
rebmuN
370 total cases
326 C C o o r r r r e e c c t t w w . . C C o o T T+Re2 0.6
298
0.5
0.4
174 0.3
0.2 88
63
0.1
0.0
1 2 3 4
n-gram
llaceR
Prompt Vanilla CoT

### CoT

CoT+Re2 Q: {question} P0 #Answer format instruction# 77.79 78.77
A: Let’s think step by step.

### Q: {question}

Read the question again: {question} P1 79.45 80.59
# Answer format instruction#
A: Let’s think step by step.

### Q: {question}

Q: {question} P2 78.09 79.38
# Answer format instruction#
A: Let’s think step by step.

### Q: {question}

A: Let’s think step by step.
P3 Read the question again: {question} 79.08 80.36
# Answer format instruction#
A: Let’s think step by step.
Figure4: Leftfigure: modelperformanceversuscom-

### Q: {question}

plexityofquestions. X-axismeansthecomplexityof A: Let’s think step by step.

### P4 Q: {question} 78.09 79.38

questionsandY-axisreferstofrequency. Thegrayhist
# Answer format instruction#
means the number of total cases for each complexity. A: Let’s think step by step.

### Rightfigure: n-gramrecallbetweenthegenerationand

theinputquestion. Wetakethequestionandgeneration Table7: Resultsofdifferentre-readinginstructions.
asthereferenceandhypothesisrespectively.
tionduringthereasoningprocess.
setto0.7. Wereporttheresultsaveragedover10
The Impact of Different Re-Reading Instrucruns,wherewesampled10outputsindependently
tions We further conduct experiments to examfromtheLLMsineachrun. Table6demonstrate
thatself-consistencysignificantlyenhancestheperinetheinfluenceofRE2withinthecontextofCoT
prompting. Specifically,wedesignvariousinstrucformanceofbothpromptingmethods. Despiteselftions for question re-reading using ChatGPT on
consistency’saggregationofmultipleanswers,our
GSM8Kdataset. AsdepictedinP1andP2inTare-readingmechanismstillcontributestoimproveble 7, instruction P1, which includes the phrase
mentonmostscenarios,indicatingitscompatibility
“Read the question again:",exhibitssuperior
withtheself-consistencyapproach.
performance compared to directly repeating the
Performance across Different Question Com- questiontwice. Theseresultssuggestthatprovidplexity. Wefurtherinvestigatetheimpactofinput ing more detailed re-reading instructions to the
questioncomplexityonthereasoningperformance LLMsisadvantageous. Subsequently,weexplore
ofbothCoTandCoT+RE2promptingsusingChat- the possibility of introducing re-reading for CoT
GPTonGSM8Kdataset,asshownintheleftpart instructions (i.e. repeating “Let’s think step
of Figure 4. In accordance with Fu et al. (2022), by step"),asexemplifiedinP3andP4. However,
wemeasurequestioncomplexitybycountingthe weobservethatrepeatingthethinkingprocesstwo
reasoningstepspresentintheground-truthexpla- timesdoesnotyieldanydiscerniblebenefits. It’s
nations. Ourfindingsrevealthattheperformance noteworthy that, in general, question re-reading
ofallpromptingsgenerallydiminishesasquestion consistentlyimprovesreasoningperformancecomcomplexity increases, suggesting that the current paredtothestandardCoTpromptingwithoutques-
LLMsstillstrugglewithhandlingintricatequeries. tionre-reading(P0).

### Notably, the introduction of re-reading enhances

performance on various complexities, including ImpactonInferenceEfficiencyandMemoryUsthose slightly complex questions. This observa- age. Re2doublesthequestionlengthinbothzerotionunderscoresthebenefitsof RE2 forimproving andfew-shotsettings,whichmayaffectinference
reasoningcapabilitiesovercomplexquestions. To efficiencyandmemoryusage. Thissectionquantifurthervalidatetheimprovedunderstandingability, tativelyexploresthatimpact. WeutilizeLlama-2
we calculate the coverage degree (n-gram recall) 7B with float16 precision and randomly sample
betweenthegenerationsandtheinputquestions,as 100instancesfromtheGSM8Kdataset. WemeaillustratedintherightpartofFigure4. Theresults sure the average inference time and memory usindicatethatRE2increasesthen-gram(n=1,2,3,4) ageacrossfourscenarios: Zero-shot,Zero-shot+
recallintheoutputexplanations,underscoringhow CoT, Few-shot, and Few-shot + CoT. When apourmethodenhancesthemodel’sfocusontheques- plying Re2, the questions in the demonstrations

<!-- Page 8 -->

2.5
2.0
1.5
1.0
0.5
0.0
Zero-shot Zero-shot CoT Few-shot Few-shot CoT
)s(
emiT
ecnerefnI
Inference Time Comparison
+4.07%

### Baseline

+Re2 +22.45%
-10.81%
+12.50%
15000
10000
5000
0
Zero-shot Zero-shot CoT Few-shot Few-shot CoT

## )Bm(

egasU

## Upg

plex reasoning tasks by generating intermediate
stepsexplicitly. Therefore,mostoftheendeavors
arededicatedtoimprovingthebasicprincipleby
the following aspects: i) the structure of “chain”,
e.g., tree (Yao et al., 2023a), graph (Yao et al.,
2023b); ii) the modality of the chain, e.g., pro-
GPU Usage Comparison gram (Gao et al., 2023); iii) the reliability of the
+0.17% -0.01% +3.84% +2.95% chain,e.g.,self-consistency(Wangetal.,2023c),
faithful (Lyu et al., 2023), retrieval-based verifying (He et al., 2023); and iv) decomposition of
the chain, e.g., least-to-most (Zhou et al., 2023),
decomposed(Radhakrishnanetal.,2023),plan-tosolve(Wangetal.,2023a). Incontrast,oursimple
Figure5: RE2’simpactoninferenceefficiencyandGPU
re-readingstrategyforLLMsisorthogonaltothese
memoryusage.
improvements via a trade-off between the intermediate steps and the query itself. Besides, our
arealsorepeated. Allexperimentsareperformed re-readingstrategyiscomplementarytomanypreon 8×NVIDIA GeForce RTX 4090 GPUs, with viousworksbypreventingtheanswerfrombeing
results shown in Figure 5. The findings reveal derived overwhelmingly from the CoT but overthatRE2onlymarginallyincreasesinferencetime lookingtheoriginalquery.
andmemoryusageinbothzero-shotandfew-shot
settings, even with longer inputs. This minimal Re-readingStrategyinNLP. Indeeplearning,
impactisattributedtovariousoptimizationandin- thesuccessofperformingtext-understandingtasks
ferenceaccelerationtechniquesincurrentLLMs, (Song et al., 2018; Luo et al., 2019a; Yang et al.,
such as grouped-query attention (Touvron et al., 2019; Lei et al., 2019) depends on the heuristics
2023b),CUDA,andGPU-basedcomputations. For of human reading strategy, e.g., pre-reading, reinstance, grouped-query attention is particularly readingandpost-reading(Saricoban,2002;Toprak
advantageous for long inputs, significantly accel- and ALMACIOG˘LU, 2009; Pressley and Afflererating decoder inference. Likewise, CUDA and bach,2012;OzekandCivelek,2006;Dowhower,
GPU-basedcomputationsarehighlyoptimizedfor 1989). Specifically,manyeffectivealgorithmshave
parallelprocessing,especiallyformatrixmultipli- been crafted around the idea of re-reading. AlcationsinLLMs(NVIDIA,2024). though deep architectures, from multi-layer Bi-

### LSTM(Huangetal.,2015)toTransformer-encoder

4 RelatedWork (Vaswanietal.,2017),havetheirmechanismsthat
provideaformof“re-reading”,thenotionthatsim-
Reasoning with Large Language Models. ply processing an input once might not be suffi-
LLMsrepresentasignificantmilestoneinthejour- cient for understanding or generating a complex
ney towards artificial general intelligence (AGI) outputhasbeenlong-standing. Initially,Shaetal.
(OpenAI, 2023; Touvron et al., 2023b) . Rea- (2016) and Sha et al. (2017) found that repeated
soning ability is particularly crucial on the way readingmechanismsdoimproveperformanceon
towards AGI, where artificial intelligence needs some tasks, e.g., sentiment analysis, semantic reto act or think like human beings (Qiao et al., lation classification, and event extraction. Then,
2023; Huang and Chang, 2023). In the literature LiuandLi(2016)proposetomimictherepeated
onLLMs,performingreasoningtasksviainterac- readingstrategyandpresentneuralnetworkswith
tioninnaturallanguageplaysasignificantrolein multi-levelattention,whichisproveneffectivein
evaluating an LLM, into which academia and in- recognizing implicit discourse relations. Sequendustryhavebeendedicatingmanyendeavors(Wei tially, Zhu et al. (2018) propose a multi-glance
et al., 2022a; Suzgun et al., 2023b; Turpin et al., mechanism,modelingthehabitofreadingbehavior,
2023). Inprinciple,mostworksforreasoningwith whichcanbenefitawiderangeoftasks. Luoetal.
largelanguagemodelscouldfallintotheparadigm (2019b)adoptanetworktoencodethegistofparaof“Chain-of-Thought”(Weietal.,2022b;Kojima graphs for rough reading and a decision-making
etal.,2022),whichassistsLLMsinfulfillingcom- policyforcarefulreading,whichcanimproveex-

<!-- Page 9 -->

tractive summarization. More recently, Springer 6 Limitations
et al. (2024) have shown the effectiveness of re-
In this paper, we introduce a simple yet effecpeating input to get bidirectional embeddings on
tivepromptingmethodforenhancingreasoningin
text embedding tasks. Therefore, it is natural to
LLMsandconductextensiveexperimentstovaliintroduce a re-reading strategy to LLMs’ reasondateitseffectiveness. Despiteourbestefforts,there
ing,sincetheTransformer-decoderarchitectureof
may be still some limitations that remain in our

### LLMs with unidirectional attention mechanisms

study. Ourinvestigationprimarilyrevolvesaround
hinderstheimplicitbidirectionalcapability.
empirical studies with extensive experiments to
validate RE2, similar to most works in prompt-
KnowledgeRecall. Fromtheperspectiveofin- ingresearch(Zhengetal.,2023;Yinetal.,2023;
formationseeking,promptingLLMscanbeseenas Gaoetal.,2023). Futureeffortswillincludemore
asortof“knowledgerecall”viaaparametricfash- theoreticalanalysestoprovideasolidfoundation.
ion, where the prompt can be seen as a retrieval Additionally, RE2 marginallyincreasestheinput
query. Incontrasttoconventionalnon-parametric length, leading to a slight reduction in efficiency
retrieval–vectordatabase(Karpukhinetal.,2020; forlongerquestionsduringinference. Futurework
Izacard et al., 2022) for example, the LLM as a willexploremorescenariosexceptreasoning,such
neural knowledge model (Bosselut et al., 2019; asmulti-turndialogueandmulti-modalreasoning.

### AlKhamissietal.,2022)caneasilygeneralizefor

huge knowledge coverage, contributing to its ef- 7 Ethics
ficacy in broad applications. In the context of

### We conducted experiments on seven math-

CoT reasoning, (Chen et al., 2023) conjuncture
ematical reasoning benchmarks, comprising
thatLLMcanbeexposedtocertainCoTsduring

### GSM8K(Cobbeetal.,2021),SVAMP(Pateletal.,

trainingandeasilycompletereasoningbyknowl-
2021), ASDiv (Miao et al., 2020), AQuA (Ling
edge recall. As such, it is natural to adapt the
etal.,2017),AddSub(Hosseinietal.,2014),Multibasicbutprevalentqueryaugmentationtechnique

### Arith(RoyandRoth,2015),SingelEQ(Royetal.,

intheterm-basedretrievaldomain(DaiandCallan,
2015),threecommonsensereasoningbenchmarks
2019), which repeats the original query multiple
(CSQA (Talmor et al., 2019), StrategyQA (Geva
timesovertheaugmentedpart(Wangetal.,2023b;
etal.,2021),andARC(Clarketal.,2018)),andtwo
Shenetal.,2023),intopromptingLLMs.
symbolicbenchmarks(DateUnderstanding(Suzgunetal.,2023a)andCoinflip(Weietal.,2022b)).
5 ConclusionandFutureWorks Amongthese,GSM8KandSVAMPdatasetsutilize
codeundertheMITLicense,whileAQuA,StrategyQA,DateUnderstanding,Coinfliputilizecode
This paper introduces RE2, a simple and effecunder the Apache-2.0 license, and ARC utilizes
tive prompting method for LLM reasoning that
code under CC-BY-SA-4.0. The licenses for the
improves performance by "re-reading" the quesremainingdatasetsareunspecified.
tion. Byshiftingfocustotheinputphase,RE2 op-
The proposed prompts do not involve the coleratesindependentlyfromotherthought-eliciting
lection or utilization of personal information perpromptings. Moreover, it shows promise in fostainingtootherindividuals. Detailsregardingthe
teringbidirectionalcomprehensionofquestionsin
prompts used in our experiments are provided in
decoder-only LLMs. Our comprehensive experi-
Appendix §B. Furthermore, it is ensured that the
mentscoverawiderangeofreasoningbenchmarks,
prompts utilized in this research do not pose any
diverseLLMtypes,varioustasksettings,andcomthreattothesafetyorwell-beingofothers.
patibilityassessmentswithotherpromptingmethods,validatingtheefficacyandversatilityof RE2.

### Acknowledgements


### Ourfindingsencouragetheresearchcommunityto

prioritizeadeeperunderstandingofinputquestions, Wewouldliketothanktheanonymousreviewers
therebycomplementingexistingthought-eliciting for their constructive comments and suggestions.
prompting strategies. Future endeavors will aim ThisworkwassupportedbytheNationalNatural
toexploreitsversatilityinadditionalcontextsbe- Science Foundation of China (No.61925203 and
yondreasoning,includingmulti-turndialogueand No.U22B2021).
multi-modalreasoningapplications.

<!-- Page 10 -->

References SarahLynnDowhower.1987. Effectsofrepeatedreadingonsecond-gradetransitionalreaders’fluencyand
Badr AlKhamissi, Millicent Li, Asli Celikyilmaz,
comprehension. ReadingResearchQuarterly,pages
Mona T. Diab, and Marjan Ghazvininejad. 2022.
389–406.
A review on language models as knowledge bases.
CoRR,abs/2204.06031.
YilunDu,ShuangLi,AntonioTorralba,JoshuaBTenenbaum,andIgorMordatch.2023. Improvingfactual-

### KonstantineArkoudas.2023. Gpt-4can’treason. arXiv

ityandreasoninginlanguagemodelsthroughmultiapreprintarXiv:2308.03762.
gentdebate. arXivpreprintarXiv:2305.14325.
Maciej Besta, Nils Blach, Ales Kubicek, Robert Gerstenberger,LukasGianinazzi,JoannaGajda,Tomasz Zhengxiao Du, Yujie Qian, Xiao Liu, Ming Ding,
Lehmann,MichalPodstawski,HubertNiewiadomski, JiezhongQiu,ZhilinYang,andJieTang.2022. GLM:
PiotrNyczyk,etal.2023. Graphofthoughts: Solv- generallanguagemodelpretrainingwithautoregresingelaborateproblemswithlargelanguagemodels. siveblankinfilling. InProceedingsofthe60thAnarXivpreprintarXiv:2308.09687. nualMeetingoftheAssociationforComputational

### Linguistics (Volume 1: Long Papers), ACL 2022,

AndrewBlair-Stanek,NilsHolzenberger,andBenjamin Dublin, Ireland, May22-27, 2022, pages320–335.
VanDurme.2023. Cangpt-3performstatutoryrea- AssociationforComputationalLinguistics.
soning? arXivpreprintarXiv:2302.06100.

### Yao Fu, Hao Peng, Ashish Sabharwal, Peter Clark,

AntoineBosselut,HannahRashkin,MaartenSap,ChaiandTusharKhot.2022. Complexity-basedprompttanya Malaviya, Asli Celikyilmaz, and Yejin Choi.
ing for multi-step reasoning. arXiv preprint

## COMET:commonsensetransformersforautoarXiv:2210.00720.

maticknowledgegraphconstruction. InProceedings
ofthe57thConferenceoftheAssociationforCompu-

### Luyu Gao, Aman Madaan, Shuyan Zhou, Uri Alon,

tationalLinguistics,ACL2019,Florence,Italy,July
PengfeiLiu, YimingYang, JamieCallan, andGra-
28-August2,2019,Volume1: LongPapers,pages
hamNeubig.2023. PAL:program-aidedlanguage
4762–4779.AssociationforComputationalLinguismodels. In International Conference on Machine
tics.
Learning, ICML 2023, 23-29 July 2023, Honolulu,

### Hawaii,USA,volume202ofProceedingsofMachine

Tom Brown, Benjamin Mann, Nick Ryder, Melanie
LearningResearch,pages10764–10799.PMLR.
Subbiah,JaredDKaplan,PrafullaDhariwal,Arvind

### Neelakantan,PranavShyam,GirishSastry,Amanda


### MorGeva,DanielKhashabi,EladSegal,TusharKhot,

Askell, Sandhini Agarwal, Ariel Herbert-Voss,
DanRoth,andJonathanBerant.2021. Didaristotle
Gretchen Krueger, Tom Henighan, Rewon Child,
usealaptop? Aquestionansweringbenchmarkwith

### AdityaRamesh,DanielZiegler,JeffreyWu,Clemens

implicit reasoning strategies. Transactions of the
Winter, Chris Hesse, Mark Chen, Eric Sigler, Ma-
AssociationforComputationalLinguistics.
teusz Litwin, Scott Gray, Benjamin Chess, Jack
Clark, ChristopherBerner, SamMcCandlish, Alec
HangfengHe,HongmingZhang,andDanRoth.2023.
Radford, Ilya Sutskever, and Dario Amodei. 2020.
Languagemodelsarefew-shotlearners. InAdvances Rethinking with retrieval: Faithful large language
inNeuralInformationProcessingSystems. modelinference. CoRR,abs/2301.00303.
JiuhaiChen,LichangChen,HengHuang,andTianyi MohammadJavadHosseini,HannanehHajishirzi,Oren
Zhou. 2023. When do you need chain-of-thought Etzioni,andNateKushman.2014. Learningtosolve
promptingforchatgpt? CoRR,abs/2304.03262. arithmeticwordproblemswithverbcategorization.

### InProceedingsofthe2014ConferenceonEmpirical

PeterClark,IsaacCowhey,OrenEtzioni,TusharKhot, MethodsinNaturalLanguageProcessing(EMNLP).

### AshishSabharwal,CarissaSchoenick,andOyvind

Tafjord.2018. Thinkyouhavesolvedquestionan- Jie Huang and Kevin Chen-Chuan Chang. 2023. Toswering? tryarc,theai2reasoningchallenge. ArXiv, wardsreasoninginlargelanguagemodels: Asurvey.
abs/1803.05457. In Findings of the Association for Computational

### Linguistics: ACL2023,Toronto,Canada,July9-14,

Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian,
2023,pages1049–1065.AssociationforComputa-
MarkChen,HeewooJun,LukaszKaiser,Matthias
tionalLinguistics.
Plappert, Jerry Tworek, Jacob Hilton, Reiichiro
Nakano, Christopher Hesse, and John Schulman.

### Zhiheng Huang, Wei Xu, and Kai Yu. 2015. Bidi-


## Training verifiers to solve math word probrectionalLSTM-CRFmodelsforsequencetagging.

lems.
CoRR,abs/1508.01991.

### Zhuyun Dai and Jamie Callan. 2019. Context-aware

sentence/passagetermimportanceestimationforfirst GautierIzacard,MathildeCaron,LucasHosseini,Sestageretrieval. CoRR,abs/1910.10687. bastian Riedel, Piotr Bojanowski, Armand Joulin,
andEdouardGrave.2022. Unsuperviseddensein-
SarahLDowhower.1989. Repeatedreading: Research formationretrievalwithcontrastivelearning. Trans.
intopractice. TheReadingTeacher,42(7):502–507. Mach.Learn.Res.,2022.

<!-- Page 11 -->

VladimirKarpukhin,BarlasOguz,SewonMin,Patrick NVIDIA. 2024. Cuda c++ programming
S.H.Lewis,LedellWu,SergeyEdunov,DanqiChen, guide. https://docs.nvidia.com/cuda/
andWen-tauYih.2020. Densepassageretrievalfor cuda-c-programming-guide/index.html. Acopen-domainquestionanswering. InProceedingsof cessed: 2024-09-29.
the2020ConferenceonEmpiricalMethodsinNatural Language Processing, EMNLP 2020, Online, OpenAI.2022. Chatgpt: Optimizinglanguagemodels
November16-20,2020,pages6769–6781.Associa- fordialogue.
tionforComputationalLinguistics.

### ROpenAI.2023. Gpt-4technicalreport. arXiv,pages

TakeshiKojima,ShixiangShaneGu,MachelReid,Yu- 2303–08774.
takaMatsuo,andYusukeIwasawa.2022. Largelanguagemodelsarezero-shotreasoners. InNeurIPS. YesimOzekandMuharremCivelek.2006. Astudyon
theuseofcognitivereadingstrategiesbyeltstudents.
ZeyangLei,YujiuYang,MinYang,WeiZhao,JunGuo,
TheAsianEFLJournal,14(1):1–26.
and Yi Liu. 2019. A human-like semantic cogni-
Arkil Patel, Satwik Bhattamishra, and Navin Goyal.
tionnetworkforaspect-levelsentimentclassification.

## AreNLPmodelsreallyabletosolvesimple

In The Thirty-Third AAAI Conference on Artificial
math word problems? In Proceedings of the 2021
Intelligence, AAAI 2019, Honolulu, Hawaii, USA,
Conference of the North American Chapter of the
January 27 - February 1, 2019, pages 6650–6657.
AssociationforComputationalLinguistics: Human
AAAIPress.
LanguageTechnologies,pages2080–2094,Online.
AssociationforComputationalLinguistics.
WangLing,DaniYogatama,ChrisDyer,andPhilBlunsom.2017. Programinductionbyrationalegenera-
Michael Pressley and Peter Afflerbach. 2012. Verbal
tion: Learningtosolveandexplainalgebraicword
protocols of reading: The nature of constructively
problems. InProceedingsofthe55thAnnualMeetresponsivereading. Routledge.
ingoftheAssociationforComputationalLinguistics
(Volume1: LongPapers).
ShuofeiQiao,YixinOu,NingyuZhang,XiangChen,

### YunzhiYao,ShuminDeng,ChuanqiTan,FeiHuang,

Yang Liu and Sujian Li. 2016. Recognizing implicit
andHuajunChen.2023. Reasoningwithlanguage
discourserelationsviarepeatedreading: Neuralnetmodelprompting: Asurvey. InProceedingsofthe
workswithmulti-levelattention. InProceedingsof
61stAnnualMeetingoftheAssociationforComputhe2016ConferenceonEmpiricalMethodsinNattationalLinguistics(Volume1: LongPapers),ACL
ural Language Processing, EMNLP 2016, Austin,
2023,Toronto,Canada,July9-14,2023,pages5368–
Texas,USA,November1-4,2016,pages1224–1233.

### AssociationforComputationalLinguistics.

TheAssociationforComputationalLinguistics.
Ansh Radhakrishnan, Karina Nguyen, Anna Chen,

### LingLuo,XiangAo,YanSong,JinyaoLi,Xiaopeng

Carol Chen, Carson Denison, Danny Hernandez,

### Yang,QingHe,andDongYu.2019a. Unsupervised


### Esin Durmus, Evan Hubinger, Jackson Kernion,

neuralaspectextractionwithsememes. InProceed-

### KamileLukosiute,NewtonCheng,NicholasJoseph,

ingsoftheTwenty-EighthInternationalJointConfer-

### NicholasSchiefer,OliverRausch,SamMcCandlish,

enceonArtificialIntelligence,IJCAI2019,Macao,

### Sheer El Showk, Tamera Lanham, Tim Maxwell,

China, August 10-16, 2019, pages 5123–5129. ij-
Venkatesa Chandrasekaran, Zac Hatfield-Dodds,
cai.org.

### JaredKaplan,JanBrauner,SamuelR.Bowman,and

Ethan Perez. 2023. Question decomposition im-

### LingLuo,XiangAo,YanSong,FeiyangPan,MinYang,

provesthefaithfulnessofmodel-generatedreasoning.
andQingHe.2019b. ReadinglikeHER:humanread-
CoRR,abs/2307.11768.
inginspiredextractivesummarization. InProceedingsofthe2019ConferenceonEmpiricalMethods
SubhroRoyandDanRoth.2015. SolvinggeneralarithinNaturalLanguageProcessingandthe9thInter- metic word problems. In Proceedings of the 2015
nationalJointConferenceonNaturalLanguagePro- Conference on Empirical Methods in Natural Lancessing,EMNLP-IJCNLP2019,HongKong,China, guageProcessing.

### November3-7,2019,pages3031–3041.Association

forComputationalLinguistics. SubhroRoy,TimVieira,andDanRoth.2015. ReasoningaboutQuantitiesinNaturalLanguage. Transac-
Qing Lyu, Shreya Havaldar, Adam Stein, Li Zhang, tionsoftheAssociationforComputationalLinguis-
Delip Rao, Eric Wong, Marianna Apidianaki, and tics.
Chris Callison-Burch. 2023. Faithful chain-ofthoughtreasoning. CoRR,abs/2301.13379. Arif Saricoban. 2002. Reading strategies of successful readers through the three phase approach. The
Shen Yun Miao, Chao Chun Liang, and Keh Yih Su. ReadingMatrix,2(3).

## Adiversecorpusforevaluatinganddeveloping

Englishmathwordproblemsolvers. InProceedings Lei Sha, Baobao Chang, Zhifang Sui, and Sujian Li.
of the 58th Annual Meeting of the Association for 2016. Reading and thinking: Re-read LSTM unit
ComputationalLinguistics. fortextualentailmentrecognition. InCOLING2016,

<!-- Page 12 -->

26thInternationalConferenceonComputationalLin- BaptisteRozière,NamanGoyal,EricHambro,Faisal
guistics,ProceedingsoftheConference: Technical Azhar, et al. 2023a. Llama: Open and effi-
Papers,December11-16,2016,Osaka,Japan,pages cient foundation language models. arXiv preprint
2870–2879.ACL. arXiv:2302.13971.

### Lei Sha, Feng Qian, and Zhifang Sui. 2017. Will re-

Hugo Touvron, Louis Martin, Kevin Stone, Peter Alpeatedreadingbenefitnaturallanguageunderstandbert, Amjad Almahairi, Yasmine Babaei, Nikolay
ing? In Natural Language Processing and Chi-
Bashlykov,SoumyaBatra,PrajjwalBhargava,Shruti
neseComputing-6thCCFInternationalConference,
Bhosale, et al. 2023b. Llama 2: Open founda-

### NLPCC2017,Dalian,China,November8-12,2017,

tion and fine-tuned chat models. arXiv preprint
Proceedings,volume10619ofLectureNotesinComarXiv:2307.09288.
puterScience,pages366–379.Springer.
Tao Shen, Guodong Long, Xiubo Geng, Chongyang Miles Turpin, Julian Michael, Ethan Perez, and
Tao,TianyiZhou,andDaxinJiang.2023. Largelan- Samuel R. Bowman. 2023. Language models
guagemodelsarestrongzero-shotretriever. CoRR, don’t always say what they think: Unfaithful exabs/2304.14233. planations in chain-of-thought prompting. CoRR,
abs/2305.04388.
YanSong,ShumingShi,andJingLi.2018. Jointlearningembeddingsforchinesewordsandtheircompo-

### Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob

nents via ladder structured networks. In Proceed-
Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz
ingsoftheTwenty-SeventhInternationalJointCon-
Kaiser,andIlliaPolosukhin.2017. Attentionisall
ferenceonArtificialIntelligence,IJCAI2018,July
youneed. InAdvancesinNeuralInformationPro-
13-19,2018,Stockholm,Sweden,pages4375–4381.
cessingSystems30: AnnualConferenceonNeural
ijcai.org.
InformationProcessingSystems2017,December4-9,
2017,LongBeach,CA,USA,pages5998–6008.

### Jacob Mitchell Springer, Suhas Kotha, Daniel Fried,

GrahamNeubig,andAditiRaghunathan.2024. Repetitionimproveslanguagemodelembeddings. Lei Wang, Wanyu Xu, Yihuai Lan, Zhiqiang Hu,
Yunshi Lan, Roy Ka-Wei Lee, and Ee-Peng Lim.
Mirac Suzgun, Nathan Scales, Nathanael Schärli, Se- 2023a. Plan-and-solveprompting: Improvingzerobastian Gehrmann, Yi Tay, Hyung Won Chung, shot chain-of-thought reasoning by large language
AakankshaChowdhery,QuocV.Le,EdChi,Denny models. arXivpreprintarXiv:2305.04091.
Zhou,andJasonWei.2023a. Challengingbig-bench
tasksandwhetherchain-of-thoughtcansolvethem.
Liang Wang, Nan Yang, and Furu Wei. 2023b.
In Findings of the Association for Computational
Query2doc: Query expansion with large language
Linguistics: ACL2023,Toronto,Canada,July9-14,
models. CoRR,abs/2303.07678.
2023,pages13003–13051.AssociationforComputationalLinguistics.
XuezhiWang, JasonWei, DaleSchuurmans, QuocV.
Mirac Suzgun, Nathan Scales, Nathanael Schärli, Se- Le,EdH.Chi,SharanNarang,AakankshaChowdbastian Gehrmann, Yi Tay, Hyung Won Chung, hery, and Denny Zhou. 2023c. Self-consistency
AakankshaChowdhery,QuocV.Le,EdChi,Denny improves chain of thought reasoning in language
Zhou,andJasonWei.2023b. Challengingbig-bench models. InTheEleventhInternationalConference
on Learning Representations, ICLR 2023, Kigali,
tasksandwhetherchain-of-thoughtcansolvethem.
In Findings of the Association for Computational Rwanda,May1-5,2023.OpenReview.net.

### Linguistics: ACL2023,Toronto,Canada,July9-14,

2023,pages13003–13051.AssociationforComputa- Jason Wei, Yi Tay, Rishi Bommasani, Colin Raffel,
tionalLinguistics. Barret Zoph, Sebastian Borgeaud, Dani Yogatama,
MaartenBosma,DennyZhou,DonaldMetzler,EdH.
Alon Talmor, Jonathan Herzig, Nicholas Lourie, and Chi, Tatsunori Hashimoto, Oriol Vinyals, Percy
JonathanBerant.2019. CommonsenseQA:Aques- Liang,JeffDean,andWilliamFedus.2022a. Emertion answering challenge targeting commonsense gentabilitiesoflargelanguagemodels. Trans.Mach.
knowledge. InProceedingsofthe2019Conference Learn.Res.,2022.
of the North American Chapter of the Association
for Computational Linguistics: Human Language
JasonWei,XuezhiWang,DaleSchuurmans,Maarten
Technologies,Volume1(LongandShortPapers).

### Bosma,BrianIchter,FeiXia,EdH.Chi,QuocV.Le,

ElifToprakandGamzeALMACIOG˘LU.2009. Three andDennyZhou.2022b. Chain-of-thoughtprompting elicits reasoning in large language models. In
readingphasesandtheirapplicationsintheteaching
NeurIPS.
ofenglishasaforeignlanguageinreadingclasses
withyounglearners. JournaloflanguageandLinguisticStudies,5(1). Xiaohan Xu, Ming Li, Chongyang Tao, Tao Shen,

### ReynoldCheng,JinyangLi,CanXu,DachengTao,

HugoTouvron,ThibautLavril,GautierIzacard,Xavier andTianyiZhou.2024. Asurveyonknowledgedis-
Martinet,Marie-AnneLachaux,TimothéeLacroix, tillationoflargelanguagemodels.

<!-- Page 13 -->


### Min Yang, Qiang Qu, Wenting Tu, Ying Shen, Zhou

Zhao, andXiaojunChen.2019. Exploringhumanlikereadingstrategyforabstractivetextsummarization. In The Thirty-Third AAAI Conference on ArtificialIntelligence,AAAI2019,Honolulu,Hawaii,
USA, January 27 - February 1, 2019, pages 7362–

### AAAIPress.

Shunyu Yao, Dian Yu, Jeffrey Zhao, Izhak Shafran,

### Thomas L. Griffiths, Yuan Cao, and Karthik

Narasimhan. 2023a. Tree of thoughts: Deliberate
problemsolvingwithlargelanguagemodels. CoRR,
abs/2305.10601.
Yao Yao, Zuchao Li, and Hai Zhao. 2023b. Beyond chain-of-thought, effective graph-of-thought
reasoning in large language models. CoRR,
abs/2305.16582.
Zhangyue Yin, Qiushi Sun, Cheng Chang, Qipeng
Guo,JunqiDai,XuanjingHuang,andXipengQiu.

## Exchange-of-thought: Enhancing large languagemodelcapabilitiesthroughcross-modelcommunication. InProceedingsofthe2023Conference

onEmpiricalMethodsinNaturalLanguageProcessing,pages15135–15153,Singapore.Associationfor
ComputationalLinguistics.

### ChuanyangZheng,ZhengyingLiu,EnzeXie,Zhenguo

Li, and Yu Li. 2023. Progressive-hint prompting
improvesreasoninginlargelanguagemodels. CoRR,
abs/2304.09797.
Denny Zhou, Nathanael Schärli, Le Hou, Jason Wei,
Nathan Scales, Xuezhi Wang, Dale Schuurmans,
ClaireCui,OlivierBousquet,QuocV.Le,andEdH.
Chi. 2023. Least-to-most prompting enables complex reasoning in large language models. In The
EleventhInternationalConferenceonLearningRepresentations,ICLR2023,Kigali,Rwanda,May1-5,

#### OpenReview.net.

PengchengZhu,YujiuYang,WenqiangGao,andYiLiu.

## Multi-glance reading model for text understanding. In Proceedings of the Eight Workshop

on Cognitive Aspects of Computational Language
LearningandProcessing,pages27–35,Melbourne.
AssociationforComputationalLinguistics.

<!-- Page 14 -->

A Datasets inclusionofRE2,thegenerationprocessmaintains
a higher attention weight on the question tokens.
Table 10 presents statistics and examples for the
Bycalculatingtheproportionofattentionweights
reasoningbenchmarksweconsidered.
assignedtothequestiontokensduringgeneration,
weobserveanincreasefrom0.32to0.40withthe

### B SpecificPromptingMethods

utilizationof RE2. Thisfindingsuggeststhatthe
Detailedinformationregardingvariouspromptings re-readingmechanismenhancesthemodel’sfocus
isshowninTable11andTable12. Theinstructions onthequestionduringthereasoningprocess.
ofanswer-formatcanbefoundinTable13.

### E PerplexityAnalysis


### C GPT-4o-miniExperiments


### LLMs are rapidly evolving, with more powerful

models emerging frequently. To assess the effectivenessof RE2 onnewer,moreadvancedmodels,
4.5
wetesteditonGPT-4o-mini,specificallythegpt-
4o-mini-2024-07-18 version 3. The results, pre-
4.0
sentedinFigure8andFigure9,demonstratethat
RE2continuestoperformeffectivelyonthesemore
advancedLLMs. 3.5
D AttentionAnalysis
3.0
2.5
Firstpass

### Firstpass

Secondpass 2.0
CoT CoT
1 2 3 4

### Times of reading


### Generation Generation

Firstpass CoT Generation Firstpass Secondpass CoT Generation
(a)CoT (b)CoT+RE2
Figure6: AttentionvisualizationwithandwithoutRE2.
(a)CoTprompting: thereisonlyonepassforthequestion. (b)CoT+RE2re-readsthequestion,includingfirst
passandsecondpass. Therowofmatrixrepresentsthe
querytokensandthecolumnrepresentsthekeytokens.

### TogaindeeperinsightsintohowRE2reshapes

attentionduringinference,wevisualizetheattention distribution by computing the average attentionweightsacrossallheadsandlayersinLlama-2.
The results are presented in Figure 6, revealing
twokeyfindings: (1)Intheblockof“Secondpass”
attending to the “First pass” as shown in (b) for

### CoT+RE2, we observe explicit attentions in the

uppertriangle. Thisobservationindicatesthattokensinthesecondquestioncanfocusonthetokens
behindthecorrespondingpositionsinthefirstquestion. In this way, RE2 enables a “bidirectional”
understanding of the question. Notably, with the
3https://platform.openai.com/docs/models/
gpt-4o-mini
ytixelpreP
Question Ground-Truth Answer
4.66 4.61 4.63
4.54
1.9
1.84 1.83 1.8

### Figure7: Theperplexityofgeneratingthequestionor

theground-truthanswerwithincreasingreadingtimes.
Fortheexplanationabout“overlyrepeatingquestions encourages LLMs to repeat the question
ratherthangeneratetheanswer”inSection3.4,we
conducted an experiment. This experiment aims
to investigate the likelihood of generating questionsversusgeneratingground-truthresponsesas
readingtimesofthequestionincreased. Wepose
tworesearchquestions: (1)Doestheprobabilityof
generatingthequestionastheoutputincreasewith
more reading times? (2) Does the probability of
generatingtheground-truthresponsedecreasewith
morereadingtimes?

### Specifically, for each question in the GSM8k

dataset, we provide the LLM with the question
withvaryingrepetitiontimesasinput,andsetthe
LLM’soutputasthequestionitselforitsgroundtruthresponse. Wethencalculatetheperplexityof
generatingboththequestionandtheground-truth
answer. Perplexityservesasanindicatorreflecting
thelikelihoodofgeneratingasequence,withlower

<!-- Page 15 -->

LLMs Methods GSM SVAMP ASDIV AQUA MultiArith SingleEQ AddSub

### Vanilla 93.40 93.70 95.13 83.46 97.83 97.05 95.70

Vanilla+RE2 94.09↑0.69 94.50↑0.80 95.28↑0.15 82.68↓0.78 98.00↑0.17 96.46↓0.59 97.22↑1.52

### GPT-4o-mini


### CoT 92.87 93.80 94.80 80.31 97.50 96.85 95.95

CoT+RE2 93.80↑0.93 94.20↑0.40 95.09↑0.29 82.28↑1.97 98.83↑1.33 97.05↑0.20 97.72↑1.77
Table8: ResultsonarithmeticreasoningbenchmarksforGPT-4o-mini.
Commonsense Symbolic

### LLMs Methods


### CSQA StrategyQA ARC-e ARC-c Date Coin


### Vanilla 82.56 75.02 95.12 92.15 66.40 99.80

Vanilla+RE2 83.95↑1.39 76.99↑1.97 95.16↑0.04 93.17↑1.02 75.07↑8.67 100.00↑0.20

### GPT-4o-mini


### CoT 82.64 79.13 95.58 93.60 70.73 100.00

CoT+RE2 83.78↑1.14 79.52↑0.39 95.45↓0.13 93.34↓0.26 79.40↑8.67 99.80↓0.20
Table9: ResultsoncommonsenseandsymbolicreasoningbenchmarksforGPT-4o-mini.
perplexity indicating a higher likelihood. These and ChatGPT in the Vanilla prompting (e.g. no
experimentsareconductedusingtheLlama2. The instruction)inTables21-24. TheyshowthatChatperplexityresultsaresummarizedinFigure7. GPTwithVanilladirectlygeneratesanswerinCoin
The results reveal two key findings: (1) The Filp and Date Understanding dataset (Tables 21-
perplexityofgeneratingquestionsdecreaseswith 22), but still generates CoT output in some other
increasingreadingtimes,suggestingthattheLLM datasets(Tables23-24).
findsiteasiertogeneratethequestion. (2)Withthe
exceptionofwhenreadingtimes=2,theperplexity
ofgeneratingtheground-truthresponseincreases
overall. This finding aligns with optimal performance observed when the question is read only
twice. Moreover, as reading times increase, the
LLM appears to be less inclined to generate the
answer.

### F CaseStudy

We also conduct a case study to show the effectivenessofourproposedre-readingpromptingover
the chain-of-thought. We choose two examples
fromGSM,andtheresultsgeneratedbyChatGPT
are listed in Table 14-15. It is evident that our
method can better align the evidence in the questionwiththecorrespondingexplanationhints. We
canobservethatCoT+RE2 tendstohighlightthe
importantevidencesinthequestionbeforegeneratingtheexplanation,forexample,“Inthemorning,
she gives 15 cups of feed, and in the afternoon,
shegivesanother25. So..."inTable14and“The
bonusisworthhalfamonth’ssalary,whichis..."
in Table 15. This observation is also consistent
withtherightfigureinFigure4.

### G MoreCases


### Tables16-20providemoreexamplesgeneratedby

ChatGPT with CoT and CoT+RE2. We also provide several examples generated by davinci-003

<!-- Page 16 -->


### Dataset Type N Answer Example

GSM8K Math 1319 Number Joshdecidestotryflippingahouse.Hebuysahousefor$80,000andthenputs
in$50,000inrepairs.Thisincreasedthevalueofthehouseby150%.Howmuch
profitdidhemake?
SVAMP Math 1000 Number Afterrestingtheydecidedtogoforaswim.Thedepthofthewateris15times
Dean’sheight.Deanis4feettallerthanRon.IfRonstandsat13feet.Howdeep
wasthewater?
ASDIV Math 2096 Number Thereare3300bananasinJanice’sbananacollection.Janicealsohas5crayons.

### Ifthebananasareorganizedinto75groups,howbigiseachgroup?

AQUA Math 254 Option Theoriginalpriceofanitemisdiscounted22%.Acustomerbuystheitemat
thisdiscountedpriceusinga$20-offcoupon.Thereisnotaxontheitem,and
thiswastheonlyitemthecustomerbought. Ifthecustomerpaid$1.90more
thanhalftheoriginalpriceoftheitem,whatwastheoriginalpriceoftheitem?
AnswerChoices:A)$61,B)$65,C)$67.40,D)$70,E)$78.20.
MultiArith Math 600 Number FortheschoolbakesaleRobinmade42cupcakes.Ifshesold22ofthemand
thenmade39more,howmanycupcakeswouldshehave?
SingleEq Math 508 Number Alyssaspenthalfofherallowancegoingtothemovies.Shewashedthefamily
carandearned8dollars. Whatisherweeklyallowanceifsheendedwith12
dollars?
AddSub Math 395 Number Mikehad34peachesathisroadsidefruitdish. Hewenttotheorchardand
pickedpeachestostockup.Therearenow86peaches.howmanydidhepick?
CSQA CS 1221 Option Wherewouldyoufindmagazinesalongsidemanyotherprintedworks?Answer
Choices:A)doctor,B)bookstore,C)market,D)trainstation,E)mortuary.
StrategyQA CS 2290 Yes/No DotheanchorsonRedeGlobospeakChinese?
ARC-e CS 2376 Option Theshapeofthemoonappearstochangeregularlyduringeachmonth.Which
ofthefollowingbestexplainswhytheshapeofthemoonappearstochange?
AnswerChoices:A)TheEarthturnsonitsaxis,B)TheMoonturnsonitsaxis,
C)TheMoonorbitsaroundtheEarth,D)CloudscovertheMoon.
ARC-c CS 1172 Option Whatisasimilaritybetweensoundwavesandlightwaves? AnswerChoices:
A)Bothcarryenergy,B)Bothtravelinvacuums,C)Botharecausedbyvibrations,
D)Botharetravelingatthesamespeed.
DateUnderstanding Sym. 369 Date YesterdaywasApril30,2021.WhatisthedatetodayinMM/DD/YYYY?
CoinFlip Sym. 500 Yes/No Acoinisheadsup. Breannaflipsthecoin. Treydoesnotflipthecoin. Omar
flipsthecoin.Patricedoesnotflipthecoin.Isthecoinstillheadsup?Notethat
"flip"heremeans"reverse".
Table 10: Details of reasoning benchmarks. Math: arithmetic reasoning. CS: commonsense reasoning. Sym.:
symbolicreasoning.

<!-- Page 17 -->

Methods PromptContent

### Q: {question}

Vanilla #Answer format instruction#

## A:


### Q: {question}

Read the question again: {question}

### Vanilla+RE2

# Answer format instruction#

## A:


### Q: {question}

CoT #Answer format instruction#
A: Let’s think step by step.

### Q: {question}

Read the question again: {question}

### CoT+RE2

# Answer format instruction#
A: Let’s think step by step.

### Q: {question}

# Answer format instruction#
A: Let’s first understand the problem and devise a plan to solve the problem.

## Ps

Then, let’s carry out the plan, solve the problem step by step,
and give the ultimate answer. Please explicitly generate the mentioned process:
[Problem Understanding], [Plan], [Solving/Calculations], [Answer]. in your response.

### Q: {question}

Read the question again: {question}
# Answer format instruction#
PS+RE2 A: Let’s first understand the problem and devise a plan to solve the problem.
Then, let’s carry out the plan, solve the problem step by step,
and give the ultimate answer. Please explicitly generate the mentioned process:
[Problem Understanding], [Plan], [Solving/Calculations], [Answer]. in your response.
Table11: SpecificpromptsofVanilla,Vanilla+RE2,CoT,CoT+RE2,PS,andPS+RE2.

<!-- Page 18 -->

Methods PromptContent
#!/bin/python3
import math
import numpy as np
import statistics
import sympy as sp
########### Task Instruction ##############
# You will write python program to solve math problems.
# You will only write code blocks.
# Please generate your code block in ‘def solution()‘ function, and thus it can be
executed by python interpreter. You don’t need to call ‘solution()‘ function because

## Pal

it will be called by the system.
# The concrete format of ‘solution()‘ is as follows:
# def solution():
# """<question>"""
# <your code>
# result = <your result>
# return result
#########################################
# Q: {question}
# Your defined "solution()" function with comments here.
#!/bin/python3
import math
import numpy as np
import statistics
import sympy as sp
########### Task Instruction ##############
# You will write python program to solve math problems.
# You will only write code blocks.
# Please generate your code block in ‘def solution()‘ function, and thus it can be
executed by python interpreter. You don’t need to call ‘solution()‘ function because
PAL+RE2 it will be called by the system.
# The concrete format of ‘solution()‘ is as follows:
# def solution():
# """<question>"""
# <your code>
# result = <your result>
# return result
#########################################
# Q: {question}
# Read the question again: {question}
# Your defined "solution()" function with comments here.
Table12: SpecificpromptsofPALandPAL+RE2

<!-- Page 19 -->


### Tasks Answer-formatInstructions

Your final answer should be a single numerical number, in the form answer ,

## Gsm

at the end of your response.
Your final answer should be a single numerical number, in the form answer ,

## Svamp

at the end of your response.
Your final answer should be a single numerical number, in the form answer ,

## Asdiv

at the end of your response.
AQUA Your answer should be in the form choice . There is only one correct choice.
Your final answer should be a single numerical number, in the form answer ,

### MultiArith

at the end of your response.
Your final answer should be a single numerical number, in the form answer ,

### SingleEQ

at the end of your response.
Your final answer should be a single numerical number, in the form answer ,

### AddSub

at the end of your response.
CommonsenseQA Your answer should be in the form choice . There is only one correct choice.
StrategyQA Your answer should be either yes or no , in the form answer .
ARC Your answer should be in the form choice . There is only one correct choice.
Your answer should be a date, in the format of MM/DD/YYYY ,
DateUnderstanding
e.g. 05/01/2022 .
CoinFlip Your answer should be either yes or no , in the form answer .
Table13: Specificanswer-formatinstructionineachtask.

<!-- Page 20 -->

Q:Everyday,Wendifeedseachofherchickensthreecupsofmixedchickenfeed,containingseeds,mealwormsandvegetables
tohelpkeepthemhealthy. Shegivesthechickenstheirfeedinthreeseparatemeals. Inthemorning,shegivesherflockof
chickens15cupsoffeed.Intheafternoon,shegivesherchickensanother25cupsoffeed.Howmanycupsoffeeddoesshe
needtogiveherchickensinthefinalmealofthedayifthesizeofWendi’sflockis20chickens?(Answer:20)

### CoT


### Input:

Q:Everyday,Wendifeedseachofherchickensthreecupsofmixedchickenfeed,containingseeds,mealwormsandvegetables
tohelpkeepthemhealthy. Shegivesthechickenstheirfeedinthreeseparatemeals. Inthemorning,shegivesherflockof
chickens15cupsoffeed.Intheafternoon,shegivesherchickensanother25cupsoffeed.Howmanycupsoffeeddoesshe
needtogiveherchickensinthefinalmealofthedayifthesizeofWendi’sflockis20chickens?
Yourfinalanswershouldbeasinglenumericalnumber,intheform answer ,attheendofyourresponse.
A:Let’sthinkstepbystep.

### Output:

First,let’scalculatehowmuchfeedWendigivesherchickensinthemorning.Shehas20chickens,andshegiveseachchicken3
cupsoffeed,sointotal,shegivesthem20x3=60cupsoffeedinthemorning.
Next,let’scalculatehowmuchfeedWendigivesherchickensintheafternoon.Again,shehas20chickens,andshegiveseach
chicken3cupsoffeed,sointotal,shegivesthem20x3=60cupsoffeedintheafternoon.
Tofindouthowmuchfeedsheneedstogiveherchickensinthefinalmealoftheday,weneedtosubtractthetotalfeedgivenin
themorningandafternoonfromthetotalfeedneededfortheday.Thetotalfeedneededforthedayfor20chickensis20x3x3
=180cupsoffeed.
So,thefeedneededinthefinalmealofthedayis180-60-60=60cupsoffeed.
Therefore,Wendineedstogiveherchickens60cupsoffeedinthefinalmealoftheday.
Answer: 60
CoT+RE2

### Input:

Q:Everyday,Wendifeedseachofherchickensthreecupsofmixedchickenfeed,containingseeds,mealwormsandvegetables
tohelpkeepthemhealthy. Shegivesthechickenstheirfeedinthreeseparatemeals. Inthemorning,shegivesherflockof
chickens15cupsoffeed.Intheafternoon,shegivesherchickensanother25cupsoffeed.Howmanycupsoffeeddoesshe
needtogiveherchickensinthefinalmealofthedayifthesizeofWendi’sflockis20chickens?
Readthequestionagain:Everyday,Wendifeedseachofherchickensthreecupsofmixedchickenfeed,containingseeds,
mealwormsandvegetablestohelpkeepthemhealthy.Shegivesthechickenstheirfeedinthreeseparatemeals.Inthemorning,
shegivesherflockofchickens15cupsoffeed.Intheafternoon,shegivesherchickensanother25cupsoffeed.Howmanycups
offeeddoessheneedtogiveherchickensinthefinalmealofthedayifthesizeofWendi’sflockis20chickens?
Yourfinalanswershouldbeasinglenumericalnumber,intheform answer ,attheendofyourresponse.
A:Let’sthinkstepbystep.

### Output:

First,weneedtodeterminethetotalamountoffeedWendigivesherchickensinthemorningandafternoon.Inthemorning,she
gives15cupsoffeed,andintheafternoon,shegivesanother25cups.So,thetotalamountoffeedgiveninthemorningand
afternoonis15+25=40cups.
Next,weneedtodeterminethetotalamountoffeedneededforWendi’sflockof20chickens.Sinceeachchickenrequires3cups
offeed,wemultiply3by20toget60cups.
Finally,wesubtractthetotalamountoffeedgiveninthemorningandafternoonfromthetotalamountneeded.60-40=20
Therefore,Wendineedstogiveherchickens20cupsoffeedinthefinalmealoftheday.

### Answer: 20

Table14: GSMExample4(Complexity=3)

<!-- Page 21 -->

Q:Timgetsapromotionthatoffershima5%raiseonhis$20000amonthsalary.Italsogiveshimabonusworthhalfamonth’s
salary.Howmuchmoneywillhemakeinayear?(Answer:262500)

### CoT


### Input:

Q:Timgetsapromotionthatoffershima5%raiseonhis$20000amonthsalary.Italsogiveshimabonusworthhalfamonth’s
salary.Howmuchmoneywillhemakeinayear?
Yourfinalanswershouldbeasinglenumericalnumber,intheform answer ,attheendofyourresponse.
A:Let’sthinkstepbystep.

### Output:

First,let’scalculatethe5%raiseonTim’s$20000monthlysalary.Todothis,wemultiply$20000by5%(or0.05):
$20000*0.05=$1000
So,Tim’sraiseis$1000permonth.
Next,let’scalculatethebonusworthhalfamonth’ssalary.Halfof$20000is$10000,soTim’sbonusis$10000.
Now,let’scalculateTim’stotalmonthlysalaryaftertheraiseandbonus:
$20000(originalsalary)+$1000(raise)+$10000(bonus)=$31000
Finally,let’scalculateTim’sannualsalarybymultiplyinghismonthlysalaryby12:
$31000*12=$372000
Therefore,Timwillmake$372000inayear.So,theansweris 372000 .
CoT+RE2

### Input:

Q:Timgetsapromotionthatoffershima5%raiseonhis$20000amonthsalary.Italsogiveshimabonusworthhalfamonth’s
salary.Howmuchmoneywillhemakeinayear?
Readthequestionagain:Timgetsapromotionthatoffershima5%raiseonhis$20000amonthsalary.Italsogiveshimabonus
worthhalfamonth’ssalary.Howmuchmoneywillhemakeinayear?
Yourfinalanswershouldbeasinglenumericalnumber,intheform answer ,attheendofyourresponse.
A:Let’sthinkstepbystep.

### Output:

First,let’scalculatethe5%raiseonTim’s$20000monthlysalary.
Theraiseamountwouldbe5%of$20000,whichisequalto0.05*$20000=$1000.
So,Tim’snewmonthlysalarywouldbe$20000+$1000=$21000.
Next,let’scalculatethebonusamount.Thebonusisworthhalfamonth’ssalary,whichisequalto0.5*$21000=$10500.
Now,tofindouthowmuchmoneyTimwillmakeinayear,weneedtocalculatethetotalsalaryfor12monthsandaddthebonus.
Totalsalaryfor12months=$21000*12=$252000.
So,Timwillmakeatotalof$252000+$10500=$262500inayear.
Therefore,Timwillmake 262500 inayear.
Table15: GSMExample641(Complexity=6)

<!-- Page 22 -->

Q:Colbylovesgoingtothemoviesandeverymonthhisparentsgivehim$150tospendatthemovies.TicketsforFridaysand
Saturdayscost$10. Ticketsforanyotherdaycost$7. Popcorncosts$8andboxesofcandycost$2. Itisthelastdayofthe
monthandit’saFriday.Hewantstomakesurehegetsapopcornandboxofcandythatnight.Howmanymoviescanheseeif
healreadysaw5moviesonaFridayorSaturday,8moviesonotherdays,had2tubsofpopcorn,andfourboxesofcandythat
month?(Answer:1)

### CoT


### Input:

Q:Colbylovesgoingtothemoviesandeverymonthhisparentsgivehim$150tospendatthemovies.TicketsforFridaysand
Saturdayscost$10. Ticketsforanyotherdaycost$7. Popcorncosts$8andboxesofcandycost$2. Itisthelastdayofthe
monthandit’saFriday.Hewantstomakesurehegetsapopcornandboxofcandythatnight.Howmanymoviescanheseeif
healreadysaw5moviesonaFridayorSaturday,8moviesonotherdays,had2tubsofpopcorn,andfourboxesofcandythat
month?
Yourfinalanswershouldbeasinglenumericalnumber,intheform answer ,attheendofyourresponse.
A:Let’sthinkstepbystep.

### Output:

First,let’scalculatethecostofthemoviesColbyhasalreadyseen.Hehasseen5moviesonaFridayorSaturday,whichcost$10
each,sothatisatotalof5*$10=$50.Hehasalsoseen8moviesonotherdays,whichcost$7each,sothatisatotalof8*$7=
$56.Therefore,thetotalcostofthemovieshehasalreadyseenis$50+$56=$106.
Next,let’scalculatethecostofthepopcornandcandyhewantstobuyonthelastdayofthemonth.Thepopcorncosts$8and
thecandycosts$2,sothetotalcostofthesnacksis$8+$2=$10.
Now,let’ssubtractthecostofthemoviesColbyhasalreadyseenandthecostofthesnacksfromthe$150hisparentsgavehim.
$150-$106-$10=$34.
SinceeachmovieonaFridayorSaturdaycosts$10andColbyhas$34left,hecanseeamaximumof$34/$10=3moviesona
FridayorSaturday.
Inconclusion,Colbycanseeatotalof3+5=8moviesinthemonth.
8
CoT+RE2

### Input:

Q:Colbylovesgoingtothemoviesandeverymonthhisparentsgivehim$150tospendatthemovies.TicketsforFridaysand
Saturdayscost$10. Ticketsforanyotherdaycost$7. Popcorncosts$8andboxesofcandycost$2. Itisthelastdayofthe
monthandit’saFriday.Hewantstomakesurehegetsapopcornandboxofcandythatnight.Howmanymoviescanheseeif
healreadysaw5moviesonaFridayorSaturday,8moviesonotherdays,had2tubsofpopcorn,andfourboxesofcandythat
month?
Readthequestionagain:Colbylovesgoingtothemoviesandeverymonthhisparentsgivehim$150tospendatthemovies.
TicketsforFridaysandSaturdayscost$10.Ticketsforanyotherdaycost$7.Popcorncosts$8andboxesofcandycost$2.Itis
thelastdayofthemonthandit’saFriday.Hewantstomakesurehegetsapopcornandboxofcandythatnight.Howmany
moviescanheseeifhealreadysaw5moviesonaFridayorSaturday,8moviesonotherdays,had2tubsofpopcorn,andfour
boxesofcandythatmonth?
Yourfinalanswershouldbeasinglenumericalnumber,intheform answer ,attheendofyourresponse.
A:Let’sthinkstepbystep.

### Output:


### First,let’scalculatethetotalamountColbyhasspentsofar:

Forthe5moviesonFridaysandSaturdays,hespent5x$10=$50.Forthe8moviesonotherdays,hespent8x$7=$56.For
the2tubsofpopcorn,hespent2x$8=$16.Forthe4boxesofcandy,hespent4x$2=$8.
Addingalltheseexpensestogether,Colbyhasspent$50+$56+$16+$8=$130.
Now,let’scalculatehowmuchmoneyhehasleftfromthe$150hisparentsgavehim:
Colbystartedwith$150-$130=$20.
Sinceit’sthelastdayofthemonthandit’saFriday,hewantstobuyapopcorn($8)andaboxofcandy($2).Thismeanshewill
spend$8+$2=$10.
Therefore,Colbywillhave$20-$10=$10left.

### Now,let’scalculatehowmanymovieshecanseewiththeremaining$10:

SinceticketsonFridaysandSaturdayscost$10,andhehas$10left,hecansee1movieonaFridayorSaturday.
Therefore,Colbycansee1moremovieonthelastdayofthemonth.
So,thefinalansweris 1 .
Table16: GSMExample926(Complexity>=9)

<!-- Page 23 -->

Q:Mikewasapenpalwith5people.Hestoppedbeingpenpalswith2ofthem.Theyeachsend2lettersaweekthatare5pages
long.Herespondsinkind.Hecanwriteapageevery6minutes.Howmanyhoursdoeshespendwritingaweek?(Answer:3)

### CoT


### Input:

Q:Mikewasapenpalwith5people.Hestoppedbeingpenpalswith2ofthem.Theyeachsend2lettersaweekthatare5pages
long.Herespondsinkind.Hecanwriteapageevery6minutes.Howmanyhoursdoeshespendwritingaweek?
Yourfinalanswershouldbeasinglenumericalnumber,intheform answer ,attheendofyourresponse.
A:Let’sthinkstepbystep.

### Output:

First,let’scalculatehowmanylettersMikereceivesinaweekfromthe5penpals.Eachpenpalsends2lettersperweek,so5
penpalswouldsendhim5*2=10lettersinaweek.
Next,let’scalculatehowmanypagesMikeneedstowriteinresponsetoeachletter. Eachletteris5pageslong,andMike
respondsinkind,sohewouldwrite5pagesforeachletterhereceives.
Therefore,Mikeneedstowriteatotalof10*5=50pagesinaweek.
Now,let’scalculatehowmanyminutesittakesforMiketowriteonepage.Wearegiventhathecanwriteapagein6minutes.
SinceMikeneedstowrite50pages,itwilltakehim50*6=300minutestocompleteallthewriting.
Lastly,let’sconverttheminutestohours.Thereare60minutesinanhour,so300minutesisequalto300/60=5hours.
Therefore,Mikespends5hourswritinginaweek.
Answer: 5 .
CoT+RE2

### Input:

Q:Mikewasapenpalwith5people.Hestoppedbeingpenpalswith2ofthem.Theyeachsend2lettersaweekthatare5pages
long.Herespondsinkind.Hecanwriteapageevery6minutes.Howmanyhoursdoeshespendwritingaweek?
Readthequestionagain:Mikewasapenpalwith5people.Hestoppedbeingpenpalswith2ofthem.Theyeachsend2lettersa
weekthatare5pageslong.Herespondsinkind.Hecanwriteapageevery6minutes.Howmanyhoursdoeshespendwritinga
week?
Yourfinalanswershouldbeasinglenumericalnumber,intheform answer ,attheendofyourresponse.
A:Let’sthinkstepbystep.

### Output:

First,let’scalculatethetotalnumberoflettersthatMikereceivesinaweek.Sincehewaspenpalswith5people,andhestopped
beingpenpalswith2ofthem,heisstillreceivinglettersfrom5-2=3people.
Eachofthese3peoplesends2lettersaweek,sothetotalnumberoflettersthatMikereceivesinaweekis3*2=6letters.
Next,let’scalculatethetotalnumberofpagesthatMikeneedstowriteinresponse. Eachletteris5pageslong,sothetotal
numberofpagesthatMikeneedstowriteis6*5=30pages.
SinceMikecanwriteapageevery6minutes,thetotaltimehespendswritinginaweekis30*6=180minutes.
Toconvertthistohours,wedivideby60sincethereare60minutesinanhour.So,Mikespends180/60=3hourswritingina
week.
Therefore,Mikespends 3 hourswritingaweek.
Table17: GSMExample242(Complexity=6)

<!-- Page 24 -->

Q:Terriisknittingasweaterwithtwosleeves,acollar,andadecorativerosette.Thebodyofthesweatertakes900stitchesto
complete,thecollartakesatenthofthatnumberofstitches,andtherosettetakestwiceasmanyasthecollar.Thewholesweater
isan1800-stitchproject.Howmanystitchesdoeseachsleevetake?(Answer:315)

### CoT


### Input:

Q:Terriisknittingasweaterwithtwosleeves,acollar,andadecorativerosette.Thebodyofthesweatertakes900stitchesto
complete,thecollartakesatenthofthatnumberofstitches,andtherosettetakestwiceasmanyasthecollar.Thewholesweater
isan1800-stitchproject.Howmanystitchesdoeseachsleevetake?
Yourfinalanswershouldbeasinglenumericalnumber,intheform answer ,attheendofyourresponse.
A:Let’sthinkstepbystep.

### Output:

First,weknowthatthebodyofthesweatertakes900stitchestocomplete.
Next,weknowthatthecollartakesatenthofthenumberofstitchesasthebody. So,thecollartakes900stitches/10=90
stitches.
Finally,weknowthattherosettetakestwiceasmanystitchesasthecollar.So,therosettetakes90stitches*2=180stitches.
Tofindouthowmanystitcheseachsleevetakes,weneedtosubtractthestitchesofthebody,collar,androsettefromthetotal
numberofstitchesinthesweater.
So,eachsleevetakes1800stitches-900stitches(body)-90stitches(collar)-180stitches(rosette)=630stitches.
Therefore,eachsleevetakes 630 stitches.
CoT+RE2

### Input:

Q:Terriisknittingasweaterwithtwosleeves,acollar,andadecorativerosette.Thebodyofthesweatertakes900stitchesto
complete,thecollartakesatenthofthatnumberofstitches,andtherosettetakestwiceasmanyasthecollar.Thewholesweater
isan1800-stitchproject.Howmanystitchesdoeseachsleevetake?
Readthequestionagain:Terriisknittingasweaterwithtwosleeves,acollar,andadecorativerosette.Thebodyofthesweater
takes900stitchestocomplete,thecollartakesatenthofthatnumberofstitches,andtherosettetakestwiceasmanyasthecollar.
Thewholesweaterisan1800-stitchproject.Howmanystitchesdoeseachsleevetake?
Yourfinalanswershouldbeasinglenumericalnumber,intheform answer ,attheendofyourresponse.
A:Let’sthinkstepbystep.

### Output:

First,weknowthatthebodyofthesweatertakes900stitchestocomplete.
Next,wearetoldthatthecollartakesatenthofthenumberofstitchesinthebodyofthesweater.Sincethebodyhas900stitches,
thecollarwillhave900/10=90stitches.
Finally,wearetoldthattherosettetakestwiceasmanystitchesasthecollar.Sincethecollarhas90stitches,therosettewill
have90*2=180stitches.
Now,let’saddupallthestitchestofindthetotalnumberofstitchesinthesweater:900(body)+90(collar)+180(rosette)=
1170stitches.
Wearegiventhatthewholesweaterisan1800-stitchproject.So,theremainingstitchesmustbeforthesleeves.
1800(totalstitches)-1170(stitchesaccountedfor)=630stitchesforthesleeves.
Sincetherearetwosleeves,eachsleevewillhave630/2=315stitches.
Therefore,eachsleevetakes315stitches.
Table18: GSMExample273(Complexity=6)

<!-- Page 25 -->

Q:Solohastoread4pagesfromhisSciencetextbook,20pagesfromhisSocialStudiestextbook,7pagesfromhisHistory
textbookand8pagesfromhisGeographytextbook.Soloread15pagesonMonday.Ifhehas4moredaystocompleteallhis
reading,howmanypagesdoesheneedtoread,onaverage,inoneday?(Answer:6)

### CoT


### Input:

Q:Solohastoread4pagesfromhisSciencetextbook,20pagesfromhisSocialStudiestextbook,7pagesfromhisHistory
textbookand8pagesfromhisGeographytextbook.Soloread15pagesonMonday.Ifhehas4moredaystocompleteallhis
reading,howmanypagesdoesheneedtoread,onaverage,inoneday?
Yourfinalanswershouldbeasinglenumericalnumber,intheform answer ,attheendofyourresponse.
A:Let’sthinkstepbystep.

### Output:

First,let’scalculatehowmanypagesSolohaslefttoread.Heneedstoread4pagesfromhisSciencetextbook,20pagesfrom
hisSocialStudiestextbook,7pagesfromhisHistorytextbook,and8pagesfromhisGeographytextbook.
So,thetotalnumberofpagesheneedstoreadis4+20+7+8=39pages.
SinceSolohas4moredaystocompleteallhisreading,wecandividethetotalnumberofpagesbythenumberofdays.
Therefore,Soloneedstoreadanaverageof39pages/4days=9.75pagesperday.
Therefore,Soloneedstoreadanaverageof 9.75 pagesperday.
CoT+RE2

### Input:

Q:Solohastoread4pagesfromhisSciencetextbook,20pagesfromhisSocialStudiestextbook,7pagesfromhisHistory
textbookand8pagesfromhisGeographytextbook.Soloread15pagesonMonday.Ifhehas4moredaystocompleteallhis
reading,howmanypagesdoesheneedtoread,onaverage,inoneday?
Readthequestionagain:Solohastoread4pagesfromhisSciencetextbook,20pagesfromhisSocialStudiestextbook,7pages
fromhisHistorytextbookand8pagesfromhisGeographytextbook.Soloread15pagesonMonday.Ifhehas4moredaysto
completeallhisreading,howmanypagesdoesheneedtoread,onaverage,inoneday?
Yourfinalanswershouldbeasinglenumericalnumber,intheform answer ,attheendofyourresponse.
A:Let’sthinkstepbystep.

### Output:

First,let’scalculatethetotalnumberofpagesSoloneedstoread.Heneedstoread4pagesfromhisSciencetextbook,20pages
fromhisSocialStudiestextbook,7pagesfromhisHistorytextbook,and8pagesfromhisGeographytextbook.So,thetotal
numberofpagesheneedstoreadis4+20+7+8=39pages.
Next,let’scalculatethenumberofpageshehaslefttoreadafterMonday.Heread15pagesonMonday,sohehas39-15=24
pageslefttoread.
Finally,let’scalculatetheaveragenumberofpagesheneedstoreadperday.Hehas4moredaystocompletehisreading,sohe
needstoread24/4=6pagesperday.
Therefore,Soloneedstoreadanaverageof 6 pagesperday.
Table19: GSMExample101(Complexity=6)

<!-- Page 26 -->

Q:Wouldanickelfitinsideakoalapouch?(Answer:yes)

### CoT


### Input:


### Q:Wouldanickelfitinsideakoalapouch?

Youranswershouldbeeither yes or no ,intheform answer .
A:Let’sthinkstepbystep.

### Output:

First,let’sconsiderthesizeofanickel.Anickelhasadiameterofapproximately21.21mmandathicknessofapproximately
1.95mm.
Next,let’sconsiderthesizeofakoalapouch.Akoalapouchisdesignedtoholdababykoala,alsoknownasajoey.Thesizeof
akoalapouchcanvary,butitisgenerallynotlargeenoughtofitobjectsthesizeofanickel.
Therefore,basedonthesizeofanickelandthesizeofakoalapouch,itisunlikelythatanickelwouldfitinsideakoalapouch.

### No

CoT+RE2

### Input:


### Q:Wouldanickelfitinsideakoalapouch?

Readthequestionagain:Wouldanickelfitinsideakoalapouch?
Youranswershouldbeeither yes or no ,intheform answer .
A:Let’sthinkstepbystep.

### Output:

First,let’sconsiderthesizeofanickel.Anickelhasadiameterofabout0.835inches(21.21mm)andathicknessofabout0.077
inches(1.95mm).
Next,let’sconsiderthesizeofakoalapouch.Akoalapouchisdesignedtoholdababykoala,alsoknownasajoey.Thepouch
isstretchyandexpandsasthejoeygrows.However,thesizeofthepouchmayvarydependingontheageandsizeofthejoey.
Basedonthesizeofanickelandthestretchinessofakoalapouch,itispossiblethatanickelcouldfitinsideakoalapouch.
However,itwoulddependonthesizeofthepouchandthepositionofthejoeyinside.
So,theansweris yes ,anickelcouldpotentiallyfitinsideakoalapouch.
Table20: StrategyQAExample262

### Input:

Acoinisheadsup.Hankdoesnotflipthecoin.Janinedoesnotflipthecoin.Frankieflipsthecoin.Isaflipsthecoin.Isthecoin
stillheadsup?Notethat"flip"heremeans"reverse".
Youranswershouldbeeither yes or no ,intheform answer .

## A:

davinci-003withVanilla
Output:
No.
ChatGPTwithVanilla
Output:
No.
Table21: CoinFlipExample16. Withoutexplicitinstruction,ChatGPTanddavinci-003directlygeneratethefinal
answer.

### Input:


### YesterdaywasApril30,2021.WhatisthedatetomorrowinMM/DD/YYYY?

Youranswershouldbeadate,intheformatof MM/DD/YYYY ,e.g. 05/01/2022 .

## A:

davinci-003withVanilla

### Output:

05/01/2021
ChatGPTwithVanilla

### Output:

11/13/2019.
Table22: DateUnderstandingExample1. Withoutexplicitinstruction,ChatGPTanddavinci-003directlygenerate
thefinalanswer.

<!-- Page 27 -->


### Input:

Nedhadtowash9shortsleeveshirtsand21longsleeveshirtsbeforeschool. Ifhehadonlywashed29ofthembythetime
schoolstarted,howmanydidhenotwash?
Yourfinalanswershouldbeasinglenumericalnumber,intheform answer ,attheendofyourresponse.

## A:

davinci-003withVanilla

### Output:

Hedidnotwash20shirts. 20
ChatGPTwithVanilla

### Output:

Nedhadtowashatotalof9+21=30shirts.Hewashed29shirts,sohedidnotwash30-29=«30-29=1»1shirt.Therefore,he
didnotwash 1 shirt.
Table23: MultiArithExample9. Withoutexplicitinstruction, ChatGPTstillcangeneratetheCoToutput, but
davinci-003doesnot.

### Input:

Atradersoldanarticleataprofitof20%forRs.360.Whatisthecostpriceofthearticle?AnswerChoices:A)270,B)300,C)

## 280,D)320,E)315

Youranswershouldbeintheform choice .Thereisonlyonecorrectchoice.

## A:

davinci-003withVanilla
Output:

## B

ChatGPTwithVanilla

### Output:

Let’sassumethecostpriceofthearticleisx. ThesellingpriceofthearticleisgivenasRs. 360,whichis120%ofthecost
price(100%+20%profit).So,wecanwritetheequationas:x+20%ofx=360Simplifyingtheequation,weget:1.2x=360
Dividingbothsidesby1.2,wefind:x=300Therefore,thecostpriceofthearticleisRs.300.Thecorrectansweris (B)300 .
Table24: AQUAExample4. Withoutexplicitinstruction,ChatGPTstillcangeneratetheCoToutput,butdavinci-
003doesnot.

## Tables

**Table (Page 1):**

| Read | the | question | again: | Roger has 5 tennis balls. He buys |  |
|---|---|---|---|---|---|
| 2 more cans of tennis balls. Each can has 3 |  |  |  |  | tennis balls. |
| How many tennis balls does he have now? |  |  |  |  |  |


**Table (Page 2):**

| Second |  |  |
|---|---|---|
|  | Pass |  |


**Table (Page 2):**

| Second Pass | Second |  |  |
|---|---|---|---|
|  |  | Pass |  |


**Table (Page 5):**

|  |  |  |  |  |  |
|---|---|---|---|---|---|
|  | 80. | 80. 59 | 89 80. | 29 80. | 2 |
|  |  |  |  |  |  |
|  | 79. | 45 79. | 15 |  |  |
| 8. | 77 |  | 78. | 77 |  |
| 7. | 79 |  |  | 77. | 5 |


**Table (Page 5):**

| 8. | 61. 98 | 64 60. | 12 58. | 83 57. | 4 |
|---|---|---|---|---|---|
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
| 9. | 24. 48 | 79 18 | .8 18. | 35 |  |
|  |  |  |  | 17. | 0 |


**Table (Page 7):**

| 370 total cases Correct w. CoT 326 Correct w. CoT+Re2 298 174 88 63 | total cases Correct w. CoT Correct w. CoT+Re2 |  |  |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |


**Table (Page 7):**

|  |  | CoT CoT+Re2 | CoT CoT+Re2 |  |  |
|---|---|---|---|---|---|
|  |  |  |  |  |  |


**Table (Page 7):**

|  |  |
|---|---|
|  |  |


**Table (Page 7):**

|  |  |
|---|---|
|  |  |


**Table (Page 7):**

|  |  |
|---|---|
|  |  |


**Table (Page 7):**

|  |  |
|---|---|
|  |  |


**Table (Page 8):**

|  | .45% |
|---|---|
|  |  |


**Table (Page 14):**

| 4. | 66 4. | 4. 54 | 61 4. | 63 |
|---|---|---|---|---|
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
| 1. | 9 1. | 84 1. | 83 1 | .8 |


**Table (Page 20):**

| Rea | dthe |  | ques |  | tion |  | again: |  | Eve | ry | day,W | endi | feed | seacho |  | fher | chick |  | ens | three |  | cup | sof | mixed |  |  | chicken |  |  | feed, | cont |  | ain | ing | seeds, |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mea | lworms |  |  | and |  | ve | get | able | sto | hel | pkeep | them | healthy. |  | She | give | sthe | chick |  | ens | theirf |  | eed | in | three |  | sepa |  | rate | meals. |  | In | th | emorn |  | ing, |
| she | gives |  | her | flock |  |  | of | chic | kens | 15 | cupso | ffeed | .In | the | after | noon, | she | gives |  | her | chicke |  | ns | ano | ther |  | 25 | cupso |  | ffeed. |  | How |  | many | cups |  |
| off | eed | does |  | she |  | need |  | tog | ive | her | chicke | nsin | thefi | nal | mea | loft | hed | ay | ift | hes | iz | eof | Wendi’s |  |  | flock |  | is | 20 | chick | ens? |  |  |  |  |  |


**Table (Page 21):**

| Read | the | ques |  |  | tion | again: |  | Tim | gets | a | pro | mo | tion | thato | ffers |  | him | a | 5% |  | raise | on | his | $20000 | a | month | salary. | It | also | gives | him | a | bonus |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| worth | half |  | a | month’s |  |  | salary. |  | How | much |  | money |  | will | he | make |  | in | a | year? |  |  |  |  |  |  |  |  |  |  |  |  |  |


**Table (Page 22):**

| Readt | hequest |  | ion | again: |  | Colby |  | loves |  | go | ingt | othe | movies |  | and | every | month |  | his | par | entsg |  | iveh | im | $150t |  | ospend |  | at | the | movies. |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tickets | for | Fri | days | and | Sa | turd | ay | scost |  | $10.Ti |  | ckets | for | any | othe | rday | cost | $7. | Pop | corn |  | cos | ts$8 | and | boxes |  | of | candy |  | cost | $2 | .It | is |
| thelas | tday | of | the | month |  | and | it’ | sa | Fr | iday.H |  | ewants |  | tom | akes | ureh | egetsa |  | pop | corn |  | and | box | of | candy |  | that | night. |  | How |  | many |  |
| movies | can | he | seei | fhe | al | readys |  | aw | 5 | movies |  | ona | Fri | day | orSa | turda | y,8 | movies |  | on | other |  | days, | had | 2 | tub | sof | pop | corn, |  | and | four |  |
| boxes | ofcandy |  | tha | tmonth? |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |


**Table (Page 23):**

| Read | the | ques | tion |  | again: |  | Mike |  | was |  | a | pen | pal |  | with | 5 | peop | le. | He | stopped |  | bei | ng | pen | pals | with | 2of | them. |  | They |  | each |  | send | 2let | ters | a |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| week | that | are | 5 | pages |  | long. |  | He | re | sponds |  |  | in | kind. |  | He | can | writea |  | page | ev | ery | 6 | min | utes. | How | many |  | hours |  | does |  | he | spend | writ | ing | a |
| week |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |


**Table (Page 24):**

| Read | the | ques | tiona | gain: | Terri | is | knit | ting | a | sweater |  |  | with |  | two | sleeves, |  | acoll | ar,a | nd | a | dec | o | ra | tive | rosette. |  | The | body |  | of | the |  | sweater |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| takes | 900 | stitchesto |  | com | plete, | the | co | llar | takes |  | a | tenth |  | of | that | num | bero | fstitches |  | ,and |  | the | rosette |  |  | takes | twice |  | as | many |  | as | the |  | col | lar. |
| The | whol | esweater |  | isan | 1800- | stitch |  | project. |  |  | How |  | many |  | stitches |  | does | each | sleeve |  | take? |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | answer |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |


**Table (Page 25):**

| Read | the | que | stio | nagain: |  | Solo | has | to | read4 |  | pages | fromhi | sSci | ence |  | tex | tbook, |  | 20 | pages |  | from | his |  | So | cial | Stud |  | ies |  | text |  | book, | 7 | pages |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| from | his | His | tory | text | boo | kand | 8 | pages |  | fro | mhis | Geograp | hytext |  | book. |  | Solo |  | read | 15 | pages |  | on | Mon |  | day. | If | he |  | has |  | 4 | more | days |  | to |
| comp | lete | all | hisr | ead | ing, | how | many |  | pages |  | doesh | eneedt | oread, |  | on | av | er | age, | in | one | day? |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |


**Table (Page 26):**

| Read | the | ques | tion | again: | Would | a | nickel |  | fit | in | side | a | koala | pouch? |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  | no |  |  |  |  |  | answer |
