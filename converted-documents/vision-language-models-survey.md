---
title: "Vision Language Models Survey"
original_file: "./Vision_Language_Models_Survey.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["prompt-engineering", "llm", "rag", "fine-tuning", "evaluation"]
keywords: ["video", "stage", "vtimellm", "visual", "training", "llm", "events", "temporal", "model", "text"]
summary: "<!-- Page 1 -->


### VTimeLLM: Empower LLM to Grasp Video Moments

BinHuang,XinWang*,HongChen,ZihanSong,WenwuZhu*

### TsinghuaUniversity

{huangb23, h-chen20, songzh23}@mails.tsinghua.edu.cn
{xin wang,wwzhu}@tsinghua.edu.cn

### Abstract

Large language models (LLMs) have shown remarkable text understanding capabilities, which have been ex-
0s 1s 3s 5s 7s 9s 11s 13s 15s 16s
tended as Video LLMs to handle video data for compre-
Ground Truth: From 0s to 4s. However, existing Video LLMs During wh"
related_documents: []
---

# Vision Language Models Survey

<!-- Page 1 -->


### VTimeLLM: Empower LLM to Grasp Video Moments

BinHuang,XinWang*,HongChen,ZihanSong,WenwuZhu*

### TsinghuaUniversity

{huangb23, h-chen20, songzh23}@mails.tsinghua.edu.cn
{xin wang,wwzhu}@tsinghua.edu.cn

### Abstract

Large language models (LLMs) have shown remarkable text understanding capabilities, which have been ex-
0s 1s 3s 5s 7s 9s 11s 13s 15s 16s
tended as Video LLMs to handle video data for compre-
Ground Truth: From 0s to 4s.
hending visual details. However, existing Video LLMs During which time period in the video does the event 'person
close the laptop' happen?
can only provide a coarse description of the entire video,
(VideoChat) The man closes the laptop from 13.0 second to 13.6 second.❌
failing to capture the precise start and end time boundary of specific events. In this paper, we solve this is- (VideoLLaMA) The event happens at the 15-second mark. ❌
sue via proposing VTimeLLM, a novel Video LLM de- (VTimeLLM, ours) The person closes the laptop from 00 to 30. (0s ~ 4.8s) ✔
signed for fine-grained video moment understanding and
Figure 1. Existing Video LLMs, such as VideoChat and Videreasoning with respect to time boundary. Specifically, our
oLLaMA,exhibitadeficiencyinboundaryawareness,leadingto

### VTimeLLM adopts a boundary-aware three-stage training

challengesinaccuratelycapturingtheprecisetimestampsofspestrategy,whichrespectivelyutilizesimage-textpairsforfeacificevents.
turealignment,multiple-eventvideostoincreasetemporalboundary awareness, and high-quality video-instruction
tuningtofurtherimprovetemporalunderstandingabilityas
tempts [15, 20, 34] utilize LLMs for video understanding.
well as align with human intents. Extensive experiments
Nevertheless, these works predominantly focus on generademonstrate that in fine-grained time-related comprehentionofgenericvideocaptionsandcanmerelyoffersurfacesion tasks for videos such as Temporal Video Grounding
level summaries of the content, thus failing to capture the
andDenseVideoCaptioning,VTimeLLMsignificantlyoutrelationships between specific moment boundaries and the
performs existing Video LLMs. Besides, benefits from the
boundedevents,asshowninFigure1.
fine-grained temporal understanding of the videos further
To tackle the problem, in this paper, we investigate imenableVTimeLLMtobeatexistingVideoLLMsinvideodiproving the boundary-aware ability of Video LLM, which
alogue benchmark, showing its superior cross-modal unfacesthefollowingtwochallenges.
derstandingandreasoningabilities. 1

## Thereisascarcityoflarge-scalevideodatasetswithaccurateboundaryannotationstotraintheVideoLLMfor

temporalalignment.

## Introduction


## Itisnon-trivialtodesigneffectivetemporal-relatedvideo

Large language models (LLMs) have garnered significant tasksfortrainingLLMtounderstandthecontentofmulattention due to their exceptional capabilities in text un- tiplemomentswithinvideos.
derstanding and generation [23, 31]. However, harness- To address these challenges, we propose VTimeLLM,
ing the potential of LLMs for understanding and reason- a novel Video LLM that can perceive fine-grained seging over multimodal data, especially videos, still remains ments in videos with better temporal reasoning ability.
a substantial challenge. This is because analyzing videos VTimeLLM consists of i) a visual encoder and a visual
requires deep understanding of both visual details and adapter to process the input video, and ii) a tailored LLM
temporal dynamics for models. Several preliminary at- tounderstandbothtextandvideocontent,whichistrained
via a novel boundary-aware three-stage training strategy.
*CorrespondingAuthors.
1Our project page is at https://github.com/huangb23/ Specifically, visual features are aligned with LLM’s se-
VTimeLLM mantic space through image-text training in the first stage.
1
3202
voN
03
]VC.sc[
1v54481.1132:viXra

<!-- Page 2 -->

In the second stage, we then design the single-turn and thecapabilitytodescribeintricateimagedetails.
multi-turn related question answering (QA) tasks to endueVTimeLLMwiththeawarenessoftimeboundariesand
Video LLMs Driven by the success of Image LLM, retheabilitytounderstandthecorrespondingeventsbounded
searchers have naturally extended their focus from singlewithintheboundaries. Weemployalarge-scalevideo-text
frame images to multi-frame videos, leading to the emerdataset containing multiple segments together with their
gence of Video-compatible LLMs like VideoChat [15],
roughly annotated labels for training VTimeLLM with the

### Video-LLaMA[34],andVideo-ChatGPT[20]. Thesemod-

QA tasks. Finally, in the third stage, we further creels employ a two-stage training strategy. In the first stage,
ate a high-quality dialogue dataset for instruction tuning,
large-scale datasets align video features with the feature
which simultaneously aligns VTimeLLM with human inspace of LLMs. In the second stage, a limited amount of
tentionandenablesVTimeLLMtoconducttemporalunder-

### GPT-annotated or human-annotated datasets are used for

standingforvideosegmentsmoreprecisely. Extensiveexinstruction tuning. While these models exhibit impressive
perimentsshowthatVTimeLLMsignificantlyoutperforms
overallvideocomprehension,theirabilitiestodescribespeexisting Video LLMs in time-related video understanding
cific video segments and perform temporal reasoning retasks,suchasTemporalVideoGroundingandDenseVideo
main limited. The limitation arises mainly due to the na-

### Captioning. In addition, benefiting from the fine-grained

tureofdatasetsusedinthefirsttrainingstage,suchasWebtemporal understanding of videos, VTimeLLM is able to

### Vid[2],whichusuallyconsistofone-eventvideosandnoisy

beat existing Video LLMs in video dialogue benchmark,
textualannotations. Moreover,thescarcityofhigh-quality,
demonstratingitssuperiorityincross-modalunderstanding
temporallyannotateddatainthesecondstageposesachaland reasoning for videos. Our contributions in this paper
lengeformodelstoconducttemporalreasoning. Tobridge
arelistedasfollows,
this gap, our approach, VTimeLLM, introduces a bound-
• WeproposeVTimeLLM,thefirstboundary-awareVideo ary perception stage between these two stages. This stage
LLM,tothebestofourknowledge. enables the model to precisely locate events within videos
• Weproposetheboundary-awarethree-stagetrainingstrat- and describe multiple distinct events accurately, empoweregy, which consecutively leverages i) large-scale image- ing our model to grasp fine-grained details of video motextdataforfeaturealignment,ii)large-scalemulti-event ments.
video-textdatatogetherwiththetemporal-relatedsingleturnandmulti-turnQAtoenhancetheawarenessoftime 2.2.Fine-GrainedVideoUnderstanding
boundary, and iii) instruction tuning on the high-quality
Fine-grained video understanding, the ability to precisely
dialogdatasetforbettertemporalreasoningability.
locate and comprehend specific events within a video, is
• We conduct extensive experiments to demonstrate that
a crucial challenge for video analysis. When integrated
theproposedVTimeLLMsignificantlyoutperformsexistwith natural language, there are two primary tasks: TemingVideoLLMsinvariousfine-grainedtemporal-related
poral Video Grounding [1, 8] and Dense Video Captionvideotasks,showingitssuperiorabilityforvideoundering[12,25].
standingandreasoning.

