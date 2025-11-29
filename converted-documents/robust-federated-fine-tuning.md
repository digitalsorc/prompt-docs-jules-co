---
title: "Robust Federated Fine Tuning"
original_file: "./Robust_Federated_Fine_Tuning.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["llm", "rag", "fine-tuning", "evaluation", "multimodal"]
keywords: ["lora", "rolora", "ffa", "tuning", "learning", "qnli", "methods", "mnli", "page", "federated"]
summary: "<!-- Page 1 -->

Robust Federated Finetuning of Foundation Models
via Alternating Minimization of LoRA
ShuangyiChen1 YueJu2 HardikDalal2 ZhongwenZhu2 AshishKhisti1
Abstract beneficialforfoundationmodels,asitcanaccessabroad
rangeofdatawhilemaintainingprivacy. ### Parameter-EfficientFine-Tuning(PEFT)hasrisen

asaninnovativetrainingstrategythatupdatesonly Recently, Parameter-Efficient Fine-Tuning (PEFT) has
aselectfewmodelparameters,significantlylow- emergedasaninnovativetrainingstrategythatupdates"
related_documents: []
---

# Robust Federated Fine Tuning

<!-- Page 1 -->

Robust Federated Finetuning of Foundation Models
via Alternating Minimization of LoRA
ShuangyiChen1 YueJu2 HardikDalal2 ZhongwenZhu2 AshishKhisti1
Abstract beneficialforfoundationmodels,asitcanaccessabroad
rangeofdatawhilemaintainingprivacy.

### Parameter-EfficientFine-Tuning(PEFT)hasrisen

asaninnovativetrainingstrategythatupdatesonly Recently, Parameter-Efficient Fine-Tuning (PEFT) has
aselectfewmodelparameters,significantlylow- emergedasaninnovativetrainingstrategythatupdatesonly
eringbothcomputationalandmemorydemands. asmallsubsetofmodelparameters,substantiallyreducing
PEFTalsohelpstodecreasedatatransferinfed- computational and memory demands. A notable method
erated learning settings, where communication inthiscategoryisLoRA(Huetal.,2021),whichutilizes
depends on the size of updates. In this work, low-rankmatricestoapproximateweightchangesduring
we explore the constraints of previous studies fine-tuning. Thesematricesareintegratedwithpre-trained
thatintegrateawell-knownPEFTmethodnamed weightsforinference,facilitatingreduceddatatransferin
LoRAwithfederatedfine-tuning,thenintroduce scenarios such as federated learning, where update size
RoLoRA, a robust federated fine-tuning frame- directly impacts communication efficiency. Many works
workthatutilizesanalternatingminimizationap- integrateLoRAintofederatedsetting. Forexample, Fedproach for LoRA, providing greater robustness PETuning (Zhang et al., 2023d) compared various PEFT
againstdecreasingfine-tuningparametersandin- methodsinafederatedsetting. SLoRA(Babakniyaetal.,
creasingdataheterogeneity. Ourresultsindicate 2023),ahybridapproachthatcombinessparsefine-tuning
thatRoLoRAnotonlypresentsthecommunica- withLoRA,isintroducedtotackledataheterogeneityinfedtionbenefitsbutalsosubstantiallyenhancesthe eratedsettings. Furthermore,FS-LLM(Kuangetal.,2023)
robustnessandeffectivenessinmultiplefederated ispresented,whichisaframeworkforfine-tuningLLMsin
fine-tuningscenarios. federatedenvironments. However,thesestudiestypically
apply the FedAVG algorithm directly to LoRA modules,
overlookingtheinterferenceintroducedbythisaggregation

## Introduction approach. With this consideration, Sun et al. designs a

federated finetuning framework named FFA-LoRA (Sun
Therecentemergenceoffoundationmodelsinvariousapplietal.,2024)basedonLoRAbyfreezingdown-projection
cationssignificantlychangesthefieldofmachinelearning.
matrixAforalltheclientsandonlyupdatingup-projection
Characterizedbytheirbroadadaptabilityandmassivescale,
matrix B. Furthermore, they apply DP-SGD to preserve
thesemodelsrequireaccesstovastanddiversedatasetstoefprivacy. Usingsufficientnumberoffinetuningparameters,
fectivelylearnacrossdifferenttasksanddomains. However,

### FFA-LoRAwithalargerlearningrateachievesperformance

this presents a significant challenge: foundation models
comparabletoFedAVGforLoRAmoduleswhilehalving
not only require large amounts of data, but also data of
thecommunicationcosts. However,weobservethatwith
highquality. Federatedlearningprovidesapromisingsolufewerfine-tuningparameters,FFA-LoRAislessrobustthan
tiontothisissue. Itenablestheuseofdatafrommultiple

### FedAVG for LoRA modules, primarily due to its limited

