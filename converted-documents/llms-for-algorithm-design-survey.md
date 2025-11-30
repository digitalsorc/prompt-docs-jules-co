---
title: "LLMs for Algorithm Design Survey"
original_file: "./LLMs_for_Algorithm_Design_Survey.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["prompt-engineering", "llm", "rag", "chain-of-thought", "react"]
keywords: ["llms", "llm", "design", "algorithm", "arxivpreprintarxiv", "optimization", "search", "llmad", "based", "llmap"]
summary: "<!-- Page 1 -->

A Systematic Survey on Large Language Models for Algorithm Design

### FEI LIU, City University of Hong Kong, China

YIMING YAO, City University of Hong Kong, China

### PING GUO, City University of Hong Kong, China

ZHIYUAN YANG, City University of Hong Kong, China and Huawei Noah’s Ark Lab, China

### XI LIN, City University of Hong Kong, China

ZHE ZHAO, City University of Hong Kong, China and University of Science and Technology of China,

### China

XIALIANG TONG, Huawei No"
related_documents: []
---

# LLMs for Algorithm Design Survey

<!-- Page 1 -->

A Systematic Survey on Large Language Models for Algorithm Design

### FEI LIU, City University of Hong Kong, China

YIMING YAO, City University of Hong Kong, China

### PING GUO, City University of Hong Kong, China

ZHIYUAN YANG, City University of Hong Kong, China and Huawei Noah’s Ark Lab, China

### XI LIN, City University of Hong Kong, China

ZHE ZHAO, City University of Hong Kong, China and University of Science and Technology of China,

### China

XIALIANG TONG, Huawei Noah’s Ark Lab, China

### MINGXUAN YUAN, Huawei Noah’s Ark Lab, China


### ZHICHAO LU, City University of Hong Kong, China

ZHENKUN WANG, Southern University of Science and Technology, China

### QINGFU ZHANG∗, City University of Hong Kong, China

AlgorithmDesign(AD)iscrucialforeffectiveproblem-solvingacrossvariousdomains.TheadventofLargeLanguage
Models(LLMs)hasnotablyenhancedtheautomationandinnovationwithinthisfield,offeringnewperspectivesand
promisingsolutions.Overthepastthreeyears,theintegrationofLLMsintoAD(LLM4AD)hasseensubstantial
progress,withapplicationsspanningoptimization,machinelearning,mathematicalreasoning,andscientificdiscovery.
Giventherapidadvancementsandexpandingscopeofthisfield,asystematicreviewisbothtimelyandnecessary.
ThispaperprovidesasystematicreviewofLLM4AD.First,weofferanoverviewandsummaryofexistingstudies.
Then,weintroduceataxonomyandreviewtheliteratureacrossfourdimensions:therolesofLLMs,searchmethods,
promptmethods,andapplicationdomainswithadiscussionofpotentialandachievementsofLLMsinAD.Finally,
weidentifycurrentchallengesandhighlightseveralpromisingdirectionsforfutureresearch.
AdditionalKeyWordsandPhrases:Largelanguagemodel,Automatedalgorithmdesign,Optimization,Heuristic,
Hyperheuristic,Evolutionaryalgorithm.
1 Introduction
Algorithms play a crucial role in addressing various problems across various domains such as industry,
economics, healthcare, and technology [26, 75]. Traditionally, designing algorithm has been a labor-intensive
processthatdemandsdeepexpertise.Recently,therehasbeenasurgeininteresttowardsemployinglearning
∗thecorrespondingauthor
Authors’ContactInformation:FeiLiu,fliu36-c@my.cityu.edu.hk,CityUniversityofHongKong,HongKong,China;Yiming
Yao,yimingyao3-c@my.cityu.edu.hk,CityUniversityofHongKong,HongKong,China;PingGuo,pingguo5-c@my.cityu.edu.
hk,CityUniversityofHongKong,HongKong,China;ZhiyuanYang,zhiyuan.yang@my.cityu.edu.hk,CityUniversityofHong
Kong,HongKong,ChinaandHuaweiNoah’sArkLab,HongKong,China;XiLin,xi.lin@my.cityu.edu.hk,CityUniversityof
HongKong,HongKong,China;ZheZhao,zzhao26-c@my.cityu.edu.hk,CityUniversityofHongKong,HongKong,Chinaand
UniversityofScienceandTechnologyofChina,Hefei,China;XialiangTong,tongxialiang@huawei.com,HuaweiNoah’sArk
Lab,Shenzhen,China;MingxuanYuan,yuan.mingxuan@huawei.com,HuaweiNoah’sArkLab,HongKong,China;Zhichao
Lu,luzhichaocn@gmail.com,CityUniversityofHongKong,HongKong,China;ZhenkunWang,wangzk3@sustech.edu.cn,
SouthernUniversityofScienceandTechnology,Shenzhen,China;QingfuZhang,qingfu.zhang@cityu.edu.hk,CityUniversity
ofHongKong,HongKong,China.
Manuscriptunderreview 1
4202
voN
1
]GL.sc[
3v61741.0142:viXra

<!-- Page 2 -->

and computational intelligence methods techniques to enhance and automate the algorithm development
process [10, 142].
In the realm of artificial intelligence, Large Language Models (LLMs) have marked a significant advancement. Characterized by their vast scale, extensive training, and superior performance, LLMs have
made notable impacts in the fields such as mathematical reasoning [4], code generation [72], and scientific
discovery [152].
Over the past three years, the application of Large Language Models for Algorithm Design (LLM4AD)
has merged as a promising research area with the potential to fundamentally transform the ways in which
algorithmsaredesigned,optimizedandimplemented.TheremarkablecapabilityandflexibilityofLLMshave
demonstrated potential in enhancing the algorithm design process, including performance prediction [56],
heuristic generation [88], code optimization [59], and even the invention of new algorithmic ideas [46]
specifically tailored to target tasks. This approach not only reduces the human effort required in the design
phase but also enhances the creativity and efficiency of the produced solutions [88, 128].
While LLM4AD is gaining traction, there is a notable absence of a systematic review in this emerging
field. The existing literature primarily focuses on the applications of LLMs within specific algorithmic
contexts. For instance, several studies have been conducted to survey the use of LLMs for optimization
topics [58, 64, 163], while others review general LLM applications [53] or their use in particular domains
such as electronic design automation [189], planning [118], recommendation systems [162], and agents [154].
This paper aims to address this gap by providing a systematic review with a multi-dimensional taxonomy
of the current state of LLMs in algorithm design. We will also explore various applications, discuss key
challenges, and propose directions for future research. By synthesizing these insights, this paper contributes
to a deeper understanding of the potential of LLMs to enhance and automate algorithm design and lays
the groundwork for further innovations in this exciting field. We expect this paper to be a helpful resource
for both newcomers to the field and experienced experts seeking a consolidated and systematic update on
current developments. The contributions of this paper are outlined as follows:
∙ SystematicReviewofLLM4AD: We present the first systematic review of the developments in using
LLMs for algorithm design, covering a significant corpus of 180+ highly related research papers
published in the last three years.
∙ Development of a Multi-dimensional Taxonomy: We introduce a multi-dimensional taxonomy that
categorizes the works and functionalities of LLM4AD into four distinct dimensions: 1) Roles of LLMs
in algorithm design, which delineates how these models contribute to or enhance algorithm design; 2)
Searchmethods,whichexploresthevariousapproachesusedbyLLMstonavigateandoptimizesearch
spaces in algorithm design; 3) Prompt methods, which examines how diverse prompting strategies are
used;and4)Applicationdomains,whichidentifiesthekeyfieldsandindustrieswhereLLMsarebeing
applied to solve complex algorithmic challenges. This taxonomy not only clarifies the landscape but
also aids in identifying gaps and opportunities for future research.
∙ Discussion on Challenges and Future Directions: We go beyond mere summarization of existing
literaturetocriticallyanalyzethelimitationspresentincurrentresearchonLLMsforalgorithmdesign.
Furthermore, we highlight potential future research directions, including developing domain-specific
LLMs, exploring multi-modal LLMs, facilitating human-LLM interaction, using LLMs for algorithm
2

<!-- Page 3 -->

assessment and understanding LLM behavior, advancing fully automated algorithm design, and
benchmarking for systematic evaluation of LLMs in algorithm design. This discussion is intended to
spur novel approaches and foster further advancements in the field.
2 Methodology and Taxonomy
2.1 Scope of Survey
Thispaperaimstoconductasystematicsurveyandclassificationofexistingresearchworksintheemerging
fieldofLargeLanguageModelforAlgorithmDesign(LLM4AD).Wedonotintendtocoveralltheliterature
on both LLMs and algorithms. We delineate the scope of our survey as follows:
∙ The term Large Language Models refers to language models of sufficient scale. These models typically
utilize a transformer architecture and operate in an autoregressive manner [188]. Studies employing
smaller models for algorithm design, such as conventional model-based and machine learning-assisted
algorithms [10], are excluded. Research utilizing other large models that lack language processing
capabilities, such as purely vision-based models, are not considered. However, multi-modal LLMs that
include language processing are within our scope.
∙ The term Algorithm in this context refers to a set of mathematical instructions or rules designed to
solve a problem, particularly when executed by a computer [26]. This broad definition encompasses
traditionalmathematicalalgorithms[4],mostheuristicapproaches[108],andcertainagentsorpolicies
that can be interpreted as algorithms [165].
We introduce the detailed pipeline for paper collection and scanning, which consists of four stages:
∙ StageIDataExtractionandCollection: We collect the related papers through Google Scholar, Web of
Science, and Scopus. The logic of our search is the title must include any combinations of at least one
of the following two groups of words “LLM”, “LLMs”, “Large Language Model”, “Large Language
Models” and “Algorithm”, “Heuristic”, “Search”, “Optimization”, “Optimizer”, “Design”, “Function”
(e.g., LLM and optimization, LLMs and algorithm). After removing duplicated papers, we ended up
with 850 papers as of July 1, 2024.
∙ Stage II Abstract Scanning: We check the title and abstract of each paper to efficiently exclude
irrelevant papers. The criteria used for exclusion include these papers that are not in English, not for
algorithm design and not using large language models. After scanning, 260 papers are remaining.
∙ Stage III Full Scanning: We thoroughly review each manuscript to exclude papers lacking relevant
content. After scanning, there are 160 papers left.
∙ Stage IV Supplementation: We append some related works manually according to our past knowledge
in this field to avoid missing any important contributions. After integrating the additional papers, we
got 180+ papers in the end.
WewillfirstpresentanoverviewoftheLLM4ADpaperlistandthenpresentataxonomytosystematically
review the progress. In addition to the organized list of papers, we also incorporate some important
publications released after July 1, 2024.
3

<!-- Page 4 -->

Stage I: Data Extraction and Collection

### Date: 2020.1.1～2024 7.1

Key Words: Title = (LLM OR Large Language Model) AND (Algorithm OR Heuristic OR Search OR
Optimization OR Optimizer OR Design OR Function)
Database: Google scholar, Web of Science, Scopus
Results (remove duplication): 850 papers
Stage II: Abstract Scanning

### Content: Title and Abstract

Exclusion Criteria: not English, not algorithm design, not using large language model
Remaining Results: 260 papers
Stage III: Full Scanning

### Content: Full paper

Exclusion Criteria: Research relevant to the topic
Remaining Results: 160 papers

### Stage IV: Supplementation

Additional pertinent papers gathered from experience

### Final Results: 180 papers

Fig.1. Fourstagesforpapercollection.
2.2 Overview
Fig. 2a illustrates the trend in the number of papers published over time, with the timeline expressed in
months. The graph shows a marked rise in research activity related to LLM4AD, particularly noting that
most of the studies have been conducted in the last year. This suggests that LLM4AD is an emerging field,
and we expect a significant increase in research output in the near future as scholars from diverse fields
become aware of its considerable potential.
Fig. 2c and Fig. 2b display the leading institutions and their respective countries contributing to
publications on LLM4AD. The United States leads, closely followed by China, with these two countries
alone accounting for 50% of the publications. The next eight countries, including Singapore, Canada, and
Japan, collectively contribute one-third of the total publications. Prominent institutions involved in this
research include esteemed universities such as Tsinghua University, Nanyang Technological University, and
theUniversityofToronto,alongsidemajorcorporationslikeHuawei,Microsoft,andGoogle.Thisdistribution
underscores the widespread interest in the research topics and their substantial relevance to practical
applications in the real world.
InFig.3,thewordcloudisgeneratedfromthetitlesandabstractsofallreviewedpapers,witheachword
appearing at least five times. It showcases the top 80 keywords, organized into four color-coded clusters
on “language”, “GPT”, “search and optimization”, and “scientific discovery”. Several keywords such as
“evolution”, “strategy”, “optimizer”, and “agent” are also highlighted.
2.3 Taxonomy
ThispaperpresentsataxonomyorganizedintofourdimensionsasshowninFig.4:1)LLMRoles,2)Search
Methods, 3) Prompt Techniques, and 4) Applications.
4

<!-- Page 5 -->

  
  
  
  
  
  
 
 
                                                                                                                                               

##  0 R Q W K V  6 L Q F H       


##  V U H S D 3  I R  U H E P X 1


##  ' D W D  3 R L Q W V


##  3 R O \ Q R P L D O  ) L W


##  0 R Q W K O \  & R X Q W V

(a)Numberofpublications

##  2 W K H U V


##  $ X V , W W U D D O O \ L

 6

##  D


##  Z L W ] H U O D Q G


##  8 .  7 V L Q J K X D  8 Q L Y H U V L W \  

 * H U P D Q \  1 D Q \ D Q J  7 H F K Q R O R J L F D O  8 Q L Y H U V L W \  

##  8 Q L Y H U V L W \  R I  7 R U R Q W R  

                               - D S D Q  8 Q L Y H U V  3  L W  H  \  N   R  L Q  I   J  :   8  0  D  Q  V  +  L  K  L  F  Y  L  X  U  Q  H  R  D  U  J  V  V  Z  W  R  L  R  W  H  I  \  Q  W  L        
      6 L Q J D S R U H  6 R X W K H U Q  8 Q L Y H U V L W \  R I  6 F L H Q F  *  H  R   D  R  Q  J  G  O H   7   '  H F  H  K  H  Q  S  R  0  O R  L Q  J  G  \    

##       8 Q L Y H U V L W \  R I  % U L W L V K  & R O X P E L D  


##  & L W \  8 Q L Y H U V L W \  R I  + R Q J  . R Q J  


##  7 K H  & K L Q H V H  8 Q L Y H U V L W \  R I  + R Q J  . R Q J  

            & D Q D G D  6  &  K  K  D  L  Q  Q  J  H  K  V  D  H  L   $   - L  F  D  D  R  G    H  7  P  R Q  \  J   R   8  I   Q  6  L  F  Y  L  H  H  U  Q  V  F  L  H  W \  V    

##  8 6 $  & D U Q H J L H  0 H O O R Q  8 Q L Y H U V L W \  


##  0 L F U R V R I W  5 H V H D U F K  


##  7 K H  + R Q J  . R Q J  3 R O \ W H F K Q L F  8 Q L Y H U V L W \  

       6 W D Q I  9  R  H  U  F  G  W    R  8  U   Q  ,  L  Q  Y  V  H  W  U  L W  V  X  L W  W  \  H    
 + R Q J  . R Q J  8 Q L Y H U V L W \  R I  6 F L H Q F H  D Q G  7 H F K Q R O R J \  
               

##  & K L Q D  1 X P E H U  R I  3 X E O L F D W L R Q V

(b)Countrydistribution (c)Institutions
Fig.2. OverviewonLLM4ADpapers.
∙ LLMRoles: This dimension examines how LLMs are integrated into algorithm development, dividing
the workds into four categories: LLMs as Optimizers (LLMaO), LLMs as Predictors (LLMaP), LLMs
as Extractors (LLMaE), and LLMs as Designers (LLMaD).
∙ SearchMethods:Thiscategoryinvolvesthesearchmethodsusedincludingthebasicsamplingmethods
and more complex approaches like evolutionary algorithms, and uncertainty-guided methods.
∙ PromptMethods: The effectiveness of pre-trained LLMs is heavily influenced by prompt engineering.
We investigate the typical prompt strategies used in LLM4AD including zero-shot, few-shot, chain-ofthought, self-consistency, and reflection prompts.
∙ Applications: The broad application of LLM4AD covers diverse fields. We identify the main domains
including optimization, machine learning, industry, and scientific discovery.
3 LLM Roles
According to the roles of LLM in algorithm design, existing works can be categorized into four classes:
LLMs as Optimizers (LLMaO), LLMs as Predictors (LLMaP), LLMs as Extractors (LLMaE), and LLMs as
5

<!-- Page 6 -->

Fig.3. Thewordcloudisgeneratedfromthetitlesandabstractsofallreviewedpapers,witheachwordappearingatleast
fivetimes.Itfeaturesthetop80keywords,organizedintofourcolor-codedclusters.
LLM Algorithm Application

## Llm4Ad


### LLM Roles Search Methods Prompt Methods Applications


### LLM as Optimizers Random Search Zero-shot Optimization

LLM as Predictors Single-point-based Few-shot Machine Learning

### Search

LLM as Extractors Chain-of-thought Industry

### Population-based

LLM as Designers Search Self-consistency Science Discovery
Uncertaintyguided Search Reflection
Fig.4. Afour-dimensionaltaxonomy.
Designers(LLMaD).Thissectionpresentstheprogressandexploretheadvantagesandlimitationsassociated
with each category.
3.1 LLMs as Optimizers (LLMaO)
InLLMaO,LLMsareutilizedasablack-boxoptimizerwithinanalgorithmframeworktogenerateandrefine
solutions (Fig. 5). The integration of LLMs into optimization tasks leverages their ability to understand
and generate complex patterns and solutions and good flexibility [86, 92, 167]. These capabilities are often
6