## RelatedWorks TemporalVideoGrounding TemporalVideoGrounding

aims to identify corresponding video segments for given

### MultimodalLargeLanguageModel textual inputs. Traditional approaches can be categorized

into two types: proposal-based [4, 29, 32] and proposal-

### ImageLLMs ToenableLargeLanguageModels(LLMs)

freemethods[9,30,33]. Proposal-basedtechniquesgenerto comprehend visual information, significant efforts have
ate candidate proposals before ranking them based on relbeenmadetoalignvisualandlinguisticmodalities. BLIP-
evance. Incontrast, proposal-freemethodsdirectlypredict
2[14]introducedtheconceptofQ-Former,utilizinglearnthestartandendboundariesofthetargetmoment.
able query vectors to extract visual features from frozen
image encoders. MiniGPT-4 [37] demonstrated that further fine-tuning with detailed image descriptions signifi- Dense Video Captioning Dense Video Captioning is a
cantlyenhancesitsusability. LLAVA[16]exploreddiverse more intricate task, demanding both temporal localization
multi-modal instruction-following data, including conver- and captioning for all events within an untrimmed video.
sations,detaileddescriptions,andcomplexreasoning,aim- Earlier methods [6, 11, 12] employed a two-stage process
ing to construct a general-purpose visual assistant. Recent involvingtemporallocalizationfollowedbyeventcaptionendeavors, such as Kosmos-2 [21] and VisionLLM [26], ing. Recent developments [25, 28, 36] in this field have
delvedintomoredetailedaspectsofimagecomprehension, witnessed a shift towards joint training of captioning and
including referring and grounding, significantly enhancing localizationmodules. Forinstance,Vid2Seq[28],enhances
2

<!-- Page 3 -->

alanguagemodelbyincorporatingspecifictimetokens,en- Input of LLM To enable the simultaneous processing
abling the model to generate event boundaries and textual of video and text inputs, we introduce a special token,
descriptionswithintheunifiedoutputsequence. ‘<video>’,torepresentthevideocontent.Moreintuitively,
Both these two tasks share a fundamental requirement: ifwewanttoasktheLLMquestionsaboutthevideo,wecan
the alignment of video segments with semantic context. useamixeddescription,e.g.,“Thisisavideo<video>can
Leveraging the power of LLM with the help of our train- youdescribethisvideo?”. Withthismixeddescription,the
ingstrategy,ourVTimeLLMmodelunifiesthesetasksand embeddinglayerwilltransformthetextualwordsexceptfor
has demonstrated remarkable effectiveness. Concurrently, <video> intoembeddingastheLLMoriginallydoes,and
VTimeLLM enables natural language interaction with hu- we will obtain a textual embedding list [w ,w ,··· ,w ]

## 1 2 M

mans, establishing itself as an excellent assistant for com- for the text description, where w ∈ Rd is the embedding
i
prehendingvideocontent. foreachwordandM isthewordnumber. Then,thevideo
featuresequencewillbeinsertedintotheembeddinglist,at

## VTimeLLM: Being Aware of Time Bound- thepositionof<video> asfollows,

ariesinVideos
input=[w ,··· ,w ,Z,w ,··· ,w ], (3)
1 j−1 j M

### Inthissection,weintroduceVTimeLLM,whichisdesigned

where j − 1 and j are the indexes of the words that are
tograspprecisevideomomentsforLLMs. Wefirstprovide
closetothespecialtoken<video>intheoriginalsentence.
a detailed description of the model architecture, and then
(In the previous example, w corresponds to the word
our innovative boundary-aware three-stage training frame- j−1
“video”, w corresponds to the word “can”). Then LLM
work,asshowninFigure2. j
canfurtherencodetheinputembeddinglistinputtounder-

### Architecture standthevideoandtheuserquery.


### ToenabletheLLMtocomprehendvideos,ourVTimeLLM


### Output for Temporal Boundaries We employ the text

model incorporates two additional modules within LLM,
format ‘from s to e’ to denote a video moment, where s
i.e.,thevisualencoderandthevisualadapter,whichtransanderepresentthestartingandendingframeindexesofthe
formthevisualinformationintotextspace.
moment, ranging from 00 to 99, with each number correspondingtoaspecificframe.
VisualEncoder OurVTimeLLMmodelutilizesafrozen

### Boundary-awareTraining

CLIPViT-L/14[22]asthevisualencoder,andforsimplicity we denote it as ViT. Given a video V ∈ RT×H×W×C In contrast to the previous typical two-stage training apwith T frames, we uniformly sample N = 100 frames, proaches[15,20,34], consistingofalignmentandinstrucrepresented as V˜ ∈ RN×H×W×C, where V˜ 1 = V 1 and tiontuning, ourapproachintroducesanadditionalstageto
V˜ N = V T . Each frame V˜ i is independently processed improve the temporal understanding ability of the model.
throughthevisualencoder: Specifically,thefirststage,featurealignment,aimstotrain
the visual adapter, to align video features with LLM’s se-
{vcls,v1,v2,...,vp}=ViT(V˜),i=1,2,...,N, (1)
i i i i i mantic space. The second stage, boundary perception, focuses on enabling LLM to develop attentional capabilities
whereprepresentsthenumberofpatchesintheViT.
forspecificmoments,facilitatingtheunderstandingofvariouseventsoccurringwithinthevideo. Thethirdstage,in-
Visual Adapter We utilize the global feature vcls as the struction tuning, allows LLM to align with human intent
i
feature for the i-th frame, and apply a linear layer f(·) to and enabling more precise event localization and descripprojectthefeaturesofeachframeintothesameembedding tion. In the following sections, we will elaborate on the
spaceasthatofLLM: trainingmethodsanddatasetsutilizedforeachofthesethree
stages.
z =f(vcls),i=1,2,...,N. (2)
i i
3.2.1 Stage1: FeatureAlignment

### Subsequently, Z = {z } ∈ RN×d becomes the input sei

quencethatLLMcancomprehend, anddisthehiddendi- Data Organization In the feature alignment stage, we
mensionofLLM. employ the image-text LCS-558K dataset as curated by
Note that in the visual modules, we do not model the LLaVA[16].Thisdatasetismeticulouslyfilteredtoachieve
temporal relationships for the frames, inspired by the fact amorebalanceddistributionofconceptualcoverage. ComthattheLLMitselfcanreceivesequentialinputembeddings prising image-text pairs, we deliberately choose not to inandcapturetheirtemporalrelations. corporate datasets containing video-text pairs with the fol-
3

<!-- Page 4 -->

Text paired with image Template-based Answer High-quality Answer
A grey watch with an army People are snowboarding down a large hill of snow, Of course! These two people play rock-paper-scissors twice.
style strap. from 00 to 93. The people get to the bottom and The first time is from 50 to 65, and after the woman puts a
start taking their snowboards off, from 94 to 99. blindfold on, they play again, from 81 to 88.
Vicuna Vicuna LoRA Vicuna LoRA LoRA

### System Template-based System

... ... High-quality Question

### Prompt Question Prompt


### Could you please detail


### Can you help me count how

Visual Visual the events that took Visual many times the two people
Adapter Adapter place during different Adapter play rock-paper-scissors in
time segments in the
the video?
video?

### Visual Visual Visual

