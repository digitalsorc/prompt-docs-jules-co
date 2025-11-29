---
title: "Optimal Decision Making Data Composition"
original_file: "./Optimal_Decision_Making_Data_Composition.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["rag", "agents", "fine-tuning", "evaluation"]
keywords: ["cid", "algorithm", "problem", "time", "data", "car", "behavior", "optimal", "agent", "results"]
summary: "<!-- Page 1 -->

Optimal Decision-Making for Autonomous Agents via Data Composition
E´miland Garrabe´, Martina Lamberti and Giovanni Russo∗

### Abstract

Weconsidertheproblemofdesigningagentsabletocomputeoptimaldecisionsbycomposingdatafrommultiplesourcesto
tackletasksinvolving:(i)trackingadesiredbehaviorwhileminimizinganagent-specificcost;(ii)satisfyingsafetyconstraints. After formulating the control problem, we show that this is convex under a suitable assumption and find the optimal solution."
related_documents: []
---

# Optimal Decision Making Data Composition

<!-- Page 1 -->

Optimal Decision-Making for Autonomous Agents via Data Composition
E´miland Garrabe´, Martina Lamberti and Giovanni Russo∗

### Abstract

Weconsidertheproblemofdesigningagentsabletocomputeoptimaldecisionsbycomposingdatafrommultiplesourcesto
tackletasksinvolving:(i)trackingadesiredbehaviorwhileminimizinganagent-specificcost;(ii)satisfyingsafetyconstraints.
After formulating the control problem, we show that this is convex under a suitable assumption and find the optimal solution.
Theeffectivenessoftheresults,whichareturnedinanalgorithm,isillustratedonaconnectedcarsapplicationviain-silicoand
in-vivoexperimentswithrealvehiclesanddrivers.Alltheexperimentsconfirmourtheoreticalpredictionsandthedeployment
of the algorithm on a real vehicle shows its suitability for in-car operation.

## I. Introduction

