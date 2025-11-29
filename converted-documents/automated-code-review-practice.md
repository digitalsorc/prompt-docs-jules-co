---
title: "Automated Code Review Practice"
original_file: "./Automated_Code_Review_Practice.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["llm", "rag", "react", "agents", "fine-tuning"]
keywords: ["code", "review", "pull", "automated", "comments", "reviews", "request", "our", "data", "developers"]
summary: "<!-- Page 1 -->


### Automated Code Review In Practice


### Umut Cihan∗, Vahid Haratian∗, Arda ˙Ic¸o¨z∗,

Mert Kaan Gu¨l†, O¨mercan Devran†, Emircan Furkan Bayendur†,

### Baykal Mehmet Uc¸ar†, Eray Tu¨zu¨n∗

∗ Bilkent University, Ankara, Tu¨rkiye
umut.cihan@bilkent.edu.tr, vahid.haratian@bilkent.edu.tr arda.icoz@bilkent.edu.tr, eraytuzun@cs.bilkent.edu.tr
† Beko, ˙Istanbul, Tu¨rkiye
mertkaan.gul@beko.com, omercan.devran@beko.com emircanfurkan bayendur@beko.com, baykal.ucar@beko.com
Abstract— "
related_documents: []
---

# Automated Code Review Practice

<!-- Page 1 -->


### Automated Code Review In Practice


### Umut Cihan∗, Vahid Haratian∗, Arda ˙Ic¸o¨z∗,

Mert Kaan Gu¨l†, O¨mercan Devran†, Emircan Furkan Bayendur†,

### Baykal Mehmet Uc¸ar†, Eray Tu¨zu¨n∗

