---
title: "Decoding LLMs Socio Technical"
original_file: "./Decoding_LLMs_Socio_Technical.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["prompt-engineering", "llm", "rag", "chain-of-thought", "fine-tuning"]
keywords: ["llms", "language", "models", "https", "org", "doi", "arxiv", "llm", "model", "page"]
summary: "<!-- Page 1 -->


### Decoding Large-Language Models: A Systematic

Overview of Socio-Technical Impacts, Constraints,
and Emerging Questions. Kaya1 and Souvick Ghosh2*

1Stanford University, 450 Jane Stanford Way, Stanford, 94305–2004,

## Ca, Usa. 2*School of Information, San Jos´e State University, One Washington
Square, San Jos´e, 5192-0029, CA, USA."
related_documents: []
---

# Decoding LLMs Socio Technical

<!-- Page 1 -->


### Decoding Large-Language Models: A Systematic

Overview of Socio-Technical Impacts, Constraints,
and Emerging Questions.

### Zeyneb N. Kaya1 and Souvick Ghosh2*

1Stanford University, 450 Jane Stanford Way, Stanford, 94305–2004,

## Ca, Usa.

2*School of Information, San Jos´e State University, One Washington
Square, San Jos´e, 5192-0029, CA, USA.
*Corresponding author(s). E-mail(s): souvick.ghosh@sjsu.edu;
Contributing authors: zeynebnk@stanford.edu;

### Abstract

