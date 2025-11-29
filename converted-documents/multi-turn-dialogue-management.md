---
title: "Multi Turn Dialogue Management"
original_file: "./Multi_Turn_Dialogue_Management.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["rag", "evaluation", "multimodal", "dialogue"]
keywords: ["data", "weight", "missingness", "causal", "age", "variables", "dag", "efv", "missing", "sex"]
summary: "<!-- Page 1 -->

Recoverability of Causal Effects under Presence of Missing

### Data: a Longitudinal Case Study

Anastasiia Holovchak1 Helen McIlleron2 Paolo Denti2 Michael Schomaker3,4

### Abstract

Missing data in multiple variables is a common issue. We investigate the applicability of the
framework of graphical models for handling missing data to a complex longitudinal pharmacological
study of children with HIV treated with an efavirenz-based regimen as part of the CHAPAS-3 trial. Specific"
related_documents: []
---

# Multi Turn Dialogue Management

<!-- Page 1 -->

Recoverability of Causal Effects under Presence of Missing

### Data: a Longitudinal Case Study

Anastasiia Holovchak1 Helen McIlleron2 Paolo Denti2 Michael Schomaker3,4

### Abstract

Missing data in multiple variables is a common issue. We investigate the applicability of the
framework of graphical models for handling missing data to a complex longitudinal pharmacological
study of children with HIV treated with an efavirenz-based regimen as part of the CHAPAS-3 trial.
Specifically, we examine whether the causal effects of interest, defined through static interventions on
multiple continuous variables, can be recovered (estimated consistently) from the available data only.
So far, no general algorithms are available to decide on recoverability, and decisions have to be made
on a case-by-case basis. We emphasize sensitivity of recoverability to even the smallest changes in
the graph structure, and present recoverability results for three plausible missingness directed acyclic
graphs (m-DAGs) in the CHAPAS-3 study, informed by clinical knowledge. Furthermore, we propose
the concept of “closed missingness mechanisms” and show that under these mechanisms an available
case analysis is admissible for consistent estimation for any type of statistical and causal query, even
if the underlying missingness mechanism is of missing not at random (MNAR) type. Both simulations
andtheoreticalconsiderationsdemonstratehow,intheassumedMNARsettingofourstudy,acomplete
oravailablecaseanalysiscanbesuperiortomultipleimputation,andestimationresultsvarydepending
on the assumed missingness DAG. Our analyses demonstrate an innovative application of missingness
DAGs to complex longitudinal real-world data, while highlighting the sensitivity of the results with
respect to the assumed causal model.
1 Introduction
Missing data are a common issue in biomedical research. In particular, longitudinal epidemiological
studies, where data are collected consecutively at several points in time, tend to suffer from missing
data on multiple variables. One common assumption which is often made regarding the missing data
mechanism is the so-called missing at random (MAR) assumption. If this assumption holds, statistical
methods for consistent estimation are available, for example, multiple imputation or inverse probability
weighting [1, 2].
However, if multiple variables are missing simultaneously, it is often difficult to justify whether the
MAR assumption holds. This is both because the classic MAR definition is event- rather than variablebased,andarguingfororagainstconditionalindependenciesofevents ispracticallychallenging,especially
in longitudinal settings [3]. Moreover, even though MAR is the weakest known condition under which
the missingness process can be ignored (i.e., dealt with using the observed data), it is only a sufficient,
but not a necessary condition for unbiased estimation; this means that under a missing not at random
(MNAR) scenario, it is unclear if and how a target estimand can be recovered (estimated consistently).
Totackletheseandotherchallenges, Mohanetal.[4]andMohanandPearl[3]proposedanalternative
causal graph-based framework, in which knowledge and assumptions about reasons for missingness are
encoded in relationships between variables and missing data indicators. This framework is very general
and can be used to evaluate whether estimands can be recovered given a correct causal missingness model
(missingness directed acyclic graph, m-DAG).
However, currently there is no general algorithm that can be used to establish recoverability for
arbitrary settings. Therefore, identification and estimation strategies have to be developed on a caseby-case basis for each particular scenario. This poses the question of how useful causal m-DAGs are
practically.
1Seminar for Statistics, ETH Zurich, Switzerland, anastasiia.holovchak@stat.math.ethz.ch
2Division of Clinical Pharmacology, Department of Medicine, University of Cape Town, South Africa
3Department of Statistics, Ludwig-Maximilians University Munich, Germany
4Centre for Infectious Disease Epidemiology and Research, University of Cape Town, South Africa
1
4202
tcO
81
]EM.tats[
3v26541.2042:viXra

<!-- Page 2 -->

Moreno-Betancur et al. [5] have convincingly argued that one should thus develop canonical m-DAGs
for recurring settings, such as for point-exposure study designs in epidemiology where missing data in
outcome, exposure, and confounders are caused by some “standard” mechanisms. They demonstrated
the usefulness of this approach in a study investigating the relationship between maternal mental illness
and child behavior.
While causal missingness graphs, and their canonical versions, are a major advancement for causal
inference research under missing data, their actual applicability has yet to be demonstrated in complex
longitudinal studies. It is unclear how well knowledge on missing data can actually be collected, then
integrated in a realistic causal graph, and how difficult the mathematical exercise of establishing identification and recoverability results in such a complex, yet realistic setting is. Can m-DAGs make their way
from blackboards to actual applications?
Recent work, such as by Balzer et al. [6] and Nugent et al. [7], has advanced the field by using
causal graphs and corresponding estimators to address recoverability and estimation of causal effects in
longitudinal settings subject to complex missingness and dependence. These studies focus on reducing
bias and improving efficiency by controlling for missing outcomes when estimating intervention effects.
Their frameworks, both relying on a Two-Stage TMLE approach, are particularly useful for handling
data in complex cluster randomized trial settings.
Inthiswork,wefocusontheexplicitmodelingofthemissingnessmechanism,notonlyfortheoutcome
but for all relevant variables in the study. This involves developing a causal missingness model, explaining its motivation through a variable-based taxonomy, and then demonstrating whether identification is
possible and what estimation strategies could be employed. We present an innovative application of missingness DAGs to a longitudinal study. Specifically, we investigate whether the derivation of identification
results in a longitudinal setting is feasible, how volatile those results are, and how complex deriving those
results can be.
Additionally, we conduct simulation studies aligned with the data example to, firstly, verify the theoreticalresultsontherecoverabilityofthedesiredcausalquery, andsecondly, toquantifytheextentofbias
in settings of special interest. Our simulations and theoretical considerations demonstrate that causal
diagrams help to explicitly guide the process of decision-making about whether a parameter of interest
can be consistently estimated from the available data. In practice, MAR is often assumed and multiple
imputation is performed, which in many cases may lead to biased estimation results. On the other hand,
we demonstrate that even in complex longitudinal study settings, there are MNAR scenarios for which
available case analysis leads to valid estimation results, whereas multiple imputation does not.
We sought to answer these questions by applying the framework proposed by Mohan and Pearl [3]
to answer a topical question in HIV-related pharmacoepidemiology, which is explained below in Section

## We i) investigate how clinical knowledge on reasons for our missing data can be best collected and

integratedintoarealisticcausalmissingnessgraph,ii)deriverecoverabilityresultsforourtargetestimand,
iii)discussestimationstrategiesforit,iv)evaluatethesensitivityofourresultswithrespecttotheassumed
causal model, and v) seek for structures that may be helpful in establishing results for future studies.
This paper is structured as follows. We introduce the motivating question in Section 2, followed by
the theoretical framework in Section 3. In Section 4, analyse the data from the complex longitudinal
pharmacological study CHAPAS-3, followed by the simulation study in Section 5. We conclude in Section
6.
2 Motivating Study
Our motivating data analysis comes from the Children with HIV in Africa–Pharmacokinetics and Adherence/Acceptability of Simple antiretroviral regimens randomized trial (CHAPAS-3). The study enrolled
478 children with HIV, between 1 month and 13 years of age, in 4 sites in Uganda and Zambia [8].
Children enrolled into the trial received combined antiretroviral therapy, i.e., one non-nucleoside reverse
transcriptase inhibitor (efavirenz or nevirapine) and two nucleoside reverse transcriptase inhibitors (abacavir, stavudine or zidovudine –which were the randomized components– and lamivudine).
We are interested in determining target concentrations using data from 125 children treated with
efavirenz (EFV). Efavirenz is used not only in children, but also adults, though dosing recommendations
2

<!-- Page 3 -->

(between 200 and 600 mg) depend on weight and age. Due to their different metabolic profiles and
adherence patterns, patients with the same efavirenz dose may have different concentrations, conferring
different protection against viral replication. Knowledge about concentrations is often used to derive
dosing recommendations using population PK models [9]. It is typically suggested that EFV concentrations between 1 and 4 mg/L should be achieved (at 12h after the dose was given, C12h). This is because
lowerconcentrationsmaybeinsufficienttoguaranteeviralsuppressionandthuseffectivetreatment, while
higher concentrations may lead to toxicity negatively affecting the central nervous system. Our target
estimand is thus the causal concentration-response curve (CCRC) at each follow-up visit, i.e. we are
interested in how the counterfactual probability of viral failure at time t varies as a function of possible
prior concentration trajectories.
Ouranalysismakesuseofthedatafrom[9]. Werecentlydiscussedstatisticalapproachesonestimating
theCCRC(10),butdidnotdiscussaspectsofmissingdata. Inthismanuscript,weextendtheabovestudy
by developing a causal missingness graph (informed by the pediatrician’s and trial team’s knowledge) and
derive identification and estimation approaches for our estimand of interest. More details on the analysis
are given in Section 4.
3 Framework
Missingness DAGs provide a natural extension of causal DAGs under the presence of missing data.
Consider a DAG G = (V,E) with a set of nodes V, |V| = n, which can be separated into two subsets V
o
and V , corresponding to sets of completely observed and partially observed variables. For each variable
m
X , i ∈ {1,...,n}, from the subset V , a binary missingness indicator variable M
i m Xi
(cid:40)
1 if X is missing,
i

## M =


### Xi

0 otherwise
is introduced in the missingness DAG to depict causal relationships with other relevant variables. In the
following, we refer to the set of missingness indicator variables as M. Additionally, the setup allows for
the existence of a latent (unmeasured) variable set U.
In this work, we make use of the framework introduced by Mohan and Pearl [3]. We refer to G as the
c
complete-DAG (c-DAG) (as in Moreno-Betancur et al. [5]), and G as the missingness DAG (m-DAG).
The c-DAG G includes only the variable set V := V ∪V ∪U that is relevant for identification conc o m
siderations with respect to the (causal) parameter of interest (assuming no missingness in the variables
in V ). The m-DAG G, however, also includes the set of missingness indicators M, and may additionm
ally consist of a set of auxiliary variables, denoted as Z, with variables in Z causing missingness in the
variables in V , but not being a cause of the variables from the set V. Note that variables from both V
m
and Z may be a cause of missingness in the variables from V .
m
[4],MohanandPearl[3]showthatcausaldiagramscanbeusedasapowerfultoolfortheidentification
and classification of missingness mechanisms. It is an important finding that the conventional taxonomy
of missing data [1] can be translated (with some minor changes) into the context of causal diagrams,
which is the focus of this work. However, it is essential to mention that the missingness taxonomy
definitions proposed by Rubin [1] and Mohan et al. [4] are, in general, not equivalent. Note that Rubin’s
framework of missing data is defined on the record-based level, which makes it particularly difficult to
apply in practice. Another issue that is often ignored is that the ‘realized’ MAR definition as proposed by
Rubin [1] is not required to hold for all possible values of the missingness indicator M, but only for those
present in the data. This makes clear that such a kind of definition does not hold for a data-generating
distribution in general, but only for a single data sample, as different missing data patterns may arise
for samples resulting from re-running of the experiment [11, 12]. To overcome this issue, Seaman et al.
[13] distinguishes between two types of MAR - realized MAR and everywhere MAR. The latter is a
‘stronger’ definition in the sense that conditional missingness distribution relates to the missing entries
for all realized and unrealized patterns of missing data, and not only to the one specific data sample
which has been observed.
3