<!-- Page 7 -->

challengingfortraditionaloptimizersandmodelstomatch.However,theblack-boxnatureofLLMstypically
results in a lack of interpretability and presents difficulties in large-scale generation [86].
Problem Algorithm Solution
Solution Solution

## Llm

Fig.5. LargeLanguageModelsasOptimizers(LLMaO).LLMsserveasoptimizerswithinthealgorithmtogeneratenew
solutions.ThistypicallyinvolvesusingtheLLMinaniterativesearchprocesstoenhancesolutionquality.Here,thealgorithm
anditsparametersareusuallycraftedbyhumans.
One of the initial efforts to utilize LLMs as optimizers in algorithm design is by Yang et al. [167]. They
leverage the in-context learning capabilities of LLMs to generate novel solutions for specific problems
based on previously evaluated solutions. This method is applied iteratively to refine solutions further. Yang
et al. [167] have successfully demonstrated this technique across various domains, including continuous and
combinatorial optimization, as well as machine learning tasks.
From an evolutionary algorithm (EA) perspective, using LLMs to generate solutions from existing data
can be seen as analogous to search operators in EA. For instance, Liu et al. [86] introduce the use of
LLMs as evolutionary operators to tackle multi-objective problems. This method involves breaking down a
multi-objective problem into simpler single-objective tasks, with LLMs acting as black-box search operators
for each sub-problem to suggest new solutions. In a related study, Liu et al. [92] explore the integration of
LLMs within EAs, not just for generating solutions but also for guiding selection, crossover, and mutation
processes.Meanwhile,Brahmacharyetal.[14]proposeanewpopulation-basedevolutionaryframeworkthat
includes both exploration and exploitation pools, with solutions being exchanged during the optimization
process and LLMs generating solutions for both pools.
Differing from direct solution generation, Lange et al. [77] investigate the use of LLMs in designing
evolution strategies, introducing a new prompting strategy to enhance the mean statistic in their EvoLLM
method, which shows superior performance over baseline algorithms in synthetic black-box optimization
functions and neuroevolution tasks. They also demonstrate that fine-tuning LLMs with data from teacher
algorithms can further improve the performance of EvoLLM. Moreover, Custode et al. [28] present a
preliminary study that uses LLMs to automate hyperparameter selection by analyzing optimization logs
and providing real-time recommendations.
Beyond traditional optimization tasks, LLMaO has been widely adopted in prompt engineering for LLMs,
a process often referred to as “automatic prompt optimization” [192]. These methods primarily involve
iterative refinement of prompts by LLMs to improve their effectiveness for specific models (typically LLMs).
Techniques include resampling-based strategies, where LLMs generate variations of original prompts while
maintaining semantic similarity [156], and reflection-based strategies, where LLMs optimize by analyzing
and learning from previous prompt iterations or errors [50], have been explored. Ma et al. [99] note that
LLM optimizers often struggle to accurately identify the root causes of errors during the reflection process,
7

<!-- Page 8 -->

influenced by their pre-existing knowledge rather than an objective analysis of mistakes. To address these
issues, they propose a new approach termed “automatic behavior optimization”, aimed at directly and more
effectively controlling the behavior of target models.
3.2 LLMs as Predictors (LLMaP)
LLMaP employs LLMs as surrogate models (Fig. 6) to predict the outcomes or responses of solutions,
functioning either in a classification or regression context [56]. Compared to other model-based predictors,
such as the Gaussian process and conventional neural networks, 1) LLMs are capable of processing and
generating human-like responses. This capability allows them to understand and interpret complex patterns
in data, making them suitable for tasks where traditional modeling techniques might struggle due to the
intricacies in the data and complicated representations [36, 161]. 2) Pre-trained LLMs can significantly
reduce the computational load and time required compared to training high-fidelity models [56, 70].
Problem Algorithm Solution
Fitness /
Solution
Category

## Llm

Fig.6. LargeLanguageModelsasPredictors(LLMaP).LLMsareutilizediterativelyinalgorithmstopredictasolution’s
outcomesorresponses,typicallyfunctioninginclassificationorregressiontasks.
The majority of LLMaP works use LLMs as pre-trained models to predict solution scores. For instance,
LLMs have been used as performance predictors for deep neural network architectures by Jawahar et al.
[70]. It offers a cost-effective alternative for performance estimation in neural architecture search. Zhang
et al. [185] introduce LINVIT, an algorithm that incorporates guidance from LLMs as a regularization
factor in value-based RL to improve sample efficiency. Science discovery is another domain that LLMaP
has commonly investigated. For example, Li et al. [82] introduce CodonBERT for sequence optimization of
mRNA-basedvaccinesandtherapeutics.CodonBERTusescodonsasinputsandistrainedonover10million
mRNA sequences from various organisms. Soares et al. [138] demonstrate the use of LLMs in predicting
the performance of battery electrolytes. Other applications include employing LLMs to determine the fame
score of celebrities to predict the box office performance of projects in the motion pictures industry [6]
and adopting LLMs to score the video question answering by using detailed video captions as content
proxies [182].
For classification, Hao et al. [56] introduce LAEA, which employs LLMs as surrogate models within
evolutionaryalgorithmsforbothregressionandclassification,eliminatingtheneedforcostlymodeltraining.
In another study, Chen et al. [23] develope a label-free node classification method that leverages LLMs
to annotate nodes. These annotations are subsequently used to train graph neural networks, resulting in
enhanced performance. Moving beyond binary classification, Bhambri et al. [12] utilize LLMs to predict
discrete actions for constructing reward shaping functions in Reinforcement Learning (RL). Their method
demonstrate effectiveness within the BabyAI environment, showcasing the versatility of LLMs in various
8

<!-- Page 9 -->

settings. Wang et al. [155] explore the use of LLMs in federated search, applying them in a zero-shot
setting to effectively select resources. This approach highlights the potential of LLMs in improving resource
selection without prior explicit training on specific tasks. Lastly, Mehrdad et al. [106] focus on automating
the relevance judgment of query-item pairs in product searches. By finetuning LLMs, they have achieved
significant improvements, underscoring the adaptability and effectiveness of LLMs in complex search tasks.
Despite these advantages, using LLMs as predictors for algorithm design also suffers from a lack of
interpretability,andtheresultscanbeinfluencedbythequalityofpromptengineering[23].Moreover,when
the target landscape is easily understood, conventional machine learning techniques and surrogate models
are often preferred. In such scenarios, LLMs can enhance the utilization of existing modeling methods, for
example, by aiding in the selection of the most effective model [127].
3.3 LLMs as Extractors (LLMaE)
LLMaE employs LLMs to mine and extract embedded features or specific knowledge from target problems
and/or algorithms, which are then utilized in the enhancement of algorithm-based problem solving (Fig 7).
For example, Kristiadi et al. [76] use LLMs as pre-trained feature extractors and the embeddings are used
to enhance standard Bayesian optimization surrogate models in the molecular space.
Problem Solution
Algorithm
Embedding

## Llm

Fig.7. LargeLanguageModelsasExtractors(LLMaE).LLMsareemployedtoextractfeaturesorspecificknowledgefrom
targetproblemand/oralgorithmstoenhanceproblem-solving.
Beyondembedding-basedfeatureextraction,LLMsexcelintextcomprehensionandknowledgeextraction,
allowing them to discern subtle patterns and relationships within the data that might not be evident
through conventional feature extraction methods. For example, Wu et al. [164] utilize LLMs to extract
high-dimensionalalgorithmrepresentationsbycomprehendingcodetext.Theserepresentationsarecombined
with problem representations to determine the most suitable algorithm for a specific problem. Du et al.
[32] propose a mixture-of-experts framework augmented with LLMs to optimize various wireless user
tasks. The LLM is used to analyze user objectives and constraints, thus selecting specialized experts, and
weighingdecisionsfromtheexperts,reducingtheneedfortrainingnewmodelsforeachuniqueoptimization
problem. Additionally, Becker et al. [9] discuss the use of LLMs in the automotive and supplier industries,
specifically focusing on retrieval-augmented generation systems to improve information retrieval from
technical documentation. Memduhoğlu et al. [107] use LLM to enhance the classification of urban building
functions by interpreting OpenStreetMap tags and integrating them with physical and spatial metrics.
Traditional techniques, which have previously struggled with semantic ambiguities, are outperformed by
LLMs due to their superior ability to capture broader language contexts.
9

<!-- Page 10 -->

The multi-modal capabilities of LLMs also distinguish them from traditional methods. Park et al. [120]
demonstrate that incorporating lexical information extracted from LLMs into an acoustic-based speaker
diarizationsystemthroughaprobabilisticmulti-modaldecodingprocessandbeamsearchescansignificantly
improve speech-processing performance.
3.4 LLMs as Designers (LLMaD)
LLMaD directly creates algorithms or specific components (Fig. 8). This utilization of LLMs extends their
application beyond traditional boundaries, enabling them to actively participate in algorithm development
bygeneratingheuristics[88],writingcodesnippets[59],orformulatingfunctions[128]thatcanbeintegrated
intoalgorithmicsystems.Bydoingso,LLMscansignificantlyacceleratethealgorithmdesignprocess,reduce
human effort, and bring creativity and optimization to algorithm development [88], which is difficult to
achieve through traditional methods.
Problem Solution
Algorithm
Algorithm

## Llm

Fig.8. LargeLanguageModelsasDesigners(LLMaD).LLMsareusedtodirectlycreatealgorithmsorspecificcomponents,
whicharecommonlyincorporatediterativelytocontinuouslysearchforbetterdesigns.
Function design is among the early applications of LLMaD. Eureka [100] leverages the capabilities of
LLMs in code-writing, and in-context learning to evolve and optimize reward functions for RL. It can
generate reward functions without specific prompts or predefined templates, achieving better performance
than rewards designed by human experts. Similarly, Auto MC-Reward [80] utilizes LLMs to automatically
designdenserewardfunctionsforRLagentsinenvironmentswithsparserewards.Thethreekeycomponents
of Auto MC-Reward work together to iteratively refine the reward function based on feedback from the
agent’s interactions with the environment. Through this iterative process, the agent is able to learn complex
tasks more efficiently, as demonstrated in experiments in Minecraft. Moreover, FunSearch [128] adopts
LLMs for function generation in an evolutionary framework with a multi-island population management. It
demonstrates promising results on both mathematical problems and combinatorial optimization problems.
EoH[88],originatesfromAEL[87],presentsanearlyattempttoadopttheLLMasadesignerforautomated
heuristicdesign.ItusesbothheuristicideasandcodeimplementationstorepresentheuristicsandadoptsLLM
in an evolutionary framework to create, combine, and revise the heuristics. EoH is applied on well-studied
combinatorial optimization problems, where it surpasses both traditional human-designed metaheuristics
anddeep-learning-basedneuralsolvers.TheapplicationofEoHhasexpandedtoBayesianoptimization[171],
image adversary attack [49], and edge server task scheduling [172], among others. Moreover, LLaMEA [150]
develops an iterative framework to generate, mutate, and select algorithms based on performance metrics
and runtime evaluations. The automatically designed algorithms outperform state-of-the-art optimization
10

<!-- Page 11 -->

algorithms on some benchmark instances. ReEvo [176] introduces an evolutionary framework with both
short and long-term reflections, which provides a search direction to explore the heuristic space. With the
reflection,betterresultsonblack-boxcases(noproblem-specificinformationisprovidedintheprompts)have
been observed. Unlike previous studies that focus on optimizing a single performance criterion, MEoH [170]
considers multiple performance metrics, including optimality and efficiency, and seeks a set of trade-off
algorithms in a single run in a multi-objective evolutionary framework. A dominance-dissimilarity score is
designed for effectively searching the complex algorithm space.
LLM-basedagentdesignhasalsogainedmuchattention.Forexample,ADAS[63]proposesanautomated
design of agentic systems, which aims to automatically generate powerful agentic system designs by using
meta agents that program new agents. They present a novel algorithm, meta agent search, which iteratively
creates new agents from an archive of previous designs, demonstrating through experiments that these
agents can outperform state-of-the-art hand-designed agents across various domains. Further studies on
LLM-based agent systems are discussed in [139] and [94].
There has been a considerable effort on using LLMs for optimization modeling. Ahmed and Choudhury
[3] assess various LLMs for transforming linguistic descriptions into mathematical optimization problems,
introducing a fine-tuning framework, LM4OPT, to enhance the performance of smaller models. Tang et al.
[145]outlinefourkeytrainingdatasetrequirementsforoperationalresearchLLMsandproposeOR-Instruct,
a semi-automated method for generating tailored synthetic data. Additionally, Mostajabdaveh et al. [111]
present a novel multi-agent framework that translates natural language into optimization models, utilizing
relational identifier agents and a verification mechanism for improved assessment.
WeidentifytwoprimarychallengesinexistingworksonLLMaD:1)LLMsstrugglewithcomplexalgorithm
designtasks.Mostexistingstudiesfocusondevelopingspecificalgorithmiccomponents,suchaskeyheuristics
and code snippets, rather than complete algorithms [88]. 2) Algorithm design is domain-specific, and LLMs
typically possess limited knowledge about specific algorithm design tasks. Consequently, standalone LLMs
often fall short in terms of performance [183]. The effectiveness of LLMaD depends on search frameworks
that can iteratively interact with both LLMs and their environments. Details on the search methods are
provided in the next section.
4 Search Methods
Incorporating LLMs within a search framework significantly enhances LLMs’ utility in algorithm design,
making it the preferred option [88, 100, 128]. This section categorizes existing research according to the
search methods employed, presents recent advancements, and discusses some of the limitations.
4.1 Sampling
ThemoststraightforwardsearchmannerisbyrepeatedlyinstructingLLMtosamplenewdesigns[192].The
best sample is selected as the final design. However, recent studies have shown that simple sampling from
LLMs can be costly [183].
4.1.1 Beam Search. Beam search explores multiple promising paths within a search space. For example, in
the context of LLM-based prompt engineering [99, 122, 192], increasing the beam size has been shown to
significantlyimproveperformance.Beyondpromptengineering.Beamsearchisalsoemployedinavarietyof
11

<!-- Page 12 -->

other applications. For instance, Text2Motion [84] uses beam search for robotic task planning. Similarly,
SayCanPay [57] applies it to plan action sequences in robotics.
4.1.2 MCTS. Monte Carlo Tree Search (MCTS) is a tree search algorithm that uses random sampling to
build a search tree and make decisions based on the results of these samples. It is particularly effective in
problems with large and complex search spaces. For example, Dainese et al. [29] propose GIF-MCTS, a
code generation strategy using MCTS, in which nodes in the tree are programs and edges are actions. Each
action taken from a parent node produces a new complete program. The upper confidence bound for trees
is used to select which action to take. Similarly, VerMCTS [15] constructs a search tree with progressive
widening to effectively manage large action spaces defined by lines of code. In this search tree, expansion
and evaluation are guided by the verifier, serving as a computationally inexpensive upper bound on the
value function. Moreover, Wang et al. [156] regard prompt optimization as a strategic planning challenge,
utilizing a principled planning algorithm based on MCTS to effectively explore the expert-level prompt
space. The proposed PromptAgent generates precise insights and detailed instructions by analyzing model
errors and providing constructive feedback.
4.2 Single-point-based Search
Single-point-based search methods iteratively refine a solution by leveraging neighborhood structures [90] or
specific search directions [122]. While these methods can produce satisfactory results within a reasonable
number of iterations, they may struggle with maintaining diversity and robustness in their search processes.
4.2.1 Hillclimb. Hillclimbsearchiterativelysearchesforbetterresults,wherethenewoneisgeneratedbased
on the last one and the better one is survived. A basic version of Hillclimb is investigated by Zhang et al.
[183] for algorithm design, where a heuristic is iteratively refined. The reasoning over the existing status is
usually adopted to enhance each search step. For example, Li et al. [80] leverage LLMs to automatically
design dense reward functions for RL agents in environments with sparse rewards, which iteratively refines
the reward function based on feedback from the agent’s interactions with the environment. Yang et al.
[169] develop a multi-module framework with innovative feedback mechanisms, demonstrating through both
LLM-based and expert evaluations that LLMs can effectively produce scientific hypotheses that are both
novel and reflective of reality.
4.2.2 Neighborhood Search. Neighborhood search methods explore the solution space by iteratively modifying a current solution to find an improved one in a structured neighborhood. Notably, the LLM-GS
framework[90]hasintroducedascheduledneighborhoodsearchmethodthatleveragestwodistinctstrategies:
1) Programmatic Neighborhood Generation, which involves generating a neighborhood of programs by
selecting a node from the abstract syntax tree of a given program and substituting it with a subtree that is
randomly generated following the production rules and sampling strategies of a domain-specific language;
and 2) Latent Space Representation, where the neighborhood is defined in a latent space by training a
variationalautoencoderonacorpusofrandomlygeneratedDSLprograms,therebycreatingamoreabstract
and potentially more informative neighborhood structure. Additionally, Jin et al. [73] contribute to this line
of research by defining neighborhood algorithms based on a minimum cosine similarity threshold of 60%
12

<!-- Page 13 -->

