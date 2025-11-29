---
title: "Adaptive RAG Dynamic Retrieval"
original_file: "./Adaptive_RAG_Dynamic_Retrieval.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["llm", "rag", "fine-tuning", "evaluation", "multimodal"]
keywords: ["dementia", "speaker", "speech", "privacy", "information", "embeddings", "score", "eer", "features", "spk"]
summary: "<!-- Page 1 -->

Prosody-Driven Privacy-Preserving Dementia Detection
DominikaWoszczyk1,RanyaAloufi1,2,SoterisDemetriou1
1ImperialCollegeLondon,UK
2TaibahUniversity,SaudiArabia
d.woszczyk19@imperial.ac.uk, r.aloufi18@imperial.ac.uk, s.demetriou@imperial.ac.uk
Abstract defined as “protected health information” (PHI) and must be
properlyde-identified. ### Speakerembeddingsextractedfromvoicerecordingshave


### PriorWorks. Anonymizationorde-identificationreferstothe

been proven valuable for dement"
related_documents: []
---

# Adaptive RAG Dynamic Retrieval

<!-- Page 1 -->

Prosody-Driven Privacy-Preserving Dementia Detection
DominikaWoszczyk1,RanyaAloufi1,2,SoterisDemetriou1
1ImperialCollegeLondon,UK
2TaibahUniversity,SaudiArabia
d.woszczyk19@imperial.ac.uk, r.aloufi18@imperial.ac.uk, s.demetriou@imperial.ac.uk
Abstract defined as “protected health information” (PHI) and must be
properlyde-identified.

### Speakerembeddingsextractedfromvoicerecordingshave


### PriorWorks. Anonymizationorde-identificationreferstothe

been proven valuable for dementia detection. However, by
taskofconcealingthespeaker’sidentitywhileretainingthelintheir nature, these embeddings contain identifiable informaguistic content, thereby making the data unlinkable [7]. Action which raises privacy concerns. In this work, we aim to
cording to the ISO/IEC International Standard 24745 on bioanonymize embeddings while preserving the diagnostic utilmetricinformationprotection[8],biometricreferencesmustbe
ity for dementia detection. Previous studies rely on adverirreversibleandunlinkableforfullprivacyprotection. Mostof
sarial learning and models trained on the target attribute and
theproposedworksfocusonprotectingspeakeridentity,using
struggle in limited-resource settings. We propose a novel apvoice conversion (VC) mechanisms [9, 10]. Beyond speaker
proachthatleveragesdomainknowledgetodisentangleprosody
identity, various works propose to protect speakers’ attributes
features relevant to dementia from speaker embeddings withandparalinguisticinformationsuchasemotion[11,12],gender
out relying on a dementia classifier. Our experiments show
[13],age[12]ornationality[14].Attributeobfuscationallowsa
theeffectivenessofourapproachinpreservingspeakerprivacy
speakertoconcealspecificpersonalaspectsintheirvoicerepre-
(speakerrecognitionF1-score.01%)whilemaintaininghighdesentationwhilestillmaintainingoverallperformance[15,13].
mentiadetectionscoreF1-scoreof74%ontheADReSSdataset.
Adversarial training disentangles dimensions in latent spaces
Ourresultsarealsoonparwithamoreconstrainedclassifierforspeakerverificationwhileminimizingdetectionofspecific
dependentsystemonADReSSo(.01%and.66%),andhaveno
attributes[11]. Theneedofanexternalattributeclassifier,esimpactonsynthesizedspeechnaturalness.12
pecially for low-resourced attributes like dementia with no or

### IndexTerms:privacy,speechverification,dementia

limitedtrainingdata,isasignificantconstraint. Analternative
approachistoworkatthefeaturelevelratherthantheutterance

## Introduction level [13, 16, 17]. By extracting and sanitizing feature representationsfromspeech,wecanshareprivacy-awarefeaturesin-


### Problem Statement. Advances in deep learning, combined

steadofcompleteutterances. Noe´ et. al.,in[13],forexample,
withnon-invasivebiomarkerslikespeech,offerapromisingopproposedaNormalizingFlow-basedarchitecturetodisentangle
portunity for large-scale disease diagnosis. Researchers have
sexinformationinx-vectors.
investigated the use of speech signals for detecting different
Our Approach. In this work, we leverage prosody disentanmedical conditions, such as neurodegenerative diseases (e.g.,
glement as a method for speaker anonymization in dementia
Parkinson’sandAlzheimer’s)[1]andrespiratoryailments(e.g.,
detection. Specifically,ourgoalistopreservethedementiaat-

## Covid-19)[2].

tribute in speaker embeddings while reducing speaker-related

### Speakerembeddings(e.g.,i-vector,x-vector,andECAPA-

information(identity). Often,adversarialtrainingormulti-task
TDNN) are a type of feature set utilized in the detection of
learning is utilized to confine information within bottlenecks,
early signs of diseases like dementia [3]. However, speaker
separatingoutdimensionssuchascontent, pitch, rhythm, and
embeddings often contain more information than required for
timbre [18, 10]. However, we take a different approach, fotheir intended tasks, which poses potential privacy concerns.
cusingonprosodicfeaturesthatareknowntobeprominentin

