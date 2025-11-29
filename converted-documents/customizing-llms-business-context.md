---
title: "Customizing LLMs Business Context"
original_file: "./Customizing_LLMs_Business_Context.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["llm", "rag", "chain-of-thought", "agents", "fine-tuning"]
keywords: ["doctor", "medical", "human", "model", "doctors", "our", "llm", "consultation", "base", "llms"]
summary: "<!-- Page 1 -->

Customizing Large Language Models for Business

### Context: Framework and Experiments


### Wen Wang1 Zhenyue Zhao2 Tianshu Sun3

1University of Maryland 2Cornell University 3University of Southern California
wenw@umd.edu, njujack@163.com, tianshus@usc.edu
TheadventofLargeLanguageModels(LLMs)hasusheredinanewerafordesignscienceinInformation
Systems, demanding a paradigm shift in tailoring LLMs design for business contexts. We propose and test
anovelframeworktocustomizeLLMsforgen"
related_documents: []
---

# Customizing LLMs Business Context

<!-- Page 1 -->

Customizing Large Language Models for Business

### Context: Framework and Experiments


### Wen Wang1 Zhenyue Zhao2 Tianshu Sun3

1University of Maryland 2Cornell University 3University of Southern California
wenw@umd.edu, njujack@163.com, tianshus@usc.edu
TheadventofLargeLanguageModels(LLMs)hasusheredinanewerafordesignscienceinInformation
Systems, demanding a paradigm shift in tailoring LLMs design for business contexts. We propose and test
anovelframeworktocustomizeLLMsforgeneralbusinesscontextsthataimstoachievethreefundamental
objectives simultaneously: (1) aligning conversational patterns, (2) integrating in-depth domain knowledge,
and (3) embodying theory-driven soft skills and core principles. We design methodologies that combine
domain-specific theory with Supervised Fine Tuning (SFT) to achieve these objectives simultaneously. We
instantiateourproposedframeworkinthecontextofmedicalconsultation.Specifically,wecarefullyconstruct
alargevolumeofrealdoctors’consultationrecordsfromaleadingonlinemedicalconsultationplatformand
avastamountofmedicalknowledgefrommultipleprofessionaldatabases.Additionally,drawingonmedical
theory,weidentifythreesoftskillsandcoreprinciplesofhumandoctors:professionalism,explainability,and
emotionalsupport,anddesignapproachestointegratethesetraitsintoLLMs.Wedemonstratethefeasibility
of our framework using online experiments with thousands of real patients as well as evaluation by domain
expertsandconsumers.ExperimentalresultsshowthatthecustomizedLLMmodelsubstantiallyoutperforms
untunedbasemodelinmedicalexpertiseaswellasconsumersatisfactionandtrustworthiness.Itsignificantly
narrows the gap between untuned language models and human professionals, significantly moving closer
to human-level performance. Additionally, we delve into the characteristics of textual consultation records
and adopt interpretable machine learning techniques to identify what drives the performance gain. Finally,
we showcase the practical value of our model through a decision support system designed to assist human
doctors in a lab experiment with medical professionals. We deploy an online consultation platform and use
ourmodeltogenerateinitialresponses,aidingdoctorsinacopilotfashionduringconsultations.Wefindthat
thecustomizedLLMmodelenhancesdoctors’productivityby53.16%intermsoftimespentandreducesthe
cognitiveloadforhumandoctorsduringconsultations,makingithighlyeffectiveandsuitableforlarge-scale
implementation in practice.
1
4202
yaM
41
]YC.sc[
2v52201.2132:viXra

<!-- Page 2 -->

2

## Introduction

In the ever-evolving landscape of Information Systems, design science has played a pivotal role in
shaping how to tailor technical designs to address complex business needs. This field has witnessed
a wide range of customization and application of various Artificial Intelligence (AI) models for
business contexts and needs. These models range from recommender systems (Zhou et al. 2023a,
Zhang et al. 2020, Yin et al. 2022) to natural language processing (NLP) (Lee et al. 2018, Liu
et al. 2019, Manzoor et al. 2023, Xie et al. 2022), forecasting and predictions (Li et al. 2023a, Sun
et al. 2022, Macha et al. 2023, Ben-Assuli and Padman 2020, Liu et al. 2020), and optimization
algorithms (Wang et al. 2023b, Song and Sun 2023, Kokkodis and Ipeirotis 2021).
The recent advancement of Large Language Models (LLMs) marks a significant milestone in AI,
showing transformative improvement over traditional AI models. LLMs revolutionize and significantly differ from traditional AI models in four key ways. Firstly, they are general-purpose AI
models, adept at a wide variety of tasks such as language understanding, generation, and even reasoning. This contrasts with traditional AI systems, which are generally task-specific, with models
optimizedforsingulartasks.Second,LLMshavesuperiorscaleandlearningcapabilities,capableof
absorbing vast industry data at the trillion level. Third, LLMs specialize in understanding unstructured data (i.e., text), whereas traditional AI systems tend to gear towards processing structured
data. Finally, LLMs revolutionize user interaction by enabling end-to-end conversational engagements, closely simulating real-world human conversations. This represents a significant advance
over the rigid, preset rules, or classifications-based communication of previous AI systems.
Such transformative advancement presents a substantial challenge to the traditional research
paradigm in design science. The conventional approach, characterized by defining specific tasks
or goals like predicting ratings or informativeness levels and creating datasets and models to link
inputs and outputs for these tasks, is becoming increasingly inadequate in the face of these new
developments. The emerging capabilities of LLMs enable the development of highly customized
solutions to function as professional experts with extensive domain expertise. These experts can

<!-- Page 3 -->

3
handle a broad range of tasks within their domains, offering a new generation of user experience services through human-like conversational interactions. Given these new capabilities and the
expanded scope they offer, there is an urgent need for a paradigm shift towards redefining and
adjusting technical designs to better align with business contexts in the LLM era.
Addressingthisgap,ourstudyintroducesanovelframeworkdesignedtotailortechnicaldesignto
businesscontextsintheLLMera.WeareamongthefirsttodemonstratehowtocustomizeLLMsfor
generalbusinesscontextsinInformationSystems.LeveragingLLMs’superiorcapabilities,itenables
customization for various business contexts, such as customer support, medical consultation, legal
assistance, sales and marketing, educational programs, and more. Our goal is to provide a versatile
framework applicable across any business context, marking a significant step forward in aligning
technical advancements with practical business needs.
Our proposed framework consists of two steps. Firstly, we decompose the business value of
customizing LLM for a business context into three fundamental objectives: (i) alignment with
conversational patterns, (ii) in-depth domain knowledge, (iii) soft skills and core principles of a
professional role. These objectives represent the three major gaps between LLMs and a specific
business context and are the main areas we need to customize. Secondly, we design methodologies
to model these objectives simultaneously by combining domain-specific theory with Supervised
Fine Tuning (SFT) in large language models.

### The decomposed three fundamental objectives as follows:

(i) Alignment with conversational patterns: Existing LLMs, such as GPT-4, deviate from the
conversational patterns typical of a professional role in a specific business context. Each business domain possesses its unique conversation pattern with specific communication structures and
norms, reflecting its deep business needs and domain-specific techniques. Taking medical consultation as an example (See Figure 1a for an example of consultation record), human doctors typically
conduct multiple conversational turns to first gather adequate patient information and deeply
understand the health conditions, then offer diagnoses and treatment recommendations, with each

<!-- Page 4 -->

4
conversation having a distinct intention. In contrast, existing LLMs primarily act as single-turn
agents with limited multi-turn questioning capabilities concerning domain-specific requirements
(e.g.,auser’shealthspecificsinthecontextofmedicalconsultation).Forexample,Figure1bshows
a GPT-4 response to a patient inquiry, which largely deviates from the human doctors’ pattern
and often includes many irrelevant details. Failing to align with the conversational patterns of professional roles can compromise reliability and specificity, potentially undermining consumer trust
and experience.
(ii) In-depth domain knowledge: The use of LLMs in specific business domains must uphold an
exceptionally high level of domain-specific knowledge. This is crucial for all contexts to ensure the
accuracy and reliability of the information and recommendations provided. Moreover, it is particularlycriticalinhigh-stakefields,suchashealthcare,legal,andeducation,whereinsufficientdomain
knowledge can lead to serious consequences. In healthcare, for example, without thorough medical
knowledge, AI systems could potentially offer misdiagnoses or suggest inappropriate treatments,
severelyendangeringpatientsafety.Similarly,inthelegaldomain,insufficientlegalknowledgecould
lead to incorrect conclusions or advice, potentially resulting in serious legal ramifications. Thus,
maintaining precise and deep domain knowledge is crucial for the effectiveness and trustworthiness
of LLMs in these specialized contexts.
(iii) Soft skills and core principles of professional roles: Beyond domain knowledge and conversational pattern alignment, it is crucial for LLM to emulate the soft skills and core principles
characteristic of various business domains. This includes non-technical skills, interpersonal competencies, and foundational principles essential for professional excellence. This aspect represents
distinct competencies separate from the previous two objectives. Soft skills and core principles
focus on human-centric abilities, while conversational pattern alignment involves adhering to specific communication structures and norms within a particular professional context and in-depth
domain knowledge pertains to the technical or specialized knowledge required in a field. For example, in the medical field, theory suggests that skills such as professionalism, clear explanations, and

<!-- Page 5 -->

5
emotional support are essential for patient satisfaction and building trust with patients (Wilkinson et al. 2009, Ha and Longnecker 2010, Markides 2011, Walter et al. 2021). These soft traits
contribute significantly to a positive consumer experience and are critical for LLMs to offer an
engaging, satisfactory, and trustworthy experience in each business domain.
Tosimultaneouslyachievethreeobjectives,wedesignmethodologiestointegratedomain-specific
theory with Supervised Fine Tuning in LLMs. Our approach involves creating a comprehensive
SFT dataset, divided into three distinct parts to meet these objectives: (i) A substantial collection
of real-world professional conversation records. This aids LLMs in learning and mimicking the conversational patterns of actual professionals; (ii) Utilization of domain-specific theories to pinpoint
essentialsoftskillsandcoreprinciplesprofessionalsshouldembody.Weleveragethistoselectexemplary conversation records, enabling LLMs to demonstrate these skills and principles; (iii) A vast
array of domain knowledge in the form of question and answer pairs, enhancing the LLMs’ ability
to maintain a high level of domain-specific knowledge. Following dataset construction, we conduct
supervised fine-tuning on open-source LLMs using this dataset. Our method employs the LoRA
(Low-rank Adaptation) fine-tuning strategy, which is widely recognized for its effectiveness (Hu
et al. 2021).
To validate the proposed framework, we instantiate our framework in the context of medical
consultation. The goal is to customize LLMs to closely resemble professional doctors, known as
LLM-doctors, thereby enabling them to potentially assist human doctors in practice. AI-assisted
medical consultations hold tremendous value for the healthcare industry, influencing both patient
experiences and the efficiency of healthcare systems. This industry has experienced rapid growth
and increasing demand in recent years. According to VantageMarketResearch (2023) and StraitsResearch (2023), the market was valued at USD 211.60 million in 2022 and is projected to reach
USD 647.29 million by 2030, growing at a compound annual growth rate (CAGR) of 15% over the
forecast period.
Specifically, we carefully construct a multi-source professional knowledge database for LLMs
customizationinthiscontext.Wecollectalargevolumeofrealdoctors’consultationrecordsfroma

<!-- Page 6 -->

6
(a) Real Doctor Record (b) GPT-4 Response to Patient’s Inquiry

### Figure1 Real doctor vs. GPT-4 Response to Patients’ Inquiry

leadingonlinemedicalconsultationplatformandavastamountofmedicalknowledgefrommultiple
professional databases. Additionally, drawing on medical theory, we identify three key soft skills
and core principles of human doctors: professionalism, explainability, and emotional support, and
design approaches to integrate these theory-driven skills into LLMs.
Then,weadoptmultipleexperiments,includingonlineexperimentandlabexperiment,todemonstrate the effectiveness and practical value of our framework. We conduct a large scale of online
experiment with thousands of real patients to conduct medical consultations, which is followed by
comprehensiveevaluationsregardingmedicalexpertisebymedicalprofessionalsaswellasconsumer
preferences by real consumers, demonstrating the effectiveness and feasibility of our framework.
Additionally, we delve into the characteristics of textual consultation records and adopt interpretable machine learning techniques to identify what drives the performance gain. Finally, we
showcase the practical value of our model through a decision support system designed to assist
human doctors in a lab experiment with medical professionals.

### Our results reveal several compelling findings:

Firstly, we conduct an online experiment with thousands of real patients who had recently felt
unwell and sought medical attention to evaluate the effectiveness of our model. We compare the

<!-- Page 7 -->

7
performance of LLM-doctor with untuned base model as well as human doctors. Our evaluations
from medical expertise perspective, conducted by medical professionals, show that LLM-doctor
significantly outperforms the untuned base model with an +11.68% improvement in professionalism (p<0.001) and a +17.43% improvement in accuracy (p<0.001). Meanwhile, the base model
significantly lags behind human doctors by -13.08% in professionalism (p<0.001) and by -16.9%
in accuracy (p<0.001). Our LLM-doctor more closely matches the medical expertise of human
doctors, with marginally smaller gaps of -2.93% in professionalism (p=0.004) and -2.42% in accuracy (p=0.019). This indicates that our framework significantly narrows the gap between untuned
LLMsandhumandoctors,bringingitclosertohuman-levelperformance.Thisresultisparticularly
significant, as a single LLM-model can approach the capabilities of thousands of human doctors
across different outpatient departments.
The same conclusion applies to consumer preference metrics evaluated by real consumers. From
a consumer satisfaction perspective, the untuned base model performs -27.76% worse than human
doctors (p<0.001), and from a consumer trustworthiness perspective, it is -27.16% worse (p<
0.001). The gap in consumer preferences between the base and human doctors is much larger than
thatinmedicalexpertise.Thisindicatesthattheuntunedbasemodelsignificantlylagsbehindwhen
engaging with consumers in reality, highlighting a potential shortcoming. This also underscores the
need for a framework to improve in this aspect. From this standpoint, LLM-doctor significantly
outperforms the base model with a +28.36% improvement in consumer satisfaction (p<0.001)
and a +27.56% improvement in trustworthiness (p<0.001). It narrows the gap to human doctors’
medical expertise with smaller deficits of -7.27% in satisfaction (p<0.001) and -7.09% in trustworthiness (p<0.001). This further indicates that our framework significantly narrows the gap
between untuned LLMs and human doctors, moving it closer to human-level performance, with an
even stronger improvement from the perspective of consumer preference.
Furthermore, beyond model comparison, we conduct an in-depth interpretability analysis using
interpretablemachinelearningtechniquestounderstandwhathappensinconversationrecordsand

<!-- Page 8 -->

8
where the performance gains come from. We specifically examine which conversational or communication characteristics contribute to these gains. We extract various textual communication and
consultation characteristics, such as whether the consultation demonstrates proactive information
gathering, provides targeted disease diagnosis, offers targeted treatment recommendations, uses
medical terms, engages in multi-round interactions, exhibits a human-like communication style,
demonstrates clarity of response, and shows respect and patience in communication, as well as logical reasoning. We find that the LLM-doctor is much closer to human doctors across the majority
of these textual communication and consultation characteristics, whereas the base model significantly lags behind. This indicates that our framework can profoundly change how LLMs conduct
consultations, including the procedures and communication styles, making them closer to those of
human doctors.
Subsequently, we apply interpretable machine learning model to use the extracted textual characteristics to predict perceived professionalism, accuracy, consumer trustworthiness, and satisfaction. Interestingly, we find that the characteristics contributing to perceived medical expertise
and consumer preference are quite distinct. For example, in terms of accuracy, the top predictors
are targeted disease diagnosis, medical term usage, proactive information gathering, multi-round
interaction,andtargetedtreatmentrecommendation.Forconsumersatisfaction,thetoppredictors
are targeted treatment recommendations, respect and patience in communication, and clarity of
response, among others. This analysis not only confirms the effectiveness of our model but also
enhances our understanding of the essential elements of successful medical consultations from both
medical expertise and consumer experience perspectives.
Last but not least, we demonstrate the practical value of our model by illustrating how it can
assist human doctors in the real world. Specifically, we showcase a decision support use case in
which, during an online consultation, our LLM-doctor can generate an initial response to patients’
queries in a copilot manner. The human doctor can either accept this generated response or edit it
before finalizing and sending it back to the patients. The copilot assistant approach enables human

<!-- Page 9 -->

9
doctors to lead the entire process, maintain control over the final response and conduct quality
assurance,therebymitigatingpotentialerrorsorriskyadvicegeneratedbytheAImodel.Toachieve
this goal, we develop an online consultation platform where our LLM-doctor or base model can be
embedded in the backend, and we conduct a laboratory experiment, inviting experienced doctors
from prestigious hospitals in China to conduct medical consultations with this platform. Results
show that with the aid of the LLM-doctor, human doctors, on average, saved 53.16% of their time
compared to operating without the LLM-doctor during consultation. The base model also saves
human doctors’ time. However, the magnitude is much smaller compared to the LLM-doctor; it
saved only 19.31% of the time compared to doctors working independently. This suggests that our
LLM-doctor has larger potential to enhance the productivity of human doctors compared to the
base model.
Additionally, through a post-hoc survey for human doctors to evaluate their experience with the
LLM-doctor or untuned base model, interestingly, the results show that human doctors generally
perceive the response quality of the LLM-doctor to be higher, and they adopt its responses (either
directly or by modifying, retaining at least 50% of the original content) more frequently than those
ofthebasemodel.Additionally,thedoctorsbelievethattheLLM-doctorcanreducetheircognitive
load during consultations much more than the base model. They also think that the LLM-doctor
can save them time spent during consultations more effectively than the base model. Furthermore,
they perceive the LLM-doctor as having more practical value for large-scale deployment on online
consultation platforms compared to the base model.
Furthermore, through open-ended feedback from human doctors, overall, human doctors think
the base model has salient drawbacks, including providing overly verbose and generic responses, a
lackofpersonalization,andmanyirrelevantdetailswhichmightincreaseanxietyforpatients.These
factors make it less useful for doctors and patients. In contrast, our LLM-doctor can proactively
ask questions and address the key points in consultations and can be directly used by human
doctors during consultations. All these factors demonstrate that our LLM-doctor’s practical value
is greater than that of the base model.

<!-- Page 10 -->

10
Overall,ourcontributionsarefourfold.Firstly,weproposeanovelframeworktocustomizeLLMs
for general business contexts, aiming to achieve three fundamental objectives simultaneously: (1)
aligning conversational patterns, (2) integrating in-depth domain knowledge, and (3) embodying
theory-drivensoftskillsandcoreprinciples.Wedesignmethodologiesthatcombinedomain-specific
theory with Supervised Fine Tuning (SFT) to achieve these objectives. Our framework facilitates
the customization of LLMs to serve as general-purpose professional experts for business purposes,
enhancingdomainexpertise,consumersatisfaction,andtrustworthiness.Secondly,wedemonstrate
the effectiveness of our proposed framework in the context of medical consultations with a largescale online experiment. Our fine-tuned LLM-doctor model significantly outperforms the untuned
basemodelandsubstantiallyreducesthegapbetweenuntunedLLMsandhumandoctors,elevating
LLMs to the level of human experts. Thirdly, we conduct an interpretability analysis to identify
what drives performance gains and the interpretable insights gained enhance our understanding
of the essential elements of successful customization from both technical expertise and consumer
experience perspectives. Finally, we showcase how to use our model in practice and demonstrate
its practical value through a decision support system designed to assist human doctors in a lab
experiment with medical professionals. In summary, our proposed framework offers step-by-step
principles, guidance, and valuable insights for future research on customizing LLMs to address
real-world business problems.

## Literature Review

Our work builds upon the extensive literature on design science, the emerging topic of Generative
AI in information system literature, as well as the emerging literature on customizing LLMs for
real-world applications, all of which we briefly review in this section.

### Design Science in Information Systems

Our study is closely related to design science studies in Information System (IS) literature. The
field of design science has been instrumental in influencing the way technology meets the demands
of intricate business requirements. Within this realm, we have observed a diverse array of adaptations and implementations of different AI models to tackle diverse business queries. One notable

<!-- Page 11 -->

11
area of focus in existing literature is the development of recommendation systems aimed at fulfilling specific business needs. For instance, Yin et al. (2022) address the limitations of traditional
recommendation systems that tend to suggest similar options, by proposing a diversity preferenceaware link recommendation model. Similarly, Zhou et al. (2023b) present a personalized healthcare
recommendation framework, enhancing individualized wellness by matching users with suitable
health interventions.
Another significant area of research involves customizing natural language processing models for
various business applications. For example, Lee et al. (2018) develop an NLP model to evaluate the
content of brand advertisements on social media platforms like Facebook, focusing on informativeness and brand personality traits. Liu et al. (2019) tailor a bidirectional long short-term memory
model for identifying medical terms in YouTube’s healthcare educational videos, categorizing these
videos based on the extent of medical information they present. Furthermore, Xie et al. (2022) and
Yang et al. (2023b) explore the realms of social media and psycholinguistics respectively, with the
former developing a sentiment-enriched deep learning method to analyze medication nonadherence
fromsocialmediaposts,andthelatterproposinganNLP-basedapproachforpersonalitydetection.
Additionally, a third strand of literature focuses on forecasting, prediction, and optimization
in various contexts. This includes Sun et al. (2022) using deep learning to anticipate consumers’
futurepurchasingpathsbyanalyzingtheiromnichannelbehaviors,Machaetal.(2023)introducing
a personalized privacy preservation framework for consumer mobile location data, and Ben-Assuli
andPadman(2020)developingpredictivemodelsforearlyriskassessmentinchronicdiseasepatient
readmissions.Moreover,Chenetal.(2023)andWangetal.(2023b)contributewithatheory-driven
method to predict customer responses in a specific commercial mode and a deep reinforcement
learning framework for optimizing sequential targeting, respectively.
The existing body of work typically adheres to paradigms that define specific tasks or goals, subsequently developing datasets and models to connect inputs with outputs for these tasks. However,
with the transformative capabilities of LLMs, such paradigms are increasingly facing challenges.

<!-- Page 12 -->

12
Our study contributes to this field by introducing a new framework that aligns technical design
withbusinesscontextsintheLLMera.Weareamongthefirsttodecomposegeneralbusinessvalue
into three fundamental objectives and design methodologies to achieve these objectives simultaneously, customizing LLMs for broad business applications in Information Systems. Our framework
facilitates the customization of LLMs to serve as general-purpose professional experts for business purposes, including demonstrating domain expertise and enhancing consumer satisfaction and
trustworthiness. The customized LLMs possess extensive domain knowledge, along with the necessary soft skills and core principles, aligning their communication patterns with those of domain
professionals. These experts are capable of handling a wide array of tasks within their domains
through human-like conversational interactions. We validate the effectiveness and performance of
our framework through its application in medical consultations. Additionally, we delve into the
characteristics of textual consultation records and adopt interpretable machine learning techniques
to identify what drives the performance gain. Finally, we showcase the practical value of our model
through a decision support system designed to assist human doctors in a lab experiment with medical professionals. Our framework and findings offer step-by-step principles and practical insights
for future research on customizing LLMs to solve real-world business needs.

### Generative AI

Our study is also closely relevant to the growing body of work on generative AI within IS. The area
of AI, particularly LLMs, has experienced remarkable advancements, heralding a new era in AI
capabilities.LLMslikeGPT-4,trainedonavastcollectionofdata,demonstratecapabilitiesbeyond
advanced language processing; they display elements of broader intelligence. GPT-4, in particular,
has shown exceptional performance, equating to human standards in various professional and academic tests, such as the Uniform Bar Exam, SAT, GRE, and AP free-response questions (OpenAI
2023, Bubeck et al. 2023, Zhang et al. 2023a, Liu et al. 2023, Yang et al. 2023a).
ThesignificanceofGenerativeAIhaspromptedamultitudeofinvestigationsintoitsimplications
and practical uses. Eloundou et al. (2023) suggests that GPTs might influence approximately 80%

<!-- Page 13 -->

13
of job tasks in the U.S. labor market. Research by Noy and Zhang (2023) and Brynjolfsson et al.
(2023) reveals that ChatGPT substantially improves average productivity, often substituting for
human labor instead of complementing skills. According to Zhou and Lee (2023), while generative
AI boosts output in design fields, it might diminish creative abilities. Investigations by Wang
et al. (2023a) and Wang et al. (2023c) delve into the business prospects of AI-generated imagery,
especially those emulating artistic styles, and offer a method for assessing the intelligence of LLMs.
Additionally, Burtch et al. (2023) demonstrates how ChatGPT is replacing human contributions
in online information communities, emphasizing the necessity of social interaction to mitigate the
risks associated with AI.
Our research contributes to this area by focusing on tailoring of LLMs for addressing businessrelated queries from a design science and technical standpoint. We introduce a new framework
for customizing LLMs for general business contexts usages, demonstrating its effectiveness and
feasibility. Our work not only presents a feasible model for applying LLMs in business contexts
but also delves into the technical intricacies of model development, offering practical solutions for
customizing LLMs for real-world business issues.

### Customize LLMs for Real-world Applications

The rapid progress of LLMs has sparked a wave of innovation, leading to the development of
customized LLMs for a diverse range of specific applications. For instance, Reisenbichler et al.
(2022) have fine-tuned a GPT model specifically for the niche of content marketing, focusing on
the creation of SEO-optimized landing pages. Similarly, Liga and Robaldo (2023) have taken these
modelsintothelegaldomain,adaptingaGPTmodelfortheintricatetaskoflegalruleclassification.
In the educational sector, Fan et al. (2023) have developed LLMs specifically designed for writing
and grammar assistance. Finally, Zhang et al. (2023b) have tailored LLMs for the task of news
summarization.
Additionally, customizing LLMs to support health service is also emerging area. For example,
Li et al. (2023b) introduce a medical assistant adapted from the LLaMA model, trained with real

<!-- Page 14 -->

14
patient-doctor dialogue data. Han et al. (2023) develop MedAlpaca by integrating Stanford Alpaca
and AlpacaLoRA technologies to enhance medical question-answering and dialogue capabilities.
Further, Wu et al. (2023) use medical papers to refine medical assistant’s performance in medical
tasks.Singhaletal.(2023)introduceMed-PaLM,demonstratingremarkableeffectivenessinvarious
benchmark tests.
Wecontributetothisliteraturebypresentinganovelandsystematicframeworktointegratecomprehensive business value into LLMs, including both technical expertise and non-technical aspects
augmentation. Oriented toward business value objectives, our model enhances domain expertise, consumer satisfaction, and trustworthiness. It not only enhances medical expertise but also
improves its ability to engage consumers and build trust. This dual focus on technical proficiency
and consumer experience represents a significant leap forward from existing approaches, which
often emphasize one aspect over others and typically neglect the business value of non-technical
aspects augmentation, thus overlooking consumer satisfaction and trustworthiness aspects. For
instance, Singhal et al. (2023), Wu et al. (2023), Han et al. (2023) enhance medical knowledge
but fall short in aligning with the conversation patterns, soft skills, and core principles of real
doctors. Similarly, Li et al. (2023b) and Bao et al. (2023) utilize real doctors’ conversation records,
but they do not explicitly model and capture the soft skills and core principles of human doctors.
Additionally, the previous method is more domain-specific, whereas our framework is a general
and systematic framework that can be applied to any business context. Our proposed framework
offers step-by-step principles and guidance on customizing LLMs to address real-world business
problems, enabling customization for various business contexts, such as customer support, medical
consultation, legal assistance, sales and marketing, educational programs, and more.

## Proposed Framework and Methodologies

In this section, we introduce our proposed framework along with its methodologies, specifically
applying them to the context of medical consultation. Our framework is structured into two main
steps. The first step involves decomposing the overarching business value into three primary objectives. These objectives are crucial for ensuring that the framework is tailored to the unique needs

<!-- Page 15 -->

15
and challenges of the given context. The second step focuses on the methodologies employed to
achieve these objectives. Here, we combine domain-specific theories with Supervised Fine Tuning
techniques in large language models.
In the specific case of medical consultation, our aim is to tailor LLMs to function similarly to
professional doctors. This customized LLMs, referred to as “LLM-doctor,” is designed to assist
general-purpose medical consultation through human-like conversational interactions.
The overall flow of the proposed framework is shown in Figure 2.
Figure2 Proposed Framework for Customizing LLMs for Business Contexts: A Medical Consultation Example

### Step 1: Construct Supervised Finetuning Dataset

In this part, we introduce the decomposed three fundamental objectives which represent the major
gaps between LLMs and a particular business context. We also show how to achieve the objectives
by compiling specific Supervised Fine Tuning data.
(i) Objective 1: Alignment of conversational patterns of professional roles: Each professional role adheres to specific communication structures and norms, reflecting its underlying

<!-- Page 16 -->

16
business needs and domain-specific techniques. However, existing LLMs often deviate from these
professional conversational patterns. To address this gap, it is essential to compile a substantial
corpus of real-world professional conversation records, which inherently encapsulate these communication norms. Rather than establishing predefined rules, we can capitalize on the ability of LLMs
to absorb vast amounts of data, enabling it to automatically understand the patterns from these
large-scale authentic professional records. This approach allows for a more organic and accurate
adaptation of LLMs to professional communication styles.
In the medical consultation context, we have gathered a large-scale collection of real doctors’
online consultation records from Chunyu Doctor Ltd., a leading medical consultation platform in
China.ChunyuDoctorisattheforefrontofmobileinternethealthcareandisanotableentityinthe
“Internet + Healthcare” sector. As of May 2022, it has garnered 150 million users and collaborated
with over 660,000 practicing doctors from public hospitals. The platform has facilitated over 400
millionpatientservicesandcompileddataonmorethan300millionhealthprofiles.Withanaverage
of over 390,000 daily consultations and a customer satisfaction rate of 98%, Chunyu Doctor’s
extensive database provides an invaluable resource for LLMs to learn the conversational patterns
of human doctors 1.
We have collected more than 1.5 million consultation records. Each online consultation record
covers multi-round patient-doctor conversation, which typically includes communication about the
condition,diagnosis,andmedicineinstructions,etc.Specifically,inastandardmedicalconsultation,
a three-step diagnostic process is typically followed. Initially, the doctors engages in information
collection, probing the patient for detailed information to better understand potential health concerns.Thisprogressestothediagnosisphase,wherebasedontheinformation,atentativediagnosis
isdrawnandaccompaniedbyinitialguidanceoradvice.Finally,inthetreatmentsuggestionphase,
the doctor outlines targeted treatment strategies suitable for the diagnosed condition, ensuring the
patient is well-informed and prepared for the next steps in their healthcare journey.
1The statistics come from the official website: https://www.chunyuyisheng.com/about_us/

<!-- Page 17 -->

17
(ii) Objective 2: In-depth domain knowledge: Implementing LLMs in specific business
domains requires a high level of domain-specific knowledge to ensure the accuracy and reliability of
the provided information and advice. This entails a comprehensive understanding of the technical
or specialized knowledge pertinent to the field. To meet this requirement, it is crucial to compile
an exhaustive collection of domain knowledge, encompassing all possible information within the
field, and present it in the format of question-answer pairs. This approach ensures that LLM is
equipped with the necessary expertise to effectively operate in the specific business domain.
In the medical consultation domain, we construct a large-scale collection of medical knowledge
Q&A pairs, covering both disease and medicine knowledge. For disease knowledge, we source comprehensive data from Dingxiang Doctor, a leading medical information platform in China. Dingxiang Doctor is known for providing health consultation and science popularization services to the
public, focusing on educational information, paid knowledge services, and healthcare e-commerce.
The collected data includes detailed information on various aspects of diseases, such as symptoms,
causes, diagnosis, treatment, lifestyle advice, prevention, and guidelines for consulting a doctor.
This leads to 88,449 Q&A pairs of diseases knowledge.
Intermsofmedicineknowledge,oursourceisMenet,aprofessionaldatabasespecializinginmedicalandhealthindustryresearch.Itoffersinsightsintohospitalandretailmarkets,commercialchannels, and internet-based medical information. We gather comprehensive details on 23,513 unique
medicinesfromMenet.Usingthesemedicines’instructionmanuals,wecreateQ&Apairsthatcover
various aspects such as usage, dosage, indications, contraindications, precautions, pharmacological effects, and chemical components. Questions are framed like “What diseases does [Medicine
Name] treat?” for indications, or “How is [Medicine Name] used?” for dosage and administration.
This results in 88,163 Q&A pairs, ensuring extensive coverage of each medicine’s characteristics.
Examples of disease and medicine Q&A pairs are illustrated in Figures 3 and 4, respectively.
(ii) Objective 3: Soft skills and core principles of professional roles: For LLMs to
effectively emulate professionals in various fields, it’s crucial that it embodies soft skills and core

<!-- Page 18 -->

18

### Figure3 Example of Disease Question Answer Pair

principles akin to those of human professionals. Each business domain has its unique set of nontechnical skills, interpersonal competencies, and foundational principles, essential for professional
excellence.Toachivethisgoal,ourapproachinvolvesintegratingdomain-specifictheoriestoidentify
the essential skills that professionals in each field should possess. We then use GPT-4 to evaluate
conversation records along these well-defined dimensions. The goal is to pinpoint exemplary conversation records within large-scale datasets. These exemplary records inherently encode these soft
skills, enabling LLMs to demonstrate similar skills and principles as human professionals.
In the context of medical consultation, we demonstrate this process by first identifying the
relevantsoftskillsandprinciplesforhumandoctorsfrommedicaltheory.Then,weselectexemplary
records that embody these identified skills.
Medical Theoretical Foundations: According to medical theory, we identify three soft skills
and core principles that a doctor should follow include professionalism, explainability, and emotional support. These skills, when combined, ensure not only patient safety but also cultivate trust,
ultimately contributing to a positive and reassuring healthcare experience for patients.

<!-- Page 19 -->

19

### Figure4 Example of Medicine Question Answer Pair


## Professionalism: It has been identified as central to the practice of medicine, and its importance in healthcare has been widely discussed in the literature (Wilkinson et al. 2009, Kanter et al.

2013,Passietal.2010,Cohen2006,vanMooketal.2009,WearandCastellani2000).Professionalisminhealthcareisthecombinationofethicalconduct,commitmenttoexpertise,andinterpersonal
skills that uphold the trust society places in medical professionals, especially doctors. It entails a
commitment to ethical practices such as honesty, integrity, and adherence to moral principles and
professional codes (Hilton and Slotnick 2005, Jha et al. 2006, Swick 2000, Van De Camp et al.
2004). This professionalism requires effective communication with patients and their support networks, reliability through accountability, task completion, organization, and punctuality (Frohna
and Stern 2005, Project 2002, Kearney 2005, Wagner et al. 2007). It also demands a dedication
to ongoing self-improvement, lifelong learning, knowledge advancement, and fostering the devel-

