---
title: "MMReview Peer Review Automation"
original_file: "./MMReview_Peer_Review_Automation.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["prompt-engineering", "llm", "rag", "chain-of-thought", "react"]
keywords: ["paper", "work", "review", "submission", "data", "model", "well", "does", "page", "strengths"]
summary: "<!-- Page 1 -->

MMReview: A Multidisciplinary and Multimodal Benchmark for

### LLM-Based Peer Review Automation

XianGao1,JiachengRuan1,ZongyunZhang1,JingshengGao1,TingLiu1,YuzhuoFu1,
1ShanghaiJiaoTongUniversity,
gaoxian@sjtu.edu.cn
Abstract LLMshavemadeautomatedpeerreviewincreasinglyviable,asthesemodelsshowstrongreason-
Withtherapidgrowthofacademicpublications, ingabilitiesandcanofferconstructivefeedbackon
peerreviewhasbecomeanessentialyettime- academicmanuscripts(LiuandShah,2023;Zhao
consumi"
related_documents: []
---

# MMReview Peer Review Automation

<!-- Page 1 -->

MMReview: A Multidisciplinary and Multimodal Benchmark for

### LLM-Based Peer Review Automation

XianGao1,JiachengRuan1,ZongyunZhang1,JingshengGao1,TingLiu1,YuzhuoFu1,
1ShanghaiJiaoTongUniversity,
gaoxian@sjtu.edu.cn
Abstract LLMshavemadeautomatedpeerreviewincreasinglyviable,asthesemodelsshowstrongreason-
Withtherapidgrowthofacademicpublications, ingabilitiesandcanofferconstructivefeedbackon
peerreviewhasbecomeanessentialyettime- academicmanuscripts(LiuandShah,2023;Zhao
consuming responsibility within the research
et al., 2024; Zhuang et al., 2025), partially allecommunity. LargeLanguageModels(LLMs)
viating reviewer burden. Yet, current evaluations
haveincreasinglybeenadoptedtoassistinthe
of LLM-generated reviews focus mainly on final
generationofreviewcomments;however,curoutputs,lackingin-depthanalysisofthereasoning
rent LLM-based review tasks lack a unified
evaluationbenchmarktorigorouslyassessthe processesbehindmodeljudgments. Additionally,
models’abilitytoproducecomprehensive,ac- most studies concentrate on AI papers with pubcurate,andhuman-alignedassessments,partic- liclyavailabletext,overlookingthemultimodalnaularlyinscenariosinvolvingmultimodalcon- tureofacademicpapers,suchasfiguresandtables,
tentsuchasfiguresandtables. Toaddressthis
andtheevaluationofLLMsinreviewingresearch
gap, we propose MMReview, a comprehenacrossbroaderscientificdomains.
sivebenchmarkthatspansmultipledisciplines

### To address the aforementioned challenges, we

and modalities. MMReview includes multiproposeMMReview,acomprehensivebenchmark
modalcontentandexpert-writtenreviewcomments for 240 papers across 17 research do- forpeerreviewgenerationthatspansmultipledismainswithinfourmajoracademicdisciplines: ciplinesandmodalities. MMReviewincorporates
Artificial Intelligence, Natural Sciences, En- three distinct types of input modalities: textual
gineeringSciences, andSocialSciences. We
content from manuscripts, figures and tables emdesignatotalof13tasksgroupedintofourcore
beddedwithinthepapers,andrenderedPDFpages
categories,aimedatevaluatingtheperformance
convertedintoimages. Thesedataspan17research
ofLLMsandMultimodalLLMs(MLLMs)in
domains across 4 disciplinary categories. To obstep-wisereviewgeneration, outcomeformulation,alignmentwithhumanpreferences,and tain high-quality peer review samples for evaluarobustness to adversarial input manipulation. tionpurposes,wedevelopedamulti-modelcollab-
Extensiveexperimentsconductedon18open- orative pipeline for data filtering and generation.
sourcemodelsand3advancedclosed-source Specifically, wefirstcuratedatotalof51,881pamodels demonstrate the thoroughness of the
perswithassociatedreviews;then,wefilteredthe
benchmark. WeenvisionMMReviewasacritcollectedseeddatasetDtoobtainhigh-qualitypaical step toward establishing a standardized
pers while maintaining a relatively balanced disfoundationforthedevelopmentofautomated
tribution;subsequently,weextractedreferenceanpeerreviewsystems.
swersfromhumanreviews. Finally,weconducted
1 Introduction manualverificationtocorrecterrors,resultingina
curatedsetof240samplesthatserveasthefoun-
Peerreviewisessentialtoscholarlypublishing,en- dationfortaskconstruction. Buildinguponthese
suring research quality and enhancing academic samples, we introduce 4 thematic categories enwriting. However, the growing volume of sub- compassing13diversetasks,eachdesignedtothormissions has strained the traditional review pro- oughlyassessthecapabilitiesofLLMsinstep-wise
cess,leadingtoinefficienciesandlimitedreviewer reviewgeneration,outcomeformulation,alignment
availability(Kimetal.,2025),whichrestrictsfeed- withhumanpreferences,androbustnesstoadverback and delays review outcomes. Advances in sarialinputmanipulation. Weconductcomprehen-
1
5202
tcO
8
]LC.sc[
4v64141.8052:viXra

<!-- Page 2 -->

siveexperimentson16open-sourcemodelsaswell prompting(D’Arcyetal.,2024)togeneratecomas5state-of-the-artclosed-sourcemodels,includ- prehensive feedback. Nonetheless, these efforts
ingGPT-4oandClaude-4-Sonnet,across13tasks. focussolelyontextualreviews,neglectingthevi-
Theresultshighlightthecomprehensivenatureof talroleofmultimodalcontent,suchasfiguresand
the MMReview benchmark and uncover several tables,andlackrigorousanalysisofthereasoning
keyfindings,offeringinsightsforfutureresearch processesbehindLLM-generatedcritiques.
onLLM-basedautomatedacademicpeerreview.
2.2 EvaluationforLLM-basedPeerReview

### Theprimarycontributionsofthispapercanbe

summarizedasfollows: Prior studies (Shen et al., 2022; Yu et al., 2024;

### Gao et al., 2024; Tan et al., 2024; Gao et al.,

• We introduce MMReview, the first compre- 2025) have predominantly evaluated the quality
hensiveevaluationbenchmarkforautomated ofLLM-generatedpeerreviewcommentsbymeaacademicpeerreviewusingLLMs,spanning suringtheircorrelationorsimilaritywithhumanmultiple disciplines and modalities. Built written reviews using automated metrics such
uponourdatafilteringandgenerationpipeline, as BLEU (Papineni et al., 2002), ROUGE (Lin,
MMReviewcomprises240high-qualitysam- 2004),BERTScore(Zhangetal.,2020),andME-
plesacross17academicfieldsin4disciplines. TEOR (Banerjee and Lavie, 2005). In addition,
severalstudies(Robertson,2023;Zhouetal.,2024;
• Wemeticulouslydesign13distincttasksen-

### Gaoetal.,2025)haveadoptedtheLLM-as-a-judge

compassingatotalof6,724thoughtfullycuparadigm,leveragingcutting-edgelanguagemodrated questions, enabling multi-dimensional
els to assess the quality of review comments proevaluation of model performance. These diduced by other LLMs. Given the absence of an
versetasksallowfortargetedassessmentand
establishedgoldstandardforthisevaluationtask,
facilitatetheidentificationofpotentiallimitarecent research (Xu et al., 2024) has introduced
tionsinLLM-generatedpeerreviewcontent.
theGenerativeEstimatorforMutualInformation
(GEM) to quantify the degree of semantic over-
• Weconductextensiveexperimentson18openlapbetweenLLM-generatedandhuman-authored
sourceand3closed-sourcemodelsusingthe
reviews. Nevertheless,existingevaluationmethod-

### MMReview benchmark, offering some key

ologies are not grounded in a unified benchmark
findingsofLLM-basedautomatedreviewing.
ortaskframework,andtheyfallshortofproviding
Ourfindingsofferin-depthanalysisandvalua comprehensive analysis of the underlying reaable guidance for the future development of
soningprocessesinvolvedinLLM-generatedpeer
LLM-assistedpeerreviewsystems.
review.
2 RelatedWorks
3 MMReviewBenchmark
2.1 LLMsforPaperReview
Inthissection,wefirstpresenttheoverallpipeline

### LLMs have shown strong potential in analyzing

fordatacollectionandconstructionoftheMMRecomplexscholarlytexts(LiuandShah,2023;Zhao
viewbenchmark,followedbyadetailedexposition
et al., 2024; Zhuang et al., 2025). Initial studofthetaskdesignmethodology.
iesindicatethatLLM-generatedreviewcomments
partially overlap with those of human reviewers, 3.1 OverallPipelineofMMReview
suggesting their potential contribution to peer re- Benchmark
view(Robertson,2023;Liangetal.,2023). How-

### AsillustratedinFigure1,theconstructionofMM-

ever, further research reveals that even advanced

### Reviewisdividedintothreestages: datacollection,

models like GPT-4o often fail to meet human exdataprocessing,andtaskconstruction.
pectationsinreviewquality(Zhouetal.,2024). To
improvealignmentwithpeerreviewstandards,re- 3.1.1 DataCollection
searchers have built datasets from public review Duringthedatacollectionphase,wegatheredacaplatformsandfine-tunedLLMs(Kangetal.,2018; demicpapersfrompubliclyaccessiblepeerreview
Yuanetal.,2021a;Shenetal.,2022;Dyckeetal., platforms or sources where reviewer comments
2023; Gao et al., 2024). Other methods involve were openly available. These papers not only
multi-turndialogue(Tanetal.,2024)ormulti-agent contain the full manuscript texts but also include
2

<!-- Page 3 -->

Data Collection Data Processing Task Construction
115
𝑫 Human 𝑫 𝒃 A R C E C J6 5 5 0 A R C E 6 C J 3 3 2 4 9 A R C E 3 C J 8 1 1 9 9 A R C E 2 C J 4 1 1 3 1
Data Filtering AI NS ES SS

### Filtering


### Review TaskGeneration

𝑫 Golden Answer Extraction
Small LLM 𝒃 Human
Verification

### Attack654

𝑫 Preference96

## 𝑸𝑨

Papers Reviews Decisions PDF Step782 Outcome768

### Parsing Screen

Domain Classification Shot
Human Verification
Human Verification
34538 MMReview
𝑫 13398 2880 1065 Text Figures Tables Benchmark

## Ai Ns Es Ss

Figure1: TheconstructionpipelineofMMReview. Theconstructionpipelineisdividedintothreestages: data
collection,dataprocessing,andtaskconstruction.
reviewer-writtenevaluationsandfinaldecisions(ac- Discipline ResearchField #Samples ACC:REJ
ceptorreject). Specifically, wecuratedatotalof MachineLearning 17 8:9

### ComputerVision 20 12:8

51,881 papers with associated reviews submitted
NaturalLanguageProcessing 16 7:9

### Artificial

between 2013 and 2024 to venues such as ICLR ReinforcementLearning 11 3:8

### Intelligence


### GraphNeuralNetworks 19 8:11

andNeurIPS(fromtheOpenReviewplatformand

### SignalProcessing 17 8:9

NeurIPSProceedings,aswellasarticlesfromthe AIApplication 15 4:11
journal Nature Communications . For each col- Biology&Medicine 11 5:6

### Physics 16 7:9

lectedpaper,weemployedDeepseek-V3andGPT- Natural Chemistry 13 5:8

### Sciences

4o to automatically infer its academic discipline Environmental&EarthSciences 10 7:3

### Mathematics&Statistics 13 5:8

andresearchdomain. Incaseswherethetwomod-

### MaterialsScience 14 6:8

els produced inconsistent classifications, human Engineering ControlScience 12 5:7
verificationwasperformed. Ultimately,allpapers Sciences ElectronicInformation 6 4:2

### EnergyScience 6 4:2

werecategorizedintofouroverarchingdisciplines:

### Social


### Society,Economics&Finance 24 11:13

ArtificialIntelligence,NaturalSciences,Engineer- Sciences
ing Sciences, and Social Sciences, resulting in a
Table 1: The distribution of papers across various reseeddatasetdenotedasD. Figure1illustratesthe
searchdomains.
distribution of papers across the four disciplines
withinD.
3.1.2 DataProcessing
et al., 2025) to generate summaries of each pa-
Duringthedataprocessingstage,wefirstfiltered perundertwodistinctinputconditions: oneusing
thecollectedseeddatasetD toobtainhigh-quality only the abstract and the other using the full text
samples while maintaining a relatively balanced ofthemanuscript. Agreaterdivergencebetween
distributionacrossdisciplinesandensuringacom- thetwogeneratedsummariesisinterpretedaseviparable number of accepted and rejected papers. dencethatthefulltextprovidessubstantiallymore
Toachievethis,wedesignedadual-pathjointdata information,thusindicatinghighersamplequality.
selectionmechanismthatsimultaneouslyfiltersfor Sampleswithasignificantinformationgainfrom
samplequalityandenforcesdistributionalbalance. thefulltextwereretainedinourtestbenchmark. To
Specifically, we utilized Qwen3-32B1 (Yang furtherensurethatthebenchmarkmaintainsabalanceddistributionacrossacademicdisciplinesand
1Qwen3-32Branksamongthetop10ontheOpenCom- anapproximatelyequalratioofacceptedtorejected
passleaderboard,offeringafavorabletrade-offbetweenperpapers,wesupplementedthebenchmarkbymanuformanceandmodelsize,makingitefficientforlarge-scale
samplefiltering allyincorporatingtop-rankedpapersfromspecific
3

<!-- Page 4 -->

domainsinD basedonthequalityrankings. This The Summary task evaluates a model’s ability to
human-filteringprocedureguaranteesthatthecom- distillkeyinformationfromafullmanuscriptinto
positionofthebenchmarkdatasetalignswithour an accurate, concise summary. In this task, the
desireddistributionalproperties. modelispromptedtogenerateabriefsummaryin
During the data filtering phase, we obtained a itsownwords,avoidingabstractcopyingandsubtotal of 240 paper samples spanning 17 research jectivejudgment. Themodel-generatedsummary
domainsacross4majordisciplinestoconstructour isthencomparedtohuman-reviewer-writtensumevaluationbenchmark,denotedasD . Thestatisti- maries and evaluated for semantic similarity and
b
caldetailsofD ,includingthenumberofsamples informationcoverage,measuringthemodel’sholisb
per domain and the distribution of accepted ver- ticcomprehensionandrepresentationofacademic
susrejectedpapers,arepresentedinTable1. For content.
each discipline, we ensured a relatively balanced
number of samples across research fields while Strengths Evaluation (SE) and Weaknesses
approachingtheactualacceptance/rejectionratio Evaluation(WE) Summarizingandanalyzinga
throughacombinationofmodel-basedfilteringand manuscript’sstrengthsandweaknessesisacoreasmanual curation. For each of these 240 samples, pectofpeerreview. TheStrengthsEvaluationand
we utilized PDF parsing tools to extract textual WeaknessesEvaluationtasksassessLLMs’ability
content, figures, and tables from the manuscript toidentifyandarticulatethemeritsandlimitations
files,andconvertedeachpageofthePDFintocor- ofacademicpapers. Thesetaskstestwhethermodresponding images. As a result, we constructed elscansynthesizetechnicalhighlightsandmethodthree distinct modalities of input data: text-only, ological concerns noted by human reviewers, fomultimodal (text combined with extracted visual cusing on four dimensions: Quality, Clarity, Sigelements),andPDF-as-image. nificance,andOriginality. IntheStrengthsEvaluationtask,modelsargueforacceptancebydetail-
3.1.3 TaskConstruction
ingmethodologicalrigor,experimentalrobustness,
During task construction, we developed 13 tasks structuralclarity,researchimpact,andnovelty,thus
groupedintofourthematiccategories,step-based, evaluating their capacity to extract technical conoutcome-based, preference-based, and attack- tributions and assess scientific merit. In contrast,
based, reflecting the peer review workflow and theWeaknessesEvaluationtaskadoptsarejectionchallenges LLMs may face. Task distribution is orientedstance,testingcriticalreasoningandconshowninFigure1. Promptsweredesignedbased structive critique. Model outputs are compared
onreviewerguidelinesfrommajoracademiccon- withhumanreviewsbasedoncontentcoverageand
ferences. For each task, we used regular expres- semanticsimilarity.
sionsorGPT-4otoextractreferenceanswersfrom
humanreviewsinD ,formingthequestion–answer SoundnessScoring(SS)andPresentationScorb
datasetD . FortheFakeStrengthEvaluationand ing (PS) The Soundness Scoring and Presenta-

## Qa

FakeWeaknessEvaluationtasks,GPT-4oandcus- tionScoringtasksevaluateLLMs’abilitytoquantompromptsgeneratedantonymicrewrites,which titatively assess manuscript quality, focusing on
weremanuallyverifiedforsemanticaccuracy. This technical soundness and writing presentation. In
processfinalizedtheMMReviewbenchmark. The SoundnessScoring,themodelratesthereliability
detailedpromptsfortaskgenerationandeachtask oftechnicalclaims,experimentalrigor,andevidencanbefoundinAppendixD. tial support, emphasizing empirical and methodological validity. Presentation Scoring assesses
3.2 Step-basedTasks
linguisticclarityandlogicalorganization,reflect-
The Step-based theme comprises five tasks de- ingwritingqualityandinformationstructure. Both
signedtoprogressivelyevaluatetheperformance tasksrequireintegerscoresfrom1to4,denoting
ofLLMsinsimulatingthekeycomponentsofthe “poor"to“excellent."Modelscoresarecompared
academicpeerreviewprocess. tohumanratingstoassessjudgmentconsistency.
Summary (S) Summarizing a paper is the ini-
3.3 Outcome-basedTasks
tialstepinpeerreviewandakeytestofamodel’s
abilitytoextractessentialcontent. Inaccuratesum- The Outcome-based tasks focus on assessing a
mariesmayimpairsubsequentreviewgeneration. model’s direct capability to generate peer review
4

<!-- Page 5 -->

outcomes,withthegoalofevaluatingitsalignment reviewsratherthanmerelyaveragingscores. This
withhumanreviewersinfinaldecision-making. taskmirrorstherealroleofanACandrigorously
evaluates the model’s capacity for synthesis and
ConditionalDecision(CD) TheConditionalDedecisionrationality. Modeloutputsarecompared
cision task assesses LLMs’ ability to synthesize
tohuman-writtenmeta-reviewstoassessreliability
human-written reviews and generate an overall
andscientificjudgmentinhigh-levelpeerreview.
qualityscoreforapaper. Providedwithreviewer
comments detailing strengths, weaknesses, and 3.4 Preference-basedTask
evaluationsofmethodologyandresults,themodel

### PairwiseRank(PR) Priorworkhasshownthat

assigns a numerical score from 1 to 10, reflectpairwisecomparisoneffectivelyevaluatesthealigningascalefrom“fundamentallyflawedorlacking
mentbetweenLLM-generatedpreferencesandhunovelty”to“groundbreakingcontribution,”aligned
manjudgments(Liuetal.,2024b). Sinceacademic
withacademicconferencestandards. Thetaskevalconferenceacceptancetiers,oral,spotlight,poster,
uates the model’s capacity to interpret sentiment,
reject,reflecthumanpreferencerankings,thePairweighting,andevaluativereasoninginthereviews
wiseRanktaskisdesignedtotestwhetherLLMs,
andtranslatethemintoacoherentquantitativejudgas reviewers, display preference patterns consisment. Model scores are compared with human
tent with human evaluators. This task assesses
ratingstoassessalignmentandaccuracyinreviewthemodel’srelativejudgmentabilitybypresenting
baseddecision-making.
pairsofpapersfromdifferentacceptancetiers: oral
DirectDecision(DD)andCoTDecision(CoD) (top 5%), spotlight (top 25%), poster, and reject.
TheDirectDecisionandCoT(Chain-of-Thought) Themodelcomparesandranksthepapers,simulat-
Decision tasks evaluate LLMs’ ability to au- ingreal-worldpeerreviewselection. Alignmentis
tonomouslyassessacademicpaperquality,reflect- measuredbycomparingmodelpreferenceswithacing two reviewing paradigms: streamlined judg- tualacceptancecategoriestodeterminerankingacmentandstep-by-stepreasoning(Weietal.,2022). curacy. Toreducepositionalbias(Shietal.,2025;
Thesetasksvaryininputformatandcognitivecom- Thakuretal.,2025),eachcomparisonisrepeated
plexity,enablingcontrolledcomparisonofmodel withreversedinputorder.
performance under different reasoning demands.
3.5 Attack-basedTasks

### In the Direct Decision task, the model produces

anoverallscorewithoutguidance,simulatingare- Thistaskcategoryassessesmodels’robustnessand
viewer’sholisticjudgmentfromasingleread. In discriminativeabilityinpeerreviewbyintroducing
contrast,theCoTDecisiontaskguidesthemodel adversarial inputs. Fabricated strengths or weakthroughastructuredreasoningprocess: summariz- nesses,suchasinvertedprosandcons,areusedto
ingthepaper,analyzingstrengthsandweaknesses testthemodel’scapacitytodetectfactualinaccuacrossQuality,Clarity,Significance,andOriginal- racies. Misleading prompts further aim to divert
ity,assigningSoundnessandPresentationscores, the model from its original instructions. Model
and synthesizing an overall score. This mirrors outputsarecomparedtohumanjudgmentsorthe
a reviewer’s iterative, analytical evaluation. The model’sownnon-adversarialresponses,focusing
taskstestreasoningabilityandscoringtraceability. onitsabilitytopreserveevaluativeindependence
Model outputs are compared to human scores to andlogicalconsistencyunderinputperturbations.
assessconsistencyandrationality.

### FakeStrengths(FS)andFakeWeaknesses(FW)

MetaDecision(MD) Beyondgeneratingindivid- LLMs have been widely observed to exhibit a
ual reviews and scores, a key aspect of academic "sycophantic"tendencyandapropensitytoalign
peerreviewistheAreaChair’s(AC)synthesisof withhumanjudgments(Liuetal.,2024a;Kumaran
reviewer feedback to make a final decision. To etal.,2025),whichmaycompromisetheirability
emulatethis, theMetaDecisiontaskrequiresthe toidentifyflawsandgeneratecriticalpeerreview
modeltoissueabinaryjudgment,AcceptorReject, comments. Additionally, the hallucination issue
basedonmultiplehumanreviews. Thepromptpro- inherent in LLMs may lead to erroneous assessvides structured guidance and evaluation criteria, ments of a paper’s strengths and weaknesses. To
prompting step-by-step reasoning. The model is investigatethesechallenges,weproposetheFake
instructedtoassessthequalityandconsistencyof StrengthandFakeWeaknesstasks,designedtoeval-
5

<!-- Page 6 -->

uatethemodel’sabilitytocorrectlyidentifycontent Theme Task #Ques. Metric
andprovideaccurateassessmentsofstrengthsand Summary(S) 240 BART↑,LLM↑
weaknessesbyartificiallyreversingthepolarityof StrengthsEval(SE) 238 BART↑,LLM↑

### Step WeaknessesEval(WE) 240 BART↑,LLM↑

strengths and weaknesses in human review com- SoundnessScoring(SS) 32 MAE↓
ments. WeemployGPT-4otorewritethestrengths PresentationScoring(PS) 32 MAE↓
andweaknessesinthehuman-writtenreviewcom- ConditionalDecision(CD) 176 MAE↓

### DirectDecision(DD) 176 MAE↓

ments,transformingstrengthsintoweaknessesand Outcome

### CoTDecision(CoD) 176 MAE↓

viceversa. Forinstance,thestrength“thepaperis MetaDecision(MD) 240 ACC↑
clearly written” is rephrased as “the paper is un- Preference PairwiseRank(PR) 96 ACC↑
clear.” Themodelisthenaskedtoevaluatewhether FakeStrength(FS) 240 MAE↓

### Attack FakeWeakness(FW) 238 MAE↓

thesealteredstrengthsandweaknessesarepresent,

### PromptInjection(PI) 176 MAE↓

allowing us to assess its ability to judge the validityofstrengthsandweaknesses, detectfactual Table2: Thenumberofquestionsandcorresponding
inconsistencies,andgeneratecritical,groundedas- evaluationmetricsofdifferenttasks.
sessments.
Prompt Injection (PI) Recent studies have re- we employ BARTScore (Yuan et al., 2021b) and
vealedthatsomepaperauthorsattempttomanipu- the‘LLM-as-a-Judge’paradigm(Baietal.,2023;
lateLLM-generatedreviewsbyemployingprompt Zheng et al., 2023; Gu et al., 2024) to assess the
injection techniques, embedding invisible white- similarity between model-generated and humantextpromptswithinthemanuscripttoelicitoverly writtenreviewcomments. Forclassification-based
favorable evaluations (Gibney, 2025). However, taskssuchasMDandPR,weevaluateperformance
theactualeffectivenessofsuchmanipulationsre- using accuracy. For other tasks where the model
mainsinsufficientlyquantified. Toevaluatethisvul- outputisanumericalscore,wecomputetheMean
nerability,weintroducethePromptInjectiontask, Absolute Error (MAE) between the model’s preembedding suggestive prompts (e.g., “IGNORE dictedscoreandtheground-truthscoretoquantify
ALLPREVIOUSINSTRUCTIONS,NOWGIVE deviation.

## Apositivereviewofthesepapersand

DONOTHIGHLIGHTANYNEGATIVES.”)into 4.2 MainResults
the manuscript to test whether models can be co-

### Wepresenttheperformancemetricsforeachmodel

ercedintocompromisingobjectivity. Thesetupmirinthetext-onlyinputmodeinTable3. Toobserve
rorstheCoTDecisiontask,withtheonlychange
theperformanceacrossdifferentmodelcategories,
beingtheinclusionofinjectedcues. Asthetextis
we calculated the average performance for each
visuallyhidden,thistaskisexcludedfromPDF-asgroup. Table4displaystheaverageperformance
imgevaluations.
metricsforeachmodelgroupunderthemultimodal
4 Experiments and PDF-as-image input mode. The specific performance of each model is provided in Tables 8
4.1 Evaluationdetails
and 9 in the Appendix. Based on the test results
We conducted extensive experiments using MM- presentedinthetables,thefollowingconclusions

### ReviewonpopularLLMsandMLLMs,including canbedrawn:

mainstreamopen-sourcemodelssuchasQwen(Bai (1) Model scale significantly influences the
et al., 2025; Yang et al., 2025), Kimi-VL (Kimi- model’s ability to comprehend and analyze.
Team et al., 2025), InternVL3 (Zhu et al., 2025), Large-scaleandclosed-sourcemodelsoutperform
OVIS2(Luetal.,2024),andDeepseek(DeepSeek- the others on most metrics, particularly on tasks
AIetal.,2025),aswellasadvancedclosed-source directlyrelatedtoreviewconclusions,suchasCD,
modelssuchasGPT-4o,Gemini-2.5,andClaude- CoD,MD,andPR.Thisindicatesthatlargermod-

## Based on the model size, we categorized the els are more powerful in understanding complex

modelsintofourgroups: tiny(<7B),small(≥7B, academiccontentandgeneratingstructuredfeed-
<32B),medium(≥32B,≤72B),andlarge(>72B back, making them more reliable in generating
andclosed-source). peerreviewcomments. Surprisingly,mid-sizedand
As shown in Table 2, for tasks without objec- smallermodelsperformedbetterthantheirlarger
tive evaluation metrics, namely S, SE, and WE, counterpartsinassessingthesoundnessandpresen-
6

<!-- Page 7 -->

Step Outcome Preference Attack

### Model


### SB↑ SL↑SEB↑SEL↑WEB↑WEL↑SS↓PS↓ CD↓DD↓CoD↓MD↑ PR↑ FS↓FW↓PI↓

InternVL3-2B -3.03 3.64 -3.66 3.56 -3.95 2.15 0.47 0.47 2.35 3.43 3.29 66.25 53.13 3.14 1.37 1.11
Qwen2.5-VL-3B -3.23 3.58 -3.89 3.36 -4.00 1.67 0.00 0.00 1.46 4.37 4.46 64.91 73.96 3.46 2.95 0.05
Tiny Kimi-VL-A3B-I -3.01 3.65 -3.67 3.46 -3.96 1.98 0.47 0.44 2.31 3.13 3.83 60.92 56.25 2.99 0.56 0.87
Kimi-VL-A3B-T -3.15 3.71 -3.68 3.79 -3.91 2.52 0.47 0.44 2.16 3.59 3.37 66.67 57.29 3.31 0.96 0.63
Avg. -3.10 3.65 -3.72 3.54 -3.95 2.08 0.35 0.34 2.07 3.63 3.74 64.69 60.16 3.22 1.46 0.67
Qwen2.5-VL-7B -3.05 3.61 -3.68 3.57 -3.96 2.06 0.47 0.44 2.43 3.59 3.57 72.92 59.38 2.99 1.66 0.19
Qwen3-8B -3.08 3.84 -3.63 3.77 -3.87 2.93 0.53 0.44 2.25 3.70 3.16 77.50 65.63 3.26 2.03 1.41
Deepseek-R1-8B -3.09 3.76 -3.63 3.79 -3.86 2.72 0.63 0.78 1.75 3.84 3.55 76.99 64.74 3.25 1.99 0.59
InternVL3-8B -2.99 3.76 -3.65 3.74 -3.93 2.27 0.47 0.44 2.85 3.35 3.35 76.67 52.08 2.99 1.35 0.53
Small OVIS2-8B -3.09 3.52 -3.70 3.45 -3.99 1.98 0.47 0.44 2.28 3.41 3.72 63.87 60.42 2.99 2.41 0.63
GLM-4.1V-9B-T -3.15 3.60 -3.68 3.73 -3.93 2.60 0.50 0.44 2.08 3.53 3.33 71.86 59.77 3.00 1.08 0.35
Qwen3-14B -3.06 3.85 -3.64 3.83 -3.87 2.79 0.53 0.50 2.16 3.77 3.64 80.42 61.46 3.02 1.99 0.71
OVIS2-16B -3.04 3.59 -3.70 3.52 -3.99 2.06 0.47 0.44 1.87 3.33 3.73 79.92 64.58 3.00 2.34 0.12
Avg. -3.07 3.69 -3.66 3.68 -3.93 2.43 0.51 0.49 2.21 3.56 3.51 75.02 61.01 3.06 1.86 0.57
Qwen2.5-VL-32B -2.97 3.90 -3.60 3.75 -3.87 2.58 0.56 0.50 2.00 3.15 3.67 67.08 67.71 2.99 1.92 0.80
Qwen3-32B -3.05 3.90 -3.61 3.81 -3.85 2.91 0.50 0.56 2.14 3.60 3.49 80.00 68.75 3.05 1.83 0.78
Middle OVIS2-34B -3.04 3.48 -3.68 3.50 -3.97 2.24 0.81 0.81 2.14 3.72 3.76 79.92 62.50 2.99 1.81 0.57
Qwen2.5-VL-72B -2.99 3.74 -3.65 3.58 -3.94 2.29 0.47 0.47 2.06 3.64 3.71 0.69 0.64 0.00 0.00 0.84
Avg. -3.01 3.76 -3.64 3.66 -3.91 2.51 0.59 0.59 2.09 3.53 3.66 56.92 49.90 2.26 1.39 0.75
Deepseek-V3 -3.04 3.84 -3.61 3.89 -3.85 2.96 0.53 0.47 2.62 3.37 3.70 75.00 66.03 2.99 0.66 0.20
Deepseek-R1 -3.04 3.92 -3.69 3.90 -3.91 3.05 0.66 0.81 1.97 3.71 3.59 82.92 66.03 3.18 1.20 0.44
Chatgpt-4o-latest -3.06 3.91 -3.61 3.89 -3.86 2.87 0.84 0.94 1.65 3.70 3.65 80.33 63.54 3.92 1.45 0.45

### Large

Claude-sonnet-4 -3.02 3.88 -3.58 3.84 -3.84 3.05 0.53 0.41 1.17 2.02 2.01 84.58 72.92 2.98 2.34 0.43
Gemini-2.5-flash -3.06 3.80 -3.58 3.89 -3.86 2.61 0.94 0.88 1.24 4.60 4.28 74.06 70.83 3.73 1.37 0.59
Avg. -3.04 3.87 -3.61 3.88 -3.87 2.91 0.70 0.70 1.73 3.48 3.45 79.38 67.87 3.36 1.41 0.42
Table3: ResultsonMMReviewwithtext-onlyinputs,whereTdenotesThinkingandIdenotesInstruct.
Model Step Outcome Preference Attack

### Size

S ↑ S ↑ SE ↑ SE ↑ WE ↑ WE ↑ SS↓ PS↓ CD↓ DD↓ CoD↓ MD↑ PR↑ FS↓ FW↓ PI↓

## B L B L B L


### Multimodal

Tiny -3.12 3.59 -3.76 3.37 -3.97 2.00 0.48 0.46 2.14 3.24 3.56 59.66 56.77 2.95 1.11 0.42
Small -3.16 3.50 -3.72 3.49 -3.99 2.13 0.48 0.46 2.41 3.64 3.82 69.72 61.98 3.00 1.77 0.31
Middle -3.05 3.71 -3.67 3.63 -3.94 2.35 0.72 0.69 2.21 3.66 3.86 73.20 61.21 3.00 1.55 0.47
Large -3.07 3.82 -3.59 3.86 -3.86 2.78 0.76 0.75 1.59 3.48 3.34 78.79 65.97 3.25 1.37 0.40

### PDF-as-img

Tiny -3.25 3.27 -4.00 2.98 -4.11 1.83 0.47 0.73 1.86 2.93 3.59 67.47 54.95 2.35 1.08 \
Small -3.55 2.89 -3.88 3.20 -4.08 1.99 0.47 0.44 2.14 3.38 3.47 72.78 59.17 2.99 1.72 \
Middle -3.14 3.55 -3.70 3.54 -3.95 2.29 0.68 0.70 2.06 3.65 3.76 71.77 55.90 3.09 1.34 \
Large -3.28 3.50 -3.67 3.72 -3.90 2.68 0.77 0.75 1.39 3.53 3.36 77.99 63.89 2.85 1.60 \
Table4: ResultsonMMReviewwithmultimodalandpdf-as-imageinputs. Thedetailedresultsfrommodelscanbe
foundinTable8and9inAppendixA.
tationofpapers. (such as Kimi-VL-A3B-Thinking and Deepseek-

### R1) outperformed non-thinking models on tasks

(2) High-quality structured reasoning en- directlyrelatedtoscoring,suchasCD,CoD,MD,
hances review outcomes. Compared to directly andPR,suggestingthatstrongerthinkingandreageneratingreviewscores(DD),theuseofCoTrea- soning abilities enhance the model’s peer review
soningtogeneratereviewscores(CoD)achieved capabilities.
a lower MAE, demonstrating that a step-by-step
review approach strengthens the model’s evalua- (3) Multimodal input improves the model’s
tivecapability. Furthermore,usingahigher-quality, robustness to prompt injection. Regardless of
human-writtenreviewprocessasareference(CD) modelsize, when bothtext and paperimages are
furtherreducedtheMAE,indicatingthatthequal- inputsimultaneously,theinfluenceofpromptinjecityofthereasoningprocessalsoaffectsthemodel’s tionislowercomparedtothetext-onlyinputmode,
evaluativeability. Modelsthatemployedthinking implyingthattheinclusionofimagemodalityen-
7

<!-- Page 8 -->


### AI NS ES SS %Raise E(Raise) %Lower E(Lower)

ChatGPT-4o-latest 4.46 5.67 3.67 4.28 Qwen3-8B 90.34 1.56 0.57 -1.00
claude-sonnet-4-20250514 2.08 2.33 1.33 2.44 Qwen3-8B-nothink 98.30 1.50 0.00 0.00
gemini-2.5-flash-thinking 4.62 6.33 4.33 4.50 Kimi-VL-A3B-I 31.15 1.28 6.56 -0.50
Deepseek-R1 2.32 4.00 3.67 4.00 Qwen3-32B 61.93 1.21 3.41 -1.00
Chatgpt-4o-latest 36.47 1.17 1.18 -1.00

### Claude-sonnet-4 11.93 1.14 25.57 -1.13

Table5: TheMAEperformanceofseveralmodelson

### Kimi-VL-A3B-T 46.02 1.10 11.93 -1.00

theCoDtaskacrossdifferentresearchdomains.

### Qwen3-14B 63.64 1.10 1.14 -1.00

Qwen2.5-VL-72B 78.41 1.07 0.00 0.00

### Deepseek-V3 16.48 1.07 2.84 -1.00

hances the model’s ability to judge paper quality OVIS2-8B 51.81 1.06 1.20 -1.00

### Qwen3-14B-nothink 80.68 1.05 0.00 0.00

andmitigatestheimpactofpromptinjectioninter-

### Deepseek-R1 15.91 1.04 22.73 -1.20

ference. Qwen2.5-VL-32B 77.71 1.03 0.00 0.00
Qwen3-32B-nothink 55.68 1.00 0.00 0.00
Qwen2.5-VL-7B 18.75 1.00 0.00 0.00
5 FurtherAnalysis

## Ovis2-34B 56.00 1.00 0.00 0.00


## Ovis2-16B 11.93 1.00 0.00 0.00

What Domains are LLM-reviewers better at?

### InternVL3-8B 52.84 1.00 0.00 0.00

Table 5 reports the MAE performance of various GLM-4.1V-9B-T 25.48 1.00 6.37 -1.10
modelsontheCoDtaskacrossresearchdomains,
Table 6: The proportion and expectation of score inindicatingtheirrelativeproficiencyinfield-specific
creasesanddecreasesundertext-onlyinputcondition.
peer review. All models use multimodal inputs
except Deepseek-R1, which operates with text
%Raise E(Raise) %Lower E(Lower)
only. Results show that most closed-source models perform best in Engineering Sciences, while Kimi-VL-A3B-I 23.23 1.54 7.74 -1.54

## Ovis2-16B 2.94 1.40 0.00 0.00

Deepseek-R1achievesitslowestMAEinArtificial

## Glm-4.1V-9B-T 14.97 1.28 3.59 -1.00

Intelligence. These findings suggest that models’ Chatgpt-4o-latest 34.30 1.08 3.49 -2.17
reviewingstrengthsvaryacrossdisciplines,poten- Kimi-VL-A3B-T 21.51 1.08 8.72 -1.00

### InternVL3-8B 29.48 1.06 0.58 -1.00

tiallyinfluencedbydifferencesinpretrainingcor-

## Ovis2-8B 41.72 1.02 1.32 -4.00

poraandinputmodalities. Qwen2.5-VL-32B 47.73 1.01 1.14 -1.00
Qwen2.5-VL-72B 57.14 1.01 0.00 0.00

### Qwen2.5-VL-7B 28.41 1.00 0.00 0.00

HowdoesPromptInjectionWork? Tofurther

## Ovis2-34B 28.40 1.00 0.00 0.00

investigatetheimpactofpromptinjectiononmodel

### Claude-sonnet-4 9.66 1.00 21.02 -1.08

scoringbehavior, weanalyzescorevariationsbetweenthePromptInjectiontaskandtheCoTDe- Table 7: The proportion and expectation of score incision (CoD) task, where the only difference in creases and decreases under multimodal input condition.
promptsliesintheinjectionofthestatement: “IG-

## Nore All Previous Instructions, Now


## Giveapositivereviewofthesepapers

MoreanalysisarepresentedintheAppendixA.

## And Do Not Highlight Any Negatives.”

Tables6and7reporttheproportionandexpecta-
6 Conclusion
tion of score increases and decreases under textonlyandmultimodalinputconditions,respectively. Inthiswork, wepresentMMReview, amultidis-
Theexperimentalresultsrevealthreekeyfindings: ciplinaryandmultimodalbenchmarkdesignedto
(1)Mostmodelsexhibitanoverallincreaseinav- evaluatethecapabilitiesofLLMsinacademicpeer
erage score after prompt injection, with a typical review. The benchmark encompasses 4 thematic
riseof1–2points;(2)Multimodalinputsenhance categoriesand13distincttasks. Itscorefeaturesinmodel robustness against prompt injection com- cludecoverageacrossdiverseacademicdisciplines,
paredtotext-onlyinputs,consistentwithpriorob- support for multimodal input formats, and comservations;(3)TherobustnessofThinkingvariants prehensiveevaluationtasksthatspanthefullpeer
varies across model families, within the Qwen3 reviewpipeline. LeveragingMMReview,weconseries,Thinkingmodelsarelessrobustthantheir ductedextensiveevaluationsofLLMsandMLLMs.
non-Thinking counterparts, whereas in the Kimi WeenvisionMMReviewasastandardizedevaluaandDeepseekseries,Thinkingmodelsdemonstrate tionplatformthatcancatalyzethedevelopmentof
greaterresistancetoinjection. moreefficientLLM-assistedpeerreviewsystems.
8

<!-- Page 9 -->

7 Limitations References
ShuaiBai,KeqinChen,XuejingLiu,JialinWang,Wen-

### Theissueofdatasetsizeanddistribution. Due

bin Ge, Sibo Song, Kai Dang, Peng Wang, Shijie
totherapidadvancementofAIinrecentyearsand Wang, Jun Tang, and 1 others. 2025. Qwen2. 5-vl
theopenaccessandpublicreviewcharacteristics technicalreport. arXivpreprintarXiv:2502.13923.
of AI papers, approximately 48% of the papers
Yushi Bai, Jiahao Ying, Yixin Cao, Xin Lv, Yuze
containingpeerreviewcommentsareconcentrated

### He,XiaozhiWang,JifanYu,KaishengZeng,Yijia

intheAIfield. Thisconcentrationmayaffectthe Xiao,HaozheLyu,JiayinZhang,JuanziLi,andLei
representativenessoftheresults. Inthefuture,we Hou.2023. BenchmarkingFoundationModelswith
Language-Model-as-an-Examiner. InThirty-Seventh
plantocollectmorepapersfromotherdomainsto
ConferenceonNeuralInformationProcessingSysenhancetherepresentativenessofourbenchmark.
temsDatasetsandBenchmarksTrack.
Thecontroversysurroundingreviewcomments SatanjeevBanerjeeandAlonLavie.2005. METEOR:
An Automatic Metric for MT Evaluation with Imwritten by human experts. There is currently
provedCorrelationwithHumanJudgments. InProalackofconsensusonwhatconstitutesagoodor ceedingsoftheACLWorkshoponIntrinsicandExhigh-quality review. Although methods such as trinsic Evaluation Measures for Machine Translaobtainingreviewconsensusandmanualscreening tionand/orSummarization,pages65–72,AnnArbor,
Michigan. Association for Computational Linguishave been employed in the paper to filter review
tics.
samples, it remains impossible to guarantee that
theseexpert-writtenreviewsareofsufficientqual- Mike D’Arcy, Tom Hope, Larry Birnbaum, and
Doug Downey. 2024. MARG: Multi-Agent Reity. Moreover, it is undeniable that all types of
view Generation for Scientific Papers. Preprint,
reviews hold value, even though they may vary
arXiv:2401.04259.
significantlyincontent,astheyreflectthediverse
perspectivesofdifferentreviewers. DeepSeek-AI,DayaGuo,DejianYang,HaoweiZhang,

### JunxiaoSong,RuoyuZhang,RunxinXu,QihaoZhu,


### ShirongMa,and1others.2025. DeepSeek-R1: In-

8 EthicalConsiderations centivizingReasoningCapabilityinLLMsviaReinforcementLearning. Preprint,arXiv:2501.12948.

### Allthepapersandpeerreviewcommentswecol-

NilsDycke,IliaKuznetsov,andIrynaGurevych.2023.
lectedaresourcedfromopen-accessplatformssuch

### NLPeer: AUnifiedResourcefortheComputational

asOpenReview,NeurIPS,andNature. Theseplat- StudyofPeerReview. InProceedingsofthe61stAnformsstatethatthecontenttheypublish,including nualMeetingoftheAssociationforComputational
butnotlimitedtothepapersthemselvesandtheir Linguistics (Volume 1: Long Papers), pages 5049–
5073, Toronto, Canada. Association for Computapeerreviewcomments,islicensedorpermittedfor
tionalLinguistics.
research purposes under the Creative Commons
Attribution International 4.0 license. We ensure XianGao,JiachengRuan,JingshengGao,TingLiu,and
YuzhuoFu.2025. ReviewAgents: BridgingtheGap
thatthecollectionandprocessingofthesepapers
BetweenHumanandAI-GeneratedPaperReviews.
and reviews are conducted for research purposes
Preprint,arXiv:2503.08506.
andcomplywiththecopyrightagreementsofthe
platforms. ZhaolinGao,KiantéBrantley,andThorstenJoachims.

## Reviewer2: Optimizing Review Gen-

Our research on the ability of LLMs to genereration Through Prompt Generation. Preprint,
ate peer review comments does not advocate for arXiv:2402.10886.
thecompletereplacementofhumanreviewerswith
ElizabethGibney.2025. Scientistshidemessagesinpa-
LLMs, as this might open the door to potential
perstogameAIpeerreview. Nature,643(8073):887–
misuse and manipulation. Instead, we envision 888.
that in the current era of a proliferation of aca-
Jiawei Gu, Xuhui Jiang, Zhichao Shi, Hexiang Tan,
demicpapers,LLMscanserveasanauxiliarytool.

### Xuehao Zhai, Chengjin Xu, Wei Li, Yinghan

Similar to the practices already adopted by aca-
Shen, Shengjie Ma, Honghao Liu, and 1 others.
demicconferenceslikeICLRandAAAI,peerre- 2024. A survey on llm-as-a-judge. arXiv preprint
viewcommentsgeneratedbyLLMscouldbeused arXiv:2411.15594.
asreferencestohelpreducetheworkloadofhuman
Dongyeop Kang, Waleed Ammar, Bhavana Dalvi,
reviewerstosomeextent.
MadeleinevanZuylen,SebastianKohlmeier,Eduard
Hovy,andRoySchwartz.2018. ADatasetofPeer
9

<!-- Page 10 -->

Reviews(PeerRead): Collection,InsightsandNLP the40thAnnualMeetingoftheAssociationforCom-
Applications. InProceedingsofthe2018Conference putationalLinguistics,pages311–318,Philadelphia,
oftheNorthAmericanChapteroftheAssociationfor Pennsylvania,USA.AssociationforComputational
ComputationalLinguistics: HumanLanguageTech- Linguistics.
nologies,Volume1(LongPapers),pages1647–1661,
NewOrleans,Louisiana.AssociationforComputa- ZacharyRobertson.2023. GPT4isSlightlyHelpfulfor
tionalLinguistics. Peer-Review Assistance: A Pilot Study. Preprint,
arXiv:2307.05492.
Jaeho Kim, Yunseok Lee, and Seulki Lee. 2025. Position: The AI Conference Peer Review Crisis De-
ChenhuiShen,LiyingCheng,RanZhou,LidongBing,
mandsAuthorFeedbackandReviewerRewards. In

### YangYou,andLuoSi.2022. MReD:AMeta-Review


### Forty-SecondInternationalConferenceonMachine

DatasetforStructure-ControllableTextGeneration.
LearningPositionPaperTrack.
In Findings of the Association for Computational
Linguistics: ACL 2022, pages 2521–2535, Dublin,

### Kimi-Team, Angang Du, Bohong Yin, Bowei Xing,

Ireland.AssociationforComputationalLinguistics.

### Bowen Qu, Bowen Wang, Cheng Chen, Chenlin

Zhang, Chenzhuang Du, Chu Wei, and 1 others.

## Kimi-vl technical report. arXiv preprint LinShi,ChiyuMa,WenhuaLiang,XingjianDiao,WearXiv:2504.07491. icheng Ma, andSoroush Vosoughi. 2025. Judging

theJudges: ASystematicStudyofPositionBiasin
DharshanKumaran,StephenM.Fleming,LarisaMar- LLM-as-a-Judge. Preprint,arXiv:2406.07791.
keeva,JoeHeyward,AndreaBanino,MrinalMathur,
RazvanPascanu,SimonOsindero,BenedettodeMar- Cheng Tan, Dongxin Lyu, Siyuan Li, Zhangyang
tino,PetarVelickovic,andVioricaPatraucean.2025. Gao, Jingxuan Wei, Siqi Ma, Zicheng Liu, and
How Overconfidence in Initial Choices and Un- Stan Z. Li. 2024. Peer Review as A Multi-Turn
derconfidence Under Criticism Modulate Change andLong-ContextDialoguewithRole-BasedInterof Mind in Large Language Models. Preprint, actions. Preprint,arXiv:2406.05688.
arXiv:2507.03120.

### AmanSinghThakur,KartikChoudhary,VenkatSrinik

Weixin Liang, Yuhui Zhang, Hancheng Cao, Binglu
Ramayapally,SankaranVaidyanathan,andDieuwke

### Wang,DaisyDing,XinyuYang,KailasVodrahalli,


### Hupkes. 2025. Judging the Judges: Evaluating


### Siyu He, Daniel Smith, Yian Yin, Daniel McFar-

Alignment and Vulnerabilities in LLMs-as-Judges.
land, and James Zou. 2023. Can large language
Preprint,arXiv:2406.12624.
models provide useful feedback on research papers? A large-scale empirical analysis. Preprint,
JasonWei,XuezhiWang,DaleSchuurmans,Maarten
arXiv:2310.01783.
Bosma, BrianIchter, FeiXia, EdChi, QuocV.Le,
andDennyZhou.2022. Chain-of-ThoughtPrompt-
Chin-Yew Lin. 2004. ROUGE: A Package for Autoing Elicits Reasoning in Large Language Models.
maticEvaluationofSummaries. InTextSummariza-
AdvancesinNeuralInformationProcessingSystems,
tionBranchesOut,pages74–81,Barcelona,Spain.
35:24824–24837.
AssociationforComputationalLinguistics.
RyanLiu,JiayiGeng,JoshuaPeterson,IliaSucholut- Shengwei Xu, Yuxuan Lu, Grant Schoenebeck, and
sky,andThomasL.Griffiths.2024a. LargeLanguage Yuqing Kong. 2024. Benchmarking LLMs’ Judg-
ModelsAssumePeopleareMoreRationalthanWe ments with No Gold Standard. In The Thirteenth
Reallyare. InTheThirteenthInternationalConfer- International Conference on Learning RepresentaenceonLearningRepresentations. tions.
RyanLiuandNiharB.Shah.2023. ReviewerGPT?An AnYang,AnfengLi,BaosongYang,BeichenZhang,
ExploratoryStudyonUsingLargeLanguageModels BinyuanHui,BoZheng,and1others.2025. Qwen3
forPaperReviewing. Preprint,arXiv:2306.00622. technicalreport. Preprint,arXiv:2505.09388.
YinhongLiu,HanZhou,ZhijiangGuo,EhsanShareghi,

### JianxiangYu,ZichenDing,JiaqiTan,KangyangLuo,

IvanVulic´,AnnaKorhonen,andNigelCollier.2024b.

### ZhenminWeng,ChenghuaGong,LongZeng,Ren-

AligningwithHumanJudgement: TheRoleofPair-

### JingCui,ChengchengHan,QiushiSun,ZhiyongWu,

wisePreferenceinLargeLanguageModelEvaluators.
Yunshi Lan, and Xiang Li. 2024. Automated Peer
InFirstConferenceonLanguageModeling.
ReviewinginPaperSEA:Standardization, Evaluation, and Analysis. In Findings of the Association
Shiyin Lu, Yang Li, Qing-Guo Chen, Zhao Xu, WeiforComputationalLinguistics: EMNLP2024,pages
huaLuo,KaifuZhang,andHan-JiaYe.2024. Ovis:
10164–10184,Miami,Florida,USA.Associationfor
Structuralembeddingalignmentformultimodallarge
ComputationalLinguistics.
languagemodel. arXivpreprintarXiv:2405.20797.
KishorePapineni,SalimRoukos,ToddWard,andWei- WeizheYuan,PengfeiLiu,andGrahamNeubig.2021a.
JingZhu.2002. Bleu: AMethodforAutomaticEval- CanWeAutomateScientificReviewing? Preprint,
uation of Machine Translation. In Proceedings of arXiv:2102.00176.
10

<!-- Page 11 -->

WeizheYuan,GrahamNeubig,andPengfeiLiu.2021b.
BARTScore: EvaluatingGeneratedTextasTextGeneration. InAdvancesinNeuralInformationProcessingSystems.
Tianyi Zhang, Varsha Kishore, Felix Wu, Kilian Q.

### Weinberger, and Yoav Artzi. 2020. BERTScore:

Evaluating Text Generation with BERT. Preprint,
arXiv:1904.09675.

### PenghaiZhao,QinghuaXing,KairanDou,JinyuTian,

Ying Tai, Jian Yang, Ming-Ming Cheng, and Xiang Li. 2024. From Words to Worth: Newborn
Article Impact Prediction with LLM. Preprint,
arXiv:2408.03934.

### LianminZheng,Wei-LinChiang,YingSheng,Siyuan


### Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin,

Zhuohan Li, Dacheng Li, Eric Xing, and 1 others.

## Judging llm-as-a-judge with mt-bench and

chatbotarena. Advancesinneuralinformationprocessingsystems,36:46595–46623.

### RuiyangZhou,LuChen,andKaiYu.2024. IsLLMa


### ReliableReviewer? AComprehensiveEvaluationof

LLMonAutomaticPaperReviewingTasks. InProceedingsofthe2024JointInternationalConference
onComputationalLinguistics,LanguageResources
andEvaluation(LREC-COLING2024),pages9340–
9351,Torino,Italia.ELRAandICCL.

### JinguoZhu,WeiyunWang,ZheChen,ZhaoyangLiu,

Shenglong Ye, Lixin Gu, Hao Tian, Yuchen Duan,

### WeijieSu, JieShao, and1others.2025. Internvl3:

Exploring advanced training and test-time recipes
foropen-sourcemultimodalmodels. arXivpreprint
arXiv:2504.10479.

### Zhenzhen Zhuang, Jiandong Chen, Hongfeng Xu,

Yuwen Jiang, and Jialiang Lin. 2025. Large languagemodelsforautomatedscholarlypaperreview:
Asurvey. Preprint,arXiv:2501.10326.
11

<!-- Page 12 -->

9 9
9
8
8 Qwen2.5-VL-7B 8
7 e ro
7 QwQewn2e.n52-.V5-LV-7LB-32B
7 Qwen2.5-VL-72B
e ro c s e
g a re 5
6 c s e g a re
v A 4

## 5 6 Q Q


## D

w w
e

## Q D


### Ge

e e
p
w e
e
n n
s
e
m
2 2
e
e p . .
e
n
i
5 5s
nk
2 e - -
i-
.V Ve
-
5

## R2

k -L L
.
-
1

## V

5

## R - -

-

## 3 7 L 1

f
2 2
l
-
a

## 7B B

s
2
h

## B 6 Q Q


## G

w
e
w
m
e e n n
in
2 2
i
. .
-
5 5
2
- -
.

## V V

5-

## L L

fl
- -
a
7 3
s

## B 2

h

## B

v A GeCmlianuid-2e.-5so-fnlnaseht-4 5
4 3 Chatgpt-4o-latest

### ClaCuhdaet-gspotn-4noe-t-la4test

3 2 ChGatrgoputn-4dotr-ulathtest 4 Claude-sonnet-4
4000 6000 8000 10000 Groundtruth
2 4000 6000Length (8t0o0ke0ns) 10000 Groundtruth 3
Length (tokens)
2
Figure2: Theaveragescoresundertext-onlyinputset-
7 8 9 10 11
9 ting,withcontextlengthmeasuredintokens.
8 Figure3: Theaveragescoresunderpdf-as-imageinput
e ro 7 Appendix Q Q w w e e n n 2 2 . . 5 5 - - V V L L - - 7 3 2 2 B B s im et a ti g n e g s , . withcontextlengthmeasuredinthenumberof
c s
e
6

### Qwen2.5-VL-7B

g Asasupplement,weprovideadditionalmaterials
a re 5 Gemini-2.5-flash
v A 4 intheappendix,includingexten Ch d a e tg d pt- e 4 x o- p la e te r s i t mental for more informative content. To investigate the
results and analyses (Appendix A), implementa-
3 Claude-sonnet-4 influenceofreferencesonmodelperformance,we
tiondetailsoftheexperiments(AppendixB),case
Groundtruth conduct an ablation study (Table 10) comparing
2
studiesC,aswellasthepromptsusedduringthe
7 8 9 10 11 inputswithandwithoutthereferencesection. ReconstruLecntgitoh n(paagnesd)applicationofthebenchmark(Apsults indicate that removing references improves
pendixD).
performance on tasks such as Chain-of-Thought
(CoT)scoring,alignmentwithhumanpreferences,

### A MoreResultsandAnalysis

anddetectionofhallucinatedstrengthsandweak-
A.1 TheImpactofPaperLength nesses. Incontrast,fortasksinvolvingquantitative
quality assessments, such as Soundness Scoring
As a long-context task, peer review performance
(SS)andPresentationScoring(PS),theinclusion
maybeinfluencedbythelengthofthemanuscript.
ofreferencesprovesbeneficial,astheirabsenceren-
To examine this, we analyze the average scores
dersthemanuscriptlesscompleteandincreasesthe
assignedbyLLMsundertwoinputsettings: textmodel’sMAE.Thissuggestsatrade-off: whilerefonly(withcontextlengthmeasuredintokens)and
erencesenhancecontentcompletenessandimprove

### PDF-as-image (with context length measured by

technicalevaluations,theirremovalshortenstheinthe number of rendered pages). As illustrated in
put context and may reduce length-related bias,
Figures 2 and 3, we observe a consistent trend
enabling models to make final judgments more
wherein models tend to assign higher scores as
alignedwithhumanpreferences.
thecontextlengthornumberofimagesincreases.
Thisupwardbiasdoesnotalignwellwithhuman

### B MoreImplementationDetails

reviewerjudgmentsacrossmultipleintervals,indicatinganinherenttendencyofLLMstoovervalue For LLMs and MLLMs with parameter sizes up
longerinputsirrespectiveofactualcontentquality. to 72B, we conducted evaluations through direct
Suchlength-inducedbiasposesasignificantchal- model deployment, while for models exceeding
lengeforthepracticaldeploymentofLLMsinpeer 72Borproprietarymodels,weperformedtesting
reviewscenarios. viaAPIaccess. Allexperimentswerecarriedout
on NVIDIA A100 GPUs. To enhance the repro-

### A.2 TheImpactofReferenceSection

ducibility of our results, we set the temperature
References are a critical component of academic parameter to 0. Prompt templates and evaluation
writing, serving to substantiate claims and situ- scripts were manually crafted with reference to
atetheworkwithinthebroaderscholarlycontext. reviewerguidelinesfrommajoracademicconfer-
However, for LLMs lacking internet access, the ences. The prompts used in the evaluations are
referencesectionmayconsumeasubstantialpor- providedintheappendix.
tionoftheinputcontextwithoutprovidingdirect Allofthehumanannotatorsandreviewersmenutility,therebyreducingtheavailabletokenspace tionedinthispaperwereselectedfromagroupof
12

<!-- Page 13 -->

Step Outcome Preference Attack

### Model

SB↑ SL↑ SEB↑ SEL↑ WEB↑ WEL↑ SS↓ PS↓ CD↓ DD↓ CoD↓ MD↑ PR↑ FS↓ FW↓ PI↓
InternVL3-2B -3.11 3.67 -3.95 2.87 -4.04 1.89 0.52 0.48 1.99 2.56 2.94 60.94 53.13 2.48 1.10 0.57
Qwen2.5-VL-3B -3.11 3.55 -3.74 3.33 -3.97 1.89 0.47 0.44 1.87 3.24 3.74 55.42 57.29 3.18 2.88 0.08
Tiny Kimi-VL-A3B-I -3.12 3.53 -3.69 3.52 -3.96 1.86 0.47 0.44 2.40 3.61 3.94 60.68 54.17 3.00 0.13 0.65
Kimi-VL-A3B-T -3.13 3.60 -3.68 3.74 -3.92 2.37 0.47 0.47 2.31 3.56 3.64 61.60 62.50 3.14 0.33 0.36
Avg. -3.12 3.59 -3.76 3.37 -3.97 2.00 0.48 0.46 2.14 3.24 3.56 59.66 56.77 2.95 1.11 0.42
Qwen2.5-VL-7B -3.09 3.64 -3.67 3.70 -3.94 2.11 0.47 0.44 2.20 3.59 3.49 75.83 64.58 3.00 1.45 0.28
InternVL3-8B -3.21 3.46 -3.82 3.26 -4.12 1.84 0.47 0.44 3.02 3.72 3.68 61.11 54.17 3.00 1.33 0.32
OVIS2-8B -3.20 3.43 -3.72 3.49 -3.97 2.06 0.50 0.53 2.27 3.79 4.44 62.91 66.28 3.00 2.15 0.58

### Small

GLM-4.1V-9B-T -3.20 3.48 -3.69 3.70 -3.93 2.60 0.50 0.47 2.42 3.68 3.59 70.72 59.77 3.02 1.80 0.31
OVIS2-16B -3.13 3.50 -3.70 3.29 -3.98 2.04 0.47 0.44 2.16 3.40 3.91 78.03 65.12 3.00 2.10 0.04
Avg. -3.16 3.50 -3.72 3.49 -3.99 2.13 0.48 0.46 2.41 3.64 3.82 69.72 61.98 3.00 1.77 0.31
Qwen2.5-VL-32B -2.99 3.89 -3.64 3.76 -3.90 2.45 0.81 0.75 2.24 3.47 3.94 76.25 60.42 3.00 1.57 0.49
OVIS2-34B -3.11 3.51 -3.69 3.43 -3.97 2.26 0.88 0.81 2.33 3.78 3.91 73.76 62.79 3.00 1.78 0.28

### Middle

Qwen2.5-VL-72B -3.04 3.74 -3.66 3.71 -3.95 2.33 0.47 0.50 2.06 3.73 3.73 69.58 60.42 3.01 1.30 0.63
Avg. -3.05 3.71 -3.67 3.63 -3.94 2.35 0.72 0.69 2.21 3.66 3.86 73.20 61.21 3.00 1.55 0.47
Chatgpt-4o-latest -3.10 3.86 -3.60 3.85 -3.87 2.67 0.91 0.94 2.24 3.65 3.75 75.97 59.38 3.88 1.22 0.46
Claude-sonnet-4 -3.02 3.86 -3.60 3.88 -3.83 3.09 0.47 0.44 1.19 2.19 2.09 84.17 69.79 2.98 2.12 0.32

### Large

Gemini-2.5-flash -3.08 3.75 -3.56 3.84 -3.87 2.58 0.91 0.88 1.34 4.60 4.19 76.25 68.75 2.89 0.78 0.41
Avg. -3.07 3.82 -3.59 3.86 -3.86 2.78 0.76 0.75 1.59 3.48 3.34 78.79 65.97 3.25 1.37 0.40
Table8: ResultsonMMReviewwithmultimodalinputs.
Step Outcome Preference Attack

### Model

S ↑ S ↑ SE ↑ SE ↑ WE ↑ WE ↑ SS↓ PS↓ CD↓ DD↓ CoD↓ MD↑ PR↑ FS↓ FW↓

## B L B L B L

InternVL3-2B -3.28 3.28 -4.80 1.51 -4.55 1.19 0.48 1.61 1.57 1.77 3.34 72.38 50.00 3.00 1.11
Qwen2.5-VL-3B -3.29 3.12 -3.76 3.34 -3.98 1.86 0.47 0.44 1.73 3.05 3.72 53.75 54.17 3.01 2.94
Tiny Kimi-VL-A3B-I -3.21 3.17 -3.74 3.34 -4.00 1.74 0.47 0.44 2.30 3.19 3.83 69.36 55.21 0.28 0.00
Kimi-VL-A3B-T -3.21 3.50 -3.71 3.72 -3.91 2.54 0.47 0.44 1.85 3.72 3.49 74.37 60.42 3.11 0.27
Avg. -3.25 3.27 -4.00 2.98 -4.11 1.83 0.47 0.73 1.86 2.93 3.59 67.47 54.95 2.35 1.08
Qwen2.5-VL-7B -3.21 3.28 -3.72 3.49 -3.95 1.91 0.47 0.44 1.97 3.09 3.12 70.83 47.92 2.99 1.01
InternVL3-8B -4.86 1.13 -4.59 1.89 -4.55 1.13 0.47 0.44 2.40 3.63 3.41 68.75 75.00 2.99 1.98
OVIS2-8B -3.23 3.28 -3.70 3.43 -3.99 2.06 0.47 0.44 2.49 3.44 3.93 65.32 53.13 3.00 2.00

### Small

GLM-4.1V-9B-T -3.26 3.36 -3.67 3.69 -3.92 2.69 0.47 0.44 1.80 3.51 3.13 80.33 65.63 3.00 1.82
OVIS2-16B -3.20 3.42 -3.70 3.49 -3.97 2.17 0.47 0.44 2.05 3.23 3.76 78.66 54.17 3.00 1.81
Avg. -3.55 2.89 -3.88 3.20 -4.08 1.99 0.47 0.44 2.14 3.38 3.47 72.78 59.17 2.99 1.72
Qwen2.5-VL-32B -3.11 3.66 -3.71 3.67 -3.92 2.46 0.78 0.81 2.11 3.55 3.77 67.50 61.46 3.24 1.22
OVIS2-34B -3.20 3.41 -3.68 3.49 -3.99 2.18 0.78 0.69 1.91 3.63 3.74 77.82 52.08 2.99 1.69

### Middle

Qwen2.5-VL-72B -3.11 3.57 -3.71 3.46 -3.95 2.22 0.47 0.59 2.15 3.76 3.77 70.00 54.17 3.03 1.11
Avg. -3.14 3.55 -3.70 3.54 -3.95 2.29 0.68 0.70 2.06 3.65 3.76 71.77 55.90 3.09 1.34
Chatgpt-4o-latest -3.33 3.65 -3.69 3.70 -3.88 2.68 0.91 0.91 1.84 3.63 3.68 77.73 59.38 3.90 1.33
Claude-sonnet-4 -3.19 3.59 -3.65 3.73 -3.90 2.88 0.48 0.45 1.22 2.36 2.22 82.92 62.50 3.00 2.73

### Large

Gemini-2.5-flash -3.31 3.26 -3.66 3.73 -3.93 2.48 0.91 0.91 1.11 4.60 4.19 73.33 69.79 1.67 0.75
Avg. -3.28 3.50 -3.67 3.72 -3.90 2.68 0.77 0.75 1.39 3.53 3.36 77.99 63.89 2.85 1.60
Table9: ResultsonMMReviewwithpdf-as-imageinputs.
model SS↓ PS↓ CD↓ DD↓ CoD↓ MD↑ PR↑ FS↓ FW↓ PI↓

### Deepseek-V3

0.53 0.47 2.62 3.37 3.70 0.75 0.66 2.99 0.66 0.20
w.o.Ref

### Deepseek-V3

0.47 0.44 2.56 3.26 3.74 0.83 0.57 2.99 0.71 0.19
w/Ref
Table10: Theinfluenceofreferencesonmodelperformance.
fivePhDstudents,eachwithextensivesubmission theobjectivesofthesetasks. Theywerecompenexperienceandabackgroundinreviewingforaca- satedatamarket-averagehourlyrateof$30/hfor
demicconferencessuchasARRandAAAI,aswell theirwork.
asanadequateknowledgebaseinthefieldscovered
by the papers. These individuals were provided C Casestudies
with clear instructions regarding the high-quality
paper selection and review comment annotation In this section, we present two representatasks they were required to complete, along with tive case studies from the evaluation results of
13

<!-- Page 14 -->

chatgpt-4o-latest,correspondingtopaperssub- promptbasedontheLikertscaleusedforLLM-asmitted to ICLR and Nature Communications, re- a-judgeevaluation.
spectively.
• Taskgenerationprompt: Figure14

### InCase1(Figures4–9),themodelwastasked

withcompletingallbenchmarktasksusingatext-
• Systemprompt: Figure15
onlyinput. Humanannotationshighlight(ingreen)
the portions of the model’s responses that align • Summary: Figure16
with the original reviewer comments. The eval-
• StrengthsandWeaknesses: Figure17-18
uated paper was a rejected submission to ICLR

## While the model provided a relatively fa-

• SoundnessScoringandPresentationScoring:
vorable overall assessment and high score in the

### Figure19


### CoTDecisiontask,itidentifiedmoreweaknesses

thanstrengths,consistentwiththehumanreview- • ConditionalDecision: Figure20
ers’ concerns, indicating partial alignment with
• DirectDecision: Figure21
humanjudgment. Whenactingasanareachairin
theMetaDecisiontask,themodelsuccessfullysyn-
• CoTDecition: Figure23
thesizedrevieweropinionstoarriveatajustifiedrejectiondecision,showcasingitsabilitytointegrate • MetaDecision: Figure22
andsummarizemultiplereviews. However,inthe
• PreferenceRank: Figure24
PromptInjection(PI)task,despitethepromptbeingidenticaltothatoftheCoDtask, themodel’s
• FakeStrengthsandFakeWeaknesses: Figure
outputexhibitedastrongbiastowardhighlighting
25
strengths (highlighted in yellow) and delivered a
morefavorablefinalassessment,underscoringthe • PromptInjection: ThesameasCoTDecision
significantinfluenceofpromptinjectiononmodel (Figure23)
behavior.
• LLM-as-a-judge: Figure26

### InCase2(Figures10–13),themodelreviewed

an accepted paper from Nature Communications
using the pdf-as-image input modality. Again,
human annotations indicate alignment between
the model’s outputs and human-written review
comments. As expected for an accepted paper,
themodelemphasizedstrengthsoverweaknesses.
However,intheMetaDecisiontask,duetotheabsenceofexplicitquantitativescoresintheoriginal
reviewer comments, the model struggled to infer
the reviewers’ overall preference and mistakenly
issued a rejection decision. This case highlights
the challenges LLMs face when interpreting unstructuredorqualitativefeedbackintheabsenceof
scoringsignals.

### D Prompts

In this section, we present the prompts used
throughouttheconstructionandevaluationphases
ofthebenchmark. Figure14illustratestheprompt
employedinthetaskgenerationstagetoproduce
antonymic rewrites of strengths and weaknesses.
Figures 15 through 25 display the prompts correspondingtothevarioustasksdesignedwithinthe
benchmark. Additionally, Figure 26 presents the
14

<!-- Page 15 -->


### Summary

### Sum mary of the Paper
This pap er proposes the **Additive Poisson Process (APP)**, a novel modeling framework designed to estimate intensity functions of multidimensional Poisson processes, particularly under **sparse observation scenarios**. The key idea is to **leverage lower-dimensional projections**
to learn the higher-order interaction effects between dimensions of the event space, thereby overcoming the **curse of dimensionality** and the
**data sp arsity** problem inherent in high-dimensional event modeling.
---
### Key Contributions
1. **APP Model Formulation via Log-Linear Structure**
The authors model the Poisson process on a **partially ordered set (poset)** using a **log-linear formulation**, which enables capturing
hierarchi cal interaction effects between subsets of dimensions. Each node in the poset represents either a full joint event or a projection (marginal)
over few er dimensions.
2. **Gen eralized Additive Model (GAM) Integration**
The framework draws a tight connection between **GAMs and Poisson processes**, enabling the decomposition of the intensity function into
additive components over lower-order interactions. This is theoretically supported by the **Kolmogorov–Arnold representation theorem**.
3. **Convex Optimization via Information Geometry**
The APP parameters are learned through **convex optimization**, specifically by minimizing the **KL divergence** between the observed data
distributi on and the modeled one. The authors use **natural gradient descent** based on **Fisher information geometry**, ensuring convergence
and stability.
4. **Effi cient Discretization for Scalability**
By discretizing time into bins and using a **kernel-based smoothing** mechanism, the method remains tractable even in high-dimensional setups,
where tra ditional methods struggle with computational infeasibility.
5. **Empirical Validation**

### The pa per provides extensive experiments across:

- **Low- and high-dimensional synthetic data** (2D to 4D),
- **Real-world New York City taxi data**,
and co mpares against **KDE**, **RKHS-based models**, and **Bayesian mixtures** (e.g., DP-beta). APP outperforms or matches these
baselines, especially in sparse data scenarios.
---
### Ove rall Impression
This work introduces a theoretically grounded and computationally feasible approach to modeling complex event dynamics using Poisson processes.
Its **inn ovation lies in bridging information geometry, additive modeling, and discrete probabilistic structures**, all while maintaining empirical
robustness across real and synthetic datasets. The APP model's **adaptability to sparsity** and **higher-order structure** makes it a promising tool
in domains like spatial-temporal modeling, ecology, and transportation analytics.
Figure4: ResultofSummarytaskincase1.
15

<!-- Page 16 -->


### Strengths

Here’s a **detailed assessment of the strengths** of the paper titled *“Additive Poisson Process: Learning Intensity of Higher-Order Interaction in Poisson Processes”*
across the requested d imensions:
### ✅ **Quality**
**Technical Soundne ss**
The paper is technic ally **solid and well-structured**, leveraging a clear chain of reasoning grounded in **information geometry**, **generalized additive models
(GAMs)**, and **log-linear models**. It reformulates the problem of learning high-dimensional intensity functions as a **convex optimization problem**, which is both
tractable and theoretic ally justified. The authors carefully formulate the model based on established results like the **Kolmogorov-Arnold representation theorem**, offering
a strong theoretical backbone.
**Methodological Appropriateness**
The shift from high-d imensional Poisson process modeling to learning through **lower-dimensional projections** is a clever and principled workaround to the curse of
dimensionality. The use of **natural gradient descent** via Fisher information is appropriate and elegant, especially for convex optimization on statistical manifolds.
**Evaluation Rigor**
Empirical results are provided across a range of scenarios (synthetic and real-world), including **dense and sparse** data regimes and **higher-order processes**. This
gives credibility to the generalizability and robustness of the method. Comparisons with **KDE, RKHS, and DP-beta** models are fair and clear.
**Honesty and Limita tions**
The authors are upfro nt about trade-offs—like the **combinatorial scaling** with interaction order and the **computational overhead** of Fisher matrix inversion. They
also recognize that in higher dimensions, some comparative models couldn't even complete execution, which is noted honestly without overstating APP’s advantages.
### **Clarity**
**Writing and Structure**
The paper is mostly c lear, especially given the complexity of the subject. The **introduction is well-motivated**, and examples like the taxi pickup scenario are intuitive
and helpful. Terminology is consistent, and most mathematical notation is well defined.
**Suggestions for Improvement**
- The paper occasiona lly introduces **dense mathematical notation without visual summaries** (e.g., Equations 6–11), which could hinder readability for some readers. A
summary table of key symbols or a diagram of the optimization pipeline might help.
- Some transitions, pa rticularly from GAM to the Poisson model via the log-linear formulation, could be more explicitly scaffolded for clarity.
**Reproducibility**
The paper is detailed enough to allow implementation, and the description of synthetic data generation, hyperparameter selection, and model comparisons supports
reproducibility.
### **Significance**
**Impact and Usefuln ess**
This work has **broad applicability** in domains like transportation, finance, and ecological modeling—anywhere **event interactions** occur across **multi-dimensional
sparse spaces**. The ability to estimate intensity functions with **low joint observations** is highly valuable.
**Advancement Over Prior Work**
- It addresses core limitations of kernel density methods (curse of dimensionality), Bayesian methods (non-convexity, infeasibility in sparse/high-dim regimes), and variational
inference (lack of convergence guarantees).
- The combination of statistical geometry and GAMs represents a **novel way to bridge structured inference and tractable optimization**.
**Adoption Potential**
The framework’s **m odularity and interpretability** (e.g., the partial order graph structure allowing domain-specific priors) could make it attractive for practical deployments
by researchers and pra ctitioners alike.
### **Originality* *
**Novel Contribution s**
- Introduces a novel formulation: the **Additive Poisson Process (APP)**, combining insights from **GAMs, log-linear models, and information geometry**.
- Leverages the **Ko lmogorov-Arnold theorem** to justify the use of projections and additive decomposition in the modeling of higher-order intensity functions.
- Applies **log-linear models on partially ordered sets**, which is quite a unique and elegant design for modeling interactions in a principled way.
**Contextualization within Literature**
The authors thorough ly situate their work within the landscape of Poisson process modeling—covering **KDE**, **Bayesian inference**, **Poisson factorization**, and
**variational inference**. The distinctions are **clearly articulated**, and the authors highlight both the theoretical and practical shortcomings of competing methods.
**Insightfulness**
Even without introduc ing entirely new types of inference, the paper **reframes an important modeling problem** using **underutilized tools (e.g., natural gradients, poset
structures)** in a compelling way.
### **Overall Str engths Summary**
- **Innovative yet grounded**: A fresh framework backed by strong theoretical justifications and ties to existing work.
- **Practical and scal able**: Performs well in both synthetic and real-world sparse data, where many traditional methods fail or are infeasible.
- **Empirically supported**: Experiments are thoughtfully designed, demonstrating robustness and effectiveness across dimensions and sample sizes.
- **General-purpose and extensible**: The framework offers enough modularity and flexibility to adapt to various domains and data conditions.
### ✅ Final Note
This paper represents a **complete, original, and methodologically sound contribution** to the modeling of higher-order interactions in Poisson processes. While minor
clarity improvements could help accessibility, its strengths in theory, practice, and novelty are substantial. A strong accept is justifiable on these grounds.
Figure5: ResultofSEtaskincase1.
16

<!-- Page 17 -->


### Weaknesses

Here’s a comprehensive review of the **weaknesses** in the paper titled **“Additive Poisson Process: Learning Intensity of Higher-Order Interaction in Poisson
Processes”**, structu red across the requested dimensions:
## **Quality**
### 1. **Lack of The oretical Guarantees and Error Bounds**
While the method is rooted in strong theoretical tools (e.g., information geometry, Kolmogorov-Arnold representation), the paper **does not provide formal theoretical
guarantees**:- There are **no bounds on estimation error**, convergence rates, or sample complexity.- The authors refer to robustness and efficiency in practice, but this is
largely **empirical a nd anecdotal**.
### 2. **Evaluation of Robustness is Limited**
Although the paper c laims robustness to sample size and sparsity, **no ablation study or sensitivity analysis** (except for a brief bandwidth sensitivity analysis in the
appendix) explicitly demonstrates this.- For example, how does APP behave with noisy observations, misspecified bandwidths, or temporal heterogeneity?
### 3. **Over-reliance on Discretization**
The discretization ap proach is central to tractability, but:- It **introduces bias** that isn’t well-characterized.- The authors state that **$M$ and $h$ are chosen by grid
search**, but don't show how sensitive the model is to these choices in real-world settings.
### 4. **Limited Baselines**
In higher-dimensiona l and real-world experiments, competing baselines like KDE, RKHS, and DP-beta are omitted due to scalability issues.- While the explanation is fair,
**it reduces the credibility of comparative performance claims**. One could argue the comparisons were not “apples to apples”.- Furthermore, more modern or scalable
baselines (e.g., GP-ba sed variational methods or sparse log-Gaussian Cox processes) are not considered, despite being mentioned in related work.
## **Clarity**
### 1. **Overly Den se and Formal Exposition**
The paper is **mathematically dense**, particularly in:- The log-linear formulation in Section 4 (Additive Poisson Process).- The optimization section, especially regarding
the derivation and use of the Fisher Information matrix.These sections **assume significant prior familiarity** with posets, natural gradients, and information geometry,
limiting accessibility.
### 2. **Lack of Concrete Examples in Technical Sections**
The introductory taxi example is helpful, but the **core technical sections do not carry this example forward**.- For instance, Equation (8) introduces complex parameter
spaces and partition f unctions **without tying them back** to intuitive use cases or diagrams.
### 3. **Notational Overload**
There is excessive no tation:- Use of multiple overlapping index sets (e.g., $I \\subseteq J$, $J \\subseteq [D]$, $\\omega = (J, \\tau)$).- The inclusion of both Poisson intensity
functions and log-line ar probability densities **can be confusing** without clearer disambiguation.
### 4. **Missing Discussion of Practical Implementation Details**
There is limited discu ssion on:- How to efficiently implement the optimization in high dimensions.- Practical heuristics for choosing hyperparameters or designing the partial
order graph in applie d settings.
## **Significanc e**
### 1. **Impact of the Contribution is Not Fully Demonstrated**
While the framework is potentially powerful, the paper **does not show enough compelling real-world benefits**:- The NY taxi dataset is a step in the right direction, but
the results are modes t and not deeply analyzed.- There is **no discussion of interpretability**, which is often a strength of additive models.
### 2. **Scalability Trade-offs Are Not Addressed Deeply**
Although the APP model scales better than certain baselines, it still **scales combinatorially with the order and dimensionality**. The authors acknowledge this but do not
propose practical wor karounds (e.g., low-rank approximations, truncation strategies).
### 3. **No Real Application Deployment or Downstream Use**
The paper doesn’t sh ow how APP would integrate into a practical pipeline, for instance:- For event prediction, anomaly detection, or intervention planning.This makes its
**practical utility spe culative** at this stage.
## **Originality* *
### 1. **Incremental vs. Novel Contribution**
The main innovation is a **combination of existing ideas**:- Additive modeling (GAMs),- Log-linear models on posets,- Natural gradients in exponential families.While
well-integrated, the * *paper lacks a crisp articulation of what is truly novel**:- Is it the use of partial orders in high-order Poisson processes?- The specific optimization
framework?- The connection to Kolmogorov-Arnold theorem in this domain?
### 2. **Limited Discussion of Prior Art**
Although Appendix A gives a review of Poisson factorization and Bayesian inference, the paper **underemphasizes recent advancements**:- Deep point process models
(e.g., Neural Hawkes).- Spatiotemporal models with variational approximations (like Cox Processes).This leaves a gap in understanding where APP sits in the contemporary
modeling landscape.
## Suggestions for Improvement
1. **Add theoretical error guarantees** for approximation or convergence.

## Include a **qualita tive comparison** of interpretability or parameter insights from APP vs. other models.


## Provide **visual aids or toy examples** within the technical sections to make the model more intuitive.


## Explore more **sc alable competing baselines**, even if approximate (e.g., sparse GP-based Cox models).


## Show how the model might be **used in practice** — for example, for forecasting or optimization.

## Summary
The paper proposes an interesting and theoretically grounded approach to modeling high-order interactions in Poisson processes via additive structures. However, **technical
complexity, lack of strong comparative baselines**, and **limited practical demonstration** hinder its impact. Improvements in **clarity, theoretical grounding, and
application depth** would make this a more compelling contribution.
Figure6: ResultofWEtaskincase1.
17

<!-- Page 18 -->


### Meta Review

### Meta-Review for: *Additive Poisson Process: Learning Intensity of Higher-Order Interaction in Poisson Processes*
#### **1. Paper Summary**
This pap er introduces the **Additive Poisson Process (APP)**, a novel method for learning the intensity function of high-dimensional Poisson
processe s by leveraging **lower-dimensional projections** and a **log-linear modeling framework**. The core idea is to overcome data sparsity
in high-dimensional Poisson processes by projecting the data into lower-dimensional spaces (leveraging principles from **Generalized Additive
Models (GAM)**) and then estimating the intensity function using **convex optimization**, specifically minimizing the KL divergence between
empirical and model distributions.
The mod el is grounded in **information geometry**, particularly using **natural gradients** for parameter updates. The theoretical framework is
supplemented with both synthetic and real-world experiments (e.g., NYC taxi dataset), showing APP’s effectiveness under sparse observation
regimes.
#### **2. Strengths and Weaknesses**
##### **Strengths**
- **Tim ely Problem**: Addresses a difficult and relevant challenge—learning Poisson process intensity functions in sparse high-dimensional
settings.
- **Meth odological Novelty**: Combines ideas from GAMs, information geometry, and log-linear models in a fresh way.
- **Conv ex Optimization**: The formulation as a convex problem with a natural gradient approach is appealing for its tractability.
- **Scalability Claims**: The method is designed to scale better than prior approaches under certain conditions (e.g., sparse data).
##### **Weaknesses**
- **Overstated Theoretical Claims**: The application of the Kolmogorov-Arnold theorem and the connection to GAMs are sometimes presented
too stron gly or imprecisely. The paper would benefit from a more careful theoretical justification.
- **Empirical Evaluation Limitations**:
- **Limited Baselines**: No comparison to GAMs with tensor product bases, which are closer analogs.
- **Ov erfitting in Visuals**: Figures (e.g., Figure 4) indicate potential overfitting behavior in APP.
- **High-Dimensional Results**: While promising, the scalability claim is weakened by the exponential growth in parameter space and limited
empirica l proof for higher dimensions.
- **Pres entation and Clarity**: Several reviewers noted that the paper could be more concise and clearer—particularly in mathematical exposition
and model intuition.
- **Hyp erparameter Selection**: Key hyperparameters (e.g., bandwidth, bin count) are selected via grid search without sufficient guidance, which
may not be practical for high-dimensional data.
#### **3 . Evaluation of the Reviews**
The reviewers collectively acknowledge the novelty and promise of the proposed method, especially Reviewer 1 and Reviewer 2, who highlight the
importance of the problem and the innovative framing. However:
- **Rev iewer 1** raises critical but constructive points around model flexibility, hyperparameter tuning, and scaling behavior. These are fair
concerns, but they still see potential in the idea.
- **Reviewer 2** and **Reviewer 4** are more skeptical. Reviewer 2 wants more theoretical rigor and guarantees. Reviewer 4 questions the novelty,
arguing the method is a variant of well-known GAM techniques (e.g., tensor-product basis).
- **Reviewer 3** gives a thorough and detailed critique, highlighting both presentation and empirical issues. Their comment about misuse of
theoretic al results (e.g., Kolmogorov-Arnold theorem) is significant.
- Import antly, none of the reviewers claim the method is unsound, only that it is either not convincingly presented or insufficiently evaluated.
The reviews reflect consensus on two fronts:
- The ** idea is promising**.
- The **execution lacks rigor**—theoretical justification, empirical breadth, and presentation need refinement.
#### **4 . Meta-Review Decision**
While the paper takes a promising direction and proposes an original framework for tackling high-dimensional intensity estimation in Poisson
processes, the **concerns raised by the reviewers are substantial and consistent**. Specifically:
- **Theo retical claims** are not carefully justified.
- **Empirical validation** is underwhelming and fails to fully demonstrate superiority over strong baselines.
- **Connections to prior work** (notably GAMs with tensor bases) are insufficiently explored.
- **Pres entation and clarity** issues further undermine the paper’s accessibility.
Given the current state of the submission, I believe the paper does not meet the bar for acceptance at a top-tier venue. However, the contribution is
*not wit hout merit*, and I would strongly encourage the authors to revise the work, address the theoretical and empirical gaps, and resubmit.
\\boxed{ {Reject}}
Figure7: ResultofMDtaskincase1.
18

<!-- Page 19 -->

CoT Decision
### Summary
This paper introduces the **Additive Poisson Process (APP)**, a novel modeling framework for learning higher-order interaction effects in **multidimensiona l Poisson processes** using **lower-dimensional projections**. The core idea is to decompose complex joint intensity functions (which are
hard to estimate due to data sparsity and high dimensionality) into additive lower-order terms, enabling more effective learning. The approach combines
**generalized additive models (GAMs)**, **log-linear models**, and **information geometry** to formulate a convex optimization problem.
Experimen tal results—on synthetic and real-world data (e.g., NYC taxi data)—demonstrate that APP outperforms baseline models like KDE, RKHS, and
DP-beta in scenarios with sparse data or high dimensionality.
### Streng ths and Weaknesses
#### **Quality**
**Strength s:**
Technically sound and grounded in strong theoretical foundations like the **Kolmogorov-Arnold representation theorem** and **information
geometry**. Convex optimization using **natural gradients** ensures global convergence and computational stability. The methodology is carefully
detailed, in cluding explicit formulations and algorithmic procedures (e.g., Fisher information matrix, natural gradient updates). Strong experimental
design—covers synthetic and real-world datasets, varying dimensionalities, and both sparse and dense scenarios.
**Weaknesses:**
Some parts of the derivations are quite dense and could be more reader-friendly. In higher-order experiments, comparisons to other baselines are omitted
(justifiably due to infeasibility) but still leave a gap in relative performance validation. No ablation studies or robustness tests (e.g., varying projection
schemes, sensitivity to bin count or order k) beyond bandwidth sensitivity.
#### **Clarity**
**Strength s:**
Clear prob lem motivation, particularly with the taxi pick-up example. Logical structure from background to formulation, algorithm, and experiments.
Careful definitions of notation, assumptions, and modeling steps.
**Weaknes ses:**
The notation can be heavy and sometimes inconsistent in formatting (e.g., use of subscripts and summations). Sections like the optimization and the
construction of the poset space could benefit from intuitive explanations or diagrams earlier in the section. Figures are referenced but not always fully
explained o r contextualized.
#### **Significance**
**Strength s:**
Tackles a **real and pressing issue** in modeling sparse, high-dimensional event data. The framework is **widely applicable** in areas like
transportation, finance, ecology—where traditional Poisson models struggle.Provides **practical utility** by being robust to sparse observations and
scalable via discretization.
**Weaknesses:**
While prom ising, real-world utility could be more convincingly demonstrated by deploying APP in a concrete decision-making scenario or downstream
task (e.g., d ispatch optimization in transportation). No discussion of integration into end-to-end systems.
#### **Or iginality**
**Strengths:**
The combination of additive modeling, log-linear structure, and convex optimization is **novel and elegant**. Clearly differentiates from KDE, Bayesian
methods, a nd Poisson factorization. Offers a **conceptual advance** by rethinking how joint intensities can be estimated via lower-dimensional
projections.
**Weaknesses:**
The extens ion of GAMs to higher-order Poisson settings is the most innovative component; however, it builds incrementally on prior known tools rather
than being a radical departure.
### Sound ness
The paper is technically sound. The theoretical framework is well-motivated, mathematically solid, and validated through both synthetic and real data
experiment s. The optimization procedure is appropriately defined and grounded in convex theory and natural gradients, ensuring convergence.
**Rating: 9/10**
### Presen tation
Overall, the presentation is good. However, certain sections (particularly involving mathematical notation) could benefit from cleaner formatting, better
notation consistency, and more intuitive verbal explanations. The examples help, but the exposition would be improved with more accessible visualizations.
**Rating: 7 .5/10**
### Final Verdict
This is a ** strong and impactful** paper that introduces a highly relevant, theoretically grounded, and practically useful framework for a well-motivated
problem. It may not be \"truly groundbreaking\" in the sense of creating a completely new paradigm, but it brings together ideas in a novel and effective
way. Minor improvements in clarity and additional empirical exploration would elevate it further.
\\boxed{8}
Figure8: ResultofCoDtaskincase1.
19

<!-- Page 20 -->

Prompt Injection
### Summary
This p aper introduces the **Additive Poisson Process (APP)**, a new modeling framework designed to estimate **high-dimensional intensity
functions** in Poisson processes, especially when direct observations are sparse. The core idea is to use **lower-dimensional projections** to
inform and reconstruct the higher-dimensional intensity structure. The authors cleverly combine tools from **information geometry**, **log-linear
model ing**, and **generalized additive models (GAMs)**. They formulate learning as a **convex optimization problem** minimizing KL
divergence between empirical and modeled distributions. The paper demonstrates APP's **robustness to sample sparsity**, scalability, and
**perf ormance superiority over KDE, RKHS, and Dirichlet process-based approaches**, both on synthetic and real-world datasets (e.g., NYC taxi
data).
### St rengths and Weaknesses
#### **Quality**
- ✅ **Technically sound and theoretically well-motivated**: The authors leverage the Kolmogorov-Arnold representation theorem and link their
model to generalized additive models and log-linear models, providing a strong theoretical foundation.
✅ **Clear derivation of the optimization strategy**: Use of **natural gradients** and the detailed construction of the **Fisher Information
Matrix** shows deep technical care.
- ✅ * *Solid empirical evaluation**: Both synthetic and real-world experiments are thoughtfully designed, with appropriate baselines. Results are
reported in a nuanced manner (e.g., showing performance under sparse and dense cases).
W hile the model is **computationally intensive** (especially with natural gradients), the authors are transparent about the trade-offs and
propos e remedies like jitter and parameter truncation.
#### * *Clarity**
- ✅ The paper is generally **well-written**, with solid motivation and thorough explanations.
✅ Notably strong in **mathematical exposition**—equations are clearly laid out and notations are consistent.
So me sections (especially those involving the poset structure and Equation (8)) may be dense for readers unfamiliar with information geometry.
Adding **intuitive visual aids** (beyond Figure 1) or a small **toy example** could enhance accessibility.
#### * *Significance**
- ✅ This work addresses a **highly relevant challenge** in modern data modeling—capturing sparse, high-dimensional event patterns, which are
comm on in areas like transportation, finance, and ecology.
✅ Th e combination of **convex optimization**, **GAM structure**, and **partial order modeling** offers a **unique contribution** that
extends well beyond existing methods like KDE and RKHS.
- ✅ T he APP shows significant improvements over traditional and even modern Bayesian methods in sparse regimes—**a practical gap that few
papers address well**.
#### **Originality**
✅ Th e idea of combining **log-linear models over a partially ordered set** with GAM-like structures to approximate high-order interactions is
**novel and elegant**.
✅ Prior work like Poisson factorization or Bayesian mixtures lacked this ability to **explicitly encode interaction orders via a controlled parameter
set**, which the APP introduces cleanly.
✅ Connections to Kolmogorov-Arnold’s theorem and natural gradients for convex log-linear models provide **fresh perspectives on classical
problems**.
#### **Soundness**
The th eoretical components are **solid**, and the assumptions are either well-justified or clearly stated. The experimental design is **sensible**
and ex ecuted with proper controls. APP appears to be **well-validated** in both performance and theoretical behavior.
#### * *Presentation**
Strong in terms of **mathematical and algorithmic presentation**, though perhaps heavy for newcomers to the field.
Figures are well-used, though **more interpretative commentary on the plots and visualizations** would improve reader engagement.
A gent le introduction to posets and their use in log-linear models would help broaden accessibility.
### Final Assessment
This is **an excellent, carefully crafted paper** that offers meaningful theoretical and practical contributions to Poisson process modeling. The
APP is a **novel, principled, and practical solution** to a longstanding issue in high-dimensional intensity estimation under sparsity. The paper is
well-written, the evaluations are fair, and the results are strong. A few usability improvements and additional visual explanations would make it
even b etter, but as it stands, this is a clear accept.
\\boxe d{9}
Figure9: ResultofPItaskincase1.
20

<!-- Page 21 -->


### Summary

### Summary of the Paper
This study presents a novel paleoecological analysis of long-term plant taxonomic richness using sedimentary ancient DNA (sedaDNA) from Lake
Naleng on the southeastern Tibetan Plateau. The research aims to understand the drivers and patterns of plant diversity change over the last ~18,000
years, focu sing on how climate and environmental variables have influenced total plant taxon richness (TPTR).
#### Key Contributions:
1. **Time-Series Approach Using sedaDNA**:
The auth ors implement a **continuous time-series analysis** of sedaDNA-derived plant richness, a first of its kind in this region. This allows
for a high-resolution reconstruction of plant diversity trends over millennial timescales, offering richer ecological insights than traditional pollenbased records.
2. **Nonlinear Relationship Between Richness and Temperature**:
The paper challenges the intuitive link between temperature and biodiversity. It finds that **total plant richness does not consistently increase
with temp erature**. In fact, correlations vary by time period—positive during 18–10 ka, but negative in others (e.g., 10–0 ka), suggesting
**nonlinear or indirect relationships**, possibly due to complex interactions between temperature, disturbance regimes, and habitat extent.
3. **Alpin e Habitat Extent as a Key Predictor**:
Using statistical models (Spearman correlation, generalized linear modeling), the study identifies **alpine habitat extent** as the **strongest and
most consi stent predictor** of total plant richness. A decline in alpine habitat due to warming is linked to a decline in richness, reinforcing the
importance of spatial ecological heterogeneity.
4. **Predic tion of Future Diversity Decline**:
By modeling a future warming scenario (+2.5°C by 2300), the authors predict a **substantial decline in total plant taxon richness**—up to 30–
40%—due to the **loss of alpine habitat**. This forward-looking simulation ties paleoecological patterns directly to anticipated anthropogenic
change.
5. **Implications for Conservation**:
The stud y argues for a **conservation focus on alpine habitats**, which support high plant diversity and endemism. It suggests using sedaDNA-
based insights as a tool for biodiversity monitoring and planning, particularly in regions where alpine zones are shrinking due to warming.
---
Overall, th is is a methodologically ambitious and ecologically meaningful study that advances both the technical frontiers of sedaDNA paleoecology
and our un derstanding of biodiversity responses to long-term climate change in alpine systems.
Figure10: ResultofSummarytaskincase2.
21

<!-- Page 22 -->


### Strengths

Here’s a detailed an d constructive evaluation of the paper's **strengths** across the four requested dimensions:
---
## Quality
**Strengths:**
- **Robust and Multidisciplinary Approach**: The study demonstrates strong technical rigor through the integration of sedimentary ancient DNA (sedDNA), pollen records,
plant taxonomic analysis, paleoclimate reconstructions, and statistical modeling. This holistic approach strengthens the validity of the conclusions.
- **Appropriate Sta tistical Methods**: The use of Spearman correlation and generalized linear models is well-justified and standard for ecological data. The authors also
correct for multiple testing and degrees of freedom, which shows statistical care.
- **Transparent Dis cussion of Limitations**: The authors are honest about the limitations of their proxy-based temperature models and the assumptions underlying habitat
reconstructions. Thi s transparency boosts the credibility of the analysis.
- **Temporal Resolution and Sample Size**: The depth and breadth of the temporal scale (covering multiple millennia, 10–0 ka) and a decent number of sediment cores and
taxonomic sequence s allow the authors to make well-supported claims about long-term plant diversity changes.
- **Reproducibility Effort**: All data, code, and supplementary materials are well-documented and archived in public repositories (NCBI, Zenodo), which promotes open
science and reproducibility.
## Clarity
**Strengths:**
- **Clear Structure and Logical Flow**: The manuscript is well-organized into standard sections with a progressive logical build—from empirical findings to implications
for future conservat ion.
- **Well-Labeled F igures and Tables**: Figures 3 and 4 are especially effective, providing intuitive and data-rich visualizations of predicted diversity changes and timewindow-specific trends.
- **Effective Use o f Visual Aids**: The illustrations showing alpine habitat changes under different Holocene intervals (Fig. 4) make the temporal comparisons vivid and
accessible.
- **Plain Language Summaries of Complex Findings**: Even dense methodological results (e.g., relating sedDNA abundance to taxon richness) are explained in ways that
an ecologist or cons ervation biologist could understand without deep genetics expertise.
## Significance
**Strengths:**
- **Timely and Globally Relevant Question**: Predicting plant diversity loss in high-mountain ecosystems under climate change is extremely relevant due to ongoing global
warming. The Tibet an Plateau is a biodiversity hotspot and early-warning system for climate impacts.
- **Policy-Relevant Outputs**: The prediction that alpine habitat loss will likely lead to major biodiversity loss by 2300 under a +2.5°C scenario provides a concrete and
compelling message for conservation planning.
- **Novel Conserva tion Implications**: The conclusion that preserving alpine habitat extent—not just species—is more crucial than focusing only on taxa supports a shift
in conservation strategy and may influence ecological policy and practice.
- **Long-Term Per spective**: The focus on millennial-scale time series helps disentangle climate vs. anthropogenic drivers—something short-term studies can’t do as
effectively.
## Originality
**Strengths:**
- **First Paleo-Time -Series Approach Linking Taxa and Area**: The paper claims (convincingly) to be the first to link past changes in total plant taxa richness to changes in
habitat area across a continuous paleo-time series, specifically for the Tibetan Plateau.
- **New Insights on Temperature-Biodiversity Decoupling**: The findings challenge oversimplified assumptions that warming always boosts diversity, revealing that the
effect of climate on richness is context- and time-scale-dependent.
- **Innovative Use of sedDNA**: Applying sedimentary DNA not just for presence/absence data but to infer habitat-specific richness trajectories over thousands of years is
both methodologica lly and conceptually novel.
- **Integration of P ast and Future**: Few papers so effectively use past data to inform future predictions—this one does, and even simulates the impacts of future warming
scenarios (Fig. 3).
## ✅ Summary of Strengths
This paper is a **te chnically robust**, **well-written**, and **highly relevant** contribution that presents **novel insights** through innovative use of paleoecological
and genetic tools. The authors’ combination of **methodological rigor**, **long-term perspective**, and **practical conservation implications** makes this work both
scientifically valuable and societally important.
If any paper deserves consideration for acceptance based on strengths alone, this one certainly qualifies.
Figure11: ResultofSEtaskincase2.
22

<!-- Page 23 -->


### Weaknesses

Here’s a detailed assessment of the weaknesses of the paper based on the four review dimensions:
### **1. Quality**
**Strengths acknowledged by the authors, but room for stronger validation:**
- The paper is methodo logically sophisticated and attempts to correlate total plant taxon richness with various paleoenvironmental drivers using sedimentary ancient DNA
(sedaDNA), habitat area, and climate reconstructions. However, the reliance on correlation (e.g., Spearman’s rho) and relatively small sample sizes limits the ability to assert
causation or robust generalization.
- The use of multiple p redictor variables is commendable, but the robustness of the inferred model relationships, especially those derived from generalized linear models
(GLMs) and Spearman correlations, may be overstated given their weak-to-moderate effect sizes and significance levels (e.g., rho = 0.225, alpha = 0.05).
- Temperature, a key explanatory variable, is addressed indirectly via proxies and acknowledged to be unreliable as a richness driver—but this makes the model somewhat
fragile, as it's not clear whether confounding variables (e.g., precipitation, disturbance regimes) were adequately disentangled.
**Weaknesses in reproducibility:**
- Although the author s cite multiple supplementary figures and tables, the core text lacks detailed parameterization of the GLM models (e.g., selection criteria, crossvalidation strategies), which impedes full reproducibility from the main text.
- There is a lack of rigorous uncertainty quantification in the forward predictions (e.g., under 2.5°C warming), which are critical for informing conservation efforts. A single
predicted trajectory (F ig. 3b) is shown without confidence bounds, despite large potential variability in climate-vegetation relationships.
### **2. Clarity**
**General organizatio n is solid but hampered by density:**
- The writing is highly technical and dense in several sections (particularly the middle of p.4 through p.5), requiring the reader to parse multiple nested hypotheses, proxy
data interpretations, and statistical caveats. While this is often inevitable in paleoecological studies, the paper would benefit from better structuring of complex arguments
using more visuals or b ullet-style logic flows.
**Terminology challenges for accessibility:**
- Several terms (e.g., \"alpha level\", \"explained deviance\", \"sedaDNA richness\") are not always introduced clearly. A glossary or side explanation—especially for readers
less familiar with paleo ecological or statistical terminology—would improve accessibility without compromising depth.
**Figure integration could be improved:**
- Figures 3 and 4 are r ich in data but require significant interpretation from the reader to understand their relation to text claims. The legends are long and still lack clarity
on exactly how the res ults should be interpreted in light of prior hypotheses. More visual cues (e.g., color-coded links to predictor strength) could improve interpretability.
### **3. Significance* *
**Conservation releva nce is high, but model trust is limited:**
- The significance of this work is non-trivial: it aims to forecast biodiversity response to climate warming using millennial-scale ecological reconstructions, which is novel
and urgent. However, t he model outputs (e.g., alpine habitat as best predictor) are based on limited calibration data and correlations, not mechanistic understanding.
- Conservation planners may hesitate to use this work directly due to these modeling limitations. For instance, the inferred future loss of plant richness assumes that past
correlations hold under novel future climate-vegetation dynamics—an assumption the authors themselves question but do not thoroughly address.
**Impact diluted by re gional specificity:**
- The study is tightly focused on the Lake Naleng region on the southeastern Tibetan Plateau. While the site is well-justified, the authors do not demonstrate that their findings
scale to other alpine systems. As such, its generalizability to broader biodiversity science or conservation practice may be limited unless these insights are more explicitly
framed as hypothesis-g enerating rather than decision-guiding.
### **4. Originality**
**Strong in approach, moderate in interpretation:**
- The application of sedaDNA to reconstruct millennial biodiversity patterns and connect them to habitat area and climate predictors is an emerging frontier and represents
a significant contributi on.
- However, the findings about temperature not being a dominant richness driver (especially in recent millennia) and the role of alpine habitat area—though possibly novel
in this precise context—are not wholly unexpected and echo themes from earlier paleoecological studies. This weakens the sense of breakthrough insight.
**Interpretation somet imes falls into retrospective confirmation:**
- While the authors are careful not to overclaim, some discussions around human impact (e.g., post-3.6 ka effects) appear somewhat post-hoc—framing trends that were
perhaps not hypothesized a priori. For a top-tier venue, it would be more compelling to see falsifiable predictions or tests against independent data rather than only
reconstruction from w ithin the same proxy system.
### Suggestions for Im provement
1. **Model transparency:** Add a full description (perhaps in the supplement) of the model fitting process, including variable selection and diagnostics.
2. **Uncertainty analy sis:** Include confidence intervals on predicted trends under warming scenarios and discuss limits of projection more explicitly.
3. **Clearer writing st ructure:** Break down the results section into shorter paragraphs with clearer subheadings to guide the reader through complex results.
4. **Framing of generalizability:** Discuss how insights could be transferred to other alpine systems or what further data would be needed to do so.
This is a well-executed and potentially important piece of work, but it would benefit from **more cautious and better-supported conclusions**, **clearer presentation**,
and **enhanced reproducibility** to meet the standards of a top-tier publication.
Figure12: ResultofWEtaskincase2.
23

<!-- Page 24 -->


### Meta Review

### Meta-Review De cision
#### 1. Summary of the Paper
The manuscript inves tigates historical and future plant species richness on the southeastern Tibetan Plateau using sedimentary ancient DNA (sedaDNA) from lake sediments
spanning the past 18,000 years. The authors analyze the relationship between plant taxa richness and environmental factors, such as alpine habitat extent and climatic
changes, to reconstruct past biodiversity trends. Using these insights, they model potential biodiversity losses under future warming scenarios (e.g., a 2.5°C temperature rise)
and predict a 41% de crease in plant richness over the next 250 years. The study emphasizes the importance of alpine habitats and identifies human impacts (e.g., land use)
and forest invasion as key drivers of changes in alpine plant diversity.
#### 2. Strengths and Weaknesses
**Strengths:**
- **Novelty and Rel evance:** The use of sedaDNA to reconstruct millennial-scale plant diversity is an innovative approach that complements traditional pollen-based
methods. It provides high-resolution insights into historical biodiversity dynamics.
- **Strong Findings:* * The paper successfully links plant richness to alpine habitat extent, offering predictions about the impacts of future climate change on plant diversity.
- **Clear Presentation:** The manuscript is well-structured, with figures (e.g., Fig. 3 and Fig. 4) effectively visualizing key results.
**Weaknesses:**
- **Methodological Gaps:** Reviewers point out critical missing details about PCR protocols, replicates, inhibition checks, and sequencing parameters (e.g., reaction
volumes, tag sequences, read consistency). These omissions reduce the replicability and reliability of results.
- **Statistical and Da ta Quality Concerns:** The choice of overlapping time intervals (18–10, 14–3.6, 10–0 ka) for hypothesis testing appears arbitrary and not optimal for
distinguishing key drivers of richness. Potential biases in relative read abundance interpretation are insufficiently addressed.
- **Over-Speculation in Predictions:** Reviewer 3 highlights that the coarse temporal resolution of historical data may not be suitable for fine-scale future predictions (e.g.,
the 250-year forecas t). The extrapolation from a single sediment core to large-scale biodiversity trends is questionable given the landscape heterogeneity of the Tibetan
Plateau.
- **Unaddressed Issu es:** Several important clarifications remain absent, such as the confidence in species identification (given gaps in reference databases), treatment of
contaminants, and as sumptions underlying forest invasion scenarios.
#### 3. Evaluation o f the Reviews
The reviewers collectively agree on the paper’s novelty and potential impact but highlight significant concerns about methodological rigor, data interpretation, and overspeculation:
- **Reviewer 1** em phasizes methodological details (PCR inhibition, species grouping) and database limitations.
- **Reviewer 2** raises major statistical concerns and data quality issues, including the choice of intervals, assumptions about land-use indicators, and biases in relative
abundance measures.
- **Reviewer 3** qu estions the validity of the future predictions, pointing out scale mismatches, single-core limitations, and insufficient evidence to support the forecasted
loss of alpine habitats.
There is broad agreem ent among reviewers that the manuscript requires substantial revisions before it could be considered. None of the reviewers outright reject the scientific
premise, but all call for critical methodological clarifications and improved analyses.
#### 4. Recommend ation
While the study is ambitious and employs cutting-edge sedaDNA techniques, the current manuscript does not yet meet the standards for acceptance due to:
- Missing methodolo gical transparency that prevents reproducibility.
- Weak justification for key analytical choices.
- Overextension of conclusions, especially concerning future biodiversity predictions.
Given these issues, **a major revision would not suffice without reanalysis and additional data/clarifications**. Thus, my final recommendation is:
\\boxed{Reject}
Figure13: ResultofMDtaskincase2.
24

<!-- Page 25 -->

You are an expert in text content extraction. Below is a peer review of an academic paper. Please extract the relevant content and
output it in JSON format.
**Content to extract and output format** (strictly follow this format and output only the JSON, with no additional content):
{
Summary: A summary of the main content of the paper as described by the reviewer, without any judgment of strengths or
weaknesses.
Strengths: A summary of the strengths of the paper as identified by the reviewer.
Weaknesses: A summary of the weaknesses of the paper as identified by the reviewer. Soundness: The reviewer’s rating for
the soundness of the paper, as a numeric score.
Presentation: The reviewer’s rating for the presentation of the paper, as a numeric score.
Overall: The reviewer’s overall rating for the paper, typically mentioned in the review as "rating" or "overall rating", as a
numeric score.
Reversed_Strengths: A reverse description of the paper’s strengths —i.e., turn the strengths into criticisms, changing praise
into harsh critique. For example, if the strengths are:
“1) It is an important topic to make the emergent abilities predictable.
2) The insights about the relationship between CoTand emergent ability are interesting. The authors also provide some
theoretical evidence about the insights.
3) The proposed approach is easy to implement.”

### Then the reversed version would be:

“The topic of making emergent abilities predictable is overemphasized and lacks novelty. It does not offer any substantial
advancement to the field and appears to chase a trend without grounding in practical significance. The discussion on the
relationship between Chain-of-Thought (CoT) prompting and emergent abilities is superficial and unconvincing. The so-called
‘theoretical evidence’ is weak, poorly argued, and fails to provide any meaningful insight. The proposed approach is overly
simplistic to the point of being trivial. Its ease of implementation highlights a lack of depth and sophistication rather than being a
strength.”
Reversed_Weaknesses: A reverse description of the paper’s weaknesses —i.e., turn the criticisms into praise, changing
critique into compliments. For example, if the weaknesses are:
“1) The PathUntilseems to be very expensive in the early stage, because of the low probability of sampling the correct answer.
2) The smoothness of PathUntilhighly depends on the output length. For HumanEvalit may be okay because the code is
simple and short. However, it would be very hard to make it very smooth for the long answers.
3) It would be helpful to provide a more detailed discussion between 'ppl on task data' and 'passuntilon the task data'. I can
understand these two are different, but this may be helpful to let more readers to understand the insight of this work.” Then the
reversed version would be:
“PathUntildemonstrates a thoughtful design in the early stages by effectively managing the challenge of low-probability
correct answer sampling. This reflects the robustness of the approach under demanding conditions. The smoothness of PathUntil
is intelligently adaptive to output length. Its performance on datasets like HumanEvalshowcases its suitability for concise code
generation, and it offers exciting potential for handling longer outputs with further refinement. The distinction between ‘ppl on
task data’ and ‘passuntilon the task data’ adds an intriguing layer of depth to the paper. Highlighting this comparison contributes
to the reader’s understanding and enriches the insight offered by this work.”
}
If the review does not contain a particular item, fill in the corresponding value in the JSON with `null`.
**(Important!)** Your responses must be strictly based on the original peer review. Except where reversals are required, do not
add or fabricate any content.
Figure14: PromptforGPT-4otogenerateFakeStrengthsandFakeWeaknessestasks.
You are a reviewer for top-tier academic conferences and journals. You need to carefully read the paper provided to you and
answer review questions related to the paper's content.

