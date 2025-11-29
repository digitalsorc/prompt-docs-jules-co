---
title: "UPRISE Universal Prompt Retrieval"
original_file: "./17_UPRISE_Universal_Prompt_Retrieval.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["prompt-engineering", "llm", "rag", "chain-of-thought", "fine-tuning"]
keywords: ["prompt", "task", "input", "shot", "uprise", "page", "cluster", "language", "retriever", "acc"]
summary: "<!-- Page 1 -->

UPRISE: Universal Prompt Retrieval for Improving Zero-Shot Evaluation
DaixuanCheng ShaohanHuang JunyuBi YuefengZhan JianfengLiu
∗
YujingWang HaoSun FuruWei DenvyDeng QiZhang

### MicrosoftCorporation

daixuancheng6@gmail.com bijunyu21@mails.ucas.ac.cn
{shaohanh,yuefzh,jianfengliu,yujing.wang,hasun,fuwei,dedeng,qizhang}@microsoft.com

### Abstract Train Inference


### Large Language Models (LLMs) are popu- GPT3-175B

larfortheirimpressiveabilities,buttheneed 🧊 GPT-Neo-2.7B OPT-6"
related_documents: []
---

# UPRISE Universal Prompt Retrieval

<!-- Page 1 -->

UPRISE: Universal Prompt Retrieval for Improving Zero-Shot Evaluation
DaixuanCheng ShaohanHuang JunyuBi YuefengZhan JianfengLiu
∗
YujingWang HaoSun FuruWei DenvyDeng QiZhang

### MicrosoftCorporation

daixuancheng6@gmail.com bijunyu21@mails.ucas.ac.cn
{shaohanh,yuefzh,jianfengliu,yujing.wang,hasun,fuwei,dedeng,qizhang}@microsoft.com

### Abstract Train Inference


### Large Language Models (LLMs) are popu- GPT3-175B

larfortheirimpressiveabilities,buttheneed 🧊 GPT-Neo-2.7B OPT-66B Cross-

### Model

formodel-specificfine-tuningortask-specific

### Tune

promptengineeringcanhindertheirgeneraliza- BLOOM-7.1B
🔥Prompt Retriever
tion. Wepropose UPRISE (UniversalPrompt

### Paraphrase


### RetrievalforImprovingzero-ShotEvaluation),

Read. Compre. Crosswhich tunes a lightweight and versatile re- Close. QA Sentiment Task
triever that automatically retrieves prompts NLI Fact-Check.
for a given zero-shot task input. Specifically, we demonstrate universality in a cross- Figure 1: UPRISE tunes a prompt retriever on multitask and cross-model scenario: the retriever pletaskswithasmallLLM,butconductsinferenceon
is tuned on diverse tasks, but tested on un- unseentasktypeswithadifferentlargerLLM.
seen task types; we use a small frozen LLM,

### GPT-Neo-2.7B, for tuning the retriever,

but test the retriever on different LLMs of providesanalternativeapproachtoimprovezeromuch larger scales, such as BLOOM-7.1B, shot task generalization (Wei et al., 2022a; Sanh

### OPT-66BandGPT3-175B.Additionally,we

et al., 2022), which partially justifies the tuning
showthatUPRISEmitigatesthehallucination
cost. Yet,theconstantevolutionofLLMscreates
problem in our experiments with ChatGPT,
theneedfortuningnewmodels,makingthecumusuggesting its potential to improve even the
lativefine-tuningcostabigconcern.
strongestLLMs. Ourmodelandcodeareavailableathttps://github.com/microsoft/LMOps. Promptengineeringconstructspromptstoguide
frozenLLMs. Promptdesignaddsanengineered
1 Introduction naturallanguageprompttoteachtheLLMtolearn
in context (Brown et al., 2020) or to induce the

### Large Language Models (LLMs) such as

LLM to reason (Wei et al., 2022b). Prompt tun-
GPT-3 (Brown et al., 2020), OPT (Zhang et al.,
ingaddsasoftpromptrepresentedbycontinuous
2022), and BLOOM (Scao et al., 2022) have
parameters,andoptimizesitthroughgradientpropshownimpressivecapabilitiesacrossawiderange
agation(Liuetal.,2021;LiandLiang,2021;Lester
of tasks. Recent research proposes two main
etal.,2021). Whilethesemethodscanimproveperapproachestofurtherimprovetheirperformance:
formanceforspecifictasks,itisuncertainwhether
fine-tuning LLMs to follow prompts (Hu et al.,
thepromptsdesignedforonetaskcangeneralize
2022;Houlsbyetal.,2019;Zakenetal.,2022;Wei
tounseentasktypes,aspromptdesignersareblind
et al., 2022a; Sanh et al., 2022) and developing
instrictzero-shotsettings(vandeKaretal.,2022).
prompt engineering techniques to guide the
In this paper, we propose UPRISE (Universal

### LLMs(Brownetal.,2020;Weietal.,2022b;Liu

Prompt Retrieval for Improving Zero-Shot
etal.,2021;Lesteretal.,2021).

### Evaluation), which tunes a lightweight and ver-

Fine-tuningLLMsadjuststheirweightstofitspesatileretrieverthatautomaticallyretrievesprompts
cificprompts. However,thiscanbeconstrainedby
from a pre-constructed pool, given a zero-shot
computationallimitationsortheunavailabilityof
task input. As illustrated in Figure 1, the remodelweights(Huetal.,2022). Multi-tasktuning
triever is trained to retrieve prompts for mul-
∗Correspondingauthor tiple tasks, enabling it to generalize to un-
12318
Proceedingsofthe2023ConferenceonEmpiricalMethodsinNaturalLanguageProcessing,pages12318–12337
December6-10,2023©2023AssociationforComputationalLinguistics

<!-- Page 2 -->

seen task types during inference. In addition, Prompt Design
we demonstrate that the cross-task capabilities 🧊 Language Model Prompt Retrieval
can generalize well from a small LLM to different LLMs of much larger scales: we use 🧊 Summarizethe… 🧊 Language Model
GPT-Neo-2.7B (Black et al., 2021) to guide Engineered Natural Task Tune

### Language Prompt Input

the tuning of the retriever and evaluate the re- 🧊Answerthis…
triever’s performance on BLOOM-7.1B (Scao Prompt Tuning Retrieved Natural Task

### Language Prompt Input

et al., 2022), OPT-66B (Zhang et al., 2022), 🧊 Language Model
and GPT3-175B (Brown et al., 2020). The backward 🔥Prompt Retriever
cross-modelandcross-taskgeneralizationof UP- 🔥 0.10,0.05,… Tunable Prompt

### Retriever

RISE makes it a promising and practical solution Tunable Soft Task

### Prompt Input

forreal-worldapplications.
Furthermore,ourapproachdemonstratesthepo- Figure 2: Typical prompt engineering methods and
tentialforenhancingeventhemostpowerfulLLMs, prompt retrieval. Prompt retrieval prepends a natural
asshowninourexperimentswithChatGPT.De- language prompt to the task input and uses a frozen
LLM to evaluate the prompt’s performance. The obspite its impressive abilities, ChatGPT has been
tainedevaluationisthenusedtotunetheretrieverina
foundtostrugglewithserioushallucinationprobreversemanner.
lems,leadingtoresponsesthatarefactuallyinaccurate (Bang et al., 2023). However, UPRISE is
able to address this issue on fact-checking tasks +
Our objective is to optimize performance of y

## P

bypromptingthemodeltodrawcorrectinferences
tomatchthetargety byupdatingtheretriever .
fromitsbuilt-inknowledge. R
Figure2comparespromptretrievalwithtypical

### Insummary,ourcontributionsinclude:

promptengineeringmethods: promptdesignadds
• WeintroduceUPRISE,alightweightandversatile
an engineered natural language prompt (Brown
approach to improve zero-shot performance of
et al., 2020; Wei et al., 2022b) and prompt tun-
LLMsinthecross-taskandcross-modelscenario.
ing tunes a soft prompt (Liu et al., 2021; Lester
• UPRISE is tuned with GPT-Neo-2.7B, but
et al., 2021). In contrast, prompt retrieval tunes
canalsobenefitdifferentLLMsofmuchlarger
a retriever to retrieve natural language prompts,
scales, such as BLOOM-7.1B, OPT-66B, and
which is both interpretable and flexible. It uses

## Gpt3-175B.

thelanguagemodelitselftolabeleachpromptin
• OurexplorationonChatGPTdemonstratesthe
thepoolaspositive/negative, andthentunesarepotentialofUPRISEinimprovingperformances
trieverfromthissignal(Rubinetal.,2022). Such
ofeventhestrongestLLMs.
fine-tunedpromptretrievalhasdemonstratedeffec-
2 ProblemDefinition tivenessinthetask-specificscenario(Rubinetal.,
2022;Yeetal.,2023): apromptretrieveristuned

### Weaimtoimprovezero-shotperformanceofLLMs

on one or multiple specific tasks using the trainbytrainingapromptretrievertoretrieveprompts1
ing sets as the prompt pool. The retriever is then
foranygiventaskinput. Specifically,UPRISEdeevaluatedonthecorrespondingtestingsets.
composes the prompting process into two steps:

### Ourworkistoachieveuniversalityoftheprompt

retrieve then predict. Given an input x, we first
retriever,whichmeansthefine-tunedretrievercan
retrieve a set of positive prompts + from a pre-
P bedirectlyusedtoretrievepromptsforunseentasks
constructedpool :

### P andvariousinferenceLLMs,withouttheneedfor

+ = (x, ). (1) furthertuning. Wedefinetheuniversalityfromtwo

## P R P

perspectives: cross-taskretrievalandcross-model
Thenweconcatenate + withxtoformaninput
P retrieval.
sequenceforafrozenLLM,whichgeneratesapredictedoutput: Cross-taskretrieval. Consideringthediversity
of tasks in real-world applications, we propose
y P + = LM y P + + x . (2) cross-task retrieval to retrieve for task types on

## |P ⊕

(cid:16) (cid:17) which the prompt retriever has not been trained.
1"Prompt"sometimesreferstoanaturallanguagetemplate

### Wesimulatethissettingbyevaluatingtheprompt

filledbyaninputexample,buthereitdenotesthesequence
prependedtothetaskinput. retriever on unseen task types: various tasks are
12319

<!-- Page 3 -->

groupedintodifferentclustersbasedontheirtask inputandthedemonstrationsareofdifferenttask
types,andweholdouteachtaskclusterforevalu- types.
ationwhiletrainingtheretrieveronallremaining
3.2 PromptScoring
clusters(Weietal.,2022a).
Cross-modelretrieval. Duetothehighcostof For each training example (x ,y ) in the training
i i
tuningapromptretrieverwithalarge-scaleLLM, clusters, we collect a set of positive and negaweproposeevaluatingthecapabilitytogeneralize tivepromptsfromthepromptpool = p N ,

## P {

j }j=P1
fromasmallLLMtoalargeLLM.Specifically,we wherethepositivepromptindicatesthatthefrozen
usearelativelysmallLLMfortuningtheretriever, LLMachievesgoodtaskscoresconditionedonthe
whileusingamuchlargerLLMforinference. Fur- prompt-input concatenation. We use these posithermore,wesuggestexploringthetransferability tiveandnegativelabelstosupervisethecontrastive
betweendifferentLLMsources,asthereareLLMs learningoftheretriever.
developedbydifferentcompaniesorinstitutions. Wecategorizealltasksintotwoquestiontypes:
textcompletionandmultiplechoice(Brownetal.,
3 Method 2020), and use different methods to score the
promptsforeachtrainingexample.

