---
title: "KD LoRA Hybrid Approach"
original_file: "./KD_LoRA_Hybrid_Approach.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["llm", "rag", "fine-tuning", "evaluation", "multimodal"]
keywords: ["lora", "urlhttps", "org", "arxiv", "abs", "fft", "base", "doi", "openreview", "net"]
summary: "<!-- Page 1 -->


### KD-LoRA: A Hybrid Approach to Efficient


### Fine-Tuning with LoRA and Knowledge Distillation

RambodAzimi1 RishavRishav1,3 MarekTeichmann2 SamiraEbrahimiKahou1,3,4

### Abstract

Largelanguagemodels(LLMs)havedemonstratedremarkableperformanceacross
variousdownstreamtasks. However,thehighcomputationalandmemoryrequirementsofLLMsareamajorbottleneck. Toaddressthis,parameter-efficientfinetuning(PEFT)methodssuchaslow-rankadaptation(LoRA)havebeenproposedto
reducecomputationalcost"
related_documents: []
---

# KD LoRA Hybrid Approach

<!-- Page 1 -->


### KD-LoRA: A Hybrid Approach to Efficient


### Fine-Tuning with LoRA and Knowledge Distillation

RambodAzimi1 RishavRishav1,3 MarekTeichmann2 SamiraEbrahimiKahou1,3,4

### Abstract