Encoder Encoder Encoder
Image Video Video
... ...
Figure2. Ourboundary-awarethree-stagetrainingframework. Inthefirststage,visualfeaturesarealignedwithLLM’ssemanticspace
through image-text training. In the second stage, we transform a large-scale multi-event dataset into a QA format based on templates,
trainingVTimeLLMtopossesstemporalboundaryawarenessandunderstandeventswithintheboundaries. Inthethirdstage,wecreate
ahigh-qualitydialoguedatasetforinstructiontuning,whichalignsVTimeLLMwithhumanintentandalsoenablesmoreprecisevideo
temporalunderstanding.
lowing two considerations. Firstly, contemporary large- tiveoftheLLM.
scale video-text datasets contain substantial textual noise,
which severely impedes the alignment between visual fea-
3.2.2 Stage2: BoundaryPerception
tures and textual semantics. Secondly, the transformation
from visual information to text space usually suffers from Afterthetraininginthefirststage,theLLMmodelbecomes
informationloss,e.g. whencaptioninganimageoravideo proficient in understanding visual information. In the secinto “a dog is running on the grass”, we may lose infor- ondstage, weenhancethemodel’scapabilitiestocompremation about the visual details (such as the color) of the hendsequentialimageframes,i.e.,video,encompassingthe
dog. Comparatively,thelossofinformationresultingfrom semantic understanding of video segments while ensuring
summarizinganimageintoafewwordsislessthanthatof alignmentwiththecorrespondingboundaries.
videos. Our experiments also demonstrate the superiority
ofusingimagedatasetsforalignmentovervideodataset(a

### DataOrganization Duetothetime-consumingnatureof

filtered subset [19] of WebVid2M [2]), and even a combimanually annotating timestamps and semantics for video
nationofboth.
segments,thereiscurrentlyalackoflarge-scalemulti-event
video-text datasets. Traditional methods align video seg-
Training Strategy For each image-text pair <I, T> in
mentswithtexttranscriptsgeneratedbyAutomaticSpeech
the dataset, a special token <image>is directly appended
Recognition (ASR). However, this approach faces chalbeforethetextT, theembeddingofthistokenisextracted
lenges due to the lack of synchronicity and consistency
with the visual encoder and the visual adapter as follows,
between actions performed and spoken content, leading
denotedasZ :
I to weak correlations and inaccuracies in boundary annota-
Z =f(ViT(I)cls), (4) tions.

## I


### Recently, we identified the InternVid-10M-FLT [27]

andwecanobtaintheembeddingsequence: dataset, which offers a viable solution for our boundaryawaretraining. Thisdatasetemploysanentirelyautomated
input=[Z ,w ,w ,··· ,w ]. (5)

## I 1 2 M

process to segment and annotate video clips, eliminating
Subsequently, we can use the sequence to train the visual the need for manual intervention. Consequently, a single
adapter f, with the original auto-regressive training objec- video may contain multiple event annotations. To ensure
4

<!-- Page 5 -->

Box1:Examplesofbothsingle-turnandmulti-turnQAforavideocontainingthreeevents.
Single-turnQA.
Q :Couldyoupleasedetailtheeventsthattookplaceduringdifferenttimesegmentsinthevideo?
1
A :T ,froms toe .T ,froms toe .T ,froms toe .
1 1 1 1 2 2 2 3 3 3
Multi-turnQA.
Q :Canyoudescribewhatoccurredfroms toe inthevideo?A :T .
1 2 2 1 2
Q :Tellmeabouttheeventsfroms toe .A :T .
2 3 3 2 3
Q :DuringwhichframesinthevideocanweobserveT happening?A :Froms toe .
3 1 3 1 1

### Box2:TheinputstoVTimeLLMinStage2andStage3

Achatbetweenacurioususerandanartificialintelligenceassistant. Theassistantgiveshelpful,detailed,and
politeanswerstotheuser’squestions.
USER:Thisisavideowith100frames:<video>\n Q ASSISTANT:A </s>
1 1
USER:Q ASSISTANT:A </s>......
2 2
suitability for our study, we selected specific videos, each Training Strategy We format these QA pairs according
notexceeding120secondsinlength. Thesevideosencom- to the original LLM’s format, keeping the initial system
passmultiplenon-overlappingeventannotations,eachlast- promptsintact.Moreover,weinsertthestatement“Thisisa
ingmorethan3seconds,andtheaveragedurationofthese videowith100frames: <video>\n”beforethefirstquesevents exceeds 8% of the video length. Thus, we curate a tion. For illustration purposes, the input for VTimeLLM
datasetcomprising134kvideos,whereeachvideocontains is presented in Box 2. With the reformated sequences, we
multiple events and their rough temporal annotations and continue to employ the auto-regressive training objective,
descriptions. wherethelossiscomputedexclusivelyonthetokenswithin
the answer of the QA dialogues(A , A , ...). To enhance
1 2
training efficiency, we utilize LoRA [10] for fine-tuning
the LLM. During this stage, we keep the visual adapter f
Ineachvideo,aseriesofevents{s ,e ,T }iscontained,
i i i
frozen. Consequently,theonlytrainableparametersarethe
where s and e represent the start and end timestamps of
i i
newlyappliedLoRAmodules.
a segment, ranging from 00 to 99. T corresponds to its
i
textualdescription. Totransformtheseeventsintodialogue
data{Q ,A ,Q ,A ,...}suitablefortrainingLLM,wede-
1 1 2 2
visetwotypesofQAdialogues: single-turnandmulti-turn,
constituting20%and80%respectively. InBox1,wehave 3.2.3 Stage3: InstructionTuning
provided examples of both single-turn and multi-turn QA
dialoguesforavideocontainingthreeevents. Specifically, Followingthetraininginthesecondstage,ourVTimeLLM
the task of single-turn QA is dense video captioning. Q model demonstrates the ability to comprehend all events
1
prompts a question requiring a comprehensive description within the video and align them with the corresponding
ofalleventsandtheircorrespondingtimestamps,whileA timestamps. Despite the diverse templates employed, the
1
outputs the respective textual descriptions and timestamps model’soutputstilltendstooverfittheanswers,whichbein a specified format as shown in the upper box of Box 1. havesmorelikeamulti-taskpretrainedmodelwhilelosing
On the other hand, multi-turn QA involves segment cap- chatting ability with the user, e.g., when we input “What
tioningandtemporalvideogroundingtasks,demandingthe coloristhecoatoftheman”tothemodel,itmayresponse
descriptiongenerationgiventimestampsortimestampsgen- “from00to10”. Additionally, thelabelsofthevideo-text
erationgivendescriptions,asshowninthelowerboxofBox datainthesecondstageareoriginallyannotatedinanauto-

## In multi-turn QA, each event will be randomly queried matedway,whicharenotsoaccurateandnoisy. Totackle

foroneofthesetwotasks,andthequestionsarenotneces- the two problems, in the third stage, we incorporate highsarilypresentedintheorderoftheevents’occurrence. We quality dialogue data for instruction tuning, enabling the
design 10 templates for each task to transform events into modeltofollowhumaninstructionsformoreaccuratevideo
QAdialogues,whichcanbefoundintheappendix. temporalcomprehensionandreasoning.
5

<!-- Page 6 -->

DataOrganization Inthisstage,weselectasubsetfrom For the Temporal Video Grounding task, we utilize
ActivityNet Captions [12] and DiDeMo [1] datasets, and datasets from ActivityNet Captions [1] and Charadestransform it into a high-quality QA dialogue dataset with STA [8]. We calculate the Intersection over Union (IoU)
the assistance of Large Language Models. In contrast to betweenthetimesegmentsgeneratedbythemodelandthe
InternVidwhichemploysautomatedsegmentingandlabel- correspondinggroundtruthtimesegments. Wereportmean
ing,thesetwodatasetsareentirelymanuallyannotated,re- IoU(mIoU)andrecall@1,IoU≥ m(R@m)metric,where
sulting in descriptions that are more detailed and tempo- mvaluesaresetat{0.3,0.5,0.7}.
ral boundaries that are more accurate. Specifically, we In the case of Dense Video Captioning, we employ the
carefully selected a subset of videos from the training set ActivityNet Captions [1] dataset. The evaluation process
of ActivityNet Captions. These videos contained a mini- encompasses two categories of metrics. Firstly, we emmum of three non-overlapping events, collectively cover- ploy SODA c [7], a metric specifically tailored for dense
ing over 90% of the video duration, amounting to approx- video caption tasks, taking into account the video’s stoimately 4.2k videos. Similarly, a subset of videos is being ryline. Secondly, we compute matched pairs between the
selected for the DiDeMo dataset, each containing at least generated events and the ground truth across IoU threshtwonon-overlappingeventsandcovering40%ofthevideo oldsof{0.3,0.5,0.7,0.9},andcalculatecaptioningmetrics
duration. Thisprocessresultsinatotalofabout4kvideos based on these matched pairs [28]. We report CIDEr [24]
for the DiDeMo subset. Subsequently, we also transform and METEOR [3] averages under different IoU thresholds
these videos, which contain a series of events {s ,e ,T }, toprovideacomprehensiveanalysis.
i i i
intoQAdialogues. However,resultsfromthesecondstage
of training indicate that template-based conversations lead

