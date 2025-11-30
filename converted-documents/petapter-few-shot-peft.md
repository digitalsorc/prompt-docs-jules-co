---
title: "PETapter Few Shot PEFT"
original_file: "./PETapter_Few_Shot_PEFT.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["llm", "rag", "fine-tuning", "evaluation", "multimodal"]
keywords: ["petapter", "sep", "pet", "few", "mask", "shot", "pattern", "lora", "learning", "page"]
summary: "<!-- Page 1 -->

PETapter: Leveraging PET-style classification heads for modular few-shot
parameter-efficient fine-tuning

### JonasRieger and MattesRuckdeschel and GregorWiedemann

LeibnizInstituteforMediaResearch|Hans-Bredow-Institut(HBI)
Rothenbaumchaussee36,20148Hamburg,Germany
rieger@statistik.tu-dortmund.de
{m.ruckdeschel, g.wiedemann} @leibniz-hbi.de

### Abstract (cid:80) (t→c)

Few-shotlearningandparameter-efficientfine- LinearLayer LinearLayer
tuning(PEFT)arecrucialtoovercomethechal- ("
related_documents: []
---

# PETapter Few Shot PEFT

<!-- Page 1 -->

PETapter: Leveraging PET-style classification heads for modular few-shot
parameter-efficient fine-tuning

### JonasRieger and MattesRuckdeschel and GregorWiedemann

LeibnizInstituteforMediaResearch|Hans-Bredow-Institut(HBI)
Rothenbaumchaussee36,20148Hamburg,Germany
rieger@statistik.tu-dortmund.de
{m.ruckdeschel, g.wiedemann} @leibniz-hbi.de

### Abstract (cid:80) (t→c)

Few-shotlearningandparameter-efficientfine- LinearLayer LinearLayer
tuning(PEFT)arecrucialtoovercomethechal- (h→t) (h→c)
lenges of data scarcity and ever growing language model sizes. This applies in particu- ActivationFunction ActivationFunction
lartospecializedscientificdomains,whereresearchers might lack expertise and resources LinearLayer LinearLayer
to fine-tune high-performing language mod- (h→h) (h→h)
els to nuanced tasks. We propose PETapter,
anovelmethodthateffectivelycombinesPEFT PEFTmodule PEFTmodule
(e.g.,LoRA) (e.g.,LoRA) methodswithPET-styleclassificationheadsto
+ +
boostfew-shotlearningcapabilitieswithoutthe

### BasePLM BasePLM

significant computational overhead typically
(e.g.,RoBERTa) (e.g.,RoBERTa)
associated with full model training. We validate our approach on three established NLP PETapter StandardPEFT
benchmarkdatasetsandonereal-worlddataset
fromcommunicationresearch. Weshowthat Figure 1: Schematic representation of the PETapter
PETapter not only achieves comparable per- architecturecomparedtostandardPEFTmethods.
formance to full few-shot fine-tuning using
pattern-exploitingtraining(PET),butalsoprovides greater reliability and higher parameperform poorly in these tasks (e.g., Rieger et al.,
terefficiencywhileenablinghighermodular-
2024). Few-shotlearning,withitspromisetogenity and easy sharing of the trained modules,
eralizefromalimitednumberoftrainingsamples,
whichenablesmoreresearcherstoutilizehighperformingNLP-methodsintheirresearch. offers an alternative pathway towards mitigating
the data scarcity problem. However, the deploy-
1 Introduction
mentoflarge-scalelanguagemodelsinafew-shot
setting can be challenging, primarily due to the
Few-shot learning and parameter-efficient finesubstantial computational resources required for
tuning(PEFT)haveemergedaspivotaldisciplines
trainingandfine-tuning,astheyupdateallparameintherealmofnaturallanguageprocessing(NLP),
tersofthemodelbydefault. PEFTmethods,such
especiallyinapplicationswheredatascarcityposes
asadaptermodules,presentaviablesolutiontothis
significant challenges. Whilst for a lot of scienissuebyenablingtheadaptationofpretrainedmodtists from fields like communication science or
elstospecifictaskswithminimalmodificationsto
political science, raw text data is available, highthemodelarchitecture. Specifically,thesemethods
qualitylabeleddataisstillscarceandthecreation
freezealargepartofthemodel’sparametersand
istime-consuming,costlyandrequiringtrainedextrainonlysmallpartsoftheexistingorfewnewly
perts. Discourseanalysisinthosefields,isclosely
added layers (Poth et al., 2023). Further, PEFT
related to the NLP sub-task of argument mining,
methodsusingastandardlinearlayerperformsigespecially argument identification and classificanificantlyworsethanfew-shotmethodswhenusing
tion. Due to the nuanced and context-dependent
fewobservations(cf.Sections5.3and6.3).
nature of argumentative discourse, standard finetuning methods for pretrained language models For this reason, this paper aims to delve into
(PLM)withonlyafewlabeleddatapointsusually the innovative intersection of few-shot learning
4202
ceD
6
]LC.sc[
1v57940.2142:viXra

<!-- Page 2 -->

and parameter-efficient fine-tuning. By integrat- RoBERTa(Liuetal.,2019)duetoitsstrongperforingfew-shotlearningparadigmswithPEFTtech- manceevenwithacomparativelysmallnumberof
niques, this paper explores how, e.g., the field of parameters(Base: 125million,Large: 355million).
argumentminingcanleveragethestrengthsofboth Whenusingnon-Englishtexts,themultilingualalapproaches to efficiently classify text sequences, ternative XLM-RoBERTa (Conneau et al., 2020)
evenwhenlittledataisavailable. Throughastudy canbeused,whichwastrainedon100differentlanon three typical NLP benchmark datasets and a guagesandprovidesareliablebasisforachieving
study on a real-world argument mining dataset, good performance, at least for high resource lanwedemonstratethatthecombinationoffew-shot guages. Asthenextbestmodel,(m)DeBERTa(He
andPEFTmethodologiescansignificantlyreduce etal.,2023)formsapromisingbasePLM,butwith
therelianceonextensiveannotateddatasetswhile 1.5 billion parameters it already has significantly
achieving competitive performance (to full few- higherrequirementsintermsofGPUcapacityand
shot fine-tuning) with reduced computational ef- computationtime.
fort. It thus combines the advantages of the two
2.1 Parameter-EfficientFine-Tuning(PEFT)
fields, few-shot learning and parameter-efficient
fine-tuning. This makes possible the creation of The ever-increasing sizes of base PLMs pose a
smallyetpowerfullanguagemodelsthatcaneasily great challenge for fully fine-tuning all paramebe created by non-experts, opening up new qual- ters. Rebuffi et al. (2017), as well as Houlsby
itative and quantitative research opportunities to et al. (2019), were among the first to tackle this
researchersfromvariousbackgroundswhowantto problembyfreezingthePLMandinsteadinserting
leveragetextdata. andtrainingbottleneckfeed-forwardlayerswithin
As contribution, we propose a new method, the pretrained architecture. Pfeiffer et al. (2020)
PETapter, as a combination of PET-style classi- refined this idea into a slightly more parameterficationheadswithPEFTmethods. Weshowthat efficientandrobustmethod,thoughstillsequential
in most scenarios PETapter is as performant as initsbasicidea,whichisnamedPfeifferadapters.
PETitself,i.e.noticeablebetterthanPEFTwitha Techniques such as low-rank adaptation (LoRA,
standardclassificationhead. PETapteradditionally Hu et al., 2021) and (IA)3 (Liu et al., 2022) inoffersallPEFTadvantages,i.e.itrequireslesscom- troduce minimal updates to the model weights,
putational resources and is easier to share in the whiletheirparallelapproachmakesitpossibleto
researchcommunityduetoitsmodularity. Wealso combine the newly learned parameters with the
show that PETapter provides more robust predic- frozen ones in such a way that there is no overtionsthanPET,especiallyonreal-worlddatasets. head during inference. Recent innovations such
Bydoingso,thispapernotonlycontributestothe asconsideringdifferentranksforeachlinearlayer
theoretical advancement of NLP techniques but in PRILoRA (Benedek and Wolf, 2024), sharing
also offers practical insights for researchers and thelow-rankmatricesacrossalllayerswithlayerpractitionersworkingonsupervisedtextclassifica- specificlearnedscalingvectorsinVeRA(Kopiczko
tionproblemsfromvariousscientificbackgrounds. et al., 2024) or LoRA-like decomposition of pre-
In Section 2, we review relevant preliminary trained weights in DoRA (Liu et al., 2024) are
NLP work, in Section 3, we recapitulate the defi- examples of further LoRA-like advancements in
nitionofpattern-verbalizerpairs(PVP)forusage thefieldofparameter-efficientfine-tuning.
inournewmethodPETapterinSection4. InSec- Inaddition,ComPEFT(Yadavetal.,2023)and
tions5and6,weconductintensiveNLPbenchmark QLoRA(Dettmersetal.,2023)offerthepossibilstudiesandareal-worldstudy,whichwefinallydis- ity of even more effective parameter usage with
cussinSection7andsummarizeinSection8. The condensationofinformationthroughquantization
data and code used will be made available in a anddesparsification. RoSA(Nikdanetal.,2024)
GitHubrepositoryafteracceptance. combines low-rank adaptation with high sparsity
trainingfollowingtheideaofrobustprincipalcom-
2 RelatedWork ponent analysis. Several specialized approaches
exist,oneofwhichisAdaSent(Huangetal.,2023)
Pretrainedlanguagemodels(PLMs)serveastheba- focusingonPEFTforsentencerepresentations.
sisformostclassificationtasksinnaturallanguage Whilemanyimplementationsareoftenlimited
processing(NLP).Afrequentlycomparedmodelis tothePEFTcharacterofthemethods(Mangrulkar

<!-- Page 3 -->

etal.,2022;Huetal.,2023a,b),thePythonpackage dia: Hüning et al. (2022) classify whether user-
Adapters(Pothetal.,2023)facilitatesthemodular generatedchatmessagescontainanargumentususeofPEFTmethods,highlightingatrendtowards ingmachinelearningtechniquesutilizingsentence
modular deep learning (Pfeiffer et al., 2023) and embeddingsasfeatures. Forsimplicity,theycateholistic PEFT implementations (He et al., 2022; gorize claims as no argument in their setting. Ju-
SabryandBelz,2023). rkschatetal.(2022)considerthepossibilityoffewshot methods for classifying aspects of argumen-
2.2 Few-ShotTextClassification
tativesentencesandshowthatPETperformsbest
Few-shot text classification aims to maximize amongthemethodsconsidered. Likewise,PETis
modelperformancewithminimallabeleddata. For used by Rieger et al. (2024) and compared with
this, a lot of approaches are based on a combi- the use of PEFT methods for the identification
nation of prompt-based learning and meta learn- of claims and arguments from news media artiing. Schick and Schütze (2021) are the first to cles. Theauthorsfindthatthetaskischallenging
proposetheutilizationofso-calledprompt-based evenforhumans,sothatonlymoderateinter-coder
clozequestions. Inthispattern-exploitingtraining agreementsareachieved.
(PET),amaskedtokenispredictedinalanguage Inthefollowing,wepresentthePETaptermodel,
model task style, similar to that used in pretrain- which combines few-shot and PEFT methods to
ing. Theauthorsshowthatduetothemodel’sprior achieve great performance, in particular in realknowledge,itisabletopredicttheseso-calledver- worlddatascarceargumentminingsettings.
balizers better than plain numbered class labels.
Furthermore,theauthorsshowthatmeta-learning 3 Pattern-Verbalizer-Pair(PVP)
on soft labels generated by augmentations using
We consider a pretrained language model (PLM)
iterativePET(iPET)alsoleadstoanimprovement,

### M with an underlying vocabulary V, where

so that a combination of prompt-based learning
[MASK] ∈ V, i.e. we assume a mask token to
andmeta-learning(Zhangetal.,2022)isproposed.
becontainedinthevocabulary. Inaddition,letL

### Chen and Shu (2023) use such an approach and

beasetoftargetlabelsforaclassificationtaskand
proposetheuseoflabel-guideddataaugmentation
x ∈ Vn an input (possibly consisting of several
methodsforprompt-basedfew-shottuning.
segments)thatcontainsatotalofntokensfromthe

### Ling et al. (2023) demonstrate the possibility

vocabulary V. We define a pattern as a function
ofanoptimizedautomatedsearchforverbalizers

### Pm : Vn → Vn+p,wherem ≤ pisthenumberof

inprompt-basedlearning,whileKarimiMahabadi
[MASK] tokens contained in the pattern and p is
etal.(2022)suggestanapproachwithouttheneed
thetotalnumberofvocabularyitemsaddedtothe
forprompts. Complementarytothis,SetFit(Tuninputxbythepatternfunction.
stalletal.,2022)formtripletsofpositiveandneg-

### Furthermore,letvm : L → Vm beaverbalizer

ativeexamplesandusecontrastivelearningtoeffunctionthatassignsmtokensfromthevocabulary
fectivelytrainonfewtrainingsamples. Therecipe
V to each label ℓ ∈ L. As the inventors of PET
T-Few(Liuetal.,2022)asanadditionaldedicated
(SchickandSchütze,2021)suggest,werefertothe
few-shot model is based on the zero-shot model
combination(Pm,vm)asapattern-verbalizerpair

### T0(Sanhetal.,2022)andenrichesitwithacom-

(PVP). The pattern function Pm is used to transbination of losses, the PEFT method (IA)3 and a
formtheinputxintoakindofclozequestionand
pretrainingofitusingout-of-domaindata,which
theverbalizerfunctionvm providesforeachlabel
can be quite expensive with regard to the trainthe“speaking”andrepresentativefill-inwordsfor
ingtimeneeded. PET,SetfitandT-Fewrepresent
thecorrespondingclozequestion,whicharetobe
key developments in the few-shot discipline and
predictedbythemodelM. AllPVPsusedinthis
produce comparable performances on the RAFT
papercanbefoundintheAppendicesAandB.
benchmark dataset (Alex et al., 2021), each with
strengthsandweaknessesondifferentdatasets
4 PETapter
2.3 ArgumentMining

### PETapter can be seen as a modular classification

In the field of argument mining, the following headwhichcanbeaddedflexiblytoaPEFTframeworks are related to our idea of using PETapter work as an alternative to a classical linear layer
toidentifyargumentativesentencesfromnewsme- classification head, cf. Figure 1. Here, the last

<!-- Page 4 -->

(purple)linearlayeroftheclassificationheaddoes 5 BenchmarkStudy
notreducethedimensiondirectlytothenumberof
Toevaluatehowwellourmodelperformsincomclassesc,buttothesizetofthesub-vocabularyT
parison to existing state-of-the-art methods, we
oftheverbalizerfunctionused. Thus,eachdimenconsider three established NLP datasets in a first
sion of the output embedding represents a token
benchmark study. These have quite a laboratory
fromthereducedverbalizervocabulary,similarto
character,asthedistributionoftheclasslabelsis
and motivated by the pattern-exploiting training
prettymuchbalanced. Furthermore,itisnotfinally
(PET) by Schick and Schütze (2021). Then, the
clear to what extent (possibly implicit) informalogits for the verbalizers (possibly composed of
tionaboutthetestdataofsuchpubliclyavailable
several tokens) can be calculated as a sum of the
datasets is contained in PLMs (Li and Flanigan,
logitsofthemaskedtokensinthepattern(cf.Equa-
2024). Nevertheless,suchdatasetswithpredefined
tion1).
train-testsplitsofferthepossibilityofcomparing

### Ingeneral,PETaptercanbecombinedwithany

methodsacrossstudieswithouttheneedofrerun-
PEFT method (cf. the blue segment in Figure 1),
ningalltheexperiments.
i.e.italsofeaturesallitsadvantagesoverfullfinetuning: fastertraining,lessresourcerequirements,
5.1 Datasets: AG,Yahoo,Yelp
bettersharabilityandreusabilityduetomodularity

### WefollowthestudybySchickandSchütze(2022)

as wellas robustification(at least) withregard to
and use the three established NLP datasets AG’s
theeliminationofcatastrophicforgetting. Specif-

### News (AG), Yahoo Questions (Yahoo), and Yelp

ically, PETapter implements all these advantages
Full (Yelp), which are presented by Zhang et al.
over PET, which uses full fine-tuning, while per-
(2015). InAppendixA,furtherinformationonthe
formingonpar(cf.Sections5.3and6.3).
threedatasetsisgiven.

### LetLbeasetoftargetlabelsforaclassification

taskwith|L| = c,letPm(x)beapatternfunction For the training, we create 5 stratified datasets
insertingm[MASK]tokenstoaninputx,andlet with n = 10 randomly drawn observations and
vm(ℓ) be an injective function that maps each of 5 datasets with n = 100 observations each for
thelabelsℓ ∈ Ltomvocabularytokens. Then,we the problems AG, Yahoo, and Yelp. We evaluate
allexperimentswiththecorrespondingentiretest
obtainthesubsetofthevocabularyrelevantforthe
verbalizersasT = (cid:83) (cid:83)m vm(ℓ) withT ⊂ V datasetfromthepredefinedsplit.
ℓ∈L i=1 i
andt = |T|thecorrespondingnumberofrelevant
5.2 ExperimentalSetup
tokens,i.e.wecanrefinevm : L → Tm.
Moreover,letM(vm(ℓ) | Pm(x)) ∈ Rm denote AsPLM,wemakeuseofRoBERTaBaseandLarge.
thelogitsforthem[MASK]tokens,theoutputof Forfine-tuningmethods,weconsiderthefew-shot
thetoplinearlayer(purple)inFigure1ontheleft. methodPET,PEFTmethodswitha(standard)lin-
The final score for each of the label candidates ℓ ear layer as classification head, and our method
foragiveninputtextxisthengivenas PETapter,i.e.PEFTmethodsincombinationwith
aPET-styleclassificationhead. Inbothcases,we
m
s(ℓ | x) =
(cid:88)

### M(vm(ℓ) | Pm(x)) (1)

considerthemethods(IA)3,LoRAandaPfeiffer
i
adapterasPEFTmethods. ForPETandPETapter,
i=1
wecomparetheuseofpromptorQ&Apattern,folandthecorrespondingpseudo-probabilityas
lowingSchickandSchütze(2022). Ineachdataset,
exp(s(ℓ | x)) wemeasurethechangeofusingn = 10or100obq(ℓ | x) = . (2)
(cid:80) exp(s(ℓ′ | x)) servations. Moreover,werepeateachexperiment
ℓ′∈L
fivetimes,i.e.inTable1eachcellcorrespondsto

### Usingthis,wecancalculatethecross-entropyloss

25experiments(5repetitions×5datasets). InApoverallobservationsas
pendixA,furtherinformationonallparametersas
L = − (cid:88) (cid:88) 1 (x,ℓ∗)log[q(ℓ | x)] wellastheusedpatternsisgiven.
CE {ℓ=ℓ∗}
(x,ℓ∗)ℓ∈L
5.3 Results
(cid:88)
= − log[q(ℓ∗ | x)] (3)
Table1showstheaverageaccuracyofthesettings
(x,ℓ∗)
and the standard deviation across the 25 experiifweconsiderℓ∗ ∈ Ltobethetruelabelofx. mentspercell. Overall,itcanbeseenthatthebest

<!-- Page 5 -->

PromptPattern Q&APattern LinearLayer

### PETapter PETapter

n Data (IA)3 LoRA Pfeif. PET (IA)3 LoRA Pfeif. PET (IA)3 LoRA Pfeif.
esaBaTREBoR
0.668 0.681 0.683 0.804 0.596 0.672 0.680 0.800 0.297 0.293 0.316

## 10 Ag

±.092 ±.080 ±.078 ±.036 ±.077 ±.077 ±.088 ±.028 ±.053 ±.045 ±.059
0.236 0.292 0.271 0.545 0.274 0.295 0.285 0.515 0.105 0.116 0.123
10 Yahoo
±.016 ±.033 ±.042 ±.040 ±.026 ±.041 ±.036 ±.036 ±.009 ±.020 ±.016
0.403 0.434 0.423 0.441 0.359 0.412 0.390 0.442 0.215 0.219 0.224
10 Yelp
±.037 ±.035 ±.038 ±.017 ±.037 ±.042 ±.047 ±.025 ±.017 ±.023 ±.027
0.856 0.861 0.860 0.875 0.863 0.861 0.862 0.871 0.837 0.862 0.864

## 100 Ag

±.012 ±.012 ±.012 ±.007 ±.006 ±.010 ±.011 ±.008 ±.007 ±.008 ±.008
0.622 0.642 0.642 0.666 0.622 0.637 0.633 0.659 0.418 0.636 0.633
100 Yahoo
±.018 ±.009 ±.011 ±.007 ±.005 ±.007 ±.008 ±.007 ±.034 ±.013 ±.012
0.541 0.553 0.551 0.552 0.536 0.553 0.548 0.554 0.354 0.538 0.535
100 Yelp
±.010 ±.018 ±.016 ±.014 ±.014 ±.015 ±.014 ±.015 ±.022 ±.018 ±.020
egraLaTREBoR
0.641 0.714 0.702 0.842 0.611 0.746 0.738 0.836 0.305 0.373 0.443

## 10 Ag

±.100 ±.070 ±.081 ±.025 ±.073 ±.054 ±.060 ±.032 ±.030 ±.049 ±.104
0.242 0.331 0.290 0.574 0.323 0.365 0.346 0.550 0.124 0.150 0.169
10 Yahoo
±.027 ±.040 ±.056 ±.030 ±.049 ±.049 ±.054 ±.040 ±.012 ±.027 ±.041
0.442 0.470 0.479 0.475 0.440 0.472 0.490 0.486 0.211 0.221 0.216
10 Yelp
±.040 ±.041 ±.035 ±.026 ±.049 ±.049 ±.046 ±.041 ±.010 ±.012 ±.014
0.868 0.873 0.875 0.877 0.876 0.870 0.873 0.874 0.833 0.875 0.875

## 100 Ag

±.011 ±.010 ±.010 ±.009 ±.009 ±.010 ±.010 ±.009 ±.011 ±.008 ±.008
0.654 0.662 0.661 0.680 0.655 0.654 0.656 0.675 0.364 0.648 0.647
100 Yahoo
±.020 ±.014 ±.017 ±.013 ±.010 ±.008 ±.012 ±.013 ±.043 ±.016 ±.015
0.611 0.613 0.614 0.593 0.626 0.622 0.620 0.595 0.347 0.551 0.512
100 Yelp
±.011 ±.014 ±.010 ±.014 ±.008 ±.013 ±.013 ±.016 ±.019 ±.019 ±.043
Table1: Meanaccuracies(±standarddeviation)oftheexperimentsinthebenchmarkstudy.
RoBERTa Architecture AG Yahoo Yelp the best global performance in this case, while it
producesratherlowscoresinmostscenarios. Our

### Base PETapter 0.33 0.33 0.32

Base PET 0.38 0.39 0.39 explanationforthisisthatIA3isjustonecompo-

### Large PETapter 0.65 0.64 0.65

nentofthegenerallyinbenchmarkscompetitively

### Large PET 1.00 1.00 1.00

performingT-Few. Overall,promptandQ&Apat-
Large PET 6.1s 6.2s 6.2s ternperformsimilarly. Thus,wecanconfirmthese
findingsfromSchickandSchütze(2022)regarding
Table2: Comparisonoftrainingtimesperiterationof

### PETandshowthattheygenerallyholdforPETapter

n=100observationsinthebenchmarkstudy. Thelast
aswell. Basically,itcanbeseenthatthelinearlayer
rowshowsthetimeforPETusingRoBERTaLarge.The
otherrowsindicatethetimerelativetoit. Thetimesfor rarelycomesclosetotheperformanceofPETapter;
usingPETapteroralinearlayerareidentical,asarefor usinglinearlayerclassificationheadsincombinathethreearchitectures(IA)3,LoRA,andPfeiffer. tionwith(IA)3 leadstotheworstresultsoverall.

### As a result, it is evident that PETapter is to be

performanceisachievedbyPETusingtheprompt preferredovertheuseofaclassicallinearlayeras
pattern, while PETapter achieves the best values aclassificationheadinusecaseswherethebenefits
intwoscenariosandthelinearlayerclassification of PEFT methods are desired. At the same time,
headneverperformsbest. Asexpected,RoBERTa PETapterachievescomparableperformancetoPET
Large consistently yields better results than the inmostcases.
Base variant, although the PEFT methods generally benefit somewhat more from the use of the Inaddition,asaPEFTmethod(cf.Section2.1),
largermodel. TheaccuracyachievedbyPETapter PETaptercanbetrainedmoreeffectivelythanstanisusuallyveryclosetothatofPET.Merelyinthe dardPET.InTable2thetrainingtimesofthemodsetting n = 10 for Yahoo the values are signifi- elsaredisplayed. Accordingtothis,PETapter(no
cantlyworse. Ontheotherhand, forn = 100on matterthearchitecture)requires≈ 65%ofthetime
Yelp,allthreePEFTarchitecturescombinedwith ofregularPETperiteration. Comparedtoaregular
our PETapter method are noticeably better than PEFTapproachusingalinearlayer,PETapterdoes
PETitself. (IA)3 withQ&Apatternevenleadsto notproduceanyoverheadintrainingtime.

<!-- Page 6 -->

6 Real-WorldStudy Label Train Test
10∗ 100∗ 250∗ All
argumentagainst 1.2 11.8 29.4 92 118
AsindicatedinSection5,theevaluationbasedon
argumentfor 1.9 19.4 48.6 152 162
AG, Yahoo, and Yelp represents a lab situation, claimagainst 2.4 23.5 58.8 184 248
e.g., because of their balancedness and (implicit) claimfor 4.6 45.2 113.2 354 456
inclusion in the pretraining of language models.

### Table 3: Label distribution in the train and test data

Complementarytothis,inasecondstudy,wecomsplitoftheUkrainedataset. ∗Expecteddistributionfor
pare theperformance ofthe methodson a(so far
randomselection.
unpublished)datasetwithreal-worldchallenges. It
isadatasetinthecontextofargumentminingwith
argumentativesentencesonthetopicofarmsdeliv- 6.2 ExperimentalSetup
eriestoUkrainewithatotalof7301thematically ForthecomparisonofourPETaptermodeltoPET
relevant articles in 2022 from 22 German media andPEFTwithalinearlayerasclassificationhead,
outlets. Thecompositionisexplainedindetailin weusetheXLM-RoBERTaLargemodelduetothe
thestudyofRiegeretal.(2024). Here,weconsider Germandataset. Inadditiontothedifferentarchiaversionofthedatasetconsistingof1766labeled tectures (cf. Section 5.2), we compare the effect
datawiththefourpossiblelabelsclaim/argument ofdifferentsamplingstrategiesandthenumberof
for/against,withnon-relevantsentencesalreadyre- trainingobservationsn = 10,100,250. Weagain
moved. repeateachexperimentfivetimes. Thus,asingle
cell in Table 4 corresponds to 25 experiments (5
6.1 Dataset: UkraineArmsDeliveries repetitions×5datasets). InAppendixB,further
informationonallparametersaswellastheused
TheGermanlanguageUkrainedatasetconsistsof
patternsisgiven.
766train(294articles)and1000test(369articles)
observations. Usingatwo-stagesampling(firstarti- 6.3 Results
cle,thensentence)weintendtotackletheproblem Table4showsthemacro-F1scoresfromtherealthatincludingveryrelatedsentencesfromthesame worldstudy. Accordingtothis,thereisnosigniftextinbothsplitscouldleadtoanoveroptimistic icantdifferencebetweentheperformanceofPET
estimation of the error. Here, a single observa- and PETapter. The scores using the linear layer,
tionconsistsofatargetsentencetobeclassifiedas on the other hand, are significantly worse in all
wellastwocontextualsentencesbeforeandafterit. scenariosandcombinations. Theclassificationtask
Based on the 766 observations, we draw training appearstobesohardthatforn = 10neitherany
sets of sizes n = 10,100,250 according to three scenarionoranymodelcouldachievemeaningful
differentsamplingstrategies. performance. Forn = 100,250,itcanbeseenthat
Wedrawthesamenumberofobservationsfrom PET benefits greatly from the use of a balanced
thesubsetsofthefourlabelsinequalsampling,i.e. training set (equal sampling); this can be seen in
25 observations each in the scenario of n = 100. astrongreductionofuncertaintymeasuredbythe
Using random sampling, we make a simple ran- standarddeviation. Inprinciple,however,PETapter
dom selection from the total number of all pos- producesconsistentlymorereliableperformances
sible training examples and with stratified sam- inthesensethatthestandarddeviationofthescores
pling we ensure that the label distribution of the isconsistentlylowerforallsettings. Itcanbeseen
entire training set is replicated as accurately as thatevenforn = 100randomandstratifiedsampossible even in smaller samples. We create 5 plingleadtosimilarresults.
datasets for each combination of sampling strat- InTable5,wealsopresentlabel-specificperforegy (Equal, Random, Stratified) and number of mancescores(precision,recall,macro-F1)foreach
shots (n = 10,100,250), where we do not con- of the four classes in the dataset. Here, we focus
sider to random sample only 10 observations in onthepresentationoftheresultsforn = 250and
ordertoensureaminimumofoneobservationper thePfeifferadaptersasPEFTmethod. Theresults
labelinalltrainingsets. Table3providesthelabel oftherandomsamplingareshowninTable8inthe
distributions of the training and test dataset and Appendix. Itisoflittlesurprisethattherarestclass
thecorrespondingexpectednumbersunderrandom argumentagainstgeneratestheworstprecision,resamplingwithn = 100,250. call,andmacro-F1scoresinthestratifiedsampling.

<!-- Page 7 -->


### PETapter LinearLayer

n Sampling (IA)3 LoRA Pfeiffer PET (IA)3 LoRA Pfeiffer
10 Equal 0.28±.046 0.31±.043 0.33±.057 0.33±.080 0.14±.039 0.13±.042 0.15±.041
10 Stratified 0.19±.023 0.27±.039 0.33±.027 0.40±.055 0.16±.000 0.16±.001 0.17±.021
100 Equal 0.49±.023 0.57±.020 0.57±.028 0.59±.027 0.23±.041 0.26±.029 0.29±.030
100 Random 0.41±.036 0.56±.036 0.55±.036 0.56±.053 0.16±.000 0.20±.041 0.26±.037
100 Stratified 0.40±.029 0.58±.042 0.57±.035 0.59±.054 0.16±.000 0.20±.030 0.26±.035
250 Equal 0.57±.015 0.67±.014 0.68±.018 0.70±.025 0.28±.027 0.46±.050 0.49±.075
250 Random 0.50±.031 0.67±.021 0.67±.024 0.67±.109 0.16±.000 0.38±.031 0.45±.086
250 Stratified 0.48±.036 0.67±.019 0.67±.018 0.67±.109 0.16±.003 0.37±.040 0.46±.082
Table4: Meanmacro-F1scores(±standarddeviation)oftheexperimentsinthereal-worldstudy(Ukraine).

### EqualSampling StratifiedSampling

Label PETapter PET Lin.Layer PETapter PET Lin.Layer
noisicerP
argumentagainst 0.50±.031 0.51±.040 0.34±.068 0.54±.037 0.54±.122 0.39±.092
argumentfor 0.58±.045 0.63±.064 0.45±.075 0.64±.032 0.66±.145 0.47±.135
claimagainst 0.70±.033 0.71±.045 0.50±.078 0.68±.036 0.66±.143 0.49±.065
claimfor 0.87±.022 0.90±.023 0.69±.076 0.84±.022 0.83±.080 0.65±.064
llaceR
argumentagainst 0.75±.043 0.81±.061 0.46±.113 0.53±.064 0.57±.140 0.16±.098
argumentfor 0.66±.048 0.70±.047 0.65±.060 0.63±.053 0.61±.138 0.42±.147
claimagainst 0.75±.026 0.76±.051 0.51±.090 0.78±.028 0.75±.161 0.54±.121
claimfor 0.67±.034 0.67±.047 0.48±.121 0.78±.022 0.80±.051 0.74±.051
1F-orcaM argumentagainst 0.60±.029 0.62±.031 0.38±.082 0.53±.045 0.55±.123 0.22±.100
argumentfor 0.62±.026 0.66±.040 0.53±.061 0.63±.024 0.63±.134 0.44±.138
claimagainst 0.72±.019 0.73±.025 0.50±.072 0.72±.028 0.70±.148 0.51±.084
claimfor 0.76±.018 0.77±.031 0.56±.105 0.81±.012 0.81±.040 0.69±.049
Table5: Meanprecision,recall,andmacro-F1scoresperlabel(each±standarddeviation)oftheexperimentsinthe
real-worldstudy(Ukraine). WeconsiderthePfeifferadapterasthePEFTmethodofPETapterandn=250. We
omittheresultsusingrandomsamplingastheyarequitesimilartothoseofthestratifieddatasets,cf.Table8.
In the case of equal sampling, this remains true 6.4 PVP-Experiments
onlyfortheprecision;therecallcanbeincreased

### AmajorcriticismofPET-likemodelsistheneed

throughtheoversamplingforPETfrompreviously
formanualgenerationofpatternsandverbalizers.
51%tothethenhighestvalueofthefourclassesof
To address this, we tested the use of automated
81%. Thefactthatanequalsamplinginthetrain-
PVPs (No Pattern, Alpha verbalizer) and badly
ingsetleadstohigheroverallmacro-F1scoresand
chosen verbalizers (Shuffle). For reasons of comloweruncertaintythanastratifiedsamplingcanbe
plexity,welimittheexperimenttothecombination
explainedbythefactthatthecorrespondingrecall
ofLoRAandPETapter. AsaresultfromTable6,
valuesofotherwiserarelyoccurringclassescanbe
itcanbeconcludedthatthepatternshouldatbest
increasedinthisway.
be chosen manually, as there are notable differ-

### In general, PETapter provides the best overall

ences between the performances in all scenarios.
performance in this real-world study. While it

### However,thechoiceofverbalizerinourtaskhas

yieldsasimilarlevelofperformance,itproduces
hardlyanyinfluenceontheperformancealreadyfor
more reliable performance values overall. Thus,
n = 100. Infact,forNoPattern,Alphamostlyper-
PETapter makes the idea of PET easily accessiformsbetterthanthemanuallyselectedverbalizers,
bleinPEFTsettingswithoutlossofperformance.
whichmaybebecauseAlphaconsistsofonlyone
While PET on our system1 processes 7 observatokeneach,whiletheothertwoscenariosrequire
tionspersecond(obs/s)duringtrainingand8obs/s
twotokensperverbalizer. Moreover,Shuffledoes
duringtesting,PETapterprocesses25obs/sduring
not result in any noteworthy differences in labeltraining and 51 obs/s ((IA)3/LoRA) or 42 obs/s
specificperformancevaluescomparedtoNormal
(Pfeiffer) during testing. This shows a meaning-
(tablenotincludedduetospaceconstraints).
fulspeed-upofPETaptercomparedtoPETforthe
Asanextension,Table7indicatesthatacombitrainingaswellastheinferencephase.
nationofthefiverepetitionsusingamajorityvote
leadstosuperiorandmorestableresults. Inparticu-
148GB NVIDIA RTX 6000 Ada, Intel Xeon W7-3445
20×2.6GHz,256GBECCDDR5-4800RAM larinthescenariooflimitedhumanresources,this

<!-- Page 8 -->


### NoPattern Pattern

n Sampling Alpha Normal Shuffle Alpha Normal Shuffle
10 Equal 0.22±.039 0.25±.040 0.22±.039 0.23±.039 0.31±.043 0.28±.043
10 Stratified 0.20±.025 0.22±.031 0.22±.033 0.23±.067 0.27±.039 0.27±.043
100 Equal 0.47±.026 0.43±.041 0.41±.037 0.57±.041 0.57±.020 0.56±.033
100 Random 0.43±.046 0.39±.040 0.39±.043 0.53±.035 0.56±.036 0.54±.044
100 Stratified 0.40±.027 0.38±.035 0.37±.027 0.52±.051 0.58±.042 0.54±.048
250 Equal 0.62±.022 0.61±.024 0.60±.022 0.67±.021 0.67±.014 0.68±.019
250 Random 0.58±.035 0.57±.054 0.56±.054 0.65±.029 0.67±.021 0.66±.020
250 Stratified 0.60±.025 0.59±.030 0.58±.032 0.65±.019 0.67±.019 0.66±.017
Table6: Meanmacro-F1scores(±standarddeviation)ofthePVP-experimentsinthereal-worldstudy(Ukraine)
usingLoRAasPEFTmethodandPETapterasclassificationhead.
Data n PVP Mean Majority ple patterns as possible. Initial experiments have
AG 10 Manual 0.71±.080 0.71±.071 shownthatPETinparticularleadstopoorresults

### AG 100 Manual 0.87±.010 0.87±.009

withsmallnifthepatternistoocomplex. PETapter

### Yahoo 10 Manual 0.30±.044 0.32±.034

Yahoo 100 Manual 0.66±.013 0.66±.012 wasslightlymorerobustagainstthechoiceofpat-
Yelp 10 Manual 0.45±.055 0.45±.053 tern in these experiments. In addition, although

### Yelp 100 Manual 0.61±.013 0.62±.009

grammaticalcorrectnessofthepatternisdesirable,

### Ukraine 10 Manual 0.27±.039 0.27±.029

Ukraine 100 Manual 0.58±.042 0.59±.025 itisnotessentialtoachievesatisfactoryresults.

### Ukraine 250 Manual 0.67±.019 0.69±.018

Ukraine 10 Autom. 0.20±.025 0.20±.021 For the activation function, we decided to use
Ukraine 100 Autom. 0.40±.027 0.41±.018 GELU in combination with LayerNorm (cf. Fig-

### Ukraine 250 Autom. 0.60±.025 0.62±.025

ure1). Wewillfurtherinvestigatethisdecisionin
futurestudiesbyexaminingtheinfluenceofusing
Table7: Mean(majority)macro-F1scores(±standard
alternativeactivationfunctions.
deviation)usingLoRAandPETapter. ForUkraine,we
presenttheresultsusingtheStratifiedsampling.Manual
PVPmeansPromptpatternforAG,Yahoo,andYelp;
8 Conclusion
for Ukraine, it represents the combination of Pattern
using the Normal verbalizers, Autom. represents the
combinationofNoPatternandAlpha. WeshowthatournovelmethodPETaptercombines
theadvantagesoffew-shotlearningandparameterefficient fine-tuning (PEFT). PETapter combines
offersthepossibilityofboostingtheperformance
PEFTmethodswithPET-styleclassificationheads.
ofautomaticallyselectedPVPsbysimplystacking
Inthisway,itmakestheideaofPETeasilyaccesindependentrepetitions.
sibleinPEFTsettings. Asaresult,itachievesPET
performanceandincreasedreliabilityoftheresults
7 Discussion
while offering all the advantages of PEFT. It can
The results show that PET benefits greatly from betrainedfasterwithhigherparameterefficiency
equalsamplingwithunbalanceddata. Wewerenot andwithoutcatastrophicforgetting. Furthermore,
abletoachievethisgaintothesameextentusing itoffersamodularitythatmakesiteasiertoshare
PETapter. Therefore,eventhoughequalsampling models because the newly learned parameters reisnotarealisticscenarioin(few-shot)real-world quire,e.g.,only16MBcomparedto2.1GBofdisk
settings, it could be promising to develop PEFT space. DuetotheimplementationintheAdapters
methodsinsuchawaythattheybenefitfrombal- (Pothetal.,2023)framework, itallowseasyexeanceddataasmuchasPET.Moreover,asafollow- cution and combination with existing/new PEFT
upstudy,wewanttoinvestigatetowhatextentor methodslikeQLoRA(Dettmersetal.,2023),mixatwhatlevelofunbalancednessitisworthsimply ture of experts models (Zadouri et al., 2024), or
omittingobservationsfromastratifiedsamplingin others(cf.Section2.1). Ourmethodmakeshighordertoobtainamorebalancedtrainingset. performingtextclassification—whichisbeneficial
Following the mathematical definition of tomanyresearchdomainswherelabeledtextisa
PETapter (cf. Equation 1), it is recommended to valuableresource—feasibleformoreresearchers,
alwaysusethesamenumberofverbalizertokens byloweringthetechnologicalboundariestoaccessforeachclass. Wealsorecommendusingassim- inglanguagemodels.

<!-- Page 9 -->

Acknowledgements AlexisConneau,KartikayKhandelwal,NamanGoyal,

### Vishrav Chaudhary, Guillaume Wenzek, Francisco

ThisworkwasfundedbytheBundesministerium Guzmán, Edouard Grave, Myle Ott, Luke Zettlefür Bildung und Forschung (BMBF) as part of moyer,andVeselinStoyanov.2020. Unsupervised
cross-lingualrepresentationlearningatscale. InProthe project FLACA: Few-shot learning for autoceedings of the 58th Annual Meeting of the Assomatedcontentanalysisincommunicationscience
ciationforComputationalLinguistics,pages8440–
(projectno.16DKWN064B)andbytheDeutsche 8451, Online. Association for Computational Lin-
Forschungsgemeinschaft (DFG) as part of the guistics.
projectFAME:Aframeworkforargumentmining
Tim Dettmers, Artidoro Pagnoni, Ari Holtzman, and
and evaluation (project no. 406289255). In addi-
LukeZettlemoyer.2023. QLoRA:Efficientfinetuntion, we acknowledge the computation resources ingofquantizedLLMs.
facilitatedbyseedfundingfromtheResearchCen-
JunxianHe,ChuntingZhou,XuezheMa,TaylorBergterTrustworthyDataScienceandSecurityaspart

### Kirkpatrick,andGrahamNeubig.2022. Towardsa

oftheprojectTrustworthyperformanceevaluation
unifiedviewofparameter-efficienttransferlearning.
oflargelanguagemodels. InInternationalConferenceonLearningRepresentations.

### Limitations

PengchengHe,JianfengGao,andWeizhuChen.2023.
AsmentionedinSections7and8,notallpromising DeBERTav3:ImprovingDeBERTausingELECTRA-
stylepre-trainingwithgradient-disentangledembedmodelsandcombinationsofmodelingredientscan
dingsharing. InTheEleventhInternationalConferbeevaluated. Therefore,itisexpectedthatbetter enceonLearningRepresentations.
performance scores can be achieved by optimiz-
Neil Houlsby, Andrei Giurgiu, Stanislaw Jastrzebski,
ingthecombinationofallmentionedingredients,
Bruna Morrone, Quentin De Laroussilhe, Andrea
cf.Section2. Instead,weshowthatthePETapter
Gesmundo,MonaAttariyan,andSylvainGelly.2019.
ideaisapromisingmethodoverall,iftheunderly- Parameter-efficient transfer learning for NLP. In
ing task is possible to formulate as classification Proceedings of the 36th International Conference
tasks. Inaddition,ouranalysesarelimitedtofour on Machine Learning, volume 97 of Proceedings
of Machine Learning Research, pages 2790–2799.
data sets (also for reasons of sustainable NLP),

## Pmlr.

whicharerestrictedtothelanguagesEnglishand
German. In return, we pay a lot of attention to a Edward J. Hu, Yelong Shen, Phillip Wallis, Zeyuan

### Allen-Zhu,YuanzhiLi,SheanWang,LuWang,and

reliableevaluationthrough5repetitions×5sam-

### WeizhuChen.2021. LoRA:Low-rankadaptationof

pleddatasetsforeachoftheconsideredscenarios
largelanguagemodels.
inSections5and6.
Shengding Hu, Ning Ding, Weilin Zhao, Xingtai Lv,
ZhenZhang,ZhiyuanLiu,andMaosongSun.2023a.
References OpenDelta: Aplug-and-playlibraryforparameterefficient adaptation of pre-trained models. In Pro-
Neel Alex, Eli Lifland, Lewis Tunstall, Abhishek ceedings of the 61st Annual Meeting of the Asso-
Thakur, Pegah Maham, C. Jess Riedel, Emmie ciation for Computational Linguistics (Volume 3:
Hine, Carolyn Ashurst, Paul Sedille, Alexis Car- System Demonstrations), pages 274–281, Toronto,
lier,MichaelNoetel,andAndreasStuhlmüller.2021. Canada.AssociationforComputationalLinguistics.

### RAFT: A real-world few-shot text classification

benchmark. In Thirty-fifth Conference on Neural Zhiqiang Hu, Lei Wang, Yihuai Lan, Wanyu Xu, Ee-
InformationProcessingSystemsDatasetsandBench- PengLim,LidongBing,XingXu,SoujanyaPoria,
marksTrack(Round2). and Roy Lee. 2023b. LLM-adapters: An adapter
family for parameter-efficient fine-tuning of large
Nadav Benedek and Lior Wolf. 2024. PRILoRA: languagemodels. InProceedingsofthe2023Con-
Prunedandrank-increasinglow-rankadaptation. In ferenceonEmpiricalMethodsinNaturalLanguage
FindingsoftheAssociationforComputationalLin- Processing,pages5254–5276,Singapore.Associaguistics: EACL 2024, pages 252–263, St. Julian’s, tionforComputationalLinguistics.
Malta.AssociationforComputationalLinguistics.

### YongxinHuang,KexinWang,SouravDutta,RajPatel,

Canyu Chen and Kai Shu. 2023. PromptDA: Label- GoranGlavaš,andIrynaGurevych.2023. AdaSent:
guideddataaugmentationforprompt-basedfewshot Efficientdomain-adaptedsentenceembeddingsfor
learners. InProceedingsofthe17thConferenceof few-shotclassification. InProceedingsofthe2023
the European Chapter of the Association for Com- Conference on Empirical Methods in Natural LanputationalLinguistics, pages562–574, Dubrovnik, guageProcessing,pages3420–3434,Singapore.As-
Croatia.AssociationforComputationalLinguistics. sociationforComputationalLinguistics.

<!-- Page 10 -->

Hendrik Hüning, Lydia Mechtenberg, and Stephanie JonasPfeiffer,AndreasRücklé,CliftonPoth,Aishwarya
Wang.2022. Detectingargumentsandtheirpositions Kamath, Ivan Vulic´, Sebastian Ruder, Kyunghyun
in experimental communication data. Available at Cho, and Iryna Gurevych. 2020. AdapterHub: A
SSRN. frameworkforadaptingtransformers. InProceedings
ofthe2020ConferenceonEmpiricalMethodsinNat-
LenaJurkschat,GregorWiedemann,MaximilianHein- uralLanguageProcessing: SystemDemonstrations,
rich, Mattes Ruckdeschel, and Sunna Torge. 2022. pages46–54,Online.AssociationforComputational
Few-shotlearningforargumentaspectsofthenuclear Linguistics.
energydebate. InProceedingsoftheThirteenthLanguageResourcesandEvaluationConference,pages Jonas Pfeiffer, Sebastian Ruder, Ivan Vulic´, and
663–672,Marseille,France.EuropeanLanguageRe- EdoardoMariaPonti.2023. Modulardeeplearning.
sourcesAssociation.

### CliftonPoth,HannahSterz,IndraneilPaul,Sukannya

Rabeeh Karimi Mahabadi, Luke Zettlemoyer, James Purkayastha, Leon Engländer, Timo Imhof, Ivan
Henderson, Lambert Mathias, Marzieh Saeidi, Vulic´,SebastianRuder,IrynaGurevych,andJonas
VeselinStoyanov,andMajidYazdani.2022. Prompt- Pfeiffer. 2023. Adapters: A unified library for
free and efficient few-shot learning with language parameter-efficientandmodulartransferlearning. In
models. In Proceedings of the 60th Annual Meet- Proceedings of the 2023 Conference on Empirical
ingoftheAssociationforComputationalLinguistics Methods in Natural Language Processing: System
(Volume1: LongPapers),pages3638–3652,Dublin, Demonstrations,pages149–160,Singapore.Associa-
Ireland.AssociationforComputationalLinguistics. tionforComputationalLinguistics.
DawidJanKopiczko,TijmenBlankevoort,andYukiM Sylvestre-Alvise Rebuffi, Hakan Bilen, and Andrea
Asano. 2024. VeRA: Vector-based random matrix Vedaldi. 2017. Learning multiple visual domains
adaptation. InTheTwelfthInternationalConference with residual adapters. In Advances in Neural InonLearningRepresentations. formation Processing Systems, volume 30. Curran
Associates,Inc.
Changmao Li and Jeffrey Flanigan. 2024. Task contamination: Languagemodelsmaynotbefew-shot JonasRieger,KostiantynYanchenko,MattesRuckdeanymore. ProceedingsoftheAAAIConferenceon schel,GerretvonNordheim,KatharinaKleinen-von
ArtificialIntelligence,38(16):18471–18480. Königslöw,andGregorWiedemann.2023. Few-shot
learning for automated content analysis (FLACA)
TongtaoLing, LeiChen, YutaoLai, andHai-LinLiu. in the German media debate on arms deliveries to

## Evolutionary verbalizer search for prompt- Ukraine. InDigitalTotal,page19.

based few shot text classification. In Knowledge
Science,EngineeringandManagement,pages279– JonasRieger,KostiantynYanchenko,MattesRuckde-
290,Cham.SpringerNatureSwitzerland. schel,GerretvonNordheim,KatharinaKleinen-von

### Königslöw,andGregorWiedemann.2024. Few-shot

HaokunLiu,DerekTam,MohammedMuqeeth,JayMo- learning for automated content analysis: Efficient
hta,TenghaoHuang,MohitBansal,andColinARaf- codingofargumentsandclaimsinthedebateonarms
fel.2022. Few-shotparameter-efficientfine-tuning deliveriestoUkraine. StudiesinCommunicationand
is better and cheaper than in-context learning. In Media,13:72–100.
AdvancesinNeuralInformationProcessingSystems,

### Mohammed Sabry and Anya Belz. 2023. PEFT-Ref:

volume 35, pages 1950–1965. Curran Associates,
A modular reference architecture and typology for
Inc.
parameter-efficientfinetuningtechniques.

### Shih-Yang Liu, Chien-Yi Wang, Hongxu Yin, Pavlo

Victor Sanh, Albert Webson, Colin Raffel, Stephen

### Molchanov, Yu-Chiang Frank Wang, Kwang-Ting

Bach, Lintang Sutawika, Zaid Alyafeai, Antoine

### Cheng,andMin-HungChen.2024. DoRA:Weight-

Chaffin, Arnaud Stiegler, Arun Raja, Manan Dey,
decomposedlow-rankadaptation.

### M Saiful Bari, Canwen Xu, Urmish Thakker,

YinhanLiu,MyleOtt,NamanGoyal,JingfeiDu,Man- ShanyaSharmaSharma,ElizaSzczechla,Taewoon
dar Joshi, Danqi Chen, Omer Levy, Mike Lewis, Kim, Gunjan Chhablani, Nihal Nayak, Debajyoti
Luke Zettlemoyer, and Veselin Stoyanov. 2019. Datta,JonathanChang,MikeTian-JianJiang,Han
RoBERTa: Arobustlyoptimizedbertpretrainingap- Wang,MatteoManica,ShengShen,ZhengXinYong,
proach. HarshitPandey,RachelBawden,ThomasWang,Trishala Neeraj, Jos Rozen, Abheesht Sharma, An-
Sourab Mangrulkar, Sylvain Gugger, Lysandre De- dreaSantilli,ThibaultFevry,JasonAlanFries,Ryan
but, Younes Belkada, Sayak Paul, and Benjamin Teehan,TevenLeScao,StellaBiderman,LeoGao,
Bossan. 2022. PEFT: State-of-the-art parameter- ThomasWolf,andAlexanderMRush.2022. Multiefficient fine-tuning methods. https://github. taskpromptedtrainingenableszero-shottaskgenercom/huggingface/peft. alization. InInternationalConferenceonLearning
Representations.

### Mahdi Nikdan, Soroush Tabesh, Elvir Crncˇevic´, and

Dan Alistarh. 2024. RoSA: Accurate parameter- Timo Schick and Hinrich Schütze. 2021. Exploiting
efficientfine-tuningviarobustadaptation. cloze-questionsforfew-shottextclassificationand

<!-- Page 11 -->

natural language inference. In Proceedings of the thepackageAdapter(Pothetal.,2023),weusethe
16thConferenceoftheEuropeanChapteroftheAsso- parameters
ciationforComputationalLinguistics: MainVolume,
• c_rate=16(Pfeiffer),
pages 255–269, Online. Association for Computa-
• r=8(LoRA),
tionalLinguistics.
• alpha=16(LoRA),
TimoSchickandHinrichSchütze.2022. Truefew-shot • learning_rate=5.0e-5,
learning with Prompts—A real-world perspective.
• max_epochs=30,

### TransactionsoftheAssociationforComputational

Linguistics,10:716–731. • per_device_train_batch_size=2
andalternatearchwithia3,lora,andpfeiffer.
LewisTunstall,NilsReimers,UnsoEunSeoJo,Luke

### Thepatternsinthefollowingsubsectionsaremo-


### Bates, Daniel Korat, Moshe Wasserblat, and Oren

tivated by the results of the study of Schick and

### Pereg. 2022. Efficient few-shot learning without

prompts. Schütze(2022). Duetothelimitedinputlengthof

### PLMs,potentialtruncationsoftheinputelements


### Thomas Wolf, Lysandre Debut, Victor Sanh, Julien

in the pattern are indicated with *, potentially as
Chaumond,ClementDelangue,AnthonyMoi,Piergroupwithin{}brackets.
ricCistac,TimRault,RemiLouf,MorganFuntowicz,JoeDavison,SamShleifer,PatrickvonPlaten,

### A.1 AG’sNews


### Clara Ma, Yacine Jernite, Julien Plu, Canwen Xu,

Teven Le Scao, Sylvain Gugger, Mariama Drame, ThisEnglishlanguagedatasetisavailableathttps:
QuentinLhoest,andAlexanderRush.2020. Trans-
//huggingface.co/datasets/ag_news (Zhang
formers:State-of-the-artnaturallanguageprocessing.
InProceedingsofthe2020ConferenceonEmpirical et al., 2015) and consists of 120 thousand train-
Methods in Natural Language Processing: System ingand7.6thousandtestobservations.