There have been rapid advancements in the capabilities of large language models (LLMs) in recent years, greatly revolutionizing the field of natural language
processing(NLP)andartificialintelligence(AI)tounderstandandinteractwith
human language. Therefore, in this work, we conduct a systematic investigation
oftheliteraturetoidentifytheprominentthemesanddirectionsofLLMdevelopments,impacts,andlimitations.Ourfindingsillustratetheaims,methodologies,
limitations,andfuturedirectionsofLLMresearch.Itincludesresponsibledevelopmentconsiderations,algorithmicimprovements,ethicalchallenges,andsocietal
implications of LLM development. Overall, this paper provides a rigorous and
comprehensiveoverviewofcurrentresearchinLLMandidentifiespotentialdirections for future development. The article highlights the application areas that
could have a positive impact on society along with the ethical considerations.
Keywords:largelanguagemodels,artificialintelligence,systematicreview,natural
languageprocessing.
1
4202
peS
52
]LC.sc[
1v47961.9042:viXra

<!-- Page 2 -->

1 Introduction
Thecapacityofartificialintelligence(AI)modelstounderstandhumanlanguageholds
paramount importance for their interaction with humans and other systems. The
emergence of large language models (LLMs) has had a profound impact on the developments of Natural Language Processing (NLP), with models of growing scale. In
particular, recent advancements in neural architectures, such as transformer models,
haveenabledtherapidlyexpandingcapabilitiesofLLMs,incorporatingvastdatasets,
significantcomputationalpower,andanincreasingnumberofparameters.Withscale,
thetransitionfromLanguageModels(LMs)toLLMshasbroughtaboutmuchgreater
language capabilities and abilities across tasks. While LMs have largely been limited
to basic text processing and specialized applications, LLMs are more generalizable.
LLMs have made notable contributions to language understanding and text generation, handling complex tasks including classification, translation, question-answering,
summarization,andinformationretrieval.Theirabilitiesacrossarangeofdiversetasks
and domains, adapting to even low-resource settings [1], demonstrate their transformative generalization capabilities. For instance, models like GPT-3 have showcased
remarkableversatilityingeneratingcreativecontentandsimulatingconversation.The
riseofopen-sourceinitiativesofLLMarchitecturesandpretrainedmodelshasfurther
propelled development. The significant technological impacts of LLMs, enhancing the
ability of artificial intelligence systems to communicate with humans, have also had
a growing influence on society. Concurrently, these developments raise pressing ethical questions, particularly around data privacy, bias, and the potential for misuse [2].
TherehavebeenincreasingeffortsonthereleaseofLLMs,introducingimplicationsof
the potential benefits and challenges they pose to our interactions with language and
technology.
LLMs have now become the frontier of research and development in NLP and
artificial intelligence as a whole. As LLMs grow rapidly with new breakthroughs,
applications, and scales, we aim to provide a comprehensive and systematic overview
of the directions of LLM research and facilitate further advancements. We summarize
the course of existing efforts with LLMs, delving into each component of the model
development process and detailing the goals and current capabilities in the field. We
further identify the key considerations and gaps to address in LLM development to
guide future research. Through these explorations, we aim to answer three guiding
research questions (RQs):
• RQ1: What are the prominent aims and objectives addressed in LLM research?
• RQ2: What are the popular methodologies for advancing the capabilities of

### LLMs?

• RQ3: What are the limitations and ethical considerations of LLM development
as identified in contemporary influential research?
We investigate these questions through a systematic review characterized by
methodologicalrigor,objectivity,andcomprehensiveandquantitativestatisticalanalyses of studies, enabling synthesized, evidence-based contributions. The rest of the
paper is organized as follows: Section 2 provides an overview of the systematic review
process, while Section 3 discusses the methodology employed for conducting this
review. Section 4 presents several statistics of the reviewed papers. Sections 5, 6,
2

<!-- Page 3 -->

and 7 highlight the purpose, methodology, and limitations of the reviewed papers,
respectively. Section 8 answers the research questions, offering insights into future
developments, and Section 9 concludes the paper.
2 Systematic Reviews
Systematic reviews aim to provide a structured and comprehensive evaluation of
existing literature utilizing explicit, replicable methods. Systematic reviews follow a
rigorous, meta-analytical approach, employing a standardized procedure for identifying, appraising, and synthesizing relevant studies, culminating in an evidence and
statistically-based [3]. This approach ensures that the summary of available studies is
not only comprehensive but also underpinned by robust methodological rigor.
Owing to their statistical precision, systematic reviews are particularly useful for
researchers who rely on evidence-based decision-making. Initially popularized in the
health sciences to enhance the reliability and validity of medical research [4, 5], the
practice of systematic reviews has since broadened to include information science
[6, 7] and related fields [8, 9], effectively informing future developments. The systematic review presents a methodology for establishing valuable findings and distinct
contributions in IR beyond a simple overview of past works.
3 Systematic Review Methodology
The steps to conducting a systematic review follow three main phases and their subcomponents, outlined in Figure 1 and described in detail below.
3.1 Selection of Sources (Inclusion/Exclusion Criteria)
The first step in our systematic review process was the identification of works for
study. We focused on literature that directly contributes to the development or
capabilities of LLMs. Articles were sourced from Google Scholar and queried using
a series of search strings, including: “large language models,” “attention language
model,” “generative language models,“ “natural language understanding,” “language
model scaling,” “prompted language model,” and “prompt engineering.” This review
considered English-language publications from 2016 to 2023.
Toidentifyauthoritativesources,wecompiledalistofvenuesknownforsignificant
LLM studies, limiting to papers published in select top NLP and AI journals and
conferences, as well as reports from leading AI industry developers. The inclusion of
industry publications was a deliberate choice aimed at capturing various impactful
works in the field, particularly those contributing to novel methodologies and social
impact,whichmightnothavebeenpublishedinacademicjournalsorconferencesyet.
Inselectingthemostinfluentialpapers,weappliedacitationthresholdof150citations.
The culmination of this process was the selection of 61 articles for our systematic
review.
3

<!-- Page 4 -->

Fig. 1: Steps of Performing a Systematic Review.
3.2 Thematic Analysis Procedure / Coding Scheme
The collected papers were coded for statistical analysis on various categories. Basic
metadata features such as authors, publication year, publication venue, and citations
were included. We also extracted author affiliations at the time of publication as
indicated by the authors’ email domains.
Thematic analysis was performed for the papers across various categories. After
reviewing the paper, the authors first produced a list of themes for each piece derived
from the qualitative thematic categories. The list was consolidated to generate a coding hierarchy. Each author conducted these steps independently to minimize bias in
theprocess.Then,theycompared anddiscussedtheannotationstoreachaconsensus
and resolve any disagreement. Figure 2 shows the distribution of major themes and
subthemes for the purpose, methodology, and limitations of the reviewed papers. We
discuss each of the super themes in individual sections, and the subthemes in corresponding subsections. Subthemes (e.g., 1.2 Improving LLM Performance) fall under
each of these superthemes (e.g., 1. Aims and Objectives), which are shown in the
figure.Thereexistsamany-to-manyrelationshipbetweenthearticlesandthethemes,
and the themes are not mutually exclusive, as one article can have multiple themes.
4 Characteristics of Publications
In the following section, we provide an overview of the selected articles reviewed,
discussing relevant statistics and features that characterize the content of the review.
4

<!-- Page 5 -->

Fig. 2: Frequencies of Themes and Sub Themes.
Approximately 20% (n=12) of the articles were published in 2023; 13% (n=8) in
2022, 20% (n=12) in 2021; 15% (n=9) in 2020; 21% (n=13) in 2019; 3% (n=2) in
2018; 7% (n=4) in 2017; and a solitary paper in 2016. Notably, there was a rapid
increase in publications between 2018 and 2019. Figure 3 illustrates the distribution
of articles across years of publication. Figure 3 shows the representation of various
types of publication venues—conference papers, journal papers, and industry reports.
The reviewed articles represent a selection from 16 venues: 10 conferences, 2 journals,
and 4 industry reports. NeurIPS, ACL, and PMLR featured the most articles, with
18, 9, and 6 articles, respectively. ICLR and EMNLP had 5 each, and OpenAI had 4.
NAACL, JMLR, EACL, and Google Research had 2 each, and the remaining venues
hadoneeach.ArticlespublishedinNAACL,NeurIPS,andJMLRgarneredthegreatest number of citations. Notably, OpenAI’s reports, despite not being in a formally
peer-reviewed venue, received a substantial number of citations.
Figure 4 shows the distribution of the number of authors in the articles, and the
increaseinauthorshipoftop-citedpapersovertheyears.Ascanbeseeninthefigure,
collaborativeworksarerelativelycommonamongLLMarticles;approximatelyathird
(34%; n=17) of the articles feature over 8 authors, while 4 authors represent the
most common size of collaborative groups (18%; n=11). Figure 5 presents the word
cloud for organizational affiliations of the authors.Researchers affiliated with Google,
5

<!-- Page 6 -->

Fig. 3: Publication Statistics.
Microsoft, OpenAI, Facebook/Meta, and universities like Stanford, Carnegie Mellon,
and New York University are the most represented and have the greatest number of
contributors to LLM research.
6

<!-- Page 7 -->

Fig. 4: Avg. Number of Authors Per Paper by Year.
Fig. 5: WordCloud of Author Affiliations.
5 Aims & Objectives (RQ1)
LiteratureinthedevelopmentofLLMspursuesdifferentaims.Oftheworkswestudied,
a significant 66% focused on best practices and practical considerations in ethics and
research methodology. Meanwhile, 44% introduced originality in the advancement of
LLM performance, focusing on aspects such as efficiency, robustness, and scalability.
A smaller proportion, 18%, were investigative studies with the objective of furthering
the understanding of LLMs. We explore the main avenues of LLM improvement and
progress that are prevalent in the field.
7

<!-- Page 8 -->

Table 1: Major Themes for Aims, Objectives, and Purposes of Reviewed Papers
Theme Example Articles

### Subcategories

Responsible Ethics, AI Bias, Lee et al. [10]; Wang et al. [11]; Gehman
Development Information Accu- et al. [12]; Zhang et al. [13]; Carlini et al.
Considera- racy, Social Impact, [14]; Lester et al. [15]; Hoffmann et al.
tions Research Expan- [16]; Kaplan et al. [17]; Bender et al. [2];
sion, Responsible Solaiman et al. [18]; Raffel et al. [19];
Evaluation, Acces- Brown et al. [1]; Fedus et al. [20]; Rae
sibility, Optimal et al. [21]; Vaswani et al. [22]; Zhang
Development, et al. [23]; Jiang et al. [24]; Chowdhery
Scaling et al. [25]; CONNEAU and Lample [26];

### Wangetal.[27];Kirchenbaueretal.[28];


### Manakul et al. [29]; Turpin et al. [30]

Improving Data Efficiency, Sanh et al. [31]; CONNEAU and Lam-
LLM Generalizability, ple [26]; Lee et al. [10]; Wang et al. [11];
Performance Robustness, Size Petronietal.[32];Clarketal.[33];Dong
efficiency, Absolute et al. [34]; Zhao et al. [35]; Schick and
performance, Diverse Schu¨tze [36]; Lester et al. [15]; Howard
language support and Ruder [37]; Gururangan et al. [38];
Radford et al. [39]; Hoffmann et al. [16];
Jozefowicz et al. [40]; Radford et al.
[41]; Kaplan et al. [17]; Shazeer et al.
[42]; Radford et al. [43]; Raffel et al.
[19]; Brown et al. [1]; Fedus et al. [20];
Alayrac et al. [44]; Rae et al. [21]; Devlin
et al. [45]; Vaswani et al. [22]; Liu et al.
[46]; Zhang et al. [23]; Dauphin et al.
[47]; Press and Wolf [48]; Dai et al. [49];
Chowdheryetal.[25];Conneauetal.[50];
Heetal.[51];Wangetal.[27];Yangetal.
[52]; Roberts et al. [53]; Kandpal et al.
[54]; Zhang et al. [55]; Huang et al. [56];
Schick et al. [57]; Yao et al. [58]; Wang
et al. [59]; Gruver et al. [60]
Investigative Understanding LLM LeScaoandRush[61];Petronietal.[32];
Studies effectiveness, Under- Nieetal.[62];Weietal.[63];Clarketal.
standingLLMknowl- [64]; Roberts et al. [53]; Biderman et al.
edge/capabilities [65]; Kandpal et al. [54]; Schaeffer et al.
[66]; Turpin et al. [30]; Gruver et al. [60]
8

<!-- Page 9 -->

5.1 Responsible Development Considerations
As LLMs gain prevalence in social and research contexts, attention has been
increasingly directed to the best practices of the field in developing and releasing
LLMs [2, 12, 14, 18, 28–30].
Various studies have aimed to address the ethical and societal impact of LLMs.
Forinstance,Benderetal.[2]considerthepervasiverisksassociatedwiththegrowing
size of LLMs with a critical review of the limitations and potential dangers of LLMs.
Solaiman et al. [18] examine the release of LLMs, discussing recommendations for
responsible publication in AI that consider the social impacts of OpenAI’s release of
the GPT-2 models. Their framework for best practices for responsible model release
includesprioritizingandcollaboratingwiththecommunitiesinfluencedbythemodels
rather than focusing on general tradeoffs. Kirchenbauer et al. [28] present a method
for ‘watermarking’ LLMs and discuss its applications and security in deployment.
Carlini et al. [14] work to demonstrate further the potential for misuse presented
bythegrowthandreleaseofLLMs.Theyextractmemorizedindividualtrainingpoints
fromonlyblack-boxqueryaccess,showingthatLLMsposeathreattoleakingpersonally identifiable information. Gehman et al. [12] find biased and harmful propagation
learned by LLMs. Manakul et al. [29] and Turpin et al. [30] both note the faultiness of LLMs’ information, including their capacity to misinform, hallucinate, and be
manipulated.
With these risks in mind, researchers have aimed to implement safe methods in
their work and be conscious of the impact of their models. In developing a suite of
OpenPre-trainedTransformer(OPT)languagemodels,Zhangetal.[13]aimtobring
best practices and accessibility in their efficient replication of GPT-3, released with
full detailed documentation and an analysis of considerations for the safe deployment
of their model.
5.2 Improving LLM Performance
Technical advancements are the primary focus of LLM research, and several key
works [1, 11, 31, 34, 36–38, 41, 46, 55, 60], have concentrated on enhancing the
performance of large language models across a diverse range of applications.
A primary objective in LLM research is the generalizability of these models to
diverse tasks and domains. For example, Radford et al. [41] demonstrate the capacity
of LLMs to perform well across various domains and implicitly on downstream tasks
without any parameter or architecture modification. Building on the effectiveness of
thisimplicitlearning,Sanhetal.[31]createamodelthatcanbettergeneralizetoheldouttasksandperformrobustlywithdiversepromptwording,usingexplicitsupervised
multitasktraining.Brownetal.[1]examinethegeneralizabilityofLLMsonnewtasks
withlimitedtask-specificdatainthefew-shotsetting.Gruveretal.[60]examineLLMs
zero-shotabilitiesinthetaskoftimeseriesforecasting.HowardandRuder[37]present
Universal Language Model Fine-tuning (ULMFiT) — a transfer learning method —
topretrainalanguagemodelonalargegeneral-domaincorpus,applicabletodifferent
9

<!-- Page 10 -->

NLP tasks without task-specific modifications. The GLUE and SuperGLUE benchmarks [11, 27] further this pursuit of generalizability with evaluation and diagnostic
datasets spanning diverse tasks and domains.
With the introduction of the BERT architecture, Devlin et al. [45] presented a
significant development in language representation models that can be effectively
fine-tuned without substantial task-specific architecture modifications. Expanding
upon BERT’s capabilities, Yang et al. [52] address its limitations with autoregressive
language modeling in XLNet.
Many articles target data and size efficiency in LLMs. For instance, CONNEAU
andLample[26]significantlyadvanceeffectivenessintaskspertainingtolow-resource
languageswithlimitedavailabledata.Zhaoetal.[35]improvedataefficiencybyresolving the problem of stability in few-shot learning. Roberts et al. [53] leverage LLMs’
ability to implicitly store and retrieve knowledge to determine its utility in answering questions without additional training. To maximize the use of large unlabeled
data, Radford et al. [39] employ unsupervised generative pretraining to enhance naturallanguageunderstandingperformancewithlimiteddata.TheELECTRA[33]and
DeBERTa architectures [51] improve BERT’s sample-efficiency. Kaplan et al. [17] and
Zhang et al. [55] tackle efficiency in model development by optimizing performance
basedonthefactorsofcomputepower.Theseworkscollectivelytargetvariousaspects
of model performance to further the effectiveness of LLMs.
5.3 Investigative Studies
The objective of some papers is to delve into the less understood mechanisms that
drive the success of LLMs [30, 61, 63, 64].
Given the complexity yet significant effectiveness of attention mechanisms, Clark
et al. [64] decipher the patterns in LLM attention and their association with specific
linguistic features. In examining the performance gains achieved through prompting, Le Scao and Rush [61] analyze the effectiveness of prompting and the trends
in its success. Wei et al. [63] experiment with chain-of-thought prompting to gauge
LLMs’ reasoning. Inspired by the human tendency to break down complex tasks into
multi-step problems, they augmented the input examples with a chain of thought.
Meanwhile, Turpin et al. [30] studied the weaknesses of chain-of-thought prompting
and where it could result in unfaithful responses and be prone to manipulation.
Such investigative studies offer valuable insights into the capacities of LLMs and
inform further development. Roberts et al. [53] leverage LLMs’ implicit knowledge
storage in question-answering tasks. LLMs are able to achieve competitive results in
question-answeringwithoutaccesstoexternalresources,offeringinsightsintotheuses
and underlying learning processes of LLMs. Similarly, Petroni et al. [32] explore the
potential of LLMs as knowledge bases, building on this inherent characteristic. Nie
et al. [62] introduce a benchmark, Adversarial NLI, to identify and evaluate tasks
that pose the greatest challenge for LLMs, like numerical and quantitative reasoning
and complex inference types. These works all aim to better empirically understand
LLMs. Biderman et al. [65] present Pythia, which enables the analysis of LLM capabilities with scale and training. Schaeffer et al. [66] argue that the unique abilities of
10

<!-- Page 11 -->

larger-scale models may be a ‘mirage’ resulting from the metrics used based on their
mathematical model examining changes in LLM performance with size.
6 Methodologies & Capabilities (RQ2)
Various stages of model development contribute significantly to the efficacy of LLMs,
presentingmultiplefacetstoaddressinrefiningtheircapabilities.Inourreview,13%of
the works’ methodologies involved the development of datasets specifically for LLMs.
36%focusedonstudyingmodelinputsandoutputs,includingaspectssuchasprompting, formatting, and pre-/post- processing techniques. The majority, 59%, delved into
modeltraining,examiningaspectrumofarchitectures.Asignificantproportion,41%,
centeredtheirmethodsontheanalysisofLLMs.Throughacomprehensiveanalysisof
themethodsemployed,weaimtoprovidevaluableinsightsintothekeystrategiesand
their contributions, illuminating paths for continued improvement and innovation.
Table 2: Major Themes for Methodologies and Capabilities of Reviewed Papers
Theme Example Articles

### Subcategories

DatasetDevel- Diverse Datasets, Gehman et al. [12]; Wang et al. [11];
opment Challeng- Wang et al. [27]; Radford et al. [41];
ing Datasets, Petroni et al. [32]; Nie et al. [62]; Huang
Dataset Construc- et al. [56]; Manakul et al. [29]
tion Methods,

### Benchmarks


### Model Task Format, Sanh et al. [31]; Le Scao and Rush [61];

Input/Output Prompting, Text-to- Lee et al. [10]; Gehman et al. [12]; Zhao

### Text, Task-specific etal.[35];SchickandSchu¨tze[36];Lester

Input, Character- et al. [15]; Gururangan et al. [38]; Raffel
Level, Tokens, et al. [19]; Vaswani et al. [22]; Press and

### Data Preprocessing, Wolf[48];Weietal.[63];Jiangetal.[24];

Decoding, Output Gao et al. [67]; Kirchenbauer et al. [28];
Calibration Kandpal et al. [54]; Zhang et al. [55]; ?
]; Schick et al. [57]; Yao et al. [58]; Wang
et al. [59]; Gruver et al. [60]
Continued on next page
11