### AsshowninFigure3,UPRISEusesafrozenLLM


### Textcompletionisthequestiontodofree-form

to supervise the fine-tuning of a prompt retriever
completion. Wecalculatescoreofthepromptusing
ondiversetasks,andthenusesthistrainedretriever
thefollowingequation:
toretrievepromptsforunseentasktypeswithdifferentLLMsduringinference. Inthissection,we
score(p ,x ) = metric y ,y
pj
, (3)
j i i i
elaborateonourdataconstruction,promptscoring,
retrievertuningandinferencepipeline.
where y
pj
= LM y
pj
p x
(cid:0)
is the m
(cid:1)
odel prei i | j ⊕ i
dictionbased ontheinputconcatenation p x ,
j i
3.1 DataConstruction (cid:0) (cid:1) ⊕
and is a text delimiter “ n”. metric( ) is the
⊕ \ ·
Task Data. We use instruction templates from function used to calculate the task metric score
FLAN(Weietal.,2022a)toconverttaskdatasets (e.g.,F1orROUGE).
into natural language instructions2. Each task Multiple choice is the question to choose one
dataset corresponds to approximately seven tem- correctcompletionfromseveraloptions. Suppose
plates. For each data example (x i ,y i ), we ran- thereareM optionsinamultiplechoicequestion
domlyselectoneoftheseventemplatestoconvert x ,y , o M ,where o M istheoption
x intoataskinputandy intoalabelcompletion. i i { m }m=1 { m }m=1

## T

i
he option suffices and n
i
ew line characters “ n”
(cid:16)setando
yi
istheg(cid:17)oldoption. Wefeedtheconcate-
\ nationp j x i totheLLMandcalculateper-token
areautomaticallyremovedfromthetaskinput,to ⊕
likelihood of each option: LH(o ). The option
m
make the text format more similar to that of the
with the highest likelihood is considered as the
pre-trainingcorpus, improvingpromptingperformodelpredictiony
pj
(Brownetal.,2020).
mance(vandeKaretal.,2022).
Accuracy of the
i
prediction acc y ,y
pj
is a
i i

### Prompt pool. For each testing cluster, the

commonmetricformultiple-choicequestions,but
promptpoolusedforretrievalismadeupoftrain- (cid:0) (cid:1)
itonlyproduces0or1foreachexample,makingit
ingdemonstrationsoftheremainingtaskclusters
hardtocompareprompteffectiveness. Toaddress
(i.e.,theclustersfortrainingtheretriever). Thisis
this,wemultiplytheaccuracybytheper-tokenlikeinspiredbyin-contextlearning(Brownetal.,2020),
lihoodofthegoldoption,whichisnormalizedby
which presents a few training demonstrations bethesumoftheper-tokenlikelihoodofalloptions,
forethetaskinputtoimprovemodelperformance.
to achieve a fine-grained comparison. The final
Eachdemonstrationisaconcatenationofthetask
scoreisformulatedas:
input and the label completion. Our motivation
is that the testing input may benefit from similar
score(p ,x ) = acc y ,y
pj LH(o yi )
.
question types, topics, or reasoning chains in the j i i i · M LH(o )
m=1 m
retrieved demonstrations, despite that the testing (cid:0) (cid:1) (4)

## P


### Promptfiltering. Intuitively,tocollecttheposi-

2Weexcludetemplatesthat“turnthetaskaround”,such
tiveandnegativepromptsforeachtrainingexamasaskingasentimentclassificationtasktogenerateamovie
review. ple,weneedtoscoreeverypromptintheprompt
12320

<!-- Page 4 -->

Tune on many tasks Inference on unseen task types
with a different language model
S T c a o s r k e 0. 0 7 . 8 1 0 3 .09 Tune Con L tr o a s s s tive 0. 0 4 . 4 1 0 9 .37 O T u a tp sk ut Sentim P e o n s t itive

### Prompt

Retriever
🧊
🔥Prompt 🔥Input

### GPT-Neo-2.7B Encoder Encoder BLOOM-7.1B OPT-66B GPT3-175B


### Read. Compre. NLI Read. Compre. NLI Read. Compre. Sentiment

Read the passage… Does love entail… Read the passage… Does love entail… Read the passage… Howdoyoufeel…
Prompt Task Prompt

### Read. Compre. NLI

Pool Read the passage… Does love entail… Input Retriever

### Close. QA

Pleaseanswer…

### Task


### NLI Sentiment


### Premise:today… Input Howdoyoufeel…

Figure3: Trainingandinferencepipeline. Inthetrainingstage,afrozenLLMisusedtosupervisethetuningofa
promptretriever,whereboththeLLMandtheretrievertaketheprompt-inputpairsasinput,andweusethetask
scoresgivenbytheLLMtosupervisethecontrastivelearningoftheretriever. Intheinferencestage,foreachtask
input,thetunedpromptretrieverretrievepositiveprompt(s)toguidetheinferencemodeltopredictataskoutput.
Overall,wefollowacross-taskandcross-modelparadigmwherethetasktypesandLLMsfortrainingcouldbe
differentfromthoseforinference.
pool and identify the prompt that yields the best addition,welabelBdemonstrationscorresponding
scoreasthepositiveprompt. Conversely,prompts tothelowestB scoresinthesampledpromptsas
that lead to the worst scores are labeled as nega- hard negatives, which are of the same task with
tiveprompts. However,scoringallthepromptscan (x ,y )butarelesseffective.
i i
becomputationallyexpensive(Rubinetal.,2022),
evenwitharelativelysmallLLM. 3.3 RetrieverTuning
To address this, we only score a subset of L Afterlabelingpromptsforeachtrainingexample,
randomly sampled demonstrations; each demon- wesplitthecollecteddataintotwosets: 90%for
stration is constrained to have the same task as training and 10% for validation. The prompt rethe training example (x ,y ). This is inspired by triever is a bi-encoder model (Karpukhin et al.,
i i
in-context learning where the testing sample and 2020)wheretheinputencoderE X ( )takesthetask
·
trainingdemonstrationssharethesametask,result- input x i as input, and the prompt encoder E P ( )
·
inginimprovedtaskscores. Byscoringasubsetof takespromptp j asinput.
demonstrations, we significantly reduce the com- Totrainthepromptretriever,InfoNCE(vanden
putationalcostwhileincreasingthelikelihoodof Oord et al., 2018) loss is used to maximize the
identifying positive prompts within the sampled similarityscorebetweentheencodedpromptand
subset. inputforpositiveprompt-inputpairs,andminimize
it for (hard) negative prompt-input pairs. For a

### Furthermore,inthecaseofadifficultquestion,

singletrainingexample(x ,y ),thelossfunction
all L prompt-input concatenation may result in a i i
foritspositiveandnegativepromptsis:
scoreof0. Toaddressthis,werepeatthesampling
processtoscoreanothersubsetofLpromptswith
thesametaskas(x ,y ),untilwefindatleastone L(x i ,p+ i ,p −i,1 ,...p −i,2B ) (5)
i i
promptwithascoregreaterthan0. esim(xi,p+ i )
= log ,
Forallthescoredpromptsforatrainingexample, − esim(xi,p+ i )+ 2 j= B 1 esim(xi,p−i,j )
welabelthepromptwiththehighestscoreaspos-

## P

itive. Fornegativesamples,werandomlysample where p+ i is the positive prompt, p −i,j is one of
B training demonstrations from the prompt pool, the (hard) negative prompts, and sim(x ,p) =
i
eachwithadifferenttaskfromthatof(x ,y ). In E (x ) E (p)calculatesthesimilarityscorebei i X i ⊤ P
12321

<!-- Page 5 -->

tween input x and prompt p using inner prod- negatives to B = 20. For difficult questions, we
i
ucts(Rubinetal.,2022). repeatthere-samplingprocessuptosevenrounds,
aswefoundthatthisissufficienttoidentifyaposi-
3.4 Inference tivepromptfor90%ofthetrainingexamples. Ifno
After fine-tuning the prompt encoder, we use it sampledpromptyieldsascoregreaterthan0,we
to encode the entire prompt pool with E ( ). At filteroutthecorrespondingtrainingexample.

## P

·
inference time, for a testing task input x , we Tuning. We initialize the two independent entest
computeitsencodingE

## X

(x
test
)andthenusemaxi- coders of the retriever with BERT

## Base

(Devlin
mum inner-product search over the prompt pool etal.,2019). Eachretrieverisfine-tunedforthree
to retrieve K most similar prompts, sorted by epochs, and the best checkpoint is chosen based
their inner product in descending order, denoted onretrievalaccuracyusingthevalidationset. For
as + = (p ,...,p ). We then concatenate the detailed tuning hyperparameters, Please refer to

## 1 K


## P

prompts with the task input, resulting in the con- AppendixB.
catenationp K ... p 1 x test (Rubinetal.,2022). Inference. Duringinference,wesetthenumber
⊕ ⊕ ⊕
To evaluate the inference results, we use the K of concatenated prompts to a relatively small
samemethoddescribedinSection3.2togenerate value of 3, to balance between prompting perforpredictions,andthenuseeachtask’scorresponding manceandinferenceefficiency. Foreachdataset,
evaluationmetrictocomputethescores. wereportmetricscoresonthetestsetwhenavailable,fallingbacktothevalidationsetotherwise.
4 ExperimentSettings
5 MainResults

### Task clustering. We group the tasks used in our

