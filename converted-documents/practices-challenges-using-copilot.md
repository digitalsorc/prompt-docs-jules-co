---
title: "Practices Challenges Using Copilot"
original_file: "./Practices_Challenges_Using_Copilot.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["llm", "rag", "react", "fine-tuning", "evaluation"]
keywords: ["copilot", "github", "code", "data", "used", "programming", "developers", "discussions", "results", "challenges"]
summary: "<!-- Page 1 -->

Practices and Challenges of Using GitHub Copilot:

### An Empirical Study

Beiqi Zhang†‡, Peng Liang†‡∗, Xiyu Zhou†‡, Aakash Ahmad§, Muhammad Waseem†‡
†School of Computer Science, Wuhan University, Wuhan, China
‡Hubei Luojia Laboratory, Wuhan, China
§School of Computing and Communications, Lancaster University Leipzig, Leipzig, Germany
{zhangbeiqi, liangp, xiyuzhou, m.waseem}whu.edu.cn, a.ahmad13@lancaster.ac.uk
Abstract—With the advances in machine learning, there is a [3]. Rel"
related_documents: []
---

# Practices Challenges Using Copilot

<!-- Page 1 -->

Practices and Challenges of Using GitHub Copilot:

### An Empirical Study

Beiqi Zhang†‡, Peng Liang†‡∗, Xiyu Zhou†‡, Aakash Ahmad§, Muhammad Waseem†‡
†School of Computer Science, Wuhan University, Wuhan, China
‡Hubei Luojia Laboratory, Wuhan, China
§School of Computing and Communications, Lancaster University Leipzig, Leipzig, Germany
{zhangbeiqi, liangp, xiyuzhou, m.waseem}whu.edu.cn, a.ahmad13@lancaster.ac.uk
Abstract—With the advances in machine learning, there is a [3]. Released on June 2021, GitHub Copilot has recently
growing interest in AI-enabled tools for autocompleting source emerged as an “AI pair programmer”, which is powered
code.GitHubCopilot,alsoreferredtoasthe“AIPairProgramby OpenAI Codex and suggests code or entire functions in
mer”,hasbeentrainedonbillionsoflinesofopensourceGitHub
IDEs as a plug-in [4] to help developers achieve code autocode,andisoneofsuchtoolsthathasbeenincreasinglyusedsince
its launch in June 2021. However, little effort has been devoted completion in programming activities.
to understanding the practices and challenges of using Copilot Although the emergence of AI-assisted programming tools
in programming with auto-completed source code. To this end, has empowered practitioners in their software development
weconductedanempiricalstudybycollectingandanalyzingthe
efforts, there is little evidence and lack of empirically-rooted
data from Stack Overflow (SO) and GitHub Discussions. More
studies (e.g, [3], [5], [6]) on the role of AI-assisted programspecifically, we searched and manually collected 169 SO posts
and 655 GitHub discussions related to the usage of Copilot. ming tools in software development. The existing studies pri-
We identified the programming languages, IDEs, technologies marilyfocusonthecorrectnessandunderstandingofthecode
used with Copilot, functions implemented, benefits, limitations, suggested by Copilot, and little is known about the practices
and challenges when using Copilot. The results show that when
and challenges of using Copilot with programming activities.
practitionersuseCopilot:(1)Themajorprogramminglanguages
To close the gap, we conducted this study that collects data
used with Copilot are JavaScript and Python, (2) the main IDE
used with Copilot is Visual Studio Code, (3) the most common from Stack Overflow (SO) and GitHub Discussions to get
used technology with Copilot is Node.js, (4) the leading function practitioners’ perspectives on using Copilot during software
implemented by Copilot is data processing, (5) the significant engineering and development.
benefit of using Copilot is useful code generation, and (6) the

### The contributions of this work: (1) we identified the

mainlimitationencounteredbypractitionerswhenusingCopilot
programming languages, IDEs, and technologies used with
isdifficultyofintegration.OurresultssuggestthatusingCopilotis
likeadouble-edgedsword,whichrequiresdeveloperstocarefully Copilot; (2) we provided the functions implemented by Copiconsider various aspects when deciding whether or not to use lot, the benefits, limitations, and challenges of using Copilot;
it. Our study provides empirically grounded foundations and and (3) we present the directions to be further explored.
basis for future research on the role of Copilot as an AI pair
programmer in software development.
Keywords—GitHub Copilot, Stack Overflow, GitHub Discus- II. RELATEDWORK
sions, Empirical Study
Several studies focused on the security issues of Copilot.
Sandoval et al. [7] conducted a user study to investigate

## I. Introduction

the impact of programming with LLMs that support Copilot.

### Large Language Models (LLMs) and Machine Learning

