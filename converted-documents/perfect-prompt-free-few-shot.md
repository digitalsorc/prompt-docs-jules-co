---
title: "PERFECT Prompt Free Few Shot"
original_file: "./PERFECT_Prompt_Free_Few_Shot.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["prompt-engineering", "llm", "rag", "chain-of-thought", "fine-tuning"]
keywords: ["mask", "perfect", "tuning", "few", "verbalizers", "shot", "learning", "adapters", "efficient", "prompt"]
summary: "<!-- Page 1 -->


## Perfect:

Prompt-free and Efficient Few-shot Learning with Language Models
RabeehKarimiMahabadi1,3,4 LukeZettlemoyer1,2 JamesHenderson4
MarziehSaeidi1 LambertMathias1 VeselinStoyanov1 MajidYazdani1
1MetaAI 2UniversityofWashington 3EPFL 4IdiapResearchInstitute
{rabeeh.karimi, james.henderson}@idiap.ch
lsz@cs.washington.edu
{marzieh,mathiasl,ves,myazdani}@fb.com

### Abstract

Labels Verbalizers
positive great
Currentmethodsforfew-shotfine-tuningofpre-

### MLM Head

trainedma"
related_documents: []
---

# PERFECT Prompt Free Few Shot

<!-- Page 1 -->


## Perfect:

Prompt-free and Efficient Few-shot Learning with Language Models
RabeehKarimiMahabadi1,3,4 LukeZettlemoyer1,2 JamesHenderson4
MarziehSaeidi1 LambertMathias1 VeselinStoyanov1 MajidYazdani1
1MetaAI 2UniversityofWashington 3EPFL 4IdiapResearchInstitute
{rabeeh.karimi, james.henderson}@idiap.ch
lsz@cs.washington.edu
{marzieh,mathiasl,ves,myazdani}@fb.com

### Abstract

Labels Verbalizers
positive great
Currentmethodsforfew-shotfine-tuningofpre-

### MLM Head

trainedmaskedlanguagemodels(PLMs)require negative terrible
carefully engineered prompts and verbalizers

### Pretrained Language Model

for each new task to convert examples into a

### Input Pattern

cloze-format that the PLM can score. In this
[CLS] The restaurant had excellent foods. It was [MASK] [SEP]
work, we propose PERFECT, a simple and efficient method for few-shot fine-tuning of PLMs
Figure 1: Existing few-shot fine-tuning methods require
withoutrelyingonanysuchhandcrafting,which
manual engineering to reduce new tasks to masked lanishighlyeffectivegivenasfewas32datapoints.
guagemodeling.PERFECTdoesnotrelyonanyhandcraft-

### PERFECT makes two key design choices: First,

ing,removingbothpatternsandverbalizers(seeFigure3).
weshowthatmanuallyengineeredtaskprompts
can be replaced with task-specific adapters that
enable sample-efficient fine-tuning and reduce
not needed for few-shot learning and instead can
memory and storage costs by roughly factors
be replaced with simple methods for data-efficient
of 5 and 100, respectively. Second, instead of
fine-tuningwithasfewas32end-taskexamples.
using handcrafted verbalizers, we learn new
multi-tokenlabelembeddingsduringfine-tuning,

### More specifically, we propose PERFECT, a

which are not tied to the model vocabulary and Prompt-free and Efficient paRadigm for FEw-shot
whichallowustoavoidcomplexauto-regressive Cloze-based fine-Tuning. To remove handcrafted
decoding. These embeddings are not only patterns,PERFECTusestask-specificadapterlayers
learnable from limited data but also enable (Houlsby et al., 2019; Pfeiffer et al., 2020) (§3.1).
nearly100xfastertrainingandinference. Exper-
FreezingtheunderlyingPLMwithmillionsorbillions
iments on a wide range of few shot NLP tasks
ofparameters(Liu etal.,2019;Raffeletal., 2020),
demonstrate that PERFECT, while being simple
andonlytuningadapterswithveryfewnewparamand efficient, also outperforms existing state-ofthe-art few-shot learning methods. Our code is eterssavesonmemoryandstoragecosts(§4.2),while
publiclyavailableathttps://github.com/ allowing very sample-efficient tuning (§4). It also
facebookresearch/perfect.git. stabilizes the training by increasing the worst-case
performance and decreasing variance across the
1 Introduction
choiceofexamplesinthefewshottrainingsets(§4.3).
Recent methods for few-shot language model Toremovehandcraftedverbalizers(withvariable
tuning obtain impressive performance but require token lengths), we introduce a new multi-token
careful engineering of prompts and verbalizers to fixed-length classifier scheme that learns task label
convertinputstoacloze-format(Taylor,1953)that embeddingswhichareindependentfromthelanguage
can be scored with pre-trained language models model vocabulary during fine-tuning (§3.2). We
(PLMs)(Radfordetal.,2018;Radfordetal.;Brown show (§4) that this approach is sample efficient
et al., 2020; Schick and Schütze, 2021a,b). For and outperforms carefully engineered verbalizers
example,asFigure1shows,asentimentclassifiercan from random initialization (§4). It also allows us
bedesignedbyinsertingtheinputtextxinaprompt to avoid previously used expensive auto-regressive
template“xItwas[MASK]”whereverbalizers(e.g., decodingschemes(SchickandSchütze,2021b),by
‘great’and‘terrible’)aresubstitutedforthe[MASK] leveragingprototypicalnetworks(Snelletal.,2017)
to score target task labels (‘positive’ or ‘negative’). overmultipletokens. Overall,thesechangesenable
In this paper, we show that such engineering is upto100xfasterlearningandinference(§4.2).
2202
rpA
62
]LC.sc[
2v27110.4022:viXra

<!-- Page 2 -->


### PERFECT has several advantages: It avoids

engineering patterns and verbalizers for each new Layer norm +
task, which can be cumbersome. Recent work has +
shown that even some intentionally irrelevant or

### Adapter

misleading prompts can perform as well as more Feed forward

### Feed forward up projection

interpretable ones (Webson and Pavlick, 2021).

### Unlikethezero-shotorextremefew-shotcase,where Layer norm

promptingmightbeessential,weargueinthispaper + Nonlinearity
thatallyouneedistensoftrainingexamplestoavoid
Feed forward down

### Adapter

thesechallengesbyadopting PERFECT orasimilar projection

### Multi-head attention

data-efficient learning method. Experiments on a
widevarietyofNLPtasksdemonstratethatPERFECT
outperforms state-of-the-art prompt-based methods Transformer Layer Adapter Layer
whilebeingsignificantlymoreefficientininference
andtrainingtime,storage,andmemoryusage(§4.2). Figure 2: Left: Adapter integration in a PLM. Right:
An adapter architecture. Adapters are usually inserted

### To the best of our knowledge, we are the first to

afterthefeed-forwardandself-attentionmodules. During
proposeafew-shotlearningmethodusingtheMLM
training,weonlyoptimizethegreencomponents
objectiveinPLMsthatprovidestate-of-the-artresults
whileremovingallper-taskmanualengineering.
and b) a feed-forward block, where both modules
2 Background
are followed by a skip connection. As depicted in
Figure 2, adapters are normally inserted after each
Problem formulation: We consider a general
oftheseblocksbeforetheskipconnection.
problemoffine-tuninglanguagemodelsinafew-shot

### Adaptersarebottleneckarchitectures. Bykeeping

setting,onasmalltrainingsetwithK uniqueclasses
inputandoutputdimensionsthesame,theyintroduce
andN examplesperclass,suchthatthetotalnumber
no additional architectural changes. Each adapter,
ofexamplesis|D|=N×K. LetD=∪K D bethe
k=1 k A(.) ∈ RH, consists of a down-projection, D(.) ∈
giventrainingset,whereD ={(xi,yi)}N shows
k k k i=1 RH×B,anon-linearity,suchasGeLU(Hendrycksand
thesetofexampleslabeledwithclassk andyi ∈Y
k Gimpel,2016),andanup-projectionU(.)∈RB×H,
is the corresponding label, where |Y| = K. We
where H is thedimension of input hidden statesx,
additionallyassumeaccesstoadevelopmentsetwith
andBisthebottlenecksize. Formallydefinedas:
thesamesizeasthetrainingdata. Notethatlargervalidationsetscangrantasubstantialadvantage(Perez

### A(x)=U(GeLU(D(x)))+x, (1)

etal.,2021),andthusitisimportanttousealimited
validationsizetobeinlinewiththegoaloffew-shot
learning. Unlessspecifiedotherwise,inthiswork,we 2.2 Prompt-basedFine-tuning
use16trainingexamples(N=16)andavalidation
Standard Fine-tuning: In standard fine-tuning
setwith16examples,foratotalof32-shotlearning.
withPLMs(Devlinetal.,2019),firstaspecial[CLS]
tokenisappendedtotheinputx,andthenthePLM
2.1 Adapters
maps it to a sequence of hidden representations
Recent work has shown that fine-tuning all param- h = (h ,...,h ) with h ∈ RH, where H is the
1 S i
eters of PLMs with a large number of parameters
hiddendimension,andS isthemaximumsequence
in low-resource datasets can lead to a sub-optimal length. Then,aclassifier,softmax(WTh ),using

