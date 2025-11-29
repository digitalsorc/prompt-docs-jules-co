---
title: "Context PEFT Multi Modal"
original_file: "./Context_PEFT_Multi_Modal.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["llm", "chain-of-thought", "fine-tuning", "evaluation", "multimodal"]
keywords: ["context", "peft", "tuning", "attention", "fine", "training", "models", "model", "lora", "our"]
summary: "<!-- Page 1 -->

Context-PEFT: Efficient Multi-Modal, Multi-Task Fine-Tuning
AvelinaAsadaHadji-Kyriacou OgnjenArandjelovic

### UniversityofStAndrews UniversityofStAndrews

DepartmentofComputerScience DepartmentofComputerScience
lhk3@st-andrews.ac.uk oa73@st-andrews.ac.uk
Abstract ontheCOCOcaptioningtasks[20],demonstratingitssuperiorperformancecomparedtofullfine-tuningundersimilar
ThispaperintroducesanovelParameter-EfficientFine- data constraints, all while delivering a substantially more
Tuning"
related_documents: []
---

# Context PEFT Multi Modal

<!-- Page 1 -->

Context-PEFT: Efficient Multi-Modal, Multi-Task Fine-Tuning
AvelinaAsadaHadji-Kyriacou OgnjenArandjelovic

### UniversityofStAndrews UniversityofStAndrews

DepartmentofComputerScience DepartmentofComputerScience
lhk3@st-andrews.ac.uk oa73@st-andrews.ac.uk
Abstract ontheCOCOcaptioningtasks[20],demonstratingitssuperiorperformancecomparedtofullfine-tuningundersimilar
ThispaperintroducesanovelParameter-EfficientFine- data constraints, all while delivering a substantially more
Tuning (PEFT) framework for multi-modal, multi-task parameter-efficient and computationally economical solutransferlearningwithpre-trainedlanguagemodels. PEFT tion.
techniquessuchasLoRA,BitFitandIA3havedemonstrated We experiment with LoRA, BitFit and IA3 as adaptor
comparable performance to full fine-tuning of pre-trained methodsforContext-PEFTandexaminehowtheyperform
modelsforspecificdownstreamtasks,allwhiledemanding compared to full fine-tuning, no fine-tuning, as well as
significantlyfewertrainableparametersandreducedGPU vanillacontext-agnosticPEFT.
memory consumption. However, in the context of multimodalfine-tuning, theneedfor architecturalmodifications

## PreviousWork

orfullfine-tuningoftenbecomesapparent. Toaddressthis
weproposeContext-PEFT,whichlearnsdifferentgroupsof 2.1.Parameter-EfficientFine-Tuning
adaptorparametersbasedonthetoken’sdomain. Thisapproach enables LoRA-like weight injection without requir- Large Language Models (LLMs) have been increasing in
ing additional architectural changes. Our method is eval- scaleoverrecentyears, withpopular‘baseline’modelsinuated on the COCO captioning task, where it outperforms creasinginsizefrom350millionparametersin2018(BERT
fullfine-tuningundersimilardataconstraintswhilesimul- Large [10]) to 7 billion parameters in 2023 (Llama 2 7B
taneouslyofferingasubstantiallymoreparameter-efficient [35]). Withthisincreaseinscaletherehasbeenanincrease
andcomputationallyeconomicalsolution. in popularity of PEFT techniques which have enabled the
fine-tuning of large models using less compute and fewer
resources. PEFT methods can be categorised by the ways

## Introduction they modify the underlying model architecture, which parameters are trainable and where new weights are intro-

Recent advancements in Parameter-Efficient Fine-Tuning duced.
(PEFT), exemplified by techniques such as LoRA, BitFit,
and IA3 [16, 21, 40], have demonstrated their ability to
deliver performance on par with full fine-tuning of pre- AdaptorModules MLPAdaptors[15,29]comeinmultitrained models for specific downstream tasks, all while plevariationsbutallsharethesamecoreideaofintroducing
significantly reducing the number of trainable parameters asmallresidualfully-connectednetworkaftersub-layersin
and GPU memory consumption. However, in the realm the transformer backbone. These adaptor layers are then
of multi-modal transfer-learning, there often arises a need trainedwhiletheoriginaltransformerlayersremainfrozen.
forarchitecturaladjustments–suchasMulti-ModalCausal

### Attention [39] – or full fine-tuning – as demonstrated by

