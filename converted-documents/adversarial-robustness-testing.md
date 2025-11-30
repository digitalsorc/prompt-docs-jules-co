---
title: "Adversarial Robustness Testing"
original_file: "./Adversarial_Robustness_Testing.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["prompt-engineering", "llm", "rag", "chain-of-thought", "agents"]
keywords: ["shot", "gpt", "mmlu", "dataset", "means", "suppose", "gemini", "questionandanswer", "questiononly", "answeronly"]
summary: "<!-- Page 1 -->


### MMLU-SR: A Benchmark for Stress-Testing

Reasoning Capability of Large Language Models
WentianWang*

## Usc

SarthakJain PaulKantor JacobFeldman LazarosGallos HaoWang

### Rutgers Rutgers&UW-Madison Rutgers Rutgers Rutgers

Abstract raised concerns about data leakage (i.e., training
modelsonthetestsets),potentiallyrenderingthese
We propose MMLU-SR, a novel dataset deresultsunreliable. Theseseeminglycontradictory
signed to measure the true comprehension
findingsprompttheques"
related_documents: []
---

# Adversarial Robustness Testing

<!-- Page 1 -->


### MMLU-SR: A Benchmark for Stress-Testing

Reasoning Capability of Large Language Models
WentianWang*

## Usc

SarthakJain PaulKantor JacobFeldman LazarosGallos HaoWang

### Rutgers Rutgers&UW-Madison Rutgers Rutgers Rutgers

Abstract raised concerns about data leakage (i.e., training
modelsonthetestsets),potentiallyrenderingthese
We propose MMLU-SR, a novel dataset deresultsunreliable. Theseseeminglycontradictory
signed to measure the true comprehension
findingspromptthequestionofwhetherLLMsare
abilities of Large Language Models (LLMs)
bychallengingtheirperformanceinquestion- genuinely performing reasoning tasks or merely
answeringtaskswithmodifiedterms. Werea- predictingthenexttoken. IfLLMsaretrulycapasoned that an agent that “truly” understands bleofreasoning,theyshouldremainunaffectedby
aconceptcanstillevaluateitwhenkeyterms thereplacementofkeysymbolswithinthetestset.
arereplacedbysuitablydefinedalternateterms,

### Ahallmarkofhumanintelligenceistheability

andsoughttodifferentiatesuchcomprehension
tohandleabstractconceptsandtoassociatethem
frommeretextreplacement. Inourstudy,we
witharbitraryterms(Pennetal.,2008). Withafew
modifiedstandardizedtestquestionsbyreplacexceptionssuchasonomatopoeia,theconnection
ingakeytermwithadummywordalongwith
its definition. The key term could be in the betweenparticularwordsandparticularmeanings
context of questions, answers, or both ques- isarbitrary,andidenticalconceptsareinvokedby
tionsandanswers. Notwithstandingthehigh differentwordsindifferenthumanlanguages(e.g.
scores achieved by recent popular LLMs on dogvschien). Similarly,humanreasonersarecapatheMMLUleaderboard,wefoundasubstanbleofanalogizingstructuralrelationshipsfromone
tialreductioninmodelperformanceaftersuch
domaintoanother,meaningthatconceptualequivreplacement,suggestingpoorcomprehension.
alence can be retained even when details change
Thisnewbenchmarkprovidesarigorousbenchmark for testing true model comprehension, (Gentner and Medina, 1998). It follows that true
andposesachallengetothebroaderscientific human-likecomprehensionshouldbeunimpaired
community. whentermsaresubstitutedforsynonymousterms,
1 Introduction as long as the substitution is comprehensibly defined.
Large Language Models (LLMs) have achieved

### WewonderedwhetherLLMpeformancereflects

impressive quantitative performance on a wide
true human-like comprehension in this sense, or
range of benchmarks, natural language processwhetheritreliesheavilyonthespecifictermsused
ing(Zellersetal.,2019;Wangetal.,2019),general
on training corpora. To assess this, we propose
knowledge question-answering(Hendrycks et al.,
MMLU-SR, a new benchmark dataset that uses
2021;Clarketal.,2018),andcoding(Chenetal.,
symbol replacement to remove some important
2021; others, 2021). Additionally, by integrating
terms from the questions and answers as shown
with some advanced prompting techniques, such
inFigure1. Insteadofrelyingonmemorizedterms,
asChain-of-Thought(CoT)(Weietal.,2023)and
thisapproachtestswhetherLLMscanreasonusing
itsvariants(Yaoetal.,2023;Trivedietal.,2023;
thedefinitionsandconceptsofthoseterms,ensur-
Zhang et al., 2023), LLMs seem to exhibit a ceringamorerobustevaluationoftheirunderstanding.
tain level of reasoning abilities including mathe-

### Our evaluations on GPT-3.5/4, Gemini, and

matics (Zhang et al., 2024) and even causal in-
Llama3 families showed significantly lower perference/discovery(Vashishthaetal.,2023;Wang
formanceonMMLU-SRcomparedtotheoriginal
etal.,2020;Maoetal.,2022;Guptaetal.,2021).

### MMLU,demonstratingtheeffectivenessofourap-