<!-- Page 4 -->

Mohanetal.[4]proposeanalternativeframeworkofmissingdatataxonomy,whichisbasedongraphicalmodels. Thetwomainadvantagesofthegraph-basedmethodareanexplicitencodingofdependencies
on the variable level (and not record-based), and also depiction of causal mechanisms which are causing
missingness [12]. Note that m-DAGs represent both the data generating mechanism and the missing data
mechanism, both in a causal manner.
Let G be an m-DAG over a set of variables V ∪V ∪U∪M, where V and V denote the sets of
o m o m
completely and partially observed variables, correspondingly, U is a set of latent (unobserved) variables,
and M is the set of missingness indicators. We denote the corresponding (joint) data distribution as
P(V ,V ,U,M), and assume the distribution to be faithful [14] with respect to G. Broadly speaking,
o m
faithfulness requires that the joint distribution P(V ,V ,U,M) satisfies all the conditional indepeno m
dence relationships encoded by the DAG, and only those relationships. In other words, one assumes that
all observed conditional independencies follow from the graphical structure, and not from other reasons
(such as deterministic relationships between variables).
The missingness mechanism is commonly characterized in terms of the conditional distribution of M
given (V ,V ,U), say p(M|V ,V ,U). It has to be assumed that any missingness indicator from the
o m o m
set M is not a parent of any variable from V ∪V ∪U. We emphasize once more that in the grapho m
based missing data framework, we work with variable-based and not the record-based definitions of the
missingness mechanisms.
M Y Y M Y Y M Y Y M Y Y

## U


## A X A X A X A X

(a) MCAR (b) MAR (c) MNARa (d) MNARb
Figure1: Examplem-DAGsdepictingthreedifferenttypesofmissingnessmechanisms. Fullyandpartially
observed variables are depicted in green and yellow squares, respectively. We assume Y to be the disease
indicator, A the type of treatment, and X the patient age. M is the missingness indicator for the

## Y

outcome Y.

## Missing completely at random (MCAR). If missingness occurs randomly and is assumed not

to be caused by any variable in the model, missing or observed, we write
p(M|V ,V ,U) = p(M),
o m
which means that the conditional distribution of the missingness mechanisms given the variables
in the data set and, possibly, also the latent variables, is equal to the marginal distribution
of the missingness mechanism. This corresponds to the (unconditional) independence statement

## (V ,V ,U) ⊥⊥ M.

o m
In terms of an m-DAG, if the joint distribution p(V ,V ,U,M) is faithful with respect to the
o m
graph G, this means that there are no edges between the M variables and variables in V and V ,
o m
and parents of missingness indicator variables from M can only be other variables from M.
A commonly used example of the MCAR mechanism is an accidental technical error in an electronic
medical record, which leads to a loss of data on the disease indicator, compare with Figure 1a.

## Missing at random (MAR). In this case, the missingness mechanism is assumed to depend on

the fully observed variables only, but is not allowed to depend on the missing data values or latent
variables. In terms of the conditional distribution of M, this corresponds to
p(M|V ,V ,U) = p(M|V ).
o m o
4

<!-- Page 5 -->

The conditional independence statement that holds in this case is (V ,U) ⊥⊥ M|V , which in
m o
terms of m-DAGs (if the joint distribution is faithful to G) means that variables from M are not
allowed to have any parents from the sets V or U, but only from V and other M variables.
m o
For example, if a disease indicator is missing for some patients, and missingness for some reason
depends on the completely observed treatment only, one says that the missing data underlies the
MAR mechanism, as depicted in the example in Figure 1b.

## Missing not at random (MNAR). This category of missingness is most general. Data that

cannot be classified as MCAR or MAR fall in the MNAR category. In this case, the conditional
distribution of M, p(M|V ,V ,U), cannot be simplified. In an m-DAG (again, assuming faithfulo m
ness), if at least one M variable has a parent which is a latent variable U or is any of the partially
observed variables from the set V , then the missing data mechanism is MNAR.
m
A common example of MNAR is when a variable is causing its own missingness, e.g., if the missingness of the disease status entry depends on the disease status itself, as this is the case for the
m-DAG in Figure 1c. For instance, the presence of a disease is likely to increase the chances of
disease status being recorded due to the associated medical follow-ups and tests.
Another practically very relevant example is presented in Figure 1d. It shows a case where missingnessisdrivenbylatentvariables,whichmaypotentiallyalsobeacauseforanobservedvariable. For
example, socio-economic status (SES) may not be recorded in a medical study, but has an impact
on both the missingness in the disease indicator due to reduced healthcare visits and the type of
treatment an individual receives, since those with higher SES may have access to better healthcare
facilities and more advanced treatment options.
Notethatbothmissingdatataxonomiesareequivalentifi)observationsareindependent, andii)missingness indicators are conditionally independent [15]. In this case, the conditional distribution from the
graph-basedMARdefinitioncanbewrittenasaproductofconditionaldistributionsforsinglemissingness
indicators as well as for single observations, and this then leads to the equivalence of both definitions.
3.1 Recoverability of Target Quantities
Ingeneral,recoverabilityisapropertyofthetargetquantity/parameterθ(andtheprobabilitydistribution
P ) which states whether this quantity can be estimated consistently from the available data. To decide

## X

on recoverability, one needs to know the independence statements that hold in the joint distribution.
However, under the Markovness and faithfulness assumptions, all conditional independence statements
present in the data can be directly read off from the m-DAG G, and recoverability can therefore be
considered as a property of the pair {θ,G} [3]. Note that the term identifiability is used when assessing
whether a causal query can be expressed as a function of the observational distribution, whereas the
recoverability concept is used to describe whether a parameter (not necessarily in a causal context) can
be expressed as a function of the available data distribution [5].
Moreno-Betancuretal.[5]describethreemainconditionsrequiredforrecoverabilityofatargetparameter θ: consistency and well-defined interventions, positivity, and conditional independence conditions.
In this context, consistency is a property of central relevance. It says that the factual treatment value
coincides with the counterfactual outcome.
It has to be emphasized that many types of target parameters θ may be of interest, and different
missingness patterns may occur, which makes it impossible to derive a general automatized algorithm
allowing a decision about the recoverability of any specific θ. Therefore, the authors work on ‘canonical’ scenarios which are most typical for epidemiological studies. Mohan et al. [4], Mohan and Pearl [3]
present some theoretical results on recoverability of joint and conditional distributions. In this work, we
only briefly provide intuition on how recoverability works, focusing on aspects that are relevant for our
ownidentificationstrategies. Themaingoalistoexploitconditionalindependenciesbetweenthevariables
of interest and the missingness indicators (which can be read off from the d-separation statements that
hold in the graphs) in order to be able to condition on the missingness indicator variables (i.e., on M = 0
i
for some i). This way, observed variable values will be sufficient for consistent estimation of the target
5

<!-- Page 6 -->

quantity.
In the following, we focus on the recoverability of causal effects. Indeed, necessary and sufficient
conditions exist for recoverability of causal effects [3]. Under the presence of missing data, a necessary
condition for recoverability of a causal effect is the identifiability of this effect from the c-DAG of interest.
The causal effect is identifiable from a graph G if the interventional distribution can be determined
uniquely from the observed-data distribution alone [16, 17]. Shpitser and Pearl [18] provide a sound
and complete algorithm for conditional causal effect identification (IDC), which, for any causal effect,
can be used for determining identifiability and also for generation of an expression for the interventional
distribution in the case of an identifiable effect. Tikka and Karvanen [19] implemented the IDC algorithm
in the R-package causaleffect. Using the IDC algorithm, we get an estimand of the causal query
whenever identifiability holds for the causal effect. In turn, a sufficient condition for recoverability is that
the (identified) estimand is recoverable from the missingness graph. This, as mentioned before, has to be
decided on a case-by-case basis.

## A A

1 2

## X X

1 2

## Y Y

1 2

## M M M M


## X1 Y1 X2 Y2

Figure2: Anm-DAGdepictingtheMNARmissingnessmechanisminasimplelongitudinalstudy. Health
outcomes at two study time points are denoted as Y and Y , sequential treatment variables as A and
1 2 1
A , and side effects as X and X .
2 1 2
Next, an example of recoverability procedure of a causal effect for a simple longitudinal study with
two measurement points is presented. The example is inspired by Mohan and Pearl [3, Section 3.5].
Consider the m-DAG in Figure 2, which is a model of a simple two-time-point longitudinal study with
attrition. The variables A and A correspond to sequential treatment, X and X are the side effects,
1 2 1 2
and Y and Y model some health outcomes. The causal effect of interest is P(Y ;do(A ,A )), which is
1 2 2 1 2
the impact of the two sequential treatments on the outcome at the second study time point. We can see
that the partially observed variables X and X are causing their own missingness, which means that
1 2
the missingness mechanism is of the MNAR type. However, even in this case, it can be shown that the
causal effect of interest is recoverable using sequential factorization [3]. First, with the help of the IDC
algorithm, an expression for identifying the causal effect from the observable data is provided (for the
case as if there had been no missingness, which is indicated in terms of potential outcomes):
(cid:88)
P(YM=0;do(A ,A ))= P(YM=0|A ,A ,YM=0)×P(YM=0|A ).
2 1 2 2 1 2 1 1 1

## Y1

Note that the potential outcome notation (·)M=0 is explicitly used only for the variables observed incompletely. In the next step, it has to be decided on the recoverability of the two conditional distributions
P(YM=0|A ,A ,YM=0) and P(YM=0|A ).
2 1 2 1 1 1
P(YM=0|A ,A ,YM=0)=P(YM=0|A ,A ,YM=0,M =0,M =0) (Y ⊥⊥{M ,M }|A ,A ,Y )
2 1 2 1 2 1 2 1 Y1 Y2 2 Y1 Y2 1 2 1
=P(Y |A ,A ,Y ,M =0,M =0) (by consistency)

## 2 1 2 1 Y1 Y2


## P(Ym=0|A )=P(Ym=0|A ,M =0) (Y ⊥⊥M |A )


## 1 1 1 1 Y1 1 Y1 1

6

<!-- Page 7 -->

=P(Y |A ,M =0) (by consistency)

## 1 1 Y1

Formally, it is true that {A ,A ,Y } is the minimal set for which
1 2 1

## Y ⊥⊥ {X ,X }|A ,A ,Y .

2 1 2 1 2 1
Analogously, A is the minimal set for which holds
1

## Y ⊥⊥ X |A .

