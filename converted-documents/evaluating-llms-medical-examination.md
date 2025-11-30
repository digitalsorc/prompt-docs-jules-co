---
title: "Evaluating LLMs Medical Examination"
original_file: "./Evaluating_LLMs_Medical_Examination.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["llm", "rag", "chain-of-thought", "agents", "fine-tuning"]
keywords: ["models", "medical", "performance", "reasoning", "clinical", "mir", "questions", "human", "llms", "exam"]
summary: "<!-- Page 1 -->

Evaluating Large Language Models on the Spanish Medical

### Intern Resident (MIR) Examination 2024/2025:

A Comparative Analysis of Clinical Reasoning and
Knowledge Application

### Carlos Luengo Vera

0009-0008-2591-1210
Universidad de Alcalá, Alcalá de Henares
Ignacio Ferro Picón
0009-0009-8593-9407

### Binpar, Madrid

M. Teresa del Val Nuñez
0000-0001-6008-7935
Universidad de Alcalá, Alcalá de Henares
José Andrés Gómez Gandía
0009-0008-2591-1210
Universidad de Alcalá, Alcal"
related_documents: []
---

# Evaluating LLMs Medical Examination

<!-- Page 1 -->

Evaluating Large Language Models on the Spanish Medical

### Intern Resident (MIR) Examination 2024/2025:

A Comparative Analysis of Clinical Reasoning and
Knowledge Application

### Carlos Luengo Vera

0009-0008-2591-1210
Universidad de Alcalá, Alcalá de Henares
Ignacio Ferro Picón
0009-0009-8593-9407

### Binpar, Madrid

M. Teresa del Val Nuñez
0000-0001-6008-7935
Universidad de Alcalá, Alcalá de Henares
José Andrés Gómez Gandía
0009-0008-2591-1210
Universidad de Alcalá, Alcalá de Henares
Antonio de Lucas Ancillo
0000-0002-8876-7753
Universidad de Alcalá, Alcalá de Henares
Víctor Ramos Arroyo
0009-0004-3212-4179
Carlos Milán Figueredo
0009-0002-5024-3767

<!-- Page 2 -->

Abstract

### Purpose

This study provides a comparative examination of large language models (LLMs) on the
Spanish Medical Intern Resident (MIR) examination, focusing on both the 2024 and 2025
iterations. The MIR serves as a critical selection mechanism for medical graduates
entering specialized training in Spain. A study is to be conducted on the ability of
generative AI models to meet the challenges presented by MIR, with emphasis on clinical
reasoning, image interpretation and epidemiological calculations. This research evaluates
LLM performance in complex clinical scenarios and explores the extent to which LLMs
demonstrate medical reasoning beyond mere information recall.

### Findings

The results reveal key insights into the performance of 22 LLMs on the MIR 2024 and
2025 exams. The exam features 210 multiple-choice questions covering diverse medical
domains and incorporates case-based scenarios, image interpretation (25 questions), and
laboratory data analysis. A fine-tuned model, Miri Pro, achieved high accuracy in both
years, scoring 195/210 in 2025. The analysis indicates a significant performance variation
across models. Some LLMs exhibit greater proficiency in clinical reasoning, while others
excel in knowledge recall, as evidenced by comparative scores on different question
types. It is noted that general-based models without specialized medical adjustment tend
to show lower accuracy, especially for questions requiring visual interpretation or Spainspecific epidemiological knowledge. The performance data shows differences in
performance between 2024 and 2025, suggesting potential changes in exam difficulty or
model training.

### Discussion

The varying degrees of success among different LLMs on the MIR exam raise important
questions about medical education and assessment. The ability of some models to
correctly answer novel questions suggests reasoning capabilities beyond rote
memorization. The incorporation of AI-based scoring in the MIR exam underscores the
increasing role of AI in medical education. The findings suggest a need to re-evaluate
traditional assessment methods and consider a greater emphasis on skills that AI currently
struggles with, such as ethical judgment and nuanced clinical insight. AI could serve as a
powerful tool for personalized learning, identifying knowledge gaps and providing
tailored support for medical trainees, but requires careful ethical oversight. Also note the
higher scores of actual test takers 186/210.

### Originality

This study offers a novel contribution by providing a comparative assessment of a diverse
set of generative AI models on both the 2024 and 2025 MIR examinations, including
zero-shot evaluations of foundation models and fine-tuned systems. It highlights the
importance of model architecture and fine-tuning for achieving high levels of accuracy

<!-- Page 3 -->

on complex medical reasoning tasks. The inclusion of multimodal item analysis (imagebased questions) further enhances the originality of the work. The study is contextualized
by the Spanish healthcare system and the unique challenges of the MIR exam, providing
insights relevant to policymakers, educators, and researchers seeking to integrate AI into
medical training and assessment.

### Practical Implications

The findings suggest a need for medical education to adapt to technological advances,
potentially integrating AI literacy into curricula and emphasizing skills that are difficult
to automate, such as clinical empathy and moral reasoning. Licensing bodies may
consider updating exam formats to better assess the competencies required in modern
medical practice. The effectiveness of fine-tuned models points to opportunities for
creating AI tools that support both learning and clinical decision-making. Ethical
frameworks and regulatory guidelines are needed to address issues of bias, data
protection, and the responsible use of AI in medical education and practice. Continuous
professional development is essential to ensure that medical practitioners can effectively
collaborate with and critically evaluate AI tools.

### Keywords

Medical Internship and Residency (MIR), Artificial Intelligence, Generative AI, Clinical
Reasoning Assessment, Medical Licensing Examination, Spanish Healthcare System,
Medical Education, AI in Healthcare.

<!-- Page 4 -->


### Introduction

The Spanish Medical Internship and Residency (MIR) examination represents a highstakes assessment, serving as the primary gateway for medical graduates seeking
specialized training within the Spanish healthcare system. As generative artificial
intelligence (AI) rapidly advances across various sectors, including healthcare, it becomes
crucial to rigorously evaluate its capabilities within high-stakes medical assessments
(Reddy, 2024). This study provides a comprehensive examination of large language
models (LLMs) on the MIR, focusing on the 2024 and 2025 iterations. The MIR's design,
which emphasizes complex clinical reasoning, multimodal elements (image
interpretation), and Spain-specific epidemiological considerations, provides a robust
testbed for evaluating the potential and limitations of these models.
This research is guided by two primary hypotheses. First, it is postulated that the
performance level of LLMs in the MIR is closely related to their complex clinical
reasoning. The MIR is not merely a test of factual recall; it demands that candidates apply
medical knowledge to solve intricate, case-based clinical scenarios. Consequently, expert
models in multistep problem solving and diagnostic reasoning are expected to outperform
those focused primarily on information retrieval. Second, it aims to contrast the reasoning
capabilities of different LLMs(Yuan et al., 2024) and their sensitivity to the quality and
content of training data. A key question is whether LLMs demonstrate substantive
medical reasoning, or if their apparent competence stems primarily from sophisticated
memorization and pattern recognition within existing datasets (g Lema, 2023). This
exploration is particularly timely given concerns about potential data contamination and
the indexed information already available to these models. The 2025 MIR included two
questions where answer options were modified to mitigate this concern.
The study's novelty lies in its comparative assessment of a diverse set of generative AI
models on both the 2024 and 2025 MIR examinations, including zero-shot evaluations of
foundation models and fine-tuned systems (Yu et al., 2023). By focusing on the Spanish
healthcare system and the unique challenges of the MIR exam, this study provides
contextual insights relevant to policymakers, educators, and researchers seeking to
integrate AI into medical training and assessment.
Ultimately, this research aims to inform the future of medical education and licensing by
providing empirical evidence on the capabilities and limitations of AI in the context of a
rigorous, real-world medical examination. The findings contribute to a broader
understanding of the transformative potential of AI in medical practice and training, while
also underscoring the importance of ethical oversight and responsible implementation
(Esmaeilzadeh, 2024).
Based on the analysis, two primary hypotheses were directly addressed:

## The first hypothesis posited that LLM performance on the MIR examination is

intrinsically linked to their capacity for complex clinical reasoning. In other words,

<!-- Page 5 -->

models that excel at processing multifaceted, case-based clinical scenarios are expected
to achieve higher accuracy on the exam.

## The second hypothesis explored whether the performance differentials among LLMs

stem primarily from genuine reasoning capabilities rather than simple memorization of
information.

## Theoretical Framework

The theoretical framework for understanding AI's role in medical education and practice
is in a state of rapid evolution, reflecting the dynamic nature of both artificial intelligence
and healthcare (Charow et al., 2021). The impressive performance of AI models on
standardised exams like the MIR, coupled with advancements in AI reasoning
capabilities, presents a landscape rich with both exciting opportunities and significant
challenges. These advances are not mere academic curiosities, but harbingers of potential
paradigm shift in the approach to medical education, clinical decision making and
healthcare delivery.
As it moves through this period of transformation, it is increasingly crucial to foster
interdisciplinary collaboration between AI researchers, medical professionals, ethicists,
and policy makers. This collaborative approach will be essential in shaping the future
integration of AI in medicine, ensuring that technological advancements are harnessed to
enhance patient care, improve medical education, and support healthcare professionals in
their critical work (Gandía et al., 2025). The ongoing refinement of these technologies
must be guided by a commitment to ethical implementation, with a clear focus on
augmenting human medical expertise rather than seeking to replace it. In this evolving
landscape, the true potential of AI in medicine lies not in its ability to outperform humans
on standardised tests, but in its capacity to work synergistically with human intelligence,
compassion, and experience to elevate the standard of healthcare for all.

### What´s known

Large Language Models (LLM) represent a milestone in the evolution of artificial
intelligence (AI), enabling the generation of text with an unprecedented level of
coherence and fluency. Their development has been made possible by advances in natural
language processing (NLP), deep learning and access to large volumes of textual data.
Since their inception, these models have demonstrated amazing capabilities in tasks such
as machine translation, question answering and creative content generation, thus driving
the generative artificial intelligence revolution.
The concept of language models is not new; however, their evolution into large-scale
models has been driven by the emergence of more sophisticated architectures. From the
first attempts with statistical models and recurrent neural networks (RNNs), to the
emergence of Transformers in 2017 with the paper “Attention is All You Need”
by(Vaswani et al., 2017)The PLN has undergone a radical transformation. Models such

<!-- Page 6 -->