Their results show that LLMs have a positive impact on the
(ML) for autocompleting source code are becoming more and
correctness of functions, and they did not find any decisive
morepopularinsoftwaredevelopment.LLMsnowadaysincorimpact on the correctness of safety. Several studies focused
porate powerful capabilities for Natural Language Processing
on the quality of the code generated by Copilot. Imai [8]
(NLP) [1], and ML approaches have been widely applied to
compared the effectiveness of programming with Copilot
source code text in a variety of new tools to support software
versushumanprogramming,andfoundthatthegeneratedcode
development [2], which makes it possible to use LLMs to
byCopilotisinferiorthanhuman-writtencode.Yetistirenetal.
synthesize code in general-purpose languages [1]. Recently,
[9] assessed the quality of generated code by Copilot in terms

### NLP-basedcodegenerationtoolshavecomeintothelimelight,

ofvalidity,correctness,andefficiency.Theirempiricalanalysis
with generative pre-trained language models trained on large
shows Copilot is a promising tool. Madi et al. [6] focused
amounts of code in an attempt to provide reasonable autoon readability and visual inspection of Copilot generated
completion of the source code when programmers write code
code. Through a human experiment, their study highlights
that programmers should beware of the code generated by

### ThisworkisfundedbytheNSFCwithGrantNo.62172311andtheSpecial

tools. Wang et al. [10] collected practitioners’ expectations
FundofHubeiLuojiaLaboratory.
DOIreferencenumber:10.18293/SEKE2023-077 on code generation tools through a mixed-methods approach.
3202
rpA
72
]ES.sc[
3v33780.3032:viXra

<!-- Page 2 -->


### TABLE I: Research Questions and their Rationales

Theyfoundthateffectivenessandcodequalityismoreimportant than other expectations. Several studies focused on the ResearchQuestion Rationale
limitations and challenges in Copilot assisted programming. RQ1: What program- Copilot can help practitioners write less code. This
minglanguagesareused RQ aims to collect the programming languages that
Dakheletal.[11]exploredthecapabilitiesofCopilotthrough withGitHubCopilot? developerstendtousewithCopilot.
empirical evaluations, and their results suggest that Copilot RQ2: What IDEs are Copilotisathird-partyplug-inusedinIDEs.ThisRQ
usedwithGitHubCopi- aimstoidentifytheIDEsfrequentlyusedwithCopilot.
shows limitations as an assistant for developers. Nguyen and
lot? The answers of this RQ can help developers choose
Nadi[12]conductedanempiricalstudytoevaluatethecorrect- whichIDEtousewhentheycodewithCopilot.
RQ3:Whattechnologies Whenwritingcode,programmersneedtoemploycerness and comprehensibility of the code suggested by Copilot.
are used with GitHub taintechnologiestocompletethedevelopment.ThisRQ
TheirfindingsrevealedthatCopilot’ssuggestionsfordifferent Copilot? aims to investigate the technologies that can be used
with Copilot (e.g., frameworks), and the answers of
programming languages do not differ significantly, and they
thisRQcanhelpdeveloperstochoosethetechnologies
identified potential shortcomings of Copilot, like generating whentheyuseCopilot.
RQ4:Whatfunctionsare Copilot can complete entire functions according to
complex code. Bird et al. [5] conducted three studies to
implemented by using users’ comments. This RQ aims to provide a cateunderstand how developers use Copilot and their findings GitHubCopilot? gorization of the functions that can be implemented
by Copilot, and the answers of this RQ can provide
indicated that developers spent more time assessing Copilot’s
developers guidance when implementing functions by
suggestions than doing the task by themselves. Sarkar et usingCopilot.
RQ5:Whataretheben- Using Copilot to assist programming can bring many
al. [13] compared programming with Copilot to previous
efits of using GitHub benefits (e.g., reducing the workload of developers).
conceptualizations of programmer assistance to examine their Copilot? ThisRQaimstocollecttheadvantagesbroughttothe
developmentbyapplyingCopilot.
similaritiesanddifferences,anddiscussedtheissuesthatmight
RQ6:Whatarethelimi- Although using Copilot to assist in writing code can
arise in applying LLMs to programming. tationsandchallengesof helpdeveloperswiththeirprogrammingactivities,there
usingGitHubCopilot? arestillrestrictionsandproblemswhenusingCopilot.
Compared to the existing work (e.g., [9], [11]), our work

### This RQ aims to collect and identify the limitations

intends to understand the practices and challenges of Copilot andchallengespractitionersmayexperiencewhenusing

### Copilot.TheanswersofthisRQcanhelppractitioners

by exploring the programming languages, IDEs, technologies
makeaninformeddecisionwhendecidingwhetherto
used with Copilot, functions implemented by Copilot, and the codewiththehelpofCopilot.
benefits, limitations, and challenges of using Copilot.

## Iii. Researchdesign

A. Research Questions community knowledge base connected with other artifacts in
The Research Questions (RQs) and their rationale are pre- a project [14]. Therefore, we decided to use SO and GitHub
sented in Table I. The overview of the research process is Discussions as the data sources to answer our RQs, and we
shown in Figure 1 and detailed below. conducted the searches for both SO and GitHub Discussions
on November 23rd, 2022.
RQ1 RQ3 [D1~D6: Data Items] For SO, “copilot” is used as the term to search the posts
Programming Development Data Extraction Template relatedtoCopilot.Aftersearching,wegotatotalof557posts

### RQ4 Languages Technologies RQ6 "copilot"

that include the search term “copilot”. The term “copilot”
Implemented Specify Research Limitations Data Collection Data Extraction may appears more than once in a post, so there may be

### Functions Questions and Filtering and Analysis

Integrated Development Benefits [RQ1~RQ3] [RQ4~RQ6] duplicatesintheURLcollectionoftheseretrievedposts.After
RQ2 Environments RQ5 removing the duplicates, we ended up with 521 posts with
[655 d G is it c H u u s b sions] St [ a 1 c 6 k 9 O p v o e s r t f s lo ] w D S e t s a c ti r s ip ti t c iv s e Co C m on p s a t r a is n o t n unique URLs. To manually label posts related to Copilot,
Phase A Phase B Phase C we conducted a pilot data labelling by two authors with 10
retrieved SO posts. Specifically, the inclusion criterion is that

### Fig. 1: Overview of the research process

the post must provide information referring to Copilot. We
calculated the Cohen’s Kappa coefficient [15] to measure the
B. Data Collection and Filtering consistency of labelled posts, which is 0.773, thus indicating
a decent agreement between the two coders. After excluding

### This study focuses on understanding the practices and

the irrelevant posts in the search results, we finally got 169
challenges of using Copilot collected from SO and GitHub
Copilot related SO posts.
Discussions. SO is a popular software development community and has been widely used by developers to ask and ForGitHubDiscussions,GitHubdiscussionsareorganized
answer questions as a Q&A platform. GitHub Discussions according to categories. After exploring the categories on
is a feature of GitHub used to support the communication GitHub Discussions, we found the “Copilot” category which
among the members of a project. Different from SO, GitHub contains the feedback, questions, and conversations about
Discussionscanprovidevariouscommunicationintentions,not Copilot [16] under the “GitHub product categories”. Since
justquestion-answering(e.g.,adiscussioncanreporterrorsor all the discussions under the “Copilot” category are related
discuss the potential development of a software project) [14], to Copilot, we then included all the discussions under the
from which the data can be complementary to the data from “Copilot” category as related discussions to extract data. The
SO. Besides, GitHub Discussions can provide a center of a number of discussions related to Copilot is 655.

<!-- Page 3 -->

C. Data Extraction and Analysis authorsreachedanagreement.Thedataanalysismethodswith
1) Extract Data: To answer the RQs in Section III-A, we their corresponding data items and RQs are listed in Table II.
The data analysis results are provided in [20].
extracted the data items listed in Table II. The first and third
authors conducted a pilot data extraction independently with
10 SO posts and 10 GitHub discussions randomly selected IV. RESULTS
from the 169 SO posts and 655 GitHub discussions. The
This section presents the results of the study, in which the
second author was involved to discuss with the two authors
results of RQ1 to RQ4 are visualized in Fig 2, and the results
and came to an agreement if any disagreements were found
of RQ5 and RQ6 are provided in Table III and IV.
duringthepilot.Afterthepilot,thecriteriafordataextraction