1 1 1
Further, P(Y |A ,A ,Y ) satisfies Y ⊥⊥ {M ,M }|A ,A ,Y , whereas for P(Y |A ) it holds that true
2 1 2 1 2 Y1 Y2 1 2 1 1 1
Y ⊥⊥ M |A . Then, applying the sequential factorization technique, both factors can be recovered as

## 1 Y1 1

P(Y |A ,A ,Y ,M = 0,M = 0) and P(Y |A ,M = 0), correspondingly.

## 2 1 2 1 Y1 Y2 1 1 Y1

This shows that the causal effect of interest can be recovered from the available data only, despite the
fact that the underlying missingness mechanism is MNAR.
After a causal effect of interest has been identified as a function of the observed data, (and after it has
been further ensured that and how it can be recovered in the presence of missing data), the causal effect
canbeestimatedusingthecommontechniques, e.g., (parametric)G-computation[20], inverseprobability
weighting [21, 22], or targeted maximum likelihood estimation (TMLE) [23].
3.2 Closed Missingness Mechanism
Next, an interesting special case of a missingness mechanism, which we refer to as closed missingness
mechanism, is discussed. We present the recoverability results for joint and conditional distributions
under the closed missingness mechanism.
Definition 1 (Closed missingness). Consider a c-DAG G with the node set V = {X ,X ,...,X },
c 1 2 n
|V| = n. Without loss of generality, assume that V = {X ,...,X } and V = {X ,...,X } for
o 1 k m k+1 n
some k ≤ n. The corresponding m-DAG consists of the set V, the missingness indicator variable set
M = {M ,...,M }, and possibly a variable set Z containing auxiliary variables that are causes of

## X

k+1

### Xn

missingness. The missingness mechanism is called closed if there is no path between any V ∈ V and any
i
M ∈ M, i ∈ {k+1,...,n}.

### Vi

In other words, the missingness mechanism is closed if only the auxiliary variables from Z are causes
of missingness. From a practical standpoint, this type of missingness mechanism is common in clinical,
epidemiological, and pharmacological studies. The variables of interest in these studies are often of
biological and medical nature (e.g., medication/therapy type, medication dose, blood values), whereas
the causes of missingness in such variables are typically related to external factors such as technical issues
with medical devices and the socioeconomic status of study participants.
Corollary 1. Consider an m-DAG G depicting a closed missing mechanism, and the general setting
as in Definition 1. The joint distribution P(V ,V ), and therefore also any marginal or conditional
o m
distribution, is recoverable from the available cases.
Proof. As there is no path between any V ∈ V,i ∈ {1,...,n}, and any M ∈ M, i ∈ {k +1,...,n}, V
i Vi i
and M are d-separated for any i without conditioning on any other variables, and therefore V ⊥⊥ M

### Vi i Vi

holds true.
NotethatthevariablesfromZmayalsobecompletelyandincompletelyobserved, orevenunobserved
or latent, but this plays no role for the variables of interest from the set V.
Theconceptofa‘closedmissingnessmechanism’canleadtoausefulpracticalruleofthumb,especially
under MNAR. If a researcher determines that missingness is likely caused by unmeasured factors, they
may initially conclude that the data are MNAR, making both imputation and available case analyses
invalid. However, by sketching a c-DAG and m-DAG (incorporating missingness indicators), if no arrows
7

<!-- Page 8 -->

are found from the c-DAG to the m-DAG, they can conclude that a available or complete case analysis is
valid, despite MNAR. Intuitively, if the causes of missing values are unrelated to the variables necessary
for identification, then relying solely on complete cases might be preferable to imputation.
Thisapproachunderscoresacrucialpracticalinsight: eveninthepresenceofMNAR,ifthemissingness
mechanism is closed, it does not impact the validity of complete case analysis. Thus, researchers can
confidentlyusecompletecasedatawhenthemissingnessindicatorsareisolatedfromtheprimaryvariables
of interest.
4 Data Analysis
4.1 Study setting, measurements and estimand
As described in Section 2, our data comes from the study of Bienczak et al. [9] and includes 125 children
with HIV who were enrolled in the CHAPAS-3 trial and treated with an efavirenz-based regimen. We
consider the trial’s follow-up visits at 6, 36, 48, 60, and 84 weeks.
Our scientific goal is to estimate causal concentration response-curves. That is, we are interested in
the counterfactual probability of a viral load (VL) > 100 copies/ml (which is considered to be a viral
failure) at 36 and 84 weeks if children had efavirenz concentrations (12h after dose) of x mg/L at each
follow-up visit, where x ranges from 0 to 10 mg/L. Missing data in the outcome (VL), efavirenz exposure
(EFV) and time-dependent confounders (weight, adherence) complicates this exercise.
Measured baseline variables include sex, age, the nucleoside reverse transcriptase inhibitors drug
(NRTI) component of the treatment regimen and weight. Moreover, we include knowledge on the
metabolism status (“genotype”, slow, intermediate, extensive) related to the single nucleotide polymorphisms in the CYP2B6 gene, which is relevant for metabolizing evafirenz and directly affects its concentration in the body. Additionally available data include knowledge on caregiver’s beliefs in the necessity
of medicine (BMQ, 24), as well as socio-economic indicators (SES). Measured follow-up variables are
weight, adherence (measured through memory caps, MEMS) and dose.
Clinical assessments were made at every visit, viral loads were measured at all time points except
week6, efavirenzlevelsweremeasuredatallassessmentsotherthanweek48, andassessmentofadherence
through MEMS primarily at weeks 36, 48 and 60 as both funding constraints and practical considerations
did not allow its consecutive implementation.
4.2 Development of the causal model
Figure 3 contains our proposed causal model. The causal graph contains 1) variables important for
identifyingtheeffectofinterest(i.e. theimpactofEFVonviralfailure,c-DAG,bottom). Wesummarized
2)clinician’sknowledgeonwhydataarepossiblymissinginam-DAGusingbinarymissingnessindicators
(top, pink shading) for relevant variables with missing data (EFV, elevated viral load (VL), adherence
(MEMS), weight). The corresponding non-parametric structural equation models are given in Appendix

## A.

4.2.1 c-DAG
The c-DAG summarizes our knowledge and assumptions, described in more detail in Schomaker et al.
[10]. Briefly, the primary cause of viral failure is subtherapeutic efavirenz concentration (EFV → VL ).
t t
The concentration itself depends on the administered dose (Dose → EFV ), adherence to treatment
t t
(MEMS → EFV ) and how fast the drug is cleared, determined - amongst other - by the 516G and
t t
983T polymorphisms in the CYP2B6 gene (Genotype → EFV ). Both weight and MEMS are assumed
t
to be time-dependent confounders. Co-morbidities (CoMo), which we defined to include tuberculosis,
pneumonia and other AIDS-defining events are reflected in the DAG, although they are expected to be
less frequent in our population, as children with active infections, those being treated for tuberculosis and
with severe laboratory abnormalities at screening, were not enrolled into the study, and most children
were in relatively good health (e.g. median CD4 cell percentage is 19%).
8

<!-- Page 9 -->

4.2.2 m-DAG
Main m-DAG (G ): The development of the missingenss causal model is a novel contribution of our
main
paper. Reasons for missing data were obtained from the trial team and the paediatricians. Those reasons
are represented by arrows leading into the missingness indicators and include i) technical issues with the
memory caps (e.g., broken containers) or in obtaining or analysing a blood sample (TI, unmeasured); ii)
missedvisits(MV),whicharelikelyrelatedtosocio-economicstatusofcaregivers(SES,measured),beliefs
and attitudes towards medicine (BMQ, measured) and other behavioural factors (BHV, unmeasured). As
almostallchildrendependontheircaregivertoarriveattheirappointment, weassumethatthechildren’s
age does not affect the probability of a missed visit.
Sensitivity of the main causal missingness model (G ): Although the clinicians did not
alt1
report any other possible reasons for missingness, we added another speculative reason for missed visits
to explore the implications of deviations from the assumed causal model: health status of the child,
captured indirectly through elevated viral load. This potential reason is represented by the blue dashed
arrows in the m-DAG (G ). In the discussion, we also mention another m-DAG (G ), where G
alt1 alt2 main
is extended with additional arrows SES → MEMS , t ∈ {6,36,48,60,84}.
t

## Bmq Ses Bhv


## Mv0 Mv6 Mv36 Mv48 Mv60 Mv84


## Mvl0 Mvl6 Mvl36 Mvl48 Mvl60 Mvl84

MWeight0 MWeight6 MWeight36 MWeight48 MWeight60 MWeight84

## Mefv6 Mefv36 Mefv48 Mefv60 Mefv84


## Mmems6 Mmems36 Mmems48 Mmems60 Mmems84


## Ti0 Ti6 Ti36 Ti48 Ti60 Ti84


## Vl0 Vl6 Vl36 Vl48 Vl60 Vl84


### Age


## Efv6 Efv36 Efv48 Efv60 Efv84


### Outcome

Genotype
c-DAG
Dose6 Dose36 Dose48 Dose60 Dose84
Intervention

### Sex

CoMo0 CoMo6 CoMo36 CoMo48 CoMo60 CoMo84

### Missingvalues

Weight0 Weight6 Weight36 Weight48 Weight60 Weight84
Missing. indicat.

## Nrti Mems6 Mems36 Mems48 Mems60 Mems84

Figure 3: m-DAG. Blue dashed arrows distinguish between G (without blue armain
rows) and G (with blue arrows). The subgraph below the gray dashed line
alt1
represents the corresponding c-DAG. Unmeasured variables are highlighted in gray.
Variable names: Sex - biological sex, Weight - body weight, Age - age (in years), VL - elevated viral load,
Dose - efavirenz dose administered, EFV - efavirenz concentration (12h after dose), NRTI - nucleoside reverse
transcriptase inhibitors drug, Genotype - metabolism status, MEMS - adherence to treatment (measured through
memory caps), CoMo - co-morbidities, MV - missed hospital visit, TI - technical issues (e.g., with blood samples
or memory caps), BMQ - beliefs and attitudes towards medicine, SES - socio-economic status of caregiver, BHV -
behavioural factors.
Followingtheintroducednotations,andundertheassumptionofG orG ,thesetsofcompletely
main alt1
and partially observed variables, auxiliary variables and missingness indicators are defined as follows:
• V = {Age,Genotype,Sex,NRTI,CoMo ,Dose }
o t t
• V = {MEMS ,Weight ,EFV ,VL }
m t t t t

## • M = {M ,M ,M ,M }

VLt Weightt EFVt MEMSt
9

<!-- Page 10 -->


## • Z = {Ti ,Mv ,Bmq,Ses,Bhv}.

