---
title: "Copilot Loop Fixing Code Smells"
original_file: "./Copilot_Loop_Fixing_Code_Smells.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["prompt-engineering", "llm", "rag", "chain-of-thought", "agents"]
keywords: ["copilot", "code", "generated", "generatedpythoncode", "python", "page", "smells", "usa", "ase", "sacramento"]
summary: "<!-- Page 1 -->

Copilot-in-the-Loop: Fixing Code Smells in Copilot-Generated

### Python Code using Copilot


### BeiqiZhang PengLiang∗ QiongFeng

SchoolofComputerScience SchoolofComputerScience SchoolofComputerScience
WuhanUniversity WuhanUniversity NanjingUniversityofScienceand

### Wuhan,China Wuhan,China Technology

zhangbeiqi@whu.edu.cn liangp@whu.edu.cn Nanjing,China
qiongfeng@njust.edu.cn

### YujiaFu ZengyangLi

SchoolofComputerScience SchoolofComputerScience
WuhanUniversity CentralChin"
related_documents: []
---

# Copilot Loop Fixing Code Smells

<!-- Page 1 -->

Copilot-in-the-Loop: Fixing Code Smells in Copilot-Generated

### Python Code using Copilot


### BeiqiZhang PengLiang∗ QiongFeng

SchoolofComputerScience SchoolofComputerScience SchoolofComputerScience
WuhanUniversity WuhanUniversity NanjingUniversityofScienceand

### Wuhan,China Wuhan,China Technology

zhangbeiqi@whu.edu.cn liangp@whu.edu.cn Nanjing,China
qiongfeng@njust.edu.cn

### YujiaFu ZengyangLi

SchoolofComputerScience SchoolofComputerScience
WuhanUniversity CentralChinaNormalUniversity

### Wuhan,China Wuhan,China

yujia_fu@whu.edu.cn zengyangli@ccnu.edu.cn

### ABSTRACT ACMReferenceFormat:

As one ofthe mostpopular dynamiclanguages, Python experi- BeiqiZhang,PengLiang,QiongFeng,YujiaFu,andZengyangLi.2024.
Copilot-in-the-Loop:FixingCodeSmellsinCopilot-GeneratedPythonCode
ences a decrease in readability and maintainability when code
smellsarepresent.RecentadvancementsinLargeLanguageModels
usingCopilot.InProceedingsofthe39thIEEE/ACMInternationalConference
onAutomatedSoftwareEngineering(ASE’24),October27–November01, havesparkedgrowinginterestinAI-enabledtoolsforbothcode
2024,Sacramento,California,USA.ACM,NewYork,NY,USA,5pages.https:
generationandrefactoring.GitHubCopilotisonesuchtoolthat
//doi.org/10.1145/xxxxxxx.xxxxxxx
hasgainedwidespreadusage.CopilotChat,releasedinSeptember
2023,functionsasaninteractivetoolaimedatfacilitatingnatural

## 1 Introduction

language-poweredcoding.However,limitedattentionhasbeen
giventounderstandingcodesmellsinCopilot-generatedPython CodesmellsrefertothesymptomsofpoordesignandimplemencodeandCopilotChat’sabilitytofixthecodesmells.Tothisend, tationdecisionsaccordingtothedefinitionbyMartinFowlerin
webuiltadatasetcomprising102codesmellsinCopilot-generated hisbook[9].Codesmellsnegativelyaffecttheinternalqualityof
Pythoncode.Ouraimistofirstexploretheoccurrenceofcode softwaresystems,hinderingcomprehensibilityandmaintainability
smellsinCopilot-generatedPythoncodeandthenevaluatethe [20,24]andincreasingerrorproneness[16,19].Theidentification
effectivenessofCopilotChatinfixingthesecodesmellsemploying ofcodesmellssuggeststhe potentialneedforcoderefactoring,
differentprompts.Theresultsshowthat8outof10typesofcode pinpointingwhenandwhatrefactoringcanbeappliedtocode[9].
smellscanbedetectedinCopilot-generatedPythoncode,among Python, consistently ranked as one of the most popular prowhichMultiply-NestedContaineristhemostcommonone.Forthese gramminglanguages[2],isincreasinglyusedinvarioussoftware
codesmells,CopilotChatachievesahighestfixingrateof87.1%, developmenttasks.Pythonisahigh-level,interpreted,anddynamic
showingpromiseinfixingPythoncodesmellsgeneratedbyCopilot languagethatprovidesasimplebuteffectiveapproachtoobjectitself.Inaddition,theeffectivenessofCopilotChatinfixingthese orientedprogramming[27].DuetoPython’snatureofflexibility
smellscanbeimprovedbyprovidingmoredetailedprompts. anddynamism,developersoftenfinditchallengingbothtowrite
andmaintainPythoncode[6],andabusingtheshortconstructsof
CCSCONCEPTS Pythoncanexposecodetobadpatternsandreducecodereadability
[3,17],leadingtotheoccurrenceofcodesmellsinPython[7].
•Softwareanditsengineering→Softwaremaintenancetools.
RecentadvancementsinLargeLanguageModels(LLMs)haveunveiledimpressivecapabilitiesinsolvingvariousNaturalLanguage