### RQ1: Programming languages used with GitHub Copilot

were determined: (1) for all the data items listed in Table II,

### Figure 2a lists the 18 programming languages used with

they will be extracted and counted only if they are explicitly
Copilot, in which JavaScript and Python are the most frementioned by developers that they were used with Copilot;
quently used ones, both accounting for one fifth. Besides,
(2) if the same developer repeatedly mentioned the same data
developers often write C# and Java code when using Copilot,
item in an SO post or a GitHub discussion, we only counted
as one practitioner mentioned “the GitHub Copilot extension
it once. In a post or discussion, multiple developers may
is enabled in my VS 2022 C# environment” (GitHub #14115).
mention Copilot related data items, resulting in situation that

### TypeScript, Rust, PHP, C, Golang, and Kotlin were used with

the total number of instances of certain data item extracted

### Copilot between 3˜8 times each (1.7% to 8.4%). The rest

may be greater than the number of posts and discussions. The
programming languages (e.g., Perl and Ruby), which are not
first and third authors further extracted the data items from
popular, were mentioned only once with Copilot.
the filtered posts and discussions according to the extraction

### RQ2: IDEs used with GitHub Copilot

criteria,markeduncertainparts,anddiscussedwiththesecond
Figure 2b shows 22 types of IDEs that are used with Copilot.
authortoreachaconsensus.Finally,thefirstauthorrechecked
VisualStudioCodeisthedominantIDE,accountingfor46.0%.
all the extraction results by the two authors from the filtered
When first released, Copilot only worked with Visual Studio
postsanddiscussionstoensurethecorrectnessoftheextracted
Code editor, and it is expected that Visual Studio Code is the
data.