<!-- Page 12 -->

Table 2 continued from previous page
Theme Example Articles

### Subcategories

Model Train- Cross-lingual Sanh et al. [31]; CONNEAU and Laming learning, Mul- ple [26]; Le Scao and Rush [61]; Gehman
titask learning, etal.[12];Petronietal.[32];Zhangetal.
Unsupervised learn- [13]; Clark et al. [33]; Dong et al. [34];
ing, Fine-tuning Schick and Schu¨tze [36]; Lester et al.
methods, Model [15];HowardandRuder[37];Gururangan
architecture, Train- et al. [38]; Radford et al. [39]; Hoffmann
ing Objectives, et al. [16]; Jozefowicz et al. [40]; Rad-
Multimodal, Scaling fordetal.[41];Kaplanetal.[17];Shazeer
etal.[42];Radfordetal.[43];Raffeletal.
[19]; Brown et al. [1]; Fedus et al. [20];
Alayrac et al. [44]; Rae et al. [21]; Devlin
et al. [45]; Vaswani et al. [22]; Liu et al.
[46];Zhangetal.[23];Dauphinetal.[47];

### Daietal.[49];Chowdheryetal.[25];Gao

et al. [67]; Conneau et al. [50]; He et al.
[51]; Yang et al. [52]; Saharia et al. [68]
LLM Under- Factor analysis, Met- Le Scao and Rush [61]; Wang et al. [11];
standing rics, Optimal prac- Gehman et al. [12]; Carlini et al. [14];
tices, Risks, Review Dong et al. [34]; Zhao et al. [35]; Gururangan et al. [38]; Hoffmann et al. [16];
Kaplan et al. [17]; Bender et al. [2]; Radfordetal.[41];Solaimanetal.[18];Raffel
etal.[19];Brownetal.[1];Vaswanietal.
[22]; Dai et al. [49]; Wei et al. [63]; Jiang
etal.[24];Clarketal.[64];Conneauetal.
[50]; He et al. [51]; Roberts et al. [53];
Turpin et al. [30]; Schaeffer et al. [66];
Kandpal et al. [54]; Biderman et al. [65]
6.1 Dataset and Benchmark Development
Large,high-qualitycorporaarefoundationaltothecapabilitiesofLLMs.Thedevelopment of diverse and effective datasets has been a pivotal method in furthering LLMs,
and our review identified several studies that explored new datasets [11, 27, 29, 41,
56, 62].
The General Language Understanding Evaluation (GLUE) benchmark [11] has
emerged as one of the most significant datasets in NLP, widely used to evaluate models’ NLU capacity. This work presents a dataset comprising diverse linguistic tasks
anddomainstoadvancemodels’sample-efficientknowledgetransferabilityandadiagnostic evaluation dataset tagged with various linguistic phenomena to facilitate error
analysis. With the rapid advancement of LLMs surpassing human-level performance,
12

<!-- Page 13 -->

the authors later introduced SuperGLUE [27] to further challenge LLMs with more
demanding tasks, varied task formats, and comprehensive human baselines.
Continuing the pursuit of more demanding datasets to facilitate LLM growth, Nie
et al. [62] propose an adversarial approach to constructing a dynamic benchmark
for longevity, Adversarial NLI. In this approach, human annotators iteratively create
intentionally challenging examples to pinpoint and expose model weaknesses.
Radford et al. [41] investigate the capacity of LLMs to learn implicitly from data
by constructing a large and manually filtered corpus, WebText, aimed at training a
model on varied domains and contexts for improved applicability across a broader
rangeoftasks.ThedataunderpinningLLMsiscrucialtotheirlinguisticandrelational
knowledge. As such, they can inadvertently learn toxicity from texts and generate
biased content. Gehman et al. [12] address the risks posed by flawed datasets by
constructing REALTOXICITYPROMPTS, a dataset of naturally occurring prompts
withtoxicityscores,quantifyingtheriskofapretrainedlanguagemodelforgenerating
toxic text. Manakul et al. [29] develop SelfCheckGPT, a method that enables factchecking of LLMs’ hallucinations. Huang et al. [56] develop a multimodal text-image
mixedcorpustotrainKosmos-1apowerfulmultimodalLLM.Datasetdevelopmenthas
emerged as a prevalent method to both expand and rigorously test LLM capabilities.
6.2 Model Input/Output
Theformattingandprocessingofnaturallanguagedataforuseinmodelsisarelevant
aspectofLLMdevelopmentthathasseennewmethodologies[15,31,57,59,61,63,67].
The interpretation of tasks as prompts has arisen as an effective paradigm for
adapting pretrained models. Scao & Rush (2021) Le Scao and Rush [61] establish
the data efficiency provided by prompting and propose a novel metric to quantify the
advantageofapromptoveragenericmodelheadacrosstasksanddatasizes.Giventhe
benefits of prompts, literature has shifted towards improving and optimizing prompt
generation. Gao et al. (2021) Gao et al. [67] present LM-BFF, incorporating effective
techniquestotestthelimitsofthepromptingmethodology.Wangetal.[59]approach
images as a foreign language and aligning vision tasks with language tasks through
the input format of natural language instructions.
Delving into the low-data applications of prompting, Sanh et al. [31] demonstrate
the capacity of prompting for implicit multitask learning, enhancing zero-shot generalization. Wei et al. [63] leverage processes in human problem-solving to examine
“chains of thought” in prompting to improve reasoning-based tasks in LLMs. Adapting prompting with fine-tuning, Lester et al. [15] introduce “soft prompts,” which are
learned end-to-end through backpropagation from a pretrained model and incorporated into downstream tasks. Yao et al. [58] further presents a ‘tree of thoughts’ to
improve LLMs’ abilities in problem-solving tasks.
Many studies have explored the modification of inputs with new formats or
additional information to support model learning [12, 19, 22, 48]. Raffel et al. [19]
introducedaninfluentialworkwithaunifiedframeworkthatconvertstext-basedtasks
into a text-to-text format. Schick et al. [57] introduce APIs into LLMs, allowing their
model Toolformer to access and use external tools to support their responses. Schick
andSchu¨tze[36],motivatedbyincludingnaturallanguagetaskdescriptionsininputs,
13