### Demonstrations,pages38–45,Online.Association

forComputationalLinguistics. PromptPattern [MASK]News: [text]*
PrateekYadav,LeshemChoshen,ColinRaffel,andMo-

### Q&APattern [text]* [SEP] Question: What is

hitBansal.2023. ComPEFT:Compressionforcomthetopicofthisarticle? Answer: [MASK].
municatingparameterefficientupdatesviasparsificationandquantization.

### Verbalizers

TedZadouri,AhmetÜstün,ArashAhmadian,BeyzaEr-

### World World

mis,AcyrLocatelli,andSaraHooker.2024. Pushing
mixtureofexpertstothelimit: Extremelyparameter Sports Sports
efficientmoeforinstructiontuning. InTheTwelfth

### Business Business

International Conference on Learning Representations. Sci/Tech Tech
HaoxingZhang,XiaofengZhang,HaiboHuang,andLei A.2 YahooQuestions

### Yu.2022. Prompt-basedmeta-learningforfew-shot

textclassification. InProceedingsofthe2022Con- This English language dataset is available
ferenceonEmpiricalMethodsinNaturalLanguage at https://huggingface.co/datasets/yahoo_
Processing, pages 1342–1357, Abu Dhabi, United answers_topics(Zhangetal.,2015)andconsists
ArabEmirates.AssociationforComputationalLinof1.4milliontrainingand60thousandtestobserguistics.
vations.
XiangZhang,JunboJakeZhao,andYannLeCun.2015.
Character-levelconvolutionalnetworksfortextclas- PromptPattern [MASK] Question: {[questionsification. InNIPS. _title][question_content][best_answer]}*
A DetailsofBenchmarkStudy Q&APattern {[question_title] [question_content] [best_answer]}* [SEP] Question:

### For the benchmark study, we compare

What is the topic of this question? Answer:
the use of “roberta-base” and “roberta-

## [Mask].

large” from HuggingFace’s Transformers
(Wolf et al., 2020). For PET (https: Verbalizers
//github.com/timoschick/pet), we use

### Society&Culture Society

the two parameters pet_num_train_epochs=10
and pet_per_gpu_train_batch_size=1 that Science&Mathematics Science
differfromthedefault. Forallexperimentsusing Health Health

<!-- Page 12 -->

Education&Reference Education andalternatearchwithia3,lora,andpfeiffer.
Computers&Internet Computer DuetothelimitedinputlengthofPLMs,potentialtruncationsoftheinputelementsinthepattern

### Sports Sports

are indicated with *, potentially as group within

### Business&Finance Business

{} brackets. We place the target sentence at the

### Entertainment&Music Entertainment

beginningtoensurethatitisnevertruncateddueto
Family&Relationships Relationship restrictionsregardingthemodel’sinputlengthof
Politics&Government Politics 512tokens. Experimentswithtarget_sentencein
themiddlereturnedslightlyworseresults. Inthe
sameway,experimentswithanequivalentGerman

### A.3 YelpFull

patternyieldslightlyworseresults.

### This English language dataset is available

at https://huggingface.co/datasets/yelp_ Pattern This sentence contains [MASK]
review_full(Zhangetal.,2015)andconsistsof [MASK] arms deliveries to Ukraine: {[tar-
650thousandtrainingand50thousandtestobser- get_sentence][SEP][context_before][SEP]
vations. [context_after]}*

### NoPattern [MASK][MASK]:{[target_sentence]

PromptPattern [text]* [SEP] All in all, it was
[SEP] [context_before] [SEP] [con-

## [Mask].

text_after]}*
Q&APattern [text]*[SEP]Question: Whatdoes