∗ Bilkent University, Ankara, Tu¨rkiye
umut.cihan@bilkent.edu.tr, vahid.haratian@bilkent.edu.tr arda.icoz@bilkent.edu.tr, eraytuzun@cs.bilkent.edu.tr
† Beko, ˙Istanbul, Tu¨rkiye
mertkaan.gul@beko.com, omercan.devran@beko.com emircanfurkan bayendur@beko.com, baykal.ucar@beko.com
Abstract— Context: Code review is a widespread practice regular[4].Thecommonbenefitsoftheprocessareknowledge
among practitioners to improve software quality and transfer sharing, learning, defect identification, and code improvement
knowledge. It is often perceived as time-consuming due to the
[5], [6].
need for manual effort and potential delays in the development
To conduct a code review, developers spend time underprocess. Several AI-assisted code review tools (Qodo, GitHub
Copilot, Coderabbit, etc.) provide automated code reviews using standing other developers’ work and where it stands in the
large language models (LLMs). The overall effects of such tools overall project. The Open Source Software (OSS developers
in the industry setting are yet to be examined. self-reported an average review time of 6.4 hours per week
Objective: This study examines the impact of LLM-based for code review [7], whereas the Google case study reveals a
automated code review tools in an industry setting.
lower number with 3.2 hours [6]. The numbers suggest that
Method: The study was conducted within an industrial softdevelopers spend a considerable amount of time on reviews.
ware development environment that adopted an AI-assisted
code review tool (based on open-source Qodo PR Agent). 238 Due to developers’ workloads, developers often postpone
practitioners across ten projects had access to the tool. We codereviewtasks.Indoingso,developerspostponethemerge
focused our analysis on three projects, encompassing 4,335 pull ofcodechanges.InthesamecasestudyatGoogle,themedian
requests,ofwhich1,568underwentautomatedreviews.Ourdata
time for merge approval is under four hours, while for large
collection comprised three primary sources: (1) a quantitative
changesets,itisfivehours[6].Highermedianapprovaltimes
analysis of pull request data, including comment labels indicating whether developers acted on the automated comments, (2) are reported from various companies: 15.7 hours for Google
surveys sent to developers regarding their experience with the Chrome, 20.8 hours for Android at Google, 17.5 hours for
reviews on individual pull requests, and (3) a broader survey of AMD,14.7hoursforBing,19.8hoursforSQL,and18.9hours
22 practitioners capturing their general opinions on automated
for Office at Microsoft [8]. This variation in approval times
code reviews.
suggests differences across companies and projects. However,

### Results: 73.8% of automated code review comments were

labeled as resolved. However, the overall average pull request the actual costs of delays in critical code changes, which are
closure duration increased from five hours 52 minutes to eight not reflected in median or average statistics, could be more
hours 20 minutes, with varying trends observed across differ- detrimental. In a study of Microsoft developers, receiving
ent projects. According to survey responses, most practitioners
timelyfeedbackwascitedasthetopchallengeregardingcode
observed a minor improvement in code quality as a result of
review practices [5].
automated code reviews.
Conclusion: The LLM-based automated code review tool Automation can potentially shorten the time for code approvedusefulinsoftwaredevelopment,enhancingbugdetection, proval and reduce the burden of manual effort on developers.
increasing awareness of code quality, and promoting best prac- In this regard, several attempts have been made to automate
tices. However, it also led to longer pull request closure times
the code review process [9]–[19], focusing mainly on the
and introduced drawbacks such as faulty reviews, unnecessary
assignment of reviewers [20]. These efforts come from tools
corrections, and irrelevant comments. Based on these findings,
we discussed how practitioners can more effectively utilize that generate code reviews [10]–[12], predict the approval
automated code review technologies. of code changes [21], [22], and fix code according to code
Index Terms—code review, large language models, pull re- reviews [23], [24]. In our study, we focus on the automation
quests, AI-assisted code review, industry case study, code review
of code review generation.
automation
To generate code reviews, developers spend time understanding the code change, looking for mistakes, and detecting

## I. Introduction

performance bottlenecks or general deviations from coding
Code review is a quality assurance process, with different standards. There have been several attempts with pre-trained
adaptationsacrosstheindustry,thatinvolvesdeveloperscheck- models to provide code reviews [21], [22], [25]. With the
ing each others’ code changes [1]. Emerging as formal code introduction of ChatGPT [26], there have been considerable
inspections[2],codereviewhasevolvedandbecomealighter automation efforts to automate code review generation [27].
process often referred to as Modern Code Review (MCR) Several tools with code review capability were created, often
[3]. MCR is characterized by being informal, tool-based, and working with OpenAI’s LLMs such as GPT-4 [28], [29].
4202
ceD
82
]ES.sc[
2v13581.2142:viXra

<!-- Page 2 -->

Automated code review tools are increasingly used in the LLMs with human feedback [17], and LLM agents [18], [19].
industry [27]. However, there is a lack of empirical evidence The effectiveness of state-of-the-art code review automation
regarding their potential benefits. For example, the time saved has been investigated by Tufano et al. [20]. In their study,
through automated reviews could be offset by new problems Tufano et al. investigated their model based on a pre-trained
they introduce. Additionally, the financial benefits of reducing Text-To-Text Transfer Transformer (T5) model [11], [41],
developer effort may be negligible compared to the cost CommentFinder model using information retrieval techniques
of operating such tools. To address this research gap, we to recommend code reviews [9], CodeReview Model using
conducted a study aimed at answering the following research pre-trainingtechniques[10],aswellasChatGPT[26]without
questions: specifying the version they used. They found that ChatGPT
• RQ1: How useful are LLM-based automated code re- couldserveasacompetitivebaselineforimprovingcode,both
views in the context of the software industry? in direct code-to-code transformations and in generating code
• RQ2: How do LLM-based automated code reviews im- based on comments (comment-to-code). In contrast, ChatGPT
pact the pace of the pull request closure process? did not outperform the state-of-the-art in comment generation
• RQ3: How does the introduction of LLM-based auto- (code-to-comment).
mated code reviews influence the volume of human code Usage of LLMs and generative artificial intelligence for
review activities? codereviewgenerationhasattractedotherstudies.Davilaetal.
• RQ4: How do developers perceive the LLM-based auto- [27] conducted a grey literature review regarding the usage of
mated code review tools? generative artificial intelligence for code reviews and showed
how LLM-based tools like ChatGPT have been explored for
We collaborated with Beko, a multinational home applicode review.Fan et al. [14]explored the capabilitiesof LLMs
ancescompany,whosesoftwaredivisionadoptedanautomatic
on three code change-related tasks: code review generation,
code review tool based on the open-source Qodo (Formerlycommitmessagegenerationandjust-in-timecommentupdate.
CodiumAI) PR Agent [29] using GPT-4 Turbo model [30].

### They concluded that LLMs are promising for the tasks men-


### This tool provides automatic code review comments for each

tioned earlier. Watanabe et al. [42] investigated 229 review
pull request across 10 projects and 22 project repositories.
Ourdatacollectionprocessincludedthreesources.First,we comments from 179 GitHub projects that included ChatGPT
extracted data from the version control system and develop- conversation links. Their analysis revealed that 30.7% of the
ment platform Azure DevOps, which hosts the project reposi- reactionstoChatGPT’sanswerwerenegative,withdevelopers
tories.Thisdataencompassedpullrequestinformation,review often citing the lack of extra benefits. In 2024, Vijayvergiya
comments, review comment labels, and comparisons between et al. [15] from Google and the University of Washington
initial and final versions of pull requests. Developers were demonstratedtheirfindingsonthedevelopmentandlarge-scale
asked to label each review comment to indicate whether they industryimplementationofAutoCommenter.AutoCommenter
had implemented the suggestions into the code. Second, the is an LLM-backed automated code review system for four
authors received a short survey for each pull request. Lastly, programming languages (C++, Java, Python, and Go). Their
we conducted a broader survey involving 22 practitioners to findings suggest the feasibility of developing an end-to-end
gather their overall perceptions. automated code review system while achieving high end-user
acceptance.

## Ii. Relatedwork


### In this study, we aim to address the lack of longitudinal

Code reviews demand significant developer effort and time research on the impact of automated code review tools in
[5], [7]. These demands, along with the need for frequent software development. Unlike previous studies, our research
context switching, have driven the push towards automation examines the effects of a commercial LLM-based automated
[31]. The automation in code review is a well-investigated codereviewtool[29]inreal-worldindustrysettingsregarding
part of the research, where the majority of efforts tackle itsimpactondevelopmentartifactsanddeveloperperceptions.
the problem of reviewer assignment [32]–[40]. There is also Thisstudyaimstoprovidepractitionerswithvaluableinsights
considerableeffortbeingputintoothercodereviewaspects.In intowhetherandhowtoadoptanLLM-basedautomatedcode
2018, Gupta et al. [25] presented a model to match historical review tool.
reviews with code snippets using supervised deep learning. In
2019, a Convolutional Neural Network (CNN) based model

## Iii. Researchsettings

by Li et al. [22] and a framework utilizing CNN and LSTM In this study, we conducted an evaluative case study to
by Shi et al. [21] were presented to predict approvals of code assess the impact of LLM-based automated code reviews
changes. In 2022, Thontanunam et al. [24] presented a model in software development. We evaluated their effectiveness,
to modify the source code automatically during code review influence on the speed of pull request closures, and changes
processes. in the volume of human code reviews. This section presents
Inadditiontotheaforementionedefforts,severaltechniques ourresearchsettings.SectionIII-Aintroducesthestudyobject.
wereinvestigatedforautomationofcodereviewgeneration,in- SectionIII-Bpresentsthisstudy’sgoalandresearchquestions.
cludinginformationretrieval[9],pre-trainedmodels[10]–[12], Our study involves both quantitative and qualitative data
LLMs [13]–[15], LLM prompt fine-tuning [16], fine-tuning sources.SectionIII-Cdescribeshowwecollectedquantitative

<!-- Page 3 -->


### Fig.1. DataCollectionTimeline

data from the projects’ repositories. Section III-D describes
our qualitative data collection through surveys. Section III-E
describes our approach toward research questions.

### A. Study Object

We conducted our study within the software development

### Fig.3. FlowofPullRequestProcess

division of Beko, a multinational company. It operates in
the consumer durables and electronics sectors. The software

## Tablei

development division of Beko is responsible for developing PROJECTSINCLUDEDINOURSTUDY
customer-facing and employee-facing software with 238 prac-
Project Explanation # of Devel- Language
titioners. opers
Figure1outlinesBeko’sjourneytoimplementtheCodeRe- B2BE-commerce TypeScript,Java,

### Project 21

viewBot, starting with the investigation phase on 25th Au- #1 Portal JavaScript
gust 2023, driven by a need to enhance code quality and EnterpriseManagement HTML,JavaScript,

### Project 51


### Platform C#

efficiency. Beko evaluated several open-source projects, in- #2
cluding CodeRabbit [28], Qodo (Formerly CodiumAI) [29], CustomizableAI C#,HTML,

### Project 22 JavaScript

and pipeline extension tools like Reviewbot1, ChatGPT- SolutionsHub

## #3 Sql

CodeReview2, and Codereview.gpt3. After careful considera-

### The Beko was selected as the study object since they had

tion, Beko selected Qodo PR-Agent [29], for its high perforused the CodeReviewBot for a considerable time. The size of
manceandseamlessintegration.Theycustomizeditsfunctiontheir development teams (103 developers) and the diversity of
ality to meet their needs, and named it ”Code Review Bot”
projects (10 projects) employing the tool are other qualities
internally.Fortherestofthestudy,wewilluse”CodeReviewthat motivated us to select them. To avoid potential risks or
Bot” to enhance readability. The first pilot project launched
on 7th November 2023. By 5th June 2024, Beko had adopted unintended consequences with collecting real-world data, we
didnotassociateanyresultwithanindividualpractitioner,and

### CodeReviewBot across 10 projects and 22 repositories. On

24th May 2024, practitioners were informed that the commit the individual survey results were not shared with the authors
from Beko. Our data analysis is conducted on three of the
resolution policy was in place via an email campaign, and
20th September 2024 marked our study’s final data collection tenprojectsthatemployedCodeReviewBot.Thisisduetothe
early start of these three projects with the CodeReviewBot
date. In Figure 2 you can see an example comment from
(Project #1 7th November 2023, Project #2 13th November
CodeReviewBot.
2023 and Project #3 3rd April 2024). The other seven projects
adopted CodeReviewBot around June 2024; hence, they did
notaccumulateconsiderabledata.TableIprovidesinformation
regarding the three projects.

### B. Study Goal and Research Questions


### Ourstudyinvestigatestheimpactofautomatedcodereviews

insoftwaredevelopmentfrommultipleperspectives.Academ-
Fig.2. ExampleReviewofCodeReviewBot ically, it provides empirical data to understand the future
direction of modern code review and reveals the potential
CodeReviewBot utilizes the GPT-4-32K Model to provide of promising automated code review tools. For practitioners,
automatic code review comments for each pull request. The it is crucial to determine whether automated code reviews
toolcomplementsthecodereviewprocess;developerscanstill positively affect the development process. From a business
add their reviews. In Figure 3, the flow of the pull request standpoint, implementing such tools involves costs that their
processisdepicted.Thetoolworksonadiverseportfolioof22 benefits must justify. Quality-wise, automated code reviews
repositories spanning 10 distinct projects. These repositories should be expected to enhance rather than diminish the excontainedJava,JavaScript,C,HTML,SQL,C#andTypeScript isting code review process. Therefore, this study is a wellcode. motivatedandvaluableinvestigationforindustryprofessionals
and academics.
1https://github.com/reviewboard/ReviewBot
2https://github.com/anc95/ChatGPT-CodeReview Weaddressedthefollowingresearchquestionsbycollecting
3https://github.com/sturdy-dev/codereview.gpt data from the project repositories and surveys:

<!-- Page 4 -->

Research Question 1: How useful are LLM-based auto- better understand the data extraction process, we described
mated code reviews in the context of the software industry? the components illustrated in Figure 4.

### ThisresearchquestionassessesLLM-basedautomatedcode

reviews’ utility in software development. Specifically, we
seek to determine whether comments generated by automated
code review tools are effectively incorporated into code. This
depends on the usefulness of the automated reviews and the
developer’s reception of them.

### ResearchQuestion2:HowdoLLM-basedautomatedcode

reviews impact the pace of the pull request closure process?

### One of the main motivations for the automation is time

gains. With this research question, we examine the effect of
LLM-based automated code reviews on the pace of development. Specifically, we aim to determine whether integrating
automated code reviews accelerates the pull request closure
process. By analyzing this impact, we seek to understand

### Fig.4. DataCollectionOverview

whether LLM-based tools contribute to more efficient development workflows. 1) Initial Pull Request: A pull request is a mechanism for
Research Question 3: How does the introduction of LLM- introducing changes to the code base. Once a pull request
basedautomatedcodereviewsinfluencethevolumeofhuman is created, other developers are informed about the proposed
code review activities? changes.Theyaddtheirreviewcommentstonotifytheauthor,
Human code reviews require substantial effort. With the who is expected to make necessary changes based on the
introductionofLLM-basedautomatedcodereviews,assessing reviews. The pull request is accepted once the code reaches
how this affects the volume of human reviews is essential. acceptable quality and the changes are merged into the code
With this research question, we aim to determine whether au- base.
tomatedtoolsleadtoanincreaseordecreaseinhumanreview Pullrequestauthorsreceiveautomaticreviewcommentsand
activities. We aim to understand how automation impacts the other reviewers’ comments in our case. Our study considers
effort and workload associated with human code reviews. 4335pullrequests,ofwhich1568werecreatedafteradopting
Research Question 4: How do developers perceive the automated code review.
LLM-based automated code review tools? 2) PullRequestComments: Pullrequestcommentsserveas
Developersareimportantactorsinthecodereviewprocess. theartifactsofthecodereviewprocess.Humanreviewersadd
Theirperceptionoftheautomatedcodereviewtoolsiscritical their reviews in the form of comments. The CodeReviewBot
forrealizingtheexpectedbenefits.Withthisresearchquestion, addeditsreviewsasseparatecomments.Weanalyzedthepull
weaimtoanalyzehowdevelopersperceivethecommentsthey request comments regarding volume and time, who generated
receive and the general process by triangulating our different them, and how pull request authors benefited.
data sources. This comprehensive assessment will provide The presence of a comment does not mean it was taken
insights into developers’ attitudes toward automation and its intoconsideration.Toinvestigatewhetherpullrequestauthors
role in the code review process. benefitedfromthereviewcomments,weconfiguredarequired
We utilized qualitative and quantitative data to achieve our comment resolution policy [43]. This system requires authors
research objectives and address our questions. The interaction to indicate how they handled the pull request comments.
between practitioners and automated code reviews is a key Unfortunately,thecommentresolutionpolicyputinplaceafter
focus of our study, which required qualitative data collection. CodeReviewBot, so we do not have the same data from prior
Toachievethis,wedevelopedapullrequestsurveyandagen- pullrequests.TableIIpresentsthecommentstatusoptionsfor
eral opinion survey and implemented a mandatory comment each review comment and their explanation according to the
resolution policy requiring developers to label how comments comment resolution policy.
were addressed. For quantitative data, we opted for repository 3) Closed Pull Request: The code changes proposed in the
mining, which offers valuable insights into real-world usage initial pull request may change with the review comments.
by systematically recording digital activities. We triangulated This is an expected event if the reviews point out problems.
our findings from the surveys and comment resolution labels The code changes are reflected as additional commits. The
byanalyzinghistoricalcommitdata,pullrequests,andrelated pull request is either accepted or rejected. The practitioners at
comments. Figure 4 depicts our data collection overview. Bekoarenotusingrejectionasaqualityassurancemechanism.
Instead, they use rejection when the change is considered

