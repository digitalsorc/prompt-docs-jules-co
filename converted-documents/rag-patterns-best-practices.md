---
title: "RAG Patterns Best Practices"
original_file: "./RAG_Patterns_Best_Practices.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["prompt-engineering", "llm", "rag", "chain-of-thought", "react"]
keywords: ["retrieval", "llms", "rag", "arxivpreprintarxiv", "page", "etal", "input", "forexample", "wenqifan", "associationforcomputationallinguistics"]
summary: "<!-- Page 1 -->

A Survey on RAG Meeting LLMs: Towards Retrieval-Augmented

### Large Language Models


### WenqiFan YujuanDing∗ LiangboNing

wenqifan03@gmail.com dingyujuan385@gmail.com BigLemon1123@gmail.com
TheHongKongPolytechnic TheHongKongPolytechnic TheHongKongPolytechnic
University,HKSAR University,HKSAR University,HKSAR

### ShijieWang HengyunLi DaweiYin

shijie.wang@connect.polyu.hk neilhengyun.li@polyu.edu.hk yindawei@acm.org
TheHongKongPolytechnic TheHongKongPolytechnic BaiduInc,China"
related_documents: []
---

# RAG Patterns Best Practices

<!-- Page 1 -->

A Survey on RAG Meeting LLMs: Towards Retrieval-Augmented

### Large Language Models


### WenqiFan YujuanDing∗ LiangboNing

wenqifan03@gmail.com dingyujuan385@gmail.com BigLemon1123@gmail.com
TheHongKongPolytechnic TheHongKongPolytechnic TheHongKongPolytechnic
University,HKSAR University,HKSAR University,HKSAR

### ShijieWang HengyunLi DaweiYin

shijie.wang@connect.polyu.hk neilhengyun.li@polyu.edu.hk yindawei@acm.org
TheHongKongPolytechnic TheHongKongPolytechnic BaiduInc,China
University,HKSAR University,HKSAR

### Tat-SengChua QingLi

dcscts@nus.edu.sg csqli@comp.polyu.edu.hk
NationalUniversityofSingapore, TheHongKongPolytechnic
Singapore University,HKSAR

## Abstract 1 Introduction

AsoneofthemostadvancedtechniquesinAI,Retrieval-Augmented Asoneofthemostfundamentaldataminingtechniques,retrieval
Generation(RAG)canofferreliableandup-to-dateexternalknowl- aims to understand the input query and extract relevant inforedge,providinghugeconveniencefornumeroustasks.Particularly mationfromexternaldatasources[24,30,67,140].Ithasfound
intheeraofAI-GeneratedContent(AIGC),thepowerfulcapac- extensive application in various fields [8, 28, 106, 179], such as
ityofretrievalinprovidingadditionalknowledgeenablesRAG search, question answering, and recommender systems. For intoassistexistinggenerativeAIinproducinghigh-qualityoutputs. stance,searchengines(e.g.,Google,Bing,andBaidu)arethemost
Recently,LargeLanguageModels(LLMs)havedemonstratedrevo- successfulapplicationsofretrievalintheindustry;theycanfilter
lutionaryabilitiesinlanguageunderstandingandgeneration,while andretrievethemostrelevantwebpagesordocumentsthatcan
stillfacinginherentlimitations,suchashallucinationsandout-of- matchauser’squery[19,179],enablinguserstofindthedesired
dateinternalknowledge.GiventhepowerfulabilitiesofRAGin informationeffectively.Meanwhile,retrievalmodels,througheffecprovidingthelatestandhelpfulauxiliaryinformation,Retrieval- tivedatamaintenanceinexternaldatabases,canprovidefaithful
AugmentedLargeLanguageModels(RA-LLMs)haveemergedto andtimelyexternalknowledge,therebyservingvitalfunctionsin
harnessexternalandauthoritativeknowledgebases,ratherthan variousknowledge-intensivetasks.Duetotheirpowerfulcapacisolelyrelyingonthemodel’sinternalknowledge,toaugmentthe ties,retrievaltechniqueshavebeensuccessfullyincorporatedinto
generationqualityofLLMs.Inthissurvey,wecomprehensively advancedgenerativemodelsintheeraofAI-GeneratedContent
reviewexistingresearchstudiesinRA-LLMs,coveringthreepri- (AIGC)[77,132,163].Notably,theintegrationofretrievalmodmarytechnicalperspectives:architectures,trainingstrategies,and elswithlanguagemodelshasgivenrisetoRetrieval-Augmented
applications.Asthepreliminaryknowledge,webrieflyintroduce Generation (RAG) [74], which has emerged as one of the most
thefoundationsandrecentadvancesofLLMs.Then,toillustratethe representativetechniquesinthefieldofgenerativeAI,aimingto
practicalsignificanceofRAGforLLMs,wesystematicallyreview enhancethequalityofthegeneratedtextcontentwithretrieved
mainstreamrelevantworkbytheirarchitectures,trainingstrate- information[6,74,77].
gies, and application areas, detailing specifically the challenges ToadvancegenerationmodelsandenhancethegeneratedreofeachandthecorrespondingcapabilitiesofRA-LLMs.Finally, sults,RAGincorporatesinformationorknowledgefromexternal
todeliverdeeperinsights,wediscusscurrentlimitationsandsev- datasources,whichservesassupplementaryfortheinputqueryor
eralpromisingdirectionsforfutureresearch.Updatedinformation thegeneratedoutput[62,103].Specifically,RAGfirstinvokesthe
aboutthissurveycanbefoundathttps://advanced-recommender- retrievertosearchandextracttherelevantdocumentsfromexternal
systems.github.io/RAG-Meets-LLMs/1. databases,whicharethenleveragedasthecontexttoenhancethe
generationprocess[54].Inpractice,RAGtechniquesarefeasible
KEYWORDS andefficienttoapplyinvariousgenerationtaskswithsimpleadaptationoftheretrievalcomponent,requiringminimalorevennoad-

### Retrieval-AugmentedGeneration(RAG),LargeLanguageModel

ditionaltraining[117].Recentstudieshavedemonstratedthegreat
(LLM),Pre-training,Fine-tuning,In-contextLearning,Prompting.
potentialofRAGnotonlyforknowledge-intensivetaskssuchas
theOpen-domainQuestionAnswering(OpenQA)[6,46,109,133],
butalsoforgenerallanguagetasks[48,62,170],andvariousdown-
∗Correspondingauthor:YujuanDing streamapplications[90,163].
1ThisisthelongversionofthesurveytoappearatKDD2024[33]
1
4202
nuJ
71
]LC.sc[
3v11260.5042:viXra

<!-- Page 2 -->

Conference’17,July2017,Washington,DC,USA WenqiFan,YujuanDing,LiangboNing,ShijieWang,HengyunLi,DaweiYin,Tat-SengChua,andQingLi
Output literaturedynamically.MolReGPTleveragesRAGtoenhancethe
Which country won Pre-trained in-contextlearningabilityofChatGPTformoleculardiscovery[77].
the Women's World LLMs
Cup 2023? Prompt ItisalsobeendemonstratedthatRAGcaneffectivelyreducehalluci-
User w/o RAG nationsinconversationaltasks[137,171].AsillustratedinFigure1,
As of my last update

### Output

mpt Context
a
o
n
ut

## L

-o

## L

f

## M

-s
-
c
b
o
a
p
s
e
ed
qu
d
e
ia
ri
l
e
o
s
g
.
s

## W

ys
it
t
h
em
th
w
e
i
h
ll
e
n
lp
ot
of
be

## Ra

ab

## G

le
to
to
re
a
t
n
r
s
i
w
ev
e
e
r
r
w
el
e
e
l
v
l
a
f
n
or
t
i
c
n
a n

## J

'
a
t
n
p
u
r
a
o
r
v
y
i d
2
e
0 2
w
2
h
,
i c

## I

h

### Pro

knowledgefromexternaldatabaseandintegrateitintotheprocess
country won ... 2023. External
ofgeneration,thedialogsystemsucceedsingivingcorrectanswers.

### Query Database

GiventheremarkableprogressinadvancingLLMswithRAG,there

### Spain won the

Women's World Cup Additional information: isanimperativeneedforasystematicreviewofrecentadvancesin

## New, Domain-specific, etc. Retrieval-AugmentedLargeLanguageModels(RA-LLMs).

with RAG

### ThissurveyaimstoprovideacomprehensiveoverviewofRA-


### LLMsbysummarizingrepresentativemethodsfromtheaspectsof

Figure 1: Retrieval-Augmented Generation (RAG) meets thearchitecture,trainingstrategy,andapplicationarearespectively.
LargeLanguageModels(LLMs).Whentheuser’squeryisout- Morespecifically,followingabriefintroductiontothebackground
of-scope,e.g.,unseencontentintrainingdataortheneedfor knowledgeofLLMsinSection2,wereviewexistingresearchfrom
thelatestinformationfortheanswer,LLMsmightshowin- several primary perspectives of RA-LLMs in terms of retrieval,
feriorgenerationperformance.WiththehelpofRAG,LLMs generation,andaugmentationinSection3,aswellasthenecessity
canleverageadditionalrelevantinformationfromexternal andapplicationfrequencyofretrievalinRAG.Then,wesummarize
databasetoenhancetheirtextgenerationcapability. themaintrainingtechniquesofRA-LLMsinSection4andvarious
RA-LLMsapplicationsinSection5.Finally,inSection6,wediscuss
keychallengesandpotentialdirectionsforfutureexploration.
Recentyearshavewitnessedtherapiddevelopmentofpre-trained Concurrenttooursurvey,severalrelatedsurveyshavediversefofoundationmodels,particularlyLargeLanguageModels(LLMs), cusesforRAGandLLMs.Forexample,Zhaoetal.[193]specifically
whichhavedemonstratedimpressiveperformanceacrossvarious reviewmulti-modalinformation-basedRAGtechniquesandZhao
tasks[1,18],includingrecommendersystems[195],moleculedis- etal.[192]discusstheRAGforAIGC.Gaoetal.[41]conductarelacovery[77],andreportgeneration[27].Technically,thegreatsuc- tivelycomprehensiveoverviewofRAGforLLMs.Oursurveydiffers
cessofLLMscanbetechnicallyattributedtotheadvancedarchitec- fromthesesurveysinconcentratingontechnicalperspectivesand
tureswithbillion-levelparameterspre-trainingonahugeamount systematicallyreviewingmodelsaccordingtothearchitectureand
oftrainingcorpusfromvarioussources.Thesetechnicalimprove- trainingparadigminRA-LLMs,aswellasapplicationtasks.
mentshavegivenrisetotheremarkableemergencecapabilities
ofLLMs[194,195],particularlyinlanguageunderstandingand 2 BACKGROUND
generation,in-contextlearning,andothers.Forinstance,GPT-FAR

### Inthissection,webrieflypresentthebackgroundoflargelanguage

introducesdetailedpromptstoteachGPT-4toperformimagetagmodelsandpromptlearning.
ging,statisticalanalysis,andtextanalysisformulti-modalfashion
reportgeneration[27].LLMsalsoachievepromisingperformance
2.1 LargeLanguageModels(LLMs)
inrecommendersystemsbyunderstandingusers’preferencestowardsitems[154,195].Despitethesuccess,LLMsstillsufferfrom Recently,thesignificantbreakthroughofLLMshasrevolutionized
intrinsiclimitations[194,195],suchasthelackofdomain-specific thefieldofartificialintelligence[7,37,194].TheadvancedLLMs
knowledge, the problem of “hallucination”, and the substantial aretypicallypre-trainedonextensivedatawithbillion-levelparamcomputationalresourcesrequiredforupdatingthemodels.These etersandhavedemonstratedtheabilitytounderstandandgenerate
problems are particularly notable in domain-specific fields like human-liketext,leadingtoadvancementsinvariousnaturallanmedicineandlaw.Forinstance,arecentstudyhasdemonstrated guageprocessingtaskssuchastextgenerationandinformation
thatlegalhallucinationsarepervasiveanddisturbing,withhalluci- retrieval [194, 195]. LLMs can be adapted to a variety of downnationratesrangingfrom69%to88%inresponsestospecificlegal streamtasksbyfine-tuningthemonspecificdatasets,allowing
queriesforstate-of-the-artLLMs[21].Moreover,thechallengesof themtospecializeinparticulardomainsorapplications.Ingeneral,
tacklingthehallucinationproblembecomeevenharderduetothe mostexistingLLMscanbebroadlydividedintothreemaincatesubstantialcomputationalresourcesrequiredforfine-tuningLLMs gories:Encoder-only,Decoder-only,andEncoder-Decodermodels.
withdomain-specificorthelatestdata.This,inturn,significantly Encoder-only models, such as the BERT (Bidirectional Encoder
hindersthewidespreadadoptionofLLMsinvariousreal-world RepresentationsfromTransformers)[25]familyofmodels,proapplications. cessinputtextbyencodingitintoahigh-dimensionalspace.The
Toaddresstheselimitations,recenteffortshavebeenmadeto keyfeatureofEncoder-onlymodelsistheirbi-directionalnature,
takeadvantageofRAGtoenhancethecapabilitiesofLLMsinvar- meaningthattheycantakeintoaccountboththeleftandrightconious tasks [6, 53, 62, 135], especially those demanding high for textofeachtokenwhenencodingit.Thisbi-directionalityallows
thelatestandreliableknowledgesuchasQuestionAnswer(QA), Encoder-onlymodelstobetterunderstandthemeaningofwordsin
AI4Science,andsoftwareengineering.Forexample,Lozanoetal. context,whichiscrucialfortaskslikesentimentanalysis,review
[92]introducesascientificQAsystembasedonretrievingscientific reading,andtextclassification[25,169].Incontrasttothesemodels,
2

<!-- Page 3 -->

ASurveyonRAGMeetingLLMs:TowardsRetrieval-AugmentedLargeLanguageModels Conference’17,July2017,Washington,DC,USA

### Citation

>1000 [500, 1000) [200, 500) [100, 200) [50, 100) [20, 50) <20

### RAG Framework/Pipeline

(Iz 2 a F 0 c i 2 D a 1 r ) d, (T I 2 R r 0 i C v 2 e o 3 d T ) i, (S R h E i, P 2 L 0 U 2 G 3) AA 20 R 2 ( 3 Y ) u, SKR 20 ( 2 W 3 a ) ng, ( R Yu E , F 2 E 0 E 2 D 3) (A S s e a lf i, - R 20 A 2 G 3) To 2 C 0 2 (K 3 i ) m,
(Kh k a 2 N n 0 N d 1 - e 9 L l ) M wal, (G R u E u, A 2 L 0 M 20) RAG 20 ( 2 L 0 e ) wis, (K S 2 o E 0 m - 2 F 1 e iD ) ili, (B R o 2 r E 0 g T 2 e R 2 a O ) ud, ( O La p 2 z e 0 a n 2 r B i 2 d o ) o o u k , (K 2 h D 0 a S 2 tt P 2 a ) b, In- R ( 2 C R 0 A o a 2 L n m 3 M te ) , xt R ( E I 2 S T 0 T h E 2 G a R 3 o E ) - , N F ( 2 J L 0 ia A 2 n R 3 g ) E , RA 2 D 0 A 2 3 ( ) Xu, C (Z 2 O h 0 M a 2 n 3 B g ) O , (T S a li n m , 2 P 0 L 2 M 4)

### RAG Learning

REALM RAG (Lewis, E (S M in D g R h 2 , (B R o E rg T e R a O ud, (Iz A a t c la a s rd, ( R s A iri G w - a e r n d d h 2 a e n n a d , RE (W T a R n O g + , + RE IT T E G R E - N Self-RAG ( P Y R a C ng A ,
(Guu, 2020) 2020) 2021) 2022) 2023) 2023) 2023) (Shao, 2023) (Asai, 2023) 2023)

### Retriever Learning

(Kar D p P u R khin, (I F z i a D c - a K r D d, C ( o G n a t u ri t e ie v r e , r (H Fi o D fs -L ta ig tt h e t r, CEIL (Ye, UDR (Li, SAIL (Luo, RADA (Xu, ( R H E u V a E ng N , RA-DIT (Lin,
2020) 2021) 2022) 2023) 2023) 2023) 2023) 2023) 2023) 2023)
EPR 20 ( 2 R 1 u ) bin, U (C 2 P h 0 R e 2 I n 3 S g ) E , Dr.I 2 C 0 L 2 3 (L ) uo, ( L 2 W L 0 a M 2 n 3 - g R ) ,

### Pre-/Post-Retrieval Technique

(Yo S g P a A t L a M ma, ( R G e la 2 s G s, HyPE (Gao, Qu (W er a y n 2 g d , oc SAIL (Luo, RECOMP ( P Y R a C ng A , SlimPLM
2021) 2022) 2022) 2023) 2023) (Xu, 2023) 2023) (Tan, 2024)
(A R g -B ra M w 2 a 5 l, QueryRewriter Ble (W nd a F ng il , ter
2022) (Ma, 2023) 2024)
2019 2020 2021 2022 2023 2024
Figure2:RepresentingRAGandRA-LLMsmethodsorganizedbytheirmaindesignfocus,proposedtimeandimpact(shownby
citation).Notethatthefirstauthorandyearshowninthefigurealongwiththemodelnamecanbeusedtolocatecorresponding
reference.
Decoder-onlymodelsgeneratetextinaleft-to-rightfashion.Asa closely match the form of their pre-training task [20, 110]. For
representativeDecoder-onlymodel,GPT(GenerativePre-trained othermodelslikeGPT,prefixpromptstendtobemoresuitableas
Transformer)[114]predictsthenexttokeninasequencebasedon theymeshwellwiththegenerationtasks[7].However,manually
thecontextprovidedbytheprevioustokens.Theirarchitecture designedpromptsrelyonhumanexperiencewithouteffectiveness
makesthemparticularlyeffectivefortaskslikelanguagegeneration, guarantees. To address this limitation, soft prompt tuning was
codegeneration,andcreativewriting.Encoder-Decodermodels, developedtolearnthetrainablecontinuouspromptembeddings[83,
suchasT5(Text-To-TextTransferTransformer)[116],uniquely 150,151].Forinstance,Prefix-Tuning[83]prependsaseriesofprefix
transformavarietyofNLPtasksintotextgenerationproblems.To embeddingintheinput,whichcanbetrainedandupdated.This
bemorespecific,theencoderinT5processestheinputsequence apportionallowspromptsnottoberealtext,givingmoreflexibility
tocaptureitsmeaning,whilethedecodergeneratestheoutput inthegenerationofprompts.However,duetothelackofdomainsequencebasedontheencodedinformation.ThisT5architecture specificknowledge,themodelmightstillnotgenerateaccurate
iswell-suitedfortasksthatinvolveconvertingonesequenceinto responseswhenfacingnewtasks.
another,suchasmachinetranslation,summarization,andconversationalresponsegeneration.
2.2.2 In-ContextLearning(ICL). Toovercomethelimitationsof
vanillapromptlearning,recentefforts[66,89,191]havedeveloped
2.2 PromptLearning
in-contextlearning(ICL).ICLisaspecificmethodofpromptlearn-
2.2.1 PromptingEngineering. Duetothemassiveparametersof ingthatgivesthemodelafewdemonstrationsoftaskswithinthe
LLMs, prompt learning emerged as a paradigm to leverage the prompt.Thisparadigmallowspre-trainedLLMstounderstandthe
powerofLLMtoimplementvarioustasks[194,195],insteadof patternprovidedbythedemonstrationstosolvenoveltaskswithfine-tuningtheLLMsextensively.Promptlearningcarefullydesigns outtheneedforfine-tuning.Forexample,bycarefullyselectinga
theinputthatguidesthemodeltoperformdownstreamtasksin fewdemonstrations,GPT-3[7]hasshownthecapabilitytoperform
LLMs.Forexample,earlymethods[7,110]providemanuallycrafted few-shottasks[89].ThissuccessindicatesthatLLMshavearemarktemplatestohandlevarioustasksinNLP.Specifically,Encoder-only ableabilitytorapidlyadapttonewtasksbasedontask-specific
modelslikeBERTtypicallyadoptclozepromptsbecausetheyvery knowledge.
3

<!-- Page 4 -->

Conference’17,July2017,Washington,DC,USA WenqiFan,YujuanDing,LiangboNing,ShijieWang,HengyunLi,DaweiYin,Tat-SengChua,andQingLi
Despiteitseffectiveness,ICLusuallyreliesheavilyonthequality Denseretrieval,onthecontrary,embedsthequeryanddocuoftheprovideddemonstrations[143?],whichmayleadtothegener- mentsintocontinuousvectorspacewithcertaincriteria,forexamationofsub-optimaloutputs.Evenworse,ICLmaynothaveenough ple,semanticsimilarity[61].Denseretrievalmethodsareusually
necessaryinformationorpriorknowledgetoguidetheLLMsin trainable,thereforeholdingmoreflexibilityandpotentialinadapgeneratingaccurateresponses.Toaddresstheaforementionedlimi- tation.Asthekeycomponentofdenseretriever,theembedding
tationsofICL,morerecentstudiesintroduceRetrieval-Augmented modelshavedelicatelydifferentdesignsinexistingRAGmodels.
Generation(RAG)technologies[74,117,135].Byintegratingre- Asimpledesign[62,72,165]istodirectlyuseapartofthegenertrievalwithgeneration,RAGmodelsprovideapromisingdirection ationmodelastheembeddinglayeroftheretriever,whichmight
forenhancingtheperformanceandadaptabilityofLLMsacross beabletoenhancethealignmentbetweentheretrievalandgenvarioustasks. eration processes. BERT-based backbone [25] is widely applied
inretrievalmodels.OnecommonretrieverdesigninRAGisto
3 RETRIEVAL-AUGMENTEDLARGE constructtwo-streamencoderswiththeBERTstructure(oneencoderforthequeryandtheotherforthedocuments),whichis

## Languagemodels(Ra-Llms)

alsocalledbi-encoder[135,164].Early-stageRAGmethodstendto

### TheRAGframeworkintheeraofLLMsconsistsofseveralmajor

freeze[6,117]orpartiallyfreeze[74]theparametersoftheretriever
processes:retrieval,generation,andaugmentation,aswellasthe
toperformgeneral-levelrelevantknowledgeextractionandpay
mechanismtodeterminewhethertheretrievalisneeded.Inthis
moreattentiontotheknowledgeleveragingandgeneratorfinesection,wewillintroduceimportanttechniquesinvolvedineach
tuning.Large-scalespecializedpre-trainingfurtherenhancesRAG
process.
modelstoexcelinmoreknowledge-intensivetasks.Onetypical
successisDensePassageRetriever(DPR)[61],whichusesaBERT-
3.1 Retrieval basedbackboneandispre-trainedspecificallyfortheOpenQAtask
GiventhequeryfromtheinputofLLMs,theretrievalprocessin withquestion-answerpairdata.DPRhasshownstrongcapacityas
RAGaimstoproviderelevantinformationfromtheexternalknowl- apre-trainedretriever,facilitatingmanyRAGmodelstosucceedin
edgesources,whichcanbeeitheropen-sourcedorclosed-sourced variousdownstreamtasks[54,74,135,139,141].Ithasalsobeen
as shown in Figure 3. The key component, retriever, as further regardedasthefirststepintheRAGparadigmforimprovingthe
detailedinFigure4,consistsofseveralprocedures,functioningasa performanceofLLMs,whichmayfurtherenhancethealignmentof
wholetomeasuretherelevancebetweenthequeryanddocuments theembeddingsbetweenqueriesandrelevanttextualdatathrough
in the database for effective information retrieval. The specific fine-tuning[16].Arecentstudy[122]hasalsodiscoveredthatDPR
pipelineoftheretrievalisfurtherdeterminedbywhetherthepre- trainingdecentralizeshowknowledgeisstoredinthenetwork,
andpost-retrievalprocessesareincluded.Inthissubsection,wewill creatingmultipleaccesspathwaystothesameinformation.With
introducethemajortechniquesinvolvedintheretrievaloftradi- effectivefine-tuning,bi-encoderretrieversarealsoappliedwidely
tionalandLLM-basedRAGs,includingtheretrievertype,retrieval inICL-basedRAG[82,93,101,111,126,176].Specifically,theyhave
granularity, pre- and post-retrieval enhancement, and database beenmoreoftenusedforsentenceembeddingsimilarity-basedreconstruction. trieval, as well as for some special requirement in ICL, such as
diverseexampleretrieval[176].
3.1.1 RetrieverType. Retrievalmethodscanbegenerallycatego- Anotherstreamofdenseretrievershavingbeenwidelyapplied
rizedintotwotypes:sparseanddense,basedontheinformation inRA-LLMsusesoneencoderonly,whichmaybebasedonTransencodingmethods.Sparseretrievalisword-basedandappliedin former,BERTorotheroff-the-shelfsequencemodelingbackbones.
textretrievalmostly,whiledenseretrievalembedsqueriesandex- Theseone-encoderretrieversaregenerallypre-trainedonlargeternalknowledgeintovectorspacesandcanappliedtovariousdata scaleunaligneddocumentsbycontrastivelearning[122],which
formats. maythereforeexcelfortheirversatility,meaningthattheycan
Asastraightforwardapproach,sparseretrieval,e.g.,TF-IDFand transferandgeneralizebettertonewdomainsortasks.Suchgeneral-
BM25[125,142],usuallyreliesoninvertedindexmatchingalong purposepre-trainedretrievers,e.g.,Contriever[42]andSpider[118],
withtherawdatainput.Forexample,manystudiesdirectlyap- wouldbemoreflexibletouseinLLMstargetingonvarioustasks
ply BM25 for passage-level retrieval to facilitate their RAG [10, andhavedemonstratedtheireffectivenessinmanyRA-LLMmeth-
57,117,168,196,197],wherepassagesarespecificallyrepresented ods,suchasIn-ContextRALM[117],Atlas[55]andSelf-RAG[5].
as a bag of words and ranked based on term and inverse docu- Accordingtoexperimentalresultsinexistingstudies[182],foropenmentfrequencies[54].Ontopofofferingsupplementarytoen- domainQAtasks,whencooperatedwithInstructGPT[107],aphancetheinputofthegenerator,sparseretrievalhasalsobeen plyinggeneral-purposepre-trainedretriever(Contriever)without
usedtofinddemonstrationstofunctioninin-contextlearningfor fine-tuningachievescomparableperformancetosparseretriever
RA-LLMs[2,96,126,138,176].Themainlimitationofapplying (BM25).However,theyarebothworsethantheDPRmodelfinesparseretrievalinRAGisitsno-trainingnature,whichmakesthe tunedontargetdatasets,showingtheeffectivenessoffine-tuning
retrievalperformanceheavilyrelyonthequalityofthedatabase ontargetedtasksanddata.
andthequery.Moreover,suchfixedterm-basedmethodsonlysupportsimilarity-basedretrieval,whilecannotbeadaptedforother 3.1.2 RetrievalGranularity. RetrievalgranularitydenotesthereretrievalcriteriapossiblyexistinginLLMapplications,suchasthe trievalunitinwhichthecorpusisindexed,e.g.,document,passage,
diversity[31]. token,orotherlevelslikeentity.ForRAG,thechoiceofretrieval
4

<!-- Page 5 -->

ASurveyonRAGMeetingLLMs:TowardsRetrieval-AugmentedLargeLanguageModels Conference’17,July2017,Washington,DC,USA
Sympton: I had very bad cardiac pain this morning, also felt dizzy and nauseous. It lasted for a few minutes.
Patient file: female, 34 years old, height: 170cm, weight: 55kg,...

### Pre-retrieval Enhancement

... The first Input-layer Generator According to

### Augmentation

symptom your sympton
Rewrite Expand sign of and conditions,
a heart OR you are likely
attack is having Coronary
sudden
Retriever A pe n c a c g a r t i r o r n e d r a s i i s a t. c is Output-layer Generator A (C rt A e D ry ) . D C is A e D a s is e
caused by Augmentation
caused by
a decrease
plaque buidup in
in
myocardial OR the wall of the
Post-retrieval Enhancement blood flow. arteries that
supply blood to
... Intermidiate-layer the heart (called

### Generator


### Augmentation coronary

Filter Compress arteries)....
Figure3:IllustrationofthebasicRetrieval-AugmentedLargeLanguageModels(RA-LLMs)frameworkforaspecificQAtask,
whichconsistsofthreemaincomponents:retrieval,augmentation,andgeneration.Retrievalmayhavedifferentprocedures
withvariousdesigns,whichoptionallyincludespre-retrievalandpost-retrievalprocesses.Theretrieveddocumentsarefurther
leveragedingenerationwiththeaugmentationmodule,whichmaybeatdifferentintegrationstages.
Dense Retrieval moreburdenforthedatabasesaving.Tokenretrievalismoresuitableincasesrequiringrarepatternsorout-of-domaindata[62],

### Relevance Scoring

meanwhilecooperateswellwiththeevery-tokenretrievalstrategy
asappliedinkNN-LMandothersimilarwork[47,104,180].In

### Embedding

comparison,atextchunkmaycontaincompactandcompleteinfor-

### Query

Retrieved Results mationwithlessredundancyandirrelevancy,thereforebecoming

### Chunking/ (Chunks/Documents/

Tokenizing/ Indexing Tokens/Entities/..) themainstreamretrievaltextgranularityinRAG.
Database ... AnothermajorretrievalgranularityproposedinRAGisentity
retrieval.Unliketheabovetypesofgranularity,entityretrievalis

