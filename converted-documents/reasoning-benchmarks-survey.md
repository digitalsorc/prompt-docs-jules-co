---
title: "Reasoning Benchmarks Survey"
original_file: "./Reasoning_Benchmarks_Survey.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["llm", "rag", "chain-of-thought", "fine-tuning", "evaluation"]
keywords: ["data", "learning", "model", "imaging", "based", "radiomics", "study", "clinical", "documented", "tissue"]
summary: "<!-- Page 1 -->


### Title page

Title: AI in radiological imaging of soft-tissue and bone tumours: a systematic review
evaluating against CLAIM and FUTURE-AI guidelines
Authors: Douwe J. Spaanderman MSc1*, Matthew Marzetti MSc2,3*, Xinyi Wan MSc1*, Andrew
F. Visser MD,
PhD1, Robert Hemke MD, PhD6, Kirsten van Langevelde MD, PhD7, David F."
related_documents: []
---

# Reasoning Benchmarks Survey

<!-- Page 1 -->


### Title page

Title: AI in radiological imaging of soft-tissue and bone tumours: a systematic review
evaluating against CLAIM and FUTURE-AI guidelines
Authors: Douwe J. Spaanderman MSc1*, Matthew Marzetti MSc2,3*, Xinyi Wan MSc1*, Andrew
F. Scarsbrook MD4,5, Philip Robinson MD4, Edwin H.G. Oei MD, PhD1, Jacob J. Visser MD,
PhD1, Robert Hemke MD, PhD6, Kirsten van Langevelde MD, PhD7, David F. Hanff MD1,
Geert J.L.H. van Leenders MD, PhD8, Cornelis Verhoef MD, PhD9, Dirk J. Grünhagen MD,
PhD9, Wiro J. Niessen PhD1,10, Stefan Klein PhD1,† , Martijn P.A. Starmans PhD1,8,†
*Shared first author
†Shared last author

### Affiliations:


## Department of Radiology and Nuclear Medicine, Erasmus MC Cancer Institute, University


### Medical Center Rotterdam, Rotterdam, the Netherlands


## Department of Medical Physics, Leeds Teaching Hospitals NHS Trust, UK


## Leeds Biomedical Research Centre, University of Leeds, UK


## Department of Radiology, Leeds Teaching Hospitals NHS Trust, UK


## Leeds Institute of Medical Research, University of Leeds, UK


## Department of Radiology and Nuclear Medicine, Amsterdam UMC, Amsterdam, the


### Netherlands


## Department of Radiology, Leiden University Medical Center, Leiden, the Netherlands


## Department of Pathology, Erasmus MC Cancer Institute, University Medical Center


### Rotterdam, Rotterdam, the Netherlands


## Department of Surgical Oncology, Erasmus MC Cancer Institute, University Medical Center


### Rotterdam, Rotterdam, the Netherlands


## Faculty of Medical Sciences, University of Groningen, Groningen, the Netherlands

Corresponding author

### Douwe J. Spaanderman

Internal postal address: P.O. Box 2040, 3000 CA Rotterdam, the Netherlands, Na-2624
Visiting address: office Na-2624, Dr. Molewaterplein 40, 3015 GD Rotterdam, the Netherlands
d.spaanderman@erasmusmc.nl
+31-10-7041026

### Authors addresses

Douwe J. Spaanderman

<!-- Page 2 -->

Department of Radiology and Nuclear Medicine, Erasmus MC Cancer Institute, University
Medical Center Rotterdam, Dr. Molewaterplein 40, 3015 GD Rotterdam, the Netherlands

### Matthew Marzetti

Department of Medical Physics, Level 1, Bexley Wing, St James’s University Hospital, Beckett
Street, Leeds, West Yorkshire, LS9 7TF, United Kingdom

### Xinyi Wan

Department of Radiology and Nuclear Medicine, Erasmus MC Cancer Institute, University
Medical Center Rotterdam, Dr. Molewaterplein 40, 3015 GD Rotterdam, the Netherlands

### Andrew F. Scarsbrook

Department of Nuclear Medicine, Level 1, Bexley Wing, St James’s University Hospital,
Beckett Street, Leeds, West Yorkshire, LS9 7TF, United Kingdom

### Philip Robinson

Leeds Biomedical Research Centre, University of Leeds, Chapel Allerton Hospital,
Chapeltown Road, Leeds, LS7 4SA, United Kingdom

### Edwin H.G. Oei

Department of Radiology and Nuclear Medicine, Erasmus MC Cancer Institute, University
Medical Center Rotterdam, Dr. Molewaterplein 40, 3015 GD Rotterdam, the Netherlands

### Jacob J. Visser

Department of Radiology and Nuclear Medicine, Erasmus MC Cancer Institute, University
Medical Center Rotterdam, Dr. Molewaterplein 40, 3015 GD Rotterdam, the Netherlands

### Robert Hemke

Department of Radiology and Nuclear Medicine, Amsterdam University Medical Center
Meibergdreef 9, 1105AZ Amsterdam, the Netherlands

### Kirsten van Langevelde

Department of Radiology, Leiden University Medical Center
Albinusdreef 2, 2333 ZA Leiden, the Netherlands

### David F. Hanff

Department of Radiology and Nuclear Medicine, Erasmus MC Cancer Institute, University
Medical Center Rotterdam, Dr. Molewaterplein 40, 3015 GD Rotterdam, the Netherlands

<!-- Page 3 -->


### Geert J.L.H. van Leenders

Department of Pathology, Erasmus MC Cancer Institute, University Medical Center Rotterdam,
Dr. Molewaterplein 40, 3015 GD Rotterdam, the Netherlands

### Cornelis Verhoef

Department of Surgical Oncology, Erasmus MC Cancer Institute, University Medical Center

### Rotterdam,

Dr. Molewaterplein 40, 3015 GD Rotterdam, the Netherlands

### Dirk J. Grünhagen

Department of Surgical Oncology, Erasmus MC Cancer Institute, University Medical Center
Rotterdam, Dr. Molewaterplein 40, 3015 GD Rotterdam, the Netherlands

### Wiro J. Niessen


### Faculty of Medical Sciences, University of Groningen

Antonius Deusinglaan 1, 9713 AV Groningen, the Netherlands

### Martijn P.A. Starmans

Department of Radiology and Nuclear Medicine, Erasmus MC Cancer Institute, University
Medical Center Rotterdam, Dr. Molewaterplein 40, 3015 GD Rotterdam, the Netherlands

### Stefan Klein

Department of Radiology and Nuclear Medicine, Erasmus MC Cancer Institute, University
Medical Center Rotterdam, Dr. Molewaterplein 40, 3015 GD Rotterdam, the Netherlands

<!-- Page 4 -->


### Title:

AI in radiological imaging of soft-tissue and bone tumours: a systematic review evaluating
against CLAIM and FUTURE-AI guidelines

### Summary


### Background:

Soft-tissue and bone tumours (STBT) are rare, diagnostically challenging lesions with variable
clinical behaviours and treatment approaches. This systematic review aims to provide an
overview of Artificial Intelligence (AI) methods using radiological imaging for diagnosis and
prognosis of these tumours, highlighting challenges in clinical translation, and evaluating study
alignment with the Checklist for AI in Medical Imaging (CLAIM) and the FUTURE-AI
international consensus guidelines for trustworthy and deployable AI to promote the clinical
translation of AI methods.

### Methods:

The systematic review identified literature from several bibliographic databases, covering
papers published before 17/07/2024. Original research published in peer-reviewed journals,
focused on radiology-based AI for diagnosis or prognosis of primary STBT was included.
Exclusion criteria were animal, cadaveric, or laboratory studies, and non-English papers.
Abstracts were screened by two of three independent reviewers to determine eligibility.
Included papers were assessed against the two guidelines by one of three independent
reviewers. The review protocol was registered with PROSPERO (CRD42023467970).

### Findings:

The search identified 15,015 abstracts, from which 325 articles were included for evaluation.
Most studies performed moderately on CLAIM, averaging a score of 28∙9±7∙5 out of 53, but
poorly on FUTURE-AI, averaging 5∙1±2∙1 out of 30.

### Interpretations:

Imaging-AI tools for STBT remain at the proof-of-concept stage, indicating significant room
for improvement. Future efforts by AI developers should focus on design (e.g. define unmet
clinical need, intended clinical setting and how AI would be integrated in clinical workflow),
development (e.g. build on previous work, training with data that reflect real-world usage,
explainability), evaluation (e.g. ensuring biases are evaluated and addressed, evaluating AI
against current best practices), and the awareness of data reproducibility and availability
(making documented code and data publicly available). Following these recommendations
could improve clinical translation of AI methods.

<!-- Page 5 -->


### Funding:

Hanarth Fonds, ICAI Lab, NIHR, EuCanImage.

### Keywords:

Systematic Review; Soft-tissue and bone tumours; Radiological imaging; Artificial
Intelligence; Medical Image Analysis, FUTURE-AI, CLAIM.

### Panel 1


### Research in context


### Evidence before this study

Research on the use of AI in diagnosing and predicting the outcomes of soft-tissue and bone
tumours (STBT) is becoming more prevalent. However, the clinical adoption of AI methods in
this field remains limited, highlighting a significant gap between AI development and its
practical implementation in healthcare settings. Previous reviews focused on the accuracy and
performance of published STBT tools, however, did not investigate the quality of research.
Recent efforts have introduced guidelines with comprehensive criteria specifically designed for
structured reporting and responsible development, deployment, and governance of trustworthy
AI in healthcare.

### Added value of this study

This review examines the methodological quality of published literature by assessing it against
two best-practice guidelines, which were chosen to complement each other and cover a wide
range of criteria. Aspects related to study quality, study design, and trustworthy and deployable
AI, as assessed in this review using the CLAIM and FUTURE-AI guidelines, may be even more
important factors than their performance for assessing their potential translation to the clinic.
This review highlights what the field is doing well and where future research should focus. The
review includes all research using AI methods investigating STBT, giving it a far wider scope
than previous reviews. Furthermore, this is a fast-moving field, hence updates on previous
reviews are required.

### Implications of all the available evidence

Currently published AI methods are producing promising proof-of-concept results but are not
ready for clinical application. This work highlights opportunities and provides
recommendations for AI developers and clinical professionals for future research to drive
clinical implementation.

<!-- Page 6 -->


### Introduction

Primary soft-tissue and bone tumours (STBT) are among the rarest neoplasms in humans,
comprising both benign and malignant lesions. Malignant STBT, i.e. sarcoma, account for
approximately 1% of all neoplasms.1 These tumours may occur at any age and almost any
anatomical site, arising from cells of the connective tissue, including muscles, fat, blood
vessels, cartilage, and bones.2 The rarity of STBT, along with their diverse subtypes and varied
clinical behaviour, poses substantial challenges in accurate diagnosis and prognosis.
Radiological imaging (including nuclear medicine) is crucial in evaluating and monitoring
STBT. Technological advancements in imaging modalities have led to a substantial increase
data volume, along with a corresponding growth in the expertise required for its interpretation.
The growing utilisation of radiological imaging and complexity of analysis has increased
radiologists’ workload. Therefore, developing intelligent computer-aided systems and
algorithms for automated image analysis that can achieve faster and more accurate results is
crucial.3 For STBT, intelligent systems may help non-specialised radiologists in diagnosing rare
cancers more effectively. Furthermore, an increased caseload is associated with higher
interpretive error, which can be avoided with computer-aided diagnostic tools.4,5
Artificial intelligence (AI) has become increasingly prevalent in medical image analysis. Over
the last 7 years, the number of FDA-approved medical imaging AI products for radiology has
substantially increased.6 However, while medical imaging AI research in STBT has also
substantially increased, there are no products developed for STBT among the FDA-approved
list.7 Hence, instead of purely developing novel technological solutions, more research should
focus on aligning with areas of unmet clinical need.
Therefore, a systematic assessment of current published research is necessary to identify the
issues required to overcome the translational barrier. This systematic review aims to evaluate
the existing literature on AI for diagnosis and prognosis of STBT using radiological imaging
against two best practice guidelines; CLAIM and FUTURE-AI.8,9 CLAIM, endorsed by the
Radiological Society of North America (RSNA), promotes comprehensive reporting of
radiological research that uses AI. FUTURE-AI proposes ethical and technical standards to
ensure responsible development, deployment, and governance of trustworthy AI in healthcare.
Utilising both guidelines allows for comprehensive coverage of different aspects of AI
research.10 Additionally, this review discusses opportunities for future research to bridge the
identified gap between AI research and clinical use in STBT.

<!-- Page 7 -->


### Methods

This systematic review was prospectively registered with PROSPERO (CRD42023467970)
and adheres to the Preferred Reporting Items for Systematic Reviews and Meta-analyses
(PRISMA) 2020 guidelines.11 The full study protocol can be found online .12

### Search strategy and selection criteria

Medline, Embase, Web of Science core collection, Google Scholar, and Cochrane Central
Register of Controlled Trials were systematically searched for relevant studies. All papers
published before 27/09/2023 were included in the initial search; the starting date depended on
the coverage of the respective database searched. The detailed search strategy is listed in
Appendix 1. The literature search was conducted by the Medical Library, Erasmus MC,
Rotterdam, the Netherlands. The database search was repeated on 17/07/2024 to update
publications.
Inclusion criteria were: (1) original research papers published in peer-reviewed journals, and
(2) studies focusing on radiology-based AI or radiomics characterisation of primary tumours
located in bone and/or soft tissues for tasks related to diagnosis or prognosis, e.g. no pure
segmentation studies. Exclusion criteria were: (1) animal, cadaveric, or laboratory studies, and
(2) not written in English language.
The complete reviewing methodology is illustrated in Figure 1. Three independent reviewers
participated in title-and-abstract screening (DS, MM, XW). Retrieved papers were randomly
divided into three batches. Reviewers 1 and 2 reviewed one batch, Reviewers 1 and 3 reviewed
a second batch, and Reviewers 2 and 3 reviewed the final batch. In cases where there were
disagreements in the screening of an abstract, the third reviewer who was not initially involved
in reviewing the specific abstract, adjudicated any conflicts.

### Data analysis

Each paper was scored according to CLAIM and FUTURE-AI guidelines. Checklists were
developed based on each guideline. Blank checklists are available in Appendix 2. These
guidelines were chosen for their complimentary nature and comprehensive coverage of clinical

### AI tool requirements.10

The CLAIM checklist was adapted from the checklist implemented by Si et. al. to contain more
detail in some of the more general checklist items.8,13,14 CLAIM consists of 44 items, covering
the following sections: title, abstract, introduction, methods, results, discussion, and other
information. The majority of items focus on the methods (30/44 items). The Methods section
is further divided into the following subsections: Study design, Data, Ground truth, Data

<!-- Page 8 -->

partition, Testing data, Model, Training, and Evaluation. Similarly, the Results section is
divided into Data and Model performance. We further divided three items into twelve sub-items
to provide more detailed information. These were: (4) Study objectives and hypotheses (4a and
4b), (7) Data sources (7a-d), and (9) Data preprocessing steps (9a-f). The adapted CLAIM
checklist totalled 53 items.
The FUTURE-AI checklist was created from the FUTURE-AI guideline and contains 30 items.9
These items are split according to the six FUTURE-AI principles: Fairness (3), Universality
(4), Traceability (6), Usability (5), Robustness (3), Explainability (2), and General (7).
Additionally, FUTURE-AI specifies guidelines for AI tools at various machine learning
technology readiness levels (TRL). It recommends (+) or strongly recommends (++) specific
guidelines for tools at the proof-of-concept stage (Research) and for those intended for clinical
development (Deployable).
All items in both sets of guidelines were scored between 0 and 1, with 0 meaning the item was
not addressed, 0∙5 meaning it was partially addressed (where relevant and only in FUTURE-
AI) and 1 meaning it was fully addressed.
To ensure consistency between scores among reviewers, a subset of papers (n=45) was selected
for independent review by all three reviewers. The subset was selected by ordering the papers
alphabetically based on the first author’s name and choosing the first 45 papers from this order
in the initial search. The number of disagreements for each item in either guideline was
recorded, and inter-reader variability for each guideline was measured by calculating Fleiss'
Kappa statistics (κ).15 Fleiss kappa statistics were interpreted according to the guidance given
by Fleiss et al., with a score 0–0∙4 indicating poor agreement, 0∙41–0∙75 showing good
agreement and >0∙75 showing excellent agreement.15 To construct 95% confidence intervals
(95% CI) for the inter-reader variability, 1000× bootstrap resampling was employed. The
percentage agreement between all three reviewers was calculated for each item. Following this
a consensus discussion was conducted between all three reviewers, allowing discussion and
resolution of any systematic differences in interpretation and scoring of specific items. Next,
each reviewer re-scored the same subset a second time, several weeks after the first scoring.
Kappa statistics and percentage agreements were re-calculated.
After consensus, the remaining included papers were equally divided between the three
reviewers and reviewed by a single reviewer. If a reviewer was uncertain how to score a paper,
they consulted one or more of the other reviewers for confirmation or discussion. In addition to
scoring the CLAIM and FUTURE-AI checklists, the following information was recorded for
each paper: (1) year of publication, (2) journal of publication, (3) disease type investigated (soft

<!-- Page 9 -->

tissue sarcoma, bone sarcoma, or gastrointestinal stromal tumour – GIST), (4) study design
(retrospective or prospective – if a study used both retrospectively and prospectively acquired
data it was recorded as being a prospective study), (5) outcome predicted (diagnosis, prognosis,
or both), (6) imaging modality (MRI, CT, ultrasound, X-ray, PET-CT, PET-MRI, scintigraphy,
or multiple imaging modalities), (7) data source (public, single centre, or multi-centre), and (8)
availability of data and AI model source code.
The performance metrics of the corresponding AI models were collected for the top 20
performing papers, as determined by their combined CLAIM and FUTURE-AI scores, that
performed external validation. Only the top 20 papers were included for this analysis as reported
model performance cannot be reliably reproduced or considered clinically meaningful as low
scoring studies lack methodological transparency or do not adhere to best scientific practices.
For the same reason, only externally validated papers were selected to ensure robust assessment
of model generalizability, reducing the risk of overfitting and dataset-specific bias, thus
strengthening the clinical relevance of the reported findings.

### Statistics

The number of papers adhering to each item of CLAIM/FUTURE-AI was calculated.
Descriptive statistics of how well papers scored in each (sub)section/principle were calculated,
including mean, standard deviation (SD), maximum, and minimum score, as well as the mean
and SD of the guideline adherence rate (AR), which is the score divided by the maximum
achievable score.

### Role of Funders

The funder of the study had no role in study design, data collection, data analysis, data
interpretation, or writing of the report.

### Ethics

This study is a systematic review of published work and thus ethical approval was deemed
unnecessary.

<!-- Page 10 -->


### Results

Database searches identified 15,015 published studies, with 5,667 duplicates. After screening,
454 articles were retained for full-text review. After excluding 129 studies a total of 325 unique
studies were included in the systematic review (Figure 2). Fifteen of the excluded papers were
part of the reproducibility subgroup, meaning 30 articles were independently reviewed by all
reviewers. A complete reference list of the final 325 included papers is provided in Appendix

## Main reasons for exclusion were focusing on different entities (e.g. renal cancer), no use of

radiological imaging, or lacking AI-based analysis.
Included studies were published between 2008 and 2024, mostly in the last five years (Figure
3). Of the 325 included studies, most AI methods used hand-crafted imaging features with
machine learning (n=221, 68%). Recently, more AI methods used model-learned imaging
features (n=62, 19%), i.e. deep learning, or a combination of model-learned and hand-crafted
imaging features with machine learning (n=29, 9%). Thirteen studies used hand-crafted
imaging features without machine learning.
Study characteristics are illustrated in Figure 4. Disease types included soft tissue tumours
(n=125, 38·5%), bone tumours (n=114, 35·1%), and GIST (n=82, 25·2%). Only four studies
included both soft tissue and bone tumours (1·2%). Study design was mostly retrospective
(n=272, 83.7%), with fewer prospective studies (n=38, 11·7%), and a minority where study
design was not clearly documented (n=15, 4·6%). The majority of reports focused on
developing AI methods to predict diagnosis (n=206, 63·4%), 109 (33·5%) evaluated prognosis,
and 10 (3·1%) studied a combination of diagnosis and prognosis of the disease. Various
radiological techniques were evaluated, with 144 (44·3%) studies using MRI, 94 (28·9%) CT,
34 (10·5%) ultrasound, 30 (9·2%) X-ray, 10 (3∙1%) PET-CT, 3 (0·9%) PET-MRI, and 1 (0∙3%)
scintigraphy, and 9 (2·8%) multiple modalities. One-hundred-and-ninety (58∙5%) studies
collected data from a single centre, whereas 93 (28·6%) utilised imaging from multiple centres.
Nineteen studies did not clearly document data provenance (5·8%). Furthermore, 23 (7·1%)
studies used publicly available data from two sources (Table 1). AI methods were most often
validated with separate internal test data (n=214, 65·8%), and sometimes additionally with
external test data (n=70, 21∙5%). Several AI methods were not validated with independent data
or validation was not clearly documented (n=41, 12·6%). Only 5 (1∙5%) studies made data
available, with 238 (73·2%) studies not providing or not specifying data availability, and 82
(25·2%) studies stating data would be made available on reasonable request. Similarly, AI
source code to facilitate reproducibility was only made available in 23 (7·1%) studies, with 287
(88·3%) not providing or not specifying code availability, and 15 (4∙6%) studies indicating
code would be made available on reasonable request.

<!-- Page 11 -->

Kappa statistics for inter-reader variability increased from 0∙58 (95% CI: [0∙55, 0∙62]) and 0∙68
(95% CI: [0∙61, 0∙75]) for CLAIM and FUTURE-AI before consensus discussion, to 0∙80 (95%
CI: [0∙78, 0∙83]) and 0∙92 (95% CI: [0∙88, 0∙95]) after, showing excellent agreement
(Supplementary Figure S1 and S2).
Individual scores for each item in Figure 5 for CLAIM and 6 for FUTURE-AI. Section level
scores are provided in Table 2 and 3. Scores by year are available in Supplementary Figure S3
and S4, both showing an increasing trend. Scores by tumour type, method type, and outcome
are available in Supplementary Figures S5 and S6, all showing no clear distinction between
groups. Individual paper scores for each item are documented in Supplementary Figures S7 and
S8, and are also available online as interactive figures and tables.16
The included studies performed moderately on the CLAIM checklist, with a mean score of 28∙9
out of 53 (SD: 7∙5, min–max: 4∙0–48∙0, AR mean±SD: 55%±14%). All items were reported at
least once, but several were only reported in less than 15% of the papers (n≤50 papers)
including: define a study hypothesis at the design phase (CLAIM-4b, 13∙8%), data deidentification methods (CLAIM-11, 3∙4%), how missing data were handled (CLAIM-12,
8∙2%), intended sample size and how it was determined (CLAIM-21, 4%), robustness or
sensitivity analysis (CLAIM-30, 13∙8%), methods for explainability or interpretability
(CLAIM-31, 12·9%), registration number and name of registry (CLAIM-34, 2∙8%), and
documented where full study protocol can be accessed (CLAIM-42, 12·3%).
The included studies rarely adhered to FUTURE-AI, with a mean score of 5∙1 out of 30 (SD:
2∙1, min–max: 0–11·5, AR: 17%±7%). From the 30 items, 5 were never reported. Only 6 items
were partially reported in over half of the reviewed papers (n>162) including: collecting and
reporting on individuals' attributes (Fairness-2, 83∙1%), using community-defined standards
(Universality-2, 56%), defining use and user requirements (Usability-1, 85·2%), engaging
interdisciplinary stakeholders (General-1, 86·2%), implementing measures for data privacy and
security (General-2, 85·2%), and defining an adequate evaluation plan (General-4, 67·7%).
Strongly recommended items by FUTURE-AI for proof-of-concept AI studies (Research), were
reported more frequently than recommended items, with mean scores of 2·9 out of 12 (SD: 1∙1,
min–max: 0–7, AR: 24%±9%) and 2·3 out of 16 (SD: 1∙2, min–max: 0–6∙5, AR: 14%±8%),
respectively. However, this trend was not observed in items intended to assess studies for
clinical deployability (Deployable), where the mean scores were 3∙8 out of 24 (SD: 1∙7, min–
max: 0–10, AR: 16%±7%) for strongly recommended items and 1∙3 out of 4 (SD: 0∙7, min–
max: 0–3, AR: 33%±18%) for recommended items.

<!-- Page 12 -->

Performance measurements of the top 20 performing papers (summed score of both CLAIM
and FUTURE-AI) which included external validation are provided in Table 4. These studies
covered diverse disease types (soft-tissue tumours: n=9, bone tumours: n=8, GIST: n=3),
imaging modalities (MRI: n=11, CT: n=4, X-ray: n=4, ultrasound: n=1), outcomes (diagnosis:
n = 12, prognosis: n= 7 and both diagnosis and prognosis: n =1), and AI methodologies
(machine learning model using a combination of hand-crafted and model-learned imaging
features: n=3; machine learning using model-learned features: n=6; machine learning using
hand-crafted imaging features: n=11). Overall, AI methods demonstrated strong performance
for their respective tasks, however there is a wide range in performance between models (AUC
range: 0∙64–0∙95). However, most studies relied on a single centre for external validation
(n=12), and only a few included prospective validation (n=2). These studies had a mean score
of 40∙4 out of 53 (SD: 3∙0, AR mean±SD: 76%±5∙8%) for CLAIM and 8∙4 out of 30 (SD: 1∙6,
AR mean±SD: 28%±5∙4%) for FUTURE-AI. Finally, among these top 20 studies, we explored
potential associations between performance metrics, individual guideline scores, and three main
study categories, as summarized in Supplementary Table S1. This showed no obvious
differences in scores and performance metrics between any of the groups.

<!-- Page 13 -->


### Discussion

This work has systematically identified and summarised radiological imaging-AI research on
STBT and conducted comprehensive evaluation of published literature against two bestpractice guidelines: CLAIM and FUTURE-AI. These guidelines were developed to ensure that
AI tools target unmet clinical needs, are transferrable, generalisable, and can be used in realworld clinical practice. Analysis revealed a rapid increase in experimental AI tools for imagingbased STBT evaluation over the past five years. Studies performed moderately against CLAIM
(28·9±7·5 out of 53) and poorly against FUTURE-AI evaluations (5·1±2·1 out of 30). The poor
results in FUTURE-AI are expected as these guidelines are recent and set high requirements.
Several papers do show higher scores in both CLAIM and FUTURE-AI (Table 4) and show
promising results in external validation cohorts (AUC range: 0∙784-0∙948). However, the
highest scoring paper achieved only a 11∙5 out of 30 in FUTURE-AI, highlighting room for
improvement. These results suggest that while progress has been made in developing AI tools
for STBT, most studies are still at the proof-of-concept stage and there remains substantial room
for improvement to guide future clinical translation. Panel 2 summarises the authors’
recommendations, focusing on five keys topics: design, development, evaluation,
reproducibility, and data availability.
In the design stage, several critical aspects warrant more attention. Intended clinical settings
(Universality-1) and prior hypotheses (CLAIM-4b) should be reported. On a positive note,
over 85% of studies involved interdisciplinary teams (Usability-1, General-1), which is
recommended for effective AI tool development.9 However, most studies did not
comprehensively identify possible sources of bias at an early stage (Fairness-1, Robustness-1),
which could limit the applicability of these AI tools. To overcome this, interdisciplinary
stakeholders should work together from the design stage to identify the clinical role of the AI
tool, ensure it integrates into the clinical workflow, and any possible sources of bias.
In the development stage, studies generally reported dataset source and conducted research with
appropriate ethical approvals (CLAIM-7). However, almost half of studies did not assess biases
during AI development (Fairness-3) and very few studies trained with representative real-world
data (Robustness-2), which can hinder the transferability of AI tools, especially given the highly
heterogeneous imaging characteristics of STBT. Another notable gap is a lack of focus on
explainability and traceability. Few studies addressed items under FUTURE-AI Explainability
(1-2) and Traceability (1-3), similar shortcoming was observed in the CLAIM checklist
(CLAIM-31). While accuracy is crucial in medical practice, it is often argued that AI methods
should go beyond pure performance metrics by addressing other factors such as prediction
uncertainties, explaining their outputs, and providing clinicians with detailed information.17 For
AI tools to be effective in clinical decision-making, explainability is vital to ensure clinicians

<!-- Page 14 -->

understand and can trust the AI’s reasoning.18 Additionally, to assist with AI development,
research should build on previous work where possible. To assist with this, researchers should
continue to adhere to community-defined standards, which is currently done in over half of the
reviewed papers, and ensure their code is available. This review shows that almost all included
studies developed new models rather than adapting or enhancing existing ones, even when
promising results were achieved. Finally, it is integral that AI tools are easy for the end-user to
use in the clinical workflow, however only two studies developed a graphical user interface for
user experience testing (Usability-3).19,20
Regarding evaluation, while over 85% of studies adopted relevant metrics and reported AI
algorithm performance (CLAIM-28 and 37), only 22% conducted external validation (CLAIM-
33), and most used single-institute datasets (Universality-3). Furthermore, several studies
lacked thorough internal validation (Robustness-3, General-4). AI tools should be tested against
independent external data, ideally from multiple sources, to assess the tool’s universality and
prevent site-specific bias. Accuracy metrics should also be compared against current bestpractice (i.e. compared to radiologists) to ensure AI tools offer improvements in outcomes. Less
than 20% of studies reported failure analysis or incorrectly classified cases (CLAIM-39).
Including failure analysis is crucial to identify potential pitfalls, helping users understand when
it is appropriate to use the tool. Developers should also ensure that the tool is robust against the
biases identified during the design stage.
Regarding reproducibility, most studies fail to provide adequate materials (code, model, and
data) to reproduce published results. Only around 10% of studies offered a full study protocol,
including comprehensive methodology or code. Making protocols and code available enables
others to reproduce the study across multiple steps, such as data preprocessing, ground truth
acquisition, model construction, and training procedure. The lack of accessible and
reproducible AI research in STBT could impede the adoption of these tools, as sarcoma centres
may struggle to reproduce the tools performance locally. Adhering to guidelines such as
CLAIM could enhance the quality and accessibility of these protocols.
Regarding data availability, there is a lack of freely accessible annotated imaging datasets of
STBT, as highlighted in Table 1. Although 25% of published research stated that data used was
available by request, a recent study by Gabelica et al. (2022) investigating compliance with
data sharing statements showed a response rate of 14%, with only 6∙8% supplying the data.21
One challenge in creating these datasets is the time required and the need for an easy-to-use
format. Structured and standardised reporting in clinical practice could help reduce the effort
needed for retrospective data collection. However, AI developers often struggle to collate data
themselves, especially since STBT are rare and only treated at tertiary sarcoma centres. This

<!-- Page 15 -->

underscores the importance of collaborating with clinical professionals. Increasing data
availability would accelerate AI tool development and allow for external validation of models.
Potential solutions include hosting “grand challenges” where clinicians provide data for AI
developers to tackle a real-world clinical problem, or employing federated learning, which has
proven effective for training AI models on rare tumours across international networks.22-24
Several reviews described the use of AI or radiomics in STBT management.25-28 This study
expands and complements these previous reviews, including a substantially larger volume of
included publications (325 vs. 21-52 reports) primarily due to our extended scope and search
strategy, including benign soft-tissue tumours, bone tumours, and a broad range of AI methods
(i.e. not limiting to radiomics with hand-crafted features). Furthermore, most previous reviews
only examined the accuracy and performance of published AI tools in the field; the current
systematic review instead examined the methodological quality of published literature by
assessing this against best-practice guidelines. The only other systematic reviews that, to the
authors knowledge, have assessed quality of AI research in radiology imaging for STBT are
Crombé et al. (2020) (52 studies) and De Angelis et al. (2024) (49 studies), both scoring against
the Radiomics Quality Score (RQS).25,26 In this study, different scoring systems were
deliberately chosen as CLAIM and FUTURE-AI are independent but complementary
guidelines, providing a broader assessment of overall quality than using only one.10 FUTURE-
AI allows assessment of trustworthiness, deployability, and translation to clinical practice,
while CLAIM guidelines, which are endorsed by the RSNA, ensures that studies are reported
according to a standard set of information especially designed for medical imaging AI. Findings
indicate that the field continues to produce promising proof-of-concept results but is not ready
to make the jump to clinical application. This agrees with earlier work in the field.
To better understand the relationship between adherence to reporting guidelines and model
performance, we examined the top 20 studies with the highest combined CLAIM and
FUTURE-AI scores. Our analyses suggest that no particular subfield demonstrates consistently
superior performance, with reported metrics varying widely—even among similar models. This
underscores the need for further external validation and standardization. Whilst some studies
show promising results, the overall heterogeneity highlights the complexity of AI performance
assessment.
Subgroup analysis in which CLAIM and FUTURE-AI scores were investigated by tumour type,
method type and outcome, showed no obvious differences between groups although papers
performing statistics on hand crafted features scored worse than studies which used some form
of machine learning. This is not surprising as the guidelines we chose focus on the use of AI.
There was a general trend for a small increase in scores for both guidelines over time. This

<!-- Page 16 -->

implies that whilst the quality of AI-based research is improving over time no field assessed in
this review is ahead than any other.
There are limitations to this study. First, due to the large volume of literature, most papers were
scored by a single reviewer. However, a sub-group of papers were scored by three reviewers
followed by consensus analysis, showing excellent agreement, and reviewers remained in
discussion if they had doubts about how best to score a paper for a particular category. Two or
more reviewers per paper might have provided more robust results but would have required a
significant time investment for likely only marginal gains. Secondly, in the reproducibility
study with subgroups, papers were selected by alphabetical order based on the first author’s
name. While this approach introduces a degree of randomness, a fully randomised selection
process would have been more robust to minimise potential biases. Third, there are other
scoring guidelines such as APPRAISE AI, TRIPOD-AI, or RQS.51-53 Future studies could
benefit from integrating other frameworks, other than CLAIM and FUTURE-AI, to provide a
more comprehensive evaluation of both reporting adherence and study quality
In conclusion, this review discusses the growing volume of published work evaluating imagingrelated AI tools to aid in diagnosis, prognosis, and management of soft tissue and bone tumours.
The top performing papers, as determined by both guidelines, may represent encouraging steps
toward bringing AI in radiology closer to clinical translation, however even these have some
limitations. The identified limitations of the reviewed studies with respect to CLAIM and
FUTURE-AI guidelines will need to be addressed before such tools can translate into the
clinical domain. Several opportunities have been identified and the authors’ recommendations
to promote translation of AI methods into clinical practice are summarised in Panel 2.
Addressing these points may help drive clinical adoption of AI tools into the radiology
workflow in a responsible and effective way.

<!-- Page 17 -->


### Contributors

D.J.S., M.M., X.W.: conceptualisation, data curation, formal analysis, investigation,
methodology, project administration, visualisation, writing – original draft, and writing –
review & editing; S.K., M.P.A.S: conceptualisation, investigation, methodology, supervision,
writing – review & editing; A.F.S., P.R., E.H.G.O., J.J.V., R.H., K.L., D.F.H., G.J.L.H.L., C.V.,
D.J.G., W.J.N.: methodology, supervision, writing – review & editing; S.K., M.P.A.S., M.M.,
E.H.G.O., J.J.V., C.V., D.J.G., W.J.N.: funding acquisition. All authors read and approved the
final version of the manuscript. D.J.S, M.M., X.W., S.K., M.P.A.S. have accessed and verified
the data. D.J.S, M.M., X.W. have contributed equally. S.K. and M.P.A.S. have contributed
equally.

### Data Sharing Statement

