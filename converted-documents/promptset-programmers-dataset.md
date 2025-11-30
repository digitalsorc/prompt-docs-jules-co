---
title: "PromptSet Programmers Dataset"
original_file: "./PromptSet_Programmers_Dataset.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["prompt-engineering", "llm", "rag", "chain-of-thought", "agents"]
keywords: ["arxiv", "https", "promptset", "com", "prompts", "lisbon", "portugal", "page", "madison", "github"]
summary: "<!-- Page 1 -->

PromptSet: A Programmer’s Prompting Dataset

### KaiserPister∗ DhrubaJyotiPaul

kaiser@cs.wisc.edu UniversityofWisconsin-Madison
UniversityofWisconsin-Madison Madison,USA

### Madison,USA


### PatrickBrophy IshanJoshi

UniversityofWisconsin-Madison UniversityofWisconsin-Madison
Madison,USA Madison,USA

## Abstract 1 Introduction

Theriseofcapabilitiesexpressedbylargelanguagemodelshas Aslargelanguagemodels(LLMs)becomemoreeffective,moresoftbeenquicklyfollowedbytheintegrationofthe"
related_documents: []
---

# PromptSet Programmers Dataset

<!-- Page 1 -->

PromptSet: A Programmer’s Prompting Dataset

### KaiserPister∗ DhrubaJyotiPaul

kaiser@cs.wisc.edu UniversityofWisconsin-Madison
UniversityofWisconsin-Madison Madison,USA

### Madison,USA


### PatrickBrophy IshanJoshi

UniversityofWisconsin-Madison UniversityofWisconsin-Madison
Madison,USA Madison,USA

## Abstract 1 Introduction

Theriseofcapabilitiesexpressedbylargelanguagemodelshas Aslargelanguagemodels(LLMs)becomemoreeffective,moresoftbeenquicklyfollowedbytheintegrationofthesamecomplexsys- wareiswrittentocontrolandcapturetheirpotential.Foranygiven
temsintoapplicationlevellogic.Algorithms,programs,systems, task,adeveloperwillhavethreecommonoptionstoimproveLLM
andcompaniesarebuiltaroundstructuredpromptingtoblackbox performance:improvethefoundationalmodel,finetuneafoundamodelswherethemajorityofthedesignandimplementationlies tionalmodeltowardsaspecifictask,oruseatasktailoredprompt.
incapturingandquantifyingthe‘agentmode’.Thestandardway Majorimprovementsacrossmanybenchmarkscanbeachievedby
toshapeaclosedlanguagemodelistoprimeitforaspecifictask retrainingthebasemodelfromscratch,howeveroutsideoflarge
withatailoredprompt,ofteninitiallyhandwrittenbyahuman.The researchlabs,thisisanintractabletask[14,21,28].Finetuningcan
textualpromptsco-evolvewiththecodebase,takingshapeoverthe functionasacheaperalternativetoretrainingfromscratch,but
courseofprojectlifeasartifactswhichmustbereviewedandmain- canrequireamodestsizeddatasettoachievemeaningfulresults.
tained,justasthetraditionalcodefilesmightbe.Unliketraditional Additionally,itleadstocatastrophicforgettingandcomplexmodel
code,wefindthatpromptsdonotreceiveeffectivestatictestingand managementwhenworkingwithmultipletasks[11,27].Promptlintingtopreventruntimeissues.Inthiswork,wepresentanovel ingcanserveasacheap,efficientwaytocontrolanLLMwithout
datasetcalledPromptSet,withmorethan61,000uniquedeveloper significantinvestmentininfrastructureordata[4,36].Sincethe
promptsusedinopensourcePythonprograms.Weperformanal- introductionoffew-shotlearning,promptinghasbecomeanecesysisonthisdatasetandintroducethenotionofastaticlinterfor saryfeatureofworkingwithLLMs,anddespitetheproliferationof
prompts.ReleasedwiththispublicationisaHuggingFacedataset researchintopromptengineering,in-context-learningandsimilar
andaGithubrepositorytorecreatecollectionandprocessingefforts, fields,therehasbeenrelativelylittleexplorationofpromptmanagebothunderthenamepisterlabs/promptset. ment[24,38].What’smore,thereexistsnostandardmethodology
for working with prompts, leading to incoherent collections of
CCSCONCEPTS files,folders,JSONobjects,andcodestringsinhibitingreadability,
reusability,andmaintainability[15].
•Computingmethodologies→Naturallanguagegeneration.
With LLMs moving from research into production, it is ever
moreimportanttotreatthepromptswhichcontrolbusinesslogic

## Keywords

asfirstclasscitizensintheCI/CDpipelinesoftraditionalsoftware

### PromptManagement,LargeLanguageModels,Dataset,Information

engineering.Therearemanyworksfocusingonassessingandopsystems,Ethnography,Taxonomy
timizingtheeffectivenessofaprompt,onceitisinyoursystem
(eitherautomaticallyormanually),buttheserelyonruntimecom-

### ACMReferenceFormat:

KaiserPister,DhrubaJyotiPaul,PatrickBrophy,andIshanJoshi.2024. putationagainstanLLMbackboneanddonotprovideanystatic
PromptSet:AProgrammer’sPromptingDataset.In2024InternationalWork- guarantees[18,19,35,37].
shoponLargeLanguageModelsforCode(LLM4Code’24),April20,2024, Inthiswork,weproposestaticanalysispassestoaddtoanexist-
Lisbon,Portugal.ACM,NewYork,NY,USA,8pages.https://doi.org/10.1145/ ingCI/CDpipelinetopreemptivelydetectnon-traditionalerrorsin
3643795.3648395 prompts,suchasmisuseofvariableformatting,typodetection,and
inputsanitization.Inordertomotivatethesepasses,weintroducea
∗Alsowith PisterLabs. suiteofextractiontechniquestoparsepromptsfromcodefilesand
anoveldataset,PromptSet,ofmorethan61,000uniquedeveloper
Permissiontomakedigitalorhardcopiesofallorpartofthisworkforpersonalor prompts used in open source Python programs. Finally, we are
classroomuseisgrantedwithoutfeeprovidedthatcopiesarenotmadeordistributed
thefirsttoourknowledgetodiscussunittestinginthecontextof
forprofitorcommercialadvantageandthatcopiesbearthisnoticeandthefullcitation
onthefirstpage.Copyrightsforcomponentsofthisworkownedbyothersthanthe promptsascode.
author(s)mustbehonored.Abstractingwithcreditispermitted.Tocopyotherwise,or
republish,topostonserversortoredistributetolists,requirespriorspecificpermission
and/orafee.Requestpermissionsfrompermissions@acm.org.

### LLM4Code’24,April20,2024,Lisbon,Portugal 2 BACKGROUND

©2024Copyrightheldbytheowner/author(s).PublicationrightslicensedtoACM. Weabstractthelanguagemodeltoitsfunctionalpurposeofdecod-

## Acmisbn979-8-4007-0579-3/24/04