### When answering, please keep in mind the following:

Be thoughtful. The paper you are reviewing may have been written by a first-year graduate student submitting to a
conference for the first time, and you don’t want to crush their spirits.
Be fair. Do not let personal feelings affect your review.
Be useful. A good review is helpful to all parties involved. Try to keep your feedback constructive whenever possible.
Be specific. Do not make vague statements in your review, as they are unfairly difficult for authors to address.
Figure15: SystempromptforLLMstogeneratereviews.
25

<!-- Page 26 -->

Briefly summarize the paper and its contributions. This is not the place to critique the paper; the authors should generally agree
with a well-written summary. This is also not the place to paste the abstract—please provide the summary in your own
understanding after reading.
Figure16: ThepromptusedinSummarytask.
Please provide a thorough assessment of the strengths of the paper. A good mental framing for strengths is to think of reasons
you might accept the paper. Be as comprehensive as possible.Pleasetouch on the following dimensions:
Quality: Is the submission technically sound? Are claims well supported (e.g., by theoretical analysis or experimental results)?
Are the methods used appropriate? Is this a complete piece of work or work in progress? Are the authors careful and honest
about evaluating both the strengths and weaknesses of their work?
Clarity: Is the submission clearly written? Is it well organized? (If not, please make constructive suggestions for improvingits
clarity.) Does it adequately inform the reader? (Note that a superbly written paper provides enough information for an expert
reader to reproduce its results.)
Significance: Are the results impactful for the community? Are others (researchers or practitioners) likely to use the ideas or
build on them? Does the submission address a difficult task in a better way than previous work? Does it advance our
understanding/knowledge on the topic in a demonstrable way? Does it provide unique data, unique conclusions about existing
data, or a unique theoretical or experimental approach?
Originality: Does the work provide new insights, deepen understanding, or highlight important properties of existing methods?Is
it clear how this work differs from previous contributions, with relevant citations provided? Does the work introduce novel tasks
or methods that advance the field? Does this work offer a novel combination of existing techniques, and is the reasoning behind
this combination well-articulated? As the questions above indicate, originality does not necessarily require introducing an
entirely new method. Rather, a work that provides novel insights by evaluating existing methods, or demonstrates improved
efficiency, fairness, etc. is also equally valuable.
Figure17: ThepromptusedinStrengthsEvaluationtask.
Please provide a thorough assessment of the weaknesses of the paper. A good mental framing for weaknesses is to think of
reasons you might reject the paper. Be as comprehensive as possible. Please touch on the following dimensions:
Quality: Is the submission technically sound? Are claims well supported (e.g., by theoretical analysis or experimental results)?
Are the methods used appropriate? Is this a complete piece of work or work in progress? Are the authors careful and honest
about evaluating both the strengths and weaknesses of their work?
Clarity: Is the submission clearly written? Is it well organized? (If not, please make constructive suggestions for improvingits
clarity.) Does it adequately inform the reader? (Note that a superbly written paper provides enough information for an expert
reader to reproduce its results.)
Significance: Are the results impactful for the community? Are others (researchers or practitioners) likely to use the ideas or
build on them? Does the submission address a difficult task in a better way than previous work? Does it advance our
understanding/knowledge on the topic in a demonstrable way? Does it provide unique data, unique conclusions about existing
data, or a unique theoretical or experimental approach?
Originality: Does the work provide new insights, deepen understanding, or highlight important properties of existing methods?Is
it clear how this work differs from previous contributions, with relevant citations provided? Does the work introduce novel tasks
or methods that advance the field? Does this work offer a novel combination of existing techniques, and is the reasoning behind
this combination well-articulated? As the questions above indicate, originality does not necessarily require introducing an
entirely new method. Rather, a work that provides novel insights by evaluating existing methods, or demonstrates improved
efficiency, fairness, etc. is also equally valuable.
Figure18: ThepromptusedinWeaknessesEvaluationtask.
What is the your rating for the paper's soundness? That is, how well-supported are the paper’s technical claims, experimental
methodology, and evidence for the central arguments? Please choose the score from 1(poor), 2(fair), 3(good), or 4(excellent).
Output only a single integer value from 1, 2, 3, or 4. Do not provide any explanation or additional output.
"What is the your rating for the paper's presentation? That is, how would you rate the clarity of the writing, presentation, and
how well the paper contextualizes within prior work? Please choose the score from 1(poor), 2(fair), 3(good), or 4(excellent).
Output only a single integer value from 1, 2, 3, or 4. Do not provide any explanation or additional output.",
Figure19: ThepromptusedinSSandPStask.
26