LLaVA[23]. Soft Prompts Soft prompt techniques – such as Prefix-
In response to these challenges we introduce a novel Tuning[18,19]–introducelearnableembeddingsasapre-
PEFT framework, Context-PEFT, which learns different fixtotheinputsequence. Theseembeddingscanbetrained
groupsofadaptorparametersbasedonthetoken’sdomain as inputs to only the first layer and then propagated to all
orpurpose. Thisapproachnecessitatesnofurtherarchitec- layers like normal tokens, or learned for each transformer
tural modifications and is adaptable to various PEFT tech- sub-layer,replacingtheresultsofembeddingsofpriorlayniques. Weconductanextensiveevaluationofourmethod ersintheprefixregion.
1
3202
ceD
41
]GL.sc[
1v00980.2132:viXra

<!-- Page 2 -->

SelectiveTraining Selectivetraininginvolvesonlytrain- kensand(2)textattendingtovisualtokens. Theynamethis
ingasubsetofparameters. SuchtechniquesincludeBitFit augmentation the ‘Multi-Modal Causal Attention Mecha-
[40] which trains only the bias terms of projection layers nism (MMCA),’ with their intuition being that the attenandLN-Tuning[26]whichlearnonlythebiasandscalepa- tionweightsofthetwodifferentmodalitiesmayinterfereif
rametersofthelayernormalisationlayers. jointly normalised. Alternatively, LLaVa [23] takes a two
stage approach. Firstly the LLM and vision-encoder are
AdditiveMethods Additivemethodsinvolveintroducing frozenwhiletheimageprojectionweightsaretrainedona
learnable vectors that are applied point-wise to the activa- largeimagecaptioncorpus. NexttheLLMisunfrozenand
tionsintransformersublayers. IA3[21]appliesanelement- isjointlyfine-tunedwiththeimageprojectionsonasmaller
wise multiplication of learnable vectors to the queries and languageandvisionmulti-turnconversationaldataset.
keys in attention layers as well as the intermediate activa- Both approaches have their own merits and their own
tionsofthefeed-forwardlayers. drawbacks.TheMMCAapproachonlytrainsasmallsubset
of weights, but increases the compute requirements comparedtovanillaattentionusingacceleratedkernelssuchas

### Reparameterization Methods Another method to re-

FlashAttention [8]; as of writing, FlashAttention does not
duce the number of trainable parameters is by augmenting
supportexplicitmasks,whichmeanstheattentionmatrices
theoriginalpre-trainedweightsusinglow-rankrepresentafor both modalities cannot be jointly computed using this
tions. One popular method is LoRA [16] which computes
acceleration structure and must instead fall back to either
delta weights for the pre-trained projection matrices using
non-acceleratedattention(whichusesmoreGPUmemory)
low-rank matrix decompositions, δW = AB. Originally,
ormultipleroundsofFlashAttention(whichincreasestrain-
LoRA was proposed for the key, query, value and output
ingandinferencelatency). SinceLLaVausesvanillacausal
projectionsofattentionlayers,butthetechniquecanalsobe
attention it can take advantage of FlashAttention, but reappliedtotheFFNlayers.
quires full fine-tuning of the LLM in the second stage of

### Vision-LanguageModels training.


### Vision-Languagemodelscanoftenbeclassifiedundertwo

categories: dual-encoder models which are more suited to 3.OurApproach
classification and retrieval tasks [13, 17, 28, 33, 41], and
vision-encodertext-decodermodelswhicharemoresuited WeformasimilarapproachtothatofLLaVa[23],optingto
to generative tasks such as captioning and VQA. Vision- fullyfreezethevision-encoderandlearnalinearprojection
encoder text-decoder models – often refered to as Large toadaptimageembeddingsasinputstothelanguagemodel.
Vision Language Models (LVLMs) – can further be split Ourmethod,however,differsinthatwereplacethefullfineinto two categories based on their attention styles: causal- tuning of the LLM with Context-PEFT and choose not to
attentiononlymodelswhichincorporateimageembeddings pre-trainthelinearprojectiononanauxiliaryimage-caption
into the input context as projected tokens [2, 23, 39], and corpus as we want to train and evaluate our models on a
cross-attentionaugmentedmodelswhichaddadditionalat- standarddatasetwithoutanyauxiliarytrainingdata.
tentionlayerstoincorporatevisualinformation[1].
AmongLVLMs,thecausal-onlystylemodelshavesome 3.1.ModelSelection
advantages over cross-attention style models when aug-

### Thefocusofthispaperisefficiency,andwiththatinmind

mentingpre-trainedtext-onlymodelstoacceptothermodalwe have selected small and efficient models for this reities. Cross-attention style LVLMs introduce a significant
search.
number of extra parameters which need to be trained, increasing both training compute requirement and inference For the LLM we wanted to use a Llama 2 style model
latency. Caremustalsobetakenwhenusingcross-attention withasimilarsizetoGPT-2small[27,35]. Howeverwith
formulti-turninterleavedtextandimageinputtoensureim- Llama models starting at 7 billion parameters we opted to
ages are correctly localised to the corresponding text seg- trainourownmodelinhouseon5billiontokensfromThe
ments. Pile text corpus [12]. Details of the LLM are described in
For causal LVLMs there are a multiple methods for supplementarymaterialSection7.
adapting pre-trained text-only LLMs to accept visual in- For the vision-encoder we opted to utilise the Swin
puts. DeepSpeed-VisualChat[39]optstocompletelyfreeze Transformer V2 family of models due to their efficiency
theLLMandvision-encoder,trainingonlythetextembed- and size of produced embeddings [25]; for images of size
dingsandimageprojectionlayer. Additionally,theauthors 256×256theSwinfamilyproduce64embeddings. Details
augmenttheattentionmechanismsuchthattwoseparateat- of the chosen Swin models are detailed in supplementary
tention matrices are used for (1) text attending to text to- materialSection6.
2

<!-- Page 3 -->

Figure2. Theoverallmodelstructureshowingtrainableadaptors
usedfordifferenttokentypesinthefrozenlanguagemodel.
Figure1. Imageandtextinputstructure. Apre-trainedvisionen- injected adaptor parameters. The overall structure of the
coderproducesimageembeddingswhichareprojectedthrougha
modelisshowninFigure2.
linearlayerandconcatenatedwithtextembeddingsofthecorre-
Our choice of adaptor methods was motivated by their
spondingcaption.
fine-tuningperformanceasreportedintheiroriginalpapers,
ability to augment into context-specific forms, and ability
to integrate into existing models with minimal modifica-

### ImageInputs

tion. Althoughweoptedtomodifythecodeofourin-house
After passing the images through the vision-encoder the modeltofacilitateeasierdebuggingofadaptorsduringdeembeddings are projected to the LLM embedding dimen- velopment, all adaptor methods can be incorporated into a
sionandaddedtothetokensequence. Thesequenceiscon- PyTorchmodelusingforwardhookswithoutmodifyingany
structed such that it begins with a [BOS] token, followed oftheoriginalcode.
by the 64 projected image embeddings, and up to 63 captiontokenswhicharepost-paddedbyan[EOS]tokenand

### Context-LoRA Weformulateamemoryefficientwayof

[PAD]tokenstoachieveafixedcontextlengthof128. Alcomputingcontext-specificLoRAsuchthatthedeltaweight
most all COCO captions fit into this 63 token budget with
matrixisneverfullymaterialised. Toadaptanyprojection,
only a tiny faction of captions exceeding this length (and

### W,forcontextLoRAwithlowrankmatricesAandB the

thusaretruncated). ThisisillustratedinFigure1.
followingalgorithmisused:

### Context-PEFT


### Algorithm1MemoryefficientContext-LoRAalgorithm

Our motivation behind Context-PEFT is inspired by Mi- x←states
crosoft’s introduction of MMCA; by decomposing the at- s←OneHot(contextNum)
tentionmechanismintotwomode-specificsubmechanisms δh←Einsum(‘...ld,cdr,crD,...lc→...lD’,x,A,B,s)
theychangethewayinwhichthetextandimagemodalities h←Wx+δh
interactandthusaggregateinformation. Thisisfurtherex-
Thelettersintheeinsumcorrespondtodifferentinputandoutput
emplifiedbythefactthattheauthorsfoundtheadditionof
dimensions. l corresponds to the sequence length dimension, d
LoRAtohaveminimaleffectsontheresults[39],whichfur- and D are the input and output dimensions of the projection, r
therhighlightstheimportanceofcontrollinginter-modality istherankoftheAandB decompositionmatrices, andcisthe
interactions. Our approach is to instead directly modulate contextselectordimension.
theweightsappliedtotokensofdifferentmodalitieswhich

### We apply context-LoRA to the query, key, value, and

we hypothesise would yield similar results to MMCA by
output projections in the attention layers as well as the up
modifying the embeddings passed to the attention mechanddownprojectionsinthefeed-forwardlayers.
anism rather than altering the mechanism itself. Our approachalsohassimilaritiestoMixture-of-Expertsmethods
whichhavebeenshowntogreatlyimproveperformanceof Context-BitFit Traditionally, BitFit fine-tuning is permulti-domaintaskssuchasany-to-anymachinetranslation formed by training only the bias terms; however this does
[14,32]. noteasilyfacilitateper-tokenbiasterms. Tocombatthiswe
Eachtokeninthesequencehasacorresponding‘context reparameterizeBitFittrainingbyaddingasecondarytrainnumber’identifierwhichdesignateswhichadaptorweights ablebiastermthatdependsonthetoken’scontextnumber.
should be used at each position of the sequence. When WeapplyBitFittoallprojectionsinalllayersofthetransperforming vanilla context-agnostic PEFT experiments we formerbackbone.
simply set all tokens to use the same context number. For
all PEFT variants, context-specific and context-agnostic, Context-IA3 Our application of Context-IA3 is almost
we freeze all original model parameters and train only the identical to Context-BitFit, with the main difference being
3

<!-- Page 4 -->


### Adaptor A F AF

IA3 13.01 12.75 (-0.25) 12.74 12.51 (-0.24) 12.13 12.0 (-0.13)
BitFit 12.97 12.51 (-0.46) 11.93 11.70 (-0.22) 11.61 11.27 (-0.34)
LoRA1 11.04 10.54 (-0.50) 10.25 9.83 (-0.41) 9.91 9.49 (-0.41)

### LoRA8 9.50 9.09 (-0.41) 8.72 8.44 (-0.28) 8.38 8.15 (-0.22)

LoRA64 8.24 7.92 (-0.32) 7.75 7.69 (-0.06) 7.57 7.46 (-0.11)

### Table1. Validationperplexityafter8epochsusingthetinySwin

variant. ‘A’ and ‘F’ in the column name represent attention
andfeed-forwardadaptationrespectively. Context-agnosticPPL,
context-specificPPL,anddifferenceinPPLarerepresentedbythe
left,centerandrightvaluesineachcolumnrespectively.
the performance of various PEFT methods when applying
adaptation to both attention and FFN layers, and to either
Figure3. Validationperplexityafter8epochsusingthetinySwin theattentionorFFNlayers.Ourcomparisonsareconducted
variant. ‘A’and‘F’intherunnamerepresentattentionandfeed- usingthe‘tiny’versionoftheSwintransformer,wherewe
forwardadaptationrespectively,withthenumberrepresentingthe analyze validation perplexity across both context-specific
LoRArank.Thevaluesabovethebarsrepresenttheimprovement and context-agnostic versions of the three PEFT methods
inPPLforthecontext-specificvariant.
andwhilealsovaryingtherankoftheLoRAadaptors.
From the results summarised in Figure 3 we consiselement-wise multiplication of the projected states rather tentlyfindthecontext-specificadaptorsoutperformingtheir
than addition. We apply IA3 to the key, value and inter- context-agnostic variant across all configurations, with the
mediate FFN activations, as described by the original au- attentionandfeed-forwardadaptorconfigurationsperformthors[21]. ing best among each technique, and LoRA with a rank of
64performingbestoverall.

## Evaluation


### Whenapplyingfine-tuningtoasubsetoflayers(the‘A’

and ‘F’ columns of Table 1) we discover that adapting the

