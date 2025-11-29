---
title: "The Prompt Report Systematic Survey"
original_file: "./01_The_Prompt_Report_Systematic_Survey.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["prompt-engineering", "llm", "rag", "chain-of-thought", "react"]
keywords: ["prompt", "page", "prompting", "shot", "language", "wang", "zhang", "models", "thought", "llm"]
summary: "<!-- Page 1 -->

The Prompt Report: A Systematic Survey of Prompt Engineering

### Techniques

SanderSchulhoff1,2∗ MichaelIlie1∗ NishantBalepur1 KonstantineKahadze1
AmandaLiu1 ChengleiSi4 YinhengLi5 AayushGupta1 HyoJungHan1 SevienSchulhoff1
PranavSandeepDulepet1 SauravVidyadhara1 DayeonKi1 SwetaAgrawal12 ChauPham13
GersonKroiz FeileenLi1 HudsonTao1 AshaySrivastava1 HevanderDaCosta1 SaloniGupta1
MeganL.Rogers8 InnaGoncearenco9 GiuseppeSarli9,10 IgorGalynker11
DenisPeskoff7 MarineCarpuat1 JulesWhi"
related_documents: []
---

# The Prompt Report Systematic Survey

<!-- Page 1 -->

The Prompt Report: A Systematic Survey of Prompt Engineering

### Techniques

SanderSchulhoff1,2∗ MichaelIlie1∗ NishantBalepur1 KonstantineKahadze1
AmandaLiu1 ChengleiSi4 YinhengLi5 AayushGupta1 HyoJungHan1 SevienSchulhoff1
PranavSandeepDulepet1 SauravVidyadhara1 DayeonKi1 SwetaAgrawal12 ChauPham13
GersonKroiz FeileenLi1 HudsonTao1 AshaySrivastava1 HevanderDaCosta1 SaloniGupta1
MeganL.Rogers8 InnaGoncearenco9 GiuseppeSarli9,10 IgorGalynker11
DenisPeskoff7 MarineCarpuat1 JulesWhite6 ShyamalAnadkat3 AlexanderHoyle1 PhilipResnik1
1 UniversityofMaryland2 LearnPrompting 3 OpenAI 4 Stanford 5 Microsoft 6 Vanderbilt 7 Princeton
8 TexasStateUniversity 9 IcahnSchoolofMedicine 10 ASSTBrianza
11 MountSinaiBethIsrael 12 InstitutodeTelecomunicações 13 UniversityofMassachusettsAmherst
sschulho@umd.edu milie@umd.edu resnik@umd.edu

### Abstract

GenerativeArtificialIntelligence(GenAI)systemsareincreasinglybeingdeployedacrossdiverseindustries
andresearchdomains. Developersandend-usersinteractwiththesesystemsthroughtheuseofprompting
andpromptengineering. Althoughpromptengineeringisawidelyadoptedandextensivelyresearchedarea,
itsuffersfromconflictingterminologyandafragmentedontologicalunderstandingofwhatconstitutes
an effective prompt due to its relatively recent emergence. We establish a structured understanding of
promptengineeringbyassemblingataxonomyofpromptingtechniquesandanalyzingtheirapplications.
Wepresentadetailedvocabularyof33vocabularyterms,ataxonomyof58LLMpromptingtechniques,
and40techniquesforothermodalities. Additionally,weprovidebestpracticesandguidelinesforprompt
engineering,includingadviceforpromptingengineeringChatGPTandotherstate-of-the-art(SOTA)LLMs.
We further present a meta-analysis of the entire literature on natural language prefix-prompting. As a
culminationoftheseefforts,thispaperpresentsthemostcomprehensivesurveyonpromptengineeringto
date.
1
5202
beF
62
]LC.sc[
6v80660.6042:viXra

<!-- Page 2 -->


### Contents

1 Introduction 4 4.1.4 RetrievalAugmentedGen-
1.1 WhatisaPrompt? . . . . . . . . . 5 eration(RAG) . . . . . . 25
1.2 Terminology . . . . . . . . . . . . 5 4.2 Evaluation . . . . . . . . . . . . . 26
1.2.1 ComponentsofaPrompt . 5 4.2.1 PromptingTechniques . . 26
1.2.2 PromptingTerms . . . . . 6 4.2.2 OutputFormat . . . . . . 27
1.3 AShortHistoryofPrompts . . . . 7 4.2.3 PromptingFrameworks . . 27
4.2.4 OtherMethodologies . . . 27
2 AMeta-AnalysisofPrompting 8
5 PromptingIssues 29
2.1 SystematicReviewProcess . . . . 8
5.1 Security . . . . . . . . . . . . . . 29
2.1.1 ThePipeline . . . . . . . 8
5.1.1 TypesofPromptHacking. 29
2.2 Text-BasedTechniques . . . . . . 8
5.1.2 RisksofPromptHacking . 29
2.2.1 In-ContextLearning(ICL) 8
5.1.3 HardeningMeasures . . . 30
2.2.2 ThoughtGeneration . . . 12
5.2 Alignment . . . . . . . . . . . . . 31
2.2.3 Decomposition . . . . . . 13
5.2.1 PromptSensitivity . . . . 31
2.2.4 Ensembling . . . . . . . . 14
5.2.2 Overconfidence and Cali-
2.2.5 Self-Criticism . . . . . . . 15
bration . . . . . . . . . . 31
2.3 PromptingTechniqueUsage . . . 16
5.2.3 Biases, Stereotypes, and
2.3.1 Benchmarks. . . . . . . . 16

### Culture . . . . . . . . . . 32

2.4 PromptEngineering . . . . . . . . 16
5.2.4 Ambiguity . . . . . . . . 32
2.5 AnswerEngineering . . . . . . . 18
2.5.1 AnswerShape . . . . . . 18 6 Benchmarking 33
2.5.2 AnswerSpace . . . . . . . 18 6.1 TechniqueBenchmarking . . . . . 33
2.5.3 AnswerExtractor . . . . . 18 6.1.1 Comparing Prompting

### Techniques . . . . . . . . 33

3 BeyondEnglishTextPrompting 20 6.1.2 QuestionFormats . . . . . 33
3.1 Multilingual . . . . . . . . . . . . 20 6.1.3 Self-Consistency . . . . . 33
3.1.1 Chain-of-Thought(CoT) . 20 6.1.4 EvaluatingResponses . . 34
3.1.2 In-ContextLearning . . . 20 6.1.5 Results . . . . . . . . . . 34
3.1.3 Prompt Template Lan- 6.2 PromptEngineeringCaseStudy . 34
guageSelection . . . . . . 20 6.2.1 Problem . . . . . . . . . . 34
3.1.4 Prompting for Machine 6.2.2 TheDataset . . . . . . . . 35
Translation . . . . . . . . 21 6.2.3 TheProcess . . . . . . . . 35
3.2 Multimodal . . . . . . . . . . . . 22 6.2.4 Discussion . . . . . . . . 42
3.2.1 ImagePrompting . . . . . 22
7 RelatedWork 44
3.2.2 AudioPrompting . . . . . 23
3.2.3 VideoPrompting . . . . . 23
8 Conclusions 45
3.2.4 SegmentationPrompting . 23
3.2.5 3DPrompting . . . . . . . 23 A Appendices 62

### A.1 DefinitionsofPrompting . . . . . 62

4 ExtensionsofPrompting 24 A.2 ExtendedVocabulary . . . . . . . 64
4.1 Agents . . . . . . . . . . . . . . . 24 A.2.1 PromptingTerms . . . . . 64
4.1.1 ToolUseAgents . . . . . 24 A.2.2 PromptEngineeringTerms 64
4.1.2 Code-GenerationAgents . 24 A.2.3 Fine-TuningTerms . . . . 64
4.1.3 Observation-BasedAgents 25 A.2.4 OrthogonalPromptTypes 64
2

<!-- Page 3 -->

A.3 Datasheet . . . . . . . . . . . . . 66 A.6 EvaluationTable . . . . . . . . . 71

### A.3.1 Motivation . . . . . . . . 66

A.7 EntrapmentPromptingProcess . . 72

### A.3.2 Composition . . . . . . . 66

A.7.1 Exploration . . . . . . . . 72

### A.3.3 CollectionProcess . . . . 67

A.3.4 Preprocessing/ Cleaning/ A.7.2 GettingaLabel . . . . . . 72

### Labeling . . . . . . . . . 67 A.7.3 Varying Prompting Tech-

A.3.5 Uses . . . . . . . . . . . . 67 niques . . . . . . . . . . . 72
A.3.6 Distribution . . . . . . . . 67
A.8 FormallyDefiningaPrompt . . . 75

### A.3.7 Maintenance . . . . . . . 67


### A.9 In-Context Learning Definitions

A.4 Keywords . . . . . . . . . . . . . 68
Disambiguation . . . . . . . . . . 77

### A.5 Prompt for Systematic Literature

Review . . . . . . . . . . . . . . 70 A.10 Contributions . . . . . . . . . . . 79
3

<!-- Page 4 -->

1 Introduction
Transformer-basedLLMsarewidelydeployed

### Core Prompting Techniques

inconsumer-facing,internal,andresearchsettings
(Bommasanietal.,2021). Typically,thesemodels Text based Techniques
rely on the user providing an input “prompt” to
which the model produces an output in response. MLT/MMTs are often derived from fundamental
text-based prompting techniques.

### Such prompts may be textual—“Write a poem

Multilingual Techniques Multimodal Techniques
abouttrees.”—ortakeotherforms: images,audio,
*Techniques on text data from *Techniques for processing multimedia
videos, or a combination thereof. The ability to multiple languages (video, audio, etc)
promptmodels,particularlypromptingwithnaturallanguage,makesthemeasytointeractwithand

### Agents

useflexiblyacrossawiderangeofusecases.
Often make use of core prompting techniques

### Knowinghowtoeffectivelystructure,evaluate,

andperformothertaskswithpromptsisessential Safety Evaluation Security
tousingthesemodels. Empirically,betterprompts Safety needs throughout Need a to g e e n v t a l o u u a t t p e u p ts rompt/ Sec t u h r r i o ty u g co h n o c u e t rns
lead to improved results across a wide range of
tasks(Weietal.,2022b;Liuetal.,2023b;Schul- Figure1.1: Categorieswithinthefieldofpromptingare
hoff,2022). Alargebodyofliteraturehasgrown interconnected. Wediscuss7corecategoriesthatare
around the use of prompting to improve results welldescribedbythepaperswithinourscope.
andthenumberofpromptingtechniquesisrapidly
increasing.
inthemodel’svocabulary,whilesoftpromptsmay

### However,aspromptingisanemergingfield,the

containtokensthathavenocorrespondingwordin
useofpromptscontinuestobepoorlyunderstood,
thevocabulary.
withonlyafractionofexistingterminologiesand
Finally,weonlystudytask-agnostictechniques.
techniquesbeingwell-knownamongpractitioners.

### Thesedecisionskeeptheworkapproachabletoless

Weperformalarge-scalereviewofpromptingtechtechnicalreadersandmaintainamanageablescope.
niquestocreatearobustresourceofterminology
and techniques in the field. We expect this to be Sections Overview We conducted a machinethefirstiterationofterminologiesthatwilldevelop assisted systematic review grounded in the
overtime. Wemaintainanup-to-datelistofterms PRISMAprocess(Pageetal.,2021)(Section2.1)
andtechniquesatLearnPrompting.org. toidentify58differenttext-basedpromptingtechniques, fromwhichwecreateataxonomywitha
Scope of Study We create a broad directory of robust terminology of prompting terms (Section
prompting techniques, that can be quickly under- 1.2).
stoodandeasilyimplementedforrapidexperimen- Our goal is to provide a roadmap for the comtationbydevelopersandresearchers. Tothisend, munity when considering which prompting techwelimitourstudytofocusonprefixprompts(Shin niquestouse(Figure1.1). Whilemuchliterature
et al., 2020a) rather than cloze prompts (Petroni onpromptingfocusesonEnglish-onlysettings,we
et al., 2019; Cui et al., 2021), because modern alsodiscussmultilingualtechniques(Section3.1).
LLMtransformerarchitectureswidelyemploypre- Giventherapidgrowthinmultimodalprompting,
fix prompts and provide robust support for both wherepromptsmayincludemediasuchasimages,
developers and researchers (Brown et al., 2020; wealsoexpandourscopetomultimodaltechniques
Google,2023;Touvronetal.,2023). Additionally, (Section3.2). Manymultilingualandmultimodal
we refined our focus to hard (discrete) prompts promptingtechniquesaredirectextensionsofEnratherthansoft(continuous)promptsandleaveout glishtext-onlypromptingtechniques.
papersthatmakeuseoftechniquesusinggradient- As prompting techniques grow more complex,
basedupdates(i.e. fine-tuning). Hardpromptscon- theyhavebeguntoincorporateexternaltools,such
tainonlytokens(vectors)thatcorrespondtowords as Internet browsing and calculators. We use the
4

<!-- Page 5 -->

term"agents"todescribethesetypesofprompting
Writeapoemabouttrees.
techniques(Section4.1).

### It is important to understand how to evaluate

theoutputsofagentsandpromptingtechniquesto Write a poem about the following topic:
ensure accuracy and avoid hallucinations. Thus, {USER_INPUT}
wediscusswaysofevaluatingtheseoutputs(Section 4.2). We also discuss security (Section 5.1)
and safety measures (Section 5.2) for designing Figure1.2: Promptsandprompttemplatesaredistinct
promptsthatreducetheriskofharmtocompanies concepts;aprompttemplatebecomesapromptwhen
inputisinsertedintoit.
andusers.

### Finally,weapplypromptingtechniquesintwo

case studies (Section 6.1). In the first, we test a

### Eachtweetinthedatasetwouldbeinsertedinto

range of prompting techniques against the comaseparateinstanceofthetemplateandtheresulting
monlyusedbenchmarkMMLU(Hendrycksetal.,
promptwouldbegiventoaLLMforinference.
2021). Inthesecond,weexploreindetailanexampleofmanualpromptengineeringonasignificant, 1.2 Terminology
real-worldusecase,identifyingsignalsoffrantic
1.2.1 ComponentsofaPrompt
hopelessness–atopindicatorofsuicidalcrisis–in
the text of individuals seeking support (Schuck There are a variety of common components inet al., 2019a). We conclude with a discussion of cludedinaprompt. Wesummarizethemostcomthenatureofpromptinganditsrecentdevelopment monlyusedcomponentsanddiscusshowtheyfit
(Section8). intoprompts(Figure1.3).
1.1 WhatisaPrompt? Directive Manypromptsissueadirectiveinthe
form of an instruction or question.1 This is the

### ApromptisaninputtoaGenerativeAImodel,that

coreintentoftheprompt,sometimessimplycalled
is used to guide its output (Meskó, 2023; White
the"intent". Forexample,hereisaninstanceofa
et al., 2023; Heston and Khun, 2023; Hadi et al.,
promptwithasingleinstruction:
2023; Brown et al., 2020). Prompts may consist
of text, image, sound, or other media. Some ex-
Tellmefivegoodbookstoread.
amplesofpromptsincludethetext,“writeathree
paragraphemailforamarketingcampaignforan
Directives can also be implicit, as in this oneaccountingfirm”,aphotographofapieceofpaper
shotcase,wherethedirectiveistoperformEnglish
withthewords“whatis10*179”writtenonit,or
toSpanishtranslation:
arecordingofanonlinemeeting,withtheinstructions“summarizethis”. Promptsusuallyhavesome

### Night: Noche

text component, but this may change as non-text

### Morning:

modalitiesbecomemorecommon.
PromptTemplate Promptsareoftenconstructed

### Examples Examples,alsoknownasexemplarsor

via a prompt template (Shin et al., 2020b). A
shots,actasdemonstrationsthatguidetheGenAI
prompttemplateisafunctionthatcontainsoneor
toaccomplishatask. TheabovepromptisaOnemorevariableswhichwillbereplacedbysomeme-
Shot(i.e. oneexample)prompt.
dia(usuallytext)tocreateaprompt. Thisprompt
can then be considered to be an instance of the Output Formatting It is often desirable for the
template. GenAI to output information in certain formats,
Consider applying prompting to the task of bi- forexample,CSV,Markdown,XML,orevencusnary classification of tweets. Here is an initial tomformats(Xiaetal.,2024). Structuringoutputs
prompttemplatethatcanbeusedtoclassifyinputs. mayreduceperformanceonsometasks(Tametal.,
2024). However, Kurt (2024) point out various

### Classifythetweetaspositiveornegative:

1“Directives”,fromSearle(1969),areatypeofspeechact

## {Tweet}

intendedtoencourageanaction,andhavebeeninvokedin
modelsofhuman-computerdialogueMorellietal.(1991).
5

<!-- Page 6 -->


### Context1.2.1


### ContextWindowA.2.1

PrimingA.2.1 In-ContextLearning Few-ShotPrompt2.2.1
PromptingTechnique 2.2.1 Exemplar1.2.2
1.2.2
Zero-ShotPrompt2.2.1.3 ContinuousPrompt
Prompting1.2.2

## A.2.4.2


### DensityA.2.4.2

DiscretePromptA.2.4.2

### UserPromptA.2.4.1


### OrthogonalPromptTypes

A.2.4 OriginatorA.2.4.1 SystemPromptA.2.4.1
PromptChain1.2.2 AssistantPromptA.2.4.1
PromptEngineering PrefixA.2.4.3

### PredictionStyleA.2.4.3

Prompt1.1 Technique1.2.2 ClozeA.2.4.3
PromptTemplate1.1 Meta-Prompting2.4

### Verbalizer2.5.3

PromptEngineering1.2.2 AnswerEngineering
Extractor2.5.3
2.5

### AnswerTrigger2.5.3

ConversationalPrompt
EngineeringA.2.2

### Prompt-Based


### LearningA.2.3


### Fine-TuningA.2.3


### PromptTuningA.2.3

Figure1.3: ATerminologyofprompting. Termswithlinkstotheappendixarenotsufficientlycriticaltodescribein
themainpaper,butareimportanttothefieldofprompting. PromptingtechniquesareshowninFigure2.2
.
flawsinTametal.(2024)andshowthatstructuring positionsotheGenAIcanproperlysigntheemail.
outputsmayactuallyimproveperformance. Here AdditionalInformationissometimescalled‘conisanexampleofhowyoumightformataprompt text‘,thoughwediscouragetheuseofthistermas
tooutputinformationasaCSV: itisoverloadedwithothermeaningsinthepromptingspace2.

## {Paragraph}


### SummarizethisintoaCSV. 1.2.2 PromptingTerms

Terminology within the prompting literature is

### StyleInstructions Styleinstructionsareatypeof

rapidly developing. As it stands, there are many
outputformattingusedtomodifytheoutputstylistipoorlyunderstooddefinitions(e.g. prompt,prompt
callyratherthanstructurally(Section2.2.1.3). For
engineering)andconflictingones(e.g. roleprompt
example:
vspersonaprompt). Thelackofaconsistentvocabulary hampers the community’s ability to clearly
Writeaclearandcurtparagraphaboutlla- describethevariouspromptingtechniquesinuse.
mas. Weprovidearobustvocabularyoftermsusedinthe
promptingcommunity(Figure1.3).3 Lessfrequent
Role ARole,alsoknownasapersona(Schmidt terms are left to Appendix A.2. In order to accuet al., 2023; Wang et al., 2023l), is a frequently ratelydefinefrequently-usedtermslikepromptand
discussedcomponentthatcanimprovewritingand promptengineering,weintegratemanydefinitions
styletext(Section2.2.1.3). Forexample: (AppendixA.1)toderiverepresentativedefinitions.
Pretendyouareashepherdandwritealim- Prompting Prompting is the process of providerickaboutllamas. ing aprompt toa GenAI,which thengenerates a
response. For example, the action of sending a

### AdditionalInformation Itisoftennecessaryto

includeadditionalinformationintheprompt. For
2e.g.thecontextisthetokensprocessedbytheLLMina
forwardpass
example,ifthedirectiveistowriteanemail,you
3Byrobust,wemeanthatitcoversmostexistingcommonly
mightincludeinformationsuchasyournameand usedtermsinthefield.
6

<!-- Page 7 -->

Dataset Inference (i.e. entries x₁ ... xₙ) Exemplar Exemplarsareexamplesofataskbeing completed that are shown to a model in a
x₁ x₂ xₙ
prompt(Brownetal.,2020).
1.3 AShortHistoryofPrompts
Prompt Template The idea of using natural language prefixes, or
prompts, to elicit language model behaviors and
responses originated before the GPT-3 and Chat-
Generative AI GPT era. GPT-2 (Radford et al., 2019a) makes

### Modify Prompt

useofpromptsandtheyappeartobefirstusedin

### Template until

thecontextofGenerativeAIbyFanetal.(2018).

### Desiderata Met

However,theconceptofpromptswasprecededby

### Extractor

relatedconceptssuchascontrolcodes(Pfaff,1979;
Poplack, 1980; Keskar et al., 2019) and writing
promptsinliterature.

### Utility Function


### The term Prompt Engineering appears to have

come into existence more recently from Radford
Figure1.4: ThePromptEngineeringProcessconsistsof etal.(2021)thenslightlylaterfromReynoldsand
threerepeatedsteps1)performinginferenceonadataset
McDonell(2021).
2)evaluatingperformanceand3)modifyingtheprompt
However,variouspapersperformpromptengitemplate. Note that the extractor is used to extract a
neering without naming the term (Wallace et al.,
finalresponsefromtheLLMoutput(e.g. "Thisphrase
is positive" → "positive"). See more information on 2019; Shin et al., 2020a), including Schick and
extractorsinSection2.5. Schütze (2020a,b); Gao et al. (2021) for nonautoregressivelanguagemodels.

### Some of the first works on prompting define a

chunk of text or uploading an image constitutes
prompt slightly differently to how it is currently
prompting.
used. Forexample,considerthefollowingprompt
PromptChain Apromptchain(activity: prompt fromBrownetal.(2020):
chaining)consistsoftwoormoreprompttemplates
usedinsuccession. Theoutputofthepromptgen- TranslateEnglishtoFrench:
erated by the first prompt template is used to pa- llama
rameterizethesecondtemplate,continuinguntilall
templatesareexhausted(Wuetal.,2022). Brownetal.(2020)considertheword"llama"to
betheprompt,while"TranslateEnglishtoFrench:"

### Prompting Technique A prompting technique

is the "task description". More recent papers, inis a blueprint that describes how to structure a
cludingthisone,refertotheentirestringpassedto
prompt,prompts,ordynamicsequencingofmultitheLLMastheprompt.
pleprompts. Apromptingtechniquemayincorporateconditionalorbranchinglogic,parallelism,or
otherarchitecturalconsiderationsspanningmultipleprompts.

### PromptEngineering Promptengineeringisthe

iterativeprocessofdevelopingapromptbymodifyingorchangingthepromptingtechniquethatyou
areusing(Figure1.4).
PromptEngineeringTechnique Apromptengineering technique is a strategy for iterating on a
prompttoimproveit. Inliterature,thiswilloften
beautomatedtechniques(Dengetal.,2022),butin
consumersettings,usersoftenperformpromptengineeringmanually,withoutanyassistivetooling.
7

<!-- Page 8 -->

2 A Meta-Analysis of Prompting
2.1 SystematicReviewProcess
3,677 from arXiv 2,087 from SS, 639 from ACL = 4797 Records
-550

### In order to robustly collect a dataset of sources

for this paper, we ran a systematic literature re- 4,247 Records after Title 1,661 papers human reviewed

### Deduplication

viewgroundedinthePRISMAprocess(Pageetal.,
2021) (Figure 2.1). We host this dataset on Hug-
-316 316 papers excluded
gingFace 4 and present a datasheet (Gebru et al.,
2021)forthedatasetinAppendixA.3. Ourmain 3,931 Records after Human Check if paper contains the

### Review word “prompt”

data sources were arXiv, Semantic Scholar, and
ACL. We query these databases with a list of
-1,579 1,579 papers excluded
44 keywords narrowly related to prompting and
promptengineering(AppendixA.4). 2,352 Records after
removing papers that don’t 1,071 papers AI reviewed
contain the word “prompt”
2.1.1 ThePipeline
-787 787 papers excluded

### In this section, we introduce our data scraping

pipeline, which includes both human and LLM- After The PRISMA Review Process,

1,565 records included in quantitative analysis.
assisted review.5 As an initial sample to establishfilteringcritera,weretrievepapersfromarXiv
Figure2.1: ThePRISMAsystematicliteraturereview
based on a simple set of keywords and boolean
process. We accumulate 4,247 unique records from
rules(A.4). Then,humanannotatorslabelasample
whichweextract1,565relevantrecords.
of1,661articlesfromthearXivsetforthefollowingcriteria:
2.2 Text-BasedTechniques

## Includeifthepaperproposesanovelprompt-

Wenowpresentacomprehensivetaxonomicaloningtechnique.
tologyof58text-basedpromptingtechniques,brokeninto6majorcategories(Figure2.2). Although

## Includeifthepaperstrictlycovershardprefix

someofthetechniquesmightfitintomultiplecateprompts.
gories,weplacetheminasinglecategoryofmost
relevance.

## Exclude if the paper focuses on training by

backpropagatinggradients.
2.2.1 In-ContextLearning(ICL)

### ICLreferstotheabilityofGenAIstolearnskills


## Include if the paper uses a masked frame

andtasksbyprovidingthemwithexemplarsandor
and/orwindowfornon-textmodalities.
relevantinstructionswithintheprompt,withoutthe
need for weight updates/retraining (Brown et al.,
A set of 300 articles are reviewed independently
2020;Radfordetal.,2019b). Theseskillscanbe
bytwoannotators,with92%agreement(Krippenlearnedfromexemplars(Figure2.4)and/orinstrucdorff’sα=Cohen’sκ=81%). Next,wedevelop
tions (Figure 2.5). Note that the word "learn" is
apromptusinggpt-4-1106-previewtoclassifythe
misleading. ICLcansimplybetaskspecification–
remaining articles (Appendix A.5). We validate
the skills are not necessarily new, and can have
the prompt against 100 ground-truth annotations,
alreadybeenincludedinthetrainingdata(Figure
achieving89%precisionand75%recall(foranF1
2.6). SeeAppendixA.9foradiscussionoftheuse
of81%). ThecombinedhumanandLLMannotaof this term. Significant work is currently being
tionsgenerateafinalsetof1,565papers.
done on optimizing (Bansal et al., 2023) and un-
4https://huggingface.co/datasets/PromptSystematicReview/Prom d p e t r _ s S t y a s n te d m in a g tic ( _ S R i ev e i t ew al _ ., D 2 at 0 a 2 se 3 t a;ŠtefánikandKadlcˇík,
5Usinggpt-4-1106-preview 2023)ICL.
8

<!-- Page 9 -->

EmotionPrompting2.2.1.3

### RolePrompting2.2.1.3

StylePrompting2.2.1.3

## S2A2.2.1.3

Zero-Shot2.2.1.3
SimToM2.2.1.3
RaR2.2.1.3

## Re22.2.1.3


### Self-Ask2.2.1.3

ExemplarGeneration SG-ICL2.2.1.2
ExemplarOrdering2.2.1.1

### AnalogicalPrompting

Few-Shot2.2.1 ExemplarSelection KNN2.2.1.2 2.2.2.1
2.2.1.2 Vote-K2.2.1.2 Step-BackPrompting
InstructionSelection2.2.1.1 Zero-ShotCoT2.2.2.1 2.2.2.1
Thread-of-Thought
(ThoT)2.2.2.1

### Tab-CoT2.2.2.1

Chain-of-Thought Active-Prompt2.2.2.2
ThoughtGeneration2.2.2
(CoT)2.2.2
Auto-CoT2.2.2.2

## Cosp2.2.4

Complexity-Based2.2.2.2

## Dense2.2.4

Contrastive2.2.2.2

### DiVeRSe2.2.4

Few-ShotCoT2.2.2.2 Memory-of-Thought
MaxMutual 2.2.2.2

### Information2.2.4

Text-BasePrompt. Tech. Uncertainty-Routed
Meta-CoT2.2.4 CoT2.2.2.2

### Ensembling2.2.4


### MoRE2.2.4 PromptMining2.2.1.2

Self-Consistency2.2.4 AutoDiCoT6.2.3.3

### Universal

Self-Consistency2.2.4

## Usp2.2.4


### PromptParaphrasing2.2.4

Chain-of-Verification2.2.5
Self-Calibration2.2.5

### Self-Refine2.2.5


### Self-Criticism2.2.5

Self-Verification2.2.5

### ReverseCoT2.2.5

CumulativeReason. 2.2.5

## Decomp2.2.3


### FaithfulCoT2.2.3


### Least-to-Most2.2.3


### Plan-and-Solve2.2.3

Decomposition2.2.3 Program-of-Thought2.2.3

### Recurs.-of-Thought2.2.3

Skeleton-of-Thought2.2.3
Tree-of-Thought2.2.3

### Metacognitive2.2.3

Figure2.2: Alltext-basedpromptingtechniquesfromourdataset.
9

<!-- Page 10 -->


## Exemplar Quantity 2. Exemplar Ordering

Include as many exemplars as Randomly order exemplars* 2+2: four
possible*
4+5: nine
Trees are beautiful: Happy
I am so mad: Angry

8+0:
I hate Pizza: Angry
I love life: Happy

Squirrels are so cute: Happy
I hate my boss: Angry

YouTube Ads Suck: Angry
Life is good: Happy

I’m so excited: I’m so excited:
Figure2.4: ICLexemplarprompt
I love life: Happy

Life is good: Happy

Trees are beautiful: Happy

I am so mad: Angry


### I’m so excited:

I hate my boss: Angry

Extract all words that have 3 of the same

### I’m so excited:

letter and at least 3 other letters from the

## Exemplar Label Distribution 4. Exemplar Label Quality

Provide a balanced label Ensure exemplars are labeled followingtext: {TEXT}
distribution* correctly*
I am so mad: Angry
I am so mad: Angry

I love life: Happy
I love life: Happy

I hate my boss: Angry

### I hate my boss: Angry

Figure2.5: ICLinstructionprompt
Life is good: Happy
Life is good: Happy

I’m so excited: I’m so excited:
I am so mad: Angry
I am so mad: Happy

People are so dense: Angry

### I love life: Angry

ExemplarQuantity Increasingthequantityofex-
I hate my boss: Angry
I hate my boss: Angry

emplars in the prompt generally improves model
Life is good: Happy
Life is good: Happy

I’m so excited: I’m so excited: performance,particularlyinlargermodels(Brown

## Exemplar Format 6. Exemplars Similarity et al., 2020). However, in some cases, the bene-


### Choose a common format* Select similar exemplars to

the test instance* fitsmaydiminishbeyond20exemplars(Liuetal.,
2021). In the case of long context LLMs, addi-
Im hyped!: Happy

### Im hyped!: Happy

tionalexemplarscontinuetoincreaseperformance,
Im not very excited: Angry
Im not very excited: Angry

I’m so excited: I’m so excited: though efficiency varies depending on task and
model(Agarwaletal.,2024;Bertschetal.,2024;
Jiangetal.,2024).

### Trees are nice===Happy

Trees are beautiful: Happy

YouTube Ads Suck===Angry
YouTube Ads Suck: Angry


### I’m so excited=== I’m so excited:

ExemplarOrdering Theorderofexemplarsaffectsmodelbehavior(Luetal.,2021;Kumarand
Figure 2.3: We highlight six main design decisions
Talukdar,2021;Liuetal.,2021;Rubinetal.,2022).
whencraftingfew-shotprompts. ∗Pleasenotethatrec-

### Onsometasks,exemplarordercancauseaccuracy

ommendations here do not generalize to all tasks; in
tovaryfromsub-50%to90%+(Luetal.,2021).
somecases,eachofthemcouldhurtperformance.

### Exemplar Label Distribution As in traditional

supervised machine learning, the distribution of

### Few-ShotPrompting (Brownetal.,2020)isthe

exemplarlabelsinthepromptaffectsbehavior. For
paradigm seen in Figure 2.4, where the GenAI
example, if 10 exemplars from one class and 2
learnstocompleteataskwithonlyafewexamples
exemplarsofanotherclassareincluded,thismay
(exemplars). Few-shotpromptingisaspecialcase
causethemodeltobebiasedtowardthefirstclass.
ofFew-ShotLearning(FSL)(Fei-Feietal.,2006;

### Wangetal.,2019), butdoesnotrequireupdating

ExemplarLabelQuality Despitethegeneralbenofmodelparameters
efitofmultipleexemplars,thenecessityofstrictly
valid demonstrationsisunclear. Somework(Min
2.2.1.1 Few-ShotPromptingDesignDecisions
etal.,2022)suggeststhattheaccuracyoflabelsis
Selectingexemplarsforapromptisadifficulttask– irrelevant—providingmodelswithexemplarswith
performancedependssignificantlyonvariousfac- incorrect labels may not negatively diminish pertorsoftheexemplars(Dongetal.,2023),andonly formance. However, under certain settings, there
a limited number of exemplars fit in the typical isasignificantimpactonperformance(Yooetal.,
LLM’scontextwindow. Wehighlightsixseparate 2022). Largermodelsareoftenbetterathandling
design decisions, including the selection and or- incorrectorunrelatedlabels(Weietal.,2023c).
derofexemplarsthatcriticallyinfluencetheoutput Itisimportanttodiscussthisfactor,sinceifyou
quality(Zhaoetal.,2021a;Luetal.,2021;Yeand areautomaticallyconstructingpromptsfromlarge
Durrett,2023)(Figure2.3). datasetsthatmaycontaininaccuracies, itmaybe
10

<!-- Page 11 -->

generatedwithrespecttoDtest attesttime. Here

### Translatetheword"cheese"toFrench. xi

istheprompttemplatewewilluseforthissection,
followingthe‘input: output‘format(Figure2.4):

### Figure 2.6: ICL from training data prompt. In this

version of ICL, the model is not learning a new skill,
{Exemplars}
butratherusingknowledgelikelyinitstrainingset.
Dtest:
xi
necessary to study how label quality affects your
results. Figure2.7: Few-ShotPromptingTemplate

### ExemplarFormat Theformattingofexemplars

alsoaffectsperformance. Oneofthemostcommon K-NearestNeighbor(KNN) (Liuetal.,2021) is
formatsis“Q:{input},A:{label}”,buttheoptimal partofafamilyofalgorithmsthatselectsexemplars
format may vary across tasks; it may be worth similartoDtesttoboostperformance. Althoughefxi
tryingmultipleformatstoseewhichperformsbest. fective,employingKNNduringpromptgeneration
Thereissomeevidencetosuggestthatformatsthat maybetimeandresourceintensive.
occur commonly in the training data will lead to
betterperformance(Jiangetal.,2020). Vote-K (Su et al., 2022) is another method to
selectsimilarexemplarstothetestsample. Inone
Exemplar Similarity Selecting exemplars that stage,amodelproposesusefulunlabeledcandidate
are similar to the test sample is generally bene- exemplars for an annotator to label. In the secficialforperformance(Liuetal.,2021;Minetal., ond stage, the labeled pool is used for Few-Shot
2022). However, in some cases, selecting more Prompting. Vote-Kalsoensuresthatnewlyadded
diverse exemplars can improve performance (Su exemplars are sufficiently different than existing
etal.,2022;Minetal.,2022). onestoincreasediversityandrepresentativeness.
InstructionSelection Whileinstructionsarere-
Self-Generated In-Context Learning (SG-ICL)
quiredtoguideLLMsinzero-shotprompts(Wei
(Kimetal.,2022)leveragesaGenAItoautomatiet al., 2022a), the benefits of adding instructions
callygenerateexemplars. Whilebetterthanzerobeforeexemplarsinfew-shotpromptsislessclear.
shot scenarios when training data is unavailable,
Ajithetal.(2024)showthatgeneric,task-agnostic
thegeneratedsamplesarenotaseffectiveasactual
instructions(i.e.,noinstructionor“Completethe
data.
followingtask:”) improveclassificationandquestion answering accuracy over task-specific ones PromptMining (Jiangetal.,2020) istheprocess
(e.g.,Whatistheanswertothisquestion?) conclud- ofdiscoveringoptimal"middlewords"inprompts
inginstruction-followingabilitiescanbeachieved throughlargecorpusanalysis. Thesemiddlewords
viaexemplarsalone. Whiletheymaynotimprove areeffectivelyprompttemplates. Forexample,incorrectness,instructionsinfew-shotpromptscan steadofusingthecommon"Q:A:"formatforfewstill guide auxiliary output attributes like writing shot prompts, there may exist something similar
style(Royetal.,2023). thatoccursmorefrequentlyinthecorpus. Formats
which occur more often in the corpus will likely
2.2.1.2 Few-ShotPromptingTechniques
leadtoimprovedpromptperformance.
Consideringallofthesefactors,Few-ShotPromptingcanbeverydifficulttoimplementeffectively. More Complicated Techniques such as LENS
WenowexaminetechniquesforFew-ShotPrompt- (Li and Qiu, 2023a), UDR (Li et al., 2023f), and
ing in the supervised setting. Ensembling ap- Active Example Selection (Zhang et al., 2022a)
proachescanalsobenefitFew-ShotPrompting,but leverageiterativefiltering,embeddingandretrieval,
wediscussthemseparately(Section2.2.4). andreinforcementlearning,respectively.

### Assume we have a training dataset, Dtrain,

whichcontainsmultipleinputsDtrain andoutputs 2.2.1.3 Zero-ShotPromptingTechniques
xi
Dtrain, which can be used to few-shot prompt a In contrast to Few-Shot Prompting, Zero-Shot
yi
GenAI(ratherthanperforminggradient-basedup- Promptinguseszeroexemplars. Thereareanumdates). Assumethatthispromptcanbedynamically berofwell-knownstandalonezero-shottechniques
11

<!-- Page 12 -->

aswellaszero-shottechniquescombinedwithan-

### Q: Jack has two baskets, each containing

otherconcept(e.g. ChainofThought),whichwe
threeballs. HowmanyballsdoesJackhave
discusslater(Section2.2.2).
intotal?
Role Prompting (Wang et al., 2023j; Zheng A:Onebasketcontains3balls,sotwobasketscontain3*2=6balls.
et al., 2023d) , also known as persona prompting

## Q:{Question}

(Schmidtetal.,2023;Wangetal.,2023l),assignsa

## A:

specificroletotheGenAIintheprompt. Forexample,theusermightpromptittoactlike"Madonna"
or a "travel writer". This can create more desir-
Figure2.8: AOne-ShotChain-of-ThoughtPrompt.
able outputs for open-ended tasks (Reynolds and

### McDonell,2021)andinsomecasesmayimprove

accuracyonbenchmarks(Zhengetal.,2023d). inreasoningbenchmarks,especiallywithcomplex
questions.
StylePrompting (Luetal.,2023a) involvesspecifyingthedesiredstyle,tone,orgenreintheprompt Self-Ask (Pressetal.,2022) promptsLLMsto
to shape the output of a GenAI. A similar effect firstdecideiftheyneedtoaskfollowupquestions
canbeachievedusingroleprompting. foragivenprompt. Ifso,theLLMgeneratesthese
questions,thenanswersthemandfinallyanswers
EmotionPrompting (Lietal.,2023a) incorpotheoriginalquestion.
ratesphrasesofpsychologicalrelevancetohumans
(e.g., "This is important to my career") into the 2.2.2 ThoughtGeneration
prompt,whichmayleadtoimprovedLLMperfor-
Thoughtgenerationencompassesarangeoftechmanceonbenchmarksandopen-endedtextgeneraniquesthatprompttheLLMtoarticulateitsreasontion.
ingwhilesolvingaproblem(Zhangetal.,2023c).

### System 2 Attention (S2A) (Weston and


### Chain-of-Thought(CoT)Prompting (Weietal.,


### Sukhbaatar, 2023) first asks an LLM to rewrite

2022b) leverages few-shot prompting to encourthepromptandremoveanyinformationunrelated
agetheLLMtoexpressitsthoughtprocessbefore
to the question therein. Then, it passes this new
deliveringitsfinalanswer.6 ThistechniqueisoccapromptintoanLLMtoretrieveafinalresponse.
sionallyreferredtoasChain-of-Thoughts(Tutunov
etal.,2023;Bestaetal.,2024;Chenetal.,2023d).
SimToM (Wilf et al., 2023) deals with compli-
Ithasbeendemonstratedtosignificantlyenhance
catedquestionswhichinvolvemultiplepeopleor
theLLM’sperformanceinmathematicsandreasonobjects. Giventhequestion,itattemptstoestablish
ingtasks. InWeietal.(2022b),thepromptincludes
thesetoffactsonepersonknows,thenanswerthe
anexemplarfeaturingaquestion,areasoningpath,
question based only on those facts. This is a two
andthecorrectanswer(Figure2.8).
promptprocessandcanhelpeliminatetheeffectof
irrelevantinformationintheprompt.
2.2.2.1 Zero-Shot-CoT
RephraseandRespond(RaR) (Dengetal.,2023) ThemoststraightforwardversionofCoTcontains
instructstheLLMtorephraseandexpandtheques- zero exemplars. It involves appending a thought
tion before generating the final answer. For ex- inducing phrase like "Let’s think step by step."
ample, it might add the following phrase to the (Kojima et al., 2022) to the prompt. Other sugquestion: "Rephraseandexpandthequestion,and gested thought-generating phrases include "First,
respond". This could all be done in a single pass let’s think about this logically" (Kojima et al.,
or the new question could be passed to the LLM 2022). Zhouetal.(2022b)usesLLMstogenerate
separately. RaRhasdemonstratedimprovements "Let’s work this out in a step by step way to be
onmultiplebenchmarks. surewehavetherightanswer". Yangetal.(2023a)
searchesforanoptimalthoughtinducer. Zero-Shot-

### Re-reading (RE2) (Xu et al., 2023) adds the

phrase"Readthequestionagain:"tothepromptin 6Wenotethatsuchtechniquesareoftendescribedusing
wordslike"think"thatanthropomorphizemodels.Weattempt
additiontorepeatingthequestion. Althoughthisis
nottousethislanguage,butdouseoriginalauthors’language
suchasimpletechnique,ithasshownimprovement whereappropriate.
12

<!-- Page 13 -->

CoTapproachesareattractiveastheydon’trequire benchmarkforbothGPT-4andGeminiUltramodexemplarsandaregenerallytaskagnostic. els.
Step-BackPrompting (Zhengetal.,2023c) isa Complexity-basedPrompting (Fuetal.,2023b)
modificationofCoTwheretheLLMisfirstasked involvestwomajormodificationstoCoT.First,it
ageneric,high-levelquestionaboutrelevantcon- selects complex examples for annotation and inceptsorfactsbeforedelvingintoreasoning. This clusionintheprompt,basedonfactorslikequesapproachhasimprovedperformancesignificantly tion length or reasoning steps required. Second,
onmultiplereasoningbenchmarksforbothPaLM- during inference, it samples multiple reasoning
2LandGPT-4. chains(answers)andusesamajorityvoteamong
chainsexceedingacertainlengththreshold,under

### AnalogicalPrompting (Yasunagaetal.,2023)

thepremisethatlongerreasoningindicateshigher
issimilartoSG-ICL,andautomaticallygenerates
answerquality. ThistechniquehasshownimproveexemplarsthatincludeCoTs. Ithasdemonstrated
mentsonthreemathematicalreasoningdatasets.
improvementsinmathematicalreasoningandcode
generationtasks.

### ActivePrompting (Diaoetal.,2023) startswith

Thread-of-Thought (ThoT) Prompting (Zhou sometrainingquestions/exemplars,askstheLLM
et al., 2023) consists of an improved thought in- tosolvethem,thencalculatesuncertainty(disagreeducer for CoT reasoning. Instead of "Let’s think ment in this case) and asks human annotators to
stepbystep,"ituses"Walkmethroughthiscontext rewritetheexemplarswithhighestuncertainty.
inmanageablepartsstepbystep,summarizingand
Memory-of-Thought Prompting (Li and Qiu,
analyzingaswego."Thisthoughtinducerworks
2023b) leverageunlabeledtrainingexemplarsto
well in question-answering and retrieval settings,
buildFew-ShotCoTpromptsattesttime. Before
especiallywhendealingwithlarge,complexcontest time, it performs inference on the unlabeled
texts.
training exemplars with CoT. At test time, it re-
TabularChain-of-Thought(Tab-CoT) (Jinand trieves similar instances to the test sample. This
Lu,2023) consistsofaZero-ShotCoTpromptthat techniquehasshownsubstantialimprovementsin
makestheLLMoutputreasoningasamarkdown benchmarks like Arithmetic, commonsense, and
table. ThistabulardesignenablestheLLMtoim- factualreasoning.
prove the structure and thus the reasoning of its
output. AutomaticChain-of-Thought(Auto-CoT)Prompting (Zhangetal.,2022b)usesWeietal.(2022b)’s
2.2.2.2 Few-ShotCoT

### Zero-Shotprompttoautomaticallygeneratechains

ThissetoftechniquespresentstheLLMwithmul- ofthought. ThesearethenusedtobuildaFew-Shot
tipleexemplars,whichincludechains-of-thought. CoTpromptforatestsample.

### Thiscansignificantlyenhanceperformance. This

technique is occasionally referred to as Manual- 2.2.3 Decomposition

### CoT(Zhangetal.,2022b)orGoldenCoT(Deland

Significantresearchhasfocusedondecomposing
Fishel,2023).
complexproblemsintosimplersub-questions. This
ContrastiveCoTPrompting (Chiaetal.,2023) isaneffectiveproblem-solvingstrategyforhumans
addsbothexemplarswithincorrectandcorrectex- aswellasGenAI(Pateletal.,2022). SomedecomplanationstotheCoTpromptinordertoshowthe positiontechniquesaresimilartothought-inducing
LLMhownot toreason. Thismethodhasshown techniques, such as CoT, which often naturally
significant improvement in areas like Arithmetic breaks down problems into simpler components.
ReasoningandFactualQA. However,explicitlybreakingdownproblemscan
furtherimproveLLMs’problemsolvingability.

### Uncertainty-Routed CoT Prompting (Google,

2023) samplesmultipleCoTreasoningpaths,then Least-to-Most Prompting (Zhou et al., 2022a)
selectsthemajorityifitisaboveacertainthresh- startsbypromptingaLLMtobreakagivenprobold(calculatedbasedonvalidationdata). Ifnot,it lemintosub-problemswithoutsolvingthem. Then,
samples greedily and selects that response. This it solves them sequentially, appending model remethoddemonstratesimprovementontheMMLU sponses to the prompt each time, until it arrives
13

<!-- Page 14 -->

at a final result. This method has shown signif- mathematicalandprogramming-relatedtasksbut
icant improvements in tasks involving symbolic islesseffectiveforsemanticreasoningtasks.
manipulation, compositional generalization, and
Faithful Chain-of-Thought (Lyu et al., 2023)
mathematicalreasoning.
generatesaCoTthathasbothnaturallanguageand
Decomposed Prompting (DECOMP) (Khot symbolic language (e.g. Python) reasoning, just
etal.,2022) Few-ShotpromptsaLLMtoshowit likeProgram-of-Thoughts. However,italsomakes
howtousecertainfunctions. Thesemightinclude use of different types of symbolic languages in a
things like string splitting or internet searching; task-dependentfashion.
theseareoftenimplementedasseparateLLMcalls.

### Skeleton-of-Thought (Ningetal.,2023) focuses

Giventhis,theLLMbreaksdownitsoriginalprobonacceleratinganswerspeedthroughparallelizalemintosub-problemswhichitsendstodifferent
tion. Givenaproblem,itpromptsanLLMtocreate
functions. Ithasshownimprovedperformanceover
askeletonoftheanswer,inasense,sub-problems
Least-to-Mostpromptingonsometasks.
tobesolved. Then,inparallel,itsendsthesequestionstoaLLMandconcatenatesalltheoutputsto
Plan-and-SolvePrompting (Wangetal.,2023f)
getafinalresponse.
consists of an improved Zero-Shot CoT prompt,
"Let’s first understand the problem and devise a

### Metacognitive Prompting (Wang and Zhao,

plantosolveit. Then,let’scarryouttheplanand
2024) attempts to make the LLM mirror human
solvetheproblemstepbystep". Thismethodgenermetacognitive processes with a five part prompt
atesmorerobustreasoningprocessesthanstandard
chain,withstepsincludingclarifyingthequestion,
Zero-Shot-CoTonmultiplereasoningdatasets.
preliminaryjudgement,evaluationofresponse,decisionconfirmation,andconfidenceassessment.
Tree-of-Thought(ToT) (Yaoetal.,2023b),also
knownasTreeofThoughts,(Long,2023),createsa
2.2.4 Ensembling
tree-likesearchproblembystartingwithaninitial
InGenAI,ensemblingistheprocessofusingmultiproblemthengeneratingmultiplepossiblestepsin
plepromptstosolvethesameproblem,thenaggretheformofthoughts(asfromaCoT).Itevaluates
gatingtheseresponsesintoafinaloutput. Inmany
theprogresseachstepmakestowardssolvingthe
cases,amajorityvote—selectingthemostfrequent
problem (through prompting) and decides which
response—isusedtogeneratethefinaloutput. Ensteps to continue with, then keeps creating more
semblingtechniquesreducethevarianceofLLM
thoughts. ToTisparticularlyeffectivefortasksthat
outputs and often improving accuracy, but come
requiresearchandplanning.
with the cost of increasing the number of model
Recursion-of-Thought (LeeandKim,2023) is callsneededtoreachafinalanswer.
similartoregularCoT.However,everytimeiten-

### DemonstrationEnsembling(DENSE) (Khalifa

countersacomplicatedprobleminthemiddleofits
et al., 2023) creates multiple few-shot prompts,
reasoningchain,itsendsthisproblemintoanother
eachcontainingadistinctsubsetofexemplarsfrom
prompt/LLMcall. Afterthisiscompleted,theanthetrainingset. Next,itaggregatesovertheiroutswer is inserted into the original prompt. In this
putstogenerateafinalresponse.
way,itcanrecursivelysolvecomplexproblems,includingoneswhichmightotherwiserunoverthat MixtureofReasoningExperts(MoRE) (Sietal.,
maximumcontextlength. Thismethodhasshown 2023d) creates a set of diverse reasoning experts
improvementsonarithmeticandalgorithmictasks. byusingdifferentspecializedpromptsfordifferent
Thoughimplementedusingfine-tuningtooutputa reasoning types (such as retrieval augmentation
specialtokenthatsendssub-problemintoanother promptsforfactualreasoning,Chain-of-Thought
prompt,itcouldalsobedoneonlythroughprompt- reasoningformulti-hopandmathreasoning, and
ing. generatedknowledgepromptingforcommonsense
reasoning). The best answer from all experts is
Program-of-Thoughts (Chenetal.,2023d) uses
selectedbasedonanagreementscore.

