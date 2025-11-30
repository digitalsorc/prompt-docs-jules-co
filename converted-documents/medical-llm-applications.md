---
title: "Medical LLM Applications"
original_file: "./Medical_LLM_Applications.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["prompt-engineering", "llm", "rag", "chain-of-thought", "agents"]
keywords: ["text", "generated", "llm", "abs", "detection", "llms", "human", "page", "detectors", "corr"]
summary: "<!-- Page 1 -->

A Survey on LLM-Generated Text Detection:
Necessity, Methods, and Future Directions

### JunchaoWu ShuYang

NLP2CTLab,FacultyofScienceand NLP2CTLab,FacultyofScienceand

### Technology Technology

InstituteofCollaborativeInnovation InstituteofCollaborativeInnovation

### UniversityofMacau UniversityofMacau

nlp2ct.junchao@gmail.com nlp2ct.shuyang@gmail.com

### RunzheZhan YulinYuan∗

NLP2CTLab,FacultyofScienceand DepartmentofChineseLanguageand

### Technology Literature,Facultyof"
related_documents: []
---

# Medical LLM Applications

<!-- Page 1 -->

A Survey on LLM-Generated Text Detection:
Necessity, Methods, and Future Directions

### JunchaoWu ShuYang

NLP2CTLab,FacultyofScienceand NLP2CTLab,FacultyofScienceand

### Technology Technology

InstituteofCollaborativeInnovation InstituteofCollaborativeInnovation

### UniversityofMacau UniversityofMacau

nlp2ct.junchao@gmail.com nlp2ct.shuyang@gmail.com

### RunzheZhan YulinYuan∗

NLP2CTLab,FacultyofScienceand DepartmentofChineseLanguageand

### Technology Literature,FacultyofArtsand

InstituteofCollaborativeInnovation Humanties

### UniversityofMacau UniversityofMacau

nlp2ct.runzhe@gmail.com yulinyuan@um.edu.mo
DepartmentofChineseLanguageand
Literature,FacultyofHumanities

### PekingUniversity

yuanyl@pku.edu.cn

### DerekFaiWong∗ LidiaSamChao

NLP2CTLab,FacultyofScienceand NLP2CTLab,FacultyofScienceand

### Technology Technology

