---
title: "Multimodal Chain of Thought"
original_file: "./Multimodal_Chain_of_Thought.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["rag", "evaluation", "multimodal"]
keywords: ["cid", "methods", "central", "parameter", "figure", "gcv", "selected", "where", "test", "iteration"]
summary: "<!-- Page 1 -->

Parameter Selection by GCV and a χ2 test within Iterative Methods for
ℓ -regularized Inverse Problems
1

### Brian Sweeney∗, Rosemary Renaut∗, and Malena I. ℓ regularizationisusedtopreserveedgesorenforcesparsityinasolutiontoaninverseproblem. We
1
investigate the Split Bregman and the Majorization-Minimization iterative methods that turn this
non-smooth minimization problem into a sequence of steps that include solving an ℓ -regularized
2
minimization problem."
related_documents: []
---

# Multimodal Chain of Thought

<!-- Page 1 -->

Parameter Selection by GCV and a χ2 test within Iterative Methods for
ℓ -regularized Inverse Problems
1

### Brian Sweeney∗, Rosemary Renaut∗, and Malena I. Espan˜ol∗

Abstract. ℓ regularizationisusedtopreserveedgesorenforcesparsityinasolutiontoaninverseproblem. We
1
investigate the Split Bregman and the Majorization-Minimization iterative methods that turn this
non-smooth minimization problem into a sequence of steps that include solving an ℓ -regularized
2
minimization problem. We consider selecting the regularization parameter in the inner generalized
Tikhonov regularization problems that occur at each iteration in these ℓ iterative methods. The
1
generalized cross validation and χ2 degrees of freedom methods are extended to these inner problems. In particular, for the χ2 method this includes extending the χ2 result for problems in which
the regularization operator has more rows than columns and showing how to use the A−weighted
generalizedinversetoestimatepriorinformationateachinneriteration. Numericalexperimentsfor
image deblurring problems demonstrate that it is more effective to select the regularization parameter automatically within the iterative schemes than to keep it fixed for all iterations. Moreover,
an appropriate regularization parameter can be estimated in the early iterations and used fixed to
convergence.
Key words. ℓ regularization,SplitBregman,Majorization-Minimization,GCV,χ2 degreesoffreedommethod
1

### AMS subject classifications. 65F22, 65F10, 68W40


## Introduction. We are interested in solving discrete ill-posed inverse problems where