<!-- Page 20 -->

20
opment of others through feedback and leadership (Hilton and Slotnick 2005, Jha et al. 2006,
Rabinowitz et al. 2004, Swick 2000).
Professionalismplaysapivotalroleinmedicalconsultations,particularlyintherealmofpatientdoctor communication, due to several compelling reasons. Firstly, it establishes a foundation of
trust, which is essential for effective healthcare delivery. When doctors communicate with professionalism, marked by respect, empathy, and clarity, it fosters a safe environment where patients
feel comfortable sharing sensitive information, crucial for accurate diagnoses and treatment plans.
Secondly, professionalism encompasses the ability to communicate complex medical information
in an accessible manner, ensuring that patients are well-informed about their health conditions
and treatment options. This level of understanding is critical for patient engagement and adherence to medical advice. Moreover, professionalism entails adherence to ethical standards, including
maintaining confidentiality, which is vital in preserving patient dignity and trust. Lastly, professional communication skills include the ability to listen actively and respond to patient concerns,
demonstratingcompassionandunderstanding.Thisnotonlyenhancesthetherapeuticrelationship
but also directly impacts patient satisfaction and health outcomes. In summary, professionalism
in patient-doctor communication is a key driver in ensuring effective, ethical, and patient-centered
medical care.

## Explainability: Explainability of a doctor’s communication is key to a successful