### Relevance Scoring

designedfromtheperspectiveofknowledgeratherthanlanguage.
Sparse Retrieval Févry et al. [39] introduce the Entities as Experts (EAE) model,
whichdividestheparameterspaceoflanguagemodelsaccording

### Figure4:IllustrationoftheretrieverinRA-LLMs,whichcan

totheentityidentity.TheproposedEAEmodelaimstolearnentity
beimplementedineitherdenseorsparsemanners,eachwith
representationsfromthetextalongwithothermodelparameters
severalkeyoperations.
withtheWikipediadatabaseandrepresentknowledgewithentity
memory.Atamorefine-grainedlevel,deJongetal.[22]proposeto
buildtheknowledgebasebylearningandretrievingmentionrather
thanentity.Overall,applyingentityormention-levelretrievalin
granularitycansignificantlyimpacttheoverallperformanceofthe

### RAGwouldbemoreeffectiveforentity-centrictasks,andmore

modelintermsofeffectivenessandefficiencyastheydetermine
efficientinspacecomparedtotoken-wiseretrieval.
thesavingspaceforthedatabaseaswellasthecomputationalcost
forsearching[4].Earlystageretrieval-augmentedlanguagemod- 3.1.3 Pre-retrievalandPost-retrievalEnhancement. Toensurethe
els[10]proposetoretrievewholepiecesofdocuments,andthen retrievalquality,i.e.,increasetheaccuracyandrelevanceofthereapplyamachinecomprehensionmodeltrainedtodetectanswer trievedresults,variouspre-andpost-retrievalstrategieshavebeen
spansinthereturneddocuments,whichfocusesmoreonlanguage proposedtofurtherenhancetheinputandoutputoftheretriever.
readingandkeyinformationlocatinginthedocument.Ingener- Wangetal.[156]proposeaqueryexpansionapproachQuery2doc,
ativelanguagemodels,Chunkretrieval(alsocalledpassagesin whichgeneratespseudo-documentsbyfew-shotpromptingLLMs
somereferences[46,57,61])iscommon,whichhasbeenusedin andexpandsthequerywiththerelevantinformationinpseudobothtraditionalandLLM-basedRAGmodelssuchasREALM[46], documentstoimprovethequerydisambiguationandguidethe
RAG[74]andAtlas[55].Amorefine-grainedretrieval,i.e.,token retrievers.Theyhaveempiricallydemonstratedthatsuchamethod
retrieval,insteadcanbedonewithfastersearchingbutwillbring canboosttheperformanceofboththesparseanddenseretriever[61]
5

<!-- Page 6 -->

Conference’17,July2017,Washington,DC,USA WenqiFan,YujuanDing,LiangboNing,ShijieWang,HengyunLi,DaweiYin,Tat-SengChua,andQingLi
onad-hocinformationretrievaldatasets.Similarly,Gaoetal.[40] querygenerationblendingandthepost-retrievalknowledgefilterproposeHypotheticalDocumentEmbedding(HyDE)method,which ing.Thismethodcantacklethecomplexquestionsaswellasthe
instructsanLLMtogeneratehypotheticaldocumentsforthegiven noisyretrievedknowledgeproblems,thereforecomprehensively
query.Thehypotheticaldocumentsarethenusedasnewqueries enhancingtheRA-LLMperformance.
togetembeddedandsearchforneighborswiththedenseretriever. More recently, advanced RAG pipelines have been proposed
Anotherpre-retrievalstrategy,queryrewrite[98],aimstoclose usingLLMstogeneratereasoningpathsandplanswiththeInforthe gaps between the input text and the needed knowledge in mationRetrieval(IR)moduletoiterativelyretrieveknowledgeto
retrieval,toreformulatetheoriginalquestionintoamoreconducive enhanceLLM-basedgeneration[130,172,175].However,Zhuetal.
versiontoretrieve.Specifically,Maetal.[98]proposetheRewrite- [198]pointoutthatiftheoutputsofIRandLLMarelow-quality,
Retrieve-Readframework,whichpromptsanLLMtogeneratethe theretrievalandgenerationprocesseswillgethinderedbyeach
queryfortheretrievalfunction.Themotivationoftherewriting otherwithsuchaniterativeguidancepipeline.Toovercomethis
stepistoclarifytheretrievalneedinthenewquerytoeasethe barrier,theyproposeanewreasoningapproachforqueryandreburden on the retrieval function to comprehend the input and trievedknowledgeenhancement.Post-retrievalstrategiesmayalso
enhancetheoutput,i.e.,retrievedrelevantinformation.Theyhave functiontoenhancethecompatibilitybetweentheretrievedresults
testedboththesettingsofusingafrozenLLMandatrainablemodel andthegenerationmodels.Forexample,oneofthemainlimitations
tobetherewriter,bothoutperformingnaiveRAGorgeneration ofexistingLLMsisthelengthoftheinputtokens,whichprevents
models,demonstratingdiverseperformanceondifferenttestedQA longretrieveddocumentsbeingdirectlyincorporatedintoexistdatasetsthough.Tanetal.[146]alsoformulateaqueryrewriting ingRA-LLMs.Forthislimitation,Xuetal.[168]proposeRetrieve,
strategyintheirmodelthatdecomposestheheuristicanswerfrom Compress,Prepend(RECOMP),whichaddsanintermediatestep
aproxygenerationmodelintodistinctclaims. toprocesstheretrieveddocumentsintoatextualsummarybefore
Yuetal.[183]proposequeryaugmentationtocombinethe in-contextaugmentationinthegenerationprocess.Fromanother
originalqueryandthepreliminarygeneratedoutputsasanew perspective,longretrievedpassagelistleadstoahighinference
query,whichisfurtherusedtoretrieverelevantinformationfrom latencywhenusingauto-regressivedecodingatgenerationstage,
theexternaldatabase.Theretrievedresultscaninspirethelanguage whichhurtsthemodel’sefficiency.Forthislimitation,Hofstätter
modeltorethinkthegeneratedresultsandenhancethem.Com- etal.[50]proposealightversionofFiDmodelthatcompressesthe
paredtoapplyingonlytheoriginalquery,suchaugmentationmay encodedvectorsperretrievedpassagebeforeconcatenatingand
contributemorerelevantinformationretrievedfromthecorpusfor feedingthemthroughthedecoderandalsoincludesare-rankeron
thedirectlyclarificationofquery-outputrelationships.Including theretrievedresultsbeforeapplyingtheminthegeneration.
initialoutputinthenewqueryfurtherenhancesthelexicaland
3.1.4 Database. RetrievalinRAGisconductedbasedonexternal
semanticoverlapbetweenthesupportingdocumentstoberetrieved
knowledgesource,whichcanbeaclosed-oropen-sourced[98,100],
withthegivenquestion.QueryaugmentationachievesoverallbetasillustratedinFigure3.Closed-sourceddatabasegenerallystores
terperformanceamongthesequeryenhancementstrategiessinceit
key-valuepairsforknowledge,whichcanbeconstructedinvarious
mayprocessallretrievedknowledgecollectivelywhilegenerating
ways.Thekeysareprimarilyusedforsimilaritymatching,beingas
answers[155].
sparsevectorssuchasinBM25ordenseembeddingsfromthere-

### Post-retrievalenhancementdenotestheproceduretoprocess