### Forexample,theycontainspeaker-specificinformation,which

dementia speech, such as articulation rate, pauses, and disflumakes them effectivein automaticspeaker verification(ASV)
encies. Our hypothesis is that by disentangling these features
and zero-shot text-to-speech (TTS) among others. This uninfrom speaker representations, we can effectively obscure the
tentionalinformationleakagemightviolateGDPRpolicies[4]
speaker’s identity while minimizing any impact on dementiaanditsdataminimizationprinciple[5](i.e.,“adequate,relevant
relatedinformation. Oursystemachievesthiswithoutrelying
andlimitedtowhatisnecessaryinrelationtothepurposesfor
ondedicatedclassifiers,usingdomainknowledgeandadversarwhich they are processed”), leaving individuals vulnerable to
iallearningtechniques.
discrimination,extortion,andtargetedadvertisementsbythird–
parties. Moreover, since speaker embeddings can be used to Belowwesummarizethe maincontributionsofthiswork:
predict both dementia and verify a speaker, they can be po-

## NovelApproach: Weproposeanovelmethodforpreservtentiallyclassifiedas“individuallyidentifiablehealthinformaing privacy in speaker embeddings in low-resource settings

tion”. UndertheHIPAAPrivacyRule[6]suchinformationis
throughdomainknowledgeandprosodydisentanglement.
1The code is available at https://github.com/domiwk/ 2. New Application Domain We shed light on a sensitive atprivacy-preserving-ad-detection tribute, dementia, thathasnotbeenextensivelyinvestigated
2Samplesareavailableathttps://shorturl.at/cNS39 inpreviousattributeobfuscationandanonymizationworks.
4202
luJ
3
]DS.sc[
1v07430.7042:viXra

<!-- Page 2 -->


## Privacy-PreservingDementiaDetection 2.4. MutualInformation-GuidedShuffling


### ThreatModel We propose a feature selection approach based on mutual information to identify important features relevant to dementia

Our threat model focuses on medical speech-processing sys- whileperturbinglessrelevantfeaturestolowerspeakerrecogtems developed for detecting dementia and their handling. nitionaccuracy. Ourmethodissimilarto[16]wheretheyex-
Thesesystemsuseaudiodatatogenerateembeddingsthatcan tractShapleyvaluesfromaclassifiertoselectkeydimensions,
helpidentifysignsofdementia. Thisraisessignificantprivacy however,unliketheirs,ourapproachisclassifier-free. Theinconcernsasspeakerembeddingscanpotentiallyrevealindivid- tuitionbehindthisapproachisthatcriticalfeaturesassociated
uals’ identities. We consider an adversary that has access to withdementiaarelikelytohavehighermutualinformationwith
theanonymizedembeddingsandaimstore-identifytheuserby thetargetvariable(dementia),whileshufflingtheremainderto
using the embeddings not for their primary purpose (demen- preservedementia-relatedfeaturesbutdecreasespeakerrecogtiaclassification)butforspeakerrecognition. Thisinformation nitionaccuracy.Wealsoexploreusingprosodyfeaturesinstead
couldbeexploitedfordiscriminatorypurposesortargetedad- ofthedementialabelasthetargetvariable.
vertising. Effective anonymization techniques should prevent Mutualinformationisameasureofmutualdependencebesuchlinkageattackswhilepreservingspeechnaturalness,intel- tween two random variables. In our context, we compute the
ligibility,andperformanceindementiadetection. mutualinformationbetweenthedistributionofdimensionofthe
Weaimtosafeguardtheprivacyofuseridentityindiffer- speakerembeddingsandthedistributionofthedementialabel
entscenariosthatinvolvevoiceembeddingsormedicalspeech acrossthedataset. Formally, themutualinformationI(X;Y)
processing. Thisinvolvesobfuscatinganyidentifyinginforma- betweenrandomvariablesXandY isdefinedas:
tionthatausermaynotwanttoshare, withoutcompromising
thefunctionalityofthesystem. Wealsoemphasizetheneedto
(cid:18) (cid:19)
offervariousprivacysettingstobalancethetrade-offbetween (cid:88) (cid:88) p(x,y)

### I(X;Y)= p(x,y)log (2)

privacyandutility, andtoencouragetransparentprivacyman- p(x)p(y)
x∈Xy∈Y
agementpractices.
where p(x,y) is the joint probability mass function of X

### ProposedApproach and Y, and p(x) and p(y) are the marginal probability mass

functions of X and Y, respectively. To estimate the mutual

### We devise a prosody-based privacy-preserving extraction for

information,weusethek-Nearest-Neighbour-basedMIestimaspeakerrepresentations,trainedonalargerauxiliarydatasetthat
tor[22]whichcanbeappliedtobothcontinuousanddiscrete
does not need to have the target attribute label. We leverage
variables. Wedesignthefeatureselectionstrategyasfollows:
domainknowledgeforthetaskofdementiadetectionandpro-
1) Compute the mutual information between each embedding
pose a method that performs disentanglement that focuses on
dimensionandthedementia/prosodyvariableacrossthewhole
prosodyfeaturesrelevanttodementia.Indeed,previousstudies
corpus. 2) Select top n dimensions as important dementiahaveshownthatfeaturessuchasspeechrate,meanenergylevrelatedfeatures. 3)Shuffletheremainingfeatures. Whencomels,numberofpausesandlengths[19,20]areinformativefor
biningseveralfeatures,computethetopndimensionsforeach
dementiaclassification. Weexploretwoapproaches: adversarandcomputetheunionasthesetofimportantfeatures.
iallearningandmutualinformation-guidedshuffling.