methodintoclusters,includingReadingCompre- We evaluate our prompt retriever on natural lanhension,Closed-bookQA,ParaphraseDetection, guageunderstandingtaskswheregenerativeLLMs
NaturalLanguageInference,SentimentAnalysis, areknowntoneedimprovement(Liuetal.,2021).
CommonsenseReasoning,CoreferenceResolution, Table 1 compares the performance of UPRISE to
StructuretoText,andSummarization. Thedatasets vanillazero-shotprompting.
usedineachclusterarelistedinAppendixA.
Datasampling. Topreventtheretrievertuning 5.1 Cross-TaskPromptRetrieval
from being dominated by large datasets, we ran- BasedontheresultsofGPT-Neo-2.7B,wecan
domlysampleupto10k dataexamplesfromeach assessourabilityofgeneralizingacrossdifferent
task’s training set, while also maintaining class tasktypes. UPRISE haspositiveimpactsonmost
balanceinclassificationtasks3. Thepromptpool of the testing clusters. Specifically, we achieve
consistsofthesampledtrainingdataonly. Onaver- absolutegainsof8.5%and14.6%inReadingComage,foreachtestingtaskcluster,thereareapproxi- prehensionandParaphraseDetectiontasks,respecmately180k trainingexamplessampledfromthe tively. We also find that UPRISE shows consistrainingclusters. tentperformanceimprovementsacrossalltasksin
LLMs. We use GPT-Neo-2.7B (Black Closed-bookQAandNaturalLanguageInference
et al., 2021) from EleutherAI to tune the clusters.
retriever, and evaluate the performance on However,UPRISEhasnegativeimpactsonComlarger LLMs from various sources during in- monsenseReasoningandCoreferenceResolution
ference, including BLOOM-7.1B (Scao et al., tasks. WeconductanalysesinAppendixDtoun-
2022) from BigScience, OPT-66B (Zhang derstand the reasons, revealing that Coreference
et al., 2022) from Meta, and Davinci and Resolution hardly benefits from demonstrations
text-davinci-001 from OpenAI, both be- andCommonsenseReasoningisharmedbydifferlonging to the GPT3-175B (Brown et al., 2020) entdemonstrationformats.
series. Greedysearchisusedtoobtainpredictions
fromalltheLLMs. 5.2 Cross-ModelPromptRetrieval
Promptscoring. Wesetthesizeoftherandomly Inadditiontoevaluatingcross-taskgeneralization,
sampledsubsettoL = 50andthenumberof(hard)
we can explore the cross-model ability by examining the results of BLOOM, OPT, Davinci and
3Forinstance,inafour-classificationtask,wesamplea
maximumof2.5kdataexamplesfromeachclass. text-davinci-001. UPRISEcontinuestoim-
12322

<!-- Page 6 -->

Task Metric GPT-Neo-2.7B BLOOM-7.1B OPT-66B Davinci Davinci-001
0-SHOT UPRISE 0-SHOT UPRISE 0-SHOT UPRISE 0-SHOT UPRISE 0-SHOT UPRISE

### ReadingComprehension

F1 4.4 26.4 4.5 5.5 6.1 7.5 6.5 6.0 41.6 57.7

### SQuADv1


### Em 0.4 14.3 0.0 0.0 0.0 0.6 0.0 0.0 16.4 36.8


### BoolQ Acc 54.5 59.4 54.0 60.2 60.7 63.5 62.0 65.7 64.2 65.7

MultiRC F1 57.1 58.1 58.8 59.8 59.6 60.4 59.8 60.0 54.3 58.9
OBQA Acc 41.8 42.2 44.0 41.8 46.4 48.8 49.2 52.4 52.8 48.8
Average 31.6 40.1 32.3 33.5 34.6 36.2 35.5 36.8 45.9 53.6

### Closed-bookQA

ARC-e Acc 45.7 55.6 53.7 60.9 56.2 66.0 64.1 71.8 67.0 74.4
ARC-c Acc 29.3 30.0 33.2 34.2 36.7 40.2 40.8 45.2 46.2 50.4
F1 1.3 5.6 0.9 1.4 2.5 2.1 0.0 2.2 18.3 18.2

## Nq


### Em 0.5 2.2 0.0 0.1 0.3 0.4 0.0 0.0 4.8 8.7

Average 19.2 23.3 22.0 24.2 23.9 27.2 26.2 29.8 34.1 37.9

### ParaphraseDetection

Acc 46.6 67.9 51.0 70.6 51.0 68.9 54.4 62.3 40.0 61.3

## Mrpc


### F1 46.0 80.4 58.0 82.1 57.8 81.5 68.9 81.4 39.2 72.9

Acc 48.4 54.3 49.5 53.1 50.5 49.7 55.2 52.4 60.9 62.6

## Qqp


### F1 42.2 59.8 46.7 59.6 43.7 58.5 33.7 57.9 43.0 45.9

PAWS Acc 51.7 45.7 50.8 45.9 50.5 44.4 52.4 44.5 53.2 52.3
Average 47.0 61.6 51.2 62.3 50.7 60.6 52.9 59.7 47.3 59.0

### NaturalLanguageInference

MNLI-m Acc 35.3 41.3 35.4 36.0 37.0 40.4 34.2 38.2 44.7 41.1
MNLI-mm Acc 36.4 43.1 34.9 35.8 37.1 41.2 34.2 38.6 46.5 42.1
QNLI Acc 50.9 53.8 49.9 51.3 54.2 53.7 51.7 51.1 60.0 58.4
SNLI Acc 35.2 42.3 35.2 34.4 34.5 40.2 33.5 37.9 47.5 42.0
RTE Acc 33.6 34.7 50.5 49.8 52.3 46.9 51.3 45.5 52.3 50.9
Average 38.3 43.0 41.2 41.5 43.0 44.5 41.0 42.3 50.2 46.9

### SentimentAnalysis

SST-2 Acc 52.4 56.2 63.2 69.1 57.9 65.3 52.3 64.3 90.5 90.5

### Yelp Acc 71.7 67.8 56.1 58.0 67.6 63.5 59.8 65.3 80.3 80.2

Sent140 Acc 64.1 61.3 74.5 72.1 59.1 61.6 64.3 72.1 87.2 89.1
Average 62.7 61.8 64.6 66.4 61.5 63.5 58.8 67.3 86.0 86.6

### CommonsenseReasoning

PiQA Acc 70.2 70.4 71.5 72.1 76.5 80.4 79.1 81.3 79.1 79.1

### COPA Acc 67.0 64.0 67.0 67.0 74.0 76.0 80.0 83.0 83.0 80.0

HellaSwag Acc 54.4 52.1 59.6 58.8 72.9 71.4 76.9 76.7 77.6 78.2
Average 63.9 62.2 66.0 66.0 74.5 75.9 78.7 80.3 79.9 79.1

### CoreferenceResolution

WSC273 Acc 73.6 76.6 78.0 81.0 83.9 86.1 60.6 50.0 78.8 75.5

### DPR Acc 59.6 51.0 64.4 55.8 66.3 50.0 82.1 83.9 64.4 58.7

Winogrande Acc 58.9 58.6 65.9 64.3 69.2 67.8 68.6 70.2 66.3 64.7

### Average 64.0 62.1 69.4 67.0 73.1 68.0 70.4 68.0 69.8 66.3

Table 1: Zero-shot performance across tasks and LLMs. The model Davinci-001 is the fine-tuned version
text-davinci-001 of Davinci. The method 0-SHOT is the vanilla zero-shot method with only the inputinstructionfedintotheLLM.
12323

<!-- Page 7 -->

60
55
50
45
40
35
GPT-Neo-2.7BBLOOM-7.1B OPT-66B Davinci Davinci-001

## 0-Shot Uprise

.gvA
Method TruthfulQA FEVER2.0 Covid-19

## 0-Shot 86.3 51.0 47.0


## Uprise 86.3 56.0 83.0

Table2: ComparativeresultsofChatGPTonhallucinationdetectiontasks.

## 0-Shot

There existed no sibling duo called Sonny & Cher. Is this true?
False. Sonny & Cher were a popular American singing duo in
Figure4: cross-modelresultsofthecross-taskretriever.
the 1960s and 1970s, consisting of Sonny Bono and his wife
Cher. They had several hit songs, including "I Got You Babe"
and "The Beat Goes On," and also had their own television
prove performance on Reading Comprehension, show, The Sonny & Cher Comedy Hour.

### Closed-bookQA,andParaphraseDetectiontasks

acrossallLLMs. WhiletheperformanceonSentiment Analysis is negative with the small 2.7B UPRISE

### GPT-Neo,weobservepositiveimpactswhenus-

Spot gold was fetching $365.25/366.25 an ounce at 0520
inglargerLLMs. Weachieveconsistentgainson

### GMT, having galloped as high as $368.90--a level not seen

Natural Language Inference tasks with the mod- since February 10. Spot gold was quoted at $367.90/368.60
els that have not been fine-tuned (BLOOM, OPT, an ounce at 1000 GMT, having marched up to $369.50--a
levelnotseensinceFebruary10.Ifthefirstsentenceistrue,
and Davinci), but experience a drop in perfor- isthesecondonealsotrue?No
mance on text-davinci-001, which could ThereexistednosiblingduocalledSonny&Cher.Isthistrue?
potentiallybeduetothemodelbeingspecifically
fine-tunedonsuchtaskstoimproveperformance.
Generally,wepresenttheaverageperformance

### True

of Reading Comprehension, Closed-book QA,
ParaphraseDetection,NaturalLanguageInference, Figure5: Caseofthechatsofvanillazero-shotpromptand Sentiment Analysis in Figure 4. The results ing and UPRISE on the FEVER2.0 dataset, the label
indicate consistent performance gains across all completionis“True”.
LLMs.
tion, which is of the Natural Language Inference
6 HallucinationMitigationofChatGPT
tasktypethatmaymotivatethemodeltocorrectly
Despite the strong abilities of ChatGPT, recent inferfromitsparametricmemory. Thisfindingsugreportshaveshownthatitsuffersfromhallucina- geststhatthelimitedmemory4 ofChatGPTmay
tion: providingfactuallyincorrectresponses(Bang notbetheonlyfactorleadingtothehallucination
etal.,2023). Toassesstheversatilityof UPRISE, challenge. Rather,ithighlightstheimportanceof
wealsoinvestigatewhetheritcanmitigatethehal- having effective inference mechanisms. Prompt
lucination problem. We evaluate on three tasks: engineering techniques such as UPRISE can help
TruthfulQA(Linetal.,2022)fordetectinghuman address this issue. Evaluation details and further
falsehood, FEVER2.0 (Thorne et al., 2018) and analysiscanbefoundinAppendixC.
Covid-19(Leeetal.,2021)forfact-checking.
7 AblationStudy