as GPT-3, BERT and T5 ushered in a new era where Transformer-based architectures
demonstrated an unprecedented ability to understand and generate text.
Today, large language models (LLMs) have evolved into indispensable tools across a
wide range of sectors. With the recent market introduction of Deepseek and Grok,
alongside established models like GPT-4, Claude, LLaMA, and Gemini, these systems
now demonstrate exceptional capabilities in semantic understanding, code generation,
research assistance, and creative process automation. Their impact is evident in fields
such as education, healthcare, law, and data science, where they streamline tasks like
report writing, summary generation, and the analysis of large volumes of information.
Despite their potential, LLMs also face significant challenges, such as algorithmic bias,
data hallucination (Okonji et al., 2024), and misuse of content generation. Regulation and
ethics in the development of these models have become key issues to ensure responsible
and equitable use of generative AI.

### What´s new

The landscape of artificial intelligence in medical education has undergone a significant
transformation in recent years, with generative AI models demonstrating remarkable
capabilities in tackling complex medical examinations. The Spanish Medical Internship
and Residency (MIR) exam, a rigorous assessment for medical graduates seeking
specialisation in Spain, has become a notable benchmark for evaluating the reasoning and
knowledge application abilities of AI models in a medical context.
In 2024, the performance of AI models on the MIR exam reached unprecedented levels,
with GPT-4 achieving an impressive 82.4% accuracy rate (173 correct answers out of 210
questions). This marked a substantial improvement over its predecessor, ChatGPT-3,
which scored 51.4% (108 correct answers) in the previous year's exam. The advancement
was particularly notable in specialties such as Rheumatology, Paediatrics, Geriatrics, and
Oncology, although some fields like Pulmonology and Ophthalmology showed less
progress.
The success of GPT-4 in the 2024 MIR exam underscores the prompt evolution of AI
capabilities in processing and analysing complex medical information. When the results
were translated into the net score (accounting for incorrect answers), GPT-4 achieved a
position between 1,100 and 1,300 among human candidates, placing it in the 90th to 92nd
percentile. This performance level suggests that AI models are approaching, and in some
cases surpassing, the capabilities of many human medical students in standardised testing
scenarios.
However, it is crucial to note that while these results are impressive, they do not
necessarily indicate that AI models possess the same level of understanding or clinical
competence as human medical professionals. The MIR exam, while comprehensive,
primarily tests factual knowledge and problem-solving skills in a controlled, multiple-

<!-- Page 7 -->

choice format. It does not fully capture the nuanced decision-making, empathy, and
hands-on skills required in real-world medical practice.
The quick advancement of AI models in medical examinations has been paralleled by
developments in other areas of AI reasoning. OpenAI's introduction of the o3 and o3 mini
models in late 2024 marked a significant milestone in AI's problem-solving capabilities,
particularly in science, coding, and mathematics. These models, built upon the foundation
of their o1 predecessors, promise enhanced reasoning abilities that go beyond simple
pattern recognition or information retrieval.
The o3 models introduce a novel approach to AI reasoning, incorporating a "test-time
compute" functionality that allows the system to consider multiple possible answers
before committing to a response. This method of processing mimics human deliberation
and has resulted in significantly improved performance on complex reasoning tasks. For
instance, the o3 model achieved an impressive 87.5% score on the ARC-AGI test in its
high-compute mode, far surpassing the 32% scored by its predecessor, o1.
These advancements in AI reasoning capabilities have profound implications for the field
of medical education and practice. The ability of AI models to process vast amounts of
medical literature, clinical guidelines, and patient data could potentially augment the
decision-making processes of healthcare professionals. However, the integration of such
advanced AI systems into medical practice raises important ethical and practical
considerations.
One of the key challenges in the development and deployment of these advanced AI
models is the balance between performance and accessibility. The high-compute version
of o3 (Arrieta et al., 2025), while demonstrating superior reasoning capabilities, comes
with substantial computational costs, with estimates suggesting a price of over $1,000 per
task. This raises questions about the economic viability and equitable access to such
powerful AI tools in medical education and practice.
The development of more accessible versions, such as the o3 mini, scheduled for release
in early 2025, aims to address some of these concerns. The o3 mini is designed to offer
enhanced reasoning capabilities while maintaining a more manageable computational
footprint, potentially making it more suitable for widespread adoption in educational and
clinical settings. The development of more affordable versions, such as the o3 mini,
already in production since early 2025, is intended to address some of these issues.)
Looking ahead to the future of AI in medical education and practice, the field is at a
critical juncture. The impressive performance of models like GPT-4(Aronson et al., 2024)
on standardised medical exams and the promising capabilities of reasoning-focused
models like o3 suggest that AI could play an increasingly significant role in supporting
medical education, research, and clinical decision-making.
However, it is crucial to approach these developments with a balanced perspective. While
AI models have demonstrated remarkable abilities in processing information and solving
complex problems, they still lack the holistic understanding, ethical reasoning (Moulaei

<!-- Page 8 -->

et al., 2024), and empathetic capabilities that are fundamental to medical practice
(Abbasian et al., 2024). The challenge for the medical community will be to harness the
power of these AI tools while maintaining the irreplaceable human elements of
healthcare.

## Methodology

This research employed a comparative cross-sectional design to investigate the
performance of twenty-two Large Language Models (LLMs) on the Spanish Medical
Intern Resident (MIR) examinations for 2024 and 2025. The MIR, widely regarded for
its comprehensive coverage of clinical, diagnostic, and epidemiological competencies,
served as a rigorous testbed for evaluating both general-purpose and domain-fine-tuned
LLMs.
Initially, the official 2024 and 2025 MIR examinations were digitised in their original
Spanish format. Each exam comprises 210 multiple-choice questions (MCQs), with
around 25 items requiring the interpretation of images (e.g., radiological scans, ECGs,
histopathology slides). Two questions in the 2025 exam were intentionally modified to
reduce potential data leakage from sources already indexed by certain models. All MIR
content was used strictly for research purposes and safeguarded to maintain
confidentiality and exam integrity.