### Implementation Details In our study, we use Vicuna

to model overfitting. Therefore, we utilize LLM for this
v1.5 [5] as the Large Language Model and train two vertransformation. Specifically,weprovidetheseeventstothe
sions:7Band13B.Weuseatotalbatchsizeof128through-
LLM, prompting it to assume the role of an AI visual asoutthetrainingprocess. TheAdamW[18]optimizerisapsistant capable of analyzing the video and generate a diaplied with a cosine learning rate decay and a warm-up pelogueaboutthevideobetweenitselfandauser.Theprompt
riod. Inthefirsttrainingstage,thetotalepochnumberis1
canbefoundintheappendix. ThisapproachresultsinQA with a learning rate of 1×10−3, and the subsequent secdialogues that are grammatically correct, linguistically coond and third stages we will train for 2 epochs each with
herent, and may encompass a variety of tasks. We gener- alearningrateof1×10−4. TheLoRAparametersareset
ate two distinct sets of dialogues for each video, yielding
to r = 64 and alpha = 128. Thanks to the efficiency of
a final dataset comprising around 16k high-quality QA di-

### LoRA,wecancompletethetrainingofthe7Bmodelwithin

alogues. Additionally, we observe that introducing a com-
30hourswith1RTX-4090GPU.
parable number of other video instruction tuning datasets
further enhances the descriptive capabilities of the model, 4.2.MainResults
with minimal impact on temporal understanding abilities.

### WeevaluatethecapabilitiesofexistingVideoLLMsintem-

Therefore,weaddanextra20kQApairsfromtheVideoInporalvideogroundinganddensevideocaptioningtasks,as
struct100K[20]dataset. Overall,inthisstage,atotalofapshown in Table 1. Detailed information about the evaluaproximately36kQAdialoguesareusedfortraining,which
tion process can be found in the appendix. VTimeLLM-
is significantly smaller than the dataset used in the second
7B outperforms these Video LLMs of the same size by a
stage.
significant margin. Upon further scaling up the model to
13Bparameters,weobserveminorchangesinperformance
Training Strategy We merge the LoRA module trained on ActivityNet tasks, while the temporal grounding abilin the second stage with the original model and introduce ityimprovesonCharades-STA.Itisworthmentioningthat
a new LoRA module, which serves as the only trainable ourtrainingdatasetdoesnotincludeCharades-STAtraining
parameters.Allothertrainingdetailsremainconsistentwith data,indicatingthatincreasingthescaleofourVTimeLLM
thoseofthesecondstage. modelenhancesitsout-of-distributiongeneralizationcapability.

## Experiment


### We provide several possible explanations to account

for the poor performance of other models: firstly, both

### ExperimentSetup


### VideoChat and VideoLLaMA extract only N=8 frames as

Tasks, Dataset, and Evaluation Metrics To assess the input, making it challenging for them to achieve a finecapability of VTimeLLM in comprehending various event grained understanding of the video content. Secondly,
segments, we mainly conduct evaluations on two tasks: the commonly used LLM (Vicuna) lacks robust positional
TemporalVideoGroundingandDenseVideoCaption. awareness in input sequences. For instance, when posed
6

<!-- Page 7 -->

Table1.TheresultsofexistingVideoLLMsintemporalvideogroundinganddensevideocaptioningtasks.

### TemporalGrounding DenseCaptioning


### Model ActivityNet Charades-STA ActivityNet

R@0.3 R@0.5 R@0.7 mIoU R@0.3 R@0.5 R@0.7 mIoU SODA c CIDEr METEOR
VideoChat-7B[15] 8.8 3.7 1.5 7.2 9.0 3.3 1.3 6.5 0.9 2.2 0.9
VideoLLaMA-7B[34] 6.9 2.1 0.8 6.5 10.4 3.8 0.9 7.1 1.9 5.8 1.9
VideoChatGPT-7B[20] 26.4 13.6 6.1 18.9 20.0 7.7 1.7 13.7 1.9 5.8 2.1
VTimeLLM-7B 44.0 27.8 14.3 30.4 51.0 27.5 11.4 31.2 5.8 27.6 6.8
VTimeLLM-13B 44.8 29.5 14.2 31.4 55.3 34.3 14.7 34.6 5.9 27.2 6.7
Table2. Ablationstudyofthethree-stagetrainingstrategy. InStage1,“I”and“V”representtheutilizationofimageorvideodatasets,
and“I+V”signifiesthemergingofbothdatasets. InStage2,wecompareoptionsforFreezingorTuningthevisualadapter. InStage3,
“Reuse”indicatesthereuseoftheLoRAfromStage2,while“Addition”signifiestheadditionofanewLoRAmodule. “✗”represents
theabsenceoftraininginthisstage.

### TemporalGrounding DenseCaptioning

Row Stage1 Stage2 Stage3 ActivityNet Charades-STA ActivityNet
R@0.3 R@0.5 R@0.7 mIoU R@0.3 R@0.5 R@0.7 mIoU SODA c CIDEr METEOR
1 Freeze 36.1 21.4 10.5 25.5 48.4 23.7 11.5 32.2 4.6 17.0 5.4

## I ✗

2 Tune 35.6 21.4 10.2 24.8 48.0 24.4 12.1 31.6 4.6 17.0 5.5
3 Freeze 33.5 17.9 8.1 23.9 46.6 17.7 6.7 30.5 4.0 14.1 5.0

## V ✗

4 Tune 34.8 18.2 8.5 24.4 47.9 19.9 8.0 31.4 4.2 14.1 5.2
5 Freeze 31.3 16.5 6.8 22.2 47.5 21.9 9.2 30.6 4.1 13.4 5.0

## I+V ✗

6 Tune 33.5 17.4 6.9 23.2 47.1 21.4 8.6 30.6 4.0 13.6 4.8
7 ✗ Tune ✗ 42.2 22.7 11.5 29.8 40.0 4.9 0.0 27.5 3.7 10.2 5.0
8 I ✗ Addition 31.0 18.1 7.7 22.9 37.5 21.8 6.1 22.8 4.2 16.0 5.0
9 I Freeze Reuse 39.3 26.6 13.0 28.1 49.7 29.8 13.3 30.9 5.2 23.2 6.1
10 I Freeze Addition 44.0 27.8 14.3 30.4 51.0 27.5 11.4 31.2 5.8 27.6 6.8
withthequestion“Whatisthepositionoftheword‘video’ asequenceof100frameseventsposedistinctchallengesfor
inthephrase‘avideoclip’?”,itmayerroneouslyrespond, modelfitting.
“Theword‘video’appearsatposition67.” Relyingsolely Another question arises during the following stage:
on a limited set of temporally annotated data for instruc- shouldthepreviouslypretrainedvisualadapterbetunedor
tiontuningisinsufficienttoaddressthisissue. Therefore,it frozen? UponcomparingRow1vsRow2,Row3vsRow
isessentialtointegrateboundary-awaretrainingtoachieve 4, and Row 5 vs Row 6, we observed minor difference in
precisevideocomprehension. performance between the two approaches. To retain the
comprehensiveinformationacquiredduringthepretraining

### AblationStudy

stage,weopttofreezetheparametersofthevisualadapter
In this section, we provide detailed ablations about our inthelattertwostages.
three-stagetrainingstrategythroughexperimentsonthe7B
model, as illustrated in Table 2. In the ablation, our most

### Q2:ShouldtheLoRAfromstage2bereusedinstage3?

conernedquestionsandtheirresultsareprovidedinthefol-
UponcomparingRow9toRow10,itisevidentthatinstage
lowing.
3, merging the LoRA module from the second stage with
theLLMparametersandadditionallyincorporatinganother

### Q1: Howtotrainagoodvisualadapter? Incontrastto

LoRA module yields superior results. This approach enother Video LLMs, we utilize a pure image modality for
suresthatthetemporalunderstandingcapabilitiesacquired
the first stage and find it to be superior across all metrics
duringstage2areeffectivelypreservedwithinthemodel.
than using a pure video modality (Rows 1, 2 vs Rows 3,
4). This effectiveness of using images to alignment could
beattributedtothehigherqualityandreducedinformation Q3: Is every training stage necessary? By comparing
lossinimagedatasets. Additionally,usingpureimagesout- Rows 1˜6 with Row 7, we observe a substantial disparity
performs the fusion of two modal datasets (Rows 1, 2 vs in the model’s performance on temporal grounding when
Rows5,6). Thiscouldbeduetothesignificantdisparityin training without stage 1. The scores are abnormally high
tasks,wheredescribingasingleframeeventanddescribing on the ActivityNet dataset, while significantly low on the
7