### Table2showsthatUPRISEoutperformsvanilla

zero-shot prompting on the fact-checking tasks.
7.1 UniversalPromptRetriever
Figure 5 presents an interesting case where 0-
Wereplacetheuniversalretrieverwiththreealter-
SHOT inducesacorrectgenerationofinformation
(“Sonny&Cher... consistingofSonnyBonoand
natives: 1) RANDOM samples prompts from the
his wife Cher.”), but an incorrect answer. In conpromptpoolrandomly,2) TOPK-BM25 usesthe
trast, UPRISE induces a precise answer. We at-
4“Limitedmemory”meansthatvanillaChatGPTdoesnot
tributethisimprovementtotheretrieveddemonstra- haveaccesstoexternalknowledgebases.
12324

<!-- Page 8 -->

Reading Comp.
Closed. QA
Paraphrase

## Nli


### Sentiment

10 30 50 70

### Average Performance


## Random Topk-Bm25 Topk-Bert Uprise

Figure6: Comparisonofdifferentuniversalretrievers,wereporttheaverageperformanceoneachtestingcluster.
sparse retriever BM25 (Robertson and Zaragoza, PromptPool Read. Closed. Para. NLI Senti.
2009)toretrievepromptssimilartothetestingin-

## Rawtext 32.0 19.3 44.7 37.5 60.3

put,and3)TOPK-BERTfollowsKATE(Liuetal., UPRISE 40.1 23.4 61.6 43.0 61.8
2022)touseSBERT(ReimersandGurevych,2019)
toretrievesimilarprompts. Table 3: Comparison of average performance on

### Figure6displaysthecomparativeperformance

GPT-Neo-2.7B with different prompt pool: RAW
using GPT-Neo-2.7B, where UPRISE achieves
TEXT uses raw data of the pre-training corpora, UP-
RISEusestrainingdemonstrationsofthetrainedtasks.
thebestresultsamongalltheuniversalretrievers.

### This suggests that word-level (TOPK-BM25) or

sentence-level(TOPK-BERT)similaritytothetestinginputisnottheonlydecisivefactorforagood
prompt. Thisfindingunderscorestheeffectiveness
offine-tuningaretrieverwiththelanguagemodel
itselfasadatalabeler.
7.2 UniversalPromptPool

### For each testing task cluster, we use training

demonstrations of the remaining clusters to construct the prompt pool. To evaluate its effectiveness, wereplaceitwiththerawtextsofwikitext-
103 (Merity et al., 2016), which belongs to the
pre-trainingcorporaofmanyLLMs. Theresultsin
Table3showourpromptpooloutperformstheraw
textsonallthetestingclusters.

### InAppendixF,weanalyzewhichtrainingtask

clusters are retrieved when testing on the heldout cluster, showing that tasks of diverse question/answertypes,suchasReadingComprehension
andClosed-bookQA,aremostfrequentlyretrieved.
Furthermore,inTable7-11inAppendix,weconductacasestudytoanalyzetherelevancebetween
the retrieved prompts and task input, observing
thatthecross-taskimprovementbenefitsfromsimilarquestiontypes,topics,textformats,orlogical
relationships. Thesefindingsunderscoretheimportanceofincludingdiversetaskdemonstrationsin
thepromptpool(Asaietal.,2022;Suetal.,2022).
.gvA

## 100%-Diverse 50%-Diverse 0-Diverse

70
55
40
25
10
Reading. Closed.QA Paraphrase NLI Sentiment

### Testing Task Type

Figure7: Impactoftrainingdatadiversityonthetesting
taskperformance. 100%-DIVERSEisUPRISEretriever
trainedonalltheremainingtasktypes,50%-DIVERSE
reducestherangeoftrainedtasktypestohalfofUPRISE,
and0-DIVERSEis0-SHOT.
8 AnalysisonTrainingDataDiversity
weconductablationstoassesstheimpactoftrainingdatadiversity.
Impact of reducing diversity. We reduce the
rangeoftrainedtasktypestoseetheimpactonthe
testingperformance: Foreachtestingtasktype,we
randomlyselect50%oftheremainingtasktypes
totrainaretriever. TheresultsinFigure7doindicateadeclineinperformanceasdiversitydecreases.
Nonetheless,theretrievertrainedon50%remainingtasktypescontinuestodemonstratebetterperformancethan 0-SHOTacrossmosttasktypes.
12325

<!-- Page 9 -->

Method 0-SHOT UPRISE FEW-SHOT UPRISE-REMAIN-TARGET UPRISE-ALL-TARGET
# Demos 0 3 3 3 3
TrainingData - RemainingTaskTypes - RemainingTaskTypes AllTaskTypes
PromptPool - RemainingTaskTypes TargetTask TargetTask TargetTask

### Read. 31.6 40.1 37.4 48.8 47.4


### Close-QA 19.2 23.3 25.1 28.1 28.9

Paraphrase 47.0 61.6 59.1 61.9 73.4

## Nli 38.3 43.0 43.4 52.1 72.4


### Sentiment 62.7 61.8 72.7 68.7 82.9

Table4: Comparativeresultswithfew-shotprompting. #Demosisthenumberofdemonstrationsprependedtothe
inputinstruction,FEW-SHOTisvanillafew-shotpromptingwherethedemonstrationsarerandomlysampledfrom
thetrainingdemonstrationsofthetargettask(Brownetal.,2020).

## Generalizable To

Read. Closed. Para. NLI Senti.

### Read. - ✓ ✓ ✓ ✓

Closed. ✓ - ✓ ✓ ✓
Para. ✘ ✓ - ✘ ✓

## Nli ✓ ✓ ✓ - ✘

Senti. ✓ ✓ ✓ ✘ -

## Ksat


## Gniniart

task pool, outperforms vanilla few-shot prompting. (3) Substantial improvements are then observed with UPRISE-ALL-TARGET, a unified retriever trained on all task types. These findings
emphasizeUPRISE’seffectivenessasacomprehensivemethodforbothzero-shotandfew-shotprompt
retrieval.
10 RelatedWork
Our work is related to prompt engineering methodsincludingpromptdesign,prompttuning,and
prompt search. Here we discuss prompt search

### Figure8: Generablizabilityofeachtasktype,✓means

the performance of prompt retrieval is better than 0- thatrelatesmostcloselytoourworkanddescribe
SHOT. promptdesignandprompttuninginAppendixE.
Prompt search involves searching for prompts
frompre-trainingcorporaordownstreamtasksto

### Generalizability of each task type. We then

constructtheinputtext(Gaoetal.,2021;Liuetal.,
reducethenumberoftrainedtaskstoonlyoneto
2022; Rubin et al., 2022; Ye et al., 2023, 2022).
testitsgeneralizability. Specifically,foreachtask
Toretrievepromptsforthetestexamples,retrievtype, we train a retriever on this type alone and
erssuchasthesparseretrieverBM25(Robertson
thenevaluateontheremainingtasktypes. ForexandZaragoza,2009)andthedenseretrieverbased
ample, if the retriever trained on A outperforms
onSBERT(ReimersandGurevych,2019)areem-
0-SHOT when testing on B, we regard task type
ployed. Furthermore, methods like EPR (Rubin
A is generalizable to task type B. The results in
et al., 2022) and CEIL (Ye et al., 2023) use the
Figure8demonstratethattaskswithdiverseques-

### LLMitselftoscorethesearchedprompts,thereby

tion/answertypes,suchasReadingComprehension
eliminatingtheneedformanualpromptengineerand Closed-book QA, tend to be more generalizingandensuringpromptingperformance.
able and can serve as representative choices for
trainingauniversalretriever. 11 Conclusion
Thispaperexplorestrainingalightweightandver-
9 ExplorationofFew-ShotLearning
satilepromptretrievertoimprovethezero-shotper-
WecompareUPRISEwithvanillafew-shotprompt- formanceofLLMs. Weinvestigatetheretriever’s
ingandapplyUPRISEtofew-shotpromptretrieval abilitytogeneralizefromthetrainedtasktypesto
in Table 4: (1) Comparing UPRISE with FEW- unseentasktypes,andfromasmallLLMtodiffer-
SHOT, UPRISE approachesandevenoutperforms entLLMsofmuchlargerscales. Wehopeourpaper
vanilla few-shot prompting on most task types; willspurfurtherresearchondevelopingauniversal
(2)UPRISE-REMAIN-TARGET,usingtheretriever assistantfortheever-expandinglandscapeoftasks
trainedonremainingtaskstoretrieveinthetarget andlargelanguagemodels.
12326

<!-- Page 10 -->

Limitations YonatanBisk,RowanZellers,RonanLeBras,Jianfeng

### Gao,andYejinChoi.2020. PIQA:reasoningabout

While UPRISE hasshownconsistentperformance physicalcommonsenseinnaturallanguage. InAAAI,
gains on most testing clusters, it displays limited pages7432–7439.AAAIPress.
impacts on tasks that are directly formulated as

### Sid Black, Leo Gao, Phil Wang, Connor Leahy,

language modeling, such as Coreference Resoluand Stella Biderman. 2021. GPT-Neo: Large
tion and Commonsense Reasoning. Future work ScaleAutoregressiveLanguageModelingwithMeshmayexploreincludingotherformatsofdemonstra- Tensorflow. If youuse this software, please cite it
usingthesemetadata.
tionssuchaschain-of-thought(Weietal.,2022b)
toimprovetheperformance. SamuelR.Bowman,GaborAngeli,ChristopherPotts,
Besides, the universality of UPRISE has been and Christopher D. Manning. 2015. A large anverifiedonlanguageonlyinourexperiment,future notated corpus for learning natural language inference. InEMNLP,pages632–642.TheAssociation
workmayexploretheversatilityof UPRISEbyinforComputationalLinguistics.
corporatingpromptssuchastool-useAPIs(Schick
etal.,2023),andmultimodalinformation(Huang TomB.Brown,BenjaminMann,NickRyder,Melanie
Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind
etal.,2023;Zhangetal.,2023).

### Neelakantan,PranavShyam,GirishSastry,Amanda

Askell, Sandhini Agarwal, Ariel Herbert-Voss,

### EthicsStatement


### Gretchen Krueger, Tom Henighan, Rewon Child,

Aditya Ramesh, Daniel M. Ziegler, Jeffrey Wu,

### Allthedatasets,andthelanguagemodelsusedin

ClemensWinter,ChristopherHesse,MarkChen,Eric
thisworkarepubliclyavailable.

