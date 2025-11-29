---
title: "Exploring Prompt Based Few Shot Dialog"
original_file: "./21_Exploring_Prompt_Based_Few_Shot_Dialog.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["prompt-engineering", "llm", "rag", "agents", "fine-tuning"]
keywords: ["eos", "user", "system", "knowledge", "encoder", "nsystem", "decoder", "bos", "grounded", "noprompts"]
summary: "<!-- Page 1 -->

Exploring Prompt-based Few-shot Learning for
Grounded Dialog Generation

### ChujieZheng,MinlieHuang

TheCoAIGroup,DCST,InstituteforArtificialIntelligence,

### StateKeyLabofIntelligentTechnologyandSystems,

BeijingNationalResearchCenterforInformationScienceandTechnology,

### TsinghuaUniversity,Beijing100084,China

chujiezhengchn@gmail.com, aihuang@tsinghua.edu.cn

### Abstract


### Dialog models can be greatly strengthened

through grounding on various external information, b"
related_documents: []
---

# Exploring Prompt Based Few Shot Dialog

<!-- Page 1 -->

Exploring Prompt-based Few-shot Learning for
Grounded Dialog Generation

### ChujieZheng,MinlieHuang

TheCoAIGroup,DCST,InstituteforArtificialIntelligence,

### StateKeyLabofIntelligentTechnologyandSystems,

BeijingNationalResearchCenterforInformationScienceandTechnology,

### TsinghuaUniversity,Beijing100084,China

chujiezhengchn@gmail.com, aihuang@tsinghua.edu.cn

### Abstract


### Dialog models can be greatly strengthened

through grounding on various external information, but grounded dialog corpora are usuallynotnaturallyaccessible. Inthiswork,we
focusonthefew-shotlearningforgroundeddialoggeneration(GDG).Wefirstproposeasimple prompting method for GDG tasks, where
differentconstructsofmodelinput,suchasthe
groundingsourceandtheconversationcontext,
are distinguished through continuous or discreteprompts.OnthreetypicalGDGtasks,we Figure1: Overviewoftheeffectsofprompting. Model
empirically demonstrate and analyze in-depth performanceismeasuredbyBLEU-2. Fullexperimentheeffectivenessofourmethod. Wethencon- talresultsareshowninTable4. Detailedexperimental
duct extensive experiments to thoroughly in- setupsaredescribedin§4.
vestigate how our prompting method works
with different pre-trained models. We show

### Comparedtogeneraldialoggeneration, where

thatpromptedlanguagemodelsperformsupetheresponseisonlyconditionedontheconversariorlytoconversationalmodels,andfurtherantion context, grounded dialog generation (GDG)
alyzevariousfactorsthatinfluencetheeffects
containstheothercondition: thegroundingsource
of prompting. Overall, our work introduces
a prompt-based perspective to the few-shot (GS). We regard that this additional condition
learningforGDGtasks,andprovidesvaluable bringstwomajorchallengestoGDGtasks. First,
findingsandinsightsforfutureresearch. themodelsneedtodiscriminatethemorecomplex
input constructs (not only utterances from differ-
1 Introduction ent speakers, but also distinct input components,
i.e., the GS and the conversation context). Sec-
Previousworkshavegreatlyenhanceddialogmodond,theconceptof“grounding”istooabstractfor
elsthroughgroundingmodel-generateddialogson
modelstograsptherelationshipbetweenthetarget
variousexternalinformation(Ghazvininejadetal.,
responseandtheGSandfurtherlearnhowtouse
2018;Huangetal.,2020),suchasWikipediadocthe information of the GS. These challenges are
uments(Dinanetal.,2018),personadescriptions
evenmoreintractableunderthefew-shotsetting.
(Zhangetal.,2018)oremotionalsupportstrategies

### Inspiredbyrecentadvancesinpre-trainedmod-