patient–physician relationship and quality of care (Ha and Longnecker 2010, Markides 2011). It
refers to the clarity and comprehensibility of the information conveyed by healthcare professionals
to their patients. This involves simplifying complex medical terms and concepts into language that
is easily understood, ensuring that patients have a solid understanding of their health conditions,
treatment options, potential risks, and the benefits of the care they are receiving (Hagihara and
Tarumi 2007, Kee et al. 2018, Olson and Windish 2010, Freeman 2019, Kee et al. 2018). This
concept is rooted in the principles of patient-centered care, which prioritize the patient’s comprehension, participation, and informed decision-making in their own healthcare.

<!-- Page 21 -->

21
Explainability of a doctor’s communication is paramount in healthcare as it directly influences
patientoutcomes.Aphysicianwhofosterstransparentdialogueismorelikelytogathercomprehensive information, leading to accurate diagnoses and effective counseling. This enhances treatment
adherence and promotes better long-term health. Conversely, insufficient explanations can result
in misunderstanding, creating a disconnect between doctor and patient, which may cause treatment to fail (DiMatteo 1998). An efficient exchange of information is critical, ensuring patient
concerns are addressed and treatment options are clearly explained, thereby facilitating shared
decision-making (Arora 2003, Lee et al. 2002, Kindler et al. 2005, Minhas 2007). Moreover, quality doctor-patient communication impacts various aspects of patient care, including satisfaction,
treatment compliance, understanding of medical information, disease management, quality of life,
and overall health (Ong et al. 1995, Smith et al. 1981, Larsen and Smith 1981, Carter et al. 1982).
Therefore, practices such as thorough explanations and active listening to patients or their families
are essential in reducing adverse events (Hagihara and Tarumi 2007).