### For most experiments we use caption perplexity (PPL) on

feed-forward layers generally yields lower perplexity than
thevalidationortestsetsasabenchmarkofmodelperforadaptingonlytheattentionlayers. Howeverweobservethe
mance. Whenreportingresultswetheuseweightsfromthe
largestgainsinperplexityforcontext-PEFTintheattentionepochwithbestvalidationloss.
only configurations compared to the context-agnostic vari-

### Training ants which suggests that attention layers benefit the most

from context-specific adaption, further validating our hy-

### Across all experiments we train using a batch size of 96

pothesis of the importance of modality specific attention
for eight epochs over the COCO dataset unless otherwise
routing,butunlikeDeepSpeed-VisualChat[39],weareable
stated. We use the Adam optimizer with a fixed learntoachievethisthroughcontext-PEFTalone.
ing rate of 1e−4 and beta values of (0.9,0.95). We apply
a dropout of 0.1 before the image projection layer, and a
residual dropout after attention and feed-forward layers in
the language model. We also apply flip, crop and colour
augmentations to the images during training. For the loss
functionweusetypicallanguagemodellinglossappliedto
thelast64tokensofthesequence. Eachexperimentisconducted on a single RTX A4500 GPU and we make use of
mixed precision training. We only use the training split of
theCOCOdatasettofine-tuneourmodels,makingnouseof
additionaltrainingdata;thisistoensurerepeatabilityandto
explore the efficacy of context-PEFT in a data-constrained
environment.

### Figure4.Testperplexityafter8epochsusingthetinySwinvariant,


### AdaptingAttentionandFeed-ForwardLayers varyingLoRArankfrom1to384intheattentionandfeed-forward

adaptorconfiguration.

### To gain an understanding of how context-PEFT affects

different parts of the transformer backbone we evaluate
4

<!-- Page 5 -->

Adaptor Context-Agnostic Context-Specific

## Ia3 55,296 110,592

BitFit 119,808 239,616

### LoRA-1 202,752 405,504


### LoRA-8 1,622,016 3,244,032

LoRA-64 12,976,128 25,952,256

### FullFT 153,196,032


### Table3.ThenumberoftrainableparametersintheLLMbackbone

for different adaptor variants in the attention and feed-forward
configuration.
‘AF’configuration,withourresultssummarisedinFigure5
andTable2.
Figure5. Testperplexityofdifferentfine-tuningmethodsafter8
epochsforbothvisionencodersizes.
Foreachadaptorvariantitcanbeseenthatthelargevisionencoderwithcontext-specificadaptationperformsbest,

### Adaptor Tiny Large