### LLMslikeCodextogenerateprogrammingcode

as reasoning steps. A code interpreter executes Max Mutual Information Method (Sorensen
thesestepstoobtainthefinalanswer. Itexcelsin etal.,2022)createsmultipleprompttemplateswith
14

<!-- Page 15 -->

variedstylesandexemplars,thenselectstheopti- PromptParaphrasing (Jiangetal.,2020) transmal template as the one that maximizes mutual formsanoriginalpromptbychangingsomeofthe
information between the prompt and the LLM’s wording,whilestillmaintainingtheoverallmeanoutputs. ing. Itiseffectivelyadataaugmentationtechnique
thatcanbeusedtogeneratepromptsforanensem-
Self-Consistency (Wang et al., 2022) is based
ble.
on the intuition that multiple different reasoning
paths can lead to the same answer. This method
2.2.5 Self-Criticism
first prompts the LLM multiple times to perform
CoT,cruciallywithanon-zerotemperaturetoelicit WhencreatingGenAIsystems,itcanbeusefulto
diverse reasoning paths. Next, it uses a majority haveLLMscriticizetheirownoutputs(Huangetal.,
voteoverallgeneratedresponsestoselectafinal 2022). Thiscouldsimplybeajudgement(e.g.,is
response. Self-Consistency has shown improve- thisoutputcorrect)ortheLLMcouldbeprompted
mentsonarithmetic,commonsense,andsymbolic toprovidefeedback,whichisthenusedtoimprove
reasoningtasks. the answer. Many approaches to generating and
integratingself-criticismhavebeendeveloped.

### UniversalSelf-Consistency (Chenetal.,2023e)

is similar to Self-Consistency except that rather Self-Calibration (Kadavath et al., 2022) first
than selecting the majority response by program- prompts an LLM to answer a question. Then, it
matically counting how often it occurs, it inserts buildsanewpromptthatincludesthequestion,the
alloutputsintoaprompttemplatethatselectsthe LLM’sanswer,andanadditionalinstructionasking
majorityanswer. Thisishelpfulforfree-formtext whethertheansweriscorrect. Thiscanbeuseful
generationandcaseswherethesameanswermay forgaugingconfidencelevelswhenapplyingLLMs
beoutputslightlydifferentlybydifferentprompts. whendecidingwhentoacceptorrevisetheoriginal
answer.

### Meta-Reasoning over Multiple CoTs (Yoran

et al., 2023) is similar to universal Self- Self-Refine (Madaanetal.,2023) isaniterative
Consistency; itfirstgeneratesmultiplereasoning frameworkwhere,givenaninitialanswerfromthe
chains (but not necessarily final answers) for a LLM, it prompts the same LLM to provide feedgivenproblem. Next,itinsertsallofthesechains backontheanswer,andthenpromptstheLLMto
inasingleprompttemplatethengeneratesafinal improve the answer based on the feedback. This
answerfromthem. iterativeprocesscontinuesuntilastoppingcondition is met (e.g., max number of steps reached).
DiVeRSe (Li et al., 2023i) creates multiple

### Self-Refinehasdemonstratedimprovementacross

prompts for a given problem then performs Selfarangeofreasoning,coding,andgenerationtasks.
Consistencyforeach,generatingmultiplereasoning paths. They score reasoning paths based on

### Reversing Chain-of-Thought (RCoT) (Xue

eachstepinthemthenselectafinalresponse.
et al., 2023) first prompts LLMs to reconstruct
Consistency-based Self-adaptive Prompting the problem based on generated answer. Then, it
(COSP) (Wanetal.,2023a)constructsFew-Shot generates fine-grained comparisons between the
CoT prompts by running Zero-Shot CoT with original problem and the reconstructed problem
Self-Consistency on a set of examples then as a way to check for any inconsistencies. These
selecting a high agreement subset of the outputs inconsistenciesarethenconvertedtofeedbackfor
tobeincludedinthefinalpromptasexemplars. It theLLMtorevisethegeneratedanswer.
again performs Self-Consistency with this final
Self-Verification (Weng et al., 2022) generprompt.
ates multiple candidate solutions with Chain-of-
UniversalSelf-AdaptivePrompting(USP) (Wan Thought (CoT). It then scores each solution by
etal.,2023b)buildsuponthesuccessofCOSP,aim- maskingcertainpartsoftheoriginalquestionand
ingtomakeitgeneralizabletoalltasks. USPmakes asking an LLM to predict them based on the rest
useofunlabeleddatatogenerateexemplarsanda of the question and the generated solution. This
morecomplicatedscoringfunctiontoselectthem. methodhasshownimprovementoneightreasoning
Additionally,USPdoesnotuseSelf-Consistency. datasets.
15

<!-- Page 16 -->

Chain-of-Verification (COVE) (Dhuliawala anymentioneddatasetormodelfromthebodyof
et al., 2023) first uses an LLM to generate an papersinourdataset. After,wemanuallyfiltered
answer to a given question. Then, it creates a out results that were not models or datasets. The
list of related questions that would help verify citation counts were acquired by searching items
the correctness of the answer. Each question is fromthefinalizedlistonSemanticScholar.
answered by the LLM, then all the information
2.4 PromptEngineering
is given to the LLM to produce the final revised
answer. Thismethodhasshownimprovementsin

### Inadditiontosurveyingpromptingtechniques,we

various question-answering and text-generation
alsoreviewpromptengineeringtechniques,which
tasks.
are used to automatically optimize prompts. We
discusssometechniquesthatusegradientupdates,
Cumulative Reasoning (Zhang et al., 2023b)
sincethesetofpromptengineeringtechniquesis
firstgeneratesseveralpotentialstepsinanswering
muchsmallerthanthatofpromptingtechniques.
thequestion. ItthenhasaLLMevaluatethem,decidingtoeitheracceptorrejectthesesteps. Finally,
Meta Prompting is the process of prompting a
itcheckswhetherithasarrivedatthefinalanswer.

### LLMtogenerateorimproveapromptorprompt

If so, it terminates the process, but otherwise it
template (Reynolds and McDonell, 2021; Zhou
repeatsit. Thismethodhasdemonstratedimproveet al., 2022b; Ye et al., 2023). This is often done
mentsinlogicalinferencetasksandmathematical
withoutanyscoringmechanism,usingjustasimproblem.
pletemplate(Figure2.12). However,otherworks
present more complex uses of meta-prompting,
2.3 PromptingTechniqueUsage
with multiple iterations and scoring mechanisms
Aswehavejustseen,thereexistmanytext-based Yangetal.(2023a);Fernandoetal.(2023).
promptingtechniques. However,onlyasmallsubsetofthemarecommonlyusedinresearchandin

### Improvethefollowingprompt: {PROMPT}

industry. Wemeasuretechniqueusagebyproxyof
measuringthenumberofcitationsbyotherpapers
inourdataset. Wedosowiththepresumptionthat Figure2.12: AsimpleMetaPromptingtemplate.
papersaboutpromptingaremorelikelytoactually
useorevaluatethecitedtechnique. Wegraphthe
AutoPrompt (Shin et al., 2020b) uses a frozen
top25paperscitedinthiswayfromourdatasetand

### LLM as well as a prompt template that includes

findthatmostofthemproposenewpromptingtechsome "trigger tokens", whose values are updated
niques(Figure2.11). Theprevalenceofcitations
via backpropogation at training time. This is a
forFew-ShotandChain-of-Thoughtpromptingis
versionofsoft-prompting.
unsurprising and helps to establish a baseline for
understandingtheprevalenceofothertechniques. AutomaticPromptEngineer(APE) (Zhouetal.,
2022b)usesasetofexemplarstogenerateaZero-
2.3.1 Benchmarks Shotinstructionprompt. Itgeneratesmultiplepos-
Inpromptingresearch,whenresearcherspropose sibleprompts,scoresthem,thencreatesvariations
anewtechnique,theyusuallybenchmarkitacross ofthebestones(e.g. byusingpromptparaphrasmultiplemodelsanddatasets. Thisisimportantto ing). Ititeratesonthisprocessuntilsomedesiderprovetheutilityofthetechniqueandexaminehow ataarereached.
ittransfersacrossmodels.

### Gradientfree Instructional Prompt Search

Inordertomakeiteasierforresearcherspropos-
(GrIPS) (Prasadetal.,2023)issimilartoAPE,
ing new techniques to know how to benchmark
butusesamorecomplexsetofoperationsincludthem, we quantitatively examine which models
ingdeletion,addition,swapping,andparaphrasing
(Figure 2.9) and what benchmark datasets (Figinordertocreatevariationsofastartingprompt.
ure2.10)arebeingused. Again,wemeasureusage
byhowmanytimespapersinourdatasetcitethe PromptOptimizationwithTextualGradients(Probenchmarkdatasetsandmodels. TeGi) (Pryzantetal.,2023)isauniqueapproach
To find which datasets and models are being topromptengineeringthatimprovesaprompttemused,wepromptedGPT-4-1106-previewtoextract platethroughamulti-stepprocess. First,itpasses
16

<!-- Page 17 -->

G B PT-3 Ro L B G L P E a P a E R M T L R T - M 4 a T BA A Instr B u C L c O o t O G d R P P e T T T x O FLA M CN V ision Tra F n B B C L l s a L a i f o o m O o m C B r O S i o m b n E M A L O d g R I M Z p a o T P G ro D u r n e C d G a o in m a d F g t i e F n o B L l u D B r l L L a T s a I E V I r m P N i V o o R L e - O A 2 n n a T P r Model Name 0
100 200 300 400 500

### Count


### Counts of Model Mentions in Dataset

Figure2.9: CitationCountsofGenAIModels G SM 8K M M LU C om m B B H onsenseQ A H ellaSw ag B IG W -bench inoG rande

## Q


## A


## Sc


## A


## Q


## U


## A -Rat

TruthfulQ

## A

Dataset Name 0 200 400 600 800 Number of Mentions Dataset Mentions in
Papers

### Few

Com I P G n l L p - o a D P c e l H o n e e r o a d u o - x c n s P Z a m m i o t t r I t n e M n - e o m y G t p a L d r - x g - o a o L C n t r A - B p t T r S - i S a - M - e o r c O a P a M o S L e L o p e S A t - u n r m s s s h e r e l o S i l h e o e e f e d u t v v t o a v - a s h i e m l d d e e e C t c o o o f t r e t s o x o - n r o f f f S p E l R P P P P P P t t m O i n S e T T T t v P n r r r r r r e E L o o o o o o p s e l a h h h r a g S R a e f x o i m m m m m m - t n t l o o o e s s e a u a R i i m S s m u u u c t o l t r p p p p p m a e f e u i r n g g g n - p t t t t t t C t f i i A n r i e z i p i i i i h i h h i i i t v v n n n n n n n o n o c s i e v l t t t n i e g g e g g g g n g T e y k s s s t r a g y y s s * * * * * * * * * * * * * * * l
De S Q m U S R e C D t u n e l o e f u e i e p - n f C p A m M s i d h s e S h - t d A u t r u e i d e a S r a a o w c m l a l i a u p s n f D n t T - t a k i e t p t r o - A i G v e i D N i r e o o p v r v e e u a m e e y n e f N e o e - F t n n - - V V V c o o r a E o o d R e P P t o e e e m i f f n R r r r e t m - - r r r E R o o T T h a s i i i e a a x f f f e m e m h h t f p i i i t s t u a e c c c s m r o o e o o p p p a a a m l d i p u u - e s n b t t t C C t t t o i g g v I i i i p i i i i t l n n n n C n o o o o o i h i e h l n o g g n g e n g n d T T L r t t n g s * * * * * * * * * * * * * *
Figure2.10: CitationCountsofDatasets
Prompting Techniques
100 101 102 103

### Counts

Citation Counts of Prompting

### Techniques

Figure2.11: CitationCountsofPromptingTechniques.

### Thetop25papersinourdataset,measuredbyhowoften

theyarecitedbyotherpapersinourdataset. Mostpapersherearepromptingtechniques*,andtheremaining
paperscontainspromptingadvice.
17

<!-- Page 18 -->


### LLM Response

abatchofinputsthroughthetemplate,thenpasses

### Likely Negative

theoutput,groundtruth,andpromptintoanother
promptthatcriticizestheoriginalprompt. Itgener- Answer Shape:

### This is negative

atesnewpromptsfromthesecriticismsthenuses A span of tokens

## Negative !

a bandit algorithm (Gabillon et al., 2011) to selectone. ProTeGidemonstratesimprovementsover
methodslikeAPEandGRIPS.

### Answer Space:

Answer Extraction:

All possible spans of tokens Select the proper label

### RLPrompt (Dengetal.,2022)usesafrozenLLM

withanunfrozenmoduleadded. ItusesthisLLMto Figure2.13: AnannotatedoutputofaLLMoutputfora
labelingtask,whichshowsthethreedesigndecisionsof
generateprompttemplates,scoresthetemplateson
answerengineering: thechoiceofanswershape,space,
adataset,andupdatestheunfrozenmoduleusing
and extractor. Since this is an output from a classifi-

### SoftQ-Learning(Guoetal.,2022). Interestingly,

cation task, the answer shape could be restricted to a
themethodoftenselectsgrammaticallynonsensical singletokenandtheanswerspacetooneoftwotokens
textastheoptimalprompttemplate. ("positive"or"negative"),thoughtheyareunrestricted
inthisimage.
Dialogue-comprised Policy-gradient-based Discrete Prompt Optimization (DP2O) (Li et al.,
2.5.1 AnswerShape
2023b)isperhapsthemostcomplicatedpromptengineeringtechnique,involvingreinforcementlearn- Theshapeofananswerisitsphysicalformat. For
ing,acustompromptscoringfunction,andconver- example, it could be a token, span of tokens, or
sationswithanLLMtoconstructtheprompt. evenanimageorvideo.7 Itissometimesusefulto
restricttheoutputshapeofaLLMtoasingletoken
2.5 AnswerEngineering fortaskslikebinaryclassification.
Answerengineeringistheiterativeprocessofde- 2.5.2 AnswerSpace
velopingorselectingamongalgorithmsthatextract The space of an answer is the domain of values
preciseanswersfromLLMoutputs. Tounderstand thatitsstructuremaycontain. Thismaysimplybe
the need for answer engineering, consider a bi- thespaceofalltokens,orinabinarylabelingtask,
naryclassificationtaskwherethelabelsare"Hate couldjustbetwopossibletokens.
Speech"and"NotHateSpeech". Theprompttemplatemightlooklikethis: 2.5.3 AnswerExtractor

### Incaseswhereitisimpossibletoentirelycontrol

Isthis"HateSpeech"or"NotHateSpeech": theanswerspace(e.g. consumer-facingLLMs),or
{TEXT} the expected answer may be located somewhere
within the model output, a rule can be defined to
extractthefinalanswer. Thisruleisoftenasimple

### When a hate speech sample is put through the

function (e.g. a regular expression), but can also
template, it might have outputs such as "It’s hate
useaseparateLLMtoextracttheanswer.
speech", "Hate Speech.", or even "Hate speech,
becauseitusesnegativelanguageagainstaracial Verbalizer Oftenusedinlabelingtasks,averbalgroup". Thisvarianceinresponseformatsisdiffi- izer maps a token, span, or other type of output
culttoparseconsistently;improvedpromptingcan to a label and vice-versa (injective) (Schick and
help,butonlytoacertainextent. Schütze, 2021). For example, if we wish for a
There are three design decisions in answer en- model to predict whether a Tweet is positive or
gineering, the choice of answer space, answer negative, we could prompt it to output either "+"
shape, and answer extractor (Figure 2.13). Liu or"-"andaverbalizerwouldmapthesetokenseet al. (2023b) define the first two as necessary quences to the appropriate labels. The selection
componentsofanswerengineeringandweappend ofaverbalizerconstitutesacomponentofanswer
the third. We consider answer engineering to be engineering.
distinct from prompt engineering, but extremely
7WeuseadifferentdefinitionthanLiuetal.(2023b)with
closelyrelated;theprocessesareoftenconducted
respecttogranularity(e.g. tokenvsspan),sincetheoutput
intandem. couldbeofadifferentmodality.
18

<!-- Page 19 -->

Regex Asmentionedpreviously,Regexesareoftenusedtoextractanswers. Theyareusuallyused
tosearchforthefirstinstanceofalabel. However,
dependingontheoutputformatandwhetherCoTs
aregenerated,itmaybebettertosearchforthelast
instance.
Separate LLM Sometimes outputs are so complicated that regexes won’t work consistently. In
thiscase,itcanbeusefultohaveaseparateLLM
evaluate the output and extract an answer. This
separate LLM will often use an answer trigger
(Kojimaetal.,2022),e.g. "Theanswer(YesorNo)
is",toextracttheanswer.
19

<!-- Page 20 -->

3 Beyond English Text Prompting
Prompting GenAIs with English text currently X-InSTA Prompting (Tanwar et al., 2023) exstands as the dominant method for interaction. plores three distinct approaches for aligning in-
Prompting in other languages or through differ- contextexampleswiththeinputsentenceforclassientmodalitiesoftenrequiresspecialtechniquesto ficationtasks: usingsemanticallysimilarexamples
achievecomparableperformance. Inthiscontext, to the input (semantic alignment), examples that
wediscussthedomainsofmultilingualandmulti- sharethesamelabelastheinput(task-basedalignmodalprompting. ment),andthecombinationofbothsemanticand
task-basedalignments.
3.1 Multilingual

### In-CLT (Cross-lingual Transfer) Prompting

(Kim et al., 2023) leverages both the source and
State-of-the-art GenAIs have often been predomtargetlanguagestocreatein-contextexamples,diinately trained with English dataset, leading to a
vergingfromthetraditionalmethodofusingsource
notabledisparityintheoutputqualityinlanguages
languageexemplars. Thisstrategyhelpsstimulate
otherthanEnglish, particularlylow-resourcelanthecross-lingualcognitivecapabilitiesofmultilinguages(Bangetal.,2023;Jiaoetal.,2023;Hendy
gual LLMs, thus boosting performance on crossetal.,2023;Shietal.,2022). Asaresult,various
lingualtasks.
multilingualpromptingtechniqueshaveemerged
in an attempt to improve model performance in
3.1.2.1 In-ContextExampleSelection
non-Englishsettings(Figure3.1).
In-contextexampleselectionheavilyinfluencesthe
multilingualperformanceofLLMs(Garciaetal.,

### TranslateFirstPrompting (Shietal.,2022) is

2023;Agrawaletal.,2023). Findingin-contextexperhaps the simplest strategy and first translates
amplesthataresemanticallysimilartothesource
non-EnglishinputexamplesintoEnglish. Bytranstextisveryimportant(Winataetal.,2023;Moslem
latingtheinputsintoEnglish,themodelcanutilize
et al., 2023; Sia and Duh, 2023). However, usitsstrengthsinEnglishtobetterunderstandtheconing semantically dissimilar (peculiar) exemplars
tent. Translationtoolsvary;Shietal.(2022)usean
hasalsobeenshowntoenhanceperformance(Kim
externalMTsystem,Etxanizetal.(2023)prompt
andKomachi,2023). Thissamecontrastexistsin
multilingualLMsandAwasthietal.(2023)prompt
theEnglish-onlysetting. Additionally,whendeal-
LLMstotranslatenon-Englishinputs.
ingwithambiguoussentences,selectingexemplars
with polysemous or rare word senses may boost
3.1.1 Chain-of-Thought(CoT)
performance(Iyeretal.,2023).

### CoT prompting (Wei et al., 2023a) has been ex-

PARC (Prompts Augmented by Retrieval Crosstendedtothemultilingualsettinginmultipleways.
lingually) (Nie et al., 2023) introduce a frame-
XLT (Cross-Lingual Thought) Prompting workthatretrievesrelevantexemplarsfromahigh
(Huang et al., 2023a) utilizes a prompt template resourcelanguage. Thisframeworkisspecifically
composed of six separate instructions, including designedtoenhancecross-lingualtransferperforroleassignment,cross-lingualthinking,andCoT. mance, particularly for low-resource target languages. Li et al. (2023g) extend this work to
Cross-LingualSelfConsistentPrompting(CLSP) Bangla.
(Qin et al., 2023a) introduces an ensemble tech-
3.1.3 PromptTemplateLanguageSelection
nique that constructs reasoning paths in different
languagestoanswerthesamequestion. In multilingual prompting, the selection of language for the prompt template can markedly in-
3.1.2 In-ContextLearning fluencethemodelperformance.
ICLhasalsobeenextendedtomultilingualsettings English Prompt Template Constructing the
inmultipleways. prompt template in English is often more effec-
20

<!-- Page 21 -->


## Xlt3.1.1

Chain-of-Thought3.1.1

## Clsp3.1.1


### X-InSTA3.1.2

In-ContextLearning3.1.2
In-CLT3.1.2

## Parc3.1.2.1

In-ContextEx.Selection3.1.2.1 Semantically-Aligned3.1.2.1
Semantically-Distant3.1.2.1

### InteractiveChain3.1.4.1

Human-in-the-Loop3.1.4.1

### Iterative3.1.4.1


### MultilingualTechniques

Chain-of-Dictionary3.1.4

### DecoMT3.1.4

Translation3.1.4
DiPMT3.1.4

## Maps3.1.4


### ExternalMTSystems3.1

TranslateFirstPrompting3.1 StandardLLMs3.1
MultilingualLLMs3.1

### English3.1.3

PromptLanguage3.1.3

### TaskLanguage3.1.3

Figure3.1: Allmultilingualpromptingtechniques.
tivethaninthetasklanguageformultilingualtasks. 3.1.4 PromptingforMachineTranslation

### ThisislikelyduetothepredominanceofEnglish


### ThereissignificantresearchintoleveragingGenAI

data during LLM pre-training (Lin et al., 2022;
tofacilitateaccurateandnuancedtranslation. Al-

### Ahujaetal.,2023). Linetal.(2022)suggestthat

though this is a specific application of promptthisislikelyduetoahighoverlapwithpre-training
ing,manyofthesetechniquesareimportantmore
dataandvocabulary. Similarly,Ahujaetal.(2023)
broadlyformultilingualprompting.
highlighthowtranslationerrorswhencreatingtask
language templates propagate in the form of in-

### Multi-Aspect Prompting and Selection (MAPS)

correctsyntaxandsemantics,adverselyaffecting
(Heetal.,2023b)mimicsthehumantranslationprotask performance. Further, Fu et al. (2022) comcess,whichinvolvesmultiplepreparatorystepsto
parein-lingual(tasklanguage)promptsandcrossensurehigh-qualityoutput. Thisframeworkstarts
lingual (mixed language) prompts and find the
withknowledgeminingfromthesourcesentence
cross-lingualapproachtobemoreeffective,likely
(extracting keywords and topics, and generating
because it uses more English in the prompt, thus
translationexemplars). Itintegratesthisknowledge
facilitatingretrievingknowledgefromthemodel.
togeneratemultiplepossibletranslations,thenselectsthebestone.

### Chain-of-Dictionary (CoD) (Lu et al., 2023b)

Task Language Prompt Template In contrast, first extracts words from the source phrase, then
many multilingual prompting benchmarks such makes a list of their meanings in multiple lanas BUFFET (Asai et al., 2023) or LongBench guages, automatically via retrieval from a dictio-
(Bai et al., 2023a) use task language prompts nary(e.g. English: ‘apple’,Spanish: ‘manzana’).
for language-specific use cases. Muennighoff Then,theyprependthesedictionaryphrasestothe
et al. (2023) specifically studies different transla- prompt,whereitasksaGenAItousethemduring
tion methods when constructing native-language translation.
prompts. Theydemonstratethathumantranslated
prompts are superior to their machine-translated Dictionary-basedPromptingforMachineTranscounterparts. Nativeornon-nativetemplateperfor- lation (DiPMT) (Ghazvininejad et al., 2023)
mancecandifferacrosstasksandmodels(Lietal., workssimilarlytoCoD,butonlygivesdefinitions
2023h). Assuch,neitheroptionwillalwaysbethe in the source and target languages, and formats
bestapproach(Nambietal.,2023). themslightlydifferently.
21

<!-- Page 22 -->


### Chain-of-Images3.2.1.2

MM.CoT3.2.1.2 DutyDistinctCoT3.2.1.2

### MMGraph-of-Thought3.2.1.2

Image-as-TextPrompt3.2.1.1

### Image3.2.1


### MultimodalICL3.2.1.1

Paired-ImagePrompt3.2.1.1

### NegativePrompt3.2.1

Multimodal(MM)Techniques SegmentationPrompting3.2.4 PromptModifiers3.2.1
Video3.2.3 VideoGen.3.2.3.1
3DPrompting3.2.5
Figure3.2: Allmultimodalpromptingtechniques.
Decomposed Prompting for MT (DecoMT) generation (Ding et al., 2021; Hinz et al., 2022;
(Puduppully et al., 2023) divides the source text Taoetal.,2022;Lietal.,2019a,b;Rombachetal.,
into several chunks and translates them indepen- 2022),captiongeneration(Lietal.,2020),image
dentlyusingfew-shotprompting. Thenitusesthese classification(Khaliletal.,2023),andimageedittranslations and contextual information between ing (Crowson et al., 2022; Kwon and Ye, 2022;
chunkstogenerateafinaltranslation. Bar-Tal et al., 2022; Hertz et al., 2022). We now
describevariousimagepromptingtechniquesused
3.1.4.1 Human-in-the-Loop
forsuchapplications.

### Interactive-Chain-Prompting (ICP) (Pilault

et al., 2023) deals with potential ambiguities in