sourceswhileprotectingtheprivacyofthedata. Bycombinexpressiveness stemming from the restricted number of
inginsightsfromdifferentdecentralizedsources,federated
trainableparameters. Anothercommonissueinfederated
learning allows for collaborative model training without
learning is data heterogeneity among clients. To address
exposingsensitiveinformation. Thismethodisespecially
this,wedrewinspirationfromthepersonalizedfederated
frameworkFedRep(Collinsetal.,2021),whichalternates
1ECE Department, University of Toronto, Toronto, Canada
2Ericsson-GAIA Montre´al, Canada. Correspondence to: between updating clients’ representation and head. This
Shuangyi Chen <shuangyi.chen@mail.utoronto.ca>, Ashish approachhighlightstheimportanceoflearningarobustlow-
Khisti<akhisti@ece.utoronto.ca>. rankrepresentationanddemonstratessuperiorconvergence
speedcomparedtosimultaneouslyupdatingbothrepresen-
WorkpresentedatES-FoMo-IIworkshopatICML2024,Vienna,
tationandhead. Therefore,weproposearobustfederated
Austria.PMLR235,2024.Copyright2024bytheauthor(s).
1
4202
peS
4
]GL.sc[
1v64320.9042:viXra

<!-- Page 2 -->

RobustFederatedFinetuningofFoundationModelsviaAlternatingMinimizationofLoRA
fine-tuningframework,RoLoRA,basedonalternatingmin- 2.3.FedRep: CommonRepresentationviaAlternating
imizationofLoRA.Empiricalevidencedemonstratesthat Minimization

### RoLoRAismorerobustagainstDecreasingFine-tuning


### Acommonchallengeinfederatedlearningisdatahetero-


### Parameters and Increasing Data Heterogeneity, while

geneity among clients. FedRep (Collins et al., 2021) adstillhalvingcommunicationcosts,similartoFFA-LoRA.
dressesthisbyfindingacommonrepresentation,whichis
effectivelyachievedviaalternativelyupdatingclients’rep-
RelatedWork Weprovideasummaryoftheliteratureon resentationandhead,aggregatingonlyrepresentationwhile
PEFT,VariantsofLoRA,PEFTinFederatedSetting,and keepingtheheaddiverse. Thealgorithmdemonstratesthe
FLwithdataheterogeneityinAppendixA. necessityoflearningarobustlow-rankrepresentation. Additionally,thealternatingoptimizationhasshownsuperior
convergence speed compared to approaches that simulta-

## Preliminaries

neouslyupdatebothrepresentationandhead. Weobserve

### Low-RankAdaptation: LoRA astructuredsimilaritybetweentheLoRAadapterandthe

representation-headstructure. Specifically,weconsiderthe

### Low-RankAdaptation(LoRA)(Huetal.,2021)fine-tunes

down-projection matrix A in each LoRA adapter as the
largelanguagemodelsefficientlybymaintainingtheorigilow-rankrepresentationforthefeaturesoftheintermediate
nalmodelweightsfixedandaddingsmall,trainablematrices
layers.Wehypothesizethatlearningarobustlowrankrepreineachlayer. Thesematricesperformlow-rankdecomposisentation(down-projectionmatrix)isalsoadvantageousfor
tionsofupdates,reducingthenumberoftrainableparamtheintermediatefeatureswhentheclientshasheterogeneous
eters. This approach is based on the finding that updates
inputs. However,sincetheLoRAadaptersarecascadedin
tomodelweightsduringtask-specifictuningareusuallyof
the model unlike single representation-head structure in
lowrank,whichallowsforfewerparameterstobeadjusted.
modelconsideredinFedRep,keepingup-projectionmatrix
Forexample,forapre-trainedweightmatrixW ∈Rd×d,
0 Bdiversemaynotbefavorableforconvergence.
the update is a low-rank product BA, where A ∈ Rr×d
and B ∈ Rd×r, with r << d. Only A and B are train- Withtheseconsiderations,weproposerobustfederatedfineable, allowing W = W +αBA, with α adjusting the tuning framework based on alternating minimization of
0
update’simpact. ApplyingLoRAinafederatedsettingisa LoRA(RoLoRA).
practicalchoice. ByusingLoRAadapters,clientscanfinetunefoundationmodelsefficientlywithlimitedresources.
Sinceonlythesespecificmatricesneedtobetransmittedto

## OurFramework

acentralserver,thisapproachsignificantlyreducescommunicationcosts. ThismakesLoRAanadvantageoussolution

### WedescribetheframeworkdesignofRoLoRAanddiscuss

forenhancingmodelperformanceincollaborativescenario
itspracticaladvantages.
comparingtofullparameterfinetuninginthefederatedsetting. Alternating Minimization and Corresponding Aggregation Motivated by the observations discussed in Section2.2and2.3,weproposeapplyingalternatingminimiza-

### FedAVGofLoRAIntroducesInterference

tiontothelocalfine-tuningofeachclientinasettingwith
IntegratingLoRAwithinafederatedsettingpresentschal- N clients. UnliketheapproachinFFA-LoRA,whereAis
lenges. Insuchasetup,eachoftheN clientsisprovided consistentlyfrozen,wesuggestaalternatingupdatestrategy.
withthepretrainedmodelweightsW ,whichremainfixed Therearealternatingoddandevencommunicationrounds
0
during finetuning. Clients are required only to send the designatedforupdating,aggregatingAandB,respectively.
updatedmatricesB andA toacentralserverforaggregai i
t e i t o a n l . ., W 2 h 0 i 2 l 3 e ) m a o n s d tc F u e r d re P n E t T st u u n d i i n e g s ( , Z su h c a h ng as e S t L al o . R ,2 A 0 ( 2 B 3 a d b ) a , k c n o i m ya - Intheoddcomm.round: N 1 (cid:88) N ∆W i 2t+1
monlyapplyFedAVGdirectlytothesematricesasshown i=1
in (2), this approach might not be optimal. The precise = 1 (Bt+1At +Bt+1At +...+Bt+1At ) (3)
updateforeachclient’smodel,∆W i ,shouldbecalculated N 1 1 2 2 N N
astheproductofthelow-rankmatricesA i andB i . Conse- = 1 (Bt+1+Bt+1+...+Bt+1)At
quently,aggregationontheindividualmatricesintroduces N 1 2 N
interference.

## N

Intheevencomm.round: 1 (cid:88) ∆W2t+2

### N i


### N i=1

1 (cid:88) 1
∆W = (B A +B A +...+B A ) (1) 1
N i N 1 1 2 2 N N = (Bt+1At+1+Bt+1At+1+...+Bt+1At+1) (4)
i=1 N 1 1 2 2 N N
1 1 1
̸= (B +B +...+B ) (A +A +...+A ) (2) = Bt+1(At+1+At+1+...+At+1)
N 1 2 N N 1 2 N N 1 2 N
2

<!-- Page 3 -->

RobustFederatedFinetuningofFoundationModelsviaAlternatingMinimizationofLoRA
Intheoddcommunicationround,allclientsfreezeAtand GLUE,wefollowthepreviousstudies(Zhangetal.,2023d)
updateBt. Thecentralserverthenaggregatestheseupdates andusetheoriginalvalidationsetasthenewtestsetand
to compute Bt+1 = 1 (cid:80)N Bt+1 and distributes Bt+1 splitapartofthetrainingsetasthevalidationset.

### N i=1 i

backtotheclients. Inthesubsequentcommunicationround,
clientsfreezeBt+1 andupdateAt. Theserveraggregates

### Implementation. We implement all the methods based

thesetoobtainAt+1 = 1 (cid:80)N At+1andreturnsAt+1to
N i=1 i onFederatedScope-LLM(Kuangetal.,2023). Tomakea
theclients. Itisimportanttonotethatinround2t+1,the
fair comparison, for each dataset, we obtain the best perfrozenAtareidenticalacrossallclients,astheyaresynchroi formanceontestsetandreporttheaverageoverfiveseeds.
nizedwithAtfromthecentralserveratthebeginningofthe

### Specifically,thelearningrateischosenfromtheset{5e−

round. Thisstrategyensuresthattheupdateandaggregation
4,1e−3,2e−3,5e−3,1e−2,2e−2,5e−2,1e−1,2e−1}.
methodintroducesnointerference,asdemonstratedin(3)
Otherhyper-parametersforexperimentsarespecifiedinTaand(4).
ble4inAppendixB.1.