### IDE most often used with Copilot. Mainstream code editors,

TABLEII:DataitemsextractedwiththeircorrespondingRQs includingVisualStudio,IntelliJIDEA,NeoVim,andPyCharm
and analysis methods are also occasionally used, account for 39.9% in total. The
remainingIDEswererarelymentionedbydevelopers,andone
# DataItem Description Analysis RQ
Method possible reason is that there are often integration issues when
D1 Programming Programming language used Descriptive RQ1 using Copilot within them according to the results of RQ6.
language withCopilot statistics[17]
D2 IDE IDEsusedwithCopilot Descriptive RQ2 RQ3: Technologies used with GitHub Copilot
statistics Figure2cpresents22technologiesusedwithCopilot.Wefind

### D3 Technology TechnologiesusedwithCopilot Descriptive RQ3

statistics that these identified technologies include frameworks, APIs,
D4 Function Functions implemented by Constant RQ4 and libraries. Node.js, whose proportion is more than 40%, is

### Copilot comparison

D5 Benefit BenefitsbroughtbyusingCopi- Constant RQ5 one of the most popular back-end runtime environments for
lot comparison JavaScript, which is also the most frequently used language
D6 Limitation and The restrictions and difficulties Constant RQ6
Challenge whenusingCopilot comparison withCopilot(seetheresultsofRQ1),thusitisreasonablethat

### Node.jsisthemajortechnologyusedwithCopilot.Inaddition,

2) Analyze Data: For RQ1, RQ2, and RQ3, we used .NET which works for Web development, and Vue, React,
descriptive statistics [17] to analyze and present the results. and Ajax which are frameworks for front-end development,
For RQ4, RQ5, and RQ6, we conducted a qualitative data were mentioned less often compared to Node.js. The rest of
analysis by applying the Constant Comparison method [18]. the identified technologies, many of which relate to machine
We constantly compared each part of the data (e.g., emergent learning(e.g.,Pandas,Dlib,andOpenCV)orfront-enddevelcodes) to explore differences and similarities in the extracted opment (e.g., Htmx, Vanilla JS, and Next.js), are rarely used
data to form categories [19]. Note that for answering RQ4, with Copilot, and each of them appears only once.
wecategorizedthefunctions(D4)basedondevelopers’discus- RQ4: Functions implemented by using GitHub Copilot
sions,i.e.,developers’descriptionsofthementionedfunctions. Figure 2d shows 14 functions implemented by using Copilot.
Firstly, the first and the third authors coded the filtered posts ThemainfunctionimplementedbyCopilotisdataprocessing,
and discussions with the corresponding data items listed (see indicating that developers tend to make use of Copilot to
Table II). Secondly, the first author reviewed the coded data writefunctionsworkingwithdata.Besides,Front-endelement
bythethirdauthortomakesuretheextracteddatawerecoded control, string processing, and Test account for the same,
correctly. Finally, the first author combined all the codes into i.e., 11.1%. When implementing functions, developers also
higher-level concepts and turned them into categories. After use Copilot to code image processing, algorithm, iteration,
that,thesecondauthorexaminedthecodingandcategorization calculation,filtering,printing,memoryread,serialization,and
results, in which any divergence was discussed till the three URL building, which range from 2.2% to 8.9%.

<!-- Page 4 -->


### Android Studio

(0.9%) CLionJupyter Notebook
R( R 0. u 6 b % y ) (3 R . u 4 s % t ) Ty ( p 4 e .5 S C % cr ) ipt VSCodium (1.3%) G (1 o . L 3 a % n ) d (1 V .1 im %) (0.9%) (0.9%) E R E c m u l b i a p y c s M s e i ( n 0 ( e 0 .2 . ( 2 % 0 % . ) 2 ) %)
(0.6%) (2.8%) C# WebSt R o i r d m er (1.5%) C N o V d A e c -O ce S s S s ( ( 0 0 . . 2 2 % % ) )

### Python (12.8%) (2.0%) Sublime Text (0.2%)