followedbythelargevisionencoderwithcontext-agnostic

## Ia3 12.46 12.18 11.52 11.32

adaption, both of which still perform better than the tiny

### BitFit 11.83 11.56 11.04 10.90

LoRA1 10.23 9.61 9.38 8.82 vision encoder with context-specific adaptation. This is
LoRA8 8.48 8.22 7.76 7.53 not surprising at all considering the large version of the
LoRA64 7.61 7.48 7.00 6.93 Swinmodelhas7timesasmoreparameters(195,202,932)

### None 14.88 13.71

thanthetinyversion(27,578,154),whichisasignificantly

### FullFT 7.70 7.18

larger increase in parameters than for context-specific vs

### FullFT(24epochs) 6.83

context-agnostic adaption as shown in Table 3. This im-
Table 2. Test perplexity of different fine-tuning methods after 8 pliesthathigherqualityimagetokenembeddingsaremore
epochs for both vision encoder sizes. The left and right values important for image understanding in our models than the
correspondtocontext-agnosticandcontext-specificresultsrespec- introduction of context-specific adaptation which only has
tively.
twice as many trainable parameters than context-agnostic
adaptation;despitethiswecanstillseethatcontext-specific
adaptationcanfurtherlowerperplexitywhichisespecially

### VaryingLoRARank

evidentinthelowerrankLoRAadaptors.
Usingtheattentionandfeed-forwardconfigurationwiththe
EventhoughtheLargeswintransformeroutperformsthe
‘tiny’SwinmodelwesweeptheLoRArankfrom1to384

### Tinyswintransformerforeachadaptorconfigurationiniso-

(half of d ) to evaluate how rank affects performance
model
lation, we can see that Context-LoRA-64 with Swin-Tiny
forbothcontext-specificandcontext-agnosticvariants.
outperformsalllowerrankLoRAvariantswithSwin-Large;

### FromtheresultsshowninFigure4itcanbeseenthattest

so even though Context-LoRA-64 has the most trainable
perplexitydecreasesasrankincreases. Howeverastherank
parameters, a full vision-text pipeline utilising Swin-Tiny
approaches 64 the perplexity plateaus and then sharply in-
+ Context-LoRA-64 has fewer total parameters and lower
creasesafterarankof256,implyinganoptimalrankvalue
perplexity than Context-LoRA-8 + Swin-Large. This has
between 64 and 128 for both context-specific and contextimportantimplicationsforscenarioswheremodelsizemay
agnostic variants in our LLM. This suggests that the lowbe more important than model performance, for example
ranknatureofLoRAhasabeneficialregularisingeffectin
when performing inference on embedded systems with redata-constrained environments, such as our fine-tuning on
source limitations preventing the use of a larger vision enthe COCO dataset. This may also explain why full finecoder.
tuningunderperformsbothinourexperimentsandsomeexperimentscarriedoutintheoriginalLoRApaper[16].
We can also see that LoRA with a rank of 64 outperformsfullfine-tuningfortherespectivevisiontransformer

### EffectofVisionTransformerSize

sizes when given the same data budget of 8 epochs, both
Weevaluatehowvisionencodersizeaffectstestperplexity withandwithoutcontext-specificadaptation. Wedoanadbycomparingthe‘tiny’and‘large’Swinmodelsforarange ditionalrunandfindittakes24epochsoffullfine-tuningto
of adaptors. We compare their performance for both the outperformcontext-LoRAwiththelargeSwinmodelasthe
context-specificandcontext-agnosticadaptorvariantsinthe visionencoder.
5

<!-- Page 6 -->


### AttentionMapObservations gain an understanding of the importance of different parts

oftheimagefordifferentpartsofthecaption. Morespecif-
The vision transformers we used were pre-trained for imically, we take the attention weight matrix for layer n and
age classification on ImageNet-1k (with the large version
slice the resulting matrix such that we only keep columns
trained on ImageNet-22k before finetuned for ImageNetcorrespondingtotheimagetokensandrowscorresponding
1k),meaningitmaybereasonabletoassumethecaptioning
tothedesiredspanofcaptiontokens.Finallywesumacross
abilitiesofourmodelscomepurelyfromtheimageclassithequeryandheaddimensionandreshapetheresultingvecfication abilities of the vision-encoder, rather than the lantor into an 8×8 matrix which we upscale and overlay on
guage model’s ability to extract and reason with the infortheoriginalimageusingacolourgradient.
mationintheimagetokensthemselves. However,weshow

### From examples given in Figure 6 and supplementary

thisisnotthecasebyanalysingtheattentionweightsofour
Section 8 we observe that the text tokens place attention
trainedmodels.
on specificregions ofthe imageswhich haveclear seman-
To collect these attention heatmaps we take imageticrelevancewithsurprisinglyfinegranularity;forexample,
captionpairsfromthetheCOCOtestset,forwardpassthem
weobserve thatthemodel isableto tellthedifference bethrough our trained Context-LoRA-64-AF model and obtween a bicycle and the person riding on it, as shown in
serve the attention weights for spans of caption tokens to

### Figures6aand6b. Thisshowsthat–eventhoughwetrain

onimagesegmentationdata–themodelcouldgeneraliseto
performpanopticsegmentationbylearninglinearclassifiers
ontheattentionmaps.
We also notice that the first and last image tokens (topleftandbottom-rightimagepatches)occasionallyhaveunusually high attention weights. The large top-left weighting may be explained through the attention sinking phenomenon[37],whilethebottom-rightweightingcanbeexplainedbythefactthatthelastimagetokenisalsothelocationthatproducesthefirsttext-tokeninauto-regressivetext
generation. We hypothesise that both phenomena would
disappear if we wrapped the image embeddings between
additional‘beginning’and‘end’tokenswhichmayfurther
leadtoperformanceimprovementsthroughmoresalientattentionbehavior.
(a) (b) 5.Discussion

### ApplicationsandLimitations

The primary application for Context-PEFT is in compute
anddata-constrainedenvironments;forexamplewhenthere
is a low volume of training data, when there are GPU
memory restrictions necessitating the use of smaller models and/or fewer trainable parameters, when there is lim-
(c) (d) ited training time which may prevent full fine-tuning from
convergingtoagoodminima,orwhenmodelsmustbedeployedforinferenceonlow-resourcehardwaresuchasconsumer grade workstations, mobile devices and embedded
systems.
However,iftheaforementionedconstraintsarenotaconcern,itisunlikelyContext-PEFTwilloutperformfullfinetuning. This is likely due to the fact that the embedding
spacesofSOTAlanguagemodelsareoftenwideenoughto
(e) (f) representmultiplemodalitieswithouttheneedforcontextspecificweightswhentrainedtoconvergenceonalargevol-
Figure6. Heatmapvisualisationsdepictingimagetokenattention ume of training data, as shown by Qwen-VL and LLaVa
weightsforspansofcaptiontokens. [2,23].
6