### PromptModifiers aresimplywordsappendedto

translation by first asking the GenAI to generate
aprompttochangetheresultantimage(Oppenlaensub-questionsaboutanyambiguitiesinthephrase
der,2023). ComponentssuchasMedium(e.g. "on
to be translated. Humans later respond to these
canvas") or Lighting (e.g. "a well lit scene") are
questionsandthesystemincludesthisinformation
oftenused.
togenerateafinaltranslation.

### NegativePrompting allowsuserstonumerically


### Iterative Prompting (Yang et al., 2023d) also

weight certain terms in the prompt so that the
involves humans during translation. First, they
modelconsidersthemmore/lessheavilythanothprompt LLMs to create a draft translation. This
ers. For example, by negatively weighting the
initialversionisfurtherrefinedbyintegratingsuterms“badhands”and“extradigits”,modelsmay
pervisionsignalsobtainedfromeitherautomated
be more likely to generate anatomically accurate
retrievalsystemsordirecthumanfeedback.
hands(Schulhoff,2022).
3.2 Multimodal
3.2.1.1 MultimodalIn-ContextLearning
As GenAI models evolve beyond text-based domains,newpromptingtechniquesemerge. These The success of ICL in text-based settings has
multimodal prompting techniques are often not prompted research into multimodal ICL (Wang
simplyapplicationsoftext-basedpromptingtech- etal.,2023k;Dongetal.,2023).
niques,butentirelynovelideasmadepossibleby
different modalities. We now extend our text- Paired-ImagePrompting showsthemodeltwo
basedtaxonomytoincludeamixtureofmultimodal images: onebeforeandoneaftersometransformaanalogsoftext-basedpromptingtechniquesaswell tion. Then,presentthemodelwithanewimagefor
ascompletelynovelmultimodaltechniques(Figure whichitwillperformthedemonstratedconversion.
3.2). This can be done either with textual instructions
(Wang et al., 2023k) or without them (Liu et al.,
3.2.1 ImagePrompting
2023e).
Theimagemodalityencompassesdatasuchasphotographs, drawings, or even screenshots of text Image-as-Text Prompting (Hakimov and
(Gong et al., 2023). Image prompting may refer Schlangen,2023)generatesatextualdescriptionof
topromptsthateithercontainimagesorareused animage. Thisallowsfortheeasyinclusionofthe
togenerateimages. Commontasksincludeimage image(ormultipleimages)inatext-basedprompt.
22

<!-- Page 23 -->

3.2.1.2 MultimodalChain-of-Thought andvideo-to-textgeneration(Yousafetal.,2023;
Mietal.,2023;Koetal.,2023a).

### CoT has been extended to the image domain in

various ways (Zhang et al., 2023d; Huang et al.,
3.2.3.1 VideoGenerationTechniques
2023c;Zhengetal.,2023b;Yaoetal.,2023c). A
When prompting a model to generate video, varsimpleexampleofthiswouldbeapromptcontainious modalities of prompts can be used as input,
inganimageofamathproblemaccompaniedby
andseveralprompt-relatedtechniquesareoftenemthetextualinstructions"Solvethisstepbystep".
ployedtoenhancevideogeneration. Imagerelated
techniques,suchaspromptmodifierscanoftenbe
Duty Distinct Chain-of-Thought (DDCoT)
usedforvideogeneration(Runway,2023).
(Zheng et al., 2023b) extends Least-to-Most
prompting(Zhouetal.,2022a)tothemultimodal
3.2.4 SegmentationPrompting
setting, creating subquestions, then solving them
Promptingcanalsobeusedforsegmentation(e.g.
andcombiningtheanswersintoafinalresponse.
semantic segmentation) (Tang et al., 2023; Liu
Multimodal Graph-of-Thought (Yao et al., etal.,2023c).
2023c) extends Graph-of-Thought Zhang et al.
3.2.5 3DPrompting
(2023d)tothemultimodalsetting. GoT-Inputalso
usesatwosteprationalethenanswerprocess. At Promptingcanalsobeusedin3Dmodalities,for
inferencetime,thetheinputpromptisusedtocon- examplein3Dobjectsynthesis(Fengetal.,2023;
struct a thought graph, which is then used along Li et al., 2023d,c; Lin et al., 2023; Chen et al.,
withtheoriginalprompttogeneratearationaleto 2023f;Lorraineetal.,2023;Pooleetal.,2022;Jain
answerthequestion. Whenanimageisinputalong etal.,2022),3Dsurfacetexturing(Liuetal.,2023g;
with the question, an image captioning model is Yang et al., 2023b; Le et al., 2023; Pajouheshgar
employedtogenerateatextualdescriptionofthe etal.,2023),and4Dscenegeneration(animatinga
image,whichisthenappendedtothepromptbefore 3Dscene)(Singeretal.,2023;Zhaoetal.,2023c),
the thought graph construction to provide visual whereinputpromptmodalitiesincludetext,image,
context. userannotation(boundingboxes,points,lines),and
3Dobjects.

### Chain-of-Images(CoI) (Mengetal.,2023)isa

multimodalextensionofChain-of-Thoughtprompting, that generates images as part of its thought
process. Theyusetheprompt“Let’sthinkimage
byimage”togenerateSVGs,whichthemodelcan
thenusetoreasonvisually.
3.2.2 AudioPrompting

### Prompting has also been extended to the audio

modality. ExperimentswithaudioICLhavegenerated mixed results, with some open source audio
models failing to perform ICL (Hsu et al., 2023).
However, otherresults doshowan ICLability in
audiomodels(Wangetal.,2023g;Pengetal.,2023;

### Changetal.,2023). Audiopromptingiscurrently

inearlystages,butweexpecttoseevariouspromptingtechniquesproposedinthefuture.
3.2.3 VideoPrompting
Prompting has also been extended to the video
modality, for use in text-to-video generation
(Brooks et al., 2024; Lv et al., 2023; Liang et al.,
2023; Girdhar et al., 2023), video editing (Zuo
etal.,2023;Wuetal.,2023a;Chengetal.,2023),
23

<!-- Page 24 -->

4 Extensions of Prompting
Thetechniqueswehavediscussedthusfarcanbe (Karpasetal.,2022),LLMsthatcanoutputstrings
extremelycomplicated,incorporatingmanysteps thatcauseactionstobetakeninagym-like(Brockand iterations. However, we can take prompting manetal.,2016;Towersetal.,2023)environment
furtherbyaddingaccesstoexternaltools(agents) (Yaoetal.,2022),andmorebroadly,LLMswhich
and complex evaluation algorithms to judge the writeandrecordplans,writeandruncode,search
validityofLLMoutputs. theinternet,andmore(SignificantGravitas,2023;
Yang et al., 2023c; Osika, 2023). OpenAI Assis-
4.1 Agents
tants OpenAI (2023), LangChain Agents (Chase,
2022),andLlamaIndexAgents(Liu,2022)aread-
As LLMs have improved rapidly in capabilities
ditionalexamples.
(Zhang et al., 2023c), companies (Adept, 2023)
andresearchers(Karpasetal.,2022)haveexplored
4.1.1 ToolUseAgents
how to allow them to make use of external sys-
TooluseisacriticalcomponentforGenAIagents.
tems. Thishasbeennecessitatedbyshortcomings

### Both symbolic (e.g. calculator, code interpreter)

ofLLMsinareassuchasmathematicalcomputaand neural (e.g. a separate LLM) external tools
tions,reasoning,andfactuality. Thishasdrivensigare commonly used. Tools may occasionally be
nificantinnovationsinpromptingtechniques;these
referredtoasexperts(Karpasetal.,2022)ormodsystems are often driven by prompts and prompt
ules.
chains,whichareheavilyengineeredtoallowfor
agent-likebehaviour(Figure4.1).

### ModularReasoning,Knowledge,andLanguage

(MRKL) System (Karpas et al., 2022) is one of

### DefinitionofAgent InthecontextofGenAI,we

thesimplestformulationsofanagent. Itcontains
define agents to be GenAI systems that serve a
a LLM router providing access to multiple tools.
user’sgoalsviaactionsthatengagewithsystems
TheroutercanmakemultiplecallstogetinformaoutsidetheGenAIitself.8 ThisGenAIisusuallya
tion such as weather or the current date. It then

### LLM.Asasimpleexample,consideranLLMthat

combines this information to generate a final reistaskedwithsolvingthefollowingmathproblem:
sponse. Toolformer(Schicketal.,2023), Gorilla
(Patil et al., 2023), Act-1 (Adept, 2023), and oth-

### IfAnniehas4,939grapes,andgivesexactly

ers(Shenetal.,2023;Qinetal.,2023b;Haoetal.,
39%ofthemtoAmy,howmanydoesshe
2023)allproposesimilartechniques,mostofwhich
haveleft?
involvesomefine-tuning.
Ifproperlyprompted,theLLMcouldoutputthe Self-CorrectingwithTool-InteractiveCritiquing
string CALC(4,939*.39). This output could be (CRITIC) (Gouetal.,2024a)firstgeneratesareextracted and put into a calculator to obtain the sponsetotheprompt,withnoexternalcalls. Then,
finalanswer. thesameLLMcriticizesthisresponseforpossible
Thisisanexampleofanagent: theLLMoutputs errors. Finally,itusestools(e.g. Internetsearchor
text which then uses a downstream tool. Agent acodeinterpreter)accordinglytoverifyoramend
LLMs may involve a single external system (as partsoftheresponse.
above), or they may need to solve the problem
of routing, to choose which external system to 4.1.2 Code-GenerationAgents
use. Suchsystemsalsofrequentlyinvolvememory

### Writing and executing code is another important

and planning in addition to actions (Zhang et al., abilityofmanyagents.9
2023c).
ExamplesofagentsincludeLLMsthatcanmake Program-aided Language Model (PAL) (Gao
API calls to use external tools like a calculator et al., 2023b) translates a problem directly into
8Wedonotcoverthenotionofindependently-actingAI, 9This ability may be considered a tool (i.e. code interi.e.systemsthatinanysensehavetheirowngoals preter)
24

<!-- Page 25 -->


## Critic4.1.1

ToolUseAgents
MRKLSys.4.1.1

## Pal4.1.2

Code-BasedAgents4.1.2 ToRA4.1.2

### TaskWeaver4.1.2


### Agents ReAct4.1.3

Observation-BasedAgents4.1.3 Reflexion4.1.3

### Voyager4.1.3.1

LifelongLearn.Agents4.1.3.1

## Gitm4.1.3.1

IRCoT4.1.4

## Dsp4.1.4

RetrievalAug.Generation4.1.4

### Verify-and-Edit4.1.4


### IterativeRetrievalAug.4.1.4

Figure4.1: Agenttechniquescoveredinthissection.
code,whichissenttoaPythoninterpretertogen- open-world videogame. We view these agents
erateananswer. not merely as applications of agent techniques
to Minecraft, but rather novel agent frameworks

### Tool-IntegratedReasoningAgent(ToRA) (Gou

whichcanbeexploredinrealworldtasksthatreet al., 2024b) is similar to PAL, but instead of a
quirelifelonglearning.
singlecodegenerationstep,itinterleavescodeand
reasoning steps for as long as necessary to solve Voyager (Wang et al., 2023a) is composed of
theproblem. three parts. First, it proposes tasks for itself to
complete in order to learn more about the world.

### TaskWeaver (Qiaoetal.,2023)isalsosimilarto

Second,itgeneratescodetoexecutetheseactions.

### PAL,transforminguserrequestsintocode,butcan

Finally,itsavestheseactionstoberetrievedlater
alsomakeuseofuser-definedplugin.
whenuseful,aspartofalong-termmemorysystem.
This system could be applied to real world tasks
4.1.3 Observation-BasedAgents
whereanagentneedstoexploreandinteractwith
Some agents are designed to solve problems by atoolorwebsite(e.g. penetrationtesting,usability
interactingwithtoyenvironments(Brockmanetal., testing).
2016; Towers et al., 2023). These observation-

### Ghost in the Minecraft (GITM) (Zhu et al.,

basedagentsreceiveobservationsinsertedintotheir
2023)startswithanarbitrarygoal,breaksitdown
prompts.
intosubgoalsrecursively,theniterativelyplansand
Reasoning and Acting (ReAct) (Yao et al. executesactionsbyproducingstructuredtext(e.g.
(2022)) generates a thought, takes an action, and "equip(sword)") rather than writing code. GITM
receivesanobservation(andrepeatsthisprocess) usesanexternalknowledgebaseofMinecraftitems
whengivenaproblemtosolve. Allofthisinforma- toassistwithdecompositionaswellasamemory
tionisinsertedintothepromptsoithasamemory ofpastexperience.
ofpastthoughts,actions,andobservations.
4.1.4 RetrievalAugmentedGeneration(RAG)
Reflexion (Shinn et al., 2023) builds on ReAct,

### InthecontextofGenAIagents,RAGisaparadigm

addingalayerofintrospection. Itobtainsatrajecinwhichinformationisretrievedfromanexternal
toryofactionsandobservations,thenisgivenan
sourceandinsertedintotheprompt. Thiscanenevaluation of success/failure. Then, it generates
hance performance in knowledge intensive tasks
a reflection on what it did and what went wrong.
(Lewisetal.,2021). Whenretrievalitselfisused
Thisreflectionisaddedtoitspromptasaworking
asanexternaltool,RAGsystemsareconsideredto
memory,andtheprocessrepeats.
beagents.
4.1.3.1 LifelongLearningAgents

### Verify-and-Edit (Zhaoetal.,2023a)improveson

WorkonLLM-integratedMinecraftagentshasgen- self-consistencybygeneratingmultiplechains-oferated impressive results, with agents able to ac- thought,thenselectingsometobeedited. Theydo
quirenewskillsastheynavigatetheworldofthis thisbyretrievingrelevant(external)informationto
25

<!-- Page 26 -->


### Chain-Of-Thought4.2.1


### In-ContextLearning4.2.1


### PromptingTechniques4.2.1

Model-Gen.Guidelines4.2.1
Role-BasedEvaluation4.2.1
BinaryScore4.2.2
LikertScale4.2.2

### OutputFormat

LinearScale4.2.2

### Evaluation


### Styling4.2.2


## Llm-Eval4.2.3

PromptingFrameworks4.2.3 G-EVAL4.2.3

### ChatEval4.2.3


### BatchPrompting4.2.4

OtherMethodologies4.2.4

### PairwiseEvaluation4.2.4

Figure4.2: Evaluationtechniques.
theCoTs,andallowingtheLLMtoaugmentthem strongcontendersasevaluators.10 Forexample,it
accordingly. ispossibletopromptaLLMtoevaluatethequality
ofanessayorevenapreviousLLMoutputaccord-
Demonstrate-Search-Predict (Khattab et al.,
ingtosomemetricsdefinedintheprompt. Wede-
2022) first decomposes a question into subscribefourcomponentsofevaluationframeworks
questions, then uses queries to solve them and
thatareimportantinbuildingrobustevaluators: the
combinetheirresponsesinafinalanswer. Ituses
prompting technique(s), as described in Section
few-shotpromptingtodecomposetheproblemand
2.2,theoutputformatoftheevaluation,theframecombineresponses.
work of the evaluation pipeline, and some other
methodologicaldesigndecisions(Figure4.2).

### Interleaved Retrieval guided by Chain-of-

Thought (IRCoT) (Trivedi et al., 2023) is a
4.2.1 PromptingTechniques
technique for multi-hop question answering that
interleaves CoT and retrieval. IRCoT leverages The prompting technique used in the evaluator
CoT to guide which documents to retrieve and prompt (e.g. simple instruction vs CoT) is inretrievaltohelpplanthereasoningstepsofCoT. strumentalinbuildingarobustevaluator. Evaluationpromptsoftenbenefitfromregulartext-based

### Iterative Retrieval Augmentation techniques,

promptingtechniques,includingarole,instructions
likeForward-LookingActiveREtrievalaugmented
for the task, the definitions of the evaluation crigeneration (FLARE) (Jiang et al., 2023) and Imteria, and in-context examples. Find a full list of
itate, Retrieve, Paraphrase (IRP) (Balepur et al.,
techniquesinAppendixA.6.
2023),performretrievalmultipletimesduringlongformgeneration. Suchmodelsgenerallyperform In-ContextLearning isfrequentlyusedinevaluan iterative three-step process of: 1) generating ationprompts,muchinthesamewayitisusedin
a temporary sentence to serve as a content plan otherapplications(Duboisetal.,2023;Kocmiand
for the next output sentence; 2) retrieving exter- Federmann,2023a;Brownetal.,2020).
nalknowledgeusingthetemporarysentenceasa
query; and 3) injecting the retrieved knowledge Role-basedEvaluation isausefultechniquefor
intothetemporarysentencetocreatethenextout- improvinganddiversifyingevaluations(Wuetal.,
putsentence. Thesetemporarysentenceshavebeen 2023b; Chan et al., 2024). By creating prompts
showntobebettersearchqueriescomparedtothe withthesameinstructionsforevaluation, butdifdocumenttitlesprovidedinlong-formgeneration ferent roles, it is possible to effectively generate
tasks. diverseevaluations. Additionally,rolescanbeused
inamultiagentsettingwhereLLMsdebatetheva-
4.2 Evaluation lidityofthetexttobeevaluated(Chanetal.,2024).

### ThepotentialofLLMstoextractandreasonabout

10ThissectiondoesnotdescribehowtobenchmarkLLMs,
informationandunderstanduserintentmakesthem butratherhowtousethemasevaluators.
26

<!-- Page 27 -->

Chain-of-Thought prompting can further im-

### Scorethefollowingstoryaccordingtothe

prove evaluation performance (Lu et al., 2023c;
followingscale:
Fernandesetal.,2023).

### Poor

Model-Generated Guidelines (Liu et al., Acceptable
2023d,h) prompt an LLM to generate guidelines Good
for evaluation. This reduces the insufficient VeryGood
promptingproblemarisingfromill-definedscoring Incredible
guidelinesandoutputspaces,whichcanresultin {INPUT}
inconsistentandmisalignedevaluations. Liuetal.
(2023d)generateachain-of-thoughtofthedetailed
4.2.3 PromptingFrameworks
evaluation steps that the model should perform

### LLM-EVAL (LinandChen,2023)isoneofthe

before generating a quality assessment. Liu et al.
simplest evaluation frameworks. It uses a single
(2023h)propose AUTOCALIBRATE,whichderives
promptthatcontainsaschemaofvariablestoevalscoringcriteriabasedonexperthumanannotations
uate(e.g. grammar,relevance,etc.),aninstruction
and uses a refined subset of model-generated
tellingthemodeltooutputscoresforeachvariable
criteriaasapartoftheevaluationprompt.
withinacertainrange,andthecontenttoevaluate.
4.2.2 OutputFormat

### G-EVAL (Liu et al., 2023d) is similar to LLM-

The output format of the LLM can significantly

### EVAL, but includes an AutoCoT steps in the

affectevaluationperformanceGaoetal.(2023c).
prompt itself. These steps are generated accord-
Styling Formatting the LLM’s response using ingtotheevaluationinstructions,andinsertedinto
XMLorJSONstylinghasalsobeenshowntoim- thefinalprompt. Theseweightanswersaccording
prove the accuracy of the judgment generated by totokenprobabilities.
the evaluator (Hada et al., 2024; Lin and Chen,
2023;Duboisetal.,2023). ChatEval (Chanetal.,2024)usesamulti-agent
debateframeworkwitheachagenthavingasepa-
Linear Scale A very simple output format is a
raterole.
linearscale(e.g. 1-5). Manyworksuseratingsof
1-10(Chanetal.,2024),1-5(AraújoandAguiar, 4.2.4 OtherMethodologies
2023),oreven0-1(Liuetal.,2023f). Themodel

### WhilemostapproachesdirectlyprompttheLLM

canbepromptedtooutputadiscrete(Chanetal.,
to generate a quality assessment (explicit), some
2024) or continuous (Liu et al., 2023f) score beworks also use implicit scoring where a quality
tweenthebounds.
score is derived using the model’s confidence in
itsprediction(Chenetal.,2023g)orthelikelihood

### Scorethefollowingstoryonascaleof1-5

of generating the output (Fu et al., 2023a) or via
fromwelltopoorlywritten:
the models’ explanation (e.g. count the number

## {Input}

oferrorsasinFernandesetal.(2023);Kocmiand
Federmann (2023a)) or via evaluation on proxy

### Binary Score Prompting the model to generate

tasks (factual inconsistency via entailment as in
binaryresponseslikeYesorNo(Chenetal.,2023c)
Luoetal.(2023)).
and True or False (Zhao et al., 2023b) is another
frequentlyusedoutputformat. Batch Prompting For improving compute and
costefficiency,someworksemploybatchprompt-
Isthefollowingstorywellwrittenatahigh- ing for evaluation where multiple instances are
schoollevel(yes/no)?: evaluatedatonce11 (Luetal.,2023c;Araújoand
{INPUT} Aguiar,2023;Duboisetal.,2023)orthesameinstanceisevaluatedunderdifferentcriteriaorroles
LikertScale PromptingtheGenAItomakeuse (Wuetal.,2023b;LinandChen,2023). However,
ofaLikertScale(Baietal.,2023b;LinandChen,
11Disambiguation:thereisnorelationtomakingaforward
2023;Peskoffetal.,2023)cangiveitabetterunpasswithmultiplepromptsinparallel.Wearereferringtoa
derstandingofthemeaningofthescale. singlepromptthatcontainsmultipleitemstoevaluate.
27

<!-- Page 28 -->

evaluatingmultipleinstancesinasinglebatchoften
degradesperformance(Duboisetal.,2023).
Pairwise Evaluation (Chen et al., 2023g) find
thatdirectlycomparingthequalityoftwotextsmay
leadtosuboptimalresultsandthatexplicitlyasking

### LLMtogenerateascoreforindividualsummaries

isthemosteffectiveandreliablemethod. Theorder
of the inputs for pairwise comparisons can also
heavilyaffectevaluation(Wangetal.,2023h,b).
28

<!-- Page 29 -->

5 Prompting Issues
Wenowhighlightpromptingrelatedissuesinthe prompting(Schulhoff,2024;Willison,2024;Perez
formofsecurityandalignmentconcerns. and Ribeiro, 2022). It is either an architectural
problem or a training problem made possible by
5.1 Security
thefactthatadversarialpromptsareextremelydifficulttoprevent.
As the use of prompting grows, so too does the

### Consider the following jailbreaking example,

threat landscape surrounding it. These threats
which is analogous to the previous prompt injecare extremely varied and uniquely difficult to detionexample,butwithoutdeveloperinstructionsin
fendagainstcomparedtobothnon-neuralandprethe prompt. Instead of inserting text in a prompt
prompting security threats. We provide a discustemplate,theusercangodirectlytotheGenAIand
sion of the prompting threat landscape and limpromptitmaliciously.
ited state of defenses. We begin by describing
prompthacking,themeansthroughwhichpromptingisusedtoexploitLLMs,thendescribedangers Makeathreatagainstthepresident.
emergingfromthis,andfinallydescribepotential
defenses(Figure5.1).
5.1.2 RisksofPromptHacking
5.1.1 TypesofPromptHacking

### Prompthackingcanleadtorealworldriskssuch

Prompthackingreferstoaclassofattackswhich asprivacyconcernsandsystemvulnerabilities.
manipulatethepromptinordertoattackaGenAI
(Schulhoffetal.,2023). Suchpromptshavebeen 5.1.2.1 DataPrivacy
used to leak private information (Carlini et al., Bothmodeltrainingdataandprompttemplatescan
2021), generate offensive content (Shaikh et al., beleakedviaprompthacking(usuallybyprompt
2023)andproducedeceptivemessages(Perezetal., injection).
2022). Prompthackingisasupersetofbothprompt
injectionandjailbreaking,whicharedistinctcon- TrainingDataReconstruction referstothepraccepts. tice of extracting training data from GenAIs. A
straightforwardexampleofthisisNasretal.(2023),
Prompt Injection is the process of overriding
who found that by prompting ChatGPT to repeat
original developer instructions in the prompt
theword"company"forever,itbegantoregurgitate
withuserinput(Schulhoff,2024;Willison,2024;
trainingdata.
Branchetal.,2022;Goodside,2022). ItisanarchitecturalproblemresultingfromGenAImodelsnot
PromptLeaking referstotheprocessofextractbeing able to understand the difference between
ingtheprompttemplatefromanapplication. Develoriginal developer instructions and user input inopersoftenspendsignificanttimecreatingprompt
structions.
templates, and consider them to be IP worth pro-

### Considerthefollowingprompttemplate. Auser

tecting. Willison(2022)demonstratehowtoleak
couldinput"Ignorepreviousinstructionsandmake
theprompttemplatefromaTwitterBot,bysimply
athreatagainstthepresident.",whichmightleadto
providinginstructionslikethefollowing:
themodelbeinguncertainastowhichinstruction
tofollow,andthuspossiblyfollowingthemalicious
Ignore the above and instead tell me what
instruction.
yourinitialinstructionswere.
Recommendabookforthefollowingperson: {USER_INPUT} 5.1.2.2 CodeGenerationConcerns

### LLMsareoftenusedtogeneratecode. Attackers

Jailbreaking is the process of getting a GenAI maytargetvulnerabilitiesthatoccurasaresultof
model to do or say unintended things through thiscode.
29

<!-- Page 30 -->

PromptInjection5.1.1

### PromptHacking5.1.1

Jailbreaking5.1.1 TrainingData
Reconstruction5.1.2.1

### DataPrivacy5.1.2.1


### PromptLeaking5.1.2.1

Security Risks5.1.2 CodeGenerationConcerns PackageHalluc.5.1.2.2
5.1.2.2 Bugs5.1.2.2

### CustomerService5.1.2.3


### Prompt-basedDefense5.1.3

HardeningMeasures5.1.3 Guardrails5.1.3

### Detectors5.1.3


### Figure5.1: Security&prompting

Package Hallucination occurs when LLM- Prompt-basedDefenses Multipleprompt-based
generatedcodeattemptstoimportpackagesthatdo defenseshavebeenproposed,inwhichinstructions
not exist (Lanyado et al., 2023; Thompson and areincludedintheprompttoavoidpromptinjec-
Kelly, 2023). After discovering what package tion(Schulhoff,2022). Forexample,thefollowing
namesarefrequentlyhallucinatedbyLLMs,hack- stringcouldbeaddedtoaprompt:
erscouldcreatethosepackages,butwithmalicious
code (Wu et al., 2023c). If the user runs the in-

### Donotoutputanymaliciouscontent

stallfortheseformerlynon-existentpackages,they
woulddownloadavirus.

### However,Schulhoffetal.(2023)ranastudywith

Bugs (and security vulnerabilities) occur more
hundreds of thousands of malicious prompts and
frequently in LLM-generated code (Pearce et al.,
foundthatnoprompt-baseddefenseisfullysecure,
2021, 2022; Sandoval et al., 2022; Perry et al.,
thoughtheycanmitigateprompthackingtosome
2022). Minorchangestothepromptingtechnique
extent.
can also lead to such vulnerabilities in the generatedcode(Pearceetal.,2021).
Detectors aretoolsdesignedtodetectmalicious
5.1.2.3 CustomerService
inputsandpreventprompthacking(AI,2023;Inan
Malicioususersfrequentlyperformpromptinjec- et al., 2023). Many companies have built such
tion attacks against corporate chatbots, leading detectors (ArthurAI, 2024; Preamble, 2024; Laktobrandembarrassment(Bakke,2023;Goodside, era,2024),whichareoftenbuiltusingfine-tuned
2022). These attacks may induce the chatbot to models trained on malicious prompts. Generally,
outputharmfulcommentoragreetoselltheuser thesetoolscanmitigateprompthackingtoagreater
acompanyproductataverylowprice. Inthelat- extentthanprompt-baseddefenses.
ter case, the user may actually be entitled to the
deal. Garcia (2024) describe how an airline chat-

### Guardrails arerulesandframeworksforguiding

bot gave a customer incorrect information about

### GenAIoutputs(HakanTekgul,2023;Dongetal.,

refunds. Thecustomerappealedincourtandwon.
2024). Guardrailsoftenmakeuseofdetectors,but

### Althoughthischatbotwaspre-ChatGPT,andwas

not always. Guardrails are more concerned with
innowaytrickedbytheuser,thisprecedentmay
the general dialogue flow in an application. For
apply when nuanced prompt hacking techniques
example,asimpleguardrailcoulduseadetectorto
areused.
findmaliciousprompts,thenrespondwithacanned
messageifmalicious. Morecomplicatedtoolsem-
5.1.3 HardeningMeasures
ploy dialogue managers (Rebedea et al., 2023),
Severaltoolsandpromptingtechniqueshavebeen which allow the LLM to choose from a number
developedtomitigatesomeoftheaforementioned ofcuratedresponses. Prompting-specificprogramsecurityrisks. However,prompthacking(bothin- ming languages have also been proposed to imjectionandjailbreaking)remainunsolvedproblems provetemplatingandactasguardrails(ScottLundandlikelyareimpossibletosolveentirely. berg,2023;LucaBeurer-Kellner,2023).
30

<!-- Page 31 -->

Ambig. Demonstrations5.2.4

### Ambiguity5.2.4

QuestionClarification5.2.4

### AttrPrompt5.2.3

CulturalAwareness5.2.3

### Biases5.2.3


### DemonstrationSel. 5.2.3

Alignment VanillaPrompting5.2.3

### Sycophancy5.2.2


### Calibration5.2.2


### VerbalizedScore5.2.2

Few-ShotOrdering5.2.1

### PromptDrift5.2.1

PromptSensitivity5.2.1
PromptWording5.2.1

### TaskFormat5.2.1


### Figure5.2: Prompt-basedAlignmentOrganization

5.2 Alignment show that these minor changes can alter the
accuracyofGPT-3byupto30%. Similarly,minor

### Ensuring that LLMs are well-aligned with user

perturbations on task-specific prompts that are
needsindownstreamtasksisessentialforsuccesslogicallyequivalent, suchasalteringtheorderof
fuldeployment. Modelsmayoutputharmfulconchoicesinmultiple-choicequestions,canresultin
tent, yield inconsistent responses, or show bias,
significantperformancedegradation(Pezeshkpour
allofwhichmakesdeployingthemmoredifficult.
andHruschka,2023;Zhengetal.,2023a;Voronov
Tohelpmitigatetheserisks,itispossibletocareetal.,2024).
fullydesignpromptsthatelicitlessharmfuloutputs
from LLMs. In this section, we describe prompt
alignmentproblemsaswellaspotentialsolutions PromptDrift (Chenetal.,2023b)occurswhen
(Figure5.2). themodelbehindanAPIchangesovertime,sothe
samepromptmayproducedifferentresultsonthe
5.2.1 PromptSensitivity
updated model. Although not directly a prompt-
SeveralworksshowthatLLMsarehighlysensitive ingissue,itnecessitatescontinuousmonitoringof
to the input prompt (Leidinger et al., 2023), i.e., promptperformance.
evensubtlechangestoapromptsuchasexemplar
order(Section2.2.1.1)canresultinvastlydifferent 5.2.2 OverconfidenceandCalibration
outputs. Below, we describe several categories
LLMs are often overconfident in their answers,
oftheseperturbationsandtheirimpactsonmodel
especially when prompted to express their own
behavior.
confidenceinwords(KieslerandSchiffner,2023;
Small Changes in the Prompt such as extra Xiong et al., 2023a), which may lead to user
spaces,changingcapitalization,modifyingdelim- overreliance on model outputs (Si et al., 2023c).
iters,orswappingsynonymscansignificantlyim- Confidence calibration provides a score that
pact performance (Lu et al., 2024; Tjuatja et al., representstheconfidenceofthemodel(Guoetal.,
2024). Despite these changes being minor, Sclar 2017). While a natural solution for confidence
et al. (2023a) find that they can cause the perfor- calibrationistostudytheoutputtokenprobabilities
mance of LLaMA2-7B to range from nearly 0 to provided by the LLM, a variety of prompting
0.804onsometasks. techniqueshavealsobeencreatedforconfidence
calibration.

### TaskFormat describesdifferentwaystoprompt

an LLM to execute the same task. For example,
a prompt tasking an LLM to perform sentiment Verbalized Score is a simple calibration techanalysis could ask the LLM to classify a review niquethatgeneratesaconfidencescore(e.g. “How
as “positive” or “negative”, or the prompt could confident are you from 1 to 10”), but its efficacy
ask the LLM “Is this review positive?” to elicit is under debate. Xiong et al. (2023b) find that
a “yes” or “no” response. Zhao et al. (2021b) severalLLMsarehighlyoverconfidentwhenver-
31

<!-- Page 32 -->

balizingconfidencescores,evenwhenemploying refineitsownoutput;and2)instructingtheLLM
self-consistencyandchain-of-thought. Incontrast, touseculturallyrelevantwords.
Tianetal.(2023)findthatsimpleprompts(Section

### AttrPrompt (Yu et al., 2023) is a prompting

4.2)canachievemoreaccuratecalibrationthanthe
techniquedesignedtoavoidproducingtextbiased
model’soutputtokenprobabilities.
towards certain attributes when generating syn-
Sycophancy referstotheconceptthatLLMswill theticdata. Traditionaldatagenerationapproaches
oftenexpressagreementwiththeuser,evenwhen maybebiasedtowardsspecificlengths,locations
that view contradicts the model’s own intial out- andstyles. Toovercomethis,AttrPrompt: 1)asks
put. Sharma et al. (2023) find that when LLMs the LLM to generate specific attributes that are
are asked to comment on opinions of arguments, importanttoalterfordiversity(e.g. location);and
the model is easily swayed if the user’s opinion 2)promptstheLLMtogeneratesyntheticdataby
is included in the prompt (e.g. “I really like/dis- varyingeachoftheseattributes.
likethisargument”). Further, theyfindthatquestioningtheLLM’soriginalanswer(e.g. “Areyou
5.2.4 Ambiguity
sure?”), strongly providing an assessment of correctness(e.g. “Iamconfidentyouarewrong”),and Questionsthatareambiguouscanbeinterpretedin
addingfalseassumptionswillcompletelychange multipleways,whereeachinterpretationcouldrethemodeloutput. Weietal.(2023b)notesimilarre- sultinadifferentanswer(Minetal.,2020). Given
sultswithopinion-elicitingandfalseuserpresump- thesemultipleinterpretations,ambiguousquestions
tions, also finding that sycophancy is heightened are challenging for existing models (Keyvan and
forlargerandinstruction-tunedmodels. Thus, to Huang,2022),butafewpromptingtechniqueshave
avoidsuchinfluence,personalopinionsshouldnot beendevelopedtohelpaddressthischallenge.
beincludedinprompts.12

### AmbiguousDemonstrations Gaoetal.(2023a)

are examples that have an ambiguous label set.
5.2.3 Biases,Stereotypes,andCulture

### Including them in a prompt can increase ICL