trievalencoding.Thevaluedependsonthespecificretrievaltarget,
theextractedtop-kdocumentsfromtheretrieverbeforefeeding
whichisrawtextinmostcases[6,46,54,72,74,129].Forexample,
themtothegeneratorforthesakeofbetteralignmentbetweenthe
eachWikipediaarticleissplitintodisjoint100-wordchunks,to
retrievalandgenerationstages[173],particularlyforclosed-source
makeatotalof21MdocumentsinearlyRAG[74].Eachdocument
generatorssuchasLLMs.Forexample,Yangetal.[173]propose
isencodedbyadenseembeddingandsavedinthedatabaseasthe
thePluggableReward-drivenContextAdapter(PRCA)thatenables
valueandkey,respectively.Thevaluecanstoretokenstoo,one
tofine-tunethelightweightadapterinsteadofthegeneratoron
foreachasappliedinkNN-LM[62]andSPALM[180].Thesource
specificdatasets.Italsodistillstheretrieveddocumentsthroughreofthedatabasedependsonthespecificapplicationdomainsand
inforcementlearningwiththerewardsresultingfromthegenerator.
Glassetal.[44]proposeRetrieve-Rerank-Generate(R2G)method, tasks.WikipediaisoneofthemostcommonlyappliedgeneralretrievalsetsinpreviousRAGwork,whichstoresfactualstructured
whichassemblestheretrieveddocumentsofdifferentretrievalapproacheswiththererankoperationtoboosttherobustnessofthe
retrievalresults.Anotherconsiderationforapplyingpost-retrieval 1Retrievers:[BE:Bi-Encoder(alsoreferredasdualencoder),OE:One-Encoder,BT:
BERT-style Transformer, GP: Partial Generation, SE: Search Engine, SR: Sparse
enhancementisthattheretrievedinformationmaysometimesbeir-
Retrieval, DPR:[61]], Generators: [DT: Decoder-only Transformer, ET: Encoderrelevantorcontainnoise,whichmightnothelpwiththegeneration only Transformer, ED: Encoder-Decoder], Pre-/Post-Retrieval techniques: [RQG:
modelforthetask,orevenworse,harmthegenerationprocess[159]. RetrievalQueryGeneration,QE:QueryExpansion,(T)RR:(Trainable)Re-Ranker,
TRA:TrainableRetrieverAdaptor,CR:CandidateRetrieval,CM:CriticModel],Aug-

### Wangetal.[159],Asaietal.[5],Yuetal.[183]proposedifferent

mentations:[Output:Output-layerIntegration,Input:Input-layerIntegration,Inter:
strategiestomitigatethenoiseinretrievedknowledgedocuments. Intermediate-layerIntegration,Demon:Asdemonstration],Tasks:[AQA:Abstractive
However,Xiongetal.[166]empiricallystudiedthatthesemethods QuestionAnswering,QG:QuestionGeneration,NQ:NaturalQuestions,WQ:WebQuestions,CT:CuratedTrec,FV:FactorVerification,TQA:TriviaQA,WizInt:Wizard
aredependentontheLLM’sconfidencelevels,whichmightnot oftheInternettask,WoW:WizardofWikipediatask,MHQA:Multi-hopQA,CQA:
beaspreciseasexpected.Forthisproblem,Wangetal.[155]pro- ConversationalQA,EL:EntityLinking,SF:Slot-filling,MMLU:Massively-Multitask
LanguageUnderstanding,CR:CommonsenseReasoning,LongQA:Long-formQA,OS:
poseBlendFilter,whichsimultaneouslyconsidersthepre-retrieval
Open-domainSummarization,BG:BiographyGeneration,UR:UtteranceRepresenting,
RF:RetrievalFusion]
6

<!-- Page 7 -->

ASurveyonRAGMeetingLLMs:TowardsRetrieval-AugmentedLargeLanguageModels Conference’17,July2017,Washington,DC,USA
Time Model Cite Retriever RetTrain RetAug Pre-/Post- Generator Aug Evaluation

### Stage Retrieval

2019 kNN-LM[62] 619 DR(GP) No Inf RA DT Output LG
2020 REALM[46] 1437 DR(BE,BT) Yes PT+FT / ET Input OpenQA(NQ,WQ,CT)
2020 RAG[74] 2125 DR(DPR) Yes FT / ED(BART) Input OpenQA, AQA, JeopardyQG,FV
2021 FiD[54] 780 SR(BM25)/ No FT / ED(T5/BART) Input OpenQA

## Dr(Dpr)

2021 SE-FiD[68] 286 SE(Bing) No Inf RQG FiD Input WizInt,WoW
2021 FiD-KD[53] 190 DR(BE) Yes FT CR FiD Input OpenQA
2021 RETRO[6] 683 DR(BERT, No PT / ED Inter LM,OpenQA

## Dpr)

2021 EPR[126] 384 DR(DPR) Yes Inf CR GPT-3,J,Neo, Demon UR

## Codex

2022 OpenBook[70] 145 SE+SR No QE GOPHERLM Input QA,FV
2022 DSP[63] 117 ColBERTv2 No Inf RQG,RF GPT-3.5 Demon OpenQA,MHQA,CQA
2023 In-Context 211 DR/SR No Inf TRR GPT-2,J,Neo Input LM,OpenQA

## Ralm[117]

2023 Atlas[55] 367 DR(OE) Yes PT+FT / ED Input OpenQA, FV, WoW,

## El,Sf,Mmlu

2023 FLARE[57] 133 SR(BM25)/ No Inf RQG GPT-3.5 Input MHQA, CR, LongQA,

### SE(Bing) OS

2023 IRCoT[149] 114 SR(BM25) No Inf / GPT-3,Flan-T5 Input OpenQA
2023 Self-RAG[5] 85 DR(OE) No FT CM tunableLLM OpenQA,LongQA,FV,

## Bg

2023 REPLUG[135] 48 DR(BE) Yes FT TRA GPT-2,3 Inpput MMLU,OpenQA
2023 UDR[80] 42 DR(DPR) Yes FT CR GPT-Neo Demon 40NLPtasks
2023 ITER- 40 DR(DPR) Yes FT RR InstructGPT, Input MHQA,FV,CR

### RETGEN[130] Llama-2

Table1:Basicpublicationinformationandmaintechnicaldesignsofhigh-impactRAGandRA-LLMmodels.1
informationandhasseveralversionsdifferinginscale,frombillion 3.2 Generation
token-level[22,39,46,62,74,117,135,168,180]totrilliontoken- Thedesignofthegeneratorheavilydependsonthedownstream
level[6].Domain-specificdatabaseisalsousedfordownstream tasks.Formosttextgenerationtasks,Decoder-onlyandEncodertasks.Forexample,forthecodegenerationtask,Zanetal.[185] Decoderaretwodominantstructures[194].TherecentdevelopcollectAPIinformationandcodefilesofpubliclibrariestobuild mentofcommercialclosed-sourcedlargefoundationmodelsmakes
theirAPIretrieverdatabase.Inaddition,Zhouetal[197]propose black-boxgenerationmodelsmainstreaminRA-LLMs.Inthispart,
touseadocumentationpoolfrequentlyupdatedwithnewcontent we will briefly review studies with these two types of genera-
(newlyreleasedlibraries)intheirmodel. tors:parameter-accessible(white-box)andparameter-inaccessible
ApplyingInternetsearchingengine[95]suchasBingandGoogle (black-box).
avoidsthemaintenanceofthesearchindexandcanaccessup-todateknowledge[68,70].Meanwhile,itprovidesabroaderknowl-
3.2.1 Parameter-AccessibleGenerators(White-box). Thestructure
edge base than the closed-sourced database [5, 70]. It can also ofEncoder-Decoderprocessestheinputandthetargetindependently
providehigh-qualityrankingafterbeingtunedoverdecadesof
withdifferentsetsofparameters,inwhichacross-attentioncompouse.Internetsearchhasbeenwidelyincorporatedwithblack-box
nentisdevelopedtoconnectinputtokenstotargettokens.Repre-
LLMsandshowseffectivenessfordifferentfunctionssuchasknowlsentativeEncoder-DecodermodelsincludeT5[116]andBART[73].
edgeaugmentation[70],fact-checking[100]andLLMagenten- Incomparison,Decoder-onlymodelsprocessinputsandtargetsafter
hancement[175].ComparedtotraditionalRAG,Internetsearch
concatenation,whichmakestherepresentationsofthetwoparts
hasbeenleveragedmoreastheretrieverinRA-LLMsowingto
concurrentlybuiltlayer-by-layerastheypropagateupthenetwork.
theextraordinarycapabilityofLLMstobetheReadertocompre-

### ThesetwotypesofgeneratorsarewidelyappliedinexistingRAG

hendthesearchingresults,i.e.,theretrieveddocuments,aswell work.Forexample,RAG[74]andRe2G[44]employBART;FID[54]
asLLMs’abilitytousetoolstoprocessandanalyzethethem[98]. andEMDR2utilizeT5.Thereareothermodels[6,84]leveraging
Existingstudies[182]haveshownthatleveragingsearchengines

### Transformer-basedEncoder-Decoderarchitecturebutwithsome

(e.g.,InstrucGPT)isparticularlyeffectiveforLLMsonzero-shot
customizeddesign.GeneratorsinRAGdifferthemselvesfromgenknowledge-intensivetaskssuchasOpenQAandfactchecking.
eralonesbyincorporatingretrieveddatatoenhancethegeneration
7

<!-- Page 8 -->

Conference’17,July2017,Washington,DC,USA WenqiFan,YujuanDing,LiangboNing,ShijieWang,HengyunLi,DaweiYin,Tat-SengChua,andQingLi
accuracyandrelevance.Furthermore,white-boxgeneratorsallow MorespeciallyforLLMs,input-layerintegrationmayusethe
parameteroptimization,whichcanbetrainedtoadapttodifferent retrievedcontentas(additional)promptsordemonstrationsontop
retrievalandaugmentationapproachesforabetterperformanceof ofusingitassupplementarytotheoriginalinputasintraditional
generation. RAGs[126].Promptretrievalaimstofindsuitablenaturallanguage
promptsautomaticallythroughretrievaltoteachtheLLMtolearn
3.2.2 Parameter-InaccessibleGenerators(Black-box). Acertainproincontext[7]ortoinducetheLLMtoreason[162].Itmayboost
portionofLLMsarereleasedwithoutthedisclosureofinternal
thezero-shotabilityofLLMswithoutdelicatepromptengineering.
structuresortheaccessibilityofparameters,especiallythosepar-
Forexample,Chengetal.[16]proposetolearnapromptretriever
ticularlylarge-scaleonessuchasGPTseries[1],Codex[12]and
basedontheinput-promptpairdatawithscorelabelsresulting
Claude,whicharecalledblack-boxgenerationmodels.ThesegenfromafrozenLLM.
eratorsonlyallowtheoperationsoffeedingqueries(input)andreceivingresponses(output)whilenotallowingtheinternalstructure
3.3.2 Output-LayerIntegration. Anotherkindofaugmentationis
tobealteredorparameterstobeupdated.Fromanotherperspecpost-hoc,i.e.,output-layerintegration,whichjointsretrievaland
tive,LLMs,eventhoseopenforfine-tuning,arelargeinscaleand
generation results. For example, kNN-LM [62] interpolates two
difficulttotunefordownstreamdomain-specifictaskswithonlya
next-tokendistributionsinprediction:oneinducedbytheLMand
limitedamountofdata.Black-boxRA-LLMs,therefore,focusmore
theotherinducedbythenearestneighborsfromtheretrievalcorontheretrievalandaugmentationprocesses,tryingtoenhance
pus.Output-layerlinearintegration[45,196]isflexibletoapply
thegeneratorbyaugmentingtheinput(alsocalledpromptinthe
sinceitcanbepluggedintomostgenerationmodelswithoutaddicontextofLLMs)withbetterknowledge,guidance,orexamplesfor
tionaltraining.However,thesimplicityofoutput-layerintegration
thegeneration.Forexample,Rubinetal.[126]proposestotraina
alsolimitsthemodel’sabilitytoreasonabouttheretrievedtext.
promptretrieverwiththedatalabeledbylanguagemodelsthem-

### Totacklethislimitation,Yogatamaetal.[180]proposetoaddan

selves,whichcanbeusedtoprovidebetterexamplesforin-context
extragatingnetworktopost-processtheretrieveddataandachieve
learning,thereforeenhancingthefinalgenerationperformance.Xu
comparativelybetterperformance.ForLLMs,output-layerinteetal.[168]proposetocompresstheretrieveddocumentsbefore
grationisasreasonableandadaptiveasinput-layerintegration.
in-contextintegration,whichcanreducethecomputationalcosts

### REFEED[183]proposesananswerrefiningmechanismthatapplies

andalsorelievetheburdenofLMstoidentifyrelevantinformation
anLLMtoevaluatetheretrievedinformationandadjusttheinitial
inlongretrieveddocuments.
answeraccordinglytoenhancetheaccuracyoftheresponse.Similarly,Zhangetal.[190]proposetheCOMBOframework,which
3.3 RetrievalIntegrationforGeneration
matchesLLM-generatedpassageswithretrievedcounterpartsinto
Augmentation compatiblepairsbasedonpre-traineddiscriminators.Thepassage
pairsarethenhandledbyaFusion-in-Decoder-based[54]toderive
Augmentationdescribesthetechnicalprocessthatintegratesreafinalanswer.
trievalandgenerationparts,whichistheessentialpartofRA-LLMs.

### Inthissubsection,weintroducethreemaindesignsofaugmenta-

3.3.3 Intermediate-LayerIntegration. Comparedtotheabovetwo
tion,whichareconductedattheinput,output,andintermediate
non-parametricapproaches,amoreengagingaugmentationisto
layersofgeneratorrespectively,asillustratedinFigure3.
designasemi-parametricmoduletointegratetheretrievedresults
3.3.1 Input-LayerIntegration. Acommonwaytointegrateretrieved throughtheinternallayersofthegenerationmodel,whichiscalled
information/documentsistocombinethemwiththeoriginalin- intermediate-layerintegration.Suchintegrationmightaddaddiput/queryandjointlypassthemtothegenerator,whichiscalled tionalcomplexityandispromisingtoenhancethecapabilityofthe
input-layerintegration.Forexample,In-ContextRALM[117]ap- generationmodelwitheffectivetraining.Typically,aTransformer
pliesinput-layerintegrationbyspecificallyconcatenatingtheorigi- module is introduced to leverage retrieved information (mostly
nalinputandallretrieveddocumentsintoasinglesequenceasthe encodedintodenserepresentations)intothegenerationmodelto
newinputforthegenerationmodel.Despitetheeffectiveness,such interactwiththerepresentationsinthemiddlestageofthegeneraintegrationislimitedtothenumberofretrieveddocuments,since tion.Forexample,RETRO[6]introducesaChunkedCrossAttention
theconcatenatednewinputmaybetoolongtobeprocessedby (CCA)layertoprocesstheretrievedchunksinthegeneratorblocks,
thegenerationmodel.In-contextRALMspecificallyalleviatesthis andWuetal.[165]introducesthekNN-AugmentedAttentionLayer.
limitationbyremovingtokensfromthebeginningofthenewin- Similarly,EAE[39]andTOME[22]useEntityMemoryandMemput.Toavoidinformationlosswithsuchatokenremovingstrategy, oryAttentionlayertoincorporatetheretrievedEntityandEntity
FID[54]employsadifferentintegrationmethodthatprocesseseach Mentions,respectively.Suchintermediate-layerintegrationcan
retrieveddocumentindependentlyintheencoder.Thisstrategy usemanyblocksfrequentlyandefficientlytoenhancethecapaisscalabletoalargenumberofcontextsasitonlyperformsself- bilityofthewholeRAGmodel.Itoffersanefficientalternativeto
attentionoveronecontextatatimeinthefollow-upprocessing. incorporatealargenumberoftextchunksfrequentlyretrieved,
Atlas[55]andREPLUG[135]applyasimilarparallelintegration whicharechallengingtoprocesswithinput-layerintegrationdue
byconcatenatingthequeryandoneretrieveddocumentatatime. totheinputlengthlimitofLMs[6].However,italsoneedstobe
Ingeneral,mostblack-boxgeneration-basedRAGmethodsapply notedthatintermediate-layerintegrationrequireshighaccessto
input-layerintegrationsinceneithertheintermediatelayerofthe thegenerationmodels,whichisnotfeasibleformostLLMsthat
generationmodelortheoutputdistributionisaccessible. areaccessiblethroughinferenceAPIs[98].
8

<!-- Page 9 -->

ASurveyonRAGMeetingLLMs:TowardsRetrieval-AugmentedLargeLanguageModels Conference’17,July2017,Washington,DC,USA
3.4 RetrievalAugmentationNecessityand cases,pre-retrieveddocuments(throughone-timeretrieval)might
Frequency notbeenoughtosupportthegenerationofthewholesequenceof
output,whichcallsforin-generationretrievaloperations.Tothis
TheretrievaloperationinLLM-basedgenerationgenerallyaimsto
end,In-ContextRALM[117]andRETRO[6]applyevery-n-token
supplementknowledgetoenhancegeneration.Althoughretrievalretrievalintheprocessofgenerationforbetteraugmentation.In
augmentedmodelshaveemergedpromising,theyhavebeencriticomparison,kNN-LM[62]adoptsamorefrequentretrievalstratcizedfornotbeingauniversalsolution[75,109]asindiscriminately
egy,whichretrievesinformationforthepredictionofeverytoken
augmenting LLMs with irrelevant passages can override potenduringthegeneration.Overall,applyingdifferentfrequenciesofretiallycorrectknowledgealreadypossessedbyLLMsandresultin
trievalcanimpactboththeeffectivenessandefficiencyofthewhole
incorrectresponsesinstead[99].Thakuretal.[147]contributea
RAGmethod.Forexample,morefrequentretrievalleadstobetter
human-annotateddatasettohelpevaluatetherobustnessofLLMs
performancebutalsoincreasesthecomputingcost[117].Choosing
againsterrorsinexternalretrievedknowledgeandobservethat
retrievalfrequencyisalmostatrade-offbetweencomputingcost
LLMsmaydoublethehallucinationrateonthenon-relevantreandperformance.
trievedpassagesthanontherelevantones.Therefore,itiscritical
forRA-LLMstoaccuratelyrecallthepriorknowledgewhileselec-

## 4 Ra-Llmstraining

tivelyincorporatingretrievedinformationonlywhennecessary,
whichisthepathtorobustRA-LLMs. Basedonwhethertrainingisrequiredornot,existingRAGmethods
Mostexistingmethodsdeterminethenecessityofretrievalbased canbecategorizedintotwomainclasses:train-freeapproaches
onthepreliminaryanswersofLLMsortheirinternalreasoning andtraining-basedapproaches.Training-freemethodsusually
results [102, 117]. For example, Self-RAG [5] introduces special directlyleveragetheretrievedknowledgeduringinferencetime
tokenstoassessthenecessityofretrievalandcontrolretrievalbe- withoutintroducingextratrainingbyinsertingtheretrievedtext
havior.Othermethodsdesigniterativepromptstodecideifextra intotheprompt,whichiscomputationallyefficient.However,one
informationisrequiredduringgeneration,whichtherebyneedsto potentialchallengeisthattheretrieverandgeneratorcomponents
invokeretrievalorotheractionsforLLMs[162,175].Wangetal. arenotspecificallyoptimizedfordownstreamtasks,whichcould
[159]proposeSelf-KnowledgeguidedRetrievalaugmentation(SKR) easilyleadtosub-optimalutilizationoftheretrievedknowledge.
method,whichusesLLMsthemselvesorexplicitsmalltrainable To fully exploit the external knowledge, extensive methods are
modelstoofferself-knowledgeasthereferencefortheadaptive proposedtofine-tunetheretrieverandgenerator,therebyguiding
callingofaretriever.IntraditionalRAGs,retrievalnecessityjudg- largelanguagemodelstoeffectivelyadaptandintegrateretrieved
menthasalsobeenexploredandproposedtoaddressbyintuitive information[127,128,130,135,153,199].
approachessuchasassessingtheconfidenceofthelogitsproduced Accordingtothetrainingstrategies,wecategorizethesetrainingbythegenerationmodels[47,56,59].Suchasolutionisalsoappli- basedapproachesintothreeclasses:1)IndependentTraining
cabletoRA-LLMs,forexample,FLARE[57]dynamicallytriggers approachesindependentlytraineachcomponentintheRAGproce-
RAGiflogitsarelowerthanaspecificthreshold.Tanetal.[146] dure,2)SequentialTrainingmethodstrainonemodulefirstand
introduceamoreflexiblemodelSlimPLM,whichdetectsmissing freezethewell-trainedcomponenttoguidethetuningprocessof
knowledgeinLLMswithaslimproxymodel,whichfunctionsto theotherpart,and3)JointTrainingapproachestrainretriever
generatea“heuristicanswer”.The“heuristicanswer”isusedto andgeneratorsimultaneously.Inthefollowingsection,wewill
assessthenecessityofretrievalandfacilitatetheretrievalprocess comprehensivelyreviewthetraining-free,independenttraining,
forqueryrewritingwhennecessary. sequentialtraining,andjointtrainingmethods.Thecomparisonof
IntraditionalRAGsthatrarelyconsiderretrievalnecessity,re- thesedifferenttrainingmethodsisdepictedinFigure5.
trievalfrequency(alsocalledretrievalstride)isanimportantdesign
aspecttodeterminethedegreeofusingtheretrievalinthegen- 4.1 Training-free
eration,therebygreatlyaffectingtheoverallperformanceofRAG
Withthehugenumberofparameters,LLMshaveexhibitedhumanmodels[117].Retrievalfrequencycontrolshowmuchtorelyonthe
levelintelligenceandachievedpromisingpredictionperformance
retrievalresults,therebyaffectingboththeefficiencyandeffectiveonvariousdownstreamtasks.However,itisextremelychallenging
nessofthemodel.Whenthenecessityofretrievalisnotconsidered,
tofrequentlyperformfine-tuningandupdatetheknowledgestored
retrievalfrequencyisoftenpre-definedandfixed,whichhavethree
in the model parameters [74] due to the considerable time and
commonsettings:one-time,every-n-token,andevery-token.Onecomputationalresourcesrequired.Recently,numerousstudieshave
timeretrievalinvokestheretrievalfunctiononlyonceandtriesto
suggestedenhancingLLMswithretrievalmechanisms,enabling
findalldesiredinformationinthatone-timeoperation.One-time
themtodynamicallyacquirenewknowledgefromexternalsources
retrievalisusuallyoperatedatthebeginningofthegenerationprowithout extra training processes (i.e., training-free) [54, 57, 63],
cess,andthenprovidesallretrieveddocumentstothegeneration
instead of relying solely on the implicit knowledge encoded in
modelsalongwiththeoriginalinput,asappliedinREALM[46].
themodel’sparameters.Theseapproacheshaveshownsignificant
One-timeretrievalismoresuitableforthecasesthattheinformaperformanceimprovementforvariousknowledge-intensivetasks,
tionneedsinexternaldatabasesareobvioustoLLMs[57].However,
suchasopen-domainquestionanswering[74].Accordingtothe
forlanguagetasksrequiringlong-formoutputsuchasopen-domain
differentwaysinwhichLLMsutilizeretrievedinformation,wecatsummarization,thedependencyamongthetokensintheoutputis
egorizethesetraining-freemethodsintotwocategories:1)Prompt
moreimportanttobeconsideredduringthegeneration.Inthese
Engineering-basedMethodsintegrateretrievedknowledgeinto
9

