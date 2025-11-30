---
title: "From Prompts to Templates"
original_file: "./From_Prompts_to_Templates.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["prompt-engineering", "llm", "rag", "chain-of-thought", "agents"]
keywords: ["https", "prompt", "com", "analysis", "templates", "github", "page", "output", "json", "text"]
summary: "<!-- Page 1 -->

From Prompts to Templates: A Systematic Prompt Template

### Analysis for Real-world LLMapps


### YuetianMao JunjieHe ChunyangChen∗

TechnicalUniversityofMunich TechnicalUniversityofMunich TechnicalUniversityofMunich

### Germany Germany Germany

yuetian.mao@tum.de junjie.he@tum.de chun-yang.chen@tum.de
ABSTRACT users,craftingclearandeffectivepromptsremainsanon-trivial
LargeLanguageModels(LLMs)haverevolutionizedhuman-AIin- challenge[16,75].Thisdifficultyarisesfromthelimitedunde"
related_documents: []
---

# From Prompts to Templates

<!-- Page 1 -->

From Prompts to Templates: A Systematic Prompt Template

### Analysis for Real-world LLMapps


### YuetianMao JunjieHe ChunyangChen∗

TechnicalUniversityofMunich TechnicalUniversityofMunich TechnicalUniversityofMunich

### Germany Germany Germany

yuetian.mao@tum.de junjie.he@tum.de chun-yang.chen@tum.de
ABSTRACT users,craftingclearandeffectivepromptsremainsanon-trivial
LargeLanguageModels(LLMs)haverevolutionizedhuman-AIin- challenge[16,75].Thisdifficultyarisesfromthelimitedunderteractionbyenablingintuitivetaskexecutionthroughnaturallan- standingofhowLLMsprocessinputinformationandthefactthat
guageprompts.Despitetheirpotential,designingeffectiveprompts evenminorvariationsinpromptscanleadtosubstantialchanges
remainsasignificantchallenge,assmallvariationsinstructureor inmodelperformance[58,61].
wordingcanresultinsubstantialdifferencesinoutput.Toaddress Toaddressthesechallenges,numerousLLMapps,whichreferto
thesechallenges,LLM-poweredapplications(LLMapps)relyon thetypeofsoftwarethatusesLLMsasoneofitsbuildingblocks,
prompttemplatestosimplifyinteractions,enhanceusability,and havebeendeveloped[27,72]indifferentdownstreamdomains.The
supportspecializedtaskssuchasdocumentanalysis,creativecon- growthofLLMappshasbeenremarkable,withoveronemillion
tentgeneration,andcodesynthesis.However,currentpractices applicationsreleasedforpublicuseandleadingLLMappsnowboast
heavilydependonindividualexpertiseanditerativetrial-and-error morethanthreemillionmonthlyactiveusers[76].Forexample,
processes,underscoringtheneedforsystematicmethodstoopti- “WriteForMe”isoneofthemostpopularLLMappsintheGPTstore,
mizeprompttemplatedesigninLLMapps.Thispaperpresentsa withover12millionconversionsandahighratingof4.3basedon
comprehensiveanalysisofprompttemplatesinpracticalLLMapps. over10,000reviews[52].Unliketraditionalsoftwaredevelopment
Weconstructadatasetofreal-worldtemplatesfromopen-source thatinvolvesfull-stackimplementation,LLMappsadoptalow-code
LLMapps,includingthosefromleadingcompanieslikeUberand paradigmwhereLLMshandlemostuser’squeries,anddevelopers
Microsoft.ThroughacombinationofLLM-drivenanalysisandhu- focusonfacilitatinguser-LLMinteractionbydesigninglightweight
manreview,wecategorizetemplatecomponentsandplaceholders, prompttemplateswhichisapredefinedstructurethatcombines
analyzetheirdistributions,andidentifyfrequentco-occurrencepat- statictextwithdynamicplaceholders,allowingdeveloperstocreate
terns.Additionally,weevaluatetheimpactofidentifiedpatternson adaptable prompts for LLMapps [19]. These predefined prompt
LLMs’instruction-followingperformancethroughsampletesting. templatessimplifyandstandardizeuserinteractionswithLLMs[20,
Ourfindingsprovidepracticalinsightsonprompttemplatedesign 60],ensuringconsistencyandefficiencyacrossvarioustasks.
fordevelopers,supportingthebroaderadoptionandoptimization Figure1presentsexamplesofprompttemplatesdesignedforvarofLLMappsinindustrialsettings. ioustasks,showcasingtheircomponentsandplaceholders.Forexample,thefirsttemplateestablishesthemodel’srole,providestaskspecificdirectives(e.g.,songsuggestion),imposesconstraintsto

## Ccsconcepts

reducemodelhallucination,anddefinestheexpectedoutputformat
•Softwareanditsengineering→SoftwaredesignengineertobeaJSONstringwithspecificattributes.The{user_requirement}
ing;•Computingmethodologies→Artificialintelligence.
placeholderallowsfordiverseuserinputs,suchas“lightmusic
forbedtime”or“asongwithasummerfeeldescribing...lifein

## Keywords

...”Theothertwotemplatesdemonstratetheuseofexamplesand

### PromptEngineering,PatternAnalysis,LargeLanguageModels