### Sigler,MateuszLitwin,ScottGray,BenjaminChess,

Jack Clark, Christopher Berner, Sam McCandlish,

### Acknowledgments

Alec Radford, Ilya Sutskever, and Dario Amodei.

## Language models are few-shot learners. In

ThefirstauthorwouldliketothankShitaoXiaofor
NeurIPS.
helpfuldebuggingsuggestionsonretrieverimplementation,YuanmengYanforinspirationaldiscus- PaulF.Christiano, JanLeike, TomB.Brown, Miljan

### Martic,ShaneLegg,andDarioAmodei.2017. Deep

sions on the initial ideas of zero-shot prompting,
reinforcementlearningfromhumanpreferences. In
HuazhengWangforcarefulpaperreview,Jinming
NIPS,pages4299–4307.

### Wufordetailedcodeimprovements,andHaifeng

Christopher Clark, Kenton Lee, Ming-Wei Chang,
Sunforencouragementandsupport.

### Tom Kwiatkowski, Michael Collins, and Kristina


### Toutanova. 2019. Boolq: Exploring the surprising

difficulty of natural yes/no questions. In NAACL-

### References


### HLT(1),pages2924–2936.AssociationforCompu-

AkariAsai,TimoSchick,PatrickLewis,XilunChen, tationalLinguistics.
Gautier Izacard, Sebastian Riedel, Hannaneh Ha-

### Jacob Devlin, Ming-Wei Chang, Kenton Lee, and

jishirzi,andWen-tauYih.2022. Task-awareretrieval

### Kristina Toutanova. 2019. BERT: pre-training of

withinstructions. arXivpreprintarXiv:2211.09260.
deepbidirectionaltransformersforlanguageunder-
YejinBang,SamuelCahyawijaya,NayeonLee,Wen- standing. InNAACL-HLT(1),pages4171–4186.AsliangDai,DanSu,BryanWilie,HolyLovenia,Ziwei sociationforComputationalLinguistics.
Ji, Tiezheng Yu, Willy Chung, Quyet V. Do, Yan

### WilliamB.DolanandChrisBrockett.2005. Automati-

Xu,andPascaleFung.2023. Amultitask,multilincallyconstructingacorpusofsententialparaphrases.
gual, multimodal evaluation of chatgpt on reason-
InIWP@IJCNLP.AsianFederationofNaturalLaning,hallucination,andinteractivity. arXivpreprint
guageProcessing.
arXiv:2302.04023.
Luisa Bentivogli, Bernardo Magnini, Ido Dagan, NanDu,YanpingHuang,AndrewM.Dai,SimonTong,
Hoa Trang Dang, and Danilo Giampiccolo. 2009. Dmitry Lepikhin, Yuanzhong Xu, Maxim Krikun,
The fifth PASCAL recognizing textual entailment Yanqi Zhou, Adams Wei Yu, Orhan Firat, Barret
challenge. InTAC.NIST. Zoph, Liam Fedus, Maarten P. Bosma, Zongwei

### Zhou,TaoWang,YuEmmaWang,KellieWebster,

Sumithra Bhakthavatsalam, Daniel Khashabi, Tushar Marie Pellat, Kevin Robinson, Kathleen S. Meier-
Khot, Bhavana Dalvi Mishra, Kyle Richardson, Hellstern, Toju Duke, Lucas Dixon, Kun Zhang,
Ashish Sabharwal, Carissa Schoenick, Oyvind QuocV.Le,YonghuiWu,ZhifengChen,andClaire
Tafjord, and Peter Clark. 2021. Think you have Cui.2022. Glam: Efficientscalingoflanguagemodsolveddirect-answerquestionanswering? tryarc-da, elswithmixture-of-experts. InICML,volume162of
the direct-answer AI2 reasoning challenge. CoRR, ProceedingsofMachineLearningResearch,pages
abs/2102.03315. 5547–5569.PMLR.
12327

<!-- Page 11 -->

OndrejDusek,DavidM.Howcroft,andVerenaRieser. BrianLester,RamiAl-Rfou,andNoahConstant.2021.

## Semanticnoisemattersforneuralnaturallan- The power of scale for parameter-efficient prompt

guagegeneration. InINLG,pages421–426.Associa- tuning. InEMNLP(1),pages3045–3059.AssociationforComputationalLinguistics. tionforComputationalLinguistics.
Tianyu Gao, Adam Fisch, and Danqi Chen. 2021. HectorJ.Levesque,ErnestDavis,andLeoraMorgen-
Makingpre-trainedlanguagemodelsbetterfew-shot stern.2012. Thewinogradschemachallenge. InKR.
learners. InACL/IJCNLP(1),pages3816–3830.As- AAAIPress.
sociationforComputationalLinguistics.

### Xiang Lisa Li and Percy Liang. 2021. Prefix-tuning:

AlecGo,RichaBhayani,andLeiHuang.2009. Twit- Optimizing continuous prompts for generation. In
tersentimentclassificationusingdistantsupervision. ACL/IJCNLP(1),pages4582–4597.Associationfor
Processing,150. ComputationalLinguistics.
Neil Houlsby, Andrei Giurgiu, Stanislaw Jastrzebski, BillYuchenLin,WangchunshuZhou,MingShen,Pei
BrunaMorrone,QuentindeLaroussilhe,AndreaGes- Zhou,ChandraBhagavatula,YejinChoi,andXiang
mundo, Mona Attariyan, and Sylvain Gelly. 2019. Ren.2020. Commongen: Aconstrainedtextgenera-
Parameter-efficient transfer learning for NLP. In tionchallengeforgenerativecommonsensereason-
ICML,volume97ofProceedingsofMachineLearn- ing. InEMNLP(Findings),volumeEMNLP2020of
ingResearch,pages2790–2799.PMLR. FindingsofACL,pages1823–1840.Associationfor
ComputationalLinguistics.

### Edward J. Hu, Yelong Shen, Phillip Wallis, Zeyuan

Allen-Zhu,YuanzhiLi,SheanWang,LuWang,and StephanieLin,JacobHilton,andOwainEvans.2022.
WeizhuChen.2022. Lora: Low-rankadaptationof Truthfulqa: Measuring how models mimic human
largelanguagemodels. InICLR.OpenReview.net. falsehoods. InACL(1),pages3214–3252.AssociationforComputationalLinguistics.

### Shaohan Huang, Li Dong, Wenhui Wang, Yaru Hao,

SakshamSinghal, ShumingMa, TengchaoLv, Lei JiachangLiu,DinghanShen,YizheZhang,BillDolan,
Cui,OwaisKhanMohammed,BarunPatra,Qiang Lawrence Carin, and Weizhu Chen. 2022. What
Liu, Kriti Aggarwal, Zewen Chi, Johan Bjorck, makesgoodin-contextexamplesforgpt-3? InDee-
Vishrav Chaudhary, Subhojit Som, Xia Song, and LIO@ACL,pages100–114.AssociationforCompu-
Furu Wei. 2023. Language is not all you need: tationalLinguistics.

### Aligningperceptionwithlanguagemodels. CoRR,

abs/2302.14045. Xiao Liu, Yanan Zheng, Zhengxiao Du, Ming Ding,

### YujieQian, ZhilinYang, andJieTang.2021. GPT

VladimirKarpukhin,BarlasOguz,SewonMin,Patrick understands,too. CoRR,abs/2103.10385.

### S.H.Lewis,LedellWu,SergeyEdunov,DanqiChen,

andWen-tauYih.2020. Densepassageretrievalfor StephenMerity,CaimingXiong,JamesBradbury,and
open-domain question answering. In EMNLP (1), RichardSocher.2016. Pointersentinelmixturemodpages 6769–6781. Association for Computational els.
Linguistics.

### TodorMihaylov,PeterClark,TusharKhot,andAshish

DanielKhashabi, SnigdhaChaturvedi, MichaelRoth, Sabharwal.2018. Canasuitofarmorconductelec-
Shyam Upadhyay, and Dan Roth. 2018. Looking tricity? A new dataset for open book question anbeyondthesurface: Achallengesetforreadingcom- swering. InEMNLP,pages2381–2391.Association
prehensionovermultiplesentences. InNAACL-HLT, forComputationalLinguistics.
pages252–262.AssociationforComputationalLinguistics. Linyong Nan, Dragomir R. Radev, Rui Zhang, AmritRau,AbhinandSivaprasad,ChiachunHsieh,Xi-
TomKwiatkowski, JennimariaPalomaki, OliviaRed- angru Tang, Aadit Vyas, Neha Verma, Pranav Krfield,MichaelCollins,AnkurP.Parikh,ChrisAlberti, ishna, Yangxiaokang Liu, Nadia Irwanto, Jessica
DanielleEpstein,IlliaPolosukhin,JacobDevlin,Ken- Pan,FaiazRahman,AhmadZaidi,MutethiaMutuma,
tonLee,KristinaToutanova,LlionJones,Matthew YasinTarabar,AnkitGupta,TaoYu,YiChernTan,
Kelcey, Ming-Wei Chang, Andrew M. Dai, Jakob XiVictoriaLin,CaimingXiong,RichardSocher,and
Uszkoreit, Quoc Le, and Slav Petrov. 2019. Natu- NazneenFatemaRajani.2021. DART:open-domain
ralquestions: abenchmarkforquestionanswering structureddatarecordtotextgeneration. InNAACL-
research. Trans.Assoc.Comput.Linguistics,7:452– HLT,pages432–447.AssociationforComputational

## Linguistics.

Nayeon Lee, Yejin Bang, Andrea Madotto, and Pas- Courtney Napoles, Matthew R. Gormley, and Bencale Fung. 2021. Towards few-shot fact-checking jamin Van Durme. 2012. Annotated gigaword. In
via perplexity. In NAACL-HLT, pages 1971–1981. AKBC-WEKEX@NAACL-HLT,pages95–100.Asso-
AssociationforComputationalLinguistics. ciationforComputationalLinguistics.
12328

<!-- Page 12 -->

Altaf Rahman and Vincent Ng. 2012. Resolving McMillan-Major, Iz Beltagy, Huu Nguyen, Lucile
complexcasesofdefinitepronouns: Thewinograd Saulnier, Samson Tan, Pedro Ortiz Suarez, Vicschemachallenge. InEMNLP-CoNLL,pages777– tor Sanh, Hugo Laurençon, Yacine Jernite, Julien

### ACL. Launay, Margaret Mitchell, Colin Raffel, Aaron


### Gokaslan, Adi Simhi, Aitor Soroa, Alham Fikri