### C. Data Collection From Azure DevOps

unnecessary or untimely. Hence, we did not treat acceptance
We collected data from the project’s version control system as a quality indicator but as categorical data.
(”Azure DevOps”). This data includes pull request informa- 4) Data Extraction and Analysis: Our data analysis starts
tion, review comments, and commits to pull requests. To with extracting raw data from the Azure DevOps server using

<!-- Page 5 -->

TABLEII review comments and received a survey of three questions.
COMMENTRESOLUTIONPOLICYINAZUREDEVOPS These surveys are our second data source. The first two
questions have one-to-five scale answers, and the last one is

### Status Explanation

Active This is the default status for new comments. open-ended. We included code review survey questions in the
The corresponding comment is being analyzed replication package.

### Pending

or waiting for some other thing. 2) GeneralOpinion Surveys: Wecreated ageneralopinion
Resolved The corresponding comment is successful and survey and received responses from 22 developers who conits suggestion was implemented.
tributed to the three projects within our research scope. These

### The corresponding comment is faulty or cannot

Won’t fix practitioners had different years of experience and positions
be implemented.
The corresponding comment was not implemented in the organization. We provide information regarding the

### Closed

for some other reasons than ”Won’t Fix”. participants in Table III. The survey questions focused on the
impact of automated code reviews on developers and their
the API. We created a data scheme that allowed us to store perspectives.Weincludedgeneralopinionsurveyquestionsin
information regarding projects, repositories, commits, pull the replication package.
requests, and pull request comments in a relational database.
We used the data scheme to store the API responses. TABLEIII
Our next step was to preprocess the data to ensure its SURVEYPARTICIPANTS
integrity and accuracy. Firstly, we converted the tables into

### SurveyParticipants

