---
title: "PREFER Prompt Ensemble Learning"
original_file: "./24_PREFER_Prompt_Ensemble_Learning.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["prompt-engineering", "llm", "rag", "chain-of-thought", "fine-tuning"]
keywords: ["prompt", "our", "feedback", "cid", "prefer", "reflect", "boosting", "bagging", "ensemble", "apo"]
summary: "<!-- Page 1 -->

PREFER: Prompt Ensemble Learning via Feedback-Reflect-Refine

### ChenruiZhang1(cid:66),LinLiu2*,JinpengWang1,


### ChuyuanWang1,XiaoSun1,HongyuWang1,MingchenCai1

1MeituanInc.,Beijing,China2BeijingJiaotongUniversity,Beijing,China
(cid:66)chenrui.zhang@pku.edu.cn,linliu@bjtu.edu.cn,{wangjinpeng04,wangchuyuan,
sunxiao10,wanghongyu15,caimingchen}@meituan.com
Abstract 6
5 Refine
As an effective tool for eliciting the power of Large Lan- How to solve issues
guageModels(LLMs),prompt"
related_documents: []
---

# PREFER Prompt Ensemble Learning

<!-- Page 1 -->

PREFER: Prompt Ensemble Learning via Feedback-Reflect-Refine

### ChenruiZhang1(cid:66),LinLiu2*,JinpengWang1,


### ChuyuanWang1,XiaoSun1,HongyuWang1,MingchenCai1

1MeituanInc.,Beijing,China2BeijingJiaotongUniversity,Beijing,China
(cid:66)chenrui.zhang@pku.edu.cn,linliu@bjtu.edu.cn,{wangjinpeng04,wangchuyuan,
sunxiao10,wanghongyu15,caimingchen}@meituan.com
Abstract 6
5 Refine
As an effective tool for eliciting the power of Large Lan- How to solve issues
guageModels(LLMs),promptinghasrecentlydemonstrated according to the situation? 7
unprecedentedabilitiesacrossavarietyofcomplextasks.To

### Different strokes for

further improve the performance, prompt ensemble has at- different folks.
tractedsubstantialinterestfortacklingthehallucinationand Input Answer Ground Truth
instabilityofLLMs.However,existingmethodsusuallyadopt
a two-stage paradigm, which requires a pre-prepared set of 4 Reflect { , }
promptswithsubstantialmanualeffort,andisunabletoper-

### Sick