t t
Note that under G (G with additional arrows SES → MEMS ), BHV becomes a part of the
alt2 main t
c-DAG.
4.3 Identifiability and Recoverability of Causal Effects
To make a decision on the recoverability of a causal query of interest, we first need to find out whether
the query is identifiable or not. Provided the identifiability holds true, the main idea of recoverability is
to transform the partially observed variables from the identified expression into observables with the help
of d-separation statements resulting from the m-DAG.
In this work, we aim to estimate the causal impact of the efavirenz drug concentration in the plasma
of children with HIV, measured and controlled over a specific time period, on viral failure.
Particularly, we focus on two causal effects,
θ :=P(VL =1; do(EFV :=a,EFV :=a)) (1)
36 36 6 36
and
θ :=P(VL =1;do(EFV :=a,EFV :=a,EFV :=a,EFV :=a,EFV :=a)), (2)
84 84 6 36 48 60 84
corresponding to the probability of viral failure after 36 and 84 weeks under a fixed intervention on the
plasma concentration of efavirenz drug at each previous up to current study time point. Note that for
assessmentofrecoverabilityofthecausaleffects,onlyvariablesfromthepreviousuptocurrentstudytime
point are considered, and we therefore focus on the corresponding subgraph of the ‘full’ m-DAG in Figure
3 containing the variables up to and including the 36-th study week when deciding about identifiability
and recoverability of θ .
36
We first consider the m-DAG G from Figure 3, ignoring the dashed blue lines from VL to MV ,
main t t
t ∈ {0,6,36,48,60,84}. Note that according to the taxonomy of the missingness mechanisms proposed by
Mohan et al. [4], the missingness is of MNAR type because TI , t ∈ {0,6,36,48,60,84}, are unobserved
t
variables directly causing missingness. Under Rubin’s definition the data would also be MNAR because
units may exhibit missing values due to unmeasured behavioral factors (BHV).
In the first step, we have to work on identifiability of the causal effect of interest. We carry this out
through two approaches. Our first proposal is the application of the IDC algorithm. Applying rules of
do-calculus therefore leads to the causal effect identifiable in terms of the observed data distribution as if
there were no missingness in any variable relevant for identification:
(cid:88)
θ = P(VL =1|Age,Sex,CoMo ,Weight ,Genotype,MEMS ,Weight ,Dose ,
36 36 0 0 6 6 6
Age,Sex,CoMo0,Weight0,

### VL0,CoMo6,VL6

EFV =a,VL ,CoMo ,VL ,MEMS ,Weight ,Dose ,EFV =a)
6 0 6 6 36 36 36 36
P(VL |Age,Sex,CoMo ,Weight ,Genotype,MEMS ,Weight ,
6 0 0 6 6 (3)
Dose ,EFV =a,VL )
6 6 0
P(CoMo |Age,Sex,CoMo ,Weight ,Genotype,VL )
6 0 0 0
P(Weight |Age,Sex)P(CoMo |Age,Sex)
0 0
P(Sex)P(Age)P(VL ).
0
The corresponding identifiability result for θ based on IDC algorithm is in Appendix B.1.
84
Theremaybeotheridentifiabilityresults,basedondifferentfactorizations. Forexample,inoursecond
proposal, we apply Pearl’s (generalized) back door-criterion to determine a sufficient adjustment set and
thensimplyapplyRobins’g-formulafactorizationtoit. Suchafactorizationmayinvolvemoreconditional
10

<!-- Page 11 -->

distributions that have to be estimated compared to the first approach. For the above estimand, θ , a
36
valid factorization would be as follows (see, e.g., Hern´an and Robins [25, Chapters 19 and 21]):
(cid:88)
θ = P(VL =1|EFV =a,EFV =a,Age,Genotype,Sex,NRTI,
36 36 6 36
Age,Genotype,Sex,NRTI,Weight0,VL0

### Weight6,MEMS6,Weight36,MEMS36

Weight ,Weight ,MEMS ,Weight ,MEMS ,VL ,VL )
0 6 6 36 36 0 6
P(Weight |EFV =a,Age,Genotype,Sex,NRTI,
36 6
VL ,VL ,Weight ,Weight ,MEMS ) (4)
0 6 0 6 6
P(MEMS |EFV =a,Age,Genotype,Sex,NRTI,
36 6
VL ,VL ,Weight ,Weight ,MEMS )
0 6 0 6 6
P(VL |EFV =a,Age,Genotype,Sex,NRTI,VL ,Weight )
6 6 0 0
P(Weight ,MEMS ,Age,Genotype,Sex,NRTI,VL ,Weight )
6 6 0 0
This is because neither the dose nor co-morbidities variables are necessarily required to block the
relevant back-door paths from EFV to VL , t∗ ≥ t, i.e. those back-door paths that do not go through
t t∗
any future concentrations.
Note that the identified expressions for θ and θ are identical under G and G because the
36 84 main alt1
c-DAG is identical in both situations. Under assumption of G , the c-DAG changes by addition of the
alt2
variable BHV, resulting in a slight change of the identified expression (see Appendix C.2).
In the second step, we need to decide on the recoverability of the identified expression in terms of the
observed data. Note that the missingness mechanism depicted in G refers to the closed missingness
main
mechanism introduced in the previous section. In this case, there is no path between any variable from
the c-DAG containing the variables of interest and the set of missingness indicators M and their causes.
Therefore, both causal effects are recoverable, and an available case analysis is admissible in this situation. In order to provide a better intuition about how to decide on the recoverability of a causal effect,
we present the recoverability result for θ in Appendix C.1, implicitly referring to a situation for which
36
no recoverability result exists, and it has to be decided on recoverability manually.
If the m-DAG G reflects relationships in the data correctly, then an available case analysis is
main
sufficient for estimating the causal effects of interest consistently. However, it is also necessary to assess
theplausibilityofthegraphstructureassumption. Asuggestionwouldbetoperformasensitivityanalysis
to investigate the recoverability of the causal effects θ and θ under the assumption of an alternative
36 84
m-DAG which is eligible in terms of content. Therefore, we consider another m-DAG, G , which is
alt1
depicted in Figure 3 when including the dashed blue lines from VL to MV , t ∈ {0,6,36,48,60,84}.
t t
The arrows from VL (binary variable elevated viral load) to MV (binary variable missed visit) for the
t t
respective measurement time point reflect the speculation that children with viral failure may miss their
appointments due to their poor health condition.
We first investigate the recoverability of θ under the assumption of G being the true underlying
36 alt1
m-DAG. Note that if at least one of the conditional distributions in Equation 3 is non-recoverable, we
conclude the non-recoverability of the causal query of interest.
We first focus on the second last conditional distribution in Equation 3 which involves the partially
observeddata,P(VL |EFV = a,Age,Genotype,Sex,NRTI,VL ,Weight ),andthegoalistocondition
6 6 0 0
on M = 0, M = 0, M = 0 and M = 0. From the m-DAG (assuming faithfulness), we

### Weight0 VL0 EFV6 VL6

know that VL ⊥⊥ (M ,M ,M ,M )|(MV ,MV ) (and we always need to condition on (at
6 Weight0 VL0 EFV6 VL6 0 6
least) MV and MV to achieve (conditional) independence), which in turn leads to
0 6
P(VLM=0|EFVM=0 =a,Age,Genotype,Sex,NRTI,VLM=0,WeightM=0)
6 6 0 0
(cid:88)
= P(VLM=0|EFVM=0 =a,Age,Genotype,Sex,NRTI,VLM=0,WeightM=0)×
6 6 0 0

## Mv0,Mv6

