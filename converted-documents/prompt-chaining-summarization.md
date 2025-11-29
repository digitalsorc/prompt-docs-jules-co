---
title: "Prompt Chaining Summarization"
original_file: "./Prompt_Chaining_Summarization.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["prompt-engineering", "llm", "rag", "evaluation", "dialogue"]
keywords: ["gpt", "prompt", "summary", "requirement", "stepwise", "article", "chaining", "critique", "refine", "draft"]
summary: "<!-- Page 1 -->

Prompt Chaining or Stepwise Prompt? Refinement in Text Summarization
ShichaoSun1,5,RuifengYuan1,ZiqiangCao4,WenjieLi1*,PengfeiLiu2,3,5*
1 TheHongKongPolytechnicUniversity,2 ShanghaiJiaoTongUniversity
3 ShanghaiArtificialIntelligenceLaboratory,4 SoochowUniversity
5 GenerativeAIResearchLab(GAIR)
cswjli@comp.polyu.edu.hk,pengfei@sjtu.edu.cn
Abstract etal.,2023;Akyureketal.,2023). Moreover,the
improvedoutcomescanalsohelptrainamorehelp-
Largelanguagemodels(LLMs)havedemonful and harml"
related_documents: []
---

# Prompt Chaining Summarization

<!-- Page 1 -->

Prompt Chaining or Stepwise Prompt? Refinement in Text Summarization
ShichaoSun1,5,RuifengYuan1,ZiqiangCao4,WenjieLi1*,PengfeiLiu2,3,5*
1 TheHongKongPolytechnicUniversity,2 ShanghaiJiaoTongUniversity
3 ShanghaiArtificialIntelligenceLaboratory,4 SoochowUniversity
5 GenerativeAIResearchLab(GAIR)
cswjli@comp.polyu.edu.hk,pengfei@sjtu.edu.cn
Abstract etal.,2023;Akyureketal.,2023). Moreover,the
improvedoutcomescanalsohelptrainamorehelp-
Largelanguagemodels(LLMs)havedemonful and harmless model (Huang et al., 2022; Bai
stratedthecapacitytoimprovesummaryqualetal.,2022;OpenAI,2023;Scheureretal.,2023).
itybymirroringahuman-likeiterativeprocess
Implementing this refinement process can be apof critique and refinement starting from the
initial draft. Two strategies are designed to proachedintwodistinctmethods: PromptChainperformthisiterativeprocess: PromptChain- ing1 and Stepwise Prompt.2 Prompt chaining uningandStepwisePrompt. Promptchainingor- dertakes drafting, critiquing, and refining phases
chestrates the drafting, critiquing, and refin- through a sequence of three discrete prompts. It
ing phases through a series of three discrete
meansthatLLMswillrunthreetimes. Although
prompts, while Stepwise prompt integrates
LLMs can concentrate on solving one particular
thesephaseswithinasingleprompt. However,
problemwithoutbeingoverwhelmedbythecomthe relative effectiveness of the two methods
plexityofthemultipletasks,itistrivialandtroublehas not been extensively studied. This paper
isdedicatedtoexaminingandcomparingthese someforhumanstoprovidethreecomprehensive
twomethodsinthecontextoftextsummariza- prompts. Conversely,stepwisepromptcompletes
tion to ascertain which method stands out as thesethreephaseswithinasinglegeneration. Stepthemosteffective. Experimentalresultsshow wise prompt only needs a simple prompt to conthatthepromptchainingmethodcanproduce
tain three sequential steps, but it is challenging
amorefavorableoutcome. ThismightbebeforLLMstogeneratealongandcomplexoutput.
causestepwisepromptmightproduceasimu-

### Currently,theeffectivenessofthesetwomethods