### ComputationandCommunicationCost Theparameter-


### EffectofNumberofFinetuningParameters InFigure1,

freezing nature of RoLoRA enhances computational and
wecomparethreemethodsacrossfiveGLUEdatasets. We
communicationefficiency. Ineachcommunicationround,
apply LoRA to every weight matrix of the selected laythe number of trainable parameters in the model is effecers,givendifferentbudgetsofLoRAparameters. Foreach
tivelyhalvedcomparedtoFedAVGwithLoRA.Theonly
dataset, we experiment with three budgets, ranging from
additionalcostforRoLoRAcomparedtoFFA-LoRAisthe
hightolow. Thecorrespondinglayersets,P ,P ,P ,are
alternatingfreezingofthecorrespondingparameters. We 1 2 3
detailedinTable5inAppendixB.1.
remarkthisadditionalcostisnegligiblebecauseitisapplied
to the clients’ models and can be executed concurrently Thefiguresindicatesthatwithsufficientnumberoffinetunduringtheserver’saggregation. ingparameters,thethreemethodscanachievecomparable
best accuracy; as the number of LoRA parameters is re-

## Experiments duced,theperformanceofthethreemethodsdeteriorates

to varying degrees. However, RoLoRA, which achieves
We evaluate the performance of RoLoRA in various fed- performance comparable to LoRA, demonstrates greater
erated settings. We use NVIDIA GeForce RTX 4090 or robustnesscomparedtoFFA-LoRA,especiallyundercon-
NVIDIAA40foralltheexperiments. ditionsoflimitedfine-tuningparameters. Itisimportantto
notethatwiththesamefinetuningparameters,thecommu-
Baselines Consideringcross-silofederatedsettingwhere nicationcostofRoLoRAandFFA-LoRAisalwayshalfof
thenumberofclientsisrelativelysmallandallclientswill thatofLoRAduetotheirparameterfreezingnature. This
participate in each round, we will explore the following impliesthatRoLoRAnotonlysustainsitsperformancebut
threemethodsbasedonFedAVG. also enhances communication efficiency. We expand the
middlesetofdataofeachofFigure1,correspondingtoP ,
2
• LoRA means LoRA adapter and its finetuning algo- andshowthedetailsoftheperformanceofthreemethodsin
rithmaredirectlyappliedtolocalfinetuningofclients Table1.
inthefederatedsystem. Specifically,initerationt,the
serverreceivesAt
i
andBt
i
fromclientiandaggregates
EffectofDataHeterogeneity Inthissection,westudy
byAt =Avg(At
i
)andBt =Avg(Bt
i
).
theeffectofdataheterogeneity. ThelayersetwithLoRA
adapters in Table 2 is P as in Table 1. In Table 2, we
• LoRA-FFA(Sunetal.,2024)isabaselinethatenable 2
increasedthenumberofclientsfrom3to20,andthento
the clients to finetune B and keep A frozen locally.
Thus, in iteration t, the server aggregates by Bt = 50, ensuring that there is no overlap in the training sam-
Avg(Bt). pleseachclientcanaccess. Consequently, eachclientrei ceivesasmallerfractionofthetotaldataset,leadingtoarise
• RoLoRAenablesclientstoalternateupdatingAand indataheterogeneityamongtheclients. Weobservethat
BasdescribedinSection3. asthedataheterogeneityincreases,whilemaintainingthe
samenumberoffine-tuningsamples,theperformanceofthe
ModelandDatasets. Wetakethepre-trainedRoBERTa- LoRAmethodsignificantlydeterioratesformostdatasets.
Large(355M)(Liuetal.,2019)modelsfromtheHugging- In contrast, RoLoRA maintains its accuracy levels. The
Face Transformers library. and evaluate the performance performanceofFFA-LoRAalsodeclines,attributedtothe
ofthreefederatedfinetuningmethodson5datasets(SST-2, limitedexpressivenessoftherandominitializationofAfor
QNLI, MNLI, QQP, RTE) from the GLUE (Wang et al., clients’ heterogeneous data. Notably, RoLoRA achieves
2019). Duetothelimitationoftheunpublishedtestsetin thisaccuracywhileincurringonlyhalfthecommunication
3