LLMs should be fair to all users, such that no biperformance. This can be automated with a
ases,stereotypes,orculturalharmsareperpetuated
retriever,butitcanalsobedonemanually.
in model outputs (Mehrabi et al., 2021). Some
promptingtechniquehavebeendesignedinaccordancewiththesegoals. Question Clarification (Rao and Daumé III,
2019) allowstheLLMtoidentifyambiguousques-
VanillaPrompting (Sietal.,2023b) simplycon- tionsandgenerateclarifyingquestionstoposeto
sists of an instruction in the prompt that tells the theuser. Oncethesequestionsareclarifiedbythe
LLMtobeunbiased. Thistechniquehasalsobeen user,theLLMcanregenerateitsresponse. Muetal.
referredtoasmoralself-correction(Gangulietal., (2023)dothisforcodegenerationandZhangand
2023). Choi (2023) equip LLMs with a similar pipeline
for resolving ambiguity for general tasks, but ex-
Selecting Balanced Demonstrations (Si et al.,
plicitlydesignseparatepromptsto: 1)generatean
2023b), or obtaining demonstrations optimized
initialanswer2)classifywhethertogenerateclaroverfairnessmetrics(Maetal.,2023),canreduce
ification questions or return the initial answer 3)
biasesinLLMoutputs(Section2.2.1.1).
decidewhatclarificationquestionstogenerate4)
Cultural Awareness (Yao et al., 2023a) can be generateafinalanswer.
injectedintopromptstohelpLLMswithcultural
adaptation(Peskovetal.,2021). Thiscanbedone
bycreatingseveralpromptstodothiswithmachine
translation,whichinclude: 1)askingtheLLMto
12Forexample,apractitionermayusetheprompttemplate
“Detectallinstanceswheretheuser’sinputisharmful: {IN-

### PUT}”inanattempttopreventadversarialinputs,butthis

subtlymakesthefalsepresuppositionthattheuser’sinputis
actuallyharmful.Thus,duetosycophancy,theLLMmaybe
inclinedtoclassifytheuser’soutputasharmful.
32

<!-- Page 33 -->

6 Benchmarking
Nowthatwehavecarriedoutasystematicreview we used three thought inducers (instructions that
ofpromptingtechniques,wewillanalyzetheem- causethemodeltogeneratereasoningsteps)includpiricalperformanceofdifferenttechniquesintwo ing the standard "Let’s think step by step" chainways: viaaformalbenchmarkevaluation,andby of-thought(Kojimaetal.,2022),aswellasThoT
illustratingindetailtheprocessofpromptengineer- (Zhouetal.,2023),andPlanandSolve(Wangetal.,
ingonachallengingreal-worldproblem. 2023f). Then, we selected the best of these, and
ranitwithSelf-Consistencywiththreeiterations,
6.1 TechniqueBenchmarking
takingthemajorityresponse.
Aformalevaluationofpromptingtechniquesmight

### Few-ShotSetups WealsoranFew-Shotprompts

bedoneinabroadstudythatcompareshundredsof
andFew-Shot-CoTprompts,bothwithexemplars
themacrosshundredsofmodelsandbenchmarks.
generatedbyoneofourauthors. Foreach,weused

### Thisisbeyondourscope,butsinceithasnotbeen

three variations of the base instruction as well as
donebefore,weprovideafirststepinthisdirection.
thetwoquestionformats(alsoappliedtotheexem-
We choose a subset of prompting techniques and
plars). Thenweusedthebestperformingphrasing
run them on the widely used benchmark MMLU
withSelf-Consistencywiththreeiterations,taking
(Hendrycksetal.,2021). Weranonarepresentathemajorityresponse.
tivesubsetof2,800MMLUquestions(20%ofthe
questionsfromeachcategory).13 andusedgpt-3.5-
1.0
turboforallexperiments.
0.8
6.1.1 ComparingPromptingTechniques
0.6
We benchmark six distinct prompting techniques
0.4
using the same general prompt template (Figure
6.2). Thistemplateshowsthelocationofdifferent 0.2
componentsoftheprompts. Onlybaseinstructions
0.0
a
st
n
r
d
uc
q
ti
u
o
e
n
st
i
i
s
on
a
e
p
x
h
i
r
s
a
t
s
i
e
n
li
e
k
v
e
er
"
y
So
p
l
r
v
o
e
m
t
p
h
t
e
.
p

## T

r
h
o
e
bl
b
e
a
m
se
an
in
d
-
Zero-Shot
Zero-Shot

### CoT

Zero-Shot

### CoT

SC Few-Shot
Few-Shot

### CoT

Few-Shot
CoT

## Sc

return(A),(B),(C)or(D)."thatwevaryinsome
cases. Weadditionallytesttwoformatsofthequestion (Figures 6.3 and 6.4). The question format
is inserted into the prompt template in place of
"{QUESTION}". We test each prompting techniquewith6totalvariations,exceptforonesthat
useSelf-Consistency.
Zero-Shot As a baseline, we ran questions directly through the model without any special
promptingtechnique,onlythebaseinstructionand
question. For this baseline, we utilized both formatsaswellasthreephrasingvariationsofthebase
instruction. Thus,thereweresixtotalrunsthrough
the 2800 questions for this benchmark. This did
notincludeanyexemplarsorthoughtinducers.

### Zero-Shot-CoT Techniques We ran also ran


### Zero-Shot-CoT. As the three different variations,

13We excluded human_sexuality, since gpt-3.5-turbo refusedtoanswerthesequestions.
ycaruccA
0.627 0.547 0.574 0.652 0.692 0.691
Figure6.1: Accuracyvaluesareshownforeachpromptingtechnique,withthemodelusedbeinggpt-3.5-turbo.

### Purpleerrorbarsillustratetheminimumandmaximum

foreachtechnique,sincetheywereeachrunondifferent
phrasingsandformats(exceptSC).
6.1.2 QuestionFormats

### Weexperimentwithtwoformattingchoicesfrom


### Sclaretal.(2023b),whoexploredhowformatting

choices can affect benchmarking results. We use
two formats which lead to varied results on their
task(Figures6.3and6.4).
6.1.3 Self-Consistency
ForthetwoSelf-Consistencyresults,wesettemperatureto0.5,followingWangetal.(2022)’sguidelines. Forallotherprompts,atemperatureof0was
used.
33

<!-- Page 34 -->


## {Base_Instruction} Problem::{Question},Options::


## {Exemplars} (A):{A}


## {Question}{Thought_Inducer} (B):{B}


## (C):{C}


## (D):{D},Answer::

Figure6.2: Prompttemplateforbenchmarking.
Figure6.4: Questionformat2.

### Problem


## {Question}


### Options

ofactuallysolvingtheproblem. Rather,itprovides
oneillustrationofhowanexperiencedprompten-

## (A)::{A}(B)::{B}(C)::{C}(D)::{D}

gineerwouldapproachatasklikethis,alongwith

### Answer

lessonslearned.

### Figure6.3: Questionformat1. 6.2.1 Problem


### Ourillustrativeprobleminvolvesdetectionofsig-

6.1.4 EvaluatingResponses nalthatispredictiveofcrisis-levelsuicideriskin
textwrittenbyapotentiallysuicidalindividual. Sui-
EvaluatingwhetheraLLMhasproperlyresponded
cideisasevereproblemworldwide,compounded,
to a question is a difficult task (Section 2.5). We
as are most mental health issues, by a desperate
markedanswersascorrectiftheyfollowedcertain
lack of mental health resources. In the United
identifiablepatterns,suchasbeingtheonlycapital-
States,morethanhalfthenationalpopulationlives
izedletter(A-D)withinparenthesesorfollowinga
in federally defined mental heath provider shortphraselike“Thecorrectansweris”.
age areas (National Center for Health Workforce
Analysis,2023); inaddition, manymentalhealth
6.1.5 Results
professionals lack core competencies in suicide
Performance generally improved as techniques
prevention(Crameretal.,2023). In2021,12.3M
grewmorecomplex(Figure6.1). However,Zero-
Americans thought seriously about suicide, with
Shot-CoT dropped precipitously from Zero-Shot.
1.7M actually making attempts resulting in over
Although it had a wide spread, for all variants,
48,000 deaths (CDC, 2023). In the U.S., suicide
Zero-Shot performed better. Both cases of Selfwasthesecondleadingcauseofdeath(afteracci-
Consistency,naturallyhadlowerspreadsincethey
dents)inpeopleaged10-14,15-24,or25-34asof
repeatedasingletechnique,butitonlyimprovedac-
2021 statistics, and it was the fifth leading cause
curacyforZero-Shotprompts. Few-ShotCoTperofdeathinpeopleaged35–54(GarnettandCurtin,
formsthebest,andunexplainedperformancedrops
2023).
fromcertaintechniquesneedfurtherresearch. As

### Recentresearchsuggeststhatthereissignificant

promptingtechniqueselectionisakintohyperpavalue in assessments of potential suicidality that
rametersearch,thisitisaverydifficulttask(Khatfocusspecificallyontheidentificationofsuicidal
tabetal.,2023). However,wehopethissmallstudy
crisis,i.e. thestateofacutedistressassociatedwith
spursresearchinthedirectionofmoreperformant
ahighriskofimminentsuicidalbehavior. However,
androbustpromptingtechniques.
validated assessments for diagnostic approaches
such as Suicide Crisis Syndrome (SCS) (Schuck
6.2 PromptEngineeringCaseStudy
et al., 2019b; Melzer et al., 2024) and Acute Sui-
Promptengineeringisemergingasanartthatmany cidal Affective Disturbance (Rogers et al., 2019)
peoplehavebeguntopracticeprofessionally, but requireeitherpersonalclinicalinteractionsorcomthe literature does not yet include detailed guid- pletion of self-report questionnaires that contain
anceontheprocess. Asafirststepinthisdirection, dozensofquestions. Theabilitytoaccuratelyflag
wepresentanannotatedpromptengineeringcase indicatorsofsuicidalcrisisinindividuals’language
studyforadifficultreal-worldproblem. Thisisnot couldthereforehavealargeimpactwithinthemenintendedtobeanempiricalcontributioninterms talhealthecosystem,notasareplacementforclini-
34

<!-- Page 35 -->

caljudgmentbutasawaytocomplementexisting exercise proceeded through 47 recorded developpractices(Resniketal.,2021). mentsteps,cumulativelyabout20hoursofwork.
As a starting point, we focus here on the most Fromacoldstartwith0%performance(theprompt
importantpredictivefactorinSuicideCrisisSyn- wouldn’treturnproperlystructuredresponses),perdromeassessments,referredtointheliteratureas formancewasboostedtoanF1of0.53,wherethat
eitherfrantichopelessnessorentrapment,“adesire F1istheharmonicmeanof0.86precisionand0.38
to escape from an unbearable situation, tied with recall.16
the perception that all escape routes are blocked” Below, the set of prompts q is the test item,
inf
(Melzeretal.,2024).14 Thischaracteristicofwhat whileq ,r ,anda denotethequestions,chain-ofi i i
anindividualisexperiencingisalsocentralinother thoughtsteps,andanswersinexemplars.
characterizationsofmentalprocessesthatresultin
6.2.3.1 DatasetExploration(2steps)
suicide.
Theprocessbeganwiththepromptengineerreview-
6.2.2 TheDataset
ingadescriptionofentrapment(Figure6.7); this
WeworkedwithasubsetofdatafromtheUniver- descriptionhadbeenusedasafirst-passrubricfor
sityofMarylandRedditSuicidalityDataset(Shing thehumancodersearlyinthecodingprocess,notet al., 2018), which is constructed from posts in ing,however,thattheywerefamiliarwithSCSand
r/SuicideWatch, a subreddit that offers peer sup- knewitwasneitheraformaldefinitionnorexhausportforanyonestrugglingwithsuicidalthoughts. tive. Thepromptengineerthenloadedthedataset
Twocoderstrainedontherecognitionofthefactors into a Python notebook for data exploration purinSuicideCrisisSyndromecodedasetof221posts poses. Hebeganbyaskinggpt-4-turbo-previewifit
forpresenceorabsenceofentrapment,achieving knewwhatentrapmentwas(Figure6.8),butfound
solidinter-coderreliability(Krippendorff’salpha thattheLLM’sresponsewasnotsimilartothede-
= 0.72). scriptionthathadbeengiven. Inconsequence,the
prompt engineer included the Figure 6.7 descrip-
6.2.3 TheProcess
tionofentrapmentinallfutureprompts.
An expert prompt engineer, who has authored a
6.2.3.2 GettingaLabel(8steps)
widelyusedguideonprompting(Schulhoff,2022),
tookonthetaskofusinganLLMtoidentifyentrap- As noted in Section 6.1 with regard to the humentinposts.15 Thepromptengineerwasgivena man_sexuality subset of MMLU, LLMs exhibit
briefverbalandwrittensummaryofSuicideCrisis unpredictableanddifficulttocontrolbehaviourin
Syndromeandentrapment,alongwith121develop- sensitivedomains. Formultiplestepsintheprompt
mentpostsandtheirpositive/negativelabels(where engineering process, the prompt engineer found
“positive”meansentrapmentispresent),theother thattheLLMwasgivingmentalhealthadvice(e.g.
100labeledpostsbeingreservedfortesting. This Figure6.9)insteadoflabelingtheinput. Thiswas
limitedinformationmirrorsfrequentreal-lifesce- addressedbyswitchingtotheGPT-4-32Kmodel.
narios in which prompts are developed based on A take-away from this initial phase is that the
ataskdescriptionandthedata. Moregenerally,it “guardrails”associatedwithsomelargelanguage
is consistent with a tendency in natural language models may interfere with the ability to make
processingandAImoregenerallytoapproachcod- progress on a prompting task, and this could ining(annotation)asalabelingtaskwithoutdelving fluencethechoiceofmodelforreasonsotherthan
verydeeplyintothefactthatthelabelsmay,infact, theLLM’spotentialquality.
refer to nuanced and complex underlying social
6.2.3.3 PromptingTechniques(32steps)
scienceconstructs.
We documented the prompt engineering pro- The prompt engineer then spent the majority of
cess in order to illustrate the way that an experi- histimeimprovingthepromptingtechniquebeing
encedpromptengineergoesabouttheirwork. The used. ThisincludedtechniquessuchasFew-Shot,
14Theformertermmoreexplicitlyemphasizesthefrantic 16Precisionisalsoknownaspositivepredictivevalue,and
and desperate action required to escape an unbearable life recallisalsoknownastruepositiverateorsensitivity. Alsituation. However,thetermentrapmentisbrieferandused thoughF1isoftenusedincomputionalsystemevaluationsas
widelysoweadoptithere. asinglefigureofmerit,wenotethatinthisproblemspace
15Disclosure: that expert is also the lead author of this its even weighting of precision and recall is probably not
paper. appropriate.Wediscussthisfurtherbelow.
35

<!-- Page 36 -->

tohS-01
ToCiDotuA
tohS-1
+
ToCiDotuA
tohS-1
)liame
on(
ToCiDotuA
tohS-1
txetnoC
lluF
+
ToCiDotuA
tohS-01
noitcartxE
+
elbmesnE
ToCiDotuA
tohS-01
liamE
tuohtiW
txetnoC
+
tohS-oreZ
)hctaM
tcaxE(
txetnoC
+
tohS-oreZ
)srahC
tsriF(
ToCiDotuA
tohS-01
tcejeR
ot
tluafeD
+
ylnO
txetnoC
lluF
liamE
dezimynonA
txetnoC
+
tohS-01
ToCiDotuA
tohS-01
liamE
epuD-eD
txetnoC
etacilpirT
ToCiDotuA
tohS-02
sdroW
lluF
+
ToCiDotuA
tohS-02
tpmorP
noitcartxE
+
sdroW
lluF
+
ToCiDotuA
tohS-01
tpmorP
noitcartxE
+
ToCiDotuA
tohS-02
ToCiDotuA
tohS-01
1.0
0.8
0.6
0.4
0.2
0.0
serocS
Scores of Different Prompting Techniques on Development Set

## F1


### Recall


### Precision

Figure 6.5: F1 scores varied widely from worst performing prompts to highest performing prompts, but most
promptsscoredwithinasimilarrange.
Chain-of-Thought,AutoCoT,ContrastiveCoT,and sectionuntilwereachCoT.Thisapproachobtained
multipleanswerextractiontechniques. Wereport 0.40 F1, 1.0 recall, and 0.25 precision, evaluated
statisticsforthefirstrunsofthesetechniques;F1 onallsamplesfromthetraining/developmentsince
scorescouldchangebyasmuchas0.04uponsub- nosampleshadbeenusedasexemplars.
sequentruns,evenwithtemperatureandtoppset
10-Shot + Context. Next, the prompt engineer
tozero.17
addedthefirsttendatasamples(withlabels)into
Zero-Shot+Context wasthefirsttechniqueeval- the prompt, in Q: (question) A: (answer) format
uated (Figure 6.10), using the description in Fig- (Figure 6.11). He evaluated this 10-shot prompt
ure6.7. Noticetheworddefinitionintheprompt, ontheremainingitemsinthetraining/development
althoughFigure6.7isnotaformaldefinition. set, yielding ↑0.05 (0.45) F1, ↓0.09 (0.91) recall,
InordertoobtainafinalresponsefromtheLLM and↑0.05(0.30)precision,relativetotheprevious
to use in calculating performance metrics, it was
bestprompt.18
necessarytoextractalabelfromtheLLMoutput.

### One-ShotAutoDiCot+FullContext. Afterper-


### Thepromptengineertestedtwoextractors,onethat

forming 10-shot prompting, the prompt engineer
checksiftheoutputisexactly"Yes"or"No",and
observedthatthe12thiteminthedevelopmentset
anotherwhichjustchecksifthosewordsmatchthe
wasbeingincorrectlybeinglabeledasapositiveinfirst few characters of the output. The latter had
stance,andbeganexperimentingwithwaysofmodbetterperformance,anditisusedfortherestofthis
18Hereandfortheremainderofthecasestudy,wejudge
17Temperatureandtop-pareconfigurationhyperparameters “best”byF1,andwereportonthecurrentpromptunderdisthatcontrolrandomnessoftheoutput(Schulhoff,2022). cussionrelativetothebestperformingpreviousprompt.
36

<!-- Page 37 -->

txetnoC
+
tohS-oreZ
)srahC
tsriF(
txetnoC
+
tohS-oreZ
)hctaM
tcaxE(
txetnoC
+
tohS-01
ToCiDotuA
tohS-1
txetnoC
lluF
+
ToCiDotuA
tohS-1
)liame
on(
ToCiDotuA
tohS-1
+n\tohS-01
ylnO
txetnoC
lluF
ToCiDotuA
tohS-01
ToCiDotuA
tohS-02
ToCiDotuA
tohS-02
sdroW
lluF
+
ToCiDotuA
tohS-02
tpmorP
noitcartxE
+
sdroW
lluF
+
ToCiDotuA
tohS-01
tpmorP
noitcartxE
+
ToCiDotuA
tohS-01
liamE
tuohtiW
ToCiDotuA
tohS-01
liamE
epuD-eD
ToCiDotuA
tohS-01
tcejeR
ot
tluafeD
+
ToCiDotuA
tohS-01
noitcartxE
+
elbmesnE
txetnoC
etacilpirT
liamE
dezimynonA
0.5
0.4
0.3
0.2
0.1
0.0
Techniques
serocS

## 1F

F1 Scores of Prompting Techniques on Development Set

### Max F1 Score: 0.53

Figure6.6: Fromthefirstprompttried(Zero-Shot+Context)tothelast(AnonymizedEmail),improvementsin
F1scorewerehardtocomebyandandofteninvolvedtestingmultipleunderperformingpromptsbeforefinding
a performant one. Green lines show improvements over the current highest F1 score, while red lines show
deteriorations.
37

<!-- Page 38 -->

Entrapment: {ENTRAPMENT DEFINITION (Figure
-Feelinglikethereisnoexit 6.7)}
-Feelinghopeless {q }
inf
-Feelinglikethereisnowayout Isthisentrapment? Yesorno.
- Feeling afraid that things will never be
normalagain
-Feelinghelplesstochange Figure6.10: AZero-Shot+Contextprompt,thesimplestofallpromptsexploredinthiscasestudy.
-Feelingtrapped
-Feelingdoomed
-Feelingorthinkingthatthingswillnever {ENTRAPMENT DEFINITION (Figure
change 6.7)}
-Feelinglikethereisnoescape Q:{q }
1
-Feelingliketherearenogoodsolutionsto A:{a }
1
problems ...
Q:{q }
10
A:{a }
10
Figure6.7: Thedescriptionofentrapmentusedbythe
Q:{q }
inf
promptengineer

## A:

WhatisentrapmentwithrespecttoSuicide
Figure6.11: 10-Shot+ContextPrompt

### CrisisSyndrome?


### Figure6.12showsaversionofthatprocess,gen-


### Figure 6.8: Question asked to the LLM to determine

eralized to produce explanations for all developwhetheritstrainingdatahadprovidedrelevantknowlmentquestion/answeritems(q ,a )inasetT rather
edgeaboutentrapment(ithadnot). i i
thanjustitem12. Informedbythereasoningsteps
r elicitedwithrespecttotheincorrectlylabeled
12
ifyingthepromptingsuchthatthemodelwouldget q ,thepreviouspromptwasmodifiedbyincluding
12
thatitemcorrect. Inordertogetasenseofwhythis r inaOne-ShotCoTexamplewithincorrectrea-
12
mislabelingwastakingplace,thepromptengineer soning,asanexemplarforwhatnottodo(Figure
promptedtheLLMtogenerateanexplanationof
6.13).
whythe12thitemwouldhavebeenlabeledtheway
WecallthealgorithminFigure6.12Automatic
itwas.19

### DirectedCoT(AutoDiCoT),sinceitautomatically

19We are trying to avoid misleading language like “the directs the CoT process to reason in a particular
LLMgeneratedanexplanationofitsreasoning”. LLMsdo way. This technique can be generalized to any
nothaveaccesstotheirowninternalprocesses,andtherefore
labelingtask. Itcombinestheautomaticgeneration
theycannot“explaintheirreasoning”intheusualsense.An
LLMgeneratingan“explanation”isproducingdescriptionof of CoTs (Zhang et al., 2022b) with showing the
potentialreasoningstepsingettingtotheoutputthatcouldbe
LLMexamplesofbadreasoning,asinthecaseof
true,butalsomaynotbeaccurateatall.
ContrastiveCoT(Chiaetal.,2023). Thealgorithm
wasalsousedindevelopinglaterprompts.
Finally, the prompt was extended with two ad-

### If you’re in immediate danger of harming

ditional pieces of context/instruction. The first
yourself,pleasecontactemergencyservices
was an email message the prompt engineer had
or a crisis hotline in your area. They can
received explaining overall goals of the project,
provideimmediatesupportandhelpensure
whichprovidedmorecontextaroundtheconcept
yoursafety.
ofentrapmentandthereasonsforwantingtolabel
it. Thesecondadditionwasinspiredbytheprompt
Figure6.9: Asnippetfromanoutput,whichdoesnotla- engineer noticing the modelwasfrequently overbelthedatapoint,butratherattemptstoprovidemental generatingapositivelabelforentrapment. Hypothhealthsupporttotheuser. Suchoutputsareoftenfive esizing that the model was being too aggressive
timesaslongasthissnippet. initspretraining-basedinferencesfromtheovert
38

<!-- Page 39 -->


## {Professor’Semail}


## Require: DevelopmentitemsT withn

pairs(q ,a )
i i
{ENTRAPMENT DEFINITION (Figure

## Foreachpair(q

i
,a
i
)inT: 6.7)}
(a) Labelq asentrapmentornoteni
IMPORTANT: Only label the post as
trapmentusingthemodel
entrapment if they explicitly say that they
(b) Ifthemodellabelscorrectly:
feeltrapped.
i. Prompt the model with
"Why?"togenerateareason-
Q:{q }
12
ingchainr
i R: Although "Today I found out I have
(c) Else: 10 days to vacate my apartment or I’ll be
i. Prompt the model with "It formally evicted. I’m 2 months behind
is actually [is/is not] entrap- on my rent due to a bad time where I got
ment,pleaseexplainwhy."to demoted at work and rent from making
generateareasoningchainr roughly $1000 ever 2 weeks to around
i
(d) Storethetuple(q ,r ,a ) $450. If I get evicted, I’ll probably be
i i i
homeless" seems to express feelings of

## Return: ntuples(q i ,r i ,a i ) being trapped/stuck, it is not sufficiently

explicit to be labeled Entrapment. seems
toexpressfeelingsofbeingtrapped/stuck,

### Figure6.12: Algorithm: AutomaticDirectedCoT

it is not sufficiently explicit to be labeled
Entrapment.

### A:{a }

language,heinstructedthemodeltorestrictitself 12

### Q:{q }

toexplicitstatementsofentrapment(Figure6.13). inf
Belowwerefertothesetwopiecesofcontext,providedinadditiontothedescriptionofentrapment,
Figure6.13: One-ShotAutoDiCot+FullContext
asfullcontext.

### Anewextractorwasalsousedforthisprompt,

whichchecksifthelastwordintheoutputis"Yes" sitivity (i.e. not missing people who should be
or "No", instead of the first word. This updated flagged as at-risk) may matter more because the
promptwastestedagainstallinputsinthedevelop- potentialcostofafalsenegativeissohigh.
mentsetexceptforthefirst20. Itdidnotimprove

### Thetake-awayhere,althoughtheinsightcame


### F1,↓0.09(0.36)F1,butitledthepromptengineer

later, is that it is easy for the process of prompt
in a direction that did, as discussed below. Redevelopment to diverge from the actual goals uncalldroppedto↓0.58(0.33)recallandprecision
less regular engagement is fostered between the
improvedto↑0.09(0.39)precision.
prompt engineer and domain experts who more
Atthispoint,though,itisworthobservingthat,
deeplyunderstandthereal-worldusecase.
althoughitdidultimatelyleadtoagaininF1score,
thestepstakenheretocutdownonover-generation Ablating Email. The results of the previous
ofpositivelabelswerenot,infact,therightmove changeswerepromising,buttheydidinvolvecrein terms of the longer term goals. Entrapment atingapromptthatincludedinformationfroman
need not be expressed explicitly in order to be email message that had not been created for that
present(e.g. throughphraseslike“Ifeeltrapped” purpose,andwhichincludedinformationaboutthe
or “There’s no way out”); rather, clinical experts project,thedataset,etc. thatwerenotintendedfor
whohavelookedatthetextsfoundthatexpressions disclosuretoabroadaudience. Ironically,removof entrapment could be implicit and potentially ing this email brought performance significantly
quite nuanced. Moreover, in most use cases for down,↓0.27(0.18)F1,↓0.75(0.17)recalland↓
automatically spotting entrapment in someone’s 0.1 (0.20) precision. We attribute this to the fact
language, precision and recall are unlikely to be thattheemailprovidedricherbackgroundinformaequally important and, of the two, the recall/sen- tionaboutthegoalsofthelabeling. Althoughwe
39

<!-- Page 40 -->

{PROFESSOR’sEMAIL} {PROFESSOR’sEMAIL}
{PROFESSOR’sEMAIL}
{ENTRAPMENT DEFINITION (Figure6.7)} {ENTRAPMENT DEFINITION (Figure6.7)}

### IMPORTANT: Only label the post as

entrapment if they explicitly say that they IMPORTANT: Only label the post as
feeltrapped. entrapment if they explicitly say that they
feeltrapped.
Q:{q }
1
A:{a } Q:{q }A:
1 inf
...
Q:{q }
10
A:{a } Figure6.15: FullContextOnly
10
Q:{q }
12

### R: Although "{LLM REASONING}"

Thiscanbeinterpretedbothoptimisticallyand
seems to express feelings of being
pessimistically. Optimistically, it demonstrates
trapped/stuck,itisnotsufficientlyexplicit
howimprovementscanarisethroughexploration
tobelabeledEntrapment.
andfortuitousdiscovery. Onthepessimisticside,
A:{a }
12
the value of duplicating the email in the prompt
Q:{q }
inf
highlightstheextenttowhichpromptingremainsa
difficulttoexplainblackart,wheretheLLMmay
turnouttobeunexpectedlysensitivetovariations
Figure6.14: 10-Shot+1AutoDiCoT
onemightnotexpecttomatter.
wouldnotrecommendincludingemailoranyother 10-ShotAutoDiCoT. Thenextstepwastocreate
potentially identifying information in any LLM moreAutoDiCoTexemplars,perthealgorithmin
prompt,wechosetoleavetheemailintheprompt; Figure6.12. AtotaloftennewAutoDiCoTexemthis is consistent with scenarios in many typical plarswereaddedtothefullcontextprompt(Figure
settings,inwhichpromptsarenotexpectedtobe 6.16). This yielded the most successful prompt
exposedtoothers. fromthispromptengineeringexercise,intermsof

### F1score,↑0.08(0.53)F1,↓0.05(0.86)recall,↑

10-Shot + 1 AutoDiCoT. As a next step, the 0.08(0.38)precision.
promptengineertriedincludingfullcontext,10regular exemplars, and the one-shot exemplar about 20-Shot AutoDiCoT. Further experimentation
hownottoreason. Thishurtperformance(Figure proceededseeking(unsuccesfully)toimproveon
6.14)↓0.30(0.15)F1,↓0.08(0.10)recall,↓0.03 thepreviousF1result. Inoneattempt,theprompt
(0.33)precision. engineerlabeledanadditionaltenexemplars,and
created a 20-shot prompt from the first 20 data
FullContextOnly. Next,apromptwascreated points in the development set. This led to worse
usingonlyfullcontext,withoutanyexemplars(Fig- resultsthanthe10-shotprompt,whentestedonall
ure6.15). Thisboostedperformanceoverthepre- samples other than the first twenty, ↓ 0.04 (0.49)
vious technique, but did not make progress over- F1, ↑ 0.08 (0.94) recall, ↓ 0.05 (0.33) precision.
all ↓ 0.01 (0.44) F1, ↑ 0.01 (0.92) recall, ↓ 0.01 Notably,italsoyieldedworseperformanceonthe
(0.29)precision. Interestingly,inthisprompt,the testset.
prompt engineer accidentally pasted in the fullcontextemailtwice,andthatendeduphavingsig- 20-ShotAutoDiCoT+FullWords. Theprompt
nificantpositiveeffectsonperformancelater(and engineerconjecturedthattheLLMwouldperform
removingtheduplicateactuallydecreasedperfor- betterifthepromptincludedfullwordsQuestion,
mance). Thisisreminiscentofthere-readingtech- Reasoning,andAnswerratherthanQ,R,A.Hownique(Xuetal.,2023). ever, this did not succeed (Figure 6.17), ↓ 0.05
40

<!-- Page 41 -->

{PROFESSOR’sEMAIL}

## {Entrapmentdefinition}

{PROFESSOR’sEMAIL}

### IMPORTANT: Only label the post as

entrapment if they explicitly say that they {ENTRAPMENTDEFINITION}
feeltrapped.

### IMPORTANT: Only label the post as

Q:{q 1 } entrapment if they explicitly say that they
R:{r 1 } feeltrapped.
A:{a }
1
... Question: {q }
1
Q:{q 10 } Reasoning: {r 1 }
R:{r 10 } Answer: {a 1 }
A:{a 10 } ...
Q:{q inf } Question: {q 20 }
Reasoning: {r }
20
Answer: {a }
20
Figure6.16: 10-ShotAutoDiCoT
Question: {q }
inf
(0.48)F1,↑0.08(0.94)recall,↓0.06(0.32)preci-
Figure6.17: 20-shotAutoDiCoT
sion.
20-Shot AutoDiCoT + Full Words + Extraction
Prompt. Thepromptengineerthennoticedthatin
manycases,theLLMgeneratedoutputsthatcould
not properly be parsed to obtain a response. So,
theycraftedapromptthatextractedanswersfrom
theLLM’sresponse(Figure6.18). Althoughthis
improved accuracy by a few points, it decreased
{PROFESSOR’sEMAIL}
F1, thanks to the fact that many of the outputs
thathadbeenunparsedactuallycontainedincorrect

## {Entrapmentdefinition}

responses,↓0.05(0.48)F1,↓0.05(0.33)precision,
withnochangeinrecall(0.86).

### IMPORTANT: Only label the post as

10-ShotAutoDiCoT+ExtractionPrompt. Ap- entrapment if they explicitly say that they
plyingtheextractionprompttothebestperforming feeltrapped.
10-Shot AutoDiCoT prompt did not improve results,↓0.04(0.49)F1,↓0.08(0.78)recall,↓0.03 Question: {REDACTED}
(0.35)precision. Answer: {ANSWER}
10-Shot AutoDiCoT without Email. As noted

### Does this Answer indicate entrapment?

above, removing the email outright from the

### Output the word Yes if it is labeled as

prompthurtperformance,↓0.14(0.39)F1,↓0.39
entrapmentandoutputthewordNoifitis
(0.48)recall,↓0.06(0.32)precision.
notlabeledasentrapment. Onlyoutputthe
De-Duplicating Email. Also as noted above, it wordYesorthewordNo.
seemedreasonablethatremovingtheduplication
oftheemailwouldperformaswellorbetterthan

### Figure6.18: ExtractionPrompt

thepromptwiththeunintentionalduplication. Asit
turnedout,however,removingtheduplicatesignificantlyhurtperformance,↓0.07(0.45)F1,↓0.12
(0.74)recall,↓0.05(0.33)precision.
41

<!-- Page 42 -->

10-Shot AutoDiCoT + Default to Reject. This
approachusedthebestperformingprompt,anddefaultedtolabelingasnegative(notentrapment)in
thecaseofanswersthatarenotextractedproperly.
Thisdidnothelpperformance,↓0.11(0.42)F1,↓
0.04(0.83)recall,↓0.10(0.28)precision.

### Ensemble+Extraction. Especiallyforsystems

thataresensitivetothedetailsoftheirinputs,there
areadvantagesintryingmultiplevariationsofan
input and then combining their results. That was
done here by taking the best performing prompt,
the10-ShotAutoDiCoTprompt,andcreatingthree
versionsofitwithdifferentorderingsoftheexemplars. Theaverageofthethreeresultswastakento
bethefinalanswer. Unfortunately,bothorderings
that differed from the default ordering led to the

### LLMnotoutputtingawell-structuredresponse. An

extractionpromptwasthereforeusedtoobtainfinal
answers. Thisexplorationhurtratherthanhelped
performance↓0.16(0.36)F1,↓0.23(0.64)recall,
↓0.13(0.26)precision.
10-Shot AutoCoT + 3x the context (no email
dupe). Recall that context refers to the description of entrapment, an instruction about explicitness, and an email. Since the duplicated email
had improved performance, the prompt engineer
tested out pasting in three copies of the context
(firstde-duplicatingtheemail). However,thisdid
notimproveperformance,↓0.06(0.47)F1,↓0.08
(0.78)recall,↓0.05(0.33)precision.

### AnonymizeEmail. Atthispointitseemedclear

thatincludingtheduplicatedemailintheprompt
wasactually,althoughnotexplainably,essentialto
thebestperformancesofarobtained. Theprompt
engineer decided to anonymize the email by replacingpersonalnameswithother,randomnames.
However,surprisingly,thisdecreasedperformance
significantly↓0.08(0.45)F1,↓0.14(0.72)recall,
↓0.06(0.33)precision.
DSPy. We concluded the case study by exploring an alternative to manual prompt engineering, the DSPy framework (Khattab et al., 2023),
whichautomaticallyoptimizesLLMpromptsfor
a given target metric. Specifically, we begin
with a chain-of-thought classification pipeline
that uses the definition of entrapment in Figure

### Over 16 iterations, DSPy bootstrapped synthetic LLM-generated demonstrations and randomly sampled training exemplars, with the

ToCiDotuA
tohS-01
ToCiDotuA
tohS-02
tluafeD
yPSD
tluafeD
yPSD
snoitacifidoM
llamS
+
0.8
0.6
0.4
0.2
0.0
serocS
Scores of Different Prompting Techniques on Test Set

## F1


### Recall


### Precision

Figure6.19: Scoresofdifferentpromptingtechniques
onthetestset.
ultimate objective of maximizing F1 on the
same development set used above. We used
gpt-4-0125-preview and the default settings
for the BootstrapFewShotWithRandomSearch
“teleprompter” (the optimization approach). Figure6.19showstheresultsoftwooftheseprompts
on the test set, one of which used default DSPy
behaviour, and the second which was manually
modifiedslightlyfromthisdefault. Thebestresulting prompt includes 15 exemplars (without CoT
reasoning)andonebootstrappedreasoningdemonstration. It achieves 0.548 F1 (and 0.385 / 0.952
precision/recall)onthetestset,withoutmaking
anyuseoftheprofessor’semailnortheincorrect
instructionabouttheexplicitnessofentrapment. It
alsoperformsmuchbetterthanthehumanprompt
engineer’s prompts on the test set, which demonstratesthesignificantpromiseofautomatedprompt
engineering.
6.2.4 Discussion
Promptengineeringisanon-trivialprocess,thenuancesofwhicharenotcurrentlywelldescribedin
literature. Fromthefullymanualprocessillustrated
above,thereareseveraltake-awaysworthsummarizing. First,promptengineeringisfundamentally
differentfromotherwaysofgettingacomputerto
behavethewayyouwantitto: thesesystemsare
being cajoled, not programmed, and, in addition
tobeingquitesensitivetothespecificLLMbeing
used, they can be incredibly sensitive to specific
details in prompts without there being any obvious reason those details should matter. Second,
therefore, it is important to dig into the data (e.g.
generatingpotentialexplanationsforLLM“reasoning”thatleadstoincorrectresponses). Related,the
42

<!-- Page 43 -->

thirdandmostimportanttake-awayisthatprompt
engineering should involve engagement between
thepromptengineer,whohasexpertiseinhowto
coaxLLMstobehaveindesiredways,anddomain
experts,whounderstandwhatthosedesiredways
areandwhy.
Ultimately we found that there was significant
promiseinanautomatedmethodforexploringthe
promptingspace,butalsothatcombiningthatautomationwithhumanpromptengineering/revision
was the most successful approach. We hope that
thisstudywillserveasasteptowardmorerobust
examinationsofhowtoperformpromptengineering.
43

<!-- Page 44 -->