<!-- Page 7 -->


### FutureWork provesthealignmentoftheimageprojectorwhichmayhave

similareffecttousinganimprovedvisionencoder. CC3M
There are numerous improvements that can be integrated
and LAION-COCO are two such corpora which are well
fromconcurrentandpreviousworkstofurtherpushthepersuitedtopre-trainingtheimage-projector.
formanceofContext-PEFTasafine-tuningmethod. These
methods and some novel suggestions for future work are
summarizedbelow: ImprovedImageProjection ReplacingthelinearprojectorwithanMLPhasalsobeenshowntoimprovealignment
quality, asexploredinLLaVa-1.5[22]. Itisalsoworthin-

### Exploring More PEFT Techniques Further exploration

vestigating the addition of learnt absolute position embedofPEFTtechniquesmayalsoyieldgreaterfine-tuningperdingsaftertheimageprojectionasthesomevisionencoder
formance at potentially lower budgets. One such example
architectures, such as CNNs, do not produce embeddings
wouldbeinvestigatinghowcontext-specificscalingandoffwhichcontainpositionalinformation.
set parameters affect the performance of LN-tuning. Another avenue worth exploring is combining PEFT techniques,suchascombiningLoRAandBitFittonotonlyper- Improved Base Language Model It is well known that
formlowrankupdatesoflinearlayersbutalsoupdatetheir largerlanguagemodelshaveimprovedzero-shotgenerative
correspondingbiasterms. capabilities over smaller language models [3], so an obvious choice for future work is to apply our framework to a
Improved Vision Encoder From our evaluation in Sec- largerbaselanguagemodelasthisshouldalsoleadtohigher
tion4.4wehaveshownthatthequalityofinputembeddings qualitycaptiongeneration.
for other modalities can greatly affect the performance of
the fine-tuned language model. There are many vision en-
Exploring Hyperparameters Optimal hyperparameter
coderalternatives:
choice can often improve the quality of a model without
• CLIP-ViT [28], which was trained specifically to conchanging the model architecture or training objective itnectvisionandtextualcontentinadditiontoproducinga
self. Itisthereforworthexploringtheimpactofoptimizer
largernumberofimageembeddingsthantheSwinTranschoice(exploringalternativesuchasAdamW,Sophia,Adformerfamily.
abelief,Lookahead,Sharpness-Aware-Minimization),opti-
• VQ-VAE[36],whichproducesagreaternumberofimage
mizerhyperparemeters,learningrateschedules,andtheimembeddings than ViT. Additionally, instead of using an
pactofdropoutwhenappliedtodifferentsubsetsoflayers
imageprojectortoalignthelatentspaceforthelanguage
andwithdifferentdrop-rates.
model,wecaninsteadtakeadvantageofthediscretenature of the latent space by learning a set of embeddings
thatmapfromtheVAE‘vocabulary’directlyintotheem- Pruning and Quantization Context-PEFT (and PEFT
beddingspaceofthelanguagemodel. techniques in general) are often lightweight for both train-
• VQ-GAN[11],whichhasthesamebenefitsasVQ-VAE ing and inference, but these techniques can further be
with the addition of producing latents which were also combined with weight quantization and pruning to furtrainedwithconditioningontextualfeatures,especiallyif therreducemodelfootprintwithminimaleffectonperfortheVQ-GAN/VQ-VAEwasfine-tunedforusewithlatent mance[5,9].
diffusionmodel[30].
• DETR[4]objectdetectionencoder,whichmayallowthe

### Training Objectives In our work we made use of only

languagemodeltolearnbettersemanticconnectionsbethe causal language modelling loss as our training objectweentexttokensandimagetokens.
tive, buttherearenumerousotherchoiceswhichmaylead
• Encoder Fine-Tuning as in Qwen-VL [2], where a preto a higher quality model. One example of a training obtrained Vision Transformer is used a starting point and
jective that may improve model quality is causal masked
thenfurtherfine-tunedwithaVisualQuestionAnswering
languagemodelling, whereaspanoftokensinthecaption
(VQA)objective.
arereplacedwithasingle[mask]tokenandthemodelis
• EncoderPEFT,similartoQwen-VL,itisworthexplortaskedwithpredictingthestringofmaskedtokens;thisobing the use of PEFT techniques like LoRA to fine-tune
jectivemayalsoconditionthemodelfordown-streamtasks
thevisionencoderwithoutperformingfullparameterupsuchasvisualquestionansweringduetoitssimilaritywith
dates.
thetrainingobjective. Anothertrainingobjectiveworthexploring would be online reinforcement learning where the
Improved Pre-Training As shown in the LLaVa pa- reward signal for generated sequences is given by CLIP
per [23], pre-training on a mass image-caption corpus im- alignmentscore[28].
7

<!-- Page 8 -->

Other Modalities We believe that Context-PEFT can be
extendedtomanyothermodalitiesandpotentiallyallowthe
fusion of several modalities into a unified model. Examples of a multi-modal tasks suitable for Context-PEFT includeprocessingaudioforspeechrecognition,andprocessingvideoforVideoQuestionAnswering.

### Boundary Tokens As shown in Section 4.5 there are

some unusual attention behaviours at the boundaries between different modalities. We hypothesize that it may be
possible to alleviate these phenomena by wrapping each
modality segment with special tokens, [section] and Figure7.ParalleltrainingforVQAwithContext-PEFT.
[/section]. The introduction of these section boundarytokensalsoopensupopportunitiesforauxiliarytraining
losses by treating the end of section token as a [CLS] to- ofadaptorparameterswhicharespecifictoeachtoken’sdoken[10],whichwouldfacilitatethelearningoflinearclas- main.
sificationheadsforawidervarietyofdownstreamtasks. Through extensive experimentation with the COCO
dataset and captioning task we validate the potential of
Context-PEFT, evaluating our framework for a variety of

### Prompt Injection Mitigation Prompt injection attacks