detailedworkflowdescriptions,employingin-contextlearningand
chain-of-thoughttechniquestoguidetheLLMseffectively.Serv-
1 INTRODUCTION ingascriticalartifactsinLLMapps,prompttemplatesreducethe
LargeLanguageModels(LLMs),suchasGPT-4[1]andLLaMA[63], complexityofcraftingeffectiveprompts,bridgingthegapbetween
haveexhibitedexceptionalcapabilitiesincomprehendingandgen- userintentandmachineresponses.SimilartoGUI(GraphicalUser
eratingtext,andLLMshaverapidlyevolvedtobecomeacorner- Interface)whichbridgesthegapbetweenbackendprogramsand
stoneofmanyAI-drivenapplications.Thisversatilityhasintro- end-users,prompttemplatesarelikea“textualGUI”forAIsystems,
duced a new paradigm of interaction between humans and AI, whereinputsfollowastructuredformatrequiringonlybasicinputs,
whereusersexpresstheirinstructionsinnaturallanguage,and suchasafewclicksorfillingintheblank,insteadoflongcomplete
theLLMgeneratesoutputsthatalignwiththesespecifications.At instructioninput.JustasGUIshavewidgetsthatcanbereusedor
firstglance,apromptmayappeartobeasimplequestionorre- customized,prompttemplateshavecomponentsandplaceholders
quest,butitactuallyservesasabridgebetweenhumanintentand thatallowflexibilityanddynamicusagewhichhidetheintricateopmachine-generatedresponses,guidingthemodelbyprovidingcon- erationsofthebackendfromtheuser.Fromsettingthecontextand
text,shapingoutputs,andinfluencingbehavior.Whilethesemodels defininginstructionstodynamicallyadjustingthecontentbasedon
havesignificantlyreducedthebarrierstoAIadoptionforgeneral userneeds,prompttemplatesofferaversatileapproachtolanguage
modelinteractions.Byprovidingaconsistentstructure,prompt
∗ChunyangChenisthecorrespondingauthor.
5202
rpA
7
]ES.sc[
2v25020.4052:viXra

<!-- Page 2 -->


### Anonymousauthors


### Figure1:Examplesofprompttemplate[23,36,56]

templateshelpusersarticulatetheirrequirementsmoreeffectively, Data Collection Prompt Template Analysis Prompt Template Testing
ensuringthattheLLMunderstandsandrespondsappropriately
eveninspecializeddomains,suchasdocumentanalysis[65],cre- { x }
Representative LLM for Analysis Component Statistical Analysis LLM for Testing LLM Output
ativecontentgeneration[9],andcodesynthesis[22]. Prompt Templates AnalysisResult Result
AsanewparadigmtodevelopLLMapps almostallcommercialLLMproviderssupportprompttemplates,suchasOpenAI’s {𝒙}
GPT series [49], Google’s Gemini [19], Anthropic’s Claude [3], Prompt Predefined Placeholder Pattern Analysis Sample Human Evaluation

### Data Categories Analysis Result Result Test Data Result


### Salesforce[57],andLangchain[39].Unliketraditionalsoftware

development, which is deterministic and relies on well-defined

### Figure2:Anillustrationofthemainpipeline

code[24,41,74],LLMappsintroducevariabilityinoutputs,challengingsoftwareengineerstodesignpromptsthatensurereliabil- • Wecategorizekeycomponents,placeholders,andpatterns
ity,maintainability,andperformance.However,itisstillunclear fromcollectedlarge-scaleprompttemplates,offeringinsights
howtodevelophigh-qualityprompttemplateswhicharenoteven intoeffectiveprompttemplatedesignpractices.
clearlymentionedinthedocumentationfromtheseleadingcom- • Throughsampletesting,wedemonstratethatwell-structured
mercialLLMproviders.Whatinformationshoulddevelopersput prompttemplatesandspecificcompositionpatternscansigintoprompttemplates?Whatpatternsdotheyfollow?Whatdy- nificantlyimproveLLMs’instruction-followingabilities.
namiccontentwillprompttemplatestakefromendusers?Howdo
differentconstructionpatternsinprompttemplatesinfluenceLLMs’ 2 METHODOLOGY
instruction-followingabilities?Consideringthegrowingsignifi-
2.1 Overview
canceofprompttemplatesintheLLMappecosystem,asystematic

### Figure2showsthemainframeworkofourmethodincludingthree

understandingoftheirstructure,composition,andeffectivenessis
mainsteps:theconstructionoflarge-scaleprompttemplatesfrom
urgentlyneeded.
real-worldGitHubrepositories,anempiricalstudyofprompttem-

### Inthispaper,weanalyzeprompttemplatesusedinLLM-powered

platesfocusingoncomponents,placeholders,patterns,andanexapplications,focusingontheircomponents,placeholders,andcomploratorystudytochecktheeffectsoftheseprompttemplatepatpositionpatterns.Ourstudyutilizesapubliclyavailabledataset
ternstoLLMoutput.
ofpromptscollectedfromopen-sourceLLMapps[51],encompassingapplicationsfromITgiantstoinnovativestartupsthatreflect
2.2 DataCollection
real-worldusecasesandindustrytrends,suchastoolsfromUber
(adoptedbyover200developers)[35,54]andMicrosoft(over5k WeconstructourdatasetbasedonPromptSet[51],acollectionof
GitHubstars)[53].Wepre-processthedatasettofilterrepresenta- promptsextractedfromLLMappsinopen-sourceGitHubprojectsas
tiveprompttemplatesandsystematicallyidentifytheircomponents ofJanuary10,2024.Theseprojectsvarywidelyincomplexity,usage,
andplaceholders.Byanalyzingthecontentandorderoftheseel- andpopularity,rangingfrompersonaldemostowidelyadopted
ements, we uncover structural and content patterns commonly applications,resultinginsignificantvariabilityinpromptquality.
employedinprompttemplatedesign.Toevaluatethesepatterns, Toensureahigh-qualitydatasetsuitableforindustrialapplications,
weconductsampletestingusingrandomlyselectedtemplates,as- wedesignaprocessingpipelinethatassignsqualitymetricstoeach
sessingtheirimpactonLLMinstruction-followingabilitiesand promptandautomaticallyfiltersoutlower-qualityexamples.
identifyingoptimalpatternsforenhancedperformance. Ourdatacollectionpipelinebeginsbyselectingnon-emptyEng-
Ourcontributionsaresummarizedasfollows: lishpromptsfromthePromptSetdataset,resultingin14,834records.
• Tothebestofourknowledge,thisisthefirststudyanalyzing ForeachcorrespondingGitHubrepository,weretrievemetadata
real-worldprompttemplatesinLLMapps,withdatasetspub- suchasstarcount andlatestupdatetime toevaluaterepository
liclyavailableat:https://github.com/RedSmallPanda/FSE2025. popularityandactivity[11,69],utilizingtheGitHubAPI,accessed
onJune20,2024.Wefilterrepositorieswithatleastfivestarsand
recentupdateswithinthepastyear,narrowingthedatasetto2,888

<!-- Page 3 -->

FromPromptstoTemplates:ASystematicPromptTemplateAnalysisforReal-worldLLMapps
Table1:RepresentativeLLMapprepositories[35,38,53,68] consolidatedintoasinglecomponentlabeled“Profile/Role.”The
mergedcomponentlistispresentedinTable2,andcomponent
CompanyName RepoTitle Description #Stars definitionsandfrequencydistributionsaredetailedinTable3.
Uber uber/piranha ToolforrefactoringcoderelatedtofeatureflagAPIs 2.3k
Microsoft microsoft/TaskWeaver Code-firstagentframeworkfordataanalytics 5.4k
Weaviate weaviate/Verba RAGchatbot 6.5k Table2:Promptcomponentsacrossdifferentframeworks
LAION LAION-AI/Open-Assistant Chat-basedassistant 37.1k
# Starsassessedon30.12.2024. anddocumentations.
LangGPT[64] ElavisSaravia[59] CRISPE[47] GoogleCloud[10] Merged
recordsacross1,525repositories.Next,weseparatemulti-prompt

### Profile - CapacityandRole Persona Profile/Role

recordsintoindividualentries,resultingin5,816prompts,andthen Objective
removeduplicatestoobtain4,540uniqueprompts.Tofurtheren- Goal Instruction Statement Instructions Directive

### SystemInstructions

hancedataquality,weexcludepromptsshorterthanfivetokens[25], Workflow - - ReasoningSteps Workflow
with4,210high-qualitypromptsleft.Finally,weextract2,163dis- B In a i c ti k a g li r z o a u t n io d n Context Insights Context Context
tinctprompttemplatesusingthellama3-70b-8192model,guided

### Example InputData - Few-shotExamples Examples

byacleardefinitionfromSchulhoffetal.[60],supplementedby Output-format ResponseFormat
illustrativeexamples.MostrepositoriesinourdatasetareLLMapps Style OutputIndicator Personality Tone OutputFormat/Style

### Constraints

servingforinformationseeking,editing,coding,andcreativewrit- Constraints - - Safeguards Constraints
ing.AsseeninTable1,someofthemarefromleadingcompanies Skill

### Suggestion - Experiment Recap Others

andorganizations,suchasUber’stoolforrefactoringcoderelated
tofeatureflagAPIs(adoptedbyover200developers[35,54]),Mi-

### Weleveragethellama3-70b-8192modeltoidentifycomponents

crosoft’scode-firstagentframeworkforexecutingdataanalytics
fromthemergedlistpresentintheprompts,employingapredefined
taskswithover5kGitHubstars[53]andsomeverypopularones,
prompttemplatethatspecifiesallavailablecomponentsandoutputs
suchasanRAGchatbotpoweredbyWeaviatewithover6kGitHub
resultsinastructuredJSONformat.
stars[68],andLAION-AI’sOpen-Assistantprogram,withmore
Toassesstheaccuracyofcomponentidentification,weperform
than37kstars[38].
bothcomponent-levelandprompt-levelhumanevaluationsona
randomlyselected5%sampleofprompts.Atthecomponentlevel,
2.3 PromptTemplateAnalysis
precisioniscalculatedastheproportionofcorrectlyidentifiedcom-
Inthissection,weaddressthefollowingresearchquestions:
ponentscomparedtohuman-labeledones.Atthepromptlevel,a
• RQ1:Whatarethecommonconstituentcomponentsin promptisclassifiedasanexactmatchonlyifallidentifiedcompoprompttemplates,andwhatspecificwords,phrases,and nentsarecorrect;promptswithatleastonecorrectcomponentare
patternsarefrequentlyusedwithinthesecomponents? classifiedaspartialmatches[33].
Weinvestigatethecomponentcompositionofrepresentative Humanevaluationsfollowestablishedpractices[40],withtwo
promptsextractedfromLLMappsandanalyzeco-occurrence evaluatorsbothwithoveroneyearofprogrammingexperiencein
patternsamongcomponents.Buildingonthesefindings,we LLMappindependentlyreviewingLLM-generatedclassifications.
conductword-levelandphrase-levelanalysisofeachcomponent Acomponentisconsideredcorrectlyidentifiedifbothevaluators
typetouncovervariationsinhowsimilarcontentisexpressed agree.Placeholderidentificationaccuracyisvalidatedinthesame
(e.g.,differentwaysusersdescribetheoutputformatas“JSON”). manner.Forprompttemplatetesting,evaluatorsscoreLLMoutputs
Fromthesevariations,weidentifycommonpatternsthatimpact basedonpredefinedmetrics,withthefinalscorebeingtheaverage
responseformatandcontent. oftheirassessments.
• RQ2: How do placeholders vary in terms of types and Theevaluationresultsindicatehighcomponent-levelprecision,
positionswithinprompttemplates? averaging86%acrossallpredefinedtypes.Atthepromptlevel,full
Weanalyzethetypesofplaceholders(variablesthatwillbere- matchprecisionis66%,whilepartialmatchprecisionreaches99%,
placedbyinputtexttocreateacompleteprompt)withinprompt demonstratingthemethod’sreliabilityincomponentdetection.
templates[60],categorizingthembasedontheirvariablenames
andcontextualusagewithinthetemplates.Thenweexaminethe 2.3.2 PlaceholderAnalysis.

### Weanalyzeplaceholderswithinprompttemplatesusingatwo-step

positionaldistributionofplaceholdersacrossprompttemplates.
iterativeprocess.First,wemanuallyclassifyplaceholdersfroma
2.3.1 PromptComponentAnalysis. randomlyselectedsetof100templatesintopredefinedornewly
Inthisstep,wedefineacomprehensivesetofcommonprompt identifiedcategoriesbasedontheirnames,followingpracticessimcomponentsbysynthesizinginsightsfromprominentprompten- ilartovariableanalysis[5].Then,weusegpt-4otoextendthis
gineeringframeworksandAIserviceplatforms.Specifically,we classificationtothefulldataset,leveragingtheinitialcategories
extractcomponentdefinitionsfromguidelinesprovidedbyGoogle anddefinitions.
Cloud’sdocumentation[10],theElavisSaraviaframework[59], Toensureaccuracy,weconducthumanevaluationstoverify
theCRISPEframework[47],andtheLangGPTframework[64].To theLLM’sclassifications,mergingunderrepresentedcategoriesand
constructaunifiedlist,wemergesimilarcomponentsacrossthese refiningdefinitionsasneeded.Afterincorporatingtheseadjustsources.Forinstance,componentslikeProfile,Capacity,Role,and ments,weperformasecondroundofLLMclassification,followed
Persona,allofwhichdefinethemodel’sbehaviororidentity,are byanotherhumanevaluation.Thisiterativeprocessachievesan

<!-- Page 4 -->


### Anonymousauthors

overallclassificationaccuracyof81%onarandomlyselectedsam- YouareanAIassistantactingasacontentadvisorforatechblog.Suggesttwo Profile/Role
pleof80records.Ultimately,weidentifyfourprimaryplaceholder relevantblogtopicsbasedonrecenttrendsin{subject_area}. Directive

### Youaregiventhefollowinginformation: Context

categories,asdetailedinTable5. -Theblogfocusesontopicsrelatedto{subject_area}.
-Recentpostson{high_engagement_topics}havereceivedhighengagement.
2.3.3 StatisticalAnalysisandPatternAnalysis. Tocompletethistask,followthesesteps: Workflows

### Reviewtheprovidedcontextandanalyzecurrenttrendsin{subject_area}.

Using the component analysis and placeholder analysis results, 2.Suggesttwoblogtopicsthatalignwiththeblog’sfocusandaudience.
we conduct a statistical analysis to examine the distribution of 3.Ensurethesuggestedtopicsarerelevanttotherecentengagementtrends,
particularly{high_engagement_topics},andareaccessibletoageneralaudieachcategory,aswellasthefrequencyandrelativepositioning ence.
ofelementsatthewordandphraselevels.Fromthesestatistical Avoidoverlytechnicalornichetopicsthatmayoverwhelmreaders.Keep Constraints
topicsbroadandengagingfornon-experts.
findings, we extract notable patterns that reveal structural and
Provideyourresponseinthefollowingformat: Output Forcontenttrendswithintheprompttemplates. Topic1:[Title]-[One-sentenceexplanation] mat/Style

### Topic2:[Title]-[One-sentenceexplanation]


### TherearetwoexampletopicsbasedontrendsinAI: Examples

2.4 EffectsofPromptTemplatePatterns Topic1:AIinPublicServices-DiscusshowAIisbeingusedtoenhance
efficiencyinpublicserviceslikehealthcareandeducation.
Inthissection,weaddressthefollowingresearchquestion: Topic2:EthicalAIinAutomation-ExploretheethicalimplicationsofAI-
drivenautomationinindustrieslikemanufacturingandlogistics.
• RQ3:Howdodifferentconstructionpatternsinprompt
templatesinfluenceLLMs’instruction-followingabilities?
Wesampleprompttemplateswithspecificpatternsidentifiedin Figure3:ATemplateExamplefollowingGeneralComponent
earlierresearchquestions,populatethemwithsampledata,and Order.
generateoutputstoassesstheeffectivenessofthesepatternson

### Table3:Frequenciesdistributionofdifferentpromptcompo-

LLMs’instruction-followingabilitiesthroughhumanevaluation.
nents.
Inthisphase,weassesstheimpactofvariouspatternsidentified
intheanalysisofRQ1andRQ2onLLMoutput,focusingontwokey

### Components Definition Frequency

dimensions:Content-Following,whichensuressemanticaccuracy

### Profile/Role Whoorwhatthemodelisactingas. 28.4%

withtaskgoals,andFormat-Following,whichenforcesadherence

### Directive Thecoreintentoftheprompt,oftenintheform 86.7%

tostructuralorsyntacticalrequirementscriticalforLLMappsbut ofaninstructionoraquestion.
underexploredinpriorresearch[70].Specificmetricsaredefined Workflow Stepsandprocessesthemodelshouldfollowto 27.5%
completethetask.
foreachtesttoevaluateoneorbothdimensions.

### Context Backgroundinformationandcontextthatthe 56.2%

Foreachpattern,werandomlysampleprompttemplatesthat modelneedstoreferto.
incorporateitandpopulatethemusingeitherthegpt-4omodel Examples Examplesofwhattheresponseshouldlooklike. 19.9%
OutputFormat/Style Thetype,format,orstyleoftheoutput. 39.7%
orreal-worlddatasources,suchasamedicalQAdataset[6],Java

### Constraints Restrictionsonwhatthemodelmustadhereto 35.7%

documentation[50],andGitHubprojects[37].Tocomparepatterns whengeneratingaresponse.
addressingsimilarissues,wemanuallyreformulatethetemplates
(e.g., modifying the output format or adding constraints) to fit
alternativepatterns.Outputsarethengeneratedusingbothllama3-
70b-8192andgpt-4omodels,followedbyhumanevaluationsto
assessoutputqualityagainstpredefinedmetrics.

## 3 Analysisresults

3.1 RQ1:AnalyzingComponentsinPrompt

### Templates

3.1.1 DistributionofComponents.
Table3showsthedetectionresultsforthesevencategoriesofcomponents,indicatingthepercentageofprompttemplatescontaining
eachcomponent.Amongthesecomponents,thefourmostcommonareDirective,Context,OutputFormat/Style,andConstraints.
TheDirectiverepresentsthetaskintentoftheprompt,guidingthe
languagemodelonhowtoperformatask.Mostpromptsrequirea
clearandcompletedirectivetoinstructthemodeleffectively.The
Contexttypicallyincludestheinputcontentandrelevantcontex- Figure4:Componentorderprobabilitymatrix
tualdescriptions,helpingthemodelunderstandthetaskindetail.
GiventhattheseprompttemplatesaredesignedforLLMapps,de- 3.1.2 ComponentOrder.
velopersoftenspecifyanOutputFormat/Style(e.g.,Topic:Title Wealsoinvestigatetherelativepositionsofvariouscomponents.
-Explanation,asillustratedinFigure3)andsetConstraints(e.g., WeobservethattheProfile/RoleandDirectivecomponentscomlength,numberofresults,outputtopicscope).Thisensuresthe monlyappearinthefirstpositionratherthanotherpositions,with
generatedcontentismorepredictableandeasierfordownstream aprobabilityof0.87and0.65,respectively.AsshowninFigure4,
applicationstoprocess,andmaintainsconsistencyacrossoutputs. boththeXandYaxesrepresentthedifferentcomponenttypes,

<!-- Page 5 -->

FromPromptstoTemplates:ASystematicPromptTemplateAnalysisforReal-worldLLMapps
Profile/Role Directive ContextWorkflows Output Format/StyleConstraints Examples

### Figure5:ACommonComponentorder

(a)InformationSeeking. (b)Coding&Debugging. (c)Editing.
witheachcoordinatepointindicatingtheprobabilitythatcompo-

### Figure6:Wordcloudforoutputformatofselectedthemes

nentXfollowscomponentY.Thedarkerthecolor,thehigherthe
probabilitythatthispositionalpatternoccurs.Forexample,Context
ismostlikelytobefollowedbyDirectivewithaprobabilityof0.48. PLACEHOLDER
Json Output Which of these functions is most suitable given the user query: "PLACEHOLDER"?
Based on the analysis, we identify a common sequential or- Respond in JSON.
derofcomponentsinprompttemplates,asdepictedinFigure5. Consider the following text:
Thissequenceassumeseachcomponentappearsexactlyonce.No- ---

### Json Output PLACEHOLDER

tably,“ContextandWorkflows”and“OutputFormat/StyleandCon- + ---
Json Attribute Name Convert the text into a JSON that lists the projects and has the following keys for
straints”consistentlyformtwopairs,wheretheorderwithinthe each project:`project_name`, `twitter_handle`, `description`. Edit the `description`
field to 2-3 sentences.
“OutputFormat/StyleandConstraints”pairisflexible.Additionally,
therelativepositioningofthesetwopairscanalsobeinterchanged Text:

### Json Output {{$input}}

withoutimpactingoverallstructure.Figure3illustratesaspecific +
promptexamplethatadherestothisidentifiedorder. Jso J n s o A n tt A rib tt u ri t + b e u D te e s N c a r m ip e ti on A {" n P a h l r y a z s e e " th : e [ r a e b w o r v it e e T o e f x T t. e R xt e a s s p o a n n d e u ff s e i c n t g iv t e h i g s o J o S g O le N s e te a m rc p h l a p t h e r : ase], "Keywords":
[keywords in Text],"NamedEntities": [NamedEntitiesin text]}
Finding1: Therearemainlyseventypesofcommoncomponents within prompt templates according to our observation. Figure7:ThreedifferentJSONoutputformats[14,28,62]

### Developerscommonlyputtheprofile/roleandtheirdirectiveat

thebeginningoftheprompt,establishingthemodel’sidentity OutputFormat/Style.Weanalyzetheoutputformatsspecified
andtaskintent,whileexamplesaretypicallyattheend. intheprompttemplatesacrossdifferentthemes.Toextractthese
formats,weconsiderthemostfrequentlyoccurringtermsinthe
3.1.3 ComponentContent. outputdescriptionsoftheprompttemplatesandmaptheminto
Weperformanin-depthanalysisofspecificpromptcomponents
wordcloudsforeachtheme,asshowninFigure6.Wordsinthe
thathaveasignificantimpactonthestructureconsistencyand
cloudaresizedproportionallytotheirfrequency:thelargerthe
instructionrelevanceofLLMresponses,focusingoncommonly
word,themoreoftenthatoutputformatisusedwithinthetheme.
usedwords,phrases,andformatsassociatedwiththesecompo-
Fromouranalysis,certainformatslike“score”and“code”are
nents.Amongtheseventypesofpromptcomponents,wefocus
frequentlyusedinparticularthemes.Forexample,“code”isapreonthree:Directive,OutputFormat/StyleandConstraints.Indirect
dominantoutputformatinthe“Coding&Debugging”tasks,often
interactionswithLLMs(suchaslivechat),usersprimarilycare
appearingastheresultoftaskssuchascodegeneration,bugfixing,
abouttherelevanceandcorrectnessoftheresponse.However,in
andcodesummarization.Similarly,“score”appearsfrequentlyin

### LLMapps,developersarenotonlyconcernedwiththeresponse

“InformationSeeking”tasks,whereusersprovidecriteriaforLLMs
contentbutalsowithitsformat,aspost-processingoftenrelieson
toevaluateinputsandgeneratenumericalscores.
structuredoutputs.Ensuringalimitedorpredictableoutputformat
Acrossallthemes,themostcommonoutputformatbesidesstancansignificantlyreduceerrorsduringpost-processing.Basedon
dardtextisJSON.JSON’sstructurednaturemakesitparticularly
ourobservationsofhowLLMappshandleresponses,wefocusonDipopular,asitiseasyforapplicationstopost-processandprovides
rective,whichencapsulatesthecoreuserintent,alongwithOutput
auser-friendlywaytoorganizecomplexinformation.
Format/StyleandConstraints,astheyplayacriticalroleinshaping
To analyze how developers define JSON output formats, we
bothresponseformatandcontent—keyfactorsfordownstream
extract all prompt templates that specify JSON as the required
processingandapplicationperformance.
outputformat.Fromthedata,weidentifythreekeycomponents
Directive. Directiveinpromptscouldbeeitherinquestionor frequentlyused:JsonOutput,whichspecifiesthattheoutputmust
instructionstyle[32,60].Usingregexpatternstocapturedirectives
beinJSONformat;JsonAttributeName,whichdefinesthenamesof
startingwithquestionwordssuchas“how”and“what”orending
theattributestobeincluded;andJsonAttributeDescription,which
withaquestionmark“?”,weclassifythedirectiveintotwotypes,
providesdetailedexplanationsforeachattribute.Thesecomponamelyinstructionandquestion.Notably,ouranalysisshowsthat
nentscombineintothreedistinctpatterns.InPattern1,developers
over 90% of directives are written in the instruction style. This
onlyindicatethattheoutputshouldbeinJSONformat,oftenacislikelyduetothefactthatinstructionssuchas“Summarizethe
companiedbygeneralguidelinesinnaturallanguageaboutthe
report”aremoredirectandclearerforthemodeltounderstand
expectedcontent.Pattern2buildsonthisbyexplicitlylistingthe
thanquestion-styledirectiveslike“Couldyousummarizethis?”.
attributenamestobeincluded,ensuringstructuralconsistencyin
theoutput.Finally,Pattern3addsdetaileddescriptionsforeach
Finding2: Thedirectivecomponenti.e.,userintentinprompt attributetoPattern2,enhancingclarityandensuringattributesare
templatespredominantlyadoptsaninstructionalstyle,whichis
well-defined,particularlyforcomplexoutputs.Figure7illustrates
morecommonlyusedthanthequestionstyle.
thesepatternsandtheircomposition.

<!-- Page 6 -->


### Anonymousauthors

Thedistributionofthesepatternsacrossallobservedtemplates
revealsthatPattern1(JsonOutput)accountsfor36.21%,Pattern
2(JsonOutput+JsonAttributeName)for19.83%,andPattern3
(JsonOutput+JsonAttributeName+JsonAttributeDescription)
for43.97%.

### Finding3: JSONisthemostcommonlyusedoutputformatin

prompttemplates.Notably,overone-thirdoftheseJSONformats
relyoninformaldescriptionswithoutexplicitlydefinedattribute
names.

### Constraints.Weusethellama3-70b-8192modeltoidentifyvarious

constrainttypesinprompttemplates,basedontheclassifications Figure8:Frequencydistributionofplaceholderpositional
established by Ross Dawson [13]. The most common types are occurrencesfordifferentplaceholdertypes.
“Exclusion”(46.0%),“Inclusion”(35.6%),and“Wordcount”(10.5%).
Thesecategoriesreflecttheprimaryconsiderationsdevelopersemphasizewhendesigningprompttemplates.The“Inclusion”constraintsguidethemodeltofocusonspecificdetails,improvingthe
relevanceandprecisionofitsresponses.“Wordcount”constraints
encourageconciseresponses,enhancingusabilityandreducingAPI
costsbyminimizingtokenusage.

### Giventhat“Exclusion”constraintsaccountfornearlyhalfof

allidentifiedconstraints,weconductedadetailedanalysisofthis Figure 9: Examples of prompt templates with different
category. Usingthe all-mpnet-base-v2embedding model andk- KnowledgeInputpositions[34,45].
meansclustering,weidentifiedfivesubcategories:“Accuracyand

### Phrasesserveasbriefinputsprovidingessentialsettingsorspe-

Relevance”,“ClarityaboutUnknowns”,“OutputControl”,“Reduncificdetails,suchas“language”or“username.”Developerstendto
dancyandContextAdherence”,and“TechnicalRestriction”(TaincludemultipleMetadata/ShortPhraseswithinonetemplate.Adble 4). These subcategories reflect nuanced developer intent in
ditionally,theUserQuestionplaceholdercapturesthedirectquery
managingmodeloutputs.
fromtheenduser,whileContextualInformationplaceholderspro-
Keysubcategories,suchas“Accuracyandrelevance”and“Clarvidesupplementarybackgroundcontent,suchas“chathistory”or
ity about unknowns” are designed to mitigate hallucinations, a
“backgroundinfo,”offeringcontextthatsupportsthetaskwithout
prevalentissuewithLLMs.Forexample,promptslike“Don’ttry
beingcentraltoit.
tomakeupananswer”reducetheriskofspeculativeorincorrect
outputs,enhancingreliability.Anthropic’sdocumentation[4]and 3.2.2 PositionalDistributionofPlaceholder.
Chenetal.[8]proposesimilarconstraintstomitigatethehallu- Weanalyzethepositionaldistributionofplaceholderswithinprompt
cination.Additionally,constraintstargetingredundancy,suchas templates,dividingeachtemplateintothreesections—beginning,
“Donotgenerateredundantinformation”streamlineresponses,re- middle, and end—each representing one-third of the template’s
ducingpost-processingneedsintaskslikecodegeneration.The length.Figure8illustratesthisdistribution,inwhichapproximately
“Technicalrestriction”subcategoryhighlightsconstraintsforspe- 60%ofuserquestionsappearattheend,reflectingacommonstruccificcontexts,suchasdatabasequeriesorAPIcalls,ensuringthat turalpattern,whereas{KnowledgeInput}ismoreevenlydistributed
modelsadheretoprecisetechnicalrequirementslikepredefined betweenthebeginningandendpositions.Figure9presentsexamstructuresorrestrictedAPIusage.Theseconstraintsarecriticalfor pleswithvaried{KnowledgeInput}positions.Additionally,placemaintainingcorrectnessandefficiencyinstructuredworkflows. holdercontentlengthvariesconsiderably;longerknowledgeinputs
mayleadtoinformationlossinLLMsacrossextendedprompts.
Finding4: Developersfrequentlyuseexclusionsastheconstraintstorefineoutputssuchasexcludingirrelevantcontent, Finding5: Therearefourtypesofplaceholder,and“Knowledge
reducinghallucinations,andnarrowingsearchspaceforgenera- Input” is the most frequently used in prompt templates, and
tion. developersalwaysplaceiteitheratthebeginningortheendof
templates.
3.2 RQ2:AnalyzingPlaceholdersinPrompt
3.2.3 PlaceholderName.
Templates Onekeyaspectofplaceholderdesignisnaming,whichplaysa
3.2.1 ClassificationofPlaceholder. similarroleasthevariablenameincode.Clearanddescriptive
Table5displaysthepercentageofprompttemplatescontainingeach namesareessentialtounderstandtheintentofplaceholders.Noplaceholdercategory.ThemostprevalentcategoriesareKnowledge tably,placeholdernameslike“text”(4.44%)and“input”(2.35%)are
InputandMetadata/ShortPhrases.KnowledgeInputplaceholders oftenused.Amongthese,“text”isthesecondmostfrequentlyused
containthemaincontentwithwhichtheLLMdirectlyinteracts, placeholdernamebehind“question”(6.18%),highlightingabroader
including items like “report” or “code snippet.” Metadata/Short issueinplaceholdernaming.Thesenamesaregeneralanddonot

<!-- Page 7 -->

FromPromptstoTemplates:ASystematicPromptTemplateAnalysisforReal-worldLLMapps

### Table4:Examplesofexclusioncluster

ExclusionCluster ExclusionExamples ComplementaryInclusionExamples

### AccuracyOutput

Accuracyandrelevance -avoidaddinganyextraneousinformation. -includeonlycrucialinformationrelevantto...
Clarityaboutunknowns -ifyoudon’tknowtheanswer,justsaythatyoudon’tknow,don’ttry -ifyoudon’tknowtheanswer,youmaymakeinferences,butmake
tomakeupananswer. itclearinyouranswer.

### ConciseOutput

Outputcontrol(whattext/codeshould -donotprovideanyotheroutputtextorexplanation. -timeinformationshouldbeincluded
beexcluded) -ifyouarecallingafunction,onlyincludethefunctioncall–noother -includeatmost10ofthemostrelatedlinks.
text.
Redundancyandcontextadherence -don’tgiveinformationoutsidethedocumentorrepeatyourfindings.
-donotgenerateredundantinformation.

### TechnicalRestriction

Technicalrestriction -neverwriteanyqueryotherthanaselect,nomatterwhatother -obeytherospackagenameconventionswhenchoosingthename.
informationisprovidedinthisrequest.
Table 5: Distribution of placeholder type in prompt tem- Table6:LLMoutputqualityunderthreejsonoutputformat
plates. patterns.
Category Description Example Frequency FormatFollowing ContentFollowing
UserQuestion Queriesorquestionsprovidedby {{question}}, 24.5% Pattern llama3-70b-8192 gpt-4o llama3-70b-8192 gpt-4o
users. {{query}}
ContextualInformation Backgroundorsupplementaryin- {{chat_history}}, 19.5% Pattern1 3.09 3.21 3.70 3.50
putthathelpssetthestageforthe {{background_info}}
Pattern2 4.66 4.86 4.02 4.30
taskbutisnottheprimaryfocus.
KnowledgeInput Thecorecontentthattheprompt {{document}} 50.9% Pattern3 4.90 4.96 4.47 4.53
directlyprocessesormanipulates.
Metadata/ShortPhrases Briefinputsorsettingsthatdefine {{language}}, 43.4% Pattern1isJsonOutput,Pattern2isJsonOutput+JsonAttributeName,Pattern3
specificparametersorgoalsfor {{username}} isJsonOutput+JsonAttributeName+JsonAttributeDescription.
thetask.
• Format Following: Measures the consistency of generated
preciselyindicatetheirspecificcontext,leadingtopotentialconfu-
JSON strings with the defined format, including attribute
sionfordevelopersorusers.Forexample,“text”couldrefertoany
count,names,andstructuraluniformityacrossoutputs.
kindofinputtext,sodevelopersanduserscannotdirectlyunder-
• ContentFollowing:Assessesthealignmentofgeneratedconstandwhattheyneedtoinputthroughitsname.Inthiscase,more
tentwiththeintentintheprompttemplate.
descriptiveplaceholdernamesaresuggestedsothatdevelopers
anduserscaneasilyunderstandwhattheyneedtoinputwithout AsshowninTable6,bothmodelsexhibitsimilartrends,with
consideringthewholeprompttemplatecontext. Pattern3achievingthehighestscoresacrossmetricsandmodels.

### InFormat-Following,Patterns2and3outperformPattern1,which

Finding 6: Similar to the variable naming convention, non- scoreslowerduetoinconsistenciesinattributecountandnaming,
semanticplaceholdernamessuchas“text”and“input”arestill stemmingfromitslackofexplicitdefinitions.Patterns2and3miticommonlyusedinprompttemplates,hinderingpromptunder- gatetheseissuesthroughexplicit“JsonAttributeNames”,ensuring
standingandmaintenance. greaterstructuralconsistency.

### ForContent-Following,Pattern3achievesthehighestscores,

with llama3-70b-8192 at 4.47 (+0.45) and gpt-4o at 4.53 (+0.23),
3.3 RQ3:EvaluatingPatternsthroughSample
suggestingthatdetailed“JsonAttributeDescriptions”enhancethe
Testing model’sabilitytogeneratecontentthatalignscloselywithuser
3.3.1 JsonOutputFormat. requirements.Thesefindingsunderscorethevalueofattribute-level
ToinvestigatetheeffectofdifferentJSONoutputpatterns,we detailinimprovingbothprecisionandsemanticadherence.
testthreeidentifiedpatternsdisplayedinFigure7.Fiverepresenta- Figure10illustratesanexampleofextractingtweetinformation
tivetemplatestargetingdifferenttasks(e.g.,tweetanalysis,DNS usingthreeprompttemplateswithidenticalinputtextbutdifferparsing)areselectedforeachpatternandthreediverseinputin- ingJSONoutputformats.Case1broadlyrequestsaJSONoutput
stancesaregeneratedpertemplate,yieldingatotalof45templates withoutdefiningrequiredfields,leadingtoredundantoutputslike
afterreformattingthemtofitallpatterns.Wedefinetwometrics “text”,“mentions”,and“hashtags”.Case2specifiesfieldnameslike
ratedfrom1to5toevaluatetheJSONobjectinLLMoutput[31,70]: “tweet_id”and“engagement”,producingmorestructuredoutputs,

<!-- Page 8 -->


### Anonymousauthors

Pattern 1 Pattern 2 Pattern 3 Finding8: UsingonlyJSONformatdefinitionsisinsufficientto
I n n e p w u s t t f w or e e ca t: r @ en e t v h u u p s d ia a s t t e s s a : n M d a T jo e r s la I c n a p r u e t n t t w h e u e s t i : a s @ ts e a vu n p d d T a e t s e l s a : f M an a s jo ! r · · n · e ·· w · s for I e n n p t u h t u s tw ia e s e ts t: a @ nd e v T u e p s d la a t f e a s n : s M ! · a ·· jo ·· r · n # e T w es s l a fo r car fullypreventextraneousexplanationsorcomments.Combining
fans! ······ #Tesla #Roadster #Tesla #Roadster (Posted on 2024-10-12, #Roadster (Posted on 2024-10-12, 2103 likes,
(Posted on 2024-10-12, 2103 likes, 2103 likes, 530 retweets, 275 replies) 530 retweets, 275 replies) “Do”instructions,suchasexplicitoutputformatdefinitions,with
530 retweets, 275 replies)
Output JSON: Output JSON: “Don’t”instructions,likeexclusionconstraints,significantlyre-
Output JSON with metadata of the { "tweet_id": , { "tweet_id": # A unique identifier for the tweet,
tweet. "username": , "username": # The username of the user who ducesredundancywhilemaintaininghighoutputconsistencyin
"timestamp": , posted the tweet, prefixed with '@',
"engagement": } th " e ti m tw e e s e ta t m w p a " s : p # u T b h li e s h ti e m d e i s n t a IS m O p 8 in 6 d 0 i 1 c a fo tin rm g a w t, hen LLM-generatedcontent.
"engagement": # Interaction metrics for the
tweet, such as likes, retweets, and replies }
{ "tweet_id": null, 3.3.3 PositionofKnowledgeInputPlaceholder.
"username": "evupdates",
"text": "Major news for car { { Inthisexperiment,weexploretheoptimalpositionofthe{Knowlenthusiasts and Tesla "tweet_id": "@evupdates", "tweet_id": "evupdates_2024-10-12",
fans! ······ #Tesla "username": "evupdates", "username": "@evupdates", edgeInput}placeholder,themostcommonlyusedtype,asidentified
# Roadster", "timestamp": "2024-10-12", "timestamp": "2024-10-12T00:00:00Z",
" " m ha e s n h t t i a o g n s s " " : : [ [ " " T e e lo sl n a m ", u " s R k o "] a , d ster"], " e " n li g k a e g s" e : m 2 e 1 n 0 t" 3 : , { " e " n li g k a e g s" e : m 2 e 1 n 0 t" 3 : , { inFinding5.Weusearetrieval-augmentedgeneration(RAG)-style
"created_at": "2024-10-12", "retweets": 530, "retweets": 530,
"likes": 2103, "replies": 275 "replies": 275 taskwhereusersposequestions,externalknowledgeisprovidedas
"retweets": 530, } }
"replies": 275 } } } input,anddevelopersdefineinstruction(e.g.,directive,constraint,
outputformat)toprocessthedynamicinput.Toassesstheimpact