we have an observation b˜ from an unknown input x, connected by the linear system A˜x ≈ b˜,
where A˜ ∈ Rm×n, b˜ ∈ Rm, and x ∈ Rn. We assume that A˜ is ill-conditioned and that b˜ is
contaminated by additive Gaussian noise: b˜ = b˜ +ϵ , where ϵ ∼ N(0,C ) is a Gaussian
true b˜ b˜ b
noise vector. The matrix C is a symmetric positive definite (SPD) covariance matrix. Since
b
A˜ is ill-conditioned, solving the problem with direct inversion will lead to a noisy solution.
Therefore, we impose regularization to make the problem well-posed. One option is to apply
Tikhonov regularization [39] and solve the minimization problem
(cid:26) 1 λ2 (cid:27)
(1.1) min ∥A˜x−b˜∥2 + ∥Lx∥2 ,
x 2 W b 2 2
where W = C−1 and the weighted norm is defined as ∥z∥2 = z⊤W z for any vector z.
b b W b b
Here,λisaregularizationparameterthatbalancesthedatafidelitytermandtheregularization
term. TheregularizationmatrixL ∈ Rp×n isoftenselectedasthediscretizationofaderivative
operator [22], and the regularization term then minimizes the corresponding derivative of x.
Other matrices, such as discrete wavelet [15] or framelet transforms [9, 41], can be used to
minimize the value of x in the corresponding subspaces.
We can whiten the noise in the data by multiplying out the weighted norm in (1.1), giving
∗School of Mathematical and Statistical Sciences, Arizona State University, Tempe, AZ (bfsweene@asu.edu,
renaut@asu.edu, and malena.espanol@asu.edu )
1
4202
ceD
31
]AN.htam[
2v65191.4042:viXra

<!-- Page 2 -->


## 2 Sweeney, Renaut And Espan˜Ol

the minimization problem
(cid:26) 1 λ2 (cid:27)
(1.2) min ∥Ax−b∥2+ ∥Lx∥2 ,
x 2 2 2 2
where
(1.3) A = W 1/2 A˜ and b = W 1/2 b˜.
b b
Now, b = b +ϵ , where ϵ ∼ N(0,I ). For the rest of the paper, we use the weighted A
true b b m
and b, meaning that we assume ϵ ∼ N(0,I ).
b m
One benefit of the ℓ regularization problem (1.2) is that it has a closed-form solution, but
2
it also makes solutions smooth. If the true solution has edges or is sparse, smooth solutions
may not be desirable. For these types of solutions, the 1-norm is typically used as it preserves
edges and enforces sparsity. This gives the ℓ -regularized problem
1
(cid:26) (cid:27)
1
(1.4) min ∥Ax−b∥2+µ∥Lx∥ .
x 2 2 1
Here, µ is a regularization parameter and L is a regularization matrix as in (1.2). One special
case of ℓ regularization is total variation (TV) regularization, first introduced in [37], where
1
L is the discretization of the first derivative. Unlike (1.2), (1.4) does not have a closed-form
solution. Matrices A and L may not have full rank, but we assume the invertibility condition

## (1.5) N(A)∩N(L) = ∅.

In both (1.2) and (1.4), the value of the regularization parameter has a large impact on
the solution. For (1.2), there are many methods for selecting λ, including the discrepancy
principle (DP) [21, 34], the unbiased predictive risk estimator (UPRE) [30], generalized cross
validation (GCV) [17], the L-curve criterion [19], and the χ2 degrees of freedom (dof) test
[33]. If training data sets are available, there are also learning approaches that can be used
to select λ [8, 11]. Many of these methods make use of the closed-form solution, which makes
applying them to (1.4) difficult. As a result, there are fewer parameter selection methods for
(1.4). Some methods have been extended to selecting µ directly in (1.4), including DP [3, 28]
and the L-curve [24, 42]. With the L-curve, the two terms in (1.4) are plotted against each
other on a log-scale, and µ is selected at the corner of the corresponding curve. There are
also methods in the statistics community for selecting µ based upon the degrees of freedom
in the solution [38], including the χ2 dof test for the TV problem [31]. Some methods have
also been applied within iterative methods for (1.4). DP in its iterative form [5, 6], GCV [5],
and the residual whiteness principle (RWP) [5, 29] have been applied to select parameters at
each iteration within iterative methods.
Main contributions: We consider the Split Bregman (SB) and Majorization-Minimization
(MM) iterative methods for solving the ℓ regularization problem. Both iterative methods
1
solve an ℓ -ℓ minimization problem of the form
2 2
(cid:26) 1 λ2 (cid:27)
(1.6) minJ(x) = min ∥Ax−b∥2+ ∥Lx−h(k)∥2 ,
x x 2 2 2 2

<!-- Page 3 -->


## Parameter Estimation In Sb And Mm Methods 3

at the kth iteration. Based on this minimization problem, we consider new methods for
selecting λ at every iteration. In particular, we extend GCV and the χ2 dof test to this
inner problem. For GCV, we derive the GCV function for (1.6), which is different than it is
for (1.2) due to h(k). To apply the χ2 dof test, we use the A-weighted generalized inverse
of L to replace h(k) in (1.6) so that we can apply the χ2 test with the regularization term
∥L(x−x )∥ for a suitably defined reference vector x . We also extend the non-central χ2
0 2 0
test for this configuration, and provide a new result on the degrees of freedom for problems in
which L has more rows than columns, as needed for 2D cases. Through numerical examples,
we show that these selection methods can be applied at each iteration to achieve results that
are comparable to finding a fixed λ that is optimal with respect to the minimization of the
relative error in the solution. We also demonstrate that GCV and the χ2 dof test can be used
in the initial iterations to find a suitable regularization parameter. The methods zoom in on a
parameter that is then held fixed when the change in the parameter per iteration is less than
a given tolerance. This works well and is less expensive than estimating λ by GCV or the χ2
estimator at every iteration.
The organization of this paper is as follows. In section 2, we review SB and MM iterative
methods. In section 3, we develop three new methods to find the iterative dependent regularization parameter for the Tikhonov problem that arises in both the SB and MM algorithm,
focusing on the GCV in subsection 3.1, the χ2 dof test in subsection 3.2, and the non-central
χ2 dof test in subsection 3.2.1. In subsection 3.3, we present the DP and RWP, which are
other established methods for selecting the parameter at each iteration. These methods are
compared with numerical examples in section 4. Conclusions are presented in section 5.

## Iterative methods for ℓ regularization. In this section, we review the split Bregman

1
(SB) and the Majorization-Minimization (MM) methods, which share the inner problem of
the form (1.6). Both methods are applied to the weighted A and b as defined in (1.3).

### The Split Bregman method. In the SB method, introduced by Goldstein and Osher

[16], the problem (1.4) is rewritten as a constrained optimization problem
(cid:26) (cid:27)
1
(2.1) min ∥Ax−b∥2+µ∥d∥ s.t. Lx = d.
x 2 2 1
Problem (2.1) can then be converted to an unconstrained optimization problem
(cid:26) 1 λ2 (cid:27)
(2.2) min ∥Ax−b∥2+ ∥Lx−d∥2+µ∥d∥ ,
x,d 2 2 2 2 1
which can be solved by a series of minimizations and updates known as the SB iteration
(cid:26) 1 λ2 (cid:27)
(2.3) (x(k+1),d(k+1)) = argmin ∥Ax−b∥2+ ∥Lx−d(k)+g(k)∥2+µ∥d∥
2 2 2 2 1
x,d
(2.4) g(k+1) = g(k)+(Lx(k+1)−d(k+1)).

<!-- Page 4 -->


## 4 Sweeney, Renaut And Espan˜Ol

In Problem (2.3) the vectors x and d can be found separately as
(cid:26) 1 λ2 (cid:27)
(2.5) x(k+1) = argmin ∥Ax−b∥2+ ∥Lx−(d(k)−g(k))∥2
2 2 2 2
x
(cid:26) λ2 (cid:27)
(2.6) d(k+1) = argmin µ∥d∥ + ∥d−(Lx(k+1)+g(k))∥2 .
1 2 2
d
Here, and in the update (2.4), g is the vector of Lagrange multipliers.
Clearly, the solution of (2.3) depends on parameters λ and µ that are often chosen as
problem-dependent known values. In this investigation, we hold the ratio τ = µ(k)/(λ(k))2
fixed and explore methods to select λ(k) at each iteration. This keeps the threshold constant
across iterations whereas if we tune µ instead, the threshold would change at each iteration.
With these parameters, µ(k) = τ(λ(k))2 and (2.6) becomes
(cid:26) (cid:27)
1
(2.7) d(k+1) = argmin τ∥d∥ + ∥d−(Lx(k+1)+g(k))∥2 .
1 2 2
d
Since the elements of d are decoupled in (2.7), d(k+1) can be computed using shrinkage
operators. That is, each element is given by
(cid:16) (cid:17)
d (k+1) = shrink (Lx(k+1)) +g (k) ,τ ,
j j j
where shrink(x,τ) = sign(x)·max(|x|−τ,0). Algorithm 2.1 summarizes the SB algorithm.
NoticethatSBisrelatedtoapplyingthealternatingdirectionmethodofmultipliers(ADMM)
to the augmented Lagrangian in (2.2) [14].
Algorithm 2.1 The SB Method for the ℓ -ℓ Problem (1.4)
2 1
Input: A,b,L,τ,d(0) = g(0) = 0

### Output: x

1: for k = 0,1,... until convergence do
2: Estimate λ(k)
(cid:26) (cid:27)
3: x(k+1) = argmin 1∥Ax−b∥2+
(λ(k))2
∥Lx−(d(k)−g(k))∥2
x 2 2 2 2
4: d(k+1) = argmin d (cid:8) τ∥d∥ 1 + 1 2 ∥d−(Lx(k+1)+g(k))∥2 2 (cid:9)
5: g(k+1) = g(k)+ (cid:0) Lx(k+1)−d(k+1)(cid:1)
6: end for

### TheMajorization-Minimizationmethod. Anotheriterativemethodforsolving(1.4)

is the MM method. MM is an optimization method that utilizes two steps: majorization and
minimization [27]. In themajorization step, the function is majorizedwith a surrogate convex
function. The convexity of this function is then utilized in the minimization step. MM is
applied to (1.4) in [26], where it is combined with the generalized Krylov subspace (GKS)
method to solve large-scale image restoration problems. In MM-GKS, the Krylov subspace is
enlarged at each iteration, and MM is then applied to the problem in the subspace. Instead of

<!-- Page 5 -->


## Parameter Estimation In Sb And Mm Methods 5

building a Krylov subspace as in [7, 26, 35], we will apply the MM method directly to (1.4),
using the fixed quadratic majorant from [26]. Other ways for majorizing (1.4) include fixed
and adaptive quadratic majorants [1, 7, 35].
With this majorant, the minimization problem at each kth iteration is
(cid:26) 1 λ2 (cid:27)
(2.8) min ∥Ax−b∥2+ ∥Lx−w(k)∥2 ,
x 2 2 2 reg 2
where λ = (µ/ε)1/2 and
(cid:32) (cid:18) ε2 (cid:19)1 2 (cid:33)
(2.9) w(k) = u(k) 1−
reg (u(k))2+ε2
with u(k) = Lx(k). All operations in (2.9) are component-wise. Again, the parameters can be
selected at each iteration. Here, as with our approach for the SB algorithm, we select λ(k) at
each iteration and fix ε as in [5] for MM-GKS. Algorithm 2.2 summarizes the MM algorithm.
Algorithm2.2TheMMMethodfortheℓ -ℓ Problem(1.4)withaFixedQuadraticMajorant
2 1
Input: A,b,L,x(0),ε

### Output: x

1: for k = 0,1,... until convergence do
2: u(k) = Lx(k)
(cid:32)
(cid:18)
(cid:19)1(cid:33)
3: w r (k eg ) = u(k) 1− (u(k) ε ) 2 2 +ε2 2
4: Estimate λ(k)
(cid:26) (cid:27)
5: x(k+1) = argmin x 1 2 ∥Ax−b∥2 2 + (λ( 2 k))2 ∥Lx−w r (k eg ) ∥2 2
6: end for

### The inner minimization problem. At each iteration k in both SB and MM we solve

a problem of the form as given by (1.6) with the regularization parameter λ replaced by λ(k)
(see (2.5) for SB and (2.8) for MM). In SB, h(k) = d(k)−g(k), while in MM, h(k) = w (k) . We
reg
focus on (1.6) and regularization parameter estimation methods for finding λ(k) that can be
used within each iteration of SB and MM.

### Matrix decompositions. To rewrite (1.6), we will use the generalized singular value

decomposition (GSVD) [18, 21, 25], which is a joint matrix decomposition of two matrices
A and L. Consider A ∈ Rm×n and L ∈ Rp×n, and let n˜ = rank(L). When m ≥ n and
the invertibility condition (1.5) is satisfied, there exist orthogonal matrices U ∈ Rm×m and
V ∈ Rp×p and an invertible matrix X ∈ Rn×n such that

## (2.10) A = Uυ˜X−1, L = Vm˜ X−1,


<!-- Page 6 -->


## 6 Sweeney, Renaut And Espan˜Ol

where
 

## Υ 0

n˜×(n−n˜)

## Υ˜ = 0

(n−n˜)×n˜
I (n−n˜)×(n−n˜), Υ = diag(υ
1
,...,υ
n˜
),
0 0
(m−n)×n˜ (m−n)×(n−n˜)
(cid:20) (cid:21)

## M 0

M˜ = n˜×(n−n˜) , M = diag(µ ,...,µ ),
0 0 1 n˜
(p−n˜)×n˜ (p−n˜)×(n−n˜)
with 0 ≤ υ ≤ ··· ≤ υ < 1, 1 ≥ µ ≥ ··· ≥ µ > 0, and υ2 +µ2 = 1 for i = 1,...,n˜. For
1 n˜ 1 n˜ i i
i = 1,...,n˜, γ = υ /µ are called the generalized singular values. Here, and throughout, we
i i i
use I and 0 to denote the identity and zero matrices, respectively, of dimension a×b
a×b a×b
and which may possibly have no rows or no columns.
The GSVD is helpful for analyzing the properties of the solutions as a function of λ and,
consequently, for analyzing regularization methods. On the other hand, computationally, it
is only helpful for small problems. Other joint decompositions, such as the discrete Fourier
transform or the discrete cosine transform, can be practical for larger problems, as we will see
in the numerical results section.

## Estimation of the regularization parameter. In this section, we present three new

methods for finding the regularization parameter in the iterative updates for the SB and MM
methods. Weconsiderinsubsection3.1theGCVmethodandinsubsection3.2theχ2 doftest.
Note that while the χ2 dof test requires that C is known, there is no such requirement for
b
the GCV method. We also consider in subsection 3.2.1 a non-central χ2 formulation adapted
to the iteration in the SB algorithm. Subsection 3.3 includes two other parameter selection
methods, DP and RWP, that will be used for comparison in the numerical results section.

### The method of generalized cross validation. GCV [2, 17] is a parameter selection

method that selects λ to minimize predictive risk. GCV has been applied to the generalized
Tikhonov problem (1.2), which has the solution x = A♯b, where A♯ is the influence matrix
λ λ λ
defined by A♯ = A−1A⊤ with A = A⊤A+λ2L⊤L. In GCV, λ is selected to minimize the
λ L L
GCV function
∥Ax −b∥2
(3.1) G(λ) = λ 2 ,
[Tr(I−A )]2
λ
where A = AA♯ is the resolution matrix. GCV has also been extended to other regulariza-
λ λ
tion problems [10]. Formulae for the GCV to solve (1.2) in terms of the GSVD of {A,L} are
given in [12, 33, 40] for different orderings of the sizes for m,n,p.
In [5], GCV is used to select the parameter at each iteration in MM when adaptive
majorants are used. With adaptive majorants, the minimization problem has the same form
as (1.2). We will extend GCV to the case when the inner-minimization problem has the form
(1.6) for which the solution x is different. This also impacts the formula in terms of the
λ
GSVD of {A,L}, and impacts the form of the GCV function as summarized in the following
Theorem. The proof follows the steps given in [10], but modified due to the vector h(k).

<!-- Page 7 -->


## Parameter Estimation In Sb And Mm Methods 7

Theorem 3.1. The GCV function for (1.6), where h(k) is replaced by h, has the same form
as (3.1), but now with x given by
λ
(3.2) x = A−1(A⊤b+λ2L⊤h) = A♯b+L♯h,
λ L λ λ
where L♯ = λ2A−1L⊤. When m ≥ n and the GSVD is defined as in (2.10), G(λ) for n ≥ p
λ L
and p > n is given by
(3.3)
(cid:80)n˜ (cid:16) λ2γi(v i ⊤h) (cid:17)2 + (cid:80)n˜ (cid:16) λ2(u⊤ i b) (cid:17)2 + (cid:80)m (cid:0) u⊤b (cid:1)2 −2 (cid:80)n˜ λ4γi(u⊤ i b)(v i ⊤h)
i=1 γ2+λ2 i=1 γ2+λ2 i=n+1 i i=1 (γ2+λ2)2

### G(λ) = i i i ,

(cid:104) (cid:105)2
max(m−n,0)+ (cid:80)n˜ λ2
i=1 γ2+λ2
i
where we ignore any sum in which the lower limit is greater than the upper limit.
Proof. In GCV, λ is selected to minimize the average predictive risk when we leave out
an entry of b. Let x [k] be the solution when the kth entry of b is missing. Then, in GCV we
λ
select λ to minimize the predictive risk for all k:
(cid:40) m (cid:41)
minG(λ) = min 1 (cid:88) ((Ax [k] ) −b )2 .
λ λ m λ k k
k=1
Defining the m × m matrix E = diag(1,1,...,1,0,1,...,1), where the kth entry is 0, the
k
[k]
solution x can be written as
λ
(3.4) x [k] = (A⊤E⊤E A+λ2L⊤L)−1(A⊤E⊤E b+λ2L⊤h).
λ k k k k
From the definition of E , we have the following properties [10]:
k
(3.5) E⊤E = E , and E = I−e e⊤,
k k k k k k
where e is the kth unit column vector of length m. From these properties, we obtain
k
A⊤E⊤E A+λ2L⊤L = (A⊤A+λ2L⊤L)−a a⊤ = A −a a⊤,
k k k k L k k
where a⊤ = e⊤A is the kth row of A. Then, by applying the Sherman-Morrison formula
k k

### B−1uv⊤B−1

(B+uv⊤)−1 = B−1−
1+v⊤B−1u
to B = A , u = −a , and v = a , and using the first property in (3.5), we rewrite (3.4) as

### L k k

(cid:32) (cid:33)

### A−1a a⊤A−1

x [k] = A−1+ L k k L (A⊤E b+λ2L⊤h)
λ L 1−a⊤A−1a k
k L k
(cid:32) (cid:33)

### A−1a a⊤

(3.6) = I+ L k k A−1(A⊤E b+λ2L⊤h).
1−a⊤A−1a L k
k L k

<!-- Page 8 -->


## 8 Sweeney, Renaut And Espan˜Ol

Notice that a⊤A−1a is the kth diagonal entry of A˜ , which we will denote by a˜ . Since
k L k λ kk
(Ax [k] ) = e⊤Ax [k] = a⊤x [k] , we use (3.6) to obtain
λ k k λ k λ
(cid:32) (cid:33)
a⊤A−1a a⊤
(Ax [k] ) = a⊤+ k L k k A−1(A⊤E b+λ2L⊤h)
λ k k 1−a⊤A−1a L k
k L k
(cid:18) (cid:19)
a˜
= 1+ kk a⊤A−1(A⊤E b+λ2L⊤h)
1−a˜ k L k
kk
(cid:18) (cid:19)
1
= e⊤AA−1(A⊤E b+λ2L⊤h)
1−a˜ k L k
kk
(cid:18) (cid:19) (cid:18) (cid:19)
1 1
= e⊤AA♯E b+ e⊤AL♯h.
1−a˜ k λ k 1−a˜ k λ
kk kk
Then, by the second property in (3.5)
(cid:18) (cid:19) (cid:18) (cid:19)
1 1
(Ax [k] ) −b = e⊤AA♯E b+ e⊤AL♯h−e⊤b
λ k k 1−a˜ k λ k 1−a˜ k λ k
kk kk
(cid:18) (cid:19)
1
= e⊤AA♯b
1−a˜ k λ
kk
(cid:18) (cid:19) (cid:18) (cid:19)
a˜ 1
− kk e⊤b+ e⊤AL♯h−e⊤b
1−a˜ k 1−a˜ k λ k
kk kk
(cid:18) (cid:19) (cid:18) (cid:19) (cid:18) (cid:19)
1 1 a˜
= e⊤AA♯b+ e⊤AL♯h− 1+ kk e⊤b
1−a˜ k λ 1−a˜ k λ 1−a˜ k
kk kk kk
(cid:18) (cid:19)
1 (Ax ) −b
= e⊤(Ax −b) = λ k k .
1−a˜ k λ 1−a˜
kk kk
Therefore, the GCV function is given by
1 (cid:88)
m (cid:20)
(Ax λ ) k −b k
(cid:21)2
G(λ) = .
m 1−a˜
kk
k=1
We can approximate the diagonal values of A˜ by the average diagonal value Tr(A˜ )/m,
λ λ
which produces a weighted version of the function [17]. The resulting function is then
∥Ax −b∥2

### G(λ) = λ 2 ,

(cid:104) (cid:16) (cid:17)(cid:105)2
Tr I−A˜
λ
which is the desired GCV function.
Next, we derive the formula of the GCV function (3.3) in terms of the GSVD of {A,L}
when m ≥ n, given in (2.10). To do so, we first write

## (3.7) A˜ = Aa−1A⊤ = Uυ˜Φ−1Υ˜⊤U⊤,

λ L

<!-- Page 9 -->


## Parameter Estimation In Sb And Mm Methods 9

where Φ = (Υ˜⊤Υ˜ +λ2M˜ ⊤M˜ ). The numerator then becomes
∥Ax −b∥2 = ∥AA♯b+AL♯h−b∥2
λ 2 λ λ 2
(3.8) = ∥UΥ˜Φ−1Υ˜⊤U⊤b+λ2UΥ˜Φ−1M˜ ⊤V⊤h−b∥2.
2
Factoring out the orthogonal matrix U from (3.8), we obtain
∥UΥ˜Φ−1Υ˜⊤U⊤b+λ2UΥ˜Φ−1M˜ ⊤V⊤h−b∥2
2
= ∥(Υ˜Φ−1Υ˜⊤−I )U⊤b+λ2Υ˜Φ−1M˜ ⊤V⊤h∥2
m 2
(3.9) = ∥KU⊤b+λ2ZV⊤h∥2,
2
where K ∈ Rm×m and Z ∈ Rm×p are diagonal matrices, defined as
 
−Ψ 0 0 (cid:20) (cid:21)
ζ 0
(3.10) K =  0 0 n−n˜ 0  and Z = 0 0
0 0 −I (m−n˜)×(p−n˜)
m−n
with Ψ,ζ ∈ Rn˜×n˜ given by
(cid:18) λ2 λ2 (cid:19) (cid:18) γ γ (cid:19)
1 n˜
(3.11) Ψ = diag ,..., and ζ = diag ,..., .
γ2+λ2 γ2 +λ2 γ2+λ2 γ2 +λ2
1 n˜ 1 n˜

### This can be written out as

(3.12) ∥KU⊤b+λ2ZV⊤h∥2 = (cid:88) n˜ (cid:18) λ2γ i (v i ⊤h) (cid:19)2 + (cid:88) n˜ (cid:18) λ2(u⊤ i b) (cid:19)2 + (cid:88) m (cid:16) u⊤b (cid:17)2
2 γ2+λ2 γ2+λ2 i
i=1 i i=1 i i=n+1
−2 (cid:88) n˜ λ4γ i (u⊤ i b)(v i ⊤h) ,
(γ2+λ2)2
i=1 i
where we ignore any sum where the lower limit is greater than the upper limit. In (3.12)
we deliberately show the cross terms involving the diagonal matrix-vector products in the
numerator. Practically, we use the form given in (3.9) that can be computed efficiently.
In the denominator, we can use (3.7) to obtain the desired result,
(cid:104) (cid:16) (cid:17)(cid:105)2 (cid:104) (cid:16) (cid:17)(cid:105)2
Tr I−A˜ = Tr I−UΥ˜Φ−1Υ˜⊤U⊤
λ
(cid:104) (cid:16) (cid:17)(cid:105)2 (cid:34) (cid:88) n˜ λ2 (cid:35)2
= Tr I−Υ˜Φ−1Υ˜⊤ = +max(m−n,0) .
γ2+λ2
i=1 i
To find the minimizer of G(λ), following the approach in [20], we first evaluate G at 200
logarithmically-spaced values of λ. We then take the λ that gives the smallest value of G and
search for the minimizer in an interval around this value.

<!-- Page 10 -->


## 10 Sweeney, Renaut And Espan˜Ol


### The χ2 degrees of freedom test. At each iteration in SB and MM, we minimize the

functional J(x) in (1.6). The χ2 dof test is a parameter selection method that treats x as a
random variable and utilizes the distribution of the functional evaluated at its minimizer to
select λ [32]. In [33], the χ2 dof test is applied to the functional J (x) which is defined by

## L

(3.13) J (x) = ∥Ax−b∥2+∥L(x−x )∥2 .

## L 2 0 W

h
Here, x is a reference vector of prior information on x. We assume that x = x, where x
0 0
is the expected value of x. It is also assumed in [33] that L has fewer rows than columns,
p ≤ n, and L(x − x ) = ϵ , where ϵ ∼ N(0,C ) and C is a SPD covariance matrix.
0 h h h h
The matrix W = C−1 is then the corresponding precision matrix. We also suppose that
h h
the model errors x − x = ϵ are normally distributed with covariance C . From this,

## 0 L L

b ∼ N(Ax,I +AC A⊤). Then, in [33, Theorem 3.1], it is shown that for large m and for
m L
given W , J is a random variable that follows a χ2 distribution with m+p−n degrees of
h L
freedom.
The goal of the χ2 method is then to find W so that J (x) most resembles a χ2 distrih L
bution with the appropriate degrees of freedom. In [36], the χ2 dof test for (3.13) is extended
to the case when x ̸= x, in which case J (x) follows a non-central χ2 distribution.

## 0 L

Under the assumption that C = λ−2I , we define
h p
(cid:110) (cid:111)
(3.14) x = argminJ (x) = argmin ∥Ax−b∥2+λ2∥L(x−x )∥2 .
λ L 2 0 2
x x
J (x) then follows a χ2 distribution. In particular, the following theorem gives its degrees of

## L

freedom, that holds for p > n and p ≤ n.
Theorem 3.2. Suppose that Ax−b ∼ N(0,I ), L(x−x ) ∼ N(0,λ−2I ), m ≥ n, and
m 0 p
n˜ = rank(L). For a given λ and the corresponding solution x , J (x ) is a random variable
λ L λ
that follows a χ2 distribution with m˜ = n˜+max(m−n,0) degrees of freedom.
Proof. The case when m ≥ n ≥ p is given in [33, Theorem 3.1]. For the general case when
m ≥ n without a restriction onp, the approach follows that given in the proof of [33, Theorem
3.1]. Noting that the solution of (3.14) is given by x = x +A−1A⊤r, where r = b−Ax ,
λ 0 L 0
we can use the GSVD of {A,L} in (2.10), to write J (x ) as

### L λ

J (x ) = ∥Ax +AA−1A⊤r−b∥2+λ2∥LA−1A⊤r∥2

### L λ 0 L 2 L 2

(cid:13) (cid:13)2
= (cid:13)AA−1A⊤r−r(cid:13) +λ2∥LA−1A⊤r∥2
(cid:13) L (cid:13) L 2
2
= ∥UΥ˜Φ−1Υ˜⊤U⊤r−r∥2+λ2∥VM˜ Φ−1Υ˜⊤U⊤r∥2
2 2
(3.15) = ∥(Υ˜Φ−1Υ˜⊤−I )s∥2+λ2∥M˜ Φ−1Υ˜⊤s∥2,
m 2 2
where s = [s ,...,s ]⊤ = U⊤r. We note that Υ˜Φ−1Υ˜⊤−I = K and
1 m m
(cid:20) (cid:21)
ζ 0

## M˜ Φ−1Υ˜⊤ = ,

0 0
(p−n˜)×(m−n˜)
where K is defined in (3.10) and ζ ∈ Rn˜×n˜ is defined in (3.11).

<!-- Page 11 -->


## Parameter Estimation In Sb And Mm Methods 11

Thus, (3.15) becomes
(cid:88)
n˜ λ4
(cid:88)
m
(cid:88)
n˜ λ2γ2

### J (x ) = s2+ s2+ i s2

L λ (γ2+λ2)2 i i (γ2+λ2)2 i
i=1 i i=n+1 i=1 i
(cid:88)
n˜ λ2
(cid:88)
m
(cid:88)
n˜
(cid:88)
m
(3.16) = s2+ s2 = k2+ k2,
γ2+λ2 i i i i
i=1 i i=n+1 i=1 i=n+1
with k = [k ,...,k ]⊤ = Ts, where
1 m

##  Ψ1/2 0 0 

T =  0 I n−n˜ 0 .

## 0 0 I

m−n
Next, we need to show that the k are distributed standard normal. Using the GSVD, we have
i
that VM˜ X−1(x−x ) ∼ N(0,λ−2I ). Using the properties for normally distributed vectors,
0 p
we obtain x−x ∼ N(0,λ−2Xdiag(M−2,0 )X−1). The residual r then has mean zero
0 n−n˜
and covariance matrix
(cid:20) M−2 0 (cid:21)  Ψ−1 0 0 

## I

m
+λ−2UΥ
0 0

## Υ⊤U⊤ = U 0 I

n−n˜

## 0 U⊤ = Ut−2U⊤.

n−n˜ 0 0 I
m−n
Thus, k has covariance TU⊤(UT−2U⊤)UT⊤ = I and the k follow a standard normal
m i
distribution. Hence, J (x ) is the sum of m˜ = n˜ +max(m−n,0) squared standard normal

### L λ

random variables.
When m˜ is large, the χ2 distribution can be approximated by a normal distribution with
m˜
mean m˜ and variance 2m˜, denoted by N(m˜,2m˜). We can use this approximation to find λ
suchthatJ (x )isthenapproximatelydistributedasN(m˜,2m˜). Asin[33], weforma(1−α)

### L λ

confidence interval to find λ:
√ √
m˜ −z 2m˜ ≤ J (x ) ≤ m˜ +z 2m˜.
α/2 L λ α/2
Here, z is the relevant z-value for the standard normal distribution, which defines the
α/2
bounds for the (1−α) confidence interval. Defining F(λ) = J (x )−m˜, we apply Newton’s

### L λ

method to λ such that
√ √
(3.17) −z 2m˜ ≤ F(λ) ≤ z 2m˜.
α/2 α/2
The derivative of F(λ) is F′(λ) = 2λ∥˜s∥2. Here, ˜s = [s˜ ,...,s˜ ]⊤, where s˜ = γ s /(γ2 +λ2)
2 1 n˜ i i i i
for i = 1,...,n˜. We notice immediately that for λ > 0, as required, F′ > 0, and hence it is
reasonable to use a root-finding method for λ, provided that we can find an interval in which
F(λ) changes sign. This is discussed in more detail in [33]. An example of F(λ) is given in
Figure 1(a).
The tolerance for Newton’s method depends on the selection of the significance level α.
A smaller value of α makes the (1−α) confidence interval wider, increasing the probability

<!-- Page 12 -->


## 12 Sweeney, Renaut And Espan˜Ol

that a random value of λ satisfies (3.17). On the other hand, a larger α narrows this interval,
increasing the confidence that λ satisfies the χ2 distribution.
For SB and MM, the inner minimization problem (1.6) is not of the desired form (3.13)
for the central χ2 dof test. In particular, we need Lx in place of h(k) in (1.6). To find x
0 0
such that h(k) ≈ Lx , we will use the the A-weighted generalized inverse of L, denoted L†

## 0 A

[13]. In terms of the GSVD of {A,L}, L† = XM˜ †V⊤, where M˜ † ∈ Rn×p has diagonal entries

## A

1/µ . If p ≥ n, then L† = L†, where L† is the pseudoinverse of L [21]. For p < n, L† ̸= L†
i A A
in general.
In terms of the GSVD of {A,L}, LL† = VM˜ M˜ †V⊤. When L is invertible, and when

## A

p ≤ n, M˜ M˜ † = I so LL† = I . In the χ2 dof test, we will estimate x as L† h(k) and use
p A p 0 A
LL† h(k) in place of h(k). With this, (1.6) can be rewritten in the form of (3.13). Provided

## A

that x is approximately the expected value of x, we may use the central χ2 dof test at each
0
iteration of SB and MM. In the case where x ̸≈ x, the central χ2 dof test no longer applies.
0

#### The non-central χ2 dof test. When x ̸≈ x, J (x) follows a non-central χ2 dis-


## 0 L

tribution with m˜ degrees of freedom and non-centrality parameter c, defined by
(cid:88)
n˜ λ2q2
(cid:88)
m
c(λ) = i + q2,
γ2+λ2 i
i=1 i i=n+1
where q = [q ,...,q ]⊤ = U⊤A(x−x ) [36]. As with the central χ2 dof test, the goal of
1 m 0
the non-central test is to find λ so that J ∼ χ2(m˜,c(λ)). When m˜ is sufficiently large, this

## L

non-centralχ2 distributioncanbe approximated bya normal distributionwith meanm˜ +c(λ)
and variance 2m˜ +4c(λ). Using this approximation, we can form a (1−α) confidence interval
to find λ:
(cid:112) (cid:112)
m˜ +c(λ)−z 2m˜ +4c(λ) ≤ J (x ) ≤ m˜ +c(λ)+z 2m˜ +4c(λ).
α/2 L λ α/2
Defining F (λ) = J (x )−(m˜ +c(λ)), this is equivalent to solving the problem

### C L λ

(cid:112) (cid:112)
(3.18) −z 2m˜ +4c(λ) ≤ F (λ) ≤ z 2m˜ +4c(λ).
α/2 C α/2
In this case, the derivative of F (λ) is

## C

(cid:16) (cid:17)
(3.19) F′ (λ) = 2λ ∥˜s∥2−∥q˜∥2 ,

## C 2 2

where q˜ = [q˜ ,...,q˜ ]⊤ with q˜ = γ q /(γ2 +λ2) for i = 1,...,n˜. Notice that when x = x,
1 n˜ i i i i 0
q = 0 and the non-central test reduces to the central test.
From (3.19), it is immediate that F′ (λ) is not of constant sign, so F (λ) may potentially

## C C

have no root or multiple roots. Figure 1(b) shows an example where F (λ) is not monotone

## C

andhasnoroot. IfF (λ)hasasingleroot, wecanapplyNewton’smethodtofindλsuchthat

## C

(3.18) holds. Otherwise, we follow the method presented in [36] to find λ such that F (λ) is

## C

close to zero.
To use the non-central χ2 dof test in SB and MM, we still rewrite (1.6) using LL† h(k) in

## A

placeofh(k). Wealsoneedtohaveanestimateoftheexpectedvalueofxtouseasxinthetest.

<!-- Page 13 -->


## Parameter Estimation In Sb And Mm Methods 13

(a) F(λ) (b) F (λ)

## C

Figure 1. Plots of F(λ) and F (λ) for MM, where the selected λ is marked. In Figure 1(b), F (λ) is not

## C C

monotonic and does not have a root.
Within both SB and MM, one option is to use the current solution x(k) as an approximation
of x. Another option in SB is to estimate x using L† d(k) since d in SB approximates Lx

## A

quite well. We will use x = x(k), assuming that at a given step of the iteration we are looking
to reduce the noise around the current estimate, and that for increasing k with convergence
we have x = lim x(k).
k

### OtherMethods. DPandRWPareotherestablishedmethodsthathavebeenapplied

to (1.6) at each iteration [5, 29]. Both methods utilize a closed form of the residual at each
iteration to select λ.
DP is a method that uses an estimate of the norm of the noise to bound the norm of
the residual. Assuming that δ > 0 is an estimate of the norm of the noise and ν > 1 is a
parameter, then λ is selected so that
(3.20) ∥Ax −b∥ ≤ νδ.
λ 2
DP is applied at each iteration in MM in [5] and can be applied in its iterative form within
other iterative methods. Using the expression for the residual r = Ax −b, (3.20) can be
λ λ √
solved using a root-finding method. Since we normalize the noise, we will use δ = ∥e ∥ = n
b 2
and set ν = 1.01.
RWP is a parameter selection method [29] for 2D problems that selects λ so that the 2D
residual most resembles white noise. We take the residual r , reshape it into its 2D form
λ
R ∈ RN×N, and use the normalized auto-correlation of R to measure whiteness. A non-
λ λ
negative scalar measure of the whiteness, W : RN×N → R+, is then used to compare the
residuals for different λ. This measure is given by
W(λ) = ∥ρ(FR )∥ = ∥FR λ ⋆FR λ ∥2 2 = (cid:80) l,m |(FR λ ) l,m |4 ,
λ ∥FR λ ∥4 2 (cid:16) (cid:80) l,m |(FR λ ) l,m |2 (cid:17)2
whereF ∈ CN×N isthe2DdiscreteFouriertransformmatrixand⋆denotesthe2Dcorrelation
operator. The optimal λ for the RWP is then λ that minimizes W. To minimize W, we will
use the same method that was used to minimize G in GCV. RWP is incorporated within
ADMM in [29] while in [5], it is applied to the residual at each iteration. As with DP, the
expression for r can be used to select λ at each iteration in SB and MM.
λ

<!-- Page 14 -->


## 14 Sweeney, Renaut And Espan˜Ol


## Numericalexamples. Inthissection,weapplySBandMMtotwodeblurringproblems

to test the parameter selection methods presented in section 3. To compare methods, we will
use the relative error (RE) which is defined by
∥x−x ∥
RE = true 2
∥x ∥
true 2
and the improved signal to noise ratio (ISNR), which is defined by
(cid:18) (cid:19)
∥b−x ∥
ISNR = 20log true 2 .
10 ∥x−x ∥
true 2
Both RE and ISNR measure how close a solution is to x , where a closer solution has a
true
smaller RE and a larger ISNR.
In practice, x is unknown, so to understand when these methods have converged, we
true
will consider the relative change in x and λ. The relative change in x, defined as
(cid:13) (cid:13)
(cid:13)x(k)−x(k−1)
(cid:13)
(4.1) RC(x(k)) = 2,
(cid:13) (cid:13)
(cid:13)x(k−1)(cid:13)
2
measures how much the solution is changing at a given iteration. If it is below a specified
tolerance, TOL , then the solution is not changing much and we can consider the solution to
x
be converged and stop iterating. This tolerance should depend on the noise level. Because we
use the weighted data fidelity term with A and b as defined in (1.3), it is sufficient to use a
fixed tolerance, here TOL = 0.001, for all noise levels.
x
The relative change in λ2,
|(λ(k))2−(λ(k−1))2|
(4.2) RC((λ(k))2) = ,
|(λ(k−1))2|
measures how much λ2 changes from one iteration to the next. If RC((λ(k))2) < TOL , then,
λ
we can stop selecting λ and fix it at the current value until convergence. This reduces the
computational cost from applying the parameter selection method at every iteration. In both
(4.1) and (4.2), we assume, without loss of generality, that the denominator is non-zero.
For each example, we select λ at each iteration with the different selection methods and
compare the results to the optimal fixed λ. To find this optimal λ, we run each example to
completion for 121 values of λ that are logarithmically spaced from 10−1 to 103 and select as
optimal the λ that has the smallest RE at convergence. This means that the optimal solution
is not feasible in general as it requires knowledge of the true solution. We report the cost for
the optimal as running the method once with a fixed λ, but the actual cost is more expensive
as it requires knowing the true solution and running the methods multiple times to find the
optimal λ. Moreover, τ and ε are tuned to minimize the RE, requiring the knowledge of the
true solution, when the optimal λ is used. When the parameter selection methods perform
as well as using the fixed optimal parameter, we should not expect there to be significant
differences between solutions. In these cases, we instead focus on the cost of each of the
methods to achieve these solutions, using the optimal solution as a point of comparison.
For the χ2 dof tests, we use xSB = L† (d − g) and xMM = L† (w ). For the non-
0 A 0 A reg
central χ2 dof test, we use x = x(k). Furthermore, in all the numerical experiments we use a
significance level of α = 0.999 for the χ2 dof test.

<!-- Page 15 -->


## Parameter Estimation In Sb And Mm Methods 15

(a) 1D deblurring (b) SB, Optimal λ, (c) MM, Optimal λ,
problem: x and b˜ λ=232.6 λ=464.2
Figure2. Figure 2(a): xandb˜ forthe1Ddeblurringproblem(SNR=20). Figures 2(b)and2(c)showthe
SB and MM solutions where λ is fixed at the optimal.

### A 1D example. For the first numerical example, we will consider a 1D blurring

problem. The matrix A˜ ∈ RN×N is symmetric Toeplitz where the first row is
1 (cid:104) (cid:16) (cid:17) (cid:105)
(4.3) z = √ exp
−[0:band−1]2
0 .
2πσ2 2σ2 N−band
We use N = 512, σ2 = 24, and band = 60. Gaussian noise with SNR = 20 is added to
the blurred signal to produce b˜. To demonstrate the capabilities of our methods, we use a
signal with sharp edges. The true signal x and the blurred and noisy data b˜ are given
true
in Figure 2(a). We solve this problem with SB and MM for L ∈ R(N−1)×N defined as the
discretization of the first derivative operator with zero boundary conditions:
 
−1 1 0 ··· 0
 0 −1 1 0 ··· 0
L =    . . . ... ... . . .    .
 
 0 ··· 0 −1 1 0
0 ··· 0 −1 1
Given the size of this 1D example, we use the GSVD of {A,L} to solve the inner problem in
bothSBandMM.Fourdifferentmethodsforselectingλateachiterationaretested: GCV,the
central χ2 dof test, the non-central χ2 dof test, and DP. These are compared with the results
obtained using the optimal fixed λ. In the χ2 dof tests, the significance level of α = 0.999
corresponds to a bound of 0.042 on F(λ). For F (λ), the bound will be at least 0.042 but it

## C

(cid:13) (cid:13)
increases with λ and (cid:13)x(k)−x 0(cid:13) 2 . In this example, the bound on F C (λ) ranges from 0.042
to 0.1, with the larger value obtained in the initial iterations. For the four selection methods,
TOL = 0.01 is applied and compared with selecting parameters at every iteration.
λ

#### Split Bregman. In SB, we set τ = 0.005 as RC(x(k)) decreases smoothly until

convergence for this τ. The ideal value of τ depends on the noise level, where τ should be
smaller when the noise level is lower. In this case, a larger value of τ causes RC(x(k)) to spike
upward at different iterations, even for a fixed value of λ. The optimal fixed λ in this case is
λ = 232.6 and the corresponding solution is shown in Figure 2(b). The results for SB with
theseselectionmethodsareshowninFigure3, withsolutionsprovidedinFigure4. Thevalues

<!-- Page 16 -->


## 16 Sweeney, Renaut And Espan˜Ol

(a) Relative error (b) Relative change (c) Selection of λ (d) Relative change (e) ISNR
in x in λ2
Figure 3. Results for SB applied to Figure 2(a) where λ is fixed at the optimal λ = 232.6, or selected at
eachiterationwithGCVortheχ2 doftests. Figure 3(a)plotstheREbyiteration,Figure 3(b)plotstherelative
change in x, Figure 3(c) plots the λ selected, Figure 3(d) plots the relative change in λ2, and Figure 3(e) plots
the ISNR.
(a) λ selected by GCV (b) λ selected by central (c) λ selected by (d) λ selected by DP
χ2 non-central χ2
(e) λ selected by GCV, (f) λ selected by central (g) λ selected by (h) λ selected by DP,
TOL =0.01 χ2, TOL =0.01 non-central χ2, TOL =0.01
λ λ λ

## Tol =0.01

λ
Figure 4. SB solutions at convergence for Figure 2(a).
of λ selected by the non-central χ2 dof test oscillate in the first 15 iterations. This is to be
anticipated with the choice x(k) for x. Initially, we expect that x(k) does not serve as a good
estimate for x to be used at step k +1 because, in the beginning steps, the values for x(k)
are far from convergence. The bound on F (λ) oscillates with λ and is largest at iteration 2

## C

where it is 0.1. This suggests that a smaller α might be better in the early iterations when
x(k) is further from x as this would increase the bound and therefore dampen the oscillations.
Despite the oscillations for the early iterations, the selection of λ still converges for α = 0.999.
On the other hand, the values of λ selected by GCV and the central χ2 dof test converge
earlier.

<!-- Page 17 -->


## Parameter Estimation In Sb And Mm Methods 17

(a) Relative error (b) Relative change (c) Selection of λ (d) Relative change (e) ISNR
in x in λ2
Figure 5. Results for MM applied to Figure 2(a) where λ is fixed at the optimal λ=464.2, or selected at
eachiterationwithGCVortheχ2 doftests. Figure 5(a)plotstheREbyiteration,Figure 5(b)plotstherelative
change in x, Figure 5(c) plots the λ selected, Figure 5(d) plots the relative change in λ2, and Figure 5(e) plots
the ISNR.
(a) λ selected by GCV (b) λ selected by central (c) λ selected by (d) λ selected by DP
χ2 non-central χ2
(e) λ selected by GCV, (f) λ selected by central (g) λ selected by (h) λ selected by DP,
TOL =0.01 χ2, TOL =0.01 non-central χ2, TOL =0.01
λ λ λ

## Tol =0.01

λ
Figure 6. MM solutions at convergence for Figure 2(a).

#### Majorization-Minimization. InMM,wefixε = 0.0003,whichisnearthesuggested

value in [4, 6] relative to the magnitude of x. The ideal value of ε depends on the magnitude
of u(k) = Lx(k). In this case, the optimal fixed λ is λ = 464.2, which produces the solution
in Figure 2(c). The results of the selection methods are shown in Figure 5 with solutions in
Figure 6. From these plots, both GCV and the χ2 dof tests select λ well, leading to better
convergence than the optimal. Initial values of λ found using the non-central χ2 dof test
oscillate, but still converge. The bound on F (λ) changes with the oscillations, reaching a

## C

maximum of 0.068 in iteration 2. These initial steps serve to find a stabilizing value for λ that
is suitable for the noise in the steps after the tolerance TOL has been achieved.
λ

<!-- Page 18 -->


## 18 Sweeney, Renaut And Espan˜Ol


#### Discussion on the one-dimensional results. The results using the SB and MM

iterative methods with the regularization parameter methods are summarized in Table 1.
In SB, the non-central χ2 dof test and DP perform best of the parameter selection methods, converging in fewer iterations and to solutions with smaller RE and larger ISNR. When
TOL = 0.01, GCV and the central χ2 dof test converge faster than the other methods but
λ
havesolutionswithalargerRE. InMM,thefourselectionmethodseachconvergetosolutions
having approximately the same RE. Of these methods, GCV is the fastest. In general, SB
and MM are different, with SB taking longer to converge but to solutions with a smaller RE
and larger ISNR. The results suggest that the best method with respect to RE and ISNR is
SB with the non-central χ2 dof test. Using TOL = 0.01 does not significantly impact the
λ
results of the selection methods.

### Table 1

RE,ISNR,iterations,andcomputationtime(inseconds)forthesolutionstothe1DexampleinFigure 2(a).
The best results are shown in boldface, excluding the methods where λ is fixed at the optimal.
No TOL TOL = 0.01
λ λ
Method RE ISNR Iter. Time RE ISNR Iter. Time

### SB, Optimal 0.126 65.14 34 0.04


### Sb, Gcv 0.138 64.37 41 0.34 0.146 63.86 46 0.06


### SB, Central χ2 0.145 63.93 44 0.10 0.145 63.92 46 0.08

SB, Non-central χ2 0.127 65.08 34 0.20 0.127 65.08 34 0.13
SB, DP 0.127 65.06 35 0.18 0.127 65.06 35 0.17

### MM, Optimal 0.165 62.78 35 0.04


### Mm, Gcv 0.171 62.50 22 0.06 0.170 62.53 23 0.04


### MM, Central χ2 0.169 62.59 22 0.07 0.169 62.59 22 0.06

MM, Non-central χ2 0.170 62.53 22 0.11 0.170 62.54 22 0.07

### Mm, Dp 0.170 62.55 24 0.12 0.170 62.55 24 0.12


### A 2D example. For our 2D example, we use an image deblurring problem. We

use the cameraman image in Figure 7(a), which is 512 by 512 pixels. Since the results are
indistinguishable when using full images, we will instead focus on the zoomed-in section of
x shown in Figure 7(b). The matrix A˜ ∈ R5122×5122 now models a separable blur, defined
true
by A˜ = (C ⊗C ), where ⊗ defines a Kronecker product and the matrix C is a circulant
z z z
matrix with first row given by (4.3) with N = 512, band = 40, and σ2 = 16. White Gaussian
noise with SNR = 20 is then added to obtain b˜. The blurred and noisy image is given in
Figure 7(c), with the blurred zoom-in shown in Figure 7(d). We set L = D , where

## 2D

(cid:20) (cid:21)

## I⊗D


## D = 1D


## 2D D ⊗I


## 1D


<!-- Page 19 -->


## Parameter Estimation In Sb And Mm Methods 19

and D ∈ RN×N is the discretization of the first derivative with periodic boundary condi-

## 1D

tions:
 
−1 1 0 0 ··· 0
 0 −1 1 0 ··· 0 

## D =

 

. .
.
... ... . .
.
 
.

## 1D  

 0 ··· 0 −1 1 0 
 
 0 0 ··· 0 −1 1 
1 0 ··· 0 0 −1
Tosolvethisproblem,weusetheweightedAandbasgivenin(1.3). Inthiscase,p = 524,288
and n = 262,144 so p = 2n > n. Instead of the GSVD, for this problem we use the discrete
Fourier transform [23] for which we have the mutual decomposition

## A = F∗Λ F


## A

(cid:20) I ⊗D (cid:21) (cid:20) F∗ 0 (cid:21)(cid:20) C (cid:21)

## L = N 1D = F.


## D ⊗I 0 F∗ D


## 1D N

Here F ∈ Cn×n is the 2D discrete Fourier transform matrix, and Λ is a diagonal matrix

## A

with the eigenvalues of A. The matrices C = diag(c ,...,c ) and D = diag(d ,...,d ) are
1 n 1 n
diagonal and defined by C = I ⊗Λ and D = Λ ⊗I , where

## N L L N

(cid:16) (cid:17)
Λ = diag(λ ,...,λ ), with λ = exp 2jπˆi/N −1, j = 1,...,N.

### L 1 N j

The matrix L† = L† is computed as

## A

(cid:20) (cid:21)
L† = L† = F∗(cid:2) C˜ D˜(cid:3) F 0 ,

## A 0 F

where C˜ = diag(c˜ ,...,c˜ ) and D˜ = diag(d˜ ,...,d˜ ) are diagonal matrices, with
1 n 1 n
(cid:40) ci , if|c |2+|d |2 ̸= 0 (cid:40) di , if|c |2+|d |2 ̸= 0
c˜
i
= |ci|2+|di|2 i i , and d˜
i
= |ci|2+|di|2 i i .
0, if|c |2+|d |2 = 0 0, if|c |2+|d |2 = 0
i i i i

### In this case,

LL† = (cid:20) F∗ 0 (cid:21)(cid:20) C (cid:21) (cid:2) C˜ D˜(cid:3) (cid:20) F 0 (cid:21) .

## A 0 F∗ D 0 F

This matrix is typically not the identity and has four diagonal submatrices of size n×n.
As before, the selection methods used for the 1D case as well as the 2D specific RWP are
compared with the optimal fixed λ. A confidence level of α = 0.999 is used in the χ2 dof tests,
which corresponds to a bound of 0.941 on F(λ) for the central test. The bound on F (λ) for

## C

the non-central test is larger, ranging from 0.941 to 1.485 in this example.

<!-- Page 20 -->


## 20 Sweeney, Renaut And Espan˜Ol

(a) x (b) x zoom-in (c) b˜ (d) b˜ zoom-in
true true
Figure 7. The true image x and the blurred and noisy image b˜ for the image deblurring example for
true
image of size 512×512. Zoomed-in sections of both images are also shown.
(a) Relative error (b) Relative change (c) Selection of λ (d) Relative change (e) ISNR
in x in λ2
Figure8. ResultsforSBappliedtoFigure 7(c)whereλisfixedattheoptimalλ=10.8, orselectedateach
iterationwithGCV,theχ2 doftests,orDP.Figure 8(a)plotstheREbyiteration,Figure 8(b)plotstherelative
change in x, Figure 8(c) plots the λ selected, Figure 8(d) plots the relative change in λ2, and Figure 8(e) plots
the ISNR.

#### Split Bregman. For SB, we set τ = 0.01 as this leads to RC(x(k)) decreasing

smoothly. Other values of τ were tested, but there was not a significant difference in the
results as long as τ is not extremely large or small. The convergence results given in Figure 8
and solutions given in Figure 9, demonstrate that GCV and the central χ2 test perform
best. Qualitatively, it is hard to distinguish between the solutions obtained using automatic
determination of λ and the optimal solution that is found by searching over a large range of
λ assuming the known solution. The DP and RWP solutions, however, are not as clear near
the handle and the stand. The λ selected by the non-central χ2 dof test oscillates initially,
but the RE is comparable to the other methods after the third iteration. In terms of RE and
ISNR, DP and RWP do not perform as well as the other selection methods.

#### Majorization-Minimization. We set ε = 0.01 as this is small relative to the magnitude of x [4, 6]. The results in Figure 10 and the reconstructions in Figure 11 show that for

this ε, both GCV and the central χ2 dof test selection methods are comparable to fixing λ at
the optimal, λ = 11.7. Again, the results are almost indistinguishable on the zoomed region
with slightly greater smoothing evident for the RWP and DP methods. The non-central χ2
dof test does not perform as well in this case, with the values of λ oscillating widely in Figure 10(c). DP and RWP again perform worse than GCV and the χ2 tests, with the solutions
not being as clear near the handle and the camera stand.

<!-- Page 21 -->


## Parameter Estimation In Sb And Mm Methods 21

(a) x zoom-in (b) Optimal λ
true
(λ=10.8)
(c) λ selected by (d) λ selected by (e) λ selected by (f) λ selected by DP (g) λ selected by

### GCV central χ2 non-central χ2 RWP

(h) λ selected by (i) λ selected by (j) λ selected by (k) λ selected by (l) λ selected by
GCV, TOL =0.01 central χ2, non-central χ2, DP, TOL =0.01 RWP, TOL =0.01
λ λ λ

## Tol =0.01 Tol =0.01

λ λ
Figure 9. Zoomed-in windows of the SB solutions at convergence for Figure 7(c). We note that the full
images are indistinguishable and are thus not shown.
(a) Relative error (b) Relative change (c) Selection of λ (d) Relative change (e) ISNR
in x in λ2
Figure 10. Results for MM applied to Figure 7(c) where λ is fixed at the optimal λ=11.7, or selected at
each iteration with GCV, the χ2 dof tests, or DP. Figure 10(a) plots the RE by iteration, Figure 10(b) plots
the relative change in x, Figure 10(c) plots the λ selected, Figure 10(d) plots the relative change in λ2, and
Figure 10(e) plots the ISNR.

<!-- Page 22 -->


## 22 Sweeney, Renaut And Espan˜Ol

(a) x zoom-in (b) Optimal λ
true
(λ=11.7)
(c) λ selected by (d) λ selected by (e) λ selected by (f) λ selected by DP (g) λ selected by

### GCV central χ2 non-central χ2 RWP

(h) λ selected by (i) λ selected by (j) λ selected by (k) λ selected by (l) λ selected by
GCV, TOL =0.01 central χ2, non-central χ2, DP, TOL =0.01 RWP, TOL =0.01
λ λ λ

## Tol =0.01 Tol =0.01

λ λ
Figure 11. Zoomed-in windows of the MM solutions at convergence for Figure 7(c). We note that the full
images are indistinguishable and are thus not shown.

#### Discussion on the two-dimensional results. The results using the SB and MM

iterative methods with the regularization parameter methods are summarized in Table 2. In
general, SB is better than MM in terms of RE and ISNR. MM does take fewer iterations than
SB,butthetimingisclose. Wealsoobservethatatoleranceshouldbesetonλasthisreduces
the computational time while having little impact on the solution. The best method for the
2D problem is SB with central χ2 as this produces the best RE and ISNR. Both GCV and
the central χ2 dof test perform well with both SB and MM, with solutions having RE and
ISNR closest to the optimal. With TOL = 0.01, central χ2 is faster than GCV. The central
λ
χ2 test, however, does require information on the noise while GCV does not. The non-central
χ2 test and DP take longer to run and perform worse. With a lower noise level, the χ2 test
does not perform as well, so for a lower noise level, GCV is preferred while for a higher noise
level, the central χ2 is better.

<!-- Page 23 -->


## Parameter Estimation In Sb And Mm Methods 23


### Table 2

RE,ISNR,iterations,andcomputationtime(inseconds)forthesolutionstothe2DexampleinFigure 7(c).
The best results are shown in boldface, excluding the methods where λ is fixed at the optimal.
No TOL TOL = 0.01
λ λ
Method RE ISNR Iter. Time RE ISNR Iter. Time

### SB, Optimal 0.104 44.90 19 0.85


### Sb, Gcv 0.104 44.91 17 49.05 0.104 44.91 17 40.04


### SB, Central χ2 0.104 44.91 17 54.43 0.104 44.91 17 21.91

SB, Non-central χ2 0.106 44.72 17 135.54 0.106 44.72 17 111.37

### Sb, Dp 0.113 44.15 16 78.64 0.113 44.16 17 69.53

SB, RWP 0.109 44.51 17 58.99 0.109 44.51 17 58.99

### MM, Optimal 0.106 44.74 14 0.71


### Mm, Gcv 0.109 44.51 11 31.86 0.109 44.51 11 30.45


### MM, Central χ2 0.108 44.57 11 45.42 0.108 44.57 11 27.14

MM, Non-central χ2 0.110 44.41 15 145.17 0.110 44.41 15 145.17

### Mm, Dp 0.118 43.83 11 73.58 0.118 43.83 11 66.52


### Mm, Rwp 0.113 44.19 11 38.11 0.113 44.19 11 38.11


## Conclusions. We have presented methods for selecting the parameters in the inner

minimization problems of SB and MM by using GCV or the χ2 dof test at each iteration,
including showing a new approach to provide an estimate of the expected value of x each
iteration, and a new theorem on the χ2 degrees of freedom when p > n. For the non-central
χ2 dof test, we proposed using the current solution in the iterative method as the mean of
the solution. Although the parameters selected in this method vary in the early iterations,
they still converge once x(k) is closer to convergence. Numerical examples demonstrate that
selecting the parameter at each iteration with these methods produces comparable results
in terms of the final relative error and the number of iterations to using the optimal fixed
parameter. In addition, these methods do not need to be used at every iteration and can still
be helpful for finding a suitable parameter in the initial iterations. They zoom in on the ideal
parameter which can then be fixed after the selection method converges. This still performs
well and is computationally cheaper than searching for the fixed parameters by running SB
or MM to completion multiple times.
Acknowledgments. Funding: This work was partially supported by the National Science
Foundation (NSF) under grant DMS-1913136, and DMS-2152704 for Renaut. Any opinions,
findings, conclusions, or recommendations expressed in this material are those of the authors
and do not necessarily reflect the views of the National Science Foundation. M.I. Espan˜ol was
supported through a Karen Uhlenbeck EDGE Fellowship.

## References

[1] M. Alotaibi, A. Buccini, and L. Reichel, Restoration of blurred images corrupted by impulse noise
via median filters and ℓ -ℓ minimization, in 2021 21st International Conference on Computational
p q

<!-- Page 24 -->


## 24 Sweeney, Renaut And Espan˜Ol

Science and Its Applications (ICCSA), IEEE, 2021, pp. 112–122.
[2] R.C.Aster,B.Borchers,andC.H.Thurber,ParameterEstimationandInverseProblems,Elsevier,
Amsterdam, 2018.
[3] T.Bonesky,Morozov’sdiscrepancyprincipleandTikhonov-typefunctionals,InverseProblems,25(2008),
p. 015015.
[4] A. Buccini, G. Huang, L. Reichel, and F. Yin, On the choice of regularization matrix for an ℓ2-ℓq
minimization method for image restoration, Appl. Numer. Math., 164 (2021), pp. 211–221.
[5] A. Buccini, M. Pragliola, L. Reichel, and F. Sgallari, A comparison of parameter choice rules
for ℓ -ℓ minimization, Annali Dell’Universita’di Ferrara, 68 (2022), pp. 441–463.
p q
[6] A. Buccini and L. Reichel,An ℓ2-ℓq regularization method for large discrete ill-posed problems,J.Sci.
Comput., 78 (2019), pp. 1526–1549.
[7] A. Buccini and L. Reichel, An ℓ -ℓ minimization method with cross-validation for the restoration of
p q
impulse noise contaminated images, J. Comput. Appl. Math., 375 (2020), p. 112824.
[8] M. J. Byrne and R. A. Renaut, Learning spectral windowing parameters for regularization using
unbiased predictive risk and generalized cross validation techniques for multiple data sets, Inverse
Probl. Imaging, 17 (2023).
[9] J.-F. Cai, S. Osher, and Z. Shen, Linearized Bregman iterations for frame-based image deblurring,
SIAM J. Imaging Sci., 2 (2009), pp. 226–252.
[10] J.Chung,G.Easley,andD.P.O’Leary,Windowedspectralregularizationofinverseproblems,SIAM
J. Sci. Comput., 33 (2011), pp. 3175–3200.
[11] J. Chung and M. I. Espan˜ol, Learning regularization parameters for general-form Tikhonov, Inverse
Problems, 33 (2017), p. 074004.
[12] J. Chung, M. I. Espan˜ol, and T. Nguyen, Optimal regularization parameters for general-form
Tikhonov regularization, arXiv preprint arXiv:1407.1911, (2014).
[13] L. Elde´n,A weighted pseudoinverse, generalized singular values, and constrained least squares problems,
BIT Numerical Mathematics, 22 (1982), pp. 487–502.
[14] E. Esser, Applications of Lagrangian-based alternating direction methods and connections to split Bregman, CAM report, 9 (2009), p. 31.
[15] H.FangandH.Zhang,Wavelet-baseddouble-differenceseismictomographywithsparsityregularization,
Geophysical Journal International, 199 (2014), pp. 944–955.
[16] T. Goldstein and S. Osher, The split Bregman method for ℓ -regularized problems, SIAM J. Imaging
1
Sci., 2 (2009), pp. 323–343.
[17] G. H. Golub, M. Heath, and G. Wahba,Generalizedcross-validationasamethodforchoosingagood
ridge parameter, Technometrics, 21 (1979), pp. 215–223.
[18] G. H. Golub and C. F. Van Loan,Matrix Computations,JohnsHopkinsUniversityPress,Baltimore,

## Md, 1983.

[19] P. C. Hansen, Analysis of discrete ill-posed problems by means of the L-curve, SIAM Rev., 34 (1992),
pp. 561–580.
[20] P. C. Hansen, Regularization tools – a Matlab package for analysis and solution of discrete ill-posed
problems, Numerical Algorithms, 46 (1994), pp. 189–194.
[21] P. C. Hansen, Rank-deficient and Discrete Ill-posed Problems: Numerical Aspects of Linear Inversion,
SIAM, Philadelphia, 1998.
[22] P. C. Hansen, Discrete Inverse Problems: Insight and Algorithms, SIAM, Philadelphia, 2010.
[23] P. C. Hansen, J. G. Nagy, and D. P. O’leary, Deblurring Images: Matrices, Spectra, and Filtering,
SIAM, Philadelphia, 2006.
[24] R. Hou, Y. Xia, Y. Bao, and X. Zhou,Selection of regularization parameter for l1-regularized damage
detection, Journal of Sound and Vibration, 423 (2018), pp. 141–160.
[25] P. Howland and H. Park, Generalizing discriminant analysis using the generalized singular value
decomposition,IEEETransactionsonPatternAnalysisandMachineIntelligence,26(2004),pp.995–
1006.
[26] G. Huang, A. Lanza, S. Morigi, L. Reichel, and F. Sgallari, Majorization–minimization generalized Krylov subspace methods for ℓ −ℓ optimization applied to image restoration, BIT Numerical
p q
Mathematics, 57 (2017), pp. 351–378.
[27] D. R. Hunter and K. Lange, A tutorial on MM algorithms, Amer. Statist., 58 (2004), pp. 30–37.

<!-- Page 25 -->


## Parameter Estimation In Sb And Mm Methods 25

[28] B.Jin,Y.Zhao,andJ.Zou,Iterativeparameterchoicebydiscrepancyprinciple,IMAJ.Numer.Anal.,
32 (2012), pp. 1714–1732.
[29] A. Lanza, M. Pragliola, and F. Sgallari, Residual whiteness principle for parameter-free image
restoration, Electron. Trans. Numer. Anal., 53 (2020), pp. 329–351, https://doi.org/10.1553/etna
vol53s329.
[30] C. L. Mallows, Some comments on C , Technometrics, 42 (2000), pp. 87–94.
p
[31] J.Mead,χ2 testfortotalvariationregularizationparameterselection,InverseProbl.Imaging,14(2020).
[32] J. L. Mead, Parameter estimation: A new approach to weighting a priori information, J. Inv. Ill-posed
Problems, 16 (2008), pp. 175–194.
[33] J. L. Mead and R. A. Renaut, A Newton root-finding algorithm for estimating the regularization
parameter for solving ill-conditioned least squares problems, Inverse Problems, 25 (2008), p. 025002.
[34] V. A. Morozov, On the solution of functional equations by the method of regularization, in Doklady
Akademii Nauk, vol. 167, Russian Academy of Sciences, 1966, pp. 510–512.
[35] M. Pasha, Krylov Subspace Type Methods for the Computation of Non-negative or Sparse Solutions of
Ill-posed Problems, PhD thesis, Kent State University, Kent, OH, 2020.
[36] R. A. Renaut, I. Hneˇtynkova´, and J. Mead, Regularization parameter estimation for large-scale
Tikhonovregularizationusingaprioriinformation,Comput.Statist.DataAnal.,54(2010),pp.3430–
3445.
[37] L. I. Rudin, S. Osher, and E. Fatemi,Nonlinear total variation based noise removal algorithms,Phys.
D, 60 (1992), pp. 259–268.
[38] R. J. Tibshirani and J. Taylor, Degrees of freedom in lasso problems, Ann. Statist., (2012).
[39] A. N. Tikhonov and V. Y. Arsenin,Solutionofincorrectlyformulatedproblemsandtheregularization
method, Soviet Math. Dokl., 5 (1963), pp. 1035–1038.
[40] S. Vatankhah, R. A. Renaut, and V. E. Ardestani, Regularization parameter estimation for underdetermined problems by the χ2 principle with application to 2D focusing gravity inversion,Inverse
Problems, 30 (2014), p. 085002.
[41] G. Wang, J. Xu, Z. Pan, and Z. Diao, Ultrasound image denoising using backward diffusion and
framelet regularization, Biomedical Signal Processing and Control, 13 (2014), pp. 212–217.
[42] H.Yao,P.Gerstoft,P.M.Shearer,andC.Mecklenbra¨uker,CompressivesensingoftheTohoku-
OkiMw9.0earthquake: Frequency-dependentrupturemodes,GeophysicalResearchLetters,38(2011).