<!-- Page 10 -->

Conference’17,July2017,Washington,DC,USA WenqiFan,YujuanDing,LiangboNing,ShijieWang,HengyunLi,DaweiYin,Tat-SengChua,andQingLi

### Training-Free


### Sequential Training

Retriever Datastore 1. Retriever First
Retriever Datastore
Large Language
Input Output

### Models


### Retriever Datastore


### Independent Training


## Independent Training of Retriever Large Language

Input Output

### Models

Retriever Datastore

## LLMs First


## Independent Training of LLMs Input Large Language Output


### Models

Large Language
Input Output

### Models

Large Language
Input Output

### Models


### Joint Training

Retriever Datastore

### Retriever Datastore

Input Large Language Output Frozen Forward
Models Retrieved Documents

### Trainable Backward

Figure5:AnillustrationofdifferenttrainingmethodsinRetrieval-AugmentedLargeLanguageModels(RA-LLMs).ExistingRA-
LLMsapproachescanbecategorizedintotwoclasses:training-freeapproachesusuallydirectlyleverageretrievedinformation
duringtheinferencetimebyintegratingtheretrievedknowledgeintotheprompt,andtraining-basedapproachesfine-tunethe
retrievalandgeneratortoenhancethegenerationperformance.Basedonthetrainingstrategies,training-basedmethodscan
befurthercategorizedintothreegroups:independenttraining,wheretheretrievalandgeneratorcomponentsaretrained
independently;sequentialtraining,wheretheyaretrainedsequentially;andjointtraining,wheretheyaretrainedjointly.
theoriginalpromptdirectly,and2)Retrieval-GuidedTokenGen- answeragivenquestionbasedontheirinternalknowledge,enerationMethodsretrieveinformationtocalibratethetokengen- ablingflexibleutilizationofbothinternalandexternalknowledge
erationprocess. byselectivelycallingtheretriever.TOC[65]firstretrievesrelevant
knowledge for ambiguous questions and recursively constructs
4.1.1 PromptEngineering-basedMethods. AstheLLMs’generation atreestructurebyclarifyingambiguousquestionsintomultiple
performancehighlydependsontheinputquery,numeroustraining- disambiguatequestions,whichisfurtheraggregatedtogenerate
freeRAGapproachesemployexternalknowledgebyrefiningthe long-formanswers.
originalprompts[57,63,81].Specifically,theretrievedtextsareusuallyusedascontextualinformationandcombinedwiththeoriginal
prompttoguidethegenerationofLLMs[54,57,63,65,81,112,158].
Forexample,In-ContextRALM[117]keepstheLLMparameters 4.1.2 Retrieval-GuidedTokenGenerationMethods. Inadditionto
unchangedanddirectlyincorporatestheretrieveddocumentbefore directlyintegratingexternalknowledgeintotheoriginalprompt,
theoriginalprompttoaugmentthegenerationprocess.IRCoT[149] theauxiliaryinformationcanbeemployedtoadjustthetokengeninterleaveschain-of-thought(CoT)generationandknowledgere- erationprocess.Forexample,KNN-KMs[62]firstretrieves𝑘most
trievalsteps,enablingtheretrievalofmorerelevantinformationfor relevantcontextsfromthedatastorebasedonthegivenquery,and
subsequentreasoningstepscomparedtostandardretrievalmethods computesaneighbordistributionbasedonthedistance.Theoutput
thatrelysolelyonthequestionasthequery.Insteadofretrieving distributioniscalibratedbyinterpolatingtheneighbordistribution
knowledgefromalargecorpus,GENREAD[182]firstpromptsa andtheoriginalmodel’soutputdistribution.Rest[49]isproposed
LLMtogeneratecontextualdocumentsbasedonthequery,and toreplacetheparametricdraftmodelwithanon-parametricrethengenerateanswersbasedonthegivencontextandquestion. trievaldatastoreandretrievesrelevanttokensbasedonthecurrent
SKR[159]proposesguidingLLMstodeterminewhethertheycan contextforspeculativedecoding[9,71,145].
10

<!-- Page 11 -->

ASurveyonRAGMeetingLLMs:TowardsRetrieval-AugmentedLargeLanguageModels Conference’17,July2017,Washington,DC,USA
4.2 IndependentTraining andintroducesanadaptivehybridretrievalstrategyforretrieving
IndependenttrainingreferstotrainingtheretrieverandLLMsas demonstrations.Additionally,itleveragesT5[116]asthegenerator,
twoentirelyindependentprocesses,inwhichthereisnointerac- whichundergoesfurtherfine-tuningbasedonthetargetlabeland
tionbetweentheretrieverandtheLLMsduringthetrainingpro- inputcombiningtheoriginalpromptwithretrieveddemonstrations.
cess[61,69,197].Comparedwithtraining-freemethods,theperfor- SMALLCAP[121]proposesusingtheCLIP[113],whichisapowmanceoftheRAG-empoweredmodelscanbeeffectivelyenhanced erfulpre-trainedmulti-modalnetwork,toencodetheinputimage
bytrainingLLMstoleveragetheretrievedknowledgeorretrievers andthetextualdataoftheexternaldatastoreandretrievethemost
tobridgethegapbetweeninformationretrievalandlanguagegen- relevantitemsbasedonthecosinesimilarity.Across-attention
eration.ForthetrainingofLLMs,thenegativeloglikelihoodlossis layeristrainedandGPT-2[115]isusedasthedecodertoproduce
themostrepresentativetrainingobjective[115,148],whichaims captions.
toguidetheLLMstogeneratedesiredoutputbasedonthegiven
input.Regardingtheretriever,itcanbecategorizedintotwotypes:
4.3.2 LLMsFirst. Similarly,itcanalsopre-trainLLMsfirst,and
1)Sparseretriever[120,125],and2)Denseretriever[61,69,197].
thentunetheretrieverunderthesupervisionofthewell-trained
Thesparseretrieversusuallyexploitsparsefeatures,e.g.,wordfre-

### LLMs.Forexample,DKRR[53]showsthatattentionscoresfroma

quencies,torepresentthedocumentsandcalculatetherelevance
sequence-to-sequencemodelcanindicatethedocument’srelevance.
scoresbasedontask-specificmetrics[77,120,125]suchasTF-IDF
Therefore,theyproposetoleveragetheattentionscoresofareader
andBM25.Asforthedenseretrievers,deepneuralnetworksare
modeltoproducesyntheticlabelstotraintheretriever.AAR[184]
employedtoencodethequeryanddocumentsintodenserepreproposesusingasmalllanguagemodeltogeneratethesupervised
sentations,andthentheinnerproductisusuallyusedtocalculate
signal for training retrievers. The well-trained retriever can be
relevancescoresandretrievetherelevantexternalknowledge.For
furtherleveragedtoenhancetheperformanceofblack-boxLLMs.
example,DPR[61]adoptstwoindependentBERT[25]networks
RA-DIT[86]firstfine-tunestheLLMstoenhancetheirabilityto
toencodethequeryandpassagesrespectively,andtrainsthese
leverageretrievedknowledge,andthentraintheretrievertobetter
modelsbyutilizingcontrastivelearning.CoG[69]proposestotrain
alignitsoutputwithLLMs.UPRISE[16]proposesalightweight
aprefixencoderandaphraseencoderforretrievalandreformulate
methodtoenhancethezero-shotperformanceofLLMsinunseen
thetextgenerationasmultiplecopy-and-pasteoperationsfrom
tasksbyintroducingapromptretriever.AfrozenLLMisemployed
existingsourcetextcollection.
toguidethefine-tuningprocessofthepromptretriever,andthis
4.3 SequentialTraining retrieverthenretrievespromptsfordifferenttaskswithvarious
LLMsduringinference.
Independenttrainingisanefficientapproachtoexploittheexternalknowledgeduringthegenerationprocesssincetheretriever
andgeneratorcanbetrainedofflineandanyoff-the-shelfmodels
4.4 JointTraining
canbeutilized,avoidingextratrainingcosts.Tobetterenhance
thesynergybetweentheretrieverandgenerator,severalmethods Jointtrainingmethods[17,51,60,79,167,196]employtheend-tohavebeenproposedtotraintheretrieverandLLMssequentially. endparadigmtooptimizetheretrieverandgeneratorsimultane-
Inthesesequentialtrainingmethods,theprocesstypicallybegins ously.Insteadoftrainingeachmodulesequentially,jointtraining
withtheindependentpre-trainingofeithertheretrieverorthe methodseffectivelyenhancetheretriever’sabilitytolocateexternal
generator,afterwhichthepre-trainedmoduleisfixedwhilethe knowledgeforgenerationandthegenerator’scapacitytoeffectively
othermoduleundergoestraining.Notethatvariousexistingmod- leveragetheretrievedinformation.Forinstance,RAG[74]miniels(e.g.,BERT[25,64,123],CLIP[113],T5[116])canbedirectly mizesthenegativeloglikelihoodtojointlytraintheretrieverand
employedasthefixedretrieverandgenerator,therebybypassing generator.REALM[46]adoptsasimilartrainingparadigmtothat
thefirstpertainingprocess.Comparedtoindependenttraining, ofRAG[74],andMaximumInnerProductSearch(MIPS)[15,29,
sequentialtraininginvolvescoordinatedtrainingoftheretriever 119,131]techniqueisusedtolocatethemostrelevantdocuments.
andgenerator,wherethetrainablemodulebenefitsfromtheassis- ToemployMIPS,allexternaldocumentsareembeddedfirstanda
tanceofthefixedmodule.Basedonthetrainingorderbetweenthe searchindexisproducedforeachembedding.Anasynchronous
retrieverandgenerator,sequentialtrainingcanbecategorizedinto indexupdatingstrategy[46,52,55,141]isproposedtorefreshthe
twoclasses:1)RetrieverFirst[5,127,128,153,199],and2)LLMs indexeveryseveralhundredtrainingstepstoavoidtimeconsump-
First[130,135,157]. tionofre-indexingalldocuments.
4.3.1 RetrieverFirst. Thesemethodsfirsttraintheretrievalmodel
andthenfixit.LLMsarethentrainedbyutilizingtheretrieved

## 5 Applications

knowledge.Forinstance,RETRO[6]adoptstheBERTmodelthatis
pre-trainedindependentlyastheretriever,andanencoder-decoder Inthissection,wewillintroducesomerepresentativeapplications
architectureistrainedtointegrateretrievalchunksintothemodel’s ofretrieval-augmentedlargelanguagemodels(RA-LLMs).Topropredictions. RALMs [181] adopts Google Search and the open- videaclearoverviewoftheapplicationsofRA-LLMs,wewillreview
source COLBERTV2 [64] as the pre-trained retriever and fine- themfromthreeperspectives:NLPapplications,downstreamtasks,
tunestheLLMtoeffectivelyleveragetheretrievedpassages.ITER- and domain-specific applications. The studies mentioned in this
RTGEN[124]utilizesthepre-trainedS-BERT[123]astheretriever sectionaresummarizedandcategorizedinFigure6.
11

<!-- Page 12 -->

Conference’17,July2017,Washington,DC,USA WenqiFan,YujuanDing,LiangboNing,ShijieWang,HengyunLi,DaweiYin,Tat-SengChua,andQingLi

### Applications

NLPApplications Downstream Domain-specific
Tasks Applications

### Software

QASystems ChatBots FactVerification Recommendations Engineering AIforScience Finance
Ghazvininejadetal.
RETRO[6] RAG[74] DiPalma[26] Docprompting[197] Clinfo.ai[92] Zhangetal.[187]
[43]
Fusion-in-Decoder[54] KDBTS[14] Atlas[55] CoRAL[163] Atlas[105] RetMol[160] AlphaFin[78]
REALM[46],etc. Komeilietal.[68] Self-RAG[5],etc. RevCore[94],etc. Dater[177] MoleculeSTM[90] ChatDOC[85]
Wangetal.[152],etc. SheetCopilo[76] PMINet[174] Yepesetal.[178],etc.
Xricl[134] BioBridge[161]
Synchromesh[111], RSA[97]
etc.
Graphvf[144],etc.
Figure6:AsummaryofapplicationsofRA-LLMscategorizedbyNLPapplications,downstreamtasks,anddomain-specific
application.Specifically,NLPapplicationsincludeQAsystems,ChatBots,andfactverification;downstreamtasksinclude
recommendationsandsoftwareengineering;anddomain-specificapplicationsincludeAIforScienceandFinance.
5.1 NLPApplications internetsearchtofurtheraugmentconversationperformance.Con-
Duetotheintrinsiccapabilityintextgeneration,RA-LLMshave sideringthedynamicnatureofknowledgeintheworld,another
variousapplicationsintheNLPfield,suchasQuestionAnswer model[152]furtheraccesseslargeamountsofdynamicinformation
(QA)Systems,ChatBot,andFactVerification. insearchenginestogenerateresponses.
5.1.1 QASystems. QASystemsaimtoprovidepreciseanswers 5.1.3 FactVerification. FactVerificationisacriticaltaskinveritouser’squeries.However,evenwhentrainedonextensivedata, fyingtheaccuracyandreliabilityofinformation.Withtheneed
thesesystemsmaylackthelatestinformationorspecificdomain fortrustedevidence,RA-LLMsarebeingutilizedtoenhancethe
knowledgethatisnotincludedintheirtrainingdata[54,91].To capabilitiesoffactverification[55,74,74].Lewisetal.[74]first
addressthislimitation,theintegrationofRA-LLMshasplayedacru- propose retrieval of external knowledge to augment a range of
cialroleinadvancingthecapabilitiesofQAsystemsbyenhancing knowledge-intensivetasksincludingfactverification.Ontheother
theirabilitytoretrieveandsynthesizerelevantinformation[6,54]. hand,Atlas[55]examinestheperformanceoftheRA-LLMsforfact
Specifically,RA-LLMscanprovidecoherentandcontextuallyrele- verificationunderfew-shotlearning.Recently,Self-RAG[5]has
vantanswersbyleveragingtheirretrievalcomponenttoaccessa greatlymadeanotableimpressionbyincorporatingaself-reflective
vastknowledgebase.Forexample,REALM[46]integratesaknowl- mechanism.Specifically,Self-RAGreflectsonwhetherretrieved
edgeretrieverthatcanretrieveinformationfromalargecorpus informationishelpfulandjudgesthereliabilityofretrievedinforduringpre-training,fine-tuning,andinference.Thisapproachal- mation,therebygreatlyimprovingtheverificationaccuracy.
lowsREALMtoeffectivelyretrievefromavastknowledgecorpus,
therebyimprovingtheaccuracyofitsresponses.Similarly,Fusion-
5.2 DownstreamTasks
in-Decoder[54]retrievespassagesfromsupportdocumentsand
thenfusesthemwithquestionstogeneratetheanswer,achieving InadditiontoNLPapplications,RA-LLMscanalsobeappliedto
higheraccuracy.Inaddition,Borgeaudetal.[6]indicatethatthe variousdownstreamtasks,suchasrecommendationsandsoftware
qualityoftheanswersmayrelymoreontheoutputofretrieval. engineering.
5.1.2 ChatBot. ChatBot is designed to interact with users in a 5.2.1 Recommendations. Recommendersystemsplayanimpornaturalandconversationalmanner[87].DifferentfromtheQA tantroleinmodelingusers’preferencesandprovidingpersonalized
system,ChatBotfocusesonmaintainingacoherentandcontextu- recommendations[34–36,154,189,195].Recently,RA-LLMshave
allyrichconversationwiththeuser.Toenhancethesecapabilities, demonstratedgreatpotentialinprovidingpersonalizedandconrecentmethodsfocusonintegratingRA-LLMs[60,68,188]forits textuallyrelevantrecommendationsbyintegratingretrievaland
abilitytoaugmenttheChatBotwithrelevantexternalknowledge, generationprocesses[26,94,163].Forexample,DiPalma[26]profacilitatingmoreengagingandcontext-richinteractionswithusers. posesasimpleretrieval-augmentedrecommendationmodel,that
Forexample,somestudies[14,43]retrieverelevantknowledge leveragesknowledgefrommovieorbookdatasetstoenhancerecfromstaticdatabases(e.g.,aWikipediadump)toaugmentconver- ommendations.Additionally,Luetal.[94]furtherretrievalfrom
sation.Komeilietal.[68]proposeretrievinginformationfromthe thereviewstoenrichiteminformationinrecommendersystems.
12