### Figure10:Outputexamplesofdifferentjsonoutputformat

ofthe{KnowledgeInput}placeholder’sposition,placedeitherat
patterns[30].
thebeginningorendoftheprompt,asnotedinFinding5,wetest
twoconfigurations:InstructionFirst,wherethetask-intentportion
oftheinstructionprecedestheknowledgeinput,andPlaceholder

### First,wheretheknowledgeinputprecedestheinstruction.Inboth

butattributeslike“username”and“timestamp”remainambigu- configurations,the{UserQuestion}placeholderremainsattheend,
ouswithoutfurtherclarification.Case3resolvestheseambigui- followingthemostfrequentpositionof{UserQuestion}inFigure8.
tiesbyaddingcleardescriptionsforeachattribute(e.g.,defining Thepopulatedtemplatesspanavarietyoftopics,suchasmedical
“username”astheTwitterhandleprefixedwith“@”andspecifying andcode-relatedQA.Wealsoselectinputsofvaryinglengthsto
“timestamp”tofollowtheISO8601format[29]),resultinginoutputs adapttoreal-worldusagescenarios.Evaluationisbasedontwo
thataremoreaccurateandalignedwithuserexpectations. human-assessedmetrics,scoredona1–5scale,whichassessesthe
relevancetoboththedeveloper-definedtaskinstructionandthe
Finding7: WhengeneratingLLMoutputsinJSONformat,ex- end-userquestioningeneraltask-orientedQ&Asystems[44]:
plicitJsonAttributeNamesenhanceformatconsistencybyensur- • ContentFollowing(Question): Alignmentwithuserquestion.
ingstructuredanduniformoutputs.Additionally,detailedJson • ContentFollowing(TaskIntent): Adherencetothedeveloper-
AttributeDescriptionsfurtherrefinecontent-following,reducing definedtaskintent(e.g.,includingdirective,constraint,and
ambiguityandbetteraligningwithuser-definedrequirements. outputformat).