(20.1%) Python JavaScript Ph ( p 2 S .6 t % or ) m Visual Studio Code G Da o t o a g S l p e e C ll o ( l 0 a . b 2 % (0 ) .2%)
P P N H e i P m rl ( ( ( 2 0 0 . . 8 . 6 6 % % % ) ) ) C++JavaC# (8 C .4 + % + ) Py (8 C . h 5 a % N r ) m eo Vim PyChar N m e I o n V V te i i s m ll u ij a I l D S E tu A dio Vis ( u 4 C a 6 o l . 0 S d % e tu ) dio Lua K ( o 0 t . l 6 in %) （% 8. ） 411 m .2 o 1 s 2 t .8 u 2 s 0 e . d 120.7 (8.8%) 8.58.89.912.746.0
(1.7%) (top 5) HTML+CSS IntelliJ IDEA
(6.1%) (9.9%)
JavaScript Java Visual Studio
(20.7%) (11.2%) (12.7%)
(a) RQ1: Programming Languages (b) RQ2: Integreted Development Environments
gnissecorp
egamI tseT 8.911.111.1 11.126.7
gnissecorp
gnirtS
gnissecorp
ataD
Data processing
(26.7%)
most implemented (top 5)
lortnoc
tnemele
dne-tnorF
most used Dart (top 5) (0.6%) Golang （%） (2.2%)

### Vanilla JS URL building Algorithm

Three.js (1.7%) Text processing (2.2%) (6.7%)
Spring (1.7%) Vue (6.7%) (4.4%) Calculation
Framework (1.7%) .Net (15.0%) (4.4%)

### React (5.0%) Test (11.1%)


### PyTorch (1.7%) Node.js Ajax (3.3%)

Pandas Data build tool (1.7%)String processing (1.7%) most used Dlib (1.7%) (11.1%)

### OpenCV (top 5) Doom (1.7%)

(1.7%) .Net Flutter (1.7%) Serialization AjaxReact Vue g G R ra P p C h Q (1 L .7 ( % 1. ) 7%) (2.2%) （%）
N (4 o 1 d .7 e % .js ) （%） 3.35.06.715.041.7 Ne M x L o t i . n J b js g i T H n o ( o j 1 t D a r m . c 7 B ( h x % 1 ( . ( ( 1 7 ) 1 1 . % . . 7 7 7 % ) % % ) ) ) Mem P ( ( 2 o r 2 . i r . 2 n 2 y % t % i r n ) e ) g ad F ( i 2 lt . e 2 r % in ) g

### Iteration (4.4%)

Image processing Front-end element control
(8.9%) (11.1%)
(c) RQ3: Development Technologies (d) RQ4: Implemented Functions
Fig. 2: Programming languages, IDEs, technologies, and implemented functions of using Copilot (results of RQ1 to RQ4)
TABLE III: Benefits of using Copilot (results of RQ5)

### Benefit Example Count %