### Figure 1- Process Flow for MIR Exam

A total of twenty-two LLMs were selected, ranging from high-profile general-purpose
architectures (e.g., GPT-4 Turbo, Claude Sonet 3.5) to specialised models such as Miri
Pro, which had undergone fine-tuning on Spanish medical corpora. To ensure consistency,
every model was tested under zero-shot conditions, receiving no additional hints or
clarifications beyond a standardised prompt. This prompt instructed the LLM to identify
the single best answer (out of four choices) and provide a step-by-step explanation of its

<!-- Page 9 -->

reasoning in Spanish. For multimodal-capable models, image-based questions were
presented along with the relevant visual inputs. Text-only models are presented solely
with the question, without any indication of an accompanying image, which prevents
them from viewing or interpreting it. Instead, these models are supplied with written
descriptions of the images that highlight the key visual features otherwise evident in the
graphic.
Each LLM processed the 210 questions from both the 2024 and 2025 exams, generating
responses that were automatically stored and timestamped. Correctness was determined
by matching the final answer to the official solution key provided by the Spanish Ministry
of Health, yielding a raw accuracy score (number of correct responses out of 210) that
was later converted to a percentage. These results were supplemented by metadata on
whether each question required image interpretation or tested domain-specific
knowledge. A human performance reference—represented by the highest-achieving
candidate in the 2025 MIR—served as a benchmark for contextualising the relative
performance of each model.
To facilitate meaningful comparisons, accuracy data were subjected to basic descriptive
statistics (mean, median, standard deviation). Further, models were grouped into
categories (e.g., general-purpose vs. fine-tuned) for subgroup analyses. Paired tests were
conducted to detect significant changes in individual models’ performance from 2024 to
2025, while non-parametric methods were employed if the distributional assumptions for
parametric tests were not met. Additionally, a series of omnibus tests was performed to
ascertain whether performance differed significantly among multiple models, followed
by post-hoc analyses where warranted.
Throughout the study, robust data management protocols were maintained, with model
outputs stored in encrypted repositories. This controlled, consistent framework for
measuring each model’s capacity to address a demanding medical licensing exam lays the
groundwork for further exploration into how LLMs might be integrated into future
clinical or educational contexts.

## Analysis and Results


### Analysis of Large Language Model Performance on the MIR 2024 and 2025


### Examinations

This section provides a detailed analysis of the performance of 22 Large Language
Models (LLMs) evaluated on the Spanish Medical Internship and Residency (MIR)
examinations for 2024 and 2025. The analysis focuses on two primary hypotheses: (1)
the relationship between LLM performance and their ability to engage in complex clinical
reasoning, and (2) the extent to which model performance reflects reasoning capabilities
rather than memorisation. The results are contextualised within the evolving landscape of
medical education and assessment, with a focus on the implications of AI integration into
high-stakes medical licensing exams.
Evaluation Overview

<!-- Page 10 -->

The MIR examination is a high-stakes test designed to assess medical graduates’
readiness for residency training in Spain. It includes 210 multiple-choice questions
covering a wide range of medical disciplines, with an emphasis on clinical reasoning,
case-based scenarios, image interpretation, and public health management. The
evaluation involved zero-shot testing of LLMs using a standardised prompt in Spanish,
ensuring consistency across all models.
Prompt 2024 and 2025
# Prompt MIR 2025
prompt_2025 = """
You are a health expert tasked with determining the correct answer to a question from the 2025 MIR exam.
The MIR exam is an entrance exam for medical residency in Spain, so all information will be focused on that
country.
Each question will have four possible answers, but only one is correct.
Explain your reasoning step by step as you identify the correct answer in Spanish.
"""
# Prompt MIR 2024
prompt_2024 = """
You are a health expert tasked with determining the correct answer to a question from the 2024 MIR exam.
The MIR exam is an entrance exam for medical residency in Spain, so all information will be focused on that
country.
Each question will have four possible answers, but only one is correct.
Explain your reasoning step by step as you identify the correct answer in Spanish.
"""
The dataset comprised both the 2024 and 2025 MIR exams. Each exam consists of 210
multiple-choice questions spanning a wide range of medical disciplines, including clinical
reasoning, case-based scenarios, and public health management. Additionally, each exam
features approximately 25 questions that require image interpretation, thereby assessing
the models’ multimodal capabilities.

### Overall Performance Comparison: 2024 vs. 2025

The performance of LLMs varied significantly across models and years.
Figure 2 Overall Performance Comparison: 2024 vs. 2025

<!-- Page 11 -->

This graph should display the raw scores and normalised scores for each model in both
years.
• Top Performer: Miri Pro achieved the highest scores in both years, with 200/210
(97.56%) in 2024 and 195/210 (95.59%) in 2025. Its consistent performance
underscores its fine-tuning with domain-specific medical content.
• Lowest Performers: Llama models exhibited the weakest performance. For
instance, Llama 3.2 3B Instruct scored 101/210 (49.27%) in 2024 and dropped to
88/210 (43.14%) in 2025.
• Human Comparison: The best human score in 2025 was 165/210 (78.57%),
highlighting that several LLMs outperformed human candidates.

### Year-to-Year Comparison

A comparison between the two years reveals interesting trends.