between the embeddings of a query vector and code snippets, enhancing the search process by ensuring that
algorithmic variations are semantically coherent and aligned with the underlying problem structure.
4.2.3 Gradient-based Search. Gradient-based search utilizes a (pseudo) gradient direction to generate new
designs in each iteration. Unlike searches in a continuous space with a differentiable objective, calculating
the gradient in the algorithm design space poses significant challenges. Consequently, a pseudo descent
direction is often employed. Pryzant et al. [122] introduce automatic prompt optimization, which improves
prompts automatically by adjusting them based on natural language “gradients” derived from training data.
Similarly, Tang et al. [143] introduce GPO, which draws parallels with gradient-based model optimizers for
promptoptimization.Moreover,Nieetal.[115]exploretheuseofLLMsasinteractiveoptimizersforsolving
maximization problems in a text space through natural language and numerical feedback. For an accurate
gradient, Guo et al. [51] perform the gradient-based search in a mapped continuous space and propose a
collaborative optimization strategy that combines a gradient-based optimizer with an LLM for tackling
complex non-convex optimization challenges. These works employ either pseudo gradients or gradients over
mapped text space, however, a systematic study of gradients over general algorithm space is anticipated.
4.2.4 Reinforcement Learning. Reinforcement learning learns to make decisions by interacting with an
environmenttomaximizerewards.Zhugeet al.[194] andDuanet al.[35] leverageLLMsandRL techniques
to optimize code, reducing complexity and enhancing efficiency. Similarly, Liu et al. [90] present a novel
LLM-guided search framework called LLM-GS, which aims at addressing the sample inefficiency in stateof-the-art programmatic RL methods by utilizing the programming expertise of LLMs to boost search
efficiency. Additionally, LLMs have been utilized in the design of RL systems, particularly in the creation of
reward-shapingfunctions.Moreover,Bhambrietal.[12]useLLMstogenerateaguidepolicyforconstructing
reward-shaping functions to tackle the issue of sample inefficiency.
4.3 Population-based Search
Population-basedevolutionarysearchisthemaintoolinvestigatedinLLM4ADpapersduetoitseffectiveness
androbustnessincomplexsearchspace[117,163].Themajorityoftheseworksuseasimplegeneticalgorithm
with greedy population management [88]. Some of them investigate advanced population management
including multi-island [128], quality-diversity [63], and dominance-dissimilarity measurement [170].
4.3.1 Single-objective Evolutionary Search. Liu et al. [92] explore the use of LLMs as evolutionary operators
in conventional EA, guiding them in solution selection, crossover, and mutation processes. Moreover,
Brahmachary et al. [14] propose a population-based evolutionary framework comprising exploration and
exploitation pools, with LLMs facilitating solution generation for both pools and enabling communication
between them during optimization. Lange et al. [77] investigate the application of LLMs in designing
evolution strategies, introducing a prompting strategy to enhance mean statistic performance.
On algorithm design tasks involving text and code search, the complicated search space poses challenges
for diversity control and population management. The majority of works adopt a greedy way [20, 49, 59, 80,
88, 112, 150, 171]. In these works, a population of individuals is maintained and only the ones with better
fitness will survive. Romera-Paredes et al. [128] adopt a multi-island evolutionary algorithm to explore a
diverse population with a dynamically adjusted population size. Moreover, Wong et al. [160] use LLMs
13

<!-- Page 14 -->

to create digital artifacts for creative and engineering applications, utilizing a multi-factorial evolutionary
algorithm to drive an LLM. Quality diversity methods [123] have also been investigated for this purpose,
Lehman et al. [78] and Hu et al. [63] utilize the MAP-Elites algorithm with niches to generate diverse and
high-quality solutions.
4.3.2 Multi-objective Evolutionary Search. Liu et al. [86] propose MOEA/D-LMO to use LLM to solve
continuous multi-objective optimization problems. Benefiting from the decomposition-based framework, the
in-context learning of LLM is used to generate new solutions for each subproblem. For multi-objective LLM
instructiongeneration,YangandLi[168]developInstOptima,whichutilizesanLLMtosimulateinstruction
operatorsandimproveinstructionqualitytosimultaneouslyoptimizeperformance,length,andperplexityof
the instruction. Moreover, Morris et al. [110] introduce guided evolution for neural architecture design. It
adopts NSGA-II and optimizes both accuracy and model size. In order to enhance the diversity control in
multiobjective heuristic design, MEoH [170] introduce a dominance-dissimilarity score for multi-objective
heuristic design, achieving a good balance of exploration and exploitation in the heuristic search space.
4.4 Uncertainty-guided Search
Uncertainty-guidedsearchcombinesBayesianOptimalExperimentDesign(BOED)orBayesianOptimization
(BO) with Large Language Models (LLMs). It starts with a prior based on initial parameter beliefs, then
uses uncertainty-driven strategies to iteratively refine the beliefs, enhancing decision-making efficiency in
a sample-efficient way. This method has shown effectiveness in various applications. For example, Handa
et al. [54] develop OPEN, which uses LLMs to extract environmental features and translate feature queries
into conversational natural language questions, employing BOED to select the most informative queries for
learninguserpreferencesefficiently.Austinetal.[8]introducethePEBOLalgorithmwithinaBOframework
to improve multi-turn and decision-theoretic reasoning, using Beta distributions to model user preferences
probabilistically. In LLM decoding, Grosse et al. [47] propose ULTS, which treats decoding as a tree-search
problem and optimizes path selection through sequential decision-making under uncertainty.
5 Prompt Strategies
Prompt strategies are vital for effectively utilizing LLMs, particularly in algorithm design tasks that require
instructionsonreasoningandreflectiononthetargettasks.WewillbeginbyprovidinganoverviewofLLMs
and the prompt strategies employed in existing works, followed by a review to works using each strategy.
Fig. 9a depicts the percentage of domain or pre-trained LLMs used in the literature. Among them, over
80% choose to use the pre-trained model without any specific finetuning, and about 10% fine-tuned the
pre-trained model on domain datasets [27] in which 4.4% are trained from scratch. LLM4AD papers show a
strong preference for GPT models. GPT-4 and GPT-3.5 are the most commonly utilized LLMs, collectively
accountingforapproximately50%.Llama-2isthemostusedopen-sourceLLM.Oncewehavethepre-trained
LLMs, prompt engineering is significant for effectively integrating LLMs into algorithm design. LLM4AD
papers involve many prompt engineering methods (as illustrated in Fig. 9b) including Zero-Shot (ZS),
Few-Shot (FS), Chain-of-Thought (CoT), Self-Consistency (SC), and Reflection (RF) [130].
14

<!-- Page 15 -->

  
  
  
  
  
  
  
  
 

##  ) H Z  6 K R W   ) 6

 =
 

##  H U R

 &
  6

##  K D


##  K


##  L


##  R


##  Q


##  W

 
 

##  R

  =

##  I 

 6
 7

##    K R X J K W   & R

 5
 7

##  H


##    I O H F W

 6

##  L R


##  H


##  Q


##  O I

 
 
 

##  F

 5

##  R

 )

##  Q


##    V L V W H Q F \   6 & 

(a)LLMs

##  V Q R L W D F L O E X 3  I R  U H E P X 1

  
  
  
 
 
(b)Promptengineeringtechniques
Fig.9. LLMtypesandpromptengineeringmethods
5.1 Zero-Shot
Zero-Shot (ZS) prompting enables a model to comprehend and perform tasks without prior specific training
on those tasks. In algorithm design, zero-shot prompting allows direct requests to the LLM for solutions
or responses, examples including conversational replies [132], assertion design [109], RL guidance [185],
and molecule generation [173]. The model leverages its pre-trained knowledge to generate these responses.
Although this method is advantageous for swiftly producing solutions based on general knowledge, it may
not consistently deliver tailored responses to the nuanced demands of complex algorithmic challenges [183].
5.2 Few-Shot
Few-Shot(FS)promptinginvolvesprovidingthemodelwithahandfulofexamplestoillustratethetaskbefore
it attempts to solve a similar problem. This approach enhances the model’s understanding of the context
and its ability to tailor responses to specific tasks. In algorithm design, this method proves particularly
effective by presenting the model with examples of algorithms [87], solutions [167], prompts [143, 156], and
codes [101, 110]. The examples used in the prompt may be manually-designed seeds [63, 128] or derived
fromLLM-generateddesigns[28,88,98,110,143,156,160].Thesesamplesaretypicallysortedtosuggesta
preference to enhance performance [128, 167].
5.3 Chain-of-Thought
Chain-of-Thought (CoT) prompting encourages the model to articulate intermediate steps or reasoning
paths that lead to the final answer. This technique is particularly valuable in algorithm design, where
understanding the step-by-step process or engaging in instructed reasoning over existing designs helps
prevent outlier results and fosters effective algorithm development. For instance, Liu et al. [88] introduce
several prompting strategies, one of which directs the LLM to reason over existing heuristics, summarize
the general pipeline, and design a new one based on this reasoning. Custode et al. [28] prompt the LLM to
evaluate whether the current step size is sufficient for convergence and to suggest adjustments based on
15

<!-- Page 16 -->

its reasoning. In addition, multiple LLM-based agents are employed within a CoT framework by Sun et al.
[140] to enhance heuristic design for a boolean satisfiability problem solver.
5.4 Self-consistency
Self-Consistency (SC) involves generating multiple answers or solutions to the same prompt and then
synthesizing them to improve accuracy and reliability. In algorithm design, this could mean prompting
the model multiple times for different approaches to solve a problem and then comparing these solutions
to identify the most efficient or robust algorithm. This approach leverages the model’s ability to generate
diverse solutions and builds a more comprehensive understanding of possible strategies. For example, Guan
et al. [48] set the number of responses as 10 and uses the majority vote to get the predicted label. As each
responsemayprovidedifferentkeywordsorregularexpressions,ittakestheunionofthekeywordsorregular
expressions to create a candidate set. Moreover, Lehman et al. [79] sample multiple revised codes from the
same selected code and updates the population accordingly.
5.5 Reflection
Reflection(RF)inpromptengineeringinvolvesaskingthemodeltocritiqueorevaluateitsownresponsesor
solutions. After generating an algorithm/solution, the model can be prompted to reflect on the efficiency,
potentialflaws,orimprovements.Maetal.[99]investigatebothimplicitandexplicitreflectioninLLM-driven
prompt optimization, which lets LLM analyze the errors and generate a reflection or feedback regarding the
current prompt. An additional study by Ye et al. [175] incorporates short-term and long-term reflections in
heuristic design, while Zhang et al. [179] focus on self-evaluation and reasoning over results from network
detection.Furthermore,bothMaetal.[100]andNarin[112]adoptLLMforRLrewardfunctiondesignwith
a reward reflection that monitors the scalar values of all reward components and the task fitness function at
various policy checkpoints during training.
6 Applications
6.1 Optimization
In this subsection, we delve into the practical applications of LLMs in algorithm design for optimization.
We categorize the existing literature into combinatorial optimization, continuous optimization, Bayesian
optimization,promptoptimization,andoptimizationmodelingbasedonthespecificdomainsofoptimization
applications.ThenweproceedtocomparethevariousrolesplayedbyLLMs,thepromptstrategiesemployed,
and the specific problems or tasks to which they are applied. The comparative analysis is summarized in
Table 1, where we list the names of the frameworks or methods proposed by the authors. For studies that
do not explicitly name their methods, we assign appropriate designations in our article and denote them
with asterisks for easy reference (e.g., MH-LLM* for [131]).
6.1.1 CombinatorialOptimization. InthedomainofCombinatorialOptimization(CO),automatedalgorithm
heuristics design has been a significant area of interest for a long time. The Traveling Salesman Problem
(TSP) stands out as one of the most renowned CO problems, involving the quest for the shortest route to
visit all specified locations exactly once and return to the starting point. Some recent work leverages LLMs
to evolve algorithms within Evolutionary Computation (EC) framework, such as AEL [87], ReEvo [176] and
16

<!-- Page 17 -->

EoH [88]. Differently, OPRO [167] employs LLMs as optimizers with a proposed meta-prompt, in which
the solution-score pairs with task descriptions are added in each optimization step. Additionally, LMEA
[91] investigates the utilization of LLMs as evolutionary combinatorial optimizers for generating offspring
solutions, wherein a self-adaptation mechanism is introduced to balance exploration and exploitation. The
CapacitatedVehicleRoutingProblem(CVRP)extendstheTSPbyintroducingconstraintsrelatedtovehicle
capacity. To address this challenge, MLLM [68] devises a multi-modal LLM-based framework with textual
andvisualinputstoenhanceoptimizationperformance.Inadditiontoroutingproblems,othercombinatorial
optimization problems that have also been investigated include cap set [128], bin packing [88], flow job shop
scheduling [88] and social networks problems [131].
6.1.2 Continuous Optimization. In the realm of single-objective continuous optimization, LLaMEA [150]
utilizes LLMs to automate the evolution of algorithm design. It demonstrates the effectiveness in generating
new metaphor-based optimization algorithms on BBOB benchmark [55] within IOHexperimenter benchmarking tool [30], which supports evaluating the quality of the generated algorithms and also provides
feedback to the LLM during evolution. Instead of creating new algorithms, EvolLLM [77] introduces a
prompt strategy that enables LLM-based optimization to act as an Evolution Strategy (ES) and showcases
robust performance on synthetic BBOB functions and neuroevolution tasks. OPRO [167] illustrates that
LLMs can effectively capture optimization directions for linear regression problems by leveraging the past
optimization trajectory from the meta-prompt. Additionally, LEO [14] devises an explore-exploit policy
using LLMs for solution generation, the method has been tested in both benchmark functions as well as
industrialengineeringproblems.DifferentwithdirectlyemployingLLMsforgeneratingsolutions,LAEA[56]
introduces LLM-based surrogate models for both regression and classification tasks and has been validated
on 2D test functions using nine mainstream LLMs.
Multi-objective optimization problems (MOPs) seek to identify a set of optimal solutions, referred to
as Pareto optimal solution set. An initial exploration of utilizing LLMs to tackle MOPs is introduced in
MOEA/D-LMO [86]. Benefiting from the decomposition-based framework, the in-context learning process
of LLMs is easily incorporated to generate candidate solutions for each subproblem derived from the
original MOP. In the realm of large-scale MOPs, LLM-MOEA* [136] showcases the inferential capabilities
of LLMs in multi-objective sustainable infrastructure planning problem. The study highlights the LLM’s
proficiency in filtering crucial decision variables, automatically analyzing the Pareto front, and providing
customizedinferencesbasedonvaryinglevelsofexpertise.Additionally,CMOEA-LLM[158]leveragesLLMs
with evolutionary search operators to address the challenges of constrained MOPs and exhibits robust
competitiveness in DAS-CMOP test suite [39].
6.1.3 Bayesian Optimization. Bayesian optimization (BO) is a model-based optimization paradigm for
solving expensive optimization problems and has found wide applications in various real-world scenarios
[44]. It typically employs a surrogate model to approximate the expensive function and well-designed
AcquisitionFunctions(AFs)toselectpotentialsolutionsinasample-efficientmanner.Tofacilitatethedirect
generation of solutions using LLMs, HPO-LLM* [181] provides LLMs with an initial set of instructions that
outlines the specific dataset, model, and hyperparameters to propose recommended hyperparameters for
evaluation in Hyperparameter Optimization (HPO) tasks. Furthermore, LLAMBO [93] incorporates LLM
capabilities to enhance BO efficiency, in which three specific enhancements throughout the BO pipeline
17

<!-- Page 18 -->

have been systematically investigated on tasks selected from Bayesmark [148] and HPOBench [37]. Instead
of utilizing LLMs for direct solution generation, BO-LIFT* [125] utilizes predictions with uncertainties
provided by a Language-Interfaced Fine-Tuning (LIFT) framework [31] with LLMs to perform BO for
catalyst optimization using natural language. EvolCAF [171] introduces a novel paradigm integrating LLMs
within EC framework to design AFs automatically for cost-aware BO, the approach showcases remarkable
efficiency and generalization for synthetic functions and HPO tasks with heterogeneous costs. Similarly,
FunBO [1] discoveres novel and well-performing AFs for BO by extending FunSearch [128], the discovered
AFs are evaluated on various global optimization benchmarks in and out of the training distribution and
HPO tasks for RBF-based SVM and AdaBoost algorithms.
6.1.4 Prompt Optimization. Prompt optimization aims to identify the most effective task prompt that
maximizes the performance of the LLM on a specific task dataset. Despite of requiring specialized training
for each specific task, traditional discrete or continuous approaches [83, 121] typically necessitate access to
the logits or internal states of LLMs, which may not be applicable when the LLM can only be accessed
through an API. To address these issues, recent works propose to model the optimization problem in
natural language with LLMs as prompts. APE [192] utilizes the LLM as an inference model to generate
instructioncandidatesdirectlybasedonasmallsetofdemonstrationsintheformofinput-outputpairs.This
approach has demonstrated human-level performance on various tasks, including Instruction Induction [60]
and Big-Bench Hard (BBH) [141]. OPRO [167] enables the LLM as an optimizer to gradually generate new
prompts based on the full optimization trajectory, the optimizer prompt showcases significant improvement
compared with human-designed prompts on BBH and GSM8K [25]. Inspired by the numerical gradient
descent method, APO [122] conducts textual “gradient descent” by identifying the current prompts’ flaws
and adjusting the prompt in the opposite semantic direction of the gradient. Similar practices are also
found in the gradient-inspired LLM-based prompt optimizer named GPO [143], as well as the collaborative
optimization approach [52] integrating a gradient-based optimizer and an LLM-based optimizer. Differently,
Guo et al. [50] introduce a discrete prompt tuning framework named EvoPrompt that prompts LLM to act
like evolutionary operators in generating new candidate prompts, harnessing the benefits of evolutionary
algorithms that strike a good balance between exploration and exploitation. StrategyLLM [45] integrates
four LLM-based agents—strategy generator, executor, optimizer, and evaluator—to collaboratively induce
anddeducereasoning.Thismethodgeneratesmoregeneralizableandconsistentfew-shotpromptsthanCoT
prompting techniques.
6.1.5 Optimization Modeling. Optimization modeling [11] aims to construct a mathematical model of a
real-world optimization problem in a standard form, represented with an objective function and a set
of constraints [2, 145]. Recently, LLMs have opened up promising avenues for automating optimization
modeling,facilitatingtheformulationofproblemsandtheimplementationofsolutions,therebydemocratizing
expertise in optimization skills and domain knowledge in various applications. For example, OptiMUS
[2] is developed as an LLM-based agent to formulate and solve optimization problems interpreted from
natural language. Despite its outstanding performance on the proposed NLP4LP dataset [2], the heavy
reliance on sensitive data submission to proprietary LLMs can pose data privacy concerns in industrial
applications. To solve this issue, Tang et al. [145] propose training open-source LLMs with OR-Instruct,
a semi-automated process for generating synthetic data customized to meet specific requirements. The
18