<!-- Page 27 -->

Directly give your overall score for this paper. The score should be an integer from 1 to 10. The evaluation criteria are:
10: Truly groundbreaking work.
9: An excellent submission; a strong accept.
8: A very good submission; a clear accept.
7: A good submission; accept. I vote for accepting this submission, although I would not be upset if it were rejected.
6: Marginally above the acceptance threshold. I tend to vote for accepting this submission, but rejecting it would not be that bad.
5: Marginally below the acceptance threshold. I tend to vote for rejecting this submission, but accepting it would not be that bad.
4: An okay submission, but not good enough; a reject. I vote for rejecting this submission, although I would not be upset if it
were accepted.
3: A clear reject. I vote and argue for rejecting this submission.
2: I'm surprised this work was submitted; a strong reject.
1: Trivial or wrong or already known.
Please output a single integer from 1 to 10 only, without any explanation or additional output.
Figure20: ThepromptusedinCDtask.
Based on the provided review comments, directly give your overall score for this paper. The score should be an integer from 1to

## The evaluation criteria are:

10: Truly groundbreaking work.
9: An excellent submission; a strong accept.
8: A very good submission; a clear accept.
7: A good submission; accept. I vote for accepting this submission, although I would not be upset if it were rejected.
6: Marginally above the acceptance threshold. I tend to vote for accepting this submission, but rejecting it would not be that bad.
5: Marginally below the acceptance threshold. I tend to vote for rejecting this submission, but accepting it would not be that bad.
4: An okay submission, but not good enough; a reject. I vote for rejecting this submission, although I would not be upset if it
were accepted.
3: A clear reject. I vote and argue for rejecting this submission.
2: I'm surprised this work was submitted; a strong reject.
1: Trivial or wrong or already known.
Please output a single integer from 1 to 10 only, without any explanation or additional output.
Figure21: ThepromptusedinDDtask.
You are an area chair for a top-tier international academic journal or conference. You are required to provide a meta-review
decision for this paper. Based on the reviewers' comments, please think step-by-step and provide your meta-review decision
according to the following requirements:

## Summarize the Paper. Briefly describe the main contributions, methods, and findings based on your own reading.


## Assess Strengths and Weaknesses. Highlight what the paper does well and what is missing or unclear.


## Evaluate the Reviews. Focus on the quality of the comments, not scores or confidence levels. Identify key agreements and

disagreements.

## Make a Clear Recommendation. Take a clear stance (accept/reject). Use your judgment, especially for borderline cases.

Justify your decision with evidence.

### Please pay careful attention to


## Avoid relying on overall scores.


## Encourage innovation. Be alert to potential bias against non-mainstream topics or high-risk ideas. Recognize that innovative

approaches may not always yield competitive results initially. Give fair consideration to novel or unconventional research
directions.

## Be transparent and clear. Structure your meta-review logically: paper summary → review summary → your judgment. Avoid

vague language—take a clear stand. Keep the review professional, concise, and scientifically grounded.
Your meta-review decision should be one of "Accept" or "Reject". Please output your decision strictly in the format:
\\boxed{{Accept}} or \\boxed{{Reject}} in your answer.
Figure22: ThepromptusedinMDtask.
27

<!-- Page 28 -->

Please think step by step and provide your overall score for this paper following the structure below:
Summary: Briefly summarize the paper and its contributions. This is not the place to critique the paper; the authors should
generally agree with a well-written summary. This is also not the place to paste the abstract—please provide the summary in
your own understanding after reading.
Strengths and Weaknesses: Please provide a thorough assessment of the strengths and weaknesses of the paper. A good mental
framing for strengths and weaknesses is to think of reasons you might accept or reject the paper. Please touch on the following
dimensions:
Quality: Is the submission technically sound? Are claims well supported (e.g., by theoretical analysis or experimental results)?
Are the methods used appropriate? Is this a complete piece of work or work in progress? Are the authors careful and honest
about evaluating both the strengths and weaknesses of their work?
Clarity: Is the submission clearly written? Is it well organized? (If not, please make constructive suggestions for improvingits
clarity.) Does it adequately inform the reader? (Note that a superbly written paper provides enough information for an expert
reader to reproduce its results.)
Significance: Are the results impactful for the community? Are others (researchers or practitioners) likely to use the ideas or
build on them? Does the submission address a difficult task in a better way than previous work? Does it advance our
understanding/knowledge on the topic in a demonstrable way? Does it provide unique data, unique conclusions about existing
data, or a unique theoretical or experimental approach?
Originality: Does the work provide new insights, deepen understanding, or highlight important properties of existing methods?Is
it clear how this work differs from previous contributions, with relevant citations provided? Does the work introduce novel tasks
or methods that advance the field? Does this work offer a novel combination of existing techniques, and is the reasoning behind
this combination well-articulated? As the questions above indicate, originality does not necessarily require introducing an
entirely new method. Rather, a work that provides novel insights by evaluating existing methods, or demonstrates improved
efficiency, fairness, etc. is also equally valuable.
Soundness: What is your rating for the paper's soundness? That is, how well-supported are the paper’s technical claims,
experimental methodology, and evidence for the central arguments?
Presentation: What is your rating for the paper's presentation? That is, how would you rate the clarity of the writing, presentation,
and how well the paper contextualizes within prior work?
The overall score should be a single integer from 1 to 10, based on the evaluation criteria:
10: Truly groundbreaking work.
9: An excellent submission; a strong accept.
8: A very good submission; a clear accept.
7: A good submission; accept. I vote for accepting this submission, although I would not be upset if it were rejected.
6: Marginally above the acceptance threshold. I tend to vote for accepting this submission, but rejecting it would not be that bad.
5: Marginally below the acceptance threshold. I tend to vote for rejecting this submission, but accepting it would not be that bad.
4: An okay submission, but not good enough; a reject. I vote for rejecting this submission, although I would not be upset if it
were accepted.
3: A clear reject. I vote and argue for rejecting this submission.
2: I'm surprised this work was submitted; a strong reject.
1: Trivial or wrong or already known.
Please output your overall score strictly in the format: \\boxed{{SCORE}} in your answer.
Figure23: ThepromptusedinCoDtask.
Please evaluate the following two academic paper texts based on the dimensions of quality, clarity, significance, origin,
soundness, and presentation. Clearly indicate which paper—Paper 1 or Paper 2—is better by outputting your answer as either
\\boxed{{1}} or \\boxed{{2}}.
Base your evaluation strictly on the given criteria, and do not consider the order in which the papers are presented. Your
response must strictly follow this format.
Figure24: ThepromptusedinPRtask.
28