We often make decisions by composing knowledge gathered from others [1] and a challenge transversal to control and
learningistodevisemechanismsallowingautonomousdecision-makerstoemulatetheseabilities.Systemsbasedonsharing
data [2] are examples where agents need to make decisions based on some form of crowdsourcing [3]. Similar mechanisms
can also be useful for the data-driven control paradigm when e.g., one needs to re-use policies synthesized on plants for
which data are available to solve a control task on a new plant, for which data are scarcely available [3]–[5].
Motivated by this, we consider the problem of designing decision-making mechanisms that enable autonomous agents to
compute optimal decisions by composing information from third parties to solve tasks that involve: (i) tracking a desired
behavior while minimizing an agent-specific cost; (ii) satisfying safety constraints. Our results enable computation of the
optimal behavior and are turned into an algorithm. This is experimentally validated on a connected car application.
Related works: we briefly survey a number of works related to the results and methodological framework of this paper.
The design of context-aware switches between multiple datasets for autonomous agents has been recently considered in
[3], [4], where the design problem, formalized as a data-driven control (DDC) problem, did not take into account safety
requirements. Results in DDC include [6]–[8], which take a behavioral systems perspective, [9], which finds data-driven
formulas towards a model-free theory of geometric control. We also recall e.g., [10]–[12] for results inspired from MPC,
[5] that considers data-driven control policies transfer and [13] that tackles he problem of computing data-driven minimumenergy control for linear systems. In our control problem (see Section III) we formalize the tracking of a given behavior
via Kullback-Leibler (KL) divergence minimization and we refer to e.g., [14], [15] for examples across learning and control
that involve minimizing this functional. Further, the study of mechanisms enabling agents to re-use data, also arises in the
design of prediction algorithms from experts [16] and of learning algorithms from multiple simulators [17]. In a yet broader
context, studies in neuroscience [18] hint that our neocortex might implement a mechanism composing the output of the
cortical columns and this might be the basis of our ability to re-use knowledge.
Contributions: we consider the problem of designing agents that dynamically combine data from heterogeneous sources
to fulfill tasks that involve tracking a target behavior while optimizing a cost and satisfying safety requirements expressed
as box constraints. By leveraging a probabilistic framework, we formulate a data-driven optimal control problem and, for
this problem, we: (i) prove convexity under a suitable condition; (ii) find the optimal solution; (iii) turn our results into an
algorithm, using it to design an intelligent parking system for connected vehicles. Validations are performed both in-silico
and in-vivo, with real cars. As such, the main purpose of this paper is twofold: (i) we introduce, and rigorously characterize
ouralgorithm;(ii)proposeastand-aloneimplementationofourresults,suitableforin-vivoexperimentsonrealcars.In-vivo
validationswereperformedviaanhardware-in-the-loopplatformallowingtoembedrealcars/driversintheexperiments.Using
the platform, we deploy our algorithm on a real vehicle showing its suitability for in-car operation. All experiments confirm
the effectiveness of our approach (documented code/data for our simulations at https://tinyurl.com/3ep4pknh).
While our results are inspired by the ones in [3], [4], our paper extends these in several ways. First, the results in [3],
[4] cannot consider box constraints and hence cannot tackle the control problem of this paper. Second, even when there are
no box constraints, the results in [3], [4] only solve an approximate version of the problem considered here. That is, the
results from [3], [4] only find an approximate, non-optimal, solution of the problem considered here. As we shall see, this
means that the solutions from [3], [4] cannot get a better cost than the one obtained with the results of this paper. Third,
the algorithm obtained from the results in this paper is deployed, and validated, on a real car and this was not done in [3],
[4]. The in-vivo implementation is novel.
∗ emails:{egarrabe,giovarusso}@unisa.it,martinalamberti3@gmail.com.E.Garrabe´ andG.RussowiththeDIEMatthe
UniversityofSalerno,84084,Salerno,Italy.
3202
yaM
22
]CO.htam[
2v51331.3032:viXra

<!-- Page 2 -->

Notation: sets are in calligraphic and vectors in bold. Given the measurable space (X,F ), with X ⊆Rd (X ⊆Zd) and
x
F being a σ-algebra on X, a random variable on (X,F ) is denoted by X and its realization by x. The probability density
x x
(resp. mass) function or pdf (pmf) of a continuous (discrete) X is denoted by p(x). The convex subset of such probability
functions (pfs) is D. The expectation of a function h(·) of the continuous variable X is E [h(X)]:= (cid:82) h(x)p(x)dx, where
p
the integral (in the sense of Lebesgue) is over the support of p(x), which we denote by S(p). The joint pf of X , X is
1 2
p(x ,x ) and the conditional pf of X given X is p(x |x ). Countable sets are denoted by {w } , where w is the
1 2 1 2 1 2 k k1:kn k
generic element of the set and k : k is the closed set of consecutive integers between k and k . The KL divergence
1 n 1 n
(cid:82)
between p(x) and q(x), where p is absolutely continuous w.r.t. q, is D (p||q):= p ln(p/q) dx: it is non-negative

### KL S(p)

and 0 if and only if p(x)=q(x). In the expressions for the expectation and KL divergence, the integral is replaced by the
sum if the variables are discrete. Finally: (i) we let 1 (x) denote the indicator function being equal to 1 if x∈A⊆X and

## A

0 otherwise; (ii) set exclusion is instead denoted by \.

## Ii. Thesetup

Theagentseekstocraftitsbehaviorbycombininganumberofsourcestofulfillataskthatinvolvestrackingatarget/desired
behavior while maximizing an agent-specific reward over the time horizon T := 0 : T, T > 0. The agent’s state at time
(cid:81)
step k ∈ T is x ∈ X and the target behavior that the agent seeks to track is p := p (x ) p(x | x ). As in
k 0:T 0 0 k∈1:T k k−1
[3], [4], we design the behavior of the agent by designing its joint pf π :=π(x ,...,x ) and we have:

## 0:T 0 T

(cid:89)
π =π (x ) π(x |x ). (1)
0:T 0 0 k k−1
k∈1:T
That is, the behavior of the agent can be designed via the pfs π(x |x ), i.e., the transition probabilities. To do so, the
k k−1
agent has access to S sources and we denote by π(i)(x |x ), with support S(π)⊆X, the behavior made available by
k k−1
source i, i∈S :=1:S, at k−1. We also let r (x ) be the agent’s reward for being in state x at k.
k k k

## Iii. Formulationofthecontrolproblem

Let α(1),...,α(S) be weights and α be their stack. Then, the control problem we consider can be formalized as:
k k k
Problem 1: find the sequence {α∗} solving
k 1:T

## T

(cid:88)
min D (π ||p )− E [r˜ (X )]
{αk}

## 1:T


## Kl 0:T 0:T

k=1
π(xk−1) k k−1
s.t. E [1 (x )]≥1−(cid:15) , ∀k,
π(xk|xk−1) Xk k k
π(x |x )= (cid:88) α(i)π(i)(x |x ), ∀k,
k k−1 k k k−1
i∈S
(cid:88) α(i) =1, α(i) ∈[0,1], ∀k.
k k
i∈S
In Problem 1, r˜ (x ):=E [r (X )] and we note that E [r˜ (X )]=E [r (X )] is the expected
k k−1 π(xk|xk−1) k k π(xk−1) k k−1 π(xk) k k
reward for the agent when the behavior in (1) is followed. The problem is a finite-horizon optimal control problem with the
α ’s as decision variables. As we shall see, these are generated as feedback from the agent state (Section IV). We say that
k
{π∗(x |x )} , with π∗(x |x )= (cid:80) α(i),∗π(i)(x |x ), is the optimal behavior for the agent, obtained by
k k−1 1:T k k−1 i∈S k k k−1
linearlycombiningthesourcesviatheα∗’s.Intheproblem,thecostformalizesthefactthattheagentseekstomaximizeits
k
reward,whiletracking(intheKLdivergencesense)thetargetbehavior.MinimizingtheKLtermamountsatminimizingthe
discrepancy between π and p . This term can also be thought as a divergence regularizer and, when p is uniform,

## 0:T 0:T 0:T

it becomes an entropic regularizer. The second and third constraints formalize the fact that, at each k, π∗(x |x )∈D
k k−1
and that this is a convex combination of the pfs from the sources. The first constraint is a box constraint and models the
fact that the probability that the agent behavior is, at each k, inside some (e.g., safety) measurable set X ⊆ X is greater
k
than some (cid:15) ≥0. We now make the following
k
Assumption 1: the optimal cost of Problem 1 is bounded.
(cid:16) (cid:17)
Remark 1: thecostinProblem1canberecastasD (π ||p˜ ),wherep˜ ∝p exp
(cid:80)T
r (x ) .Thismeans

### KL 0:T 0:T 0:T 0:T k=1 k k

thatAssumption1issatisfiedwheneverthereexistssomeπ˜ thatisfeasibleforProblem1andthatisabsolutelycontinuous

## 0:T

w.r.t. p˜ . See also Remark 3.

## 0:T


## Iv. Mainresults

WeproposeanalgorithmtotackleProblem1.ThealgorithmtakesasinputT,thetargetbehavior,thereward,thebehaviors
of the sources and the box constraints of Problem 1 (if any). Given the inputs, it returns the optimal behavior for the agent.

<!-- Page 3 -->

The key steps of the algorithm are given as pseudo-code in Algorithm 1. An agent that follows Algorithm 1 computes
{α } via backward recursion (lines 4−9). At each k, the α ’s are obtained as the minimizers of
k 1:N k
min c (π(x |x ))
k k k−1
αk
s.t. E [1 (x )]≥1−(cid:15)
π(xk|xk−1) Xk k k
π(x |x )= (cid:88) α(i)π(i)(x |x ) (2)
k k−1 k k k−1
i∈S
(cid:88) α(i) =1, α(i) ∈[0,1],
k k
i∈S
where
c (π(x |x )):=D (π(x |x )||p(x |x ))
k k k−1 KL k k−1 k k−1
(3)
−E [r¯ (X )],
π(xk|xk−1) k k
with r¯ (·) iteratively built within the recursion (lines 5, 8). The weights are used (line 7) to compute π∗(x |x ).
k k k−1
Remark 2: results are stated for continuous variables (proofs for discrete variables omitted for brevity). Note that integrals/summations in the cost are over S(π).
Remark 3: followingRemark1,theoptimalcostoftheproblemin(2)isboundedifthereexistssomefeasibleπ˜(x |x )
k k−1
that is absolutely continuous w.r.t. p˜(x |x )∝p(x |x )exp(r¯ (x )). From the design viewpoint, this can satisfied
k k−1 k k−1 k k
if it holds for at least one π(i)(x |x ).
k k−1

### Finally, we make the following

Assumption 2: ∀i ∈ S and ∀x ∈ X, there exist some constants, say m and M, with 0 < m ≤ M < +∞, such that
k−1
m≤π(i)(x |x )≤M, ∀x ∈S(π).
k k−1 k
Remark 4: Assumption 1 is satisfied for e.g., Gaussian distributions. As we shall see (Section V) the assumption can be
fulfilled by injecting noise in the data.

### A. Properties of Algorithm 1

Before characterizing convexity of the problems recursively solved in Algorithm 1 and optimality, we give a condition
ensuring feasibility of the problem in (2).
Lemma 1: the problem in (2) is feasible if and only if there exists at least one source, say π(j)(x | x ), such that
k k−1
E [1 (x )]≥1−(cid:15) .
π(j) P (x r k o | o x f k : −1 th ) ei X fp k art k clearlyhold k s.Fortheonlyifpartweprovethatifproblem(2)isinfeasible,thenmax E [1 (x )]<
i π(i)(xk|xk−1) Xk k
1−(cid:15) . In fact, if the problem is infeasible, then for all α such that (cid:80) α(i) =1 and α(i) ∈[0,1] it must hold that
k k i∈S k k
(cid:90)
(cid:88) α(i)π(i)(x |x )dx <1−(cid:15) .
k k k−1 k k

### Xk i∈S

Note that this must also hold for all α such that (cid:80) α(i) =1 and α(i) ∈{0,1}, as these are contained in the set of
k i∈S k k
real-valued α ’s. We conclude the proof by noticing that, if α is such that α(i) =0∀i(cid:54)=j and α(j) =1, then
k k k k
(cid:90) (cid:90)
(cid:88) α(i)π(i)(x |x )dx = π(j)(x |x )dx
k k k−1 k k k−1 k

### Xk i∈S Xk

=E [1 (x )].
π(j)(xk|xk−1) Xk k

### Algorithm 1 Pseudo-code

1: Input: time horizon T, target behavior p 0:T , reward r k (·), sources π(i)(x k |x k−1 ), box constraints (optional)
2: Output: optimal agent behavior {π∗(x k |x k−1 )} 1:T
3: rˆ T (x T )←0
4: for k =T :1 do
5: r¯ k (x k )←r k (x k )−rˆ k (x k )
6: α∗ k (x k−1 )←minimizer of the problem in (2);
7: π∗(x k |x k−1 )← (cid:80) i∈S α( k i),∗(x k−1 )π(i)(x k |x k−1 )
8: rˆ k−1 (x k−1 )←c k (π∗(x k |x k−1 ))
9: end for

<!-- Page 4 -->

It then follows that, ∀j,
E [1 (x )]<1−(cid:15) .
π(j)(xk|xk−1) Xk k k

### Convexity: we are now ready to prove the following

Proposition 1: let Assumption 2 hold. Then, the problem in (2) is convex.
Proof: Clearly, the second and third constraint in the problem are convex. For the first constraint, we get
(cid:90)
E [1 (x )]= π(x |x )1 (x )dx
π(xk|xk−1) Xk k k k−1 Xk k k
(cid:90)
= (cid:88) α(i)π(i)(x |x )dx
k k k−1 k

### Xk i∈S

(cid:90)
= (cid:88) α(i) π(i)(x |x )dx ,
k k k−1 k
i∈S Xk
which is therefore convex in the decision variables.
Now,weshowthatthecostisalsoconvexinthesevariablesandwedosobyexplicitlycomputing,foreachx ,itsHessian,
k−1
say H(x ). Specifically, after embedding the second constraint of the problem in (2) in the cost and differentiating with
k−1
respect to the decision variables we get, for each j ∈S:
∂c k := ∂ (cid:90) (cid:88) α(i)π(i)(x |x ) (cid:32) log (cid:32)(cid:80) i∈S α k (i)π(i)(x k |x k−1 ) (cid:33) −r¯ (x ) (cid:33) dx
∂α
k
(j) ∂α
k
(j) S(π)i∈S k k k−1 p(x k |x k−1 ) k k k
= (cid:90) ∂ (cid:88) α(i)π(i)(x |x ) (cid:32) log (cid:32)(cid:80) i∈S α k (i)π(i)(x k |x k−1 ) (cid:33) −r¯ (x ) (cid:33) dx
S(π) ∂α k (j) i∈S k k k−1 p(x k |x k−1 ) k k k
(cid:32) (cid:32) (cid:33) (cid:33)
(cid:90)
= π(j)(x |x ) log (cid:88) α(i)π(i)(x |x ) −log(p(x |x ))−r¯ (x )+1 dx .
k k−1 k k k−1 k k−1 k k k

### S(π) i∈S

The above chain of identities was obtained by swapping integration and differentiation, leveraging the fact that the cost is
smooth in the decision variables. Similarly, we get
(cid:32) (cid:32) (cid:33) (cid:33)
∂2c k = ∂ (cid:90) π(j)(x |x ) log (cid:88) α(i)π(i)(x |x ) −log(p(x |x ))−r¯ (x )+1 dx
∂α k (j)2 ∂α k (j) S(π) k k−1 i∈S k k k−1 k k−1 k k k
(cid:90) π(j)(x |x )2
= k k−1 dx
S(π) (cid:80) i∈S α k (i)π(i)(x k |x k−1 ) k
=:h (x ),
jj k−1
and, for each m(cid:54)=j, m∈S,
∂2c (cid:90) π(j)(x |x )π(m)(x |x )
k = k k−1 k k−1 dx =:h (x ).
∂α k (j)∂α k (m) S(π) (cid:80) i∈S α k (i)π(i)(x k |x k−1 ) k jm k−1
Also, following Assumption 2, ∀j,m∈S we have that
(cid:12) (cid:12)
(cid:90) (cid:12)π(j)(x |x )π(m)(x |x )(cid:12) M
(cid:12) k k−1 k k−1 (cid:12)dx ≤
S(π) (cid:12) (cid:12) (cid:80) i∈S α k (i)π(i)(x k |x k−1 ) (cid:12) (cid:12) k m
where we used the third constraint. That is, the above integrals are well defined and thus we can conclude the proof by
computing vTH(x )v for some non-zero v∈RS:
k−1
(cid:88)
vTH(x )v= v v h (x )
k−1 j m jm k−1
j,m
(cid:90)
(cid:88)
= v v a (x ,x )dx
j m jm k k−1 k
j,m S(π)
(cid:90)
(cid:88)
= v v a (x ,x )dx ,
j m jm k k−1 k
S(π) j,m

<!-- Page 5 -->

where the a ’s are the elements of the matrix
jm
 π(1)(x |x ) 
k k−1
A(x ,x ):=π¯(x ,x ) . . · · (cid:2) π(1)(x |x )...π(S)(x |x ) (cid:3) ,
k k−1 k k−1  .  k k−1 k k−1
π(S)(x |x )
k k−1
(cid:16) (cid:17)
with π¯(x ,x ) := 1/ (cid:80) α(i)π(i)(x |x ) . The above expression is indeed positive semi-definite for each x ,
k k−1 i∈S k k k−1 k
x and we can draw the desired conclusion.
k−1

### Optimality: we can now prove the following

Proposition 2: let Assumption 2 and Assumption 1 hold. Then, Algorithm 1 gives an optimal solution for Problem 1.
Proof: the chain rule for the KL divergence and the linearity of expectation imply that the cost can be written as

## T−1

(cid:88)
D (π ||p )− E [r˜ (X )]+E [c (π(x |x ))], (4)
KL 0:T−1 0:T−1 π(xk−1) k k−1 π(xT−1) T T T−1
k=1
where c (π(x |x )) is defined as in (3) with r¯ (x ) given by Algorithm 1 – see lines 3 and 5 and note that, at time

## T T T−1 T T

step T, r¯ (x )=r (x ). To obtain the above expression, the fact that c (π(x |x )) only depends on x was also

## T T T T T T T−1 T−1

used. Hence, Problem 1 can be split into the sum of two sub-problems: a first problem over k ∈0:T −1 and the second
for k =T. For this last time step, the problem can be solved independently on the others and is given by:
min E [c (π(x |x ))]
αT
π(xT−1) T T T−1
s.t. E [1 (x )]≥1−(cid:15) ,
π(xT|xT−1) XT T T
π(x |x )= (cid:88) α(i)π(i)(x |x ), (5)

## T T−1 T T T−1

i∈S
(cid:88) α(i) =1, α(i) ∈[0,1].

## T T

i∈S
Using linearity of the expectation and the fact that the decision variable is independent on π(x ), we have that the

## T−1

minimizer of the problem in (5) is the same as the problem in (2) with k =T. Following Proposition 1, such a problem is
convex and we denote its optimal solution as α∗(x ) – see line 6 of Algorithm 1 – and the optimal cost of the problem,

## T T−1

which is bounded by Assumption 1, is c (π∗(x |x )), where:

## T T T−1

π∗(x |x )= (cid:88) α(i),∗(x )π(i)(x |x ).

## T T−1 T T−1 T T−1

i∈S
This gives rˆ (x ) in Algorithm 1 (lines 7−8), thus yielding the steps for the backward recursion of the Algorithm

## T−1 T−1

1 at time step T. Now, the minimum value of the problem in (5) is given by E [rˆ (X )]. Hence, the cost of
π(xT−1) T−1 T−1
Problem 1 becomes

## T−1

(cid:88)
D (π ||p )− E [r˜ (X )]+E [rˆ (X )].
KL 0:T−1 0:T−1 π(xk−1) k k−1 π(xT−1) T−1 T−1
k=1
Then, following the same reasoning used to obtain (4) and by noticing that

### E [rˆ (X )]=E (cid:2)E [rˆ (X )] (cid:3) ,

π(xT−1) T−1 T−1 π(xT−2) π(xT−1|xT−2) T−1 T−1
we get:

## T−2

(cid:88)

### D (π ||p )− E [r˜ (X )]+E [c (π(x |x ))],

KL 0:T−2 0:T−2 π(xk−1) k k−1 π(xT−2) T−1 T−1 T−2
k=1
where c (π(x | x )) is again given in (3) with r¯ (x ) again defined as in Algorithm 1. By iterating the

## T−1 T−1 T−2 T−1 T−1

arguments above, we find that at each time step Problem 1 can always be split as the sum of two sub-problems, where the
last sub-problem can be solved independently on the previous ones. Moreover, the minimizer of this last sub-problem is

<!-- Page 6 -->

always the solution of a problem of the form
minD (π(x |x )||p(x |x ))−E [r¯ (X )]
αk
KL k k−1 k k−1 π(xk|xk−1) k k
s.t. E [1 (x )]≥1−(cid:15) ,
π(xk|xk−1) Xk k k
π(x |x )= (cid:88) α(i)π(i)(x |x ), (6)
k k−1 k k k−1
i∈S
(cid:88) α(i) =1, α(i) ∈[0,1],
k k
i∈S
where r¯ (x ):=r (x )−rˆ (x ), with rˆ (x ):=c (π∗(x |x )) and π∗(x |x )= (cid:80) α(i),∗(x )π(i)(x |
k k k k k k k k k+1 k+1 k k k−1 i∈S k k−1 k
x ). This yields the desired conclusions.
k−1
Remark 5: the results from [3], [4] solve an approximate version of Problem 1 when there are no box constraints. Hence,
even in this special case, the results from [3], [4] do not lead to the optimal solution found with Algorithm 1. Specifically,
the approximate solution from [3], [4] corresponds to the optimal solution of a problem with additional binary constraints
on the decision variables. As a result, the algorithm from [3], [4] searches solutions in a feasibility domain that is contained
in the feasibility domain of Problem 1. Hence, the solutions found in [3], [4] cannot achieve a better cost than the ones
obtained via Algorithm 1.

## V. Designinganintelligentparkingsystem

We now use Algorithm 1 to design an intelligent parking system for connected cars and validate the results via in-silico
and in-vivo experiments. For the latter set of experiments, Algorithm 1 is deployed on a real car and validation is performed
via an hardware-in-the-loop (HiL) platform inspired from [19]. Before reporting the results, we describe the validation
scenarios and the experimental set-up. Code, maps and parameters with instructions to replicate the simulations are given
at https://tinyurl.com/3ep4pknh.

### A. Validation Scenarios and Experimental Set-up

We consider the problem of routing vehicles in a given geographic area to find parking. In all experiments we consider
a morning rush scenario at the University of Salerno campus (see Figure 1). Specifically, cars arrive to the campus through
a highway exit and, from here, users seek to park in one of the parking locations: Biblioteca and Terminal.
In this context, vehicles are agents equipped with Algorithm 1. The set of road links within the campus is X and time
steps are associated to the time instants when the vehicle changes road link. The state of the agent, x , is the road link
k
occupied by the vehicle at time step k. Given this set-up, at each k Algorithm 1 outputs the turning probability for the
car given the current car link, π∗(x | x ). The next direction for the car is then obtained by sampling from this pf.
k k−1
Fig. 1: campus map. The magnified areas show the obstructed road link (in blue) and links used within the validations. Colors online.

<!-- Page 7 -->

Agents have access to a set of sources, each providing different routes. As discussed in [20], sources might be third parties
navigation services, routes collected from other cars/users participating to some sharing service. Agents wish to track their
target/desired behavior (driving them to the preferred parking – Terminal in our experiments) and the reward depends on the
actual road conditions within the campus. Links adjacent to a parking lot are assigned a constant reward of: (i) 3.8 if the
parking has available spaces; (ii) 0 when it becomes full. Unparked cars already on full parking lots are assigned a target
behavior leading them to another parking. In normal road conditions, the reward for the other links is 0 and becomes −20
when there is an obstruction. In our experiments, the reward was selected heuristically so that it would be: (i) sufficiently
penalizing for links affected by obstruction; (ii) encouraging cars to drive towards parking lots with available spaces. In
the first scenario (Scenario 1) there are no box constraints: this is done to benchmark Algorithm 1 with [3], [4]. To this
aim, we use the campus map from [20] in which [3], [4] were thoroughly validated via simulations. Then, we show that
by introducing box constraints Algorithm 1 can effectively regulate access of vehicles through selected road links. This is
Scenario 2 and we considered three situations: (A) the road towards the Biblioteca parking lot is forbidden. To account
for this, we set in Algorithm 1 X = X \l , where the link l is shown in Figure 1, and (cid:15) = 0.027; (B) the set X as
k 2 2 k k
before but now (cid:15) =0.5; (C) the road towards the Terminal parking lot is forbidden and in this case we set X =X \l ,
k k 1
(cid:15) = 0.027 (see Figure 1 for link l ). For this last scenario, Algorithm 1 is validated both in-silico and in-vivo. Next, we
k 1
describe the simulation and HiL experimental set-ups.
Simulation set-up: simulations were performed in SUMO [21]; see also [20] for a description of the pipeline to import
maps and traffic demands. In our simulations, each parking lot can accommodate up to 50 cars and we generated the traffic
demand so that 100 cars would arrive on campus at 5-second intervals. All the cars seek to park and, by doing so, the
parking capacity is saturated. Given this setting, we simulated a road obstruction on the main link (in blue in Figure 1) from
the highway exit to the campus entrance. This was done by restricting, in SUMO, the speed of the link to less than one
kilometer per hour. Information on the cars in the simulation are contained in the stand-alone file agent.npy. Instead, the
pfs associated with the sources (described below) are all stored in behaviors.npy.
HiL set-up: the platform embeds a real vehicle into a SUMO simulation. By doing so, performance of the algorithm
deployed on a real car can be assessed under arbitrary synthetic traffic conditions generated via SUMO. The high-level
architecture of the platform is shown in Figure 2. The platform creates an avatar of the real car in the SUMO simulation.
Namely, as shown in Figure 2, the position of the real car is embedded in SUMO by using a standard smartphone to collect
its GPS coordinates. These coordinates are then sent via bluetooth to a computer, also hosted on the car in the current
implementation. The connection is established via an off-the-shelf app, which writes the coordinates in a rfcomm file. By
using the pySerial library, an interface was developed to read data in Python. Here, a script was designed leveraging
pynmeaGPS to translate the data in the NMEA format for longitude/latitude coordinates. With this data format, a Python
script was created to place the avatar of the real car in the position given by the coordinates. A GUI is also included
to highlight the trajectory of the real car on the map and an off-the-shelf text-to-speech routine is used to provide audio
feedback to the driver on the vehicle.

### B. In-car Implementation of the Algorithm

For both the in-silico and in-vivo experiments, Algorithm 1 was implemented in Python as a stand-alone class so that
each car equipped with the algorithm could function as a stand-alone agent. The class has methods accepting all the input
parameters of Algorithm 1 and providing as output the car behavior computed by the algorithm. The optimization problems
within the algorithm loop were solved via the Python library scipy.optimize. Additionally, the class also implements
methods to compute the cost and to support receding horizon implementations of Algorithm 1. In our experiments, we used
this receding horizon implementation: the width of the receding horizon window was T =5 and every time the car entered
Fig. 2: HiL functional architecture.

<!-- Page 8 -->

in a new link/state computations were triggered. The pfs from the sources in our experiments were such that, at each k,
feasibility of the problem was ensured (see Lemma 1). Following [20], we also implemented an utility function that restricts
calculations of the agent only to the road links that can be reached in T time steps (rather than through the whole state
space/map). With this feature, in our experiments the algorithm took on average approximately half a second to output a
behavior, less than the typical time taken to drive through a road link.1 Finally, the pfs of the sources were obtained via
built-in routing functions in SUMO and we added noise to the routes so that Assumption 2 would be fulfilled (for each road
link, S(π) is the set of outgoing links). See our github for the details.

### C. Experimental Results

Simulation results: first, we benchmarked the performance obtained by Algorithm 1 against these from the algorithm in
[3], [4], termed as crowdsourcing algorithm in what follows. To this aim, we considered Scenario 1 and performed two sets
of 10 simulations. In the first set of experiments, Algorithm 1 was used to determine the behavior of cars on campus (note
that Assumption 1 is fulfilled). In the second set of simulations, the cars instead used the crodwourcing algorithm. Across
the simulations, we recorded the number of cars that the algorithms were able to park. The results are illustrated in Figure 3
(top panel). The figure shows that the crowdsourcing algorithm was not able to park all the cars within the simulation. This
was instead achieved by Algorithm 1, which outperformed the algorithm from [3], [4]. To further quantify the performance,
we also computed the average time spent by a car looking for a parking space after it enters the simulation (ATTP: average
time-to-parking). Across the simulations, the ATTP for the algorithm in [3] was of 224.74±19.67, while for Algorithm 1
it was of 151.32±30.59 (first quantities are means, second quantities are standard deviations). That is, Algorithm 1 yielded
an average improvement of 32.7% in the ATTP. Then, we simulated the three cases of Scenario 2 to verify that Algorithm
1 can effectively regulate access through specific links. The constraints for the three cases of Scenario 2 were given as an
input to the algorithm and in Figure 3 (bottom panel) the optimal solution π∗(x |x =l ) is shown. The figure shows
k k−1 r
that the optimal solution indeed fulfills the constraints (the road link l is in Figure 1).
r
HiLresults: wedeployedAlgorithm1onarealvehicleusingtheHiLplatformandvalidateditseffectivenessinScenario
2 (C): the target behavior of the agent would make the real car reach the Terminal parking but this route is forbidden.
What we observed in the experiment was that, once the car entered in the campus, this was re-routed towards the Biblioteca
parking. The re-routing was an effect of Algorithm 1 computing the rightmost pf in Figure 3 (bottom panel). A video of the
HiLexperimentisavailableonourgithub.Thevideoshowsthatthealgorithmissuitableforrealcaroperation:itwouldrun
smoothly during the drive, providing feedback to the driver on the vehicle. Figure 4 shows the car’s route recorded during
the experiment.

## Vi. Conclusions

We considered the problem of designing agents able to compute optimal decisions by re-using data from multiple sources
to solve tasks involving: (i) tracking a desired behavior while minimizing an agent-specific cost; (ii) satisfying certain safety
constraints. After formulating the control problem, we showed that this is convex under a mild condition and computed the
optimal solution. We turned the results in an algorithm and used it to design an intelligent parking system. We evaluated the
algorithm via in-silico and in-vivo experiments with real vehicles/drivers. All experiments confirmed the effectiveness of the
algorithm and its suitability for in-car operation. Besides considering the use of other divergences in the cost and deploying
our results in more complex urban scenarios that would use data from pedestrians and sensors on-board vehicles, our future
research will involve devising mechanisms for the composition of policies for the tasks with actuation constraints in [22].

## References

[1] B.M.Lakeetal.,“Human-levelconceptlearningthroughprobabilisticprograminduction,”Science,vol.350,no.6266,pp.1332–1338,2015.
[2] E.Crisostomietal.,Analyticsforthesharingeconomy:Mathematics,EngineeringandBusinessperspectives. Springer,2020.
[3] G.Russo,“Onthecrowdsourcingofbehaviorsforautonomousagents,”IEEECont.Sys.Lett.,vol.5,pp.1321–1326,2020.
[4] E´.Garrabe´ andG.Russo,“Onthedesignofautonomousagentsfrommultipledatasources,”IEEECont.Sys.Lett.,vol.6,pp.698–703,2021.
[5] L. Li, C. De Persis, P. Tesi, and N. Monshizadeh, “Data-based transfer stabilization in linear systems,” 2022. [Online]. Available:
https://arxiv.org/abs/2211.05536
[6] J.Coulson,J.Lygeros,andF.Do¨rfler,“Data-enabledpredictivecontrol:IntheshallowsoftheDeePC,”inEuropeanControlConference,2019,pp.
307–312.
[7] H. J. van Waarde, J. Eising, H. L. Trentelman, and M. K. Camlibel, “Data informativity: a new perspective on data-driven analysis and control,”
IEEETrans.AutomaticControl,vol.65,pp.4753–4768,2020.
[8] C.DePersisandP.Tesi,“Formulasfordata-drivencontrol:Stabilization,optimality,androbustness,”IEEETrans.AutomaticControl,vol.65,pp.
909–924,2020.
[9] F.CeliandF.Pasqualetti,“Data-drivenmeetsgeometriccontrol:Zerodynamics,subspacestabilization,andmaliciousattacks,”IEEECont.Sys.Lett.,
vol.6,pp.2569–2574,2022.
[10] U.RosoliaandF.Borrelli,“Learningmodelpredictivecontrolforiterativetasks.Adata-drivencontrolframework,”IEEETrans.AutomaticControl,
vol.63,pp.1883–1896,2018.
1this duration was measured between the moment where the GUI shows the car merging on a new link and the moment where new directions are
displayed.Thesimulationwasrunonamodernlaptop.

<!-- Page 9 -->

[11] K.P.WabersichandM.N.Zeilinger,“Bayesianmodelpredictivecontrol:Efficientmodelexplorationandregretboundsusingposteriorsampling,”
ser.Proc.ofMLResearch,vol.120,2020,pp.455–464.
[12] J.Berberich,J.Kohler,M.A.Muller,andF.Allgower,“Data-drivenmodelpredictivecontrolwithstabilityandrobustnessguarantees,”IEEETrans.
Aut.Contr.,vol.66,pp.1702–1707,2021.
[13] G. Baggio, V. Katewa, and F. Pasqualetti, “Data-driven minimum-energy controls for linear systems,” IEEE Cont. Sys. Lett., vol. 3, pp. 589–594,
2019.
[14] E´miland Garrabe´ and G. Russo, “Probabilistic design of optimal sequential decision-making algorithms in learning and control,” Annual Rev, in
Control,vol.54,pp.81–102,2022.
[15] N.Cammardella,A.Busic,Y.Ji,andS.P.Meyn,“Kullback-Leibler-Quadraticoptimalcontrolofflexiblepowerdemand,”inIEEE58thConference
onDecisionandControl,2019,pp.4195–4201.
[16] N.Cesa-BianchiandG.Lugosi,Prediction,learning,andgames. CambridgeUniversityPress,2006.
[17] M.Cutler,T.J.Walsh,andJ.P.How,“Real-worldreinforcementlearningviamultifidelitysimulators,”IEEETrans.onRobotics,vol.31,pp.655–671,
2015.
[18] V.B.Mountcastle,“Thecolumnarorganizationoftheneocortex.”Brain,vol.120,pp.701–722,Apr1997.
[19] W. Griggs et al., A Vehicle-in-the-Loop Emulation Platform for Demonstrating Intelligent Transportation Systems. Cham: Springer International
Publishing,2019,pp.133–154.
[20] E´.Garrabe´ andG.Russo,“CRAWLING:aCrowdsourcingAlgorithmonWheelsforSmartParking,”2022,preprintsubmittedtoScientificReports.
[Online].Available:https://arxiv.org/abs/2212.02467
[21] Pablo Alvarez Lopez and others, “Microscopic traffic simulation using SUMO,” in 21st IEEE International Conference on Intelligent TransportationSystems,2018,pp.2575–2582.
[22] D. Gagliardi and G. Russo, “On a probabilistic approach to synthesize control policies from example datasets,” Automatica, vol. 137, p. 110121,
2022.
Fig. 3: Top: unparked cars over time for crowdsourcing and Algorithm 1. Solid lines are means across the simulations, shaded areas
are confidence intervals (one standard deviation). Bottom: π∗(x | x = l ) for the three cases of Scenario 2. The pfs satisfy the
k k−1 r
constraints. Link definitions in Figure 1.

<!-- Page 10 -->


## Appendix

We report here an investigation of how the time taken by Algorithm 1 changes as a function of the number of sources,
S, and time horizon T. This time is a crucial aspect to investigate whether the approach we propose would scale to more
complex urban scenarios than the one presented in Section V, which would e.g., include more parking locations (note
that these are seen as links by Algorithm 1) and more complex road networks together with more sources that the agent
could use to determine its optimal behavior. The time Algorithm 1 takes to output a behavior depends on the number of
available sources, the time horizon T and the number of links accessible to the car within the time horizon. We analyze the
computation time w.r.t. the
To investigate Algorithm 1’s computation time, we considered the same implementation as in Section V-B and ran the
algorithm by varying the receding horizon window between 0 and 5 time steps, and the number of sources available to the
agent between 1 and 6. For this, additional sources were taken from [20], where more sources were used to implement the
algorithm from [4]. For each pair of these parameters, we measured the time taken by Algorithm 1 to output a behavior,
by running the algorithm over each link in the network on a standard computer and taking the average of such times. This
gives a fair estimate of the average runtime, as the amount of states considered depends on the density of the connections
in the neighborhood of each link.
The results of this numerical investigation are shown in Figure 5. The figure shows that the highest computation time is
about one second, which appears to be suitable for our reference application.
Fig. 4: Route of the real vehicle. The continuous line shows the GPS position during the HiL experiment (map from OpenStreetMaps).

<!-- Page 11 -->

Fig. 5: Computation time as a function of time horizon and number of sources