## ExperimentalSetup


### Adversarial Learning for Speaker-Prosody Disentanglement 3.1. Datasets

Theproposedadversarialmodelisbasedondomainadversar- We train our disentanglement model on the LibriSpeech
ial training [21] which aims to create domain-invariant latent dataset[23],acorpusofreadEnglishspeech. Weselectedthe
spaces by maximising the domain discriminator’s confusion train-clean-100 subset which consists of 100 hours of
while minimizing the task-specific loss. In our case, we train speech from 251 speakers. We split the data into 25685, and
ourmodeltoextractdementia-relevantprosodyfeatureswhile 2850 samples for train, and dev sets respectively. We extract
maximisingthelossofspeaker-relevantfeatures. Totrainthis prosodyfeaturesforeachsample.
model, we can take advantage of a larger dataset and extract For testing dementia detection, we use two publicly
prosodicfeatures. Atinferencetime,werunthemodelonany available datasets widely studied in dementia classification:
datasetwewishtoanonymize. Themodelconsistsofseveral ADReSS[24]andADReSSo[24].TheADReSS(ADR)dataset
components: the feature extractor that extracts speaker repre- isasubsetoftheDementiaBankdataset,acollectionofrecordsentations, and prosody regressors for each prosodic feature. ingsfromcontrol(CD)anddementia(AD)patientsdescribing
Thelossofourmodelisdefinedas: theCookieTheftPicture[25]. Manualtranscriptsareprovided
andwespliteachsampleintosegmentsusingthesentence-level
n n timestampsfromthetranscripts.Wegrouptheoriginaltestand
(cid:88) (cid:88)
L= L ADprosi − λ j L SPKprosj (1) trainsetsandsplitthedatatocontainonesampleperspeakerin
i=0 j=0 thetestsetandkeeptheremainingsamplesastrainingdata.We
endupwith1723samples(868CC|855AD)inthetraining
whereL ADprosi denotestheith lossassociatedwiththeith setand156(78CC|78AD)inthetestandvalidationsets.The
dementia-relevantprosodyfeatureextraction,andL SPKprosj the ADReSSo(ADRo)datasetisanothersubsetofDementiaBank
jth lossassociatedwiththejth speaker-relevantprosodyfea- designedfordetectingdementiafromspontaneousspeechonly,
tureregressor. λ isahyperparameterthatcontrolsthebalance withoutaccesstomanualtranscriptions. Theoriginalsetconj
between the different objectives and n is the total number of sistsof151trainsamples(87CC|74AD)and71testsamples
prosodyregressors. (35CC|35AD).Weusetheprovidedsegmentationtimestamps

<!-- Page 3 -->

toisolatesegmentsspokenbythepatientsandget2705samples 4. Results
inthetrainset(920CC|1026AD)and231samples(74CC|

### ProsodicFeaturesSelection

87AD)inthetestandvalidationsets,oneperspeaker.

### Wechooseprosodyfeaturesbasedonmutualinformation(MI)


#### DataProcessing withdementialabelsintheADReSSdataset,selectingthetop

35 quantiles. Then, we assess their importance in speaker
For the dementia datasets, we split samples into segments as recognition by computing MI with speaker labels. Figure 1
described in Section 3.1. For both LibriSpeech and Demen- showsMIscoresforfeaturesw.r.t. classandspeakeridentity.
tiadatasets,weextractaseriesofarticulationfeatures,number Notably,meanf0andenergyaresignificantforbothdementia
and length of pauses, f0 and mean energy. We compute the and speakers. However, mean energy is strongly linked with
featureswithParselmouthandPraatscriptsmadeavailableby speakeridentity,whilef0isaknownspeakercharacteristic. To
Feinberg[26]andnormalisethemtobewithin[0,1].Whenex- removespeakerinformation,wedecidetoseparatefeaturesinto
tractingembeddings,wetrimthesegmentsto30s. prosodicanddisfluencyfeaturestodisentanglespeakersanddementia. Weselectspeechrate(spr),numberofpauses(pnum),