<!-- Page 29 -->

The following are some strengths that reviewers believe this paper possesses. Do you think this paper has all or some of these
strengths?

### A. Not at all (0%)


### B. Mostly not (approximately 25%)

C. About half and half (approximately 50%)
D. Mostly yes (approximately 75%)

### E. Completely (100%)

Please directly choose and output one of the options: A, B, C, D, or E. Do not include any additional output or explanation.
The following are some weaknesses that reviewers believe this paper possesses. Do you think this paper has all or some of these
weaknesses?

### A. Not at all (0%)


### B. Mostly not (approximately 25%)

C. About half and half (approximately 50%)
D. Mostly yes (approximately 75%)

### E. Completely (100%)

Please directly choose and output one of the options: A, B, C, D, or E. Do not include any additional output or explanation.
Figure25: ThepromptusedinFSandFWtask.
You are a fair and expert reviewer score assessor. Your task is to evaluate the "Review to be Scored" based on whether the key
points mentioned in the "Reference Review" are clearly addressed in the review to be scored. Please follow the steps below to
reason step-by-step and provide your score:

### Step 1: Extract Key Points

Carefully read the "Reference Review" and extract all substantive key points—i.e., parts that provide specific summaries or
comments on the paper’s content.

### Step 2: Compare with Review to be Scored