However, some studies (Oren et al., 2023) have
proachinpreventingmodelsfromexploitingmem-
*VisitingstudentatRutgersMLLab. orizeddata. MMLU-SRthusprovidesamorechal-
4202
tcO
4
]LC.sc[
2v86451.6042:viXra

<!-- Page 2 -->

Reasoning or Simply Next Token Prediction?

## Mmlu Mmlu-Sr


### Question Question

Suppose 'Hat' means "the name given to any laboratory technique

### Enzyme assay can be used

that measures enzyme activity within a sample." Hat can be used to
to identify carriers of: identify carriers of:
Answer

### Answer

A. Suppose 'Bard' means 'An inherited disorder that affects the
Symbol lungs, digestive system, and other organs, characterized by the
Replacement production of thick, sticky mucus.' Bard.
B. Suppose 'Jump' means 'A genetic condition causing intellectual
A. Cystic fibrosis. disability, behavioral challenges, and certain physical
B. Fragile X syndrome. characteristics, resulting from a mutation in the FMR1 gene.' Jump.
C. Oculocutaneous albinism. C. Suppose 'Zelly' means 'A group of inherited disorders
D. Tay-Sachs disease. characterized by a lack of melanin production in the skin, hair, and
eyes, leading to light pigmentation.' Zelly.
D. Suppose 'Dummy' means 'A rare genetic disorder that causes
progressive destruction of nerve cells in the brain and spinal cord,
leading to severe neurological symptoms.' Dummy.
D. Tay-Sachs disease. A. Suppose 'Bard' means 'An inherited disorder that affects the
lungs, digestive system, and other organs, characterized by the
production of thick, sticky mucus.' Bard.
Figure1: IllustrationofourMMLU-SRtestingscenarios. Thered-coloredandgreen-coloredwordsrepresentthe
originalsymbolsintheMMLUdatasetshowinginanswersandquestions,whicharereplacedintheMMLU-SR
datasetwithrandomwordsfollowedbytheirdefinitions,showninorangetext. Theexamplequestionfromthe
MMLUdatasetiscorrectlyansweredbybothGPT-3.5-turboandChatGPT-4. However,themodifiedquestionfrom
theMMLU-SR“QuestionandAnswer”datasetisansweredincorrectlybybothmodels.
lengingandrevealingtestofLLMs’truereasoning Theypreservetheoriginalstructureandintentof
abilitiesandunderstanding. MMLUwhileenablingabroaderexaminationof
Our findings indicate that while current LLMs multilingualcapabilities.
excelontraditionalbenchmarks,theyfacesubstan-

### ReasoningCapabilitiesBenchmarks. Several

tialdifficultieswhenkeytermsarereplaced,highadvancedreasoningbenchmarkshavebeendevellightingtheneedforbenchmarkslikeMMLU-SR
opedtoevaluatethereasoningcapabilitiesoflantoensurerobustandcomprehensiveevaluationof
guage models. AGIEval (Zhong et al., 2023) inlanguagemodels.
cludesstandardizedtestsandcivilserviceexamsto
assessreasoningandproblem-solvingskillsinaca-
2 RelatedWorks
demic and professional scenarios. BoolQ (Clark
MMLUVariantsBenchmarks. MMLUVariants et al., 2019) comprises over 15,000 real yes/no
suchasCMMLU(Lietal.,2024)andTMMLU+ questions paired with Wikipedia passages to test
(Tam et al., 2024) are adaptations of the MMLU theabilityofmodelstoinferanswersfromcontexbenchmarkfornon-Englishlanguages;theytrans- tualinformation. GSM8K(Cobbeetal.,2021)fealate the original MMLU questions and answers tures8.5Kgrade-schoolmathproblemsrequiring
into other languages, providing a way to evalu- multistepoperations,targetingtheevaluationofbaatelanguagemodels’performanceinnon-English sictointermediatemathematicalproblem-solving
contexts. These benchmarks are crucial for as- abilities. DROP(Duaetal.,2019),anadversariallysessingthegeneralizabilityandrobustnessofmod- created reading comprehension benchmark, chalelsacrossdifferentlanguagesandculturalsettings. lengesmodelstonavigatereferencesandperform

<!-- Page 3 -->

Question Only 3 MMLU-SRDataset

### Question: Model Input

Suppose 'Hat' means "the name given to any laboratory technique that measures 3.1 DatasetConstruction
enzyme activity within a sample." Hat can be used to identify carriers of:
Answer: WehavedevelopedtheMMLU-SRbenchmarkto
A. Cystic fibrosis.
B. Fragile X syndrome. rigorouslyevaluatethereasoningandunderstand-
C. Oculocutaneous albinism.
D. Tay-Sachs disease. ing capabilities of LLMs. Inspired by ObjectNet

### Model Output

The hypothetical technique "Hat," described as measuring enzyme activity within (Borji, 2020), our benchmark contains three suba sample. Among the diseases listed:
Cystic fibrosis is primarily diagnosed through genetic testing and sweat chloride sets: “QuestionOnly”,“AnswerOnly”,and“Questests, not directly through enzyme activity.
Fragile X syndrome is diagnosed through genetic testing, specifically by tionandAnswer”,eachofferingauniqueperspecidentifying mutations in the FMR1 gene, not through enzyme activity.
Oculocutaneous albinism involves a lack of pigment production and is diagnosed tive on the data to comprehensively assess LLM
through genetic and physical exams, not typically through enzyme activity.
Tay-Sachs disease is characterized by a deficiency of the enzyme hexosaminidase performance. Toreducehumaneffortsinsomere-
A. This deficiency leads to a buildup of specific lipids in the brain and nerve cells,
dundanttasks,weproposedanautomaticprocess
which can be measured through enzyme activity tests.
Given this, the best answer is: D. Tay-Sachs disease. togenerateourdataset.
Figure 2: Example ChatGPT-4 output of MMLU-SR

## Term Extraction and Definition Genera-

‘QuestionOnly”.
tion: Weextractedkeytermsfromthequestionsandanswersacrossall57subjectsusing
the assistance of gpt-3.5-turbo. The processinvolvedcarefulfew-shotprompting,and
weseparatelyextractedthecontextsofquesdiscrete operations such as addition and sorting, tions or answers alone to ensure the model
thusevaluatingtheircapacitytounderstandcom- focusedonextractingtermsratherthansolvplextextsandexecutelogicalreasoningtasks. Be- ing the questions. We also retrieved approyondpurelylanguage-basedevaluation,onthemul- priate definitions within the specific subject
timodalfront, MMNeedle(Wangetal.,2024)in- foreachextractedterm. Fortermswherethe
troduced oneof thefirst multimodal benchmarks automatedprocessprovidedirrelevantorinactoevaluatelong-contextmultimodalreasoningca- curatedefinitions,wemanuallyreviewedand
pabilitiesofmultimodalLLMs. correctedtheseentries(seeAppendixFfordetailsontheextentofmanualmodifications).

### Unlike advanced reasoning benchmarks and


## Dictionary Creation: Once the terms and

MMLU variants for language extension (e.g.,
theirdefinitionswereextractedforeachsub-
CMMLUandTMMLU+),ourMMLU-SRbenchject, we created JSON files where the terms
mark introduces a novel approach. It enhances
served as keys and the definitions as values.
the challenge by replacing key words within the
Thisdictionaryservedasthebasisforreplacquestions with random words, each paired with
ingtermsinthequestionsandanswers.
its definition, to differentiate from other benchmarks. Thisapproachtargetsthemodels’reason-

## DataReplacement: Usingthecreateddictioingabilitiesbypreventingrelianceonmemorized

naries,wereplacedthekeytermsinthequesterms or vocabularies. By altering key symbols,
tions with random dummy words followed

### MMLU-SRensuresthattheevaluationfocuseson

by their definitions to create the “Question
the models’ understanding and reasoning, rather

### Only”dataset. Similarly, wedidthis forthe

thantheirrecognitionofspecificvocabulary,thus
answers to form the “Answer Only” dataset.
providing a more robust assessment of their true
Thisensuredthatthecontextremainedhumancognitive capabilities. We build our benchmark
readable but required reasoning to infer the
on the MMLU dataset because it encompasses a
replacedterms. Somedefinitionsandreplacewiderangeofsubjectsacrossvariousdomains,inmentsrequiredmanualadjustmentstoensure
cludingHumanities,SocialSciences,STEM,and
clarityandaccuracy.

### Otherfields. Thisdiversesubjectmatterensuresa

comprehensiveevaluationoflanguagemodels’rea- 4. CombiningQuestionandAnswerSets: Afsoningcapabilities,incontrasttootherreasoning tercreatingthe“QuestionOnly”and“Answer
benchmarksthatoftenfocusexclusivelyonspecific Only” datasets, we combined them to form
STEMsubjects. the“QuestionandAnswer”dataset. Thisstep

<!-- Page 4 -->

involved ensuring that the terms were con- Answer Only

### Model Input

sistently replaced across both questions and Question:
Enzyme assay can be used to identify carriers of:
answers, maintaining the coherence of the Answer:
A. Suppose 'Bard' means 'An inherited disorder that affects the lungs, digestive system, and other
dataset. organs, characterized by the production of thick, sticky mucus.' Bard.
B. Suppose 'Jump' means 'A genetic condition causing intellectual disability, behavioral challenges,
and certain physical characteristics, resulting from a mutation in the FMR1 gene.' Jump.
C. Suppose 'Zelly' means 'A group of inherited disorders characterized by a lack of melanin

## Final Adjustments: All CSV sheets were production in the skin, hair, and eyes, leading to light pigmentation.' Zelly.

D. Suppose 'Dummy' means 'A rare genetic disorder that causes progressive destruction of nerve
encodedinUTF-8withoutheaders. Wemanu- cells in the brain and spinal cord, leading to severe neurological symptoms.' Dummy.

### Model Output

allyfixedanytyposthatexistedintheoriginal To determine which disorder enzyme assays can identify among the given options, let's analyze
each one:
A. 'Bard' sounds like Cystic Fibrosis. Enzyme assays can indeed be used to identify carriers of
MMLUdatasettoensurethequalityandread- Cystic Fibrosis.
B. 'Jump' is indicative of Fragile X Syndrome. Identification of carriers typically involves genetic
abilityoftheMMLU-SRdataset. testing rather than enzyme assays.
C. 'Zelly' refers to albinism. Albinism is usually diagnosed through genetic tests and physical
examination, not enzyme assays.
TheMMLU-SRdatasetwascreatedusingthese D. 'Dummy' is reminiscent of Huntington's Disease. Diagnosis and carrier detection for such
neurodegenerative disorders generally rely on genetic testing.
Based on this analysis, the most appropriate answer is: A. Bard (Cystic Fibrosis)
meticulous steps. We formed both development
andtestsets,withthedevelopmentsetusedforfew-

### Figure 3: Example ChatGPT-4 output of MMLU-SR

shotlearningandthetestsetreservedforevaluation.
“AnswerOnly”.

### Thisstructuredapproachensuredthatthedataset

effectivelytestedthereasoningabilitiesofLLMs, Question and Answer
differentiatingbetweensimplepatternrecognition Model Input

### Question:

andgenuineunderstanding. Toeffectivelydemon- Suppose 'Hat' means "the name given to any laboratory technique that measures enzyme activity within
a sample." Hat can be used to identify carriers of:

### Answer:

strate how our MMLU-SR dataset can challenge A. Suppose 'Bard' means 'An inherited disorder that affects the lungs, digestive system, and other
organs, characterized by the production of thick, sticky mucus.' Bard.
moresophisticatedmodels,weuseFigure2,Fig- B. Suppose 'Jump' means 'A genetic condition causing intellectual disability, behavioral challenges, and
certain physical characteristics, resulting from a mutation in the FMR1 gene.' Jump.
ure 3, and Figure 4 that feature responses from C. Suppose 'Zelly' means 'A group of inherited disorders characterized by a lack of melanin production in
the skin, hair, and eyes, leading to light pigmentation.' Zelly.
D. Suppose 'Dummy' means 'A rare genetic disorder that causes progressive destruction of nerve cells in
ChatGPT-4. Forcomparativeinsights,examplere- the brain and spinal cord, leading to severe neurological symptoms.' Dummy.
sponsesofChatGPT-3.5areavailablefromTable8, Model Output
Given that 'Hat' is defined as any laboratory technique measuring enzyme activity, we can analyze:
Table9,andTable10inAppendixB. B Ju a m rd p : : r r e e fe fe r r s s t o to C F y r s a ti g c i l F e i X br S o y si n s d , r a o n m d e c . a C n a b r e ri s e c r r i e d e e n n e t d if i f c o a r t i u o s n in t g y p e i n c z a y ll m y e r e a l s ie s s a y o s n genetic testing rather
than enzyme assays.
Zelly: refers to albinism. Diagnosing albinism generally involves genetic tests and physical
3.2 “QuestionOnly”Dataset examination, not typically enzyme assays.
Dummy: refers to a neurological condition like Huntington's Disease. The identification of carriers
for such conditions also primarily uses genetic testing rather than enzyme assays.
Our“QuestionOnly”datasetreplaceskeysymbols Thus, the use of 'Hat' (enzyme assays) is most applicable to: A. Bard (Cystic Fibrosis)
withdummywordsinmostquestionsfromtheorig-
Figure 4: Example ChatGPT-4 output of MMLU-SR
inalMMLUdatasetandkeepstheanswerchoices
“QuestionandAnswer”.
unchanged. However,somestraightforwardquestions, such as those involving only mathematical
operations and numbers or simple questions like ontheprovideddefinitions,ratherthanrelyingon
“Which of the following statements is true?”, re- pre-trainedknowledgeoftheterm‘enzymeassay’.
mainunmodified. Generally,wechangedatleast
3.3 “AnswerOnly”Dataset
oneimportantterminthecontext,replacingitwith
arandomdummywordfollowedbyitsdefinition; Our “Answer Only” dataset modifies the answer
sometimes,multipletermsarereplacedintheques- choices in most text from the original MMLU
tiontofurthertestthemodel’sreasoningcapabili- dataset similarly to the “Question Only” dataset
ties. and keeps the questions unchanged. We ensure
Figure2illustratesanexamplewherethedummy thatatleastoneanswerchoiceismodifiedamong
word‘Hat’isusedtoreplaceterm‘enzymeassay’ allfourchoices. Inspecificcases,suchas“moral
andisdefinedas“thenamegiventoanylaboratory scenarios”wheretheanswersaresimpleTRUEor
technique that measures enzyme activity within FALSEchoices,wemakesubstitutionslike“Supa sample.” In this case, ChatGPT-4 successfully pose ‘Jack’ means ‘True’.” and “Suppose ‘Luck’
recognized ‘Hat’ and understood that the critical means ‘False’.” Despite these modifications, Taaspect was whether the diseases listed in the an- ble 3 still shows the accuracy drops among all
swerchoicescouldbeidentifiedthroughenzyme modelscomparedtotheoriginal“moralscenarios”
activity. Themodelsystematicallyeliminatedeach sheetfromMMLU.Thisunderscoresthechallenge
answer option, except for the last one, as it was posedtomodelsinadaptingtothesesymbolicsubtheonlychoicethatcouldbemeasuredthroughen- stitutions. Figure3demonstratesthatChatGPT-4
zymeactivitytests. Thissetupeffectivelyteststhe wasabletorecognizethereplacedtermsinanswer
model’s ability to comprehend and reason based choicesA,B,andC,identifying‘Bard’as‘Cystic

<!-- Page 5 -->

Table1: Performanceofgpt-4o-mini,gpt-4o,gemini-1.5-pro,andllama3-70b.
Dataset Humanities SocialSciences STEM Other Average

### GPT-4o-mini


### MMLU(5-shot) 0.793 0.858 0.689 0.782 0.771

QuestionOnly(5-shot) 0.744 0.792 0.621 0.724 0.710

### AnswerOnly(5-shot) 0.659 0.738 0.602 0.651 0.655

QuestionandAnswer(5-shot) 0.588 0.666 0.531 0.585 0.585

### GPT-4o


### MMLU(5-shot) 0.880 0.906 0.771 0.854 0.845

QuestionOnly(5-shot) 0.838 0.856 0.702 0.811 0.792

### AnswerOnly(5-shot) 0.764 0.824 0.705 0.760 0.757

QuestionandAnswer(5-shot) 0.708 0.754 0.635 0.712 0.695

### Gemini-1.5-pro


### MMLU(5-shot) 0.849 0.881 0.802 0.815 0.832

QuestionOnly(5-shot) 0.795 0.836 0.700 0.754 0.764

### AnswerOnly(5-shot) 0.741 0.816 0.747 0.739 0.758

QuestionandAnswer(5-shot) 0.690 0.752 0.670 0.681 0.694

### Llama3-70B


### MMLU(5-shot) 0.681 0.868 0.697 0.814 0.765

QuestionOnly(5-shot) 0.635 0.812 0.631 0.770 0.712

### AnswerOnly(5-shot) 0.539 0.683 0.565 0.622 0.602


### QuestionandAnswer(5-shot) 0.523 0.653 0.536 0.591 0.576

Table2: RelativepercentagedropofaccuracyinMMLU-SRcomparedtoMMLU.
Dataset Humanities SocialSciences STEM Other Average

### GPT-4o-mini


### QuestionOnly(5-shot) 6.18% 7.69% 9.87% 7.42% 7.91%


### AnswerOnly(5-shot) 16.90% 13.99% 12.63% 16.75% 15.05%

QuestionandAnswer(5-shot) 25.85% 22.38% 22.93% 25.19% 24.12%

### GPT-4o


### QuestionOnly(5-shot) 4.77% 5.52% 8.95% 5.03% 6.27%


### AnswerOnly(5-shot) 13.18% 9.05% 8.56% 11.01% 10.41%

QuestionandAnswer(5-shot) 19.55% 16.78% 17.64% 16.63% 17.75%

### Gemini-1.5-pro

QuestionOnly(5-shot) 6.36% 5.11% 12.72% 7.48% 8.17%

### AnswerOnly(5-shot) 12.72% 7.38% 6.86% 9.33% 8.89%

QuestionandAnswer(5-shot) 18.73% 14.64% 16.46% 16.44% 16.59%

### Llama3-70B


### QuestionOnly(5-shot) 6.75% 6.45% 9.47% 5.41% 6.93%


### AnswerOnly(5-shot) 20.85% 21.31% 18.94% 23.59% 21.31%

QuestionandAnswer(5-shot) 23.20% 24.77% 23.10% 27.40% 24.71%
Fibrosis’, ‘Jump’ as ‘Fragile X Syndrome’, and disease. Such misidentification led the model to
‘Zelly’as‘Albinism’. Themodelincorrectlyidenti- persistinincorrectlyaffirmingthatchoiceA(‘Bard’
fiedtheterm‘Dummy’as‘Huntington’sDisease’, as‘CysticFibrosis’)wasthecorrectanswer(itis
whilethecorrecttermis‘Tay-SachsDisease’. Both not).
disordersareindeedgenetic,buttheyaredistinctin
3.4 “QuestionandAnswer”Dataset
theirgeneticcausesandmanifestations. Itappears
thatChatGPT-4,focusingonthebroadercategory Our“QuestionandAnswer”datasetintegrateseleof‘geneticdisorder’fromtheprovideddefinition, mentsfromboththe“QuestionOnly”and“Answer
inadvertently linked the description to the wrong Only” datasets, replacing fundamental terms in
boththequestionsandanswerchoiceswithdummy

<!-- Page 6 -->

Table3: DetailedaccuracyfordifferentHumanitiessubjectsacrossdifferentmodels.
MMLU QuestionOnly AnswerOnly QuestionandAnswer

### Subject

GPT Gemini Llama3 GPT Gemini Llama3 GPT Gemini Llama3 GPT Gemini Llama3
FormalLogic 0.730 0.698 0.532 0.603 0.500 0.484 0.643 0.579 0.516 0.556 0.500 0.460
LogicalFallacies 0.902 0.902 0.853 0.883 0.834 0.810 0.853 0.847 0.663 0.834 0.841 0.564
MoralDisputes 0.882 0.832 0.847 0.832 0.806 0.769 0.777 0.830 0.630 0.711 0.749 0.653
MoralScenarios 0.813 0.760 0.318 0.830 0.774 0.289 0.143 0.199 0.318 0.177 0.167 0.253
Philosophy 0.891 0.865 0.865 0.778 0.724 0.772 0.698 0.756 0.598 0.582 0.611 0.582
WorldReligions 0.901 0.895 0.906 0.895 0.836 0.895 0.842 0.813 0.696 0.825 0.772 0.684
HighSchoolEuropeanHistory 0.903 0.885 0.848 0.885 0.855 0.830 0.897 0.849 0.721 0.861 0.818 0.739
HighSchoolUsHistory 0.946 0.922 0.946 0.917 0.902 0.887 0.897 0.863 0.799 0.863 0.819 0.799
HighSchoolWorldHistory 0.937 0.920 0.945 0.924 0.920 0.916 0.907 0.865 0.806 0.882 0.827 0.840
Prehistory 0.948 0.901 0.910 0.904 0.836 0.793 0.843 0.803 0.670 0.790 0.769 0.670
InternationalLaw 0.942 0.926 0.868 0.901 0.860 0.868 0.934 0.843 0.769 0.835 0.802 0.760
Jurisprudence 0.898 0.861 0.852 0.852 0.861 0.806 0.861 0.806 0.602 0.722 0.750 0.556
ProfessionalLaw 0.749 0.666 0.616 0.683 0.627 0.583 0.641 0.585 0.461 0.563 0.544 0.461
Table4: DetailedaccuracyfordifferentSocialSciencesubjectsacrossdifferentmodels.
MMLU QuestionOnly AnswerOnly QuestionandAnswer

### Subject

GPT Gemini Llama3 GPT Gemini Llama3 GPT Gemini Llama3 GPT Gemini Llama3
Econometrics 0.711 0.702 0.693 0.588 0.579 0.570 0.640 0.614 0.561 0.535 0.535 0.421
HighSchoolMacroeconomics 0.921 0.880 0.821 0.849 0.785 0.779 0.813 0.785 0.628 0.721 0.715 0.572
HighSchoolMicroeconomics 0.971 0.929 0.870 0.903 0.870 0.773 0.857 0.815 0.664 0.769 0.744 0.571
HighSchoolGovernmentAndPolitics 0.984 0.974 0.969 0.979 0.943 0.938 0.943 0.922 0.798 0.922 0.845 0.782
PublicRelations 0.836 0.746 0.755 0.755 0.755 0.736 0.664 0.682 0.600 0.627 0.646 0.555
SecurityStudies 0.824 0.841 0.824 0.788 0.792 0.767 0.731 0.796 0.673 0.633 0.714 0.624
UsForeignPolicy 0.930 0.940 0.930 0.920 0.930 0.890 0.870 0.880 0.740 0.810 0.810 0.780
HumanSexuality 0.931 0.893 0.855 0.924 0.855 0.840 0.863 0.847 0.710 0.802 0.756 0.756
Sociology 0.935 0.891 0.920 0.900 0.896 0.841 0.881 0.881 0.806 0.831 0.851 0.786
HighSchoolGeography 0.955 0.939 0.924 0.894 0.909 0.833 0.884 0.864 0.737 0.813 0.813 0.662
HighSchoolPsychology 0.965 0.938 0.921 0.923 0.917 0.884 0.927 0.912 0.719 0.872 0.859 0.739
ProfessionalPsychology 0.908 0.895 0.845 0.845 0.801 0.788 0.817 0.791 0.627 0.719 0.737 0.601
wordsfollowedbytheirdefinitions. Asillustrated The evaluation for GPT and Gemini models was
in Figure 4, ChatGPT-4 successfully interpreted conducted using the Gemini-benchmark pipeline
the original terms for each replaced term in an- (Akteretal.,2023). Forthesemodels,wesetthe
swer choices A through C. However, similar to temperatureparameterto0andutilizedcarefully
theresultsseeninFigure3,themodelincorrectly crafted prompts that required responses in the
recognized the term in the last answer choice D format of “Answer: Letter of Choice.” This
(‘Dummy’ for Huntington’s Disease), leading to approachensuresthatthegeneratedresponsesare
anincorrectanswer. Thisoutcomecontrastswith directly comparable and suitable for evaluation.
Figure 2, where ChatGPT-4 correctly answered Additionally, both models were evaluated in
thequestionswhenonlythequestionsweremod- the 5-shot setting, using examples from our
ified. This illustrates that as complexity in con- development dataset to enhance their contextual
text increases, with terms being replaced in both understanding. Llama3 was evaluated using the
questionsandanswers,themodelstrugglestoac- lm-evaluation-harness framework (Gao et al.,
curately identify the correct original term, conse- 2023). Thismodelemployedadifferentevaluation
quentlyleadingtoanincorrectanswerchoice. strategy; it uses log likelihood to determine the
model’s responses. Consistent with the other
4 Experiments models,Llama3alsousesthesame5-shotsetting,
ensuring a standardized comparison across all
4.1 EvaluationProtocol tests. Thecompleteresultsofallsevenmodelsare
availableinAppendixE.
We evaluated seven models across OpenAI,
Gemini, Llama families: gpt-3.5-turbo,
gpt-4o-mini, gpt-4o, gemini-1.0-pro,
gemini-1.5-pro, llama3-8b, and llama3-70b.

<!-- Page 7 -->

Table5: DetailedaccuracyfordifferentSTEMsubjectsacrossdifferentmodels.
MMLU QuestionOnly AnswerOnly QuestionandAnswer

### Subject

GPT Gemini Llama3 GPT Gemini Llama3 GPT Gemini Llama3 GPT Gemini Llama3
AbstractAlgebra 0.660 0.690 0.380 0.470 0.550 0.370 0.640 0.730 0.400 0.460 0.520 0.400
CollegeMathematics 0.490 0.680 0.510 0.420 0.630 0.490 0.440 0.650 0.460 0.410 0.610 0.480
HighSchoolStatistics 0.769 0.866 0.699 0.708 0.708 0.657 0.750 0.829 0.620 0.644 0.662 0.597
ElementaryMathematics 0.735 0.921 0.606 0.675 0.786 0.521 0.706 0.900 0.561 0.661 0.825 0.497
HighSchoolMathematics 0.541 0.700 0.422 0.537 0.504 0.356 0.541 0.615 0.426 0.511 0.526 0.367
Astronomy 0.947 0.901 0.921 0.908 0.829 0.849 0.888 0.849 0.697 0.855 0.796 0.684
CollegePhysics 0.686 0.716 0.559 0.559 0.647 0.451 0.618 0.745 0.431 0.480 0.608 0.422
ConceptualPhysics 0.911 0.932 0.783 0.804 0.757 0.677 0.791 0.843 0.494 0.685 0.698 0.447
HighSchoolPhysics 0.748 0.782 0.563 0.649 0.556 0.530 0.589 0.616 0.477 0.543 0.596 0.450
CollegeChemistry 0.570 0.610 0.580 0.540 0.550 0.570 0.550 0.530 0.480 0.480 0.560 0.470
HighSchoolChemistry 0.759 0.788 0.734 0.709 0.685 0.631 0.670 0.680 0.537 0.586 0.626 0.468
CollegeBiology 0.951 0.868 0.931 0.938 0.882 0.854 0.924 0.861 0.708 0.833 0.826 0.625
HighSchoolBiology 0.958 0.929 0.903 0.932 0.893 0.858 0.884 0.858 0.713 0.858 0.829 0.729
CollegeComputerScience 0.790 0.790 0.670 0.690 0.610 0.650 0.760 0.730 0.610 0.670 0.660 0.570
ComputerSecurity 0.840 0.820 0.830 0.830 0.770 0.750 0.760 0.730 0.660 0.760 0.610 0.720
HighSchoolComputerScience 0.910 0.920 0.870 0.860 0.880 0.790 0.880 0.910 0.820 0.850 0.870 0.740
MachineLearning 0.777 0.714 0.652 0.661 0.643 0.589 0.643 0.661 0.527 0.580 0.580 0.509
ElectricalEngineering 0.841 0.807 0.745 0.752 0.724 0.655 0.655 0.710 0.510 0.566 0.655 0.490
Table6: DetailedaccuracyfordifferentOthersubjectsacrossdifferentmodels.
MMLU QuestionOnly AnswerOnly QuestionandAnswer

### Subject

GPT Gemini Llama3 GPT Gemini Llama3 GPT Gemini Llama3 GPT Gemini Llama3
Anatomy 0.911 0.793 0.807 0.874 0.733 0.726 0.815 0.667 0.563 0.726 0.659 0.578
ClinicalKnowledge 0.898 0.838 0.849 0.811 0.785 0.740 0.796 0.755 0.638 0.713 0.709 0.608
CollegeMedicine 0.832 0.844 0.757 0.780 0.786 0.740 0.798 0.763 0.647 0.717 0.740 0.659
HumanAging 0.830 0.807 0.807 0.794 0.744 0.758 0.704 0.740 0.457 0.632 0.691 0.471
MedicalGenetics 0.960 0.910 0.830 0.900 0.850 0.820 0.840 0.780 0.570 0.830 0.740 0.550
Nutrition 0.899 0.876 0.853 0.863 0.758 0.804 0.798 0.784 0.663 0.699 0.703 0.647
ProfessionalMedicine 0.956 0.864 0.868 0.919 0.776 0.868 0.901 0.783 0.754 0.842 0.735 0.754
Virology 0.578 0.578 0.536 0.548 0.506 0.488 0.524 0.542 0.452 0.524 0.494 0.404
BusinessEthics 0.860 0.850 0.750 0.890 0.780 0.720 0.750 0.670 0.500 0.710 0.640 0.480
Management 0.913 0.893 0.913 0.883 0.816 0.903 0.757 0.835 0.728 0.767 0.767 0.650
Marketing 0.949 0.940 0.923 0.906 0.927 0.880 0.838 0.846 0.615 0.808 0.803 0.662
GlobalFacts 0.650 0.600 0.530 0.540 0.540 0.430 0.580 0.690 0.540 0.520 0.470 0.410
Miscellaneous 0.955 0.955 0.903 0.932 0.877 0.860 0.861 0.847 0.692 0.840 0.791 0.616
ProfessionalAccounting 0.766 0.663 0.638 0.716 0.674 0.596 0.681 0.638 0.514 0.631 0.596 0.489
4.2 ResultsandAnalysis formanceissimilarlyobservedintheothermodels.
General Trend. Table 1 shows the accu- We observe a crucial trend in decreasing accuracy of the four models gpt-4o-mini, gpt-4o, racyacrossdatasets: The“QuestionOnly”dataset
gemini-1.5-pro, and llama3-70b evaluated in experiences the least drop, followed by the “AnbothMMLUandourMMLU-SR.Thedatahigh- swer Only” dataset, with the most significant
lights how each model performs in the Humani- decline occurring in the “Question and Answer”
ties,SocialSciences,STEM,andOtheracademic dataset. This trend can be primarily attributed to
fields, providing average scores for each subset. two major reasons: (1) When only the question
Weobserveconsistentdropinmodelperformance ismodified,themodelretainstheoriginalanswer
across all subsets when transitioning from the choices,facilitatingtheinferenceofthemodified
standard MMLU dataset to the more challenging question’smeaning;incontrast,alteringtheanswer
MMLU-SR dataset, as evidenced by the decline choices removes this contextual aid, challenging
in average accuracy from 0.771 on the MMLU themodel’sabilitytocorrectlymatchthequestion
datasetto0.710,0.655,and0.585,onourMMLU- with the appropriate answer. (2) Answer choices
SR’s“QuestionOnly”,“AnswerOnly”,and“Ques- are typically more concise and therefore lack the
tion and Answer” subsets, respectively, for the extensivecontextfoundinquestions;consequently,
gpt-4o-minimodel. Thistrendofdecreasedper- replacingtermsintheanswersnotonlyintroduces

<!-- Page 8 -->

ambiguitybutalsodemandsmorecomplexinfer- and models, indicating a high sensitivity to
ential reasoning, disrupting the model’s learned contextual changes in this area. Similarly,
pattern-recognition strategies and resulting in a llama3-70b follows closely with a 27.40%
greateraccuracydrop. Theobservationsabovealso drop, which is the highest in the Other catjustifythedesignofourMMLU-SRonthreevari- egory for this model. gemini-1.5-pro also
ants (i.e., “Question Only”, “Answer Only”, and shows a substantial drop of 16.44%, though
“QuestionandAnswer”). slightly less compared to the other models,
Accuracy Drop in Each Category. Table 2 suggestingthatthe“Other”category,likeHushows several aspects in the relative percent- manities, might be more context-dependent
age drop of accuracy in MMLU-SR compared and hence more susceptible to performance
to that in MMLU across different categories degradationwhensymbolsarereplaced.
forgpt-4o-mini,gpt-4o,gemini-1.5-pro,and
llama3-70b: DetailedAccuracyDropinEachSubject. Table 3 shows a detailed comparison of accuracy

## Humanities and Social Sciences. For scoresacrossdifferentmodelsevaluatedonvarious

gpt-4o-miniandgpt-4o,theaccuracydrops
subjectsintheHumanitiescategory. TheMMLU
significantlyintheHumanitiescategory,with scoresserveasabaselineforcomparison. gpt-4o
aslightlylowerdropinSocialSciences. The demonstratesexceptionalperformanceacrossmost
gemini-1.5-pro shows the smallest perfor- subjects in this category, often leading in accumancedeclineintheHumanitiesandSocial racy,particularlyincomplexsubjectslikePhiloso-
Sciencecategoriescomparedtotheothertwo phyandInternationalLaw. gemini-1.5-proalso
modelsevaluated. llama3-70bexhibitsapat- showsstrongperformance,butgpt-4ofrequently
ternsimilartogpt-4o-mini,withtheHuman- matchesorexceedsitsaccuracy. Notably,gpt-4o
itiesandSocialSciencescategoriesshowing performs particularly well in subjects like High
amoderatepercentagedrop, thoughslightly SchoolWorldHistoryandJurisprudence. However,
higher than gpt-4o-mini, in the “Answer allmodelscontinuetostrugglewithMoralScenar-
Only”and“QuestionandAnswer”dataset. ios, where the accuracy score drops significantly,
particularlyforllama3-70b,whichshowsadras-

## STEM. For gemini-1.5-pro and

tic decrease, reflecting a higher sensitivity to the
llama3-70b, the STEM category shows a
challengesposedbytheMMLU-SRdatasets
relatively moderate decrease in accuracy
Table4showsadetailedcomparisonofaccuracy
across the MMLU-SR datasets. Notably,
acrossdifferentmodelsevaluatedonvarioussubgemini-1.5-pro experiences the highest
jects in the Social Science category. We observe
drop of 12.72% in the “Question Only”
thatallmodelsperformexceptionallywellinSocial
dataset, indicating some sensitivity in this
Science on MMLU, particularly in High School
area. llama3-70b demonstrates a similar

### GovernmentandPolitics,wheregpt-4oachieves

trend, with the highest drop of 9.47% in the
animpressiveaccuracyof0.984. Whilethereisstill
STEM category, suggesting both models
adropinaccuracyfromMMLUtoMMLU-SR’s
retain some robustness in STEM but are
“Question and Answer” dataset, gpt-4o demonstill impacted by symbol replacement. On
strates remarkable resilience, maintaining accuthe other hand, gpt-4o-mini experiences a
racy levels around 0.7∼0.9 across most subjects.
higherdropinthe“AnswerOnly”and“Ques-
Thisperformancesignificantlyoutpacestheother
tionandAnswer”datasets,particularlywith
models, particularlyinsubjectslikeHighSchool
a 22.93% drop in the latter, highlighting its
PsychologyandSociology. Thedropinaccuracy,
relativevulnerabilityinthisdomaincompared
thoughlesspronouncedforgpt-4o,stillillustrates
togemini-1.5-proandllama3-70b.
howoursymbolreplacementmethodincreasesdif-

## Other. TheOthercategorygenerallyshowsa ficulty, effectively stress-testing the models’ reasignificantdropacrossallmodelsanddatasets, soning capabilities versus mere memorization of

with the highest drops often observed in the pre-trainedterms.
“Question and Answer” dataset. For exam- Table5showsadetailedcomparisonofaccuracy
ple,gpt-4o-miniexperiencesanotabledrop acrossvariousSTEMsubjectsfordifferentmodels.
of25.19%, thehighestamongallcategories Eachmodeldemonstratedvaryingdegreesofsuc-

<!-- Page 9 -->

cessacrossthesubjects,withnotabledifficultiesin thissysteminstructionacrosstheentireMMLU-SR
someareas. CollegeMathematicsandHighSchool datasetaswell,withresultsshowninTable11from
Mathematicsremainchallengingforallmodels,in- AppendixC.Theresultsindicatethatwhilethesyscludinggpt-4o,withaccuracydroppingtoaround teminstructionslightlyimprovesaccuracyinthe
0.4to0.5inMMLU-SR’s“QuestionandAnswer” “QuestionOnly”and“AnswerOnly”datasets,the
dataset. However,gpt-4oshowsmarkedimprove- modelstillstruggleswiththeincreasedcomplexity
mentinsubjectslikeAstronomy,CollegeBiology, inthe“QuestionandAnswer”dataset.
and High School Biology, maintaining high ac-
5 Conclusion
curacy even in the more challenging MMLU-SR
datasets. The subject with the lowest accuracies

### WeintroducedMMLU-SR,anovelbenchmarkthat

amongallmodelsisstillHighSchoolMathematics,
challengesLLMsbyreplacingkeytermsinqueswherellama3-70bstrugglesthemost,especially
tions with random words followed by their defiintheAnswerOnly”and“QuestionandAnswer”
nitions, aiming to test the models’ reasoning and
datasets. Similarly,CollegePhysicsandAbstract
comprehensionabilitiesratherthantheirmemoriza-
Algebra also show significant drops in accuracy
tionskills. Ourevaluationacrossmultipledomains
acrossallmodels,highlightingthepersistentchalrevealed that popular LLMs suffer from signifilengesinsubjectsinvolvingextensivecalculations
cantdropsinperformancewiththesemodifications,
andcomplexproblem-solving.
highlighting their reliance on memorized terms.
Table6showsadetailedcomparisonofaccuracy

### MMLU-SR’suniqueapproachaddressesconcerns

scoresacrossdifferentmodelsevaluatedonvarious
aboutoverfittingtotraditionalbenchmarksandprosubjects in the Other category. We observe that
vides a more rigorous measure of true language
gpt-4o performs exceptionally well in MMLU,
understanding. Thisdatasetwillenableresearchers
withaccuracyconsistentlyabove0.9inmostsubtobetteridentifyandaddressthereasoninglimitajects, significantly outperforming other models.
tionsofcurrentLLMs,fosteringthedevelopment
Marketing stands out with a particularly high acofmorerobustandgenuinelyintelligentmodels.
curacyof0.949forgpt-4o,indicatingoutstanding
performanceinthissubject. ProfessionalAccount- 6 Acknowledgements
ing shows improved performance with gpt-4o,

### We thank the anonymous reviewers for their

achievinganaccuracyof0.766inMMLU.Virology remains challenging, but gpt-4o shows im- thoughtful feedback and for recognizing the significance and contributions of our research. This
provementwithanaccuracyof0.578. Whilethere
research is based on work partially supported by
isstilladropinaccuracyfromMMLUtoMMLU-
SR’s“QuestionandAnswer”dataset,gpt-4omain- DARPA Grant HR00112420363, NSF Grant IIS-
2127918,andNSFCAREERAwardIIS-2340125.
tains relatively high performance, with accuracy
generallystayingabove0.7formostsubjects. Even
inchallengingareaslikeVirologyandGlobalFacts,

### References

gpt-4odemonstratesresilience,maintainingaccuracylevelssignificantlyhigherthanothermodels. S. N. Akter, Z. Yu, A. Muhamed, T. Ou, A. Bäuerle,
Á.A.Cabrera,K.Dholakia,C.Xiong,andG.Neubig.

### CoTandSystemInstruction. Wedevelopeda


## Anin-depthlookatgemini’slanguageabilities.

simplebaselinetotestourMMLU-SRdataseton
arXivpreprintarXiv:2312.11444.
morerecentandsophisticatedmodelslikeGPT-4.
This involves adding the instruction “Let’s think Ali Borji. 2020. Objectnet dataset: Reanalysis and
correction. Preprint,arXiv:2004.02042.
stepbystep”attheendofanswerchoicestoenable
zero-shot CoT prompting. As shown in Table 7 MarkChenetal.2021. Evaluatinglargelanguagemodfrom Appendix A, we also included a system in- elstrainedoncode. Preprint,arXiv:2107.03374.
structioninformingChatGPT-4thatthefollowing
Christopher Clark, Kenton Lee, Ming-Wei Chang,
questionswouldinvolvesymbolreplacementwith

### Tom Kwiatkowski, Michael Collins, and Kristina

arbitrarydefinitions. However,theexampledemon- Toutanova. 2019. Boolq: Exploring the surprisstrates that despite applying (zero-shot) CoT, the ingdifficultyofnaturalyes/noquestions. Preprint,
arXiv:1905.10044.
modelstillincorrectlyinterpretstheterm‘Dummy’
inchoiceDas‘neurodegenerativedisorder,’lead-

### PeterClark,IsaacCowhey,OrenEtzioni,TusharKhot,

ing to the wrong answer, choice A. We applied AshishSabharwal,CarissaSchoenick,andOyvind

<!-- Page 10 -->

Tafjord.2018. Thinkyouhavesolvedquestionan- Z.-R. Tam, Y.-T. Pai, Y.-W. Lee, S. Cheng, and H.-
swering? tryarc,theai2reasoningchallenge. ArXiv, H. Shuai. 2024. An improved traditional chinese
abs/1803.05457. evaluationsuiteforfoundationmodel. arXivpreprint
arXiv:2403.01858.
Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian,
Harsh Trivedi, Niranjan Balasubramanian, Tushar

### MarkChen,HeewooJun,LukaszKaiser,Matthias


### Khot, and Ashish Sabharwal. 2023. Interleav-


### Plappert, Jerry Tworek, Jacob Hilton, Reiichiro

ing retrieval with chain-of-thought reasoning for
Nakano, Christopher Hesse, and John Schulman.
knowledge-intensivemulti-stepquestions. Preprint,

## Training verifiers to solve math word probarXiv:2212.10509.

lems. Preprint,arXiv:2110.14168.

### AniketVashishtha, AbbavaramGowthamReddy, Ab-

DheeruDua,YizhongWang,PradeepDasigi,Gabriel hinav Kumar, Saketh Bachu, Vineeth N Balasub-
Stanovsky,SameerSingh,andMattGardner.2019. ramanian, and Amit Sharma. 2023. Causal infer-
Drop: Areadingcomprehensionbenchmarkrequir- ence using llm-guided discovery. arXiv preprint
ing discrete reasoning over paragraphs. Preprint, arXiv:2310.15117.
arXiv:1903.00161.

### Alex Wang, Amanpreet Singh, Julian Michael, Felix

LeoGao,JonathanTow,BaberAbbasi,StellaBiderman, Hill, Omer Levy, and Samuel R. Bowman. 2019.
SidBlack,AnthonyDiPofi,CharlesFoster,Laurence Glue: A multi-task benchmark and analysis plat-
Golding,JeffreyHsu,AlainLeNoac’h,HaonanLi, formfornaturallanguageunderstanding. Preprint,
KyleMcDonell,NiklasMuennighoff,ChrisOciepa, arXiv:1804.07461.

### Jason Phang, Laria Reynolds, Hailey Schoelkopf,

Hengyi Wang, Haizhou Shi, Shiwei Tan, Weiyi Qin,
Aviya Skowron, Lintang Sutawika, Eric Tang, An-

### Wenyuan Wang, Tunyu Zhang, Akshay Nambi,

ishThite, BenWang, KevinWang, andAndyZou.

### Tanuja Ganu, and Hao Wang. 2024. Multimodal


## A framework for few-shot language model

needleinahaystack: Benchmarkinglong-contextcaevaluation.
pabilityofmultimodallargelanguagemodels. arXiv
preprintarXiv:2406.11230.
D. Gentner and J. Medina. 1998. Similarity and the
developmentofrules. Cognition,65(2/3):263–297.
Yuhao Wang, Vlado Menkovski, Hao Wang, Xin Du,
and Mykola Pechenizkiy. 2020. Causal discovery
Shantanu Gupta, Hao Wang, Zachary Lipton, and fromincompletedata: Adeeplearningapproach. In
YuyangWang.2021. Correctingexposurebiasfor AAAIStarAIWorkshop.
linkrecommendation. InICML.

### J.Wei,X.Wang,D.Schuurmans,M.Bosma,B.Ichter,

Dan Hendrycks, Collin Burns, Steven Basart, Andy F.Xia,E.Chi,Q.Le,andD.Zhou.2023. Chain-of-
Zou,MantasMazeika,DawnSong,andJacobStein- thoughtpromptingelicitsreasoninginlargelanguage
hardt.2021. Measuringmassivemultitasklanguage models. arXivpreprintarXiv:2201.11903.
understanding. InProceedingsoftheInternational
Shunyu Yao, Dian Yu, Jeffrey Zhao, Izhak Shafran,
ConferenceonLearningRepresentations(ICLR).

### Thomas L. Griffiths, Yuan Cao, and Karthik

Narasimhan. 2023. Tree of thoughts: Deliber-

### H.Li,Y.Zhang,F.Koto,Y.Yang,H.Zhao,Y.Gong,

ate problem solving with large language models.
N.Duan,andT.Baldwin.2024. Cmmlu: Measuring
Preprint,arXiv:2305.10601.
massivemultitasklanguageunderstandinginchinese.
arXivpreprintarXiv:2306.09212. Rowan Zellers, Ari Holtzman, Yonatan Bisk, Ali

### Farhadi, and Yejin Choi. 2019. Hellaswag: Can

Chengzhi Mao, Kevin Xia, James Wang, Hao Wang, a machine really finish your sentence? Preprint,
JunfengYang,EliasBareinboim,andCarlVondrick. arXiv:1905.07830.

## Causaltransportabilityforvisualrecognition.

InCVPR. BoningZhang,ChengxiLi,andKaiFan.2024. Mario
eval: Evaluate your math llm with your math llm–
Y. Oren, N. Meister, N. Chatterji, F. Ladhak, and a mathematical dataset evaluation toolkit. arXiv
T. B. Hashimoto. 2023. Proving test set contamipreprintarXiv:2404.13925.
nationinblackboxlanguagemodels. arXivpreprint
Zhuosheng Zhang, Aston Zhang, Mu Li, and Alex
arXiv:2310.17623.

### Smola.2023. Automaticchainofthoughtprompting

in large language models. In The Eleventh Inter-
ShuaiLuothers.2021. Codexglue: Amachinelearnnational Conference on Learning Representations
ingbenchmarkdatasetforcodeunderstandingand

## (Iclr2023).

generation. CoRR,abs/2102.04664.

### Wanjun Zhong, Ruixiang Cui, Yiduo Guo, Yaobo

D. C. Penn, K. J. Holyoak, and D. J. Povinelli. 2008. Liang,ShuaiLu,YanlinWang,AminSaied,Weizhu
Darwin’s mistake: explaining the discontinuity be- Chen, and Nan Duan. 2023. Agieval: A humantweenhumanandnonhumanminds. Behavioraland centricbenchmarkforevaluatingfoundationmodels.
BrainSciences,31(2):109–130. Preprint,arXiv:2304.06364.

<!-- Page 11 -->

A CoTExamples and llama3-70b. The percentage drop of each
modelisshowninTable14.

### Table7showsanexampleofincorrectanswerusing

zero-shotCoTwithasysteminstructionproduced F NumbersofHumanModifiedTerms
bytheChatGPT-4onMMLU-SR’s“Questionand

### Figure5showsthenumberofmanuallymodified


### Answer”dataset. ThecorrectanswerischoiceD,

termdefinitionsacross41subjectglossaries. These
butChatGPT-4respondedwithchoiceA.
glossaries were created by consolidating related
B ExamplesofChatGPT-3.5Response topicsfromtheoriginal57subjectsintheMMLU
dataset. Of the 28,676 terms initially generated
Table 8 shows an example of incorrect answer bygpt-3.5-turboforthese41subjects,approxiproduced by the ChatGPT-3.5 on MMLU-SR’s mately1,197(4.2%)requiredhumanmodification.
“Question and Answer” dataset. Table 9 shows
an example of incorrect answer produced by the
ChatGPT-3.5onMMLU-SR’s“QuestionandAnswer” dataset. Table 10 shows an example of incorrect answer produced by the ChatGPT-3.5 on
MMLU-SR’s“QuestionandAnswer”dataset.

### C SystemInstructionExample


### Table 11 shows the performance comparison of

gemini-1.0-pro with and without using the systeminstruction“IneachofthequestionsthatIask,

### I will replace some of the words that you might

knowwithawordthatisarbitrarilyassignedaspecific meaning just for this test. The meaning of
these arbitrary definition may change with every
question.”

### D HardMMLU-SRExample

Table 12 illustrates a challenging example mentioned in the “Question and Answer” section in
the main paper. In the question, we substituted
“enzyme assay” with a synonym, “protein”, and
used the original terms from the MMLU dataset
asplaceholdersintheanswerchoices,eachpaired
with a definition. ChatGPT-4 correctly identified
theterm“Tay-SachsDisease”butassociateditwith
theincorrectanswerchoiceanddefinition,which
wasmeantfor“FragileXsyndrome.” Thisexample demonstrates that ChatGPT-4 can be misled
by the complexity of the dataset, tending to rely
on pre-existing knowledge rather than engaging
in substantive reasoning to align terms with their
definitions.

### E CompleteExperimentResults

Table 13 shows our complete experiment results of different LLMs including gpt-3.5-turbo, gpt-4o-mini,
gemini-1.0-pro, gemini-1.5-pro, llama3-8b

<!-- Page 12 -->

Table7: Exampleofincorrectoutputusingzero-shotCoTwithsysteminstruction.
SystemPrompt IneachofthequestionsthatIask, Iwillreplacesomeofthewordsthatyou
might know with a word that is arbitrarily assigned a specific meaning just
forthistest. Themeaningofthesearbitrarydefinitionmaychangewithevery
question.
Input Suppose‘Hat’means‘thenamegiventoanylaboratorytechniquethatmeasures
enzymeactivitywithinasample.’ Hatcanbeusedtoidentifycarriersof:
A.Suppose‘Bard’means‘Aninheriteddisorderthataffectsthelungs,digestive
system, and other organs, characterized by the production of thick, sticky
mucus.’ Bard.
B.Suppose‘Jump’means‘Ageneticconditioncausingintellectualdisability,
behavioral challenges, and certain physical characteristics, resulting from a
mutationintheFMR1gene.’ Jump.
C.Suppose‘Zelly’means‘Agroupofinheriteddisorderscharacterizedbyalack
ofmelaninproductionintheskin,hair,andeyes,leadingtolightpigmentation.’
Zelly.
D.Suppose‘Dummy’means‘Araregeneticdisorderthatcausesprogressive
destructionofnervecellsinthebrainandspinalcord,leadingtosevereneurologicalsymptoms.’ Dummy.
Let’sthinkstepbystep.
Output In this scenario, Hat is used to detect variations or abnormalities in enzyme
levelsthatmightbeindicativeofcertaingeneticdisorders.
A: Bard refers to cystic fibrosis. Areas of land (Jack) often have boundaries
(Winky)thatseparatethemfromotherareas.
B: Jump refers to Fragile X syndrome, primarily involves genetic testing to
detectthespecificmutationratherthanenzymeactivitymeasurements.
C:Zellyreferstoconditionssuchasalbinism,whicharetypicallydiagnosed
basedonpigmentabsenceratherthanenzymeactivity,althoughsomebiochemicaltestscanberelevantinspecificcontexts.
D:Dummycouldbereferringtoseveralneurodegenerativedisorders,which
might be associated with enzyme activities related to nerve cell function or
metabolicprocesses,butgenerally,suchdisordersarediagnosedthroughgenetic
markersandneuroimagingratherthanenzymeactivityalone.
Giventheseexplanations,thebestmatchfor‘Hat’intermsofbeingatechnique
tomeasureenzymeactivityusefulfordiagnosiswouldbeA,‘Bard’ascystic
fibrosis,duetoitsdirectrelationshipwithenzymedysfunctionandmeasurement.
✗

<!-- Page 13 -->

Table8: ExampleofincorrectresponsegeneratedbyChatGPT-3.5in“QuestionOnly”dataset.
Input Suppose‘Hat’means“thenamegiventoanylaboratorytechniquethatmeasures
enzymeactivitywithinasample.” Hatcanbeusedtoidentifycarriersof:
A.Cysticfibrosis.
B.FragileXsyndrome.
C.Oculocutaneousalbinism.

### D.Tay-Sachsdisease

Output “Hat”inthiscontextreferstoanenzymeassaytechniqueratherthanagenetic
condition or disease. Therefore, it wouldn’t be used to identify carriers of
genetic disorders like cystic fibrosis, Fragile X syndrome, oculocutaneous
albinism, or Tay-Sachs disease. It’s essential to keep in mind the specific
contextinwhichtermsareusedinscientificfields! ✗
Table9: ExampleofincorrectresponsegeneratedbyChatGPT-3.5in“AnswerOnly”dataset.

### Input Enzymeassaycanbeusedtoidentifycarriersof:

A.Suppose‘Bard’means‘Aninheriteddisorderthataffectsthelungs,digestive
system, and other organs, characterized by the production of thick, sticky
mucus.’ Bard.
B.Suppose‘Jump’means‘Ageneticconditioncausingintellectualdisability,
behavioral challenges, and certain physical characteristics, resulting from a
mutationintheFMR1gene.’ Jump.
C.Suppose‘Zelly’means‘Agroupofinheriteddisorderscharacterizedbyalack
ofmelaninproductionintheskin,hair,andeyes,leadingtolightpigmentation.’
Zelly.
D.Suppose‘Dummy’means‘Araregeneticdisorderthatcausesprogressive
destructionofnervecellsinthebrainandspinalcord,leadingtosevereneurologicalsymptoms.’ Dummy.
Output An enzyme assay could be used to identify carriers of Bard, Jump, Zelly, or
Dummyifthespecificenzymeassociatedwitheachdisorderisknownandcan
betestedfor. Enzymeassaysarecommonlyusedingenetictestingtodetect
thepresenceorabsenceofspecificenzymesortheiractivitylevels,whichcan
provideinformationaboutanindividual’sgeneticmakeupandpotentialcarrier
statusforcertaingeneticdisorders. ✗

<!-- Page 14 -->

Table10: ExampleofincorrectresponsegeneratedbyChatGPT-3.5in“QuestionandAnswer”dataset.
Input Suppose’Hat’means“thenamegiventoanylaboratorytechniquethatmeasures
enzymeactivitywithinasample.” Hatcanbeusedtoidentifycarriersof
A.Suppose‘Bard’means‘Aninheriteddisorderthataffectsthelungs,digestive
system, and other organs, characterized by the production of thick, sticky
mucus.’ Bard.
B.Suppose‘Jump’means‘Ageneticconditioncausingintellectualdisability,
behavioral challenges, and certain physical characteristics, resulting from a
mutationintheFMR1gene.’ Jump.
C.Suppose‘Zelly’means‘Agroupofinheriteddisorderscharacterizedbyalack
ofmelaninproductionintheskin,hair,andeyes,leadingtolightpigmentation.’
Zelly.
D.Suppose‘Dummy’means‘Araregeneticdisorderthatcausesprogressive
destructionofnervecellsinthebrainandspinalcord,leadingtosevereneurologicalsymptoms.’ Dummy.

### Output Basedontheprovideddefinitions:

A.Hat(enzymeactivitymeasurement)canbeusedtoidentifycarriersofZelly
(lackofmelaninproductiondisorders).
Explanation: Enzymeactivitymeasurementsareoftenusedinmedicaldiagnosticstoidentifyvariousconditions,includinggeneticdisorders. Inthiscase,the
lackofmelaninproduction,asseeninZellydisorders,canbeidentifiedusing
enzymeactivitytests. ✗
Table11: Performancecomparisonofthegemini-1.0-promodelwithandwithoutthesysteminstruction.
Dataset Humanities SocialSciences STEM Other Average

### Gemini-1.0-pro

QuestionOnly(5-shot) 0.687 0.744 0.539 0.658 0.645

### AnswerOnly(5-shot) 0.619 0.670 0.504 0.591 0.586

QuestionandAnswer(5-shot) 0.582 0.622 0.472 0.544 0.546

### Gemini-1.0-prowithSystemInstruction

QuestionOnly 0.688 0.735 0.535 0.650 0.652

### AnswerOnly 0.619 0.661 0.502 0.576 0.590

QuestionandAnswer 0.570 0.612 0.460 0.537 0.545

<!-- Page 15 -->

Table12: ExampleofahardversionofMMLU-SR.
Input Suppose ‘Protein’ means ‘the name given to any laboratory technique that
measures enzyme activity within a sample.’ Protein can be used to identify
carriersof:
A.Suppose‘Oculocutaneousalbini’means‘Aninheriteddisorderthataffects
thelungs,digestivesystem,andotherorgans,characterizedbytheproduction
ofthick,stickymucus.’ Oculocutaneousalbini.
B.Suppose‘Tay-Sachsdiseas’means‘Ageneticconditioncausingintellectual
disability,behavioralchallenges,andcertainphysicalcharacteristics,resulting
fromamutationintheFMR1gene.’ Tay-Sachsdiseas.
C.Suppose‘Cysticfibrosi’means‘Agroupofinheriteddisorderscharacterized
by a lack of melanin production in the skin, hair, and eyes, leading to light
pigmentation.’ Cysticfibrosi.
D. Suppose ‘Fragile X syndrom’ means ‘A rare genetic disorder that causes
progressivedestructionofnervecellsinthebrainandspinalcord,leadingto
severeneurologicalsymptoms.’ FragileXsyndrom.
Output The given problem seems to involve identifying which condition might be
detectedthroughalaboratorytechniquemeasuringenzymeactivity. Fromthe
provideddefinitions,noneoftheconditionsdirectlyindicateanenzyme-related
pathologyexceptforapossiblemisalignmentinthedefinitionsandnames:
A: Oculocutaneous albini is defined incorrectly and does not relate to the
productionofenzymes.
B:Tay-Sachsdiseaseisageneticdisordercharacterizedbythedestructionof
nervecellsinthebrainduetoadeficiencyofaspecificenzyme(Hexosaminidase
A). This is actually a plausible answer if we correct the name to Tay-Sachs
disease,whichfitsthedescriptionofadiseaseinvolvingenzymeactivity.
C:CysticfibrosisandD:FragileXsyndromearemisdefinedanddonotrelate
to conditions involving measurable enzyme activity relevant to their actual
conditions.
Thus,themostlikelyanswer,B.Tay-Sachsdisease(withthecorrecteddefinition
andname). ✗

<!-- Page 16 -->

Table13: Completeperformanceofgpt-3.5-turbo,gpt-4o-mini,gpt-4o,gemini-1.0-pro,gemini-1.5-pro,
llama3-8b,andllama3-70b.
Dataset Humanities SocialSciences STEM Other Average

### GPT-3.5-turbo


### MMLU(5-shot) 0.723 0.770 0.554 0.714 0.677

QuestionOnly(5-shot) 0.661 0.702 0.506 0.641 0.616

### AnswerOnly(5-shot) 0.540 0.595 0.441 0.538 0.520

QuestionandAnswer(5-shot) 0.469 0.523 0.396 0.476 0.459

### GPT-4o-mini


### MMLU(5-shot) 0.793 0.858 0.689 0.782 0.771

QuestionOnly(5-shot) 0.744 0.792 0.621 0.724 0.710

### AnswerOnly(5-shot) 0.659 0.738 0.602 0.651 0.655

QuestionandAnswer(5-shot) 0.588 0.666 0.531 0.585 0.585

### GPT-4o


### MMLU(5-shot) 0.880 0.906 0.771 0.854 0.845

QuestionOnly(5-shot) 0.838 0.856 0.702 0.811 0.792

### AnswerOnly(5-shot) 0.764 0.824 0.705 0.760 0.757

QuestionandAnswer(5-shot) 0.708 0.754 0.635 0.712 0.695

### Gemini-1.0-pro


### MMLU(5-shot) 0.728 0.758 0.596 0.703 0.686

QuestionOnly(5-shot) 0.687 0.744 0.539 0.658 0.645

### AnswerOnly(5-shot) 0.619 0.670 0.504 0.591 0.586

QuestionandAnswer(5-shot) 0.582 0.622 0.472 0.544 0.546

### Gemini-1.5-pro


### MMLU(5-shot) 0.849 0.881 0.802 0.815 0.832

QuestionOnly(5-shot) 0.795 0.836 0.700 0.754 0.764

### AnswerOnly(5-shot) 0.741 0.816 0.747 0.739 0.758

QuestionandAnswer(5-shot) 0.690 0.752 0.670 0.681 0.694

### Llama3-8B


### MMLU(5-shot) 0.593 0.757 0.557 0.729 0.651

QuestionOnly(5-shot) 0.546 0.685 0.507 0.668 0.595

### AnswerOnly(5-shot) 0.455 0.599 0.460 0.557 0.510

QuestionandAnswer(5-shot) 0.421 0.538 0.424 0.499 0.465

### Llama3-70B


### MMLU(5-shot) 0.681 0.868 0.697 0.814 0.765

QuestionOnly(5-shot) 0.635 0.812 0.631 0.770 0.712

### AnswerOnly(5-shot) 0.539 0.683 0.565 0.622 0.602

QuestionandAnswer(5-shot) 0.523 0.653 0.536 0.591 0.576

<!-- Page 17 -->

Table14: CompleterelativepercentagedropofaccuracyinMMLU-SRcomparedtoMMLU.
Dataset Humanities SocialSciences STEM Other Average

### GPT-3.5-turbo


### QuestionOnly(5-shot) 8.58% 8.83% 8.67% 10.22% 9.08%


### AnswerOnly(5-shot) 25.31% 22.73% 20.40% 24.65% 23.27%

QuestionandAnswer(5-shot) 35.12% 32.08% 28.52% 33.30% 32.26%

### GPT-4o-mini


### QuestionOnly(5-shot) 6.18% 7.69% 9.87% 7.42% 7.91%


### AnswerOnly(5-shot) 16.90% 13.99% 12.63% 16.75% 15.05%

QuestionandAnswer(5-shot) 25.85% 22.38% 22.93% 25.19% 24.12%

### GPT-4o


### QuestionOnly(5-shot) 4.77% 5.52% 8.95% 5.03% 6.27%


### AnswerOnly(5-shot) 13.18% 9.05% 8.56% 11.01% 10.41%

QuestionandAnswer(5-shot) 19.55% 16.78% 17.64% 16.63% 17.75%

### Gemini-1.0-pro


### QuestionOnly(5-shot) 5.63% 1.85% 9.56% 6.40% 5.86%


### AnswerOnly(5-shot) 14.96% 11.61% 15.44% 15.91% 14.48%

QuestionandAnswer(5-shot) 20.05% 17.94% 20.81% 22.60% 20.85%

### Gemini-1.5-pro

QuestionOnly(5-shot) 6.36% 5.11% 12.72% 7.48% 8.17%

### AnswerOnly(5-shot) 12.72% 7.38% 6.86% 9.33% 8.89%

QuestionandAnswer(5-shot) 18.73% 14.64% 16.46% 16.44% 16.59%

### Llama3-8B


### QuestionOnly(5-shot) 7.92% 9.51% 8.98% 8.36% 8.69%


### AnswerOnly(5-shot) 23.27% 20.87% 17.41% 23.56% 21.28%

QuestionandAnswer(5-shot) 28.16% 28.93% 23.88% 31.56% 28.63%

### Llama3-70B


### QuestionOnly(5-shot) 6.75% 6.45% 9.47% 5.41% 6.93%


### AnswerOnly(5-shot) 20.85% 21.31% 18.94% 23.59% 21.31%

QuestionandAnswer(5-shot) 23.20% 24.77% 23.10% 27.40% 24.71%
suoenallecsim ygolohcysp scisyhp noitirtun ygoloriv ygoloib scitilop namuh wal scimonoce htam ycilop
ngierof
su
tnemeganam ymotana sciteneg
lacidem
enicidem gnitnuocca seicallaf
lacigol
snoigiler lacinilc gninrael
enihcam
gnireenigne
lacirtcele
yrtsimehc larom scitsitats enicidem yhposolihp gnitekram yhpargoeg yrotsih scirtimonoce ecneics
retupmoc
ecnedurpsiruj ytiruces ymonortsa ygoloicos stcaf
labolg
scihte
ssenisub
snoitaler
cilbup
ytiruces
retupmoc
scigol
lamrof
3000
2500
2000
1500
1000
500
0
Subjects
smreT
fo
rebmuN
Modified vs Total Terms by Subject
Modified Terms

### Total Terms

Figure5: Comparisonoftotalgeneratedterms(red)andhuman-modifiedterms(blue)across41subjectglossaries

## Tables

**Table (Page 2):**

| A. Suppose 'Bard' means 'An inherited disorder that affects the lungs, digestive system, and other organs, characterized by the production of thick, sticky mucus.' Bard. B. Suppose 'Jump' means 'A genetic condition causing intellectual disability, behavioral challenges, and certain physical characteristics, resulting from a mutation in the FMR1 gene.' Jump. C. Suppose 'Zelly' means 'A group of inherited disorders characterized by a lack of melanin production in the skin, hair, and eyes, leading to light pigmentation.' Zelly. D. Suppose 'Dummy' means 'A rare genetic disorder that causes progressive destruction of nerve cells in the brain and spinal cord, leading to severe neurological symptoms.' Dummy. |
|---|
|  |


**Table (Page 3):**

| Suppose ' | Hat | ' means " | the name given to any laboratory technique that measures |  |  |  |
|---|---|---|---|---|---|---|
| enzyme activity within a sample. |  |  |  | " | Hat | can be used to identify carriers of: |


**Table (Page 4):**

| Suppose ' | Hat | ' means " |  | the name given to any laboratory technique that measures enzyme activity within |
|---|---|---|---|---|
| a sample." | Hat |  | can be used to identify carriers of: |  |


**Table (Page 17):**

|  |  |  | Total Terms |
|---|---|---|---|
|  |  |  |  |