<!-- Page 4 -->

RobustFederatedFinetuningofFoundationModelsviaAlternatingMinimizationofLoRA
Figure1.ResultswithRoBERTa-LargemodelsonGLUEofdifferentbudgetoffinetuningparameters. Theaccuracyiscomputedby
averagingoverdifferentranks{1,2,4,8}.Thenumberofclientsis3.
Rank Methods Comm.cost SST-2 QNLI MNLI QQP RTE Avg.
LoRA ×16 95.68±0.14 91.46±0.30 85.93±0.01 85.95±0.18 81.35±0.74 88.07
r=8 FFA-LoRA ×8 94.99±0.10 91.09±0.36 85.21±0.03 85.76±0.08 80.14±1.02 87.44
RoLoRA ×8 95.45±0.14 91.84±0.09 85.76±0.01 85.91±0.22 81.32±0.78 88.06
LoRA ×8 95.62±0.17 91.59±0.21 86.20±0.05 86.13±0.10 81.46±1.22 88.20
r=4 FFA-LoRA ×4 95.18±0.09 91.35±0.32 84.58±0.21 85.50±0.25 81.10±0.33 87.48
RoLoRA ×4 95.49±0.16 91.64±0.30 85.70±0.04 86.14±0.06 82.43±0.84 88.28
LoRA ×4 95.64±0.11 92.04±0.11 85.85±0.19 86.16±0.08 82.19±1.03 88.38
r=2 FFA-LoRA ×2 94.91±0.16 90.11±0.17 84.06±0.19 85.48±0.01 80.86±0.51 87.08
RoLoRA ×2 95.60±0.10 91.62±0.32 85.55±0.05 86.16±0.18 82.19±1.03 88.22
LoRA ×2 95.32±0.18 90.48±0.56 85.08±0.04 85.01±0.05 81.10±0.95 87.40
r=1 FFA-LoRA ×1 94.49±0.22 89.87±0.37 82.60±0.03 84.42±0.50 79.66±1.08 86.21
RoLoRA ×1 95.22±0.14 91.01±0.23 84.97±0.05 85.24±0.18 80.23±1.02 87.33
Table1.ResultswithRoBERTa-LargemodelsonGLUE.Wereporttheaverageandstd. overfiveseeds. Thenumberofclientsis3.
PleaserefertoTable6inAppendixB.2.2fortheactualcommunicationcost.
SST-2 QNLI MNLI QQP RTE Model/Rank Methods QNLI MNLI QQP RTE
LoRA 95.64 92.04 85.85 86.16 82.19 LoRA 86.07 76.58 83.77 73.58
iid. FFA-LoRA 94.91 90.11 84.06 85.48 80.86 Rob-Lr=4 FFA-LoRA 88.54 78.28 84.04 74.64
RoloRA 95.60 91.62 85.66 86.16 82.19 RoLoRA 89.13 82.33 84.58 76.51
LoRA 94.27 86.91 81.22 82.07 46.21 LoRA 85.47 76.26 82.32 69.68
mildhet. FFA-LoRA 93.92 89.58 80.51 82.62 57.76 Rob-Lr=2 FFA-LoRA 87.81 77.24 83.81 76.11
RoloRA 94.84 90.77 85.13 85.10 81.23 RoLoRA 89.19 82.18 84.24 76.53