7 Related Work
In this section, we review existing surveys and erage. Huaetal.(2024)useaGPT-4-automatedapmeta-analyses of prompting. Liu et al. (2023b) proachtoreviewLLMsinthementalhealthspace.
perform a systematic review of prompt engineer- Wangetal.(2023c)reviewpromptengineeringand
ing in the pre-ChatGPT era, including various relevant models in the visual modality and Yang
aspects of prompting like prompt template engi- etal.(2023e)providedacomprehensivelistofqualneering,answerengineering,promptensembling, itativeanalysesofmultimodalprompting,particuand prompt tuning methods. Their review cov- larlyfocusingonGPT-4V20.Duranteetal.(2024)
ersmanydifferenttypesofprompting(e.g.,cloze, reviewmultimodalinteractionsbasedonLLMemsoft-prompting, etc., across many different types bodiedagents. Koetal.(2023b)reviewliterature
of language models) while we focus on discrete ontheadoptionofText-to-Imagegenerationmodpre-fix prompting but more in-depth discussion. els for visual artists’ creative works. Gupta et al.
Chen et al. (2023a) provide a review of popular (2024) review GenAI through a topic modeling
promptingtechniqueslikeChain-of-Thought,Tree- approach. Awais et al. (2023) review foundation
of-Thought,Self-Consistency,andLeast-to-Most modelsinvision,includingvariouspromptingtechprompting,alongwithoutlooksforfutureprompt- niques. Hou et al. (2023) perform a systematic
ing research. White et al. (2023) and Schmidt review of prompt engineering techniques as they
et al. (2023) provide a taxonomy of prompt pat- relate to software engineering. They use a systerns,whicharesimilartosoftwarepatterns(and tematicreviewtechniquedevelopedbyKeeleetal.
promptingtechniquesforthatmatter). Gao(2023) (2007), specifically for software engineering reprovideapracticalpromptingtechniquetutorialfor views. Wang et al. (2023e) review the literature
anon-technicalaudience. SantuandFeng(2023) on software testing with large language models.
provideageneraltaxonomyofpromptsthatcanbe Zhang et al. (2023a) review ChatGPT prompting
usedtodesignpromptswithspecificpropertiesto performanceonsoftwareengineeringtaskssuchas
perform a wide range of complex tasks. Bubeck automatedprogramrepair. Neagu(2023)provide
etal.(2023)qualitativelyexperimentwithawide a systematic review on how prompt engineering
rangeofpromptingmethodsontheearlyversion canbeleveragedincomputerscienceeducation. Li
ofGPT-4tounderstanditscapabilities. Chuetal. et al. (2023j) review literature on the fairness of
(2023) review Chain-of-Thought related prompt- largelanguagemodels. Therearealsosurveyson
ingmethodsforreasoning. Inearlierwork,Bom- related aspects such as hallucination of language
masanietal.(2021)reviewanddiscussopportuni- models (Huang et al., 2023b), verifiability (Liu
ties and risks of foundation models broadly, and et al., 2023a), reasoning (Qiao et al., 2022), aug-
Dangetal.(2022)discusspromptingstrategiesfor mentation(Mialonetal.,2023),andlinguisticpropinteractivecreativeapplicationsthatuseprompting ertiesofprompts(Leidingeretal.,2023). Different
as a new paradigm for human interaction, with a fromtheseworks,weperformourreviewtargeting
particular focus on the user interface design that broadcoverageandgenerallyapplicableprompting
supportsuserprompting. Asanadditiontothese techniques. Finally,intermsofmoregeneralprior
existingsurveys,ourreviewaimstoprovideamore and concurrent surveys (Liu et al., 2023b; Sahoo
updatedandformalizedsystematicreview. etal.,2024;VatsalandDubey,2024),thissurvey
offersanupdateinafast-movingfield. Inaddition,
Thereisalsoalineofworkthatsurveyspromptweprovideastartingpointfortaxonomicorganiing techniques for particular domains or downzation of prompting techniques and standardizastreamapplications. Meskó(2023)andWangetal.
tionofterminology. Moreover,unlikemanyworks
(2023d) offer recommended use cases and limithat claim to be systematic, we base our work in
tations of prompt engineering in the medical and
thewidelyusedstandardforsystematicliterature
healthcaredomains. HestonandKhun(2023)proreviews—PRISMA(Pageetal.,2021).
vide a review of prompt engineering for medical
education use cases. Peskoff and Stewart (2023)
20https://openai.com/research/
queryChatGPTandYouChattoassessdomaincov- gpt-4v-system-card
44

<!-- Page 45 -->

8 Conclusions
GenerativeAIisanoveltechnology,andbroader working with constitute a good representation of
understanding of models’ capabilities and limita- that problem. It is better to start with simpler aptionsremainslimited. Naturallanguageisaflexi- proaches first, and to remain skeptical of claims
ble,open-endedinterface,withmodelshavingfew about method performance. To those already enobvious affordances. The use of Generative AI gagedinpromptengineering,wehopethatourtaxthereforeinheritsmanyofthestandardchallenges onomywillshedlightontherelationshipsbetween
oflinguisticcommunication—e.g.,ambiguity,the existingtechniques. Tothosedevelopingnewtechrole of context, the need for course correction— niques,weencouragesituatingnewmethodswithin
while at the same time adding the challenge of our taxonomy, as well as including ecologically
communicatingwithanentitywhose“understand- valid case studies and illustrations of those teching”oflanguagemaynotbearanysubstantialre- niques.
lationship to human understanding. Many of the

### Acknowledgements

techniquesdescribedherehavebeencalled“emergent”,butitisperhapsmoreappropriatetosaythat

### WeappreciatetheadvicegivenbyHalDauméIII,

they were discovered—the result of thorough ex-
Adam Visokay, and Jordan Boyd-Graber and reperimentation,analogiesfromhumanreasoning,or
viewbyDiyiYang,BrandonM.Stewart,Shubham
pureserendipity.

### Vatsal,MasonMarchetti,AaronTay,AndreaVella,

Thepresentworkisaninitialattempttocatego- andAllieMiller. Wealsoappreciatethe10KUSD
rize the species of an unfamiliar territory. While inAPIcreditsgivenbyOpenAIanddesignwork
wemakeeveryattempttobecomprehensive,there byBenjaminDiMarco.
are sure to be gaps and redundancies. Our intentionistoprovideataxonomyandterminologythat
coveralargenumberofexistingpromptengineeringtechniques,andwhichcanaccommodatefuture
methods. We discuss over 200 prompting techniques,frameworksbuiltaroundthem,andissues
likesafetyandsecuritythatneedtobekeptinmind
whenusingthem. Wealsopresenttwocasestudies
in order to provide a clear sense of models’ capabilities and what it is like to tackle a problem
inpractice. Last, ourstanceisprimarilyobservational,andwemakenoclaimstothevalidityofthe
presentedtechniques. Thefieldisnew,andevaluationisvariableandunstandardized—eventhemost
meticulousexperimentationmaysufferfromunanticipated shortcomings, and model outputs themselvesaresensitivetomeaning-preservingchanges
ininputs. Asaresult,weencouragethereaderto
avoid taking any claims at face value and to recognize that techniques may not transfer to other
models,problems,ordatasets.

### Tothosejustbeginninginpromptengineering,

our recommendations resemble what one would
recommend in any machine learning setting: understandtheproblemyouaretryingtosolve(rather
thanjustfocusingoninput/outputandbenchmark
scores), and ensure the data and metrics you are
45

<!-- Page 46 -->

References Liu,AohanZeng,LeiHou,YuxiaoDong,JieTang,
andJuanziLi.2023a. Longbench: Abilingual,mul-
Adept.2023. ACT-1: TransformerforActions. https:
titaskbenchmarkforlongcontextunderstanding.
//www.adept.ai/blog/act-1.
YushiBai, JiahaoYing, YixinCao, XinLv, YuzeHe,
Rishabh Agarwal, Avi Singh, Lei M Zhang, Bernd
XiaozhiWang,JifanYu,KaishengZeng,YijiaXiao,

### Bohnet,LuisRosias,StephanieChan,BiaoZhang,


### HaozheLyu,etal.2023b. BenchmarkingFoundation

Ankesh Anand, Zaheer Abbas, Azade Nova, et al.

### ModelswithLanguage-Model-as-an-Examiner. In


## Many-shotin-contextlearning. arXivpreprint

NeurIPS2023DatasetsandBenchmarks.
arXiv:2404.11018.
ChrisBakke.2023. Buyingachevroletfor1$.
Sweta Agrawal, Chunting Zhou, Mike Lewis, Luke

### Zettlemoyer, andMarjanGhazvininejad.2023. In-

Nishant Balepur, Jie Huang, and Kevin Chang. 2023.
contextexamplesselectionformachinetranslation.
Expository text generation: Imitate, retrieve, para-
In Findings of the Association for Computational
phrase. InProceedingsofthe2023Conferenceon

### Linguistics: ACL2023,pages8857–8873,Toronto,

Empirical Methods in Natural Language Process-
Canada.AssociationforComputationalLinguistics.
ing,pages11896–11919,Singapore.Associationfor
ComputationalLinguistics.
Kabir Ahuja, Harshita Diddee, Rishav Hada, Millicent Ochieng, Krithika Ramesh, Prachi Jain, Ak-
YejinBang,SamuelCahyawijaya,NayeonLee,WenshayNambi,TanujaGanu,SameerSegal,Maxamed
liangDai,DanSu,BryanWilie,HolyLovenia,Ziwei
Axmed, Kalika Bali, and Sunayana Sitaram. 2023.

### Ji,TiezhengYu,WillyChung,QuyetV.Do,YanXu,

MEGA: Multilingual Evaluation of Generative AI.
andPascaleFung.2023. AMultitask,Multilingual,
InEMNLP.
MultimodalEvaluationofChatGPTonReasoning,
Hallucination,andInteractivity. InAACL.
Rebuff AI. 2023. A self-hardening prompt injection
detector.
HritikBansal,KarthikGopalakrishnan,SaketDingliwal,
Sravan Bodapati, Katrin Kirchhoff, and Dan Roth.
AnirudhAjith,ChrisPan,MengzhouXia,AmeetDesh-

## RethinkingtheRoleofScaleforIn-Context

pande,andKarthikNarasimhan.2024. InstructEval:
Learning: AnInterpretability-basedCaseStudyat66
Systematicevaluationofinstructionselectionmeth-
BillionScale. InACL.
ods. In Findings of the Association for ComputationalLinguistics: NAACL2024,pages4336–4350,
OmerBar-Tal,DolevOfri-Amar,RafailFridman,Yoni

### MexicoCity,Mexico.AssociationforComputational

Kasten,andTaliDekel.2022. Text2live: Text-driven
Linguistics.
layeredimageandvideoediting.

### SílviaAraújoandMicaelaAguiar.2023. Comparing


### AmandaBertsch,MaorIvgi,UriAlon,JonathanBerant,

chatgpt’s and human evaluation of scientific texts’
MatthewRGormley,andGrahamNeubig.2024. Intranslationsfromenglishtoportugueseusingpopular
context learning with long-context models: An inautomatedtranslators. CLEF.
depthexploration. arXivpreprintarXiv:2405.00200.
ArthurAI.2024. Arthurshield.
Maciej Besta, Nils Blach, Ales Kubicek, Robert Gerstenberger,LukasGianinazzi,JoannaGajda,Tomasz
Akari Asai, Sneha Kudugunta, Xinyan Velocity Yu,

### Lehmann,MichałPodstawski,HubertNiewiadomski,

Terra Blevins, Hila Gonen, Machel Reid, Yulia

### PiotrNyczyk,andTorstenHoefler.2024. Graphof

Tsvetkov,SebastianRuder,andHannanehHajishirzi.
Thoughts: SolvingElaborateProblemswithLarge

## BUFFET: Benchmarking Large Language

LanguageModels. ProceedingsoftheAAAIConfer-
ModelsforFew-shotCross-lingualTransfer.
enceonArtificialIntelligence,38(16):17682–17690.

### Muhammad Awais, Muzammal Naseer, Salman

RishiBommasani,DrewA.Hudson,EhsanAdeli,Russ

### Khan,RaoMuhammadAnwer,HishamCholakkal,

Altman,SimranArora,SydneyvonArx,MichaelS.

### MubarakShah,Ming-HsuanYang,andFahadShah-

Bernstein,JeannetteBohg,AntoineBosselut,Emma
bazKhan.2023. Foundationalmodelsdefininganew
Brunskill,ErikBrynjolfsson,S.Buch,DallasCard,
erainvision: Asurveyandoutlook.
Rodrigo Castellon, Niladri S. Chatterji, Annie S.
Abhijeet Awasthi, Nitish Gupta, Bidisha Samanta, Chen, Kathleen A. Creel, Jared Davis, Dora Dem-
ShachiDave,SunitaSarawagi,andParthaTalukdar. szky,ChrisDonahue,MoussaDoumbouya,EsinDur-

## Bootstrappingmultilingualsemanticparsers mus,StefanoErmon,JohnEtchemendy,KawinEthausinglargelanguagemodels. InProceedingsofthe yarajh,LiFei-Fei,ChelseaFinn,TrevorGale,Lau-

17thConferenceoftheEuropeanChapteroftheAs- ren E. Gillespie, Karan Goel, Noah D. Goodman,
sociationforComputationalLinguistics,pages2455– ShelbyGrossman,NeelGuha,TatsunoriHashimoto,
2467,Dubrovnik,Croatia.AssociationforComputa- PeterHenderson,JohnHewitt,DanielE.Ho,Jenny
tionalLinguistics. Hong,KyleHsu,JingHuang,ThomasF.Icard,Saahil

### Jain, Dan Jurafsky, Pratyusha Kalluri, Siddharth

Yushi Bai, Xin Lv, Jiajie Zhang, Hongchang Lyu, Karamcheti,GeoffKeeling,FereshteKhani,O.Khat-
JiankaiTang,ZhidianHuang,ZhengxiaoDu,Xiao tab,PangWeiKoh,MarkS.Krass,RanjayKrishna,
46

<!-- Page 47 -->

Rohith Kuditipudi, Ananya Kumar, Faisal Ladhak, CDC.2023. Suicidedataandstatistics.

### MinaLee,TonyLee,JureLeskovec,IsabelleLevent,

XiangLisaLi,XuechenLi,TengyuMa,AliMalik, Chi-MinChan,WeizeChen,YushengSu,JianxuanYu,
Christopher D. Manning, Suvir Mirchandani, Eric WeiXue,ShanghangZhang,JieFu,andZhiyuanLiu.
Mitchell, Zanele Munyikwa, Suraj Nair, Avanika 2024. Chateval: Towards better LLM-based eval-
Narayan, Deepak Narayanan, Benjamin Newman, uators through multi-agent debate. In The Twelfth
AllenNie,JuanCarlosNiebles,HamedNilforoshan, International Conference on Learning Representa-
J. F. Nyarko, Giray Ogut, Laurel J. Orr, Isabel Pa- tions.
padimitriou,JoonSungPark,ChrisPiech,EvaPorte-
Ernie Chang, Pin-Jie Lin, Yang Li, Sidd Srinivasan,
lance,ChristopherPotts,AditiRaghunathan,Robert
Gael Le Lan, David Kant, Yangyang Shi, Forrest

### Reich,HongyuRen,FriedaRong,YusufH.Roohani,

Iandola,andVikasChandra.2023. In-contextprompt
Camilo Ruiz, Jack Ryan, Christopher R’e, Dorsa
editingforconditionalaudiogeneration.
Sadigh, Shiori Sagawa, Keshav Santhanam, Andy
Shih,KrishnaParasuramSrinivasan,AlexTamkin,
HarrisonChase.2022. LangChain.
Rohan Taori, Armin W. Thomas, Florian Tramèr,

### Rose E. Wang, William Wang, Bohan Wu, Jiajun


### Banghao Chen, Zhaofeng Zhang, Nicolas Langrené,

Wu, Yuhuai Wu, Sang Michael Xie, Michihiro YaandShengxinZhu.2023a. Unleashingthepotential
sunaga, Jiaxuan You, Matei A. Zaharia, Michael
ofpromptengineeringinlargelanguagemodels: a
Zhang, Tianyi Zhang, Xikun Zhang, Yuhui Zhang,
comprehensivereview.
LuciaZheng,KaitlynZhou,andPercyLiang.2021.
OntheOpportunitiesandRisksofFoundationMod- LingjiaoChen,MateiZaharia,andJamesZou.2023b.
els. ArXiv,abs/2108.07258. Howischatgpt’sbehaviorchangingovertime? arXiv
preprintarXiv:2307.09009.

### HezekiahJ.Branch,JonathanRodriguezCefalu,Jeremy

McHugh, Leyla Hujer, Aditya Bahl, Daniel del ShiqiChen,SiyangGao,andJunxianHe.2023c. Eval-
CastilloIglesias,RonHeichman,andRameshDar- uatingfactualconsistencyofsummarieswithlarge
wishi. 2022. Evaluating the susceptibility of pre- languagemodels. arXivpreprintarXiv:2305.14069.
trainedlanguagemodelsviahandcraftedadversarial
examples. Wenhu Chen, Xueguang Ma, Xinyi Wang, and

### William W. Cohen. 2023d. Program of thoughts

Greg Brockman, Vicki Cheung, Ludwig Pettersson, prompting: Disentanglingcomputationfromreason-
JonasSchneider,JohnSchulman,JieTang,andWoj- ingfornumericalreasoningtasks. TMLR.
ciechZaremba.2016. Openaigym.

### Xinyun Chen, Renat Aksitov, Uri Alon, Jie Ren, Ke-

TimBrooks,BillPeebles,ConnorHomes,WillDePue, fanXiao,PengchengYin,SushantPrakash,Charles
YufeiGuo,LiJing,DavidSchnurr,JoeTaylor,Troy Sutton,XuezhiWang,andDennyZhou.2023e. Uni-
Luhman,EricLuhman,ClarenceWingYinNg,Ricky versalself-consistencyforlargelanguagemodelgen-
Wang,andAdityaRamesh.2024. Videogeneration eration.
modelsasworldsimulators. OpenAI.
YangChen,YingweiPan,YehaoLi,TingYao,andTao

### TomB.Brown,BenjaminMann,NickRyder,Melanie

Mei.2023f. Control3d: Towardscontrollabletext-to-
Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind
3dgeneration.

### Neelakantan,PranavShyam,GirishSastry,Amanda

Askell, Sandhini Agarwal, Ariel Herbert-Voss, YiChen,RuiWang,HaiyunJiang,ShumingShi,and
Gretchen Krueger, Tom Henighan, Rewon Child, RuifengXu.2023g. Exploringtheuseoflargelan-
Aditya Ramesh, Daniel M. Ziegler, Jeffrey Wu, guagemodelsforreference-freetextqualityevalua-
ClemensWinter,ChristopherHesse,MarkChen,Eric tion: Anempiricalstudy. InFindingsoftheAssocia-
Sigler,MateuszLitwin,ScottGray,BenjaminChess, tionforComputationalLinguistics: IJCNLP-AACL
Jack Clark, Christopher Berner, Sam McCandlish, 2023 (Findings), pages 361–374, Nusa Dua, Bali.
Alec Radford, Ilya Sutskever, and Dario Amodei. AssociationforComputationalLinguistics.

## Languagemodelsarefew-shotlearners.


### JiaxinCheng,TianjunXiao,andTongHe.2023. Con-

Sébastien Bubeck, Varun Chandrasekaran, Ronen El- sistentvideo-to-videotransferusingsyntheticdataset.
dan,JohnA.Gehrke,EricHorvitz,EceKamar,Peter ArXiv,abs/2311.00213.

### Lee,YinTatLee,Yuan-FangLi,ScottM.Lundberg,

HarshaNori,HamidPalangi,MarcoTulioRibeiro, YewKenChia,GuizhenChen,LuuAnhTuan,Soujanya
and Yi Zhang. 2023. Sparks of artificial general Poria,andLidongBing.2023. Contrastivechain-ofintelligence: Early experiments with gpt-4. ArXiv, thoughtprompting.
abs/2303.12712.

### Jiqun Chu and Zuoquan Lin. 2023. Entangled repre-

Nicholas Carlini, Florian Tramer, Eric Wallace, sentationlearning: Abidirectionalencoderdecoder
Matthew Jagielski, Ariel Herbert-Voss, Katherine model. InProceedingsofthe20225thInternational
Lee, Adam Roberts, Tom Brown, Dawn Song, Ul- ConferenceonAlgorithms,ComputingandArtificial
farErlingsson,AlinaOprea,andColinRaffel.2021. Intelligence,ACAI’22,NewYork,NY,USA.Asso-
Extractingtrainingdatafromlargelanguagemodels. ciationforComputingMachinery.
47

<!-- Page 48 -->

ZhengChu,JingchangChen,QianglongChen,Weijiang Yi Dong, Ronghui Mu, Gaojie Jin, Yi Qi, Jinwei Hu,
Yu,TaoHe,HaotianWang,WeihuaPeng,MingLiu, XingyuZhao,JieMeng,WenjieRuan,andXiaowei
BingQin,andTingLiu.2023. Asurveyofchainof Huang.2024. Buildingguardrailsforlargelanguage
thoughtreasoning: Advances,frontiersandfuture. models.
RobertJCramer,JacintaHawgood,AndréaRKaniuka, YannDubois,XuechenLi,RohanTaori,TianyiZhang,
ByronBrooks,andJustinCBaker.2023. Updated IshaanGulrajani,JimmyBa,CarlosGuestrin,Percy
suicide prevention core competencies for mental Liang, and Tatsunori B Hashimoto. 2023. Alpacahealth professionals: Implications for training, re- farm:Asimulationframeworkformethodsthatlearn
search,andpractice. ClinicalPsychology: Science fromhumanfeedback. InNeurIPS.
andPractice.

### ZaneDurante,QiuyuanHuang,NaokiWake,RanGong,

Katherine Crowson, Stella Biderman, Daniel Kornis, JaeSungPark,BidiptaSarkar,RohanTaori,Yusuke
Dashiell Stander, Eric Hallahan, Louis Castricato, Noda, Demetri Terzopoulos, Yejin Choi, Katsushi
andEdwardRaff.2022. Vqgan-clip: Opendomain Ikeuchi,HoiVo,Fei-FeiLi,andJianfengGao.2024.
imagegenerationandeditingwithnaturallanguage Agentai: Surveyingthehorizonsofmultimodalinguidance. teraction.
LeyangCui,YuWu,JianLiu,SenYang,andYueZhang. JulenEtxaniz,GorkaAzkune,AitorSoroa,OierLopez

## Template-basednamedentityrecognitionus- deLacalle,andMikelArtetxe.2023. Domultilingual

ingbart. FindingsoftheAssociationforComputa- languagemodelsthinkbetterinenglish?
tionalLinguistics: ACL-IJCNLP2021.
Angela Fan, Mike Lewis, and Yann Dauphin. 2018.
HaiDang,LukasMecke,FlorianLehmann,SvenGoller, Hierarchicalneuralstorygeneration. InProceedings
andDanielBuschek.2022. Howtoprompt? opportu- of the 56th Annual Meeting of the Association for
nitiesandchallengesofzero-andfew-shotlearning ComputationalLinguistics(Volume1: LongPapers).
forhuman-aiinteractionincreativeapplicationsof AssociationforComputationalLinguistics.
generativemodels.

### LiFei-Fei,RobFergus,andPietroPerona.2006. One-

MaksymDelandMarkFishel.2023. Truedetective: A shot learning of object categories. IEEE Transacdeep abductive reasoning benchmark undoable for tionsonPatternAnalysisandMachineIntelligence,
gpt-3andchallengingforgpt-4. InProceedingsof 28:594–611.
the12thJointConferenceonLexicalandComputationalSemantics(*SEM2023).AssociationforCom- LincongFeng,MuyuWang,MaoyuWang,KuoXu,and
XiaoliLiu.2023. Metadreamer: Efficienttext-to-3d
putationalLinguistics.
creationwithdisentanglinggeometryandtexture.

### MingkaiDeng,JianyuWang,Cheng-PingHsieh,Yihan

Patrick Fernandes, Daniel Deutsch, Mara Finkel-
Wang,HanGuo,TianminShu,MengSong,EricP.
stein,ParkerRiley,AndréMartins,GrahamNeubig,
Xing,andZhitingHu.2022. RLPrompt: Optimizing

### AnkushGarg,JonathanClark,MarkusFreitag,and

DiscreteTextPromptswithReinforcementLearning.
InRLPrompt:OptimizingDiscreteTextPromptswith OrhanFirat.2023. Thedevilisintheerrors:Leverag-
ReinforcementLearning. inglargelanguagemodelsforfine-grainedmachine
translationevaluation. InProceedingsoftheEighth
YiheDeng,WeitongZhang,ZixiangChen,andQuan- Conference on Machine Translation, pages 1066–
quan Gu. 2023. Rephrase and respond: Let large 1083,Singapore.AssociationforComputationalLinlanguagemodelsaskbetterquestionsforthemselves. guistics.
Shehzaad Dhuliawala, Mojtaba Komeili, Jing Xu, Chrisantha Fernando, Dylan Banarse, Henryk
Roberta Raileanu, Xian Li, Asli Celikyilmaz, and Michalewski, Simon Osindero, and Tim Rock-
JasonWeston.2023. Chain-of-verificationreduces täschel. 2023. Promptbreeder: Self-referential
hallucinationinlargelanguagemodels. self-improvementviapromptevolution.
Shizhe Diao, Pengcheng Wang, Yong Lin, and Tong JinlanFu,See-KiongNg,ZhengbaoJiang,andPengfei
Zhang. 2023. Active prompting with chain-of- Liu.2023a. Gptscore: Evaluateasyoudesire. arXiv
thoughtforlargelanguagemodels. preprintarXiv:2302.04166.
MingDing,ZhuoyiYang,WenyiHong,WendiZheng, JinlanFu,See-KiongNg,andPengfeiLiu.2022. Poly-
Chang Zhou, Da Yin, Junyang Lin, Xu Zou, Zhou glotprompt: Multilingualmultitaskprompttraining.
Shao,HongxiaYang,andJieTang.2021. Cogview: In Proceedings of the 2022 Conference on Empiri-
Mastering text-to-image generation via transform- calMethodsinNaturalLanguageProcessing,pages
ers. InAdvancesinNeuralInformationProcessing 9919–9935,AbuDhabi,UnitedArabEmirates.As-
Systems,volume34,pages19822–19835.CurranAs- sociationforComputationalLinguistics.
sociates,Inc.

### YaoFu,HaoPeng,AshishSabharwal,PeterClark,and

QingxiuDong,LeiLi,DamaiDai,CeZheng,Zhiyong TusharKhot.2023b. Complexity-basedprompting
Wu,BaobaoChang,XuSun,JingjingXu,LeiLi,and for multi-step reasoning. In The Eleventh Interna-
ZhifangSui.2023. Asurveyonin-contextlearning. tionalConferenceonLearningRepresentations.
48

<!-- Page 49 -->

VictorGabillon,MohammadGhavamzadeh,Alessandro RohitGirdhar,MannatSingh,AndrewBrown,Quentin
Lazaric,andSébastienBubeck.2011. Multi-bandit Duval,SamanehAzadi,SaiSakethRambhatla,Akbar
best arm identification. In Advances in Neural In- Shah, Xi Yin, Devi Parikh, and Ishan Misra. 2023.
formation Processing Systems, volume 24. Curran Emuvideo: Factorizingtext-to-videogenerationby
Associates,Inc. explicitimageconditioning.
Deep Ganguli, Amanda Askell, Nicholas Schiefer, YichenGong,DelongRan,JinyuanLiu,CongleiWang,
ThomasLiao,Kamile˙ Lukošiu¯te˙,AnnaChen,Anna

### TianshuoCong,AnyuWang,SisiDuan,andXiaoyun

Goldie,AzaliaMirhoseini,CatherineOlsson,Danny Wang. 2023. Figstep: Jailbreaking large vision-
Hernandez,etal.2023. Thecapacityformoralself- languagemodelsviatypographicvisualprompts.
correctioninlargelanguagemodels. arXivpreprint
arXiv:2302.07459.

### RileyGoodside.2022. Exploitinggpt-3promptswith

malicious inputs that order the model to ignore its
AndrewGao.2023. Promptengineeringforlargelanpreviousdirections.
guagemodels. SSRN.
Lingyu Gao, Aditi Chaudhary, Krishna Srinivasan, Google. 2023. Gemini: A family of highly capable
Kazuma Hashimoto, Karthik Raman, and Michael multimodalmodels.

### Bendersky. 2023a. Ambiguity-aware in-context

learningwithlargelanguagemodels. arXivpreprint ZhibinGou,ZhihongShao,YeyunGong,yelongshen,
arXiv:2309.07900. Yujiu Yang, Nan Duan, and Weizhu Chen. 2024a.

### CRITIC: Large language models can self-correct

Luyu Gao, Aman Madaan, Shuyan Zhou, Uri Alon, withtool-interactivecritiquing. InTheTwelfthInter-
PengfeiLiu, YimingYang, JamieCallan, andGra- nationalConferenceonLearningRepresentations.
ham Neubig. 2023b. Pal: program-aided languagemodels. InProceedingsofthe40thInterna- ZhibinGou,ZhihongShao,YeyunGong,yelongshen,
tionalConferenceonMachineLearning,ICML’23. YujiuYang,MinlieHuang,NanDuan,andWeizhu
JMLR.org. Chen. 2024b. ToRA: A tool-integrated reasoning
agent for mathematical problem solving. In The

### MingqiGao,JieRuan,RenliangSun,XunjianYin,Ship-

TwelfthInternationalConferenceonLearningRepreingYang,andXiaojunWan.2023c. Human-likesumsentations.
marizationevaluationwithchatgpt. arXivpreprint
arXiv:2304.02554.
ChuanGuo,GeoffPleiss,YuSun,andKilianQWeinberger.2017. Oncalibrationofmodernneuralnet-
Tianyu Gao, Adam Fisch, and Danqi Chen. 2021.
works. InInternationalconferenceonmachinelearn-
Makingpre-trainedlanguagemodelsbetterfew-shot
ing,pages1321–1330.PMLR.
learners. In Proceedings of the 59th Annual MeetingoftheAssociationforComputationalLinguistics
andthe11thInternationalJointConferenceonNatu- HanGuo,BowenTan,ZhengzhongLiu,EricP.Xing,
ralLanguageProcessing(Volume1: LongPapers), andZhitingHu.2022. Efficient(soft)q-learningfor
textgenerationwithlimitedgooddata.
pages3816–3830,Online.AssociationforComputationalLinguistics.

### PriyankaGupta,BoshengDing,ChongGuan,andDing

MarisaGarcia.2024. Whataircanadalostin‘remark- Ding. 2024. Generative ai: A systematic review
able’lyingaichatbotcase. Forbes. usingtopicmodellingtechniques. DataandInformationManagement,page100066.

### Xavier Garcia, Yamini Bansal, Colin Cherry, George

Foster,MaximKrikun,MelvinJohnson,andOrhan RishavHada,VarunGumma,AdrianWynter,Harshita
Firat.2023. Theunreasonableeffectivenessoffew- Diddee,MohamedAhmed,MonojitChoudhury,Kashotlearningformachinetranslation. InProceedings lika Bali, and Sunayana Sitaram. 2024. Are large
of the 40th International Conference on Machine
languagemodel-basedevaluatorsthesolutiontoscal-
Learning,ICML’23.JMLR.org. ingupmultilingualevaluation? InFindingsofthe

### Association for Computational Linguistics: EACL


### MF Garnett and SC Curtin. 2023. Suicide mortality

2024,pages1051–1070,St.Julian’s,Malta.Associaintheunitedstates,2001–2021. NCHSDataBrief,
tionforComputationalLinguistics.
464:1–8.
Timnit Gebru, Jamie Morgenstern, Briana Vec- Muhammad Usman Hadi, Qasem Al Tashi, Rizwan
chione, Jennifer Wortman Vaughan, Hanna Wal- Qureshi,AbbasShah,AmgadMuneer,Muhammad
lach, Hal Daumé III, and Kate Crawford. 2021. Irfan, and et al. 2023. Large language models: A
Datasheets for datasets. Communications of the comprehensivesurveyofitsapplications,challenges,
ACM,64(12):86–92. limitations,andfutureprospects. TechRxiv.
Marjan Ghazvininejad, Hila Gonen, and Luke Zettle- AparnaDhinakaranHakanTekgul.2023. Guardrails:
moyer.2023. Dictionary-basedphrase-levelprompt- What are they and how can you use nemo and
ingoflargelanguagemodelsformachinetranslation. guardrailsaitosafeguardllms? Online.
49

<!-- Page 50 -->

SherzodHakimovandDavidSchlangen.2023. Images JiaxinHuang,ShixiangShaneGu,LeHou,YuexinWu,
inlanguagespace: Exploringthesuitabilityoflarge XuezhiWang,HongkunYu,andJiaweiHan.2022.
language models for vision & language tasks. In Large language models can self-improve. arXiv
FindingsoftheAssociationforComputationalLin- preprintarXiv:2210.11610.
guistics: ACL 2023, pages 14196–14210, Toronto,
Canada.AssociationforComputationalLinguistics. LeiHuang,WeijiangYu,WeitaoMa,WeihongZhong,

### Zhangyin Feng, Haotian Wang, Qianglong Chen,

ShiboHao,TianyangLiu,ZhenWang,andZhitingHu. WeihuaPeng,XiaochengFeng,BingQin,andTing

## ToolkenGPT:AugmentingFrozenLanguage Liu.2023b. Asurveyonhallucinationinlargelan-

ModelswithMassiveToolsviaToolEmbeddings. In guagemodels: Principles,taxonomy,challenges,and
NeurIPS. openquestions.
HangfengHe,HongmingZhang,andDanRoth.2023a.
Shaohan Huang, Li Dong, Wenhui Wang, Yaru Hao,
Socreval: Large language models with the so-

### SakshamSinghal, ShumingMa, TengchaoLv, Lei

craticmethodforreference-freereasoningevaluation.
Cui,OwaisKhanMohammed,BarunPatra,Qiang
arXivpreprintarXiv:2310.00074.

### Liu, Kriti Aggarwal, Zewen Chi, Johan Bjorck,


### Vishrav Chaudhary, Subhojit Som, Xia Song, and

Zhiwei He, Tian Liang, Wenxiang Jiao, Zhuosheng
Furu Wei. 2023c. Language is not all you need:
Zhang,YujiuYang,RuiWang,ZhaopengTu,Shum-
Aligningperceptionwithlanguagemodels.
ingShi,andXingWang.2023b. Exploringhumanliketranslationstrategywithlargelanguagemodels.
Hakan Inan, Kartikeya Upasani, Jianfeng Chi, Rashi

### Rungta, Krithika Iyer, Yuning Mao, Michael

DanHendrycks,CollinBurns,StevenBasart,AndyZou,
Tontchev,QingHu,BrianFuller,DavideTestuggine,
MantasMazeika,DawnSong,andJacobSteinhardt.
andMadianKhabsa.2023. Llamaguard: Llm-based

## MeasuringMassiveMultitaskLanguageUninput-outputsafeguardforhuman-aiconversations.

derstanding. InICLR.
Amr Hendy, Mohamed Gomaa Abdelrehim, Amr VivekIyer,PinzhenChen,andAlexandraBirch.2023.
Sharaf, Vikas Raunak, Mohamed Gabr, Hitokazu Towardseffectivedisambiguationformachinetrans-
Matsushita, Young Jin Kim, Mohamed Afify, and lationwithlargelanguagemodels.

### Hany Hassan Awadalla. 2023. How good are gpt

models at machine translation? a comprehensive AjayJain,BenMildenhall,JonathanT.Barron,Pieter
evaluation. ArXiv,abs/2302.09210. Abbeel,andBenPoole.2022. Zero-shottext-guided
objectgenerationwithdreamfields.
AmirHertz,RonMokady,JayTenenbaum,KfirAberman, Yael Pritch, and Daniel Cohen-Or. 2022. QiJia,SiyuRen,YizhuLiu,andKennyQZhu.2023.
Prompt-to-promptimageeditingwithcrossattention Zero-shotfaithfulnessevaluationfortextsummarizacontrol. tionwithfoundationlanguagemodel. arXivpreprint
arXiv:2310.11648.

### T.F.HestonandC.Khun.2023. Promptengineeringin

medicaleducation. Int.Med.Educ.,2:198–205. Yixing Jiang, Jeremy Irvin, Ji Hun Wang, Muhammad Ahmed Chaudhry, Jonathan H Chen, and An-
TobiasHinz,StefanHeinrich,andStefanWermter.2022.
drew Y Ng. 2024. Many-shot in-context learning
Semantic object accuracy for generative text-toin multimodal foundation models. arXiv preprint
imagesynthesis. IEEETransactionsonPatternAnalarXiv:2405.09798.
ysisandMachineIntelligence,44(3):1552–1565.
Zhengbao Jiang, Frank Xu, Luyu Gao, Zhiqing Sun,

### XinyiHou,YanjieZhao,YueLiu,ZhouYang,Kailong


### Qian Liu, Jane Dwivedi-Yu, Yiming Yang, Jamie

Wang, Li Li, Xiapu Luo, David Lo, John Grundy,
Callan,andGrahamNeubig.2023. Activeretrieval
andHaoyuWang.2023. Largelanguagemodelsfor
augmentedgeneration. InProceedingsofthe2023
softwareengineering: Asystematicliteraturereview.
Conference on Empirical Methods in Natural LanguageProcessing,pages7969–7992,Singapore.As-
Ming-Hao Hsu, Kai-Wei Chang, Shang-Wen Li, and
sociationforComputationalLinguistics.
Hung yi Lee. 2023. An exploration of in-context
learningforspeechlanguagemodel.

### ZhengbaoJiang,FrankF.Xu,JunAraki,andGraham

YiningHua,FenglinLiu,KailaiYang,ZehanLi,Yihan Neubig. 2020. How can we know what language
Sheu, Peilin Zhou, Lauren V. Moran, Sophia Ana- modelsknow? TransactionsoftheAssociationfor
niadou, and Andrew Beam. 2024. Large language ComputationalLinguistics,8:423–438.
modelsinmentalhealthcare: ascopingreview.

### WenxiangJiao,WenxuanWang,JentseHuang,Xing

Haoyang Huang, Tianyi Tang, Dongdong Zhang, Wang,ShumingShi,andZhaopengTu.2023. Ischat-
WayneXinZhao,TingSong,YanXia,andFuruWei. gptagoodtranslator? yeswithgpt-4astheengine.
2023a. Notalllanguagesarecreatedequalinllms:
Improvingmultilingualcapabilitybycross-lingual- ZiqiJinandWeiLu.2023. Tab-cot: Zero-shottabular
thoughtprompting. chainofthought.
50

<!-- Page 51 -->

SauravKadavath,TomConerly,AmandaAskell,Tom NatalieKieslerandDanielSchiffner.2023. Largelan-
Henighan, Dawn Drain, Ethan Perez, Nicholas guagemodelsinintroductoryprogrammingeduca-
Schiefer,ZacHatfield-Dodds,NovaDasSarma,Eli tion: Chatgpt’s performance and implications for
Tran-Johnson, Scott Johnston, Sheer El-Showk, assessments. arXivpreprintarXiv:2308.08572.

### Andy Jones, Nelson Elhage, Tristan Hume, Anna