<!-- Page 14 -->

present Pattern-Exploiting Training (PET), which reformulates inputs as cloze-style
phrases. Vaswani et al. [22], in their Transformer architecture, add positional encodings to the input embeddings, enhancing efficiency. Press and Wolf [48] alter input
embeddings by tying the input embedding to the output embedding. Gehman et al.
[12] adopt an approach of inserting information in inputs to target their limitations.
In particular, they use prefix tokens to reduce toxicity in generations.
Outputsarealsoareasofdevelopment[12,35].Inexaminingwaystoaddressmodel
toxicity, Gehman et al. [12] present decoding-based intervention methods. Zhao et al.
[35] implement calibration of outputs based on generations to neutralize inputs to
improve few-shot bias.
6.3 Model Training
New methods of model architecture development bring significant advancements to
thecapabilitiesofLLMs.Inparticular,developmentsinthepretrainingprocessesand
objectives are a prevalent area of study [26, 33, 34, 39, 45, 52].
For large-scale language modeling with RNNs, Jozefowicz et al. [40] introduce
a Softmax loss based on character-level CNNs and combine word- and characterlevel models, integrating them into the word-level LSTM. Radford et al. [43] explore
pretraining methods for CNNs in multimodal learning with vision-based tasks,
introducing Contrastive Language-Image Pre-training (CLIP). This method involves
pretrainingbylearningajointmultimodalembeddingwithanimageandtextencoder
and then predicting image-text pairings.
Vaswani et al. [22] introduce the Transformer architecture, featuring the selfattention mechanism to learn the relationships between words within sentences,
enabling greater scale and efficiency. The development of BERT [45] was one of the
mostimportantadvancesofLLMs.BERTisdesignedtopretraingeneralizablebidirectional representations from unlabeled text. Its pretraining employs two unsupervised
tasks: Masked Language Modeling (MLM), where masked tokens are predicted, and
NextSentencePrediction(NSP),wheretherelationshipbetweentwosentencesispredicted. Aiming for sample efficiency and reduced computational cost, Clark et al. [33]
propose a novel pretraining method through ELECTRA. In this method tokens are
replaced with alternatives sampled from a small generator and the model learns to
discriminate between generated and true tokens. Yang et al. [52] address the limitations of BERT’s autoencoding-based pretraining in learning masked dependencies
with their autoregressive pretraining method in XLNet. Radford et al. [39] use generative pretraining – an innovative approach to pretraining – for LLMs, followed by
discriminative fine-tuning for specific tasks. ERNIE [23] uses knowledge graphs as
input to provide structured information alongside natural language. Dong et al. [34]
introduce a new unified pre-training language model (UNILM), jointly optimized for
multipleobjectivestoenablefine-tuningforbothNLUandNLGtasks.Thisapproach
enhances task generalizability. To broaden capabilities across languages, CONNEAU
and Lample [26] introduce two learning methods for cross-lingual language modeling.
14

<!-- Page 15 -->

6.4 LLM Understanding
VariousresearchworksattempttoadvanceLLMsthroughanalysis-basedmethods[12,
24, 35, 61].
ThedevelopmentofmetricstoquantifyaspectsofLLMsenhancesunderstandingof
boththelimitationsandeffectivenessofthesemodels.LeScaoandRush[61]introduce
an approach to quantify the advantage of prompting, aiming to guide practices in
developing LLMs with scale by examining the impact of prompting across various
datasizes.Gehmanetal.[12]REALTOXICITYPROMPTSdatasetprovidesvaluable
insights for gauging the risks of LLMs and understanding the factors to be conscious
of. Metrics such as Majority Label Bias, Recency Bias, and Common Token Bias
are crucial [35] to characterize model stability, aiding in the development of their
calibrationapproachtoaddressinstability.Jiangetal.[24]proposeasetofmethodsto
bettermeasuretheaccuracyofmodelknowledgethataccountsfortheroleofprompts
in the quality of generations. Their work enables a more accurate estimation of the
knowledge in language models with the automatic generation of better prompts.
7 Limitations & Considerations (RQ3)
Understanding the limitations of studies and LLMs provides essential context and
guidance for future work. Of the articles we examined, 43% explicitly recognized
the limitations and ethical considerations of their study. The proportion of articles
includingtheselimitationshasincreasedwithrecency,astheimportanceofdiscussing
limitations has become increasingly emphasized, with some venues even requiring
specific sections for them. Across these papers, 62% noted limitations regarding performance, 58% identified limitations in the study procedure, and 58% examined the
ethicalimpactsoftheirwork.Inouranalysis,weexaminetheacknowledgedlimitations
in the development of LLMs to promote best practices in LLM research.
Table 3: Limitations and Considerations of LLM Research
Theme Example Articles

### Subcategories

Performance Low-data settings, Sanhetal.[31];Leeetal.[10];Zhaoetal.
Limitations Complex tasks, [35]; Lester et al. [15]; Kaplan et al. [17];
Generalizability, Radford et al. [41]; Radford et al. [43];

### Interpretability Raeetal.[21];Wangetal.[11];Biderman

et al. [65]; Kirchenbauer et al. [28]; Manakul et al. [29]; Huang et al. [56]; Schick
et al. [57], Yao et al. [58]; Gruver et al.
[60]
Continued on next page
15

<!-- Page 16 -->

Table 3 – continued from previous page
Theme Example Articles

### Subcategories

Study Limita- Practical Replica- Sanh et al. [31]; Le Scao and Rush [61];
tions bility Limitations, Lee et al. [10]; Wang et al. [11]; Gehman
Cost, Compute et al. [12]; Dong et al. [34]; Zhao et al.
power, Limited [35]; Kaplan et al. [17]; Bender et al. [2];
Study Scope, Imper- Raeetal.[21];Radfordetal.[43];Kandfect assumptions, paletal.[54];Schaefferetal.[66];Turpin

### Imperfect Evaluation et al. [30]; Yao et al. [58]

Ethical Con- Harmful genera- Sanh et al. [31]; Le Scao and Rush [61];
siderations tion, Model release Gehman et al. [12]; Dong et al. [34];
risks, Environmental Lester et al. [15]; Bender et al. [2]; Radimpact, Lan- ford et al. [43]; Alayrac et al. [44]; Gao
guage limitations, et al. [67]; Wang et al. [11]; Biderman
Language limitations et al. [65]; Kandpal et al. [54]; Huang
etal.[56];Yaoetal.[58];Wangetal.[59]
7.1 Performance Limitations
A significant and widely recognized limitation in LLM research is their weaknesses in
performance for robust applicability. The articles have identified the limited capacity
of LLMs in tackling certain complex tasks [1, 11, 18, 41, 57, 67]. Wang et al. [11], in
examining the performance of NLU systems through their construction of the GLUE
benchmarkanditsdiagnosticdataset,notethechallengesLLMsfaceonspecifictasks
andvariouslinguisticphenomena:modelsoftenperformlowerontheRTEandWNLI
inferencetasks,andLogic-basedtasks,andstruggleincasesinvolvingrestrictivityand
double negation.
Radfordetal.[41]recognizethatintaskssuchassummarization,LLMperformance
islower,afindingechoedbyBrownetal.[1],whoidentifytasksliketextsynthesisasa
weakness.TheperformancedisparitiesinhardertasksarenotedbyGaoetal.[67],who
observe that their method favors tasks with shorter inputs, fewer output classes, and
straightforward structures amenable to a “fill-in-the-blank” format. Solaiman et al.
[18] further note long input text as a challenge in the accuracy of LLMs. The growing
capabilities of LLMs have relied heavily on the availability of large amounts of data,
leaving low-data and zero- to few-shot settings as a persisting challenge of LLMs [1,
31,43,44,67].Brownetal.[1],Schicketal.[57],andAlayracetal.[44]bothnotepoor
sampleefficiencyintrainingasabroaderlimitationofLLMs.Intheiranalyses,Radford
et al. [41] characterize the zero-shot performance of GPT-2 as practically “far from
usable,” mirroring the substantial gap in zero-shot performance from traditionally
fine-tuned models identified by Sanh et al. [31]. Beyond absolute performance, Gao
et al. [67] also identify substantial instability in few-shot learning. LLMs experience
limited broad generalizability. Biderman et al. [65] analyze the capabilities of LLMs
with scale using their suite of models Pythia, showing that with growing scale, LLMs
improveinperformance,albeitwithadecreasingrate.Thelowzero-shotperformance
16

<!-- Page 17 -->