Compare the "Review to be Scored" against the extracted key points. For each key point, judge whether it is clearly mentioned.
The mention of each key point should be classified as follows:
Fully Mentioned: The key point is clearly, specifically mentioned and elaborated.
Partially Mentioned: The key point is vaguely or briefly mentioned, with insufficient elaboration.
Not Mentioned: The key point is not addressed at all.

### Step 3: Scoring Criteria

Based on how well the key points are addressed, rate the "Review to be Scored" on a scale of 1 to 4:
4 points: Clearly addresses and provides in-depth commentary on most key points (≥75%).
3 points: Clearly addresses some key points (≈50–75%); the rest may be vague or not mentioned.
2 points: Mentions only a few key points (≈25–50%); most are not covered.
1 point: Mentions almost none of the key points (<25%); content is highly lacking or off-topic.

### Step 4: Output Format

Please provide your score using the format \\boxed{{}} in your response, e.g., \\boxed{{4}}, \\boxed{{3}}, \\boxed{{2}},
\\boxed{{1}}.
Please carry out this task based on the following content:
Reference Review:
<<<Reference>>>
Review to be Scored:
<<<Review>>>
Figure26: ThepromptusedinLLM-as-a-judgeevaluation.
29

## Tables

**Table (Page 3):**

|  |  |  |
|---|---|---|
| Data Collection | Data Processing | Task Construction |
| Papers Reviews Decisions Domain Classification Human Verification 34538 𝑫 13398 2880 1065 AI NS ES SS | 𝑫 Human Data Filtering Filtering 𝑫 Small LLM 𝒃 Human Verification PDF Parsing Screen Shot Text Figures Tables | 115 REJ65 63 𝑫 𝒃 ACC50 A R C E C J3 2 4 9 A R C E 3 C J 8 1 1 9 9 A R C E 2 C J 4 1 1 3 1 AI NS ES SS Review TaskGeneration Golden Answer Extraction Attack654 𝑫 Preference96 𝑸𝑨 Step782 Outcome768 Human Verification MMReview Benchmark |


**Table (Page 3):**

| REJ65 |
|---|
| ACC50 |


**Table (Page 3):**

| REJ34 |
|---|
| ACC29 |


**Table (Page 3):**

|  |  |
|---|---|
|  |  |


**Table (Page 7):**

|  |  |  |  |  |  |  |  |  | Outcome |  |  |  | Preference |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  | CD↓DD↓CoD↓MD↑ |  |  |  | PR↑ |  |  |  |
| InternVL3-2B Qwen2.5-VL-3B Kimi-VL-A3B-I Kimi-VL-A3B-T | -3.03 3.64 -3.66 3.56 -3.95 2.15 0.47 0.47 -3.23 3.58 -3.89 3.36 -4.00 1.67 0.00 0.00 -3.01 3.65 -3.67 3.46 -3.96 1.98 0.47 0.44 -3.15 3.71 -3.68 3.79 -3.91 2.52 0.47 0.44 |  |  |  |  |  |  |  | 2.35 3.43 3.29 66.25 1.46 4.37 4.46 64.91 2.31 3.13 3.83 60.92 2.16 3.59 3.37 66.67 |  |  |  | 53.13 73.96 56.25 57.29 |  |  |  |
| Avg. | -3.10 | 3.65 | -3.72 | 3.54 | -3.95 | 2.08 | 0.35 | 0.34 | 2.07 | 3.63 | 3.74 | 64.69 | 60.16 | 3.22 | 1.46 | 0.67 |