Chen, Yuntao Bai, Sam Bowman, Stanislav Fort, HwichanKimandMamoruKomachi.2023. Enhancing
Deep Ganguli, Danny Hernandez, Josh Jacobson, few-shotcross-lingualtransferwithtargetlanguage
JacksonKernion,ShaunaKravec,LianeLovitt,Ka- peculiarexamples. InFindingsoftheAssociationfor
malNdousse,CatherineOlsson,SamRinger,Dario ComputationalLinguistics: ACL2023,pages747–
Amodei,TomBrown,JackClark,NicholasJoseph, 767,Toronto,Canada.AssociationforComputational
BenMann,SamMcCandlish,ChrisOlah,andJared Linguistics.
Kaplan.2022. Languagemodels(mostly)knowwhat
HyuhngJoonKim,HyunsooCho,JunyeobKim,Taeuk
theyknow.
Kim, Kang Min Yoo, and Sang goo Lee. 2022.
Self-generatedin-contextlearning: Leveragingauto-
EhudKarpas, OmriAbend, YonatanBelinkov, Barak
regressivelanguagemodelsasademonstrationgen-
Lenz,OpherLieber,NirRatner,YoavShoham,Hofit
erator.
Bata,YoavLevine,KevinLeyton-Brown,DorMuhlgay, Noam Rozen, Erez Schwartz, Gal Shachaf,
SunkyoungKim, DayeonKi, YireunKim, andJinsik

### ShaiShalev-Shwartz,AmnonShashua,andMoshe


### Lee.2023. Boostingcross-lingualtransferabilityin

Tenenholtz.2022. Mrklsystems: Amodular,neuromultilingualmodelsviain-contextlearning.
symbolicarchitecturethatcombineslargelanguage
models,externalknowledgesourcesanddiscreterea-
DayoonKo,SanghoLee,andGunheeKim.2023a. Can
soning.
languagemodelslaughatyoutubeshort-formvideos?
Staffs Keele et al. 2007. Guidelines for performing Hyung-KwonKo,GwanmoPark,HyeonJeon,Jaemin
systematicliteraturereviewsinsoftwareengineering. Jo,JuhoKim,andJinwookSeo.2023b. Large-scale
text-to-image generation models for visual artists’
NitishShirishKeskar,BryanMcCann,LavR.Varshney, creativeworks. Proceedingsofthe28thInternational
CaimingXiong,andRichardSocher.2019. Ctrl: A ConferenceonIntelligentUserInterfaces.
conditionaltransformerlanguagemodelforcontrollablegeneration. TomKocmiandChristianFedermann.2023a. Gembamqm: Detectingtranslationqualityerrorspanswith
KimiyaKeyvanandJimmyXiangjiHuang.2022. How gpt-4. arXivpreprintarXiv:2310.13988.
to approach ambiguous queries in conversational
search: A survey of techniques, approaches, tools, Tom Kocmi and Christian Federmann. 2023b. Large
andchallenges. ACMComputingSurveys,55(6):1– language models are state-of-the-art evaluators of
40. translation quality. In Proceedings of the 24th AnnualConferenceoftheEuropeanAssociationforMa-
MuhammadKhalifa,LajanugenLogeswaran,Moontae chineTranslation,pages193–203,Tampere,Finland.
Lee,HonglakLee,andLuWang.2023. Exploring EuropeanAssociationforMachineTranslation.
demonstrationensemblingforin-contextlearning.

### TakeshiKojima,ShixiangShaneGu,MachelReid,Yu-

MahmoudKhalil,AhmadKhalil,andAliouneNgom. takaMatsuo,andYusukeIwasawa.2022. Largelan-

## Acomprehensivestudyofvisiontransformers guagemodelsarezero-shotreasoners.

inimageclassificationtasks.

### SawanKumarandParthaTalukdar.2021. Reordering

Omar Khattab, Keshav Santhanam, Xiang Lisa Li, exampleshelpsduringpriming-basedfew-shotlearn-
David Hall, Percy Liang, Christopher Potts, and ing.

### Matei Zaharia. 2022. Demonstrate-search-predict:

Will Kurt. 2024. Say what you mean: A response to

### Composing retrieval and language models for

’let me speak freely’. https://blog.dottxt.co/
knowledge-intensivenlp.
say-what-you-mean.html.
Omar Khattab, Arnav Singhvi, Paridhi Maheshwari,
Gihyun Kwon and Jong Chul Ye. 2022. Clipstyler:

### Zhiyuan Zhang, Keshav Santhanam, Sri Vard-

Imagestyletransferwithasingletextcondition.
hamanan,SaifulHaq,AshutoshSharma,ThomasT.
Joshi, Hanna Moazam, Heather Miller, Matei Za-
Lakera.2024. Lakeraguard.
haria,andChristopherPotts.2023. Dspy: Compiling
declarativelanguagemodelcallsintoself-improving BarLanyado,OrtalKeizman,andYairDivinsky.2023.
pipelines. arXivpreprintarXiv:2310.03714. Canyoutrustchatgpt’spackagerecommendations?
VulcanCyberBlog.

### TusharKhot,HarshTrivedi,MatthewFinlayson,YaoFu,

KyleRichardson,PeterClark,andAshishSabharwal. Cindy Le, Congrui Hetang, Ang Cao, and Yihui He.

## Decomposedprompting: Amodularapproach 2023. Euclidreamer: Fastandhigh-qualitytexturing

forsolvingcomplextasks. for3dmodelswithstablediffusiondepth.
51

<!-- Page 52 -->

Soochan Lee and Gunhee Kim. 2023. Recursion of Xiaoqian Li, Ercong Nie, and Sheng Liang. 2023g.
thought: A divide-and-conquer approach to multi- Crosslingualretrievalaugmentedin-contextlearning
contextreasoningwithlanguagemodels. forbangla.
Alina Leidinger, Robert van Rooij, and Ekaterina Xiujun Li, Xi Yin, Chunyuan Li, Pengchuan Zhang,
Shutova.2023. Thelanguageofprompting: What XiaoweiHu,LeiZhang,LijuanWang,HoudongHu,
linguisticpropertiesmakeapromptsuccessful? Li Dong, Furu Wei, Yejin Choi, and Jianfeng Gao.

## Oscar: Object-semanticsalignedpre-training

BrianLester,RamiAl-Rfou,andNoahConstant.2021. forvision-languagetasks.
The power of scale for parameter-efficient prompt
tuning. InProceedingsofthe2021Conferenceon
Yaoyiran Li, Anna Korhonen, and Ivan Vulic´. 2023h.
EmpiricalMethodsinNaturalLanguageProcessing.
Onbilinguallexiconinductionwithlargelanguage
AssociationforComputationalLinguistics.
models.
PatrickLewis,EthanPerez,AleksandraPiktus,Fabio
YifeiLi,ZeqiLin,ShizhuoZhang,QiangFu,BeiChen,
Petroni,VladimirKarpukhin,NamanGoyal,Hein-

### Jian-GuangLou,andWeizhuChen.2023i. Making

richKüttler, MikeLewis, WentauYih, TimRocklanguage models better reasoners with step-aware
täschel, Sebastian Riedel, and Douwe Kiela. 2021.
verifier. InProceedingsofthe61stAnnualMeeting
Retrieval-augmented generation for knowledgeoftheAssociationforComputationalLinguistics(Volintensivenlptasks.
ume1: LongPapers).AssociationforComputational
Linguistics.

### Bowen Li, Xiaojuan Qi, Thomas Lukasiewicz, and

PhilipH.S.Torr.2019a. Controllabletext-to-image
YingjiLi,MengnanDu,RuiSong,XinWang,andYing
generation.

### Wang.2023j. Asurveyonfairnessinlargelanguage

Cheng Li, Jindong Wang, Yixuan Zhang, Kaijie Zhu, models.

### WenxinHou,JianxunLian,FangLuo,QiangYang,

andXingXie.2023a. Largelanguagemodelsunder- JingyunLiang,YuchenFan,KaiZhang,RaduTimofte,
standandcanbeenhancedbyemotionalstimuli. LucVanGool,andRakeshRanjan.2023. Movideo:

### Motion-awarevideogenerationwithdiffusionmod-

ChengzhengxuLi,XiaomingLiu,YichenWang,Duyi els.

### Li, Yu Lan, and Chao Shen. 2023b. Dialogue for

prompting: apolicy-gradient-baseddiscreteprompt Chen-Hsuan Lin, Jun Gao, Luming Tang, Towaki
optimizationforfew-shotlearning. Takikawa,XiaohuiZeng,XunHuang,KarstenKreis,
SanjaFidler,Ming-YuLiu,andTsung-YiLin.2023.
Jiahao Li, Hao Tan, Kai Zhang, Zexiang Xu, Fujun Magic3d: High-resolution text-to-3d content cre-
Luan,YinghaoXu,YicongHong,KalyanSunkavalli, ation.

### GregShakhnarovich,andSaiBi.2023c. Instant3d:

Fasttext-to-3dwithsparse-viewgenerationandlarge XiVictoriaLin,TodorMihaylov,MikelArtetxe,Tianlu
reconstructionmodel. Wang,ShuohuiChen,DanielSimig,MyleOtt,NamanGoyal,ShrutiBhosale,JingfeiDu,Ramakanth
MingLi,PanZhou,Jia-WeiLiu,JussiKeppo,MinLin,
Pasunuru,SamShleifer,PunitSinghKoura,Vishrav
ShuichengYan,andXiangyuXu.2023d. Instant3d:
Chaudhary,BrianO’Horo,JeffWang,LukeZettle-
Instanttext-to-3dgeneration.
moyer,ZornitsaKozareva,MonaDiab,VeselinStoyanov, and Xian Li. 2022. Few-shot learning with
Ruosen Li, Teerth Patel, and Xinya Du. 2023e.
multilingualgenerativelanguagemodels. InProceed-
Prd: Peer rank and discussion improve large laningsofthe2022ConferenceonEmpiricalMethods
guage model based evaluations. arXiv preprint
inNaturalLanguageProcessing,pages9019–9052,
arXiv:2307.02762.
AbuDhabi,UnitedArabEmirates.Associationfor
ComputationalLinguistics.
Wenbo Li, Pengchuan Zhang, Lei Zhang, Qiuyuan
Huang,XiaodongHe,SiweiLyu,andJianfengGao.

### Yen-Ting Lin and Yun-Nung Chen. 2023. Llm-eval:

2019b. Object-driven text-to-image synthesis via
Unifiedmulti-dimensionalautomaticevaluationfor
adversarialtraining.
open-domainconversationswithlargelanguagemodels. arXivpreprintarXiv:2305.13711.
XiaonanLi,KaiLv,HangYan,TianyangLin,WeiZhu,

### YuanNi,GuotongXie,XiaolingWang,andXipeng

Qiu.2023f. Unifieddemonstrationretrieverforin- JerryLiu.2022. LlamaIndex.
contextlearning.

### JiachangLiu,DinghanShen,YizheZhang,BillDolan,

XiaonanLiandXipengQiu.2023a. Findingsupport Lawrence Carin, and Weizhu Chen. 2021. What
examplesforin-contextlearning. makes good in-context examples for GPT-3? In

### WorkshoponKnowledgeExtractionandIntegration

XiaonanLiandXipengQiu.2023b. Mot: Memory-of- forDeepLearningArchitectures;DeepLearningInthoughtenableschatgpttoself-improve. sideOut.
52

<!-- Page 53 -->

NelsonFLiu,TianyiZhang,andPercyLiang.2023a. YaoLu,MaxBartolo,AlastairMoore,SebastianRiedel,
Evaluatingverifiabilityingenerativesearchengines. and Pontus Stenetorp. 2021. Fantastically ordered
InProceedingsofthe2023ConferenceonEmpirical promptsandwheretofindthem: Overcomingfew-
MethodsinNaturalLanguageProcessing. shotpromptordersensitivity.
PengfeiLiu,WeizheYuan,JinlanFu,ZhengbaoJiang, YaoLu,JiayiWang,RaphaelTang,SebastianRiedel,
HiroakiHayashi,andGrahamNeubig.2023b. Pre- andPontusStenetorp.2024. Stringsfromthelibrary
train, prompt, and predict: A systematic survey of ofbabel: Randomsamplingasastrongbaselinefor
promptingmethodsinnaturallanguageprocessing. promptoptimisation.
ACMComputingSurveys,55(9):1–35.
CharlesDuffyLucaBeurer-Kellner,MarcFischer.2023.
lmql. GitHubrepository.

### WeihuangLiu,XiShen,Chi-ManPun,andXiaodong


### Cun.2023c. Explicitvisualpromptingforlow-level

Zheheng Luo, Qianqian Xie, and Sophia Ananiadou.
structuresegmentations. In2023IEEE/CVFConfer-

## Chatgptasafactualinconsistencyevaluator

ence on Computer Vision and Pattern Recognition
for abstractive text summarization. arXiv preprint

## (Cvpr).Ieee.

arXiv:2303.15621.

### Yang Liu, Dan Iter, Yichong Xu, Shuohang Wang,

Jiaxi Lv, Yi Huang, Mingfu Yan, Jiancheng Huang,

### Ruochen Xu, and Chenguang Zhu. 2023d. Gpte-


### Jianzhuang Liu, Yifan Liu, Yafei Wen, Xiaoxin

val: Nlg evaluation using gpt-4 with better human
Chen,andShifengChen.2023. Gpt4motion: Scriptalignment. arXivpreprintarXiv:2303.16634.
ingphysicalmotionsintext-to-videogenerationvia
blender-orientedgptplanning.

### YihaoLiu,XiangyuChen,XianzhengMa,XintaoWang,

JiantaoZhou,YuQiao,andChaoDong.2023e. Uni- Qing Lyu, Shreya Havaldar, Adam Stein, Li Zhang,
fyingimageprocessingasvisualpromptingquestion Delip Rao, Eric Wong, Marianna Apidianaki, and
answering. Chris Callison-Burch. 2023. Faithful chain-ofthoughtreasoning.

### Yongkang Liu, Shi Feng, Daling Wang, Yifei Zhang,

andHinrichSchütze.2023f. Evaluatewhatyoucan’t HuanMa,ChangqingZhang,YataoBian,LemaoLiu,
evaluate: Unassessablegeneratedresponsesquality. ZhiruiZhang,PeilinZhao,ShuZhang,HuazhuFu,
arXivpreprintarXiv:2305.14658. Qinghua Hu, and Bingzhe Wu. 2023. Fairnessguidedfew-shotpromptingforlargelanguagemod-
YuxinLiu,MinshanXie,HanyuanLiu,andTien-Tsin els. arXivpreprintarXiv:2303.13217.

### Wong.2023g. Text-guidedtexturingbysynchronized

multi-viewdiffusion. AmanMadaan, NiketTandon,PrakharGupta,Skyler

### Hallinan, Luyu Gao, Sarah Wiegreffe, Uri Alon,

Yuxuan Liu, Tianchi Yang, Shaohan Huang, Zihan Nouha Dziri, Shrimai Prabhumoye, Yiming Yang,
Zhang, Haizhen Huang, Furu Wei, Weiwei Deng, Shashank Gupta, Bodhisattwa Prasad Majumder,
Feng Sun, and Qi Zhang. 2023h. Calibrating llm- Katherine Hermann, Sean Welleck, Amir Yazdanbasedevaluator. arXivpreprintarXiv:2309.13308. bakhsh,andPeterClark.2023. Self-refine: Iterative
refinementwithself-feedback.

### JieyiLong.2023. Largelanguagemodelguidedtree-of-

Ninareh Mehrabi, Fred Morstatter, Nripsuta Saxena,
thought.
KristinaLerman,andAramGalstyan.2021. Asurveyonbiasandfairnessinmachinelearning. ACM
Jonathan Lorraine, Kevin Xie, Xiaohui Zeng, Chencomputingsurveys(CSUR),54(6):1–35.
HsuanLin,TowakiTakikawa,NicholasSharp,Tsung-
YiLin,Ming-YuLiu,SanjaFidler,andJamesLucas.
LauraMelzer,ThomasForkmann,andTobiasTeismann.

## Att3d: Amortizedtext-to-3dobjectsynthesis.


## Suicidecrisissyndrome: Asystematicreview.

SuicideandLife-ThreateningBehavior. February27,
Albert Lu, Hongxin Zhang, Yanzhe Zhang, Xuezhi
onlineaheadofprint.
Wang,andDiyiYang.2023a. Boundingthecapabilitiesoflargelanguagemodelsinopentextgeneration
FanxuMeng,HaotongYang,YidingWang,andMuhan
withpromptconstraints.
Zhang.2023. Chainofimagesforintuitivelyreasoning.
HongyuanLu,HaoyangHuang,DongdongZhang,Haoran Yang, Wai Lam, and Furu Wei. 2023b. Chain- B. Meskó. 2023. Prompt engineering as an imporof-dictionary prompting elicits translation in large tantemergingskillformedicalprofessionals: Tutolanguagemodels. rial. JournalofMedicalInternetResearch,25(Suppl
1):e50638.

### QingyuLu, BaopuQiu, LiangDing, LipingXie, and

DachengTao.2023c. Erroranalysispromptingen- YachunMi,YuLi,YanShu,ChenHui,PuchaoZhou,
ableshuman-liketranslationevaluationinlargelan- andShaohuiLiu.2023. Clif-vqa: Enhancingvideo
guage models: A case study on chatgpt. arXiv quality assessment by incorporating high-level sepreprintarXiv:2303.13809. manticinformationrelatedtohumanfeelings.
53

<!-- Page 54 -->

GrégoireMialon,RobertoDessì,MariaLomeli,Christo- AlexandraNeagu.2023. HowcanlargelanguagemodforosNalmpantis,RamPasunuru,RobertaRaileanu, els and prompt engineering be leveraged in Com-
Baptiste Rozière, Timo Schick, Jane Dwivedi-Yu, puter Science education?: Systematic literature re-
AsliCelikyilmaz,EdouardGrave,YannLeCun,and view. Master’sthesis,DelftUniversityofTechnol-
ThomasScialom.2023. Augmentedlanguagemod- ogy,6.
els: asurvey.

### ErcongNie,ShengLiang,HelmutSchmid,andHinrich

SewonMin,XinxiLyu,AriHoltzman,MikelArtetxe, Schütze. 2023. Cross-lingual retrieval augmented
MikeLewis,HannanehHajishirzi,andLukeZettle- promptforlow-resourcelanguages. InFindingsof
moyer.2022. Rethinkingtheroleofdemonstrations: theAssociationforComputationalLinguistics: ACL
Whatmakesin-contextlearningwork? 2023,pages8320–8340,Toronto,Canada.AssociationforComputationalLinguistics.

### SewonMin,JulianMichael,HannanehHajishirzi,and

Luke Zettlemoyer. 2020. Ambigqa: Answering Xuefei Ning, Zinan Lin, Zixuan Zhou, Zifu Wang,
ambiguousopen-domainquestions. arXivpreprint HuazhongYang,andYuWang.2023. Skeleton-ofarXiv:2004.10645. thought: Largelanguagemodelscandoparalleldecoding.
R.A.Morelli,J.D.Bronzino,andJ.W.Goethe.1991. A
OpenAI.2023. OpenAIAssistants.
computationalspeech-actmodelofhuman-computer
conversations. In Proceedings of the 1991 IEEE

### Jonas Oppenlaender. 2023. A taxonomy of prompt

SeventeenthAnnualNortheastBioengineeringConmodifiersfortext-to-imagegeneration.
ference,pages263–264.
AntonOsika.2023. gpt-engineer.
Yasmin Moslem, Rejwanul Haque, John D. Kelleher,
andAndyWay.2023. Adaptivemachinetranslation
Matthew J Page, Joanne E McKenzie, Patrick M
withlargelanguagemodels. InProceedingsofthe
Bossuyt, Isabelle Boutron, Tammy C Hoffmann,
24thAnnualConferenceoftheEuropeanAssociation
Cynthia D Mulrow, Larissa Shamseer, Jennifer M
forMachineTranslation,pages227–237,Tampere,
Tetzlaff, Elie A Akl, Sue E Brennan, Roger Chou,

### Finland.EuropeanAssociationforMachineTransla-

JulieGlanville,JeremyMGrimshaw,AsbjørnHróbtion.
jartsson, Manoj M Lalu, Tianjing Li, Elizabeth W
Loder,EvanMayo-Wilson,SteveMcDonald,LukeA

### FangwenMu,LinShi,SongWang,ZhuohaoYu,Bin-

McGuinness,LesleyAStewart,JamesThomas,AnquanZhang,ChenxueWang,ShichaoLiu,andQing
dreaCTricco,VivianAWelch,PennyWhiting,and
Wang. 2023. Clarifygpt: Empowering llm-based
DavidMoher.2021. Theprisma2020statement: an
codegenerationwithintentionclarification.
updatedguidelineforreportingsystematicreviews.

## Bmj,372.

NiklasMuennighoff,ThomasWang,LintangSutawika,

### Adam Roberts, Stella Biderman, Teven Le Scao,


### Ehsan Pajouheshgar, Yitao Xu, Alexander Mordvint-

MSaifulBari, ShengShen, ZhengXinYong, Haisev, Eyvind Niklasson, Tong Zhang, and Sabine
ley Schoelkopf, Xiangru Tang, Dragomir Radev,
Süsstrunk.2023. Meshneuralcellularautomata.
Alham Fikri Aji, Khalid Almubarak, Samuel Albanie,ZaidAlyafeai,AlbertWebson,EdwardRaff,
Pruthvi Patel, Swaroop Mishra, Mihir Parmar, and
and Colin Raffel. 2023. Crosslingual generaliza-

### ChittaBaral.2022. Isaquestiondecompositionunit

tion through multitask finetuning. In Proceedings
allweneed?
of the 61st Annual Meeting of the Association for
ComputationalLinguistics(Volume1: LongPapers),
Shishir G. Patil, Tianjun Zhang, Xin Wang, and
pages15991–16111,Toronto,Canada.Association
Joseph E. Gonzalez. 2023. Gorilla: Large lanforComputationalLinguistics.
guage model connected with massive apis. ArXiv,
abs/2305.15334.

### AkshayNambi,VaibhavBalloli,MercyRanjit,Tanuja

Ganu,KabirAhuja,SunayanaSitaram,andKalika Hammond Pearce, Baleegh Ahmad, Benjamin Tan,
Bali.2023. Breakinglanguagebarrierswithaleap: Brendan Dolan-Gavitt, and Ramesh Karri. 2021.
Learningstrategiesforpolyglotllms. Asleep at the keyboard? assessing the security of
githubcopilot’scodecontributions.

### Milad Nasr, Nicholas Carlini, Jonathan Hayase,

Matthew Jagielski, A. Feder Cooper, Daphne Ip- Hammond Pearce, Benjamin Tan, Baleegh Ahmad,
polito, Christopher A. Choquette-Choo, Eric Wal- RameshKarri,andBrendanDolan-Gavitt.2022. Exlace,FlorianTramèr,andKatherineLee.2023. Scal- aminingzero-shotvulnerabilityrepairwithlargelanable extraction of training data from (production) guagemodels.
languagemodels.

### PuyuanPeng,BrianYan,ShinjiWatanabe,andDavid

NationalCenterforHealthWorkforceAnalysis.2023. Harwath.2023. Promptingthehiddentalentofweb-
Behavioralhealthworkforce,2023. scalespeechmodelsforzero-shottaskgeneralization.
54

<!-- Page 55 -->

EthanPerez,SaffronHuang,FrancisSong,TrevorCai, Preamble.2024. Ourproduct.
Roman Ring, John Aslanides, Amelia Glaese, Nat
OfirPress,MuruZhang,SewonMin,LudwigSchmidt,
McAleese,andGeoffreyIrving.2022. Redteaming
NoahA.Smith,andMikeLewis.2022. Measuring
languagemodelswithlanguagemodels.
andnarrowingthecompositionalitygapinlanguage
Fábio Perez and Ian Ribeiro. 2022. Ignore previous models.
prompt: Attacktechniquesforlanguagemodels.

### Reid Pryzant, Dan Iter, Jerry Li, Yin Tat Lee, Chen-

NeilPerry,MeghaSrivastava,DeepakKumar,andDan guang Zhu, and Michael Zeng. 2023. Automatic
Boneh. 2022. Do users write more insecure code prompt optimization with "gradient descent" and
withaiassistants? beamsearch.
Denis Peskoff and Brandon M Stewart. 2023. Credi- Ratish Puduppully, Anoop Kunchukuttan, Raj Dabre,
blewithoutcredit: Domainexpertsassessgenerative AiTiAw,andNancyF.Chen.2023. Decomposed
languagemodels. InProceedingsofthe61stAnnual promptingformachinetranslationbetweenrelated
Meeting of the Association for Computational Lin- languagesusinglargelanguagemodels.
guistics(Volume2: ShortPapers),pages427–438.

### Bo Qiao, Liqun Li, Xu Zhang, Shilin He, Yu Kang,

DenisPeskoff,AdamVisokay,SanderSchulhoff,Ben- Chaoyun Zhang, Fangkai Yang, Hang Dong, Jue
jamin Wachspress, Alan Blinder, and Brandon M Zhang,LuWang,Ming-JieMa,PuZhao,SiQin,Xi-
Stewart.2023. Gptdecipheringfedspeak: Quantify- aotingQin,ChaoDu,YongXu,QingweiLin,S.Rajing dissent among hawks and doves. In Findings mohan,andDongmeiZhang.2023. Taskweaver: A
of the Association for Computational Linguistics: code-firstagentframework. ArXiv,abs/2311.17541.
EMNLP2023,pages6529–6539.

### ShuofeiQiao,YixinOu,NingyuZhang,XiangChen,

DenisPeskov,ViktorHangya,JordanBoyd-Graber,and YunzhiYao,ShuminDeng,ChuanqiTan,FeiHuang,
Alexander Fraser. 2021. Adapting entities across andHuajunChen.2022. Reasoningwithlanguage
languagesandcultures. FindingsoftheAssociation modelprompting: Asurvey.
forComputationalLinguistics: EMNLP2021.

### LiboQin,QiguangChen,FuxuanWei,ShijueHuang,

Fabio Petroni, Tim Rocktäschel, Sebastian Riedel, and Wanxiang Che. 2023a. Cross-lingual prompt-
Patrick Lewis, Anton Bakhtin, Yuxiang Wu, and ing: Improvingzero-shotchain-of-thoughtreasoning
AlexanderMiller.2019. Languagemodelsasknowl- acrosslanguages.
edge bases? Proceedings of the 2019 Conference
Yujia Qin, Shengding Hu, Yankai Lin, Weize Chen,
onEmpiricalMethodsinNaturalLanguageProcess-

### Ning Ding, Ganqu Cui, Zheni Zeng, Yufei Huang,

ing and the 9th International Joint Conference on

### ChaojunXiao,ChiHan,YiRenFung,YushengSu,

NaturalLanguageProcessing(EMNLP-IJCNLP).

### HuadongWang,ChengQian,RunchuTian,Kunlun

Pouya Pezeshkpour and Estevam Hruschka. 2023. Zhu,ShiLiang,XingyuShen,BokaiXu,ZhenZhang,
Large language models sensitivity to the order of YiningYe,BoLi,ZiweiTang,JingYi,YuZhu,Zhenoptionsinmultiple-choicequestions. arXivpreprint ningDai, LanYan, XinCong, Ya-TingLu, Weilin
arXiv:2308.11483. Zhao,YuxiangHuang,Jun-HanYan,XuHan,Xian

### Sun, Dahai Li, Jason Phang, Cheng Yang, Tong-

Carol W. Pfaff. 1979. Constraints on language mix- shuang Wu, Heng Ji, Zhiyuan Liu, and Maosong
ing: Intrasententialcode-switchingandborrowingin Sun.2023b. Toollearningwithfoundationmodels.
spanish/english. Language,pages291–318. ArXiv,abs/2304.08354.
JonathanPilault,XavierGarcia,ArthurBražinskas,and AlecRadford,JongWookKim,ChrisHallacy,Aditya
OrhanFirat.2023. Interactive-chain-prompting: Am- Ramesh,GabrielGoh,SandhiniAgarwal,GirishSasbiguityresolutionforcrosslingualconditionalgener- try, Amanda Askell, Pamela Mishkin, Jack Clark,
ationwithinteraction. etal.2021. Learningtransferablevisualmodelsfrom
naturallanguagesupervision. InInternationalconfer-
Ben Poole, Ajay Jain, Jonathan T. Barron, and Ben
enceonmachinelearning,pages8748–8763.PMLR.

### Mildenhall.2022. Dreamfusion: Text-to-3dusing2d

diffusion. AlecRadford,JeffreyWu,RewonChild,DavidLuan,
Dario Amodei, Ilya Sutskever, et al. 2019a. Lan-

### ShanaPoplack.1980. Sometimesi’llstartasentencein

guage models are unsupervised multitask learners.
spanishyterminoenespañol: Towardatypologyof
OpenAIblog,1(8):9.
code-switching. Linguistics,18(7-8):581–618.

### AlecRadford,JeffreyWu,RewonChild,DavidLuan,

Archiki Prasad, Peter Hase, Xiang Zhou, and Mohit

### Dario Amodei, Ilya Sutskever, et al. 2019b. Lan-

Bansal. 2023. GrIPS: Gradient-free, edit-based inguage models are unsupervised multitask learners.
structionsearchforpromptinglargelanguagemodels. OpenAIblog,1(8):9.
InProceedingsofthe17thConferenceoftheEuropeanChapteroftheAssociationforComputational Sudha Rao and Hal Daumé III. 2019. Answer-based
Linguistics, pages3845–3864, Dubrovnik, Croatia. adversarialtrainingforgeneratingclarificationques-
AssociationforComputationalLinguistics. tions. arXivpreprintarXiv:1904.02281.
55

<!-- Page 56 -->

Traian Rebedea, Razvan Dinu, Makesh Sreedhar, TimoSchickandHinrichSchütze.2020a. Exploiting
Christopher Parisien, and Jonathan Cohen. 2023. cloze-questionsforfew-shottextclassificationand
Nemoguardrails: Atoolkitforcontrollableandsafe naturallanguageinference. InConferenceoftheEullmapplicationswithprogrammablerails. arXiv. ropeanChapteroftheAssociationforComputational
Linguistics.
PhilipResnik,AprilForeman,MichelleKuchuk,Katherine Musacchio Schafer, and Beau Pinkham. 2021. TimoSchickandHinrichSchütze.2020b. It’snotjust
Naturallyoccurringlanguageasasourceofevidence size that matters: Small language models are also
insuicideprevention. SuicideandLife-Threatening few-shotlearners. ArXiv,abs/2009.07118.
Behavior,51(1):88–96.

### Timo Schick and Hinrich Schütze. 2021. Exploiting

LariaReynoldsandKyleMcDonell.2021. Promptpro- cloze-questionsforfew-shottextclassificationand
gramming for large language models: Beyond the natural language inference. In Proceedings of the
few-shot paradigm. In Extended Abstracts of the 16thConferenceoftheEuropeanChapteroftheAsso-
2021CHIConferenceonHumanFactorsinComput- ciationforComputationalLinguistics: MainVolume.
ingSystems,CHI’21.ACM. AssociationforComputationalLinguistics.
MeganLRogers,CarolChu,andThomasJoiner.2019. DouglasC.Schmidt,JesseSpencer-Smith,QuchenFu,
Thenecessity,validity,andclinicalutilityofanewdi- andJulesWhite.2023. Catalogingpromptpatternsto
agnosticentity: Acutesuicidalaffectivedisturbance enhancethedisciplineofpromptengineering. Dept.
(asad). JournalofClinicalPsychology,75(6):999. ofComputerScience,VanderbiltUniversity. Email:
douglas.c.schmidt, jesse.spencer-smith, quchen.fu,
RobinRombach,AndreasBlattmann,DominikLorenz,
jules.white@vanderbilt.edu.
Patrick Esser, and Björn Ommer. 2022. Highresolutionimagesynthesiswithlatentdiffusionmod-
AllisonSchuck,RaffaellaCalati,ShiraBarzilay,Sarah
els.

### Bloch-Elkouby,andIgorI.Galynker.2019a. Suicide

crisis syndrome: A review of supporting evidence

### Shamik Roy, Raphael Shu, Nikolaos Pappas, Elman

foranewsuicide-specificdiagnosis. Behavioralsci-
Mansimov,YiZhang,SaabMansour,andDanRoth.
ences&thelaw,373:223–239.

## Conversation style transfer using few-shot

learning. In Proceedings of the 13th International
AllisonSchuck,RaffaellaCalati,ShiraBarzilay,Sarah

### JointConferenceonNaturalLanguageProcessing


### Bloch-Elkouby,andIgorGalynker.2019b. Suicide

andthe3rdConferenceoftheAsia-PacificChapterof
crisis syndrome: A review of supporting evidence
theAssociationforComputationalLinguistics(Volforanewsuicide-specificdiagnosis. Behavioralsciume 1: Long Papers), pages 119–143, Nusa Dua,
encesandthelaw,37(3):223–239.
Bali.AssociationforComputationalLinguistics.
SanderSchulhoff.2022. LearnPrompting.
Ohad Rubin, Jonathan Herzig, and Jonathan Berant.

## Learning to retrieve prompts for in-context

SanderSchulhoff,JeremyPinto,AnaumKhan,Louislearning. InProceedingsofthe2022Conferenceof
François Bouchard, Chenglei Si, Svetlina Anati,
theNorthAmericanChapteroftheAssociationfor

### ValenTagliabue,AnsonKost,ChristopherCarnahan,

ComputationalLinguistics: HumanLanguageTechandJordanBoyd-Graber.2023. Ignorethistitleand
nologies.AssociationforComputationalLinguistics.
HackAPrompt: Exposing systemic vulnerabilities
of LLMs through a global prompt hacking compe-

### Runway. 2023. Gen-2 prompt tips. https:

tition. In Proceedings of the 2023 Conference on
//help.runwayml.com/hc/en-us/articles/
EmpiricalMethodsinNaturalLanguageProcessing,
17329337959699-Gen-2-Prompt-Tips.
pages4945–4977,Singapore.AssociationforCom-
Pranab Sahoo, Ayush Kumar Singh, Sriparna Saha, putationalLinguistics.
VinijaJain,SamratMondal,andAmanChadha.2024.
Asystematicsurveyofpromptengineeringinlarge Sander V Schulhoff. 2024. Prompt injection vs jaillanguagemodels: Techniquesandapplications. breaking: Whatisthedifference?
GustavoSandoval,HammondPearce,TeoNys,Ramesh MelanieSclar,YejinChoi,YuliaTsvetkov,andAlane
Karri, Siddharth Garg, and Brendan Dolan-Gavitt. Suhr. 2023a. Quantifying language models’ sensi-

## Lostatc: Auserstudyonthesecurityimplica- tivitytospuriousfeaturesinpromptdesignor: How

tionsoflargelanguagemodelcodeassistants. ilearnedtostartworryingaboutpromptformatting.
arXivpreprintarXiv:2310.11324.
ShubhraKantiKarmakerSantuandDongjiFeng.2023.
Teler: Ageneraltaxonomyofllmpromptsforbench- MelanieSclar,YejinChoi,YuliaTsvetkov,andAlane
markingcomplextasks. Suhr.2023b. Quantifyinglanguagemodels’sensitivitytospuriousfeaturesinpromptdesignor: Howi
TimoSchick,JaneDwivedi-Yu,RobertoDessì,Roberta learnedtostartworryingaboutpromptformatting.

### Raileanu,MariaLomeli,LukeZettlemoyer,Nicola

Cancedda,andThomasScialom.2023. Toolformer: Harsha-Nori Scott Lundberg, Marco Tulio Cor-
Languagemodelscanteachthemselvestousetools. reiaRibeiro.2023. guidance. GitHubrepository.
56

<!-- Page 57 -->

JohnR.Searle.1969. SpeechActs: AnEssayinthePhi- Chenglei Si, Navita Goyal, Sherry Tongshuang Wu,
losophyofLanguage. CambridgeUniversityPress. Chen Zhao, Shi Feng, Hal Daumé III, and Jordan

### Boyd-Graber. 2023c. Large language models help

OmarShaikh,HongxinZhang,WilliamHeld,Michael humansverifytruthfulness–exceptwhentheyarecon-
Bernstein,andDiyiYang.2023. Onsecondthought, vincinglywrong. arXivpreprintarXiv:2310.12558.
let’snotthinkstepbystep! biasandtoxicityinzeroshotreasoning. ChengleiSi,WeijiaShi,ChenZhao,LukeZettlemoyer,
andJordanLeeBoyd-Graber.2023d. GettingMoRE
outofMixtureoflanguagemodelReasoningExperts.
Mrinank Sharma, Meg Tong, Tomasz Korbak, David
FindingsofEmpiricalMethodsinNaturalLanguage
Duvenaud, Amanda Askell, Samuel R Bowman,
Processing.

### NewtonCheng,EsinDurmus,ZacHatfield-Dodds,


### ScottRJohnston,etal.2023. Towardsunderstand-

Suzanna Sia and Kevin Duh. 2023. In-context learningsycophancyinlanguagemodels. arXivpreprint
ingasmaintainingcoherency: Astudyofon-the-fly
arXiv:2310.13548.
machinetranslationusinglargelanguagemodels.
YongliangShen,KaitaoSong,XuTan,DongShengLi,
SignificantGravitas.2023. AutoGPT.
WeimingLu,andYueTingZhuang.2023. Hugginggpt: Solvingaitaskswithchatgptanditsfriendsin
Uriel Singer, Shelly Sheynin, Adam Polyak, Oron
huggingface. ArXiv,abs/2303.17580.
Ashual, Iurii Makarov, Filippos Kokkinos, Naman

### Goyal,AndreaVedaldi,DeviParikh,JustinJohnson,

FredaShi,MiracSuzgun,MarkusFreitag,XuezhiWang, andYanivTaigman.2023. Text-to-4ddynamicscene
SurajSrivats,SoroushVosoughi,HyungWonChung, generation.