### Table7presentstheaverageContentFollowingscoresunder

3.3.2 ExclusionConstraintforOutput. differentconfigurations.BothmodelsexhibithighscoresforCon-
Well-definedJSONoutputformatsenhancetheformat-following tentFollowing(Question),reflectingconsistentalignmentwithuser
abilitiesofLLMswhengeneratingJSONobjects.However,asob- queriesattheendoftheprompttemplateregardlessofplaceholder
servedinthepreviousexperiment,LLMsoftenincluderedundant position.However,forContentFollowing(TaskIntent),thePlaceexplanationsalongsidetheJSONobject,leadingtooutputincon- holderFirstpatternconsistentlyoutperformstheInstructionFirst
sistency.Thisexperimentevaluatestheeffectivenessofexclusion pattern,withaveragescoresof4.63forLLaMA(+0.91)and4.60
constraintsinreducingsuchredundancies.Usingthesame15pop- forGPT(+0.34).Notably,asknowledgeinputlengthincreases,the
ulatedtemplatesfromtheJSONOutputPattern3experiment,we InstructionFirstpatternsuffersamoresignificantperformance
applyanexclusionconstraint,“Donotprovideanyotheroutput dropcomparedtothePlaceholderFirstpattern.Thissuggeststhat
textbeyondtheJSONstring”,positionedbeforetheJSONformat placingthetaskintentofinstructionbeforetheknowledgeinput
definitionasperthecomponentorderidentifiedinfindings1.For increases the likelihood of forgetting or misalignment as input
evaluation,wedefinethemetricFormatFollowingasabinaryvalue: lengthgrows.Conversely,placingthetaskintentofinstruction
“1”iftheoutputconsistssolelyoftheJSONstringandisreadyfor aftertheknowledgeinputmitigatesthisissue,maintainingrobust
directparsing,and“0”otherwise. taskintentadherenceevenwithlonginputs.