Empty checklists for this review are included in the supplementary material. All data collected
and analysed in this study are available online.16 A website (https://douwespaanderman.github.io/AI-STTandBoneTumour-Review/) with interactive figures and tables
with scores for each paper is also available online.

### Declaration of Interests

WJN is the founder of Quantib and was scientific lead until 31-1-2023. JJV received a grant to
institution from Qure.ai / Enlitic; consulting fees from Tegus; payment to institution for lectures
from Roche; travel grant from Qure.ai; participation on a data safety monitoring board or
advisory board from Contextflow, Noaber Foundation, and NLC Ventures; leadership or
fiduciary role on the steering committee of the PINPOINT Project (payment to institution from
AstraZeneca) and RSNA Common Data Elements Steering Committee (unpaid); phantom
shares in Contextflow and Quibim; chair scientific committee EuSoMII (unpaid); chair ESR
value-based radiology subcommittee (unpaid); member editorial board European Journal of
Radiology (unpaid). SK and EHGO are scientific directors of the ICAI lab “Trustworthy AI for
MRI”, a public-private research program partially funded by General Electric Healthcare. The
other authors do not have any conflicts of interest.

### Acknowledgments

This research was supported by an unrestricted grant of Stichting Hanarth Fonds, The
Netherlands. MPAS and SK acknowledge funding from the research project EuCanImage
(European Union's Horizon 2020 research and innovation programme under grant agreement
Nr. 95210). MPAS also acknowledges funding from a NGF AiNed Fellowship
(NGF.1607.22.025). MM, Doctoral Clinical and Practitioner Academic Fellow, NIHR302901,
is funded by Health Education England (HEE) / National Institute for Health and Research
(NIHR) for this research project. This research was conducted within the “Trustworthy AI for

<!-- Page 18 -->

MRI” ICAI lab within the project ROBUST, funded by the Dutch Research Council (NWO),
GE Healthcare, and the Dutch Ministry of Economic Affairs and Climate Policy (EZK). AS
receives salary support from ICNIHR Leeds Biomedical Research Centre (NIHR203331). The
funders had no role in study design, data collection and analysis, decision to publish, or
preparation of the manuscript. The views expressed in this publication are those of the author
and not necessarily those of the NIHR, NHS or the UK Department of Health and Social Care.

<!-- Page 19 -->

Panel 2: Recommendations to promote clinical translation of AI methods for soft-tissue
and bone tumours.

### Design

• Interdisciplinary stakeholders should define; (A) the unmet clinical need, (B) the
intended use of AI, (C) intended clinical setting in which AI should operate, (D) the
end-user requirements, (E) how AI would operate in clinical workflow.
• Possible types and sources of bias (e.g. sex, age, ethnicity, socioeconomics, geography)
should be identified at the early design stage.

### Development

• Data used for AI development should reflect real-world data used in the intended
clinical setting or preferably retrieved from the clinical setting. Additionally, sources
of variation and potential biases should be investigated early in the development
process.
• Explainability of AI methods should be developed and implemented in a way that it is
possible to understand why an AI tool has arrived at its predictions.
• AI development should build on previous work by: (A) adhering to community-defined
standards, and (B) considering previous existing methods by validating or improving
them whenever possible.
• Ensure that AI tools are easy for the end-user to use in a clinical setting.

### Evaluation

• AI tools should be evaluated using independent external test data. Limits on
universality of the external test sets should be discussed.
• AI tools should be evaluated against current best practices, e.g. classification by
radiologist or histology results from biopsy, and evaluated with intended end-users.
• Failure analysis of incorrect classified cases should be conducted.
• The robustness and sensitivity to variations and biases in data, identified prior to AI
development, should be thoroughly investigated.

### Reproducibility

• Code should be made publicly available, readable, usable and traceable to increase
confidence in the method.
• The Methods section should comprehensively cover all aspects of AI development,
including; (A) data preprocessing, (B) ground truth acquisition, (C) a detailed
description of the AI methodology, and (D) the training procedures. To this end, the
Checklist for Artificial Intelligence in Medical Imaging (CLAIM) could be followed.

### Data availability

• Structured and standardised reporting should be introduced in clinical practice to limit
the manual work required in retrospective data collection.
• Tertiary sarcoma centres should collect labelled data and make this publicly available,
preferably in the context of a “grand challenge”, while protecting patient details and
respecting privacy.
• To protect patient privacy and avoid excessive data-sharing, researchers could work
together using a federated learning approach.

<!-- Page 20 -->


### Tables

Table 1: Open-access datasets available with imaging for soft-tissue and bone tumours.
Data Vallières el al. (2015) [29] Starmans et al. (2021) [preprint - 30]

### Origin


### Canada the Netherlands


### Various soft-tissue sarcoma

Disease type Various soft-tissue tumours
(Extremities)
Imaging modality MR and PET-CT MR or CT
Number of patients 51 564

### Tumour segmentation and


### Tumour segmentation and clinical

Additional data clinical outcome (lung
outcome (phenotype)
metastasis)

<!-- Page 21 -->

Table 2: Summary scores of the included studies for each (sub)section of the Checklist for
Artificial Intelligence in Medical Imaging (CLAIM).

### Maximum Adherence rate

(Sub)section Score (Mean ± SD) Max score Min score
achievable (Mean ± SD)
score
Title / Abstract 2∙0 2∙0 ± 0∙2 2∙0 0∙0 98% ± 12%
Introduction 3∙0 2∙1 ± 0∙4 3∙0 0∙0 70% ± 14%

### Methods 38∙0 19∙8 ± 5∙8 34∙0 0∙0 52% ± 15%

Study design 2∙0 1∙8 ± 0∙5 2∙0 0∙0 89% ± 24%

### Data 15∙0 8∙0 ± 2∙8 14∙0 0∙0 54% ± 18%


### Ground truth 5∙0 2∙9 ± 1∙4 5∙0 0∙0 57% ± 29%

Data partitions 2∙0 1∙7 ± 0∙6 2∙0 0∙0 87% ± 30%
Testing data 1∙0 0∙0 ± 0∙2 1∙0 0∙0 4% ± 20%

### Model 3∙0 1∙5 ± 1∙0 3∙0 0∙0 51% ± 33%


### Training 3∙0 1∙2 ± 0∙9 3∙0 0∙0 40% ± 31%

Evaluation 7∙0 2∙7 ± 1∙3 6∙0 0∙0 38% ± 18%
Results 5∙0 2∙6 ± 1∙2 5∙0 0∙0 52% ± 24%
Data 2∙0 1∙0 ± 0∙8 2∙0 0∙0 50% ± 39%

### Model

3∙0 1∙6 ± 0∙8 3∙0 0∙0 53% ± 25%
performance
Discussion 2∙0 1∙3 ± 0∙6 2∙0 0∙0 66% ± 32%

### Other

3∙0 1∙2 ± 0∙9 3∙0 0∙0 39% ± 31%
information
Overall 53∙0 28∙9 ± 7∙5 48∙0 4∙0 55% ± 14%

<!-- Page 22 -->

Table 3: Summary scores of the included studies for each principle from the FUTURE-AI
international consensus guideline for trustworthy and deployable AI.
Maximum Score (Mean ± Max Min Adherence rate

### Principle

achievable score SD Score Score (Mean ± SD)

### Fairness 3∙0 1∙1 ± 0∙7 2∙5 0∙0 37% ± 22%

Universality 4∙0 0∙8 ± 0∙7 3∙0 0∙0 20% ± 17%
Traceability 6∙0 0∙1 ± 0∙2 1∙0 0∙0 1% ± 3%

### Usability 5∙0 0∙5 ± 0∙3 3∙0 0∙0 10% ± 7%


### Robustness 3∙0 0∙4 ± 0∙4 2∙5 0∙0 14% ± 12%

Explainability 2∙0 0∙1 ± 0∙2 1∙5 0∙0 4% ± 12%

### General 7∙0 2∙2 ± 0∙8 3∙5 0∙0 32% ± 11%

Overall 30∙0 5∙1 ± 2∙1 11∙5 0∙0 17% ± 7%

<!-- Page 23 -->

Table 4: Performance measurements of the top 20 performing papers, as determined by their
combined CLAIM and FUTURE-AI scores, among those that performed external validation.
AUC = area under the curve, CI = confidence interval, NPV = negative predictive value.
*AI development centre was also included as one of the eight external validation centres.
† Values are mean ± standard deviation
Author Short description Validation Performance (Proportion, 95%

## Ci)

Ye et A multi-task machine learning model External validation AUC: 0∙900 (0∙773–1∙000)
al. [31] using learned imaging features (deep 53 patients from 1 Accuracy: 0∙783 (0∙581–0∙903)
learning) for the segmentation, centre Sensitivity: 0∙756 (0∙552–0∙886)
detection, and differentiation of Specificity: 0∙886 (0∙764–0∙950)
malignant and benign primary bone
tumours, as well as bone infections,
leveraging multi-modal inputs
including T1-weighted MRI, T2-
weighted MRI, and clinical data.
Dong et Machine learning model using learned External validation External validation
al. [32] imaging features (deep learning) 241 patients from 1 AUC: 0∙948 (0∙921–0∙969)
differentiating gastrointestinal stromal centre Accuracy: 0∙917 (0∙875–0∙946)
tumours (GISTs) and leiomyomas on Sensitivity: 0∙903 (0∙834–0∙945)
endoscopic ultrasonography. Prospective Specificity: 0∙930 (0∙872–0∙963)
validation 59 Precision: 0∙919 (0∙853–0∙957)
patients from 1 NPV: 0∙915 (0∙855–0∙952)
centre
Prospective validation (for GISTs
and leiomyomas, respectively)
AUC: 0∙865 (0∙782–0∙977) and
0∙864 (0∙762–0∙966)

### Accuracy: 0∙865 and 0∙864

Sensitivity: 0∙897 and 0∙857
Specificity: 0∙833 and 0∙871
Precision: 0∙839 and 0∙857

### NPV: 0∙893 and 0∙881

Xie et Machine learning model using learned External validation AUC: 0∙873 (0∙812–0∙920)
al. [33] imaging features (deep learning) to 89 patients from 1 Accuracy: 0∙687 (0∙614–0∙783)
classify histological types of primary centre Sensitivity: 0∙572 (0∙457–0∙685)
bone tumours on radiographs. Specificity: 0∙916 (0∙893–0∙938)
Xu et Machine learning model using a External validation AUC: 0∙861 (0∙737–0∙985)
al. [34] combination of hand-crafted and 63 patients from 2 Accuracy: 0∙810
model-learned imaging features to centre
differentiate between retroperitoneal
lipomas and well-differentiated
liposarcomas based on MDM2 status
on contrast-enhanced CT.
Arthur Machine learning model using hand- External validation Histology and Grade
et al. crafted imaging features classifying 89 patients from 8 AUC: 0∙928 and 0·882
[35] histological type and tumour grade in centres* Accuracy: 0·843 and 0·823
retroperitoneal sarcoma on CT. Sensitivity: 0·923 and 0·800
Specificity: 0·829 and 0·848
Precision: 0·480 and 0·865

## Npv: 0·984, 0·778

Guo et Machine learning model using a External validation External validation (Centre 1 and
al. [36] combination of hand-crafted and 125 and 44 patients Centre 2)
model-learned imaging features to from 2 centres AUC: 0∙860 (0∙787–0∙916) and
classify histological grade and predict 0∙838 (0∙696–0∙932)
prognosis of soft-tissue tumours on Prospective Accuracy: 0∙840 and 0∙750
MRI. validation 12 Sensitivity: 0∙835 and 0∙840
patients from 1 Specificity: 0∙794 and 0∙737
centre Hazard ratio: 4∙624 (1∙924–11∙110)
and 2∙920 (0∙603–14∙150)

### Prospective validation


## Auc: 0∙819 (0∙501–0∙974)


### Accuracy: 0∙667

Sensitivity: 0∙667
Specificity: 1∙000

<!-- Page 24 -->

Gitto et Machine learning model using hand- External validation AUC: 0∙94 for atypical cartilaginous
al. [37] crafted imaging features 65 patients from 1 tumour and 0∙90 for grade II
differentiating atypical cartilaginous centre chondrosarcomal
tumour and grade II chondrosarcoma Accuracy: 0∙92
of long bones on MRI. Sensitivity: 0∙92

### Precision: 0∙92

Von Machine learning model using hand- External validation AUC: 0∙90
Schaky crafted imaging features to distinguish 96 patients from 1 Accuracy: 0∙75 (0∙65–0∙83)
et al. between benign and malignant bone centre Sensitivity: 0∙90 (0∙74–0∙98)
[38] lesions on radiography. Specificity: 0∙68 (0∙55–0∙79)
Precision: 0∙57 (0∙42–0∙71)

## Npv: 0∙94 (0∙82–0∙99)

Gitto et Machine learning model using hand- External validation AUC: 0∙90
al. [39] crafted imaging features 30 patients from 1 Accuracy: 0∙80
differentiating atypical cartilaginous centre Sensitivity: 0∙89
tumour and high-grade Specificity: 0∙67
chondrosarcoma of long bones on
radiography.
Cao et Machine learning model using hand- External validation AUC: 0∙865 (0∙732–0∙998) for 3-
al. [40] crafted imaging features predicting the 42 patients from 1 year and 0∙931 (0∙849–1∙00) for 5
local recurrence after surgical centre year
treatment of primary C-index: 0∙866 (0∙786–0∙946)
dermatofibrosarcoma protuberans,
based on MRI.
Yang et Machine learning model using hand- External validation AUC: 0∙766 for 1-year, 0∙776 for 3-
al. [41] crafted imaging features predicting 45 patients from 1 year, and 0∙893 for 5-year
progression-free survival after centre C-index: 0∙718 (0∙618–0∙818)
imatinib therapy in patients with liver
metastatic gastrointestinal stromal
tumours on multi-sequence MRI.
Chen et Machine learning model using hand- External validation AUC: 0∙842 (0∙793–0∙883)
al. [42] crafted imaging features predicting 34 patients from 3 Accuracy: 0∙765 ± 0∙020†
pathologic response to neoadjuvant centres Sensitivity: 0∙739 ± 0∙032†
chemotherapy (NAC) in patients with Specificity: 0∙909 ± 0∙026†
osteosarcoma on MRI.
Liang Machine learning model using a External validation AUC: 0∙833 (0∙732–0∙933)
et al. combination of hand-crafted and 126 patients from 2 Accuracy: 0∙897
[43] model-learned imaging features for centre Sensitivity: 0∙474
predicting lung metastases in patients Specificity: 0∙972
with soft-tissue sarcoma on MRI. Precision: 0∙750

## Npv: 0∙912

Kang et Machine learning model using learned External validation Low-malignant, intermediateal. [44] imaging features (deep learning) to 388 patients from 1 malignant, and high-malignant
predict preoperative risk of centre AUC: 0∙87 (0∙83–0∙91), 0∙64 (0∙60–
gastrointestinal stromal tumours on 0∙68), and 0∙85 (0∙81–0∙89)
CT. Accuracy: 0∙81 (0∙77–0∙85), 0∙75
(0∙71–0∙79), and 0∙77 (0∙73–0∙81)
Sensitivity: 0∙72 (0∙64–0∙79), 0∙24
(0∙14–0∙34), and 0∙79 (0∙73–0∙85)
Specificity: 0∙86 (0∙83–0∙90), 0∙86
(0∙82–0∙90), and 0∙75 (0∙70–0∙81)
He et Machine learning model using learned External validation AUC: 0∙877 (0∙833–0∙918) benign
al. [45] imaging features (deep learning) for 291 patients from 2 vs not benign and 0∙916 (0∙877–
classification of benign, intermediate centre 0∙949) malignant vs not malignant
or malignant primary bone tumours on Accuracy: 0∙734
radiography.
Peeken Machine learning model using hand- External validation AUC: 0∙75 (0∙56–0∙93)
et al. crafted imaging features from 53 patients from 1 Accuracy: 0∙86
[46] different timepoints (delta radiomics) centre Balanced accuracy: 0∙57
predicting pathologic complete Sensitivity: 0∙20
response to neoadjuvant therapy in Specificity: 0∙95
high grade soft tissue sarcoma of Precision: 0∙33
trunk and extremity, based on MRI. NPV: 0∙90
Forema Machine learning model using hand- External validation AUC: 0∙88 (0∙85–0∙91)
n et al. crafted imaging features predicting the 50 patients from 1 Accuracy: 0∙76
[47] MDM2 gene amplification status in centre Sensitivity: 0∙70
order to differentiate between atypical Specificity: 0∙81
lipomatous tumours (ALT) and
lipomas on MRI.

<!-- Page 25 -->

Spraker Machine learning model using hand- External validation Sensitivity: 0∙79
et al. crafted imaging features predicting 61 patients from 1 Specificity: 0∙68
[48] overall survival of grade II and III centre C-index: 0∙78
soft-tissue tumours on MRI. Hazard ratio: 2∙4
Fradet Machine learning model using a External validation AUC: 0∙80
et al. combination of hand-crafted and 60 patients from 35 Specificity: 0∙63
[49] model-learned imaging features centres
predicting malignancy for lipomatous
soft-tissue lesions on MRI.
Gitto et Machine learning model using hand- External validation AUC: 0∙784
al. [50] crafted imaging features 36 patients from 1 Accuracy: 0∙75
differentiating atypical cartilaginous centre
tumours and high-grade
chondrosarcomas of long bones on

## Ct.


<!-- Page 26 -->


### References


## Cormier JN, Pollock RE. Soft Tissue Sarcomas. CA: A Cancer Journal for Clinicians

2004; 54: 94–109.

## Kruiswijk AA, Dorleijn DMJ, Marang-an de Mheen PJ, van de Sande MAJ, van

Bodegom-Vos L. Health-Related Quality of Life of Bone and Soft-Tissue Tumor
Patients around the Time of Diagnosis. Cancers 2023; 15: 2804.

## Zhang Z, Sejdić E. Radiological images and machine learning: trends, perspectives,

and prospects. Computers in biology and medicine 2019; 108: 354–70.

## Hanna TN, Lamoureux C, Krupinski EA, Weber S, Johnson J-O. Effect of Shift,

Schedule, and Volume on Interpretive Accuracy: A Retrospective Analysis of 2.9
Million Radiologic Examinations. Radiology 2018; 287: 205–12.

## Bechtold RE, Chen MYM, Ott DJ, Zagoria RJ, Scharling ES, Wolfman NT, et al.

Interpretation of Abdominal CT: Analysis of Errors and Their Causes. Journal of
Computer Assisted Tomography 1997; 21: 681.

## McNabb NK, Christensen EW, Rula EY, Coombs L, Drey K, Wald C, et al. Projected

Growth in FDA-Approved Artificial Intelligence Products Given Venture Capital
Funding. Journal of the American College of Radiology: JACR 2024; 21: 617–23.

## Artificial Intelligence and Machine Learning (AI/ML)-Enabled Medical Devices.

FDA. 2024; published online Aug. https://www.fda.gov/medical-devices/softwaremedical-device-samd/artificial-intelligence-and-machine-learning-aiml-enabledmedical-devices (accessed Aug 2024).

## Tejani AS, Klontzas ME, Gatti AA, Mongan JT, Moy L, Park SH, et al. Checklist for

Artificial Intelligence in Medical Imaging (CLAIM): 2024 Update. Radiology:
Artificial Intelligence 2024; 6: e240300.

## Lekadir K, Frangi AF, Porras AR, et al. FUTURE-AI: international consensus

guideline for trustworthy and deployable artificial intelligence in healthcare. BMJ
2025; 388: e081554.

## Klontzas ME, Gatti AA, Tejani AS, Kahn CE. AI Reporting Guidelines: How to

Select the Best One for Your Research. Radiology: Artificial Intelligence 2023; 5:
e230055.

## Page MJ, McKenzie JE, Bossuyt PM, Boutron I, Hoffmann TC, Mulrow CD, et al.

The PRISMA 2020 statement: an updated guideline for reporting systematic reviews.
BMJ 2021; 372: n71.

## Spaanderman D, Marzetti M, Wan X, Scarsbrook A, Oei E, Visser J, et al. AI in

radiological imaging of soft-tissue and bone tumors: a systematic review and
evaluation against best-practice guidelines. PROSPERO International prospective

<!-- Page 27 -->

register of systematic reviews. 2023; published online Oct 6.
https://www.crd.york.ac.uk/prospero/display_record.php?RecordID=467970
(accessed Aug 2024).

## Si L, Zhong J, Huo J, Xuan K, Zhuang Z, Hu Y, et al. Deep learning in knee imaging:

a systematic review utilizing a Checklist for Artificial Intelligence in Medical
Imaging (CLAIM). European Radiology 2021; 32: 1353–61.

## Mongan J, Moy L, Kahn CE. Checklist for Artificial Intelligence in Medical Imaging

(CLAIM): A Guide for Authors and Reviewers. Radiology: Artificial Intelligence
2020; 2: e200029.

## Fleiss JL, Levin B, Paik MC. The Measurement of Interrater Agreement. In:

Statistical Methods for Rates and Proportions, 1st edn. Wiley, 2003: 598–626.

## Spaanderman D, Marzetti M, Wan X, Starmans M, Klein S. AI in radiological

imaging of soft-tissue and bone tumours: a systematic review evaluating against bestpractice guidelines. Github. 2024; published online Aug 21. https://douwespaanderman.github.io/AI-STTandBoneTumour-Review (accessed Aug 21, 2024).

## Abrantes J, Rouzrokh P. Explaining explainability: The role of XAI in medical

imaging. European Journal of Radiology 2024; 173.
DOI:https://doi.org/10.1016/j.ejrad.2024.111389.

## Amann J, Blasimme A, Vayena E, Frey D, Madai VI. Explainability for artificial

intelligence in healthcare: a multidisciplinary perspective. BMC Medical Informatics
and Decision Making 2020; 20: 310.

## Yang X, Wang H, Dong Q, Xu Y, Liu H, Ma X, et al. An artificial intelligence

system for distinguishing between gastrointestinal stromal tumors and leiomyomas
using endoscopic ultrasonography. Endoscopy 2022; 54: 251–61.

## Dong Z, Zhao X, Zheng H, Zheng H, Chen D, Cao J, et al. Efficacy of real-time

artificial intelligence-aid endoscopic ultrasonography diagnostic system in
discriminating gastrointestinal stromal tumors and leiomyomas: a multicenter
diagnostic study. eClinicalMedicine 2024; 73.
DOI:https://doi.org/10.1016/j.eclinm.2024.102656.

## Gabelica M, Bojčić R, Puljak L. Many researchers were not compliant with their

published data sharing statement: a mixed-methods study. Journal of Clinical
Epidemiology 2022; 150: 33–41.

## Dieuwertje Luitse, Blanke T, Poell T. AI competitions as infrastructures of power in

medical imaging. Information Communication & Society 2024; 1–22.

## Grand Challenge. grand-challenge.org. https://grand-challenge.org/.


## Pati S, Baid U, Edwards B, Sheller M, Wang S, Reina GA, et al. Federated learning

enables big data for rare cancer boundary detection. Nature Communications 2022;
13: 7346.

<!-- Page 28 -->


## Crombé A, Fadli D, Italiano A, Saut O, Buy X, Kind M. Systematic review of

sarcomas radiomics studies: Bridging the gap between concepts and clinical
applications? European Journal of Radiology 2020; 132: 109283–3.

## De Angelis R, Casale R, Coquelet N, Ikhlef S, Mokhtari A, Simoni P, et al. The

impact of radiomics in the management of soft tissue sarcoma. Discover Oncology
2024; 15. DOI:https://doi.org/10.1007/s12672-024-00908-2.

## Crombé A, Spinnato P, Italiano A, Brisse HJ, Feydy A, Fadli D, et al. Radiomics and

artificial intelligence for soft-tissue sarcomas: Current status and perspectives.
Diagnostic and Interventional Imaging 2023; 104: 567–83.

## Zhu N, Meng X, Wang Z, Hu Y, Zhao T, Fan H, et al. Radiomics in Diagnosis,

Grading, and Treatment Response Assessment of Soft Tissue Sarcomas: A
Systematic Review and Meta-analysis. Academic Radiology 2024; 0.
DOI:https://doi.org/10.1016/j.acra.2024.03.029.

## Vallières M, Freeman CR, Skamene R, Naqa IEI. A radiomics model from joint

FDG-PET and MRI texture features for the prediction of lung metastases in softtissue sarcomas of the extremities. Physics in Medicine & Biology 2015; 60: 5471.
30. [preprint] Starmans, MPA, Milea T, Vos M, Padmos GA, Grünhagen DJ, Verhoef C,
et al. The WORC database: MRI and CT scans, segmentations, and clinical labels for
930 patients from six radiomics studies. medRxiv 2021; published online Aug.
DOI:https://doi.org/10.1101/2021.08.19.21262238.

## Ye Q, Yang H, Lin B, Wang M, Song L, Xie Z, et al. Automatic detection,

segmentation, and classification of primary bone tumors and bone infections using an
ensemble multi-task deep learning framework on multi-parametric MRIs: a multicenter study. European Radiology 2023; 34: 4287–99.

## Dong Z, Zhao X, Zheng H, Zheng H, Chen D, Cao J et al. Efficacy of real-time

artificial intelligence-aid endoscopic ultrasonography diagnostic system in
discriminating gastrointestinal stromal tumors and leiomyomas: a multicenter
diagnostic study. EClinicalMedicine 2024; 73: 102656–6.

## Xie H, Hu J, Zhang X, Ma S, Liu Y, Wang X. Preliminary utilization of radiomics in

differentiating uterine sarcoma from atypical leiomyoma: Comparison on diagnostic
efficacy of MRI features and radiomic features. European Journal of Radiology
2019; 115: 39–45.

## Xu J, Miao L, Wang CX, Wang HH, Wang QZ, Li M, et al. Preoperative

Contrast-Enhanced CT-Based Deep Learning Radiomics Model for
Distinguishing Retroperitoneal Lipomas and Well‑Differentiated
Liposarcomas. Academic Radiology 2024; 31.
DOI:https://doi.org/10.1016/j.acra.2024.06.035.

<!-- Page 29 -->


## Arthur A, Orton MR, Emsley R, Vit S, Kelly-Morland C, Strauss D, et al. A CT-

based radiomics classification model for the prediction of histological type and
tumour grade in retroperitoneal sarcoma (RADSARC-R): a retrospective multicohort
analysis. The Lancet Oncology 2023; 24: 1277–86.

## Guo J, Li Y, Guo H, Hao DP, Xu JX, Huang CC, et al. Parallel CNN‐Deep Learning

Clinical‐Imaging Signature for Assessing Pathologic Grade and Prognosis of Soft
Tissue Sarcoma Patients. Journal of Magnetic Resonance Imaging 2024; published
online June 10. DOI:https://doi.org/10.1002/jmri.29474.

## Gitto S, Cuocolo R, van Langevelde K, van de Sande MAJ, Parafioriti A, Luzzati A,

et al. MRI radiomics-based machine learning classification of atypical cartilaginous
tumour and grade II chondrosarcoma of long bones. EBioMedicine 2022; 75:
103757–7.
38. von Schacky CE, Wilhelm NJ, Schäfer VS, Leonhardt Y, Jung M, Jungmann PM, et
al. Development and evaluation of machine learning models based on X-ray
radiomics for the classification and differentiation of malignant and benign bone
tumors. European Radiology 2022; 32: 6247–57.

## Gitto S, Alessio Annovazzi, Nulle K, Interlenghi M, Salvatore C, Anelli V, et al. X-

rays radiomics-based machine learning classification of atypical cartilaginous tumour
and high-grade chondrosarcoma of long bones. EBioMedicine 2024; 101: 105018–8.

## Cao C, Yi Z, Xie M, Xie Y, Tang X, Tu B, et al. Machine learning-based radiomics

analysis for predicting local recurrence of primary dermatofibrosarcoma protuberans
after surgical treatment. Radiotherapy and Oncology 2023; 186: 109737–7.

## Yang L, Zhang D, Zheng T, Liu D, Fang Y. Predicting the progression-free survival

of gastrointestinal stromal tumors after imatinib therapy through multi-sequence
magnetic resonance imaging. Abdominal Radiology 2023; 49: 801–13.

## Chen H, Zhang X, Wang X, Quan X, Deng Y, Lu M, et al. MRI-based radiomics

signature for pretreatment prediction of pathological response to neoadjuvant
chemotherapy in osteosarcoma: a multicenter study. European Radiology 2021; 31:
7913–24.

## Liang H, Yang S, Zou H, Hou F, Duan LS, Huang CC, et al. Deep Learning

Radiomics Nomogram to Predict Lung Metastasis in Soft-Tissue Sarcoma: A Multi-
Center Study. Frontiers in Oncology 2022; 12.
DOI:https://doi.org/10.3389/fonc.2022.897676.

## Kang B, Yuan X, Wang H, Qin S, Song X, Yu X, et al. Preoperative CT-Based Deep

Learning Model for Predicting Risk Stratification in Patients With Gastrointestinal
Stromal Tumors. Frontiers in Oncology 2021; 11.
DOI:https://doi.org/10.3389/fonc.2021.750875.

<!-- Page 30 -->


## He Y, Pan I, Bao B, Halsey K, Chang M, Liu H, et al. Deep learning-based

classification of primary bone tumors on radiographs: A preliminary study.
eBioMedicine 2020; 62: 103121.

## Peeken JC, Asadpour R, Specht K, Chen EY, Klymenko O, Akinkuoroye V, et al.

MRI-based delta-radiomics predicts pathologic complete response in high-grade softtissue sarcoma patients treated with neoadjuvant therapy. Radiotherapy and oncology
2021; 164: 73–82.

## Foreman S, Llorián-Salvador O, David D, Rösner VKN, Rischewski JF, Feuerriegel

GC, et al. Development and Evaluation of MR-Based Radiogenomic Models to
Differentiate Atypical Lipomatous Tumors from Lipomas. Cancers 2023; 15: 2150–
0.

## Spraker MB, Wootton L, Hippe DS, Ball KC, Peeken JC, Macomber MW, et al. MRI

Radiomic Features Are Independently Associated With Overall Survival in Soft
Tissue Sarcoma. Advances in radiation oncology 2019; 4: 413–21.

## Fradet G, Ayde R, Bottois H, El Harchaoui M, Khaled W, Drape JL, et al. Prediction

of lipomatous soft tissue malignancy on MRI: comparison between machine learning
applied to radiomics and deep learning. European Radiology Experimental 2022; 6.
DOI:https://doi.org/10.1186/s41747-022-00295-9.

## Gitto S, Cuocolo R, Annovazzi A, Anelli V, Acquasanta M, Cincotta A, et al. CT

radiomics-based machine learning classification of atypical cartilaginous tumours and
appendicular chondrosarcomas. EBioMedicine 2021; 68: 103407–7.

## Kwong J, Khondker A, Lajkosz K, et al. APPRAISE-AI Tool for Quantitative

Evaluation of AI Studies for Clinical Decision Support. JAMA network open 2023; 6:
e2335377–7.

## Collins GS, Moons K, Dhiman P, et al. TRIPOD+AI statement: updated guidance for

reporting clinical prediction models that use regression or machine learning methods.
BMJ 2024; e078378–8.

## Lambin P, Leijenaar R, Deist T, et al. Radiomics: the bridge between medical

imaging and personalized medicine. Nature Reviews Clinical Oncology 2017; 14:
749–62.

<!-- Page 31 -->


### Supplementary Table

Table S1: Score analysis for different predicted outcomes, disease types, and AI methods of
the top 20 studies in terms of highest combined CLAIM and FUTURE-AI score.
Mean

### Mean

FUTURE AUC Accuracy Sensitivity Specificity

### Categories N CLAIM

-AI range range range range
score
score
Diagnosis 12 41·2 8·7 0·78-0·95 0·69-0·92 0·57-1·00 0·63-0·93

### Outcome

Prognosis 7 39·0 7·9 0·64-0·93 0·77-0·90 0·20-0·79 0·68-0·97
type

### Both 1 40·0 9·0 0·82-0·86 0·67-0·84 0·67-0·84 0·74-1·00

Bone tumour 8 41·4 8·1 0·78-0·94 0·69-0·92 0·57-0·90 0·67-0·92

### Disease

Soft-tissue tumour 9 38·9 8·6 0·75-0·93 0·67-0·90 0·20-1·00 0·63-1·00
typea

## Gist 3 42·0 8·7 0·64-0·95 0·75-0·92 0·24-0·90 0·75-0·93


### Hand-crafted

11 39·5 7·6 0·75-0·94 0·75-0·92 0·20-0·92 0·67-0·95
features

### Model-learned

Method 6 42·8 9·3 0·64-0·95 0·67-0·92 0·24-0·90 0·74-1·00
features
type
Combined handcrafted and model- 3 38·3 9·5 0·80-0·86 0·80-0·86 0·47-1·00 0·63-0·97
learned features
The ranges presented in the table are derived from the minimum and maximum values reported for each metric across the
selected studies. For the study categorized under 'both,' performance metrics were reported from three external validation
sites, contributing to the observed ranges.
a No papers investigating both Soft-tissue tumour (STT) and Bone tumours were in the top 20 scoring papers.

<!-- Page 32 -->


### Figures

Figure 1: Reviewing methodology.

<!-- Page 33 -->

Figure 2: PRISMA flow diagram.

<!-- Page 34 -->

Figure 3: Number of included studies (n=325) between 2008 and July 2024, color coded for the various
AI methodologies used.

<!-- Page 35 -->

Figure 4: Characteristics of the studies included (n=325) as percentages.

<!-- Page 36 -->

Figure 5: Reported and unreported criteria for the included studies (n=325) from the Checklist for Artificial
Intelligence in Medical Imaging (CLAIM). Gray bars between criteria within categories indicate
subcategories.

<!-- Page 37 -->

Figure 6: Scores of the included studies (n=325) for each criterion from the FUTURE-AI international
consensus guideline for trustworthy and deployable AI. For each criterion, expected compliance for both
research (Res.) and deployable (Dep.) AI tools is reported. F = Fairness, U = Universality, T = Traceability,
U = Usability, R = Robustness, E = Explainability, G = General recommendations.

<!-- Page 38 -->


### Supplementary Figures

Figure S1: Inter-reader variability sub-group analysis (n=30) for criteria of the Checklist for Artificial
Intelligence in Medical Imaging (CLAIM). Agreement before (green) and after (orange) consensus
discussion is reported between raters.

<!-- Page 39 -->

Figure S2: Inter-reader variability sub-group analysis (n=30) for criteria of the FUTURE-AI international
consensus guideline for trustworthy and deployable AI. Agreement before (green) and after (orange)
consensus discussion is reported between raters.

<!-- Page 40 -->

Figure S3: Trend of scores on the Checklist for Artificial Intelligence in Medical Imaging (CLAIM) for
each year across included studies (n=325). Red dots represent the mean score for each year, while each
blue dot corresponds to a single study, with their positions slightly adjusted to avoid overlap. The
regression line is calculated with the starting point (x = 0) set to 2008.

<!-- Page 41 -->

Figure S4: Trend of scores on the FUTURE-AI international consensus guideline for trustworthy and
deployable AI for each year across included studies (n=325). Red dots represent the mean score for each
year, while each blue dot corresponds to a single study, with their positions slightly adjusted to avoid
overlap. The regression line is calculated with the starting point (x = 0) set to 2008.

<!-- Page 42 -->

Figure S5: Scores on the Checklist for Artificial Intelligence in Medical Imaging (CLAIM) for different
AI methods, disease types and predicted outcomes across included studies (n=325).

<!-- Page 43 -->

Figure S6: Scores on the FUTURE-AI international consensus guideline for trustworthy and deployable
AI for different AI methods, disease types and predicted outcomes across included studies (n=325).

<!-- Page 44 -->

Figure S7: Reported and unreported criteria for each study (n=325) from the Checklist for Artificial
Intelligence in Medical Imaging (CLAIM). An interactive version of this plot can be found at:
https://douwe-spaanderman.github.io/AI-STTandBoneTumour-Review/#
Figure S8: Scores of each study (n=325) for each criterion from the FUTURE-AI international consensus
guideline for trustworthy and deployable AI. An interactive version of this plot can be found at:
https://douwe-spaanderman.github.io/AI-STTandBoneTumour-Review/#

<!-- Page 45 -->


### Appendix 1: Search strategy

Database searched Platform Coverage period

### Medline ALL Ovid 1946 – 07/2024


### Embase Embase.com 1971 - 07/2024

Web of Science Core Collection* Web of Knowledge 1975 - 07/2024
Cochrane Central Register of Wiley 1992 - 07/2024

### Controlled Trials**

Additional Search Engines: Google Scholar***

### Total

*Science Citation Index Expanded (1975- 07/2024); Social Sciences Citation Index (1975- 07/2024); Arts & Humanities Citation Index (1975-
07/2024); Conference Proceedings Citation Index- Science (1990- 07/2024); Conference Proceedings Citation Index- Social Science &
Humanities (1990- 07/2024); Emerging Sources Citation Index (2005- 07/2024)
** Manually deleted abstracts from trial registries
***Google Scholar was searched via "Publish or Perish" to download the results in EndNote.
No other database limits were used than those specified in the search strategies

### Embase

('artificial intelligence'/exp OR 'machine learning'/exp OR 'pattern recognition'/exp OR 'radiomics'/exp
OR (CNN OR (artificial* NEAR/3 intelligen*) OR ((machine OR deep) NEAR/3 learning) OR (neural*
NEAR/3 network*) OR (classification* NEAR/3 (algorithm OR binary OR multiclass OR multilabel)) OR
(classifier*) OR (data-mining*) OR (feature NEAR/3 detection*) OR (feature* NEAR/3 (extraction OR
learning OR ranking OR selection OR analysis OR fusion*)) OR (k-nearest* NEAR/3 neighbo*) OR
(kernel* NEAR/3 method*) OR (learning* NEAR/3 algorithm*) OR (least* NEAR/3 absolute* NEAR/3
shrinkage* NEAR/3 selection* NEAR/3 operator*) OR (Markov* NEAR/3 model*) OR (memristor*) OR
(network* NEAR/3 learning*) OR (perceptron*) OR (radial* NEAR/3 basis* NEAR/3 function*) OR
(random* NEAR/3 forest*) OR (recursive* NEAR/3 feature* NEAR/3 elimination*) OR (recursive*
NEAR/3 partitioning*) OR (support* NEAR/3 vector* NEAR/3 machine*) OR ((recognition* OR
detection* OR classification* OR predict* OR comput* OR diagnos*) NEAR/3 (algorithm* OR network*
OR computer-aided* OR automatic* OR automated*)) OR bayesian* OR radiomic* OR pattern-recognit*
OR ((AI) NEXT/1 (tool* OR model*))):ab,ti,kw OR AI:ti) AND ('musculoskeletal tumor'/exp OR 'bone
cyst'/exp OR 'fibrous dysplasia'/exp OR 'lipoma'/exp OR 'hibernoma'/exp OR 'mesenchymoma'/exp OR
'lymphoma'/exp OR 'histiocytosis'/exp OR 'sinus histiocytosis'/exp OR 'sarcoma'/exp OR 'soft tissue
tumor'/exp OR 'nerve tumor'/exp OR 'lymphangioma'/exp OR 'lipoblastoma'/exp OR 'ganglion cyst'/exp
OR (GCTB OR DDLS OR GIST OR GISTs OR ((soft-tissue* OR adipos*-tissue* OR glomus* OR gastrointeststroma* OR gastr*-intest*-stroma* OR spinal* OR rib OR skull OR sternal* OR tibial* OR sacrum* OR jaw
OR maxillar* OR mandibular* OR odontogenic* OR connective-tissue* OR subcutan*-tissue* OR vein*
OR muscle* OR musculoskeletal* OR bone* OR benign-notochordal-cell OR fibrous* OR osteoblast* OR
osteoclast* OR synov* OR granular-cell* OR cartilag* OR joint* OR femoral* OR humerus* OR lympho*
OR rhabdoid OR non-ossifying OR extramedullary-myeloid* OR atypical-lipmatous* OR nerve* OR giantcell* OR schwann-cell* OR desmoplastic* OR myofibroblastic*) NEAR/3 (tumor* OR tumour* OR
cancer* OR neoplas* OR maligna* OR lesion* OR plasmacytom* OR metasta*)) OR ((vascular* OR
arter* OR vessel* OR venal*) NEXT/1 (tumor* OR tumour* OR cancer* OR neoplas* OR maligna* OR
lesion* OR plasmacytom* OR metasta*)) OR ((lymph-node*) NEAR/3 (tumor* OR tumour* OR cancer*
OR neoplas* OR maligna* OR lesion* OR plasmacytom*)) OR adamantin* OR plasma-cell-granulom* OR

<!-- Page 46 -->

glomangiom* OR myoma* OR desmoid* OR Bessel-Hagen OR diaphyseal-aclas* OR ((subungual OR
multipl* OR dysplas* OR familial*) NEAR/3 (exosto*)) OR osteocyst* OR ecchondrosis-ossificans OR
chondrodysplasia OR adenosarcom* OR sarcom* OR gliosarcoma* OR adenosarcom* OR osteosarcom*
OR chondrosarcom* OR chondrom* OR enchondrom* OR chondroblastom* OR chondromatosis* OR
osteom* OR osteoblastom* OR osteochondrom* OR maffucci* OR hemangiom* OR haemangiom* OR
hemangioendotheliom* OR angiosarcom* OR bone-cyst* OR osseous-cyst* OR intraosseous-gangli* OR
intra-osseous-gangli* OR ganglion-cyst* OR jaw-cyst* OR subchondral-cyst* OR chordom* OR
synoviom* OR ((fibro*) NEAR/2 (dysplas* OR dystroph* OR osteodys*)) OR cherubism* OR osteofibrousdysplasi* OR lipom* OR angiolipom* OR angiom* OR lipomatos* OR fetal-lipoma* OR Bannayan OR
fatty-kidney OR fatty-pancreas* OR hibernom* OR mesenchym* OR adamantinom* OR hodgkin* OR
erdheim-Chester* OR chester-erdheim* OR eosinophil*-granulom* OR histiocytos* OR dorfman-rosaidisease* OR nora-s-lesion* OR chondromesenchymal-hamartoma-of-chest-wall* OR lymphom* OR
fibroma* OR osteoclastom* OR histioblastom* OR histiosarcom* OR leiomyosarcom* OR
angioendotheliom* OR angioendotheliosarcom* OR hemangiosarcom* OR haemangiosarcom* OR
haemangioendotheliom* OR hemangio-endotheliosarcom* OR hemangioendotheliom* OR
hemangioendotheliosarcom* OR hemangio-endotheliom OR haemangio-endotheliom* OR
lymphangiosarcom* OR Stewart-Treves OR rhabdomysarcom* OR myxofibrosarcom* OR myxosarcom*
OR myofibrom* OR myofibroblastom* OR synoviom* OR myxom* OR myopericytom* OR fibrosarcom*
OR fibroadenosarcom* OR dermatofibrosarcom* OR neurofibrosarcom* OR chloroma* OR
extramedullary-leukaemia* OR extramedullary-leukemia* OR leukosarcom* OR liposarcom* OR
neurom* OR perineurom* OR ganglionneurom* OR neurilemom* OR neurofibrom* OR neurothekeom*
OR leiomyom* OR rhabdomyom* OR elastofibroma* OR lymphangiom* OR hemangiopericytom* OR
haemangiopericytom* OR pericytom* OR myopericytom* OR glomangiopericytom* OR lipoblastom* OR
schwannom* OR neurilemmom* OR neurinom* OR neurolemmom* OR neurilemom* OR
neurolilemmon* OR ((pigment* OR arthritis*) NEAR/3 (villonodular* OR villous*)) OR ((arthritis*)
NEAR/3 (pigment* OR schueller*)) OR ((synovitis*) NEAR/3 (pigment* OR dendritic* OR villonodular*))
OR lymphosarcom* OR reticulosarcom* OR rhabdomyosarcom* OR ameloblastom* OR myosarcom* OR
fibrosarcom* OR myoblastom* OR fibrous-histiocytom* OR histiomatos* OR reticulohistiocyt*):ab,ti,kw)
AND ('radiomics'/exp OR 'radiogenomics'/exp OR 'diagnostic imaging'/de OR 'radiodiagnosis'/exp OR
'nuclear magnetic resonance imaging'/exp OR 'diffusion coefficient'/de OR 'diffusion weighted
imaging'/de OR 'Doppler flowmetry'/de OR 'echography'/exp OR (radiogenomic* OR ((radio OR radiat*)
NEXT/1 (genomic* OR diagnos*)) OR radiomic* OR ((diagnos* OR medical*) NEAR/3 imag*) OR radiogenomic* OR radiomic* OR (diagnos* NEAR/3 imag*) OR radiodiagnos* OR ((comput* OR positron)
NEAR/3 tomogra*) OR spect OR ct OR pet OR mri OR (magnetic NEAR/3 resonance) OR ((nuclear OR mr
OR multimodalit*) NEAR/3 imaging*) OR rontgen OR roentgen OR ultraso* OR scintigra* OR (diffusion*
NEAR/3 (coefficient* OR weighted OR tensor)) OR dwi OR dti OR Doppler OR echogra*):ab,ti,kw) NOT
([Conference Abstract]/lim AND [1800-2020]/py) NOT ('case report'/de OR (case-report):ti) NOT
((animal/exp OR animal*:de OR nonhuman/de) NOT ('human'/exp))

### Medline

(exp Artificial Intelligence/ OR exp Machine Learning/ OR Pattern Recognition, Automated/ OR (CNN OR
(artificial* ADJ3 intelligen*) OR ((machine OR deep) ADJ3 learning) OR (neural* ADJ3 network*) OR
(classification* ADJ3 (algorithm OR binary OR multiclass OR multilabel)) OR (classifier*) OR (data-

<!-- Page 47 -->

mining*) OR (feature ADJ3 detection*) OR (feature* ADJ3 (extraction OR learning OR ranking OR
selection OR analysis OR fusion*)) OR (k-nearest* ADJ3 neighbo*) OR (kernel* ADJ3 method*) OR
(learning* ADJ3 algorithm*) OR (least* ADJ3 absolute* ADJ3 shrinkage* ADJ3 selection* ADJ3
operator*) OR (Markov* ADJ3 model*) OR (memristor*) OR (network* ADJ3 learning*) OR
(perceptron*) OR (radial* ADJ3 basis* ADJ3 function*) OR (random* ADJ3 forest*) OR (recursive* ADJ3
feature* ADJ3 elimination*) OR (recursive* ADJ3 partitioning*) OR (support* ADJ3 vector* ADJ3
machine*) OR ((recognition* OR detection* OR classification* OR predict* OR comput* OR diagnos*)
ADJ3 (algorithm* OR network* OR computer-aided* OR automatic* OR automated*)) OR bayesian* OR
radiomic* OR pattern-recognit* OR ((AI) ADJ (tool* OR model*))).ab,ti,kf. OR AI.ti.) AND (exp Bone
Cysts/ OR exp Fibrous Dysplasia of Bone/ OR exp Lipoma/ OR exp Mesenchymoma/ OR exp Lymphoma/
OR exp Histiocytosis/ OR exp Histiocytosis, Sinus/ OR exp Sarcoma/ OR exp Soft Tissue Neoplasms/ OR
exp Neuroma/ OR exp Lymphangioma/ OR exp Ganglion Cysts/ OR (GCTB OR DDLS OR GIST OR GISTs OR
((soft-tissue* OR adipos*-tissue* OR glomus* OR gastrointest-stroma* OR gastr*-intest*-stroma* OR
spinal* OR rib OR skull OR sternal* OR tibial* OR sacrum* OR jaw OR maxillar* OR mandibular* OR
odontogenic* OR connective-tissue* OR subcutan*-tissue* OR vein* OR muscle* OR musculoskeletal*
OR bone* OR benign-notochordal-cell OR fibrous* OR osteoblast* OR osteoclast* OR synov* OR
granular-cell* OR cartilag* OR joint* OR femoral* OR humerus* OR lympho* OR rhabdoid OR nonossifying OR extramedullary-myeloid* OR atypical-lipmatous* OR nerve* OR giant-cell* OR schwanncell* OR desmoplastic* OR myofibroblastic*) ADJ3 (tumor* OR tumour* OR cancer* OR neoplas* OR
maligna* OR lesion* OR plasmacytom* OR metasta*)) OR ((vascular* OR arter* OR vessel* OR venal*)
ADJ (tumor* OR tumour* OR cancer* OR neoplas* OR maligna* OR lesion* OR plasmacytom* OR
metasta*)) OR ((lymph-node*) ADJ3 (tumor* OR tumour* OR cancer* OR neoplas* OR maligna* OR
lesion* OR plasmacytom*)) OR adamantin* OR plasma-cell-granulom* OR glomangiom* OR myoma* OR
desmoid* OR Bessel-Hagen OR diaphyseal-aclas* OR ((subungual OR multipl* OR dysplas* OR familial*)
ADJ3 (exosto*)) OR osteocyst* OR ecchondrosis-ossificans OR chondrodysplasia OR adenosarcom* OR
sarcom* OR gliosarcoma* OR adenosarcom* OR osteosarcom* OR chondrosarcom* OR chondrom* OR
enchondrom* OR chondroblastom* OR chondromatosis* OR osteom* OR osteoblastom* OR
osteochondrom* OR maffucci* OR hemangiom* OR haemangiom* OR hemangioendotheliom* OR
angiosarcom* OR bone-cyst* OR osseous-cyst* OR intraosseous-gangli* OR intra-osseous-gangli* OR
ganglion-cyst* OR jaw-cyst* OR subchondral-cyst* OR chordom* OR synoviom* OR ((fibro*) ADJ2
(dysplas* OR dystroph* OR osteodys*)) OR cherubism* OR osteofibrous-dysplasi* OR lipom* OR
angiolipom* OR angiom* OR lipomatos* OR fetal-lipoma* OR Bannayan OR fatty-kidney OR fattypancreas* OR hibernom* OR mesenchym* OR adamantinom* OR hodgkin* OR erdheim-Chester* OR
chester-erdheim* OR eosinophil*-granulom* OR histiocytos* OR dorfman-rosai-disease* OR nora-slesion* OR chondromesenchymal-hamartoma-of-chest-wall* OR lymphom* OR fibroma* OR
osteoclastom* OR histioblastom* OR histiosarcom* OR leiomyosarcom* OR angioendotheliom* OR
angioendotheliosarcom* OR hemangiosarcom* OR haemangiosarcom* OR haemangioendotheliom* OR
hemangio-endotheliosarcom* OR hemangioendotheliom* OR hemangioendotheliosarcom* OR
hemangio-endotheliom OR haemangio-endotheliom* OR lymphangiosarcom* OR Stewart-Treves OR
rhabdomysarcom* OR myxofibrosarcom* OR myxosarcom* OR myofibrom* OR myofibroblastom* OR
synoviom* OR myxom* OR myopericytom* OR fibrosarcom* OR fibroadenosarcom* OR
dermatofibrosarcom* OR neurofibrosarcom* OR chloroma* OR extramedullary-leukaemia* OR

<!-- Page 48 -->

extramedullary-leukemia* OR leukosarcom* OR liposarcom* OR neurom* OR perineurom* OR
ganglionneurom* OR neurilemom* OR neurofibrom* OR neurothekeom* OR leiomyom* OR
rhabdomyom* OR elastofibroma* OR lymphangiom* OR hemangiopericytom* OR
haemangiopericytom* OR pericytom* OR myopericytom* OR glomangiopericytom* OR lipoblastom* OR
schwannom* OR neurilemmom* OR neurinom* OR neurolemmom* OR neurilemom* OR
neurolilemmon* OR ((pigment* OR arthritis*) ADJ3 (villonodular* OR villous*)) OR ((arthritis*) ADJ3
(pigment* OR schueller*)) OR ((synovitis*) ADJ3 (pigment* OR dendritic* OR villonodular*)) OR
lymphosarcom* OR reticulosarcom* OR rhabdomyosarcom* OR ameloblastom* OR myosarcom* OR
fibrosarcom* OR myoblastom* OR fibrous-histiocytom* OR histiomatos* OR reticulohistiocyt*).ab,ti,kf.)
AND (exp Radiation Genomics/ OR Diagnostic Imaging/ OR exp Magnetic Resonance Imaging/ OR Laser-
Doppler Flowmetry/ OR exp Ultrasonography/ OR (radiogenomic* OR ((radio OR radiat*) ADJ1
(genomic* OR diagnos*)) OR radiomic* OR ((diagnos* OR medical*) ADJ3 imag*) OR radiodiagnos* OR
((comput* OR positron) ADJ3 tomogra*) OR spect OR ct OR pet OR mri OR (magnetic ADJ3 resonance)
OR ((nuclear OR mr OR multimodalit*) ADJ3 imaging*) OR rontgen OR roentgen OR ultraso* OR
scintigra* OR (diffusion* ADJ3 (coefficient* OR weighted OR tensor)) OR dwi OR dti OR Doppler OR
echogra*).ab,ti,kf.) NOT (news OR congres* OR abstract* OR book* OR chapter* OR dissertation
abstract*).pt. NOT (Case Reports/ OR (case-report).ti.) NOT (exp animals/ NOT humans/)

### Cochrane

((CNN OR (artificial* NEAR/3 intelligen*) OR ((machine OR deep) NEAR/3 learning) OR (neural* NEAR/3
network*) OR (classification* NEAR/3 (algorithm OR binary OR multiclass OR multilabel)) OR (classifier*)
OR (data NEXT/1 mining*) OR (feature NEAR/3 detection*) OR (feature* NEAR/3 (extraction OR learning
OR ranking OR selection OR analysis OR fusion*)) OR (k NEXT/1 nearest* NEAR/3 neighbo*) OR (kernel*
NEAR/3 method*) OR (learning* NEAR/3 algorithm*) OR (least* NEAR/3 absolute* NEAR/3 shrinkage*
NEAR/3 selection* NEAR/3 operator*) OR (Markov* NEAR/3 model*) OR (memristor*) OR (network*
NEAR/3 learning*) OR (perceptron*) OR (radial* NEAR/3 basis* NEAR/3 function*) OR (random* NEAR/3
forest*) OR (recursive* NEAR/3 feature* NEAR/3 elimination*) OR (recursive* NEAR/3 partitioning*) OR
(support* NEAR/3 vector* NEAR/3 machine*) OR ((recognition* OR detection* OR classification* OR
predict* OR comput* OR diagnos*) NEAR/3 (algorithm* OR network* OR computer NEXT/1 aided* OR
automatic* OR automated*)) OR bayesian* OR radiomic* OR pattern NEXT/1 recognit* OR ((AI) NEXT/1
(tool* OR model*))):ab,ti,kw OR AI:ti) AND ((GCTB OR DDLS OR GIST OR GISTs OR ((soft NEXT/1 tissue*
OR adipos* NEXT/1 tissue* OR glomus* OR gastrointest NEXT/1 stroma* OR gastr* NEXT/1 intest*
NEXT/1 stroma* OR spinal* OR rib OR skull OR sternal* OR tibial* OR sacrum* OR jaw OR maxillar* OR
mandibular* OR odontogenic* OR connective NEXT/1 tissue* OR subcutan* NEXT/1 tissue* OR vein* OR
muscle* OR musculoskeletal* OR bone* OR benign NEXT/1 notochordal NEXT/1 cell OR fibrous* OR
osteoblast* OR osteoclast* OR synov* OR granular NEXT/1 cell* OR cartilag* OR joint* OR femoral* OR
humerus* OR lympho* OR rhabdoid OR non NEXT/1 ossifying OR extramedullary NEXT/1 myeloid* OR
atypical NEXT/1 lipmatous* OR nerve* OR giant NEXT/1 cell* OR schwann NEXT/1 cell* OR
desmoplastic* OR myofibroblastic*) NEAR/3 (tumor* OR tumour* OR cancer* OR neoplas* OR maligna*
OR lesion* OR plasmacytom* OR metasta*)) OR ((vascular* OR arter* OR vessel* OR venal*) NEXT/1
(tumor* OR tumour* OR cancer* OR neoplas* OR maligna* OR lesion* OR plasmacytom* OR metasta*))
OR ((lymph NEXT/1 node*) NEAR/3 (tumor* OR tumour* OR cancer* OR neoplas* OR maligna* OR

<!-- Page 49 -->

lesion* OR plasmacytom*)) OR adamantin* OR plasma NEXT/1 cell NEXT/1 granulom* OR glomangiom*
OR myoma* OR desmoid* OR Bessel NEXT/1 Hagen OR diaphyseal NEXT/1 aclas* OR ((subungual OR
multipl* OR dysplas* OR familial*) NEAR/3 (exosto*)) OR osteocyst* OR ecchondrosis NEXT/1 ossificans
OR chondrodysplasia OR adenosarcom* OR sarcom* OR gliosarcoma* OR adenosarcom* OR
osteosarcom* OR chondrosarcom* OR chondrom* OR enchondrom* OR chondroblastom* OR
chondromatosis* OR osteom* OR osteoblastom* OR osteochondrom* OR maffucci* OR hemangiom*
OR haemangiom* OR hemangioendotheliom* OR angiosarcom* OR bone NEXT/1 cyst* OR osseous
NEXT/1 cyst* OR intraosseous NEXT/1 gangli* OR intra NEXT/1 osseous NEXT/1 gangli* OR ganglion
NEXT/1 cyst* OR jaw NEXT/1 cyst* OR subchondral NEXT/1 cyst* OR chordom* OR synoviom* OR
((fibro*) NEAR/2 (dysplas* OR dystroph* OR osteodys*)) OR cherubism* OR osteofibrous NEXT/1
dysplasi* OR lipom* OR angiolipom* OR angiom* OR lipomatos* OR fetal NEXT/1 lipoma* OR Bannayan
OR fatty NEXT/1 kidney OR fatty NEXT/1 pancreas* OR hibernom* OR mesenchym* OR adamantinom*
OR hodgkin* OR erdheim NEXT/1 Chester* OR chester NEXT/1 erdheim* OR eosinophil* NEXT/1
granulom* OR histiocytos* OR dorfman NEXT/1 rosai NEXT/1 disease* OR nora NEXT/1 s NEXT/1 lesion*
OR chondromesenchymal NEXT/1 hamartoma NEXT/1 of NEXT/1 chest NEXT/1 wall* OR lymphom* OR
fibroma* OR osteoclastom* OR histioblastom* OR histiosarcom* OR leiomyosarcom* OR
angioendotheliom* OR angioendotheliosarcom* OR hemangiosarcom* OR haemangiosarcom* OR
haemangioendotheliom* OR hemangio NEXT/1 endotheliosarcom* OR hemangioendotheliom* OR
hemangioendotheliosarcom* OR hemangio NEXT/1 endotheliom OR haemangio NEXT/1 endotheliom*
OR lymphangiosarcom* OR Stewart NEXT/1 Treves OR rhabdomysarcom* OR myxofibrosarcom* OR
myxosarcom* OR myofibrom* OR myofibroblastom* OR synoviom* OR myxom* OR myopericytom* OR
fibrosarcom* OR fibroadenosarcom* OR dermatofibrosarcom* OR neurofibrosarcom* OR chloroma* OR
extramedullary NEXT/1 leukaemia* OR extramedullary NEXT/1 leukemia* OR leukosarcom* OR
liposarcom* OR neurom* OR perineurom* OR ganglionneurom* OR neurilemom* OR neurofibrom* OR
neurothekeom* OR leiomyom* OR rhabdomyom* OR elastofibroma* OR lymphangiom* OR
hemangiopericytom* OR haemangiopericytom* OR pericytom* OR myopericytom* OR
glomangiopericytom* OR lipoblastom* OR schwannom* OR neurilemmom* OR neurinom* OR
neurolemmom* OR neurilemom* OR neurolilemmon* OR ((pigment* OR arthritis*) NEAR/3
(villonodular* OR villous*)) OR ((arthritis*) NEAR/3 (pigment* OR schueller*)) OR ((synovitis*) NEAR/3
(pigment* OR dendritic* OR villonodular*)) OR lymphosarcom* OR reticulosarcom* OR
rhabdomyosarcom* OR ameloblastom* OR myosarcom* OR fibrosarcom* OR myoblastom* OR fibrous
NEXT/1 histiocytom* OR histiomatos* OR reticulohistiocyt*):ab,ti,kw) AND ((radiogenomic* OR ((radio
OR radiat*) NEXT/1 (genomic* OR diagnos*)) OR radiomic* OR ((diagnos* OR medical*) NEAR/3 imag*)
OR radio NEXT/1 genomic* OR radiomic* OR (diagnos* NEAR/3 imag*) OR radiodiagnos* OR ((comput*
OR positron) NEAR/3 tomogra*) OR spect OR ct OR pet OR mri OR (magnetic NEAR/3 resonance) OR
((nuclear OR mr OR multimodalit*) NEAR/3 imaging*) OR rontgen OR roentgen OR ultraso* OR
scintigra* OR (diffusion* NEAR/3 (coefficient* OR weighted OR tensor)) OR dwi OR dti OR Doppler OR
echogra*):ab,ti,kw) NOT "conference abstract":pt

### Web of Science

TS=(((CNN OR (artificial* NEAR/2 intelligen*) OR ((machine OR deep) NEAR/2 learning) OR (neural*
NEAR/2 network*) OR (classification* NEAR/2 (algorithm OR binary OR multiclass OR multilabel)) OR
(classifier*) OR (data-mining*) OR (feature NEAR/2 detection*) OR (feature* NEAR/2 (extraction OR
learning OR ranking OR selection OR analysis OR fusion*)) OR (k-nearest* NEAR/2 neighbo*) OR

<!-- Page 50 -->

(kernel* NEAR/2 method*) OR (learning* NEAR/2 algorithm*) OR (least* NEAR/2 absolute* NEAR/2
shrinkage* NEAR/2 selection* NEAR/2 operator*) OR (Markov* NEAR/2 model*) OR (memristor*) OR
(network* NEAR/2 learning*) OR (perceptron*) OR (radial* NEAR/2 basis* NEAR/2 function*) OR
(random* NEAR/2 forest*) OR (recursive* NEAR/2 feature* NEAR/2 elimination*) OR (recursive*
NEAR/2 partitioning*) OR (support* NEAR/2 vector* NEAR/2 machine*) OR ((recognition* OR
detection* OR classification* OR predict* OR comput* OR diagnos*) NEAR/2 (algorithm* OR network*
OR computer-aided* OR automatic* OR automated*)) OR bayesian* OR radiomic* OR pattern-recognit*
OR ((AI) NEAR/1 (tool* OR model*))) OR AI:ti) AND ((GCTB OR DDLS OR GIST OR GISTs OR ((soft-tissue*
OR adipos*-tissue* OR glomus* OR gastrointest-stroma* OR gastr*-intest*-stroma* OR spinal* OR rib
OR skull OR sternal* OR tibial* OR sacrum* OR jaw OR maxillar* OR mandibular* OR odontogenic* OR
connective-tissue* OR subcutan*-tissue* OR vein* OR muscle* OR musculoskeletal* OR bone* OR
benign-notochordal-cell OR fibrous* OR osteoblast* OR osteoclast* OR synov* OR granular-cell* OR
cartilag* OR joint* OR femoral* OR humerus* OR lympho* OR rhabdoid OR non-ossifying OR
extramedullary-myeloid* OR atypical-lipmatous* OR nerve* OR giant-cell* OR schwann-cell* OR
desmoplastic* OR myofibroblastic*) NEAR/2 (tumor* OR tumour* OR cancer* OR neoplas* OR maligna*
OR lesion* OR plasmacytom* OR metasta*)) OR ((vascular* OR arter* OR vessel* OR venal*) NEAR/1
(tumor* OR tumour* OR cancer* OR neoplas* OR maligna* OR lesion* OR plasmacytom* OR metasta*))
OR ((lymph-node*) NEAR/2 (tumor* OR tumour* OR cancer* OR neoplas* OR maligna* OR lesion* OR
plasmacytom*)) OR adamantin* OR plasma-cell-granulom* OR glomangiom* OR myoma* OR desmoid*
OR Bessel-Hagen OR diaphyseal-aclas* OR ((subungual OR multipl* OR dysplas* OR familial*) NEAR/2
(exosto*)) OR osteocyst* OR ecchondrosis-ossificans OR chondrodysplasia OR adenosarcom* OR
sarcom* OR gliosarcoma* OR adenosarcom* OR osteosarcom* OR chondrosarcom* OR chondrom* OR
enchondrom* OR chondroblastom* OR chondromatosis* OR osteom* OR osteoblastom* OR
osteochondrom* OR maffucci* OR hemangiom* OR haemangiom* OR hemangioendotheliom* OR
angiosarcom* OR bone-cyst* OR osseous-cyst* OR intraosseous-gangli* OR intra-osseous-gangli* OR
ganglion-cyst* OR jaw-cyst* OR subchondral-cyst* OR chordom* OR synoviom* OR ((fibro*) NEAR/2
(dysplas* OR dystroph* OR osteodys*)) OR cherubism* OR osteofibrous-dysplasi* OR lipom* OR
angiolipom* OR angiom* OR lipomatos* OR fetal-lipoma* OR Bannayan OR fatty-kidney OR fattypancreas* OR hibernom* OR mesenchym* OR adamantinom* OR hodgkin* OR erdheim-Chester* OR
chester-erdheim* OR eosinophil*-granulom* OR histiocytos* OR dorfman-rosai-disease* OR nora-slesion* OR chondromesenchymal-hamartoma-of-chest-wall* OR lymphom* OR fibroma* OR
osteoclastom* OR histioblastom* OR histiosarcom* OR leiomyosarcom* OR angioendotheliom* OR
angioendotheliosarcom* OR hemangiosarcom* OR haemangiosarcom* OR haemangioendotheliom* OR
hemangio-endotheliosarcom* OR hemangioendotheliom* OR hemangioendotheliosarcom* OR
hemangio-endotheliom OR haemangio-endotheliom* OR lymphangiosarcom* OR Stewart-Treves OR
rhabdomysarcom* OR myxofibrosarcom* OR myxosarcom* OR myofibrom* OR myofibroblastom* OR
synoviom* OR myxom* OR myopericytom* OR fibrosarcom* OR fibroadenosarcom* OR
dermatofibrosarcom* OR neurofibrosarcom* OR chloroma* OR extramedullary-leukaemia* OR
extramedullary-leukemia* OR leukosarcom* OR liposarcom* OR neurom* OR perineurom* OR
ganglionneurom* OR neurilemom* OR neurofibrom* OR neurothekeom* OR leiomyom* OR
rhabdomyom* OR elastofibroma* OR lymphangiom* OR hemangiopericytom* OR
haemangiopericytom* OR pericytom* OR myopericytom* OR glomangiopericytom* OR lipoblastom* OR
schwannom* OR neurilemmom* OR neurinom* OR neurolemmom* OR neurilemom* OR
neurolilemmon* OR ((pigment* OR arthritis*) NEAR/2 (villonodular* OR villous*)) OR ((arthritis*)

<!-- Page 51 -->

NEAR/2 (pigment* OR schueller*)) OR ((synovitis*) NEAR/2 (pigment* OR dendritic* OR villonodular*))
OR lymphosarcom* OR reticulosarcom* OR rhabdomyosarcom* OR ameloblastom* OR myosarcom* OR
fibrosarcom* OR myoblastom* OR fibrous-histiocytom* OR histiomatos* OR reticulohistiocyt*)) AND
((radiogenomic* OR ((radio OR radiat*) NEAR/1 (genomic* OR diagnos*)) OR radiomic* OR ((diagnos*
OR medical*) NEAR/2 imag*) OR radio-genomic* OR radiomic* OR (diagnos* NEAR/2 imag*) OR
radiodiagnos* OR ((comput* OR positron) NEAR/2 tomogra*) OR spect OR ct OR pet OR mri OR
(magnetic NEAR/2 resonance) OR ((nuclear OR mr OR multimodalit*) NEAR/2 imaging*) OR rontgen OR
roentgen OR ultraso* OR scintigra* OR (diffusion* NEAR/2 (coefficient* OR weighted OR tensor)) OR dwi
OR dti OR Doppler OR echogra*)) NOT ((animal* OR rat OR rats OR mouse OR mice OR murine OR dog
OR dogs OR canine OR cat OR cats OR feline OR rabbit OR cow OR cows OR bovine OR rodent* OR sheep
OR ovine OR pig OR swine OR porcine OR veterinar* OR chick* OR zebrafish* OR baboon* OR
nonhuman* OR primate* OR cattle* OR goose OR geese OR duck OR macaque* OR avian* OR bird* OR
fish*) NOT (human* OR patient* OR women OR woman OR men OR man))) NOT DT=(Meeting Abstract
OR Meeting Summary) NOT TI=(case-report)

### Google Scholar

“artificial intelligence”|”machine|deep learning”|”neural network”|radiomics
“musculoskeletal|bone|nerve tumor|tumour|neoplasm|cancer”|“soft tissue
tumor|tumour|neoplasm|cancer” radiomics|radiogenomics|”diagnostic imaging”|”radio
diagnosis”|MRI|doppler

<!-- Page 52 -->

Appendix 2

## Welcome

This document contains checklists based on the CLAIM [1] and FUTURE-AI [2] guidelines.
These checklists were used to assess the quality of research using AI in the diagnosis and
prognosis of soft tissue and bone tumours. A completed checklist, used in the study "AI in
radiological imaging of soft-tissue and bone tumours: a systematic review evaluating against
CLAIM and FUTURE-AI guidelines" can be found at: https://douwe-spaanderman.github.io/AI-
STTandBoneTumour-Review [3].
The second page in this document (general information) records basic information about each
paper and the intial of the reviewer. The third page (FUTURE-AI) gives the checklist based on
FUTURE-AI. As well as having a scoring system for each item it is divided into each principle
and indiates if an item is "recommended" or "highly-recommended" by the FUTURE-AI
guidelines. The fourth page gives the checklist based on CLAIM guidelines. Each item is
placed within in its corresponding topic.
The CLAIM checklist has been adapted from the checklist initially developed by Si et al. [4],
which used the original version of CLAIM [5] rather than the updated one. The checklist in this
document has adapted the checklist created by Si et al. to reflect the 2024 update of CLAIM
[1].

## References

[1] Tejani AS, Klontzas ME, Gatti AA, Mongan JT, Moy L, Park SH, Kahn CE Jr; CLAIM 2024
Update Panel. Checklist for Artificial Intelligence in Medical Imaging (CLAIM): 2024 Update.
Radiol Artif Intell. 2024 Jul;6(4):e240300. doi: 10.1148/ryai.240300. PMID: 38809149; PMCID:

## Pmc11304031.

[2] Lekadir K, Feragen A, Fofanah AJ, et al. FUTURE-AI: International consensus guideline for
trustworthy and deployable artificial intelligence in healthcare. arXiv 2024; published online

### July. DOI:https://doi.org/10.48550/arXiv.2309.12325

[3] Spaanderman D, Marzetti M, Wan X, Starmans M, Klein S. AI in radiological imaging of softtissue and bone tumours: a systematic review evaluating against best-practice guidelines.
Github. 2024; published online Aug 21. https://douwe-spaanderman.github.io/AI-

### STTandBoneTumour-Review

[4] Si L, Zhong J, Huo J, Xuan K, Zhuang Z, Hu Y, Wang Q, Zhang H, Yao W. Deep learning in
knee imaging: a systematic review utilizing a Checklist for Artificial Intelligence in Medical

### Imaging (CLAIM). European Radiology. 2022 Feb 1:1-9

[5] Mongan J, Moy L, Kahn CE Jr. Checklist for Artificial Intelligence in Medical Imaging
(CLAIM): A Guide for Authors and Reviewers. Radiol Artif Intell. 2020 Mar 25;2(2):e200029.
doi: 10.1148/ryai.2020200029. PMID: 33937821; PMCID: PMC8017414.

<!-- Page 53 -->

General Information
(sub)Section Values
Rater

### Year


### Journal


### Type imaging

prognosis / diagnosis 0. Diagnosis 1. Prognosis 2. Both
Soft tissue tumour/ Bone tumour/
Which disease?

## Gist


### Used publicly available dataset 0. No 1. Yes 2. Both

Retrospective vs prospective 0. Retrospective 1. Prospective
Signle centre vs multi-centre 0. Single-centre 1. Multi-centre
Data available 0. No 1. Upon request 2. Yes
Code Available 0. No 1. Upon request 2. Yes

## Not learning 1. Hand crafted

Methods features 2. Model-learned features 3.
Combined

<!-- Page 54 -->


### FUTURE-AI Checklist

Principle no. Recommendations Low ML-TRL High ML-TRL Description Scoring criteria
Bias in medical AI is application-specific. At the design phase, the development team should identify possible types and sources 0) No potential biases were discussed prior to AI development,
1 Define any potential sources of bias from an early stage ++ ++ o m f e b d i i a c s a l f o p r r o th fi e l i e r s A o I f t t o h o e l i . n T d h iv e i s d e u m al a s y ( e i . n g c . l u w d i e t h g r c o o u m p o a r t b t i r d ib it u i t e e s s o ( r e . d g i . s a s b ex il , i t g y e ) n , d as e r w , a e g ll e , a s e t h h u n m ici a t n y , b s ia o s c e i s o e ( c e o .g n . o d m a i t c a s l , a g b e e o ll g in ra g p , h d y a ) t , a t he 0 d . i 5 sc ) u P s o se te d n p ti r a i l o r b i t a o s e A s I i d n e a v t e l l o ea p s m t e 1 n g t, r oup (group attributes, medical profile, human biases) were
curation, or the selection of the input features). 1) Potential biases in all 3 groups were discussed prior to AI development.
F 2 Collect data on individuals’ attributes, when possible + + T e b t y o h n e id i t c h e i i n t c y t s i , f c y r o i s b m k ia m f s a e i c t s t t o e a e r n s s d , t c o a o p e m p n l o s y u r b m re id e a a i n t s i u e a r s p e p s o r r f o o d p r i r s i i a a n b t c e i r l e b i a t a s i l e e a s d n , c f s e a h i b r o n e u e t l w s d s e , b e r e n e l c t e o h v l e a l e n b c t e t n e a d e tt f . r i i t T b s h u f i t o s e r s s n h o o o f n u t - h l d d e i s b i c n e r d i s m i u v i b i n d j a e u t c a i t o l s n t , o a s i n u n d c f h o r r i a m s s k e s s d e f x c o , o r n g re s e - e n i n d d t e e r a n , n t i a d f g i c a e a p , t p io ro n v . al 0 0 f 1 a ) . ) c 5 N t M ) o o A r o s r r t ( e e a l l s e t e h a v 1 s a a t n i n t t t e t h m w a e t o ) t t , r w i a c b t o o t u r m t a i e b t o s t u r r i t o b b e f i s u d t t i i h e t n e s i e t i p s h n a e o t t i r l h e i d n e s i t t l s i w w a s b t e e i r r c l e e i o t c l i c e l o o e s l l c ) l l t e e e c c d t t e e ; d d ( , ; l i O st R :s w ex i t O h R ot h g e e r n d at e t r r , i b a u g t e e , s ethnicity, risk
3 Evaluate potential biases and bias correction measures + ++ W m r a 2 e c ) p e c . h t r u e r e r n i s a c e c s p n y . o t . T a s t I s o i m i o b c n p l o e s o r , , r r t e i e a c . q n e t u . t f l a t o y l h r i , e s a a e i n n d n y y d o i i p d v d o d i e t d s n e u t n p i a t f o l i i s a s e ’ t l d - p a b b t r i t o i a r a s i c s b e e s u s s h s t , o i e n s m u g l a i d ) r t e i a b g n i e a d n t d c i o t l o e u n c s d u t m e e m d d e e a i t n n s o t u e v t r d h e e e s r a i n d s fy h d a t o t a r h u e , e l p b d i o r i r b a i t s m e e d d a p e p t a t o p c e l t c i i t n o e i d f n o o n ( r b e m o m .g t h e t . h t h d t e h a o e e t d a n s t d o r e - s o u - h l s s o ’ a e s u m r l s f d a p a i l r b n i n n e d e g s a c , s p i b t p a i i l z n a i e d e s n d - f s t r h b e ( e e y s e m u e s o T i d n r e a g l c ’ e f s a a i b r i n l e it s y s 0 0 1 ap ) . ) 5 p B B ) l i i i B e a a s s s i ) e a e s s s e w w s e e w r r e e e r n a e l e s i i n o th v c e e o r s r t i r i n e g v c a t e t e s e d t d i g f a o a n r t d e b d r y e n p m o o r i r t t c i e o g d r a , r t e i c o t n e d m f e o a r s , ures (In case of no biases found, 3 also
0) The clinical setting was not reported
At the design phase, the development team should specify the clinical settings in which the AI tool will be applied (e.g. primary 0.5) Clinical setting outlined (e.g. primary healthcare centres, hospitals, home care, low vs. high-
1 Define intended clinical settings and cross-setting variations ++ ++ healthcare centres, hospitals, home care, low vs. high-resource settings, one or multiple countries), and anticipate potential resource settings, one or multiple countries)
obstacles to universality (e.g. differences in clinical definitions, medical equipment or IT infrastructures across settings). 1) Clinical setting outlined and potential obstacles to universality discussed (e.g. differences in
clinical definitions, medical equipment or IT infrastructures across settings)
2 Use community-defined stand s a t r a d n s d ( a e r . d g s . ) clinical definitions, technical + + T T F o h H e I e s R n e s m H ur L a e y 7 t ) h i , n e d c q l a u u ta d a l e a i n t c y n l i o a n t n i a c d t a i l o i n n d t s e e , f r i o e n p v i e t a i r l o a u b n a i s t l i , i o t m n y e c o d r f i i t c t e a h r l e i a o , A n a I t n o t d o lo o t g e l, i c e h i s t n ( i s e c h . a g o l u . s l S t d a N n b d O e a M r d d e E s v D e (e l o . C g p . T e d I , E 1 b 0 E a E s O e 1 M d 3 o O o n r P I e 1 S x 1 O i ) s , 1 t i i 4 n n ) g t . e r c f o a m ce m st u a n n i d ty ar - d d s e f ( i e n . e g d . s D ta IC nd O a M rds , . A 0 1 ) ) r e N Y c o e o s mmunity defined standards used:
U To assess generalisability, technical validation of the AI tools should be performed with external datasets that are distinct from
those used for training. These may include reference or benchmarking datasets which are representative for the task in question (i.e. 0) This study only used single center data --> no external validation;
3 Evaluate using external datasets and/or multiple sites ++ ++ a s p h p o r u o l x d im be a t p i e n r g fo t r h m e e e d x p at e c m te u d l t r i e p a l l e - w si o t r e l s d t v o a a ri s a s t e i s o s n s p ) e . r f E o x rm ce a p n t c f e o r a n A d I i t n o t o er ls o p in er t a e b n i d l e it d y f a o c r r o si s n s g c l l e i n c i e c n a t l r e w s, o r t k h f e l o c w lin s. i c I a f l t h ev e a t l o u o a l t ’ i s o n studies 0 p . u 5 b ) l i E c v a a v lu ai a l t a i b o l n e ) w ; as performed using external dataset from one other site (or same source, e.g.
generalisability is limited, mitigation measures (e.g. transfer learning or domain adaptation) should be considered, applied and 1) Evaluation was performed using external dataset from multiple sites;
tested.
4 Evaluate and demonstrate local clinical validity + ++ C e w A a l o I c i h r n m k i s f c o l i a o d t l e w e , s l s e t s t h a h t e i n o n d A u g l s I p d e t v o r b a f o e o r y l r p s m e i s n r h f w o o m e r u m l a l l n d e o y d b n a e ( s t e h e p .g v e e . c a l , t l o u s t c , h a a t r s l e o u d p u c o g h fo p h a r u s m l t a h p o t e o i d i o p r e n u l l s o l f . a i c t n I a i f e l o - t n c t h u l s e i , n n p i e i n c e q g a r u f l i o o p v r r m m a r l e i a e d t n n r i c a t t , e i y n c . i i l s n I i n n g d i ) e p c . c a a r l r e t w a ic s o u e r d l k a r f w , l o h t w h en e s , A e a v I n a t d l o u o e a n t l e d s d - h u l o s o u e c l r a d s l . l f y H i , t e r t n e h c - e c e a l t l o o i c b a e r l a n t c s i l u o i r n n e i o c t a r f u l t s h t e a t 0 d 0 1 h ) e . ) a 5 p v l l ) o l o e o c l c b y o a a e l e c l e d a c c n l l l o i i c d n n u l e i i i t c n c p s a a i i l l d c l o a e y v v l e a a o v d l l f i i a d d t r l o i e i i t d t s y y d e i t a e h y h r a a c a l h s h s w a n b s s i o e e t b t e h t t e n i b e t n h e n d g e i i / s n d s e c i x l u d s o t c i s e c s u s r a c n s e l u s d a c s e l l s l d a i y e n n d ) a d i n c , d a e o l v r e a v v w l a u a l a l a i s u d te a i n d t t y e o d a . t n , a d p p if l i n ca ee b d le e d (e , . m g. i t A ig I a t t o io o n l w st a ra s t e n g o i t e s
Throughout the AI tool’s lifecycle, the development team should analyse potential risks, assess each risk’s likelihood, effects and
risk-benefit balance, define risk mitigation measures, monitor the risks and mitigations continuously, and maintain a risk
management file. The risks may include those explicitly covered by the FUTURE-AI guiding principles (e.g. bias, harm), but also 0) Risks regarding the AI lifecycle have not been described,
1 Implement a risk management process throughout the AI lifecycle + ++ a th p e p l i i n c s a t t r i u o c n t - i s o p n e s c , i f r i e c c e ri i s v k in s. g O in th su er f f r i i c s i k en s t t o tr a c i o n n in si g d ) e , r a i p n p c l l i u c d at e i o h n u m of a n th f e a c A to I r t s o o th l a t t o m in a d y i v le i a d d u a t l o s m w i h s o u s a e r e o n f o th t e w A it I h i t n o o t l h e (e t . a g r . g n et o t p o fo p l u lo la w ti i o n n g , 0 1 . ) 5 A ) R ri i s s k k s m r a e n g a a g rd m in e g n t t h p e la A n I h l a i s f e b c e y e c n l e d h e a sc v r e i b b e e d e n in d o es rd cr e i r b e to d , c ircumvent risks during the AI
use of the tool by others than the target end-users (e.g. technician instead of physician), hardware failure, incorrect data annotations lifecycle.
or input values, and adversarial attacks. Mitigation measures may include warnings to the users, system shutdown, re-processing
of the input data, the acquisition of new input data, or the use of an alternative procedure or human judgement only.
To increase transparency, traceability, and accountability, adequate documentation should be created and maintained for the AI
2 Provide documentation (e.g. technical, clinical) ++ ++ t r a l o i i b s m o o k l u i s , t t a w ( t e t i h h . o g e i n c . A s h b , I i m a a m n s a e d y o s d ) p i e n e a l r c n ’ i l s d o u d p d i i n r e c o s ( p t a i r e u ) u r d a c ti i n t e t i s o s A n a ( I s e n . i d f g n o . u f r o h p r u d y m s p a e t a e ; e t r i s ( p o i ; a i n ) ( r i a i l a m i e ) t a e e f a t l c e e h p r t n s u t ) i b o , c l a t i i l r c n a a d f i t o n o io i r c m n n u g m b c a i e a n t s n i d e z t d e t t n o e o s s n i t a n i n n e fo g x d r i m d s h t a e i t a n A a l g , t I h e A d c v a e I a r v l r e e u e l p p a o t o r p i o o r e t f n i e r n s s , c g s r i h i o s t e t e n a a r a l n i l t a d h s a a a o r n b d r d g o s a , u r n e t a s i n t s u h d a l e t t s ( i i t o , v o n b ) o s i l a a ’ a s s r n e i i d s s n k t r a e e n n g d d u e l o a d t t h o u e r s r s e , 0 0 1 ) . ) 5 N D ) o o D c d o u o c m u cu m en m e t n a e t n t i a t o t a i n t o i o n ab n a o b h u o a t s u 3 t b - 1 4 ee - 2 p n o p p i o n ro i t n s v t i ( s d s e e ( d s e e , d e e d s e c c ri r p ip ti t o io n n h ) a h v a e v e b e b e e n e n p r p o r v o i v d i e d d e ) d),
management file (see Traceability 1).
T 3 Define mechanisms for quality control of the AI inputs and outputs + ++ T a d b u n a e p h d t d e a p a o r A p t o u e r I v s t e p i t - d s o p u h e o r t o d o s l , c u s ( e l s a h s d u n o s c d i b u h n e l c g d a a a , s l p b i a b p e t n o r l d d a i e i t e d d e e v r d e e r t n ) o l o o t n t i o p a f e y d e o i d d u n m r s f a e o i n s o s r s d m s r i a i d n m n t e g h y p p e o l l i o r a e d y u n e o e s d n u d i - t t b u i - f l w o s i e e e f i - d r A t r s h a I l n o i m m o g n u e e i t c t t h i p h a n e t u a i p n t o d u s i n e . t s g s m F v r a e a o s n e r r i f d a o o q b f e r u l n a c c e h l o o s i , a n n t n y f i t i i n c d n c e c o e u o t n n o n h c t u e s r e s i o A s i l m t n I e o n o t m f h t n t e o h i d t d e a r o e e t r A a s l i s u n I f l g o o t d r s v a e m . e n c r F a i d s t t i s i i n q o m a u o n l e a r s l . l y , u i , t n u y w i n t c c s h o e , e r n n i t t n a r n i c o n o e l t c r y o r e e s f e c s s t t a h t r a i e y m n , A n a m o t I e t o i a s n t d i s p e o h u l n o t s s u l o d r 0 0 o 1 ) . u ) 5 t N M ) p o u M o t n m s o i n t o o i n t r i o i t n r o i g r n i g o n r g o q r o u r q a u q li a u t l y a i l t i y c t o y c n o c t n r o o t n r l t o r m l o l m e a m e s a u e s r a e u s s r u e r h s e a s h v a o e v f b e e e i b e t n e h e e n i r m i i n m p p l p e u m l t e s m n o t e e r n d o t e f u o d t r p f u b o t o r s t e h h i t a i h v n e p e r u b t t h e s e e n a i n i n m d p u p o l t u s e t m p o u e r t n s t . ed
4 Implement a system for periodic auditing and updating + ++ T d c n o a e h t n c e a e c s s A e e s p t I a s t r t y d o a n r o u i d f l p t s s d t h i , a m o t n e u e e s l l w d i t n l o y b e s t e o h f c d e o c e r A u v p r e I r l e i m o r n i p g o o e d d d b i e i c l a a s n s e e d v o s a r , d l A u e p p a e I t l r i t o f o o o y n o r e m s l d s ( a e w s n . h c g i o e t . h u d e l a e v d g e c b r r o a y e n d f y a a i p t e g i a p u o r l n r ) i a . e b o d T l r . e h c e s h y p a s n e t r g e i m o es d i f i c n o r a t u p h d e e r i i t d o i e n d c g i i c s s i a h o u o n d u m i l t d i a n k e g n i , n a g w b l h o e i f c t h t h h e e s i h d e o n e u n d l t - d i u f s i d c e e a r f s t i i . n o A e n c s o c it f o e r d - d s a i p t n a e g c o l i y r fi , c 0 0 1 ) . ) 5 N M ) o N e t d e h e i o s d d c u o s s f f s o a i u r o d a n i u t o d f o i t r a i u n p d g o i t t o e n r o t r u i a p fu l d t u a u t p r i e d n a g u t p e a s d r e a i t s d i n i d s g i c s ; u c s u s s e s d e . d;
5 Implement a logging system for usage recording + ++ T p en r o i c v o i a n u c c n y r t e - e p a r s r e e e d s t e i r r s a v s c i u e n a e g b s . i m l T it a i y n m n a e e n - r d s , e s a r p i c e c e s c o i u s f t n y a t t a t i h b s e t i i l c i d t s a y t a , a n a t d n h a v A t i s I i u s l a o a l g c is c g a e i t s n i s o g e n d s s y a s s n h te d o m u u l s d s e h d b o , e u r l e u d c s o e b r d e d t i t o m h e i p n l A s e p m I e p e c r n t e t t d e h i d e c t t u i o o s n a tr g s a e c a e n o d f t h t c e h l e i u n s A i e c I r a ’ l t s o d o m e l c a i o i s n v i o e a r n c s t t i i , m o a n e n s . d i n lo a g any 0 1 ) ) N A o s y sy st s e t m em h h as a s b b ee e n en d e d v ev is i e s d e d f o fo r r l o lo g g g g in in g g u u sa s g ag e e o o f f t h th e e A A I I t o to o o l l;
After deployment, the governance of the AI tool should be specified. In particular, the roles of risk management, periodic auditing,
6 Establish mechanisms for AI governance + ++ m f A o c a r c i A n o t u I e - n n re t a a l n a b c t i e e l d i , t y a e n r m r d o e r s s c u h p s a h e n r o i v u s i m l s d i s o b n s e h s o c h l u o e l a u d r l l d y b e b s e e p s e a t c a s i s b f i i l g e i d s n h e a e d m d , , o s i u n n g c c h o c r a l p i s n o t i r c o a i t a I i n n T g s , t e b h a o m e t a h l s t h i o n c r d a h r i e v e i a c d l e t u n h a t c l r a e a r s e n , d a A d c I m o d l i l e n e v i c s e t t l i r o v a p e to e l r r i s s a . , b F a il n i u d t r y t , h m e a a r l m n o u n o f g r a e s c i , t d u r e e r e s c r p o s o . m n p si e b n i s li a t t i i e o s n 0 1 ) ) A Th I e h r a e s i s n o a t g l o e v as e t r n 1 a n g c o e v m ern ec a h n a c n e i m sm ec ( h s a e n e i s q m ue s im tio p n le f m or e n e t x e a d m /d p e l s e c s r ) i , b ed
and support structures for patients impacted by AI errors.
0) Only 1 type of stakeholder (e.g. AI developers/departments) was present for AI development,
1 Define intended use and user requirements from an early stage ++ ++ T m ( e e x h . a p g e n e . a A r g h ie I e u n r d m s c e , e a v , a n e d l - l e A o m a p I r i n e n i r a n i s b s t t e i s r l r h a i f t o t a y o c u ) r e l . s s d ) ) , e f r n a o s g m a w g a e e n l l c l e a i a s n r i l o c y n a l s h t e a u x g m p e e , a r n t t o s f , a c e c o n t m o d r - p s u i s l th e e a r i s t n ( f m e o . a r g m y . a i p m ti a o t p i n e a n c o t t n s t , h t p h e h e u y s A s a i I g c e t i o a o n o f l s ’ ) t s h a e i n n d A te I o n t t d h o e e o d r l u r ( e e s l . e e g v a . a n e n d r t g e s o n t n a d o k - m u eh s i o e c r l s d , r e e i r q n s u t u ( ir e i e . t g m iv . e e d n n a t e t s s a s , a 0 d s 1 n t . e ) a 5 d v k M ) e e n l O h u o o o l n p t i l l m i n d y p t e e l e 1 r e n n s t s d t , w y t e a h p d e k o e r e e u w h o s p e o f e v r l s e d a e t s r n e a e r d k i n s n e t u h t w e f s o o n e e l r r r d d e e A r e e d p r I q r ( u e u d e s s i . e e r g e v e n . e m a t l A n o f e d o I p n r m t d e n A e w e v d n I a e - t s u d l , o s e d n p e v e r o e e s r l r c s i o e r n / q p i d t b u m e e e i n p d r e t a e n , e r m d t t m e a u n n e s t d n e t w c s o o ) a r s m w r e d p a q e s i u s l e p c ir d r r e i e b m i s n e e e d f n n o ; t t r O m f w o R a r a t , s A i o m d I n e u c o l r t n i i b p t e l h d e e ; AI
tool’s intended use and end-user requirements.
Based on the user requirements, the AI developers should implement interfaces to enable end- users to effectively utilise the AI
model, annotate the input data in a standardised manner, and verify the AI inputs and results. Given the high-stakes nature of 0) The AI tool has no human oversight,
2 Establish mechanisms for human-AI interactions and oversight + ++ medical AI, human oversight is essential and increasingly required by policy makers and regulators. Human-in-the-loop 1) The AI tool provides at least one interface or human-in-the-loop mechanism to involve human
mechanisms should be designed and implemented to perform specific quality checks (e.g. to flag biases, errors or implausible oversight
U 3 Provide training materials an se d s s a i c o ti n v s i ) ties (e.g. tutorials, hands-on + ++ e T m a x c o a c p t o l f e a a u r n c i n i a a t l l t i s i t t o h a ( n t e e e s . d g ) b , i . e v a t s e n u t r d t s u o i s t t r y o a ia g l o o e s f v , o e e m f r n r t d a u h n - l e u e u s A a t e h l r I s s e , t A o ( e e o x I . l a g p , m . r m e c p d l i l i i n e n c s i i t m ) c i o a i i n l n s s e s a p c w e e c r c r h e o i s e a r s n l s i i b s n a t l e n s e c d , l e a n s h n u s a a g r r s r m u y e a s . , g , a e t n e a d c n h d i n n / i o c c r r i e a t a n r s a s e i , n A c in i I t g i l z i a t e e c n r t s a iv c o y it r , i e a t s d h m e ( e d i . n g e i v . s e h t l r a a o n t p o d e r s r s s - ) o . s n h s o e u s l s d i o p n ro s) v , i d ta e k t i r n a g in i i n n t g o H 0 1 ) ) a s N Y a o e n s y training material been provided:
4 Evaluate user experience and acceptance with independent end-users + ++ T ( t d e h e o . e c g i f . u s a s i c w o e il i r n i t ’ t h s m a t s r e a e a k s t a i p i d s n e f o g c a p t c o t t t i i f o o o t n n s h , , e e x t p h e , e n e r g f d e u o - n s r u m a d s b e e a i r r n l , s i . c t a e y g e a o , n f d c t l h i p n e r i o c A d a u I l c t r o t o i o l v e l i , t s y d h . i o g T u i h t l a d e l s b e p e r t o e e f s v i t c a s i l e u s n h a c t o e y u d , l d ( i d n a i s t ls h )a o e b v r i e l e i a r t l i y f w ) y . o w T rl h h d e e t w u h s i e t a r h b t i h r l e e i p t y A re I t s e e t s o n t t o s a l t s i i h v m o e u p a l a n d c d t g s d a t t i h h v e e e r r b s e e e v h e i a d n v e d i n o -u c u e s r e o a r n s n d 0 0 1 ) . ) 5 T T ) h h T e e h A A e I I A t t I o o o t o o l l o w w l a a w s s a n e s v o e a t v lu e a v l a u a te l a d u te a d f t o e f r d o u f r o s u e r s r u e e s r x e e p r x e e p r x i e e p r n i e e c r n i e e c n b e c y b e , y m 1 u l u ti s p e l r e independent end-users.
5 Evaluate clinical utility and s b a e f n et e y fi t ( ) e.g. effectiveness, harm, cost- + ++ T t h i r h s a e h n e a i e d l m c t o A l h p i m c I n o a i i t r r c s o t e i a e o a n d o l n t r c s g ( t l h e a o i o . n n g s u i i . s h c l a a d o i t l n w i b c o t r e r n t i e h a e a ( l a v s e . t e a . d g l t u h . p a e r t r e e o A d d d u I u f c t o c e o t r d o i v i l c t i s o i t s y s c , t s l s i a i , n m f e i o c p p a a r t n l o i d m u v t e d i i d s l o i e e t c d y s a r w n a e n ) o o , d t r f k c o s f a a r l u o f t e s w h t e y e s h . ) p , a T a r w t m h i h e e n e t c o n t l i ( c i n e n o i . d c g m a i . v l p e i a e a d r v r e u l a d i a l e l u r s t a o d t ( i o i t o a h r n g e s s n p c o o u e s c f r i r i s t e f h , i n c e b t g e A s t r t t o I a e u n t r o d p o o a s u ) r l d , t s c s h o o u o m f c u c h e l a s d r a ) e s , s . h a t A h n o r d d w o / d u o i b g r t e i h f o n o n e a r f a i t l t h l s y e , f o i r t 0 0 1 (R ) . ) 5 C T T ) h h T T e e ) h . A A e I I A t t I o o o t o o l l o w w l a a w s s a n e s v o e a t v lu e a v l a u a te l a d u te a d f t o e f r d o c f r l o i c r n l i i c n c l a i ic n l a i u c l t a u i l l t i u i t l y t i i t l y a i n ty a d n a d s n a d s fe a t f s y e a t f y i e n t . y a . Randomized Control Trial
0) Data acquisiton and possible variation of the data source to the real world has not been
1 Define sources of data variation from an early stage ++ ++ A r d o a t b t a t u h s a e t c n q d e u e s s i s s i g i i t n n i o t p n h h e o a s r r e e a a , n l a n w n o o t i a n rl t v d io e . n n T t , o h a r e n y s d e s / h o m o r a u a y l d d v i n e b c r e s l u a m r d i a e a l d d e a i t f o t f a e f c r t k e h n s e . c e a s p p in li c e a q t u io ip n m -sp en ec t, i f t i e c c s h o n u ic rc a e l s f a o u f l t v o ar f i a a t i m on a c t h h i a n t e m , d a a y t a i m he p t a e c r t o g th e e n e A it I i e t s o o d l u ’s ri ng d 0 d 1 i . i ) s 5 s E c c ) u u x D s s t s s e a e e n t d a d s , , i a v c e q u re i p si o t r o t n in a g n , d i n p c o lu ss d i i b n l g e r v e a f r e i r a e t n io ce n t o o f t t h h e e l d it a e t r a a t s u o r u e r a c n e d to o t t h he er r e p a r l i m w a o ry rl d s o h u a r s c e b s e , e a n b out how
the data may vary (or does not vary) to the real world data
0) The representative of the training data to the real-world data was not evaluated;
R 2 Train with representative real-world data ++ ++ C v en a l r r i i i n a c i t h c i e i o a d n n s a s c , e c n c o i c r t o d iz u i e n n n g t s e r t a e o n d t d h i n e o t r s h e o e a u r l - r s w c t e a o s k r l o e d f h o v c l l a d i r n e i i a r c s t a i o a l n r p e r i m a d c e o t n i r c t e e i f . l i i e H k d e e l a n y t c e t t o , h e t t h r d u e e s s t t r i a g t i h n n e i p n A h g I a d s t e o a t o ( a s l s e e i e f t s R i t s o h i b s o u u t s r l a t d n i n e b e s e d s c 1 o a ) n r . e f d u a l t l a y t s h e a l t e c a t d e e d q , u a a n te a l l y y s r e e d p r a e n s d en ts the 0 1 ac . ) 5 c T o ) h r T d e h i n r e e g p r l e r y p e ; s re e s n e t n at t i a v ti e v o e f o t f h t e h t e r a t i r n ai i n n i g n g d a d ta a t t a o t o th t e h r e e a re l- a w l- o w r o ld rl d d a d ta a t w a a w s a e s v e a v lu al a u te a d te d an ; d enriched
Note "real world data" has to be data taken from a cinical setting
Evaluation studies should be implemented to evaluate the AI tool’s robustness (including stress tests and repeatability tests), by 0) The AI tool has not been evaluated against real-world data (test data),
3 Evaluate and optimise robustness against real-world variations ++ ++ c v o a n ri s a i t d io er n i s n . g D a e ll p e p n o d te in n g ti a o l n s o th u e r c r e e s s u o l f t s v , a m ria i t t i i o g n at i ( o se n e m R e o a b su u r s e tn s e s s h s o 1 u ) l , d s b u e c h i m as p l d e a m ta e - n , t e e q d u t i o p m op e t n i t m -, i s c e li n th ic e i a ro n b -, u p st a n ti e e s n s t - o a f n th d e c A en I t r m e- o re d l e a l t , e d 0 1 . ) 5 T ) h T e h A e I A t I o t o o l o h l a h s a b s e b e e n e n ev e a v lu al a u te a d te d ag a a g in ai s n t s r t e a re l- a w l- o w r o ld rl d d a d ta a t ( a t e ( s te t s d t a d ta a ) t a a ) n , d the AI tool's robustness
such as regularisation, data augmentation, data harmonisation, or domain adaptation. has been optimized (if applicable) using mitigation methods.
0) Explainibility has not been defined at the design phase,
At the design phase, it should be established if explainability is required for the AI tool. In this case, the specific requirements for 0.5) At least one of the following areas is discussed: (i) the goal of the explanations (e.g. global
1 Define the need and requirements for explainability with end-users ++ ++ e d x e p sc la ri i p n t a i b o i n li t o y f s th h e o u m ld o d b e e l ’ d s e b fi e n h e a d v i w ou it r h v r s e . p l re o s c e a n l t e a x ti p v l e a n e a x t p io er n t s o a f n e d a c e h n d A - I u s d e e r c s i , s i i o n n cl ) u , d (i i i n ) g t h ( e i) m th o e s g t o s a u l i t o a f b l t e h e a p e p x r p o l a a c n h a t f i o o r n s A ( I e .g. global d su es it c a r b ip le ti o ap n p o ro f a t c h h e f m or o d A e I l ’ e s x b p e la h i a n v a i b o i u li r t y v s a . n l d o c ( a ii l i ) e x th p e la p n o at t i e o n n ti a o l f l e i a m c i h t a A ti I o n d s e c t i o s i a o n n t ) i , c ( ip ii a ) t t e h a e n m d ost
explainability, and (iii) the potential limitations to anticipate and monitor (e.g. over-reliance of the end-users on the AI decision). monitor (e.g. over-reliance of the end-users on the AI decision).
E 1) more than one of the areas has been identified and discussed
The explainable AI methods should be evaluated, first quantitatively by using in silico methods to assess the correctness of the 0) Explainability has not been defined or not evaluated with end-users,
2 Evaluate explainability with en u d s - e u rs s ) ers (e.g. correctness, impact on + + e e x v p al l u an at a i t o io n n s s s , h t o h u e l n d q a u ls a o li t i a d t e iv nt e i l f y y w an it y h l e i n m d i - t u a s ti e o rs n s t o o f a s t s h e e s s A t I h e e x ir p l i a m n p at a i c o t n o s n ( e u . s g e . r t s h a e t y is a fa re c t c io li n n , i c c a o l n ly fi d in e c n o c h e e a r n en d t c o li r n s i e c n al s i p ti e v rf e o t r o m n an o c is e e . T or h e 0 1 . ) 5 E ) x E p x l p ai l n ai a n b a i b li i t l y it y h a h s a b s e b e e n e n ev e a v lu al a u te a d te d w i i t n h s e i n li d c - o u s O e R rs w no i t t h i n e v n o d l v u e s d e rs in i n th v e o l d v e e v d e l i o n p t m he e n d t e ( v e e . l g o . p ment
adversarial attacks, they unreasonably increase the confidence in the AI-generated results). clinical users - radiologists/clinicians, radiographers etc...)
Throughout the AI tool’s lifecycle, the AI developers should continuously engage with inter-disciplinary stakeholders, such as Was a multi-disciplinary team involved in AI development (more than 1 department)
1 Engage inter-disciplinary stakeholders throughout the AI lifecycle ++ ++ healthcare professionals, citizens, patient representatives, expert ethicists, data managers and legal experts. This interaction will 0) No
facilitate the understanding and anticipation of the needs, obstacles and pathways towards acceptance and adoption. 1) Yes
Adequate measures to ensure data privacy and security should be put in place throughout the AI lifecycle. These may include
2 Implement measures for data privacy and security ++ ++ p g p c fo a r o s i r r e v v e u p e f a d u r r c n o o l y l a t n - y e n e y c n c a m t e h s i n s a i a s e g n f a s t c e t s t i i h r e n o d e g d n e A , a t p n e k I l c d o - t h a o y c n n o m o i o l q n n e u s a n y i g e t m d s a e ( i i ( e r n t e e . y s . g d t g ) . . , . m l F t d o h a u i g l e f r i g f t c b e h i i r n a e o e l g r u n a m n s t s i c o y a a e r l t s e t t b p , a e c e r m t i t k h v w s e a f , e o c m e s y r n u , a d c n t e a h h u n t a e f c a a r s a h c y c t e b p c u a y t e l r i e s t o h u r s n s , s b ) i s a , n e n e n g d e d e a s T f t d i y a r t e s a s p p t c e r l f e o o o m a t r y b e - e i c l c l r e i t s i t v i t i o y e z s n l e h 5 n o c i ) s y m u . b l a I p d e f n a r d d i s c m e e t t c - h a p i u d s e l r e s e i r e m t n i y s s t e s i k s f n m s i o t c e l f a a u n o t n t i r t i o d o a r n e n n r - e s d i i g s d o u a e i p r n l m a p t a r i p p r l f o y l i p e c p l m e a i r t v c ia i e a a o t n t l e n i u t o e a d s n d t a h e - t s ( o a e m p u . e g l e c d . a i s f b i u c e r es H e 0 1 t ) ) a h s N Y i c d o e a s a l t c a o p m ri m va i c tt y e e a , n ( d w s a e i c v u e r d i ) t y i n b f e o e r n m d ed is c c u o s n s s e e d n t ( ) e ? .g. data anonymization, clearance from medical
defence mechanisms (e.g. attack detection or mitigation).
0) No mitigation measures to address challenges and risks identified at the design stage have
At the development stage, the development team should define an AI modelling plan that is aligned with the application-specific been reported.
requirements. After implementing and testing a baseline AI model, the AI modelling plan should include mitigation measures to 0.5) One mitigation measure (1 of F3, R2 or R3) to either enhance robusteness to real-world
3 Implement measures to address identified AI risks ++ ++ a e d n d h r a e n s c s e t r h o e b c u h s a tn ll e e s n s g t e o s r a e n a d l- w ris o k rl s d i d v e a n ri t a i t f i i o ed n s a t ( e t . h g e . d re e g s u ig la n r i s s t a a t g io e n ( , s e d e a t F a a a ir u n g e m ss e n 1 t a to ti o E n x , p d la a i t n a a h b a i r l m ity o n 1 i ) s . a T ti h o e n s , e d m om ay a i i n n c a l d u a d p e t a m ti e o a n s ) u , r e e n s s t u o r e v b a e r e i n a t t i a o k n e n o . r ensure generalisability across settings or to correct for biases across subgroups has
General g sa e m ne p ra li l n is g a , b b il i i a t s y - f a re c e ro r s e s p s re e s tt e i n n t g a s ti o (e n . , g . e q tr u a a n l s is fe e r d l o ea d r d n s i n p g o , s k t- n p o ro w c l e e s d s g in e g d ) i . stillation), and correct for biases across subgroups (e.g. data re-1 an ) d T / w or o e o n r s u m re o r g e e n m e i r t a i l g is a a t b io i n li t m y e a a c s r u o r s e s s s ( e F tt 3 i , n g R s 2 a , n R d/ 3 o ) r t c o o e rr n e h c a t n f c o e r r b o i b as u e s s t e a n c e r s o s s s t o s u re b a g l r - o w u o p r s ld h v av ar e i a b ti e o e n n
taken.
4 Define adequate evaluation m pl e a t n h o (e d . s g ) . datasets, metrics, reference ++ ++ T m s s s h e t o a e l o e n t i u h c d n l t o a c d e d r r d d e s b , a ) e p s . t a e r w F k a c t i e i r n r t l u s i l g c s t , s e t i e n a a s p d t n h a o e d o r q a u a a u t c l e d a d c d o t o e b p f u r e t t n o i e o t p s m n t e t h r , d t f e h o a a i n t r e r a m t b a s r e p e a h d n p i o n e r t u o i f o n i l p t d g s e r i n b a a t a o t e n b e d s p l e e e r p v l e c e o a v o c l t e u t e m n e n a d t p t t i i d a o f a r o a l n a t r t f a i p l a v a l l s w e e a s a n e s a k s . s s a s s h F g i e n o e i s g n . u s m a l F e d l a l u e y c b n r h , t e t h b d o e d e r i f e m n m f m c i o n e h o n r e m e d d s , i a e o ( a r l i k n d n p i e c n e o q l r g f u f u o d t a w r r t i u m e n i s t g h a e t w n v t r c a e o e e l s s r u . t t p a h d e t y c i a o t t A a n t , o I m . m r I e e n e f t t e r r p i r i c e a c s n r s t c s i a e c h n u o A d l u a I r l r e d , t f o t e b o h r e e l e s n c t c o a e e r s r e t f u d l a l t y a 0 0 e 1 s c v h o ) . ) 5 a o m E T ) l u u v h p A l a a e d a t l r i u s A e b o e a e n I t p t o i e t c o m o r o r n a o a m e t d l e t w r p i w i o t a a c e l s a r s s o e s t n d g ( e c o s i . o t s e t g o t t m s c . w s ) o p s a n a e a m d s n re u s e u d i c s t m t i t e e v o d e d i t t c r t u y u i o c s r a s i r e n n e v f n g d o a t l r s s u s t p c a t a u e a t n e c n r d r i d e t f a h i a n r c r d e t i d t i c A z y l p e ) i I r d n a t i c o a c t n o a i l c d l e t a e b n ( s e i d . t s s e t . r - e p e p s r v a o o a c r l t t f u i e o c d a r e t s i e o o , x n n a m u m s p i e n l t e r g i c h a s o p w p on r o d t p i e d r s i a t i t t s e e t
5 Identify and comply with applicable AI regulatory requirements + ++ T at h a e n d e e a v r e l l y o p st m ag e e n t t o te a a n m ti c s i h p o a u te ld r e i g d u en la t t i o fy ry t h o e b l a i p g p a l t i io ca n b s l e b a A s I e d re o g n u l t a h ti e o m ns e d d i e c p a e l n A di I n t g o o o l n ’s t h in e t e re n l d e e v d a n c t l a j s u s r i i f s i d c i a c t t i i o o n n s a . n d T h ri i s s k s s h . ould be done H 0 1 ) ) a v N Y e o e s AI regulatory requirements been identified?
In addition to the well-known ethical issues that arise in medical AI (e.g. privacy, transparency, equity, autonomy), AI developers, Have ethical issues been investigated?
6 Investigate and address ethical issues + ++ domain specialists and professional ethicists should identify, discuss and address all application-specific ethical, social and 0) No
societal issues as an integral part of the development and deployment of the AI too. 1) Yes
Social and societal implications should be considered and addressed when developing the AI tool, to ensure a positive impact on
citizens and society. Relevant issues include the impact of the AI tool on the working conditions and power relations, on the new Have social and societal implications been investigated?
7 Investigate and address social and societal issues + + skills (or deskilling) of the healthcare professionals and citizens, and on future interactions between citizens, health professionals 0) No
and social carers. Furthermore, for environmental sustainability, AI developers should consider strategies to reduce the carbon 1) Yes
footprint of the AI tool.