## [Cls]

solution(Petersetal.,2019;Dodgeetal.,2020). As
the embedding of the classification token (h ),

## [Cls]

showninFigure2,Rebuffietal.(2018)andHoulsby
istrainedend-to-endforeachdownstreamtask. The
et al. (2019) suggest an efficient alternative, by
main drawback of this approach is the discrepancy
insertingsmalltask-specificmodulescalledadapters
betweenthepre-trainingandfine-tuningphasessince
within layers of a PLMs. They then only train the

### PLMshavebeentrainedtopredictmasktokensina

newlyaddedadaptersandlayernormalization,while
maskedlanguagemodelingtask(Devlinetal.,2019).
fixingtheremainingparametersofaPLM.
Each layer of a transformer model is composed Prompt-based tuning: To address this discrepof two primary modules: a) an attention block, ancy,prompt-basedfine-tuning(SchickandSchütze,

<!-- Page 3 -->

2021a,b;Gaoetal.,2021)formulatestasksinacloze- Label Embedding
d
format(Taylor,1953).Thisway,themodelcanpredict e
targets with a masked language modeling (MLM) m
at
el s W1 W M
objective. Forexample,asshowninFigure1,fora E
sti
L a
b

### Hinge Loss

sentimentclassificationtask,inputsareconvertedto:
d
x prompt = [CLS]x.Itwas[MASK].[SEP] e si
r e
a b
el s
Em

## M

be

## A

d

## S

d

## K

in g 1 Emb

## M

e

## A

d

## S

d

## K

in g M
(cid:124)(cid:123)(cid:122)(cid:125) DL
pattern

### Layer norm

Then, the PLM determines which verbalizer (e.g., +
‘great’and‘terrible’)isthemostlikelysubstitutefor
r
themaskinthex .Thissubsequentlydetermines e
prompt y Adapter
a
thescoreoftargets(‘positive’or‘negative’). Indetail: L
M Feed forward

## L

Trainingstrategy: LetM:Y→V beamapping P

### Layer norm

from target labels to individual words in a PLM’s
+
vocabulary. Werefertothismappingasverbalizers.
Then the input is converted to x = T(x) by
prompt Adapter
appendingapatternandamasktokentoxsothatit
hastheformatofamaskedlanguagemodelinginput. Multi-head Attention

### Then,theclassificationtaskisconvertedtoaMLM

objective (Tam et al., 2021; Schick and Schütze, Embedding Layer
2021a),andthePLMcomputestheprobabilityofthe
labelyas: CLS TOK 1 TOK N MASK 1 MASK M SEP

### Input Masks

Figure3:Weremovehandcraftedpatternsandverbalizers.
p(y|x)=p([MASK]=M(y)|x )
prompt

### We replace patterns using task-specific adapters and

exp(W M T (y) h [MASK] ) designlabelembeddingsfortheclasses.Weonlytrainthe
= , (2)
(cid:80) exp(WTh ) green blocks (the label embeddings, adapters, and layer
v(cid:48)∈V v(cid:48) [MASK]
norms).
whereh isthelasthiddenrepresentationofthe

## [Mask]

mask, and W shows the output embedding of the
v onthisnewtoken,theprobabilitiesoftheremaining
PLMforeachverbalizerv∈V. Formanytasks,vermask positions are recomputed. They repeat this
balizers have multiple tokens. Schick and Schütze
autoregressive decoding until they fill all mask
(2021b) extended (2) to multiple mask tokens by
positions. Thisinferencestrategyisveryslow,asthe
adding the maximum number of mask tokens M
numberofforwardpassesincreaseswiththenumber
neededtoexpresstheoutputs(verbalizers)foratask.
ofclassesandthenumberofverbalizer’stokens.

### Inthatcase, SchickandSchütze(2021b)computes

This formulation obtained impressive few-shot
theprobabilityofeachclassasthesummationofthe
performancewithPLMs.However,thesuccessofthis
logprobabilitiesofeachtokeninthecorresponding
approach heavily relies on engineering handcrafted
verbalizer,andthentheyaddahingelosstoensurea
patterns and verbalizers. Coming up with suitable
marginbetweenthecorrectverbalizerandtheincorverbalizersandpatternscanbedifficult(Mishraetal.,
rectones.
2022b,a).Additionally,theperformanceissensitiveto
Inference strategy: During inference, the model thewordingofpatterns(Zhaoetal.,2021;Perezetal.,
needstoselectwhichverbalizertouseinthegiven 2021;SchickandSchütze,2021a;Jiangetal.,2020)or
context. Schick and Schütze (2021b) predicts the tothechosenverbalizers(WebsonandPavlick,2021).
verbalizertokensinanautoregressivefashion. They Inaddition,handcraftedverbalizerscauseproblems
firsttrimthenumberofmasktokensfromM toeach for efficient training: a) they require updating the
candidateverbalizer’stokenlengthandcomputethe PLM embedding layer, causing large memory
probability of each mask token. They then choose overhead; b)fine-tuningPLMsalsorequiresavery
thepredictedtokenwiththehighestprobabilityand small learning rate (usually 10−5), which slows
replacethecorrespondingmasktoken. Conditioning down tuning the parameters of the verbalizers;

<!-- Page 4 -->

c) modeling verbalizers as one of the tokens of be unstable in low-resource settings (Dodge et al.,
the PLM vocabulary (perhaps unintentionally) 2020);adaptersallowsample-efficientfine-tuning,by
impacts the input representation during tuning; d) keepingtheunderlyingPLMfixed,b)adaptersreduce
verbalizershavevariabletokenlengths,complicating the storage and memory footprints (§4.2), c) they
the implementation in a vectorized format, thereby alsoincreasestabilityandperformance(§4),making
makingitchallengingtoefficientlyfine-tunePLMs. them an excellent choice for few-shot fine-tuning.

### Toourknowledge,thisisthefirstapproachforusing

3 Method task-specific adapters to effectively and efficiently
removepatternsinfew-shotlearning. Experimental

### WeproposePERFECT,averbalizerandpatternfree

results in §4 show its effectiveness compared to
few-shot learning method. We design PERFECT to
handcraftedpatternsandsoftprompts(LiandLiang,
beclosetothepre-trainingphase,similartothePET
2021;Lesteretal.,2021).
familyofmodels(SchickandSchütze,2021b;Gao
etal.,2021),whilereplacinghandcraftedpatternsand
3.2 Multi-TokenLabelEmbeddings
verbalizers with new components that are designed
We freeze the weights of the PLM’s embedding
todescribethetaskandlearnthelabels. Asshown
layer and introduce a separate label embedding
in Figure 3, we first convert each input x to its
input
L∈RK×M×H,whichisamulti-tokenlabelrepresenmaskedlanguagemodeling(MLM)inputcontaining
M masktokens [MASK]1 withnoaddedpatterns, tationwhereM isthenumberoftokensrepresenting
denoted as x
masked
= T(cid:48)(x
input
).2 PERFECT then eachlabel,K indicatesthenumberofclasses,H is
theinputhiddendimension. Usingafixednumberof
trainsaclassifierper-tokenandoptimizestheaverage
tokensM foreachlabel,versusvariable-tokenlength
multi-classhingelossovereachmaskposition.
verbalizersusedinpriorwork(SchickandSchütze,

### Threemaincomponentsplayaroleinthesuccess

2021a,b)substantiallysimplifiestheimplementation
ofPERFECT: a)apattern-freetaskdescription,where
andacceleratesthetraining(§4.2).
we use task-specific adapters to efficiently tell the
model about the given task, replacing previously
3.3 TrainingPERFECT
manuallyengineeredpatterns(§3.1),b)multi-token
label-embeddingasanefficientmechanismtolearn AsshowninFigure3,weoptimizelabelembeddings
thelabelrepresentations,removingmanuallydesigned so that the PLM predicts the correct label, and
verbalizers(§3.2). c)anefficientinferencestrategy optimizeadapterstoadaptthePLMforthegiventask.
buildingontopoftheideaofprototypicalnetworks For label embeddings, PERFECT trains a classifier
(Snell et al., 2017) (§3.4), which replaces prior per token and optimizes the average multi-class
iterative autoregressive decoding methods (Schick hinge loss over all mask positions. Given x masked ,
andSchütze,2021b). leth [MASK] betheembeddingofitsi-thmasktoken
i
AsshowninFigure3,wefixtheunderlyingPLM fromthelastlayerofthePLMencoder. Additionally,
model and only optimize the new parameters that let f(.) : RH → RK be a per-token classifier that
weadd(greenboxes). Thisincludesthetask-specific computes the predictions by multiplying the mask
adapterstoadapttherepresentationsforagiventask token embedding with its corresponding label
andthemulti-tokenlabelrepresentations. Wedetail embedding. Formallydefinedas:
eachofthesecomponentsbelow.
t =f(h )=LTh ,
i [MASK] i i [MASK] i
3.1 Pattern-FreeTaskDescription
where L ∈RK×H shows the label embedding for
We use task-specific adapter layers to provide i
thei-thmaskposition. Then,foreachmaskposition,
the model with learned, implicit task descriptions.
we optimize a multi-class hinge loss between their
Adapters additionally bring multiple other benefits:
scorest andlabels. Formallydefinedas:
a)fine-tuningallweightsofPLMswithmillionsor i
billionsofparametersissample-inefficient,andcan (cid:80)K
max(0,m−t +t )
k=1,k=(cid:54) y iy ik