CSV files, uploaded the data using the pandas library4, and ExperienceinSoftwareDevelopment NumberofParticipants
createdscriptstoextracttherelevantmetrics.Thefirstproblem 0-2 4
2-5 9
we noticed was the high number of active comments, which
5-10 6
should not have been the case for the comment resolution 10+ 3
policy.Wemanuallyexaminedpullrequestsandobservedthat PositionatBeko NumberofParticipants
some pull requests were closed before the CodeReviewBot IndividualContributor 16

### Lead/Manager 6

could comment. The comments created by the tool arrived

### TotalPractitioners 22

after the pull request was closed, meaning they did not need
to be resolved. We reviewed the time it took to merge the

### E. Approach Towards Research Questions

PRs and, using elbow evaluation, identified a threshold that
covers93%ofthePRs.Wethenappliedthisfiltertotheentire Since our research questions have multiple aspects, we
historyforafairevaluation.Finally,wemanuallyremovedthe relied on findings from multiple data sources. We used the
remaining 7% to eliminate all outliers. reviewcommentlabels,commitstopullrequestsafterreviews,
The second issue we encountered was the high number of and general opinion survey question answers to establish a
comments from some developers. Two developers had unrea- multi-aspect evaluation for the first research question. We exsonablyhighercommentsthanotherdevelopers.Weexamined tracted pull request closure duration data from Azure DevOps
theircommentsandrealizedthattheirAzureDevOpsaccounts toanswerthesecondresearchquestion.Inthegeneralopinion
wereusedfordifferentsoftwarebots,suchasSonarQube5.We survey, we asked the practitioners whether automated code
also excluded these accounts from our study. reviews affected the development pace.
Lastly, we observed that many comments had unknown WeextractedthenumberofhumancodereviewsfromAzure
comment resolution labels due to being deleted or including DevOps for the third research question. We asked developers
the pull request description generated by CodeReviewBot. whether they could manually generate the same comments in
For that, we excluded such comments. On top of that, the the survey. The last research question is centered around the
comment resolution policy was only active when the pull developer and pull request survey. Our data analysis scripts,
request targeted the repository’s main branch. For that, we survey questions, and results are shared in our replication
excluded pull requests targeting other branches except for package6.
the main branch. The data cleaning process involved several

## Iv. Results

collaborative sessions with both non-practitioner and Beko
participants, after which we confirmed the dataset was free A. Code Review Surveys
from corruption. Ultimately, we analyzed 4,335 pull requests, During our study, we collected ratings for 38 pull requests
of which 1,568 were subject to automated reviews. thatreceivedautomatedcodereviews.Thepullrequestauthors
werealsoaskedtofilloutasurveyconsistingoftwomultiple-

### D. Data Collection From Surveys

choicequestionsandoneopen-endedquestion,andtenpeople
1) Code Review Surveys: With each pull request, the au- went on to do so.
thorswereaskedtogiveazerotofiveratingfortheautomated Theaverageratingfortheautomatedreviewcommentswas
3.46, with a standard deviation of 1.79. Figure 5 depicts the
4https://pandas.pydata.org/pandas-docs/stable/index.html#
5https://www.sonarsource.com/products/sonarqube/ 6https://doi.org/10.5281/zenodo.13917481

<!-- Page 6 -->

ratingsforthedifferentprojectsandtheoverallrating.Thereis B. General Opinion Surveys
aconsiderabledifferencebetweenratingsacrossprojects,with
averagesof4.04,2.72,and3.00forProject#1,Project#2,and We sent a survey consisting of eight questions to the
Project#3,respectively.Thismightindicateadifferenceinthe developers who contributed to the projects. We received 23
qualityofreviewsconcerningdifferentprojectconditions,orit responses, with 22 respondents consenting to be involved in
may be due to the differences between developers in different publishedresults.Thissurveywascreatedtocollecttheoverall
projects. perceptions of developers.
The survey that we sent to the authors contained three Thesurveycomprisedsixmultiple-choicequestionsandtwo
questions. The first two questions were regarding whether open-ended questions. Figure 7 and 8 present the results. The
authors found the reviews agreeable and how they found the first question addressed the impact of automated code reviews
presentation of the review comments. The third question was on development speed. Eight developers perceived a minor
open-ended and asked for additional feedback. improvement in the pace of development due to automated
code reviews, while four perceived no effect, three perceived
aminordeterioration,andtwoperceivedamajorimprovement.

### Fig.5. AutomatedCodeReviewRatingsfromCodeReviewSurveys

Unfortunately,wedidnotreceivemanyanswersforthethird Fig.7. GeneralOpinionSurveyResponses(Questions1-3)
question. Most of the answers were simple remarks such as
”Great.” Ten practitioners answered the first two questions, The second question focused on knowledge sharing. Nine
and we reported on the responses in Figure 6. Eight people practitionersperceivednoeffectonknowledgesharingamong
answered with ”5” when asked how agreeable they found developers.Atthesametime,theeightdevelopersperceiveda
the comments, while nine answered with ”5” when asked positiveimpact.Thethirdquestionexploredcodequality,with
how well-presented they found the comments. One person mostrespondents(14)suggestingthatautomatedcodereviews
answered both questions with ”1”. There is a difference contributetoaminorimprovementintheoverallqualityofthe
between the number of responses for ratings and surveys. code.
Since the survey required extra effort, dissatisfied developers
mighthavefeltlessmotivatedtocompletethesurvey.Overall,
the ratings and the pull request survey show developers found
the comments agreeable and well-presented.

### Fig.6. CodeReviewSurvey

Fig.8. GeneralOpinionSurveyResponses(Questions4-6)

<!-- Page 7 -->

The fourth question examined the relevance of the comments generated by the automated code reviews to the pull
request. With nine respondents rating the relatedness as ”4”
and seven rating the relatedness as ”3”, results indicate that
most practitioners found the automated comments related to
pull requests.

### Thefifthquestionaskedwhetherdeveloperscouldmanually

identifytheissuestheautomatedcodereviewspointedoutwith
”1,” meaning they could not manually identify none, and ”5,”
meaningtheycouldidentifyallofthem.Tenrespondentsrated
this question ”3,” while six rated it ”2”.
The sixth question addressed the importance of the issues
highlightedbytheautomatedreviews.Eightrespondentsrated
this question ”3,” while six rated it ”2”. The dispersion of the
ratings shows that practitioners have different views. Fig.10. CommitsAfterCodeReviews
requests may have been opened as drafts, with new commits

### C. Analysis of the Azure DevOps Data

addedafterward.Adifferencebetweenthenumberofcommits
after CodeReviewBot and the comments with the ”Resolved”
label is expected. Since pull requests receive more than one
comment and commits are made for the pull request, the
”Resolved” labeled comments should be more than the commits. However, developers might also disregard the expected
labeling policy and use ”Resolved” instead of ”Closed” or
”Won’tFix.””Closed”referstocommentsthatwerenotfaulty
but were not implemented for some other reason.

### RQ1: How useful are LLM-based automated code

reviews in the context of the software industry?

### Our analysis showed that 73.8% of the comments

suggested by CodeReviewBot were accepted and implemented by developers, highlighting the bot’s significant impact on the code review process. Moreover,

### Fig.9. CommentLabelsonMergedPRs