## Emotional Support: Emotional support from doctors is a fundamental facet of patient care

that substantially influences patient outcomes and satisfaction (Bradshaw et al. 2022, Walter et al.
2021, Delbanco 1992). This support extends beyond biomedical expertise to encompass essential
psychosocial competencies (Ommen et al. 2011). Patients share their hopes, fears, and concerns,
seeking an empathetic ear and understanding (Finset 2012). When doctors provide care that integrates clinical acumen with emotional support, the patient experience is markedly improved (Han
et al. 2019, Allen et al. 2018, Northcott and Hilari 2018, Rathert et al. 2015). Emotional support in
healthcare comprises cognitive, affective, and altruistic dimensions that collectively work to comprehend,empathizewith,andeasepatientdistress(Bivinsetal.2017,Sharpetal.2016).Narrative
knowing, which involves a mutual understanding between patient and doctor about the experience
of illness,further deepens thissupport (Buckley etal. 2018). Additionally,there are other practices
tofacilitateemotionalsupportsuchasactivelisteningandempatheticcommunication(Bivinsetal.
2017, Babaei and Taleghani 2019).

<!-- Page 22 -->

22
Emotional support has been shown to enhance patients’ engagement and satisfaction within
onlinehealthcommunities,toagreaterextentthaninformationalsupportalone(Chenetal.2020).
It can alleviate fears and anxieties, leading to higher levels of trust in doctors (Delbanco 1992, Cao
et al. 2017). It has been shown emotional support is crucial for cancer patients and those nearing
the end of life, offering solace and companionship during trying times (Slevin et al. 1996, Wenrich
et al. 2003).
GPT rating: After identifying the relevant soft skills from medical theory, we employ a largescaleanalysisofprofessionalrecordstopinpointexemplarycasesdemonstratingtheseskills.Utilizing GPT-4, we assess each online consultation record across these identified soft skill dimensions,
rating them on a scale from 1 to 100. This process involves instructing GPT-4 to evaluate the
performanceofprofessionals(e.g.,doctors)inspecificareas,withascoringrangefrom0(indicating
poor performance) to 100 (indicating excellent performance).
Using GPT-4’s evaluations, we select the upper 50% of records based on three essential skills,
resulting in a total of 262,482 conversations. The distribution of these skills, both before and
after this selection, is illustrated in Figure 5, demonstrating a significant improvement in all three
skills post-selection (p<0.001). By using these role model medical records, we aim to make our
LLM-doctor’s emulate the skills exhibited by these exemplary human doctors.

### Step 2: Finetuning Implementation

After SFT data construction, we perform supervised fine-tuning with open-source LLMs, specifically targeting the Baichuan2-13B-Chat model (Baichuan 2023). This model, developed by
Baichuan Intelligence Inc., is a prominent open-source LLM for Chinese, fitting our dataset’s language. Notably, our method is adaptable to other open-source LLMs. Baichuan2 is part of the
latest generation of large-scale open-source language models, trained on a 2.6 trillion token corpus.
It showcases exceptional performance in both Chinese and English benchmarks and is available in
7B and 13B versions for Base and Chat models, including a 4-bit quantized version for the Chat
model. It has been thoroughly tested in six domains: general, legal, medical, mathematics, coding,

<!-- Page 23 -->

23
Figure5 IdentifyRoleModelRecordsBasedonTheory-drivenSoftSkillsandCorePrinciplesofHumanDoctors.
All Dimensions Has Been Significantly Improved After Filter (p<0.001)
and multilingual translation, demonstrating excellent Chinese-English translation capabilities and
versatility in other languages.
For fine-tuning, we adopt the LoRA (Low-Rank Adaptation) strategy (Hu et al. 2021). This
method adapts large pre-trained language models like GPT-3 without retraining all their parameters. LoRA differs from full fine-tuning by freezing the original model weights and introducing
trainable rank decomposition matrices to each layer of the Transformer architecture. This method
significantly reduces the number of trainable parameters and GPU memory requirements. LoRA
has shown similar or even superior performance compared to traditional fine-tuning on models like
RoBERTa, DeBERTa, GPT-2, and GPT-3, offering the benefits of greater training efficiency and
no additional inference latency.
Our training setup includes 8 Nvidia 100 GPUs, completing the training in 60 hours over four
epochs.Thehyperparametersareaglobalbatchsizeof16,alearningrateof2e-5usingtheAdamW
optimizer, and a maximum sequence length of 1024 tokens.

<!-- Page 24 -->

24

## Model Performance Evaluation with Online Experiment


### Online Experiment

We conduct online experiments to evaluate the performance of our framework. We compare LLM-
doctor with two benchmarks: one is the untuned base model, and the other is a human doctor.
Such a comparison allows us to see how our framework improves over the base model as well as
the gap with the human doctor.
We develop an online consultation platform that embeds either the LLM-doctor or an untuned
base model in the backend to automatically generate responses for patients’ inquiries and serve as
a virtual doctor. We distribute this platform through the Credamo platform in China to recruit
experimental participants. Credamo is similar to Amazon Mechanical Turk, facilitating large-scale
data collection by connecting researchers with participants. We specifically recruit a large number
of online patients who recently felt ill and needed medical consultation. Initially, we ask them
if they were feeling unwell and required a doctor’s consultation. If they responded affirmatively,
we present them with a conversation interface where either the LLM-doctor or the untuned base
modelisembeddedinthebackend;otherwise,theyarenoteligibletoparticipateinourstudy.This
method help us filter for genuine patients to interact with our models. We recruit 1000 patients
to interact with the LLM-doctor and another 1000 patients to engage with the base model. All
consultation records, including patients’ queries and the models’ responses, are saved in real-time
to our backend database on our platform.
To avoid perception bias, we introduce our service as a new online doctor platform without
revealing its AI nature at the beginning. This creates an environment where users believe they are
interacting with real doctors. This ensures a fair comparison with human doctor records without
the concern of perception bias towards AI or humans. Our system is designed as a general-purpose
medical consultation assistant, capable of addressing a broad range of medical inquiries without
any disease-specific restrictions. Therefore, we do not set any constraints on acceptable disease
categories. Instead, we welcome all inquiries from patients. Patients initiate conversations based
on their unique health concerns.

<!-- Page 25 -->

25
It’s worth noting that our primary objective is to evaluate the effectiveness of our AI model
and demonstrate its proof of concept. To ensure participants’ safety and avoid potential harm, we
display a message at the conclusion of their consultation—on the thank you page—clarifying that
the responses were generated by an AI model, not a human doctor. Additionally, we specifically
advisethemnottoconsidertheconsultationasprofessionalmedicaladviceandtoconsultahuman
doctor for genuine medical guidance.
Following the collection of 2000 consultation records for LLM-doctor and the untuned base
model, we employ GPT-4 to categorize each record into the appropriate broad outpatient departments, including internal medicine, surgery, head, neck, and vision, as well as other departments.
The distribution of records is summarized in Table 1. We find that both LLM-doctor and the
base model have a similar distribution over four outpatient departments, where the base model
covers 40.4% internal medicine, 25.1% surgery, 13.6% head, neck, and vision, and 20.9% other
departments, while LLM-doctor covers 43.1% internal medicine, 22.1% surgery, 14.9% head, neck,
and vision, and 19.9% other departments. The proportion of each department is similar, and the
coverage of the four departments is also similar. The relatively same distribution is important as it
ensures that the comparison of the two models does not have a systematic difference in outpatient
department coverage and ensures a fair comparison between the two models. Again, our system
can handle all kinds of diseases; we don’t set any constraints about disease or department. Patients
initiate conversations based on their unique health concerns. Such distribution reflects the true
medical demands from online patients/participants.
Additionally, we also want to compare with human doctors. We acknowledge the challenge of
engaging a large number of human doctors. Therefore, we utilize the pre-collected real patientdoctorconsultationrecordsfromChunyuDoctor,whichconsistofactualresponsesfromdoctorsto
patient inquiries. To ensure a fair comparison with the base model and LLM-doctor, we randomly
draw1000samplesbasedonLLM-doctor’sdistributionoverfourdepartments.Thesampledhuman
doctor records distribution is summarized in Table 1. It has a relatively same distribution as the

<!-- Page 26 -->

26
base model and LLM-doctor, covering 43.1% internal medicine, 22.3% surgery, 14.9% head, neck,
and vision, and 19.7% other departments. It reveals that all three groups span a wide range of
outpatient departments with roughly equivalent coverage. Consequently, there is no systematic
difference in outpatient department coverage, ensuring a fair comparison among the groups.

### Department BaseModel LLM-doctor HumanDoctor

InternalMedicine 404(40.4%) 431(43.1%) 431(43.1%)

### Surgery 251(25.1%) 221(22.1%) 223(22.3%)

Head,Neck,andVision 136(13.6%) 149(14.9%) 149(14.9%)
OtherDepartments 209(20.9%) 199(19.9%) 197(19.7%)

### Total 1000 1000 1000

Table1 Consultation Records Distribution Across Multiple Outpatient Departments

### Performance Evaluation with Medical Professionals and Real Consumers

Our evaluation covers two key dimensions: medical expertise and consumer preference. For medical expertise, we assess consultations’ professionalism and accuracy. For consumer preference, we
focus on patient satisfaction and trustworthiness. Firstly, professionalism and accuracy directly
relate to the quality of medical advice provided; ensuring that the system adheres to professional
consultation procedures and standards and delivers precise diagnostics is paramount to patient
safety and effective treatment. Secondly, patient satisfaction and trustworthiness are essential for
gauging how well the system meets patient needs and expectations, which are crucial for patient
engagement and adherence to medical advice. This comprehensive evaluation helps in refining the
AI’s capabilities and ensuring its utility in real-world healthcare settings.
For the medical expertise aspect, we have engaged a large group of real doctors from prominent
hospitals in China. Their extensive clinical experience is crucial for accurate evaluations. We compare the consultation records from the untuned base model, LLM-doctor, and real doctors. We ask
them to rate professionalism and accuracy along a scale of 0-100, where 100 represents extremely
highand0representsextremelylow.Eachrecordisassessedbyatleastthreedifferentexpertsfrom
the same department, ensuring a robust evaluation. The final score for each consultation record is
the average of these ratings.