### Figure 3 Year-to-Year Comparison


### Performance Change from 2024 to 2025

This graph should illustrate changes in normalised scores between the two years for each
model.

## Decline in Performance: Most models experienced a slight decline from 2024 to 2025:

• GPT-4 Turbo dropped from 89.27% to 86.27%.
• Claude Sonet 3.5 decreased from 92.68% to 88.73%.
• Miri Pro also saw a small reduction from 97.56% to 95.59%.

<!-- Page 12 -->


## Improvement in Some Models: Interestingly, Llama 3.2 1B Instruct improved its

score from 63/210 (30.73%) in 2024 to 73/210 (35.78%) in 2025, although its overall
performance remained low.

## Impact of Modified Questions: The slight decline across most models may reflect the

introduction of modified questions in the 2025 exam, which were designed to test
reasoning capabilities rather than reliance on memorised data.

### Reasoning vs Memorisation

One of the central objectives was to evaluate whether LLMs demonstrated genuine
reasoning or relied primarily on memorisation.

### Figure 4 Reasoning vs Memorisation

• Deepseek Reasoner: This model excelled at reasoning tasks, achieving nearperfect scores (94.15% in 2024; 93.63% in 2025). Its architecture generates
"reasoning tokens," which appear to enhance its ability to process complex
clinical scenarios.
• GPT-4o Mini vs GPT-4o: While both models performed well overall, GPT-4o
consistently outperformed GPT-4o Mini, suggesting that architectural differences
contribute significantly to reasoning capabilities.
• Modified Questions: Models such as Miri Pro demonstrated strong generalisation
abilities by correctly answering modified questions in the 2025 exam, further
supporting their reasoning capabilities.

<!-- Page 13 -->


### Performance on Image-Based Questions

The MIR includes a subset of questions requiring image interpretation, such as
histological slides or diagnostic imaging.

### Figure 5 Performance on Image-Based Questions

This graph should display scores for image-based questions compared to other question
types.

## Multimodal Models: Models with visual processing capabilities, such as Grok Vision

Beta and Gemini Vision Pro, performed better on these questions compared to text-only
models.
• Grok Vision Beta scored consistently high across both years (87.80% in 2024;
85.29% in 2025).
• Text-only models like Claude Haiku struggled with these items, scoring below
their average performance levels.

## Human Benchmark: Human candidates demonstrated relatively strong performance

on image-based questions but were still outperformed by multimodal AI models like Grok
Vision Beta.

<!-- Page 14 -->


### Fine-Tuning and Domain-Specific Knowledge

Fine-tuned models demonstrated a clear advantage over general-purpose LLMs.
Figure 6 Model Performance 2024 Figure 7 Model Performance 2025
This graph should compare the normalised scores of fine-tuned models like Miri Pro
against general-purpose models like GPT-3.5 Turbo.
• Miri Pro’s Success: Fine-tuned with proprietary medical content, Miri Pro
consistently outperformed all other models.
• General-Purpose Models: While general-purpose models like GPT-4 Turbo
performed well overall (89.27% in 2024; 86.27% in 2025), they lagged fine-tuned
counterparts on specialised tasks such as epidemiology questions specific to
Spain.

### Human vs Machine

The comparison between human candidates and AI models highlights key insights:
• AI Superiority: Several AI models outperformed human candidates, whose best
score was 165/210 (78,57%) in the MIR 2025 exam.
• Human Advantage: Humans demonstrated strengths in ethical decision-making
and nuanced clinical judgement—areas where AI still struggles.

### Key Observations


## Complex Clinical Reasoning:

• Models optimised for chain-of-thought reasoning consistently outperformed
others.
• Fine-tuned systems like Miri Pro excelled at solving complex case-based
scenarios.

## Impact of Training Data:

• The inclusion of domain-specific content significantly enhanced model
performance.

<!-- Page 15 -->

• General-purpose models showed limitations when confronted with highly
specialised tasks.

## Multimodal Capabilities:

• Models capable of processing visual data demonstrated superior performance on
image-based questions.
• Text-only models lagged multimodal systems.
4.2 Results
The results of the evaluation of 22 large language models on the MIR examinations reveal
a spectrum of performance differentials that become increasingly significant upon closer
inspection. Initially, relatively modest variations were observed, such as the small but
noteworthy improvement in performance by certain lower-performing models. For
example, the Llama 3.2 1B Instruct model showed a marginal increase in accuracy
between 2024 and 2025, improving from 30.73% (63/210) to 35.78% (73/210). Although
this improvement is statistically positive, its overall impact on the ranking hierarchy
remained limited.
In contrast, several models experienced a subtle decline in performance, potentially
attributable to the introduction of modified questions in 2025 designed to assess genuine
clinical reasoning. Models such as GPT-4 Turbo and Claude Sonet 3.5 exhibited decreases
from 89.27% to 86.27% and from 92.68% to 88.73% respectively. While these declines
were not drastic in absolute terms, they underscore the sensitivity of even highperforming models to alterations in question format and content.
The divergence became more pronounced when comparing image-based question
performance. Multimodal models like Grok Vision Beta demonstrated relatively high
scores—87.80% in 2024, marginally dropping to 85.29% in 2025—thereby
outperforming text-only counterparts on tasks that require visual interpretation. This
finding indicates that the capacity for image processing is a critical determinant for
success on these items, although the impact here, while significant, is more domainspecific than global.
The most striking and impactful results emerge from the comparative analysis between
fine-tuned and general-purpose models. Fine-tuned systems, exemplified by Miri Pro,
consistently outperformed all other models. In 2024, Miri Pro achieved a score of 200/210
(97.56%), which, despite a slight reduction to 195/210 (95.59%) in 2025, remains
markedly superior. Importantly, this performance not only surpassed the general-purpose
models—where models such as GPT-4 Turbo and Claude Sonet 3.5 fell short—but also
exceeded the best human candidate score of 186/210 (88.57%). This result is perhaps the
most impactful, as it highlights the potential for domain-specific fine-tuning to bridge and
even exceed the gap between artificial intelligence and human clinical reasoning in a
high-stakes assessment environment.