<!-- Page 55 -->

CLAIM Checklist

## Claim

(sub)section Criterion Explanation Values
item #
The study identifies the AI methodology, or Specify the AI techniques used in the study—such as “vision transformers” or “deep
Title or Abstract 1 specifies the category of technology used (eg. learning”—in the article’s title and/or abstract; use judgment regarding the level of 0. Not specified
deep learning). specificity. 1. Specified
The abstract should present a succinct structured summary of the study’s design,
methods, results, and conclusions. Include relevant detail about the study
population, such as data source and use of publicly available datasets, number of
patients or examinations, number of studies per data source, modalities and
relevant series or sequences. Provide information about data partitions and level of
Abstract 2 Summary of study design, methods, results, data splitting (eg, patient- or image-level). Clearly state if the study is prospective or 0. Not included
and conclusions retrospective and summarize the statistical analysis that was performed. The reader 1. Included
should clearly understand the primary outcomes and implication of the study’s
findings, including relevant clinical impact. Indicate whether the software, data,
and/or resulting model are publicly available (including where to find more details, if
applicable).
Considered as complete if at least a simple sentence was provided to
introduce the medical context and rationale for developing/validating the
model: The current practice should be explicitly mentioned. (1) Describe the 0. Not provided
3 Scientific and/or clinical background, including study’s rationale, goals, and anticipated impact. (2) resent a focused summary of 1. Provided
the intended use and role of the AI approach the pertinent literature to describe current practice and highlight how the
investigation changes or builds on that work. Guide readers to understand the
context for the study, the underlying science, the assumptions underlying the
Introduction methodology, and the nuances of the study.