88 commits were made after CodeReviewBot and be-
1) Comment Labels: Within our analysis, we extracted fore human reviewers’ comments, indicating proactive
4408 comments by CodeReviewBot. Since the comment res- changes based on the bot’s suggestions. Most survey
olution policy was enforced sometime after the CodeReview- respondents also perceived an improvement in code
Bot, we had to filter out comments before the policy intro- qualityusingCodeReviewBot.Therefore,weconclude
duction and the currently active or pending comments. After that LLM-based automated code reviews are highly
thefiltering,weexamined1408CodeReviewBotcommentson useful in this company’s context.
merged pull requests. We reported the status of comments for
each project in Figure 9. 73.8% of the comments are labeled 3) Pull Request Closure Durations: The overall average
as”Resolved,”while21.3%arelabeledas”Won’tFix.”When pull request closure duration increased from five hours and
we compare the results across projects, we see a significant 52 minutes before the introduction of CodeReviewBot to
difference for Project #1 and Project #3 with 55% and 90% eight hours and 20 minutes after its implementation. The
of comments labeled as ”Resolved.” independent samples t-test indicated this overall increase was
2) Commits on Pull Requests: As a measure of change statistically significant (p-value < 0.001). We observed differcaused bythe codereview process,pull requests receivecom- ent trends across projects as depicted in Figure 11.
mitsaftertheyreceivecomments.Weanalyzedthesecommits Project#1showedasignificantincreaseinclosureduration,
for the pull requests after CodeReviewBot’s implementation. rising from two hours and 48 minutes to four hours and
The results are shown in Figure 10. Pull requests received 38 minutes after CodeReviewBot was introduced. The t-test
88 commits after CodeReviewBot’s comments but before indicated this increase was statistically significant (p-value <
human comments. After the human reviewer had commented, 0.001).Project#2experiencedasignificantdecreaseinclosure
the pull requests received 69 commits. It should be noted duration, dropping from six hours and six minutes to three
that authors may also act upon CodeReviewBot’s comments hours and seven minutes. The analysis yielded a statistically
after the human reviewer’s comments. Conversely, some pull significant result (p-value < 0.001). Project #3 observed an

<!-- Page 8 -->


### After introducing CodeReviewBot, human comments per

pull request significantly increased in Project #1 (from 0.14
to 0.29, p-value < 0.05), significantly decreased in Project #2
(from0.37to0.08,p-value<0.05),andremainedstatistically
unchanged in Project #3 (from 0.50 to 0.49, p-value ≥ 0.05).
RQ3: How does the introduction of LLM-based automated code reviews influence the volume of human
code review activities?

### The average number of human comments decreased

from 0.31 to 0.28 with the introduction of CodeReviewBot.However,accordingtoourPoissonregression
analysis, this decrease was not statistically significant.
Fig. 11. Pull Request Closure Durations Before and After CodeReviewBot
(H:MM) Additionally, the impact of LLM-based automated
codereviewsonhumanrevieweractivityvariedacross
increase in closure duration from 20 hours and 22 minutes
different projects, potentially influenced by project
to 30 hours and 51 minutes after the bot’s introduction. The
dynamics and team practices.
statisticaltestshowedthisincreasewasstatisticallysignificant
(p-value < 0.001).

### RQ2: How do LLM-based automated code reviews

impact the pace of the pull request closure process?

### D. General Opinion Survey Open-Ended Questions


### Our results indicated a significant slowdown in the

pull request closure process. This slowdown could be The general opinion survey had two questions about the
explained by developers needing to address additional advantages and disadvantages of automated code review. We
comments from the bot and those from human re- received20legitimateanswers,withtwonon-usefulresponses
viewers.Theimpactonclosuredurationsvariedacross (blankspaces).Asignificantproportionofparticipants(13/20)
different projects, suggesting that project-specific con- remarked on advantages regarding code quality improvement
ditions play a critical role in determining the effects. and the maintenance of coding standards. Some respondents
highlighted the enhancements in the review process, such as
shortening the review process and helping spot overlooked
code smells and potential bugs. The auto-generated code
descriptions were cited as beneficial in expediting the review
process. Other notable advantages included providing suggestions for improvement and enhancing awareness of best
practices.
RQ4: How do developers perceive the LLM-based
automated code review tools?
Some practitioners voiced concerns that out-of-scope
orirrelevantsuggestionscouldslowdownreviewsand
createdistractions.Somepractitionerswereconcerned
thatautomatedcodereviewsmissedcriticalissuesthat
a human reviewer would catch. One respondent raised
a significant concern about automated code review

### Fig.12. AverageNumberofHumanReviewerComments

potentially altering the context of pull requests, which
4) Human Reviewer Comments: Overall, human reviewers could introduce severe bugs if changes are applied
left an average of 0.31 comments per pull request before without careful consideration. Despite these drawdeployingCodeReviewBot,whichdecreasedto0.28afterward, backs, the majority of developers perceive automated
as shown in Figure 12. The Poisson regression analysis code review tools as beneficial for improving code
indicated that this overall decrease was not statistically sig- quality and maintaining coding standards, notably by
nificant (p-value ≥ 0.05). For comparison, CodeReviewBot detectingqualityproblemsandprovidingimprovement
left a higher average of 3.65 comments per pull request. The suggestions.
statistical analysis revealed different trends across projects:

<!-- Page 9 -->

V. DISCUSSION severe bugs to go unnoticed. Practitioners should examine

### LLM-based automated code review tools extensively before