### L(x,y,i)= ,

1Wediscussthegeneralcasewithinsertingmultiplemasks; K
forsomedatasetsthisimprovesperformance(§4.3.1).
2We insert mask tokens after the input string in single- wheret showsthek-thelementoft ,representing
ik i
sentence benchmarks, and after the first sentence in the case
the score corresponding to class k, and m is the
ofsentence-pairdatasetsandencodebothsentencesasasingle
input,whichwefoundtoperformthebest(AppendixC). margin,whichwefixtothedefaultvalueofm=1.

<!-- Page 5 -->

Then,thefinallossiscomputedbyaveragingtheloss thewordsensedisambiguationdatasetWiC(Pilehvar
overallmasktokensandtrainingsamples: and Camacho-Collados, 2019), 7) the paraphrase
detectiondatasetsMRPC(DolanandBrockett,2005)
1 (cid:88) (cid:88) M andQQP.4SeedatasetsstatisticsinAppendixA.

### L= L(x,y,i) (3)

M|D| ForMR,CR,SST-5,SUBJ,andTREC,weteston
(x,y)∈Di=1
theoriginaltestsets,whileforotherdatasets,sincetest
3.4 InferencewithPERFECT
setsarenotpubliclyavailable,wetestontheoriginal
During evaluation, instead of relying on the prior validationset. Wesample16instancesperlabelfrom
iterative autoregressive decoding schemes (Schick thetrainingsettoformtrainingandvalidationsets.
and Schütze, 2021b), we classify a query point by
Baselines We compare with the state-of-the-art
findingthenearestclassprototypetothemasktoken
few-shotlearningofPETandfine-tuning:
embeddings:
PET (Schick and Schütze, 2021a,b) is the statey=argmax max (cid:16) exp−d(hq i ,c iy ) (cid:17) , (4) of-the-art few-shot learning method that employs
y∈Y i∈{1,...,M} carefullycraftedverbalizersandpatterns. Wereport
wheredissquaredeuclideandistance,3hq
indicates
thebest(PET-best)andaverage(PET-average)results
i amongallpatternsandverbalizers.5
the embedding of the i-th mask position for the
query sample q, and c ∈ RD is the prototype FINETUNE Thestandardfine-tuning(Devlinetal.,
iy
2019), with adding a classifier on top of the [CLS]
representationofthei-thmasktokenwithclasslabel
tokenandfine-tuningallparameters.
y,i.e.,themeanembeddingofi-thmaskpositionin
alltrainingsampleswithlabely:
Our method We study the performance of
1 (cid:88)

### PERFECT and perform an extensive ablation study

c iy = |D | hb i , (5) toshowtheeffectivenessofourdesignchoices:
y
b∈Dy PERFECT-rand Werandomlyinitializethelabel
embeddingLfromanormaldistributionN(0,σ)with
wherehb
i
showstheembeddingofi-thmaskposition
σ=10−4 (chosenbasedonvalidationperformance,
fortrainingsampleb,andD isthetraininginstances
y seeAppendixD)withoutrelyingonanyhandcrafted
withclassy.Thisstrategycloselyfollowsprototypical
patterns and verbalizers. As an ablation, we study
networks (Snell et al., 2017), but applied across
thefollowingtwovariants:
multiple tokens. We choose this form of inference

### PERFECT-init Weinitializethelabelembedding

because prototypical networks are known to be
with the token embeddings of manually designed
sample efficient and robust (Snell et al., 2017),
verbalizers in the PLM’s vocabulary to study the
and because it substantially speeds up evaluation
impactofengineeredverbalizers.
comparedtopriormethods(§4.2).
prompt+mte Tocomparetheimpactofadapters
versussoftprompt-tuningforfew-shotlearning,we
4 Experiments
appendtrainablecontinuouspromptembeddingsto
We conduct extensive experiments on a variety of theinput(Lesteretal.,2021). Thenweonlytunethe
NLPdatasetstoevaluatetheperformanceofPERFECT softpromptandmulti-tokenlabelembeddings(mte).
andcompareitwithstate-of-the-artfew-shotlearning. bitfit+mte Following Cai et al. (2020) and Ravfogel et al. (2021), we tune biases as an alternative

### Datasets: Weconsider7tasksand12datasets:1)

to adapters. We additionally tune multi-token label
thesentimentanalysisdatasetsSST-2(Socheretal.,
embeddings.
2013), SST-5 (Socher et al., 2013), MR (Pang and
LoganIVetal.(2021)Following LoganIVetal.
Lee, 2005), and CR (Hu and Liu, 2004), 2) the
(2021),weremovepatternsandtunethebiasesinthe
subjectivity classification dataset SUBJ (Pang and

## Pet.


### Lee, 2004), 3) the question classification dataset

TREC (Voorhees and Tice, 2000), 4) the natural Experimentaldetails: WeusetheRoBERTalarge
languageinferencedatasetsCB(DeMarneffeetal., model(Liuetal.,2019)(355Mparameters)astheun-
2019)andRTE(Wangetal.,2019a),5)thequestion derlyingPLMforallmethods. WeusetheHuggingansweringdatasetQNLI(Rajpurkaretal.,2016),6)
4https://quoradata.quora.com/
3We also tried with cosine similarity but found a slight 5Foracontrolledstudy,weusetheMLMvariantshownin
improvementwithsquaredEuclideandistance(Snelletal.,2017). (2),whichhasbeenshowntoperformthebest(Tametal.,2021).

<!-- Page 6 -->

Method SST-2 CR MR SST-5 Subj TREC Avg
Single-SentenceBenchmarks

## Finetune 81.4

/70.0/4.0
80.1
/72.9/4.1
77.7
/66.8/4.6
39.2
/34.3/2.5
90.2
/84.1/1.8
87.6
/75.8/3.7
76.0
/67.3/3.4

### PET-Average 89.7 88.4 85.9 45.9 88.1 85.0 80.5

/81.0/2.4 /68.8/3.0 /79.0/2.1 /40.3/2.4 /79.6/2.4 /70.6/4.5 /69.9/2.8

### PET-Best 89.1 88.8 86.4 46.0 88.7 85.8 80.8

/81.0/2.6 /85.8/1.9 /82.0/1.6 /41.2/2.4 /84.6/1.8 /70.6/4.4 /74.2/2.4
LoganIVetal.(2021) 89.8
/84.1/1.7
89.9
/87.2/1.1
84.9
/76.2/3.2
45.7
/41.6/2.3
81.8/73.5/4.0 84.7
/81.8/1.6
79.5
/74.1/2.3
PERFECT-rand 90.7
/88.2/1.2
90.0
/85.5/1.4
86.3
/81.4/1.6
42.7
/35.1/2.9
89.1
/82.8/2.1
90.6
/81.6/3.2
81.6
/75.8/2.1

### Ablation

PERFECT-init 90.9
/87.6/1.5
89.7
/87.4/1.2
85.4
/75.8/3.3
42.8
/35.9/3.5
87.6
/81.6/2.8
90.4
/86.6/1.8
81.1
/75.8/2.4
prompt+mte 70.6 71.0 66.6 32.2 82.7 79.6 67.1
/56.0/8.3 /55.8/8.2 /49.6/7.3 /26.5/3.2 /69.6/3.9 /66.8/6.5 /54.0/6.2
bitfit+mte 89.5 90.1 85.6 42.3 89.1 90.4 81.2/
/81.7/3.0 /87.8/1.0 /80.5/1.9 /36.8/3.3 /82.4/2.4 /85.0/1.4 75.7/2.2
Method CB RTE QNLI MRPC QQP WiC Avg
Sentence-PairBenchmarks

## Finetune 72.9

/67.9/2.5
56.8
/50.2/3.5
62.7
/51.4/7.0
70.1
/62.7/4.7
65.0
/59.8/3.6
52.4
/46.1/3.7
63.3
/56.4/4.2

### PET-Average 86.9 60.1 66.5 62.1 63.4 51.0 65.0/

/73.2/5.1 /49.5/4.7 /55.7/6.2 /38.2/6.8 /44.7/7.9 /46.1/2.6 51.2/5.6

### PET-Best 90.0 62.3 70.5 63.4 70.7 51.6 68.1/

/78.6/3.9 /51.3/4.5 /57.9/6.4 /49.3/6.5 /55.2/5.8 /47.2/2.3 56.6/4.9

### LoganIVetal.(2021) 91.0 64.4 71.2 63.9 70.4 52.4 68.9