### AlphaVerbalizers

thecustomerthinkofthisrestaurant? Answer:
Thealphanumericverbalizersonlyconsistof

## [Mask].

one token each, so that in this case the used
Verbalizers patternisreducedtoone[MASK]tokenonly.
1star terrible argumentagainst a
argumentfor b
2stars bad
claimagainst c
3stars okay
claimfor d
4stars good
nostance e
5stars great

### NormalVerbalizers


### B DetailsoftheReal-WorldStudy

argumentagainst argumentagainst
Thedatasetwillbemadeavailabletoresearchers
argumentfor argumentfor
after acceptance of the paper. Since this
claimagainst claimagainst
dataset is in German language, we use “xlmroberta-large” from HuggingFace’s Transform- claimfor claimfor
ers (Wolf et al., 2020). For PET (https: nostance nothingregarding
//github.com/timoschick/pet), we use the

### ShuffleVerbalizers

two parameters pet_num_train_epochs=10 and
pet_per_gpu_train_batch_size=1 (for a fair argumentagainst claimfor
training time comparison in Table 2, we use
argumentfor claimagainst
pet_per_gpu_train_batch_size=2) that differ
claimagainst nothingregarding
from the default. For all experiments using the
claimfor argumentagainst
package Adapter (Poth et al., 2023), we use the
nostance argumentfor
parameters
• c_rate=16(Pfeiffer),
C RAFTBenchmark
• r=8(LoRA),
• alpha=16(LoRA), TheRAFTLeaderboard(Alexetal.,2021,https:
• learning_rate=5.0e-5, //raft.elicit.org/) has been under mainte-
• max_epochs=30, nanceforsometimenow. Wemadeasubmission
• per_device_train_batch_size=2 awhileago,butunfortunatelystillgotnoscore. If

<!-- Page 13 -->


### RandomSampling StratifiedSampling

Label PETapter PET Lin.Layer PETapter PET Lin.Layer
noisicerP
argumentagainst 0.57±.042 0.57±.126 0.37±.228 0.54±.037 0.54±.122 0.39±.092
argumentfor 0.64±.050 0.66±.141 0.45±.117 0.64±.032 0.66±.145 0.47±.135
claimagainst 0.68±.030 0.66±.141 0.52±.063 0.68±.036 0.66±.143 0.49±.065
claimfor 0.81±.027 0.81±.077 0.65±.065 0.84±.022 0.83±.080 0.65±.064
llaceR
argumentagainst 0.51±.059 0.53±.147 0.12±.093 0.53±.064 0.57±.140 0.16±.098
argumentfor 0.61±.056 0.61±.140 0.42±.169 0.63±.053 0.61±.138 0.42±.147
claimagainst 0.75±.039 0.74±.157 0.54±.175 0.78±.028 0.75±.161 0.54±.121
claimfor 0.80±.029 0.82±.047 0.76±.054 0.78±.022 0.80±.051 0.74±.051
1F-orcaM argumentagainst 0.53±.037 0.55±.128 0.16±.109 0.53±.045 0.55±.123 0.22±.100
argumentfor 0.62±.046 0.63±.134 0.43±.142 0.63±.024 0.63±.134 0.44±.138
claimagainst 0.71±.025 0.70±.146 0.52±.124 0.72±.028 0.70±.148 0.51±.084
claimfor 0.81±.016 0.81±.039 0.70±.036 0.81±.012 0.81±.040 0.69±.049
Table8: Meanprecision,recall,andmacro-F1scoresperlabel(each±standarddeviation)oftheexperimentsinthe
real-worldstudy(Ukraine). WeconsiderthePfeifferadapterasthePEFTmethodofPETapterandn = 250. In
additiontotheresultsfromTable5,wepresenttheresultsofrandomsamplingincomparisontostratifiedsampling.
thescoresarepublishedduringthereviewprocess, C.2 banking_77
we will include a table with comparative values

### Fortheprocessingofthebanking_77dataset,some

forT-Few(Liuetal.,2022),Setfit(Tunstalletal.,
preprocessingisnecessary. Asthereareonly50ob-
2022), PET (Schick and Schütze, 2021) and the
servationsineachofthetrainingsetsoftheRAFT
humanbaselineatthispoint.
setting,butatthesametimethereare77different
The 11 datasets of RAFT are in English lanclasses in this specific dataset, the model misses
guage and available at https://huggingface.
27oftheclassesinthetrainingset. Toovercome
co/datasets/ought/raft. We use the model
this,weaugmentthetrainingdatasuchthateachof
“microsoft/deberta-v2-xxlarge” from Huggingthe50observationsiscombinedwithall77classes

### Face’s Transformers (Wolf et al., 2020) and for

using the yes/no pattern below. As a result, the
all11datasetstheparameters
27classesthatwerepreviouslynotincludedinthe
• arch=lora,
trainingdatanowbecomepartiteach50timesin
• r=8,
combinationwiththelabelno.
• alpha=16,
• learning_rate=5.0e-5,
Pattern Thefollowingisabankingcustomerser-
• max_epochs=30,
vicequery. [SEP]{[Query][SEP]Is[Label]}*
• per_device_train_batch_size=2,
thecorrectcategoryforthisquery? Answer:
• number_of_runs=5,

## [Mask].

where we select the majority vote out of the five
runsasthefinalsubmission.

### Verbalizers


### The patterns in the following subsections are

motivatedbytheresultsofthestudyofSchickand No No
Schütze(2022). Duetothelimitedinputlengthof

### Yes Yes


### PLMs,potentialtruncationsoftheinputelements

inthepatternsareindicatedwith*,potentiallyas
C.3 neurips_impact_statement_risks
groupwithin{}brackets.

### Pattern {Title: [Papertitle][SEP]Statement: [Im-

C.1 ade_corpus_v2 pactstatement]}*[SEP]Question: Doesthis
impactstatementmentionaharmfulapplica-
Pattern [Sentence]*[SEP]Question: Isthissention? Answer: [MASK].
tencerelatedtoanadversedrugeffect(ADE)?
Answer: [MASK].
Verbalizers