A. Does LLM-based automated code review considerably imwidespread adoption. Organizational awareness of the limitaprove software development activity?
tions should be established, and necessary precautions should
ImplementinganLLM-basedautomatedcodereviewtoolis be taken.
asubstantialorganizationaldecisionthatinvolvesbothbenefits Unnecessary Review Comments: The results from the
and costs. While such tools incur expenses—for instance, comment resolution labels show that 26.2% of the tool
in our study, the CodeReviewBot used an average of 3,937 comments were not acted upon as they were labeled with
tokens per pull request at a cost of 0.48$ — they also require ”Won’tFix”or”Closed”.Thesecommentscouldbetootrivial,
developers to invest time in addressing review comments. unrelated or not a problem for the context of the pull request.
The comment labels assigned by pull request authors In any way, developers spend time on them. The survey
showed that 73.8% of the comments were addressed by the respondents also cited this problem. One respondent in the
author.Additionally,weobservedthat88commitsweremade general opinion survey said, ”It also makes suggestions that
aftertheCodeReviewBot’sreviewsbeforehumanreviews,sig- fix code blocks that are not in the scope of the task,” and
nifying that the automated reviews affected the pull requests. another said, ”Sometimes the mistakes it thinks it finds are
Our survey of developers revealed that 68.8% perceived a not mistakes at all.”
minor improvement in the code quality after CodeReviewBot. EarlyIdentificationofBugs:Thesurveyshowedthatearly
According to our survey results, practitioners consider issues identification of bugs is an advantage of the automated code
pointed out by CodeReviewBot important and related to the review. One respondent in the general opinion survey said ”It
respective pull requests. This further supports the usefulness makes finding code defects more easy. Developers can see
of LLM-based automated code reviews. their mistakes fast.” Respondents also highlighted the tool’s
Ontopofusefulnessforcodequality,codereviewsarealso ability to detect typos and forgotten test code. Another said,
helpful for knowledge sharing [5]. Within our general opin- ”very effective in detecting overlooked code smells”. These
ion survey, we asked practitioners whether CodeReviewBot remarks show us how the tool can improve code quality.
affected knowledge-sharing. Most respondents cited no effect,
while no respondent pointed to a negative impact. C. Implications to Researchers
One of the cited benefits of automated code review is its Effectiveness of LLM-Based Tools: This study provides
potential to save time and developer effort [31]. To explore valuable empirical evidence on the effectiveness of LLM-
this, we analyzed the durations for pull request closures. based automated code review tools in real-world industry
Althoughweobservedanoverallincreaseinclosuretimes,this settings. The positive reception of developers and the percentcouldbeattributedtoauthorsspendingextratimefixingissues age of comments accounted for in the pull requests (73.8%)
highlighted by the automated reviewer bot. The trends varied suggest that LLMs can enhance the code review process. One
significantly across different projects, suggesting that devel- respondent in the general opinion survey said, ”It improved
opers were actively engaging with the automated feedback, the awareness of the team about code quality”. This remark
whichmayhaveextendedtheclosuretimesbutpotentiallyled suggests that the tool also has effects beyond code review
to higher code quality. Furthermore, our analysis showed that practice.
the number of human review comments per pull request did Human-AI Interaction Dynamics: Integrating automated
notdecreasesignificantlyafterintroducingtheautomatedtool. reviews into the code review process introduces new dynam-
This suggests that while developers invested additional effort ics in human-AI interaction. One of the findings was the
to address automated comments, it did not replace the need frustration caused by recursive reviews, with one respondent
for human reviews. Consequently, we did not find conclusive saying, ”With each fix, a new review is generated. However,
evidencesupportingconsistenttimeoreffortsavingsasaresult after the initial review, subsequent comments on revised pull
of implementing the automated code review tool. requestsoftenbecomeredundantandunhelpful.”.Researchers
Our findings suggest that automated code review can mod- caninvestigatefactorsinfluencingdevelopertrust,satisfaction,
erately improve software development activity. The decision and reliance on automated reviews, leading to more humanto implement such a tool should still be considered carefully. centered design improvements in these tools.
The observed benefits within our study might be hindered by

## Vi. Threatstovalidity

existingcodereviewhabitsorotherqualityassuranceactivities
in place. A. Construct Validity
Our data collection process involves collecting data from

### B. Implications to Practitioners

respondents through survey answers and comment resolution
Over-reliance on automated code reviews: One respon- labels. These data entries are subject to misinterpretation.
dent in the general opinion survey said, ”It may create bias To mitigate this threat to validity, extra effort was put into
so reviewers may ignore by saying that if any other issue explaining the expectations from the respondents. We also
exists, the bot would have written it.” This over-reliance on thoroughly reviewed the questions with multiple reviewers to
automation can be harmful to the organization by allowing rephrase potentially confusing and complicated language.

<!-- Page 10 -->


### B. Internal Validity D. Conclusion Validity

This study might have led to different results in a different

### Some authors of this paper are part of Beko’s software

company setting. We cannot account for the many changing
development organization. Specifically, one of the authors is
conditions to reach statistical conclusions; therefore, we conin a managerial position in the organization. This introduces
sideredacasestudythemostappropriateapproach.Amultiple
the possibility of biases. For having a neutral stance, the
case study examination using our methodology would be
results and discussions in this paper were created by the nonrequired to reach definitive conclusions. Given the challenges
practitioner authors.
of conducting such a comprehensive study, we limited our

### We acknowledge that the mandatory comment resolution

scope and did not aim for statistical generalizations.
policy could be considered time-consuming for practitioners
because they do not provide reliable comment resolution VII. CONCLUSION
labels. To account for this threat, we triangulated our data

### In this study, we conducted an evaluative case study within

sources to come to conclusions. For example, we used comthe software development division of Beko, a multinational
ment labels alongside pull request change information to see
company,focusingonautomatedcodereviews.AnLLM-based
whether they agreed to a certain extent.
automated code review tool, based on the open-source Qodo
Ourdatacollectioniscenteredaroundsummer.Bekopracti- PR-Agent[29],wasadoptedacrosstenprojects.Wenarrowed
tionersmentionedthatmoredevelopersareonvacationduring our research scope to three of these projects, selected based
the summer, which decreases productivity and development on their longer duration of tool usage.
pace. For this matter, we acknowledge that our conclusions Ourfindingssuggestthatthetoolwaseffective,with73.8%
are subject to seasonality. of the comments being acted upon. Additionally, most devel-
The projects examined in this study are real projects that opers reported a minor improvement in code quality in the
commenced well before the research began. We did not survey and no deterioration in knowledge sharing. Regarding
associate any results with individual practitioners to avoid pull request closure times, there was a statistically significant
unintended effects and ethical concerns. As a result, the prac- increase between the average times of five hours and 52
titioners involved in the projects had no incentive to behave minutesbeforeandeighthoursand20minutesafterthetool’s
differently since the analysis was conducted independently introduction.Acrossprojects,thereweredifferenttrends,with
afterward. oneproject’spullrequestclosuredurationdeclining.Addition-
Since the pull request authors the same pull request survey ally, there was no significant change in the number of human
repeatedly,weconsiderthattheymightbecomefrustratedand code reviews before and after the tool’s implementation.
respond carelessly. To avoid this decline in engagement, we Since developers are the primary users interacting with
decided to limit the survey to three questions. the tool, we examined their perceptions of automated code
reviews.Thesurveyrevealedthatpractitionerscommonlyper-
Our quantitative data analysis relies on the integrity of data
ceived the issues identified in automated reviews as important
in Azure DevOps. Corruptions in the database could impact
and relevant to the pull requests. Participants noted several
our results. To mitigate such corruption, we conducted joint
advantages contributing to code quality, including faster bug
data cleaning sessions where we discussed the quality of the
detection, eliminating code smells, increased awareness of
data. We identified two accounts involved in the projects that
codequality,andthepromotionofstandardizedbestpractices.
were used as bot accounts for a certain time. We removed
The disadvantages included suggestions for out-of-scope code
the comments made by those accounts. We acknowledge that
changes and occasional misaligned recommendations that disthosecommentsmightincludehumancomments,thoughmost
tract developers and slow down the development. There were
were from bots.
also concerns about the downsides of potential over-reliance
Although the ”Active” and ”Pending” comments would
on automated systems.
not allow the pull request to be closed, we observed that
Our study revealed that automated code reviews can possome automated comments arrived after the pull request was
itively impact software development; however, some uninclosed. These comments were mostly left as active, and we
tended effects and disadvantages were also identified. Practidisregarded them in our analysis.
tionerscanusetheseinsightstomakemoreinformeddecisions
on the implementation and use of LLM-based automated
C. External Validity code review tools. We aim to replicate our study with different software development companies to account for inter-
Our study was conducted with a certain automated code organizational differences in our future work.
review tool (Qodo PR Agent [29]) based on a certain LLM
(GPT-4 32k[30]). Since we usedthis specific tooland model,

## Viii. Acknowledgements

we acknowledge that other LLMs and automated code review This work has been supported the ITEA4 GENIUS
tools might exhibit different behavior. Therefore, further re- project, which has been funded by the national
search is needed to determine if other LLMs would behave in funding authorities of the participating countries:
a comparable manner. https://itea4.org/project/genius.html