InstituteofCollaborativeInnovation StateKeyLaboratoryofInternetof
UniversityofMacau ThingsforSmartCity
derekfw@um.edu.mo UniversityofMacau
lidiasc@um.edu.mo
Thepowerfulabilitytounderstand,follow,andgeneratecomplexlanguageemergingfrom
large language models (LLMs) makes LLM-generated text flood many areas of our daily
lives at an incredible speed and is widely accepted by humans. As LLMs continue to expand,
there is an imperative need to develop detectors that can detect LLM-generated text. This is
crucial to mitigate potential misuse of LLMs and safeguard realms like artistic expression and
social networks from harmful influence of LLM-generated content. The LLM-generated text
detection aims to discern if a piece of text was produced by an LLM, which is essentially
a binary classification task. The detector techniques have witnessed notable advancements recently,propelledbyinnovationsinwatermarkingtechniques,statistics-baseddetectors,neuralbase detectors, and human-assisted methods. In this survey, we collate recent research breakthroughs in this area and underscore the pressing need to bolster detector research. We also
∗ YulinYuanandDerekFaiWongareco-corespondingauthors.
Preprint.
4202
rpA
91
]LC.sc[
3v42741.0132:viXra

<!-- Page 2 -->

delve into prevalent datasets, elucidating their limitations and developmental requirements.
Furthermore, we analyze various LLM-generated text detection paradigms, shedding light on
challenges like out-of-distribution problems, potential attacks, real-world data issues and the
lack of effective evaluation framework. Conclusively, we highlight interesting directions for
future research in LLM-generated text detection to advance the implementation of responsible
artificial intelligence (AI). Our aim with this survey is to provide a clear and comprehensive
introduction for newcomers while also offering seasoned researchers a valuable update in the
field of LLM-generated text detection. The useful resources are publicly available at: https:
//github.com/NLP2CT/LLM-generated-Text-Detection.

## Introduction

With the rapid development of LLMs, the text generation capabilities of LLMs have
reachedalevelcomparabletohumanwriting(OpenAI2023;Anthropic2023;Chowdhery et al. 2022b). LLMs have permeated various aspects of daily life and play a vital
role become pivotal in many professional workflows (Veselovsky, Ribeiro, and West
2023), facilitating tasks such as advertising slogan creation (Murakami, Hoshino, and
Zhang2023),newscomposition(Yanagietal.2020),storygeneration(Yuanetal.2022),
and code generation (Becker et al. 2023; Zheng et al. 2023). A recent research from
HanleyandDurumeric(2023)indicatesthattherelativequantityofAI-generatednews
articles on mainstream websites has risen by 55.4%, whereas on websites known for
disseminatingmisinformation,ithasrisenby457%fromJanuary1,2022,toMay1,2023.
Furthermore,theirimpactsignificantlyshapestheprogressionofnumeroussectorsand
disciplines, including education (Susnjak 2022), law (Cui et al. 2023), biology (Piccolo
etal.2023),andmedicine(Thirunavukarasuetal.2023).
The powerful generation capabilities of LLMs have rendered it challenging for
individuals to discern between LLM-generated and human-written texts, resulting
in the emergence of intricate concerns. The concerns regarding LLM-generated text
originate from two perspectives. Firstly, LLMs are susceptible to fabrications (Ji et al.
2023), reliance on outdated information, and heightened sensitivity to prompts. These
vulnerabilitiescanfacilitatethespreadoferroneousknowledge(Christian2023),underminetechnicalexpertise(Rodriguezetal.2022a;AlimanandKester2021),andpromote
plagiarism (Lee et al. 2023a). Secondly, there exists the risk of malicious exploitation
of LLMs in activities such as disinformation dissemination (Pagnoni, Graciarena, and
Tsvetkov 2022a; Lin, Hilton, and Evans 2022), online fraudulent schemes (Weidinger
et al. 2021; Ayoobi, Shahriar, and Mukherjee 2023), social media spam production
(Mirskyetal.2022),andacademicdishonesty,especiallywithstudentsemployingLLMs
foressaywriting(Stokel-Walker2022;Kasnecietal.2023).Concurrently,LLMsincreasinglyshoulderthedatagenerationresponsibilityinAIresearch,leadingtotherecursive
use of LLM-generated text in their own training and assessment. A recent analysis,
titled Model Autophagy Disorder (MAD) (Alemohammad et al. 2023), raised alarms
overthisAIdatafeedbackloop.Asgenerativemodelsundergoiterativeimprovements,
LLM-generated text may gradually replace the need for human-curated training data.
This could potentially lead to a reduction in the quality and diversity of subsequent
models. In essence, the consequences of LLM-generated text encompass both societal
(Cardenuto et al. 2023) and academic (Yu et al. 2023a) risks, and the use of LLM-
generateddatawillhinderthefuturedevelopmentofLLMsanddetectiontechnology.
However,fortheLLM-generatedtextdetectiontask,currentdetectiontechnologies,
includingthediscriminatorycapabilities (PriceandSakellarios2023)ofcommercialde-
2

<!-- Page 3 -->


### Wuetal. ASurveyonLLM-GeneratedTextDetection

tectorsareunreliable.Theyareprimarilybiasedtowardsclassifyingoutputsashumanwrittentext,ratherthandetectingtextgeneratedbyLLMs(Walters2023;Weber-Wulff
et al. 2023; Weber-Wulff et al. 2023). Detection methods that rely on human are also
unreliable and have very low accuracy, even only slightly better than random classification(Uchenduetal.2021;Douetal.2022;Clarketal.2021a;SoniandWade2023a,b).
Furthermore,theabilityofhumanstoidentifyLLM-generatedtextisoftenlowerthan
that of detectors or detection algorithms in various environmental settings (Ippolito
et al. 2020; Soni and Wade 2023b). Thus, there is an imperative demand for robust
detectors to identify LLM-generated text effectively. Establishing such mechanisms is
pivotaltomitigatingLLMmisuserisksandfosteringresponsibleAIgovernanceinthe
LLM era (Stokel-Walker and Van Noorden 2023; Porsdam Mann et al. 2023; Shevlane
etal.2023).
ResearchonthedetectionofLLM-generatedtexthasreceivedlotsofattentioneven
beforetheadventofChatGPT,especiallyinareassuchasearlyidentificationofdeepfake
text (Pu et al. 2023a), machine-generated text detection (Jawahar, Abdul-Mageed, and
Lakshmanan2020)andauthorshipattribution(Uchendu,Le,andLee2023a).Typically,
thisproblemwasregardedasaclassificationtask,discerningbetweenLLM-generated
text and human-written text (Jawahar, Abdul-Mageed, and Lakshmanan 2020). Back
to this research stage, the detection task was predominantly focusing on translationgenerated texts and utilizing simple statistical methods. The introduction of ChatGPT
has sparked a significant surge in interest surrounding LLMs, heralding a paradigm
shiftintheresearchlandscape.InresponsetotheescalatingchallengesposedbyLLM-
generatedtext,theNLPcommunityhasintenselypursuedsolutions,delvingintoLLM-
generatedtextdetectionandrelatedattackingmethodologies.WhileCrothers,Japkowicz,andViktor(2023a);Tang,Chuang,andHu(2023)recentlypresentedreviewsonthis
topic, we argue that its depth of detection methods is insufficient (We discuss related
workindetailinsubsection3.1).
In this article, we furnish a meticulous and profound review of contemporary
researchonLLM-generatedtextdetection,aimingtoguideresearchersthroughthechallenges and prospective research trajectories. We investigate the latest breakthroughs,
beginning with an introduction to the task of LLM-generated text detection, the underlyingmechanismsoftextgenerationbyLLMs,andthesourcesofLLM’senhanced
textgenerationcapabilities.WealsoshedlightonthecontextsandimperativesofLLM-
generatedtextdetection.Furthermore,wespotlightpopulardatasetsandbenchmarks
forthetask,exposingtheircurrentdeficienciestostimulatethecreationofmorerefined
dataresources.Ourdiscussionextendstothelatestdetectorstudies.Inadditiontothe
traditionalneural-basedmethodsandstatistical-basedmethods,wealsoreportwatermarking techniques, and human-assisted methods. A subsequent analysis pinpoints
research limitations in LLM-generated text detectors, highlighting critical areas like
out-of-distributionchallenges,potentialattacks,real-worlddataissues,andthelackof
effectiveevaluationframework.Conclusively,weponderuponpotentialdirectionsfor
futureresearch,aimingtohelpthedevelopmentofefficientdetectors.

## Background

2.1LLM-generatedTextDetectionTask
Detecting LLM-generated text is an intricate challenge. Generally speaking, humans
struggle to discern between LLM-generated text and human-written text (Uchendu
et al. 2021; Dou et al. 2022; Clark et al. 2021a; Soni and Wade 2023a,b), and their
3

<!-- Page 4 -->

Generating Task Human Writing

### Human ?

Questions

### Text from

Writing Topics unknown sources
Detectors
LLMs ?
…
LLMs Generating

### Figure1

ToypictureofLLM-generatedtextdetectiontask.Thistaskisabinaryclassificationtaskthat
detectswhethertheprovidedtextisgeneratedbyLLMsorwrittenbyhumans.
capabilitytodistinguishsuchtextsexceedsrandomclassificationonlyslightly.Table1
offers some examples where LLM-generated text often is extremely close to humanwrittentextandcanbedifficulttodistinguish.WhenLLMsgeneratefabricateddetails,
discerningtheiroriginsandveracityremainsequallychallenging.

### Table1

Examplesofhuman-writtentextandLLM-generatedtext.TextgeneratedbyLLMsduring
normaloperationandinstancesinwhichtheyfabricatefactsoftenexhibitnointuitively
discernibledifferences.WhenLLMseitherabstainfromprovidingananswerorcraftneutral
responses,certainindicators,suchastheexplicitstatement“IamanAIlanguagemodel”,may
facilitatehumanadjudication,butsuchexamplesareless.

### Type Question Human-written LLMs-generated

Naturallanguageprocessing(NLP)is Naturallanguageprocessing(NLP)is
Normal Explain what is aninterdisciplinarysubfieldoflinguis- afieldofcomputerscience,artificialin-
NLP? tics,computerscience,andartificialin- telligence,andlinguisticsthatfocuses
telligence... on...
Today’s Special is a Canadian chil- I’m sorry, but I am an AI language
Refusal Howistodayspe- dren’s television show produced by modelanddonothaveaccesstocurcial? CliveVanderBurghatTVOntariofrom rentdatesorevents.Isthereanything
1981to1987. elseIcanhelpyouwith...

### NLPisamultidisciplinaryfieldatthe

In“Naturallanguageprocessing:state intersection of computer science, lin-

### Explain what is

of the art, current trends and chal- guistics,andai,asdescribedinarecent
Fabricated NLPbasedonone lenges”,NLPissummarizedasadis- peer-reviewedpublicationtitled"Natpublication in the
cipline that uses various algorithms, ural Language Processing: A Comrecentliterature.
toolsandmethodsto... prehensiveOverviewandRecentAdvances"(2023)...
Recent studies (Guo et al. 2023; Ma, Liu, and Yi 2023; Muñoz-Ortiz, Gómez-
Rodríguez,andVilares2023;Giorgietal.2023;SealsandShalin2023)havehighlighted
significant disparities between human-written and LLM-generated text, such as Chat-
GPT. The differences between LLM-generated text and human-written text are not
merely within the scope of individual word choice (Seals and Shalin 2023), but also
manifest in stylistic dimensions, such as syntactical simplicity, use of passive voice,
and narrativity. Notably, LLM-generated text often exhibits qualities of enhanced organization,logicalstructure,formality,andobjectivityincomparisontohuman-written
4

<!-- Page 5 -->


### Wuetal. ASurveyonLLM-GeneratedTextDetection

text. Additionally, LLMs frequently produce extensive and comprehensive responses,
characterized by a lower prevalence of bias and harmful content. Nevertheless, they
occasionallyintroducenonsensicalorfabricateddetails.Linguistically,LLM-generated
text tends to be about twice the length of human-written text but exhibits a more limitedvocabulary.LLMsexhibitahigherfrequencyofnoun,verb,determiner,adjective,
auxiliary,coordinatingconjunction,andparticlewordcategoriescomparedtohumans,
and less adverb and punctuation, incorporating more deterministic, conjunctive, and
auxiliary structures in their syntax. Additionally, LLM-generated text often conveys
lessemotionalintensityandexhibitsclearerpresentationthanhumanwritings,aphenomenon possibly linked to an inherent positive bias in LLMs (Giorgi, Ungar, and
Schwartz 2021; Markowitz, Hancock, and Bailenson 2023; Mitrovic, Andreoletti, and
Ayoub2023).Althoughthereareslightlydifferentstatisticalgapsondifferentdatasets,it
isclearthatthedifferencebetweenLLM-generatedtextandhuman-writtentextclearly
exists, because the statistical results of the difference in language features and human
visual perception are consistent. Chakraborty et al. (2023b) have further substantiated
the view by reporting on the detectability of text generated by LLMs, including the
high-performance models such as GPT-3.5-Turbo and GPT-4 (Helm, Priebe, and Yang
2023),whileChakrabortyetal.(2023a)introducedanAIDetectabilityIndextofurther
rankmodelsaccordingtotheirdetectability.
In this survey, we begin by providing definitions for human-written text, LLM-
generatedtext,andthedetectiontask.
Human-written Text. is characterized as the text crafted by individuals to express
thoughts, emotions, and viewpoints. This encompasses articles, poems, and reviews,
amongothers,typicallyreflectingpersonalknowledge,culturalmilieu,andemotional
disposition,spanningtheentiretyofthehumanexperience.
LLM-generatedText.isdefinedascohesive,grammaticallysound,andpertinentcontent
generatedbyLLMs.ThesemodelsaretrainedextensivelyonNLPtechniques,utilizing
large datasets and machine learning methodologies. The quality and fidelity of the
generatedtexttypicallydependonthescaleofthemodelandthediversityoftraining
data.
LLM-generatedTextDetectionTask.isconceptualizedasabinaryclassificationtask,aimingtoascertainifagiventextisgeneratedbyanLLM.Theformalrepresentationofthis
taskisgivenbythesubsequentequation:

1 ifxgeneratedbyLLMs

### D(x)= (1)

0 ifxwrittenbyhuman
whereD(x)representsthedetector,andxisthetexttobedetected.
2.2LLMsTextGenerationandConfusionSources
2.2.1 Generation Mechanisms of LLMs. The text generation mechanism of LLMs operates by sequentially predicting subsequent tokens. Rather than producing an entire
paragraph instantaneously, LLMs methodically construct text one word at a time.
Specifically,LLMsdecodesubsequenttokensinatextualsequence,takingintoaccount
5

<!-- Page 6 -->

both the input sequence and previously decoded tokens. Assume that the total time
step is T, the current time step is t, the input text or tokenised sequence is: X =

## T

{x ,x ,...x },andthepreviousoutputsequenceisY ={y ,y ,...y }.Atthispoint,
1 2 T t−1 1 2 t−1
theoutputnextwordy canbeexpressedas:
t
y ∼P(y |Y ,X )=softmax(w ·h ) (2)
t t t−1 T o t
h is the hidden state of the model at time step t, w is the output matrix, the softmax
t o
function is used to obtain the probability distribution of the vocabulary, and y is
t
sampled from the probability distribution of the vocabulary P(y |Y ,X ). The joint
t t−1 T
probabilityfunctionforthefinaloutputsequencecanbemodeledandrepresentedas:
Y ={y ,y ,...,y } (3)

## T 1 2 T

Thequalityofthedecodedtextisintrinsicallytiedtothechosendecodingstrategy.
Given that the model constructs text sequentially, the quality of generated text hinges
onthemethodusedtoselectthesubsequentwordfromthevocabulary,thatis,howy
t
issampledfromtheprobabilitydistributionofvocabulary.Thepredominantdecoding
techniquesencompassgreedysearch,beamsearch,top-ksampling,andtop-psampling.
Table 2 offers a comparison of the underlying principles, along with the respective
meritsanddrawbacks,ofthesedecodingmethods.Thiscomparisonaidsinelucidating
the text generation process of LLMs and the specific characteristics of the text they
produce.

### Table2

Thecoreideasofdifferenttextdecodingstrategies,aswellastheiradvantagesand
disadvantages.GreedySearchusesasimplegreedystrategy,consideringonlythecurrent
highestprobabilitytokenateachstep,whichissimpleandfastbutlacksdiversity.BeamSearch
allowsformultiplecandidatestobeconsidered,whichimprovesthequalityofthetextbuttends
togenerateduplicates.Top-KSamplingincreasesdiversitybuthasdifficultycontrollingthe
qualityofgeneration.Top-PSamplingreliesontheshapeoftheprobabilitydistributionto
determinethesetoftokenstosample,whichiscoherent,butdiversityiscorrelatedwiththe
parameterP.

### Strategy CoreIdea Advantages Drawbacks

GreedySearch Onlythetokenwiththehighest Fastandsimple. Easytofallintolocaloptimality,
currentprobabilityisconsidered lackofdiversity,unabletodeal
ateachstep. withuncertainty.
Beam Search Severalmorecandidatescanbe Improvement of text Tendtogeneraterepetitivefrag-
(Graves2012) consideredateachstep. qualityandflexibility. ments,workpoorlyinopengenerationdomains,unabletohandleuncertainty.
Top-K Sampling Samples among the K most Increase diversity and Difficulty in controlling the
(Fan,Lewis,and likelywordsateachstep. beabletodealwithun- quality of generation, which
Dauphin2018) certainty. mayresultinincoherenttext.
Top-P Sampling Usetheshapeoftheprobability Coherenceandtheabil- Dependentonthequalityofthe
(Holtzmanetal. distributiontodeterminetheset ity to deal with uncer- model predictions, diversity is
2020) oftokenstobesampledfrom tainty. relatedtotheparameterP.
6

<!-- Page 7 -->


### Wuetal. ASurveyonLLM-GeneratedTextDetection

2.2.2 Sources of LLMs’ Strong Generation Capabilities. The burgeoning growth in
model size, data volume, and computational capacity has significantly enhanced the
capabilities of LLMs. Beyond a specific model size, certain abilities manifest that are
notpredictablebyscalinglaws.Theseabilities,absentinsmallermodelsbutevidentin
LLMs,aretermed“EmergentAbilities”ofLLMs.
In-Context Learning (ICL). The origins of ICL capabilities remain a topic of ongoing
debate (Dai et al. 2023). However, this capability introduces a paradigm where model
parametersremainunchanged,andonlythedesignofthepromptismodifiedtoelicit
desired outputs from LLMs. This concept was first introduced in the GPT-3 (Brown
et al. 2020). Brown et al. (2020) posited that the presence of ICL is fundamental for
the swift adaptability of LLMs across a diverse set of tasks. With just a few examples,
LLMs can effectively tackle downstream tasks, obviating the previous BERT modelbased approach that relied on pretraining followed by fine-tuning for specific tasks
(Raffeletal.2020).
AlignmentofHumanPreference.AlthoughLLMscanbeguidedtogeneratecontentusing
carefullydesignedprompts,theresultingtextmightlackcontrol,potentiallyleadingto
thecreationofmisleadingorbiasedcontent(Zhangetal.2023b).Theprimaryconcern
of these models lies in predicting subsequent words to form coherent sentences based
onvastcorpora,ratherthanensuringthatthecontentgeneratedisbothbeneficialand
innocuous to humans. To address these shortcomings, OpenAI introduced the Reinforcement Learning from Human Feedback (RLHF) approach, as detailed in (Ouyang
etal.2022)and(Lambertetal.2022).Thisapproachbeginsbyfine-tuningLLMsusing
datafromuser-directedquizzesandsubsequentlyevaluatingthemodel’soutputswith
human assessors. Simultaneously, a reward function is established, and the LLM is
further refined using the Proximal Policy Optimization (PPO) algorithm (Schulman
et al. 2017a). The end result is a model that aligns with human values, understands
humaninstructions,andgenuinelyassistsusers.
Complex Reasoning Capabilities. While LLMs’ ICL and alignment capability facilitate
meaningful interactions and assistance, their performance tends to degrade in tasks
demanding logical reasoning and heightened complexity. Wei et al. (2022) observed
thatencouragingLLMstoproducemoreintermediatestepsthroughaChainofThought
(CoT)canenhancetheireffectiveness.TreeofThoughts(ToT)(Yaoetal.2023)andGraph
ofThoughts(GoT)(Bestaetal.2023)areextensionsofthismethodology.Bothstrategies
augment LLM performance on intricate tasks by amplifying the computational effort
requiredforthemodeltodeduceananswer.
2.3WhyDoWeNeedtoDetectTextGeneratedbyLLMs?
As LLMs undergo iterative refinements and reinforcement learning through human
feedback, their outputs become increasingly harmonized with human values and
preferences. This alignment facilitates broader acceptance and integration of LLM-
generated text into everyday life. The emergence of various AI tools has played a
significant role in fostering intuitive human-AI interactions and democratizing access
totheadvancedcapabilitiesofpreviouslyesotericmodels.Frominteractiveweb-based
7

<!-- Page 8 -->

assistants like ChatGPT,1 to search engines enhanced with LLM technology like the
contemporary version of Bing,2 to specialized tools like Coplit,3 and Scispeace4 that
assistprofessionalsincodegenerationandscientificresearch,LLMshavesubtlywoven
intothedigitalfabricofourlives,propagatingtheircontentacrossdiverseplatforms.
However, it is important to acknowledge that for the majority of users, LLMs
and their applications are still considered black-box AI systems. For individual users,
this often serves as a benign efficiency boost, sidestepping laborious retrieval, and
summarization. However, within specific contexts and against the backdrop of the
broader digital landscape, it becomes crucial to discern, filter, or even exclude LLM-
generatedtext.Itisimportanttoemphasizethatnotallsituationscallforthedetection
ofLLM-generatedtext.Unnecessarydetectioncanleadtoconsequencessuchassystem
inefficienciesandinflateddevelopmentcosts.Generally,detectingLLM-generatedtext
mightbesuperfluouswhen:
• TheutilizationofLLMsposesminimalrisk,especiallywhentheyhandle
routine,replicabletasks.
• ThespreadofLLM-generatedtextisconfinedtopredictable,limited
domains,likeclosedinformationcircleswithfewparticipants.
Drawingupontheliteraturereviewedinthisstudy,therationalebehinddetecting
LLM-generated text can be elucidated from multiple vantage points, as illustrated in
Figure2.Thedelineatedperspectivesare,inpart,informedbytheinsightspresentedin
(Gadeetal.2020)and(SaeedandOmlin2023).
Whilethelistprovidedabovemaynotbeexhaustiveandsomefacetsmayintersect
orfurtherdelineateasLLMsandAIsystemsmature,wepositthatthesepointsunderscoretheparamountreasonsforthenecessityofdetectingtextgeneratedbyLLMs.
Regulation. As AI tools, often characterized as black boxs, the inclusion of LLM-
generated text in creative endeavorsraises significant legal issues. A pressing concern
is the eligibility of LLM-generated texts for intellectual property rights protection, a
subject still mired in debate (Epstein et al. 2023; Wikipedia 2023), although the EU AI
Act5 hasbeguntocontinuouslyimprovetoregulatetheuseofAI.Themainchallenges
arise from issues such as ownership of the training data used by the AI in generating
output and how to determine how much human involvement is enough to make
the work theirs. The prerequisite for copyright protection for AI supervision and AI-
generatedcontentisthathumancreativityinthematerialsusedtotrainAIsystemscan
be distinguished, so as to further promote the implementation of more complete legal
supervision.
Users. LLM-generated text, refined through various alignment methods, is progressively aligning with human preferences. This content permeates numerous useraccessible platforms, including blogs and Questions & Answers (Q&A) forums. However, excessive reliance on such content can undermine user trust in AI systems and,
1 https://chat.openai.com/
2 https://www.bing.com/
3 https://github.com/features/copilot/
4 https://typeset.io/
5 https://artificialintelligenceact.eu/the-act/
8

<!-- Page 9 -->

Wuetal. ASurveyonLLM-GeneratedTextDetection

### Regulation

e.g., making Ai regulation

### Users Science

e.g., trustworthiness e.g., academic integrity
LLM-generated Text

### Detection


### Development of LLMs Human Society

e.g., data administration e.g., informativeness

### Figure2

ThemostcriticalreasonswhyLLM-generatedtextdetectionisneededurgently.Wediscussedit
fromfiveperspectives:Regulation,Users,Developments,Science,andHumanSociety.
byextension,digitalcontentasawhole.Inthiscontext,theroleofLLM-generatedtext
detectionbecomescrucialasagatekeepertoregulatetheprevalenceofLLM-generated
textonline.
Developments. With the evolving prowess of LLMs, Li et al. (2023b) suggested that
LLMscanself-assessandevenbenchmarktheirownperformances.Duetoitsexcellent
text generation performance, LLMs are also used to construct many training data sets
through preset instructions (Taori et al. 2023). However, Alemohammad et al. (2023)
positedthatthis“Self-Consuming”paradigmmayengenderahomogenizationinLLM-
generatedtexts,potentiallyculminatinginwhatistermedas“LLMAutophagyDisorder” (MAD). If LLMs heavily rely on web-sourced data for training, and a significant
portion of this data originates from LLM outputs, it could hinder their long-term
progress.
Science. The relentless march of human progress owes much to the spirit of scientific
exploration and discovery. However, the increasing presence of LLM-generated text
in academic writing (Májovsky` et al. 2023) and the use of LLM-originated designs
in research endeavors raise concerns about potentially diluting human ingenuity and
exploratorydrive.Atthesametime,itcouldalsounderminetheabilityofhighereducation to validate student knowledge and comprehension, and diminish the academic
reputation of specific higher education institutions (Ibrahim et al. 2023). Although
current methodologies may have limitations, further enhancements in detection capabilitieswillstrengthenacademicintegrityandpreservehumanindependentthinkingin
scientificresearch.
9

<!-- Page 10 -->

Human Society. From a societal perspective, analyzing the implications of LLM-
generatedtextrevealsthatthesemodelsessentiallymimicspecifictextualpatternswhile
predicting subsequent tokens. If used improperly, these models have the potential to
diminishlinguisticdiversityandcontributetotheformationofinformationsiloswithin
societaldiscourse.Inthelongrun,detectingandfilteringLLM-generatedtextiscrucial
forpreservingtherichnessanddiversityofhumancommunication,bothlinguistically
andinformatively.

## RelatedWorksandOurInvestigation

3.1RelatedWorks
The comprehensive review article by Beresneva (2016) represents the first extensive
survey of methods for detecting computer-generated text. At that time, the detection
process was relatively simple, mainly focusing on machine translation text detection
and employing simple statistical methods for detection. The emergence of autoregressivemodelshassignificantlyincreasedthecomplexityoftextdetectiontasks.Jawahar,
Abdul-Mageed, and Lakshmanan (2020) provide a detailed survey on the detection
of machine-generated text, establishing a foundational context for the field with an
emphasis on the SOTA generative models prevalent at the time, such as GPT-2. The
subsequent release of ChatGPT sparked a surge of interest in LLMs, and signified a
major shift in research directions. In response to the rapid challenges posed by LLM-
generated text, the NLP community has recently embarked on extensive research to
devise robust detection mechanisms and explore the dynamics of detector evasion
techniques,aimingtoseekeffectivesolutions.TherecentsurveybyCrothers,Japkowicz, and Viktor (2023b); Dhaini, Poelman, and Erdogan (2023) provide new reviews of
LLM-generated text detection, but we contend that these reviews are not advanced
enough and the summary of detection methods needs to be improved. Tang, Chuang,
and Hu (2023) present another survey, categorizing detection methods into black-box
detectionandwhite-boxdetection,andhighlightingcutting-edgetechnologiessuchas
watermarking, but the review could benefit from a more comprehensive analysis and
critical evaluation. Ghosal et al. (2023) discuss the current attacks and defenses of AI-
generated text detectors and provide a thorough inductive analysis. Nevertheless, the
discussioncouldbeenrichedwithamoredetailedexaminationoftaskmotivation,data
resources,andevaluationmethodologies.
Inthisarticle,westrivetoprovideamorecomprehensiveandinsightfulreviewof
thelatestresearchonLLM-generatedtextdetection,enrichedwiththoughtfulanalysis.

### Wehighlightthestrengthsofourreviewincomparisontoothers:

• SystematicandComprehensiveReview:Oursurveyoffersanextensive
explorationofLLM-generatedtextdetection,coveringthetask’s
descriptionandunderlyingmotivation,benchmarksanddatasets,various
detectionandattackmethods,evaluationframeworks,themostpressing
challengesfacedtoday,potentialfuturedirections,andacritical
examinationofeachaspect.
• In-depthAnalysisofDetectionMechanisms:Weprovideadetailed
overviewofdetectionstrategies,fromtraditionalapproachestothelatest
10

<!-- Page 11 -->


### Wuetal. ASurveyonLLM-GeneratedTextDetection

research,andsystematicallyevaluatetheireffectiveness,strengths,and
weaknessesinthecurrentenvironmentofLLMs.
• MorePragmaticInsights.Ourdiscussiondelvesintoresearchquestions
withpracticalimplications,suchashowmodelsizeaffectsdetection
capabilities,thechallengesofidentifyingtextthatisnotpurelygenerated
byLLMs,andthelackofeffectiveevaluationframework.
Insummary,wefirmlybelievethatthisreviewismoresystematicandcomprehensive than existing works. More importantly, our critical discussion not only provides
guidancetonewresearchersbutalsoimpartsvaluableinsightsintoestablishedworks
withinthefield.
3.2SystematicInvestigationandImplementation

### Table3

Overviewofthediversedatabasesandsearchenginesutilizedinourresearch,alongwiththe
incorporatedsearchschemesandtheconsequentresultsobtained.GoogleScholarpredominates
asthesearchengineyieldingthemaximumnumberofretrievabledocuments.Uponmeticulous
examination,itisobservedthatasubstantialportionofthedocumentsoriginatefromArXiv,
primarilysharedbyresearchers.

### Databases SearchEngine SearchScheme Retrieved

GoogleScholar https://scholar.google.com/ FullText 210

### ArXiv https://arxiv.org/ FullText N/Aa

Scopus https://www.scopus.com/ TITLE-ABS-KEY: ( Title, Ab- 133
stract, Author Keywords, IndexedKeywords)
WebofScience https://www.webofscience.com/ Topic:(SearchesTitle,Abstract, 92
Author Keywords, Keywords

### Plus)


### IEEEXplore https://ieeexplore.ieee.org/ FullText 49

SpringerLink https://link.springer.com/ FullText N/Aa
ACLAnthology https://aclanthology.org/ FullText N/Aa

### ACMDigitalLibrary https://dl.acm.org/ Title N/Ab

a Search engines cannot use all keywords in a single search string. Therefore the retrieved results are
inaccurateandtheremaybeduplicateresultsofthesisqueries.
bThesearchengineretrievedaninaccuratenumberofpapersthatwereweaklyrelatedtoourtopic.
Our survey employed the System for Literature Review (SLR) as delineated by
Barbara Kitchenham (2007), a methodological framework designed for evaluating
the extent and quality of extant evidence pertaining to a specified research question
or topic. Offering a more expansive and accurate insight compared to conventional
literaturereviews,thisapproachhasbeenprominentlyutilizedinnumerousscholarly
11

<!-- Page 12 -->

60
40
20
0
2019 2020 2021 2022 2023

### Year

snoitacilbupforebmuN

### Figure3

Thedistributionbyyearofthelast5yearsofliteratureobtainedfromthescreeningisplotted.
Thenumberofpublishedarticlesobtainsignificantattentionin2023.
surveys, as evidenced by Murtaza et al. (2020); Saeed and Omlin (2023). The research
questionsguidingourSLRwereasfollows:
WhataretheprevailingmethodsfordetectingLLM-generatedtext,andwhatarethe
mainchallengesassociatedwiththesemethods?
Upon delineating the research problems, our study utilized search terms directly
related to the research issue, specifically: “LLM-generated text detection”, “machinegenerated text detection”, “AI-written text detection”, “authorship attribution”, and
“deepfaketextdetection”.ThesetermswerestrategicallycombinedusingtheBoolean
operatorORtoformulatethefollowingsearchstring:(“LLM-generatedtextdetection”
OR“machine-generatedtextdetection”OR“AI-writtentextdetection”OR“authorship
attribution”OR“deepfaketextdetection”).Subsequently,employingthissearchstring,
we engaged in a preliminary search through pertinent and authoritative electronic
dissertationdatabasesandsearchengines.OurinvestigationmainlyfocusedonscholarlyarticlesthatwerepubliclyaccessiblepriortoNovember2023.Table3outlinesthe
sourcesusedandprovidesanoverviewofourresults.
Subsequently,weestablishedtheensuingcriteriatoscrutinizetheamassedarticles:
• Thearticleshouldbeareviewfocusingonthemethodsandchallenges
pertinenttoLLM-generated(machine-generated/AI-written)text
detection.
• Thearticleshouldproposeamethodologyspecificallydesignedforthe
detectionofLLM-generated(machine-generated/AI-written)text.
• Thearticleshoulddelineatechallengesandprospectivedirectionsfor
futureresearchinthedomainoftextgenerationforLLMs.
12

<!-- Page 13 -->


### Wuetal. ASurveyonLLM-GeneratedTextDetection

• Thearticleshouldarticulatethenecessityandapplicationsof
LLM-generatedtextdetection.
If any one of the aforementioned four criteria was met, the respective work was
deemed valuable for our study. Following a process of de-duplication and manual
screening,weidentified83pertinentpiecesofliterature.Thedistributiontrendofthese
works, delineated by year, is illustrated in Figure 3. Notably, the majority of relevant
researchonLLM-generatedtextdetectionwaspublishedintheyear2023(asshownin
Figure3),underscoringthevibrantdevelopmentwithinthisfieldandhighlightingthe
significance of our study. In subsequent sections, we provide a synthesis and analysis
of the data (see section 4), primary detectors (see section 5), evaluation metrics (see
section6),issues(seesection7),andfutureresearchdirections(seesection8)pertinent
toLLM-generatedtextdetection.Thecomprehensivestructureofthesurveyisoutlined
inTable4,offeringadetailedoverviewoftheorganizationofourreview.

### Table4

Summaryofcontentorganisationofthissurvey.

### Section Topic Content

Section4 Data Datasets and Benchmarks for LLM-generated Text Detection,
OtherDatasetsEasilyExtendedtoDetectionTasksandChallenge
ofdatsetsforLLM-generatedTextDetection.
Section5 Detectors Watermarking Technology, Statistics-Based Detectors, Neural-

### BasedDetectors,andHuman-AssistedMethods

Section6 EvaluationMetrics Accuracy, Precision, Recall, False Positive Rate, True Negative
Rate, False Negative Rate, F1-Score, and Area under the ROC
curve(AUROC).
Section7 Issues Out of Distribution Challenges, Potential Attacks, Real-world
Data Issues, Impact of Model Size on Detectors, and Lack of

### EffectiveEvaluationFramework

Section8 FutureDirections BuildingRobustDetectorswithAttacks,EnhancingtheEfficacy
ofZero-ShotDetectors,OptimizingDetectorsforLow-resource

### Environments, Detection for Not purely LLM-generated Text,

ConstructingDetectorsAmidstDataAmbiguity,DevelopingEffective Evaluation Framework Aligned With Real-World, and
Constructing Detectors with Misinformatio Discrimination Capabilities.
Section9 Conclusion -

## Data

High-qualitydatasetsarepivotalforadvancingresearchintheLLM-generatedtextdetectiontask.Thesedatasetsenableresearcherstoswiftlydevelopandcalibrateefficient
detectorsandestablishstandardizedmetricsforevaluatingtheefficacyoftheirmethodologies.However,procuringsuchhigh-qualitylabeleddataoftendemandssubstantial
financial, material, and human resources. Presently, the development of datasets focusedondetectingLLM-generatedtextisinitsnascentstages,plaguedbyissuessuchas
13

<!-- Page 14 -->

limiteddatavolumeandsamplecomplexity,bothcrucialforcraftingrobustdetectors.In
thissection,wefirstintroducepopulardatasetsemployedfortrainingLLM-generated
text detectors. Additionally, we highlight datasets from unrelated domains or tasks,
which,thoughnotinitiallydesignedfordetectiontasks,canberepurposedforvarious
detection scenarios, which is a prevailing strategy in many contemporary detection
studies.WesubsequentlyintroducebenchmarksforverifyingtheeffectivenessofLLM-
generated text detectors, which are carefully designed to evaluate the performance of
thedetectorfromdifferentperspectives.Lastly,weevaluatethesetrainingdatasetsand
benchmarks, identifying current shortcomings and challenges in dataset construction
forLLM-generatedtextdetection,aimingtoinformthedesignoffuturedataresources.
4.1Training
4.1.1 Detection Datasets. Massive and high-quality datasets can assist researchers in
rapidlytrainingtheirdetectors.Wethoroughlyorganizeandcomparedatasetsthatare
widely used and have potential, refer to Table 5. Given that different studies focus on
various practical issues, our aim is to facilitate researchers in conveniently selecting
high-qualitydatasetsthatmeettheirspecificneedsthroughourcomprehensivereview
work.

### Table5

SummaryofDetectionDatasetsforLLM-generatedtextdetection.

### Corpus Use HumanLLMs LLMsType Language Attack Domain

HC3(Guoetal.2023) train ~80k ~43k ChatGPT English, - WebText,QA,SocialMedia

### Chinese

CHEAT(Yuetal.2023a) train ~15k ~35k ChatGPT English Paraphrase ScientificWriting
HC3 Plus (Su et al. train ~95k GPT-3.5-Turbo Englilsh, Paraphrase NewsWriting,SocialMedia
2023b) valid ~10k Chinese
test ~38k
OpenLLMText (Chen train, ~52k ~209k ChatGPT, PaLM, LLaMA, English - WebText
etal.2023a) valid, ~8k ~33k GPT2-XL
test ~8k ~33k
GROVER Dataset train ~24k Grover-Mega English - NewsWriting
(Zellersetal.2019b)
TweepFake(Fagnietal. train ~12k ~12k GPT-2, RNN, Markov, LSTM, English - SocialMedia
2021) CharRNN
GPT-2OutputDataset6 train ~250k ~2000kGPT-2(small,medium,large,xl) English - WebText
test ~5k ~40k
ArguGPT (Liu et al. train ~6k GPT2-Xl, Text-Babbage-001, English - Scientificwriting
2023c) valid 700 Text-Curie-001, Text-Davincitest 700 001, Text-Davinci-002, Text-

### Davinci-003,GPT-3.5-Turbo

DeepfakeTextDetect (Li train ~236k GPT (Text-Davinci-002, Text- English Paraphrase Social Media, News Writing,
etal.2023c) valid ~56k Davinci-003, GPT-Turbo-3.5), QA,StoryGeneration,Compretest ~56k LLaMA (6B, 13B, 30B, 65B), hensionandReasoning,Scien-
GLM-130B, FLAN-T5 (small, tificwriting
base,large,xl,xxl),OPT(125M,

## 350M, 1.3B, 2.7B, 6.7B, 13B,

30B,iml1.3B,iml-30B),T0(3B,

## 11B), Bloom-7B1, Gpt-J-6B,


### GPT-NeoX-20B)

HC3.TheHumanChatGPTComparisonCorpus(HC3)(Guoetal.2023)standsasoneof
theinitialopen-sourceeffortstocompareChatGPT-generatedtextwithhuman-written
text. It involves collecting both human and ChatGPT responses to identical questions.
Due to its pioneering contributions in this field, the HC3 corpus has been utilized in
numerous subsequent studies as a valuable resource. The corpus offers datasets in
14

<!-- Page 15 -->


### Wuetal. ASurveyonLLM-GeneratedTextDetection

both English and Chinese. Specifically, HC3-en comprises 58k human responses and
26k ChatGPT responses, derived from 24k questions, which primarily originate from
the ELI5 dataset, WikiQA dataset, Crawled Wikipedia, Medical Dialog dataset, and
FiQAdataset.Ontheotherhand,HC3-zhencompassesabroaderspectrumofdomains,
featuring 22k human answers and 17k ChatGPT responses. The data within HC3-
zh spans seven sources: WebTextQA, BaikeQA, Crawled BaiduBaike, NLPCC-DBQA
dataset,MedicalDialogdataset,BaiduAIStudio,andtheLegalQAdataset.However,it
ispertinenttonotesomelimitationsoftheHC3dataset,suchasthelackofdiversityin
promptsusedfordatacreation.
CHEAT. The CHEAT dataset (Yu et al. 2023a) stands as the most extensive publicly
accessible resource dedicated to detecting spurious academic content generated by
ChatGPT. It includes human-written academic abstracts sourced from IEEE Xplore,
with an average abstract length of 163.9 words and a vocabulary size of 130k words.
Following the ChatGPT generation process, the dataset contains 15k human-written
abstractsand35kChatGPT-generatedsummaries.Tobettersimulatereal-worldapplications,theoutputswereguidedbyChatGPTforfurtherrefinementandamalgamation.
The “polishing” process aims to simulate users who may seek to bypass plagiarism
detection by improving the text, while “blending” represents scenarios where users
might combine manually drafted abstracts with those seamlessly crafted by ChatGPT
to elude detection mechanisms. Nevertheless, a limitation of the CHEAT dataset is
itsfocusonnarrowacademicdisciplines,overlookingcross-domainchallenges,which
stemsfromconstraintsrelatedtoitsprimarydatasource.
HC3Plus.HC3Plus(Suetal.2023b)representsanenhancedversionoftheoriginalHC3
dataset,introducinganaugmentedsectionnamedHC3-SI.Thisnewsectionspecifically
targets tasks requiring semantic invariance, such as summarization, translation, and
paraphrasing,thusextendingthescopeofHC3.Tocompilethehuman-writtentextcorpusforHC3-SI,datawascuratedfromseveralsources,includingtheCNN/DailyMail
dataset, Xsum, LCSTS, the CLUE benchmark, and datasets from the Workshop on
MachineTranslation(WMT).Simultaneously,theLLM-generatedtextsweregenerated
usingGPT-3.5-Turbo.TheexpandedEnglishdatasetnowincludesatrainingsetof95k
samples, a validation set of 10k samples, and a test set of 38k samples. The Chinese
dataset,incomparison,contains42ktrainingsamples,4kforvalidation,and22kfortesting.Despitetheseexpansions,HC3-SIstillmirrorsHC3’sapproachtodataconstruction,
whichissomewhatmonolithicandlacksdiversity,particularlyinthevarietyofLLMs
andtheuseofcomplexandvariedpromptsforgeneratingdata.
OpenLLMText.TheOpenLLMTextdataset(Chenetal.2023a)isderivedfromfourtypes
ofLLMs:GPT-3.5,PaLM,LLaMA-7B,andGPT2-1B(alsoknownasGPT-2ExtraLarge).
ThesamplesfromGPT2-1BaresourcedfromtheGPT-2Outputdataset,whichOpenAI
has made publicly available. Text generation from GPT-3.5 and PaLM was conducted
using the prompt “Rephrase the following paragraph paragraph by paragraph: [Human_Sample],” while LLaMA-7B generated text by completing the first 75 tokens of
human samples. The dataset comprises a total of 344k samples, including 68k written
by humans. It is divided into training, validation, and test sets at 76%, 12%, and 12%,
respectively.Notably,thisdatasetfeaturesLLMslikePaLM,whicharecommonlyused
in everyday applications. However, it does not fully capture the nuances of crossdomainandmultilingualtext,whichlimitsitsusefulnessforrelatedresearch.
15

<!-- Page 16 -->

TweepFakeDataset.TweepFake(Fagnietal.2021)isafoundationaldatasetdesignedfor
the analysis of fake tweets on Twitter, derived from both genuine and counterfeit accounts.Itencompassesatotalof25ktweets,withanequaldistributionbetweenhumanwritten and machine-generated samples. The machine-generated tweets were crafted
usingvarioustechniques,includingGPT-2,RNN,Markov,LSTM,andCharRNN.While
TweepFake continues to be a dataset of choice for many scholars, those working with
LLMsshouldcriticallyassessitsrelevanceandrigorinlightofevolvingtechnological
capabilities.
GPT2-Output Dataset. The GPT2-Output Dataset,7 introduced by OpenAI, is based on
250kdocumentssourcedfromtheWebTexttestsetforitshuman-writtentext.Regarding
theLLM-generatedtext,thedatasetincludes250krandomlygeneratedsamplesusinga
temperaturesettingof1withouttruncationandanadditional250ksamplesproduced
with Top-K 40 truncation. This dataset was conceived to further research into the
detectability of the GPT-2 model. However, a notable limitation lies in the insufficient
complexityofthedataset,markedbytheuniformityofboththegenerativemodelsand
datadistribution.
GROVER Dataset. The GROVER Dataset, introduced by Zellers et al. (2019b), is styled
after news articles. Its human-written text is sourced from RealNews, a comprehensive corpus of news articles derived from Common Crawl. The LLM-generated text
is produced by Grover-Mega, a transformer-based news generator with 1.5 billion
parameters. A limitation of this dataset, particularly in the current LLM landscape, is
theuniformityandsingularityofbothitsgenerativemodelanddatadistribution.
ArguGPT Dataset. The ArguGPT Dataset (Liu et al. 2023c) is specifically designed for
detectingLLM-generatedtextinvariousacademiccontextssuchasclassroomexercises,
TOEFL, and GRE writing tasks. It comprises 4k argumentative essays, generated by
sevendistinctGPTmodels.Itsprimaryaimistotackletheuniquechallengesassociated
withteachingEnglishasasecondlanguage.
DeepfakeTextDetect Dataset. Attention is also drawn to the DeepfakeTextDetect Dataset
(Li et al. 2023c), a robust platform tailored for deepfake text detection. The dataset
combineshuman-writtentextfromtendiversedatasets,encompassinggenreslikenews
articles,stories,scientificwritings,andmore.Itfeaturestextsgeneratedby27prominent
LLMs, sourced from entities such as OpenAI, LLaMA, and EleutherAI. Furthermore,
thedatasetintroducesanaugmentedchallengewiththeinclusionoftextproducedby
GPT-4andparaphrasedtext.
4.1.2 Potential Datasets. Constructing a dataset from scratch that encompasses both
human-written and LLM-generated text can indeed be a resource-intensive endeavor.
Recognizing the diverse requirements for LLM-generated text detection across scenarios, researchers commonly adapt existing datasets from fields like Q&A, academic
writing, and story generation to represent human-written text. They then produce
LLM-generatedtextfordetectorstrainingusingmethodslikepromptengineeringand
bootstrapcomplementation.Thissurveyoffersaconciseclassificationandoverviewof
thesedatasets,summarizedinTable6.
7 https://github.com/openai/gpt-2-output-dataset
16

<!-- Page 17 -->

Wuetal. ASurveyonLLM-GeneratedTextDetection

### Table6

SummaryofotherpotentialdatasetsthatcaneasilyextendedtoLLM-generatedtextdetection
tasks.

### Corpus Size Source Language Domain

XSum(Narayan,Cohen,andLapata2018) 42k BBC English NewsWriting
SQuAD(Rajpurkaretal.2016) 98.2k Wiki English QuestionAnswering
WritingPrompts(Fan,Lewis,andDauphin2018) 302k RedditWRITINGPROMPTS English StoryGeneration

### Wiki40B(Guoetal.2020) 17.7m Wiki 40+Languages WebText

PubMedQA(Jinetal.2019) 211k PubMed English QuestionAnswering
Children’sBookCorpus(Hilletal.2016) 687k Books English QuestionAnswering
AvaxTweetsDataset(Muric,Wu,andFerrara2021) 137m Twitter English SocialMedia
ClimateChangeDataset(LittmanandWrubel2019) 4m Twitter English SocialMedia

### YelpDataset(Asghar2016) 700k Yelp English SocialMedia


### ELI5(Fanetal.2019) 556k Reddit English QuestionAnswering

ROCStories(Mostafazadehetal.2016) 50k Crowdsourcing English StoryGeneration
HellaSwag(Zellersetal.2019a) 70k ActivityNetCaptions,Wikihow English QuestionAnswering
SciGen(Moosavietal.2021) 52k arXiv English ScientificWriting,QuestionAnswering

### WebText(Radfordetal.2019) 45m Web English WebText

TruthfulQA(Lin,Hilton,andEvans2022) 817 authorswrittEnglish English QuestionAnswering
NarrativeQA(Kocˇiskýetal.2018) 1.4k Gutenberg3,web English QuestionAnswering
TOEFL11(Blanchardetal.2013) 12k TOEFLtest 11Languages Scientificwriting

### NIPS2013–2017,CoNLL2016,ACL2017

PeerReviews(Kangetal.2018) 14.5k English ScientificWriting

### ICLR2017,arXiv2007–2017

Q&A. Q&A is a prevalent and equitable method for constructing datasets. By posing
identicalquestionstoLLMs,onecangeneratepairedsetsofhuman-writtenandLLM-
generatedtext.
• PubMedQA(Jinetal.2019):Thisisabiomedicalquestion-and-answer(QA)
datasetsourcedfromPubMed.8
• ChildrenBookCorpus(Hilletal.2016):Thisdataset,derivedfromfreely
availablebooks,gaugesthecapacityofLMstoharnessbroaderlinguistic
contexts.Itchallengesmodelstoselectthecorrectanswerfromtenpossible
options,basedonacontextof20consecutivesentences.Theanswertypes
encompassverbs,pronouns,namedentities,andcommonnouns.
• ELI5(Fanetal.2019):Asubstantialcorpusforlong-formQ&A,ELI5
focusesontasksdemandingdetailedresponsestoopen-endedqueries.
Thedatasetcomprises270kentriesfromtheRedditforum“ExplainLike
I’mFive”,whichoffersexplanationstailoredtothecomprehensionlevelof
afive-year-old.
• TruthfulQA(Lin,Hilton,andEvans2022):Thisbenchmarkevaluatesthe
veracityofanswersgeneratedbyLLMs.Itencompasses817questions
spreadacross38categoriessuchashealth,law,finance,andpolitics.All
questionswerecraftedbyhumans.
8 https://www.ncbi.nlm.nih.gov/pubmed/
17

<!-- Page 18 -->

• NarrativeQA(Kocˇiskýetal.2018):ThisEnglish-languagedatasetincludes
summariesorstoriesalongwithrelatedquestionsaimedatassessing
readingcomprehension,especiallyconcerningextendeddocuments.Data
issourcedfromProjectGutenberg9andweb-scrapedmoviescripts,with
hiredannotatorsprovidingtheanswers.
Scientific Writing. Scientific writing is frequently explored in real-world research contexts. Given a specific academic topic, LLMs can efficiently generate academic articles
orabstracts.
• PeerRead(Kangetal.2018):Thisrepresentstheinauguralpublicdatasetof
scientificpeer-reviewedarticles,comprising14.7kdraftarticlesand10.7k
expert-writtenpeerreviewsforasubsetofthesearticles.Additionally,it
includestheacceptanceorrejectiondecisionsfrompremierconferences
suchasACL,NeurIPS,andICLR.
• ArXiv:10Afreelyaccessibledistributionserviceandrepository,ArXiv
hosts2.3millionscholarlyarticlesspanningdisciplineslikephysics,
mathematics,computerscience,andstatistics.
• TOEFL11(Blanchardetal.2013):Apubliclyaccessiblecorpusfeaturing
worksofnon-nativeEnglishwritersfromtheTOEFLtest,itencompasses
1.1kessaysamplesacross11languages:Arabic,Chinese,French,German,
Hindi,Italian,Japanese,Korean,Spanish,Telugu,andTurkish.These
essaysareuniformlydistributedovereightwritingpromptsandthree
scorelevels(low/medium/high).
Story Generation. LLMs excel in the domain of story generation, with users frequently
utilizingstorytitlesandwritingpromptstoguidethemodelsintheircreativeendeavors.
• WritingPrompts(Fan,Lewis,andDauphin2018):Thisdatasetcomprises
300khuman-writtenstoriespairedwithwritingprompts.Thedatawas
sourcedfromReddit’swritingpromptsforum,avibrantonline
communitywheremembersinspireoneanotherbypostingstoryideasor
prompts.Storiesinthisdatasetarerestrictedinlength,rangingbetween30
to1kwords,withnowordsrepeatedmorethan10times.
NewsWriting.Thetaskofnewsarticlewritingcanbeapproachedthrougharticlesummary datasets. LLMs can be instructed either to generate abstracts from the primary
textortogeneratearticlesbasedonprovidedabstracts.Nonetheless,giventheresource
constraints,researchersoftenemployLLMstogeneratesuchdatasetsbydirectlyreinterpretingoraugmentingtheexistingabstractsandarticles.
• ExtremeSummarization(XSum)(Narayan,Cohen,andLapata2018):This
datasetcontainsBBCarticlesaccompaniedbyconciseone-sentence
abstracts.Itencompassesatotalof225ksamplesfrom2010to2017,
9 https://gutenberg.org/
10 https://arxiv.org/
18

<!-- Page 19 -->


### Wuetal. ASurveyonLLM-GeneratedTextDetection

spanningvariousdomainssuchasNews,Politics,Sports,Weather,
Business,Technology,Science,Health,Family,Education,Entertainment,
Arts,andmore.
WebText.WebtextdataprimarilyoriginatesfromplatformslikeWikipedia.Forwebtext
generation,acommonapproachistoprovidetheLLMswithanopeningsentenceand
allowthemtocontinuethenarrative.Alternatively,LLMscanbeinstructedtogenerate
contentbasedonawebpagetitle.
• Wiki-40B(Guoetal.2020):Initiallyconceivedasamultilingualbenchmark
forlanguagemodeltraining,thisdatasetcomprisestextfrom
approximately19.5millionWikipediapagesacross40languages,
aggregatingtoabout40billioncharacters.Thecontenthasbeen
meticulouslycleanedtomaintainquality.
• WebText(Radfordetal.2019):Originallyutilizedtoinvestigatethelearning
potentialofLMsorLLMs,thisdatasetencompasses45millionwebpages.
Prioritizingcontentquality,thedatasetexclusivelyincludeswebpages
curatedorfilteredbyhumans,whiledeliberatelyexcludingcommon
sourcesfromotherdatasets,suchasWikipedia.
SocialMedia.SocialMediadatasetsareinstrumentalinassessingthedisparityinsubjectiveexpressionsbetweenLLM-generatedandhuman-writtentexts.
• YelpReviewsDataset(Asghar2016):Sourcedfromthe2015YelpDataset
Challenge,thisdatasetwasprimarilyusedforclassificationtaskssuchas
predictinguserratingsbasedonreviewsanddeterminingpolaritylabels.
Itcomprises1.5millionreviewtextsamples.
• r/ChangeMyView(CMV)RedditSubcommunity:11Oftenreferredtoas
“ChangeMyView(CMV)”,thissubredditoffersaplatformforusersto
debateaspectrumoftopics,rangingfrompoliticsandmediatopopular
culture,oftenpresentingcontrastingviewpoints.
• IMDBDataset:12Servingasanexpansivefilmreviewdatasetforbinary
sentimentclassification,itexceedspriorbenchmarkdatasetsinvolume,
encompassing25ktrainingand25ktestsamples.
• AvaxTweetsDataset(Muric,Wu,andFerrara2021):Designedtoexamine
anti-vaccinemisinformationonsocialmedia,thisdatasetwasacquiredvia
theTwitterAPI.Itfeaturesastreamingdatasetcenteredonkeywordswith
over1.8milliontweets,complementedbyahistoricalaccount-level
datasetcontainingmorethan135milliontweets.
• ClimateChangeTweetsIds(LittmanandWrubel2019):Thisdatasethouses
thetweetIDsfor39.6milliontweetsrelatedtoclimatechange.These
tweetsweresourcedfromtheTwitterAPIbetween21September2017and
17May2019usingtheSocialFeedManager,basedonspecificsearch
keywords.
11 https://www.reddit.com/r/changemyview/
12 https://huggingface.co/datasets/imdb
19

<!-- Page 20 -->

Comprehension and Reasoning. Datasets geared towards comprehension and generation
typicallyprovideconsistentcontextualmaterials,guidingLLMsintheregenerationor
continuationoftext.
• StanfordQuestionandAnswerDataset(SQuAD)(Rajpurkaretal.2016):This
readingcomprehensiondatasetfeatures100kQ&Apairs,encompassing
subjectsfrommusicalcelebritiestoabstractnotions.Itdrawssamplesfrom
thetop10kEnglishWikipediaarticlessourcedviaPageRank.Fromthis
collection,536articleswererandomlyselected,excludingpassagesshorter
than500words.Crowdsourcecontributorsframethequestionsbasedon
theseexperts,whileadditionalpersonnelprovidetheanswers.
• SciGen(Moosavietal.2021):Thistaskcentersonreasoningfrom
perceptualdatatogeneratetext.Itcomprisestablesfromscientificarticles
alongsidetheirdescriptions.Theentiredatasetissourcedfromthe
“ComputerScience”sectioninthearXivwebsite,holdingupto17.5k
samplesfrom“ComputationandLanguage”andanother35.5kfrom
domainslike“MachineLearning”.Additionally,thedatasetfacilitatesthe
evaluationofgenerativemodels’arithmeticreasoningcapabilitiesusing
intricateinputformats,suchasscientifictables.
• ROCStoriesCorpora(ROC)(Mostafazadehetal.2016):Aimedatnatural
languageunderstanding,thisdatasettaskssystemswithdeterminingthe
aptconclusiontoafour-sentencenarrative.Itisacuratedcollectionof50k
five-sentencestoriesreflectingeverydayexperiences.Beyonditsprimary
purpose,itcanalsosupporttaskslikestorygeneration.
• HellaSwag(Zellersetal.2019a):Focusedoncommon-sensereasoning,this
datasetencompassesapproximately70kquestions.UtilizingAdversarial
Filtering(AF),thedatasetcraftsmisleadingandintricatefalseanswersfor
multiple-choicesettings,wheretheobjectiveistopinpointthecorrect
answerincontext.
4.2EvaluationBenchmarks
Benchmarks with high quality can help researchers verify whether their detectors are
feasible and effective rapidly. We sort out and compare the benchmarks that are currentlypopularorwithpotential,asshowninTable7.Ontheonehand,wehopetohelp
researchersbetterunderstandtheirdifferencestochoosesuitablebenchmarksfortheir
experiments. On the other hand, we hope to draw researchers’ attention to the latest
benchmarks, which have been fully designed to verify the latest issues for the task,
withgreatpotential.
TuringBench.TheTuringBenchdataset(Uchenduetal.2021)isaninitiativedesignedto
explorethechallengesofthe“Turingtest”inthecontextofneuraltextgenerationtechniques. It comprises human-written content derived from 10k news articles, predominantlyfromreputablesourcessuchasCNN.Forthepurposeofthisdataset,onlyarticles
rangingbetween200to400wordswereselected.LLM-generatedtextwithinthisdataset
is produced by 19 distinct text generation models, including GPT-1, GPT-2 variants
(small, medium, large, xl, and pytorch), GPT-3, different versions of GROVER (base,
large,andmega),CTRL,XLM,XLNETvariants(baseandlarge),FAIRforbothWMT19
20

<!-- Page 21 -->

Wuetal. ASurveyonLLM-GeneratedTextDetection

### Table7

SummaryofbenchmarksforLLM-generatedtextdetection.

### Corpus Use HumanLLMs LLMsType Language Attack Domain

TuringBench(Uchenduetal. train ~8k ~159k GPT-1, GPT-2, GPT-3, English - NewsWriting

## 2021) Grover,Ctrl,Xlm,


## Xlnet,Fair,Trans-


## Former_Xl,Pplm

MGTBench(Heetal.2023) train ~2.4k ~14.4k ChatGPT, ChatGPT- English Adversarial Scientific Writing,
test ~0.6k ~3.6k turbo,ChatGLM,Dolly, Story Generation,

### GPT4All,StableLM NewsWriting

GPABenchmark (Liu et al. test ~150k ~450k GPT-3.5 English Paraphrase ScientificWriting
2023d)
Scientific-articles Benchmark test ~16k ~13k SCIgen, GPT-2, GPT-3, English - ScientificWriting
(Moscaetal.2023) ChatGPT,Galactica
MULTITuDE (Macko et al. train ~4k ~40k Alpaca-lora, GPT-3.5- Arabic, - Scientific Writing,
2023) test ~3k ~26k Turbo, GPT-4, LLaMA, Catalan, NewsWriting,So-
OPT, OPT-IML-Max, Chinese, cialMedia
Text-Davinci-003, Czech,
Vicuna Dutch,
English,

### German,

Portuguese,
Russian,

### Spanish,


### Ukrainian

HANSEN(Triptoetal.2023) test - ~21k ChatGPT, PaLM2, Vi- English - SpokenText
cuna13B
M4(Wangetal.2023b) train ~35k ~112k GPT-4, ChatGPT, GPT- English, - Web Text,
valid ~3.5k ~3.5k 3.5, Cohere, Dolly-v2, Chinese, Scientific Writing,
test ~3.5k ~3.5k BLOOMz176B Russian, News Writing,
Urdu, In- SocialMedia,QA
donesian,
Bulgarian,

### Arabic

and WMT20, Transformer-XL, and both PLM variants (distil and GPT-2). Each model
contributed 8k samples, categorized by label type. Notably, TuringBench emerged as
one of the pioneering benchmark environments for the detection of LLM-generated
text.However,giventherapidadvancementsinLLMtechnologies,thesampleswithin
TuringBench are now less suited for training and validating contemporary detector
performances.Assuch,timelyupdatesincorporatingthelatestgenerationmodelsand
theirresultanttextsareimperative.
MGTBench. Introduced by He et al. (2023), MGTBench stands as the inaugural benchmark framework for MGT detection. It boasts a modular architecture, encompassing
an input module, a detection module, and an evaluation module. The dataset draws
upon several of the foremost LLMs, including ChatGPT, ChatGLM, Dolly, ChatGPT-
turbo, GPT4All, and StableLM, for text generation. Furthermore, it incorporates over
tenwidely-recognizeddetectionalgorithms,demonstratingsignificantpotential.
GPABenchmark. The GPABenchmark (Liu et al. 2023d) is a comprehensive dataset
encompassing 600k samples. These samples span human-written, GPT-written, GPT-
completed,andGPT-polishedabstractsfromabroadspectrumofacademicdisciplines,
21

<!-- Page 22 -->

suchascomputerscience,physics,andthehumanitiesandsocialsciences.Thisdataset
meticulously captures the quintessential scenarios reflecting both the utilization and
potentialmisapplicationofLLMsinacademiccomposition.Consequently,itdelineates
threespecifictasks:generationoftextbasedonaprovidedtitle,completionofapartial
draft, and refinement of an existing draft. Within the domain of academic writing
detection,GPABenchmarkstandsasarobustbenchmark,attributedtoitsvoluminous
dataanditsholisticapproachtoscenariorepresentation.
Scientific-articles Benchmark. The Scientific-articles Benchmark (Mosca et al. 2023) comprises16khuman-writtenarticlesalongside13kLLM-generatedsamples.ThehumanwrittenarticlesaresourcedfromthearXivdatasetavailableonKaggle.Incontrast,the
machine-generated samples, which include abstracts, introductions, and conclusions,
are produced by SCIgen, GPT-2, GPT-3, ChatGPT, and Galactica using the titles of
the respective scientific articles as prompts. A notable limitation of this dataset is its
omissionofvariousadversarialattacktypes.
MULTITuDE. It is a benchmark for detecting machine-generated text in multiple languages. This dataset consists of 74k machine-generated texts and 7k human-written
textsacross11languages(Mackoetal.2023),includingArabic,Catalan,Chinese,Czech,
Dutch, English, German, Portuguese, Russian, Spanish, and Ukrainian. The machinegeneratedtextsareproducedbyeightgenerativemodels,includingAlpaca-Lora,GPT-
3.5-turbo,GPT-4,LLaMA,OPT,OPT-IML-Max,Text-Davinci-003,andVicuna.Inanera
ofrapidlyincreasingnumbersofmultilingualLLMs,MULTITuDEservesasaneffective
benchmark for assessing the detection capabilities of LLM-generated text detectors in
variouslanguages.
HANSEN. TheHumanand AISpokenTextBenchmark(HANSEN)(Tripto etal.2023)
is the largest benchmark for spoken text, encompassing the organization of 17 speech
datasetsandrecords,aswellas23knovelAI-generatedspokentexts.TheAI-generated
spokentextsinHANSENwerecreatedbyChatGPT,PaLM2,andVicuna-13B.Duetothe
stylisticdifferencesbetweenspokenandwrittenlanguage,detectorsmayrequireamore
nuancedunderstandingofspokentext.HANSENcaneffectivelyassesstheprogressin
researchaimedatdevelopingsuchnuanceddetectors.
M4. M4 (Wang et al. 2023b) serves as a comprehensive benchmark corpus for the
detection of text generated by LLMs. It spans a variety of generators, domains, and
languages.Compiledfromdiversesources,includingwikipagesfromvariousregions,
newsoutlets,andacademicportals,thedatasetreflectscommonscenarioswhereLLMs
are utilized in daily applications. The LLM-generated texts in M4 are created using
cutting-edgegenerativemodelssuchasChatGPT,LLaMa,BLOOMz,FlanT5,andDolly.
Notably, the dataset captures cross-lingual subtleties, featuring content in more than
ten languages. In summary, while the M4 dataset proficiently tackles complexities
acrossdomains,models,andlanguages,itcouldbefurtherenrichedbyincorporatinga
broaderrangeofadversarialscenarios.
22

<!-- Page 23 -->

Wuetal. ASurveyonLLM-GeneratedTextDetection
4.3DataChallenges
Inlightofourextensiveexperienceinthearea,anotabledeficiencypersistsintherealm
ofrobustdatasetsandbenchmarkstailoredforLLMs.Despitecommendableadvancements, current efforts remain insufficient. A noticeable trend among researchers is the
tendencytoutilizedatasetsoriginallydesignedforothertasksashuman-writtentexts,
and produce LLM-generated texts base on them for training detectors. This approach
arises from the limitations of existing datasets or benchmarks in comprehensively addressing diverse research perspectives. As a result, we aim to outline the prominent
limitationsandchallengesassociatedwiththecurrentdatasetsandbenchmarksinthis
article.
4.3.1 Comprehensiveness of Evaluation Frameworks. Before gaining trust, a reliable
detector demands multifaceted assessment. The current benchmarks are somewhat
limited, providing only superficial challenges and thereby not facilitating a holistic
evaluation of detectors. We highlight five crucial dimensions that are essential for the
developmentofmorerobustbenchmarksforLLM-generatedtextdetectiontask.These
dimensions include the incorporation of multiple types of attacks, diverse domains,
variedtasks,aspectrumofmodels,andtheinclusionofmultiplelanguages.
Multiple Types of Attack. are instrumental in ascertaining the efficacy of detection
methodologies. In practical environments, LLM-generated text detectors often encountertextsthataregeneratedusingawiderangeofattackmechanisms,whichdiffer
fromtextsgeneratedthroughsimpleprompts.Forinstance,thepromptattackelucidated
insubsection7.2impelsthegenerativemodeltoyieldsuperior-qualitytext,leveraging
intricate and sophisticated prompts. Integrating such texts into prevailing datasets is
imperative.ThisconcernisalsoechoedinthelimitationsoutlinedbyGuoetal.(2023).
Multi-domains and multi-tasks. configurations are pivotal in assessing a detector’s performanceacrossdiversereal-worlddomainsandLLMapplications.Thesedimensions
bear significant implications for a detector’s robustness, usability, and credibility. For
instance,inscholarlycontexts,aproficientdetectorshouldconsistentlyexcelacrossall
fields. In everyday scenarios, it should adeptly identify LLM-generated text spanning
academic compositions, news articles, arithmetic reasoning, and Q&A sessions. While
numerousexistingstudiesprudentlyincorporatetheseconsiderations,weadvocatefor
theproliferationofsuperior-qualitydatasets.
Multiple LLMs. The ongoing research momentum in LLMs has ushered in formidable
counterparts like LLaMa (Touvron et al. 2023), PaLM (Chowdhery et al. 2022a), and
Claude-2,13 rivaling ChatGPT’s prowess. As the spotlight remains on ChatGPT, it is
essentialtoconcurrentlyaddresspotentialrisksemanatingfromotheremergingLLMs.
Multilingual. considerations demand increased attention. We strongly encourage researcherstospearheadthecreationofmultilingualdatasetstofacilitatetheevaluation
oftextdetectorsgeneratedbyLLMsacrossdifferentlanguages.Theutilizationofpretrained models may uncover instances where certain detectors struggle with under-
13 https://www.anthropic.com/index/claude-2
23

<!-- Page 24 -->

representedlanguages,whileLLMscouldexhibitmorenoticeableinconsistencies.This
dimensionpresentsarichavenueforexplorationanddiscourse.
4.3.2 Temporal. It is discernible that certain contemporary studies persistently employed seminal but somewhat antiquated benchmark datasets, which had significantlyshapedpriorGPT-generatedtextandfakenewsdetectionendeavors.However,
thesedatasetspredominantlyoriginatefrombackwardLLMs,implyingthatvalidated
methodologies might not invariably align with current real-world dynamics. We emphasize the significance of utilizing datasets formulated with advanced and powerful
LLMs, while also urging benchmark dataset developers to regularly update their contributionstoreflecttherapidevolutionofthefield.

## AdvancesinDetectorResearch

Inthissection,wepresentdifferentdetectordesignsanddetectionalgorithms,including watermarking technology, statistics-based detectors, neural-based detectors, and
human-assistedmethods.Wefocusonthemostrecentlyproposedmethodsanddivide
ourdiscussionaccordingtotheirunderlyingprinciples(seeFigure4).
5.1WatermarkingTechnology
Originally deployed within the realm of computer vision for the development of generative models, watermarking techniques have been integral to the detection of AI-
generatedimages,servingasprotectivemeasuresforintellectualandpropertyrightsin
thevisualarts.WiththeadventandsubsequentproliferationofLLMs,theapplication
ofwatermarkingtechnologyhasexpandedtoencompasstheidentificationoftextgeneratedbythesemodels.Watermarkingtechniquesnotonlyprotectsubstantialmodels
fromunauthorizedacquisition,suchasthroughsequencedistillationbutalsomitigate
therisksassociatedwithreplicationandmisuseofLLM-generatedtext.
5.1.1Data-DrivenWatermarking.Data-drivenmethodsenabletheverificationofdata
ownershiporthetrackingofillegalcopyingormisusebyembeddingspecificpatterns
ortagswithinthetrainingdatasetsofLLMs.Thesemethodstypicallyrelyonbackdoor
insertion, where a small number of watermarked samples are added to the dataset,
allowing the model to implicitly learn a secret function set by the defender. When
a specific trigger is activated, the backdoor watermark is triggered, which is usually
implementedinablack-boxsetting(Guetal.2022).Thismechanismprotectsthemodel
fromunauthorizedfine-tuningorusebeyondthetermsofthelicensebyembeddinga
backdoorduringthefoundationalandmulti-tasklearningframeworkphasesofmodel
training, specified by the owner’s input. Even if the model is fine-tuned for several
downstreamtasks,thewatermarkremainsdifficulttoeradicate.
However,subsequentstudiesidentifiedvulnerabilitiesinthistechnology,showing
thatitcanberelativelyeasilycompromised.LucasandHavens(2023)detailedanattack
method on this watermarking strategy by analyzing the content generated by autoregressive models to precisely locate the trigger words or phrases of the backdoor watermark.Thestudypointsoutthattriggerscomposedofrandomlycombinedcommon
wordsareeasiertodetectthanthosecomposedofuniqueandraremarkers.Additionally,theresearchmentionsthataccesstothemodel’sweightsistheonlyprerequisitefor
detectingthebackdoorwatermark.Recently,Tangetal.(2023)introducedaclean-label
24

<!-- Page 25 -->


### Wuetal. ASurveyonLLM-GeneratedTextDetection

Data-DrivenWatermarking:(Guetal.2022)/(LucasandHavens2023)/
(Tangetal.2023)
Model-DrivenWatermarking:(Kirchenbaueretal.2023a)/(Leeetal.2023b)/
(Kirchenbaueretal.2023b)/(Liuetal.2023b)/(Liuetal.2023a)/
(Kuditipudietal.2023)/(Houetal.2023)
WatermarkingTechnology Post-ProcessingWatermarking:(Por,Wong,andChee2012)/
(Rizzo,Bertini,andMontesi2016)/(Topkara,Topkara,andAtallah2006)/
(Yangetal.2022)/(MunyerandZhong2023)/(Yooetal.2023)/
(Yangetal.2023a)/(AbdelnabiandFritz2021)/(Zhangetal.2023a)
LinguisticsFeaturesStatistics:(Corston-Oliver,Gamon,andBrockett2001)/
(Kalinichenkoetal.2003)/(Baayen2001)/(AraseandZhou2013)/
(Galléetal.2021)/(HamedandWu2023)
White-BoxStatistics:(Solaimanetal.2019)/(Gehrmann,Strobelt,andRush2019)
(Suetal.2023a)/(Lavergne,Urvoy,andYvon2008)/(Beresneva2016)/
(Vasilatosetal.2023)/(Wuetal.2023)/(Mitchelletal.2023)/(Dengetal.2023)/
(Baoetal.2023)/(Yangetal.2023b)/(Tulchinskiietal.2023)

### Statistics-BasedDetectors

Black-BoxStatistics:(Yangetal.2023b)/(Maoetal.2024)/(Zhuetal.2023)/
(Yuetal.2023b)/(Quidwai,Li,andDube2023)/(GuoandYu2023)
Advanced Feature-BasedClassifiers:(Aich,Bhattacharya,andParde2022)/(Shahetal.2023)/
(CorizzoandLeal-Arenas2023)/(Mindner,Schlippe,andSchaaff2023)/

### Detector

(Schaaff,Schlippe,andMindner2023)/(Schusteretal.2020a)/
Research (Crothersetal.2022)/(Lietal.2023a)/(Wangetal.2023a)/(WuandXiang2023)
(Sec.5)
Pre-TrainingClassifiers:(Bakhtinetal.2019)/(Uchenduetal.2020)/
(Antounetal.2023a)/(Lietal.2023c)/(Fagnietal.2021)/(Gambinietal.2022)/
(Guoetal.2023)/(Liuetal.2023c)/(Liuetal.2023d)/(Wangetal.2023c)/
(Wangetal.2023c)/(Bakhtinetal.2019)/(Uchenduetal.2020)/
(Antounetal.2023a)/(Lietal.2023c)/(Sarvazyanetal.2023a)/
(Rodriguezetal.2022b)/(Liuetal.2022)/(Zhongetal.2020)/
(Bhattacharjeeetal.2023)/(Yang,Jiang,andLi2023)/(Shietal.2023)/

### Neural-BasedDetectors

(Koike,Kaneko,andOkazaki2023b)/(Heetal.2023)/(Hu,Chen,andHo2023)/
(Koike,Kaneko,andOkazaki2023b)/(Tuetal.2023)/(Kumarageetal.2023a)/
(Cowap,Graham,andFoster2023)/(Uchendu,Le,andLee2023b)

### LLMsasDetectors:(Zellersetal.2019b)/(Liuetal.2023c)/

(BhattacharjeeandLiu2023)/(Koike,Kaneko,andOkazaki2023b)
IntuitiveIndicators:(Uchenduetal.2023)/(Duganetal.2023)/
/(Jawahar,Abdul-Mageed,andLakshmanan2020)
ImperceptibleFeatures:(Ippolitoetal.2020)/(Clarketal.2021b)/
(Gehrmann,Strobelt,andRush2019)
EnhancingHumanDetectionCapabilities:(Ippolitoetal.2020)/(Duganetal.2020)/
(Duganetal.2023)/(Douetal.2022)

### Human-AssistedMethods

MixedDetection:UnderstandingandExplanation:(Wengetal.2023)

### Figure4

ClassificationofLLM-generatedtextdetectorswithcorrespondingdiagramsandpaperlists.We
categorizethedetectorsintowatermarkingtechnology,statistics-baseddetectors,neural-based
detectors,andhuman-assistedmethods.Inthediagrams,HWTrepresentsHuman-WrittenText
andLGTrepresentsLLM-GeneratedText.Weusetheorangelinestohighlightthesourceofthe
detector’sdetectioncapability,andthegreenlinestodescribethedetectionprocess.
25

<!-- Page 26 -->

backdoorwatermarkingframeworkthatusessubtleadversarialperturbationstomark
andtriggersamples.Thismethodeffectivelyprotectsthedatasetwhileminimizingthe
impactontheperformanceoftheoriginaltask.Theresultsshowthataddingjust1%of
watermarkedsamplescaninjectatraceablewatermarkfeature.
Itisimportanttonotethatdata-drivenmethodswereinitiallydesignedtoprotect
copyright of datasets and therefore generally lack substantial payload capacity and
generalizability. Moreover, applying such techniques in the field of LLM-generated
text detection requires significant resource investment, including the embedding of
watermarksinavastamountofdataandtheretrainingofLLMs.|
5.1.2 Model-Driven Watermarking. Model-Driven methods embed watermarks directlyintotheLLMsbymanipulatingthelogitsoutputdistributionortokensampling
during the inference process. As a result, the LLMs generate responses that carry the
embeddedwatermark.
Logits-BasedMethods.Kirchenbaueretal.(2023a)werethefirsttodesignalogits-based
watermarking framework for LLMs, characterized by minimal impact on text quality.
This framework facilitates the detection process through efficient open-source algorithms,eliminatingtheneedtoaccesstheLLM’sAPIorparameters.Beforetextgeneration,themethodrandomlyselectsasetof“green”tokens,definestherestas“red,”and
then gently guides the model to choose tokens from the “green” set during sampling.
Additionally, Kirchenbauer et al. (2023a) developed a watermark detection method
basedoninterpretablep-values,whichidentifieswatermarksbyperformingstatistical
analysisontheredandgreentokenswithinthetexttocalculatethesignificanceofthe
p-values. Following (Kirchenbauer et al. 2023a), Lee et al. (2023b) introduced a new
watermarking method called SWEET, which elevates “green” tokens only at positions
with high token distribution entropy during the generation process, thus maintaining
thewatermark’sstealthandintegrity.Itusesentropy-basedstatisticaltestsandZ-scores
fordetectingwatermarkedcode.
Despite the excellent performance of Kirchenbauer et al. (2023a), its robustness
is still debated. Recent work from Kirchenbauer et al. (2023b) studies the resistance
of watermarked texts to attacks via manual rewriting, rewriting using an unwatermarkedLLM,orintegrationintoalargecorpusofhandwrittendocuments.Thisstudy
introduces a window testing method called “WinMax” to evaluate the effectiveness
of accurately detecting watermarked areas within a large number of documents. To
addressthechallengesofsynonymsubstitutionandtextparaphrasing,Liuetal.(2023b)
proposed a semantic invariant robust watermarking method for LLMs. This method
generates semantic embeddings for all preceding tokens and uses them to determine
thewatermarklogic,demonstratingrobustnesstosynonymsubstitutionandtextparaphrasing.Moreover,currentwatermarkdetectionalgorithmsrequireasecretkeyduring
generation, which can lead to security vulnerabilities and forgery in public detection
processes.Toaddressthisissue,Liuetal.(2023a)introducedthefirstdedicatedprivate
watermarkingalgorithmforwatermarkgenerationanddetection,deployingtwodifferentneuralnetworksforeachstage.Byavoidingtheuseofthesecretkeyinbothstages,
this method innovatively extends existing text watermark algorithms. Furthermore, it
shares certain parameters between the watermark generation and detection networks,
thusimprovingtheefficiencyandaccuracyofthedetectionnetworkwhileminimizing
theimpactonthespeedofbothgenerationanddetectionprocesses.
26

<!-- Page 27 -->


### Wuetal. ASurveyonLLM-GeneratedTextDetection

TokenSampling-BasedMethods.Duringthenormalmodelinferenceprocess,tokensampling is determined by the sampling strategy and is often random, which helps guide
theLLMstoproducemoreunpredictabletext.Tokensampling-basedmethodsachieve
watermarking by influencing the token sampling process, either by setting random
seeds or specific patterns for token sampling. Kuditipudi et al. (2023) employed a
sequenceofrandomnumbersasasecretwatermarkkeytointerveneinanddetermine
the token sampling, which is then mapped into the LLMs to generate watermarked
text.Inthedetectionphase,thesecretkeyisutilizedtoalignthetextwiththerandom
number sequence for the detection task. The method demonstrates strong robustness
againstparaphrasingattacks,evenwhenapproximately40-50%ofthetokenshavebeen
modified.
AnotherrecentworkisSemStamp(Houetal.2023),arobustsentence-levelsemanticwatermarkingalgorithmbasedonLocality-SensitiveHashing(LSH).Thisalgorithm
starts by encoding and LSH hashing the candidate sentences generated by the LLM,
dividing the semantic embedding space into watermarked and non-watermarked regions.Itthencontinuouslyperformssentence-levelrejectionsamplinguntilasampled
sentencefallsintothewatermarkedpartitionofthesemanticembeddingspace.Experimental results indicate that this method is not only more robust than previous SOTA
methods in defending against common and more effective bigram paraphrase attacks
butalsosuperiorinmaintainingthequalityoftextgeneration.
In general, model-driven watermarking is a plug-and-play method that does not
requireanychangestothemodel’sparametersandhasminimalimpactontextquality,
makingitareliableandpracticalwatermarkingapproach.However,thereisstillsignificantopportunityforimprovementinitsrobustness,anditsspecificusabilityneedsto
befurtherexploredthroughadditionalexperimentsandpracticalapplications.
5.1.3 Post-Processing Watermarking. Post-processing watermarking refers to a technique that involves embedding a watermark by processing the text after it has been
outputbyaLLM.Thismethodtypicallyfunctionsasaseparatemodulethatworksina
pipelinewiththeoutputofthegenerativemodel.
Character-Embedded Methods. Early post-processing watermarking techniques relied on
the insertion or substitution of special Unicode characters into text. These characters
are difficult for the naked eye to recognize but carry distinct encoding information
(Por, Wong, and Chee 2012; Rizzo, Bertini, and Montesi 2016). More recently, Rizzo,
Bertini,andMontesi(2016)introducedEasymark,amethodwhichingeniouslyutilizes
the fact that Unicode has many code points with identical or similar appearances.
Specifically, Easymark embeds watermarks by replacing the regular space character
(U+0020)withanotherwhitespacecodepoint(e.g.,U+2004),usingUnicode’svariation
selectors,substitutingsubstrings,orusingspacesandhomoglyphsofslightlydifferent
lengths,allwhileensuringthattheappearanceofthetextremainsvirtuallyunchanged.
The results indicate that watermarks embedded by Easymark can be reliably detected
withoutreducingtheBLEUscoreorincreasingperplexityofthetext,surpassingexistingadvancedtechniquesintermsofbothqualityandwatermarkreliability.
27

<!-- Page 28 -->

SynonymSubstitution-BasedMethods.Inlightofthevulnerabilityofcharacter-levelmethods to targeted attacks, some research has shifted towards embedding watermarks
at the word level, mainly through synonym substitution. Early watermark embedding schemes involve the continuous replacement of words with synonyms until the
text carries the intended watermark content. To address this, Topkara, Topkara, and
Atallah (2006) introduced a quantifiable and resilient watermarking technique using
Wordnet (Fellbaum 1998). Building upon this, Yang et al. (2022); Munyer and Zhong
(2023); Yoo et al. (2023) employed pre-trained or further fine-tuned neural models to
performwordreplacementanddetectiontasks,therebybetterpreservingthesemantic
integrity of the original sentences. Additionally, Yang et al. (2023a) defined a binary
encodingfunctiontocalculaterandombinarycodescorrespondingtowords,andselectively replaced words representing a binary ”0“ with contextually relevant synonyms
representing a binary ”1“, effectively embedding the watermark. Experiments have
demonstrated that this method ensures the watermark’s robustness against attacks
suchasretranslation,textpolishing,worddeletion,andsynonymsubstitutionwithout
compromisingtheoriginaltext’ssemantics.
Sequence-to-Sequence Methods. Recent research has explored end-to-end watermark encryptiontechniqueswiththegoalofenhancingflexibilityandreducingthepresenceof
artifactsintroducedbywatermarks.Forinstance,AbdelnabiandFritz(2021)proposed
AdversarialWatermarkTransformer(AWT),thefirstframeworktoautomatethelearning of word replacements and their contents for watermark embedding. This method
combines end-to-end and adversarial training, capable of injecting binary messages
into designated input text at the encoding layer, producing an output text that is unnoticeableandminimallyaltersthesemanticsandcorrectnessoftheinput.Themethod
employs a transformer encoder layer to extract secret messages embedded within the
text. Similarly, Zhang et al. (2023a) introduced the REMARK-LLM framework, which
includesthreecomponents:(i)amessageencodingmodulethatinjectsbinarysignatures
into texts generated by LLMs; (ii) a reparametrization module that converts the dense
distributionofmessageencodingintoasparsedistributionforgeneratingwatermarked
text tokens; (iii) a decoding module dedicated to extracting signatures. Experiments
suggest that REMARK-LLM embeds more signature bits into the same text while
maintainingsemanticintegrityandshowingenhancedresistancetovariouswatermark
removalanddetectionattackscomparedtoAWT.
Comparedtomodel-drivenwatermarking,post-processingwatermarkingmaydependmoreheavilyonspecificrules,makingitmorevulnerabletosophisticatedattacks
thatexploitvisibleclues.Despitethisrisk,post-processingwatermarkinghassignificant
potential for various applications. Many existing watermarking techniques typically
necessitate training within white-box models, making them unsuitable for use with
black-box LLMs setting. For instance, embedding watermarks in GPT-4 is nearly impossible given its proprietary and closed-source nature. Nevertheless, post-processing
watermarking provides a solution for adding watermarks to text generated by blackboxLLMs,enablingthirdpartiestoembedwatermarksindependently.
5.2Statistics-BasedMethods
Within the statistics-based setup, this subsection presents methods for proficiently
identifying text generated by LLMs using detectors, without the need for additional
trainingthroughsupervisedsignals.ThisapproachassumesaccesstoLLMsorextract
28

<!-- Page 29 -->


### Wuetal. ASurveyonLLM-GeneratedTextDetection

features from text, and is evaluated based on unique features and statistical data to
derivestatisticalregularities(e.g.,computethresholds).
5.2.1LinguisticsFeaturesStatistics.Theinceptionofstatistics-baseddetectionresearch
can be traced back to the pioneering work of Corston-Oliver, Gamon, and Brockett
(2001). In this foundational study, the authors utilized linguistic features, such as the
branchingpropertiesobservedingrammaticalanalysesoftext,functionworddensity,
andconstituentlength,todeterminewhetheragiventextwasgeneratedbyamachine
translation model. These features served as key indicators in distinguishing machinegeneratedtextfromhuman-generatedtext.
Another notable method, dedicated to achieving similar detection objectives, employsfrequencystatistics.Forinstance,Kalinichenkoetal.(2003)utilizedthefrequency
statistics associated with word pairs present in the text as a mechanism to ascertain
whether the text had been autonomously generated by a generative system. Furthermore,theapproachadoptedbyBaayen(2001)isgroundedinthedistributionalfeatures
characteristic of words. Progressing in this line of inquiry, Arase and Zhou (2013)
latercontributedbydevelopingadetectiontechniquethatcapturesthe“phrasesalad”
phenomenonwithinsentences.
Recent studies on LLM generated text detection have proposed methodologies
based on linguistics features statistics. Gallé et al. (2021) proposed a method of using
repeated high-order n-grams to detect LLM-generated documents. This approach is
predicatedontheobservationthatcertainn-gramsrecurwithunusualfrequencywithin
LLM-generated text, a phenomenon that has been documented extensively. Similarly,
Hamed and Wu (2023) developed a detection system based on statistical similarities
of bigrams. Their findings indicate that only 23% of bigrams in texts generated by
ChatGPTareunique,underscoringsignificantdisparitiesinterminologyusagebetween
human and LLM-generated content. Impressively, their algorithm successfully identified98of100LLM-writtenacademicpapers,therebydemonstratingtheefficacyoftheir
featureengineeringapproachindistinguishingLLM-generatedtexts.
However, our empirical observations reveal a conspicuous limitation in the applicationoflinguisticfeaturestatistics:theavailabilityofthesemethodsreliesheavilyon
extensivecorpusstatisticsandvarioustypesofLLMs.
5.2.2 White-Box Statistics. Currently, white-box methods for detecting text generated
by LLMs require direct access to the source model for implementation. The existing
white-box detection techniques primarily use zero-shot approaches, which involves
obtaining the model’s logits output and calculating specific metrics. These metrics are
thencomparedagainstpredeterminedthresholdsobtainedthroughstatisticalmethods
toidentifyLLM-generatedtext.
Logits-BasedStatistics.LogitsaretherawoutputsproducedbyLLMsduringtextgeneration, specifically from the model’s final linear layer, which is typically located before
the softmax function. These outputs indicate the model’s confidence levels associated
with generating each potential subsequent word. The Log-Likelihood (Solaiman et al.
2019), a metric derived directly from the logits, measures the average token-wise log
probabilityforeachtokenwithintheprovidedtextbyconsultingtheoriginatingLLM.
Thismeasurementhelpstodeterminethelikelihoodofthetextbeinggeneratedbyan
LLM.Atpresent,theLog-Likelihoodisrecognizedasoneofthemostpopularbaseline
metricsforLLM-generatedtextdetectiontask.
29

<!-- Page 30 -->

Similarly, Rank (Solaiman et al. 2019) is another normal baseline computed from
logits. The Rank metric calculates the ranking of each word in a sample within the
model’soutputprobabilitydistribution.Thisrankingisdeterminedbycomparingthe
logitscoreofthewordagainstthelogitscoresofallotherpossiblewords.Iftheaverage
rankofeachwordinthesampleishigh,itsuggeststhatthesampleislikelygenerated
by LLMs. Log-Rank, on the other hand, further processes each token’s rank value by
applyingalogarithmicfunctionandhasgarneredincreasingattention.Onenoteworthy
methodbasedonthisintuitiveapproachisGLTR(Gehrmann,Strobelt,andRush2019),
whichisdesignedasavisualforensictooltofacilitatecomparativejudgment.Thetool
dividesdifferentmarkingcolorsaccordingtothesamplingfrequencylevelofthetoken,
and highlights the proportion of words that LLMs tend to use in the analyzed text by
markingdifferentcolorsforthetokensthatprovidethetext.TheLog-LikelihoodRatio
Ranking(LRR)proposedbySuetal.(2023a)combinesLog-LikelihoodandLog-Rankby
takingtheratioofthetwometrics.Thisapproachenhancesperformancebyeffectively
complementingLogLikelihoodassessmentswithLogRankanalysistoprovideamore
comprehensiveassessment.
Entropy represents another early zero-shot method used for evaluating LLM-
generated text. It is typically employed to measure the uncertainty or the amount of
information in a text or model output, and is also calculated through the probability
distribution of words. High entropy indicates that the content of the sample text is
unclear or highly diversified, meaning that many words have a similar probability of
being chosen. In such cases, the sample is likely to have been generated by an LLM.
Lavergne, Urvoy, and Yvon (2008) employed the Kullback-Leibler (KL) divergence to
assign scores to n-grams, taking into account the semantic relationships between their
initialandfinalwords.Thisapproachidentifiesn-gramswithsignificantdependencies
betweentheinitialandterminalwords,thusaidinginthedetectionofspuriouscontent
andenhancingtheoverallperformanceofthedetectionprocess.
Themethodemployingperplexity,groundedintraditionaln-gramLMs,evaluates
the proficiency of LMs at predicting text (Beresneva 2016). More recent work, such as
HowkGPT (Vasilatos et al. 2023), discerns LLM-generated text, specifically homework
assignments, by calculating and comparing perplexity scores derived from studentwritten and ChatGPT-generated text. Through this comparison, thresholds are establishedtoidentifytheoriginofsubmittedassignmentsaccurately.Moreover,thewidely
recognized GPTZero14 estimates the likelihood of a review text being generated by
LLMs. This estimation is based on a meticulous examination of the text’s perplexity
and burstiness metrics. In a recent study, Wu et al. (2023) unveiled LLMDet, a tool
designedtoquantifyandcataloguetheperplexityscoresattributabletovariousmodels
forselectedn-gramsbycomputingtheirnext-tokenprobabilities.LLMDetexploitsthe
intrinsicself-watermarkingcharacteristicsoftext,asevidencedbyproxyperplexity,to
trace the source of the text and to detefct it accordingly. The tool demonstrates a high
classificationaccuracyof98.54%,whilealsoofferingcomputationalefficiencycompared
to fine-tuned RoBERTa. In addition, Venkatraman, Uchendu, and Lee (2023) extract
UID-based features by analyzing the token probabilities of articles and then trains a
logisticregressionclassifiertofittheUIDcharacteristicsoftextsgeneratedbydifferent
LLMs,inordertoidentifytheoriginsofthetexts.GHOSTBUSTER(Vermaetal.2023)
inputstextgeneratedbyLLMsintoaseriesofweakerlanguagemodelstoobtaintoken
probabilities,andthenconductsastructuredsearchonthecombinationsofthesemodel
14 https://gptzero.me/
30

<!-- Page 31 -->


### Wuetal. ASurveyonLLM-GeneratedTextDetection

outputstotrainalinearclassifierfordistinguishingLLM-generatedtexts.Thisdetector
achievesanaverageF1scoreof99.0,whichisanincreaseof41.6F1scoreoverprevious
methodssuchasGPTZeroandDetectGPT.
Perturbed-Based Methods. Some white-box statistical (or zero-shot) approaches detect
LLM-generated text by comparing the differences in performance metrics after statisticalperturbation.Mitchelletal.(2023)proposedamethodtoidentifytextproducedby
LLMsbyanalyzingstructuralpatternsintheLLMs’probabilityfunctions,specificallyin
regionsofnegativecurvature.ThepremiseisthatLLM-generatedtexttendstocluster
atlocallog-probabilitymaxima.Detectioninvolvescomparinglog-probabilitiesoftext
against those from the target LLM, using a pre-trained mask-filling model like T5 to
createsemanticallysimilartextperturbations.
Whileinnovativeandsometimesmoreeffectivethansupervisedmethods,Detect-
GPThaslimitations,includingpotentialperformancedropsifrewritesdon’tadequately
representthespaceofmeaningfulalternatives,andhighcomputationaldemands,asit
needstoscoremanytextperturbations.Inresponsetothischallenge,Dengetal.(2023)
proposed a method that uses a Bayesian surrogate model to select a small number
of typical samples for scoring. By interpolating the scores of typical samples to other
samples to improve query efficiency, the overhead is reduced by half while maintaining performance. Bao et al. (2023) reported a method that replaces the perturbation
step of DetectGPT with a more efficient sampling step, significantly improving the
detection accuracy by about 75% and increasing the detection speed by 340 times.
UnlikeDetectGPT,thewhite-boxconfigurationinDNA-GPT(Yangetal.2023b)utilizes
large language models such as ChatGPT to continue writing truncated texts instead
of employing perturbation settings. It analyzes the differences between the original
textandthecontinuedtextbycalculatingprobabilitydivergence,achievingadetection
performance close to 100%. DetectLLM (Su et al. 2023a), another recent contribution,
parallels the conceptual framework of DetectGPT. It employs normalized perturbed
log-rank for text detection generated by LLMs, asserting a lower susceptibility to the
perturbationmodelandthenumberofperturbationscomparedtoDetectGPT.
IntrinsicDimensionEstimation.ThestudyconductedbyTulchinskiietal.(2023)posited
the invariant nature of the competencies exhibited by both human and LLMs within
their respective textual domains. The proposed approach involves the construction of
detectorsutilizingtheintrinsicdimensionsofmanifoldsunderpinningtheembedding
set of given text samples. More specifically, the methodology entails computing the
averageintrinsicdimensionalityvaluesforbothsetsoffluenthuman-writtentextsand
LLM-generated texts in the target natural language. The ensuing statistical separation
between these two sets facilitates the establishment of a separation threshold for the
targetlanguage,therebyenablingthedetectionoftextgeneratedbyLLMs.Itisimperativetoacknowledgetherobustnessofthisapproachacrossvariousscenarios,including
cross-domainchallenges,modelshifts,andadversarialattacks.However,itsreliability
falterswhenconfrontedwithsuboptimalorhigh-temperaturegenerators.
5.2.3 Black-Box Statistics. Unlike white-box statistical methods, black-box statistical
methods utilize a black-box model to calculate specific feature scores of a text without needing access to the logits of the source or surrogate model. Yang et al. (2023b)
employedLLMstocontinuewritingtruncatedtextsunderreviewanddefinedhumanwritten versus LLM-generated texts by calculating the n-gram similarity between the
31

<!-- Page 32 -->

continuation and the original text. Similarly, Mao et al. (2024) and Zhu et al. (2023)
identifiedLLM-generatedtextsbycomputingthesimilarityscoresbetweentheoriginal
textsandtheirrewrittenandrevisedversions.Theseapproachesarebasedontheobservationthat human-writtentextstend totriggermore revisionswhenLLMs aretasked
with rewriting and editing than LLM-generated texts. Yu et al. (2023b) introduced a
detection mechanism that also capitalizes on the similarity between the original text
andtheregeneratedtext.Differingfromothermethods,thisapproachinitiallyidentifies
theoriginalquestionthatpromptedthegenerationofthetextandregeneratesthetext
based on this inferred question. Additionally, (Quidwai, Li, and Dube 2023) analyzes
sentences from LLM-generated texts and their paraphrases, distinguishing them from
human-written texts by calculating cosine similarity, achieving an accuracy of up to
94%. Guo and Yu (2023) introduced a denoising-based black-box zero-shot statistics
methodthatemploysablack-boxLLMtodenoiseartificiallyaddednoisetoinputtexts.
Thedenoisedtextsarethensemanticallycomparedtotheoriginaltexts,resultinginan
AUROCscoreof91.8%.
However,theapproachesofblack-boxstatisticsarenotwithoutchallenges,includingthesubstantialoverheadofaccessingtheLLMandlongresponsetimes.
5.3Neural-BasedMethods
5.3.1Features-BasedClassifiers.
LinguisticFeatures-Basedclassifiers.WhencomparingtextsgeneratedbyLLMswiththose
writtenbyhumans,thedifferencesinnumerouslinguisticfeaturesprovideasolidbasis
for feature-based classifiers to effectively distinguish between them. The workflow of
such classifiers typically starts with the extraction of key statistical language features,
followed by the application of machine learning techniques to train a classification
model. This approach has been widely used in the identification of fake news. For
instance,intherecentstudy,Aich,Bhattacharya,andParde(2022)achievedanimpressiveaccuracyof97%byextracting21textualfeaturesandemployingaKNNclassifier.
Drawing inspiration from the tasks of detecting fake news and LLM-generated texts,
the linguistic features of texts can be extensively categorized into stylistic features,
complexity features, semantic features, psychological features, and knowledge-based
features.Thesefeaturesareprimarilyobtainedthroughstatisticalmethods.
Stylistic Features primarily focus on the frequency of words that can highlight
the stylistic elements of the text, including the frequency of capitalized words, proper
nouns, verbs, past tense words, stopwords, technical words, quotes, and punctuation
(HorneandAdali2017).ComplexityFeaturesareextractedtoshowcasethecomplexity
of the text, such as the type-token ratio (TTR) and textual lexical diversity (MTLD)
(McCarthy 2005). Semantic Features includes Advanced Semantic (AdSem), Lexico
Semantic (LxSem), and statistics of semantic dependency tags, among other semanticlevelfeatures.ThesecanbeextractedusingtoolslikeLingFeat(Lee,Jang,andLee2021).
Psychological Features generally related to sentiment analysis, these can be based on
toolslikeSentiWordNet(Baccianella,Esuli,andSebastiani2010)tocalculatesentiment
scores or extracted using sentiment classifiers. Information Features include named
entities (NE), opinions (OP), and entity relation extraction (RE), and can be extracted
usingtoolssuchasUIE(Luetal.2022)andCogIE(Jinetal.2021).
Shahetal.(2023)constructedaclassifierbasedonstylisticfeaturessuchassyllable
count,wordlength,sentencestructure,frequencyoffunctionwordusage,andpunctuationratio.Thisclassifierachievedanaccuracyof93%,whicheffectivelydemonstrates
the significance of stylistic features for LLM-generated text detection. Other work in-
32

<!-- Page 33 -->


### Wuetal. ASurveyonLLM-GeneratedTextDetection

tegrated text modeling with a variety of linguistic features through data fusion techniques(CorizzoandLeal-Arenas2023),whichincludeddifferenttypesofpunctuation
marks,theuseoftheOxfordcomma,paragraphstructures,averagesentencelength,the
repetitivenessofhigh-frequencywords,andsentimentscores.OnEnglishandSpanish
datasets,thisapproachachievedF1-Scoresof98.36%and98.29%respectively,indicating
its exceptional performance. Mindner, Schlippe, and Schaaff (2023) further employed
a multidimensional approach to enhance the classifier’s discriminative power, which
included complexity measures, semantic analysis, list searches, error-based features,
readability assessments, artificial intelligence feedback, and text vector features. Ultimately, the optimized detector’s performance exceeded that of GPTZero by 183.8% in
F1Score,showcasingitssuperiordetectioncapabilities.
Although classifiers based on linguistic features have their advantages in distinguishing between human and AI-generated texts, their shortcomings cannot be overlooked. The results from (Schaaff, Schlippe, and Mindner 2023) indicate that such
feature classifiers have poor robustness against ambiguous semantics and often underperform neural network features. Moreover, classifiers based on stylistic features
maybecapableofdifferentiatingbetweentextswrittenbyhumansandthosegenerated
by LLMs, but their ability to detect LLM-generated misinformation is limited. This
limitation is highlighted in (Schuster et al. 2020a), which shows that language models
tend to produce stylistically consistent texts. However, Crothers et al. (2022) suggests
that statistical features can offer additional adversarial robustness and can be utilized
inconstructingintegrateddetectionmodels.
Model Features-Based Classifiers. In addition to linguistic features, classifiers based on
model features have recently garnered considerable attention from researchers. These
classifiers are not only capable of detecting texts generated by LLMs but can also
be employed for text provenance tracing. Sniffer (Li et al. 2023a) involves extracting
alignedtoken-levelperplexityandcontrastivefeatures,whichmeasurethepercentage
ofwordswithlowerperplexitywhencomparingonemodelθ withanothermodelθ .
i j
Bytrainingalinearclassifierwiththesefeatures,anaccuracyof86.0%wasachieved.SeqXGPT(Wangetal.2023a)representsfurtherexplorationinthefieldoftextprovenance
tracing, building on the proposed features to design a context network that combines
aCNNwithatwo-layertransformerforencodingtexts,anddetectingLLM-generated
texts through a sequence tagging task. Research in (Wu and Xiang 2023) considers a
combinationoffeaturessuchasloglikelihood,logrank,entropy,andLLMbias,andby
traininganeuralnetworkclassifier,itachievedanaverageF1scoreof98.41%.However,
a common drawback of these methods is that they all require access to the source
model’s logits. For other powerful closed-source models where logits are inaccessible,
thesemethodsmaystruggletobeeffective.
5.3.2Pre-TrainingClassifiers.
In-domain Fine-tuning is All You Need. Within this subsection, we explore methods that
involvefine-tuningTransformer-basedLMstodiscriminatebetweeninputtextsthatare
generatedbyLLMsandthosethatarenot.Thisapproachrequirespairedsamplesforthe
facilitationofsupervisedtrainingprocesses.Accordingto(Qiuetal.2020),pre-trained
LMshaveproventobepowerfulinnaturallanguageunderstanding,whichiscrucialfor
enhancingvarioustasksinNLP,withtextcategorizationbeingparticularlynoteworthy.
Esteemed pre-trained models, such as BERT (Devlin et al. 2019a), Roberta (Liu et al.
33

<!-- Page 34 -->

2019), and XLNet (Yang et al. 2019), have exhibited superior performance relative to
their counterparts in traditional statistical machine learning and deep learning when
appliedtothetextcategorizationtaskswithintheGLUEbenchmark(Wangetal.2019).
Moreover, there is an extensive body of prior work (Bakhtin et al. 2019; Uchendu
etal.2020;Antounetal.2023a;Lietal.2023c)thathasmeticulouslyexaminedthecapabilitiesoffine-tunedLMsindetectingLLM-generatedtext.Notably,studiesconducted
in2019haveacknowledgedfine-tunedLMs,withRoberta(Liuetal.2019)beingespecially prominent, as being amongst the most formidable detectors of LLM-generated
text.Inthefollowingdiscourse,wewillintroducerecentscholarlycontributionsinthis
vein,providinganupdatedreviewandsummaryofthemethodsdeployed.
Fine-tuning Roberta provides a robust baseline for detecting text generated by
LLMs.Fagnietal.(2021)observedthatfine-tuningRobertaledtooptimalclassification
outcomesinvariousencodingconfigurations(Gambinietal.2022),withthesubsequent
OpenAI detector (Radford et al. 2019) also adopting a Roberta fine-tuning approach.
Recentworks(Guoetal.2023;Liuetal.2023c,d;Chenetal.2023b;Wangetal.2023c,c)
further corroborated the superior performance of fine-tuned members of the BERT
family, such as RoBERTa, in identifying LLM-generated text. On average, these finetunedmodelsyieldeda95%accuracyratewithintheirrespectivedomains,outperforming zero-shot and watermarking methods, and exhibiting a modicum of resilience to
various attack techniques within in-domain settings. Nevertheless, like their counterparts,theseencoder-basedfine-tuningapproacheslackrobustness(Bakhtinetal.2019;
Uchendu et al. 2020; Antoun et al. 2023a; Li et al. 2023c), as they tend to overfit to
theirtrainingdataorthesourcemodel’strainingdistribution,resultinginadeclinein
performance when faced with cross-domain or unseen data. Additionally, fine-tuning
LMsclassifiersislimitedinfacingdatageneratedbydifferentmodels(Sarvazyanetal.
2023a).Despitethis,detectorsbasedonRoBERTaexhibitsignificantpotentialforrobustness,requiringasfewasafewhundredlabelstofine-tuneanddeliverimpressiveresults
(Rodriguez et al. 2022b). mBERT (Devlin et al. 2019b) has demonstrated consistently
robust performance in document-level LLM-generated text classification and various
model attribution settings, maintaining optimal performance particularly in English
and Spanish tasks. In contrast, encoder models like XLM-RoBERTa (Conneau et al.
2020) and TinyBERT (Jiao et al. 2020) have shown significant performance disparities
in the same document-level tasks and model attribution setups, suggesting that these
twotasksmayrequiredifferentcapabilitiesfromthemodels.
ContrastiveLearning.Datascarcityhaspropelledtheapplicationofcontrastivelearning
(Yanetal.2021;Gao,Yao,andChen2021;Chenetal.2022)toLM-basedclassifiers,with
the core of this approach being self-supervised learning. This strategy minimizes the
distance between the anchor and positive samples while maximizing the distance to
negative samples through spatial transformations. An enhanced contrastive loss, proposedbyLiuetal.(2022),assignsgreaterweighttohard-negativesamples,therebyoptimizingmodelutilityandstimulationtobolsterperformanceinlow-resourcecontexts.
Thismethodthoroughlyaccountsforlinguisticcharacteristicsandsentencestructures,
representing text as a coherence graph to encapsulate its inherent entity consistency.
Research findings affirm the potency of incorporating information fact structures to
refine LM-based detectors’ efficacy, a conclusion echoed by Zhong et al. (2020). Bhattacharjee et al. (2023) proposed ConDA, a contrastive domain adaptation framework,
which combines standard domain adaptation technology with the representation capabilities of contrastive learning, greatly improving the model’s defense capabilities
againstunknownmodels.
34

<!-- Page 35 -->


### Wuetal. ASurveyonLLM-GeneratedTextDetection

AdversarialLearningMethods.Inlightofthevulnerabilityofdetectorstodifferentattacks
and robustness issues, a significant body of scholarly research has been dedicated
to utilizing adversarial learning as a mitigation strategy. Predominantly, adversarial
learningmethodsbearrelevancetofine-tuningLMsmethods.Noteworthyrecentwork
byKoike,Kaneko,andOkazaki(2023b)revealedthatitisfeasibletotrainadversarially
withoutfine-tuningthemodel,withcontextservingasaguidefortheparameter-frozen
model. We compartmentalize the studies into two categories: Sample Enhancement
BasedAdversarialTrainingandTwo-PlayerGames.
A prominent approach within Sample Enhancement Based Adversarial Training
centersondeployingadversarialattackspredicatedonsampleaugmentation,withthe
overarching aim of crafting deceptive inputs to thereby enhance the model’s competencyinaddressingabroaderarrayofscenariosthatbeardeceptionpotential.Specifically,thismethodemphasizestheimportanceofsampleaugmentationandachievesit
byinjectingpredeterminedadversarialattacks.Thisaugmentationprocessisintegralto
fortifying the detector’s robustness by furnishing it with an expanded pool of adversarial samples. Section 7.2 of the article outlines various potential attack mechanisms,
includingparaphraseattacks,adversarialattacks,andpromptattacks.Yang,Jiang,and
Li(2023);Shietal.(2023);Heetal.(2023)conductedtheadversarialdataaugmentation
process on LLM-generated text, the findings of which indicated that models trained
onmeticulouslyaugmenteddataexhibitedcommendablerobustnessagainstpotential
attacks.
ThemethodsofTwo-PlayerGamesfundamentallyalignedwiththeprinciplesunderpinningGenerativeAdversarialNetworks(Goodfellowetal.2020)andBreak-It-Fix-
Itstrategies(YasunagaandLiang2021),typicallyinvolvetheconfigurationofanattack
model alongside a detection model, with the iterative confrontation between the two
culminatinginenhanceddetectioncapabilities.Hu,Chen,andHo(2023)introduceda
framework,RADAR,envisagedfortheconcurrenttrainingofrobustdetectorsthrough
adversarial learning. This framework facilitates interaction between a paraphrasing
model,responsibleforgeneratingrealisticcontentthatevadesdetection,andadetector
whosegoalistoenhanceitscapabilitytoidentifytextproducedbyLLMs.TheRADAR
frameworkincrementallyrefinestheparaphrasemodel,drawingonfeedbackgarnered
fromthedetectorandemployingPPO(Schulmanetal.2017b).Despiteitscommendable
performance in countering paraphrase attacks, the study by Hu, Chen, and Ho (2023)
did not provide a comprehensive analysis of RADAR’s defense mechanism against
otherattackmodalities.Inaparallelvein,Koike,Kaneko,andOkazaki(2023b)proposed
atrainingmethodologyfordetectors,predicatedonacontinualinteractionbetweenan
attackerandadetector.DistinctfromRADAR,OUTFOXallocatesgreateremphasison
thelikelihoodofdetectorsemployingICL(Dongetal.2023)forattackeridentification.
Specifically, the attacker in the OUTFOX framework utilizes predicted labels from the
detectorasICLexemplarstogeneratetextthatposesdetectionchallenges.Conversely,
the detector uses the content generated adversarially as ICL exemplars to enhance
its detection capabilities against formidable attackers. This reciprocal consideration of
each other’s outputs fosters improved robustness in detectors for text generated by
LLMs.EmpiricalevidenceatteststothesuperiorperformanceoftheOUTFOXmethod
relative to preceding statistical methods and those based on RoBERTa, particularly in
respondingtoattacksfromTF-IDFandDIPPER(Krishnaetal.2023).
Features-Enhanced Approaches. In addition to enhancements in training methodology,
Tu et al. (2023) demonstrated that the extraction of linguistic features can effectively
35

<!-- Page 36 -->

improve the robustness of a RoBERTa-based detector, with benefits observed in various related models. Cowap, Graham, and Foster (2023) developed an emotion-aware
detector by fine-tuning a Pre-trained Language Model (PLM) for sentiment analysis,
thereby enhancing the potential of emotion as a signal for identifying synthetic text.
Theyachievedthisbyfurtherfine-tuningBERTspecificallyforsentimentclassification,
resulting in a detection performance F1 score improvement of up to 9.03%. Uchendu,
Le,andLee(2023b)employedRoBERTatocapturecontextualrepresentations,suchas
semantic and syntactic linguistic features, and integrated Topological Data Analysis
to analyze the shape and structure of data, which includes linguistic structure. This
approach surpassed the performance of RoBERTa alone on the SynSciPass and M4
datasets.TheframeworkJ-Guard(Kumarageetal.2023a)guidesexistingsupervisedAI
textdetectorsindetectingAI-generatednewsbyextractingJournalismFeatures,which
help the detector recognize LLM-generated fake news text. This framework exhibits
strong robustness, maintaining an average performance decrease as low as 7% when
facedwithadversarialattacks.
5.3.3LLMsasDetectors.
Questionable Reliability of Using LLMs. Several works have examined the feasibility of
utilizing LLMs as detectors to discern text generated by either themselves or other
LLMs. This approach was first broached by Zellers et al. (2019b), wherein the text
generation model Grover (Zellers et al. 2019b) was noted to produce disinformation
that was remarkably deceptive due to its inherently controllable nature. Subsequent
exploratoryanalysesbyZellersetal.(2019b)engagingvariousarchitecturalmodelslike
GPT-2(Radfordetal.2019)andBERT(Devlinetal.2019c)revealedthatGrover’smost
effective countermeasure was Grover itself, boasting an accuracy rate of 92%, while
otherdetectortypesexperiencedadeclineinaccuracytoapproximately70%asGrover’s
size increased. A recent reevaluation conducted by Bhattacharjee and Liu (2023) on
morerecentLLMslikeChatGPTandGPT-4yieldedthatneithercouldreliablyidentify
text generated by various LLMs. During the observations, it was noted that ChatGPT
and GPT-4 exhibited contrasting tendencies. ChatGPT tended classify text generated
byLLMsasifitwerewrittenbyhumans,withamisclassificationprobabilityofabout
50%. While GPT-4 leaned towards labeling human-written text as if it were generated
by LLMs, and about 95% of human-written texts are misclassified as LLM-generated
texts. ArguGPT (Liu et al. 2023c) further attested to the lackluster performance of
GPT-4-Turbo in detecting text generated by LLMs, with accuracy rates languishing
below50%acrosszero-shot,one-shot,andtwo-shotsettings.Thesefindingscollectively
demonstrate the diminishing reliability of employing LLMs for direct self-generated
textdetection,particularlywhencomparedtostatisticalandneuralnetworkmethods.
ThisisparticularlyevidentinlightoftheincreasingcomplexityofLLMs.
ICL: A Powerful Technique for LLM-Based Detection. Despite the unreliability issues associatedwithusingLLMsfordirectdetectionofLLM-generatedtext,recentempirical
investigations highlight the potential efficacy of ICL in augmenting LLMs’ detection
capabilities. ICL, a specialized form of cue engineering, integrates examples into cues
providedtothemodel,therebyfacilitatingthelearningofnewtasksbyLLMs.Through
ICL, existing LLMs can adeptly tackle different tasks without necessitating additional
fine-tuning. The OUTFOX Detector (Koike, Kaneko, and Okazaki 2023b) employs an
ICL approach, continuously supplying example samples to LLMs for text generation
36

<!-- Page 37 -->


### Wuetal. ASurveyonLLM-GeneratedTextDetection

detection tasks. The experimental findings demonstrate that the ICL strategy outperformsbothtraditionalzero-shotmethodsandRoBERTa-baseddetectors.
5.4Human-AssistedMethods
In this section, we delve into human-assisted methods for detecting text generated by
LLMs.Thesemethodsleveragehumanpriorknowledgeandanalyticalskills,providing
notableinterpretabilityandcredibilityinthedetectionprocess.
5.4.1IntuitiveIndicators.Severalstudieshavedelvedintothedisparitiesbetweenhumanandmachineclassificationcapabilities.Humanclassificationprimarilydependson
visualobservationtodiscernfeaturesindicativeoftextgenerationbyLLMs.Uchendu
etal.(2023)notedthatalackofcoherenceandconsistencyinLLM-generatedtextserves
asastrongindicatoroffalsifiedcontent.TextsproducedbyLLMsoftenexhibitsemantic
inconsistencies and logical errors. Furthermore, Dugan et al. (2023) identified that the
human discernment of LLM-generated text varies across different domains. For instance,LLMstendtogeneratemore“generic”textinthenewsdomain,whereas,instory
domains,thetextmightbemore“irrelevant”.Maetal.(2023)notedthatevaluatorsof
academicwritingtypicallyemphasizestyle.SummariesgeneratedbyLLMsoftenlack
detail,particularlyindescribingtheresearchmotivationandmethodology,whichhampers the provision of fresh insights. In contrast, LLM-generated papers exhibit fewer
grammaticalandothertypesoferrorsanddemonstrateabroadervarietyofexpression
(Yanetal.2023;Liaoetal.2023a).However,thesepaperscommonlyusegeneralterms
instead of effectively tailored information pertinent to the specific problem context. In
human-writtentexts,suchasscientificpapers,authorsarepronetocomposinglengthy
paragraphs and using ambiguous language (Desaire et al. 2023), often incorporating
termslike“but,”“however,”and“although.”Duganetal.(2023)alsonotedthatrelying
solely on grammatical errors as a detection strategy is unreliable. In addition, LLMs
frequently commit factual and common-sense reasoning errors, which, while often
overlookedbyneuralnetwork-baseddetectors,areeasilynoticedbyhumans(Jawahar,
Abdul-Mageed,andLakshmanan2020).
5.4.2ImperceptibleFeatures.Ippolitoetal.(2020)suggestedthattextperceivedashigh
qualitybyhumanstendstobemoreeasilyrecognizablebydetectors.Thisobservation
implies that some features, imperceptible to humans, can be efficiently captured by
detection algorithms. While humans are adept at identifying errors in many LLM-
generated texts, unseen features also significantly inform human decision-making. In
contrast, statistical thresholds commonly employed in zero-shot Detector research to
distinguish LLM-generated text can be manipulated. However, humans typically possesstheabilitytodetectsuchmanipulationsthroughvariousmetrics,GLTR(Gehrmann,
Strobelt, and Rush 2019) pioneered this approach, serving as a visual forensic tool to
assisthumanvettingprocesses,whilealsoprovidingrichinterpretationseasilyunderstandablebynon-experts(Clarketal.2021b).
5.4.3 Enhancing Human Detection Capabilities. Recent studies (Ippolito et al. 2020)
indicated that human evaluators might not be as proficient as detection algorithms
in recognizing LLM-generated text across various settings. However, exposing evaluators to examples before evaluation enhances their detection capabilities, especially
with longer samples. The platform RoFT (Dugan et al. 2020) allows users to engage
withLLM-generatedtext,sheddinglightonhumanperceptionofsuchtext.Although
37

<!-- Page 38 -->

revealingtrueboundariespost-annotationdidnotleadtoanimmediateimprovement
in annotator accuracy, it is worth noting that with proper incentives and motivations,
annotators can indeed improve their performance over time (Dugan et al. 2023). The
SCARECROW framework (Dou et al. 2022) facilitates the annotation and review of
LLM-generated text, outlining ten error types to guide users. The result from SCARE-
CROWreportsManualannotationoutperformeddetectionmodelsonhalfoftheerror
types,suggestingpotentialindevelopingefficientannotationsystemsdespitetheassociatedhumanoverhead.
5.4.4MixedDetection:UnderstandingandExplanation.Wengetal.(2023)introduced
aprototypeamalgamatinghumanexpertiseandmachineintelligenceforvisualanalysis,premisedonthebeliefthathumanjudgmentisthebenchmark.Initially,expertslabel
text based on their prior knowledge, elucidating the distinctions between human and
LLM-generatedtext.Subsequently,machine-learningmodelsaretrainedanditeratively
refinedbasedonlabeleddata.Finally,themostintuitivedetectorisselectedthroughvisualstatisticalanalysis,servingthedetectionpurpose.Thisgranularanalysisapproach
notonlybolstersexperts’trustindecision-makingmodelsbutalsofosterslearningfrom
themodels’behaviortoefficientlyidentifyLLM-generatedsamples.

## EvaluationMetrics

Evaluation metrics, indispensable for the assessment of model performance within
any NLP task, warrant meticulous consideration. In this section, we enumerate and
discuss metrics conventionally utilized in the tasks of LLM-generated text detection.
ThesemetricsincludeAccuracy,PairedAccuracy,UnpairedAccuracy,Recall,HumanwrittenRecall(HumanRec),LLM-generatedRecall(LLMRec),AverageRecall(AvgRec),
F1Score,andAreaUndertheReceiverOperatingCharacteristicCurve(AUROC).Furthermore, we discuss the advantages and drawbacks associated with each metric to
facilitateinformedmetricselectionforvariedresearchscenariosinsubsequentstudies.
Theconfusionmatrixcanhelpeffectivelyevaluatetheperformanceoftheclassificationtaskanddescribesallpossibleresults(fourtypesintotal)oftheLLM-generated
textdetectiontask:
• TruePositive(TP)referstotheresultofthepositivecategory
(LLM-generatetext)correctlyclassifiedbythemodel.
• TrueNegative(TN)referstotheresultofthenegativecategory
(human-writtentext)correctlyclassifiedbythemodel.
• FalsePositive(FP)referstotheresultofthepositivecategory
(LLM-generatetext)incorrectlyclassifiedbythemodel.
• FalseNegative(FN)referstotheresultofthenegativecategory
(human-writtentext)incorrectlypredictedbythemodel.
TheevaluationmetricsintroducedbelowcanallbedescribedbyTP,TN,FP,andFP.
Accuracy.Accuracyservesasageneralmetric,denotingtheratioofcorrectlyclassified
textstothe totaltextcount. Whilesuitableforbalanceddatasets, itsutilitydiminishes
forunbalancedonesduetosensitivitytocategoryimbalance.ThemetricsofPairedand
Unpaired Accuracy have also found application in (Zellers et al. 2019b; Zhong et al.
38

<!-- Page 39 -->


### Wuetal. ASurveyonLLM-GeneratedTextDetection

2020)toevaluatethedetector’sabilityindifferentscenarios.Intheunpairedsetting,the
discriminator must independently classify each test sample as human or machine. In
thepairedsetting,themodelisgiventwotestsampleswiththesamemetadata,onereal
andonegeneratedbythelargemodel.Thediscriminatormustassignahighermachine
probabilitytoarticleswrittenbylargemodelsthantoarticleswrittenbyhumans.These
indicators are used to measure the performance of the algorithm on data in different
scenarios. Relatively speaking, the detection difficulty of unpaired settings is higher
thanthatofpairedsettings.Accuracycanbedescribedbythefollowingformula:
correctlydetectedsamples

### Accuracy=

allsamples
(4)

## Tp +Tn

=

## Tp +Tn+Fp +Fn

Precision. Precision is a measure of the correctness of real predictions and refers to
theproportionofcorrectlydetectedLLM-generatedsamplesamongalldetectedLLM-
generated samples. This metric is very useful in situations where we are concerned
about false positives. When a sample is not LLM-generated, but is classified as LLM-
generated text, this erroneous result may reduce the user’s impression of the model
or even cause the negative impact on business. Therefore, improving precision is also
importantintheLLM-generatedtextdetectiontask.ThisMetriccanbedescribedbythe
followingformula:
correctlydetectedLLM-generatedsamples

### Precision=

alldetectedLLM-generatedsamples
(5)

## Tp

=

## Tp +Fp

Recall. Recall represents the proportion of actual machine-generated texts accurately
identifiedassuch.Thismetricisinvaluableincontextswhereunderreportingmustbe
minimized,asininstancesrequiringthecaptureofthemajorityofmachine-generated
texts.AvgRec,themeanrecallacrosscategories,isparticularlyusefulformulti-category
tasks requiring collective performance assessment across categories. HumanRec and
LLMRec denote the proportions of texts accurately classified as human-written and
machine-generated, respectively, shedding light on the model’s differential performanceonthesetwoclasses.Recall,HumanRec,LLMRec,andAvgReccanbedescribed
bythefollowingformulasrespectively:

## Tp

Recall= (6)

## Tp +Fn

correctlydetectedhuman-writtensamples

### HumanRecall= (7)

allhuman-writtensamples
correctlydetectedLLM-generatedsamples

### LLMRecall= (8)

allLLM-generatedsamples
HumanRecall+LLMRecall
AvgRecall= (9)
2
39

<!-- Page 40 -->

False Positive Rate (FPR). The FPR refers to the proportion of all actual human-written
samplesthatareincorrectlydetectedasLLM-generatedsamples.Thismetriccanmeasure the proportion of incorrect predictions made by the model in samples that are
actuallywrittenbyhumans.Ithelpstounderstandthefalsepositiverateofthemodel
and thus has a higher sensitivity for the detection of LLM-generated samples. This
metriccanbedescribedbythefollowingformula:
incorrectlydetectedLLM-generatedsamples

## Fpr=

allhuman-writtensamples
(10)

## Fp

=

## Fp +Tp

TrueNegativeRate(TNR).TheTNRreferstotheproportionofsamplesthatarecorrectly
detectedashuman-writtenamongallactualhuman-writtensamples.Thismetricmeasureshowaccuratelythemodelpredictshuman-writtensamples,butdoesnottakeinto
account the FPR, where text that is actually human-written is incorrectly detected as
LLM-generatedtext.Thismetriccanbedescribedbythefollowingformula:
correctlydetectedhuman-writtensamples

## Tnr=

allhuman-writtensamples
(11)

## Tn

=

## Tn+Fp

FalseNegativeRate(FNR).TheFNRreferstotheproportionofallactualLLM-generated
samples that are incorrectly detected as human-written. This metric helps understand
howmisinterpretedthemodelisforLLM-generatedtext.Thismetriccanbedescribed
bythefollowingformula:
incorrectlydetectedhuman-writtensamples

## Fnr=

allLLM-generatedsamples
(12)

## Fn

=

## Fn+Tp

F Score.TheF Scoreconstitutesaharmonicmeanofprecisionandrecall,integrating
1 1
considerations of false positives and false negatives. It emerges as a prudent choice
when a balance between precision and recall is imperative. The F score can be calcu-
1
latedusingthefollowingformula:
Precision∗Recall

## F =2∗

1 Precision+Recall
(13)

## 2Tp

=

## 2Tp +Fp +Fn

AUROC. The AUROC metric, derived from Receiver Operating Characteristic curves,
considers true and false positive rates at varying classification thresholds, proving
beneficial for evaluating classification efficacy at different thresholds. This is particularly crucial in scenarios necessitating specific false positive and miss rates, especially
withinthecontextofunbalanceddatasetsandbinaryclassificationtasks.Giventhatthe
detectionrateofzero-shotdetectionmethodssignificantlyhingesonthresholdvalues,
the AUROC metric is commonly employed to evaluate their performance across all
40

<!-- Page 41 -->


### Wuetal. ASurveyonLLM-GeneratedTextDetection

possiblethresholds.ThecalculationformulaofAUROCisasfollows:
(cid:90) 1 TP FP
AUROC = d (14)

## Tp +Fp Fp +Tn

0

## ImportantIssuesofLLM-generatedTextDetection

In this section, we discuss the main issues and limitations of contemporary SOTA
techniquesdesignedfordetectingtextgeneratedbyLLMs.Itisimportanttonotethat
no technique has been acknowledged as infallible. The issues elucidated herein may
pertainspecificallytooneormultipleclassesofdetectors.
7.1OutofDistributionChallenges
Out-of-distributionissuessignificantlyimpedetheefficacyofcurrenttechniquesdedicatedtothedetectionofLLM-generatedtext.Thissectionelucidatestheconstraintsof
thesedetectorstovariationsindomainsandlanguages.
Cross-domain.Thedilemmaofcross-domainapplicationisaubiquitouschallengeinherenttonumerousNLPtasks.StudiesconductedbyAntounetal.(2023a);Lietal.(2023c)
underscored considerable limitations in the performance of sophisticated detectors,
includingbutnotlimitedtoDetectGPT(Mitchelletal.2023),GLTR(Gehrmann,Strobelt,
and Rush 2019), and fine-tuned Roberta methods when applied to cross-domain data.
Thesedetectorsexhibitsubstantialperformancedegradationwhenconfrontedwithoutof-distributiondataprevalentinreal-worldscenarios,withtheefficacyofsomeclassifiers marginally surpassing that of random classification. This disparity between high
reported performance and actual reliability underlines the need for critical evaluation
andenhancementofexistingmethods.
Cross-lingual. The issue of cross-lingual application introduces a set of complex challengesthathindertheglobalapplicabilityofexistingdetectorresearch.Predominantly,
contemporarydetectorsdesignedforLLM-generatedtextprimarilytargetmonolingual
applications, often neglecting to evaluate and optimize performance across multiple
languages. Wang et al. (2023b) and Chaka (2023) noted the lack of control observed
in multilingual LLM-generated text detectors across various languages, despite the
existenceofcertainlanguagemigrationcapabilities.Weemphaticallydrawattentionto
thesecross-lingualchallengesasaddressingthemispivotalforenhancingtheusability
andfairnessofdetectorsforLLM-generatedtext.Moreover,recentresearch(Liangetal.
2023a) revealed a discernible decline in the performance of state-of-the-art detectors
when processingtexts authored bynon-native English speakers. Althoughemploying
effective prompt strategies can alleviate this bias, it also inadvertently allows the generated text to bypass the detectors. Consequently, there is a risk that detectors might
inadvertently penalize writers who exhibit non-standard linguistic styles or employ
limited expressions, thereby introducing issues of discrimination within the detection
process.
41

<!-- Page 42 -->

Cross-llms. Another significant out-of-distribution issue in the LLM-generated text detectiontaskisthecross-llmschallenge.Currentwhite-boxdetectionapproachesprimarilyrelyonaccessingthesourcemodelandcomparingfeaturessuchasLog-likelihood.
Consequently, white-box methods may underperform when encountering text generated by unknown LLMs. The results of DetectGPT (Mitchell et al. 2023) highlight the
vulnerability of white-box methods when dealing to unknown models, particularly
whenencounteringpowerfulmodelslikeGPT-3.5-Turbo.However,therecentfindings
fromFast-DetectGPT(Baoetal.2023)showthatstatisticalcomparisonswithsurrogate
models can significantly mitigate this issue. Additionally, identifying the type of the
generative model before applying white-box methods could be beneficial. In this regard, the methodologies of Siniff (Li et al. 2023a), SeqXGPT (Wang et al. 2023a), and
LLMDet (Wu et al. 2023) may provide useful insights. On the other hand, methods
based on neural classifiers, especially those fine-tuned classifiers susceptible to overfittingtrainingdata,maystruggletorecognizetypesofLLMsnotseenduringtraining.
Thus,fornewlyemergingLLMs,detectorsmaynoteffectivelyidentifythem(Pagnoni,
Graciarena,andTsvetkov2022b).Forinstance,theOpenAIdetector15 (trainedontexts
generated by GPT-2) struggles to discern texts generated by GPT-3.5-Turbo and GPT-
4,achieving an AUROC of only 74.74%, while itperforms nearly perfectly on GPT-2
generatedtexts(Baoetal.2023).Theresultsof(Sarvazyanetal.2023b)demonstratethat
supervisedLLM-generatedtextdetectorsexhibitgoodgeneralizationcapabilitiesacross
modelscalesbuthavelimitationsingeneralizingacrossmodelfamilies.Enhancingthe
cross-llmsrobustnessofneuralclassifiersisthusessentialforthepracticaldeployment
ofdetectors.Nonetheless,classifiersfine-tunedonRobertastillpossessstrongtransfer
capabilities, and with additional fine-tuning on just a few hundred samples, detectors
caneffectivelygeneralizetotextsgeneratedbyothermodels.Therefore,incorporating
LLM-generated text from various sources into the training data could substantially
improve the cross-llms robustness of detectors in real-world applications, even with
asmallsamplesize.
7.2PotentialAttacks
Potential attacks significantly contribute to the ongoing unreliability of current LLM-
generatedtextdetectors.Wepresentthecurrenteffectiveattackstopushresearchersto
focusonmorecomprehensivedefensivemeasures.
ParaphraseAttacks.Paraphrasingattacksareoneofthemosteffectiveattacksthatcanbe
fully effective against detectors using watermarking technology as well as fine-tuned
supervised detectors and zero-shot detectors (Sadasivan et al. 2023; Orenstrakh et al.
2023).Theunderlyingprincipleinvolvesapplyingalightweightparaphrasemodelon
LLMs’ outputs and changing the distribution of lexical and syntactic features of the
text by paraphrasing, thereby confusing the detector. Sadasivan et al. (2023) reported
onParrot(Damodaran2021),aT5-basedparaphrasemodelandDIPPER(Krishnaetal.
2023),an11Bparaphrasingmodelthatallowsfortuningparaphrasediversityandthe
degree of content reordering that attacks the overall superiority of existing detection
methods.Althoughretrieval-basedapproacheshavebeenshowntodefendeffectively
againstparaphrasingattacks(Krishnaetal.2023),implementingsuchdefensesrequires
15 openai-community/roberta-large-openai-detector
42

<!-- Page 43 -->


### Wuetal. ASurveyonLLM-GeneratedTextDetection

ongoing maintenance by the language model API provider and is still susceptible to
recursiveparaphrasingattacks(Sadasivanetal.2023).
AdversarialAttacks.NormalLLM-generatedtextsarehighlyidentifiable,yetadversarial
perturbations, such as substitution, can effectively reduce the accuracy of detectors
(Pengetal.2024).Wesummariseattacksthatprocessontextualfeaturesasadversarial
attacks,includingcutoff(croppingaportionofthefeatureorinput)(Shenetal.2020),
shuffle (randomly disrupting the word order of the input) (Lee et al. 2020), mutation
(character and word mutation) (Liang, Guerrero, and Alsmadi 2023), word swapping
(substituting other suitable words given the context) (Shi and Huang 2020; Ren et al.
2019;Crothersetal.2022)andmisspelling(Gaoetal.2018a).Therearealsoadversarial
attack frameworks such as TextAttack (Morris et al. 2020), which can build an attack
fromfourcomponents:anobjectivefunction,asetofconstraints,atransformation,and
asearchmethod.Shietal.(2023)andHeetal.(2023)reportedontheeffectivenessofthe
permutationapproachonattackdetectors.Specifically,Shietal.(2023)replacedwords
with synonyms based on context, which forms an effective attack on the fine-tuned
classifier, watermarking (Kirchenbauer et al. 2023a), and DetectGPT (Mitchell et al.
2023),reducingdetectorperformancebymorethan18%,10%,and25%respectively.He
etal.(2023)employedprobability-weightedwordsaliency(Renetal.2019)togenerate
adversarialexamples,whichfurthermaintainssemanticsimilarity.
StiffandJohansson(2022)utilizedtheDeepWordBug(Gaoetal.2018b)adversarial
attack algorithm to introduce character-level perturbations to generated texts, including adjacent character swaps, character substitutions, deletions, and insertions, which
resultedinmorethanahalvingoftheperformanceoftheOpenAIlargedetector.16Wolff
(2020)presentedtwotypesofblack-boxattacksagainstthesedetectors:randomsubstitutionsofcharacterswithvisuallysimilarhomoglyphsandtheintentionalmisspelling
ofwords.Theseattacksdrasticallyreducedtherecallrateofpopularneuraltextdetectorsfrom97.44%to0.26%and22.68%,respectively.Moreover,BhatandParthasarathy
(2020) showed that detectors are more sensitive to syntactic perturbations, including
breaking longer sentences, removing definite articles, using semantic-preserving rule
conversions (such as changing “that’s” to “that is”), and reformatting paragraphs of
machine-generatedtext.
Although existing detection methods are highly sensitive to adversarial attacks,
differenttypesofdetectorsexhibitvaryingdegreesofresiliencetosuchattacks.Antoun
et al. (2023b) reported that supervised approaches are effective defensive measures
againsttheseattacks:trainingonadversarialsamplescansignificantlyimproveadetector’sabilitytorecognizetextsthathavebeenmanipulatedbysuchattacks.Additionally,
Kulkarni et al. (2023) explored the impact of semantic perturbations on the Grover
detector,findingthatsynonymsubstitution,fake-fakereplacement,insertioninsteadof
substitution,andchangesinthepositionofsubstitutionhadnoeffectonGrover’sdetectioncapabilities.However,adversarialembeddingtechniquescaneffectivelydeceive
Grover into classifying false articles as genuine. The attack degrades the performance
ofthefine-tuningclassifiersignificantly,eventhoughthedistributionalfeaturesofthe
attackcanbelearnedbythefine-tuningclassifiertoformastrongdefense.
PromptAttacks.PromptattacksposeasignificantchallengeforcurrentLLM-generated
textdetectiontechniques.ThequalityofLLM-generatedtextisassociatedwiththecom-
16 openai-community/roberta-large-openai-detector
43

<!-- Page 44 -->

plexityofthepromptsthatinstructLLMstogeneratetext.Asthemodelandcorpussize
increase,LLMsemergewithexcellentICLcapabilitiesformorecomplextextgeneration
capabilities. Numerous efficient prompting methods have been developed, including
few-shot prompt (Brown et al. 2020), combining prompt (Zhao et al. 2021), Chain of
Thought (CoT) (Wei et al. 2022), and zero-shot CoT (Kojima et al. 2022), etc., which
significantly enhance the quality and capabilities of LLMs. Existing works on LLM-
generatedtextdetectorsprimarilyutilizedatasetscreatedwithsimpledirectprompts.
Forinstance,thestudybyGuoetal.(2023)demonstratesthatdetectorsmightstruggle
toidentifytextgeneratedwithcomplexprompts.Liuetal.(2023d)reportedanoticeable
decreaseinthedetectionabilityofadetectorusingafine-tunedlanguagemodelwhen
facedwithvariedprompts,whichindicatesthattheuseofdifferentpromptsresultsin
largedifferencesinthedetectionperformanceofexistingdetectors(Koike,Kaneko,and
Okazaki2023a).
The Substitution-based Contextual Example Optimisation method, as proposed
by Lu et al. (2023), employs sophisticated prompts to bypass the defenses of current
detectionsystems.ThisleadstoanappreciablereductionintheAreaUndertheCurve
(AUC),averagingadecreaseof0.54,andachievesahighersuccessratewithbettertext
quality compared to paraphrase attacks. It is worth mentioning that both paraphrase
attacks and adversarial attacks mentioned above could be executed through careful
prompt design (Shi et al. 2023; Koike, Kaneko, and Okazaki 2023b). With ongoing
researchinpromptengineering,theriskposedbypromptattacksisexpectedtoescalate
further.Thisunderscorestheneedfordevelopingmorerobustdetectionmethodsthat
caneffectivelycounteractsuchevolvingthreats.
Training Threat Models. Further training of language models has been preliminarily
proven to effectively attack existing detectors. Nicks et al. (2023) used the “humanity” scores of various open source and commercial detectors as a reward function
for reinforcement learning, which fine-tunes language models to confound existing
detectors. Without significantly altering the model, further fine-tuning of the Llama-
2-7BcanreducetheAUROCoftheOpenAIRoBERTa-Largedetectorfrom0.84AUROC
to0.62AUROCinashorttrainingperiod.Asimilarideaisdemonstratedin(Schneider
et al. 2023): using reinforcement learning to refine generative models can successfully
circumventBERT-basedclassifierswithdetectionaccuracyaslowas0.15AUROC,even
whenusinglinguisticfeaturesasarewardfunction.Kumarageetal.(2023b)proposesa
universalevasionframeworknamedEScaPetoguidePLMsingenerating“human-like
text” that may mislead detectors. Through evasive soft prompt learning and transfer,
the performance of DetectGPT and OpenAI Detector can be effectively reduced by up
to 40% AUROC. The results from (Henrique, Kucharavy, and Guerraoui 2023) reveal
anotherpotentialvulnerabilityofdetectors.Ifagenerativemodelcanaccessthehumanwritten text used to train the detector and use them for fine-tuning, it is impossible
to use detector for text detection on this generative model. This indicate that LLMs
trainedonmorehuman-writtencorpuswillbemorerobustagainstexistingdetectors,
and training against a specific detector can provide the LLMs with a sharp spear to
breachitsdefenses.
7.3Real-WorldDataIssues
44

<!-- Page 45 -->


### Wuetal. ASurveyonLLM-GeneratedTextDetection

Detection for Not Purely LLM-generated Text. In practice, there are many texts that are
not purely generated by LLMs, and they may even contain a mix of human-written
text.Specifically,thiscanbecategorizedaseitherdata-mixedtextorhuman-editedtext.
Data-mixed text refers to the sentence or paragraph level mixture of human-written
text and LLM-generated text. For instance, in a document, some sentences may be
generated by LLMs, while others are written by humans. In such cases, identifying
thecategoryofthedocumentbecomeschallenging.Data-mixedtextnecessitatesmore
fine-graineddetectionmethods,suchassentence-leveldetection,toeffectivelyaddress
this challenge. However, current LLM-generated text detectors struggle to perform
effectivelywithshorttexts.Recentresearch,suchasthatbyWangetal.(2023a),indicates
thatsentence-leveldetectionappearstobefeasible.Furthermore,weareverypleasedto
observethatstudieshavestartedtoproposeandattempttosolvethisissue.Zengetal.
(2023)proposedatwo-stepmethodtoeffectivelyidentifyamixofhuman-writtenand
LLM-generatedtext.Thismethodfirstusescontrastivelearningtodistinguishbetween
contentgeneratedbyLLMsandhuman-writtencontent.Itthencalculatesthesimilarity
betweenadjacentprototypes,assumingthataboundaryexistsbetweentheleastsimilar
adjacentprototypes.
Another issue that has not been fully discussed is the human-edited text. For
example,afterapplyingLLMtogenerateatext,humansofteneditandmodifycertain
words or passages. The detection of such text poses a significant challenge and is an
issuewemustconfront,asitisprevalentinreal-worldapplications.Therefore,thereis
anurgentneedtoorganizerelevantdatasetsanddefinetaskstoaddressthisissue.One
potentialapproachfortacklingthisproblemisinformedbyexperimentalresultsfrom
paraphrasingandadversarialperturbationattacks.Thesemethodseffectivelysimulate
howindividualsmightuseLLMstorefinetextormakewordsubstitutions.However,
tend to degrade in performance when dealing with paraphrased text, current mainstreamdetectors tendto degradeinperformance whendealingwith paraphrasedtext
(Wolff 2020), although certain black-box detectors display relatively good robustness.
Anotherpotentialsolutioncouldinvolvebreakingdownthedetectiontasktotheword
level,butasofnow,thereisnoresearchdirectlyaddressingthis.
DataAmbiguity.DataambiguityremainsachallengeinthefieldofLLM-generatedtext
detection, with close ties to the inherent mechanics of the detection technology itself.
ThepervasivedeploymentofLLMsacrossvariousdomainsexacerbatesthisissue,rendering it increasingly challenging to discern whether training data comprises humanwrittenorLLM-generatedtext.UtilizingLLM-generatedtextastrainingdataunderthe
misapprehensionthatitishuman-writteninadvertentlyinstigatesadetrimentalcycle.
Within this cycle, detectors, consequently trained, demonstrate diminished efficacy in
distinguishingbetweenhuman-writtenandLLM-generatedtext,therebyundermining
the foundational premises of detector research. It is imperative to acknowledge that
this quandary poses a significant, pervasive threat to all facets of detection research,
yet,toourknowledge,noexistingstudiesformallyaddressthisconcern.Anadditional
potentialriskwasarticulatedbyAlemohammadetal.(2023),whopositedthatdataambiguitymightprecipitatetherecyclingofLLM-generateddatainthetrainingprocesses
ofsubsequentmodels.Thisscenariocouldadverselyimpactthetextgenerationquality
oftheseemergentLLMs,therebydestabilizingtheresearchlandscapededicatedtothe
detectionofLLM-generatedtext.
45

<!-- Page 46 -->

7.4ImpactofModelSizeonDetectors
Manyresearchersareconcernedabouttheimpactofthemodelsizeondetectors,which
can be viewed from two perspectives: one is the size of the generative model, and
the other is the size of the supervised classifiers. The size of the generative model is
closelyrelatedtothequalityofthegeneratedtext.Generallyspeaking,textsgenerated
bysmaller-sizedmodelsareeasiertorecognize,whilethosegeneratedbylargermodels
poseagreaterchallengefordetection.Anotherissueofconcernishowthetextsgeneratedbymodelsofdifferentsizesaffectthedetectorswhenusedastrainingsamples.Pu
etal.(2023b)reportthatdetectorstrainedwithdatageneratedbymedium-sizedLLMs
cangeneralizetolargerversionswithoutanysamples,whiletrainingsamplesgenerated
byoverlylargeorsmallmodelsmayreducethegeneralizationabilityofthedetectors.
Antoun, Sagot, and Seddah (2023) further explores the apparent negative correlation
betweenclassifiereffectivenessandthesizeofthegenerativemodel.Theresultsshow
that text generated by larger LLMs is more difficult to detect, especially when the
classifier is trained on data generated by smaller LLMs. Aligning the distribution of
thegenerativemodelsforthetrainingandtestsetscanimprovetheperformanceofthe
detectors. From the perspective of the size of the supervised classifiers, the detection
capabilityofthedetectorsisdirectlyproportionaltothesizeofthefine-tunedLMs(Guo
etal.2023).However,recentfindingssuggestthatwhilelargerdetectorsperformbetter
ontestsetswiththesamedistributionasthetrainingset,theirgeneralizationabilityis
somewhatdiminished.
7.5LackofEffectiveEvaluationFramework
A widespread phenomenon is that many studies claim their detectors exhibit impressive and robust performance. However, in practical experiments, these methods often
perform less than satisfactorily on the test sets created by other researchers. This varianceisduetoresearchersusingdifferentstrategiestoconstructtheirtestsets.Variables
such as the parameters used to generate the test set, the computational environment,
textdistribution,andtextprocessingstrategies,includingtruncation,canallinfluence
theeffectivenessofdetectors.Duetothesefactors’complexnature,thereproducibility
of evaluation results is often compromised, even when researchers adhere to identical
dataset production protocols. We elaborate on the limitations of existing benchmarks
in section 4, where we advocate for the creation of a high-quality and comprehensiveevaluationframework.Weencouragefutureresearchtoactivelyimplementthese
frameworks to maintain consistency in testing standards. Furthermore, we call upon
researchers focusing on specific issues to openly share their test sets, emphasizing the
strongadaptabilityofcurrentevaluationframeworkstointegratethem.Inconclusion,
settinganobjectiveandfairbenchmarkfordetectorcomparisonisessentialtopropelresearchindetectingLLM-generatedtextforward,ratherthanpersistinginsiloedefforts.

## FutureResearchDirections

Inthissection,weexplorepotentialdirectionsforfutureresearchaimedatbetterconstructionofmoreefficientandrealisticallyeffectivedetectors.
46

<!-- Page 47 -->

Wuetal. ASurveyonLLM-GeneratedTextDetection
8.1BuildingRobustDetectorswithAttacks
Theattackmethodsintroducedinsubsection7.2,encompassParaphraseAttacks(Sadasivan et al. 2023), Adversarial Attacks (He et al. 2023), and Prompt Attacks (Lu et al.
2023).Thesemethodsunderscoretheprimarychallengesimpedingtheutilityofcurrent
detectors. While recent research, such as Yang, Jiang, and Li (2023), has addressed
robustness against specific attacks, it often neglects potential threats posed by other
attack forms. Consequently, it is imperative to develop and validate diverse attack
types, thereby gaining insights into vulnerabilities inherent to LLM-generated text
detectors.Wefurtheradvocatefortheestablishmentofcomprehensivebenchmarksto
assessexistingdetectionstrategies.Althoughsomestudies(Heetal.2023;Wangetal.
2023b) purport to provide such benchmarks, the scope and diversity of the validated
attacksremainlimited.
8.2EnhancingtheEfficacyofZero-shotDetectors
Zero-shot methods stand out as notably stable detectors (Deng et al. 2023). Crucially,
theyofferenhancedcontrollabilityandinterpretabilityforusers(Mitrovic´,Andreoletti,
and Ayoub 2023). Recent research (Giorgi et al. 2023; Liao et al. 2023b) has elucidated
distinctdisparitiesbetweenLLM-generatedtextandhuman-writtentext,underscoring
atangibleanddiscerniblegapbetweenthetwo.Thisrevelationhasinvigoratedresearch
inthedomainofLLM-generatedtextdetection.WeadvocateforaproliferationofstudiesthatdelveintothenuanceddistinctionsbetweenLLM-generatedtextsandhumanwrittentext,spanningfromlow-dimensionaltohigh-dimensionalfeatures.Unearthing
metricsthatmoreaccuratelydistinguishthetwocanbolstertheevolutionofautomatic
detectors and furnish more compelling justifications for decision-making processes.
We have observed that the latest emerging black-box zero-shot methods (Yang et al.
2023b; Mao et al. 2024; Zhu et al. 2023; Quidwai, Li, and Dube 2023; Guo and Yu
2023) demonstrate enhanced stability and application potential compared to whiteboxbasedzero-shotmethodsbyextractingdiscriminativemetricsthatareindependent
of white-box models. These methods do not rely on an understanding of the model’s
internal workings, thereby offering broader applicability across various models and
environments.
8.3OptimizingDetectorsforLow-resourceEnvironments
Many contemporary detection techniques tend to overlook the challenges faced by
resource-constrained settings, neglecting the need for resources in developing the detector.Therelativeefficacyofvariousdetectorsacrossdifferentdatavolumesettingsremainsinadequatelyexplored.Concurrently,determiningtheminimalresourceprerequisitesfordifferentdetectionmethodstoyieldsatisfactoryresultsisimperative.Beyond
examiningthemodel’sadaptabilityacrossdistinctdomains(Rodriguezetal.2022a)and
languages(Wangetal.2023b),weadvocateforinvestigatingthedefensiveadaptability
againstvariedattackstrategies.Suchexplorationcanguideusersinselectingthemost
beneficialapproachtoestablishadependabledetectorunderresourceconstraints.
8.4DetectionforNotPurelyLLM-GeneratedText
Insection7.3,wehighlightasignificantchallengeencounteredinreal-worldscenarios:
the detection of text that is not purely produced by LLMs. We examine this issue by
47

<!-- Page 48 -->

separatelydiscussingtextsthatareamixtureofdatasourcesandthosethathavebeen
editedbyhumans,andreviewthelatestrelatedworkandproposepotentialsolutions,
whicharestillpendingverification.Weemphasizethatorganizingrelevantdatasetsand
definingtaskstoaddressthisissueisanurgentneedatpresent,becausefundamentally,
thistypeoftextmaybethemostcommonlyencounteredindetectorapplications.
8.5ConstructingDetectorsAmidstDataAmbiguity
A significant challenge that arises is verifying the authenticity of training data. When
aggregating textual data from sources such as blogs and web comments, there is a
potential risk of inadvertently including a substantial amount of LLM-generated text.
This incorporation can fundamentally compromise the integrity of detector research,
perpetuating a detrimental feedback loop. We urge forthcoming detection studies to
prioritizetheauthenticityassessmentofreal-worlddata,anticipatingthisasapressing
challengeinthefuture.
8.6DevelopingEffectiveEvaluationFrameworkAlignedWithReal-World
Insubsection7.5,weanalyzetheobjectivedifferencesbetweenevaluationenvironments
andreal-worldsettings,whichlimittheeffectivenessofexistingdetectorswhenapplied
in practice. On one hand, there may be biases in the construction of test sets in many
worksbecausetheyoftenfavorthedetectorsbuiltbytheircreators;ontheotherhand,
currentbenchmarksfrequentlyreflectidealizedscenariosfarremovedfromreal-world
applications.Wecallonresearcherstodevelopafairandeffectiveevaluationframework
closelylinkedtothepracticalneedsofLLM-generateddetectiontasks.Forinstance,consideringthenecessityoftheapplicationdomain,theblack-boxnatureofLLM-generated
texts,andthevariousattacksandpost-editingstrategiesthattextsmayencounter.We
believe such an evaluation framework will promote the research and development of
detectorsthataremorepracticalandalignedwithreal-worldscenarios.
8.7ConstructingDetectorswithMisinformationDiscriminationCapabilities
Contemporarydetectionmethodologieshavelargelyoverlookedthecapacitytodiscern
misinformation. Existing detectors primarily emphasize the distribution of features
within text generated by LLMs, while often overlooking their potential for factual
verification. A proficient detector should possess the capability to discern the veracity
orfalsityoffactualclaimspresentedintext.Intheinitialstagesofgenerativemodeling’s
emergence,whenithadyettoposesignificantsocietalchallenges,theemphasiswason
assessingthetruthorfalsityofthecontentinLLM-generatedtext,withlessregardfor
itssource(Schusteretal.2020b).Constructingdetectorswithmisinformationdiscriminationcapabilitiescanaidinmoreaccuratelyattributingthesourceoftext,ratherthan
relyingsolelyondistributionalfeatures,andsubsequentlycontributetomitigatingthe
proliferationofmisinformation.Recentstudies(Gaoetal.2023;Chernetal.2023)highlightthepotentialofLLMstodetectfactualcontentintexts.Werecommendbolstering
suchendeavorsthroughintegrationwithexternalknowledgebases(Asaietal.2023)or
searchengines(Liangetal.2023b).
48

<!-- Page 49 -->

Wuetal. ASurveyonLLM-GeneratedTextDetection

## Conclusion

With the widespread development and application of LLMs, the pervasive presence
of LLM-generated text in our daily lives has transitioned from expectation to reality.
LLM-generated text detectors play a pivotal role in distinguishing between humanwritten and LLM-generated text, serving as a crucial defense against the misuse of
LLMs for generating deceptive news, engaging in scams, or exacerbating issues such
as educational inequality. In this survey, we introduce the task of LLM-generated text
detection,outlinethesourcescontributingtoenhancedLLM-generatedtextcapabilities,
andhighlighttheescalatingdemandforefficientdetectors.Wealsolistdatasetsthatare
popular or promising, pointing out the challenges and requirements associated with
existing detectors. In addition, we shed light on the critical limitations of contemporary detectors, including issues related to out-of-distribution data, potential attacks,
real-world data issues, and the lack of an effective evaluation framework, to direct
researchers’attentiontothefocalpointsofthefield,therebysparkinginnovativeideas
andapproaches.Finally,weproposepotentialfutureresearchdirectionsthatarepoised
toguidethedevelopmentofmorepowerfulandeffectivedetectionsystems.

### Acknowledgments

ThisworkwassupportedinpartbytheMajorProgramoftheStateCommissionofScience
TechnologyofChina(GrantNo.2020AAA0106701),theScienceandTechnologyDevelopment
Fund,MacauSAR(GrantNos.FDCT/0070/2022/AMJ,FDCT/060/2022/AFJ)andthe
Multi-yearResearchGrantfromtheUniversityofMacau(GrantNo.

## Myrg-Grg2023-00006-Fst-Umdf).


### References Anthropic.2023. Modelcardandevaluations

Abdelnabi,SaharandMarioFritz.2021. forclaudemodels.
Adversarialwatermarkingtransformer: Antoun,Wissam,VirginieMouilleron,Benoît
Towardstracingtextprovenancewithdata Sagot,andDjaméSeddah.2023a. Towards
hiding. In42ndIEEESymposiumon arobustdetectionoflanguagemodel
SecurityandPrivacy,SP2021,SanFrancisco, generatedtext:Ischatgptthateasyto
CA,USA,24-27May2021,pages121–140, detect? CoRR,abs/2306.05871.

### IEEE. Antoun,Wissam,VirginieMouilleron,Benoît

Aich,Ankit,SouvikBhattacharya,and Sagot,andDjaméSeddah.2023b. Towards
NatalieParde.2022. Demystifyingneural arobustdetectionoflanguagemodel
fakenewsvialinguisticfeature-based generatedtext:Ischatgptthateasyto
interpretation. InProceedingsofthe29th detect? CoRR,abs/2306.05871.
InternationalConferenceonComputational Antoun,Wissam,BenoîtSagot,andDjamé
Linguistics,COLING2022,Gyeongju, Seddah.2023. Fromtexttosource:Results
RepublicofKorea,October12-17,2022,pages indetectinglargelanguage
6586–6599,InternationalCommitteeon model-generatedcontent. CoRR,
ComputationalLinguistics. abs/2309.13322.

### Alemohammad,Sina,Josue Arase,YukiandMingZhou.2013. Machine

Casco-Rodriguez,LorenzoLuzi, translationdetectionfrommonolingual
AhmedImtiazHumayun,HosseinBabaei, web-text. InProceedingsofthe51stAnnual
DanielLeJeune,AliSiahkoohi,and MeetingoftheAssociationforComputational
RichardG.Baraniuk.2023. Linguistics(Volume1:LongPapers),pages
Self-consuminggenerativemodelsgo 1597–1607,AssociationforComputational
MAD. CoRR,abs/2307.01850. Linguistics.
Aliman,NadishaMarieandLeonKester. Asai,Akari,SewonMin,ZexuanZhong,and

## Epistemicdefensesagainstscientific DanqiChen.2023. Retrieval-based

andempiricaladversarialaiattacks. In languagemodelsandapplications. In
CEURWorkshopProceedings,volume2916, Proceedingsofthe61stAnnualMeetingofthe
CEURWS. AssociationforComputationalLinguistics
(Volume6:TutorialAbstracts),pages41–46.
49

<!-- Page 50 -->

Asghar,Nabiha.2016. Yelpdataset languagemodels. ArXivpreprint,
challenge:Reviewratingprediction. ArXiv abs/2308.09687.
preprint,abs/1605.05362. Bhat,MeghanaMoorthyandSrinivasan
Ayoobi,Navid,SadatShahriar,andArjun Parthasarathy.2020. Howeffectivelycan

### Mukherjee.2023. Theloomingthreatof machinesdefendagainst

fakeandllm-generatedlinkedinprofiles: machine-generatedfakenews?an
Challengesandopportunitiesfor empiricalstudy. InProceedingsoftheFirst
detectionandprevention. InProceedingsof WorkshoponInsightsfromNegativeResults
the34thACMConferenceonHypertextand inNLP,Insights2020,Online,November19,
SocialMedia,pages1–10. 2020,pages48–53.
Baayen,RHarald.2001. Wordfrequency Bhattacharjee,Amrita,TharinduKumarage,
distributions,volume18. SpringerScience RahaMoraffah,andHuanLiu.2023.
&BusinessMedia. Conda:Contrastivedomainadaptationfor
Baccianella,Stefano,AndreaEsuli,and ai-generatedtextdetection. CoRR,
FabrizioSebastiani.2010. Sentiwordnet abs/2309.03992.
3.0:Anenhancedlexicalresourcefor Bhattacharjee,AmritaandHuanLiu.2023.
sentimentanalysisandopinionmining. In Fightingfirewithfire:Canchatgptdetect
ProceedingsoftheInternationalConferenceon ai-generatedtext? ArXivpreprint,
LanguageResourcesandEvaluation,LREC abs/2308.01284.
2010,17-23May2010,Valletta,Malta, Blanchard,Daniel,JoelTetreault,Derrick
EuropeanLanguageResources Higgins,AoifeCahill,andMartin

### Association. Chodorow.2013. Toefl11:Acorpusof

Bakhtin,Anton,SamGross,MyleOtt, non-nativeenglish. ETSResearchReport
YuntianDeng,Marc’AurelioRanzato,and Series,2013(2):i–15.
ArthurSzlam.2019. Realorfake?learning Brown,TomB.,BenjaminMann,NickRyder,
todiscriminatemachinefromhuman MelanieSubbiah,JaredKaplan,Prafulla
generatedtext. CoRR,abs/1906.03351. Dhariwal,ArvindNeelakantan,Pranav
Bao,Guangsheng,YanbinZhao,Zhiyang Shyam,GirishSastry,AmandaAskell,
Teng,LinyiYang,andYueZhang.2023. SandhiniAgarwal,ArielHerbert-Voss,
Fast-detectgpt:Efficientzero-shot GretchenKrueger,TomHenighan,Rewon
detectionofmachine-generatedtextvia Child,AdityaRamesh,DanielM.Ziegler,
conditionalprobabilitycurvature. arXiv JeffreyWu,ClemensWinter,Christopher
preprintarXiv:2310.05130,abs/2310.05130. Hesse,MarkChen,EricSigler,Mateusz
BarbaraKitchenham,StuartCharters.2007. Litwin,ScottGray,BenjaminChess,Jack
Guidelinesforperformingsystematic Clark,ChristopherBerner,Sam
literaturereviewsinsoftwareengineering. McCandlish,AlecRadford,IlyaSutskever,

### Becker,BrettA,PaulDenny,James andDarioAmodei.2020. Language

Finnie-Ansley,AndrewLuxton-Reilly, modelsarefew-shotlearners. InAdvances
JamesPrather,andEddieAntonioSantos. inNeuralInformationProcessingSystems33:

## Programmingishard-oratleastit AnnualConferenceonNeuralInformation

usedtobe:Educationalopportunitiesand ProcessingSystems2020,NeurIPS2020,
challengesofaicodegeneration. In December6-12,2020,virtual.
Proceedingsofthe54thACMTechnical Cardenuto,JoãoPhillipe,JingYang,Rafael
SymposiumonComputerScienceEducation Padilha,RenjieWan,DanielMoreira,
V.1,pages500–506. HaoliangLi,ShiqiWang,FernandaA.
Beresneva,Daria.2016. Computer-generated Andaló,SébastienMarcel,andAnderson
textdetectionusingmachinelearning:A Rocha.2023. Theageofsyntheticrealities:
systematicreview. InNaturalLanguage Challengesandopportunities. CoRR,
ProcessingandInformationSystems:21st abs/2306.11503.
InternationalConferenceonApplicationsof Chaka,Chaka.2023. Detectingaicontentin
NaturalLanguagetoInformationSystems, responsesgeneratedbychatgpt,youchat,
NLDB2016,Salford,UK,June22-24,2016, andchatsonic:Thecaseoffiveaicontent
Proceedings21,pages421–426,Springer. detectiontools. JournalofAppliedLearning
Besta,Maciej,NilsBlach,AlesKubicek, andTeaching,6(2).
RobertGerstenberger,LukasGianinazzi, Chakraborty,Megha,S.M.TowhidulIslam
JoannaGajda,TomaszLehmann,Michal Tonmoy,S.M.MehediZaman,Shreya
Podstawski,HubertNiewiadomski,Piotr Gautam,TanayKumar,KrishSharma,
Nyczyk,etal.2023. Graphofthoughts: NiyarR.Barman,ChandanGupta,Vinija
Solvingelaborateproblemswithlarge Jain,AmanChadha,AmitP.Sheth,and
50

<!-- Page 51 -->


### Wuetal. ASurveyonLLM-GeneratedTextDetection

AmitavaDas.2023a. Counterturingtest DavidLuan,HyeontaekLim,BarretZoph,
(CT2):ai-generatedtextdetectionisnotas AlexanderSpiridonov,RyanSepassi,
easyasyoumaythink-introducingAI DavidDohan,ShivaniAgrawal,Mark
detectabilityindex(ADI). InProceedingsof Omernick,AndrewM.Dai,
the2023ConferenceonEmpiricalMethodsin ThanumalayanSankaranarayanaPillai,
NaturalLanguageProcessing,EMNLP2023, MariePellat,AitorLewkowycz,Erica
Singapore,December6-10,2023,pages Moreira,RewonChild,Oleksandr
2206–2239,AssociationforComputational Polozov,KatherineLee,ZongweiZhou,

### Linguistics. XuezhiWang,BrennanSaeta,MarkDiaz,

Chakraborty,Souradip,AmritSinghBedi, OrhanFirat,MicheleCatasta,JasonWei,
SichengZhu,BangAn,DineshManocha, KathyMeier-Hellstern,DouglasEck,Jeff
andFurongHuang.2023b. Onthe Dean,SlavPetrov,andNoahFiedel.2022a.
possibilitiesofai-generatedtextdetection. Palm:Scalinglanguagemodelingwith
CoRR,abs/2304.04736. pathways. CoRR,abs/2204.02311.
Chen,Qianben,RichongZhang,Yaowei Chowdhery,Aakanksha,SharanNarang,
Zheng,andYongyiMao.2022. Dual JacobDevlin,MaartenBosma,Gaurav
contrastivelearning:Textclassificationvia Mishra,AdamRoberts,PaulBarham,
label-awaredataaugmentation. ArXiv HyungWonChung,CharlesSutton,
preprint,abs/2201.08702. SebastianGehrmann,etal.2022b. Palm:

### Chen,Yutian,HaoKang,VivianZhai, Scalinglanguagemodelingwith

LiangzeLi,RitaSingh,andBhikshaRaj. pathways. ArXivpreprint,abs/2204.02311.
2023a. Tokenpredictionasimplicit Christian,Jon.2023. Cnetsecretlyusedaion
classificationtoidentifyllm-generated articlesthatdidn’tdisclosethatfact,staff
text. InProceedingsofthe2023Conferenceon say. Futurusm,January.
EmpiricalMethodsinNaturalLanguage Clark,Elizabeth,TalAugust,SofiaSerrano,
Processing,EMNLP2023,Singapore, NikitaHaduong,SuchinGururangan,and
December6-10,2023,pages13112–13120, NoahA.Smith.2021a. Allthat’s‘human’
AssociationforComputational isnotgold:Evaluatinghumanevaluation

### Linguistics. ofgeneratedtext. InProceedingsofthe59th

Chen,Yutian,HaoKang,VivianZhai, AnnualMeetingoftheAssociationfor
LiangzeLi,RitaSingh,andBhiksha ComputationalLinguisticsandthe11th
Ramakrishnan.2023b. Gpt-sentinel: InternationalJointConferenceonNatural
Distinguishinghumanandchatgpt LanguageProcessing(Volume1:Long
generatedcontent. ArXivpreprint, Papers),pages7282–7296,Associationfor
abs/2305.07969. ComputationalLinguistics.
Chern,I,SteffiChern,ShiqiChen,Weizhe Clark,Elizabeth,TalAugust,SofiaSerrano,
Yuan,KehuaFeng,ChuntingZhou, NikitaHaduong,SuchinGururangan,and
JunxianHe,GrahamNeubig,PengfeiLiu, NoahA.Smith.2021b. Allthat’s’human’
etal.2023. Factool:Factualitydetectionin isnotgold:Evaluatinghumanevaluation
generativeai–atoolaugmented ofgeneratedtext. InProceedingsofthe59th
frameworkformulti-taskand AnnualMeetingoftheAssociationfor
multi-domainscenarios. ArXivpreprint, ComputationalLinguisticsandthe11th
abs/2307.13528. InternationalJointConferenceonNatural
Chowdhery,Aakanksha,SharanNarang, LanguageProcessing,ACL/IJCNLP2021,
JacobDevlin,MaartenBosma,Gaurav (Volume1:LongPapers),VirtualEvent,
Mishra,AdamRoberts,PaulBarham, August1-6,2021,pages7282–7296,
HyungWonChung,CharlesSutton, AssociationforComputational
SebastianGehrmann,ParkerSchuh, Linguistics.
KensenShi,SashaTsvyashchenko,Joshua Conneau,Alexis,KartikayKhandelwal,
Maynez,AbhishekRao,ParkerBarnes, NamanGoyal,VishravChaudhary,
YiTay,NoamShazeer,Vinodkumar GuillaumeWenzek,FranciscoGuzmán,

### Prabhakaran,EmilyReif,NanDu,Ben EdouardGrave,MyleOtt,Luke

Hutchinson,ReinerPope,JamesBradbury, Zettlemoyer,andVeselinStoyanov.2020.
JacobAustin,MichaelIsard,GuyGur-Ari, Unsupervisedcross-lingualrepresentation
PengchengYin,TojuDuke,Anselm learningatscale. InProceedingsofthe58th
Levskaya,SanjayGhemawat,SunipaDev, AnnualMeetingoftheAssociationfor
HenrykMichalewski,XavierGarcia, ComputationalLinguistics,ACL2020,
VedantMisra,KevinRobinson,Liam Online,July5-10,2020,pages8440–8451,
Fedus,DennyZhou,DaphneIppolito, AssociationforComputational
51

<!-- Page 52 -->


### Linguistics. Deng,Zhijie,HongchengGao,YiboMiao,

Corizzo,RobertoandSebastianLeal-Arenas. andHaoZhang.2023. Efficientdetection

## Adeepfusionmodelforhuman ofllm-generatedtextswithabayesian

$vs$.machine-generatedessay surrogatemodel. ArXivpreprint,
classification. InInternationalJoint abs/2305.16617.
ConferenceonNeuralNetworks,IJCNN2023, Desaire,Heather,AleesaE.Chua,Madeline
GoldCoast,Australia,June18-23,2023, Isom,RomanaJarosova,andDavidHua.
pages1–10,IEEE. 2023. Chatgptoracademicscientist?
Corston-Oliver,Simon,MichaelGamon,and distinguishingauthorshipwithover99%
ChrisBrockett.2001. Amachinelearning accuracyusingoff-the-shelfmachine
approachtotheautomaticevaluationof learningtools. CoRR,abs/2303.16352.
machinetranslation. InProceedingsofthe Devlin,Jacob,Ming-WeiChang,KentonLee,
39thAnnualMeetingoftheAssociationfor andKristinaToutanova.2019a. BERT:
ComputationalLinguistics,pages148–155, pre-trainingofdeepbidirectional
AssociationforComputational transformersforlanguageunderstanding.

### Linguistics. InProceedingsofthe2019Conferenceofthe

Cowap,Alan,YvetteGraham,andJennifer NorthAmericanChapteroftheAssociationfor
Foster.2023. Dostochasticparrotshave ComputationalLinguistics:HumanLanguage
feelingstoo?improvingneuraldetection Technologies,NAACL-HLT2019,
ofsynthetictextviaemotionrecognition. Minneapolis,MN,USA,June2-7,2019,
InFindingsoftheAssociationfor Volume1(LongandShortPapers),pages
ComputationalLinguistics:EMNLP2023, 4171–4186,AssociationforComputational
Singapore,December6-10,2023,pages Linguistics.
9928–9946,AssociationforComputational Devlin,Jacob,Ming-WeiChang,KentonLee,

### Linguistics. andKristinaToutanova.2019b. BERT:

Crothers,Evan,NathalieJapkowicz,and pre-trainingofdeepbidirectional
HernaLViktor.2023a. Machine-generated transformersforlanguageunderstanding.
text:Acomprehensivesurveyofthreat InProceedingsofthe2019Conferenceofthe
modelsanddetectionmethods. IEEE NorthAmericanChapteroftheAssociationfor

### Access. ComputationalLinguistics:HumanLanguage

Crothers,Evan,NathalieJapkowicz,and Technologies,NAACL-HLT2019,

### HernaL.Viktor.2023b. Minneapolis,MN,USA,June2-7,2019,

Machine-generatedtext:Acomprehensive Volume1(LongandShortPapers),pages
surveyofthreatmodelsanddetection 4171–4186,AssociationforComputational
methods. IEEEAccess,11:70977–71002. Linguistics.
Crothers,Evan,NathalieJapkowicz, Devlin,Jacob,Ming-WeiChang,KentonLee,
HernaL.Viktor,andPaulaBranco.2022. andKristinaToutanova.2019c. BERT:

### Adversarialrobustnessof Pre-trainingofdeepbidirectional

neural-statisticalfeaturesindetectionof transformersforlanguageunderstanding.
generativetransformers. InInternational InProceedingsofthe2019Conferenceofthe
JointConferenceonNeuralNetworks,IJCNN NorthAmericanChapteroftheAssociationfor
2022,Padua,Italy,July18-23,2022,pages ComputationalLinguistics:HumanLanguage
1–8,IEEE. Technologies,Volume1(LongandShort
Cui,Jiaxi,ZongjianLi,YangYan,Bohua Papers),pages4171–4186,Associationfor
Chen,andLiYuan.2023. Chatlaw: ComputationalLinguistics.
Open-sourcelegallargelanguagemodel Dhaini,Mahdi,WesselPoelman,andEge
withintegratedexternalknowledgebases. Erdogan.2023. Detectingchatgpt:A

### ArXivpreprint,abs/2306.16092. surveyofthestateofdetecting

Dai,Damai,YutaoSun,LiDong,YaruHao, chatgpt-generatedtext. CoRR,
ShumingMa,ZhifangSui,andFuruWei. abs/2309.07689.

## Whycangptlearnin-context? Dong,Qingxiu,LeiLi,DamaiDai,CeZheng,

languagemodelsimplicitlyperform ZhiyongWu,BaobaoChang,XuSun,
gradientdescentasmeta-optimizers. In JingjingXu,andZhifangSui.2023. A
ICLR2023WorkshoponMathematicaland surveyforin-contextlearning. ArXiv
EmpiricalUnderstandingofFoundation preprint,abs/2301.00234.

### Models. Dou,Yao,MaxwellForbes,Rik

Damodaran,Prithiviraj.2021. Parrot: Koncel-Kedziorski,NoahA.Smith,and
Paraphrasegenerationfornlu. YejinChoi.2022. IsGPT-3text
indistinguishablefromhumantext?
52

<!-- Page 53 -->


### Wuetal. ASurveyonLLM-GeneratedTextDetection

scarecrow:Aframeworkforscrutinizing Gade,Krishna,SahinGeyik,Krishnaram
machinetext. InProceedingsofthe60th Kenthapadi,VarunMithal,andAnkur
AnnualMeetingoftheAssociationfor Taly.2020. Explainableaiinindustry:
ComputationalLinguistics(Volume1:Long Practicalchallengesandlessonslearned.
Papers),pages7250–7274,Associationfor InCompanionProceedingsoftheWeb
ComputationalLinguistics. Conference2020,pages303–304.
Dugan,Liam,DaphneIppolito,Arun Gallé,Matthias,JosRozen,Germán
Kirubarajan,andChrisCallison-Burch. Kruszewski,andHadyElsahar.2021.

## RoFT:Atoolforevaluatinghuman Unsupervisedanddistributionaldetection

detectionofmachine-generatedtext. In ofmachine-generatedtext. CoRR,
Proceedingsofthe2020Conferenceon abs/2111.02878.
EmpiricalMethodsinNaturalLanguage Gambini,Margherita,TizianoFagni,Fabrizio
Processing:SystemDemonstrations,pages Falchi,andMaurizioTesconi.2022. On
189–196,AssociationforComputational pushingdeepfaketweetdetection

### Linguistics. capabilitiestothelimits. InProceedingsof

Dugan,Liam,DaphneIppolito,Arun the14thACMWebScienceConference2022,
Kirubarajan,SherryShi,andChris pages154–163.
Callison-Burch.2023. Realorfaketext?: Gao,Ji,JackLanchantin,MaryLouSoffa,
Investigatinghumanabilitytodetect andYanjunQi.2018a. Black-box
boundariesbetweenhuman-writtenand generationofadversarialtextsequencesto
machine-generatedtext. InThirty-Seventh evadedeeplearningclassifiers. In2018
AAAIConferenceonArtificialIntelligence, IEEESecurityandPrivacyWorkshops(SPW),
AAAI2023,Thirty-FifthConferenceon pages50–56,IEEE.
InnovativeApplicationsofArtificial Gao,Ji,JackLanchantin,MaryLouSoffa,
Intelligence,IAAI2023,Thirteenth andYanjunQi.2018b. Black-box
SymposiumonEducationalAdvancesin generationofadversarialtextsequencesto
ArtificialIntelligence,EAAI2023, evadedeeplearningclassifiers. In2018
Washington,DC,USA,February7-14,2023, IEEESecurityandPrivacyWorkshops,SP
pages12763–12771,AAAIPress. Workshops2018,SanFrancisco,CA,USA,
Epstein,Ziv,AaronHertzmann, May24,2018,pages50–56.
InvestigatorsofHumanCreativity,Memo Gao,Luyu,ZhuyunDai,PanupongPasupat,
Akten,HanyFarid,JessicaFjeld, AnthonyChen,ArunTejasviChaganty,
MorganRFrank,MatthewGroh,Laura YichengFan,VincentZhao,NiLao,
Herman,NeilLeach,etal.2023. Artand HongraeLee,Da-ChengJuan,etal.2023.
thescienceofgenerativeai. Science, Rarr:Researchingandrevisingwhat
380(6650):1110–1111. languagemodelssay,usinglanguage
Fagni,Tiziano,FabrizioFalchi,Margherita models. InProceedingsofthe61stAnnual
Gambini,AntonioMartella,andMaurizio MeetingoftheAssociationforComputational
Tesconi.2021. TweepFake:About Linguistics(Volume1:LongPapers),pages
detectingdeepfaketweets. PLOSONE, 16477–16508.
16(5):e0251415. Gao,Tianyu,XingchengYao,andDanqi
Fan,Angela,YacineJernite,EthanPerez, Chen.2021. SimCSE:Simplecontrastive
DavidGrangier,JasonWeston,and learningofsentenceembeddings. In
MichaelAuli.2019. ELI5:Longform Proceedingsofthe2021Conferenceon
questionanswering. InProceedingsofthe EmpiricalMethodsinNaturalLanguage
57thAnnualMeetingoftheAssociationfor Processing,pages6894–6910,Association
ComputationalLinguistics,pages3558–3567, forComputationalLinguistics.
AssociationforComputational Gehrmann,Sebastian,HendrikStrobelt,and

### Linguistics. AlexanderRush.2019. GLTR:Statistical

Fan,Angela,MikeLewis,andYann detectionandvisualizationofgenerated
Dauphin.2018. Hierarchicalneuralstory text. InProceedingsofthe57thAnnual
generation. InProceedingsofthe56th MeetingoftheAssociationforComputational
AnnualMeetingoftheAssociationfor Linguistics:SystemDemonstrations,pages
ComputationalLinguistics(Volume1:Long 111–116,AssociationforComputational
Papers),pages889–898,Associationfor Linguistics.

### ComputationalLinguistics. Ghosal,SoumyaSuvra,Souradip

Fellbaum,Christiane.1998. WordNet:An Chakraborty,JonasGeiping,Furong
electroniclexicaldatabase. MITpress. Huang,DineshManocha,andAmritBedi.

## Asurveyonthepossibilities&

53

<!-- Page 54 -->

impossibilitiesofai-generatedtext chatgpt-generatedfakescienceusingreal
detection. TransactionsonMachineLearning publicationtext:Introducingxfakebibsa
Research. supervised-learningnetworkalgorithm.
Giorgi,Salvatore,DavidM.Markowitz, CoRR,abs/2308.11767.
NikitaSoni,VasudhaVaradarajan, Hanley,HansW.A.andZakirDurumeric.
SiddharthMangalik,andH.Andrew 2023. Machine-mademedia:Monitoring
Schwartz.2023. "isleptlikeababy":Using themobilizationofmachine-generated
humantraitstocharacterizedeceptive articlesonmisinformationand
chatgptandhumantext. InProceedingsof mainstreamnewswebsites. CoRR,
theIACT-The1stInternationalWorkshopon abs/2305.09820.
ImplicitAuthorCharacterizationfromTexts He,Xinlei,XinyueShen,ZeyuanChen,
forSearchandRetrievalheldinconjunction MichaelBackes,andYangZhang.2023.
withthe46thInternationalACMSIGIR Mgtbench:Benchmarking
ConferenceonResearchandDevelopmentin machine-generatedtextdetection. ArXiv
InformationRetrieval(SIGIR2023),Taipei, preprint,abs/2303.14822.
Taiwan,July27,2023,volume3477of Helm,HaydenS.,CareyE.Priebe,and
CEURWorkshopProceedings,pages23–37, WeiweiYang.2023. Astatisticalturingtest

### CEUR-WS.org. forgenerativemodels. CoRR,

Giorgi,Salvatore,LyleUngar,and abs/2309.08913.

### H.AndrewSchwartz.2021. Henrique,DaSilvaGameiro,Andrei

Characterizingsocialspambotsbytheir Kucharavy,andRachidGuerraoui.2023.
humantraits. InFindingsoftheAssociation Stochasticparrotslookingforstochastic
forComputationalLinguistics:ACL-IJCNLP parrots:Llmsareeasytofine-tuneand
2021,pages5148–5158,Associationfor hardtodetectwithotherllms. CoRR,
ComputationalLinguistics. abs/2304.08968.
Goodfellow,Ian,JeanPouget-Abadie,Mehdi Hill,Felix,AntoineBordes,SumitChopra,
Mirza,BingXu,DavidWarde-Farley, andJasonWeston.2016. Thegoldilocks
SherjilOzair,AaronCourville,andYoshua principle:Readingchildren’sbookswith
Bengio.2020. Generativeadversarial explicitmemoryrepresentations. In4th
networks. CommunicationsoftheACM, InternationalConferenceonLearning
63(11):139–144. Representations,ICLR2016,SanJuan,Puerto
Graves,Alex.2012. Sequencetransduction Rico,May2-4,2016,ConferenceTrack
withrecurrentneuralnetworks. arXiv Proceedings.
preprintarXiv:1211.3711. Holtzman,Ari,JanBuys,LiDu,Maxwell
Gu,Chenxi,ChengsongHuang,Xiaoqing Forbes,andYejinChoi.2020. Thecurious
Zheng,Kai-WeiChang,andCho-Jui caseofneuraltextdegeneration. In8th
Hsieh.2022. Watermarkingpre-trained InternationalConferenceonLearning
languagemodelswithbackdooring. ArXiv Representations,ICLR2020,AddisAbaba,
preprint,abs/2210.07543. Ethiopia,April26-30,2020,
Guo,Biyang,XinZhang,ZiyuanWang, OpenReview.net.
MinqiJiang,JinranNie,YuxuanDing, Horne,BenjaminandSibelAdali.2017. This
JianweiYue,andYupengWu.2023. How justin:Fakenewspacksalotintitle,uses
closeischatgpttohumanexperts? simpler,repetitivecontentintextbody,
comparisoncorpus,evaluation,and moresimilartosatirethanrealnews. In
detection. ArXivpreprint,abs/2301.07597. ProceedingsoftheinternationalAAAI
Guo,Mandy,ZihangDai,DennyVrandecˇic´, conferenceonwebandsocialmedia,
andRamiAl-Rfou.2020. Wiki-40B: volume11,pages759–766.
Multilinguallanguagemodeldataset. In Hou,AbeBohan,JingyuZhang,Tianxing
ProceedingsoftheTwelfthLanguage He,YichenWang,Yung-SungChuang,
ResourcesandEvaluationConference,pages HongweiWang,LingfengShen,
2440–2452,EuropeanLanguageResources BenjaminVanDurme,DanielKhashabi,

### Association. andYuliaTsvetkov.2023. Semstamp:A

Guo,ZhenandShangdiYu.2023. semanticwatermarkwithparaphrastic
Authentigpt:Detecting robustnessfortextgeneration. CoRR,
machine-generatedtextviablack-box abs/2310.03991.
languagemodelsdenoising. CoRR, Hu,Xiaomeng,Pin-YuChen,andTsung-Yi
abs/2311.07700. Ho.2023. Radar:Robustai-textdetection
Hamed,AhmedAbdeenandXindongWu. viaadversariallearning. ArXivpreprint,

## Improvingdetectionof abs/2307.03838.

54

<!-- Page 55 -->


### Wuetal. ASurveyonLLM-GeneratedTextDetection

Ibrahim,Hazem,FengyuanLiu,Rohail Processingandthe9thInternationalJoint
Asim,BalarajuBattu,Sidahmed ConferenceonNaturalLanguageProcessing
Benabderrahmane,BasharAlhafni,Wifag (EMNLP-IJCNLP),pages2567–2577,
Adnan,TukaAlhanai,BedoorK.AlShebli, AssociationforComputational
RiyadhBaghdadi,JocelynJ.Bélanger, Linguistics.
ElenaBeretta,KemalCelik,Moumena Jin,Zhuoran,YuboChen,DianboSui,
Chaqfeh,MohammedF.Daqaq,ZaynabEl ChenhaoWang,ZhipengXue,andJun
Bernoussi,DarylFougnie,BorjaGarcia Zhao.2021. Cogie:Aninformation
deSoto,AlbertoGandolfi,AndrásGyörgy, extractiontoolkitforbridgingtextsand
NizarHabash,J.AndrewHarris,Aaron cognet. InProceedingsoftheJointConference
Kaufman,LefterisKirousis,Korhan ofthe59thAnnualMeetingoftheAssociation
Kocak,KangsanLee,SeungahS.Lee, forComputationalLinguisticsandthe11th
SamreenMalik,MichailManiatakos, InternationalJointConferenceonNatural
DavidMelcher,AzzamMourad,Minsu LanguageProcessing,ACL2021-System
Park,MahmoudRasras,AlicjaReuben, Demonstrations,Online,August1-6,2021,
DaniaZantout,NancyW.Gleason,Kinga pages92–98,Associationfor
Makovi,TalalRahwan,andYasirZaki. ComputationalLinguistics.

## Perception,performance,and Kalinichenko,LeonidA,VladimirV

detectabilityofconversationalartificial Korenkov,VladislavPShirikov,AlexeyN
intelligenceacross32universitycourses. Sissakian,andOlegVSunturenko.2003.

### CoRR,abs/2305.13934. Digitallibraries:Advancedmethodsand

Ippolito,Daphne,DanielDuckworth,Chris technologies,digitalcollections. D-Lib
Callison-Burch,andDouglasEck.2020. Magazine,9(1):1082–9873.
Automaticdetectionofgeneratedtextis Kang,Dongyeop,WaleedAmmar,Bhavana
easiestwhenhumansarefooled. In Dalvi,MadeleinevanZuylen,Sebastian
Proceedingsofthe58thAnnualMeetingofthe Kohlmeier,EduardHovy,andRoy
AssociationforComputationalLinguistics, Schwartz.2018. Adatasetofpeerreviews
pages1808–1822,Associationfor (PeerRead):Collection,insightsandNLP
ComputationalLinguistics. applications. InProceedingsofthe2018
Jawahar,Ganesh,Muhammad ConferenceoftheNorthAmericanChapterof
Abdul-Mageed,andLaksLakshmanan, theAssociationforComputationalLinguistics:
V.S.2020. Automaticdetectionofmachine HumanLanguageTechnologies,Volume1
generatedtext:Acriticalsurvey. In (LongPapers),pages1647–1661,
Proceedingsofthe28thInternational AssociationforComputational
ConferenceonComputationalLinguistics, Linguistics.
pages2296–2309,InternationalCommittee Kasneci,Enkelejda,KathrinSeßler,Stefan
onComputationalLinguistics. Küchemann,MariaBannert,Daryna
Ji,Ziwei,NayeonLee,RitaFrieske,Tiezheng Dementieva,FrankFischer,UrsGasser,
Yu,DanSu,YanXu,EtsukoIshii,YeJin GeorgGroh,StephanGünnemann,Eyke
Bang,AndreaMadotto,andPascaleFung. Hüllermeier,etal.2023. Chatgptforgood?

## Surveyofhallucinationinnatural onopportunitiesandchallengesoflarge

languagegeneration. ACMComputing languagemodelsforeducation. Learning
Surveys,55(12):1–38. andIndividualDifferences,103:102274.
Jiao,Xiaoqi,YichunYin,LifengShang,Xin Kirchenbauer,John,JonasGeiping,Yuxin
Jiang,XiaoChen,LinlinLi,FangWang, Wen,JonathanKatz,IanMiers,andTom
andQunLiu.2020. Tinybert:Distilling Goldstein.2023a. Awatermarkforlarge
BERTfornaturallanguageunderstanding. languagemodels. InInternational
InFindingsoftheAssociationfor ConferenceonMachineLearning,ICML2023,
ComputationalLinguistics:EMNLP2020, 23-29July2023,Honolulu,Hawaii,USA,
OnlineEvent,16-20November2020,volume volume202ofProceedingsofMachine
EMNLP2020ofFindingsofACL,pages LearningResearch,pages17061–17084,
4163–4174,AssociationforComputational PMLR.

### Linguistics. Kirchenbauer,John,JonasGeiping,Yuxin

Jin,Qiao,BhuwanDhingra,ZhengpingLiu, Wen,ManliShu,KhalidSaifullah,Kezhi
WilliamCohen,andXinghuaLu.2019. Kong,KasunFernando,AniruddhaSaha,
PubMedQA:Adatasetforbiomedical MicahGoldblum,andTomGoldstein.
researchquestionanswering. In 2023b. Onthereliabilityofwatermarksfor
Proceedingsofthe2019Conferenceon largelanguagemodels. CoRR,
EmpiricalMethodsinNaturalLanguage abs/2306.04634.
55

<!-- Page 56 -->

Kocˇiský,Tomáš,JonathanSchwarz,Phil contentwithrelativeentropyscoring. In
Blunsom,ChrisDyer,KarlMoritz Proceedingsofthe2008International
Hermann,GáborMelis,andEdward ConferenceonUncoveringPlagiarism,
Grefenstette.2018. TheNarrativeQA AuthorshipandSocialSoftware
readingcomprehensionchallenge. Misuse-Volume377,pages27–31.

### TransactionsoftheAssociationfor Lee,BruceW.,YooSungJang,and

ComputationalLinguistics,6:317–328. JasonHyung-JongLee.2021. Pushingon
Koike,Ryuto,MasahiroKaneko,andNaoaki textreadabilityassessment:Atransformer
Okazaki.2023a. Howyoupromptmatters! meetshandcraftedlinguisticfeatures. In
eventask-orientedconstraintsin Proceedingsofthe2021Conferenceon
instructionsaffectllm-generatedtext EmpiricalMethodsinNaturalLanguage
detection. CoRR,abs/2311.08369. Processing,EMNLP2021,VirtualEvent/
Koike,Ryuto,MasahiroKaneko,andNaoaki PuntaCana,DominicanRepublic,7-11
Okazaki.2023b. Outfox:Llm-generated November,2021,pages10669–10686,
essaydetectionthroughin-context AssociationforComputational
learningwithadversariallygenerated Linguistics.
examples. ArXivpreprint,abs/2307.11729. Lee,Haejun,DrewA.Hudson,Kangwook
Kojima,Takeshi,ShixiangShaneGu,Machel Lee,andChristopherD.Manning.2020.

### Reid,YutakaMatsuo,andYusuke SLM:Learningadiscourselanguage

Iwasawa.2022. Largelanguagemodels representationwithsentenceunshuffling.
arezero-shotreasoners. InNeurIPS. InProceedingsofthe2020Conferenceon
Krishna,Kalpesh,YixiaoSong,Marzena EmpiricalMethodsinNaturalLanguage
Karpinska,JohnWieting,andMohitIyyer. Processing(EMNLP),pages1551–1562,

## Paraphrasingevadesdetectorsof AssociationforComputational

ai-generatedtext,butretrievalisan Linguistics.
effectivedefense. ArXivpreprint, Lee,Jooyoung,ThaiLe,JinghuiChen,and
abs/2303.13408. DongwonLee.2023a.Dolanguagemodels
Kuditipudi,Rohith,JohnThickstun, plagiarize? InProceedingsoftheACMWeb
TatsunoriHashimoto,andPercyLiang. Conference2023,pages3637–3647.

## Robustdistortion-freewatermarks Lee,Taehyun,SeokheeHong,JaewooAhn,

forlanguagemodels. CoRR, IlgeeHong,HwaranLee,SangdooYun,
abs/2307.15593. JaminShin,andGunheeKim.2023b. Who
Kulkarni,Pranav,ZiqingJi,YanXu,Marko wrotethiscode?watermarkingforcode
Neskovic,andKevinNolan.2023. generation. CoRR,abs/2305.15060.
Exploringsemanticperturbationson Li,Linyang,PengyuWang,KeRen,
grover. CoRR,abs/2302.00509. TianxiangSun,andXipengQiu.2023a.
Kumarage,Tharindu,AmritaBhattacharjee, Origintracinganddetectingofllms.
DjordjePadejski,KristyRoschke,Dan CoRR,abs/2304.14072.
Gillmor,ScottW.Ruston,HuanLiu,and Li,Xian,PingYu,ChuntingZhou,Timo
JoshuaGarland.2023a. J-guard: Schick,LukeZettlemoyer,OmerLevy,
Journalismguidedadversariallyrobust JasonWeston,andMikeLewis.2023b.
detectionofai-generatednews. CoRR, Self-alignmentwithinstruction
abs/2309.03164. backtranslation. ArXivpreprint,
Kumarage,Tharindu,ParasSheth,Raha abs/2308.06259.
Moraffah,JoshuaGarland,andHuanLiu. Li,Yafu,QintongLi,LeyangCui,WeiBi,
2023b. Howreliableareai-generated-text LongyueWang,LinyiYang,ShumingShi,
detectors?anassessmentframeworkusing andYueZhang.2023c. Deepfaketext
evasivesoftprompts. InFindingsofthe detectioninthewild. CoRR,
AssociationforComputationalLinguistics: abs/2305.13242.
EMNLP2023,Singapore,December6-10, Liang,Gongbo,JesusGuerrero,andIzzat
2023,pages1337–1349,Associationfor Alsmadi.2023. Mutation-based

### ComputationalLinguistics. adversarialattacksonneuraltext

Lambert,Nathan,LouisCastricato,Leandro detectors. ArXivpreprint,abs/2302.05794.
vonWerra,andAlexHavrilla.2022. Liang,Weixin,MertYuksekgonul,Yining
Illustratingreinforcementlearningfrom Mao,EricWu,andJamesZou.2023a. Gpt
humanfeedback(rlhf). HuggingFaceBlog. detectorsarebiasedagainstnon-native
Https://huggingface.co/blog/rlhf. englishwriters. InICLR2023Workshopon
Lavergne,Thomas,TanguyUrvoy,and TrustworthyandReliableLarge-ScaleMachine
FrançoisYvon.2008. Detectingfake LearningModels.
56

<!-- Page 57 -->


### Wuetal. ASurveyonLLM-GeneratedTextDetection

Liang,Yaobo,ChenfeiWu,TingSong, Liu,Zeyan,ZijunYao,FengjunLi,and
WenshanWu,YanXia,YuLiu,YangOu, BoLuo.2023d. Checkmeifyoucan:
ShuaiLu,LeiJi,ShaoguangMao,etal. Detectingchatgpt-generatedacademic
2023b. Taskmatrix.ai:Completingtasks writingusingcheckgpt. ArXivpreprint,
byconnectingfoundationmodelswith abs/2306.05524.
millionsofapis. ArXivpreprint, Lu,Ning,ShengcaiLiu,RuiHe,and
abs/2303.16434. KeTang.2023. Largelanguagemodelscan
Liao,Wenxiong,ZhengliangLiu,Haixing beguidedtoevadeai-generatedtext
Dai,ShaochenXu,ZihaoWu,Yiyang detection. ArXivpreprint,abs/2305.10847.
Zhang,XiaokeHuang,DajiangZhu, Lu,Yaojie,QingLiu,DaiDai,XinyanXiao,
HongminCai,TianmingLiu,andXiang HongyuLin,XianpeiHan,LeSun,and
Li.2023a. Differentiatechatgpt-generated HuaWu.2022. Unifiedstructure
andhuman-writtenmedicaltexts. CoRR, generationforuniversalinformation
abs/2304.11567. extraction. InProceedingsofthe60thAnnual
Liao,Wenxiong,ZhengliangLiu,Haixing MeetingoftheAssociationforComputational
Dai,ShaochenXu,ZihaoWu,Yiyang Linguistics(Volume1:LongPapers),ACL
Zhang,XiaokeHuang,DajiangZhu, 2022,Dublin,Ireland,May22-27,2022,
HongminCai,TianmingLiu,etal.2023b. pages5755–5772,Associationfor
Differentiatechatgpt-generatedand ComputationalLinguistics.
human-writtenmedicaltexts. ArXiv Lucas,EvanandTimothyHavens.2023.Gpts
preprint,abs/2304.11567. don’tkeepsecrets:Searchingforbackdoor
Lin,Stephanie,JacobHilton,andOwain watermarktriggersinautoregressive
Evans.2022. TruthfulQA:Measuringhow languagemodels. InProceedingsofthe3rd
modelsmimichumanfalsehoods. In WorkshoponTrustworthyNaturalLanguage
Proceedingsofthe60thAnnualMeetingofthe Processing(TrustNLP2023),pages242–248.
AssociationforComputationalLinguistics Ma,Yongqiang,JiaweiLiu,andFanYi.2023.
(Volume1:LongPapers),pages3214–3252, Isthisabstractgeneratedbyai?aresearch
AssociationforComputational forthegapbetweenai-generatedscientific
Linguistics. textandhuman-writtenscientifictext.
Littman,JustinandLauraWrubel.2019. ArXivpreprint,abs/2301.10416.

### ClimateChangeTweetsIds. Ma,Yongqiang,JiaweiLiu,FanYi,Qikai

Liu,Aiwei,LeyiPan,XumingHu,Shu’ang Cheng,YongHuang,WeiLu,and
Li,LijieWen,IrwinKing,andPhilipSYu. XiaozhongLiu.2023. Aivs.
2023a. Aprivatewatermarkforlarge human–differentiationanalysisof
languagemodels. ArXivpreprint, scientificcontentgeneration. arXiv,2301.
abs/2307.16230. Macko,Dominik,RóbertMóro,Adaku
Liu,Aiwei,LeyiPan,XumingHu,Shiao Uchendu,JasonSamuelLucas,Michiharu
Meng,andLijieWen.2023b. Asemantic Yamashita,MatúsPikuliak,IvanSrba,
invariantrobustwatermarkforlarge ThaiLe,DongwonLee,JakubSimko,and
languagemodels. CoRR,abs/2310.06356. MáriaBieliková.2023. Multitude:

### Liu,Xiaoming,ZhaohanZhang,Yichen Large-scalemultilingual

Wang,YuLan,andChaoShen.2022. Coco: machine-generatedtextdetection
Coherence-enhancedmachine-generated benchmark. InProceedingsofthe2023
textdetectionunderdatalimitationwith ConferenceonEmpiricalMethodsinNatural
contrastivelearning. ArXivpreprint, LanguageProcessing,EMNLP2023,
abs/2212.10341. Singapore,December6-10,2023,pages
Liu,Yikang,ZiyinZhang,WanyangZhang, 9960–9987.
ShisenYue,XiaojingZhao,Xinyuan Májovsky`,Martin,MartinCˇerny`,Mateˇj
Cheng,YiwenZhang,andHaiHu.2023c. Kasal,MartinKomarc,andDavidNetuka.
Argugpt:evaluating,understandingand 2023. Artificialintelligencecangenerate
identifyingargumentativeessays fraudulentbutauthentic-lookingscientific
generatedbygptmodels. ArXivpreprint, medicalarticles:Pandora’sboxhasbeen
abs/2304.07666. opened. JournalofMedicalInternet
Liu,Yinhan,MyleOtt,NamanGoyal,Jingfei Research,25:e46924.
Du,MandarJoshi,DanqiChen,Omer Mao,Chengzhi,CarlVondrick,HaoWang,
Levy,MikeLewis,LukeZettlemoyer,and andJunfengYang.2024. Raidar:
VeselinStoyanov.2019. Roberta:A generativeAIdetectionviarewriting.
robustlyoptimizedBERTpretraining CoRR,abs/2401.12970.
approach. CoRR,abs/1907.11692.
57

<!-- Page 58 -->

Markowitz,DavidM,JeffreyHancock,and 119–126.
JeremyBailenson.2023. Linguistic Mosca,Edoardo,MohamedHeshamIbrahim
markersofinherentaideceptionand Abdalla,PaoloBasso,Margherita
intentionalhumandeception:Evidence Musumeci,andGeorgGroh.2023.
fromhotelreviews. PsyArXivpreprint. Distinguishingfactfromfiction:A
McCarthy,PhilipM.2005. Anassessmentof benchmarkdatasetforidentifying
therangeandusefulnessoflexicaldiversity machine-generatedscientificpapersinthe
measuresandthepotentialofthemeasureof llmera. InProceedingsofthe3rdWorkshop
textual,lexicaldiversity(MTLD). Ph.D. onTrustworthyNaturalLanguageProcessing
thesis,TheUniversityofMemphis. (TrustNLP2023),pages190–207.
Mindner,Lorenz,TimSchlippe,andKristina Mostafazadeh,Nasrin,NathanaelChambers,
Schaaff.2023. Classificationofhuman- XiaodongHe,DeviParikh,DhruvBatra,
andai-generatedtexts:Investigating LucyVanderwende,PushmeetKohli,and
featuresforchatgpt. CoRR, JamesAllen.2016. Acorpusandcloze
abs/2308.05341. evaluationfordeeperunderstandingof
Mirsky,Yisroel,AmbraDemontis,Jaidip commonsensestories. InProceedingsofthe
Kotak,RamShankar,DengGelei,Liu 2016ConferenceoftheNorthAmerican
Yang,XiangyuZhang,MauraPintor, ChapteroftheAssociationforComputational
WenkeLee,YuvalElovici,etal.2022. The Linguistics:HumanLanguageTechnologies,
threatofoffensiveaitoorganizations. pages839–849,Associationfor
Computers&Security,page103006. ComputationalLinguistics.
Mitchell,Eric,YoonhoLee,Alexander Muñoz-Ortiz,Alberto,Carlos
Khazatsky,ChristopherD.Manning,and Gómez-Rodríguez,andDavidVilares.
ChelseaFinn.2023. Detectgpt:Zero-shot 2023. Contrastinglinguisticpatternsin
machine-generatedtextdetectionusing humanandllm-generatedtext. ArXiv
probabilitycurvature. InInternational preprint,abs/2308.09067.
ConferenceonMachineLearning,ICML2023, Munyer,TravisJ.E.andXinZhong.2023.
23-29July2023,Honolulu,Hawaii,USA, Deeptextmark:Deeplearningbasedtext
volume202ofProceedingsofMachine watermarkingfordetectionoflarge
LearningResearch,pages24950–24962, languagemodelgeneratedtext. CoRR,
PMLR. abs/2305.05773.
Mitrovic,Sandra,DavideAndreoletti,and Murakami,Soichiro,ShoHoshino,and
OmranAyoub.2023. Chatgptorhuman? PeinanZhang.2023. Naturallanguage
detectandexplain.explainingdecisionsof generationforadvertising:Asurvey.
machinelearningmodelfordetecting ArXivpreprint,abs/2306.12719.
shortchatgpt-generatedtext. CoRR, Muric,G,YWu,andEFerrara.2021.
abs/2301.13852. Covid-19vaccinehesitancyonsocial
Mitrovic´,Sandra,DavideAndreoletti,and media:Buildingapublictwitterdatasetof
OmranAyoub.2023. Chatgptorhuman? anti-vaccinecontent,vaccine
detectandexplain.explainingdecisionsof misinformationandconspiracies.2021;
machinelearningmodelfordetecting 1–10. ArXivpreprint,abs/2105.05134.
shortchatgpt-generatedtext. ArXiv Murtaza,Ghulam,LiyanaShuib,
preprint,abs/2301.13852. AinuddinWahidAbdulWahab,Ghulam
Moosavi,NafiseSadat,AndreasRücklé,Dan Mujtaba,GhulamMujtaba,HenryFriday
Roth,andIrynaGurevych.2021. Scigen:a Nweke,MohammedAliAl-garadi,Fariha
datasetforreasoning-awaretext Zulfiqar,GhulamRaza,andNorAniza
generationfromscientifictables. In Azmi.2020. Deeplearning-basedbreast
Thirty-fifthConferenceonNeuralInformation cancerclassificationthroughmedical
ProcessingSystemsDatasetsandBenchmarks imagingmodalities:stateoftheartand
Track(Round2). researchchallenges. ArtificialIntelligence
Morris,JohnX.,EliLifland,JinYongYoo, Review,53:1655–1720.
JakeGrigsby,DiJin,andYanjunQi.2020. Narayan,Shashi,ShayB.Cohen,andMirella
Textattack:Aframeworkforadversarial Lapata.2018. Don’tgivemethedetails,
attacks,dataaugmentation,and justthesummary!topic-aware
adversarialtraininginNLP. InProceedings convolutionalneuralnetworksforextreme
ofthe2020ConferenceonEmpiricalMethods summarization. InProceedingsofthe2018
inNaturalLanguageProcessing:System ConferenceonEmpiricalMethodsinNatural
Demonstrations,EMNLP2020-Demos, LanguageProcessing,pages1797–1807,
Online,November16-20,2020,pages AssociationforComputational
58

<!-- Page 59 -->


### Wuetal. ASurveyonLLM-GeneratedTextDetection


### Linguistics. DanielRodger,etal.2023. Generativeai

Nicks,Charlotte,EricMitchell,Rafael entailsacredit–blameasymmetry. ArXiv
Rafailov,ArchitSharma,ChristopherD preprint,abs/2305.15324.
Manning,ChelseaFinn,andStefano Price,GregoryandMarcDSakellarios.2023.
Ermon.2023. Languagemodeldetectors Theeffectivenessoffreesoftwarefor
areeasilyoptimizedagainst. InTheTwelfth detectingai-generatedwriting.
InternationalConferenceonLearning InternationalJournalofTeaching,Learning
Representations. andEducation,2(6).
OpenAI.2023. GPT-4technicalreport. CoRR, Pu,Jiameng,ZainSarwar,SifatMuhammad
abs/2303.08774. Abdullah,AbdullahRehman,Yoonjin
Orenstrakh,MichaelSheinman,Oscar Kim,ParantapaBhattacharya,Mobin
Karnalim,CarlosAnibalSuarez,and Javed,andBimalViswanath.2023a.
MichaelLiut.2023. Detecting Deepfaketextdetection:Limitationsand
llm-generatedtextincomputing opportunities. In44thIEEESymposiumon
education:Acomparativestudyfor SecurityandPrivacy,SP2023,SanFrancisco,
chatgptcases. ArXivpreprint, CA,USA,May21-25,2023,pages
abs/2307.07411. 1613–1630,IEEE.
Ouyang,Long,JeffWu,XuJiang,Diogo Pu,Xiao,JingyuZhang,XiaochuangHan,
Almeida,CarrollLWainwright,Pamela YuliaTsvetkov,andTianxingHe.2023b.

### Mishkin,ChongZhang,Sandhini Onthezero-shotgeneralizationof

Agarwal,KatarinaSlama,AlexRay,etal. machine-generatedtextdetectors. In

## Traininglanguagemodelstofollow FindingsoftheAssociationforComputational

instructionswithhumanfeedback,2022. Linguistics:EMNLP2023,pages4799–4808.
ArXivpreprint,abs/2203.02155. Qiu,Xipeng,TianxiangSun,YigeXu,Yunfan
Pagnoni,Artidoro,MartinGraciarena,and Shao,NingDai,andXuanjingHuang.
YuliaTsvetkov.2022a. Threatscenarios 2020. Pre-trainedmodelsfornatural
andbestpracticestodetectneuralfake languageprocessing:Asurvey. Science
news. InProceedingsofthe29th ChinaTechnologicalSciences,
InternationalConferenceonComputational 63(10):1872–1897.
Linguistics,pages1233–1249,International Quidwai,MujahidAli,ChunhuiLi,and
CommitteeonComputationalLinguistics. ParijatDube.2023. BeyondblackboxAI
Pagnoni,Artidoro,MartinGraciarena,and generatedplagiarismdetection:From
YuliaTsvetkov.2022b. Threatscenarios sentencetodocumentlevel. InProceedings
andbestpracticestodetectneuralfake ofthe18thWorkshoponInnovativeUseof
news. InProceedingsofthe29th NLPforBuildingEducationalApplications,
InternationalConferenceonComputational BEA@ACL2023,Toronto,Canada,13July
Linguistics,COLING2022,Gyeongju, 2023,pages727–735,Associationfor
RepublicofKorea,October12-17,2022,pages ComputationalLinguistics.
1233–1249,InternationalCommitteeon Radford,Alec,JeffreyWu,RewonChild,

### ComputationalLinguistics. DavidLuan,DarioAmodei,Ilya

Peng,Xinlin,YingZhou,BenHe,LeSun, Sutskever,etal.2019. Languagemodels
andYingfeiSun.2024. Hiddingthe areunsupervisedmultitasklearners.
ghostwriters:Anadversarialevaluationof OpenAIblog,1(8):9.
ai-generatedstudentessaydetection. Raffel,Colin,NoamShazeer,AdamRoberts,

### CoRR,abs/2402.00412. KatherineLee,SharanNarang,Michael

Piccolo,StephenR,PaulDenny,Andrew Matena,YanqiZhou,WeiLi,andPeterJ.
Luxton-Reilly,SamuelPayne,andPerryG Liu.2020. Exploringthelimitsoftransfer
Ridge.2023. Manybioinformatics learningwithaunifiedtext-to-text
programmingtaskscanbeautomated transformer. J.Mach.Learn.Res.,
withchatgpt. ArXivpreprint, 21:140:1–140:67.
abs/2303.13528. Rajpurkar,Pranav,JianZhang,Konstantin
Por,LipYee,KokSheikWong,andKokOnn Lopyrev,andPercyLiang.2016. SQuAD:
Chee.2012. Unispach:Atext-baseddata 100,000+questionsformachine
hidingmethodusingunicodespace comprehensionoftext. InProceedingsofthe
characters. J.Syst.Softw.,85(5):1075–1082. 2016ConferenceonEmpiricalMethodsin
PorsdamMann,Sebastian,BrianDEarp, NaturalLanguageProcessing,pages
SvenNyholm,JohnDanaher,Nikolaj 2383–2392,AssociationforComputational
Møller,HilaryBowman-Smart,Joshua Linguistics.
Hatherley,JulianKoplin,MonikaPlozza,
59

<!-- Page 60 -->

Ren,Shuhuai,YiheDeng,KunHe,and Multilinguality,Multimodality,and
WanxiangChe.2019. Generatingnatural Interaction-14thInternationalConferenceof
languageadversarialexamplesthrough theCLEFAssociation,CLEF2023,
probabilityweightedwordsaliency. In Thessaloniki,Greece,September18-21,2023,
Proceedingsofthe57thAnnualMeetingofthe Proceedings,volume14163ofLectureNotes
AssociationforComputationalLinguistics, inComputerScience,pages121–132,
pages1085–1097,Associationfor Springer.
ComputationalLinguistics. Schaaff,Kristina,TimSchlippe,andLorenz
Rizzo,StefanoGiovanni,FlavioBertini,and Mindner.2023. Classificationofhuman-
DaniloMontesi.2016. Content-preserving andai-generatedtextsforenglish,french,
textwatermarkingthroughunicode german,andspanish. InProceedingsofthe
homoglyphsubstitution. InProceedingsof 6thInternationalConferenceonNatural
the20thInternationalDatabaseEngineering LanguageandSpeechProcessing(ICNLSP
&ApplicationsSymposium,IDEAS2016, 2023),VirtualEvent,16-17December2023,
Montreal,QC,Canada,July11-13,2016, pages1–10,Associationfor
pages97–104,ACM. ComputationalLinguistics.
Rodriguez,Juan,ToddHay,DavidGros, Schneider,Sinclair,FlorianSteuber,Joao
ZainShamsi,andRaviSrinivasan.2022a. A.G.Schneider,andGabiDreoRodosek.

### Cross-domaindetectionof 2023. Howwellcanmachine-generated

GPT-2-generatedtechnicaltext. In textsbeidentifiedandcanlanguage
Proceedingsofthe2022Conferenceofthe modelsbetrainedtoavoididentification?
NorthAmericanChapteroftheAssociationfor CoRR,abs/2310.16992.
ComputationalLinguistics:HumanLanguage Schulman,John,FilipWolski,Prafulla
Technologies,pages1213–1233,Association Dhariwal,AlecRadford,andOlegKlimov.
forComputationalLinguistics. 2017a. Proximalpolicyoptimization
Rodriguez,JuanDiego,ToddHay,David algorithms. CoRR,abs/1707.06347.
Gros,ZainShamsi,andRaviSrinivasan. Schulman,John,FilipWolski,Prafulla
2022b. Cross-domaindetectionof Dhariwal,AlecRadford,andOlegKlimov.
gpt-2-generatedtechnicaltext. In 2017b. Proximalpolicyoptimization
Proceedingsofthe2022Conferenceofthe algorithms. ArXivpreprint,
NorthAmericanChapteroftheAssociationfor abs/1707.06347.
ComputationalLinguistics:HumanLanguage Schuster,Tal,RoeiSchuster,DarshJ.Shah,
Technologies,NAACL2022,Seattle,WA, andReginaBarzilay.2020a. The
UnitedStates,July10-15,2022,pages limitationsofstylometryfordetecting
1213–1233,AssociationforComputational machine-generatedfakenews. Comput.
Linguistics. Linguistics,46(2):499–510.
Sadasivan,VinuSankar,AounonKumar, Schuster,Tal,RoeiSchuster,DarshJ.Shah,
SriramBalasubramanian,WenxiaoWang, andReginaBarzilay.2020b. The
andSoheilFeizi.2023. Canai-generated limitationsofstylometryfordetecting
textbereliablydetected? ArXivpreprint, machine-generatedfakenews.
abs/2303.11156. ComputationalLinguistics,46(2):499–510.
Saeed,WaddahandChristianOmlin.2023. Seals,S.M.andValerieL.Shalin.2023.
Explainableai(xai):Asystematic Long-formanalogiesgeneratedbychatgpt
meta-surveyofcurrentchallengesand lackhuman-likepsycholinguistic
futureopportunities. Knowledge-Based properties. CoRR,abs/2306.04537.

### Systems,263:110273. Shah,Aditya,PrateekRanka,UrmiDedhia,

Sarvazyan,AregMikael,JoséÁngel ShrutiPrasad,SiddhiMuni,andKiran

### González,PaoloRosso,andMarc Bhowmick.2023. Detectingand

Franco-Salvador.2023a. Supervised unmaskingai-generatedtextsthrough
machine-generatedtextdetectors:Family explainableartificialintelligenceusing
andscalematters. InInternational stylisticfeatures. InternationalJournalof
ConferenceoftheCross-LanguageEvaluation AdvancedComputerScienceand
ForumforEuropeanLanguages,pages Applications,14(10).
121–132,Springer. Shen,Dinghan,MingzhiZheng,Yelong
Shen,YanruQu,andWeizhuChen.2020.
Sarvazyan,AregMikael,JoséÁngel
Asimplebuttough-to-beatdata

### González,PaoloRosso,andMarc

augmentationapproachfornatural

### Franco-Salvador.2023b. Supervised

languageunderstandingandgeneration.
machine-generatedtextdetectors:Family
ArXivpreprint,abs/2009.13818.
andscalematters. InExperimentalIRMeets
60

<!-- Page 61 -->


### Wuetal. ASurveyonLLM-GeneratedTextDetection

Shevlane,Toby,SebastianFarquhar,Ben HC3plus:Asemantic-invarianthuman
Garfinkel,MaryPhuong,Jess chatgptcomparisoncorpus. CoRR,
Whittlestone,JadeLeung,Daniel abs/2309.02731.
Kokotajlo,NahemaMarchal,Markus Susnjak,Teo.2022. Chatgpt:Theendof
Anderljung,NoamKolt,LewisHo,Divya onlineexamintegrity? ArXivpreprint,
Siddarth,ShaharAvin,WillHawkins, abs/2212.09292.
BeenKim,IasonGabriel,VijayBolina,Jack Tang,Ruixiang,Yu-NengChuang,andXia
Clark,YoshuaBengio,PaulF.Christiano, Hu.2023. Thescienceofdetecting
andAllanDafoe.2023. Modelevaluation llm-generatedtexts. CoRR,
forextremerisks. CoRR,abs/2305.15324. abs/2303.07205.
Shi,ZhouxingandMinlieHuang.2020. Tang,Ruixiang,QizhangFeng,NinghaoLiu,
Robustnesstomodificationwithshared FanYang,andXiaHu.2023. Didyoutrain
wordsinparaphraseidentification. In onmydataset?towardspublicdataset
FindingsoftheAssociationforComputational protectionwithclean-labelbackdoor
Linguistics:EMNLP2020,pages164–171, watermarking. CoRR,abs/2303.11470.
AssociationforComputational Taori,Rohan,IshaanGulrajani,Tianyi

### Linguistics. Zhang,YannDubois,XuechenLi,Carlos

Shi,Zhouxing,YihanWang,FanYin, Guestrin,PercyLiang,andTatsunoriB.
XiangningChen,Kai-WeiChang,and Hashimoto.2023. Stanfordalpaca:An
Cho-JuiHsieh.2023. Redteaming instruction-followingllamamodel.
languagemodeldetectorswithlanguage https://github.com/tatsu-lab/
models. ArXivpreprint,abs/2305.19713. stanford_alpaca.
Solaiman,Irene,MilesBrundage,JackClark, Thirunavukarasu,ArunJames,Darren
AmandaAskell,ArielHerbert-Voss,Jeff ShuJengTing,KabilanElangovan,Laura
Wu,AlecRadford,GretchenKrueger, Gutierrez,TingFangTan,andDaniel
JongWookKim,SarahKreps,etal.2019. ShuWeiTing.2023. Largelanguage
Releasestrategiesandthesocialimpactsof modelsinmedicine. Naturemedicine,
languagemodels. ArXivpreprint, pages1–11.
abs/1908.09203. Topkara,Umut,MercanTopkara,and
Soni,MayankandVincentWade.2023a. MikhailJ.Atallah.2006. Thehiding
Comparingabstractivesummaries virtuesofambiguity:quantifiablyresilient
generatedbychatgpttorealsummaries watermarkingofnaturallanguagetext
throughblindedreviewersandtext throughsynonymsubstitutions. In
classificationalgorithms. CoRR, Proceedingsofthe8thworkshopon
abs/2303.17650. Multimedia&Security,MM&Sec2006,
Soni,MayankandVincentP.Wade.2023b. Geneva,Switzerland,September26-27,2006,
Comparingabstractivesummaries pages164–174,ACM.
generatedbychatgpttorealsummaries Touvron,Hugo,ThibautLavril,Gautier
throughblindedreviewersandtext Izacard,XavierMartinet,Marie-Anne
classificationalgorithms. ArXivpreprint, Lachaux,TimothéeLacroix,Baptiste
abs/2303.17650. Rozière,NamanGoyal,EricHambro,
Stiff,HaraldandFredrikJohansson.2022. FaisalAzhar,AurélienRodriguez,

### Detectingcomputer-generated ArmandJoulin,EdouardGrave,and

disinformation. Int.J.DataSci.Anal., GuillaumeLample.2023. Llama:Open
13(4):363–383. andefficientfoundationlanguagemodels.
Stokel-Walker,Chris.2022. Aibotchatgpt CoRR,abs/2302.13971.
writessmartessays-shouldacademics Tripto,NafisIrtiza,AdakuUchendu,Thai
worry? Nature. Le,MattiaSetzu,FoscaGiannotti,and
Stokel-Walker,ChrisandRichard DongwonLee.2023. HANSEN:human

### VanNoorden.2023. Whatchatgptand andAIspokentextbenchmarkfor

generativeaimeanforscience. Nature, authorshipanalysis. CoRR,
614(7947):214–216. abs/2310.16746.
Su,Jinyan,TerryYueZhuo,DiWang,and Tu,Shangqing,ChunyangLi,JifanYu,
PreslavNakov.2023a. Detectllm: XiaozhiWang,LeiHou,andJuanziLi.
Leveraginglogrankinformationfor 2023. Chatlog:Recordingandanalyzing
zero-shotdetectionofmachine-generated chatgptacrosstime. CoRR,
text. CoRR,abs/2306.05540. abs/2304.14106.
Su,Zhenpeng,XingWu,WeiZhou, Tulchinskii,Eduard,KristianKuznetsov,
GuangyuanMa,andSonglinHu.2023b. LaidaKushnareva,DaniilCherniavskii,
61

<!-- Page 62 -->

SergueiBarannikov,IrinaPiontkovskaya, Walters,WilliamH.2023. Theeffectiveness
SergeyNikolenko,andEvgenyBurnaev. ofsoftwaredesignedtodetect

## Intrinsicdimensionestimationfor ai-generatedwriting:Acomparisonof16

robustdetectionofai-generatedtexts. aitextdetectors. OpenInformationScience,
ArXivpreprint,abs/2306.04723. 7(1):20220158.
Uchendu,Adaku,ThaiLe,andDongwon Wang,Alex,AmanpreetSingh,Julian
Lee.2023a. Attributionandobfuscationof Michael,FelixHill,OmerLevy,and
neuraltextauthorship:Adatamining SamuelR.Bowman.2019. GLUE:A
perspective. SIGKDDExplor.Newsl., multi-taskbenchmarkandanalysis
25(1):1–18. platformfornaturallanguage
Uchendu,Adaku,ThaiLe,andDongwon understanding. In7thInternational
Lee.2023b. Toproberta:Topology-aware ConferenceonLearningRepresentations,
authorshipattributionofdeepfaketexts. ICLR2019,NewOrleans,LA,USA,May6-9,
CoRR,abs/2309.12934. 2019,OpenReview.net.
Uchendu,Adaku,ThaiLe,KaiShu,and Wang,Pengyu,LinyangLi,KeRen,Botian
DongwonLee.2020. Authorship Jiang,DongZhang,andXipengQiu.
attributionforneuraltextgeneration. In 2023a. Seqxgpt:Sentence-level
Proceedingsofthe2020Conferenceon ai-generatedtextdetection. CoRR,
EmpiricalMethodsinNaturalLanguage abs/2310.08903.
Processing(EMNLP),pages8384–8395, Wang,Yuxia,JonibekMansurov,Petar
AssociationforComputational Ivanov,JinyanSu,ArtemShelmanov,

### Linguistics. AkimTsvigun,ChenxiWhitehouse,

Uchendu,Adaku,JooyoungLee,HuaShen, OsamaMohammedAfzal,Tarek
andThaiLe.2023. Doeshuman Mahmoud,AlhamFikriAji,etal.2023b.
collaborationenhancetheaccuracyof M4:Multi-generator,multi-domain,and
identifyingllm-generateddeepfaketexts? multi-lingualblack-box
ArXivpreprint,abs/2304.01002. machine-generatedtextdetection. ArXiv
Uchendu,Adaku,ZeyuMa,ThaiLe,Rui preprint,abs/2305.14902.
Zhang,andDongwonLee.2021. Wang,Zecong,JiaxiCheng,ChenCui,and

### TURINGBENCH:Abenchmark ChenhaoYu.2023c. ImplementingBERT

environmentforTuringtestintheageof andfine-tunedrobertatodetectAI
neuraltextgeneration. InFindingsofthe generatednewsbychatgpt. CoRR,
AssociationforComputationalLinguistics: abs/2306.07401.

### EMNLP2021,pages2001–2016, Weber-Wulff,Debora,Alla

AssociationforComputational Anohina-Naumeca,SonjaBjelobaba,

### Linguistics. TomášFolty`nek,JeanGuerrero-Dib,

Vasilatos,Christoforos,ManaarAlam,Talal OlumidePopoola,PetrŠigut,andLorna
Rahwan,YasirZaki,andMichail Waddington.2023. Testingofdetection
Maniatakos.2023. Howkgpt:Investigating toolsforai-generatedtext. International
thedetectionofchatgpt-generated JournalforEducationalIntegrity,19(1):26.
universitystudenthomeworkthrough Weber-Wulff,Debora,Alla
context-awareperplexityanalysis. ArXiv Anohina-Naumeca,SonjaBjelobaba,
preprint,abs/2305.18226. TomásFoltýnek,JeanGuerrero-Dib,
Venkatraman,Saranya,AdakuUchendu, OlumidePopoola,PetrSigut,andLorna
andDongwonLee.2023. Gpt-who:An Waddington.2023. Testingofdetection
informationdensity-based toolsforai-generatedtext. CoRR,
machine-generatedtextdetector. CoRR, abs/2306.15666.
abs/2310.06202. Wei,Jason,XuezhiWang,DaleSchuurmans,
Verma,Vivek,EveFleisig,NicholasTomlin, MaartenBosma,FeiXia,EdChi,QuocV
andDanKlein.2023. Ghostbuster: Le,DennyZhou,etal.2022.
Detectingtextghostwrittenbylarge Chain-of-thoughtpromptingelicits
languagemodels. CoRR,abs/2305.15047. reasoninginlargelanguagemodels.
Veselovsky,Veniamin,ManoelHortaRibeiro, AdvancesinNeuralInformationProcessing
andRobertWest.2023. Artificialartificial Systems,35:24824–24837.
artificialintelligence:Crowdworkers Weidinger,Laura,JohnMellor,Maribeth
widelyuselargelanguagemodelsfortext Rauh,ConorGriffin,JonathanUesato,
productiontasks. ArXivpreprint, Po-SenHuang,MyraCheng,MiaGlaese,
abs/2306.07899. BorjaBalle,AtoosaKasirzadeh,etal.2021.
Ethicalandsocialrisksofharmfrom
62

<!-- Page 63 -->


### Wuetal. ASurveyonLLM-GeneratedTextDetection

languagemodels(2021). ArXivpreprint, Yang,Xi,JieZhang,KejiangChen,Weiming
abs/2112.04359. Zhang,ZehuaMa,FengWang,and
Weng,Luoxuan,MinfengZhu,KamKwai NenghaiYu.2022. Tracingtextprovenance
Wong,ShiLiu,JiashunSun,HangZhu, viacontext-awarelexicalsubstitution. In
DongmingHan,andWeiChen.2023. Thirty-SixthAAAIConferenceonArtificial
Towardsanunderstandingand Intelligence,AAAI2022,Thirty-Fourth
explanationformixed-initiativeartificial ConferenceonInnovativeApplicationsof
scientifictextdetection. ArXivpreprint, ArtificialIntelligence,IAAI2022,The
abs/2304.05011. TwelvethSymposiumonEducational
Wikipedia.2023. Largelanguagemodelsand AdvancesinArtificialIntelligence,EAAI
copyright. 2022VirtualEvent,February22-March1,
Wolff,Max.2020. Attackingneuraltext 2022,pages11613–11621,AAAIPress.
detectors. CoRR,abs/2002.11768. Yang,Xianjun,WeiCheng,LindaR.Petzold,
Wu,Kangxi,LiangPang,HuaweiShen, WilliamYangWang,andHaifengChen.
XueqiCheng,andTat-SengChua.2023. 2023b. DNA-GPT:divergentn-gram
Llmdet:Athirdpartylargelanguage analysisfortraining-freedetectionof
modelsgeneratedtextdetectiontool. In gpt-generatedtext. CoRR,abs/2305.17359.
FindingsoftheAssociationforComputational Yang,Zhilin,ZihangDai,YimingYang,
Linguistics:EMNLP2023,Singapore, JaimeG.Carbonell,RuslanSalakhutdinov,
December6-10,2023,pages2113–2133, andQuocV.Le.2019. Xlnet:Generalized
AssociationforComputational autoregressivepretrainingforlanguage

### Linguistics. understanding. InAdvancesinNeural

Wu,ZhendongandHuiXiang.2023. Mfd: InformationProcessingSystems32:Annual
Multi-featuredetectionofllm-generated ConferenceonNeuralInformationProcessing
text. CoRR. Systems2019,NeurIPS2019,December8-14,
Yan,Duanli,MichaelFauss,JiangangHao, 2019,Vancouver,BC,Canada,pages
andWenjuCui.2023. Detectionof 5754–5764.
ai-generatedessaysinwritingassessment. Yao,Shunyu,DianYu,JeffreyZhao,Izhak
PsychologicalTestingandAssessment Shafran,ThomasLGriffiths,YuanCao,

### Modeling,65(2):125–144. andKarthikNarasimhan.2023. Treeof

Yan,Yuanmeng,RumeiLi,SiruiWang, thoughts:Deliberateproblemsolvingwith
FuzhengZhang,WeiWu,andWeiranXu. largelanguagemodels,may2023. ArXiv

## ConSERT:Acontrastiveframework preprint,abs/2305.10601.

forself-supervisedsentencerepresentation Yasunaga,MichihiroandPercyLiang.2021.
transfer. InProceedingsofthe59thAnnual Break-it-fix-it:Unsupervisedlearningfor
MeetingoftheAssociationforComputational programrepair. InProceedingsofthe38th
Linguisticsandthe11thInternationalJoint InternationalConferenceonMachine
ConferenceonNaturalLanguageProcessing Learning,ICML2021,18-24July2021,
(Volume1:LongPapers),pages5065–5075, VirtualEvent,volume139ofProceedingsof
AssociationforComputational MachineLearningResearch,pages
Linguistics. 11941–11952,PMLR.
Yanagi,Yuta,RyoheiOrihara,YuichiSei, Yoo,KiYoon,WonhyukAhn,JihoJang,and
YasuyukiTahara,andAkihikoOhsuga. NojunKwak.2023. Robustmulti-bit

## Fakenewsdetectionwithgenerated naturallanguagewatermarkingthrough

commentsfornewsarticles. In2020IEEE invariantfeatures. InProceedingsofthe61st
24thInternationalConferenceonIntelligent AnnualMeetingoftheAssociationfor
EngineeringSystems(INES),pages85–90, ComputationalLinguistics(Volume1:Long

### IEEE. Papers),ACL2023,Toronto,Canada,July

Yang,Lingyi,FengJiang,andHaizhouLi. 9-14,2023,pages2092–2115,Association

## Ischatgptinvolvedintexts? forComputationalLinguistics.

measurethepolishratiotodetect Yu,Peipeng,JiahanChen,XuanFeng,and
chatgpt-generatedtext. ArXivpreprint, ZhihuaXia.2023a. CHEAT:Alarge-scale
abs/2307.11380. datasetfordetectingchatgpt-written
Yang,Xi,KejiangChen,WeimingZhang, abstracts. CoRR,abs/2304.12008.
ChangLiu,YuangQi,JieZhang,Han Yu,Xiao,YuangQi,KejiangChen,Guoqiang

### Fang,andNenghaiYu.2023a. Chen,XiYang,PengyuanZhu,Weiming

Watermarkingtextgeneratedbyblack-box Zhang,andNenghaiYu.2023b. Gpt
languagemodels. CoRR,abs/2305.08883. paternitytest:Gptgeneratedtextdetection
withgptgeneticinheritance. ArXiv
63

<!-- Page 64 -->

preprint,abs/2305.12519. deepfakedetectionwithfactualstructure
Yuan,Ann,AndyCoenen,EmilyReif,and oftext. InProceedingsofthe2020Conference
DaphneIppolito.2022. Wordcraft:story onEmpiricalMethodsinNaturalLanguage
writingwithlargelanguagemodels. In Processing(EMNLP),pages2461–2470,
27thInternationalConferenceonIntelligent AssociationforComputational
UserInterfaces,pages841–852. Linguistics.
Zellers,Rowan,AriHoltzman,YonatanBisk, Zhu,Biru,LifanYuan,GanquCui,Yangyi
AliFarhadi,andYejinChoi.2019a. Chen,ChongFu,BingxiangHe,Yangdong
HellaSwag:Canamachinereallyfinish Deng,ZhiyuanLiu,MaosongSun,and
yoursentence? InProceedingsofthe57th MingGu.2023. Beatllmsattheirown
AnnualMeetingoftheAssociationfor game:Zero-shotllm-generatedtext
ComputationalLinguistics,pages4791–4800, detectionviaqueryingchatgpt. In
AssociationforComputational Proceedingsofthe2023Conferenceon

### Linguistics. EmpiricalMethodsinNaturalLanguage

Zellers,Rowan,AriHoltzman,Hannah Processing,EMNLP2023,Singapore,
Rashkin,YonatanBisk,AliFarhadi, December6-10,2023,pages7470–7483,
FranziskaRoesner,andYejinChoi.2019b. AssociationforComputational
Defendingagainstneuralfakenews. In Linguistics.
AdvancesinNeuralInformationProcessing
Systems32:AnnualConferenceonNeural
InformationProcessingSystems2019,

### NeurIPS2019,December8-14,2019,

Vancouver,BC,Canada,pages9051–9062.
Zeng,Zijie,LeleSha,YuhengLi,Kaixun

### Yang,DraganGaševic´,andGuanliang

Chen.2023. Towardsautomaticboundary
detectionforhuman-aihybridessayin
education. arXivpreprintarXiv:2307.12267.

### Zhang,Ruisi,ShehzeenSamarahHussain,

PaarthNeekhara,andFarinazKoushanfar.
2023a. REMARK-LLM:Arobustand
efficientwatermarkingframeworkfor
generativelargelanguagemodels. CoRR,
abs/2310.12362.
Zhang,Yue,YafuLi,LeyangCui,DengCai,
LemaoLiu,TingchenFu,XintingHuang,
EnboZhao,YuZhang,YulongChen,etal.
2023b. Siren’ssongintheaiocean:A
surveyonhallucinationinlargelanguage
models. ArXivpreprint,abs/2309.01219.

### Zhao,Zihao,EricWallace,ShiFeng,Dan

Klein,andSameerSingh.2021. Calibrate
beforeuse:Improvingfew-shot
performanceoflanguagemodels. In

### Proceedingsofthe38thInternational

ConferenceonMachineLearning,ICML2021,
18-24July2021,VirtualEvent,volume139
ofProceedingsofMachineLearningResearch,
pages12697–12706,PMLR.
Zheng,Qinkai,XiaoXia,XuZou,Yuxiao

### Dong,ShanWang,YufeiXue,ZihanWang,

LeiShen,AndiWang,YangLi,etal.2023.

### Codegeex:Apre-trainedmodelforcode

generationwithmultilingualevaluations
onhumaneval-x. ArXivpreprint,
abs/2303.17568.
Zhong,Wanjun,DuyuTang,ZenanXu,

### RuizeWang,NanDuan,MingZhou,

JiahaiWang,andJianYin.2020. Neural
64