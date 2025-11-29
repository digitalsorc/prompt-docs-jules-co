---
title: "Demystifying Practices Challenges Copilot"
original_file: "./Demystifying_Practices_Challenges_Copilot.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["llm", "rag", "react", "fine-tuning", "evaluation"]
keywords: ["copilot", "github", "code", "developers", "data", "results", "they", "discussions", "used", "when"]
summary: "<!-- Page 1 -->


### September 13, 2023 1:2 WSPC/INSTRUCTION FILE ws-ijseke

InternationalJournalofSoftwareEngineeringandKnowledgeEngineering
©WorldScientificPublishingCompany
Demystifying Practices, Challenges and Expected Features of Using

### GitHub Copilot


### BeiqiZhang,PengLiang∗,XiyuZhou

School of Computer Science, Hubei Luojia Laboratory, Wuhan University

### Wuhan 430072, China

{zhangbeiqi, liangp, xiyuzhou}@whu.edu.cn

### AakashAhmad

School of Computing and Communications, Lan"
related_documents: []
---

# Demystifying Practices Challenges Copilot

<!-- Page 1 -->


### September 13, 2023 1:2 WSPC/INSTRUCTION FILE ws-ijseke

InternationalJournalofSoftwareEngineeringandKnowledgeEngineering
©WorldScientificPublishingCompany
Demystifying Practices, Challenges and Expected Features of Using

### GitHub Copilot


### BeiqiZhang,PengLiang∗,XiyuZhou

School of Computer Science, Hubei Luojia Laboratory, Wuhan University

### Wuhan 430072, China

{zhangbeiqi, liangp, xiyuzhou}@whu.edu.cn

### AakashAhmad

School of Computing and Communications, Lancaster University Leipzig

### Leipzig 04109, Germany

a.ahmad13@lancaster.ac.uk

### MuhammadWaseem

School of Computer Science, Hubei Luojia Laboratory, Wuhan University
Wuhan 430072, China
m.waseem@whu.edu.cn
ReceivedDayMonthYear)

### Revised(DayMonthYear)


### Accepted(DayMonthYear)