## Keywords

Processing(NLP)tasks[29,30],showcasingtheireffectivenessin

### CodeSmell,CodeQuality,CodeRefactoring,GitHubCopilot

e.g.,codegeneration[13]andrefactoring[23,26].ReleasedinJune
∗ThisworkispartiallyfundedbyNSFCwithNo.62172311. 2021,GitHubCopilotpoweredbyLLM(i.e.,OpenAICodex)has
beenwidelyembracedbydevelopersforcodeauto-completion,and
Permissiontomakedigitalorhardcopiesofallorpartofthisworkforpersonalor ithasevolvedintotheworld’smostwidelyadoptedAIdeveloper
classroomuseisgrantedwithoutfeeprovidedthatcopiesarenotmadeordistributed
forprofitorcommercialadvantageandthatcopiesbearthisnoticeandthefullcitation tool[1].However,concernsaroseregardingthequalityofcode
onthefirstpage.CopyrightsforcomponentsofthisworkownedbyothersthanACM generatedbyCopilot[31,33].Copilot’scodesuggestionalgorithms
mustbehonored.Abstractingwithcreditispermitted.Tocopyotherwise,orrepublish,
areincentivizedtoproposesuggestionsmorelikelytobeaccepted
topostonserversortoredistributetolists,requirespriorspecificpermissionand/ora
fee.Requestpermissionsfrompermissions@acm.org. ratherthaneasytoreadandunderstand,whichhasanadverse
ASE’24,October27–November01,2024,Sacramento,California,USA impactforlong-termcodemaintainability[11].Subsequently,in
©2024AssociationforComputingMachinery. September2023,apublicbetaofGitHubCopilotChathasbeen

## Acmisbn978-1-4503-Xxxx-X/18/06...$15.00