### ImplementationDetails lengthofpauses(plength)andnumberofsyllablesasdementia

featuresandmeanf0(f0)andenergy(nrg)asspeaker-relevant
Weselectapre-trainedECAPA-TDNN[27]embeddingextracfortheADVPROSandShuffle systems.
tor,regardedasthestate-of-the-art(SOTA)forspeakerembed- MIpros
dings. Weuse theSpeechBrain[28] implementationandpre-
Top Features for Dementia Label Top Features for Speaker ID
trainedmodelwhichwastrainedontheVoxCelebdataset. We

### Number of Pauses Number of Syllables

augment the ECAPA-TDNN embedding extractor with classifiers for each prosodic feature, each consisting of two layers Length of Pauses Number of Pauses
with 126 hidden dimensions. We use the Mean-Square-Error Number of Syllables Length of Pauses
Loss for the prosody regressors and investigate λ values in Speech Rate Speech Rate
{1,5,10,30}andsetλto1.0. Wetrainthemodelwithabatch Mean F0 Mean F0
size of 8 with cyclical learning rate policy (CLR) and set the

### Energy Energy

baseandmaximumlearningratesto1e-7and1e-5respectively.
0.00 0.02 0.04 0.0 0.5 1.0
Wefinetunethemodelsfor15epochswithearlystopping. We Mutual Information Mutual Information
compareourmodeltoseveralmodels:amodeltrainedonade- Figure 1: Mutual information scores of key prosodic features
mentia dataset to classify dementia while fooling the speaker extracted from audio segments for dementia label (left) and
classifier (ADV SPK AD + AD), a model trained on the Lib- speakeridentity(ID)(right)ontheADReSSdataset.
riSpeech dataset to fool the speaker classifier (ADV SPK ),

## Ls

a random shuffling method (Shuffle ) and a shuffling

### Random

from [16] where we train an XGBoost model [29] on demen- 4.2. OverallResults
tiaandselecttopnShapleyvalues(Shuffle ). Forthemu-

### Shap

tualinformationshufflingmethod(Shuffle MI ),wecomputethe Table1: Comparisonofanonymizationsystems’performance.
mutualinformationusingthesklearnlibrary [30].Thedemen- WereportthedementiadetectionF1-score(AD),speakerrecogtia classifier is a two-layer model with a hidden space size of nition F1-score (SPK), their 95% confidence intervals and
8 and a ReLu activation between layers, trained with Binary EqualErrorRate(EER).

### Cross-Entropy.Thespeakerclassifierisatwo-layermodelwith

ahiddenspacesizeof96trainedwithCross-EntropyLoss. We ADReSS ADReSSo

### System

optimiseregressorswithbayesiansearch. AD↑ SPK↓ EER(%)↑ AD↑ SPK↓ EER(%)↑

### Original .81±.06 .33±.06 35 .73±.06 .36±.04 35


### EvaluationMetrics ADVSPKAD+AD .64±.06 .00±.02 47 .63±.06 .00±.02 45


## Advspkls .80±.13 .69±.01 15 .75±.1 .75±.01 16


### ADVnrgPROS .73±.13 .01±.01 43 .66±.10 .01±.01 44

Privacy. Wemeasuretheprivacygainthroughthedropofan ShuffleRandom .63±.08 .01±.00 41 .61±.06 .02±.04 41
adversary’s (speaker classifier from Section 3.2) F1-score and ShuffleShap .62±.07 .02±.02 41 .64±.07 .04±.02 40
speakerverificationEqualErrorRate(EER)score(usingcosine

### ShuffleMIAD .63±.07 .02±.02 41 .62±.06 .02±.01 42


### ShuffleMIpros .62±.08 .01±.02 44 .68±.06 .02±.01 43

distance). Duetothesizeofourdataset,wefocusonablackbox setting and do not adapt our adversary. We evaluate the
Table1showstheperformanceoftheanonymizationsysanonymized embeddings against an SVM with a radial basis
tems. WeseethatADVSPK +ADdropsthespeakerF1-
functionkernel,asitperformedthebestonbothdatasets. AD
score to 0% for both ADR and ADRo and increases the EER
Utility. To evaluate the ability to detect dementia, we train a by12%,10%respectively,givingthebestanonymizationperneuraldementiaclassifierontopoftheembeddingsandreport formance. We note that the EER on the original samples is
theF1-score. Weimplementafeed-forwardnetworkwithtwo quitehigh(35%),whichweattributetothenoisynatureofthe
layers,ahiddenspacesizeof8andaReLuactivationbetween dataset. However,inthiswork,weareinterestedintherelative
layers. Additionally, we perform zero-shot speech generation increase.WeseethesystemreducestheADdetectionF1-score
withthenewembeddingsandmeasureMOSNet[41],SI-SDR to65%,onparwiththeshufflingapproaches. Throughexper-
[42],andSTOI[43],whichareusedasobjectivemetricstoeval- imentations,weobservethattheenergy(nrg)gaveusstronger
uatethequalityofspeechsignals,andWER(WordErrorRate) privacyguaranteesacrosssubsets,asshowninTable3. WerewithWhisper[31]. Thesemetricsareusedtoassessthequal- portADV PROSasourbestsystem. ADV PROS,drops
nrg nrg
ityoftheprocessedsignalcomparedtotheoriginalsignal. We theaccuracyto0.01%andadds8%totheEERwhilepreserving
pickYourTTS[32]andSpeechT5[33],twoopen-sourcezero- 73%F1-scoreonADR,adropof7%fromtheoriginalperforshotTTSsystemsthathaveshownSOTAperformance. mance, makingitthebest-performingapproach. OnADRoit