<!-- Page 8 -->

Table3.Theresultsofvideodialogueonvideo-basedgenerativeperformancebenchmarking.
EvaluationAspect VideoLLaMA LLaMA-Adapter VideoChat VideoChatGPT BT-Adapter VTimeLLM

### TemporalUnderstanding 1.82 1.98 1.94 1.98 2.34 2.49

CorrectnessofInformation 1.96 2.03 2.23 2.40 2.68 2.78

### DetailOrientation 2.18 2.32 2.50 2.52 2.69 3.10

ContextualUnderstanding 2.16 2.30 2.53 2.62 3.27 3.40
Consistency 1.79 2.15 2.24 2.37 2.46 2.47

### Mean 1.98 2.16 2.29 2.38 2.69 2.85

Charades-STAdataset.Uponcarefulanalysisoftheoutputs bilities, VTimeLLM achieves state-of-the-art results in all
underthissetting,wefindthatthemodelhasnoteffectively aspects. The most substantial improvement is observed in
learnedtolocalizeevents. Instead,ittendstopredictatem- theaspectofdetailorientation,whereVTimeLLMachieves
poral segment spanning nearly the entire video (e.g., from anoteworthyenhancementof+0.41(15.2%). Weattribute
00to95). Insuchcases,iftheratioofgroundtruthduration this progress to two primary factors. Firstly, the imageto video length is denoted as x, the IoU with the model’s based training in stage 1 ensures comprehensive preseroutputisapproximatelyx.TheActivityNetdatasetcontains vation of visual details in individual frames, facilitating
asignificantnumberoflongsamples, with20%ofqueries a detailed understanding of spatial dimension. Secondly,
having x > 0.5, leading to an inflated evaluation metric. the temporal-aware training employed in the second and
Conversely, intheCharades-STAdataset, xrarelyexceeds thirdstagesenablesVTimeLLMtocapturemultipleevents
0.5, demanding more precise localization [13]. However, withinvideos,enhancingitsabilitytodepictdetailsoftemthemodelwithoutstage1trainingfailstoachieveit. More- poraldimension.
over, themodel’sperformanceindensecaptioningtasksis To better illustrate the video dialogue performance of
unsatisfactory,whichalsohighlightstheessentialnatureof VTimeLLM,wepresentaqualitativeexample,asshownin
thefeaturealignmentstage. Figure3.
The necessity of stage 2 can be demonstrated by comparingRow8withRows9, 10. Despitethehigherquality
of annotations in stage 3, the limited dataset size hinders
themodel’sabilitytoachievearobusttemporalunderstand- Describe the video.
ing through stage 3 training alone. Models trained solely This video showcases a man crawling through a hole in a wall,
instage3exhibitinferiorperformanceacrossvarioustasks emerging into a dark room. He then continues crawling
through a pipe that leads him to a well. The video concludes
comparedtothosethathaveundergonepreliminarytraining with the man standing in the rain, gazing up at the sky.
instage2. When does he crawl through the pipe?
Afterstage3training,themodelexhibitscomprehensive The man crawl through the pipe from 51 to 68.

### Which movie does this video belong to?

improvement in the tasks outlined in the table (Row 1 vs
This video belongs to the movie "The Shawshank Redemption."
Row10). Furthermore,itregainschattingability,enabling
ittorespondtoawiderangeofquestionsposedbyhumans.
Figure3. Aqualitativeexampleofvideodialogue. Thevideois

### VideoDialoguePerformance 160secondslong.

Besides the ability for fine-grained video understanding
tasks, we explore whether VTimeLLM can address a

## Conclusion

broader range of questions through dialogue. We employ the Video-ChatGPT [20] benchmark and conduct an In this work, we introduce VTimeLLM, a Video LLM caevaluation of video-based generative performance. This pable of comprehending multiple events within a video
benchmark covers many questions associated with five and providing precise temporal boundaries. We unify
key aspects. GPT-3.5 assigns a score, not exceeding video tasks demanding fine-grained comprehension, such
5, to the model-predicted answer based on the ques- as temporal video grounding and dense video captioning,
tion and the correct answer. We present the average and pioneer their addressing using Video LLM. Specifscores in Table 3 and compare VTimeLLM with all exist- ically, we propose a three-stage temporal-aware training
ing Video LLMs, including VideoLLaMA [34], LLaMA- framework. This framework utilizes large-scale image-
Adapter[35],VideoChat[15],VideoChatGPT[20]andBT- text data for feature alignment, leverages extensive multi-
Adapter[17]. eventvideo-textdataalongwithtemporal-relatedquestion-
Thanks to the fine-grained video comprehension capa- answeringtoenhancetemporalawareness,andemploysin-
8

<!-- Page 9 -->

struction tuning on a high-quality dialogue dataset to im- [11] VladimirIashinandEsaRahtu. Abetteruseofaudio-visual
prove temporal reasoning ability. Extensive experiments cues: Dense video captioning with bi-modal transformer.
demonstrate that VTimeLLM outperforms existing Video arXivpreprintarXiv:2005.08271,2020. 2
LLMs significantly across various tasks, particularly ex- [12] Ranjay Krishna, Kenji Hata, Frederic Ren, Li Fei-Fei, and
celling in fine-grained temporal-related video tasks, show- JuanCarlosNiebles. Dense-captioningeventsinvideos. In
Proceedings of the IEEE international conference on coming VTimeLLM’s superior ability for video understanding
putervision,pages706–715,2017. 2,6
andreasoning.
[13] Xiaohan Lan, Yitian Yuan, Xin Wang, Long Chen, Zhi

### Wang, Lin Ma, and Wenwu Zhu. A closer look at debi-

References asedtemporalsentencegroundinginvideos:Dataset,metric,
andapproach.ACMTransactionsonMultimediaComputing,
[1] Lisa Anne Hendricks, Oliver Wang, Eli Shechtman, Josef

### CommunicationsandApplications,19(6):1–23,2023. 8


### Sivic, Trevor Darrell, and Bryan Russell. Localizing mo-

[14] Junnan Li, Dongxu Li, Silvio Savarese, and Steven Hoi.
ments in video with natural language. In Proceedings of
Blip-2: Bootstrapping language-image pre-training with
theIEEEinternationalconferenceoncomputervision,pages
frozen image encoders and large language models. arXiv
5803–5812,2017. 2,6
preprintarXiv:2301.12597,2023. 2
[2] Max Bain, Arsha Nagrani, Gu¨l Varol, and Andrew Zisser- [15] KunChang Li, Yinan He, Yi Wang, Yizhuo Li, Wenhai
man. Frozenintime: Ajointvideoandimageencoderfor Wang, Ping Luo, Yali Wang, Limin Wang, and Yu Qiao.
end-to-endretrieval. InProceedingsoftheIEEE/CVFInter- Videochat:Chat-centricvideounderstanding.arXivpreprint
nationalConferenceonComputerVision,pages1728–1738, arXiv:2305.06355,2023. 1,2,3,7,8
2021. 2,4
[16] HaotianLiu,ChunyuanLi,QingyangWu,andYongJaeLee.
[3] SatanjeevBanerjeeandAlonLavie. Meteor: Anautomatic Visualinstructiontuning. arXivpreprintarXiv:2304.08485,
metricformtevaluationwithimprovedcorrelationwithhu- 2023. 2,3
manjudgments. InProceedingsoftheaclworkshoponin- [17] Ruyang Liu, Chen Li, Yixiao Ge, Ying Shan, Thomas H
trinsicandextrinsicevaluationmeasuresformachinetrans- Li, and Ge Li. One for all: Video conversation is fealationand/orsummarization,pages65–72,2005. 6 sible without video instruction tuning. arXiv preprint
[4] JingyuanChen,XinpengChen,LinMa,ZequnJie,andTat- arXiv:2309.15785,2023. 8
SengChua.Temporallygroundingnaturalsentenceinvideo. [18] IlyaLoshchilovandFrankHutter. Decoupledweightdecay
InProceedingsofthe2018conferenceonempiricalmethods regularization. arXivpreprintarXiv:1711.05101,2017. 6
innaturallanguageprocessing,pages162–171,2018. 2 [19] RuipuLuo,ZiwangZhao,MinYang,JunweiDong,Minghui
[5] Wei-Lin Chiang, Zhuohan Li, Zi Lin, Ying Sheng, Zhang- Qiu, PengchengLu, TaoWang, andZhongyuWei. Valley:
haoWu,HaoZhang,LianminZheng,SiyuanZhuang,Yong- Videoassistantwithlargelanguagemodelenhancedability.
hao Zhuang, Joseph E. Gonzalez, Ion Stoica, and Eric P. arXivpreprintarXiv:2306.07207,2023. 4
Xing. Vicuna: An open-source chatbot impressing gpt-4 [20] MuhammadMaaz,HanoonaRasheed,SalmanKhan,andFawith90%*chatgptquality,2023. 6 hadShahbazKhan. Video-chatgpt: Towardsdetailedvideo
understandingvialargevisionandlanguagemodels. arXiv
[6] Xuguang Duan, Wenbing Huang, Chuang Gan, Jingdong
preprintarXiv:2306.05424,2023. 1,2,3,6,7,8