### LoRA 93.23 82.57 58.96 76.96 49.10

severehet. FFA-LoRA 92.32 85.15 62.79 77.78 53.07 Table3.ResultswithRoBERTa-LargemodelsonGLUE.Same
RoloRA 94.61 89.83 85.15 85.55 72.92 messagesizeineachroundforthreemethodsforeachdataset.The
numberofclientsis3.
Table2.ResultswithRoBERTa-Largemodelswithvaryingclient
numbers(3,20,50)toincreasedataheterogeneityinfederated
setting,maintainingaconstantsamplecountduringfine-tuning.
Therankusedis2.
tailedinTable1. Thesecondapproachrequiresdoubling
thenumberoflayersequippedwithLoRAadapters. Inthe
costs associated with LoRA. Figure 2 in Appendix B.2.2 resultspresentedinTable3,thelatterstrategyisemployed.
illustratesthedynamicsduringfine-tuningforthreemeth- Specifically,forbothFFA-LoRAandRoLoRA,weadjust
ods,highlightingthattheconvergencespeedofRoLoRAis thecommunicationcostsbydoublingthenumberoflayers
substantiallybetterthanthatoftheothertwomethods. equipped with LoRA adapters, compared to the baseline
LoRA method, where the layer set P are attached with
3
adapters,therebystandardizingthesizeofthetransmitted
AlignCommunicationCostforThreeMethods InTamessages. Table3demonstratesthatwhenoperatingwithin
ble 3, we conduct a comparison of three methods under
aconstrainedcommunicationcostbudget,theperformance
theconstraintofidenticalcommunicationcostsunderthe
of RoLoRA consistently surpasses that of the other two
assumptionthatthenumberofclientsissmall. Toalignthe
methods.
communicationcostsacrossthesemethods,twoapproaches
are considered. The first approach involves doubling the Moreexperimentalresultswithdifferentmodelsandsettings
rank of FFA-LoRA and RoLoRA, with the outcomes de- areprovidedinAppendixB.2.
4

<!-- Page 5 -->

RobustFederatedFinetuningofFoundationModelsviaAlternatingMinimizationofLoRA

## Conclusion Li,Y.,Yu,Y.,Liang,C.,He,P.,Karampatziakis,N.,Chen,


### W.,andZhao,T. Loftq: Lora-fine-tuning-awarequantiza-

Inthiswork,weintroduceRoLoRA,arobustfederatedfinetionforlargelanguagemodels,2023.
tuningframeworkusingalternatingminimizationforLoRA.
RoLoRAimprovesrobustnessagainstreducedfine-tuning Liu, S.-Y., Wang, C.-Y., Yin, H., Molchanov, P., Wang,
parameters and increased data heterogeneity. Our results Y.-C.F.,Cheng,K.-T.,andChen,M.-H. Dora: WeightshowthatRoLoRAenhancescommunicationefficiency,ro- decomposedlow-rankadaptation,2024.
bustness,andeffectivenessinvariousfederatedfine-tuning
settings. Liu, X., Ji, K., Fu, Y., Tam, W.L., Du, Z., Yang, Z., and

### Tang,J. P-tuningv2: Prompttuningcanbecomparable

tofine-tuninguniversallyacrossscalesandtasks,2022.

### References

Liu, Y., Ott, M., Goyal, N., Du, J., Joshi, M., Chen, D.,
Babakniya, S., Elkordy, A., Ezzeldin, Y., Liu, Q., Song,
Levy,O.,Lewis,M.,Zettlemoyer,L.,andStoyanov,V.

