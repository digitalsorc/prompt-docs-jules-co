---
title: "GitHub Copilot Asset or Liability"
original_file: "./GitHub_Copilot_Asset_or_Liability.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["prompt-engineering", "llm", "rag", "fine-tuning", "evaluation"]
keywords: ["copilot", "solutions", "correct", "code", "programming", "problems", "problem", "students", "different", "buggy"]
summary: "<!-- Page 1 -->


### GitHub Copilot AI pair programmer: Asset or Liability? Arghavan Moradi Dakhel∗, Vahid Majdinasab∗, Amin Nikanjam, Foutse Khomh, Michel C. Desmarais
Polytechnique Montreal, Montreal, Canada

### Zhen Ming (Jack) Jiang

York University, Toronto, Canada

### Abstract

Automatic program synthesis is a long-lasting dream in software engineering."
related_documents: []
---

# GitHub Copilot Asset or Liability

<!-- Page 1 -->


### GitHub Copilot AI pair programmer: Asset or Liability?

Arghavan Moradi Dakhel∗, Vahid Majdinasab∗, Amin Nikanjam, Foutse Khomh, Michel C. Desmarais
Polytechnique Montreal, Montreal, Canada

### Zhen Ming (Jack) Jiang

York University, Toronto, Canada

### Abstract

Automatic program synthesis is a long-lasting dream in software engineering. Recently, a promising Deep Learning (DL)
based solution, called Copilot, has been proposed by OpenAI and Microsoft as an industrial product. Although some
studies evaluate the correctness of Copilot solutions and report its issues, more empirical evaluations are necessary to
understand how developers can benefit from it effectively. In this paper, we study the capabilities of Copilot in two
different programming tasks: (i) generating (and reproducing) correct and efficient solutions for fundamental algorithmic
problems, and (ii) comparing Copilot’s proposed solutions with those of human programmers on a set of programming
tasks. For the former, we assess the performance and functionality of Copilot in solving selected fundamental problems
in computer science, like sorting and implementing data structures. In the latter, a dataset of programming problems
with human-provided solutions is used. The results show that Copilot is capable of providing solutions for almost all
fundamental algorithmic problems, however, some solutions are buggy and non-reproducible. Moreover, Copilot has
some difficulties in combining multiple methods to generate a solution. Comparing Copilot to humans, our results show
that the correct ratio of humans’ solutions is greater than Copilot’s suggestions, while the buggy solutions generated
by Copilot require less effort to be repaired. Based on our findings, if Copilot is used by expert developers in software
projects, it can become an asset since its suggestions could be comparable to humans’ contributions in terms of quality.
However, Copilot can become a liability if it is used by novice developers who may fail to filter its buggy or non-optimal
solutions due to a lack of expertise.
Keywords: Code Completion, Language Model, GitHub Copilot, Testing.

## Introduction formalmodels[15,27]toEvolutionaryAlgorithms[48]and

machine-learned translation [42].
Recent breakthroughs in Deep Learning (DL), in par- Novel Large Language Models (LLMs) with the transticular the Transformer architecture, have revived the Soft- former architecture recently achieved good performance
ware Engineering (SE) decades-long dream of automating in automatic program synthesis [6, 8, 9, 20]. One such
code generation that can speed up programming activi- model is Codex [8]; a GPT-3 [6] based language model
ties. Program generation aims to deliver a program that withupto12billionparameterswhichhasbeenpretrained
meets a user’s intentions in the form of input-output ex- on 159 GB of code samples from 54 million GitHub reposiamples, natural language descriptions, or partial programs tories. Codex shows a good performance in solving a set of
[2, 33, 25]. hand-written programming problems (i.e., not in the train-
Program synthesis is useful for different purposes such ing dataset) using Python, named HumanEval dataset [8].
as teaching, programmer assistance, or the discovery of This dataset includes simple programming problems with
new algorithmic solutions for a problem [25]. One finds test cases to assess the functional correctness of codes. A
different approaches to automatic code generation in the production version ofCodex is available as an extension on
literature, from natural language programming [35] and the Visual Studio Code development environment, named
GitHub Copilot1. Copilot, as an “AI pair programmer”,
cangeneratecodeindifferentprogramminglanguageswhen
∗Correspondingauthors. Bothauthorscontributedequallytothis
provided with some context (called prompt), such as comresearch.
Email addresses: {arghavan.moradi-dakhel, ments, methods names, or surrounding code.
vahid.majdinasab, amin.nikanjam, foutse.khomh, Several studies focus on the correctness of codes sugmichel.desmarais}@polymtl.ca(AminNikanjam,FoutseKhomh,
MichelC.Desmarais),zmjiang@cse.yorku.ca(ZhenMing(Jack)

### Jiang)

1https://copilot.github.com/
Preprint submitted to Journal of Software and System April 18, 2023
3202
rpA
41
]ES.sc[
2v13351.6022:viXra

<!-- Page 2 -->

gestedbyCopilotonthedifferenttypesofproblemssuchas all, are concrete formulations of abstract algorithms based
linearalgebraproblemsforanMITcourse[16]oruniversity on particular representations and structures of data” [53].
level probability and statistical problems [49]. The author The results of our study show that Copilot is capable
in[21]usedDavinci(anAPIonabetaversionofCodex)on of providing efficient solutions for the majority of fundadifferent programming questions of a programming course mental problems, however, some solutions are buggy or
and compared students’ grades with the grade of the tool non-reproducible. We also observed that Copilot has some
in solving the programming questions correctly. There are difficulties in combining multiple methods to generate a
few studies that assess other aspects of Copilot besides solution. Compared to human programmers, Copilot’s sothe correctness of its suggestions. Nguyen and Nadi [38] lutions to programming tasks have a lower correct ratio
compared the complexity of Copilot’s solutions in different and diversity. While the buggy codes generated by Copilot
programming languages for several LeetCode questions, can be repaired easily, the results highlight the limitation
besides their correctness. Authors in [51] conducted a user of Copilot in understanding some details in the context of
study to understand how Copilot can help programmers the problems, which are easily understandable by humans.
completeatask. Theystudiedhowmuchtimeparticipants OurfindingshowsCopilotcancompetewithhumansin
needed to complete a task using Copilot. coding and even though it can become an asset in software
While these studies highlight some qualifications of projects if used by experts. However, it can also become a
Copilot, they neither examined the quality of the codes liability if it is used by novices, who may not be familiar
produced by Copilot compared to humans nor did they with the problem context and correct coding methods.
investigate the buggy solutions suggested by Copilot and Copilotsuggestssolutionsthatmightbebuggyanddifficult
the diversity of its suggestions. Therefore, despite all these to understand, which may be accepted as correct solutions
previous studies, we still do not know if–how Copilot, as by novices. Adding such buggy and complex codes into
an industrial component, can be leveraged by developers software projects can highly impact their quality.
efficiently. We need to go beyond evaluating the correct- To summarize, this paper makes the following contriness of Copilot’s suggestions and examine how despite its butions:
limitations,itcanbeusedasaneffectivepairprogramming
tool. • We present an empirical study on the performance
The focus of our study is not on the type or difficulty and functionality of Copilot’s suggestions for fundalevel of programming tasks that Copilot can handle, but mental algorithmic problems.
is on the quality of the codes that it will add to software • We empirically compare Copilot’s solutions with huprojects if it is used as an AI pair programmer. We aim to
man solutions on a dataset of Python programming
investigate if the quality of codes generated by Copilot is
problems.
competitive with humans and if it can be used instead of a
developer in pair programming tasks of software projects • We make the dataset used and the detailed results
without impacting code quality. We highlight Copilot’s obtained in this study publicly available online [18]
limitations and competence with two different strategies forotherresearchersand–orpractitionerstoreplicate
and compared its suggestions with humans in different our results or build on our work.
aspects. We also formulate suggestions on how developers
can benefit from using Copilot in real software projects. The rest of this paper is organized as follows.
First, we assess Copilot’s capabilities in solving funda- We briefly review the related works in Section 2. Section 3
mentalalgorithmicproblems(i.e.,searchingandsorting)in presents the design of our study to evaluate Copilot as
programming. We study the correctness and reproducibil- an assistant to developers. We report our experiments to
ity of Copilot’s solutions to these problems. Secondly, we assess Copilot’s suggestions for fundamental algorithmic
compare Copilot’s solutions with human solutions in solv- problems and compare generated suggestions with what
ing programming tasks, to assess the extent to which it programmersdoonspecificprogrammingtasksinSection4.
can mimic the work of a human pair programmer. We use WediscussourresultsandpotentiallimitationsinSection5.
a dataset of different programming tasks containing up to Threats to validity are reviewed in Section 6. Finally, we
4000 in human-provided solutions (correct and buggy). conclude the paper in Section 7.

### To conduct our study, we have chosen datasets for

which Copilot is able to generate answers corresponding

## Related Works

to their programming tasks. While such tasks may not
be representative of the typical programming tasks that A few studies empirically investigate the different caa professional developer performs, they allow us to assess pabilities of Copilot. Sobania et al. [47] compared Copilot
Copilot’scapabilitiesandlimitationsandtolistoursugges- with a Genetic Programming (GP) based approach that
tions to developers on how to benefit from this tool in real achieved good performance in program synthesis. Their
software projects. We make the assumption that the find- findingsshowthatGPbasedapproachesneedmoretimeto
ings on these datasets can generalize to more professional generate a solution. Moreover, training GP based models
programming tasks and this is because “programs, after are expensive due to the high cost of data labeling. Also,
2

<!-- Page 3 -->

these approaches are not suitable to support developers in investigated if Copilot learns from buggy code to generate
practice as GP usually generates codes that are bloated insecure code. Another study investigates how Copilot can
and difficult to understand by humans [47]. reproduce vulnerabilities in human programs [4]. To do
Vaithilingam et al. [51] conducted a human study in- so, they first used a dataset of vulnerabilities generated by
volving 24 participant to understand how Copilot can help humans, then rebuilt the whole code before the bug and
programmerstocompleteatask. Theyfocusedon3Python askedCopilottocompletethecode. Thecompletedsection
programming tasks: “1. edit CSV, 2. web scraping” and was manually inspected by three coders to determine if
“3. graph plotting”. Their finding shows that while Copi- Copilot reproduced the bug or fixed it.
lot did not necessarily improve the task completion time Moroz et al. [37] examined the challenges and the poand success rate, programmers prefer to use Copilot for tentialofCopilottoimprovetheproductivityofdevelopers.
theirdailytasksbecauseitsuggestsgoodstartingpointsto They highlighted the copyright problems and the safety
address the task. The tasks in this study involve less prob- issuesofitssolutions. Theydiscussedthenon-deterministic
lem solving effort compared to the typical programming nature of such models and the harmful content that could
tasks in our study. They are mostly related to using pro- be generated by them.
gramming language libraries. Also, they did not compare Authors in [56] surveyed 2631 developers about the
Copilot’s suggestions with their participants’ suggestions impact of Copilot on their productivity and highlighted
when working without the help of Copilot. differentmetricsofusers’interactionwithCopilotthathelp
Drori and Verma [16] studied Copilot’s capability in predict their productivity. They relied on the SPACE [22]
solving linear algebra problems for the MIT linear algebra framework to generate 11 Likert-style questions in their
course. In the same line of work, Tang et al. examined survey. Also,theyanalyzedtheusagedataofCopilotofthe
Copilot’s capability in solving university level probability participants who responded to this survey. They extracted
and statistical problems [49]. These two studies only fo- different metrics from this data such as the acceptance
cused on the correctness ratio of Copilot’s solutions and rate of solutions, persistence rate, unchanged and mostly
did not examine its performance on programming tasks. unchanged accepted solutions, etc. They found that the
Finnie-Ansley et al. [21] used Davinci (an API on a acceptance rate of solutions by developers is the most
beta version of Codex) on two datasets. The first dataset relevant metric that shows the impact of Copilot on the
includes 23 programming questions for a programming productivity of developers.
course, students’ solutions for these questions, and their To the best of our knowledge, none of these studies
grades. This dataset is not publicly available. The sec- compared Copilot with humans for solving programming
ond dataset is a set of different descriptions of a single tasks. The majority of these studies focused on assessing
well-known problem, rainfall, without humans’ solutions. the correctness of Copilot’s solutions and highlighted its
For the programming questions, the paper focused on the issues; e.g., the presence of vulnerabilities in generated sograding of the solutions suggested by Codex: generating lutions. Inthisstudy,wefocusonfundamentalalgorithmic
the correct solution for the problems after different runs problems and compare Copilot with humans in solving real
(10 runs) and then comparing the grading with students. world programming tasks.
For the second dataset, besides the code correctness, they
checked the variety of solutions by calculating the number

## Study Design

of source lines of code (sloc). Their results showed that
Codex outperformed most students as evidenced by the Inthissection,wepresentourmethodstoassessCopilot
grades received for their proposed solutions. Also, they ob- as an AI pair programmer and detail the experimental
servedthatusingthesameinputasapromptonCodexcan design to achieve our goals.
leadtodifferentsolutions,whileCodexcangeneratecorrect Tosolveaprogrammingtask,adeveloperusuallybuilds
solutions for different descriptions of the same problem. thecodeontopoffundamentaldatastructures(e.g.,queues,
NguyenandNadi[38]evaluatedCopiloton33LeetCode trees, graphs) and algorithms (e.g., search, sorting) in
questionsin4differentprogramminglanguages. Theyused computer science. Moreover, the developer needs to come
the LeetCode platform to test the correctness of Copilot’s up with ideas to achieve the goal(s) of the programming
solutions. The questions in their study included different task efficiently.
levelsofdifficulty. Althoughtheyevaluatedthecorrectness We evaluate Copilot on 1) the adequacy of recomofCopilot’ssolutionsandcomparedtheirunderstandability, mended code for fundamental algorithmic problems, and
they did not assess whether Copilot successfully found the 2) the quality of recommendations compared to humanoptimal solution for each task. provided solutions. Specifically, we address the following
Another group of studies focuses on vulnerability is- research questions (RQs):
sues to evaluate Copilot solutions. As mentioned before,

### RQ1: Can Copilot suggest correct and efficient solutions

Copilot is trained on a large volume of publicly available
for fundamental algorithmic problems?
code repositories on GitHub which may contain bug or
vulnerability problems. Pearce et al. [40] conducted dif- RQ2: Are Copilot’s solutions competitive with human soluferent scenarios on high-risk cybersecurity problems and tions for solving programming problems?
3

<!-- Page 4 -->