With the advances in machine learning, there is a growing interest in AI-enabled tools
for autocompleting source code. GitHub Copilot, also referred to as the “AI Pair Programmer”,hasbeentrainedonbillionsoflinesofopensourceGitHubcode,andisone
of such tools that has been increasingly used since its launch in June 2021. However,
little effort has been devoted to understanding the practices, challenges, and expected
featuresofusingCopilotinprogrammingforauto-completedsourcecodefromthepoint
ofviewofpractitioners.Tothisend,weconductedanempiricalstudybycollectingand
analyzingthedatafromStackOverflow(SO)andGitHubDiscussions.Morespecifically,
wesearchedandmanuallycollected303SOpostsand927GitHubdiscussionsrelatedto
theusageofCopilot.Weidentifiedtheprogramminglanguages,IntegratedDevelopment
Environments(IDEs),technologiesusedwithCopilot,functionsimplemented,benefits,
limitations,andchallengeswhenusingCopilot.TheresultsshowthatwhenpractitionersuseCopilot:(1)ThemajorprogramminglanguagesusedwithCopilotareJavaScript
and Python, (2) the main IDE used with Copilot is Visual Studio Code, (3) the most
commonusedtechnologywithCopilotisNode.js,(4)theleadingfunctionimplemented
by Copilot is data processing, (5) the main purpose of users using Copilot is to help
generate code, (6) the significant benefit of using Copilot is useful code generation, (7)
themainlimitationencounteredbypractitionerswhenusingCopilotisdifficulty of integration, and (8) the most common expected feature is that Copilot can be integrated
with more IDEs. Our results suggest that using Copilot is like a double-edged sword,
∗Correspondingauthor.
1
3202
peS
11
]ES.sc[
1v78650.9032:viXra

<!-- Page 2 -->

September 13, 2023 1:2 WSPC/INSTRUCTION FILE ws-ijseke
2 B. Zhang et al.
which requires developers to carefully consider various aspects when deciding whether
ornottouseit.Ourstudyprovidesempiricallygroundedfoundationsthatcouldinform
softwaredevelopersandpractitioners,aswellasprovideabasisforfutureinvestigations
ontheroleofCopilotasanAIpairprogrammerinsoftwaredevelopment.
Keywords:GitHubCopilot,StackOverflow,GitHubDiscussions,RepositoryMining

## Introduction

Large Language Models (LLMs) and Machine Learning (ML) for autocompleting
source code are becoming more and more popular in software development. LLMs
nowadaysincorporatepowerfulcapabilitiesforNaturalLanguageProcessing(NLP)
[1], and ML approaches have been widely applied to source code using a variety
of new tools to support software development [2], which makes it possible to use
LLMs to synthesize code in general-purpose languages [1]. Recently, NLP-based
code generation tools have come into the limelight, with generative pre-trained
languagemodelstrainedonlargecorpusofcodeinanattempttoprovidereasonable
auto-completion of the source code when programmers write code [3]. Released in
June 2021, GitHub Copilot has recently emerged as an “AI pair programmer”,
which is powered by OpenAI Codex and suggests code or entire functions in IDEs
as a plug-in [4] to help developers achieve code auto-completion in development.
AlthoughtheemergenceofAI-assistedprogrammingtoolshasempoweredpractitioners in their software development efforts, there is little evidence and lack of
empirically-rooted studies (e.g, [3], [5], [6]) on the role of AI-assisted programming
toolsinsoftwaredevelopment.Theexistingstudiessuchas[7]and[8]primarilyfocus
onthecorrectnessandunderstandingofthecodesuggestedbyCopilot,andlittleis
known about the practices, challenges, and expected features of using Copilot during programming and software development activities for the developers and users
of Copilot. To ameliorate this gap, we conducted this study that collects data
from Stack Overflow (SO) and GitHub Discussions to get practitioners’ perspectives on using Copilot during software development. While Bird et al. investigated
Copilot users’ initial experiences of how they would use Copilot, as well as what
challenges they encountered by three studies [5], our study explored the practices,
challenges, and expected features of using Copilot by analyzing the data from developer communities. The emergence of Copilot has shifted the paradigm of pair
programming, and it is challenging for software development teams to adopt this
approach and tool on a large scale [5]. Our work intends to provide developers and
users of GitHub Copilot with comprehensive insights on the practices, purposes,
and expected features of using Copilot.
The contributions of this work: (1) we identified the programming languages,IDEs,andtechnologiesusedwithCopilot;(2)weprovidedthefunctionsimplemented by Copilot, the purposes, benefits, limitations/challenges, and expected
features of using Copilot; and (3) we collected and added more data related to
Copilot from SO and GitHub Discussions (134 posts and 272 discussions, leading
to 303 posts and 927 discussions in total) for purposes of enhancing the external

<!-- Page 3 -->


### September 13, 2023 1:2 WSPC/INSTRUCTION FILE ws-ijseke

Demystifying Practices, Challenges and Expected Features of Using GitHub Copilot 3
validity of our study results.
This paper is an extension of our previous conference paper [9] published in
the Proceedings of the 35th International Conference on Software Engineering and
Knowledge Engineering (SEKE 2023), and the following additions show how we
extended the previous work: (1) we extended our dataset by including the latest
data from Stack Overflow and GitHub Discussions formulated before June 18th,
2023(303SOpostsand927GitHubdiscussionsintotal);weexploredandreported
thepurposesofusingGitHubCopilotinRQ1.4;(3)weinvestigatedandreportedthe
expectedfeaturesofusersaboutGitHubCopilotfrompractitioners’perspectivesin
RQ2.3; and (4) we provide more implications based on the study results.
The structure of the paper: Section 2 surveys the related work, and Section 3
presentstheresearchdesignofthisstudy.Section4providesthestudyresults,which
are further discussed in Section 5. The potential threats to validity are clarified in
Section 6 and Section 7 concludes this work with future directions.

## Related Work


### Analyzing the Code Generated Using Copilot

Several studies focused on the security issues of Copilot. Sandoval et al. [10] conducted a user study to investigate the impact of programming with LLMs that
support Copilot. Their results show that LLMs have a positive impact on the correctness of functions, and they did not find any decisive impact on the correctness
of safety. Several studies focused on the quality of the code generated by Copilot. Imai [11] compared the effectiveness of programming with Copilot versus human programming, and found that the generated code by Copilot is inferior than
human-written code. Yetistiren et al. [8] assessed the quality of generated code by
Copilot in terms of validity, correctness, and efficiency. Their empirical analysis
shows Copilot is a promising tool. Madi et al. [6] focused on readability and visual
inspection of Copilot generated code. Through a human experiment, their study
highlights that programmers should beware of the code generated by tools. Wang
et al. [12] collected practitioners’ expectations on code generation tools through a
mixed-methods approach. They found that effectiveness and code quality is more
important than other expectations. Several studies focused on the limitations and
challenges in Copilot assisted programming.

### Capabilities and Limitations of Copilot

Several studies have explored the capabilities and limitations of GitHub Copilot.
Dakhelet al.[13]exploredCopilot’scapabilitiesthroughempiricalevaluations,and
their results suggest that Copilot shows limitations as an assistant for developers.NguyenandNadi[14]conductedanempiricalstudytoevaluatethecorrectness
andcomprehensibilityofthecodesuggestedbyCopilot.Theirfindingsrevealedthat
Copilot’ssuggestionsfordifferentprogramminglanguagesdonotdiffersignificantly,

<!-- Page 4 -->

September 13, 2023 1:2 WSPC/INSTRUCTION FILE ws-ijseke
4 B. Zhang et al.
andtheyidentifiedpotentialshortcomingsofCopilot,likegeneratingcomplexcode.
Bird et al. [5] conducted three studies to understand how developers use Copilot
and their findings indicated that developers spent more time assessing suggestions
by Copilot than doing the task by themselves. Sarkar et al. [15] compared programmingwithCopilottopreviousconceptualizationsofprogrammerassistanceto
examine their similarities and differences, and discussed the issues that might arise
in applying LLMs to programming.
Compared to the existing work (e.g., [8], [13]), our work intends to understand
thepractices,challenges,andexpectedfeaturesofusingCopilotbyexploringvarious
aspects of Copilot’s usage.

## Research Design

The goal of this study is to understand the practices, benefits and challenges, and
expectedfeaturesofusingGitHubCopilotfromthepointofviewofpractitionersin
thecontextofCopilotrelatedSOpostsandGitHubdiscussions.Weconductedand
reported this exploratory study by following the guidelines for empirical studies in
softwareengineringproposedin[16].WeformulatedtwoResearchQuestions(RQs)
witheightsub-RQsthatcontributetothegoalofthisstudy,aspresentedinSection
3.1 with their rationale. The overview of the research process is shown in Figure 1
and detailed in Section 3.2 and Section 3.3.

### Fig. 1: Overview of the research process


### Phase A - Outlining the Research Questions

We aimed to explore the characteristics of practices, challenges, and expected features of using GitHub Copilot by answering the RQs in the following:
RQ1: Programming Languages, IDEs, Technologies, Functions, and Purposes of Using GitHub Copilot
RQ1.1: What programming languages are used with GitHub Copilot?

<!-- Page 5 -->


### September 13, 2023 1:2 WSPC/INSTRUCTION FILE ws-ijseke

Demystifying Practices, Challenges and Expected Features of Using GitHub Copilot 5
Rationale: In software development, the role of programming languages is fundamental - enabling programmers to translate requirements by writing source code
using a specific programming language such as Java or Python. This RQ aims to
collect the programming languages that developers tend to use with Copilot.

### RQ1.2: What IDEs are used with GitHub Copilot?

Rationale: Copilot is a third-party plug-in used in IDEs. This RQ aims to identify
theIDEsfrequentlyusedwithCopilot.TheanswersofthisRQcanhelpdevelopers
choose which IDE to use when they code with Copilot.

### RQ1.3: What technologies are used with GitHub Copilot?

Rationale: When writing code, programmers need to employ certain technologies
to complete the development. This RQ aims to investigate the technologies that
can be used with Copilot (e.g., frameworks), and the answers of this RQ can help
developers to choose the technologies when they use Copilot.
RQ1.4: What functions are implemented by using GitHub Copilot?
Rationale: Copilotcancompleteentirefunctionsaccordingtousers’comments.This
RQ aims to provide a categorization of the functions that can be implemented by
Copilot, and the answers of this RQ can provide developers guidance when implementing functions by using Copilot.

### RQ1.5: What are the purposes of using GitHub Copilot?

Rationale: Users may use Copilot for different purposes. This RQ aims to explore
what are users using Copilot for, and the answers of this RQ can help us get a
better understanding of how people are using Copilot.
RQ2: Benefits, Limitations & Challenges, and Expected Features of Using GitHub Copilot

### RQ2.1: What are the benefits of using GitHub Copilot?

Rationale: Using Copilot to assist programming can bring many benefits (e.g., reducingtheworkloadofdevelopers).ThisRQaimstocollecttheadvantagesbrought
to the development by applying Copilot.
RQ2.2: What are the limitations & challenges of using GitHub Copilot?
Rationale: Although using Copilot to assist in writing code can help developers
with their programming activities, there are still restrictions and problems when
using Copilot. This RQ aims to collect and identify the limitations and challenges
practitioners may experience when using Copilot. The answers of this RQ can help
practitioners make an informed decision when deciding whether to code with the
help of Copilot.
RQ2.3: What are the expected features of users about GitHub Copilot?
Rationale: Since its released on June, 2021, GitHub Copilot has become increasinglypopularamongprogrammersandhasbeendevelopedintoamatureautomated
code-completion tool. However, there are still some features Copilot does not providebutuserswanttohave.ThisRQaimstoinvestigatetheexpectedfeaturesthat
users expect about GitHub Copilot. The answers of this RQ can give suggestions
to the development team of GitHub Copilot, guiding them to make Copilot an AI-

<!-- Page 6 -->

September 13, 2023 1:2 WSPC/INSTRUCTION FILE ws-ijseke
6 B. Zhang et al.
enabled coding tool that can better meet users’ needs.

### Phase B - Data Collection and Filtering

Thisstudyfocusesonunderstandingthepractices,challenges,andexpectedfeatures
of using Copilot collected from SO and GitHub Discussions. SO is a popular software development community and has been widely used by developers to ask and
answer questions as a Q&A platform. GitHub Discussions is a feature of GitHub
used to support the communication among the members of a project. Different
from SO, GitHub Discussions can provide various communication intentions, not
justquestion-answering(e.g.,adiscussioncanreporterrorsordiscussthepotential
development of a software project) [17], from which the data can be complementary to the data from SO. Besides, GitHub Discussions can provide a center of a
community knowledge base connected with other artifacts in a project [17]. Therefore, we decided to use SO and GitHub Discussions as the data sources to answer
our RQs, and we conducted the searches for both SO and GitHub Discussions on
June 18th, 2023. We conducted the data filtering manually because the numbers of
posts from SO and discussions from GitHub Discussions are not large, which could
be completed in an acceptable effort and time by manual work. Another reason
for using a manual approach is that conducting data filtering using an automatic
approach would lead to false positive filtering results and thus make the filtering
results inaccurate, which will negatively affect the findings we obtain.
For SO, “copilot” is used as the term to search the posts related to Copilot.
After searching, we got a total of 714 posts that include the search term “copilot”. The term “copilot” may appears more than once in a post, so there may be
duplicates in the URL collection of these retrieved posts. After removing the duplicates, we ended up with 678 posts with unique URLs. We conducted the data
To manually label posts related to Copilot, we conducted a pilot data labelling by
two authors with 10 retrieved SO posts. Specifically, the inclusion criterion is that
the post must provide information referring to Copilot. We calculated the Cohen’s
Kappa coefficient [18] to measure the consistency of labelled posts, which is 0.773,
thus indicating a decent agreement between the two coders. After excluding the
irrelevant posts in the search results, we finally got 303 Copilot related SO posts.
ForGitHubDiscussions,GitHubdiscussionsareorganizedaccordingtocategories.AfterexploringthecategoriesonGitHubDiscussions,wefoundthe“Copilot”
category which contains the feedback, questions, and conversations about Copilot [19] under the “GitHub product categories”. Since all the discussions under the
“Copilot” category are related to Copilot, we then included all the discussions under the “Copilot” category as related discussions to extract data. The number of
discussions related to Copilot is 927.

<!-- Page 7 -->


### September 13, 2023 1:2 WSPC/INSTRUCTION FILE ws-ijseke

Demystifying Practices, Challenges and Expected Features of Using GitHub Copilot 7

### Phase C - Data Extraction and Analysis

To answer the RQs in Section 3.1, similar to Data Collection and Filtering in Section3.2,wemanuallyextractedthedataitemslistedinTable1.Thefirstandthird
authors conducted a pilot data extraction independently with 10 SO posts and 10
GitHub discussions randomly selected from the 303 SO posts and 927 GitHub discussions.Thesecondauthorwasinvolvedtodiscusswiththetwoauthorsandcame
to an agreement if any disagreements were found during the pilot. After the pilot,
the criteria for data extraction were determined: (1) for all the data items listed in
Table 1, they will be extracted and counted only if they are explicitly mentioned
by developers that they were used with Copilot; (2) if the same developer repeatedly mentioned the same data item in an SO post or a GitHub discussion, we only
counted it once. In a post or discussion, multiple developers may mention Copilot
related data items, resulting in situation that the total number of instances of certain data item extracted may be greater than the number of posts and discussions.
The first and third authors further extracted the data items from the filtered posts
and discussions according to the extraction criteria, marked uncertain parts, and
discussed with the second author to reach a consensus. Finally, the first author
rechecked all the extraction results by the two authors from the filtered posts and
discussions to ensure the correctness of the extracted data.
Table 1: Data items extracted and their corresponding RQs
# Data Item Description RQ
D1 Programminglanguage ProgramminglanguagesusedwithCopilot RQ1.1

### D2 IDE IDEsusedwithCopilot RQ1.2

D3 Technology TechnologiesusedwithCopilot RQ1.3
D4 Function FunctionsimplementedbyCopilot RQ1.4

### D5 Purpose IntentionsofusingCopilot RQ1.5


### D6 Benefit BenefitsbroughtbyusingCopilot RQ2.1

D7 Limitationandchallenge RestrictionsanddifficultieswhenusingCopilot RQ2.2
D8 Expectedfeature FeaturesthatuserswantCopilottoprovide RQ2.3
Table 2: Data items and their analysis methods
# Data Item Data Analysis Method RQ
D1 Programminglanguage Descriptivestatistics[20] RQ1.1

### D2 IDE Descriptivestatistics RQ1.2

D3 Technology Descriptivestatistics RQ1.3
D4 Function Constantcomparison[21] RQ1.4
D5 Purpose Constantcomparison RQ1.5

### D6 Benefit Constantcomparison RQ2.1

D7 Limitationandchallenge Constantcomparison RQ2.2
D8 ExpectedFeature Constantcomparison RQ2.3

<!-- Page 8 -->

September 13, 2023 1:2 WSPC/INSTRUCTION FILE ws-ijseke
8 B. Zhang et al.

#### Analyze Data

For RQ1.1, RQ1.2, and RQ1.3, we used descriptive statistics [20] to analyze and
present the results. For RQ1.4, RQ1.5, and RQ2, we conducted a qualitative data
analysis by applying the Constant Comparison method [22]. We constantly comparedeachpartofthedata(e.g.,emergentcodes)toexploredifferencesandsimilarities in the extracted data to form categories [23]. Note that for answering RQ1.4,
we categorized the functions (D4) based on developers’ discussions, i.e., developers’ descriptions of the mentioned functions. Firstly, the first and the third authors
coded the filtered posts and discussions with the corresponding data items listed
(see Table 1). Secondly, the first author reviewed the coded data by the third author to make sure the extracted data were coded correctly. Finally, the first author
combined all the codes into higher-level concepts and turned them into categories.
After that, the second author examined the coding and categorization results, in
which any divergence was discussed till the three authors reached an agreement.
The data analysis methods with their corresponding data items and RQs are listed
in Table 2. The data analysis results are provided in [24].

## Results

Inthissection,thestudyresultsofRQ1.1toRQ1.4arevisualizedinFig2,andthe
results of RQ1.5 and RQ2.1 to RQ2.3 are provided in Table 3, 4, 5, and 6.

### RQ1: Programming Languages, IDEs, Technologies, and


### Functions of Using GitHub Copilot

RQ1.1: What programming languages are used with GitHub Copilot?
Figure2aliststhe19programminglanguagesusedwithCopilot,inwhichJavaScript
andPython arethemostfrequentlyusedones,bothaccountingforonefifth.Besides,
developers often write C# and Java code when using Copilot, as one practitioner
mentioned “the GitHub Copilot extension is enabled in my VS 2022 C# environment” (GitHub #14115). HTML+CSS, TypeScript, Golang, C, Rust, PHP, and
Kotlin were used with Copilot between 3˜12 times each (1.5% to 6.1%). The rest
programminglanguages(e.g.,Perl,Ruby),andVisual Basic whicharenotpopular,
were mentioned only once with Copilot.

### RQ1.2: What IDEs are used with GitHub Copilot?

Figure2bshows25typesofIDEsthatareusedwithCopilot.Visual Studio Code is
the dominant IDE, accounting for 48.0%. When first released, Copilot only worked
with Visual Studio Code editor, and it is expected that Visual Studio Code is
the IDE most often used with Copilot. Mainstream code editors, including Visual
Studio, IntelliJ IDEA, NeoVim, and PyCharm are also occasionally used, account
for 38.2% in total. The remaining IDEs were rarely mentioned by developers, and
one possible reason is that there are often integration issues when using Copilot
within them according to the results of RQ2.2.

<!-- Page 9 -->


### September 13, 2023 1:2 WSPC/INSTRUCTION FILE ws-ijseke

Demystifying Practices, Challenges and Expected Features of Using GitHub Copilot 9

### Jupyter Notebook Eclipse (0.1%)

(0.8%) CLion Android Studio R Em ub a y c M s i ( n 0 e .1 ( % 0. ) 1%)
Rust(0 D .6 a % rt )(3. C 1% PH ) P (2.6%) ( K 1 o .5 tl % in ) V V S i C su o a d l i u S m tu d (1 io .1%) G (0 o . L 9 a % n ) d (0 V .8 im %) (0.7%) (0.7%) C N Su o V b d A l e i c m -O c e e S s T S s e ( x ( 0 0 t . . 1 ( 1 0 % % .1 ) ) %)
(3.1%) Insider Rider (1.3%) Google Colab (0.1%)
Perl (0.5%) JavaScript (1.5%) DataSpell (0.1%)
(19.4%) WebStorm Xcode (0.1%)
(

## P

1
y
9
t
.
h
4
o
%
n
)
pythonJavaScript (1.9% Ph )
(
p
2

## S

.7
t
%
or
)
m Visual Studio Code CodeSpaces (0.1%)
Nim (0.5%) C++JavaC# (13 C .8 # %) Py (7 C . h 1 a % r ) m N ( e 7 o .7 V % im ) PyCharNme I o n V V te i i s m ll u ij a I l D S E tu A dio m ( o to st p u 5 s ) ed Visual Studio

### Code

Lu G a (3 o ( . 0 l 1 a . % 5 n % g ) ) R （% 8. ） 710.7 m 1 ( o t 3 o s . t p 8 u 1 5 9 s ) e .4 d 19.4 HTML+CSS Inte (8 ll . i 7 J % ID ) EA （% 7 ） .17.78.714.748.0 (48.0%)
(1.0%) (6.1%)
Ty ( p 4 e .6 S % cr ) ipt (8 C .7 + % + ) (1 J 0 a .7 v % a ) Vis ( u 1 a 4 l . 7 S % tu ) dio
Visual Basic Ruby
(0.5%) (0.6%)
(a) RQ1.1: Programming Languages (b) RQ1.2: Integreted Development Environments

### OpenCV (1.4%)


### GraphQL (1.4%) Ajax (2.8%) gRPC (1.4%)

LibTo J H r i c n t h m ja ( x 1 ( 1 ( .4 1 .4 % .4 % % ) ) ) .Net (12.5%)Do N o e m xt ( .j 1 s . 4 ( % 1.4 ) %)

### Dlib (1.4%)


### MongoDB (1.4%) Node.js


### Vue (5.6%) React (4.2%)

P T P y h a T r n e o d e r a c .j s h s ( ( ( 1 1 1 . . . 4 4 4 % % % ) ) ) m ( o to st p u 5 s ) ed .Net Sp V r F a i n n lu i g l t l t a F e r r J a ( S m 2 . ( e 8 1 w % .4 o ) % rk ) (1.4%) QT (1.4%) AjaxReactVue Data Build Tool (1.4%)
（%） 2.84.25.612.548.6

### Node.js (48.6%)

(c) RQ1.3: Development Technologies (d) RQ1.4: Implemented Functions
gnissecorp egamI tseT 7.59.413.2 15.122.6 gnissecorp ataD
Text processing URL ( 3 b . u 7% ild ) ing Al g (7 o .5 ri % th ) m
(3.7%) Calculation (3.7%)

### Test (15.1%)

Data processing (22.6%) String processing (9.4%) （%）
Serialization most implemented (3.8%) (top 5)
Printing (1.9%) Filtering

### Memory read (1.9%)

(1.9%) It ( e 3 r . a 8 t % io ) n Image ( 7 p . r 5 o % ce ) ssingFront-end ( 1 e 3 le .2 m % e ) nt control
gnissecorp gnirtS
lortnoc
tnemele dne-tnorF
Fig. 2: Programming languages, IDEs, technologies, and implemented functions of
using Copilot (results of RQ1.1 to RQ1.4)

### RQ1.3: What technologies are used with GitHub Copilot?

Figure 2c presents 23 technologies used with Copilot. We find that these identified
technologies include frameworks, APIs, and libraries. Node.js, whose proportion is
more than 45%, is one of the most popular back-end runtime environments for
JavaScript, which is also the most frequently used language with Copilot (see the
results of RQ1.1), thus it is reasonable that Node.js is the major technology used
withCopilot.Inaddition,.NET whichworksforWebdevelopment,andVue,React,
Flutter,andAjax whichareframeworksforfront-enddevelopment,werementioned
less often compared to Node.js. The rest of the identified technologies, many of
which relate to machine learning (e.g., Pandas, Dlib, and OpenCV) or front-end
development (e.g., Htmx, Vanilla JS, and Next.js), are rarely used with Copilot,
and each of them appears only once.
RQ1.4: What functions are implemented by using GitHub Copilot?
Figure 2d shows 14 functions implemented by using Copilot. The main function
implementedbyCopilotisdata processing,indicatingthatdeveloperstendtomake

<!-- Page 10 -->

September 13, 2023 1:2 WSPC/INSTRUCTION FILE ws-ijseke
10 B. Zhang et al.
use of Copilot to write functions working with data. Besides, test (15.1%) and
front-end element control (13.2%) are the functions that account for more than
10% besides data processing. When implementing functions, developers also use
Copilot to code string processing, image processing, and algorithm, among which
image processing and algorithm account for the same, i.e., 7.5%. The rest types
of functions are seldom implemented by using Copilot, which are mentioned by
developers twice or once.

### RQ1.5: What are the purposes of users using GitHub Copilot?

Table 3 shows nine purposes of using Copilot. 43.3% of the developers from SO
and GitHub Discussions indicated that they used Copilot to help generate code
they needed. Another 9 developers (15.0%) said that they wanted to try out the
functionality of Copilot, so they downloaded the tool and used it. To fix bugs is the
third most popular reason for developers to use Copilot. When developers found
their code did not work and they could not fix the bugs by themselves, they would
turn to Copilot for help, as one developer mentioned in the post “I’ve been working
with copilot and chatgpt for days trying to get the code to work by fixing it” (SO
# 76498229).Toimprovecodingability andtoprovideideasforwritingcode havethe
samepercentage,6.7%.SomedevelopersusedCopilottohelpthemlearnknowledge
related to coding to improve coding ability, for examples, one developer said that
“I am trying to learn js” (GitHub #6947) when he applied for free use of Copilot.
Some developers did not want to directly use the code suggested by Copilot, and
they only wanted to refer to the suggestions of Copilot to provide them with ideas
on how to solve their problems. Copilot can be used for educational purposes and
for research purposes as well. Users also use Copilot to help them generate code
comments,asonedevelopermentionedthatheused“Copilot in Visual Studio 2022
to document code” (SO #76070342), but the percentage of this purpose is only
5.0%.Besides,twodevelopers(3.3%)madeuseofCopilotto check the code because
they could not find why the code did not work.

### RQ2: Benefits, Limitations & Challenges, and Expected


### Features of Using GitHub Copilot


### RQ2.1: What are the benefits of using GitHub Copilot?

Table 4 highlights 10 benefits of using Copilot. Most developers mentioned that
they used Copilot for useful code generation, which reduced their workload and
gave them help when they have no idea about how to write code. Programming
with Copilot also brings faster development, as one discussion remarked, Copilot
“saves developers a lot of time” (GitHub #35850). Meanwhile, better code quality
can be obtained by using Copilot. Compared to the code written by developers
themselves, the code suggested by Copilot is usually shorter and more correct, as
one developer said, “often Copilot is smarter than me” (SO #74512186). Copilot
can use machine learning models to learn code style of developers, so as to offer
good adaptation to users’ code patterns. Four developers mentioned that Copilot

<!-- Page 11 -->


### September 13, 2023 1:2 WSPC/INSTRUCTION FILE ws-ijseke

Demystifying Practices, Challenges and Expected Features of Using GitHub Copilot 11
Table 3: Purposes of using GitHub Copilot (results of RQ1.5)

### Purpose Example Count %

Tohelpgeneratecode GitHub CoPilot was able to fill in the code I needed 26 43.3%
afterIwrotethestepsincomments(SO#71905508)
Totryoutthefunctional- I use VIM and IntelliJ on a daily basis, and I re- 9 15.0%
ityofCopilot centlyinstalledVSCodetotryoutthenewest”CopilotChat”features (SO#76349751)
Tofixbugs spent a month trying to get it to work on my own 7 11.7%
and after a week of trying to get chatgpt or copilot
tofixthebugsI’malloutofideas (SO#76266095)
Toimprovecodingability I’m improving my rusty skills lately and saw (in 4 6.7%
some Copilot suggestions) the question mark operatorusedasaprefixofvariables (SO#74008676)
To provide ideas for writ- With the input from jps (AES is actually OK for 4 6.7%
ingcode encrypted tokens, but not signed) and Github CopilotIcameupwithaworkingsolutionusingHMAC-

## Sha256 (So#72812667)

Foreducationalpurposes For the past year I have used and taught my stu- 3 5.0%
dentshowtheycouldbenefitfromco-pilotwhilecoding (GitHub#19410)
To generate code com- Using ChatGPT and Copilot, I’ve commented it to 3 5.0%
ments understanditsfunctionality.(SO#75624961)
Tocheckthecode I’vecheckedmyselfbysteppingthrough,I’vechecked 2 3.3%
with GitHub Copilot, I’ve checked with ChatGPT,
andtheyallsaythisiscorrect.(SO#76311798)
Forresearchpurposes IamworkingonascientificstudytestinghowCopi- 2 3.3%
lotwilleffecttheacademicsetting (GitHub#8324)
Table 4: Benefits of using GitHub Copilot (results of RQ2.1)

### Benefit Example Count %

Usefulcodegeneration I find myself writing a lot of tests, and Copilot 28 45.9%
isexcellentathelpingwithwritingrepetitivetests
(GitHub#9282)
Fasterdevelopment Ireallyenjoyusingit,itreduceprogrammingtime 10 16.4%
(GitHub#17382)
Bettercodequality it’s faster and simpler to your solution (SO 7 11.5%
# 68418725)
Good adaptation to users’ GitHubcopilotadapttoyourcodingpractices(SO 4 6.6%
codepatterns #69740880)
Betteruserexperience Since copilot works totally different compared to 4 6.6%
all the other products out there, it is a lot more
funtouseanddoesnotannoymelikesomeother

### AIsystems (GitHub#7254)

Freeforstudents IfyouareastudentyoucansignupfortheGitHub 3 4.9%
Student Pack, which gives a lot of benefits, one
beingcopilotforfree (GitHub#31494)
Powerful code interpreta- DoesCopilothavethecodeexplanationfeatureor 2 3.3%
tion and conversion func- something similar? It does! some active members
tions weregivenbetaaccess.(GitHub#38089)
Frequentupdatestoprovide Keep in mind that there are updates to the plu- 1 1.6%
morefeatures gin very frequently, so there’s still hope (SO
# 70428218)
Strong integration capabil- GitHubissupportingmoreeditors(GitHub#6858) 1 1.6%
ity
Easeofstudyanduse when using this plugin, can study at a relatively 1 1.6%
lowcost (GitHub#8028)
can give them better user experience than other AI-assisted programming tools, for
example, one developer stated that “Copilot works totally different compared to all

<!-- Page 12 -->

September 13, 2023 1:2 WSPC/INSTRUCTION FILE ws-ijseke
12 B. Zhang et al.
the other products out there, it is a lot more fun to use and does not annoy me like
someotherAIsystems”(GitHub#7254),withoutprovidingthenamesoftheother
products.
RQ2.2: What are the limitations & challenges of using GitHub Copilot?
Table5lists15limitationsandchallengesofusingCopilot.Mostdeveloperspointed
out the difficulty of integration between Copilot and IDEs or other plug-ins. After
Copilotwasinstalledindevelopers’IDEs,certainplug-insdidnotworkandCopilot
mayconflictwithsomeshortcutsettingsoftheeditors.Moreover,Copilotcannotbe
successfully integrated with some IDEs as Copilot does not support these editors
yet. Due to the instability of Copilot servers, no support for proxies, and access
restriction of some regions, developers may have difficulties of accessing Copilot.
The code suggested by Copilot has constraints as well, and sometimes it just offers few solutions, which are not enough for users, which brings limitation to code
generation,asonedevelopersaid“multiple solution is too little”(GitHub#37304).
Practitioners also complained about the poor quality of generated code by Copilot.
Some practitioners said that “GitHub Copilot suggest solutions that don’t work”
(SO #73701039), and some practitioners found that when the code files became
larger,thequalityofthecodesuggestedbyCopilot“becomesunacceptable”(GitHub
# 9282). When using Copilot, developers pay much attention to code privacy threat
as well. They were worried that Copilot may use their code information without
permission. Contrary to the developers who mentioned that Copilot gave them a
betteruserexperience thanotherAI-assistedprogrammingtools,somepractitioners
said they had an unfriendly user experience when coding with Copilot. Compared
to the results of our previous work [9], the number of difficulty of subscription increases significantly. This may be caused by the restrictions for free users, as one
user complained “so looks like people with a free plan are stuck on a rate-limit for
now with no way out” (GitHub #43893).
Table 5: Limitations and challenges of using Copilot (results of RQ2.2)

### Limitation & Challenge Example Count %

Difficultyofintegration CopilotonlyworkswithVSCode,VSCodiumisnot 114 28.1%
supportedatthemoment (GitHub#14837)
DifficultyofaccessingCopi- I cannot connect to the GitHub account and the 69 17.0%
lot Copilot server in VSCode, also cannot use the

### Copilotplugin (SO#74398521)

Limitation to code genera- Copilotislimitedtoaround1000charactersinthe 48 11.8%
tion response (GitHub#15122)
Poor quality of generated Github Copilot suggest solutions that don’t work 36 8.9%
code (SO#73701039)
Codeprivacythreat Copilotdoescollectpersonaldatasojusttakepre- 29 7.1%
caution when working in private repos (GitHub
# 7163)
Unfriendlyuserexperience I had the same problem today, an amazing tool 25 6.2%
withpooruserexperience (GitHub#8468)
Difficultyofsubscription My copilot subscription suddenly stopped. Tried 22 5.4%
logoutandin.Neverhavereplyonsupportticket
over10days (GitHub#36190)

<!-- Page 13 -->


### September 13, 2023 1:2 WSPC/INSTRUCTION FILE ws-ijseke

Demystifying Practices, Challenges and Expected Features of Using GitHub Copilot 13
Highpricing itisobviousthatnooneinSouthAmericawillpay 14 3.4%
thatprice,itistooexpensive (GitHub#24594)
Lackofcustomization MyquestionisaboutsettingupshortcutsinVisual 13 3.2%
StudioCodeVSCodeforGitHubCopilotLabs.(SO
# 73564811)
Difficulty of understanding I really do not understand this enough, and have 12 3.0%
thegeneratedcode noideahalfofwhatthiscodedoeshonestly.Itwas
writtenbyCopilot.(SO#72282605)
Hardtoconfigure Keepgetting”YourCopilotexperienceisnotfully 10 2.5%
configured,completeyoursetup”inVisualStudio
2022 (GitHub#19556)
Noeditionfororganizations Currently, Copilot is only available for individual 8 2.0%
useraccountsandorganizationsaren’tabletopurchase/manage Copilot for their members just yet
(GitHub#32775)
Showloading I am not sure what is causing this but while edit- 3 0.7%
ing files within Visual Studio, I am periodically
locking up with the following dialog showing (SO
# 73682137)
Challenge of not providing making sure that the tool does not provide out- 2 0.5%
outdatedsuggestions dated suggestions would still be a challenge (SO
# 72554382)
Needofbasicprogramming Itisuselessifyoudonotunderstandtheprogram- 1 0.2%
knowledge minglanguageorthetaskyouwanttodo(GitHub
# 35850)
Table 6: Expected features of users about Copilot (results of RQ2.3)

### Expected Feature Count %


### CanbeintegratedwithmoreIDEs 32 28.8%

Allowcustomizationofshortcutsforsuggestions 12 10.8%
Givesuggestionswhenrequested 8 7.2%

### Ateamversion 7 6.3%


### Supportaccessproxies 7 6.3%

Allowcustomizationoftheformatofgeneratedcode 5 4.5%

### Accepttheneededpartofthesuggestions 4 3.6%

Compatiblewithothercodegenerationtools 4 3.6%
Allowsettingfiltersforsuggestions 3 2.7%

### Allowself-signedcertificates 3 2.7%

Canbeusedwithmoredevelopmentframeworks 2 1.8%

### Abilitytoturnoffdatacollection 2 1.8%

SuggestionsinIDEUIcanbeconfigured 2 1.8%

### Codeexplanation 2 1.8%


### Freeforcertaintypeofusers 2 1.8%


### Providemoresuggestionsatatime 2 1.8%

Providemorecompletesuggestions 2 1.8%

### AbilitytodrawUMLdigrams 1 0.9%

Enableadialogtoacceptordenysuggestions 1 0.9%
AversionforCLI(Command-LineInterface) 1 0.9%

### Aon-premisesversion 1 0.9%

Abilitytoselectthetrainingsourcesforsuggestions 1 0.9%

### Canbeusedinremoteservers 1 0.9%


### Provideagettingstartedguide 1 0.9%

Provideasecurityratingforgeneratedcode 1 0.9%
Reminduserswhenithasnosuggestions 1 0.9%

### Showacceptancerateofsuggestions 1 0.9%

Viewthecode-relateddatasharedbyCopilot 1 0.9%

### Disablenotificationsoundsofsuggestions 1 0.9%

RQ2.3: What are the expected features of users about GitHub Copilot?

<!-- Page 14 -->

September 13, 2023 1:2 WSPC/INSTRUCTION FILE ws-ijseke
14 B. Zhang et al.
Table6presents29featuresthatusersexpectedtouseaboutCopilot.ThemostoftenmentionedfeaturebyusersisthattheyhopeCopilotcanbeintegratedwithmore
IDEs (28.8%).AccordingtotheresultsofRQ2.2,thedominantlimitationandchallenge of using Copilot is difficulty of integration as Copilot cannot be used in some
editors. It is then reasonable that many users want Copilot to support more IDEs.
10.8%usersremarkedthattheywantedCopilottoallow customization of shortcuts
for suggestions, as one post wrote “Github CoPilot should give us an option to assign a custom key instead of a [TAB] or should change to something like [SHIFT +
TAB]insteadofTAB”(GitHub#7036).Eightusers(7.2%)expectedCopilottogive
suggestions when requested. They did not want Copilot to suggest code all the time
because it was interruptive, and they just wanted to get suggestions from Copilot
whentheyrequested.Forexample,oneuserasked“IsitpossibletonothaveGitHub
Copilot automatically suggest code, instead only showing its suggestions when using the ‘trigger inline suggestion’ shortcut?” (SO #76147937). Seven developers
expected Copilot to lanch a team version and support access proxies, respectively.
Allow customization of the format of generated code was mentioned by 5 developers.Theywantedthisfeatureto“configuresuggestionappearance”(GitHub#7234)
so that Copilot suggestions could be “more distinguishable with normal code” and
thus “improve the accessibility” (GitHub #7628). Few developers indicated that
they only wanted to “accept one line of several” of Copilot suggested code (SO
# 75183662), and they called for the feature that they can accept the needed part of
the suggestions. Besides, four developers also mentioned that they hoped Copilot
could be compatible with other code generation tools like ReSharper.

## Implications

Thissectionpresentsthekeyimplicationsofourstudy,whichrepresentempirically
grounded findings that could help researchers and developers to understand the
effective usage of Copilot.
IntegrationofCopilotwithIDEs:AccordingtotheresultsofRQ1.2andRQ2.2,
we found that most developers choose to integrate the Copilot plug-in with mainstreamIDEs(includingVisual Studio Code,Visual Studio,IntelliJ IDEA,NeoVim,
andPyCharm),andthepercentageofmainstreamIDEsusedwithCopilotbypractitionersreaches86.2%.WhendeveloperschoosethelesserknownIDEs(e.g.,Sublime
Text), they often find it hard to integrate the Copilot plug-in and thus have difficulty of integration.InadditiontothereasonthatdevelopersmayinstallCopilotin
theirchosenIDEsincorrectly,anotherreasonforthedifficulty of integration isthat
Copilot does not support certain IDEs at the moment. When developers choose to
use Copilot in mainstream IDEs, they can install it smoothly, and even if problems
ariseduringtheinstallationoruse,theycaneasilyfindasolutiononSOorGitHub
Discussions as many other developers may have encountered similar issues. On the
contrary, when developers choose to use Copilot in unpopular IDEs, they may not
be able to install it because the IDEs are not officially supported by Copilot, and

<!-- Page 15 -->


### September 13, 2023 1:2 WSPC/INSTRUCTION FILE ws-ijseke

Demystifying Practices, Challenges and Expected Features of Using GitHub Copilot 15
theycannotfindsolutionsasfewdevelopersuseCopilotwiththeseIDEs.Toreduce
the difficulty of integration, we recommend practitioners to use mainstream IDEs
with Copilot. Besides, the most expected feature of users is that they hope Copilot
can be integrated with more IDEs, which confirms with the results of RQ2.2 (the
main limitation of using Copilot is difficulty of integration). We suggest GitHub
can consider integrating Copilot with more IDEs in the future, which can meet the
needs of diverse developers.
Support for Front-end and Machine Learning Development: As shown in
the results of RQ1.1, RQ1.3, and RQ1.4, practitioners often write JavaScript and
Python code when using Copilot, and they tend to use Copilot with front-end and
machine learning related technologies (including frameworks, APIs, and libraries)
toimplementfront-end(e.g.,front-end element control)andmachinelearningfunctions(e.g.,data processing andimage processing).JavaScript isthefoundationlanguage of many popular front-end frameworks and most of Websites use JavaScript
on the client side. Python is the first choice when it comes to the development of
machinelearningsolutionswiththehelpofrichlibraries,e.g.,OpenCV.ItisconsequentlyreasonablethatdeveloperstendtouseCopilotwithJavaScript togenerate
code for front-end and Python for developing machine learning applications.
Different Versions of Copilot: From the results of RQ2.3, we can find that
different versions of Copilot are needed (i.e., a team version, a version for CLI
(Command-Line Interface), and a on-premises version). In different development
environments, developers may have specific requirements when using Copilot. If
GitHubcanreleasedifferentversionsofCopilot,itwouldincreasetheusabilityand
acceptanceofCopilotandthusmakeitavailabletoawidervarietyofusers.Besides,
GitHub has officially launched some versions of Copilot, e.g., Copilot Labs, Copilot
X, and Copilot Nightly. Copilot Labs [25] is used to experiment with new ideas
before taking them into real production, Copilot X [26] provides an enhancement
with new features, and Copilot Nightly contains experimental and less well tested
changes. Developers can choose the version of Copilot according to their needs.
Potentials and Perils of Using Copilot in Software Development: Trained
on billions of lines of code, Copilot can turn natural language prompts into coding
suggestions across dozens of programming languages and make developers code
faster and easier [4]. The results of RQ2.1 and RQ2.2 show that many benefits of
using Copilot contradict its limitations and challenges, e.g., useful code generation
vs. limitation to code generation. When deciding to use Copilot, developers should
consider tool integration, user experience, budget, code privacy, and some other
aspects, and make trade-offs between these factors. In short, using Copilot is like
a double-edged sword, and practitioners need to consider various aspects carefully
when deciding whether or not to use it. If Copilot can be used with appropriate
programming languages and technologies to implement functions required by users
correctlyindevelopers’IDEs,itwillcertainlyoptimizedevelopers’codingworkflow
and do what matters most - building software by letting AI do the redundant
work. Otherwise, it will bring difficulties and restrictions to development, making

<!-- Page 16 -->

September 13, 2023 1:2 WSPC/INSTRUCTION FILE ws-ijseke
16 B. Zhang et al.
developers feel frustrated and constrained. The study results can help practitioners
being aware of the potential advantages and disadvantages of using Copilot and
thus make an informed decision whether to use it for programming activities.
Understanding the Code Generated by Copilot: From the results of RQ2.1,
RQ2.2, and RQ2.3, we can see that some practitioners think one of the benefits of
usingCopilotisthatithaspowerfulcodeinterpretation feature,butsomepractitioners complained about the difficulty of understanding the generated code by Copilot
and called for code explanation feature. It would be interesting to investigate why
developers have opposing attitude towards understanding the code generated by
Copilot and how the generated code by Copilot can be better explained to and
understood by developers. Besides, GitHub Copilot Labs which is dependent on
Copilot extension has been released for experimental purposes, and Copilot Labs
has the feature to provide explanations of the code generated by Copilot for developers [25]. The latest Copilot X also has the code explanation feature [26], but we
do not know the reason why developers do not use Copilot Labs or Copilot X to
interpret Copilot-generated code. We suggest that Copilot can provide the features
for developers to better understand the generated code directly, such as generating
code comments with the generated code in IDEs.
Users’ customization on suggestions by Copilot: According to the results
of RQ2.2, some developers thought that one of the limitations and challenges of
Copilot is lack of customization, and it is expected that a number of developers
called for features of Copilot to allow customization of shortcuts for suggestions,
allowcustomizationoftheformatofgeneratedcode,andaccepttheneededpartofthe
suggestions (seetheresultsofRQ2.3).TheexistingfeaturesofCopilotcannotsatisfy
users’needsoncodesuggestions.Userspointedoutthattheyhaddifficultyinsetting
up shortcuts for actions on suggestions (e.g., accepting suggestions). Based on the
feedbackfromusers,theycanonlyacceptsuggestionsviathetabkey,however,they
want “an option to change the keybinding for accepting the suggestions” instead
(GitHub #6919). Besides, a few users also reflected that it was hard to distinguish
between the code wrote by themselves and the code suggested by Copilot. They
wanted to customize the color, font, and format of Copilot suggestions. Another
expectedfeatureofusersaboutCopilotisthattheyhopetheycanaccepttheneeded
partofthesuggestions.SomeuserswanttoacceptCopilotsuggestionslinebylineor
acceptonlythenextwordofCopilotsuggestionseachtime,whiletheydonotwant
accept the entire suggestions by Copilot. As a result, there is a need for users to
customizethewayofacceptingsuggestionsbyCopilot.Someotherexpectedfeatures
(e.g., allow setting filters for suggestions, suggestions in IDE UI can be configured,
andabilitytoselectthetrainingsourcesforsuggestions)alsorelatetocustomization
onsuggestionsbyCopilot.Onthebasisoftheabovefeedbackfromusers,webelieve
that it is necessary for Copilot to allow customization for suggestions, which will
give developers better user experience when using Copilot as they are able to use
it in the way they want.
Towards an Effective Use of Copilot:Furtherinvestigationaboutthepractices

<!-- Page 17 -->


### September 13, 2023 1:2 WSPC/INSTRUCTION FILE ws-ijseke

Demystifying Practices, Challenges and Expected Features of Using GitHub Copilot 17
ofCopilotcanbeconductedbyquestionnaireandinterview.Underwhatconditions
thechallengesofusingCopilotwillshowupasadvantagesordisadvantages,andhow
to use Copilot to convert its disadvantages into advantages are also worth further
exploration.Besides,althoughwehaveinvestigatedvariousaspectsofusingCopilot
(e.g.,limitationsandchallenges),wedidnotlookedindepthatwhattypesofusers
(e.g., developers, educators, and students) who use Copilot, when and how they
useCopilot.Byexploringtheseaspects,researcherscangetmeaningfulinformation
which would help guide towards an effective use of Copilot.

## Threats to Validity

The validity threats are discussed according to the guidelines in [16], and internal
validity is not considered, since we did not investigate the relationships between
variablesandresults.Thethreevaliditythreatspresentedbelowhighlightpotential
limitations of this research that may invalidate some of the results. Future research
can focus on minimizing these threats to ensure methodological rigor of the study.
Construct validity indicates whether the theoretical and conceptual constructs are correctly measured and interpreted. We conducted data labelling, extraction, and analysis manually, which may lead to personal bias. To reduce this
threat, the data labelling of SO posts was performed after the pilot labelling to
reachanagreementbetweentheauthors.Thedataextractionandanalysiswasalso
conductedbytwoauthors,andthefirstauthorrecheckedalltheresultsproducedby
the third author. During the whole process, the first author continuously consulted
with the second author to ensure there are no divergences.
External validity indicates the the degree of generalization of the study results, i.e., the extent to which the results can be generalized to other contexts. We
chose two popular developer communities (SO and GitHub Discussions) because
SOhasbeenwidelyusedinsoftwareengineeringstudiesandGitHubDiscussionsis
a new feature of GitHub for discussing specific topics [17]. These two data sources
can partially alleviate the threat to external validity. However, we admit that our
selected data sources may not be representative enough to understand all the practices, challenges, and expected features of using Copilot.
Reliability indicates the replicability of a study yielding the same or similar
results. We conducted a pilot labelling before the formal labelling of SO posts with
two authors, and the Cohen’s Kappa coefficient is 0.773, indicating a decent consistency. We acknowledge that this threat might still exist due to the small number
of posts used in the pilot. All the steps in our study, including manual labelling,
extraction, and analysis of data were conducted by three authors. During the process, the three authors discussed the results until there was no any disagreements
in order to produce consistent results. In addition, the dataset of this study that
contains all the extracted data and labelling results from the SO posts and GitHub
discussions has been provided online for validation and replication purposes [24].

<!-- Page 18 -->

September 13, 2023 1:2 WSPC/INSTRUCTION FILE ws-ijseke
18 B. Zhang et al.

## Conclusions

We conducted an empirical study on SO and GitHub discussions to understand
the practices, challenges, and expected features of using GitHub Copilot from the
practitioners’ perspective. We used “copilot” as the search term to collect data
from SO and collected all the discussions under the “Copilot” category in GitHub
discussions. Finally, we got 303 SO posts and 927 GitHub discussions related to
Copilot.Ourresultsidentifiedtheprogramminglanguages,IDEs,technologiesused
with Copilot, functions implemented by Copilot, and the benefits, limitations, and
challenges of using Copilot, which are first-hand information for developers. The
main results are that: (1) JavaScript and Python are the most frequently discussed
programming languages by developers with Copilot. (2) Visual Studio Code is the
dominant IDE used with Copilot. (3) Node.js is the major technology used with
Copilot. (4) Data processing is the main function implemented by Copilot. (5) To
help generate code is the leading purpose of users using Copilot. (6) Useful code
integration is the most common benefit mentioned by developers when using Copilot. (7) Difficulty of integration is the most frequently encountered limitations and
challenges when developers use Copilot. (8) Copilot can be integrated with more
IDEs is the most expected feature of users.
Inthenextstep,weplantoexplorethepracticesofusingCopilotbyconducting
interviews or an online survey to get practitioners’ perspectives on using Copilot,
which can supplement our existing data collected from repository mining. Besides,
wealsoplantofurtherexplorevariousaspectsofCopilot,especiallyhowtoimprove
the understanding of developers on the generated code (see Section 5).

### Acknowledgements

ThisworkhasbeensupportedbytheNaturalScienceFoundationofChina(NSFC)
under Grant No. 62172311 and the Special Fund of Hubei Luojia Laboratory.

### References

[1] J.Austin,A.Odena,M.Nye,M.Bosma,H.Michalewski,D.Dohan,E.Jiang,C.Cai,
M.Terry,Q.Leetal.,“Programsynthesiswithlargelanguagemodels,”arXivpreprint
abs/2108.07732, 2021.
[2] M.Allamanis,E.T.Barr,P.Devanbu,andC.Sutton,“Asurveyofmachinelearning
for big code and naturalness,” arXiv preprint abs/1709.06182, 2018.
[3] H. Pearce, B. Ahmad, B. Tan, B. Dolan-Gavitt, and R. Karri, “An empirical
cybersecurity evaluation of github copilot’s code contributions,” arXiv preprint
abs/2108.09293, 2021.
[4] GitHub Copilot · Your AI pair programmer, https://github.com/features/copilot.
[5] C.Bird,D.Ford,T.Zimmermann,N.Forsgren,E.Kalliamvakou,T.Lowdermilk,and
I. Gazit, “Taking flight with copilot: Early insights and opportunities of ai-powered
pair-programming tools,” ACM Queue, vol. 20, no. 6, pp. 35–57, 2023.
[6] N.AlMadi,“Howreadableismodel-generatedcode?examiningreadabilityandvisual
inspection of github copilot,” in Proc. of the 37th Int. Conf. on Automated Software
Engineering (ASE). ACM, 2023, pp. 1–5.

<!-- Page 19 -->


### September 13, 2023 1:2 WSPC/INSTRUCTION FILE ws-ijseke

Demystifying Practices, Challenges and Expected Features of Using GitHub Copilot 19
[7] N. Nguyen and S. Nadi, “An empirical evaluation of github copilot’s code suggestions,”inProc.ofthe19thInt.Conf.onMiningSoftwareRepositories(MSR). IEEE,
2022, pp. 1–5.
[8] B.Yetistiren,I.Ozsoy,andE.Tuzun,“Assessingthequalityofgithubcopilot’scode
generation,”inProc. of the 18th Int. Conf. on Predictive Models and Data Analytics
in Software Engineering (PROMISE). ACM, 2022, pp. 62–71.
[9] B.Zhang,P.Liang,X.Zhou,A.Ahmad,andM.Waseem,“Practicesandchallengesof
usinggithubcopilot:Anempiricalstudy,”inProc.ofthe35thInt.Conf.onSoftware
Engineering and Knowledge Engineering (SEKE). KSI, 2023, pp. 124–129.
[10] G. Sandoval, H. Pearce, T. Nys, R. Karri, B. Dolan-Gavitt, and S. Garg, “Security
implications of large language model code assistants: A user study,” arXiv preprint
abs/2208.09727, 2022.
[11] S. Imai, “Is github copilot a substitute for human pair-programming? an empirical
study,”inProc.ofthe44thInt.Conf.onSoftwareEngineering:CompanionProceedings (ICSE-Companion). IEEE, 2022, pp. 319–321.
[12] C.Wang,J.Hu,C.Gao,Y.Jin,T.Xie,H.Huang,Z.Lei,andY.Deng,“Practitioners’
expectations on code completion,” arXiv preprint abs/2301.03846, 2023.
[13] A. M. Dakhel, V. Majdinasab, A. Nikanjam, F. Khomh, M. C. Desmarais, Z. Ming,
and Jiang, “Github copilot ai pair programmer: Asset or liability?” arXiv preprint
abs/2206.15331, 2022.
[14] N. Nguyen and S. Nadi, “An empirical evaluation of github copilot’s code suggestions,” in Proc. of the 19th IEEE/ACM Int. Conf. on Mining Software Repositories
(MSR). IEEE, 2022, pp. 1–5.
[15] A.Sarkar,A.D.Gordon,C.Negreanu,C.Poelitz,S.S.Ragavan,andB.Zorn,“What
isitliketoprogramwithartificialintelligence?”arXivpreprintabs/2208.06213,2022.
[16] P. Runeson and M. Ho¨st, “Guidelines for conducting and reporting case study research in software engineering,” Empirical Software Engineering, vol. 14, no. 2, pp.
131–164, 2009.
[17] H. Hata, N. Novielli, S. Baltes, R. G. Kula, and C. Treude, “Github discussions: An
exploratorystudyofearlyadoption,”Empirical Software Engineering,vol.27,no.1,
pp. 1–32, 2022.
[18] J. Cohen, “A coefficient of agreement for nominal scales,” Educational and Psychological Measurement, vol. 20, no. 1, pp. 37–46, 1960.
[19] GitHub Discussions: Copilot Category, https://github.com/community/community/
discussions/categories/copilot.
[20] A. N. Christopher, Interpreting and Using Statistics in Psychological Research.
SAGE Publications, 2017.
[21] K.-J. Stol, P. Ralph, and B. Fitzgerald, “Grounded theory in software engineering
research:Acriticalreviewandguidelines,”inProc.ofthe38thInt.Conf.onSoftware
Engineering (ICSE). ACM, 2016, pp. 120–131.
[22] B. G. Glaser, “The constant comparative method of qualitative analysis,” Social
Problems, vol. 12, no. 4, pp. 436–445, 1965.
[23] L. R. Hallberg, “The “core category” of grounded theory: Making constant comparisons,”International Journal of Qualitative Studies on Health and Well-being,vol.1,
no. 3, pp. 141–148, 2006.
[24] B. Zhang, P. Liang, X. Zhou, A. Ahmad, and M. Waseem, Dataset of the Paper:
Demystifying Practices, Challenges and Expected Features of Using GitHub Copilot,
2023, https://doi.org/10.5281/zenodo.8123302.
[25] GitHub Next — GitHub Copilot Labs,https://githubnext.com/projects/copilot-labs.
[26] Introducing GitHub Copilot X, https://github.com/features/preview/copilot-x.