### Wang,WenwuZhu,andJunzhouHuang.Weaklysupervised

[21] ZhiliangPeng,WenhuiWang,LiDong,YaruHao,Shaohan
denseeventcaptioninginvideos. AdvancesinNeuralInfor-
Huang, Shuming Ma, and Furu Wei. Kosmos-2: GroundmationProcessingSystems,31,2018. 2
ingmultimodallargelanguagemodelstotheworld. arXiv
[7] SoichiroFujita,TsutomuHirao,HidetakaKamigaito,ManpreprintarXiv:2306.14824,2023. 2
abu Okumura, and Masaaki Nagata. Soda: Story oriented
[22] Alec Radford, Jong Wook Kim, Chris Hallacy, Aditya
densevideocaptioningevaluationframework. InComputer
Ramesh, Gabriel Goh, Sandhini Agarwal, Girish Sastry,
Vision–ECCV 2020: 16th European Conference, Glasgow,

### AmandaAskell,PamelaMishkin,JackClark,etal.Learning


### UK, August 23–28, 2020, Proceedings, Part VI 16, pages

transferable visual models from natural language supervi-
517–531.Springer,2020. 6
sion.InInternationalconferenceonmachinelearning,pages
[8] JiyangGao, ChenSun, ZhenhengYang, andRamNevatia.

## 8748–8763.Pmlr,2021. 3


### Tall: Temporalactivitylocalizationvialanguagequery. In

[23] Hugo Touvron, Louis Martin, Kevin Stone, Peter Albert,
Proceedings of the IEEE international conference on com-
Amjad Almahairi, Yasmine Babaei, Nikolay Bashlykov,
putervision,pages5267–5275,2017. 2,6
Soumya Batra, Prajjwal Bhargava, Shruti Bhosale, et al.
[9] Soham Ghosh, Anuva Agarwal, Zarana Parekh, and Llama2:Openfoundationandfine-tunedchatmodels.arXiv
Alexander Hauptmann. Excl: Extractive clip localiza- preprintarXiv:2307.09288,2023. 1
tion using natural language descriptions. arXiv preprint [24] Ramakrishna Vedantam, C Lawrence Zitnick, and Devi
arXiv:1904.02755,2019. 2 Parikh. Cider: Consensus-basedimage descriptionevalua-
[10] Edward J Hu, Yelong Shen, Phillip Wallis, Zeyuan Allen- tion. In Proceedings of the IEEE conference on computer
Zhu,YuanzhiLi,SheanWang,LuWang,andWeizhuChen. visionandpatternrecognition,pages4566–4575,2015. 6
Lora: Low-rankadaptationoflargelanguagemodels. arXiv [25] JingwenWang,WenhaoJiang,LinMa,WeiLiu,andYong
preprintarXiv:2106.09685,2021. 5 Xu. Bidirectional attentive fusion with context gating for
9

<!-- Page 10 -->

dense video captioning. In Proceedings of the IEEE conference on computer vision and pattern recognition, pages
7190–7198,2018. 2
[26] Wenhai Wang, Zhe Chen, Xiaokang Chen, Jiannan Wu,

### XizhouZhu,GangZeng,PingLuo,TongLu,JieZhou,Yu

Qiao, et al. Visionllm: Large language model is also an
open-endeddecoderforvision-centrictasks. arXivpreprint
arXiv:2305.11175,2023. 2
[27] Yi Wang, Yinan He, Yizhuo Li, Kunchang Li, Jiashuo Yu,

### Xin Ma, Xinyuan Chen, Yaohui Wang, Ping Luo, Ziwei

Liu, et al. Internvid: A large-scale video-text dataset for
multimodal understanding and generation. arXiv preprint
arXiv:2307.06942,2023. 4
[28] Antoine Yang, Arsha Nagrani, Paul Hongsuck Seo, AntoineMiech,JordiPont-Tuset,IvanLaptev,JosefSivic,and
CordeliaSchmid. Vid2seq: Large-scalepretrainingofavisuallanguagemodelfordensevideocaptioning.InProceedingsoftheIEEE/CVFConferenceonComputerVisionand

### PatternRecognition,pages10714–10726,2023. 2,6

[29] YitianYuan,LinMa,JingwenWang,WeiLiu,andWenwu
Zhu. Semanticconditioneddynamicmodulationfortemporalsentencegroundinginvideos. AdvancesinNeuralInformationProcessingSystems,32,2019. 2
[30] YitianYuan,TaoMei,andWenwuZhu. Tofindwhereyou
talk: Temporalsentencelocalizationinvideowithattention
basedlocationregression. InProceedingsoftheAAAIConferenceonArtificialIntelligence,pages9159–9166,2019. 2
[31] AohanZeng,XiaoLiu,ZhengxiaoDu,ZihanWang,Hanyu

### Lai,MingDing,ZhuoyiYang,YifanXu,WendiZheng,Xiao

Xia,etal. Glm-130b: Anopenbilingualpre-trainedmodel.
arXivpreprintarXiv:2210.02414,2022. 1
[32] Da Zhang, Xiyang Dai, Xin Wang, Yuan-Fang Wang, and

### LarrySDavis. Man:Momentalignmentnetworkfornatural

languagemomentretrievalviaiterativegraphadjustment.In
ProceedingsoftheIEEE/CVFConferenceonComputerVisionandPatternRecognition,pages1247–1257,2019. 2
[33] Hao Zhang, Aixin Sun, Wei Jing, and Joey Tianyi Zhou.
Span-basedlocalizingnetworkfornaturallanguagevideolocalization. arXivpreprintarXiv:2004.13931,2020. 2
[34] Hang Zhang, Xin Li, and Lidong Bing. Video-llama: An
instruction-tunedaudio-visuallanguagemodelforvideounderstanding. arXivpreprintarXiv:2306.02858,2023. 1,2,
3,7,8
[35] Renrui Zhang, Jiaming Han, Aojun Zhou, Xiangfei Hu,
ShilinYan,PanLu,HongshengLi,PengGao,andYuQiao.

### Llama-adapter: Efficient fine-tuning of language models

with zero-init attention. arXiv preprint arXiv:2303.16199,
2023. 8
[36] LuoweiZhou,YingboZhou,JasonJCorso,RichardSocher,
andCaimingXiong.End-to-enddensevideocaptioningwith
maskedtransformer. InProceedingsoftheIEEEconference
on computer vision and pattern recognition, pages 8739–
8748,2018. 2
[37] Deyao Zhu, Jun Chen, Xiaoqian Shen, Xiang Li, and Mohamed Elhoseiny. Minigpt-4: Enhancing vision-language
understandingwithadvancedlargelanguagemodels. arXiv
preprintarXiv:2304.10592,2023. 2
10

<!-- Page 11 -->


### A.MoreExamples

Weshowcaseadditionalexamplesofvideodialoguesacross

### What is happening in the video?