adaptor methods and fine-tuning configurations, and we
are typically mitigated through cleansing incoming messhow our method is very competitive with full fine-tuning
sagesandusingspecialformattingtopreventexploitssuch
fordata-constrainedandcompute-limitedenvironments.
as the model interpreting user inputs as system messages.

### Finally, we suggest a range of possible applications for

However,badactorsoftenstillfindwaystoovercomethese context-PEFT and provide a variety of future research diprotections and bypass the safety guardrails of publicly rections and potential improvements to further explore its
availableLLMs-as-a-service. WehypothesizethatContext- performanceandcapabilitiesbeyondouruse-caseofimage
PEFTcouldpotentiallybeusedtomitigatepromptinjection captioning.
byusingdifferentadaptorsforsystemmessages,userinputs
andgeneratedresponses,which–whencombinedwithre- References
inforcementlearningasistypicallyusedfor‘chat’models–
[1] Jean-Baptiste Alayrac, Jeff Donahue, Pauline Luc, Anmayconditionthemodeltocompletelyignoreanyattempts
toine Miech, Iain Barr, Yana Hasson, Karel Lenc, Arthur
toinjectharmfulpromptswithinuserinputsegments.

### Mensch, Katie Millican, Malcolm Reynolds, Roman Ring,


### Eliza Rutherford, Serkan Cabi, Tengda Han, Zhitao Gong,

ParallelTraining WealsobelievethatContext-PEFThas Sina Samangooei, Marianne Monteiro, Jacob Menick, Seuntappedpotentialforparalleltrainingondifferenttasksto bastian Borgeaud, Andrew Brock, Aida Nematzadeh, Sahand Sharifzadeh, Mikolaj Binkowski, Ricardo Barreira,
then assemble the learnt adaptors into a unified model for
Oriol Vinyals, Andrew Zisserman, and Karen Simonyan.
further fine-tuning on a combined task. One example use
Flamingo: a visual language model for few-shot learning,
case–illustratedinFigure7–istrainingonesetofcontext-
2022. 2

### PEFT adaptors for image captioning, training another set

[2] Jinze Bai, Shuai Bai, Shusheng Yang, Shijie Wang, Sinan
of context-PEFT adaptors for textual question answering

### Tan, Peng Wang, Junyang Lin, Chang Zhou, and Jingren

(wherequestionsandanswersrepresentdifferentcontexts),
Zhou. Qwen-vl: Aversatilevision-languagemodelforunandthenfine-tuningtheunifiedensembleofadaptorsfora derstanding,localization,textreading,andbeyond,2023. 2,
downstream Visual Question Answering task. Taking this 6,7
to the extreme, we could train context-PEFT on dozens of [3] TomB.Brown,BenjaminMann,NickRyder,MelanieSubtasksandmodalitiesinparallel,effectivelytreatingeachset biah, Jared Kaplan, Prafulla Dhariwal, Arvind Neelakanofadaptorsas‘plugins’whichcanbeintegratedintoasin- tan, Pranav Shyam, Girish Sastry, Amanda Askell, Sandgleunifiedmodel. hini Agarwal, Ariel Herbert-Voss, Gretchen Krueger, Tom

### Henighan,RewonChild,AdityaRamesh,DanielM.Ziegler,


### Conclusion JeffreyWu,ClemensWinter,ChristopherHesse,MarkChen,


### Eric Sigler, Mateusz Litwin, Scott Gray, Benjamin Chess,

Inthispaper,wehaveintroducedContext-PEFTasamulti- JackClark,ChristopherBerner,SamMcCandlish,AlecRadmodal,multi-taskfine-tuningframeworktoefficientlyadapt ford, IlyaSutskever, andDarioAmodei. Languagemodels
pre-trained language models to other modalities in a data- arefew-shotlearners,2020. 7
and parameter-efficient manor by learning multiple groups [4] NicolasCarion,FranciscoMassa,GabrielSynnaeve,Nicolas
8

<!-- Page 9 -->

Usunier,AlexanderKirillov,andSergeyZagoruyko.End-to- [16] Edward J. Hu, Yelong Shen, Phillip Wallis, Zeyuan Allenendobjectdetectionwithtransformers,2020. 7 Zhu,YuanzhiLi,SheanWang,LuWang,andWeizhuChen.
[5] Tianlong Chen, Jonathan Frankle, Shiyu Chang, Sijia Liu, Lora: Low-rankadaptationoflargelanguagemodels,2021.

### Yang Zhang, Zhangyang Wang, and Michael Carbin. The 1,2,5

lotterytickethypothesisforpre-trainedbertnetworks,2020. [17] ChaoJia,YinfeiYang,YeXia,Yi-TingChen,ZaranaParekh,
7 HieuPham,QuocV.Le,YunhsuanSung,ZhenLi,andTom
[6] Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Duerig.Scalingupvisualandvision-languagerepresentation
Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul learningwithnoisytextsupervision,2021. 2
Barham, Hyung Won Chung, Charles Sutton, Sebas- [18] BrianLester,RamiAl-Rfou,andNoahConstant.Thepower
tian Gehrmann, Parker Schuh, Kensen Shi, Sasha ofscaleforparameter-efficientprompttuning,2021. 1
Tsvyashchenko, Joshua Maynez, Abhishek Rao, Parker [19] XiangLisaLiandPercyLiang. Prefix-tuning: Optimizing
Barnes, Yi Tay, Noam Shazeer, Vinodkumar Prabhakaran, continuouspromptsforgeneration,2021. 1

### EmilyReif, NanDu, BenHutchinson, ReinerPope, James

[20] Tsung-Yi Lin, Michael Maire, Serge Belongie, Lubomir

### Bradbury, Jacob Austin, Michael Isard, Guy Gur-Ari,


### Bourdev, Ross Girshick, James Hays, Pietro Perona, Deva

Pengcheng Yin, Toju Duke, Anselm Levskaya, Sanjay Ramanan,C.LawrenceZitnick,andPiotrDolla´r. Microsoft
Ghemawat, Sunipa Dev, Henryk Michalewski, Xavier
coco:Commonobjectsincontext,2015. 1

### Garcia,VedantMisra,KevinRobinson,LiamFedus,Denny

[21] HaokunLiu,DerekTam,MohammedMuqeeth,JayMohta,
Zhou, Daphne Ippolito, David Luan, Hyeontaek Lim,

### TenghaoHuang,MohitBansal,andColinRaffel. Few-shot


### Barret Zoph, Alexander Spiridonov, Ryan Sepassi, David