(Liuetal.,2021c). However,groundeddialogcorelsandprompt-basedlearning(Liuetal.,2021a),
porausuallydonotnaturallyexistandaremostly
which has shown impressive results in few-shot
collectedviacrowd-sourcing,whichcouldrestrict
learning for various NLP tasks, in this paper we
thescaleofaccessibledata. Hence,theabilityof
indepthexploresprompt-basedfew-shotlearning
few-shotlearning1 becomesincreasinglynecessary
forgroundeddialoggeneration. Asfarasweknow,
forgroundeddialogmodels.
thisworkisthefirstattemptthatappliestheprompt-
1Inthefew-shotlearningsettingofthiswork,weassume ingmethodtoboostthefew-shotlearningperforthatonlyasmallamountofdatasamplesareaccessibleand manceforGDGtasks. Ourcontributionsfallinto
noadditionaldataisused,whichisthusdistinctfromworks
thefollowingtwoaspects.
thataddressthelow-resourcelearningviapre-trainingonextra
corpora(Zhaoetal.,2020;Lietal.,2020;Liuetal.,2021b). First, we propose a simple prompting method
2202
naJ
41
]LC.sc[
2v31560.9012:viXra

<!-- Page 2 -->

A lifeguard is a rescuer who supervises the I am an artist Seeker I feel so frustrated.
safety and rescue of swimmers, surfers, and I have fourchildren
[Question]
other water sports participantssuch as in a I recently got a cat

### Persona Supporter May I ask why you are feeling

Wikipedia swimming pool, water park, beach, spa, river I enjoy walking for exercise
frustrated?
(Lifeguard) and lake…In some areas, lifeguards are part I love watching Game of
of the emergency services system to incidents Thrones My school was closed without any prior

### Seeker

and in some communities, lifeguards may warning due to the pandemic.

### Speaker1 Hi

function as the primary EMS provider.
[Self-disclosure]

### Speaker2 Hello ! How are you today ?

So I am a lifeguard. Know anything about I understand you. I would also have

### Apprentice Supporter

saving lives in water? I am good thank you , how been really frustrated if that happened

### Speaker1

are you. to me.

### I’m impressed! It’s a big responsibility to

Wizard supervise other people’s safety in the water! Great, thanks ! My children Yeah! I don't even know what is going

### Seeker

Tell me more. Speaker2 and I were just about to to happen with our final.
watch Game of Thrones.
Well, I help make sure people do not drown or [Reflection of Feelings]

### Apprentice Supporter

get injured while in or near the water! Nice ! How old are your That is really upsetting and stressful.

### Speaker1

children?
I’ve heard that in some places, lifeguards also [Providing Suggestions]
Wizard help with other sorts of emergencies, like I have fourthat range in age Supporter Have you thought about talking to your

### Speaker2

mountain rescues! from 10 to 21. You? parents or a close friend about this?
Figure 2: Examples of grounded dialogs from Wizard-of-Wikipedia (Dinan et al., 2018), PersonaChat (Zhang
etal.,2018)andESConv(Liuetal.,2021c),whicharegroundedontheWikipediaknowledge(left),thepersona
profile(middle)andtheemotionalsupportstrategies(right)respectively. Thepartsofgroundingsourcesthatthe
utterancesareengagedinaremarkedinblue.
forGDGtasks,wherethecomplexinputconstructs Grounded Dialog Generation (GDG) In the
(i.e.,distinctinputcomponentsanddifferentspeak- pastfewyears,researchersareincreasinglyinterers’utterances)aredistinguishedthroughcontinu- estedingroundingmachine-generateddialogson
ousordiscreteprompts,asillustratedinFigure3. variousexternalinformation(Ghazvininejadetal.,
TakingGPT2-mediumasthebackbonemodel,we 2018;Zhouetal.,2018a,b;Gopalakrishnanetal.,
empiricallyverifyandanalyzetheeffectivenessof 2019; Zheng et al., 2020; Zhou et al., 2020). As
ourproposedmethod(§5). shown in Figure 2, (Dinan et al., 2018) utilizes
Second, we conduct extensive experiments to Wikipedia documents as the background knowlthoroughlyinvestigatehowourpromptingmethod edge. (Zhang et al., 2018) equips conversational
works with different pre-trained models. Results agents with pre-defined persona profiles to make
demonstratethatpromptedlanguagemodels(e.g., themmoreengaging. (Liuetal.,2021c)groundson
GPT2andT5)canachievesuperiorperformance diverseemotionalsupportstrategies,enablingdiato conversational models (e.g., DialoGPT and logmodelstobemoreempatheticandtoprovide
Blender)(Figure1and§6.2),andvariousfactors moreeffectiveemotionalsupport.
alsoinfluencetheeffectsofprompting(§6.3). The Low-resource Learning for GDG Leveraging
keyfindingsinourworkaresummarizedin§3. pre-trainingtechniques,recentworksalsomadeattempstoaddressGDGtasksunderalow-resource
2 RelatedWork
setting(Zhaoetal.,2020;Lietal.,2020;Liuetal.,
2021b). Our work is distinguished from these in
Pre-trainingandPrompt-basedLearning Rethatinsteadoffacilitatingdownstreamfine-tuning
cently, pre-trained models have shown the draviapre-trainingonextracorpora,wefocusonmakmatic utility in various NLP tasks (Devlin et al.,
ingthemostuseofaccessibledatasamplestoper-
2019; Radford et al., 2019; Raffel et al., 2020),
formfew-shotlearning. Whileonecanexpectthat
whichlearngeneral-purposelanguagerepresentacombiningourpromptingmethodwithpreviously
tion through pre-training on massive textual data
adoptedpre-trainingtechniqueswouldleadtobetwithunsupervisedlearningobjectives. Thepromptterfew-shotlearningperformance,wedonotspebased learning further takes the power of preciallyevaluatethisbutleaveitforfuturework.
trainedmodelstounprecedentedheights,especially
intermsoffew-shotlearning(Brownetal.,2020).
3 KeyFindings
Inthisparadigm,thepre-trainedmodelsarestimulatedtosolvedownstreamtasksthroughinserting Our work evaluates the proposed prompting
discreteorcontinuouspromptsintoeitheroriginal method(§5)andinvestigatesitseffectivenesswith
modelinputs(SchickandSchütze,2021)orhidden differentpre-trainedmodels(§6). Thekeyfindings
states (Li and Liang, 2021). We refer readers to aresummarizedasfollows.
(Liuetal.,2021a)foracomprehensivesurvey. 1. Distinguishing the input constructs is an ef-

<!-- Page 3 -->


### NoPrompts NoPrompts

{knowledge}<eos> {utterance1}<eos><Reflection of Feelings>{utterance2}<eos>
{utterance1}<eos>{utterance2}<eos> {utterance3}<eos><Self-disclosure>{utterance4}<eos>
{utterance3}<eos>{utterance4}<eos>

### ContinuousPrompts


### ContinuousPrompts <user>{utterance1}<eos>

<knowledge>{knowledge}<context> <system><Reflection of Feelings>{utterance2}<eos>
<user>{utterance1}<eos><system>{utterance2}<eos> <user>{utterance3}<eos>
<user>{utterance3}<eos><system>{utterance4}<eos> <system><Self-disclosure>{utterance4}<eos>

### DiscretePrompts DiscretePrompts

The following is a conversation between a user and a The following is a conversation between a user and an
knowledgeable system.The system’s utterances are empathetic system.The system can use various support skills
grounded on the background knowledge:\n to provide emotional support to the user.\n
{knowledge}\n User:{utterance1}\n
Conversationcontext:\n Systemreflects and describes user’s feelings:{utterance2}\n
User:{utterance1}\nSystem:{utterance2}\n User:{utterance3}\n
User:{utterance3}\nSystem:{utterance4}\n Systemshares similar experiences or emotions:{utterance4}\n
Figure 3: Illustration of our prompting method. Our method inserts indicative tokens (middle, Continuous
Prompts) or textual descriptions (lower, Discrete Prompts) into input sequences to distinguish different input
constructs. For the discrete prompts, we also prepend input sequences with task instructions. All the model
parametersaretrainedwiththenegativeloglikelihoodlossonthetargetresponses(theendtoken,either“<eos>”
orthelinebreak“\n”,isunderlined).
fectiveapproachtoboostthefew-shotlearning WoW PC ESConv
performance for GDG tasks (§5.1). However, DataSplit
poorlyinitializedpromptswouldinsteaddamage
Train 66K 50K 12K

### Full-data

modellearningandleadtopoorperformance. Valid 7K 6K 3K

## Discrete prompts generally outperform con- Train 50

Few-shot

### Valid 15

tinuous prompts under both few-shot and fulldata settings (§5.2). In particular, minor pertur- Test 3K
bations do not result in significant performance SequenceLength
fluctuation. Itindicatesthepracticabilityofmanu- Context
(5Utterances)
68.5≤269 52.3≤95 90.2≤427
allycrafteddiscretepromptsandthatitmaybenot

### GroundingSource 224.0≤368 34.5≤53 -

necessarytooptimizethemlaboriously. Response 22.6≤90 13.3≤25 21.6≤155

## Prompted language models are superior to


### TruncationLength

conversational models (§6.2). Despite that our

### Context 250 150 250

promptingmethodgreatlybenefitslanguagemod- GroundingSource 300 100 -
els,itdoesnotworkwithconversationalmodels. Response 50 25 50

## Our prompting method works across differ-

Table 1: Data statistics. Each (context, response) pair
ent model architectures, while its effectiveness
isviewedasonedatasample.Sequencelengthsarecalalso relies on backbone models with enough culatedonthetestsets(withGPT2tokenization). Subprowess (§6.3). Specifically, prompting is espe- scripts“≤x”denotesthemaxlengthinthetestsetisx.
ciallyeffectiveifthebackbonemodelshavelarge Thecontextsaretruncatedattheleftwhilethegroundenoughsizesandarepre-trainedwithgeneralpre- ingsourcesandtheresponsesareattheright.
trainingobjectives(e.g.,languagemodeling).
model-sideutteranceeitherreferstoaknowledge
4 ExperimentalSetups sentence from the first paragraph of the selected
Wikipediaentryordoesnotrefertoanyknowledge.
4.1 DataPreparation

### Weremovedthedatasampleswheretheresponses

Ourexperimentswereconductedonthreetypical donotuseknowledgereference,andusedthefirst
GDG tasks: Wizard-of-Wikipedia, PersonaChat paragraph of the selected Wikipedia entry as the
and ESConv. Their data examples are shown in GSforeachsample.
Figure2,andthestatisticsarelistedinTable1. PersonaChat (PC) (Zhang et al., 2018) is a
Wizard-of-Wikipedia(WoW)(Dinanetal.,2018) persona-grounded dialog task, where the model
is a knowledge-grounded dialog task, where the isassignedwithapre-definedprofileconsistingof
modelmakesuseofWikipediadocumentstocon- severaltextualpersonadescriptions. Weremoved
verse and provide information. In WoW, each thedatasampleswheretheresponsesdonothave

<!-- Page 4 -->

any non-stop word overlap with the persona pro- plexity(PPL)(Zhangetal.,2018)reflectsthetask
files(usingtheNLTKstopwordlist). adaptationabilitybycalculatingthelossonthetest
ESConv (Liu et al., 2021c) is a support strategy- samples. BLEU-n(Papinenietal.,2002;Liuetal.,
grounded dialog task, where the model uses var- 2021c)reflectsthegrammaticalityandcontextual
ious support strategies to provide emotional sup- coherencebycomputingthen-gramoverlapswith
porttothehelp-seekers. Notethatdifferentfrom golden responses. We reported the corpus-level
WoWandPCwhereGSisintheformofunstruc- BLEU-2(B-2)scores. UnigramF1(Dinanetal.,
turedtexts, ESConvtakesdiscreteconcepts(sup- 2018;Zhaoetal.,2020)measuresthelexicalsimportstrategies)astheGS,whicharemoreabstract ilarity between generated and golden responses
andhavemorecomplexmeanings. (withNLTKtokenization).
WoW and PC adopted the official data split, Toevaluatethegroundednessofgeneration,we
whileESConvwasmanuallysplitinto12K/3K/3K. further used another two metrics. For WoW and
Note that for the sake of experimental efficiency, PC, we computed Wiki/PSN F1 (Dinan et al.,
for WoW and PC we held 3K test samples2. For 2018; Shuster et al., 2021) as the unigram F1 bethefew-shotsetting,werandomlysampled50/15 tweenmodel-generatedresponsesandthegrounddatasamplesfromtheoriginaltraining/validation ing sources (i.e., Wikipedia knowledge and persets,usingtheproportionsin(LiandLiang,2021). sona). Note that to truly reflect the informative
Wedidfourrandomsamplingstoobtainfourdif- referred contents, we only counted the non-stop
ferentsubsets,andrantworandomseedsforeach words as overlapped unigrams. For ESConv, we
subset. Consequently, each reported final experi- computedMatchRatioastheratioofcaseswhere
mentalresultwasobtainedbyaveragingoneight the strategies identified from the generated re-
(4*2)differentoriginalresults. sponsesexactlymatchedthedesignatedones3. To
identifytheresponses’strategies,wefine-tuneda
4.2 ImplementationDetails

### BERT-Large(Devlinetal.,2019)classifieronthe

Training We trained all the model parameters full training set of ESConv, which obtained 57.5
duringfine-tuning. Unlessotherwisespecified,for accuracy,86.4Hits@3and51.4macro-F1onthe
thefew-shotsettingandforallthemodelsandall testset(8-class).
the tasks, we employed the AdamW (Loshchilov Weconductedsignificancetestsusingbootstrap
andHutter,2018)optimizerwithbatchsize5and resampling (Berg-Kirkpatrick et al., 2012) for
learningrate2e-5,andusedthelinearlearningrate BLEU, Students’ t-test for F1 and Wiki/PSN F1,
scheduler with warmup steps 5. Gradient check- and sign test for Match Ratio. Since the sample
pointing was applied to reduce GPU memory oc- sizeaffectsstatisticalsignificance,forthefew-shot
cupation. Modelsweretrainedfor10epochs,and experiments, we evenly sampled from the eight
checkpoints were selected based on the perplex- generationsetstoconstructanon-repetitivesample
ityonvaidationsets. Forthefull-datasetting,the setforsignificancetests.
learningrateandtrainingepochnumberwere1e-5
5 PromptingGPT2
and5respectively.

### Inference For WoW, following (Zhao et al.,

In the implementation of our prompting method,
2020;Lietal.,2020),weemployedbeamsearch
continuous prompts work via the newly added
with a beam size 3. For PC and ESConv, followindicative tokens, while discrete prompts introing(Wolfetal.,2019;Liuetal.,2021c),weaddiduce no new parameters but only textual descriptionallyadoptedTop-psampling(Holtzmanetal.,
tions. Whileintuitivelyreasonable,thetwotypes
2019) (temperature τ = 0.7 and p = 0.9). For
ofpromptsmayhavetheirownshortcomingsun-

### WoWandESConv,themin/maxgenerationlengths

der the few-shot learning setting, as revealed in
were10/50respectively,whilePCwas5/25.
previousworks(Liuetal.,2021a). Specifically,the
initialization of continuous prompts could sensi-
4.3 EvaluationMetrics
tivelyaffectfew-shotlearningperformance(Liand

### Weadoptedthefollowingautomaticmetricstoeval-

Liang,2021;Guetal.,2021),andevenminorperuatethequalityofmodel-generatedresponses. Per-
3ESConvdefines7supportstrategiesalongwithan“others”
2Due to that WoW has an in-domain and the other out- one,whichdoesnotexplicitlyrefertoanyspecificstrategy.
of-domaintestset, weheld1.5Ksamplesfromeachsetto We removed the cases where the designated strategies are
constructthewholetestsamples(totally3K). “others”whencomputingmatchratio.

<!-- Page 5 -->


### Wizard-of-Wikipedia PersonaChat ESConv

PPL↓ B-2 F1 WikiF1 PPL↓ B-2 F1 PSNF1 PPL↓ B-2 F1 Match

### Full-data(66K) Full-data(50K) Full-data(12K)