various tasks, encompassing a creative task (Figure 4), a
In the video, a man is standing in a yard and using an ax to cut a log. He
fine-grainedunderstandingtask(Figure5),andavideorea- is wearing a blue shirt and jeans and is holding the ax in his right hand.
soning task (Figure 6). In the creative task (Figure 4), our
Can you write a short poem inspired from the video?
VTimeLLMdemonstratesaremarkablecapacitytocompre-

### Sure, here's a short poem inspired by the video:

hendvisualinformationandsubsequentlycraftapoemin-

### A man in blue, a yard to clear,

spired by it. This achievement is attributed to we freeze An ax in hand, a log to rear.
the LLM at all three stages of training, thereby preserv- He swings with might, with each strike,
The log splits, a satisfying sight.
ing its ability for engaging in creative dialogue. In the
fine-grainedunderstandingtask(Figure5),ourVTimeLLM
comprehends multiple events within the video, as well as Figure4.CreativeTask.OurVTimeLLMcomprehendsthevisual
the specific visual content within individual events. This informationandcraftsapoeminspiredbyit.
demonstrationunderscoresitsproficiencyingraspingtemporalandspatialdetails,acapabilityattributedtoourthreestagetrainingstrategy. Inthevideoreasoningtask(Figure
6),ourVTimeLLMrespondstoseveralquestionsrequiring

### Can you describe the video in detail?

inference,showingitscapacitytoengageinreasoningbased
Sure, the video features a woman who is seen standing in a room, wearing a
onacomprehensiveunderstandingofvisualcontent. pair of ballet shoes. She then proceeds to perform a series of ballet moves,
showcasing her flexibility and grace. As the video progresses, the woman
transitions to a different setting, where she is seen performing the same ballet
moves in a different location. The background of the video is not specified, but
B.TemplatesandPrompts it is clear that the woman is performing in a professional setting. The video
ends with the woman finishing her performance and walking away, leaving the
viewer with a sense of admiration for her talent and dedication to ballet.
In Stage 2, we need to transform events {s ,e ,T } into What is the brand shown at the end of the video?
i i i
template-basedQA,wheres i ande i representthestartand The video ends with the brand UA (Under Armour) being shown.
end timestamps of a segment, ranging from 00 to 99. T
i
correspondstoitstextualdescription. Foragivensequence Figure 5. Fine-grained Understanding Task. Our VTimeLLM
ofevents,thereisa20%probabilityoftransformationinto comprehendsmultipleeventswithinthevideo,aswellasthespesingle-turn QA, completing a dense caption task where all cificvisualcontentwithinindividualevents.
events are described within a single answer. Conversely,
there is an 80% probability of transformation into MultiturnQA.Inthisscenario,eacheventisindividuallyqueried
and answered within a dialogue, in the form of two tasks,
event captioning or temporal grounding. We provide 10
templatesforeachtask,asshowninBox3.
Explain why the video is funny.

### InStage3,weneedtotransformeventsintohigh-quality

dialogue. This is accomplished by providing a prompt to The video is funny because the bear is dancing and moving
around in a funny way. The bear's movements are
a text-based LLM(Vicuna-7B v1.5). The prompt can be exaggerated and comical, adding to the humor of the video.
found in Box 4. In the prompt, specific timestamps are

### Is this a real bear?

not provided because their inclusion does not enhance the
No, this is not a real bear. It is a costume worn by a person in the video.
LLM’s comprehension of temporal relationships. On the
contrary,theymayintroduceerrorsintothedialogue. Con-

### Figure 6. Video Reasoning Task. our VTimeLLM responds to

sequently, events are presented in a sequential order, acseveral questions requiring reasoning based on a comprehensive
companied by specific symbols e.g., <s1>, <e1>in the
understandingofvisualcontent.
box, denoting the timestamps. The generated dialogue is
expectedtointegratetemporalperceptionandreasoning.

### C.1.EvaluationofVTimeLLM

C.EvaluationProcess For VTimeLLM that has undergone only stages 1, 2 training without stage 3, the input and output formats remain
Inthissection,weprovideadetailedprocessontheevalu- entirelyconsistentwiththetemplate. Consequently,wecan
ationoftemporalgroundinganddensecaptioningtasksfor directlyemploythetemplatesinBox3asqueries. Specif-
VTimeLLMandotherVideoLLMs. ically, for the dense captioning task, we employ Q , i.e.,

## D1

1

<!-- Page 12 -->

“Couldyoupleasedetailtheeventsthattookplaceduring
different time segments in the video?” as the query. For
thetemporalgroundingtask,weemployqueriesQ ,Q ,

## T1 T2

and Q to compute IoU for their respective outputs, and

## T3

we report the average metrics. The performance obtained
fromdifferentqueriesissimilar.
VTimeLLMthathasundergonestage3trainingdemonstrate commendable instruction-following ability, and the
performancemayvarywithdifferentqueries. Forexample,
the inclusion of the phrase “in detail” in the query leads
to a more detailed description of the video. For the dense
captioningtask,weutilizethefollowingquery:“Couldyou
please describe the events in the video in detail? Be specificabouttheactivitiesofindividuals,theirsurroundings,
andinteractionswithothers. TheoutputshouldbeinJSON
format,structuredasfollows: {‘event’: ‘xx’,‘timestamps’:
‘fromxxtoxx’}.” WefindthatthisqueryoutperformsQ

## D1

acrossvariousmetricsbyapproximately10%. Forthetemporalgroundingtask,wecontinuetoreporttheaverageresultsofqueriesQ ,Q ,andQ ,withmetricsforeach

## T1 T2 T3

queryremainingconsistentlyclose. Notably,evenwiththe
adoption of a simpler query such as ‘When does T hapi
pen?”,weachievecomparableresults,underscoringthestabilityofoutputsinthistask.

### C.2.EvaluationofotherVideoLLMs


### For other Video LLMs (VideoLLaMA, VideoChat, and

VideoChatGPT) that we test in our study, we try our best
toassesstheiroptimalperformanceastheywerenottrained
on these tasks. Our testing methodology follows several
principles: First,weincludevideodurationDinthequery.

### Second,asthesemodelsoftenfailtoadheretoourprompt

for outputting in JSON format, we apply multiple regular
expressions to format the output. This successfully handles over 70% of the outputs. For these outputs cannot be
processed, we exclude the corresponding data from metric
calculations. Third, we design multiple queries and select
theoneyieldingthebestperformanceasthefinalresult.For
example,inourexperiment,wefindthatthebestqueryfor
VideoChatGPTinthedensecaptioningcaskis:“Thisvideo
hasadurationofD seconds. Fromwhichsecondtowhich
secondinthevideo,whateventhappens? Bespecificabout
the activities of individuals, their surroundings, and interactionswithothers. Listtheeventsintheformat: 1. From
x1secondtoy1second: event1. \n 2. Fromx2secondto
y2second: event2.\n ...”
2

<!-- Page 13 -->

Box3: Templatestotransformevents{s ,e ,T }intoQAdialogues,10templatesforeachtask.
i i i

### DenseCaptioning(taskofSingle-turnQA):

Q : Couldyoupleasedetailtheeventsthattookplaceduringdifferenttimesegmentsinthevideo?

## D1

Q : I’mcuriousaboutwhathappenedatdifferentpointsinthevideo. Couldyoupleasedescribetheevents?

## D2

Q : Couldyouprovideasummaryoftheincidentsthatoccurredatvarioustimestampsinthevideo?

## D3

Q : I’d like to know what events transpired during specific time intervals in the video. Could you please

## D4

elaborate?
Q : Canyougivemeabreakdownoftheoccurrencesatdifferenttimestampsinthevideo?

## D5

Q : I’minterestedinunderstandingtheeventsthatunfoldedatdifferentpointsinthevideo. Couldyouplease

## D6

specify?
Q : Couldyououtlinetheincidentsthathappenedduringdifferenttimeperiodsinthevideo?

## D7

Q : I’m trying to grasp the sequence of events in the video. Could you please outline what happened at

## D8

differenttimes?
Q : Canyougothroughthevideoanddescribewhattookplaceatdifferenttimeintervals?

## D9

Q :I’dappreciateitifyoucouldprovideadetailedaccountoftheeventsthatoccurredatdifferenttimestamps

## D10

inthevideo.
A : T ,froms toe . T ,froms toe . T ,froms toe ......