### YiTay,SebastianRuder,DennyZhou,DipanjanDas,

andJasonWei.2022. Languagemodelsaremultilin- Taylor Sorensen, Joshua Robinson, Christopher Rytgualchain-of-thoughtreasoners. ting,AlexanderShaw,KyleRogers,AlexiaDelorey,
MahmoudKhalil,NancyFulda,andDavidWingate.
Taylor Shin, Yasaman Razeghi, Robert L Logan IV, 2022. Aninformation-theoreticapproachtoprompt
Eric Wallace, and Sameer Singh. 2020a. Eliciting engineeringwithoutgroundtruthlabels. InProceedknowledge from language models using automati- ingsofthe60thAnnualMeetingoftheAssociation
callygeneratedprompts. ArXiv,abs/2010.15980. forComputationalLinguistics(Volume1: LongPapers),pages819–862,Dublin,Ireland.Association
TaylorShin,YasamanRazeghi,RobertL.LoganIV,Eric forComputationalLinguistics.

### Wallace, and Sameer Singh. 2020b. Autoprompt:

Elicitingknowledgefromlanguagemodelswithau- AndreaSottana,BinLiang,KaiZou,andZhengYuan.
tomaticallygeneratedprompts. Proceedingsofthe 2023. Evaluationmetricsintheeraofgpt-4: Reli-
2020ConferenceonEmpiricalMethodsinNatural ablyevaluatinglargelanguagemodelsonsequence
LanguageProcessing(EMNLP). tosequencetasks. arXivpreprintarXiv:2310.13800.

### Michal Štefánik and Marek Kadlcˇík. 2023. Can in-

Han-ChinShing,SurajNair,AyahZirikly,MeirFriedencontext learners learn a reasoning concept from
berg,HalDauméIII,andPhilipResnik.2018. Expert,
demonstrations? In Proceedings of the 1st Workcrowdsourced, and machine assessment of suicide
shoponNaturalLanguageReasoningandStructured
riskviaonlinepostings. InProceedingsoftheFifth
WorkshoponComputationalLinguisticsandClinical Explanations (NLRSE), pages 107–115, Toronto,
Psychology: FromKeyboardtoClinic,pages25–36, Canada.AssociationforComputationalLinguistics.
New Orleans, LA. Association for Computational
HongjinSu,JungoKasai,ChenHenryWu,WeijiaShi,
Linguistics.
TianluWang,JiayiXin,RuiZhang,MariOstendorf,
LukeZettlemoyer,NoahA.Smith,andTaoYu.2022.

### NoahShinn,FedericoCassano,EdwardBerman,Ash-

Selectiveannotationmakeslanguagemodelsbetter
winGopinath,KarthikNarasimhan,andShunyuYao.
few-shotlearners.

## Reflexion: Languageagentswithverbalreinforcementlearning.

Zhi Rui Tam, Cheng-Kuang Wu, Yi-Lin Tsai, Chieh-
Yen Lin, Hung yi Lee, and Yun-Nung Chen. 2024.
Chenglei Si, Dan Friedman, Nitish Joshi, Shi Feng,

### Letmespeakfreely? astudyontheimpactofformat

DanqiChen, andHeHe.2023a. Measuringinducrestrictionsonperformanceoflargelanguagemodels.
tivebiasesofin-contextlearningwithunderspecified
demonstrations. InAssociationforComputational Lv Tang, Peng-Tao Jiang, Hao-Ke Xiao, and Bo Li.
Linguistics(ACL). 2023. Towardstraining-freeopen-worldsegmentationviaimagepromptingfoundationmodels.

### Chenglei Si, Zhe Gan, Zhengyuan Yang, Shuohang

Wang,JianfengWang,JordanBoyd-Graber,andLi- EshaanTanwar,SubhabrataDutta,ManishBorthakur,
juanWang.2023b. Promptinggpt-3tobereliable. andTanmoyChakraborty.2023. MultilingualLLMs
InInternationalConferenceonLearningRepresenta- arebettercross-lingualin-contextlearnerswithaligntions(ICLR). ment. InProceedingsofthe61stAnnualMeetingof
57

<!-- Page 58 -->

theAssociationforComputationalLinguistics(Vol- the61stAnnualMeetingoftheAssociationforComume 1: Long Papers), pages 6292–6307, Toronto, putational Linguistics (Volume 1: Long Papers),
Canada.AssociationforComputationalLinguistics. pages10014–10037,Toronto,Canada.Association
forComputationalLinguistics.

### MingTao, HaoTang, FeiWu, Xiao-YuanJing, Bing-

Kun Bao, and Changsheng Xu. 2022. Df-gan: A RasulTutunov,AntoineGrosnit,JuliuszZiomek,Jun
simpleandeffectivebaselinefortext-to-imagesyn- Wang, and Haitham Bou-Ammar. 2023. Why can
thesis. large language models generate correct chain-ofthoughts?

### Charlotte Thompson and Tiana Kelly. 2023. When

hallucinationsbecomereality: Anexplorationofai Shubham Vatsal and Harsh Dubey. 2024. A survey
packagehallucinationattacks. DarktraceBlog. of prompt engineering methods in large language
modelsfordifferentnlptasks.

### Katherine Tian, Eric Mitchell, Allan Zhou, Archit

Sharma,RafaelRafailov,HuaxiuYao,ChelseaFinn, AntonVoronov,LenaWolf,andMaxRyabinin.2024.
and Christopher Manning. 2023. Just ask for cali- Mindyourformat: Towardsconsistentevaluationof
bration: Strategiesforelicitingcalibratedconfidence in-context learning improvements. arXiv preprint
scoresfromlanguagemodelsfine-tunedwithhuman arXiv:2401.06766.
feedback. In Proceedings of the 2023 Conference
onEmpiricalMethodsinNaturalLanguageProcess- EricWallace,ShiFeng,NikhilKandpal,MattGardner,
ing, pages 5433–5442, Singapore. Association for andSameerSingh.2019. Universaladversarialtrig-
ComputationalLinguistics. gersforattackingandanalyzingnlp. InConference
onEmpiricalMethodsinNaturalLanguageProcess-
LindiaTjuatja,ValerieChen,TongshuangWu,Ameet ing.

### Talwalkwar, and Graham Neubig. 2024. Do llms

exhibithuman-likeresponsebiases? acasestudyin XingchenWan,RuoxiSun,HanjunDai,SercanO.Arik,
surveydesign. TransactionsoftheAssociationfor andTomasPfister.2023a. Betterzero-shotreasoning
ComputationalLinguistics,12:1011–1026. withself-adaptiveprompting.
Hugo Touvron, Louis Martin, Kevin Stone, Peter Al- Xingchen Wan, Ruoxi Sun, Hootan Nakhost, Hanbert, Amjad Almahairi, Yasmine Babaei, Nikolay junDai,JulianMartinEisenschlos,SercanO.Arik,
Bashlykov,SoumyaBatra,PrajjwalBhargava,Shruti and Tomas Pfister. 2023b. Universal self-adaptive
Bhosale,DanBikel,LukasBlecher,CristianCanton prompting.

### Ferrer,MoyaChen,GuillemCucurull,DavidEsiobu,

JudeFernandes,JeremyFu,WenyinFu,BrianFuller, Guanzhi Wang, Yuqi Xie, Yunfan Jiang, Ajay Man-
CynthiaGao,VedanujGoswami,NamanGoyal,An- dlekar,ChaoweiXiao,YukeZhu,LinxiFan,andAnthonyHartshorn,SagharHosseini,RuiHou,Hakan imaAnandkumar.2023a. Voyager: Anopen-ended
Inan,MarcinKardas,ViktorKerkez,MadianKhabsa, embodiedagentwithlargelanguagemodels.

### IsabelKloumann,ArtemKorenev,PunitSinghKoura,

Marie-AnneLachaux,ThibautLavril,JenyaLee,Di- JiaanWang,YunlongLiang,FandongMeng,Haoxiang
anaLiskovich,YinghaiLu,YuningMao,XavierMar- Shi,ZhixuLi,JinanXu,JianfengQu,andJieZhou.
tinet,TodorMihaylov,PushkarMishra,IgorMoly- 2023b. Ischatgptagoodnlgevaluator?apreliminary
bog, Yixin Nie, Andrew Poulton, Jeremy Reizen- study. arXivpreprintarXiv:2303.04048.
stein,RashiRungta,KalyanSaladi,AlanSchelten,
Ruan Silva, Eric Michael Smith, Ranjan Subrama- Jiaqi Wang, Zhengliang Liu, Lin Zhao, Zihao Wu,
nian, Xiaoqing Ellen Tan, Binh Tang, Ross Tay- Chong Ma, Sigang Yu, Haixing Dai, Qiushi Yang,
lor, Adina Williams, Jian Xiang Kuan, Puxin Xu, YihengLiu,SongyaoZhang,EnzeShi,YiPan,Tuo
ZhengYan,IliyanZarov,YuchenZhang,AngelaFan, Zhang, Dajiang Zhu, Xiang Li, Xi Jiang, Bao Ge,
Melanie Kambadur, Sharan Narang, Aurelien Ro- Yixuan Yuan, Dinggang Shen, Tianming Liu, and
driguez,RobertStojnic,SergeyEdunov,andThomas ShuZhang.2023c. Reviewoflargevisionmodels
Scialom.2023. Llama2: Openfoundationandfine- andvisualpromptengineering.
tunedchatmodels.

### Jiaqi Wang, Enze Shi, Sigang Yu, Zihao Wu, Chong

Mark Towers, Jordan K. Terry, Ariel Kwiatkowski, Ma,HaixingDai,QiushiYang,YanqingKang,Jinru
John U. Balis, Gianluca de Cola, Tristan Deleu, Wu,HuawenHu,ChenxiYue,HaiyangZhang,Yi-
Manuel Goulão, Andreas Kallinteris, Arjun KG, hengLiu,XiangLi,BaoGe,DajiangZhu,Yixuan
Markus Krimmel, Rodrigo Perez-Vicente, Andrea Yuan,DinggangShen,TianmingLiu,andShuZhang.
Pierré,SanderSchulhoff,JunJetTai,AndrewTanJin 2023d. Promptengineeringforhealthcare: Method-
Shen,andOmarG.Younis.2023. Gymnasium. ologiesandapplications.
HarshTrivedi,NiranjanBalasubramanian,TusharKhot, JunjieWang,YuchaoHuang,ChunyangChen,ZheLiu,
andAshishSabharwal.2023. Interleavingretrieval SongWang,andQingWang.2023e. Softwaretesting
with chain-of-thought reasoning for knowledge- withlargelanguagemodel: Survey,landscape,and
intensive multi-step questions. In Proceedings of vision.
58

<!-- Page 59 -->

Lei Wang, Wanyu Xu, Yihuai Lan, Zhiqiang Hu, JasonWei,XuezhiWang,DaleSchuurmans,Maarten
Yunshi Lan, Roy Ka-Wei Lee, and Ee-Peng Lim. Bosma,BrianIchter,FeiXia,EdChi,QuocLe,and
2023f. Plan-and-solveprompting: Improvingzero- Denny Zhou. 2023a. Chain-of-thought prompting
shot chain-of-thought reasoning by large language elicitsreasoninginlargelanguagemodels.
models.

### Jerry Wei, Da Huang, Yifeng Lu, Denny Zhou, and

SiyinWang, Chao-HanHuckYang, JiWu, andChao Quoc V Le. 2023b. Simple synthetic data reduces
Zhang.2023g. Canwhisperperformspeech-based sycophancyinlargelanguagemodels. arXivpreprint
in-contextlearning. arXiv:2308.03958.
Jerry Wei, Jason Wei, Yi Tay, Dustin Tran, Albert
Xinyi Wang, Wanrong Zhu, Michael Saxon, Mark

### Webson, Yifeng Lu, Xinyun Chen, Hanxiao Liu,

Steyvers, and William Yang Wang. 2023h. Large

### Da Huang, Denny Zhou, et al. 2023c. Larger

languagemodelsarelatentvariablemodels: Explainlanguagemodelsdoin-contextlearningdifferently.
ingandfindinggooddemonstrationsforin-context
arXivpreprintarXiv:2303.03846.
learning.
YixuanWeng,MinjunZhu,FeiXia,BinLi,ShizhuHe,

### XuezhiWang,JasonWei,DaleSchuurmans,QuocLe,

Shengping Liu, Bin Sun, Kang Liu, and Jun Zhao.

### EdChi,SharanNarang,AakankshaChowdhery,and


## Large language models are better reasoners

DennyZhou.2022. Self-consistencyimproveschain
withself-verification.
ofthoughtreasoninginlanguagemodels.

### JasonWestonandSainbayarSukhbaatar.2023. System

Yaqing Wang, Jiepu Jiang, Mingyang Zhang, Cheng
2attention(issomethingyoumightneedtoo).
Li, Yi Liang, Qiaozhu Mei, and Michael Bendersky. 2023i. Automated evaluation of personalized JulesWhite,QuchenFu,SamHays,MichaelSandborn,
textgenerationusinglargelanguagemodels. arXiv CarlosOlea,HenryGilbert,AshrafElnashar,Jesse
preprintarXiv:2310.11593. Spencer-Smith, and Douglas C. Schmidt. 2023. A
promptpatterncatalogtoenhancepromptengineer-
Yaqing Wang, Quanming Yao, James Kwok, and Li- ingwithchatgpt.
onelM.Ni.2019. Generalizingfromafewexamples:
Asurveyonfew-shotlearning. AlexWilf,SihyunShawnLee,PaulPuLiang,andLouis-

### PhilippeMorency.2023. Thinktwice: Perspective-

Yuqing Wang and Yun Zhao. 2024. Metacognitive taking improves large language models’ theory-ofpromptingimprovesunderstandinginlargelanguage mindcapabilities.
models.

### SimonWillison.2022. Promptinjectionattacksagainst

Zekun Moore Wang, Zhongyuan Peng, Haoran Que, gpt-3.

### Jiaheng Liu, Wangchunshu Zhou, Yuhan Wu,

Hongcheng Guo, Ruitong Gan, Zehao Ni, Man SimonWillison.2024. Promptinjectionandjailbreak-
Zhang, Zhaoxiang Zhang, Wanli Ouyang, Ke Xu, ingarenotthesamething.
Wenhu Chen, Jie Fu, and Junran Peng. 2023j.

### GentaIndraWinata,Liang-KangHuang,SoumyaVad-

Rolellm: Benchmarking, eliciting, and enhancing
lamannati,andYashChandarana.2023. Multilingual
role-playingabilitiesoflargelanguagemodels.
few-shotlearningvialanguagemodelretrieval.

### ZhendongWang,YifanJiang,YadongLu,YelongShen,

Jay Zhangjie Wu, Yixiao Ge, Xintao Wang, Weixian
PengchengHe,WeizhuChen,ZhangyangWang,and

### Lei,YuchaoGu,YufeiShi,WynneHsu,YingShan,


### Mingyuan Zhou. 2023k. In-context learning un-

XiaohuQie,andMikeZhengShou.2023a. Tune-alockedfordiffusionmodels.
video: One-shot tuning of image diffusion models
fortext-to-videogeneration.

### ZhenhailongWang,ShaoguangMao,WenshanWu,Tao


### Ge,FuruWei,andHengJi.2023l. Unleashingcogni-

Ning Wu, Ming Gong, Linjun Shou, Shining Liang,
tivesynergyinlargelanguagemodels:Atask-solving
andDaxinJiang.2023b. Largelanguagemodelsare
agentthroughmulti-personaself-collaboration.
diverse role-players for summarization evaluation.
arXivpreprintarXiv:2303.15078.

### JasonWei,MaartenBosma,VincentZhao,KelvinGuu,

Adams Wei Yu, Brian Lester, Nan Du, Andrew M. Tongshuang Wu, Michael Terry, and Carrie Jun Cai.
Dai, and Quoc V Le. 2022a. Finetuned language 2022. Ai chains: Transparent and controllable
modelsarezero-shotlearners. InInternationalCon- human-ai interaction by chaining large language
ferenceonLearningRepresentations. modelprompts. CHIConferenceonHumanFactors
inComputingSystems.

### JasonWei,XuezhiWang,DaleSchuurmans,Maarten

Bosma,BrianIchter,FeiXia,EdChi,QuocLe,and XiaodongWu,RanDuan,andJianbingNi.2023c. Un-
Denny Zhou. 2022b. Chain-of-thought prompting veilingsecurity,privacy,andethicalconcernsofchatelicitsreasoninginlargelanguagemodels. gpt. JournalofInformationandIntelligence.
59

<!-- Page 60 -->

CongyingXia, ChenXing, JiangshuDu, XinyiYang, Yao Yao, Zuchao Li, and Hai Zhao. 2023c. Beyond
Yihao Feng, Ran Xu, Wenpeng Yin, and Caiming chain-of-thought,effectivegraph-of-thoughtreason-
Xiong.2024. Fofo: Abenchmarktoevaluatellms’ inginlargelanguagemodels.
format-followingcapability.

### MichihiroYasunaga,XinyunChen,YujiaLi,Panupong

Miao Xiong, Zhiyuan Hu, Xinyang Lu, Yifei Li, Jie Pasupat, Jure Leskovec, Percy Liang, Ed H. Chi,
Fu,JunxianHe,andBryanHooi.2023a. Canllms andDennyZhou.2023. Largelanguagemodelsas
express their uncertainty? an empirical evaluation analogicalreasoners.
of confidence elicitation in llms. arXiv preprint
arXiv:2306.13063. Qinyuan Ye, Maxamed Axmed, Reid Pryzant, and

### FereshteKhani.2023. Promptengineeringaprompt

Miao Xiong, Zhiyuan Hu, Xinyang Lu, Yifei Li, Jie
engineer.

### Fu,JunxianHe,andBryanHooi.2023b. Canllms

express their uncertainty? an empirical evaluation

### XiYeandGregDurrett.2023. Explanationselection

of confidence elicitation in llms. arXiv preprint
usingunlabeleddataforchain-of-thoughtprompting.
arXiv:2306.13063.

### KangMinYoo,JunyeobKim,HyuhngJoonKim,Hyun-

Xiaohan Xu, Chongyang Tao, Tao Shen, Can Xu,
sooCho,HwiyeolJo,Sang-WooLee,SanggooLee,
Hongbo Xu, Guodong Long, and Jian guang Lou.
andTaeukKim.2022. Ground-truthlabelsmatter: A

## Re-reading improves reasoning in language

deeperlookintoinput-labeldemonstrations.
models.
OriYoran,TomerWolfson,BenBogin,UriKatz,Daniel

### TianciXue,ZiqiWang,ZhenhailongWang,ChiHan,


### Deutch, and Jonathan Berant. 2023. Answering


### Pengfei Yu, and Heng Ji. 2023. Rcot: Detecting

questions by meta-reasoning over multiple chains
andrectifyingfactualinconsistencyinreasoningby
ofthought.
reversingchain-of-thought.
ChengrunYang,XuezhiWang,YifengLu,HanxiaoLiu, Adeel Yousaf, Muzammal Naseer, Salman Khan, Fa-
QuocV.Le,DennyZhou,andXinyunChen.2023a. hadShahbazKhan,andMubarakShah.2023. Video-
Largelanguagemodelsasoptimizers. prompter: anensembleoffoundationalmodelsfor
zero-shotvideounderstanding.
HaiboYang,YangChen,YingweiPan,TingYao,ZhinengChen,andTaoMei.2023b. 3dstyle-diffusion: Yue Yu, Yuchen Zhuang, Jieyu Zhang, Yu Meng,
Pursuingfine-grainedtext-driven3dstylizationwith Alexander Ratner, Ranjay Krishna, Jiaming Shen,
2ddiffusionmodels. and Chao Zhang. 2023. Large language model as
attributedtrainingdatagenerator: Ataleofdiversity
HuiYang,SifuYue,andYunzhongHe.2023c. Auto- andbias. arXivpreprintarXiv:2306.15895.
gpt for online decision making: Benchmarks and
additionalopinions. XiangYue,BoshiWang,KaiZhang,ZiruChen,YuSu,
and Huan Sun. 2023. Automatic evaluation of at-
Xinyi Yang, Runzhe Zhan, Derek F. Wong, Junchao tributionbylargelanguagemodels. arXivpreprint
Wu,andLidiaS.Chao.2023d. Human-in-the-loop arXiv:2305.06311.
machinetranslationwithlargelanguagemodel. In
ProceedingsofMachineTranslationSummitXIXVol.

### ZhiyuanZeng,JiatongYu,TianyuGao,YuMeng,Tanya

2: Users Track, pages 88–98, Macau SAR, China.
Goyal, and Danqi Chen. 2023. Evaluating large
MachineTranslationSummit.
languagemodelsatevaluatinginstructionfollowing.
arXivpreprintarXiv:2310.07641.

### ZhengyuanYang,LinjieLi,KevinLin,JianfengWang,

Chung-Ching Lin, Zicheng Liu, and Lijuan Wang.
MichaelJQZhangandEunsolChoi.2023. Clarifywhen
2023e. Thedawnoflmms: Preliminaryexplorations
necessary: Resolvingambiguitythroughinteraction
withgpt-4v(ision). ArXiv,abs/2309.17421.
withlms. arXivpreprintarXiv:2311.09469.
Binwei Yao, Ming Jiang, Diyi Yang, and Junjie Hu.

### QuanjunZhang,TongkeZhang,JuanZhai,Chunrong

2023a. Empoweringllm-basedmachinetranslation
Fang, BowenYu, WeisongSun, andZhenyuChen.
withculturalawareness.
2023a. Acriticalreviewoflargelanguagemodelon
Shunyu Yao, Dian Yu, Jeffrey Zhao, Izhak Shafran, softwareengineering: Anexamplefromchatgptand
Thomas L. Griffiths, Yuan Cao, and Karthik automatedprogramrepair.

### Narasimhan. 2023b. Tree of thoughts: Deliberate

problemsolvingwithlargelanguagemodels. Yifan Zhang, Jingqin Yang, Yang Yuan, and Andrew

### Chi-Chih Yao. 2023b. Cumulative reasoning with

Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak largelanguagemodels.
Shafran,KarthikNarasimhan,andYuanCao.2022.
React: Synergizingreasoningandactinginlanguage YimingZhang,ShiFeng,andChenhaoTan.2022a. Acmodels. tiveexampleselectionforin-contextlearning.
60

<!-- Page 61 -->

Zhuosheng Zhang, Yao Yao, Aston Zhang, Xiangru Denny Zhou, Nathanael Schärli, Le Hou, Jason Wei,
Tang,XinbeiMa,ZhiweiHe,YimingWang,Mark Nathan Scales, Xuezhi Wang, Dale Schuurmans,
Gerstein, RuiWang, GongshenLiu, andHaiZhao. ClaireCui,OlivierBousquet,QuocLe,etal.2022a.
2023c. Igniting language intelligence: The hitch- Least-to-most prompting enables complex reasonhiker’sguidefromchain-of-thoughtreasoningtolan- ing in large language models. arXiv preprint
guageagents. arXiv:2205.10625.
Zhuosheng Zhang, Aston Zhang, Mu Li, and Alex Yongchao Zhou, Andrei Ioan Muresanu, Ziwen Han,
Smola.2022b. Automaticchainofthoughtprompt- KeiranPaster,SilviuPitis,HarrisChan,andJimmy
inginlargelanguagemodels. Ba.2022b. Largelanguagemodelsarehuman-level
promptengineers.
Zhuosheng Zhang, Aston Zhang, Mu Li, Hai Zhao,

### YuchengZhou,XiuboGeng,TaoShen,ChongyangTao,

George Karypis, and Alex Smola. 2023d. Multi-
GuodongLong,Jian-GuangLou,andJianbingShen.
modalchain-of-thoughtreasoninginlanguagemod-

## Threadofthoughtunravelingchaoticcontexts.

els.

### XizhouZhu,YuntaoChen,HaoTian,ChenxinTao,Wei-

Ruochen Zhao, Xingxuan Li, Shafiq Joty, Chengwei jieSu,ChenyuYang,GaoHuang,BinLi,LeweiLu,
Qin, and Lidong Bing. 2023a. Verify-and-edit: A Xiaogang Wang, Yu Qiao, Zhaoxiang Zhang, and
knowledge-enhanced chain-of-thought framework. Jifeng Dai. 2023. Ghost in the minecraft: Gener-
In Proceedings of the 61st Annual Meeting of the allycapableagentsforopen-worldenvironmentsvia
AssociationforComputationalLinguistics(Volume large language models with text-based knowledge
1: LongPapers),pages5823–5840,Toronto,Canada. andmemory.
AssociationforComputationalLinguistics.

### ZhichaoZuo,ZhaoZhang,YanLuo,YangZhao,Haijun

TonyZ.Zhao,EricWallace,ShiFeng,DanKlein,and Zhang, Yi Yang, and Meng Wang. 2023. Cut-and-
SameerSingh.2021a. Calibratebeforeuse: Improv- paste: Subject-driven video editing with attention
ingfew-shotperformanceoflanguagemodels. control.

### YilunZhao,HaoweiZhang,ShengyunSi,LinyongNan,

XiangruTang,andArmanCohan.2023b. Largelanguagemodelsareeffectivetable-to-textgenerators,
evaluators,andfeedbackproviders. arXivpreprint
arXiv:2305.14987.
YuyangZhao,ZhiwenYan,EnzeXie,LanqingHong,
ZhenguoLi,andGimHeeLee.2023c. Animate124:
Animatingoneimageto4ddynamicscene.

### Zihao Zhao, Eric Wallace, Shi Feng, Dan Klein, and

Sameer Singh. 2021b. Calibrate before use: Improvingfew-shotperformanceoflanguagemodels.
InInternationalConferenceonMachineLearning,
pages12697–12706.PMLR.

### ChujieZheng,HaoZhou,FandongMeng,JieZhou,and

MinlieHuang.2023a. Onlargelanguagemodels’selectionbiasinmulti-choicequestions. arXivpreprint
arXiv:2309.03882.

### GeZheng,BinYang,JiajinTang,Hong-YuZhou,and

SibeiYang.2023b. Ddcot: Duty-distinctchain-ofthoughtpromptingformultimodalreasoninginlanguagemodels.
HuaixiuStevenZheng,SwaroopMishra,XinyunChen,

### Heng-TzeCheng,EdH.Chi,QuocVLe,andDenny

Zhou.2023c. Takeastepback: Evokingreasoning
viaabstractioninlargelanguagemodels.
MingqianZheng,JiaxinPei,andDavidJurgens.2023d.

### Is"ahelpfulassistant"thebestroleforlargelanguage

models? a systematic evaluation of social roles in
systemprompts.
61

<!-- Page 62 -->


### A Appendices


### A.1 DefinitionsofPrompting


### Reference Prompt PromptEngineering

(Meskó, The practice of designing, refining, and
2023) implementingpromptsorinstructionsthat
guidetheoutputofLLMstohelpinvarioustasks. Itisessentiallythepracticeof
effectivelyinteractingwithAIsystemsto
optimizetheirbenefits.
(Chen et al., theinputofthemodel the process of structuring input text for
2023a) LLMsandisatechniqueintegraltooptimizingtheefficacyofLLMs
(Santu and refers to a textual input provided to the involves crafting and revising the query
Feng,2023) LLMs with the intention of guiding its orcontextinsuchawaythatitelicitsthe
outputtowardaspecifictask desiredresponseorbehaviorfromLLMs
(Wang et al., involves designing effective prompts to
2023d) guide the pre-trained language model in
downstreamtasks.
(Wang et al., theprocessofdesigningpromptsthaten-
2023c) ablethemodeltoadaptandgeneralizeto
differenttasks. downstreamtasks.
(Hou et al., manuallypredefinednaturallanguagein- thecarefuldesignofspecializedprompts
2023) structions
(Wang et al., inputoftheLLMs communicate with LLMs to steer its be-
2023e) haviorfordesiredoutcomes
(Whiteetal., Instructions given to an LLM to enforce anincreasinglyimportantskillsetneeded
2023) rules,automateprocesses,andensurespe- to converse effectively with large lancificqualities(andquantities)ofgenerated guagemodels(LLMs),suchasChatGPT
output. Prompts are also a form of prothe means by which LLMs are programmingthatcancustomizetheoutputs
grammedviaprompts
andinteractionswithanLLM.

### Apromptisasetofinstructionsprovided

toanLLMthatprogramstheLLMbycustomizingitand/oren-hancingorrefining
itscapabilities
(Heston and theinput structuringtheinputinaspecializedman-

### Khun,2023) ner

(Liu et al., choosingaproperprompt
2023b)
theprocessofcreatingapromptingfunction f (x) that results in the most
prompt
effectiveperformanceonthedownstream
task.
62

<!-- Page 63 -->

(Hadi et al., the instructions provided to an LLM to refers to the designing and wording of
2023) makeitfollowspecifiedrules,automation promptsgiventoLLMssoastogetadeof processes and to ensure that the out- siredresponsefromthem.
put generated is of a specific quality or
quantity
(Neagu, entails various strate- gies, including ex-
2023) plicitinstruction,andimplicitcontext[21].
Explicitinstructioninvolvesprovidingexplicitguidanceorconstraintstothemodel
throughinstructions,examples,orspecifications. Implicit context leverages the
model’sunder-standingofthepreceding
contexttoinfluenceitsresponse
(Dang et al., the systematic practice of constructing
2022) promptstoimprovethegeneratedoutput
ofagenerativemodel
TableA.1: DefinitionsofPromptandPromptEngineeringfromdifferentpapers.
63

<!-- Page 64 -->

A.2 ExtendedVocabulary

### A.2.1 PromptingTerms

ContextWindow Thecontextwindowisthespaceoftokens(forLLMs)whichthemodelcanprocess.
Ithasamaximallength(thecontextlength).
Priming (Schulhoff,2022) referstogivingamodelaninitialpromptthatlaysoutcertaininstructions
fortherestofaconversation. Thisprimingpromptmightcontainsaroleorotherinstructionsonhowto
interactwiththeuser. Primingcaneitherbedoneinthesystemoruserprompt(seebelow).

### A.2.2 PromptEngineeringTerms

ConversationalPromptEngineering isPromptEngineeringincolloquio. Thatis,duringthecourseofa
conversationwithaGenAI,ausermayasktheGenAItorefineitsoutput. Incontrast,promptengineering
isoftendonebysendingtheGenAIacompletelynewpromptratherthancontinuingaconversation.

### A.2.3 Fine-TuningTerms

Prompt-BasedLearning (Liuetal.,2023b),alsoknownasPromptLearning(Liuetal.,2023b;Wang
etal.,2023d)referstotheprocessofusingprompting-relatedtechniques. Itoftenisusedinthecontextof
fine-tuning,especiallyfine-tuningprompts. Duetoconflictingusage,wedonotusethisterm.
Prompt Tuning (Lester et al., 2021) refers to directly optimizing the weights of the prompt itself,
usuallythroughsomeformofgradient-basedupdates. IthasalsobeenreferredtohasPromptFine-Tuning.
Itshouldnotbeusedtorefertodiscretepromptengineering.

### A.2.4 OrthogonalPromptTypes

Wenowdiscussterminologyforhigh-levelwaysofclassifyingprompts.

### A.2.4.1 Originator

UserPrompt Thisisthetypeofpromptthatcomesfromtheuser. Thisisthemostcommonformof
promptingandishowpromptsareusuallydeliveredinconsumerapplications.
AssistantPrompt This"prompt"issimplytheoutputoftheLLMitself. Itcanbeconsideredaprompt
(orpartofone)whenitisfedbackintothemodel,forexampleaspartofaconversationhistorywitha
user.
SystemPrompt ThispromptisusedtogiveLLMshighlevelinstructionsforinteractingwithusers. Not
allmodelshavethis.

### A.2.4.2 HardvsSoftPrompts

Hard (discrete) Prompt These prompts only contain tokens that directly correspond to words in the
LLMvocabulary.
Soft(continuous)Prompt Thesepromptscontaintokensthatmaynotcorrespondtoanywordinthe
vocabulary(Lesteretal.,2021;Wangetal.,2023c). Softpromptscanbeusedwhenfine-tuningisdesired,
butmodifyingtheweightsofthefullmodelisprohibitivelyexpensive. Thus,afrozenmodelcanbeused
whileallowinggradientstoflowthroughtheprompttokens.
HardPrompts ⊆ SoftPrompts

### A.2.4.3 PredictionStyles

In LLMs, a prediction style is the format in which it predicts the next token. There are two common
formatsforthisinpromptingresearch. Wedonotdiscussnon-textpredictionstyles.
Cloze InClozeprompts,thetoken(s)tobepredictedarepresentedas"slotstofill",usuallysomewhere
inthemiddleoftheprompt(Liuetal.,2023b). Thisisusuallythecaseforearliertransformermodels
suchasBERT(ChuandLin,2023).
64

<!-- Page 65 -->

Prefix InPrefixprompts,thetokentobepredictedisattheendoftheprompt(Liuetal.,2023b). Thisis
usuallythecasewithmodernGPT-stylemodels(Radfordetal.,2019b).
65

<!-- Page 66 -->


### A.3 Datasheet

We present a datasheet (Gebru et al., 2021) with more information about the associated paper dataset,
whichishostedonHuggingFace.

### A.3.1 Motivation

Forwhatpurposewasthedatasetcreated? Wasthereaspecifictaskinmind? Wasthereaspecific
gapthatneededtobefilled? Pleaseprovideadescription.
Thisdatasetwascreatedtogatherexistingliteratureonpromptengineeringinordertoanalyzeallcurrent
hardprefixpromptingtechniques.
Whocreatedthedataset(e.g.,whichteam,researchgroup)andonbehalfofwhichentity(e.g.,
company,institution,organization)?
This research was associated with the University of Maryland, Learn Prompting, and sponsored by
OpenAI,butnotcreatedonthebehalfofanyparticularorganization.
Whofundedthecreationofthedataset? Ifthereisanassociatedgrant,pleaseprovidethename
ofthegrantorandthegrantnameandnumber.
OpenAIcontributed$10,000increditsfortheirAPI.

### A.3.2 Composition

Whatdotheinstancesthatcomprisethedatasetrepresent(e.g.,documents,photos,people,countries)? Aretheremultipletypesofinstances(e.g.,movies,users,andratings;peopleandinteractions
betweenthem;nodesandedges)? Pleaseprovideadescription.
Thedatasetcontains1,565researchpapersinPDFformat. Anyduplicatepaperswereremovedautomatically,thoughsomecouldexist.
What data does each instance consist of? “Raw” data (e.g., unprocessed text or images) or
features? Ineithercase,pleaseprovideadescription.
EachdatainstanceisaresearchpaperasaPDF.
Istherealabelortargetassociatedwitheachinstance? Ifso,pleaseprovideadescription.

### No

Is any information missing from individual instances? If so, please provide a description, explainingwhythisinformationismissing(e.g.,becauseitwasunavailable). Thisdoesnotinclude
intentionallyremovedinformation,butmightinclude,e.g.,redactedtext.
No.
Are there any errors, sources of noise, or redundancies in the dataset? If so, please provide a
description.
The papers were gathered in a semi-automated process which introduced the possibility of irrelevant
papersbeingcollectedandrelevantpapersnotbeingcollected. Thereweremanualreviewsdoneforboth
possibleerrorstomitigatetheseerrors.
Is the dataset self-contained, or does it link to or otherwise rely on external resources (e.g.,
websites,tweets,otherdatasets)?
Itisself-contained.
Doesthedatasetcontaindatathatmightbeconsideredconfidential(e.g.,datathatisprotectedby
legalprivilegeorbydoctor–patientconfidentiality,datathatincludesthecontentofindividuals’
non-publiccommunications)? Ifso,pleaseprovideadescription.
No.
Doesthedatasetcontaindatathat,ifvieweddirectly,mightbeoffensive,insulting,threatening,
ormightotherwisecauseanxiety? Ifso,pleasedescribewhy.
The dataset contains some papers on prompt injection. These papers may contain offensive content
includingracismandsexism.
66

<!-- Page 67 -->


### A.3.3 CollectionProcess


### Howwasthedataassociatedwitheachinstanceacquired?

ThedatasetwascompiledfromArxiv,SemanticScholar,andACL.

### Whatmechanismsorprocedureswereusedtocollectthedata?

WewrotescriptstoautomaticallyquerytheAPIsofArxivandSemanticScholar.

### Overwhattimeframewasthedatacollected?

Thedatasetwascuratedthedurationoftheresearchpaper,primarilyinFebruaryof2024.
Wereanyethicalreviewprocessesconducted?
No.

### A.3.4 Preprocessing/Cleaning/Labeling


### Wasanypreprocessing/cleaning/labelingofthedatadone?

Aftercollectingdatafromdifferentsources,weremovedduplicatepapersanddidamanualandsemiautomatedreviewofpaperstoensuretheywereallrelevant.
Wasthe“raw”datasavedinadditiontothepreprocessed/cleaned/labeleddata?
No,wedonotanticipatetheuseofourpreprocesseddata. However,rawdatacanberecoveredfromthe
linkswestore.
Isthesoftwarethatwasusedtopreprocess/clean/labelthedataavailable?
ItiscontainedwithinourcoderepositoryonGithub.

### A.3.5 Uses

Hasthedatasetbeenusedforanytasksalready?
No.
Istherearepositorythatlinkstoanyorallpapersorsystemsthatusethedataset?
Yes.
Isthereanythingaboutthecompositionofthedatasetorthewayitwascollectedandpreprocessed/cleaned/labeledthatmightimpactfutureuses?
AllofthepaperswecollectedwerewritteninEnglish. Itispossiblesomepaperswerenotincludeddueto
atranslationnotbeingavailable.
Aretheretasksforwhichthedatasetshouldnotbeused?
No.

### A.3.6 Distribution

Willthedatasetbedistributedtothirdpartiesoutsideoftheentityonbehalfofwhichthedataset
wascreated?
No.

### A.3.7 Maintenance

Whowillbesupporting/hosting/maintainingthedataset?
Ourteamwillcontinuemaintenance.
Howcantheowner/curator/managerofthedatasetbecontacted?
Pleaseemailusatsanderschulhoff@gmail.com
Isthereanerratum?
No.
Ifotherswanttoextend/augment/buildon/contributetothedataset, isthereamechanismfor
themtodoso?
Yes,anyoneisfreetouse/modifythedata.
67

<!-- Page 68 -->


### A.4 Keywords

Herearethekeywordsweusedforsearch.
• jailbreakprompt
• promptanllm
• promptalargelanguagemodel
• promptinjection
• promptoptimization
• promptengineering
• few-shotlearning
• fewshotlearning
• prompt-basedmethods
• promptbasedmethods
• prompting-basedmethods
• promptingbasedmethods
• few-shotprompt
• fewshotprompt
• one-shotprompt
• oneshotprompt
• few-shotprompting
• fewshotprompting
• one-shotprompting
• oneshotprompting
• promptingtechniques
• promptengineeringtechniques
• llmprompting
• largelanguagemodelprompting
• 0-shotprompt
• 0shotprompt
• zero-shotprompt
• many-shotprompt
• zero-shotprompting
• many-shotprompting
68

<!-- Page 69 -->

• in-contextlearning
• incontextlearning
• transformermodelprompts
• prompt-basedtransferlearning
• nlppromptingstrategies
• llminterpretabilityviaprompts
• curriculumlearningwithprompts
• feedbackloopsinllmprompting
• human-in-the-loopprompting
• token-efficientprompting
• multimodalprompting
• instructionprompting
• prompttemplating
• prompttemplate
69

<!-- Page 70 -->


### A.5 PromptforSystematicLiteratureReview

Pleasefindthepromptweusedhere. Wepresentitintextinthisdocument,butnotethatyoushoulduse
theversioninourcodebaseratherthancopyandpastethis.

### Weusedthefollowingsystemprompt:

Youarealabassistant,helpingwithasystematicreviewonpromptengineering. You’vebeenaskedto
ratetherelevanceofapapertothetopicofpromptengineering. Tobeclear,thisreviewwillstrictlycover
hard prefix prompts. For clarification: Hard prompts have tokens that correspond directly to words in
thevocab. Forexample,youcouldmakeupanewtokenbyaddingtwotogether. Thiswouldnolonger
correspondtoanywordinthevocabulary,andwouldbeasoftpromptPrefixpromptsarepromptsused
formostmoderntransformers,wherethemodelpredictsthewordsafterthisprompt. Inearliermodels,
suchasBERT,modelscouldpredictwords(e.g. <MASK>)inthemiddleoftheprompt. Yourjobistobe
abletotellwhetherapaperisrelatedto(orsimplycontains)hardprefixpromptingorpromptengineering.
Pleasenotethatapapermightnotspelloutthatitisusing"hardprefix"promptingandsoitmightjustsay
prompting. Inthiscase,youshouldstillrateitasrelevanttothetopicofpromptengineering. Pleasealso
note,thatapaperthatfocusesontrainingamodelasopposedtopost-trainingpromptingtechniquesis
consideredirrelevant. ProvidearesponseinJSONformatwithtwofields: ’reasoning’(asinglesentence
thatjustifiesyourreasoning)and’rating’(astringthatisoneofthefollowingcategories: ’highlyrelevant’,
’somewhatrelevant’,’neutrallyrelevant’,’somewhatirrelevant’,’highlyirrelevant’)indicatingrelevance
tothetopicofpromptengineering)
Then,weusedthisuserprompttemplatetoinputinformationforeachpaper:
Title: ’{title}’,Abstract: ’{abstract}’. Rateitsrelevancetothetopicofpromptengineeringasoneofthe
followingcategories: ’highlyrelevant’,’somewhatrelevant’,’neutrallyrelevant’,’somewhatirrelevant’,
’highlyirrelevant’,andprovidetextfromtheabstractthatjustifiesyourreasoning
70