parameter-efficientfine-tuningisbetterandcheaperthanin-
Dohan, Shivani Agrawal, Mark Omernick, Andrew M.
contextlearning,2022. 1,2,4

### Dai, Thanumalayan Sankaranarayana Pillai, Marie Pellat,

[22] Haotian Liu, Chunyuan Li, Yuheng Li, and Yong Jae Lee.

### AitorLewkowycz, EricaMoreira, RewonChild, Oleksandr

Improvedbaselineswithvisualinstructiontuning,2023. 7

### Polozov, Katherine Lee, Zongwei Zhou, Xuezhi Wang,

[23] HaotianLiu,ChunyuanLi,QingyangWu,andYongJaeLee.
Brennan Saeta, Mark Diaz, Orhan Firat, Michele Catasta,

### Visualinstructiontuning,2023. 1,2,6,7


### JasonWei,KathyMeier-Hellstern,DouglasEck,JeffDean,

[24] HongLiu,ZhiyuanLi,DavidHall,PercyLiang,andTengyu

### Slav Petrov, and Noah Fiedel. Palm: Scaling language

Ma. Sophia: A scalable stochastic second-order optimodelingwithpathways,2022. 1
mizer for language model pre-training. arXiv preprint
[7] Zihang Dai, Zhilin Yang, Yiming Yang, Jaime Carbonell,
arXiv:2305.14342,2023. 1

### Quoc V. Le, and Ruslan Salakhutdinov. Transformer-xl:

[25] Ze Liu, Han Hu, Yutong Lin, Zhuliang Yao, Zhenda Xie,
Attentive language models beyond a fixed-length context,
YixuanWei,JiaNing,YueCao,ZhengZhang,LiDong,Furu
2019. 1

### Wei, and Baining Guo. Swin transformer v2: Scaling up

[8] Tri Dao, Daniel Y. Fu, Stefano Ermon, Atri Rudra, and
capacityandresolution,2022. 2,1

### ChristopherRe´. Flashattention: Fastandmemory-efficient

exactattentionwithio-awareness,2022. 2,1 [26] Wang Qi, Yu-Ping Ruan, Yuan Zuo, and Taihao Li.
Parameter-efficient tuning on layer normalization for pre-
[9] Tim Dettmers, Artidoro Pagnoni, Ari Holtzman, and Luke
trainedlanguagemodels,2022. 2

### Zettlemoyer. Qlora: Efficientfinetuningofquantizedllms,

2023. 7 [27] Alec Radford, Jeff Wu, Rewon Child, David Luan, Dario
[10] Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Amodei,andIlyaSutskever. Languagemodelsareunsuper-
Toutanova. Bert: Pre-training of deep bidirectional trans- visedmultitasklearners. 2019. 2
formersforlanguageunderstanding,2019. 1,8 [28] Alec Radford, Jong Wook Kim, Chris Hallacy, Aditya
[11] PatrickEsser,RobinRombach,andBjo¨rnOmmer. Taming Ramesh, Gabriel Goh, Sandhini Agarwal, Girish Sastry,
transformersforhigh-resolutionimagesynthesis,2021. 7 Amanda Askell, Pamela Mishkin, Jack Clark, Gretchen
[12] Leo Gao, Stella Biderman, Sid Black, Laurence Golding, Krueger, and Ilya Sutskever. Learning transferable visual
Travis Hoppe, Charles Foster, Jason Phang, Horace He, modelsfromnaturallanguagesupervision,2021. 2,7
Anish Thite, Noa Nabeshima, Shawn Presser, and Connor [29] Sylvestre-AlviseRebuffi,HakanBilen,andAndreaVedaldi.
Leahy. Thepile: An800gbdatasetofdiversetextforlan- Learning multiple visual domains with residual adapters,
guagemodeling,2020. 2 2017. 1
[13] Rohit Girdhar, Alaaeldin El-Nouby, Zhuang Liu, Mannat [30] Robin Rombach, Andreas Blattmann, Dominik Lorenz,
Singh, Kalyan Vasudev Alwala, Armand Joulin, and Ishan PatrickEsser,andBjo¨rnOmmer.High-resolutionimagesyn-
Misra. Imagebind: Oneembeddingspacetobindthemall, thesiswithlatentdiffusionmodels,2022. 7
2023. 2 [31] OlgaRussakovsky,JiaDeng,HaoSu,JonathanKrause,San-
[14] JiataoGu,HanyHassan,JacobDevlin,andVictorO.K.Li. jeevSatheesh,SeanMa,ZhihengHuang,AndrejKarpathy,
Universal neural machine translation for extremely low re- AdityaKhosla,MichaelBernstein, AlexanderC.Berg, and
sourcelanguages,2018. 3 LiFei-Fei.Imagenetlargescalevisualrecognitionchallenge,
[15] NeilHoulsby,AndreiGiurgiu,StanislawJastrzebski,Bruna 2015. 1
Morrone,QuentindeLaroussilhe,AndreaGesmundo,Mona [32] Tianxiao Shen, Myle Ott, Michael Auli, and Marc’Aurelio
Attariyan, and Sylvain Gelly. Parameter-efficient transfer Ranzato. Mixture models for diverse machine translation:
learningfornlp,2019. 1 Tricksofthetrade,2019. 3
9

<!-- Page 10 -->

[33] AmanpreetSingh, RonghangHu, VedanujGoswami, Guillaume Couairon, Wojciech Galuba, Marcus Rohrbach, and
Douwe Kiela. Flava: A foundational language and vision
alignmentmodel,2022. 2
[34] Jianlin Su, Yu Lu, Shengfeng Pan, Ahmed Murtadha, Bo
Wen, and Yunfeng Liu. Roformer: Enhanced transformer
withrotarypositionembedding,2022. 1
[35] Hugo Touvron, Louis Martin, Kevin Stone, Peter Albert, Amjad Almahairi, Yasmine Babaei, Nikolay Bashlykov, Soumya Batra, Prajjwal Bhargava, Shruti Bhosale, Dan Bikel, Lukas Blecher, Cristian Canton Ferrer,
Moya Chen, Guillem Cucurull, David Esiobu, Jude Fernandes, Jeremy Fu, Wenyin Fu, Brian Fuller, Cynthia

### Gao,VedanujGoswami,NamanGoyal,AnthonyHartshorn,

