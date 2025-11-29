---
title: "LLM Judge Evaluation Framework"
original_file: "./LLM_Judge_Evaluation_Framework.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["prompt-engineering", "llm", "rag", "evaluation"]
keywords: ["length", "citation", "len", "model", "generation", "control", "citations", "cited", "work", "linguistics"]
summary: "<!-- Page 1 -->

Improving Citation Text Generation: Overcoming Limitations in Length

### Control


### BiswadipMandal,XiangciLi,JessicaOuyang


### TheuniversityofTexasatDallas,Richardson,TX,USA

{biswadip.mandal,xiangci.li,jessica.ouyang}@utdallas.edu
Abstract Target:Parvezetal.(2018)explicitlymodelthetypeof
thenextwordinadditiontotheworditself. ### Akeychallengeincitationtextgenerationis

Baseline:Parvezetal.(2018)extendvanillaLMswith
thatthelengthofgeneratedtextoftendiffers
alanguagemodelto"
related_documents: []
---

# LLM Judge Evaluation Framework

<!-- Page 1 -->

Improving Citation Text Generation: Overcoming Limitations in Length

### Control


### BiswadipMandal,XiangciLi,JessicaOuyang


### TheuniversityofTexasatDallas,Richardson,TX,USA

{biswadip.mandal,xiangci.li,jessica.ouyang}@utdallas.edu
Abstract Target:Parvezetal.(2018)explicitlymodelthetypeof
thenextwordinadditiontotheworditself.

### Akeychallengeincitationtextgenerationis

Baseline:Parvezetal.(2018)extendvanillaLMswith
thatthelengthofgeneratedtextoftendiffers
alanguagemodeltomodelthecompatibilitybetween
fromthelengthofthetarget,loweringthequalcontextsentencesandlabels.However,theirapproach
ityofthegeneration. Whilepriorworkshave doesnotexplicitlyaddresstheproblemofnoisylabels.
investigatedlength-controlledgeneration,their
effectivenessdependsonknowingtheappropri- Oracle: Parvez et al. (2018) propose to use LM-
enhancementtoimproveentitytyping.
ategenerationlength. Inthiswork,wepresent
anin-depthstudyofthelimitationsofpredict-

### Target:...neural-basedmethods(Chuetal.,2016...)

ing scientific citation text length and explore learn to identify parallel sentences in the semantic
theuseofheuristicestimatesofdesiredlength. spaces.However,thesemethodsrequirelargeamounts
of parallel sentence pairs...which does not apply to
1 Introduction languageswithlimitedresources.
Baseline: ...proposals(Chuetal., 2016...) usethe
Citationtextgenerationforscientificarticlesisthe
corporatotrainmodelsandextractparallelsentences.
task of summarizing the content of a cited paper
asitrelatestothecitingpaper. Onekeychallenge Oracle: ...approaches (Chu et al., 2016...) extract
parallel sentences from comparable monolingual
isthatthelengthsofhuman-writtencitationsvary
corporausingneuralnetworks.However,thesemethods
greatly. For example, if the citing paper directly areonlyforasmallnumberoflanguagesanddonotuse
buildsontheapproachofthecitedpaper,thecita- anyexternalresourcessuchasdictionariesorcorpora.
tion text may be longer and more detailed; if the
citingpapermentionsthecitedpaperasoneamong Figure1: Examplesofgeneratedcitationsthataretoo
manysimilarbackgroundworks,thecitationmay long(top)ortooshort(bottom).
beshorter. Thechallengeforthegenerationmodel
istoproduceacitationthatisneithertoolong,contheappropriategenerationlength,ratherthanusing
tainingirrelevantorredundantinformation,nortoo
anarbitraryone(eg. asummarylengthlimit),has
short,lackingsufficientinformation.
received less attention. Additionally, what work

### Inthiswork,weusethedatasetofLietal.(2022)