<!-- Page 19 -->

best-performing resulting model named ORLM demonstrates state-of-the-art performance on NL4Opt [124],
MAMO [67], and the proposed IndustryOR benchmark. A related study is found in LM4OPT [3], which
is a progressive fine-tuning framework to enhance LLMs’ specificity for optimization problem formulation
task. To make it accessible to decision makers lacking problem-related modeling skills, DOCP [159] aids
in decision-making by interacting with the user in natural language, and utilizes human’s knowledge and
feedback to create and solve a problem-specific optimization model.
Table1. AnOverviewofOptimizationApplicationsUtilizingLanguageModelsAcrossVariousDomainsandTasks.
Application Method RoleofLLM PromptStrategy SpecificProblemsorTasks

### AEL[87] LLMaD FS,CoT TSP

ReEvo[176] LLMaD CoT,RF TSP

### OPRO[167] LLMaO FS TSP

CombinatorialOptimization

### LMEA[91] Mixed FS TSP


### MLLM[68] Mixed ZS,FS CVRP

FunSearch[128] LLMaD FS CapSetProblem,OnlineBPP

### EoH[88] LLMaD FS,OS,CoT TSP,OnlineBPP,FSSP

MH-LLM*[131] LLMaD ZS,FS SocialNetworksProblem

### LLaMEA[150] LLMaD CoT BBOB

EvoLLM[77] LLMaO FS BBOB,Neuroevolution
OPRO[167] LLMaO FS LinearRegression

### ContinuousOptimization

LEO[14] LLMaO FS NumericalBenchmarks,IndustrialEngineeringProblems
LAEA[56] LLMaP FS,CoT Ellipsoid,Rosenbrock,Ackley,Griewank

### MOEA/D-LMO[86] LLMaO FS ZDT,UF

LLM-MOEA*[136] LLMaE ZS Multi-objectiveSustainableInfrastructurePlanningProblem
CMOEA-LLM[158] LLMaO FS DAS-CMOP

### HPO-LLM*[181] LLMaO FS HPOBench

LLAMBO[93] Mixed FS,ZS,CoT Bayesmark,HPOBench

### BayesianOptimization


### BO-LIFT*[125] LLMaD FS CatalystOptimization

EvolCAF[171] LLMaD FS,OS,CoT SyntheticFunctions,HPO

### FunBO[1] LLMaD FS SyntheticFunctions,HPO

APE[192] LLMaO FS InstructionInduction,BBH

### OPRO[167] LLMaO FS GSM8K,BBH

PromptOptimization APO[122] LLMaO ZS,FS NLPBenchmarkClassificationTasks
GPO[143] LLMaO FS Reasoning,Knowledge-intensive,NLPTasks

### MaaO[52] LLMaO FS NLUTasks,ImageClassificationTasks

EvoPrompt[50] LLMaO CoT,FS LanguageUnderstandingandGenerationTasks,BBH

### StrategyLLM[45] Mixed ZS,FS,CoT ReasoningTasks


### DOCP[159] LLMaO FS,CoT FacilityLocationProblems

OptimizationModeling OptiMUS[2] Mixed ZS,FS NL4LP
ORLMs[145] LLMaD ZS NL4Opt,MAMO,IndustryOR

### LM4OPT[3] LLMaD FS,ZS NL4Opt


### AS-LLM[164] LLMaE ZS AlgorithmSelection

OtherApplications LLaMoCo[101] LLMaD FS OptimizationCodeGeneration
6.1.6 Other Applications. In addition to the previously mentioned optimization applications, we have
identified further uses of LLMs in related fields. For example, AS-LLM [164] utilizes LLMs to extract and
selectkeyalgorithmfeaturesforalgorithmselection,enhancingthematchbetweenalgorithmsandproblems.
LLaMoCo[101]introducesthefirstinstruction-tuningframeworkforLLMs,optimizingcodegenerationwith
a structured instruction set and a two-phase training approach, thereby minimizing the need for extensive
domain expertise and prompt design effort.
19

<!-- Page 20 -->

6.2 Machine Learning
In this subsection, we investigate the applications of LLMs in the machine learning domain, focusing on
their contribution to algorithmic design. These applications are summarized in Table 2.
6.2.1 Task Planning with LLMs. The advent of LLMs has garnered significant interest in their application
to planning tasks, owing to their remarkable generative capabilities of instructions in the form of natural
language. Pioneering work by Huang et al. [65] demonstrates the effectiveness of LLMs in leveraging world
knowledge to produce actionable plans for VirtualHome environments. This method was further enhanced
by Ahn et al. [5], who employed a value function to ground the world knowledge, enabling the derivation of
an optimal policy for robotic task execution in lifelike kitchen settings. In subsequent research, Huang et al.
[66] broaden the scope of grounded information in a more adaptive way. Moreover, Lin et al. [84] utilize
greedy search in combination with heuristic algorithms to refine the planning system. Distinctly, Singh
et al. [137] tackle planning challenges by integrating programming languages, thereby generating code to
streamline planning processes. A more comprehensive approach, named SayCanPay [57], is developed for
planning by considering both the affordance function and reward within the task framework.
6.2.2 Reinforcement Learning. Reinforcement Learning (RL) has been the de facto standard for sequential
decision-making tasks, and recently, the synergy between RL and LLMs has emerged as a novel trend in the
domain.Thisconvergencemirrorsthedynamicsoftaskplanning,yetplacesRLatthecoreofitsmethodology.
Many of the LLM4AD papers on RL is for automatically designing the reward functions [12, 100, 112]. In
addition, Shah et al. [133] investigate the employment of LLMs for heuristic planning to steer the search
processwithinRLframeworks.Zhangetal.[185]integrateLLMsintoRLbyintroducingaKullback-Leibler
divergence regularization term that aligns LLM-driven policies with RL-derived policies. LLMs have also
extendedtheirreachtomulti-agentRLscenarios,asshownbyDuetal.[32],whoillustratestheirapplication
within a Mixture-of-Experts system to direct RL models in the realm of intelligent network solutions.
6.2.3 Neural Architecture Search. Neural Architecture Search (NAS), which is a significant focus within the
AutoML community, has been investigated in many LLM4AD papers. For example, Chen et al. [20] have
integrated LLMs with evolutionary search to successfully generate NAS code for diverse tasks. Nasir et al.
[113] introduce a quality-diversity algorithm tailored to NAS, producing architectures for CIFAR-10 and
NAS-bench-201 benchmarks. Moreover, Morris et al. [110] introduce guided evolution for the development
of neural architectures and suggest the concept of the evolution of thought in algorithm design. Except
for using LLM for design, Jawahar et al. [70] employ LLMs in predicting NAS performance, combining
this approach with evolutionary search to effectively create novel network architectures. In contrast to the
LLM-based architecture design and performance prediction, Zhou et al. [191] explore the adoption of LLMs
for transferring design principles to narrow and guide the search space.
6.2.4 Graph Learning. Graph learning is another application with the advancing capabilities of LLMs in
symbolic reasoning and graph processing. For example, Chen et al. [23] apply LLMs to the task of labeling
in Text-Attributed Graphs (TAGs), capitalizing on the language task proficiency of LLMs. Both Mao et al.
[104] and Chen et al. [21] adopt LLMs in an evolutionary framework for designing functions. The former
evolvesheuristiccodefunctionstoidentifycriticalnodesinagraphwhilethelatteridentifiesmeta-structures
20

<!-- Page 21 -->

within heterogeneous information networks to enhance their interpretability. Moreover, knowledge graphs
have also seen substantial benefits from the application of LLMs. Zhang et al. [184] introduce AutoAlign, a
method that employs LLMs to semantically align entities across different knowledge graphs, and Feng et al.
[41] develop the knowledge search language to effectively conduct searches within knowledge graphs.
6.2.5 Dataset Labeling. LLMs have been used for mining semantic and multi-modal information from
datasets. LLMs are employed to train interpretable classifiers to extract attributes from images [24] and to
generate label functions for weakly supervised learning [48].
Table2. AnOverviewofMachineLearningApplicationsUtilizingLanguageModelsAcrossVariousDomainsandTasks.
Application Method RoleofLLM PromptStrategy SpecificProblemsorTasks

### Zero-Planner[65] LLMaP ZS,FS VirtualHomeTasks


### SayCan[5] LLMaP FS Real-worldKitchenTaskswithRobots

TaskPlanning LLM-GM[66] LLMaP FS Real-worldKitchenTaskswithRobots
Text2Motion[84] LLMaP FS LongSequenceTasksforRobots

### ProgPrompt[137] LLMaD FS,COT VirtualHomeTasks

SayCanPay[57] LLMaP FS VirtualHomeTasks,RavensTasks,BabyAITasks

### LFG[133] LLMaP FS,CoT ObjectNavTasks,Real-worldTasks

SLINVIT[185] LLMaP ZS,FS ALFWorldTasks,InterCodeTasks,BlocksWorldTasks

### ReinforcementLearning MEDIC[12] LLMaP ZS BabyAITasks

Eureka[100] LLMaD FS,CoT IsaacGymTasks,BidexterousManipulationTasks

### EROM[112] LLMaD ZS,CoT IsaacGymTasks


### LLM-MOE[32] LLMaP FS,CoT IntelligentNetworks

EvoPrompting[19] LLMaD FS,ZS,CoT MNISTDataset,CLRSAlgorithmicReasoning
NeuralArchitectureSearch HS-NAS[70] LLMaP FS,ZS,CoT MachineTranslationTasks
LLMatic[113] LLMaD FS,ZS,CoT CIFAR-10Dataset,NAS-bench-201Benchmarks
LAPT[191] LLMaD ZS,FS NAS201,Trans101,DARTs

### LLM-GE[110] LLMaD FS,ZS,CoT CIFAR-10Dataset

LLM-Critical[104] LLMaD FS,ZS,CoT CriticalNodeIdentification
LLM-GNN[23] LLMaP FS,CoT Label-freeNodeClassification

### GraphLearning

ReStruct[21] LLMaE FS,ZS Meta-structureDiscovery
AutoAlign[184] LLMaE FS,ZS EntityTypeInference

### KSL[41] LLMaP FS KnowledgeSearch

Inter-Classier[24] LLMaO FS,ZS iNaturalistDatasets,KikiBoubadatasets

### DatasetLabeling


### DataSculpt[48] LLMaP FS LabelFunctionDesign


### LLM2FEA[160] LLMaP FS,CoT Objective-orientedGeneration

OtherApplications tnGPS[178] LLMaD FS,OS,CoT TensorNetworkStructureSearch

### L-AutoDA[49] LLMaD FS,OS,CoT AdversarialAttack

6.2.6 OtherApplications. OtherapplicationsofLLMsextendtoamyriadofmachinelearningtasks.Notably,
Wongetal.[160]capitalizeonmulti-tasklearningandtheiterativerefinementofpromptstofosterinnovative
design approaches. Zeng et al. [178] integrate LLMs with evolutionary search to develop a heuristic function
aimedatefficientlysiftingthroughcandidatetensorsetsrepresentingtheprimaltensornetwork.Furthermore,
Guo et al. [49] have blazed a trail in employing LLMs to generate novel decision-based adversarial attack
algorithms, thus opening up a new diagram for the automatic assessment of model robustness.
6.3 Science Discovery
This subsection is dedicated to exploring LLM-based scientific discoveries related to algorithm designs.
Table. 3 lists the related works in this domain.
21

<!-- Page 22 -->

6.3.1 General Science Discovery. In the realm of scientific discovery, LLMs are usually adopted for equation
orfunctioinsearch.Notably,Duetal.[34]introduceLLM4ED,aframeworkthatemploysiterativestrategies,
including a black-box optimizer and evolutionary operators, to generate and optimize equations. This
approach has shown significant advancements in stability and usability for uncovering physical laws from
nonlineardynamicsystems.Similarly,Shojaeeetal.[135]presentLLM-SR,whichcombinesLLMs’extensive
scientific knowledge and code generation capabilities with evolutionary search. This framework excels in
proposingandrefininginitialequationstructuresbasedonphysicalunderstanding,outperformingtraditional
symbolicregressionmethodsindiscoveringphysicallyaccurateequationsacrossmultiplescientificdomains.A
bileveloptimizationframework,namedSGA,isintroducebyMaetal.[98].Itmergestheabstractreasoning
capabilities of LLMs with the computational power of simulations. This integration facilitates hypothesis
generationanddiscretereasoningwithsimulationsforexperimentalfeedbackandoptimizationofcontinuous
variables, leading to improved performance.
6.3.2 Chemistry, Biology & Physics. In the field of chemistry, LLMs can be applied not only to conventional
molecular generation and design [13, 69], but also to specialized areas such as drug molecule design [173],
chemicalreactionpredictionandoptimization[126],andcatalystdesign[153],providingcustomizedsolutions.
Furthermore,LLMshavealsoshownpromisingapplicationprospectsinmaterialsdiscovery[71,180],synthesis
route planning [89], green chemistry [129], and other areas. These studies demonstrate the advantages of
LLMs in molecular representation and optimization.
In biology, LLMs are increasingly being used for tasks such as protein engineering [97, 134], enzyme
design[146],andbiologicalsequenceanalysis[42].BycombiningLLMswithvastamountsofbiologicaldata,
they can more accurately predict interactions between biological molecules and significantly improve the
efficiency of bioinformatics workflows. This has important implications for drug discovery and therapeutic
proteindesign.TheuniquesequencegenerationandoptimizationcapabilitiesofLLMsoffernewpossibilities
for tackling combinatorial optimization challenges in biomacromolecular design.
Although applications in physics are relatively fewer, some emerging work has demonstrated the broad
prospectsofLLMs.Panetal.[119]usemulti-stepprompttemplatestoprovethatLLMscanperformcomplex
analytical calculations in theoretical physics. Quantum computing algorithm design, physics simulation
optimization, and computational methods in condensed matter.
6.3.3 Mechanics. MechAgents [114] introduces a class of physics-inspired generative machine learning
platforms that utilize multiple LLMs to solve mechanics problems, such as elasticity, by autonomously
collaborating to write, execute, and self-correct code using finite element methods. Moreover, Du et al. [33]
adoptLLMsinautomaticallydiscoveringgoverningequationsfromdata,utilizingthemodels’generationand
reasoning capabilities to iteratively refine candidate equations. This approach, tested on various nonlinear
systemsincludingtheBurgers,Chafee–Infante,andNavier–Stokesequations,demonstratesasuperiorability
to uncover correct physical laws and shows better generalization on unseen data compared to other models.
AnotherexampleinfluiddynamicshasbeeninvestigatedbyZhuetal.[193],whichintroducesFLUID-LLM,
a novel framework that integrates pre-trained LLMs to enhance the prediction of unsteady fluid dynamics.
AutoTurb [186], on the other hand, adopts LLMs in an evolutionary framework to automatically design and
search for turbulence model in computational fluid dynamics. Furthermore, Buehler [17] study LLM-based
22

<!-- Page 23 -->

methods for forward and inverse mechanics problems including bio-inspired hierarchical honeycomb design,
carbon nanotube mechanics, and protein unfolding.
Table3. AnOverviewofScienceDiscoveryApplicationsUtilizingLanguageModelsAcrossVariousDomainsandTasks.
Application Method RoleofLLM SpecificProblemsorTasks

### Bilevel[98] LLMaD PhysicalScientificDiscovery

GeneralScientificEquationDiscovery LLM-SR[135] LLMaD ScientificEquationDiscovery

### LLM4ED[34] LLMaD EquationDiscovery


### ChatChemTS[69] LLMaD MoleculeDesign

DebjyotiBhattacharya,etal.[13] LLMaO MoleculeDesign
AgustinusKristiadi,etal.[76] LLMaE MoleculeDesign

### Chemical


### BoChemian[126] LLMaE ChemicalReaction

Multi-modalMoLFormer[138] LLMaP BatteryElectrolytesFormulationDesign
CataLM[153] LLMaP CatalystDesign

### GavinYe[173] LLMaD DrugDesign

DrugAssist[174] LLMaO DrugDesign

### MLDE[147] LLMaP ProteinDesign

Prollama[97] Mixed ProteinDesign

### Biology


### X-LoRA[16] LLMaP ProteinDesign


### CodonBERT[82] LLMaP mRNADesignandOptimization

Revisiting-PLMs[62] LLMaP ProteinFunctionPrediction
FLUID-LLM[193] LLMaP ComputationalFluidDynamics
MechAgents[114] LLMaD MechanicsDesign

### Mechanics


### MeLM[17] LLMaP,LLMaD CarbonNanotubesandProteinsDesign