<!-- Page 27 -->

27
Regarding consumer preference, we involve real consumers who assess the consultation records
from a patient’s perspective. This is conducted on the Credamo platform. Participants rate the
records based on trustworthiness and satisfaction, as if they were the patients in the consultations.
We ask them to rate trustworthiness and satisfaction along a scale of 0-100, where 100 represents
extremely high and 0 represents extremely low. Each record is reviewed by at least three different
consumers. The final score for each consultation record is the average of these ratings.
The evaluations from both medical professionals and consumers are summarized in Table 2.
Specifically, we report the average scores across various dimensions and also include the statistical
significance, with t-statistics and p-values, for comparisons between two models. Overall medical
expertiseisanaverageofprofessionalismandaccuracy,overallconsumerpreferenceisanaverageof
consumersatisfactionandtrustworthiness,andoverallperformanceisanaverageofprofessionalism,
accuracy, satisfaction, and trustworthiness.
From a medical expertise standpoint, LLM-doctor significantly outperforms the base model
with an +11.68% improvement in professionalism (p < 0.001) and a +17.43% improvement in
accuracy (p<0.001). Meanwhile, the base model significantly lags behind human doctors by -
13.08% in professionalism (p<0.001) and by -16.9% in accuracy (p<0.001). Our LLM-doctor
more closely matches the medical expertise of human doctors, with marginally smaller gaps of
-2.93% in professionalism (p=0.004) and -2.42% in accuracy (p=0.019). This indicates that our
framework significantly narrows the gap between untuned LLMs and human doctors, bringing it
closertohuman-levelperformance.Thisresultisparticularlysignificant,asasingleLLM-modelcan
approach the capabilities of nearly 1000 human doctors across different outpatient departments.
This highlights the potential of the LLM-model to function as a general medical assistant, serving
many human doctors in real worlds.
The same conclusion applies to consumer preference metrics. From a consumer satisfaction perspective, the base model performs -27.76% worse than human doctors (p<0.001), and from a
consumer trustworthiness perspective, it is -27.16% worse (p<0.001). The gap in consumer preferences between the base and human doctors is much larger than that in medical expertise. This

<!-- Page 28 -->

28
indicates that the untuned base model significantly lags behind when engaging with consumers in
reality, highlighting a potential shortcoming. This also underscores the need for a framework to
improveinthisaspect.Fromthisstandpoint,LLM-doctorsignificantlyoutperformsthebasemodel
with a +28.36% improvement in consumer satisfaction (p<0.001) and a +27.56% improvement in
trustworthiness (p<0.001). It narrows the gap to human doctors’ medical expertise with smaller
deficits of -7.27% in satisfaction (p<0.001) and -7.09% in trustworthiness (p<0.001). This further
indicates that our framework significantly narrows the gap between untuned LLMs and human
doctors, moving it closer to human-level performance, with an even stronger improvement from
the perspective of consumer preference.
LLM-doctor LLM-doctor Base

### Base LLM Human vs vs vs

Evaluationmetrics Model Doctor Doctor Base HumanDoctor HumanDoctor
Professionalism 67.78 75.70 77.98 +11.68% -2.93% -13.08%
(9.29,p<0.001) (-2.86,p=0.004) (-15.45,p<0.001)
Accuracy 63.17 74.18 76.01 +17.43% -2.42% -16.90%
(12.77,p<0.001) (-2.35,p=0.019) (-20.83,p<0.001)
Overall Medical Expertise 65.47 74.94 77.00 +14.45% -2.68% -14.97%
(11.36,p<0.001) (-2.70,p=0.007) (-19.32,p<0.001)
Satisfaction 56.24 72.19 77.86 +28.36% -7.27% -27.76%
(21.51,p<0.001) (-7.87,p<0.001) (-29.37,p<0.001)
Trustworthiness 56.68 72.30 77.82 +27.56% -7.09% -27.16%
(20.69,p<0.001) (-7.57,p<0.001) (-28.32,p<0.001)
Overall Consumer Preference 56.46 72.25 77.84 +27.96% -7.18% -27.46%
(21.41,p<0.001) (-7.81,p<0.001) (-29.26,p<0.001)
Overall Performance 60.97 73.59 77.42 +20.71% -4.94% -21.25%
(22.81,p<0.001) (-7.21,p<0.001) (-35.04,p<0.001)

### Numberofentities 1 1 1000


### Numberofrecords 1000 1000 1000

Table2 Medical Experts and Real Consumers Evaluation: Model Performance Comparison for Base Model,
LLM-doctor and Human Doctors Along Medical Expertise Metrics and Consumer Preference Metrics.
Note:Weconducttwosamplet-testandreportthet-statsandp-valuetocomparetwomodel.

### Heterogeneous Comparison Across Various Outpatients Departments

Beyond average performance, we delve into various outpatient departments and compare the
nuancedperformanceineachdepartmentasshowninTable3.Suchanalysiscanhelpusunderstand
how the performance of our framework differs across heterogeneous outpatient departments.
We find that in the internal medicine department, the LLM-doctor shows a relatively larger
overall improvement (an average of medical expertise and consumer preference) compared to the

<!-- Page 29 -->

29
untuned base model, about +21.64% (p < 0.001), followed by the surgery department with an
improvement of +16.76% (p<0.001). The smallest improvement occurs in the head, neck, and
vision departments with an improvement of +15.82% (p<0.001). Correspondingly, in the internal
medicinedepartment,theLLM-doctorisclosesttothehumandoctorwitha-4.74%gap(p<0.001),
followed by a -5% gap (p<0.001)in the surgery department. The largest gap, -6.5% (p<0.001),
occurs in the head, neck, and vision departments. This indicates that our framework functions
better in internal medicine and could be prioritized for use in this department compared to others.

## Interpretability analysis: Understand Where the Gains Come From

In the previous section, we compare the performance of three models and demonstrate the superiority of our framework in terms of both medical expertise and perceived consumer satisfaction and
trustworthiness as determined by consumers. However, it is unclear what happens in conversation
records and where the performance gain come from, particularly which conversation or communication characteristics contribute to the performance gains. To answer this question, we delve
deep into the textual conversation records between patients and the LLM-doctor, base model, and
human doctor, extracting textual communication and consultation characteristics from consultationrecords.Afterwards,weuseaninterpretablemachinelearningmodel,XGBoost,tounderstand
how these extracted textual characteristics influence perceived medical expertise and consumer
preference.

### Analyze Textual Communication and Consultation Characteristics

Given the proven reliability of GPT-4 in annotations and evaluations (as noted in sources such
as Gilardi 2023, Eloundou 2023, and Lou 2023), we utilize GPT-4 to extract characteristics from
medical records across various textual communication and consultation features. To bypass difficulties or ambiguities, we simplify the classification into a binary decision—yes or no—specifically
determining whether the doctor’s record demonstrates proactive information gathering, provides
targeteddiseasediagnosis,offerstargetedtreatmentrecommendations,usesmedicalterms,engages
in multi-round interactions, exhibits a human-like communication style, demonstrates clarity of

<!-- Page 30 -->

30
LLM-doctor LLM-doctor Base

### Base LLM Human vs vs vs

Department Evaluationmetrics Model Doctor Doctor Base HumanDoctor HumanDoctor
Professionalism 69.53 75.84 79.43 +9.08% -4.52% -12.46%
(9.52),p<0.001 (-4.27),p<0.001 (-11.41),p<0.001

### Accuracy 64.60 74.73 76.98 +15.68% -2.92% -16.07%

InternalMedicine (13.79),p<0.001 (-3.42),p<0.001 (-18.38),p<0.001
Satisfaction 54.85 72.99 77.55 +33.07% -5.88% -29.27%
(16.91),p<0.001 (-4.22),p<0.001 (-19.82),p<0.001
Trustworthiness 55.02 73.26 77.64 +33.14% -5.64% -29.13%
(16.50),p<0.001 (-3.99),p<0.001 (-19.49),p<0.001
Medical Expertise 67.07 75.29 78.20 +12.26% -3.73% -14.24%
(13.13),p<0.001 (-4.48),p<0.001 (-17.23),p<0.001
Consumer Preference 54.94 73.13 77.60 +33.10% -5.76% -29.20%
(17.00),p<0.001 (-4.15),p<0.001 (-19.91),p<0.001
Overall Performance 61.00 74.21 77.90 +21.64% -4.74% -21.69%
(21.16),p<0.001 (-5.61),p<0.001 (-25.79),p<0.001
Professionalism 71.95 76.38 77.44 +6.15% -1.37% -7.09%
(5.84),p<0.001 (-1.30),p=0.194 (-7.00),p<0.001

### Accuracy 65.34 74.74 75.88 +14.38% -1.50% -13.89%


### Surgery (10.65),p<0.001 (-1.30),p=0.194 (-11.88),p<0.001

Medical Expertise 68.65 75.56 76.66 +10.07% -1.44% -10.45%
(9.51),p<0.001 (-1.36),p=0.174 (-10.57),p<0.001
Satisfaction 57.38 71.71 78.53 +24.98% -8.68% -26.94%
(8.98),p<0.001 (-4.38),p<0.001 (-13.79),p<0.001
Trustworthiness 57.79 71.94 78.43 +24.49% -8.28% -26.32%
(8.85),p<0.001 (-4.22),p<0.001 (-13.29),p<0.001
Consumer Preference 57.58 71.82 78.48 +24.73% -8.48% -26.63%
(9.01),p<0.001 (-4.35),p<0.001 (-13.72),p<0.001
Overall Performance 63.11 73.69 77.57 +16.76% -5.00% -18.64%
(11.88),p<0.001 (-4.36),p<0.001 (-17.17),p<0.001
Professionalism 70.11 75.17 77.58 +7.21% -3.11% -9.63%
(5.60),p<0.001 (-2.74),p=0.006 (-8.65),p<0.001

### Accuracy 66.58 73.71 75.34 +10.71% -2.16% -11.63%

Head,Neck,andVision (6.88),p<0.001 (-1.65),p=0.100 (-8.49),p<0.001
Medical Expertise 68.35 74.44 76.46 +8.92% -2.64% -10.62%
(7.30),p<0.001 (-2.30),p=0.022 (-9.78),p<0.001
Satisfaction 55.70 70.14 78.15 +25.93% -10.25% -28.73%
(6.35),p<0.001 (-4.01),p<0.001 (-11.95),p<0.001
Trustworthiness 57.12 69.97 78.01 +22.49% -10.31% -26.78%
(5.59),p<0.001 (-3.98),p<0.001 (-11.18),p<0.001
Consumer Preference 56.41 70.05 78.08 +24.19% -10.28% -27.75%
(6.03),p<0.001 (-4.04),p<0.001 (-11.74),p<0.001
Overall Performance 62.38 72.25 77.27 +15.82% -6.50% -19.27%
(8.09),p<0.001 (-4.45),p<0.001 (-13.92),p<0.001
Professionalism 57.88 75.02 75.73 +29.62% -0.93% -23.57%
(4.60),p<0.001 (-0.21),p=0.836 (-7.59),p<0.001

### Accuracy 55.56 72.70 74.57 +30.85% -2.50% -25.49%