### K.-B.,EL-Khamy,M.,andAvestimehr,S. SLoRA:Fed-

Roberta: Arobustlyoptimizedbertpretrainingapproach,
eratedparameterefficientfine-tuningoflanguagemod-
2019.
els. InInternationalWorkshoponFederatedLearning
in the Age of Foundation Models in Conjunction with
Oh, J., Kim, S., and Yun, S.-Y. FedBABU: Toward en-
NeurIPS2023, 2023. URLhttps://openreview.
hancedrepresentationforfederatedimageclassification.
net/forum?id=06quMTmtRV.

### InInternationalConferenceonLearningRepresentations,

Chen, H.-Y. and Chao, W.-L. On bridging generic and 2022. URLhttps://openreview.net/forum?
personalizedfederatedlearningforimageclassification, id=HuaYQfggn5u.
2022.

### Sun, Y., Li, Z., Li, Y., and Ding, B. Improving loRA in

Collins,L.,Hassani,H.,Mokhtari,A.,andShakkottai,S. privacy-preserving federated learning. In The Twelfth
Exploiting shared representations for personalized fed- InternationalConferenceonLearningRepresentations,
eratedlearning. InMeila,M.andZhang,T.(eds.),Pro- 2024. URLhttps://openreview.net/forum?
ceedings of the 38th International Conference on Ma- id=NLPzL6HWNl.
chineLearning,volume139ofProceedingsofMachine
Wang, A., Singh, A., Michael, J., Hill, F., Levy, O., and

### Learning Research, pp. 2089–2099. PMLR, 18–24 Jul


#### URLhttps://proceedings.mlr.press/ Bowman,S.R. Glue: Amulti-taskbenchmarkandanalyv139/collins21a.html. sisplatformfornaturallanguageunderstanding,2019.

Dettmers,T.,Pagnoni,A.,Holtzman,A.,andZettlemoyer, Xu, J., Tong, X., and Huang, S.-L. Personalized fed-
L. Qlora: Efficientfinetuningofquantizedllms,2023. erated learning with feature alignment and classifier
collaboration. In The Eleventh International Confer-
Hayou,S.,Ghosh,N.,andYu,B. Lora+: Efficientlowrank enceonLearningRepresentations,2023. URLhttps:
adaptationoflargemodels,2024. //openreview.net/forum?id=SXZr8aDKia.

### Houlsby, N., Giurgiu, A., Jastrzebski, S., Morrone, B.,

Zaken,E.B.,Ravfogel,S.,andGoldberg,Y. Bitfit: Simde Laroussilhe, Q., Gesmundo, A., Attariyan, M., and
pleparameter-efficientfine-tuningfortransformer-based
Gelly, S. Parameter-efficient transfer learning for nlp,
maskedlanguage-models,2022.
2019.

### Zhang,H.,Li,C.,Dai,W.,Zou,J.,andXiong,H. FedCR:


### Hu,E.J.,Shen,Y.,Wallis,P.,Allen-Zhu,Z.,Li,Y.,Wang,

Personalized federated learning based on across-client

### S.,Wang,L.,andChen,W. Lora: Low-rankadaptation

commonrepresentationwithconditionalmutualinformaoflargelanguagemodels,2021.
tion regularization. In Krause, A., Brunskill, E., Cho,
Kopiczko,D.J.,Blankevoort,T.,andAsano,Y.M. VeRA: K., Engelhardt, B., Sabato, S., and Scarlett, J. (eds.),
Vector-basedrandommatrixadaptation. InTheTwelfth Proceedings of the 40th International Conference on
InternationalConferenceonLearningRepresentations, Machine Learning, volume 202 of Proceedings of Ma-

## URLhttps://openreview.net/forum? chineLearningResearch,pp.41314–41330.PMLR,23–

id=NjNfLdxr3A. 29 Jul 2023a. URL https://proceedings.mlr.
press/v202/zhang23w.html.

### Kuang,W.,Qian,B.,Li,Z.,Chen,D.,Gao,D.,Pan,X.,Xie,

Y., Li, Y., Ding, B., and Zhou, J. Federatedscope-llm: Zhang,L.,Zhang,L.,Shi,S.,Chu,X.,andLi,B. Lora-fa:
Acomprehensivepackageforfine-tuninglargelanguage Memory-efficientlow-rankadaptationforlargelanguage
modelsinfederatedlearning,2023. modelsfine-tuning,2023b.
5

<!-- Page 6 -->

RobustFederatedFinetuningofFoundationModelsviaAlternatingMinimizationofLoRA
Zhang, Q., Chen, M., Bukharin, A., Karampatziakis, N.,

### He, P., Cheng, Y., Chen, W., and Zhao, T. Adalora:

Adaptivebudgetallocationforparameter-efficientfinetuning,2023c.
Zhang, Z., Yang, Y., Dai, Y., Wang, Q., Yu, Y., Qu, L.,
and Xu, Z. FedPETuning: When federated learning
meets the parameter-efficient tuning methods of pretrainedlanguagemodels. InRogers,A.,Boyd-Graber,J.,
andOkazaki,N.(eds.),FindingsoftheAssociationfor

### ComputationalLinguistics: ACL2023,pp.9963–9977,

Toronto,Canada,July2023d.AssociationforComputationalLinguistics. doi: 10.18653/v1/2023.findings-acl.

## URL https://aclanthology.org/2023.

findings-acl.632.
6

<!-- Page 7 -->

RobustFederatedFinetuningofFoundationModelsviaAlternatingMinimizationofLoRA

### A.RelatedWorks


### A.1.ParameterEfficientFineTuning(PEFT):LoRAandItsVariants

Asthesizeoflargelanguagemodels(LLMs)continuestoincrease,itiscomputationallyexpensiveandtime-consuming
tofinetunetothefullmodel. Parameterefficientfinetuning(PEFT)allowsforupdatestoasmallersubsetofparameters,
significantlyreducingthecomputationalandmemoryrequirements. Oneofthemostwell-knownmethodsisLoRA(Huetal.,
2021). LoRAuseslow-rankmatricestoapproximatechangesinweightsduringfine-tuning,allowingthemtobeintegrated
withpre-trainedweightsbeforeinference. BasedonLoRA,manyPEFTmethodsaredeveloped. Forexample,Zhanget
al. (Zhangetal.,2023c)designsAdaLoRAbyusingSVDdecompositionandpruninglesssignificantsingularvaluesfor
moreefficientupdates. VeRA(Kopiczkoetal.,2024)isproposedtofurtherreducethenumberoftrainableparameters
duringfinetuningbyusingasinglepairoflow-rankmatricessharedacrossalllayersandlearningsmallscalingvectors.
Zhang et al. (Zhang et al., 2023b) proposes a memory-efficient fine-tuning method named LoRA-FA which keeps the
projection-downweightofAfixedandupdatestheprojection-upweightofBduringfinetuning. Hayouetal. (Hayouetal.,
2024)enhanceLoRAbyassigningdifferentlearningratestoAandB,theoreticallyconfirmingthattheoptimalapproach
requiresahigherlearningrateforBthanforA. Liuetal. analyzemagnitudeanddirectionalupdatesinLoRAversusfull
parameterfine-tuningandintroduceDoRA(Liuetal.,2024),whichdecomposespre-trainedweightsforfine-tuningand
appliesLoRAfordirectionalupdates. AquantizedversionofLoRAnamedQLoRA(Dettmersetal.,2023)isintroduced.
Buildinguponthat,Lietal. developsLoftQ(Lietal.,2023)forabetterinitializationforquantizedtraining.

### A.2.PEFTinFederatedSetting

PEFTadjustsonlyafewlightweightorasmallportionofthetotalparametersforspecifictasks,keepingmostfoundational
model parameters unchanged. This feature can help reduce data transfer in federated learning, where communication
dependsonthesizeofupdates. Zhangetal. (Zhangetal.,2023d)comparesmultiplePEFTmethodsinfederatedsetting,
includingAdapter(Houlsbyetal.,2019),LoRA(Huetal.,2021),Prompttuning(Liuetal.,2022)andBit-Fit(Zakenetal.,
2022). SLoRA(Babakniyaetal.,2023),whichcombinessparsefinetuningandLoRA,isproposedbyBabakniyaetal. to
addressthedataheterogeneityinfederatedsetting. Sunetal. designsafederatedfinetuningframeworknamedFFA-LoRA
basedonLoRA(Sunetal.,2024)byfreezingmatrixAforalltheclientsandonlyupdatingmatrixB. Furthermore,they
applyDP-SGDtopreserveprivacy. FS-LLM(Kuangetal.,2023),aframeworkforfinetuningLLM,isintroduced.

### A.3.FLwithDataHeterogeneity

FLwithaCommonRepresentation FLwithacommonrepresentationaimstoaddressthechallengesofdataheterogeneityinFL.ThoseFLmethodslearnasharedglobalrepresentationwhileallowingeachclienttohaveitsownpersonalized
partial model. Works include FedRep(Collins et al., 2021), which learns a global low-dimensional representation and
personalizedheadforeachclient,FedCR(Zhangetal.,2023a),whichintroducesaregularizertoencouragelearningashared
representation,andFedPAC(Xuetal.,2023),whichperformsclass-wisefeaturealignment. OthermethodslikeFedBABU
(Ohetal.,2022)andFedRoD(Chen&Chao,2022)alsoaimtolearnasharedrepresentationacrossclients. Although
wefocusonacommonmodelinthefederatedsettinginthiswork,wegotinspiredbytrainingalgorithmintroducedby
FedRep(Collinsetal.,2021)tolearnalow-rankrepresentationfortheintermediatefeatures. Wediscussthesimilarityand
differencebetweentheLoRAadapterandrepresentation-headstructure.
B.Experiments