MenggeDu,etal.[33] LLMaD NonlinearDynamicsEquationDiscovery
AutoTurb[186] LLMaD ComputationalFliudDynamics
6.4 Industry
This subsection explores the transformative impact of LLMs on algorithm design across various industries.
As we envision the future of manufacturing, LLMs are poised to play a pivotal role. Existing developments
focus on enhancing research and investment to refine these models while assessing their performance in
terms of safety, bias, and utility. LLMs can be seen as a gateway between humans and machines, facilitating
informed decision-making.
For instance, LLMs are instrumental in building a comprehensive intelligent 6G network system [95],
addressing challenges such as low latency, high-frequency bands, high bandwidth, high transmission rates,
and overall intelligence [190]. Moreover, LLMs have the potential to revolutionize the telecom industry by
streamlining tasks and reducing the need for extensive manpower and engineering expertise. However, it is
crucial to address existing challenges to fully realize their potential [102].
Recently, the application of LLMs in Electronic Design Automation (EDA) has emerged as a promising
area of exploration. LLM-based solutions have been developed to enhance interactions with EDA tools [40].
In particular, within the VLSI design flow, it is essential to verify that the implementation conforms to its
specifications. To achieve this, system verilog assertions need to be generated automatically. Generative AI
techniques, such as LLMs, can be effectively utilized to facilitate this process [109].
To enhance the reliability and availability of cloud services, conducting root cause analysis (RCA) for
cloud incidents is essential. RCACopilot [22] effectively matches incoming incidents with the appropriate
23

<!-- Page 24 -->

incidenthandlersbasedontheiralerttypes.Itaggregatescriticalruntimediagnosticinformation,predictsthe
incident’s root cause category, and provides explanatory results without the need for manual investigations.
More applicable scenarios include various industrial design challenges, such as chip design [18], car shape
design [161], aircraft concept design [96] UI design [43], and robot design [177]. LLMs primarily leverage
billions of web resources. However, practical applications require fine-tuning with thousands of specific
representations of design intent to recognize the distinct patterns associated with each design task. Other
traditional industrial tasks, such as itinerary planning, can also be enhanced by leveraging the power of
LLMs [166]. LLM-based open-domain urban itinerary planning [144] combines spatial optimization with
LLMs to create detailed urban itineraries tailored to users’ requests.
7 Challenges of LLMs in Algorithm Design
7.1 Scalability
One of the primary limitations of LLMs in algorithm design is their scalability. LLMs are limited by a fixed
contextsize,restrictingtheamountofinformationtheycanprocessatonce,whichisachallengeforcomplex
algorithmic tasks requiring detailed specifications and extensive content. Additionally, even when input and
output lengths are sufficient, LLMs struggle with comprehension and reasoning over long inputs, impacting
their effectiveness in designing complex algorithms. For instance, LLMs tend to solve only low-dimensional
problems when used as optimizers [167], and they are employed to design a function or heuristic component
of an algorithm rather than the entire algorithm when used as designers [88].
7.2 Interpretability
Interpretability is another challenge when using pre-trained LLMs for algorithm design. It is difficult to
tracehowspecificinputsleadtoparticularoutputsinLLMsduetotheirblack-boxnature.Thisopacitycan
be problematic, especially in critical applications, e.g., some industry applications, where understanding the
decision-making process is essential for trust and reliability. Efforts to enhance the interpretability involve
techniquessuchasfeaturevisualization,modelsimplification[86],andthestudyofthecontributionofdifferent
parts of the data to the model’s behavior [7]. Despite these efforts, achieving principled interpretability
without compromising the performance of LLMs remains a key area of ongoing research.
7.3 Security
Integrating LLMs into algorithm design introduces significant security risks, including the mishandling of
personal data and the potential creation of harmful code. LLMs are trained on extensive datasets that
often contain sensitive information, posing a risk of privacy breaches if these models inadvertently generate
outputs influenced by this data. Additionally, the autonomous nature of LLMs can lead to the unintentional
developmentofflawedormaliciousalgorithms,whichisacriticalconcerninsectorslikefinancialservicesand
personal data management [187]. To address these issues, it is vital to establish stringent data governance
and model training protocols that prevent the inclusion of sensitive data, rigorously test algorithms under
variousconditionstopreventunintendedbehaviors,andcontinuouslyupdatesecuritymeasurestocounteract
emerging vulnerabilities.
24

<!-- Page 25 -->

7.4 Cost
The utilization of LLMs in algorithm design also faces challenges related to high cost in model training and
usage. Training domain LLMs requires significant computational resources, often involving extensive GPU
or TPU usage over several weeks or even months, which incurs high financial and time costs. Once trained,
the inference cost—the computational expense involved in applying the model to algorithm design—also
becomes a critical factor, especially when the model is used frequently, such as the evolutionary search used
in many LLM4AD works [128]. For practical applications in algorithm design, where multiple iterations and
tests might be necessary, these costs can accumulate, making the use of LLMs potentially less viable for
researchers without substantial computational budgets.
7.5 Idea Innovation
Despite extensive research on LLM4AD, their capacity for generating novel ideas remains questionable.
LLMsareadeptatinterpolatingwithintheirtrainingdatabutoftenfalterinextrapolatingtonewscenarios.
In algorithm design, this means LLMs can suggest or slightly enhance existing algorithms but struggle
to develop radically new methods. Although there is evidence of LLMs producing new ideas in certain
tasks [171], consistently generating practical, innovative concepts continues to be a challenge [63].
8 Future Directions
8.1 Domain LLM for Algorithm Design
Instead of using a general pre-trained general-purpose LLM, it is worthwhile studying how to train an
LLM specifically for automatic algorithm design tasks. The following aspects can be explored in developing
domain LLMs: 1) Training domain LLMs are costly and resource-consuming. On the one hand, advanced
light fine-tuning techniques (e.g., LoRA [61]) could be used for efficient domain adaptation. On the other
hand,thesizeofalgorithmLLMsforaspecificapplicationcanbereducedwiththehelpofdomaindataand
knowledge. 2) Generating and collecting domain data for algorithm design poses challenges. Unlike general
codegenerationorlinguisticprocesstasks,thereisnolargeandformatteddataspecificforalgorithmdesign.
Some Github repositories on algorithms might be helpful, but the resources should be scanned and cleaned
foralgorithmdesign.Lehmanetal.[79]provideanexampleofgenerationdomaindataforLLMs,wherethe
samplesgeneratedduringsearchingareusedasthetrainingdatasettofine-tuneapre-trainedmodelresulting
in better performance on the target problem. 3) Instead of learning a text and code generation model, how
tolearnthealgorithmdevelopmentideasandthealgorithmicreasoningabilityremainunexplored[116,157].
8.2 Multi-modal LLM for Algorithm Design
The primary focus of existing LLM4AD works is on utilizing the text comprehension and generation
capabilities of LLMs, whether in language, code, or statistics. One advantage of LLMs compared to
traditional model-based optimization is their ability to process multi-modal information like humans, which
is rarely studied. Some attempts have been conducted to showcase the advantages of incorporating multimodal information in algorithm design, as evidenced by Huang et al. [68] and Narin [112]. It is anticipated
that more methods and applications utilizing multi-modal LLMs will be developed in the future.
25

<!-- Page 26 -->

8.3 Interaction with Human Experts
Further research is needed to explore the interaction between LLMs and human experts in algorithm
design [81]. For example, in LLMaD works, LLMs can be seen as intelligent agents, making it feasible for
human experts to step in and take over tasks such as generating, modifying, and evaluating algorithms.
Investigating how to facilitate efficient and productive collaboration between LLMs and human experts
would be valuable. Ideas and techniques in collective intelligence [103] can be used for this purpose.
8.4 Multi-objective Algorithm Design
Thereareusuallymultiplecriteria(e.g.,optimalsolutiongeneratedbyalgorithm,optimizationefficiency,and
generalizationperformance)inreal-worldalgorithmdesign.ThemajorityofexistingLLM4ADpapersconsider
one objective [88, 128] focusing only the optimal solutions. A preliminary attempt has been conducted
by Yao et al. [170], where a dominance-dissimilarity measurement, considering both the dominance relation
in objective space and the distance in code space, is designed for efficient multi-objective search in the
heuristics space. More future works are anticipated to develop new methods for effective multi-objective
algorithm design.
8.5 LLM-based Algorithm Assessment
LLMs can be benefitial in algorithm assessment. Some attempts have been carried out on test instance
generation and algorithm evaluation. For example, Jorgensen et al. [74] use LLMs to generate test cases of
increasing difficulties to enhance genetic programming and OMNI-EPIC [38] utilizes LLMs to automatically
produce code that defines the next engaging and learnable tasks for algorithm evaluation. Further research
in this area is anticipated.
8.6 Understand the Behavior of LLM
In the majority of works, LLM works as a black-box model. The interpretation of LLM’s behavior not
only enriches our understanding of LLM’s behavior but also benefits cases where it is challenging or costly
to directly request LLMs. Some attempts have been made to approximate and understand the in-context
learningbehaviorofLLMinsolutiongeneration.Forexample,Liuetal.[86]hasdesignedawhite-boxlinear
operator to approximate the results of LLM in multi-objective evolutionary optimization. In spite of these
preliminary attempts, how to interpret LLM’s behavior is still an open question in many algorithm design
cases including heuristic generation and idea exploration.
8.7 Fully Automatic Algorithm Design
Fully automatic algorithm design faces two primary challenges: 1) the generation of novel algorithmic ideas
and 2) the creation of complex, lengthy code. While the generation of new ideas has been investigated in
some works [88], the complete design of algorithms (instead of a heuristic component), remains a challenge.
Existing applications typically focus on automating components within predefined algorithm frameworks
rather than creating new algorithms from scratch. Future research needs to tackle these complexities to
advance the field of fully automatic algorithm design.
8.8 Benchmarking LLM4AD
Benchmarking allows for a fair, standardized, and convenient comparison, which can identify best practices
and enable generating new insights for innovation. While we are glad to witness the emergence of diverse
26

<!-- Page 27 -->

researchworksandapplications,LLM4ADstilllacksabenchmarkingoneitheralgorithmdesigntestsetsfor
systematic and scientific assessment or a strict pipeline and evaluation criteria on large language models for
algorithmdesign.Severalattemptshavebeenmadeonrelatedtopicssuchasmathematicalreasoning[85]and
planning[149].[151]presentsanalgorithmtestsetbuiltonsomebasicalgorithmsand[105]demonstratesthe
superiorperformanceofLLMwhencomparedtoneuralalgorithmreasoners.Inthefuture,morebenchmarks
are expected and they are going to play a crucial role in advancing LLM4AD.
9 Conclusion
This paper has provided a systematic and up-to-date survey on large language models for algorithm design
(LLM4AD). By systematically reviewing a significant corpus of main contributions in this emerging research
field, this paper not only highlights the current state and evolution of LLM applications in algorithm design
but also introduces a multi-dimensional taxonomy with comprehensive lists of papers that categorize the
roles and functionalities of LLMs in this domain. This taxonomy serves as a framework for both academic
and industrial researchers to understand and navigate the complex landscape of algorithm design using
LLMs. We have also identified the limitations and challenges currently faced by the field, such as issues
of scalability, interpretability, and security. Moreover, we have highlighted and discussed some promising
research directions to inspire and guide future studies.
As we look forward, the intersection of LLMs and algorithm design holds promising potential for
revolutionizing how algorithms are developed and implemented. We hope this paper can contribute to a
deeper understanding of this potential and set the stage for future innovations and collaborations in this
emerging avenue of research.

### References

[1] VirginiaAglietti,IraKtena,JessicaSchrouff,EleniSgouritsa,FranciscoJRRuiz,AlexisBellot,andSilviaChiappa.2024.
FunBO:DiscoveringAcquisitionFunctionsforBayesianOptimizationwithFunSearch.arXivpreprintarXiv:2406.04824
(2024).
[2] AliAhmadiTeshnizi,WenzhiGao,andMadeleineUdell.2023. Optimus:Optimizationmodelingusingmipsolversand
largelanguagemodels. arXivpreprintarXiv:2310.06116 (2023).
[3] Tasnim Ahmed and Salimur Choudhury. 2024. LM4OPT: Unveiling the potential of Large Language Models in
formulatingmathematicaloptimizationproblems. INFOR:InformationSystemsandOperationalResearch (2024),
1–14.
[4] Janice Ahn, Rishu Verma, Renze Lou, Di Liu, Rui Zhang, and Wenpeng Yin. 2024. Large language models for
mathematicalreasoning:Progressesandchallenges. arXivpreprintarXiv:2402.00157 (2024).
[5] MichaelAhn,AnthonyBrohan,NoahBrown,YevgenChebotar,OmarCortes,ByronDavid,ChelseaFinn,Keerthana
Gopalakrishnan,KarolHausman,AlexanderHerzog,DanielHo,JasmineHsu,JulianIbarz,BrianIchter,AlexIrpan,
EricJang,RosarioJaureguiRuano,KyleJeffrey,SallyJesmonth,NikhilJ.Joshi,RyanJulian,DmitryKalashnikov,
YuhengKuang,Kuang-HueiLee,SergeyLevine,YaoLu,LindaLuu,CarolinaParada,PeterPastor,JornellQuiambao,
KanishkaRao,JarekRettinghouse,DiegoReyes,PierreSermanet,NicolasSievers,ClaytonTan,AlexanderToshev,
VincentVanhoucke,FeiXia,TedXiao,PengXu,SichunXu,andMengyuanYan.2022. DoAsICan,NotAsISay:
GroundingLanguageinRoboticAffordances. CoRR(2022).
[6] Mohammad Alipour-Vaezi and Kwok-Leung Tsui. 2024. Data-Driven Portfolio Management for Motion Pictures
Industry:ANewData-DrivenOptimizationMethodologyUsingaLargeLanguageModelastheExpert. arXivpreprint
arXiv:2404.07434 (2024).
[7] ZeyuanAllen-ZhuandYuanzhiLi.2023. Physicsoflanguagemodels:Part3.1,knowledgestorageandextraction.
arXivpreprintarXiv:2309.14316 (2023).
[8] DavidEricAustin,AntonKorikov,ArminToroghi,andScottSanner.2024. BayesianOptimizationwithLLM-Based
AcquisitionFunctionsforNaturalLanguagePreferenceElicitation. arXivpreprintarXiv:2405.00981 (2024).
27

<!-- Page 28 -->

[9] RobertBecker,LauraSteffny,ThomasBleistein,andDirkWerth.2024.FromDatatoDesign:LLM-enabledinformation
extractionacrossindustries. atpmagazin 66,6-7(2024),80–87.
[10] Yoshua Bengio, Andrea Lodi, and Antoine Prouvost. 2021. Machine learning for combinatorial optimization: a
methodologicaltourd’horizon. EuropeanJournalofOperationalResearch 290,2(2021),405–421.
[11] JohnBerryandKenHouston.1995. Mathematicalmodelling. GulfProfessionalPublishing.
[12] Siddhant Bhambri, Amrita Bhattacharjee, Huan Liu, and Subbarao Kambhampati. 2024. Efficient Reinforcement
LearningviaLargeLanguageModel-basedSearch. arXivpreprintarXiv:2405.15194 (2024).
[13] DebjyotiBhattacharya,HarrisonJCassady,MichaelAHickner,andWesleyFReinhart.2024. LargeLanguageModels
asMolecularDesignEngines. JournalofChemicalInformationandModeling(2024).
[14] ShuvayanBrahmachary,SubodhMJoshi,AniruddhaPanda,KaushikKoneripalli,ArunKumarSagotra,HarshilPatel,
AnkushSharma,AmeyaDJagtap,andKaushicKalyanaraman.2024. LargeLanguageModel-BasedEvolutionary
Optimizer:Reasoningwithelitism. arXivpreprintarXiv:2403.02054 (2024).
[15] DavidBrandfonbrener,SimonHenniger,SibiRaja,TarunPrasad,ChloeLoughridge,FedericoCassano,SabrinaRuixin
Hu, Jianang Yang, William E. Byrd, Robert Zinkov, and Nada Amin. 2024. VerMCTS: Synthesizing Multi-Step
ProgramsusingaVerifier,aLargeLanguageModel,andTreeSearch. arXiv:2402.08147[cs.SE]
[16] EricLBuehlerandMarkusJBuehler.2024. X-LoRA:Mixtureoflow-rankadapterexperts,aflexibleframeworkfor
largelanguagemodelswithapplicationsinproteinmechanicsandmoleculardesign. APL Machine Learning 2,2
(2024).
[17] MarkusJBuehler.2023. MeLM,agenerativepretrainedlanguagemodelingframeworkthatsolvesforwardandinverse
mechanicsproblems. JournaloftheMechanicsandPhysicsofSolids181(2023),105454.
[18] KaiyanChang,KunWang,NanYang,YingWang,DantongJin,WenlongZhu,ZhirongChen,CangyuanLi,HaoYan,
YunhaoZhou,etal.2024. Dataisallyouneed:FinetuningLLMsforChipDesignviaanAutomateddesign-data
augmentationframework. arXivpreprintarXiv:2403.11202 (2024).
[19] AngelicaChen,DavidDohan,andDavidSo.2023.EvoPrompting:LanguageModelsforCode-LevelNeuralArchitecture
Search.InAdvancesinNeuralInformationProcessingSystems.
[20] AngelicaChen,DavidDohan,andDavidSo.2024. EvoPrompting:languagemodelsforcode-levelneuralarchitecture
search. AdvancesinNeuralInformationProcessingSystems36(2024).
[21] LinChen,FengliXu,NianLi,ZhenyuHan,MengWang,YongLi,andPanHui.2024. LargeLanguageModel-driven
Meta-structureDiscoveryinHeterogeneousInformationNetwork.InProceedingsofthe30thACMSIGKDDConference
onKnowledgeDiscoveryandDataMining,KDD.ACM.
[22] YinfangChen,HuaibingXie,MinghuaMa,YuKang,XinGao,LiuShi,YunjieCao,XuedongGao,HaoFan,Ming
Wen,etal.2024. Automaticrootcauseanalysisvialargelanguagemodelsforcloudincidents.InProceedingsofthe
NineteenthEuropeanConferenceonComputerSystems.674–688.
[23] ZhikaiChen,HaitaoMao,HongzhiWen,HaoyuHan,WeiJin,HaiyangZhang,HuiLiu,andJiliangTang.2024. LabelfreeNodeClassificationonGraphswithLargeLanguageModels(LLMs).InTheTwelfthInternationalConferenceon
LearningRepresentations. https://openreview.net/forum?id=hESD2NJFg8
[24] MiaChiquier,UtkarshMall,andCarlVondrick.2024. EvolvingInterpretableVisualClassifierswithLargeLanguage
Models. CoRR(2024).
[25] KarlCobbe,VineetKosaraju,MohammadBavarian,MarkChen,HeewooJun,LukaszKaiser,MatthiasPlappert,Jerry
Tworek,JacobHilton,ReiichiroNakano,etal.2021. Trainingverifierstosolvemathwordproblems. arXivpreprint
arXiv:2110.14168 (2021).
[26] ThomasHCormen,CharlesELeiserson,RonaldLRivest,andCliffordStein.2022. Introductiontoalgorithms. MIT
press.
[27] Chris Cummins, Volker Seeker, Dejan Grubisic, Baptiste Roziere, Jonas Gehring, Gabriel Synnaeve, and Hugh
Leather.2024. MetaLargeLanguageModelCompiler:FoundationModelsofCompilerOptimization. arXivpreprint
arXiv:2407.02524 (2024).
[28] Leonardo Lucio Custode, Fabio Caraffini, Anil Yaman, and Giovanni Iacca. 2024. An investigation on the use of
LargeLanguageModelsforhyperparametertuninginEvolutionaryAlgorithms.InProceedingsoftheGeneticand
EvolutionaryComputationConferenceCompanion.1838–1845.
[29] NicolaDainese,MatteoMerler,MinttuAlakuijala,andPekkaMarttinen.2024. GeneratingCodeWorldModelswith
LargeLanguageModelsGuidedbyMonteCarloTreeSearch. arXivpreprintarXiv:2405.15383 (2024).
[30] JacobdeNobel,FurongYe,DiederickVermetten,HaoWang,CarolaDoerr,andThomasBäck.2024. Iohexperimenter:
Benchmarkingplatformforiterativeoptimizationheuristics. EvolutionaryComputation (2024),1–6.
[31] TuanDinh,YuchenZeng,RuisuZhang,ZiqianLin,MichaelGira,ShashankRajput,Jy-yongSohn,DimitrisPapailiopoulos,andKangwookLee.2022. Lift:Language-interfacedfine-tuningfornon-languagemachinelearningtasks.
AdvancesinNeuralInformationProcessingSystems35(2022),11763–11784.
28