w/oGS 17.7 8.5∗∗ 21.9∗∗ 4.0∗∗ 15.2 10.9∗∗ 25.3∗∗ 6.6∗∗ 15.1 6.6∗∗ 20.6∗∗ 20.7∗∗
Random 9.0 15.5 28.0 9.1 11.4 12.2 26.6 11.8 14.7 7.6∗ 22.5 40.6∗∗
Semantic 9.0 15.3 27.9 8.9 11.3 12.0 26.7 11.6 14.5 7.9 22.9 57.4
NoPrompts 9.1 15.1∗ 27.5 9.0 11.4 11.7∗∗ 26.5 11.7 14.6 7.6∗∗ 22.7 57.3

### Few-shot(50)

w/oGS 26.50.2 5.8∗
0.
∗
2
17.7∗
0.
∗
5
3.1∗
0.
∗
2
26.30.5 7.1∗
0.
∗
7
20.1∗
1.
∗
0
5.0∗
0.
∗
7
21.10.1 5.4∗
0.
∗
5
16.5∗
0.
∗
8
12.8∗
1.
∗
8
Random 101.625.1 5.6∗
1.
∗
4
16.9∗
2.
∗
6
3.4∗
0.
∗
9
51.316.4 7.3∗
1.
∗
1
19.9∗
2.
∗
6
6.1∗
1.
∗
6
72.018.8 5.1∗
0.
∗
6
16.0∗
0.
∗
8
12.5∗
1.
∗
1
Vocab 13.50.2 10.3∗
0.
∗
4
20.90.2 7.0∗
0.
∗
4
20.60.9 8.6∗
0.
∗
7
21.50.7 8.8∗
2.
∗
6
20.80.2 6.1∗
0.
∗
8
17.4∗
0.
∗
6
16.6∗
1.
∗
1
Frequent 13.90.1 10.9∗
0.5
21.00.2 7.80.6 21.20.9 8.4∗
0.
∗
6
21.50.6 8.3∗
2.
∗
2
21.30.2 5.8∗
0.
∗
8
17.3∗
0.
∗
7
17.0∗
1.
∗
7
Semantic 13.3 0.1 11.1 0.4 21.3 0.3 8.3 0.4 20.1 0.5 9.0 0.6 22.0 0.6 10.1 2.6 20.0 0.2 6.4 0.7 18.7 0.5 29.0 2.6
w/oCo-Ind 13.50.1 10.4∗
0.
∗
2
20.90.3 6.8∗
0.
∗
2
20.60.9 8.80.7 21.60.8 8.7∗
2.
∗
6
- - - -
w/oSp-Ind 14.20.1 9.7∗
0.
∗
2
19.9∗
0.
∗
2
7.0∗
0.
∗
9
21.10.7 7.3∗
0.
∗
6
20.8∗
0.
∗
8
8.7∗
2.
∗
2
- - - -
NoPrompts 14.40.2 9.1∗
0.
∗
3
19.6∗
0.
∗
2
5.8∗
0.
∗
4
21.40.9 7.3∗
0.
∗
5
20.8∗
0.
∗
7
8.0∗
2.
∗
2
21.10.1 5.9∗
0.
∗
5
18.10.3 28.12.4
Table2: Resultsofcontinuousprompts. Subscriptsdenotestandarddeviationsofeightdifferentresults. Thebest
resultsundereitherthefull-dataorfew-shotsettingareinbold. ∗/∗∗ denotessignificantgapstothebestresults
(p-value<0.05/0.01respectively). Thesemarkshavethesamemeaninghereinafter.
turbationsondiscretepromptscouldleadtosignif- Prompts). Amongdifferentinitializationmethods,
icantperformancefluctuation(SchickandSchütze, the Semantic initialization method performs con-
2021). To address these concerns, in this section sistently best and thus proves its soundness. In
we take GPT2-medium as the backbone model, contrast, random initialization (Random) shows
andindetailevaluateandanalyzeourmethodwith dramatically poor performance, even worse than
different options (e.g., prompts’ initialization or notaddingGS(w/oGS),onallthreetasksunder
perturbation). thefew-shotsetting.
However,insertingcontinuouspromptsornotor
5.1 ContinuousPrompts
initializingthemwithdifferentmethodshaveonly
Initialization Methods Except random initial- minorgapsonWoWandPCunderthefull-datasetization4,wecomparedthreecommonlyusedandin- ting. Notably,semantic-initializedstrategytokens
tuitivewaysofinitializingthecontinuousprompts alwaysbringmuchhighermatchratiosunderboth
(Gu et al., 2021): (1) using the pre-trained em- few-shot(comparedtoRandom,29.0vs. 12.5)and
bedding of a random vocabulary token (Vocab), full-data(57.4vs. 40.6)settings,highlightingthe
(2) using the pre-trained embedding of a random necessityofleveragingthestrategies’priorsemantop-100frequenttokeninthetrainingcorpus(Fre- ticmeaningstoachievebettercontrollability.
quent), and (3) using the average embeddings of Ablation Study Based on the Semantic initialthetextualsemanticexplanationsoftheindicators ization,weablatedeitherthespeaker(w/oSp-Ind),
(Semantic)5. Note that on ESConv, the strategy the component (w/o Co-Ind) or both types of intokens(Liuetal.,2021c)areinitializedinthesame dicativetokens(NoPrompts). FromTable2,they
wayascontinuousprompts. Weaddedacompared bothcontributetothefinalpromptingeffects,showbaselineasthecontrolgroupwheretheGSisnot ingthereasonablenessofpromptingGDGtasksby
provided(w/oGS). distinguishing the complex input constructs. We
Results Table 2 shows the results. Unsurpris- noticethatthespeakertypeoccupiesalargerconingly,onallthreetasks,wellinitializedcontinuous tribution. The reason may be that the speaker inprompts (e.g., Semantic) consistently boosts the dicativetokensoccurmoreininputsequences(up
performancecomparedtonotusingprompts(No to 5 utterances) and thus provide major prompts
abouttheconstructsofinputsequences.
4Toensureconvergence,wetrainedtheRandominitializationmethodfor20epochs(10morethandefault).
5.2 DiscretePrompts
5Forinstance,forthetokenthatindicatesthecomponents
ofknowledgeorpersona,weaveragetheembeddingsofthe

### Prompt Perturbation The basic discrete

tokenized word “knowledge” or ”persona” to initialize the
correspondingindicativetoken. promptsaresimplyobtainedbyreplacingindica-

<!-- Page 6 -->


### Wizard-of-Wikipedia PersonaChat ESConv

PPL↓ B-2 F1 WikiF1 PPL↓ B-2 F1 PSNF1 PPL↓ B-2 F1 Match

### Full-data(66K) Full-data(50K) Full-data(12K)

Continuous 9.0 15.3∗∗ 27.9 8.9∗∗ 11.3 12.0 26.7 11.6 14.5 7.9∗∗ 22.9 57.4∗∗
Discrete 9.0 15.9 28.1 9.4 11.2 12.2 26.9 11.4 14.4 8.2 23.4 59.9

### Few-shot(50)

Continuous 13.30.1 11.1∗ 0. ∗ 4 21.3∗ 0. ∗ 3 8.3∗ 0. ∗ 4 20.10.5 9.0 0.6 22.0∗ 0. ∗ 6 10.1∗ 2. ∗ 6 20.00.2 6.4∗ 0. ∗ 7 18.7∗ 0. ∗ 5 29.0∗ 2. ∗ 6
Discrete 12.1 0.1 11.90.5 22.20.4 8.9∗ 0. ∗ 5 17.90.3 8.90.7 22.50.4 10.31.6 18.3 0.1 7.00.3 20.0 0.4 42.2∗ 3. ∗ 6
w/oInstruction 12.10.1 12.00.3 22.20.3 9.20.6 17.90.2 8.90.5 22.60.5 10.42.1 18.40.1 7.0 0.4 19.70.3 43.1∗ 4. ∗ 3
w/Instruct-Pert 12.20.1 12.1 0.4 22.4 0.4 9.3 0.7 18.00.3 8.6∗ 0. ∗ 5 22.50.4 10.61.9 18.30.1 6.90.4 19.90.3 44.5 4.3
w/Speaker-Pert 12.20.1 12.10.3 22.30.3 9.10.5 17.9 0.3 9.00.4 22.8 0.4 10.7 1.9 18.40.1 6.70.5 19.80.3 44.53.5
Table3: Resultsofdiscreteprompts.
torswithtextualexplanationsandprependinginput promptingmethodworkswithdifferentpre-trained
sequences with task instructions (Figure 3). We models,andanalyzethefactorsthatinfluencethe
alsoattemptedthreeperturbationsonthediscrete effectivenessofprompting.
prompts,asshowninFigure5: (1)removingtask
instructions (w/o Instruction), (2) perturbing in- 6.1 ComparedModels
structions by word substitution, including “The

### We compared several representative pre-trained

following”with“Below”,“conversation”with“dimodelstobeusedasthebackbonemodels,which
alog”,“grounded”with“based”,etc. (w/Instructare also popularly adopted in previous works of

### Pert), and (3) further substituting speaker words

dialog generation (Mi et al., 2021; Shuster et al.,
“user”/“system”with“human”/“AI”basedon(2)
2021). Note that our choice of model sizes was
(w/Speaker-Pert).
mainlylimitedbycomputationalresources(Tesla
Results Table 3 shows the results. Profited by

### V10032G),andweusedthelargestavailableand

thepriorinformationintroducedinthetextualdefeasiblemodelswithintherangethatresourcesalscriptions, discrete prompts significantly outperlow.
form continuous prompts in most cases (except
Language Models GPT2-Medium (345M pathe B-2 metric on PC), and even maintain the rerameters) (Radford et al., 2019) is an autoregresmarkablesuperiorityunderthefull-datasetting(on
sive language model, pre-trained with the lan-

### WoWandESConv). Meanwhile,despitetheneed

guage modeling objective. We also included
ofmanualcrafting,thediscretepromptsgenerally
threeencoder-decoderlanguagemodels,T5-Base
donothaveobviousperformancefluctuationdue
(220M), T5-Large (770M6) (Raffel et al., 2020)
tominormodifications. Suchrobustnesstoprompt
andBART-Large(400M)(Lewisetal.,2020). T5
perturbationcomesfromnotonlytheall-parameter
andBARTbothadoptthedenoisingobjectivesbut
training (§4.2) (Logan IV et al., 2021) but also
aredifferentintermsofthenoisingfunctions,the
thehugeoutputspaceofGDGtasks(comparedto
input/outputformatsandthetrainingcorpora.

### NLU tasks). It indicates the practicability of dis-

Conversational Models We meanwhile incretepromptsandthatitmaybenotnecessaryto
cludedDialoGPT-Medium(345M)(Zhangetal.,
optimizethemlaboriously.
2020) and Blender-Small (90M) (Roller et al.,
2021). Theyarebothpre-trainedonmassiveReddit
6 PromptingDifferentPre-trained
corporawhileBlenderisfurtherfine-tunedonsev-

### Models

eral crowd-sourced datasets7 (Dinan et al., 2018;
While both continuous and discrete prompts per- Zhang et al., 2018; Rashkin et al., 2019; Smith
formwellwithGPT2,wefurtherwonderwhether
they still work with other backbone models. As 6WhilethefurtherenlargedGPT2(Large,762M)hasa
similar parameter number to T5-Large, the architecture of
showninpreviousworks(Liuetal.,2021d;Liand

### GPT2leadstomuchmoreGPUmemoryoccupation,over-

Liang, 2021), effective prompting methods vary loadingourcomputationalresources.ThusthelargestGPT2
fromtheadoptedpre-trainedmodels,dependingon wecouldexperimentwithisGPT2-Medium.
7Sincewefoundthatthefine-tuningofBlenderdoesnot
thepre-trainingsettings,modelarchitectures,etc.
utilize the grounding sources (Roller et al., 2021), we still
Inthissection,wethoroughlyinvestigatehowour experimentedwithBlenderforcomparison.

<!-- Page 7 -->


### Wizard-of-Wikipedia PersonaChat ESConv

PPL↓ B-2 F1 WikiF1 PPL↓ B-2 F1 PSNF1 PPL↓ B-2 F1 Match

### GPT2-Medium(345M)

NoPrompts 14.40.2 9.1∗
0.
∗
3
19.6∗
0.
∗
2
5.8∗
0.
∗
4
21.40.9 7.3∗
0.
∗
5
20.8∗
0.
∗
7
8.0∗
2.
∗
2
21.10.1 5.9∗
0.
∗
5
18.1∗
0.
∗
3
28.1∗
2.
∗
4
Continuous 13.30.1 11.1∗ 0. ∗ 4 21.3∗ 0.3 8.3∗ 0. ∗ 4 20.10.5 9.0 0.6 22.00.6 10.12.6 20.00.2 6.4∗ 0. ∗ 7 18.7∗ 0. ∗ 5 29.0∗ 2. ∗ 6
Discrete 12.1 0.1 11.9 0.5 22.2 0.4 8.9 0.5 17.9 0.3 8.90.7 22.5 0.4 10.3 1.6 18.3 0.1 7.0 0.3 20.0 0.4 42.2 3.6

### T5-Base(220M)

NoPrompts 13.7 0.1 9.2∗ 0. ∗ 3 20.30.3 10.8 0.7 13.4 0.1 8.6 0.6 22.5 0.1 16.0 0.8 22.3 0.1 4.7∗ 0. ∗ 5 16.1∗ 0. ∗ 4 13.8∗ 0. ∗ 8
Continuous 13.80.1 9.0∗
0.
∗
3
20.30.2 10.40.3 13.60.1 8.4∗
0.7
22.40.3 15.5∗
0.8
22.50.2 4.5∗
0.
∗
4
15.8∗
0.
∗
3
13.4∗
0.
∗
4
Discrete 14.60.3 10.0 0.3 20.7 0.4 8.2∗ 0. ∗ 7 14.40.3 5.6∗ 0. ∗ 6 18.8∗ 0. ∗ 9 11.1∗ 1. ∗ 5 23.70.2 6.2 0.2 17.6 0.2 25.0 0.9

### T5-Large(770M)

NoPrompts 11.10.1 10.5∗
0.
∗
1
22.2∗
0.
∗
2
12.3∗
0.
∗
5
10.50.2 8.1∗
0.
∗
7
23.6∗
0.
∗
3
15.9∗
1.
∗
2
17.80.1 5.1∗
0.
∗
5
17.2∗
0.
∗
4
16.8∗
0.
∗
5
Continuous 10.70.1 10.9 0.2 22.6∗ 0. ∗ 2 11.5∗ 0. ∗ 8 10.40.1 10.10.8 23.80.3 18.81.8 17.40.1 5.4∗ 0. ∗ 5 17.4∗ 0. ∗ 3 16.4∗ 0. ∗ 8
Discrete 10.5 0.1 10.90.3 23.8 0.2 13.6 0.9 10.1 0.1 10.4 1.1 24.6 0.2 18.9 2.5 16.9 0.1 6.4 0.6 19.4 0.4 38.9 2.0

### BART-Large(400M)

NoPrompts 16.1 0.4 9.0∗ 0.4 20.50.6 11.8 1.2 26.51.4 8.4 1.5 21.10.8 14.4∗ 2. ∗ 7 23.30.5 6.3 0.7 17.40.5 19.40.9
Continuous 16.40.3 8.90.8 19.9∗ 0.7 8.9∗ 1. ∗ 4 25.6 1.1 7.9∗ 1. ∗ 0 21.2 0.8 13.1∗ 1. ∗ 9 22.9 0.6 6.20.9 17.80.7 21.6 2.0
Discrete 16.30.6 9.6 0.6 20.6 0.7 10.4∗ 2. ∗ 2 25.80.7 8.11.5 20.61.2 15.7 3.8 25.00.4 6.00.6 18.0 0.8 15.9∗ 1. ∗ 8

### DialoGPT-Medium(345M)

NoPrompts 56.8 1.1 6.7 0.4 18.70.8 4.9∗ 0. ∗ 6 17.7 0.2 9.6 0.5 23.2 0.3 10.9∗ 1. ∗ 2 35.21.0 5.3∗ 0. ∗ 4 18.6∗ 0.4 30.6 1.2
Continuous 60.12.4 6.50.6 18.60.8 5.10.8 19.20.4 9.40.5 22.60.4 10.7∗ 1. ∗ 4 34.7 1.4 5.4∗ 0. ∗ 3 18.6∗ 0.3 27.1∗ 3. ∗ 1
Discrete 95.52.7 6.40.4 16.8∗ 0. ∗ 5 5.3 0.8 24.10.8 9.30.7 23.10.5 11.8 2.0 42.81.4 5.8 1.0 19.1 0.4 26.7∗ 3. ∗ 9

### Blender-Small(90M)

NoPrompts 14.8 0.2 9.8 0.3 21.6 0.4 8.61.3 15.00.2 8.5∗ 1. ∗ 0 22.90.6 9.5∗ 1. ∗ 3 21.00.2 6.10.7 19.50.6 34.9 2.8
Continuous 14.90.1 9.60.4 21.30.5 8.2∗ 0.8 14.9 0.2 8.5∗ 0. ∗ 8 23.0 0.2 9.70.8 21.10.2 6.1 0.6 19.6 0.4 34.73.1
Discrete 15.40.3 9.0∗ 0. ∗ 9 20.8∗ 0.9 8.7 0.7 14.90.3 9.4 0.7 22.90.6 10.0 1.5 20.1 0.1 5.7∗ 0. ∗ 5 18.6∗ 0. ∗ 6 15.7∗ 1. ∗ 9
Table 4: Results of using different pre-trained models. The best results among all the models are highlighted.
Perplexity(PPL)isnotcomparablebetweenmodelsduetothedifferencesinvocabularyandtokenization.
etal.,2020). Notethatwedidnotincludelarger- important. Itsuggeststhatonlypre-trainingonmassizedBlendermodelsbecausetheyonlyacceptthe sive general dialog corpora makes it difficult for
encoderinputofmaxlength128. conversationalmodelstomakeuseofnon-dialog
Wecomparedthreemethodswithdifferentpre- externalinformation. Incontrast,althoughnotspetrainedmodels: notusingprompts(NoPrompts), ciallypre-trainedondialogcorpora,languagemodcontinuous prompts and discrete prompts. The els(e.g.,GPT2andT5)canstillbequicklyadapted
inputformatsofDialoGPTarethesameasGPT2, to dialog generation tasks, and at the same time
andthoseofT5andBART/Blenderareshownin acquiretheabilitytoutilizeexternalinformation,
Figure6and7respectively. Resultsareshownin thatis,thecapabilityofgrounding.
Table4.

### Whilecriticaltolanguagemodels(exceptBART,

aswillbediscussedlater),promptingdoesnotwork
6.2 LanguageModelsvs. Conversational
with conversational models. A direct evidence is

### Models

thePPLsofDialoGPT(Discrete>Continuous≈
Promptedlanguagemodelsperformsuperiorlyto No Prompts, on all three tasks). Intuitively, disconversationalmodelsonallthreetasks,whileun- crete prompts are naturally not tailored for conprompted ones generally perform worse than the versationalmodelsduetotheenormousgapswith
latter. On WoW and ESConv, prompted GPT2 theinputformatsofpre-training(i.e.,concatenatachieves higher B-2, F1 and Match Ratio scores ing utterances of the conversation context as the
thanbothDialoGPTandBlender,butunprompted encoder input). Hence, discrete prompts would
GPT2, T5 and BART all underperform Blender. instead hurt conversational models’ performance
On PC, prompting also enables T5-Large to out- andareusuallyinferiortocontinuouspromptsor
performDialoGPTintermsofallthemetrics. We not using prompts on all three tasks. As for conthinkthatsuchobservationisnottrivialandrather tinuousprompts,theyseemtodifferlittlefromthe

<!-- Page 8 -->

performanceofnotaddingprompts. Weconjecture Wizard-of-Wikipedia PersonaChat
thatthereasonisthatconversationalmodelshave B-2 WikiF1 B-2 PSNF1
beenabletodistinguishtheinputconstructsduring

### GPT2-Medium(345M)

pre-trainingondialogcorpora,wheretheconversa-

### NoPrompts 9.1(+0.0) 9.0(+3.3) 7.5(+0.2) 12.6(+4.6)

tioncontextcouldcontainutterancesfrommultiple Continuous 10.7(-0.4) 11.1(+2.8) 9.2(+0.2) 15.5(+5.5)
speakers. Discrete 9.4(-2.6) 6.8(-2.1) 7.8(-0.8) 10.6(+0.3)

### T5-Base(220M)

6.3 FurtherAnalysis NoPrompts 8.6(-0.6) 9.3(-1.4) 8.2(-0.5) 15.3(-0.6)

### Continuous 7.7(-1.3) 10.2(-0.2) 8.4(+0.0) 14.9(-0.5)

EffectsofModelPre-training Amongthethree Discrete 8.2(-1.8) 6.6(-1.7) 5.2(-0.5) 10.2(-0.9)
languagemodels,GPT2andT5-Largebothbenefit

### T5-Large(770M)

fromcontinuousanddiscreteprompts,whileBART
NoPrompts 9.8(-0.7) 11.5(-0.8) 7.3(-0.7) 14.8(-1.1)
generally does not (only small improvements on

### Continuous 10.0(-0.9) 11.5(-0.0) 9.2(-0.9) 17.2(-1.6)

WoW).Itprobablyresultsfromthedifferencesin Discrete 9.6(-1.2) 11.4(-2.2) 9.2(-1.2) 18.0(-0.9)
their pre-training objectives and corpora. Specif- BART-Large(400M)
ically, GPT2 and T5 adopt the more general pre-

### NoPrompts 8.9(-0.1) 10.0(-1.9) 8.2(-0.2) 13.6(-0.8)

training objectives (language modeling and span Continuous 9.0(+0.1) 9.2(+0.2) 7.4(-0.6) 12.9(-0.2)
corruption,respectively)thanBART(denoisingin
Discrete 9.3(-0.2) 11.0(+0.6) 7.9(-0.2) 15.4(-0.3)
anautoencodingway),andT5isevenpre-trained
Table5: Resultsofpost-positioningtheGSrightafter
on much larger pre-training corpora (745GB vs.
the conversation context. Performance changes are in
BART’s160GB).Asaresult,GPT2andT5canbe parentheses. The largest and smallest changes (absomoreeasilystimulatedbywellinitializedcontinu- lutevalues)amongallthemodelsarehighlightedand
ouspromptsandnaturallanguagediscreteprompts. shadowedrespectively.

### Effects of Model Sizes Comparing T5 of two

sizes,wenoticethatunlikeT5-Large,T5-Baseusu- turb the pre-trained models, especially under the
ally is not profited by continuous prompts on all few-shotsetting. Alternatively,wemovedtheGS
threetasks,anditsperformanceisevendamaged rightaftertheconversationcontext(thecorrespondby discrete prompts on PC. It suggests that the ingdiscretepromptsareshowninFigure8),aimlargermodelsizeisbeneficialtoeffectiveprompt- ingtoobservewhethergeneratedresponsesrefer
ing, which is also our motivation to experiment moretotheGS.ResultsareshowninTable5. For
withaslargeaspossiblepre-trainedmodels. theNoPromptsandContinuousmethods,post-GS
Effects of Model Architectures Continuous makesGPT2achievelargelyincreasedWiki/PSN
and discrete prompts benefit both GPT2 and T5- F1, while T5 and BART are not influenced obvi-
Large. It indicates that our prompting method is ously. Itimpliestheeffectsofmodelarchitectures
effectivewithlanguagemodelsofdifferentarchi- andindirectlyprovesthereasonablenessofourhytectures. pothesis. Meanwhile,wenotethattheperformance
of discrete prompts drops remarkably with both
Interestingly,wenotethatencoder-decodermod-
GPT2andT5,indicatingthatpost-positioningthe
elsaremorepronetocopyGSthanautoregressive

### GS is not a suitable prompt design for these two

languagemodels,thatis,T5andBARTachievenolanguagemodels.
tablyhigherWiki/PSNF1thanGPT2onWoWand
PC.Wehypothesizethatthisphenomenonresults
7 Conclusion
fromthedifferentmodelarchitectures. Specifically,
giventhattheGSispositionedbeforetheconversa- This work explores the prompt-based few-shot
tioncontext,thebidirectionalencodingofT5and learning for grounded dialog generation (GDG).
BART enables the unified attention to the model We show that distinguishing the constructs of
input. In contrast, the unidirectional attention of modelinputiseffectivetoboostthefew-shotlearn-
GPT2 may focus more on the contents nearby to ingperformance,inwhichwellinitializedcontinthetargetresponses(i.e.,theconversationcontext uouspromptsoreasilydesigneddiscreteprompts
ratherthantheGS). playthekeyrole. Weadditionallydemonstratethat
To verify our hypothesis, comparing the same ourpromptingmethodperformswellwithlanguage
modelbymodifyingtheattentiondirectionsseems modelsofdifferentarchitectures(e.g.,GPT2and
directbutinsteadinfeasible,becauseitwouldper- T5) but does not work with conversational mod-

<!-- Page 9 -->

els (e.g., DialoGPT and Blender), among which Venkatesh, Raefer Gabriel, and Dilek Hakkanipromptedlanguagemodelscanevenachievesupe- Tür. 2019. Topical-Chat: Towards Knowledge-
GroundedOpen-DomainConversations. InProc.Inriorperformancetoconversationalmodels. Further
terspeech2019,pages1891–1895.
analysisshowsthattheeffectivenessofourprompting method also relies on backbone models with Yuxian Gu, Xu Han, Zhiyuan Liu, and Minlie Huang.
enough prowess. Our work reveals the potential 2021. Ppt: Pre-trained prompt tuning for few-shot
learning. arXivpreprintarXiv:2109.04332.
ofpromptingmethodsinthefew-shotlearningfor
GDG,andraisesattentiontotheproperselection AriHoltzman, JanBuys, LiDu, MaxwellForbes, and
ofpre-trainedmodelsinGDGtasks. YejinChoi.2019. Thecuriouscaseofneuraltextdegeneration. In International Conference on Learn-
Acknowledgements ingRepresentations.
ThisworkwassupportedbytheNationalScience Minlie Huang, Xiaoyan Zhu, and Jianfeng Gao. 2020.
Challenges in building intelligent open-domain dia-
FoundationforDistinguishedYoungScholars(with
logsystems. ACMTransactionsonInformationSys-
No. 62125604)andtheNSFCprojects(Keyproject
tems(TOIS),38(3):1–32.
with No. 61936010 and regular project with No.
61876096). Thisworkwasalsosupportedbythe Mike Lewis, Yinhan Liu, Naman Goyal, Marjan Ghazvininejad, Abdelrahman Mohamed, Omer
Guoqiang Institute of Tsinghua University, with
Levy, Veselin Stoyanov, and Luke Zettlemoyer.
GrantNo. 2019GQG1and2020GQG0005. 2020. BART:Denoisingsequence-to-sequencepretrainingfornaturallanguagegeneration,translation,
andcomprehension. InProceedingsofthe58thAn-
References nual Meeting of the Association for Computational
Linguistics, pages 7871–7880, Online. Association
Taylor Berg-Kirkpatrick, David Burkett, and Dan
forComputationalLinguistics.
Klein. 2012. An empirical investigation of statistical significance in NLP. In Proceedings of the Linxiao Li, Can Xu, Wei Wu, Yufan Zhao, Xueliang
2012JointConferenceonEmpiricalMethodsinNat- Zhao, and Chongyang Tao. 2020. Zero-resource
ural Language Processing and Computational Nat- knowledge-grounded dialogue generation. In Adural Language Learning, pages 995–1005, Jeju Is- vances in Neural Information Processing Systems
land,Korea.AssociationforComputationalLinguis- 33: AnnualConferenceonNeuralInformationProtics. cessing Systems 2020, NeurIPS 2020, December 6-
12,2020,virtual.

### TomBBrown, BenjaminMann, NickRyder, Melanie


### Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind

Xiang Lisa Li and Percy Liang. 2021. Prefix-tuning:

### Neelakantan,PranavShyam,GirishSastry,Amanda


### Optimizing continuous prompts for generation. In

Askell, et al. 2020. Language models are few-shot
Proceedings of the 59th Annual Meeting of the
learners. arXivpreprintarXiv:2005.14165.
Association for Computational Linguistics and the
11thInternationalJointConferenceonNaturalLan-

### Jacob Devlin, Ming-Wei Chang, Kenton Lee, and

guage Processing (Volume 1: Long Papers), pages

### Kristina Toutanova. 2019. BERT: Pre-training of

4582–4597, Online. Association for Computational
deep bidirectional transformers for language under-
Linguistics.
standing. In Proceedings of the 2019 Conference
of the North American Chapter of the Association
PengfeiLiu,WeizheYuan,JinlanFu,ZhengbaoJiang,
for Computational Linguistics: Human Language
Hiroaki Hayashi, and Graham Neubig. 2021a. Pre-

### Technologies, Volume 1 (Long and Short Papers),

train, prompt, and predict: A systematic survey of
pages4171–4186,Minneapolis,Minnesota.Associprompting methods in natural language processing.
ationforComputationalLinguistics.
arXivpreprintarXiv:2107.13586.
Emily Dinan, Stephen Roller, Kurt Shuster, Angela
Shilei Liu, Xiaofeng Zhao, Bochao Li, Feiliang
Fan,MichaelAuli,andJasonWeston.2018. Wizard
Ren, Longhui Zhang, and Shujuan Yin. 2021b.
of wikipedia: Knowledge-powered conversational
A Three-Stage Learning Framework for Lowagents. In International Conference on Learning
Resource Knowledge-Grounded Dialogue Genera-
Representations.
tion. In Proceedings of the 2021 Conference on
Marjan Ghazvininejad, Chris Brockett, Ming-Wei EmpiricalMethodsinNaturalLanguageProcessing,
Chang,BillDolan,JianfengGao,Wen-tauYih,and pages2262–2272, OnlineandPuntaCana, Domini-
Michel Galley. 2018. A knowledge-grounded neu- can Republic. Association for Computational Linralconversationmodel. InProceedingsoftheAAAI guistics.
ConferenceonArtificialIntelligence,volume32.

### Siyang Liu, Chujie Zheng, Orianna Demasi, Sahand

Karthik Gopalakrishnan, Behnam Hedayatnia, Qin- Sabour, Yu Li, Zhou Yu, Yong Jiang, and Minlie
lang Chen, Anna Gottardi, Sanjeev Kwatra, Anu Huang. 2021c. Towards emotional support dialog

<!-- Page 10 -->

systems. In Proceedings of the 59th Annual Meet- In Proceedings of the 2021 Conference on EmpiriingoftheAssociationforComputationalLinguistics calMethodsinNaturalLanguageProcessing,pages
andthe11thInternationalJointConferenceonNat- 390–402, Online and Punta Cana, Dominican ReuralLanguageProcessing(Volume1:LongPapers), public.AssociationforComputationalLinguistics.
pages3469–3483,Online.AssociationforComputationalLinguistics. KurtShuster,SpencerPoff,MoyaChen,DouweKiela,
and Jason Weston. 2021. Retrieval augmentation
Xiao Liu, Yanan Zheng, Zhengxiao Du, Ming Ding, reduces hallucination in conversation. In Findings
Yujie Qian, Zhilin Yang, and Jie Tang. 2021d. Gpt of the Association for Computational Linguistics:
understands,too. arXivpreprintarXiv:2103.10385. EMNLP 2021, pages 3784–3803, Punta Cana, Dominican Republic. Association for Computational
Robert L Logan IV, Ivana Balaževic´, Eric Wallace, Linguistics.
Fabio Petroni, Sameer Singh, and Sebastian Riedel.
Eric Michael Smith, Mary Williamson, Kurt Shuster,

## Cutting down on prompts and parameters:

Jason Weston, and Y-Lan Boureau. 2020. Can you
Simple few-shot learning with language models.
putitalltogether: Evaluatingconversationalagents’
arXivpreprintarXiv:2106.13353.
abilitytoblendskills. InProceedingsofthe58thAn-
Ilya Loshchilov and Frank Hutter. 2018. Decoupled nual Meeting of the Association for Computational
weight decay regularization. In International Con- Linguistics, pages 2021–2030, Online. Association
ferenceonLearningRepresentations. forComputationalLinguistics.
Thomas Wolf, Victor Sanh, Julien Chaumond, and
FeiMi,YitongLi,YashengWang,XinJiang,andQun

### Clement Delangue. 2019. Transfertransfo: A

Liu.2021. Cins:Comprehensiveinstructionforfewtransfer learning approach for neural network
shotlearningintask-orienteddialogsystems. arXiv
based conversational agents. arXiv preprint
preprintarXiv:2109.04645.
arXiv:1901.08149.

### KishorePapineni,SalimRoukos,ToddWard,andWei-

Saizheng Zhang, Emily Dinan, Jack Urbanek, Arthur

### JingZhu.2002. Bleu: amethodforautomaticeval-

Szlam,DouweKiela,andJasonWeston.2018. Peruation of machine translation. In Proceedings of
sonalizing dialogue agents: I have a dog, do you
the40thAnnualMeetingoftheAssociationforComhave pets too? In Proceedings of the 56th AnputationalLinguistics,pages311–318,Philadelphia,
nual Meeting of the Association for Computational

### Pennsylvania,USA.AssociationforComputational

Linguistics (Volume 1: Long Papers), pages 2204–
Linguistics.
2213, Melbourne, Australia. Association for ComputationalLinguistics.
Alec Radford, Jeffrey Wu, Rewon Child, David Luan,

### DarioAmodei,andIlyaSutskever.2019. Language


### YizheZhang,SiqiSun,MichelGalley,Yen-ChunChen,

modelsareunsupervisedmultitasklearners. OpenAI
Chris Brockett, Xiang Gao, Jianfeng Gao, Jingjing
blog,1(8):9.
Liu, and Bill Dolan. 2020. DIALOGPT : Largescale generative pre-training for conversational re-

### ColinRaffel,NoamShazeer,AdamRoberts,Katherine

sponse generation. In Proceedings of the 58th An-

### Lee, Sharan Narang, Michael Matena, Yanqi Zhou,

nual Meeting of the Association for Computational
Wei Li, and Peter J Liu. 2020. Exploring the lim-

### Linguistics: System Demonstrations, pages 270–

its of transfer learning with a unified text-to-text
278,Online.AssociationforComputationalLinguistransformer. JournalofMachineLearningResearch,
tics.
21(140):1–67.
Xueliang Zhao, Wei Wu, Chongyang Tao, Can Xu,
HannahRashkin,EricMichaelSmith,MargaretLi,and

### Dongyan Zhao, and Rui Yan. 2020. Low-resource

Y-Lan Boureau. 2019. Towards empathetic openknowledge-grounded dialogue generation. In Interdomainconversationmodels:Anewbenchmarkand
nationalConferenceonLearningRepresentations.
dataset. In Proceedings of the 57th Annual Meeting of the Association for Computational Linguis- Chujie Zheng, Yunbo Cao, Daxin Jiang, and Minlie
tics, pages 5370–5381, Florence, Italy. Association Huang. 2020. Difference-aware knowledge selecforComputationalLinguistics. tion for knowledge-grounded conversation generation. In Findings of the Association for Computa-
Stephen Roller, Emily Dinan, Naman Goyal, Da Ju, tional Linguistics: EMNLP 2020, pages 115–125,
Mary Williamson, Yinhan Liu, Jing Xu, Myle Ott, Online.AssociationforComputationalLinguistics.
EricMichaelSmith,Y-LanBoureau,andJasonWeston. 2021. Recipes for building an open-domain HaoZhou,TomYoung,MinlieHuang,HaizhouZhao,
chatbot. In Proceedings of the 16th Conference of Jingfang Xu, and Xiaoyan Zhu. 2018a. ComtheEuropeanChapteroftheAssociationforCompu- monsenseknowledgeawareconversationgeneration
tational Linguistics: Main Volume, pages 300–325, withgraphattention. InProceedingsoftheTwenty-
Online.AssociationforComputationalLinguistics. SeventhInternationalJointConferenceonArtificial

### Intelligence, IJCAI-18, pages 4623–4629. Interna-

Timo Schick and Hinrich Schütze. 2021. Few-shot tional Joint Conferences on Artificial Intelligence
text generation with natural language instructions. Organization.

<!-- Page 11 -->

NoPrompts A UsedPre-trainedModels
{persona}<eos>
{utterance1}<eos>{utterance2}<eos> This work experiments with the following open-
{utterance3}<eos>{utterance4}<eos> sourcedpre-trainedmodels: BERT-Large8,GPT2-

### ContinuousPrompts

Medium9,T5-Base10,T5-Large11,BART-Large12,
<persona>{persona}<context>
<user>{utterance1}<eos><system>{utterance2}<eos> DialoGPT-Medium13 andBlender-Small14.
<user>{utterance3}<eos><system>{utterance4}<eos>

### DiscretePrompts

The following is a conversation between a user and an
engagingsystem.The system’s utterances are grounded
on the personaprofile:\n
{persona}\n

### Conversationcontext:\n

User:{utterance1}\nSystem:{utterance2}\n

### User:{utterance3}\nSystem:{utterance4}\n

Figure 4: Applying our prompting method to PersonaChat.
RemovingTaskInstructions
Backgroundknowledge:\n
{knowledge}\n

### Conversationcontext:\n

User:{utterance1}\nSystem:{utterance2}\n
User:{utterance3}\nSystem:{utterance4}\n

### InstructionPerturbation

Below is a dialog between a user and a knowledgeable
system.The system’s utterances are based on the
knowledge document:\n
{knowledge}\n

### Dialogcontext:\n

User:{utterance1}\nSystem:{utterance2}\n
User:{utterance3}\nSystem:{utterance4}\n

### SpeakerPerturbation


### Below is a dialog between a human and a

knowledgeable AI.The AI’s utterances are based on the
knowledge document:\n
{knowledge}\n

### Dialogcontext:\n

Human:{utterance1}\nAI:{utterance2}\n
Human:{utterance3}\nAI:{utterance4}\n
Figure5: Perturbeddiscreteprompts.
HaoZhou,ChujieZheng,KailiHuang,MinlieHuang,
and Xiaoyan Zhu. 2020. KdConv: A Chinese
multi-domain dialogue dataset towards multi-turn
knowledge-driven conversation. In Proceedings of
the58thAnnualMeetingoftheAssociationforComputational Linguistics, pages 7098–7108, Online.
AssociationforComputationalLinguistics.
8https://huggingface.co/
bert-large-uncased
Kangyan Zhou, Shrimai Prabhumoye, and Alan W 9https://huggingface.co/gpt2-medium
Black. 2018b. A dataset for document grounded 10https://huggingface.co/t5-base
conversations. In Proceedings of the 2018 Confer- 11https://huggingface.co/t5-large
ence on Empirical Methods in Natural Language 12https://huggingface.co/facebook/
Processing, pages 708–713, Brussels, Belgium. As- bart-large
sociationforComputationalLinguistics. 13https://huggingface.co/microsoft/

### DialoGPT-medium

14https://huggingface.co/facebook/
blenderbot_small-90M

<!-- Page 12 -->


## T5


### NoPrompts NoPrompts

Encoder:{knowledge}<eos>{utterance1}<eos> Encoder:{utterance1}<eos><Reflection of Feelings>
{utterance2}<eos>{utterance3}<eos><X> {utterance2}<eos>{utterance3}<eos><Self-disclosure><X>
Decoder:<bos><X>{utterance4}<eos> Decoder:<bos><X>{utterance4}<eos>

### ContinuousPrompts ContinuousPrompts

Encoder:<knowledge>{knowledge}<context><user> Encoder:<user>{utterance1}<eos><system><Reflection of
{utterance1}<eos><system>{utterance2}<eos> Feelings>{utterance2}<eos><user>{utterance3}<eos>
<user>{utterance3}<eos><system><X> <system><Self-disclosure><X>
Decoder:<bos><X>{utterance4}<eos> Decoder:<bos><X>{utterance4}<eos>

### DiscretePrompts DiscretePrompts

Encoder:The following is a conversation between a user Encoder:The following is a conversation between a user and
and aknowledgeable system.The system’s utterances an empathetic system.The system can use various support
are grounded on the background knowledge:\n skills to provide emotional support to the user.\n
{knowledge}\nConversationcontext:\nUser: User:{utterance1}\nSystemreflects and describes user’s

### Bart/blender

{utterance1}\nSystem:{utterance2}\nUser:{utterance3} feelings:{utterance2}\nUser:{utterance3}\nSystemshares
\nSystem:<X> similar experiences or emotions:<X>
Decoder:<bos><X>{utterance4}<eos> Decoder:<bos><X>{utterance4}<eos>
Figure6: InputformatsforT5.

### NoPrompts NoPrompts

Encoder:{knowledge}<eos>{utterance1}<eos> Encoder:{utterance1}<eos><Reflection of Feelings>
{utterance2}<eos>{utterance3} {utterance2}<eos>{utterance3}
Decoder:<bos>{utterance4}<eos> Decoder:<bos><Self-disclosure>{utterance4}<eos>

### ContinuousPrompts ContinuousPrompts

Encoder:<knowledge>{knowledge}<context><user> Encoder:<user>{utterance1}<eos><system><Reflection of
{utterance1}<eos><system>{utterance2}<eos> Feelings>{utterance2}<eos><user>{utterance3}
<user>{utterance3} Decoder:<bos><Self-disclosure>{utterance4}<eos>
Decoder:<bos>{utterance4}<eos>

### DiscretePrompts

DiscretePrompts Encoder:The following is a conversation between a user and
Encoder:The following is a conversation between a user an empathetic system.The system can use various support
and aknowledgeable system.The system’s utterances skills to provide emotional support to the user.\n
are grounded on the background knowledge:\n User:{utterance1}\nSystemreflects and describes user’s
{knowledge}\nConversationcontext:\nUser: feelings:{utterance2}\nUser:{utterance3}\nSystemshares
{utterance1}\nSystem:{utterance2}\nUser:{utterance3} similar experiences or emotions:
\nSystem: Decoder:<bos>{utterance4}<eos>

### Decoder:<bos>{utterance4}<eos>

Figure7: InputformatsforBARTandBlender.

### KnowledgePostposition

The following is a conversation between a user and a
knowledgeable system.\n

### Conversationcontext:\n

User:{utterance1}\nSystem:{utterance2}\n
User:{utterance3}\n
\n
The system’s utterances are grounded on the
background knowledge:\n
{knowledge}\n
What is the system’s next response?\n
System:{utterance4}\n

### PersonaPostposition

The following is a conversation between a user and an
engaging system.\n

### Conversationcontext:\n

User:{utterance1}\nSystem:{utterance2}\n
User:{utterance3}\n
\n
The system’s utterances are grounded on the persona
profile:\n
{persona}\n
What is the system’s next response?\n

### System:{utterance4}\n

Figure8: Post-positioningtheGSindiscreteprompts.

## Tables

**Table (Page 2):**

| A lifeguard is a rescuer who supervises the safety and rescue of swimmers, surfers, and other water sports participantssuch as in a Wikipedia swimming pool, water park, beach, spa, river (Lifeguard) and lake…In some areas, lifeguards are part of the emergency services system to incidents and in some communities, lifeguards may function as the primary EMS provider. | I am an artist I have fourchildren I recently got a cat Persona I enjoy walking for exercise I love watching Game of Thrones | Seeker I feel so frustrated. [Question] Supporter May I ask why you are feeling frustrated? My school was closed without any prior Seeker warning due to the pandemic. [Self-disclosure] I understand you. I would also have Supporter been really frustrated if that happened to me. Yeah! I don't even know what is going Seeker to happen with our final. [Reflection of Feelings] Supporter That is really upsetting and stressful. [Providing Suggestions] Supporter Have you thought about talking to your parents or a close friend about this? |
|---|---|---|
|  | Speaker1 Hi Speaker2 Hello ! How are you today ? I am good thank you , how Speaker1 are you. Great, thanks ! My children Speaker2 and I were just about to watch Game of Thrones. Nice ! How old are your Speaker1 children? I have fourthat range in age Speaker2 from 10 to 21. You? |  |
| So I am a lifeguard. Know anything about Apprentice saving lives in water? I’m impressed! It’s a big responsibility to Wizard supervise other people’s safety in the water! Tell me more. Well, I help make sure people do not drown or Apprentice get injured while in or near the water! I’ve heard that in some places, lifeguards also Wizard help with other sorts of emergencies, like mountain rescues! |  |  |


**Table (Page 3):**

| NoPrompts {knowledge}<eos> {utterance1}<eos>{utterance2}<eos> {utterance3}<eos>{utterance4}<eos> |
|---|
| ContinuousPrompts <knowledge>{knowledge}<context> <user>{utterance1}<eos><system>{utterance2}<eos> <user>{utterance3}<eos><system>{utterance4}<eos> |
| DiscretePrompts The following is a conversation between a user and a knowledgeable system.The system’s utterances are grounded on the background knowledge:\n {knowledge}\n Conversationcontext:\n User:{utterance1}\nSystem:{utterance2}\n User:{utterance3}\nSystem:{utterance4}\n |


**Table (Page 3):**

| NoPrompts {utterance1}<eos><Reflection of Feelings>{utterance2}<eos> {utterance3}<eos><Self-disclosure>{utterance4}<eos> |
|---|
| ContinuousPrompts <user>{utterance1}<eos> <system><Reflection of Feelings>{utterance2}<eos> <user>{utterance3}<eos> <system><Self-disclosure>{utterance4}<eos> |
| DiscretePrompts The following is a conversation between a user and an empathetic system.The system can use various support skills to provide emotional support to the user.\n User:{utterance1}\n Systemreflects and describes user’s feelings:{utterance2}\n User:{utterance3}\n Systemshares similar experiences or emotions:{utterance4}\n |


**Table (Page 5):**

| Wizard-of-Wikipedia | PersonaChat |
|---|---|
| PPL↓ B-2 F1 WikiF1 | PPL↓ B-2 F1 PSNF1 |


**Table (Page 5):**

| 17.7 8.5∗∗ 21.9∗∗ 4.0∗∗ 9.0 15.5 28.0 9.1 9.0 15.3 27.9 8.9 | 15.2 10.9∗∗ 25.3∗∗ 6.6∗∗ 11.4 12.2 26.6 11.8 11.3 12.0 26.7 11.6 |
|---|---|
| 9.1 15.1∗ 27.5 9.0 | 11.4 11.7∗∗ 26.5 11.7 |


**Table (Page 5):**

| 26.50.2 5.8∗ ∗ 17.7∗ ∗ 3.1∗ ∗ 0. 2 0. 5 0. 2 101.625.1 5.6∗ ∗ 16.9∗ ∗ 3.4∗ ∗ 1. 4 2. 6 0. 9 13.50.2 10.3∗ ∗ 20.90.2 7.0∗ ∗ 0. 4 0. 4 13.90.1 10.9∗ 21.00.2 7.80.6 0.5 13.3 11.1 21.3 8.3 0.1 0.4 0.3 0.4 | 26.30.5 7.1∗ ∗ 20.1∗ ∗ 5.0∗ ∗ 0. 7 1. 0 0. 7 51.316.4 7.3∗ ∗ 19.9∗ ∗ 6.1∗ ∗ 1. 1 2. 6 1. 6 20.60.9 8.6∗ ∗ 21.50.7 8.8∗ ∗ 0. 7 2. 6 21.20.9 8.4∗ ∗ 21.50.6 8.3∗ ∗ 0. 6 2. 2 20.1 9.0 22.0 10.1 0.5 0.6 0.6 2.6 |
|---|---|
| 13.50.1 10.4∗ ∗ 20.90.3 6.8∗ ∗ 0. 2 0. 2 14.20.1 9.7∗ ∗ 19.9∗ ∗ 7.0∗ ∗ 0. 2 0. 2 0. 9 14.40.2 9.1∗ ∗ 19.6∗ ∗ 5.8∗ ∗ 0. 3 0. 2 0. 4 | 20.60.9 8.80.7 21.60.8 8.7∗ ∗ 2. 6 21.10.7 7.3∗ ∗ 20.8∗ ∗ 8.7∗ ∗ 0. 6 0. 8 2. 2 21.40.9 7.3∗ ∗ 20.8∗ ∗ 8.0∗ ∗ 0. 5 0. 7 2. 2 |


**Table (Page 6):**

| Wizard-of-Wikipedia | PersonaChat |
|---|---|
| PPL↓ B-2 F1 WikiF1 | PPL↓ B-2 F1 PSNF1 |


**Table (Page 6):**

| 13.30.1 11.1∗ ∗ 21.3∗ ∗ 8.3∗ ∗ 0. 4 0. 3 0. 4 12.1 0.1 11.90.5 22.20.4 8.9∗ 0. ∗ 5 | 20.10.5 9.0 0.6 22.0∗ 0. ∗ 6 10.1∗ 2. ∗ 6 17.90.3 8.90.7 22.50.4 10.31.6 |
|---|---|
| 12.10.1 12.00.3 22.20.3 9.20.6 12.20.1 12.1 0.4 22.4 0.4 9.3 0.7 12.20.1 12.10.3 22.30.3 9.10.5 | 17.90.2 8.90.5 22.60.5 10.42.1 18.00.3 8.6∗ ∗ 22.50.4 10.61.9 0. 5 17.9 0.3 9.00.4 22.8 0.4 10.7 1.9 |


**Table (Page 7):**

| Wizard-of-Wikipedia | PersonaChat |
|---|---|
| PPL↓ B-2 F1 WikiF1 | PPL↓ B-2 F1 PSNF1 |


**Table (Page 8):**

| Wizard-of-Wikipedia |
|---|
| B-2 WikiF1 |


**Table (Page 11):**

| NoPrompts A UsedPre-trainedModels {persona}<eos> {utterance1}<eos>{utterance2}<eos> This work experiments with the follo {utterance3}<eos>{utterance4}<eos> sourcedpre-trainedmodels: BERT-La ContinuousPrompts Medium9,T5-Base10,T5-Large11,BA <persona>{persona}<context> <user>{utterance1}<eos><system>{utterance2}<eos> DialoGPT-Medium13 andBlender-Sm <user>{utterance3}<eos><system>{utterance4}<eos> DiscretePrompts The following is a conversation between a user and an engagingsystem.The system’s utterances are grounded on the personaprofile:\n {persona}\n Conversationcontext:\n User:{utterance1}\nSystem:{utterance2}\n User:{utterance3}\nSystem:{utterance4}\n Figure 4: Applying our prompting method to Per- sonaChat. RemovingTaskInstructions Backgroundknowledge:\n |  |
|---|---|
|  | Figure 4: Applying our prompting method to Per- sonaChat. RemovingTaskInstructions Backgroundknowledge:\n |


**Table (Page 11):**

| NoPrompts {persona}<eos> {utterance1}<eos>{utterance2}<eos> {utterance3}<eos>{utterance4}<eos> |
|---|
| ContinuousPrompts <persona>{persona}<context> <user>{utterance1}<eos><system>{utterance2}<eos> <user>{utterance3}<eos><system>{utterance4}<eos> |
| DiscretePrompts The following is a conversation between a user and an engagingsystem.The system’s utterances are grounded on the personaprofile:\n {persona}\n Conversationcontext:\n User:{utterance1}\nSystem:{utterance2}\n User:{utterance3}\nSystem:{utterance4}\n |


**Table (Page 11):**

| RemovingTaskInstructions Backgroundknowledge:\n |
|---|
| {knowledge}\n Conversationcontext:\n User:{utterance1}\nSystem:{utterance2}\n User:{utterance3}\nSystem:{utterance4}\n |
| InstructionPerturbation Below is a dialog between a user and a knowledgeable system.The system’s utterances are based on the knowledge document:\n {knowledge}\n Dialogcontext:\n User:{utterance1}\nSystem:{utterance2}\n User:{utterance3}\nSystem:{utterance4}\n |
| SpeakerPerturbation Below is a dialog between a human and a knowledgeable AI.The AI’s utterances are based on the knowledge document:\n {knowledge}\n Dialogcontext:\n Human:{utterance1}\nAI:{utterance2}\n Human:{utterance3}\nAI:{utterance4}\n |


**Table (Page 12):**

|  | T5 NoPrompts NoPrompts Encoder:{knowledge}<eos>{utterance1}<eos> Encoder:{utterance1}<eos><Reflection of Feelings> {utterance2}<eos>{utterance3}<eos><X> {utterance2}<eos>{utterance3}<eos><Self-disclosure><X> Decoder:<bos><X>{utterance4}<eos> Decoder:<bos><X>{utterance4}<eos> ContinuousPrompts ContinuousPrompts Encoder:<knowledge>{knowledge}<context><user> Encoder:<user>{utterance1}<eos><system><Reflection of {utterance1}<eos><system>{utterance2}<eos> Feelings>{utterance2}<eos><user>{utterance3}<eos> <user>{utterance3}<eos><system><X> <system><Self-disclosure><X> Decoder:<bos><X>{utterance4}<eos> Decoder:<bos><X>{utterance4}<eos> DiscretePrompts DiscretePrompts Encoder:The following is a conversation between a user Encoder:The following is a conversation between a user and and aknowledgeable system.The system’s utterances an empathetic system.The system can use various support |
|---|---|
|  | are grounded on the background knowledge:\n skills to provide emotional support to the user.\n {knowledge}\nConversationcontext:\nUser: User:{utterance1}\nSystemreflects and describes user’s Bart/blender {utterance1}\nSystem:{utterance2}\nUser:{utterance3} feelings:{utterance2}\nUser:{utterance3}\nSystemshares \nSystem:<X> similar experiences or emotions:<X> Decoder:<bos><X>{utterance4}<eos> Decoder:<bos><X>{utterance4}<eos> Figure6: InputformatsforT5. NoPrompts NoPrompts Encoder:{knowledge}<eos>{utterance1}<eos> Encoder:{utterance1}<eos><Reflection of Feelings> {utterance2}<eos>{utterance3} {utterance2}<eos>{utterance3} |
|  | Decoder:<bos>{utterance4}<eos> Decoder:<bos><Self-disclosure>{utterance4}<eos> ContinuousPrompts ContinuousPrompts Encoder:<knowledge>{knowledge}<context><user> Encoder:<user>{utterance1}<eos><system><Reflection of {utterance1}<eos><system>{utterance2}<eos> Feelings>{utterance2}<eos><user>{utterance3} <user>{utterance3} Decoder:<bos><Self-disclosure>{utterance4}<eos> Decoder:<bos>{utterance4}<eos> DiscretePrompts DiscretePrompts Encoder:The following is a conversation between a user and Encoder:The following is a conversation between a user an empathetic system.The system can use various support and aknowledgeable system.The system’s utterances skills to provide emotional support to the user.\n are grounded on the background knowledge:\n User:{utterance1}\nSystemreflects and describes user’s {knowledge}\nConversationcontext:\nUser: feelings:{utterance2}\nUser:{utterance3}\nSystemshares {utterance1}\nSystem:{utterance2}\nUser:{utterance3} similar experiences or emotions: \nSystem: Decoder:<bos>{utterance4}<eos> Decoder:<bos>{utterance4}<eos> Figure7: InputformatsforBARTandBlender. KnowledgePostposition |
| KnowledgePostposition The following is a conversation between a user and a knowledgeable system.\n Conversationcontext:\n User:{utterance1}\nSystem:{utterance2}\n User:{utterance3}\n \n The system’s utterances are grounded on the background knowledge:\n {knowledge}\n What is the system’s next response?\n System:{utterance4}\n PersonaPostposition The following is a conversation between a user and an engaging system.\n Conversationcontext:\n User:{utterance1}\nSystem:{utterance2}\n User:{utterance3}\n \n The system’s utterances are grounded on the persona profile:\n {persona}\n What is the system’s next response?\n System:{utterance4}\n Figure8: Post-positioningtheGSindiscreteprompts. | KnowledgePostposition |


**Table (Page 12):**

| NoPrompts Encoder:{knowledge}<eos>{utterance1}<eos> {utterance2}<eos>{utterance3}<eos><X> Decoder:<bos><X>{utterance4}<eos> |
|---|
| ContinuousPrompts Encoder:<knowledge>{knowledge}<context><user> {utterance1}<eos><system>{utterance2}<eos> <user>{utterance3}<eos><system><X> Decoder:<bos><X>{utterance4}<eos> |
| DiscretePrompts Encoder:The following is a conversation between a user and aknowledgeable system.The system’s utterances |
| are grounded on the background knowledge:\n {knowledge}\nConversationcontext:\nUser: Bart/blender {utterance1}\nSystem:{utterance2}\nUser:{utterance3} \nSystem:<X> Decoder:<bos><X>{utterance4}<eos> |


**Table (Page 12):**

| NoPrompts Encoder:{utterance1}<eos><Reflection of Feelings> {utterance2}<eos>{utterance3}<eos><Self-disclosure><X> Decoder:<bos><X>{utterance4}<eos> |
|---|
| ContinuousPrompts Encoder:<user>{utterance1}<eos><system><Reflection of Feelings>{utterance2}<eos><user>{utterance3}<eos> <system><Self-disclosure><X> Decoder:<bos><X>{utterance4}<eos> |
| DiscretePrompts Encoder:The following is a conversation between a user and an empathetic system.The system can use various support |
| skills to provide emotional support to the user.\n User:{utterance1}\nSystemreflects and describes user’s feelings:{utterance2}\nUser:{utterance3}\nSystemshares similar experiences or emotions:<X> Decoder:<bos><X>{utterance4}<eos> |


**Table (Page 12):**

| NoPrompts Encoder:{knowledge}<eos>{utterance1}<eos> {utterance2}<eos>{utterance3} |
|---|
| Decoder:<bos>{utterance4}<eos> |
| ContinuousPrompts Encoder:<knowledge>{knowledge}<context><user> {utterance1}<eos><system>{utterance2}<eos> <user>{utterance3} Decoder:<bos>{utterance4}<eos> |
| DiscretePrompts Encoder:The following is a conversation between a user and aknowledgeable system.The system’s utterances are grounded on the background knowledge:\n {knowledge}\nConversationcontext:\nUser: {utterance1}\nSystem:{utterance2}\nUser:{utterance3} \nSystem: Decoder:<bos>{utterance4}<eos> |


**Table (Page 12):**

| NoPrompts Encoder:{utterance1}<eos><Reflection of Feelings> {utterance2}<eos>{utterance3} |
|---|
| Decoder:<bos><Self-disclosure>{utterance4}<eos> |
| ContinuousPrompts Encoder:<user>{utterance1}<eos><system><Reflection of Feelings>{utterance2}<eos><user>{utterance3} Decoder:<bos><Self-disclosure>{utterance4}<eos> |
| DiscretePrompts Encoder:The following is a conversation between a user and an empathetic system.The system can use various support skills to provide emotional support to the user.\n User:{utterance1}\nSystemreflects and describes user’s feelings:{utterance2}\nUser:{utterance3}\nSystemshares similar experiences or emotions: Decoder:<bos>{utterance4}<eos> |


**Table (Page 12):**

| KnowledgePostposition |
|---|
| The following is a conversation between a user and a knowledgeable system.\n Conversationcontext:\n User:{utterance1}\nSystem:{utterance2}\n User:{utterance3}\n \n The system’s utterances are grounded on the background knowledge:\n {knowledge}\n What is the system’s next response?\n System:{utterance4}\n |
| PersonaPostposition The following is a conversation between a user and an engaging system.\n Conversationcontext:\n User:{utterance1}\nSystem:{utterance2}\n User:{utterance3}\n \n The system’s utterances are grounded on the persona profile:\n {persona}\n What is the system’s next response?\n System:{utterance4}\n |