OtherDepartments (4.63),p<0.001 (-0.54),p=0.590 (-8.22),p<0.001
Medical Expertise 56.72 73.86 75.15 +30.22% -1.71% -24.52%
(4.65),p<0.001 (-0.38),p=0.706 (-8.04),p<0.001
Satisfaction 57.91 72.54 77.53 +25.25% -6.44% -25.30%
(9.31),p<0.001 (-3.24),p=0.001 (-12.02),p<0.001
Trustworthiness 58.26 72.36 77.38 +24.19% -6.48% -24.70%
(8.80),p<0.001 (-3.12),p=0.002 (-11.37),p<0.001
Consumer Preference 58.09 72.45 77.45 +24.72% -6.46% -25.00%
(9.22),p<0.001 (-3.23),p=0.001 (-11.90),p<0.001
Overall Performance 57.40 73.16 76.30 +27.44% -4.12% -24.76%
(8.01),p<0.001 (-1.70),p=0.090 (-13.63),p<0.001
Table3 Model Comparison Along Heterogeneous Outpatient Departments
Note:Note:Weconducttwosamplet-testandreportthet-statsandp-valuetocomparetwomodel.

<!-- Page 31 -->

31
response, and shows respect and patience in communication, as well as logical reasoning. Consider
proactiveinformationgatheringasanexample.ThepromptforGPT-4todoclassificationis:Below
is a conversation between a patient and a doctor during an online consultation. Please determine
if the doctor first asked questions to learn more about the patient’s health condition and gathered
more information before making any diagnosis and treatment recommendations (Yes), or if the
doctor did not ask any further questions and made a direct diagnosis and treatment recommendations (No). Please answer with either ”Yes” or ”No,” and only return the answer. We calculate
the percentage of ”Yes” answers for each model across each characteristic and plot the distribution
in Figure 6, and also report the significance test for comparison between models across various
textual characteristics in Table 4.
As we observe, both LLM-doctor (94.7% of consultation records) and human doctors (89.2% of
consultation records) consistently engage in proactive information gathering by asking patients for
more details about their health conditions before making diagnoses and suggestions, whereas the
base model seldom does with only 6.2% of consultation records proactively asking. Proactive information gathering is extremely important for doctors to fully understand patients’ health situations
and provide precise diagnosis and recommendations. This suggests the base model significantly
falls short in this manner. Our LLM-doctor is much closer to real doctors’ consultation procedures. Additionally, both LLM-doctor (72.3% of consultation records) and human doctors (82.6%
of consultation records) provide targeted diagnosis, whereas the base model rarely (only 14.1%
of consultation records) provides targeted responses and often includes many irrelevant details.
Regardingtargetedtreatmentrecommendations,humandoctorsprovidetargetedtreatmentrecommendations based on patient’s health conditions in 96.5% of all consultation records, LLM-doctor
in 87.4% of all consultation records, whereas the base model only provides 42.7% targeted treatment recommendations. Regarding medical term usage, human doctors use medical terms in 90.8%
of cases during consultations, LLM-doctor in 78.5% of cases, whereas the base model uses medical
terms less often, only in 63.6% of cases.

<!-- Page 32 -->

32
Furthermore, LLM-doctor (93% of consultation records) and human doctors (95.7% of consultation records) often engage in multi-round interactions, whereas only 20.5% of base model
consultationrecordshavemulti-roundinteractions.Themajorityofconsultationrecordsfromboth
LLM-doctor and human doctors exhibit a human-like communication style, with human doctors
showing this style in 95.6% of consultations, and LLM-doctor in 91% of records. However, the
base model only demonstrates this style 2.3% of the time. This suggests that the base model is far
removed from human communication styles, resembling more of a bot-style communication. This
underscores the benefit of aligning conversation patterns to make our model more akin to a human
doctor. Additionally, the majority of human doctors’ responses exhibit high clarity with 90.6% of
cases, LLM-doctor with 95% of cases, whereas the base model’s clarity is relatively low with only
33.8% of cases exhibiting high clarity. This indicates the response of the base model lacks clarity,
is very long, and includes redundant and irrelevant information.
To summarize, LLM-doctor is much closer to human doctors along the majority of these textual communication and consultation characteristics, whereas the base model is relatively far from
human doctors. This indicates our framework can significantly change how LLMs conduct consultations such as the procedure, and communication styles, making it more human doctor-like.

### Interpretable Machine Learning Analysis

We then employ the interpretable machine learning model to understand how these extracted
textual communication and consultation characteristics influence perceived medical expertise and
consumer preference. Specifically, we adopt XGBoost (Chen and Guestrin 2016), which is a highly
efficient and scalable implementation of gradient boosted trees, designed to push the limits of
computing power for boosted tree algorithms. It has gained significant popularity in business
applications due to its robust performance and its ability to provide interpretable insights through
feature importance metrics (Zhang and Luo 2023, Wang and Li 2023). This feature allows users
to understand which variables most significantly impact the model’s predictions, offering valuable
insights into the underlying data patterns and decision-making processes.

<!-- Page 33 -->

33
LLM-doctor LLM-doctor Base

### Base LLM Human vs vs vs

Evaluationmetrics Model Doctor Doctor Base HumanDoctor HumanDoctor
proactiveinformationgathering 6.2% 94.7% 89.2% +1427.42% +6.17% -93.05%
(84.98),p<0.001 (4.54),p<0.001 (-66.74),p<0.001
targeteddiseasediagnosis 14.1% 72.3% 82.6% +412.77% -12.47% -82.93%
(32.45),p<0.001 (-5.55),p<0.001 (-42.07),p<0.001
targetedtreatmentrecommendation 42.7% 87.4% 96.5% +104.68% -9.43% -55.75%
(23.72),p<0.001 (-7.58),p<0.001 (-32.23),p<0.001
medicaltermusage 63.6% 78.5% 90.8% +23.43% -13.55% -29.96%
(7.44),p<0.001 (-7.74),p<0.001 (-15.32),p<0.001
multi-roundinteraction 20.5% 93% 95.7% +353.66% -2.82% -78.58%
(47.98),p<0.001 (-2.62),p=0.009 (-52.61),p<0.001
human-likecommunicationstyle 2.3% 91% 95.6% +3856.52% -4.81% -97.59%
(86.78),p<0.001 (-4.13),p<0.001 (-116.08),p<0.001
clarityofresponse 33.8% 95% 90.6% +181.07% +4.86% -62.69%
(37.14),p<0.001 (3.82),p<0.001 (-32.30),p<0.001
respectandpatienceincommunication 100% 96.9% 98.9% -3.10% -2.02% +1.11%
(-5.65),p<0.001 (-3.13),p=0.002 (3.33),p<0.001
logicalreasoning 89.3% 87.7% 92.9% -1.79% -5.60% -3.88%
(-1.12),p=0.262 (-3.94),p<0.001 (-2.83),p=0.005
Table4 Medical Consultation Record Characteristics Comparison For Base Model, LLM-doctor and Human
Doctors. We Show Percentage of ”Yes” Answers for Each Model across Each Characteristic
Note:Weconducttwosamplet-testandreportthet-statsandp-valuetocomparetwomodel.
Figure6 Visualization of Medical Consultation Record Characteristics Comparison in Terms of Percentage of
”Yes” Answers Across Characteristics
We use the extracted textual characteristics to predict four metrics including professionalism,
accuracy, consumer trustworthiness, and satisfaction, as well as overall medical expertise and consumer preference on all consultation records from three models. Medical expertise is calculated as
the average of professionalism and accuracy, while consumer preference is the average of satisfac-

<!-- Page 34 -->

34
tion and trustworthiness. We plot the learned feature importance for medical expertise in Figure 7
and for consumer preference in Figure 8.
Interestingly, we find that the characteristics contributing to perceived medical expertise and
consumer preference are very different. For accuracy, the top five predictors are targeted disease
diagnosis, medical term usage, proactive information gathering, multi-round interaction, and targeted treatment recommendation. The top predictors for perceived professionalism are human-like
communication style, proactive information gathering, logical reasoning, multi-round interaction,
and medical term usage. These aspects suggest that training and technology solutions should focus
on enhancing these characteristics in medical professionals and AI systems to meet professional
standards.
For consumer preference, the top predictors for consumer satisfaction are targeted treatment
recommendations, respect and patience in communication, clarity of response, and medical term
usage. For consumer trustworthiness, the top predictors are clarity of response, multi-round interaction, targeted disease diagnosis, targeted treatment recommendations, and medical term usage.
This indicates that beyond technical medical competence, the manner in which information is
communicated to patients is vital. Managers in healthcare settings should, therefore, emphasize
patient-centered communication skills in training programs to ensure clarity and respectfulness,
tailoring interactions to effectively meet consumer needs. Our framework aligns the conversation
pattern with that of a human doctor and models the soft skills and core principles into LLMs,
which can improve consumer satisfaction and trustworthiness. These insights can guide the development of technology solutions that align with professional standards and consumer expectations,
ultimately enhancing patient care and satisfaction.

## Decision Support Showcase to Demonstrate the Practical Value to


### Assist Human Doctor

In this section, we demonstrate the practical value of our model by illustrating how it can assist
human doctors in the real world.

<!-- Page 35 -->

35
(a) Professionalism
(b) Accuracy
(c) Overall Medical Expertise
Figure7 Feature Importance of Medical Consultation Record Characteristics on Medical Expertise

<!-- Page 36 -->

36
(a) Satisfaction
(b) Trustworthiness
(c) Overall Consumer Preference
Figure8 Feature Importance of Medical Consultation Record Characteristics on Consumer Preference

<!-- Page 37 -->

37

### Lab Experiments Design

We showcase a decision support use case in which, during an online consultation, our LLM-doctor
can be used to generate an initial response to patients’ queries in a copilot manner. The human
doctor can either accept this generated response or edit it before finalizing and sending it back
to the patients. The copilot assistant approach enables human doctors to lead the entire process,
maintaincontroloverthefinalresponseandconductqualityassurance,therebymitigatingpotential
errors or risky advice generated by the AI model.
To achieve this goal, we develop an online consultation platform where our LLM-doctor or base
model can be embedded in the backend to generate initial responses for the doctor in a copilot
manner. For example, as illustrated in the screenshot in Figure 9, when a patient submits a query
or text, our model generates an initial response that appears in the chat box of the human doctor,
who can then directly edit it in the chat box and send it to the patients. Such generation occurs
in each round of interactions. Our platform supports a two-way connection, enabling both doctors
and patients to log in simultaneously for consultations. It offers three modes: human doctor alone,
human doctor + LLM-doctor, and human doctor + base model.
To demonstrate the practical value and effectiveness of such a system, we conduct a laboratory
experiment, inviting five experienced doctors from prestigious hospitals in China. Each doctor
participated in medical consultations with patients in all three modes, including human doctor
alone, human doctor + LLM-doctor, and human doctor + base model. Allowing each doctor
to experience all three modes helps them get a direct sense of how these models differ in their
consultation process. To ensure a fair comparison, we recruit multiple research assistants and,
according to the doctors’ expertise, generate synthetic patient profiles from a random sample of
historical records from Chunyu doctors using GPT-4. Each research assistant has a fixed patient
profile and consults with the same human doctor three times under different modes. This synthetic
patient profile avoids the risks of interacting with real patients and ensures a fair comparison of
the three modes. We film the consultation process and save the recorded videos, which can help us
analyze the entire consultation process. We also distribute a post-hoc survey to gather the doctors’
evaluations of their experience.

<!-- Page 38 -->

38

### Results

Firstly, we compare the productivity of human doctors across the three modes as shown in Table 5.
We measure productivity by using the time spent by human doctors during consultations. Please
note that we exclude patients’ time spent, as our key focus is to observe the increase in human
doctors’ productivity. For each doctor, we show the time spent under three conditions and calculate the time saved by using the LLM-doctor and base model. With the aid of the LLM-doctor,
human doctors, on average, saved 53.16% of their time compared to operating without the LLM-
doctor. The base model also saves human doctors’ time. However, the magnitude is much smaller
compared to the LLM-doctor; it saved only 19.31% of the time compared to the doctors working
independently. This suggests that our LLM-doctor can dramatically enhance the productivity of
human doctors compared to the base model. Such a pattern is consistent for all human doctors in
our experimental results.
Furthermore, we collect post-hoc surveys from human doctors regarding the evaluation of their
experiments and plot their responses in Figure 10. Specifically, we ask human doctors to rate the
quality of response, frequency of direct adoption, frequency of adoption or modification, improvement in time efficiency, reduction in cognitive burden, support for problem-solving, potential for
online deployment, and satisfaction with response speed on a 1-5 Likert scale, where 5 indicates
extremelyhighand1indicatesextremelylow.Wespecificallyposethefollowingquestionstohuman
doctors. Each doctor is asked to evaluate both the LLM-doctor and the base model using the same
survey.
• Quality of response: What do you think of the quality of AI-generated response suggestions?
• Direct adoption frequency: How frequently do you directly adopt AI-suggested answers in
conversations with patients?
• Adoption or modification frequency: How frequently do you either directly adopt or modify
(retaining at least 50% of the original) AI-suggested answers in conversations with patients?
• Time efficiency improvement: Has the time you spend on patient consultations been reduced
when using AI assistance?