/87.5/2.7 /58.5/3.9 /66.5/2.6 /53.7/5.3 /62.7/3.4 /48.4/1.8 /62.9/3.3
PERFECT-rand 90.3
/83.9/3.5
60.4
/53.1/4.7
74.1
/60.3/4.6
67.8
/54.7/5.7
71.2
/64.2/3.5
53.8
/47.0/3.0
69.6
/60.5/4.2

### Ablation

PERFECT-init 87.9
/75.0/4.9
60.7
/52.7/4.5
72.8
/56.7/6.8
65.9
/56.6/6.0
71.1
/65.6/3.5
51.7
/46.6/2.8
68.4
/58.9/4.8
prompt+mte 73.0 56.9 55.4 60.0 54.3 51.3 58.5
/62.5/6.1 /50.7/4.1 /50.2/4.6 /51.5/5.8 /46.2/5.6 /46.7/2.8 /51.3/4.8
bitfit+mte 89.6 61.3 70.6 68.5 69.4 52.9 68.7/
/82.1/4.3 /53.8/5.2 /51.9/5.9 /57.4/5.1 /63.0/3.9 /47.8/2.7 59.3/4.5
Table1: Performanceofallmethodsonsingle-sentenceandsentence-pairbenchmarks. Wereportaverage/worst-case
accuracy/standarddeviation.PERFECTobtainsthestate-of-the-artresults.Boldfontsindicatethebestresults.
FacePyTorchimplementation(Wolfetal.,2020). For theperformancecomparedtoPET-averageby+1.1
thebaselines,weusedthecarefullymanuallydesigned and+4.6pointsforsingle-sentenceandsentence-pair
patternsandverbalizersinGaoetal.(2021),Minetal. datasetsrespectively. ItevenoutperformsPET-best,
(2021), and Schick and Schütze (2021b) (usually 5 wherewereportthebestperformanceofPETacross
differentoptionsperdatasets;seeAppendixB). multiplemanuallyengineeredpatternsandverbalizers.
Weevaluateallmethodsusing5differentrandom Moreover, PERFECT generally improves the minisamples to create the training/validation sets and 4 mum performance and reduces standard deviation
different random seeds for training. Therefore, for substantially. Finally,PERFECTisalsosignificantly
PET-average,wereporttheresultson20x5(number more efficient: reducing the training and inference
of patterns and verbalizers) = 100 runs, while for time,memoryusage,andstoragecosts(see§4.2).
PET-bestandourmethod,wereporttheresultsover

### PET-bestimprovestheresultsoverPET-average

20runs. Thevarianceinfew-shotlearningmethodsis
showingthatPETisunstabletothechoiceofpatterns
usuallyhigh(Perezetal.,2021;Zhaoetal.,2021;Lu
and verbalizers; this difference is more severe for
etal.,2021). Therefore,wereportaverage,worst-case
sentence-pairbenchmarks. Thismightbebecausethe
performance,andstandarddeviationacrossallruns,
positionofthemaskhighlyimpactstheresults,and
where the last two values can be important for
thepatternsusedforsentence-pairdatasetsinSchick
risk-sensitiveapplications(Asrietal.,2016).
andSchütze(2021b)exploitsthisvariationbyputting
themaskinmultiplelocations(seeAppendixB).
4.1 ExperimentalResults

### RemovingpatternsandtuningbiasesinLoganIV

Table 1 shows the performance of all methods. etal.(2021)isnotexpressiveenoughandperforms
PERFECTobtainsstate-of-the-artresults,improving substantiallyworsethanPERFECTonaverage.

<!-- Page 7 -->

Metric PET PERFECT ∆% on the 500-sampled QNLI dataset. We select the
largest batch size for each method that fits a fixed
Trainedparams(M) 355.41 3.28 -99.08%
budgetoftheGPUmemory(40GB).

### Peakmemory(GB) 20.93 16.34 -21.93%

Due to the auto-regressive inference strategy of

### Trainingtime(min) 23.42 0.65 -97.22%

PET (Schick and Schütze, 2021b), all prior work
+PETinbatch 0.94 0.65 -30.85%
implemented it with a batch size of 1 (Perez et al.,

### Inferencetime(min) 9.57 0.31 -96.76%

2021;SchickandSchütze,2021b;Tametal.,2021).

### Additionally, since PET deals with verbalizers of


### Table 2: Percentage of trained parameters, average peak