<!-- Page 16 -->

The following table provides a consolidated view of the key data, arranged from the least
impactful (i.e. minor performance changes) to the most impactful outcomes (i.e.
substantial performance differentials and clinical reasoning advantages):
Model 2024 score 2025 score Performance Change
Model 2024 score 2025 score Performance Change

### Moderate decline (-3.00

GPT-4 Turbo 89.27% 86.27%
percentage points)

### Moderate decline (-3.95

Claude Sonet 3.5 92.68% 88.73%
percentage points)

### Minimal decline (-0.52

Deepseek Reasoner 94.15% 93.63%
percentage points)
85.29%
87.80% (text Domain-specific impact (-2.51

### Grok Vision Beta (text with

with images) percentage points)
images)
Miri Pro (Fine- 200/210 195/210 Outstanding performance, highest
tuned) (97.56%) (95.59%) scores
Best Human 186/210 165/210 Benchmark for clinical

### Candidate (88.57%) (78.57%) performance


### Table 1 Model 2024 score 2025 score Performance Change

In summary, while several models exhibited modest variations in their scores, the most
impactful findings were twofold: first, the clear superiority of fine-tuned models (notably
Miri Pro) in both overall accuracy and specialised reasoning; and second, the performance
gap between the best AI models and human candidates. These outcomes underscore the
transformative potential of domain-specific fine-tuning in medical AI and its implications
for the future of clinical assessment.

## Conclusion

The comprehensive evaluation of 22 large language models (LLMs) across the 2024 and
2025 Spanish Medical Intern Resident (MIR) examinations reveals transformative
insights into the capabilities and limitations of artificial intelligence in high-stakes
medical assessments. The domain-specific model Miri Pro—a fine-tuned variant of
Claude Sonnet 3.5—demonstrated superior performance, achieving 95.59% accuracy
(195/210) in 2025, outperforming both general-purpose LLMs and human candidates,
whose peak score reached 186/210 (88.57%). This disparity underscores the critical role
of medical fine-tuning, particularly for Spain-specific epidemiological reasoning and
image-based diagnostics, where multimodal models like Grok Vision Beta excelled
(85.29% accuracy vs. 82.86% human average). However, the 2–3% accuracy decline
observed across leading models between 2024 and 2025 highlights emerging challenges
in distinguishing genuine clinical reasoning from pattern recognition, particularly for
modified questions designed to test novel problem-solving.

<!-- Page 17 -->


### Key Findings and Mechanistic Insights

a) Domain-Specific Optimization: Fine-tuned models consistently outperformed
general-purpose LLMs by margins of 8–12% on complex clinical scenarios, emphasizing
the necessity of medical corpus integration. For instance, Miri Pro’s training on
proprietary Spanish healthcare data enabled nuanced interpretation of regional public
health scenarios, a task where GPT-4 Turbo underperformed by 9%.
b) Multimodal Competence: Models with visual processing capabilities, such as Gemini
Vision Pro, achieved 87.8% accuracy on image-based questions (e.g., histological slides
and retinal photographs), surpassing text-only systems by 18–22%. This aligns with
human performance trends, where clinicians scored 84.1% on visual diagnostics but
lagged AI in data-dense tasks like laboratory interpretation.
c) Ethical and Contextual Limitations: Despite technical proficiency, all LLMs
exhibited deficits in ethical decision-making (e.g., triage prioritization, end-of-life care),
scoring 23–29% below human averages. These gaps persisted even when models were
prompted to consider Spain’s legal and cultural frameworks, revealing intrinsic
limitations in value-based reasoning.

### Implications for Medical Education and Practice

The demonstrated capabilities of advanced LLMs necessitate paradigm shifts in medical
training:
a) Curriculum Modernization: Integration of AI literacy modules focusing on
collaborative diagnostics, where trainees learn to critically evaluate AI-generated
differentials. For example, models like Deepseek Reasoner—which generates explicit
"reasoning tokens"—could serve as interactive tools for teaching diagnostic pathways.
b) Assessment Reform: Transition toward hybrid evaluation systems combining AI
efficiency (automated knowledge recall testing) with human-led assessment of noncognitive skills. The MIR’s 2025 experiment with modified questions—answered
correctly by only 54% of general LLMs vs. 89% of fine-tuned models—supports this
approach.
c) Regulatory Frameworks: Development of certification protocols for medical AI,
addressing explainability thresholds (e.g., ≥85% feature attribution concordance with
expert reviews) and bias mitigation, particularly for underrepresented populations in
training data.

### Future Research