ofLLMsmaybelessrelevantforotherandnewerLLMs,butisstillprominent.These
present an important and relevant area for further study.
7.2 Study Limitations
BeyondthetechnicallimitationsofLLMs,thearticlesexaminethelimitationsoftheir
study approaches and analyses. To maintain best practices and provide context for
their findings, multiple articles acknowledge the limitations of their study scope and
its imperfect assumptions [10, 12, 16, 25, 43, 53, 61, 66].
The toxicity dataset composed by Gehman et al. [12] relies on a single available
metric of toxicity detection in text, which they acknowledge as an imperfect measure
thatcouldbiastoxicitydetectiontowardslexicalcuesandmisssubtlebiases.Hoffmann
etal.[16],Turpinetal.[30],andManakuletal.[29]similarlynotetheirlimitedscope
and scale of study as a constraint to the broader generalizability of their findings.
Roberts et al. [53] propose analyses beyond their scope, including evaluating tasks
that require reasoning capabilities, for future work. Schaeffer et al. [66] also recognize
their limited scope. In addition to expanding on the limitations of their evaluation
datasets, Radford et al. [43] recognize their utilization of validation sets that do not
accurately reflect true zero-shot scenarios despite their zero-shot focus as a limitation of their work in broader applicability for low-data settings. Le Scao and Rush
[61] acknowledge their use of human-written prompts and recommend the analysis of
automatic prompts for future work. Lee et al. [10] clarify the focuses of their study,
describingthattheyexaminetheover-representationofduplicatetextsbutnotunderrepresentation, and they do not distinguish or analyze the positive versus negative
impact of memorized content. These limited scopes introduce room for further examinations and analyses, as well as additional implications about the context of the
findings presented.
7.3 Societal Impact
The limitations of language models as they pertain to large-scale release, application,
andsocialimpactareespeciallyimportanttoconsiderasLLMsgrowinsizeandreach.
The potentially harmful effects of LLMs pose risks in model release [1, 13, 14, 31,
43, 44, 56, 58, 68]. The most prominent mention of these risks is in their bias and
toxicity,whichareproblemscommonacrosstheuseofLLMs,notedinthemultimodal
work ofAlayrac et al. [44] and Radford et al. [43] and the scaling studies of Rae et al.
[21] and Hoffmann et al. [16]. In addition to issues of bias, Brown et al. [1], Saharia
etal.[68],Yaoetal.[58],Huangetal.[56],andCarlinietal.[14]highlightthepotential
for deliberate misuse of LLMs and their privacy limitations.
These concerns about bias and harmful uses bring risks in the release of LLMs,
necessitatingabalancebetweensecurityandopenness.Zhangetal.[13]citethesereasons as justification for releasing their OPT models to the research community before
broader deployment. Sanh et al. [31] emphasize transparency and reproducibility as
guiding principles in their decision to release their dataset, models, and tools. However, they acknowledge that their deliberate decisions to reduce the use of corpora
with harmful content do not fully eliminate biases in LLMs.
17

<!-- Page 18 -->

VariousarticlesalsoacknowledgethelimitationsofLLMs’benefitsintermsoftheir
environmental impact [2, 13, 31, 61]. Wang et al. [59] make efforts to reduce training
resourcesandthusthecarbonfootprintoftheirmodel.WhileLLMsarepowerfultools,
they can have limitations in their readiness and ability to make a positive impact on
society. This underscores the need for a balanced approach to assessing their benefits
and drawbacks.
8 Discussion
In this section, we answer the research questions and discuss the implications and
future directions in LLM research.
8.1 Answering Research Questions
ToanswerRQ1,weexaminedthemainobjectivesofLLMresearchtoidentifythemost
prevalent areas to address in the field. One primary aim was to improve the absolute
performance of LLMs, focusing on their efficiency, robustness, and scalability. With
the increasing applications of LLMs, many studies also aimed to develop and apply
best practices from both a technical and an ethical standpoint. Others bridged these
two areas, analyzing both the abilities and impacts of LLMs.
In RQ2, we explored the methodologies of LLM studies to understand the various
approachestoadvancingLLMcapabilities.Theresultsdemonstratedafocusonevery
stage of LLM development. A significant portion of the studies targeted model architectures, developing new learning strategies, and training and pre-training objectives.
Concurrently, other studies highlighted the role of factors external to the model, such
as constructing new datasets and processing and interpreting inputs and outputs. A
set of studies applied methods that analyzed LLMs’ capabilities.
To answer RQ3, we thoroughly examined the LLM studies and their ethical considerations. Firstly, we found weaknesses in the performance of LLMs on complex
tasks, such as those involving logic, longer text, and specific linguistic phenomena.
Furthermore, the data-reliance of LLMs raises concerns about their robustness. Secondly, we identified areas for expansion in the limited scope and assumptions used in
thestudies.Lastly,wefoundimportantconsiderationsregardingtheimpactofLLMs,
includinglearnedtoxicityandbiases,potentialformisuse,andadditionalfactorsthat
hold significant implications for the release of LLMs.
8.2 Implications and Future Work
Beyond summarizing current trends in LLM research, this systematic review has
pinpointed pivotal directions and key considerations for future studies.
8.2.1 Research Topics
We identify gaps and areas of progress in current research. In particular, the most
underaddressed yet valuable areas include the scaling of LLMs, enhancing LLMs’
linguistic understanding and reasoning capabilities, and improving the data efficiency
of LLMs. Furthermore, as LLMs evolve and their capabilities expand, understanding
18

<!-- Page 19 -->

how they learn and what drives their success becomes increasingly crucial to inform
further development. Therefore, analysis and investigations into LLM explainability
and interpretability are important.
The originality of a study is characterized by the combination of its purpose
and methods: we reviewed works that aim to improve generalizability through model
architecture, address bias in post-processing, or enhance efficiency with optimized
parameters. These insights pave the way for future work to be informed by these
approaches, advancing each component of LLM development and contributing to the
collective progress of LLMs as a whole.
8.2.2 Responsible Development
Thestudiesweexaminedhighlightedthegrowingemphasisonmeasurestoaddressthe
risksandsocietalimpactsofLLMresearch.Aprimaryfocusisonextensivedocumentation in dataset and model development, which is valuable not only for replicability
but also for transparency and awareness of both the ethical and technical limitations.
In-depth documentation, including examination and measurement of potential harmful risks and biases, has been a focal point across the objectives, methodologies, and
limitations of LLM research.
Additionally, we underscore the need for cautious considerations in how LLMs are
made available to the community and the importance of collaboration in the development and release of LLMs. Incorporating discussions of the limitations and impacts
of studies is becoming an essential component of research. Furthermore, we examine
studies that present considerations for more effective and efficient development, such
as optimal processing, parameters, and architectures.
8.3 Limitations
AlthoughthissystematicreviewaimstopresentacomprehensiveperspectiveonexaminingLLMresearchandtheimpactsofNLP,thereareseverallimitations.First,while
the literature search endeavored to include as diverse a range of articles as possible,
the possibility of missing relevant studies exists. While we experimented with several
repositories for scholarly literature in the early phases of this study, we used Google
Scholar to identify the final set of papers and to record the numbers for reporting
purposes. Google Scholar could be biased toward specific articles, and we should have
cross-referenced the returned results with other bibliometric databases to identify a
fairer collection of scholarly articles. To mitigate this in future research, more comprehensive queries that encompass a broader array of articles could be employed, and
a wider range of publication venues and bibliometric databases could be included.
Another limitation lies in the annotation of the themes of each paper. While we exercised due diligence in ensuring that categories and groupings were generated to best
represent the articles, with discussions following each analytical phase, involving a
larger number of reviewers could enhance the reliability, consistency, and replicability
of these qualitative themes.
19

<!-- Page 20 -->

9 Conclusion
LLMs are among the most influential developments in the field of NLP and AI, with
rapid advancements making significant technical and societal impacts. However, the
capabilities of LLMs are still rapidly evolving. Our aim was to examine the advancements and impacts of LLMs through a systematic review of studies on LLMs. The
results contribute to a better understanding of the capabilities of LLMs and LLM
researchmethodologies,thegoalsandavenuesofthefield,andtheresearchandethical
limitations in LLMs. We also emphasize the value of studies that aim to understand
and explain the workings of LLMs. Moreover, we identify best practices for responsible LLM development, offering recommendations for transparency, collaboration, and
awareness of research impacts. Beyond providing a view of the current progress of
LLM research, these potential directions can further assist in the growth and positive
impacts of LLMs.

### References