memory,training,andinferencetime. ∆%istherelative variablelengths,itishardtoimplementtheirtraining
differencewithrespecttoPET.Lowerisbetter. phaseinbatchmode. WespecificallychooseQNLI
to have verbalizers of the same length and enable
batching for comparison purposes (referred to as
As an ablation, even if we initialize the label

### PETinbatch). However,verbalizersarestillnotof

embedding with handcrafted verbalizers in PER-
fixed-lengthformostothertasks,andthisspeed-up
FECT-init,itconsistentlyobtainslowerperformance,
doesnotapplygenerallytoPET.
demonstratingthatPERFECTisabletoobtainstate-of-

### In Table 2, for each method we report the

the-artperformancewithlearningfrompurerandom
percentage of trained parameters, memory usage,
initialization. We argue that initializing randomly
trainingtime,andinferencetime. PERFECTreduces
closetozero(withlowvarianceσ=10−4),asdone
thenumberoftrainedparameters,andthereforethe
in our case, slightly improves performance, which
storage requirement, by 99.08%. It additionally reperhaps is not satisfied when initializing from the
ducesthememoryrequirementby21.93%compared
manuallyengineeredverbalizers(seeAppendixD).
toPET.PERFECTspeedsuptrainingsubstantially,by

### Asasecondablation,whenlearningpatternswith

97.22%relativetotheoriginalPET’simplementation,
optimizingsoftpromptsinprompt+mte,weobserve
and 30.85% to our implementation of PET. This is
high sensitivity to learning rate, as also confirmed
becauseadapter-basedtuningsavesonmemoryand
inLiandLiang(2021)andMahabadietal.(2021a).
allows training with larger batch sizes. In addition,
We experimented with multiple learning rates but
PERFECTissignificantlyfasterduringinferencetime
performanceconsistentlylagsbehindPERFECT-rand.
(96.76%lessinferencetimerelativetoPET).
Thiscanbeexplainedbythelowflexibilityofsuch

### Notethatalthoughprompt+mteandbitfit+mtecan

methodsasalltheinformationregardingspecifying
alsoreducethestoragecosts,byhaving0.02Mand
patternsneedstobecontainedintheprefixes. Asa
0.32Mtrainableparametersrespectively,theyarenot
result,themethodonlyallowslimitedinteractionwith
expressiveenoughtolearntaskdescriptions,andtheir
therestofthemodelparameters,andobtaininggood
performancesubstantiallylagsbehindPERFECT(see
performancerequiresverylargemodels(Lesteretal.,
Table1).
2021). In addition, increasing the sequence length
Overall, given the size of PLMs with millions
leadstomemoryoverhead(Mahabadietal.,2021a),
and billions of parameters (Liu et al., 2019; Raffel
and the number of prompt tokens is capped by the
etal.,2020),efficientfew-shotlearningmethodsare
numberoftokensthatcanfitinthemaximuminput
of paramount importance for practical applications.
length,whichcanbealimitationfortasksrequiring
largecontexts.

### PERFECTnotonlyoutperformsthestate-of-the-artin

termsofaccuracyandgenerallyimprovesthestability

### Asathirdablation,tuningbiaseswithoptimizing

(Table 1), but also is significantly more efficient in
softpromptsinbitfit+mteobtainslowerperformance
runtime,storage,andmemory.
comparedto PERFECT,showingthatadaptersarea
betteralternativecomparedtotuningbiasestolearn
4.3 Analysis
taskdescriptionsforfew-shotlearning.
Weincludemoreablationresultsondesignchoices Can task-specific adapters replace manually
ofPERFECTinAppendixE. engineered patterns? PERFECT is a pattern-free
approachandemploysadapterstoprovidethePLMs
4.2 EfficiencyEvaluation
withtaskdescriptionsimplicitly. Inthissection,we
Inthissection,wecomparetheefficiencyofPERFECT study the contribution of replacing manual patterns
with the state-of-the-art few-shot learning method, with adapters in isolation without considering our
PET.Tothisend,wetrainallmethodsfortenepochs other contributions in representing labels, training,

<!-- Page 8 -->


### Dataset PET-Average Pattern-Free Dataset PERFECT -Adapters


## Sst-2 89.7/81.0/2.4 90.5/87.8/1.2 Sst-2 90.7/88.2/1.2 88.2/81.9/2.3


## Cr 88.4/68.8/3.0 89.8/87.0/1.4 Cr 90.0/85.5/1.4 89.2/83.1/1.7


## Mr 85.9/79.0/2.1 86.4/83.0/1.8 Mr 86.3/81.4/1.6 82.5/78.2/2.5


## Sst-5 45.9/40.3/2.4 44.8/40.0/2.4 Sst-5 42.7/35.1/2.9 40.6/33.6/3.3


## Subj 88.1/79.6/2.4 85.3/74.7/3.8 Subj 89.1/82.8/2.1 89.7/85.0/1.9


## Trec 85.0/70.6/4.5 87.9/84.6/1.8 Trec 90.6/81.6/3.2 89.8/74.2/4.3


## Cb 86.9/73.2/5.1 93.0/89.3/1.9 Cb 90.3/83.9/3.5 89.6/83.9/2.8


## Rte 60.1/49.5/4.7 63.7/56.3/4.1 Rte 60.4/53.1/4.7 61.7/53.8/5.1


## Qnli 66.5/55.7/6.2 71.3/65.8/2.5 Qnli 74.1/60.3/4.6 73.2/56.3/5.8


## Mrpc 62.1/38.2/6.8 66.0/54.4/5.6 Mrpc 67.8/54.7/5.7 68.0/54.2/6.1


## Qqp 63.4/44.7/7.9 71.8/64.3/3.7 Qqp 71.2/64.2/3.5 71.0/62.0/3.7

WiC 51.0/46.1/2.6 53.7/50.3/2.0 WiC 53.8/47.0/3.0 52.5/46.9/3.0
Avg 72.8/60.6/4.2 75.4/69.8/2.7 Avg 75.6/68.1/3.1 74.7/66.1/3.5
Table3: AverageperformanceofPET withfivedifferent Table 4: Performance of PERFECT w/o adapters, -
patternsvs.Pattern-Freethatreplaceshandcraftedpatterns Adapters. Wereporttheaverageperformance/worst-case
withtask-specificadapters. Wereporttheaverage/worst- performance/andthestandarddeviation.
caseperformance/andthestandarddeviation.
and unstable on resource-limited datasets (Dodge
andinference. InPET(SchickandSchütze,2021a,b),
etal.,2020;Zhangetal.,2020;Mosbachetal.,2021).
wereplacethehandcraftedpatternswithtask-specific

### However,byusingadapters,wesubstantiallyreduce

adapters(Pattern-Free)whilekeepingtheverbalizers
the number of trainable parameters, allowing the
and the training and inference intact6 and train it
modeltobebettertunedinafew-shotsetting.
with a similar setup as in §4. Table 3 shows the
results. WhilePETisverysensitivetothechoiceof Impact of the number of masks In Table 1, to
prompts,adaptersprovideanefficientalternativeto compareourdesignwithPETinisolation,wefixed
learnpatternsrobustlybyimprovingtheperformance thenumberofmasktokensasthemaximumnumber
(averageandworst-case)andreducingthestandard insertedbyPET.Intable5, westudytheimpactof
deviation.Thisfindingdemonstratesthattask-specific varying the number of inserted mask tokens for a
adapterscaneffectivelyreplacemanuallyengineered randomselectionofsixtasks. Formosttasks,having
prompts. Additionally,theyalsosaveonthetraining twomasktokensperformsthebest,whileforMRand
budget by at least 1/numberofpatterns (normally RTE,havingone,andforMRPC,insertingtenmasks
1/5)bynotrequiringrunningthemethodfordifferent improves the results substantially. The number of
choicesofpatterns,andbyfreezingmostparameters, requiredmasksmightbecorrelatedwiththedifficulty
thissavesonmemoryandoffersadditionalspeed-up. of the task. PERFECT is designed to be general,
enablinghavingmultiplemasktokens.
4.3.1 AblationStudy
Impact of Removing Adapters To study the
5 RelatedWork
impact of adapters in learning patterns, we remove
adapters, while keeping the label embedding. Adapter Layers: Mahabadi et al. (2021b) and
Handcrafted patterns are not included and we Üstün et al. (2020) proposed to generate adapters’
tune all parameters of the model. Table 4 shows weightsusinghypernetworks(Haetal.,2017),where
the results. Adding adapters for learning patterns Mahabadi et al. (2021b) proposed to share a small
contributes to the performance by improving the hypernetworktogenerateconditionaladapterweights
averageperformance,andmakingthemodelrobustby efficientlyforeachtransformerlayerandtask. Maimprovingtheminimumperformanceandreducing habadietal.(2021a)proposedcompacterlayersby
thestandarddeviation. ThisisbecausetrainingPLMs building on top of ideas of parameterized hyperwith millions of parameters is sample-inefficient complex layers (Zhang et al., 2021) and low-rank
methods(Lietal.,2018;Aghajanyanetal.,2021),as
6Sincewedon’thavepatterns,inthecaseofmultiplesetsof
verbalizers,weusethefirstsetofverbalizersasarandomchoice. an efficient fine-tuning method for PLMs. We are

<!-- Page 9 -->

Datasets 1 2 5 10 being far simpler and more efficient than recent
few-shotlearningmethods,producesstate-of-the-art

## Cr 90.1 90.2 89.0 87.8

results. Overall, the simplicity and effectiveness of

## Mr 86.9 86.1 85.4 85.6

PERFECTmakeitapromisingapproachforfew-shot

## Mrpc 67.4 68.2 70.1 72.3

learningwithPLMs.

## Qnli 73.7 73.9 73.0 65.1

RTE 60.0 57.3 56.2 56.0 Acknowledgements

## Trec 90.0 90.9 88.9 88.8

The authors would like to thank Sebastian Ruder

### Avg 78.0 77.8 77.1 75.9

and Marius Mosbach for their comments on drafts
ofthispaper. Thisresearchwaspartlysupportedby
Table5:Testperformanceforthevaryingnumberofmask
theSwissNationalScienceFoundationundergrant
tokens.Boldfontsindicatethebestresultsineachrow.
number200021_178862.
the first to employ adapters to replace handcrafted

### References

patternsforfew-shotlearning.
Armen Aghajanyan, Luke Zettlemoyer, and Sonal

### Few-shot Learning with PLMs: Le Scao and


### Gupta. 2021. Intrinsic dimensionality explains the

Rush(2021)showedthatpromptingprovidessubstan- effectivenessoflanguagemodelfine-tuning. InACL.
tialimprovementscomparedtofine-tuning,especially

### HibaAsri,HajarMousannif,HassanAlMoatassime,and

in low-resource settings. Subsequently, researchers
Thomas Noel. 2016. Using machine learning algocontinuouslytriedtoaddressthechallengesofmanu- rithms for breast cancer risk prediction and diagnosis.
allyengineeredpatternsandverbalizers: a)Learning ProcediaComputerScience.
thepatternsinacontinuousspace(LiandLiang,2021; Roy Bar-Haim, Ido Dagan, Bill Dolan, Lisa Ferro,
QinandEisner,2021;Lesteretal.,2021),whilefreez- and Danilo Giampiccolo. 2006. The second pascal
ingPLMforefficiency,hastheproblemthat,inmost recognising textual entailment challenge. Second
PASCALChallengesWorkshoponRecognisingTextual
cases,suchanapproachonlyworkswithverylarge
Entailment.
scalePLMs(Lesteretal.,2021),andlagsbehindfull
fine-tuning in a general setting, while being ineffi- LuisaBentivogli,IdoDagan,HoaTrangDang,DaniloGiampiccolo,andBernardoMagnini.2009. Thefifthpascientandnotaseffectivecomparedtoadapters(Macalrecognizingtextualentailmentchallenge. InTAC.
habadi et al., 2021a). b) Optimizing patterns in a

### Tom Brown, Benjamin Mann, Nick Ryder, Melanie

discrete space (Shin et al., 2020; Jiang et al., 2020;
Subbiah, Jared D Kaplan, Prafulla Dhariwal, Arvind

### Gaoetal.,2021)hastheproblemthatsuchmethods


### Neelakantan, Pranav Shyam, Girish Sastry, Amanda

are computationally costly. c) Automatically find- Askell, Sandhini Agarwal, Ariel Herbert-Voss,
ingverbalizersinadiscreteway(Schicketal.,2020; Gretchen Krueger, Tom Henighan, Rewon Child,
Schick and Schütze, 2021a) is computationally ex- Aditya Ramesh, Daniel Ziegler, Jeffrey Wu, Clemens

### Winter,ChrisHesse,MarkChen,EricSigler,Mateusz

pensive and does not perform as well as manually
Litwin, Scott Gray, Benjamin Chess, Jack Clark,
designedones. d)Removingmanuallydesignedpat-

### Christopher Berner, Sam McCandlish, Alec Radford,

terns(LoganIVetal.,2021)substantiallylagsbehind Ilya Sutskever, and Dario Amodei. 2020. Language
theexpert-designedones.Ourproposedmethod,PER- modelsarefew-shotlearners. InNeurIPS.
FECT,doesnotrelyonanyhandcraftedpatternsand HanCai,ChuangGan,LigengZhu,andSongHan.2020.
verbalizers. Tinytl: Reduce memory, not parameters for efficient
on-devicelearning. InNeurIPS.
6 Conclusion
IdoDagan,OrenGlickman,andBernardoMagnini.2005.
The pascal recognising textual entailment challenge.
WeproposedPERFECT,asimpleandefficientmethod
InMachineLearningChallengesWorkshop.
for few-shot learning with pre-trained language
models without relying on handcrafted patterns Marie-CatherineDeMarneffe,MandySimons,andJudith
Tonhauser. 2019. The commitmentbank: Investigatand verbalizers. PERFECT employs task-specific
ing projection in naturally occurring discourse. In
adapterstolearntaskdescriptionsimplicitly,replacing
proceedingsofSinnundBedeutung.
previous handcrafted patterns, and a continuous
JacobDevlin,Ming-WeiChang,KentonLee,andKristina
multi-tokenlabelembeddingtorepresenttheoutput
Toutanova. 2019. BERT: Pre-training of deep bidiclasses. Throughextensiveexperimentsover12NLP
rectionaltransformersforlanguageunderstanding. In
benchmarks,wedemonstratethatPERFECT,despite NAACL.