<!-- Page 13 -->

ASurveyonRAGMeetingLLMs:TowardsRetrieval-AugmentedLargeLanguageModels Conference’17,July2017,Washington,DC,USA
CoRAL[163]utilizesreinforcementlearningtoretrievecollabo- Trustworthy RA-LLMs. The essential objective of developing
rative information from the dataset and align it with semantic RAG-empoweredLLMsistoenhancethecapabilityofthelanguage
informationformoreaccuraterecommendations. models,therebybenefitingusersandsocietybyalleviatingredundantandmeaninglesslabor,increasingconveniences,andspurring
5.2.2 SoftwareEngineering. TheriseofRA-LLMshasinfluenced
socialprogress.However,recentresearchindicatesthatRA-LLMs
manyaspectsofsoftwareengineering[105,177,197].Forexample,
canbemaliciouslyandunintentionallymanipulatedtomakeunsome studies propose the retrieval-augmented generation parareliabledecisionsandharmhumans[23,200],whichmayhave
digmforcodegeneration[197]andprogramrepair[105].Simiseriousconsequencesinsafety-criticalscenarios[11,13,32,38,88].
larly,Parvezetal.[108]retrievetop-rankedcodesorsummaries
Inaddition,privateretrievaldatabasehasariskofleakage,raising
fromthecodebaseandaggregatethemwithinputtoenhancecode
concernsregardingtheprivacyofRA-LLMs[186].Therefore,degenerationandsummarization.Inaddition,RA-LLMsshowpotenvelopingtrustworthyRA-LLMsisofparamountimportanceasit
tialintabulardataprocessing[76,177]andText-to-SQLsemantic
cansignificantlymitigatethepotentialnegativeimpactsofLLMs
parsing[111,134].
technologyandprovidepeoplewithpowerfulAImodelsthatcanbe
fullytrusted.Tobespecific,theidealtrustworthinessinRA-LLMs
5.3 Domain-specificApplications
systemsshouldpossessthefollowingcharacteristics:1)robust-
RA-LLMshavebeenwidelyadoptedforvariousdomain-specific ness,2)fairness,3)explainability,and4)privacy.Forexample,
tasks,suchasAIforScienceandFinance. robustnessmeansatrustworthyRA-LLMssystemshouldberobustagainstmaliciousorinadvertentperturbationsintroducedby
5.3.1 AIforScience. RA-LLMshaveproventobebeneficialfor attackers.FairnessindicatesatrustworthyRA-LLMssystemought
therealmsofscience,suchasmolecularandprotein.Molecules toavoiddiscriminationduringthedecision-makingprocess.Exincludeidentifyingthemolecule’spropertyandpredictingnew plainabilityrequiresacompleteunderstandingoftheintrinsic
molecules,therebyfavoringdrugdiscovery.Currently,someRA- workingsofRA-LLMssystems,i.e.,thepredictionsofRA-LLMssys-
LLMshavebeenappliedtomoleculesbyintegratingretrievalof temsareexplainableandtransparent.Privacyentailssafeguarding
moleculestructureandbiomedicalentitieslikeprotein,molecule, thesafetyofthisprivateinformationhousedwithinthedatastore
anddisease[90,160,161,174],etc.Lietal.[77],Wangetal.[160] whenestablishingtrustworthyRA-LLMssystems.
proposeretrieval-basedframeworksbyretrievingfromthedatabase Multi-LingualRA-LLMs.Theabilityofleveragingknowledge
toguidemoleculegeneration.Liuetal.[90]introduceamulti-modal frommultiplelanguagescangreatlyenhancethecapabilitiesof
moleculestructure-textmodelbyretrievingtextualknowledgefrom retrieval-augmentedlanguagemodels.Astheworldbecomesinalarge-scaledatasetformolecularpropertyprediction.Inaddition, creasinglyinterconnected,thereisagrowingneedforAIsystems
RA-LLMsalsosignificantlyinfluenceProteinrepresentationand thatcanunderstandandcommunicateacrossdifferentlanguages.
generation [97, 144]. For instance, RSA [97] queries protein se- Byincorporatingmultilingualknowledgeretrievalandgeneration,
quencesassociatedwithacollectionofstructurallyorfunctionally thesemodelscanaccessandsynthesizeinformationfromdiverse
similarsequencesinthedatabasetoenhanceproteinrepresenta- linguisticsources,enablingmorecomprehensiveandnuanceduntions.Furthermore,Lozanoetal.[92]presentaclinicalQAsystem derstandingandgenerationcapabilities.Additionally,multilingual
basedonretrievingpublishedreviewarticles. modelscanfacilitatecross-culturalcommunicationandknowledge
sharingandbreakingdownlanguagebarriers,therebybringingcon-
5.3.2 Finance. Inthehighlydata-drivenandinformation-intensive
veniencetopeopleacrossdifferentregionsoftheworld,especially
fieldoffinance,RA-LLMshaveprovedtobeasignificanttechnology
thoseinareaswithminoritylanguages[58,81].Forexample,users
forenhancingdecision-making[78,178,187].Forexample,Zhang
fromcountrieswithlessprevalentlanguagescanutilizeabundant
etal.[187]retrievefinancialinformationfromexternalsources,
EnglishandChinesecorporaforknowledgeretrieval,enhancing
suchasnewsplatforms(e.g.,BloombergandReuters)andsocial
theperformanceoflargelanguagemodelsindownstreamtasks.
mediaplatforms(e.g.,Twitter,Reddit),tocombinewiththeoriginal
Multi-modalRA-LLMs.Multi-modalretrieval-augmentedgenerquerytoenhancetheprecisionoffinancialsentimentanalysis.In
ationextendstheknowledgesourcesbeyondtexttoincludevarious
addition,financialQAisanotherprimarytaskoffinancialanalysis,
datamodalitiessuchasimages,videos,andaudio.Byintegrating
whichusuallyextractsrelevantknowledgefromfinancialdocuvariousmodalities,LLMscanleveragerichercontextualinformaments.AsprofessionaldocumentsareusuallystoredinPDFformat,
tionthansingle-modalRAGanddevelopamorecomprehensive
Lin[85]introducesaPDFparsercombinedwithRA-LLMstoreunderstandingofusers’needs,bringingprecise,fine-grained,and
trieveknowledgefromfinancialreports.Ontheotherhand,Yepes
high-qualitygeneration.Forinstance,animageorvideocanprovide
etal.[178]proposeadocumentchunkingmethodbasedonstrucvaluablevisualcuesthatcomplementtextualinformation,leading
tureinsteadofchunkingbasedonparagraphs,furtherimproving
tomorepreciselanguagegeneration[51,199].Byfusingmultiple
thequalityofRA-LLMsoutputs.
modalities,multi-modalRA-LLMscandevelopamorecomprehensive understanding of the world, leading to more accurate and

## 6 Futurechallengesand

insightfuloutputs,benefitingawiderangeofdomains,including

## Opportunities

healthcare[199],drugdiscovery[136],molecularanalysis[3,90],
SincethestudiesofRA-LLMsarestillintheearlystage,wepresent etc.
somepotentialresearchdirectionsthatcanbeexploredinthefuture
inthefieldofRA-LLMs.
13

<!-- Page 14 -->

Conference’17,July2017,Washington,DC,USA WenqiFan,YujuanDing,LiangboNing,ShijieWang,HengyunLi,DaweiYin,Tat-SengChua,andQingLi
QualityofExternalKnowledge.Asacommonlyuseddatastore [9] CharlieChen,SebastianBorgeaud,GeoffreyIrving,Jean-BaptisteLespiau,LauincurrentRAGsystems,Wikipedia[61,199]servesasavastreposi- rentSifre,andJohnJumper.2023.Acceleratinglargelanguagemodeldecoding
withspeculativesampling.arXivpreprintarXiv:2302.01318(2023).
toryofexternaltextualknowledgeusedtoaugmentthegeneration
[10] DanqiChen,AdamFisch,JasonWeston,andAntoineBordes.2017.Reading
process,whichcontainsmillionsofarticlescoveringvariousdisci- WikipediatoAnswerOpen-DomainQuestions.InACL(1).Associationfor
plines.However,thereliabilityandaccuracyofindividualarticles ComputationalLinguistics,1870–1879.
[11] JingfanChen,WenqiFan,GuanghuiZhu,XiangyuZhao,ChunfengYuan,Qing
withinWikipediavarysignificantly,andtheintroductionofsome Li,andYihuaHuang.2022.Knowledge-enhancedBlack-boxAttacksforRecomtextsthatdeviatefromfactsmightevenmisleadthemodel’sgener- mendations.InProceedingsofthe28thACMSIGKDDConferenceonKnowledge
DiscoveryandDataMining.108–117.
ationprocess.Therefore,itiscrucialtoenhancethequalityofthe
[12] Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Ponde
externalknowledgecorpusandmitigatethenegativeimpactoflow- deOliveiraPinto,JaredKaplan,HarriEdwards,YuriBurda,NicholasJoseph,
qualityknowledgeontheperformanceofLLMs.Byenhancingthe GregBrockman,etal.2021.Evaluatinglargelanguagemodelstrainedoncode.
arXivpreprintarXiv:2107.03374(2021).
qualityoftheexternalknowledgeandtailingrobustmechanisms
[13] XiaoChen,WenqiFan,JingfanChen,HaochenLiu,ZitaoLiu,ZhaoxiangZhang,
byfilteringoutlow-qualityorunreliableinformation,theRA-LLM andQingLi.2023.Fairlyadaptivenegativesamplingforrecommendations.In
systemsmightproducemoreaccurate,reliableoutputs,thereby
ProceedingsoftheACMWebConference2023.3723–3733.
[14] XiuyiChen,FandongMeng,PengLi,FeilongChen,ShuangXu,BoXu,andJie
improvingtheireffectivenessinvariousreal-worldapplications. Zhou.2020.Bridgingthegapbetweenpriorandposteriorknowledgeselection
forknowledge-groundeddialoguegeneration.InProceedingsofthe2020confer-
7 CONCLUSION enceonempiricalmethodsinnaturallanguageprocessing(EMNLP).3426–3437.
[15] YudongChen,ZhihuiLai,YujuanDing,KaiyiLin,andWaiKeungWong.2019.
Retrieval-augmented generation (RAG), a cutting-edge AI tech- Deepsupervisedhashingwithanchorgraph.InProceedingsoftheIEEE/CVF
internationalconferenceoncomputervision.9796–9804.
nique,hasachievedremarkablesuccessacrossvariousapplications,
[16] DaixuanCheng,ShaohanHuang,JunyuBi,YuefengZhan,JianfengLiu,Yujing
includingrecommendation,moleculegeneration,proteinrepresen- Wang,HaoSun,FuruWei,WeiweiDeng,andQiZhang.2023.UPRISE:Universal
tation,andsoftwareengineering,owingtothepotentcapabilitiesof PromptRetrievalforImprovingZero-ShotEvaluation.InProceedingsofthe2023
ConferenceonEmpiricalMethodsinNaturalLanguageProcessing.12318–12337.
retrievalinprovidingsupplementaryinformationtoenhancegen-
[17] XinCheng,DiLuo,XiuyingChen,LemaoLiu,DongyanZhao,andRuiYan.
erationperformance.Recently,increasingeffortshavebeenmade 2024.Liftyourselfup:Retrieval-augmentedtextgenerationwithself-memory.
toalleviatethelimitationsoflargelanguagemodels(LLMs),such
AdvancesinNeuralInformationProcessingSystems36(2024).
[18] AakankshaChowdhery,SharanNarang,JacobDevlin,MaartenBosma,Gaurav
ashallucinationandout-of-dateinternalknowledge,byleveraging Mishra,AdamRoberts,PaulBarham,HyungWonChung,CharlesSutton,Seretrievaltoprovidethelatestauxiliaryinformationandteaching bastianGehrmann,etal.2023.Palm:Scalinglanguagemodelingwithpathways.
JournalofMachineLearningResearch24,240(2023),1–113.

### LLMstoharnesstheretrievedexternalknowledge.Withtherapid

[19] WBruceCroft,DonaldMetzler,andTrevorStrohman.2010. Searchengines:
advancementsinretrieval-augmentedlargelanguagemodels(RA- Informationretrievalinpractice.Vol.520.Addison-WesleyReading.
LLMs),thereisapressingneedforacomprehensiveandsystematic [20] LeyangCui,YuWu,JianLiu,SenYang,andYueZhang.2021.Template-Based
NamedEntityRecognitionUsingBART.InACL/IJCNLP(Findings)(Findingsof
overview.Tobridgethisgap,inthispaper,wecomprehensively ACL,Vol.ACL/IJCNLP2021).AssociationforComputationalLinguistics,1835–
reviewtheRA-LLMsfromtheperspectivesofmorelarchitecture, 1845.
trainingstrategy,andapplicationarea,providingresearcherswith [21] MatthewDahl,VarunMagesh,MiracSuzgun,andDanielEHo.2024. Large
legalfictions:Profilinglegalhallucinationsinlargelanguagemodels. arXiv
anin-depthunderstanding.Moreover,sincethestudiesofRA-LLMs preprintarXiv:2401.01301(2024).
arestillintheearlystage,wealsodiscussthecurrentlimitations [22] MichieldeJong,YuryZemlyanskiy,NicholasFitzGerald,FeiSha,andWilliamW.
Cohen.2022.MentionMemory:incorporatingtextualknowledgeintoTransandseveralpotentialresearchdirectionsforfutureresearch.
formersthroughentitymentionattention.InICLR.OpenReview.net.
[23] GeleiDeng,YiLiu,KailongWang,YuekangLi,TianweiZhang,andYangLiu.
REFERENCES 2024.Pandora:JailbreakGPTsbyRetrievalAugmentedGenerationPoisoning.
arXivpreprintarXiv:2402.08416(2024).
[1] JoshAchiam,StevenAdler,SandhiniAgarwal,LamaAhmad,IlgeAkkaya,Floren-
[24] ZiqingDeng,ZhihuiLai,YujuanDing,HengKong,andXuWu.2024. Deep

## A

ci
n
a
a

## L

d
e
k
o
a
n
t
i
,

## A

et
le
a
m
l.
a
2
n
0
,
2

## D

3.
io

## G

go
pt

## A

-4
lm
te
e
c
id
h
a
n
,
ic
Ja
a
n
l
k
re
o
p

## A

o
l
r
t
t
e
.
n
a
s
r
c

## X

h
i
m
v
i
p
d
r
t,
ep

## S

r
a
i
m
nt

## A

a
l
r
t

## X

m
iv
a
:
n
2
,
3

## S

0
h
3.
y
0
a
8
m
77
a
4
l ScalingFactorQuantizationNetworkforLarge-scaleImageRetrieval.InICMR.

## Acm,851–859.

(2023).
[25] JacobDevlin,Ming-WeiChang,KentonLee,andKristinaToutanova.2019.BERT:
[2] SwetaAgrawal,ChuntingZhou,MikeLewis,LukeZettlemoyer,andMarjan
Pre-trainingofDeepBidirectionalTransformersforLanguageUnderstanding.

## G

In
h

## A

az

## C

v

## L

in

## (F

in
in
e
d
ja
in
d
g
.
s
2
)
0
.
2

## A

3
s
.
s

## I

o
n
c
-
i
c
a
o
ti
n
o
t
n
ex
f
t
or

## E


## C

xa
o
m
m
p
p
l
u
e
t
s
a

## S

ti
e
o
l
n
ec
a
t
l
io

## L

n
in
f
g
o
u
r
is

## M

ti
a
cs
c
,
h
8
in
85
e
7

## T

–
r
8
a
8
n
7
s
3
l
.
ation. InNAACL-HLT(1).AssociationforComputationalLinguistics,4171–4186.
[26] DarioDiPalma.2023.Retrieval-augmentedrecommendersystem:Enhancing
[3] MilesCAndrews,JunnaOba,Chang-JiunWu,HaifengZhu,TatianaKarpinets, recommendersystemswithlargelanguagemodels.InProceedingsofthe17th
CaitlinACreasy,Marie-AndréeForget,XiaoxingYu,XingzhiSong,Xizeng ACMConferenceonRecommenderSystems.1369–1373.
Mao,etal.2022.Multi-modalmolecularprogramsregulatemelanomacellstate.
Naturecommunications13,1(2022),4000. [27] Y
Li
u
.
j
2
u
0
a
2
n
4.

## D


## F

in
as
g
h
,
i

## Y

o
u
n
n

## R

s
e
h

## G

a
e
n
n:

## M


## L

a

## L

,

## M


## W


## -E

en
m
q
p
i
o

## F

w
a
e
n
r
,
e

## Y

d
ig

## F

e
as

## Y

h
a
io
o
n

## ,T


## R

a
e
t
p

## -S

o
e
r
n
t
g
Ge

## C

n
h
e
u
ra
a
t
,
i
a
o
n
n
d
.a

## Q

rX
in
i
g
v

## [4] A

la
k
n
a
g
r
u
i
a

## A

g
s
e
ai
m

## ,S

o
e
d
w
el
o
s
n
a

## M

nd
in
a
,
p

## Z

p
e
l
x
ic
u
a
a
t
n
io

## Z

n
h
s.
on
In
g,

## P

a
r
n
oc
d
e

## D

ed
a
i
n
n
q
g
i
s

## C

o
h
f
e
th
n
e
.2
6
0
1
2
s
3
t
.

## A