https://doi.org/10.1145/3643795.3648395 ingtokensbasedonaninputsequenceoftokens[10].Theinternal
4202
beF
62
]ES.sc[
1v23961.2042:viXra

<!-- Page 2 -->

LLM4Code’24,April20,2024,Lisbon,Portugal Pister,etal.
mechanismsareindependentoftheworkpresentedhere.Foranin- 2.2 OtherPromptingDatasets
depthunderstandingoftheaforementionedarchitecture,wedirect At Mining Software Repositories ’24, there was a code mining
readerstowardtheexistingliteratureonthissubject.[5,22,31]. challengeaddressingasimilartaskofunderstandingthepurpose
Followingthediscoveryofzero-shotandfew-shotabilitiesof ofpromptssenttoDevGPT,achatbotbuiltfortalkingtocode
LLMs,acottageindustryofobservationtoolshasdevelopedinthe repositoriesonGithub[34].Incontrasttothepromptswefindin
market,allowingprogrammerstoadequatelymonitorandexperi- ourdataset,DevGPTpresentsconversationaltext,similartoauser
mentwithopenaccesslanguagemodels[1,29].Thesetoolsgive talkingonChatGPT.PromptSetrepresentsprogrammaticprompts
userstheabilitytodetectanomaliesintheiragentsystems,afford- thatoftendictateapplicationlevellogic.Thesepromptsarenot
ingreliabilityinadesignspacethatisnotoriouslyunreliable.In designedforchattingwithauser,exceptoccasionallybywayofa
parallel,qualityisaffordedbyalargearrayoftoolsforoptimizing programmedbot.
theperformanceofindividualprompts.Onlinecoursesforprompt
engineeringasadisciplinehavecroppedupadjacenttoGithub

## 3 Methodology

repositoriesof"awesome-prompts"toimproveadeveloper’sman-

### Towardsthegoalofdevelopingmeaningfulstaticanalysispasses,

ualpromptingability[6,33].Althoughthetopicisoftencriticised
wefirstperformanethnographicsurveyofhowdevelopersbuild
as a pseudo-science, common tricks and minor variations have
applicationswithopenLLMSDKs.Thecodesurveyisintendedto
demonstrablylargeeffectsonthequalityofresults[2].Automatic
validateourhypothesesandmotivatethedevelopmentoftargeted
optimizationtoolsleverageanLLMasaself-optimizeracrossan
lintingrulesorunittests.WemakePromptSetopenlyavailableto
establisheddatasettoimprovepromptquality[35].
facilitatefuturestaticanalysisfromthecommunity.
Intraditionalsoftwareengineeringreliabilityandqualityare

### Ourpromptdatasetoriginatesfromopensourcecodehostedon

checkedregularlythroughtheuseofcontinuousintegrationand

### Github.WescrapePythoncodefileswhichfulfillasimplecriteria

delivery(CI/CD)systems.CI/CDpipelinescanmanagemanyasof using a language model library; see appendix A for the spepectsofacodebase,suchasformatting,linting,andunittesting.
cificquerystring.Wesearchforusageoftheopenai,anthropic,

### Regardlessoftheimplementation,thesesystemsareresponsible

cohere,andlangchainlibraries,astheseareregularlycitedasthe
forreducingthenumberofissuesdeployedtoproductionsystems.
mostpopulartoolsinonlineresources.Weignoreforkedreposito-

### Formattingkeepscodeconsistent,simplifyingreviewsbetween

riestoreduceduplication.Notably,weexcludethetransformers
teammembers.Lintingusesstaticanalysistokeepacodebase
librarywhichwouldincludetextprompts,butwefindittohave
cleanfromcommonproblems.Unittestingguaranteesrun-time
toomanyfalsepositivesduetoitsotherusecases.Figure1shows
assumptionsatagranularlevel.Asdevelopmentteamsscaletononanexamplecodefilewhichhasbeenflaggedforprocessing.
trivialsizes,CI/CDbecomesoneofthekeyfactorsinmaintaining
featurevelocity[13].
3.1 ExtractingPrompts

### Primarilyduetotheinfancyofthefieldofprompting,wefindthe

CI/CDecosystemforpromptingwanting.Formattingforprompts WeutilizeTree-sitterforbuildingabstractsyntaxtree(AST)repreresidesatthelevelofthedeveloper’seditorandisagnostictothe sentationsofeachscrapedfileandthenqueryagainstthetreewith
purposeoftheprompt.Oftenapromptexistsalongsidetherest specificpatternsbasedonAPIdesignspecificationsandcommonly
ofthecodeasasimplestring.Theredoesnotexistanyformof observedbehavior[30].
lintingforprompts,evenbugsassimpleasamismatchedvariable Weexpectourdatasettobeasubsetoftheentiresetofprompts
interpolationwon’tbedetecteduntilrun-time. inthesefilesasdiscussedinsection5.1.
Functionality(integration)testingofpromptsisquitepopular, (1) OpenAI&AnthropicAPIcalls:
andtherearemanytoolsthatsupportthisbehavior[25].Wedistin- BothOpenAI(beta,v1)andAnthropichavesimilarAPIdeguishbetweentheeffectivenessofaprompt(itsevaluationresults signspecifications.TheSDKsexpose.createfunctionson
onadataset)andthecharacteristicsoftheprompt.Forexample,a the.completionsendpoint.OpenAIadditionallyexposes
unittestofapromptmightbeanassertionthatthepromptdoes a.chatvariant,whichiscapturedwiththesamepattern.
notattempttointerpolateastringintoanintegerformattedslot Fromthemethodcalls,weextractspecificargumentvalues
(e.g."Num: {:02d}".format("x")).Abugofthisclasscouldbe forpositionallypassedarguments,aswellasthekeyword
detectedbyastaticanalysispass,similartoanytraditionaltype argumentspromptandmessages.Commonadditionalarguerror. mentsaretrackedanddisplayedinTable3.
(2) CohereAPIcalls:
TheCohereSDKexposesmultiplemethodsforhandlingtext
input.Thetwomainentrypointsare.chatand.summarize.
2.1 TaxonomiesofPrompts Wepatternmatchonthesecalls,andfollowthesamemethod-
Otherworkshavelookedtobuildaprescriptivetaxonomyofef- ologyasaboveforextractingthearguments.
fectivepromptingtechniques[9,33].Weleveragetheseworksto (3) LangChainPromptTemplateandMessageclasses:
categorizeandclassifyourpromptdataset,butfindthatalarge LangChainintroducesmultiplewaystocreateprompts,in
majorityofourpromptsdonotfitneatlyintooneormoreofthese particularaPromptTemplateclassandaMessage
categories.Wetakeanunsupervised,descriptiveapproachwith (HumanMessage,AIMessage)class,whichsupportcompleourclassifications,andleavefurthercategoryrefinementtofuture tionandchatendpointsrespectively.Thesearebaseclasses
work. thatdeveloperscanextendwiththeirownfunctionality.We

<!-- Page 3 -->

PromptSet:AProgrammer’sPromptingDataset LLM4Code’24,April20,2024,Lisbon,Portugal

### Figure1:Examplecodefile

searchforconstructorcallsofclasseswhichcontain*Prompt pattern,butnotethatthiscouldbeanoisyheuristic.Inpracor*Messageintheirname,andextracttheargumentspassed ticeitprovestomatchthequalityoftheotherextraction
totheinitializefunction. techniques.1
(4) LangChainTools: (7) "content"indictionaries
LangChainexposesaPythondecoratorforautomatically Thebasicstructureformanychatmessagingtemplatesis
convertingafunctionintoanLLMtoolusingthefunction’s usingaPythondictionarywiththekeysroleandcontent.
docstringandtypehintsasthetool’sdescription.Similarly, Theroleentrytypicallycontains"user","system"or"assistheyallowforextendingaBaseToolclass.Wematchon tant".Thecontententrycontainsthemessagethatwillbe
@tooldecoratorsandBaseToolsuperclassestodetectthese senttoLLM.Wedirectlysearchfordictionarieswiththe
usecases. specifickeymatching"content"toextracttheseprompts.
(5) PromptTemplate.from_file (8) DevGPTConversationPrompts
LangChainallowsuserstosavepromptstostandardtextfiles, Finally,weaddthepromptsfromtherecentDevGPTMSR
andloadthematruntimeforprocessing.Thefrom_file challengetocompareandcontrastagainstPromptSet.These
functionaccomplishesthistask,andwematchdirectlyon promptsaredifferentinnature,andwekeepthemseparate
anyuseof*Template.from_file. throughourevaluation.
(6) PromptandTemplatevariables
Fromourobservations,weseethatthevastmajorityofvari- 3.2 Post-Processing
ablesusedaspromptsarenamedwiththekeyphraseprompt
AfterextractingthekeyregionsoftheASTfromeachfile,weuse
ortemplate.Weflaganyvariabledeclarationsmatchingthis
theblackformattertoconsistentlyformattheinputsforbetter
1Wefoundthemessagenamewasoverloadedtoooftentobeofmuchuse.

<!-- Page 4 -->

LLM4Code’24,April20,2024,Lisbon,Portugal Pister,etal.
readabilityanddeduplication[8].Finally,weusetree-sitteragain Table1:PromptCountperSource
toextractstrings,identifiers,andinterpolationsperprompt.
Library Source Count
3.3 IncreasingYield

### OpenAI/Anth. completions.create 12,420

Afterperformingafirstiterationthroughtheseheuristics,were-

### Cohere .chat 260

viewedtheextractedpromptsaswellasthefileswhichfailedtofind

### LangChain @tool 1,425

anypromptsandrefinedtheextractionprocess.Inparticular,we

### LangChain Template/Messageclass 24,302

addedanaive𝛽-substitutionpreprocessingsteptoreplaceconstant

### LangChain from_file 21

expressionswiththeirrespectivevaluesthroughoutthefile.As

### All Prompt/Templatename 94,897

weprocessafileinsearchofpromptpatterns,wetrackconstant

### All ContentKeyindictionary 34,324

variabledeclarationsbylookingforstaticsingleassignmenttovari-

### DevGPT Conversations 13,748

ablenamesinthesamefile.Furthermore,weconstructasimple
string-evaluationlanguageforprocessingstringoperationssuchas
concatenationandinterpolationacrossthestaticvariableset.See Table2:UniquePrompts
listing1foranexample.
Wenotethatthisstringinterpreterissoundbutnotcomplete,

### Set TotalFound Unique Length>10 Repositories

andcannotprocessallPythonstringmanipulations.Furtherexplo-

### PromptSet 118,862 61,448 57,981 20,598

rationofpartialexecutionmodelscouldbeleveragedtoincrease

### DevGPT 13,748 13,236 13,053 -

theyieldofprompts,butweleavethistofuturework.
1 import cohere # file is flagged for processing
2 Table3:LLMCallArguments
3 co = cohere.Client()
4 pre = "You are an agent working at the check-in desk."
5 query = pre + " User said: {history}" Parameter MostCommon2 2nd 3rd
6 co.generate(query) # flag `query`
model gpt-3.5-turbo davinci-003 gpt-4
7
8 # compute: query [pre:= "You are...", history: <free>] temperature 0 0.7 0.5
9 # query := "You are an ... User said: PLACEHOLDER" top_p 1 0.95 0.5
Listing1:naive𝛽-substitution max_tokens 100 1024 1000
3.4 DiscardedHeuristics
thetruenegativesarefilesthatonlyusethesemanticembedding
Weconsideramulti-linestringheuristicbutuponreviewfoundtoo
functionalityoftheselibrariesorprovidelightwrappersaround
manyfalsepositivesgiventhecorrelationbetweenthestreamlit
thelibraryAPIs.AquickcheckagainstthesearchtermsonGithub
library,docstrings,andLLMdevelopment.Weconsiderasequence
revealsthattheratioofextractedpromptsmatchesroughlywiththe
classifiertodetectpromptsbutdiscarditforsimilarreasons.
distributionbetweenLangChain(mostpopular),OpenAI(popular),
and Cohere (uncommon). Tool usage was introduced relatively

## 4 Results

recently,sothesmallcountoftoolsisexpected.
WedescribePromptSetintwoparts.Firstweprovideasurface

### Inordertoperformper-promptanalysis,wejointheprompts

overviewofthedataset,thenweprovidespecificfindingsfrom
intoasinglesetfortesting.Theresultsofdeduplicationareshown
ouranalysis.Thepromptscrapingandextractionwaslastrunon
in table 2. We display length and language distributions of the

### January10,2024.BymanuallysearchingGithubwithourqueries,

dataset in figures 2 and 3. Language is detected on prompts of
weapproximatethatthereare153,000codefileswhichmatchour
lengthgreaterthantencharactersusingtheftlangdetectpackage
searchcriteria.Duetoratelimiting,weareabletodownload93,142
[16,17].ThemajorityofpromptsarewritteninEnglish,accounting
ofthesefiles,soweconcludethatourdatasetrepresents60.7%of
for 84.1% of the strings we extracted. The remaining 15.9% fall
theopen-sourceAPI-basedLLM-usage.The93,142codefilescome
betweenMandarin,Japanese,Spanish,French,German,andKorean
from37,944repositories.
(below1%arenotmentioned).
Briefly,weinvestigatethedistributionsofinterpolations,and
4.1 DatasetOverview
confirmthatthemostcommonvariablesarechat,query,input
Usingthemethodologydescribedinsection3.1,weextract118,862 andsimilarplaceholderinputvaluesforconversationalAI.There
totalpromptsfromthescrapedfiles,asseenintable1.Theextracted wasminimalrepresentationoftype-formattingstatementsinthe
promptscomefrom37,112ofthecodefiles(20,598repositories). dataset,(e.g."ratio:.2f"),allofwhichwerefloatingpointfor-
Theremaining56,030filesdonotcontainanypromptsmatching matting.
ourextractioncriteria,inpartduetooverscrapingfromGithuband Finally,weperformaZipf’slawanalysisontheinputtokens
inpartduetostrictpatternmatching.Weperformamanualreview usingthecl100k_basetokenizer,asthatsupportsthemostcomof 200 code files which report no prompts found and manually monmodelsused.Fromfigure4,weseethatthemassisdistributed
tag36asfalsenegatives,i.e.thesefilesdidcontainprompts,but
ourextractionmethodologydidnotfindthem.Themajorityof 2DatareportedfromoriginalNovemberdataset

<!-- Page 5 -->

PromptSet:AProgrammer’sPromptingDataset LLM4Code’24,April20,2024,Lisbon,Portugal
Figure4:Zipf’slawplottedontokensfromPromptSet.
resultsareshowninfigure5andanenumerationofthecategories
Figure2:DistributionofpromptlengthsinPromptSet.
withextractedexamplesisprovidedintable4.3
Theseresultsshowthatthereissomealignmentbetweentheprescribed"goodpromptingtechniques"andthepromptingtechniques
wefindinthewild,howevertherearestilllargediscrepancies.Many
usersareenactingthecategory-2,"OutputCustomization-Persona",
beginningtheirpromptswith"Actasa...",toelicitaspecifictype
ofresponse.ThedistributionofDevGPTpromptsismoreevenly
spreadthanthedistributionsofPromptSetwhichfavorscategories
1and2(InputandOutput).Webelievethistobethecasebecause
developersrequirestrictcontroloftheinputandoutputtotheir
systems.Onlyoncethoseareundercontrolcantheyleveragecategories3-6.Ontheotherhand,inaconversationtherearenosuch
restrictions.

### Manyofthepromptsfailtofallintoanyofthecategories,and

wesuspectthisisduetoafewcontributingfactors.First,some
ofthepromptsarepartialpromptswhichmightnohaveaclear
categorywithoutmorecontext.Second,sincethepromptswere
labeledwithanLLMwithameta-promptthatdidnotundergoany
optimization,thereisthepossibilityforerror.Third,thetaxonomy
proposedbyWhiteetal.isnowtenmonthsold,andthestudyof
promptinghasprogressedmuchsinceitsrelease.Itispossiblethat
anewcategorycouldemerge,thoughwedonotseeacleartrend
inthedatasetatthispoint.
Figure3:DistributionoflanguagesinPromptSet.
Inordertoperformourownclassification,wecreateaclustering
nearestneighborplotwiththesemanticmeaningofeachprompt.To
start,weembedeachpromptusingtheall-MiniLM-L6-v2model
fromthesentence-transformerslibrary[23].Wefitat-SNEwith
above the ideal line, meaning there is a more even distribution 10clusterstotheembeddingoutputsandshowtheresultsinfigure
acrossthetokensetthanintraditionalwriting. 6.Manualinspectionoftheclustersshowsmanysimilarities,and
weassignlabelednamesbasedonthemostcommonpatternswe
see.
4.2 CategorizationandClustering
Usingthedataset,webegininvestigationinmultipledirectionsto
4.3 TechniquePropagation
betterunderstandthepotentialusecasesoftheseprompts.Tostart,

### Nextweinvestigatethepropagationofresearchtechniquesinto

wefollowtheworkofWhiteetal.andcategorizetheprompts,using
PromptSetintable5.Weuseafewheuristicstoderiveusageofsome
thesixcategorieslaidoutintheirwork[33].Wecraftaprompt
ofthemostpopulartechniques,suchaschain-of-thought,fewshot
basedontheirexplanationofthecategoriesandsend2,200input
promptstothegpt-4-preview-1106modelforpredictionacross
3Interestingly,onlytwoofthepromptsinthe2,000PromptSetsampledpromptscaused
PromptSetandDevGPT(2,000forPromptSet,200forDevGPT).The breaksinourprompt.

<!-- Page 6 -->

LLM4Code’24,April20,2024,Lisbon,Portugal Pister,etal.
Table4:PromptPatternsPerWhiteetal.

### PatternName Source Example4

InputSemantics jxnl Youareanexpertatoutputtingjson.
YoualwaysoutputvalidJSONbasedonthepydanticschemagiventoyou.
OutputCustomization benczech212 Youareawizardshopownernamed{ASSISTANT_NAME}.
Onlytalkonthebehalfof{ASSISTANT_NAME}.Mynameis{USER_NAME}

### ErrorIdentification

PromptImprovement Kaastor Giventhefollowingconversationandafollowupquestion,rephrasethefollowupquestion
tobeastandalonequestion.
Interaction offtian Youareplayingthe’20Questions’gamewithanotherplayer.Yourroleistoanswer’Yes’or
’No’toquestionsbasedonagivenconceptorobject.
ContextControl nachollorca Yourtaskistoansweraquestiongivensomecontextgivenhere,delimitedbytriplebackticks:
thistobeanunderestimateonusage.Thedoccolumnrepresents
promptsmentioning"documents"whichhaveahighprevalencein
recentproductdevelopments.
4.4 ErrorInvestigation
Toperformanerrorinvestigation,wefirstlookfortyposinthe
prompts.Promptstendtobenaturallanguagerequests,typedby
hand and as we have observed, can be riddled with typos. We
usethecspellpackageoneachpromptandfindcloseto28,000
spellingerrorsacrosstheuniqueEnglishpromptsofPromptSet
[7].Manyofthespellingerrorsstemfrompropernounsandcode
relatedterminology,soweremovecapitalizedmistakesandwords
withunderscores,reducingtheerrorcountto16,989.Tofurther
improvetheaccuracytwoauthorsindependentlymanuallytag200
oftheseerrors,andfindatruepositiveratebetween33%-40%.Ifwe
extrapolatewiththisrate,therewouldbeatypoinapproximately
Figure5:CategorizationofPromptSet. 1of8prompts.
These mistakes are not limited to junior developers. In writingthiswork,wefoundtyposinourownpromptsaswellasthe
academicpapersthatwehavereviewed[26].
Finally, we develop a simple white space detection lint pass,
whichchecksfortrailingandleadingwhitespaceinprompts.The
officialdocumentationfromOpenAIdiscussesthattrailingwhite
spacesinpromptscanleadtopoortokenizationwhichcausesa
degradationinperformanceofthemodel.Whileasimple.strip()
can resolve the issue, there is no guarantee that this stripping
happensontheserverside.Thuswhitespacedetectionisaperfect
problemforalintertosolve.Theresultsintable6showthata
largeportionofthepromptswefinddoindeedhavetrailingwhite
spaces,suchasnewlines,tabsandspaces.

## 5 Discussion

Inthisworkweintroduceanoveldatasetwiththepurposeofbetter
understandinghowdevelopersareinteractingwiththenewfound
Figure6:t-SNEofPromptSet. powerofintegratingLLMsintotheirapplications.PromptSetindeed
displaysadiversityofideasandweacknowledgethateventhis
onlyrepresentsafractionoftheprogrammingpromptusagethat
prompting,andspecialtokens[3,32].Foreachofthesetechniques,
exists.
weassignafewrepresentativestringstofilteronthrougheach
ofthesplits.Chain-of-thought,forexample,matcheswith"stepby-step","stepbystep","let(’)sthink",and"thought(s):".Weexpect 4Promptsareabbreviatedforspace

<!-- Page 7 -->

PromptSet:AProgrammer’sPromptingDataset LLM4Code’24,April20,2024,Lisbon,Portugal

### Table5:ResearchTechniqueDetection

Set Total concise FewShot doc CoT CodeBlock InstructionBlock Scratchpad Tooluse SpecialTokens
PromptSet 57953 176(0.3) 1008(1.7) 1939(3.3) 1095(1.9) 1696(2.9) 927(1.6) 170(0.3) 168(0.3) 178(0.3)
DevSet 13053 2(0.0) 88(0.7) 1015(7.8) 105(0.8) 730(5.6) 120(0.9) 0(0.0) 319(2.4) 16(0.1)

### Table6:Leading&TrailingWhitespaceDetection REFERENCES

[1] LangChainAI.2023.LangServe. https://github.com/langchain-ai/langserve
[2] Anthropic.2023. Claude2.1Prompting. https://www.anthropic.com/index/
Set Total Trailing(%) Leading(%) All(%)
claude-2-1-prompting
PromptSet 58,814 17,668(30.0) 9,723(16.5) 19,681(33.5) [3] MaciejBesta,NilsBlach,AlesKubicek,RobertGerstenberger,LukasGianinazzi,
JoannaGajda,TomaszLehmann,MichalPodstawski,HubertNiewiadomski,
DevGPT 13,399 2,081(15.5) 235(1.8) 2,256(16.8) PiotrNyczyk,andTorstenHoefler.2023.GraphofThoughts:SolvingElaborate

### ProblemswithLargeLanguageModels. arXiv:2308.09687[cs.CL]

[4] TomBrown,BenjaminMann,NickRyder,MelanieSubbiah,JaredDKaplan,
PrafullaDhariwal,ArvindNeelakantan,PranavShyam,GirishSastry,Amanda
Askell,SandhiniAgarwal,ArielHerbert-Voss,GretchenKrueger,TomHenighan,
RewonChild,AdityaRamesh,DanielZiegler,JeffreyWu,ClemensWinter,
5.1 Limitations
ChrisHesse,MarkChen,EricSigler,MateuszLitwin,ScottGray,Benjamin
Asmentionedintheresults,weexpecttohaveapproximately60% Chess,JackClark,ChristopherBerner,SamMcCandlish,AlecRadford,Ilya
Sutskever,andDarioAmodei.2020.LanguageModelsareFew-ShotLearners.
publiccoverageofthelibrarieswemention,howeverthereare InAdvancesinNeuralInformationProcessingSystems,H.Larochelle,M.Ranotherlibrarieswedidnotconsiderscrapingandmanyclosedsource zato,R.Hadsell,M.F.Balcan,andH.Lin(Eds.),Vol.33.CurranAssociates,
Inc.,1877–1901. https://proceedings.neurips.cc/paper_files/paper/2020/file/
repositoriesthatareobviouslyoutofreach.Additionally,werestrict
1457c0d6bfcb4967418bfb8ac142f64a-Paper.pdf
oursettoPython,butthereisanactiveJavaScriptdevelopment [5] TomB.Brown,BenjaminMann,NickRyder,MelanieSubbiah,JaredKaplan,
communityfocusedonLLMdevelopmentaswell.Beyondhitting PrafullaDhariwal,ArvindNeelakantan,PranavShyam,GirishSastry,Amanda
Askell,SandhiniAgarwal,ArielHerbert-Voss,GretchenKrueger,TomHenighan,
APIlimitstofullysearchGithub,theextractiontechniquesproposed
RewonChild,AdityaRamesh,DanielM.Ziegler,JeffreyWu,ClemensWinter,
donotfindthefullsetofpromptstringsusedinthefilesmentioned, ChristopherHesse,MarkChen,EricSigler,MateuszLitwin,ScottGray,Benjamin
nordotheyextractpromptsfromadjacentfilesinthesamesystem Chess,JackClark,ChristopherBerner,SamMcCandlish,AlecRadford,Ilya
Sutskever,andDarioAmodei.2020.LanguageModelsareFew-ShotLearners.
(forexamplepromptsthatwereimportedfromanotherfile).This arXiv:2005.14165[cs.CL]
meansthatwhilePromptSetcontainsalargenumberofdiverse [6] MiguelCorralm.2023. AwesomePrompting. https://github.com/corralm/
awesome-prompting
prompts,itmightnotreflectthetruedistributionandcharacteristics
[7] CSpell.2023.CSpell. https://www.npmjs.com/package/cspell
ofprompts.Consequently,ourdatasetisnotexhaustiveandmay [8] PythonSoftwareFoundation.2023.Black. https://github.com/psf/black
notincludeallrelevantdatapoints,afactorthatmustbeconsidered [9] Thorsten Händler. 2023. Balancing Autonomy and Alignment: A Multi-
DimensionalTaxonomyforAutonomousLLM-poweredMulti-AgentArchitecwheninterpretingthefindings,asitcouldleadtogapsthataffect
tures.ArXivabs/2310.03659(2023). https://api.semanticscholar.org/CorpusID:
theoverallresults. 263671545
[10] AriHoltzman,PeterWest,andLukeZettlemoyer.2023.GenerativeModelsas
aComplexSystemsScience:Howcanwemakesenseoflargelanguagemodel
5.2 FutureWork behavior?preprint(2023).
[11] EdwardJHu,YelongShen,PhillipWallis,ZeyuanAllen-Zhu,YuanzhiLi,Shean
Despite the potential benefit to readability, we cannot quantify Wang,LuWang,andWeizhuChen.2022.LoRA:Low-RankAdaptationofLarge
thattyposorpromptmistakesarebadforeverypossibletask[20]. LanguageModels.InInternationalConferenceonLearningRepresentations. https:
//openreview.net/forum?id=nZeVKeeFYf9

### Insteadwepositthatinthemajorityofthecases,adeveloperwould

[12] YangsiboHuang,SamyakGupta,MengzhouXia,KaiLi,andDanqiChen.2023.
liketoactivelymakeachoiceinhandlingthelikelymistakesof CatastrophicJailbreakofOpen-sourceLLMsviaExploitingGeneration.arXiv
typos. preprintarXiv:2310.06987(2023).
[13] Instagram.2016. ContinuousDeploymentatInstagram. https://instagram-
Agoodunittestforapromptmighttestthatthepromptfollows engineering.com/continuous-deployment-at-instagram-1e18548f01d1
theprojectguidelinesonappropriatewording,orassertsthatthe [14] AlbertQ.Jiang,AlexandreSablayrolles,ArthurMensch,ChrisBamford,DevendraSinghChaplot,DiegodelasCasas,FlorianBressand,GiannaLengyel,
prompt does not allow for injection into a non-data section of
GuillaumeLample,LucileSaulnier,LélioRenardLavaud,Marie-AnneLachaux,
theprompt[12].Perhapsassertingthatallpromptsincludethe PierreStock,TevenLeScao,ThibautLavril,ThomasWang,TimothéeLacroix,
properpersonawithinarepositorywouldbeahelpfultestforsome andWilliamElSayed.2023.Mistral7B. arXiv:2310.06825[cs.CL]
[15] ZhengbaoJiang,FrankF.Xu,JunAraki,andGrahamNeubig.2020.HowCan
developers.Withunittesting,thepowerliesintheflexibilityto

### WeKnowWhatLanguageModelsKnow? arXiv:1911.12543[cs.CL]

tailorthetesttoeachindividualtaskandprompt. [16] ArmandJoulin,EdouardGrave,PiotrBojanowski,MatthijsDouze,HérveJégou,
ThegoalforPromptSetistoputforwardatooltoparseprompts andTomasMikolov.2016.FastText.zip:Compressingtextclassificationmodels.
arXivpreprintarXiv:1612.03651(2016).
from files so that downstream applications can easily perform [17] ArmandJoulin,EdouardGrave,PiotrBojanowski,andTomasMikolov.2016.Bag
properpromptmanagement.Wehopetoestablishaconversation ofTricksforEfficientTextClassification.arXivpreprintarXiv:1607.01759(2016).
[18] YaoLu,MaxBartolo,AlastairMoore,SebastianRiedel,andPontusStenetorp.
aboutappropriateprompthygienesothattheopensourcecommu-

## FantasticallyOrderedPromptsandWheretoFindThem:Overcoming

nitycandevelopstrongtoolingforimprovingtheCI/CDpipeline Few-ShotPromptOrderSensitivity. arXiv:2104.08786[cs.CL]
forprompts.Inthisworkweproposeafewsurfacelevellintpasses, [19] Rajasekhar Reddy Mekala, Yasaman Razeghi, and Sameer Singh. 2023.
EchoPrompt:InstructingtheModeltoRephraseQueriesforImprovedIn-context
suchastypodetection,whitespacetrimmingandtypeannotation

### Learning. arXiv:2309.10687[cs.CL]

matching,howeverthepossibilitiesgofarbeyondthesesimple [20] SewonMin,XinxiLyu,AriHoltzman,MikelArtetxe,MikeLewis,Hannaneh
tests. Hajishirzi,andLukeZettlemoyer.2022.RethinkingtheRoleofDemonstrations:

<!-- Page 8 -->

LLM4Code’24,April20,2024,Lisbon,Portugal Pister,etal.
WhatMakesIn-ContextLearningWork? arXiv:2202.12837[cs.CL] Vol.30.CurranAssociates,Inc. https://proceedings.neurips.cc/paper_files/paper/
[21] OpenAI.2023.GPT-4TechnicalReport. arXiv:2303.08774[cs.CL] 2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf
[22] MaryPhuongandMarcusHutter.2022.FormalAlgorithmsforTransformers. [32] JasonWei,XuezhiWang,DaleSchuurmans,MaartenBosma,BrianIchter,FeiXia,
arXiv:2207.09238[cs.LG] EdChi,QuocLe,andDennyZhou.2023.Chain-of-ThoughtPromptingElicits
[23] NilsReimersandIrynaGurevych.2019.Sentence-BERT:SentenceEmbeddings ReasoninginLargeLanguageModels. arXiv:2201.11903[cs.CL]
usingSiameseBERT-Networks.CoRRabs/1908.10084(2019).arXiv:1908.10084 [33] JulesWhite,QuchenFu,SamHays,MichaelSandborn,CarlosOlea,Henry
http://arxiv.org/abs/1908.10084 Gilbert,AshrafElnashar,JesseSpencer-Smith,andDouglasC.Schmidt.2023.
[24] LariaReynoldsandKyleMcDonell.2021.PromptProgrammingforLargeLan- APromptPatternCatalogtoEnhancePromptEngineeringwithChatGPT.
guageModels:BeyondtheFew-ShotParadigm. arXiv:2102.07350[cs.CL] arXiv:2302.11382[cs.SE]
[25] SquidgyAI.2023.SquidgyTesty. https://github.com/squidgyai/squidgy-testy [34] TaoXiao,ChristophTreude,HideakiHata,andKenichiMatsumoto.2024.De-
[26] RobinStaab,MarkVero,MislavBalunović,andMartinVechev.2023. Beyond vGPT:StudyingDeveloper-ChatGPTConversations.InProceedingsoftheInter-
Memorization:ViolatingPrivacyViaInferencewithLargeLanguageModels. nationalConferenceonMiningSoftwareRepositories(MSR2024).
arXiv:2310.07298[cs.AI] [35] ChengrunYang,XuezhiWang,YifengLu,HanxiaoLiu,QuocV.Le,Denny
[27] RohanTaori,IshaanGulrajani,TianyiZhang,YannDubois,XuechenLi,Carlos Zhou, and Xinyun Chen. 2023. Large Language Models as Optimizers.
Guestrin,PercyLiang,andTatsunoriB.Hashimoto.2023.StanfordAlpaca:An arXiv:2309.03409[cs.LG]
Instruction-followingLLaMAmodel. https://github.com/tatsu-lab/stanford_ [36] SeonghyeonYe,HyeonbinHwang,SoheeYang,HyeonguYun,YireunKim,and
alpaca. MinjoonSeo.2023.In-ContextInstructionLearning. arXiv:arXiv:2302.14691
[28] HugoTouvron,LouisMartin,KevinStone,PeterAlbert,AmjadAlmahairi,Yas- [37] TonyZ.Zhao,EricWallace,ShiFeng,DanKlein,andSameerSingh.2021.
mineBabaei,NikolayBashlykov,SoumyaBatra,PrajjwalBhargava,ShrutiBhos- CalibrateBeforeUse:ImprovingFew-ShotPerformanceofLanguageModels.
ale,DanBikel,LukasBlecher,CristianCantonFerrer,MoyaChen,GuillemCucu- arXiv:2102.09690[cs.CL]
rull,DavidEsiobu,JudeFernandes,JeremyFu,WenyinFu,BrianFuller,Cynthia [38] YongchaoZhou,AndreiIoanMuresanu,ZiwenHan,KeiranPaster,SilviuPitis,
Gao,VedanujGoswami,NamanGoyal,AnthonyHartshorn,SagharHosseini, HarrisChan,andJimmyBa.2022.LargeLanguageModelsAreHuman-Level
RuiHou,HakanInan,MarcinKardas,ViktorKerkez,MadianKhabsa,Isabel PromptEngineers.(2022).arXiv:2211.01910[cs.LG]
Kloumann,ArtemKorenev,PunitSinghKoura,Marie-AnneLachaux,Thibaut
Lavril,JenyaLee,DianaLiskovich,YinghaiLu,YuningMao,XavierMartinet,
TodorMihaylov,PushkarMishra,IgorMolybog,YixinNie,AndrewPoulton, A GITHUBSCRAPINGCODE
JeremyReizenstein,RashiRungta,KalyanSaladi,AlanSchelten,RuanSilva,
EricMichaelSmith,RanjanSubramanian,XiaoqingEllenTan,BinhTang,Ross 1 for lib in ["openai",
Taylor,AdinaWilliams,JianXiangKuan,PuxinXu,ZhengYan,IliyanZarov, 2 "anthropic",
YuchenZhang,AngelaFan,MelanieKambadur,SharanNarang,AurelienRo- 3 "cohere",
driguez,RobertStojnic,SergeyEdunov,andThomasScialom.2023. Llama2: 4 "langchain"]:
OpenFoundationandFine-TunedChatModels. arXiv:2307.09288[cs.CL] 5 goto(f"https://github.com/search?" +
[29] Traceloop. 2023. OpenTelemetry. https://www.traceloop.com/blog/diy-
6 "q=%22from+{lib}%22+OR+" +
observability-for-llm-with-opentelemetry
[30] treesitter.[n.d.].Tree-sitter. https://tree-sitter.github.io/tree-sitter 7 "%22import+{lib}%22+" +
[31] AshishVaswani,NoamShazeer,NikiParmar,JakobUszkoreit,LlionJones, 8 "language%3Apython&type=code")
AidanNGomez,ŁukaszKaiser,andIlliaPolosukhin.2017. AttentionisAll
youNeed.InAdvancesinNeuralInformationProcessingSystems,I.Guyon,U.Von Received25January2024
Luxburg,S.Bengio,H.Wallach,R.Fergus,S.Vishwanathan,andR.Garnett(Eds.),