### Verbalizers

doesn’tmentionaharmfulapplication
notADE-related No No
ADE-related Yes mentionsaharmfulapplication Yes

<!-- Page 14 -->

C.4 one_stop_english industrialrevolution[SEP]{Journal: [Publication Title] [SEP] Title: [Title] [SEP] Ab-
Pattern [Article]* [SEP] Question: Is the level
stract: [AbstractNote]}*[SEP]Question: Is
ofthisarticle’elementary’,’intermediate’or
this paper a TAI safety research paper? An-
’advanced’? Answer: [MASK].
swer: [MASK].
Verbalizers

### Verbalizers

elementary elementary
notTAIsafetyresearch No
intermediate intermediate
TAIsafetyresearch Yes
advanced advanced

### C.9 terms_of_service


### C.5 overruling Pattern ThefollowingsentenceisfromaTermsof

Pattern In law, an overruling sentence is a state- Service. [SEP][Sentence]*[SEP]Question:
mentthatnullifiesapreviouscasedecisionas Is this sentence potentially unfair? Answer:
aprecedent. [SEP][Sentence]*[SEP]Ques- [MASK].
tion: Is this sentence overruling? Answer:
Verbalizers

## [Mask].

notpotentiallyunfair No

### Verbalizers

potentiallyunfair Yes
notoverruling No
C.10 tweet_eval_hate
overruling Yes
Pattern [Tweet]*[SEP]Question: Doesthistweet
containhatespeechagainsteitherimmigrants
C.6 semiconductor_org_types
orwomen? Answer: [MASK].