<!-- Page 29 -->

[32] HongyangDu,GuangyuanLiu,YijingLin,DusitNiyato,JiawenKang,ZehuiXiong,andDongInKim.2024. Mixture
ofExpertsforNetworkOptimization:ALargeLanguageModel-enabledApproach. arXivpreprintarXiv:2402.09756
(2024).
[33] MenggeDu,YuntianChen,ZhongzhengWang,LongfengNie,andDongxiaoZhang.2024. Largelanguagemodelsfor
automaticequationdiscoveryofnonlineardynamics. PhysicsofFluids36,9(2024).
[34] MenggeDu,YuntianChen,ZhongzhengWang,LongfengNie,andDongxiaoZhang.2024. LLM4ED:LargeLanguage
ModelsforAutomaticEquationDiscovery. arXivpreprintarXiv:2405.07761 (2024).
[35] Shukai Duan, Nikos Kanakaris, Xiongye Xiao, Heng Ping, Chenyu Zhou, Nesreen K Ahmed, Guixiang Ma, Mihai
Capota,TheodoreLWillke,ShahinNazarian,etal.2023. LeveragingReinforcementLearningandLargeLanguage
ModelsforCodeOptimization. arXivpreprintarXiv:2312.05657 (2023).
[36] NaokiEgami,MusashiHinck,BrandonStewart,andHanyingWei.2024. Usingimperfectsurrogatesfordownstream
inference: Design-based supervised learning for social science applications of large language models. Advances in
NeuralInformationProcessingSystems36(2024).
[37] KatharinaEggensperger,PhilippMüller,NeeratyoyMallik,MatthiasFeurer,RenéSass,AaronKlein,NoorAwad,
MariusLindauer,andFrankHutter.2021. HPOBench:Acollectionofreproduciblemulti-fidelitybenchmarkproblems
forHPO. arXivpreprintarXiv:2109.06716 (2021).
[38] Maxence Faldor, Jenny Zhang, Antoine Cully, and Jeff Clune. 2024. OMNI-EPIC: Open-endedness via Models of
humanNotionsofInterestingnesswithEnvironmentsProgrammedinCode. arXivpreprintarXiv:2405.15568 (2024).
[39] Zhun Fan, Wenji Li, Xinye Cai, Hui Li, Caimin Wei, Qingfu Zhang, Kalyanmoy Deb, and Erik Goodman. 2020.
Difficultyadjustableandscalableconstrainedmultiobjectivetestproblemtoolkit. Evolutionarycomputation 28,3
(2020),339–378.
[40] Wenji Fang, Mengming Li, Min Li, Zhiyuan Yan, Shang Liu, Hongce Zhang, and Zhiyao Xie. 2024. Assertllm:
Generatingandevaluatinghardwareverificationassertionsfromdesignspecificationsviamulti-llms. arXivpreprint
arXiv:2402.00386 (2024).
[41] ChaoFeng,XinyuZhang,andZichuFei.2023. KnowledgeSolver:TeachingLLMstoSearchforDomainKnowledge
fromKnowledgeGraphs. (2023).
[42] RuijunFeng,ChiZhang,andYangZhang.2024. Largelanguagemodelsforbiomolecularanalysis:Frommethodsto
applications. TrACTrendsinAnalyticalChemistry(2024),117540.
[43] SidongFeng,MingyueYuan,JieshanChen,ZhenchangXing,andChunyangChen.2023. DesigningwithLanguage:
WireframingUIDesignIntentwithGenerativeLargeLanguageModels. arXivpreprintarXiv:2312.07755 (2023).
[44] PeterIFrazierandJialeiWang.2016. Bayesianoptimizationformaterialsdesign. Informationscienceformaterials
discoveryanddesign (2016),45–75.
[45] ChangGao,HaiyunJiang,DengCai,ShumingShi,andWaiLam.2023. Strategyllm:Largelanguagemodelsasstrategy
generators,executors,optimizers,andevaluatorsforproblemsolving. arXivpreprintarXiv:2311.08803 (2023).
[46] KaranGirotra,LennartMeincke,ChristianTerwiesch,andKarlTUlrich.2023.Ideasaredimesadozen:Largelanguage
modelsforideagenerationininnovation. AvailableatSSRN4526071 (2023).
[47] JuliaGrosse,RuotianWu,AhmadRashid,PhilippHennig,PascalPoupart,andAgustinusKristiadi.2024. Uncertainty-
GuidedOptimizationonLargeLanguageModelSearchTrees. arXivpreprintarXiv:2407.03951 (2024).
[48] NaiqingGuan,KaiwenChen,andNickKoudas.2023. CanLargeLanguageModelsDesignAccurateLabelFunctions?

### CoRR(2023). arXiv:2311.00739

[49] PingGuo,FeiLiu,XiLin,QingchuanZhao,andQingfuZhang.2024. L-autoda:Leveraginglargelanguagemodelsfor
automateddecision-basedadversarialattacks. arXivpreprintarXiv:2401.15335 (2024).
[50] QingyanGuo,RuiWang,JunliangGuo,BeiLi,KaitaoSong,XuTan,GuoqingLiu,JiangBian,andYujiuYang.2023.
Connectinglargelanguagemodelswithevolutionaryalgorithmsyieldspowerfulpromptoptimizers. arXivpreprint
arXiv:2309.08532 (2023).
[51] ZixianGuo,MingLiu,ZhilongJi,JinfengBai,YiwenGuo,andWangmengZuo.[n.d.]. TwoOptimizersAreBetter
ThanOne:LLMCatalystEmpowersGradient-BasedOptimizationforPromptTuning. arXiv:2405.19732[cs.CV]
[52] ZixianGuo,MingLiu,ZhilongJi,JinfengBai,YiwenGuo,andWangmengZuo.2024. TwoOptimizersAreBetter
ThanOne:LLMCatalystforEnhancingGradient-BasedOptimization. arXivpreprintarXiv:2405.19732 (2024).
[53] MuhammadUsmanHadi,QasemAlTashi,AbbasShah,RizwanQureshi,AmgadMuneer,MuhammadIrfan,Anas
Zafar,MuhammadBilalShaikh,NaveedAkhtar,JiaWu,etal.2024. Largelanguagemodels:acomprehensivesurvey
ofitsapplications,challenges,limitations,andfutureprospects. AuthoreaPreprints(2024).
[54] KunalHanda,YarinGal,ElliePavlick,NoahGoodman,JacobAndreas,AlexTamkin,andBelindaZLi.2024. Bayesian
preferenceelicitationwithlanguagemodels. arXivpreprintarXiv:2403.05534 (2024).
[55] NikolausHansenandRaymondRos.2010. Black-boxoptimizationbenchmarkingofNEWUOAcomparedtoBIPOP-
CMA-ES:ontheBBOBnoiselesstestbed.InProceedingsofthe12thannualconferencecompaniononGeneticand
29

<!-- Page 30 -->

evolutionarycomputation.1519–1526.
[56] Hao Hao, Xiaoqun Zhang, and Aimin Zhou. 2024. Large Language Models as Surrogate Models in Evolutionary
Algorithms:APreliminaryStudy. arXivpreprintarXiv:2406.10675 (2024).
[57] RishiHazra,PedroZuidbergDosMartires,andLucDeRaedt.2024. Saycanpay:Heuristicplanningwithlargelanguage
modelsusinglearnabledomainknowledge.InProceedingsoftheAAAIConferenceonArtificialIntelligence,Vol.38.
20123–20133.
[58] ChengHe,YeTian,andZhichaoLu.[n.d.]. ArtificialEvolutionaryIntelligence(AEI):EvolutionaryComputation
EvolveswithLargeLanguageModels. ([n.d.]).
[59] ErikHemberg,StephenMoskal,andUna-MayO’Reilly.2024. Evolvingcodewithalargelanguagemodel. Genetic
ProgrammingandEvolvableMachines25,2(2024),21.
[60] OrHonovich,UriShaham,SamuelRBowman,andOmerLevy.2022. Instructioninduction:Fromfewexamplesto
naturallanguagetaskdescriptions. arXivpreprintarXiv:2205.10782 (2022).
[61] EdwardJHu,PhillipWallis,ZeyuanAllen-Zhu,YuanzhiLi,SheanWang,LuWang,WeizhuChen,etal.2022. LoRA:
Low-RankAdaptationofLargeLanguageModels.InInternationalConferenceonLearningRepresentations.
[62] MingyangHu,FajieYuan,KevinYang,FusongJu,JinSu,HuiWang,FeiYang,andQiuyangDing.2022. Exploring
evolution-aware &-free protein language models as protein function predictors. Advances in Neural Information
ProcessingSystems35(2022),38873–38884.
[63] ShengranHu,CongLu,andJeffClune.2024. Automateddesignofagenticsystems. arXivpreprintarXiv:2408.08435
(2024).
[64] SenHuang,KaixiangYang,ShengQi,andRuiWang.2024. WhenLargeLanguageModelMeetsOptimization. arXiv
preprintarXiv:2405.10098 (2024).
[65] WenlongHuang,PieterAbbeel,DeepakPathak,andIgorMordatch.2022. LanguageModelsasZero-ShotPlanners:
ExtractingActionableKnowledgeforEmbodiedAgents.InInternationalConferenceonMachineLearning,ICML
(ProceedingsofMachineLearningResearch).PMLR.
[66] Wenlong Huang, Fei Xia, Dhruv Shah, Danny Driess, Andy Zeng, Yao Lu, Pete Florence, Igor Mordatch, Sergey
Levine,KarolHausman,andBrianIchter.2023. GroundedDecoding:GuidingTextGenerationwithGroundedModels
forEmbodiedAgents.InAdvancesinNeuralInformationProcessingSystems36:AnnualConferenceonNeural
InformationProcessingSystems2023,NeurIPS.
[67] XuhanHuang,QingningShen,YanHu,AnningzheGao,andBenyouWang.2024. Mamo:aMathematicalModeling
BenchmarkwithSolvers. arXivpreprintarXiv:2405.13144 (2024).
[68] Yuxiao Huang, Wenjie Zhang, Liang Feng, Xingyu Wu, and Kay Chen Tan. 2024. How multimodal integration
boosttheperformanceofllmforoptimization:Casestudyoncapacitatedvehicleroutingproblems. arXivpreprint
arXiv:2403.01757 (2024).
[69] ShoichiIshida,TomohiroSato,TerukiHonma,andKeiTerayama.2024. LargeLanguageModelsOpenNewWayof
AI-AssistedMoleculeDesignforChemists. (2024).
[70] Ganesh Jawahar, Muhammad Abdul-Mageed, Laks VS Lakshmanan, and Dujian Ding. 2023. LLM Performance
PredictorsaregoodinitializersforArchitectureSearch. arXivpreprintarXiv:2310.16712 (2023).
[71] ShuyiJia,ChaoZhang,andVictorFung.2024. LLMatDesign:AutonomousMaterialsDiscoverywithLargeLanguage
Models. arXivpreprintarXiv:2406.13163 (2024).
[72] JuyongJiang,FanWang,JiasiShen,SungjuKim,andSunghunKim.2024. ASurveyonLargeLanguageModelsfor
CodeGeneration. arXivpreprintarXiv:2406.00515 (2024).
[73] MatthewJin,SyedShahriar,MicheleTufano,XinShi,ShuaiLu,NeelSundaresan,andAlexeySvyatkovskiy.2023.
Inferfix:End-to-endprogramrepairwithllms.InProceedingsofthe31stACMJointEuropeanSoftwareEngineering
ConferenceandSymposiumontheFoundationsofSoftwareEngineering.1646–1656.
[74] Steven Jorgensen, Giorgia Nadizar, Gloria Pietropolli, Luca Manzoni, Eric Medvet, Una-May O’Reilly, and Erik
Hemberg.2024. LargeLanguageModel-basedTestCaseGenerationforGPAgents.InProceedingsoftheGeneticand
EvolutionaryComputationConference.914–923.
[75] JKleinberg.2006. AlgorithmDesign.Vol.92. PearsonEducation.
[76] AgustinusKristiadi,FelixStrieth-Kalthoff,MartaSkreta,PascalPoupart,AlanAspuru-Guzik,andGeoffPleiss.2024.
ASoberLookatLLMsforMaterialDiscovery:AreTheyActuallyGoodforBayesianOptimizationOverMolecules?.
InForty-firstInternationalConferenceonMachineLearning. https://openreview.net/forum?id=Pa3GyTe3kf
[77] RobertLange,YingtaoTian,andYujinTang.2024. Largelanguagemodelsasevolutionstrategies.InProceedingsof
theGeneticandEvolutionaryComputationConferenceCompanion.579–582.
[78] JoelLehman,JonathanGordon,ShawnJain,KamalNdousse,CathyYeh,andKennethOStanley.2023. Evolution
throughlargemodels. InHandbookofEvolutionaryMachineLearning.Springer,331–366.
30

<!-- Page 31 -->

[79] JoelLehman,JonathanGordon,ShawnJain,KamalNdousse,CathyYeh,andKennethO.Stanley.2024. Evolution
ThroughLargeModels. SpringerNatureSingapore,Singapore,331–366.
[80] HaoLi,XueYang,ZhaokaiWang,XizhouZhu,JieZhou,YuQiao,XiaogangWang,HongshengLi,LeweiLu,andJifeng
Dai.2024. Automc-reward:Automateddenserewarddesignwithlargelanguagemodelsforminecraft.InProceedings
oftheIEEE/CVFConferenceonComputerVisionandPatternRecognition.16426–16435.
[81] JiayangLi,JialeLi,andYunshengSu.2024. AMapofExploringHumanInteractionPatternswithLLM:Insightsinto
CollaborationandCreativity.InInternationalConferenceonHuman-ComputerInteraction.Springer,60–85.
[82] SizhenLi,SaeedMoayedpour,RuijiangLi,MichaelBailey,SalehRiahi,LorenzoKogler-Anele,MiladMiladi,Jacob
Miner,DinghaiZheng,JunWang,etal.2023. Codonbert:Largelanguagemodelsformrnadesignandoptimization.
bioRxiv(2023),2023–09.
[83] XiangLisaLiandPercyLiang.2021. Prefix-tuning:Optimizingcontinuouspromptsforgeneration. arXivpreprint
arXiv:2101.00190 (2021).
[84] KevinLin,ChristopherAgia,TokiMigimatsu,MarcoPavone,andJeannetteBohg.2023. Text2motion:Fromnatural
languageinstructionstofeasibleplans. AutonomousRobots47,8(2023),1345–1365.
[85] XiaohanLin,QingxingCao,YinyaHuang,ZhichengYang,ZhengyingLiu,ZhenguoLi,andXiaodanLiang.2024. ATG:
BenchmarkingAutomatedTheoremGenerationforGenerativeLanguageModels. arXivpreprintarXiv:2405.06677
(2024).
[86] FeiLiu,XiLin,ZhenkunWang,ShunyuYao,XialiangTong,MingxuanYuan,andQingfuZhang.2023. LargeLanguage
ModelforMulti-objectiveEvolutionaryOptimization. arXivpreprintarXiv:2310.12541 (2023).
[87] FeiLiu,XialiangTong,MingxuanYuan,andQingfuZhang.2023. Algorithmevolutionusinglargelanguagemodel.
arXivpreprintarXiv:2311.15249 (2023).
[88] Fei Liu, Tong Xialiang, Mingxuan Yuan, Xi Lin, Fu Luo, Zhenkun Wang, Zhichao Lu, and Qingfu Zhang. 2024.
EvolutionofHeuristics:TowardsEfficientAutomaticAlgorithmDesignUsingLargeLanguageModel.InForty-first
InternationalConferenceonMachineLearning.
[89] GangLiu,MichaelSun,WojciechMatusik,MengJiang,andJieChen.2024. MultimodalLargeLanguageModelsfor
InverseMolecularDesignwithRetrosyntheticPlanning. arXivpreprintarXiv:2410.04223 (2024).
[90] Max Liu, Chan-Hung Yu, Wei-Hsu Lee, Cheng-Wei Hung, Yen-Chun Chen, and Shao-Hua Sun. 2024. Synthesizing Programmatic Reinforcement Learning Policies with Large Language Model Guided Search. arXiv preprint
arXiv:2405.16450 (2024).
[91] ShengcaiLiu,CaishunChen,XinghuaQu,KeTang,andYew-SoonOng.2024. Largelanguagemodelsasevolutionary
optimizers.In2024IEEECongressonEvolutionaryComputation(CEC).IEEE,1–8.
[92] Siyi Liu, Chen Gao, and Yong Li. 2024. Large Language Model Agent for Hyper-Parameter Optimization. arXiv
preprintarXiv:2402.01881 (2024).
[93] TennisonLiu,NicolásAstorga,NabeelSeedat,andMihaelavanderSchaar.2024. Largelanguagemodelstoenhance
bayesianoptimization. arXivpreprintarXiv:2402.03921 (2024).
[94] ZhiweiLiu,WeiranYao,JianguoZhang,LiangweiYang,ZuxinLiu,JuntaoTan,PrafullaKChoubey,TianLan,Jason
Wu,HuanWang,etal.2024. AgentLite:ALightweightLibraryforBuildingandAdvancingTask-OrientedLLMAgent
System. arXivpreprintarXiv:2402.15538 (2024).
[95] SifanLong,FengxiaoTang,YangfanLi,TiaoTan,ZhengjieJin,MingZhao,andNeiKato.2024. 6Gcomprehensive
intelligence:networkoperationsandoptimizationbasedonLargeLanguageModels. arXivpreprintarXiv:2404.18373
(2024).
[96] Jorge Lovaco, Raghu Chaitanya Munjulury, Ingo Staack, and Petter Krus. 2024. LARGE LANGUAGE MODEL-