latedrefinementprocessaccordingtoourvariousexperiments. Sincerefinementisadaptable remainsunderexploredinanytextgenerationtask.
todiversetasks,ourconclusionshavethepo- In this short paper, we compare prompt chaintentialtobeextrapolatedtootherapplications, ingandstepwiseprompttofindthebettermethod
therebyofferinginsightsthatmaycontributeto
forrefinementintextsummarization. Specifically,
thebroaderdevelopmentofLLMs.
weconductexperimentsonthedatasetInstruSum
1 Introduction (Liuetal.,2023)introducedtoevaluatethecapabilitiesofLLMs. Itinvolvesinstructioncontrollable
Large language models (LLMs) can enhance the textsummarization,whichsummarizesthearticle
summary via iterative refinement (Zhang et al., basedonthespecificrequirement. Weevaluatethe
2023). This is motivated by how humans refine qualityofinitialsummaries,critiques,refinedsumtheir written text. The main idea contains three mariestoshowtheeffectofpromptchainingand
sequentialsteps: (1)Drafting: LLMsgeneratean stepwiseprompt. Experimentalresultsindicatethat
initial summary; (2) Critiquing: LLMs provide thepromptchainingisbetterthanstepwiseprompt.
critical feedback and helpful suggestions for its Moreover,variousexperimentsimplythatstepwise
output; (3) Refining: LLMs use the feedback to promptmightproduceasimulatedrefinement
refinetheinitialsummary.

### Moregenerally,thisrefinementcanbeapplied