### Pattern {Title: [Paper title] [SEP] Organization

name: [Organization name]}* [SEP] Ques- Verbalizers
tion: Whatisthecategoryofthisinstitution? nothatespeech No
Answer: [MASK].
hatespeech Yes

### Verbalizers C.11 twitter_complaints

company Company Pattern [Tweettext]*[SEP]Question: Doesthis
tweetcontainacomplaint? Answer: [MASK].
researchinstitute Institute
university University Verbalizers
nocomplaint No
C.7 systematic_review_inclusion
complaint Yes

### Pattern {Journal: [Journal] [SEP] Title: [Title]

[SEP] Abstract: [Abstract]}* [SEP] Ques- D GPTComparison
tion: Shouldthispaperbeincludedinameta-

### AdifferentversionoftheUkrainedataset,inwhich

review which includes the findings of sysnotonlythefourclassesoutlinedinthispaperare
tematic reviews on interventions designed
considered,butalsoirrelevant sentencesareconto promote charitable donations? Answer:
tained,isstudiedbyRiegeretal.(2023)inacom-

## [Mask].

parisonbetweenfullfine-tuningmethods,PETand
Verbalizers PEFT methods. The authors show that PETapter
already with only 272 observations outperforms
notincluded No
zero-shotGPT-4. Theauthorsfurtherobservethat
included Yes GPT-4performsbetteronthisreal-worldandunpublisheddatasetinazero-shotmannerthanusing