### Resultshighlighttheimpactoftheexclusionconstraint.Forthe

llama3-70b-8192model,theoriginalpromptsyieldaFormatFollowingrateof40%(onlyJSONstringin40%ofoutputs).Theconstraint Table7:Outputqualityunderdifferentpositionpatterns
raises this rate to 100%, demonstrating improved adherence. In

### ContentFollowing ContentFollowing

16.67%ofcases,theoutputisenclosedin"""json"""withoutany Pattern Model (Question) (TaskIntent)
otherexplanationtext,whichwedonotconsiderredundant.The

### LLaMA 4.52 3.72


### InstructionFirst

gpt-4omodelperformsbetterwiththeoriginalprompts,achieving GPT 4.61 4.26
an86.67%adherencerate,furtherincreasingto100%withtheex-

### PlaceholderFirst


### LLaMA 4.84(+0.32) 4.63(+0.91)

clusionconstraintapplied.Thesefindingsunderlinetheexclusion GPT 4.70(+0.09) 4.60(+0.34)
constraint’svalueinimprovingclarity,reducingredundancy,and
InstructionFirstPatternisTaskIntent->{KnowledgeInput}->{UserQuestion}.
ensuringstrictadherencetooutputformatrequirements. PlaceholderFirstPatternis{KnowledgeInput}->TaskIntent->{UserQuestion}.

<!-- Page 9 -->