## Not provided

4a Study aims and objectives Define clearly the clinical or scientific question to be answered; avoid vague 1. Provided
statements or descriptions of a process. Limit the chance of post hoc data dredging
by specifying the study’s hypothesis a priori. The study’s hypothesis and objectives
should guide appropriate statistical analyses, sample size calculations, and whether 0. Not provided
4b Study hypothesis the hypothesis will be supported or not. 1. Provided

### Methods

5 Prospective or retrospective study Indicate if the study is retrospective or prospective. Evaluate predictive models in a 0. Not documented
prospective setting, if possible. 1. Documented
Considered as complete if at least a simple sentence was provided involving
one of the points below: (1) Define the study’s goal, such as model creation,
Study Design exploratory study, feasibility study, or noninferiority trial. For classification systems, 0. Not documented
6 Study goal state the intended use, such as diagnosis, screening, staging, monitoring, 1. Documented
surveillance, prediction, or prognosis. (2) Describe the type of predictive modeling
to be performed, the target of predictions, and how it will solve the clinical or
scientific question.
7a Data source 0: Not documented
State the source(s) of data including publicly available datasets and/or synthetic 1: Documented
7b Data collection institutions images; provide links to data sources and/or images, if available. Describe how well 0. Not documented
the data align with the intended use and target population of the model. Provide 1. Documented
7c Institutional review board approval l t i o n k d s e t p o o d s a it t d a a s t o a u a rc n e d s /o a r n s d o / f o tw r a im re a g u e s s e , d i f f o a r v a m i o la d b e le lin . A g u o t r h d o a rs t a a r a e n s a t l r y o s n is g i l n y e a n p c u o b u l r ic a l g y ed 0 1 . . N D o o t c u d m oc e u n m te e d nted
7d Participant consent accessible repository. 0. Not documented

## Documented

Specify inclusion and exclusion criteria, such as location, dates, patient-care
setting, demographics (eg, age, sex, race), pertinent follow-up, and results from 0. Not provided
8 Inclusion and exclusion criteria prior tests. Define how, where, and when potentially eligible participants or studies 1. Provided
were identified. Indicate whether a consecutive, random, or convenience series was
selected.

## Not provided

9a Data pre-processing steps with details 1. Provided
9b Normalization / resampling in preprocessing 0. Not documented

## Documented

9c W lim h it e e t d h e (“ r b d in a a ta ri z h e a d v ”) e , b a e nd e / n o r r e s s t c a a n l d e a d r , d t i h z r e e d shold- D S e p s e c c r i i f b y e t h p e re u p s r e o c o e f s n s o in r g m a st li e z p a s ti o to n , a r l e lo s w a m o p th li e n r g i n o v f e im st a ig g a e t o s r i s z e to , c r h e a p n ro g d e u i c n e b t i h t e d m ep . th, 0 1 . . N D o o t c u d m oc e u n m te e d nted
and/or adjustment of window/level settings. If applicable, state whether the data
Specify how the following issues were handled: have been rescaled, threshold-limited (“binarized”), and/or standardized. Specify
9d r d e a g t i a o , n m al i s f s o in rm g a d t, a m ta a , n w u ro al n i g n p d u a t t , a in t c y o p n e s s i , s f t i e le n t p m r i o s c s e in s g s e d s a t u a s , e in d c t o o r r a e d c d t r d e a s t s a r t e y g p i e o , n f a il l e f o m rm an a i t p ti u n l g a , t io m n a s n , u a a n l d in m pu is t s , in in g c o a n n s o is n t y e m n i t z d a a tio ta n , . 0 1 . . N D o o t c u d m oc e u n m te e d nted
manipulations, and missing anonymization. State any criteria used to remove outliers. When applicable, include description for
Data libraries, software (including manufacturer name and location and version numbers),
9e Define any criteria to remove outliers and all option and configurations settings. 0. Not documented