### C.8 tai_safety_research

anin-contextlearningpromptwithfew(upto10)
Pattern TransformativeAI(TAI)isdefinedasAI examples. Moreover,theyfoundoutthatGPT-3.5
that precipitates a transition comparable to performs significantly worse than GPT-4 on this
(ormoresignificantthan)theagriculturalor task.

## Tables

**Table (Page 5):**

| 0.668 0.681 0.683 ±.092 ±.080 ±.078 | 0.804 ±.036 | 0.596 0.672 0.680 ±.077 ±.077 ±.088 | 0.800 ±.028 |
|---|---|---|---|
| 0.236 0.292 0.271 ±.016 ±.033 ±.042 | 0.545 ±.040 | 0.274 0.295 0.285 ±.026 ±.041 ±.036 | 0.515 ±.036 |
| 0.403 0.434 0.423 ±.037 ±.035 ±.038 | 0.441 ±.017 | 0.359 0.412 0.390 ±.037 ±.042 ±.047 | 0.442 ±.025 |
| 0.856 0.861 0.860 ±.012 ±.012 ±.012 | 0.875 ±.007 | 0.863 0.861 0.862 ±.006 ±.010 ±.011 | 0.871 ±.008 |
| 0.622 0.642 0.642 ±.018 ±.009 ±.011 | 0.666 ±.007 | 0.622 0.637 0.633 ±.005 ±.007 ±.008 | 0.659 ±.007 |
| 0.541 0.553 0.551 ±.010 ±.018 ±.016 | 0.552 ±.014 | 0.536 0.553 0.548 ±.014 ±.015 ±.014 | 0.554 ±.015 |
| 0.641 0.714 0.702 ±.100 ±.070 ±.081 | 0.842 ±.025 | 0.611 0.746 0.738 ±.073 ±.054 ±.060 | 0.836 ±.032 |
| 0.242 0.331 0.290 ±.027 ±.040 ±.056 | 0.574 ±.030 | 0.323 0.365 0.346 ±.049 ±.049 ±.054 | 0.550 ±.040 |
| 0.442 0.470 0.479 ±.040 ±.041 ±.035 | 0.475 ±.026 | 0.440 0.472 0.490 ±.049 ±.049 ±.046 | 0.486 ±.041 |
| 0.868 0.873 0.875 ±.011 ±.010 ±.010 | 0.877 ±.009 | 0.876 0.870 0.873 ±.009 ±.010 ±.010 | 0.874 ±.009 |
| 0.654 0.662 0.661 ±.020 ±.014 ±.017 | 0.680 ±.013 | 0.655 0.654 0.656 ±.010 ±.008 ±.012 | 0.675 ±.013 |
| 0.611 0.613 0.614 ±.011 ±.014 ±.010 | 0.593 ±.014 | 0.626 0.622 0.620 ±.008 ±.013 ±.013 | 0.595 ±.016 |