### B.1.Setup

Weshowthehyper-parameterconfigurationsforeachdatasetinTable4.

## Sst-2 Qnli Mnli Qqp Rte

Totalcomm.rounds 500 500 500 500 200

### BatchSize 64 32 32 32 32


### LocalEpochs 20 20 20 20 20

Table4. Hyper-parametersconfigurations
7

<!-- Page 8 -->

RobustFederatedFinetuningofFoundationModelsviaAlternatingMinimizationofLoRA
LayerAttributes SST-2 QNLI MNLI QQP RTE
Type W ,W W ,W W ,W W ,W W ,W

### P v q v q v q v q v q

1 Index {0,...,23} {12,...,23} {12,...,23} {12,...,23} {12,...,23}
Type W ,W W ,W W ,W W ,W W ,W

### P v q v q v q v q v q

2 Index {18,...,23} {15,...,23} {15,...,23} {15,...,23} {16,...,23}
Type W W ,W W ,W W ,W W ,W

### P v v q v q v q v q

3 Index {21,...,23} {21,...,23} {21,...,23} {21,...,23} {21,...,23}

### Table5. TheselectedlayersetattachedwithLoRA

InTable5,weincludethedetailsaboutlayersattachedwithLoRAadaptersfordifferentbudgetoffinetuningparameters,
foreachdataset.

### B.2.MoreResults


## B.2.1.Communicationcost

InTable6,weshowtheuplinkcommunicationcostforthreemethodsforthelayersetP usingrank=1.
2
Rank Methods SST-2 QNLI MNLI QQP RTE

### LoRA 46.9 93.8 93.8 140.6 125

r=1 FFA-LoRA 23.5 46.9 46.9 70.3 62.5

### RoLoRA 23.5 46.9 46.9 70.3 62.5

Table6.Uplinkmessagesize(KB)ineachcommunicationroundforexperimentsinTable1whenrank=1. Themessagesizewill
proportionallyincreaseifutilizingdifferentranks.

## B.2.2.Finetuningdynamicsofthesetupwithseveredataheterogeneity

In Figure 2, we show the convergence of three methods under severe data heterogeneity with 50 clients. RoLoRA
demonstratessuperiorconvergencespeedcomparedtotheothertwomethods.
Figure2.AccuraciesoverroundswithRoBERTa-LargemodelsonSST-2,QNLI,MNLI,andQQP.Thetotalnumberofclientsis50.
8

<!-- Page 9 -->

RobustFederatedFinetuningofFoundationModelsviaAlternatingMinimizationofLoRA

## B.2.3.Deberta-Xlargeresults

In Table 7, we show the results with DeBERTa-XLarge (900M). For both FFA-LoRA and RoLoRA, we modify the
communicationcostsbyequippingtwiceasmanylayerswithLoRAadapterscomparedtothestandardLoRAmethod. So
thecommunicationcostsarealignedforthreemethods.
Model/Rank Methods QNLI MNLI QQP RTE

### LoRA 90.16 83.58 85.67 74.97

Deb-XL FFA-LoRA 90.08 83.31 85.79 78.73
r=4
RoLoRA 91.36 84.63 86.54 81.48

### LoRA 90.12 83.25 84.56 72.55

Deb-XL FFA-LoRA 90.28 83.47 85.59 79.06
r=2

### RoLoRA 91.32 84.84 86.50 81.34

Table7.ResultswithDeBERTa-XLargemodelsonGLUE.Samemessagesizeineachroundforthreemethodsforeachdataset. The
numberofclientsis3.

## B.2.4.Performancewhenqloraisapplied

InTable8,wequantizethefrozenpre-trainedweightsto8bitand4bitforeachclient,andapplyQLoRA(Dettmersetal.,
2023). Therelativeaccuracyiscomputedas AccFP−Avg(Acc8b+Acc4b). Weusesufficientfinetuningparametersandtheselected

### AccFP

layersetisP tostudytheeffectofthequantizedfoundationmodelinthefederatedsetting.
1

### Methods QQP QNLI MNLI

FP 8-bit 4-bit FP 8-bit 4-bit FP 8-bit 4-bit RelativeAcc.
LoRA 85.86 85.78 85.47 92.87 92.71 92.00 87.69 86.57 86.49 ↓0.7%
FFA-LoRA 85.74 85.59 85.35 92.51 91.20 91.12 85.75 84.86 83.19 ↓1.3%
RoLoRA 85.64 85.51 85.47 92.48 92.51 91.63 87.95 87.27 86.12 ↓0.7%
Table8. ResultsofRoBERTa-LargemodelsonQQP,QNLI,MNLIwiththequantizedbasemodel.Therankusedis2.
9