## Drivensimulationsforsystemofsystemsanalysisinfirefightingaircraftconceptual

DESIGN.In34thCongressoftheInternationalCounciloftheAeronauticalSciences,2024.
[97] Liuzhenghao Lv, Zongying Lin, Hao Li, Yuyang Liu, Jiaxi Cui, Calvin Yu-Chian Chen, Li Yuan, and Yonghong
Tian.2024. Prollama:Aproteinlargelanguagemodelformulti-taskproteinlanguageprocessing. arXiv preprint
arXiv:2402.16445 (2024).
[98] PingchuanMa,Tsun-HsuanWang,MinghaoGuo,ZhiqingSun,JoshuaBTenenbaum,DanielaRus,ChuangGan,and
WojciechMatusik.2024. LLMandSimulationasBilevelOptimizers:ANewParadigmtoAdvancePhysicalScientific
Discovery. arXivpreprintarXiv:2405.09783 (2024).
[99] RuotianMa,XiaoleiWang,XinZhou,JianLi,NanDu,TaoGui,QiZhang,andXuanjingHuang.2024. AreLarge
LanguageModelsGoodPromptOptimizers? arXivpreprintarXiv:2402.02101 (2024).
[100] YechengJasonMa,WilliamLiang,GuanzhiWang,De-AnHuang,OsbertBastani,DineshJayaraman,YukeZhu,Linxi
Fan,andAnimaAnandkumar.2024. Eureka:Human-LevelRewardDesignviaCodingLargeLanguageModels.InThe
TwelfthInternationalConferenceonLearningRepresentations.
31

<!-- Page 32 -->

[101] ZeyuanMa,HongshuGuo,JiachengChen,GuojunPeng,ZhiguangCao,YiningMa,andYue-JiaoGong.2024.LLaMoCo:
InstructionTuningofLargeLanguageModelsforOptimizationCodeGeneration. arXivpreprintarXiv:2403.01131
(2024).
[102] AliMaatouk,NicolaPiovesan,FadhelAyed,AntonioDeDomenico,andMerouaneDebbah.2024. Largelanguage
modelsfortelecom:Forthcomingimpactontheindustry. IEEECommunicationsMagazine(2024).
[103] ThomasWMaloneandMichaelSBernstein.2022. Handbookofcollectiveintelligence. MITpress.
[104] JinzhuMao,DongyunZou,LiSheng,SiyiLiu,ChenGao,YueWang,andYongLi.2024. IdentifyCriticalNodesin
ComplexNetworkwithLargeLanguageModels. (2024).
[105] SeanMcLeish,AviSchwarzschild,andTomGoldstein.2024. BenchmarkingChatGPTonAlgorithmicReasoning. arXiv
preprintarXiv:2404.03441 (2024).
[106] NavidMehrdad,HrushikeshMohapatra,MossaabBagdouri,PrijithChandran,AlessandroMagnani,XunfanCai,Ajit
Puthenputhussery,SachinYadav,TonyLee,ChengXiangZhai,etal.2024. LargeLanguageModelsforRelevance
JudgmentinProductSearch. arXivpreprintarXiv:2406.00247 (2024).
[107] AbdulkadirMemduhoğlu,NirFulman,andAlexanderZipf.2024. EnrichingbuildingfunctionclassificationusingLarge
LanguageModelembeddingsofOpenStreetMapTags. EarthScienceInformatics(2024),1–16.
[108] Jean-YvesPotvinMichelGendreau.2019. Handbookofmetaheuristics. Springer.
[109] SamitShahnawazMiftah,AmishaSrivastava,HyunminKim,andKanadBasu.2024.Assert-O:Context-basedAssertion
OptimizationusingLLMs.InProceedingsoftheGreatLakesSymposiumonVLSI2024.233–239.
[110] ClintMorris,MichaelJurado,andJasonZutty.2024. LLMGuidedEvolution-TheAutomationofModelsAdvancing
Models. arXivpreprintarXiv:2403.11446 (2024).
[111] MahdiMostajabdaveh,TimothyTYu,RindranirinaRamamonjison,GiuseppeCarenini,ZiruiZhou,andYongZhang.

## Optimization modeling and verification from problem specifications using a multi-agent multi-stage LLM

framework. INFOR:InformationSystemsandOperationalResearch (2024),1–19.
[112] AliNarin.2024.EvolutionaryRewardDesignandOptimizationwithMultimodalLargeLanguageModels.InProceedings
ofthe3rdWorkshoponAdvancesinLanguageandVisionResearch(ALVR).202–208.
[113] MuhammadUNasir,SamEarle,JulianTogelius,StevenJames,andChristopherCleghorn.2023. LLMatic:Neural
ArchitectureSearchviaLargeLanguageModelsandQuality-DiversityOptimization. arXivpreprintarXiv:2306.01102
(2023).
[114] BoNiandMarkusJBuehler.2024. MechAgents:Largelanguagemodelmulti-agentcollaborationscansolvemechanics
problems,generatenewdata,andintegrateknowledge. ExtremeMechanicsLetters67(2024),102131.
[115] AllenNie,Ching-AnCheng,AndreyKolobov,andAdithSwaminathan.2024. TheImportanceofDirectionalFeedback
forLLM-basedOptimizers. arXivpreprintarXiv:2405.16434 (2024).
[116] OpenAI.2024. IntroducingOpenAIo1-preview.
[117] Una-MayO’ReillyandErikHemberg.2024. UsingLargeLanguageModelsforEvolutionarySearch.InProceedingsof
theGeneticandEvolutionaryComputationConferenceCompanion.973–983.
[118] Vishal Pallagani, Bharath Chandra Muppasani, Kaushik Roy, Francesco Fabiano, Andrea Loreggia, Keerthiram
Murugesan,BiplavSrivastava,FrancescaRossi,LiorHoresh,andAmitSheth.2024. Ontheprospectsofincorporating
large language models (llms) in automated planning and scheduling (aps). In Proceedings of the International
ConferenceonAutomatedPlanningandScheduling,Vol.34.432–444.
[119] Haining Pan, Nayantara Mudur, Will Taranto, Maria Tikhanovskaya, Subhashini Venugopalan, Yasaman Bahri,
MichaelPBrenner,andEun-AhKim.2024. QuantumMany-BodyPhysicsCalculationswithLargeLanguageModels.
arXivpreprintarXiv:2403.03154 (2024).
[120] TaeJinPark,KunalDhawan,NithinKoluguri,andJagadeeshBalam.2024. Enhancingspeakerdiarizationwithlarge
languagemodels:Acontextualbeamsearchapproach.InICASSP 2024-2024 IEEE International Conference on
Acoustics,SpeechandSignalProcessing(ICASSP).IEEE,10861–10865.
[121] ArchikiPrasad,PeterHase,XiangZhou,andMohitBansal.2022. Grips:Gradient-free,edit-basedinstructionsearch
forpromptinglargelanguagemodels. arXivpreprintarXiv:2203.07281 (2022).
[122] ReidPryzant,DanIter,JerryLi,YinTatLee,ChenguangZhu,andMichaelZeng.2023.Automaticpromptoptimization
with"gradientdescent"andbeamsearch. arXivpreprintarXiv:2305.03495 (2023).
[123] Justin K Pugh, Lisa B Soros, and Kenneth O Stanley. 2016. Quality diversity: A new frontier for evolutionary
computation. FrontiersinRoboticsandAI 3(2016),202845.
[124] RindranirinaRamamonjison,TimothyYu,RaymondLi,HaleyLi,GiuseppeCarenini,BissanGhaddar,ShiqiHe,Mahdi
Mostajabdaveh,AminBanitalebi-Dehkordi,ZiruiZhou,etal.2023. Nl4optcompetition:Formulatingoptimization
problemsbasedontheirnaturallanguagedescriptions.InNeurIPS2022CompetitionTrack.PMLR,189–203.
[125] Mayk Caldas Ramos, Shane S Michtavy, Marc D Porosoff, and Andrew D White. 2023. Bayesian optimization of
catalystswithin-contextlearning. arXivpreprintarXiv:2304.05341 (2023).
32

<!-- Page 33 -->

[126] BojanaRankovićandPhilippeSchwaller.2023.BoChemian:LargelanguagemodelembeddingsforBayesianoptimization
ofchemicalreactions.InNeurIPS 2023 Workshop on Adaptive Experimental Design and Active Learning in the
RealWorld.
[127] Thiago Rios, Felix Lanfermann, and Stefan Menzel. 2024. Large language model-assisted surrogate modelling for
engineeringoptimization.In2024IEEEConferenceonArtificialIntelligence(CAI).IEEE,796–803.
[128] BernardinoRomera-Paredes,MohammadaminBarekatain,AlexanderNovikov,MatejBalog,MPawanKumar,Emilien
Dupont,FranciscoJRRuiz,JordanSEllenberg,PengmingWang,OmarFawzi,etal.2024. Mathematicaldiscoveries
fromprogramsearchwithlargelanguagemodels. Nature625,7995(2024),468–475.
[129] Emily F Ruff, Jeanne L Franz, and Joseph K West. 2024. Using ChatGPT for Method Development and Green
ChemistryEducationinUpper-LevelLaboratoryCourses. JournalofChemicalEducation101,8(2024),3224–3232.
[130] PranabSahoo,AyushKumarSingh,SriparnaSaha,VinijaJain,SamratMondal,andAmanChadha.2024.Asystematic
surveyofpromptengineeringinlargelanguagemodels:Techniquesandapplications. arXivpreprintarXiv:2402.07927
(2024).
[131] CamiloChacónSartori,ChristianBlum,FilippoBistaffa,andGuillemRodríguezCorominas.2024. Metaheuristicsand
LargeLanguageModelsJoinForces:TowardsanIntegratedOptimizationApproach. arXivpreprintarXiv:2405.18272
(2024).
[132] IvanSekulić,MohammadAlinannejadi,andFabioCrestani.2024. Analysingutterancesinllm-basedusersimulation
forconversationalsearch. ACMTransactionsonIntelligentSystemsandTechnology15,3(2024),1–22.
[133] DhruvShah,MichaelRobertEqui,BłażejOsiński,FeiXia,BrianIchter,andSergeyLevine.2023. Navigationwith
largelanguagemodels:Semanticguessworkasaheuristicforplanning.InConference on Robot Learning.PMLR,
2683–2699.
[134] Yiqing Shen, Zan Chen, Michail Mamalakis, Yungeng Liu, Tianbin Li, Yanzhou Su, Junjun He, Pietro Liò, and
YuGuangWang.2024. TourSynbio:AMulti-ModalLargeModelandAgentFrameworktoBridgeTextandProtein
SequencesforProteinEngineering. arXivpreprintarXiv:2408.15299 (2024).
[135] ParshinShojaee,KazemMeidani,ShashankGupta,AmirBaratiFarimani,andChandanKReddy.2024. LLM-SR:
Scientific Equation Discovery via Programming with Large Language Models. arXiv preprint arXiv:2404.18400
(2024).
[136] GauravSinghandKaviteshKumarBali.2024. EnhancingDecision-MakinginOptimizationthroughLLM-Assisted
Inference:ANeuralNetworksPerspective. arXivpreprintarXiv:2405.07212 (2024).
[137] IshikaSingh,ValtsBlukis,ArsalanMousavian,AnkitGoyal,DanfeiXu,JonathanTremblay,DieterFox,JesseThomason,
andAnimeshGarg.2023. ProgPrompt:GeneratingSituatedRobotTaskPlansusingLargeLanguageModels.InIEEE
InternationalConferenceonRoboticsandAutomation,ICRA.IEEE.
[138] Eduardo Soares, Vidushi Sharma, Emilio Vital Brazil, Young-Hye Na, and Renato Cerqueira. 2024. Capturing
FormulationDesignofBatteryElectrolyteswithChemicalLargeLanguageModel. (2024).
[139] ChuannengSun,SongjunHuang,andDarioPompili.2024. LLM-basedMulti-AgentReinforcementLearning:Current
andFutureDirections. arXivpreprintarXiv:2405.11106 (2024).
[140] YiwenSun,XianyinZhang,ShiyuHuang,ShaoweiCai,Bing-ZhenZhang,andKeWei.2024. AutoSAT:Automatically
OptimizeSATSolversviaLargeLanguageModels. arXivpreprintarXiv:2402.10705 (2024).
[141] Mirac Suzgun, Nathan Scales, Nathanael Schärli, Sebastian Gehrmann, Yi Tay, Hyung Won Chung, Aakanksha
Chowdhery,QuocVLe,EdHChi,DennyZhou,etal.2022. Challengingbig-benchtasksandwhetherchain-of-thought
cansolvethem. arXivpreprintarXiv:2210.09261 (2022).
[142] KeTangandXinYao.2024. LearntoOptimize-ABriefOverview. NationalScienceReview(2024),nwae132.
[143] XinyuTang,XiaoleiWang,WayneXinZhao,SiyuanLu,YaliangLi,andJi-RongWen.2024. UnleashingthePotential
ofLargeLanguageModelsasPromptOptimizers:AnAnalogicalAnalysiswithGradient-basedModelOptimizers.
arXivpreprintarXiv:2402.17564 (2024).
[144] YihongTang,ZhaokaiWang,AoQu,YihaoYan,KebingHou,DingyiZhuang,XiaotongGuo,JinhuaZhao,ZhanZhao,
andWeiMa.2024. SynergizingSpatialOptimizationwithLargeLanguageModelsforOpen-DomainUrbanItinerary
Planning. arXivpreprintarXiv:2402.07204 (2024).
[145] ZhengyangTang,ChenyuHuang,XinZheng,ShixiHu,ZizhuoWang,DongdongGe,andBenyouWang.2024. ORLM:
TrainingLargeLanguageModelsforOptimizationModeling. arXivpreprintarXiv:2405.17743 (2024).
[146] YvesGaetanNanaTeukam,FedericoZipoli,TeodoroLaino,EmanueleCriscuolo,FrancescaGrisoni,andMatteoManica.

## IntegratingGeneticAlgorithmsandLanguageModelsforEnhancedEnzymeDesign. (2024).

[147] ThanhVTTranandTruongSonHy.2024. Proteindesignbydirectedevolutionguidedbylargelanguagemodels.
IEEETransactionsonEvolutionaryComputation (2024).
[148] Uber.2020. Uber/bayesmark:Benchmarkframeworktoeasilycomparebayesianoptimizationmethodsonrealmachine
learningtasks.
33

<!-- Page 34 -->