**Table (Page 7):**

| 0.28±.046 0.31±.043 0.33±.057 0.19±.023 0.27±.039 0.33±.027 | 0.33±.080 0.40±.055 |
|---|---|
| 0.49±.023 0.57±.020 0.57±.028 0.41±.036 0.56±.036 0.55±.036 0.40±.029 0.58±.042 0.57±.035 | 0.59±.027 0.56±.053 0.59±.054 |
| 0.57±.015 0.67±.014 0.68±.018 0.50±.031 0.67±.021 0.67±.024 0.48±.036 0.67±.019 0.67±.018 | 0.70±.025 0.67±.109 0.67±.109 |


**Table (Page 7):**

| 0.50±.031 0.51±.040 0.34±.068 0.58±.045 0.63±.064 0.45±.075 0.70±.033 0.71±.045 0.50±.078 0.87±.022 0.90±.023 0.69±.076 |
|---|
| 0.75±.043 0.81±.061 0.46±.113 0.66±.048 0.70±.047 0.65±.060 0.75±.026 0.76±.051 0.51±.090 0.67±.034 0.67±.047 0.48±.121 |
| 0.60±.029 0.62±.031 0.38±.082 0.62±.026 0.66±.040 0.53±.061 0.72±.019 0.73±.025 0.50±.072 0.76±.018 0.77±.031 0.56±.105 |


**Table (Page 8):**

| 0.22±.039 0.25±.040 0.22±.039 0.20±.025 0.22±.031 0.22±.033 |
|---|
| 0.47±.026 0.43±.041 0.41±.037 0.43±.046 0.39±.040 0.39±.043 0.40±.027 0.38±.035 0.37±.027 |
| 0.62±.022 0.61±.024 0.60±.022 0.58±.035 0.57±.054 0.56±.054 0.60±.025 0.59±.030 0.58±.032 |


**Table (Page 13):**

| 0.57±.042 0.57±.126 0.37±.228 0.64±.050 0.66±.141 0.45±.117 0.68±.030 0.66±.141 0.52±.063 0.81±.027 0.81±.077 0.65±.065 |
|---|
| 0.51±.059 0.53±.147 0.12±.093 0.61±.056 0.61±.140 0.42±.169 0.75±.039 0.74±.157 0.54±.175 0.80±.029 0.82±.047 0.76±.054 |
| 0.53±.037 0.55±.128 0.16±.109 0.62±.046 0.63±.134 0.43±.142 0.71±.025 0.70±.146 0.52±.124 0.81±.016 0.81±.039 0.70±.036 |