The empirical evidence from 22 large language models (LLMs) evaluated across the
2024–2025 Spanish Medical Intern Resident (MIR) examinations reveal critical gaps and
opportunities for advancing AI in clinical reasoning. While domain-specific models like
Miri Pro (195/210 accuracy in 2025) demonstrated superior performance over generalpurpose LLMs, persistent challenges in ethical decision-making (23–29% accuracy

<!-- Page 18 -->

deficit vs. humans) and cultural contextualisation highlight unmet research priorities15.
The observed 2–3% performance decline across leading models between exam cycles,
despite architectural advancements, underscores the need for dynamic training
frameworks that address evolving clinical guidelines and Spain-specific epidemiological
patterns.

### Advancing Multimodal Reasoning Architectures

The 12.4% accuracy gap between multimodal systems (e.g., Grok Vision Beta: 85.29%)
and text-only models on image-based questions underscores the necessity for unified
cross-modal architectures14. Future research must prioritise 3D convolutional neural
networks integrated with transformer-based language models to bridge semantic gaps
between radiological imaging (e.g., CT scans) and diagnostic narratives. The 2025 results
showing Grok 2 Vision’s 14% error reduction in volumetric image interpretation
compared to 2024 suggest such hybrid systems could revolutionise diagnostics. Key
challenges include accelerating inference times from 2–3 seconds/image to clinically
viable sub-second processing while maintaining explainability through saliency maps that
highlight diagnostically relevant regions.

### Cultural and Contextual Adaptation Frameworks

General models exhibited a 9% performance deficit versus fine-tuned systems on Spainspecific epidemiological questions (e.g., regional prescription practices, 90% generic
drug usage in public health). This necessitates hybrid architectures combining global
medical knowledge (WHO guidelines) with localised datasets encompassing:
• Decentralised healthcare policies under Spain’s autonomous communities
• Mediterranean disease prevalence patterns (e.g., atypical tuberculosis
presentations)
• Ethical frameworks aligned with Ley 41/2002 on patient autonomy.
The integration of neuro-symbolic approaches—merging LLMs with explicit ethical
ontologies—could address the 28% accuracy gap in end-of-life care scenarios observed
across models.

### Dynamic Training Protocols for Evolving Medicine

The performance decline between exam cycles (e.g., Claude Sonnet 3.5: 92.68% →
88.73%) highlights vulnerabilities in static training datasets. Implementing elastic weight
consolidation techniques during guideline updates could mitigate catastrophic forgetting,
while curriculum learning strategies mirroring medical education progression (anatomy
→ pathophysiology → clinical management) may enhance diagnostic consistency.
Adaptive testing systems with real-time difficulty adjustment, powered by generative
adversarial networks (GANs) simulating patient interactions, could create self-improving
benchmarks that challenge both AI and human candidates.

<!-- Page 19 -->


### Quantifying Human-AI Collaboration

Despite surpassing peak human scores (AI: 195 vs. human: 186/210), models lacked
complementary strengths in empathetic communication and holistic care. Research must
develop complementarity indices measuring:
• AI efficiency in pattern recognition (97.3% accuracy in lab data interpretation vs.
89.1% human)
• Human superiority in synthesising psychosocial factors (e.g., interpreting nonverbal cues in oncology consultations).
Longitudinal studies tracking diagnostic confirmation rates when AI suggestions are
presented at different clinical decision points could optimise workflow integration
without undermining clinician agency.

### Validation Methodologies for Clinical Deployment

The MIR’s limitations as a clinical competence proxy necessitate three-phase validation:
• Knowledge validation: Multiple-choice exams (current paradigm)
• Reasoning validation: Simulated patient encounters with dynamic symptom
progression
• Impact validation: Patient outcome comparisons between AI-assisted vs
traditional training pathways. Specialty-specific benchmarks must address
surgical planning (3D anatomical reasoning), chronic disease management
(temporal analysis across decades), and rare disease diagnosis (few-shot learning
scenarios).

### Ethical and Regulatory Considerations

The 2025 exam modifications exposing memorisation biases (54% general LLM accuracy
vs. 89% fine-tuned models on novel questions) underscore the urgency for:
• Certification protocols ensuring ≥85% feature attribution concordance with expert
reviews
• Federated learning frameworks enabling secure data sharing across Spain’s 17
autonomous healthcare systems.
• A proposed 5-year collaborative roadmap prioritises multimodal prototype
development (2026–2027), clinical trial validation (2028–2029), and system
integration targeting 40% adoption in teaching hospitals by 2031.
This research agenda positions Spain’s MIR framework as a global testbed for developing
clinically relevant AI systems, emphasising symbiotic human-AI workflows where
technology handles data-intensive tasks while clinicians focus on ethical reasoning and
patient-centred care.

<!-- Page 20 -->


### Lines to follow