## Documented


### Specify the libraries, software (including

9f manufacturer name and location), and version 0. Not documented
numbers, and all option and configuration 1. Documented
settings employed.
State whether investigators selected subsets of raw extracted data during
preprocessing. For example, describe whether investigators selected a subset of
the images, cropped portions of images, or extracted segments of a report. If this
10 Selection of data subsets process is automated, describe the tools and parameters used. If performed 0. Not documented
manually, describe the training of the personnel and criteria used in their 1. Documented
instruction. Justify how this manual step would be accommodated in context of the
clinical or scientific problem, describing methods of scaling processes, when
applicable.
Describe the methods used to de-identify data and how protected health
11 De-identification methods information has been removed to meet U.S. (HIPAA), EU (AI Act, EU Health Data 0. Not defined

### Space, GDPR), or other relevant regulations 1. Defined

Clearly describe how missing data were handled. For example, describe processes
12 How missing data were handled to replace them with approximate, predicted, or proxy values. Discuss biases that 0. Not defined
imputed data may introduce. 1. Defined
Describe the image acquisition protocol, such as manufacturer, MRI sequence,
13 Image acquisition protocol ultrasoundfrequency, maximum CT energy, tube current, slice thickness,scan 0. Not defined
range, and scan resolution; include all relevant parametersto enable reproducibility 1. Defined
of the stated methods.
Include a clear, detailed description of methods used to obtain the reference
standard; readers should be able to replicate the reference standard based on this
description. Include specific, standard guidelines provided to all annotators. Avoid
vague descriptions, such as “white matter lesion burden,” and use precise
14 Definition of method(s) used to obtain reference definitions, such as “lesion location (periventricular, juxtacortical, infratentorial), size 0. Not defined
standard measured in three dimensions, and number of lesions as measured on T2/FLAIR 1. Defined
MR brain images.” Provide an atlas of examples to annotators to illustrate
subjective grading schemes (eg, mild, moderate, severe) and make that information
available for review.
Describe the rationale for choice of the reference standard versus any alternatives.
15 Rationale for choosing the reference standard Include information on potential errors, biases, and limitations of that reference 0. Not documented
standard. 1. Documented
Ground Truth

<!-- Page 56 -->

Considered as complete if all points below were provided: (1) Specify the source
of reference standard annotations, citing relevant literature if annotations from
Ground Truth 16 Source of reference standard annotations existing data resources are used (2)Specify the number of human annotators and 0. Not documented
their qualifications (eg, level of expertise, subspecialty training). (3) Describe the 1. Documented
instructions and training given to annotators; include training materials as a
supplement
Detail the steps taken to annotate the test set with sufficient detail so that another
investigator could replicate the annotation. Include any standard instructions
provided to annotators for a given task. Specify software used for manual
17 Annotation of test set annotation, including the version number. Describe if and how imaging labels were 0. Not documented
extracted from imaging reports or electronic health records using natural language 1. Documented
processing or recurrent neural networks. This information should be included for
any step involving manual annotation, in addition to any semiautomated or
automated annotation.
Describe the methods to measure inter- and intra- rater variability, and any steps
18 Measurement of inter- and intrarater variability taken to reduce or mitigate this variability and/or resolve discrepancies between 0. Not documented
of features described by annotators annotators. 1. Documented
Specify how data were partitioned for training, model optimization (often termed
“tuning” or “validation”), and testing. Indicate the proportion of data in each partition
(eg, 80/10/10) and justify that selection. Indicate if there are any systematic
19 How data were assigned to partitions; specify differences between the data in each partition, and if so, why and how potential 0. Not documented
proportions class imbalance was addressed. If using openly available data, use established 1. Documented
Data Partitions splits to improve comparison to the literature. If freely sharing data, provide data
splits so that others can perform model training and testing comparably.
Describe the level at which the partitions are disjoint (eg, patient-, series-, image-
20 Level at which partitions are disjoint level). Sets of medical images generally should be disjoint at the patient level or 0. Not documented
higher so that images of the same patient do not appear in each partition. 1. Documented
Describe the size of the testing set and how it was determined. Use traditional
power calculation methods, if applicable, to estimate the required sample size. For
Testing Data 21 Intended sample size classification problems, in cases where there is no algorithm-specific sample size 0. Not documented
estimation method available, sample size can be estimated for a given area under 1. Documented
the curve and confidence interval width
If novel model architecture is used, provide a complete and detailed structure of the
model, including inputs, outputs, and all intermediate layers, in sufficient detail that
another investigator could exactly reconstruct the network. For neural network
models, include all details of pooling, normalization, regularization, and activation in
the layer descriptions. Model inputs must match the form of the preprocessed data.
22 Detailed description of model Model outputs must correspond to the requirements of the stated clinical problem, 0. Not documented
and for supervised learning should match the form of the reference standard 1. Documented
annotations. If a previously published model architecture is employed, cite a
reference that meets the preceding standards and fully describe every modification
made to the model. Cite a reference for any proprietary model described previously,
Model as well. In some cases, it may be more convenient to provide the structure of the
model in code as supplemental data.
Specify the names and version numbers of all software libraries, frameworks, and
23 Software libraries, frameworks, and packages packages. A detailed hardware description may be helpful, especially if 0. Not documented
computational performance benchmarking is a focus of the work. 1. Documented
Indicate how the parameters of the model were initialized. Describe the distribution
from which random values were drawn for randomly initialized parameters. Specify
24 Initialization of model parameters the source of the starting weights if transfer learning is employed to initialize 0. Not documented
parameters. When there is a combination of random initialization and transfer 1. Documented
learning, make it clear which portions of the model were initialized with which
strategies.
Describe the training procedures and hyperparameters in sufficient detail to enable
another investigator to replicate the experiment. To fully document training, a
manuscript should: (a) describe how training data were augmented (eg, types and
ranges of transformations for images), (b) state how convergence of training of
each model was monitored and what the criteria for stopping training were, and (c)
indicate the values that were used for every hyperparameter, including which of
these were varied between models, over what range, and using what search
strategy. For neural networks, descriptions of hyperparameters should include at
25 Details of training approach least the learning rate schedule, optimization algorithm, minibatch size, dropout 0. Not documented
rates (if any), and regularization parameters (if any). Discuss what objective function 1. Documented
was employed, why it was selected, and to what extent it matches the performance
required for the clinical or scientific use case. Define criteria used to select the best-
Training performing model. If some model parameters are frozen or restricted from
modification, for example in transfer learning, clearly indicate which parameters are
involved, the method by which they are restricted, and the portion of the training for
which the restriction applies. It may be more concise to describe these details in
code in the form of a succinct training script, particularly for neural network models
when using a standard framework.
Describe the method and metrics used to select the best-performing model among
26 Method of selecting the final model all the models trained for evaluation against the held-out test set. If more than one 0. Not documented
model was selected, justify why this was appropriate. 1. Documented
If the final algorithm involves an ensemble of models, describe each model 0. Not documented
27 Ensembling techniques comprising the ensemble in complete detail in accordance with the preceding 1. Documented
recommendations. Indicate how the outputs of the component models are
weighted and/or combined.
Describe the metrics used to assess the model’s performance and indicate how
28 Metrics of model performance they address the performance characteristics most important to the clinical or 0. Not documented
scientific problem. Compare the presented model to previously published models. 1. Documented
Considered as complete if all points below were provided: (1) Indicate the
29 Statistical measures of significance and uncertainty of the performance metrics’ values, such as with standard deviation 0. Not documented
uncertainty and/or confidence intervals. (2) Compute appropriate tests of statistical significance 1. Documented
to compare metrics. (3) Specify the statistical software, including version.
30 Robustness or sensitivity analysis Analyze the robustness or sensitivity of the model to various assumptions or initial 0. Not documented
conditions. 1. Documented
If applied, describe the methods that allow one to explain or interpret the model’s 0. Not documented / NA
31 Methods for explainability or interpretability results and provide the parameters used to generate them. Describe how any such 1. Documented
methods were validated in the current study.
Document and describe evaluation performed on internal data. If there are
Evaluation 32 Evaluation on internal data s s y e s t t a e n m d a t t i h c e d i i n ff t e e r r e n n a c l e te s s in t s t e h t e , e st x r p u l c a t i u n r e th o e f d a i n ff n e o re ta n t c io e n s, s a o n r d d a d t e a s c b r e ib tw e e th e e n a th p e p r t o ra a i c n h in g 0. Not described
taken to accommodate the differences. Document whether there is consistency in 1. Employed internal test data
performance on the training and internal test sets.
Describe the external data used to evaluate the completed algorithm. If no external
testing is performed, note and justify this limitation. If there are differences in
33 Testing on external data structure of annotations or data between the training set and the external testing 0. Not described
set, explain the differences, and describe the approach taken to accommodate the 1. Employed external test data
differences.

<!-- Page 57 -->


### Evaluation

If applicable, comply with the clinical trial registration statement from the
International Committee of Medical Journal Editors (ICMJE). ICMJE recommends
that all medical journal editors require registration of clinical trials in a public trials
34 Clinical trial registration registry at or before the time of first patient enrollment as a condition of 0. Not documented
consideration for publication. Registration of the study protocol in a clinical trial 1. Documented
registry, such as ClinicalTrials.gov or WHO Primary Registries, helps avoid
overlapping or redundant studies and allows interested parties to contact the study
coordinators.

### Results

Document the numbers of patients, examinations, or images included and excluded
35 Flow of participants or cases, using a diagram based on each of the study’s inclusion and exclusion criteria. Include a flowchart or 0. Not documented
to indicate inclusion and exclusion alternative diagram to show selection of the initial patient population and those 1. Documented
excluded for any reason.

### Data

Specify the demographic and clinical characteristics of cases in each partition and
36 Demographic and clinical characteristics of dataset. Identify sources of potential bias that may originate from differences in 0. Not documented
cases in each partition demographic or clinical characteristics, such as sex distribution, underrepresented 1. Documented
racial or ethnic groups, phenotypic variations, or differences in treatment.
Considered as complete if at least two points below were provided: (1) Report
the final model’s performance on the test partition. (2) Benchmark the performance
37 Performance metrics and measures of statistical of the AI model against current standards, such as histopathologic identification of 0. Not documented
uncertainty disease or a panel of medical experts with an explicit method to resolve 1. Documented
disagreements. (3) State the performance metrics on all data partitions and
datasets, including any demographic subgroups.
Considered as complete if at least three points below were provided: For
classification tasks, (1) include estimates of diagnostic accuracy and their precision,
such as 95% confidence intervals. (2) Apply appropriate methodology such as
receiver operating characteristic analysis and/or calibration curves. When the direct
38 Estimates of diagnostic accuracy and their calculation of confidence intervals is not possible, report non-parametric estimates 0. Not documented
Model Performance precision from bootstrap samples. (3) State which variables were shown to be predictive of 1. Documented
the response variable. (4) Identify the subpopulation(s) for which the prediction
model worked most and least effectively. (5) If applicable, recognize the presence
of class imbalance (uneven distribution across data classes within or between
datasets) and provide appropriate metrics to reflect algorithm performance
Considered as complete if at least one points below were provided: Provide
information to help understand incorrect results. (1) If the task entails classification
into two or more categories, provide a confusion matrix that shows tallies for
39 Failure analysis of incorrectly classified cases predicted versus actual categories. (2) Consider presenting examples of incorrectly 0. Not documented
classified cases to help readers better understand the strengths and limitations of 1. Documented
the algorithm. (3) Provide sufficient detail to frame incorrect results in the
appropriate medical context.
Identify the study’s limitations, including those involving the study’s methods,
materials, biases, statistical uncertainty, unexpected results, and generalizability.
40 Study limitations This discussion should follow succinct summarization of the results with appropriate 0. Not discussed
context and explanation of how the current work advances our knowledge and the 1. Discussed
state of the art.
Discussion Considered as complete if at least three points below were provided: (1)
Describe the implications for practice, including the intended use and possible
41 Implications for practice, including the intended clinical role of the AI model. (2) Describe the key impact the work may have on the 0. Not discussed
use and/or clinical role field. (3) Envision the next steps that one might take to build upon the results. (4) 1. Discussed
Discuss any issues that would impede successful translation of the model into
practice.
State where readers can access the full study protocol or additional technical
details if this description exceeds the journal’s word limit. For clinical trials, include
reference to the study protocol text referenced in item 34. For experimental or 0. Not access to the full study protocol
42 Provide a reference to the full study protocol or preclinical studies, include reference to details of the AI methodology, if not fully 1. Provided access to the full study
to additional technical details documented in the manuscript or supplemental material. This information can help protocol
readers evaluate the validity of the study and can help researchers who want to
replicate the study.
Other information State where the reader can access the software, model, and/or data associated
with the study, includingconditions under which these resources can be accessed. 0. Not discussed
43 Statement about the availability of software, Describe the algorithms and software in sufficient detail to allowreplication of the 1. Discussed
trained model, and/or data study. Authors should deposit all computercode used for modeling and/or data
analysis into a publiclyaccessible repository.
Specify the sources of funding and other support and the exact role of the funders
44 Sources of funding and other support; role of in performing the study. Indicate whether the authors had independence in each 0. Not documented
funders phase of the study. 1. Documented

<!-- Page 58 -->


### Appendix 3


## Alabdulkreem E, Saeed MK, Alotaibi SS, Allafi R, Mohamed A, Hamza MA. Bone Cancer Detection

and Classification Using Owl Search Algorithm With Deep Learning on X-Ray Images. Ieee Access 2023;
11: 109095-103.

## Alaoui EA, Tekouabou SCK, Hartini S, Rustam Z, Silkan H, Agoujil S. Improvement in Automated

Diagnosis of Soft Tissues Tumors Using Machine Learning. Big Data Min Anal 2021; 4(1): 33-46.

## Alge O, Lu L, Li Z, Hua Y, Gryak J, Najarian K. Automated Classification of Osteosarcoma and

Benign Tumors using RNA-seq and Plain X-ray. Annu Int Conf IEEE Eng Med Biol Soc 2020; 2020: 1165-8.

## Altameem T. Fuzzy rank correlation-based segmentation method and deep neural network for

bone cancer identification. Neural Computing and Applications 2020.

## Amini B, Chenglei L, Duran-Sierra E, Wang WL, Canjirathinkal MA, Moradi H, et al. Role of

Apparent Diffusion Coefficient Map-Based First- and High-Order Radiomic Features for the
Discrimination of Sacral Chordomas and Chondrosarcomas With Overlapping Conventional Imaging
Features. JCO precis oncol 2023; 7: e2300243.

## Ao W, Cheng G, Lin B, Yang R, Liu X, Zhou C, et al. A novel CT-based radiomic nomogram for

predicting the recurrence and metastasis of gastric stromal tumors. Am J Cancer Res 2021; 11(6): 3123-
34.

## Arthur A, Orton MR, Emsley R, Vit S, Kelly-Morland C, Strauss D, et al. A CT-based radiomics

classification model for the prediction of histological type and tumour grade in retroperitoneal sarcoma
(RADSARC-R): a retrospective multicohort analysis. Lancet Oncol 2023; 24(11): 1277-86.

## Ba-Ssalamah A, Muin D, Schernthaner R, Kulinna-Cosentini C, Bastati N, Stift J, et al. Texturebased classification of different gastric tumors at contrast-enhanced CT. Eur J Radiol 2013; 82(10): e537-

43.

## Bandyopadhyay O, Biswas A, Bhattacharya BB. Bone-Cancer Assessment and Destruction Pattern

Analysis in Long-Bone X-ray Image. J Digit Imaging 2019; 32(2): 300-13.

## Banerjee I, Crawley A, Bhethanabotla M, Daldrup-Link HE, Rubin DL. Transfer learning on fused

multiparametric MR images for classifying histopathological subtypes of rhabdomyosarcoma. Comput
Med Imaging Graph 2018; 65: 167-75.

## Baskaran K, Malathi R, Thirusakthimurugan P. Feature Fusion for FDG-PET and MRI for

Automated Extra Skeletal Bone Sarcoma Classification. Mater Today-Proc 2018; 5(1): 1879-89.

## Blackledge MD, Winfield JM, Miah A, Strauss D, Thway K, Morgan VA, et al. Supervised Machine-

Learning Enables Segmentation and Evaluation of Heterogeneous Post-treatment Changes in Multi-
Parametric MRI of Soft-Tissue Sarcoma. Front oncol 2019; 9: 941.

## Bouhamama A, Leporq B, Khaled W, Nemeth A, Brahmi M, Dufau J, et al. Prediction of Histologic

Neoadjuvant Chemotherapy Response in Osteosarcoma Using Pretherapeutic MRI Radiomics. Radiol
Imaging Cancer 2022; 4(5): e210107.

<!-- Page 59 -->


## Breden S, Hinterwimmer F, Consalvo S, Neumann J, Knebel C, von Eisenhart-Rothe R, et al. Deep

Learning-Based Detection of Bone Tumors around the Knee in X-rays of Children. J Clin Med 2023; 12(18).

## Cao C, Yi Z, Xie M, Xie Y, Tang X, Tu B, et al. Machine learning-based radiomics analysis for

predicting local recurrence of primary dermatofibrosarcoma protuberans after surgical treatment.
Radiother Oncol 2023; 186: 109737.

## Cao Y, Wang Z, Ren J, Liu W, Da H, Yang X, Bao H. Differentiation of retroperitoneal

paragangliomas and schwannomas based on computed tomography radiomics. Sci rep 2023; 13(1): 9253.

## Cappello G, Giannini V, Cannella R, Tabone E, Ambrosini I, Molea F, et al. A mutation-based

radiomics signature predicts response to imatinib in Gastrointestinal Stromal Tumors (GIST). Eur J Radiol
Open 2023; 11: 100505.

## Casale R, De Angelis R, Coquelet N, Mokhtari A, Bali MA. The Impact of Edema on MRI Radiomics

for the Prediction of Lung Metastasis in Soft Tissue Sarcoma. Diagnostics 2023; 13(19).

## Casale R, Varriano G, Santone A, Messina C, Casale C, Gitto S, et al. Predicting risk of metastases

and recurrence in soft-tissue sarcomas via Radiomics and Formal Methods. Jamia Open 2023; 6(2):
ooad025.

## Cay N, Mendi BAR, Batur H, Erdogan F. Discrimination of lipoma from atypical lipomatous

tumor/well-differentiated liposarcoma using magnetic resonance imaging radiomics combined with
machine learning. Jpn J Radiol 2022; 40(9): 951-60.

## Chen CY, Chiou HJ, Chou SY, Chiou SY, Wang HK, Chou YH, Chiang HK. Computer-aided diagnosis

of soft-tissue tumors using sonographic morphologic and texture features. Acad Radiol 2009; 16(12):
1531-8.

## Chen G, Fan L, Liu J, Wu S. Machine learning-based predictive model for the differential diagnosis

of <= 5 cm gastric stromal tumor and gastric schwannoma based on CT images. Discov Oncol 2023; 14(1):
186.

## Chen H, Liu J, Cheng Z, Lu X, Wang X, Lu M, et al. Development and external validation of an MRI-

based radiomics nomogram for pretreatment prediction for early relapse in osteosarcoma: A
retrospective multicenter study. Eur J Radiol 2020; 129: 109066.

## Chen H, Zhang X, Wang X, Quan X, Deng Y, Lu M, et al. MRI-based radiomics signature for

pretreatment prediction of pathological response to neoadjuvant chemotherapy in osteosarcoma: a
multicenter study. Eur Radiol 2021; 31(10): 7913-24.

## Chen S, Li N, Tang Y, Chen B, Fang H, Qi S, et al. Radiomics Analysis of Fat Saturated T2-Weighted

MRI Sequences for Prognostic Prediction to Soft-Tissue Sarcoma of the Extremities and Trunk Treated
With Neoadjuvant Radiotherapy. Int J Radiat Oncol Biol Phys 2021; 111(3): e315.

## Chen T, Liu S, Li Y, Feng X, Xiong W, Zhao X, et al. Developed and validated a prognostic

nomogram for recurrence-free survival after complete surgical resection of local primary gastrointestinal
stromal tumors based on deep learning. EBioMedicine 2019; 39: 272-9.

<!-- Page 60 -->


## Chen T, Ning Z, Xu L, Feng X, Han S, Roth HR, et al. Radiomics nomogram for predicting the

malignant potential of gastrointestinal stromal tumours preoperatively. Eur Radiol 2019; 29(3): 1074-82.

## Chen W, Ayoub M, Liao M, Shi R, Zhang M, Su F, et al. A fusion of VGG-16 and ViT models for

improving bone tumor classification in computed tomography. J Bone Oncol 2023; 43: 100508.

## Chen X, Huang Y, He L, Zhang T, Zhang L, Ding H. CT-Based Radiomics to Differentiate Pelvic

Rhabdomyosarcoma From Yolk Sac Tumors in Children. Front oncol 2020; 10: 584272.

## Chen Z, Xu L, Zhang C, Huang C, Wang M, Feng Z, Xiong Y. CT Radiomics Model for Discriminating

the Risk Stratification of Gastrointestinal Stromal Tumors: A Multi-Class Classification and Multi-Center
Study. Front oncol 2021; 11: 654114.

## Cheng Y, Yang L, Wang Y, Kuang L, Pan X, Chen L, et al. Development and validation of a radiomics

model based on T2-weighted imaging for predicting the efficacy of high intensity focused ultrasound
ablation in uterine fibroids. Quant Imaging Med Surg 2024; 14(2): 1803-19.

## Chianca V, Cuocolo R, Gitto S, Albano D, Merli I, Badalyan J, et al. Radiomic Machine Learning

Classifiers in Spine Bone Tumors: A Multi-Software, Multi-Scanner Study. Eur J Radiol 2021; 137: 109586.

## Chiappa V, Interlenghi M, Salvatore C, Bertolina F, Bogani G, Ditto A, et al. Using rADioMIcs and

machine learning with ultrasonography for the differential diagnosis of myometRiAL tumors (the
ADMIRAL pilot study). Radiomics and differential diagnosis of myometrial tumors. Gynecol Oncol 2021;
161(3): 838-44.

## Chiou HJ, Chen CY, Liu TC, Chiou SY, Wang HK, Chou YH, Chiang HK. Computer-aided diagnosis of

peripheral soft tissue masses based on ultrasound imaging. Comput Med Imaging Graph 2009; 33(5):
408-13.

## Chu H, Pang P, He J, Zhang D, Zhang M, Qiu Y, et al. Value of radiomics model based on enhanced

computed tomography in risk grade prediction of gastrointestinal stromal tumors. Sci rep 2021; 11(1):
12009.

## Cilengir AH, Evrimler S, Serel TA, Uluc E, Tosun O. The diagnostic value of magnetic resonance

imaging-based texture analysis in differentiating enchondroma and chondrosarcoma. Skeletal Radiol
2023; 52(5): 1039-49.

## Consalvo S, Hinterwimmer F, Neumann J, Steinborn M, Salzmann M, Seidl F, et al. Two-Phase

Deep Learning Algorithm for Detection and Differentiation of Ewing Sarcoma and Acute Osteomyelitis in
Paediatric Radiographs. Anticancer Res 2022; 42(9): 4371-80.

## Corino VDA, Montin E, Messina A, Casali PG, Gronchi A, Marchiano A, Mainardi LT. Radiomic

analysis of soft tissues sarcomas can distinguish intermediate from high-grade lesions. J Magn Reson
Imaging 2018; 47(3): 829-40.

## Crombe A, Fadli D, Buy X, Italiano A, Saut O, Kind M. High-Grade Soft-Tissue Sarcomas: Can

Optimizing Dynamic Contrast-Enhanced MRI Postprocessing Improve Prognostic Radiomics Models? J
Magn Reson Imaging 2020; 52(1): 282-97.

<!-- Page 61 -->


## Crombe A, Lucchesi C, Bertolo F, Kind M, Spalato-Ceruso M, Toulmonde M, et al. Integration of

pre-treatment computational radiomics, deep radiomics, and transcriptomics enhances soft-tissue
sarcoma patient prognosis. NPJ Precis Oncol 2024; 8(1): 129.

## Crombe A, Perier C, Kind M, De Senneville BD, Le Loarer F, Italiano A, et al. T2 -based MRI Deltaradiomics improve response prediction in soft-tissue sarcomas treated by neoadjuvant chemotherapy. J

Magn Reson Imaging 2019; 50(2): 497-510.

## Dai M, Liu Y, Hu Y, Li G, Zhang J, Xiao Z, Lv F. Combining multiparametric MRI features-based

transfer learning and clinical parameters: application of machine learning for the differentiation of
uterine sarcomas from atypical leiomyomas. Eur Radiol 2022; 32(11): 7988-97.

## Dai Y, Yin P, Mao N, Sun C, Wu J, Cheng G, Hong N. Differentiation of Pelvic Osteosarcoma and

Ewing Sarcoma Using Radiomic Analysis Based on T2-Weighted Images and Contrast-Enhanced T1-
Weighted Images. Biomed Res Int 2020; 2020: 9078603.

## Deng J, Zeng W, Shi Y, Kong W, Guo S. Fusion of FDG-PET Image and Clinical Features for

Prediction of Lung Metastasis in Soft Tissue Sarcomas. Comput math methods med 2020; 2020: 8153295.

## Deng KH, Wang B, Ma SS, Xue Z, Cao XH. A Bone Lesion Identification Network (BLIN) in CT

Images with Weakly Supervised Learning. 2024; 14349: 243-52.

## Ding Y, Wang Z, Xu P, Ma Y, Yao W, Li K, Gong Y. MRI-based radiomics in distinguishing Kaposiform

hemangioendothelioma (KHE) and fibro-adipose vascular anomaly (FAVA) in extremities: A preliminary
retrospective study. J Pediatr Surg 2022; 57(7): 1228-34.

## Djuricic GJ, Ahammer H, Rajkovic S, Kovac JD, Milosevic Z, Sopta JP, Radulovic M. Directionally

Sensitive Fractal Radiomics Compatible With Irregularly Shaped Magnetic Resonance Tumor Regions of
Interest: Association With Osteosarcoma Chemoresistance. J Magn Reson Imaging 2023; 57(1): 248-58.

## Do BH, Langlotz C, Beaulieu CF. Bone Tumor Diagnosis Using a Naïve Bayesian Model of

Demographic and Radiographic Features. J Digit Imaging 2017; 30(5): 640-7.

## Do NT, Jung ST, Yang HJ, Kim SH. Multi-level seg-unet model with global and patch-based x-ray

images for knee bone tumor detection. Diagn 2021; 11(4).

## Dong J, Yu M, Miao Y, Shen H, Sui Y, Liu Y, et al. Differential Diagnosis of Solitary Fibrous

Tumor/Hemangiopericytoma and Angiomatous Meningioma Using Three-Dimensional Magnetic
Resonance Imaging Texture Feature Model. Biomed Res Int 2020; 2020: 5042356.

## Dong Z, Zhao X, Zheng H, Zheng H, Chen D, Cao J, et al. Efficacy of real-time artificial intelligenceaid endoscopic ultrasonography diagnostic system in discriminating gastrointestinal stromal tumors and

leiomyomas: a multicenter diagnostic study. EClinicalMedicine 2024; 73: 102656.

## Dou Y, Li X, Tao J, Dong Y, Xu N, Wang S. Prediction of high-grade soft-tissue sarcoma using a

combined intratumoural and peritumoural MRI-based radiomics nomogram. Clin Radiol 2023; 78(12):
e1032-e40.

## Erdem F, Tamsel I, Demirpolat G. The use of radiomics and machine learning for the

differentiation of chondrosarcoma from enchondroma. J Clin Ultrasound 2023; 51(6): 1027-35.

<!-- Page 62 -->


## Escobars T, Vauclin S, Orlhac F, Nioche C, Pineau P, Buvat I. An original voxel-wise supervised

analysis of tumors with multimodal radiomics to highlight predictive biologicalpatterns. J Nucl Med 2021;

## 62(Suppl 1).


## Eweje FR, Bao B, Wu J, Dalal D, Liao WH, He Y, et al. Deep Learning for Classification of Bone

Lesions on Routine MRI. EBioMedicine 2021; 68: 103402.

## Fadli D, Kind M, Michot A, Le Loarer F, Crombe A. Natural Changes in Radiological and Radiomics

Features on MRIs of Soft-Tissue Sarcomas Naive of Treatment: Correlations With Histology and Patients'
Outcomes. J Magn Reson Imaging 2022; 56(1): 77-96.

## Fan L, Gong X, Zheng C, Li J. Data pyramid structure for optimizing EUS-based GISTs diagnosis in

multi-center analysis with missing label. Comput Biol Med 2024; 169.

## Fares R, Atlan LD, Druckmann I, Factor S, Gortzak Y, Segal O, et al. Imaging-Based Deep Learning

for Predicting Desmoid Tumor Progression. J Imaging 2024; 10(5).

## Farhidzadeh H, Goldgof DB, Hall LO, Scott JG, Gatenby RA, Gillies RJ, Raghavan M. A Quantitative

Histogram-based Approach to Predict Treatment Outcome for Soft Tissue Sarcomas Using Pre- and Posttreatment MRIs. 2016: 4549-54.

## Feng N, Chen HY, Wang XJ, Lu YF, Zhou JP, Zhou QM, et al. A CT-based nomogram established for

differentiating gastrointestinal heterotopic pancreas from gastrointestinal stromal tumor: compared with
a machine-learning model. BMC med imaging 2023; 23(1): 131.

## Feng Q, Tang B, Zhang Y, Liu X. Prediction of the Ki-67 expression level and prognosis of

gastrointestinal stromal tumors based on CT radiomics nomogram. Int j comput assist radiol surg 2022;
17(6): 1167-75.

## Fichera G, Giraudo C, Stramare R, Bisogno G, Motta R, Evangelista L, et al. Radiomic features as

biomarkers of soft tissue paediatric sarcomas: results of a PET/MR study. Insights Imaging 2022; 14: 112.

## Fields BKK, Demirjian NL, Cen SY, Varghese BA, Hwang DH, Lei X, et al. Predicting Soft Tissue

Sarcoma Response to Neoadjuvant Chemotherapy Using an MRI-Based Delta-Radiomics Approach. Mol
Imaging Biol 2023; 25(4): 776-87.

## Fields BKK, Demirjian NL, Hwang DH, Varghese BA, Cen SY, Lei X, et al. Whole-tumor 3D

volumetric MRI-based radiomics approach for distinguishing between benign and malignant soft tissue
tumors. Eur Radiol 2021; 31(11): 8522-35.

## Findlay MC, Yost S, Bauer SZ, Cole KL, Henson JC, Lucke-Wold B, et al. Application of Radiomics to

the Differential Diagnosis of Temporal Bone Skull Base Lesions: A Pilot Study. World Neurosurg 2023;
172: e540-e54.

## Foreman SC, Llorián-Salvador O, David DE, Rösner VKN, Rischewski JF, Feuerriegel GC, et al.

Development and Evaluation of MR-Based Radiogenomic Models to Differentiate Atypical Lipomatous
Tumors from Lipomas. Cancers (Basel) 2023; 15(7).

<!-- Page 63 -->


## Fradet G, Ayde R, Bottois H, El Harchaoui M, Khaled W, Drape JL, et al. Prediction of lipomatous

soft tissue malignancy on MRI: comparison between machine learning applied to radiomics and deep
learning. Eur Radiol Exp 2022; 6(1): 41.

## Gao Y, Ghodrati V, Kalbasi A, Fu J, Ruan D, Cao M, et al. Prediction of soft tissue sarcoma

response to radiotherapy using longitudinal diffusion MRI and a deep neural network with generative
adversarial network-based data augmentation. Med Phys 2021; 48(6): 3262-372.

## Gao Y, Kalbasi A, Hsu W, Ruan D, Fu J, Shao J, et al. Treatment effect prediction for sarcoma

patients treated with preoperative radiotherapy using radiomics features from longitudinal diffusionweighted MRIs. Phys Med Biol 2020; 65(17): 175006.

## Gawade S, Bhansali A, Patil K, Shaikh D. Application of the convolutional neural networks and

supervised deep-learning methods for osteosarcoma bone cancer detection. Healthc Anal 2023; 3.

## George A, Ayshwarya B. Adaptive FLAME based segmentation and classification for bone cancer

detection. … Conference on Artificial Intelligence … 2023.

## Georgeanu V, Mamuleanu ML. Convolutional neural networks for automated detection and

classification of bone tumors in magnetic resonance imaging. … on Artificial Intelligence … 2021.

## Georgeanu VA, Mămuleanu M, Ghiea S, Selișteanu D. Malignant Bone Tumors Diagnosis Using

Magnetic Resonance Imaging Based on Deep Learning Algorithms. Medicina (Kaunas) 2022; 58(5).

## Gitto S, Annovazzi A, Nulle K, Interlenghi M, Salvatore C, Anelli V, et al. X-rays radiomics-based

machine learning classification of atypical cartilaginous tumour and high-grade chondrosarcoma of long
bones. EBioMedicine 2024; 101: 105018.

## Gitto S, Bologna M, Corino VDA, Emili I, Albano D, Messina C, et al. Diffusion-weighted MRI

radiomics of spine bone tumors: feature stability and machine learning-based classification performance.
Radiol Med (Torino) 2022; 127(5): 518-25.

## Gitto S, Corino VDA, Annovazzi A, Milazzo Machado E, Bologna M, Marzorati L, et al. 3D vs. 2D

MRI radiomics in skeletal Ewing sarcoma: Feature reproducibility and preliminary machine learning
analysis on neoadjuvant chemotherapy response prediction. Front oncol 2022; 12: 1016123.

## Gitto S, Cuocolo R, Albano D, Chianca V, Messina C, Gambino A, et al. MRI radiomics-based

machine-learning classification of bone chondrosarcoma. Eur J Radiol 2020; 128: 109043.

## Gitto S, Cuocolo R, Annovazzi A, Anelli V, Acquasanta M, Cincotta A, et al. CT radiomics-based

machine learning classification of atypical cartilaginous tumours and appendicular chondrosarcomas.
EBioMedicine 2021; 68: 103407.

## Gitto S, Cuocolo R, van Langevelde K, van de Sande MAJ, Parafioriti A, Luzzati A, et al. MRI

radiomics-based machine learning classification of atypical cartilaginous tumour and grade II
chondrosarcoma of long bones. EBioMedicine 2022; 75: 103757.

## Gitto S, Interlenghi M, Cuocolo R, Salvatore C, Giannetta V, Badalyan J, et al. MRI radiomicsbased machine learning for classification of deep-seated lipoma and atypical lipomatous tumor of the

extremities. Radiol Med (Torino) 2023; 128(8): 989-98.

<!-- Page 64 -->


## Gruber L, Gruber H, Luger AK, Glodny B, Henninger B, Loizides A. Diagnostic hierarchy of

radiological features in soft tissue tumours and proposition of a simple diagnostic algorithm to estimate
malignant potential of an unknown mass. Eur J Radiol 2017; 95: 102-10.

## Grueneisen J, Schaarschmidt B, Demircioglu A, Chodyla M, Martin O, Bertram S, et al. (18)F-FDG

PET/MRI for Therapy Response Assessment of Isolated Limb Perfusion in Patients with Soft-Tissue
Sarcomas. J Nucl Med 2019; 60(11): 1537-42.

## Guo C, Zhou H, Chen X, Feng Z. Computed tomography texture-based models for predicting KIT

exon 11 mutation of gastrointestinal stromal tumors. Heliyon 2023; 9(10): e20983.

## Guo J, Li YM, Guo H, Hao DP, Xu JX, Huang CC, et al. Parallel CNN-Deep Learning Clinical-Imaging

Signature for Assessing Pathologic Grade and Prognosis of Soft Tissue Sarcoma Patients. J Magn Reson
Imaging 2024.

## Hajianfar G, Sabouri M, Salimi Y, Amini M, Bagheri S, Jenabi E, et al. Artificial intelligence-based

analysis of whole-body bone scintigraphy: The quest for the optimal deep learning algorithm and
comparison with human observer performance. Z Med Phys 2024; 34(2): 242-57.

## Hao J, Liu S, Wang T, Han X, Gao A, Wang H, Hao D. Differentiation of malignant from benign soft

tissue tumors using radiomics based on pharmacokinetic parameter maps obtained from dynamic
contrast-enhanced magnetic resonance imaging data. Chin J Acad Radiol 2024.

## He F, Xie L, Sun X, Xu J, Li Y, Liu R, et al. A Scoring System for Predicting Neoadjuvant

Chemotherapy Response in Primary High-Grade Bone Sarcomas: A Multicenter Study. Orthop Surg 2022;
14(10): 2499-509.

## He J, Bi X. Automatic classification of spinal osteosarcoma and giant cell tumor of bone using

optimized DenseNet. J Bone Oncol 2024; 46: 100606.

## He Q, Bano S, Liu J, Liu W, Stoyanov D, Zuo S. Query2: Query over queries for improving

gastrointestinal stromal tumour detection in an endoscopic ultrasound. Comput Biol Med 2023; 152:
106424.

## He Y, Guo J, Ding X, van Ooijen PMA, Zhang Y, Chen A, et al. Convolutional neural network to

predict the local recurrence of giant cell tumor of bone after curettage based on pre-surgery magnetic
resonance images. Eur Radiol 2019; 29(10): 5441-51.

## He Y, Pan I, Bao B, Halsey K, Chang M, Liu H, et al. Deep learning-based classification of primary

bone tumors on radiographs: A preliminary study. EBioMedicine 2020; 62.

## Hermessi H, Mourali O, Zagrouba E. Deep feature learning for soft tissue sarcoma classification in

MR images via transfer learning. Expert Syst Appl 2019; 120: 116-27.

## Hu P, Chen L, Zhou Z. Machine Learning in the Differentiation of Soft Tissue Neoplasms:

Comparison of Fat-Suppressed T2WI and Apparent Diffusion Coefficient (ADC) Features-Based Models. J
Digit Imaging 2021; 34(5): 1146-55.

<!-- Page 65 -->


## Hu Y, Tang J, Zhao SH, Li Y. Diffusion-Weighted Imaging-Magnetic Resonance Imaging Information

under Class-Structured Deep Convolutional Neural Network Algorithm in the Prognostic Chemotherapy
of Osteosarcoma. Sci Program 2021; 2021.

## Hu Y, Wang H, Yue Z, Wang X, Wang Y, Luo Y, Jiang W. A contrast-enhanced MRI-based nomogram

to identify lung metastasis in soft-tissue sarcoma: A multi-centre study. Med Phys 2023; 50(5): 2961-70.

## Hu Z, Liang H, Zhao H, Hou F, Hao D, Ji Q, et al. Preoperative contrast-enhanced CT-based

radiomics signature for predicting hypoxia-inducible factor 1alpha expression in retroperitoneal sarcoma.
Clin Radiol 2023; 78(8): e543-e51.

## Huang B, Wang J, Sun M, Chen X, Xu D, Li ZP, et al. Feasibility of multi-parametric magnetic

resonance imaging combined with machine learning in the assessment of necrosis of osteosarcoma after
neoadjuvant chemotherapy: a preliminary study. BMC Cancer 2020; 20(1): 322.

## Iwai T, Kida M, Okuwaki K, Watanabe M, Adachi K, Ishizaki J, et al. Deep learning analysis for

differential diagnosis and risk classification of gastrointestinal tumors. Scand J Gastroenterol 2024: 1-8.

## Jansma C, Wan X, Acem I, Spaanderman DJ, Visser JJ, Hanff D, et al. Preoperative Classification of

Peripheral Nerve Sheath Tumors on MRI Using Radiomics. Cancers (Basel) 2024; 16(11).

## Jayachandran JJB, Ambigapathy S. X-Ray Image Analysis in Identification of Bone Cancer Using

Laws Features and Machine Learning Model. … Artificial Intelligence … 2022.

## Jeong SY, Kim W, Byun BH, Kong CB, Song WS, Lim I, et al. Prediction of Chemotherapy Response

of Osteosarcoma Using Baseline 18F-FDG Textural Features Machine Learning Approaches with PCA.
Contrast Media Mol Imaging 2019; 2019: 3515080.

## Ji X, Shang Y, Tan L, Hu Y, Liu J, Song L, et al. Prediction of High-Risk Gastrointestinal Stromal

Tumor Recurrence Based on Delta-CT Radiomics Modeling: A 3-Year Follow-up Study After Surgery. Clin
Med Insights Oncol 2024; 18: 11795549241245698.

## Jia X, Wan L, Chen X, Ji W, Huang S, Qi Y, et al. Risk stratification for 1- to 2-cm gastric

gastrointestinal stromal tumors: visual assessment of CT and EUS high-risk features versus CT radiomics
analysis. Eur Radiol 2023; 33(4): 2768-78.

## Joo DC, Kim GH, Lee MW, Lee BE, Kim JW, Kim KB. Artificial Intelligence-Based Diagnosis of

Gastric Mesenchymal Tumors Using Digital Endosonography Image Analysis. J Clin Med 2024; 13(13).

## Juntu J, Sijbers J, De Backer S, Rajan J, Van Dyck D. Machine learning study of several classifiers

trained with texture analysis features to differentiate benign from malignant soft-tissue tumors in T1-
MRI images. J Magn Reson Imaging 2010; 31(3): 680-9.

## Kang B, Yuan X, Wang H, Qin S, Song X, Yu X, et al. Preoperative CT-Based Deep Learning Model

for Predicting Risk Stratification in Patients With Gastrointestinal Stromal Tumors. Front oncol 2021; 11:
750875.

## Kim BC, Kim J, Kim K, Byun BH, Lim I, Kong CB, et al. Preliminary Radiogenomic Evidence for the

Prediction of Metastasis and Chemotherapy Response in Pediatric Patients with Osteosarcoma Using
(18)F-FDF PET/CT, EZRIN and KI67. Cancers (Basel) 2021; 13(11).

<!-- Page 66 -->


## Kim H, Rha SE, Shin YR, Kim EH, Park SY, Lee SL, et al. Differentiating Uterine Sarcoma From

Atypical Leiomyoma on Preoperative Magnetic Resonance Imaging Using Logistic Regression Classifier:
Added Value of Diffusion-Weighted Imaging-Based Quantitative Parameters. Korean J Radiol 2024; 25(1):
43-54.

## Kim J, Jeong SY, Kim BC, Byun BH, Lim I, Kong CB, et al. Prediction of Neoadjuvant Chemotherapy

Response in Osteosarcoma Using Convolutional Neural Network of Tumor Center (18)F-FDG PET Images.
Diagnostics (Basel) 2021; 11(11).

## Kim W, Park J, Sheen H, Byun BH, Lim I, Kong CB, et al. Development of deep learning model for

prediction of chemotherapy response using PET images and radiomics features. 2018.

## Kim YH, Kim GH, Kim KB, Lee MW, Lee BE, Baek DH, et al. Application of A Convolutional Neural

Network in The Diagnosis of Gastric Mesenchymal Tumors on Endoscopic Ultrasonography Images. J Clin
Med 2020; 9(10).

## Kumar R, Suhas MV. Classification of Benign and Malignant bone lesions on CT ImagesUsing

Support Vector Machine: A Comparison of Kernel Functions. 2016: 821-4.

## Kumar VDA. Bone Cancer Detection Using Feature Extraction with Classification Using K-Nearest

Neighbor and Decision Tree Algorithm. Smart Intelligent Computing and Communication … 2021.

## Lee S, Jung JY, Nam Y, Jung CK, Lee SY, Lee J, et al. Diagnosis of Marginal Infiltration in Soft Tissue

Sarcoma by Radiomics Approach Using T2-Weighted Dixon Sequence. J Magn Reson Imaging 2023;
57(3): 752-60.

## Lee S, Lee SY, Jung JY, Nam Y, Jeon HJ, Jung CK, et al. Ensemble learning-based radiomics with

multi-sequence magnetic resonance imaging for benign and malignant soft tissue tumor differentiation.
PLoS ONE 2023; 18(5): e0286417.

## Lee SE, Jung JY, Nam Y, Lee SY, Park H, Shin SH, et al. Radiomics of diffusion-weighted MRI

compared to conventional measurement of apparent diffusion-coefficient for differentiation between
benign and malignant soft tissue tumors. Sci rep 2021; 11(1): 15276.

## Leporq B, Bouhamama A, Pilleul F, Lame F, Bihane C, Sdika M, et al. MRI-based radiomics to

predict lipomatous soft tissue tumors malignancy: a pilot study. Cancer Imaging 2020; 20(1): 78.

## Li A, Hu Y, Cui XW, Ye XH, Peng XJ, Lv WZ, Zhao CK. Predicting the malignancy of extremity softtissue tumors by an ultrasound-based radiomics signature. Acta Radiol 2024; 65(5): 470-81.


## Li J, Li S, Li X, Miao S, Dong C, Gao C, et al. Primary bone tumor detection and classification in

full-field bone radiographs via YOLO deep learning model. Eur Radiol 2023; 33(6): 4237-48.

## Li L, Wang K, Ma X, Liu Z, Wang S, Du J, et al. Radiomic analysis of multiparametric magnetic

resonance imaging for differentiating skull base chordoma and chondrosarcoma. Eur J Radiol 2019; 118:
81-7.

## Li Q, Wang N, Wang Y, Li X, Su Q, Zhang J, et al. Intratumoral and peritumoral CT radiomics in

predicting prognosis in patients with chondrosarcoma: a multicenter study. Insights imaging 2024; 15(1):
9.

<!-- Page 67 -->


## Li X, Jiang F, Guo Y, Jin Z, Wang Y. Computer-aided diagnosis of gastrointestinal stromal tumors: a

radiomics method on endoscopic ultrasound image. Int j comput assist radiol surg 2019; 14(10): 1635-
45.

## Li X, Lan M, Wang X, Zhang J, Gong L, Liao F, et al. Development and validation of a MRI-based

combined radiomics nomogram for differentiation in chondrosarcoma. Front oncol 2023; 13: 1090229.

## Li X, Shi X, Wang Y, Pang J, Zhao X, Xu Y, et al. A CT-based radiomics nomogram for predicting

histologic grade and outcome in chondrosarcoma. Cancer Imaging 2024; 24(1): 50.

## Li X, Zhang J, Leng Y, Liu J, Li L, Wan T, et al. Preoperative prediction of histopathological grading

in patients with chondrosarcoma using MRI-based radiomics with semantic features. BMC med imaging
2024; 24(1): 171.

## Liang HY, Yang SF, Zou HM, Hou F, Duan LS, Huang CC, et al. Deep Learning Radiomics Nomogram

to Predict Lung Metastasis in Soft-Tissue Sarcoma: A Multi-Center Study. Front oncol 2022; 12: 897676.

## Lin JX, Wang FH, Wang ZK, Wang JB, Zheng CH, Li P, et al. Prediction of the mitotic index and

preoperative risk stratification of gastrointestinal stromal tumors with CT radiomic features. Radiol Med
(Torino) 2023; 128(6): 644-54.

## Lin P, Yang PF, Chen S, Shao YY, Xu L, Wu Y, et al. A Delta-radiomics model for preoperative

evaluation of Neoadjuvant chemotherapy response in high-grade osteosarcoma. Cancer Imaging 2020;
20(1): 7.

## Lingappa E, Parvathy LR. Image Classification with Deep Learning Methods for Detecting and

Staging Bone Cancer from MRI. 2023 International Conference on … 2023.

## Liu B, Liu H, Zhang L, Song Y, Yang S, Zheng Z, et al. Value of contrast-enhanced CT based

radiomic machine learning algorithm in differentiating gastrointestinal stromal tumors with KIT exon 11
mutation: a two-center study. Diagn Interv Radiol 2022; 28(1): 29-38.

## Liu C, Guo Y, Jiang F, Xu L, Shen F, Jin Z, Wang Y. Gastrointestinal stromal tumors diagnosis on

multi-center endoscopic ultrasound images using multi-scale image normalization and transfer learning.
Technol Health Care 2022; 30(S1): 47-59.

## Liu C, Qiao M, Jiang F, Guo Y, Jin Z, Wang Y. TN-USMA Net: Triple normalization-based

gastrointestinal stromal tumors classification on multicenter EUS images with ultrasound-specific
pretraining and meta attention. Med Phys 2021; 48(11): 7199-214.

## Liu H, Jiao M, Yuan Y, Ouyang H, Liu J, Li Y, et al. Benign and malignant diagnosis of spinal tumors

based on deep learning and weighted fusion framework on MRI. Insights imaging 2022; 13(1): 87.

## Liu J, Huang J, Song Y, He Q, Fang W, Wang T, et al. Differentiating Gastrointestinal Stromal

Tumors From Leiomyomas of Upper Digestive Tract Using Convolutional Neural Network Model by
Endoscopic Ultrasonography. J Clin Gastroenterol 2024; 58(6): 574-9.

## Liu J, Lian T, Chen H, Wang X, Quan X, Deng Y, et al. Pretreatment Prediction of Relapse Risk in

Patients with Osteosarcoma Using Radiomics Nomogram Based on CT: A Retrospective Multicenter
Study. Biomed Res Int 2021; 2021: 6674471.

<!-- Page 68 -->


## Liu L, Chen J, Shan J, Sun X. Development and validation of an EUS-based nomogram for

prediction of the malignant potential in gastrointestinal stromal tumors. Scand J Gastroenterol 2023;
58(7): 830-7.

## Liu M, Bian J. Radiomics signatures based on contrast-enhanced CT for preoperative prediction

of the Ki-67 proliferation state in gastrointestinal stromal tumors. Jpn J Radiol 2023; 41(7): 741-51.

## Liu R, Pan D, Xu Y, Zeng H, He Z, Lin J, et al. A deep learning–machine learning fusion approach

for the classification of benign, malignant, and intermediate bone tumors. Eur Radiol 2022; 32(2): 1371-
83.

## Liu S, Sun W, Yang S, Duan L, Huang C, Xu J, et al. Deep learning radiomic nomogram to predict

recurrence in soft tissue sarcoma: a multi-institutional study. Eur Radiol 2022; 32(2): 793-805.

## Liu X, Guo L, Wang H, Guo J, Yang S, Duan L. Research on imbalance machine learning methods

for MR[Formula: see text]WI soft tissue sarcoma data. BMC med imaging 2022; 22(1): 149.

## Liu X, Yin Y, Wang X, Yang C, Wan S, Yin X, et al. Gastrointestinal stromal tumors: associations

between contrast-enhanced CT images and KIT exon 11 gene mutation. Ann transl med 2021; 9(19):
1496.

## Liu Y, He C, Fang W, Peng L, Shi F, Xia Y, et al. Prediction of Ki-67 expression in gastrointestinal

stromal tumors using radiomics of plain and multiphase contrast-enhanced CT. Eur Radiol 2023; 33(11):
7609-17.

## Liu Y, Yin P, Cui J, Sun C, Chen L, Hong N. Postoperative Relapse Prediction in Patients With Ewing

Sarcoma Using Computed Tomography-Based Radiomics Models Covering Tumor Per Se and Peritumoral
Signatures. J Comput Assist Tomogr 2023; 47(5): 766-73.

## Liu Y, Yin P, Cui J, Sun C, Chen L, Hong N, Li Z. Radiomics analysis based on CT for the prediction of

pulmonary metastases in ewing sarcoma. BMC med imaging 2023; 23(1): 147.

## Lombardi A, Arezzo F, Di Sciascio E, Ardito C, Mongelli M, Di Lillo N, et al. A human-interpretable

machine learning pipeline based on ultrasound to support leiomyosarcoma diagnosis. Artif Intell Med
2023; 146: 102697.

## Long B, Zhang H, Zhang H, Chen W, Sun Y, Tang R, et al. Deep learning models of ultrasonography

significantly improved the differential diagnosis performance for superficial soft-tissue masses: a
retrospective multicenter study. BMC Med 2023; 21(1): 405.

## Lu Y, Chen L, Wu J, Er L, Shi H, Cheng W, et al. Artificial intelligence in endoscopic

ultrasonography: risk stratification of gastric gastrointestinal stromal tumors. Therap adv in gastroenterol
2023; 16: 17562848231177156.

## Lu Y, Wu J, Hu M, Zhong Q, Er L, Shi H, et al. Artificial Intelligence in the Prediction of

Gastrointestinal Stromal Tumors on Endoscopic Ultrasonography Images: Development, Validation and
Comparison with Endosonographers. Gut Liver 2023; 17(6): 874-83.

<!-- Page 69 -->


## Luo Z, Li J, Liao Y, Huang W, Li Y, Shen X. Prediction of response to preoperative neoadjuvant

chemotherapy in extremity high-grade osteosarcoma using X-ray and multiparametric MRI radiomics.

## Journal Of X-Ray Science And Technology 2023; 31(3): 611-26.


## Luo Z, Li J, Liao Y, Liu R, Shen X, Chen W. Radiomics Analysis of Multiparametric MRI for

Prediction of Synchronous Lung Metastases in Osteosarcoma. Front oncol 2022; 12: 802234.

## Lv C, Chen H, Huang P, Chen Y, Liu B. Application of Computer-Assisted Endoscopic

Ultrasonography Based on Texture Features in Differentiating Gastrointestinal Stromal Tumors from
Benign Gastric Mesenchymal Tumors. Turk J Gastroenterol 2024; 35(5): 366-73.

## Malek M, Gity M, Alidoosti A, Oghabian Z, Rahimifar P, Seyed Ebrahimi SM, et al. A machine

learning approach for distinguishing uterine sarcoma from leiomyomas based on perfusion weighted
MRI parameters. Eur J Radiol 2019; 110: 203-11.

## Malinauskaite I, Hofmeister J, Burgermeister S, Neroladaki A, Hamard M, Montet X, Boudabbous

S. Radiomics and Machine Learning Differentiate Soft-Tissue Lipoma and Liposarcoma Better than
Musculoskeletal Radiologists. SARCOMA 2020; 2020: 7163453.

## Mao H, Zhang B, Zou M, Huang Y, Yang L, Wang C, et al. MRI-Based Radiomics Models for

Predicting Risk Classification of Gastrointestinal Stromal Tumors. Front oncol 2021; 11: 631927.

## Martin-Carreras T, Li H, Cooper K, Fan Y, Sebro R. Radiomic features from MRI distinguish

myxomas from myxofibrosarcomas. BMC med imaging 2019; 19(1): 67.

## Mayerhoefer ME, Breitenseher M, Amann G, Dominkus M. Are signal intensity and homogeneity

useful parameters for distinguishing between benign and malignant soft tissue masses on MR images?
Objective evaluation by means of texture analysis. Magn Reson Imaging 2008; 26(9): 1316-22.

## Mazumder MH, Singh MP. Bone Cancer Detection Using Deep Learning. … on Innovations in

Computer Science and … 2022.

## Megala G, Swarnalatha P, Venkatesan R. Detecting Bone Tumor on Applying Edge Computational

Deep Learning Approach. International Conference on … 2023.

## Minoda Y, Ihara E, Fujimori N, Nagatomo S, Esaki M, Hata Y, et al. Efficacy of ultrasound

endoscopy with artificial intelligence for the differential diagnosis of non-gastric gastrointestinal stromal
tumors. Sci rep 2022; 12(1): 16640.

## Minoda Y, Ihara E, Komori K, Ogino H, Otsuka Y, Chinen T, et al. Efficacy of endoscopic ultrasound

with artificial intelligence for the diagnosis of gastrointestinal stromal tumors. J Gastroenterol 2020;
55(12): 1119-26.

## Mutlu IN, Kocak B, Kus EA, Ulusan MB, Kilickesmez O. Machine Learning-Based Computed

Tomography Texture Analysis of Lytic Bone Lesions Needing Biopsy: A Preliminary Study. Istanb Med J
2021; 22(3): 223-31.

## Nakagawa M, Nakaura T, Namimoto T, Iyama Y, Kidoh M, Hirata K, et al. A multiparametric MRI-

based machine learning to distinguish between uterine sarcoma and benign leiomyoma: comparison
with 18F-FDG PET/CT. Clin Radiol 2019; 74(2): 167.e1-.e.

<!-- Page 70 -->


## Nakagawa M, Nakaura T, Namimoto T, Iyama Y, Kidoh M, Hirata K, et al. Machine Learning to

Differentiate T2-Weighted Hyperintense Uterine Leiomyomas from Uterine Sarcomas by Utilizing
Multiparametric Magnetic Resonance Quantitative Imaging Features. Acad Radiol 2019; 26(10): 1390-9.

## Nakagawa M, Nakaura T, Yoshida N, Azuma M, Uetani H, Nagayama Y, et al. Performance of

Machine Learning Methods Based on Multi-Sequence Textural Parameters Using Magnetic Resonance
Imaging and Clinical Information to Differentiate Malignant and Benign Soft Tissue Tumors. Acad Radiol
2023; 30(1): 83-92.

## Navarro F, Dapper H, Asadpour R, Knebel C, Spraker MB, Schwarze V, et al. Development and

External Validation of Deep-Learning-Based Tumor Grading Models in Soft-Tissue Sarcoma Patients Using
MR Imaging. Cancers (Basel) 2021; 13(12).

## Nguyen VX, Nguyen CC, Li B, Das A. Digital image analysis is a useful adjunct to endoscopic

ultrasonographic diagnosis of subepithelial lesions of the gastrointestinal tract. J Ultrasound Med 2010;
29(9): 1345-51.

## Nie P, Zhao X, Wang N, Ma J, Zuo P, Hao D, Yu T. A Computed Tomography Radiomics Nomogram

in Differentiating Chordoma From Giant Cell Tumor in the Axial Skeleton. J Comput Assist Tomogr 2023;
47(3): 453-9.

## Ning Z, Luo J, Li Y, Han S, Feng Q, Xu Y, et al. Pattern Classification for Gastrointestinal Stromal

Tumors by Integration of Radiomics and Deep Convolutional Features. IEEE j biomed health inform 2019;
23(3): 1181-91.

## Oh CK, Kim T, Cho YK, Cheung DY, Lee BI, Cho YS, et al. Convolutional neural network-based

object detection model to identify gastrointestinal stromal tumors in endoscopic ultrasound images. J
Gastroenterol Hepatol 2021; 36(12): 3387-94.

## Ouyang H, Meng F, Liu J, Song X, Li Y, Yuan Y, et al. Evaluation of Deep Learning-Based Automated

Detection of Primary Spine Tumors on MRI Using the Turing Test. Front Oncol 2022; 12.

## Pan D, Liu R, Zheng B, Yuan J, Zeng H, He Z, et al. Using Machine Learning to Unravel the Value of

Radiographic Features for the Classification of Bone Tumors. BioMed Res Int 2021; 2021.

## Pan J, Zhang K, Le H, Jiang Y, Li W, Geng Y, et al. Radiomics Nomograms Based on Non-enhanced

MRI and Clinical Risk Factors for the Differentiation of Chondrosarcoma from Enchondroma. J Magn
Reson Imaging 2021; 54(4): 1314-23.

## Park CW, Oh SJ, Kim KS, Jang MC, Kim IS, Lee YK, et al. Artificial intelligence-based classification

of bone tumors in the proximal femur on plain radiographs: System development and validation. PLoS
ONE 2022; 17(2 February).

## Peeken JC, Asadpour R, Specht K, Chen EY, Klymenko O, Akinkuoroye V, et al. MRI-based deltaradiomics predicts pathologic complete response in high-grade soft-tissue sarcoma patients treated with

neoadjuvant therapy. Radiother Oncol 2021; 164: 73-82.

## Peeken JC, Bernhofer M, Spraker MB, Pfeiffer D, Devecka M, Thamer A, et al. CT-based radiomic

features predict tumor grading and have prognostic value in patients with soft tissue sarcomas treated
with neoadjuvant radiation therapy. Radiother Oncol 2019; 135: 187-96.

<!-- Page 71 -->


## Peeken JC, Neumann J, Asadpour R, Leonhardt Y, Moreira JR, Hippe DS, et al. Prognostic

Assessment in High-Grade Soft-Tissue Sarcoma Patients: A Comparison of Semantic Image Analysis and
Radiomics. Cancers (Basel) 2021; 13(8).

## Peeken JC, Spraker MB, Knebel C, Dapper H, Pfeiffer D, Devecka M, et al. Tumor grading of soft

tissue sarcomas using MRI-based radiomics. EBioMedicine 2019; 48: 332-40.

## Peng Y, Bi L, Guo Y, Feng D, Fulham M, Kim J. Deep multi-modality collaborative learning for

distant metastases predication in PET-CT soft-tissue sarcoma studies. Annu Int Conf IEEE Eng Med Biol
Soc 2019; 2019: 3658-88.

## Peng Y, Bi L, Kumar A, Fulham M, Feng D, Kim J. Predicting distant metastases in soft-tissue

sarcomas from PET-CT scans using constrained hierarchical multi-modality feature learning. Phys Med
Biol 2021; 66(24).

## Pereira HM, Leite Duarte ME, Ribeiro Damasceno I, de Oliveira Moura Santos LA, Nogueira-

Barbosa MH. Machine learning-based CT radiomics features for the prediction of pulmonary metastasis
in osteosarcoma. Br J Radiol 2021; 94(1124): 20201391.

## Pressney I, Khoo M, Endozo R, Ganeshan B, O'Donnell P. Pilot study to differentiate lipoma from

atypical lipomatous tumour/well-differentiated liposarcoma using MR radiomics-based texture analysis.
Skeletal Radiol 2020; 49(11): 1719-29.

## Purnima S, Lashna V, Mahalakshmi R. An Approach to Detect and Classify Bone tumour using fast

and Robust Fuzzy C Means Clustering technique. Annals of the … 2021.

## Ren C, Wang S, Zhang S. Development and validation of a nomogram based on CT images and 3D

texture analysis for preoperative prediction of the malignant potential in gastrointestinal stromal tumors.
Cancer Imaging 2020; 20(1): 5.

## Rengo M, Onori A, Caruso D, Bellini D, Carbonetti F, De Santis D, et al. Development and

Validation of Artificial-Intelligence-Based Radiomics Model Using Computed Tomography Features for
Preoperative Risk Stratification of Gastrointestinal Stromal Tumors. J Pers Med 2023; 13(5).

## Ristow I, Madesta F, Well L, Shenas F, Wright F, Molwitz I, et al. Evaluation of magnetic resonance

imaging-based radiomics characteristics for differentiation of benign and malignant peripheral nerve
sheath tumors in neurofibromatosis type 1. Neuro-oncol 2022; 24(10): 1790-8.

## Roller LA, Wan Q, Liu X, Qin L, Chapel D, Burk KS, et al. MRI, clinical, and radiomic models for

differentiation of uterine leiomyosarcoma and leiomyoma. Abdom Radiol 2024; 49(5): 1522-33.

## Sampath K, Rajagopal S, Chintanpalli A. A comparative analysis of CNN-based deep learning

architectures for early diagnosis of bone cancer using CT images. Sci rep 2024; 14(1): 2144.

## Santoro M, Zybin V, Coada CA, Mantovani G, Paolani G, Di Stanislao M, et al. Machine Learning

Applied to Pre-Operative Computed-Tomography-Based Radiomic Features Can Accurately Differentiate
Uterine Leiomyoma from Leiomyosarcoma: A Pilot Study. Cancers (Basel) 2024; 16(8).

<!-- Page 72 -->


## Seven G, Silahtaroglu G, Kochan K, Ince AT, Arici DS, Senturk H. Use of Artificial Intelligence in the

Prediction of Malignant Potential of Gastric Gastrointestinal Stromal Tumors. Dig Dis Sci 2022; 67(1):
273-81.

## Seven G, Silahtaroglu G, Seven OO, Senturk H. Differentiating Gastrointestinal Stromal Tumors

from Leiomyomas Using a Neural Network Trained on Endoscopic Ultrasonography Images. Dig Dis 2022;
40(4): 427-35.

## Shang S, Sun J, Yue Z, Wang Y, Wang X, Luo Y, et al. Multi-parametric MRI based radiomics with

tumor subregion partitioning for differentiating benign and malignant soft-tissue tumors. Biomed Signal
Process Control 2021; 67.

## Shao J, Lin H, Ding L, Li B, Xu D, Sun Y, et al. Deep learning for differentiation of osteolytic

osteosarcoma and giant cell tumor around the knee joint on radiographs: a multicenter study. Insights
imaging 2024; 15(1): 35.

## Shao J, Wang C, Shu K, Zhou Y, Cheng N, Lai Z, et al. A contrast-enhanced CT-based radiomic

nomogram for the differential diagnosis of intravenous leiomyomatosis and uterine leiomyoma. Front
oncol 2023; 13: 1239124.

## Shao M, Niu Z, He L, Fang Z, He J, Xie Z, et al. Building Radiomics Models Based on Triple-Phase

CT Images Combining Clinical Features for Discriminating the Risk Rating in Gastrointestinal Stromal
Tumors. Front oncol 2021; 11: 737302.

## Sharma A, Yadav DP, Garg H, Kumar M, Sharma B, Koundal D. Bone Cancer Detection Using

Feature Extraction Based Machine Learning Model. Comput math methods med 2021; 2021: 7433186.

## Sheen H, Kim W, Byun BH, Kong CB, Song WS, Cho WH, et al. Metastasis risk prediction model in

osteosarcoma using metabolic imaging phenotypes: A multivariable radiomics model. PLoS ONE 2019;
14(11): e0225242.

## Shen R, Li Z, Zhang L, Hua Y, Mao M, Li Z, et al. Osteosarcoma Patients Classification Using Plain

X-Rays and Metabolomic Data. Conf Proc IEEE Eng Med Biol Soc 2018; 2018: 690-3.

## Shrivastava A, Nag MK. Enhancing Bone Cancer Diagnosis Through Image Extraction and

Machine Learning: A State-of-the-Art Approach. Surg Innov 2024; 31(1): 58-70.

## Sierra ED, Valenzuela R, Canjirathinkal MA, Costelloe CM, Moradi H, Madewell JE, et al. Cancer

Radiomic and Perfusion Imaging Automated Framework: Validation on Musculoskeletal Tumors. JCO Clin
Cancer Inform 2024; 8: e2300118.

## Singh M, Angurala M, Bala M. Bone Tumour detection Using Feature Extraction with

Classification by Deep Learning Techniques. Research Journal of Computer … 2020.

## Skorpil M, Ryden H, Berglund J, Brynolfsson P, Brosjo O, Tsagozis P. Soft-tissue fat tumours:

differentiating malignant from benign using proton density fat fraction quantification MRI. Clin Radiol
2019; 74(7): 534-8.

<!-- Page 73 -->


## Song Y, Li J, Wang H, Liu B, Yuan C, Liu H, et al. Radiomics Nomogram Based on Contrastenhanced CT to Predict the Malignant Potential of Gastrointestinal Stromal Tumor: A Two-center Study.

Acad Radiol 2022; 29(6): 806-16.

## Spraker MB, Wootton LS, Hippe DS, Ball KC, Peeken JC, Macomber MW, et al. MRI Radiomic

Features Are Independently Associated With Overall Survival in Soft Tissue Sarcoma. Adv Radiat Oncol
2019; 4(2): 413-21.

## Starmans MPA, Timbergen MJM, Vos M, Renckens M, Grunhagen DJ, van Leenders G, et al.

Differential Diagnosis and Molecular Stratification of Gastrointestinal Stromal Tumors on CT Images Using
a Radiomics Approach. J Digit Imaging 2022; 35(2): 127-36.

## Su Q, Wang N, Wang B, Wang Y, Dai Z, Zhao X, et al. Ct-based intratumoral and peritumoral

radiomics for predicting prognosis in osteosarcoma: A multicenter study. Eur J Radiol 2024; 172: 111350.

## Sudjai N, Siriwanarangsun P, Lektrakul N, Saiviroonporn P, Maungsomboon S, Phimolsarnti R, et

al. Robustness of Radiomic Features: Two-Dimensional versus Three-Dimensional MRI-Based Feature
Reproducibility in Lipomatous Soft-Tissue Tumors. Diagnostics (Basel) 2023; 13(2).

## Sudjai N, Siriwanarangsun P, Lektrakul N, Saiviroonporn P, Maungsomboon S, Phimolsarnti R, et

al. Tumor-to-bone distance and radiomic features on MRI distinguish intramuscular lipomas from welldifferentiated liposarcomas. J ORTHOP SURG 2023; 18(1): 255.

## Sun K, Yu S, Wang Y, Jia R, Shi R, Liang C, et al. Development of a multi-phase CT-based radiomics

model to differentiate heterotopic pancreas from gastrointestinal stromal tumor. BMC med imaging
2024; 24(1): 44.

## Sun W, Liu S, Guo J, Liu S, Hao D, Hou F, et al. A CT-based radiomics nomogram for distinguishing

between benign and malignant bone tumours. Cancer Imaging 2021; 21(1): 20.

## Sun XF, Zhu HT, Ji WY, Zhang XY, Li XT, Tang L, Sun YS. Preoperative prediction of malignant

potential of 2-5 cm gastric gastrointestinal stromal tumors by computerized tomography-based
radiomics. World J Gastrointest Oncol 2022; 14(5): 1014-26.

## Tagliafico AS, Bignotti B, Rossi F, Valdora F, Martinoli C. Local recurrence of soft tissue sarcoma: a

radiomic analysis. RADIOL ONCOL 2019; 53(3): 300-6.

## Tamehisa T, Sato S, Sakai T, Maekawa R, Tanabe M, Ito K, Sugino N. Establishment of Noninvasive

Prediction Models for the Diagnosis of Uterine Leiomyoma Subtypes. Obstet Gynecol 2024; 143(3): 358-
65.

## Tang Y, Cui J, Zhu J, Fan G. Differentiation Between Lipomas and Atypical Lipomatous Tumors of

the Extremities Using Radiomics. J Magn Reson Imaging 2022; 56(6): 1746-54.

## Teo KY, Daescu O, Cederberg K, Sengupta A, Leavey PJ. Correlation of histopathology and multimodal magnetic resonance imaging in childhood osteosarcoma: Predicting tumor response to

chemotherapy. PLoS ONE 2022; 17(2): e0259564.

## Thornhill RE, Golfam M, Sheikh A, Cron GO, White EA, Werier J, et al. Differentiation of lipoma

from liposarcoma on MRI using texture and shape analysis. Acad Radiol 2014; 21(9): 1185-94.

<!-- Page 74 -->


## Tian L, Li X, Zheng H, Wang L, Qin Y, Cai J. Fisher discriminant model based on LASSO logistic

regression for computed tomography imaging diagnosis of pelvic rhabdomyosarcoma in children. Sci rep
2022; 12(1): 15631.

## Tian L, Zhang D, Bao S, Nie P, Hao D, Liu Y, et al. Radiomics-based machine-learning method for

prediction of distant metastasis from soft-tissue sarcomas. Clin Radiol 2021; 76(2): 158.e19-.e25.

## Tian Z, Cheng Y, Zhao S, Li R, Zhou J, Sun Q, Wang D. Deep learning radiomics-based prediction

model of metachronous distant metastasis following curative resection for retroperitoneal
leiomyosarcoma: a bicentric study. Cancer Imaging 2024; 24(1): 52.

## Timbergen MJM, Starmans MPA, Padmos GA, Grunhagen DJ, van Leenders G, Hanff DF, et al.

Differential diagnosis and mutation stratification of desmoid-type fibromatosis on MRI using radiomics.
Eur J Radiol 2020; 131: 109266.

## Toyohara Y, Sone K, Noda K, Yoshida K, Kato S, Kaiume M, et al. The automatic diagnosis artificial

intelligence system for preoperative magnetic resonance imaging of uterine sarcoma. J gynecol oncol
2024; 35(3): e24.

## Toyohara Y, Sone K, Noda K, Yoshida K, Kurokawa R, Tanishima T, et al. Development of a deep

learning method for improving diagnostic accuracy for uterine sarcoma cases. Sci rep 2022; 12(1): 19612.

## Usuff R, Kothandapani S, Rangan R. Enhancing radiographic image interpretation: WARES-PRS

model for knee bone tumour detection. … in Neural Systems 2024.

## Vaiyapuri T, Balaji P, Shridevi S, Dharmarajlu SM, Alaseem NA. An attention-based bidirectional

long short-term memory based optimal deep learning technique for bone cancer detection and
classifications. Aims Mathematics 2024; 9(6): 16704-20.

## Vallieres M, Freeman CR, Skamene SR, El Naqa I. A radiomics model from joint FDG-PET and MRI

texture features for the prediction of lung metastases in soft-tissue sarcomas of the extremities. Phys
Med Biol 2015; 60(14): 5471-96.
225. von Schacky CE, Wilhelm NJ, Schäfer VS, Leonhardt Y, Gassert FG, Foreman SC, et al. Multitask
deep learning for segmentation and classification of primary bone tumors on radiographs. Radiology
2021; 301(2): 398-406.
226. von Schacky CE, Wilhelm NJ, Schafer VS, Leonhardt Y, Jung M, Jungmann PM, et al. Development
and evaluation of machine learning models based on X-ray radiomics for the classification and
differentiation of malignant and benign bone tumors. Eur Radiol 2022; 32(9): 6247-57.

## Vos M, Starmans MPA, Timbergen MJM, van der Voort SR, Padmos GA, Kessels W, et al.

Radiomics approach to distinguish between well differentiated liposarcomas and lipomas on MRI. Br J
Surg 2019; 106(13): 1800-9.

## Wahab CA, Jannot AS, Bonaffini PA, Bourillon C, Cornou C, Lefrere-Belda MA, et al. Diagnostic

Algorithm to Differentiate Benign Atypical Leiomyomas from Malignant Uterine Sarcomas with Diffusionweighted MRI (vol 297, pg 361, 2020). Radiology 2020; 297(3): E347-E.

<!-- Page 75 -->


## Wang B, Perronne L, Burke C, Adler RS. Artificial intelligence for classification of soft-tissue

masses at us. Radiology: Art Int 2021; 3(1).

## Wang C, Li H, Jiaerken Y, Huang P, Sun L, Dong F, et al. Building CT Radiomics-Based Models for

Preoperatively Predicting Malignant Potential and Mitotic Count of Gastrointestinal Stromal Tumors.
Transl Oncol 2019; 12(9): 1229-36.

## Wang C, Zhang Z, Dou Y, Liu Y, Chen B, Liu Q, Wang S. Development of clinical and magnetic

resonance imaging-based radiomics nomograms for the differentiation of nodular fasciitis from soft
tissue sarcoma. Acta Radiol 2023; 64(9): 2578-89.

## Wang FH, Zheng HL, Li JT, Li P, Zheng CH, Chen QY, et al. Prediction of recurrence-free survival

and adjuvant therapy benefit in patients with gastrointestinal stromal tumors based on radiomics
features. Radiol Med (Torino) 2022; 127(10): 1085-97.

## Wang H, Chen H, Duan S, Hao D, Liu J. Radiomics and Machine Learning With Multiparametric

Preoperative MRI May Accurately Predict the Histopathological Grades of Soft Tissue Sarcomas. J Magn
Reson Imaging 2020; 51(3): 791-7.

## Wang H, Nie P, Wang Y, Xu W, Duan S, Chen H, et al. Radiomics nomogram for differentiating

between benign and malignant soft-tissue masses of the extremities. J Magn Reson Imaging 2020; 51(1):
155-63.

## Wang H, Zhang J, Bao S, Liu J, Hou F, Huang Y, et al. Preoperative MRI-Based Radiomic Machine-

Learning Nomogram May Accurately Distinguish Between Benign and Malignant Soft-Tissue Lesions: A
Two-Center Study. J Magn Reson Imaging 2020; 52(3): 873-82.

## Wang J, Shao M, Hu H, Xiao W, Cheng G, Yang G, et al. Convolutional neural network applied to

preoperative venous-phase CT images predicts risk category in patients with gastric gastrointestinal
stromal tumors. BMC Cancer 2024; 24(1): 280.

## Wang J, Xie Z, Zhu X, Niu Z, Ji H, He L, et al. Differentiation of gastric schwannomas from

gastrointestinal stromal tumors by CT using machine learning. Abdom Radiol 2021; 46(5): 1773-82.

## Wang JK. Predictive value and modeling analysis of MSCT signs in gastrointestinal stromal tumors

(GISTs) to pathological risk degree. Eur Rev Med Pharmacol Sci 2017; 21(5): 999-1005.

## Wang M, Feng Z, Zhou L, Zhang L, Hao X, Zhai J. Computed-Tomography-Based Radiomics Model

for Predicting the Malignant Potential of Gastrointestinal Stromal Tumors Preoperatively: A Multi-
Classifier and Multicenter Study. Front oncol 2021; 11: 582847.

## Wang P, Yan J, Qiu H, Huang J, Yang Z, Shi Q, Yan C. A radiomics-clinical combined nomogrambased on non-enhanced CT for discriminating the risk stratification in GISTs. J Cancer Res Clin Oncol 2023;

149(14): 12993-3003.

## Wang Q, Zhang Y, Zhang E, Xing X, Chen Y, Nie K, et al. A Multiparametric Method Based on

Clinical and CT-Based Radiomics to Predict the Expression of p53 and VEGF in Patients With Spinal Giant
Cell Tumor of Bone. Front oncol 2022; 12: 894696.

<!-- Page 76 -->


## Wang Q, Zhang Y, Zhang E, Xing X, Chen Y, Su MY, Lang N. Prediction of the early recurrence in

spinal giant cell tumor of bone using radiomics of preoperative CT: Long-term outcome of 62 consecutive
patients. J Bone Oncol 2021; 27: 100354.

## Wang S, Sun M, Sun J, Wang Q, Wang G, Wang X, et al. Advancing musculoskeletal tumor

diagnosis: Automated segmentation and predictive classification using deep learning and radiomics.
Comput Biol Med 2024; 175: 108502.

## Wang Y, Wang Y, Ren J, Jia L, Ma L, Yin X, et al. Malignancy risk of gastrointestinal stromal tumors

evaluated with noninvasive radiomics: A multi-center study. Front oncol 2022; 12: 966743.

## Wei CJ, Yan C, Tang Y, Wang W, Gu YH, Ren JY, et al. Computed Tomography-Based Differentiation

of Benign and Malignant Craniofacial Lesions in Neurofibromatosis Type I Patients: A Machine Learning
Approach. Front oncol 2020; 10: 1192.

## Wei Y, Lu Z, Ren Y. Predictive Value of a Radiomics Nomogram Model Based on Contrast-

Enhanced Computed Tomography for KIT Exon 9 Gene Mutation in Gastrointestinal Stromal Tumors.
Technol Cancer Res Treat 2023; 22: 15330338231181260.

## White LM, Atinga A, Naraghi AM, Lajkosz K, Wunder JS, Ferguson P, et al. T2-weighted MRI

radiomics in high-grade intramedullary osteosarcoma: predictive accuracy in assessing histologic
response to chemotherapy, overall survival, and disease-free survival. Skeletal Radiol 2023; 52(3): 553-
64.

## Wu Y, Xu L, Yang P, Lin N, Huang X, Pan W, et al. Survival Prediction in High-grade Osteosarcoma

Using Radiomics of Diagnostic Computed Tomography. EBioMedicine 2018; 34: 27-34.

## Xie H, Hu J, Zhang X, Ma S, Liu Y, Wang X. Preliminary utilization of radiomics in differentiating

uterine sarcoma from atypical leiomyoma: Comparison on diagnostic efficacy of MRI features and
radiomic features. Eur J Radiol 2019; 115: 39-45.

## Xie H, Zhang X, Ma S, Liu Y, Wang X. Preoperative Differentiation of Uterine Sarcoma from

Leiomyoma: Comparison of Three Models Based on Different Segmentation Volumes Using Radiomics.
Mol Imaging Biol 2019; 21(6): 1157-64.

## Xie H, Zhang Y, Dong L, Lv H, Li X, Zhao C, et al. Deep learning driven diagnosis of malignant soft

tissue tumors based on dual-modal ultrasound images and clinical indexes. Front oncol 2024; 14:
1361694.

## Xie Z, Suo S, Zhang W, Zhang Q, Dai Y, Song Y, et al. Prediction of high Ki-67 proliferation index of

gastrointestinal stromal tumors based on CT at non-contrast-enhanced and different contrast-enhanced
phases. Eur Radiol 2024; 34(4): 2223-32.

## Xie Z, Zhao H, Song L, Ye Q, Zhong L, Li S, et al. A radiograph-based deep learning model

improves radiologists’ performance for classification of histological types of primary bone tumors: A
multicenter study. Eur J Radiol 2024; 176.

## Xu F, Ma X, Wang Y, Tian Y, Tang W, Wang M, et al. CT texture analysis can be a potential tool to

differentiate gastrointestinal stromal tumors without KIT exon 11 mutation. Eur J Radiol 2018; 107: 90-7.

<!-- Page 77 -->


## Xu J, Miao L, Wang CX, Wang HH, Wang QZ, Li M, et al. Preoperative Contrast-Enhanced CT-Based

Deep Learning Radiomics Model for Distinguishing Retroperitoneal Lipomas and Well-Differentiated
Liposarcomas. Acad Radiol 2024; 31(12): 5042-53.

## Xu L, Wang MY, Qi L, Zou YF, Fei-Yun WU, Sun XL. Radiomics approach to distinguish between

benign and malignant soft tissue tumors on magnetic resonance imaging. Eur J Radiol Open 2024; 12:
100555.

## Xu L, Yang P, Hu K, Wu Y, Xu-Welliver M, Wan Y, et al. Prediction of neoadjuvant chemotherapy

response in high-grade osteosarcoma: added value of non-tumorous bone radiomics using CT images.
Quant imaging med surg 2021; 11(4): 1184-95.

## Xu R, Kido S, Suga K, Hirano Y, Tachibana R, Muramatsu K, et al. Texture analysis on (18)F-FDG

PET/CT images to differentiate malignant and benign bone and soft-tissue lesions. Ann Nucl Med 2014;
28(9): 926-35.

## Xu W, Hao D, Hou F, Zhang D, Wang H. Soft Tissue Sarcoma: Preoperative MRI-Based Radiomics

and Machine Learning May Be Accurate Predictors of Histopathologic Grade. AJR Am J Roentgenol 2020;
215(4): 963-9.

## Xu Z, Niu K, Tang S, Song T, Rong Y, Guo W, He Z. Bone tumor necrosis rate detection in few-shot

X-rays based on deep learning. Comput Med Imaging Graph 2022; 102.

## Yamazawa E, Takahashi S, Shin M, Tanaka S, Takahashi W, Nakamoto T, et al. MRI-Based

Radiomics Differentiates Skull Base Chordoma and Chondrosarcoma: A Preliminary Study. Cancers (Basel)
2022; 14(13).

## Yan J, Zhao X, Han S, Wang T, Miao F. Evaluation of Clinical Plus Imaging Features and

Multidetector Computed Tomography Texture Analysis in Preoperative Risk Grade Prediction of Small
Bowel Gastrointestinal Stromal Tumors. J Comput Assist Tomogr 2018; 42(5): 714-20.

## Yan M, Liu Y, You H, Zhao Y, Jin J, Wang J. Differentiation of Small Gastrointestinal Stromal Tumor

and Gastric Leiomyoma with Contrast-Enhanced CT. J healthc eng 2023; 2023: 6423617.

## Yan R, Hao D, Li J, Liu J, Hou F, Chen H, et al. Magnetic Resonance Imaging-Based Radiomics

Nomogram for Prediction of the Histopathological Grade of Soft Tissue Sarcomas: A Two-Center Study. J
Magn Reson Imaging 2021; 53(6): 1683-96.

## Yang F, Feng Y, Sun P, Traverso A, Dekker A, Zhang B, et al. Preoperative prediction of high-grade

osteosarcoma response to neoadjuvant therapy based on a plain CT radiomics model: A dual-center
study. J Bone Oncol 2024; 47: 100614.

## Yang J, Chen Z, Liu W, Wang X, Ma S, Jin F, Wang X. Development of a Malignancy Potential

Binary Prediction Model Based on Deep Learning for the Mitotic Count of Local Primary Gastrointestinal
Stromal Tumors. Korean J Radiol 2021; 22(3): 344-53.

## Yang L, Du D, Zheng T, Liu L, Wang Z, Du J, et al. Deep learning and radiomics to predict the

mitotic index of gastrointestinal stromal tumors based on multiparametric MRI. Front oncol 2022; 12:
948557.

<!-- Page 78 -->


## Yang L, Ma CF, Li Y, Zhang CR, Ren JL, Shi GF. Application of radiomics in predicting the

preoperative risk stratification of gastric stromal tumors. Diagn Interv Radiol 2022; 28(6): 532-9.

## Yang L, Zhang D, Zheng T, Liu D, Fang Y. Predicting the progression-free survival of gastrointestinal

stromal tumors after imatinib therapy through multi-sequence magnetic resonance imaging. Abdom
Radiol 2024; 49(3): 801-13.

## Yang L, Zheng T, Dong Y, Wang Z, Liu D, Du J, et al. MRI Texture-Based Models for Predicting

Mitotic Index and Risk Classification of Gastrointestinal Stromal Tumors. J Magn Reson Imaging 2021;
53(4): 1054-65.

## Yang P, Wu J, Liu M, Zheng Y, Zhao X, Mao Y. Preoperative CT-based radiomics and deep learning

model for predicting risk stratification of gastric gastrointestinal stromal tumors. Med Phys 2024; 51(10):
7257-68.

## Yang X, Wang H, Dong Q, Xu Y, Liu H, Ma X, et al. An artificial intelligence system for

distinguishing between gastrointestinal stromal tumors and leiomyomas using endoscopic
ultrasonography. Endoscopy 2022; 54(3): 251-61.

## Yang Y, Ma X, Wang Y, Ding X. Prognosis prediction of extremity and trunk wall soft-tissue

sarcomas treated with surgical resection with radiomic analysis based on random survival forest.
Updates Surg 2022; 74(1): 355-65.

## Yang Y, Zhou Y, Zhou C, Ma X. Novel computer aided diagnostic models on multimodality medical

images to differentiate well differentiated liposarcomas from lipomas approached by deep learning
methods. Orphanet J Rare Dis 2022; 17(1): 158.

## Yang Y, Zhou Y, Zhou C, Zhang X, Ma X. MRI-Based Computer-Aided Diagnostic Model to Predict

Tumor Grading and Clinical Outcomes in Patients With Soft Tissue Sarcoma. J Magn Reson Imaging 2022;
56(6): 1733-45.

## Ye Q, Yang H, Lin B, Wang M, Song L, Xie Z, et al. Automatic detection, segmentation, and

classification of primary bone tumors and bone infections using an ensemble multi-task deep learning
framework on multi-parametric MRIs: a multi-center study. Eur Radiol 2024; 34(7): 4287-99.

## Yildiz Potter I, Yeritsyan D, Mahar S, Wu J, Nazarian A, Vaziri A, Vaziri A. Automated Bone Tumor

Segmentation and Classification as Benign or Malignant Using Computed Tomographic Imaging. J Digit
Imaging 2023; 36(3): 869-78.

## Yin P, Mao N, Chen H, Sun C, Wang S, Liu X, Hong N. Machine and Deep Learning Based

Radiomics Models for Preoperative Prediction of Benign and Malignant Sacral Tumors. Front Oncol 2020;
10.

## Yin P, Mao N, Liu X, Sun C, Wang S, Chen L, Hong N. Can clinical radiomics nomogram based on

3D multiparametric MRI features and clinical characteristics estimate early recurrence of pelvic
chondrosarcoma? J Magn Reson Imaging 2020; 51(2): 435-45.

## Yin P, Mao N, Wang S, Sun C, Hong N. Clinical-radiomics nomograms for pre-operative

differentiation of sacral chordoma and sacral giant cell tumor based on 3D computed tomography and
multiparametric magnetic resonance imaging. Br J Radiol 2019; 92(1101): 20190155.

<!-- Page 79 -->


## Yin P, Mao N, Zhao C, Wu J, Chen L, Hong N. A Triple-Classification Radiomics Model for the

Differentiation of Primary Chordoma, Giant Cell Tumor, and Metastatic Tumor of Sacrum Based on T2-
Weighted and Contrast-Enhanced T1-Weighted MRI. J Magn Reson Imaging 2019; 49(3): 752-9.

## Yin P, Mao N, Zhao C, Wu J, Sun C, Chen L, Hong N. Comparison of radiomics machine-learning

classifiers and feature selection for differentiation of sacral chordoma and sacral giant cell tumour based
on 3D computed tomography features. Eur Radiol 2019; 29(4): 1841-7.

## Yin P, Sun C, Wang S, Chen L, Hong N. Clinical-Deep Neural Network and Clinical-Radiomics

Nomograms for Predicting the Intraoperative Massive Blood Loss of Pelvic and Sacral Tumors. Front
Oncol 2021; 11.

## Yin P, Wang W, Wang S, Liu T, Sun C, Liu X, et al. The potential for different computed

tomography-based machine learning networks to automatically segment and differentiate pelvic and
sacral osteosarcoma from Ewing's sarcoma. Quant imaging med surg 2023; 13(5): 3174-84.

## Yin P, Zhong J, Liu Y, Liu T, Sun C, Liu X, et al. Clinical-radiomics models based on plain X-rays for

prediction of lung metastasis in patients with osteosarcoma. BMC med imaging 2023; 23(1): 40.

## Yin XN, Wang ZH, Zou L, Yang CW, Shen CY, Liu BK, et al. Computed tomography radiogenomics: A

potential tool for prediction of molecular subtypes in gastric stromal tumor. World J Gastrointest Oncol
2024; 16(4): 1296-308.

## Yisheng X, Yueqin L, Ming Z. Diagnostic significance of multisequence MRI radiomics models in

distinguishing benign and malignant spinal fractures. J Radiat Res Appl Sci 2024; 17(3).

## Yoon H, Choi WH, Joo MW, Ha S, Chung YA. SPECT/CT Radiomics for Differentiating between

Enchondroma and Grade I Chondrosarcoma. Tomography 2023; 9(5): 1868-75.

## Yu Y, Guo H, Zhang M, Hou F, Yang S, Huang C, et al. Multi-institutional validation of a radiomics

signature for identification of postoperative progression of soft tissue sarcoma. Cancer Imaging 2024;
24(1): 59.

## Yue Z, Wang X, Wang Y, Wang H, Jiang W. Clinical-Radiomics Nomogram from T1W, T1CE, and

T2FS MRI for Improving Diagnosis of Soft-Tissue Sarcoma. Mol Imaging Biol 2022; 24(6): 995-1006.

## Yue Z, Wang X, Yu T, Shang S, Liu G, Jing W, et al. Multi-parametric MRI-based radiomics for the

diagnosis of malignant soft-tissue tumor. Magn Reson Imaging 2022; 91: 91-9.

## Yuguang Y, Chen Y, Zhu D, Huang Y, Huang Y, Li X, Xiahou J. GHA-DenseNet prediction and

diagnosis of malignancy in femoral bone tumors using magnetic resonance imaging. J Bone Oncol 2024;
44: 100520.

## Zhai Y, Bai J, Xue Y, Li M, Mao W, Zhang X, Zhang Y. Development and validation of a preoperative

MRI-based radiomics nomogram to predict progression-free survival in patients with clival chordomas.
Front oncol 2022; 12: 996262.

## Zhang C, Wang C, Mao G, Cheng G, Ji H, He L, et al. Radiomics analysis of contrast-enhanced

computerized tomography for differentiation of gastric schwannomas from gastric gastrointestinal
stromal tumors. J Cancer Res Clin Oncol 2024; 150(2): 87.

<!-- Page 80 -->


## Zhang C, Wang J, Yang Y, Dai B, Xu Z, Zhu F, Yu H. Machine learning for predicting the risk

stratification of 1-5 cm gastric gastrointestinal stromal tumors based on CT. BMC med imaging 2023;
23(1): 90.

## Zhang L, Gao Q, Dou Y, Cheng T, Xia Y, Li H, Gao S. Evaluation of the neoadjuvant chemotherapy

response in osteosarcoma using the MRI DWI-based machine learning radiomics nomogram. Front oncol
2024; 14: 1345576.

## Zhang L, Ge Y, Gao Q, Zhao F, Cheng T, Li H, Xia Y. Machine Learning-Based Radiomics Nomogram

With Dynamic Contrast-Enhanced MRI of the Osteosarcoma for Evaluation of Efficacy of Neoadjuvant
Chemotherapy. Front oncol 2021; 11: 758921.

## Zhang L, Kang L, Li G, Zhang X, Ren J, Shi Z, et al. Computed tomography-based radiomics model

for discriminating the risk stratification of gastrointestinal stromal tumors. Radiol Med (Torino) 2020;
125(5): 465-73.

## Zhang L, Ren Z. Comparison of CT and MRI images for the prediction of soft-tissue sarcoma

grading and lung metastasis via a convolutional neural networks model. Clin Radiol 2020; 75(1): 64-9.

## Zhang L, Yang Y, Wang T, Chen X, Tang M, Deng J, et al. Intratumoral and peritumoral MRI-based

radiomics prediction of histopathological grade in soft tissue sarcomas: a two-center study. Cancer
Imaging 2023; 23(1): 103.

## Zhang M, Tong E, Hamrick F, Lee EH, Tam LT, Pendleton C, et al. Machine-Learning Approach to

Differentiation of Benign and Malignant Peripheral Nerve Sheath Tumors: A Multicenter Study.
Neurosurgery 2021; 89(3): 509-17.

## Zhang M, Tong E, Wong S, Hamrick F, Mohammadzadeh M, Rao V, et al. Machine learning

approach to differentiation of peripheral schwannomas and neurofibromas: A multi-center study. Neurooncol 2022; 24(4): 601-9.

## Zhang QW, Gao YJ, Zhang RY, Zhou XX, Chen SL, Zhang Y, et al. Personalized CT-based radiomics

nomogram preoperative predicting Ki-67 expression in gastrointestinal stromal tumors: a multicenter
development and validation cohort. Clin Transl Med 2020; 9(1): 12.

## Zhang QW, Zhang RY, Yan ZB, Zhao YX, Wang XY, Jin JZ, et al. Personalized radiomics signature to

screen for KIT-11 mutation genotypes among patients with gastrointestinal stromal tumors: a
retrospective multicenter study. J transl med 2023; 21(1): 726.

## Zhang QW, Zhou XX, Zhang RY, Chen SL, Liu Q, Wang J, et al. Comparison of malignancyprediction efficiency between contrast and non-contract CT-based radiomics features in gastrointestinal

stromal tumors: A multicenter study. Clin Transl Med 2020; 10(3): e291.

## Zhang XD, Zhang L, Gong TT, Wang ZR, Guo KL, Li J, et al. A combined radiomic model

distinguishing GISTs from leiomyomas and schwannomas in the stomach based on endoscopic
ultrasonography images. J appl clin med phys 2023; 24(7): e14023.

## Zhang Y, Yue X, Zhang P, Zhang Y, Wu L, Diao N, et al. Clinical-radiomics-based treatment decision

support for KIT Exon 11 deletion in gastrointestinal stromal tumors: a multi-institutional retrospective
study. Front oncol 2023; 13: 1193010.

<!-- Page 81 -->


## Zhang Y, Zhao H, Liu Y, Zeng M, Zhang J, Hao D. Diagnostic Performance of Dynamic Contrast-

Enhanced MRI and 18F-FDG PET/CT for Evaluation of Soft Tissue Tumors and Correlation with Pathology
Parameters. Academic Radiology 2022.

## Zhang Y, Zhu Y, Shi X, Tao J, Cui J, Dai Y, et al. Soft Tissue Sarcomas: Preoperative Predictive

Histopathological Grading Based on Radiomics of MRI. Acad Radiol 2019; 26(9): 1262-8.

## Zhao K, Zhang M, Xie Z, Yan X, Wu S, Liao P, et al. Deep Learning Assisted Diagnosis of

Musculoskeletal Tumors Based on Contrast-Enhanced Magnetic Resonance Imaging. J Magn Reson
Imaging 2022; 56(1): 99-107.

## Zhao S, Su Y, Duan J, Qiu Q, Ge X, Wang A, Yin Y. Radiomics signature extracted from diffusionweighted magnetic resonance imaging predicts outcomes in osteosarcoma. J Bone Oncol 2019; 19:

100263.

## Zhao Y, Feng M, Wang M, Zhang L, Li M, Huang C. CT Radiomics for the Preoperative Prediction

of Ki67 Index in Gastrointestinal Stromal Tumors: A Multi-Center Study. Front oncol 2021; 11: 689136.

## Zheng F, Yin P, Liang K, Wang Y, Hao W, Hao Q, Hong N. Fusion Radiomics-Based Prediction of

Response to Neoadjuvant Chemotherapy for Osteosarcoma. Acad Radiol 2024; 31(6): 2444-55.

## Zheng F, Yin P, Liang KW, Liu T, Wang YJ, Hao WH, et al. Comparison of Different Fusion Radiomics

for Predicting Benign and Malignant Sacral Tumors: A Pilot Study. Journal of Imaging Informatics in
Medicine 2024.

## Zheng J, Liao Q, Chen X, Hong M, Mazzocca A, Urbini M, et al. Development and validation of a

computed tomography-based radiomics signature to predict "highest-risk" from patients with high-risk
gastrointestinal stromal tumor. J gastrointest oncol 2024; 15(1): 125-33.

## Zheng J, Xia Y, Xu A, Weng X, Wang X, Jiang H, et al. Combined model based on enhanced CT

texture features in liver metastasis prediction of high-risk gastrointestinal stromal tumors. Abdom Radiol
2022; 47(1): 85-93.

## Zheng Y, Chen L, Liu M, Wu J, Yu R, Lv F. Prediction of Clinical Outcome for High-Intensity Focused

Ultrasound Ablation of Uterine Leiomyomas Using Multiparametric MRI Radiomics-Based Machine
Leaning Model. Front oncol 2021; 11: 618604.

## Zheng Y, Chen L, Liu M, Wu J, Yu R, Lv F. Nonenhanced MRI-based radiomics model for

preoperative prediction of nonperfused volume ratio for high-intensity focused ultrasound ablation of
uterine leiomyomas. Int J Hyperthermia 2021; 38(1): 1349-58.

## Zhong J, Zhang C, Hu Y, Zhang J, Liu Y, Si L, et al. Automated prediction of the neoadjuvant

chemotherapy response in osteosarcoma with deep learning and an MRI-based radiomics nomogram.
Eur Radiol 2022; 32(9): 6196-206.

## Zhou Y, Zhang J, Chen J, Yang C, Gong C, Li C, Li F. Prediction using T2-weighted magnetic

resonance imaging-based radiomics of residual uterine myoma regrowth after high-intensity focused
ultrasound ablation. Ultrasound Obstet Gynecol 2022; 60(5): 681-92.

<!-- Page 82 -->


## Zhou Z, Xie P, Dai Z, Wu J. Self-supervised tumor segmentation and prognosis prediction in

osteosarcoma using multiparametric MRI and clinical characteristics. Comput Methods Programs Biomed
2024; 244: 107974.

## Zhu MP, Ding QL, Xu JX, Jiang CY, Wang J, Wang C, Yu RS. Building contrast-enhanced CT-based

models for preoperatively predicting malignant potential and Ki67 expression of small intestine
gastrointestinal stromal tumors (GISTs). Abdom Radiol 2022; 47(9): 3161-73.

## Zhuo M, Chen X, Guo J, Qian Q, Xue E, Chen Z. Deep Learning-Based Segmentation and Risk

Stratification for Gastrointestinal Stromal Tumors in Transabdominal Ultrasound Imaging. J Ultrasound
Med 2024; 43(9): 1661-72.

## Zhuo M, Guo J, Tang Y, Tang X, Qian Q, Chen Z. Ultrasound radiomics model-based nomogram for

predicting the risk Stratification of gastrointestinal stromal tumors. Front oncol 2022; 12: 905036.

## Zhuo M, Tang Y, Guo J, Qian Q, Xue E, Chen Z. Predicting the risk stratification of gastrointestinal

stromal tumors using machine learning-based ultrasound radiomics. J Med Ultrason (2001) 2024; 51(1):
71-82.

## Tables

**Table (Page 6):**

| Primary soft-tissue and bone tumours (STBT) are among the rarest neoplasms in humans, |
|---|
| comprising both benign and malignant lesions. Malignant STBT, i.e. sarcoma, account for |
| approximately 1% of all neoplasms.1 These tumours may occur at any age and almost any |
| anatomical site, arising from cells of the connective tissue, including muscles, fat, blood |
| vessels, cartilage, and bones.2 The rarity of STBT, along with their diverse subtypes and varied |
| clinical behaviour, poses substantial challenges in accurate diagnosis and prognosis. |
|  |


**Table (Page 6):**

|  |
|---|
| Artificial intelligence (AI) has become increasingly prevalent in medical image analysis. Over |
| the last 7 years, the number of FDA-approved medical imaging AI products for radiology has |
| substantially increased.6 However, while medical imaging AI research in STBT has also |
| substantially increased, there are no products developed for STBT among the FDA-approved |
| list.7 Hence, instead of purely developing novel technological solutions, more research should |
| focus on aligning with areas of unmet clinical need. |
|  |


**Table (Page 23):**

| Author | Short description | Validation | Performance (Proportion, 95% CI) |
|---|---|---|---|
| Ye et al. [31] | A multi-task machine learning model using learned imaging features (deep learning) for the segmentation, detection, and differentiation of malignant and benign primary bone tumours, as well as bone infections, leveraging multi-modal inputs including T1-weighted MRI, T2- weighted MRI, and clinical data. | External validation 53 patients from 1 centre | AUC: 0∙900 (0∙773–1∙000) Accuracy: 0∙783 (0∙581–0∙903) Sensitivity: 0∙756 (0∙552–0∙886) Specificity: 0∙886 (0∙764–0∙950) |
| Dong et al. [32] | Machine learning model using learned imaging features (deep learning) differentiating gastrointestinal stromal tumours (GISTs) and leiomyomas on endoscopic ultrasonography. | External validation 241 patients from 1 centre Prospective validation 59 patients from 1 centre | External validation AUC: 0∙948 (0∙921–0∙969) Accuracy: 0∙917 (0∙875–0∙946) Sensitivity: 0∙903 (0∙834–0∙945) Specificity: 0∙930 (0∙872–0∙963) Precision: 0∙919 (0∙853–0∙957) NPV: 0∙915 (0∙855–0∙952) Prospective validation (for GISTs and leiomyomas, respectively) AUC: 0∙865 (0∙782–0∙977) and 0∙864 (0∙762–0∙966) Accuracy: 0∙865 and 0∙864 Sensitivity: 0∙897 and 0∙857 Specificity: 0∙833 and 0∙871 Precision: 0∙839 and 0∙857 NPV: 0∙893 and 0∙881 |
| Xie et al. [33] | Machine learning model using learned imaging features (deep learning) to classify histological types of primary bone tumours on radiographs. | External validation 89 patients from 1 centre | AUC: 0∙873 (0∙812–0∙920) Accuracy: 0∙687 (0∙614–0∙783) Sensitivity: 0∙572 (0∙457–0∙685) Specificity: 0∙916 (0∙893–0∙938) |
| Xu et al. [34] | Machine learning model using a combination of hand-crafted and model-learned imaging features to differentiate between retroperitoneal lipomas and well-differentiated liposarcomas based on MDM2 status on contrast-enhanced CT. | External validation 63 patients from 2 centre | AUC: 0∙861 (0∙737–0∙985) Accuracy: 0∙810 |
| Arthur et al. [35] | Machine learning model using hand- crafted imaging features classifying histological type and tumour grade in retroperitoneal sarcoma on CT. | External validation 89 patients from 8 centres* | Histology and Grade AUC: 0∙928 and 0·882 Accuracy: 0·843 and 0·823 Sensitivity: 0·923 and 0·800 Specificity: 0·829 and 0·848 Precision: 0·480 and 0·865 NPV: 0·984, 0·778 |
| Guo et al. [36] | Machine learning model using a combination of hand-crafted and model-learned imaging features to classify histological grade and predict prognosis of soft-tissue tumours on MRI. | External validation 125 and 44 patients from 2 centres Prospective validation 12 patients from 1 centre | External validation (Centre 1 and Centre 2) AUC: 0∙860 (0∙787–0∙916) and 0∙838 (0∙696–0∙932) Accuracy: 0∙840 and 0∙750 Sensitivity: 0∙835 and 0∙840 Specificity: 0∙794 and 0∙737 Hazard ratio: 4∙624 (1∙924–11∙110) and 2∙920 (0∙603–14∙150) Prospective validation AUC: 0∙819 (0∙501–0∙974) Accuracy: 0∙667 Sensitivity: 0∙667 Specificity: 1∙000 |


**Table (Page 24):**

| Gitto et al. [37] | Machine learning model using hand- crafted imaging features differentiating atypical cartilaginous tumour and grade II chondrosarcoma of long bones on MRI. | External validation 65 patients from 1 centre | AUC: 0∙94 for atypical cartilaginous tumour and 0∙90 for grade II chondrosarcomal Accuracy: 0∙92 Sensitivity: 0∙92 Precision: 0∙92 |
|---|---|---|---|
| Von Schaky et al. [38] | Machine learning model using hand- crafted imaging features to distinguish between benign and malignant bone lesions on radiography. | External validation 96 patients from 1 centre | AUC: 0∙90 Accuracy: 0∙75 (0∙65–0∙83) Sensitivity: 0∙90 (0∙74–0∙98) Specificity: 0∙68 (0∙55–0∙79) Precision: 0∙57 (0∙42–0∙71) NPV: 0∙94 (0∙82–0∙99) |
| Gitto et al. [39] | Machine learning model using hand- crafted imaging features differentiating atypical cartilaginous tumour and high-grade chondrosarcoma of long bones on radiography. | External validation 30 patients from 1 centre | AUC: 0∙90 Accuracy: 0∙80 Sensitivity: 0∙89 Specificity: 0∙67 |
| Cao et al. [40] | Machine learning model using hand- crafted imaging features predicting the local recurrence after surgical treatment of primary dermatofibrosarcoma protuberans, based on MRI. | External validation 42 patients from 1 centre | AUC: 0∙865 (0∙732–0∙998) for 3- year and 0∙931 (0∙849–1∙00) for 5 year C-index: 0∙866 (0∙786–0∙946) |
| Yang et al. [41] | Machine learning model using hand- crafted imaging features predicting progression-free survival after imatinib therapy in patients with liver metastatic gastrointestinal stromal tumours on multi-sequence MRI. | External validation 45 patients from 1 centre | AUC: 0∙766 for 1-year, 0∙776 for 3- year, and 0∙893 for 5-year C-index: 0∙718 (0∙618–0∙818) |
| Chen et al. [42] | Machine learning model using hand- crafted imaging features predicting pathologic response to neoadjuvant chemotherapy (NAC) in patients with osteosarcoma on MRI. | External validation 34 patients from 3 centres | AUC: 0∙842 (0∙793–0∙883) Accuracy: 0∙765 ± 0∙020† Sensitivity: 0∙739 ± 0∙032† Specificity: 0∙909 ± 0∙026† |
| Liang et al. [43] | Machine learning model using a combination of hand-crafted and model-learned imaging features for predicting lung metastases in patients with soft-tissue sarcoma on MRI. | External validation 126 patients from 2 centre | AUC: 0∙833 (0∙732–0∙933) Accuracy: 0∙897 Sensitivity: 0∙474 Specificity: 0∙972 Precision: 0∙750 NPV: 0∙912 |
| Kang et al. [44] | Machine learning model using learned imaging features (deep learning) to predict preoperative risk of gastrointestinal stromal tumours on CT. | External validation 388 patients from 1 centre | Low-malignant, intermediate- malignant, and high-malignant AUC: 0∙87 (0∙83–0∙91), 0∙64 (0∙60– 0∙68), and 0∙85 (0∙81–0∙89) Accuracy: 0∙81 (0∙77–0∙85), 0∙75 (0∙71–0∙79), and 0∙77 (0∙73–0∙81) Sensitivity: 0∙72 (0∙64–0∙79), 0∙24 (0∙14–0∙34), and 0∙79 (0∙73–0∙85) Specificity: 0∙86 (0∙83–0∙90), 0∙86 (0∙82–0∙90), and 0∙75 (0∙70–0∙81) |
| He et al. [45] | Machine learning model using learned imaging features (deep learning) for classification of benign, intermediate or malignant primary bone tumours on radiography. | External validation 291 patients from 2 centre | AUC: 0∙877 (0∙833–0∙918) benign vs not benign and 0∙916 (0∙877– 0∙949) malignant vs not malignant Accuracy: 0∙734 |
| Peeken et al. [46] | Machine learning model using hand- crafted imaging features from different timepoints (delta radiomics) predicting pathologic complete response to neoadjuvant therapy in high grade soft tissue sarcoma of trunk and extremity, based on MRI. | External validation 53 patients from 1 centre | AUC: 0∙75 (0∙56–0∙93) Accuracy: 0∙86 Balanced accuracy: 0∙57 Sensitivity: 0∙20 Specificity: 0∙95 Precision: 0∙33 NPV: 0∙90 |
| Forema n et al. [47] | Machine learning model using hand- crafted imaging features predicting the MDM2 gene amplification status in order to differentiate between atypical lipomatous tumours (ALT) and lipomas on MRI. | External validation 50 patients from 1 centre | AUC: 0∙88 (0∙85–0∙91) Accuracy: 0∙76 Sensitivity: 0∙70 Specificity: 0∙81 |


**Table (Page 25):**

| Spraker et al. [48] | Machine learning model using hand- crafted imaging features predicting overall survival of grade II and III soft-tissue tumours on MRI. | External validation 61 patients from 1 centre | Sensitivity: 0∙79 Specificity: 0∙68 C-index: 0∙78 Hazard ratio: 2∙4 |
|---|---|---|---|
| Fradet et al. [49] | Machine learning model using a combination of hand-crafted and model-learned imaging features predicting malignancy for lipomatous soft-tissue lesions on MRI. | External validation 60 patients from 35 centres | AUC: 0∙80 Specificity: 0∙63 |
| Gitto et al. [50] | Machine learning model using hand- crafted imaging features differentiating atypical cartilaginous tumours and high-grade chondrosarcomas of long bones on CT. | External validation 36 patients from 1 centre | AUC: 0∙784 Accuracy: 0∙75 |


**Table (Page 31):**

| Categories |  | N | Mean CLAIM score | Mean FUTURE -AI score | AUC range | Accuracy range | Sensitivity range | Specificity range |
|---|---|---|---|---|---|---|---|---|
| Outcome type | Diagnosis | 12 | 41·2 | 8·7 | 0·78-0·95 | 0·69-0·92 | 0·57-1·00 | 0·63-0·93 |
|  | Prognosis | 7 | 39·0 | 7·9 | 0·64-0·93 | 0·77-0·90 | 0·20-0·79 | 0·68-0·97 |
|  | Both | 1 | 40·0 | 9·0 | 0·82-0·86 | 0·67-0·84 | 0·67-0·84 | 0·74-1·00 |
| Disease typea | Bone tumour | 8 | 41·4 | 8·1 | 0·78-0·94 | 0·69-0·92 | 0·57-0·90 | 0·67-0·92 |
|  | Soft-tissue tumour | 9 | 38·9 | 8·6 | 0·75-0·93 | 0·67-0·90 | 0·20-1·00 | 0·63-1·00 |
|  | GIST | 3 | 42·0 | 8·7 | 0·64-0·95 | 0·75-0·92 | 0·24-0·90 | 0·75-0·93 |
| Method type | Hand-crafted features | 11 | 39·5 | 7·6 | 0·75-0·94 | 0·75-0·92 | 0·20-0·92 | 0·67-0·95 |
|  | Model-learned features | 6 | 42·8 | 9·3 | 0·64-0·95 | 0·67-0·92 | 0·24-0·90 | 0·74-1·00 |
|  | Combined hand- crafted and model- learned features | 3 | 38·3 | 9·5 | 0·80-0·86 | 0·80-0·86 | 0·47-1·00 | 0·63-0·97 |


**Table (Page 45):**

| Database searched | Platform | Coverage period |
|---|---|---|
| Medline ALL | Ovid | 1946 – 07/2024 |
| Embase | Embase.com | 1971 - 07/2024 |
| Web of Science Core Collection* | Web of Knowledge | 1975 - 07/2024 |
| Cochrane Central Register of Controlled Trials** | Wiley | 1992 - 07/2024 |
| Additional Search Engines: Google Scholar*** |  |  |
| Total |  |  |


**Table (Page 53):**

| General Information |  |
|---|---|
| (sub)Section | Values |
| Rater |  |
| Year |  |
| Journal |  |
| Type imaging |  |
| prognosis / diagnosis | 0. Diagnosis 1. Prognosis 2. Both |
| Which disease? | Soft tissue tumour/ Bone tumour/ GIST |
| Used publicly available dataset | 0. No 1. Yes 2. Both |
| Retrospective vs prospective | 0. Retrospective 1. Prospective |
| Signle centre vs multi-centre | 0. Single-centre 1. Multi-centre |
| Data available | 0. No 1. Upon request 2. Yes |
| Code Available | 0. No 1. Upon request 2. Yes |
| Methods | 0. Not learning 1. Hand crafted features 2. Model-learned features 3. Combined |


**Table (Page 54):**

| FUTURE-AI Checklist |  |  |  |  |  |  |
|---|---|---|---|---|---|---|
| Principle | no. | Recommendations | Low ML-TRL | High ML-TRL | Description | Scoring criteria |
| F | 1 | Define any potential sources of bias from an early stage | ++ | ++ | Bias in medical AI is application-specific. At the design phase, the development team should identify possible types and sources of bias for their AI tool. These may include group attributes (e.g. sex, gender, age, ethnicity, socioeconomics, geography), the medical profiles of the individuals (e.g. with comorbidities or disability), as well as human biases (e.g. data labelling, data curation, or the selection of the input features). | 0) No potential biases were discussed prior to AI development, 0.5) Potential biases in at least 1 group (group attributes, medical profile, human biases) were discussed prior to AI development, 1) Potential biases in all 3 groups were discussed prior to AI development. |
|  | 2 | Collect data on individuals’ attributes, when possible | + | + | To identify biases and apply measures for increased fairness, relevant attributes of the individuals, such as sex, gender, age, ethnicity, risk factors, comorbidities or disabilities, should be collected. This should be subject to informed consent and approval by ethics committees to ensure an appropriate balance between the benefits for non-discrimination and risks for re-identification. | 0) No relevant attributes of the patient were collected; 0.5) At least the two attributes in the list collected; (list :sex OR gender, age, ethnicity, risk factors(as 1 item), comorbidities or disabilities) 1) More than two attributes in the list were collected, OR with other attributes |
|  | 3 | Evaluate potential biases and bias correction measures | + | ++ | When possible, i.e. the individuals’ attributes are included in the data, bias detection methods should be applied by using fairness metrics. To correct for any identified biases, mitigation measures should be applied (e.g. data re-sampling, bias-free representations, equalised odds post-processing) and tested to verify their impact on both the tool’s fairness and the model’s accuracy. Importantly, any potential bias should be documented and reported to inform the end-users and citizens (see Traceability 2). | 0) Biases were neither investigated nor corrected for, 0.5) Biases were investigated and reported, 1) Biases were also corrected for by mitigation measures (In case of no biases found, 3 also applies) |
| U | 1 | Define intended clinical settings and cross-setting variations | ++ | ++ | At the design phase, the development team should specify the clinical settings in which the AI tool will be applied (e.g. primary healthcare centres, hospitals, home care, low vs. high-resource settings, one or multiple countries), and anticipate potential obstacles to universality (e.g. differences in clinical definitions, medical equipment or IT infrastructures across settings). | 0) The clinical setting was not reported 0.5) Clinical setting outlined (e.g. primary healthcare centres, hospitals, home care, low vs. high- resource settings, one or multiple countries) 1) Clinical setting outlined and potential obstacles to universality discussed (e.g. differences in clinical definitions, medical equipment or IT infrastructures across settings) |
|  | 2 | Use community-defined standards (e.g. clinical definitions, technical standards) | + | + | To ensure the quality and interoperability of the AI tool, it should be developed based on existing community-defined standards. These may include clinical definitions, medical ontologies (e.g. SNOMED CT,10 OMOP11), interface standards (e.g. DICOM, FHIR HL7), data annotations, evaluation criteria, and technical standards (e.g. IEEE13 or ISO14). | Are community defined standards used: 0) No 1) Yes |
|  | 3 | Evaluate using external datasets and/or multiple sites | ++ | ++ | To assess generalisability, technical validation of the AI tools should be performed with external datasets that are distinct from those used for training. These may include reference or benchmarking datasets which are representative for the task in question (i.e. approximating the expected real-world variations). Except for AI tools intended for single centres, the clinical evaluation studies should be performed at multiple sites to assess performance and interoperability across clinical workflows. If the tool’s generalisability is limited, mitigation measures (e.g. transfer learning or domain adaptation) should be considered, applied and tested. | 0) This study only used single center data --> no external validation; 0.5) Evaluation was performed using external dataset from one other site (or same source, e.g. public available); 1) Evaluation was performed using external dataset from multiple sites; |
|  | 4 | Evaluate and demonstrate local clinical validity | + | ++ | Clinical settings vary in many aspects, such as populations, equipment, clinical workflows, and end-users. Hence to ensure trust at each site, the AI tools should be evaluated for their local clinical validity. In particular, the AI tool should fit the local clinical workflows and perform well on the local populations. If the performance is decreased when evaluated locally, re-calibration of the AI model should be performed (e.g., through model fine-tuning or retraining). | 0) local clinical validity has not been discussed, or was not applicable (e.g. AI tool was not deployed outside of research setting/externally) 0.5) local clinical validity has been discussed and evaluated, 1) local clinical validity has been discussed and evaluated and if needed, mitigation strategies have been deployed to deal with this local clinical validity. |
| T | 1 | Implement a risk management process throughout the AI lifecycle | + | ++ | Throughout the AI tool’s lifecycle, the development team should analyse potential risks, assess each risk’s likelihood, effects and risk-benefit balance, define risk mitigation measures, monitor the risks and mitigations continuously, and maintain a risk management file. The risks may include those explicitly covered by the FUTURE-AI guiding principles (e.g. bias, harm), but also application-specific risks. Other risks to consider include human factors that may lead to misuse of the AI tool (e.g. not following the instructions, receiving insufficient training), application of the AI tool to individuals who are not within the target population, use of the tool by others than the target end-users (e.g. technician instead of physician), hardware failure, incorrect data annotations or input values, and adversarial attacks. Mitigation measures may include warnings to the users, system shutdown, re-processing of the input data, the acquisition of new input data, or the use of an alternative procedure or human judgement only. | 0) Risks regarding the AI lifecycle have not been described, 0.5) Risks regarding the AI lifecycle have been described, 1) A risk managment plan has been described in order to circumvent risks during the AI lifecycle. |
|  | 2 | Provide documentation (e.g. technical, clinical) | ++ | ++ | To increase transparency, traceability, and accountability, adequate documentation should be created and maintained for the AI tool, which may include (i) an AI information leaflet to inform citizens and healthcare professionals about the tool’s intended use, risks (e.g. biases) and instructions for use; (ii) a technical document to inform AI developers, health organisations and regulators about the AI model’s properties (e.g. hyperparameters), training and testing data, evaluation criteria and results, biases and other limitations, and periodic audits and updates; (iii) a publication based on existing AI reporting standards, and (iv) a risk management file (see Traceability 1). | 0) No documentation has been provided, 0.5) Documentation about 1-2 points (see decription) have been provided), 1) Documentation about 3-4 points (see description have been provided) |
|  | 3 | Define mechanisms for quality control of the AI inputs and outputs | + | ++ | The AI tool should be developed and deployed with mechanisms for continuous monitoring and quality control of the AI inputs and outputs, such as to identify missing or out-of-range input variables, inconsistent data formats or units, incorrect annotations or data pre-processing, and erroneous or implausible AI outputs. For quality control of the AI decisions, uncertainty estimates should be provided (and calibrated) to inform the end-users on the degree of confidence in the results. Finally, when necessary, model updates should be applied to address any identified limitations and enhance the AI models over time. | 0) No monitoring or quality control measures of either inputs or outputs have beenimplemented 0.5) Monitoring or quality control measures have been implemented for either the inputs or outputs 1) Monitoring or quality control measures have been implemnted for both inputs and outputs. |
|  | 4 | Implement a system for periodic auditing and updating | + | ++ | The AI tool should be developed and deployed with a configurable system for periodic auditing, which should define site-specific datasets and timelines for periodic evaluations (e.g. every year). The periodic auditing should enable the identification of data or concept drifts, newly occurring biases, performance degradation or changes in the decision making of the end-users. Accordingly, necessary updates to the AI models or AI tools should be applied. | 0) No discussion of audit or future updating; 0.5) Need of audit or potential updates is discussed; 1) Methods for auditing or updating are discussed. |
|  | 5 | Implement a logging system for usage recording | + | ++ | To increase traceability and accountability, an AI logging system should be implemented to trace the user’s main actions in a privacy-preserving manner, specify the data that is accessed and used, record the AI predictions and clinical decisions, and log any encountered issues. Time-series statistics and visualisations should be used to inspect the usage of the AI tool over time. | 0) No system has been devised for logging usage of the AI tool; 1) A system has been devised for logging usage of the AI tool |
|  | 6 | Establish mechanisms for AI governance | + | ++ | After deployment, the governance of the AI tool should be specified. In particular, the roles of risk management, periodic auditing, maintenance, and supervision should be assigned, such as to IT teams or healthcare administrators. Furthermore, responsibilities for AI-related errors should be clearly specified among clinicians, healthcare centres, AI developers, and manufacturers. Accountability mechanisms should be established, incorporating both individual and collective liability, alongside compensation and support structures for patients impacted by AI errors. | 0) AI has no governance mechanism (see question for examples), 1) There is at least 1 governance mechanism implemented/described |
| U | 1 | Define intended use and user requirements from an early stage | ++ | ++ | The AI developers should engage clinical experts, end-users (e.g. patients, physicians) and other relevant stakeholders (e.g. data managers, administrators) from an early stage, to compile information on the AI tool’s intended use and end-user requirements (e.g. human-AI interfaces), as well as on human factors that may impact the usage of the AI tool (e.g. ergonomics, intuitiveness, experience, learnability). | 0) Only 1 type of stakeholder (e.g. AI developers/departments) was present for AI development, and no intended use and user requirement was described, 0.5) Only 1 type of stakeholder (e.g. AI developers/departments) was present for AI development, however intended use and end-user requirement was described; OR, multiple stakeholders were present for AI development, no intented use or requirement was decribed; 1) Multiple stakeholders were present for AI development and compiled information on the AI tool’s intended use and end-user requirements. |
|  | 2 | Establish mechanisms for human-AI interactions and oversight | + | ++ | Based on the user requirements, the AI developers should implement interfaces to enable end- users to effectively utilise the AI model, annotate the input data in a standardised manner, and verify the AI inputs and results. Given the high-stakes nature of medical AI, human oversight is essential and increasingly required by policy makers and regulators. Human-in-the-loop mechanisms should be designed and implemented to perform specific quality checks (e.g. to flag biases, errors or implausible explanations), and to overrule the AI predictions when necessary. | 0) The AI tool has no human oversight, 1) The AI tool provides at least one interface or human-in-the-loop mechanism to involve human oversight |
|  | 3 | Provide training materials and activities (e.g. tutorials, hands-on sessions) | + | ++ | To facilitate best usage of the AI tool, minimise errors and harm, and increase AI literacy, the developers should provide training materials (e.g. tutorials, manuals, examples) in accessible language and/or training activities (e.g. hands-on sessions), taking into account the diversity of end-users (e.g. clinical specialists, nurses, technicians, citizens or administrators). | Has any training material been provided: 0) No 1) Yes |
|  | 4 | Evaluate user experience and acceptance with independent end-users | + | ++ | To facilitate adoption, the usability of the AI tool should be evaluated in the real world with representative and diverse end-users (e.g. with respect to sex, gender, age, clinical role, digital proficiency, (dis)ability). The usability tests should gather evidence on the user’s satisfaction, performance and productivity. These tests should also verify whether the AI tool impacts the behaviour and decision making of the end-users. | 0) The AI tool was not evaluated for user experience, 0.5) The AI tool was evaluated for user experience by 1 user 1) The AI tool was evaluated for user experience by multiple independent end-users. |
|  | 5 | Evaluate clinical utility and safety (e.g. effectiveness, harm, cost- benefit) | + | ++ | The AI tool should be evaluated for its clinical utility and safety. The clinical evaluations of the AI tool should show benefits for the clinician (e.g. increased productivity, improved care), for the patient (e.g. earlier diagnosis, better outcomes), and/or for the healthcare organisation (e.g. reduced costs, optimised workflows), when compared to the current standard of care. Additionally, it is important to show that the AI tool is safe and does not cause harm to individuals (or specific groups), such as through a randomised clinical trial. | 0) The AI tool was not evaluated for clinical utility and safety. 0.5) The AI tool was evaluated for clinical utility and safety. 1) The AI tool was evaluated for clinical utility and safety in a Randomized Control Trial (RCT). |
| R | 1 | Define sources of data variation from an early stage | ++ | ++ | At the design phase, an inventory should be made of the application-specific sources of variation that may impact the AI tool’s robustness in the real world. These may include differences in equipment, technical fault of a machine, data heterogeneities during data acquisition or annotation, and/or adversarial attacks. | 0) Data acquisiton and possible variation of the data source to the real world has not been discussed, 0.5) Data acquisiton and possible variation of the data source to the real world has been discussed, 1) Extensive reporting, including reference to the literature and other primary sources, about how the data may vary (or does not vary) to the real world data |
|  | 2 | Train with representative real-world data | ++ | ++ | Clinicians, citizens and other stakeholders are more likely to trust the AI tool if it is trained on data that adequately represents the variations encountered in real-world clinical practice. Hence, the training datasets should be carefully selected, analysed and enriched according to the sources of variation identified at the design phase (see Robustness 1). | 0) The representative of the training data to the real-world data was not evaluated; 0.5) The representative of the training data to the real-world data was evaluated; 1) The representative of the training data to the real-world data was evaluated and enriched accordingly; Note "real world data" has to be data taken from a cinical setting |
|  | 3 | Evaluate and optimise robustness against real-world variations | ++ | ++ | Evaluation studies should be implemented to evaluate the AI tool’s robustness (including stress tests and repeatability tests), by considering all potential sources of variation (see Robustness 1), such as data-, equipment-, clinician-, patient- and centre-related variations. Depending on the results, mitigation measures should be implemented to optimise the robustness of the AI model, such as regularisation, data augmentation, data harmonisation, or domain adaptation. | 0) The AI tool has not been evaluated against real-world data (test data), 0.5) The AI tool has been evaluated against real-world data (test data), 1) The AI tool has been evaluated against real-world data (test data) and the AI tool's robustness has been optimized (if applicable) using mitigation methods. |
| E | 1 | Define the need and requirements for explainability with end-users | ++ | ++ | At the design phase, it should be established if explainability is required for the AI tool. In this case, the specific requirements for explainability should be defined with representative experts and end-users, including (i) the goal of the explanations (e.g. global description of the model’s behaviour vs. local explanation of each AI decision), (ii) the most suitable approach for AI explainability, and (iii) the potential limitations to anticipate and monitor (e.g. over-reliance of the end-users on the AI decision). | 0) Explainibility has not been defined at the design phase, 0.5) At least one of the following areas is discussed: (i) the goal of the explanations (e.g. global description of the model’s behaviour vs. local explanation of each AI decision), (ii) the most suitable approach for AI explainability and (iii) the potential limitations to anticipate and monitor (e.g. over-reliance of the end-users on the AI decision). 1) more than one of the areas has been identified and discussed |
|  | 2 | Evaluate explainability with end-users (e.g. correctness, impact on users) | + | + | The explainable AI methods should be evaluated, first quantitatively by using in silico methods to assess the correctness of the explanations, then qualitatively with end-users to assess their impact on user satisfaction, confidence and clinical performance. The evaluations should also identify any limitations of the AI explanations (e.g. they are clinically incoherent or sensitive to noise or adversarial attacks, they unreasonably increase the confidence in the AI-generated results). | 0) Explainability has not been defined or not evaluated with end-users, 0.5) Explainability has been evaluated in silico OR with end users involved in the development 1) Explainability has been evaluated with end-users not involved in the development (e.g. clinical users - radiologists/clinicians, radiographers etc...) |
| General | 1 | Engage inter-disciplinary stakeholders throughout the AI lifecycle | ++ | ++ | Throughout the AI tool’s lifecycle, the AI developers should continuously engage with inter-disciplinary stakeholders, such as healthcare professionals, citizens, patient representatives, expert ethicists, data managers and legal experts. This interaction will facilitate the understanding and anticipation of the needs, obstacles and pathways towards acceptance and adoption. | Was a multi-disciplinary team involved in AI development (more than 1 department) 0) No 1) Yes |
|  | 2 | Implement measures for data privacy and security | ++ | ++ | Adequate measures to ensure data privacy and security should be put in place throughout the AI lifecycle. These may include privacy-enhancing techniques (e.g. differential privacy, encryption), data protection impact assessment and appropriate data governance after deployment (e.g. logging system for data access, see Traceability 5). If de-identification is implemented (e.g. pseudonymisation, k-anonymity), the balance between the health benefits for citizens and the risks for re-identification should be carefully assessed and considered. Furthermore, the manufacturers and deployers should implement and regularly evaluate measures for protecting the AI tool against malicious attacks, such as by using system-level cybersecurity solutions or application-specific defence mechanisms (e.g. attack detection or mitigation). | Has data privacy and security been discussed (e.g. data anonymization, clearance from medical ethical committee, (waived) informed consent)? 0) No 1) Yes |
|  | 3 | Implement measures to address identified AI risks | ++ | ++ | At the development stage, the development team should define an AI modelling plan that is aligned with the application-specific requirements. After implementing and testing a baseline AI model, the AI modelling plan should include mitigation measures to address the challenges and risks identified at the design stage (see Fairness 1 to Explainability 1). These may include measures to enhance robustness to real-world variations (e.g. regularisation, data augmentation, data harmonisation, domain adaptation), ensure generalisability across settings (e.g. transfer learning, knowledge distillation), and correct for biases across subgroups (e.g. data re- sampling, bias-free representation, equalised odds post-processing). | 0) No mitigation measures to address challenges and risks identified at the design stage have been reported. 0.5) One mitigation measure (1 of F3, R2 or R3) to either enhance robusteness to real-world variation or ensure generalisability across settings or to correct for biases across subgroups has been taken. 1) Two or more mitigation measures (F3, R2, R3) to enhance robusteness to real-world variation and/or ensure generalisability across settings and/or correct for biases across subgroups have been taken. |
|  | 4 | Define adequate evaluation plan (e.g. datasets, metrics, reference methods) | ++ | ++ | To increase trust and adoption, an appropriate evaluation plan should be defined (including test data, metrics and reference methods). First, adequate test data should be selected for assessing each dimension of trustworthy AI. In particular, the test data should be well separated from the training to prevent data leakage. Furthermore, adequate evaluation metrics should be carefully selected, taking into account their benefits and potential flaws. Finally, benchmarking with respect to reference AI tools or standard practice should be performed to enable comparative assessment of model performance. | 0) Evaluation was not conducted using standardized and best practices, 0.5) A seperate test set was used to evaluate the AI tool and reported on using appropriate evaluation metrics (e.g. sensitivity and specificity) 1) The AI tool was compared to current standard practice (i.e. evaluation metrics on test set should be compared to same metrics for current clinical tests - so for example how did it compare to radiologists) |
|  | 5 | Identify and comply with applicable AI regulatory requirements | + | ++ | The development team should identify the applicable AI regulations depending on the relevant jurisdictions. This should be done at an early stage to anticipate regulatory obligations based on the medical AI tool’s intended classification and risks. | Have AI regulatory requirements been identified? 0) No 1) Yes |
|  | 6 | Investigate and address ethical issues | + | ++ | In addition to the well-known ethical issues that arise in medical AI (e.g. privacy, transparency, equity, autonomy), AI developers, domain specialists and professional ethicists should identify, discuss and address all application-specific ethical, social and societal issues as an integral part of the development and deployment of the AI too. | Have ethical issues been investigated? 0) No 1) Yes |
|  | 7 | Investigate and address social and societal issues | + | + | Social and societal implications should be considered and addressed when developing the AI tool, to ensure a positive impact on citizens and society. Relevant issues include the impact of the AI tool on the working conditions and power relations, on the new skills (or deskilling) of the healthcare professionals and citizens, and on future interactions between citizens, health professionals and social carers. Furthermore, for environmental sustainability, AI developers should consider strategies to reduce the carbon footprint of the AI tool. | Have social and societal implications been investigated? 0) No 1) Yes |