## R

n
e
n
tr
u
i
a
e
l
va

## M

le
b
e
a
t
s
in
ed
g
preprintarXiv:2403.06660(2024).
oftheAssociationforComputationalLinguistics(Volume6:TutorialAbstracts). [28] Y
ou
u
t
j
fi
u
t
a
g
n
e

## D

ne
in
ra
g
t
,
io

## P

n

## .Y

w
.
i

## M

th
o
u
k
s
,
e

## Y

r
u
co
n
o
sh
rd
a
i
n
na

## M

ti
a
o
,
n
a
p
n
r
d
ef

## Y

er
i
e

## B

n
i
c
n
e
.
l
2
e
0
a
2
rn
3.
in

## P

g
e
.
r

## I

s
n
o
f.
n

## P

a
r
l
o
iz
ce
e
s
d
s.
f

## M

as
a
h
n
io
ag
n
.
41–46.
60,5(2023),103434.
[5] AkariAsai,ZeqiuWu,YizhongWang,AvirupSil,andHannanehHajishirzi.2023.
[29] YujuanDing,WaiKeungWong,ZhihuiLai,andZhengZhang.2020.Bilinear
S In el T f- h R e A T G w : e L lf e t a h rn In in te g rn to at R io e n t a ri l e C ve o , n G fe e r n en er c a e t o e n ,a L n e d ar C n r i i n t g iq R u e e p t r h e r s o en u t g a h ti S o e n l s f . -Reflection. S V u id p e e o rv T i e s c e h d no H l. a 3 s 0 h , in 2 g (2 B 0 a 2 s 0 e ), d 5 o 90 n – 2 6 D 02. ImageFeatures. IEEETrans.CircuitsSyst.
[6] SebastianBorgeaud,ArthurMensch,JordanHoffmann,TrevorCai,ElizaRuther-
[30] YujuanDing,WaiKeungWong,ZhihuiLai,andZhengZhang.2020.Discrimiford,KatieMillican,GeorgeBmVanDenDriessche,Jean-BaptisteLespiau,Bog- nativedual-streamdeephashingforlarge-scaleimageretrieval.Information
d
fr
a
o
n
m

## D

t
a
r
m
ill
o
io
c
n
,
s

## A

o
id
f
a
t
n
ok

## C

e
l
n
a
s
r
.
k

## I

,
n
et
In
a
t
l
e
.
r
2
n
0
a
2
t
2
io
.
n

## I

a
m
l
p
c
r
o
o
n
v
fe
in
re
g
n
l
c
a
e
n
o
g
n
ua
m
g
a
e
c
m
hi
o
n
d
e
e
l
l
e
s
a
b
rn
y
in
re
g
t
.
r

## P

ie

## M

vi

## L

n

## R

g
,
Processing&Management57,6(2020),102288.
[31] AndrewDrozdov,NathanaelSchärli,EkinAkyürek,NathanScales,Xinying
2206–2240.
Song,XinyunChen,OlivierBousquet,andDennyZhou.2022.Compositional
[7] TomBrown,BenjaminMann,NickRyder,MelanieSubbiah,JaredDKaplan, semanticparsingwithlargelanguagemodels.InTheEleventhInternational

## A

Pr
s
a
k
f
e
u
l
l
l
l
,
a
e

## D

ta
h
l
a
.
r
2
i
0
w
2
a
0
l
.
,

## L


## A

a
r
n
v
g
in
u
d
ag

## N

e
e
m
el
o
ak
d
a
e
n
ls
ta
a
n
re

## ,P

fe
r
w
an
-
a
s
v
ho

## S

t
h
l
y
e
a
a
m
rn
,
e

## G

rs
i
.
ri

## A

sh
dv

## S

a
a
n
st
c
r
e
y
s
,
i

## A

n
m
ne
a
u
n
r
d
a
a
l
ConferenceonLearningRepresentations.
informationprocessingsystems33(2020),1877–1901. [32] WenqiFan,TylerDerr,XiangyuZhao,YaoMa,HuiLiu,JianpingWang,Jiliang
[8] StefanButtcher,CharlesLAClarke,andGordonVCormack.2016.Information Tang,andQingLi.2021.Attackingblack-boxrecommendationsviacopying
retrieval:Implementingandevaluatingsearchengines.MitPress.
14

<!-- Page 15 -->

ASurveyonRAGMeetingLLMs:TowardsRetrieval-AugmentedLargeLanguageModels Conference’17,July2017,Washington,DC,USA
cross-domainuserprofiles.In2021IEEE37thInternationalConferenceonData Grave.2023. Atlas:Few-shotLearningwithRetrievalAugmentedLanguage
Engineering(ICDE).IEEE,1583–1594. Models.JournalofMachineLearningResearch24,251(2023),1–43.
[33] WenqiFan,YujuanDing,LiangboNing,ShijieWang,HengyunLi,DaweiYin, [56] ZhengbaoJiang,JunAraki,HaiboDing,andGrahamNeubig.2021.Howcanwe
Tat-SengChua,andQingLi.2024.ASurveyonRAGMeetingLLMs:Towards knowwhenlanguagemodelsknow?onthecalibrationoflanguagemodelsfor
Retrieval-AugmentedLargeLanguageModels.Proroceedingsofthe30thACM questionanswering.TransactionsoftheAssociationforComputationalLinguistics
SIGKDDConferenceonKnowledgeDiscovery&DataMining(2024). 9(2021),962–977.
[34] WenqiFan,XiaoruiLiu,WeiJin,XiangyuZhao,JiliangTang,andQingLi.2022. [57] ZhengbaoJiang,FrankFXu,LuyuGao,ZhiqingSun,QianLiu,JaneDwivedi-
GraphTrendFilteringNetworksforRecommendation.InProceedingsofthe45th Yu,YimingYang,JamieCallan,andGrahamNeubig.2023. ActiveRetrieval
InternationalACMSIGIRConferenceonResearchandDevelopmentinInformation AugmentedGeneration.InProceedingsofthe2023ConferenceonEmpirical
Retrieval.112–121. MethodsinNaturalLanguageProcessing.7969–7992.
[35] WenqiFan,YaoMa,QingLi,YuanHe,EricZhao,JiliangTang,andDaweiYin. [58] AnubhaKabra,EmmyLiu,SimranKhanuja,AlhamFikriAji,GentaWinata,

### Graphneuralnetworksforsocialrecommendation.InTheworldwideweb SamuelCahyawijaya,AnuoluwapoAremu,PerezOgayo,andGrahamNeubig.

conference.417–426. 2023.Multi-lingualandMulti-culturalFigurativeLanguageUnderstanding.In
[36] WenqiFan,YaoMa,QingLi,JianpingWang,GuoyongCai,JiliangTang,and The61stAnnualMeetingOfTheAssociationForComputationalLinguistics.
DaweiYin.2020.Agraphneuralnetworkframeworkforsocialrecommenda- [59] SauravKadavath,TomConerly,AmandaAskell,TomHenighan,DawnDrain,
tions.IEEETransactionsonKnowledgeandDataEngineering(2020). EthanPerez,NicholasSchiefer,ZacHatfield-Dodds,NovaDasSarma,EliTran-
[37] WenqiFan,ShijieWang,JianiHuang,ZhikaiChen,YuSong,WenzhuoTang, Johnson,etal.2022.Languagemodels(mostly)knowwhattheyknow.arXiv
HaitaoMao,HuiLiu,XiaoruiLiu,DaweiYin,etal.2024.GraphMachineLearn- preprintarXiv:2207.05221(2022).
ingintheEraofLargeLanguageModels(LLMs).arXivpreprintarXiv:2404.14928 [60] MinkiKang,JinMyungKwak,JinheonBaek,andSungJuHwang.2023.Knowl-
(2024). edgegraph-augmentedlanguagemodelsforknowledge-groundeddialogue
[38] WenqiFan,XiangyuZhao,XiaoChen,JingranSu,JingtongGao,LinWang, generation.arXivpreprintarXiv:2305.18846(2023).
QidongLiu,YiqiWang,HanXu,LeiChen,etal.2022.AComprehensiveSurvey [61] VladimirKarpukhin,BarlasOguz,SewonMin,PatrickS.H.Lewis,LedellWu,
onTrustworthyRecommenderSystems.arXivpreprintarXiv:2209.10117(2022). SergeyEdunov,DanqiChen,andWen-tauYih.2020.DensePassageRetrieval
[39] ThibaultFévry,LivioBaldiniSoares,NicholasFitzGerald,EunsolChoi,andTom forOpen-DomainQuestionAnswering.InEMNLP(1).AssociationforCompu-
Kwiatkowski.2020. EntitiesasExperts:SparseMemoryAccesswithEntity tationalLinguistics,6769–6781.
Supervision.InEMNLP(1).AssociationforComputationalLinguistics,4937– [62] UrvashiKhandelwal,OmerLevy,DanJurafsky,LukeZettlemoyer,andMike

## Lewis.2020.GeneralizationthroughMemorization:NearestNeighborLanguage

[40] LuyuGao,XueguangMa,JimmyLin,andJamieCallan.2023. PreciseZero- Models.InInternationalConferenceonLearningRepresentations.
ShotDenseRetrievalwithoutRelevanceLabels.InACL(1).Associationfor [63] OmarKhattab,KeshavSanthanam,XiangLisaLi,DavidHall,PercyLiang,
ComputationalLinguistics,1762–1777. ChristopherPotts,andMateiZaharia.2022.Demonstrate-search-predict:Com-
[41] YunfanGao,YunXiong,XinyuGao,KangxiangJia,JinliuPan,YuxiBi,YiDai, posingretrievalandlanguagemodelsforknowledge-intensivenlp. arXiv
JiaweiSun,andHaofenWang.2023.Retrieval-augmentedgenerationforlarge preprintarXiv:2212.14024(2022).
languagemodels:Asurvey.arXivpreprintarXiv:2312.10997(2023). [64] OmarKhattabandMateiZaharia.2020.Colbert:Efficientandeffectivepassage
[42] IzacardGautier,CaronMathilde,HosseiniLucas,RiedelSebastian,Bojanowski searchviacontextualizedlateinteractionoverbert.InProceedingsofthe43rd
Piotr,JoulinArmand,andGraveEdouard.2022.Unsuperviseddenseinformation InternationalACMSIGIRconferenceonresearchanddevelopmentinInformation
retrievalwithcontrastivelearning.TransactionsonMachineLearningResearch Retrieval.39–48.
(2022). [65] GangwooKim,SungdongKim,ByeonggukJeon,JoonsukPark,andJaewooKang.
[43] MarjanGhazvininejad,ChrisBrockett,Ming-WeiChang,BillDolan,Jianfeng 2023.TreeofClarifications:AnsweringAmbiguousQuestionswithRetrieval-
Gao,Wen-tauYih,andMichelGalley.2018.Aknowledge-groundedneuralcon- AugmentedLargeLanguageModels.InThe2023ConferenceonEmpiricalMethods
versationmodel.InProceedingsoftheAAAIConferenceonArtificialIntelligence, inNaturalLanguageProcessing.
Vol.32. [66] HyuhngJoonKim,HyunsooCho,JunyeobKim,TaeukKim,KangMinYoo,
[44] MichaelR.Glass,GaetanoRossiello,Md.FaisalMahbubChowdhury,Ankita andSang-gooLee.2022.Self-generatedin-contextlearning:Leveragingauto-
Naik,PengshanCai,andAlfioGliozzo.2022.Re2G:Retrieve,Rerank,Generate. regressivelanguagemodelsasademonstrationgenerator. arXivpreprint
InNAACL-HLT.AssociationforComputationalLinguistics,2701–2715. arXiv:2206.08082(2022).
[45] EdouardGrave,ArmandJoulin,andNicolasUsunier.2017.ImprovingNeural [67] MeiKobayashiandKoichiTakeda.2000.Informationretrievalontheweb.ACM
LanguageModelswithaContinuousCache.InICLR(Poster).OpenReview.net. computingsurveys(CSUR)32,2(2000),144–173.
[46] KelvinGuu,KentonLee,ZoraTung,PanupongPasupat,andMingweiChang. [68] MojtabaKomeili,KurtShuster,andJasonWeston.2022.Internet-Augmented

### Retrievalaugmentedlanguagemodelpre-training.InInternationalconfer- DialogueGeneration.InACL(1).AssociationforComputationalLinguistics,

enceonmachinelearning.PMLR,3929–3938. 8460–8478.
[47] JunxianHe,GrahamNeubig,andTaylorBerg-Kirkpatrick.2021.EfficientNear- [69] TianLan,DengCai,YanWang,HeyanHuang,andXian-LingMao.2022.Copy
estNeighborLanguageModels.InEMNLP(1).AssociationforComputational isAllYouNeed.InTheEleventhInternationalConferenceonLearningRepresen-
Linguistics,5703–5714. tations.
[48] QiuxiangHe,GuopingHuang,QuCui,LiLi,andLemaoLiu.2021. Fastand [70] AngelikiLazaridou,ElenaGribovskaya,WojciechStokowiec,andNikolaiGrigaccurateneuralmachinetranslationwithtranslationmemory.InProceedingsof orev.2022.Internet-augmentedlanguagemodelsthroughfew-shotprompting
the59thAnnualMeetingoftheAssociationforComputationalLinguisticsandthe foropen-domainquestionanswering.arXivpreprintarXiv:2203.05115(2022).
11thInternationalJointConferenceonNaturalLanguageProcessing(Volume1: [71] YanivLeviathan,MatanKalman,andYossiMatias.2023.Fastinferencefrom
LongPapers).3170–3180. transformersviaspeculativedecoding.InInternationalConferenceonMachine
[49] ZhenyuHe,ZexuanZhong,TianleCai,JasonDLee,andDiHe.2023. Rest: Learning.PMLR,19274–19286.
Retrieval-basedspeculativedecoding.arXivpreprintarXiv:2311.08252(2023). [72] MikeLewis,MarjanGhazvininejad,GargiGhosh,ArmenAghajanyan,Sida
[50] SebastianHofstätter,JiecaoChen,KarthikRaman,andHamedZamani.2023. Wang,andLukeZettlemoyer.2020.Pre-trainingviaparaphrasing.Advancesin
FiD-Light:EfficientandEffectiveRetrieval-AugmentedTextGeneration.In NeuralInformationProcessingSystems33(2020),18470–18481.
SIGIR.ACM,1437–1447. [73] MikeLewis,YinhanLiu,NamanGoyal,MarjanGhazvininejad,Abdelrahman
[51] ZiniuHu,AhmetIscen,ChenSun,ZiruiWang,Kai-WeiChang,YizhouSun, Mohamed,OmerLevy,VeselinStoyanov,andLukeZettlemoyer.2020.BART:
CordeliaSchmid,DavidARoss,andAlirezaFathi.2023. Reveal:Retrieval- DenoisingSequence-to-SequencePre-trainingforNaturalLanguageGeneraaugmentedvisual-languagepre-trainingwithmulti-sourcemultimodalknowl- tion,Translation,andComprehension.InACL.AssociationforComputational
edgememory.InProceedingsoftheIEEE/CVFconferenceoncomputervisionand Linguistics,7871–7880.
patternrecognition.23369–23379. [74] Patrick Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir
[52] JieHuang,WeiPing,PengXu,MohammadShoeybi,KevinChen-ChuanChang, Karpukhin,NamanGoyal,HeinrichKüttler,MikeLewis,Wen-tauYih,TimRockandBryanCatanzaro.2023.Raven:In-contextlearningwithretrievalaugmented täschel,etal.2020.Retrieval-augmentedgenerationforknowledge-intensivenlp
encoder-decoderlanguagemodels.arXivpreprintarXiv:2308.07922(2023). tasks.AdvancesinNeuralInformationProcessingSystems33(2020),9459–9474.
[53] GautierIzacardandEdouardGrave.2021.DistillingKnowledgefromReaderto [75] DaliangLi,AnkitSinghRawat,ManzilZaheer,XinWang,MichalLukasik,
RetrieverforQuestionAnswering.InICLR2021-9thInternationalConferenceon AndreasVeit,FelixYu,andSanjivKumar.2022.Largelanguagemodelswith
LearningRepresentations. controllableworkingmemory.arXivpreprintarXiv:2211.05110(2022).
[54] GautierIzacardandEdouardGrave.2021.LeveragingPassageRetrievalwith [76] HongxinLi,JingranSu,YuntaoChen,QingLi,andZHAO-XIANGZHANG.
GenerativeModelsforOpenDomainQuestionAnswering.InEACL2021-16th 2024.SheetCopilot:BringingSoftwareProductivitytotheNextLevelthrough
ConferenceoftheEuropeanChapteroftheAssociationforComputationalLinguis- LargeLanguageModels.AdvancesinNeuralInformationProcessingSystems36
tics.AssociationforComputationalLinguistics,874–880. (2024).
[55] GautierIzacard,PatrickLewis,MariaLomeli,LucasHosseini,FabioPetroni,
TimoSchick,JaneDwivedi-Yu,ArmandJoulin,SebastianRiedel,andEdouard
15

<!-- Page 16 -->