formdirectedoptimizationfordifferentweaklearners.Inthis
paper,weproposeasimple,universal,andautomaticmethod How to solve? { , }
named PREFER (PRompt Ensemble learning via Feedback-

### Bug


## 1 Llm 2


### REflect-Refine)toaddressthestatedlimitations.Specifically,

given the fact that weak learners are supposed to focus on { , }
hard examples during boosting, PREFER builds a feedback 3 Feedback

### Rainstorm

mechanism for reflecting on the inadequacies of existing How to solve the rest? Hard Examples
weaklearners.Basedonthis,theLLMisrequiredtoautomaticallysynthesizenewpromptsforiterativerefinement.More- Figure 1: High-level overview of feedback-reflect-refine
over,toenhancestabilityoftheprompteffectevaluation,we paradigm.p denotesthepromptatthet-thiteration.
t
propose a novel prompt bagging method involving forward
andbackwardthinking,whichissuperiortomajorityvoting
trinsicknowledgeandreasoningabilityofLLMsbasedona
andisbeneficialforbothfeedbackandweightcalculationin
pretrain-prompt-predictmanner(Liuetal.2023).
boosting. Extensive experiments demonstrate that our PRE-
FER achieves state-of-the-art performance in multiple types Though promising, the na¨ıve prompting approaches are
oftasksbyasignificantmargin.Wehavemadeourcodepub- afflictedbyseverallimitations.Asgenerativelanguagemodliclyavailable1. els, LLMs’ output commonly has a large variance. For instance, the reasoning logic and predicted results could be
Introduction contradictory in multiple runs, although the input prompts
arefixed.Inaddition,LLMssufferfromthenotoriouslyhal-

### Large Language Models (LLMs) have recently flourished

lucination issue (Ji et al. 2023), leading to results that are
acrossavarietyoffields,demonstratingunprecedentedabilplausible-soundingbutfactuallyincorrectorirrelevanttothe
itiesinmyriadofcomplextasks(Zhaoetal.2023b;Ouyang
inputs.Furthermore,thequalityofLLMs’outputissuscepet al. 2022). Trained with large-scale web data on massive
tibletothegivenprompts,whichentailssubstantialmanual
parameters,LLMsshowemergentabilitiesbeyondtheorigeffortanddomainexpertisetofindoutthereliableprompts.
inallinguisticcompetence(Weietal.2022a),whichperform
As a promising solution to these issues, prompt ensemtremendous versatility in both academia and industry. To
blelearninghasattractedsubstantialinterestinthecommuelicitthepowerofpretrainedLLMsdirectlyoradaptLLMs
nity very recently, demonstrating significant improvements
tospecificdomains,variousparadigmsareproposed,includin both effectiveness and stability across various tasks. As
ing prompt engineering (Qiao et al. 2022), p-tuning (Liu
a representative work, PromptBoosting (Hou et al. 2023)
etal.2021),andLoRAfinetuning(Huetal.2021),etc.Due
applies the traditional ADABOOST (Freund and Schapire
totheimmensescaleofthemodelparameters,finetuningon
1997) algorithm over a set of pre-defined prompts for text
all or even part of LLMs is costly and time-consuming. To
classification. BPE (Pitis et al. 2023) focuses on Chain-ofthis end, as a simple and effective paradigm, prompt engi-
Thought(CoT)(Weietal.2022b)boostingandbuildsfewneering explores a fundamentally new way of invoking inshot CoT prompts based on self-consistency (Wang et al.
*ThisworkwasdoneduringtheinternshipatMeituan. 2022). These efforts empirically demonstrate the strength
1https://github.com/zcrwind/PREFER ofpromptensemblesforLLM-basedtasks,yieldingexcep-
3202
guA
32
]LC.sc[
1v33021.8032:viXra

<!-- Page 2 -->

tionalperformancegainsoversingle-promptbaselines. fectivenessandefficiency.
However, despite their success, existing prompt ensem- Weconductextensiveexperimentsandin-depthcasestudble approaches, which typically adopt a two-stage process, iesonanumberoftasks,includingreasoning,topicclassifihave several limitations. First, they require a pre-prepared cation,hatespeechdiscrimination,etc.Theempiricalresults
set of prompts in advance, which are either manually de- testifytheeffectivenessofourPREFERapproach.Moreover,
fined or generated by another language model with heavy PREFER shows superiority in both stability and efficiency
parameters. This preliminary work is costly and laborious, comparedtoexistingapproaches.Wewillprovidethesource
ofteninvolvingatrial-and-errororpre-evaluationprocessto codeforreproducibilityinthesupplementarymaterial.
ensurethequalityofpre-definedprompts.Second,thetwostageparadigmfixesthepromptstobeusedintheensemble RelatedWork
process, limiting the adaptability and scalability of prompt
Ourworkisconceptuallyrelatedtoseveralsubareasofartiboosting,asthepromptscannotbeoptimizedjointly.Since
ficialintelligent,includingLargeLanguageModels(LLMs),
the relationships between prompts are ignored during the
prompt engineering, and prompt ensemble learning. In this
iterative boosting process, the pre-defined prompts tend to
section,webrieflyreviewtheworksineachsubarea.
besub-optimalandsusceptible.Moreover,existingmethods
conductensembleseitherinboostingorinbaggingindivid-

### LargeLanguageModels

ually,neglectingthepotentialbenefitsofcombiningthetwo
worldstoenhanceperformance. Nowadays,LargeLanguageModels(LLMs)havemaderev-
Toalleviatetheaboveissues,weadvocatethatasmarter olutionaryprogressandposedsignificantimpactonvarious
paradigm for prompt ensemble in the era of LLMs is ex- artificialintelligentcommunity(Zhaoetal.2023b;Ouyang
pectedtobeautomatic,self-adaptiveandjoint-optimizable. etal.2022).Accordingtothescalelaw,LLMsdemonstrate
Such paradigm reduces the need for manual effort and do- unprecedentpower(calledemergentabilities)withtherapid
mainexpertise,aswellastakespromptrelationsintoconsid- growth of model parameters and data volume (Wei et al.
eration for directed optimization. Accordingly, we propose 2022a). For instance, the most prominent applications ina simple, automatic and universal approach called PREFER cluding ChatGPT and GPT-4 (OpenAI 2023) have shown
(PRomptEnsemblelearningviaFeedback-REflect-Refine), surprisingreasoningability,human-likeconversationskills,
towards a more effective prompt ensemble via utilizing aswellasarichreserveoffactualcommonsense.Basedon
the generative and reflective capabilities that LLMs excel the surprising emergent abilities, a series of classical algoat(Madaanetal.2023).AsshowninFigure1,ourPREFER rithmscanevolvetoamoreintelligentversion.Inthispaper,
adopts a feedback-reflect-refine circle for prompt boosting. weprovideapilotworkonensemblealgorithmasaprelim-
Concretely speaking, inspired by the fact that weak learn- inary study. We believe that our proposed approach could
ers pay more attention to hard examples via weight redis- not only simply serve as a strong baseline to foster future
tribution during boosting, we propose to transfer this hard- researchonpromptensemble,butalsoshedlightontheposample-oriented weighting into nature language feedback, tential research direction towards improving classical algowhich returns error information to the LLM for reflection. rithmswiththepowerofLLMs.
Hence,consideringthereflectioninformation,theLLMper-

### PromptEngineering

ceives the inadequacies of existing prompts and is able to
generatenewpromptstorefinethempurposefully.Attribute In order to invoke the power of LLMs, a series of apto the feedback-reflect-refine path, the LLM jointly opti- proaches have been proposed in the community, including
mizesthedownstreamtaskssolvingandpromptgeneration parameter-efficient fine-tuning (Hu et al. 2021; Liu et al.
in an automatic manner. Iterating along this path, potential 2021) and prompt engineering (Qiao et al. 2022; Liu et al.
conflictandredundancyamongpromptsarereduced,which 2023),etc.DuetotheheavyweightofLLMs,fullyoreven
isvitalforbuildingamorestableandfasterlearner. partlyfine-tuningthemisexpensiveandinefficient.Accord-
Furthermore, to adequately unleash the ability of each ingly, as an out-of-the-box paradigm, prompt engineering
prompt and further enhance the stability during boosting, (akaprompting)hasemergedasanewapproachforadapting
we propose a bilateral bagging approach, which incor- pretrain-prompt-predictpathfordownstreamtasks.Tremenporates forward and backward thinking for multi-source douscutting-edgeefforthasbeenmadetowardsthisareato
verification. Specifically, drawing inspiration from human improvetheperformanceofprompting.Concretely,promptdecision-making, wherein uncertain answers are often re- ing adopts natural language as additional inputs, acting as
solved through a process of elimination, we instruct the instructions or hints to LLMs. For example, GPT2 (Rad-
LLM to compute a confidence score for each response and ford et al. 2019) allows for unsupervised learning of LLM
subsequently filter out the most uncertain answers. Given onmultipletasksthroughhandcraftedtask-specificprompts.
theobservedtendencyofLLMstooverestimateconfidence However, building prompts manually can be expensive, biin their predictions (Zhao et al. 2021), our bilateral bag- ased and sub-optimal (Liu et al. 2023). Another line of
gingapproachassessestheresponsesfrombothforwardand worksaredevotedtoconductingpromptinginanautomatic
backward directions, in which the overconfidence bias can way. STaR (Zelikman et al. 2022) utilizes a simple loop to
be counteracted subtly. The empirical results demonstrate bootstrapLLMswithaself-taughtmanner,inwhichChainthe superiorityof our bilateralbagging approach compared of-Thought(CoT)(Weietal.2022b)rationaleisiteratively
tootherregularmethodssuchasmajorityvotinginbothef- generatedtohintthequestionansweringprocess.Closerto

<!-- Page 3 -->

Feedback
weight
update

### Boosting

{ , } { , }
Bilateral Bilateral
Bagging Bagging

## Llm

For , succeed, but failed. Refine Iteration
How to solve the rest? Prompt Weight

### Boosting Error

Instance Weight
weight
update

### Bilateral Prompt Bagging

T o o c o c n o t a a r i s n e s d c e o s n c f r u ip si t n io g n w . ords. Reflect
No guidance for evidence...
Figure2:ThepipelineofPREFER.Giventheinitialpromptp
0
,LLMpartiallysolvestheproblemviaincorporatingbackward
thinking.Thentheerrorinformationwillbeusedforpromptoptimizationthroughthefeedback-reflect-refineprocess.Iterating
thisprocessandfinallyensemblingpromptsbasedonevolvedweights.
ourwork,APO(Pryzantetal.2023)iterativelyoptimizesthe x ∈ X denotes the input texts and y ∈ Y denotes the
i i
singlepromptinafeedbackmanner,whichtreatsthetextual outputlabel.Itisnotedthataninitialpromptp isprovided
0
reflectioninformationasgradientinclassicaldeeplearning. astheseedforthesubsequentiteration.Insteadofrequiring
anysupervisedfine-tuning(SFT)orreinforcementlearning,
PromptEnsembleLearning our proposed PREFER utilizes out-of-box LLM API (e.g.,

### ChatGPT or GPT-4) as the foundation model M for uni-

Prior studies have proven that LLMs have multiple reasonversalityandflexibility.AsillustratedinFigure2,ourPRE-
ing paths for a single problem, which could lead to dis-

### FER mainly contains two components, i.e. feedback-driven

tinct outputs from identical inputs (Wang et al. 2022). To
prompt boosting and bilateral prompt bagging, which will
thisend,promptensemblelearninghasbeenpresentedasa
beelaboratedinsectionsbelow.
solution,whichcombinesseveralindividualpromptstoobtain better stability and generalization performance. Boost-

### PromptBoostingviaFeedback-Reflect-Refine

ing and bagging are two typical ensemble methods widely
adopted in numerous classical tasks, while their adaptation Before delving into the technical details of the proposed
on LLMs is still in its infancy. Current works for prompt prompt boosting approach, we first provide our design
boosting typically utilize a two-stage paradigm. Prompt- principle, based on the thinking about what characteristics
Boosting (Hou et al. 2023) has done a preliminary trial on should an intelligent prompt boosting have in the era of
this way, which conducts the traditional ADABOOST (Fre- LLMs.ReviewthatboostingalgorithmscombineseveralinundandSchapire1997)algorithmoverapre-definedprompt dividual weak learners to obtain better generalization persetfortextclassification.Ontheotherhand,existingprompt formance.Consideringthefactthatweakerlearnersaresupbaggingapproachesmainlyrelyonregularmajorityvoting, posed to pay more attention to hard samples during boostwhichcanbecomputationallyintensive.Notably,BPE(Pitis ing, we advocate that an intelligent boosting algorithm is
et al. 2023) focuses on constructing few-shot CoT prompts expected to understand what problems the previous weak
based on self-consistency (Wang et al. 2022), which offers learners cannot solve. That is, instead of building prompts
better performance than a single prompt in the case of in- individually, the relation among prompts should be considtroducing exponentially additional computation. In this pa- ered for better performance and faster convergence. In anper, we propose a computation-efficiency prompt bagging other vein, to reduce the manual effort, the prompt boostapproach inspired by the human ethology, which incorpo- ingprocessshouldbeautomatic,whereeachpromptcanbe
ratespromptboostingforfurtherperformanceimprovement. constructed without manual intervention. Furthermore, the
prompt boosting should be universal and adaptive, for em-
Our PREFER Approach powering any prompting-based task with the superiority of
ensemblelearningseamlessly.

### Preliminaries


### Our proposed PREFER embraces all the above design

In this section, we introduce preliminaries of our PREFER principles,towardsasimple,automaticandadaptiveprompt
approach, including the problem formulation and the dis- ensemble paradigm. Inspired by the classical boosting almantlingofkeycomponents. gorithm such as ADABOOST (Freund and Schapire 1997)
Considering a reasoning or classification task driven by anditerativepromptingalgorithms(Pryzantetal.2023),we
(cid:83)
LLMs, given the training data D = {(x ,y )}, the adoptaniterativemannertobuildthepromptsetwhereeach
tr i i i
goaloftheproposedPREFERistoautomaticallyconstructa prompt is treated as a weak learner. As illustrated in Fig-
(cid:83) (cid:83)
promptsetP = {p }alongwithpromptweights {λ } ure 2, acting as a weak learner, each prompt can only hant t t t
viaLLM-augmentedensemblelearning,whichcanthenbe dle part of the instance space, where new prompts will be
utilized cooperatively for the subsequent inference. Here added to expand the solving space by introducing more in-

<!-- Page 4 -->

Listing1:solving prompt seriesofreasonswhythecurrentpromptp cansolvesome
t
# Task examples well but not others. Based on the reflection, the
Given two sentences, determine whether LLM is asked to generate new prompts in connection with
sentence 2 provides an answer to the hard examples specified in the previous iteration. In detail,
question posed by sentence 1. the sampled wrong examples and corresponding textual labelsarecombinedtoerror infoinListing2.Mathemat-
# Output format ically,thisfeedback-reflect-refineprocesscanbeformulated
Explain your reasoning process in one
viatheBayesiantheory:
sentence and Answer "Yes" or "No" as the
label. P(p |X,Y,p )=P(R |X,Y,p )·P(p |R ) (2)
t t−1 t t−1 t t
# Prediction hereR t denotesthereflectionoftheLLMMatthet-thiter-
Sentence 1: {text1} ation.ItisnotedthatourPREFERonlymodifiestheinstruc-
Sentence 2: {text2} tion of the solving prompt, while other parts remain
Label:[] unchanged.
Close to our work, APO (Pryzant et al. 2023) also conductsafeedback-basedmechanismforpromptoptimization.

### Listing2:feedback prompt

Nevertheless,thereareseveralintrinsicdifferencesbetween

### I’m trying to write a Textual Entailment

such iterative prompting approach and our PREFER. First,
task prompt. My current prompt is: {prompt}
APOaimstosearchforasinglepromptcoveringthelargest
But this prompt gets the following examples
wrong: {error_info}
possible solution space, while our PREFER organizes a set
of prompts via ensemble learning, which works in tandem
Give {num_feedbacks} reasons why the prompt tocovermultiplesub-spaces.Second,ourPREFERproposes
could have gotten these examples wrong. Wrap aneffectivebaggingapproachtoreducethevarianceofthe
each reason with <START> and <END>. LLM, which is superior to the regular techniques such as
beam search or Monte Carlo search in APO. Experimental
resultsdemonstratethatourPREFERoutperformsAPObya
formation. Based on the error-ambiguity decomposition of quite large margin with less computational cost and higher
ensemble learning (Opitz and Shavlik 1995), the ensemble stability.
errormathematicallycontainstwoparts:
BilateralPromptBagging

## E =E¯−A¯ (1)

ensemble AsshowninEq.(1),thequalityandstabilityofweaklearnwhereE¯andA¯respectivelydenotetheaverageerrorandthe ers is essential to the ensemble performance. Due to the
averageambiguity(alsocalleddiversity)ofindividualweak generative property of language model, LLMs’ outputs are
learners.BasedonEq.(1),theensembleperformanceispos- highlysensitivetotheinputprompts,whichaffectsthestaitively correlated with both the accuracy and diversity of bility of both the feedback and weight calculation process.
weaklearners. Consideringthisrequirement, theprompt in Toalleviatethisissue,directsolutionsincludemajorityvoteachiterationissupposedtofocusonthehardexamplesthat ingorbeamsearch,whichiscommonlyusedinthecommuthepromptsinpreviousiterationscannothandle.Inspiredby nity(Wangetal.2022;Lietal.2023).However,thesemeththewayhumanreflectandrefineforimprovingperformance odsarecomputationallyintensive,especiallyforLLMswith
whentacklingdifficulttasks,weproposeafeedback-reflect- massiveparameters.Accordingly,toenhancetheabilityand
refine pipeline, asking the LLM to consider the relation of stabilityofeachpromptwithlimitedcalculationburden,we
promptsintheiteration,generatenewinformativeprompts, furtherproposeabaggingapproachcalledbilateralprompt
andoptimizethemjointly. bagging, which draws inspiration from human behavior of
Concretelyspeaking,wedefinetwotypesofprompttem- utilizing forward and backward thinking for tackling diffiplates,namelythesolving promptandthefeedback culttasks.
prompt, which are respectively responsible for solving Concretely speaking, humans commonly adopt the prodownstreamtasksandconductingthefeedbackprocess.Fol- cessofeliminationwhentheyarenotsureaboutthedecision
lowing In-Context Learning (ICL) (Dai et al. 2022), we making. Inspired by this, we advocate that similar spirits
format both types of prompts with the component of the canbeutilizedinthepromptbagging.Ineachiteration,the
instruction, demonstration and output format. Exemplary LLM M is required to evaluate its answer’s confidence by
cases of these two templates are illustrated in Listing 1 utilizing the generated prompt p followed by a confidence
t
andListing2,respectively.Giventheinitialseedpromptp evaluation clause. When the evaluation result is not confi-
0
and the corresponding performance, we build the feedback dent enough, the reverse thinking takes effect via conductpromptbasedonthefeedbacktemplateandthewrongexam- ingeliminationprocess.Indetail,weconsiderthequantitaples.Thisisreminiscentofthegradientindeeplearningop- tive confidence score evaluation in both forward and backtimization,whichindicatesthedirectionofmodeloptimiza- wardthinking.Taketheclassificationtaskasanexample,in
tion,thekeydifferenceliesthatthefeedbackformchanges theforwardevaluation,Misrequiredtomeasuretheconfifromnumericalintotextual.Thefeedbackpromptwillthen dencethateachcandidateansweristhecorrectone.Asfor
befedtotheLLMMforself-reflecting,andMprovidesa thebackwardevaluation,Misrequiredreverselytomeasure

<!-- Page 5 -->

Algorithm1:OurPREFERAlgorithm hereIistheidentifyfunction.Moreover,theweightineach
Input:TrainingdataD = (cid:83) {(x ,y )},theLLMM,the iterationisupdatedbasedontheaboveerrorinformationas:
tr i i i
s O e u ed tp p u r t o : m th p e t r p e 0 s , u t l h t e pr p o r m om pt p s t e t t e P mp = lat (cid:83) es { T p so } lv a i n ng d a th n e d ir T w fe e e i d g b h ac t k s λ(t) =log 1−error(t) +log (cid:0) |Y|−1 (cid:1) (5)
(cid:83) (cid:83) t t error(t)
{λ },thereflectionset {R }
t t t t Finally, the instance weights in training dataset D can be
tr
1: Set the initial data weight to ω i (0) = 1/|D tr |,∀i ∈ updatedby:
2: f { o 0 r ,· t · = ·, 0 |D to tr N |}, d P o ={p 0 }. ω i (t) =ω i (t−1)·exp (cid:16) λ(t)·I(cid:0) y i ̸=M(p t ,x i ) (cid:1)(cid:17) (6)
3: ift>0then
here ∀i ∈ {0,···,|D |} is the index of training exam-
4: Generatenewp t with{M,reflectionR t−1 } ples. Once the process tr of Algorithm 1 is complete, opti-
5: endif (cid:83) (cid:83)
mizedprompts {p }alongwiththeirweights {λ }can
6: Solvetargettaskswith{p t ,T solving ,ω i } be obtained, whic t h c t an then be utilized for applic t atio t n via
7: Conductbilateralbagging
weighted decision making. Moreover, the intermediate re-
8: Build feedback prompt with {error info, (cid:83)
flection {R }naturallyprovidesabundantinterpretability

### T } t t

feedback forpromptboosting.
9: PerformfeedbackandgetthereflectionR t
10: ComputeweightederrorasEq.(4)

### Experiments

11: Updatetheweightonp t byEq.(5)
12: Update the instance weights in D tr by Eq.(6) fol- ExperimentalSettings
lowedbyre-normalization Datasets Weconductexperimentsonawiderangeoftasks
13: P =P ∪p t ,R=R∪R t includingnaturallanguageinferenceandclassification:
14: endfor • NaturalLanguageInference
(cid:83) (cid:83) (cid:83)
15: return t {p t }, t {λ t }, t {R t } SNLI (Bowman et al. 2015), MNLI (Williams, Nangia,
and Bowman 2017), and RTE (Dagan, Glickman, and

### Magnini2005):textualentailmentinference;

the confidence that each candidate answer is excluded. For QNLI (Rajpurkaretal.2016):question-answeringinfernotationalsimplicity,wenametheconfidencescorescorre- ence.
spondingtotheforwardandbackwardevaluationswithS+
• NaturalLanguageClassification
and S− respectively. After these, the final probability can Ethos (Mollas et al. 2020): hate speech detection;
be calculated via combining S+ and S− with a subtractive Liar(Wang2017):fakenewsclassification;
fashion: ArSarcasm(FarhaandMagdy2020):ArabicsarcasmdeeS
j

## +−S

j
−
tection.
yˆ=argmax (3)
j(cid:80)K
c
eSc +−Sc −

### Compared Baselines To manifest the superiority of our

here yˆ denotes the predicted answer, c and j denote the PREFER approach, we compare it with several state-ofindexes of candidate answers. It is noted that LLMs tend the-art baselines. As the closest work to our proposal,
to evaluate confidence score overconfidently (Zhao et al. PromptBoosting (Hou et al. 2023) conducts the traditional
2021), while our proposal ingeniously circumvents this in- ADABOOSTalgorithmoverapre-definedpromptsetfortext
adequacy via positive and negative offsets. We believe that classification. As a remarkable work of iterative prompting
such paradigm can also shed light on the community of methods,APO(Pryzantetal.2023)utilizesaniterativeman-
LLMs’calibration(Zhaoetal.2023a). ner for optimizing a single prompt, where the performance
Attributedtotheintroductionofreversethinkingmecha- of the previous prompt will be used to form a natural lannism,theaccuracy-versus-efficiencydilemmacanbelargely guage“gradient”thatguidesthepromptoptimization.Morealleviatedforpromptbagging.Experimentalresultsexplic- over,wealsoconductsingle-promptandChain-of-Thought
itlymanifestthatsuchbilateralbaggingoutperformsregular (CoT)enhancedsingle-promptexperiments,tofigureoutthe
methods(e.g.,majorityvoting)inbotheffectivenessandef- superiorityofour PREFER comparedwithvanillaandoptificiency. mizednon-iterativepromptingworks.Lastly,wecomparea
variantofourPREFER,whichrewritessynonymousprompts

### OverallAlgorithm Tosumup,weconcludetheproposed

forboostinginsteadoffeedback-reflect-refineparadigm,for
PREFERinAlgorithm1.Basically,ourPREFERfollowsthe
ascertainingtheutilityofLLMs’reflectiveability.
pipeline of the classical ADABOOST (Freund and Schapire
1997) algorithm, while enhancing it with the feedback- Runningsettings Tomakeafaircomparison,weclosely
reflect-refine boosting and the bilateral prompt bagging. follow the experimental protocols that were set up in APO
Both branches can co-adapt and cooperate for automatic withourowndatasplit.Indetail,wemainlyconductdevelprompt set optimization. In detail, the weighted ensemble oping and evaluation of our PREFER in few-shot settings.
errorinthet-thiterationiscalculatedas: For each task, we randomly sample k examples from the
error(t) = | (cid:88) Dtr| ω i (t)·I(cid:0) y i ̸=M(p t ,x i ) (cid:1) (4) d o e ri f g a i u n l a t, l t t h ra e in k in in g t d h a i t s as p e a t p , e to ri b s u s i e ld tt k o -s 5 h 0 o . t W tr e ai u n s in e g F s 1 e - t s D co t r r e .B fo y r
(cid:80)|Dtr|ω performanceevaluation.
i=1 i i

<!-- Page 6 -->


### Datasets SNLI MNLI QNLI RTE Ethos Liar ArSarcasm


### SinglePrompt 0.587 0.660 0.660 0.720 0.833 0.535 0.511

SinglePrompt(CoT) 0.575 0.685 0.660 0.731 0.804 0.549 0.525
SynonymEnsemble 0.580 0.746 0.720 0.659 0.812 0.572 0.569
PromptBoosting 0.619 0.574 0.631 0.673 - - -

## Apo - - - - 0.964 0.663 0.873


## Apo* - - - - 0.947 0.658 0.639


### Ours 0.647 0.767 0.793 0.753 0.963 0.744 0.739

Table 1: Main experimental results of our PREFER and the compared approaches. APO and APO* respectively denote the
reportedandourreproducedresultsoftheAutomaticPromptOptimization(Pryzantetal.2023).Bold:best;underline:runnerup(resultsarebasedonourreproduction).
Method −Feedback −Bagging Voting Ours
0.96

## Snli 0.580↓ 0.640 0.626 0.647

0.94

## Mnli 0.746 0.713 0.733 0.767

0.92

## Qnli 0.720 0.747 0.767 0.793


## Rte 0.659↓ 0.740 0.760 0.753 0.90

Ethos 0.812↓ 0.947 0.938 0.963 0.88
Liar 0.572↓ 0.718 0.701 0.744
0.86
Sarcasm 0.572↓ 0.653↓ 0.649↓ 0.739
0.84
Table 2: Experimental results of the ablation study. ↓ indi- 0 1 2 3 4 5

### Optimization Step

catesasevereperformancedrop(morethan10%).

### ExperimentalResults


### InviewofthekeyproposalsinourPREFERapproach,weare

naturallymotivatedtoaskthefollowinginterestingresearch
questions.
• RQ1. Is the prompt ensemble learning really useful for
improvingLLMs’performance?
• RQ2. Are the feedback-driven boosting and bilateral
bagging mechanism both useful for prompt synthesis in
ensemblelearning?
• RQ3. Is the reason why our proposal is superior to the
iterative approaches due to the expansion of the sample
space?

### Tofigureouttheanswerstothesequestions,weconduct

sufficient experiments and the experimental results can be
found in Table 1. For the first question, we compare the
ensemble-basedapproaches(includingPromptBoostingand
our PREFER) with the single-prompt-based approaches. As
shown in the experimental results, when compared to the
vanilla(Line1)andCoT-enhancedsinglepromptapproach
(Line2),bothPromptBoostingandourPREFERoutperform
thembyasignificantmargin.Forexample,ourPREFERoutperforms the second best approach by up to 6.3% for the

### QNLI dataset, and 13.1% for the Liar dataset. The general

trend that becomes apparent from the results in Table 1 is
thatthemoredifficultthetaskis,thebetterensemblelearning performs. We conjecture that it is due to the feedbackreflect-refineparadigmcanachievegreaterimprovementfor
thehardertasks,whilethemarginalgainofthismechanism
would be diminishing for easier tasks. It is noted that the
experimentalresultschangemarginallybyaddingChain-of-
Thought(CoT)forsingle-promptapproach.

## 1F

Ours

## Apo

Figure3:TrainingprocesscomparisonforAPOandours.

### To explore the second research question, we compare

our PREFER with both the two-stage ensemble approach
PromptBoosting(Line4)andthesynonymrewritingensembleapproach(Line3).ForPromptBoosting,weusethepublicly available code of (Hou et al. 2023) and conduct experimentsfollowingitshyperparametersetting.Forthesynonymrewritingensemble,weconductpromptrewritingoperationwithsamesemantics,followedbyregularensemble
learningsimilartoourPREFER.AsdemonstratedinTable1,
ourapproachconsistentlyoutperformsthetwoensembleapproaches by a significant margin, reaching around 5% to
35%relativeimprovementinmostdatasets.Weattributethe
superiorityof PREFER toitsfeedback-reflect-refinemechanismaswellasthedesignofthejointoptimizationparadigm
thatnaturallycapturesrelationsamongweaklearners.

### As for the third question, APO (Pryzant et al. 2023) is

introduced as the remarkable approach of iterative prompting for comparison. It is noted that we reproduce the APO
approach (APO* at Line 6) for a strictly fair comparison,
whicheliminatestheinterferencefromdatasampling.Similar performance trends are observed in this comparison,
that is, our PREFER outperforms APO with the power of
feedback-reflect-refine boosting and bilateral prompt bagging. It manifests that through expanding the sample space
inanonlinearway,promptingperformancecanbeenhanced
significantly than single-prompt methods with similar iteration rounds. In fact, attributed to our bagging design, our
PREFER is superior to APO not only in effectiveness, but
alsoinstabilityandefficiency.

### AblationStudy

Tofigureouttheeffectivenessofeachcomponentinourproposal,weperformablationsonbothfeedback-reflect-refine

<!-- Page 7 -->


### APO Ours Synonymous Rewriting

Frequency b(N +2)+T|D | 2N +2 Decide whether sentence 2 answers the question asked by
sample sentence 1 when given two sentences.
T 579.0s 132.4s
step1
T 2100.4s 336.1s Initial prompt
step2

### Given two sentences, determine whether sentence 2 provides

Table 3: Comparison of training efficiency. Frequency de- an answer to the question posed by sentence 1.
notes the number of API accesses required by the method

### Reflection

within each optimization step, where N is training size
The prompt does not provide any guidance on how to handle
andb,T,|D |arehyperparametersrequiredbyAPO.
sample cases where the question posed by sentence 1 is vague
T andT representthetimerequiredforthecorre- or open-ended.
step1 step2 The prompt does not provide any guidance on how to handle
sponding optimization steps from the beginning, where we cases where sentence 1 and sentence 2 have different
setN =50,b=4,T =20,|D |=16. levels of specificity or granularity.
sample The prompt does not take into account the possibility of
implicit answers, where sentence 2 provides a
plausible inference or implication rather than an explicit
boostingandbilateralbagging,andtheexperimentalresults statement.
areprovidedinTable2.First,weremovethefeedbackmech-

### Refine

anisminpromptboosting(“−Feedback”),inwhichtheinitial seed prompt is just modified by the LLM without di- Assess whether sentence 2 provides supporting evidence or
contradictory information to the argument made in sentence
rected optimization, then the similar boosting and bagging 1, both implicitly and explicitly.
strategy is performed to align the settings of our PREFER.
Figure 4: Comparison of the generation obtained from our

### AsshowninTable2,itisobservedthatthepromptensemble

feedback-reflect-refineparadigmandsynonymousrewrite.
withoutfeedback-reflect-refinepathissub-optimal,signifying that such feedback mechanism plays an important role
for directed prompt boosting. Second, to figure out the ef- CaseStudy
fectivenessofourbilateralbaggingcomponent,wealsoturn
off the whole component (“−Bagging”) or replace it with To visualize our feedback-reflect-refine paradigm, we promajority voting (“Voting”), as shown in the column 3 and vided a case study as an illustration. As shown in Figure
4 in Table 2, respectively. The experimental results convey 4, taking the nature language inference task on the QNLI
thatourbilateralbaggingisbeneficialforPREFER,anddis- datasetasanexample,weprovidetheintermediateoutputof
tinctlyoutperformtheregularbaggingapproachofmajority the LLM in the feedback-reflect-refine process, to show its
voting.Notably,theperformanceofmajorityvotingisbasi- effectiveness and interpretability. Compared to the prompt
cally satisfactory, manifesting that the prompt bagging can generatedbysynonymousrewriting(graybox),theonegenbenefit the boosting prompt process consistently. An inter- eratedbyourmethodismoreinformativeandlogicallycomesting phenomenon is that removing the feedback-reflect- pensates for the deficiencies of the previous prompt, thus
refine module leads to more serious performance decline achievingdirectedpromptoptimization.
than removing the bagging module. This is expected, since
the bagging mainly benefits the stability for each prompt,

### Conclusion

whiletheboostingismoreimportantforpromptensemble.

### In this paper, we propose a simple, automatic, and uni-

TrainingEfficiency versal prompt ensemble approach called PREFER (PRompt

### Ensemble learning via Feedback-REflect-Refine), empiri-

To further demonstrate the superiority of our method, we cally showing consistent and significant improvement over
conductdetailedexperimentsontheEthosdatasetfortrain- previousbaselines.PREFERcontainstwomaincomponents,
ing efficiency, including training time and convergence includingfeedback-reflect-refinepromptboostingandbilatspeed. As shown in Figure 3, both APO and our PREFER eral prompt bagging. Prompt boosting branch directly and
reach the peak at optimization step 2 to 3, which indi- collectivelyoptimizespromptinanautomaticfashionbased
cates thatneither approaches requireextensive iterations to on the evolving self-reflection. Prompt bagging proposes a
achieveimpressiveresults.Clearly,ourPREFERhasamore bagging paradigm containing forward and backward coopstableperformanceretentioncomparedtoAPOduringsub- eration inspired by human behavior, which adequately unsequent iterations. On the other hand, considering the lim- earthstherealqualityofeachgeneratedpromptandthusenitations on the speed and frequency of LLM API accesses, suresthestabilityofboththefeedback-reflect-refineprocess
wecomparethenumberofAPIaccessesduringtrainingand and weight calculation in boosting. In a parallel note, our
thetimeconsumptionforthefirsttwopromptoptimization PREFER brings the prompt ensemble approach with more
steps,whichisdisplayedinTable3.Itcanbeobservedthat interpretability by harnessing the LLMs’ language ability.
the access number of APO increases rapidly during beam For future work, two interesting questions worth studying,
searchandbanditselection,whichbringsseriousefficiency namely 1) how to further reduce the calculation of prompt
problems.Onthecontrary,ourPREFERdoesnotenforceop- ensembletoapproachsingle-promptcolleagues,and2)how
timaloptimization ateachtimestep, butrathermaintains a tomakemoreclassicalalgorithmmoreintelligentbasedon
stableandefficientimprovementviaensemblelearning. thepowerofLLMs.

<!-- Page 8 -->

References Ouyang,L.;Wu,J.;Jiang,X.;Almeida,D.;Wainwright,C.;
Mishkin, P.; Zhang, C.; Agarwal, S.; Slama, K.; Ray, A.;
Bowman, S. R.; Angeli, G.; Potts, C.; and Manning, C. D.
etal.2022. Traininglanguagemodelstofollowinstructions

## Alargeannotatedcorpusforlearningnaturallanguage

withhumanfeedback. AdvancesinNeuralInformationProinference. arXivpreprintarXiv:1508.05326.
cessingSystems,35:27730–27744.
Dagan,I.;Glickman,O.;andMagnini,B.2005. Thepascal

### Pitis,S.;Zhang,M.R.;Wang,A.;andBa,J.2023. Boosted

recognisingtextualentailmentchallenge. InMachinelearn-
Prompt Ensembles for Large Language Models. arXiv
ingchallengesworkshop,177–190.Springer.
preprintarXiv:2304.05970.
Dai, D.; Sun, Y.; Dong, L.; Hao, Y.; Sui, Z.; and Wei, F.
Pryzant,R.;Iter,D.;Li,J.;Lee,Y.T.;Zhu,C.;andZeng,M.

## Why can gpt learn in-context? language models se-


## Automatic prompt optimization with” gradient decretly perform gradient descent as meta optimizers. arXiv

scent”andbeamsearch. arXivpreprintarXiv:2305.03495.
preprintarXiv:2212.10559.

### Qiao, S.; Ou, Y.; Zhang, N.; Chen, X.; Yao, Y.; Deng,

Farha, I. A.; and Magdy, W. 2020. From arabic sentiment

### S.; Tan, C.; Huang, F.; and Chen, H. 2022. Reasoning

analysistosarcasmdetection:Thearsarcasmdataset.InProwith language model prompting: A survey. arXiv preprint
ceedingsofthe4thWorkshoponOpen-SourceArabicCorarXiv:2212.09597.
poraandProcessingTools,withaSharedTaskonOffensive
LanguageDetection,32–39. Radford, A.; Wu, J.; Child, R.; Luan, D.; Amodei, D.;
Sutskever,I.;etal.2019.Languagemodelsareunsupervised
Freund,Y.;andSchapire,R.E.1997. Adecision-theoretic
multitasklearners. OpenAIblog,1(8):9.
generalization of on-line learning and an application to
Rajpurkar, P.; Zhang, J.; Lopyrev, K.; and Liang, P. 2016.
boosting. Journal of computer and system sciences, 55(1):
Squad: 100,000+ questions for machine comprehension of
119–139.
text. arXivpreprintarXiv:1606.05250.
Hou, B.; O’Connor, J.; Andreas, J.; Chang, S.; and Zhang,

### Wang, W. Y. 2017. ”liar, liar pants on fire”: A new


### Y.2023. Promptboosting:Black-boxtextclassificationwith

benchmark dataset for fake news detection. arXiv preprint
tenforwardpasses.InInternationalConferenceonMachine
arXiv:1705.00648.
Learning,13309–13324.PMLR.

### Wang,X.;Wei,J.;Schuurmans,D.;Le,Q.;Chi,E.;Narang,


### Hu,E.J.;Shen,Y.;Wallis,P.;Allen-Zhu,Z.;Li,Y.;Wang,

S.; Chowdhery, A.; and Zhou, D. 2022. Self-consistency

### S.;Wang,L.;andChen,W.2021.Lora:Low-rankadaptation

improves chain of thought reasoning in language models.
oflargelanguagemodels.arXivpreprintarXiv:2106.09685.
arXivpreprintarXiv:2203.11171.

### Ji,Z.;Lee,N.;Frieske,R.;Yu,T.;Su,D.;Xu,Y.;Ishii,E.;

Wei, J.; Tay, Y.; Bommasani, R.; Raffel, C.; Zoph, B.;
Bang,Y.J.;Madotto,A.;andFung,P.2023. Surveyofhal-

### Borgeaud,S.;Yogatama,D.;Bosma,M.;Zhou,D.;Metzler,

lucinationinnaturallanguagegeneration. ACMComputing
D.;etal.2022a. Emergentabilitiesoflargelanguagemod-
Surveys,55(12):1–38.
els. arXivpreprintarXiv:2206.07682.

### Li,Y.;Lin,Z.;Zhang,S.;Fu,Q.;Chen,B.;Lou,J.-G.;and

Wei, J.; Wang, X.; Schuurmans, D.; Bosma, M.; Xia, F.;

### Chen,W.2023.MakingLanguageModelsBetterReasoners

Chi, E.; Le, Q. V.; Zhou, D.; et al. 2022b. Chain-ofwith Step-Aware Verifier. In Proceedings of the 61st AnthoughtpromptingelicitsreasoninginlargelanguagemodnualMeetingoftheAssociationforComputationalLinguisels. Advances in Neural Information Processing Systems,
tics(Volume1:LongPapers),5315–5333.
35:24824–24837.
Liu,P.;Yuan,W.;Fu,J.;Jiang,Z.;Hayashi,H.;andNeubig,

### Williams, A.; Nangia, N.; and Bowman, S. R. 2017. A


### G.2023.Pre-train,prompt,andpredict:Asystematicsurvey

broad-coverage challenge corpus for sentence understandofpromptingmethodsinnaturallanguageprocessing. ACM
ingthroughinference. arXivpreprintarXiv:1704.05426.
ComputingSurveys,55(9):1–35.
Zelikman,E.;Mu,J.;Goodman,N.D.;andWu,Y.T.2022.

### Liu, X.; Zheng, Y.; Du, Z.; Ding, M.; Qian, Y.; Yang, Z.;

Star:Self-taughtreasonerbootstrappingreasoningwithreaand Tang, J. 2021. GPT understands, too. arXiv preprint
soning. arXivpreprintarXiv:2203.14465.
arXiv:2103.10385.

### Zhao,T.;Wei,M.;Preston,J.S.;andPoon,H.2023a. Auto-

Madaan, A.; Tandon, N.; Gupta, P.; Hallinan, S.; Gao, L.;
maticCalibrationandErrorCorrectionforLargeLanguage
Wiegreffe, S.; Alon, U.; Dziri, N.; Prabhumoye, S.; Yang,

### ModelsviaParetoOptimalSelf-Supervision. arXivpreprint

Y.; et al. 2023. Self-refine: Iterative refinement with selfarXiv:2306.16564.
feedback. arXivpreprintarXiv:2303.17651.
Zhao, W. X.; Zhou, K.; Li, J.; Tang, T.; Wang, X.; Hou,
Mollas,I.;Chrysopoulou,Z.;Karlos,S.;andTsoumakas,G.
Y.; Min, Y.; Zhang, B.; Zhang, J.; Dong, Z.; et al. 2023b.

## Ethos:anonlinehatespeechdetectiondataset. arXiv A survey of large language models. arXiv preprint

preprintarXiv:2006.08328.
arXiv:2303.18223.
OpenAI.2023. GPT-4TechnicalReport. TechnicalReport Zhao, Z.; Wallace, E.; Feng, S.; Klein, D.; and Singh, S.
arXiv:2303.08774,OpenAI. 2021. Calibrate before use: Improving few-shot perfor-
Opitz, D.; and Shavlik, J. 1995. Generating accurate and manceoflanguagemodels. InInternationalConferenceon
diverse members of a neural-network ensemble. Advances MachineLearning,12697–12706.PMLR.
inneuralinformationprocessingsystems,8.

## Tables

**Table (Page 6):**

| Ours 0.96 APO 0.94 0.92 1F 0.90 0.88 0.86 0.84 0 1 2 3 4 5 Optimization Step |  | Ours |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |
|  |  | APO |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