**Table (Page 55):**

| CLAIM Checklist |  |  |  |  |
|---|---|---|---|---|
| (sub)section | CLAIM item # | Criterion | Explanation | Values |
| Title or Abstract | 1 | The study identifies the AI methodology, or specifies the category of technology used (eg. deep learning). | Specify the AI techniques used in the study—such as “vision transformers” or “deep learning”—in the article’s title and/or abstract; use judgment regarding the level of specificity. | 0. Not specified 1. Specified |
| Abstract | 2 | Summary of study design, methods, results, and conclusions | The abstract should present a succinct structured summary of the study’s design, methods, results, and conclusions. Include relevant detail about the study population, such as data source and use of publicly available datasets, number of patients or examinations, number of studies per data source, modalities and relevant series or sequences. Provide information about data partitions and level of data splitting (eg, patient- or image-level). Clearly state if the study is prospective or retrospective and summarize the statistical analysis that was performed. The reader should clearly understand the primary outcomes and implication of the study’s findings, including relevant clinical impact. Indicate whether the software, data, and/or resulting model are publicly available (including where to find more details, if applicable). | 0. Not included 1. Included |
| Introduction | 3 | Scientific and/or clinical background, including the intended use and role of the AI approach | Considered as complete if at least a simple sentence was provided to introduce the medical context and rationale for developing/validating the model: The current practice should be explicitly mentioned. (1) Describe the study’s rationale, goals, and anticipated impact. (2) resent a focused summary of the pertinent literature to describe current practice and highlight how the investigation changes or builds on that work. Guide readers to understand the context for the study, the underlying science, the assumptions underlying the methodology, and the nuances of the study. | 0. Not provided 1. Provided |
|  | 4a | Study aims and objectives | Define clearly the clinical or scientific question to be answered; avoid vague statements or descriptions of a process. Limit the chance of post hoc data dredging by specifying the study’s hypothesis a priori. The study’s hypothesis and objectives should guide appropriate statistical analyses, sample size calculations, and whether the hypothesis will be supported or not. | 0. Not provided 1. Provided |
|  | 4b | Study hypothesis |  | 0. Not provided 1. Provided |
| Methods |  |  |  |  |
| Study Design | 5 | Prospective or retrospective study | Indicate if the study is retrospective or prospective. Evaluate predictive models in a prospective setting, if possible. | 0. Not documented 1. Documented |
|  | 6 | Study goal | Considered as complete if at least a simple sentence was provided involving one of the points below: (1) Define the study’s goal, such as model creation, exploratory study, feasibility study, or noninferiority trial. For classification systems, state the intended use, such as diagnosis, screening, staging, monitoring, surveillance, prediction, or prognosis. (2) Describe the type of predictive modeling to be performed, the target of predictions, and how it will solve the clinical or scientific question. | 0. Not documented 1. Documented |
| Data | 7a | Data source | State the source(s) of data including publicly available datasets and/or synthetic images; provide links to data sources and/or images, if available. Describe how well the data align with the intended use and target population of the model. Provide links to data sources and/or images, if available. Authors are strongly encouraged to deposit data and/or software used for modeling or data analysis in a publicly accessible repository. | 0: Not documented 1: Documented |
|  | 7b | Data collection institutions |  | 0. Not documented 1. Documented |
|  | 7c | Institutional review board approval |  | 0. Not documented 1. Documented |
|  | 7d | Participant consent |  | 0. Not documented 1. Documented |
|  | 8 | Inclusion and exclusion criteria | Specify inclusion and exclusion criteria, such as location, dates, patient-care setting, demographics (eg, age, sex, race), pertinent follow-up, and results from prior tests. Define how, where, and when potentially eligible participants or studies were identified. Indicate whether a consecutive, random, or convenience series was selected. | 0. Not provided 1. Provided |
|  | 9a | Data pre-processing steps with details | Describe preprocessing steps to allow other investigators to reproduce them. Specify the use of normalization, resampling of image size, change in bit depth, and/or adjustment of window/level settings. If applicable, state whether the data have been rescaled, threshold-limited (“binarized”), and/or standardized. Specify processes used to address regional formatting, manual input, inconsistent data, missing data, incorrect data type, file manipulations, and missing anonymization. State any criteria used to remove outliers. When applicable, include description for libraries, software (including manufacturer name and location and version numbers), and all option and configurations settings. | 0. Not provided 1. Provided |
|  | 9b | Normalization / resampling in preprocessing |  | 0. Not documented 1. Documented |
|  | 9c | Whether data have been rescaled, threshold- limited (“binarized”), and/or standardized |  | 0. Not documented 1. Documented |
|  | 9d | Specify how the following issues were handled: regional format, manual input, inconsistent data, missing data, wrong data types, file manipulations, and missing anonymization. |  | 0. Not documented 1. Documented |
|  | 9e | Define any criteria to remove outliers |  | 0. Not documented 1. Documented |
|  | 9f | Specify the libraries, software (including manufacturer name and location), and version numbers, and all option and configuration settings employed. |  | 0. Not documented 1. Documented |
|  | 10 | Selection of data subsets | State whether investigators selected subsets of raw extracted data during preprocessing. For example, describe whether investigators selected a subset of the images, cropped portions of images, or extracted segments of a report. If this process is automated, describe the tools and parameters used. If performed manually, describe the training of the personnel and criteria used in their instruction. Justify how this manual step would be accommodated in context of the clinical or scientific problem, describing methods of scaling processes, when applicable. | 0. Not documented 1. Documented |
|  | 11 | De-identification methods | Describe the methods used to de-identify data and how protected health information has been removed to meet U.S. (HIPAA), EU (AI Act, EU Health Data Space, GDPR), or other relevant regulations | 0. Not defined 1. Defined |
|  | 12 | How missing data were handled | Clearly describe how missing data were handled. For example, describe processes to replace them with approximate, predicted, or proxy values. Discuss biases that imputed data may introduce. | 0. Not defined 1. Defined |
|  | 13 | Image acquisition protocol | Describe the image acquisition protocol, such as manufacturer, MRI sequence, ultrasoundfrequency, maximum CT energy, tube current, slice thickness,scan range, and scan resolution; include all relevant parametersto enable reproducibility of the stated methods. | 0. Not defined 1. Defined |
|  | 14 | Definition of method(s) used to obtain reference standard | Include a clear, detailed description of methods used to obtain the reference standard; readers should be able to replicate the reference standard based on this description. Include specific, standard guidelines provided to all annotators. Avoid vague descriptions, such as “white matter lesion burden,” and use precise definitions, such as “lesion location (periventricular, juxtacortical, infratentorial), size measured in three dimensions, and number of lesions as measured on T2/FLAIR MR brain images.” Provide an atlas of examples to annotators to illustrate subjective grading schemes (eg, mild, moderate, severe) and make that information available for review. | 0. Not defined 1. Defined |
|  | 15 | Rationale for choosing the reference standard | Describe the rationale for choice of the reference standard versus any alternatives. Include information on potential errors, biases, and limitations of that reference standard. | 0. Not documented 1. Documented |