[149] Karthik Valmeekam, Matthew Marquez, Alberto Olmo, Sarath Sreedharan, and Subbarao Kambhampati. 2024.
Planbench:Anextensiblebenchmarkforevaluatinglargelanguagemodelsonplanningandreasoningaboutchange.
AdvancesinNeuralInformationProcessingSystems36(2024).
[150] NikivanSteinandThomasBäck.2024. LLaMEA:ALargeLanguageModelEvolutionaryAlgorithmforAutomatically
GeneratingMetaheuristics. arXivpreprintarXiv:2405.20132 (2024).
[151] PetarVeličković,AdriàPuigdomènechBadia,DavidBudden,RazvanPascanu,AndreaBanino,MishaDashevskiy,
RaiaHadsell,andCharlesBlundell.2022. TheCLRSalgorithmicreasoningbenchmark.InInternationalConference
onMachineLearning.PMLR,22084–22102.
[152] HanchenWang,TianfanFu,YuanqiDu,WenhaoGao,KexinHuang,ZimingLiu,PayalChandak,ShengchaoLiu,
PeterVanKatwyk,AndreeaDeac,etal.2023. Scientificdiscoveryintheageofartificialintelligence. Nature620,7972
(2023),47–60.
[153] LudiWang,XueqingChen,YiDu,YuanchunZhou,YangGao,andWenjuanCui.2024. CataLM:EmpoweringCatalyst
DesignThroughLargeLanguageModels. arXivpreprintarXiv:2405.17440 (2024).
[154] LeiWang,ChenMa,XueyangFeng,ZeyuZhang,HaoYang,JingsenZhang,ZhiyuanChen,JiakaiTang,XuChen,
YankaiLin,etal.2024. Asurveyonlargelanguagemodelbasedautonomousagents. FrontiersofComputerScience
18,6(2024),186345.
[155] ShuaiWang,ShengyaoZhuang,BevanKoopman,andGuidoZuccon.2024. ReSLLM:LargeLanguageModelsare
StrongResourceSelectorsforFederatedSearch. arXivpreprintarXiv:2401.17645 (2024).
[156] Xinyuan Wang, Chenxi Li, Zhen Wang, Fan Bai, Haotian Luo, Jiayou Zhang, Nebojsa Jojic, Eric P. Xing, and
ZhitingHu.2023. PromptAgent:StrategicPlanningwithLanguageModelsEnablesExpert-levelPromptOptimization.
arXiv:2310.16427[cs.CL]
[157] XuezhiWangandDennyZhou.2024.Chain-of-thoughtreasoningwithoutprompting.arXivpreprintarXiv:2402.10200
(2024).
[158] Zeyi Wang, Songbai Liu, Jianyong Chen, and Kay Chen Tan. 2024. Large Language Model-Aided Evolutionary
SearchforConstrainedMultiobjectiveOptimization.InInternationalConferenceonIntelligentComputing.Springer,
218–230.
[159] SegevWasserkrug,LeonardBoussioux,DickdenHertog,FarzanehMirzazadeh,IlkerBirbil,JannisKurtz,andDonato
Maragno. 2024. From Large Language Models and Optimization to Decision Optimization CoPilot: A Research
Manifesto. arXivpreprintarXiv:2402.16269 (2024).
[160] MelvinWong,JiaoLiu,ThiagoRios,StefanMenzel,andYewSoonOng.2024. LLM2FEA:DiscoverNovelDesigns
withGenerativeEvolutionaryMultitasking. arXivpreprintarXiv:2406.14917 (2024).
[161] MelvinWong,ThiagoRios,StefanMenzel,andYewSoonOng.2024.GenerativeAI-basedPromptEvolutionEngineering
DesignOptimizationWithVision-LanguageModel. arXivpreprintarXiv:2406.09143 (2024).
[162] LikangWu,ZhiZheng,ZhaopengQiu,HaoWang,HongchaoGu,TingjiaShen,ChuanQin,ChenZhu,HengshuZhu,
QiLiu,etal.2024. Asurveyonlargelanguagemodelsforrecommendation. WorldWideWeb27,5(2024),60.
[163] XingyuWu,Sheng-haoWu,JibinWu,LiangFeng,andKayChenTan.2024. EvolutionaryComputationintheEraof
LargeLanguageModel:SurveyandRoadmap. arXivpreprintarXiv:2401.10034 (2024).
[164] Xingyu Wu, Yan Zhong, Jibin Wu, Bingbing Jiang, Kay Chen Tan, et al. 2024. Large language model-enhanced
algorithm selection: towards comprehensive algorithm representation. International Joint Conference on Artificial
Intelligence.
[165] ZhihengXi,WenxiangChen,XinGuo,WeiHe,YiwenDing,BoyangHong,MingZhang,JunzheWang,SenjieJin,
Enyu Zhou, et al. 2023. The rise and potential of large language model based agents: A survey. arXiv preprint
arXiv:2309.07864 (2023).
[166] Jian Xie, Kai Zhang, Jiangjie Chen, Tinghui Zhu, Renze Lou, Yuandong Tian, Yanghua Xiao, and Yu Su. 2024.
Travelplanner:Abenchmarkforreal-worldplanningwithlanguageagents. arXivpreprintarXiv:2402.01622 (2024).
[167] ChengrunYang,XuezhiWang,YifengLu,HanxiaoLiu,QuocVLe,DennyZhou,andXinyunChen.2024. Large
LanguageModelsasOptimizers.InTheTwelfthInternationalConferenceonLearningRepresentations.
[168] HengYangandKeLi.2023. Instoptima:Evolutionarymulti-objectiveinstructionoptimizationvialargelanguage
model-basedinstructionoperators. arXivpreprintarXiv:2310.17630 (2023).
[169] ZonglinYang,XinyaDu,JunxianLi,JieZheng,SoujanyaPoria,andErikCambria.2023. Largelanguagemodelsfor
automatedopen-domainscientifichypothesesdiscovery. arXivpreprintarXiv:2309.02726 (2023).
[170] Shunyu Yao, Fei Liu, Xi Lin, Zhichao Lu, Zhenkun Wang, and Qingfu Zhang. 2024. Multi-objective Evolution of
HeuristicUsingLargeLanguageModel. arXivpreprintarXiv:2409.16867 (2024).
[171] Yiming Yao, Fei Liu, Ji Cheng, and Qingfu Zhang. 2024. Evolve Cost-aware Acquisition Functions Using Large
LanguageModels. arXivpreprintarXiv:2404.16906 (2024).
34

<!-- Page 35 -->

[172] Wang Yatong, Pei Yuchen, and Zhao Yuqi. 2024. TS-EoH: An Edge Server Task Scheduling Algorithm Based on
EvolutionofHeuristic. arXivpreprintarXiv:2409.09063 (2024).
[173] Gavin Ye. 2024. De novo drug design as GPT language modeling: large chemistry models with supervised and
reinforcementlearning. JournalofComputer-AidedMolecularDesign 38,1(2024),20.
[174] GeyanYe,XibaoCai,HoutimLai,XingWang,JunhongHuang,LongyueWang,WeiLiu,andXiangxiangZeng.2023.
Drugassist:Alargelanguagemodelformoleculeoptimization. arXivpreprintarXiv:2401.10334 (2023).
[175] HaoranYe,JiaruiWang,ZhiguangCao,FedericoBerto,ChuanboHua,HaeyeonKim,JinkyooPark,andGuojieSong.

## Largelanguagemodelsashyper-heuristicsforcombinatorialoptimization. arXivpreprintarXiv:2402.01145

(2024).
[176] HaoranYe,JiaruiWang,ZhiguangCao,andGuojieSong.2024. ReEvo:LargeLanguageModelsasHyper-Heuristics
withReflectiveEvolution. arXivpreprintarXiv:2402.01145 (2024).
[177] WenhaoYu,NimrodGileadi,ChuyuanFu,SeanKirmani,Kuang-HueiLee,MontseGonzalezArenas,Hao-TienLewis
Chiang,TomErez,LeonardHasenclever,JanHumplik,etal.2023. Languagetorewardsforroboticskillsynthesis.
arXivpreprintarXiv:2306.08647 (2023).
[178] JunhuaZeng,ChaoLi,ZhunSun,QibinZhao,andGuoxuZhou.2024. tnGPS:DiscoveringUnknownTensorNetwork
StructureSearchAlgorithmsviaLargeLanguageModels(LLMs).InForty-firstInternationalConferenceonMachine
Learning,ICML.
[179] HanZhang,AkramBinSediq,AliAfana,andMelikeErol-Kantarci.2024.LargeLanguageModelsinWirelessApplication
Design:In-ContextLearning-enhancedAutomaticNetworkIntrusionDetection. arXiv preprint arXiv:2405.11002
(2024).
[180] HuanZhang,YuSong,ZiyuHou,SantiagoMiret,andBangLiu.2024. HoneyComb:AFlexibleLLM-BasedAgent
SystemforMaterialsScience. arXivpreprintarXiv:2409.00135 (2024).
[181] MichaelRZhang,NishkritDesai,JuhanBae,JonathanLorraine,andJimmyBa.2023. Usinglargelanguagemodels
forhyperparameteroptimization.InNeurIPS2023FoundationModelsforDecisionMakingWorkshop.
[182] RuohongZhang,LiangkeGui,ZhiqingSun,YihaoFeng,KeyangXu,YuanhanZhang,DiFu,ChunyuanLi,Alexander
Hauptmann, Yonatan Bisk, et al. 2024. Direct Preference Optimization of Video Large Multimodal Models from
LanguageModelReward. arXivpreprintarXiv:2404.01258 (2024).
[183] RuiZhang,FeiLiu,XiLin,ZhenkunWang,ZhichaoLu,andQingfuZhang.2024. UnderstandingtheImportanceof
EvolutionarySearchinAutomatedHeuristicDesignwithLargeLanguageModels.InInternationalConferenceon
ParallelProblemSolvingfromNature.Springer,185–202.
[184] Rui Zhang, Yixin Su, Bayu Distiawan Trisedya, Xiaoyan Zhao, Min Yang, Hong Cheng, and Jianzhong Qi. 2024.
AutoAlign:FullyAutomaticandEffectiveKnowledgeGraphAlignmentEnabledbyLargeLanguageModels. IEEE
Trans.Knowl.DataEng.(2024).
[185] ShenaoZhang,SiruiZheng,ShuqiKe,ZhihanLiu,WanxinJin,JianboYuan,YingxiangYang,HongxiaYang,and
ZhaoranWang.2024. HowCanLLMGuideRL?AValue-BasedApproach. arXivpreprintarXiv:2402.16181 (2024).
[186] YuZhang,KefengZheng,FeiLiu,QingfuZhang,andZhenkunWang.2024. AutoTurb:UsingLargeLanguageModels
forAutomaticAlgebraicModelDiscoveryofTurbulenceClosure. arXivpreprintarXiv:2410.10657 (2024).
[187] HuaqinZhao,ZhengliangLiu,ZihaoWu,YiweiLi,TianzeYang,PengShu,ShaochenXu,HaixingDai,LinZhao,
GengchenMai,etal.2024. Revolutionizingfinancewithllms:Anoverviewofapplicationsandinsights. arXivpreprint
arXiv:2401.11641 (2024).
[188] WayneXinZhao,KunZhou,JunyiLi,TianyiTang,XiaoleiWang,YupengHou,YingqianMin,BeichenZhang,Junjie
Zhang,ZicanDong,etal.2023. Asurveyoflargelanguagemodels. arXivpreprintarXiv:2303.18223 (2023).
[189] RuizheZhong,XingboDu,ShixiongKai,ZhentaoTang,SiyuanXu,Hui-LingZhen,JianyeHao,QiangXu,Mingxuan
Yuan,andJunchiYan.2023. Llm4eda:Emergingprogressinlargelanguagemodelsforelectronicdesignautomation.
arXivpreprintarXiv:2401.12224 (2023).
[190] HaoZhou,ChengmingHu,andXueLiu.2024. AnOverviewofMachineLearning-EnabledOptimizationforReconfigurableIntelligentSurfaces-Aided6GNetworks:FromReinforcementLearningtoLargeLanguageModels. arXiv
preprintarXiv:2405.17439 (2024).
[191] Xun Zhou, Liang Feng, Xingyu Wu, Zhichao Lu, and Kay Chen Tan. 2024. Design Principle Transfer in Neural
ArchitectureSearchviaLargeLanguageModels. arXivpreprintarXiv:2408.11330 (2024).
[192] YongchaoZhou,AndreiIoanMuresanu,ZiwenHan,KeiranPaster,SilviuPitis,HarrisChan,andJimmyBa.2022.
Largelanguagemodelsarehuman-levelpromptengineers. arXivpreprintarXiv:2211.01910 (2022).
[193] Max Zhu, Adrián Bazaga, and Pietro Liò. 2024. FLUID-LLM: Learning Computational Fluid Dynamics with
Spatiotemporal-awareLargeLanguageModels. arXivpreprintarXiv:2406.04501 (2024).
[194] MingchenZhuge,WenyiWang,LouisKirsch,FrancescoFaccio,DmitriiKhizbullin,andJürgenSchmidhuber.2024.
GPTSwarm:LanguageAgentsasOptimizableGraphs.InForty-firstInternationalConferenceonMachineLearning.
35

## Tables

**Table (Page 5):**

|  ' D W D  3 R L Q W V  3 R O \ Q R P L D O  ) L W  0 R Q W K O \  & R X Q W V |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |


**Table (Page 5):**

|  |  |  |  |   |           |     |     |
|---|---|---|---|---|---|---|---|
|  |  |  |     |                 |  |  |  |


**Table (Page 9):**

|  |  |  |  |
|---|---|---|---|
| Algorithm | Algorithm |  |  |
|  |  |  |  |


**Table (Page 10):**

|  |  |  |  |
|---|---|---|---|
| Algorithm | Algorithm |  |  |
|  |  |  |  |


**Table (Page 15):**

|  V Q R L W D F L O E X 3  I R  U H E P X 1 |  |
|---|---|
|  |  V Q R L W D F L O E X 3  I R  U H E P X 1 |


**Table (Page 19):**

| Method | RoleofLLM | PromptStrategy |
|---|---|---|
| AEL[87] | LLMaD | FS,CoT |
| ReEvo[176] | LLMaD | CoT,RF |
| OPRO[167] | LLMaO | FS |
| LMEA[91] | Mixed | FS |
| MLLM[68] | Mixed | ZS,FS |
| FunSearch[128] | LLMaD | FS |
| EoH[88] | LLMaD | FS,OS,CoT |
| MH-LLM*[131] | LLMaD | ZS,FS |
| LLaMEA[150] | LLMaD | CoT |
| EvoLLM[77] | LLMaO | FS |
| OPRO[167] | LLMaO | FS |
| LEO[14] | LLMaO | FS |
| LAEA[56] | LLMaP | FS,CoT |
| MOEA/D-LMO[86] | LLMaO | FS |
| LLM-MOEA*[136] | LLMaE | ZS |
| CMOEA-LLM[158] | LLMaO | FS |
| HPO-LLM*[181] | LLMaO | FS |
| LLAMBO[93] | Mixed | FS,ZS,CoT |
| BO-LIFT*[125] | LLMaD | FS |
| EvolCAF[171] | LLMaD | FS,OS,CoT |
| FunBO[1] | LLMaD | FS |
| APE[192] | LLMaO | FS |
| OPRO[167] | LLMaO | FS |
| APO[122] | LLMaO | ZS,FS |
| GPO[143] | LLMaO | FS |
| MaaO[52] | LLMaO | FS |
| EvoPrompt[50] | LLMaO | CoT,FS |
| StrategyLLM[45] | Mixed | ZS,FS,CoT |
| DOCP[159] | LLMaO | FS,CoT |
| OptiMUS[2] | Mixed | ZS,FS |
| ORLMs[145] | LLMaD | ZS |
| LM4OPT[3] | LLMaD | FS,ZS |
| AS-LLM[164] | LLMaE | ZS |
| LLaMoCo[101] | LLMaD | FS |


**Table (Page 21):**

| Method | RoleofLLM | PromptStrategy |
|---|---|---|
| Zero-Planner[65] | LLMaP | ZS,FS |
| SayCan[5] | LLMaP | FS |
| LLM-GM[66] | LLMaP | FS |
| Text2Motion[84] | LLMaP | FS |
| ProgPrompt[137] | LLMaD | FS,COT |
| SayCanPay[57] | LLMaP | FS |
| LFG[133] | LLMaP | FS,CoT |
| SLINVIT[185] | LLMaP | ZS,FS |
| MEDIC[12] | LLMaP | ZS |
| Eureka[100] | LLMaD | FS,CoT |
| EROM[112] | LLMaD | ZS,CoT |
| LLM-MOE[32] | LLMaP | FS,CoT |
| EvoPrompting[19] | LLMaD | FS,ZS,CoT |
| HS-NAS[70] | LLMaP | FS,ZS,CoT |
| LLMatic[113] | LLMaD | FS,ZS,CoT |
| LAPT[191] | LLMaD | ZS,FS |
| LLM-GE[110] | LLMaD | FS,ZS,CoT |
| LLM-Critical[104] | LLMaD | FS,ZS,CoT |
| LLM-GNN[23] | LLMaP | FS,CoT |
| ReStruct[21] | LLMaE | FS,ZS |
| AutoAlign[184] | LLMaE | FS,ZS |
| KSL[41] | LLMaP | FS |
| Inter-Classier[24] | LLMaO | FS,ZS |
| DataSculpt[48] | LLMaP | FS |
| LLM2FEA[160] | LLMaP | FS,CoT |
| tnGPS[178] | LLMaD | FS,OS,CoT |
| L-AutoDA[49] | LLMaD | FS,OS,CoT |


**Table (Page 23):**

| Method | RoleofLLM |
|---|---|
| Bilevel[98] | LLMaD |
| LLM-SR[135] | LLMaD |
| LLM4ED[34] | LLMaD |
| ChatChemTS[69] | LLMaD |
| DebjyotiBhattacharya,etal.[13] | LLMaO |
| AgustinusKristiadi,etal.[76] | LLMaE |
| BoChemian[126] | LLMaE |
| Multi-modalMoLFormer[138] | LLMaP |
| CataLM[153] | LLMaP |
| GavinYe[173] | LLMaD |
| DrugAssist[174] | LLMaO |
| MLDE[147] | LLMaP |
| Prollama[97] | Mixed |
| X-LoRA[16] | LLMaP |
| CodonBERT[82] | LLMaP |
| Revisiting-PLMs[62] | LLMaP |
| FLUID-LLM[193] | LLMaP |
| MechAgents[114] | LLMaD |
| MeLM[17] | LLMaP,LLMaD |
| MenggeDu,etal.[33] | LLMaD |
| AutoTurb[186] | LLMaD |