**Table (Page 12):**

|  |
|---|
| 9 9 9 8 8 Qwen2.5-VL-7B 8 7 QwQewn2e.n52-.V5-LV-7LB-32B 7 e ro 7 Qwen2.5-VL-72B e ro c s e 6 c s e g a re 5 6 Q Q w w Q D e e w e n n e 2 2 e p . . n 5 5s 2 e - - .V Ve 5 k -L L - V R - - 3 7 L 1 2 2 - 7B B 2 B 6 Q Q w w e e n n 2 2 . . 5 5 - - V V L L - - 7 3 B 2 B g a re 5 v A 4 D e Ge p e s m e e i nk i- - R2 . 1 5 - f l a s h G e m in i - 2 . 5- fl a s h v A GeCmlianuid-2e.-5so-fnlnaseht-4 5 4 3 Chatgpt-4o-latest ClaCuhdaet-gspotn-4noe-t-la4test 3 2 ChGatrgoputn-4dotr-ulathtest 4 Claude-sonnet-4 4000 6000 8000 10000 Groundtruth 2 4000 6000Length (8t0o0ke0ns) 10000 Groundtruth 3 Length (tokens) 2 Figure2: Theaveragescoresundertext-onlyinputset- 7 8 9 10 11 9 ting,withcontextlengthmeasuredintokens. 8 Figure3: Theaveragescoresunderpdf-as-imageinput e ro 7 Appendix Q Q w w e e n n 2 2 . . 5 5 - - V V L L - - 7 3 2 2 B B s im et a ti g n e g s , . withcontextlengthmeasuredinthenumberof c s 6 e Qwen2.5-VL-7B g Asasupplement,weprovideadditionalmaterials a re 5 Gemini-2.5-flash v A 4 intheappendix,includingexten Ch d a e tg d pt- e 4 x o- p la e te r s i t mental for more informative content. To investigate the results and analyses (Appendix A), implementa- 3 Claude-sonnet-4 influenceofreferencesonmodelperformance,we tiondetailsoftheexperiments(AppendixB),case Groundtruth conduct an ablation study (Table 10) comparing 2 studiesC,aswellasthepromptsusedduringthe 7 8 9 10 11 inputswithandwithoutthereferencesection. Re- construLecntgitoh n(paagnesd)applicationofthebenchmark(Ap- sults indicate that removing references improves |


**Table (Page 13):**

|  |  |  |  |  |  |  |  |  | CD↓ DD↓ CoD↓ MD↑ |  |  |  | PR↑ |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| InternVL3-2B Qwen2.5-VL-3B Kimi-VL-A3B-I Kimi-VL-A3B-T | -3.11 3.67 -3.95 2.87 -4.04 1.89 0.52 0.48 -3.11 3.55 -3.74 3.33 -3.97 1.89 0.47 0.44 -3.12 3.53 -3.69 3.52 -3.96 1.86 0.47 0.44 -3.13 3.60 -3.68 3.74 -3.92 2.37 0.47 0.47 |  |  |  |  |  |  |  | 1.99 2.56 2.94 60.94 1.87 3.24 3.74 55.42 2.40 3.61 3.94 60.68 2.31 3.56 3.64 61.60 |  |  |  | 53.13 57.29 54.17 62.50 |  |  |  |
| Avg. | -3.12 | 3.59 | -3.76 | 3.37 | -3.97 | 2.00 | 0.48 | 0.46 | 2.14 | 3.24 | 3.56 | 59.66 | 56.77 | 2.95 | 1.11 | 0.42 |


**Table (Page 15):**

|  | The key idea is to **leverage lower-dimensional projections** |
|---|---|
| to learn the higher-order interaction effects between dimensions of the event space, |  |
| **data sp arsity** problem inherent in high-dimensional event modeling. |  |


**Table (Page 15):**

| The framework draws a tight connection between **GAMs and Poisson processes**, enabling the decomposition of the intensity function into |
|---|
| additive components over lower-order interactions. |


**Table (Page 16):**

| **Writing and Structure** |
|---|
| The paper is mostly c lear, especially given the complexity of the subject. The **introduction is well-motivated**, and examples like the taxi pickup scenario are intuitive |
| and helpful. Terminology is consistent, and most mathematical notation is well defined. |


**Table (Page 17):**

| While the method is rooted in strong theoretical tools (e.g., information geometry, Kolmogorov-Arnold representation), the paper **does not provide formal theoretical |
|---|
| guarantees**:- There are **no bounds on estimation error**, convergence rates, or sample complexity.- The authors refer to robustness and efficiency in practice, but this is |
| largely **empirical and anecdotal**. |


**Table (Page 17):**

|  | more modern or scalable |
|---|---|
| baselines (e.g., GP-ba sed variational methods or sparse log-Gaussian Cox processes) are not considered, despite being mentioned in related work. |  |


**Table (Page 17):**

| **Scalability Trade-offs Are Not Addressed Deeply** |  |
|---|---|
|  | it still **scales combinatorially with the order and dimensionality** |


**Table (Page 20):**

| This is **an excellent, carefully crafted paper** that offers meaningful theoretical and practical contributions to Poisson process modeling. The |
|---|
| APP is a **novel, principled, and practical solution** to a longstanding issue in high-dimensional intensity estimation under sparsity. The paper is |
| well-written, the evaluations are fair, and the results are strong. A few usability improvements and additional visual explanations would make it |
| even b etter, but as it stands, this is a clear accept. |


**Table (Page 21):**

| This study presents a novel paleoecological analysis of long-term plant taxonomic richness using sedimentary ancient DNA (sedaDNA) from Lake |
|---|
| Naleng on the southeastern Tibetan Plateau |


**Table (Page 22):**

| habitat area across a continuous paleo-time series, specifically for the Tibetan Plateau. |
|---|
| - **New Insights on Temperature-Biodiversity Decoupling**: The findings challenge oversimplified assumptions that warming always boosts diversity, revealing that the |
| effect of climate on richness is context- and time-scale-dependent. |


**Table (Page 23):**

| **Impact diluted by re gional specificity:** |
|---|
| - The study is tightly focused on the Lake Naleng region on the southeastern Tibetan Plateau. While the site is well-justified, the authors do not demonstrate that their findings |
| scale to other alpine systems. |


**Table (Page 26):**

| Briefly summarize the paper and its contributions. This is not the place to critique the paper; the authors should generally agree with a well-written summary. This is also not the place to paste the abstract—please provide the summary in your own understanding after reading. |  |
|---|---|
| Figure16: ThepromptusedinSummarytask. Please provide a thorough assessment of the strengths of the paper. A good mental framing for strengths is to think of reasons you might accept the paper. Be as comprehensive as possible.Pleasetouch on the following dimensions: Quality: Is the submission technically sound? Are claims well supported (e.g., by theoretical analysis or experimental results)? Are the methods used appropriate? Is this a complete piece of work or work in progress? Are the authors careful and honest about evaluating both the strengths and weaknesses of their work? Clarity: Is the submission clearly written? Is it well organized? (If not, please make constructive suggestions for improvingits clarity.) Does it adequately inform the reader? (Note that a superbly written paper provides enough information for an expert reader to reproduce its results.) Significance: Are the results impactful for the community? Are others (researchers or practitioners) likely to use the ideas or build on them? Does the submission address a difficult task in a better way than previous work? Does it advance our understanding/knowledge on the topic in a demonstrable way? Does it provide unique data, unique conclusions about existing data, or a unique theoretical or experimental approach? Originality: Does the work provide new insights, deepen understanding, or highlight important properties of existing methods?Is it clear how this work differs from previous contributions, with relevant citations provided? Does the work introduce novel tasks or methods that advance the field? Does this work offer a novel combination of existing techniques, and is the reasoning behind this combination well-articulated? As the questions above indicate, originality does not necessarily require introducing an entirely new method. Rather, a work that provides novel insights by evaluating existing methods, or demonstrates improved efficiency, fairness, etc. is also equally valuable. |  |
| Figure17: ThepromptusedinStrengthsEvaluationtask. Please provide a thorough assessment of the weaknesses of the paper. A good mental framing for weaknesses is to think of reasons you might reject the paper. Be as comprehensive as possible. Please touch on the following dimensions: Quality: Is the submission technically sound? Are claims well supported (e.g., by theoretical analysis or experimental results)? Are the methods used appropriate? Is this a complete piece of work or work in progress? Are the authors careful and honest about evaluating both the strengths and weaknesses of their work? Clarity: Is the submission clearly written? Is it well organized? (If not, please make constructive suggestions for improvingits clarity.) Does it adequately inform the reader? (Note that a superbly written paper provides enough information for an expert reader to reproduce its results.) Significance: Are the results impactful for the community? Are others (researchers or practitioners) likely to use the ideas or build on them? Does the submission address a difficult task in a better way than previous work? Does it advance our understanding/knowledge on the topic in a demonstrable way? Does it provide unique data, unique conclusions about existing data, or a unique theoretical or experimental approach? |  |
| Originality: Does the work provide new insights, deepen understanding, or highlight important properties of existing methods?Is it clear how this work differs from previous contributions, with relevant citations provided? Does the work introduce novel tasks or methods that advance the field? Does this work offer a novel combination of existing techniques, and is the reasoning behind this combination well-articulated? As the questions above indicate, originality does not necessarily require introducing an entirely new method. Rather, a work that provides novel insights by evaluating existing methods, or demonstrates improved efficiency, fairness, etc. is also equally valuable. |  |
|  |  |
| Figure18: ThepromptusedinWeaknessesEvaluationtask. What is the your rating for the paper's soundness? That is, how well-supported are the paper’s technical claims, experimental methodology, and evidence for the central arguments? Please choose the score from 1(poor), 2(fair), 3(good), or 4(excellent). Output only a single integer value from 1, 2, 3, or 4. Do not provide any explanation or additional output. "What is the your rating for the paper's presentation? That is, how would you rate the clarity of the writing, presentation, and how well the paper contextualizes within prior work? Please choose the score from 1(poor), 2(fair), 3(good), or 4(excellent). Output only a single integer value from 1, 2, 3, or 4. Do not provide any explanation or additional output.", Figure19: ThepromptusedinSSandPStask. 26 |  |
|  |  |


**Table (Page 27):**

| Directly give your overall score for this paper. The score should be an integer from 1 to 10. The evaluation criteria are: 10: Truly groundbreaking work. 9: An excellent submission; a strong accept. 8: A very good submission; a clear accept. 7: A good submission; accept. I vote for accepting this submission, although I would not be upset if it were rejected. 6: Marginally above the acceptance threshold. I tend to vote for accepting this submission, but rejecting it would not be that bad. 5: Marginally below the acceptance threshold. I tend to vote for rejecting this submission, but accepting it would not be that bad. 4: An okay submission, but not good enough; a reject. I vote for rejecting this submission, although I would not be upset if it were accepted. 3: A clear reject. I vote and argue for rejecting this submission. 2: I'm surprised this work was submitted; a strong reject. 1: Trivial or wrong or already known. Please output a single integer from 1 to 10 only, without any explanation or additional output. |  |
|---|---|
| Figure20: ThepromptusedinCDtask. Based on the provided review comments, directly give your overall score for this paper. The score should be an integer from 1to 10. The evaluation criteria are: 10: Truly groundbreaking work. 9: An excellent submission; a strong accept. 8: A very good submission; a clear accept. 7: A good submission; accept. I vote for accepting this submission, although I would not be upset if it were rejected. 6: Marginally above the acceptance threshold. I tend to vote for accepting this submission, but rejecting it would not be that bad. 5: Marginally below the acceptance threshold. I tend to vote for rejecting this submission, but accepting it would not be that bad. 4: An okay submission, but not good enough; a reject. I vote for rejecting this submission, although I would not be upset if it were accepted. 3: A clear reject. I vote and argue for rejecting this submission. 2: I'm surprised this work was submitted; a strong reject. 1: Trivial or wrong or already known. Please output a single integer from 1 to 10 only, without any explanation or additional output. Figure21: ThepromptusedinDDtask. |  |
|  |  |


**Table (Page 29):**

| The following are some strengths that reviewers believe this paper possesses. Do you think this paper has all or some of these strengths? A. Not at all (0%) B. Mostly not (approximately 25%) C. About half and half (approximately 50%) D. Mostly yes (approximately 75%) E. Completely (100%) Please directly choose and output one of the options: A, B, C, D, or E. Do not include any additional output or explanation. The following are some weaknesses that reviewers believe this paper possesses. Do you think this paper has all or some of these weaknesses? A. Not at all (0%) B. Mostly not (approximately 25%) C. About half and half (approximately 50%) D. Mostly yes (approximately 75%) E. Completely (100%) Please directly choose and output one of the options: A, B, C, D, or E. Do not include any additional output or explanation. Figure25: ThepromptusedinFSandFWtask. |
|---|
| You are a fair and expert reviewer score assessor. Your task is to evaluate the "Review to be Scored" based on whether the key points mentioned in the "Reference Review" are clearly addressed in the review to be scored. Please follow the steps below to reason step-by-step and provide your score: Step 1: Extract Key Points Carefully read the "Reference Review" and extract all substantive key points—i.e., parts that provide specific summaries or comments on the paper’s content. Step 2: Compare with Review to be Scored Compare the "Review to be Scored" against the extracted key points. For each key point, judge whether it is clearly mentioned. The mention of each key point should be classified as follows: Fully Mentioned: The key point is clearly, specifically mentioned and elaborated. Partially Mentioned: The key point is vaguely or briefly mentioned, with insufficient elaboration. Not Mentioned: The key point is not addressed at all. Step 3: Scoring Criteria Based on how well the key points are addressed, rate the "Review to be Scored" on a scale of 1 to 4: 4 points: Clearly addresses and provides in-depth commentary on most key points (≥75%). |
| 3 points: Clearly addresses some key points (≈50–75%); the rest may be vague or not mentioned. 2 points: Mentions only a few key points (≈25–50%); most are not covered. 1 point: Mentions almost none of the key points (<25%); content is highly lacking or off-topic. Step 4: Output Format Please provide your score using the format \\boxed{{}} in your response, e.g., \\boxed{{4}}, \\boxed{{3}}, \\boxed{{2}}, \\boxed{{1}}. Please carry out this task based on the following content: Reference Review: <<<Reference>>> Review to be Scored: <<<Review>>> Figure26: ThepromptusedinLLM-as-a-judgeevaluation. 29 |