<!-- Page 39 -->

39
HumanDoctor HumanDoctor HumanDoctor TimeSaved TimeSaved
withoutAI +LLM-doctor +Base byLLM-doctor byBase
HumanDoctor1 15.3 5.0 12.7 -67.32% -16.99%
HumanDoctor2 11.5 3.5 8.3 -69.57% -27.83%
HumanDoctor3 10.7 2.9 10.0 -72.90% -6.54%
HumanDoctor4 9.4 6.8 8.2 -27.66% -12.77%
HumanDoctor5 7.4 5.3 5 -28.38% -32.43%

### Average - - - -53.16% -19.31%

Table5 Productivity Comparison: Time Spent (min) by Human Doctors under Different Experimental
Conditions.
• Cognitive burden reduction: Does AI assistance help reduce your cognitive workload?
• Problem-solving support: Can AI help you solve problems that you would find difficult to solve
on your own?
• Potential for online deployment:Howgreatdoyouthinkthepotentialisforlarge-scaledeployment of this AI in online consultation platforms?
• Response speed satisfaction: Does the response speed of the AI meet your work needs?
Interestingly, the results show that human doctors generally perceive the response quality of the
LLM-doctor to be higher, and they adopt its responses (either directly or by modifying, retaining
at least 50% of the original content) more frequently than those of the base model. Additionally,
the doctors believe that the LLM-doctor can reduce their cognitive load during consultations much
more than the base model. They also think the LLM-doctor can save them time spent during
consultations more effectively than the base model. Furthermore, they perceive the LLM-doctor as
having more practical value for large-scale deployment on online consultation platforms compared
to the base model. These analyses show that the LLM-doctor’s practical value in assisting human
doctors is greater than that of the base model.
Additionally, we also provide an open-ended question regarding their additional evaluation or
comments toward our LLM-doctor and base model. For LLM-doctor, we receive the following
open-ended evaluations and comments:
• Itisgenerallyhelpfulandcanoftenbeuseddirectly,althoughitoccasionallyprovidesresponses
that are too brief.

<!-- Page 40 -->

40
(a) Interface with LLM-doctor Assistant
(b) Interface without LLM-doctor Assistant

### Figure9 Online Consultation Platform Interface

• It offers valuable insights that might be overlooked by doctors, thereby helping to decrease
the risk of acute illnesses.

<!-- Page 41 -->

41
Figure10 Human Doctors’ Experience Evaluation Toward LLM-doctor and Base Model in Medical

### Consultation Lab Experiment

• The AI excels in proactively asking questions and effectively gathering information from
patients, addressing the key points in its responses.
For the base model, we receive the following open-ended evaluations and comments:
• Responses are too lengthy, verbose, and not immediately usable, necessitating manual input
which increases the workload.
• Information lacks professionalism and personalization, and does not provide effective medical
advice, making it less useful for both doctors and patients.
• The information provided is overly dense and generic and often includes many irrelevant
details, similar to what is readily available online, adding little value for medical professionals and
potentially increasing anxiety for patients with limited medical knowledge.
Overall, human doctors think the base model has salient drawbacks, including providing overly
verbose and generic responses, a lack of personalization, and many irrelevant details which might
increase anxiety for patients. These factors make it less useful for doctors and patients. In contrast,
our LLM-doctor can proactively ask questions and address the key points in consultations and can

<!-- Page 42 -->

42
be directly used by human doctors during consultations. All these factors demonstrate that our
LLM-doctor’s practical value is greater than that of the base model.

## Conclusion

The significant progress in LLMs has profoundly impacted the conventional approach in design
science research. This traditional approach involves identifying specific tasks, generating relevant
datasets, and constructing models to connect inputs with outputs for these tasks. However, such
approach is increasingly facing challenges due to the superior capabilities of LLMs.
Inthisstudy,weproposeanovelframeworktocustomizeLLMsforgeneralbusinesscontextsthat
aims to achieve three fundamental objectives simultaneously: (1) aligning conversational patterns,
(2) integrating in-depth domain knowledge, and (3) embodying theory-driven soft skills and core
principles. We design methodologies that combine domain-specific theory with Supervised Fine
Tuning (SFT) to achieve these objectives simultaneously. Our framework facilitates the customization of LLMs to serve as general-purpose professional experts for business purposes, including
demonstrating domain expertise and enhancing consumer satisfaction and trustworthiness.
Then,weadoptmultipleexperiments,includingonlineexperimentandlabexperiment,todemonstratetheeffectivenessandpracticalvalueofourframeworkinthecontextofmedicalconsultations.
Ourevaluationsincludeonlineexperimentswithactualpatientsandassessmentsbydomainexperts
and real consumers show that customized LLM model substantially outperforms untuned base
model in medical expertise as well as consumer satisfaction and trustworthiness. Our framework
significantly narrows the gap between untuned language models and human professionals, significantlymovingclosertohuman-levelperformance.Inaddition,weanalyzethecontentoftext-based
consultation records and apply interpretable machine learning methods to identify the factors contributing to these performance improvements. We also demonstrate the practical applications of
our model in a decision-support system intended to aid doctors during consultations in lab-based
experiments. We implement an online platform for consultations where our model provides preliminary responses, supporting doctors in a supportive copilot fashion. The results indicate that

<!-- Page 43 -->

43
with the support of the LLM-doctor, medical professionals can reduce their consultation time by
an average of 53.16%, and decrease their cognitive load, proving the model’s high efficacy and
adaptability for broad use in practice.
Our study carries fruitful managerial implications. Although we instantiate our framework in
the context of medical consultation, our framework can be easily generalized to other business
contexts. For example, it is possible to generalize it to customer support, legal assistance, sales
and marketing, educational programs, and more. Our framework offers step-by-step principles,
guidance and valuable insights that future research can potentially use.
Furthermore, our study has practical implications for the healthcare industry. We demonstrate
one possible way of integrating an LLM-doctor to assist human doctors in generating initial
responses in a copilot manner. In fact, there are many other possibilities for integrating the customized LLM-doctor model into medical workflows, which can potentially benefit healthcare delivery by enhancing accessibility, scalability, and cost-effectiveness. It opens up new possibilities for
24/7 medical consultation services, especially in remote or underserved areas, and offers a solution
to workforce shortages by handling routine consultations. This, in turn, allows medical professionalstoconcentrateonmorecomplexcases,therebyimprovingtheoverallefficiencyandeffectiveness
of healthcare systems.

### References

Allen D, Scarinci N, Hickson L (2018) The nature of patient-and family-centred care for young adults living
withchronicdiseaseandtheirfamilymembers:asystematicreview.International journal of integrated
care 18(2).
Arora NK (2003) Interacting with cancer patients: the significance of physicians’ communication behavior.
Social science & medicine 57(5):791–806.
Babaei S, Taleghani F (2019) Compassionate care challenges and barriers in clinical nurses: A qualitative
study. Iranian journal of nursing and midwifery research 24(3):213.
Baichuan (2023) Baichuan 2: Open large-scale language models. arXiv preprint arXiv:2309.10305 URL
https://arxiv.org/abs/2309.10305.

<!-- Page 44 -->

44
Bao Z, Chen W, Xiao S, Ren K, Wu J, Zhong C, Peng J, Huang X, Wei Z (2023) Disc-medllm: Bridging
general large language models and real-world medical consultation. arXiv preprint arXiv:2308.14346 .
Ben-Assuli O, Padman R (2020) Trajectories of repeated readmissions of chronic disease patients: Risk
stratification, profiling, and prediction. MIS Quarterly 44(1).
Bivins R, Tierney S, Seers K (2017) Compassionate care: not easy, not free, not only nurses.
Bradshaw J, Siddiqui N, Greenfield D, Sharma A (2022) Kindness, listening, and connection: patient and
clinician key requirements for emotional support in chronic and complex care. Journal of Patient
Experience 9:23743735221092627.
Brynjolfsson E, Li D, Raymond LR (2023) Generative ai at work. Technical report, National Bureau of
Economic Research.
Bubeck S, Chandrasekaran V, Eldan R, Gehrke J, Horvitz E, Kamar E, Lee P, Lee YT, Li Y, Lundberg
S, et al. (2023) Sparks of artificial general intelligence: Early experiments with gpt-4. arXiv preprint
arXiv:2303.12712 .
BuckleyC,McCormackB,RyanA(2018)Workinginastoriedway—narrative-basedapproachestopersoncentred care and practice development in older adult residential care settings. Journal of Clinical
Nursing 27(5-6):e858–e872.
BurtchG,LeeD,ChenZ(2023)Theconsequencesofgenerativeaiforugcandonlinecommunityengagement.
Available at SSRN 4521754 .
CaoW,QiX,YaoT,HanX,FengX(2017)Howdoctorscommunicatetheinitialdiagnosisofcancermatters:
cancer disclosure and its relationship with patients’ hope and trust. Psycho-oncology 26(5):640–648.
Carter WB, Inui TS, Kukull WA, Haigh VH (1982) Outcome-based doctor-patient interaction analysis: Ii.
identifying effective provider and patient behavior. Medical Care 550–566.
Chen G, Xiao S, Zhang C, Zhao H (2023) A theory-driven deep learning method for voice chat–based
customer response prediction. Information Systems Research .
Chen S, Guo X, Wu T, Ju X (2020) Exploring the online doctor-patient interaction on patient satisfaction
based on text mining and empirical analysis. Information Processing & Management 57(5):102253.

<!-- Page 45 -->

45
Chen T, Guestrin C (2016) Xgboost: A scalable tree boosting system. Proceedings of the 22nd acm sigkdd
international conference on knowledge discovery and data mining, 785–794.
Cohen JJ (2006) Professionalism in medical education, an american perspective: from evidence to accountability. Medical education 40(7):607–617.
Delbanco TL (1992) Enriching the doctor-patient relationship by inviting the patient’s perspective. Annals
of internal medicine 116(5):414–418.
DiMatteo M (1998) The role of the physician in the emerging health care environment. Western Journal of
Medicine 168(5):328.
EloundouT,ManningS,MishkinP,RockD(2023)Gptsaregpts:Anearlylookatthelabormarketimpact
potential of large language models. arXiv preprint arXiv:2303.10130 .
Fan Y, Jiang F, Li P, Li H (2023) Grammargpt: Exploring open-source llms for native chinese grammatical error correction with supervised fine-tuning. CCF International Conference on Natural Language
Processing and Chinese Computing, 69–80 (Springer).
Finset A (2012) “i am worried, doctor!” emotions in the doctor–patient relationship. Patient education and
counseling 88(3):359–363.
FreemanAL(2019)Howtocommunicateevidencetopatients.Drugand therapeutics bulletin 57(8):119–124.
Frohna A, Stern D (2005) The nature of qualitative comments in evaluating professionalism. Medical Education 39(8):763–768.
Ha JF, Longnecker N (2010) Doctor-patient communication: a review. Ochsner Journal 10(1):38–43.
HagiharaA,TarumiK(2007)Associationbetweenphysicians’communicativebehaviorsandjudges’decisions
in lawsuits on negligent care. Health Policy 83(2-3):213–222.
Han E, Shiraz F, Haldane V, Koh JJK, Quek RYC, Ozdemir S, Finkelstein EA, Jafar TH, Choong HL, Gan
S, et al. (2019) Biopsychosocial experiences and coping strategies of elderly esrd patients: a qualitative
studytoinformthedevelopmentofmoreholisticandperson-centredhealthservicesinsingapore.BMC
Public Health 19:1–13.