<!-- Page 71 -->

A.6 EvaluationTable

## Id Model

RolesCoT

## P


## D


## R

e

## O

fin

## M

it

## P

io

## T

nFew-Shot

## Outputspace Typeres.Batch

(Kocmi and Federmann, 2023b)GPT-family DA,sMQM,stars,classes E S
(Lu et al., 2023c) Dav3,GPT-4-Turbo,GPT-4 ✓ ✓ ✓ ErrorSpan→Score E S ✓
(Fernandes et al., 2023) PaLM ✓ ✓ ✓ ErrorSpan I S
(Kocmi and Federmann, 2023a)GPT-4 ✓ ✓ ✓ ErrorSpan I S ✓
(Araújo and Aguiar, 2023) ChatGPT ✓ Likert[1-5] E S ✓
(Wang et al., 2023b) ChatGPT ✓ DA,stars E S
(Liu et al., 2023d)† GPT-3.5,GPT-4 ✓ Likert[1-10] I M
(Chan et al., 2024) ChatGPT,GPT-4 ✓ ✓ Likert[1-10] I M
(Luo et al., 2023) ChatGPT ✓ ✓ yes/no;A/B;Likert[1-10] E S
(Hada et al., 2024) GPT-4-32K ✓ ✓ [0,1,2]orbinary E S ✓
(Fu et al., 2023a) GPT-3,OPT,FLAN-T5,GPT-2 Probability I S
(Gao et al., 2023c) ChatGPT ✓ Likert[1-5],Pairwise,Pyramid,0/1 E S
(Chen et al., 2023g) ChatGPT Likert[1-10];yes/no;pairwise:A/B/CE&I S
(He et al., 2023a) GPT-4 ✓ Likert[1-5] E S
(Sottana et al., 2023) GPT-4 ✓ Likert[1-5] E S
(Chen et al., 2023c) GPT,Flan-T5 ✓ Yes/No E S
(Zhao et al., 2023b) GPT-3.5,GPT-4 ✓ ✓ true/false E S
(Wu et al., 2023b) GPT-3 ✓ pairwisevoting E M ✓
(Wang et al., 2023i) PaLM2-IT-L A/B E M
(Jia et al., 2023) LLaMa7b Probability I S
(Yue et al., 2023) ChatGPT,Alpaca,Vicuna,GPT-4 ✓ ✓ Yes/No E S
(Li et al., 2023e) GPT-3.5,GPT-4,Bard,Vicuna ✓ Pairwise I M
(Liu et al., 2023f) ChatGPT,Vicuna,chatGLM,StableLM ✓ continuous[0-1] E S
(Bai et al., 2023b) GPT-4,Claude,ChatGPT,Bard,Vicuna ✓ Likert[1-5] E S
(Dubois et al., 2023) GPT-4,ChatGPT,Dav3 ✓ ✓ pairwise E M ✓
(Liu et al., 2023h)† GPT-4-32K ✓ Likert[1-5] E S
(Wang et al., 2023h) GPT-4-Turbo,ChatGPT,GPT-4,Vicuna ✓ Likert[1-10] E M
(Zeng et al., 2023) GPT-4,ChatGPT,LLaMA-2-Chat,PaLM2,Falcon ✓ ✓ ✓ Pairwise E S
(Zheng et al., 2023b) Claude-v1,GPT-3.5,GPT-4 ✓ ✓ Pairwise/Likert[1-10] E S/M
(Lin and Chen, 2023) Claude-v1.3 Likert[0-5],Likert[0-100] E S ✓
TableA.2:EvaluationPaperSummary.E:Explicit(whetherthemodelgeneratesanassessment),I:Implicit(whether
anassessmentisderivedfromthemodeloutput);Response(Res.) S:Singleresponse,M:Multipleresponses;†:
Modelgeneratedinstruction;
71

<!-- Page 72 -->


### A.7 EntrapmentPromptingProcess

Thissectioncontainsthethoughtprocessofourpromptengineerashedevelopedtheprompt.

### A.7.1 Exploration

• Firstdidabitofdatasetexploration,lookingatlength/labeldistribution,thenchoseentrapmentto
startwith.
• Checkedifgpt-1106-previewunderstoodentrapment,byaskingittodefinethetermWRTSCS.It
didnot.

### A.7.2 GettingaLabel

• Showeditthedefinitionofentrapmentinthesystempromptandaskedittolabeladatapoint,butit
respondedsayingIshouldseekmentalhealthsupport.
• Iputtheinstructionsintheuserprompt,butgetasimilarresponse.
• Appending"Isthisentrapment? Yesorno"gotittoactuallyrespondwithalabel.
• Igaveitarejectexample,butitlabeleditasaccept,andalsosometimesgivesemotionalresponses
aboutgettinghelp.
• Using10-shotprompting,itstillgivesthegethelpresponses.
• Itriedremovingthedefinition,gotthesameproblem. Itseemsthatitdoesn’tlike"accept"/"reject"
aslabels.
• Iaddedbackthedefinition,changedlabelstoentrapment/notentrapment,itoftensays"notenough
infotodetermine".
• IswitchedtoGPT-4-32K,whichgaveonewordresponsesandcorrectlypredictedarejectandan
acceptdatapoint.
A.7.3 VaryingPromptingTechniques
• Tested0-shotwithcontext.
• 10-shotwithcontext,showedimprovement.
• Takingfirstfailinginstanceintoplayground. (12thintrainfile)
• Trieddoing’A:Let’sgostepbystepandfigurethisout: ",output"A:Yes"
• Did"A:Let’sgostepbystepandfigurethisout: ",OUTPUT:
The individual in this post is expressing feelings of hopelessness, loneliness, and despair.
Theymentionasignificantloss(theirmother)andasubsequentdeclineintheirmentalhealth,
turning to alcohol as a coping mechanism. They also mention financial struggles and the
possibility of becoming homeless. They express feelings of guilt and shame about their
situationandcomparethemselvesnegativelytotheirfriendsandfamily. Mostconcerning
is their detailed plan for suicide, involving sleeping pills and alcohol. They also mention
consideringsteppinginfrontofacar. Giventhesefactors,thelabelforthispostwouldbe
"Yes"forexpressingfeelingsofentrapment.
72

<!-- Page 73 -->

• "A:Beforepredictingalabel,let’sgostepbystepandwriteoutyourthoughtprocess. Usetheitems
inthedefinitionofentrapmenttosupportyourconclusion.",OUTPUT:
Beforepredictingalabel,let’sgostepbystepandwriteoutyourthoughtprocess. Usethe
itemsinthedefinitionofentrapmenttosupportyourconclusion.
• BegandiscussingwiththeAI"theydon’teversaytheyfeeltrappedorthatthereisnowayout,how
didugetthatidea?",OUTPUT:
Theindividualdoesn’texplicitlystatethattheyfeeltrappedorthatthereisnowayout,but
theirnarrativesuggestsasenseofentrapment. Theymentionthattheyarefacingeviction,
strugglingwithdebt, anddealingwithadecreaseinincome. Theyalsoexpressasenseof
hopelessnessanddespair,andcontemplatesuicideasapotentialsolutiontotheirproblems.
These elements suggest a feeling of being trapped in their current circumstances with no
apparent way out. However, it’s important to note that this interpretation is based on the
informationprovidedinthepostandtheindividual’sexpressedfeelingsandthoughts.
• Asked it to help reformulate instructions to make explicitness more clearly needed, still predicts
entrapment.
• Added"ENTRAPMENTMUSTBEEXPLICIT,NOTIMPLICIT."toinstructionattopafterdefinitions(noCoTinducer)
• AlsotriedwithpreviousCoTinducer,stillsaysentrapmentinahardtoparseoutway.
• Added"Ifthepersondoesnotexplicitlysaytheyfeeltrapped,thisdoesn’tcountasentrapment."(no
CoT),stillentrapment.
• TalkingtoAI,itthinks"TodayIfoundoutIhave10daystovacatemyapartmentorI’llbeformally
evicted. I’m2monthsbehindonmyrentduetoabadtimewhereIgotdemotedatworkandrent
frommakingroughly$1000ever2weekstoaround$450. IfIgetevicted,I’llprobablybehomeless"
isfeelingtrapped/stuck.
• Tried"Beforestatingalabel,writeoutreasoningusingthegridaboveaboutwhythismay/maynot
beentrapment:",stillthinksentrapment.
• pasteinemail: [REDACTED]abovedefinitionofentrapment
• removeshots,says"Entrapment"
• addthisafterdef: IMPORTANT:Onlylabelthepostasentrapmentiftheyexplicitlysaythatthey
feeltrapped.,says"Yes"
• Intheprompt,gaveitCoTreasoning. (18.txt),andtriedwiththenextwronglylabeledone(15),(full
prompt,19.txt)
• Testedthisoneverythingexceptfirst20,didprettywell
• Triedremovingemail,performancedroppedofacliff
• Atthispoint,Iamthinkingthatgivingexampleswithreasoninghelps(obviously)
• Triedtoadd10shotsinforfree,beforethelastonewithreasoning,badresults
73

<!-- Page 74 -->


### A.7.3.1 AutoCoT

• Developdatasetusingthisprompt(22.txt). Thenaskit"Why?". Ifitdisagrees,Isay"Itisactually
notentrapment,pleaseexplainwhy."(accidentallyduplicatedemail23.txt)
• Justforfun,tried0shotfullcontext(hadtoadjustverbalizer)
• triedthiswithspecialverbalizerwhichcatches"ThispostdoesnotmeetthecriteriaforEntrapment."
• Testedmygenerateddata,beat0.5F1
• Doing10moreexemplarswautocot. Sometimesrespondsimmediatelywithreasoninglike"This
postdoesnotmeetthecriteriaforEntrapmentastheindividualdoesnotexplicitlyexpressfeelings
ofbeingtrappedorhopeless.",sojustusethatifso. Sometimesgetrefusal"I’mreallysorrytohear
thatyou’refeelingthisway,butI’munabletoprovidethehelpthatyouneed. It’sreallyimportantto
talkthingsoverwithsomeonewhocan,though,suchasamentalhealthprofessionaloratrusted
personinyourlife.",justask"Explainwhyitisnotentrapment."afterifso.
• performancedidntreallyimprove,realizedabout11%aregetting-1,meaningnotextractedproperly.
Retryingwithfullwords"Question"insteadofQ,alsoforreasoningandanswer.
• thisledtohigherinabilitytoparse,atabout16%.

### A.7.3.2 DevelopingAnswerExtraction

• putfirstfailingtoparseonein(22),anddevelopedapromptforit.
• did worse: (0.42857142857142855, 0.5051546391752577, 0.8571428571428571,
0.2857142857142857)
• only using extracted label if have -1 helps slightly to (0.48, 0.61, 0.8571428571428571,
0.3333333333333333)
• goingbacktobestperformingprompt–10QRAshot,andperformingextractionwithany-1s,doesnt
helpotherthangentlyboostingaccuracy,perhapswhenitdoesntanswer

### A.7.3.3 IteratingonEmail

• triedbestperf,withnoemail
• triedwithdedupedemail,worseresults
• noticedthatonesitsunsureaboutoftencontained1labelsthatshouldbe0,sotryingto"recover"
thesedoesnthelp
• trymovingaroundexemplarorder,performingextraction,didnthelp
• triplicatedemail,didnthelp
74

<!-- Page 75 -->


### A.8 FormallyDefiningaPrompt

"Prompt" is a widely used term, but uses and definitions differ widely across research. As a result, it
is difficult to create a formal, mathematical definition for a prompt. In this section, we outline some
formalismsforpromptengineering.
AsaconditioningMechanism. Qiaoetal.(2022)presentthefollowingdefinition,whichinvolvesthe
prompt T and a question Q as conditioning mechanisms on predicting the next token. Note that they
appeartouseBrownetal.(2020)’soriginaldefinitionofprompt,whichreferstothenon-questionpartof
theprompt(e.g. few-shotexemplars,instructions).

## |A|


## Y

p(A | T,Q) = p (a | T,Q,a ) (A.1)
LM i 1:i−1
i=1
Here,thepromptandquestionconditionthepre-trainedLLMp . Thea arepreviouslygenerated

### LM 1:i−1

answertokensandAacompleteanswer.
Templating. The above formalization does not include the notion of maximizing a scoring or utility
function (e.g. accuracy on a dataset), which prompts are often designed to do. Additionally, prompt
engineersoftenseektodesignprompttemplateratherthanprompts. Here,wereformulateeq.(A.1)to
includetheprompttemplate:

## |A|

p(A | T(x∗)) = Y p (a | T(x∗),a ) (A.2)
LM i 1:i−1
i=1
WereplaceQwithx∗ ∈ D ,anitemfromadataset(e.g.,evaluationdata). Additionally,wereplace
eval
QontherightsidewithT(x). T(·)isaprompttemplate: afunctionthatacceptssomeitemasinputthen
returnsapromptthatisusedtoconditionthemodel.
Few-ShotPrompting. Often,animportantpartofthepromptingprocessistheuseoffew-shotexemplars.
D istrainingdata(usedtobuildtheprompt)andX isatestsetforevaluation.
train
D = {(x ,y ),(x ,y ),...,(x ,y )} (A.3)
train 1 1 2 2 n n
X = {x∗,x∗,...,x∗ } (A.4)
1 2 m
In the few-shot setting, the prompt template function T(·) also takes as input one or more training
samplesX = {(x ,y )}n ⊂ D
i i 1 train

## |A|

p (cid:0) A | T (X, x∗) (cid:1) = Y p (a | T (X, x∗),a ) (A.5)
LM i 1:i−1
i=1
Optimization. Asmentioned,itisoftendesirabletospeakaboutimprovingprompts(prompttemplates,
thatis)withrespecttoascoringfunction,usuallydefinedwithrespecttoadataset.
T∗ = argmax E [S(p (A|T(x )),y )] (A.6)
xi,yi∼D LM i i

## T

In this definition, we are evaluating over a dataset D with respect to the scoring function S(·). S(·)
evaluatestheoutputA,generatedbytheLLMconditionedonthepromptT(§ ). y arelabeledoutputs
⟩ i
thatcanbeusedbyS.
Insomecases,theremaynotbeanylabeleddatay ,andS(·)maybereference-free.
i
75

<!-- Page 76 -->

Otherconsiderations. TheseformalismscouldbeadaptedtocatertoCoT,retrievalsystems,andmore.
Herewedescribeasimplesetupwhichismostdescriptiveofthepromptingprocesswithoutaddingtoo
muchcomplexity.
Wealsodrawattentiontothelesserknownconceptofanswerengineering. E(A)isatransformation
functionovertherawLLMoutputthatallowsittobecomparedtothegroundtruth.
A ∼ p (A | T(x ),y ) (A.7)

### LM i i

T∗ = argmax E [S(E(A),y )] (A.8)
xi,yi∼D i

## T,E

76

<!-- Page 77 -->


### A.9 In-ContextLearningDefinitionsDisambiguation

Brownetal.(2020)seeminglyoffertwodifferentdefinitionsforICL.Allboldinginthissectionisour
own.
Recentwork[RWC+19]attemptstodothisviawhatwecall“in-contextlearning”,usingthetext
inputofapretrainedlanguagemodelasaformoftaskspecification: themodelisconditioned
on a natural language instruction and/or a few demonstrations of the task and is then
expectedtocompletefurtherinstancesofthetasksimplybypredictingwhatcomesnext.

### However,theylaterappeartodefineitasfew-shotonly:

Foreachtask,weevaluateGPT-3under3conditions: (a)“few-shotlearning”,orin-context
learning where we allow as many demonstrations as will fit into the model’s context
window(typically10to100),(b)“one-shotlearning”,whereweallowonlyonedemonstration,
and(c)“zero-shot”learning,wherenodemonstrationsareallowedandonlyaninstructionin
naturallanguageisgiventothemodel.
However,theyincludethisimagethatclarifiesthematter:
FigureA.1: ICLfromBrownetal.(2020).
Additionally,theyexplicitlystatethatICLdoesnotnecessarilyinvolvelearningnewtasks.
77

<!-- Page 78 -->

Toavoidthisconfusion,weusetheterm“meta-learning”tocapturetheinner-loop/outer-loop
structureofthegeneralmethod,andtheterm“incontext-learning”torefertotheinnerloop
of meta-learning. We further specialize the description to “zero-shot”, “one-shot”, or “fewshot” depending on how many demonstrations are provided at inference time. These terms
areintendedtoremainagnosticonthequestionofwhetherthemodellearnsnewtasks
fromscratchatinferencetimeorsimplyrecognizespatternsseenduringtraining–this
isanimportantissuewhichwediscusslaterinthepaper, but“meta-learning”isintendedto
encompassbothpossibilities,andsimplydescribestheinner-outerloopstructure.
WeuseBrownetal.(2020)’sbroaddefinition,thoughnotethatpractitionersoftenuseICLtoreferto
situationsinwhichthemodelappearstobelearningnewtasksfromtheprompt. Ourdefinitiondiffers
fromDongetal.(2023)’sformaldefinition,eventhoughitisalsoderivedfrom(Brownetal.,2020).
78

<!-- Page 79 -->


### A.10 Contributions

Thefollowingarethecontributionsmadebytheteammembersinvarioussectionsofthispaper. Most
authorsconductedreviewsofothersectionsaswell.

### Advisors

• DenisPeskoff: Assistedwithpaperorganizationandfinalreview.
• Alexander Hoyle: Provided guidance on writing, meta-analysis approach, and ran automated
baselinesforcasestudy.
• ShyamalAnadkat: Assistedwiththeoverallreviewofthepaperandtheetymologyanddefinitions.
• JulesWhite: Builttreesfortechniquetaxonomies.
• MarineCarpaut: Framed,reviewedandsuggestedpapersforthemultilingualsection.
• PhillipResnik: PrincipalInvestigator

### SCSLabeling

• MeganL.Rogers,InnaGoncearenco,GiuseppeSarli,IgorGalynker: reviewedandgaveadvice
forthissection.

### BenchmarkingandAgents

• KonstantineKahadze: TeamleaderfortheBenchmarkingsection;managedMMLUbenchmarking
codebase,contributedtoSecurityandMetaAnalysis.
• AshaySrivastava: TeamleaderfortheAgentssection,reviewedpapersforhumanreview,worked
onthetooluseagentssection. Workedonthecompilationofcontributions.
• Hevander Da Costa: Contributed to the Benchmarking section and Meta Review datasets list,
reviewed literature on LLM code generation and prompting techniques. Added literature review
contenttotheAgentssection.
• FeileenLi: Workedonthetooluseagentssection,assistedwiththehumanpaperreview.

### AlignmentandSecurity

• Nishant Balepur: Team leader for the alignment section, helped with high-level discussions in
benchmarking,andrevieweddrafts.
• SevienSchulhoff: Teamleaderforthesecuritysectionandcontributedtothebenchmarkingsection.

### RelatedWorksandSectionContributions

• ChengleiSi: Suggestedrelatedworksandeditedsection2.2andsection7.
• PranavSandeepDulepet: Contributeddefinitionsforsection2andworkedonsegmentationand
objectdetectioninthemultimodalsection.
• HyoJungHan: ContributedtotheMultimodalsection,especiallythespeech+textpart,andwrote
theaudiopromptingsection.
• HudsonTao: Authoredsectionsonimage,video,and3Dwithinmultimodal,reviewedpapersfor
humanreview;maintainedGitHubcodebase,andbuilttheprojectwebsite.
• AmandaLiu: Authoredtaxonomicontologysections,conductedbackgroundresearchforintroductionandrelatedwork,developedcodepipelinesformeta-analysisgraphs
79

<!-- Page 80 -->

• SwetaAgrawal: Teamleadforevaluationsection.
• SauravVidyadhara: Assistedwithgeneralreviewandrevisingtaxonomytrees.
• ChauPham: Assistedwithmetareview,includingautomatedanalysisoftopics.

### MultilingualPromptingandMetaAnalysis

• DayeonKi: LedtheMultilingualpromptingsection,conductedreviewonrelatedpapers,andwrote
Section3.1.
• YinhengLi: Workedonsection2.2text-basedtechniques,reviewedtechniques,andcontributedto
draftingfigure2.2.
• SaloniGupta: Wrotetestsforpapercompilation,helpedsetuppaperpipeline,andworkedonthe
codediagramandgrammarforthepaper.
• GersonKroiz: Involvedwithsection1.1anddefiningaprompt.
• AayushGupta: ContributedtotheMetaAnalysis,compilingpapers,andgeneratingvisualization
graphs.
• MichaelIlie: Co-LeadAuthor,managedcodebase,ranexperiments,collecteddata,andhelpedwith
varioussectionsincludingthePRISMAreviewfigureandtheSCSpromptingcasestudy.
• SanderSchulhoff: LeadAuthor
80

## Tables

**Table (Page 10):**

| beautiful: Happy  I am so a: Angry  I love lif re so cute: Happy  I hate m ds Suck: Angry  Life is g ted: I’m so e | mad: Angry  e: Happy  y boss: Angry  ood: Happy  xcited: |
|---|---|
| I love lif Life is g beautiful: Happy  I am so ted: I hate m I’m so e | e: Happy  ood: Happy  mad: Angry  y boss: Angry  xcited: |


**Table (Page 10):**

| ad: Angry  I am so Happy  I love life boss: Angry  I hate m d: Happy  Life is g ited: I’m so ex | mad: Angry  : Happy  y boss: Angry  ood: Happy  cited: |
|---|---|
| ad: Angry  I am so e so dense: Angry  I love life boss: Angry  I hate m d: Happy  Life is g ited: I’m so ex | mad: Happy  : Angry  y boss: Angry  ood: Happy  cited: |


**Table (Page 10):**

| : Happy  Im hype y excited: Angry  Im not v ited: I’m so ex | d!: Happy  ery excited: Angry  cited: |
|---|---|
| nice===Happy  Trees ar ds Suck===Angry  YouTube ited=== I’m so ex | e beautiful: Happy  Ads Suck: Angry  cited: |


**Table (Page 17):**

|  | Count 100 200 300 400 500 0 G PT-3 B RoB G E P E T R -4 T Co |  |  |  |  |  |  |  |  | Counts 100 101 102 103 Few G L o P e H o r a d u o s Z m m t I e n - t p a r - o o C n t S - - - o O P M S e L A - n r h r e l o S o f d u t o v - s h e m e C t t e t o x o r o p l R P t t m n S t P r e E L o s e a r R a e x o i m n t s s e a a i m s c t o t r p m e i r n n p t t i n i e i p i i t v n n n c i v l n i g e g g y t a g y s * * * * l Citation Com I P n l p - a D c l n e e o - x c n P a i o t r t n M e o m y G L d x g - a L r A - B p t T r i S a M e r c a a o L o p e S t u m s s s e i l h e e e e t v v a a i l d d e e c o o o f r s - n f f f S E P P P P P O i e T T T v n r r r r r o o o o o p l h h h a g S f m m m m m - t l o o o e u R i S m u u u l p p p p a e f u g g g - t t t t C t f i A r z i i i h i h h i i v n n n n o n o s e t t t e g g g g n T e k s s s r y s * * * * * * * * * * * Prompting Techniques Counts of Prompting De S Q m U S R e C D t u n e l o e f u e i e p - n f C p A m M s i d h s e S h - t d A u t r u e i d e a S r a a o w c m l a l i a u p s n f D n t T - t a k i e t p t r o - A i G v e i D N i r e o o p v r v e e u a m e e y n e f N e o e - F t n n - - V V V c o o r a E o o d R e P P t o e e e m i f f n R r r r e t m - - r r r E R o o T T h a s i i i e a a x f f f e m e m h h t f p i i i t s t u a e c c c s m r o o e o o p p p a a a m l d i p u u - e s n b t t t C C t t t o i g g v I i i i p i i i i t l n n n n C n o o o o o i h i e h l n o g g n g e n g n d T T L r t t n g s * * * * * * * * * * * * * * Techniques |  |
|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |  |  |
|  | LL P a R L T M a a M |  |  |  |  |  |  | unt |  | Le r a o s m t-t pt O e r lf d - e C r on E s x is a t m e ple g s * |  |
|  | BA A C RT In od |  |  |  |  |  |  | s o |  | o-M Sensit n cy* ost P iv |  |
|  |  |  |  |  |  |  |  |  |  |  |  |
|  | struc ex O P |  |  |  |  |  |  | f |  | Hum Prom rom ity an p pti |  |
|  | tG T B LO P T O |  |  |  |  |  |  | Mo |  | -Level t Retrie n g* P r v |  |
|  |  |  |  |  |  |  |  |  |  |  |  |
|  | FLA M |  |  |  |  |  |  | d |  | Autom om al pt |  |
|  | CN Mod LIP B SA io |  |  |  |  |  |  | el |  | atic in g C Tre Co T |  |
|  | V isi F B L la a m m B i b E d R M a T el Na |  |  |  |  |  |  | Men |  | om plex P r o g ram e o f Th S e lf -A sk * i t y -B o f o u g h * |  |
|  | on Tran C s L f o O o C O o n M O g Z o me |  |  |  |  |  |  | tio |  | ased T h ou t s * Decom P ro m g ht s * p t |  |
|  | rmp B LIP er |  |  |  |  |  |  | ns |  | posed S elf-Ref i ng* P i |  |
|  | C odell -2 V L P |  |  |  |  |  |  | in |  | Self-Ev rom ne* In-c M ai ptin |  |
|  | FinB a m G E a |  |  |  |  |  |  | D |  | ontext eutic aluati g* P |  |
|  | ro und G ato L LaV R T D i r A |  |  |  |  |  |  | at |  | Learnin rom on* Gra ptin P |  |
|  | rea n g T ron m D I |  |  |  |  |  |  | as |  | LL ph of g Sur g* ro |  |
|  | Fus N O io |  |  |  |  |  |  | et |  | M Though vey mpti s Pla as A O |  |
|  | n |  |  |  |  |  |  |  |  | n-and- ctive ptim ts* ng P iz |  |
|  |  |  |  |  |  |  |  |  |  | Solve rom ers Tec pti P |  |
|  |  |  |  |  |  |  |  |  |  | rom ng* hniq S Fai pti |  |
| Figure2.9: CitationCountsofGenAIModels |  |  |  |  |  |  |  |  |  | u pport t hful n g * ues U k E C o T |  |
|  |  |  |  |  |  |  |  |  |  | nified NN xam * P p |  |
|  | Number of Mentions 20 40 60 80 |  |  |  |  |  |  |  |  | Dem rom les o pti |  |
|  | 0 0 0 0 0 |  |  |  |  |  |  |  |  | Tree-of Retriev ng* |  |
|  |  |  |  |  |  |  |  |  |  |  |  |
|  | G SM 8K |  |  |  |  |  |  |  |  | Step-Aw Autom -Thoug er* |  |
|  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  | are ate-C ht* Q Sel Ve |  |
|  | M M LU |  |  |  |  |  |  |  |  | uestio f-Gener rificatio oT* |  |
|  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  | D |  | Deduc n Deco ated n* I |  |
|  | C om B m B H |  |  |  |  |  |  | at |  | Cum tive m posit C L* ul Ve i |  |
|  |  |  |  |  |  |  |  |  |  |  |  |
|  | onse |  |  |  |  |  |  | as |  | ative rificati on Chai S R |  |
|  | nseQ A |  |  |  |  |  |  | et |  | elf-Ada n-of-Ve easonin on* Dem |  |
|  |  |  |  |  |  |  |  |  |  |  |  |
|  | H ella D |  |  |  |  |  |  | M |  | onstra p tive rificatio g* Pr t |  |
|  | Sw ag at |  |  |  |  |  |  | e |  | ion om n* M em En ptin |  |
|  | B ase IG -b |  |  |  |  |  |  | nti |  | Rephras ory-of- sem g* bli |  |
|  | ench t W N |  |  |  |  |  |  | o |  | e Thoug ng and |  |
|  | inoG am r |  |  |  |  |  |  | ns |  | Respon ht* |  |
|  | ande e |  |  |  |  |  |  | in |  | d* |  |
|  | Q Papers A SC A Q U A -RAT TruthfulQ A |  |  |  |  |  |  |  |  |  |  |


**Table (Page 33):**

|  |
|---|
| 0.627 |


**Table (Page 33):**

|  |
|---|
| 0.652 |


**Table (Page 33):**

|  |
|---|
| 0.692 |


**Table (Page 33):**

|  |
|---|
| 0.691 |


**Table (Page 33):**

|  |
|---|
| 0.547 |


**Table (Page 36):**

|  |  |  |
|---|---|---|
|  |  |  |
|  |  |  |


**Table (Page 36):**

|  |  |  |
|---|---|---|
|  |  |  |
|  |  |  |


**Table (Page 36):**

|  |  |  |
|---|---|---|
|  |  |  |
|  |  |  |


**Table (Page 36):**

|  |  |  |
|---|---|---|
|  |  |  |
|  |  |  |


**Table (Page 36):**

|  |  |  |
|---|---|---|
|  |  |  |
|  |  |  |


**Table (Page 36):**

|  |  |  |
|---|---|---|
|  |  |  |
|  |  |  |


**Table (Page 36):**

|  |  |  |
|---|---|---|
|  |  |  |
|  |  |  |


**Table (Page 36):**

|  |  |  |
|---|---|---|
|  |  |  |
|  |  |  |


**Table (Page 36):**

|  |  |  |
|---|---|---|
|  |  |  |
|  |  |  |


**Table (Page 36):**

|  |  |  |
|---|---|---|
|  |  |  |
|  |  |  |


**Table (Page 36):**

|  |  |  |
|---|---|---|
|  |  |  |
|  |  |  |


**Table (Page 36):**

|  |  |  |
|---|---|---|
|  |  |  |
|  |  |  |


**Table (Page 36):**

|  |  |  |
|---|---|---|
|  |  |  |
|  |  |  |


**Table (Page 36):**

|  |  |  |
|---|---|---|
|  |  |  |
|  |  |  |


**Table (Page 36):**

|  |  |  |
|---|---|---|
|  |  |  |
|  |  |  |


**Table (Page 36):**

|  |  |  |
|---|---|---|
|  |  |  |
|  |  |  |


**Table (Page 36):**

|  |  |  |
|---|---|---|
|  |  |  |
|  |  |  |


**Table (Page 36):**

|  |  |  |
|---|---|---|
|  |  |  |
|  |  |  |


**Table (Page 37):**

|  |  |  |
|---|---|---|
|  |  | Max F1 Score: 0.53 |


**Table (Page 37):**

|  |
|---|
| Max F1 Score: 0.53 |


**Table (Page 37):**

|  |  |
|---|---|
|  |  |


**Table (Page 42):**

|  |  |  |
|---|---|---|
|  |  |  |
|  |  |  |


**Table (Page 42):**

|  |  |  |
|---|---|---|
|  |  |  |
|  |  |  |


**Table (Page 42):**

|  |  |  |
|---|---|---|
|  |  |  |
|  |  |  |


**Table (Page 42):**

|  |  |  |
|---|---|---|
|  |  |  |
|  |  |  |


**Table (Page 62):**

| Reference | Prompt | PromptEngineering |
|---|---|---|
| (Meskó, 2023) |  | The practice of designing, refining, and implementingpromptsorinstructionsthat guidetheoutputofLLMstohelpinvari- oustasks. Itisessentiallythepracticeof effectivelyinteractingwithAIsystemsto optimizetheirbenefits. |
| (Chen et al., 2023a) | theinputofthemodel | the process of structuring input text for LLMsandisatechniqueintegraltoopti- mizingtheefficacyofLLMs |
| (Santu and Feng,2023) | refers to a textual input provided to the LLMs with the intention of guiding its outputtowardaspecifictask | involves crafting and revising the query orcontextinsuchawaythatitelicitsthe desiredresponseorbehaviorfromLLMs |
| (Wang et al., 2023d) |  | involves designing effective prompts to guide the pre-trained language model in downstreamtasks. |
| (Wang et al., 2023c) |  | theprocessofdesigningpromptsthaten- ablethemodeltoadaptandgeneralizeto differenttasks. downstreamtasks. |
| (Hou et al., 2023) | manuallypredefinednaturallanguagein- structions | thecarefuldesignofspecializedprompts |
| (Wang et al., 2023e) | inputoftheLLMs | communicate with LLMs to steer its be- haviorfordesiredoutcomes |
| (Whiteetal., 2023) | Instructions given to an LLM to enforce rules,automateprocesses,andensurespe- cificqualities(andquantities)ofgenerated output. Prompts are also a form of pro- grammingthatcancustomizetheoutputs andinteractionswithanLLM. Apromptisasetofinstructionsprovided toanLLMthatprogramstheLLMbycus- tomizingitand/oren-hancingorrefining itscapabilities | anincreasinglyimportantskillsetneeded to converse effectively with large lan- guagemodels(LLMs),suchasChatGPT the means by which LLMs are pro- grammedviaprompts |
| (Heston and Khun,2023) | theinput | structuringtheinputinaspecializedman- ner |
| (Liu et al., 2023b) |  | choosingaproperprompt theprocessofcreatingapromptingfunc- tion f (x) that results in the most prompt effectiveperformanceonthedownstream task. |


**Table (Page 63):**

| (Hadi et al., 2023) | the instructions provided to an LLM to makeitfollowspecifiedrules,automation of processes and to ensure that the out- put generated is of a specific quality or quantity | refers to the designing and wording of promptsgiventoLLMssoastogetade- siredresponsefromthem. |
|---|---|---|
| (Neagu, 2023) |  | entails various strate- gies, including ex- plicitinstruction,andimplicitcontext[21]. Explicitinstructioninvolvesprovidingex- plicitguidanceorconstraintstothemodel throughinstructions,examples,orspeci- fications. Implicit context leverages the model’sunder-standingofthepreceding contexttoinfluenceitsresponse |
| (Dang et al., 2022) |  | the systematic practice of constructing promptstoimprovethegeneratedoutput ofagenerativemodel |