<!-- Page 4 -->

Table 2: Zero-Shot TTS Quality Metrics and WER on the tectionwithanegligibleimpactonprivacymetrics. Nearlyall
ADReSSdataset. featuresareusefulforpreservingdementia,whilethespeaking
ratedidnotseemtoaffectthedetection.
TTS System MOSNet↑ SI-SDR↑ STOI↑ Avg.Rank↓ WER(%)↓

### Original 2.84 -69.01 .26 3.33 23


### Table3: Differentprosodysets. Wereportthedementiadetec-

SpeechT5 AD A V DV SP n K rg A P D R + OS AD 2 2 . . 8 8 4 4 - - 7 7 2 3 . . 2 4 3 1 . . 2 2 1 3 2 1 . . 8 8 3 3 3 3 5 0 tionF1-score(AD),speakerrecognitionF1-score(SPK),their
ShuffleMIpros 2.84 -70.73 .26 2.50 21 95%confidenceintervals,andEqualErrorRate(EER).
ShuffleShap 2.84 -72.16 .23 2.83 34

### Original 2.77 -68.57 .24 2.33 27

YourTTS AD A V DV SP n K rg A P D R + OS AD 2 2 . . 8 8 2 2 - - 6 6 7 8 . . 9 6 0 0 . . 2 2 3 3 2 1 . . 8 3 3 3 2 3 9 0 System AD↑ A SP D K R ↓ eSS EER(%)↑ AD↑ A S D P R K e ↓ SSo EER(%)↑

### ShuffleMIpros 2.82 -68.43 .23 2.00 27

ShuffleShap 2.82 -68.23 .23 2.66 28 ADVf0 .79±.13 .17±.02 29 .72±.11 .20±.01 29
ADVf0PROS .76±.13 .29±.02 29 .74±.11 .27±.02 29

### ADVnrgf0 .73±.13 .03±.02 32 .72±.11 .03±.01 33

ADVnrgf0PROS .74±.13 .02±.02 32 .68±.11 .03±.01 33
achievescomparableperformancetoADVSPK +ADand

### ADVnrg .65±.11 .01±.01 45 .67±.11 .01±.01 46


### AD ADVnrgPROS .73±.13 .01±.01 43 .66±.11 .01±.01 44

shufflingapproaches. Wecompareittothemodeltrainedad- ADVnrgPROSnonsyll .68±.13 .01±.01 43 .66±.11 .01±.01 45
versarially against a speaker classifier ADV SPK . Surpris- ADVnrgPROSnoplength .70±.13 .01±.01 44 .64±.11 .00±.01 47

### LS ADVnrgPROSnopnum .69±.13 .00±.01 44 .61±.11 .01±.01 46

ingly,themodelsimprovedthespeakerrecognitionanddemen- ADVnrgPROSnospr .71±.13 .02±.02 43 .64±.11 .01±.01 44
tiaclassifiersonbothdatasets. Weevaluateditincombination
withotherfeatures,andasimilarpatternwasseen,hencewereportonlyADVSPK LS .Finally,weevaluatedifferentshuffling 5. Discussion
approaches. We report the systems selecting top 50 features
as it gave us the best privacy/utility tradeoff for all systems. In this work, we show that we can successfully anonymize
WenotethattheselectionprocesswithMIbasedonthelabel speaker embeddings and preserve dementia detection by dis-
(Shuffle MIAD )andprosody(Shuffle MIpros )seemstoaddlit- entangling prosodic features relevant to dementia. Albeit the
tletotheaccuracywhencomparedtoShuffle Random . Never- originalEERisquitehigh,itsincreasedemonstratestheeffectheless, theshufflingapproachesachievesimilarresultstothe tivenessofourapproach. Futureworkwillexploreastronger
strongbaselineADVSPK AD +AD,whilebeingsimpler. adversaryinawhite-boxsettingandmorerobusttochallenging
speech. Furthemore,theapproachcanbeextendedtootherat-

### Zero-shotTTS-basedEvaluation tributesorhealthconditions. Nevertheless,alimitationofour

workisthedomainknowledgeandfeatureanalysisrequiredto
The Voice Privacy Challenge (VPC) revealed that all methfine-tunethedisentanglement. Forourusecase,themeanenods,includingx-vectorembeddingsandsignalprocessingtechergywasanimportantfeatureinremovingspeakerinformation.
niques, could lead to a degradation in speech naturalness and

### However,thisisdataset-specificandthegeneralizabilityofour

intelligibility [7, 34]. We thus conducted an objective evalsystemwouldneedtobeevaluatedonalargerdataset,andexuation on the ADReSS dataset using speech synthesis modplore more features. In terms of feature selection on the emels using two text-to-speech (TTS) systems: SpeechT5 and
beddings, future work would investigate explainable methods

### YourTTS (zero-shot TTS systems) to assess the effectiveness

tounderstandwhatembeddingsencodethroughouttheextracofanonymizedembeddingsintext-to-speech(TTS)tasks. We
tionprocesstobetterextract/obfuscateinformation.Finally,deutilizesentence-leveltranscriptionsasinputdataandcondition
mentiahasanimportantimpactonlinguisticsandtheircontent
the TTS system on speaker embeddings. For a fair compariwhich could be further explored to preserve dementia better.
son, we regenerate the raw recordings using the raw embed-

### However,thisalsoraisesotherprivacyconcernswherepatient

ding extracted from the original recordings. We then use the
transcripts might be leaked and calls for content disentangleanonymized embeddings of different settings to generate difmentaswell.Weleavetheexplorationofthisproblemtofuture
ferenttestsets. Rankingswerebasedonaverageperformance
work.
across all metrics, with lower average ranks indicating better
overallspeechquality. MOSNetrepresentstheMeanOpinion

## Conclusion

Score predicted by a neural network model for the quality of
speechsignals. HigherMOSNet,SI-SDR,andSTOIscoresin-
Wepresentanovelapproachforanonymizingspeakerembeddicatebetterqualityandspeechintelligibility. Table2reports
dings for privacy-preserving dementia detection. Our experitheresultsofourproposedmethodunderdifferentsettingsand
mentsshowthepotentialofusingprosodydisentanglementto
the baseline (synthesized raw recordings) using two TTS sysisolatespecificattributesfromspeakeridentityinlow-resource
tems.Wefindthattheanonymizationresultsinalmostthesame
settings. By training an embedding extraction model against
voice distinctiveness as the data originally had, and, accordprosodicextractorsonanauxiliarydataset,weeffectivelyminingtospeechrecognition,producesintelligiblespeechrecordimise speaker identity information while preserving the diagings. ADV SPK + AD seems to strike the best balance in
AD nosticutilityfordementia. Weshowtheeffectivenessofshufmaintainingvoicedistinctivenesswhileensuringanonymity,as
flingselectedembeddingdimensionsforanonymizationwithan
shownbyitslowerAvg. Rank,eventhoughallmethodsintroimpactsimilartoclassifier-dependentadversariallearning.NoducesomelevelofdegradationinSI-SDRandWER,whichis
tably,ourdisentanglementapproachoutperformsthetraditional
atrade-offforachievingspeakeranonymity.
adversarial training, showcasingthe importance of thedataset
size. Amongourselectedfeatures,disfluencyandarticulatory

### Ablationstudy

featurescontributetopreservingdementiawithlittleimpacton
We investigate the impact of dementia-relevant and speaker- thespeaker’sprivacy. OurworkisafirststeptowardsprivacyrelevantprosodicfeaturesandreporttheresultsinTable3. We preservingspeakerembeddingsforhealthcareapplicationsand
findthattheadditionofprosodyfeaturesimprovesdementiade- wehopetoinspirefurtherrefinementsoftheseapproaches.

<!-- Page 5 -->


## References

[18] K.Qian,Y.Zhang,S.Chang,M.Hasegawa-Johnson,andD.Cox,
“Unsupervisedspeechdecompositionviatripleinformationbot-
[1] S.delaFuenteGarcia,F.Haider,andS.Luz,“Cross-corpusfeatleneck,” in International Conference on Machine Learning.
turelearningbetweenspontaneousmonologueanddialoguefor
PMLR,2020,pp.7836–7846.
automaticclassificationofalzheimer’sdementiaspeech,”in2020
42ndAnnualInternationalConferenceoftheIEEEEngineering [19] V. Vincze, G. Szatlo´czki, L. To´th, G. Gosztolya, M. Pa´ka´ski,
inMedicine&BiologySociety(EMBC). IEEE,2020,pp.5851– I.Hoffmann,andJ.Ka´lma´n,“Telltalesilence: temporalspeech
parameters discriminate between prodromal dementia and mild
5855.
alzheimer’sdisease,” ClinicalLinguistics& Phonetics, vol.35,
[2] E.Casanova,A.CandidoJr,R.C.F.Junior,M.Finger,L.R.S. no.8,pp.727–742,2021.

### Gris,M.A.Ponti,andD.P.P.DaSilva,“Transferlearningand

[20] P.Pastoriza-Dominguez,I.G.Torre,F.Dieguez-Vide,I.Go´mezdataaugmentationtechniquestothecovid-19identificationtasks Ruiz,S.Gelado´,J.Bello-Lo´pez,A.A´vila-Rivera,J.A.Matiasincompare2021.”inInterspeech,2021,pp.446–450.

### Guiu,V.Pytel,andA.Herna´ndez-Ferna´ndez,“Speechpausedis-

[3] C.Botelho,T.Schultz,A.Abad,andI.Trancoso,“Challengesof tributionasanearlymarkerforalzheimer’sdisease,”SpeechComusinglongitudinalandcross-domaincorporaonstudiesofpatho- munication,vol.136,pp.107–117,2022.
logicalspeech.”2022. [21] Y. Ganin, E. Ustinova, H. Ajakan, P. Germain, H. Larochelle,
[4] eur lex.europa.eu, “Regulation (eu) 2016/679 of the european F.Laviolette,M.March,andV.Lempitsky,“Domain-adversarial
parliamentandofthecouncilof27april2016ontheprotection training of neural networks,” Journal of machine learning reof natural persons with regard to the processing of personal search,vol.17,no.59,pp.1–35,2016.
data and on the free movement of such data, and repealing [22] B.C.Ross,“Mutualinformationbetweendiscreteandcontinuous
directive95/46/ec(generaldataprotectionregulation).”[Online]. datasets,”PloSone,vol.9,no.2,p.e87357,2014.

### Available:https://tinyurl.com/6tk3j9aw

[23] V. Panayotov, G. Chen, D. Povey, and S. Khudanpur, “Lib-
[5] commission.europa.eu, “What personal data is considered rispeech: an asr corpus based on public domain audio books,”
sensitive?”[Online].Available:https://tinyurl.com/2fmu22j6 in2015IEEEinternationalconferenceonacoustics,speechand
signalprocessing(ICASSP). IEEE,2015,pp.5206–5210.
[6] hhs.gov, “The hipaa privacy rule,” accessed online on March
2024.[Online].Available:https://tinyurl.com/yhbpsame [24] S.Luz,F.Haider,S.delaFuente,D.Fromm,andB.MacWhinney, “Alzheimer’s dementia recognition through spontaneous
[7] N. Tomashenko, B. M. L. Srivastava, X. Wang, E. Vincent,
speech:Theadresschallenge,”arXivpreprintarXiv:2004.06833,
A.Nautsch,J.Yamagishi,N.Evans,J.Patino,J.-F.Bonastre,P.-
2020.
G.Noe´etal.,“Introducingthevoiceprivacyinitiative,”inINTER-
[25] J.T.Becker,F.Boiler,O.L.Lopez,J.Saxton,andK.L.McGo-

## Speech2020,2020.

nigle,“Thenaturalhistoryofalzheimer’sdisease: descriptionof
[8] ISO/IEC,“Iso/iec24745:Informationsecurity,cybersecurityand studycohortandaccuracyofdiagnosis,”Archivesofneurology,
privacy protection — biometric information protection.” May vol.51,no.6,pp.585–594,1994.
2021.
[26] D.R.Feinberg,“Parselmouthpraatscriptsinpython,”Jan2022.
[9] B. M. L. Srivastava, N. Vauquier, M. Sahidullah, A. Bellet, [Online].Available:osf.io/6dwr3
M.Tommasi,andE.Vincent,“Evaluatingvoiceconversion-based [27] B. Desplanques, J. Thienpondt, and K. Demuynck, “Ecapaprivacyprotectionagainstinformedattackers,”inICASSP2020- tdnn: Emphasized channel attention, propagation and ag-
2020 IEEE International Conference on Acoustics, Speech and gregation in tdnn based speaker verification,” arXiv preprint
SignalProcessing(ICASSP). IEEE,2020,pp.2802–2806. arXiv:2005.07143,2020.
[10] P.-G. Noe´, M. Mohammadamini, D. Matrouf, T. Parcollet, [28] M. Ravanelli, T. Parcollet, P. Plantinga, A. Rouhe, S. Cornell,
A.Nautsch,andJ.-F.Bonastre,“Adversarialdisentanglementof L. Lugosch, C. Subakan, N. Dawalatabad, A. Heba, J. Zhong,
speakerrepresentationforattribute-drivenprivacypreservation,” J.-C. Chou, S.-L. Yeh, S.-W. Fu, C.-F. Liao, E. Rastorgueva,
arXivpreprintarXiv:2012.04454,2020. F. Grondin, W. Aris, H. Na, Y. Gao, R. D. Mori, and Y. Ben-
[11] O.Chouchane,M.Panariello,O.Zari,I.Kerenciler,I.Chihaoui, gio, “SpeechBrain: A general-purpose speech toolkit,” 2021,
M.Todisco,andM.O¨nen,“Differentiallyprivateadversarialauto- arXiv:2106.04624.
encodertoprotectgenderinvoicebiometrics,”inProceedingsof [29] T. Chen and C. Guestrin, “XGBoost: A scalable tree boosting
the2023ACMWorkshoponInformationHidingandMultimedia system,”inProceedingsofthe22ndACMSIGKDDInternational
Security,2023,pp.127–132. ConferenceonKnowledgeDiscoveryandDataMining,ser.KDD
’16. NewYork,NY,USA:ACM,2016,pp.785–794.
[12] F. Teixeira, A. Abad, B. Raj, and I. Trancoso, “Privacyorientedmanipulationofspeakerrepresentations,”arXivpreprint [30] F.Pedregosa,G.Varoquaux,A.Gramfort,V.Michel,B.Thirion,
arXiv:2310.06652,2023. O.Grisel,M.Blondel,P.Prettenhofer,R.Weiss,V.Dubourgetal.,
“Scikit-learn: Machinelearninginpython,”Journalofmachine
[13] P.-G. Noe´, A. Nautsch, D. Matrouf, P.-M. Bousquet, and J.-F. learningresearch,vol.12,no.Oct,pp.2825–2830,2011.
Bonastre, “A bridge between features and evidence for binary
[31] A.Radford,J.W.Kim,T.Xu,G.Brockman,C.McLeavey,and
attribute-drivenperfectprivacy,”inICASSP2022-2022IEEEIn-
I.Sutskever,“Robustspeechrecognitionvialarge-scaleweaksuternationalConferenceonAcoustics,SpeechandSignalProcesspervision,” in International Conference on Machine Learning.
ing(ICASSP). IEEE,2022,pp.3094–3098.
PMLR,2023,pp.28492–28518.
[14] C. Luu, S. Renals, and P. Bell, “Investigating the contribution
[32] E.Casanova,J.Weber,C.D.Shulby,A.C.Junior,E.Go¨lge,and
of speaker attributes to speaker separability using disentangled
M.A.Ponti, “Yourtts: Towardszero-shotmulti-speakerttsand
speakerrepresentations,”inInterspeech2022. ISCA,2022,pp.
zero-shotvoiceconversionforeveryone,” inInternationalCon-
610–614.
ferenceonMachineLearning. PMLR,2022,pp.2709–2720.
[15] R.Aloufi,H.Haddadi,andD.Boyle,“Privacy-preservingvoice [33] J.Ao,R.Wang,L.Zhou,C.Wang,S.Ren,Y.Wu,S.Liu,T.Ko,
analysisviadisentangledrepresentations,”inProceedingsofthe Q.Li,Y.Zhang,Z.Wei,Y.Qian,J.Li,andF.Wei,“SpeechT5:
2020 ACM SIGSAC Conference on Cloud Computing Security Unified-modalencoder-decoderpre-trainingforspokenlanguage
Workshop, ser.CCSW’20. NewYork, NY,USA:Association processing,”inProceedingsofthe60thAnnualMeetingoftheAsforComputingMachinery,2020,p.1–14. sociationforComputationalLinguistics(Volume1:LongPapers).
[16] C.Lavania, S.Das, X.Huang, andK.Han, “Utility-preserving Dublin,Ireland:AssociationforComputationalLinguistics,May
privacy-enabledspeechembeddingsforemotiondetection,”2023. 2022,pp.5723–5738.
[34] S. Meyer, F. Lux, P. Denisov, J. Koch, P. Tilli, and N. T. Vu,
[17] M.TranandM.Soleymani,“Privacy-preservingRepresentation
Learning for Speech Understanding,” in Proc. INTERSPEECH “Speaker Anonymization with Phonetic Intermediate Represen-
2023,2023,pp.2858–2862.
tations,”inProc.Interspeech2022,2022,pp.4925–4929.

## Tables

**Table (Page 3):**

|  |  |  |  |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |


**Table (Page 3):**

|  |  |  |  |  |
|---|---|---|---|---|
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |


**Table (Page 3):**

| ADReSS |
|---|
| AD↑ SPK↓ EER(%)↑ |
| .81±.06 .33±.06 35 |
| .64±.06 .00±.02 47 .80±.13 .69±.01 15 .73±.13 .01±.01 43 |
| .63±.08 .01±.00 41 .62±.07 .02±.02 41 .63±.07 .02±.02 41 .62±.08 .01±.02 44 |


**Table (Page 4):**

| ADReSS |
|---|
| AD↑ SPK↓ EER(%)↑ |
| .79±.13 .17±.02 29 .76±.13 .29±.02 29 .73±.13 .03±.02 32 .74±.13 .02±.02 32 |
| .65±.11 .01±.01 45 .73±.13 .01±.01 43 |
| .68±.13 .01±.01 43 .70±.13 .01±.01 44 .69±.13 .00±.01 44 .71±.13 .02±.02 43 |