existsonlengthprediction(Yangetal.,2020;Oka
andusetheirannotatedcitationspansasourgeneretal.,2020)hasbeenforthetaskofmachinetransationtargets. Weobservethatmanyofthecitations
lation,wherethelengthsoftheinputandoutputare
producedbyLietal.’slength-agnosticgeneration
correlatedbecausethetwomustbehighlysemanmodel are of a different length than the humanticallysimilar. Incontrast,forcitationgeneration,
writtentargets. Figure1showstwoexamplecitatheinputconsistsoftheabstractofthecitedpaper
tionsgeneratedbyLietal.’smodel,andFigure2
andthesurroundingcontextofthetargetcitation,
shows ahistogramoflengthdifferencesbetween
whiletheoutputisaconcisesummaryofthecited
targetcitationsandLietal.’soutput.
paperasitrelatestothecontext;thelengthofthe

### Inthiswork,weexperimentwithmitigatingthis

outputisnotnecessarilyrelatedtothatoftheinput.
lengthdifferencebypredictingandcontrollingthe
lengthofthegeneratedcitation. Controllinggener- Wetacklethechallengeofgeneratingcitations
ationlengthinencoder-decodermodelshasbeen thatarebothinformativeandofappropriatelength.
previously studied in Kikuchi et al. (2016a); Fan Ourmaincontributionsareasfollows:
etal.(2017);Liuetal.(2018). However,predicting • We demonstrate that controlling the length
4202
luJ
02
]LD.sc[
1v79941.7042:viXra

<!-- Page 2 -->

downstreamgenerationtask. WeuseLongformer

### Encoder-Decoder(LED;Beltagyetal.,2020)for

generation and the length-difference position encoding (LDPE) control approach of Takase and
Okazaki (2019), which uses the decoder’s positionalencodingtorepresenttheremaininggenerationlengthateachtimestep(AppendixA.1).
3.1 AutomaticLengthPrediction
Figure2: Lengthdifferenceintokensbetweenground

### FollowingLietal.(2022),theinputxtooursystem

truthcitationsandLietal.(2022)’sgeneratedcitations.
istheconcatenationofthecitingpaper’sintroductionsection;theparagraphcontainingthe(masked)
of generated citation produces a significant
target citation; and the citation mark (eg. “Smith
improvementintheirquality.
etal. (2023)"),title,andabstractofthecitedpaper.
• Wefindthatautomaticcitationlengthpredic-

### Topredictthecitationlength,wetaketheencoding

tionisverydifficult, andheuristiclengthesoftheCLS meta-tokenfromtheLEDencoderand
timatesgivebetterperformanceonthedownpass it through a feed-forward network (FF) to
streamcitationgenerationtask.
predictascalarvalueforlength. Wethenusethe
• Weprovideinsightsintothebehaviorofgenpredictedlengthtocontrolthelengthofthegenereratedcitationswhenlengthismodified.
atedcitation,allowingthelengthregressionmodel
to receive training updates from the downstream
2 RelatedWork
generationmodel(Equation1).
Citation Text Generation. Older, extractive ap-

### H = LED (x)

proachesselectsalientsentencesfromcitedpapers enc
toserveascitations(HoangandKan,2010;Huand leˆn = FF(H ) (1)

## <Cls>

Wan,2014;ChenandZhuge,2019),whilerecent yˆ= LED (H+LDPE(leˆn))
dec
workfocusesonabstractiveapproachestogenerate
citationsusingneuralseq2seqmodels(Xingetal., Weexplorethreeapproachesfortraininglength
2020;Geetal.,2021;Luuetal.,2021;Chenetal., regressionandcontrolledgeneration(Figure3).
2021;Lietal.,2022). However,nopriorworkhas Vanilla Multitasking. We jointly train length
investigatedthelengthdifferenceissueaddressed regressionandcitationgenerationusingmulti-task
in this work, nor attempted length prediction or learning. Wepassthepredictedlengthtothegenercontrolforcitationtextgeneration. ationmodelforlengthcontrolandbackpropagate
LengthPredictionandControl. Manyworks the generation loss through the length regression
havestudiedlengthcontrol(Kikuchietal.,2016b; module. Thetraininglossisgivenby:
Fan et al., 2018; Liu et al., 2018; Lakew et al.,
L = λ L +(1−λ )L (2)
all g gen g len
2019), but few have addressed length prediction.
Formachinetranslation,wheretheinputandoutput L andL aregeneration(cross-entropy)loss
gen len
lengthsarerelatedbasedontheirsharedsemantics, and regression (root mean square error) loss, re-
Yang et al. (2020) trained length prediction and spectively. We tried several values for λ , but as
g
generationjointly,buttheyusedlengthprediction wediscussinSection5,noneworkedverywell;he
onlyasanauxiliarytrainingtasktoimprovetrans- reportedresultsuseλ = 0.3.
g
lation. Okaetal.(2020)usedalengthprediction Scheduled Sampling Multitasking. We use
modeltocontrolatranslationmodel,butthetwo scheduledsampling(Bengioetal.,2015)tograduweretrainedseparatelyandusedinapipeline. allyintroducethepredictedlengthtothegeneration
model. Webeginbyusingthegroundtruthtarget
3 PredictingandControllingLength
lengthwithprobabilityp,initializedtoahighvalue
p ,andslowlydecreaseitusingexponentialdecay:

### Weexplorejointlypredictingandcontrollinglength 0

for citation generation. We experiment with a (epoch+ step+1 )
p = p 0 ∗k total_steps (3)
multi-task approach where the predicted length
controlsgeneration,allowingourlengthregression total_steps is the number of updates per epoch,
modeltoreceiveadditionaltrainingsignalfromthe and k is the decay rate; we use p = 0.99 and
0

<!-- Page 3 -->

Length Predicted

### Regressor Length

target length (scheduled sampling & teacher forcing)

### Citing & Longformer Longformer Generated


### Cited Papers Encoder Decoder Citation Span

Figure3: Architectureofourjointlengthpredictionandcontrolledcitationgenerationmodels.
k = 0.98. We do not tune these values, but set Model R-1 R-2 R-L
themhighinordertousethegroundtruthlength

### Oracle(targetlength) 0.295 0.083 0.224

formostoftraining. AswediscussinSection5,the Lietal.(2022) 0.271 0.079 0.212

### GPT-3.5Turbo 0.257 0.063 0.187

vanillalengthregressionmodelisnotveryaccurate,
sothisstrategyfavorsusinggroundtruthlength. VanillaMultitask 0.236 0.073 0.197

### ScheduledSampling 0.254 0.061 0.193

TeacherForcingPipelineWeuseahybridap-

### TeacherForcing 0.269 0.068 0.199

proach of Yang et al. (2020); Oka et al. (2020),

### H.Average 0.271 0.075 0.208

where length regression is trained as a separate H.CitationMarks 0.276 0.077 0.212
auxiliarytask,anditspredictionsareusedonlyat H.CitingPaper 0.280 0.077 0.223

### H.Random 0.241 0.065 0.187

testtime;thegenerationmodelistrainedusingthe
groundtruthlengthexclusively.
Table1: Performanceofpredictedandheuristiclengths
forcontrolledgeneration(ROUGEF1).
3.2 HeuristicLengthEstimates
We also experiment with simple statistical estimodels, Li et al. use LED (Beltagy et al., 2020)
matesofcitationlength;wetrainaseparatelengthwithdefaultsettingsandthesameinputformat.
controlledgenerationmodelforeachheuristic:
Finally, we use one-shot prompting with GPT-
• Averagecitationlengthacrossthetrainingset.
3.5 Turbo for length-controlled generation; the
• Citation marks: average length across the
prompt contains a demonstration example, all intrainingset,partitionedbythenumberofcitaputsusedbyourmodels,andthegroundtruthtarget
tionmarks(i.e. citedpapersreferenced).
citationlength. Thisbaselineteststhefeasibilityof
• Citingpaperaveragecitationlength,reflectcitationlengthcontrolbypromptingLLMs.
ingtheauthor’sstyle.
• Randomsamplefromthecitationlengthdis- 5 ResultsandAnalysis
tributionofthetrainingset.
5.1 Length-ControlledGeneration
4 ExperimentalSettings Table1showstheperformanceofourmultitaskapproachestocombininglengthpredictionandcon-
WeusetheCORWAdatasetofNLP-domainrelated trol,aswellasourlengthestimateheuristics,comworksectionsannotatedwithcitations;duetothe paredwiththebaselines.
length restriction, we refer the reader to Li et al. Citation length matters. The Oracle model
(2022)fordetailsofthedataset. achieves the best performance, a significant im-
We compare our experimental approaches to provementoverLietal.’slength-agnosticbaseline.
three baselines. First, we train a length control Further,theRandomheuristichasthelowestperformodelusingthegroundtruthtargetcitationlengths; mance,evenworsethanbaseline. Toillustratethe
this Oracle model also uses ground truth lengths importanceofgenerationlength,weseeinthefirst
attesttime,servingasanupperboundonlength- exampleinFigure1thattheTargetdoesnotcriticontrolledcitationgenerationperformance. cizethecitedpaper,andtheBaselineerroneously
Second, the length-agnostic model of Li et al. doesso; theOraclecitationfixesthisproblemby
(2022)servesasalowerboundthatlengthpredic- eliminating the extra sentence. An opposite case
tion and control should improve upon. Like our canbeseeninthesecondexample.

<!-- Page 4 -->

Model MAE ControlVariance len=20:...WangandLu(2018a)proposedasegmental
hypergraphmodelformodeling.

### Oracle - 0.0001


### GPT-3.5Turbo - 0.1852

len=50: ...Wang and Lu (2018a) proposed a
VanillaMultitask 15.04 0.5170 segmental hypergraph representation to model over-
ScheduledSampling 13.45 0.0138 lapping entities. However, their model is not able
TeacherForcing 13.84 0.0051 to capture the interactions between entities with
overlappingspans.
Table2: Performanceonlengthregressionandcontrol.

### Wang and Lu (2018a) abstract: ...We show

LengthregressionisevaluatedusingMAEinnumber thatourmodelbuiltontopofsuchanewrepresentation
oftokens;controlisevaluatedusingvariancebetween isabletocapturefeaturesandinteractionsthatcannot
desiredandgeneratedlength. becapturedbypreviousmodels...

### Figure4: Exampleofover-longcitationresultingina

Citation length is idiosyncratic. Of our aphallucinatedcriticismofthecitedpaper.
proaches,theCitingPaperheuristicperformsbest,
suggestingthatcitationlengthswithinapaperdo
not vary as much as citations from different pa- forcing the model to generate short citations repers. Thismayexplainwhylengthpredictionisso sults in vague, generic citations. Increasing the
challenging;citationlengthdependsontheauthor. length results in additional sentences being generated, which can comment about the methodol-
5.2 TheEffectsofLengthPrediction
ogy, add more information, or criticize the cited
Toexaminewhyjointlengthpredictionandcontrol paper. However,whenthedesiredlengthexceeds
was outperformed by the Citing Paper heuristic, the ground truth, the model begins to hallucinate
weusemeanabsoluteerror(MAE)tomeasureour these comments, especially criticisms. Figure 4
length regression performance. We evaluate the shows a citation being generated at both the corability of the generation model to control output rect (20 tokens) and a longer (50 token) length.
lengthusingControlVariance(Liuetal.,2018): Thelongergenerationhallucinatesacriticismthat
clearlycontradictsthecitedpaper’sabstract.
n
1 (cid:88)
Control_Var = 0.001∗ |l −len |2 (4) Finally,weseethatGPT-3.5hasrelativelypoor
i i
n
i=0 length controllability, corroborating the observations of Sun et al. (2023) regarding the managen is the number of datapoints and l and len are
i i
mentofoutputlengthinLLMsthroughprompting.
thegeneratedanddesiredlength,respectively.
Citation length prediction is hard. We find
6 Conclusion
thatallofourlengthregressionmodelsstruggleto
accurately predict citation length. Table 2 shows We have explored different approaches for prethatallthreeapproacheshaveMAEof13tokens dicting the lengths of citations and using length
ormore,whichissignificant,consideringtheaver- to control generation. Our experimental results
age length of citations in the dataset is only 34.5 demonstratethatusingthegroundtruthlengthcan
tokens. We do find that the Vanilla and Sched- significantlyimprovethequalityofthegenerated
uledSamplingstrategies,whichareupdatedwith citations, but predicting the length of a citation
the generation loss, perform better than Teacher based solely on the cited paper abstract and tar-
Forcing,butoveralltheirperformanceispoorand getcitationcontextischallenging. Toaddressthis
causesthedownstreamgenerationtasktoperform issue, we propose the use of heuristic estimates
worse than Baseline. Further, we see that, while of desired length, finding that citation length is
the Oracle approach exhibits a high level of con- mostlyrelatedtoeachauthor’sindividualwriting
trollability, our multitask strategies do not. This style, which explains why it is so difficult to pregapmayarisefromourpredictedlengthbeingso dict. Ourworkhighlightsanimportantchallenge
noisy: thedownstreamlengthcontrolmodellearns incitationtextgenerationandsuggestsastraighttoignorethisunreliablelengthsignal. forwardsolution. Byusingauthor-specificcitation
Tofurtherinvestigatetheimpactofinputlength lengthestimates, wecaneliminatethelengthdiferrors, we conduct an experiment where we take ference between the generated and ground truth
the same target citation and generate it at differ- citations,significantlyimprovingthequalityofthe
ent lengths: 20, 30, or 50 tokens. We find that generatedcitations. Wehavemadeourcodeavail-

<!-- Page 5 -->

able at https://github.com/mandalbiswadip/ ceedingsofthe2016ConferenceonEmpiricalMeth-
LengthControlledGeneration ods in Natural Language Processing, pages 1328–
1338,Austin,Texas.AssociationforComputational
Linguistics.

### References

YutaKikuchi,GrahamNeubig,RyoheiSasano,Hiroya

### Takamura,andManabuOkumura.2016b. Control-

Iz Beltagy, Matthew E. Peters, and Arman Cohan.
lingoutputlengthinneuralencoder-decoders. InPro-

## Longformer: Thelong-documenttransformer.

ceedingsofthe2016ConferenceonEmpiricalMetharXiv:2004.05150.
ods in Natural Language Processing, pages 1328–
1338.

### SamyBengio,OriolVinyals,NavdeepJaitly,andNoam

Shazeer. 2015. Scheduled sampling for sequence

### SurafelMelakuLakew,MattiaDiGangi,andMarcello

predictionwithrecurrentneuralnetworks. Advances
Federico. 2019. Controlling the output length of
inneuralinformationprocessingsystems,28.
neural machine translation. In Proceedings of the
16thInternationalConferenceonSpokenLanguage
JingqiangChenandHaiZhuge.2019. Automaticgener-
Translation.
ationofrelatedworkthroughsummarizingcitations.

### ConcurrencyandComputation: PracticeandExperi-

Xiangci Li, Biswadip Mandal, and Jessica Ouyang.
ence,31(3):e4261.

## CORWA: A citation-oriented related work

annotationdataset. InProceedingsofthe2022Con-
XiuyingChen,HindAlamro,MingzheLi,ShenGao,Xiference of the North American Chapter of the AsangliangZhang,DongyanZhao,andRuiYan.2021.
sociation for Computational Linguistics: Human
Capturing relations between scientific papers: An

### LanguageTechnologies,pages5426–5440,Seattle,

abstractivemodelforrelatedworksectiongeneration.
United States. Association for Computational Lin-
In Proceedings of the 59th Annual Meeting of the
guistics.
Association for Computational Linguistics and the
11thInternationalJointConferenceonNaturalLan-
Yizhu Liu, Zhiyi Luo, and Kenny Zhu. 2018. ConguageProcessing(Volume1: LongPapers),pages
trollinglengthinabstractivesummarizationusinga
6068–6077,Online.AssociationforComputational convolutionalneuralnetwork. InProceedingsofthe
Linguistics. 2018ConferenceonEmpiricalMethodsinNatural
Language Processing, pages 4110–4119, Brussels,
AngelaFan,DavidGrangier,andMichaelAuli.2017.
Belgium.AssociationforComputationalLinguistics.

### Controllable abstractive summarization. arXiv

preprintarXiv:1711.05217. Kelvin Luu, Xinyi Wu, Rik Koncel-Kedziorski, Kyle

### Lo,IsabelCachola,andNoahA.Smith.2021. Ex-

AngelaFan,DavidGrangier,andMichaelAuli.2018.
plainingrelationshipsbetweenscientificdocuments.
Controllableabstractivesummarization. InProceed-
In Proceedings of the 59th Annual Meeting of the
ingsofthe2ndWorkshoponNeuralMachineTrans-
Association for Computational Linguistics and the
lationandGeneration,pages45–54.
11thInternationalJointConferenceonNaturalLanguageProcessing(Volume1: LongPapers),pages

### YubinGe,LyDinh,XiaofengLiu,JinsongSu,Ziyao

2130–2144,Online.AssociationforComputational
Lu, Ante Wang, and Jana Diesner. 2021. BACO:
Linguistics.
Abackgroundknowledge-andcontent-basedframeworkforcitingsentencegeneration. InProceedings YuiOka,KatsukiChousa,KatsuhitoSudoh,andSatoshi
of the 59th Annual Meeting of the Association for Nakamura. 2020. Incorporating noisy length con-
ComputationalLinguisticsandthe11thInternational straintsintotransformerwithlength-awarepositional
JointConferenceonNaturalLanguageProcessing encodings. InProceedingsofthe28thInternational
(Volume1: LongPapers),pages1466–1478,Online. Conference on Computational Linguistics, pages
AssociationforComputationalLinguistics. 3580–3585.
CongDuyVuHoangandMin-YenKan.2010. Towards JiaoSun,YufeiTian,WangchunshuZhou,NanXu,Qian
automated related work summarization. In Coling Hu,RahulGupta,JohnFrederickWieting,Nanyun
2010: Posters,pages427–435. Peng,andXuezheMa.2023. Evaluatinglargelanguagemodelsoncontrolledgenerationtasks. arXiv
Yue Hu and Xiaojun Wan. 2014. Automatic generpreprintarXiv:2310.14542.
ation of related work sections in scientific papers:
An optimization approach. In Proceedings of the ShoTakaseandNaoakiOkazaki.2019. Positionalen-
2014ConferenceonEmpiricalMethodsinNatural coding to control output sequence length. arXiv
LanguageProcessing(EMNLP),pages1624–1633, preprintarXiv:1904.07418.
Doha,Qatar.AssociationforComputationalLinguistics. XinyuXing,XiaoshengFan,andXiaojunWan.2020.

### Automatic generation of citation texts in scholarly

YutaKikuchi,GrahamNeubig,RyoheiSasano,Hiroya papers: A pilot study. In Proceedings of the 58th
Takamura,andManabuOkumura.2016a. Control- AnnualMeetingoftheAssociationforComputational
lingoutputlengthinneuralencoder-decoders. InPro- Linguistics,pages6181–6190.

<!-- Page 6 -->


### ZijianYang,YingboGao,WeiyueWang,andHermann

Ney.2020. Predictingandusingtargetlengthinneural machine translation. In Proceedings of the 1st

### ConferenceoftheAsia-PacificChapteroftheAsso-

We have written an incomplete related work section.
ciationforComputationalLinguisticsandthe10th
We want a set of cited papers to be summarized in

### InternationalJointConferenceonNaturalLanguage

the context of the imcomplete related work section.

### Processing,pages389–395,Suzhou,China.Associa-


### Given the incomplete related work section and a list

tionforComputationalLinguistics. ofcitedpapers,completeitbysummarizingthecited
papersintherelatedworksectioncontextin<Length>

### A Appendix

words.Thepositionwherethesummarizedtextgoesis
indicatedbythespecialtoken‘[Dominant]’.
A.1 Length-DifferencePositionalEncoding

## (Ldpe)


### Thecitedpapercanbeoneoftwotypes,referredtoas

TakaseandOkazaki(2019)definetheLDPEfora CitationType:
Dominant:Thesecitationsarediscussedindetail,usu-

### Transformer-basedencoder-decoderasfollows:

allyviasummarizationoftheircontent,andareoften
(len−pos) longerthanreferencecitations.
LDPE(pos,len,2i) = sin( ) Reference: Thesecitationsarenotdiscussedindetail.
2i
10000d Reference citations tend to be more abstract than
(len−pos) dominantcitations.
LDPE(pos,len,2i+1) = cos( )
2i
10000d
(5) Output format: Summarize the cited papers given
theirCitationMark,CitationType,Title,andAbstract.
len refers to the desired length of the generation,

### Returnonlythepieceoftextrequiredtocompletethe

measuredinthenumberoftokens. relatedworksection. Returnitinstringformat. The
numberofwordsintheoutputshouldbethesameas
A.2 MoreCitationLengthExamples <Length>.

### Figure 5 shows an example of a citation that is

IncompleteRelatedworksection:<Example1incomvagueandtoogenericwhengeneratedatashorter
pleterelatedworksection>
length. Figure6showstwoexamplesofcitations Listofcitedpapers:
generatedatshorterorlongerlengths,resultingin 1.
Citation mark: <Example 1 first cited paper citation
lowerfluency.
mark>

### Citation Type: <Example 1 first cited paper citation

len=20:Pengetal.(2018)improvethestate-of-the-art. type>

### Title:<Example1firstcitedpapertitle>

len=30: Peng et al. (2018) propose a joint model Abstract:<Example1firstcitedpaperabstract>
forframe-semanticparsingandsemanticdependency 2.
parsingbytreatingannotationsasvariables. ...
Numberofoutputwords:<Example1Length>

### Output:“‘<Example1output>”’

Figure5: Exampleofanoverly-short,genericcitation. Explanation: The generated output has <Example 1

### Length>words,whichstartswiththeword<Example1

outputstartingword>andendswiththeword<Example
1outputendingword>
Tooshort:Alkhoulietal.(2018)proposedtouseanadditionalalignmentheadtoimproveNMTperformance,
buttheirscalability. IncompleteRelatedworksection: <Inputincomplete
relatedworksection>
Toolong: Firatetal. (2016b)proposedadistillation- Listofcitedpapers:
based distillation approach, in which the distillation 1.
processistrainedonasmallsetoflabeleddata. Citationmark:<Inputfirstcitedpapercitationmark>
CitationType:<Inputfirstcitedpapercitationtype>

### Title:<Inputfirstcitedpapertitle>

Figure 6: Examples of shorter and longer generated Abstract:<Inputfirstcitedpaperabstract>
2.
citations(comparedtothegroundtruthtargetlength)
...
resultinginpoorfluency.
Numberofoutputwords:<Length>

### Output:


### A.3 GPT-3.5TurboPrompt


### Figure7: One-shotpromptusedforlength-controlled

Figure7showsthepromptweusedforourGPT-3.5 citationgenerationusingGPT-3.5Turbo.

### Turbolengthcontrolbaseline. Thepromptconsists

of the citation context and a list of papers to cite,
aswellasthegroundtruthtargetcitationlength.