FromPromptstoTemplates:ASystematicPromptTemplateAnalysisforReal-worldLLMapps
offerpre-definedtemplatesforcommontasks.Forinstance,tem-
Use the information provided below to answer the questions at Information: {Knowledge about skin cancer}
t I f G I in h n r f o e f e c t o h m n l u r e e e m d n t r a h e a a d n e t t . i e i s n o c w n t o t h h e , n e e r g t e t e a a o x n n n t t e . s s h r w w e a e e t q e r r u i s " n e T o s e h m t n i e o e g n a l c i n s i u s s h r w i n o la e o u n r t s g c is o u o r a n n g r o ta e e t i l n . e in e v a d th n i e n t f c t a h o c e n t s t p e e r x o t x ” v t . r id a e ct d e d U t I f G I h n r f o s e e c th m e n l u e e e t d n t h r a h e a d e n e t . i e s n in c w t o f t h o h e n e r e r t m e t a a o x a n n t t t . s s i h o w w e n e e q p r r u r i s o n e o v s e m i t d n io e e g n d l c i s i u b s h r e i n o l l a o o u n w t s g c t o u o o r a n a g r ta e n e i l s n . e w e va d e n r i n t t h f t a e h c e q t s u p e e ro s x v t t i r i o d a n e c s t d e a d t p o ta u la s t k t p e u s (s t c e f o e o u r S m ld e a c i t t n i ( c o s l e n u e d 3 S e . e 3 a c .3 n t ) io . in n B f y 3 o . r 1 l m e .3 v a ) e t o r io r a n g a - i R n se A g e G k th - in s e t g y o l t v e a e s q r k u a e w ll s i t c t i o h o m n J - S p a O o n N n sw e a n e s t ri t o n h r g e -
Information: {Knowledge about skin cancer} information, generate “The answer is not in the context”.
Question: Question: der identified in Section 3.1.2, providers can establish a unified
{What are different types of skin cancer? } {What are different types of skin cancer? }
structureforthesetemplates.Furthermore,basedonthepattern
Output of Pattern 1 Output of Pattern 2 testingresultsoutlinedinSection3.3,APIproviderscanadoptop-
According to the provided context, there are two main forms of skin According to the provided context, there are two main forms of skin timalwritingpatternstailoredtospecifictasks,ensuringimproved
cancer: melanoma and nonmelanoma. ······ The most common types cancer: melanoma and nonmelanoma. ······ The most common
o sq f u n a o m nm ou e s l a c n e o ll m c a a r s c k in in o m ca a n . cers are basal cell carcinoma and t s y q p u e a s m o o f u n s o c n e m ll e c l a a r n c o i m no a m s a k . in cancers are basal cell carcinoma and generationperformanceforthesepre-definedtemplates.
Curious fact: Did you know that the skinis the body's largest organ, Curious fact: Did you know that skin cancer can occur in mucous Automatedtemplateevaluation/explainabilitytools.Inand it protects against heat, sunlight, injury, and infection, while membranes, such as the lips, and is called intraocular or ocular
also helping to control body temperature and storing water, fat, and melanoma? formedbyourfindingsinRQ3,APIproviderscoulddevelopautovitamin D?
Relevant fact: Melanomacan occur in people of all skin tones, not matedevaluationtoolstoassistLLMappdevelopersintestingand
just those with fair skin.
refiningprompttemplates.Thesetoolsshouldenabledevelopers
tocompareoutputsfromdifferenttemplatepatternsforthesame
Figure11:OutputexampleswithKnowledgeInputindifferinputs,facilitatingtheidentificationofoptimaldesigns.Moreover,
entprompttemplatepositions[7].
thetoolsshouldanalyzethetemplatestructuretoidentifymeasur-
Figure11presentsacomparisonusingalonginputtext.The ableevaluationcriteria,suchasconstraintsoroutputrequirements.
leftexamplefollowstheInstructionFirstpattern,whiletheright These evaluations could give scores and explanations based on
onefollowsPlaceholderFirst.Inboth,theuserquestionremains metricslikecontent-followingandformat-following.Additional
attheendoftheprompttemplate.Coloredsectionshighlightthe features,suchasmodelversioncomparisonsandprompttemplate
instruction(red),knowledgeinput(green),anduserquestion(grey). historytracking,couldfurtherenhancetheusabilityofthesetools.
Theupperportionofeachsidepresentsthefilledprompttemplate,
whilethelowerportionshowcasestherespectiveLLMoutput.In
thisexample,thelonginputisadetaileddescriptionofskincancer. 4.2 ImplicationsforLLMappDevelopers
RegardingtheLLMoutputs,bothpatternsprovidesimilarresponses AfteranLLMapp’srelease,maintainingprompttemplatesbasedon
totheuserquestion,withthemiddleportionofthelongdescrip- userfeedbackiscrucialtoensurehigh-qualityoutputs.However,
tionaboutskincancerbeingreducedinbothcases.However,the identifyingthemosteffectiveimprovementstrategy—suchasmodidifferencesariseinhowtheLLMaddressesthefactsrequiredby fyingspecificcomponentsoradoptingnewprompttechniques—can
theinstruction.IntheInstructionFirstpattern,the“curiousfact” bechallenging.Whileswitchingtoamorepowerfulmodelmay
outputdiscusseswhattheskinis,which,althoughinteresting,is improveperformance,italsosignificantlyincreasescosts,making
unrelatedtotheuserquestion.Additionally,therelevantfactis costefficiencyacriticalconsiderationforthesuccessofLLMapps.
missing.Incontrast,thePlaceholderFirstpatterngeneratesmore Prompttemplatesmaintenance. Prompttemplatesshould
alignedresults.The“curiousfact”and“relevantfact”bothrelate adaptdynamicallytoenhanceuserexperience,incorporatinguser
to skin cancer types, discussing where they occur (e.g., on mu- feedbackandexpertreviewsforcontinuousrefinement[31,46].
cousmembranes)andtheiroccurrenceacrossvariousskintones, Analyzinghistoricalusagedata,suchasinputlengthsandcontent
thusprovidingamorerelevantandcomprehensiveresponsetothe types,helpsdevelopersoptimizeplaceholdersandadjustcompoinstructionanduserquestion. nentpositionstopreventkeyinformationfrombeingoverlooked,
especiallywhenhandlinglonginputs(asnotedinRQ3).Placehold-

### Finding9: Positioningthetaskintentofinstructionanduser

ersshouldalsoalignwithreal-worldscenarios—forinstance,sepaquestionaftertheknowledgeinputenhancesoutputconsistency
ratingbackgroundandanalyticalinputsintodistinctplaceholders
andmitigatesinformationdecayinQ&Atasks,particularlywhen
improvesclarityandusability.Incorporatingmetadataplaceholders,
processingprompttemplateswithhighlyvariableinputlengths
suchas{output_format},ensuresflexibilityandrobustness,accominLLMapps.
modatingdiverseuserneeds.Developerandexpertreviewsfurther
validaterefinements,aligningtemplateswithbestpractices.Addi-

## 4 Implications

tionally,asobservedinSection3.2.3,manyprompttemplatesstill
Ourresearchoffersactionableinsightsintopromptengineeringfor
useambiguousplaceholders(e.g.,approximately5%ofplaceholders
variouspartiesinthesoftwareindustry:
arenamedsimplyas“text”),whichlacksmeaningfulcontextand
cancomplicatemaintenanceduringLLMappevolution.Clear,de-
4.1 ImplicationsforLLMProviders scriptivenamingreduceserrors,mitigateschallengesarisingfrom
LLMproviderscanenhancetheusabilityandperformanceoftheir memorylimitationsanddeveloperturnover,andensureslong-term
APIs by offering best practices for designing, testing, and opti- softwarereliability.
mizingprompttemplates.AlmostallcommercialLLMproviders Usingwell-definedprompttemplatestostrengthenweak
supportprompttemplates,suchasGoogleCloudGemini[19]and LLMs. As demonstrated in our sample testing results in Sec-
Langchain[39].However,noneofthemprovidesanyguidelineon tion3.3,well-definedprompttemplatessignificantlyenhancethe
howtowriteeffectiveprompttemplates. instruction-following capability of weaker models (e.g., llama3-
Pre-definedprompttemplates.Toaddressthechallengesde- 70b-8192).Insomecases,thesetemplatesenableweakermodels
velopersfaceincraftingeffectiveprompts,LLMproviderscould toachieveperformancelevelscomparabletothebest-performing

<!-- Page 10 -->


### Anonymousauthors

LLMs(e.g.,gpt-4o).Forinstance,inthelong-inputexperimentdis- execution.Thisworkoffersfoundationalsupportforenhancing
cussed in Section 3.3.3, the output quality boost achieved with boththeusabilityandperformanceofLLMapps.
awell-definedprompttemplateforllama3-70b-8192wasnearly PromptEngineering. Promptengineeringiscriticalforguiding
doublethatofgpt-4o.Thishighlightsthecriticalroleofcarefully LLMs,butthevariabilityofnaturallanguageposeschallengesin
designedprompttemplatesforoptimizingweakermodels.When achievingclarityandconsistency.Recentresearchhasfocusedon
selectingfoundationmodelsforLLMapps,developersshouldfirst commonelementsandstructuralpatterns,includingstandardizing
considerre-designingprompttemplatesforthetargettaskifthe promptelementsintoreusableframeworks[64],emphasizingtaskgenerationqualityfallsshortofexpectations,ratherthanimmedi- specificinstructionsandformatting[55],andanalyzingtheeffects
atelyswitchingtoamoreadvancedmodel.Well-designedprompt ofcomponentsequencing[12,43,77].Otherstudieshaveexplored
templatescansignificantlystrengthentheinstruction-following theimpactofminorpromptmodifications,suchaspunctuation[61]
abilitiesofweakermodels,thereforecontributingtoreducingcosts, andwordrephrasing[73].
anessentialfactorforbusinesssuccess. Incontrasttostudiesongeneralpromptdesign,ourresearch
Trade-offsinIn-Contextlearning. In-contextlearninghas focuses on systematically analyzing prompt templates used in
becomeawidelyadoptedpromptengineeringtechniqueinsoft- LLMapps.Buildingonpriorworkinpromptanalysis[10,60],werewareengineeringresearch[26].However,ourstatisticalanalysisof finetheanalysisframeworkbytargetingthecommoncomponents
componentdistributioninprompttemplates(Table3)revealsthat of prompt templates. Unlike general prompts crafted for direct
fewerthan20%ofapplicationsinourdatasetincorporatefew-shot user-LLMinteractions,prompttemplatesdesignedbyLLMappdeexamplesintheirprompts.Consideringtheusageofdynamically velopersaretypicallylongerandmoreintricate,oftenincorporating
loadedexamplesthroughplaceholders(lessthan5%),few-shotex- multiplecomponentstoarticulatedetailedtaskinstructions[66].
amples are still not commonly used in prompt templates. Prior Adistinctivefeatureofprompttemplatesistheinclusionofplaceresearchalsohighlightsthatclearlydefinedtaskswithoutexam- holders [60], which general prompts usually lack. Placeholders
plescansometimesoutperformthosewithfew-shotexamplesin allowdeveloperstoaccountfordiverseuserinputsandscenarios
termsofgenerationquality[55].Thisfindinglikelyexplainswhy whileenhancingthereusabilityandadaptabilityoftemplates.To
manyLLMappsomitfew-shotlearning.Whilefew-shotexamples thebestofourknowledge,thisisthefirststudytosystematically
cansometimesenhanceperformance,theyareoftenunnecessary analyzeprompttemplatesinLLMapps,providingdeveloperswith
whenawell-definedprompttemplateisused.Moreover,including actionableguidancefordesigningeffective,reusabletemplatesthat
suchexamplescanintroducedrawbacks,suchasincreasedtoken accommodateabroadrangeofuserinputs.
costsandtheriskofsemanticcontamination.In-contextlearningis
notaone-size-fits-allsolution.WhendesigningLLMapps,develop- 6 CONCLUSION
ersshouldprioritizerefiningandoptimizingprompttemplatesto Thispaperprovidesacomprehensiveanalysisofprompttemplate
achieveclarityandalignmentwithtaskrequirementsratherthan structureandcompositioninLLM-poweredapplications,analyzdefaultingtofew-shotlearning. ing how developers design these templates to optimize LLM’s
instruction-followingabilities.Weconstructadatasetofprompt

## 5 Relatedwork

templatesfromGitHubopen-sourceprojects,identifyingcommon
SoftwareEngineeringforLLM.TheemergingfieldofSoftware componentsandplaceholdersinthoseprompttemplates.Through
Engineering for Large Language Models (SE4LLM) applies soft- LLM-assisted and human-verified analysis, we analyze the frewareengineeringprinciplestovariousstagesofLLMdevelopment, quentlyusedtermsofthesecomponentsandplaceholders,aswellas
addressingchallengessuchasefficiencythroughsystemstackop- theirpositions,andfurtheridentifyseveralorganizationalpatterns
timization[2],modelcompressionviapromptlearning[71],and basedontheanalysisresult.Finally,weconductprompttemplate
securitywithmulti-roundautomaticred-teaming[18]andmonitor- testingtoevaluatehowdifferentpatternsinfluencetheinstructioningthroughmodularapproaches[21].Researchhasalsoexplored followingperformanceofLLM.Thesefindingsofferfoundationalininterpretabilityusingattentionvisualization[17],concept-based sightsforpromptengineering,guidingthedesignofrobustprompt
analysis[48],andsubnetworkextraction[67]. templatesthatenhancethequalityofLLMoutputsacrossvarious
BeyondLLMoptimization,attentionhasturnedtoLLMapps, LLMapps.
focusingonpost-deploymentchallenges.Zhaoetal.[76]examined
LLMappstores,investigatinguserexperience,developerstrate- ACKNOWLEDGEMENTS
gies,andecosystemdynamicswhilehighlightingchallengessuch