Conference’17,July2017,Washington,DC,USA WenqiFan,YujuanDing,LiangboNing,ShijieWang,HengyunLi,DaweiYin,Tat-SengChua,andQingLi
[77] JiatongLi,YunqingLiu,WenqiFan,Xiao-YongWei,HuiLiu,JiliangTang, LanguageModels.arXivpreprintarXiv:2402.13492(2024).
andQingLi.2023. EmpoweringMoleculeDiscoveryforMolecule-Caption [100] JacobMenick,MajaTrebacz,VladimirMikulik,JohnAslanides,FrancisSong,
TranslationwithLargeLanguageModels:AChatGPTPerspective.arXivpreprint MartinChadwick,MiaGlaese,SusannahYoung,LucyCampbell-Gillingham,
arXiv:2306.06615(2023). GeoffreyIrving,etal.2022.Teachinglanguagemodelstosupportanswerswith
[78] XiangLi,ZhenyuLi,ChenShi,YongXu,QingDu,MingkuiTan,JunHuang, verifiedquotes.arXivpreprintarXiv:2203.11147(2022).
andWeiLin.2024.AlphaFin:BenchmarkingFinancialAnalysiswithRetrieval- [101] AristidesMilios,SivaReddy,andDzmitryBahdanau.2023.In-contextlearning
AugmentedStock-ChainFramework.arXivpreprintarXiv:2403.12582(2024). fortextclassificationwithmanylabels.InProceedingsofthe1stGenBench
[79] XinzeLi,ZhenghaoLiu,ChenyanXiong,ShiYu,YuGu,ZhiyuanLiu,and Workshopon(Benchmarking)GeneralisationinNLP.173–184.
GeYu.2023. Structure-AwareLanguageModelPretrainingImprovesDense [102] SewonMin,XinxiLyu,AriHoltzman,MikelArtetxe,MikeLewis,Hannaneh
RetrievalonStructuredData.InThe61stAnnualMeetingOfTheAssociationFor Hajishirzi,andLukeZettlemoyer.2022. RethinkingtheRoleofDemonstra-
ComputationalLinguistics. tions:WhatMakesIn-ContextLearningWork?.InEMNLP.Associationfor
[80] XiaonanLi,KaiLv,HangYan,TianyangLin,WeiZhu,YuanNi,GuotongXie, ComputationalLinguistics,11048–11064.
XiaolingWang,andXipengQiu.2023. UnifiedDemonstrationRetrieverfor [103] SewonMin,JulianMichael,HannanehHajishirzi,andLukeZettlemoyer.2020.
In-ContextLearning.InACL(1).AssociationforComputationalLinguistics, AmbigQA:AnsweringAmbiguousOpen-domainQuestions.InEMNLP(1).As-
4644–4668. sociationforComputationalLinguistics,5783–5797.
[81] XiaoqianLi,ErcongNie,andShengLiang.2023.FromClassificationtoGen- [104] SewonMin,WeijiaShi,MikeLewis,XilunChen,Wen-tauYih,HannanehHaeration:InsightsintoCrosslingualRetrievalAugmentedICL.InNeurIPS2023 jishirzi,andLukeZettlemoyer.2023.NonparametricMaskedLanguageModel-
WorkshoponInstructionTuningandInstructionFollowing. ing.InACL(Findings).AssociationforComputationalLinguistics,2097–2118.
[82] XiaonanLiandXipengQiu.2023.MoT:Memory-of-ThoughtEnablesChatGPT [105] NoorNashid,MiftaSintaha,andAliMesbah.2023. Retrieval-basedprompt
toSelf-Improve.InProceedingsofthe2023ConferenceonEmpiricalMethods selectionforcode-relatedfew-shotlearning.In2023IEEE/ACM45thInternational
inNaturalLanguageProcessing.AssociationforComputationalLinguistics, ConferenceonSoftwareEngineering(ICSE).IEEE,2450–2462.
Singapore,6354–6374. [106] NeilO’Hare,PalomaDeJuan,RossanoSchifanella,YunlongHe,DaweiYin,
[83] XiangLisaLiandPercyLiang.2021. Prefix-Tuning:OptimizingContinuous andYiChang.2016.Leveraginguserinteractionsignalsforwebimagesearch.
PromptsforGeneration.InACL/IJCNLP(1).AssociationforComputational InProceedingsofthe39thInternationalACMSIGIRconferenceonResearchand
Linguistics,4582–4597. DevelopmentinInformationRetrieval.559–568.
[84] ZonglinLi,RuiqiGuo,andSanjivKumar.2022.Decoupledcontextprocessing [107] LongOuyang,JeffreyWu,XuJiang,DiogoAlmeida,CarrollWainwright,Pamela
forcontextaugmentedlanguagemodeling. AdvancesinNeuralInformation Mishkin,ChongZhang,SandhiniAgarwal,KatarinaSlama,AlexRay,etal.2022.
ProcessingSystems35(2022),21698–21710. Traininglanguagemodelstofollowinstructionswithhumanfeedback.Advances
[85] DemiaoLin.2024.RevolutionizingRetrieval-AugmentedGenerationwithEn- inneuralinformationprocessingsystems35(2022),27730–27744.
hancedPDFStructureRecognition.arXivpreprintarXiv:2401.12599(2024). [108] Md.RizwanParvez,WasiUddinAhmad,SaikatChakraborty,BaishakhiRay,
[86] XiVictoriaLin,XilunChen,MingdaChen,WeijiaShi,MariaLomeli,Richard andKai-WeiChang.2021. RetrievalAugmentedCodeGenerationandSum-
James,PedroRodriguez,JacobKahn,GergelySzilvasy,MikeLewis,etal.2023. marization.InEMNLP(Findings).AssociationforComputationalLinguistics,
RA-DIT:Retrieval-AugmentedDualInstructionTuning.InTheTwelfthInterna- 2719–2734.
tionalConferenceonLearningRepresentations. [109] FabioPetroni,PatrickS.H.Lewis,AleksandraPiktus,TimRocktäschel,Yuxiang
[87] HaochenLiu,JamellDacon,WenqiFan,HuiLiu,ZitaoLiu,andJiliangTang.2020. Wu,AlexanderH.Miller,andSebastianRiedel.2020. HowContextAffects
DoesGenderMatter?TowardsFairnessinDialogueSystems.InProceedingsof LanguageModels’FactualPredictions.InAKBC.
the28thInternationalConferenceonComputationalLinguistics.4403–4416. [110] FabioPetroni,TimRocktäschel,PatrickLewis,AntonBakhtin,YuxiangWu,
[88] HaochenLiu,YiqiWang,WenqiFan,XiaoruiLiu,YaxinLi,ShailiJain,Yunhao AlexanderHMiller,andSebastianRiedel.2019.Languagemodelsasknowledge
Liu,AnilKJain,andJiliangTang.2021. Trustworthyai:Acomputational bases?arXivpreprintarXiv:1909.01066(2019).
perspective.arXivpreprintarXiv:2107.06641(2021). [111] GabrielPoesia,AlexPolozov,VuLe,AshishTiwari,GustavoSoares,Christopher
[89] JiachangLiu,DinghanShen,YizheZhang,BillDolan,LawrenceCarin,and Meek,andSumitGulwani.2022.Synchromesh:ReliableCodeGenerationfrom
WeizhuChen.2022. WhatMakesGoodIn-ContextExamplesforGPT-3?.In Pre-trainedLanguageModels.InICLR.OpenReview.net.
DeeLIO@ACL.AssociationforComputationalLinguistics,100–114. [112] AnupamPurwarandRahulSundar.2023.KeywordAugmentedRetrieval:Novel
[90] ShengchaoLiu,WeiliNie,ChengpengWang,JiaruiLu,ZhuoranQiao,LingLiu, frameworkforInformationRetrievalintegratedwithspeechinterface.arXiv
JianTang,ChaoweiXiao,andAnimashreeAnandkumar.2023. Multi-modal preprintarXiv:2310.04205(2023).
moleculestructure–textmodelfortext-basedretrievalandediting. Nature [113] AlecRadford,JongWookKim,ChrisHallacy,AdityaRamesh,GabrielGoh,Sand-
MachineIntelligence5,12(2023),1447–1457. hiniAgarwal,GirishSastry,AmandaAskell,PamelaMishkin,JackClark,etal.
[91] YeLiu,SemihYavuz,RuiMeng,DragomirRadev,CaimingXiong,andYingbo 2021.Learningtransferablevisualmodelsfromnaturallanguagesupervision.
Zhou.2022. Uni-Parser:UnifiedSemanticParserforQuestionAnswering InInternationalconferenceonmachinelearning.PMLR,8748–8763.
onKnowledgeBaseandDatabase.InEMNLP.AssociationforComputational [114] AlecRadford,KarthikNarasimhan,TimSalimans,IlyaSutskever,etal.2018.
Linguistics,8858–8869. Improvinglanguageunderstandingbygenerativepre-training.(2018).
[92] AlejandroLozano,ScottLFleming,Chia-ChunChiang,andNigamShah.2023. [115] Alec Radford, Jeffrey Wu, Rewon Child, David Luan, Dario Amodei, Ilya
Clinfo.ai:Anopen-sourceretrieval-augmentedlargelanguagemodelsystemfor Sutskever,etal.2019.Languagemodelsareunsupervisedmultitasklearners.
answeringmedicalquestionsusingscientificliterature.InPACIFICSYMPOSIUM OpenAIblog1,8(2019),9.
ONBIOCOMPUTING2024.WorldScientific,8–23. [116] ColinRaffel,NoamShazeer,AdamRoberts,KatherineLee,SharanNarang,
[93] PanLu,LiangQiu,Kai-WeiChang,YingNianWu,Song-ChunZhu,Tanmay MichaelMatena,YanqiZhou,WeiLi,andPeterJLiu.2020.Exploringthelimits
Rajpurohit,PeterClark,andAshwinKalyan.2023. DynamicPromptLearn- oftransferlearningwithaunifiedtext-to-texttransformer.Journalofmachine
ingviaPolicyGradientforSemi-structuredMathematicalReasoning.InICLR. learningresearch21,140(2020),1–67.
OpenReview.net. [117] OriRam,YoavLevine,ItayDalmedigos,DorMuhlgay,AmnonShashua,Kevin
[94] YuLu,JunweiBao,YanSong,ZichenMa,ShuguangCui,YouzhengWu,and Leyton-Brown,andYoavShoham.2023.In-contextretrieval-augmentedlan-
XiaodongHe.2021.RevCore:Review-AugmentedConversationalRecommen- guagemodels.TransactionsoftheAssociationforComputationalLinguistics11
dation.InACL/IJCNLP(Findings)(FindingsofACL,Vol.ACL/IJCNLP2021).As- (2023),1316–1331.
sociationforComputationalLinguistics,1161–1173. [118] OriRam,GalShachaf,OmerLevy,JonathanBerant,andAmirGloberson.2022.
[95] HongyinLuo,TianhuaZhang,Yung-SungChuang,YuanGong,YoonKim, LearningtoRetrievePassageswithoutSupervision.InNAACL-HLT.Association
XixinWu,HelenMeng,andJamesR.Glass.2023.SearchAugmentedInstruction forComputationalLinguistics,2687–2700.
Learning.InEMNLP(Findings).AssociationforComputationalLinguistics,3717– [119] ParikshitRamandAlexanderGGray.2012.Maximuminner-productsearch
3729. usingconetrees.InProceedingsofthe18thACMSIGKDDinternationalconference
[96] ManLuo,XinXu,ZhuyunDai,PanupongPasupat,MehranKazemi,ChittaBaral, onKnowledgediscoveryanddatamining.931–939.
VaivaImbrasaite,andVincentYZhao.2023.Dr.icl:Demonstration-retrieved [120] JuanRamosetal.2003.Usingtf-idftodeterminewordrelevanceindocument
in-contextlearning.arXivpreprintarXiv:2305.14128(2023). queries.InProceedingsofthefirstinstructionalconferenceonmachinelearning,
[97] ChangMa,HaitengZhao,LinZheng,JiayiXin,QintongLi,LijunWu,Zhi- Vol.242.Citeseer,29–48.
hongDeng,YangLu,QiLiu,andLingpengKong.2023. RetrievedSequence [121] RitaRamos,BrunoMartins,DesmondElliott,andYovaKementchedjhieva.2023.
AugmentationforProteinRepresentationLearning.bioRxiv(2023),2023–02. Smallcap:lightweightimagecaptioningpromptedwithretrievalaugmenta-
[98] XinbeiMa,YeyunGong,PengchengHe,HaiZhao,andNanDuan.2023.Query tion.InProceedingsoftheIEEE/CVFConferenceonComputerVisionandPattern
rewriting for retrieval-augmented large language models. arXiv preprint Recognition.2840–2849.
arXiv:2305.14283(2023). [122] BenjaminZ.ReichmanandLarryHeck.2024.Retrieval-AugmentedGeneration:
[99] SeijiMaekawa,HayateIso,SairamGurajada,andNikitaBhutani.2024.Retrieval IsDensePassageRetrievalRetrieving?CoRRabs/2402.11035(2024).
HelpsorHurts?ADeeperDiveintotheEfficacyofRetrievalAugmentationto
16

<!-- Page 17 -->

ASurveyonRAGMeetingLLMs:TowardsRetrieval-AugmentedLargeLanguageModels Conference’17,July2017,Washington,DC,USA
[123] NilsReimersandIrynaGurevych.2019.Sentence-BERT:SentenceEmbeddings WhenandWhattoRetrieveforLLMs.arXivpreprintarXiv:2402.12052(2024).
usingSiameseBERT-Networks.InProceedingsofthe2019ConferenceonEmpirical [147] NandanThakur,LuizBonifacio,XinyuZhang,OdunayoOgundepo,Ehsan
MethodsinNaturalLanguageProcessingandthe9thInternationalJointConference Kamalloo, David Alfonso-Hermelo, Xiaoguang Li, Qun Liu, Boxing Chen,
onNaturalLanguageProcessing(EMNLP-IJCNLP).3982–3992. MehdiRezagholizadeh,etal.2023. NoMIRACL:KnowingWhenYouDon’t
[124] YubingRen,YananCao,PingGuo,FangFang,WeiMa,andZhengLin.2023. KnowforRobustMultilingualRetrieval-AugmentedGeneration.arXivpreprint
Retrieve-and-sample:Document-leveleventargumentextractionviahybridre- arXiv:2312.11361(2023).
trievalaugmentation.InProceedingsofthe61stAnnualMeetingoftheAssociation [148] HugoTouvron,LouisMartin,KevinStone,PeterAlbert,AmjadAlmahairi,
forComputationalLinguistics(Volume1:LongPapers).293–306. YasmineBabaei,NikolayBashlykov,SoumyaBatra,PrajjwalBhargava,Shruti
[125] StephenRobertson,HugoZaragoza,etal.2009. Theprobabilisticrelevance Bhosale,etal.2023. Llama2:Openfoundationandfine-tunedchatmodels.
framework:BM25andbeyond.FoundationsandTrends®inInformationRetrieval arXivpreprintarXiv:2307.09288(2023).
3,4(2009),333–389. [149] HarshTrivedi,NiranjanBalasubramanian,TusharKhot,andAshishSabharwal.
[126] OhadRubin,JonathanHerzig,andJonathanBerant.2022.LearningToRetrieve 2023.InterleavingRetrievalwithChain-of-ThoughtReasoningforKnowledge-
PromptsforIn-ContextLearning.InNAACL-HLT.AssociationforComputa- IntensiveMulti-StepQuestions.InThe61stAnnualMeetingOfTheAssociation
tionalLinguistics,2655–2671. ForComputationalLinguistics.
[127] SaraSarto,MarcellaCornia,LorenzoBaraldi,andRitaCucchiara.2022.Retrieval- [150] LifuTu,CaimingXiong,andYingboZhou.2022.Prompt-TuningCanBeMuch
augmentedtransformerforimagecaptioning.InProceedingsofthe19thinterna- BetterThanFine-TuningonCross-lingualUnderstandingWithMultilingual
tionalconferenceoncontent-basedmultimediaindexing.1–7. LanguageModels.InEMNLP(Findings).AssociationforComputationalLinguis-
[128] TimoSchick,JaneDwivedi-Yu,RobertoDessì,RobertaRaileanu,MariaLomeli, tics,5478–5485.
EricHambro,LukeZettlemoyer,NicolaCancedda,andThomasScialom.2024. [151] TuVu,BrianLester,NoahConstant,RamiAl-Rfou’,andDanielCer.2022.SPoT:
Toolformer:Languagemodelscanteachthemselvestousetools.Advancesin BetterFrozenModelAdaptationthroughSoftPromptTransfer.InACL(1).
NeuralInformationProcessingSystems36(2024). AssociationforComputationalLinguistics,5039–5059.
[129] MinjoonSeo,JinhyukLee,TomKwiatkowski,AnkurPParikh,AliFarhadi,and [152] AnteWang,LinfengSong,QiLiu,HaitaoMi,LongyueWang,ZhaopengTu,
HannanehHajishirzi.2019.Real-timeopen-domainquestionansweringwith JinsongSu,andDongYu.2023.Search-engine-augmenteddialogueresponse
dense-sparsephraseindex.arXivpreprintarXiv:1906.05807(2019). generationwithcheaplysupervisedqueryproduction.ArtificialIntelligence319
[130] ZhihongShao,YeyunGong,MinlieHuang,NanDuan,WeizhuChen,etal. (2023),103874.

## EnhancingRetrieval-AugmentedLargeLanguageModelswithIterative [153] BoxinWang,WeiPing,PengXu,LawrenceMcAfee,ZihanLiu,Mohammad

Retrieval-GenerationSynergy.InThe2023ConferenceonEmpiricalMethodsin Shoeybi,YiDong,OleksiiKuchaiev,BoLi,ChaoweiXiao,etal.2023.ShallWe
NaturalLanguageProcessing. PretrainAutoregressiveLanguageModelswithRetrieval?AComprehensive
[131] FuminShen,WeiLiu,ShaotingZhang,YangYang,andHengTaoShen.2015. Study.InProceedingsofthe2023ConferenceonEmpiricalMethodsinNatural
Learningbinarycodesformaximuminnerproductsearch.InProceedingsofthe LanguageProcessing.7763–7786.
IEEEInternationalConferenceonComputerVision.4148–4156. [154] HanbingWang,XiaoruiLiu,WenqiFan,XiangyuZhao,VenkataramanaKini,
[132] ShellySheynin,OronAshual,AdamPolyak,UrielSinger,OranGafni,Eliya DevendraYadav,FeiWang,ZhenWen,JiliangTang,andHuiLiu.2024. Re-
Nachmani,andYanivTaigman.2023. kNN-Diffusion:ImageGenerationvia thinkingLargeLanguageModelArchitecturesforSequentialRecommendations.
Large-ScaleRetrieval.InICLR.OpenReview.net. arXivpreprintarXiv:2402.09543(2024).
[133] KaizeShi,XueyaoSun,QingLi,andGuandongXu.2024.CompressingLong [155] HaoyuWang,TuoZhao,andJingGao.2024.BlendFilter:AdvancingRetrieval-
ContextforEnhancingRAGwithAMR-basedConceptDistillation. arXiv AugmentedLargeLanguageModelsviaQueryGenerationBlendingandKnowlpreprintarXiv:2405.03085(2024). edgeFiltering.arXivpreprintarXiv:2402.11129(2024).
[134] PengShi,RuiZhang,HeBai,andJimmyLin.2022. XRICL:Cross-lingual [156] LiangWang,NanYang,andFuruWei.2023.Query2doc:QueryExpansionwith
Retrieval-AugmentedIn-ContextLearningforCross-lingualText-to-SQLSe- LargeLanguageModels.InEMNLP.AssociationforComputationalLinguistics,
manticParsing.InEMNLP(Findings).AssociationforComputationalLinguistics, 9414–9423.
5248–5259. [157] LiangWang,NanYang,andFuruWei.2024.LearningtoRetrieveIn-ContextEx-
[135] WeijiaShi,SewonMin,MichihiroYasunaga,MinjoonSeo,RichJames,Mike amplesforLargeLanguageModels.InEACL(1).AssociationforComputational
Lewis,LukeZettlemoyer,andWen-tauYih.2023.Replug:Retrieval-augmented Linguistics,1752–1767.
black-boxlanguagemodels.arXivpreprintarXiv:2301.12652(2023). [158] Xintao Wang, Qianwen Yang, Yongting Qiu, Jiaqing Liang, Qianyu He,
[136] GuyShtar.2021.Multimodalmachinelearningfordrugknowledgediscovery. ZhouhongGu,YanghuaXiao,andWeiWang.2023. Knowledgpt:Enhanc-
InProceedingsofthe14thACMInternationalConferenceonWebSearchandData inglargelanguagemodelswithretrievalandstorageaccessonknowledgebases.
Mining.1115–1116. arXivpreprintarXiv:2308.11761(2023).
[137] KurtShuster,SpencerPoff,MoyaChen,DouweKiela,andJasonWeston.2021. [159] YileWang,PengLi,MaosongSun,andYangLiu.2023.Self-KnowledgeGuided
RetrievalAugmentationReducesHallucinationinConversation.InEMNLP RetrievalAugmentationforLargeLanguageModels.InThe2023Conferenceon
(Findings).AssociationforComputationalLinguistics,3784–3803. EmpiricalMethodsinNaturalLanguageProcessing.
[138] SuzannaSiaandKevinDuh.2023.In-contextlearningasmaintainingcoherency: [160] ZichaoWang,WeiliNie,ZhuoranQiao,ChaoweiXiao,RichardG.Baraniuk,and
Astudyofon-the-flymachinetranslationusinglargelanguagemodels.arXiv AnimaAnandkumar.2023.Retrieval-basedControllableMoleculeGeneration.
preprintarXiv:2305.03573(2023). InICLR.OpenReview.net.
[139] DevendraSingh,SivaReddy,WillHamilton,ChrisDyer,andDaniYogatama. [161] ZifengWang,ZichenWang,BalasubramaniamSrinivasan,VassilisNIoannidis,