Pranav Rajpurkar, Robin Jia, and Percy Liang. 2018. Aji, Amit Alfassy, Anna Rogers, Ariel Kreisberg
Knowwhatyoudon’tknow:Unanswerablequestions Nitzav,CanwenXu,ChenghaoMou,ChrisEmezue,
forsquad. InACL(2),pages784–789.Association ChristopherKlamm,ColinLeong,DanielvanStrien,
forComputationalLinguistics. DavidIfeoluwaAdelani,andetal.2022. BLOOM:

### A176b-parameteropen-accessmultilinguallanguage

PranavRajpurkar,JianZhang,KonstantinLopyrev,and model. CoRR,abs/2211.05100.
PercyLiang.2016. Squad: 100,000+questionsfor
machinecomprehensionoftext. InEMNLP,pages
TimoSchick,JaneDwivedi-Yu,RobertoDessì,Roberta
2383–2392.TheAssociationforComputationalLin-
Raileanu,MariaLomeli,LukeZettlemoyer,Nicola
guistics.
Cancedda,andThomasScialom.2023. Toolformer:
Languagemodelscanteachthemselvestousetools.
NilsReimersandIrynaGurevych.2019. Sentence-bert:
CoRR,abs/2302.04761.
Sentenceembeddingsusingsiamesebert-networks.

### InEMNLP/IJCNLP(1),pages3980–3990.Associa-

Richard Socher, Alex Perelygin, Jean Wu, Jason
tionforComputationalLinguistics.

### Chuang, Christopher D. Manning, Andrew Y. Ng,

StephenE.RobertsonandHugoZaragoza.2009. The andChristopherPotts.2013. Recursivedeepmodprobabilistic relevance framework: BM25 and be- elsforsemanticcompositionalityoverasentiment
yond. Found.TrendsInf.Retr.,3(4):333–389. treebank. InEMNLP,pages1631–1642.ACL.
Melissa Roemmele, Cosmin Adrian Bejan, and An- HongjinSu,WeijiaShi,JungoKasai,YizhongWang,
drew S. Gordon. 2011. Choice of plausible alter- Yushi Hu, Mari Ostendorf, Wen-tau Yih, Noah A.
natives: Anevaluationofcommonsensecausalrea- Smith, Luke Zettlemoyer, and Tao Yu. 2022. One
soning. InAAAISpringSymposium: LogicalFormal- embedder, any task: Instruction-finetuned text emizationsofCommonsenseReasoning.AAAI. beddings.
Ohad Rubin, Jonathan Herzig, and Jonathan Berant.

### Romal Thoppilan, Daniel De Freitas, Jamie Hall,


## Learning to retrieve prompts for in-context


### Noam Shazeer, Apoorv Kulshreshtha, Heng-Tze

learning. InNAACL-HLT,pages2655–2671.Associ-
Cheng,AliciaJin,TaylorBos,LeslieBaker,YuDu,
ationforComputationalLinguistics.
YaGuang Li, Hongrae Lee, Huaixiu Steven Zheng,

### AminGhafouri,MarceloMenegali,YanpingHuang,

KeisukeSakaguchi,RonanLeBras,ChandraBhagavat-

### MaximKrikun,DmitryLepikhin,JamesQin,Dehao

ula,andYejinChoi.2020. Winogrande: Anadver-

### Chen,YuanzhongXu,ZhifengChen,AdamRoberts,

sarialwinogradschemachallengeatscale. InAAAI,
MaartenBosma,VincentZhao,YanqiZhou,Chungpages8732–8740.AAAIPress.

### Ching Chang, Igor Krivokon, Will Rusch, Marc

Pickett,PraneshSrinivasan,LaicheeMan,Kathleen
VictorSanh,AlbertWebson,ColinRaffel,StephenH.
Meier-Hellstern, Meredith Ringel Morris, Tulsee
Bach, Lintang Sutawika, Zaid Alyafeai, Antoine

### Doshi,RenelitoDelosSantos,TojuDuke,JohnnySo-

Chaffin, Arnaud Stiegler, Arun Raja, Manan Dey,
raker,BenZevenbergen,VinodkumarPrabhakaran,

### M Saiful Bari, Canwen Xu, Urmish Thakker,

Mark Diaz, Ben Hutchinson, Kristen Olson, Ale-

### ShanyaSharmaSharma,ElizaSzczechla,Taewoon

jandraMolina,ErinHoffman-John,JoshLee,Lora

### Kim,GunjanChhablani,NihalV.Nayak,Debajyoti

Aroyo, Ravi Rajakumar, Alena Butryna, Matthew
Datta,JonathanChang,MikeTian-JianJiang,Han

### Lamm,ViktoriyaKuzmina,JoeFenton,AaronCo-


### Wang,MatteoManica,ShengShen,ZhengXinYong,

hen,RachelBernstein,RayKurzweil,BlaiseAguera-
HarshitPandey,RachelBawden,ThomasWang,Tr-

### Arcas,ClaireCui,MarianCroak,EdChi,andQuoc

ishala Neeraj, Jos Rozen, Abheesht Sharma, An-
Le.2022. Lamda: LanguagemodelsfordialogapplidreaSantilli,ThibaultFévry,JasonAlanFries,Ryan
cations. CoRR,abs/2201.08239.

### Teehan,TevenLeScao,StellaBiderman,LeoGao,

ThomasWolf,andAlexanderM.Rush.2022. Multitaskpromptedtrainingenableszero-shottaskgener- James Thorne, Andreas Vlachos, Oana Cocarascu,
alization. InICLR.OpenReview.net. ChristosChristodoulopoulos,andArpitMittal.2018.

### TheFEVER2.0sharedtask. InProceedingsofthe

Teven Le Scao, Angela Fan, Christopher Akiki, El- SecondWorkshoponFactExtractionandVERificalie Pavlick, Suzana Ilic, Daniel Hesslow, Roman tion(FEVER).

### Castagné,AlexandraSashaLuccioni,FrançoisYvon,

MatthiasGallé,JonathanTow,AlexanderM.Rush, Mozes van de Kar, Mengzhou Xia, Danqi Chen, and
StellaBiderman,AlbertWebson,PawanSasankaAm- MikelArtetxe.2022. Don’tprompt,search! miningmanamanchi, ThomasWang,BenoîtSagot, Niklas basedzero-shotlearningwithlanguagemodels. In
Muennighoff,AlbertVillanovadelMoral,Olatunji EMNLP,pages7508–7520.AssociationforCompu-
Ruwase, Rachel Bawden, Stas Bekman, Angelina tationalLinguistics.
12329

<!-- Page 13 -->

AäronvandenOord,YazheLi,andOriolVinyals.2018. Yuan Zhang, Jason Baldridge, and Luheng He. 2019.
Representationlearningwithcontrastivepredictive PAWS:paraphraseadversariesfromwordscrambling.
coding. CoRR,abs/1807.03748. InNAACL-HLT(1),pages1298–1308.Association
forComputationalLinguistics.

### Alex Wang, Amanpreet Singh, Julian Michael, Felix

Hill, Omer Levy, and Samuel R. Bowman. 2019. Zhuosheng Zhang, Aston Zhang, Mu Li, Hai Zhao,
GLUE: A multi-task benchmark and analysis plat- George Karypis, and Alex Smola. 2023. Multiform fornatural languageunderstanding. In ICLR modalchain-of-thoughtreasoninginlanguagemod-
(Poster).OpenReview.net. els. CoRR,abs/2302.00923.

### JasonWei, MaartenBosma, VincentY.Zhao, Kelvin

Guu, Adams Wei Yu, Brian Lester, Nan Du, Andrew M. Dai, and Quoc V. Le. 2022a. Finetuned
language models are zero-shot learners. In ICLR.
OpenReview.net.
JasonWei,XuezhiWang,DaleSchuurmans,Maarten
Bosma,EdH.Chi,QuocLe,andDennyZhou.2022b.
Chainofthoughtpromptingelicitsreasoninginlarge
languagemodels. CoRR,abs/2201.11903.
Adina Williams, Nikita Nangia, and Samuel R. Bowman. 2018. A broad-coverage challenge corpus
for sentence understanding through inference. In
NAACL-HLT, pages 1112–1122. Association for
ComputationalLinguistics.

### JiachengYe,ZhiyongWu,JiangtaoFeng,TaoYu,and

LingpengKong.2023. Compositionalexemplarsfor
in-contextlearning.

### SeonghyeonYe,JoelJang,DoyoungKim,YongraeJo,

andMinjoonSeo.2022. Retrievalofsoftpromptenhanceszero-shottaskgeneralization. arXivpreprint
arXiv:2210.03029.
EladBenZaken,YoavGoldberg,andShauliRavfogel.

## Bitfit: Simpleparameter-efficientfine-tuning

fortransformer-basedmaskedlanguage-models. In
ACL(2),pages1–9.AssociationforComputational
Linguistics.
Rowan Zellers, Ari Holtzman, Yonatan Bisk, Ali
Farhadi, and Yejin Choi. 2019. Hellaswag: Can
amachinereallyfinishyoursentence? InACL(1),
pages 4791–4800. Association for Computational
Linguistics.
Rui Zhang and Joel R. Tetreault. 2019. This email
couldsaveyourlife: Introducingthetaskofemail
subjectlinegeneration. InACL(1),pages446–456.
AssociationforComputationalLinguistics.
Susan Zhang, Stephen Roller, Naman Goyal, Mikel

### Artetxe, Moya Chen, Shuohui Chen, Christopher


### Dewan, Mona T. Diab, Xian Li, Xi Victoria Lin,

TodorMihaylov,MyleOtt,SamShleifer,KurtShuster, Daniel Simig, Punit Singh Koura, Anjali Sridhar, Tianlu Wang, and Luke Zettlemoyer. 2022.
OPT: open pre-trained transformer language models. CoRR,abs/2205.01068.
XiangZhang,JunboJakeZhao,andYannLeCun.2015.
Character-levelconvolutionalnetworksfortextclassification. InNIPS,pages649–657.
12330

<!-- Page 14 -->

Appendices C HallucinationMitigationofChatGPT

### A TaskClustering


### WeevaluateChatGPT’sperformanceusingitsre-