<!-- Page 11 -->

REFERENCES [20] R. Tufano, O. Dabic´, A. Mastropaolo, M. Ciniselli, and G. Bavota,
“Codereviewautomation:Strengthsandweaknessesofthestateofthe
[1] T. Baum, O. Liskin, K. Niklas, and K. Schneider, “A faceted classifi- art,” IEEE Trans. Softw. Eng., vol. 50, no. 2, p. 338–353, Jan. 2024.
cation scheme for change-based industrial code review processes,” in [Online].Available:https://doi.org/10.1109/TSE.2023.3348172
2016 IEEE International Conference on Software Quality, Reliability [21] S.-T. Shi, M. Li, D. Lo, F. Thung, and X. Huo, “Automatic code
andSecurity(QRS),2016,pp.74–85. review by learning the revision of source code,” Proceedings of
[2] M.E.Fagan,“Designandcodeinspectionstoreduceerrorsinprogram the AAAI Conference on Artificial Intelligence, vol. 33, no. 01, pp.
development,”IBMSystemsJournal,vol.15,no.3,pp.182–211,1976. 4910–4917, Jul. 2019. [Online]. Available: https://ojs.aaai.org/index.
[3] N.DavilaandI.Nunes,“Asystematicliteraturereviewandtaxonomy php/AAAI/article/view/4420
of modern code review,” Journal of Systems and Software, vol. 177, [22] H.-Y. Li, S.-T. Shi, F. Thung, X. Huo, B. Xu, M. Li, and
p. 110951, 2021. [Online]. Available: https://www.sciencedirect.com/ D. Lo, “Deepreview: Automatic code review using deep multiscience/article/pii/S0164121221000480 instance learning,” in Advances in Knowledge Discovery and Data
[4] A. Bacchelli and C. Bird, “Expectations, outcomes, and challenges of Mining: 23rd Pacific-Asia Conference, PAKDD 2019, Macau, China,
moderncodereview,”in201335thInternationalConferenceonSoftware April 14-17, 2019, Proceedings, Part II. Berlin, Heidelberg:
Engineering(ICSE),2013,pp.712–721. Springer-Verlag, 2019, pp. 318–330. [Online]. Available: https:
[5] L. MacLeod, M. Greiler, M.-A. Storey, C. Bird, and J. Czerwonka, //doi.org/10.1007/978-3-030-16145-3 25
“Codereviewinginthetrenches:Challengesandbestpractices,”IEEE [23] M.Tufano,J.Pantiuchina,C.Watson,G.Bavota,andD.Poshyvanyk,
Software,vol.35,no.4,pp.34–42,2018. “Onlearningmeaningfulcodechangesvianeuralmachinetranslation,”
[6] C. Sadowski, E. So¨derberg, L. Church, M. Sipko, and A. Bacchelli, CoRR, vol. abs/1901.09102, 2019. [Online]. Available: http://arxiv.org/
“Moderncodereview:Acasestudyatgoogle,”inInternationalConfer- abs/1901.09102
ence on Software Engineering, Software Engineering in Practice track [24] P.Thongtanunam,C.Pornprasit, andC.Tantithamthavorn,“Autotrans-
(ICSESEIP),2018. form: Automated code transformation to support modern code review
[7] A. Bosu and J. C. Carver, “Impact of peer code review on peer process,”inProceedingsofthe44thinternationalconferenceonsoftware
impression formation: A survey,” in 2013 ACM / IEEE International engineering,2022,pp.237–248.

### SymposiumonEmpiricalSoftwareEngineeringandMeasurement,2013,

[25] A. Gupta and N. Sundaresan, “Intelligent code reviews using deep
pp.133–142.
learning,” in Proceedings of the 24th ACM SIGKDD International
[8] P. C. Rigby and C. Bird, “Convergent contemporary software peer ConferenceonKnowledgeDiscoveryandDataMining(KDD’18)Deep
review practices,” in Proceedings of the 2013 9th Joint Meeting on LearningDay,2018.
Foundations of Software Engineering, ser. ESEC/FSE 2013. New
[26] OpenAI, “Chatgpt,” https://www.openai.com/chatgpt, 2023, accessed:
York, NY, USA: Association for Computing Machinery, 2013, p.
2024-04-28.
202–212.[Online].Available:https://doi.org/10.1145/2491411.2491444
[27] N.Davila,J.Melegati,andI.Wiese,“Talesfromthetrenches:Expec-
[9] Y. Hong, C. Tantithamthavorn, P. Thongtanunam, and A. Aleti,
tations and challenges from practice for code review in the generative
“Commentfinder: a simpler, faster, more accurate code review
aiera,”IEEESoftware,vol.PP,pp.1–8,012024.
comments recommendation,” in Proceedings of the 30th ACM Joint
[28] “What is coderabbit?” May 2023. [Online]. Available: https://docs.
European Software Engineering Conference and Symposium on the
coderabbit.ai/
Foundations of Software Engineering, ser. ESEC/FSE 2022. New
[29] “Codium-ai/pr-agent,” September 2024. [Online]. Available: https:
York, NY, USA: Association for Computing Machinery, 2022, p.
//github.com/Codium-ai/pr-agent
507–519.[Online].Available:https://doi.org/10.1145/3540250.3549119
[10] Z. Li, S. Lu, D. Guo, N. Duan, S. Jannu, G. Jenks, D. Majumder, [30] J.Achiam,S.Adler,S.Agarwal,L.Ahmad,I.Akkaya,F.L.Aleman,
J.Green,A.Svyatkovskiy,S.Fu,andN.Sundaresan,“Automatingcode D. Almeida, J. Altenschmidt, S. Altman, S. Anadkat et al., “Gpt-4
reviewactivitiesbylarge-scalepre-training,”2022. technicalreport,”arXivpreprintarXiv:2303.08774,2023.
[11] R.Tufano,S.Masiero,A.Mastropaolo,L.Pascarella,D.Poshyvanyk, [31] R. Tufano, L. Pascarella, M. Tufano, D. Poshyvanyk, and G. Bavota,
and G. Bavota, “Using pre-trained models to boost code review “Towards automating code review activities,” in Proceedings of
automation,” CoRR, vol. abs/2201.06850, 2022. [Online]. Available: the 43rd International Conference on Software Engineering, ser.
https://arxiv.org/abs/2201.06850 ICSE ’21. IEEE Press, 2021, p. 163–174. [Online]. Available:
[12] L.Li,L.Yang,H.Jiang,J.Yan,T.Luo,Z.Hua,G.Liang,andC.Zuo, https://doi.org/10.1109/ICSE43902.2021.00027
“Auger: Automatically generating review comments with pre-training [32] W. H. A. Al-Zubaidi, P. Thongtanunam, H. K. Dam,
models,”2022. C. Tantithamthavorn, and A. Ghose, “Workload-aware reviewer
[13] J. Yu, P. Liang, Y. Fu, A. Tahir, M. Shahin, C. Wang, and Y. Cai, recommendation using a multi-objective search-based approach,”
“Security code review by large language models,” 2024. [Online]. in Proceedings of the 16th ACM International Conference on
Available:https://arxiv.org/abs/2401.16310 Predictive Models and Data Analytics in Software Engineering,
[14] L. Fan, J. Liu, Z. Liu, D. Lo, X. Xia, and S. Li, “Exploring the ser. PROMISE 2020. New York, NY, USA: Association for
capabilities of llms for code change related tasks,” 2024. [Online]. Computing Machinery, 2020, p. 21–30. [Online]. Available:
Available:https://arxiv.org/abs/2407.02824 https://doi.org/10.1145/3416508.3417115
[15] M. Vijayvergiya, M. Salawa, I. Budiselic´, D. Zheng, P. Lamblin, [33] S. Asthana, R. Kumar, R. Bhagwan, C. Bird, C. Bansal, C. Maddila,
M. Ivankovic´, J. Carin, M. Lewko, J. Andonov, G. Petrovic´ et al., S. Mehta, and B. Ashok, “Whodo: automating reviewer suggestions
“Ai-assisted assessment of coding practices in modern code review,” at scale,” in Proceedings of the 2019 27th ACM Joint Meeting on
inProceedingsofthe1stACMInternationalConferenceonAI-Powered European Software Engineering Conference and Symposium on the
Software,2024,pp.85–93. Foundations of Software Engineering, ser. ESEC/FSE 2019. New
[16] C. Pornprasit and C. Tantithamthavorn, “Fine-tuning and prompt York, NY, USA: Association for Computing Machinery, 2019, p.
engineeringforlargelanguagemodels-basedcodereviewautomation,” 937–945.[Online].Available:https://doi.org/10.1145/3338906.3340449
Information and Software Technology, vol. 175, p. 107523, 2024. [34] J. Jiang, D. Lo, J. Zheng, X. Xia, Y. Yang, and L. Zhang, “Who
[Online]. Available: https://www.sciencedirect.com/science/article/pii/ should make decision on this pull request? analyzing time-decaying
S0950584924001289 relationships and file similarities for integrator prediction,” Journal of
[17] M. Nashaat and J. Miller, “Towards efficient fine-tuning of language SystemsandSoftware,vol.154,pp.196–210,2019.[Online].Available:
models with organizational data for automated software review,” IEEE https://www.sciencedirect.com/science/article/pii/S0164121219300962
TransactionsonSoftwareEngineering,pp.1–14,2024. [35] H.Ying,L.Chen,T.Liang,andJ.Wu,“Earec:Leveragingexpertiseand
[18] D. Tang, K. Kim, Y. Song, C. Lothritz, B. Li, S. Ezzini, authorityforpull-requestreviewerrecommendationingithub,”in2016
H. Tian, J. Klein, and T. F. Bissyande´, “Codeagent: Collaborative IEEE/ACM3rdInternationalWorkshoponCrowdSourcinginSoftware
agents for software engineering,” 2024. [Online]. Available: https: Engineering(CSI-SE),2016,pp.29–35.
//api.semanticscholar.org/CorpusID:267412469 [36] E. Mirsaeedi and P. C. Rigby, “Mitigating turnover with code
[19] Z. Rasheed, M. A. Sami, M. Waseem, K.-K. Kemell, X. Wang, reviewrecommendation:balancingexpertise,workload,andknowledge
A. Nguyen, K. Systa¨, and P. Abrahamsson, “Ai-powered code review distribution,” in Proceedings of the ACM/IEEE 42nd International
withllms:Earlyresults,”2024. Conference on Software Engineering, ser. ICSE ’20. New York, NY,