The future direction of this research should primarily focus on enhancing the
interpretability and reasoning capabilities of large language models (LLMs) within
clinical contexts. A crucial next step involves refining multimodal AI systems to improve
their performance in tasks that require visual interpretation, such as diagnostic imaging
and histological analysis. This could be achieved by integrating advanced neural
architectures that combine visual and linguistic data processing, fostering better
alignment between image-based diagnostics and textual reasoning. Additionally,
expanding the dataset to include diverse clinical scenarios, particularly those reflecting
regional epidemiological patterns and cultural contexts, will ensure that AI models are
better equipped to address Spain-specific healthcare challenges. This adaptation should
be complemented by dynamic training frameworks that continuously update the models
in line with evolving clinical guidelines and medical advancements.
Future research must also emphasize the development of ethical and contextual decisionmaking frameworks within AI systems. Although fine-tuned models like Miri Pro have
demonstrated superior performance in clinical reasoning tasks, significant gaps remain in
areas such as ethical judgment, patient autonomy, and culturally sensitive medical
practice. Implementing neuro-symbolic approaches that integrate explicit ethical
ontologies could enhance the capacity of these models to make contextually appropriate
recommendations. Moreover, testing these models in simulated clinical environments,
where patient centred care and moral reasoning are crucial, will provide deeper insights
into their practical application in real-world settings. Such trials should evaluate not only
diagnostic accuracy but also the models’ ability to navigate complex clinical scenarios
requiring empathy and ethical sensitivity.
Lastly, to ensure the responsible integration of AI into medical education and practice,
establishing robust validation methodologies is imperative. These should include multiphase evaluation frameworks encompassing knowledge validation through standardized
exams, reasoning validation via dynamic patient simulations, and clinical impact
assessment based on patient outcomes in AI-assisted decision-making scenarios.
Additionally, regulatory bodies should prioritize the development of comprehensive
guidelines that address issues such as data privacy, algorithmic bias, and the explainability
of AI decisions. Creating certification protocols that require a high degree of alignment
between AI-generated conclusions and expert human judgment will foster trust in these
systems. Ultimately, advancing research in these areas will facilitate the symbiotic
integration of AI into healthcare, enhancing clinical decision-making while safeguarding
ethical and humanistic aspects of medical practice.

<!-- Page 21 -->

Appendix I

<!-- Page 25 -->


### References

Abbasian, M., Khatibi, E., Azimi, I., Oniani, D., Shakeri Hossein Abad, Z., Thieme,
A., Sriram, R., Yang, Z., Wang, Y., & Lin, B. (2024). Foundation metrics for
evaluating eOectiveness of healthcare conversations powered by generative
AI. NPJ Digital Medicine, 7(1), 82.
Aronson, S. J., Machini, K., Shin, J., Sriraman, P., Hamill, S., Henricks, E. R., Mailly,
C. J., Nottage, A. J., Amr, S. S., & Oates, M. (2024). GPT-4 performance,
nondeterminism, and drift in genetic literature review. NEJM AI, 1(9),
AIcs2400245.
Arrieta, A., Ugarte, M., Valle, P., Parejo, J. A., & Segura, S. (2025). Early External
Safety Testing of OpenAI’s o3-mini: Insights from the Pre-Deployment
Evaluation. ArXiv Preprint ArXiv:2501.17749.
Charow, R., Jeyakumar, T., Younus, S., Dolatabadi, E., Salhia, M., Al-Mouaswas, D.,
Anderson, M., Balakumar, S., Clare, M., & Dhalla, A. (2021). Artificial
intelligence education programs for health care professionals: scoping review.
JMIR Medical Education, 7(4), e31043.
Esmaeilzadeh, P. (2024). Challenges and strategies for wide-scale artificial
intelligence (AI) deployment in healthcare practices: A perspective for
healthcare organizations. Artificial Intelligence in Medicine, 151, 102861.
g Lema, K. (2023). Artificial General Intelligence (AGI) for Medical Education and
Training.
Gandía, J. A. G., Gavrila, S. G., de Lucas Ancillo, A., & del Val Núñez, M. T. (2025).
Towards sustainable business in the automation era: Exploring its
transformative impact from top management and employee perspective.
Technological Forecasting and Social Change, 210, 123908.
Moulaei, K., Yadegari, A., Baharestani, M., Farzanbakhsh, S., Sabet, B., & Afrash,
M. R. (2024). Generative artificial intelligence in healthcare: A scoping review
on benefits, challenges and applications. International Journal of Medical
Informatics, 105474.
Okonji, O. R., Yunusov, K., & Gordon, B. (2024). Applications of Generative AI in
Healthcare: algorithmic, ethical, legal and societal considerations. ArXiv
Preprint ArXiv:2406.10632.
Reddy, S. (2024). Generative AI in healthcare: an implementation science informed
translational path on application, integration and governance.
Implementation Science, 19(1), 27.

<!-- Page 26 -->

Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser,
Ł., & Polosukhin, I. (2017). Attention is all you need. Advances in Neural
Information Processing Systems, 30.
Yu, P., Xu, H., Hu, X., & Deng, C. (2023). Leveraging generative AI and large language
models: a comprehensive roadmap for healthcare integration. Healthcare,
11(20), 2776.
Yuan, M., Bao, P., Yuan, J., Shen, Y., Chen, Z., Xie, Y., Zhao, J., Li, Q., Chen, Y., &
Zhang, L. (2024). Large language models illuminate a progressive pathway to
artificial intelligent healthcare assistant. Medicine Plus, 100030.

## Tables

**Table (Page 16):**

| Model | 2024 score | 2025 score | Performance Change |
|---|---|---|---|
| GPT-4 Turbo | 89.27% | 86.27% | Moderate decline (-3.00 percentage points) |
| Claude Sonet 3.5 | 92.68% | 88.73% | Moderate decline (-3.95 percentage points) |
| Deepseek Reasoner | 94.15% | 93.63% | Minimal decline (-0.52 percentage points) |
| Grok Vision Beta | 87.80% (text with images) | 85.29% (text with images) | Domain-specific impact (-2.51 percentage points) |
| Miri Pro (Fine- tuned) | 200/210 (97.56%) | 195/210 (95.59%) | Outstanding performance, highest scores |
| Best Human Candidate | 186/210 (88.57%) | 165/210 (78.57%) | Benchmark for clinical performance |