Weusethefollowingdatasetsforeachtaskcluster. leasedAPI,withthegpt-3.5-turbo-0301modeland
• Reading Comprehension: SQuADv1 (Ra- atemperatureof0. Humanevaluationisconducted
jpurkaretal.,2016),BoolQ(Clarketal.,2019), to check the accuracy on sampled test examples
MultiRC(Khashabietal.,2018),andOBQA(Mi- fromeachdataset,including66fromTruthfulQA
haylovetal.,2018). tofollowBangetal.(2023),100fromFEVER2.0,
• Closed-book QA: ARC-c/e (Bhakthavatsalam and 100 from the scientific subset of Covid-19.
etal.,2021)andNQ(Kwiatkowskietal.,2019). As types of these tasks have no overlap with the
• Paraphrase Detection: MRPC (Dolan and typeswelistedinAppendixA,weusetheretriever
Brockett, 2005), QQP (Wang et al., 2019), and trainedwithallthelistedtasktypesforthecross-
PawsWiki(Zhangetal.,2019). taskandcross-modelevaluation.
• Natural Language Inference: MNLI-
On the Covid-19 dataset, which requires a
m/mm(Williamsetal.,2018),QNLI(Rajpurkar
true/false answer to input claims, we observe
et al., 2018), SNLI (Bowman et al., 2015), and
vanillazero-shotpromptingoftenleadstoambigu-
RTE(Bentivoglietal.,2009).
ousanswers,whichweconsidertheanswerincor-
• SentimentAnalysis: SST-2(Socheretal.,2013),
rect. However,byconcatenatingretrievedprompts,

### Yelp(Zhangetal.,2015),andSentiment140(Go

primarily focused on natural language inference,
etal.,2009).
ChatGPT generates the correct answer. An ex-
• CommonsenseReasoning: COPA(Roemmele
ample is shown in Figure 9. This suggests the
et al., 2011), HellaSwag (Zellers et al., 2019),
model has access to necessary information but
andPIQA(Bisketal.,2020).
struggleswithmakinginferences,possiblydueto
• Coreferenece Resolution: Winogrande (Sak-
RLHF(Christianoetal.,2017)trainingorinherent
aguchi et al., 2020), DPR (Rahman and Ng,
difficulty.
2012),andWSC273(Levesqueetal.,2012).
• Structure to Text: CommonGen (Lin et al.,
2020), E2ENLG (Dusek et al., 2019), and 0-SHOT
DART(Nanetal.,2021). On July 8 2020, the following claim was made: There is a
possibility for some animals to become infected COVID-19
• Summarization: AESLC(ZhangandTetreault,
throughclosecontactwithinfectedhumans.
2019),AGNews(Zhangetal.,2015),andGiga- Q:Wasthisclaimtrueorfalse?
word(Napolesetal.,2012).
B TuningDetails AsanAIlanguagemodel,Icannotdeterminetheveracityofa
claimwithoutadditionalcontextorinformation.However,itis
widely accepted that some animals, such as cats, dogs, and
minks, can become infected with COVID-19 through close

### Hyperparameter Assignment

contactwithinfectedhumans.
ComputingInfrastructure 8V100-32GBGPUs

### Numberofepochs 3 UPRISE

Run-time 36Hours Scientists at the Genome Institute of Singapore (GIS) have
BatchsizeperGPU 2 discovered the complete genetic sequence of a coronavirus
isolated from a Singapore patient with SARS. Can we infer

### Maximumsequencelength 256

the following? Singapore scientists reveal that SARS virus
Maximumlearningrate 1e-5 hasundergonegeneticchanges.Yes,No,orMaybe?Maybe
Optimizer Adam On July 8 2020, the following claim was made: There is a
possibility for some animals to become infected COVID-19

### Adamepsilon 1e-8

throughclosecontactwithinfectedhumans.
Adambetaweights 0.9,0.999 Q:Wasthisclaimtrueorfalse?
Learningratescheduler warmuplinear

### Weightdecay 0.0


### Warm-upsteps 1000 True


### Learningratedecay linear


### Figure9: Caseofthechatsofvanillazero-shotprompt-

Table 5: Hyperparameter settings of tuning a prompt ingandUPRISEonCovid-19dataset,thelabelcompleretriever tionis“True”.
12331

<!-- Page 15 -->

D AnalysisonPerformanceDecline seriesofintermediatereasoningstepsthatleadto
thefinalanswer.
We conduct analysis on why UPRISE shows neg-

### Prompt Tuning. Traditional natural language

ative performance when testing on Coreference
promptsrequiresignificanthumanengineeringand
ResolutionandCommonsenseReasoningtasks.
canleadtosuboptimalperformance. Prompttuning
CoreferenceResolutionhardlybenefitsfrom proposestolearnapromptrepresentedbycontindemonstrations. ForCoreferenceResolutiontask uous parameters rather than discrete natural lantype,weobservethatevenvanillafew-shotprompt- guage tokens (Liu et al., 2021). Prompt tuning
ing underperforms zero-shot prompting, as high- takes the source text embedded by the LM input
lighted in Table 65. This trend is consistent with embeddings and prepends learnable embeddings
GPT-3 (Brown et al., 2020), GLaM (Du et al., toobtainanewembeddedsequence. Avariantof
2022),andLaMDA-PT(Thoppilanetal.,2022),as prompttuningisprefixtuning(LiandLiang,2021;
reportedbyFLAN(Weietal.,2022a). Thesemod- Lesteretal.,2021),wherethelearnablevectorsare
elsalsoexhibitlimitedperformancegainfromfew- added not only to the input but to all transformer
shotpromptingcomparedtozero-shotforCorefer- layers.
enceResolution. Wededucethatthetask’sinherent
naturemightmakeitlessresponsivetodemonstra- F AnalysisonRetrievedTraining
tions,regardlessoftheiralignmentwiththetask. Clusters
To further interpret the impact of the retrieved

### Method 0-SHOT FEW-SHOT

promptsonthetestingtaskperformance,weana-
Coreference. 59.3 50.6 lyzewhichtrainingtaskclustersareretrievedwhen
testingontheheld-outcluster.
Table6: Averagescoresofvanillazero-shotandfew-

### AsshowninthevisualisationplotinFigure10,

shotpromptingofCoreferenceResolutiontasks.
clustersincludingdiversequestiontypeslikeReadingComprehensioncorrespondtohighretrievedra-
CommonsenseReasoningisharmedbydiffertios(e.g.,80.7%forClose-QAand36.1%forNLI),
entdemonstrationformat. Byanalyzingtherewhile the less diverse Sentiment Analysis cluster
trievedtrainingtasktypes(asshowninFigure10),
does not reach the top ranks. This finding furwefindthatClosed-bookQAisthemost-frequently
thersupportsthatincludingtasksofdiversequesretrievedtypewhentestingCommonsenseReasontion/answer types in the training data contributes
ing. However,thetwotypesdiffersignificantlyon
togoodgeneralizabilityoftheretriever.
theinput-outputformat: Closed-bookQAfollows
a question-answering format, but Commonsense

## Retrievedpromptcluster(%)


### Reasoningfollowsthelanguagemodelingformat,

whichmayleadtothedecreaseinperformance. Read. Closed NLI Para. Senti.Comm. Core. Summ.Struct.
Read. 0.0 37.5 33.1 3.7 7.8 3.3 1.8 12.5 0.2

### E ExtendedRelatedWork

Closed 80.7 0.0 16.9 0.9 0.0 1.1 0.2 0.1 0.0

### Nli 36.1 11.5 0.0 47.0 0.6 2.1 2.5 0.2 0.1

PromptDesign. In-contextLearning(Brownetal.,
Para. 4.8 6.2 13.9 0.0 0.2 0.1 74.4 0.4 0.0
2020)isamethodthathelpsLLMstransfertonew
tasksviainferencealonebyconditioningaconcate- Senti. 17.7 5.1 23.4 1.3 0.0 9.4 1.9 34.9 6.2
nationoftrainingdemonstrationsandtestinginput, Comm. 19.3 40.7 2.1 0.1 12.4 0.0 23.5 1.7 0.3
withoutanygradientupdates. Core. 1.6 3.3 1.1 33.1 0.1 51.5 0.0 9.4 0.1
Withstandardin-contextlearning,LLMsstruggle to tackle complex arithmetic, commonsense,
andsymbolicreasoningtasks. Chain-of-Thoughts
(CoT)(Weietal.,2022b)proposesprovidingLLMs
with a series of intermediate reasoning steps as
demonstrationstoinduceLLMstoproduceanother
5WSC273datasetofCoreferenceResolutionhasnotrainingset,thusit’sexcludedfromtheaveragetaskscorescalculation.

## Retsulcgnitset

Figure 10: Percentages of retrieved prompts in each
trainingtaskclusterwhentestingontheheld-outcluster.
12332

<!-- Page 16 -->


## Testing Cluster: Task

ReadingComprehension: SQuADv1(Rajpurkaretal.,2016)

## Input Instruction

Hereisaquestionaboutthisarticle: AsofAugust2010,Victoriahad1,548publicschools,489Catholic
schoolsand214independentschools. Justunder540,800studentswereenrolledinpublicschools,and
justover311,800inprivateschools. Over61percentofprivatestudentsattendCatholicschools. More
than 462,000 students were enrolled in primary schools and more than 390,000 in secondary schools.
Retentionratesforthefinaltwoyearsofsecondaryschoolwere77percentforpublicschoolstudentsand
90percentforprivateschoolstudents. Victoriahasabout63,519full-timeteachers. Whatistheanswer
tothisquestion: WhatpercentageofprivateschoolstudentsgotoCatholicschools?

## Label Completion

61

## Prompt Cluster: Task

Closed-bookQA:NaturalQuestions(Kwiatkowskietal.,2019)

## Demonstration Input

Whatistheanswertothisquestion? Whatistheofficialpovertyrateintheus?

## Demonstration Answer


### In2015,13.5%


## Testing Cluster: Task

ReadingComprehension: MultiRC(Khashabietal.,2018)

## Input Instruction

Whatcausesachangeinmotion? Theapplicationofaforce. Anytimeanobjectchangesmotion,aforce
hasbeenapplied. Inwhatwayscanthishappen? Forcecancauseanobjectatresttostartmoving. Forces
cancauseobjectstospeeduporslowdown. Forcescancauseamovingobjecttostop. Forcescanalso
causeachangeindirection. Inshort,forcescausechangesinmotion. Themovingobjectmaychangeits
speed,itsdirection,orboth. Weknowthatchangesinmotionrequireaforce. Weknowthatthesizeof
theforcedeterminesthechangeinmotion. Howmuchanobjectsmotionchangeswhenaforceisapplied
dependsontwothings. Itdependsonthestrengthoftheforce. Italsodependsontheobjectsmass. Think
aboutsomesimpletasksyoumayregularlydo. Youmaypickupabaseball. Thisrequiresonlyavery
smallforce. Afterreadingtheabove,is“No”thecorrectanswertothequestion“Wouldthemassofa
baseballaffecthowmuchforceyouhavetousetopickitup?”?,