<!-- Page 46 -->

46
Han T, Adams LC, Papaioannou JM, Grundmann P, Oberhauser T, L¨oser A, Truhn D, Bressem KK (2023)
Medalpaca–an open-source collection of medical conversational ai models and training data. arXiv
preprint arXiv:2304.08247 .
Hilton SR, Slotnick HB (2005) Proto-professionalism: how professionalisation occurs across the continuum
of medical education. Medical education 39(1):58–65.
Hu EJ, Shen Y, Wallis P, Allen-Zhu Z, Li Y, Wang S, Wang L, Chen W (2021) Lora: Low-rank adaptation
of large language models. arXiv preprint arXiv:2106.09685 .
Jha V, Bekker H, Duffy S, Roberts T (2006) Perceptions of professionalism in medicine: a qualitative study.
Medical education 40(10):1027–1036.
Kanter MH, Nguyen M, Klau MH, Spiegel NH, Ambrosini VL (2013) What does professionalism mean to
the physician? The Permanente Journal 17(3):87.
Kearney RA (2005) Defining professionalism in anaesthesiology. Medical education 39(8):769–776.
Kee JW, Khoo HS, Lim I, Koh MY (2018) Communication skills in patient-doctor interactions: learning
from patient complaints. Health professions education 4(2):97–106.
KindlerC,SzirtL,SommerD,H¨auslerR,LangewitzW(2005)Aquantitativeanalysisofanaesthetist–patient
communication during the pre-operative visit. Anaesthesia 60(1):53–59.
Kokkodis M, Ipeirotis PG (2021) Demand-aware career path recommendations: A reinforcement learning
approach. Management Science 67(7):4362–4383.
Larsen KM, Smith CK (1981) Assessment of nonverbal communication in the patient-physician interview. J
Fam Pract 12(3):481–488.
LeeD,HosanagarK,NairHS(2018)Advertisingcontentandconsumerengagementonsocialmedia:Evidence
from facebook. Management Science 64(11):5105–5131.
LeeSJ,BackAL,BlockSD,StewartSK(2002)Enhancingphysician-patientcommunication.ASHEducation
Program Book 2002(1):464–483.
Li R, Ghose A, Xu K, Li B (2023a) Predicting consumer in-store purchase using real-time retail video
analytics. Available at SSRN 4513385 .

<!-- Page 47 -->

47
Li Y, Li Z, Zhang K, Dan R, Jiang S, Zhang Y (2023b) Chatdoctor: A medical chat model fine-tuned on a
large language model meta-ai (llama) using medical domain knowledge. Cureus 15(6).
Liga D, Robaldo L (2023) Fine-tuning gpt-3 for legal rule classification. Computer Law & Security Review
51:105864.
LiuX,ZhangB,SusarlaA,PadmanR(2019)Gotoyoutubeandcallmeinthemorning:Useofsocialmedia
for chronic conditions. Liu, X., Zhang, B., Susarla, A., and Padman 257–283.
Liu Y, Han T, Ma S, Zhang J, Yang Y, Tian J, He H, Li A, He M, Liu Z, et al. (2023) Summary of
chatgpt/gpt-4 research and perspective towards the future of large language models. arXiv preprint
arXiv:2304.01852 .
Liu Y, Pant G, Sheng OR (2020) Predicting labor market competition: Leveraging interfirm network and
employee skills. Information Systems Research 31(4):1443–1466.
MachaM,FoutzNZ,LiB,GhoseA(2023)Personalizedprivacypreservationinconsumermobiletrajectories.
Information Systems Research .
Manzoor E, Chen GH, Lee D, Smith MD (2023) Influence via ethos: On the persuasive power of reputation
in deliberation online. Management Science .
MarkidesM(2011)Theimportanceofgoodcommunicationbetweenpatientandhealthprofessionals.Journal
of Pediatric Hematology/Oncology 33:S123–S125.
Minhas R (2007) Does copying clinical or sharing correspondence to patients result in better care? International journal of clinical practice 61(8):1390–1395.
NorthcottS,HilariK(2018)“i’vegotsomebodythere,someonecares”:whatsupportismostvaluedfollowing
a stroke? Disability and rehabilitation 40(20):2439–2448.
NoyS,ZhangW(2023)Experimentalevidenceontheproductivityeffectsofgenerativeartificialintelligence.
Science 381(6654):187–192.
Olson DP, Windish DM (2010) Communication discrepancies between physicians and hospitalized patients.
Archives of internal medicine 170(15):1302–1307.

<!-- Page 48 -->

48
Ommen O, Thuem S, Pfaff H, Janssen C (2011) The relationship between social support, shared decisionmaking and patient’s trust in doctors: a cross-sectional survey of 2,197 inpatients using the cologne
patient questionnaire. International journal of public health 56:319–327.
Ong LM, De Haes JC, Hoos AM, Lammes FB (1995) Doctor-patient communication: a review of the literature. Social science & medicine 40(7):903–918.
OpenAI (2023) Gpt-4 technical report. arXiv preprint arXiv:2303.08774 .
Passi V, Doug M, Peile E, Thistlethwaite J, Johnson N (2010) Developing medical professionalism in future
doctors: a systematic review. International journal of medical education 1:19.
Project MP (2002) Medical professionalism in the new millennium: a physicians’ charter. The Lancet
359(9305):520–522.
RabinowitzD,ReisS,VanRaalteR,AlroyG,BerR(2004)Developmentofaphysicianattributesdatabase
asaresourceformedicaleducation,professionalismandstudentevaluation.MedicalTeacher 26(2):160–
165.
Rathert C, Williams ES, McCaughey D, Ishqaidef G (2015) Patient perceptions of patient-centred care:
empirical test of a theoretical model. Health Expectations 18(2):199–209.
Reisenbichler M, Reutterer T, Schweidel DA, Dan D (2022) Frontiers: Supporting content marketing with
natural language generation. Marketing Science 41(3):441–452.
Sharp S, McAllister M, Broadbent M (2016) The vital blend of clinical competence and compassion: How
patients experience person-centred care. Contemporary nurse 52(2-3):300–312.
Singhal K, Azizi S, Tu T, Mahdavi SS, Wei J, Chung HW, Scales N, Tanwani A, Cole-Lewis H, Pfohl S,
et al. (2023) Large language models encode clinical knowledge. Nature 620(7972):172–180.
Slevin M, Nichols S, Downer S, Wilson P, Lister T, Arnott S, Maher J, Souhami R, Tobias J, Goldstone A,
et al. (1996) Emotional support for cancer patients: what do patients really want? British journal of
cancer 74(8):1275–1279.
Smith CK, Polis E, Hadac RR, et al. (1981) Characteristics of the initial medical interview associated with
patient satisfaction and understanding. J Fam Pract 12(2):283–288.

<!-- Page 49 -->

49
Song Y, Sun T (2023) Ensemble experiments to optimize interventions along the customer journey: A reinforcement learning approach. Management Science .
StraitsResearch (2023) Healthcare chatbots market: Information by end-users (healthcare providers,
patients, payers), mode of delivery (cloud-based, on-premise), component (software, services), and
region—forecast till 2031. Retrieved on November 13, 2023 from https://straitsresearch.com/
report/healthcare-chatbots-market .
Sun C, Adamopoulos P, Ghose A, Luo X (2022) Predicting stages in omnichannel path to purchase: A deep
learning model. Information Systems Research 33(2):429–445.
Swick HM (2000) Toward a normative definition of medical professionalism. Academic medicine 75(6):612–
616.
Van De Camp K, Vernooij-Dassen MJ, Grol RP, Bottema BJ (2004) How to conceptualize professionalism:
a qualitative study. Medical teacher 26(8):696–702.
van Mook WN, de Grave WS, Wass V, O’Sullivan H, Zwaveling JH, Schuwirth LW, van der Vleuten CP
(2009)Professionalism:Evolutionoftheconcept.EuropeanJournalofInternalMedicine 20(4):e81–e84.
VantageMarketResearch (2023) Top trends driving the global healthcare chatbots market, size
will cross usd 431.47 million by 2028, global report by vantage market research. Retrieved
on November 13, 2023 from https://www.vantagemarketresearch.com/industry-report/
healthcare-chatbots-market-1388 .
Wagner P, Hendrich J, Moseley G, Hudson V (2007) Defining medical professionalism: a qualitative study.
Medical education 41(3):288–294.
WalterS,HrabalV,KahleJ,GeibelMA,FrischS,Jerg-BretzkeL(2021)Partnershipandemotionalsupport
in the doctor-patient relationship: A comparison of patient preferences from 1996/1997 versus 2018.
Deutsches A¨rzteblatt International 118(23):405.
Wang W, Bell JJ, Dotson JP, Schweidel DA (2023a) Generative ai and artists: Consumer preferences for
style and fair compensation. Available at SSRN .
WangW,LiB(2023)Learningpersonalizedprivacypreferencefrompublicdata.AvailableatSSRN4483615
.

<!-- Page 50 -->

50
Wang W, Li B, Luo X, Wang X (2023b) Deep reinforcement learning for sequential targeting. Management
Science 69(9):5439–5460.
Wang W, Pei S, Sun T (2023c) Unraveling generative ai from a human intelligence perspective: A battery
of experiments. Available at SSRN 4543351 .
Wear D, Castellani B (2000) The development of professionalism: curriculum matters. Academic Medicine
75(6):602–611.
Wenrich MD, Curtis JR, Ambrozy DA, Carline JD, Shannon SE, Ramsey PG (2003) Dying patients’ need
for emotional support and personalized care from physicians: perspectives of patients with terminal
illness, families, and health care providers. Journal of Pain and Symptom Management 25(3):236–246.
Wilkinson TJ, Wade WB, Knock LD (2009) A blueprint to assess professionalism: results of a systematic
review. Academic medicine 84(5):551–558.
Wu C, Zhang X, Zhang Y, Wang Y, Xie W (2023) Pmc-llama: Further finetuning llama on medical papers.
arXiv preprint arXiv:2304.14454 .
Xie J, Liu X, Dajun Zeng D, Fang X (2022) Understanding medication nonadherence from social media: A
sentiment-enriched deep learning approach. MIS Quarterly 46(1).
Yang J, Jin H, Tang R, Han X, Feng Q, Jiang H, Yin B, Hu X (2023a) Harnessing the power of llms in
practice: A survey on chatgpt and beyond. arXiv preprint arXiv:2304.13712 .
Yang K, Lau RY, Abbasi A (2023b) Getting personal: a deep learning artifact for text-based measurement
of personality. Information Systems Research 34(1):194–222.
Yin K, Fang X, Chen B, Liu Sheng OR (2022) Diversity preference-aware link recommendation for online
social networks. Information Systems Research .
ZhangC,ZhangC,LiC,QiaoY,ZhengS,DamSK,ZhangM,KimJU,KimST,ChoiJ,etal.(2023a)One
small step for generative ai, one giant leap for agi: A complete survey on chatgpt in aigc era. arXiv
preprint arXiv:2304.06488 .
Zhang J, Adomavicius G, Gupta A, Ketter W (2020) Consumption and performance: Understanding longitudinal dynamics of recommender systems via an agent-based simulation framework. Information
Systems Research 31(1):76–101.

<!-- Page 51 -->

51
Zhang M, Luo L (2023) Can consumer-posted photos serve as a leading indicator of restaurant survival?
evidence from yelp. Management Science 69(1):25–50.
ZhangT,LadhakF,DurmusE,LiangP,McKeownK,HashimotoTB(2023b)Benchmarkinglargelanguage
models for news summarization. arXiv preprint arXiv:2301.13848 .
Zhou E, Lee D (2023) Generative ai, human creativity, and art. Available at SSRN .
ZhouM,ZhangJ,AdomaviciusG(2023a)Longitudinalimpactofpreferencebiasesonrecommendersystems’
performance. Information Systems Research .
Zhou T, Wang Y, Yan L, Tan Y (2023b) Spoiled for choice? personalized recommendation for healthcare
decisions: A multiarmed bandit approach. Information Systems Research .