**Table (Page 56):**

| Ground Truth | 16 | Source of reference standard annotations | Considered as complete if all points below were provided: (1) Specify the source of reference standard annotations, citing relevant literature if annotations from existing data resources are used (2)Specify the number of human annotators and their qualifications (eg, level of expertise, subspecialty training). (3) Describe the instructions and training given to annotators; include training materials as a supplement | 0. Not documented 1. Documented |
|---|---|---|---|---|
|  | 17 | Annotation of test set | Detail the steps taken to annotate the test set with sufficient detail so that another investigator could replicate the annotation. Include any standard instructions provided to annotators for a given task. Specify software used for manual annotation, including the version number. Describe if and how imaging labels were extracted from imaging reports or electronic health records using natural language processing or recurrent neural networks. This information should be included for any step involving manual annotation, in addition to any semiautomated or automated annotation. | 0. Not documented 1. Documented |
|  | 18 | Measurement of inter- and intrarater variability of features described by annotators | Describe the methods to measure inter- and intra- rater variability, and any steps taken to reduce or mitigate this variability and/or resolve discrepancies between annotators. | 0. Not documented 1. Documented |
| Data Partitions | 19 | How data were assigned to partitions; specify proportions | Specify how data were partitioned for training, model optimization (often termed “tuning” or “validation”), and testing. Indicate the proportion of data in each partition (eg, 80/10/10) and justify that selection. Indicate if there are any systematic differences between the data in each partition, and if so, why and how potential class imbalance was addressed. If using openly available data, use established splits to improve comparison to the literature. If freely sharing data, provide data splits so that others can perform model training and testing comparably. | 0. Not documented 1. Documented |
|  | 20 | Level at which partitions are disjoint | Describe the level at which the partitions are disjoint (eg, patient-, series-, image- level). Sets of medical images generally should be disjoint at the patient level or higher so that images of the same patient do not appear in each partition. | 0. Not documented 1. Documented |
| Testing Data | 21 | Intended sample size | Describe the size of the testing set and how it was determined. Use traditional power calculation methods, if applicable, to estimate the required sample size. For classification problems, in cases where there is no algorithm-specific sample size estimation method available, sample size can be estimated for a given area under the curve and confidence interval width | 0. Not documented 1. Documented |
| Model | 22 | Detailed description of model | If novel model architecture is used, provide a complete and detailed structure of the model, including inputs, outputs, and all intermediate layers, in sufficient detail that another investigator could exactly reconstruct the network. For neural network models, include all details of pooling, normalization, regularization, and activation in the layer descriptions. Model inputs must match the form of the preprocessed data. Model outputs must correspond to the requirements of the stated clinical problem, and for supervised learning should match the form of the reference standard annotations. If a previously published model architecture is employed, cite a reference that meets the preceding standards and fully describe every modification made to the model. Cite a reference for any proprietary model described previously, as well. In some cases, it may be more convenient to provide the structure of the model in code as supplemental data. | 0. Not documented 1. Documented |
|  | 23 | Software libraries, frameworks, and packages | Specify the names and version numbers of all software libraries, frameworks, and packages. A detailed hardware description may be helpful, especially if computational performance benchmarking is a focus of the work. | 0. Not documented 1. Documented |
|  | 24 | Initialization of model parameters | Indicate how the parameters of the model were initialized. Describe the distribution from which random values were drawn for randomly initialized parameters. Specify the source of the starting weights if transfer learning is employed to initialize parameters. When there is a combination of random initialization and transfer learning, make it clear which portions of the model were initialized with which strategies. | 0. Not documented 1. Documented |
| Training | 25 | Details of training approach | Describe the training procedures and hyperparameters in sufficient detail to enable another investigator to replicate the experiment. To fully document training, a manuscript should: (a) describe how training data were augmented (eg, types and ranges of transformations for images), (b) state how convergence of training of each model was monitored and what the criteria for stopping training were, and (c) indicate the values that were used for every hyperparameter, including which of these were varied between models, over what range, and using what search strategy. For neural networks, descriptions of hyperparameters should include at least the learning rate schedule, optimization algorithm, minibatch size, dropout rates (if any), and regularization parameters (if any). Discuss what objective function was employed, why it was selected, and to what extent it matches the performance required for the clinical or scientific use case. Define criteria used to select the best- performing model. If some model parameters are frozen or restricted from modification, for example in transfer learning, clearly indicate which parameters are involved, the method by which they are restricted, and the portion of the training for which the restriction applies. It may be more concise to describe these details in code in the form of a succinct training script, particularly for neural network models when using a standard framework. | 0. Not documented 1. Documented |
|  | 26 | Method of selecting the final model | Describe the method and metrics used to select the best-performing model among all the models trained for evaluation against the held-out test set. If more than one model was selected, justify why this was appropriate. | 0. Not documented 1. Documented |
|  | 27 | Ensembling techniques | If the final algorithm involves an ensemble of models, describe each model comprising the ensemble in complete detail in accordance with the preceding recommendations. Indicate how the outputs of the component models are weighted and/or combined. | 0. Not documented 1. Documented |
| Evaluation | 28 | Metrics of model performance | Describe the metrics used to assess the model’s performance and indicate how they address the performance characteristics most important to the clinical or scientific problem. Compare the presented model to previously published models. | 0. Not documented 1. Documented |
|  | 29 | Statistical measures of significance and uncertainty | Considered as complete if all points below were provided: (1) Indicate the uncertainty of the performance metrics’ values, such as with standard deviation and/or confidence intervals. (2) Compute appropriate tests of statistical significance to compare metrics. (3) Specify the statistical software, including version. | 0. Not documented 1. Documented |
|  | 30 | Robustness or sensitivity analysis | Analyze the robustness or sensitivity of the model to various assumptions or initial conditions. | 0. Not documented 1. Documented |
|  | 31 | Methods for explainability or interpretability | If applied, describe the methods that allow one to explain or interpret the model’s results and provide the parameters used to generate them. Describe how any such methods were validated in the current study. | 0. Not documented / NA 1. Documented |
|  | 32 | Evaluation on internal data | Document and describe evaluation performed on internal data. If there are systematic differences in the structure of annotations or data between the training set and the internal test set, explain the differences, and describe the approach taken to accommodate the differences. Document whether there is consistency in performance on the training and internal test sets. | 0. Not described 1. Employed internal test data |
|  | 33 | Testing on external data | Describe the external data used to evaluate the completed algorithm. If no external testing is performed, note and justify this limitation. If there are differences in structure of annotations or data between the training set and the external testing set, explain the differences, and describe the approach taken to accommodate the differences. | 0. Not described 1. Employed external test data |