## End-to-endtrainingofmulti-documentreaderandretrieverforopen- HuzefaRangwala,andRishitaAnubhai.2023.BioBridge:BridgingBiomedical

domainquestionanswering.AdvancesinNeuralInformationProcessingSystems FoundationModelsviaKnowledgeGraph. arXivpreprintarXiv:2310.03320
34(2021),25968–25981. (2023).
[140] AmitSinghaletal.2001.Moderninformationretrieval:Abriefoverview.IEEE [162] JasonWei,XuezhiWang,DaleSchuurmans,MaartenBosma,FeiXia,EdChi,
DataEng.Bull.24,4(2001),35–43. QuocVLe,DennyZhou,etal.2022.Chain-of-thoughtpromptingelicitsreason-
[141] ShamaneSiriwardhana,RivinduWeerasekera,ElliottWen,TharinduKalu- inginlargelanguagemodels.Advancesinneuralinformationprocessingsystems
arachchi,RajibRana,andSurangaNanayakkara.2023.Improvingthedomain 35(2022),24824–24837.
adaptationofretrievalaugmentedgeneration(RAG)modelsforopendomain [163] JundaWu,Cheng-ChunChang,TongYu,ZhankuiHe,JianingWang,Yupeng
questionanswering.TransactionsoftheAssociationforComputationalLinguistics Hou,andJulianMcAuley.2024.CoRAL:CollaborativeRetrieval-Augmented
11(2023),1–17. LargeLanguageModelsImproveLong-tailRecommendation. arXivpreprint
[142] KarenSparckJones.1972.Astatisticalinterpretationoftermspecificityandits arXiv:2403.06447(2024).
applicationinretrieval.Journalofdocumentation28,1(1972),11–21. [164] LedellWu,FabioPetroni,MartinJosifoski,SebastianRiedel,andLukeZettle-
[143] HongjinSu,JungoKasai,ChenHenryWu,WeijiaShi,TianluWang,JiayiXin, moyer.2020.ScalableZero-shotEntityLinkingwithDenseEntityRetrieval.In
RuiZhang,MariOstendorf,LukeZettlemoyer,NoahA.Smith,andTaoYu.2023. EMNLP(1).AssociationforComputationalLinguistics,6397–6407.
SelectiveAnnotationMakesLanguageModelsBetterFew-ShotLearners.In [165] YuhuaiWu,MarkusNormanRabe,DeLesleyHutchins,andChristianSzegedy.
ICLR.OpenReview.net. 2022.MemorizingTransformers.InICLR.OpenReview.net.
[144] FangSun,ZhihaoZhan,HongyuGuo,MingZhang,andJianTang.2023.Graphvf: [166] MiaoXiong,ZhiyuanHu,XinyangLu,YifeiLi,JieFu,JunxianHe,andBryan
Controllableprotein-specific3dmoleculegenerationwithvariationalflow.arXiv Hooi.2023. Canllmsexpresstheiruncertainty?anempiricalevaluationof
preprintarXiv:2304.12825(2023). confidenceelicitationinllms.arXivpreprintarXiv:2306.13063(2023).
[145] ZitengSun,AnandaTheerthaSuresh,JaeHunRo,AhmadBeirami,Himanshu [167] BenfengXu,ChunxuZhao,WenbinJiang,PengFeiZhu,SongtaiDai,Chao
Jain,andFelixYu.2024.Spectr:Fastspeculativedecodingviaoptimaltransport. Pang,ZhuoSun,ShuohuanWang,andYuSun.2023. Retrieval-augmented
AdvancesinNeuralInformationProcessingSystems36(2024). domainadaptationoflanguagemodels.InProceedingsofthe8thWorkshopon
[146] JiejunTan,ZhichengDou,YutaoZhu,PeidongGuo,KunFang,andJi-Rong RepresentationLearningforNLP(RepL4NLP2023).54–64.
Wen.2024.SmallModels,BigInsights:LeveragingSlimProxyModelsToDecide
17

<!-- Page 18 -->

Conference’17,July2017,Washington,DC,USA WenqiFan,YujuanDing,LiangboNing,ShijieWang,HengyunLi,DaweiYin,Tat-SengChua,andQingLi
[168] FangyuanXu,WeijiaShi,andEunsolChoi.2023.RECOMP:Improvingretrieval- Linguistics(Volume1:LongPapers).2421–2436.
augmentedLMswithcontextcompressionandselectiveaugmentation.InThe [185] DaoguangZan,BeiChen,ZeqiLin,BeiGuan,YongjiWang,andJian-Guang
TwelfthInternationalConferenceonLearningRepresentations. Lou.2022.WhenLanguageModelMeetsPrivateLibrary.InEMNLP(Findings).
[169] HuXu,BingLiu,LeiShu,andPhilipS.Yu.2019.BERTPost-TrainingforReview AssociationforComputationalLinguistics,277–288.
ReadingComprehensionandAspect-basedSentimentAnalysis.InNAACL-HLT [186] ShenglaiZeng,JiankunZhang,PengfeiHe,YueXing,YidingLiu,HanXu,Jie
(1).AssociationforComputationalLinguistics,2324–2335. Ren,ShuaiqiangWang,DaweiYin,YiChang,etal.2024.TheGoodandThe
[170] JitaoXu,Josep-MariaCrego,andJeanSenellart.2020.Boostingneuralmachine Bad:ExploringPrivacyIssuesinRetrieval-AugmentedGeneration(RAG).arXiv
translationwithsimilartranslations.InAnnualMeetingoftheAssociationfor preprintarXiv:2402.16893(2024).
ComputationalLinguistics.AssociationforComputationalLinguistics,1570– [187] BoyuZhang,HongyangYang,TianyuZhou,MuhammadAliBabar,andXiao-

## YangLiu.2023.Enhancingfinancialsentimentanalysisviaretrievalaugmented

[171] JingXu,ArthurSzlam,andJasonWeston.2022.BeyondGoldfishMemory:Long- largelanguagemodels.InProceedingsoftheFourthACMInternationalConference
TermOpen-DomainConversation.InACL(1).AssociationforComputational onAIinFinance.349–356.
Linguistics,5180–5197. [188] HouyuZhang,ZhenghaoLiu,ChenyanXiong,andZhiyuanLiu.2020.Grounded
[172] ShichengXu,LiangPang,HuaweiShen,XueqiCheng,andTat-sengChua.2023. ConversationGenerationasGuidedTraversesinCommonsenseKnowledge
Search-in-the-chain:Towardstheaccurate,credibleandtraceablecontentgen- Graphs.InACL.AssociationforComputationalLinguistics,2031–2043.
erationforcomplexknowledge-intensivetasks.arXivpreprintarXiv:2304.14732 [189] JiahaoZhang,RuiXue,WenqiFan,XinXu,QingLi,JianPei,andXiaoruiLiu.
(2023). 2024. Linear-TimeGraphNeuralNetworksforScalableRecommendations.
[173] HaoyanYang,ZhitaoLi,YongZhang,JianzongWang,NingCheng,MingLi, arXivpreprintarXiv:2402.13973(2024).
andJingXiao.2023. PRCA:FittingBlack-BoxLargeLanguageModelsfor [190] YunxiangZhang,MuhammadKhalifa,LajanugenLogeswaran,MoontaeLee,
RetrievalQuestionAnsweringviaPluggableReward-DrivenContextualAdapter. HonglakLee,andLuWang.2023.Merginggeneratedandretrievedknowledge
InEMNLP.AssociationforComputationalLinguistics,5364–5375. foropen-domainQA.arXivpreprintarXiv:2310.14393(2023).
[174] LingYang,ZhilinHuang,XiangxinZhou,MinkaiXu,WentaoZhang,YuWang, [191] ZhuoshengZhang,AstonZhang,MuLi,andAlexSmola.2023.AutomaticChain
XiawuZheng,WenmingYang,RonODror,ShendaHong,etal.2023.PromptofThoughtPromptinginLargeLanguageModels.InICLR.OpenReview.net.
based3dmoleculardiffusionmodelsforstructure-baseddrugdesign.(2023). [192] PenghaoZhao,HailinZhang,QinhanYu,ZhengrenWang,YuntengGeng,
[175] Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik R. Fangcheng Fu, Ling Yang, Wentao Zhang, and Bin Cui. 2024. Retrieval-
Narasimhan,andYuanCao.2023.ReAct:SynergizingReasoningandActingin AugmentedGenerationforAI-GeneratedContent:ASurvey. arXivpreprint
LanguageModels.InICLR.OpenReview.net. arXiv:2402.19473(2024).
[176] JiachengYe,ZhiyongWu,JiangtaoFeng,TaoYu,andLingpengKong.2023. [193] RuochenZhao,HailinChen,WeishiWang,FangkaiJiao,XuanLongDo,Cheng-
Compositionalexemplarsforin-contextlearning.InInternationalConferenceon weiQin,BoshengDing,XiaobaoGuo,MinzhiLi,XingxuanLi,etal.2023.Re-
MachineLearning.PMLR,39818–39833. trievingmultimodalinformationforaugmentedgeneration:Asurvey.arXiv
[177] YunhuYe,BinyuanHui,MinYang,BinhuaLi,FeiHuang,andYongbinLi.2023.
preprintarXiv:2303.10868(2023).
LargeLanguageModelsareVersatileDecomposers:DecomposingEvidenceand [194] WayneXinZhao,KunZhou,JunyiLi,TianyiTang,XiaoleiWang,YupengHou,
QuestionsforTable-basedReasoning.InSIGIR.ACM,174–184. YingqianMin,BeichenZhang,JunjieZhang,ZicanDong,etal.2023.Asurvey
[178] AntonioJimenoYepes,YaoYou,JanMilczek,SebastianLaverde,andLeahLi.
oflargelanguagemodels.arXivpreprintarXiv:2303.18223(2023).

### FinancialReportChunkingforEffectiveRetrievalAugmentedGeneration. [195] ZihuaiZhao,WenqiFan,JiatongLi,YunqingLiu,XiaoweiMei,YiqiWang,Zhen

arXivpreprintarXiv:2402.05131(2024). Wen,FeiWang,XiangyuZhao,JiliangTang,etal.2024.Recommendersystems
[179] DaweiYin,YueningHu,JiliangTang,TimDaly,MianweiZhou,HuaOuyang,
intheeraoflargelanguagemodels(llms).IEEETransactionsonKnowledgeand
JianhuiChen,ChangsungKang,HongboDeng,ChikashiNobata,etal.2016.
DataEngineering(2024).
Rankingrelevanceinyahoosearch.InProceedingsofthe22ndACMSIGKDD [196] ZexuanZhong,TaoLei,andDanqiChen.2022.TrainingLanguageModelswith
InternationalConferenceonKnowledgeDiscoveryandDataMining.323–332. MemoryAugmentation.In2022ConferenceonEmpiricalMethodsinNatural
[180] DaniYogatama,CypriendeMassond’Autume,andLingpengKong.2021.Adap-
LanguageProcessing,EMNLP2022.
tivesemiparametriclanguagemodels.TransactionsoftheAssociationforCom- [197] ShuyanZhou,UriAlon,FrankFXu,ZhengbaoJiang,andGrahamNeubig.
putationalLinguistics9(2021),362–373. 2022.Docprompting:Generatingcodebyretrievingthedocs.InTheEleventh
[181] OriYoran,TomerWolfson,OriRam,andJonathanBerant.2023. Making
InternationalConferenceonLearningRepresentations.
Retrieval-AugmentedLanguageModelsRobusttoIrrelevantContext.InThe [198] YinZhu,ZhilingLuo,andGongCheng.2023. FurthestReasoningwithPlan
TwelfthInternationalConferenceonLearningRepresentations. Assessment:StableReasoningPathwithRetrieval-AugmentedLargeLanguage
[182] WenhaoYu,DanIter,ShuohangWang,YichongXu,MingxuanJu,Soumya
Models.arXivpreprintarXiv:2309.12767(2023).
Sanyal,ChenguangZhu,MichaelZeng,andMengJiang.2023.Generaterather [199] YinghaoZhu,ChangyuRen,ShiyunXie,ShukaiLiu,HangyuanJi,Zixiang
thanRetrieve:LargeLanguageModelsareStrongContextGenerators.InICLR. Wang,TaoSun,LongHe,ZhoujunLi,XiZhu,etal.2024.REALM:RAG-Driven
OpenReview.net. EnhancementofMultimodalElectronicHealthRecordsAnalysisviaLarge
[183] WenhaoYu,ZhihanZhang,ZhenwenLiang,MengJiang,andAshishSabharwal.
LanguageModels.arXivpreprintarXiv:2402.07016(2024).

### Improvinglanguagemodelsviaplug-and-playretrievalfeedback.arXiv [200] WeiZou,RunpengGeng,BinghuiWang,andJinyuanJia.2024.PoisonedRAG:

preprintarXiv:2305.14002(2023). KnowledgePoisoningAttackstoRetrieval-AugmentedGenerationofLarge
[184] ZichunYu,ChenyanXiong,ShiYu,andZhiyuanLiu.2023. Augmentation-
LanguageModels.arXivpreprintarXiv:2402.07867(2024).
AdaptedRetrieverImprovesGeneralizationofLanguageModelsasGenericPlug-
In.InProceedingsofthe61stAnnualMeetingoftheAssociationforComputational
18

## Tables

**Table (Page 3):**

| RAG Framework/Pipeline |
|---|
| (Iz 2 a F 0 c i 2 D a 1 r ) d, (T I 2 R r 0 i C v 2 e o 3 d T ) i, (S R h E i, P 2 L 0 U 2 G 3) AA 20 R 2 ( 3 Y ) u, SKR 20 ( 2 W 3 a ) ng, ( R Yu E , F 2 E 0 E 2 D 3) (A S s e a lf i, - R 20 A 2 G 3) To 2 C 0 2 (K 3 i ) m, (Kh k a 2 N n 0 N d 1 - e 9 L l ) M wal, (G R u E u, A 2 L 0 M 20) RAG 20 ( 2 L 0 e ) wis, (K S 2 o E 0 m - 2 F 1 e iD ) ili, (B R o 2 r E 0 g T 2 e R 2 a O ) ud, ( O La p 2 z e 0 a n 2 r B i 2 d o ) o o u k , (K 2 h D 0 a S 2 tt P 2 a ) b, In- R ( 2 C R 0 A o a 2 L n m 3 M te ) , xt R ( E I 2 S T 0 T h E 2 G a R 3 o E ) - , N F ( 2 J L 0 ia A 2 n R 3 g ) E , RA 2 D 0 A 2 3 ( ) Xu, C (Z 2 O h 0 M a 2 n 3 B g ) O , (T S a li n m , 2 P 0 L 2 M 4) |


**Table (Page 3):**

| RAG Learning |
|---|
| REALM RAG (Lewis, E (S M in D g R h 2 , (B R o E rg T e R a O ud, (Iz A a t c la a s rd, ( R s A iri G w - a e r n d d h 2 a e n n a d , RE (W T a R n O g + , + RE IT T E G R E - N Self-RAG ( P Y R a C ng A , (Guu, 2020) 2020) 2021) 2022) 2023) 2023) 2023) (Shao, 2023) (Asai, 2023) 2023) |


**Table (Page 3):**

| Retriever Learning |
|---|
| (Kar D p P u R khin, (I F z i a D c - a K r D d, C ( o G n a t u ri t e ie v r e , r (H Fi o D fs -L ta ig tt h e t r, CEIL (Ye, UDR (Li, SAIL (Luo, RADA (Xu, ( R H E u V a E ng N , RA-DIT (Lin, 2020) 2021) 2022) 2023) 2023) 2023) 2023) 2023) 2023) 2023) EPR 20 ( 2 R 1 u ) bin, U (C 2 P h 0 R e 2 I n 3 S g ) E , Dr.I 2 C 0 L 2 3 (L ) uo, ( L 2 W L 0 a M 2 n 3 - g R ) , |


**Table (Page 3):**

| Pre-/Post-Retrieval Technique |
|---|
| (Yo S g P a A t L a M ma, ( R G e la 2 s G s, HyPE (Gao, Qu (W er a y n 2 g d , oc SAIL (Luo, RECOMP ( P Y R a C ng A , SlimPLM 2021) 2022) 2022) 2023) 2023) (Xu, 2023) 2023) (Tan, 2024) (A R g -B ra M w 2 a 5 l, QueryRewriter Ble (W nd a F ng il , ter 2022) (Ma, 2023) 2024) |


**Table (Page 12):**

| RETRO[6] |
|---|
| Fusion-in-Decoder[54] |


**Table (Page 12):**

| Ghazvininejadetal. [43] |
|---|
| KDBTS[14] |


**Table (Page 12):**

| RAG[74] |
|---|
| Atlas[55] |


**Table (Page 12):**

| DiPalma[26] |
|---|
| CoRAL[163] |


**Table (Page 12):**

| Docprompting[197] |
|---|
| Atlas[105] |


**Table (Page 12):**

| Clinfo.ai[92] |
|---|
| RetMol[160] |


**Table (Page 12):**

| Zhangetal.[187] |
|---|
| AlphaFin[78] |


**Table (Page 12):**

| Xricl[134] |
|---|
| Synchromesh[111], etc. |


**Table (Page 12):**

| BioBridge[161] |
|---|
| RSA[97] |
| Graphvf[144],etc. |