Usefulcodegeneration Ifindmyselfwritingalotoftests,andCopilotisexcellentathelpingwithwritingrepetitivetests(GitHub#9282) 24 49.0%
Fasterdevelopment Ireallyenjoyusingit,itreduceprogrammingtime(GitHub#17382) 8 16.3%
Bettercodequality it’sfasterandsimplertoyoursolution(SO#68418725) 5 10.2%
Good adaptation to users’ code GitHubcopilotadapttoyourcodingpractices(SO#69740880) 3 6.1%
patterns
Betteruserexperience Sincecopilotworkstotallydifferentcomparedtoalltheotherproductsoutthere,itisalotmorefuntouseanddoes 3 6.1%
notannoymelikesomeotherAIsystems(GitHub#7254)
Powerfulcodeinterpretationand DoesCopilothavethecodeexplanationfeatureorsomethingsimilar?Itdoes!someactivemembersweregivenbeta 2 4.1%
conversionfunctions access.(GitHub#38089)
Frequent updates to provide Keepinmindthatthereareupdatestothepluginveryfrequently,sothere’sstillhope(SO#70428218) 1 2.0%
morefeatures
Freeforstudents IfyouareastudentyoucansignupfortheGitHubStudentPack,whichgivesalotofbenefits,onebeingcopilotfor 1 2.0%
free(GitHub#31494)
Strongintegrationcapability GitHubissupportingmoreeditors(GitHub#6858) 1 2.0%
Easeofstudyanduse whenusingthisplugin,canstudyatarelativelylowcost(GitHub#8028) 1 2.0%
RQ5: Benefits of using GitHub Copilot than other AI-assisted programming tools, for example, one
Table III highlights 10 benefits of using Copilot. Most de- developerstatedthat“Copilotworkstotallydifferentcompared
velopers mentioned that they used Copilot for useful code to all the other products out there, it is a lot more fun to use
generation, which reduced their workload and gave them help and does not annoy me like some other AI systems” (GitHub
whentheyhavenoideaabouthowtowritecode.Programming #7254), without providing the names of the other products.
withCopilotalsobringsfasterdevelopment,asonediscussion RQ6: Limitations and challenges of using GitHub Copilot
remarked, Copilot “saves developers a lot of time” (GitHub Table IV lists 15 limitations and challenges of using Copilot.
# 35850). Meanwhile, better code quality can be obtained by Most developers pointed out the difficulty of integration beusing Copilot. Compared to the code written by developers tween Copilot and IDEs or other plug-ins. After Copilot was
themselves, the code suggested by Copilot is usually shorter installed in developers’ IDEs, certain plug-ins did not work
and more correct, as one developer said, “often Copilot is and Copilot may conflict with some shortcut settings of the
smarter than me” (SO #74512186). Copilot can use machine editors. Moreover, Copilot cannot be successfully integrated
learningmodelstolearncodestyleofdevelopers,soastooffer with some IDEs as Copilot does not support these editors
good adaptation to users’ code patterns. Three developers yet. Due to the instability of Copilot servers, developers may
mentioned that Copilot can give them better user experience have difficulties of accessing Copilot. The code suggested by

<!-- Page 5 -->

TABLE IV: Limitations and challenges of using Copilot (results of RQ6)

### Limitation&Challenge Example Count %

Difficultyofintegration CopilotonlyworkswithVSCode,VSCodiumisnotsupportedatthemoment(GitHub#14837) 75 28.0%
Difficulty of accessing Copi- I cannot connect to the GitHub account and the Copilot server in VSCode, also cannot use the Copilot plugin (SO 47 17.5%
lot #74398521)
Limitationtocodegeneration Copilotislimitedtoaround1000charactersintheresponse(GitHub#15122) 39 14.6%
Poor quality of generated GithubCopilotsuggestsolutionsthatdon’twork(SO#73701039) 31 11.6%
code
Codeprivacythreat Copilotdoescollectpersonaldatasojusttakeprecautionwhenworkinginprivaterepos(GitHub#7163) 20 7.5%
Unfriendlyuserexperience Ihadthesameproblemtoday,anamazingtoolwithpooruserexperience(GitHub#8468) 14 5.2%
Highpricing itisobviousthatnooneinSouthAmericawillpaythatprice,itistooexpensive(GitHub#24594) 11 4.1%
Difficulty of understanding Ireallydonotunderstandthisenough,andhavenoideahalfofwhatthiscodedoeshonestly.ItwaswrittenbyCopilot. 9 3.4%
thegeneratedcode (SO#72282605)
Noeditionfororganizations Currently,Copilotisonlyavailableforindividualuseraccountsandorganizationsaren’tabletopurchase/manageCopilot 7 2.7%
fortheirmembersjustyet(GitHub#32775)
Lackofcustomization MyquestionisaboutsettingupshortcutsinVisualStudioCodeVSCodeforGitHubCopilotLabs.(SO#73564811) 5 1.9%
Difficultyofsubscription Mycopilotsubscriptionsuddenlystopped.Triedlogoutandin.Neverhavereplyonsupportticketover10days(GitHub 3 1.1%
# 36190)
Challenge of not providing makingsurethatthetooldoesnotprovideoutdatedsuggestionswouldstillbeachallenge(SO#72554382) 2 0.7%
outdatedsuggestions
Showloading I am not sure what is causing this but while editing files within Visual Studio, I am periodically locking up with the 2 0.7%
followingdialogshowing(SO#73682137)
Hardtoconfigure Keepgetting”YourCopilotexperienceisnotfullyconfigured,completeyoursetup”inVisualStudio2022(GitHub#19556) 2 0.7%
Need of basic programming Itisuselessifyoudonotunderstandtheprogramminglanguageorthetaskyouwanttodo(GitHub#35850) 1 0.4%
knowledge
Copilot has restrictions as well, and sometimes it just offers Besides, Copilot may consider improving the integration of
few solutions, which are not enough for users, which brings Copilot by supporting more IDEs in the future.
limitation to code generation, as one developer said “multiple Support for Front-end and Machine Learning Developsolutionistoolittle”(GitHub#37304).Practitionersalsocom- ment:AswecanseefromtheresultsofRQ1,RQ3,andRQ4,
plained about the poor quality of generated code by Copilot. practitioners often write JavaScript and Python code when
Somepractitionerssaidthat“GitHubCopilotsuggestsolutions usingCopilot,andtheytendtouseCopilotwithfront-endand
that don’t work” (SO #73701039), and some practitioners machine learning related technologies (including frameworks,
foundthatwhenthecodefilesbecamelarger,thequalityofthe APIs, and libraries) to implement front-end (e.g., front-end
code suggested by Copilot “becomes unacceptable” (GitHub element control) and machine learning functions (e.g., data
# 9282). When using Copilot, developers pay much attention processingandimageprocessing).JavaScriptisthefoundation
tocodeprivacythreataswell.TheywereworriedthatCopilot language of many popular front-end frameworks and most of
may use their code information without permission. Contrary Websites use JavaScript on the client side. Python is the first
to the developers who mentioned that Copilot gave them a choicewhenitcomestothedevelopmentofmachinelearning
better user experience than other AI-assisted programming solutions with the help of rich libraries, e.g., OpenCV. It is
tools, some practitioners said they had an unfriendly user consequently reasonable that developers tend to use Copilot
experience when coding with Copilot. with JavaScript to facilitate and generate code for front-end
and Python for machine learning development.

## V. Implications


### Potentials and Perils of Using Copilot in Software

IntegrationofCopilotwithIDEs:Accordingtotheresults Development: Trained on billions of lines of code, Copilot
of RQ2 and RQ6, we found that most developers choose to can turn natural language prompts into coding suggestions
integrate the Copilot plug-in in mainstream IDEs (including acrossdozensofprogramminglanguagesandmakedevelopers
Visual Studio Code, Visual Studio, IntelliJ IDEA, NeoVim, code faster and easier [4]. The results of RQ5 and RQ6 show
and PyCharm), and the percentage of mainstream IDEs used that many benefits of using Copilot contradict its limitations
withCopilotbypractitionersreaches85.9%.Whendevelopers and challenges, e.g., useful code generation vs. limitation to
choose the lesser known IDEs (e.g., Sublime Text), they often code generation. When deciding to use Copilot, developers
find it hard to integrate the Copilot plug-in and thus have shouldconsidertoolintegration,userexperience,budget,code
difficulty of integration. In addition to the reason that devel- privacy, and some other aspects, and make trade-offs between
opers may install Copilot in their chosen IDEs incorrectly, these factors. In short, using Copilot is like a double-edged
another reason for the difficulty of integration is that Copilot sword, and practitioners need to consider various aspects
doesnotsupportcertainIDEsatthemoment.Whendevelopers carefullywhendecidingwhetherornottouseit.IfCopilotcan
choose to use Copilot in mainstream IDEs, they can install it be used with appropriate programming languages and techsmoothly, and even if problems arise during the installation nologiestoimplementfunctionsrequiredbyuserscorrectlyin
or use, they can easily find a solution on SO or GitHub developers’IDEs,itwillcertainlyoptimizedevelopers’coding
Discussions as many other developers may have encountered workflow and do what matters most - building software by
similar issues. To reduce the difficulty of integration, we letting AI do the redundant work. Otherwise, it will bring
recommendpractitionerstousemainstreamIDEswithCopilot. difficultiesandrestrictionstodevelopment,makingdevelopers

<!-- Page 6 -->

feel frustrated and constrained. The study results can help GitHub Discussions. Finally, we got 169 SO posts and 655
practitioners being aware of the potential advantages and GitHub discussions related to Copilot. Our results identified
disadvantages of using Copilot and thus make an informed the programming languages, IDEs, technologies used with
decision whether to use it for programming activities. Copilot, functions implemented by Copilot, and the benefits,
TowardsanEffectiveUseofCopilot:Furtherinvestigation limitations, and challenges of using Copilot, which are firstabout the practices of Copilot can be conducted by question- hand information for developers.
naire and interview. Under what conditions the challenges of In the next step, we plan to further explore when to use
using Copilot will show up as advantages or disadvantages, Copilot,forwhatspecificpurposes,andbywhom,whichhelps
and how to use Copilot to convert its disadvantages into ad- to guide towards an effective use of Copilot.
vantages are also worth further exploration. Besides, although

## References

we have investigated various aspects of using Copilot (e.g.,
limitations and challenges), we have not looked in depth at [1] J. Austin, A. Odena, M. Nye, M. Bosma, H. Michalewski, D. Dohan,

### E.Jiang,C.Cai,M.Terry,Q.Leetal.,“Programsynthesiswithlarge

what types of users (e.g., developers, educators, and students)
languagemodels,”arXivpreprintabs/2108.07732,2021.
whouseCopilot,whenandhowtheyuseCopilot,andforwhat [2] M. Allamanis, E. T. Barr, P. Devanbu, and C. Sutton, “A survey
specific purposes. By exploring these aspects, researchers can of machine learning for big code and naturalness,” arXiv preprint
abs/1709.06182,2018.
get meaningful information which would help guide towards
[3] H.Pearce,B.Ahmad,B.Tan,B.Dolan-Gavitt,andR.Karri,“Aneman effective use of Copilot. piricalcybersecurityevaluationofgithubcopilot’scodecontributions,”
arXivpreprintabs/2108.09293,2021.
VI. THREATSTOVALIDITY [4] GitHubCopilot·YourAIpairprogrammer,https://github.com/features/
copilot.
Construct validity: We conducted data labelling, extrac- [5] C. Bird, D. Ford, T. Zimmermann, N. Forsgren, E. Kalliamvakou,
tion, and analysis manually, which may lead to personal bias. T.Lowdermilk,andI.Gazit,“Takingflightwithcopilot:Earlyinsights
andopportunitiesofai-poweredpair-programmingtools,”ACMQueue,
To reduce this threat, the data labelling of SO posts was
vol.20,no.6,pp.35—-57,2023.
performed after the pilot labelling to reach an agreement [6] N.AlMadi,“Howreadableismodel-generatedcode?examiningreadbetweentheauthors.Thedataextractionandanalysiswasalso ability and visual inspection of github copilot,” in Proc. of the 37th
International Conference on Automated Software Engineering (ASE).
conductedbytwoauthors,andthefirstauthorrecheckedallthe
ACM,2023,pp.1–5.
resultsproducedbythethirdauthor.Duringthewholeprocess, [7] G.Sandoval,H.Pearce,T.Nys,R.Karri,B.Dolan-Gavitt,andS.Garg,
the first author continuously consulted with the second author “Securityimplicationsoflargelanguagemodelcodeassistants:Auser
study,”arXivpreprintabs/2208.09727,2022.
to ensure there are no divergences.
[8] S. Imai, “Is github copilot a substitute for human pair-programming?
External validity: We chose two popular developer com- an empirical study,” in Proc. of the 44th International Conference
munities (SO and GitHub Discussions) because SO has been onSoftwareEngineering:CompanionProceedings(ICSE-Companion).
IEEE,2022,pp.319–321.
widely used in software engineering studies and GitHub Dis-
[9] B.Yetistiren,I.Ozsoy,andE.Tuzun,“Assessingthequalityofgithub
cussions is a new feature of GitHub for discussing specific copilot’scodegeneration,”inProc.ofthe18thInternationalConference
topics [14]. These two data sources can partially alleviate the on Predictive Models and Data Analytics in Software Engineering
(PROMISE). ACM,2022,pp.62–71.
threattoexternalvalidity.However,weadmitthatourselected
[10] C. Wang, J. Hu, C. Gao, Y. Jin, T. Xie, H. Huang, Z. Lei, and
data sources may not be representative enough to understand Y. Deng, “Practitioners’ expectations on code completion,” arXiv
all the practices and challenges of using Copilot. preprintabs/2301.03846,2023.
[11] A.M.Dakhel,V.Majdinasab,A.Nikanjam,F.Khomh,M.C.Desmarais,

### Reliability: We conducted a pilot labelling before the for-

Z. Ming, and Jiang, “Github copilot ai pair programmer: Asset or
mal labelling of SO posts with two authors, and the Cohen’s liability?”arXivpreprintabs/2206.15331,2022.
Kappa coefficient is 0.773, indicating a decent consistency. [12] N. Nguyen and S. Nadi, “An empirical evaluation of github copilot’s
code suggestions,” in Proc. of the 19th IEEE/ACM International Con-
We acknowledge that this threat might still exist due to the
ferenceonMiningSoftwareRepositories(MSR). IEEE,2022,pp.1–5.
small number of posts used in the pilot. All the steps in our [13] A.Sarkar,A.D.Gordon,C.Negreanu,C.Poelitz,S.S.Ragavan,and
study, including manual labelling, extraction, and analysis of B.Zorn,“Whatisitliketoprogramwithartificialintelligence?”arXiv
preprintabs/2208.06213,2022.
data were conducted by three authors. During the process,
[14] H. Hata, N. Novielli, S. Baltes, R. G. Kula, and C. Treude, “Github
the three authors discussed the results until there was no discussions:Anexploratorystudyofearlyadoption,”EmpiricalSoftware
any disagreements in order to produce consistent results. Engineering,vol.27,no.1,pp.1–32,2022.
[15] J.Cohen,“Acoefficientofagreementfornominalscales,”Educational
In addition, the dataset of this study that contains all the
andPsychologicalMeasurement,vol.20,no.1,pp.37–46,1960.
extracted data and labelling results from the SO posts and [16] GitHub Discussions: Copilot Category, https://github.com/community/
GitHub discussions has been provided online for validation community/discussions/categories/copilot.
[17] A. N. Christopher, Interpreting and Using Statistics in Psychological
and replication purposes [20].
Research. SAGEPublications,2017.
[18] B.G.Glaser,“Theconstantcomparativemethodofqualitativeanalysis,”
VII. CONCLUSIONS SocialProblems,vol.12,no.4,pp.436–445,1965.
[19] L. R. Hallberg, “The “core category” of grounded theory: Making
We conducted an empirical study on SO and GitHub Disconstant comparisons,” International Journal of Qualitative Studies on
cussions to understand the practices and challenges of using HealthandWell-being,vol.1,no.3,pp.141–148,2006.
GitHub Copilot from the practitioners’ perspective. We used [20] B. Zhang, P. Liang, X. Zhou, A. Ahmad, and M. Waseem, Dataset
of the Paper: Practices and Challenges of Using GitHub Copilot: An
“copilot” as the search term to collect data from SO and
EmpiricalStudy,2023,https://doi.org/10.5281/zenodo.7604508.
collected all the discussions under the “Copilot” category in