<!-- Page 10 -->

Jesse Dodge, Gabriel Ilharco, Roy Schwartz, Ali ChunyuanLi, HeeradFarkhoor, RosanneLiu, andJason
Farhadi, Hannaneh Hajishirzi, and Noah Smith. 2020. Yosinski. 2018. Measuring the intrinsic dimension of
Fine-tuning pretrained language models: Weight objectivelandscapes. InICLR.
initializations, data orders, and early stopping. arXiv
preprintarXiv:2002.06305. XiangLisaLiandPercyLiang.2021. Prefix-tuning: Optimizingcontinuouspromptsforgeneration. InACL.

### WilliamBDolanandChrisBrockett.2005. Automatically

constructingacorpusofsententialparaphrases. InIWP. YinhanLiu,MyleOtt,NamanGoyal,JingfeiDu,Mandar

### Joshi, Danqi Chen, Omer Levy, Mike Lewis, Luke

TianyuGao,AdamFisch,andDanqiChen.2021. Making Zettlemoyer,andVeselinStoyanov.2019. Roberta: A
pre-trained language models better few-shot learners. robustly optimized bert pretraining approach. arXiv
InACL. preprintarXiv:1907.11692.
DaniloGiampiccolo, BernardoMagnini, IdoDagan, and RobertLLoganIV,IvanaBalaževic´,EricWallace,Fabio
BillDolan.2007. ThethirdPASCALrecognizingtex- Petroni, Sameer Singh, and Sebastian Riedel. 2021.
tualentailmentchallenge. InACL-PASCALWorkshop Cutting down on prompts and parameters: Simple
onTextualEntailmentandParaphrasing. few-shot learning with language models. arXiv
preprintarXiv:2106.13353.
DavidHa,AndrewDai,andQuocV.Le.2017. Hypernetworks. InICLR. Yao Lu, Max Bartolo, Alastair Moore, Sebastian Riedel,
and Pontus Stenetorp. 2021. Fantastically ordered
DanHendrycksandKevinGimpel.2016. Gaussianerror
prompts and where to find them: Overcoming
linearunits(gelus). arXivpreprintarXiv:1606.08415.
few-shot prompt order sensitivity. arXiv preprint
arXiv:2104.08786.
Neil Houlsby, Andrei Giurgiu, Stanislaw Jastrzebski,

### Bruna Morrone, Quentin De Laroussilhe, Andrea

Rabeeh Karimi Mahabadi, James Henderson, and Se-
Gesmundo, MonaAttariyan, andSylvainGelly.2019.
bastianRuder.2021a. Compacter: Efficientlow-rank
Parameter-efficienttransferlearningfornlp. InICML.
hypercomplexadapterlayers. InNeurIPS.

### MinqingHuandBingLiu.2004. Miningandsummariz-

Rabeeh Karimi Mahabadi, Sebastian Ruder, Mostafa
ingcustomerreviews. InSIGKDD.

### Dehghani, and James Henderson. 2021b. Parameter-

Zhengbao Jiang, Frank F Xu, Jun Araki, and Graham efficient multi-task fine-tuning for transformers via
Neubig. 2020. How can we know what language sharedhypernetworks. InACL.
modelsknow? InTACL.

### George A Miller. 1995. Wordnet: a lexical database for

TevenLeScaoandAlexanderMRush.2021. Howmany english. InCommunicationsoftheACM.
datapointsisapromptworth? InNAACL.

### SewonMin,MikeLewis,HannanehHajishirzi,andLuke

Brian Lester, Rami Al-Rfou, and Noah Constant. 2021. Zettlemoyer. 2021. Noisy channel language model
The power of scale for parameter-efficient prompt prompting for few-shot text classification. arXiv
tuning. InEMNLP. preprintarXiv:2108.04106.
Quentin Lhoest, Albert Villanova del Moral, Patrick Swaroop Mishra, Daniel Khashabi, Chitta Baral, Yejin
von Platen, Thomas Wolf, Mario Šaško, Yacine Choi, and Hannaneh Hajishirzi. 2022a. Reframing
Jernite, Abhishek Thakur, Lewis Tunstall, Suraj Patil, instructional prompts to gptk’s language. In Findings
Mariama Drame, Julien Chaumond, Julien Plu, Joe ofACL.

### Davison, Simon Brandeis, Victor Sanh, Teven Le


### SwaroopMishra,DanielKhashabi,ChittaBaral,andHan-


### Scao, Kevin Canwen Xu, Nicolas Patry, Steven Liu,

nanehHajishirzi.2022b. Cross-taskgeneralizationvia
Angelina McMillan-Major, Philipp Schmid, Sylvain
naturallanguagecrowdsourcinginstructions. InACL.

### Gugger,NathanRaw,SylvainLesage,AntonLozhkov,

Matthew Carrigan, Théo Matussière, Leandro von

### MariusMosbach,MaksymAndriushchenko,andDietrich


### Werra, Lysandre Debut, Stas Bekman, and Clément

Klakow. 2021. On the stability of fine-tuning bert:
Delangue.2021a. huggingface/datasets:1.15.1.
Misconceptions,explanations,andstrongbaselines. In

## Iclr.

Quentin Lhoest, Albert Villanova del Moral, Yacine Jernite,AbhishekThakur,PatrickvonPlaten,SurajPatil,
BoPangandLillianLee.2004. Asentimentaleducation:

### JulienChaumond,MariamaDrame,JulienPlu,Lewis

sentiment analysis using subjectivity summarization
Tunstall,JoeDavison,MarioŠaško,GunjanChhablani,
basedonminimumcuts. InACL.

### Bhavitvya Malik, Simon Brandeis, Teven Le Scao,

Victor Sanh, Canwen Xu, Nicolas Patry, Angelina BoPangandLillianLee.2005. Seeingstars: Exploiting
McMillan-Major, Philipp Schmid, Sylvain Gugger, class relationships for sentiment categorization with
ClémentDelangue,ThéoMatussière,LysandreDebut, respecttoratingscales. InACL.

### Stas Bekman, Pierric Cistac, Thibault Goehringer,

VictorMustar,FrançoisLagunas,AlexanderRush,and Ethan Perez, Douwe Kiela, and Kyunghyun Cho. 2021.
ThomasWolf.2021b. Datasets: Acommunitylibrary True few-shot learning with language models. In
fornaturallanguageprocessing. InEMNLP. NeurIPS.

<!-- Page 11 -->

Matthew E Peters, Sebastian Ruder, and Noah A Smith. TaylorShin,YasamanRazeghi,RobertLLoganIV,Eric

## To tune or not to tune? adapting pretrained Wallace,andSameerSingh.2020. Elicitingknowledge

representationstodiversetasks. InRepL4NLP. from language models using automatically generated
prompts. InEMNLP.

### JonasPfeiffer,AishwaryaKamath,AndreasRück´le,Cho


### JakeSnell,KevinSwersky,andRichardZemel.2017. Pro-

Kyunghyun, and Iryna Gurevych. 2021. AdapterFutotypicalnetworksforfew-shotlearning. InNeurIPS.
sion: Non-destructive task composition for transfer
learning. InEACL.

### RichardSocher,AlexPerelygin,JeanWu,JasonChuang,


### Christopher D Manning, Andrew Y Ng, and Christo-

JonasPfeiffer, AndreasRücklé, CliftonPoth, Aishwarya
pherPotts.2013. Recursivedeepmodelsforsemantic
Kamath, Ivan Vulic´, Sebastian Ruder, Kyunghyun
compositionality over a sentiment treebank. In
Cho, and Iryna Gurevych. 2020. Adapterhub: A

## Emnlp.

framework for adapting transformers. In EMNLP:
SystemDemonstrations. Derek Tam, Rakesh R Menon, Mohit Bansal, Shashank

### Srivastava, and Colin Raffel. 2021. Improving and

Mohammad Taher Pilehvar and Jose Camacho-Collados. simplifyingpatternexploitingtraining. arXivpreprint

## Wic: theword-in-contextdatasetforevaluating arXiv:2103.11955.

context-sensitivemeaningrepresentations. InNAACL.

### Wilson L Taylor. 1953. “cloze procedure”: A new tool

GuanghuiQinandJasonEisner.2021. Learninghowto formeasuringreadability. Journalismquarterly.
ask: Querying lms with mixtures of soft prompts. In
AhmetÜstün,AriannaBisazza,GosseBouma,andGert-

## Naacl.