### D 1 1 1 2 2 2 3 3 3


### EventCaptioning(OnetaskinMulti-turnQA):

Q : Canyoudescribewhatoccurredfroms toe inthevideo?

### E1 i i

Q : Couldyoutellmewhathappenedfroms toe inthevideo?

### E2 i i

Q : Whattranspiredfroms toe inthevideo?

### E3 i i

Q : Describewhattookplacefroms toe inthevideo.

### E4 i i

Q : Tellmeabouttheeventsfroms toe inthevideo.

### E5 i i

Q : Whatwasgoingonfroms toe inthevideo?

### E6 i i

Q : Pleaserecountwhatoccurredfroms toe inthevideo.

### E7 i i

Q : Explainwhathappenedfroms toe inthevideo.

### E8 i i

Q : Providedetailsabouttheeventsfroms toe inthevideo.

### E9 i i

Q : Sharewhattranspiredfroms toe inthevideo.
E10 i i

## A : T .


### E i


### TemporalGrounding(OnetaskinMulti-turnQA):

Q : DuringwhichframescanweseeT happeninginthevideo?

### T1 i

Q : BetweenwhichframesisT visibleinthevideo?

### T2 i

Q : AtwhatpointinthevideocanweobserveT takingplace?

### T3 i

Q : BetweenwhichtwoframescanwewitnessT occurringinthevideo?

### T4 i

Q : DuringwhichframesinthevideocanweobserveT happening?

### T5 i

Q : AtwhichtimeintervalinthevideocanweseeT occurring?

### T6 i

Q : BetweenwhichframescanwefindT takingplaceinthevideo?

### T7 i

Q : AtwhatpointinthevideocanwewitnessT happening?

### T8 i

Q : BetweenwhichtwoframesinthevideocanweobserveT takingplace?

### T9 i

Q : DuringwhichframesdoesT occurinthevideo?

### T10 i

A : Froms toe .
T i i
3

<!-- Page 14 -->

Box4: PromptforLLMinStage3,designedtotransformaseriesofeventsintohigh-qualitydialogue.
YouareanAIvisualassistantwiththetaskofanalyzingasinglevideo.
Craft a conversation between yourself and a user discussing the video’s content. Develop responses that
embody the persona of an active visual AI assistant, capable of observing the video and providing insightful
answers. Include inquiries about temporal perception and reasoning, like events preceding or succeeding
specificoccurrences,orrequestingtimestampsforparticularactionsorevents.
Ensure that the questions can be definitively answered based on the observable video content or confidently
ascertainable absence from the video. Utilize the timestamps <s?>and <t?>to create contextual questions
consideringthetemporalrelationshipsbetweenevents. Theconversationsshouldbeconcise.
Here’sanillustrativeexample:
===examplestart===

### Events:

from<s1>to<e1>: Amanandwomanplayrockpaperscissors,thewomanwinsandsmiles.
from<s2>to<e2>: Thewomanputsablindfoldon.
from<s3>to<e3>: Thewomancontinuesplayingrock-paper-scissorswiththemanandwinsagain.
from<s4>to<e4>: Thewomangivesthemanahug.

### Dialogue:


### User: Couldyouprovideabriefoverviewofthevideo’scontent?

Assistant: Certainly! In the video, a man and a woman engage in a game of rock-paper-scissors. The woman
emerges victorious and shares a smile. Subsequently, she places a blindfold on. She then proceeds to win
anotherroundofrock-paper-scissorsagainsttheman. Thevideoconcludeswiththewomanembracingtheman
warmly.
User: Canyoupinpointwhenthewomanachievedvictoryinthegametwice?
Assistant: Certainly. The first victory occurs from <s1>to <e1>, while the second triumph takes place from
<s3>to<e3>.
User: I’mcuriousabouttheinteractionbetween<s4>and<t4>. Couldyouelaborate?
Assistant: Absolutely. During the interval from <s4>to <t4>, the woman conveys her emotions through a
heartfeltembrace,demonstratinghergenuineaffectionfortheman.
User: Whatmightbetheunderlyingreasonforthewoman’saffectionatehug?
Assistant: Thewoman’saffectionatehuglikelystemsfromherdesiretouplifttheman’sspiritsafterhislossin
therock-paper-scissorsgame.
===exampleend===

### Events:

from<s1>to<e1>: T .
1
from<s2>to<e2>: T .
2
from<s3>to<e3>: T .
3
......
Dialogue:
4

## Tables

**Table (Page 7):**

| Model | TemporalGrounding |  | DenseCaptioning |
|---|---|---|---|
|  | ActivityNet R@0.3 R@0.5 R@0.7 mIoU | Charades-STA R@0.3 R@0.5 R@0.7 mIoU | ActivityNet SODA c CIDEr METEOR |
| VideoChat-7B[15] VideoLLaMA-7B[34] VideoChatGPT-7B[20] | 8.8 3.7 1.5 7.2 6.9 2.1 0.8 6.5 26.4 13.6 6.1 18.9 | 9.0 3.3 1.3 6.5 10.4 3.8 0.9 7.1 20.0 7.7 1.7 13.7 | 0.9 2.2 0.9 1.9 5.8 1.9 1.9 5.8 2.1 |
| VTimeLLM-7B VTimeLLM-13B | 44.0 27.8 14.3 30.4 44.8 29.5 14.2 31.4 | 51.0 27.5 11.4 31.2 55.3 34.3 14.7 34.6 | 5.8 27.6 6.8 5.9 27.2 6.7 |


**Table (Page 7):**

| Row | Stage1 | Stage2 | Stage3 | TemporalGrounding |  | DenseCaptioning |
|---|---|---|---|---|---|---|
|  |  |  |  | ActivityNet R@0.3 R@0.5 R@0.7 mIoU | Charades-STA R@0.3 R@0.5 R@0.7 mIoU | ActivityNet SODA c CIDEr METEOR |
| 1 | I | Freeze | ✗ | 36.1 21.4 10.5 25.5 35.6 21.4 10.2 24.8 33.5 17.9 8.1 23.9 34.8 18.2 8.5 24.4 31.3 16.5 6.8 22.2 33.5 17.4 6.9 23.2 42.2 22.7 11.5 29.8 31.0 18.1 7.7 22.9 39.3 26.6 13.0 28.1 44.0 27.8 14.3 30.4 | 48.4 23.7 11.5 32.2 48.0 24.4 12.1 31.6 46.6 17.7 6.7 30.5 47.9 19.9 8.0 31.4 47.5 21.9 9.2 30.6 47.1 21.4 8.6 30.6 40.0 4.9 0.0 27.5 37.5 21.8 6.1 22.8 49.7 29.8 13.3 30.9 51.0 27.5 11.4 31.2 | 4.6 17.0 5.4 4.6 17.0 5.5 4.0 14.1 5.0 4.2 14.1 5.2 4.1 13.4 5.0 4.0 13.6 4.8 3.7 10.2 5.0 4.2 16.0 5.0 5.2 23.2 6.1 5.8 27.6 6.8 |
| 2 |  | Tune |  |  |  |  |
| 3 | V | Freeze | ✗ |  |  |  |
| 4 |  | Tune |  |  |  |  |
| 5 | I+V | Freeze | ✗ |  |  |  |
| 6 |  | Tune |  |  |  |  |
| 7 | ✗ | Tune | ✗ |  |  |  |
| 8 | I | ✗ | Addition |  |  |  |
| 9 | I | Freeze | Reuse |  |  |  |
| 10 | I | Freeze | Addition |  |  |  |


**Table (Page 8):**

| EvaluationAspect | VideoLLaMA | LLaMA-Adapter | VideoChat | VideoChatGPT | BT-Adapter | VTimeLLM |
|---|---|---|---|---|---|---|
| TemporalUnderstanding CorrectnessofInformation DetailOrientation ContextualUnderstanding Consistency Mean | 1.82 1.96 2.18 2.16 1.79 1.98 | 1.98 2.03 2.32 2.30 2.15 2.16 | 1.94 2.23 2.50 2.53 2.24 2.29 | 1.98 2.40 2.52 2.62 2.37 2.38 | 2.34 2.68 2.69 3.27 2.46 2.69 | 2.49 2.78 3.10 3.40 2.47 2.85 |