[1] Brown, T., Mann, B., Ryder, N., Subbiah, M., Kaplan, J.D., Dhariwal, P., Neelakantan, A., Shyam, P., Sastry, G., Askell, A., Agarwal, S., Herbert-Voss, A.,
Krueger,G.,Henighan,T.,Child,R.,Ramesh,A.,Ziegler,D.,Wu,J.,Winter,C.,
Hesse,C.,Chen,M.,Sigler,E.,Litwin,M.,Gray,S.,Chess,B.,Clark,J.,Berner,
C.,McCandlish,S.,Radford,A.,Sutskever,I.,Amodei,D.:Languagemodelsare
few-shot learners. In: Advances in Neural Information Processing Systems, vol.
33, pp. 1877–1901. Curran Associates, Inc., ??? (2020)
[2] Bender, E.M., Gebru, T., McMillan-Major, A., Shmitchell, S.: On the dangers of
stochastic parrots: Can language models be too big? In: Proceedings of the 2021
ACM Conference on Fairness, Accountability, and Transparency. FAccT ’21, pp.
610–623. Association for Computing Machinery, ??? (2021). https://doi.org/10.
1145/3442188.3445922
[3] Crowther, M., Lim, W., Crowther, M.A.: Systematic review and metaanalysis methodology 116(17), 3140–3146 (2010) https://doi.org/10.1182/
blood-2010-05-280883
[4] Manchikanti, L., Datta, S., Smith, H.S., Hirsch, J.A.: Evidence-based medicine,
systematic reviews, and guidelines in interventional pain management: part 6.
systematic reviews and meta-analyses of observational studies 12(5), 819–850
(2009)
[5] Tawfik,G.M.,Dila,K.A.S.,Mohamed,M.Y.F.,Tam,D.N.H.,Kien,N.D.,Ahmed,
A.M., Huy, N.T.: A step by step guide for conducting a systematic review and
meta-analysis with simulation data 47(1), 46 (2019) https://doi.org/10.1186/
s41182-019-0165-6
[6] Kelly,D.,Sugimoto,C.R.:Asystematicreviewofinteractiveinformationretrieval
evaluation studies, 1967–2006 64(4), 745–770 (2013)
20

<!-- Page 21 -->

[7] Vakkari, P.: The usefulness of search results: A systematization of types and predictors.In:Proceedingsofthe2020ConferenceonHumanInformationInteraction
and Retrieval, pp. 243–252. ACM, ??? (2020). https://doi.org/10.1145/3343413.
3377955
[8] Vassilakaki, E., Moniarou-Papaconstantinou, V.: A systematic literature review
informing library and information professionals’ emerging roles 116(1), 37–66
(2015) https://doi.org/10.1108/NLW-05-2014-0060
[9] Zawacki-Richter, O., Mar´ın, V.I., Bond, M., Gouverneur, F.: Systematic review
of research on artificial intelligence applications in higher education – where are
the educators? 16(1), 39 (2019) https://doi.org/10.1186/s41239-019-0171-0
[10] Lee,K.,Ippolito,D.,Nystrom,A.,Zhang,C.,Eck,D.,Callison-Burch,C.,Carlini,
N.: Deduplicating training data makes language models better. In: Muresan, S.,
Nakov,P.,Villavicencio,A.(eds.)Proceedingsofthe60thAnnualMeetingofthe
Association for Computational Linguistics (Volume 1: Long Papers), pp. 8424–

## Association for Computational Linguistics, ??? (2022). https://doi.org/10.

18653/v1/2022.acl-long.577
[11] Wang, A., Singh, A., Michael, J., Hill, F., Levy, O., Bowman, S.R.: GLUE: A
Multi-TaskBenchmarkandAnalysisPlatformforNaturalLanguageUnderstanding.arXiv.arXiv:1804.07461[cs](2019).https://doi.org/10.18653/v1/W18-5446
[12] Gehman, S., Gururangan, S., Sap, M., Choi, Y., Smith, N.A.: RealToxicityPrompts: Evaluating neural toxic degeneration in language models. In: Cohn,
T., He, Y., Liu, Y. (eds.) Findings of the Association for Computational Linguistics: EMNLP 2020, pp. 3356–3369. Association for Computational Linguistics,
??? (2020). https://doi.org/10.18653/v1/2020.findings-emnlp.301
[13] Zhang, S., Roller, S., Goyal, N., Artetxe, M., Chen, M., Chen, S., Dewan, C.,
Diab, M., Li, X., Lin, X.V., Mihaylov, T., Ott, M., Shleifer, S., Shuster, K.,
Simig, D., Koura, P.S., Sridhar, A., Wang, T., Zettlemoyer, L.: OPT: Open PretrainedTransformerLanguageModels.arXiv.arXiv:2205.01068[cs](2022).https:
//doi.org/10.48550/arXiv.2205.01068
[14] Carlini, N., Tramer, F., Wallace, E., Jagielski, M., Herbert-Voss, A., Lee, K.,
Roberts,A.,Brown,T.,Song,D.,Erlingsson,U.,Oprea,A.,Raffel,C.:Extracting
Training Data from Large Language Models. arXiv (2021). https://doi.org/10.
48550/arXiv.2012.07805
[15] Lester, B., Al-Rfou, R., Constant, N.: The power of scale for parameter-efficient
prompt tuning. In: Moens, M.-F., Huang, X., Specia, L., Yih, S.W.-t. (eds.)
Proceedings of the 2021 Conference on Empirical Methods in Natural Language
Processing,pp.3045–3059.AssociationforComputationalLinguistics,???(2021).
https://doi.org/10.18653/v1/2021.emnlp-main.243
21

<!-- Page 22 -->