### ThisresearchwassupportedbyOpenAIthroughtheprovisionof

assecurityandprivacy.SecurityissuesintheLLMappecosystem,
APIcreditsunderOpenAIResearcherAccessProgram.Weappreincludingjailbreaking,promptinjection,credentialleaks,andinciatetheirsupportinfacilitatingourstudyonprompttemplate
consistentdataprovision,havebeenextensivelystudied[15,42,72],
analysis.
emphasizingtheneedforrobustsafeguards.
Incontrasttothesepost-deploymentstudies,ourresearchfocusesonthepre-deploymentphaseofLLMappdevelopmentby
analyzingprompttemplates—thecriticalinterfacebetweenusers
andLLMs.Byexaminingpromptstructure,components,andpatterns,weprovideactionableinsightstohelpdevelopersdesignmore
effectivetemplates,therebyoptimizinginteractionsbeforemodel

<!-- Page 11 -->

FromPromptstoTemplates:ASystematicPromptTemplateAnalysisforReal-worldLLMapps

## References 130–146.

[1] JoshAchiam,StevenAdler,SandhiniAgarwal,LamaAhmad,IlgeAkkaya,Floren- [25] MatthewHonnibalandInesMontani.2017.spaCy2:NaturallanguageunderciaLeoniAleman,DiogoAlmeida,JankoAltenschmidt,SamAltman,Shyamal standingwithBloomembeddings,convolutionalneuralnetworksandincremen-
Anadkat,etal.2023. Gpt-4technicalreport. arXivpreprintarXiv:2303.08774 talparsing.(2017). Toappear.
(2023). [26] XinyiHou,YanjieZhao,YueLiu,ZhouYang,KailongWang,LiLi,XiapuLuo,
[2] RezaYazdaniAminabadi,SamyamRajbhandari,AmmarAhmadAwan,Cheng DavidLo,JohnGrundy,andHaoyuWang.2024. Largelanguagemodelsfor
Li,DuLi,EltonZheng,OlatunjiRuwase,ShadenSmith,MinjiaZhang,Jeff softwareengineering:Asystematicliteraturereview. ACMTransactionson
Rasley,etal.2022.Deepspeed-inference:enablingefficientinferenceoftrans- SoftwareEngineeringandMethodology33,8(2024),1–79.
formermodelsatunprecedentedscale.InSC22:InternationalConferencefor [27] XinyiHou,YanjieZhao,andHaoyuWang.2024.Onthe(In)SecurityofLLM
HighPerformanceComputing,Networking,StorageandAnalysis.IEEE,1–15. AppStores.arXivpreprintarXiv:2407.08422(2024).
[3] Anthropic. 2024. User Guides - Prompt engineering. https: [28] Hypercerts.2024.hypercerts. https://github.com/hypercerts-org/hypercerts
//docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prompt- [29] InternationalOrganizationforStandardization.2019.ISO8601. https://www.
templates-and-variables iso.org/iso-8601-date-and-time-format.html
[4] Anthropic.2024.UserGuides-Strengthenguardrails. https://docs.anthropic. [30] JinaAI.2023.dev-gpt. https://github.com/jina-ai/dev-gpt
com/en/docs/test-and-evaluate/strengthen-guardrails/reduce-hallucinations [31] IshikaJoshi,SimraShahid,ShreeyaVenneti,ManushreeVasu,YantaoZheng,
[5] EranAvidanandDrorGFeitelson.2017.Effectsofvariablenamesoncompre- YunyaoLi,BalajiKrishnamurthy,andGromitYeuk-YinChan.2024.CoPrompter:
hension:Anempiricalstudy.In2017IEEE/ACM25thInternationalConference User-CentricEvaluationofLLMInstructionAlignmentforImprovedPrompt
onProgramComprehension(ICPC).IEEE,55–65. Engineering. ArXivabs/2411.06099(2024). https://api.semanticscholar.org/
[6] AsmaBenAbachaandDinaDemner-Fushman.2019. Aquestion-entailment CorpusID:273963317
approachtoquestionanswering.BMCbioinformatics20(2019),1–23. [32] Shubhra(Santu)KarmakerandDongjiFeng.2023.TELeR:AGeneralTaxonomy
[7] DiegoCarpintero.2024.wikisearch. https://github.com/dcarpintero/wikisearch ofLLMPromptsforBenchmarkingComplexTasks.ArXivabs/2305.11430(2023).
[8] XinxiChen,LiWang,WeiWu,QizhiTang,andYiyaoLiu.2024. HonestAI: https://api.semanticscholar.org/CorpusID:258823169
Fine-Tuning"Small"LanguageModelstoSay"IDon’tKnow",andReducing [33] GeorgeKatsogiannis-MeimarakisandGeorgiaKoutrika.2023.Asurveyondeep
HallucinationinRAG.ArXivabs/2410.09699(2024). https://api.semanticscholar. learningapproachesfortext-to-SQL.TheVLDBJournal32,4(2023),905–936.
org/CorpusID:273346023 [34] kenoharada.2023.AI-LaBuddy. https://github.com/kenoharada/AI-LaBuddy
[9] YihanChen,BenfengXu,QuanWang,YiLiu,andZhendongMao.2024.Bench- [35] AmeyaKetkar,DanielRamos,LazaroClapp,RajBarik,andMuraliKrishna
markinglargelanguagemodelsoncontrollablegenerationunderdiversified Ramanathan.2024. ALightweightPolyglotCodeTransformationLanguage.
instructions.InProceedingsoftheAAAIConferenceonArtificialIntelligence, ProceedingsoftheACMonProgrammingLanguages8,PLDI(2024),1288–1312.
Vol.38.17808–17816. [36] KwonKo.2024.chart-llm. https://github.com/hyungkwonko/chart-llm
[10] Google Cloud. 2024. Prompt Design Strategies for Generative AI. [37] Kyubyong.2019.ATensorFlowImplementationofTransformer. https://github.
https://cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/prompt- com/Kyubyong/transformer
design-strategiesAccessed:2024-07-14. [38] LAION-AI.2024.Open-Assistant.https://github.com/LAION-AI/Open-Assistant
[11] ValerioCosentino,JavierLuis,andJordiCabot.2016. FindingsfromGitHub: [39] LangChain.2024. PromptTemplates. https://python.langchain.com/docs/
methods,datasetsandlimitations.InProceedingsofthe13thInternational concepts/prompt_templates/
ConferenceonMiningSoftwareRepositories.137–141. [40] JiaLi,YongminLi,GeLi,ZhiJin,YiyangHao,andXingHu.2023.Skcoder:A
[12] FlorinCuconasu,GiovanniTrappolini,FedericoSiciliano,SimoneFilice,Cesare sketch-basedapproachforautomaticcodegeneration.In2023IEEE/ACM45th
Campagnano,YoelleMaarek,NicolaTonellotto,andFabrizioSilvestri.2024. InternationalConferenceonSoftwareEngineering(ICSE).IEEE,2124–2135.
Thepowerofnoise:Redefiningretrievalforragsystems.InProceedingsof [41] ZongjieLi,ChaozhengWang,ZhiboLiu,HaoxuanWang,DongChen,Shuai
the47thInternationalACMSIGIRConferenceonResearchandDevelopment Wang,andCuiyunGao.2023. Cctest:TestingandrepairingcodecompleinInformationRetrieval.719–729. tionsystems.In2023IEEE/ACM45thInternationalConferenceonSoftware
[13] RossDawson.2024.Humans+AI:PromptElements. https://rossdawson.com/ Engineering(ICSE).IEEE,1238–1250.
humans-plus-ai-old/humans-ai-prompt_elements/Accessed:2024-10-12. [42] YiLiu,GeleiDeng,YuekangLi,KailongWang,ZihaoWang,XiaofengWang,Tian-
[14] Definitive.2024.openassistants. https://github.com/definitive-io/openassistants weiZhang,YepangLiu,HaoyuWang,YanZheng,etal.2023.PromptInjection
[15] GeleiDeng,YiLiu,YuekangLi,KailongWang,YingZhang,ZefengLi,Haoyu attackagainstLLM-integratedApplications. arXivpreprintarXiv:2306.05499
Wang,TianweiZhang,andYangLiu.2023.MASTERKEY:AutomatedJailbreaking (2023).
ofLargeLanguageModelChatbots.Proceedings2024NetworkandDistributed [43] YijinLiu,XianfengZeng,FandongMeng,andJieZhou.2023.Instructionposition
SystemSecuritySymposium(2023). https://api.semanticscholar.org/CorpusID: mattersinsequencegenerationwithlargelanguagemodels. arXivpreprint
259951184 arXiv:2308.12097(2023).
[16] MichaelDesmondandMichelleBrachman.2024.ExploringPromptEngineering [44] BeiLuo,RaymondYKLau,ChunpingLi,andYain-WharSi.2022.Acriticalreview
PracticesintheEnterprise.arXivpreprintarXiv:2403.08950(2024). ofstate-of-the-artchatbotdesignsandapplications. WileyInterdisciplinary
[17] AndreaGalassi,MarcoLippi,andPaoloTorroni.2020.Attentioninnaturallan- Reviews:DataMiningandKnowledgeDiscovery12,1(2022),e1434.
guageprocessing.IEEEtransactionsonneuralnetworksandlearningsystems [45] MaanvithaGongalla.2024.thinkai. https://github.com/maanvithag/thinkai
32,10(2020),4291–4308. [46] StephenMacneil,AndrewTran,JoanneKim,ZihengHuang,SethBernstein,
[18] SuyuGe,ChuntingZhou,RuiHou,MadianKhabsa,Yi-ChiaWang,QifanWang, andDanMogil.2023. PromptMiddleware:MappingPromptsforLargeLan-
JiaweiHan,andYuningMao.2023.Mart:Improvingllmsafetywithmulti-round guageModelstoUIAffordances. ArXivabs/2307.01142(2023). https://api.
automaticred-teaming.arXivpreprintarXiv:2311.07689(2023). semanticscholar.org/CorpusID:259316650
[19] Google Cloud. 2024. Generative AI on Vertex AI - Use prompt tem- [47] MattNigh.2023.ChatGPT3-Free-Prompt-List:Afreeguideforlearningtocreate
plates. https://cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/ ChatGPT3Prompts. https://github.com/mattnigh/ChatGPT3-Free-Prompt-List
prompt-templates [48] TuomasOikarinen,SubhroDas,LamMNguyen,andTsui-WeiWeng.2023.
[20] SimonCorneliusGorissen,StefanSauer,andWolfGBeckmann.2024. ASur- Label-freeconceptbottleneckmodels.arXivpreprintarXiv:2304.06129(2023).
veyofNaturalLanguage-BasedEditingofLow-CodeApplicationsUsingLarge [49] OpenAI.2024. OpenAIPromptEngineeringBestPractices. https://platform.
LanguageModels.InInternationalConferenceonHuman-CentredSoftware openai.com/docs/guides/prompt-engineeringAccessed:2024-07-14.
Engineering.Springer,243–254. [50] Oracle.2024.JDK22Documentation. https://docs.oracle.com/en/java/javase/22
[21] ShubhGoyal,MedhaHira,ShubhamMishra,SukritiGoyal,ArnavGoel,Niharika [51] KaiserPister,DhrubaJyotiPaul,IshanJoshi,andPatrickBrophy.2024.PromptSet:
Dadu,DBKirushikesh,SameepMehta,andNishthaMadaan.2024.LLMGuard: AProgrammer’sPromptingDataset.InProceedingsofthe1stInternational
GuardingagainstUnsafeLLMBehavior.InProceedingsoftheAAAIConference WorkshoponLargeLanguageModelsforCode.62–69.
onArtificialIntelligence,Vol.38.23790–23792. [52] puzzle.today. 2024. GPT Store - Write For Me. https://gptstore.ai/gpts/
[22] LianghongGuo,YanlinWang,EnshengShi,WanjunZhong,HongyuZhang,Ji- LJybdvxEb4-write-for-me
achiChen,RuikaiZhang,YuchiMa,andZibinZheng.2024. Whentostop? [53] BoQiao,LiqunLi,XuZhang,ShilinHe,YuKang,ChaoyunZhang,FangkaiYang,
towardsefficientcodegenerationinllmswithexcesstokenprevention.In HangDong,JueZhang,LuWang,etal.2023.Taskweaver:Acode-firstagent
Proceedingsofthe33rdACMSIGSOFTInternationalSymposiumonSoftware framework.arXivpreprintarXiv:2311.17541(2023).
TestingandAnalysis.1073–1085. [54] MuraliKrishnaRamanathan,LazaroClapp,RajkishoreBarik,andManuSrid-
[23] hambuger.2023.Andrew. https://github.com/hambuger/Andrew haran.2020.Piranha:Reducingfeatureflagdebtatuber.InProceedingsofthe
[24] KaroliineHolter,JuhanOskarHennoste,PatrickLam,SimmoSaan,andVesalVo- ACM/IEEE42ndInternationalConferenceonSoftwareEngineering:Software
jdani.2024.Abstractdebuggers:Exploringprogrambehaviorsusingstaticanaly- EngineeringinPractice.221–230.
sisresults.InProceedingsofthe2024ACMSIGPLANInternationalSymposium [55] LariaReynoldsandKyleMcDonell.2021.Promptprogrammingforlargelanguage
onNewIdeas,NewParadigms,andReflectionsonProgrammingandSoftware. models:Beyondthefew-shotparadigm.InExtendedabstractsofthe2021CHI
conferenceonhumanfactorsincomputingsystems.1–7.