**Table (Page 57):**

|  | 34 | Clinical trial registration | If applicable, comply with the clinical trial registration statement from the International Committee of Medical Journal Editors (ICMJE). ICMJE recommends that all medical journal editors require registration of clinical trials in a public trials registry at or before the time of first patient enrollment as a condition of consideration for publication. Registration of the study protocol in a clinical trial registry, such as ClinicalTrials.gov or WHO Primary Registries, helps avoid overlapping or redundant studies and allows interested parties to contact the study coordinators. | 0. Not documented 1. Documented |
|---|---|---|---|---|
| Results |  |  |  |  |
| Data | 35 | Flow of participants or cases, using a diagram to indicate inclusion and exclusion | Document the numbers of patients, examinations, or images included and excluded based on each of the study’s inclusion and exclusion criteria. Include a flowchart or alternative diagram to show selection of the initial patient population and those excluded for any reason. | 0. Not documented 1. Documented |
|  | 36 | Demographic and clinical characteristics of cases in each partition | Specify the demographic and clinical characteristics of cases in each partition and dataset. Identify sources of potential bias that may originate from differences in demographic or clinical characteristics, such as sex distribution, underrepresented racial or ethnic groups, phenotypic variations, or differences in treatment. | 0. Not documented 1. Documented |
| Model Performance | 37 | Performance metrics and measures of statistical uncertainty | Considered as complete if at least two points below were provided: (1) Report the final model’s performance on the test partition. (2) Benchmark the performance of the AI model against current standards, such as histopathologic identification of disease or a panel of medical experts with an explicit method to resolve disagreements. (3) State the performance metrics on all data partitions and datasets, including any demographic subgroups. | 0. Not documented 1. Documented |
|  | 38 | Estimates of diagnostic accuracy and their precision | Considered as complete if at least three points below were provided: For classification tasks, (1) include estimates of diagnostic accuracy and their precision, such as 95% confidence intervals. (2) Apply appropriate methodology such as receiver operating characteristic analysis and/or calibration curves. When the direct calculation of confidence intervals is not possible, report non-parametric estimates from bootstrap samples. (3) State which variables were shown to be predictive of the response variable. (4) Identify the subpopulation(s) for which the prediction model worked most and least effectively. (5) If applicable, recognize the presence of class imbalance (uneven distribution across data classes within or between datasets) and provide appropriate metrics to reflect algorithm performance | 0. Not documented 1. Documented |
|  | 39 | Failure analysis of incorrectly classified cases | Considered as complete if at least one points below were provided: Provide information to help understand incorrect results. (1) If the task entails classification into two or more categories, provide a confusion matrix that shows tallies for predicted versus actual categories. (2) Consider presenting examples of incorrectly classified cases to help readers better understand the strengths and limitations of the algorithm. (3) Provide sufficient detail to frame incorrect results in the appropriate medical context. | 0. Not documented 1. Documented |
| Discussion | 40 | Study limitations | Identify the study’s limitations, including those involving the study’s methods, materials, biases, statistical uncertainty, unexpected results, and generalizability. This discussion should follow succinct summarization of the results with appropriate context and explanation of how the current work advances our knowledge and the state of the art. | 0. Not discussed 1. Discussed |
|  | 41 | Implications for practice, including the intended use and/or clinical role | Considered as complete if at least three points below were provided: (1) Describe the implications for practice, including the intended use and possible clinical role of the AI model. (2) Describe the key impact the work may have on the field. (3) Envision the next steps that one might take to build upon the results. (4) Discuss any issues that would impede successful translation of the model into practice. | 0. Not discussed 1. Discussed |
| Other information | 42 | Provide a reference to the full study protocol or to additional technical details | State where readers can access the full study protocol or additional technical details if this description exceeds the journal’s word limit. For clinical trials, include reference to the study protocol text referenced in item 34. For experimental or preclinical studies, include reference to details of the AI methodology, if not fully documented in the manuscript or supplemental material. This information can help readers evaluate the validity of the study and can help researchers who want to replicate the study. | 0. Not access to the full study protocol 1. Provided access to the full study protocol |
|  | 43 | Statement about the availability of software, trained model, and/or data | State where the reader can access the software, model, and/or data associated with the study, includingconditions under which these resources can be accessed. Describe the algorithms and software in sufficient detail to allowreplication of the study. Authors should deposit all computercode used for modeling and/or data analysis into a publiclyaccessible repository. | 0. Not discussed 1. Discussed |
|  | 44 | Sources of funding and other support; role of funders | Specify the sources of funding and other support and the exact role of the funders in performing the study. Indicate whether the authors had independence in each phase of the study. | 0. Not documented 1. Documented |