1Prompt chaining is introduced in https://www.
tovarioustextgenerationtaskstoimprovetheout- promptingguide.ai/techniques/prompt_chaining
comes(Madaanetal.,2023;Gouetal.,2023;Ye 2Stepwise prompt is similar to specifying the steps
required to complete a task at https://platform.
* CorrespondingAuthors. openai.com/docs/guides/prompt-engineering/
WorkdonewhilevisitingGAIRLab. tactic-specify-the-steps-required-to-complete-a-task
4202
nuJ
1
]LC.sc[
1v70500.6042:viXra

<!-- Page 2 -->

process,whereLLMsintentionallyproduceerrors 4 ExperimentsandResults
onlytosubsequentlycorrectthem. Intuitively,this
conclusionwillworkonotherdomainsandfurther 4.1 Dataset
facilitatefutureresearch.

### WeconductexperimentsonthedatasetInstruSum

(Liu et al., 2023), which is produced to evaluate
thecapabilitiesofLLMstosummarizethearticle
2 RelatedWorks
basedonthespecificrequirement. InstruSumcontains 100 article-requirement pairs in total. The
Recentworkhasprovedthatrefinementcansignif- articles contain around 1000-1200 words, stemicantly improve LLMs performance. Self-Refine mingfromtheBBCnewswebsite.3 Requirements
(Madaanetal.,2023)usesLLMsfordraftingout- for a summary are designed to reflect diverse incomes, providing feedback, and refining initial formationneedsthatreadersmayhaveatdifferent
generation. In a series of 7 varied tasks, ranging stagesoftheirreadingjourney. Theserequirements
from dialogue response to mathematical reason- include(a)Informationalrequirement,whichsuping,outputscreatedusingtheSelf-Refinemethod plies pertinent details about the topic or subject
arefavoredoverthoseproducedthroughone-step beingdiscussedwithinthearticles;(b)Formatting
generation with the same LLM, as judged by hu- requirement,whichenhancesthesummary’sstrucmanevaluatorsandautomatedmetrics. Critic(Gou ture,suchasincorporatingbulletlists,toimprove
etal.,2023)proposestoleverageexternaltoolsto its readability and facilitate quicker comprehencritiquegeneratedtextandrefinetheinitialgener- sion;(c)Metarequirement,whichreflectsahighation via evaluation feedback. SelFee (Ye et al., leveloverviewofthearticle.
2023)collectsgenerations,feedback,andrevised
generationstofinetuneLLaMAmodels(Touvron 5 ModelsandMetrics
etal.,2023). Akyureketal.(2023)proposetotrain
Refinement can be powered by various LLMs.
a better critique model to help repair the model

### In this paper, we choose the newest versions

outputs. Zhangetal.(2023)introducearefinement
of GPT-3.5 (gpt-3.5-turbo-0125) and GPT-4
paradigmtoenhancethefaithfulnessandcontrolla-
(gpt-4-0125-preview)modelsfromOpenAI4 to
bilityintextsummarization. Moreover,therefined
draft,critique,andrefinetheoutcomesduetotheir
outcomes can also help train a more helpful and
stronginstruction-followingcapabilities. Wealso
harmless model (Huang et al., 2022; Bai et al.,
explore the performance of a strong open-source
2022;OpenAI,2023;Scheureretal.,2023).
LLM(Mixtral8×7B(Jiangetal.,2024)).

### WeusetheLLMCompareasourevaluationpro-

3 Prompts tocol,whichcomparestwocandidateoutputsand
then selects the better one (Zheng et al., 2023;

### Wangetal.,2023). ThisisbecauseLLMCompare

Figure 1 illustrates the prompts of prompt chaincoupledwithGPT-4isthebestevaluationprotocol,
ingandstepwisepromptwithinthecontextofinasmentionedinLiuetal.(2023). Theevaluation
structioncontrollabletextsummarization. Prompt
promptsareshowninAppendixA.
chaining requires a human to segment the refine-

### Weevaluatethegeneratedsummariesfromthe

mentprocessintothreesteps. Eachstepleverages
threequalitydimensionsasintroducedinLiuetal.
the output from the preceding one. In contrast,
(2023): (1) Overall Quality measures the overstepwisepromptspecifiesthesamethreestepsto
allexcellenceofthesummaryfollowingthesumbeexecutedwithinasingleoperation. Therefore,
maryrequirements. (2)MissingInformationasthey can generate the equivalent results, includsesseswhetherthesummaryomitsanyessentialaring: (1)DraftSummaryistheinitiallygenerated
ticledetailspertinenttothesummaryrequirements.
summary. (2) Critique is the critical comment
(3)IrrelevantInformationexamineswhetherthe
andthehelpfulsuggestion. (3)RefinedSummary
summarycontainsextraneousinformationthatfalls
stems from refining the draft summary based on
outsidethescopeofthesummaryrequirements.
thecritique. Correspondingly,theseoutcomesare
obtainedfromeachstepinpromptchainingorthe 3https://www.bbc.com/news
sequentialitemsinthepromptchainingoutcome. 4https://platform.openai.com/docs/models

<!-- Page 3 -->


### Step 1: Drafting Step 1: Generating

You are a helpful assistant designed to output JSON.
You are a helpful assistant designed to output JSON.
Your task is to summarize the article based on the specific requirement.
Your task is to summarize the article based on the
The output is json format as follows:
specific requirement.
{ "summary": "the generated summary" } To complete this task, you should generate the
<article> content step by step as follows:
{article}
Step 1: draft your summary for the article based on
<requirement>
the specific requirement.
{requirement}
Step 2: critique your summary to provide the critical
comments and helpful suggestions.
Step 2: Critiquing Step 3: refine your summary to address all issues in
the critique and ensure that all suggestions from the
You are a helpful assistant designed to output JSON. critique are incorporated.
Your task is to provide the critical comments and helpful suggestions for the The output is json format as follows:
summary, which summarizes the article based on the specific requirement. {
The output is json format as follows: "summary": "the generated summary"，
{ "critique": "the generated critique for the summary" } "critique": "the generated critique for the summary",
<article> "refinement": "the refined summary"
{article} }
<requirement>
{requirement} <article>
<summary> {article}
{summary}
<requirement>

### Step 3: Refining {requirement}

You are a helpful assistant designed to output JSON.
Your task is to refine the summary based on the critique, where the
summary summarizes the article based on the specific requirement.
You should address all issues in the critique and ensure that all suggestions
from the critique are incorporated.

### The output is json format as follows:

{ "refinement": "the refined summary" }
<article>
{article}
Prompt Chaining
<requirement>
{requirement}
<summary> Stepwise Prompt
{summary}
Figure1: PromptChainingv.s. StepwisePrompt.
5.1 ExpI:SummarizationBenchmark ingandstepwiseprompt?
Setup Consistentwiththesettingsemployedin Promptchainingachievesthehighestwintimes
previousresearchonautomaticLLMbenchmark- (77outof100),considerablyoutshiningstepwise
ing(Duboisetal.,2023;Zhengetal.,2023),weuse prompt in producing higher-quality summaries.
GPT-4(gpt-4-0125-preview)one-stepoutcomes Moreover,promptchainingcoupledwithabetter
asthebaseline. Weassesstheperformanceofvar- backbonemodelcanleadtobetterperformanceby
iousmethodsthroughdirectcomparisonwiththe comparingtheoutcomesofGPT3.5andGPT-4.
baseline GPT-4 results. To mitigate the potential Q2: How does prompt chaining or stepwise
positional bias, the summary pairs are randomly promptaffecttheinitialoutcome?
shuffled before the evaluation. We perform the Notably,summariesinitiallydraftedusingstep-
LLMComparepromptsviagpt-4-0125-preview. wisepromptfrequentlyfallshortinquality. This
maybeduetotheanticipationthatitsoutputswill
Results Table 1 shows the automatic benchsubsequentlyundergocritiqueandrefinement,pomarking results. More win times or less lose
tentiallyinfluencingtheinitialdraftingprocess.
times mean a stronger performance. Generally, the draft summary is enhanced via refine-
5.2 ExpII:Robustness
ment, regardless of the methods used. Notably,
the performance of gpt-3.5-stepwise-refine Setup Basedontheunderstandingthatdifferent
(and Mixtral-stepwise-refine) is compara- modelsusedforLLMCompareevaluationcanyield
ble to that of gpt-3.5-chaining-draft (and varied results as indicated by Liu et al. (2023),
Mixtral-stepwise-draft). Itindicatesthatstep- we employ two iterations of the GPT-4 model,
wisepromptmightleadtoasimulatedrefinement gpt-4-1106-previewandgpt-4-0125-preview,
process in which LLMs intentionally produce er- tovalidatethestabilityandrobustnessofprompt
rorsonlytosubsequentlycorrectthem. chaining’s superiority over stepwise prompt. We
Q1: Whichisthebettermethodofpromptchain- do not use the GPT-3.5 models for powering

<!-- Page 4 -->

Overall Missing Irrelevant

### Models


### Win Tie Lose Win Tie Lose Win Tie Lose Length


### Mixtral-stepwise-draft 12 29 59 13 35 52 8 33 59 111.19


### Mixtral-chaining-draft 18 27 55 19 41 40 11 46 43 119.63

Mixtral-stepwise-refine 19 25 56 20 30 50 11 29 60 124.35
Mixtral-chaining-refine 27 21 52 31 29 40 14 48 38 127.3
gpt-3.5-stepwise-draft 10 14 76 8 30 62 5 37 58 86.58
gpt-3.5-chaining-draft 12 22 66 13 28 59 7 37 56 94.76
gpt-3.5-stepwise-refine 12 13 75 14 17 69 2 27 71 85.79
gpt-3.5-chaining-refine 21 17 62 14 24 62 11 38 51 97.24
gpt-4-stepwise-draft 34 40 26 27 53 20 16 60 24 125.73
gpt-4-stepwise-refine 53 29 18 42 49 9 12 57 31 145.85
gpt-4-chaining-refine 77 14 9 57 38 5 19 39 42 174.35
Table1: Automaticbenchmarkingresults. Thesummariesofdifferentmethodsarecomparedagainstsummaries
generatedbyGPT-4(gpt-4-0125-preview)one-stepgeneration(i.e.,gpt-4-chaining-draft)usingtheLLM-
Compareprotocol(Liuetal.,2023). Theaveragelengthofbaselinesummariesis113.03.

### Wins Tie Loses stepwiseprompt?

Weobservethatpromptchainingbeatsstepwise
gpt-4-1106 29 61 10
prompt in both Overall and Missing evaluation
gpt-4-0125 49 31 20
across different evaluation models. Meanwhile,
average 39 46 15 promptchainingexhibitscomparableperformance
0 25% 50% 75% 100% tostepwisepromptinIrrelevant. Itcanconfirmthe
reliabilityofourconclusionthatpromptchaining
(a)Overall
stablyoutperformsstepwiseprompt.
gpt-4-1106 21 74 5
6 ExpIII:HumanEvaluation
gpt-4-0125 29 61 10
average 25 67.5 7.5 Setup Weengagedtwopostgraduatestudentsto
0 25% 50% 75% 100% conducthumanevaluation,whereintheycompared
(b)Missing therefinedoutcomesofPromptChainingagainst
thoseoftheStepwisePrompt. IfPromptChaining
gpt-4-1106 15 67 18 outperforms Stepwise Prompt, it is notated as a
gpt-4-0125 22 57 21 “Win”. For this human evaluation, we randomly
average 18.5 62 19.5 selected30%datafromInstruSumdataset. Similar
totheautomatedevaluation,wealsouse“overall”,
0 25% 50% 75% 100%
“missing”,“irrelevant”astheevaluationmetrics.
(c)Irrelevant
Results Table2presentsthequalityofcritique.
Figure2:Winratesofrefinedresultsfrompromptchain-

### A higher score means a better performance. The

ing over stepwise prompt. The left-hand models are
usedtoevaluatetherefinedoutcome. “win”timessignificantlyexceedthe“los”times. It
indicates that prompt chaining outperforms stepwise prompt. This conclusion is consistent with

### LLMCompare evaluations due to their observed

GPT-4automatedevaluation. Additionally,weoblowerconsistencywithhumanevaluators. Lastly,
serve that there are fewer “lose” times when we
averagereportsthemeanvalueofthetwoscores.
applythemoreadvancedmodel,GPT-4. ItmayimplythatPromptChainingsignificantlyoutperforms
Results Figure 2 shows the win rates between
StepwisePromptwhenusingadvancedmodels.
promptchainingandstepwisepromptthroughrefinedresults. ThehigherwinratesofOverallsug-
7 ExpIV:CritiqueEvaluation
gestthatpromptchainingmoreeffectivelyadheres
totheestablishedsummaryrequirements. Setup WeuseMETACRITIQUE(Sunetal.,2024)
Q3: Does prompt chaining stably outperform poweredbygpt-4-0613toevaluatethequalityof

<!-- Page 5 -->

Overall Missing Irrelevant

### Models

Win Tie Lose Win Tie Lose Win Tie Lose
GPT 3.5 16 5 9 15 7 8 6 20 4

### Gpt 4 14 8 8 13 10 7 9 14 7


### Mixtral 11 16 3 7 22 1 6 19 5

Table2: Humanevaluationresults.
critiques, which are the intermediate outputs of Acknowledgements
promptchainingandstepwiseprompt. METACRI-

### Wethanktheanonymousreviewersfortheirvalu-


### TIQUEinvolvesthreemetrics: (1)Precisiongauges

ablefeedbackandhelpfulsuggestions. Thisproject
thefactualityofthecritique;(2)Recallmeasures
issupportedbyResearchGrantsCouncilofHong
thecomprehensivenessofthecritique;(3)F1Score

### Kong (PolyU/15203617 and PolyU/5210919),

harmonizestheprecisionscoreandrecallscore. We
National Natural Science Foundation of China
donotassessGPT-4critiques,asMETACRITIQUE
(62076212 and 62106165), Qingyuan Research
usesGPT-4outcomesasreferences.
ProjectandShanghaiArtificialIntelligenceLaboratory.
Results Table3presentsthequalityofcritique.
Ahigherscoremeansabetterperformance.

### Limitations


### Q4: How does prompt chaining or stepwise

promptaffectthecritiquegeneration? Refinementcanbeappliedtovariousnaturallan-
Stepwisepromptcangeneratehigh-qualitycri- guage processing (NLP) tasks. However, this patiques that are both more factual and comprehen- peronlycomparespromptchainingandstepwise
sive. However,intermsofF1score,promptchain- promptinthescopeoftextsummarization. Future
ingachievesonlyhalfofthatofstepwiseprompt, researchiswarrantedtovalidatetheeffectiveness
despite the superior performance in refined sum- ofthesestrategiesonanexpansiverangeofNLP
maries. Theseresultsimplythatstepwiseprompt tasks,therebyenhancingthegeneralizabilityofour
producesasimulatedrefinementprocess. findingsandtheirpotentialutilityacrossthefield.
EthicalConsiderations
MetaCritique

### Models

Precision Recall F1Score Our experimental data stems from InstruSum,
which is well-established and publicly available.
gpt-3.5-stepwise 78.91 43.29 52.48
gpt-3.5-chaining 40.21 25.62 24.79 Datasetconstructionandannotationareconsistent
withtheintellectualpropertyandprivacyrightsof
Table3: METACRITIQUEscores. theoriginalauthors. Thisworkcomplieswiththe
ACLEthicsPolicy5.
8 Conclusion

### References


### LLMs can enhance summaries by emulating the


### AfraFeyzaAkyurek, EkinAkyurek, AshwinKalyan,

human-like process of critique and refinement of PeterClark,DerryTantiWijaya,andNiketTandon.
theirinitialdrafts. Thispaperexplorestwodistinct 2023. RL4F:Generatingnaturallanguagefeedback
strategies for implementing this process: Prompt withreinforcementlearningforrepairingmodeloutputs. InProceedingsofthe61stAnnualMeetingof
ChainingandStepwisePrompt. WeconductrigortheAssociationforComputationalLinguistics(Volousexperimentsinthecontextoftextsummariza- ume 1: Long Papers), pages 7716–7733, Toronto,
tion. Our findings indicate that prompt chaining Canada.AssociationforComputationalLinguistics.
garners a superior performance. Besides, the re-

### Yuntao Bai, Saurav Kadavath, Sandipan Kundu,

sults imply that stepwise prompt might produce

### Amanda Askell, Jackson Kernion, Andy Jones,

a simulated refinement process. Given that such Anna Chen, Anna Goldie, Azalia Mirhoseini,
refinement can be adapted to various tasks, our Cameron McKinnon, et al. 2022. Constitutional
insightscouldextendbeyondtextsummarization,
5https://www.aclweb.org/portal/content/
potentiallyadvancingtheprogressofLLMs. acl-code-ethics

<!-- Page 6 -->

ai: Harmlessnessfromaifeedback. arXivpreprint SeonghyeonYe,YongraeJo,DoyoungKim,Sungdong
arXiv:2212.08073. Kim, Hyeonbin Hwang, and Minjoon Seo. 2023.

### Selfee: Iterativeself-revisingllmempoweredbyself-

YannDubois,XuechenLi,RohanTaori,TianyiZhang, feedbackgeneration. Blogpost.

### IshaanGulrajani,JimmyBa,CarlosGuestrin,Percy

Liang, and Tatsunori B Hashimoto. 2023. Al- Haopeng Zhang, Xiao Liu, and Jiawei Zhang. 2023.
pacafarm: A simulation framework for methods SummIt: IterativetextsummarizationviaChatGPT.
that learn from human feedback. arXiv preprint In Findings of the Association for Computational
arXiv:2305.14387. Linguistics: EMNLP2023,pages10644–10657,Singapore.AssociationforComputationalLinguistics.

### Zhibin Gou, Zhihong Shao, Yeyun Gong, Yelong

Shen, Yujiu Yang, Nan Duan, and Weizhu Chen. LianminZheng,Wei-LinChiang,YingSheng,Siyuan

## Critic: Largelanguagemodelscanself-correct Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin,

with tool-interactive critiquing. arXiv preprint Zhuohan Li, Dacheng Li, Eric Xing, et al. 2023.
arXiv:2305.11738. Judging llm-as-a-judge with mt-bench and chatbot
arena. arXivpreprintarXiv:2306.05685.
JiaxinHuang,ShixiangShaneGu,LeHou,YuexinWu,
XuezhiWang,HongkunYu,andJiaweiHan.2022.

### A Prompts

Large language models can self-improve. arXiv
preprintarXiv:2210.11610.

### WeelaborateonthepromptsforGPT-4evaluation

Albert Q Jiang, Alexandre Sablayrolles, Antoine inTable4,5and6forLLMCompareOverall,LLM-
Roux,ArthurMensch,BlancheSavary,ChrisBam- CompareMissing,andLLMComapreIrrelevant.
ford,DevendraSinghChaplot,DiegodelasCasas,
Emma Bou Hanna, Florian Bressand, et al. 2024.
Mixtralofexperts. arXivpreprintarXiv:2401.04088.
Yixin Liu, Alexander R Fabbri, Jiawen Chen, Yilun

### Zhao, Simeng Han, Shafiq Joty, Pengfei Liu,

DragomirRadev,Chien-ShengWu,andArmanCohan. 2023. Benchmarking generation and evaluation capabilities of large language models for instructioncontrollablesummarization. arXivpreprint
arXiv:2311.09184.

### AmanMadaan, NiketTandon,PrakharGupta,Skyler

Hallinan, Luyu Gao, Sarah Wiegreffe, Uri Alon,

### Nouha Dziri, Shrimai Prabhumoye, Yiming Yang,

et al. 2023. Self-refine: Iterative refinement with
self-feedback. arXivpreprintarXiv:2303.17651.
OpenAI. 2023. Gpt-4 technical report. ArXiv,
abs/2303.08774.

### JérémyScheurer,JonAnderCampos,TomaszKorbak,


### Jun Shern Chan, Angelica Chen, Kyunghyun Cho,

and Ethan Perez. 2023. Training language modelswithlanguagefeedbackatscale. arXivpreprint
arXiv:2303.16755.

### ShichaoSun,JunlongLi,WeizheYuan,RuifengYuan,

Wenjie Li, and Pengfei Liu. 2024. The critique of
critique. arXivpreprintarXiv:2401.04518.
Hugo Touvron, Louis Martin, Kevin Stone, Peter Albert, Amjad Almahairi, Yasmine Babaei, Nikolay

### Bashlykov,SoumyaBatra,PrajjwalBhargava,Shruti

Bhosale, et al. 2023. Llama 2: Open foundation and fine-tuned chat models. arXiv preprint
arXiv:2307.09288.
Yidong Wang, Zhuohao Yu, Zhengran Zeng, Linyi

### Yang, Cunxiang Wang, Hao Chen, Chaoya Jiang,

Rui Xie, Jindong Wang, Xing Xie, et al. 2023.

### Pandalm: An automatic evaluation benchmark for

llminstructiontuningoptimization. arXivpreprint
arXiv:2306.05087.

<!-- Page 7 -->


## ————–Systemmessage————-

YouareahelpfulassistantdesignedtooutputJSON.
Inthistask,youwillbeprovidedwithanewsarticle,aspecificsummaryrequirement,andtwosummaries.Thesummariesarecraftedtomeetaspecificsummary
requirement.Notethattheremaybeidenticalsummaries.
Yourtaskistocomparetheoverallqualityofthesetwosummariesconcerningthesummaryrequirementandpicktheonethatisbetter(therecanbeatie).
Firstyouwillgiveanexplanationofyourdecisionthenyouwillprovideyourdecisionintheformatof1or2ortie.
Pleaserefertotheexamplebelowfortheformatofyourresponse.
ExampleResponse:
{
"explanation":"Yourexplanationhere",
"decision":"1or2ortie",
}

## ————–Usermessage————-

<article>
{article}
<requirement>
{requirement}
<summary1>
{summary1}
<summary2>
{summary2}
Table4: PromptforLLMCompareOverall.

## ————–Systemmessage————-

YouareahelpfulassistantdesignedtooutputJSON.
Inthistask,youwillbeprovidedwithanewsarticle,aspecificsummaryrequirement,andtwosummaries.Thesummariesarecraftedtomeetaspecificsummary
requirement.Notethattheremaybeidenticalsummaries.
Yourtaskistocomparethequalityofthesetwosummariesconcerningwhethertheyomitanycrucialinformationfromthearticlewithrespecttothesummary
requirementandpicktheonethatisbetter(therecanbeatie).Crucialinformationreferstokeydetailsorfactsthatareessentialtounderstandingthearticleand
meetingthesummaryrequirement.
Firstyouwillgiveanexplanationofyourdecisionthenyouwillprovideyourdecisionintheformatof1or2ortie.
Pleaserefertotheexamplebelowfortheformatofyourresponse.
ExampleResponse:
{
"explanation":"Yourexplanationhere",
"decision":"1or2ortie",
}

## ————–Usermessage————-

<article>
{article}
<requirement>
{requirement}
<summary1>
{summary1}
<summary2>
{summary2}
Table5: PromptforLLMCompareMissing.

<!-- Page 8 -->


## ————–Systemmessage————-

YouareahelpfulassistantdesignedtooutputJSON.
Inthistask,youwillbeprovidedwithanewsarticle,aspecificsummaryrequirement,andtwosummaries.Thesummariesarecraftedtomeetaspecificsummary
requirement.Notethattheremaybeidenticalsummaries.
Yourtaskistocomparethequalityofthesetwosummariesconcerningwhethertheyincludeanyinformationthatisnotrelevanttothesummaryrequirementandpick
theonethatisbetter(therecanbeatie).Firstyouwillgiveanexplanationofyourdecisionthenyouwillprovideyourdecisionintheformatof1or2ortie.
Pleaserefertotheexamplebelowfortheformatofyourresponse.
ExampleResponse:
{
"explanation":"Yourexplanationhere",
"decision":"1or2ortie",
}

## ————–Usermessage————-

<article>
{article}
<requirement>
{requirement}
<summary1>
{summary1}
<summary2>
{summary2}
Table6: PromptforLLMCompareIrrelevant.

## Tables

**Table (Page 3):**

|  |
|---|
| Step 1: Drafting |


**Table (Page 3):**

| Step 2: Critiquing |
|---|
|  |


**Table (Page 4):**

| 25 | 67.5 |  |  | 7.5 |
|---|---|---|---|---|
|  |  |  |  |  |


**Table (Page 4):**

| 18.5 | 62 |  |  |  | 19.5 |
|---|---|---|---|---|---|
|  |  |  |  |  |  |
