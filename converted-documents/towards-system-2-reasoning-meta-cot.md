---
title: "Towards System 2 Reasoning Meta CoT"
original_file: "./Towards_System_2_Reasoning_Meta_CoT.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["prompt-engineering", "llm", "rag", "chain-of-thought", "agents"]
keywords: ["model", "search", "reasoning", "training", "models", "thought", "but", "roots", "page", "meta"]
summary: "<!-- Page 1 -->

Towards System 2 Reasoning in LLMs:
Learning How to Think With Meta

### Chain-of-Thought

VioletXiang2,CharlieSnell3,KanishkGandhi2,AlonAlbalak1,AnikaitSingh2,ChaseBlagden1,DuyPhung1,
RafaelRafailov2,1,NathanLile1,DakotaMahan1,LouisCastricato1,Jan-PhilippFränken2,NickHaber2 and

### ChelseaFinn2

1SynthLabs.ai,2StanfordUniversity,3UCBerkeley
We propose a novel framework, Meta Chain-of-Thought (Meta-CoT), which extends traditional Chain-of-
Thought (CoT) by explicitly modeling t"
related_documents: []
---

# Towards System 2 Reasoning Meta CoT

<!-- Page 1 -->

Towards System 2 Reasoning in LLMs:
Learning How to Think With Meta

### Chain-of-Thought

VioletXiang2,CharlieSnell3,KanishkGandhi2,AlonAlbalak1,AnikaitSingh2,ChaseBlagden1,DuyPhung1,
RafaelRafailov2,1,NathanLile1,DakotaMahan1,LouisCastricato1,Jan-PhilippFränken2,NickHaber2 and

### ChelseaFinn2

1SynthLabs.ai,2StanfordUniversity,3UCBerkeley
We propose a novel framework, Meta Chain-of-Thought (Meta-CoT), which extends traditional Chain-of-
Thought (CoT) by explicitly modeling the underlying reasoning required to arrive at a particular CoT. We
presentempiricalevidencefromstate-of-the-artmodelsexhibitingbehaviorsconsistentwithin-contextsearch,
andexploremethodsforproducingMeta-CoTviaprocesssupervision,syntheticdatageneration,andsearch
algorithms. Finally,weoutlineaconcretepipelinefortrainingamodeltoproduceMeta-CoTs,incorporating
instructiontuningwithlinearizedsearchtracesandreinforcementlearningpost-training. Finally,wediscuss
openresearchquestions,includingscalinglaws,verifierroles,andthepotentialfordiscoveringnovelreasoning
algorithms. ThisworkprovidesatheoreticalandpracticalroadmaptoenableMeta-CoTinLLMs,pavingthe
wayformorepowerfulandhuman-likereasoninginartificialintelligence.

### Give a man a fish and you feed him for a day;

teach a man to fish and you feed him for a lifetime.
-Proverb

### Contents

1 Introduction 4
1.1 Motivation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
1.2 Outline . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
2 Meta Chain-Of-Thought 6
2.1 Deriving The Meta-CoT Process . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
2.2 Why Does (Classical) CoT Fail? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
3 Towards Deliberate Reasoning With Language Models - Search 9
3.1 Inference-Time Compute: Search . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
3.2 Inference-Time Compute: Verification . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
Authorsareorderedrandomly.Correspondencetoteam@synthlabs.ai.
5202
naJ
8
]IA.sc[
1v28640.1052:viXra

<!-- Page 2 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought
3.3 From Best-of-N To General Search . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
3.4 Is Search (Inference Time Compute) A Fundamental Capability Shift? . . . . . . . . . 14
4 Towards Meta-CoT Reasoning 15
4.1 Bootstrapping Meta-CoT . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
4.1.1 Self-Taught Reasoner . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
4.1.2 Meta-STaR . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
4.2 Empirical Examples Of Internalizing Search . . . . . . . . . . . . . . . . . . . . . . . 16
4.2.1 Small-Scale Empirical Results on Internalizing Search . . . . . . . . . . . . . . 16
4.2.2 In-context Exploration For LLMs . . . . . . . . . . . . . . . . . . . . . . . . . . 19
4.2.3 Using variable Compute . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
4.2.4 Backtracking in LLMs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
4.3 Synthetic Meta-CoT Via Search . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
4.3.1 Monte-Carlo Tree Search . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
4.3.2 A* search . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
4.4 Do Advanced Reasoning Systems Implement In-Context Search? . . . . . . . . . . . . 23
5 Process Supervision 26
5.1 Learning Process Reward Models . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
5.2 PRM Quality And Its Effect On Search . . . . . . . . . . . . . . . . . . . . . . . . . . 27
5.3 Verifiable Versus Open-Ended Problems . . . . . . . . . . . . . . . . . . . . . . . . . . 27
6 Meta Reinforcement Learning - Learning How To Think 28
6.1 Meta-RL In Small Domains . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
6.2 Meta-RL In Language Model Reasoning . . . . . . . . . . . . . . . . . . . . . . . . . . 32
6.3 Efficiency Or Super-Intelligence? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
6.4 Can System 2 Reasoning Emerge From Pure RL? . . . . . . . . . . . . . . . . . . . . . 35
6.4.1 Inducing Meta-Reasoning In LLMs . . . . . . . . . . . . . . . . . . . . . . . . 35
7 Putting It All Together - A Pipeline for System 2 Reasoning 39
7.1 Instruction Tuning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
7.2 Post-Training With RL . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
7.2.1 Q* or q-STaR? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
7.2.2 Discount Rates . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
2

<!-- Page 3 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought
8 Going Forward 43
8.1 The "Big MATH" Project . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 44
8.1.1 Data Sourcing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45
8.1.2 Data Filtering . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45
8.2 Infrastructure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46
8.3 Open Research Questions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47
8.3.1 Open-Ended Verification And CoT Faithfulness . . . . . . . . . . . . . . . . . . 47
8.3.2 Process Guidance And The Verifier Gap . . . . . . . . . . . . . . . . . . . . . . 48
8.3.3 Scaling Laws For Reasoning And Search . . . . . . . . . . . . . . . . . . . . . 49
8.3.4 Meta-Search/Search 2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50
8.3.5 Reasoning with External Tools . . . . . . . . . . . . . . . . . . . . . . . . . . . 50
9 Conclusion 51
10 Acknowledgments 52

### A Prompting 62


### B Regret Analysis 63

C Different Instruction Tuning Objectives 63

### D MCTS Details 63

E Chains-Of-Thought 64
3

<!-- Page 4 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought

## Introduction


### Motivation

A key aspect of the current era of Large Language Models has been the foundational principle of
next-token prediction (Elman, 1990; Jordan, 1997). That is, tokenizing text (or other continuous
modalities) into a discrete sequence in the following way:
"The quick brown fox jumps over the lazy dog." → y ,y ,...,y ,
1 2 𝑛
where y are elements of some finite vocabulary and, subsequently, train a large parameterized
𝑖
neural network 𝑝 (transformer) model with the following maximum likelihood objective:
𝜃
[︃ ]︃
∑︁
ℒ = E − log𝑝 (y |y ) .
𝜃 𝒟train 𝜃 𝑡+1 ≤𝑡
𝑡
Behind this approach is a simple principle often abbreviated as "compression is intelligence", or
the model must approximate the distribution of data and perform implicit reasoning in its activations
in order to predict the next token (see Solomonoff Induction; Solomonoff 1964). That is, language
models learn the implicit meaning in text, as opposed to the early belief some researchers held that
sequence-to-sequence models (including transformers) simply fit correlations between sequential
words.
A fundamental question, however, is: What is the relationship between the complexity of the
underlying data stream and the model’s capability to learn the data-generating algorithm? While
natural language has some irreducible entropy, this question holds even in deterministic scenarios (as
demonstrated below). Mathematical reasoning is a good domain to demonstrate and evaluate these
questions. One can ask an LLM to generate a response to questions like:
“What is 1+2?”
to which most immediately answer “3”. We can increase the complexity of the question by asking, for
example:
“What is the value of
(𝑥2−1)(𝑥+1) 1
−
𝑥3−𝑥 𝑥
evaluated at 𝑥 = 𝜋?”
This is actually a simple question since the expression is canonically equal to 1, yet even powerful
LLMs such as GPT-4o and Claude fail to answer it correctly even once. That is, the true conditional
generative process 𝑝(y |y ) could have arbitrarily high computational complexity even when it is
𝑡+1 𝑡
deterministic as in the example above. In contrast, if we instruct models to “think step by step” and
produce a chain-of-thought we can significantly improve their capabilities producing traces like the
following:
4

<!-- Page 5 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought
We are tasked with evaluating
(𝑥2−1)(𝑥+1) 1
−
𝑥3−𝑥 𝑥
at 𝑥 = 𝜋. Let us simplify the expression before substituting 𝑥 = 𝜋.

### Step 1: Simplify (𝑥2−1)(𝑥+1)

The numerator of the first term can be rewritten:
𝑥2−1 = (𝑥−1)(𝑥+1),
so
(𝑥2−1)(𝑥+1) = (𝑥−1)(𝑥+1)2.
Step 2: Simplify 𝑥3−𝑥 in the denominator

### Factorize 𝑥3−𝑥:

𝑥3−𝑥 = 𝑥(𝑥2−1) = 𝑥(𝑥−1)(𝑥+1).
Thus, the first term becomes:
(𝑥2−1)(𝑥+1) (𝑥−1)(𝑥+1)2
= .
𝑥3−𝑥 𝑥(𝑥−1)(𝑥+1)
Cancel (𝑥−1) and one factor of (𝑥+1):
(𝑥2−1)(𝑥+1) 𝑥+1
= .
𝑥3−𝑥 𝑥
Step 3: Subtract 1
𝑥
Now substitute this simplified result into the full expression:
𝑥+1 1
− .
𝑥 𝑥
Combine the terms over the common denominator 𝑥:
𝑥+1 1 𝑥+1−1 𝑥
− = = = 1.
𝑥 𝑥 𝑥 𝑥
Step 4: Evaluate at 𝑥 = 𝜋 Theexpressionsimplifiesto1,whichisindependentof𝑥. Thus,the
value at 𝑥 = 𝜋 is:
1 .
There have been multiple explanations for this phenomenon (Merrill & Sabharwal, 2023; Prystawski
et al., 2024; Ye et al., 2024a; Dutta et al., 2024), however we focus on the complexity hypothesis (Merrill & Sabharwal, 2023). Specifically, a CoT expansion allows for (in-theory) arbitrarily large
amounts of compute to be deployed towards the prediction of answer tokens. A large theoretical
literature has been developed arguing for the representational complexity of transformers with and
withoutCoT(Merrill&Sabharwal,2023;Nowaketal.,2024;Lietal.,2024). Theliteraturesaysthat
endowing LLMs with CoT allows them to represent new orders of complexity and (with assumptions,
such as infinite memory) may even make them Turing complete. However, in practice, today’s LLMs
can only reliably solve problems of limited complexity (Snell et al., 2024).
5

<!-- Page 6 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought

### Outline

In this paper, we investigate the limitations of current LLMs in handling complex reasoning tasks and
propose a novel framework, Meta Chain-of-Thought (Meta-CoT), to address these shortcomings. We
argue that traditional Chain-of-Thought (CoT) methods, while effective for simpler problems, fail
to capture the true data-generating process of complex reasoning which often involves a non-linear,
iterative, and latent process of exploration and verification. Meta-CoT extends CoT by explicitly
modeling this latent “thinking” process, which we hypothesize is essential for solving problems that
require advanced reasoning capabilities.
We draw inspiration from Cognitive Science’s dual-process theory, framing Meta-CoT as a form of
System 2 reasoning. We establish the theoretical foundations of Meta-CoT, demonstrating how it can
be realized through systematic search processes, and how these processes can be internalized within
a single auto-regressive model. We then present empirical evidence supporting our claims, including
analyses on state-of-the-art models like OpenAI’s o1 (OpenAI, 2024) and DeepSeek-R1 (DeepSeek,
2024), which exhibit behaviors consistent with internalized (in-context) search. We further explore
methodsfortrainingmodelsonMeta-CoTthroughprocesssupervision,andsyntheticdatageneration
via search algorithms like Monte Carlo Tree Search (MCTS) and A*.
Finally, we outline a concrete pipeline for achieving Meta-CoT in a single end-to-end system,
incorporating instruction tuning with linearized search traces and reinforcement learning (RL) posttraining. We discuss open research questions, including the scaling laws of reasoning and search, the
roleofverifiers,andthepotentialfordiscoveringnovelreasoningalgorithmsthroughmeta-RL.Wealso
present the “Big MATH” project, an effort to aggregate over 1,000,000 high-quality, verifiable math
problems to facilitate further research in this area. Our work provides both theoretical insights and a
practical road map to enable Meta-CoT in LLMs, paving the way for more powerful and human-like
reasoning in artificial intelligence.

## Meta Chain-Of-Thought

In this section, we first formulate the meta chain-of-thought process and discuss how it can describe
the problem solving process for complex reasoning problems. Then, we describe and demonstrate
why classical chain-of-thought fails under certain circumstances.

### Deriving The Meta-CoT Process

A question to ask ourselves is: Should language models with Chain-Of-Thought prompting really be
able to express any function, and thus solve arbitrarily complex problems, which was the theoretical
pointoftheprevioussection? Wewillstickwiththemathematicalreasoningdomainforthepurposeof
the discussion. Today, the capabilities of frontier models are enough for a large class of mathematical
reasoning problems. Current state-of-the art systems such as GPT-4o and Claude largely solve the
Hendrycks MATH Levels 1-3 Benchmark (Hendrycks et al., 2021), however, they still struggle with
advanced problems such as those in Levels 4 and 5, HARP (Yue et al., 2024) and Omni-MATH (Gao
et al., 2024) (as well as other advanced reasoning tasks). We put forward the following theory to
explain these empirical observations.
Reasoning data present in pre-training corpuses does not represent the true data generation
process, especially for complex problems, which is a product of extensive latent reasoning.
Moreover, this process generally does not occur in a left-to-right, auto-regressive, fashion.
6

<!-- Page 7 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought
In more details, the CoT reasoning data prevalent in the pre-training corpus and post-training
instruction tuning follows the true data-generating process for solutions of simple problems such as
algebraic computations, counting, basic geometry etc.. That is, for example, the textbook solutions
forsolvinghigh-school algebrapresent thegeneral processofgeneratingthose solutions. Ifwefollow
somesetofstepsorapproachespresentinexistingtextbooks,wecaneventuallyarriveatthesolution.
Hence,thesearelearnablewithaconstant-depthtransformersthatcanexpressthecomplexityofeach
individual step in the process. In contrast, complex reasoning problems do not follow that pattern.
We may have a set of triples (q,S,a) of questions q, solution steps S = (s ,...,s ) and (optionally)
1 𝑛
answers a, but the true data generation process is not auto-regressive:
q → z → ... → z → (s ,...,s ,a), (1)
1 𝐾 1 𝑛
where z are the latent "thoughts" left out of the solutions steps, which can be represented fully
𝑖
with left-to-right generation, while the dataset solution S = (s ,...,s ) is generated jointly. Let
1 𝑛
us illustrate this with an example from the International Mathematics Olympiad 2011. This is the
(in)famous "windmill" problem:
“Let 𝒮 be a finite set of at least two points in the plane. Assume that no three points of 𝒮 are
collinear. A windmill is a process that starts with a line ℓ going through a single point 𝑃 ∈ 𝒮.
The line rotates clockwise about the pivot 𝑃 until the first time that the line meets some other
point belonging to 𝒮. This point, 𝑄, takes over as the new pivot, and the line now rotates
clockwise about 𝑄, until it next meets a point of 𝒮. This process continues indefinitely. Can we
choose a point 𝑃 in 𝒮 and a line ℓ going through 𝑃 such that the resulting windmill uses each
point of 𝒮 as a pivot infinitely many times.”
which has the following solution:
“Let|𝑆| = 𝑛. Nowconsideranarbitrarypoint𝑃 in𝑆 andchoosealine𝑙 through𝑃 whichsplits
the points in the plane into roughly equal chunks. Next notice that as the line rotates it will
sweep a full 2𝜋 angle against some fixed reference frame. Now take another random point
𝑃′ and similarly constructed stationary line 𝑙′. At some point in the windmill process we will
have 𝑙||𝑙′. However notice that 𝑙 and 𝑙′ split the points into the same two sets and are parallel.
Therefore we must have that 𝑙 ≡ 𝑙′ and thus 𝑙 passes through 𝑃′. This of course holds for any
𝑃′ ∈ 𝑆. Applying the same argument recursively yields the final proof that it is in fact possible
to make such a construction for any set 𝑆 with these properties.”
The solution above does not use any prior knowledge and fits within a few sentences. Yet, this
problem was considered among the most difficult in the competition (there were only a handful of
solutions among the 600+ participants). What makes the problem difficult is the highly non-linear
structure of the solution. Most participants would follow the standard "generative" solution process
andinvestigateapproachesbasedontheconvexhullconstructionorusetoolsfromHamiltoniangraph
theory, none of these leading to a solution. Instead, participants who solved the problem followed an
experimental approach with a lot of geometric exploration and inductive reasoning. Moreover, the
solution itself is not linear. It’s hard to see the utility of the proposed construction in the beginning
without the analysis of the dynamics of 𝑙. Essentially, to start generating the solution requires
that we already know the full approach. The underlying generative process of the solution is not
auto-regressive from left-to-right.
We can formalize this argument through the interpretation of reasoning as a latent variable
process (Phan et al., 2023). In particular, classical CoT can be viewed as
7

<!-- Page 8 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought
Figure 1: Top: Performance of current frontier models by size on the HARP mathematics benchmark (Yue et al., 2024) by difficulty level and topic. The OpenAI O1 series significantly out-performs
prior generation models across the board. Source: Figure 3 in (Yue et al., 2024). Bottom Average
number of tokens generated by each model grouped by difficulty level, as well as average number of
tokens in human-generated solutions (using GPT4 tokenizer). Source: Figure 4 in (Yue et al., 2024).
∫︁ 𝑛
∏︁
𝑝data(a|q) ∝ 𝑝data(a|s
1
,...,s
𝑛
,q) 𝑝data(s
𝑡
|s
<𝑡
,q)𝑑S,
⏟ ⏞
AnswerGeneration 𝑡=1
⏟ ⏞

### CoT

i.e., the probability of the final answer being produced by a marginalization over latent reasoning
chains. Weclaimthatforcomplexproblems,thetruesolutiongeneratingprocessshouldbeviewedas

## ∫︁ 𝐾

∏︁
𝑝data(a,s
1
,...,s
𝑛
|q) ∝ 𝑝data(a,s
1
,...,s
𝑛
|z
1
,...,z
𝑘
,q) 𝑝data(z
𝑡
|z
<𝑡
,q)𝑑Z,
⏟ ⏞
JointAnswer+CoT 𝑡=1
⏟ ⏞

### Meta-CoT

i.e., the joint probability distribution of the solution (a,s ,...,s ) is conditioned on the latent
1 𝑛
generative process. Notice that this argument is a meta-generalization of the prior CoT argument,
hence why we will refer to the process q → z → ... → z as Meta-CoT.

## 1 𝐾

8

<!-- Page 9 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought

### Why Does (Classical) CoT Fail?

Based on the previous discussion, a natural question follows: Why do LLMs fail at these advanced
reasoning tasks? Above we proposed that the pre-training and instruction-tuning corpora consist of
data of the type (q,s ,...,s ,a), which do not contain the true data generating process as shown in
1 n
Equation 1. Indeed, the solution to the windmill problem above is widely available on the internet,
but there is little to no discussion about the ways in which commonly used convex hull or planar
graph arguments fail. This is true in general - textbooks contain advanced proofs but not the full
thought process of deriving these proofs. We can then apply the same general meta-argument of why
CoT is necessary to the Meta-CoT case: simply because the conditional solution-level distribution
𝑝data(a,s
1
,...,s
𝑛
|q) (without the intermediate Meta-CoT) on hard reasoning questions can have
arbitrarily high complexity in the same way that 𝑝data(a|q) can have arbitrarily high complexity in
the standard CoT setting. We will examine some empirical evidence for our stance in the following
sections.
We will argue in the following chapters that the OpenAI o1 model series performs full Meta-CoT
reasoning in an auto-regressive fashion at inference time. A useful analysis is presented in a new
mathematics benchmark with challenging high-school Olympiad-level problems (Yue et al., 2024).
Figure1sourcedfromthatworkshowstherelevantresults. First,weseethattheo1familyofmodels
significantlyoutperforms“standard”reasoningmodelsacrosstheboard. However,thegapbetweeno1
andothermodels’performanceincreasesonhigherdifficultyproblems(withtheinterestingexception
of the LLaMa 3.1 models), that is, problems which have higher solution complexity.
Furthermore, the bottom half of Figure 1 shows the average number of tokens generated grouped
byproblemdifficultylevel. First,weseethatoutsideoftheo1seriesofmodels,LLMsgeneratesolutions
of comparable lengths to humans. While this may initially appear quite intriguing, suggesting that
models are learning to approximate or replicate human reasoning, the simple explanation is that
models are learning solutions to match the training data - i.e. 𝑝data(a,s
1
,...,s
𝑛
|q). Much more
intriguingly, the o1 series of models exhibits significantly different token behavior. We see that:

## On level 1 problems the o1 series generates a comparable number of tokens to human-written

solutions. These are the types of problems where the training solutions likely match the true
datagenerationprocessandeachindividuallogicalstepcanbeinternalizedinaconstant-depth
transformer.

## Athigherdifficulty,theo1seriesofmodelsgeneratessignificantlymoretokensperproblemand

also widens the performance gap over the classical reasoning models. In fact the gap between
the inference compute used by the o1 model and prior series of models seems to scale with
the complexity of the problems. We hypothesize that in those more challenging problems the
solutions do NOT in fact represent the true data generative process, which is instead better
approximated by the more extensive Meta-CoT generated by the o1 family of models.
Ofcourse,inpracticethedistinctionbetweenthesetwoisnotsoclearcut,andinfacttheconstantdepth transformer can likely internalize part of the Meta-CoT generative process as evidenced by the
gradation of (Meta-)CoT lengths from Levels 2-6 in Figure 1. In the next chapter we will discuss in
greater detail what the Meta-CoT process actually represents.

## Towards Deliberate Reasoning With Language Models - Search

In the previous section we introduced the Meta-CoT process and argued that LLMs fail on advanced
reasoningtasksbecausethetrainingdatadoesnotadequatelyrepresentthetruedatageneration
9

<!-- Page 10 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought
0.5
0.4
0.3
0.2
0 100000 200000 300000 400000 500000 600000 700000
Number of Examples
ycaruccA

## Htam

0.8
0.7
0.6
0.5
0.4
Majority@64
Majority@8
0.3

### Greedy


### Base Filter


### Original 0.2

0 100000 200000 300000 400000 500000 600000 700000
Number of Examples
ycaruccA

## Htam

Pass@2 Pass@16
Pass@4 Pass@32

### Pass@8 Pass@64

Figure 2: Train-time scaling curves for increasing quantities of training data during supervised
fine-tuning of Llama3.1 8B, when evaluating for accuracy on the MATH test set. Left: A comparison
of training on on the original data (x) and base filtered data (o) and evaluated using either greedy
or majority vote decoding. For all settings, the filtered dataset shows improved scaling, and has not
plateaued. Right: A comparison of pass@k for increasing 𝑘 with a model trained on the base filtered
dataset. The chart shows how increasing 𝑘 leads to a much greater probability of at least 1 correct
solution, even for a relatively small model. Additionally, the performance improvement from 𝑘 = 32
to64doesnotshowplateauing,suggestingthat𝑘 canfurtherbeincreasedforimprovedperformance.
process, i.e. text corpora do not include (or only include limited amounts of) Meta-CoT data. So the
remaining question is: what does the true data generating process look like?

## First, we argue that for many advanced reasoning or goal-oriented problems there exist meaningful gaps between the complexity of generation and verification. This is of course one of the

fundamental open problems of theoretical computer science and any attempt to prove this is
significantly beyond the scope of the current writing, but we will review what we believe to be
compelling empirical evidence from the literature.

## Second,assuminganon-trivialgenerator-verifiergap,wearguethatthesolutionstochallenging

problemspresentintextcorporaaretheoutcomesofanextended search process,whichitself
is not represented in the data.
We will dive deeper into these two points in the remainder of this section.

### Inference-Time Compute: Search

The first point above (generation-verification gap) has recently become a popular research and
discussion direction under the framework of “deploying inference-time compute” and we explore this
in our first experiment. We start with a LLaMa 3.1 8B base model (Dubey et al., 2024) and carry out
extensive supervised fine-tuning on the Numina MATH dataset (LI et al., 2024). Refer to Figure 2 for
resultsandSection8.1fordatasetdetails. Foreachintermediatecheckpointweevaluateperformance
on the Hendrycks MATH (Hendrycks et al., 2021) 500 problems evaluation dataset (Lightman et al.,
2023). Based on the results, we make a few observations here:

## We evaluate pass@𝑘 (i.e. using an oracle verifier) on intermediate checkpoints and see a

significant jump in performance for increasing 𝑘. While zero-shot performance with greedy
10

<!-- Page 11 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought
Figure 3: Scaling trends for verifier models on algorithmic reasoning, grade-school math (GSM8k),
and transfer from GSM8k to MATH. The performance of all verifiers improves in the best-of-N setting,
as N increases. Figure sourced from (Zhang et al., 2024a).
decoding improves from about 20% to 40% (see the base filter on the left side of Figure 2),
even the first model checkpoint outperforms these results at pass@4 (right side of Figure 2).
Moreover, the pass@64 for the final checkpoint of an 8B model achieves accuracy close to 85%,
outperforming the zero-shot performance of many current frontier models.

## Wealsoevaluateperformanceundermajorityvotingwith𝑘 = 8and𝑘 = 64. Thereiscontinuous

improvement for both increased training and samples, with maj@64 outperforming the greedy
model performance with only 15% of the training compute without access to a ground-truth
verifier.
These results demonstrate that even as we directly optimize for answer generation ability by
finetuning on increasing amounts of SFT data, there remains a consistent verifier-generator gap, as
evidenced by the improved performance in botht eh pass@k and majority voting settings. Recent
literature has observed similar results on post-training sampling (Lightman et al., 2023; Brown
et al., 2024; Snell et al., 2024). However, most of these studies do not systematically evaluate the
effects of varying amounts of training data, compute, and model size which we believe is a fruitful
direction for additional empirical work. These questions are important as the observed gains from
additional inference might disappear at larger scales and training - i.e. the model may be able to
fully internalize the reasoning process. This definitely seems to be the case for advanced models
and simpler benchmarks like GSM8k (Cobbe et al., 2021). While we observe the opposite result in
our experiments, we admit that our results are the outcomes of preliminary study and additional
work is required, but we will argue from a theoretical point in Section 6 that a persistent search gap
remains in domains with high enough epistemic uncertainty. Besides this point, the question remains
whethertheimprovementfromincreasedinferencecanbeeffectivelyachievedwithoutoracleverifiers
or environment feedback. In theory, it is possible to generate correct solutions under an increased
inference budget, but we may not be able to verify them effectively, as verification complexity may be
just as high as, or even higher than, generation complexity. We will address this issue next.

### Inference-Time Compute: Verification

Severalworksfocusontrainingverifiermodels,whichexplicitlyevaluatethecorrectnessofreasoning
steps and solutions. Verifiers can be trained either using explicit binary classification (Cobbe et al.,
2021; Lightman et al., 2023; Snell et al., 2024; Anonymous, 2024; Setlur et al., 2024b) or modeling
11

<!-- Page 12 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought
Figure 4: Reasoning via Planning (RAP) demonstrates the search procedure described here. If we
haveaccesstoastateevaluator,wecantruncatebrancheswithlowvaluesandbacktracktopromising
nodes, without resampling the same steps again. Source: Figure 2 in (Hao et al., 2023).
evaluation directly in natural language, using the LLM-as-a-judge prior (Zhang et al., 2024a; Mahan
et al., 2024). The unifying formulation of these approaches is the model 𝑣 which evaluates a
𝜃
reasoning process 𝑣 (q,S) → [0,1]. Under this framework, 𝐾 candidate solutions (S1,...,S𝐾) can
𝜃
be generated from a fixed generator 𝜋 (·|q) and ranked based on their evaluation score.
𝜃
S* = argmax{𝑣 (q,S1),...,𝑣 (q,S𝐾)}
𝜃 𝜃
For empirical results, we refer the reader to Figure 3 sourced from (Zhang et al., 2024a) which
evaluates a number of verifier models 𝑣 . Regardless of the efficiency of the verifier, there is a
𝜃
significant improvement in performance with additional online sampling. Moreover using explicitly
trainedverifiermodelsoutperformsnaiveinference-computescalingstrategiessuchasself-consistency
or majority voting.
A question remains regarding the effect of using a fixed generation model (policy): Could this
modelbeunder-trained,andifitwerefurthertrained,coulditszero-shotperformanceimprovetothe
point where additional online search no longer provides meaningful improvement? We will address
this in Section 3.4.

### From Best-of-N To General Search

Sofar,weempiricallyexploredbest-of-Napproaches,generatingmultiplefullsolutionsindependently
andselectingthemostpromisingonebasedonscores. However,thisapproachisinefficientbecauseit
requires exploring full solution paths, even if a mistake occurs early on, and may repeatedly sample
thesamecorrectsteps. Instead,wecanmodelreasoningasaMarkovDecisionProcess(MDP),defined
by the tuple ℳ = (𝒮,𝒜,𝑃,𝑅,𝛾), where:
• 𝒮: the set of states, where each state S ∈ 𝒮, consists of the prompt and generations so far, i.e.
S = (q,s ,...,s ).
𝑡 1 𝑡
• 𝒜: the set of actions, where each action a ∈ 𝒜 will be represented as the next reasoning step
a = s .
𝑡+1 𝑡+1
• 𝑃(s′ | s,a): the transition probability function, representing the probability of transitioning
to state s′ when taking action a in state s. For simplicity, we will mostly consider the deter-
12

<!-- Page 13 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought
ministictransitionfunction𝑃(·|s ,(q,s ,...,s )) → (q,s ,...,s ,s )thatappendsthenext
𝑡+1 1 𝑡 1 𝑡 𝑡+1
reasoning step to the context. In general, the environment dynamics can be more complex.
For example, models with tool access have to call the actual tool and receive the environment
feedbackincontextorevenmodifytheirenvironmentsuchasthecasesofSWEandWebagents.
• 𝑅(s,a): the reward function, which provides a scalar reward for taking action a in state s.
We will assume zero intermediate rewards and final reward of 1 for a correct solution and
zero otherwise, although this is not strictly necessary in the presence of a good process reward
model (Setlur et al., 2024c).
• 𝛾 ∈ [0,1]: thediscountfactor,balancingthetrade-offbetweenfurthercomputationandrewards.
We refer to the LLM generating the reasoning steps as the policy s ∼ 𝜋 (·|S ). In addition we
𝑡+1 𝜃 𝑡
refer to a solution starting from s = q as an episode or a trajectory. We will also use the notation z
0 𝑡
to represent individual reasoning steps that are part of the Meta-CoT and correspondingly denote
Z = (q,z ,...,z ).
𝑡 1 𝑡
Inthepriorsectionweconsideredgeneratingandrankingfullsolutions,whichmaybeinefficient.
We can extend the concept of a solution verifier from the prior section, to estimating the probability
that a particular intermediate state will lead to a solution: 𝑣 (q,S ) → [0,1]. These models have
𝜃 𝑡
become more widely known as Process Reward Models (PRMs) (Lightman et al., 2023). If we have
access to such a model, we can improve the efficiency of the search process with the following steps:

## Terminate a solution attempt that is not making progress, or is incorrect prior to reaching the

final answer.

## Reset the agent to any intermediate, previously visited, state that has a high likelihood of

success.
Notice that with these two operations, and the general structure of language, we can implement any tree search procedure. This is the premise of several approaches (Yao et al., 2023; Hao
et al., 2023; Zhou et al., 2024a) with the RAP method (Hao et al., 2023) illustrated in Figure 4.
Theseapproachesusedifferingsearchstrategies(DF-

### S/BFS vs. MCTS) and process guidance evaluation

(generative self-evaluation vs. Monte-Carlo rollouts),
but they all share the same core idea: formulate the
reasoning problem as tree search guided by an intermediate heuristic function. As noted above, in
theory, tree search does not induce a fundamental
capability shift over parallel sampling, however, it
may induce significant efficiency gains as demonstrated by Yao et al. (2023). In particular, Figure 5
(sourcedfromYaoetal.(2023))showsnearly4times
increased efficiency, in terms of inference budget,
on a toy reasoning problem (Game of 24) when using a tree-structured search approach compared to
parallel sampling. While these earlier works focus
on zero-shot (or close to zero-shot) performance on
simple reasoning tasks, it is important to note that
tree-search methods have been successfully scaled Figure 5: ToT efficiency on the game of 24
shownasaccuracy(y-axis)vs. #nodesvisited
and deployed to a number of realistic agentic appli-
(x-axis). Source: Figure3inYaoetal.(2023).
cations (Koh et al., 2024; Putta et al., 2024; Brown
et al., 2024; Yu et al., 2024).
13

<!-- Page 14 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought
Figure 6: Scaling trends for MCTS at training and inference-time on board games. Left: Elo
scores of models trained with different architectures (depth × width) where each point represents
theEloscoreofthatmodelevaluatedwiththelabeledtreesize(between1to512nodes). Thecurves
demonstrate that the performance of each model snapshot follows a sigmoid pattern with respect
to the test-time compute budget. Source: Figure 8 in (Jones, 2021). Right: The trade-off between
train-time and test-time compute, with progressively improving Elo (from bottom-left to top-right).
Source: Figure 9 in (Jones, 2021).

### Is Search (Inference Time Compute) A Fundamental Capability Shift?

Aspointedoutearlier,thequestionremainswhetherinference-timesearchisafundamentalnewcapability or whether it is accessible with additional training. Results from classical RLHF tuning (Dubois
et al., 2024) suggest that this is a learnable capability, where zero-shot performance of post-trained
models matches or outperforms the best-of-N paradigm.
We stipulate that performance on complex reasoning tasks is governed by a scaling law, which
involves model size, training data (compute) and inference time compute.
ThisisindeedconsistentwiththetheoreticalresultsofLietal.(2024)andtheintuitionpresented
in Section 2. Larger models are more capable of internalizing the Meta-CoT process in their activations, and are also capable of using longer inference-time Meta-CoT to approximate solutions with
significantly higher computational complexity. Empirically, we have limited (but promising) evidence
towards this hypothesis. A major prior work to study these questions is Jones (2021) which carries
out studies using the AlphaZero algorithm (Silveretal.,2018)onboardgames. Thisapproach

### Method Policy Value Accuracy(%)

fits our desiderata very well as the underlying 𝜋 - 41.4

### Greedy 𝜃0

MCTS algorithm jointly scales the policy and 𝜋 - 47.9
𝜃1
value (verifier) models’ training in conjunction 𝜋 {𝑣,𝑟ˆ} 51.9
with search. Moreover, this family of board 𝜋
𝜃0
{𝑣,𝑟ˆ}
𝜑0
53.2
gameshaveacleargenerator-verifiergapasgen-
MCTS-𝛼
𝜋
𝜃0
{𝑣,𝑟ˆ}
𝜑1
54.1
erating optimal strategies at intermediate steps
𝜃1 𝜑0
𝜋 {𝑣,𝑟ˆ} 56.5
can be quite computationally complex, while
𝜃1 𝜑1
verifyingawinningconditionistrivial. Thema- Table 1: Iterative update results on GSM8k. 𝜃 ,𝜑
0 0
jor empirical results on scaling are shown in are the old parameters while 𝜃 ,𝜑 are the new
1 1
Figure 6. On the right side we see that perfor- ones. TS-LLM can boost performance by training
mance increases both with increased training LLMpolicy,value,orboth. Source: Table4in(Feng
compute and model size, as outlined earlier. In- et al., 2024).
terestingly, on the left we see the performance
14

<!-- Page 15 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought
of using different quantities of compute (i.e., search with a value function) during inference. There
is also a clear scaling trend, showing improved performance with additional online search at each
intermediate checkpoint of training. In fact, the results in this domain indicate there is a clear
log-log scaling trade-off between train-time and test-time compute deployment. Currently, we have
limited evidence of similar scaling laws in LLMs because such a training pipeline requires significant
resources. One major work towards that goal is Feng et al. (2024) which carries out two iterations of
MCTSfine-tuningusingaLLaMa7BontheGSM8kdataset(Cobbeetal.,2021). Theyshowimproved
performance in zero-shot evaluations of the policy, as well as significant gains from using additional
inference-time search, at both iterations 1 and 2 (full results are shown in Table 1). However, their
work does not ablate the model size, data scaling, or inference-time search scaling, which remain
under-explored in the literature for LLM reasoning.

## Towards Meta-CoT Reasoning

Inpriorsectionswe: introducedtheconceptofMeta-CoTandarguedthatitisnecessaryforadvanced
reasoning, discussed the generator-verifier gap as a fundamental limitation, argued for search as
a fundamental building block of the Meta-CoT, and discussed the utility of approaches integrating
generator, verifier, and search components. However, the question remains on how to integrate these
into a model to perform Meta-CoT or “System 2” reasoning. The first question we need to answer is:
why do we actually need to internalize deliberate reasoning inside a single model? We propose two
main reasons:

## Efficiency: By incorporating search within the context of an auto-regressive model, exploration

can be done efficiently since the model has access to all previously visited nodes, in context.
Unique to the case of reasoning in natural language, many branches may contain semantically
similar content, unlike other domains (e.g., board games), motivating the need for improved
efficiency. Infact,evenadvancedreasoningmodelscarryoutmanyrepeatedstepsofsemantically
identical reasoning as we show in Figure 14 and 15.

## Super-Intelligence: If an auto-regressive model can learn to implement search algorithms

in-context, then additional RL training may enable the model to discover novel reasoning
approaches. Essentially,weproposethattrainingamodelcapableofinternalSystem2reasoning
(e.g. Meta-CoT) and search is an optimization over algorithms rather than specific outputs,
possibly yielding novel modes of problem solving. This will potentially allow the model to solve
classesofproblemspreviouslyunsolvableundersymbolic-basestree-searchapproachesaswe’ve
outlined in Sections 3.3 and 3.4.
In the remainder of this section, we explore how to train a model to internalize such a reasoning
system.

### Bootstrapping Meta-CoT

In this subsection, we overview the core idea behind the Self-Taught Reasoner (STaR) approach (Zelikman et al., 2022; Singh et al., 2024; Yuan et al., 2023) to bootstrapping intermediate CoT steps
and how to use a similar concept to generalize to meta-reasoning strategies.

#### Self-Taught Reasoner

The STaR method introduces an iterative bootstrapping approach designed to improve the reasoning
capability of LLMs (Zelikman et al., 2022). STaR focuses on training models to generate and refine
15

<!-- Page 16 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought
rationales, particularly for tasks requiring complex reasoning in a reinforcement learning-based
manner. In this formulation we assume we have access to a dataset 𝒟 = {q(𝑖),a(𝑖)}𝑁 of questions q
𝑖=1
that require reasoning along with corresponding answers a. Notice that we do not require access to
ground-truth rationales for these problems. We begin by prompting a model aˆ(𝑖),Sˆ(𝑖) ∼ 𝜋(a,S|q(𝑖))
to provide CoT rationale Sˆ(𝑖) = s (𝑖) ,...,s (𝑖) and final answer aˆ(𝑖). We then filter the generated data,
1 𝑁𝑖
keeping only rationales that lead to a correct final answer (i.e., aˆ(𝑖) = a(𝑖)) to create a dataset of
questions, (bootstrapped) rationales and answers 𝒟STaR = {q(𝑖),Sˆ(𝑖),a(𝑖)}𝑁
𝑖=1
. 𝒟STaR is then used to
train a model with the standard supervised fine-tuning objective:
[︁ ]︁
ℒ (𝜋 ) = −E −log𝜋 (a,Sˆ|q) . (2)

### STaR 𝜑 (q,S^,a)∼𝒟STaR 𝜑

The above procedure is repeated over several iterations. The core idea behind STaR is to generate a
trainingdatasetofsyntheticrationalesthroughsamplingandverification. Wewillextendthatideato
the the concept of Meta-CoT below.

#### Meta-STaR

We can generalize the above idea to Meta-CoT in a straightforward way. Consider a base policy
𝜋 combined with some general search procedure over intermediate steps. Given a question q we
𝜃
perform the search procedure repeatedly to generate search traces zˆ ,...,zˆ until we find a final

## 1 𝐾

solution (s ,...,s ). If we can verify the final produced solution 𝑣(S) → {0,1}, for example by using
1 𝑛
a formalization and verification approach (as in AlphaProof1) or some other outcome verification,
we can then apply a similar approach to STaR. For example, we can construct a dataset 𝒟STaR =
{q(𝑖),Zˆ(𝑖),Sˆ(𝑖)}𝑁 and use a similar training objective as before:
𝑖=1
[︁ ]︁
ℒ (𝜋 ) = −E −log𝜋 (Sˆ,Zˆ|q) . (3)

### Meta−STaR 𝜑 (q,Z^,S^)∼𝒟STaR 𝜑

Essentially,wecanuseabasepolicyandsearchproceduretogeneratesyntheticsearchdataandthen
train the model to implement these in-context through the Meta-CoT concept. We are effectively
proposing to linearize the search approaches described in Section 3 and teach an auto-regressive
model to run them sequentially. So far we have deliberately been vague about how these search
proceduresanddatasetslook. Wewillnowprovideexamplesandproofofconceptfromtheliterature
on practical approaches to this problem as well as synthetic examples of realistic training data.

### Empirical Examples Of Internalizing Search

When we formulate search in a sequential fashion we can explicitly parameterize each component in
language, or choose leave it implicit (Gandhi et al., 2024). Note that models trained with standard
next token prediction still need to implicitly internalize all of these components anyway in order to
accurately model the search sequence, even if they are not explicitly verbalized. However, allowing
themodeltovocalizeit’scertaintyorestimatedprogresscouldallowforadditionalmodelingcapacity
or be useful for interpretability purposes. We will present some examples of auto-regressive search
procedures from the literature in the following section.

#### Small-Scale Empirical Results on Internalizing Search

Twoparticularpriorworksthatexploretheideaofin-contextsearchareYangetal.(2022)andLehnert
etal.(2024)whichfocusonmazesandotherclassicalRLenvironments. TheformulationfromLehnert
1https://deepmind.google/discover/blog/ai-solves-imo-problems-at-silver-medal-level/
16

<!-- Page 17 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought
Figure 7: A* planning algorithm outline for a simple maze navigation task, along with a state and
action tokenization scheme. The search representation explicitly models nodes and queue state, the
search procedure and the cost and heuristic evaluation. Source: Figure 1 in (Lehnert et al., 2024).
Figure 8: Model performance vs. training compute when using the A* planning algorithm (Search
Augmented) vs. no search (Solution Only). We see that the search augmented models perform much
better across all training scales (charts a and b). In particular performance is consistent with the
search formulation of Section 3.4. Figure c) shows performance in terms of task complexity as maze
size increases. Results are consistent with the Meta-CoT complexity argument presented in Section 2
and results on the HARP benchmark in Figure 1. Source: Figure 2 in (Lehnert et al., 2024).
17

<!-- Page 18 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought
Figure 9: Inference compute scaling relationships for the o1 model (Left, sourced from (OpenAI,
2024) on AIME, Stream-of-Search on the Game of 24 (Middle) and MAV-MCTS on Chess (Right,
sourcedfrom(Schultzetal.,2024)). Thesefiguresshowperformanceofasinglemodelunderdifferent
token sampling budgets.
et al. (2024) is shown in Figure 7, which illustrates linearizing A* search. In our framework the
“Trace” corresponds to the Meta-CoT Z, and the “Plan” is the CoT output S. In this setting the
search procedure is stated explicitly as it shows node states, actions, costs and heuristic values.
In this “stream” format we can then use standard auto-regressive language models with a next
token-prediction objective to train a model to internalize the search process. Evaluation results
are shown in Figure 8 sourced from the same paper. We observe empirical effects consistent with
the scaling law hypothesis presented in 3.4; there is consistent improvement with additional
training data and model size (train-time compute) across the board. A particularly interesting
observation is the complexity scaling relationship in part (c) of the figure. At smaller mazes (lower
complexity) the model directly producing the Plan (CoT) and performs comparably to smaller search
(Meta-CoT) augmented models, however as maze size (complexity) increases we see a widening gap
in performance between the search-augmented and zero-shot models. This is essentially identical
to the results shown in Figure 1 on the challenging HARP benchmark (Yue et al., 2024) between
the prior frontier models and the o1 series. These empirical observations are well aligned with the
intuition we presented in Section 2. For small mazes (low complexity problems) models are capable
of internalizing the reasoning process, but as problem complexity (maze size) increases this becomes
more challenging and model performance falls off compared to models which explicitly carries out a
search procedure. Unfortunately, Lehnert et al. (2024) did not publish inference compute scaling
laws, but given the algorithmic structure of the training data we can presume that inference-time
tokens scale with the same complexity as the A* search algorithm, which can be exponential in the
branching factor, while the plan length is linear in 𝑛. These results would also be consistent with the
inference costs on advanced math reasoning tasks reported in Figure 1.
Gandhi et al. (2024) extend the linearized search idea to a more realistic reasoning task - the
Countdown game - which requires the model to predict a sequence of mathematical operations on a
givensetofnumberstomatchatargetvalue. WhileGandhietal.(2024)useafixed250Mparameter
transformermodelanddonotexploreordiscusstheroleofmodelsize,trainingdata,andcomplexity
intermsofscalingperformance,weobtainadditionalresultsintermsofinference-timescaling,shown
in Figure 9. Our findings demonstrate a consistent log-linear relationship between tokens spent and
success rate. Similar results were also observed in recent work by Schultz et al. (2024), who train
language models on linearized search traces obtained from MCTS on board game environments.
Similar to the work of Gandhi et al. (2024), they find consistent improvements in performance as
the model is given additional search budget at test-time (Figure 9 right). Note that these models
demonstrateaninference-timescalinglawwiththesamefunctionalformastheo1modelondifficult
18

<!-- Page 19 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought
mathematics problems (OpenAI, 2024).

#### In-context Exploration For LLMs

While the prior section showed promise in teaching auto-regressive language models to internalize
complex search strategies involving exploration and backtracking, it remains unclear whether these
results can generalize to realistic language domains. In this section we will overview several recent
works, which show promise in internalizing episode-level search. Both Qu et al. (2024) and Snell
et al. (2024) evaluate results using open-source LLMs in the 7B and larger range on problems from
theMATHdataset(Hendrycksetal.,2021). Theyposetheproblemassequentialsampling-i.e. given
a problem q, generating full solutions from the same model auto-regressively as
S𝑗 ∼ 𝜋 (·|S𝑗−1,...,S1,q) (4)
𝜃
where S𝑖 are full solutions to the problem q. Both works formulate the problem as self-correction,
or revisions, during training. The approach generates training data by concatenating a number of
incorrect solutions with the correct revision and training on a linearized sequence (although the
exact training objective use a particular weighting grounded in RL (Peng et al., 2019)). The general
objective follows the form
min E [︀ −log𝜋 (S*|S𝑗−1,...,S1,q) ]︀ (5)
𝜃

### S𝑖∼𝜋ref(·|q),q∼𝒟train 𝜃

where 𝑗 is a fixed number of in-context exploration episodes sampled from a fixed distribution 𝜋ref
(i.e. 𝜋 ) and S* is some optimal solution. Essentially, this can be considered a linearization of the
0
Best-Of-N search strategy presented in Section 3.1 with rejection sampling. In this setting, the
Meta-CoTrepresentssearchinfullepisodesZ = S1,...,S𝑗−1 andS = S𝑗. Attesttimewecanfurther
control the quantity of compute by iteratively sampling from
S𝑖 ∼ 𝜋 (·|S𝑖−1,...,S𝑖−𝑗,q). (6)
𝜃
RepresentativeresultsforthisapproachareareshowninFigure10,sourcedfrom(Snelletal.,2024).
We see clear improvement in the pass@1 metric with additional amounts of in-context exploration
episodes with nearly 6-7% gain from zero-shot to the level of saturation. At the same time, autoregressive generation shows clearly better scaling properties than independent parallel sampling
(Figure 10 right). These results indicate that the model learns some degree of in-context exploration
and self-correction.

#### Using variable Compute


### Whiletheaboveapproachesdemonstratepromisefor

the model’s capability to carry-out in-context search,
theyaretrainedwithafixednumberofrevisionsand
useapre-determinednumberofrevisionsattesttime.
This is not ideal, as ideally the model would be able
tousearbitraryamountsofcomputeuntilitarrivesat
a solution with high enough confidence. We repeat
the above experiment using a uniform number of incontext solutions during training (ranging between
0-7),allowingthemodeltogenerateupto8solutions
at inference time by optimizing

### Figure11:Numberofin-contextrevisionsthe

model attempts grouped by difficulty level.
19

<!-- Page 20 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought
26
25
24
23
22
21
20
19
18
17
0 10 20 30 40 50 60
Number of Generations
)%(
ycaruccA
tseT

## Htam

Revision Model Pass@1 At Each Step
40
35
30
25
20
20 21 22 23 24 25 26
Number of Generations
)%(
ycaruccA
tseT

## Htam

Revision Model Parallel Verses Sequential
Sequential Best-of-N Weighted
Parallel Best-of-N Weighted
Sequential Majority

### Parallel Majority

Figure 10: Left: Pass@1 accuracy of a revision model after the specified number of generations
(revisions). Right: Scaling performance of the best-of-N strategy under parallel and auto-regressive
(in-context)sampling. Theperformancegapindicatesthatthemodellearnssomedegreeofin-context
exploration and self-correction. Source: Figure 6 from (Snell et al., 2024).
min E [︀ −log𝜋 (S*,EOS|S𝑗−1,...,S1,q) ]︀ ,𝑗 ∼ Unif(1,8) (7)
𝜃

### S𝑖∼𝜋ref(·|q),q∼𝒟train 𝜃

Thisformulationencouragesthemodeltocontinuerevisingit’ssolutionuntilitreachesasolution
with high confidence of correctness. Interestingly, our model generates an increasing number of
solutionsbasedonquestiondifficulty. SummarystatisticsbyproblemdifficultyareshowninFigure11
(right), where the model generates an average of 2.45 solutions for Level 1 problems and an average
of 5.84 for Level 5 problems, consistent with the behavior shown in Figures 1 and 8 (c). Specifically,
this demonstrates that the model has internalized the need for extended exploration on complex
reasoning tasks.
Our best performing run achieved an improvement of 2% over the LLaMa 3.1 8B Instruct model
that we initialize our models from. We attribute this to a mismatch between the instruct model’s RL
post-training,theoff-policySFTfine-tuningweutilize,andthelimitedamountoftrainingdatainthe
MATH train dataset. Indeed, any regular SFT training we performed on the RL post-trained model
actually worsened performance. We are currently exploring post-training on pre-RL base models
with extended datasets.

#### Backtracking in LLMs

In the prior sections, we reviewed evidence that auto-regressive models can internalize complex
search strategies in simple domains. We also showed that LLMs can learn in-context exploration at
the episode-level. However, whether models can implement complex search strategies (e.g. those
outlined in Section 3) auto-regressively remains an open question in public research. Specifically,
we refer to the ability to terminate a reasoning chain prior to completion, and the ability to reset
(semantically)toanarbitrarypreviouslyvisitedstatein-context. Thesetwostepscanbeunifiedunder
the concept of backtracking. Here we will review some recent works demonstrating that LLMs can
learn to backtrack.
Recent works have demonstrated that training on data with backtracking can improve language
modelsonsimplereasoningtasks(Yeetal.,2024b;Anonymous,2024)findthatlanguagemodelscan
sometimes“recognize”theirerrorsinternally,butdonothavetherequiredmechanismstoself-correct.
20

<!-- Page 21 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought
Similar to our motivation with Meta-CoT, their aim is for a single model to both recognize errors
and self-correct in-context. In their approach they create training data with incorrect steps directly
followed by the correction. The backtracking is signified by a special token, [BACK], at the end of
an incorrect step to allow the model to explicitly state it’s belief that an error has occurred. That is:
given a dataset 𝒟train of questions q and correct reasoning CoT solutions S = s
1
,...,s
𝑛
the training
objective becomes

### ℒbacktrack(𝜃) = −E

s1,...,s𝑛∼𝒟train,𝑡∼Unif(1,𝑛)
[︀ log𝜋
𝜃
(s
1
,...,s−
𝑡
,[BACK],s
𝑡
,...,s
𝑛
|q) ]︀ (8)
where 𝑡 is a randomly sampled time step in the solution and s− is a single incorrect reasoning step.
𝑡
This is in contrast to the standard approach, which only trains on the correct solution chains:
ℒstandard(𝜃) = −E
S∼𝒟train
[log𝜋
𝜃
(S|q)]. (9)
Ye et al. (2024b) explore inserting incorrect steps at varying rates (between 1% and 50%) and find
that high rates of incorrect steps actually leads to improved downstream performance. In particular,
theyfindthata50%rateofincorrectsteps(objectiveinEquation8)leadstoanincreasefrom78%to
94% accuracy on hard math problems as compared to training on only correct solutions (Equation 9,
CoT). While promising, these results are only verified on small models (124M parameters).
Incontrast,Zhangetal.(2024b)teachLLMstobacktrackbasedonsafetyconsiderationsusingthe
largerGemma2BandLLaMa38Bmodels. Inparticular,followingtheabovenotation,givenaprompt
q and two possible answers - a safe option S+ = s+,...,s+ and an unsafe option S− = s−,...,s−,
1 𝑛 1 𝑛′
where s here represent individual tokens (unlike before where they stood for logical steps), they
optimize the objective:

### ℒ(𝜃) = −E [log𝜋 ([BACK],S+|S−,q) +

(q,S+,S−)∼𝒟train,𝑡∼Unif(1,𝑛′) 𝜃 𝑡 (10)
log𝜋 (S+|q)].
𝜃
That is a combination of the Meta-CoT and regular CoT objectives as outlined above. Additionally,
notice that this objective masks out the unsafe completion, while the prior work trains on all tokens
including the incorrect logical steps. While the approach of Ye et al. (2024b) backtracks for a single
logicalstep(correction)thisworkalwaysresetstheagenttotheinitialstate. SFTtrainingissuccessful
inteachingthemodeltobacktrackandimprovesthesafetycharacteristicsoversupervisedfine-tuning
on just the safe answer (only the second term of Equation 10). However, these effects appear weak in
regular SFT models, but are significantly improved through further downstream RL training, which
we will discuss later on.

### Synthetic Meta-CoT Via Search

In the prior sections we argued for an approach to reasoning that teaches an LLM to internalize an
auto-regressive search procedure in-context. We also reviewed several recent works showing that
small auto-regressive models can carry out in-context exploration at the episode level, and larger
models can learn individual step backtracking. In this section, we explore how to construct synthetic
data for realistic Meta-CoT that involves full-scale in-context tree search.
Setup. For demonstrative purposes, we use the math problem presented by OpenAI (2024) as our
benchmark task, where Gemini 1.5 Pro (Reid et al., 2024) achieves a Pass@128 score of 6.25%
(8/128correct)–notablybeingtheonlyfrontiermodel(withoutadvancedreasoning)todemonstrate
non-zero performance at the time of our experiments. We use the same RL formulations for state
and actions as presented in 3.3. We explore two principal search algorithms for generating synthetic
21

<!-- Page 22 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought
training data: Monte Carlo Tree Search (MCTS) and A* variants. Both approaches necessitate a
heuristic state estimation function, for which we employ pure Monte-Carlo rollouts following the
methodology of Silver et al. (2018). Specifically, we estimate the value of a partial solution trajectory
as

## 𝐾

𝑣(S ,q) = E 1 ∑︁ 𝑟*([S𝑗 ,S ],q) (11)
𝑡 S𝑗
≥𝑡+1
∼𝜋
𝜃

## (S

≥𝑡+1
|S𝑡,q)𝐾 ≥𝑡+1 𝑡
𝑗=1
where 𝑟* is the verifiable ground-truth outcome reward. In our experiments, we sample 128 completions from the partial solution and evaluate the mean success rate under ground-truth outcome
supervision. In Appendix E, the numerical values of the states are listed after each step.

#### Monte-Carlo Tree Search

We conduct an example based on Monte-Carlo

### Tree Search (MCTS), which seeks to balance

exploration and exploitation. The MCTS implementation of Silver et al. (2018) has been
widely applied to the reasoning domain (Tian
et al., 2024; Feng et al., 2024), and we mostly
follow their implementation with some modificationstoaccountforthestructureofoursearch
problem (see Appendix D).
We present the search trace for our example problem - all the actions taken during the
search (i.e., the Meta-CoT in a linear format)
- in Appendix E. The numbers following each Figure 12: MCTS tree for the math problem presented by OpenAI (2024). The red node indicates
reasoningsteprepresentthevalueestimates. In
the solution.
our initial MCTS attempt we obtained a trace
with an excessive number of backtracks and
repetitions,includingfromhigh-valuestates(as
high as 1.0) with the resulting exploration tree is shown in Figure 12. We believe these effects are
due to the exploration bonus in MCTS search. We did not carry out extensive ablations on the search
parameters due to speed and costs. Since we use pure MC rollouts ("simulations") for state value
estimation, a single tree uses up to 20 million tokens inference (a cost of ∼$100 per tree). Moreover
the process can take up to half an hour due to API limits. Because of these issues we also evaluate a
more efficient best-first exploration strategy, which we present below.

#### A* search

We begin with an exploration of a type of best-first search based on the work by Koh et al. (2024),
which itself loosely follows an A* approach. The search procedure maintains a frontier ℱ of states,
whichisimplementedasamaxpriorityqueue. SimilarlytotheMCTSapproach,eachstateS consists
𝑡
of the question q and a partial solution consisting of generated reasoning steps (s ,...,s ). At each
1 𝑡
iteration, the state S ← pop(ℱ) with the highest value 𝑣 = 𝑣(S ,q) is selected, where 𝑣 ∈ [0,1]
𝑝 𝑝 𝑝 𝑝
is the value of the partial solution S including current and previous reasoning steps. At each node
𝑝
the policy 𝜋 proposes 𝑏 candidate next steps, each of which is evaluated by 𝑣 and added to ℱ if the
𝜑
depth of the tree |(s ,...,s )| has not reached the maximum depth search limit 𝑑. For the purpose
0 𝑝
of generating synthetic data, we run the search until we find a solution that is correct using the
ground-truth verifier. The resulting tree is shown in Figure 13. It shows more consistent flow of the
22

<!-- Page 23 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought
reasoning steps, with less backtracking concentrated around a few key steps.

### Do Advanced Reasoning Systems Implement In-Context Search?

In this section we will investigate whether advanced reasoning systems, such as OpenAI’s

### O1 (OpenAI, 2024), DeepSeek R1 (DeepSeek,

2024) and Gemini 2.0 Flash Thinking Mode 2
and the Qwen QwQ Team (2024) implement
in-context search. We provide successful reasoning traces for the same math problem in
Appendix E.
Starting with OpenAI’s o1 model, by carefullyexaminingtheprovidedmathematical reasoning trace, we observe:

## Inconsistent flow ofthought -consecutive

steps do not logically continue the prior
state. Figure 13: Resulting A* search tree on the math

## Backtracking - the model carries out "se- problem from OpenAI (2024). This trace presents

mantic backtracking" - frequently return- moreofabest-firstapproachwithfewerbacktracks,
ing to the same logical points. concentratedaroundkeysteps,ascomparedtothe

## Repetition - the model often repeats log- one produced by MCTS in Figure 12.

ical steps.
The qualitative behaviors observed in o1 (Figure 14 left) are similar to those in the example
synthetic trace (Figure 15) generated by Gemini 1.5 with and MCTS-like search processes. In
particular, there are abrupt changes in logical flow of the (Meta) CoT, which is natural as the model
backtracks between branches of the tree. Moreover, the model may explore multiple child nodes
of the same parent which are different strings, but can also be very semantically similar leading to
repetitive logic. This is clear in the provided trace, as the model repeats logical statement and goes
over the same derivations multiple times. Note also that we do not claim the model is implementing
tree search at test time, but rather that as much as the model’s output are expected to resemble
it’s training data, we hypothesize that examples of search were used during training (likely model
initialization). We will specifically address the need and effects of RL training in Section 6.
The DeepSeek R1 model DeepSeek (2024) also exhibits similar behaviors, as shown in Figure 14,
however, it also carries out a significant amount of self-evaluation steps. This could be achieved
by integrating a form of self-criticism (Madaan et al., 2023; Shinn et al., 2023) or a generative
verifier (Zhang et al., 2024a) in the search trace. The LATS framework (Zhou et al., 2024a) uses
a similar approach, combining MCTS search with self-criticism and shows empirical improvements
from self-reflection. Another alternative for synthetic data generation is the "Iteration-Of-Thought"
approach Radha et al. (2024) which also interleaves generation with inner dialogue. This would
explain the rather smooth logical flow of the R1 model, which does not exhibit as much abrupt
back-tracking, as compared to O1. As mentioned earlier, in order to adequately model the search
2https://ai.google.dev/gemini-api/docs/thinking-mode
23

<!-- Page 24 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought
Let n be an even positive integer. Let p be a monic, real polynomial of degree 2n; that is to say, 𝑝𝑥 = 𝑥!"+𝑎!"#$𝑥!"#$+⋯+ 𝑎$𝑥+ 𝑎% for some real
coefficients 𝑎%,…,𝑎!"#$​. Suppose that 𝑝
&
$ = 𝑘!for all integers k such that 1≤ 𝑘 ≤𝑛. Find all other real numbers xx for which 𝑝
’
$ = 𝑥!

### Backtracking Steps Verification Steps


### O1 DeepSeek–R1 Gemini 2.0 Flash Thinking

We are told that for all integer values of 𝑘satisfying 1≤𝑘≤𝑛 SoI have this problem here. Let's see what it's about. We have The problem asks for the real numbers 𝑥other than
𝑝 ( $ = 𝑘! a d n e g e r v e e e n 2 p n o , s w it h iv ic e h i n m te e g a e n r s n it , l a o n o d k s a l m ike o n th ic is r : eal polynomial 𝑝(𝑥)of ±1,±$ ! ,…,± " $such that 𝑝 & $ =𝑥!.
Our problem is: Given that 𝑝is monic of degree 2𝑛, and that 𝑝𝑥 =𝑥!"+𝑎!"#$𝑥!"#$+⋯+𝑎$𝑥+𝑎% We are given that 𝑝(𝑥)is a monic polynomial of degree 2𝑛.
𝑝 ( $ = 𝑘!for 𝑘=±1,±2,…,±𝑛, find all other real numbers 𝑥 for some real coefficients 𝑎%,𝑎$,…,𝑎!"#$. Thecondition𝑝 ( $ =𝑘!holds for integers 𝑘such that 1≤𝑘≤𝑛.
s In u c o h th t e h r a t w 𝑝 ord & $ s, = w e 𝑥 a ! r . e to find all real numbers 𝑥such that therefore, 𝑥!"𝑝( & $)is a polynomi ⋯ al of degree 2𝑛, and 𝑥!"’!is a T − h 1 is , − m 2 e , a … n , s − th 𝑛 e . condition holds for 𝑘=1,2,…,𝑛and 𝑘=
𝑝
&
$ = 𝑥!.
⋯
m
𝑥!
o
"
n
𝑝
om
& $
ia
−
l o
𝑥
f
!
d
"’
e
!
g
i
r
s
e e
a
2
p
𝑛
ol
+
yn
2
o
.
m
so
ia
,
l
t
o
h
f
e
d
ir
e
d
g
if
r
f
e
e
e
r e
2
n
𝑛
ce
+
𝑥
2
!
.
"𝑞𝑥 = T
So
he
, 𝑔
va
𝑥
lue
=
o
−
f ( $
𝑥
a
!
re
−
±
1
1,
𝑥
±
!
$ !
−
,…
4
,±
…
" $
⋯
.
𝑥!−𝑛!𝑄(𝑥).
Our equation is 𝑝 & $ − 𝑥!=0. wait, but 𝑝(𝑥)is of degree 2𝑛, so 𝑝 & $ is & $ !"+𝑎!"#$&!" $ #$+⋯+ The degreeof 𝑥!−1 𝑥!−4…𝑥!−𝑛! is 𝑛.
L M r fu a e t n o t i c o r m e t n i o o e a v n l d e f o u e r, n f f s i c n 𝑥 in t e . i c o q e n ( 𝑝 x o ) f i s = 𝑥 a o 𝑝 p f o d & $ l e y g n − o re m 𝑥 e ! i ⋯ a 2 . l 𝑛 o w f h d e e n g r c e o e n 2 s 𝑛 id , e t r h e e d n 𝑝 as & $ a is a 𝑎 𝑎 t w w h $ $ h a i 𝑥 s & $ i i t c ! , + i h " s a # a 𝑎 i c $ t % t p m u + , o a a i 𝑎 l g l n l y % y h d n , 𝑥 t o s ! m b i m " n e u , c i , l a w e t l b i h p 𝑝 o u i l c ( f y t 𝑥 h i d s n ) i e i g n s i g s c i b r e n m e y d 𝑝 e o 𝑥 e ( n 2 e ! 𝑥 i " 𝑛 d ⋯ ) c g + i o a s i f v 2 m d e d , e o s e a g n g 1 s r i s e r c + e u e , e m 𝑎 𝑎 2 2 % i ! 𝑛 n " 𝑛 c g # p , o $ o t 𝑎 u 𝑥 h l % l y e d + n i s l b o e ⋯ n e m a o d + a i t a i n n z l. y g e t r h t o e i , n r g m . T T L 𝑔 W C e h h o e 𝑥 t e e n ’s r k s d e c n i = d f e o o o g e n − w r r r e s e 𝑥 t , i t d e h ! h t " e e h a o ’ r e t p f ! t 𝑔 d 𝑔 o h + e e l 𝑘 y 𝑥 g 𝑎 n e % r o x e = 𝑥 i p m s e ! r 0 " 2 i e o a 𝑛 + s f f l o s + ℎ 𝑄 i r 𝑎 o ( $ 𝑘 2 𝑥 n 𝑥 𝑥 . ) = o ! = " i f s ± # 𝑔 1 $ 1 2 + + , 𝑥 𝑛 ± ⋯ 𝑎 + 2 i ! n , " + 2 … m # 𝑎 $ , o − ± 𝑥 ! r " 𝑛 e + 𝑛 # . $ d = ⋯ 𝑥 e 𝑛 t + + a + i 1 𝑎 l. . % 2 𝑥 . !"−𝑥!"’!.
But we can consider q(x)=𝑝 & $ − 𝑥!. is 𝑥!", so 𝑝 & $ =𝑥#!"+⋯+𝑎%, and 𝑥!"’!𝑝 & $ =1+𝑎!"#$𝑥+ Therootsofℎ(𝑥)are ±1,±2,…, ⋯ ±𝑛.
Alternatively, let’s consider sx = 𝑥!"𝑝 & $ −𝑥!"’!. ⋯+𝑎%𝑥!", which is indeed a degree 2𝑛polynomial. Let's recheck the degree of the factors.
Let me consider that 𝑠𝑥 =𝑥!" ⋯ 𝑝 & $ −𝑥! =𝑥!"𝑞(𝑥). s 𝑥 o !" , ’ 𝑥 ! ! , " w 𝑞 h 𝑥 ich = is 𝑥 a ! " d 𝑝 eg & $ ree − 2 𝑥 𝑛 !" + ’! 2 = pol 1 yn + o 𝑎 m ! i " a # l $ i 𝑥 f 𝑥 + !" ⋯ ’! + is 𝑎 % th 𝑥 e ! " hig − hest T T 𝑥 h h ! e e − p le r 1 a o d d i h u n a c g s t t d h e a e rm s g r d e o e e f g ℎ 2 re ( . 𝑥 e ) 2 i 𝑛 s . a form −𝑥!"’!.
S S o inc 𝑠 e 𝑥 𝑞 = 𝑘 𝑥 = !" 0 𝑞( fo 𝑥) r . 𝑘 =±1,±2,…,±𝑛, we have 𝑞𝑘 =0. degree term. ⋯ The leading term of 𝐶 𝑅(𝑥)is 𝐶 𝑥!".
This doesn't seem right.
B B Re u u c t t a o 𝑡 l u l 𝑥 t r h k a = e t y 𝑝 𝑞 i ∗ s ( 𝑘 𝑥 th ) = a , t a 0 𝑠 nd f 𝑥 o 𝑠 r = 𝑘 𝑥 = 𝑥 = ! ± " 𝑡 𝑞 1 ( , 𝑥 ⋯ 𝑥 ± ) 2 . − , … 𝑥! , " ’ ± ! 𝑛 . . w 𝑘 𝑘 ! ! e " , ’ k s n ! o o = 𝑞 w 0 𝑘 t . ha = t 𝑞 𝑘! 𝑘 "𝑝 = ( $ 0 − fo 𝑘 r ! 𝑘 "’ = ! ± = 1 𝑘 ,± !" 2, 5 ⋯ 𝑘! ,± − 𝑛 𝑘 , ! b " e ’ c ! a = us 𝑘 e ! " 𝑝 ’! ( $ − = L 𝑔 W e e 𝑥 t's h = a g v o e − b 𝑥 𝑔 a ! c " 𝑘 k ’ ! t = o + t 0 h 𝑎 e % fo 𝑥 d r ! e " 𝑘 f + i = ni 𝑎 t ± i $ o 1 𝑥 n , ! … " o # f , $ ± 𝑔 + 𝑛 𝑥 . ⋯ . +𝑎!"#$𝑥+1.
⋯ therefore, 𝑞𝑥 has 2𝑛roots at 𝑥=±1,±2,⋯,+𝑛. Consider the polynomial𝑠𝑥 = ∏"%& . $ ( & & ! ) #(!.
Thus, 𝑠𝑥 must be divisible by the monic polynomial whose since 𝑞𝑥 is a degree 2𝑛+2polynomial, there are two more ⋯
r T o h o u t s s , a 𝑠 re 𝑥 ± = 1, 𝑚 ±2 𝑥 ,… ℎ , ( ± 𝑥 𝑛 ). . r fo o r o t s s o m be e y o co n n d s 2 ta 𝑛 n r t o 𝑎 o , t b s. ecause the roots come in pairs 𝑥=𝑘and The values± " $ !are distinct from ±1,±2,…,±𝑛.
Where 𝑚𝑥 = 𝑥−−𝑛 𝑥−−𝑛+1 …𝑥−−1 D𝑥− 𝑥=−𝑘, and possibly another pair 𝑥= 𝑎and 𝑥=−𝑎. The real numbers𝑥for which 𝑝 & $ =𝑥!are ±1,±2,…,±𝑛, " $ ! ,− " $ !.
T 1 he E re … fo (𝑥 re − , ℎ 𝑛 ( ) 𝑥 . )is a quadratic p ⋯ olynomial. w g m i a v o i e r t e , s b r 𝑛 o u q o t u t 𝑞 s a 𝑥 t d o r a a i t s c i c c d o f e a u g c n r t e t o e f r o s 2 , r . 𝑛 w + hic 2 h , a is n d d e ( g 𝑥 r ! ee − 2 𝑘 𝑛 ! . ) s f o o , r t 𝑘 he = re 1 a t r o e 𝑛 two T − h " $ e !. question asks for the other real numbers, which are " $ !and
Our plan is to write 𝑠𝑥 =𝑚𝑥ℎ(𝑥). alternatively, perhaps 𝑞𝑥 =(𝑥!−1)(𝑥!−4)⋯(𝑥!−𝑛!)5(𝑥!− Let's double check the reasoning.
Given that 𝑠𝑥 is degree 2𝑛+2with leading coefficient −1, 𝑎)(𝑥!−𝑏), where 𝑎and 𝑏are th ⋯ e remaining roots. The condition 𝑝 & $ =𝑘!for 1≤𝑘≤𝑛implies that 𝑥=
⋯ ±1,±2,…,±𝑛are roots of 𝑔(𝑥).
Similarly, 𝑚𝑥 is a degree 2𝑛monic polynomial. wait, but in the factorization, I have 𝑥!"− (" $ !)!, which gives 𝑥= ⋯
T co h e e f r f e ic fo ie r n e t , ℎ − ( 1 𝑥 , )must be a degree 2polynomial with leading ± " $ !, assuming that’s correct. T So he , 𝑞 ro 𝑦 ots = o C f 𝑞 y (𝑦 − ) 1 are y ± + 1, 1 ±2 y ,… − , 2 ±𝑛 y . +2…(y−n)(y+n)
Alternatively, since 𝑠𝑥 =𝑚𝑥ℎ(𝑥), but ineed to verify this conclusion. 𝑞𝑦 =𝐶 𝑦!−1 𝑦!−4…(𝑦!−𝑛!).
We can write 𝑠𝑥 = −1𝑥!"’!+𝑙𝑜𝑤𝑒𝑟 𝑑𝑒𝑔𝑟𝑒𝑒 𝑡𝑒𝑟𝑚𝑠. given that 𝑎= (" $ !)!, and the factorization is 𝑟𝑥−𝑥!"’!= The leading term of 𝑞𝑦 is 𝑦!"’!.
Sowe have: ⋯ −𝑥!−1 𝑥!−4⋯𝑥!−𝑛! 𝑥!− " $ !! ,that indeed, the roots T T h h e is l d e o ad es in n g o t t e m rm a t o ch f . 𝐶 𝑦!−1…(𝑦!−𝑛!)is 𝐶 𝑦!".
𝑠𝑥 =𝑚𝑥ℎ𝑥 =[∏"(-$(𝑥!−𝑘!)](−𝑥!+𝑏𝑥+𝑐)and 𝑠𝑥 = are 𝑥=±1,±2,…,±𝑛,± " $ !. Let's re-read the problem carefully.
𝑥 A Th ! lt " e e 𝑝 n rn 𝑠 a & $ t 𝑥 iv − e = , 𝑥 l ! e 𝑡 " t ’ ’ 𝑥 s ! c . − on 𝑥 s ! id "’ e ! r t = ha 𝑝 t ∗ 𝑡 𝑥 ⋯ 𝑥 − = 𝑥 𝑥 !" ! ’ " ! 𝑝 . & $ =𝑝∗(𝑥). t ± b o h f u e " $ t 𝑎 r ! . e . w f a o i r t e , , i s t h 𝑛 e ! c a o d r d re it c io t n h a e l r e so ? lu le t t io m n e s b d e o y u o b n le d - c 𝑥 h = ec ± k 1 th ,± e 2 c , a … lc , u ± la 𝑛 tio ar n e W W Co e e n a a s r r id e e e g a r s iv t k h e e e n d p c fo o o r l n y d r n e i o t a i m l o n n ia u s l m o 𝑟 n b 𝑥 e 𝑝 rs = & $ 𝑥 𝑥 . s ! u 𝑝 ch & $ th − at 1 𝑝 . & $ =𝑥!.
So, the coefficient of 𝑥!"in 𝑠(𝑥)is 𝑠!"=𝑐. earlier, ihad: The roots of𝑟(𝑥)are the values of 𝑥for which 𝑝 & $ = & $ !.
B So u t 𝑠 𝑠 𝑥 𝑥 = = [𝑝 𝑝 ∗ ∗ (𝑥 𝑥 )] − − 𝑥 𝑥 ! ! " " ’ ’ ! ! . . 𝑎= −1"(15 1 459⋯𝑛!)=(𝑛 1 !)! The given condition is 𝑝 ( $ =𝑘!.
B T T T h h h u u u u t s s s 𝑝 , , 𝑥 ∗ 𝑐 t ! h 𝑥 = e = o ( h 𝑐 " t $ a ! h ) = s ! e r d 0 r e e ⟹ g a r l e 𝑥 n e u = ≤ m ± b 2𝑛 e " $ r . ! s ar ⋯ e 𝑥=± " $ ! s t h ± h i e n e " n $ c r ! c e e e f 𝑛 o , r t i e h s , e e t v h o e e th n a e , d r ( d − re i 1 t a i ) o l " n n = a u l m 1 r , o b s o e o t r s s i n a 𝑥 d re t e h e 𝑥 a d t = , s 𝑎 a ± t = i " s $ f ! ( y " $ 𝑝 !)!. & $ =𝑥!are 𝑥= T 𝑛 T T T h h h h . e e e e s q r v e o a u o a l e u t r s e e s t s i o ± o f f n o 1 𝑔 , r a ± ( w s 𝑥 k $ ! h ) s , i a c … f r h o e , r t ± t h " h e a " $ e l . l c v o o a t n l h u d e e it r s i o r ⋯ o e n f a i l 𝑥 s n f g u o i m r v e w b n h e i r a c s r h " e . t ( $ he w h e e q r u e a 1 lit ≪ y h 𝑘 ol ≪ ds.
Answer: The other real numbers 𝑥satisfying 𝑝1⁄𝑥 =𝑥!are The values±1,±2,…,±𝑛correspond to the given conditions.
𝑥=± " $ ! The other real numbers are" $ !and − " $ !.
Figure14:Examplesofintermediatetracesfromo1(OpenAI,2024),DeepSeek-R1(DeepSeek,2024),
andGemini2.0FlashThinkingMode. Wehighlighttwotypesofsteps: Backtracking,wherethemodel
visits a bad state and returns to a previously visited step, and Verification, where the model assesses
thecorrectnessofthepreviousoutput. Inconsistentlogicalflowandrepetitionarepresentinallthree
traces. DeepSeek-R1 and Gemini 2.0 Flash Thinking Mode both exhibit generative verification before
reaching an answer, while Gemini makes an incorrect verification and returns to the initial state. Full
search traces can be found in Appendix E.
24

<!-- Page 25 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought
Let n be an even positive integer. Let p be a monic, real polynomial of degree 2n; that is to say, 𝑝𝑥 = 𝑥!"+
𝑎!"#$𝑥!"#$+⋯+ 𝑎$𝑥+ 𝑎% for some real coefficients 𝑎%,…,𝑎!"#$​. Suppose that 𝑝
&
$ = 𝑘!for all integers k such that
1≤ 𝑘 ≤𝑛. Find all other real numbers xx for which 𝑝 $ = 𝑥!
’

### Backtracking Steps Verification Steps


### MCTS (Gemini 1.5) A* (Gemini 1.5) QwenQwQ

Let 𝑞𝑥 =𝑝 # " −𝑥!. Let 𝑞𝑥 =𝑥!𝑝 # " =𝑎$𝑥!%+𝑎"𝑥!%&"+⋯+𝑎!%&"𝑥+1. L in e t t e 's g e ta r c 𝑛 k , l e a n th d i s a p m ro o b n l i e c m re s a t l e p p o b ly y n s o t m ep ia . l S 𝑝 o o , w f d e e h g a r v e e e a 2 n 𝑛 . e T ve h n at p m o e si a ti n v s e
Let 𝑞𝑥 =𝑝 # " −𝑥!. Then 𝑞(𝑥)is a rational function of the The given condition 𝑝 ’ " =𝑘!implies 𝑞𝑘 =𝑘!%𝑘!=𝑘!%(! 𝑝𝑥 =𝑥!%+𝑎!%&"𝑥!%&", where all the coefficients are real numbers.
f 𝑞 or 𝑥 m ="(/!#%&#(⋯(/&#! # # ! % # &(/’#!#&#!#(!#!#. f L p o e o r t l y 1 𝑝 n ≤ o 𝑥 m |𝑘 = ia | l ≤ 𝑥 o ! f 𝑛 % d + eg 𝑎 r ! e % e & " 2 𝑥 𝑛 ! , % w &" he + re ⋯ 𝑛 + is 𝑎 " a 𝑥 n + ev 𝑎 e $ n b p e o a si t m iv o e n i i n c t eger. T 𝑘 h ≤ e 𝑛 p . r o S b in le ce m 𝑛 st i a s t e e v s e t n h , a t t h 𝑝 e i ’ " nte = ge 𝑘 r ! s f 𝑘 or r a a n ll g i e n t f e ro g m er s − 𝑘 𝑛 s t u o c 𝑛 h , t e h x a c t l 1 ud ≤ ing
We are given that 𝑝(𝑥)is a monic real polynomial of degree 2𝑛. zero, because 𝑘is the denominator.
𝑞𝑥 ="(/!#%&#(⋯(/&#! # # ! % # &(/’#!#&#!#(!#!#. W 𝑘≤ e a 𝑛 r . e given that 𝑝 ’ " =𝑘!for all integers 𝑘such that 1≤ So, we have 𝑝 ’ " =𝑘!for 𝑘=±1,±2,…,±𝑛. That gives us 2𝑛
𝑞𝑥 ="(/!#%&#(⋯(/&# # ! ! # # %&(/’#!#&#!#(!=1 # ( ! # # ). We are given that 𝑝 ’ " =𝑘!for integers 𝑘such that 1≤𝑘≤ e in q c u lu a d ti e o d n . s because for each 𝑘from 1to 𝑛, both 𝑘and −𝑘are
⋯ 𝑛. ⋯
L 𝑎 e "𝑥 t ! 𝑞 %& 𝑥 "+ = 𝑎 𝑥 $ ! 𝑥 % ! 𝑝 % ( . # "). Then 𝑞𝑥 =1+𝑎!%&"𝑥+𝑎!%&!𝑥!+⋯+ T 𝑞 h 𝑘 e c = on 𝑘 d ! i % ti 𝑘 o ! n = 𝑝 𝑘 ’ " !%( = ! 𝑘 fo ! r f 1 or ≤ 1≤ 𝑘 ≤ 𝑘 𝑛 ≤ . 𝑛is equivalent to B ha u n t d 𝑝 le # , " le i t s ' s a m ra u t l i t o ip n l a y l b fu o n t c h t i s o id n e , s n o b t y a 𝑥 p !% ol t y o n o el m im ia in l. a T t o e m th a e k e it easier to
Thus, 𝑟(𝑥)is a polynomial of degree 2𝑛+2with roots 𝑘for 1≤ Consider the polynomial 𝑟𝑥 =𝑥!%(!−𝑞(𝑥). We are given denominator:
𝑘 W ≤ e a 𝑛 r . e S g in iv c e e n t h th e a re t 𝑝 a ( re 𝑥 ) 2 i 𝑛 s a su m ch o n v i a c l u re e a s l o p f o 𝑘 ly , n w o e m c i a a n l o w f r d it e e gree 2𝑛. t S h in a c t e 𝑟 𝑛 𝑘 is = ev 0 e f n o , r l e 1 t ≤ 𝑛= 𝑘 2 ≤ 𝑚. 𝑛 T . hen we have 2𝑛=4𝑚. Thus, 𝑥!%𝑝 𝑥 1 −𝑥!%𝑥!
Since 𝑝 ’ " =𝑘!for all integers 𝑘such that 1≤𝑘≤𝑛, we have 𝑟𝑘 has the roots ±1,±2,…,±2𝑚. Now,𝑝 # " =( # ")!%+𝑎!%&"( # ")!%&"+⋯+𝑎" # " +𝑎$, so multiplying by
𝑞𝑘 =𝑝 ’ " −𝑘!=0for 1≤𝑘 ⋯ ≤𝑛. 𝑟 ∏! ’ 𝑥 ) *" = 𝑥− 𝑥− 𝑘 1 𝑥+ 𝑥+ 𝑘 1 =∏ 𝑥 ! ’ − ) *" 2 𝑥! 𝑥 − + 𝑘 2 ! … . 𝑥−2𝑚 𝑥+2𝑚 = 𝑥!%giv 1 e + s: 𝑎!%&"𝑥+𝑎!%&!𝑥!+⋯+𝑎"𝑥!%&"+𝑎$𝑥!%−𝑥!%(!=0
We also know that the coefficient of 𝑥!%("is 𝑟(𝑥)is 0. The Since 𝑞𝑥 is a polynomial of degree 2𝑛, 𝑟𝑥 is a monic Let’s denote this polynomial as𝑞𝑥 =1+𝑎!%&"𝑥+𝑎!%&!𝑥!+⋯+
c

## 𝐵

o
=
eff
0
ic
.
ient of 𝑥!%("in ∏% ’*"(𝑥!−𝑘!)(−𝑥!+𝐵𝑥+𝐶)is 𝐵. Thus p
T 𝑟 h
o
𝑥 e
ly
r
n
e =
o
fo
m
re 𝑥
ia
, !
l
w −
o
e
f
1
d
ca
e
n 𝑥
g
!
r
w
e
− r
e
it 2 e
2
!
𝑛
…
+2
𝑥!
=
−
4𝑚
2𝑚
+2
!
.
= 𝑥!−1(𝑥!−
𝑎

## S

"
o
𝑥
,
!
t
%
h
&
e
"
r
+
oo
𝑎
t
$
s
𝑥
o
!
f
%
q
−
𝑥
𝑥!
=
%(
0
!.
corresponds to the values of 𝑥where
So, 𝐵(2𝑚!)!=0, which implies 𝐵=0. 4)…𝑥!−4𝑚! 𝑝 # " =𝑥!.
We have 𝑟𝑥 =∏% ’*"(𝑥!−𝑘!)(−𝑥!+𝐵𝑥+𝐶). Therefore, we can write 𝑟𝑥 =𝑥!%(!−𝑞𝑥 = 𝑥!−1(𝑥!− ⋯
Sowe have 𝑟𝑥 =∏% ’*"(𝑥!−𝑘!)(−𝑥!+& % " ! # !). 4)…𝑥!−𝑛!𝑅(𝑥), where 𝑅(𝑥)is a polynomial of degree As we did earlier, multiplying both sides by 𝑥!%gives us 𝑥!%𝑝 # " −
Thus, 𝐵(2𝑚!)!=0, which means 𝐵=0. Therefore, 2𝑛+2−2𝑛=2. 𝑥!%(!=0.
S T b i h y n e c ∏ e c % ’ o * 𝑛 n " i s s − t a e 𝑘 n v t e t n 𝑘 e , r 𝐶 m … = 𝐶 of ( = % 𝑟 " !)! 𝑥 − . 1 A is l % s 1 o . 𝑛 , A ! 𝐴 l ! s = 𝐶 o, . − T th 1 h e . u S s c , o o ( , n − s 1 ta ) n % t ( 𝑛 te !) r ! m 𝐶 i = s g 1 i , v en W eq e u i a v r a e l e lo n o t k to in 𝑞 g f 𝑥 or = va 𝑥 lu ! e % s ( ! o . f T 𝑥 h ⋯ i s s u m ch e t a h n a s t w 𝑝 e # " wa = nt 𝑥 t ! o , f w in h d ic t h h e is But 𝑝 # " = 𝑥! ( % # " 𝑝 )!% 𝑥 1 +𝑎 = !% ( & 𝑥 1 " ) ( ! # " % )! + % 𝑎 & ! " % + &" ⋯ ( 𝑥 1 + )! 𝑎 % " &" # " +⋯ + + 𝑎$ 𝑎 , " so 𝑥 1 : +𝑎$
which implies 𝐶= (&")# " (%!)!. r 𝑘 o ≤ ots 𝑛 . o W f 𝑟 e 𝑥 are = lo 0 o . k W in e g k f n o o r w th t e h r a o t o 𝑟 ts 𝑥 of = 𝑥! 0 + fo 𝑏 r 𝑥 𝑥 + = 𝑐 ± = 𝑘 0 fo . r 1≤ Therefore, t = he 1 e + qu 𝑎 a !% ti & o " n 𝑥 b + e 𝑎 co !% m & e !𝑥 s: !+⋯+𝑎"𝑥!%&"+𝑎$𝑥!%
So, we have 𝑟𝑥 =∏% ’*"𝑥!−𝑘! −𝑥!+& % " ! # ! . 𝑟𝑥 =(𝑥!−1)(𝑥!−4)⋯(𝑥!−𝑛!)(𝑥!+𝑏𝑥− % " !!). 1+𝑎!%&"𝑥+𝑎!%&!𝑥!+⋯+𝑎"𝑥!%&"+𝑎$𝑥!%=0
⋯ Since the coefficients of 𝑝(𝑥)are real, the coefficients of 𝑞(𝑥) As we defined earlier, 𝑞𝑥 =1+𝑎!%&"𝑥+𝑎!%&!𝑥!+⋯+𝑎"𝑥!%&"+
Thus, we have 𝑟𝑥 =∏% ’*"(𝑥!−𝑘!)(−𝑥!+( ( & % " !) ) ! #). Since 𝑛is a th re e r c e o a e l, f f a ic n ie d n s t o s o th f e R c (𝑥 o ) ef a f r ic e i e re n a ts l. o In f r p ( a 𝑥 r ) ti a c r u e la r r e , a 𝑏 l. i s T h re e a re l. fore, 𝑎 W $ e 𝑥! k % n − ow 𝑥! th %( a ! t 𝑞(𝑥)has roots at 𝑥=±1,±2,…,±𝑛, which are 2𝑛
even, let 𝑛=2𝑚. roots.
We have 𝑟𝑥 =∏% ’*"(𝑛!−𝑘!)(−𝑥!+( ( & % " !) ) ! #.The roots of 𝑟(𝑥) The roots of 𝑥!+𝑏𝑥− % " !!=0are 𝑥= &,± ! ,!(# " !!. Thusthe ⋯
However, the problem specifies to find all other real numbers 𝑥for
other than ±1,±2,…,±𝑛satisfy −𝑥!+& % " !! #=0, so 𝑥!=( ( & % " !) ) ! #. r r o ea o l t . s are real if 𝑏!+ % . !!≥0, which is always true because 𝑏is which 𝑝 # " =𝑥!, excluding the 𝑥=±1,±2,…,±𝑛that are already
𝑟𝑥 =∏% ’*"𝑥!−𝑘! −𝑥!+ % " !! =−𝑥!∏% ’*"(𝑥!− Consider 𝑟𝑥 =𝑥!%(!−𝑞(𝑥). given.
𝑘!)+ (% " !)! ∏% ’*"𝑥!−𝑘!. The equation 𝑝 # " =𝑥!implies 𝑥!%𝑝 # " =𝑥!%(!, so q𝑥 = Therefore, the additional real solutions are𝑥=± % " !.
So, 𝑟𝑥 =∏% ’*"(𝑥!−𝑘!)(−𝑥!+( ( & % " !) ) ! # . We are looking for the 𝑥 ± ! 𝑘 %( ,1 !, ≤ th 𝑘 us ≤ 𝑥 𝑛 !% , ( a ! re − ro 𝑞 o (𝑥 ts ) . =0. We already know that 𝑥= But let's double-check this result. ⋯
r r o o o o t t s s o o f f 𝑟 −𝑥 𝑥 !+ =0 & % , " ! o ! # th = e 0 r , t h w a h n i c ± h 1 g ,± ive 2 s ,… us ,± 𝑥 𝑛 ! . = Th ( ( & e % " s !) ) e ! # . m S u in s c t e b e 𝑛 t is h e a n W Sin e c h e a 𝑟 v ( e 𝑥 ) 𝑟 i 𝑥 s an = e ( v 𝑥 e ! n − fu 1 n )( c 𝑥 ti ! on − , 4 𝑏 ) = ⋯ 0 ( . 𝑥!−𝑛!)(𝑥!+𝑏𝑥− % " !!). H 𝑥 e = nc ± e 1 , , 𝑥 ± = 2,… ± , % " ± !a 𝑛 r . e indeed additional solutions beyond the given
even integer, we have 𝑥!= (% " !)!, so 𝑥=± % " !. The other solutions are roots of 𝑥!− % " !!=0, so 𝑥=± % " !. **Final Answer** ⋯

### Final Answer: The final answer is ± % " ! ± % " !

Figure 15: Example synthetic search traces from Gemini 1.5 with MCTS and 𝐴*. We highlight
backtracking steps, where the model visits a bad state and returns to a previously visited step.
Inconsistentlogicalflowandrepetitionarepresentinbothtraces,butstandsoutparticularlyinMCTS
trace. Full search traces can be found in Appendix E.
25

<!-- Page 26 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought
process the model must internalize an evaluation mechanism. However, providing an explicit CoT
verification may be able to expand the model computational capacity and improve self-verification.
This is an empirical question, which is currently unclear in open research.
Gemini2.0FlashThinkingModeappearstoimplementasomewhatdifferentstructure. Specifically,
theflowofreasoningqualitativelyappearssmootherwithfewerlogicallyinconsistentsteps. Moreover,
it backtracks less frequently and often returns to the initial state. In fact in the provided example
the model solves the problem correctly and then fully re-generates a new solution from scratch
(backtracks from the final state to the initial one). It’s behavior seems to be to attempt a full solution,
whichmaybeterminatedearlybasedonsomesearchheuristic. Incaseswherethesolutionattemptis
unsuccessful, the model attempts a different solution approach, rather than branch at the step-level
in a tree search structure. This seems more consistent with a revision-based strategy as reflected in
past works (Qu et al., 2024; Anonymous, 2024; Kumar et al., 2024). The Qwen QwQ model Team
(2024) shows similar behavior, generating multiple solutions in-context, as also pointed out by Chen
et al. (2024).

## Process Supervision

A key component of the search approaches presented in prior sections is the evaluation function
𝑣(q,S ), which scores intermediate states in a reasoning chain. These evaluation functions have
𝑡
become widely known as Process Reward Models (PRM). By incorporating process supervision, the
search mechanism gains the flexibility to backtrack to earlier promising states when suboptimal
paths are encountered, thereby enabling more effective exploration. However, the question of how to
efficiently access such capabilities remains an open question. In Section 4.3 we showed examples of
using outcome-based verification with MCTS in combination with Monte-Carlo rollouts. However,
this approach can only be used during training due to the necessity for ground-truth answers, and
moreover it is extremely computationally inefficient. As mentioned earlier, a single training example
requires up to 20 million inference tokens, costing up to hundreds of dollars. It is significantly more
efficient to amortize the evaluation procedure into a single parameterized model, and we will outline
strategies for building such process guidance models below.

### Learning Process Reward Models

Parameterized PRMs are built on top of pre-trained models, either using a linear head or the logits
of specific tokens. The model takes the question q and a partial solution S as input and outputs a
𝑡
single scalar value 𝑣
𝜃
(q,S
𝑡
) → [0,1]. Given a dataset 𝒟train of partial solutions S
𝑡
and corresponding
value targets 𝑦 the model is generally optimized with a standard cross-entropy classification loss. A

### S𝑡

central question for training PRMs is: where do the supervision labels 𝑦 come from? One approach

### S𝑡

is to have human annotators provide step-by-step level evaluation of reasoning problems, as done
by Lightman et al. (2023). While their work showed promise in terms of empirical results, this
method is challenging to scale due to the high annotation time and cost, especially as evaluating
hard reasoning problems requires high-caliber experts. An alternative approach presented by Wang
et al. (2024) only relies on access to outcome verification - i.e. problems with a ground truth answer.
The proposed approach is to amortize the Monte Carlo state-value estimation into a parameterized
function. Essentially,thismethodfitsanempiricalvaluefunctionofthereferencerolloutpolicywhere
the targets 𝑦 are represented by Equation 11. This idea has been widely adopted in follow-up

### S𝑡

works (Snell et al., 2024; Anonymous, 2024) and further extended (Setlur et al., 2024c).
26

<!-- Page 27 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought

### PRM Quality And Its Effect On Search

Theperformanceandefficiencyofsearchattest-timedependsonthequalityofthePRM(Setluretal.,
2024b; Anonymous, 2024). Setlur et al. (2024b) demonstrate effective scaling (in both training data
sizeandlabelquality)ofaspecificvariantofPRMsthatestimatevaluesbasedontheimprovementin
likelihood of the correct answer after a step. The accuracy of test-time search improves log-linearly
with training data size, and the quality of learned value labels improve with more Monte Carlo
estimates. Anonymous (2024) show that oracle verifier-enabled search is orders of magnitude more
efficient than a learned PRM with noisy value estimates.
In this section we conduct an experiment demonstrating the scaling characteristics of a PRM.
To train our PRM, we first need to generate diverse solution trajectories where each solution step
is annotated with a ground truth value. To do so, we use the method from Wang et al. (2024)
to obtain ground truth values, performing 16 Monte Carlo (MC) rollouts for each step of a seed
solution. Wegeneratetheseedsolutionsandstep-levelMCrolloutsfromasupervisedfinetuned(SFT)
Llama3.1-8B using the PRM800K (Lightman et al., 2023) dataset. The PRM training data uses 7,086
unique questions - each with seed solutions - and after removing duplicate seed solutions results in
97,000trajectoriesinthetrainingdata. Toevaluatethescalingperformancewithincreasingdata,we
split the small set of data into three subsets: one with 500 unique questions, one with 3,000 unique
questions, and one with all 7,086 unique questions. We create an evaluation set using the MATH-500
dataset (Hendrycks et al., 2021; Lightman et al., 2023) by generating step-by-step solutions from the
SFTed model and step-level ground truth values from 128 MC rollouts.
With this trained PRM, we find a reduction in the absolute error of predicted values when
comparingPRMsthataretrainedacrossdatasetsofdifferentsizes,aswellasaselectionofintermediate
checkpointsinFigure16. Weobservethat: 1)thepredictionerrordecreasesasthesizeofthetraining
data increases, and 2) when the size of the dataset is small, improvement converges early during
training (around 30% of an epoch for Qs=500 and Qs=3000). Although these findings are based
on small-scale experiments, we anticipate continued improvement in prediction errors with larger
datasets and more extensive training, suggesting significant potential in further refining and scaling
PRMs. Additionally,weevaluatetheperformanceofthethreefully-trainedPRMsasoutcomeverifiers
whenperformingaBest-of-Nsearchduringinferencetime. Figure17leftshowsthatthePRM’sability
to verify full solutions improves as they are trained with more data, yet there exists a remarkable
gap between the trained PRMs and an oracle PRM. Additionally, we observe that the PRM’s ability
to guide the search process towards the correct answer with a more efficient path also improves as
the increased accuracy and reduced number of tokens used in the search process are both observed
in Figure 17 right. One interesting remaining question is: what is the scaling law for these process
supervision models?

### Verifiable Versus Open-Ended Problems

Training a value function with MC rollouts is scalable with infrastructure and inference, but is fundamentally limited to problems with verifiable solutions. This excludes proof problems and scientific
derivations which are often more important than the numerical answer itself. While automated proof
assistance is an established area of research in mathematics (mathlib Community, 2020), this is
rather limiting. First of all, these methods are largely limited to math and do not transfer to other
domains such as science or more general problem-solving scenarios. In those domains, training a
PRMbasedonhumanevaluationsofvalidreasoningstepscouldyieldageneralverifier, whichcanbe
used for assuring the validity of the proof/solution chain. This would explain the need for human
annotators and verification.
27

<!-- Page 28 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought
% pf Training Epoch
# of Unique Problems ~0.05 ~0.3 1
(#Training Trajectories)
500
(7.44k)
3000
(41.7k)
7086
(97k)
Figure16:DistributionofalearnedPRM’spredictedvaluesforeachstatevs. groundtruth(computed
using128MCsamples)asuniquetrainingquestionsincrease. Meanabsoluteerror(MAE)decreasesas
the PRM is trained with more questions. When the quantity of training data is small the performance
on the test set converges early (∼ 30% of an epoch in training).

## Meta Reinforcement Learning - Learning How To Think

In this section we will build out an interpretation of the reasoning problem and Meta-CoT from the
perspectives of meta-learning and meta-RL. In Section 4.2.1 we motivated the need for in-context
search through the paradigm of computational complexity and the generator-verifier gap. In this
section, we build an alternative formulation which will help us formalize empirical results of RL
training. In particular, we consider the search problem in the deterministic MDP formulation from
Section3.3,however,inthissectionweassumetherewardfunction𝑟(S,q) → {0,1}isadeterministic
(but a-priori unknown) function of the prompt q, which accepts only a particular set of solutions. At
testtimeunderanewprompt,thiscreatesepistemicuncertainty oftherewardfunctioni.e. a-priori
we do not know the full set of accepted or rejected solutions for this task (prompt question). This
process turns the MDP formulation we previously outlined in 3.3 into a Partially Observable MDP
(POMDP), a view formalized in classical RL by Ghosh et al. (2021). Their work proves the following
general remark:
28

<!-- Page 29 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought
0.7
0.6
0.5
0.4
0.3
1 2 4 8 16 32 64 Number of Generations per Problem
ycaruccA
PRM-Q7086 - BoN
PRM-Q3000 - BoN
PRM-Q500 - BoN

### Oracle

Majority ycaruccA snekoT
fo
#
hcraeS
ni
desU

### Process Reward Models

Figure 17: Left: Scaling curves for Best-of-N (BoN) using PRMs trained with different number of
questions with oracle and majority vote. Right: Beam search (N=5, beam width=4) accuracy and
numberoftokensusedduringsearchwiththesamePRMs. Withmoretrainingdata,thePRM’sability
to verify at outcome-level and process-level improves.
Figure18:Right: TheparadigmoftheRL2 formulationofmeta-reinforcementlearning. Foreachnew
task (prompt), the agent explores its environment over multiple episodes, keeping all the experience
incontextandmaximizesrewardsovertheentireinteraction. Source: Figure1in(Duanetal.,2016).
Remark 5.2 from Ghosh et al. (2021): The expected test-time return of policies that are
learned by maximizing reward in any MDP from the posterior, as standard RL methods do,
may be arbitrarily low compared to that of the Bayes-optimal behavior.
Inotherwords,regularRL-trainedpoliciescan,intheory,havearbitrarilybadperformanceonnew
reasoning domains Setlur et al. (2025). This statement is expanded on and made mathematically
precise by Ghosh et al. (2021) and follow-up works, however that formalization is beyond the scope
of the current report. In this work, we stipulate that the reasoning problem, as a POMDP, is better
suitedtoameta-RLframework(Humpliketal.,2019;Rakellyetal.,2019)ratherthantheregularRL
setting, as described above. In the meta-learning setting we are given a distribution of tasks, which
in our case would be individual reasoning problems q ∼ 𝒟train . The meta-learning objective seeks a
policy 𝜋 and an adaptation procedure 𝑈 such that, for a sampled task q, the adapted policy 𝜋
𝜃 𝑈(𝜃)
performs well with minimal additional samples. The overall optimization objective is
minE E [𝐿 (𝜃)],
𝜃
q∼𝒟train 𝜋
𝑈(𝜃)
q
where 𝐿 represents the loss associated with task q. For example, in the revision formulation of
q

### Section 4.2.2 the objective is

minE E [︀ −log𝜋 (S*|S𝑗,...,S1,q) ]︀ , (12)
𝜃
q∼𝒟train S𝑖∼𝜋ref(·|q) 𝜃
where S* is the optimal solution to the problem q and S𝑖,𝑖 = 1,...,𝑗 are solutions provided by
some reference policy (usually 𝜋 ). Here the adaptation procedure is represented by the operator
𝜃0
29

<!-- Page 30 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought
𝜋 (·|q) → 𝜋 (·|S𝑗,...,S1,q),whichisreminiscentofmeta-learningwithmemorynetworksSantoro

### 𝑈(𝜃) 𝜃

et al. (2016). The issue with this approach is that at inference time, given a new test problem q, we
samplesolutionsauto-regressivelyfromthecurrentiterationofthemodel𝜋 (·|q)ratherthan𝜋 which
𝜃 𝜃0
generatedourtrainingdata,whichgeneratesatrain-testdistributionshift. Indeed,Kumaretal.(2024)
notedacontinuousshiftduringtrainingevenwith𝑗 = 1wherethemodelsuccessfullycorrectswrong
solutions from the reference training data, but it’s capability to self-correct (correct wrong solutions
sampledfromthecurrentpolicy)diminishes-refertoFigure19(sourcedfromKumaretal.(2024))for
empirical results. If the reference model 𝜋ref
does not generate data with sufficiently high
coverage,thenthisdistributionshiftfundamentally necessitates the use of on-policy reinforcement learning approaches. Unlike conventionalreinforcementlearning,wheretheobjective is to optimize for immediate rewards,
meta-RL emphasizes training agents to quickly
explore a new environment and adapt to the
task at hand. This requires optimizing the sampling process during meta-training to ensure
theadaptationprocess𝑈 maximizestheagent’s
Figure19:Self-correctionperformancefromselfgenerated vs. fixed first steps. As training profinal performance.
gresses(fromlefttoright)themodelbecomesmore
If we modify the meta-learning objective in capable of correcting errors in solutions from the
Equation12withon-policysampling,wecanes- reference distribution, but less capable of correctsentiallyrecoveraformulationoftheRL2(Duan ing its own induced errors. Source: Figure 5 from
et al., 2016) approach, which has strong syner- (Kumar et al., 2024).
gies with LLMs due to their in-context learning
capabilities. In this setting the agent, represented as a recurrent policy, encounters a series of tasks q
and interacts with them for several episodes with persistent intra-episode memory for the particular
task. Here, the goal of the agent is to maximize the accumulated reward over 𝐾 episodes:
⎡ ⎤

## 𝐾

∑︁
m
𝜋
axE q∼𝒟train E S𝑗∼𝜋
𝜃
(·|S𝑗−1,...,S1,q)⎣ 𝑟(S𝑗,q)⎦ (13)
𝜃
𝑗=1
across the distribution of tasks, also notice that here the expectation is taken over the current policy
iterate𝜋 ,removingtheissueofdistributionshift. Wewilldrawsomeadditionalconnectionsbetween
𝜃
Equation 12 and Equation 13 in the next section. This objective be optimized through standard
reinforcement learning algorithms such as REINFORCE (Williams, 1992) and PPO (Schulman et al.,
2017). Whilesuccessfulinclassicalmeta-RLtasks,thisapproachcanleadtopolicycollapseonlocally
greedy behavior - i.e. it may not be able to fully explore new environments but instead collapse to
common behaviors. Addressing this issue, Stadie et al. (2019) propose a simple modification, E-RL2,
which considers the objective
maxE E [︀ 𝑟(S𝐾,q) ]︀ (14)
𝜋
q∼𝒟train S𝑗∼𝜋
𝜃
(·|S𝑗−1,...,S1,q)
𝜃
aiming to maximize the return over the final episode only. This allows the policy to explore without
reward supervision for 𝐾 −1 episodes, providing wider coverage of the environment which allows
the policy to maximize rewards in the final episode. This slight modification mostly prevents the
collapse to greedy behaviors seen in the standard RL2 algorithm. Since these early works there has
beensignificantfollow-upliteratureandwereferthereadertothesurveyofBecketal.(2024)foran
overview.
30

<!-- Page 31 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought
Figure20:Thebenefitsofreinforcementlearningforlangaugemodelreasoning. Whencomparing
ExpertIteration(SoS+STaR)vs. theRL-basedSoS+APA,weseethattheuseofRLleadstoimproved
policy performance (left), with fewer arithmetic errors (center), and improved efficiency (right).
Source: (left to right) Figures 4a, 6a, and 6b from (Gandhi et al., 2024).
The above discussion uses the standard RL2 episodic formulation as it was studied in classical
MDPs,however,thisisnotstrictlynecessaryinthelanguagesettingoutlinedinSection4. Ifweequip
the agent with the capability to
1. terminate an episode early - i.e. achieve the information objective before it reaches the final
solution
2. reset to an arbitrary state in context rather than restart the solution from the first step
thenthemeta-RLformulationremainsvalidforanyin-contextexplorationstrategy,includinggeneral
tree search approaches. In purely language domains, such as mathematical reasoning, this is feasible
and we can directly apply the E-RL2 algorithm outlined above to models such as those by Yang et al.
(2022),Lehnertetal.(2024),orGandhietal.(2024). However,indomainswherethepolicydoes
not have full control of the environment, such as code or agentic formulations, different search
structures may be required.

### Meta-RL In Small Domains

In the prior section we argued for on-policy RL in reasoning systems to handle train-test distribution
shifts, but whether pure instruction-tuning (without RL) is enough to induce capabilities in the
model is still debated. In general, the use of RL in post-training improves model performance.
Indeed, in Section 4 we outlined the capability to discover improved exploration (adaptation 𝑈)
algorithms through RL as a major advantage, but the degree to which this occurs remains unclear.
Specifically, we want to answer the question: can an in-context search algorithm, post-trained with
reinforcement learning, outperform a modular search system? One such example exists where, as
shown in Figure 20, RL post-training improves overall performance in terms of accuracy, reduces the
numberoflogical mistakes, andmakes thesearch more efficient. However, theoverallperformanceis
stillonlycomparabletothemodular(symbolic)searchparadigm-i.e. whileRLsignificantlyimproves
performance over the pure SFT (instruction-tuned) model, RL is not currently able to discover new
31

<!-- Page 32 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought
Figure 21: Overview of Reinforcement Learning with Execution Feedback. This training routine
directlymapstotheE-RL2 framework(Stadieetal.,2019). Source: Figure2in(Gehringetal.,2024).
search algorithms. Whether this is a fundamental limitation of the environment, pre-training data,
or scaling is currently an open question in the literature.

### Meta-RL In Language Model Reasoning


### Training

Two works that have scaled the multi-turn for- Model Valid Test

### Method

mulationofmeta-RLforreasoningtasksareKumar et al. (2024) and Gehring et al. (2024). – 8.9 10.5
While Reinforcement Learning with Execution Llama 3.1 Few-Shot 8.5 8.5
Feedback (RLEF) (Gehring et al., 2024) does 8B Instruct SFT 10.3 10.0
not use the meta-RL or search formulations, RLEF 17.2 16.0
they do frame their approach as "learning from
– 25.9 27.5
feedback", and it fits the Meta-CoT framework.

### Llama 3.1 Few-Shot 22.5 20.3

Specifically, RLEF implements the E-RL2 objec-
70B Instruct SFT 27.7 27.2
tive from equation 14 with an additional dis-

## Rlef 37.5 40.1

tributional constraint following standard RLHF
practices (Stiennon et al., 2022; Ouyang et al.,
Table 2: Comparison of different training methods
2022). First, the model runs several iterations
for 8B and 70B Instruct models on validation and
of exploration (episodes, which represent a
test datasets. “–” directly evaluates the instruct
fullcodesolution),receivingcompilerfeedback
model. Source: Table 3 in (Gehring et al., 2024).
from public test cases until it passes or reaches
an exploration limit. Next, the model proposes
a final solution (evaluation episode) and receives a reward based on hidden private test cases, which
isusedforRLtraining. SeeFigure21foranoverviewoftheprocess,alongwithanexampleofmodel
outputs. (Gehring et al., 2024) shows a number of interesting empirical findings. The first finding is
the relative effect of SFT versus RL training (results shown in Table 2). The clear trend is that SFT
32

<!-- Page 33 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought
Figure 22: Scaling results for Reinforcement Learning with Execution Feedback. Left: Pass@1 and
pass@10 for 8 and 70B models when given either ground truth feedback or random execution
feedback. Right: Model solve rates at various turn limits (1, 3, 5, and 10) and sample budgets.
Source: Figure 4 in (Gehring et al., 2024).
training does not induce any in-context exploration capability and the does not lead to improved
performance. This finding is consistent with the results from Kumar et al. (2024), which carry out a
similar analysis over multi-turn revisions of math problem solutions.
Next,asshowninFigure22,itisclearfromthepass@1resultsthatthemodelisabletoexploreand
internalize environment feedback to refine the code over multiple turns. However, more interestingly,
it is able to do so without reliable feedback. In particular the "random feedback" results replaces the
compiler output with output from an unrelated problem. This likely creates significant issues for the
model, since the feedback could throw off the LLM’s grounding (Mirzadeh et al., 2024). However, we
seethatwithRLtuningperformancecontinuestoimprovewithadditionaltest-timerevisions,although
a gap with ground-truth feedback still exists. This is consistent with the findings from Kumar et al.
(2024), which demonstrate the capability to self-correct without external feedback in the mathematical
reasoning domain. Furthermore, these results are also consistent with our formulation of exploration
in the epistemic POMDP from Section 6.

### Efficiency Or Super-Intelligence?

As outlined in the beginning of Section 4 two main reasons to internalize a search procedure within
a single auto-regressive model are: (1) improved efficiency of the search procedure, and (2) the
emergence of “super”-intelligence.
Results in Figure 20 show significant improvement from RL post-training in the limited domain
of the Countdown game, specifically, success rates improve while also using smaller search budgets.
However, even after RL post-training the SoS model does not out-perform the success rate of
the symbolic approach which generated the instruction-tuning data. Similar findings have also
been reported by Lehnert et al. (2024), where the model achieves significant improvement in token
efficiency, but not in success rates based on some simple post-training procedure. Currently, it is
unclear whether continued RL training can lead to a stronger model that substantially out-performs
the modular search approach. An interesting analysis by Gandhi et al. (2024) (Figure 23) shows the
performanceofvariousmethodsondifficultproblems(i.e.,problemsthatnomodularsymbolicsearch
33

<!-- Page 34 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought
Figure 23: Left: Scaling laws of the R1 model. Red: different training checkpoints. Blue: inference
timescalingcurvesfromeachcheckpoint. Weseethatthemodelusesinferencebudgetmoreefficiently
than parallel sampling with majority vote, but does not outperform large-scale parallel sampling at
higher token budgets. Source: (DeepSeek, 2024). Right: The percentage of problems which the SoS
model solves on Countdown, but symbolic strategies do not. The biggest gain comes from RL tuning
via STaR. Source: Figure 5c in (Gandhi et al., 2024).
approach solves). The base SFT-tuned SoS model solves about 1% of these problems, with RL-tuned
models reaching up to 4% (STaR in particular).
InSection6weoutlinedtheMeta-RLformulation,whichstipulatesthatthroughRLpost-training,
we’re essentially searching over algorithms, i.e. in-context adaptation procedures 𝑈(𝜃), rather than
pure policies. In-theory, this process could discover novel reasoning strategies that unlock capabilities
beyond the training data or manually designed reasoning approaches. Within the simple domain of
Countdown,thisdoesallowustosolvesomecomplexproblemsthatstandardsearchmethodsdonot,
but this effect appears weak, even in this limited setting. As outlined earlier, it is unclear whether
further RL training will allow us to discover novel reasoning algorithms that allow us to solve new
classes of problems. At larger scales, similar results seem to hold in the math (Snell et al., 2024)
and code-generation domains (with ground-truth environment feedback) (Gehring et al., 2024). As
shown in Figures 10 and 22 the E-RL2 training clearly improves the search performance in terms of
pass rate versus search budgets. However, it is unclear whether the RL post-trained model actually
solves classes of problems that are unsolved by the base model under increased search budget.
Indeed,forcodegeneration,atthe70Bscale,with𝑘 = 100theperformanceoftheRL-tunedmodelis
only about 5% above the base model. At the same time, performance of the RL model appears to be
saturating, while the base model demonstrates continued scaling. One potential counterpoint is the
scaling law presented by DeepSeek (2024), as shown in Figure 23 (left). In particular, we see that at
low token limits the model demonstrates significantly better scaling with additional in-context search
rather than parallel majority voting. On the other hand, at the higher end of token limits, majority
voting can out-perform the model with in-context search, but at a higher inference cost. We should
note that this approach uses solution-level majority voting, rather than a separate verifier, which has
proven to be a much stronger search strategy (Cobbe et al., 2021; Lightman et al., 2023).
34

<!-- Page 35 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought
In conclusion, based on public evidence, the proposed framework of in-context search can
significantly improve the efficiency of the search procedure over base models and "symbolic"
approaches or search strategies. However, there is only weak evidence that these models can
discover novel reasoning methods that can solve classes of problems that were not solvable
previously under some search budget.
That is, under current empirical evidence the benefits outlined in point (1) above appear clear.
However, evidence of emergent "super"-reasoning under point (2) appears weak.

### Can System 2 Reasoning Emerge From Pure RL?

Thereisanopinionintheopen-researchcommunitythatthecurrentgenerationofadvancedreasoning
models are artifacts of continual reinforcement learning 3. For both theoretical and practical reasons,
webelievethisisunlikelywiththecurrentgenerationoflanguagemodels. First,outsideoftheOpenAI
o1, DeepSeek R1, and Qwen QwQ models, which have undisclosed training routines, “standard”
models do not exhibit such strong reasoning behaviors, despite the fact that they have already been
extensivelypost-trainedwithinstruction-tuningandreinforcementlearningonreasoningtasks. From
amoretheoreticalpoint-of-view,meta-RLdoesnotarisefromstandardRL.Indeed,thisisthemain
point of Ghosh et al. (2021) and the remark in Section 6 - models trained with RL on standard CoT
formulation can exhibit arbitrarily bad performance on new problems.
We see this empirically in Figure 22 (right). Note that setting the turn limit to 1 (solid blue
line) corresponds to standard RL training (no in-context exploration episodes). In this setting the
RL post-trained model performs worse than the base model (dotted blue line) at higher levels of
inferencecompute(SampleBudget)onaheld-outtestset. Furthermore,modelstrainedwithevena
turnlimitof3showsignificantlybetterinferencescalingoverthebasemodel,continuingwellbeyond
their training budget. Similar results were obtained by Kumar et al. (2024), showing that a naive
applicationoftheRL2 objectiveinEquation13leadsthemodeltocollapseontoagreedypolicywhich
does not perform in-context exploration (consistent with the findings of the original work (Stadie
et al., 2019)). On the first step, the two-episode formulation of SCoRe (method proposed by Kumar
et al. (2024)) is identical to standard RL, which prevents the model from meaningful in-context
exploration. ToalleviatethisissuetheyincludeanadditionaltrainingstageusingtheE-RL2 objective,
similartoGehringetal.(2024),beforeannealingintoanRL2 approach. Theseempiricalobservations
are in line with prior results from meta-RL theory. However, in the pure language setting, such as
mathematical reasoning, the model uses an auto-regressive architecture with memory. Moreover, it
essentially has full control of the environment and, in theory, can induce meta-behaviors such as
backtracking and branching. In practical terms, there is no theoretical reason that the LLM cannot
produce a complex sequence of tokens, such as the Meta-CoTs described earlier. We will investigate
the presence of such artifacts next.

#### Inducing Meta-Reasoning In LLMs

Prior works have shown that complex exploration and reasoning behaviors can be induced in LLMs
through in-context demonstrations (Sel et al., 2024; Gandhi et al., 2023; Nie et al., 2024). However,
the degree to which such prompting can induce genuine meta-reasoning capabilities, particularly
for complex reasoning, remains an open question. In this section, we investigate meta-reasoning
induction through carefully constructed prompting strategies. We evaluate model performance on
the MATH test set (Hendrycks et al., 2021). Our analysis examines three key dimensions: token
3https://www.interconnects.ai/p/openais-o1-using-search-was-a-psyop
35

<!-- Page 36 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought
Figure 24: Per-problem, token-ordered attempts (n=5) analysis of solution accuracy and selfcorrection behavior. Lines indicate accuracy trajectories; bars represent frequency of explicit error
recognition.
36

<!-- Page 37 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought
Figure 25: Boxplots of completion tokens generated and scatter plots of accuracy across MATH
difficultylevels,brokendownbymodelandpromptingstrategy. Higherdifficultyproblemsgenerally
elicit longer generations. Box plots represent token distributions while dashed lines track accuracy.
Although complex strategies (e.g. Think & Verify) spend the most total tokens, the baseline prompt
consistently scales at faster percentage gains from level-to-level while accuracy lines follow similar
curves.
37

<!-- Page 38 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought
generation patterns, expressions of meta-cognitive behaviors (such as explicit error recognition), and
mathematical problem-solving accuracy. We evaluate five prompting strategies with progressively
increasing complexity:

## The Baseline strategy implements minimal instruction, directing the model to assume mathematical expertise while providing basic formatting requirements.


## The CoT strategy extends the Baseline prompt by requesting explicit step-by-step reasoning

and chain of thought verbalization.

## TheThink strategyimplementsadistinctiveapproachtomathematicalreasoningbyrequesting

stream-of-consciousness meta-cognition within explicit structural constraints. This strategy aims
to elicit authentic search by placing an inner monologue inside of a private “thinking” header,
using natural language patterns (“Hmm”, “Let me see...”, “Because of this...”) that request
self-verificationandcandemandexplicitbacktrackingonidentifiederrors. Thesedesignchoices
mimic the non-linear reasoning patterns of mathematicians approaching new problems. The
three-shot variant (Think 3-shot) augments this with examples, using a static set of in-context
demonstrations to illustrate desired behavior patterns.

## The Think & Verify prompt introduces structured iteration bounds and verification requirements through dual constraints. The prompt mandates a second-pass verification for confident

solutions while maintaining a soft maximum of six distinct solution attempts. Upon reaching a
high-confidence solution, the protocol demands one additional verification attempt. Successful
verification permits termination, though the model retains autonomy to continue exploration
within the maximum bound should it self-report uncertainty. This adaptive termination criterion functions as an in-context best-of-N approach with self-consistency based early-stopping,
optimistically balancing comprehensive solution space exploration with self-verification.
We analyze expressions of regret and self-correction across models. We define regret as explicit
acknowledgments of errors or uncertainty through phrases like "I made a mistake", "oops", "let me
reconsider", or similar language. A detailed breakdown of regret statistics across different models
and prompting strategies is provided in Table 5 in Appendix B.
The regret analysis reveals a clear distinction between basic prompting approaches and those explicitlydesignedtoencouragemeta-cognitivebehaviors. UnderbaselineandstandardCoTprompting,
which provide no explicit instruction for self-verification, models rarely express regret or acknowledge errors (<0.5% of solutions across all models), showing that behaviors like self-verification and
backtracking rarely emerge natively with standard prompting. In contrast, the Think strategy, which
explicitlyinstructsmodelsthattheycan"think,reflect,revise,backtrack,andverifyduringresponding
when it considers doing so would lead to a better solution," produces substantially higher rates of
error recognition and correction, particularly in larger models like Llama 3.1 70B (12.65%). This
effect is further amplified when combining such instruction with structured examples (Think 3-shot)
and explicit verification requirements (Think & Verify), leading to significantly increased rates of
regretexpressionacrossmostmodels,peakingat25.67%forLlama3.170BundertheThink&Verify
strategy.
Interestingly, model scale correlates with willingness to express regret, but not monotonically.
While larger Llama models show high rates of regret expression (15-25% under Think & Verify),
more advanced models like GPT-4o and Claude 3.5 Sonnet exhibit notably lower rates (1-4%).
Our main set of results is shown in Figure 25. First, to further understand how model behavior
varies across difficulty levels and prompting strategies, we analyze the relationship between token
usageandaccuracy. Theboxplotsshowtokendistributionswhileoverlaiddashedlinestrackaccuracy
across difficulty levels. Notably, more complex prompting strategies incur higher token overhead but
38

<!-- Page 39 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought
donotconsistentlytranslatethisadditionalcomputationintoproportionalaccuracygains,particularly
in higher difficulty regimes. For smaller models like Llama 3.1 8B, we observe significantly increased
tokenusageinhigherdifficultylevelsthatcorrespondswithamarkeddeclineinaccuracy. Incontrast,
larger models maintain more consistent token usage patterns across difficulty levels. The Think
& Verify approach consistently produces longer solutions across all models, reflecting the inherent
overhead of verification steps. However, this increased verbosity does not translate to improved
accuracy—particularly for smaller models where longer solutions may indicate joint struggles with
problem-solving and verification. Moreover, we see significant increases in verbosity on all problem
difficulties. Of particular interest, we find that the Think & Verify strategy leads to equivalent
accuracies on the lowest difficulty problems (for all models), while often requiring more than double
the token budget. This observation indicates that models seek to match the reasoning "style"
rather than substance and may be even faking mistakes to match the desired in-context
behaviors (Gudibande et al., 2023).
In conclusion, while sophisticated prompts successfully elicit reasoning-like behaviors absent
from baseline approaches, these behaviors - including recognizing mistakes and backtracking -
do not consistently yield performance benefits. In fact, when models engage in self-correction
and backtracking, the final answers are more likely to be incorrect. This pattern, combined
with the observation that token generation increases with MATH difficulty level across all
strategieswhileaccuracytrajectoriesremainsimilar,suggestsfundamentallimitationsinusing
explicit meta-cognitive instruction to induce robust reasoning capabilities.

## Putting It All Together - A Pipeline for System 2 Reasoning

Sofar,wehavepresentedatheoryofadvancedreasoningcapabilitiesbasedaroundsearch,aswellas
some early empirical findings. In this section we suggest an overall approach to training advanced
reasoning models. Our proposal follows the overall structure of modern post-training, consisting of
instruction-tuning and RL training (Stiennon et al., 2022; Ouyang et al., 2022).

### Instruction Tuning

InSection6.4.1,wepresentedevidencethatthecurrentgenerationofmodelscannotinduceeffective
meta-reasoning through in-context prompting, and may even exhibit misleading behaviors. Instead,
we propose to begin the process through instruction-tuning with synthetic in-context search data, in
the manner outlined in Section 4.3. We showed in Section 6.4.1 that even advanced models rarely
demonstratemeta-reasoningcapabilities,suchasexpressingregretorbacktracking. Hence,webelieve
an instruction-tuning stage is critical to endow the model with such backtracking and branching
capabilities,whicharenotfrequentlypresentinthepre-trainingcorpusorgeneralpurposeinstructiontuning data. Following the synthetic data approach in Section 4.3, we construct a training dataset
𝒟train = {q(𝑖),Z(𝑖),S(𝑖)}𝑁
𝑖=1
which represents the Meta-CoT Z = z
1
,...,z

## 𝐾

, followed by verifiable
solutionS = s,...,s . Forthisstageoftraining,multipletrainingobjectivescanbeconsidered,which
𝑛
weoutlineinAppendixC.Towhatdegreeeachofthesedifferentobjectives(andcombinationsthereof)
yield qualitatively different behaviors is an open empirical question. However, based on previous
resultsatthescaleofmodernLLMs,wehypothesizethatthe exact format of the pre-training stage
isnotcrucial,ratherthekeyperformancecontributorisRLpost-training(Yeetal.,2024b;Kumar
et al., 2024; Gehring et al., 2024).
39

<!-- Page 40 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought

### Post-Training With RL

Prior works have shown strong empirical results with multi-turn RL training (Kumar et al., 2024;
Gehring et al., 2024). We propose using a similar objective based on the E-RL2 approach outlined in
Equation 14 with the standard additional distributional constraints:
[︃ ]︃
∑︁
m
𝜃
axE
S,Z∼𝜋
𝜃
(·|q),q∼𝒟train
𝑟*(S,q)−𝛽 D

## 𝐾𝐿

[𝜋
𝜃
(z
𝑡+1

## |Z

𝑡
,q)||𝜋ref(z
𝑡+1

## |Z

𝑡
,q)] (15)
𝑡
where𝑟*istheverifiablerewardfromthesolutionand𝜋ref isareferencepolicy(usuallytheinstructiontuned model). Similar objectives have been considered in agentic applications where the "Meta-CoT"
represents an actual search over a web interface (Nakano et al., 2022; Putta et al., 2024). Note
that the reference constraint here is not strictly necessary, but likely required to keep the chain
stable and interpretable. Keeping the RL process stable over long horizons and learning robust credit
assignment is likely a significant challenge. There are a number of possible options for dealing with
these challenges:

## The step-wise branching structure of MCTS training presents one possible resolution. For

example, by using an objective similar to that proposed by Feng et al. (2024), who perform an
SFTpolicydistillationapproachusingMCTS.AlthoughingeneralSFT-basedpolicyoptimization
tends to be inefficient in language model settings (Tajwar et al., 2024).

## Anumberofstep-levelDPOobjectiveshavebeenproposed,specificallyforreasoningapplications,

whichcanbecombinedwithtree-searchbasedexploration(Xieetal.,2024;Setluretal.,2024a;
Lai et al., 2024). We believe this might be a promising direction, as DPO-based approaches
also tend to be more robust to off-policy data (Noukhovitch et al., 2024) than comparable
policy-gradient based approaches (Shao et al., 2024), which allows for massive asynchronous
RL scaling.

## A branching version of on-policy methods could also be used, such as a step-level version of

RLOO (Ahmadian et al., 2024) or VinePPO (Havrilla et al., 2024; Kazemnejad et al., 2024),
although these methods might not be as robust to off-policy data as prior options and hence
less scalable (Noukhovitch et al., 2024).
Theexactcorrelationsbetweeninstruction-tuning,pre-training,andRLareunknowninthepublic
literature. Smaller scale studies have found SFT tuning to be effective in endowing transformers
with meta-reasoning behaviors (Yang et al., 2022; Lehnert et al., 2024; Gandhi et al., 2024; Ye et al.,
2024b),whilelargerscalestudiesindicatethatpurelytrainingwithnext-tokenpredictiononsynthetic
traces might not be enough due to train-test distribution shifts and find that on-policy RL is the key
component for improving performance (Zhang et al., 2024b; Kumar et al., 2024; Gehring et al.,
2024).

#### Q* or q-STaR?

In the prior section, we introduced the RL training objective in Equation 15 using a verifier reward
𝑟*(S,q). HerewewillderiveanotherRLformulationwithaself-trainingtypeofRLobjectivewithout
the need for an external verifier.
Under the (Meta-)CoT formulation of Section 2, we can consider the Meta-CoT process Z as a
general latent variable model for the whole problem solution S. We can then apply a widely known
40

<!-- Page 41 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought
Figure 26: Left: The training loss of fitting only the oracle answer or a sequence of answers with the
revision objective in Equation 5. The model that uses in-context exploration is better able to model
the correct solution than directly outputting it after the question, consistent with our complexity
considerations in Section 2. Source: Figure 5 in Qu et al. (2024). Right: An example in which
the DeepSeek R1 model DeepSeek (2024) reaches the correct final solution (448) in its Meta-CoT
Z ∼ 𝜋 (·|q), but the summary model S ∼ 𝜋 (·|Z,q) fails and produces the wrong final solution
𝜃 𝜃
(1792).
formulation of the STaR algorithm as latent inference Singh et al. (2024):
∫︁
log𝜋data(S|q) = log 𝜋(S|Z,q)𝜋(Z|q)𝑑Z ≥ (16)
max E [log𝜋(S|Z,q)]+D [𝑞(Z|q)||𝜋(Z|q)] (17)
𝑞(Z|q) 𝐾𝐿
𝑞(Z|q)
where 𝑞(Z|q) is a variational inference function Kingma & Welling (2013), or in our case a latent
reasoner. Since all components here are auto-regressive transformers (LLMs), we can amortize them
inside a single model. Now, if we set 𝜋(Z|q) to be the prior model 𝜋ref , which is initialized as the
instruction-tuned base model (𝜋 ) from Section 7.1 and amortize the reasoning inference model
𝜃0
𝑞(Z|q) and the decoder model 𝜋(S|Z,q) into a single LLM 𝜋 we get the objective:
𝜃
m
𝜃
axE
Z∼𝜋
𝜃
(·|q),S,q∼𝒟train
[log𝜋
𝜃
(S|Z,q)−𝛽D

## 𝐾𝐿

[𝜋
𝜃
(Z,|q)||𝜋ref(Z|q)]] (18)
where we used the 𝛽−VAE formulation Higgins et al. (2017). Unlike standard VAEs though, the
parametric models here are auto-regressive transformers, which sample discrete tokens, hence we
cannotusethereparameterizationtricktocomputegradientsoftheabovedistributionandmustresult
to RL optimization. This objective indeed looks similar to the main RL objective from the previous
section, as formulated in Equation 15, but with a few key differences. First, the reward function is
represented as
𝑟(S,q) = log𝜋 (S|Z,q) (19)
𝜃
wherethesolutionSisnolongersampledon-policyfromthemodel,butfromapre-existingquestionsolution training dataset. Hence the sampling expectation from the policy is only over the latent
Meta-CoT. Notice also that the reward itself is a function of the model parameters 𝜃, which then
requires a modification to the standard policy gradient approach. With some simple differentiationby-parts calculus, the above objective can be represented as:
41

<!-- Page 42 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought
m
𝜃
axE
Z∼𝜋
𝜃
(·|q),S,q∼𝒟train
[sg(log𝜋
𝜃
(S|Z,q))−𝛽D

## 𝐾𝐿

[𝜋
𝜃
(Z,|q)||𝜋ref(Z|q)]]+ (20)
maxE [log𝜋 (S|Z,q)]
𝜃
Z∼sg(𝜋
𝜃
(·|q)),S,q∼𝒟train 𝜃
HerethefirstequationisnowastandardRLproblemwithrewardasdefinedinEquation19which
can be optimized with the standard methods, outlined in Section 7.2. The second part is a maximum
likelihood training of the Meta-CoT "summarization" model on the ground-truth solution. Essentially
the goal of this training objective is to make the conditional model 𝜋 (S|Z,q) more expressive than
𝜃
the standard training objective 𝜋 (S|q). Some empirical evidence from Qu et al. (2024) supports
𝜃
this hypothesis as shown in Figure 26 (left) which shows training curves for the revision objective
in Equation 5. Indeed, even with standard SFT using in-context exploration the model achieves
significantly lower loss than directly predicting the correct answer. This is similar in spirit to the goal
ofQuiet-STaRZelikmanetal.(2024),withthedifferencebeingthatweoptimizeandmarginalizeover
the entire latent meta-reasoning process and final solution with arbitrary complexity. In comparison
Quiet-STaR applies the above objective at a token-level with fixed token budget for the latent process,
thusessentiallymakingthetransformercomputationgraphdeeper,similarlytoUniversalTransformer
Dehghanietal.(2019),ratherthanoptimizingmeaningfulsemanticreasoning. Thislineofreasoning
is also consistent with the complexity arguments outlined in Section 2.
Finally, we should note that while this approach does not utilize verifiers for RL training, it
still needs to bootstrap the latent reasoning processes Z, which still requires verifiable outcomes to
generate high-quality synthetic training data.
The objective in Equation 20 has one major advantage that we no longer require verification of
the final solution, since the training objective only requires a dataset of question-solution pairs. This
allows us to train on open-ended and hard to verify problems, such as proofs and general reasoning.
Thedownsideisnowthatthemodel𝜋 (S|Z,q)isonlyessentiallytrainedwithsupervisedfine-tuning
𝜃
and does not get on-policy reward feedback, which may be sub-optimal. If the Meta-CoT process can
find a solution with high certainty, then perhaps an SFT training objective for the summarization
model is sufficient, which is an empirical question. Anecdotally, we have observed instances of the
DeepSeek R1 model DeepSeek (2024) finds the correct answer in its Meta-CoT but actually outputs
the wrong final solution as shown in Figure 26 (right).

#### Discount Rates

While standard RLHF pipelines have not used discount rates in the past, they may be required in
reasoning applications. Recent works have discovered that small biases in preferences for longer
answers are routinely exploited by reward models in RL pipelines, which has yielded significantly
more verbose models (Singhal et al., 2023; Park et al., 2024). These issues are present even in
strong systems, such as GPT-4 (OpenAI, 2023) and require explicit regularization. As demonstrated
in prior chapters, when increased sampling correlates with higher accuracy then, without explicit
regularization, the model can choose to continue generating/searching for solutions or collapse on
some majority voting approach with potentially unlimited inference targets. Indeed, recent work
Chenetal.(2024)foundthatadvancedreasoningmodelscangeneratesignificantlylongersequences
even for simple problems ("What is 2+3=") as shown in Figure 27. The Qwen QwQ model (Team,
2024) generates up to 13 solutions in context before providing a final answer. To mitigate this issue,
we might require a modification of the RL objective from Equation 15, to use a discounted objective
[︃ ]︃
∑︁
m
𝜃
axE
S,Z∼𝜋
𝜃
(·|q),q∼𝒟train
𝛾|Z|𝑟*(S,q)−𝛽 D

## 𝐾𝐿

[𝜋
𝜃
(z
𝑡+1

## |Z

𝑡
,q)||𝜋ref(z
𝑡+1

## |Z

𝑡
,q)] (21)
𝑡
42

<!-- Page 43 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought

## Prm-Q7086


## Prm-Q3000


## Prm-Q500


### Oracle

Majority
𝛾=1
𝛾=0.995
𝛾=0.99
Figure 27: Left: Figure 17 with discounted objective. The undiscounted version of Best-Of-N sees
continued improvement with additional sampling, while the discounted objective exhibits a humpshaped frontier. Right: Token lengths for answers of "what is 2+3=?" by different models. Source:
Figure 1 in Chen et al. (2024).
fiwhere𝛾 < 1. Thisobjectivewould(intheory) force themodelto trade-off computeversuscertainty
in its response. This effect is demonstrated in Figure 27 (left), which shows a discounted version of
thebest-of-Nobjective. Withoutaparticularpenaltyonthegenerationbudget,performanceincreases
steadily with additional compute, which may push the model to continuously increase the inference
budget (as compared to base models) as shown on the right. If we consider the discounted reward
(accuracy) instead, we see a hump-shaped objective as there is a stronger trade-off between verifier
confidence and the generation budget.
This also raises an interesting trade-off on controlling model behaviors in terms of inference/accuracy. We might be interested in forcing a particular trade-off depending on problem difficulty.
Consider then a distribution over discount rates 𝛾 < ... < 𝛾 . We can also associated an individual
1 𝑚
language prompts p with each discount rate such as "Work as quickly as possible" for high discount,
𝛾
to "Take as much time as needed" for a low discount rate. Then, at train time we can optimize the
objective
[︃ ]︃
m
𝜃
axE
S,Z∼𝜋 𝜃 (·|q,p𝛾𝑖 ),q∼𝒟train,𝑖∼1:𝑚
𝛾
𝑖
|Z| 𝑟*(S,q)−𝛽 ∑︁ D

## 𝐾𝐿

[𝜋
𝜃
(z
𝑡+1

## |Z

𝑡
,q,p
𝛾𝑖
)||𝜋ref(z
𝑡+1

## |Z

𝑡
,q)]
𝑡
Then, at inference time we can control the qualitative model behavior through conditioning on the
prompttotrade-offinferencecomputeversusaccuracy.Schultzetal.(2024)showedthataifwetrain
a model on MCTS search traces with different parameters, at inference time we can condition the
model on a particular parameter configuration and recreate the qualitative behaviors(as shown in
Figure9). Asdiscussedearlier,simplesupervisedfine-tuningmaynotbesufficienttoinduceadvanced
reasoning capabilities (and likely even more difficult to do so in a controllable way), however, these
resultsdemonstratepromiseininducingcontrollablebehaviorsintothemodelthroughtheconditional
prompting objective above.

## Going Forward

Public open-research/source progress on reasoning models is currently bottle-necked by three main
issues:
43

<!-- Page 44 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought

## Access to resources in terms of both data and compute as these algorithms require significant

amount of both.

## Open-source infrastructure for large scale inference and training is currently lackluster.


## Algorithmic exploration - we have a lot of avenues to explore and only limited people and

resources actively working on the right directions.
We expand on these issues in this section.

### The "Big MATH" Project

While compute bottlenecks are a persistent issue in open research, we found the lack of open
datasetswithverifiablereasoningproblemstobeanevenbiggerchallenge. Priorworkshaveusedthe
GSM8k (Cobbe et al., 2021) and MATH (Hendrycks et al., 2021) datasets, but the first has largely
been saturated by the current generation of models and the second is quite limited, with only 12,000
problems. To overcome these challenges, we have put significant work into the "Big MATH" project
- an effort to aggregate over 1,000,000 high-quality, high-confidence, and diverse verifiable math
problems. We combine existing datasets with significant post-processing, as well as efforts to acquire
additional data from novel sources. We outline this below.
Ourproposedtrainingpipelinerequiresalarge-scalecorpusofchallengingpromptswithverifiable
answers, but developing such datasets presents fundamental constraints in automated verification
andassessmentofreasoningcapabilities. Inmanydomains,solutionsaretoounstructuredornuanced
for automated verification: a single objective answer may not exist, correct solutions can appear in
equally valid but textually distinct forms, and certain tasks (e.g. complex proofs) resist reduction
to deterministically verifiable outputs with a single canonical representation. These issues make
automated grading infeasible. Even in contexts where problem-answer pairs can be constructed
and easily verified, these formats may reduce to factual retrieval rather than exercises that require
reasoning capabilities.
As evidenced by the wide array of literature discussed in previous sections, mathematics offers
a stable ground truth for correctness, naturally programmatic answer grading, and existing public
datasetsinproblem-solution-answerformat. Whilewerecognizesignificantpotentialinmanydomains
(e.g.,programming,diagnostics,finance,analysis)wherestructuredreasoningpathscanbevalidated,
the substantial resources required to construct and verify such datasets, particularly without access
to proprietary data, makes them impractical for our immediate objectives. While the availability
of existing datasets ultimately drove our domain selection, even these openly available resources
are constrained in both scale and distribution. We face the critical challenge of distinguishing
between computational and pattern proficiency and conceptual understanding when assessing model
capabilities-adistinctionthatfundamentallyshapesourdatasetrequirementsandevaluationmetrics.
To guide our data construction, we define three core criteria:
1. the existence of uniquely verifiable solutions, meaning that problems must admit a single
correct answer that can be reliably verified;
2. open-ended problem formulations, ensuring that tasks cannot be easily solved by guessing
(as might occur in multiple-choice formats) and instead require nontrivial reasoning steps; and
3. closed-form solutions, such that the final answer must be expressible in a closed form (e.g., a
scalar or formula, not a proof), thereby enabling automated evaluation.
These criteria reveal significant limitations in existing datasets. Those that meet our structural
requirements remain severely limited in scale, containing orders of magnitude fewer examples than
44

<!-- Page 45 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought
we estimate necessary for model training. Within the structured collections, we observe a concerning
scarcity of non-trivial problems that effectively challenge reasoning capabilities, with many examples
simply testing computational abilities or following predictable patterns. Perhaps most problematic
is the non-negligible proportion of incorrect problem-solution labels, even in widely-used datasets,
introducing substantial complexity to data cleaning.
Preliminary analysis of one of the largest available datasets, NuminaMath (LI et al., 2024),
exemplifies these issues. Basic verification shows that out of roughly 860,000 entries, more than
42,500areduplicates(∼5%ofthedataset). Further,while89.7%ofentriescontainexactlyoneclearly
boxedsolutionsuitableforautomatedverification,2.6%containnoboxedsolution,and7.7%include
multiple boxed solutions. Problems like this underscore the state of open and publicly available data
and suggest deeper quality concerns.

#### Data Sourcing

We consider multiple established mathematical problem datasets that are commonly used in the
literature(Table3). First,weincludetheHumanAnnotatedReasoningProblems(HARP)dataset(Yue
etal.,2024),containingnearly4,800competition-levelshortanswerproblemswithprogrammaticallycheckable answers. Next, we use the NuminaMath (LI et al., 2024) dataset, which is composed of
roughly860,000problemsfromavarietyofbenchmarksandsources: Chinesehighschoolmathexercises,matholympiad-stylecompetitionproblems,theartofproblemsolvingforum,MATH(Hendrycks
etal.,2021),andGSM8k(Cobbeetal.,2021). NuminaMathfurtherincorporatessyntheticdatafrom
the synthetically generated dataset Orca-Math (Mitra et al., 2024) as well as further generating a
significantamountofsyntheticdatabasedontheMATHdatasetandasubsetofthemathcompetition
problems. Additionally,whileNuminaMathusestheoriginalsplitoftheMATHdataset(7,000training
problems, 5,500 test problems), we choose to use version with 12,000 training problems and 500
test problems, as originally proposed by (Lightman et al., 2023). We incorporate the Omni-MATH
dataset (Gao et al., 2024), contributing almost 4,500 olympiad-level problems curated from 39
different competition websites. Notably, this dataset employs professional annotators and verifiers to
maintain solution-answer quality. Finally, we include OpenMathInstruct-2 (Toshniwal et al., 2024),
composed of about 607,000 synthetically generated problems. Toshniwal et al. (2024) use Llama3.1-
405B (Dubey et al., 2024) in a multi-step data augmentation pipeline which they seed using the
GSM8k (Cobbe et al., 2021) and MATH (Hendrycks et al., 2021) datasets.
Beyond drawing from these established datasets, we maintain an active data collection initiative
that extends our corpus through manual curation of competition-level problems. This effort has
already contributed thousands of additional olympiad-style problems and continues to grow. Our
manual collection process focuses on acquiring mathematically rigorous content from competition
archives, olympiad materials, and historical sources not present in existing datasets.

#### Data Filtering

To create datasets with which we can train a model in our training pipeline, we next clean and filter
the data from each source using a combination of bespoke and common strategies (Albalak et al.,
2024). Specifically for our two-stage pipeline, we create two versions of the dataset. First, we have
the base filter, where the data will be used during SFT for the model to learn (1) an approximation
of the distribution of math problems and (2) to follow the desired chain-of-thought format. Next,
the strict filter is intended to be used for the Meta-RL training stage. Thus, the strictly filtered data
should contain only problems that closely follow our three desired properties: open-ended, verifiable,
closed-form problem-solution pairs.
45

<!-- Page 46 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought
Data Source Original Base Filter Strict Filter

### HARP (Yue et al., 2024) 4,780 3,691 2,996

NuminaMath (LI et al., 2024) 859,608 452,820 231,887

### Omni-MATH (Gao et al., 2024) 4,428 3,660 2,478

OpenMathInstruct-2 (Toshniwal et al., 2024) 607,324 600,191 496,331

### Total 1,476,140 1,060,362 733,692

Table 3: Comparison of Problems by Data Source and Filter Type
The Base Filter performs some operations that are unique to each subset, and some operations
that are shared across the full collection of data. First, in the HARP dataset (Yue et al., 2024), we
find many problems that contain figures in the Asymptote4 vector graphics language, which we
filter out of the dataset. Next, we filter the NuminaMath dataset (LI et al., 2024). This dataset
contains a significant amount of synthetic data, which is often difficult to verify for accuracy and
correctness. However, the Orca-Math (Mitra et al., 2024) subset has empirically been proven to
improve performance on supervised fine-tuning, and for this reason, we elect to maintain only
the Orca-Math data, while discarding the other synthetic subsets. Next, NuminaMath does not
explicitlycontainanswerstoeachproblem,soweextractanswerstoproblemsbysearchingforboxed
solutions (“\boxed{}” in LaTeX). Any problems whose solution does not contain exactly 1 boxed
answer is filtered out. When exploring Omni-MATH (Gao et al., 2024), we found many problems
containing author attributions (e.g. a person’s name in parenthesis) and removed the attributions
from the problem. OpenMathInstruct-2 originally contains multiple solutions and final answers to
each problem (Toshniwal et al., 2024). The first step we take is to group all matching problems
together, removing those which have mismatched expected answers. Next, we found that the data
still contains evidence of the synthetic data generation process, such as asking “do you want to solve
it?” or “here’s the new problem” and remove any problems with similar phrases.
Finally, after running each of the described filters over the individual subsets, we perform four
filteringoperationsacrossthefullcollection. First,weuseexactmatchingtofindandremoveduplicate
problems. Then, we use a FastText language identifier (Joulin et al., 2016b,a; Grave et al., 2018)
and remove any problems where English is not the primary language. Next, we remove problems
containingahyperlink,asthissuggeststhatamodelmaynothavethefullresourcesrequiredtosolve
the problem. Lastly, we decontaminate the dataset by removing any examples of the MATH500 test
set (Lightman et al., 2023).
The Strict Filter further reduces the base filtered data to problem-answer pairs which are more
likelytobeopen-ended,verifiable,andclosed-form. Thestrictfiltersareappliedequallytoallsubsets
of the dataset through a mix of rule-based and model-based filtering. First, we remove questions
containingmultiplepartsasthesecanbechallengingtoevaluate. Forasimilarreason,wealsoremove
questions that ask for a proof as these problems are difficult to evaluate. Next, we choose to remove
multiple choice problems as models have a high probability of selecting the correct answer without
producing an accurate reasoning chain. For the same reason, we also remove Yes/No and True/False
problems, as these may give a poor learning signal during Meta-RL training. Finally, we use the
SemDeDupalgorithm(Abbasetal.,2023)withthemodelatsentence-transformers/all-MiniLM-L6-v2
and remove problems with a cosine similarity over 0.5.

### Infrastructure

For the proposed family of algorithms we need RL training infrastructure that can:
4https://asymptote.sourceforge.io/
46

<!-- Page 47 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought

## Scale to multiple nodes in a straightforward way


## Allow for high-performance inference throughput


## Allow for interleaving inference and training efficiently for online RL algorithms

Hereweoutlineourrecentprogressontheseissuesintheopen-sourceGPT-NeoXframework(Andonian et al., 2023). We leverage CUDA IPC handles to enable true asynchronous RLHF training by
sharing GPU memory directly between training and inference processes. By allocating model weights
in the training framework and sharing CUDA
memorypointerswiththeinferenceframework,
both processes maintain access to the same
physical memory throughout training. When
the training process updates weights, these updates are immediately visible to the inference
process through its mapped pointers without
requiring any explicit synchronization. This
shared memory architecture enables fully parallel execution - the inference process can continuously generate tokens while the training
process updates weights, with neither process
blocking the other. Although early portions
of generated rollouts may be off-policy, the final steps will generally be only one training
step off-policy at most, as the inference process
immediately sees weight updates through the Figure 28: Async training versus slightly off policy
shared memory. Unlike previous asynchronous methods that require dedicated weight synchroapproaches (Noukhovitch et al., 2024) that re- nization
quire distinct generation and training phases,
our system maintains constant GPU utilization across both processes. Direct memory sharing provides significantly higher throughput by eliminating synchronization overhead between training and
inference. Our initial experiments show 40% improved throughput compared to 3-step asynchronous
training that requires explicit weight synchronization, as shown in Figure 28. However, this approach
comes with important trade-offs in memory utilization and parallelism. Sharing GPUs between
processes restricts us to suboptimal tensor parallelism (TP) configurations compared to dedicated
training and inference setups, resulting in lower theoretical peak throughput for both processes. The
impactisparticularlypronouncedforinference,wherereducedmemoryforKVcacheandsuboptimal
TP configurations significantly constrain the generation speed. In scenarios where inference compute
significantly exceeds training compute (e.g. MCTS, where most of the search tree is discarded after
each rollout), using separate dedicated GPU clusters with optimized TP configurations for each
process can achieve higher overall throughput despite the synchronization overhead.

### Open Research Questions

A number of open research questions remain which are currently not answered in the literature.

#### Open-Ended Verification And CoT Faithfulness

In this report we outline a pipeline for training advanced reasoning models on verifiable questions.
These types of questions largely consist of things like math, scientific questions with symbolic or
numerical answers, or code problems with unit tests. However, we believe it is still an open question
47

<!-- Page 48 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought
Figure 29: Under a fixed generator model and a variable verifier performance seems to also obey
a form of a scaling law. Right: Accuracy seems to improve in a log-linear fashion with amount of
training data under a standard discriminative PRM. Source: Figure 6 in (Setlur et al., 2024c). Left:
Performance of a Generative Reward Model (with CoT) on reasoning tasks with a a reference using
variable amount of CoTs and majority voting. Increasing the amount of inference-time sampling
improves accuracy. Source: Figure 5 in (Mahan et al., 2024).
on how to ensure that the resulting CoTs are faithful and in fact provide valid reasoning. In many
applications, such as science for example, the reasoning chain can be even more important than
the final answer. Qualitatively, current models with “advanced” reasoning still struggle and produce
many CoTs which are inconsistent or unfaithful, even when they obtain the correct final answer.
Interestingly, even the single math example provided along with the announcement of the O1
model has an incomplete solution as it makes an unsubstantiated assumption on the form of the
polynomial ℎ(𝑥) = 𝑥2 −𝑐 without proving that the coefficient of 𝑥 is in fact zero (OpenAI, 2024).
Under a competitive setting this would likely receive 5/7 points, even though the final answer is
correct. Itisworthnotingthatthemodelactuallyverifiesandprovesthisassumptioninit’sMeta-CoT
butthefinaloutputprovideddoesnotincludethosesteps. Webelievethismightbeonetypeofartifact
that arises from training with final answer verification only. How to provide rewards on full CoTs
and open-ended problems such as proofs remains an open question. Under the assumption of a wide
enough generation-verification gap, we believe an RLAIF approach could be promising. In particular,
foregoing concepts such as formal verification, one avenue to explore is a “generative verifier” similar
to Zhang et al. (2024a) or Mahan et al. (2024). In this setting the evaluation model can be provided
with one or several reference solutions/proofs, or other relevant material such as textbook chapters,
tools like Wolfram or Mathematica, and specifically fine-tuned to provide evaluations to proposed
solutions, rather than final answers alone. As outlined in Section 3.2, we found advanced models
to already posses some capabilities in that vein. Unfortunately, a major bottleneck in that line of
research is the need for a dataset of open-ended reasoning problems (such as proofs), which would
likely require significant human annotations.

#### Process Guidance And The Verifier Gap

Thecurrentworkbringstolightsomeremainingquestionsontheapproachestoprocessguidanceand
PRMS. In Section 5 we outlined results showing that pre-trained PRMs still significantly lack behind
pure Monte Carlo approaches in terms of search efficiency. Moreover, with few exceptions (Setlur
et al., 2024c), we believe algorithmic approaches for training these models remain understudied. In
particular,ifweviewaPRMasavaluefunction,thenmanyapproachesfromofflineRL(Levineetal.,
2020)becomeapplicablewithsomealreadyshowingpromiseinagenticdomains(Zhouetal.,2024b).
In the same vein, Silver et al. (2016) introduced a separate value function over the standard MCTS
48

<!-- Page 49 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought
approach using roll-outs for efficiency purposes. However, we believe there may be a fundamental
verifier gap beyond just the efficiency question. As shown in Figure 3 there remains a significant
gap between the "best-of-N" verifier driven approach and the oracle pass@N performance. A similar
gap seems to exist in the multi-turn code generation domain, as shown in Figure 22 (Gehring et al.,
2024). Moreover, under a fixed generator, results from Setlur et al. (2024c) and our own empirical
findings in Section 5 indicate that verifier performance may also be driven by a scaling law as
well. In Figure 29 (left) we see clear log-linear scaling in performance in terms of training data. One
hypothesis is that verification is also a matter of computational complexity, which is why allowing
verifiers to use CoT improves performance as shown in Figure 3 (Zhang et al., 2024a; Mahan et al.,
2024). In addition, Mahan et al. (2024) show further inference-time scaling for verifiers, as using
additional CoTs with majority vote improves reward accuracy on reasoning problems well beyond
the performance of the standard discriminative verifier. This raises questions for the fundamental
learnabilityofin-contextsearchtraces. Inessence,ifasearchtracewasgeneratedusingground-truth
verification or Monte-Carlo roll-outs, the resulting sequence may have significant implicit complexity,
which would be challenging for the model to learn. This would also motivate incorporating further
self-evaluationorreflectionintoreasoningchains. Theassociatedverificationscalinglawsanddesign
choices remain largely unexplored in the literature and present an important research direction.

#### Scaling Laws For Reasoning And Search

While recent model releases have demonstrated strong inference scaling performance, we still lack a
thorough scientific exploration of scaling laws in public research, which is a key piece of the recently
emerging model paradigm.

## The scaling laws of search presented by Jones (2021) have not been publicly evaluated

on realistically challenging reasoning applications with LLMs. While the results from Feng
et al. (2024) show promise, they are still limited and partial. Obtaining a more thorough
evaluation on joint policy and verifier scaling will provide clarity to current research questions.
So far, unfortunately, the research community has been limited by a lack of data and scalable
infrastructure.

## Exploration of search approaches remains a very under-studied topic. As discussed in Section 4.4, it appears that current reasoning models all implement different approaches to search,

which leads to qualitatively different behaviors based on the search strategies presented in
Section 4.3. Given a strong trained verifier, what are the performance effects of different
search strategies such as BFS/DFS-V, A*, MCTS, etc.? Furthermore, the relationship between
exploration strategies at training and test time is an important direction of future study.

## Thetrade-offsbetweeninstruction-tuningandRLremainunclear. AsdiscussedinSection6,

it appears that standard instruction tuning can endow models with meta-reasoning capabilities
in small/simple domains, but these results do not scale, and realistic applications require
significant on-policy RL. Is this a fundamental issue with distribution shift, or is performance
driven by another relationship, similar to the trade-offs discovered by Setlur et al. (2024a)?

## The fundamental missing piece of the current inference time scaling law discussion is the

performanceoftheproposedin-contextsearchstrategycomparedwithanexplicitsearch-based
method. Intheory,thepost-trainingapproachoutlinedinSection7candiscovernovelreasoning
approaches (algorithms) that solve fundamentally new classes of problems unsolvable under
any search budget by a standard search approach. While there is clear evidence of the efficiency
of in-context search (fewer tokens per interaction), it is unclear whether the current generation
ofmodelshaveanyemergentcapabilitiesyet. Insimplestterms,dostrongreasoningmodelsshift
the compute-accuracy curve to the left or up?. As outlined in Section 6.4, current evidence in the
open literature for emergent capabilities remains weak.
49

<!-- Page 50 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought

#### Meta-Search/Search 2

In this report we argued that advanced reasoning should incorporate in-context search, which can
yield higher efficiency and potentially more advanced capabilities in reasoning tasks. However, such
anapproachalsohaspotentialdownsides. In particular, wearelimited bythemodel’scontextlength,
whichinducesfundamentallimitsonthesearchcomplexity. Moreover,thesequentialnatureofin-context
searchcanmaketheprocessslow,limitingthepower
ofthesemodels. Atthesametimeneitheroftheseare
issueswithclassicalsearchapproachessuchasMCTS,
whichcanbeparallelizedLiuetal.(2020). Anatural
question is: can we can build an additional search
procedureontopofanadvancedreasoningmodel(a
processwhichwecallMeta-SearchorSearch2followingthenamingconventionofDuanetal.(2016))? In
recent literature, Anonymous (2024) trained a value
function (PRM) with a “multi-turn” approach, conditioning the value function on all prior explored solutions. Ratherthanthetraditionalvaluefunction,they Figure 30: Scaling performance of search
insteadtrainafunction𝑣 (Z ,S ,q),wheretheMeta- with"meta"-valuefunctionandregular(single
𝜃 t 𝑡
CoT Z consists of prior solution attempts. The em- turn) value function. Conditioning the model
𝑡
pirical performance of their method compared with on prior explored paths improves search efregular PRM training is shown in Figure 30, demon- ficiency. Source: Figure 5 in Anonymous
stratingimprovedscalingovertraditionalvaluefunc- (2024).
tion training. This result suggests that we may be
able to increase the search efficiency using a meta-critic, however this remains an open empirical
question. If this is indeed the case, it would allow us to also massively scale online search with
reasoning models.

#### Reasoning with External Tools

0.9
0.8
0.7
0.6
0.5
0.4
0.3
0.2
20 21 22 23 24 25 26
Number of samples
ycaruccA

### Building on our discussion of scaling laws and

search approaches, we investigate a critical direction: augmenting model reasoning with ex- AIMO_AMC
ternal computational tools. Just as humans Majority Vote (TIR)

### Best of N (TIR)

leverage calculators, spreadsheets, and special- Majority Vote (CoT)

### Best of N (CoT)

izedsoftwaretosolveproblemsmoreefficiently,
LLMscanpotentiallyachievebetterscalingproperties by offloading the compute burden to external tools - requiring less training data during SFT and fewer samples during test-time
searchtoreachthehighlevelofperformance.

### Forinstance,whilepureCoTreasoningrequires

models to perform all calculations internally to
solve math problems, these computations can
beoffloadedtoaPythoninterpreter. Priorworks
demonstratethatsuchtool-integratedreasoning
Figure 31: Scaling curves for a Tool Integrated
(TIR) improves performance on mathematical
Reasoning(TIR)model,trainedon100Kproblems,
questions(LIetal.,2024;Yinetal.,2024;Chen
and a Chain-of-Thought (CoT) model trained on
etal.,2022). However,thescalingpropertiesof
400K problems on the First AIMO Prize, using an
oracle verifier.
50

<!-- Page 51 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought
TIR remain unexplored.
Figure 31, using models trained by LI et al.
(2024), provides initial evidence for the efficiency of TIR models. Despite being fine-tuned on 25% as much data, the TIR model demonstrates
superior scaling properties compared to the CoT model. This occurs across all sample sizes, with
both majority vote and Best-of-N strategies consistently outperforming their CoT counterparts. The
efficiencygainisparticularlyevidentinthelow-sampleregime(20 to23 samples),whereTIRachieves
nearly double the accuracy of CoT methods. This suggests that offloading computations to external
tools significantly improves the model’s ability to solve problems even with limited attempts, and TIR
is more efficient at both training and inference time.
Based on these promising initial results, we identify several critical directions for future investigation:

## Scaling laws and search strategies: We need to systematically study the scaling properties of

different search methods (e.g., BFS, DFS, 𝐴* 5, MCTS) in Tool-Integrated Reasoning models.

## Verification scaling: The role and scaling properties of the verifier in TIR settings remains

under-explored - what is the relation between training data for the verifier, verifier accuracy,
and policy accuracy?

## Internal reasoning vs reasoning with external tools: While our initial results show TIR’s

efficiency advantages, we need to better understand the fundamental trade-offs between these
approaches. When does offloading computation to external tools provide the most benefit
compared to pure language reasoning? How do these trade-offs change with model scale and
problem complexity?

## Conclusion

In this position paper, we have introduced Meta Chain-of-Thought (Meta-CoT) as a framework for
understanding and enhancing the reasoning capabilities of Large Language Models (LLMs). We have
argued that traditional Chain-of-Thought does not fully represent the underlying data generative
process on reasoning problems. By incorporating the concepts of search, verification, and iterative
refinement, Meta-CoT provides a more complete model of the cognitive processes required for
advanced problem-solving.
We believe that Meta-CoT represents a promising path towards more robust and generalizable
reasoning in LLMs. The observed behaviors of state-of-the-art models, along with our experiments on
in-contextexplorationandbacktracking,lendsupporttothehypothesisthatinternalsearchprocesses
arecrucialforperformanceoncomplextasks. Furthermore,theproposedtrainingpipelinepresentsa
concrete approach for developing LLMs with enhanced Meta-CoT capabilities. Future work should
validate the efficacy of our proposed pipeline.
Beyondourproposedmethod, numerous openquestionsandchallengesremain. Furtherresearch
is needed to determine the optimal scaling laws for reasoning and search, to develop more effective
processsupervisionandverificationtechniques,andtoclarifytheinterplaybetweeninstructiontuning
and reinforcement learning for meta chain of thought reasoning. The "Big MATH" dataset we have
introduced aims to support this research by providing a large-scale resource for training reasoning
models. Furthermore, the possibility of meta-RL paired with Meta-CoT automatically discovering
novel search algorithms is a particularly intriguing open research question for future work to explore.
5AnexampleBest-FirstsearchtracewithTIRisavailableinSectionE.
51

<!-- Page 52 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought

## Acknowledgments

WewouldliketothankAviralKumar, BenjaminEysenbach,NathanLambert,RishabhAgarwal,Sasha
Rush and Noah Goodman for the fruitful discussions and feedback on this report.
52

<!-- Page 53 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought

### References

Amro Abbas, Kushal Tirumala, Dániel Simig, Surya Ganguli, and Ari S. Morcos. Semdedup: Dataefficientlearningatweb-scalethroughsemanticdeduplication,2023. URLhttps://arxiv.org/
abs/2303.09540.
Arash Ahmadian, Chris Cremer, Matthias Gallé, Marzieh Fadaee, Julia Kreutzer, Ahmet Üstün, and
Sara Hooker. Back to basics: Revisiting reinforce style optimization for learning from human
feedback in llms. arXiv preprint arXiv:2402.14740, 2024.
Alon Albalak, Yanai Elazar, Sang Michael Xie, Shayne Longpre, Nathan Lambert, Xinyi Wang, Niklas
Muennighoff, Bairu Hou, Liangming Pan, Haewon Jeong, Colin Raffel, Shiyu Chang, Tatsunori
Hashimoto, and William Yang Wang. A survey on data selection for language models, 2024. URL
https://arxiv.org/abs/2402.16827.
Alex Andonian, Quentin Anthony, Stella Biderman, Sid Black, Preetham Gali, Leo Gao, Eric Hallahan,
Josh Levy-Kramer, Connor Leahy, Lucas Nestler, Kip Parker, Michael Pieler, Jason Phang, Shivanshu
Purohit, Hailey Schoelkopf, Dashiell Stander, Tri Songz, Curt Tigges, Benjamin Thérien, Phil Wang,
and Samuel Weinbach. GPT-NeoX: Large Scale Autoregressive Language Modeling in PyTorch,

## URL https://www.github.com/eleutherai/gpt-neox.

Anonymous. Improving the efficiency of test-time search in LLMs with backtracking. In Submitted
to The Thirteenth International Conference on Learning Representations, 2024. URL https://
openreview.net/forum?id=hJ2BCYGvFg. under review.
Jacob Beck, Risto Vuorio, Evan Zheran Liu, Zheng Xiong, Luisa Zintgraf, Chelsea Finn, and Shimon
Whiteson. Asurveyofmeta-reinforcementlearning,2024. URLhttps://arxiv.org/abs/2301.
08028.
Bradley Brown, Jordan Juravsky, Ryan Ehrlich, Ronald Clark, Quoc V Le, Christopher Ré, and Azalia
Mirhoseini. Large language monkeys: Scaling inference compute with repeated sampling. arXiv
preprint arXiv:2407.21787, 2024.
Wenhu Chen, Xueguang Ma, Xinyi Wang, and William W Cohen. Program of thoughts prompting: Disentangling computation from reasoning for numerical reasoning tasks. arXiv preprint
arXiv:2211.12588, 2022.
Xingyu Chen, Jiahao Xu, Tian Liang, Zhiwei He, Jianhui Pang, Dian Yu, Linfeng Song, Qiuzhi Liu,
Mengfei Zhou, Zhuosheng Zhang, Rui Wang, Zhaopeng Tu, Haitao Mi, and Dong Yu. Do not think
thatmuchfor2+3=? ontheoverthinkingofo1-likellms,2024. URLhttps://arxiv.org/abs/
2412.21187.
KarlCobbe,VineetKosaraju,MohammadBavarian,MarkChen,HeewooJun,LukaszKaiser,Matthias
Plappert, Jerry Tworek, Jacob Hilton, Reiichiro Nakano, Christopher Hesse, and John Schulman.
Training verifiers to solve math word problems, 2021. URL https://arxiv.org/abs/2110.
14168.
DeepSeek. Deepseek-r1-lite-previewisnowlive: unleashingsuperchargedreasoningpower!,112024.
URL https://x.com/deepseek_ai/status/1859200141355536422. Posted on X (formerly
Twitter).
Mostafa Dehghani, Stephan Gouws, Oriol Vinyals, Jakob Uszkoreit, and Łukasz Kaiser. Universal
transformers, 2019. URL https://arxiv.org/abs/1807.03819.
53

<!-- Page 54 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought
Yan Duan, John Schulman, Xi Chen, Peter L. Bartlett, Ilya Sutskever, and Pieter Abbeel. Rl2: Fast
reinforcement learning via slow reinforcement learning, 2016. URL https://arxiv.org/abs/
1611.02779.
Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey, Abhishek Kadian, Ahmad Al-Dahle, Aiesha
Letman, Akhil Mathur, Alan Schelten, Amy Yang, Angela Fan, Anirudh Goyal, Anthony Hartshorn,
Aobo Yang, Archi Mitra, Archie Sravankumar, Artem Korenev, Arthur Hinsvark, Arun Rao, Aston
Zhang, Aurelien Rodriguez, Austen Gregerson, Ava Spataru, Baptiste Roziere, Bethany Biron, Binh
Tang, Bobbie Chern, Charlotte Caucheteux, Chaya Nayak, Chloe Bi, Chris Marra, Chris McConnell,
Christian Keller, Christophe Touret, Chunyang Wu, Corinne Wong, Cristian Canton Ferrer, Cyrus
Nikolaidis, Damien Allonsius, Daniel Song, Danielle Pintz, Danny Livshits, David Esiobu, Dhruv
Choudhary, Dhruv Mahajan, Diego Garcia-Olano, Diego Perino, Dieuwke Hupkes, Egor Lakomkin,
Ehab AlBadawy, Elina Lobanova, Emily Dinan, Eric Michael Smith, Filip Radenovic, Frank Zhang,
Gabriel Synnaeve, Gabrielle Lee, Georgia Lewis Anderson, Graeme Nail, Gregoire Mialon, Guan
Pang, Guillem Cucurell, Hailey Nguyen, Hannah Korevaar, Hu Xu, Hugo Touvron, Iliyan Zarov,
Imanol Arrieta Ibarra, Isabel Kloumann, Ishan Misra, Ivan Evtimov, Jade Copet, Jaewon Lee, Jan
Geffert, Jana Vranes, Jason Park, Jay Mahadeokar, Jeet Shah, Jelmer van der Linde, Jennifer
Billock, Jenny Hong, Jenya Lee, Jeremy Fu, Jianfeng Chi, Jianyu Huang, Jiawen Liu, Jie Wang,
Jiecao Yu, Joanna Bitton, Joe Spisak, Jongsoo Park, Joseph Rocca, Joshua Johnstun, Joshua Saxe,
Junteng Jia, Kalyan Vasuden Alwala, Kartikeya Upasani, Kate Plawiak, Ke Li, Kenneth Heafield,
Kevin Stone, Khalid El-Arini, Krithika Iyer, Kshitiz Malik, Kuenley Chiu, Kunal Bhalla, Lauren
Rantala-Yeary, Laurens van der Maaten, Lawrence Chen, Liang Tan, Liz Jenkins, Louis Martin,
Lovish Madaan, Lubo Malo, Lukas Blecher, Lukas Landzaat, Luke de Oliveira, Madeline Muzzi,
Mahesh Pasupuleti, Mannat Singh, Manohar Paluri, Marcin Kardas, Mathew Oldham, Mathieu
Rita, Maya Pavlova, Melanie Kambadur, Mike Lewis, Min Si, Mitesh Kumar Singh, Mona Hassan,
Naman Goyal, Narjes Torabi, Nikolay Bashlykov, Nikolay Bogoychev, Niladri Chatterji, Olivier
Duchenne, Onur Çelebi, Patrick Alrassy, Pengchuan Zhang, Pengwei Li, Petar Vasic, Peter Weng,
PrajjwalBhargava,PratikDubal,PraveenKrishnan,PunitSinghKoura,PuxinXu,QingHe,Qingxiao
Dong,RagavanSrinivasan,RajGanapathy,RamonCalderer,RicardoSilveiraCabral,RobertStojnic,
Roberta Raileanu, Rohit Girdhar, Rohit Patel, Romain Sauvestre, Ronnie Polidoro, Roshan Sumbaly,
RossTaylor,RuanSilva,RuiHou,RuiWang,SagharHosseini,SahanaChennabasappa,SanjaySingh,
Sean Bell, Seohyun Sonia Kim, Sergey Edunov, Shaoliang Nie, Sharan Narang, Sharath Raparthy,
Sheng Shen, Shengye Wan, Shruti Bhosale, Shun Zhang, Simon Vandenhende, Soumya Batra,
Spencer Whitman, Sten Sootla, Stephane Collot, Suchin Gururangan, Sydney Borodinsky, Tamar
Herman, Tara Fowler, Tarek Sheasha, Thomas Georgiou, Thomas Scialom, Tobias Speckbacher,
Todor Mihaylov, Tong Xiao, Ujjwal Karn, Vedanuj Goswami, Vibhor Gupta, Vignesh Ramanathan,
Viktor Kerkez, Vincent Gonguet, Virginie Do, Vish Vogeti, Vladan Petrovic, Weiwei Chu, Wenhan
Xiong, Wenyin Fu, Whitney Meers, Xavier Martinet, Xiaodong Wang, Xiaoqing Ellen Tan, Xinfeng
Xie, Xuchao Jia, Xuewei Wang, Yaelle Goldschlag, Yashesh Gaur, Yasmine Babaei, Yi Wen, Yiwen
Song,YuchenZhang,YueLi,YuningMao,ZacharieDelpierreCoudert,ZhengYan,ZhengxingChen,
ZoePapakipos,AadityaSingh,AaronGrattafiori,AbhaJain,AdamKelsey,AdamShajnfeld,Adithya
Gangidi, Adolfo Victoria, Ahuva Goldstand, Ajay Menon, Ajay Sharma, Alex Boesenberg, Alex
Vaughan, Alexei Baevski, Allie Feinstein, Amanda Kallet, Amit Sangani, Anam Yunus, Andrei Lupu,
Andres Alvarado, Andrew Caples, Andrew Gu, Andrew Ho, Andrew Poulton, Andrew Ryan, Ankit
Ramchandani, Annie Franco, Aparajita Saraf, Arkabandhu Chowdhury, Ashley Gabriel, Ashwin
Bharambe, Assaf Eisenman, Azadeh Yazdan, Beau James, Ben Maurer, Benjamin Leonhardi, Bernie
Huang, Beth Loyd, Beto De Paola, Bhargavi Paranjape, Bing Liu, Bo Wu, Boyu Ni, Braden Hancock,
Bram Wasti, Brandon Spence, Brani Stojkovic, Brian Gamido, Britt Montalvo, Carl Parker, Carly
Burton, Catalina Mejia, Changhan Wang, Changkyu Kim, Chao Zhou, Chester Hu, Ching-Hsiang
Chu, Chris Cai, Chris Tindal, Christoph Feichtenhofer, Damon Civin, Dana Beaty, Daniel Kreymer,
54

<!-- Page 55 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought
DanielLi,DannyWyatt,DavidAdkins,DavidXu,DavideTestuggine,DeliaDavid,DeviParikh,Diana
Liskovich, Didem Foss, Dingkang Wang, Duc Le, Dustin Holland, Edward Dowling, Eissa Jamil,
Elaine Montgomery, Eleonora Presani, Emily Hahn, Emily Wood, Erik Brinkman, Esteban Arcaute,
Evan Dunbar, Evan Smothers, Fei Sun, Felix Kreuk, Feng Tian, Firat Ozgenel, Francesco Caggioni,
Francisco Guzmán, Frank Kanayet, Frank Seide, Gabriela Medina Florez, Gabriella Schwarz, Gada
Badeer,GeorgiaSwee,GilHalpern,GovindThattai,GrantHerman, GrigorySizov, Guangyi,Zhang,
Guna Lakshminarayanan, Hamid Shojanazeri, Han Zou, Hannah Wang, Hanwen Zha, Haroun
Habeeb, Harrison Rudolph, Helen Suk, Henry Aspegren, Hunter Goldman, Ibrahim Damlaj, Igor
Molybog, Igor Tufanov, Irina-Elena Veliche, Itai Gat, Jake Weissman, James Geboski, James Kohli,
Japhet Asher, Jean-Baptiste Gaya, Jeff Marcus, Jeff Tang, Jennifer Chan, Jenny Zhen, Jeremy
Reizenstein, Jeremy Teboul, Jessica Zhong, Jian Jin, Jingyi Yang, Joe Cummings, Jon Carvill, Jon
Shepard, Jonathan McPhie, Jonathan Torres, Josh Ginsburg, Junjie Wang, Kai Wu, Kam Hou U,
Karan Saxena, Karthik Prasad, Kartikay Khandelwal, Katayoun Zand, Kathy Matosich, Kaushik
Veeraraghavan, Kelly Michelena, Keqian Li, Kun Huang, Kunal Chawla, Kushal Lakhotia, Kyle
Huang, Lailin Chen, Lakshya Garg, Lavender A, Leandro Silva, Lee Bell, Lei Zhang, Liangpeng
Guo, Licheng Yu, Liron Moshkovich, Luca Wehrstedt, Madian Khabsa, Manav Avalani, Manish
Bhatt, Maria Tsimpoukelli, Martynas Mankus, Matan Hasson, Matthew Lennie, Matthias Reso,
Maxim Groshev, Maxim Naumov, Maya Lathi, Meghan Keneally, Michael L. Seltzer, Michal Valko,
Michelle Restrepo, Mihir Patel, Mik Vyatskov, Mikayel Samvelyan, Mike Clark, Mike Macey, Mike
Wang, Miquel Jubert Hermoso, Mo Metanat, Mohammad Rastegari, Munish Bansal, Nandhini
Santhanam, Natascha Parks, Natasha White, Navyata Bawa, Nayan Singhal, Nick Egebo, Nicolas
Usunier,NikolayPavlovichLaptev,NingDong,NingZhang,NormanCheng,OlegChernoguz,Olivia
Hart, Omkar Salpekar, Ozlem Kalinli, Parkin Kent, Parth Parekh, Paul Saab, Pavan Balaji, Pedro
Rittner, Philip Bontrager, Pierre Roux, Piotr Dollar, Polina Zvyagina, Prashant Ratanchandani,
Pritish Yuvraj, Qian Liang, Rachad Alao, Rachel Rodriguez, Rafi Ayub, Raghotham Murthy, Raghu
Nayani, Rahul Mitra, Raymond Li, Rebekkah Hogan, Robin Battey, Rocky Wang, Rohan Maheswari,
RussHowes,RutyRinott,SaiJayeshBondu,SamyakDatta,SaraChugh,SaraHunt,SargunDhillon,
SashaSidorov,SatadruPan,SaurabhVerma,SeijiYamamoto,SharadhRamaswamy,ShaunLindsay,
Shaun Lindsay, Sheng Feng, Shenghao Lin, Shengxin Cindy Zha, Shiva Shankar, Shuqiang Zhang,
Shuqiang Zhang, Sinong Wang, Sneha Agarwal, Soji Sajuyigbe, Soumith Chintala, Stephanie Max,
Stephen Chen, Steve Kehoe, Steve Satterfield, Sudarshan Govindaprasad, Sumit Gupta, Sungmin
Cho, Sunny Virk, Suraj Subramanian, Sy Choudhury, Sydney Goldman, Tal Remez, Tamar Glaser,
Tamara Best, Thilo Kohler, Thomas Robinson, Tianhe Li, Tianjun Zhang, Tim Matthews, Timothy
Chou,TzookShaked,VarunVontimitta,VictoriaAjayi,VictoriaMontanez,VijaiMohan,VinaySatish
Kumar,VishalMangla,VítorAlbiero,VladIonescu,VladPoenaru,VladTiberiuMihailescu,Vladimir
Ivanov, Wei Li, Wenchen Wang, Wenwen Jiang, Wes Bouaziz, Will Constable, Xiaocheng Tang,
Xiaofang Wang, Xiaojian Wu, Xiaolan Wang, Xide Xia, Xilun Wu, Xinbo Gao, Yanjun Chen, Ye Hu,
Ye Jia, Ye Qi, Yenda Li, Yilin Zhang, Ying Zhang, Yossi Adi, Youngjin Nam, Yu, Wang, Yuchen Hao,
Yundi Qian, Yuzi He, Zach Rait, Zachary DeVito, Zef Rosnbrick, Zhaoduo Wen, Zhenyu Yang, and
Zhiwei Zhao. The llama 3 herd of models, 2024. URL https://arxiv.org/abs/2407.21783.
Yann Dubois, Xuechen Li, Rohan Taori, Tianyi Zhang, Ishaan Gulrajani, Jimmy Ba, Carlos Guestrin,
Percy Liang, and Tatsunori B. Hashimoto. Alpacafarm: A simulation framework for methods that
learn from human feedback, 2024.
Subhabrata Dutta, Joykirat Singh, Soumen Chakrabarti, and Tanmoy Chakraborty. How to think
step-by-step: A mechanistic understanding of chain-of-thought reasoning. ArXiv, abs/2402.18312,

## URL https://api.semanticscholar.org/CorpusID:268041831.

Jeffrey L Elman. Finding structure in time. Cognitive science, 14(2):179–211, 1990.
55

<!-- Page 56 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought
Xidong Feng, Ziyu Wan, Muning Wen, Stephen Marcus McAleer, Ying Wen, Weinan Zhang, and Jun
Wang. Alphazero-like tree-search can guide large language model decoding and training, 2024.
Kanishk Gandhi, Dorsa Sadigh, and Noah D. Goodman. Strategic reasoning with language models,

## URL https://arxiv.org/abs/2305.19165.

Kanishk Gandhi, Denise Lee, Gabriel Grand, Muxin Liu, Winson Cheng, Archit Sharma, and Noah D
Goodman. Streamofsearch(sos): Learningtosearchinlanguage. arXivpreprintarXiv:2404.03683,
2024.
Bofei Gao, Feifan Song, Zhe Yang, Zefan Cai, Yibo Miao, Qingxiu Dong, Lei Li, Chenghao Ma,
Liang Chen, Runxin Xu, Zhengyang Tang, Benyou Wang, Daoguang Zan, Shanghaoran Quan,
Ge Zhang, Lei Sha, Yichang Zhang, Xuancheng Ren, Tianyu Liu, and Baobao Chang. Omnimath: A universal olympiad level mathematic benchmark for large language models, 2024. URL
https://arxiv.org/abs/2410.07985.
Jonas Gehring, Kunhao Zheng, Jade Copet, Vegard Mella, Taco Cohen, and Gabriel Synnaeve. Rlef:
Grounding code llms in execution feedback with reinforcement learning, 2024. URL https:
//arxiv.org/abs/2410.02089.
Dibya Ghosh, Jad Rahme, Aviral Kumar, Amy Zhang, Ryan P. Adams, and Sergey Levine. Why
generalization in rl is difficult: Epistemic pomdps and implicit partial observability, 2021. URL
https://arxiv.org/abs/2107.06277.
EdouardGrave,PiotrBojanowski,PrakharGupta,ArmandJoulin,andTomasMikolov. Learningword
vectorsfor157languages. InProceedingsoftheInternationalConference onLanguageResourcesand
Evaluation (LREC 2018), 2018.
Arnav Gudibande, Eric Wallace, Charlie Snell, Xinyang Geng, Hao Liu, Pieter Abbeel, Sergey Levine,
and Dawn Song. The false promise of imitating proprietary llms, 2023. URL https://arxiv.
org/abs/2305.15717.
Shibo Hao, Yi Gu, Haodi Ma, Joshua Jiahua Hong, Zhen Wang, Daisy Zhe Wang, and Zhiting Hu.
Reasoningwithlanguagemodelisplanningwithworldmodel,2023. URLhttps://arxiv.org/
abs/2305.14992.
Alex Havrilla, Yuqing Du, Sharath Chandra Raparthy, Christoforos Nalmpantis, Jane Dwivedi-Yu,
Maksym Zhuravinskyi, Eric Hambro, Sainbayar Sukhbaatar, and Roberta Raileanu. Teaching large
language models to reason with reinforcement learning, 2024. URL https://arxiv.org/abs/
2403.04642.
Dan Hendrycks, Collin Burns, Saurav Kadavath, Akul Arora, Steven Basart, Eric Tang, Dawn Song,
andJacobSteinhardt. Measuringmathematicalproblemsolvingwiththemathdataset,2021. URL
https://arxiv.org/abs/2103.03874.
Irina Higgins, Loic Matthey, Arka Pal, Christopher Burgess, Xavier Glorot, Matthew Botvinick, Shakir
Mohamed, and Alexander Lerchner. B-vae: Learning basic visual concepts with a constrained
variational framework. In International Conference on Learning Representations (ICLR), 2017. URL
https://openreview.net/forum?id=Sy2fzU9gl.
Jan Humplik, Alexandre Galashov, Leonard Hasenclever, Pedro A. Ortega, Yee Whye Teh, and Nicolas
Heess. Meta reinforcement learning as task inference, 2019. URL https://arxiv.org/abs/
1905.06424.
56

<!-- Page 57 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought
AndyL.Jones. Scalingscalinglawswithboardgames,2021. URLhttps://arxiv.org/abs/2104.
03113.
Michael I Jordan. Serial order: A parallel distributed processing approach. In Advances in psychology,
volume 121, pp. 471–495. Elsevier, 1997.
Armand Joulin, Edouard Grave, Piotr Bojanowski, Matthijs Douze, H’erve J’egou, and Tomas Mikolov.
Fasttext.zip: Compressing text classification models. arXiv preprint arXiv:1612.03651, 2016a.
Armand Joulin, Edouard Grave, Piotr Bojanowski, and Tomas Mikolov. Bag of tricks for efficient text
classification. arXiv preprint arXiv:1607.01759, 2016b.
Amirhossein Kazemnejad, Milad Aghajohari, Eva Portelance, Alessandro Sordoni, Siva Reddy, Aaron
Courville, and Nicolas Le Roux. Vineppo: Unlocking rl potential for llm reasoning through refined
credit assignment, 2024. URL https://arxiv.org/abs/2410.01679.
DiederikPKingmaandMaxWelling. Auto-encodingvariationalbayes. arXivpreprintarXiv:1312.6114,

## URL https://arxiv.org/abs/1312.6114.

Levente Kocsis and Csaba Szepesvári. Bandit based Monte-Carlo planning. In Johannes Fürnkranz,
Tobias Scheffer, and Myra Spiliopoulou (eds.), Machine Learning: ECML 2006, volume 4212 of
Lecture Notes in Computer Science, Berlin, Heidelberg, 2006. Springer. doi: 10.1007/11871842_29.
Jing Yu Koh, Stephen McAleer, Daniel Fried, and Ruslan Salakhutdinov. Tree search for language
model agents. arXiv preprint arXiv:2407.01476, 2024.
Aviral Kumar, Vincent Zhuang, Rishabh Agarwal, Yi Su, John D Co-Reyes, Avi Singh, Kate Baumli,
Shariq Iqbal, Colton Bishop, Rebecca Roelofs, Lei M Zhang, Kay McKinney, Disha Shrivastava,
Cosmin Paduraru, George Tucker, Doina Precup, Feryal Behbahani, and Aleksandra Faust. Training
language models to self-correct via reinforcement learning, 2024. URL https://arxiv.org/
abs/2409.12917.
XinLai,ZhuotaoTian,YukangChen,SenqiaoYang,XiangruPeng,andJiayaJia. Step-dpo: Step-wise
preference optimization for long-chain reasoning of llms, 2024. URL https://arxiv.org/abs/
2406.18629.
Lucas Lehnert, Sainbayar Sukhbaatar, DiJia Su, Qinqing Zheng, Paul Mcvay, Michael Rabbat, and
Yuandong Tian. Beyond a*: Better planning with transformers via search dynamics bootstrapping,

## URL https://arxiv.org/abs/2402.14083.

Sergey Levine, Aviral Kumar, George Tucker, and Justin Fu. Offline reinforcement learning: Tutorial,
review, and perspectives on open problems, 2020.
Jia LI, Edward Beeching, Lewis Tunstall, Ben Lipkin, Roman Soletskyi, Shengyi Costa
Huang, Kashif Rasul, Longhui Yu, Albert Jiang, Ziju Shen, Zihan Qin, Bin Dong,
Li Zhou, Yann Fleureau, Guillaume Lample, and Stanislas Polu. Numinamath. [https:
//huggingface.co/AI-MO/NuminaMath-CoT](https://github.com/project-numina/
aimo-progress-prize/blob/main/report/numina_dataset.pdf), 2024.
Zhiyuan Li, Hong Liu, Denny Zhou, and Tengyu Ma. Chain of thought empowers transformers to
solve inherently serial problems, 2024. URL https://arxiv.org/abs/2402.12875.
Hunter Lightman, Vineet Kosaraju, Yura Burda, Harri Edwards, Bowen Baker, Teddy Lee, Jan
Leike, John Schulman, Ilya Sutskever, and Karl Cobbe. Let’s verify step by step. arXiv preprint
arXiv:2305.20050, 2023.
57

<!-- Page 58 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought
Anji Liu, Yitao Liang, Ji Liu, Guy Van den Broeck, and Jianshu Chen. On effective parallelization of
monte carlo tree search, 2020. URL https://arxiv.org/abs/2006.08785.
Aman Madaan, Niket Tandon, Prakhar Gupta, Skyler Hallinan, Luyu Gao, Sarah Wiegreffe, Uri Alon,
Nouha Dziri, Shrimai Prabhumoye, Yiming Yang, Shashank Gupta, Bodhisattwa Prasad Majumder,
Katherine Hermann, Sean Welleck, Amir Yazdanbakhsh, and Peter Clark. Self-refine: Iterative
refinement with self-feedback, 2023. URL https://arxiv.org/abs/2303.17651.
Dakota Mahan, Duy Van Phung, Rafael Rafailov, Chase Blagden, Nathan Lile, Louis Castricato, Jan-
Philipp Fränken, Chelsea Finn, and Alon Albalak. Generative reward models. arXiv preprint
arXiv:2410.12832, 2024.
The mathlib Community. The lean mathematical library. In Proceedings of the 9th ACM SIGPLAN
International Conference on Certified Programs and Proofs, POPL ’20. ACM, January 2020. doi:
10.1145/3372885.3373824. URL http://dx.doi.org/10.1145/3372885.3373824.
William Merrill and Ashish Sabharwal. The expresssive power of transformers with chain of thought.
arXiv preprint arXiv:2310.07923, 2023.
Iman Mirzadeh, Keivan Alizadeh, Hooman Shahrokhi, Oncel Tuzel, Samy Bengio, and Mehrdad
Farajtabar. Gsm-symbolic: Understanding the limitations of mathematical reasoning in large
language models, 2024. URL https://arxiv.org/abs/2410.05229.
Arindam Mitra, Hamed Khanpour, Corby Rosset, and Ahmed Awadallah. Orca-math: Unlocking the
potential of slms in grade school math, 2024. URL https://arxiv.org/abs/2402.14830.
Reiichiro Nakano, Jacob Hilton, Suchir Balaji, Jeff Wu, Long Ouyang, Christina Kim, Christopher
Hesse, Shantanu Jain, Vineet Kosaraju, William Saunders, Xu Jiang, Karl Cobbe, Tyna Eloundou,
Gretchen Krueger, Kevin Button, Matthew Knight, Benjamin Chess, and John Schulman. Webgpt:
Browser-assisted question-answering with human feedback, 2022.
Allen Nie, Yi Su, Bo Chang, Jonathan N. Lee, Ed H. Chi, Quoc V. Le, and Minmin Chen. Evolve:
Evaluating and optimizing llms for exploration, 2024. URL https://arxiv.org/abs/2410.
06238.
MichaelNoukhovitch,ShengyiHuang,SophieXhonneux,ArianHosseini,RishabhAgarwal,andAaron
Courville. Asynchronous rlhf: Faster and more efficient off-policy rl for language models, 2024.
URL https://arxiv.org/abs/2410.18252.
Franz Nowak, Anej Svete, Alexandra Butoi, and Ryan Cotterell. On the representational capacity of
neural language models with chain-of-thought reasoning. arXiv preprint arXiv:2406.14197, 2024.
OpenAI. Gpt-4 technical report. arXiv preprint, 2023. https://arxiv.org/abs/2303.08774.
OpenAI. Learning to reason with llms. https://openai.com/index/
learning-to-reason-with-llms/, 2024. Accessed: 2024-12-20.
Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida, Carroll Wainwright, Pamela Mishkin, Chong
Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, John Schulman, Jacob Hilton, Fraser
Kelton, Luke Miller, Maddie Simens, Amanda Askell, Peter Welinder, Paul F Christiano, Jan
Leike, and Ryan Lowe. Training language models to follow instructions with human feedback. In S. Koyejo, S. Mohamed, A. Agarwal, D. Belgrave, K. Cho, and A. Oh (eds.), Advances in Neural Information Processing Systems, volume 35, pp. 27730–27744. Curran Associates, Inc., 2022. URL https://proceedings.neurips.cc/paper_files/paper/2022/
file/b1efde53be364a73914f58805a001731-Paper-Conference.pdf.
58

<!-- Page 59 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought
Ryan Park, Rafael Rafailov, Stefano Ermon, and Chelsea Finn. Disentangling length from quality in
direct preference optimization, 2024.
XueBinPeng,AviralKumar,GraceZhang,andSergeyLevine. Advantage-weightedregression: Simple
and scalable off-policy reinforcement learning. arXiv preprint arXiv:1910.00177, 2019.
Du Phan, Matthew D. Hoffman, David Dohan, Sholto Douglas, Tuan Anh Le, Aaron Parisi, Pavel
Sountsov, Charles Sutton, Sharad Vikram, and Rif A. Saurous. Training chain-of-thought via
latent-variable inference, 2023. URL https://arxiv.org/abs/2312.02179.
Ben Prystawski, Michael Li, and Noah Goodman. Why think step by step? reasoning emerges from
the locality of experience. Advances in Neural Information Processing Systems, 36, 2024.
Pranav Putta, Edmund Mills, Naman Garg, Sumeet Motwani, Chelsea Finn, Divyansh Garg, and
RafaelRafailov. Agentq: Advancedreasoningandlearningforautonomousaiagents. arXivpreprint
arXiv:2408.07199, 2024.
Yuxiao Qu, Tianjun Zhang, Naman Garg, and Aviral Kumar. Recursive introspection: Teaching
languagemodelagentshowtoself-improve,2024. URLhttps://arxiv.org/abs/2407.18219.
Santosh Kumar Radha, Yasamin Nouri Jelyani, Ara Ghukasyan, and Oktay Goktas. Iteration of
thought: Leveraging inner dialogue for autonomous large language model reasoning, 2024. URL
https://arxiv.org/abs/2409.12618.
Kate Rakelly, Aurick Zhou, Deirdre Quillen, Chelsea Finn, and Sergey Levine. Efficient off-policy
meta-reinforcementlearningviaprobabilisticcontextvariables,2019. URLhttps://arxiv.org/
abs/1903.08254.
Machel Reid, Nikolay Savinov, Denis Teplyashin, Dmitry Lepikhin, Timothy Lillicrap, Jean-baptiste
Alayrac, Radu Soricut, Angeliki Lazaridou, Orhan Firat, Julian Schrittwieser, et al. Gemini
1.5: Unlocking multimodal understanding across millions of tokens of context. arXiv preprint
arXiv:2403.05530, 2024.
Christopher D. Rosin. Multi-armed bandits with episode context. Annals of Mathematics and Artificial
Intelligence, 61(3):203–230, 2011. doi: 10.1007/s10472-011-9258-6.
Adam Santoro, Sergey Bartunov, Matthew Botvinick, Daan Wierstra, and Timothy Lillicrap. One-shot
learningwithmemory-augmentedneuralnetworks,2016. URLhttps://arxiv.org/abs/1605.
06065.
John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov. Proximal policy
optimization algorithms, 2017.
John Schultz, Jakub Adamek, Matej Jusup, Marc Lanctot, Michael Kaisers, Sarah Perrin, Daniel
Hennes, Jeremy Shar, Cannada Lewis, Anian Ruoss, Tom Zahavy, Petar Veličković, Laurel Prince,
Satinder Singh, Eric Malmi, and Nenad Tomašev. Mastering board games by external and internal
planning with language models, 2024. URL https://arxiv.org/abs/2412.12119.
Bilgehan Sel, Ahmad Al-Tawaha, Vanshaj Khattar, Ruoxi Jia, and Ming Jin. Algorithm of thoughts:
Enhancingexplorationofideasinlargelanguagemodels,2024. URLhttps://arxiv.org/abs/
2308.10379.
Amrith Setlur, Saurabh Garg, Xinyang Geng, Naman Garg, Virginia Smith, and Aviral Kumar. Rl
on incorrect synthetic data scales the efficiency of llm math reasoning by eight-fold, 2024a. URL
https://arxiv.org/abs/2406.14532.
59

<!-- Page 60 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought
Amrith Setlur, Chirag Nagpal, Adam Fisch, Xinyang Geng, Jacob Eisenstein, Rishabh Agarwal, Alekh
Agarwal, Jonathan Berant, and Aviral Kumar. Rewarding progress: Scaling automated process
verifiers for llm reasoning. arXiv preprint arXiv:2410.08146, 2024b.
Amrith Setlur, Chirag Nagpal, Adam Fisch, Xinyang Geng, Jacob Eisenstein, Rishabh Agarwal, Alekh
Agarwal, Jonathan Berant, and Aviral Kumar. Rewarding progress: Scaling automated process
verifiers for llm reasoning, 2024c. URL https://arxiv.org/abs/2410.08146.
Amrith Setlur, Yuxiao Qu, Lunjun Zhang, Matthew Yang, Virginia Smith,
and Aviral Kumar. Optimizing llm test-time compute involves solving a meta-rl problem. https://blog.ml.cmu.edu/2025/01/08/
optimizing-llm-test-time-compute-involves-solving-a-meta-rl-problem/,

## CMU MLD Blog.

ZhihongShao,PeiyiWang,QihaoZhu,RunxinXu,JunxiaoSong,XiaoBi,HaoweiZhang,Mingchuan
Zhang,Y.K.Li,Y.Wu,andDayaGuo. Deepseekmath: Pushingthelimitsofmathematicalreasoning
in open language models, 2024. URL https://arxiv.org/abs/2402.03300.
Noah Shinn, Federico Cassano, Edward Berman, Ashwin Gopinath, Karthik Narasimhan, and Shunyu
Yao. Reflexion: Languageagentswithverbalreinforcementlearning,2023. URLhttps://arxiv.
org/abs/2303.11366.
D. Silver, A. Huang, C. Maddison, et al. Mastering the game of go with deep neural networks and
tree search. Nature, 529:484–489, 2016. doi: 10.1038/nature16961.
David Silver, Thomas Hubert, Julian Schrittwieser, Ioannis Antonoglou, Matthew Lai, Arthur Guez,
Marc Lanctot, Laurent Sifre, Dharshan Kumaran, Thore Graepel, Timothy P. Lillicrap, Karen
Simonyan, and Demis Hassabis. A general reinforcement learning algorithm that masters chess,
shogi, and go through self-play. Science, 362(6419):1140–1144, 2018. doi: 10.1126/science.
aar6404.
AviSingh,JohnD.Co-Reyes,RishabhAgarwal,AnkeshAnand,PiyushPatil,XavierGarcia,PeterJ.Liu,
JamesHarrison,JaehoonLee,KelvinXu,AaronParisi,AbhishekKumar,AlexAlemi,AlexRizkowsky,
AzadeNova,BenAdlam,BerndBohnet,GamaleldinElsayed,HanieSedghi,IgorMordatch,Isabelle
Simpson, Izzeddin Gur, Jasper Snoek, Jeffrey Pennington, Jiri Hron, Kathleen Kenealy, Kevin
Swersky, Kshiteej Mahajan, Laura Culp, Lechao Xiao, Maxwell L. Bileschi, Noah Constant, Roman
Novak, Rosanne Liu, Tris Warkentin, Yundi Qian, Yamini Bansal, Ethan Dyer, Behnam Neyshabur,
Jascha Sohl-Dickstein, and Noah Fiedel. Beyond human data: Scaling self-training for problemsolving with language models, 2024. URL https://arxiv.org/abs/2312.06585.
PrasannSinghal,TanyaGoyal,JiachengXu,andGregDurrett. Alongwaytogo: Investigatinglength
correlations in rlhf, 2023.
CharlieSnell,JaehoonLee,KelvinXu,andAviralKumar. Scalingllmtest-timecomputeoptimallycan
be more effective than scaling model parameters, 2024. URL https://arxiv.org/abs/2408.
03314.
Ray J Solomonoff. A formal theory of inductive inference. part i. Information and control, 7(1):1–22,
1964.
Bradly C. Stadie, Ge Yang, Rein Houthooft, Xi Chen, Yan Duan, Yuhuai Wu, Pieter Abbeel, and Ilya
Sutskever. Someconsiderationsonlearningtoexploreviameta-reinforcementlearning,2019. URL
https://arxiv.org/abs/1803.01118.
60

<!-- Page 61 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought
Nisan Stiennon, Long Ouyang, Jeff Wu, Daniel M. Ziegler, Ryan Lowe, Chelsea Voss, Alec Radford,
Dario Amodei, and Paul Christiano. Learning to summarize from human feedback, 2022.
Fahim Tajwar, Anikait Singh, Archit Sharma, Rafael Rafailov, Jeff Schneider, Tengyang Xie, Stefano
Ermon, Chelsea Finn, and Aviral Kumar. Preference fine-tuning of llms should leverage suboptimal,
on-policy data. arXiv preprint arXiv:2404.14367, 2024.
Qwen Team. Qwq: Reflect deeply on the boundaries of the unknown, November 2024. URL
https://qwenlm.github.io/blog/qwq-32b-preview/.
Ye Tian, Baolin Peng, Linfeng Song, Lifeng Jin, Dian Yu, Haitao Mi, and Dong Yu. Toward selfimprovement of llms via imagination, searching, and criticizing, 2024. URL https://arxiv.
org/abs/2404.12253.
ShubhamToshniwal,WeiDu,IvanMoshkov,BranislavKisacanin,AlexanAyrapetyan,andIgorGitman.
Openmathinstruct-2: Accelerating ai for math with massive open-source instruction data. arXiv
preprint arXiv:2410.01560, 2024.
PeiyiWang,LeiLi,ZhihongShao,RunxinXu,DamaiDai,YifeiLi,DeliChen,YuWu,andZhifangSui.
Math-shepherd: Verify and reinforce llms step-by-step without human annotations. In Proceedings
of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers),
pp. 9426–9439, 2024.
Ronald J. Williams. Simple statistical gradient-following algorithms for connectionist reinforcement
learning. Mach. Learn., 8(3–4):229–256, may 1992. ISSN 0885-6125. doi: 10.1007/BF00992696.
URL https://doi.org/10.1007/BF00992696.
Yuxi Xie, Anirudh Goyal, Wenyue Zheng, Min-Yen Kan, Timothy P. Lillicrap, Kenji Kawaguchi, and
Michael Shieh. Monte carlo tree search boosts reasoning via iterative preference learning, 2024.
URL https://arxiv.org/abs/2405.00451.
Mengjiao Yang, Dale Schuurmans, Pieter Abbeel, and Ofir Nachum. Chain of thought imitation with
procedure cloning, 2022. URL https://arxiv.org/abs/2205.10816.
Shunyu Yao, Dian Yu, Jeffrey Zhao, Izhak Shafran, Thomas L. Griffiths, Yuan Cao, and Karthik
Narasimhan. Treeofthoughts: Deliberateproblemsolvingwithlargelanguagemodels,2023. URL
https://arxiv.org/abs/2305.10601.
Tian Ye, Zicheng Xu, Yuanzhi Li, and Zeyuan Allen-Zhu. Physics of language models: Part 2.1,
grade-school math and the hidden reasoning process, 2024a. URL https://arxiv.org/abs/
2407.20311.
Tian Ye, Zicheng Xu, Yuanzhi Li, and Zeyuan Allen-Zhu. Physics of language models: Part 2.2, how
to learn from mistakes on grade-school math problems, 2024b. URL https://arxiv.org/abs/
2408.16293.
Shuo Yin, Weihao You, Zhilong Ji, Guoqiang Zhong, and Jinfeng Bai. Mumath-code: Combining tooluse large language models with multi-perspective data augmentation for mathematical reasoning.
arXiv preprint arXiv:2405.07551, 2024.
Xiao Yu, Baolin Peng, Vineeth Vajipey, Hao Cheng, Michel Galley, Jianfeng Gao, and Zhou Yu.
Exact: Teaching ai agents to explore with reflective-mcts and exploratory learning, 2024. URL
https://arxiv.org/abs/2410.02052.
61

<!-- Page 62 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought
Zheng Yuan, Hongyi Yuan, Chengpeng Li, Guanting Dong, Keming Lu, Chuanqi Tan, Chang Zhou,
and Jingren Zhou. Scaling relationship on learning mathematical reasoning with large language
models, 2023. URL https://arxiv.org/abs/2308.01825.
Albert S. Yue, Lovish Madaan, Ted Moskovitz, DJ Strouse, and Aaditya K. Singh. HARP: A challenging human-annotated math reasoning benchmark, 2024. URL https://github.com/
aadityasingh/HARP.
Eric Zelikman, Yuhuai Wu, Jesse Mu, and Noah Goodman. Star: Bootstrapping reasoning with
reasoning. Advances in Neural Information Processing Systems, 35:15476–15488, 2022.
Eric Zelikman, Georges Harik, Yijia Shao, Varuna Jayasiri, Nick Haber, and Noah D Goodman.
Quiet-star: Language models can teach themselves to think before speaking. arXiv preprint
arXiv:2403.09629, 2024.
Lunjun Zhang, Arian Hosseini, Hritik Bansal, Mehran Kazemi, Aviral Kumar, and Rishabh Agarwal.
Generative verifiers: Reward modeling as next-token prediction, 2024a. URL https://arxiv.
org/abs/2408.15240.
Yiming Zhang, Jianfeng Chi, Hailey Nguyen, Kartikeya Upasani, Daniel M. Bikel, Jason Weston, and
EricMichaelSmith. Backtrackingimprovesgenerationsafety, 2024b. URLhttps://arxiv.org/
abs/2409.14586.
Andy Zhou, Kai Yan, Michal Shlapentokh-Rothman, Haohan Wang, and Yu-Xiong Wang. Language
agent tree search unifies reasoning acting and planning in language models, 2024a. URL https:
//arxiv.org/abs/2310.04406.
Yifei Zhou, Andrea Zanette, Jiayi Pan, Sergey Levine, and Aviral Kumar. Archer: Training language
modelagentsviahierarchicalmulti-turnrl,2024b. URLhttps://arxiv.org/abs/2402.19446.

### A. Prompting

We investigate whether carefully constructed prompting protocols can induce reasoning capabilities
similartothosedemonstratedbyRL-basedmodelslikeO1. Throughanevaluationoffiveincreasingly
sophisticated instruction sets, we analyze token generation patterns, presence of reasoning-like
behaviors, and their correlation with math problem-solving performance.
Table 4: Input token count across prompting strategies using OpenAI’s GPT-4o tokenizer (excluding
problem tokens). Complex instructions like Think (3-shot) use substantially more tokens, primarily
due to in-context demonstrations and explicit capabilities descriptions (e.g. thinking, reflection, and
verification requirements).
Strategy Tokens

### Baseline 23

Chain-of-Thought (CoT) 35

### Think 1,895

Think with demonstrations (3-shot) 4,659
Think & Verify 2,111
62

<!-- Page 63 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought

### B. Regret Analysis

Table 5 presents detailed statistics on regret expression across different models and prompting
strategies. The data shows varying levels of self-correction and error acknowledgment behaviors
across model scales and prompting approaches.

### C. Different Instruction Tuning Objectives

Below we outline a number of potential finetuning objectives for the instruction tuning stage of our
reasoning pipeline described in Section 7.1.

## A standard procedural-cloning approach (Yang et al., 2022) which uses traditional supervised

fine-tuning
⎡ ⎤

## |Z| |S|

∑︁ ∑︁
ℒ(𝜃) = min−E (q,Z,S)∼𝒟train ⎣ log𝜋 𝜃 (z 𝑖+1 |Z 𝑖 ,q)+ log𝜋 𝜃 (s 𝑖+1 |S 𝑖 ,Z,q)⎦. (22)
𝜃
𝑖=1 𝑖=1

## Alternatively, we can optimize only over the Meta-CoT tokens with the following optimization

objective
⎡ ⎤

## |Z|

∑︁
ℒ(𝜃) = min−E (q,Z,S)∼𝒟train ⎣ log𝜋 𝜃 (z 𝑖+1 |Z 𝑖 ,q)⎦. (23)
𝜃
𝑖=1
In this formulation, the model will not learn to generate a solution, requiring the use of a
separate step to summarize the search process into a final solution. One hypothesis is that
training on joint sequences with the solution can serve as additional supervision to help the
model with maintaining internal state.

## One consideration is whether updating model parameters for sub-optimal, or even incorrect,

branches can induce the model to generate more errors. To handle this, we can mask incorrect
steps/branches in the above loss
⎡ ⎤

## |Z|

∑︁
ℒ(𝜃) = min−E (q,Z,S)∼𝒟train ⎣ 𝐼{z 𝑖+1 ∈ S}log𝜋 𝜃 (z 𝑖+1 |Z 𝑖 ,q)⎦. (24)
𝜃
𝑖=1
Thatisweonlytrainonthebranchesthatareonthecorrectpathfromtherootnode(problem)
tothefinalanswer. Priorworks(Gandhietal.,2024;Yeetal.,2024b)didnotmasktheincorrect
steps, and reported no degradation in performance, as long as the data distribution remains
reasonable. On the other hand Zhang et al. (2024b) specifically mask the tokens of the unsafe
generation.

## Under the above objective, there could be significant task mismatch between training and

generation, especially in the case of long search chains. One method to mitigate this issue is to
generate more synthetic training data by pruning intermediate branches not on the optimal
solution path to generate additional sequences. For example this was the SFT objective used
byZhangetal.(2024b),whichsimultaneouslytrainsonbacktrackingtrajectories(withmasking)
and the final optimal solution (Equation 1 in that paper).

### D. MCTS Details

Here we outline the details of our MCTS procedure from Section 4.3.1. Our procedure involves three
main steps: selection, backup, and expansion. We describe each step in detail below.
63

<!-- Page 64 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought
Selection. Startingattherootnodes (initializedasthequestionq), achildnodes(i.e. thenext
0
stepinthesolution)isselecteduntilaleafnodes isreached. Apartialsolutionisthenrepresentedas
𝑡
S = (s ,...,s ). The child node is selected according to the policy s = argmax 𝑈(S ,s) where
𝑡 1 𝑡 𝑡+1 s 𝑡
𝑈(S ,s) is calculated using UCT (Kocsis & Szepesvári, 2006), defined as
𝑡
√︃
log𝑁(S ,s)
𝑡

## 𝑈(S

𝑡
,s) = 𝑄(S
𝑡
,s)+𝑐exp .

## 𝑁(S )

𝑡
In this equation 𝑄(S ,s) is a value function, 𝑁(S ,s) is the visit count of selecting step s from the
𝑡 𝑡
partialsolutionS
𝑡

## ,𝑁(S

𝑡
) = ∑︀
𝑠

## 𝑁(S

𝑡
,s)isthetotalvisitcountofthepartialsolutionS
𝑡
,and𝑐exp ∈ R
is the exploration constant. We opt for the UCT formulation, instead of the more recent PUCT
variant (Rosin, 2011), as in our case actions are represented by logical steps and thus likelihoods
could be quite skewed.
Expansion. After the selection operation, we have chosen a leaf node s , and the path from the
𝑡
root node s to the leaf node forms a partial solution by concatenating the individual steps into the
0
partial solution, i.e. S = (s ,...,s ). If s is terminal, we do not expand it, otherwise the node is
𝑡 1 𝑡 𝑡
expanded by sampling 𝑏 actions {s𝑖 }𝑏 ∼ 𝜋 (·|S ) from the policy 𝜋 , and then adding the nodes
𝑡+1 𝑖=1 𝜃 𝑡 𝜃
{a𝑖 }𝑏 aschildrenofnodeS . Thevalueofeachchildnodeisinitializedwithavaluefunction𝑣 as
𝑡+1 𝑖=1 𝑡
𝑄(S ,s𝑖) = 𝑣((S ,s𝑖 ),q). This evaluation essentially replaces the "simulation" step usually carried
𝑡 𝑡 𝑡 𝑡+1
out in game settings.
Backup. Finally, the statistics of the expanded node S are backed up through the path to the
𝑡
root node s . For every ancestor node S on the path, the visit count is incremented
0 𝑖

## 𝑁(S ) = 𝑁(S )+1

𝑖 𝑖
and the value of each ancestor is updated as
𝑣(S ,q)−𝑄(S ,s )
𝑡 𝑖 𝑖+1
𝑄(S ,s ) = 𝑄(S ,s )+ .
𝑖 𝑖+1 𝑖 𝑖+1
𝑁(S ,s )
𝑖 𝑖+1

### E. Chains-Of-Thought

This section contains synthetic CoT traces comparing how different models reason through the same
planningproblems. Specifically,weshowcompletereasoningtracesfromGemini-1.5solvingproblems
using A* and MCTS algorithms, alongside parallel traces from DeepSeek-R1, DeepSeek-O1, and
Gemini-2 working through identical tasks. We also include an example trace demonstrating how a
smaller SFT-tuned Llama3.1-8B model performs tool-augmented reasoning on a challenging problem
using dynamic programming. Each trace details the step-by-step "internal" traces and the final
solution.
64

<!-- Page 65 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought
Therewere12seatspreparedforthejuryataroundtable,eachwithanameindicatedon
it. Nikolai Nikolaevich, who arrived first, absent-mindedly sat not in his designated seat
but in the next one clockwise. Each jury member arriving at the table afterward would
eithersitintheirdesignatedseat,or,ifitwasalreadyoccupied,theywouldwalkaround
the table clockwise and sit in the next available seat. The resulting seating arrangement
of the jury members depends on the order in which they approached the table. How
many different ways can the jury be seated?
0.0
Let's break this down step-by-step:
0.03125

## The first person, Nikolai, can sit in any of the 12 seats.


## The second person can sit in any of the remaining 11 seats.


## The third person can sit in any of the remaining 10 seats.


## This pattern continues until all 12 seats are filled.

0.0
Alternatively...

## The first person, Nikolai Nikolaevich, has only one choice for his

seat.

## The second person has one choice, as both their designated seat and

the seat next to it are taken.

## The third person also has one choice, as two seats are taken.


## This pattern continues until all seats are filled.

0.0
Alternatively...

## The first member can choose any of the 12 seats.


## The second member can choose any of the remaining 11 seats, but if

the first member chose the next seat clockwise, the second member
has only 10 options (not considering the first seat). This pattern
continues until the last member, who has only 1 option left.
0.0
Alternatively...

## Nikolai Nikolaevich can only sit in one position (the next seat

clockwise from his designated seat).

## After Nikolai Nikolaevich sits down, there are 11 remaining seats.


## The next person to sit can choose from the 11 remaining seats, but

if one of those seats is already occupied, they have to sit in the
next available seat. This means that the second person has 11
choices.

## The third person then has 10 choices, and so on, until the last

person has only 1 choice.
0.0
65

<!-- Page 66 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought
Alternatively...

## The first person, Nikolai Nikolaevich, has a fixed position.


## The second person can either sit in their designated seat or move to

the next seat clockwise. This gives 2 options for the second
person.

## The third person can either sit in their designated seat or move to

the next seat clockwise. This gives 2 options for the third person,
but we need to consider the case where the second person moved, so
there's only 1 additional option for the third person.

## Similarly, for each subsequent person, there are 2 options if the

previous person didn't move, and 1 additional option if the
previous person moved.
0.046875
Let's analyze the pattern:
0.0390625
- The first person has 1 option.
- The second person has 2 options.
- The third person has 2 options.
- The fourth person has 2 options if the third person didn't move, and
1 option if the third person moved, but since the second person
moved, the fourth person still has 2 options.
- This pattern continues for the rest of the jury members.
0.03125
So, the total number of ways the jury can be seated is the product of
the options for each person:
0.03125
\[ 1 \times 2 \times 2 \times 2 \times 2 \times 2 \times 2 \times 2 \
times 2 \times 2 \times 2 \times 2 = 2^{11} = 2048 \]
0.0078125
Wait, however, this process can be simplified by realizing that each
person has a unique "decision point" - the first time they have a
choice between sitting in their designated seat and moving to the
next seat. After that, their seat is determined by the previous
choices.
0.0078125
Alternatively, however, this is a circular arrangement, and we need to
account for the fact that the last person can also move. This
introduces a complication, as the last person will always have only
1 option if everyone else is seated.
0.0546875
66

<!-- Page 67 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought
Let's simplify the problem by considering the first 12 people. For each
of these 12 people, there are 2 options. However, we need to
subtract the cases where the last person doesn't move, as these
cases are already counted in the 2 options for each person.
0.0078125
Wait, to simplify, let's consider the arrangement of people relative to

### Nikolai Nikolaevich's fixed position. There are 11! ways to

arrange the remaining jury members around the table, as each person
has a fixed position relative to Nikolai.
0.0234375
However, this calculation doesn't take into account the fact that some
people can move. To correct for this, we need to consider the
number of "cycle" arrangements, where each cycle represents a group
of people who moved together.
0.0078125
Wait, let's re-examine the situation:
0.046875

## Nikolai Nikolaevich is seated.


## The second person can move or stay, giving 2 options.


## For each subsequent person, there's only 1 option left if everyone

else is seated.
0.046875
The pattern continues until the last person, who always has only 1
option.
0.03125
So, the total number of arrangements is the product of the options at
each step:
0.0390625
\[ 2 \times 2 \times 2 \times 2 \times 2 \times 2 \times 2 \times 2 \
times 2 \times 2 \times 1 = 2^{11} = \boxed{2048} \]
0.0
Wait, let's consider the total number of ways without the circular
constraint. For the first person, there's 1 option. For the rest,
there are 2 options each, except for the last person who has only 1
option. So, the total number of arrangements without the circular
constraint is:
\[ 1 \times 2^{11} \]
67

<!-- Page 68 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought
0.171875
However, we need to subtract the cases where everyone is seated in
their designated seats, which is 1 arrangement. But this is already
counted in the 2 options for each person.
0.03125
Alternatively, however, this counts each arrangement twice, since the
table is round, and we can rotate the arrangement without changing
it. To account for this, we divide by the number of seats, which is
12.
0.0703125
Alternatively, however, this counts each arrangement twice (once in
each direction around the table), so we need to divide by 2:
\[ \frac{1 \times 2^{11}}{2} = 2^{10} \]
0.328125
But this is not the correct answer. The correct answer is the number of
derangements of 12 objects, which is given by the formula:
\[!12 = 12! \left( 1 - \frac{1}{1!} + \frac{1}{2!} - \frac{1}{3!} + \
cdots + \frac{(-1)^{12}}{12!} \right) \]
0.0078125
Alternatively, but this is still not correct because it doesn't account
for the fact that the last person always has only 1 option. Let's
reconsider the problem.
0.0625
Alternatively, but this is not the correct answer because the problem
statement asks for the number of different ways the jury can be
seated, considering the circular arrangement. In a circular
arrangement, the last person's position is fixed once the first
person's position is chosen. Therefore, the correct calculation
should consider the number of ways to arrange the remaining 11
people around the table, not the total possible arrangements.
0.1484375
Alternatively, but we're not done yet! We need to consider the case
where the second person moves, which would cause the last person to
have only 1 option. This introduces an overcount. To correct for
this, we need to subtract the number of arrangements where the
second person moves, which is equivalent to the number of ways the
jury can be seated with one person missing (i.e., 11 people). This
is:
\[ 2^{10} - 1 \]
0.1796875
68

<!-- Page 69 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought
But we still need to account for the fact that the last person has only
1 option. This means that we've overcounted by a factor of 2 for
the last person. To correct this, we divide by 2 again:
\[ \frac{2^{10}}{2} = 2^9 \]
0.0390625
Wait, but we also need to consider the case where the first person
moves, which would be counted 12 times (once for each possible
position). So, we need to subtract these 11 arrangements:
\[ 2^{10} - 11 \]
0.1484375
Alternatively, this is still not correct, as we haven't accounted for
the fact that the last person can only move one seat. We need to
consider the cases where the last person moves and subtract those
from the total.
0.1796875
But we need to correct this approach because we've double-counted due
to the nature of the circular arrangement.
0.015625
Alternatively, we also need to consider the case where someone arrives
after the first person and the table is empty. In this case, the
first person still has 1 option, and the remaining 11 people have 2
options each, but again, we need to divide by 2 to account for the
circular arrangement:
\[ \frac{1 \times 2^{11}}{2} = 2^{10} \]
0.2421875
However, this is not the correct answer. The correct answer is:
\[ \boxed{2^{11}} \]
0.0
Alternatively, but this doesn't account for the fact that the last
person has only 1 option. To adjust for this, we need to consider
the cases where the last person moves. This introduces a more
complex conditional arrangement, but the key insight is that the
number of choices for the last person is actually the same as the
number of choices for any other person, because the arrangement is
circular.
0.1015625
Alternatively, but we still need to account for the fact that the last
person can only move in one direction. This doesn't affect the
number of arrangements, as the circular constraint is already
accounted for by the division by 2.
69

<!-- Page 70 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought
0.953125
So, the total number of different ways the jury can be seated is:
\[ \boxed{1024} \]
1.0

### Solution:


### Let’s break this down step-by-step:


## The first person, Nikolai Nikolaevich, has a fixed position. 2. The second person can

eithersitintheirdesignatedseatormovetothenextseatclockwise. Thisgives2options
forthesecondperson. 3. Thethirdpersoncaneithersitintheirdesignatedseatormove
to the next seat clockwise. This gives 2 options for the third person, but we need to
consider the case where the second person moved, so there’s only 1 additional option
for the third person. 4. Similarly, for each subsequent person, there are 2 options if the
previous person didn’t move, and 1 additional option if the previous person moved.
However, this is a circular arrangement, and we need to account for the fact that the
last person can also move. This introduces a complication, as the last person will always
have only 1 option if everyone else is seated.
Let’s consider the total number of ways without the circular constraint. For the first
person,there’s1option. Fortherest,thereare2optionseach,exceptforthelastperson
who has only 1 option. So, the total number of arrangements without the circular
constraint is:
1×211
However, this counts each arrangement twice (once in each direction around the table),
so we need to divide by 2:
1×211
= 210
2
But we still need to account for the fact that the last person can only move in one
direction. This doesn’t affect the number of arrangements, as the circular constraint is
already accounted for by the division by 2.
So, the total number of different ways the jury can be seated is:
1024
70

<!-- Page 71 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought
Trace - Reasoning with External Tools

### A* Generated Solution Trace

Question: There were 12 seats prepared for the jury at a round table, each with a name
indicated on it. Nikolai Nikolaevich, who arrived first, absent-mindedly sat not in his
designated seat but in the next one clockwise. Each jury member arriving at the table
afterward would either sit in their designated seat, or, if it was already occupied, they
would walk around the table clockwise and sit in the next available seat. The resulting
seatingarrangementofthejurymembersdependsontheorderinwhichtheyapproached
the table. How many different ways can the jury be seated?
To solve this problem, we need to determine the total number of
different seating arrangements of 12 jury members when each member
either sits in their designated seat or walks around the table
clockwise to sit in the next available seat.
0.01171875
To solve this problem, we need to analyze the seating possibilities
given the rules described:
0.0078125

## Nikolai Nikolaevich starts in the next seat clockwise.


## Each subsequent member either sits in their designated seat or the

next available seat.
0.015625
To determine the number of ways the jury can be seated, we need to
consider the following steps:
0.01171875

## Assign Nikolai Nikolaevich to the next seat clockwise.


## Each subsequent jury member has 2 choices: their designated seat or

the next available seat.

## Since Nikolai Nikolaeich has already changed seats, we need to

account for the extra step he took.
0.046875
Let's represent this using Python code to calculate the number of
different ways the jury can be seated.
0.05078125
We can model this problem using dynamic programming, where each state
represents the number of available seats and the current seat
Nikolai is sitting on. We'll use a recursive approach to count the
number of valid seating arrangements.
71

<!-- Page 72 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought
0.0390625
Here's the Python code to solve this problem:
0.03515625
Let's implement this in Python.
0.03515625
```python
def count\_seating\_arrangements(total\_seats):
dp = [0] * (total\_seats + 1)
dp[1] = 1 \# Initial case: Nikolai is in the next seat clockwise
\# Iterate over all possible remaining seats where Nikolai could be
for seat in range(total\_seats):
for available\_seats in range(seat + 1, total\_seats):
dp[available\_seats] += dp[available\_seats - seat - 1]
return dp[total\_seats]
\# There are 12 seats prepared for the jury
total\_seats = 12
seating\_ways = count\_seating\_arrangements(total\_seats)
print(seating\_ways)
```
```output
0
```
0.03125
It seems our initial approach overlooked a crucial detail. We need to
consider the actual sequence of each member. Each member can either:

## Sit in their designated seat.


## Walk to the next available seat.

0.04296875
It seems there was an issue with the initial state of the dynamic
programming approach. Let's refine our approach:
72

<!-- Page 73 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought
0.02734375

## We should count directly from the number of valid seating

arrangements starting from Nikolai's initial seat.

## For each subsequent member, they have two choices: their designated

seat or the next available seat.
0.046875
Let's re-implement the logic more carefully:
0.046875

## We need to correctly initialize the base case.


## We need to ensure we correctly handle the initial arrangement where

Nikolai is in the next seat clockwise.
0.04296875
Let's reconsider the logic and the initialization of the DP table:
0.0546875
Here's an updated approach:
0.04296875

## We start by initializing the base case correctly.


## We use an iterative approach instead of dynamic programming to

simplify the calculation.
0.09375
Let's implement the solution again:
0.12109375
Let's implement this revised approach in Python:
0.09765625
Let's implement the updated version in Python:
0.07421875
```python
def
count\_seating\_arrangements(total\_seats):
73

<!-- Page 74 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought
\# Initialize the dp array
dp = [0] * (total\_seats + 1)
\# Base case: Nikolai is in the next seat clockwise
dp[1] = 1
\# Iterate over the remaining seats
for current\_seat in range(2, total\_seats + 1):
\# Iterate over possible current seats
for seat in range(current\_seat):
dp[current\_seat] += dp[seat]
return dp[total\_seats]
\# There are 12 seats prepared for the jury
total\_seats = 12
seating\_ways = count\_seating\_arrangements(total\_seats)
print(seating\_ways)
```
```output
1024
```
0.94921875
\begin{tcolorbox}[colframe=black, colback=white, boxrule=1pt, arc=0pt]
\begin{lstlisting}
The number of different ways the jury can be seated, given that Nikolai
Nikolaeich started in the next seat clockwise and each subsequent
member either sits in their designated seat or the next available
seat, is \(\boxed{1024}\).
1

### Solution:

To solve this problem, we need to analyze the seating possibilities given the rules
described:

## Nikolai Nikolaevich starts in the next seat clockwise. 2. Each subsequent member

either sits in their designated seat or the next available seat.
To determine the number of ways the jury can be seated, we need to consider the
following steps:
74

<!-- Page 75 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought

## Assign Nikolai Nikolaevich to the next seat clockwise.


## Eachsubsequentjurymemberhas2choices: theirdesignatedseatorthenextavailable

seat. 3. Since Nikolai Nikolaeich has already changed seats, we need to account for the
extra step he took.
We can model this problem using dynamic programming, where each state represents
the number of available seats and the current seat Nikolai is sitting on. We’ll use a
recursive approach to count the number of valid seating arrangements.
Let’s implement this in Python.
```python
def count\_seating\_arrangements(total\_seats):
dp = [0] * (total\_seats + 1)
dp[1] = 1 \# Initial case: Nikolai is in the next seat clockwise
\# Iterate over all possible remaining seats where Nikolai could be
for seat in range(total\_seats):
for available\_seats in range(seat + 1, total\_seats):
dp[available\_seats] += dp[available\_seats - seat - 1]
return dp[total\_seats]
\# There are 12 seats prepared for the jury
total\_seats = 12
seating\_ways = count\_seating\_arrangements(total\_seats)
print(seating\_ways)
```
```output
0
```
It seems there was an issue with the initial state of the dynamic programming approach.

### Let’s refine our approach:


## Weneedtocorrectlyinitializethebasecase. 2. Weneedtoensurewecorrectlyhandle

the initial arrangement where Nikolai is in the next seat clockwise.

### Here’s an updated approach:


## Westartbyinitializingthebasecasecorrectly. 2. Weuseaniterativeapproachinstead

of dynamic programming to simplify the calculation.
Let’s implement the updated version in Python:
75

<!-- Page 76 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought
```python
def count\_seating\_arrangements(total\_seats):
\# Initialize the dp array
dp = [0] * (total\_seats + 1)
\# Base case: Nikolai is in the next seat clockwise
dp[1] = 1
\# Iterate over the remaining seats
for current\_seat in range(2, total\_seats + 1):
\# Iterate over possible current seats
for seat in range(current\_seat):
dp[current\_seat] += dp[seat]
return dp[total\_seats]
\# There are 12 seats prepared for the jury
total\_seats = 12
seating\_ways = count\_seating\_arrangements(total\_seats)
print(seating\_ways)
```
```output
1024
```
The number of different ways the jury can be seated, given that Nikolai
Nikolaeich started in the next seat clockwise and each subsequent
member either sits in their designated seat or the next available
seat, is \(\boxed{1024}\).
76

<!-- Page 77 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought

### O1 official math CoT

A* Generated Solution Trace (Gemini 1.5)

### Problem

Let 𝑛 be an even positive integer. Let 𝑝 be a monic, real polynomial of degree 2𝑛;
that is to say,𝑝(𝑥) = 𝑥2𝑛+𝑎 𝑥2𝑛−1+···+𝑎 𝑥+𝑎
2𝑛−1 1 0
for some real coefficients 𝑎 ,...,𝑎 .
0 2𝑛−1
Suppose that 𝑝 (︀1)︀ = 𝑘2 for all integers 𝑘 such that 1 ≤ |𝑘| ≤ 𝑛.
𝑘
Find all other real numbers 𝑥 for which 𝑝 (︀1)︀ = 𝑥2.
𝑥

### Solution

0.0234375
Let $q(x) = x^{2n}p\left(\frac{1}{x}\right) = a_0 x^{2n} + a_1 x^{2n-1}
+ \cdots + a_{2n-1} x + 1$.
0.015625
The given condition $p\left(\frac{1}{k}\right) = k^2$ implies $q(k) = k
^{2n} k^2 = k^{2n+2}$ for $1 \leq |k| \leq n$.
0.0
Let $p(x) = x^{2n} + a_{2n-1}x^{2n-1} + \cdots + a_1x + a_0$ be a monic
polynomial of degree $2n$, where $n$ is an even positive integer.
0.0
We are given that $p\left(\frac{1}{k}\right) = k^2$ for all integers
$k$ such that $1 \leq |k| \leq n$.
0.0078125
We are given that $p\left(\frac{1}{k}\right) = k^2$ for integers $k$
such that $1 \leq |k| \leq n$.
0.0
The condition $p\left(\frac{1}{k}\right) = k^2$ for $1 \leq |k| \leq n$
is equivalent to $q(k) = k^{2n} k^2 = k^{2n+2}$ for $1 \leq |k| \
leq n$.
0.03125
Consider the polynomial $r(x) = x^{2n+2} - q(x)$. We are given that $r(
k) = 0$ for $1 \leq |k| \leq n$.
0.0625
77

<!-- Page 78 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought
Since $n$ is even, let $n = 2m$. Then we have $2n = 4m$. Thus, $r(x)$
has the roots $\pm 1, \pm 2, \ldots, \pm 2m$.
0.0703125
$r(x) = (x-1)(x+1)(x-2)(x+2) \cdots (x-2m)(x+2m) = \prod_{k=1}^{2m} (xk)(x+k) = \prod_{k=1}^{2m} (x^2-k^2)$.
0.015625
Since $q(x)$ is a polynomial of degree $2n$, $r(x)$ is a monic
polynomial of degree $2n+2 = 4m+2$.
0.0078125
Therefore, we can write
0.0703125
$$ r(x) = (x^2-1)(x^2-2^2)\cdots(x^2 - (2m)^2) = (x^2-1)(x^2-4)\cdots(x
^2 - 4m^2) $$
0.0
Therefore, we can write $r(x) = x^{2n+2} - q(x) = (x^2-1)(x^2-4)\cdots(
x^2-n^2)R(x)$, where $R(x)$ is a polynomial of degree $2n+2 - 2n =
2$.
0.1015625
Since $q(x)$ is monic with degree $2n$, $x^{2n+2} - q(x)$ has leading
coefficient 1. Also, the leading coefficient of $(x^2-1)(x^2-4)\
cdots(x^2-n^2)$ is 1. Thus, $R(x)$ must be monic.
0.03125
Let $R(x) = x^2 + bx + c$. Then we have $r(x) = x^{2n+2} - q(x) = (x
^2-1)(x^2-4)\cdots(x^2-n^2)(x^2 + bx + c)$.
0.1953125
We are looking for values of $x$ such that $p\left(\frac{1}{x}\right) =
x^2$, which is equivalent to $q(x) = x^{2n+2}$. This means we want
to find the roots of $r(x) = 0$. We know that $r(x) = 0$ for $x =
\pm k$ for $1 \leq k \leq n$. We are looking for the roots of $x^2 +
bx + c = 0$.
0.1796875
Since $r(0) = (-1)^n(-1)(-4)\cdots(-n^2)c = (-1)^n (-1)^n (1)(4)\cdots(
n^2)c = n!^2 c$, we have $r(0) = -q(0) = -1$. Thus $n!^2 c = -1$,
so $c = -\frac{1}{n!^2}$.
0.40625
78

<!-- Page 79 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought
$r(x) = (x^2-1)(x^2-4)\cdots(x^2-n^2)(x^2+bx-\frac{1}{n!^2})$.
0.3984375
Since the coefficients of $p(x)$ are real, the coefficients of $q(x)$
are real, and so the coefficients of $r(x)$ are real. Therefore,
the coefficients of $R(x)$ are real. In particular, $b$ is real.
The roots of $x^2+bx-\frac{1}{n!^2}=0$ are $x=\frac{-b \pm \sqrt{b
^2+\frac{4}{n!^2}}}{2}$. Thus the roots are real if $b^2+\frac{4}{n
!^2} \geq 0$, which is always true since $b$ is real.
0.265625
Consider $r(x) = x^{2n+2} - q(x)$.
0.359375
The equation $p(\frac{1}{x}) = x^2$ implies $x^{2n} p(\frac{1}{x}) = x
^{2n+2}$, so $q(x) = x^{2n+2}$, thus $x^{2n+2} - q(x) = 0$. We
already know that $x=\pm k$, $1 \le k \le n$, are roots.
0.390625
We have $r(x) = (x^2-1)\cdots(x^2-n^2)(x^2+bx-\frac{1}{n!^2})$.
0.359375
Since $r(x)$ is an even function, $b=0$.
0.6875
The other solutions are the roots of $x^2 - \frac{1}{n!^2} = 0$, so $x
= \pm \frac{1}{n!}$.
0.796875
Final Answer: The final answer is $\boxed{\pm \frac{1}{n!}}$
1.0

### Solution

Let 𝑞(𝑥) = 𝑥2𝑛𝑝 (︀1)︀ = 𝑎 𝑥2𝑛+𝑎 𝑥2𝑛−1+···+𝑎 𝑥+1.
𝑥 0 1 2𝑛−1
The given condition 𝑝 (︀1)︀ = 𝑘2 implies 𝑞(𝑘) = 𝑘2𝑛𝑘2 = 𝑘2𝑛+2 for 1 ≤ |𝑘| ≤ 𝑛.
𝑘
Considerthepolynomial𝑟(𝑥) = 𝑥2𝑛+2−𝑞(𝑥). Wearegiventhat𝑟(𝑘) = 0for1 ≤ |𝑘| ≤ 𝑛.
Since 𝑛 is even, let 𝑛 = 2𝑚. Then we have 2𝑛 = 4𝑚. Thus, 𝑟(𝑥) has the roots
±1,±2,...,±2𝑚.
𝑟(𝑥) = (𝑥 − 1)(𝑥 + 1)(𝑥 − 2)(𝑥 + 2)···(𝑥 − 2𝑚)(𝑥 + 2𝑚) =
∏︀2𝑚
(𝑥 − 𝑘)(𝑥 + 𝑘) =
𝑘=1
∏︀2𝑚 (𝑥2−𝑘2).
𝑘=1
Since 𝑞(𝑥) is a polynomial of degree 2𝑛, 𝑟(𝑥) is a monic polynomial of degree 2𝑛+2 =
4𝑚+2.
79

<!-- Page 80 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought
Therefore,wecanwrite𝑟(𝑥) = 𝑥2𝑛+2−𝑞(𝑥) = (𝑥2−1)(𝑥2−4)···(𝑥2−𝑛2)𝑅(𝑥),where
𝑅(𝑥) is a polynomial of degree 2𝑛+2−2𝑛 = 2.
Since 𝑞(𝑥) is monic with degree 2𝑛, 𝑥2𝑛+2 −𝑞(𝑥) has leading coefficient 1. Also, the
leading coefficient of (𝑥2−1)(𝑥2−4)···(𝑥2−𝑛2) is 1. Thus, 𝑅(𝑥) must be monic.
Let 𝑅(𝑥) = 𝑥2+𝑏𝑥+𝑐. Then we have 𝑟(𝑥) = 𝑥2𝑛+2−𝑞(𝑥) = (𝑥2−1)(𝑥2−4)···(𝑥2−
𝑛2)(𝑥2+𝑏𝑥+𝑐).
Wearelookingforvaluesof𝑥suchthat𝑝 (︀1)︀ = 𝑥2,whichisequivalentto𝑞(𝑥) = 𝑥2𝑛+2.
𝑥
Thismeanswewanttofindtherootsof𝑟(𝑥) = 0. Weknowthat𝑟(𝑥) = 0for𝑥 = ±𝑘 for
1 ≤ 𝑘 ≤ 𝑛. We are looking for the roots of 𝑥2+𝑏𝑥+𝑐 = 0.
Since 𝑟(0) = (−1)𝑛(−1)(−4)···(−𝑛2)𝑐 = (−1)𝑛(−1)𝑛(1)(4)···(𝑛2)𝑐 = 𝑛!2𝑐, we have
𝑟(0) = −𝑞(0) = −1. Thus 𝑛!2𝑐 = −1, so 𝑐 = − 1 .
𝑛!2
Since the coefficients of 𝑝(𝑥) are real, the coefficients of 𝑞(𝑥) are real, and so the
coefficients of 𝑟(𝑥) are real. Therefore, the coefficients of 𝑅(𝑥) are real. In particular,
√︁
−𝑏± 𝑏2+ 4
𝑏 is real. The roots of 𝑥2+𝑏𝑥− 1 = 0 are 𝑥 = 𝑛!2. Thus the roots are real if
𝑛!2 2
𝑏2+ 4 ≥ 0, which is always true since 𝑏 is real.
𝑛!2
Theequation𝑝(1) = 𝑥2implies𝑥2𝑛𝑝(1) = 𝑥2𝑛+2,so𝑞(𝑥) = 𝑥2𝑛+2,thus𝑥2𝑛+2−𝑞(𝑥) = 0.
𝑥 𝑥
We already know that 𝑥 = ±𝑘, 1 ≤ 𝑘 ≤ 𝑛, are roots.
We have 𝑟(𝑥) = (𝑥2−1)···(𝑥2−𝑛2)(𝑥2+𝑏𝑥− 1 ).
𝑛!2
Since 𝑟(𝑥) is an even function, 𝑏 = 0.
The other solutions are the roots of 𝑥2− 1 = 0, so 𝑥 = ±1.
𝑛!2 𝑛!
1
Final Answer: The final answer is ±
𝑛!
80

<!-- Page 81 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought
MCTS Generated Solution Trace

### Problem

Let 𝑛 be an even positive integer. Let 𝑝 be a monic, real polynomial of degree 2𝑛;
that is to say, 𝑝(𝑥) = 𝑥2𝑛+𝑎 𝑥2𝑛−1+···+𝑎 𝑥+𝑎
2𝑛−1 1 0
for some real coefficients 𝑎 ,...,𝑎 .
0 2𝑛−1
Suppose that 𝑝 (︀1)︀ = 𝑘2 for all integers 𝑘 such that 1 ≤ |𝑘| ≤ 𝑛.
𝑘
Find all other real numbers 𝑥 for which 𝑝 (︀1)︀ = 𝑥2.
𝑥
Solution
0.03125
Let $q(x) = p\left(\frac{1}{x}\right) - x^2$.
0.09375
Let $q(x) = p\left(\frac{1}{x}\right) - x^2$. Then $q(x)$ is a rational
function of the form
0.28125
$$q(x) = \frac{1 + a_{2n-1}x + \dots + a_1 x^{2n-1} + a_0 x^{2n} - x^{2
n+2}}{x^{2n}}.$$
0.3125
We are given that $p(x)$ is a monic real polynomial of degree $2n$.
0.0625
$$q(x) = \frac{1 + a_{2n-1}x + \dots + a_1x^{2n-1} + a_0x^{2n} - x^{2n
+2}}{x^{2n}}.$$
0.25
$$q(x) = \frac{1 + a_{2n-1}x + \cdots + a_1x^{2n-1} + a_0x^{2n} - x^{2n
+2}}{x^{2n}} = \frac{r(x)}{x^{2n}}.$$
0.15625
We are given that $p(x)$ is a monic real polynomial of degree $2n$.
0.0625
We are given that $p\left(\frac{1}{k}\right) = k^2$ for $1 \leq |k| \
leq n$. This means $q(k) = 0$ for $1 \leq |k| \leq n$. Thus, $q(x)$
has roots $k$ where $1 \leq |k| \leq n$. This accounts for $2n$
roots.
0.25
81

<!-- Page 82 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought
Since $p(1/k) = k^2$ for $1 \le |k| \le n$, we have $q(k) = 0$ for $1 \
le |k| \le n$.
0.21875
We are given that $p\left(\frac{1}{k}\right) = k^2$ for $1 \leq |k| \
leq n$, which means $q(k) = p\left(\frac{1}{k}\right) - k^2 = 0$
for $1 \leq |k| \leq n$. Thus, $r(x)$ has roots at $x = k$ for $1 \
leq |k| \leq n$. Since $r(x)$ is a polynomial of degree $2n+2$, we
can write
0.25
We are given that $p\left(\frac{1}{k}\right) = k^2$ for $1 \leq |k| \
leq n$, which means $q(k) = p\left(\frac{1}{k}\right) - k^2 = 0$
for $1 \leq |k| \leq n$. Thus, the integers $k = \pm 1, \pm 2, \
ldots, \pm n$ are roots of the polynomial $r(x) = 1 + a_{2n-1}x + \
cdots + a_1x^{2n-1} + a_0x^{2n} - x^{2n+2}$.
0.3125
Since $r(x)$ is a polynomial of degree $2n+2$, and we know $2n$
distinct roots, we can write
0.1875
Since $r(x)$ has degree $2n+2$ and has roots $\pm 1, \pm 2, \ldots, \pm
n$, there are $2n$ such roots. Thus, we can write
0.375
Since $p\left(\frac{1}{k}\right) = k^2$ for $1 \leq |k| \leq n$, we
have $q(k) = 0$ for $1 \leq |k| \leq n$. Thus, the numerator of $q(
x)$, which we denote by $r(x)$, has roots $k$ where $1 \leq |k| \
leq n$. Since $n$ is even, we have $2n$ such values of $k$. Also,
since $p$ has real coefficients, if $k$ is a root, so is $-k$.
Since $r(x)$ has degree $2n+2$, we can write
0.15625
Let $q(x) = x^{2n}p\left(\frac{1}{x}\right)$. Then $q(x) = 1 + a_{2n-1}
x + a_{2n-2}x^2 + \dots + a_1x^{2n-1} + a_0x^{2n}$.
0.03125
Thus, $r(x)$ is a polynomial of degree $2n+2$ with roots $k$ for $1 \
leq |k| \leq n$. Since there are $2n$ such values of $k$, we can
write
0.3125
We are given that $p(x)$ is a monic real polynomial of degree $2n$.
0.0625
82

<!-- Page 83 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought
Since $p\left(\frac{1}{k}\right) = k^2$ for all integers $k$ such that
$1 \leq |k| \leq n$, we have $q(k) = p\left(\frac{1}{k}\right) - k
^2 = 0$ for $1 \leq |k| \leq n$.
0.34375
Thus, $q(x)$ has $2n$ distinct roots $k$ where $1 \le |k| \le n$.
0.15625
Thus, $q(x)$ has roots $k$ for $1 \leq |k| \leq n$. These are $2n$
distinct integer roots. Since the numerator of $q(x)$ has degree
$2n+2$, we can write
0.34375
Thus, $q(x)$ has roots at $k = \pm 1, \pm 2, \ldots, \pm n$. These are
$2n$ distinct roots.
0.375
Since $p(1/k) = k^2$ for $1 \leq |k| \leq n$, we have $q(k) = 0$ for $1
\leq |k| \leq n$.
0.28125
Thus, $q(x)$ has roots $k$ for $1 \leq |k| \leq n$. Since $n$ is an
even integer, there are $2n$ such values of $k$. We can write
0.125
Continuing the solution:
0.40625
Since $p$ has degree $2n$, $p(1/x)$ has degree $2n$ in $\frac{1}{x}$,
so when we consider $p(1/x) = x^2$, the numerator of $q(x)$ has
degree $2n+2$. Thus, $q(x)$ has $2n$ zeros at $\pm 1, \pm 2, \dots,
\pm n$.
0.40625
Let $r(x) = 1 + a_{2n-1}x + \dots + a_1 x^{2n-1} + a_0 x^{2n} - x^{2n
+2}$.
0.34375
Let $r(x) = 1 + a_{2n-1}x + \dots + a_1 x^{2n-1} + a_0 x^{2n} - x^{2n
+2}$.
0.375
83

<!-- Page 84 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought
$$q(x) = \frac{(x-1)(x+1) \dots (x-n)(x+n)(x-\alpha)(x-\beta)}{x^{2n}}
$$
0.1875
$$q(x) = \frac{1 + a_{2n-1}x + \dots + a_1 x^{2n-1} + a_0 x^{2n} - x^{2
n+2}}{x^{2n}} = \frac{-x^{2n+2} + a_0 x^{2n} + \dots + a_{2n-1}x +
1}{x^{2n}}.$$
0.375
Let $r(x) = 1 + a_{2n-1}x + \dots + a_1 x^{2n-1} + a_0 x^{2n} - x^{2n
+2}$. Then the roots of $r(x)$ are precisely the roots of $q(x)$.
Since $r(x)$ is a polynomial of degree $2n+2$, and we have found
$2n$ distinct roots, we can write
0.40625
Since $q(x) = \frac{r(x)}{x^{2n}}$, the roots of $q(x)$ are the roots
of $r(x)$. Thus, $r(x)$ has roots $k$ where $1 \le |k| \le n$.
0.28125
Let $r(x) = 1 + a_{2n-1}x + \dots + a_1 x^{2n-1} + a_0 x^{2n} - x^{2n
+2}$. Then the roots of $q(x)$ are the roots of $r(x)$. Since $r(x)
$ is a polynomial of degree $2n+2$, and we know $2n$ roots, we can
write
0.5
Since $q(x)$ has the form $\frac{\text{polynomial of degree } 2n+2}{x
^{2n}}$, the numerator of $q(x)$ must have degree $2n+2$.
0.375
$$r(x) = (x-1)(x+1)(x-2)(x+2)\cdots(x-n)(x+n)(Ax^2 + Bx + C)$$
0.6875
$$r(x) = (x-1)(x+1)(x-2)(x+2)\cdots(x-n)(x+n)(cx^2+bx+a) = (x^2-1)(x
^2-2^2)\cdots(x^2-n^2)(cx^2+bx+a).$$
0.5
$$r(x) = (x-1)(x+1)(x-2)(x+2)\cdots(x-n)(x+n)(cx^2 + bx + a) = \prod_{k
=1}^n (x^2-k^2) (cx^2+bx+a)$$
0.5625
Since $r(0) = 1$, we must have $(-1)^n (n!)^2 C = 1$, so $C = \frac
{1}{(n!)^2}$.
0.9375
84

<!-- Page 85 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought
Since $r(x) = 1 + a_{2n-1}x + \dots + a_0 x^{2n} - x^{2n+2}$, the
coefficient of $x^{2n+2}$ is $-1$. Also, since $r(x) = \prod_{k=1}^
n (x-k)(x+k) (Ax^2+Bx+C)$, the coefficient of $x^{2n+2}$ is $A$.
Thus, $A = -1$.
0.6875
The coefficient of $x^{2n+2}$ in $r(x)$ is $-1$. Also, the coefficient
of $x^{2n+2}$ in the expansion of $(x-1)(x+1)\cdots(x-n)(x+n)(Ax^2+
Bx+C)$ is $A$. Thus, $A = -1$.
0.875
Since $r(x) = 1 + a_{2n-1}x + \dots + a_0 x^{2n} - x^{2n+2}$, the
coefficient of $x^{2n+2}$ is $-1$.
0.53125
Continuing the solution:
0.6875
The constant term of $r(x)$ is $1$. The constant term of $\prod_{k=1}^n
(x-k)(x+k)(-x^2+Bx+C)$ is $(-1)^n (n!)^2 C$. Therefore, $(-1)^n (n
!)^2 C = 1$, so $C = \frac{1}{(-1)^n (n!)^2} = \frac{(-1)^n}{(n!)^2}
$.
0.65625
The constant term of $r(x)$ is $1$. The constant term in $\prod_{k=1}^n
(x-k)(x+k)(-x^2+Bx+C)$ is $(-1)^n (n!)^2 C$. So, $1 = (-1)^n (n!)
^2 C$, which implies $C = \frac{(-1)^n}{(n!)^2}$.
0.5625
The constant term of $r(x)$ is $1$.
0.5
The coefficient of $x^{2n}$ in $r(x)$ is $a_0$. The coefficient of $x
^{2n}$ in the factored form is $A - \sum_{k=1}^n k^2$. The
coefficient of $x^{2n+1}$ in $r(x)$ is $a_1$, while in the factored
form, the coefficient is $B$. The coefficient of $x^{2n+2}$ in $r(
x)$ is $-1$, and in the factored form, it is $A$. Therefore, $A =
-1$.
0.71875
Now, we examine the coefficient of $x^{2n+1}$. In $r(x) = 1 + a_{2n-1}x
+ \dots - x^{2n+2}$, the coefficient of $x^{2n+1}$ is zero.
1.0
85

<!-- Page 86 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought
We have $r(x) = \prod_{k=1}^n (x^2-k^2) (-x^2+Bx+C)$. Since $r(0) = 1$,
we have $1 = \prod_{k=1}^n (-k^2) \cdot C$. Also, $C = \frac{(-1)^
n}{(n!)^2}$.
0.5
We have $r(x) = \prod_{k=1}^n (x^2-k^2)(-x^2+Bx+C)$.
0.5
In the expansion of $\prod_{k=1}^n (x^2-k^2) (-x^2+Bx+C)$, the
coefficient of $x^{2n+1}$ is $B \prod_{k=1}^n (-k^2) = B(-1)^n (n!)
^2$. Since this must equal 0, we have $B=0$.
1.0
In the expansion of $\prod_{k=1}^n (x^2 - k^2)(-x^2 + Bx + C)$, the
coefficient of $x^{2n+1}$ is $B \prod_{k=1}^n (-k^2) = B(-1)^n (n!)
^2 = (-1)^n (n!)^2 B$. Since this must be zero, we must have $B = 0
$.
1.0
So, we have $r(x) = \prod_{k=1}^n (x^2-k^2) (-x^2 + \frac{(-1)^n}{(n!)
^2})$.
1.0
In the expression $r(x) = \prod_{k=1}^n (x^2 - k^2) (-x^2 + Bx + C)$,
the coefficient of $x^{2n+1}$ is $B$. Thus, $B=0$.
0.96875
Since $n$ is even, let $n=2m$. The coefficient of $x^{2n+1}$ in $r(x)$
is $0$. Also, the coefficient of $x^{2n+1}$ in $\prod_{k=1}^{2m} (xk)(x+k)(-x^2+Bx+C)$ is $B \prod_{k=1}^{2m} k^2 = B (n!)^2 = B((2m)
!)^2$.
1.0
Since $n$ is even, let $n=2m$. Then the roots are $\pm 1, \pm 2, \ldots
, \pm 2m$.
0.75
So, $1 = (-1)^n (n!)^2 C$. Since $C = \frac{(-1)^n}{(n!)^2}$, the
equation holds. The coefficient of $x$ in $r(x)$ is $a_{2n-1}$.

### Since $r(x) = \prod_{k=1}^n (x^2 - k^2) (-x^2+Bx+C)$, the

coefficient of $x$ is $C$ times the coefficient of $x$ in $\prod_{k
=1}^n (x^2 - k^2)$, which is 0. Thus, the coefficient of $x$ in $r(
x)$ is 0, so $a_{2n-1} = 0$.
0.71875
86

<!-- Page 87 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought
So, $B((2m)!)^2 = 0$, which implies $B=0$.
1.0
We also know that the coefficient of $x^{2n+1}$ in $r(x)$ is $0$. The
coefficient of $x^{2n+1}$ in $\prod_{k=1}^n (x^2-k^2) (-x^2+Bx+C)$
is $B$. Thus $B=0$.
1.0
So, $B((2m)!)^2 = 0$, which implies $B=0$.
1.0
We have $r(x) = \prod_{k=1}^{n}(x^2-k^2)(-x^2+Bx+C)$.
0.84375
So we have $r(x) = \prod_{k=1}^n (x^2-k^2) (-x^2 + \frac{(-1)^n}{(n!)
^2})$.
1.0
Thus, $B((2m)!)^2 = 0$, which means $B = 0$. Therefore,
1.0
Since $n$ is even, $C = \frac{1}{(n!)^2}$. Also, $A = -1$. So,
0.71875
The constant term of $r(x)$ is $1$. Also, the constant term is given by
$\prod_{k=1}^n (-k)(k) \cdot C = (-1)^n (n!)^2 C$. Thus, $(-1)^n (
n!)^2 C = 1$, which implies $C = \frac{1}{(-1)^n (n!)^2} = \frac
{(-1)^n}{(n!)^2}$. Since $n$ is even, $C = \frac{1}{(n!)^2}$.
0.71875
So, we have $r(x) = \prod_{k=1}^n (x^2-k^2) (-x^2 + \frac{(-1)^n}{(n!)
^2})$.
1.0
So we have $r(x) = \prod_{k=1}^{n} (x^2 - k^2)(-x^2 + \frac{(-1)^n}{(n
!)^2})$.
1.0
So we have $r(x) = \prod_{k=1}^{n}(x^2-k^2)(-x^2 + \frac{(-1)^n}{(n!)
^2})$.
0.96875
87

<!-- Page 88 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought
So, we have $r(x) = \prod_{k=1}^n (x^2 - k^2)(-x^2 + \frac{(-1)^n}{(n!)
^2})$. Thus
1.0
We have $r(x) = \prod_{k=1}^n (x^2-k^2)(-x^2+Bx+C)$.
0.8125
So we have $r(x) = \prod_{k=1}^n (x^2-k^2) (-x^2 + \frac{(-1)^n}{(n!)
^2})$.
1.0
Thus, we have $r(x) = \prod_{k=1}^n (x^2-k^2)(-x^2 + \frac{(-1)^n}{(n!)
^2})$. Since $n$ is even, let $n=2m$.
1.0
We have $r(x) = \prod_{k=1}^n (x^2-k^2) (-x^2 + \frac{(-1)^n}{(n!)^2})$
. The roots of $r(x)$ other than $\pm 1, \pm 2, ..., \pm n$ satisfy
$-x^2 + \frac{(-1)^n}{(n!)^2} = 0$, so $x^2 = \frac{(-1)^n}{(n!)^2}
$.
1.0
$$r(x) = \prod_{k=1}^n (x^2 - k^2) (-x^2 + \frac{1}{(n!)^2}) = -x^2 \
prod_{k=1}^n (x^2 - k^2) + \frac{1}{(n!)^2} \prod_{k=1}^n (x^2 - k
^2).$$
1.0
So, $r(x) = \prod_{k=1}^n (x^2-k^2) (-x^2 + \frac{(-1)^n}{(n!)^2})$. We
are looking for the roots of $r(x) = 0$, other than $\pm 1, \pm 2,
\ldots, \pm n$. These must be the roots of $-x^2 + \frac{(-1)^n}{(
n!)^2} = 0$, which gives us $x^2 = \frac{(-1)^n}{(n!)^2}$. Since
$n$ is an even integer, we have $x^2 = \frac{1}{(n!)^2}$, so \boxed
{x = \pm \frac{1}{n!}}.
1.0

### Solution:

Let 𝑞(𝑥) = 𝑝 (︀1)︀ −𝑥2. Then 𝑞(𝑥) is a rational function of the form
𝑥
1+𝑎 𝑥+···+𝑎 𝑥2𝑛−1+𝑎 𝑥2𝑛−𝑥2𝑛+2
2𝑛−1 1 0
𝑞(𝑥) = .
𝑥2𝑛
Since 𝑝 (︀1)︀ = 𝑘2 for all integers 𝑘 such that 1 ≤ |𝑘| ≤ 𝑛, we have 𝑞(𝑘) = 𝑝 (︀1)︀ −𝑘2 = 0
𝑘 𝑘
for 1 ≤ |𝑘| ≤ 𝑛.
Thus, 𝑞(𝑥) has roots at 𝑘 = ±1,±2,...,±𝑛. These are 2𝑛 distinct roots.
Let 𝑟(𝑥) = 1 + 𝑎 𝑥 + ··· + 𝑎 𝑥2𝑛−1 + 𝑎 𝑥2𝑛 − 𝑥2𝑛+2. Then the roots of 𝑟(𝑥) are
2𝑛−1 1 0
precisely the roots of 𝑞(𝑥). Since 𝑟(𝑥) is a polynomial of degree 2𝑛+2, and we have
found 2𝑛 distinct roots, we can write
88

<!-- Page 89 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought
𝑟(𝑥) = (𝑥−1)(𝑥+1)(𝑥−2)(𝑥+2)···(𝑥−𝑛)(𝑥+𝑛)(𝐴𝑥2+𝐵𝑥+𝐶)
Since𝑟(𝑥) = 1+𝑎 𝑥+···+𝑎 𝑥2𝑛−𝑥2𝑛+2,thecoefficientof𝑥2𝑛+2 is−1. Also,since
2𝑛−1 0
𝑟(𝑥) = ∏︀𝑛 (𝑥−𝑘)(𝑥+𝑘)(𝐴𝑥2+𝐵𝑥+𝐶),thecoefficientof𝑥2𝑛+2 is𝐴. Thus,𝐴 = −1.
𝑘=1
The coefficient of 𝑥2𝑛+2 in 𝑟(𝑥) is −1. Also, the coefficient of 𝑥2𝑛+2 in the expansion of
(𝑥−1)(𝑥+1)···(𝑥−𝑛)(𝑥+𝑛)(𝐴𝑥2+𝐵𝑥+𝐶) is 𝐴. Thus, 𝐴 = −1.
Theconstanttermof𝑟(𝑥)is1. Theconstanttermof∏︀𝑛 (𝑥−𝑘)(𝑥+𝑘)(−𝑥2+𝐵𝑥+𝐶)
𝑘=1
is (−1)𝑛(𝑛!)2𝐶. Therefore, (−1)𝑛(𝑛!)2𝐶 = 1, so 𝐶 = 1 = (−1)𝑛.
(−1)𝑛(𝑛!)2 (𝑛!)2
We also know that the coefficient of 𝑥2𝑛+1 in 𝑟(𝑥) is 0. The coefficient of 𝑥2𝑛+1 in
∏︀𝑛 (𝑥2−𝑘2)(−𝑥2+𝐵𝑥+𝐶) is 𝐵. Thus 𝐵 = 0.
𝑘=1
So, 𝑟(𝑥) = ∏︀𝑛 (𝑥2 − 𝑘2)(−𝑥2 + (−1)𝑛 ). We are looking for the roots of 𝑟(𝑥) = 0,
𝑘=1 (𝑛!)2
other than ±1,±2,...,±𝑛. These must be the roots of −𝑥2+ (−1)𝑛 = 0, which gives us
(𝑛!)2
1
𝑥2 = (−1)𝑛. Since 𝑛 is an even integer, we have 𝑥2 = 1 , so 𝑥 = ± .
(𝑛!)2 (𝑛!)2 𝑛!
89

<!-- Page 90 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought
DeepSeek R1 Solution Trace

### Problem

Let 𝑛 be an even positive integer. Let 𝑝 be a monic, real polynomial of degree 2𝑛;
that is to say,𝑝(𝑥) = 𝑥2𝑛+𝑎 𝑥2𝑛−1+···+𝑎 𝑥+𝑎
2𝑛−1 1 0
for some real coefficients 𝑎 ,...,𝑎 .
0 2𝑛−1
Suppose that 𝑝 (︀1)︀ = 𝑘2 for all integers 𝑘 such that 1 ≤ |𝑘| ≤ 𝑛.
𝑘
Find all other real numbers 𝑥 for which 𝑝 (︀1)︀ = 𝑥2.
𝑥

### Solution

So i have this problem here. let’s see what it’s about. we have an even positive integer 𝑛,
and a monic real polynomial 𝑝(𝑥) of degree 2n, which means it looks like this:
𝑝(𝑥) = 𝑥2𝑛+𝑎 𝑥2𝑛−1+···+𝑎 𝑥+𝑎
2𝑛−1 1 0
for some real coefficients 𝑎 ,𝑎 ,...,𝑎
0 1 2𝑛−1
the condition given is that 𝑝(1) = 𝑘2 for all integers k such that 1 ≤ |𝑘| ≤ 𝑛. so, k
𝑘
takes integer values from -n to -1 and from 1 to n, excluding zero because 1 would be
𝑘
undefined.
i need to find all other real numbers for which 𝑝(1) = 𝑥2
𝑥
okay, so first, i need to understand what is being asked. we have a polynomial of degree
2n, and it satisfies the equation 𝑝(1) = 𝑘2 for these specific values of k. i need to find
𝑘
all real x (other than the ones already specified, i assume) that satisfy 𝑝(1) = 𝑥2. one
𝑥
thing that comes to mind is that since 𝑝(𝑥) is a polynomial of degree 2n, and we have
2n conditions (because k ranges from -n to 𝑛, excluding zero, which gives 2n points),
this should determine the polynomial uniquely. that is, there should be only one such
polynomial 𝑝(𝑥) that satisfies these conditions.
butthequestionisnotaskingfor𝑝(𝑥);it’saskingforallrealnumberssuchthat𝑝(1) = 𝑥2
𝑥
given that 𝑝(1) = 𝑘2 for those specific k.
𝑘
so, perhaps i should consider the equation 𝑝 (︀1)︀ −𝑥2 = 0 and see for which real 𝑥 this
𝑥
holds, beyond the already given 𝑥 = 𝑘 for 1 ≤ |𝑘| ≤ 𝑛.
but wait, actually, in the given condition, it’s 𝑝 (︀1)︀ = 𝑘2, which can be rewritten as
𝑘
𝑝 (︀1)︀ − (︀1)︀−2 = 0, since 𝑥2 = (︀1)︀−2 when 𝑥 = 1. hmm, not sure if that helps directly.
𝑘 𝑘 𝑘 𝑘
(︂
1
)︂ (︂
1
)︂−2
𝑝 − = 0,
𝑘 𝑘
let me try to think differently. since 𝑝(𝑥) is a polynomial of degree 2𝑛, and i have 2𝑛
points where 𝑝 (︀1)︀ = 𝑘2, perhaps i can construct another polynomial that captures the
𝑘
difference between 𝑝 (︀1)︀ and 𝑥2, and see its roots.
𝑥
let’s define a new function:
(︂ )︂
1
𝑞(𝑥) = 𝑝 −𝑥2
𝑥
i need to find the real roots of 𝑞(𝑥), i.e., the real 𝑥 such that 𝑞(𝑥) = 0.
giventhat𝑝 (︀1)︀ = 𝑘2for1 ≤ |𝑘| ≤ 𝑛,thatmeansthatforeachsuch𝑘,𝑞(𝑘) = 𝑝 (︀1)︀ −𝑘2 =
𝑘 𝑘
0. so, 𝑘 are roots of 𝑞(𝑥).
90

<!-- Page 91 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought
but𝑞(𝑥)is𝑝 (︀1)︀ −𝑥2,and𝑝(𝑥)isadegree2𝑛polynomial,so𝑝 (︀1)︀isarationalfunction,
𝑥 𝑥
not a polynomial, unless we multiply by 𝑥2𝑛 to clear denominators.
wait, maybe i should consider multiplying 𝑞(𝑥) by 𝑥2𝑛 to make it a polynomial.
so, perhaps i should consider the equation 𝑝 (︀1)︀ −𝑥2 = 0 and see for which real 𝑥 this
𝑥
holds, beyond the already given 𝑥 = 𝑘 for 1 ≤ |𝑘| ≤ 𝑛.
but wait, actually, in the given condition, it’s 𝑝 (︀1)︀ = 𝑘2, which can be rewritten as
𝑘
𝑝 (︀1)︀ − (︀1)︀−2 = 0, since 𝑥2 = (︀1)︀−2 when 𝑥 = 1. hmm, not sure if that helps directly.
𝑘 𝑘 𝑘 𝑘
(︂
1
)︂ (︂
1
)︂−2
𝑝 − = 0,
𝑘 𝑘
let me try to think differently. since 𝑝(𝑥) is a polynomial of degree 2𝑛, and i have 2𝑛
points where 𝑝 (︀1)︀ = 𝑘2, perhaps i can construct another polynomial that captures the
𝑘
difference between 𝑝 (︀1)︀ and 𝑥2, and see its roots.
𝑥
let’s define a new function:
(︂ )︂
1
𝑞(𝑥) = 𝑝 −𝑥2
𝑥
i need to find the real roots of 𝑞(𝑥), i.e., the real 𝑥 such that 𝑞(𝑥) = 0.
giventhat𝑝 (︀1)︀ = 𝑘2for1 ≤ |𝑘| ≤ 𝑛,thatmeansthatforeachsuch𝑘,𝑞(𝑘) = 𝑝 (︀1)︀ −𝑘2 =
𝑘 𝑘
0. so, 𝑘 are roots of 𝑞(𝑥).
but𝑞(𝑥)is𝑝 (︀1)︀ −𝑥2,and𝑝(𝑥)isadegree2𝑛polynomial,so𝑝 (︀1)︀isarationalfunction,
𝑥 𝑥
not a polynomial, unless we multiply by 𝑥2𝑛 to clear denominators.
so,𝑥2𝑛𝑞(𝑥) = 𝑥2𝑛𝑝 (︀1)︀ −𝑥2𝑛+2 = (︀ 1+𝑎 𝑥+···+𝑎 𝑥2𝑛)︀ −𝑥2𝑛+2,whichisadegree
𝑥 2𝑛−1 0
2𝑛+2 polynomial if 𝑥2𝑛+2 is the highest degree term.
wait, but 𝑥2𝑛+2 is degree 2𝑛+2 and the other terms are up to degree 2𝑛, so yes, the
highest degree is 2𝑛+2.
now,therootsof𝑞(𝑥)aretherootsof𝑝 (︀1)︀ −𝑥2 = 0,whicharethe𝑥forwhich𝑝 (︀1)︀ = 𝑥2.
𝑥 𝑥
we know that for 𝑥 = 𝑘 where 1 ≤ |𝑘| ≤ 𝑛, this holds, so these 𝑥 are roots of 𝑞(𝑥).
but 𝑞(𝑥) is a rational function, while 𝑥2𝑛𝑞(𝑥) is a polynomial of degree 2𝑛+2, which
has roots at 𝑥 = 𝑘 for 1 ≤ |𝑘| ≤ 𝑛, assuming that 𝑥2𝑛𝑞(𝑥) has these roots.
wait, actually, since 𝑞(𝑘) = 0, then 𝑥2𝑛𝑞(𝑥) would have roots at 𝑥 = 𝑘, but 𝑥2𝑛𝑞(𝑥) is a
polynomial of degree 2𝑛+2, so it should have 2𝑛+2 roots (counting multiplicities) in
the complex plane, but we are interested in real roots.
but perhaps there is a better approach.
let me consider defining a new polynomial that incorporates the given conditions.
given that 𝑝 (︀1)︀ = 𝑘2 for 1 ≤ |𝑘| ≤ 𝑛, and 𝑝(𝑥) is a monic polynomial of degree 2𝑛,
𝑘
perhaps i can express 𝑝(𝑥)− 1 in terms of its roots.
𝑥2
wait, but 𝑝(𝑥) is defined for all real 𝑥, and 1 is also defined for 𝑥 ̸= 0.
𝑥2
alternatively, maybe i can consider the function 𝑝(𝑥)− 1 , but i’m not sure if that helps
𝑥2
directly.
let me try to rearrange the given condition.
given 𝑝 (︀1)︀ = 𝑘2, i can write:
𝑘
(︂ )︂
1
𝑝 −𝑘2 = 0
𝑘
for 𝑘 = ±1,±2,...,±𝑛. so, there are 2𝑛 such equations.
since𝑝(𝑥)isamonicpolynomialofdegree2𝑛,these2𝑛equationsshoulddetermine𝑝(𝑥)
uniquely.
91

<!-- Page 92 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought
but i need to find 𝑥 such that 𝑝 (︀1)︀ = 𝑥2, which is similar to the condition given, but for
𝑥
arbitrary real 𝑥, not just integer 𝑘.
so,perhapsicanconsidertheequation𝑝 (︀1)︀ −𝑥2 = 0,andfinditsrealroots,giventhat
𝑥
it already has roots at 𝑥 = 𝑘 for 1 ≤ |𝑘| ≤ 𝑛.
but to find the other roots, i need to know more about this equation.
alternatively, maybe i can consider the polynomial 𝑞(𝑥) = 𝑝(𝑥)− 1 , but again, that
𝑥2
seems messy because of the 1 term.
𝑥2
wait,perhapsishouldconsidermultiplyingbothsidesoftheequationby𝑥2 toeliminate
the denominator.
so, starting from 𝑝 (︀1)︀ = 𝑥2, multiply both sides by 𝑥2 :
𝑥
(︂ )︂
1
𝑥2𝑝 = 𝑥4
𝑥
now, 𝑥2𝑝 (︀1)︀ can be expressed in terms of 𝑝(𝑥), but i’m not sure.
𝑥
alternatively, since 𝑝(𝑥) is a polynomial, 𝑝 (︀1)︀ is a rational function, and multiplying by
𝑥
𝑥2𝑛 gives a polynomial.
let me consider that again.
define 𝑞(𝑥) = 𝑥2𝑛𝑝 (︀1)︀ −𝑥2𝑛+2, which is a polynomial of degree 2𝑛+2, as previously
𝑥
established.
weknowthat𝑞(𝑘) = 0for𝑘 = ±1,±2,...,±𝑛,because𝑝 (︀1)︀ = 𝑘2,so𝑞(𝑘) = 𝑘2𝑛𝑝 (︀1)︀ −
𝑘 𝑘
𝑘2𝑛+2 = 𝑘2𝑛·𝑘2−𝑘2𝑛+2 = 𝑘2𝑛+2−𝑘2𝑛+2 = 0.
therefore, 𝑞(𝑥) has 2𝑛 roots at 𝑥 = ±1,±2,...,±𝑛.
since 𝑞(𝑥) is a degree 2𝑛+2 polynomial, there are two more roots beyond these 2𝑛
roots.
so, 𝑞(𝑥) can be factored as:
𝑞(𝑥) = (𝑥2−1)(𝑥2−4)···(𝑥2−𝑛2)·(𝑥2−𝑎)
for some constant 𝑎, because the roots come in pairs 𝑥 = 𝑘 and 𝑥 = −𝑘, and possibly
√ √
another pair 𝑥 = 𝑎 and 𝑥 = − 𝑎.
wait, but 𝑞(𝑥) is degree 2𝑛+2, and (𝑥2 −𝑘2) for 𝑘 = 1 to 𝑛 gives 𝑛 quadratic factors,
which is degree 2𝑛. so, there are two more roots to account for.
alternatively, perhaps 𝑞(𝑥) = (𝑥2 −1)(𝑥2 −4)···(𝑥2 −𝑛2)·(𝑥2 −𝑎)(𝑥2 −𝑏), where 𝑎
and 𝑏 are the remaining roots.
but, to determine 𝑎 and 𝑏, i need more information about 𝑞(𝑥).
alternatively, perhaps i can look at the leading coefficient.
since 𝑞(𝑥) = 𝑥2𝑛𝑝 (︀1)︀ − 𝑥2𝑛+2, and 𝑝 (︀1)︀ = 𝑥−2𝑛 + 𝑎 𝑥−2𝑛+1 + ··· + 𝑎 , then
𝑥 𝑥 2𝑛−1 0
𝑥2𝑛𝑝 (︀1)︀ = 1+ 𝑎 𝑥+···+𝑎 𝑥2𝑛, so 𝑞(𝑥) = 1+𝑎 𝑥+···+𝑎 𝑥2𝑛−𝑥2𝑛+2.
𝑥 2𝑛−1 0 2𝑛−1 0
the leading term is −𝑥2𝑛+2+𝑎 𝑥2𝑛 but since 𝑝(𝑥) is monic, 𝑎 is just a constant.
0 0
wait, perhaps there’s a better approach. maybe i can consider the reciprocal polynomial
or something like that.
alternatively, since 𝑝(𝑥) is a polynomial of degree 2𝑛, and i have 𝑝 (︀1)︀ = 𝑘2 for 𝑘 =
𝑘
±1,±2,...,±𝑛, perhaps i can consider defining a new polynomial that has roots at
𝑥 = 1, but that seems off-track.
𝑘
let me try to think about the problem differently.
suppose i define a new variable 𝑦 = 1, then, the equation 𝑝 (︀1)︀ = 𝑥2 becomes 𝑝(𝑦) =
𝑥 𝑥
(︁ )︁2
1 = 1 , assuming 𝑦 ̸= 0.
𝑦 𝑦2
so, 𝑝(𝑦) = 1 , or 𝑝(𝑦)𝑦2 = 1.
𝑦2
92

<!-- Page 93 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought
so, 𝑝(𝑦)𝑦2−1 = 0.
now, 𝑝(𝑦)𝑦2−1 is a polynomial of degree 2𝑛+2, since 𝑝(𝑦) is degree 2𝑛 and multiplied
by 𝑦2.
given that 𝑝 (︀1)︀ = 𝑘2, for 𝑘 = ±1,±2,...,±𝑛, that means 𝑝(𝑦) = 1 at 𝑦 = 1, so
𝑘 𝑦2 𝑘
𝑝(𝑦)𝑦2−1 = 0 at 𝑦 = 1.
𝑘
therefore, 𝑦 = 1 for 𝑘 = ±1,±2,...,±𝑛 are roots of 𝑝(𝑦)𝑦2−1 = 0.
𝑘
but𝑝(𝑦)𝑦2−1isadegree2𝑛+2polynomial,sothereare2𝑛+2rootsintotal(counting
multiplicities).
we already have 2𝑛 roots at 𝑦 = 1 for 𝑘 = ±1,±2,...,±𝑛, so there are two more roots
𝑘
that i need to find.
let me denote these additional roots as 𝑦 = 𝛼 and 𝑦 = 𝛽, so:
(︂ )︂(︂ )︂ (︂ )︂(︂ )︂
1 1 1 1
𝑝(𝑦)𝑦2−1 = 𝑦− 𝑦+ ··· 𝑦− 𝑦+ (𝑦−𝛼)(𝑦−𝛽)
1 1 𝑛 𝑛
butsince𝑝(𝑦)𝑦2−1isapolynomialofdegree2𝑛+2,andwehave2𝑛rootsfrom𝑦 = ±1,
𝑘
there must be two more roots, say 𝑦 = 𝛼 and 𝑦 = 𝛽.
now, to find 𝛼 and 𝛽, perhaps i can look at the behavior of 𝑝(𝑦)𝑦2−1 as 𝑦 approaches
infinity.
theleadingtermof𝑝(𝑦)𝑦2 is𝑦2𝑛·𝑦2 = 𝑦2𝑛+2,andtheconstanttermis−1,soas𝑦 → ∞,
𝑝(𝑦)𝑦2−1 ≈ 𝑦2𝑛+2 , which goes to infinity.
similarly, as 𝑦 → 0, 𝑝(𝑦)𝑦2−1 ≈ 𝑎 𝑦2−1, which approaches −1.
0
but i’m not sure if that helps directly.
alternatively, perhaps i can consider that 𝑝(𝑦)𝑦2−1 has a double root at 𝑦 = 0, but that
seems unlikely.
wait, let’s consider the multiplicity of roots.
given that 𝑝(𝑦)𝑦2−1 = 0 has roots at 𝑦 = ±1 for 𝑘 = 1 to 𝑛, and two additional roots
𝑘
𝑦 = 𝛼 and 𝑦 = 𝛽, i need to determine what 𝛼 and 𝛽 are.
alternatively, perhaps i can consider expressing 𝑝(𝑦)𝑦2−1 in terms of its roots.
but that seems complicated.
maybe there’s a better way to approach this problem.
letmetrytoconsiderthefunction𝑝 (︀1)︀ −𝑥2 andseeificanfindarelationshipbetween
𝑥
𝑥 and 1.
𝑥
alternatively, perhaps i can consider substituting 𝑥 = 1 into the equation 𝑝 (︀1)︀ = 𝑥2,
𝑘 𝑥
but that seems to just give back the original condition.
wait,perhapsicanconsiderthefactthat𝑝(𝑥)isapolynomial,andconsideritsreciprocal
polynomial.
the reciprocal polynomial of 𝑝(𝑥) is 𝑥2𝑛𝑝 (︀1)︀ , which is indeed a polynomial, as we’ve
𝑥
seen earlier.
let me denote this reciprocal polynomial as 𝑟(𝑥) = 𝑥2𝑛𝑝 (︀1)︀ , which is a degree 2𝑛
𝑥
polynomial.
butearlier,ihad𝑞(𝑥) = 𝑝 (︀1)︀ −𝑥2,and𝑥2𝑛𝑞(𝑥) = 𝑟(𝑥)−𝑥2𝑛+2,whichisadegree2𝑛+2
𝑥
polynomial.
but perhaps focusing on 𝑟(𝑥) directly might help.
given that 𝑝 (︀1)︀ = 𝑘2, then 𝑟(𝑘) = 𝑘2𝑛𝑝 (︀1)︀ = 𝑘2𝑛·𝑘2 = 𝑘2𝑛+2.
𝑘 𝑘
wait, but earlier i had 𝑞(𝑘) = 0, which led to 𝑟(𝑘)−𝑘2𝑛+2 = 0, so 𝑟(𝑘) = 𝑘2𝑛+2.
therefore, 𝑟(𝑘) − 𝑘2𝑛+2 = 0, meaning that 𝑟(𝑥) − 𝑥2𝑛+2 has roots at 𝑥 = 𝑘 for 𝑘 =
±1,±2,...,±𝑛.
93

<!-- Page 94 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought
but 𝑟(𝑥) is a degree 2𝑛 polynomial, and 𝑥2𝑛+2 is a monomial of degree 2𝑛 + 2, so
𝑟(𝑥)−𝑥2𝑛+2 is a degree 2𝑛+2 polynomial with 2𝑛 roots at 𝑥 = ±1,±2,...,±𝑛, and
two additional roots.
wait, but 𝑟(𝑥) is degree 2𝑛, and 𝑥2𝑛+2 is degree 2𝑛+2, so their difference is degree
2𝑛+2, as previously established.
butif𝑟(𝑥)−𝑥2𝑛+2has2𝑛rootsat𝑥 = ±1,±2,...,±𝑛,andit’sadegree2𝑛+2polynomial,
then there are two more roots.
now, perhaps i can factor 𝑟(𝑥)−𝑥2𝑛+2 as:
𝑟(𝑥)−𝑥2𝑛+2 = (𝑥2−1)(𝑥2−4)···(𝑥2−𝑛2)·(𝑥2−𝑎)
for some constant 𝑎, since the roots come in pairs 𝑥 = ±𝑘 for 𝑘 = 1 to 𝑛, and possibly
√
another pair 𝑥 = ± 𝑎.
but i need to find 𝑎.
alternatively, perhaps i can look at the behavior of 𝑟(𝑥)−𝑥2𝑛+2 at specific points to
determine 𝑎.
but this seems complicated. maybe there’s a different approach.
let me consider that 𝑝(𝑥) is a monic polynomial of degree 2𝑛, and 𝑝 (︀1)︀ = 𝑘2 for
𝑘
𝑘 = ±1,±2,...,±𝑛.
perhapsicanconsiderthepolynomial𝑝(𝑥)− 1 ,butasbefore,thatintroducesarational
𝑥2
function.
alternatively, maybe i can consider building 𝑝(𝑥) explicitly.
since 𝑝(𝑥) is monic of degree 2𝑛, and it satisfies 𝑝 (︀1)︀ = 𝑘2 for 𝑘 = ±1,±2,...,±𝑛,
𝑘
perhaps i can write 𝑝(𝑥) in terms of these roots.
wait, but 𝑝 (︀1)︀ = 𝑘2, which is like saying 𝑝 (︀1)︀ −𝑘2 = 0, meaning that 1 are roots of
𝑘 𝑘 𝑘
the equation 𝑝(𝑥)− 1 = 0, but again, that’s a rational function.
𝑥2
alternatively, perhaps i can consider that 𝑝(𝑥) − 1 has roots at 𝑥 = 1 for 𝑘 =
𝑥2 𝑘
±1,±2,...,±𝑛, and try to factor it accordingly.
but this seems tricky because of the 1 term.
𝑥2
maybe a better approach is to consider the polynomial 𝑥2𝑝(𝑥)−1, which is a degree
2𝑛+2 polynomial.
given that 𝑝 (︀1)︀ = 𝑘2, then 𝑥2𝑝(𝑥) − 1 evaluated at 𝑥 = 1 gives (︀1)︀2 𝑝 (︀1)︀ − 1 =
𝑘 𝑘 𝑘 𝑘
1 ·𝑘2−1 = 1−1 = 0, so 𝑥 = 1 are roots of 𝑥2𝑝(𝑥)−1 = 0.
𝑘2 𝑘
therefore, 𝑥2𝑝(𝑥)−1 is a degree 2𝑛+2 polynomial with roots at 𝑥 = ±1,±1,...,±1,
1 2 𝑛
and possibly two more roots.
wait,but𝑥2𝑝(𝑥)−1isapolynomial,anditsrootsarethesolutionsto𝑥2𝑝(𝑥) = 1,which
is similar to the original equation 𝑝 (︀1)︀ = 𝑥2.
𝑥
so,perhapsicanconsidertherootsof𝑥2𝑝(𝑥)−1 = 0,whicharethesameasthesolutions
to 𝑝 (︀1)︀ = 𝑥2 due to the substitution 𝑦 = 1.
𝑥 𝑥
therefore, finding the roots of 𝑥2𝑝(𝑥) − 1 = 0 is equivalent to finding 𝑥 such that
𝑝 (︀1)︀ = 𝑥2.
𝑥
giventhat,andknowingthat𝑝(𝑥)isamonicpolynomialofdegree2𝑛,andthat𝑝 (︀1)︀ = 𝑘2
𝑘
for 𝑘 = ±1,±2,...,±𝑛, perhaps i can find a relationship between 𝑝(𝑥) and these roots.
alternatively, perhaps i can consider the lagrange interpolation formula for 𝑝(𝑥), given
its values at specific points.
since 𝑝(𝑥) is a monic polynomial of degree 2𝑛, and i have its values at 2𝑛 points, i
can indeed find 𝑝(𝑥) explicitly using interpolation, but that seems complicated for this
problem.
94

<!-- Page 95 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought
moreover, the problem is not asking for 𝑝(𝑥), but for the real numbers 𝑥 that satisfy
𝑝 (︀1)︀ = 𝑥2, beyond the given 𝑥 = 𝑘 for 𝑘 = ±1,±2,...,±𝑛.
𝑥
so, perhaps there is a symmetry or a particular property of 𝑝(𝑥) that i can exploit.
wait, perhaps i can consider that 𝑝(𝑥) and 𝑝 (︀1)︀ are related in a specific way.
𝑥
giventhat𝑝(𝑥)isapolynomial,𝑝 (︀1)︀isarationalfunction,andmultiplyingby𝑥2𝑛 gives
𝑥
a polynomial.
alternatively, perhaps there is a functional equation that 𝑝(𝑥) satisfies.
let me consider writing 𝑝(𝑥) in terms of its roots.
but 𝑝(𝑥) is a monic polynomial of degree 2𝑛, so it can be written as:
𝑝(𝑥) = (𝑥−𝑟 )(𝑥−𝑟 )···(𝑥−𝑟 )
1 2 2𝑛
for some roots 𝑟 ,𝑟 ,...,𝑟 .
1 2 2𝑛
but i don’t know these roots, so that might not help directly.
alternatively, perhaps i can consider the fact that 𝑝(𝑥) has certain symmetries given the
condition 𝑝 (︀1)︀ = 𝑘2.
𝑘
wait, maybe i can consider the function 𝑝(𝑥)− 1 , but again, that introduces a rational
𝑥2
function.
alternatively, perhaps i can consider the derivative of 𝑝(𝑥), but i don’t see an immediate
connection.
let me try to think differently.
suppose i define a new function 𝑓(𝑥) = 𝑝 (︀1)︀ −𝑥2, as i did earlier.
𝑥
then, 𝑓(𝑥) = 0 for 𝑥 = ±1,±2,...,±𝑛, as given.
i need to find all real 𝑥 such that 𝑓(𝑥) = 0, beyond these known roots.
now, 𝑓(𝑥) is a rational function, but 𝑥2𝑛𝑓(𝑥) is a polynomial of degree 2𝑛 + 2, as
established earlier.
therefore, 𝑥2𝑛𝑓(𝑥) = 0 has roots at 𝑥 = ±1,±2,...,±𝑛, and possibly two more roots.
so, if i can find this polynomial 𝑥2𝑛𝑓(𝑥), i can factor it and find the additional roots.
but to find 𝑥2𝑛𝑓(𝑥), i need to know more about 𝑝(𝑥), which i don’t.
alternatively, perhaps i can consider the behavior of 𝑓(𝑥) as 𝑥 approaches infinity or
zero.
as 𝑥 → ∞, 𝑝 (︀1)︀ behaves like (︀1)︀2𝑛 , which approaches 0, while 𝑥2 approaches infinity,
𝑥 𝑥
so 𝑓(𝑥) → −∞.
as 𝑥 → 0, 𝑝 (︀1)︀ behaves like (︀1)︀2𝑛 , which goes to infinity, while 𝑥2 approaches 0, so
𝑥 𝑥
𝑓(𝑥) → ∞.
this suggests that there are additional roots beyond the given 𝑥 = ±1,±2,...,±𝑛,
possibly at infinity or near zero, but i need to find them explicitly.
wait, perhaps there’s a smarter way to approach this.
given that 𝑝(𝑥) is a monic polynomial of degree 2𝑛, and it satisfies 𝑝 (︀1)︀ = 𝑘2 for
𝑘
𝑘 = ±1,±2,...,±𝑛, perhaps i can consider the minimal polynomial that satisfies these
conditions.
alternatively, maybe i can consider that 𝑝(𝑥) can be expressed in terms of a product
involving these roots.
wait, perhaps i can consider that 𝑝(𝑥)− 1 has roots at 𝑥 = ±1,±1,...,±1, but again,
𝑥2 1 2 𝑛
that introduces a rational function.
alternatively, perhaps i can consider that 𝑥2𝑝(𝑥)−1 has roots at 𝑥 = ±1,±1,...,±1,
1 2 𝑛
as previously established, and try to find a general form for this polynomial.
let me consider that 𝑥2𝑝(𝑥) − 1 is a degree 2𝑛 + 2 polynomial with roots at 𝑥 =
±1,±1,...,±1, and two additional roots.
1 2 𝑛
95

<!-- Page 96 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought
given that, perhaps i can express 𝑥2𝑝(𝑥)−1 as:
𝑛 (︂ )︂
∏︁ 1
𝑥2𝑝(𝑥)−1 = 𝑥2− ·(𝑥2−𝑎)
𝑘2
𝑘=1
√
for some constant 𝑎, since the roots come in pairs 𝑥 = ±1 and possibly 𝑥 = ± 𝑎.
𝑘
but i need to determine 𝑎.
alternatively, perhaps i can consider that the product ∏︀𝑛 (︀ 𝑥2− 1 )︀ is a degree 2𝑛
𝑘=1 𝑘2
polynomial, and 𝑥2𝑝(𝑥)− 1 is degree 2𝑛+2, so there are two more roots.
but without knowing more about 𝑝(𝑥), it’s hard to pin down 𝑎.
wait, perhaps i can consider the behavior at 𝑥 = 0.
at 𝑥 = 0, 𝑥2𝑝(𝑥)−1 = −1, so 𝑥 = 0 is not a root.
similarly, as 𝑥 → ∞, 𝑥2𝑝(𝑥)−1 behaves like 𝑥2𝑛+2, which goes to infinity.
but i still don’t see how to find 𝑎.
alternatively,perhapsicanconsiderthevalueof𝑥2𝑝(𝑥)−1ataspecificpoint,say𝑥 = 1,
but that’s already a root.
wait, perhaps i can consider 𝑥 = ∞, but that’s not helpful.
alternatively, perhaps i can consider that 𝑝(𝑥) is determined by its values at 2𝑛 points,
so i can use interpolation to find 𝑝(𝑥), but that seems too involved for this problem.
alternatively, perhaps there’s a symmetry in the equation that i can exploit.
given that 𝑝(𝑥) is a polynomial of even degree 2𝑛, and the conditions are given for
𝑘 = ±1,±2,...,±𝑛, perhaps 𝑝(𝑥) has some symmetry properties.
for example, maybe 𝑝(𝑥) is an even function, but i don’t know that for sure.
wait, let’s check: if 𝑝(𝑥) were even, then 𝑝(−𝑥) = 𝑝(𝑥), but the conditions are given for
both positive and negative 𝑘, so perhaps that’s a clue.
given that 𝑝 (︀1)︀ = 𝑘2 for both 𝑘 and −𝑘, and 𝑘2 is the same for both, it suggests that
𝑘
𝑝(𝑥) might be even, but i need to confirm.
however, 𝑝(𝑥) is a general monic polynomial of degree 2𝑛, and its coefficients could
make it even or not.
(︁ )︁
but in this case, since 𝑝 (︀1)︀ = 𝑝 1 = 𝑘2, which is the same, it suggests that 𝑝 (︀1)︀ is
𝑘 −𝑘 𝑥
even in 𝑥, but 𝑝(𝑥) itself doesn’t have to be even.
alternatively, perhaps i can consider that 𝑝(𝑥) has a reciprocal property, given the
conditions involving 1.
𝑘
wait, perhaps i should consider the reciprocal polynomial of 𝑝(𝑥), which is 𝑥2𝑛𝑝 (︀1)︀ as
𝑥
before.
let me denote this as 𝑟(𝑥) = 𝑥2𝑛𝑝 (︀1)︀ , which is a degree 2𝑛 polynomial.
𝑥
given that, and knowing that 𝑝 (︀1)︀ = 𝑘2, then 𝑟(𝑘) = 𝑘2𝑛𝑝 (︀1)︀ = 𝑘2𝑛·𝑘2 = 𝑘2𝑛+2.
𝑘 𝑘
therefore, 𝑟(𝑘) = 𝑘2𝑛+2 for 𝑘 = ±1,±2,...,±𝑛.
now, since 𝑟(𝑥) is a degree 2𝑛 polynomial, and it equals 𝑥2𝑛+2 at 2𝑛 points, which is
more points than the degree, unless there’s some dependency.
wait, but 𝑟(𝑥) is degree 2𝑛, and 𝑥2𝑛+2 is degree 2𝑛+2, so they can’t be equal at more
points than their degree difference unless they are the same polynomial, which they
aren’t.
this suggests that my earlier assumption is incorrect, or perhaps i need to consider that
𝑟(𝑥)−𝑥2𝑛+2 is a polynomial of degree 2𝑛+2, but that seems inconsistent because 𝑟(𝑥)
is degree 2n and 𝑥2𝑛+2 is degree 2𝑛+ 2, so their difference should be degree 2𝑛+2.
wait, perhaps i should correct that.
given 𝑟(𝑥) = 𝑥2𝑛𝑝 (︀1)︀ , which is degree 2𝑛, and 𝑥2𝑛+2 is degree 2𝑛+2, their difference
𝑥
𝑟(𝑥)−𝑥2𝑛+2 is degree 2𝑛+2, as the highest degree term comes from −𝑥2𝑛+2.
96

<!-- Page 97 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought
given that 𝑟(𝑘) = 𝑘2𝑛+2 for 𝑘 = ±1,±2,...,±𝑛, then 𝑟(𝑥)−𝑥2𝑛+2 = 0 at these points.
therefore,𝑟(𝑥)−𝑥2𝑛+2 has2𝑛rootsat𝑥 = ±1,±2,...,±𝑛,andsinceit’sdegree2𝑛+2,
there are two more roots.
now, perhaps i can factor 𝑟(𝑥)−𝑥2𝑛+2 as:
𝑟(𝑥)−𝑥2𝑛+2 = (𝑥2−1)(𝑥2−4)···(𝑥2−𝑛2)·(𝑥2−𝑎)
for some constant 𝑎, since the roots come in pairs 𝑥 = ±𝑘, and possibly another pair
√
𝑥 = ± 𝑎.
now, to find 𝑎, perhaps i can consider the behavior at infinity or use the fact that the
leading coefficients must match.
given that 𝑟(𝑥) = 𝑥2𝑛𝑝 (︀1)︀ and 𝑝(𝑥) is monic of degree 2𝑛, the leading term of 𝑝(𝑥) is
𝑥
𝑥2𝑛, so 𝑝 (︀1)︀ = 𝑥−2𝑛+··· , and thus 𝑟(𝑥) = 𝑥2𝑛·𝑥−2𝑛+··· = 1+··· , so the leading
𝑥
term of 𝑟(𝑥) is 1.
on the other hand, 𝑥2𝑛+2 has leading term 𝑥2𝑛+2, so 𝑟(𝑥) − 𝑥2𝑛+2 has leading term
−𝑥2𝑛+2.
now,theright-handside,(𝑥2−1)(𝑥2−4)···(𝑥2−𝑛2)(𝑥2−𝑎),expandsto𝑥2𝑛+2−(1+
4+···+𝑛2+ 𝑎)𝑥2𝑛+··· .
wait,actually,theproduct(𝑥2−1)(𝑥2−4)···(𝑥2−𝑛2)(𝑥2−𝑎)wouldhaveleadingterm
𝑥2𝑛+2, and the coefficient of 𝑥2𝑛 would be −(1+4+···+𝑛2+𝑎).
but𝑟(𝑥)−𝑥2𝑛+2 hasleadingterm−𝑥2𝑛+2,andthecoefficientof𝑥2𝑛 wouldbesomething
else, depending on
on the other hand, 𝑥2𝑛+2 has leading term 𝑥2𝑛+2, so 𝑟(𝑥) − 𝑥2𝑛+2 has leading term
−𝑥2𝑛+2.
now,theright-handside,(𝑥2−1)(𝑥2−4)···(𝑥2−𝑛2)(𝑥2−𝑎),expandsto𝑥2𝑛+2−(1+
4+···+𝑛2+ 𝑎)𝑥2𝑛+··· .
wait,actually,theproduct(𝑥2−1)(𝑥2−4)···(𝑥2−𝑛2)(𝑥2−𝑎)wouldhaveleadingterm
𝑥2𝑛+2, and the coefficient of 𝑥2𝑛 would be −(1+4+···+𝑛2+𝑎).
but𝑟(𝑥)−𝑥2𝑛+2 hasleadingterm−𝑥2𝑛+2,andthecoefficientof𝑥2𝑛 wouldbesomething
else, depending on the expansion of 𝑟(𝑥).
therefore, to match the leading coefficients, i must have:
−𝑥2𝑛+2 = 𝑥2𝑛+2−(1+4+···+𝑛2+𝑎)𝑥2𝑛+···
this implies that:
−𝑥2𝑛+2 = 𝑥2𝑛+2−(1+4+···+𝑛2+𝑎)𝑥2𝑛+···
comparing coefficients, the coefficient of 𝑥2𝑛+2 on the left is −1, and on the right is 1.
this suggests that there’s an inconsistency unless i made a mistake in my earlier steps.
wait, perhaps i need to reconsider the factorization.
given that 𝑟(𝑥)−𝑥2𝑛+2 = (𝑥2−1)(𝑥2−4)···(𝑥2−𝑛2)(𝑥2−𝑎), and the leading term
on the left is −𝑥2𝑛+2, while on the right, it’s 𝑥2𝑛+2, this suggests that there is a sign
discrepancy.
therefore, perhaps the correct factorization should include a negative sign:
𝑟(𝑥)−𝑥2𝑛+2 = −(𝑥2−1)(𝑥2−4)···(𝑥2−𝑛2)(𝑥2−𝑎)
this way, the leading coefficient matches: −𝑥2𝑛+2 = −𝑥2𝑛+2.
now, to find 𝑎, perhaps i can consider the constant term.
the constant term of 𝑟(𝑥)−𝑥2𝑛+2 is 𝑟(0)−0 = 𝑟(0).
97

<!-- Page 98 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought
but 𝑟(𝑥) = 𝑥2𝑛𝑝 (︀1)︀ , so 𝑟(0) = lim 𝑥2𝑛𝑝 (︀1)︀ .
𝑥 𝑥→0 𝑥
but 𝑝 (︀1)︀ behaves like (︀1)︀2𝑛 as 𝑥 → 0, so 𝑥2𝑛· (︀1)︀2𝑛 = 1, so 𝑟(0) = 1.
𝑥 𝑥 𝑥
on the other hand, the constant term of −(𝑥2 − 1)(𝑥2 − 4)···(𝑥2 − 𝑛2)(𝑥2 − 𝑎) is
−(−1)𝑛·1·4·9···𝑛2·𝑎.
wait, actually, expanding the product:
(𝑥2−1)(𝑥2−4)···(𝑥2−𝑛2)(𝑥2−𝑎) = 𝑥2𝑛+2−(1+4+···+𝑛2+𝑎)𝑥2𝑛+···+(−1)𝑛+1(1·
4·9···𝑛2·𝑎)
therefore, the constant term is (−1)𝑛+1(1·4·9···𝑛2·𝑎).
but since 𝑟(𝑥)−𝑥2𝑛+2 has constant term 𝑟(0) = 1, and the right-hand side has constant
term −(−1)𝑛+1(1· 4·9···𝑛2·𝑎) = (−1)𝑛(1·4·9···𝑛2·𝑎), we have:
(−1)𝑛(1·4·9···𝑛2·𝑎) = 1
therefore:
1
𝑎 =
(−1)𝑛(1·4·9···𝑛2)
but 1·4·9···𝑛2 = (𝑛!)2, since 1 = 12,4 = 22,9 = 32, etc., up to 𝑛2.
therefore:
1
𝑎 =
(−1)𝑛(𝑛!)2
but since 𝑎 is a real number, and 𝑛 is even (as given in the problem), because 𝑛 is an
even positive integer, (−1)𝑛 = 1, so:
1
𝑎 =
(𝑛!)2
therefore, the factorization is:
(︂ )︂
𝑟(𝑥)−𝑥2𝑛+2 = − (︀ 𝑥2−1 )︀(︀ 𝑥2−4 )︀ ··· (︀ 𝑥2−𝑛2)︀ 𝑥2− 1
(𝑛!)2
now, since 𝑟(𝑥) = 𝑥2𝑛𝑝 (︀1)︀ , and 𝑟(𝑥)−𝑥2𝑛+2 = 0 when 𝑝 (︀1)︀ = 𝑥2, the roots of this
𝑥 𝑥
equation are 𝑥 = ±1,±2,...,±𝑛,±1.
𝑛!
wait,no. actually,fromthefactorization,therootsare𝑥 = ±1,±2,...,±𝑛,±1 because
𝑛!
𝑥2− 1 = 0 gives
(𝑛!)2
1
𝑥 = ± .
𝑛!
therefore, the solutions to 𝑝 (︀1)︀ = 𝑥2 are 𝑥 = ±1,±2,...,±𝑛,±1.
𝑥 𝑛!
but the problem states that 𝑝 (︀1)︀ = 𝑘2 for 1 ≤ |𝑘| ≤ 𝑛, so these 𝑥 = ±1,±2,...,±𝑛 are
𝑘
already known solutions.
therefore, the "other real numbers" 𝑥 that satisfy 𝑝 (︀1)︀ = 𝑥2 are 𝑥 = ±1.
𝑥 𝑛!
wait, but in the factorization, i have
1
𝑥2− ,
(𝑛!)2
which gives 𝑥 = ±1, assuming that’s correct.
𝑛!
but i need to verify this conclusion.
98

<!-- Page 99 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought
given that 𝑎 = 1 and the factorization is
(𝑛!)2
(︂ )︂
𝑟(𝑥)−𝑥2𝑛+2 = − (︀ 𝑥2−1 )︀(︀ 𝑥2−4 )︀ ··· (︀ 𝑥2−𝑛2)︀ 𝑥2− 1 ,
(𝑛!)2
then indeed, the roots are 𝑥 = ±1,±2,...,±𝑛,±1.
𝑛!
therefore, the additional solutions beyond 𝑥 = ±1,±2,...,±𝑛 are
1
𝑥 = ± .
𝑛!
but wait, is 𝑛! correct here? let me double-check the calculation of 𝑎.
earlier, i had:
1 1
𝑎 = =
(−1)𝑛(1·4·9···𝑛2) (𝑛!)2
since 𝑛 is even, (−1)𝑛 = 1, so indeed, 𝑎 = 1 .
(𝑛!)2
therefore, the additional roots are 𝑥 = ±1.
𝑛!
hence, the other real numbers 𝑥 that satisfy 𝑝 (︀1)︀ = 𝑥2 are 𝑥 = ±1.
𝑥 𝑛!
**final answer**
1
𝑥 = ±
𝑛!
99

<!-- Page 100 -->

TowardsSystem2ReasoninginLLMs:LearningHowtoThinkWithMetaChain-of-Thought
Table 5: Regret Statistics by Model and Prompting Strategy
Model Prompting Strategy Regret Count Regret %
Baseline 6 0.24

### CoT 8 0.32

Llama 3.1 405B Think 87 3.49

### Think (3-shot) 216 8.69

Think & Verify 391 15.67
Baseline 7 0.30

### CoT 12 0.50

Llama 3.1 8B Think 103 4.51

### Think (3-shot) 103 4.28

Think & Verify 454 20.87
Baseline 5 0.20

### CoT 6 0.25

Llama 3.1 70B Think 313 12.65

### Think (3-shot) 231 9.33

Think & Verify 638 25.67
Baseline 1 0.04

### CoT 2 0.08

GPT-4o-mini Think 66 2.64
Think (3-shot) 53 2.12
Think & Verify 62 2.48
Baseline 0 0.00

### CoT 0 0.00


### GPT-4o Think 34 1.36

Think (3-shot) 28 1.12
Think & Verify 38 1.52
Baseline 1 0.04

### CoT 2 0.08

GPT-3.5-turbo Think 24 0.96
Think (3-shot) 25 1.00
Think & Verify 12 0.48
Baseline 0 0.00

### CoT 3 0.12

Claude 3.5 Sonnet Think 81 3.24

### Think (3-shot) 99 3.96

Think & Verify 111 4.44
Baseline 0 0.00

### CoT 1 0.04

Claude 3.5 Haiku Think 16 0.64
Think (3-shot) 16 0.64
Think & Verify 4 0.16
100

## Tables

**Table (Page 10):**

|  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  | M M |  |  |  |
|  |  |  |  |  |  |  | M M | ajority@6 ajority@8 | 4 |
|  |  |  |  |  |  |  | Gr Ba Or | eedy se Filter iginal |  |


**Table (Page 10):**

|  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  | Pass@ Pass@ | 2 4 | Pass@1 Pass@3 | 6 2 |
|  |  |  |  |  |  | Pass@ | 8 | Pass@6 | 4 |


**Table (Page 14):**

| Policy | Value |
|---|---|
| 𝜋 𝜃0 𝜋 𝜃1 | - - |
| 𝜋 𝜃0 𝜋 𝜃0 𝜋 𝜃1 𝜋 𝜃1 | {𝑣,𝑟ˆ} 𝜑0 {𝑣,𝑟ˆ} 𝜑1 {𝑣,𝑟ˆ} 𝜑0 {𝑣,𝑟ˆ} 𝜑1 |


**Table (Page 20):**

|  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |


**Table (Page 20):**

|  | Sequential | Best-of-N Weig | hted |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|
|  | Parallel Be Sequential Parallel Ma | st-of-N Weighte Majority jority | d |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |


**Table (Page 28):**

| % pf Training Epoch # of Unique Problems ~0.05 ~0.3 1 (#Training Trajectories) 500 (7.44k) 3000 (41.7k) 7086 (97k) |  |  |
|---|---|---|
|  |  |  |
|  |  |  |
|  |  |  |


**Table (Page 28):**

|  |
|---|
|  |
|  |


**Table (Page 28):**

|  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |


**Table (Page 28):**

|  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |


**Table (Page 28):**

|  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |


**Table (Page 28):**

|  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |


**Table (Page 28):**

|  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |


**Table (Page 28):**

|  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |


**Table (Page 28):**

|  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |


**Table (Page 28):**

|  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |


**Table (Page 28):**

|  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |


**Table (Page 29):**

| Oracle 0.6 Majority ycaruccA 0.5 0.4 0.3 1 2 4 8 16 32 64 Number of Generations per Problem | Oracle Majority |
|---|---|
|  |  |
|  |  |


**Table (Page 29):**

| hcraeS ycaruccA snekoT ni fo desU # Process Reward Models |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |


**Table (Page 29):**

|  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |


**Table (Page 43):**

|  |  | PRM-Q7086 PRM-Q3000 PRM-Q500 Oracle Majority 𝛾=1 𝛾=0.995 𝛾=0.99 |
|---|---|---|
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |


**Table (Page 46):**

| Data Source | Original | Base Filter | Strict Filter |
|---|---|---|---|
| HARP (Yue et al., 2024) NuminaMath (LI et al., 2024) Omni-MATH (Gao et al., 2024) OpenMathInstruct-2 (Toshniwal et al., 2024) | 4,780 859,608 4,428 607,324 | 3,691 452,820 3,660 600,191 | 2,996 231,887 2,478 496,331 |
| Total | 1,476,140 | 1,060,362 | 733,692 |


**Table (Page 50):**

| Majority Vote (TIR) Best of N (TIR) |  |
|---|---|
| Majority Vote (CoT) Best of N (CoT) |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