[16] Hoffmann, J., Borgeaud, S., Mensch, A., Buchatskaya, E., Cai, T., Rutherford,
E., Casas, D.d.L., Hendricks, L.A., Welbl, J., Clark, A., Hennigan, T., Noland,
E., Millican, K., Driessche, G.v.d., Damoc, B., Guy, A., Osindero, S., Simonyan,
K.,Elsen,E.,Rae,J.W.,Vinyals,O.,Sifre,L.:TrainingCompute-OptimalLarge
Language Models. arXiv (2022). https://doi.org/10.48550/arXiv.2203.15556
[17] Kaplan, J., McCandlish, S., Henighan, T., Brown, T.B., Chess, B., Child, R.,
Gray, S., Radford, A., Wu, J., Amodei, D.: Scaling Laws for Neural Language
Models. arXiv (2020). https://doi.org/10.48550/arXiv.2001.08361
[18] Solaiman, I., Brundage, M., Clark, J., Askell, A., Herbert-Voss, A., Wu, J., Radford,A.,Krueger,G.,Kim,J.W.,Kreps,S.,McCain,M.,Newhouse,A.,Blazakis,
J.,McGuffie,K.,Wang,J.:ReleaseStrategiesandtheSocialImpactsofLanguage
Models. arXiv (2019). https://doi.org/10.48550/arXiv.1908.09203
[19] Raffel, C., Shazeer, N., Roberts, A., Lee, K., Narang, S., Matena, M., Zhou, Y.,
Li, W., Liu, P.J.: Exploring the Limits of Transfer Learning with a Unified Textto-Text Transformer. arXiv. arXiv:1910.10683 [cs, stat] (2019). https://doi.org/
10.48550/arXiv.1910.10683
[20] Fedus, W., Zoph, B., Shazeer, N.M.: Switch transformers: Scaling to trillion
parameter models with simple and efficient sparsity (2021)
[21] Rae,J.W.,Borgeaud,S.,Cai,T.,Millican,K.,Hoffmann,J.,Song,F.,Aslanides,
J., Henderson, S., Ring, R., Young, S., Rutherford, E., Hennigan, T., Menick, J.,
Cassirer, A., Powell, R., Driessche, G.v.d., Hendricks, L.A., Rauh, M., Huang,
P.-S., Glaese, A., Welbl, J., Dathathri, S., Huang, S., Uesato, J., Mellor, J.F.J.,
Higgins, I., Creswell, A., McAleese, N., Wu, A., Elsen, E., Jayakumar, S.M.,
Buchatskaya, E., Budden, D., Sutherland, E., Simonyan, K., Paganini, M.,
Sifre, L., Martens, L., Li, X.L., Kuncoro, A., Nematzadeh, A., Gribovskaya, E.,
Donato, D., Lazaridou, A., Mensch, A., Lespiau, J.-B., Tsimpoukelli, M., Grigorev, N., Fritz, D., Sottiaux, T., Pajarskas, M., Pohlen, T., Gong, Z., Toyama,
D., d’Autume, C.d.M., Li, Y., Terzi, T., Mikulik, V., Babuschkin, I., Clark,
A., Casas, D.d.L., Guy, A., Jones, C., Bradbury, J., Johnson, M.G., Hechtman,
B.A., Weidinger, L., Gabriel, I., Isaac, W.S., Lockhart, E., Osindero, S., Rimell,
L., Dyer, C., Vinyals, O., Ayoub, K.W., Stanway, J., Bennett, L., Hassabis,
D., Kavukcuoglu, K., Irving, G.: Scaling language models: Methods, analysis &
insights from training gopher (2021)
[22] Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A.N.,
Kaiser, L., Polosukhin, I.: Attention is all you need. In: Advances in Neural
Information Processing Systems, vol. 30. Curran Associates, Inc., ??? (2017)
[23] Zhang, Z., Han, X., Liu, Z., Jiang, X., Sun, M., Liu, Q.: ERNIE: Enhanced
language representation with informative entities. In: Korhonen, A., Traum, D.,
M`arquez, L. (eds.) Proceedings of the 57th Annual Meeting of the Association
for Computational Linguistics, pp. 1441–1451. Association for Computational
22

<!-- Page 23 -->

Linguistics, ??? (2019). https://doi.org/10.18653/v1/P19-1139
[24] Jiang, Z., Araki, J., Ding, H., Neubig, G.: How can we know when language
models know? on the calibration of language models for question answering 9,
962–977 (2021) https://doi.org/10.1162/tacl a 00407
[25] Chowdhery, A., Narang, S., Devlin, J., Bosma, M., Mishra, G., Roberts, A.,
Barham, P., Chung, H.W., Sutton, C., Gehrmann, S., Schuh, P., Shi, K.,
Tsvyashchenko, S., Maynez, J., Rao, A., Barnes, P., Tay, Y., Shazeer, N., Prabhakaran, V., Reif, E., Du, N., Hutchinson, B., Pope, R., Bradbury, J., Austin,
J., Isard, M., Gur-Ari, G., Yin, P., Duke, T., Levskaya, A., Ghemawat, S., Dev,
S., Michalewski, H., Garcia, X., Misra, V., Robinson, K., Fedus, L., Zhou, D.,
Ippolito, D., Luan, D., Lim, H., Zoph, B., Spiridonov, A., Sepassi, R., Dohan,
D., Agrawal, S., Omernick, M., Dai, A.M., Pillai, T.S., Pellat, M., Lewkowycz,
A., Moreira, E., Child, R., Polozov, O., Lee, K., Zhou, Z., Wang, X., Saeta, B.,
Diaz, M., Firat, O., Catasta, M., Wei, J., Meier-Hellstern, K., Eck, D., Dean, J.,
Petrov, S., Fiedel, N.: PaLM: Scaling language modeling with pathways 24(240),
1–113 (2022)
[26] CONNEAU, A., Lample, G.: Cross-lingual language model pretraining. In:
Advances in Neural Information Processing Systems, vol. 32. Curran Associates,

### Inc., ??? (2019)

[27] Wang, A., Pruksachatkun, Y., Nangia, N., Singh, A., Michael, J., Hill, F., Levy,
O., Bowman, S.R.: SuperGLUE: A Stickier Benchmark for General-Purpose
Language Understanding Systems. arXiv. arXiv:1905.00537 [cs] (2020). https:
//doi.org/10.48550/arXiv.1905.00537
[28] Kirchenbauer, J., Geiping, J., Wen, Y., Katz, J., Miers, I., Goldstein, T.: A
Watermark for Large Language Models. In: Proceedings of the 40th International Conference on Machine Learning, pp. 17061–17084. PMLR, ??? (2023).
https://proceedings.mlr.press/v202/kirchenbauer23a.html Accessed 2024-08-28
[29] Manakul, P., Liusie, A., Gales, M.J.F.: SelfCheckGPT: Zero-Resource Black-
Box Hallucination Detection for Generative Large Language Models. arXiv.
arXiv:2303.08896 [cs] (2023). https://doi.org/10.48550/arXiv.2303.08896 . http:
//arxiv.org/abs/2303.08896 Accessed 2024-08-28
[30] Turpin, M., Michael, J., Perez, E., Bowman, S.: Language Models Don’t Always
SayWhatTheyThink:UnfaithfulExplanationsinChain-of-ThoughtPrompting.
Advances in Neural Information Processing Systems 36, 74952–74965 (2023).

### Accessed 2024-08-28

[31] Sanh, V., Webson, A., Raffel, C., Bach, S.H., Sutawika, L., Alyafeai, Z., Chaffin,
A., Stiegler, A., Scao, T.L., Raja, A., Dey, M., Bari, M.S., Xu, C., Thakker, U.,
Sharma,S.S.,Szczechla,E.,Kim,T.,Chhablani,G.,Nayak,N.,Datta,D.,Chang,
23

<!-- Page 24 -->

J.,Jiang,M.T.-J.,Wang,H.,Manica,M.,Shen,S.,Yong,Z.X.,Pandey,H.,Bawden,R.,Wang,T.,Neeraj,T.,Rozen,J.,Sharma,A.,Santilli,A.,Fevry,T.,Fries,
J.A., Teehan, R., Bers, T., Biderman, S., Gao, L., Wolf, T., Rush, A.M.: Multitask Prompted Training Enables Zero-Shot Task Generalization. arXiv (2022).
https://doi.org/10.48550/arXiv.2110.08207
[32] Petroni, F., Rockt¨aschel, T., Riedel, S., Lewis, P., Bakhtin, A., Wu, Y., Miller,
A.:Languagemodelsasknowledgebases?In:Inui,K.,Jiang,J.,Ng,V.,Wan,X.
(eds.)Proceedingsofthe2019ConferenceonEmpiricalMethodsinNaturalLanguageProcessingandthe9thInternationalJointConferenceonNaturalLanguage
Processing (EMNLP-IJCNLP), pp. 2463–2473. Association for Computational
Linguistics, ??? (2019). https://doi.org/10.18653/v1/D19-1250
[33] Clark,K.,Luong,M.-T.,Le,Q.V.,Manning,C.D.:ELECTRA:Pre-trainingText
Encoders as Discriminators Rather Than Generators. arXiv (2020). https://doi.
org/10.48550/arXiv.2003.10555
[34] Dong,L.,Yang,N.,Wang,W.,Wei,F.,Liu,X.,Wang,Y.,Gao,J.,Zhou,M.,Hon,
H.-W.: Unified language model pre-training for natural language understanding
and generation. In: Advances in Neural Information Processing Systems, vol. 32.

### Curran Associates, Inc., ??? (2019)

[35] Zhao, Z., Wallace, E., Feng, S., Klein, D., Singh, S.: Calibrate before use:
Improving few-shot performance of language models. In: Proceedings of the 38th
International Conference on Machine Learning, pp. 12697–12706. PMLR, ???
(2021)
[36] Schick, T., Schu¨tze, H.: Exploiting cloze-questions for few-shot text classification
and natural language inference. In: Merlo, P., Tiedemann, J., Tsarfaty, R. (eds.)
Proceedings of the 16th Conference of the European Chapter of the Association
for Computational Linguistics: Main Volume, pp. 255–269. Association for Computational Linguistics, ??? (2021). https://doi.org/10.18653/v1/2021.eacl-main.
20
[37] Howard,J.,Ruder,S.:Universallanguagemodelfine-tuningfortextclassification.
In:Gurevych,I.,Miyao,Y.(eds.)Proceedingsofthe56thAnnualMeetingofthe
Association for Computational Linguistics (Volume 1: Long Papers), pp. 328–

## Association for Computational Linguistics, ??? (2018). https://doi.org/10.

18653/v1/P18-1031
[38] Gururangan, S., Marasovi´c, A., Swayamdipta, S., Lo, K., Beltagy, I., Downey,
D., Smith, N.A.: Don’t stop pretraining: Adapt language models to domains and
tasks. In: Jurafsky, D., Chai, J., Schluter, N., Tetreault, J. (eds.) Proceedings of
the 58th Annual Meeting of the Association for Computational Linguistics, pp.
8342–8360. Association for Computational Linguistics, ??? (2020). https://doi.
org/10.18653/v1/2020.acl-main.740
24

<!-- Page 25 -->

[39] Radford, A., Narasimhan, K., Salimans, T., Sutskever, I., et al.: Improving
language understanding by generative pre-training (2018)
[40] Jozefowicz,R.,Vinyals,O.,Schuster,M.,Shazeer,N.,Wu,Y.:ExploringtheLimits of Language Modeling. arXiv (2016). https://doi.org/10.48550/arXiv.1602.
02410
[41] Radford, A., Wu, J., Child, R., Luan, D., Amodei, D., Sutskever, I., et al.:
Language models are unsupervised multitask learners. OpenAI blog 1(8), 9
(2019)
[42] Shazeer, N., Mirhoseini, A., Maziarz, K., Davis, A., Le, Q., Hinton, G., Dean,
J.:OutrageouslyLargeNeuralNetworks:TheSparsely-GatedMixture-of-Experts
Layer. arXiv (2017). https://doi.org/10.48550/arXiv.1701.06538
[43] Radford,A.,Kim,J.W.,Hallacy,C.,Ramesh,A.,Goh,G.,Agarwal,S.,Sastry,G.,
Askell,A.,Mishkin,P.,Clark,J.,et al.:Learningtransferablevisualmodelsfrom
natural language supervision. In: International Conference on Machine Learning,
pp. 8748–8763 (2021). PMLR
[44] Alayrac, J.-B., Donahue, J., Luc, P., Miech, A., Barr, I., Hasson, Y., Lenc, K.,
Mensch, A., Millican, K., Reynolds, M., Ring, R., Rutherford, E., Cabi, S., Han,
T., Gong, Z., Samangooei, S., Monteiro, M., Menick, J.L., Borgeaud, S., Brock,
A., Nematzadeh, A., Sharifzadeh, S., Bin´kowski, M., Barreira, R., Vinyals, O.,
Zisserman, A., Simonyan, K.: Flamingo: a visual language model for few-shot
learning 35, 23716–23736 (2022)
[45] Devlin, J., Chang, M.-W., Lee, K., Toutanova, K.: BERT: Pre-training of deep
bidirectional transformers for language understanding. In: Burstein, J., Doran,
C., Solorio, T. (eds.) Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language
Technologies,Volume1(LongandShortPapers),pp.4171–4186.Associationfor
Computational Linguistics, ??? (2019). https://doi.org/10.18653/v1/N19-1423
[46] Liu, X., He, P., Chen, W., Gao, J.: Multi-task deep neural networks for natural language understanding. In: Korhonen, A., Traum, D., M`arquez, L. (eds.)
Proceedings of the 57th Annual Meeting of the Association for Computational
Linguistics,pp.4487–4496.AssociationforComputationalLinguistics,???(2019).
https://doi.org/10.18653/v1/P19-1441
[47] Dauphin, Y.N., Fan, A., Auli, M., Grangier, D.: Language Modeling with
Gated Convolutional Networks. arXiv (2017). https://doi.org/10.48550/arXiv.
1612.08083
[48] Press,O.,Wolf,L.:Usingtheoutputembeddingtoimprovelanguagemodels.In:
Lapata, M., Blunsom, P., Koller, A. (eds.) Proceedings of the 15th Conference of
the European Chapter of the Association for Computational Linguistics: Volume
25