SagharHosseini,RuiHou,HakanInan,MarcinKardas,Viktor Kerkez, Madian Khabsa, Isabel Kloumann, Artem Korenev, Punit Singh Koura, Marie-Anne Lachaux, Thibaut
Lavril, Jenya Lee, Diana Liskovich, Yinghai Lu, Yuning

### Mao, Xavier Martinet, Todor Mihaylov, Pushkar Mishra,

IgorMolybog,YixinNie,AndrewPoulton,JeremyReizenstein, Rashi Rungta, Kalyan Saladi, Alan Schelten, Ruan
Silva, Eric Michael Smith, Ranjan Subramanian, Xiaoqing Ellen Tan, Binh Tang, Ross Taylor, Adina Williams,
Jian Xiang Kuan, Puxin Xu, Zheng Yan, Iliyan Zarov,

### Yuchen Zhang, Angela Fan, Melanie Kambadur, Sharan


### Narang,AurelienRodriguez,RobertStojnic,SergeyEdunov,

andThomasScialom. Llama2: Openfoundationandfinetunedchatmodels,2023. 1,2
[36] Aaron van den Oord, Oriol Vinyals, and Koray
Kavukcuoglu. Neural discrete representation learning,
2018. 7
[37] Guangxuan Xiao, Yuandong Tian, Beidi Chen, Song Han,
andMikeLewis. Efficientstreaminglanguagemodelswith
attentionsinks,2023. 6
[38] Wenhan Xiong, Jingyu Liu, Igor Molybog, Hejia Zhang,
Prajjwal Bhargava, Rui Hou, Louis Martin, Rashi Rungta,

### Karthik Abinav Sankararaman, Barlas Oguz, Madian

Khabsa, Han Fang, Yashar Mehdad, Sharan Narang, KshitizMalik,AngelaFan,ShrutiBhosale,SergeyEdunov,Mike
Lewis, Sinong Wang, and Hao Ma. Effective long-context
scalingoffoundationmodels,2023. 1
[39] Zhewei Yao, Xiaoxia Wu, Conglong Li, Minjia Zhang,

### Heyang Qin, Olatunji Ruwase, Ammar Ahmad Awan,

Samyam Rajbhandari, and Yuxiong He. Deepspeedvisualchat: Multi-round multi-image interleave chat via
multi-modalcausalattention,2023. 1,2,3,4
[40] EladBenZaken,ShauliRavfogel,andYoavGoldberg.Bitfit:
Simpleparameter-efficientfine-tuningfortransformer-based
maskedlanguage-models,2022. 1,2
[41] XiaohuaZhai,XiaoWang,BasilMustafa,AndreasSteiner,
Daniel Keysers, Alexander Kolesnikov, and Lucas Beyer.
Lit: Zero-shottransferwithlocked-imagetexttuning,2022.
2
10

<!-- Page 11 -->

Context-PEFT: Efficient Multi-Modal, Multi-Task Fine-Tuning

### Supplementary Material


## VisionEncoderDetails due to containing some copyrighted materials, but this removal occurred after the start of this work. Alternatives

WeexperimentwithtwoversionsoftheSwinTransformer such as the Pile-Uncopyrighted4 exist and should provide
V2[25],‘Tiny’and‘Large’.
comparableperformanceintermsofpre-training.

### Thetinyvariationisusedforinitialexperimentationand

finegrainedcomparisonsofdifferentadaptors. Thisvaria- 8.Heatmaps
tion was pre-trained for image classification on ImageNet-
1k [31] and has a final embedding dimension of 768. The WeprovideauxiliaryheatmapvisualisationstofurtherillusweightsandmodelwereprovidedbyHuggingFace1. trate the image-text semantic understanding capabilities of
The large variation is used for final evaluation and ourmodel.
coarsegrainedcomparisonswiththebestadaptorvariants.
This variation was pre-trained for image classification on
ImageNet-21k [31], further fine-tuned for ImageNet-1k,
andhasafinalembeddingdimensionof1536. Theweights
andmodelwereprovidedbyHuggingFace2.

## LLMPre-TrainingDetails


### The LLM has 150 million parameters with an embedding

dimension of 768, 12 layers of transformer blocks, 12 attention heads per attention layer utilising Rotary Position

### Embeddings [34] with an adjusted base frequency (RoPE

ABF[38]),SwiGLUactivation[6]inthefeedforwardlayers with an intermediate size of 6144/3072, and using a
frozen embedding layer taken from OPT-125m3 to speed
upconvergence. WemakeuseofFlashAttention2[8]toattainbetterperformanceandmemoryutilisationthanvanilla
dot-productattention.

### We also train the model with a Transformer-XL style

cache and shifting window [7], although instead of saving
keys and values we cache the hidden states pre-projection
and recompute them for each segment. This introduces
some additional training and inference latency when the
cache is in use, but comes with the advantage of generatingpartialgradientsfortheXL-cacheandhalvesthepersistent memory cost for the cache when accumulating gradientsoverseveralsub-batches.
The Sophia optimiser was used [24] for pre-training,
withawarm-upofapproximately2000batchestoalearning
rateof6e-4andcosineannealedtoalearningrateof6e-5,
using a batch size of 480, sequence length of 1024 tokens
(withadditionalXLmemoryof1024statesfortotalcontext
sizeof2048)andoptimiserhyper-parameterssuggestedby
theoriginalSophiaauthors.

### We train for 5 billion tokens on the now defunct Pile

dataset. The Pile was removed from its hosting platform
1SwinTV2TinyonHuggingFace
2SwinTV2LargeonHuggingFace
3OPT-125monHuggingFace 4Pile-UncopyrightedonHuggingFace
1

<!-- Page 12 -->

2

<!-- Page 13 -->

3

## Tables

**Table (Page 4):**

| A | F |
|---|---|
| 13.01 12.75 (-0.25) 12.97 12.51 (-0.46) 11.04 10.54 (-0.50) 9.50 9.09 (-0.41) 8.24 7.92 (-0.32) | 12.74 12.51 (-0.24) 11.93 11.70 (-0.22) 10.25 9.83 (-0.41) 8.72 8.44 (-0.28) 7.75 7.69 (-0.06) |


**Table (Page 5):**

| Context-Agnostic |
|---|
| 55,296 119,808 202,752 1,622,016 12,976,128 |


**Table (Page 5):**

| Tiny |
|---|
| 12.46 12.18 11.83 11.56 10.23 9.61 8.48 8.22 7.61 7.48 |
| 14.88 7.70 |