Largelanguagemodels(LLMs)havedemonstratedremarkableperformanceacross
variousdownstreamtasks. However,thehighcomputationalandmemoryrequirementsofLLMsareamajorbottleneck. Toaddressthis,parameter-efficientfinetuning(PEFT)methodssuchaslow-rankadaptation(LoRA)havebeenproposedto
reducecomputationalcostswhileensuringminimallossinperformance. Additionally,knowledgedistillation(KD)hasbeenapopularchoiceforobtainingcompact
studentmodelsfromteachermodels. Inthiswork,wepresentKD-LoRA,anovel
fine-tuningmethodthatcombinesLoRAwithKD.Ourresultsdemonstratethat
KD-LoRAachievesperformancecomparabletofullfine-tuning(FFT)andLoRA
whilesignificantlyreducingresourcerequirements. Specifically,KD-LoRAretains
98%ofLoRA’sperformanceontheGLUEbenchmark,whilebeing40%morecompact. Additionally,KD-LoRAreducesGPUmemoryusageby30%comparedto
LoRA,whiledecreasinginferencetimeby30%comparedtobothFFTandLoRA.
WeevaluateKD-LoRAacrossthreeencoder-onlymodels: BERT,RoBERTa,and
DeBERTaV3. Codeisavailableathttps://github.com/rambodazimi/KD-LoRA.
1 Introduction
Withadvancementsintransformer(Vaswanietal.,2017)architecturesandhardwarecapabilities,
includingGPUsanddistributedtraining,researchershavebeenabletodevelopLLMswithbillions
ofparameters(Lietal.,2020;Narayananetal.,2021;Dashetal.,2023),suchasLLaMA3.1(Dubey
etal.,2024)whichboastsupto405billionparameters. Thesemodels,trainedontrillionsoftokens,
exhibitremarkablecapabilitiesacrossvariousdownstreamtasks(Brownetal.,2020;Zhuangetal.,
2021;Weietal.,2022). However,fine-tuningthesemodelsrequiressubstantialenergyandmemory
demands(Samsietal.,2023). Furthermore,inrecentyears,thegrowthinthenumberofparameters
inLLMshassignificantlyoutpacedtheadvancementsinavailableGPUmemory(Lialinetal.,2023),
amplifyingthechallengesofmanagingmemoryduringfine-tuning(Singhetal.,2024;Kimetal.,
2024;Dongetal.,2024).
To address these challenges, PEFT techniques (Houlsby et al., 2019) have emerged as effective
solutions,whichfine-tuneasmallsubsetofparameterswhilekeepingthemajorityfixed. Asshown
inFigure1, onepopularPEFTtechnique, LoRA(Huetal.,2022), anditsvariants(Zhangetal.,
2023a; Zi et al., 2024; Ren et al., 2024; Zhao et al., 2024a; Liu et al., 2024) reduce the number
oftrainableparametersbyintroducingsmall,trainablerankdecompositionmatrices,maintaining
performance as FFT across many tasks (Dettmers et al., 2023). For example, DoRA (Liu et al.,
2024)enhancesLoRAbydecomposingpre-trainedweightsintomagnitudeanddirection,applying
LoRAtodirectionalupdatesforreducedtrainableparameters. Similarly,AdaLoRA(Zhangetal.,
2023a)improvesLoRAbydynamicallyallocatingparametersbasedontheirimportance,optimizing
efficiencyandperformance,particularlyundertightbudgetconstraints.
1Mila–QuebecAIInstitute,2CMLabsSimulationsInc,3UniversityofCalgary,4CanadaCIFARAIChair
4thNeurIPSEfficientNaturalLanguageandSpeechProcessingWorkshop(ENLSP-IV2024).
4202
tcO
82
]LC.sc[
1v77702.0142:viXra

<!-- Page 2 -->

However,theeffectivenessofPEFTmethodsvariesacrossLLMsbasedonseveralfactorssuchas
modelarchitectureandtasktype(Puetal.,2023;Leeetal.,2023). Additionally,LoRAstillrequires
substantialmemory,asitdoesnotreducetheactivationmemorycostcomparedtoFFT(Chenetal.,
2016; Zhang et al., 2023b; Zhao et al., 2024b). For example, a GPT-like model with 1.5 billion
parameters,asequencelengthof1K,andabatchsizeof32requiresapproximately60GBofGPU
memory(Rajbhandarietal.,2020). Moreover,LoRAdoesnotimproveinferencetime,asthefull
modelstillneedstobeprocessedduringinference(Liaoetal.,2023;Guetal.,2024a).
KD(Hintonetal.,2015)hasbecomeanotherprominentwaytomakethetrainingandinferenceless
memory-intensivebytransferringcapabilitiesoflargerteachermodels,suchasGPT-4(OpenAIetal.,
2024),Gemini(Aniletal.,2024),andLLaMA(Dubeyetal.,2024)tosmallerstudentmodelswithout
greatlycompromisingperformance(Guetal.,2024b;Xuetal.,2024).
KDhasforinstancebeenusedtodistilltheBERTmodelintoTinyBERT(Jiaoetal.,2020)thathas
only14.5millionparameterswithoutsignificantperformanceloss. Theperformanceofthedistilled
11BparameterT5model(Hsiehetal.,2023)hasbeenshowntoevensurpassthatofthemuchlarger
540BparameterPaLMteachermodel.
Inthispaper,weintroduceKD-LoRA,anovelfine-tuningmethodthatintegratesLoRAintotheKD
frameworktoachievecompetitiveperformancewithreducedcomputationalcosts,makingitidealfor
deploymentinresource-limitedenvironments. WeaccomplishthisbyincorporatingLoRAmatrices
intothestudentmodelandthenapplyingthedistillationprocesswhileupdatingtheLoRAmatrices
ofthestudentmodel. BycombiningKDwithLoRA,weleveragethestrengthsofbothmethods:
LoRA’sefficiencyinreducingtrainableparametersandKD’sabilitytoeffectivelytransferknowledge
tomorecompactstudentmodels,resultinginreducedmodelsizeandshorterinferencetime.
WeevaluatetheeffectivenessofKD-LoRAincomparisontoFFTandLoRAacrossthreeencoderonlyLLMs: BERT(Devlinetal.,2019), RoBERTa(Zhuangetal.,2021), andDeBERTaV3(He
etal.,2023). FortheKDcomponent,weselectasmallerstudentmodelfromthesamefamilyfor
eachLLM.ForeachGLUEbenchmarktask(Wangetal.,2019),weexplorevarioushyperparameter
configurations and PEFT settings, utilizing NVIDIA A100 GPUs. The median performance is
reportedbasedonthetop6configurations. OurcomprehensiveexperimentsontheGLUEbenchmark
revealthatKD-LoRAoffersseveraladvantages:
• KD-LoRAachievesabout97%ofFFT’sperformancewhileupdatingsignificantlyfewer
parameters. Forinstance,FFTfine-tunesall110MparametersoftheBERT-basemodel,
whereasKD-LoRAfine-tunesonly1.2Mparameterswitharankof8.
• KD-LoRA achieves about 98% of LoRA’s performance while incorporating knowledge
fromalargerteachermodelandusingfewertrainableparametersduetothemorecompact
studentmodel.Forexample,LoRAfine-tunes2.9MparametersoftheRoBERTa-basemodel
witharankof8,whereasKD-LoRAfine-tunesonly1.5Mparameterswiththesamerank.
• KD-LoRAis40%morecompactthanbothFFTandLoRAbyutilizingasmallerstudent
model. ThisapproachalsoreducesGPUmemoryusagebyapproximately75%comparedto
FFTand30%comparedtoLoRAduringtraining.
• KD-LoRA reduces inference time by approximately 30% while maintaining the same
convergencespeedasbothFFTandLoRA.
Figure1: Overviewofthreefine-tuningmethods: (a)FFT,whichupdatesallmodelparameters;(b)
LoRA,whichaddslow-rankmatricestoupdateasmallsubsetofparameters; and(c)KD,which
trainsasmallerstudentmodeltoemulatealargerteachermodel.
2

<!-- Page 3 -->

2 Method
WeproposeKD-LoRA,anovelfine-tuningmethodologythatintegratesLoRAwithKD.Theproposed
methodinvolvesthreemainsteps: (1)selectingandfine-tuningateachermodel,(2)initializinga
smallerstudentmodelwithLoRAmodules,and(3)performingdistillationtotransferknowledge
fromtheteachermodeltothestudentmodel.
Teacher Model. Let T denote the teacher model, initialized from a pre-trained language model
(e.g.,BERT,RoBERTa,DeBERTa). Theteachermodelisfine-tunedonaspecifictaskD ,using
task
FFT,whereallparametersofthemodelareupdated(Lvetal.,2024). Theobjectivefunctionfor
fine-tuningtheteachermodelis:
1 (cid:88)
LT = L (T(x ),y ) (1)
task |D | CE i i
task
(xi,yi)∈Dtask
whereL denotesthecross-entropyloss(CEL)loss,x representstheinputdata,andy denotesthe

### CE i i

correspondinglabel. Thislossfunctionmeasuresthediscrepancybetweenthepredictedprobabilities
T(x )andthetruelabelsy . Thefine-tunedteachermodelT thenservesasthesourceofdistilled
i i
knowledge.
StudentModelwithLoRA.ThestudentmodelS isinitializedfromasmallerversionwithinthe
samemodelfamilyastheteachermodelT.WemodifythestudentmodelbyinjectingLoRAmodules
intoitsarchitecture. Specifically,LoRAisappliedtotheattentionlayers,wheretheweightmatrices
W andW (correspondingtothequeryandvalueprojections)aredecomposedasfollows:
q v
W =Wbase+A B , W =Wbase+A B (2)
q q q q v v v v
where Wbase and Wbase are the pre-trained weight matrices, while A , B , A , and B are the
q v q q v v
low-rankmatrices,theonlyparametersupdatedduringfine-tuning.
KD-LoRA.WithLoRAmodulesalreadyinplace,theKDprocessisperformed,wherethestudent
modelS learnsfromtheteachermodel. Duringthisphase,thestudentmodel,equippedwithLoRA,
adapts its low-rank matrices to capture the knowledge transferred from the teacher. The student
modelistrainedonthetargettaskD usingthecombinedlossfunctionLS ,whichisgivenby:
task total
LS =αLS +(1−α)L (zS,zT) (3)
total task KD
wherezT andzS arethelogits(outputsbeforethesoftmaxlayer)oftheteacherandstudentmodels,
respectively. TheKDlossL iscomputedastheKullback-Leiblerdivergence(KL)(Shlens,2014)

## Kd

between the softened output probabilities of the teacher model T and the student model S. The
parameterαbalancesthetask-specificlossLS andtheKDlossL . Duringeachtrainingstep,the
task KD
studentmodel’slow-rankmatricesareupdatedtominimizethelossinEq.3.
3 Experiments
Figure2: Comparisonofconvergencespeedbetweenfullfine-tuning(FFT),LoRA,andKD-LoRA
forthreeLLMsontheCoLAtask. KD-LoRAmatchestheconvergencespeedofFFTandLoRA.
3

<!-- Page 4 -->

Table1: PerformancemetricsforBERT-base(BERT-b),DeBERTa-v3-base(DeB-b),andRoBERTabase(RoB-b)acrossGLUEtasksusingthreefine-tuningmethods. Resultsshowthemedianofthe
top6hyperparameterandPEFTsetups. DistilBERT-base(DBERT-b),DeBERTa-v3-small(DeB-s),
andDistilRoBERTa-base(DRoB-b)serveasstudentmodels. MetricsincludeMatthewscorrelation
forCoLA,averagePearson/SpearmancorrelationsforSTS-B,averageaccuracy/F1scoresforMRPC
andQQP,andaccuracyforallothertasks. KD-LoRAachievesabout97%ofFFT’sperformance
andabout98%ofLoRA’sperformance.

### Model BERT-b DBERT-b DeB-b DeB-s RoB-b DRoB-b

Method FFT LoRA KD-LoRA FFT LoRA KD-LoRA FFT LoRA KD-LoRA
CoLA 57.7 56.9 56.3 67.8 69.1 68.1 60.9 59.4 56.8
MNLI 84.5 83.4 82.0 90.3 90.3 88.8 87.7 87.2 83.3
m
MNLI 84.9 83.9 82.4 90.6 90.2 89.0 87.4 86.9 83.4
mm
MRPC 89.0 89.2 88.3 91.9 90.9 90.7 91.1 89.9 89.3
QNLI 91.8 91.1 89.7 94.1 94.3 93.4 92.7 92.8 90.7
QQP 89.7 87.9 89.1 91.2 90.4 89.9 89.8 88.6 87.3

### Rte 71.6 70.1 64.0 85.0 84.0 78.8 74.8 71.8 65.3

SST-2 92.8 92.6 92.0 95.9 96.0 95.7 94.3 94.2 92.9
STS-B 89.5 88.9 88.7 91.5 91.1 89.8 90.8 90.3 87.9

### Wnli 56.3 56.9 56.3 66.9 56.3 56.3 56.3 56.3 56.3


### Score 80.8 80.1 78.9 86.5 85.3 84.1 82.6 81.7 79.3

Table 2: Comparison of trainable parameters, memory usage, and inference time for three finetuningmethodsacrossthreemodelsandtheirdistilledcounterpartsforKD-LoRA.Inferencetimeis
averagedover100runsontheCoLAvalidationset. Witharankof8,KD-LoRAreducestrainable
parameters by 99% compared to FFT and 49% compared to LoRA, while lowering GPU
memoryusageby75%and30%,respectively. KD-LoRAalsocutsinferencetimeby30%.
Model Method Rank8 Rank16 Rank32 Rank64 MemoryUsage InferenceTime
BERT-base FFT 110M 110M 110M 110M 1332.0MB 6.10s

### LoRA 2.9M 5.9M 11.8M 23.6M 463.5MB 6.22s

DistilBERT-base KD-LoRA 1.2M 2.4M 4.7M 9.4M 296.8MB 5.36s
RoBERTa-base FFT 125M 125M 125M 125M 1515.9MB 7.21s

### LoRA 2.9M 5.9M 11.8M 23.6M 531.9MB 7.19s

DistilRoBERTa-base KD-LoRA 1.5M 2.9M 5.9M 11.8M 358.3MB 4.44s
DeBERTa-v3-base FFT 183M 183M 183M 183M 2234.5MB 14.37s

### LoRA 2.9M 5.9M 11.8M 23.6M 763.4MB 15.62s

DeBERTa-v3-small KD-LoRA 1.5M 2.9M 5.9M 11.8M 590.3MB 10.38s
Forourexperiments,weselectthreewidelyrecognizedencoder-onlyLLMs: BERT(Devlinetal.,
2019),RoBERTa(Zhuangetal.,2021),andDeBERTaV3(Heetal.,2023). WeevaluatethreefinetuningstrategiesacrossthesemodelsontheGLUEbenchmark: FFT,LoRA,andKD-LoRA.Inthis
approach,weemploycompactstudentmodelsthatbelongtothesamefamilyastheircorresponding
largerteachermodels. Specifically,weuseDistilBERT-base(Sanhetal.,2020),DeBERTa-v3-small,
andDistilRoBERTa-baseasstudentmodelsforBERT-base,DeBERTa-v3-base,andRoBERTa-base,
respectively. ForFFT,weselect25hyperparameterconfigurations,varyinglearningrates(2e-5to
5e-5),batchsizes(8to32),epochs(2to5),andweightdecay(0.01to0.1). ForLoRAandKD-LoRA,
weselect24PEFTconfigurations,varyingrank(8to32),epochs(3to5),LoRAalpha(16to32),
andLoRAdropout(0.0to0.1). AllexperimentsareconductedusingNVIDIAA100GPUs. Table1
showstheresultscalculatedbasedonthemedianofthetop6configurations. Table2providesthe
numberoftrainableparametersforeachmethodatdifferentranks,alongwiththeirGPUmemory
usageduringinferenceandtheinferencetimecalculatedontheCoLAdataset.
KD-LoRAachievesapproximately97%ofFFT’sperformanceandabout98%ofLoRA’s,withscores
of78.9forthestudentmodelofBERT-basecomparedto80.8forFFTand80.1forLoRA.Itreduces
thenumberoftrainableparametersbyabout99%comparedtoFFTandabout49%comparedto
LoRA,updating1.5MparametersintheDistilRoBERTa-basemodelwithKD-LoRAversus2.9M
withLoRAatarankof8. KD-LoRAalsoreducesGPUmemoryusageby75%comparedtoFFTand
30%comparedtoLoRA,resultinginamodelthatisabout40%morecompactthanbothFFTand
4

<!-- Page 5 -->

LoRA.Additionally,KD-LoRAdecreasesinferencetimebyaround30%ontheCoLAdataset,while
maintainingcomparableconvergencespeed,asillustratedinFigure2.
4 Conclusion
WepresentKD-LoRA,anovelfine-tuningmethodthatintegratesLoRAmodulesintoastudentmodel
whileleveragingKDfromalargerteachermodel. EmpiricalresultsontheGLUEbenchmarkshow
thatKD-LoRAretainsapproximately97%ofFFTperformanceand98%ofLoRAperformance,
allwhilereducingmodelsizebyaround40%. KD-LoRAalsolowerstrainableparametersby99%
comparedtoFFTand49%comparedtoLoRA,reducesGPUmemoryusageby75%comparedto
FFTand30%comparedtoLoRA,andcutsinferencetimeby30%.

### Acknowledgements

TheauthorsthankCMLabs,MilaandCIFARforresearchfunding. Thisresearchwasenabledbythe
computeprovidedbyCalculQuebecandDigitalResearchAllianceofCanada.

### References

Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez,
Ł ukasz Kaiser, and Illia Polosukhin. Attention is all you need. In I. Guyon, U. Von
Luxburg, S. Bengio, H. Wallach, R. Fergus, S. Vishwanathan, and R. Garnett, editors, Advances in Neural Information Processing Systems, volume 30. Curran Associates,
Inc., 2017. URL https://proceedings.neurips.cc/paper_files/paper/2017/file/
3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf.
ShenLi,YanliZhao,RohanVarma,OmkarSalpekar,PieterNoordhuis,TengLi,AdamPaszke,Jeff
Smith,BrianVaughan,PritamDamania,andSoumithChintala. Pytorchdistributed: experiences
onacceleratingdataparalleltraining. Proc.VLDBEndow.,13(12):3005–3018,aug2020. ISSN
2150-8097. doi: 10.14778/3415478.3415530. URLhttps://doi.org/10.14778/3415478.
3415530.
DeepakNarayanan,MohammadShoeybi,JaredCasper,PatrickLeGresley,MostofaPatwary,Vijay
Korthikanti, Dmitri Vainbrand, Prethvi Kashinkunti, Julie Bernauer, Bryan Catanzaro, Amar
Phanishayee,andMateiZaharia.Efficientlarge-scalelanguagemodeltrainingongpuclustersusing
megatron-lm. InProceedingsoftheInternationalConferenceforHighPerformanceComputing,
Networking,StorageandAnalysis,SC’21,NewYork,NY,USA,2021.AssociationforComputing
Machinery. ISBN9781450384421. doi: 10.1145/3458817.3476209. URLhttps://doi.org/
10.1145/3458817.3476209.
SajalDash,IsaacLyngaas,JunqiYin,XiaoWang,RomainEgele,GuojingCong,FeiyiWang,and
Prasanna Balaprakash. Optimizing distributed training on frontier for large language models.
CoRR,abs/2312.12705,2023. doi: 10.48550/ARXIV.2312.12705. URLhttps://doi.org/10.
48550/arXiv.2312.12705.
AbhimanyuDubey,AbhinavJauhri,AbhinavPandey,AbhishekKadian,AhmadAl-Dahle,etal. The
llama3herdofmodels,2024. URLhttps://arxiv.org/abs/2407.21783.
Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, et al. Language models are fewshot learners. In H. Larochelle, M. Ranzato, R. Hadsell, M.F. Balcan, and H. Lin, editors,
AdvancesinNeuralInformationProcessingSystems,volume33,pages1877–1901.CurranAssociates,Inc.,2020. URLhttps://proceedings.neurips.cc/paper_files/paper/2020/
file/1457c0d6bfcb4967418bfb8ac142f64a-Paper.pdf.
LiuZhuang,LinWayne,ShiYa,andZhaoJun. ArobustlyoptimizedBERTpre-trainingapproach
withpost-training. InShengLi, MaosongSun, YangLiu, HuaWu, KangLiu, WanxiangChe,
Shizhu He, and Gaoqi Rao, editors, Proceedings of the 20th Chinese National Conference on
ComputationalLinguistics,pages1218–1227,Huhhot,China,August2021.ChineseInformation
ProcessingSocietyofChina. URLhttps://aclanthology.org/2021.ccl-1.108.
5

<!-- Page 6 -->

Jason Wei, Maarten Bosma, Vincent Zhao, Kelvin Guu, Adams Wei Yu, Brian Lester, Nan Du,
AndrewM.Dai,andQuocVLe.Finetunedlanguagemodelsarezero-shotlearners.InInternational
ConferenceonLearningRepresentations,2022. URLhttps://openreview.net/forum?id=
gEZrGCozdqR.
SiddharthSamsi,DanZhao,JosephMcDonald,BaolinLi,AdamMichaleas,MichaelJones,William
Bergeron,JeremyKepner,DeveshTiwari,andVijayGadepally. Fromwordstowatts: Benchmarkingtheenergycostsoflargelanguagemodelinference. In2023IEEEHighPerformanceExtreme
ComputingConference(HPEC),pages1–9,2023. doi: 10.1109/HPEC58863.2023.10363447.
VladislavLialin,VijetaDeshpande,andAnnaRumshisky. Scalingdowntoscaleup: Aguideto
parameter-efficientfine-tuning,2023. URLhttps://arxiv.org/abs/2303.15647.
ArjunSingh,NikhilPandey,AnupShirgaonkar,PavanManoj,andVijayAski. Astudyofoptimizationsforfine-tuninglargelanguagemodels,2024.URLhttps://arxiv.org/abs/2406.02290.
TaehoKim,YanmingWang,VatshankChaturvedi,LokeshGupta,SeyeonKim,YonginKwon,and
SangtaeHa.Llmem:Estimatinggpumemoryusageforfine-tuningpre-trainedllms.InKateLarson,
editor,ProceedingsoftheThirty-ThirdInternationalJointConferenceonArtificialIntelligence,
IJCAI-24,pages6324–6332.InternationalJointConferencesonArtificialIntelligenceOrganization,
82024. doi: 10.24963/ijcai.2024/699. URLhttps://doi.org/10.24963/ijcai.2024/699.
MainTrack.
Yanjie Dong, Xiaoyi Fan, Fangxin Wang, Chengming Li, Victor C. M. Leung, and Xiping Hu.
Fine-tuninganddeployinglargelanguagemodelsoveredges: Issuesandapproaches,2024. URL
https://arxiv.org/abs/2408.10691.
NeilHoulsby,AndreiGiurgiu,StanislawJastrzebski,BrunaMorrone,QuentinDeLaroussilhe,AndreaGesmundo,MonaAttariyan,andSylvainGelly. Parameter-efficienttransferlearningforNLP.
InKamalikaChaudhuriandRuslanSalakhutdinov,editors,Proceedingsofthe36thInternational
Conference on Machine Learning, volume 97 of Proceedings of Machine Learning Research,
pages 2790–2799. PMLR, 09–15 Jun 2019. URL https://proceedings.mlr.press/v97/
houlsby19a.html.
EdwardJHu,yelongshen,PhillipWallis,ZeyuanAllen-Zhu,YuanzhiLi,SheanWang,LuWang,
and Weizhu Chen. LoRA: Low-rank adaptation of large language models. In International
ConferenceonLearningRepresentations,2022. URLhttps://openreview.net/forum?id=
nZeVKeeFYf9.
QingruZhang,MinshuoChen,AlexanderBukharin,PengchengHe,YuCheng,WeizhuChen,andTuo
Zhao. Adaptivebudgetallocationforparameter-efficientfine-tuning. InTheEleventhInternational
ConferenceonLearningRepresentations,2023a. URLhttps://openreview.net/forum?id=
lq62uWRJjiY.
BojiaZi,XianbiaoQi,LingzhiWang,JiananWang,Kam-FaiWong,andLeiZhang. Delta-loRA:
Fine-tuning high-rank parameters with the delta of low-rank matrices, 2024. URL https://
openreview.net/forum?id=FAO4VS9QRV.
Weijieying Ren, Xinlong Li, Lei Wang, Tianxiang Zhao, and Wei Qin. Analyzing and reducing
catastrophic forgetting in parameter efficient tuning, 2024. URL https://arxiv.org/abs/
2402.18865.
HongboZhao,BolinNi,JunsongFan,YuxiWang,YuntaoChen,GaofengMeng,andZhaoxiang
Zhang. Continual forgetting for pre-trained vision models. In Proceedings of the IEEE/CVF
Conference on Computer Vision and Pattern Recognition (CVPR), pages 28631–28642, June
2024a.
Shih-YangLiu,Chien-YiWang,HongxuYin,PavloMolchanov,Yu-ChiangFrankWang,Kwang-
TingCheng,andMin-HungChen. DoRA:Weight-decomposedlow-rankadaptation. InRuslan
Salakhutdinov,ZicoKolter,KatherineHeller,AdrianWeller,NuriaOliver,JonathanScarlett,and
FelixBerkenkamp,editors,Proceedingsofthe41stInternationalConferenceonMachineLearning,
volume235ofProceedingsofMachineLearningResearch,pages32100–32121.PMLR,21–27
Jul2024. URLhttps://proceedings.mlr.press/v235/liu24bn.html.
6

<!-- Page 7 -->

TimDettmers,ArtidoroPagnoni,AriHoltzman,andLukeZettlemoyer. QLoRA:Efficientfinetuning
ofquantizedLLMs. InThirty-seventhConferenceonNeuralInformationProcessingSystems,

## URLhttps://openreview.net/forum?id=OUIFPHEgJU.

George Pu, Anirudh Jain, Jihan Yin, and Russell Kaplan. Empirical analysis of the strengths
and weaknesses of PEFT techniques for LLMs. In ICLR 2023 Workshop on Mathematical
andEmpiricalUnderstandingofFoundationModels,2023. URLhttps://openreview.net/
forum?id=HB7zDQ4mvX.
YoonhoLee,AnnieSChen,FahimTajwar,AnanyaKumar,HuaxiuYao,PercyLiang,andChelsea
Finn. Surgicalfine-tuningimprovesadaptationtodistributionshifts. InTheEleventhInternational
ConferenceonLearningRepresentations,2023. URLhttps://openreview.net/forum?id=
APuPRxjHvZ.
Tianqi Chen, Bing Xu, Chiyuan Zhang, and Carlos Guestrin. Training deep nets with sublinear
memorycost,2016. URLhttps://arxiv.org/abs/1604.06174.
LongtengZhang,LinZhang,ShaohuaiShi,XiaowenChu,andBoLi. Lora-fa: Memory-efficient
low-rankadaptationforlargelanguagemodelsfine-tuning,2023b. URLhttps://arxiv.org/
abs/2308.03303.
JiaweiZhao,ZhenyuZhang,BeidiChen,ZhangyangWang,AnimaAnandkumar,andYuandong
Tian. Galore:Memory-efficientLLMtrainingbygradientlow-rankprojection. In5thWorkshopon
practicalMLforlimited/lowresourcesettings,2024b. URLhttps://openreview.net/forum?
id=AzqPyO22zt.
SamyamRajbhandari,JeffRasley,OlatunjiRuwase,andYuxiongHe. Zero: memoryoptimizations
towardtrainingtrillionparametermodels. InProceedingsoftheInternationalConferenceforHigh
PerformanceComputing,Networking,StorageandAnalysis,SC’20.IEEEPress,2020. ISBN
9781728199986.
BaohaoLiao,YanMeng,andChristofMonz. Parameter-efficientfine-tuningwithoutintroducingnew
latency. InAnnaRogers,JordanBoyd-Graber,andNaoakiOkazaki,editors,Proceedingsofthe
61stAnnualMeetingoftheAssociationforComputationalLinguistics(Volume1: LongPapers),
pages4242–4260,Toronto,Canada,July2023.AssociationforComputationalLinguistics. doi:
10.18653/v1/2023.acl-long.233. URLhttps://aclanthology.org/2023.acl-long.233.
JihaoGu,ShuaiChen,ZelinWang,YiboZhang,andPingGong. Sara: Singular-valuebasedadaptive
low-rankadaption,2024a. URLhttps://arxiv.org/abs/2408.03290.
GeoffreyHinton,OriolVinyals,andJeffreyDean. Distillingtheknowledgeinaneuralnetwork. In
NIPSDeepLearningandRepresentationLearningWorkshop,2015. URLhttp://arxiv.org/
abs/1503.02531.
OpenAI,JoshAchiam,StevenAdler,SandhiniAgarwal,LamaAhmad,IlgeAkkaya,FlorenciaLeoni
Aleman,DiogoAlmeida,etal. Gpt-4technicalreport,2024. URLhttps://arxiv.org/abs/
2303.08774.
RohanAnil,SebastianBorgeaud,Jean-BaptisteAlayrac,JiahuiYu,RaduSoricut,JohanSchalkwyk,
Andrew M. Dai, et al. Gemini: A family of highly capable multimodal models, 2024. URL
https://arxiv.org/abs/2312.11805.
Yuxian Gu, Li Dong, Furu Wei, and Minlie Huang. MiniLLM: Knowledge distillation of large
languagemodels. InTheTwelfthInternationalConferenceonLearningRepresentations,2024b.
URLhttps://openreview.net/forum?id=5h0qf7IBZZ.
XiaohanXu,MingLi,ChongyangTao,TaoShen,ReynoldCheng,JinyangLi,CanXu,Dacheng
Tao,andTianyiZhou. Asurveyonknowledgedistillationoflargelanguagemodels,2024. URL
https://arxiv.org/abs/2402.13116.
XiaoqiJiao,YichunYin,LifengShang,XinJiang,XiaoChen,LinlinLi,FangWang,andQunLiu.
TinyBERT:DistillingBERTfornaturallanguageunderstanding. InTrevorCohn,YulanHe,and
YangLiu,editors,FindingsoftheAssociationforComputationalLinguistics: EMNLP2020,pages
4163–4174,Online,November2020.AssociationforComputationalLinguistics.doi:10.18653/v1/
2020.findings-emnlp.372. URLhttps://aclanthology.org/2020.findings-emnlp.372.
7

<!-- Page 8 -->

Cheng-Yu Hsieh, Chun-Liang Li, Chih-kuan Yeh, Hootan Nakhost, Yasuhisa Fujii, Alex Ratner, Ranjay Krishna, Chen-Yu Lee, and Tomas Pfister. Distilling step-by-step! outperforming larger language models with less training data and smaller model sizes. In Anna Rogers,
Jordan Boyd-Graber, and Naoaki Okazaki, editors, Findings of the Association for Computational Linguistics: ACL 2023, pages 8003–8017, Toronto, Canada, July 2023. Association for Computational Linguistics. doi: 10.18653/v1/2023.findings-acl.507. URL https:
//aclanthology.org/2023.findings-acl.507.
Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. BERT: Pre-training of
deepbidirectionaltransformersforlanguageunderstanding. InJillBurstein,ChristyDoran,and
Thamar Solorio, editors, Proceedings of the 2019 Conference of the North American Chapter
of the Association for Computational Linguistics: Human Language Technologies, Volume 1
(LongandShortPapers),pages4171–4186,Minneapolis,Minnesota,June2019.Associationfor
ComputationalLinguistics. doi: 10.18653/v1/N19-1423. URLhttps://aclanthology.org/

## N19-1423.

PengchengHe,JianfengGao,andWeizhuChen.DeBERTav3:ImprovingdeBERTausingELECTRA-
stylepre-trainingwithgradient-disentangledembeddingsharing. InTheEleventhInternational
ConferenceonLearningRepresentations,2023. URLhttps://openreview.net/forum?id=
sE7-XhLxHA.
Alex Wang, Amanpreet Singh, Julian Michael, Felix Hill, Omer Levy, and Samuel R. Bowman.
GLUE:Amulti-taskbenchmarkandanalysisplatformfornaturallanguageunderstanding. In
InternationalConferenceonLearningRepresentations,2019. URLhttps://openreview.net/
forum?id=rJ4km2R5t7.
KaiLv,YuqingYang,TengxiaoLiu,QipengGuo,andXipengQiu. Fullparameterfine-tuningfor
largelanguagemodelswithlimitedresources. InLun-WeiKu,AndreMartins,andVivekSrikumar,
editors,Proceedingsofthe62ndAnnualMeetingoftheAssociationforComputationalLinguistics
(Volume1: LongPapers),pages8187–8198,Bangkok,Thailand,August2024.Associationfor
ComputationalLinguistics. URLhttps://aclanthology.org/2024.acl-long.445.
JonathonShlens. Notesonkullback-leiblerdivergenceandlikelihood,2014. URLhttps://arxiv.
org/abs/1404.2000.
VictorSanh,LysandreDebut,JulienChaumond,andThomasWolf. Distilbert,adistilledversionof
bert: smaller,faster,cheaperandlighter,2020. URLhttps://arxiv.org/abs/1910.01108.
8