<!-- Page 12 -->


### Anonymousauthors

[56] AlokSaboo.2024.beets-plexsync. https://github.com/arsaboo/beets-plexsync [67] YulongWang,HangSu,BoZhang,andXiaolinHu.2020. Interpretneural
[57] Salesforce. 2024. Prompt Builder - Prompt Template Types. https: networksbyextractingcriticalsubnetworks. IEEETransactionsonImage
//help.salesforce.com/s/articleView?id=sf.prompt_builder_standard_template_ Processing29(2020),6707–6720.
types.htm&type=5 [68] weaviate.2024.Verba. https://github.com/weaviate/Verba
[58] AbelSalinasandFredMorstatter.2024.Thebutterflyeffectofalteringprompts: [69] SimonWeberandJieboLuo.2014.Whatmakesanopensourcecodepopular
Howsmallchangesandjailbreaksaffectlargelanguagemodelperformance. ongithub?.In2014IEEEInternationalConferenceonDataMiningWorkshop.
arXivpreprintarXiv:2401.03729(2024). IEEE,851–855.
[59] ElvisSaraviaetal.2022.Promptengineeringguide.GitHub.URL:https://github. [70] CongyingXia,ChenXing,JiangshuDu,XinyiYang,YihaoFeng,RanXu,Wencom/dair-ai/Prompt-Engineering-Guide(2022). Accessed:2024-06-01. pengYin,andCaimingXiong.2024. FOFO:ABenchmarktoEvaluateLLMs’
[60] SanderSchulhoff,MichaelIlie,NishantBalepur,KonstantineKahadze,Amanda Format-FollowingCapability.arXivpreprintarXiv:2402.18667(2024).
Liu,ChengleiSi,YinhengLi,AayushGupta,HyoJungHan,SevienSchulhoff, [71] ZhaozhuoXu,ZiruiLiu,BeidiChen,YuxinTang,JueWang,KaixiongZhou,
etal.2024.ThePromptReport:ASystematicSurveyofPromptingTechniques. XiaHu,andAnshumaliShrivastava.2023.Compress,thenprompt:Improving
arXivpreprintarXiv:2406.06608(2024). accuracy-efficiencytrade-offofllminferencewithtransferableprompt.arXiv
[61] MelanieSclar,YejinChoi,YuliaTsvetkov,andAlaneSuhr.2023. Quantify- preprintarXiv:2305.11186(2023).
ingLanguageModels’SensitivitytoSpuriousFeaturesinPromptDesignor: [72] ChuanYan,RuomaiRen,MarkHuasongMeng,LiuhuoWan,TianYangOoi,
HowIlearnedtostartworryingaboutpromptformatting. arXivpreprint andGuangdongBai.2024. Exploringchatgptappecosystem:Distribution,
arXiv:2310.11324(2023). deploymentandsecurity.InProceedingsofthe39thIEEE/ACMInternational
[62] Stevenic.2024.AgentM. https://github.com/Stevenic/agentm-py ConferenceonAutomatedSoftwareEngineering.1370–1382.
[63] HugoTouvron,ThibautLavril,GautierIzacard,XavierMartinet,Marie-Anne [73] AdamYang,ChenChen,andKonstantinosPitas.2024. Justrephraseit!Un-
Lachaux,TimothéeLacroix,BaptisteRozière,NamanGoyal,EricHambro,Faisal certaintyestimationinclosed-sourcelanguagemodelsviamultiplerephrased
Azhar,etal.2023.Llama:Openandefficientfoundationlanguagemodels.arXiv queries.arXivpreprintarXiv:2405.13907(2024).
preprintarXiv:2302.13971(2023). [74] ZhiqiangYuan,MingweiLiu,ShijiDing,KaixinWang,YixuanChen,XinPeng,
[64] MingWang,YuanzhongLiu,XiaomingZhang,SonglianLi,YijieHuang,Chi andYilingLou.2024.Evaluatingandimprovingchatgptforunittestgeneration.
Zhang,DalingWang,ShiFeng,andJigangLi.2024.LangGPT:RethinkingStruc- ProceedingsoftheACMonSoftwareEngineering1,FSE(2024),1703–1726.
turedReusablePromptDesignFrameworkforLLMsfromtheProgrammingLan- [75] J.D.Zamfirescu-Pereira,RichmondY.Wong,BjoernHartmann,andQianYang.
guage.ArXivabs/2402.16929(2024). https://api.semanticscholar.org/CorpusID: 2023. WhyJohnnyCan’tPrompt:HowNon-AIExpertsTry(andFail)to
268032985 DesignLLMPrompts. Proceedingsofthe2023CHIConferenceonHuman
[65] YuWang,NedimLipka,RyanARossi,AlexaSiu,RuiyiZhang,andTylerDerr. FactorsinComputingSystems(2023).https://api.semanticscholar.org/CorpusID:

### Knowledgegraphpromptingformulti-documentquestionanswering.In 258217984

ProceedingsoftheAAAIConferenceonArtificialIntelligence,Vol.38.19206– [76] YanjieZhao,XinyiHou,ShenaoWang,andHaoyuWang.2024.Llmappstore
19214. analysis:Avisionandroadmap.arXivpreprintarXiv:2404.12737(2024).
[66] YizhongWang,SwaroopMishra,PegahAlipoormolabashi,YeganehKordi,Amir- [77] ZihaoZhao,EricWallace,ShiFeng,DanKlein,andSameerSingh.2021.Calibrate
rezaMirzaei,AnjanaArunkumar,ArjunAshok,ArutSelvanDhanasekaran, beforeuse:Improvingfew-shotperformanceoflanguagemodels.InInternational
AtharvaNaik,DavidStap,etal.2022.Super-naturalinstructions:Generalization conferenceonmachinelearning.PMLR,12697–12706.
viadeclarativeinstructionson1600+nlptasks.arXivpreprintarXiv:2204.07705
(2022). Received2025-XX-XX;accepted2025-XX-XX;revisedxxx;revisedxxx;
acceptedxxx

## Tables

**Table (Page 2):**

| ttemplate[23,36,56] |  |  |
|---|---|---|
| Data Collection { x } Representative Prompt Templates Prompt Data | Prompt Template Analysis LLM for Analysis Component Statistical Analysis AnalysisResult Result {𝒙} Predefined Placeholder Pattern Analysis Categories Analysis Result Result | Prompt Template Testing LLM for Testing LLM Output Sample Human Evaluation Test Data Result |
| Figure2:Anillustrationofthemainpipeline |  |  |


**Table (Page 2):**

|  |  |
|---|---|
|  |  |


**Table (Page 2):**

| {𝒙} |
|---|
|  |


**Table (Page 9):**

| Use the information provided below to answer the questions at the end. Include in the answer some curiousor relevantfactsextracted from the context. Generate the answer in englishlanguage. If the answer to the question is not contained in the provided information, generate "The answer is not in the context”. | Information: {Knowledge about skin cancer} |
|---|---|
|  | Use the information provided below to answer the questions at the end. Include in the answer some curiousor relevant facts extracted from the context. Generate the answer in englishlanguage. If the answer to the question is not contained in the provided information, generate “The answer is not in the context”. |
| Information: {Knowledge about skin cancer} |  |
| Question: {What are different types of skin cancer? } | Question: {What are different types of skin cancer? } |