P(MV ,MV |EFVM=0 =a,Age,Genotype,Sex,NRTI,VLM=0,WeightM=0)
0 6 6 0 0
(cid:88)
= P(VLM=0|EFVM=0 =a,Age,Genotype,Sex,NRTI,VLM=0,WeightM=0,
6 6 0 0

## Mv0,Mv6

11

<!-- Page 12 -->


## M =0,M =0,M =0,M =0)×


### Weight0 VL0 EFV6 VL6

P(MV ,MV |EFV =aM=0,Age,Genotype,Sex,NRTI,VLM=0,WeightM=0)
0 6 6 0 0
(cid:88)
= P(VL |EFV =a,Age,Genotype,Sex,NRTI,VL ,Weight ,
6 6 0 0

## Mv0,Mv6


## M =0,M =0,M =0,M =0)×


### Weight0 VL0 EFV6 VL6

P(MV ,MV |EFV =aM=0,Age,Genotype,Sex,NRTI,VLM=0,WeightM=0).
0 6 6 0 0

### The second factor in the expression above,

P(MV ,MV |EFVM=0 =a,Age,Genotype,Sex,NRTI,VLM=0,WeightM=0),
0 6 6 0 0
cannot be further decomposed following the adjustment formula, as among others we would need MV to
6
be conditionally independent of M (possibly given some other variables), but there is no such subset

## Efv6

because MV is a parent of M .

## 6 Efv6

Because other available recoverability techniques, like sequential factorization or R factorization [3],
are not applicable in our case, we conclude that the conditional distribution cannot be expressed in
terms of the observed data distribution only; this results in non-recoverability of θ . Based on the same
36
arguments, non-recoverability of θ also follows.
84
4.4 Analysis
The analysis is conducted using the m-DAG G from Figure 3 and the study data described in Section
main

### The plug-in g-formula estimation (see, e.g., Hernan and Robins [25, Chapter 13]) of our estimands 1

and 2 was based on equations 4 and 6, respectively. Given the recoverability under G , we conduct
main
the analysis based on available cases. For modeling the respective conditional distributions, between 69
and 85 complete observations are available.
Note that in our setting, relevant co-morbidities in the DAG refer to AIDS-defining events, including
tuberculosis, persistent diarrhea, malnutrition, and severe wasting, among others. Most of those events
were not measured regularly in our study and thus were not included in the analysis. However, those
co-morbidities are not expected to be very frequent in the study population. This is because children
with active infections, those being treated for tuberculosis and with severe laboratory abnormalities at
screening, were not enrolled into the study, and most children were in relatively good health [8]. Also,
not all valid identification formulae require information on them, such as those used in our analysis.
As adherence could not be measured regularly, as explained in Section 4.1, we constructed a variable
indicating any signs of non-adherence, defined as the mean memory caps opening percentage being less
than 90%.
Although the main analysis was based on available cases due to the identification results, we also
implemented a multiple imputation analysis. We consider the results of the multiple imputation analysis
invalid because the underlying missingness mechanism is assumed to be MNAR. This is primarily due to
the unobserved variables (TI ), which directly cause missingness in variables from the c-DAG.
t
WemultiplyimputedfivedatasetsusingtheExpectation-MaximizationBootstrap(EMB)Algorithm,
a joint modeling-based imputation approach implemented in the R-package Amelia II. Our setup considered the longitudinal setup through lag-variables and the inclusion of splines of time. Additionally, to
improve numerical stability of the EM algorithm, we added a ridge prior (which shrinks the covariances
among the variables toward zero without changing the means or variances). This is often recommended
when using EMB on small samples [26]. To address the fact that age, weight and EFV concentrations
can not have negative or other illogical values, we specified lower and upper bounds for those variables
in the EMB algorithm: 0 and 35 for EFV, 0 and 3 for log age and 2 and 4 for log weight. Amelia
II implements these bounds by rejection sampling: when drawing the imputations from the respective
posterior distributions, all logical constraints need to be satisfied; otherwise, imputations are redrawn
until those constraints are met.
The results of our analyses are presented in Figures 4a and 4b.
12

<!-- Page 13 -->

0.5
0.4
0.3
0.2
0.1
0.0
0.0 2.5 5.0 7.5 10.0
Efavirenz Mid−Dose Concentrations (mg/L),
intervened on at each time point
skeew
63
retfa
daoL
lariV
detavelE
0.5
0.4
0.3
0.2
0.1
0.0 2.5 5.0 7.5 10.0
Efavirenz Mid−Dose Concentrations (mg/L),
intervened on at each time point
(a) θ under G
36 main
skeew
48
retfa
daoL
lariV
detavelE
(b) θ under G
84 main
Figure 4: Estimated CCRCs for θ and θ under m-DAG G . (a) Estimated CCRCs for θ . (b)
36 84 main 36
Estimated CCRCs for θ . Causal effects were estimated using available cases (blue squares) and multiple
84
imputation, mean over 20 imputed data sets (red dots); results represent the mean over 1000 seeds.
One can see a higher probability of viral failure with lower EFV concentration values, independent of
the approach employed to address the missing data. Using the suggested available cases approach, the
probability of failure is estimated to be > 50% at both 36 and 84 weeks if concentrations were 0mg/L,
e.g. if patients did not take any medications. With higher concentrations, failure probabilities decrease to
below 5%, which is expected as EFV is expected to be a potent drug. Interestingly, the CCRCs estimated
using multiple imputation are much flatter than under the available case approach, both for θ and θ .
36 84
We will now explore the derived theoretical results, along with comparisons between the available case
and multiple imputation approaches in the simulation studies below.
5 Simulation Studies
In this section, through simulation studies, we assess the reliability of CCRC estimates for θ in the
84
presence of missing data. We compare true CCRC values with estimates derived from: (i) an ideal
scenario with no missing data (complete data analysis), (ii) available case analysis, and (iii) multiple
imputation.
5.1 Setup
The data were simulated using the R-package simcausal [27], which is a powerful and flexible tool for
simulation of longitudinal data structures based on structural causal models. A structural causal model
(SCM) uniquely imposes a causal graph, allowing data structures to be generated according to such a
causal DAG (in our case, an m-DAG).
Simulation1: Wesimulatedatacorrespondingtobothm-DAGs,G andG ,asdefinedinFigure
main alt1

## We first simulate binary and normally distributed confounder sets, a continuous (truncated normally

distributed) intervention and a binary outcome for all 6 time points and for the sample size of n = 5.000.
This way, the data aligning with the c-DAG is simulated. Afterwards, we simulate the binary variables
causing missingness (SES (as proxy for BMQ , SES and BHV ), MV and TI , t ∈ {0,6,36,48,60,84}.
t t t t t t
Based on these variables, we simulate the missingness indicators for VL , t ∈ {0,6,36,48,60,84}, and
t
MEMS , t ∈ {6,36,48,60,84}. In this scenario, we assume that only these two variables (for all time
t
points) are subject to missing data.
Simulation 2: The DGP is the same as for Simulation 1, but we simulate missingness indicators for
13

<!-- Page 14 -->

many more variables: VL , Weight , t ∈ {0,6,36,48,60,84}, and MEMS , EFV , t ∈ {6,36,48,60,84}.
t t t t
This scenario mostly coincides with the GPD induced by Figure 3. This scenario introduces another layer
of complexity because the distribution of EFV , t ∈ {6,36,48,60,84} is non-symmetric and complex. Ust
ing a parametric imputation model with slightly misspecified distributional assumptions may introduce
some bias. This setting serves as a benchmark for a realistic scenario where missing data with somewhat
complex distributions are imputed using parametric assumptions in conjunction with predictive mean
matching (fully conditional imputation procedures, like (M)ICE), or variations thereof (joint modeling,
as in Amelia II which we use below).
The exact model specifications are given in Appendix D.1. Based on the DGP, we first simulate the
interventional data (1000 repetitions) and compute the true CCRC based on it. We intervene on EFV at
time points 6,36,48,60, and 84, considering a sequence of interventions from 0 up to 10 mg/L with steps
of 0.5 mg/L. Next, the CCRC is estimated using the g-formula factorization provided in Appendix B.1,
once on the complete data and once on the available case data. Compared to the widely used complete
case analysis, which relies on samples where all variables in the data set are observed, the available
case analysis retains all samples where variables in the query of interest (for the g-formula, the variables
required for the estimation of the conditional distribution of interest) are observed. For this reason,
an available case analysis is preferred over a complete case analysis due to a more economical usage of
available data [3]. Finally, the CCRC is estimated using multiple imputation (MI) and the g-formula.
5.2 Results
0.4
0.2
0.0
0.0 2.5 5.0 7.5 10.0
Efavirenz Mid−Dose Concentrations (mg/L), intervened on at each time point
skeew
48
retfa
daoL
lariV
detavelE
0.4
0.2
0.0
0.0 2.5 5.0 7.5 10.0
Efavirenz Mid−Dose Concentrations (mg/L), intervened on at each time point
(a) Data simulated under the main DAG G
main
skeew
48
retfa
daoL
lariV
detavelE
(b) Data simulated under the alternative DAG G
alt1
Figure 5: Estimated CCRCs for the probability of viral failure after 84 weeks. (a) Data simulated
under the main DAG G . (b) Data simulated under the alternative DAG G . Causal effects were
main alt1
estimated on complete data (black squares), incomplete data using available cases (blue dots), incomplete
data using multiple imputation (red triangles) and counterfactual data (green diamonds, true CCRC);
results represent the mean over 1000 seeds.
Below, we focus on the results from Simulation 1. The results of the Simulation 2are presented in
Appendix D.2, specifically in Figures 6a and 6b.
The simulation results align with the theoretical findings. We first consider the estimated CCRC
curve for elevated viral load after 84 weeks based on data simulated under G , as presented in Figure
main
5a. According to the findings in Section 4, the missingness mechanism is of MNAR type. Despite this,
the causal query of interest, θ , remains recoverable, allowing for consistent estimation of the CCRC via
84
an available case analysis. Conversely, the MI approach is inadmissible due to its underlying assumption of Missing At Random (MAR), which is not met because of the partially observed variables TI ,
t
t ∈ 0,6,36,48,60,84, that affect the probability of missingness in variables from V . The estimated
m
14

<!-- Page 15 -->

counterfactual outcomes, illustrated in Figure 5a, represent the mean estimated values across 1000 simulation repetitions. It is evident that the CCRC estimates from available case analysis (dashed blue line)
match the true CCRC (dashed green line), whereas those derived from MI differ markedly. To determine whether the discrepancies represent a bias or could also be explained by simulation uncertainty,
we calculated Monte Carlo confidence intervals for the differences between the MI estimation results and
the true causal effects θ . The results are reported in Table 1a and show that for each EFV value, the
84
estimated differences are significantly different from zero. This discrepancy underscores the theoretical
findings regarding the bias introduced by MI due to the MNAR missingness mechanism.
Secondly, consider the results under the alternative DAG G , presented in Figure 5b. In this case,
alt1
the causal query of interest is non-recoverable. The results confirm this and demonstrate that neither
the available case analysis (dashed blue line) nor the MI estimates (dashed red line) align with the true
CCRC (dashed green line). The respective Monte Carlo confidence intervals, see Tables 1b and 1c in
the appendix, show that these differences cannot be explained by simulation uncertainty alone, which is
consistent with the theoretical findings.
ThesefindingshighlightthecriticalneedtoscrutinizethecommonMAR-typemissingnessassumption,
especially in complex longitudinal data scenarios where multiple variables experience missingness. Our
simulation study illustrates how even minor changes in the missingness structure can dramatically affect
recoverability and, consequently, the accuracy of estimation results. This emphasizes the importance of
careful consideration and justification of missingness assumptions in such analyses.
6 Conclusions
Our analyses demonstrate the applicability of missingness DAGs to complex longitudinal studies and
show that, in some cases, available case analyses can be valid under MNAR. However, our application
also highlights the massive effort involved, the technical expertise required, and sensitivity of results to
the assumed causal model.
Under the assumptions represented in Figure 3, the data are missing not at random (MNAR) because
technical issues (TI) with pill containers (frequently) and blood samples (rarely), which we assume to
be direct causes of missingness in multiple variables, have not been measured. However, we show that
these assumptions are sufficient to estimate the desired impact using the available data and g-formula
representations, despite the MNAR mechanism. However, if reasons for missed visits are caused by
the outcome (elevated viral load), as speculated in the alternative DAG, the causal effect cannot be
recovered. Interestingly, additional simulations (Appendix D.2, Figure 7) show that recoverability holds
true even if behavioural factors directly cause non-adherence. This corresponds to the situation discussed
in the second alternative DAG, G . However, it is possible that more complex processes exist between
alt2
socio-economic/behavioural factors and biologic processes, for which identifiability does not hold. Our
investigationsdemonstratethesensitivityofrecoverabilityresultstoevenminorchangesinthemissingness
structure. We therefore emphasize the need for careful inspection of the assumptions regarding the
missing data mechanism, especially in complex longitudinal studies with multiple variables experiencing
missingness.
It is also important to highlight that the estimated concentration-response curves are much flatter
when using multiple imputation and are actually invalid under the assumptions stated in Figure 3, as
predicted by theory and confirmed by our simulations.
Our analyses show lower probabilities of viral failure with higher concentrationsafter accounting for
the missing data. There are, of course, many further complications that may have to be considered for
accurate causal inference in our setting. First, one may also account for measurement error, e.g. in viral
load and EFV concentrations [28], though this may not affect our binary viral failure definition very
much. Second, it would be advantageous if measurements were available more frequently and precisely,
especially for measuring actual adherence to the prescribed treatment plan, which is difficult in practice.
While advancements in causal modeling and appropriate statistical estimation techniques are impressive, answering complex epidemiological and biological questions remains a challenge.
15

<!-- Page 16 -->


### Acknowledgements

We are grateful for the support of the CHAPAS-3 trial team, their advice regarding the data analysis
and making their data available to us. We would like to thank David Burger, Sarah Walker, Di Gibb
and Andrzej Bienczak for their help in interpreting the data. We thank Elizabeth Kaudha and Victor
Musiime for discussing reasons for missingness with us. We would further like to acknowledge the help of
Alexander Szubert in constructing some of the variables. Michael Schomaker is supported by the German
Research Foundations (DFG) Heisenberg Programm (grants 465412241 and 465412441). The CHAPAS-3
trial was funded by the European Developing Countries Clinical Trials Partnership (IP.2007.33011.006),
Medical Research Council UK (MC UU 00004/03), Department for International Development UK, and
Ministerio de Sanidady Consumo Spain. Cipla Ltd donated first-line antiretrovirals. We thank all the
children, carers, and staff from all the centres participating in the CHAPAS-3 trial.

### References

[1] Donald B. Rubin. Inference and missing data. Biometrika, 63(3):581–592, 1976. ISSN 00063444. URL http://www.
jstor.org/stable/2335739.
[2] Karthika Mohan and Judea Pearl. Graphical models for recovering probabilistic and causal queries from missing data.
InZ.Ghahramani,M.Welling,C.Cortes,N.Lawrence,andK.Q.Weinberger,editors,Advances in Neural Information
Processing Systems, volume 27. Curran Associates, Inc., 2014. URL https://proceedings.neurips.cc/paper/2014/
file/31839b036f63806cba3f47b93af8ccb5-Paper.pdf.
[3] Karthika Mohan and Judea Pearl. Graphical models for processing missing data. Journal of the American Statistical Association, 116(534):1023–1037, 2021. doi: 10.1080/01621459.2021.1874961. URL https://doi.org/10.1080/
01621459.2021.1874961.
[4] Karthika Mohan, Judea Pearl, and Jin Tian. Graphical models for inference with missing data. In C.J. Burges,
L. Bottou, M. Welling, Z. Ghahramani, and K.Q. Weinberger, editors, Advances in Neural Information Processing Systems, volume 26. Curran Associates, Inc., 2013. URL https://proceedings.neurips.cc/paper/2013/file/
0ff8033cf9437c213ee13937b1c4c455-Paper.pdf.
[5] Margarita Moreno-Betancur, Katherine J Lee, Finbarr P Leacy, Ian R White, Julie A Simpson, and John B Carlin.
Canonical Causal Diagrams to Guide the Treatment of Missing Data in Epidemiologic Studies. American Journal of
Epidemiology, 187(12):2705–2715, 08 2018. ISSN 0002-9262. doi: 10.1093/aje/kwy173. URL https://doi.org/10.
1093/aje/kwy173.
[6] Laura B Balzer, Mark van der Laan, James Ayieko, Moses Kamya, Gabriel Chamie, Joshua Schwab, Diane V
Havlir, and Maya L Petersen. Two-Stage TMLE to reduce bias and improve efficiency in cluster randomized trials. Biostatistics, 24(2):502–517, 12 2021. ISSN 1465-4644. doi: 10.1093/biostatistics/kxab043. URL https:
//doi.org/10.1093/biostatistics/kxab043.
[7] Joshua R. Nugent, Carina Marquez, Edwin D. Charlebois, Rachel Abbott, and Laura B. Balzer. Blurring cluster
randomized trials and observational studies using two-stage tmle to address sub-sampling, missingness, and minimal
independent units, 2023. URL https://arxiv.org/abs/2208.09508.
[8] Veronica Mulenga, Victor Musiime, Adeodata Kekitiinwa, Adrian D. Cook, George Abongomera, Julia Kenny, Chisala
Chabala, Grace Mirembe, Alice Asiimwe, Ellen Owen-Powell, David Burger, Helen McIlleron, Nigel Klein, Chifumbe
Chintu, Margaret J. Thomason, Cissy Kityo, A. Sarah Walker, and Diana Gibb. Abacavir, zidovudine, or stavudine
as paediatric tablets for african hiv-infected children (chapas-3): an open-label, parallel-group, randomised controlled
trial. The Lancet Infectious Diseases, 16(2):169–79, 2016.
[9] Andrzej Bienczak, Paolo Denti, Adrian Cook, Lubbe Wiesner, Veronica Mulenga, Cissy Kityo, Addy Kekitiinwa, Diana M. Gibb, David Burger, A. Sarah Walker, and Helen McIlleron. Plasma efavirenz exposure, sex, and age predict
virologicalresponseinhiv-infectedafricanchildren. Journal of Acquired Immune Deficiency Syndromes,73(2):161–168,

## URL <GotoISI>://MEDLINE:27116047.

[10] M.Schomaker,H.McIlleron,P.Denti,andI.D`ıaz. Causalinferencewithcontinuousmultipletimepointinterventions.
arXiv e-prints, https://arxiv.org/abs/2305.06645, 2023.
[11] Joseph L. Schafer and John W. Graham. Missing data: our view of the state of the art. Psychological methods, 7 2:
147–77, 2002.
16

<!-- Page 17 -->

[12] Jin Tian. Missing at Random in Graphical Models. In Guy Lebanon and S. V. N. Vishwanathan, editors, Proceedings
oftheEighteenthInternationalConferenceonArtificialIntelligenceandStatistics,volume38ofProceedingsofMachine
Learning Research,pages977–985,SanDiego,California,USA,09–12May2015.PMLR. URLhttps://proceedings.
mlr.press/v38/tian15.html.
[13] Shaun Seaman, John Galati, Dan Jackson, and John Carlin. What is meant by “missing at random”? Statistical
Science, 28(2), may 2013. doi: 10.1214/13-sts415. URL https://doi.org/10.1214%2F13-sts415.
[14] Judea Pearl and Thomas S Verma. Equivalence and synthesis of causal models. In Proceedings of the 6th Conference
on Uncertainty in Artificial Intelligence, pages 220–227. Elsevier, 1990.
[15] Michael Schomaker. Regression and causality, 2020. URL https://arxiv.org/abs/2006.11754.
[16] Judea Pearl. Causality. Cambridge University Press, 2 edition, 2009. doi: 10.1017/CBO9780511803161.
[17] Jin Tian and Judea Pearl. A general identification condition for causal effects. In Eighteenth National Conference on
Artificial Intelligence, page 567–573, USA, 2002. American Association for Artificial Intelligence. ISBN 0262511290.
[18] Ilya Shpitser and Judea Pearl. Identification of joint interventional distributions in recursive semi-markovian causal
models. InProceedingsofthe21stNationalConferenceonArtificialIntelligence-Volume2,AAAI’06,page1219–1226.
AAAI Press, 2006. ISBN 9781577352815.
[19] Santtu Tikka and Juha Karvanen. Identifying causal effects with the R package causaleffect. Journal of Statistical
Software, 76(12):1–30, 2017. doi: 10.18637/jss.v076.i12.
[20] James Robins. A new approach to causal inference in mortality studies with a sustained exposure period—application
to control of the healthy worker survivor effect. Mathematical Modelling, 7(9):1393–1512, 1986. ISSN 0270-0255.
doi: https://doi.org/10.1016/0270-0255(86)90088-6. URL https://www.sciencedirect.com/science/article/pii/
0270025586900886.
[21] Miguel Herna´n and James Robins. Estimating causal effects from epidemiologic data. Journal of epidemiology and
community health, 60:578–86, 08 2006. doi: 10.1136/jech.2004.029496.
[22] M. Hernan and J. Robins. Causal inference. Chapman & Hall/CRC, Boca Raton, 2020. URL https://www.hsph.
harvard.edu/miguel-hernan/causal-inference-book/.
[23] M.J.vanderLaanandS.Rose. TargetedLearning: CausalInferenceforObservationalandExperimentalData. Springer
Series in Statistics. Springer New York, 2011. ISBN 9781441997821. URL https://books.google.de/books?id=
RGnSX5aCAgQC.
[24] G.Abongomera,A.Cook,V.Musiime,C.Chabala,M.Lamorde,J.Abach,M.Thomason,V.Mulenga,A.Kekitiinwa,
R.Colebunders,C.Kityo,A.S.Walker,D.M.Gibb,andCHAPAS-3TrialTeam. Improvedadherencetoantiretroviral
therapy observed among hiv-infected children whose caregivers had positive beliefs in medicine in sub-saharan africa.
Aids and Behavior, 21(2):441–449, 2017.
[25] MA Herna´n and JM Robins. Causal Inference: What If. Chapman & Hall/CRC, Boca Raton, 2020.
[26] J. Honaker, G. King, and M. Blackwell. Amelia ii: A program for missing data. Journal of Statistical Software, 45(7):
1–47, 2011.
[27] Oleg Sofrygin, Mark J. van der Laan, and Romain Neugebauer. simcausal R package: Conducting transparent and reproduciblesimulationstudiesofcausaleffectestimationwithcomplexlongitudinaldata. JournalofStatisticalSoftware,
81(2):1–47, 2017. doi: 10.18637/jss.v081.i02.
[28] M.Schomaker,S.Hogger,L.F.Johnson,C.J.Hoffmann,T.Barnighausen,andC.Heumann. Simultaneoustreatment
of missing data and measurement error in hiv research using multiple overimputation. Epidemiology, 26(5):628–636,
2015.
17

<!-- Page 18 -->


### A Structural equation model

We now present the non-parametric structural equation models (SEMs) corresponding to the m-DAGs
in Figure 3. Note that the follow-up time points 1 through 5 coincide with the study weeks 6, 36, 48, 60
and 84. The independent (joint) noise term is denoted as U.
The SEM corresponding to G in Figure 3 is as follows:
main

### Fort=0:

Genotype = fGenotype(Sex,UGenotype)
Weight = f (Sex,Age,U )
0 Weight0 Weight0

### NRTI0 = fNRTI(Age,UNRTI)

MV0 = fMV0 (BMQ,SES,BHV,UMV0 )

### Fort=1:

Dose1 = fDose1 (Weight
1
,UDose1 )
Fort≥0:

## M


### Weightt

= fMWeightt (MVt,UMWeightt )
MVLt = fMVLt (MVt,TIt,UMVLt )

### Fort≥1:

MEMSt = fMEMSt (CoMot−1,MEMSt−1,UMEMSt ) [assumeMEMS0=0]
Weight
t
= f
Weightt
(Weight
t−1
,CoMot−1,U
Weightt
)
CoMot = fCoMot (CoMot−1,Age,Weight
t−1
,VLt−1,UCoMot )
EFVt = fEFVt (Doset,MEMSt,Genotype,UEFVt )
VLt = fVLt (VLt−1,CoMot−1,EFVt,UVLt )

### MVt = fMVt (BMQ,SES,BHV,UMVt )

MEFVt = fMEFVt (MVt,TIt,UMEFVt )
MMEMSt = fMMEMSt (TIt,UMMEMSt )

### Fort≥2:

Doset = fDoset (Doset−1,Weight
t
,UDoset )
The SEM for G (with present blue dashed lines in Figure 3) is the same as the SEM above, except
alt1
for the structural equations for MV , t ∈ {0,6,36,48,60,84}. These are specified as follows for G :
t alt1

### Fort=0:

MV0 = fMV0 (BMQ,SES,BHV,VL0,UMV0 )

### Fort≥1:


### MVt = fMVt (BMQ,SES,BHV,VLt,UMVt )

This way, MV additionally depends on VL , t ∈ {0,6,36,48,60,84}, which corresponds to the dashed
t t
blue lines in the DAG.
18

<!-- Page 19 -->


### B Identifiability results

B.1 Identifiability results for θ
84
The identifiability result below is based on application of the IDC algorithm [18].
(cid:88)
θ = P(VL =1|Age,Sex,CoMo ,Weight ,Genotype,MEMS ,Weight ,
84 84 0 0 6 6

### Age,Sex,CoMo0,Weight0,


### MEMS6,Weight6,VL0,CoMo6,


### VL6,MEMS36,Weight36,CoMo36,

MEMS48,Weight48,VL36,CoMo48,

### VL48,CoMo60,VL60

Dose ,EFV =a,VL ,CoMo ,VL ,MEMS ,
6 6 0 6 6 36
Weight ,CoMo ,Dose ,MEMS ,Weight ,EFV =a,
36 36 36 48 48 36
Dose ,VL ,EFV =a,CoMo ,VL ,MEMS ,Weight ,CoMo ,
48 36 48 48 48 60 60 60
Dose ,MEMS ,Weight ,EFV =a,Dose ,VL ,EFV =a)
60 84 84 60 84 60 84
P(VL |Age,Sex,CoMo ,Weight ,Genotype,MEMS ,Weight ,
60 0 0 6 6
Dose ,EFV =a,VL ,CoMo ,VL ,MEMS ,
6 6 0 6 6 36
Weight ,CoMo ,Dose ,MEMS ,Weight ,EFV =a,Dose ,
36 36 36 48 48 36 48
VL ,EFV =a,CoMo ,VL ,MEMS ,Weight ,Dose ,EFV =a)
36 48 48 48 60 60 60 60
P(CoMo |Age,Sex,CoMo ,Weight ,Genotype,MEMS ,Weight ,
60 0 0 6 6
Dose ,Dose ,EFV =a,VL ,CoMo ,VL ,MEMS ,Weight ,CoMo ,
36 6 6 0 6 6 36 36 36
MEMS ,Weight ,EFV =a,Dose ,VL ,EFV =a,CoMo ,VL )
48 48 36 48 36 48 48 48
P(VL |Age,Sex,CoMo ,Weight ,Genotype,MEMS ,Weight ,Dose ,
48 0 0 6 6 6
EFV =a,VL ,CoMo ,VL ,MEMS ,Weight ,CoMo ,Dose ,
6 0 6 6 36 36 36 36
MEMS ,Weight ,EFV =a,Dose ,VL ,EFV =a)
48 48 36 48 36 48
P(CoMo |Age,Sex,CoMo ,Weight ,Genotype,MEMS ,Weight ,
48 0 0 6 6
Dose ,EFV =a,VL ,CoMo ,VL ,MEMS ,
6 6 0 6 6 36
Weight ,CoMo ,Dose ,EFV =a,VL )
36 36 36 36 36
P(Weight |Age,Sex,CoMo ,Weight ,Genotype,MEMS ,Weight ,
48 0 0 6 6
Dose ,EFV =a,VL ,CoMo ,VL ,Weight ,CoMo )
6 6 0 6 6 36 36
P(MEMS |Age,Sex,CoMo ,Weight ,Genotype,MEMS ,Weight ,
48 0 0 6 6
Dose ,EFV =a,VL ,CoMo ,VL ,MEMS ,CoMo )
6 6 0 6 6 36 36
P(CoMo |Age,Sex,CoMo ,Weight ,Genotype,MEMS ,Weight ,
36 0 0 6 6
Dose ,EFV =a,VL ,CoMo ,VL )
6 6 0 6 6
P(VL |Age,Sex,CoMo ,Weight ,Genotype,MEMS ,Weight ,Dose ,
36 0 0 6 6 6
EFV =a,VL ,CoMo ,VL ,MEMS ,Weight ,Dose ,EFV =a)
6 0 6 6 36 36 36 36
P(Weight |Age,Sex,CoMo ,Weight ,Genotype,Weight ,
36 0 0 6
VL ,CoMo )P(MEMS |Age,Sex,CoMo ,Weight ,Genotype,MEMS ,
0 6 36 0 0 6
VL ,CoMo )P(VL |Age,Sex,CoMo ,Weight ,Genotype,
0 6 6 0 0
MEMS ,Weight ,Dose ,EFV =a,VL )
6 6 6 6 0
P(CoMo |Age,Sex,CoMo ,Weight ,Genotype,VL )
6 0 0 0
P(Weight |Age,Sex,CoMo ,Weight )P(MEMS |CoMo )
6 0 0 6 0
P(Weight |Age,Sex)P(CoMo |Age,Sex)P(VL )P(Sex)P(Age)
0 0 0
(5)
An alternative identifiability result can be obtained, for example, by applying the generalized backdoor criterion. This results in using an adjustment set given by the confounders weight and adherence
(MEMS). Both dose and co-morbidities are not necessarily required to block the relevant back-door paths
from EFV to VL , t∗ ≥ t, i.e. the back-door paths that do not pass through any future concentrations
t t∗
[25]. Applying Robins’ parametric g-formula [20, 25] leads to the following valid g-formula factorization:
19

<!-- Page 20 -->

(cid:40)
(cid:90)
θ = P(VL =1|A¯ =a¯ ,L¯ =¯l )
84 84 84 84 84 84
l
84 (cid:41)
× (cid:89) f(L =l |A¯ =a¯ ,L¯ =¯l ) dF (l), (6)
s s s−1 s−1 s−1 s−1 l
s=0
where F (·) denotes the CDF with respect to L. In the above, L = {weight ,MEMS }, L =

### L t t t 0

{weight ,NRTI,Genotype,Sex,Age}andA = EFV . Notethattheoverbarreferstotheinterventionand
0 t t
confounder histories, i.e. for of a unit i (up to and including time t) the histories areA¯ = (A ,...,A )
t,i 0,i t,i
and L¯s = (Ls ,...,Ls ), s = 1,2, i = 1,...,n, respectively. Outcomes (i.e., VL) prior to s are part of
t,i 0,i t,i
L¯ . The inner product of the 2 time-varying and ordered confounders L = {L1,L2} can be decomposed
s s s s
further:
84
(cid:89) f(L2 =l2 |L1 =l1,A¯ =a¯ ,L¯ =¯l )×f(L1 =l1 |A¯ =a¯ ,L¯ =¯l )
s s s s s−1 s−1 s−1 s−1 s s s−1 s−1 s−1 s−1
s=0
Thus, implementing (6), requires fitting models for the outcome and two confounder distributions at
each time point, given their respective history.
C Recoverability results for θ
36
C.1 Assuming G
main
To assess the recoverability of the identified causal effect θ in Equation 3, we must show that each of
36
the multiplicative factors corresponding to the conditional or marginal distributions can be expressed in
terms of the observed data only. Although the missingness mechanism is of the ‘closed’ type, and the
recoverability result is directly available for this case, we want to demonstrate how one would examine
identifiability if such a result is not available. T do so, we present the result for one of the conditional
distributions containing partially observed variables. The results for other multiplicative factors are
derived analogously.
P(CoMoM=0|Age,Sex,CoMoM=0,WeightM=0,Genotype,VLM=0)
6 0 0 0
=P(CoMoM=0|Age,Sex,CoMoM=0,WeightM=0,Genotype,VLM=0,M=0)
6 0 0 0
=P(CoMo |Age,Sex,CoMo ,Weight ,Genotype,VL ,M=0)
6 0 0 0
The first equality holds due to the fact that all partially observed variables are independent of the
corresponding relevant missingness indicators, whereas the second equality is true due to the consistency
assumption [5].
Note that the recoverability result above is trivial due to the specific missingness mechanism. In a
general case, much more effort is required to recover a distribution of interest.
C.2 Assuming G
alt2
We consider a second plausible alternative m-DAG, G , which is equivalent to G in Figure 3, with
alt2 main
the addition of a direct effect of BHV on MEMS for weeks 6, 36, 48, 60 and 84. In this model, we
propose that behavioural pattern may affect adherence.
20

<!-- Page 21 -->

Under G , the identified expression for the causal effect of interest, θ , is as follows:
alt2 36
(cid:88)
θ = P(VL |Age,Sex,BHV,CoMo ,Weight ,Genotype,MEMS ,
36 36 0 0 6
Age,Sex,CoMo0,Weight0,

### VL0,CoMo6,VL6

Weight ,Dose ,EFV =a,VL ,CoMo ,VL ,MEMS ,Weight ,
6 6 6 0 6 6 36 36
Dose ,EFV =a)
36 36 (7)
P(VL |Age,Sex,CoMo ,Weight ,Genotype,MEMS ,
6 0 0 6
Weight ,Dose ,EFV =a,VL )
6 6 6 0
P(CoMo |Age,Sex,CoMo ,Weight ,Genotype,VL )
6 0 0 0
P(Weight |Age,Sex)P(CoMo |Age,Sex)P(VL )P(Sex)P(Age).
0 0 0
NotethateveniftheidentifiedexpressionlooksalmostidenticaltotheoneweobtainunderG orG
main alt1
(compare Equation 3), the recoverability result may differ due to the different conditional independence
statements that hold in G , assuming it is faithful.
alt2

### D Simulation Studies


### D.1 DGP for Simulations 1 and 2

Both baseline data (t = 0) and follow-up data (t = 1,...,5) were created using structural equations
with the R-package simcausal. Note that the follow-up time points 1 through 5 correspond to the study
weeks6, 36, 48, 60and84. Thedistributionslistedbelow, intemporalorder, describethedata-generating
process. Our baseline data consists of Sex, Genotype, log(age) (Age), log(weight) (Weight), the respective Nucleoside Reverse Transcriptase Inhibitor (NRTI), and a proxy for socio-economic status (SES).
The time-varying variables are co-morbidities (CoMo), efavirenz dose (Dose), efavirenz mid-dose concentration (EFV), elevated viral load (= viral failure, VL), adherence (measured through memory caps,
MEMS), missed visit (MV), technical issues (TI), and the missingness indicators for EFV, Weight, VL,
and MEMS, respectively. In addition to Bernoulli (B), Poisson (Poisson), Multinominal (MN) and
Normal (N) distributions, we also use truncated normal distributions, denoted by N , where
[a,a1,a2,b,b1,b2]
a and b are the truncation levels. Values smaller than a are replaced by a random draw from a U(a ,a )
1 2
distribution and values greater than b are drawn from a U(b ,b ) distribution, where U refers to a con-
1 2
tinuous uniform distribution. For the specified multinomial distributions, probabilities are normalized, if
required, to ensure they add up to 1.
The DGP corresponding to G in Figure 3 is as follows:
main

### Fort=0:

Sex0 ∼ B(p=0.5)
 
p1=1/(1+exp(−(−0.103+I(Sex0=1)×0.223+I(Sex0=0)×0.173))),
Genotype 0 ∼ MN p2=1/(1+exp(−(−0.086+I(Sex0=1)×0.198+I(Sex0=0)×0.214))), 
p3=1/(1+exp(−(−0.309+I(Sex0=1)×0.082+I(Sex0=0)×0.170)))

### Age ∼ N (µ=1.501,σ=0.369)

0 [0.693,0.693,1,2.8,2.7,2.8]
Weight
0

## ∼ N

[2.26,2.26,2.67,3.37,3.02,3.37]
(µ=(1.5+0.2×Sex0+0.774×Age
0
)×0.94),σ=0.369)
 
p1=1/(1+exp(−(−0.006+I(Age >1.4563)×Age ×0.1735+I(Age ≤1.4563)×Age ×0.1570))),
0 0 0 0
NRTI0 ∼ MN p2=1/(1+exp(−(−0.006+I(Age 0 >1.4563)×Age 0 ×0.1735+I(Age 0 ≤1.4563)×Age 0 ×0.1570))), 
p3=1/(1+exp(−(−0.006+I(Age >1.4563)×Age ×0.1570+I(Age ≤.14563)×Age ×0.1818)))
0 0 0 0
CoMo0 ∼ B(p=0.15)
(cid:112)
VL0 ∼ B(p=1−(1/(1+exp(−(0.4+1.9× EFV0)))))

### SES0 ∼ Poisson(λ=3)

MV0 ∼ B(p=1/(1+exp(−(−2.95+0.1×SES0))))

### Fort=1:

 p1=1/(1+exp(−(5+ (cid:112) (Weight )×8−Age ×10))), 
1 0
(cid:112)
Dose1 ∼ MN   p2=1/(1+exp(−(4+ (cid:112) (Weight 1 )×8.768−Age 0 ×9.06))),  
 p3=1/(1+exp(−(3+ (Weight )×6.562−Age ×8.325))), 
1 0
p4=1−(p1+p2+p3)
21

<!-- Page 22 -->


### Fort≥0:


### TIt ∼ B(p=0.05))))

MEFVt ∼ B(p=I(MVt=1)+I(MVt=0)×I(TIt=1)×0.5))))

## M


### Weightt

∼ B(p=I(MVt=1))
MVLt ∼ B(p=I(MVt=1)+I(MVt=0)×I(TIt=1)×0.5))))

### Fort≥1:

MEMSt ∼ B(p=1/(1+exp(−(0.71+CoMot−1×0.31+MEMSt−1×I(t≥2)×0.31)))), [assumeMEMS0=0]
Weight
t

## ∼ N

[2.26,2.26,2.473,3.37,3.2,3.37]
(µ=Weight
t−1
×1.04−0.05×I(CoMot−1=1),σ=0.4)
CoMot ∼ B(p=1−(1/(1+exp(−(0.5×I(CoMot−1=1)+Age
0
×0.1+Weight
t−1
×0.1)))))

### EFVt ∼ N

[0.2032,0.2032,0.88,21.84,8.37,21.84]
(µ=0.1×Doset+0.1×MEMSt+I(Genotype
0
≤2)×2.66
+I(Genotype =3)×4.6,σ=4.06)
0
(cid:112)
VLt ∼ B(p=1−(1/(1+exp(−(1−0.6×I(t=1)−1.2×I(t=4)+0.1×CoMot−1+(2−0.2×I(t=3))× EFVt)))))
MVt ∼ B(p=1/(1+exp(−(−2.95+0.1×SES0+MVt−1))))
MMEMSt ∼ B(p=1/(1+exp(−(0.5×I(TIt=1)+0.2))))

### Fort≥2:

 p1=(1/(1+exp(−(4+Doset−1×0.5+ (cid:112) Weight
t
×4−Age
0
×10))), 
(cid:112)
Doset ∼ MN   p2=(1/(1+exp(−(−8+Doset−1×0.5+ (cid:112) Weight t ×8.568−Age 0 ×9.06))),  
 p3=(1/(1+exp(−(20+Doset−1×0.5+ Weight t ×6.562−Age 0 ×18.325))), 
p4=1−(p1+p2+p3)
The DGP for G (including the blue dashed lines in Figure 3) coincides with the DGP above, except
alt1
for the structural equations for MV , t ∈ {0,6,36,48,60,84}. These are specified as follows for G :
t alt1

### Fort=0:

MV0 ∼ B(p=1/(1+exp(−(−2.95+0.1×SES0+2×VL0))))

### Fort≥1:


### MVt ∼ B(p=1/(1+exp(−(−2.95+0.1×SES0+MVt−1+2×VLt))))

Thus, MV additionally depends on VL , t ∈ {0,6,36,48,60,84}, which corresponds to the dashed blue
t t
lines in the DAG.
The DGP for G (where SES is a cause of MEMS , t ∈ {6,36,48,60,84}) coincides with the
alt2 t
DGP for G above, except for the structural equations for MEMS , t ∈ {6,36,48,60,84}. These are
main t
specified for G as follows:
alt2

### Fort≥1:

MEMSt∼B(p=1/(1+exp(−(0.71+CoMot−1×0.31+MEMSt−1×I(t≥2)×0.31−SES0×0.5))))
After generating the data set using the structural equations, we introduce missing values based on
the missingness indicators: if a missingness indicator equals 1, the corresponding covariate value is set to
NA. In Simulation 1, we ignore the missingness indicators for EFV , t ∈ {6,36,48,60,84}, and Weight ,
t t
t ∈ {0,6,36,48,60,84}, and generate missingness only in VL and MEMS , t ∈ {0,6,36,48,60,84}.
t t
In Simulation 2, missingness is introduced in EFV , t ∈ {6,36,48,60,84}, Weight , VL and MEMS ,
t t t t
t ∈ {0,6,36,48,60,84}.

### D.2 Results

The results below are based on Simulation 2 as defined in Section 5.
The following results are based on simulation 1 as defined in Section 5 under the assumption of G
alt2
being the true underlying causal m-DAG.
22

<!-- Page 23 -->

0.4
0.2
0.0
0.0 2.5 5.0 7.5 10.0
Efavirenz Mid−Dose Concentrations (mg/L), intervened on at each time point
skeew
48
retfa
daoL
lariV
detavelE
0.4
0.2
0.0
0.0 2.5 5.0 7.5 10.0
Efavirenz Mid−Dose Concentrations (mg/L), intervened on at each time point
(a) Data simulated under the main DAG G
main
skeew
48
retfa
daoL
lariV
detavelE
(b) Data simulated under the alternative DAG G
alt1
Figure 6: Estimated CCRCs for the probability of viral failure after 84 weeks. (a) Data simulated
under the main DAG G . (b) Data simulated under the alternative DAG G . Causal effects were
main alt1
estimated on complete data (black squares), incomplete data using available cases (blue dots), incomplete
data using multiple imputation (red triangles) and counterfactual data (green diamonds, true CCRC);
results represent the mean over 1000 seeds.
0.4
0.2
0.0
0.0 2.5 5.0 7.5 10.0
Efavirenz Mid−Dose Concentrations (mg/L), intervened on at each time point
skeew
48
retfa
daoL
lariV
detavelE

### Figure 7: Estimated CCRCs for the probability of

viral failure after 84 weeks based on data simulated under the main DAG G . Causal effects
alt2
were estimated on complete data (black squares),
incomplete data using available cases (blue dots),
incompletedatausingmultipleimputation(redtriangles) and counterfactual data (green diamonds,
true CCRC); results represent the mean over 1000
seeds.

### D.3 Monte Carlo Confidence Intervals

The Monte Carlo confidence intervals in Tables 1a, 1b and 1c are reported to determine whether the
differences between MI estimates and true values (main and alternative m-DAGs, G and G ),
main alt1
and between available case analysis estimates and true causal effects θ (alternative m-DAG G ) stem
84 alt1
fromsimulationuncertaintyorindicatesystematicdeviations. A95%confidenceinterval[meandifference
(cid:112)
−2·SE; mean difference +2·SE], with the standard error SE computed as sd(estimate)/ (#runs), excluding zero suggests that the differences can likely not be explained by simulation uncertainty, indicating
a bias caused by the estimation approach.
23

<!-- Page 24 -->

Table 1: Monte Carlo confidence intervals for the difference between estimates and true causal effects
across efavirenz (EFV) concentrations. (a) Multiple imputation estimates under the main m-DAG G .
main
(b) Available case estimates under the alternative m-DAG G . (c) Multiple imputation (MI) estimates
alt1
under the alternative m-DAG G .
alt1
(a) Multiple imputation under G (b) Available case under G (c) Multiple imputation under G
main alt1 alt1

### EFV Lower Upper EFV Lower Upper EFV Lower Upper

0.0 -0.19441 -0.19351 0.0 -0.12787 -0.10112 0.0 -0.29980 -0.29904
0.5 -0.04522 -0.04452 0.5 -0.04754 -0.03497 0.5 -0.10118 -0.10062
1.0 -0.00881 -0.00824 1.0 -0.03208 -0.02512 1.0 -0.04923 -0.04876
1.5 0.00696 0.00749 1.5 -0.02465 -0.02075 1.5 -0.02354 -0.02312
2.0 0.01493 0.01539 2.0 -0.01873 -0.01642 2.0 -0.00888 -0.00849
2.5 0.01774 0.01817 2.5 -0.01470 -0.01320 2.5 -0.00111 -0.00076
3.0 0.01842 0.01880 3.0 -0.01195 -0.01092 3.0 0.00326 0.00358
3.5 0.01812 0.01847 3.5 -0.01012 -0.00935 3.5 0.00583 0.00614
4.0 0.01721 0.01754 4.0 -0.00823 -0.00759 4.0 0.00727 0.00755
4.5 0.01626 0.01656 4.5 -0.00677 -0.00620 4.5 0.00804 0.00830
5.0 0.01502 0.01530 5.0 -0.00558 -0.00509 5.0 0.00832 0.00857
5.5 0.01403 0.01429 5.5 -0.00450 -0.00405 5.5 0.00849 0.00871
6.0 0.01309 0.01335 6.0 -0.00358 -0.00317 6.0 0.00851 0.00872
6.5 0.01191 0.01214 6.5 -0.00296 -0.00257 6.5 0.00815 0.00835
7.0 0.01123 0.01145 7.0 -0.00222 -0.00186 7.0 0.00819 0.00838
7.5 0.01051 0.01071 7.5 -0.00175 -0.00141 7.5 0.00795 0.00814
8.0 0.00952 0.00971 8.0 -0.00145 -0.00115 8.0 0.00749 0.00766
8.5 0.00886 0.00904 8.5 -0.00114 -0.00085 8.5 0.00718 0.00734
9.0 0.00810 0.00827 9.0 -0.00088 -0.00062 9.0 0.00675 0.00691
9.5 0.00750 0.00766 9.5 -0.00074 -0.00048 9.5 0.00640 0.00655
10.0 0.00685 0.00701 10.0 -0.00058 -0.00034 10.0 0.00605 0.00620
24

<!-- Page 25 -->


### Competing interests

No competing interest is declared.

### Author contributions statement

The study was designed by MS, PD and HM. Data was collected and interpreted by PD, HM. All authors
reviewedthestudydesignandinterpretedthedata. MethodsdevelopmentwasleadbyAH.Thefirstdraft
of the article was written by AH. All authors reviewed this and the following drafts, revising it critically
for its content. All authors have read and approved the final version and agree with the manuscript’s
conclusion.

### Acknowledgments

We are grateful for the support of the CHAPAS-3 trial team, their advice regarding the data analysis
and making their data available to us. We would like to thank David Burger, Sarah Walker, Di Gibb
and Andrzej Bienczak for their help in interpreting the data. We thank Elizabeth Kaudha and Victor
Musiime for discussing reasons for missingness with us. We would further like to acknowledge the help of
Alexander Szubert in constructing some of the variables. Michael Schomaker is supported by the German
Research Foundations (DFG) Heisenberg Programm (grants 465412241 and 465412441). The CHAPAS-3
trial was funded by the European Developing Countries Clinical Trials Partnership (IP.2007.33011.006),
Medical Research Council UK (MC UU 00004/03), Department for International Development UK, and
Ministerio de Sanidady Consumo Spain. Cipla Ltd donated first-line antiretrovirals. We thank all the
children, carers, and staff from all the centres participating in the CHAPAS-3 trial.

### Data Availability

The code used for conducting the simulation study in Section 5 is accessible at the following GitHub
repository: https://github.com/aholovchak/Recoverability-of-causal-effects.
25

## Tables

**Table (Page 9):**

| VL6 |  |
|---|---|
|  |  |
| EF | V6 |
|  |  |


**Table (Page 9):**

| VL36 |  |
|---|---|
|  |  |
| EF | V36 |


**Table (Page 9):**

| VL48 |  |
|---|---|
|  |  |
| EF | V48 |


**Table (Page 9):**

| VL60 |  |
|---|---|
|  |  |
| EF | V60 |


**Table (Page 9):**

|  | W | eight6 |
|---|---|---|
|  |  |  |
|  |  |  |
| MEMS6 |  |  |


**Table (Page 9):**

|  | W |
|---|---|
|  |  |


**Table (Page 9):**

|  |  | Wei |
|---|---|---|
|  |  |  |
| MEMS60 |  |  |


**Table (Page 13):**

|  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |


**Table (Page 13):**

|  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |


**Table (Page 14):**

|  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |


**Table (Page 14):**

|  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |


**Table (Page 23):**

|  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |


**Table (Page 23):**

|  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |


**Table (Page 23):**

|  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