## Label Completion


### No


## Prompt Cluster: Task

NaturalLanguageInference: QNLI(Rajpurkaretal.,2018)

## Demonstration Input

Q:Whattemperaturearecaskalesstoredatbeforebeingtapped? A:Typically,whenacaskarrivesina
pub,itisplacedhorizontallyonaframecalleda“stillage”whichisdesignedtoholditsteadyandatthe
rightangle,andthenallowedtocooltocellartemperature,beforebeingtappedandventedtapisdriven
througha(usuallyrubber)bungatthebottomofoneend,andahardspileorotherimplementisused
toopenaholeinthesideofthecask,whichisnowuppermost. Doestheanswercorrectlyanswerthe
question?

## Demonstration Answer


### Yes

Table7: ExamplesoftestinginputandtargetofReadingComprehensioncluster,andtheretrievedtop-1demonstrationfromtheremainingclusters. Thefirstexampleinvolvesstatisticalquestionsinboththetestinginputand
prompt,whilethesecondexamplerequiresabinary"Yes"or"No"answerinboththeinputandprompt.
12333

<!-- Page 17 -->


## Testing Cluster: Task

Closed-bookQA:ARC(Bhakthavatsalametal.,2021)

## Input Instruction

Whichstatementbestexplainswhyphotosynthesisisthefoundationofmostfoodwebs? Picktheanswer
fromtheseoptions.

## Label Completion

Sunlightisthesourceofenergyfornearlyallecosystems.

## Prompt Cluster: Task

ReadingComprehension: OBQA(Mihaylovetal.,2018)

## Demonstration Input

Rootsareavehicleforabsorbingwaterandnutrientsfromsoilintotheplant. Whichofthefollowingis
likelytorejectnutrientsfromfood?

## Demonstration Answer


### Bamboo


## Testing Cluster: Task

Closed-bookQA:NaturalQuestions(Kwiatkowskietal.,2019)

## Input Instruction

Q:WhendidTaylorSwift’sfirstalbumrelease? A:

## Label Completion


### October24,2006


## Prompt Cluster: Task

ReadingComprehension: SQuADv1(Rajpurkaretal.,2016)

## Demonstration Input

In October 2014, Beyoncé signed a deal to launch an activewear line of clothing with British fashion
retailerTopshop. The50-50ventureiscalledParkwoodTopshopAthleticLtdandisscheduledtolaunch
itsfirstdance,fitnessandsportsrangesinautumn2015. ThelinewilllaunchinApril2016. Q:Whenwill
thefulllineappear?

## Demonstration Answer


### April2016

Table8: ExamplesoftestinginputandtargetofClosed-bookQAcluster,andtheretrievedtop-1demonstration
fromtheremainingclusters. Inthefirstcase,boththetestinginputandthepromptrelatetothetopicofbotany. In
thesecondcase,boththeinputandpromptinvolvequestionsabouttimeandsharethetopicofAmericansingers
(TaylorSwiftandBeyoncé).
12334

<!-- Page 18 -->


## Testing Cluster: Task

ParaphraseDetection: PawsWiki(Zhangetal.,2019)

## Input Instruction


## JohnBarrowIslandisamemberoftheQueenElizabethIslandsandtheCanadianArcticArchipelagoin

theterritoryofNunavut. 2.JohnBarrowIslandisamemberoftheCanadianArcticArchipelagoandthe
QueenElizabethIslandsintheNunavutarea. Arethesetwosentencesparaphrasesofeachother?

## Label Completion


### No


## Prompt Cluster: Task

CoreferenceResolution: DPR(RahmanandNg,2012)

## Demonstration Input

Considerthissentence: WhenMr.Bond,theveterinarian,cametolookattheblackhorsethatlaygroaning
onthegrass,hefelthimallover,andshookhishead;oneofhislegswasbroken. Are“his”and“theblack
horse”thesame?

## Demonstration Answer


### Yes


## Testing Cluster: Task

ParaphraseDetection: MRPC(DolanandBrockett,2005)

## Input Instruction

ThisintegrateswithRationalPurifyPlusandallowsdeveloperstoworkinsupportedversionsofJava,
Visual C# and Visual Basic.NET. IBM said the Rational products were also integrated with Rational
PurifyPlus,whichallowsdeveloperstoworkinJava,VisualC#andVisualBasic.Net. Ifthefirstsentence
istrue,isthesecondonealsotrue?

## Label Completion


### Yes


## Prompt Cluster: Task

NaturalLanguageInference: MNLI(Williamsetal.,2018)

## Demonstration Input

Sentence1: “uponthetidalbulgeintoastorm’sbarometriclow,”Sentence2: “Astorm’sbarometriclow
wasonthetidalbulge.” Ifthefirstsentenceistrue,thenisthesecondsentencetrue? Yes,No,orMaybe?

## Demonstration Answer


### Yes

Table9:ExamplesoftestinginputandtargetofParaphraseDetectioncluster,andtheretrievedtop-1demonstration
fromtheremainingclusters. Inbothcases,theretrievedpromptshavesimilarsentenceformatstothetestinginput.
12335

<!-- Page 19 -->


## Testing Cluster: Task

NaturalLanguageInference: MNLI(Williamsetal.,2018)

## Input Instruction

Hereisapremise: “ThissiteincludesalistofallawardwinnersandasearchabledatabaseofGovernment
Executivearticles.” Hereisahypothesis: “TheGovernmentExecutivearticleshousedonthewebsiteare
notabletobesearched.” Isitpossibletoconcludethatifthepremiseistrue,thensoisthehypothesis?

### Yes,No,orMaybe?


## Label Completion


### No


## Prompt Cluster: Task

ParaphraseDetection: MRPC(DolanandBrockett,2005)

## Demonstration Input

“AndtheywilllearnthemeaningofAmericanjustice,”hesaidtostrongandextendedapplause. “The
U.S.willfindthekillersandtheywilllearnthemeaningofAmericanjustice,”Bushtoldthecrowd,which
burstintoapplause. Ifthefirstsentenceistrue,isthesecondonealsotrue?

## Demonstration Answer


### No


## Testing Cluster: Task

NaturalLanguageInference: QNLI(Rajpurkaretal.,2018)

## Input Instruction

Doesthesentence“Thesymptomsofinflammationareredness,swelling,heat,andpain,whicharecaused
byincreasedbloodflowintotissue.” provideavalidanswertothequestion“Whatcausesthesymptoms
ofinflammation?”?

## Label Completion


### Yes


## Prompt Cluster: Task

CommonsenseReasoning: COPA(Roemmeleetal.,2011)

## Demonstration Input

Answerthefollowingquestionaboutthissentence: “Thespydiscoveredtheenemy’slocation.” Whatis
thecause?

## Demonstration Answer

Thespybuggedtheenemy’sphone.
Table10: ExamplesoftestinginputandtargetofNaturalLanguageInferencecluster,andtheretrievedtop-1
demonstrationfromtheremainingclusters. Inthefirstcase,boththetestinginputandthepromptsshareasimilar
questionformat,askingwhethersomethingremainstrueundercertainconditions. Inthesecondcase,boththeinput
andpromptaskaquestionaboutthelogicalrelationshipbetweencauseandeffect.
12336

<!-- Page 20 -->


## Testing Cluster: Task

SentimentAnalysis: SST-2(Socheretal.,2013)

## Input Instruction

“it’sslow—very,veryslow.” Howwouldthesentimentofthissentencebeperceived?

## Label Completion


### Negative


## Prompt Cluster: Task

CommonsenseReasoning: COPA(Roemmeleetal.,2011)

## Demonstration Input

“Themanwentintodenialaboutthetragedy.” Whatistheeffectoftheprecedingsentence?

## Demonstration Answer

Herefusedtotalkaboutit.

## Testing Cluster: Task

SentimentAnalysis: Sentiment140(Goetal.,2009)

## Input Instruction

Reading my kindle2... Love it... Lee childs is good read. How would the sentiment of this tweet be
described?

## Label Completion


### Positive


## Prompt Cluster: Task

Summarization: AESLC(ZhangandTetreault,2019)

## Demonstration Input

Witmakesitsownwelcome,andlevelsalldistinctions. Nodignity,nolearning,noforceofcharacter,can
makeanystandagainstgoodwit. -Ralph. Generateasubjectlineforthisemail.

## Demonstration Answer

Whatawonderisawonderfulwit...
Table11: ExamplesoftestinginputandtargetofSentimentAnalysiscluster,andtheretrievedtop-1demonstration
fromtheremainingclusters. Inbothcases,theretrievedpromptsharesthesamesentimentasthetestinginput,
facilitatingthelanguagemodeltoaccuratelypredictthesentiment.
12337

## Tables

**Table (Page 7):**

| 60 55 50 .gvA 45 40 35 GPT-Neo-2.7BBLOOM-7.1B OPT-66B Davinci Davinci-001 |  |
|---|---|
|  | 55 50 .gvA 45 40 35 GPT-Neo-2.7BBLOOM-7.1B OPT-66B Davinci Davinci-001 |
|  | 0-SHOT UPRISE |


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


**Table (Page 7):**

|  |  |
|---|---|
|  |  |


**Table (Page 8):**

|  |  |  |
|---|---|---|
|  |  |  |


**Table (Page 8):**

|  |  |  |
|---|---|---|
|  |  |  |


**Table (Page 8):**

|  |  |  |
|---|---|---|
|  |  |  |


**Table (Page 15):**

| 0.0 | 37.5 | 33.1 | 3.7 | 7.8 | 3.3 | 1.8 | 12.5 | 0.2 |
|---|---|---|---|---|---|---|---|---|
| 80.7 | 0.0 | 16.9 | 0.9 | 0.0 | 1.1 | 0.2 | 0.1 | 0.0 |
| 36.1 | 11.5 | 0.0 | 47.0 | 0.6 | 2.1 | 2.5 | 0.2 | 0.1 |
| 4.8 | 6.2 | 13.9 | 0.0 | 0.2 | 0.1 | 74.4 | 0.4 | 0.0 |
| 17.7 | 5.1 | 23.4 | 1.3 | 0.0 | 9.4 | 1.9 | 34.9 | 6.2 |
| 19.3 | 40.7 | 2.1 | 0.1 | 12.4 | 0.0 | 23.5 | 1.7 | 0.3 |
| 1.6 | 3.3 | 1.1 | 33.1 | 0.1 | 51.5 | 0.0 | 9.4 | 0.1 |