<!-- Page 12 -->

USA: Association for Computing Machinery, 2020, p. 1183–1195.
[Online].Available:https://doi.org/10.1145/3377811.3380335
[37] A. Ouni, R. G. Kula, and K. Inoue, “Search-based peer reviewers
recommendation in modern code review,” in 2016 IEEE International
ConferenceonSoftwareMaintenanceandEvolution(ICSME),2016,pp.
367–377.
[38] M.M.Rahman,C.K.Roy,andJ.A.Collins,“Correct:Codereviewer
recommendationingithubbasedoncross-projectandtechnologyexperience,”in2016IEEE/ACM38thInternationalConferenceonSoftware
EngineeringCompanion(ICSE-C),2016,pp.222–231.
[39] P.Thongtanunam,C.Tantithamthavorn,R.G.Kula,N.Yoshida,H.Iida,
and K.-i. Matsumoto, “Who should review my code? a file locationbased code-reviewer recommendation approach for modern code review,”in2015IEEE22ndInternationalConferenceonSoftwareAnalysis,Evolution,andReengineering(SANER),2015,pp.141–150.
[40] E. Su¨lu¨n, E. Tu¨zu¨n, and U. Dog˘ruso¨z, “Rstrace+: Reviewer
suggestionusingsoftwareartifacttraceabilitygraphs,”Informationand
Software Technology, vol. 130, p. 106455, 2021. [Online]. Available:
https://www.sciencedirect.com/science/article/pii/S0950584920300021
[41] C. Raffel, N. Shazeer, A. Roberts, K. Lee, S. Narang, M. Matena,
Y.Zhou,W.Li,andP.J.Liu,“Exploringthelimitsoftransferlearning
with a unified text-to-text transformer,” CoRR, vol. abs/1910.10683,
2019.[Online].Available:http://arxiv.org/abs/1910.10683
[42] M.Watanabe,Y.Kashiwa,B.Lin,T.Hirao,K.Yamaguchi,andH.Iida,
“On the use of chatgpt for code review: Do developers like reviews
by chatgpt?” in Proceedings of the 28th International Conference on
Evaluation and Assessment in Software Engineering, ser. EASE ’24.
New York, NY, USA: Association for Computing Machinery, 2024, p.
375–380.[Online].Available:https://doi.org/10.1145/3661167.3661183
[43] “Branch policies and settings,” may 2024. [Online]. Available: https:
//learn.microsoft.com/en-us/azure/devops/repos/git/branch-policies?
view=azure-devops&tabs=browser#check-for-comment-resolution

## Tables

**Table (Page 3):**

| Project | Explanation | # of Devel- opers | Language |
|---|---|---|---|
| Project #1 | B2BE-commerce Portal | 21 | TypeScript,Java, JavaScript |
| Project #2 | EnterpriseManagement Platform | 51 | HTML,JavaScript, C# |
| Project #3 | CustomizableAI SolutionsHub | 22 | C#,HTML, JavaScript SQL |


**Table (Page 5):**

| Status | Explanation |
|---|---|
| Active | This is the default status for new comments. |
| Pending | The corresponding comment is being analyzed or waiting for some other thing. |
| Resolved | The corresponding comment is successful and its suggestion was implemented. |
| Won’t fix | The corresponding comment is faulty or cannot be implemented. |
| Closed | The corresponding comment was not implemented for some other reasons than ”Won’t Fix”. |


**Table (Page 5):**

| SurveyParticipants |  |
|---|---|
| ExperienceinSoftwareDevelopment | NumberofParticipants |
| 0-2 | 4 |
| 2-5 | 9 |
| 5-10 | 6 |
| 10+ | 3 |
| PositionatBeko | NumberofParticipants |
| IndividualContributor | 16 |
| Lead/Manager | 6 |
| TotalPractitioners | 22 |