jan van Noord. 2020. Udapter: Language adaptation
fortrulyuniversaldependencyparsing. InEMNLP.

### Alec Radford, Karthik Narasimhan, Tim Salimans,

and Ilya Sutskever. 2018. Improving language Ellen M Voorhees and Dawn M Tice. 2000. Building a
understandingbygenerativepre-training. questionansweringtestcollection. InSIGIR.
Alec Radford, Jeffrey Wu, Rewon Child, David Luan, Alex Wang, Yada Pruksachatkun, Nikita Nangia, Aman-
DarioAmodei, andIlyaSutskever. Languagemodels preet Singh, Julian Michael, Felix Hill, Omer Levy,
areunsupervisedmultitasklearners. and Samuel R Bowman. 2019a. Superglue: a
stickier benchmark for general-purpose language
Colin Raffel, Noam Shazeer, Adam Roberts, Katherine understandingsystems. InNeurIPS.

### Lee, Sharan Narang, Michael Matena, Yanqi Zhou,

AlexWang,AmanpreetSingh,JulianMichael,FelixHill,
WeiLi,andPeterJLiu.2020. Exploringthelimitsof

### OmerLevy, andSamuelR.Bowman.2019b. GLUE:

transferlearningwithaunifiedtext-to-texttransformer.
JMLR. A multi-task benchmark and analysis platform for
naturallanguageunderstanding. InICLR.
Pranav Rajpurkar, Jian Zhang, Konstantin Lopyrev, and
AlbertWebsonandElliePavlick.2021. Doprompt-based
Percy Liang. 2016. Squad: 100,000+ questions for
modelsreallyunderstandthemeaningoftheirprompts?
machinecomprehensionoftext. InEMNLP.
arXivpreprintarXiv:2109.01247.
Shauli Ravfogel, Elad Ben-Zaken, and Yoav Goldberg. Thomas Wolf, Lysandre Debut, Victor Sanh, Julien

## Bitfit: Simple parameter-efficient fine-tuning Chaumond, ClementDelangue, AnthonyMoi, Pierric

for transformer-based masked languagemodels. Cistac,TimRault,RémiLouf,MorganFuntowicz,Joe
arXiv:2106.10199. Davison, Sam Shleifer, Patrick von Platen, Clara Ma,

### YacineJernite,JulienPlu,CanwenXu,TevenLeScao,

Sylvestre-Alvise Rebuffi, Hakan Bilen, and Andrea SylvainGugger,MariamaDrame,QuentinLhoest,and
Vedaldi. 2018. Efficient parametrization of multi- AlexanderM.Rush.2020. Transformers: State-of-thedomaindeepneuralnetworks. InCVPR. art natural language processing. In EMNLP: System
Demonstrations.
TimoSchick,HelmutSchmid,andHinrichSchütze.2020.
Automatically identifying words that can serve as Aston Zhang, Yi Tay, SHUAI Zhang, Alvin Chan,
labelsforfew-shottextclassification. InCOLING. Anh Tuan Luu, Siu Hui, and Jie Fu. 2021. Beyond
fully-connected layers with quaternions: Parame-
Timo Schick and Hinrich Schütze. 2021a. Exploiting terization of hypercomplex multiplications with 1/n
cloze-questions for few-shot text classification and parameters. InICLR.
naturallanguageinference. InEACL.
Tianyi Zhang, Felix Wu, Arzoo Katiyar, Kilian Q Weinberger, and Yoav Artzi. 2020. Revisiting few-sample
Timo Schick and Hinrich Schütze. 2021b. It’s not just
bertfine-tuning. InICLR.
size that matters: Small language models are also
few-shotlearners. InNAACL.
Tony Z. Zhao, Eric Wallace, Shi Feng, Dan Klein, and

### SameerSingh.2021. Calibratebeforeuse: Improving

KarinKipperSchuler.2005. Verbnet: Abroad-coverage,
few-shotperformanceoflanguagemodels. ICML.
comprehensiveverblexicon. PhDThesis.

<!-- Page 12 -->

Dataset Task #Train #Test K a higher value of 10−4.7 Through all experiments,
wefixtheadapterbottlenecksizeto64. Following

### Single-SentenceBenchmarks

Pfeifferetal.(2021),weexperimentedwithkeeping

### MR Sentimentanalysis 8662 2000 2

one of the adapters in each layer for better training

### CR Sentimentanalysis 1774 2000 2

efficiency and found keeping the adapter after the

### SST-2 Sentimentanalysis 6920 872 2

feed-forwardmoduleineachlayertoperformthebest.

### SST-5 Sentimentanalysis 8544 2210 5

Fortuninglabelembedding,weusethelearningrate

### SUBJ Subjectivityclassification 8000 2000 2

of {10−1,10−2,10−3,10−4,10−5} and choose the

### TREC Questionclassification 5452 500 6

oneobtainingthehighestvalidationperformance. For

### Sentence-PairBenchmarks


### PERFECT-prompt, we tune the continuous prompt

CB Naturallanguageinference 250 56 3 for learning rate of {10−1,10−2,10−3}.8Following
RTE Naturallanguageinference 2490 277 2 Lester et al. (2021), for PERFECT-prompt, we set

### WiC Wordsensedisambiguation 5428 638 2

the number of prompt tokens to 20, and initialize

### MRPC Paraphrasedetection 3668 408 2

themwitharandomsubsetofthetop5000token’s

### QNLI Questionanswering 104743 5463 2

embedding of the PLM. We train all methods for

### QQP Paraphrasedetection 363846 40430 2

6000steps. Basedonourresults,thisissufficientto
allowthemodelstoconverge. Wesaveacheckpoint

### Table6:Statisticsofdatasetsusedinthiswork.Wesample

N×|Y|instances(withmultipleseeds)fromtheoriginal every100stepsforallmethodsandreporttheresults
training set to form the few-shot training and validation forthehyper-parametersperformingthebestonthe
sets.Thetestcolumnshowsthesizeofthetestset. validationsetforeachtask.
B ChoiceofPatternsandVerbalizers

### A ExperimentalDetails


### For SST-2, MR, CR, SST-5, and TREC, we used

Datasets Table 6 shows the stastistics of the 4 different patterns and verbalizers from Gao et al.
datasetsused. WedownloadSST-2,MR,CR,SST-5, (2021). For CB, WiC, RTE datasets, we used the
andSUBJfromGaoetal.(2021), whiletherestof designed patterns and verbalizers in Schick and
thedatasetsaredownloadedfromtheHuggingFace Schütze(2021b). ForQQP,MRPC,andQNLI,we
Datasets library (Lhoest et al., 2021b,a). RTE, CB, wrotethepatternsandverbalizersinspiredbytheones
WiCdatasetsarefromSuperGLUEbenchmark(Wang in Schick and Schütze (2021b). The used patterns
etal.,2019a),whileQQP,MRPCandQNLIarefrom andverbalizersareasfollows:
GLUEbenchmark(Wangetal.,2019b)withCreative
• Forsentimentanalysistasks(MR,CR,SST-2,
Commonslicense(CCBY4.0). RTE(Wangetal.,

### SST-5),givenasentences:

2019a)isacombinationofdatafromRTE1(Dagan
etal.,2005),RTE2(Bar-Haimetal.,2006),RTE3(GisA<MASK>one.
ampiccoloetal.,2007),andRTE5(Bentivoglietal.,
2009). For WiC (Pilehvar and Camacho-Collados,
2019)sentencesareselectedfromVerbNet(Schuler, sItwas<MASK>.
2005),WordNet(Miller,1995),andWiktionary.
Computing infrastructure We run all the exper- sAllinall<MASK>.
imentsononeNVIDIAA100with40Gofmemory.
sA<MASK>piece.

### Traininghyper-parameters Wesetthemaximum

sequencelengthbasedontherecommendedvalues
in the HuggingFace repository (Wolf et al., 2020) with"great"asaverbalizerforpositive,"terrible"
andpriorwork(Minetal.,2021;SchickandSchütze, fornegative. IncaseofSST-5withfivelabels,
2021b),i.e.,wesetitto256forSUBJ,CR,CB,RTE, weexpanditto"great","good","okay","bad",
andWiC,and128forotherdatasets. Forallmethods, and"terrible".
weuseabatchsizeof32. ForFINETUNEandPET, 7Wehavealsotriedtotunethebaselineswiththelearning
we use the default learning rate of 10−5, while for rateof10−4butitperformedworst.
8We also tried tuning prompts with learning rates of
our method, as required by adapter-based methods
{10−4,10−5}butitperformedworst,asalsoobservedinprior
(Mahabadietal.,2021a),wesetthelearningrateto work(Mahabadietal.,2021a;Minetal.,2021).

<!-- Page 13 -->

• ForSUBJ,givenasentences: • Forentailmenttask(CB)givenapremisepand
ahypothesish:
sThisis<MASK>.
"h"?|<MASK>,"p"
sIt’sall<MASK>.
h?|<MASK>,p
sIt’s<MASK>.
"h"?|<MASK>.p
sIsit<MASK>?
with"Yes"asaverbalizerforentailment,"No"
forcontradiction,"Maybe"forneutral.
with"subjective"and"objective"asverbalizers.
• For TREC, given a question q, the task is to p question: h true, false or neither? answer:

## <Mask>

classifythetypeofit:
q<MASK>: with"true"asaverbalizerforentailment,"false"
forcontradiction,"neither"forneutral.
• ForQNLI,givenasentencesandquestionq:
qQ:<MASK>:
s.Question:q?Answer:<MASK>.
qwhy<MASK>?
with"Yes"or"true"asverbalizersforentailment
and"No"or"false"fornotentailment.
qAnswer:<MASK>.
s.Basedontheprevioussentence,q?<MASK>.
with "Description", "Entity", "Expression",
"Human","Location","Number"asverbalizers with"Yes"or"true"asverbalizersforentailment
for question types of "Description", "Entity", and"No"or"false"fornotentailment.
"Abbreviation", "Human", "Location", and
"Numeric". Basedonthefollowingsentence,q?<MASK>.s
• For entailment task (RTE) given a premise p
with "Yes" and "No" as verbalizers for
andhypothesish:
entailmentandnotentailmentrespectively.
"h"?|<MASK>,"p" • ForQQP,giventwoquestionsq andq :
1 2
Doq andq havethesamemeaning?<MASK>.
1 2
h?|<MASK>,p
with"Yes"or"true"asverbalizersforduplicate
and"No"or"false"fornotduplicate.
"h"?|<MASK>.p
q . Based on the previous question, q ?
1 2
with"Yes"asaverbalizerforentailment,"No"

## <Mask>.

forcontradiction.
with"Yes"or"true"asverbalizersforduplicate
pquestion:hTrueorFalse?answer:<MASK>
and"No"or"false"fornotduplicate.
with"true"asaverbalizerforentailment,"false"
Basedonthefollowingquestion,q ?<MASK>.q
1 2
forcontradiction.

<!-- Page 14 -->

with"Yes"and"No"asverbalizersforduplicate Datasets 1 2 3 4
andnotduplicaterespectively.

## Cb 89.8 91.6 88.9 86.5

• ForMRPC,giventwosentencess ands : RTE 69.1 69.1 64.5 65.3
1 2

## Qnli 72.0 83.3 77.7 73.1

Dos ands havethesamemeaning?<MASK>. MRPC 71.6 69.5 66.4 72.0
1 2

## Qqp 79.2 82.8 72.5 70.2


### WiC 60.3 59.5 60.2 59.5

with"Yes"or"true"asverbalizersforequivalent
and"No"or"false"fornotequivalent. Avg 73.7 76.0 71.7 71.1
s . Based on the previous sentence, s ? Table7: Validationperformanceforsentence-pairbench-
1 2
<MASK>. marksfordifferentlocationsofmasktokens. Boldfonts
indicatethebestresultsineachrow.
with"Yes"or"true"asverbalizersforequivalent

### Datasets 10−2 10−3 10−4 10−5

and"No"or"false"fornotequivalent.

## Cb 90.0 92.2 91.6 91.6

/82.5 /85.0 /87.5 /87.5
Based on the following sentence, MRPC 69.8 /56.2 70.8 /56.2 69.5 /56.2 70.8 /56.2
s 1 ?<MASK>.s 2 QNLI 83.3 /71.9 82.7 /71.9 83.3 /71.9 83.1 /68.8

## Qqp 82.8 82.7 82.8 83.0

/78.1 /75.0 /75.0 /75.0
with"Yes"and"No"asverbalizersforequivalent RTE 69.8 /62.5 69.2 /59.4 69.1 /62.5 68.3 /62.5
andnotequivalentrespectively. WiC 62.2 /50.0 59.7 /46.9 59.5 /53.1 58.9 /50.0

### Avg 76.3 76.2 76.0 76.0

• ForWiC,giventwosentencess ands anda /66.9 /65.7 /67.7 /66.7
1 2
wordw,thetaskistoclassifywhetherwisused TotalAvg 71.6 71.0 71.8 71.3
inthesamesense.

### Table 8: Validation performance for different values of

"s 1 "/"s 2 ".Similarsenseof"w"?<MASK>. σ. We show mean performance/worst-case performance
across20runs. Thelastrowshowstheaverageofmean
performance/worst-caseperformance.
s s Doesw havethesamemeaninginboth
1 2
sentences?<MASK>
4. s |s <MASK>
1 2
With "No" and "Yes" as verbalizers for False, Table7showshowthepositionofmasksimpact
andTrue. the results. As demonstrated, pattern 2, inserting
masktokensbetweenthetwosentencesandencoding
w.Sense(1)(a)"s "(<MASK>)"s " both as a single sentence obtains the highest
1 2
validationperformance. Weusethischoiceinallthe
experimentswhenremovinghandcraftedpatterns.
With "2" and "b" as verbalizers for False, and
True.
D ImpactofInitialization

### C ImpactofthePosition

Weinitializethelabelembeddingmatrixwithrandom
ofMasksinSentence-pairDatasets
initializationfromanormaldistributionN(0,σ). In
table8,weshowthedevelopmentresultsfordifferent
Weevaluatetheimpactofthepositionofmasktokens
valuesofσ. Wechoosetheσ obtainingthehighest
insentence-pairbenchmarks. Giventwosentencess
1
performanceonaverageoveraverageandworstcase
ands ,weconsiderthefollowingfourlocationsfor
2
performance,i.e.,σ=10−4.
insertingmasktokens,whereinthecaseofencoding
as two sentences, input parts to the encoder are
E AblationResults
separatedwith|:

### To study the impact of different design choices in

1. s 1 s 2 <MASK> PERFECT,weconsideredthefollowingexperiments:
2. s 1 <MASK>s 2 • -Hinge Loss: In this variant, we replace the
3. s |<MASK>s hingelosswithmulti-classcrossentropyloss.
1 2

<!-- Page 15 -->


### Dataset PERFECT -HingeLoss +LabelEmb -Prototypical


## Sst-2 90.7/88.2/1.2 90.0/85.9/1.7 90.6/87.6/1.1 90.4/85.2/1.6


## Cr 90.0/85.5/1.4 90.1/88.6/0.9 89.7/86.6/1.4 89.9/86.8/1.4


## Mr 86.3/81.4/1.6 85.2/78.6/2.4 85.8/82.4/1.4 85.7/78.0/2.0


## Sst-5 42.7/35.1/2.9 43.3/36.8/3.1 41.8/37.1/2.5 41.2/35.9/2.4


## Subj 89.1/82.8/2.1 89.4/83.1/2.2 90.0/86.0/1.8 89.7/86.0/1.8


## Trec 90.6/81.6/3.2 89.9/76.8/4.2 89.7/71.6/6.1 89.6/76.2/4.9


## Cb 90.3/83.9/3.5 89.2/80.4/4.8 89.6/82.1/3.6 89.3/80.4/3.9


## Rte 60.4/53.1/4.7 60.7/54.5/4.0 58.6/50.9/4.0 58.5/50.9/4.5


## Qnli 74.1/60.3/4.6 72.9/64.4/3.9 74.9/66.7/3.6 74.7/67.5/3.5


## Mrpc 67.8/54.7/5.7 67.0/49.8/5.5 68.1/56.9/4.8 68.1/56.9/4.8


## Qqp 71.2/64.2/3.5 69.9/63.0/4.1 70.3/62.2/4.0 70.2/62.2/4.0

WiC 53.8/47.0/3.0 53.7/46.7/3.3 53.6/50.2/2.4 53.6/50.0/2.6

### Avg 75.6/68.1/3.1 75.1/67.4/3.3 75.2/68.4/3.1 75.1/68.0/3.1

Table9:AblationresultsontheimpactofdifferentdesignchoicesinPERFECT.Wereporttheaverageperformance/worstcaseperformance/andthestandarddeviation.
• +Label Emb: We use the trained label embeddingsduringtheinference,substitutingthe
computedprototypesin(5).
• -Prototypical: Instead of using prototypical
networks, during inference, we use the same
objectiveastraining,i.e.,(4).

### ResultsareshowninTable9. Experimentalresults

demonstrate that PERFECT obtains the best results
onaverage. Usingmulti-classcross-entropyinstead
ofhingeloss, obtainssubstantiallylowerminimum
performance(67.4versus68.1), demonstratingthat
training with hinge loss makes the model more
stable. Usingthetrainedlabelembeddings(+Label
Emb)obtainsverycloseresultstoPERFECT(slightly
worseonaverageandslightlybetterontheminimum
performance). Usingthesimilarobjectiveastraining
withreplacingprototypicalnetworks(-Prototypical),
obtains lower performance on average (75.1 versus
75.6). These results confirmthe design choices for

## Perfect.


## Tables

**Table (Page 1):**

| Input |  | Pattern |  |
|---|---|---|---|
|  |  |  |  |
|  |  |  | [MASK] |


**Table (Page 14):**

| s s <MASK> 1 2 |
|---|
| s <MASK>s 1 2 |
| s \|<MASK>s 1 2 |