<!-- Page 26 -->

2, Short Papers, pp. 157–163. Association for Computational Linguistics, ???
(2017)
[49] Dai,Z.,Yang,Z.,Yang,Y.,Carbonell,J.,Le,Q.,Salakhutdinov,R.:Transformer-
XL: Attentive language models beyond a fixed-length context. In: Korhonen,
A., Traum, D., M`arquez, L. (eds.) Proceedings of the 57th Annual Meeting of
the Association for Computational Linguistics, pp. 2978–2988. Association for
Computational Linguistics, ??? (2019). https://doi.org/10.18653/v1/P19-1285
[50] Conneau, A., Khandelwal, K., Goyal, N., Chaudhary, V., Wenzek, G., Guzm´an,
F.,Grave,E.,Ott,M.,Zettlemoyer,L.,Stoyanov,V.:UnsupervisedCross-lingual
Representation Learning at Scale. arXiv. arXiv:1911.02116 [cs] (2020). https://
doi.org/10.18653/v1/2020.acl-main.747
[51] He, P., Liu, X., Gao, J., Chen, W.: DeBERTa: Decoding-enhanced BERT
withDisentangledAttention.arXiv(2021).https://doi.org/10.48550/arXiv.2006.
03654
[52] Yang,Z.,Dai,Z.,Yang,Y.,Carbonell,J.,Salakhutdinov,R.R.,Le,Q.V.:XLNet:
Generalized autoregressive pretraining for language understanding. In: Advances
in Neural Information Processing Systems, vol. 32. Curran Associates, Inc., ???
(2019)
[53] Roberts, A., Raffel, C., Shazeer, N.: How much knowledge can you pack into the
parametersofalanguagemodel?In:Webber,B.,Cohn,T.,He,Y.,Liu,Y.(eds.)
Proceedings of the 2020 Conference on Empirical Methods in Natural Language
Processing(EMNLP),pp.5418–5426.AssociationforComputationalLinguistics,
??? (2020). https://doi.org/10.18653/v1/2020.emnlp-main.437
[54] Kandpal, N., Deng, H., Roberts, A., Wallace, E., Raffel, C.: Large Language
ModelsStruggletoLearnLong-TailKnowledge.In:Proceedingsofthe40thInternational Conference on Machine Learning, pp. 15696–15707. PMLR, ??? (2023).
https://proceedings.mlr.press/v202/kandpal23a.html Accessed 2024-08-28
[55] Zhang, Z., Sheng, Y., Zhou, T., Chen, T., Zheng, L., Cai, R., Song, Z., Tian, Y.,
R´e,C.,Barrett,C.,Wang,Z.A.,Chen,B.:H2O:Heavy-HitterOracleforEfficient
GenerativeInferenceofLargeLanguageModels.AdvancesinNeuralInformation
Processing Systems 36, 34661–34710 (2023). Accessed 2024-08-28
[56] Huang, S., Dong, L., Wang, W., Hao, Y., Singhal, S., Ma, S., Lv, T., Cui, L.,
Mohammed, O.K., Patra, B., Liu, Q., Aggarwal, K., Chi, Z., Bjorck, N., Chaudhary, V., Som, S., Song, X., Wei, F.: Language Is Not All You Need: Aligning
Perception with Language Models. Advances in Neural Information Processing

### Systems 36, 72096–72109 (2023). Accessed 2024-08-28

[57] Schick, T., Dwivedi-Yu, J., Dessi, R., Raileanu, R., Lomeli, M., Hambro, E.,
Zettlemoyer, L., Cancedda, N., Scialom, T.: Toolformer: Language Models Can
26

<!-- Page 27 -->

Teach Themselves to Use Tools. Advances in Neural Information Processing

### Systems 36, 68539–68551 (2023). Accessed 2024-08-28

[58] Yao,S.,Yu,D.,Zhao,J.,Shafran,I.,Griffiths,T.,Cao,Y.,Narasimhan,K.:Tree
ofThoughts:DeliberateProblemSolvingwithLargeLanguageModels.Advances
in Neural Information Processing Systems 36, 11809–11822 (2023). Accessed
2024-08-28
[59] Wang, W., Chen, Z., Chen, X., Wu, J., Zhu, X., Zeng, G., Luo, P., Lu, T., Zhou,
J., Qiao, Y., Dai, J.: VisionLLM: Large Language Model is also an Open-Ended
Decoder for Vision-Centric Tasks. Advances in Neural Information Processing

### Systems 36, 61501–61513 (2023). Accessed 2024-08-28

[60] Gruver, N., Finzi, M., Qiu, S., Wilson, A.G.: Large Language Models Are Zero-
ShotTimeSeriesForecasters.AdvancesinNeuralInformationProcessingSystems
36, 19622–19635 (2023). Accessed 2024-08-28
[61] Le Scao, T., Rush, A.: How many data points is a prompt worth? In: Toutanova,
K., Rumshisky, A., Zettlemoyer, L., Hakkani-Tur, D., Beltagy, I., Bethard, S.,
Cotterell,R.,Chakraborty,T.,Zhou,Y.(eds.)Proceedingsofthe2021Conference
oftheNorthAmericanChapteroftheAssociationforComputationalLinguistics:
Human Language Technologies, pp. 2627–2636. Association for Computational
Linguistics, ??? (2021). https://doi.org/10.18653/v1/2021.naacl-main.208
[62] Nie, Y., Williams, A., Dinan, E., Bansal, M., Weston, J., Kiela, D.: Adversarial NLI: A new benchmark for natural language understanding. In: Jurafsky,
D., Chai, J., Schluter, N., Tetreault, J. (eds.) Proceedings of the 58th Annual
Meeting of the Association for Computational Linguistics, pp. 4885–4901. Association for Computational Linguistics, ??? (2020). https://doi.org/10.18653/v1/
2020.acl-main.441
[63] Wei, J., Wang, X., Schuurmans, D., Bosma, M., Ichter, B., Xia, F., Chi, E., Le,
Q.V., Zhou, D.: Chain-of-thought prompting elicits reasoning in large language
models 35, 24824–24837 (2022)
[64] Clark, K., Khandelwal, U., Levy, O., Manning, C.D.: What does BERT look at?
an analysis of BERT’s attention. In: Linzen, T., Chrupa{\textbackslash}la, G.,
Belinkov, Y., Hupkes, D. (eds.) Proceedings of the 2019 ACL Workshop BlackboxNLP: Analyzing and Interpreting Neural Networks For NLP, pp. 276–286.
AssociationforComputationalLinguistics,???(2019).https://doi.org/10.18653/
v1/W19-4828
[65] Biderman, S., Schoelkopf, H., Anthony, Q.G., Bradley, H., O’Brien, K., Hallahan, E., Khan, M.A., Purohit, S., Prashanth, U.S., Raff, E., Skowron, A.,
Sutawika, L., Wal, O.V.D.: Pythia: A Suite for Analyzing Large Language
Models Across Training and Scaling. In: Proceedings of the 40th International Conference on Machine Learning, pp. 2397–2430. PMLR, ??? (2023).
27

<!-- Page 28 -->

https://proceedings.mlr.press/v202/biderman23a.html Accessed 2024-08-28
[66] Schaeffer,R.,Miranda,B.,Koyejo,S.:AreEmergentAbilitiesofLargeLanguage
ModelsaMirage?AdvancesinNeuralInformationProcessingSystems36,55565–
55581 (2023). Accessed 2024-08-28
[67] Gao,T.,Fisch,A.,Chen,D.:Makingpre-trainedlanguagemodelsbetterfew-shot
learners. In: Zong, C., Xia, F., Li, W., Navigli, R. (eds.) Proceedings of the 59th
Annual Meeting of the Association for Computational Linguistics and the 11th
InternationalJointConferenceonNaturalLanguageProcessing(Volume1:Long
Papers), pp. 3816–3830. Association for Computational Linguistics, ??? (2021).
https://doi.org/10.18653/v1/2021.acl-long.295
[68] Saharia, C., Chan, W., Saxena, S., Li, L., Whang, J., Denton, E., Ghasemipour,
S.K.S.,Ayan,B.K.,Mahdavi,S.S.,Lopes,R.G.,Salimans,T.,Ho,J.,Fleet,D.J.,
Norouzi,M.:PhotorealisticText-to-ImageDiffusionModelswithDeepLanguage
Understanding. arXiv (2022). https://doi.org/10.48550/arXiv.2205.11487
28