https://doi.org/10.1145/xxxxxxx.xxxxxxx releasedasaninteractivetoolforCopilot,aimingtoenablenatural
4202
guA
12
]ES.sc[
2v67141.1042:viXra

<!-- Page 2 -->

ASE’24,October27–November01,2024,Sacramento,California,USA B.Zhangetal.
language-poweredcoding[34].DeveloperscanutilizeCopilotChat observedacrossprogramminglanguages.Pearceetal.[21]investifortaskssuchascodeanalysisandfixingsecurityissues,democ- gatedtheprevalenceandconditionsthatcancauseGitHubCopilot
ratizingsoftwaredevelopmentforanewgeneration.Giventhe torecommendinsecurecode.Theirfindingsrevealedthatabout
potentialforCopilot-generatedPythoncodetoexhibitcodesmells 40%ofprogramsgeneratedbyCopilotweredeemedvulnerable.
and the capacity of Copilot Chat to assist in rectifying such is- Differenttothestudiesabove,ourworkfocusesoninvestigating
sues,thispaperdelvesintofixingcodesmellsinCopilot-generated aspecificissue—codesmells—inCopilot-generatedPythoncode
PythoncodeusingCopilotChat.Inthispaper,toevaluatethe andaccessingCopilotChat’sabilitytofixthesesmellsintheloop.
prevalenceofcodesmellsinCopilot-generatedPythoncodeand
thecompetenceofCopilotChatinfixingPythonsmells,webuilt 3 METHODOLOGY
adatasetwith102codesmellsinCopilot-generatedPythoncode.
3.1 UsePysmelltoDetectPythonCodeSmells

### Specifically,weinvestigatedtwoResearchQuestions(RQs):

ThisstudyaimstoexplorePythoncodesmellsinCopilot-generated
• RQ1:TowhatextentdoestheCopilot-generatedPython
codeandevaluateCopilotChat’scapabilitytofixPythonsmells.
codecontaincodesmells?
Wefirstbuiltadatasetconsistingof102codesmellsinCopilot-
• RQ2:HoweffectiveisCopilotChatinfixingdifferenttypes
generatedPythoncodebythefollowingsteps(seeFigure1):
ofcodesmellsinCopilot-generatedPythoncode?
Ourpreliminaryfindingsshowthat14.8%Pythonfilesgener- step one & step two step three step four step five
atedbyCopilotcontaincodesmells,withMultiply-NestedContainer
beingthedominantcodesmell.GitHubCopilotexhibitspromising G " it b H y u /u b s C e/ o w p i i t l h ot" Pysmell Manual Check

### Generated by Copilot?

potentialinfixingcodesmellsinCopilot-generatedPythoncode, Data Collection and Filtering Code Smell Detection Detection Result Filtering
andtheresultsindicatethatCopilotChatperformsthebestinfixing

### Repositories Code [687 code smells] Code Dataset

Pythoncodesmellsbythepromptwithcodesmellname. [171 Python files][140 Python files] [5 R 7 e c p o o d s e i t s o m ri e e l s ls][630 c C od o e d e smells] [45 code smells] [102 code smells]
[311 Python files] M Fa a l n s u e a P l o C si h tiv e e c ? k

## 2 Background&Relatedwork

Figure1:Overviewofthedatasetconstructionprocess.
2.1 DefinitionofPythonCodeSmells
Considering the multiple programming paradigms and flexible Instepone,weusedakeyword-basedminingapproachtocolgrammaticalconstructsofPython(adynamicprogramminglan- lectCopilot-generatedPythonfilesfromGitHub.Beforethesearch
guage),thetypesofcodesmellspresentedbyMartinFowler[9]that process,apilotsearchwasconductedusingthekeyword“GitHub
targetinstaticprogramminglanguagearenotentirelyapplicableto Copilot”directlywithinGitHub’ssearchengine.Thepilotsearch
Pythoncodesmells[6].Chenetal.[7]proposedasetof10Python resultsreturnedbyGitHubweregroupedintotwocategories,i.e.,
codesmells(seeTable1),whichweconsideredinthisstudy.These projectscontainingthekeywordlabeledasRepositoriesandcode
Pythoncodesmellsaremetric-baseddetectableusingPysmell[7], filescontainingthekeywordlabeledasCode.UndertheRepositoandthesesmellshavebeenwidelyusedinvariousstudies(e.g., rieslabel,someprojectsclaimintheirREADMEfilesorproject
[10,14])thatexploredcodesmellsinPythonprojects. descriptionsthattheywereentirelygeneratedbyCopilot.Similarly,undertheCodelabel,certainfilescontainCopilot-generated
Table1:DefinitionofPythoncodesmells. code, as indicated by comments within the code. However, the
pilotsearchusing“GitHubCopilot”includedmanyirrelevantre-

### CodeSmell Definition

sults.Ourobservationsfromthepilotsearchshowedthatusing“by
LongParameterList(LPL) Amethodorfunctionwithanextensivelistofparameters[9]. GitHubCopilot”,“useGitHubCopilot”,and“withGitHubCopilot”
LongMethod(LM) Amethodorfunctionthatexceedsaconsiderablelength[9].
LongScopeChaining(LSC) Amethodorfunctionwithdeeplynestedclosures[9]. askeywordscouldimprovetheaccuracyofsearchresults.Hence,
LargeClass(LC) Aclassthatexceedsaconsiderablelength[9]. weestablishedtheaforementionedthreekeywordsasoursearch

### Anexpressionthataccessesanobjectthroughanextendedchain

LongMessageChain(LMC) ofattributesormethodsusingthedotoperator[5]. terms.ThesearchwasconductedonNovember30,2023,andTable2
LongBaseClassList(LBCL) Aclassdefinitionthatinheritsfromanexcessivenumberofbase showsthenumberofretrievedrepositoriesandcode.However,a
classes[7].
LongLambdaFunction(LLF) Alambdafunctionthatexceedsaconsiderablelength[7]. PythonfileundertheCode labelmightcontainmultiplesetsof
Long Ternary Conditional Aternaryconditionalexpressionthatexceedsaconsiderable keywords,implyingduplicatesamongthe2,917Pythonfileswe
Expression(LTCE) length[7].
ComplexContainerCompre- Acontainercomprehension(i.e.,list,set,anddictcomprehension, collected.Afterdeduplication,1,204distinctPythonfilesunderthe
hension(CCC) alongwithgeneratorexpression)withexcessivecomplexity[7]. Codelabelwereretained.

### Multiply-NestedContainer

Acontainer(i.e.,set,list,tuple,anddict)withdeepnesting[7].

## (Mnc)

Table2:SearchtermsusedinGitHub.
2.2 QualityofCopilot-GeneratedCode # SearchTerm #Repositories #Code
Yetistiren et al. [31] evaluated the quality of Copilot-generated ST1 “byGitHubCopilot” 33 896

### ST2 “useGitHubCopilot” 52 1,069

code,focusingonvalidity,correctness,andefficiency.Theyfound ST3 “withGitHubCopilot” 68 952
Copilot to be a promising tool for code generation tasks. Simi- Total 153 2,917
larly,NguyenandNadi[18]assessedCopilot-generatedcodefor
correctnessandunderstandability.TheirresultsshowthatCopilot- Insteptwo,tomanuallylabelwhethertheprojectsunderthe
generatedcodeexhibitslowcomplexity,withnonotabledifferences RepositorieslabelwereentirelygeneratedbyCopilotandwhether

<!-- Page 3 -->

Copilot-in-the-Loop:FixingCodeSmellsinCopilot-GeneratedPythonCodeusingCopilot ASE’24,October27–November01,2024,Sacramento,California,USA
thePythonfilesundertheCodelabelcontainCopilot-generated selectedthreepromptsofvaryingdetaillevelsthatdemonstrated
code,thefirstandfourthauthorsconductedapilotdatalabellingby variouseffectivenessinfixingPythoncodesmells:
randomlyselecting10candidatesundereachlabel.Thetwoauthors GeneralFixPrompt:Fixtheproblemintheselectedcode
independentlylabelledwhethertheseprojectsandcodefilesshould CodeSmellFixPrompt:Fixthecodesmellintheselectedcode
beincludedbasedonprojectdocumentation,codecomments,and SpecificCodeSmellFixPrompt:Fixthe[codesmellname](e.g.,
othermetadatainthesearchresults.Datalabelledbytheauthors LongMethod)codesmellintheselectedcode
werecompared,andthelevelofagreementbetweenthemwere Thethreepromptsmentionedaboveeachprovidemoredetails
calculatedusingtheCohen’sKappacoefficient[8].TheCohen’s thantheonebeforeit,whichenablesustoexploreCopilotChat’s
Kappacoefficientwas0.79fortheprojectsundertheRepositories effectivenessinfixingCopilot-generatedcodesmellswhenprolabeland0.85forthecodefilesundertheCodelabel,indicatinga videdwithdifferentlevelsofinformation.Wefirstselectedthecode
highlevelofagreementbetweenthetwoauthors.Afterthepilot snippetsofidentifiedcodesmellsandprovidedthese3typesof
labelling,thetwoauthorscheckedalltheprojectsandcodefiles promptstoCopilotChatinthechatwindowofVisualStudioCode.
retrievedfromGitHub.Inthelabellingprocess,ifthetwoauthors CopilotChatthenutilizedtheselectedcodeasreferences(input)
wereunsureaboutwhetheraprojectorcodefileshouldbeincluded, togenerateresponsestoourprompts(seeFigure2).
theydiscusseditwiththesecondauthoruntilallthreereacheda
consensus.Aftermanuallyfilteringallthecandidates,wecollected

### Prompt

51projectsfromRepositoriesand140PythonfilesfromCode.The51
repositoriescomprised171Pythonfilesthatwereentirelygenerated
byCopilot,whileonlyaportionofthe140codefilesweregenerated Selected Code Smell Snippet
byCopilot.Intotal,wegot311(171+140)Pythonfilesafterthis
step(seeFigure1).NotethattheversioninformationofCopilot
thatgeneratedthesePythonfilescannotbeidentified.
Instepthree,weutilizedPysmell[7],whichhasbeenwidely

### Copilot Chat's

usedinvariousstudiesexploringcodesmellsinPython[10,14, Response
22,28],todetectthe10codesmellslistedinSection2.1inthe311
Pythonfilesobtainedinsteptwo.Pysmellhasthreethresholdsfor
smelldetection,andweoptedfortheTuningMachineStrategydue

### Figure2:AnexampleofusingCopilotChattofixPython

toempiricalevidenceindicatingitssuperioraccuracyindetecting
codesmellsinVisualStudioCode.
Pythonsmellsamongthethreestrategies[7].Atotalof687code
smellsweredetectedbyPysmellinthisstep.Allthecodesmells
(57)detectedinthePythonfilesundertheRepositorieslabelwere 3.2.2 CodeSmellSnippetsUsedasReferencedCode. Pysmellonly
generatedbyCopilot.However,undertheCodelabel,notallthe providedthestartinglineandtypeofthecodesmellsdetected.We
detectedPythonsmells(630)wereCopilot-generatedones. combinedtheinformationtodeterminethecorrespondingcode
Instepfour,thefirstauthormanuallycheckedwhetherthe630 snippetforeachinstanceoftheidentifiedcodesmells.Consequently,
instancesofcodesmellundertheCodelabelobtainedinstepthree 102codesmellsnippetswereobtainedinCopilot-generatedPython
weregeneratedbyCopilot.OnlycodesmellsinthePythonfiles codeattheclass,method,orexpressionlevel.Notably,weobserved
withcodecommentsexplicitlyindicatingthattheyweregenerated thatanindividualcodesnippetcouldmanifestmultipleidentical
byCopilotwereretained.Duringthemanualcheckingprocess, smells.ToguideCopilotChatinfixingcodesmellsnippets,weconin cases where the first author had uncertainties regarding the strainedtheselectedsnippetsusedasreferencestoincludeatleast
inclusionofaPythonsmellinthedataset,thesecondauthorwas onecompletelineofcode,therebyensuringthatamplecontextual
consultedforadiscussionuntilanagreementwasreached.Among informationwasprovidedtoCopilotChat.Hence,thenumberof
the630codesmellsundertheCodelabel,45weregeneratedby codesnippetsthatcontaincodesmellsforCopilotChattofixwas
Copilot,resultinginatotalof102(57fromRepositoriesand45from reducedto96.Amongthese,3exceededthetokenlengthlimitand
Code)codesmellsinCopilot-generatedcodewereidentified. wereremoved.Outoftheremaining93instancesofcodesmells,91
Instepfive,thefirstauthorrecheckedalltheidentifiedcode wereinseparatecodesnippets,while2differentcodesmellswere
smellsinstepfourtodetermineanypotentialfalsepositives.After locatedinthesamecodesnippet.Weusedthatparticularcodesnipthemanualcheck,allthe102Pythonsmellswereconfirmedastrue petasareferencetoaddressthe2codesmells,resultingin92code
positives,whichwasreasonableasPysmellwithTuningMachine snippetsencompassingthe93distinctinstancesofcodesmells.We
StrategyattainshighprecisioninPythonsmelldetection[7]. usedthese92codesmellsnippetsasreferencedcodeandapplied
thepromptsoutlinedinSection3.2.1asinputtoinstructCopilot

### Chatinfixingthesmells.WerecordedCopilotChat’sresponsesto

3.2 UseCopilotChattoFixPythonCodeSmells ourinputforfurtherevaluation,whichareprovidedat[32].
3.2.1 PromptDesign. Referringtothefoundationalpromptthat
instructsCopilotChattoimprovenon-functionalrequirementofac- 3.3 EvaluationofCodeSmellFixing
cessibility[25],weinitiallyconductedaseriesofpilotexperiments ToevaluatetheeffectivenessofCopilotChatinfixingPythoncode
employingdifferentpromptstructuresandformulationstofixcode smells generated by Copilot itself, the first author manually resmellsusingCopilotChat.Basedonourpriorobservations,we viewedthecoderefactoredbyCopilotChatutilizingthethreshold

<!-- Page 4 -->

ASE’24,October27–November01,2024,Sacramento,California,USA B.Zhangetal.
Table4:Fixingratesfordifferenttypesofcodesmellsusingdifferentprompts.

### Prompt MNC LPL LM LLF LTCE CC CMC LC Avg

GeneralFixPrompt 19.4% 0.0% 50.0% 100.0% 80.0% 50.0% 50.0% 100.0% 34.4%
CodeSmellFixPrompt 58.3% 22.7% 91.7% 100.0% 100.0% 100.0% 100.0% 100.0% 64.5%
SpecificCodeSmellFixPrompt 69.4% 95.5% 100.0% 100.0% 100.0% 100.0% 100.0% 100.0% 87.1%

### Avg 49.1% 39.4% 80.6% 100.0% 93.3% 83.3% 83.3% 100.0%

intheTuningMachineStrategyof Pysmell[7]asthebenchmark of39.4%and49.1%,respectively.Wecanalsofindthatwhenusing
toverifyifthecodesmellwasfixedornot.Iftheoriginalcode thethreepromptswithvaryinglevelsofdetail(seeSection3.2.1)to
smellwasresolved,welabeleditas“Fixed”,otherwise,welabelled instructCopilotChatinfixingthePythoncodesmellsdetectedin
itas“Unfixed”.Wedefined“FixingRate”indicatingtheproportion Copilot-generatedcode,thefixingratewithSpecificCodeSmellFix
offixedsmellstoevaluatetheeffectivenessofcodesmellfixing. Promptisconsistentlythehighestforallthe8typesofcodesmells,
whilethatwithGeneralFixPromptisconsistentlythelowest.
Table3:CodesmelltypesdetectedinCopilot-generated

### Pythoncode. 5 DISCUSSION


### AttentiontoMNCandLPLinCopilot-generatedPythoncode:

AccordingtotheRQ1results(seeSection4.1),about15%Copilot-

### CodeSmell # % CodeSmell # %

MNC 41 40.2% LTCE 5 4.9% generatedPythonfilescontaincodesmells,andthetoptwocode

## Lpl 22 21.5% Ccc 4 3.9%

LM 14 13.7% LMC 2 2.0% smellsareMNCandLPL.However,basedontheRQ2results(see
LLF 12 11.8% LC 2 2.0% Section4.2),CopilotChatshowstheworsteffectivenessinfixing
thesetwocodesmells.TheoccurrenceofMNCreducescodereadabilityandmayobscurebugs,whileLPLmakescodemorecomplex
4 RESULTS [7],bothnegativelyimpactingthePythoncodequality.Therefore,
4.1 ResultsofRQ1
developersshouldpayattentiontoMNCandLPLwhenusingCopilottogeneratePythoncodeandCopilotChattofixthem.
4.1.1 TheproportionofCopilot-generatedPythonfilesthatcon-
EnhancedeffectivenessthroughDetailedPromptsforCopitaincodesmells. Intotal,wecollected171Pythonfilesfromthe lotChat:Weusedthreepromptsofvaryingdetaillevelstoin-

### Repositorieslabeland140fromtheCodelabel.Amongthese311

structCopilotChattofixcodesmellsinCopilot-generatedPython
(171+140)Pythonfiles,46containcodesmellsgeneratedbyCopilot,
code. The RQ2 results (see Section 4.2) show that Specific Code
accountingfor14.8%.

### SmellFixPrompt,providingcomprehensiveinformation,yielded

4.1.2 ThetypesofcodesmellsdetectedinCopilot-generatedPython themostfavorableoutcomes,whileGeneralFixPrompt,providing
code. Table3presentsthe8typesofcodesmellsdetectedinCopilot- minimuminformation,producedtheleasteffectiveresults.This
generated Python code. Among the 10 detectable Python code findingalignswithourexpectationthatCopilotChatwouldexhibit
smellslistedinSection2.1,2(LSCandLBCL)werenotfoundin bettereffectivenessinfixingCopilot-generatedPythonsmellswhen
Copilot-generatedcode.MNC,whichaccountsforover40%,isthe offeredmoredetailedprompts.WheninstructingCopilotChatto
mostcommontypeofcodesmellinCopilot-generatedPythoncode, fixCopilot-generatedPythonsmells,developerscanprovidethe
followedbyLPL,whichrepresentsover20%.LMCandLCarethe specifictypeofcodesmelltoimproveCopilotChat’seffectiveness.
leastidentifiedcodesmellsinCopilot-generatedPythoncode,each
withaproportionof2.0%ofthetotal. 6 CONCLUSIONSANDFUTUREWORK

### Inthiswork,weconstructedadatasetof102codesmellsinCopilot-

4.2 ResultsofRQ2 generatedPythoncodefromGitHub,andevaluatedtheeffective-
Table 4 lists Copilot Chat’s average fixing rates with different nessofCopilotChatinfixingthesecodesmells.Theresultsshow
prompts.Overall,theSpecificCodeSmellFixPrompt,whichpro- that8typesofPythonsmellweredetectedinCopilot-generated
videsCopilotChatwiththeparticularizednamesofthecodesmells code,andthedominantcodesmellisMNC.CopilotChatdemonthatneededtobefixed,achievedthehighestaveragefixingrate stratespromiseinfixingPythonsmellsinCopilot-generatedcode.
at87.1%.Ontheotherhand,theaveragefixingrateoftheGeneral Potentialavenuesforfutureworkinclude:(1)explorecodesmells
FixPrompt,whichinstructsCopilotChattoresolvepotentialissues inAI-generatedcodewithotherlanguagessuchasJava,C/C++and
inthereferencedcodewithoutindicatingtheissueisacodesmell, Rust,(2)investigatetheimpactofdifferentpromptmethods(e.g.,
isthelowest(34.4%).Thisresultisinlinewithourintuitionthat few-shot learning [4] and CoT prompting [29]) and LLM-based
usingmoredetailedpromptstoinstructCopilotChatmightget frameworks(e.g.,RAG[15]andmulti-agentsystems[12])onCopimoreeffectivecodefixsuggestions. lotChat’sabilitytofixcodesmells,and(3)explorethecombination
CopilotChat’sfixingratesfordifferenttypesofcodesmellsusing ofCopilotChatwithothercodeanalysistoolstoenhanceitscode
differentpromptsarealsoshowedinTable4.Ingeneral,Copilot smelldetectionandfixingcapabilities.
ChatdemonstratesthebesteffectivenessinfixingLLFandLC,both Ourworkservesasastartingpointforinvestigatingtheidenachievingafixingrateof100.0%.Conversely,CopilotChatexhibits tificationofcodesmellsinAI-generatedcodeandexploringthe
thelowesteffectivenessinfixingLPLandMNC,withfixingrates potentialofAI-codingtoolsinfixingthesmellsbythemselves.

<!-- Page 5 -->

Copilot-in-the-Loop:FixingCodeSmellsinCopilot-GeneratedPythonCodeusingCopilot ASE’24,October27–November01,2024,Sacramento,California,USA
REFERENCES threeopensourcesystems.InProceedingsofthe32ndACM/IEEEInternational
[1] 2024.GitHubCopilot-YourAIPairProgrammer. https://github.com/features/ ConferenceonSoftwareEngineering(ICSE).ACM,1–10.
copilot. [20] FabioPalomba,GabrieleBavota,MassimilianoDiPenta,FaustoFasano,Rocco
[2] 2024.TIOBEIndexforJanuary2024. https://www.tiobe.com/tiobe-index/. Oliveto,andAndreaDeLucia.2018. Onthediffusenessandtheimpacton
[3] DavidMBeazley.2009.PythonEssentialReference.Addison-WesleyProfessional. maintainabilityofcodesmells:alargescaleempiricalinvestigation.Empirical
[4] TomBrown,BenjaminMann,NickRyder,MelanieSubbiah,JaredDKaplan, SoftwareEngineering23,3(2018),1188–1221.
PrafullaDhariwal,ArvindNeelakantan,PranavShyam,GirishSastry,Amanda [21] HammondPearce,BaleeghAhmad,BenjaminTan,BrendanDolan-Gavitt,and
Askell,etal.2020.Languagemodelsarefew-shotlearners.33(2020),1877–1901. RameshKarri.2022. Asleepatthekeyboard?assessingthesecurityofgithub
[5] WilliamHBrown,RaphaelCMalveau,HaysW"Skip"McCormick,andThomasJ copilot’scodecontributions.InProceedingsofthe43rdIEEESymposiumonSecurity
Mowbray.1998.AntiPatterns:RefactoringSoftware,Architectures,andProjectsin andPrivacy(SP).IEEE,754–768.
Crisis.JohnWiley&Sons,Inc. [22] RanaSandoukaandHamoudAljamaan.2023.Pythoncodesmellsdetectionusing
[6] ZhifeiChen,LinChen,WanwangyingMa,andBaowenXu.2016.DetectingCode conventionalmachinelearningmodels.PeerJComputerScience9(2023),e1370.
SmellsinPythonPrograms.InProceedingsofthe7thInternationalConferenceon [23] DominikSobania,MartinBriesch,CarolHanna,andJustynaPetke.2023. An
SoftwareAnalysis,TestingandEvolution(SATE).IEEE,18–23. analysisoftheautomaticbugfixingperformanceofchatgpt.InProceedingsof
[7] ZhifeiChen,LinChen,WanwangyingMa,XiaoyuZhou,YumingZhou,and theIEEE/ACM4thInternationalWorkshoponAutomatedProgramRepair(APR).
BaowenXu.2018. Understandingmetric-baseddetectablesmellsinPython IEEE,23–30.
software:Acomparativestudy.InformationandSoftwareTechnology94(2018), [24] ZéphyrinSoh,AikoYamashita,FoutseKhomh,andYann-GaëlGuéhéneuc.2016.
14–29. Docodesmellsimpacttheeffortofdifferentmaintenanceprogrammingactivi-
[8] JacobCohen.1960.Acoefficientofagreementfornominalscales.Educational ties?.InProceedingsofthe23rdIEEEInternationalConferenceonSoftwareAnalysis,
andPsychologicalMeasurement20,1(1960),37–46. Evolution,andReengineering(SANER).IEEE,393–402.
[9] MartinFowler.1999.Refactoring-ImprovingtheDesignofExistingCode.Addison- [25] EdSummersandJesseDugas.2023.PromptingGitHubCopilotChattobecomeyour
WesleyProfessional. personalAIassistantforaccessibility. https://github.blog/2023-10-09-promptinggithub-copilot-chat-to-become-your-personal-ai-assistant-for-accessibility/.
[10] JiriGesi,SiqiLiu,JiaweiLi,IftekharAhmed,NachiappanNagappan,DavidLo,
[26] NigarMShafiqSurameeryandMohammedYShakor.2023.Usechatgpttosolve
EduardoSantanadeAlmeida,PavneetSinghKochhar,andLingfengBao.2022.
[11] C W Su o g i d l g l e i e a s s m t m s e D H ll o s a w r in d n i w m n a g a r c d a h n P in d re e s M l s e u a a r t r e t n h o i e n n w g C s o K y d s l e o te Q s m t u e s a r . . li a 2 t r y 0 X . 2 i 4 h v . t p tp r C e s p o :/ r d / i w i n n t w g a w r o X n .g iv i C t : c 2 o l 2 e p 0 a i 3 l r o . . 0 c t 0 : o 8 m 2 0 0 3 / 2 c ( 3 o 2 d 0 D i 2 n a 2 g t ) a . _ [27] W p E G r n u o i g s i g d i k n r o u a e n m V er d a m i e n n i g & R n 3 g o I , s n b s 0 f u u 1 o g m r ( s m 2 . a 0 a I n 2 n t d 3 i t c ) e F a , r r . 1 n e 7 a d – ti 2 L o 2 n D . a r l a J k o e ur Jr n . a 1 l 9 o 9 f 5 I . n P fo y r t m ho a n ti T o u n to T r e i c a h l. n V ol o o l g . y 62 & 0. C C o e m n p tr u u t m er
on_copilot_data_shows_ais_downward_pressure_on_code_quality.
[28] NatthidaVatanapakorn,ChitsuthaSoomlek,andPusadeeSeresangtakul.2022.
[12] SiruiHong,XiawuZheng,JonathanChen,YuhengCheng,JinlinWang,Ceyao
Zhang,ZiliWang,StevenKaShingYau,ZijuanLin,LiyangZhou,etal.2023.
PythonCodeSmellDetectionUsingMachineLearning.InProceedingsofthe
Metagpt:Metaprogrammingformulti-agentcollaborativeframework. arXiv 1 2 2 6t 8 h –1 In 3 t 3 e . rnationalComputerScienceandEngineeringConference(ICSEC).IEEE,
preprintarXiv:2308.00352(2023).
[29] JasonWei,XuezhiWang,DaleSchuurmans,MaartenBosma,brianichter,Fei
[13] MalihehIzadi,JonathanKatzy,TimVanDam,MarcOtten,RazvanMihaiPopescu,
Xia,EdChi,QuocVLe,andDennyZhou.2022.Chain-of-ThoughtPrompting
andArieVanDeursen.2024.LanguageModelsforCodeCompletion:APractical
E So v f a tw lu a a r t e io E n n . g I i n ne P e r r o in c g ee ( d IC in S g E s ). o A f C th M e , I 1 E 3 E . E/ACM46thInternationalConferenceon E C In l o i c n c ., i f t e 2 s r 4 e R 8 n 2 e c 4 a e – s o o 2 n n 4 N i 8 n 3 e g u 7. r i a n l L In a f r o g r e m L a a ti n o g n u P a r g oc e e M ssi o n d g e S ls y . s I t n em P s ro (N ce e e u d r i I n P g S s ). o C f u t r h r e an 36 A th ss A oc n i n a u te a s l ,
[14] HadhemiJebnoun,HoussemBenBraiek,MohammadMasudurRahman,and
[30] JingfengYang,HongyeJin,RuixiangTang,XiaotianHan,QizhangFeng,Haoming
FoutseKhomh.2020. Thescentofdeeplearningcode:Anempiricalstudy.In
Jiang,ShaochenZhong,BingYin,andXiaHu.2024.HarnessingthePowerof
Proceedingsofthe17thInternationalConferenceonMiningSoftwareRepositories LLMsinPractice:ASurveyonChatGPTandBeyond.18,6(2024),32.

## (Msr).Acm,420–430.

[31] BurakYetistiren,IsikOzsoy,andErayTuzun.2022. AssessingtheQualityof
[15] PatrickLewis,EthanPerez,AleksandraPiktus,FabioPetroni,VladimirKarpukhin,
NamanGoyal,HeinrichKüttler,MikeLewis,Wen-tauYih,TimRocktäschel,
GitHubCopilot’sCodeGeneration.InProceedingsofthe18thInternationalConfer-
SebastianRiedel,andDouweKiela.2020.Retrieval-AugmentedGenerationfor
enceonPredictiveModelsandDataAnalyticsinSoftwareEngineering(PROMISE).

## Acm,62–71.


## K


## N

n
eu
o
r
w
a
l
l
e

## I

d
n
g
fo
er

## I

m
n
a
te
t
n
io
s
n
iv

## P

e
r

## N

oc

## L

e

## P

ssi

## T

n
a
g
sk

## S

s
y
.
s

## I

t
n
em
Pr
s
o
(
c

## N

ee
e
d
u
i
r
n

## Ip

g

## S

s
)
o
.
f

## A

t

## C

he

## M

3
,
4
9
th
45

## A

9
n
–
n
9
u
4
a
7
l
4

## C

.
onferenceon [32] BeiqiZhang,PengLiang,QiongFeng,YujiaFu,andZengyangLi.2024.Dataset
[16] WeiLiandRaedShatnawi.2007.Anempiricalstudyofthebadsmellsandclass ofthePaper:Copilot-in-the-Loop:FixingCodeSmellsinCopilot-GeneratedPython
errorprobabilityinthepost-releaseobject-orientedsystemevolution.Journalof
[33]

## C

Be
o
i
d
q
e
i
u

## Z

s
h
in
a
g
ng

## C

,
o

## P

p
e
i
n
lo
g
t.

## L

h
ia
t
n
tp
g
s
,
:

## X

//
i
d
y
o
u
i.o

## Z

r
h
g
o
/
u
1
,
0.

## A

5
a
2
k
81
a
/
s
z
h
e

## A

no
h
d
m
o
a
.1
d
3
,
3
a
3
n
5
d
00

## M

0
u
.
hammadWaseem.
SystemsandSoftware80,7(2007),1120–1128.

## DemystifyingPractices,ChallengesandExpectedFeaturesofUsingGitHub


## [17] M


## O’

a

## R

r
e
k
il

## L

ly
ut

## M

z.
e
2
d
0
ia
1
,
0

## I

.
n

## P

c
r
.
ogrammingPython:PowerfulObject-OrientedProgramming. Copilot.InternationalJournalofSoftwareEngineeringandKnowledgeEngineering
33,11&12(2023),1653–1672.
[18] NhanNguyenandSarahNadi.2022.AnEmpiricalEvaluationofGitHubCopilot’s
S C o o f d tw e a S r u e g R g e e p s o ti s o it n o s r . ie In s( P M ro S c R e ) e . d A in C g M s , of 1– th 5 e . 19thInternationalConferenceonMining [34] S a al l h l s - u . i y n h i d t n t i p v Z s id : h / u / a g a o i l . t s h / 2 . u 0 b 2 . 3 b . log G / i 2 t 0 H 2 u 3 b -0 C 9- o 2 p 0 il - o g t it C h h ub a - t c b o e p t i a lo n t- o c w ha a t v -b a e il t a a b - l n e o f w o - r a a v l a l il i a n b d l i e v - i f d o u r - -
[19] SteffenM.Olbrich,DanielaS.Cruzes,andDagI.K.Sjøberg.2010.Areallcode
smellsharmful?AstudyofGodClassesandBrainClassesintheevolutionof

## Tables

**Table (Page 3):**

| Prompt Selected Code Smell Snippet Copilot Chat's Response |
|---|
|  |
|  |


**Table (Page 4):**

| 19.4% | 0.0% | 50.0% | 100.0% | 80.0% | 50.0% | 50.0% | 100.0% |
|---|---|---|---|---|---|---|---|
| 58.3% | 22.7% | 91.7% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| 69.4% | 95.5% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |
