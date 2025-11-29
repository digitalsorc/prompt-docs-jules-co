---
title: "LLM Prompt Chaining Legal Documents"
original_file: "./28_LLM_Prompt_Chaining_Legal_Documents.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["prompt-engineering", "llm", "rag", "chain-of-thought", "fine-tuning"]
keywords: ["shot", "page", "gpt", "arxiv", "neox", "model", "label", "our", "flan", "randomclass"]
summary: "<!-- Page 1 -->

Large Language Model Prompt Chaining for
Long Legal Document Classification

### DietrichTrautmann

ThomsonReutersLabs,Zug,CantonofZug,Switzerland

### Abstract

Promptingisusedtoguideorsteeralanguagemodelingeneratinganappropriateresponsethatisconsistentwiththe
desiredoutcome.Chainingisastrategyusedtodecomposecomplextasksintosmaller,manageablecomponents.Inthis
study,weutilizepromptchainingforextensivelegaldocumentclassificationtasks,whichpresentdifficultiesduetotheir
intricatedo"
related_documents: []
---

# LLM Prompt Chaining Legal Documents

<!-- Page 1 -->

Large Language Model Prompt Chaining for
Long Legal Document Classification

### DietrichTrautmann

ThomsonReutersLabs,Zug,CantonofZug,Switzerland

### Abstract

Promptingisusedtoguideorsteeralanguagemodelingeneratinganappropriateresponsethatisconsistentwiththe
desiredoutcome.Chainingisastrategyusedtodecomposecomplextasksintosmaller,manageablecomponents.Inthis
study,weutilizepromptchainingforextensivelegaldocumentclassificationtasks,whichpresentdifficultiesduetotheir
intricatedomain-specificlanguageandconsiderablelength.Ourapproachbeginswiththecreationofaconcisesummaryof
theoriginaldocument,followedbyasemanticsearchforrelatedexemplartextsandtheircorrespondingannotationsfroma
trainingcorpus.Finally,wepromptforalabel-basedonthetask-toassign,byleveragingthein-contextlearningfromthe
few-shotprompt.Wedemonstratethatthroughpromptchaining,wecannotonlyenhancetheperformanceoverzero-shot,
butalsosurpassthemicro-F1scoreachievedbylargermodels,suchasChatGPTzero-shot,usingsmallermodels.

### Keywords

PromptChaining,PromptEngineering,LongLegalDocuments,LegalNLP,LegalAI

## Introduction


### What is the

topic of this
Thelegaldomain,withitsoftenchallengingtasksand document?
complexlongdocuments,isanimportantfieldofstudy
fornaturallanguageprocessing(NLP)andmachinelearn-

### Legal ? Label

ing[1,2].Longlegaldocumenttextclassificationtasks Document
canbechallengingduetoseveralfactors,includinglarge
size,complexlanguageandspecificvocabulary,highly
specialized content structure, imbalanced data (many

### Summary Label

commoncasesvs. along-tailofpeculiarones),subjec- Generation Generation
tivity(opentointerpretationanddebate),andtheneed
forexpensive,manualannotationsfromsubjectmatter Corpus

## Db

experts. N-Shot
Summary

### Prompt


### Therecentsurgeintheutilizationoflegalbenchmarks

has stimulated a proliferation of innovative solutions Semantic
harnessing pre-trained language models [3]. Conven- Similarity

### Search

tionally, thesemethodologiesnecessitateanintensive
annotationprocess(thoughsomeutilizemetadataannotations),followedbyacostlyfine-tuningprocessforthe
models[3,4].
The advent of large-scale pre-training of large lan-
Figure1:PromptChainingforLegalDocumentClassification
guagemodels(LLMs)haspresentedanopportunityto

### Thetechniqueofpromptchaining[6,7]hasshown

leveragethemdirectlythroughnaturallanguagepromptpromiseinNLP,sequentiallylinkingmultipleprompts
ing [5], circumventing the need for additional tasktoguidethegenerationprocess(Fig.1).Throughtheutidependentfine-tuning. Promptinginvolvesproviding
lizationofconsecutiveprompts,thesystemcanproduce
aspecificinstruction,query,orquestiontoanLLMto
morecontextuallyrelevantresponsesforeachstepand
generate a specific output or response. The input, or
morecomplexresponsesfortheoveralltask.
prompt,steersthesystemtowardsproducingaresponse
Promptchainingprovesparticularlyadvantageousin
meaningfullyrelatedtoit.
longlegaldocumentclassification,improvingtaskperformance,efficiency,flexibility,andconsistencyviathe
SwissText’23:The8theditionoftheSwissTextAnalyticsConference– inspectionofindividualstepsinthechain[8].Thetech-

### GenerativeAI&LLM,June12–14,2023,Neuchâtel,Switzerland

$Dietrich.Trautmann@tr.com(D.Trautmann) niqueenhancestheinterpretabilityoftheoverallclas-
(cid:26)0000-0003-0858-6977(D.Trautmann) sificationandpermitsdebuggingofcomplexreasoning
©2023Copyrightforthispaperbyitsauthors.UsepermittedunderCreativeCommonsLicense tasksuponfailure[9].
Attribution4.0International(CCBY4.0).
CWPr Eoo UrckR esehdoinpgshISttSpN:// c1e6u1r3-w-0s0.o7r3g CEURWorkshopProceedings(CEUR-WS.org)
3202
guA
8
]LC.sc[
1v83140.8032:viXra

<!-- Page 2 -->

Overall,promptchainingisavaluabletoolintheclas- tasksanddomains. Thetwomostsubstantialprojects
sificationoflonglegaldocuments,helpingtoimprove includeOpenPrompt[15]andPromptSource[16].
theperformanceandefficiencyoftheclassificationprocess.Promptchainingallowslanguagemodelstobuild OpenPrompt providesauser-friendlyandresearchontheirpreviousoutputsandprovidemorenuancedclas- friendlytoolkitforprompt-learninginpre-trainedlansificationresults,anditcanbecustomizedtomeetthe guagemodels(PLMs).Theadventofprompt-learningin
specificneedsofthelegaldocumentclassificationtask. naturallanguageprocessingsparkedaneedforastan-
Ourcontributionsinthisworkare: dardizedimplementationframework.OpenPromptcaters
to this need by delivering a modular and extendable
• Weshowthatwecansuccessfullychainprompts
toolkitthataccommodatesvariousPLMs,taskformats,
forlegaldocumentclassificationtasks(visualized
andpromptingmodulesinaunifiedparadigm.
inFig.1).
• Weapplypromptchainingononebinaryclassificationtaskandononemulti-classtextclassifica- PromptSource isatoolkitdesignedtofacilitatethedevelopmentandsharingofnaturallanguagepromptsfor
tiontask.
trainingandqueryinglanguagemodelsinNLP.Itoffersa
• Weimprovetheresultsoverzero-shotprompting
templatinglanguageforcreatingdata-linkedprompts,a
withourchainingapproach.
swiftiterativedevelopmentinterface,andacommunity-
• Ourpromptchainingapproachevenoutperforms
drivensetofguidelinesforcontributingnewprompts.
zero-shotChatGPTpromptingonthemicro-f1
Currently,theplatformoffersover2,000promptsforapscore.
proximately170datasets,promotingcollaborationand
efficientutilizationofpromptsforlanguagemodeltrain-

## Related Work ingandquerying.

Intermsofrelatedliteraturewefocusonthelegaldocu- PromptChaining asaconceptwasexploredin[8],
mentclassificationworkandoncurrentpromptingap- where prompts were chained using a visual program
proaches,aswellasthecombinationofthetwofields. editor.Now,thereareframeworkswithpromptchaining
attheircore,suchasLangChain[17],LLamaIndex[18],
andMiniChain[19].

### LegalDocumentClassification

Documents,withtheircharacteristiclongtextualdata,

### LegalPrompting

oftenposesignificantchallengesforautomatedmachine
learningmethodsinprocessingandclassificationtasks Recentresearchhascombinedpromptingandnatural
[10],[11]. Thesechallengesbecomemorepronounced languagetasksinthelegaldomain.In[20],authorsevalinthelegaldomainduetoadditionalcomplexitiessuch uatedzero-shotpromptingonthelegaljudgmentpreasintricategrammar,nestedsentences,domain-specific dictiontaskusingmultilingualdatafromtheEuropean
vocabulary,andextensiveuseofabbreviations[12]. CourtforHumanRights(ECHR)andtheFederalSupreme
The LexGLEU benchmark [3] represents a compre- CourtofSwitzerland(FSCS).Meanwhile,[21]appraised
hensiveconsolidationofrecentdatasetsinvolvinglong GPT-3’szero-andfew-shotcapabilitiesforlegalreasonlegaldocuments,exclusivelyintheEnglishlanguage.It ingtasksontheCOLLIEentailmenttask(usingEnglish
includes legal documents related to EU & US Law, as translationsoftheJapanesebarexam).
wellascontractswithtaskspertainingtomulti-labeland TheGPT-3.5modelwasevaluatedontheUSBarExam
multi-classclassificationandmultiplechoicequestion- [22], and GPT-4[23]has demonstratedproficiency in
answering.In[13],theauthorsevaluatedahierarchical passingmultipleteststhroughzero-shotprompting.
approachformodelinglongdocuments,and[14]investigatedstrategiestoaugmentthecontext-windowoftrans-

## Data

formersfordomain-specifictasks,includingtheaforementionedLexGLEU benchmark.Whilebenchmarksin

### Thedatasetsutilizedinourstudyaresourcedfromtwo

otherlanguagesdoexist,suchasMultiEURLEX [4],our
widelyrecognizedbenchmarkscomprisinglengthydocworkwillalsofocussolelyontheEnglishlanguage.
uments in the legal domain: the European Court of

### HumanRights(ECHR)andtheSupremeCourtofthe


### Prompting UnitedStates(SCOTUS).Thesedatasetsformpartofthe

Severalnoteworthyprojectsaimtoconsolidate,evaluate,
LexGLUEbenchmark[3].
and standardize prompting approaches across diverse

<!-- Page 3 -->


### ECHR objectives(diversespancorruptionandprefixlanguage

modelingtasks).Thismodelwasfurtherinstructionfine-

### The ECHR dataset comprises approximately 11,000

tunedusingtheFlanpromptingcollection[27].ThecolcasessourcedfromtheEuropeanCourtofHumanRights
lectioncontainsinstructionsforadiversesetoftasks
publicdatabase.Thisdatasetissplitintotraining,devel-
(e.g.,tosummarizeatext;toclassifybasedonalistof
opment,andtestsets. Eachcaseincludesfactualparaoptions).Themodelispubliclyavailablewithanopen
graphs,alongwiththecorrespondingECHRarticlesthat
sourcelicense(Apache2.0).
wereviolatedorallegedtobeviolated.Theoriginaltask
involvestopredicttheviolatedhumanrightsarticlesfor
acase’sfacts.However,forthepurposeofourstudy,we 4.2. SummarizationModels
havesimplifiedthistasktoabinaryclassificationprob-
Wealsousedtask-specificsummarizationmodelsforthe
lem.Wedistinguishcasesbasedonwhethertherewas
creationofthelegalsummaries.Inourexperimentswe
aviolationofanyhumanrightsarticles,irrespectiveof
foundthat–duetothelackofground-truthsummaries
whichspecificarticleswereviolated.
forourlonglegaldocuments–thetask-specificsummarizationmodelscreatedmorecoherentsummariescom-

### SCOTUS paredtoresultsfrompromptingthegeneralgeneration

models.

### TheSCOTUSdatasetprovidesinsightintothehighest

federalcourtintheUSA,whichhandlescomplexorcontroversialcasesunresolvedbylowercourts.Thisdataset 4.2.1. BRIO
combinesinformationfromSCOTUSopinionsandthe TheBRIO4model[28]isanabstractivesummarization
SupremeCourtDataBase(SCDB).TheSCDBoffersmeta- modelthatachievesstate-of-the-artresultontheCNN/-
data for all cases spanning from 1946 to 2020. Utiliz- DailyMailandXSumdatasets. ItusesBART[29]asits
ingtheSCDB,thedatasetclassifiescourtopinionsinto basemodelandhasacontextwindowof1024tokens.
14issueareas(refertoApp. B).Thedatasetisdivided
chronologicallyintotraining(#5000samples,1946–1982),

## Primera

development(#1400samples,1982–1991),andtest(#1400
samples,1991–2016)sets,eachcoveringadistincttime ThePRIMERA5model[30]isanabstractivesummarizaperiod. tionmodelthatwastrainedontheMulti-LexSumdataset
atdifferentgranularities. Weusedthemodelthatwas
trainedonthegranularityfromthefullsourcedocument

## Models

tocreateashortsummaryandithasacontextwindow
of1024tokens.Theotheroptionsare–besidesdifferent
Our experimental design incorporates both generalmodelarchitectures–longandtinysummaries.
purposetextgenerationmodelsandtask-specificsummarizationmodels.

### SemanticSimilaritySearch


### GenerationModels We use semantic similarity search for the few-shot

promptbuildingwereweretrievesemanticsimilarsum-

### Weusedtwodifferent20billionparameterLLMsinour

mariesfromthetrainingsettoatargetsummary(either
textgenerationsteps.Bothofthemodelshaveacontext
fromthedevelopmentortestset).Forthispurpose,our
windowofupto2048tokens.
summarieswereencodedusingthesentence-transformers
library[31]andthecustom-legalbert6 model[32]. Fur-

#### GPT-NeoX thermore,weusedtheannoy7libraryfortheapproximate

TheGPT-NeoX model[24]isanautoregressivelanguage nearestneighborsearch(semanticsimilaritysearch).
model, specifically a decoder-only model1, trained on
thePiledataset[25]. Thismodels’weightsareopenly

## Prompt Chaining

availableunderapermissivelicense(Apache2.02).

### PromptChainingisamethodologyemployedtodecom-


#### Flan-UL2 posecomplextasksintosmaller,manageablesub-tasks.A

promptchaintypicallycomprisesseveralprompts-either

### Flan-UL2[26]isanencoder-decodermodel3basedonthe

T5architecture,trainedwiththemixture-of-denoisers
4https://hf.co/Yale-LILY/brio-cnndm-uncased
1https://hf.co/EleutherAI/gpt-neox-20b 5https://hf.co/allenai/primera-multi_lexsum-source-short
2https://www.apache.org/licenses/LICENSE-2.0.html 6https://hf.co/zlucia/custom-legalbert
3https://hf.co/google/flan-ul2 7https://github.com/spotify/annoy

<!-- Page 4 -->

task-specificorgeneral-purpose,eachservingasingle we embedded all our summaries with the models dispurpose.Theoutputofonepromptfeedsintothenextas cussedinsection4.3andcalculatedthesemanticallyclosaninput.Inourapproach,weutilizepre-definedsteps; estneighbors(uptoeight)ofeachsummaryinthedehowever,it’sworthnotingthatthismethodologycould velopmentandtestsets,ascomparedtothetrainingset.
befurtheroptimizedbyincorporatingaselectionpro- Thesesummariesfromthetrainingset,alongwiththeir
cessforthenextsteporbyintroducingstoppingcriteria truelabelsandthecurrenttargetsample(excludingits
intheoutputgeneration,asexemplifiedin[9]and[33]. truelabelfromthedevelopmentandtestsets),served
Thestepsforourpromptchainingprocess,specifically asthefew-shotprompts. Thisapproachleveragesthe
utilizedfortheclassificationoflonglegaldocuments,are in-contextlearningabilitiesoflargelanguagemodels.
depictedinFig.1.Inthefollowingsections,wewilldelve Asillustratedby[34],analternativeapproachcould
intoeachoftheprimarysteps,namelysummarization, involvepromptingalargelanguagemodeltogenerate
few-shotpromptbuilding,andfinallabelgeneration. contextualtextsbasedonaninput,insteadofretrieving
fromacorpusdatabaseaswehavedone.Thesegenerated
samplescouldthenbeincorporatedasin-contextsam-

### SummaryGeneration

plesinthefollowingstep.Thisoptioncanalsobepoten-
Theinauguralstepinourpromptchainingapproachis tiallyimplementedviaLLMspromptinginourprompting
thegenerationofasuccinctsummaryofthelegalcase pipeline.Theevaluationofthisapproach’sfeasibilityis
text.Asamajorityoflegaldocumentsarelengthy,often leftforfuturework.
exceedingthelargecontextwindowof2048tokensprovidedbycontemporarylanguagemodels,weadvocate

### LabelGeneration

thecreationofsummariesforchunksofthewholedocument.Thesechunksarecraftedbasedonthemodel’s Thefinalstepinourpromptchaininvolveslabelgencontextwindow.Sentencesaresequentiallystackedun- eration. Here,wequeriedtheLLMswiththefew-shot
tilthecontextlimitoftherespectivemodelsisreached promptspreviouslyconstructed,inconjunctionwithan
(1024or2048tokens).Posttheinitialparsingofthefull instructionforthecorrespondingtaskandalistofpotendocument,thesummarygenerationprocessforchunksis tiallabelstochoosefrom.FortheECHRexperiments,the
iterativelycontinueduntilthedesiredsummarylength,in binaryoptionsprovidedwereYESorNO,whileforthe
ourcaseupto128tokens,isachieved.Thesesummaries SCOTUSexperiments,upto13issuearealabelswerepretypicallyconsistofafewsentences(upto5)derivedfrom sentedformodelprediction.Thispromptconstruction
ourdata. enabledthemodelstoyieldthedesiredlabelinallourex-
Initial experimentation with direct prompting ap- periments.Greedydecodingwasusedinthisgeneration
proachesonlargelanguagemodelsresultedinvariable stepforallresults.
outcomes.Thetemplatesusedforpromptingincluded: Anotherstrategyemployedinvolvedsamplingfrom
themodeloutputmultipletimes,atechniqueknownas
• INPUTTEXTInsummary,
self-consistencyviaoutputsampling[35]. Ithasbeen

## • Inputtexttldr:

demonstratedthatqueryingmultipletimesenhancesthe
probabilityofgeneratingthetruelabel.Attheconclusion

### Sincewedonotpossessground-truthsummariesfor

ofeachsuchsampling(upto10times),themajoritycount
the documents, our assessments relied on manual inofthegeneratedlabelswastakenasthefinalprediction.
spectionofasubsetofthesummariesgenerated(from
thetrainingset).Theinspectionindicatedthatthesummarieswererelativelygenericandoftenomittedthecore 6. Experiments
legalissuesofinterest.
Consequently,ourinvestigationsteeredtowardstask- Our experiments pursued two objectives. Firstly, we
specificsummarizationmodels.Notably,theBRIOmodel, aimed to enhance the zero-shot outcomes from prior
beingpre-trainedandfine-tunedonnewsarticles,gener- work on the binary classification task on the ECHR
atedmoregenericsummaries.Incontrast,thePRIMERA dataset,leveragingpromptingtechniqueswithoutany
model,fine-tunedspecificallyonlegaldocuments,gener- parameteradjustmentstothemodels.Followingthesucatedsummarieswherethecorelegalcontextwasmostly cessfuldemonstrationoftheefficacyofthefew-shotappreserved.Thisiterativesummarizationwasuniformly proach,weexpandedourfocus.Thesecondexperiment
appliedacrossalldocumentsusingthesameparameters. involvedextendingtheprocesstothe13labelsinthe

### SCOTUScorpus,atasksignificantlymorechallenging


### SemanticSimilaritySearch thanthepriorbinaryclassification.


### Inadditiontothis,wecomparedourresultstothezero-

The objective at this stage was to construct few-shot shotChatGPTresultsreportedin[36],whichcovereda
promptsforthesubsequentlabelgenerationstep.Thus,

<!-- Page 5 -->


### Yes No

Predicted Labels
slebaL
lautcA
seY
oN
# Label #Samples F1
1 Yes 825 0.864
732 93
2 No 175 0.248

### Table1 137 38

LabelwiseF1-ScoresforthedevelopmentsetofECHR.
Figure2:Confusionmatrixforthedev.setofECHR.
subsetoftheoverallsamplesintheSCOTUSdata. We
selected the corresponding samples and provided our
resultsforcomparison.
Overmultipleiterations,wedevelopedthefew-shot
promptsonarandomlyselectedportion(n=40)ofthe
developmentsetsforboththeECHR andtheSCOTUS
datasets.Thefinaleight-shotpromptincorporatedthe
eightsemanticallyclosestsummariesfromthetraining
settothecorrespondingtargetset,aswellastherespective gold label from the training set. Notably for the
SCOTUScorpus,welimitedtheavailableissuearealabelsforthemodel,basedonthelabelsoftheincluded
eightsamples.Onceweidentifiedthemosteffectivecompositionofthefew-shotpromptontherandomsample,
weappliedittothefulldevelopmentandtestsets,and
reportedtheresults.

### OurcomputationalrequirementswerelimitedtoCPU

resources,asweonlyperformedinferencecallsonthe
generativemodels.Ourworkdidnotinvolvetheuseof
anyGPUs.Detailedcomputationalinformationisavailableintheappendix(seeApp.A).

## Results

In this section, we discuss our results on both benchmarks.Wehaveincludedtheconfusionmatricesforthe
developmentsets(seeFig. 2forECHRandFig. 3for
SCOTUS),thelabelwiseF1-scores(seeTab.1andTab.4),
andtheoverallresults(seeTab.2andTab.3).

### ECHRResults

WithrespecttotheECHRresults,wemanagedtoimprove upon the zero-shot results from previous work.
However, the few-shot context still did not suffice to
reachtheperformanceofsupervisedtrainedmodels.It’s
importanttorememberthatfullsupervisedfine-tuning
involveshoursofupdaterunswiththousandsofannotatedsamples,whileourexperimentsonlyincludedinferencecalls.Theconfusionmatrix(Fig.2)alsodemonstratessomemisclassificationalongtheoff-diagonalaxis,
althoughthefew-shotpromptingdidcapturemoreofthe
minority(NO)class.
erudecorp
lanimirc
ytivitca
cimonoce
sthgir
livic
rewop
laiciduj
tnemdnema
tsrif
msilaredef ssecorp
eud
snoinu noitaxat
laredef
syenrotta ycavirp snoitaler
etatsretni
suoenallecsim
criminal procedure
economic activity
civil rights
judicial power
first amendment
federalism
due process
unions
federal taxation
attorneys
privacy
interstate relations
miscellaneous
Predicted Labels
slebaL
lautcA
235 8 43 23 8 0 39 2 0 0 2 0 0
3 12817 39 13 3 7 5 10 1 0 0 0
9 9 14918 13 3 8 3 2 3 0 1 0
10 29 40 50 21 0 3 5 4 1 0 0 2
3 3 10 2 85 0 3 0 0 1 1 0 0
0 24 17 10 2 18 2 6 4 0 0 0 0
11 7 19 10 2 4 13 2 1 0 0 0 1
0 2 5 10 2 0 0 31 0 0 0 0 0
0 2 0 0 1 1 1 0 33 0 0 0 0
0 3 19 0 3 0 3 0 0 6 0 0 1
1 0 2 3 6 0 0 0 1 0 9 0 0
0 3 1 0 0 5 0 0 0 0 0 5 0
1 0 1 4 0 0 1 0 2 0 0 0 1
Figure3:Confusionmatrixforthedev.setofSCOTUS.

### SCOTUSResults

Theresultsforthemulti-classtextclassificationtaskfor

### SCOTUSarepresentedinTab.2.Alongsideourresultson

thedevelopmentandtestsets,wealsoincludedexternal
(ext.)resultsfrom[3]and[36].

### Whileweachievedsatisfactoryperformanceonthe

developmentset,weobservedasubstantialdropinperformanceonthetestset. Thetestsetperformancein
termsofmacro-f1scorewasbelowthezero-shotChat-

### GPTresults. However,ourpromptchainingapproach

wasmoreeffectiveinretrievingthehigherfrequency
classes,asreflectedinthebettermicro-f1score.
Thistrendisalsoevidentinthelabel-wisescores(Tab.
4),wherethehigherfrequencyclassesreceivedbetter
scoresthantheminorityclasses.Theconfusionmatrix
(Fig.3)forthisexperimentshowedthatparticularlymany
issueareaswerepredictedascivilrights,whilealsothe
criminalprocedure,judicialpower andfederalismwere
misclassifiedasothers.

## Conclusion

Ourexperimentssuccessfullydemonstratedthattheimplementationoffew-shotpromptscanleadtoimprove-

<!-- Page 6 -->

Model Precision Recall macro-F1 micro-F1 weighted-F1 Accuracy
tes.ved
minorityclass .088 .500 .149 .175 .052 .175
randomclass .506 .510 .451 .514 .572 .514
majorityclass .412 .500 .452 .825 .746 .825
GPT-NeoX(0-shot,(F)) .527 .536 .526 .709 .731 .709
GPT-NeoX(8-shot,(S)) .566 .552 .556 .770 .756 .770
testset
minorityclass .077 .500 .133 .153 .041 .153
randomclass .479 .460 .410 .484 .555 .484
majorityclass .423 .500 .459 .847 .777 .847
GPT-NeoX(0-shot,(F)) .522 .530 .521 .707 .728 .707
GPT-NeoX(8-shot,(S)) .525 .537 .527 .779 .768 .779

### Table2

TheresultsfortheECtHRdevelopmentandtestsets.Besidesthemacro-averagedF1-score,precisionandrecall,wereportalso
themicro-averagedandweighted-F1andtheaccuracyscores.The(F)standsforthefulldocumentthatwasusedintheinput
tothemodel,whilethe(S)standsforthesummaries(concatenatedinthefew-shotprompts)astheinputtothemodel.
Model Precision Recall macro-F1 micro-F1 weighted-F1 Accuracy
tes.ved
majorityclass .020 .077 .031 .257 .105 .257
randomclass .070 .064 .057 .071 .084 .071
FLAN-UL2(8-shot,(S)) .529 .455 .461 .545 .543 .545
testset
majorityclass .020 .077 .032 .266 .112 .266
randomclass .079 .074 .060 .077 .095 .077

### FLAN-UL2(8-shot,(S)) .427 .373 .359 .486 .483 .486

FLAN-UL2(8-shot,(S))† .435 .388 .371 .484 .480 .484
.txe
ChatGPT(0-shot,(F)) - - .420 .438 - -
supervised(full) - - .695 .782 - -

### Table3

TheresultsfortheSCOTUSdevelopmentandtestsets.Besidesthemacro-averagedF1-score,precisionandrecall,wereport
alsothemicro-averagedandweighted-F1andtheaccuracyscores.The(F)standsforthefulldocumentthatwasusedinthe
inputtothemodel,whilethe(S)standsforthesummaries(concatenatedinthefew-shotprompts)astheinputtothemodel.
†Wecalculatedthescoresbasedonthesamereducedsetofdocuments(1k)astheChatGPTwork.Theext.rowsareexternal
resultscopiedfromthecorrespondingpapers[3,36].
# Label #Samples F1 mentsuponthezero-shotresults.Wealsoshowedthatit
1 CriminalProcedure 360 0.742 isfeasibletopredictfrequentlabelswithappreciableF1
2 FederalTaxation 226 0.695 scoresusingthisapproach.
3 FirstAmendment 218 0.644 Thestrategyofprompting, andaswehavedemon-
4 Unions 165 0.590
strated, the concept of prompt chaining, represent
5 EconomicActivity 108 0.577
promisingavenuesforfutureexploration. Thesetech-
6 CivilRights 83 0.551
niquesareparticularlyadvantageousastheycircumvent
7 Privacy 70 0.529
theneedforcostlydataannotationandthedevelopment
8 InterstateRelations 51 0.500
9 Federalism 38 0.308 ofcustommodels.
10 JudicialPower 35 0.299 Lastbutnotleast,establishedpromptingpipelinescan
11 Attorneys 22 0.255 beadaptedforusewithdifferent(updated)modelsand,as
12 DueProcess 14 0.173 shownin[23],theyofferacross-the-boardenhancements
13 Miscellaneous 10 0.133 foradiverserangeoftasks,freeofcost.Lookingahead,
our future work aims to experiment with even larger
Table4 modelsonadditionallegalbenchmarks.
LabelwiseF1-ScoresforthedevelopmentsetofSCOTUS.

<!-- Page 7 -->

References [12] A.Garimella,A.Sancheti,V.Aggarwal,A.Ganesh,

### N.Chhaya,N.Kambhatla, Textsimplificationfor

[1] R.Dale, Lawandwordorder: Nlpinlegaltech, legaldomain:Insightsandchallenges, NLLP2022
NaturalLanguageEngineering25(2019)211–217. 2022(2022)296–304.
[2] H.Zhong,C.Xiao,C.Tu,T.Zhang,Z.Liu,M.Sun, [13] I.Chalkidis,X.Dai,M.Fergadiotis,P.Malakasiotis,
How does nlp benefit legal system: A summary D.Elliott, Anexplorationofhierarchicalattention
oflegalartificialintelligence, in: Proceedingsof transformersforefficientlongdocumentclassificathe 58th Annual Meeting of the Association for tion, arXivpreprintarXiv:2210.05529(2022).
ComputationalLinguistics,2020,pp.5218–5230. [14] D. Mamakas, P. Tsotsi, I. Androutsopoulos,
[3] I.Chalkidis,A.Jana,D.Hartung,M.Bommarito, I.Chalkidis, Processinglonglegaldocumentswith
I.Androutsopoulos,D.Katz,N.Aletras, Lexglue:A pre-trainedtransformers: Moddinglegalbertand
benchmarkdatasetforlegallanguageunderstand- longformer,arXivpreprintarXiv:2211.00974(2022).
inginenglish, in:Proceedingsofthe60thAnnual [15] N.Ding,S.Hu,W.Zhao,Y.Chen,Z.Liu,H.Zheng,
MeetingoftheAssociationforComputationalLin- M.Sun, Openprompt:Anopen-sourceframework
guistics(Volume1:LongPapers),2022,pp.4310– forprompt-learning, in: Proceedingsofthe60th

## AnnualMeetingoftheAssociationforComputa-

[4] I. Chalkidis, M. Fergadiotis, I. Androutsopoulos, tionalLinguistics: SystemDemonstrations,2022,
Multieurlex-amulti-lingualandmulti-labellegal pp.105–113.
documentclassificationdatasetforzero-shotcross- [16] S.Bach,V.Sanh,Z.X.Yong,A.Webson,C.Raffel,
lingualtransfer, in:Proceedingsofthe2021Con- N.V.Nayak,A.Sharma,T.Kim,M.S.Bari,T.Févry,
ferenceonEmpiricalMethodsinNaturalLanguage etal., Promptsource:Anintegrateddevelopment
Processing,2021,pp.6974–6996. environmentandrepositoryfornaturallanguage
[5] L.Ouyang,J.Wu,X.Jiang,D.Almeida,C.Wain- prompts, in:Proceedingsofthe60thAnnualMeetwright,P.Mishkin,C.Zhang,S.Agarwal,K.Slama, ingoftheAssociationforComputationalLinguis-
A.Ray,etal., Traininglanguagemodelstofollow tics:SystemDemonstrations,2022,pp.93–104.
instructionswithhumanfeedback, Advancesin [17] H. Chase, LangChain, 2022. URL: https://github.
NeuralInformationProcessingSystems35(2022) com/hwchase17/langchain.
27730–27744. [18] J.Liu,LlamaIndex,2022.URL:https://github.com/
[6] T.Wu,M.Terry,C.J.Cai, Aichains:Transparent jerryjliu/gpt_index.
andcontrollablehuman-aiinteractionbychaining [19] S.Rush,Mini-Chain,2023.URL:https://github.com/
large language model prompts, in: Proceedings srush/MiniChain/.
ofthe2022CHIConferenceonHumanFactorsin [20] D.Trautmann,A.Petrova,F.Schilder,Legalprompt
ComputingSystems,2022,pp.1–22. engineeringformultilinguallegaljudgementpre-
[7] J.Wei,X.Wang,D.Schuurmans,M.Bosma,E.Chi, diction, arXiv preprint arXiv:2212.02199 (2022).
Q.Le,D.Zhou, Chainofthoughtpromptingelicits URL:https://doi.org/10.48550/arXiv.2212.02199.
reasoninginlargelanguagemodels, arXivpreprint [21] F. Yu, L. Quartey, F. Schilder, Legal prompting:
arXiv:2201.11903(2022). Teachingalanguagemodeltothinklikealawyer,
[8] T.Wu,E.Jiang,A.Donsbach,J.Gray,A.Molina, arXivpreprintarXiv:2212.01326(2022).
M.Terry,C.J.Cai, Promptchainer:Chaininglarge [22] M. Bommarito II, D. M. Katz, Gpt takes the bar
languagemodelpromptsthroughvisualprogram- exam, arXivpreprintarXiv:2212.14402(2022).
ming, in: CHIConferenceonHumanFactorsin [23] D.M.Katz,M.J.Bommarito,S.Gao,P.Arredondo,
ComputingSystemsExtendedAbstracts,2022,pp. Gpt-4 passes the bar exam, Available at SSRN
1–10. 4389233(2023).
[9] O. Khattab, K. Santhanam, X. L. Li, D. Hall, [24] S. Black, S. Biderman, E. Hallahan, Q. Anthony,
P.Liang,C.Potts,M.Zaharia, Demonstrate-search- L.Gao,L.Golding,H.He,C.Leahy,K.McDonell,
predict: Composingretrievalandlanguagemod- J. Phang, et al., Gpt-neox-20b: An open-source
els for knowledge-intensive nlp, arXiv preprint autoregressivelanguagemodel, Challenges&PerarXiv:2212.14024(2022). spectivesinCreatingLargeLanguageModels(2022)
[10] V. Wagh, S. Khandve, I. Joshi, A. Wani, G. Kale, 95.
R.Joshi, Comparativestudyoflongdocumentclas- [25] L.Gao,S.Biderman,S.Black,L.Golding,T.Hoppe,
sification, in:TENCON2021-2021IEEERegion10 C.Foster,J.Phang,H.He,A.Thite,N.Nabeshima,
Conference(TENCON),IEEE,2021,pp.732–737. et al., The pile: An 800gb dataset of diverse
[11] H.H.Park,Y.Vyas,K.Shah, Efficientclassifica- text for language modeling, arXiv preprint
tionoflongdocumentsusingtransformers, arXiv arXiv:2101.00027(2020).
preprintarXiv:2203.11258(2022). [26] Y.Tay,M.Dehghani,V.Q.Tran,X.Garcia,D.Bahri,

<!-- Page 8 -->

T.Schuster,H.S.Zheng,N.Houlsby,D.Metzler,Uni- A. Compute Requirements
fyinglanguagelearningparadigms, arXivpreprint
arXiv:2205.05131(2022). WeusedthefollowingAmazonEC2M5instance:
[27] S.Longpre,L.Hou,T.Vu,A.Webson,H.W.Chung,
Y. Tay, D. Zhou, Q. V. Le, B. Zoph, J. Wei, et al., StandardInstance vCPU Memory
Theflancollection: Designingdataandmethods
ml.m5d.24xlarge 96 384GiB
for effective instruction tuning, arXiv preprint
arXiv:2301.13688(2023).
Wehaven’tusedanyGPUsinourexperiments.
[28] Y.Liu,P.Liu,D.Radev,G.Neubig, Brio:Bringing
ordertoabstractivesummarization,in:Proceedings
ofthe60thAnnualMeetingoftheAssociationfor B. SCOTUS issue areas
ComputationalLinguistics(Volume1:LongPapers),
2022,pp.2890–2903. • CriminalProcedure
[29] M.Lewis,Y.Liu,N.Goyal,M.Ghazvininejad,A.Mo- • CivilRights
hamed,O.Levy,V.Stoyanov,L.Zettlemoyer, Bart: • FirstAmendment
Denoisingsequence-to-sequencepre-trainingfor • DueProcess
naturallanguagegeneration,translation,andcom-
• Privacy
prehension, in: Proceedingsofthe58thAnnual
• Attorneys
MeetingoftheAssociationforComputationalLin-
• Unions
guistics,2020,pp.7871–7880.
• EconomicActivity
[30] Z.Shen,K.Lo,L.Yu,N.Dahlberg,M.Schlanger,
• JudicialPower

### D.Downey, Multi-lexsum:Real-worldsummaries

ofcivilrightslawsuitsatmultiplegranularities, in: • Federalism
Thirty-sixthConferenceonNeuralInformationPro- • InterstateRelations
cessingSystemsDatasetsandBenchmarksTrack, • FederalTaxation
2022. • Miscellaneous
[31] N. Reimers, I. Gurevych, Sentence-bert: Sen- • PrivateActionwasnotavailableinthedata
tenceembeddingsusingsiamesebert-networks, in:

### Proceedingsofthe2019ConferenceonEmpirical

Methods in Natural Language Processing, AssociationforComputationalLinguistics,2019.URL:
http://arxiv.org/abs/1908.10084.
[32] L.Zheng,N.Guha,B.R.Anderson,P.Henderson,

### D.E.Ho, Whendoespretraininghelp?assessing

self-supervisedlearningforlawandthecasehold
datasetof53,000+legalholdings,in:Proceedingsof
theeighteenthinternationalconferenceonartificial
intelligenceandlaw,2021,pp.159–168.
[33] T. Schick, J. Dwivedi-Yu, R. Dessì, R. Raileanu,
M.Lomeli,L.Zettlemoyer,N.Cancedda,T.Scialom,

### Toolformer:Languagemodelscanteachthemselves

tousetools,arXivpreprintarXiv:2302.04761(2023).
[34] W. Yu, D. Iter, S. Wang, Y. Xu, M. Ju, S. Sanyal,

### C.Zhu,M.Zeng,M.Jiang, Generateratherthan

retrieve:Largelanguagemodelsarestrongcontext
generators, arXivpreprintarXiv:2209.10063(2022).
[35] X. Wang, J. Wei, D. Schuurmans, Q. Le, E. Chi,
D. Zhou, Self-consistency improves chain of
thought reasoning in language models, arXiv
preprintarXiv:2203.11171(2022).
[36] I.Chalkidis, Chatgptmaypassthebarexamsoon,
but has a long way to go for the lexglue benchmark(2023).URL:https://dx.doi.org/10.2139/ssrn.
4385460.

## Tables

**Table (Page 1):**

| Legal Document |  |  |  |
|---|---|---|---|
|  |  | Label |  |
|  |  | Label |  |
|  | ? | Labe |  |
|  |  |  |  |
|  |  |  | Label Generation |


**Table (Page 1):**

|  |  |
|---|---|
| CWPr Eoo UrckR esehdoinpgshISttSpN:// c1e6u1r3-w-0s0.o7r3g |  |


**Table (Page 5):**

| 732 | 93 |
|---|---|
| 137 | 38 |


**Table (Page 5):**

| 235 | 8 | 43 | 23 | 8 | 0 | 39 | 2 | 0 | 0 | 2 | 0 | 0 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 3 | 128 | 17 | 39 | 13 | 3 | 7 | 5 | 10 | 1 | 0 | 0 | 0 |
| 9 | 9 | 149 | 18 | 13 | 3 | 8 | 3 | 2 | 3 | 0 | 1 | 0 |
| 10 | 29 | 40 | 50 | 21 | 0 | 3 | 5 | 4 | 1 | 0 | 0 | 2 |
| 3 | 3 | 10 | 2 | 85 | 0 | 3 | 0 | 0 | 1 | 1 | 0 | 0 |
| 0 | 24 | 17 | 10 | 2 | 18 | 2 | 6 | 4 | 0 | 0 | 0 | 0 |
| 11 | 7 | 19 | 10 | 2 | 4 | 13 | 2 | 1 | 0 | 0 | 0 | 1 |
| 0 | 2 | 5 | 10 | 2 | 0 | 0 | 31 | 0 | 0 | 0 | 0 | 0 |
| 0 | 2 | 0 | 0 | 1 | 1 | 1 | 0 | 33 | 0 | 0 | 0 | 0 |
| 0 | 3 | 19 | 0 | 3 | 0 | 3 | 0 | 0 | 6 | 0 | 0 | 1 |
| 1 | 0 | 2 | 3 | 6 | 0 | 0 | 0 | 1 | 0 | 9 | 0 | 0 |
| 0 | 3 | 1 | 0 | 0 | 5 | 0 | 0 | 0 | 0 | 0 | 5 | 0 |
| 1 | 0 | 1 | 4 | 0 | 0 | 1 | 0 | 2 | 0 | 0 | 0 | 1 |


**Table (Page 6):**

| Model | Precision | Recall | macro-F1 | micro-F1 | weighted-F1 |
|---|---|---|---|---|---|
| minorityclass randomclass majorityclass GPT-NeoX(0-shot,(F)) GPT-NeoX(8-shot,(S)) | .088 .506 .412 .527 .566 | .500 .510 .500 .536 .552 | .149 .451 .452 .526 .556 | .175 .514 .825 .709 .770 | .052 .572 .746 .731 .756 |
| minorityclass randomclass majorityclass GPT-NeoX(0-shot,(F)) GPT-NeoX(8-shot,(S)) | .077 .479 .423 .522 .525 | .500 .460 .500 .530 .537 | .133 .410 .459 .521 .527 | .153 .484 .847 .707 .779 | .041 .555 .777 .728 .768 |


**Table (Page 6):**

| Model | Precision | Recall | macro-F1 | micro-F1 | weighted-F1 |
|---|---|---|---|---|---|
| majorityclass randomclass FLAN-UL2(8-shot,(S)) | .020 .070 .529 | .077 .064 .455 | .031 .057 .461 | .257 .071 .545 | .105 .084 .543 |
| majorityclass randomclass FLAN-UL2(8-shot,(S)) FLAN-UL2(8-shot,(S))† | .020 .079 .427 .435 | .077 .074 .373 .388 | .032 .060 .359 .371 | .266 .077 .486 .484 | .112 .095 .483 .480 |
| ChatGPT(0-shot,(F)) supervised(full) | - - | - - | .420 .695 | .438 .782 | - - |


**Table (Page 6):**

| Label | #Samples |
|---|---|
| CriminalProcedure FederalTaxation FirstAmendment Unions EconomicActivity CivilRights Privacy InterstateRelations Federalism JudicialPower Attorneys DueProcess Miscellaneous | 360 226 218 165 108 83 70 51 38 35 22 14 10 |


**Table (Page 8):**

| vCPU |
|---|
| 96 |