Intherestofthissection,wedescribetheresearchmeth- • Data Structures. From this section, we selected
ods we followed to answer each of our RQs as illustrated the Binary Search Tree (BST). BST is a basic data
in Figure 1. structure that is taught in algorithm design. Each
node of the tree contains a value (called key) that

### RQ1: Copilot on Algorithm Design is greater than all the values in the left sub-tree

Our goal in RQ1 is to observe if Copilot can generate and smaller than all the values in its right sub-tree.
solutions for fundamental algorithmic problems given clear The implementation of BST involves multiple steps,
descriptionsoftheproblemanddofurtheranalysis. Solving namely:
these fundamental algorithmic problems is important for
developers contributing to a software project. Although – Finding the minimum and maximum values in
these problems are not necessarily typical of professional the tree before inserting any new value.
projects, understandinghowtosolvethemwithanoptimal – In-order tree walks to extract all the values in
algorithm is essential because professional programming the tree in a sorted manner.
tasks are a combination of fundamental algorithmic and
– Findingthesuccessornode. Givenanodex, the
data structure problems [53]. Hence, the ability to address
successor of x is the node that has the smallest
basic programming problems correctly and efficiently is a
value which is greater than x.
prerequisite for addressing more professional programming
tasks. Further,failingtoperformthemislikelytotranslate • Graph Algorithms. From this section, we selected
into failure on more complex software engineering tasks. the Elementary Graph Algorithms. These algorithms
In this section, we plan to examine if Copilot is capable of are used to perform some elementary operations on
solving these fundamental problems with optimal solutions. a graph. Since graphs store information about how
each node is connected to others, they can be used in

#### Dataset: FundamentalAlgorithmicProblems

implementing applications such as maps and social
We selected the problems and their descriptions from
media user connections. We tested Copilot on the
[11]. We choose this resource because it is widely used
following graph algorithms problems:
for teaching algorithmic design fundamentals to computer
science students [12]. In this book, the authors explain – Generating code for a simple graph data structhe principal algorithms that computer engineers must ture.
be knowledgeable about by breaking them into categories.
– Breadth First Search (BFS) on a graph.
Since our problems were selected from this book, we fol-
– Depth First Search (DFS) on a graph.
lowed its categorization, such that our tests on Copilot
were conducted on 4 categories: – Implementing Directed Acyclic Graphs (DAG).

### DAGs require a more complex implementation

• SortingAlgorithms: Sortingalgorithmsareamong logiccomparedtosimplegraphs,sinceduringinithe first algorithmic concepts that are taught to com- tialization, based on the directions of the edges,
puter science students. These algorithms introduce we need to check if a cycle exists in the graph
the concept of time complexity and how inefficient or not.
codecanmakedifferencesinmorecomplexprograms.
– Finding reachable vertices. A pair of vertices
Sorting algorithms are used in databases to segment
are defined as reachable if both vertices can be
large amounts of data that cannot be loaded entirely
reached from each other in a directed graph.
into memory or in numerical operations to determine
whichnumbersshouldundergooperationsfirstforthe • AdvancedDesignandAnalysisTechniques. We
results to be produced as quickly as possible. From selected the greedy algorithms from this section. Unthis section, we selected some well-known sorting al- like the algorithms described above, the greedy techgorithms which students are asked to learn and then nique is a general approach for solving optimization
implement. Thesealgorithmsaremethodsforsorting problems based on breaking problems down into mulan array of numbers (integers or floats) in a descend- tiple subproblems and selecting the best solution at
ing or ascending manner. In these problems, time the given time. As these solutions need to be evalcomplexity, a measure of an algorithm’s run-time as uated in the context of a problem, we selected the
a function of input length, is an important factor to “activityselection”,anintroductoryproblemtogreedy
be considered. algorithms as described in [11].
From the algorithms described in the book, we selected bubble sort, bucket sort, heap sort, insertion 3.1.2. Prompt Engineering
sort, merge sort, quick sort, radix sort, and selection Alongside code completion, Copilot can generate code
sort. We selected these algorithms based on their fromnaturallanguagedescriptionsintheformofcomments.
implementation complexity, from easy to hard, based However, as noted by [31], if the description becomes too
on [11]’s descriptions. long or detailed, Copilot’s performance degrades. Since
4

<!-- Page 5 -->


### Solution Found

Prompt Evaluation Correct Solution
Engineering

### Found

Optimize Solution
Algorithmic

### Found


### Problems


### Recommened

Solution d e f f o s r e i a i r n c r h a ( n x, g s e e (l q e ) n : (seq)): Reproduced Correct
if x <= seq[i]: solution
GitHub r e t u r r n e l t e u n rn (s i eq)

### Copilot

Ratio of Correct

### Solutions


### Repairing Cost of

Assignments Evaluation Buggy Solutions
Repairing

### Tool

Diversity of Correct
Python Solutions

### Programming

Course Quality of Solutions

### Students'


### Submissions


### Students Syntactic Mastery

Figure1: The Workflow of proposed methods. ThestudyincludestwodifferentmethodstotestCopilotinrecommendingcodestosolve
programmingproblems. Thefirstpipelinefocusesonalgorithmicproblemscollectedfromawell-knownalgorithmdesignbook[11]. Thesecond
pipelinefocusesontheassignmentsofaPythonprogrammingcourse[28]. ItcomparesCopilotwithstudentsinsolvingprogrammingproblems
indifferentaspects.
the book that we are using to collect the problems [11] createdtheinputdescriptionsasexplainedabove. Afis a comprehensive educational book, each problem is de- ter this, these descriptions were cross-checked with
scribed in detail and by building upon concepts that were the first author to make sure that they were correct,
explained in the previous chapters. As a result, some prob- understandable, and contained enough information
lem descriptions span multiple paragraphs and sometimes, about the problem being described. The first two
pages. authors both have taken the course “Introduction to
However a summary description of our selected prob- Algorithms” during their education and have more
lems can be found in different resources, but the authors than 5 years of experience in coding and program
summarized the description of each problem in their own design. To assess the agreement, we have calculated
words to reduce the chance of memorization [7] issue on Cohen’s Kappa score [10]. While the score was 0.95
Copilot. Therefore, our prompt engineering was done in implying an almost perfect agreement, for cases
two steps: wheretherewereconflictsaboutthedescriptions, the
twoauthorsmetanddiscussedtheconflictstoresolve

## Describing the problem: We needed to summathem. In the end, the descriptions were also crossrize each problem’s description to feed them to Copichecked with the third author who has more than

lot while staying as faithful as possible to the books.
10 years of experience in teaching algorithm design.

### To make sure that our descriptions were understand-

Therefore, the final input descriptions were what all
able and did contain enough information about the
three authors agreed on.
algorithm being described, we cross-checked each of
them with those on popular coding websites such as Excluding sorting algorithms, other problems require code
W3SCHOOLS [52] and GEEKSFORGEEKS [24] as tobegeneratedusingpreviouscodeasitiscommonpractice
well. For cross-checking, the second author summa- in both functional and object oriented programming For
rized [11]’s algorithm descriptions while keeping in these problems, we followed exactly the book’s example
mind Copilot’s limits on the length of the prompt. If by asking Copilot to generate code for the underlying
there were differences in the descriptions (i.e., the de- subproblems and then for the succeeding problems, we
scriptionwasmissingsomekeyelementsinexplaining asked it to implement the solution using the code it had
the problem), the descriptions were revised. generated before. We have recorded all of our descriptions
and Copilot’s responses in our replication package [18].

## Crossvalidationofproblemdescriptions: Crossvalidationofproblemdescriptions: Thesecondauthor

5

<!-- Page 6 -->


#### Solving Fundamental Algorithmic Problems (1) Response Received

with Copilot Our observation shows that if Copilot is unable to pro-
To generate solutions with Copilot, we feed the descrip- vide solutions to the problem with the provided prompt,
tionofeachalgorithmicproblem,callitprompt,toCopilot. it will return irrelevant responses such as repeating user’s
At each attempt on Copilot with a selected prompt, it only prompts, code that only contains import statements or
returns up to the top 10 solutions. Thus, we do not have natural language responses. Thus, this metric helps us to
access to the rest of the potential suggestions. To inquire evaluate if Copilot generates code for the summarized deabout Copilot’s consistency in generating correct solutions, scriptionoftheprograminsteadofthementionedirrelevant
we repeat the process 6 times and each time collect its top responses.
10 suggestions. We used the description of each problem in the form
To assess whether Copilot’s suggestions are consistent of comments and collected up to the top 10 suggestions of
over time, we performed 2 trials within a 30 days time Copilot in 6 different attempts and two separate trials, as
window. Each trial consists of 3 attempts for each prompt it is described in Subsection 3.1.3. To calculate this metric,
and each attempt contains up to 10 suggestions provided if at least one of the suggested solutions in an attempt
by Copilot. The collection of 3 first attempts is called within a trial is code content, we consider it as a successful
“First Trial” and the collection of 3 last attempts which code generation attempt or “Response Received”. Since
were conducted 30 days later is named “Second Trial”. weconduct3separateattemptsineachtrial, wereportthe
Given that Copilot may try to consider the script’s value of this metric with a number ∈[0,3]∈N per trial.
filename as a part of its query, to make sure that solutions
were only generated from our descriptions, we gave the (2) Correct Ratio
scripts unrelated names. We report the correct ratio as a fraction of solutions
suggested by Copilot per problem that are functional and

#### Evaluation Criteria address the objective of the problem. To calculate this

Below, we briefly explain the 4 different metrics which metric,wefirstneedtoevaluatethecorrectnessofCopilot’s
wehaveusedtoevaluateCopilotandexplainthemindetail suggestions for a problem. A suggested code is correct if it
in the rest of this section. The metrics are calculated per passed a set of unit tests.
each fundamental algorithmic problem. However, in algorithmic problems, passing a set of unit
tests to check the correctness of solutions is not enough.

## Response Received ∈ [0,3] ∈ N. The number In this category, not only we need to verify a suggestion

of attempts in each trial that Copilot was able to on passing a set of unit tests, but also we need to verify its
understand the problem and generate code content chosen algorithm.
as its response. For example, in the “Sorting” problems, all problems
have the same functionality: sorting a list of numbers. But

## Correct Ratio (%). The percentage of correct

the importance is the choice of the algorithm to address
solutions suggested by Copilot in each trial.
the problem and to check if Copilot is able to understand

## Code Optimality ∈ [Yes,No]. Whether at least the structure of the solution from the given description. If

one of the correct solutions suggested by Copilot in Copilotimplementsthe“Bubblesort”insteadofthe“Seleceach trial has optimal time complexity [Yes or No]. tion sort” algorithm or uses the Python built-in functions
“sort” or “sorted”, the code is still functionally correct and

## Code Reproducibility ∈[Yes,No]. is able to sort the inputs. But the code is not addressing

the algorithm described in the problem. That is the same
• Within a Trial: Whether at least one of the
situation for implementing the data structure of a BST or
correct solutions suggested by Copilot in one
a graph.
attempt was repeated in two other attempts,
We tackle this challenge of calculating the correct ratio
within a trial [Yes or No].
by following three steps:
• Across Trials: Whether at least one of the
correct solutions suggested by Copilot in the 1. We check the functional correctness of Copilot’s sugfirst trial was repeated in the second trial [Yes gestions on a set of unit tests.
or No].

## We check if the selected algorithm in the solution


## Code Similarity ∈[0,1]∈R. follows the description that we gave to Copilot for

that problem. To conduct this step, same as in Sub-
• Within Trial: The similarity degree between section3.1.2, thetwofirstauthorsseparatelychecked
all correct solutions within a trial. the solutions suggested by Copilot for the problems.
• Across Trials: The similarity of correct solu- They compared the algorithm of the solutions (that
tions between two trials. is employed by Copilot to solve the problem) to the
reference algorithms (ground truth). We collect the
6

<!-- Page 7 -->

ground truth for each problem from the reference text in each solution as they are not part of the code
book [11] and from popular coding websites such itself.
as W3SCHOOLS [52] and GEEKSFORGEEKS [24].
AST similarity is bounded between 0 and 1 with 1

### We calculate Cohen’s Kappa score to measure the

denoting structurally equivalent programs (regardagreement between the two authors.
less of their semantic similarity) and 0 denoting no
equivalence between programs. It also returns 1 for

## The solutions per problem within a trial that passed

“structurallyequivalentrecordedprograms”wherethe
the two above steps are labeled as correct. Then, we
programs are functionally identical but their instruccalculate the correct ratio based on the fraction of
tions are executed in a different order, and “structhe correct solutions within a trial.
turallyequivalentrenamedidenticalprograms”where
the programs are structurally the same with different
(3) Code Optimality
variable names.

### We report this metric because the problems in our

datasetcanbeimplementedwithdifferentalgorithms. This Therefore,thissimilaritymeasurewillnotbeaffected
choice of the algorithm may impact their computation by different statement orders or different variable
complexity for example using a nested loop, queue, or names. However, this similarity will be different
recursive functions to solve a problem. With this metric, for semantically similar programs where the same
we want to check if Copilot is able to suggest the optimal concept is implemented in different ways. In Subsecalgorithm of a problem among its correct suggestions. tion 3.2.4, we explain in more detail why we need to
We cannot write a code to automatically check if the apply this method to detect similar codes when we
computationsizeofanothercodeisoptimalduetoTuring’s discuss Copilot’s duplication solutions.
halting problem [5]. Thus, same as in Subsection 3.1.2 and
• Toapplythiscomparisontocorrectsolutions“Within
Correct Ratio in this section, the two first authors check
a Trial”, we compare the pairs of correct solutions
if there is a solution with an optimal algorithm between
across 3 different attempts within that trial. If at
the correct solutions suggested by Copilot for a problem in
least one of the correct solutions in one attempt is
a trial. They separately compared correct solutions with
reproduced in two other attempts (similarity equals
a reference optimal code for a problem (ground truth). If
1), or in other words if at least one of the correct
at least one of the correct solutions suggested by Copilot
solutions within a trial occurs in all its 3 attempts,
within a trial is optimal, they consider that Copilot is
we consider that Copilot is able to reproduce the
able to find an optimal solution for that problem [Yes]
correct solution for that problem “Within a Trial”
and otherwise [No]. We calculate Cohen’s Kappa score to
[Yes], otherwise, we consider that [No]. To apply
report the agreement of two authors on code optimality.
it “Across Trials”, we compare the pairs of correct
solutions among two trials. If at least one of the
(4) Code Reproducibility and Similarity
correctsolutionsinthefirsttrialisreproducedinthe
While Copilot is closed-source and we have no informasecond trial (similarity equals 1), we consider that
tion about its characteristics that may impact its behavior

### Copilot is able to reproduce the correct solution for

on our prompts, we want to study if this tool is able to
that problem “Across Trials” [Yes], otherwise, we
reproduce a correct solution for a problem in different atconsider that [No].
temptsandovertime. Weintroduce“CodeReproducibility”
as a metric for this measurement. For more clarification,
OurobservationshowsthatinsomecaseshoweverCopiwe split our approach for measuring this metric into three
lot’ssuggestionsarenotexactlythesamebuttheyarevery
subsets:
similar. R2-25: For example, Figure 2 shows two code
• We consider two different types for reproducing a samples for “Insertion Sort”. The differences between the
twocodesamplesareonlysyntacticallyinafewlines. Code
code: the one that checks if a correct solution is

### Sample#1calculatesthelengthofthelistwithintherange

reproduced across different attempts within a trial
in for loop instructor. However, Code Sample #2 assigns
andcallsit“WithinaTrial”,andtheonethatchecks
the length of the list into a variable and then uses it to
if a correct solution of a problem is reproduced over
control the loop. Also, the comparison operator in the
a time window among two trials and call it “Across
while loop condition is different in the two code samples.
Trials”.

### However, only the variables of the operator are switched

• To identify the correct solutions that are reproduced and both are applying the same comparison.
and measure their similarity, we have used the Ab- Therefore, in addition to “Code Reproducibility”, we
stract Syntax Trees (AST) similarity method de- report the “Code Similarity” as the average similarity bescribed in [44]. AST similarity is calculated by first tween pairs of correct solutions for different fundamental
building the AST of a code and then pruning the algorithmicproblems. Tocalculatethesimilarity,wefollow
leaves that are related to variable or function names. the same AST similarity measure as explained above. For
Also, we ignore comments or any natural language “Within a Trial”, we compare all pairs of correct solutions
7

<!-- Page 8 -->

There are studies on Copilot that used easy but more
practicalprogrammingtasksthancourseassignments,such
as tasks in [51] (i.e., editing a CSV file), but these types of
tasks need less problem-solving effort compared to the assignments of a programming course in our selected dataset.
As in this study, our investigations go beyond the code
correctness,thereareotheradvantagestousingthisdataset.
First, this dataset includes students’ submissions that support our research question on comparing Copilot with
humans. Second, the task description in this dataset is
human-written,reducingthechanceofmemorizationissues
[7]. They are new tasks for testing Copilot and different
from the tasks in the Codex test set, i.e., the HumanEval
dataset [8]. In addition, this dataset includes different
test cases for each task alongside a tool for automatically
checking the functional correctness of solutions and the
repairing cost of buggy solutions.
This dataset includes 2442 “Correct” and 1783 “Buggy”
studentsubmissionsfor5Pythonprogrammingassignments

### Figure 2: Two different solutions suggested by Copilot for

Insertionsort. Thereareafewlinesinthesetwocodesam- inaPythoncourse. Anotherstudyalsousedthisdatasetfor
plesthataresyntacticallydifferentbutbothareaddressing characterizing the benefit of adaptive feedback for errors
the same functionality. Code Sample #1 calculates the length
generated by novice developers [1]. Table 1 shows the
ofthelistwithintherangeinforloopinstructor. CodeSample#2
assignsthelengthofthelisttoavariableandthenusesittocontrol descriptionofeachprogrammingtask. Eachtaskincludesa
the loop. The comparison operator in the while loop condition is description of the problem, one or more reference solutions,
differentinthetwocodesamples. However,onlythevariablesofthe adifferentnumberofsubmissionsbystudentsthatincludes
operatorareswitchedandbothareapplyingthesamecomparison.
“Correct” and “Buggy” solutions, and different unit tests
for each task, with an average of 9 tests per problem, to
indifferentattemptswithinatrial,andfor“AcrossTrials”,
evaluate the functional correctness of solutions.
wecompareallpairsofcorrectsolutionsbetweentwotrials.

### This dataset also contains a tool named “Refactory”

Finally, the average of these comparisons is reported for
to automatically repair the buggy submissions of students
each problem.
if applicable [28]. In our study, we use this tool to repair buggy solutions generated by Copilot and students

### RQ2: Copilot vs. Human

to evaluate the complexity of fixing bugs in codes gener-
In this subsection, we aim to describe our research ated by Copilot compared to those of junior programmers.
method for RQ2, on how to compare Copilot codes with This tool matches each buggy program with the closest
humanwrittencodesindifferentquantitativemetrics. First, correct solution based on its AST structure. Then, it modwe illustrate the dataset of programming tasks that we ifies different blocks of the incorrect program to repair its
used in our experiments and explain why we select this bug(s) and convert it to a correct solution if possible. This
dataset. Then, we explain how we employ Copilot to tool shows better performance than other state-of-the-art
generate solutions for each task in this dataset. After that, methods in repairing buggy programs such as Clara [26].
we present how we selected students’ solutions for this Despite others that need a large and diverse range of corcomparison. Finally, we discuss the criteria to compare rect solutions, this tool can repair buggy codes even with
CopilotwithstudentsinsolvingPythonprogrammingtasks one or two references (i.e., correct solutions).
from different aspects.

#### Solving Programming Problems with Copilot


#### Dataset: Python Programming Tasks


### To generate solutions with Copilot, akin to Subsec-

To address RQ2, as we already discussed in Subsection 3.1.3, we feed the description of each programming
tion 3.1, we require a dataset of programming problems
taskinTable1,calledprompt,toCopilot. Ateachattempt,
thatCopilotcansolvesothatwecanconductfurtherinves-
Copilot only returns the Top-10 solutions for a prompt.
tigations on Copilot’s suggestions. Considering the choice

### Thus, we do not have access to the rest of the potential

of programming tasks and in order to have a fair comparisuggestions. To inquire about the Copilot’s consistency in
son, wecompareCopilotwithjuniordevelopers. Therefore,
generating solutions, similar to the previous experiments,
we choose a dataset of a Python programming course that
we repeat the process. In this setup, we repeat the process
includes students’ submissions for 5 programming assign-
5timesandeachtimecollectitstop10suggestedsolutions.
ments2.
Expressly, we ask Copilot to solve each programming problemin5differentattemptsandcollectthetop10suggested
2https://github.com/githubhuyang/refactory
8

<!-- Page 9 -->

Table 1: A summary of the dataset used to compare Copilot with the human in solving simple programming tasks. The
DatasetincludestheassignmentsandsubmissionsofaPythonprogrammingcourse. Itincludesstudents’submissionsfor5Pythonprogramming
tasks[28]. Thelasttwocolumnsrepresentthenumberofstudents’submissionsintwocategories“Correct”and“Buggy”.

### Task Description Correct Buggy


### Takes in a value “x” and a sorted sequence “seq”, and

Sequential returns the position that “x” should go to such that the
q1 768 575
Search sequence remains sorted. Otherwise, return the length of
the sequence.
Given a month and a list of possible birthdays, returns
True if there is only one possible birthday with that

### Unique Dates

q2 month and unique day, and False otherwise. Implement 291 435

### Months

3 different functions: unique day, unique month and contains unique day.
Write a function remove extras(lst) that takes in a list

### Duplicate

q3 and returns a new list with all repeated occurrences of 546 308

### Elimination

any element removed.

### We represent a person using a tuple (gender, age). Given

a list of people, write a function sort age that sorts the
Sorting people and returns a list in an order such that the older
q4 419 357
Tuples people are at the front of the list. You may assume that
no two members in the list of people are of the same age.
Write a function top k that accepts a list of integers as
the input and returns the greatest k number of values as

### Top k

q5 a list, with its elements sorted in descending order. You 418 108

### Elements

may use any sorting algorithm you wish, but you are not
allowed to use sort and sorted.

### Total 2442 1783

solutionsin each one. Thus intotal, we collect50 solutions solutions on the following markers. In the rest of this
by Copilot for each problem. section, we explain each metric in more detail.
As we already explained in Subsection 3.2.1, there are

## Correct Ratio (pass@Topk)

different test cases per task. To evaluate the functional
correctness of Copilot’s solutions, a solution is considered

## Repairing Costs

“’Correct”ifitpassesalltheunittestsrelatedtoitsproblem.
Otherwise, it is considered as “Buggy”. 3. Diversity

## Cyclomatic Complexity


#### Downsampling Student Solutions

In each attempt on Copilot, we only have access to its 5. Syntactic Mastery.
top 10 suggestions while the average number of student
submissions for these tasks is 689.8. One solution to have (1) Correct Ratio (pass@Topk)
more suggestions by Copilot could be to increase the num-
A very common metric to evaluate programming lanber of attempts on Copilot. But, increasing the number
guage models is pass@k metric [31, 8]. For example, calof attempts to more than 5 will increase the number of
culating pass@100 shows the fraction of correct solutions
duplicate answers in Copilot’s suggestions. We discuss the
out of 100 solutions. However, since Copilot returns only
duplicate solutions in Subsection 3.2.4 with more details.
theTop10solutionsineachattempt, wecannotaccurately
Thus, instead of increasing the number of attempts on
use this metric in our study.
Copilot, we downsample the students’ submissions to the

### Inthisstudy,whatattractsourinterestisthepass@Topk

samesizeofCopilotsolutions(50intotal)tohaveanequal
inalltheattempts. ItmeansthatifwecallCopilotntimes
number of solutions for students and Copilot.
for the same problem (the same prompt), n equals the
number of attempts, and collect the Topk solutions of each

#### Evaluation Criteria

attempt, then pass@Topk equals the fraction of these so-
For this part of our study, we consider different criteria lutions that passed all the test units. As an example for
to compare solutions suggested by Copilot and students pass@Top2, we collect all the Top2 suggested solutions
to solve these programming tasks. We investigate the for a problem in n=5 different attempts (#solutions=
k∗n=2∗5=10). Then pass@Top2 reports the fraction
9

<!-- Page 10 -->

of these 10 solutions that passed all test units. We can • Avg. Repair Time: Thismetricshowstheaverage
calculate pass@K for Copilot but we cannot calculate it for time taken to repair a buggy program in seconds.
students.
• Relative Patch Size (RPS): This metric defines
Another evaluation that comes to our attention is the
as the Tree-Edit-Distance (TED) between the AST
Correct Ratio (CR) of solutions. We calculate the correct
of a buggy code and the AST of its repaired code,
ratioofsolutionssameasSubsection3.1.4. HerebyCR,we
normalized by the AST size of the buggy code.
mean the fraction of correct solutions out of all solutions
suggested by the Copilot or human for each problem. We
(3) Diversity
calculate this fraction for each problem while collecting
Topk suggestions of Copilot in different attempts. For It is already shown in language models such as Codex
students, we calculate the fraction of correct submissions that increasing the number of sample solutions for a proout of all students’ submissions for each problem. grammingtaskcanincreasethenumberofcorrectsolutions
Also, we calculate the distribution of the CR and its thatpassalltestunits[8,31]. However,theydidnotstudy
average in independent attempts on Copilot. We like to if this increment is due to the increasing diversity of solustudyhowincreasingthenumberofattempts(givingdiffer- tions or if the new correct solutions are just a duplication
ent chances to Copilot to solve the same problem) impacts of previous ones.
the CR. Copilotclaimsthatitremovesduplicatesolutionsamong
the Top 10 suggested solutions in a single attempt. How-
(2) Repairing Costs ever, our observations show the appearance of duplicate
solutionsintheTop10suggestionsofasingleattempt. Fig-

### After computing the CR for Copilot and students, we

ure 3 shows three different solutions generated by Copilot
aim to compare Copilot’s buggy solutions with students’
for task q3: Duplicate Elimination at a single attempt. As
buggy submissions. Our observation shows that several
wecansee,thestructureofallthreecodesisthesame. The
buggy solutions generated by Copilot can be easily cononly difference between Figure 3a and Figure 3b is in the
verted into a correct solution by applying small changes.
variablename, “item”and“i”. Also, thesolutioninFigure
We discuss this observation in detail in Subsection 4.2.2.
3c is the same as the solution in Figure 3a alongside com-
Repairing cost of bugs in a software project is an imments. Since Copilot compares the sequence of characters
portant metric to show the quality of a code snippet [30].
to eliminate duplicates, it considers these three solutions

### The long repairing time of a bug can be correlated with

as three unique suggestions in the Top 10 solutions of a
structural problems in a code snippet [30]. One of the
single attempt.
important factors that impact the repairing time of a bug

### To remove duplicate solutions in each attempt, we use

is the code churn or the size of changes that are required
the method discussed in Subection 3.1.4 for reproducibility
to fix the bug [55]. Complex or low-quality codes (in case
evaluation. We investigate if increasing the number of
of being buggy) need more time to be repaired, e.g., the
attempts and consequently increasing the total number of
developer needs to spend more time to detect the bug, or
solutionswillincreasethenumberofuniquesolutions. Also,
bigger patches are required for fixing the bug. Thus, to
we compare the diversity of solutions (correct and buggy)
compare the quality of codes generated by Copilot with
provided by Copilot and students. This metric compares
students, we repair the buggy solutions and then compare
Copilot’snoveltyingeneratingsolutionstothatofstudents
them in terms of repair costs.
in solving a programming task.

### We use the repairing tool that we explained in Sub-


### To remark on the duplicate solutions, as we discussed

section 3.2.1. We choose an automated tool for repairing
in Subsection 3.1.4, we compare the AST of two codes. We
buggy codes because:
eliminate the leaves in AST which are related to variable

## Using an automated tool to fix bugs is very common or function names. Also, we ignore comments or any natin software projects. Software projects train their ural language text in each solution. Then, we calculate a

own tool for automatically fixing the bugs within the similarity between the AST of every two solutions for a
projects to save developers time [3]. problem by the method introduced in [44]. If the similarity
between two ASTs is equal to 1, then they are assumed to

## Byusinganautomatedtool,wepreventourrepairing

beduplicates. Wekeepjustoneofthesolutions. Anyvalue
process from being biased by one specific human
lessthan1representsadifferencebetweenthefunctionality
expertise.
of the two solutions.
This tool reports three different metrics to evaluate the
(4) Cyclomatic Complexity
repairing cost of buggy solutions [28] including:

### A programming language is comprised of a set of pro-

• Repair Rate: This metric shows the fraction of gramming keywords and built-in functions, methods, and
buggycodesthatpassedalltestcasesaftertherepair types. Developers may solve a simple programming task
process. in different ways. They may choose different programming
10

<!-- Page 11 -->

(a)Samplecode1 (b)Samplecode2 (c)Samplecode3
Figure3: ThreedifferentsolutionsweregeneratedbyCopilotfortheq3: DuplicateEliminationTaskinoneattempt. There
isnodifferencebetweentheapproachofthese3solutionsinsolvingthetask. Theonlydifferencebetween(a)and(b)isinvariablenames,“i”
and“item”. Thedifferencebetween(c)and(b)istheadditionalcommentin(c). Thedifferencesbetween(c)and(a)areinvariablenames
andcomments.
keywords and built-ins to solve the same problem. How- types in solving the same problem can reflect the develever, even though flexibility in completing a programming opers’ mastery as novice developers may not be familiar
task is desired, it can impact the efficiency, readability, with all possible programming keywords and features in a
and even maintainability of codes in some cases [34, 14]. programming language. While diversity in syntax patterns
These differences can also reflect developers’ mastery of of a solution to address a specific task shows familiarity
the programming language. For example, Figure 4 shows with more programming keywords and built-ins, these ditwo different solutions to a simple programming task, q4: verse solutions may not necessarily be the best practice
Sorting Tuples, from Table 1. Code Sample #1 has more to solve a problem. One of the goals of pair programming
diverse programming syntax keywords and built-in func- in industrial projects is to transfer such experiences from
tions, but Code Sample #2 is easier to understand and experts to novice developers [41, 32, 23]. So, as another
more readable. evaluation criterion, we compare the diversity of program-
Cyclomatic Complexity (McCabe’s Cyclomatic Com- mingkeywordsandPython’sbuilt-infunctionsofCopilot’s
plexity C.C.) is another code quality metric that evaluates code to those of humans.
the understandability of a code snippet. C.C. shows the For example, the codes in Figure 4 are different solunumber of independent paths in a code component, specifi- tions to solve the same programming task. Code sample
cally, thenumberof decisionsthat canbe madein asource #1 has more diverse programming syntax keywords such
code[17,45]. Measuringtheunderstandabilityofcodesnip- as {‘FunctionDef’, ‘List[None]’, ‘for’, ‘if’, ‘BoolOp’, ‘else’,
pets allows us to estimate the required effort for adding ‘break’, ‘elif’, ‘return’} and more diverse built-ins such as
new features to the code or modifying it [46]. {‘append’, ‘range’, ‘insert’}. Code sample #2 includes
There are studies that apply C.C. to measure the read- programming syntax keywords such as {‘FunctionDef’,
ability and understandability of small code snippets [19, ‘Lambda’, ‘NameConstant’, ‘Subscript[Num]’} and built-in
13, 38]. When comparing solutions for a problem, a lower method, ’sort’, which are less diverse than the first sample
C.C. indicates a more readable and understandable code. but more advanced and a less complex solution (in terms
For example, in Figure 4, the C.C. of code samples #1 and of cyclomatic complexity).
# 2 are 4.13 and 1, respectively. While code sample #1 We follow the instructions suggested by [36] to collect
representstwonestedfor-loopstosortthelist,codesample programmingsyntaxpatterns. Weconverteachsolutionto
# 2 simply calls sort and uses a lambda to loop over the its AST and then walk through the syntax tree to collect
list. Such an approach is more Pythonic and also more nodes as programming keywords.
understandable. Tocollectbuilt-infunctionswithinacode,first,weneed
To evaluate if Copilot’s suggestions are as understand- todistinguishthebuilt-infunctionfromotherfunctioncalls
ableashumans’,wecalculatetheC.C.ofCopilot’ssolutions since all types of calls in Python, from built-in to local
andcomparethemtotheC.C.ofhumans’solutionsforthe or public library, are a subset of a node named “Call” in
same problems. Thus, we can assess whether Copilot can AST. To do so, we extract a list of Python built-ins 4.
provide understandable code that is easy to change and Then, we collect the node’s name of the node “Call” if
maintain (lower C.C.) or not if used as a pair programmer its “class name” was in the list of Python built-ins. We
inasoftwareproject. WeuseaPythonpackage,RADON3, comparethediversityofthekeywordsandPythonbuilt-ins
to calculate it. C.C. close or above 10 is interpreted as not in Copilot’s and humans’ codes to study their capabilities
a best practice code. in using Python’s keywords and built-ins.

## Empirical results

(5) Syntactic Mastery
As we already discussed in Subsection 3.2.4/(4), differ- In this section, we present the results we obtained to
ent syntax patterns and built-in functions, methods, and answer our RQs, one by one.
3https://radon.readthedocs.io/en/latest 4https://docs.python.org/3/library/functions.html
11

<!-- Page 12 -->

(2) Correct Ratio

### Copilot shows various behavior in generating correct

solutions for sorting algorithms. The difficulty of problems
impactsits ability togeneratea correctsolutionandto use
the correct algorithm for the implementation. However,
Copilot shows different behavior in two different trials.
For example in the first trial for bubble and bucket sort
which are two easy sorting algorithms, 100%, and 85.71%
of Copilot’s suggestions were correct respectively. However,
in the second trial, it generates no correct solutions for
these two sorting problems.

### Since implementing heap sort requires implementing

a max heap, and then writing a sorting function, this
algorithmishardertoimplement. Inthefirsttrial, Copilot
generates no correct solution for this problem. However,
during our second trial, 9.09% of its suggestions for this
problem are correct. In the second trial for Radix sort,
Copilot showed improvement in solving the problem as it
Figure4: Twodifferentsolutionstosolveq4: SortingTuples.
CodeSample#1hasmorediversesyntaxpatternsandPythonbuilt- generated codes in all three attempts (Response Received)
infunctionscomparedtoCodeSample#2. But#2ismorereadable but none of the generated codes were correct.
andlesscomplex(intermsofC.C.)inunderstandingbecauseofusing Copilot shows some particular behavior for some of the
moreadvancedprogrammingsyntaxandbuilt-inmethods. TheC.C.
sorting algorithms. For example, during the second trial
of Code Sample #1 (written by a human) is 4.13 while it is 1 for
CodeSample#2(suggestedbyCopilot). where we asked it to generate codes for Bucket sort, some
of the generated codes were calling the Quick sort function
for sorting the buckets even though Quick sort had not

### RQ1: Copilot on Algorithm Design

been implemented in the code.
In this section, we assess the capability of Copilot to For validating the algorithm choice in solutions that
solve algorithmic problems. To highlight the difference passed all unit tests, two authors disagreed on the result
between our two trials which have been conducted 30 days for selection sort. The input prompt was summarized
apart from each other, for each marker, we have indicated from the descriptions collected from the algorithm design
the results of the solutions “Within a Trial” separately book[11]. Thegivenpromptforthisalgorithmwas“Create
from each other as “First Trial” and “Second Trial”. For afunctionthatacceptsalistasinput. Thefunctionshould
this part of our study, we discuss the different evaluation create two lists named sorted and unsorted. The function
criteria per each category of problems since our finding sorts an array by repeatedly finding the minimum element
shows there is a correlation between the difficulty of the (considering ascending order) from an unsorted list and
categories and the results. putting it at the beginning of the sorted list. Finally, it
should return the sorted array”. Given this description,

#### Sorting Algorithms the second author only accepted solutions that followed

In this section, we discuss our findings on Sorting Al- this exact description, mainly those which created the two
gorithms. For those evaluation metrics where the manual empty sorted and unsorted lists. Upon review, however,
inspection of authors was required (Response Received, al- the first and third authors mentioned that some solutions
gorithmvalidationonCorrectRatio,andcodeOptimality), followed the selection sort algorithm, without following the
the authors achieved 89% of the Kappa agreement. We exactstepsmentionedinthedescription. Afterdiscussions,
discuss the details in the following of this section. these solutions were considered as correct as well.
(1) Response Received (3) Code Optimality
Our results in Table 2 on sorting algorithms show that Our result on code optimality shows that if Copilot is
when the algorithm gets more difficult and requires more able to generate correct solutions for a sorting algorithm,
details in implementation, Copilot struggles to generate it generates an optimal solution for that problem, too. In
solutions. For example, on the first trial, for Heap and the first trial, Copilot generates correct solutions for 7 out
Radix sort, Copilot generates code in only one of the 3 of 8 sorting algorithms and it is able to generate optimal
attempts within the trial. However, in the second trial, solutions for these 7 problems in the same trial, too. In
Copilot showed improvement as it generated codes in all the second trial, Copilot generates correct solutions for
three attempts. The situation is the opposite for Merge 4 sorting algorithms and it is able to generate optimal
sort. In the first trial, Copilot generates code in all three solutions within its correct solutions for these 4 sorting
attempts. But in the second trial, it is responsive in only problems as well.
two of the three attempts.
12

<!-- Page 13 -->

are not exactly reproduced for the majority of sorting
algorithms.
However, the correct solutions are not exactly reproduced within a trial or across two trials, our results in
Table 3 on the similarity degree between pairs of correct
solutions show that they are very similar in some cases.
For example, for Quick sort in the second trial, the correct
solutions are not exactly reproduced but based on Table
3, there is a 0.99 similarity between its correct solutions.

### As another example, for selection sort in the first trial

and across two trials, the correct solutions are not exactly
reproduced but the similarity degree between them equals
0.61 and 0.63 respectively.

### Same as code optimality, if Copilot was not able to

generate the correct solution for a problem within a trial,
then the code reproducibility metric and similarity degree
are not applicable. Also, if Copilot generates correct solutions for the sorting problems just in one of two trials,
then reproducibility and similarity across trials are not
Figure 5: Two different solutions suggested by Copilot for
applicable. We use “-” for nonapplicable cases.

### Quick sort. CodeSample#1isarecursivefunction. Itpickedthe

firstelementasapivottopartitionthegivenarrayandemployedthe
correct “Divide and Conquer” algorithm to implement Quick sort. Summary of Results. In summary, Copilot is relatively
However, Code Sample #2 randomly divided the given array into capable of providing solutions for sorting problems. It
partitions. Itisbuggy,anditisnotdeployingthesortingproperly,
is responsive (Response Received) for 6 out of 8 sorting
butitusesthePythonbuilt-infunction,“sort”tosorteachpartition.
problems of the first trial and for 7 out of 8 problems of
the second trial.
Since we have no correct solutions for example for Bub-
On Correct Ratio, in the first trial, Copilot generates
blesortorBucketsortinthesecondtrial,codeoptimalityis
correct solutions for all sorting problems except Heap sort,
not applicable for these cases. Thus, we show their results
and on average, 51.42% of its solutions within this trial
with “-”.
are correct. However, in the second trial, it generates

### However, this result on sorting algorithms is due to the

correct solutions for only 4 sorting problems (out of 8) and
fact that for some of the sorting algorithms such as bubble
the average correct ratio within this trial is 34.77%. In
sortorheapsort,thereisnootherpossibleimplementation
both trials, if Copilot generates the correct solution for a
than the optimal one (quadratic or log-linear).
problem, at least one of those correct solutions is optimal.

### We also observed that Copilot generates Pythonic code


### Finally, the correct solutions suggested by Copilot are

or uses Python’s language-specific features instead of renot exactly reproduced for the 4th, 3rd, and 2nd sorting
implementing the desired functionality to some extent. For
problems in the first trial, second trial, and across two
example, alongside using list comprehensions (which are
trials respectively, but the similarity degree between some
faster in Python than iterating over the list in explicit forof those non-reproduced correct solutions is above 0.6. In
loops), Copilot generated codes that use built-in functions.
some trials and for some of the sorting problems the code

### An example of this can be observed in Figure 5, codes

optimality,reproducibility,andsimilarityarenotapplicable
generated for the Quick sort where after dividing the input
due to the lack of comparable correct solutions.
array into left and right subarrays, instead of generating
code for sorting the arrays, Copilot used Python’s built-in

#### Binary Search Trees

sort function. For sorting problems where iterating over

### In this section we discuss ourfindings onBinary Search

the entire input was required, instead of using while loops,

### Trees (BSTs). The Kappa agreement between two authors

Copilot generates code with either explicit “for” loops or
on evaluation metrics that needed manual inspection is
list comprehensions. Doing so removes the risk of getting
100%. For this problem, we first asked Copilot to generate
trapped in an infinite loop and in the case of using list
the BST data structure which should comprise of a class
comprehensionscanmakearealdifferenceintheprogram’s
with parent, right, and left nodes alongside the node’s
running time.
value. After that, we asked Copilot to generate a method
whichhandlesinsertionpertheBSTinsertionalgorithmfor
(4) Code Reproducibility and Similarity
the class. Then, we asked Copilot to create a method for
As the last evaluation metric in Table 2, we report if at
deleting a node. These operations require the BST to be
least one of the correct solutions suggested by Copilot is
re-built in order to conform to the BST property. We also
exactly reproduced (similarity equals 1) within a trial and
asked Copilot to implement a search method for finding if
across two trials. Our result shows that correct solutions
a value is present in the BST. These 3 methods, comprise
13

<!-- Page 14 -->

Table2: Results of Copilot’s code generation ability on fundamental algorithmic problems. “Response Received”showsthe
numberofattemptsineachtrialthatCopilotcangeneratecodesfortheproposedprompt. Itrangesin[0,3]∈N. “Correct Ratio”shows
thepercentageofcorrectsolutionsineachtrial. “Optimal”statusis“Yes”ifatleastoneofthecorrectsolutionsineachtrailisoptimal. Ifat
leastonecorrectsolutioninoneofthethreeattempts(WithinaTrial)repeatsintwootherattempts(atthesameTrial),then“Reproduced”
is“Yes”. “Across Trials”for“Reproduced”metricis“Yes”ifatleastoneofthecorrectsolutionsfromtheFirstTrialrepeatsinSecond
Trial. Ifthemetricsarenotapplicablethenitpresentsby“-”. Forexample,in“SecondTrial”of“BubbleSort”,wereceiveno(0)response
fromCopilot. Consequently,“CorrectRatio”and“Optimal”in‘SecondTrial”and“Reproduced”in“SecondTrial”and“AcrossTrials”assign
“-”forthisalgorithm.
ResponseReceived[0,3] CorrectRatio[%] Optimal[Yes/No] Reproduced[Yes/No]

### Algorithm

FirstTrial SecondTrial FirstTrial SecondTrial FirstTrial SecondTrial FirstTrial SecondTrial AcrossTrials

### SortingAlgorithms


### BubbleSort 3 3 100 0 Yes - Yes - -

BucketSort 3 3 85.71 0 Yes - Yes - -

### HeapSort 1 3 0 9.09 - Yes - No -

InsertionSort 3 3 100 100 Yes Yes Yes Yes Yes

### MergeSort 3 2 33.34 0 Yes - No - -

QuickSort 3 3 16.67 16.67 Yes Yes No No No

### RadixSort 1 3 10 0 Yes - No - -

SelectionSort 3 3 14.28 13.34 Yes Yes No No No

### BinarySearchTrees


### DataStructure 3 1 61.9 35.71 Yes Yes No No Yes

MinandMaxValuesinTree 3 3 71.42 66.67 Yes Yes No Yes No

### In-orderTreeWalk 3 3 94.12 16.67 Yes Yes Yes No Yes

FindingTheSuccessorNode 3 3 100 100 No Yes No Yes Yes

### ElementaryGraphAlgorithms


### SimpleDataStructure 2 2 50 0 Yes - No - -

BreadthFirstSearch 3 3 100 100 Yes Yes Yes Yes Yes

### DepthFirstSearch 3 3 75 0 Yes - No - -

DirectedAcyclicDataStructure 2 3 86.37 0 Yes - No - -
FindingReachableVertices 3 3 60 100 Yes No Yes Yes No

### GreedyAlgorithms


### ActivityClass 2 3 0 0 - - - - -


### ComparingActivities 3 3 9.52 0 Yes - Yes - -

AddingActivitiestoaSet 3 3 13.33 16.67 Yes No No No Yes
GenerateAllinonePrompt 1 3 0 0 - - - - -
14

<!-- Page 15 -->

Table 3: Similarity ratios of the AST of Copilot’s correct versions (with iterative and recursive programming techsuggestions on fundamental algorithmic problems. Tocalcuniques) for “Finding maximum and minimum values in
latethesimilarity,weremovedtheduplicatecorrectsolutionsineach
attempt(threeattemptswithinatrial). Theresultsshowhowever the tree”, “In-order tree walk”, and “Finding successor
someofthecorrectsolutionsarenotexactlyreproducedindifferent nodes” problems. For the “In-order Tree Walk” problem,
attemptswithinatrialorbetweentwotrials,buttheyareverysimilar. Copilot generated functions inside the main function re-
Thesimilarityisblank,“-”,ifitcannotbecalculated(i.e. nocorrect
sponsible for executing the walk. These functions were
solutionoronlyonecorrectsolution).
duplicatefunctionsofthosegeneratedforfindingminimum
Algorithm FirstTrial SecondTrial AcrossTrials andmaximumvaluesinthetree. Thisisbadprogramming
SortingAlgorithms practice as it over-complicates the code. However, since
BubbleSort 0.93 - - these functions were not used by the original function at

### BucketSort 1 - -

HeapSort - - - all, the generated code was still optimal. Copilot tends

### InsertionSort 0.99 1 0.99

to generate recursive functions when the solution can be

### MergeSort - - -

QuickSort - - 0.99 solved using such an approach. For example, for the “In-

### RadixSort - - -

SelectionSort 0.61 - 0.63 order Tree Walk” and “Finding maximum and minimum
BinarySearchTrees values in the tree” problems, the generated codes are all
DataStructure 0.51 0.46 0.53 recursive functions.

### MinandMaxValuesinTree - 1 0.83

In-orderTreeWalk 1 - 1 Thus, for all the BST problems in both trials, except

### FindingTheSuccessorNode 0.33 0.99 0.55

for “Finding successor nodes” in the first trial, at least one

### ElementaryGraphAlgorithms

of the correct solutions suggested by Copilot has optimal

### SimpleDataStructure 0.25 - -

BreadthFirstSearch 0.54 0.72 0.45 time complexity.

### DepthFirstSearch 0.73 - -

DirectedAcyclicDataStructure 0.63 - -

### FindingReachableVertices 0.79 1 0.076

(4) Code Reproducibility and Similarity

### GreedyAlgorithms

As it is shown in Table 2, in the first trial, Copilot

### ActivityClass - - -

ComparingActivities 1 - - exactly reproduces at least one of its correct solutions in 3

### AddingActivitiestoaSet 0.09 0.11 0.17

GenerateAllinonePrompt - - - differentattemptsonlyforthe“In-ordertreewalk”problem.

### Based on Table 3, the similarity between the pairs of its

correct solutions is not greater than 0.51 for those correct
the base BST data structure. In the next steps, we asked
solutions that are not exactly reproduced. For example,

### Copilottogeneratefunctionsforfindingthemaximumand

the similarity of correct solutions in different attempts of
minimum value in a tree, performing an in-order tree walk,
the first trial for “Data Structure” and “Finding successor
and finding the successor node of a child node. We discuss
nodes” are 0.51 and 0.33 respectively.
the details of our results in the following section.
In the second trial, based on Table 2, the exact correct
solutions are reproduced for “Finding maximum and min-
(1) Response Received
imum values in the Tree” and “Finding successor nodes”
Our results show that Copilot is capable of understandproblems. The similarity for correct solutions of ‘Data
ing the BST problems in both trials. Only in the second
Structure” which is not exactly reproduced in this trial is
trial, Copilot struggles in suggesting code in 2 out of 3
0.46.
attempts for generating the data structure of a BST.

### Unlike sorting algorithms, reproducibility across two

trials was not an issue on BST problems as Copilot repro-
(2) Correct Ratio
ducesatleastoneofthecorrectsolutionsfromthefirsttrial
OurresultsinTable2showthatCopilothasinconsistent in the second trials for all BST problems except “Finding
behavior in generating correct solutions for some BST maximum and minimum values in the Tree”. However,
problems in two trials. For example, considering the “In- Table 3 shows that the similarity of the correct solution for
order Tree Walk”, 94.12% of Copilot’s suggestions are this problem across two trials is 0.83.
correct in the first trial, but in the second trial, it reduces
to 16.67%. However, for the two problems, “Min and Max Summary of Results. In summary, Copilot is capable
Values in Tree” and “Finding The Successor Node”, the of understanding the description of BST problems in both
correct ratio on both trials are very close to each other. trials, except for the “Data Structure” problem on the
For example, for ‘Finding The Successor Node”, 100% of second trial.
Copilot’s suggestions are correct in both trials. Copilot has inconsistent behavior in generating correct
solutions in two trials as 81.86% of its solutions are correct
(3) Code Optimality in the first trial but the correct ratio equals 54.76% in the
It should be noted that, in a majority of the cases, second trial. Copilot was able to generate optimal code for
Copilot was able to generate code consistent with optimal all the BST problems in both trials except for “Finding
time complexities as required for an efficient BST problem. successor nodes” in the first trial.
In addition, Copilot was able to generate multiple different Copilotstruggledinexactlyreproducingitscorrectsolutions within each trial and the similarity of those solutions
15

<!-- Page 16 -->

that are not exactly reproduced is not above 0.51. However,Copilotreproducesatleastoneofitscorrectsolutions
from the first trial in the second trial (Across Trials) for all

### BST problems except “Finding maximum and minimum

values in the Tree”. Although the correct solutions for this
problem are not exactly reproduced across two trials, the
Figure 6: R2-10 and R2-25: Code sample of operator oversimilarity of its correct solutions is 0.83.
loading. “operatoroverloading”isanadvancedPythonfeaturein
which a Python built-in function is re-written by the programmer

#### Elementary Graph Algorithms tobehavedifferentlydependingontheargumentsthatitreceivesas

input. “contains” and “str” are two Python native functions that
In this section, we discuss our findings on Elementary
Copilotre-wroteingraphproblems.

### Graph Algorithms. The Kappa agreement between the

two authors on metrics that needed manual inspection is
trial, out of 2 problems that Copilot addressed correctly,
83%. As our algorithms are becoming more complex, it is
onlyoneofthem,BFS,includestheoptimalsolutionwithin
requiredforCopilottogeneratecodethatusestheprevious
its correct solutions. Checking if a graph is cyclic, requires
codes that it has generated. We discuss the details of our
using a BFS or DFS approach. If Copilot does not use
results in the following section.
the codes that it has generated for BFS and DFS during
(1) Response Received checkingifagraphiscyclic,wewillbeleftwithcodepieces
thatrepeatthesameoperationoverandoverwhichisabad
Our results in Table 2 show that like BSTs, Copilot is
practice in programming. We consider those suggestions
adept at generating code for elementary graph algorithms.
as non-optimal.
In the first trial, Copilot generates code in all 3 attempts
We examined the solutions suggested by Copilot for
forallgraphproblemsexcept“SimpleDataStructure”and
constructing the graph data structure and observed that
“Directed Acyclic Data Structure” and in the second trial,
its solutions contain both list comprehensions and explicit
it struggles only in one of the 3 attempts on “Simple Data
“for” loops. In one of the correct solutions, the generated
Structure”.
code constructs the nodes from the input using explicit
(2) Correct Ratio “for” loops and in another solution, it does so using list
comprehensions. We accept the code that uses list compre-

### As we can find in Table 2, same as BST problems,

hensionsasoptimalsinceiftheinputislarge,thereisareal
Copilot shows inconsistent behavior in generating correct
running time difference between these two approaches. We
solutions for some graph problems in two trials. For exalso observed that some of the generated codes are using
ample, for “Simple Data Structure”, “Depth First Search”
an advanced Python feature called “operator overloading”
and “Directed Acyclic Data Structure” in the first trial,
in which a native Python function is re-written by the pro-
50%, 75% and 86.37% of Copilot’s Suggestions are correct
grammertobehavedifferentlydependingonthearguments
respectively. However, in the second trial, Copilot is not
that it receives as input. Figure 6 shows an example of
able to generate correct solutions for these problems. For
operator overloading generated by Copilot.
the “BFS” problem, 100% of Copilot solutions are correct
in both trials.
(4) Code Reproducibility and Similarity

### Our observation shows that during different attempts

on Copilot to generate code for BFS and DFS, Copilot As we can find in Table 2, in the first trial, Copilot is
generated code for both algorithms regardless of us asking abletoreproduceatleastoneofitscorrectsolutionsforonly
it to do so only for one of them. two graph problems, “Breath First Search” and “Finding
EventhoughCopilotwasabletorecognizeandgenerate Reachable Vertices”. However, for other problems such as
code for our description, some of the generated codes had “DepthFirstSearch”and’DirectedAcyclicDataStructure”,
one flaw and since successor methods use the previous the correct solution is not exactly reproduced by Copilot
methods, this bug was present in every piece of generated but their similarity equals 0.73 and 0.63 respectively. In
code. Thissnow-ballingeffecthasaffectedourKappascore the second trial, Copilot is able to reproduce the correct
as well. This bug was a result of Copilot considering the solutionsforthosetwoproblemsthatitaddressedcorrectly.
nodes being named by integer numbers. As a result, if a For across trials, Copilot is able to exactly reproduce the
node is created with a name that is not an integer (e.g. correct solutions only for the BFS problem. The similarity
”A” or ”Node1” instead of ”1” or ”2”), the code will fail between correct solutions of “Finding Reachable Vertices”
to iterate through the list of nodes and generate a syntax is very low across two trials, 0.076.
error. However, since the code functioned correctly given
Summary of Results. OurresultsshowCopilotisadept
the normal usage, we labeled them as correct.
at generating code for elementary graph algorithms. However, same as BST, Copilot shows inconsistent behavior
(3) Code Optimality
in generating correct solutions for some graph problems

### Inthefirsttrial,Copilotgeneratedoneoptimalsolution

in two trials. In the first trial, Copilot is able to generate
for each of the graph problems. However, in the second
16

<!-- Page 17 -->

correct solutions for all graph problems with an average activity starts. if the inputs have overlapping start-times,
correct ratio of 74.27%. However, in the second trial, it return False”. Here, Copilot implemented the description
is able to generate correct solutions for only two prob- correctly. However, since this method is dependent on
lems and 100% of its correct solutions are correct. Copilot its inputs being instances of the activity class, this code
was able to generate optimal code for all problems that will fail if the input is anything else. Type checking is
it addressed correctly in both trials except for “Finding important and a basic operation to do which Copilot fails
Reachable Vertices” in the second trial. In the manner todohere. Finally,foraddingactivitiestoasetofactivities,
of reproducibility, it struggled to reproduce its correct so- Copilotwasaskedtocreateamethodwhichacceptsasetof
lutions for all graph problems. However, the similarity activitiesalongsideastarttimeandendtimeofanactivity.
between correct solutions for some problems is more than The method should first create a new activity instance
0.6. with the given start and end time and then check if this
new activity does not overlap with the activities in the set.

#### Greedy Algorithms Copilot was unable to generate the necessary code for this

In this section, we discuss our findings on the “activity no matter how detailed the description was.
selection” problem as a Greedy Algorithm. The Kappa
agreementbetweenthetwoauthorsonmetricsthatneeded (3) Code Optimality
manual inspection is 100%. The “activity selection” prob- AsCopilotwasnotabletogeneratecorrectsolutionsto
lem requires the programmer to define a class for “activ- mostoftheproblems, wecouldonlyanalyzetheoptimality
ities”. Each activity has a start and end time. The goal of the solutions generated for “Comparing activities” and
of this problem is: given a set of activities where each “AddingActivitiestoaSet”. Here,thegeneratedcodeswere
activity has its own start and ending time, return a set simple (As was the underlying problem) and the solutions
that contains the maximum number of activities that can required only checking the boundaries of class attributes
be performed as long as they do not overlap. Overlapping or whether the output of a function was true or not.
is defined as:
(4) Code Reproducibility and Similarity
• An activity’s start time must be after a previous As Table 2 and 3 show, Copilot was only capable
activity’s end time. of reproducing solutions to a problem for the “Adding
activitiestoaset”problemacrosstrailsandthesesolutions
• An activity should not happen during another activwere different from each other. As Table 3 shows, for
ity.
the “Comparing Activities” problem, Copilot generated
Forthisproblem,weaskedCopilottogeneratecodesfor solutions which were exactly the same in the same trial.
implementing the activity class, comparing activities, and However, in the second trial it was not capable of even
finallycheckingforoverlapsbetweenactivitiestoinvestigate producing a correct solution.
if the generated solutions are “greedy”.

### Summary of Results. The activity selection problem

was used as a proxy to see whether Copilot would be able
(1) Response Received
to generate code for solving this problem with a greedy

### Our results in Table 2 show that Copilot is capable

solution. However, Copilot was not able to generate soof understanding what the underlying problem is and can
lutions that satisfied the criteria of a correct solution. In
generate code for it. Our observations show that Copilot
particular, Copilot showed difficulties in understanding
can even generate code when we give it the entire problem
type checking and variable boundary checking even though
definition (activity class, comparing activities, and adding
such behaviors were explicitly required in the prompt.
activities to a set) in one go.
Findings: Copilot is able to recognize fundamen-
(2) Correct Ratio
tal algorithms by their names and generate correct,
Even though Copilot is capable of understanding what
optimal code for them as long as the descriptions
we ask from it, the codes that it generates for solving
areshortandconcise. Insomecases,thedevelopers
the problem are either buggy or incorrect. For example,
may need to invoke Copilot multiple times in order
given the prompt “implement a class called activity. Each
to receive solutions that are correct and tailored to
instanceofthisclasshastwoattributes: start-timeandendtheir descriptions.
time. Both should be integer numbers between 0 and 24”,

### Challenges: Copilot is unable to generate code

the generated code has no functionalities for checking the
for type-checking variables. It also generates needinput type or their boundaries. In another problem, when
lesslycomplicatedcodeforsomesimpledescriptions.
we asked Copilot to implement a method for comparing

### Hence, Copilot still needs to be improved to truly

activities, we gave it the following prompt: “implement a
be considered as a pair programmer.
function for comparing two activities. the function should
return True if the first activity ends before the second
17

<!-- Page 18 -->


### RQ2: Copilot vs. Human in Solving Program-

Table4: TheCorrectRatio(CR)ofCopilot’ssolutionswhilecollecting
ming Problems Top1,Top5,andTop10solutionsinall5attemptscomparedtothe

### CorrectRatio(CR)ofstudents’submissions

In this section, we discuss our findings to answer RQ2.

### Copilot Students

We discuss the results for each criterion of our evaluation
Task CR@Top1 CR@Top5 CR@Top10 CR
separately.
q1 SequentialSearch 0.6 0.44 0.36 0.57
q2 UniqueDatesMonths 0.00 0.00 0.00 0.40
q3 DuplicateElimination 1 0.72 0.56 0.64

#### Correct ratio of Copilot’s suggestions and

q4 SortingTuples 0.00 0.08 0.14 0.54
students’ submissions q5 Top-kElements 1 0.92 0.76 0.79

### Total 0.52 0.43 0.35 0.59


### As explained in Subsection 3.2.4, we calculate the

pass@Topk for solutions generated by Copilot for each
programming task. The pass@Topk shows the fraction of comparison, we calculate three different CRs for Copilot.
correct solutions among the Topk solutions, collected from The first, CR@Top1, reports the number of correct solu-
5 different attempts. We normalized the values to report tions out of all Top1 solutions in 5 different attempts for
this metric for the programming tasks. each programming task. CR@Top5 calculates the fraction
Figure 7a shows the normalized values for pass@Topk of correct solutions out of all Top5 solutions suggested
of each programming task for Copilot. TopK solutions by Copilot in 5 different attempts. Finally, CR@Top10
range between Top1 to Top10 because each attempt on represents the number of correct solutions generated by
Copilot includes only the Top10 suggestions. Based on Copilot out of all its 50 solutions for a programming task.
this result, Copilot cannot find correct solutions for “q2: CollectingmoresolutionsdecreasestheCRofCopilotsince
Unique Dates Months”. This task asks for “...solve the itincreasesthefractionofwrongsolutions. Forsomeofthe
problem by implementing 3 different functions...”. Copilot questions, CR@Top1 and CR@Top5 of Copilot are greater
couldnotunderstandthispointwithinthetaskdescription than students’ CR. For all questions, the CR of students’
and tried to solve the problem in one function. Thus, all of submissions is greater than CR@Top10 for Copilot’s sug-
Copilot’ssolutionsforthistaskfailedthetestcasesbecause gestions. On average for all the programming tasks, the
the test units of this task are based on implementing 3 CorrectRatio(CR)ofstudents’submissionsisgreaterthan
different functions. the CR of Copilot’s suggestions.
There are no correct solutions in Copilot’s Top3 suggestions for “q4: Sorting Tuples” in 5 different attempts. 4.2.2. Repairing costs of Buggy solutions generated
It increases to 0.02 in the set of Top4 solutions. For “q1”, by Copilot and students
“q3”, and “q5”, the pass@Top1 is equal to 0.08, 0.13, and In this part, we compare the repair cost of buggy solu-
0.13, respectively. For some questions, the pass@Topk, tions for Copilot with students. As we already discussed,
at different values of k, shows greater values than the our observation shows there are buggy solutions that are
other questions. For example, “q5” has the greatest val- generated by Copilot and are very similar to correct soues for pass@Top4 and above. Also, “q4” has the lowest lutions. A small change can convert them into a correct
pass@Topk, for different values of k, after “q2”. solution. Therefore,weattempttoquantifyourobservation
In general, pass@Topk increases by increasing the k. It by calculating the intersection between Copilot’s correct
means collecting a larger number of solutions suggested by and buggy solutions for each problem using the BLEU
Copilot increases the number of correct solutions and this score [39]. The comparison has been done in a pairwise
growth can be different for different programming tasks. manner between each correct and each buggy solution. For
In addition, Figure 7b shows the Correct Ratio (CR) example, if out of 50 solutions, 40 are correct and 10 are
of solutions in each attempt independently. However, the buggy, we end up with 400 pairwise comparisons.
distribution of CRs in different attempts is varied, but BLEUisusedinevaluatingprogramsynthesisapproaches
adding new attempts can increase the average CR of solu- such as text-to-code, code summarization, and code predictions. For example, the average CR in the first attempt tion. BLEU score uses the n-gram overlap between tokens
(atp1) is equal to 0.32 while it increases to 0.44 in the last of two contents and penalizes length difference. It returns
attempts (atp5). It shows if we ask Copilot to solve the a value between 0 and 1 [50]. BLEU measures how well
same problem multiple times (here 5 attempts), there is twotextsmatchoraresimilartoeachother. Renetal.[43]
a chance to increase the CR among new Top10 suggested introduces a new metric, called CodeBLEU, that measures
solutions on average. However, this is not correct for all the BLEU score on syntax and semantics of codes. As a
questions. For example for “q1”, the CR in “atp4” is 0.7 part of this new metric, they measure CodeBLEU between
but it decreases to 0.4 in “atp5”. But, for “q5”, the CR in AST of codes.
the first attempt is equal to 0.7 and it increases to 0.9 in To measure the overlap between correct and buggy
the last attempt. solutions, we measure the BLEU score between the AST of
Since we cannot calculate pass@Topk for students, in the buggy and correct. We omit those buggy codes which
Table 4, we compare the CR of solutions generated by have syntax errors and cannot be converted into AST. For
Copilot with the CR of students’ submissions. For this example, the BLEU score of more than 0.7 between the
18

<!-- Page 19 -->

(a)Normalizedpass@Topkof5differentattempts (b)CRofsolutionsin5attempts
Figure7: Evaluation of correct solutions generated by Copilot. Plot(a)showsthenormalizedvaluesforpass@Topkmetricsagainst
differentvaluesofk. ItshowsthefractionofcorrectsolutionsbetweenTopksolutionsof5differentattempts. Plot(b)showsthedistribution,
averageandstandarddeviationoftheCorrectRatio(CR)ineachattemptfordifferentprogrammingtasks.
AST of several correct and buggy pairs of solutions implies dent buggy submissions. The average repairing time for
a high similarity between these two solutions. It can give Copilot’s buggy solutions is 4.94 seconds while it is equal
us an estimation of the number of changes that we need to to 6.48 seconds for the students. The reason is that on
apply to a buggy solution to repair it. average, the Relative Patch Size (RPS) of Copilot’s buggy
Figure 8 shows the density distribution for the BLEU solutionsthatneedtoberepairedissmallerthanstudents’.
score among pairs of the buggy and correct solutions gen- AswecanfindinTable5, theaverageRPSforCopilotand
erated by Copilot for different programming tasks. As we students are 0.33 and 0.35, respectively.
can see in this figure, there are pairs of correct and buggy We can conclude that however on average, the CR of
solutionswithBLEUscoresof0.75orgreater. Itshowsthat students’ submissions is greater than Copilot’s solutions,
sometimes a small change in a buggy solution generated but the repairing costs of buggy solutions of Copilot are
by Copilot can easily convert it into a correct solution, for less than students. With a repairing tool, we can repair
example, changing “>” (greater) to “≥” (greater equal). the majority of buggy solutions generated by Copilot and
Now that some of the buggy solutions generated by increase its CR.
Copilot are very similar to the correct solutions, we are in- Thus, if Copilot, as a pair programmer in a software
terested in comparing the repairing cost of Copilot’s buggy project, suggests buggy solutions, it is less expensive to fix
solutions with students’ buggy submissions. As we have its bugs compared to bugs that may be produced by junior
explained in Subsection 3.2.3, for this comparison, we need developers when solving the same programming task.
to downsample students’ submissions to the same size as
Copilot’s suggestions. Figure 9 shows the distribution of 4.2.3. Diversity of Copilot’s suggestions and sturepairing time for repairing students’ buggy submissions. dents’ submissions
There are a high number of submissions with low repairing The diversity of solutions shows the novelty of Copilot
time and few with high repairing time. Thus, to keep the and students in solving different problems. Also, it shows
distribution of repairing costs in the sample set close to that while increasing the number of sample codes increases
the entire population, we repeat the downsampling pro- the fraction of correct solutions, this increment is due
cess 5 times and report all repairing metrics for students’ to the diversity of correct solutions or duplication. As we
submissions based on the average of all 5 sampleset. discussedinSubsection3.2.4,weobserveduplicatesolutions
As we can find in Table5, the average repair rate for inasingleattemptandacrossmultipleattemptsonCopilot
Copilot’s buggy solutions is greater than students’, which tosolveaproblem. Ontheotherhand,weobserveduplicate
are 0.95 and 0.89 respectively. This means that on average, solutionsamongstudents’submissionsaswell. Forexample,
95% of buggy solutions generated by Copilot have been for “q1: Sequential Search”, after comparing the ASTs of
fixedaftertherepairprocess. Forexample,for“q4: Sorting students’ correct submissions, 54.32% of their submissions
Tuples” and “q5: Top-k Elements”, all buggy solutions of are identified to be duplicated.
Copilot (100%) have been fixed while the repairing rate of To compare the diversity among students’ submissions
students’ submissions for these two tasks is equal to 85%. and Copilot’s solutions, we randomly downsample 10 stu-
In addition, the average repair time for Copilot’s buggy dent submissions in 5 different sample sets and consider
solutions is less than the students’. This means that not them as 5 different attempts. Then, in each attempt on
only the repairing tool can fix the majority of Copilot’s Copilot and for each sample set of students’ submissions,
buggy solutions but also it can fix them faster than stu- we eliminate duplicate correct and buggy solutions. There
19

<!-- Page 20 -->

Figure8: Distribution of BLEU score among the pair of correct and buggy solutions generated by Copilot. Thischartshows
ahistogramoftheBLEUScoreonpairsofcorrectandbuggysolutionsgeneratedbyCopilot. TheBLEUscoreof0.75andaboverepresentsa
greatsimilaritybetweentheASTofacorrectandbuggypair. TheBLEUscorebetweenseveralpairsofthebuggyandcorrectsolutionsis
greaterthan0.7,indifferentprogrammingtasks. Thissupportsourobservationthatseveralbuggysolutionscanbecorrectedwithsmall
changes.
Figure 9: The distribution of repairing time for students’ buggy submissions. This chart shows a histogram of students’ buggy
submissionsbasedontheirrepairingtime. Itshowsthattherearemorebuggysubmissionswithlowrepairingtimethanbuggysubmissions
withhighrepairingtime. Werepeatthedownsamplingprocessonstudents’submissions5timestoobservethesamedistributioninsamplesets.
20

<!-- Page 21 -->

Table5: ComparingtheRepairingCostofCopilot’ssuggestionswithstudents’ssubmissions

### Copilot Students

Rep Avg Rep Avg Rep Avg Rep Avg

### Task


### Rate Time(sec) rps Rate Time RPS

q1 sequential search 0.94 9.61 0.48 0.98 2.58 0.40
q2 unique dates months 0.92 3.26 0.28 0.82 3.81 0.44
q3 duplicate elimination 0.91 0.64 0.26 0.96 4.35 0.30
q4 sorting tuples 1.00 0.78 0.15 0.85 8.82 0.29
q5 top-k elements 1.00 10.40 0.50 0.85 12.84 0.30

### Total 0.95 4.94 0.33 0.89 6.48 0.35

are a few buggy solutions for Copilot and for student so- In general, the diversity of correct and buggy submislutions involving syntax errors that cannot be converted sions for students is more than Copilot. While there is no
intoAST(3solutions). Weconsiderthemasnon-duplicate guarantee that all non-duplicate solutions are optimized,
buggy solutions. students solved these 5 tasks with more diverse and novel
Figure 10 shows the cumulative distribution of Correct solutions.
(C) solutions, None Duplicate Correct (NDC) solutions,
Buggy (B) solutions, and None Duplicate Buggy (NDB) 4.2.4. The Cyclomatic Complexity of Codes
solutions by Copilot and students across different tasks. Inthissection,wecalculatetheCyclomaticComplexity
In this figure, for example, in “q3: atp3”, the number (C.C.) of codes generated by Copilot and students. Table 6
of Correct (C) solutions suggested by Copilot is 17 but shows the average and the standard deviation of C.C. for
the number of Non-duplicate Correct (NDC) solutions is the correct solutions generated by Copilot and students.
only 2. This means that after generating more solutions It is worth mentioning that we use the sampling method
and running more attempts, Copilot repeats these 2 cor- explained in Subsection 3.2.3 to collect students’ correct
rect solutions several times. However, out of 14 Correct solutions.
(C) solutions generated by students in the third attempt On average, the correct solutions suggested by Copilot
(atp3), 13 solutions are non-duplicate. That is the same are found to be more optimized than students’ solutions.
observation for buggy solutions. Increasing the number However, we should consider that for example, for “q2”,
of attempts on Copilot leads to a jump in the number of Copilot has no correct solutions, or the CR of Copilot
correct solutions for “’q1” and “q5” from 2 to 18 and 7 to for “q4” is only 8%. In general, Copilot recommends less
38 respectively. However, for “q3” and “q4”, this growth complex solutions than students for the same questions
is smaller. The number of None Duplicate Correct (NDC) exceptfor“q1”. But,for“q1”,theC.C.ofCopilot’scorrect
solutions of Copilot is less than or equal to the number of solutions have a lower standard deviation. It means that
Correct (C) solutions in each attempt for each task. This its C.C. is less spread around the average. Also, for “q5”,
is the same story for Buggy solutions. However, it shows CopilotusedPythonbuilt-infunctions“Sort”and“Sorted”,
that despite Copilot’s claims that it removes the duplicate however, it was asked in the description to not use them.
solutions, there are still duplicates in the Top 10 solutions
of each attempt. Table 6: The Cyclomatic Complexity (C.C.) of Copilot’s solutions
comparetostudents’submissions
The difference between C and NDC in student submissions is less than Copilot. For example, in “q3”, the

### Question C.C. Copilot C.C. Students

cumulative number of C solutions generated by Copilot in
q1 SequentialSearch 5.8±1.94 4.63±2.1
different attempts is greater than students’ submissions in
q2 uniquedatesMonths - 4.18±1.03
different samplesets. However, it is the opposite for NDC q3 DuplicateElimination 3±0.01 3.12±0.5
solutions. In “atp5” the cumulative number of C solutions q4 SortingTuples 1±0 4.13±1.03
generated by Copilot equals 28 and it equals 22 after the q5 Top kElements 1.44±0.69 3.3±1.46
5 sampleset on students’ submissions. However, the cu- Total 2.81 3.87
mulative NDC solutions at these attempts equal 2 (out of
28) for Copilot and it equals 21 (out of 22) for students. As already observed, we can conclude, the suggestions
It shows more diversity between correct and even buggy of Copilot can compete with students’ solutions in C.C.
submissions of students compare to Copilot’s solutions.
As another example for Copilot, there is no more NDC 4.2.5. Syntactic Mastery
solutionafter“atp3”for“q3”and“q5”. Thismeansthatby As discussed in Subsection 3.2.4/(5), different developincreasingthenumberofsolutionsgeneratedbyCopilotfor ers can solve a programming task with different solutions.
thesetwoquestions,theCRincreasesduetotheduplication Consequently, this can impact the readability and mainof correct solutions not generating new ones. tainability of the code if it is not an efficient solution.
21

<!-- Page 22 -->

Figure10: The cumulative distribution of solutions by Copilot and students. ItshowsthecumulativedistributionofCorrect(C),
Non-duplicateCorrect(NDC),Buggy(B),andNon-duplicateBuggy(NDB)solutionsforCopilotandstudents. Attempts(atp)forstudents
equaltoarandomsamplesetoftheirsubmission. Eachvalueonthestackrepresentsthenumberofsolutionsineachofthe4categories. The
growthofNDCsolutionsforCopilot’ssolutionsdecreasesorstopsforsomeprogrammingtaskswhilethenumberofitsCorrect(C)solutions
increases. Students’submissionsaremorediversethanCopilot’ssolutions.
In this section, we compare the diversity of syntax Subsection 4.2.3, or it could be the result of restriction in
keywords and the usage of built-in functions between the some assignments’ descriptions, for example in q5: Top k
solutionsgeneratedbyCopilotandthosewrittenbyhumans elements that not using the built-in functions sort and
for different programming tasks. Figure 11 shows the sorted is requested which, unlike the students, Copilot was
diversityofsyntaxkeywordsandbuilt-insthatweobserved not able to understand this restriction.
in both Copilot’s and students’ solutions with normalized

### Findings: In general, Copilot suggests solutions

values. Students used more diverse keywords and built-ins
thatcompetewithstudents’submissionsindifferent
in comparison to Copilot.
aspects. The correct ratio and diversity of students’
For example, for q3: Duplicate Elimination, the only
submissions are greater than Copilot’s. However,
Python built-in function in Copilot’s solutions is ”append”.
the cost of repairing buggy solutions generated by
However, students included more diverse built-ins such

### Copilot is less than students’. In addition, the

as {’count’, ’remove’, ’index’, ’copy’, ’append’, ’reverse’,
complexity of Copilot’s generated codes is less than
’pop’} in their solutions. As another example, in q5: Topstudents’.
k elements, Copilot used {’sort’, ’append’, ’remove’} as

### Challenges: Copilot has difficulty understanding

built-in functions in all of its solutions but students used
some requirements in the description of tasks. This
{’copy’, ’pop’, ’remove’, ’append’, ’sort’, ’extend’, ’reverse’,
affects the correct ratio of its solutions. However,
’clear’}. The using of programming keywords by Copilot
studentsunderstandthosedetailsandconsiderthem
and students is similar to built-ins. For example, for q4:
in their submissions.

### Sorting Tuples, there are solutions provided by students

that iterate over the list of tuples to sort them causing
diverse syntax patterns in their solutions such as {’Tuple’,
’Lt’,’Add’,’Expr’,’Continue’,’Eq’,’Break’,’Gt’,’BoolOp’,

## Discussion and Limitation

’And’, ’UnaryOp’, ’USub’, ’LtE’}. We cannot find these
programmingpatternsinCopilot’ssolutionsasitonlyused In this section, we discuss the boundaries of Copilot
the built-in function ”sort” in the majority of its solutions. and how to make it more beneficial in real programming
Students used more diverse syntax patterns and built- tasks despite its limitations.
ins to solve the same problem compared to Copilot. This
may be the result of students not being familiar with ad- 5.1. Description of Problems (Prompts)
vanced Python features as opposed to Copilot which uses

### Our results show that Copilot cannot understand some

suchfeaturesfrequently. However,thisdiversitycouldstem
details in the description of problems that are understandfrom the diversity of student submissions as discussed in
able by humans. For example, in q5, “Top-k Elements”, it
22

<!-- Page 23 -->

Figure11: R2-2: Diversity of programming Syntax Patterns in Solutions generated by Copilot and Students. Plot(a)shows
thenormalizedvalueforthedistinctnumberofPythonbuilt-infunctionsinCopilot’ssolutionscomparedtostudents’fordifferentquestions.
Plot(b)showsthenormalizedvalueforthedistinctnumberofPythonSyntaxkeywordsinCopilot’ssolutionscomparedtostudents.
is asked in the description to “... not use Python’s built-in we observed that Copilot might misunderstand the probfunctions sort and sorted ...”. Copilot cannot understand lem entirely if the description contains multiple sentences
this detail and uses these two built-in functions in all of (whether short or long).
the correct solutions. However, the majority of students
avoided using these built-in functions. Instead, they wrote 5.2. Experimental Suggestions
a sorting algorithm and then called it for sorting tasks Furthermore, for more exploration on how to change
or used other built-in functions such as “append”, “re- prompt to meet the target solution, we performed some
move” and “max” in their solutions. As our results in experiments by applying different scenarios and discussing
Subsection 4.1 show, Copilot suggests correct solutions for their impacts on the results.
different sorting algorithms (meaning that Copilot is famil- Scenario#1: In this scenario, we changed “...older
iar with different sorting algorithms such as “Bubble Sort” people are at the front...” to “...descending order...” in the
or “Merge Sort”), but it did not use them in q5 because it description of q4 and repeated the process with Copilot
could not figure out the requirements of the problem. But to generate solutions. This small change improves the CR
studentsapplytheirknowledgeaboutsortingalgorithmsto from 14% to 79%. This improvement shows there are some
solve this problem. Thus, since in the prompt, we cannot details/keywords in the description of problems that seem
limit Copilot to NOT using certain functions, instead, it is obvious to humans, but Copilot cannot understand those
better to clarify our task by defining functions that it is details in natural language. If we change those details into
allowed to use. programmingspecific/technicalkeywordssuchas“descend-
In q4, “Sorting Tuple”, it is asked to return the list ing”, it can help Copilot recommend relevant solutions.
of tuples in an order that “... older people are at the
front ...”. Copilot cannot understand this part. In 92% Scenario#2: We have a similar observation for q2,
of suggestions, it returned the sorted tuples in the default “Unique Birthday”, where the Copilot cannot understand
order: ascending. However, students considered this point therequirementsmentionedinthedescription,however,all
in their submission. We even checked some of the buggy studentsconsideredit. Inthisquestion,itisaskedfor“...imsubmissions by students. Our observations show that even plement 3 different functions unique day, unique month
in buggy submission, students considered the correct order and contains unique day...”, to address the problem. Copiof sorting. It means that they fully understood what the lot could not understand this condition. Unit tests for q2
point of sorting tuples is in a way that “...older people are are testing all 3 functions. Thus, the CR of Copilot for q2
at the front...”. equals zero because all 50 solutions in different attempts
Copilot shows similar limitations on algorithmic prob- have failed on some of the test units.
lems. For example, when asking Copilot to implement the So, in this scenario, we gave 3 separate descriptions to
“activity” class in Subsection 4.1.4, Copilot cannot under- Copilotforunique day,unique month,andcontains unique
stand putting limits on variables even though it was asked day functions in the same source file. Here is the revised
to do so explicitly. Another limitation is its difficulties in description that we used:
understanding long descriptions which are also observed
by [31]. Throughout our testing in Subsections 4.1 and 4.2, • unique day: Given a day and a list of possible
23

<!-- Page 24 -->

birthdaydatesreturnTrueifthereisonlyonepossible shows that none of them assumed any wrong structure for
birthday with that day, and False otherwise. the input data, while the structure of input is not clear
in the description of the question. Thus, we assume that
• unique month: Given a month and a list of possithere is some extra clarification between students and the
ble birthday dates, return True if there is only one
lecturer about the structure of the input.
possible birthday within that month, and False otherwise.

## Threats to Validity

• contains unique day: Given a month and a list of
possible birthday dates, return True if there is only We now discuss the threats to the validity of our study
one possible birthday with that month and day, and following the guidelines provided by Wohlin [54] for exper-
False otherwise. imentation in software engineering.
We start with the description of unique day at the first 6.1. Internal Validity
line of the source file. Then, we accepted the first solution
The threat to internal validity comes from the fact that
suggested by Copilot. We continued with the description
Copilot is closed-source. We cannot analyze our results
of unique month in the next line and accepted the first
based on the characteristics (and expected behavior) of
suggested solution and followed the same instruction for
Copilot’s trained model. This is also the case for Copilot’s
contains unique day. We repeat the process 50 times to
training data, hence we are not able to indicate whether it
generate 50 solutions that contain 3 separate functions.
memorizedthesolutionstotheseinquiriesfromitstraining
Copilot even calls the unique day function in some of its
set or whether it generates a unique solution. Similar to
suggestions for the contains unique day function. You can
other researchers [38, 29, 51, 8], we can only investigate
findsamplesolutionsinthereplicationpackage. Sincethere

### Copilot’s functionality in suggesting code for the provided

are separate unit tests to test each function separately, we
prompt.
runrelatedtestsagainsteachfunction. Inthisscenario,the

### Also, as our experiments have shown, Copilot’s sug-


### CR of unique day, unique month, and contains unique day

gestions change over time and are not always consistent.
are 88%, 0%, and 40% respectively.
This may come from the inconsistency stemming from the
While the original description was clear to students,
nature of LLMs and also the continuous improvement of
Copilot could not understand it. Instead of asking Copilot

### Copilot’s engine as an ML product, perhaps by feeding

to solve the problem with different functions, we divide a
new code samples or learning from new queries submitted
problem into 3 different problems. It increases the CR for
to Copilot. As a result, we cannot guarantee that other
unique day and contains unique day. However, the CR of
researchers will receive the same suggestions and results
unique month is still zero. In the following, we investigate
that we obtained by performing the same experiments.
this case with a different scenario.

### External Validity


### Scenario#3: Since Copilot could not find any cor-


### The lack of a dataset that comes from an industrial

rect solutions for unique month, we manually checked its
context and contains programming task statements along
suggested solutions. We found that in all buggy solutions,
with their corresponding codes drives us to follow the path
Copilot refers to the second item of the “birthday” tuple
of other research in software engineering using classical
in the list of birthday dates as the month. However, unit
programming tasks to study Copilot’s competence [51, 47,
tests consider month as the first item of tuples to test the
38, 16, 49]. There are different advantages to these types
functionality of the method. For example, consider below
of programming tasks that we discussed in Subsections 3.1
unit test:
and 3.2.1. To highlight two advantages, first, Copilot is
• unique month (Month = “January”, Birthdays = able to generate answers corresponding to these task de-
[( “January”,“1” ), ( “January”, “2” )]). scriptions. Thus, we could apply our assessments beyond
the correctness of the suggested solutions. Also, the task
Ineachtupleinthelistofbirthdays,forexample,(“Jan- descriptions in our datasets are human-written and it deuary”,“1”), Copilotreferredtotheseconditemasamonth, creases the possibility of the memorization issue in LLMs.
however, the first item in the tuple is the birthday month. But these programming tasks are not representative of the
In the description of “unique month”, we added the whole programming tasks in real software projects.
aboveunittestasasampleinput,attheendofthedescrip- Considering the choice of programming tasks and to
tion. It improves the CR of “unique month” from 0% to haveafaircomparison,wecomparedCopilotwithstudents
91%. Itshowsthataddingsampleinputorsampleunittest in a Python programming course. While we have no inin the description of problems can help Copilot to generate formation about the background and characteristics of the
more correct solutions. participants, we assume that they are good representatives
In addition, we randomly checked 20% of students’ of junior developers inreal software projects, but they may
submissions (both correct and buggy). Our observation not be representatives of the whole population.
24

<!-- Page 25 -->


### Conclusion Validity inimprovingtheirprogrammingskills. Therefore,asfuture

Tomitigatethethreatstothevalidityofourconclusions, work, a tool or a layer on top of Copilot that can filter out
we choose different quantitative metrics, based on other buggy and non-optimal suggestions will reduce the liabilstudies in software engineering, to compare Copilot’s codes ity of using this tool in software projects. Future works
with humans’ [19, 38, 30]. Even though these quantitative can also use our study design and explore more diverse
metricsreducethechanceofhavingbiasedconclusions,they programming tasks with heterogeneous participants in a
do not enable us to conduct any qualitative assessment human-centered study, to more comprehensively compare
such as how humans interact with the tool. Copilot with humans as an AI pair programmer.

### Construct Validity References


### The threat to the construct validity of our study stems

[1] U. Z. Ahmed, N. Srivastava, R. Sindhgatta, and A. Karkare.
from the fact that all the features and capacities of a
Characterizing the pedagogical benefits of adaptive feedback
good AI pair programmer cannot be captured by quantiforcompilationerrorsbynoviceprogrammers. InProceedings
tative metrics. Since pair programming is an interaction of the ACM/IEEE 42nd International Conference on Software
between human-human or human-tool, the opinion of hu- Engineering: Software Engineering Education and Training,
pages139–150,2020.
mans about their experience in using such tools as an AI
[2] R.Alur,R.Bodik,G.Juniwal,M.M.Martin,M.Raghothaman,
pairprogrammerisalsorequiredforacomprehensivestudy. S. A. Seshia, R. Singh, A. Solar-Lezama, E. Torlak, and
For example, someone may prefer a pair programming tool A.Udupa. Syntax-guided synthesis. IEEE,2013.
that accepts voice commands to a tool that suggests a list [3] A. Arcuri. On the automation of fixing software bugs. In

### Companion of the 30th international conference on Software

of possible solutions because they like the discussion part
engineering,pages1003–1006,2008.
of pair programming more than seeing a list of suggestions. [4] O.Asare,M.Nagappan,andN.Asokan. Isgithub’scopilotas
bad as humans at introducing vulnerabilities in code? arXiv
preprint arXiv:2204.04741,2022.

## Conclusion [5] R.K.BeraandR.K.Bera. Fundamentallimitstocomputing.


### The Amazing World of Quantum Computing, pages 171–206,

In this paper, we have studied Copilot’s ability on code 2020.
[6] T. Brown, B. Mann, N. Ryder, M. Subbiah, J. D. Kaplan,
generation and compared its generated codes with those
P. Dhariwal, A. Neelakantan, P. Shyam, G. Sastry, A. Askell,
of humans. Our results show that Copilot is able to genetal.Languagemodelsarefew-shotlearners.Advancesinneural
erate correct and optimal solutions for some fundamental information processing systems,33:1877–1901,2020.
problems in algorithm design. However, the quality of the [7] N. Carlini, D. Ippolito, M. Jagielski, K. Lee, F. Tramer, and
C. Zhang. Quantifying memorization across neural language
generated codes depends greatly on the conciseness and
models. arXiv preprint arXiv:2202.07646,2022.
depth of the prompt that is provided by the developer. [8] M. Chen, J. Tworek, H. Jun, Q. Yuan, H. P. d. O. Pinto,
Furthermore, our results indicate that Copilot still needs J. Kaplan, H. Edwards, Y. Burda, N. Joseph, G. Brockman,
more development in fully understanding natural language etal. Evaluatinglargelanguagemodelstrainedoncode. arXiv
preprint arXiv:2107.03374,2021.
utterances in order to be able to fill-in the position of a
[9] C. B. Clement, D. Drain, J. Timcheck, A. Svyatkovskiy, and
pair-programmer. Copilot may occasionally be unable to N. Sundaresan. Pymt5: multi-mode translation of natural
generate code that satisfies all the criteria described in the language and python code with transformers. arXiv preprint
prompt, but the generated code can be incorporated with arXiv:2010.03150,2020.
[10] J.Cohen. Acoefficientofagreementfornominalscales. Educalittle to moderate changes to the provided prompt or the
tional and psychological measurement,20(1):37–46,1960.
code. [11] T. H. Cormen, C. E. Leiserson, R. L. Rivest, and C. Stein.
Although, Copilot suggests solutions that are more Introduction to algorithms. MITpress,4thedition,2022.
[12] T. H. Cormen, C. E. Leiserson, and C. S. Ronald L Rivest.
advancedinprogrammingthansolutionsprovidedbyjunior
Introduction to algorithms reviews. https://www.goodreads.
developers,andeventhoughthosesolutionsarecomparable
com/book/show/58064696-introduction-to-algorithms,2022.
to humans’ in correctness, optimality, reproducibility, and [13] C.E.C.DantasandM.A.Maia. Readabilityandunderstandrepairing costs, an expert developer is still required to abilityscoresforsnippetassessment: anexploratorystudy.arXiv
preprint arXiv:2108.09181,2021.
detect and filter its buggy or non-optimal solutions. Thus,
[14] R.M.dosSantosandM.A.Gerosa. Impactsofcodingpractices
Copilot can be an asset in software projects if it is used
onreadability.InProceedingsofthe26thConferenceonProgram
by expert developers as a pair programmer but it can turn Comprehension,pages277–285,2018.
into a liability if it is used by those who are not familiar [15] R. Drechsler, I. G. Harris, and R. Wille. Generating formal
systemmodelsfromnaturallanguagedescriptions.In2012IEEE
with the problem context and correct coding methods.
International High Level Design Validation and Test Workshop
Given that Copilot has recently been released as a (HLDVT),pages164–165.IEEE,2012.
commercial product, a new wave of developers will have [16] I. Drori and N. Verma. Solving linear algebra by program
access to it. This will undoubtedly enrich Copilot’s train- synthesis. arXiv preprint arXiv:2111.08171,2021.
[17] C. Ebert, J. Cain, G. Antoniol, S. Counsell, and P. Laplante.
ing dataset and will also expose more of its shortcomings.
Cyclomaticcomplexity. IEEE software,33(6):27–29,2016.
However, Copilot solutions can be troublesome if novice [18] M. et al. Replication package. https://github.com/
developers/students fully trust them, on the other hand, Copilot-Eval-Replication-Package/CopilotEvaluation,
we hypothesize that Copilot’s suggestions may help them 2022.
25

<!-- Page 26 -->

[19] S.Fakhoury,D.Roy,A.Hassan,andV.Arnaoudova. Improv- potentialofartificialintelligenceasamethodofsoftwaredeveling source code readability: Theory and practice. In 2019 oper’sproductivityimprovement.In2022ConferenceofRussian
IEEE/ACM 27th International Conference on Program Com- Young Researchers in Electrical and Electronic Engineering (Elprehension (ICPC),pages2–12.IEEE,2019. ConRus),pages386–390.IEEE,2022.
[20] Z.Feng,D.Guo,D.Tang,N.Duan,X.Feng,M.Gong,L.Shou, [38] N.NguyenandS.Nadi.AnempiricalevaluationofGitHubCopi-
B. Qin, T. Liu, D. Jiang, et al. Codebert: A pre-trained lot’scodesuggestions. InAccepted for publication Proceedings
modelforprogrammingandnaturallanguages. arXiv preprint of the 19th ACM International Conference on Mining Software
arXiv:2002.08155,2020. Repositories (MSR),pages1–5,2022.
[21] J.Finnie-Ansley,P.Denny,B.A.Becker,A.Luxton-Reilly,and [39] K. Papineni, S. Roukos, T. Ward, and W.-J. Zhu. Bleu: a
J.Prather. Therobotsarecoming: Exploringtheimplications method for automatic evaluation of machine translation. In
ofopenaicodexonintroductoryprogramming. InAustralasian Proceedings of the 40th annual meeting of the Association for
Computing Education Conference,pages10–19,2022. Computational Linguistics,pages311–318,2002.
[22] N. Forsgren, M.-A. Storey, C. Maddila, T. Zimmermann, [40] H.Pearce,B.Ahmad,B.Tan,B.Dolan-Gavitt,andR.Karri.
B. Houck, and J. Butler. The space of developer productiv- Asleepatthekeyboard? assessingthesecurityofgithubcopilot’s
ity: There’s more to it than you think. Queue, 19(1):20–48, codecontributions. In2022 2022 IEEE Symposium on Security
2021. andPrivacy(SP)(SP),pages980–994,LosAlamitos,CA,USA,
[23] I. Fronza, A. Sillitti, and G. Succi. An interpretation of the may2022.IEEEComputerSociety. doi: 10.1109/SP46214.2022.
results of the analysis of pair programming during novices in- 00057. URLhttps://doi.ieeecomputersociety.org/10.1109/
tegration in a team. In 2009 3rd International Symposium SP46214.2022.00057.
on Empirical Software Engineering and Measurement, pages [41] L.Plonka,H.Sharp,J.VanderLinden,andY.Dittrich. Knowl-
225–235.IEEE,2009. edgetransferinpairprogramming: Anin-depthanalysis. Inter-
[24] Geeksforgeeks Team. Geeksforgeeks. https://www. national journal of human-computer studies,73:66–78,2015.
geeksforgeeks.org,2022. [42] K. Rahit, R. H. Nabil, and M. H. Huq. Machine translation
[25] S.Gulwani. Dimensionsinprogramsynthesis. InProceedingsof fromnaturallanguagetocodeusinglong-shorttermmemory. In
the 12th International ACM SIGPLAN Symposium on Princi- Proceedings of the Future Technologies Conference,pages56–63.
ples and Practice of Declarative Programming,PPDP’10,page Springer,2019.
13–24,NewYork,NY,USA,2010.AssociationforComputing [43] S.Ren,D.Guo,S.Lu,L.Zhou,S.Liu,D.Tang,N.Sundare-
Machinery.ISBN9781450301329.doi: 10.1145/1836089.1836091. san, M. Zhou, A. Blanco, and S. Ma. Codebleu: a method
URLhttps://doi.org/10.1145/1836089.1836091. for automatic evaluation of code synthesis. arXiv preprint
[26] S.Gulwani,I.Radiˇcek,andF.Zuleger. Automatedclustering arXiv:2009.10297,2020.
andprogramrepairforintroductoryprogrammingassignments. [44] P. Salazar Paredes et al. Comparing Python programs using
ACM SIGPLAN Notices,53(4):465–480,2018. abstractsyntaxtrees. Technicalreport,Uniandes,2020.
[27] C.B.HarrisandI.G.Harris. Glast: Learningformalgrammars [45] M.M.S.Sarwar,S.Shahzad,andI.Ahmad.Cyclomaticcomplextotranslatenaturallanguagespecificationsintohardwareasser- ity: Thenestingproblem.InEighthInternationalConferenceon
tions.In2016Design,Automation&TestinEuropeConference DigitalInformationManagement(ICDIM2013),pages274–279.
& Exhibition (DATE),pages966–971.IEEE,2016. IEEE,2013.
[28] Y.Hu,U.Z.Ahmed,S.Mechtaev,B.Leong,andA.Roychoud- [46] S. Scalabrino, G. Bavota, C. Vendome, M. Linares-Vasquez,
hury.Re-factoringbasedprogramrepairappliedtoprogramming D.Poshyvanyk,andR.Oliveto. Automaticallyassessingcode
assignments. In2019 34th IEEE/ACM International Confer- understandability. IEEE Transactions on Software Engineering,
enceonAutomatedSoftwareEngineering(ASE),pages388–398. 47(3):595–613,2019.
IEEE,2019. [47] D. Sobania, M. Briesch, and F. Rothlauf. Choose your pro-
[29] S. Imai. Is github copilot a substitute for human pair- grammingcopilot: Acomparisonoftheprogramsynthesisperprogramming? an empirical study. In Proceedings of the formance of github copilot and genetic programming. arXiv
ACM/IEEE 44th International Conference on Software En- preprint arXiv:2111.07875,2021.
gineering: Companion Proceedings,pages319–321,2022. [48] D. Sobania, D. Schweim, and F. Rothlauf. Recent develop-
[30] S. Kim and E. J. Whitehead Jr. How long did it take to fix mentsinprogramsynthesiswithevolutionaryalgorithms. arXiv
bugs? In Proceedings of the 2006 international workshop on preprint arXiv:2108.12227,2021.
Mining software repositories,pages173–174,2006. [49] L. Tang, E. Ke, N. Singh, N. Verma, and I. Drori. Solving
[31] Y. Li, D. Choi, J. Chung, N. Kushman, J. Schrittwieser, probabilityandstatisticsproblemsbyprogramsynthesis. arXiv
R. Leblond, T. Eccles, J. Keeling, F. Gimeno, A. D. Lago, preprint arXiv:2111.08267,2021.
etal. Competition-levelcodegenerationwithalphacode. arXiv [50] N.Tran,H.Tran,S.Nguyen,H.Nguyen,andT.Nguyen. Does
preprint arXiv:2203.07814,2022. bleuscoreworkforcodemigration? In2019 IEEE/ACM 27th
[32] K. M. Lui and K. C. Chan. Pair programming productiv- International Conference on Program Comprehension (ICPC),
ity: Novice–novice vs. expert–expert. International Journal pages165–176.IEEE,2019.
of Human-computer studies,64(9):915–925,2006. [51] P.Vaithilingam, T.Zhang, andE.L.Glassman. Expectation
[33] Z.MannaandR.Waldinger. Adeductiveapproachtoprogram vs.experience: Evaluatingtheusabilityofcodegenerationtools
synthesis. ACM Transactions on Programming Languages and poweredbylargelanguagemodels.InCHIConferenceonHuman
Systems (TOPLAS),2(1):90–121,1980. Factors in Computing Systems Extended Abstracts,pages1–7,
[34] L. M. Maruping, X. Zhang, and V. Venkatesh. Role of collec- 2022.
tiveownershipandcodingstandardsincoordinatingexpertise [52] W3schools Team. W3schools. https://www.w3schools.com,
in software project teams. European Journal of Information 2022.
Systems,18(4):355–371,2009. [53] N. Wirth. Algorithms & data structures. Prentice-Hall, Inc.,
[35] R. Mihalcea, H. Liu, and H. Lieberman. Nlp (natural lan- 1985.
guageprocessing)fornlp(naturallanguageprogramming). In [54] C.Wohlin,P.Runeson,M.Ho¨st,M.C.Ohlsson,B.Regnell,and
InternationalConferenceonintelligenttextprocessingandcom- A.Wessl´en. Experimentation in software engineering. Springer
putational linguistics,pages319–330.Springer,2006. Science&BusinessMedia,2012.
[36] A.MoradiDakhel,M.C.Desmarais,andF.Khomh. Assessing [55] F.Zhang,F.Khomh,Y.Zou,andA.E.Hassan. Anempirical
developerexpertisefromthestatisticaldistributionofprogram- studyonfactorsimpactingbugfixingtime.In201219thWorking
mingsyntaxpatterns.InEvaluationandAssessmentinSoftware conference on reverse engineering,pages225–234.IEEE,2012.
Engineering,pages90–99,2021. [56] A.Ziegler,E.Kalliamvakou,S.Simister,G.Sittampalam,A.Li,
[37] E. A. Moroz, V. O. Grizkevich, and I. M. Novozhilov. The A.Rice,D.Rifkin,andE.Aftandilian. Productivityassessment
26

<!-- Page 27 -->

of neural code completion. arXiv preprint arXiv:2205.06537,
2022.
27

## Tables

**Table (Page 5):**

|  | def search(x, seq): for i in range(len(s if x <= seq[i]: return i return len(seq) |  |  |
|---|---|---|---|
|  |  | def search(x, seq): for i in range(len(s if x <= seq[i]: return i return len(seq) |  |
|  |  |  |  |
