---
title: "Riemannian Preconditioned LoRA"
original_file: "./Riemannian_Preconditioned_LoRA.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["llm", "rag", "chain-of-thought", "fine-tuning", "evaluation"]
keywords: ["cid", "bit", "ctc", "tuning", "aibit", "page", "lora", "riemannianpreconditionedlora", "group", "gpt"]
summary: "<!-- Page 1 -->

Riemannian Preconditioned LoRA for Fine-Tuning Foundation Models

### FangzhaoZhang1 MertPilanci1

Abstract solutionwhilestilldeliveringstrongperformanceindownstream tasks. A widely-used PEFT method is Low Rank

### Low-Rank Adaptation (LoRA) emerges as a

Adaptation,alsoknownasLoRA(Huetal.,2021),which
popular parameter-efficient fine-tuning (PEFT)
proposestoaddlow-rankmatricestoexistingmodelweights
method, which proposes to freeze pretrained
andonlytraintheseadditivecomponents."
related_documents: []
---

# Riemannian Preconditioned LoRA

<!-- Page 1 -->

Riemannian Preconditioned LoRA for Fine-Tuning Foundation Models

### FangzhaoZhang1 MertPilanci1

Abstract solutionwhilestilldeliveringstrongperformanceindownstream tasks. A widely-used PEFT method is Low Rank

### Low-Rank Adaptation (LoRA) emerges as a

Adaptation,alsoknownasLoRA(Huetal.,2021),which
popular parameter-efficient fine-tuning (PEFT)
proposestoaddlow-rankmatricestoexistingmodelweights
method, which proposes to freeze pretrained
andonlytraintheseadditivecomponents. Simplyspeaking,
modelweightsandupdateanadditivelow-rank
forapretrainedmodelweightmatrixW ofdimensionm
trainablematrix. Inthiswork, westudytheenby n, LoRA replaces W with W +BA where B,A are
hancement of LoRAtraining by introducing an
trainableweightmatricesofdimensionmbyrandrbyn
r×rpreconditionerineachgradientstepwherer
forsomesmallrankr. Inthefine-tuningprocedure,W is
istheLoRArank. Wetheoreticallyverifythatthe
frozenandweareonlyoptimizingoverA’sandB’s. Comproposedpreconditionerstabilizesfeaturelearnparedtofullfine-tuning,LoRAintroducesfewertrainable
ingwithLoRAunderinfinite-widthNNsetting.
parameters. Effectiveness of LoRA has been empirically
Empirically,theimplementationofthisnewpreverified in different fields. Here we note that optimizing
conditioner requires a small change to existing
LoRAparametersfallsintooptimizingoverlow-rankmaoptimizer code and creates virtually minuscule
triceswhichformaquotientmanifold. Thismotivatesthe
storage and runtime overhead. Our experimenideaofenhancingLoRAtrainingviatoolsfromthefieldof
talresultswithbothlargelanguagemodelsand
Riemannianoptimization.
text-to-imagediffusionmodelsshowthatwiththis
newpreconditioner,theconvergenceandreliabil- RecentworksuchasLoRA+(Hayouetal.,2024)hasdrawn
ityofSGDandAdamWcanbesignificantlyen- attentiontotheoptimizationparadigmofLoRAandreveals
hanced. Moreover,thetrainingprocessbecomes thatthelearningrateofLoRAparameterB shouldbeset
muchmorerobusttohyperparameterchoicessuch largerthanthatofAtoachievestablefeaturelearningunas learning rate. The new preconditioner can dertheinfinite-widthNNsetting,makingthelearningrate
be derived from a novel Riemannian metric in tuningajointhyperparametersearch. Morespecifically,delow-rank matrix field. Code can be accessed notelearningratesforAandBbyη A andη B respectively,
at https://github.com/pilancilab/ LoRA+proposestouseaheuristicη B /η A =24inpractice
Riemannian_Preconditioned_LoRA. andtuneonlyη A . Inthiswork,weproposeanimprovement
ofLoRAtrainingwiththeintroductionofanr×rpreconditionerinitsoptimizationstep,andweshowthatwiththis
simplepreconditioner,LoRAlearnsstablefeatureswithout

## Introduction

theneedofsettingdifferentlearningratesforAandB. As
Withtheexpandingscaleofneuralnetworkmodelsinboth anillustration,weproposemodifyingthegradientupdates
vision and language domains, training a neural network fortheLoRAparametersasfollows
from scratch to match the performance of existing large

### A =A −α(BTB )−1(∇ L),

models has become almost infeasible. As a result, fine- t+1 t t t At
(1)
tuninghasemergedasaprevalentapproachfordownstream B =B −α(∇ L)(A AT)−1,
t+1 t Bt t t
tasks. Traditional full parameter fine-tuning demands extensive storage, making it impractical for many applica- where (A t AT t )−1 and (B t TB t )−1 are the preconditioners
tions. In contrast, recent advances in Parameter-Efficient we introduce and L is the training loss objective. This
Fine-Tuning(PEFT)methodsofferamorestorage-efficient scaledgradientmethod(scaledGD)canbederivedfroma
novel Riemannian metric studied in (Mishra et al., 2012)
1DepartmentofElectricalEngineering, StanfordUniversity. whichtakesintoconsiderationboththeobjectivefunction
Correspondenceto:FangzhaoZhang<zfzhao@stanford.edu>.
andconstraintsandhasbeenshowntohavebetterconvergencerateforconventionallow-rankmatrixoptimization

### Proceedings of the 41st International Conference on Machine

Learning,Vienna,Austria.PMLR235,2024.Copyright2024by problemsinvolvingmatrixsensingandrobustPCA(Cantheauthor(s). des et al., 2009). Our work shows for the first time that
1
4202
nuJ
5
]GL.sc[
3v74320.2042:viXra

<!-- Page 2 -->


### RiemannianPreconditionedLoRA

Figure1. Generationresultsforprompt“ablue⟨V ⟩”afterfine-tuningon6redvaseimagesoftheStableDiffusionV1.5model.No
vase
blackimagesareobservedforourmethod(scaledAdamW)’sgenerationandAdamWgeneratesonlyblackimagesforlargelearningrates.
Ourmethodgeneratesphotosbettercapturingthepromptandismorerobusttolearningratechanges.SeeSection6.4.1forexperimental
details.
thispreconditionerenablesLoRAtoachievestablefeature theperformanceofunscaledoptimizers. SeeSection6for
learningwithAdamoptimizer,revealingthesuperiorityof the experimental details. To the best of our knowledge,
preconditioninginfine-tuningdeeplearningmodels. Em- thisisthefirstworktoapplyRiemannianoptimizationin
pirically,weverifythevalidityofthisnewpreconditioner designingpreconditionersforfine-tuninglargefoundation
forLoRAtrainingviaextensivefine-tuningtasksforboth models. Thisapproachisparticularlyappropriategiventhe
languagemodelsandtext-to-imagediffusionmodels. The matrixfactorizationcharacteristicsoftheLoRAmodel.
experimentalresultsshowthattheconvergenceofbothSGD
Next,wefirstprovidesomeintuitiononourmethodinSecandAdamWissignificantlyenhancedbypreconditioning
tion3. WethenshowthatLoRAtrainingwiththeproposed
(gradientscaling). Despitetheacceleratedconvergence,the
preconditionersachievesstablefeaturelearninginSection4.
optimizationprocedurealsobecomesmorerobusttolearn-

### WeincludeanoverviewofbasicRiemannianoptimization

ing rate changes with this new preconditioner. Figure 1
conceptsaswellasthederivationofthispreconditionerby
compares the generation results for diffusion model fineintroductionofanewRiemannianmetricinSection5. We
tuningwithAdamWoptimizerwithandwithoutgradient
offerapseudocodeandpresentextensiveexperimentalrescaling,fromwhichitcanbeobservedthatgradientscalsultsinSection6. Finallywestateourconvergenceresults
ingsignificantlyimprovesthegenerationqualityaswellas
forrelatedproblemsinSection7andreviewpriorliterature
trainingrobustnessagainstlearningratechanges,seeAlgoinSection8.
rithm1fortheformalalgorithmforscaledAdamW.Most
importantly,ourpreconditionerisonlyofdimensionrbyr
thusthestorageoverheadisnegligibleforsmallLoRArank 2.Notation
r. Also, unlike most second-order preconditioners based

### WeadoptsamenotationconventionasinLoRA+(Hayou

onHessianinverses,invertinganrbyrmatrixforsmallr
etal.,2024). Specifically,foranysequences ∈Randany
introducesnegligibleruntimeoverheadandrunsasfastas n
given c ∈ R+, we use s = O(c ) and s = Ω(c ) to
unpreconditionedoptimizers. Inpractice,smallvalues,e.g., n n n n n
represent s < κc and s > κc respectively for some
r =4,areusuallyusedasdefaultforLoRAfine-tuning,see n n n n
κ > 0. We use s = Θ(c ) when both s = O(c ) and
Figure2forruntimecomparisonwhenfine-tuningGPT-2 n n n n
s =Ω(c ). Forvectorandmatrixsequences,thenotation
withbothscaledandunscaledoptimizers. n n
is applied entrywise. For a sequence that is a vector of
Tosummarize,westudytheapplicationofpreconditioned randomvariables,convergenceinsecondmoment,i.e.,L
2
gradientupdates(1)inLoRAtraining. Theoretically, we convergence,isadopted.
showthattheproposedpreconditionerprovidesanelegant
solutiontolearningratechoicesforstablefeaturelearning

## TheoreticalInsights

withLoRAunderinfinite-widthNNsetting.Wealsoprovide
aconvergenceguaranteeforfine-tuningareparameterized Wefirstofferanintuitiveexplanationfortheeffectiveness
modelwhichisequivalenttoatwo-layerReLUnetworkvia of the preconditioner (1) before we move on to its stable
convexification. SeeSection4andSection7respectively learningpropertiesandreviewitsrigorousderivationfrom
for details. Empirically, we apply this method for LoRA aRiemannianmetricformulation. Considerinthet-thitfine-tuning for both large language and diffusion models eration pretrained model weight W and its additive lowand observe that scaled optimizers significantly improve rank component B A . Let X = W +B A denote the
t t t t t
2

<!-- Page 3 -->


### RiemannianPreconditionedLoRA

wholeweightmatrixandletLdenotethelossfunction,i.e., fortrainingAandB. Incontrast,LoRAtrainedwiththeun-
L(A,B) := L(W +BA). Fortheplaingradientdescent preconditionedAdamoptimizerrequiresdifferentlearning
method, when step size η is small, the updated weight is ratesettingsforAandBtoachievestablefeaturelearning.
approximatelygivenby

### Wefirstillustrateourkeypointviaasimpletoyexample

X =W +B A and we then proceed to our main theorem. Consider the
t+1 t+1 t+1
simplelinearmodel
≈W +B A −η∇ LA −ηB ∇ L
t t Bt t t At
=X −η∇ L(ATA )−η(B BT)∇ L, f(x)=(W +baT)x,
t Xt t t t t Xt
whereweignorethesecond-orderterminthesecondline where W ∈ R1×n is the pretrained model weight and
sincewhenηissmall,η2isnegligible. Thederivationfrom b ∈ R,a ∈ Rn are trainable LoRA parameters. Conthe second line to the third line comes from the simple siderthequadraticlossfunctionL(a,b)=(f(x)−y)2/2
fact∇ L=(∇ L)AT and∇ L=BT(∇ L). Thus withsomescalarlabely.WeadoptGaussianinitialization

### Bt Xt t At t Xt

theLoRAupdateingradientdescentstepisapproximately a ∼ N(0,σ2),b ∼ N(0,σ2). Conventionally,baT isinii a b
constrainedtothecolumnspaceofB andtherowspaceof tialized at zero for LoRA, and we thus consider setting
t
A . Ifwescale∇ Lrightby(A AT)−1andscale∇ L σ2 =0,σ2 =Θ(1).
t Bt t t At a b
leftby(BTB )−1,whichisexactlythepreconditioner(1),
t t Analysis of unpreconditioned training. Assume the
thescaledupdatebecomes
model is trained with gradient descent with learning rate
X˜ ≈X −η(∇ L)AT(A AT)−1A η =Θ(nc)forsomec∈R.Sincethetrainingprocedureint+1 t Xt t t t t
volvesonlyelementaryalgebraicoperations,thequantities
−ηB (BTB )−1BT(∇ L)
t t t t Xt thereshouldbeof powersof n.Initerationt, thefeature
=X −ηProj (∇ L)−ηProj (∇ L)T, updatewithoutpreconditioningisgivenby
t row(At) Xt col(Bt) Xt
wheretheupdateisdoneaccordingtoprojectionofthefull ∆f :=f (x)−f (x)
t t t−1
matrixgradientontotherowspaceofA t andthecolumn =−ηb2 (f (x)−y)∥x∥2
spaceofB ,whichbetterapproximatesfullfine-tuningcom- t−1 t−1
t
−η(aT x)2(f (x)−y)
paredtotheunscaledgradientdescentstep. Therefore,our t−1 t−1
preconditioner(1)effectivelyservesasagradientprojector. +η2(f (x)−y)2b (aT x)∥x∥2.
t−1 t−1 t−1
We denote δ1 = ηb2 (f (x) − y)∥x∥2,δ2 =

## StableFeatureLearning t t−1 t−1 t

η(aT x)2(f (x) − y), and δ3 = η2(f (x) −
t−1 t−1 t t−1
Giventhecurrenttrendofincreasingmodelsizes,therehas y)2b (aT x)∥x∥2.Forstablefeaturelearning,wewould
t−1 t−1
beenafocusonanalyzingtheasymptotictrainingbehavior like δ1,δ2,δ3 ∈ Θ(1) and further f (x) ∈ Θ(1).
t t t t−1
of neural networks as the number of neurons approaches Note that δ3 ∈ Θ(1) is guaranteed as long as δ1,δ2 ∈
t t t
infinity(Schoenholzetal.,2017;Hayouetal.,2019;Yang, Θ(1). Thus for stable feature learning, it suffices to have
2020). Underthisinfinite-widthNNsetting,wenaturally δ1,δ2,f (x) ∈ Θ(1).Forthesakeofnotationalclarity,
t t t−1
expect that both the NN prediction ft(x) in the t-th iter- weintroducenewnotationγ suchthatv = Θ(nγ[v])capation and the increment ∆ft := ft(x)−ft−1(x) to be turesthepolynomialbehaviorforanyv. Wereferreadersto
ofconstantmagnitude,whichensuresthatneithertheNN SectionA.2in(Hayouetal.,2024)foradditionalproperties
predictionsnortheincrementsexplodeorvanishastheNN ofγ[·].Stablefeaturelearningisthusequaltothefollowing
sizeincreases,therebyleadingtostabletrainingdynamics. linearconstraints
Werefertothisbehaviorasstablefeaturelearning,formally

c+2γ[b ]+1=0 (forδ1 =Θ(1)),
definedinDefinitionA.1intheAppendix. Theauthorsof  t−1 t
LoRA+(Hayouetal.,2024)observethatthelearningrateof c+2γ[aT x]=0 (forδ2 =Θ(1)),
t−1 t
LoRAparameterBshouldbesettobelargerthanthatofA γ[b ]+γ[aT x]=0 (forf (x)=Θ(1)),
t−1 t−1 t−1
forasymptoticstablefeaturelearning. Theiranalysismostly
focusesontheorderofmagnitudeofiteratesandthecon- fromwhichwecanderivec=−1/2andthusthelearning
clusionthatη ≫η doesnotimmediatelyofferpractical rateshouldbesettoη =Θ(n−1/2).Withγ[b ]=γ[b ]=0

## B A 1 0

guidance. Hereweshowthatourpreconditionedupdates(1) and γ[aTx] = γ[ηb y∥x∥2] = 1/2, one can inductively
1 0
introduceanelegantandpracticalsolutiontolearningrate deducethatγ[b ]=0andγ[aTx]=1/2foralltandthus
t t
choicesforstablefeaturelearningintheinfinite-widthNN γ[f ] = 1/2, contradicting to f = Θ(1). Instead, stable
t t
regime. Specifically, we will see that LoRA trained with feature learning requires to set separately η = Θ(1/n)
a
Adamoptimizerscaledbyourpreconditionerasin(1)leads andη =Θ(1)asshowninProposition2in(Hayouetal.,
b
tostablefeaturelearningwhenthesamelearningrateisused 2024).
3

<!-- Page 4 -->


### RiemannianPreconditionedLoRA

Analysisofpreconditionedtraining. Wenowproceed ofTheorem4.1aswellasanexplanationofthisdifference.
toshowthatwithourpreconditonedparameterupdates(1), Theorem1in(Hayouetal.,2024)showsthatη =Θ(n−1)

## A

c = −1wouldgeneratestablefeaturelearning. Afterthe andη =Θ(1)arerequiredforLoRAtrainingwithunpre-

## B

injectionofpreconditioner(1), thetrainingdynamicsare conditionedAdamtoobtainstability,revealingthatwithout
givenby preconditioningweneedtotuneη andη separatelywhile

## A B

ourpreconditionerelegantlyfixesthisimbalancebetween
∆f t :=f t (x)−f t−1 (x) thelearningrates.
=(b −η(f (x)−y)aT x ∥a ∥−2)(aT
t−1 t−1 t−1 t−1 t−1
(cid:124) (cid:123)(cid:122) (cid:125) 5.ARiemannianMetricFormulation
preconditioner
−η(f (x)−y)b xT b−2 )x
t−1 t−1 t−1 Afterdiscussingthemotivationandsuperiorityforstabiliz-
(cid:124)(cid:123)(cid:122)(cid:125)
ingfeaturelearningofourproposedpreconditionerinprior
preconditioner
=−η(f (x)−y)∥x∥2 sections,wenowreviewhowtheproposedpreconditioner
t−1
is derived from a new Riemannian metric. Optimization
−η(aT x)2(f (x)−y)∥a ∥−2
t−1 t−1 t−1 overmatrixwithrankconstraintisacommonexamplefor
+η2(f (x)−y)2b−1 ∥a ∥−2(aT x)∥x∥2. optimizationoverRiemanniansubmanifolds. Specifically,
t−1 t−1 t−1 t−1
matriceswithfixedrankformaquotientmanifoldofgeneral
We similarly define δ1scaled = η(f (x) − y)∥x∥2, matrixfield. LetMdenoteanyRiemanniansubmanifold,
t t−1
δ2scaled = η(aT x)2(f (x) − y)∥a ∥−2, δ3scaled = thenRiemanniangradientdescentusuallytakesform
t t−1 t−1 t−1 t
η2(f (x)−y)2b−1 ∥a ∥−2(aT x)∥x∥2asscaledvert−1 t−1 t−1 t−1 X =R(X −η∇ f(X )),
sionofδ1,δ2,δ3.Forstablefeaturelearning,wethushave t+1 t Mr t
t t t
thebelowmodifiedlinearconstraints whereRisaretractionoperatorthatmapstoM. Here,f is
 c+1=0 (forδ1scaled =Θ(1)), theobjectivefunctionand∇ Mr f(X t )denotesRiemannian
 t gradientdefinedby
c+2γ[aT x]−γ[∥a ∥2]=0 (forδ1scaled =Θ(1)),
t−1 t−1 t
γ[b
t−1
]+γ[aT
t−1
x]=0 (forf
t−1
(x)=Θ(1)), Df(x)[η x ]=g x (∇ Mr f(x),η x )forallη x ∈T x M,
whereDf(x)[η ]istheconventionalEuclideandirectional
fromwhichwecanderivec=−1.Withη =Θ(n−1),we x
derivativeoff inthedirectionη . Inthisdefinition,g isa
getγ[b ] = γ[b ] = 0andγ[aTx] = γ[ηb−1y∥x∥2] = 0. x x
1 0 1 0 Riemannianmetricwhichmapstwoelementsinthetangent
Onecanrecursivelyderiveb ,aTx,δscaled,δscaled,δscaled ∈
t t 1 2 3 spaceT Mtoarealnumberandmightnotbeunique,we
x

### Θ(1)forallt,whichpreservesf ∈Θ(1)and∆f ∈Θ(1),

t t willseethattheinnovativedesignofg isthekeytoderive
x
i.e.,stabilityisachieved.
ourpreconditionedupdates(1). Beforeproceedingtothe
Theabovetoyexampleillustratesthatourpreconditioned derivationofourpreconditioner,weneedonemorepieceof
LoRAupdatesachievestablefeaturelearningwithlearning knowledgeaboutquotientmanifold.
ratesforAandBofsameorderofmagnitude,whileforun-
WhenitcomestoaquotientspaceM/∼whereeachelepreconditionedLoRA,differentlearningratesarerequired
ment[x] = {y ∈ M : y ∼ x}representsanequivalence
toobtainthesamestability. Nevertheless,thetoyexample
class,forlow-rankmatrixproblemswhereABT areconsidislimitedtolinearmodelwithLoRArankr =1andalso
ered,each(A,B)pairisequivalentto(AO,BO−1)forany
gradient updates without a momentum term. Indeed, the

### O ∈GL(r)inthesensethattheyobtainthesameobjective

stabilitypersistsforarbitraryLoRAranksandfortheAdam
value,whereGL(r)standsforthegenerallineargroupover
optimizerwhenaidedwithourpreconditioner(1), which
r×r invertible matrices. Tangent space T M respects
[x]
weformalizeasourtheorembelow.
theequivalencerelation∼bytheintroductionofhorizontal
Theorem4.1. [StableFeatureLearning(Informal)]Assume and vertical spaces at each element, i.e., we decompose
LoRAparametersAandB aretrainedwithAdamscaled T M = V ⊕H where V is the tangent space of the
x x x x
byourpreconditionerasin(1). FurtherassumethatBAx equivalenceclass[x]andH isitscomplement. Theneach
x
hasdimensionΘ(n).ThentheLoRAmodelachievesstable η ∈T McorrespondstoauniqueelementinH which
[x] [x] x
featurelearningwithη =Θ(1).WhileforunscaledAdam, iscalledthehorizontalliftofx.ARiemannianmetricfor
η

## A

= Θ(n−1) and η

## B

= Θ(1) are required for stable M/∼satisfies
featurelearning.
g (η ,ξ )=g (η ,ξ ),
Noteherewerequireη =Θ(1)insteadofη =Θ(n−1)as [x] [x] [x] x x x
inthetoyexample,thisdiscrepancyisduetoourassumption where η and ξ are horizontal lifts of η and ξ at x.
x x [x] [x]
aboutvectoroutputandAdamoptimizer’sgradientprocess- Thus a Riemannian metric on quotient space is invariant
ing. SeeSectionAforthedetailedstatementandtheproof alongequivalenceclassesofthequotientspace.
4

<!-- Page 5 -->


### RiemannianPreconditionedLoRA

Algorithm1PseudocodeofscaledAdamWinPyTorch.
# group trainable parameters into LoRA pairs in train.py.
for LoRAA, LoRAB in pairwise(trainableparameter):
paramgroups.append({"params": [LoRAA,LoRAB], "lr": learningrate})
# apply preconditioner in optimizer.py
for group in param_groups:

### A, B = group["params"]

dA, dB = group["params"].grad
# update parameter A
dAscaled =inverse(B.T@B+delta*torch.eye(r)).mm(dA) # precondition gradient of A
A_m = beta1*A_m+(1-beta1)*dA_scaled; A_m_hat = A_m/(1-beta1**t) # update first momentum of A
A_v = beta2*A_v+(1-beta2)*dA_scaled**2; A_v_hat = A_v/(1-beta2**self.t) # update second momentum of A
A.add_(A_m_hat/(sqrt(A_v_hat)+eps), -group[’lr’]) # update A
# update parameter B similarly
# ...
pairwise:readeverytwoelementsinalist
In(Mishra&Sepulchre,2016),Mishraetal. describeanew AdamW
Riemannianmetricthatdrawsmotivationfromregularized
Runtime(×103/s) scaled

## Sg


## A


## D

damW
scaledGD
Lagrangian and involves both objectives and constraints. 18
When specialized to least squares matrix decomposition 14
problem of form ∥ABT − Y∥2/2, following derivation

## F 10

(33)in(Mishra&Sepulchre,2016),wegetthefollowing
6
metriconquotientspace[x]=(A,B), Training
2

### Steps

g [x] (η [x] ,ξ [x] )=⟨η A ,ξ A BTB⟩+⟨η B ,ξ B ATA⟩. (2) 1 2 3 4 5 6 7 8 910 111213 (×103/step)

### Under this new metric, the Riemannian gradient descent

effectivelyreplacesthegradientoperatorsviathemap Figure2.RuntimeforLoRAfine-tuningGPT-2mediummodel
withdifferentoptimizers.Ourscaledmethodsintroducenegligible
(cid:16) ∂ (cid:17) (cid:16) ∂ (cid:17) (cid:16) ∂ (cid:17) (cid:16) ∂ (cid:17)
→ (BTB)−1, → (ATA)−1, runtime overhead and train as fast as unscaled methods. See
∂A ∂A ∂B ∂B Section6.2forexperimentaldetails.Herewesetr=4.
whichthencorrespondstothepreconditionedupdates(1)
weproposeinthiswork. Fordetailsinthedesignofthenew
metric(2)anditsconnectionwithsequentialquadraticpro- onlybasedonthegradientdescentmethod. OurTheorem
gramming(SQP),wepointreadersto(Mishra&Sepulchre, 4.1introducesthispreconditionerforAdamforthefirsttime
2016)and(Mishraetal.,2012)whichincludeathorough andrevealsitsadvantagesforAdamanditsvariants. We
explanationandvisualizationofRiemannianoptimization notethatAdamWismorepopularthanSGDforfine-tuning
concepts. duetoitsfastconvergence. Toextendpreconditioningto

### AdamW,onecouldapplythepreconditionerateachindivid-


## EmpiricalResults ualgradientcomputationsteporapplythescalingtotheprocessedgradient. ThoughourproofofTheorem4.1adopts


### AlgorithmsandSimpleImplementation thelatterversionandpreconditionstheprocessedgradient,

weempiricallyfindthatscalingthegradientineachsingle

### Inthissection,wedescribetheoptimizationalgorithmsand

iterationbehavesbetterthanscalingtheprocessedgradient,
thesoftwareimplementationweuseforacceleratingLoRA
thus we scale each single gradient in AdamW algorithm
training in practice. Let L denote the loss function and
forourpracticalimplementationanddubitscaledAdamW
(A(t),B(t))denotethepairofLoRAparametersinthet-th
method. WeoutlinethepseudocodeofourscaledAdamW
iteration.
inAlgorithm1. Remarkably,ourmethodonlyrequiresfour
ScaledGD.ToapplygradientscalingtoSGD,wefollow lineschangeofexistingoptimizercode,whichissimpleto
exactly(1)anduse(B(t−1)TB(t−1)+δI)−1 toscalegra- implement. Wehighlightthechangedcodeinredcolor.
dient ∇ L and vice versa. Note here a small δ > 0

### A(t−1)

is used to tackle the case when either B(t−1)TB(t−1) or 6.2.RuntimeComparison
A(t−1)A(t−1)T is not invertible. See Appendix C for the
Amainconcernofourmethodmayarisefromthecommon
completealgorithm.
stereotypeaboutthecumbersomenessandheavycomputa-
ScaledAdamW.TheconventionalscaledGDmethodstud- tioncomplexityofusualpreconditioningmethods. Thisis
ied for classic low-rank matrix optimization problems is likelyduetoHessian-inversetypesecond-orderprecondi-
5

<!-- Page 6 -->

RiemannianPreconditionedLoRA

## E2E


### Method


### BLEU NIST MET ROUGE-L CIDEr


## Sgd 66.6 8.54 44.2 68.2 2.32

r=4
scaledGD(ours) 69.2 8.71 46.3 70.9 2.48
r=4
AdamW 68.9 8.69 46.5 71.3 2.51
r=4
scaledAdamW(ours) 69.6 8.77 46.6 71.8 2.52
r=4
Table1.ScoresforLoRAfine-tuningofGPT-2mediummodelonE2ENaturalLanguageGenerationchallengewithdifferentoptimizers.
OurscaledoptimizersoutperformunscaledoptimizersonallevaluationmetricsandscaledGDclosestheperformancegapbetweenSGD
andAdamW.SeeSection6.3.1forexperimentaldetails.
tionerusuallyinvolveslargesizepreconditionersandcom- normalizedbygradientvarianceinAdamWmethod. See
plexcomputationprocedures,whichisnotthecaseforthe also Appendix E.1 for experimental results for different
preconditionersweconsider. Ineachiteration,weusecur- LoRAranks,differentdatasets,anddifferentmodelsizes.
rentvalueof(AAT)−1topreconditiongradientofB. The Our scaled optimizers show significant and uniform impreconditioneriseasilyobtainedandisofsmallsize. We provementsoverunscaledoptimizersforalmostalltests.
present a runtime comparison between scaled optimizers
and their unscaled counterparts for fine-tuning a GPT-2 6.3.2.MISTRAL7B
mediummodelonE2ENLGchallenge,seeSection6.3.1
Mistral7BisarecentlanguagemodelreleasedbytheMisforexperimentaldetails. Figure2showstheruntimeused
tralAIteam(Jiangetal.,2023)whichhasbeenshownto
fordifferentoptimizersforthefine-tuningtasktrainedon
outperformLlama2-13BonallbenchmarksandLlama1-
NVIDIAA100GPUs.Notethereislittledifferencebetween
34Bonmanybenchmarks(MistralAIteam,2023),andthus
thescaledoptimizersandunscaledones,whichverifiesthat
isconsideredthemostpowerfullanguagemodelsforitssize
ourpreconditionerispractical. Seeruntimecomprisonsfor
todate. Weexperimentourscaledoptimizerswiththisnew
largerrankr =256inAppendixD.
languagemodelontheGLUE(Wangetal.,2018)benchmarkfornaturallanguageunderstandingproblems. Table2

### LLMFine-Tuning

showsthefinalfine-tuningresults. Notablythatourscaled
In this section, we study the fine-tuning task for GPT-2 optimizersoutperformunscaledoptimizersonallevaluation
model and Mistral 7B model with our scaled optimizers. metrics,whichdemonstratestheeffectivenessofgradient
Empirically,weobservethatourscaledoptimizersoutper- scalingforfine-tuningMistral7Bmodel. SeeAppendixE.2
form unscaled optimizers by a large margin for various fortraininghyperparameterselection.
tasks,datasets,LoRAranks,modelsizes,modeltypes,and
benchmarks,whichdemonstratesthesuperiorityofgradi- 6.4.DiffusionModelFine-Tuning
entscalingintrainingLoRAmodels. Seebelowandalso
Diffusionmodelsarenowusedforvariousimagegenera-
AppendixEforallourexperiments.
tiontasksandLoRAhasbeenwidelyusedforfine-tuning
diffusionmodels. Herewestartwiththecommonlyused

## Gpt-2


### StableDiffusionV1.5modelandshowtheeffectivenessof

WeexploitthenewpreconditionerforLoRAfine-tuningof applyingournewpreconditionerinLoRAfine-tuningforob-
GPT-2models. Wefollowexactlythesameexperimental jectgeneration. Then,weexperimentwiththeMix-of-Show
setupas(Huetal.,2021)exceptthatherewetunelearning model(Guetal.,2023)whichcangeneratehigh-qualityface
rate individually using grid search for different methods images. Weobservethatwithgradientscaling,imagegenerbeingtested,seeAppendixE.1forexperimentaldetailsand ationbecomesmuchmorerobusttolearningratechanges,
traininghyperparameters. Table1showsthefinalscorefor whichisareflectionofthefactthatournewpreconditioner
fine-tuning GPT-2 medium model with LoRA rank 4 on stabilizes the training process against learning rate varia-
E2E (Novikova et al., 2017) natural language generation tions. Thishasimportantpracticalbenefitssincelearning
challenge. ItcanbeobservedthatscaledGDmethodcloses ratechoicescanbecrucialinimagegenerationproblems
thegapbetweenSGDandAdamWandbehavescompara- wheresmalldifferenceinlearningratecanproduceimages
bletoAdamWwhiledemandingsmalleroptimizerstorage. ofverydifferentquality. ThiscanbeobservedfromFigures
ScaledAdamWmethodimprovesscoreofAdamWmethod 1 and 3. Furthermore, it’s widely observed that training
onallevaluationmetrics, whichrevealsthatthenewpre- lossisuselessinmonitoringimagegenerationqualitywhen
conditionerisadvantageousevenforgradientcomputation trainingdiffusionmodels. Thusabetteroptimizerwhichis
6

<!-- Page 7 -->

RiemannianPreconditionedLoRA

## Glue


### Method

MNLI SST-2 MRPC CoLA QNLI QQP RTE STS-B WNLI Avg.
SGD 88.15 96.10 70.10 55.89 94.22 88.59 50.90 47.64 49.30 71.21
r=16
scaledGD(ours) 90.21 96.90 81.62 68.17 94.40 91.15 54.15 90.31 56.34 80.36
r=16
AdamW 89.86 96.79 88.48 71.05 94.42 91.24 90.61 90.42 81.69 88.28
r=16
scaledAdamW(ours) 90.68 97.25 89.46 71.30 94.67 92.22 91.34 91.10 83.10 89.01
r=16
Table2.ScoresforLoRAfine-tuningof4-bitquantizedMistral7BmodelonGLUEbenchmarkforNaturalLanguageUnderstanding
(NLU)challengeswithdifferentoptimizers.Ourscaledoptimizersoutperformunscaledoptimizersonallevaluationmetrics.SeeSection
6.3.2forexperimentaldetails.
morerobusttolearningratechoicesisveryimportant. See pencilsketch,whichdemonstratesitseffectivenessingen-
Appendix F for experimental details for diffusion model eratingimagesofhigherqualityandalsoitsrobustnessto
fine-tuningtasks. learningratechanges. SeeAppendixF.2.1forgeneration
resultsformorepromptsandalsofortheHermoinecharac-

#### OBJECTGENERATION terwithdifferentLoRAparameterfusioncoefficients. See

alsoAppendixF.2.2forgenerationresultsincludingSGD
We build our object generation experiments on a popular
and scaled GD methods for varying learning rates. Our
stablediffusionfine-tuningrepository(Ryu,2023)withStaobservationsaresimilarinallthesegenerationresults.
bleDiffusionV1.5asthebasemodel. Wefollowthedefault
settingsthereandtuneboththeU-Netandthetextencoder

## ConvergenceTheory

whereLoRAparametersareinjected. Forallexperiments,
wefixtheU-Netfine-tuninglearningrateasdefaultvalue

### Inthissection,wefurtherverifythesuperiorityofscaled

1e−4 which we find important for generating recogniz-

### GDmethodappliedtoareparameterizedtwo-layerReLU

able images. After fine-tuning on 6 images of a red vase

### NNtuningproblem,i.e.,weshowscaledGDmethodhas

titled“aphotoof⟨V ⟩”, Figure1showsthegeneration
vase convergencerateindependentofdataconditionnumberof
resultsforprompt“ablue⟨V ⟩”. Withlargelearningrate
vase thisspecificproblemandisthusadvantageouscomparedto
as1e−2fortextencoderfine-tuning, AdamWproduces
plaingradientdescent. WhenscaledGDisappliedtodeep
out-of-distributionresultswhileourmethodproducessatislearning models, nonlinearities in such models typically
factoryimages. Withdefaultlearningratesetting,AdamW
render theoretical analysis intractable. To tackle this, we
stillfailstocapturethepromptinformationandgenerates
insteadstudyanequivalentproblemtothetwo-layerReLU
onlyredvases. Instead,scaledAdamWwithdefaultlearnneuralnetwork.Wefirstintroducetheconceptofhyperplane
ingrateisabletoproducethedesiredbluevase. AdamW
arrangementmatrices.ForadatamatrixX ∈Rn×dandany
turns out to be able to generate the desired blue vase for
arbitrary vector u ∈ Rd, We consider the set of diagonal
learningratevaluesuchas1e−6. SeeAppendixF.1for
matrices
other target object generation including chairs and dogs.

### D :={diag(1{Xu≥0})},

ScaledAdamWimprovesAdamWforallexperiments.
whichtakesvalue1or0alongthediagonalsthatindicate

#### FACEGENERATION thesetofpossiblearrangementactivationpatternsforthe


### ReLUactivation. Indeed,wecanenumeratethesetofsign

Face generation is a more challenging task compared to
patternsasD ={D }P whereP isboundedby
objectgenerationandwethusswitchtoMix-of-Show(Gu i i=1
etal.,2023)variantofcustomdiffusionmodelwhichisorig- (cid:18) e(n−1) (cid:19)r

### P ≤2r

inallydesignedformulti-conceptLoRAandhasbeenrecr
ognizedtobeabletogeneratehigh-qualityfaceimages. For
bettervisualizationofdifferencesbetweendifferentLoRA for r = rank(X) (Pilanci & Ergen, 2020; Stanley et al.,
optimizationmethods,weturnoffembeddingfine-tuning 2004). The two-layer ReLU model is equivalent to the
andtuneonlytext-encodersandU-NetswhereLoRAfac- problem below for squared loss through convexification
torsareinjected.Weuse14imagesofPotterprovidedinthe
undermildconditions1(Mishkinetal.,2022),
originalprojectrepositorywherethecharacternameisre- P
1 (cid:88)
placedwith⟨V ⟩incaptionsofthetrainingimages. Fig- min ∥ D XW −Y∥2.
ure3showsge
p
n
o
e
tte
r
r
ationresultsforprompt“apencilsketch
Wi 2
i=1
i i F
of ⟨V ⟩” for various step sizes. Our method (scaled
potter 1Theequivalenceholdswhenthenumberofhiddenneuronsis
AdamW)generatesvisuallybetterimagesmoreresemblea
greaterthanorequalto2Pd.
7

<!-- Page 8 -->


### RiemannianPreconditionedLoRA

Figure3.Generationresultsforprompt“apencilsketchof⟨V ⟩”byMix-of-Showmodelwithdifferentoptimizersandvariouslearning
potter
rates.Ourmethod(scaledAdamW)generatesphotosbettercapturingtheprompt,i.e.,apencilsketch,andismorerobusttolearningrate
choices.SeeSection6.4.2forexperimentaldetails.
Therefore, we base our analysis on fine-tuning the above matrix. Weconsideraspecificinitializationstrategyhere
modelandshowthattheconvergencerateofproblembelow whichisanextensionofspectralinitializationformultiple
withscaledGDmethod(Algorithm2)hasnodependence termsasbelow,
onconditionnumberofthedatamatrixX. Wefocuson
Definition 7.3. (Extended Spectral Initialization) Let
P AiBiT bethebestrank-rapproximationof(D X)T(Y −
1 (cid:88) 0 0 i
A m i, i B n i 2 ∥ i=1 D i X(W i +A i B i T)−Y∥2 F , (3) (cid:80)P j=1 D j XW j )foreachi.
Now,wearereadytostateourmainconvergenceresultas
where X ∈ Rn×d,A ∈ Rd×r,B ∈ Rc×r,Y ∈ Rn×c.
We consider the respo
i
nse model Y
i
=
(cid:80)P

## D X(W +

follows,
AiBiT ). Here,Xi = AiBiT = UiΣiViT i= a 1 re i fixeda i nd Theorem7.4. UnderAssumption7.2withδ 2 i r ≤0.01for
⋆ ⋆ ⋆ ⋆ ⋆ ⋆ ⋆ ⋆ eachi. Withextendedspectralinitializationdescribedin
unknownmatriceswithU ⋆ iΣi ⋆ V ⋆ iT beingthesingularvalue Definition 7.3, ∥AiBiT − Xi∥ ≤ 1.5dist(Fi,Fi). In
decompositionofXi. DenoteFi = [Ai,Bi]T andFi = t t ⋆ F t ⋆
⋆ ⋆ ⋆ ⋆ t addition,ifthestepsize0 < η ≤ 2/3,thenthe(t+1)-th
[Ai,Bi]T withAi andBi denotethevalueof(A ,B )at
t t t t i i iterationFi satisfies
t-th iteration. Let σ (·) denote the r-th largest singular t+1
r
value.
max(dist(Fi ,Fi))≤(1−0.5η)max(dist(Fi,Fi)).
t+1 ⋆ t ⋆
i i
WefirstintroducethedefinitionofRestrictedIsometryProperty(RIP)andillustratetheassumptionsrequiredforour
Proof. SeeAppendixB.
theoremtohold,
Definition7.1. (RIP(Rechtetal.,2010))ThematrixA∈ Ourresultmainlybuildsonresultsfrom(Tongetal.,2021b)
Rn×dsatisfiesrank-rRIPwithaconstantδ r ∈[0,1)iffor and can be viewed as an extension of matrix sensing to
allmatricesM ∈Rd×cofrankatmostr,thebelowholds, ReLUneuralnetworks.
(1−δ r )∥M∥2 F ≤∥AM∥2 F ≤(1+δ r )∥M∥2 F . 8.LiteratureReview
Assumption 7.2. Suppose that D i X obeys the 2r-RIP Ourworkiscloselyrelatedtolow-rankmatrixoptimization
with a constant δ 2 i r for each i, and ∥XTD i TD j X∥ 2 ≤ and we briefly review some basic knowledge and related
min(δ 2 i r ∥X ⋆ i∥F, 0.12 )foranyj ̸=i. workinSection8.1. Ourworkappliespreconditionersfor

### P∥X⋆ j∥F 7P(P+1)

acceleratingtheLoRAfine-tuningprocess,whichfallsinto
Note for matrix X with i.i.d Gaussian entries preconditioningmethodsforPEFT,andrelatedpriorwork
N(0,1/d∥D ∥ ), D X satisfies RIP for a constant δ thereisdiscussedinSection8.2andSection8.3.
i 0 i
when∥D ∥ isontheorderofr(d+c)/(dδ2). See(Recht
i 0
et al., 2010) for other measurement ensembles satisfying 8.1.RiemannianOptimization
theRIPproperty. Notealso∥XTD i TD j X∥ 2 ≤∥XTX∥ 2 Severalrecentstudieshavemadetheoreticcontributionsto
for all (i,j)’s. Thus bounding ∥XTD TD X∥ amounts theconvergencerateofscaledGDmethodwhichemploys
i j 2
toboundinglargestsingularvalueofempiricalcovariance thepreconditioner(1).Specifically,in(Tongetal.,2021a;b),
8

<!-- Page 9 -->


### RiemannianPreconditionedLoRA

theauthorsshowlocalconvergenceofscaledGDmethod LoRA(Huetal.,2021),whichproposestoaddalow-rank
withbetterconvergencerateindependentofdatacondition adaptationtoeachexistingweightmatrix. Byfactorizing
numbercomparedtoplaingradientdescentmethodforsome the update into two low-rank matrices, LoRA is able to
classiclow-rankmatrixoptimizationproblemincludingma- achieve similar fine-tuning result as full fine-tuning with
trixsensing,robustPCA,etc.Theauthorsof(Jiaetal.,2023) 10,000timesfewerparameters. LoRAhasshowngoodpershowglobalconvergenceofscaledGDmethodwithratein- formance in both language model fine-tuning and vision
dependentofdataconditionnumberforleastsquaresmatrix modelfine-tuning. VariantsofLoRAmethodinvolveDydecompositionproblem∥ABT−Y∥2/2.Differentvariants LoRA (Valipour et al., 2023), IncreLoRA (Zhang et al.,

## F

ofscaledGDhavebeenproposedandstudied. In(Zhang 2023a),andAdaLoRA(Zhangetal.,2023d),allfocuson
et al., 2023c), the authors suggest to use (ATA+λI)−1 dynamically adjusting the rank hyperparameter. GLoRA
and(BTB +λI)−1 withsomefixedλ > 0inreplaceof (Chavan et al., 2023) generalizes LoRA by introducing a
(1)fortacklingoverparametrizationandill-conditionessin promptmodule;Delta-LoRA(Zietal.,2023)proposesto
matrixsensingproblems. In(Zhangetal.,2023b),theau- simultaneouslyupdatepretrainedmodelweightsbydifferthors suggest using (ATA+λ I)−1 where λ = βλ ence of LoRA weights. QLoRA (Dettmers et al., 2023)
t t+1 t
(similarchangeforB),i.e.,usinganexponentiallydecay exploitsquantizedLoRAmodelwhichfurtherreducesthe
regularizationterm. (Zhangetal.,2023c)proposesprecGD modelsize. Besidessuchadditivemethods,therearealso
(cid:112)
methodwhichsetsλ = f(A BT). (Tongetal.,2022; multiplicativePEFTmethodssuchastheorthogonalfinet t t
Ma et al., 2023) present extension of scaled GD method tuningmethod(OFT)(Qiuetal.,2023)anditsvariantBOFT
totensoroptimizationproblem. (Jiaetal.,2023)analyzes (Liuetal.,2023).

### AltScaledGDmethodwhichupdatesAandBalternatively

ThoughLoRAhasbecomeverypopularanddifferentvariandshowsthatsuchmethodhasbetterconvergenceratefor
antsemerge,currentLoRAtrainingmainlyexploitsgradilargerstepsize.
entbasedoptimizersandweareunawareofanypriorwork
studying acceleration of LoRA training given its special

### PreconditionersinDeepLearning

low-rankmatrixfactorizationnature. Ourworkshowsthat
Current deep learning training is dominated by gradientbyregroupingtrainableparametersandapplyinganr×r
basedmethodwhichfollowsadescentdirectiontoupdate
preconditioner,theoptimizationprocedureofLoRAcanbe
parametersfordecreasingobjectivevalue. Foraccelerating
significantlyenhancedwithnegligiblestorageandruntime
such training procedure, more advanced techniques such
overhead.
asAdagrad(Duchietal.,2011)proposestoscalegradient
basedontheirvariance. Specifically,G− t 1/2isusedasgra- 9.Conclusion
dientpreconditionerwhereG isaccumulatedouterproduct
t
Inthiswork,weborrowtoolsfromRiemannianoptimizaofhistoricsubgradients. Morepracticaloptimizerssuchas
tiontoenhanceLoRAfine-tuning. Specifically,westudy

### Adam(Kingma&Ba,2017)andAdamW(Loshchilov&

theapplicationofaRiemanniangradientpreconditioning

### Hutter,2019)performlikeadiagonalversionofAdagrad

method which introduces a new r ×r preconditioner to
andarethemaintrainingtoolsformostdeeplearningmod-

### LoRAfine-tuningprocedure. Empirically,weobservethat

elsinvariousfields. Morerecently,Shampoo(Guptaetal.,
thegradientscalingboostsperformanceofbothSGDand
2018)hasbeenproposedwhichusesaleftpreconditioner

### AdamW methods and theoretically we show that LoRA

andarightpreconditionerforaweightmatrix. Shampoois
trainedwithpreconditionedAdammethodachievesstable
inspiritclosetoAdagradbutrequiresmuchlessstorage. In
featurelearningunderinfinite-widthNNsettingwhileuncontrastwiththepreconditionersdesignedforaccelerating
preconditionedtrainingwouldrequiretuninglearningrates
optimizationprocedureforgeneraldeeplearningmodels.
forLoRAparametersseparately. Priortoourwork, theo-
WestudyaspecificpreconditionerdesignedforLoRAfinereticconvergencefortheproposedgradientscalingscheme
tuningmodelwhichexploitsitslowrankmatrixfactorizahasonlybeenestablishedforclassiclow-rankmatrixoptitionpropertyandborrowsfromRiemannianoptimization
mizationproblemsandonlywithgradientdescentmethod,
knowledge.
wefirsttimeintroducesittodeeplearningregimeconsideringthelow-ranknatureofLoRAmodelandrevealsits

### PEFTFine-TuningReview

superioritybeyondSGD.

### Currentcommonly-useddeeplearningmodelsaregrowing

largerandlarger,makingfullfine-tuningfordownstream

### Acknowledgements

tasksnearlyimpossible. Alineofparameter-efficientfinetuningmethodsemergesandhasbeenusedinvariousfields. ThisworkwassupportedinpartbytheNationalScience
Thesemethodsaimatachievinglowfine-tuninglosswith Foundation(NSF)underGrantDMS-2134248;inpartby
fewertrainableparameters. OnepopularPEFTmethodis theNSFCAREERAwardunderGrantCCF-2236829; in
9

<!-- Page 10 -->


### RiemannianPreconditionedLoRA

partbytheU.S.ArmyResearchOfficeEarlyCareerAward Hu,E.J.,Shen,Y.,Wallis,P.,Allen-Zhu,Z.,Li,Y.,Wang,
underGrantW911NF-21-1-0242;andinpartbytheOffice S.,Wang,L.,andChen,W. Lora: Low-rankadaptation
ofNavalResearchunderGrantN00014-24-1-2164. oflargelanguagemodels,2021.

### ImpactStatement


### Jia,X.,Wang,H.,Peng,J.,Feng,X.,andMeng,D. Precon-

Thispaperaimstoadvancethefieldofmachinelearning ditioningmatters: Fastglobalconvergenceofnon-convex
throughinnovativeresearch. Whileourworkholdssignif- matrixfactorizationviascaledgradientdescent.InThirtyicantpotentialforsocietalimpact,wedonotidentifyany seventh Conference on Neural Information Processing
specificconsequencesthatneedstobehighlightedhere. Systems,2023.
References Jiang, A. Q., Sablayrolles, A., Mensch, A., Bamford, C.,

### Chaplot,D.S.,delasCasas,D.,Bressand,F.,Lengyel,

Candes,E.J.,Li,X.,Ma,Y.,andWright,J.Robustprincipal
G.,Lample,G.,Saulnier,L.,Lavaud,L.R.,Lachaux,M.-
componentanalysis?,2009.
A.,Stock,P.,Scao,T.L.,Lavril,T.,Wang,T.,Lacroix,
T.,andSayed,W.E. Mistral7b,2023.
Chavan, A., Liu, Z., Gupta, D., Xing, E., and Shen, Z.
One-for-all: Generalizedloraforparameter-efficientfine-
Kingma,D.P.andBa,J. Adam: Amethodforstochastic
tuning,2023.
optimization,2017.
Dettmers,T.,Pagnoni,A.,Holtzman,A.,andZettlemoyer,
Labonne, M. Mistral fine-tuning example, 2024.
L. Qlora: Efficientfinetuningofquantizedllms,2023.
URL https://towardsdatascience.
com/fine-tune-a-mistral-7b-model\
Duchi, J., Hazan, E., and Singer, Y. Adaptive subgradi-
-with-direct-preference-optimization\
entmethodsforonlinelearningandstochasticoptimiza-
-708042745aac. Accessed: 2024-01-25.
tion. Journal of Machine Learning Research, 12(61):
2121–2159,2011.

### Liu,W.,Qiu,Z.,Feng,Y.,Xiu,Y.,Xue,Y.,Yu,L.,Feng,H.,

Gal, R., Alaluf, Y., Atzmon, Y., Patashnik, O., Bermano, Liu,Z.,Heo,J.,Peng,S.,Wen,Y.,Black,M.J.,Weller,
A.H.,Chechik,G.,andCohen-Or,D. Animageisworth A., and Scho¨lkopf, B. Parameter-efficient orthogonal
oneword: Personalizingtext-to-imagegenerationusing finetuningviabutterflyfactorization,2023.
textualinversion,2022.

### Loshchilov,I.andHutter,F. Decoupledweightdecayregu-

Gardent, C., Shimorina, A., Narayan, S., and Perez- larization,2019.

### Beltrachini, L. The WebNLG challenge: Generat-

Lu,C.,Zhou,Y.,Bao,F.,Chen,J.,Li,C.,andZhu,J. Dpming text from RDF data. In Alonso, J. M., Bugar´ın,
A., and Reiter, E. (eds.), Proceedings of the 10th In- solver:Afastodesolverfordiffusionprobabilisticmodel
ternational Conference on Natural Language Gener- samplinginaround10steps,2022.
ation, pp. 124–133, Santiago de Compostela, Spain,

### Ma,C.,Xu,X.,Tong,T.,andChi,Y. Provablyaccelerating

September 2017. Association for Computational Linill-conditionedlow-rankestimationviascaledgradient
guistics. doi: 10.18653/v1/W17-3518. URL https:
descent,evenwithoverparameterization,2023.
//aclanthology.org/W17-3518.

### Mishkin,A.,Sahiner,A.,andPilanci,M. Fastconvexopti-

Gu, Y., Wang, X., Wu, J. Z., Shi, Y., Chen, Y., Fan, Z.,
mizationfortwo-layerrelunetworks: Equivalentmodel
Xiao,W.,Zhao,R.,Chang,S.,Wu,W.,Ge,Y.,Shan,Y.,
classesandconedecompositions,2022.
andShou,M.Z. Mix-of-show: Decentralizedlow-rank
adaptationformulti-conceptcustomizationofdiffusion
Mishra,B.andSepulchre,R. Riemannianpreconditioning.
models,2023.

### SIAMJournalonOptimization,26(1):635–660,January

Gupta,V.,Koren,T.,andSinger,Y. Shampoo: Precondi- 2016. ISSN1095-7189. doi: 10.1137/140970860. URL
tionedstochastictensoroptimization,2018.
http://dx.doi.org/10.1137/140970860.
Hayou,S.,Doucet,A.,andRousseau,J. Ontheimpactof Mishra,B.,Apuroop,K.A.,andSepulchre,R.Ariemannian
theactivationfunctionondeepneuralnetworkstraining, geometryforlow-rankmatrixcompletion,2012.
2019.

### Mistral AI team. Mistral-7b announcement,

Hayou,S.,Ghosh,N.,andYu,B. Lora+: Efficientlowrank 2023. URL https://mistral.ai/news/
adaptationoflargemodels,2024. announcing-mistral-7b. Accessed: 2024-01-25.
10

<!-- Page 11 -->


### RiemannianPreconditionedLoRA

Nan, L., Radev, D., Zhang, R., Rau, A., Sivaprasad, A., Tong,T.,Ma,C.,andChi,Y.Low-rankmatrixrecoverywith
Hsieh, C., Tang, X., Vyas, A., Verma, N., Krishna, P., scaledsubgradientmethods: Fastandrobustconvergence
Liu,Y.,Irwanto,N.,Pan,J.,Rahman,F.,Zaidi,A.,Mu- without the condition number. IEEE Transactions on
tuma, M., Tarabar, Y., Gupta, A., Yu, T., Tan, Y. C., Signal Processing, 69:2396–2409, 2021a. ISSN 1941-
Lin, X. V., Xiong, C., Socher, R., and Rajani, N. F. 0476. doi: 10.1109/tsp.2021.3071560. URLhttp://
DART:Open-domainstructureddatarecordtotextgen- dx.doi.org/10.1109/TSP.2021.3071560.
eration. InToutanova,K.,Rumshisky,A.,Zettlemoyer,

### Tong,T.,Ma,C.,andChi,Y. Acceleratingill-conditioned

L., Hakkani-Tur, D., Beltagy, I., Bethard, S., Cotterell,
low-rankmatrixestimationviascaledgradientdescent,
R., Chakraborty, T., and Zhou, Y. (eds.), Proceedings
2021b.
of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics:
Tong, T., Ma, C., Prater-Bennette, A., Tripp, E., andChi,

### Human Language Technologies, pp. 432–447, Online,


### Y. Scalingandscalability: Provablenonconvexlow-rank

June 2021. Association for Computational Linguistics.
tensorestimationfromincompletemeasurements,2022.
doi: 10.18653/v1/2021.naacl-main.37. URL https:
//aclanthology.org/2021.naacl-main.37. Valipour,M.,Rezagholizadeh,M.,Kobyzev,I.,andGhodsi,

### A. Dylora: Parameter efficient tuning of pre-trained

Novikova, J., Dusˇek, O., and Rieser, V. The e2e dataset: modelsusingdynamicsearch-freelow-rankadaptation,
Newchallengesforend-to-endgeneration,2017. 2023.
Pilanci, M. and Ergen, T. Neural networks are convex Wang, A., Singh, A., Michael, J., Hill, F., Levy, O., and
regularizers: Exactpolynomial-timeconvexoptimization Bowman,S.GLUE:Amulti-taskbenchmarkandanalysis
formulationsfortwo-layernetworks,2020. platformfornaturallanguageunderstanding. InLinzen,

### T., Chrupała, G., and Alishahi, A. (eds.), Proceedings

Qiu,Z.,Liu,W.,Feng,H.,Xue,Y.,Feng,Y.,Liu,Z.,Zhang, of the 2018 EMNLP Workshop BlackboxNLP: Analyz-
D., Weller, A., and Scho¨lkopf, B. Controlling text-to- ingandInterpretingNeuralNetworksforNLP,pp.353–
imagediffusionbyorthogonalfinetuning,2023. 355,Brussels,Belgium,November2018.Associationfor
ComputationalLinguistics. doi: 10.18653/v1/W18-5446.
Radford, A., Wu, J., Child, R., Luan, D., Amodei, URLhttps://aclanthology.org/W18-5446.

### D., and Sutskever, I. Language models are unsu-

Yang,G.Scalinglimitsofwideneuralnetworkswithweight
pervised multitask learners. 2019. URL https:
sharing: Gaussian process behavior, gradient indepen-
//api.semanticscholar.org/CorpusID:
dence,andneuraltangentkernelderivation,2020.
160025533.
Zhang, F. F., Li, L., Chen, J.-C., Jiang, Z., Wang, B.,

### Recht, B., Fazel, M., and Parrilo, P. A. Guaranteed

and Qian, Y. Increlora: Incremental parameter alminimum-ranksolutionsoflinearmatrixequationsvia
location method for parameter-efficient fine-tuning.
nuclear norm minimization. SIAM Review, 52(3):

### ArXiv, abs/2308.12043, 2023a. URL https:

471–501, January 2010. ISSN 1095-7200. doi: 10.
//api.semanticscholar.org/CorpusID:
1137/070697835. URL http://dx.doi.org/10.
261076438.
1137/070697835.

### Zhang,G.,Chiu,H.-M.,andZhang,R.Y. Fastandminimax

Rombach, R., Blattmann, A., Lorenz, D., Esser, P., and optimalestimationoflow-rankmatricesvianon-convex
Ommer, B. High-resolution image synthesis with la- gradientdescent,2023b.
tentdiffusionmodels. InProceedingsoftheIEEE/CVF
ConferenceonComputerVisionandPatternRecognition Zhang, G., Fattahi, S., and Zhang, R. Y. Preconditioned
(CVPR),pp.10684–10695,June2022. gradientdescentforoverparameterizednonconvexburer–
monteirofactorizationwithglobaloptimalitycertification,
Ryu, S. Low-rank adaptation for fast text-to-image 2023c.
diffusion fine-tuning. https://github.com/
Zhang, Q., Chen, M., Bukharin, A., He, P., Cheng, Y.,
cloneofsimo/lora/tree/master,2023.
Chen,W.,andZhao,T. Adaptivebudgetallocationfor
parameter-efficientfine-tuning,2023d.

### Schoenholz, S. S., Gilmer, J., Ganguli, S., and Sohl-

Dickstein,J. Deepinformationpropagation,2017. Zi,B.,Qi,X.,Wang,L.,Wang,J.,Wong,K.-F.,andZhang,

### L. Delta-lora: Fine-tuninghigh-rankparameterswiththe

Stanley,R.P.etal. Anintroductiontohyperplanearrangedeltaoflow-rankmatrices,2023.
ments. Geometriccombinatorics,13(389-496):24,2004.
11

<!-- Page 12 -->

RiemannianPreconditionedLoRA

### A.DetailsofTheorem4.1


### A.1.AssumptionsandTechnicalLemmas

DefinitionA.1. (StableFeatureLearning)ConsideranygeneralLoRAlayerBAxwithB ∈Rm×r andA∈Rr×nbeing
LoRAparameters. Denote∆t = B A x−B A xforfine-tuningstept. WesaythatLoRAmodelachievesStable
t t t−1 t−1
FeatureLearningwhenx,Ax,BAx∈Θ(1)forallLoRAlayersand∆t ∈Θ(1)forallfine-tuningstept.
Assumption A.2. We assume that the Adam gradient processing step satisfies gt x = Θ(n) for all t where gt is the

## A A

normalizedgradientofAint-thiteration.
ExplanationofAssumptionA.2. WeadoptthesameassumptionasAssumption1in(Hayouetal.,2024)wheretheauthors
provideaproofforAdamwithnomomentum,i.e.,forSignSGDmethod. ThisassumptionshouldholdforgeneralAdam
variantsaslongastheprocessedgradientpreservesthesign(x)direction.
LemmaA.3. ForanymatrixA∈Rm×n,wherembeingpowersofn,suchthatATAisinvertibleandγ[A ]=cforall
ij
(i,j),wehaveγ[(ATA)−1]=−γ[∥a∥2]withabeinganycolumnofA.
Proof. Firstwenotethat(ATA)−1 =adj(ATA)/det(ATA)anddet(ATA)=Θ((mn2c)n).Furthermore,bypropertyof
adjugatematrix,
det(adj(ATA))=(det(ATA))n−1 =Θ((mn2c)n(n−1)),
fromwhichwededuce
adj(ATA)=Θ((mn2c)n−1).

### Therefore,

(ATA)−1 =Θ((mn2c)−1).
Notethat∥a∥2 =Θ(mn2c),wethusconcludeγ[(ATA)−1]=−γ[∥a∥2],asdesired.

### A.2.StatementandProofofTheorem4.1


### Now,westatetheformalversionofourTheorem4.1below,

TheoremA.4. (StableFeatureLearning(Formal))Letg andg denotetheprocessedgradientofAandBrespectively.

## A B

ConsiderLoRAparametersAandBtrainedwithAdamscaledbypreconditioner(1). AssumeAssumptionA.2issatisfied
withAdamgradientprocessingandg ,g ∈Θ(1)afterthegradientprocessing. FurtherassumeBAxhasdimensionof

## A B

Θ(n).ThentheLoRAmodelachievesstablefeaturelearningwithη =Θ(1).WhileforunscaledAdam,η =Θ(n−1)and

## A

η =Θ(1)arerequiredforstablefeaturelearning.

## B

Proof. WeconsiderGaussianinitializationwithA ∼ N(0,σ2)andB ∼ N(0,σ2).Conventionally,wewantBAto
ij a ij b
beinitializedaszeroandAxdoesnotexplodewithNNwidth,thusweproceedwithσ2 =Θ(n−1)andσ2 =0.Wefirst
a b
decomposetheLoRAincrementas
∆t =B A x−B A x
t t t−1 t−1
=(B −ηgt−1(A AT )−1)(A −η(BT B )−1gt−1)x−B A x
t−1 B t−1 t−1 t−1 t−1 t−1 A t−1 t−1
=−ηB (BT B )−1gt−1x−ηgt−1(A AT )−1A x+η2gt−1(A AT )−1(BT B )−1gt−1x.
t−1 t−1 t−1 A B t−1 t−1 t−1 B t−1 t−1 t−1 t−1 A
Wewrite

δ1 =ηB (BT B )−1gt−1x,
 t t−1 t−1 t−1 A
δ2 =ηgt−1(A AT )−1A x,
t B t−1 t−1 t−1
δ3 =η2gt−1(A AT )−1(BT B )−1gt−1x.
t B t−1 t−1 t−1 t−1 A
FollowingAssumptionA.2,weknowgt−1x∈Θ(n),thushavingδ1,δ2,B A x∈Θ(1)equatesto
A t t t−1 t−1

γ[η]+γ[B ]+γ[(BT B )−1]+1=0,
 t−1 t−1 t−1
γ[η]+γ[(A AT )−1]+γ[A x]=0, (4)
t−1 t−1 t−1
γ[B
]+γ[A x]=0.
t−1 t−1
12

<!-- Page 13 -->

RiemannianPreconditionedLoRA
Forgradientupdate,wehave
B =B −ηgt−1(A AT )−1
t t−1 B t−1 t−1
A x=A x−η(BT B )−1gt−1x,
t t−1 t−1 t−1 A
andthus
γ[B ]=max(γ[B ],γ[η]+γ[(A AT )−1])
t t−1 t−1 t−1
γ[A x]=max(γ[A x],γ[η]+γ[(BT B )−1]+1).
t t−1 t−1 t−1
NoteA =A andthusγ[A x]=γ[A x]=0.Furthermore,γ[B ]=γ[η]+γ[(A AT)−1].Sinceγ[∥a ∥2]=0forany
1 0 1 0 1 0 0 0 2
rowa ofA ,γ[(A AT)−1] = 0byLemmaA.3. Thereforeγ[B ] = 0.Sinceγ(∥b ∥2) = 1foranycolumnb ofB ,
0 0 0 0 1 1 2 1 1
γ[(BTB )−1] = −1byLemmaA.3andthusγ[A x] = 0bytheaboverecursion. SinceA = A −η(BTB )−1g1 =

## 1 1 2 2 1 1 1 A

A −Θ(n−1),γ[∥a ∥2] = 0 for any row a of A and again by Lemma A.3 we know γ[(A AT)−1] = 0. Therefore
0 2 2 2 2 2
γ[B ] = 0. The recursion persists and we know γ[B ] = γ[A x] = 0 for all t. Since γ[(BT B )−1] = −1 and
2 t t t−1 t−1
γ[(A AT )−1]=0,allequationsin(4)aresatisfied. Onecancheckthatδ3 ∈Θ(1)andthereforestablefeaturelearning
t−1 t−1 t
isachieveswithη =Θ(1).Theorem1in(Hayouetal.,2024)showsthatη =Θ(n−1)andη =Θ(1)arerequiredfor

## A B

unpreconditionedLoRAtrainingtoachievestablefeaturelearning.

### A.3.ExplanationofDifferentLearningRates

Herewenotethatlearningrateη =Θ(1)isrequiredforTheorem4.1whilelearningrateη =Θ(n−1)isusedforourtoy
exampledescribedinSection4. Thisdiscrepancyarisesfromdifferentsettingsbeingconsideredinthesetworegimes.
Specifically, Theorem 4.1 deals with vector output, i.e., we assume BAx is of dimension Θ(n). This is core to our
preconditionersincewethenhaveγ[(BT B )−1]=−1fromγ[B ]=0.Forscalaroutputasconsideredinthetoy
t−1 t−1 t−1
example, whenγ[B ] = 0, wewillhaveγ[(BT B )−1] = 0andthusfailtoscalethestaticscorrectly. Thenone
t−1 t−1 t−1
wouldwonderforscalaroutput,whethersettingη =Θ(n−1)wouldbethecorrectchoiceasinthetoyexample. Thisis
nolongertrueduetoourAssumptionA.2. Inthetoyexample, wehavegt = (f (x)−y)bxandgtT x = Θ(n)isnot
a t a
guaranteedsinceitalsoscaleswithf (x)andb. Instead,Theorem4.1wouldholdforscalaroutputwithη =Θ(1)and
t 1
η =Θ(n−1)fort>1whichwedonotincludeinthetheoremstatementforsimplicityandonecandeducefollowingour
t
prooftechniqueofTheorem4.1. Thetakeawayisthatforscalaroutput,ourpreconditionercanstillachievestablefeature
learningwithsameorderofmagnitudelearningrateforbothAandBthoughonemayneedtotunelearningratesacross
iterations,whichisthecurrentconventionoflearningratescheduling.

### B.ProofofTheorem7.4

Noteproblem(3)isequivalenttotheproblembelowuptoachangeoflabels,

## P

(cid:88)
min ∥ C A BT −Y∥2, (5)
i i i F
Ai,Bi
i=1
where C ∈ Rn×d,A ∈ Rd×r,B ∈ Rc×r,Y ∈ Rn×c. Consider Y = (cid:80)P C AiBiT . Denote Xi = AiBiT =
i i i i=1 i ⋆ ⋆ ⋆ ⋆ ⋆
UiΣiViT whereUiΣiViT isthesingularvaluedecompositionofXi. DenoteFi = [Ai,Bi]T.ForanyF = [A,B]T,
⋆ ⋆ ⋆ ⋆ ⋆ ⋆ ⋆ ⋆ ⋆ ⋆
considerthefollowingdistancemetric
dist2(F,Fi)= inf (cid:13) (cid:13)(AQ−Ai)Σi1/2 (cid:13) (cid:13) 2 + (cid:13) (cid:13)(BQ−T −Bi)Σi1/2 (cid:13) (cid:13) 2 , (6)
⋆ (cid:13) ⋆ ⋆ (cid:13) (cid:13) ⋆ ⋆ (cid:13)

### Q∈GL(r) F F

whereGL(r)denotesthesetofinvertiblematrixinRr×r. Letσ (·)denotetherthlargestsingularvalueandκ denote
r i
conditionnumberofXi. ConsiderthefollowingscaledGDstep:
⋆
Ai =Ai−ηCT( (cid:88) C AjBjT −Y)Bi(BiT Bi)−1,
t+1 t i j t t t t t
j
Bi =Bi−η(CT( (cid:88) C AjBjT −Y))TAi(AiT Ai)−1.
t+1 t i j t t t t t
j
13

<!-- Page 14 -->


### RiemannianPreconditionedLoRA

Beforewebeginthemainproof,weneedthefollowingpartialFrobeniusnormwhichhasbeenintroducedinSectionA.3in
(Tongetal.,2021b)withsomeimportantpropertiesstudiedthere.
DefinitionB.1. (PartialFrobeniusnorm)ForanymatrixX,itspartialFrobeniusnormoforderrisgivenbyl normof
2
vectorscomposedbyitstop-rsingularvalues,
(cid:118)
(cid:117) r
(cid:117)(cid:88)

## ∥X∥


### F,r

=(cid:116) σ
i

## 2(X).

i=1
Nowwestarttheproofbyfirstprovingsomeusefullemmas.
LemmaB.2. UnderAssumption7.2,letFi =[Ai,Bi]T,thentheextentedspectralinitializationinDefinition7.3satisfies
0 0 0
√
dist(Fi,Fi)≤10δi rκ σ (Xi).
0 ⋆ 2r i r ⋆
Proof. AccordingtoLemma11in(Tongetal.,2021b),sinceAiBiT −Xi hasrankatmost2r,
0 0 ⋆
(cid:113)√
dist(Fi,Fi)≤ 2+1∥AiBiT −Xi∥ ,

## 0 ⋆ 0 0 ⋆ F

(cid:113) √
≤ 2( 2+1)∥AiBiT −Xi∥ .
0 0 ⋆ F,r
SinceAiBiT isthebestrankrapproximationofCTY = (cid:80)P CTC Xj. Then
0 0 i j=1 i j ⋆

## P P

∥AiBiT −Xi∥ ≤∥ (cid:88) CTC Xj −AiBiT ∥ +∥ (cid:88) CTC Xj −Xi∥ ,
0 0 ⋆ F,r i j ⋆ 0 0 F,r i j ⋆ ⋆ F,r
j=1 j=1
(cid:88)
≤2∥(CTC −I)Xi + CTC Xj∥ ,
i i ⋆ i j ⋆ F,r
j̸=i
(cid:88)
≤2δi ∥Xi∥ +2 ∥CTC Xj∥ ,
2r ⋆ F i j ⋆ F
j̸=i
wherethelastinequalityfollowsLemma15andinequality(50)in(Tongetal.,2021b). Therefore,
(cid:88)
dist(Fi,Fi)≤5δi ∥Xi∥ +5 ∥CTC Xj∥ ,
0 ⋆ 2r ⋆ F i j ⋆ F
j̸=i
√
≤10δi ∥Xi∥ ≤10δi rκ σ (Xi).
2r ⋆ F 2r i r ⋆
LemmaB.3. (Contraction)Underassumption7.2withδi ≤0.01. Ifthet-thiteratesatisfiesdist(Fi,Fi)≤0.1σ (Xi)
2r t ⋆ r ⋆
where Fi = [Ai,Bi]T, then ∥AiBiT −Xi∥ ≤ 1.5dist(Fi,Fi). In addition, if the step size 0 < η ≤ 2/3, then the
t t t t t ⋆ F t ⋆
(t+1)-thiterationFi satisfies
t+1
max(dist(Fi ,Fi))≤(1−0.5η)max(dist(Fi,Fi)).
t+1 ⋆ t ⋆
Proof. Wefirstshow∥AiBiT −Xi∥ ≤1.5dist(Fi,Fi).AccordingtoLemma9in(Tongetal.,2021b),weknowQi,the
t t ⋆ F t ⋆ t
optimalalignmentmatrixbetweenFiandFi,i.e.,theoptimalvalueofproblem(5)withF replacedbyFiisattainedatQi,
t ⋆ t t
exists,denoteAi =AiQi,Bi =BiQi−T ,△i =Ai−Ai,△i =Bi−Bi.Byderivation(45)in(Tongetal.,2021b),we
t t t t A ⋆ B ⋆
furtherknowforϵ=0.1,
∥△i Σi−1/2 ∥ ∨∥△i Σi−1/2 ∥ ≤ϵ,

## A ⋆ 2 B ⋆ 2

14

<!-- Page 15 -->

RiemannianPreconditionedLoRA
where∨denotesmaximum. Note
∥AiBiT −Xi∥ =∥AiBiT −Xi∥
t t ⋆ F ⋆ F
=∥△i BiT +Ai△i T ∥

## A ⋆ B F

=∥△i △i T +△i BiT +Ai△i T ∥

## A B A ⋆ ⋆ B F

≤∥△i △i T ∥ +∥△i BiT ∥ +∥Ai△i T ∥

## A B F A ⋆ F ⋆ B F

=∥△i Σi1/2 ∥ +∥△i Σi1/2 ∥ +∥△i △i T ∥

### A ⋆ F B ⋆ F A B F (7)

≤∥△i Σi1/2 ∥ +∥△i Σi1/2 ∥ +

## A ⋆ F B ⋆ F

1 (∥△i Σi−1/2 ∥ ∨∥△i Σi−1/2 ∥ )(∥△i Σi1/2 ∥ +∥△i Σi1/2 ∥ )
2 A ⋆ 2 B ⋆ 2 A ⋆ F B ⋆ F
≤(1+ ϵ )(∥△i Σi1/2 ∥ +∥△i Σi1/2 ∥ )

## 2 A ⋆ F B ⋆ F

ϵ √
≤(1+ ) 2dist(Fi,Fi)≤1.5dist(Fi,Fi).
2 t ⋆ t ⋆
(cid:113)
Notethesecondlastinequalityfollowsfromdist(Fi,Fi)= ∥△i Σi1/2∥2 +∥△i Σi1/2∥2. Wethenproceedtoshow
t ⋆ A ⋆ F B ⋆ F
thecontractionofdistance. Bydefinition,
dist2(Fi ,Fi)≤∥(Ai Qi−Ai)Σi1/2 ∥2 +∥(Bi Qi−T −Bi)Σi1/2 ∥2.
t+1 ⋆ t+1 t ⋆ ⋆ F t+1 t ⋆ ⋆ F
SubstitutetheupdateruleforLi weget
t+1
(Ai Qi−Ai)Σi1/2 =(AiQi−ηCT( (cid:88) C AjBjT −Y)Bi(BiT Bi)−1Qi−Ai)Σi1/2
t+1 t ⋆ ⋆ t t i j t t t t t t ⋆ ⋆
j
=(△i −ηCT( (cid:88) C AjBjT −Y)Bi(BiT Bi)−1Qi)Σi1/2
A i j t t t t t t ⋆
j
=(△i −ηCT( (cid:88) C AjBjT −Y)Bi(BiT Bi)−1)Σi1/2
A i j t t ⋆
j
=(△i −ηCTC (AiBiT −Xi)Bi(BiT Bi)−1−ηCBi(BiT Bi)−1)Σi1/2

### A i i ⋆ ⋆

whereC = (cid:88) CTC (AjBjT −Xj),
i j t t ⋆
j̸=i
=(△i −η(AiBiT −Xi)Bi(BiT Bi)−1−η(CTC −I)(AiBiT −Xi)Bi(BiT Bi)−1

### A ⋆ i i ⋆

−ηCBi(BiT Bi)−1)Σi1/2
⋆
sinceAiBiT −Xi =△i BiT +Ai△i T ,

## ⋆ A ⋆ B

=(△i −η△i −ηAi△i T Bi(BiT Bi)−1−η(CTC −I)(AiBiT −Xi)Bi(BiT Bi)−1

### A A ⋆ B i i ⋆

−ηCBi(BiT Bi)−1)Σi1/2
⋆
=(1−η)△i Σi1/2 −ηAi△i T Bi(BiT Bi)−1Σi1/2 −

## A ⋆ ⋆ B ⋆

η(CTC −I)(AiBiT −Xi)Bi(BiT Bi)−1Σi1/2 −ηCBi(BiT Bi)−1Σi1/2 .
i i ⋆ ⋆ ⋆

### Therefore,

∥(Ai Qi−Ai)Σi1/2 ∥2 =∥(1−η)△i Σi1/2 −ηAi△i T Bi(BiT Bi)−1Σi1/2 ∥2
t+1 t ⋆ ⋆ F A ⋆ ⋆ B ⋆ F
+η2∥(CTC −I)(AiBiT −Xi)Bi(BiT Bi)−1Σi1/2 +CBi(BiT Bi)−1Σi1/2 ∥2
i i ⋆ ⋆ ⋆ F
(8)
−2ηtr(((1−η)Σi1/2 △i T −ηΣi1/2 (BiT Bi)−1BiT △i AiT )

## ⋆ A ⋆ B ⋆

((CTC −I)(AiBiT −Xi)Bi(BiT Bi)−1Σi1/2 +CBi(BiT Bi)−1Σi1/2 )).
i i ⋆ ⋆ ⋆
15

<!-- Page 16 -->


### RiemannianPreconditionedLoRA

Followderivation(46)in(Tongetal.,2021b),wecanbound
∥(1−η)△i Σi1/2 −ηAi△i T Bi(BiT Bi)−1Σi1/2 ∥2

## A ⋆ ⋆ B ⋆ F

≤ (cid:18) (1−η)2+ 2ϵη(1−η) (cid:19) ∥△i Σi1/2 ∥2 + η2(2ϵ+ϵ2) ∥△i Σi1/2 ∥2. (9)
1−ϵ A ⋆ F (1−ϵ)2 B ⋆ F

### Next,wewanttobound

∥(CTC −I)(AiBiT −Xi)Bi(BiT Bi)−1Σi1/2 +CBi(BiT Bi)−1Σi1/2 ∥2
i i ⋆ ⋆ ⋆ F
=∥(CTC −I)(AiBiT −Xi)Bi(BiT Bi)−1Σi1/2 ∥2 +∥CBi(BiT Bi)−1Σi1/2 ∥2
i i ⋆ ⋆ F ⋆ F
+2tr(((CTC −I)(AiBiT −Xi)Bi(BiT Bi)−1Σi1/2 )TCBi(BiT Bi)−1Σi1/2 ).
i i ⋆ ⋆ ⋆
BytheboundforS inLemma1in(Tongetal.,2021b),wecanbound
4
∥(CTC −I)(AiBiT −Xi)Bi(BiT Bi)−1Σi1/2 ∥2 ≤ δ 2 i r 2 (2+ϵ)2 (∥△i Σi1/2 ∥2 +∥△i Σi1/2 ∥2)
i i ⋆ ⋆ F 2(1−ϵ)2 A ⋆ F B ⋆ F
Wenowproceedtobound∥CBi(BiT Bi)−1Σi1/2 ∥2.AccordingtoLemma9in(Tongetal.,2021b),weknowQjexists,the
⋆ F t
optimalalignmentmatrixbetweenFjandFjexists.DenoteAj =AjQj,Bj =BjQj−T ,△j =Aj−Aj,△j =Bj−Bj.
t ⋆ t t t t A ⋆ B ⋆

### Since

∥CTC (AjBjT −Xj)Bi(BiT Bi)−1Σi1/2 ∥
i j t t ⋆ ⋆ F
=∥CTC (△j △j T +△j BjT +Aj△j T )Bi(BiT Bi)−1Σi1/2 ∥
i j A B A ⋆ ⋆ B ⋆ F
≤∥C i TC j ∥ 2 (∥△j A △j B T ∥ F +∥△j A B ⋆ jT ∥ F +∥Aj ⋆ △j B T ∥ F )∥Bi(BiT Bi)−1Σi ⋆ 1/2 ∥ 2 (10)
byLemma12in(Tongetal.,2021b)and(7),
≤ (2+ϵ)∥C i TC j ∥ 2(∥△j Σj1/2 ∥ +∥△j Σj1/2 ∥ ).
2(1−ϵ) A ⋆ F B ⋆ F

### Thus

∥CBi(BiT Bi)−1Σi1/2 ∥2 ≤(P −1) (cid:88) ∥CTC (AjBjT −Xj)Bi(BiT Bi)−1Σi1/2 ∥2
⋆ F i j t t ⋆ ⋆ F
j̸=i

## ≤(P −1)

(cid:88)(2+ϵ)2∥C
i

## Tc

j
∥2
2(∥△j Σj1/2 ∥2 +∥△j Σj1/2 ∥2).
2(1−ϵ)2 A ⋆ F B ⋆ F
j̸=i

### Nextwebound

|tr(((CTC −I)(AiBiT −Xi)Bi(BiT Bi)−1Σi1/2 )TCBi(BiT Bi)−1Σi1/2 )|
i i ⋆ ⋆ ⋆
≤∥Bi(BiT Bi)−1Σi1/2 ∥2|tr(((CTC −I)(AiBiT −Xi))TC)|
⋆ 2 i i ⋆
byLemma12in(Tongetal.,2021b),
≤ 1 |tr(((CTC −I)(AiBiT −Xi))TC)|
(1−ϵ)2 i i ⋆
byLemma17in(Tongetal.,2021b),sinceC is2r-RIP,
i
≤ δ 2 i r ∥C∥ ∥AiBiT −Xi∥
(1−ϵ)2 F ⋆ F
byderivationin(10),
≤
(cid:88)(1+
2
ϵ)2δ
2
i
r∥CTC ∥ (∥△j Σj1/2 ∥ +∥△j Σj1/2 ∥ )(∥△i Σi1/2 ∥ +∥△i Σi1/2 ∥ ).
(1−ϵ)2 i j 2 A ⋆ F B ⋆ F A ⋆ F B ⋆ F
j̸=i
16

<!-- Page 17 -->

RiemannianPreconditionedLoRA

### Tosummarize,

∥(CTC −I)(AiBiT −Xi)Bi(BiT Bi)−1Σi1/2 +CBi(BiT Bi)−1Σi1/2 ∥2
i i ⋆ ⋆ ⋆ F
≤ δ 2 i r 2 (2+ϵ)2 (∥△i Σi1/2 ∥2 +∥△i Σi1/2 ∥2)+(P −1) (cid:88)∥C i TC j ∥2 2 (2+ϵ)2 (∥△j Σj1/2 ∥2 +∥△j Σj1/2 ∥2)
2(1−ϵ)2 A ⋆ F B ⋆ F 2(1−ϵ)2 A ⋆ F B ⋆ F
j̸=i
+
(cid:88)2(1+
2
ϵ)2σ
2
i
r∥CTC ∥ (∥△j Σj1/2 ∥ +∥△j Σj1/2 ∥ )(∥△i Σi1/2 ∥ +∥△i Σi1/2 ∥ ).
(1−ϵ)2 i j 2 A ⋆ F B ⋆ F A ⋆ F B ⋆ F
j̸=i
(11)

### Finally,wemoveontobound

|tr(((1−η)Σi1/2 △i T −ηΣi1/2 (BiT Bi)−1BiT △i AiT )((CTC −I)(AiBiT −Xi)Bi(BiT Bi)−1Σi1/2 (12)
⋆ A ⋆ B ⋆ i i ⋆ ⋆
+CBi(BiT Bi)−1Σi1/2
))|
⋆
≤|tr((1−η)Σi1/2 △i T (CTC −I)(AiBiT −Xi)Bi(BiT Bi)−1Σi1/2 )|
⋆ A i i ⋆ ⋆
+|tr(ηΣi1/2 (BiT Bi)−1BiT △i AiT (CTC −I)(AiBiT −Xi)Bi(BiT Bi)−1Σi1/2 )|
⋆ B ⋆ i i ⋆ ⋆
+|tr((1−η)Σi1/2 △i T CBi(BiT Bi)−1Σi1/2 )|+|tr(ηΣi1/2 (BiT Bi)−1BiT △i AiT CBi(BiT Bi)−1Σi1/2 )|.

## ⋆ A ⋆ ⋆ B ⋆ ⋆

Firstnoticebytheboundfor|S |inLemma1in(Tongetal.,2021b),
2
|tr((1−η)Σi1/2 △i T (CTC −I)(AiBiT −Xi)Bi(BiT Bi)−1Σi1/2 )|
⋆ A i i ⋆ ⋆
≤ (1−η)δ 2 i r (2+ϵ) ( 3 ∥△i Σi1/2 ∥2 + 1 ∥△i Σi1/2 ∥2). (13)
2(1−ϵ) 2 A ⋆ F 2 B ⋆ F
Similarly,bytheboundfor|S |inLemma1in(Tongetal.,2021b),
3
|tr(ηΣi1/2 (BiT Bi)−1BiT △i AiT (CTC −I)(AiBiT −Xi)Bi(BiT Bi)−1Σi1/2 )|
⋆ B ⋆ i i ⋆ ⋆
≤ ηδ 2 i r (2+ϵ) ( 3 ∥△i Σi1/2 ∥2 + 1 ∥△i Σi1/2 ∥2). (14)
2(1−ϵ)2 2 B ⋆ F 2 A ⋆ F

### Next,considerbounding

|tr((1−η)Σi1/2 △i T CBi(BiT Bi)−1Σi1/2 )|

## ⋆ A ⋆

≤(1−η) (cid:88) |tr(Σi1/2 △i T CTC (AjBjT −Xj)Bi(BiT Bi)−1Σi1/2 )|
⋆ A i j t t ⋆ ⋆
j̸=i
≤(1−η) (cid:88) ∥CTC ∥ ∥AjBjT −Xj∥ ∥Bi(BiT Bi)−1Σi△i T ∥
i j 2 t t ⋆ F ⋆ A F
j̸=i
byLemma12in(Tongetal.,2021b), (15)
≤ 1−η (cid:88) ∥CTC ∥ ∥AjBjT −Xj∥ ∥△i Σi1/2 ∥
1−ϵ i j 2 t t ⋆ F A ⋆ F
j̸=i
byderivationin(7),
≤ (2+ϵ)(1−η)(cid:88) ∥CTC ∥ (∥△j Σj1/2 ∥ +∥△j Σj1/2 ∥ )∥△i Σi1/2 ∥ ,
2(1−ϵ) i j 2 A ⋆ F B ⋆ F A ⋆ F
j̸=i
17

<!-- Page 18 -->

RiemannianPreconditionedLoRA
and
|tr(ηΣi1/2 (BiT Bi)−1BiT △i AiT CBi(BiT Bi)−1Σi1/2 )|

## ⋆ B ⋆ ⋆

=η|tr( (cid:88) CTC (AjBjT −Xj)Bi(BiT Bi)−1Σi(BiT Bi)−1BiT △i AiT )|
i j t t ⋆ ⋆ B ⋆
j̸=i
≤η (cid:88) ∥CTC ∥ ∥AjBjT −Xj∥ ∥Bi(BiT Bi)−1Σi(BiT Bi)−1BiT △i AiT ∥
i j 2 t t ⋆ F ⋆ B ⋆ F
j̸=i
≤η (cid:88) ∥CTC ∥ ∥AjBjT −Xj∥ ∥Bi(BiT Bi)−1Σi1/2 ∥2∥△i LiT ∥
i j 2 t t ⋆ F ⋆ 2 B ⋆ F
j̸=i (16)
byLemma12in(Tongetal.,2021b),
≤ η (cid:88) ∥CTC ∥ ∥AjBjT −Xj∥ ∥△i AiT ∥
(1−ϵ)2 i j 2 t t ⋆ F B ⋆ F
j̸=i
byderivationin(7),
≤ η(2+ϵ) (cid:88) ∥CTC ∥ (∥△j Σj1/2 ∥ +∥△j Σj1/2 ∥ )∥△i AiT ∥ .
2(1−ϵ)2 i j 2 A ⋆ F B ⋆ F B ⋆ F
j̸=i

### Combine(13),(14),(15),(16)tobound(12)

|tr(((1−η)Σi1/2 △i T −ηΣi1/2 (BiT Bi)−1BiT △i AiT )((CTC −I)(AiBiT −Xi)Bi(BiT Bi)−1Σi1/2
⋆ A ⋆ B ⋆ i i ⋆ ⋆
+CBi(BiT Bi)−1Σi1/2
))|
⋆
≤ (1−η)δ 2 i r (2+ϵ) ( 3 ∥△i Σi1/2 ∥2 + 1 ∥△i Σi1/2 ∥2)+ ηδ 2 i r (2+ϵ) ( 3 ∥△i Σi1/2 ∥2 + 1 ∥△i Σi1/2 ∥2)
2(1−ϵ) 2 A ⋆ F 2 B ⋆ F 2(1−ϵ)2 2 B ⋆ F 2 A ⋆ F
+ (2+ϵ)(1−η)(cid:88) ∥CTC ∥ (∥△j Σj1/2 ∥ +∥△j Σj1/2 ∥ )∥△i Σi1/2 ∥
2(1−ϵ) i j 2 A ⋆ F B ⋆ F A ⋆ F
j̸=i
+ η(2+ϵ) (cid:88) ∥CTC ∥ (∥△j Σj1/2 ∥ +∥△j Σj1/2 ∥ )∥△i LiT ∥ (17)
2(1−ϵ)2 i j 2 A ⋆ F B ⋆ F B ⋆ F
j̸=i
≤ (1−η)δ 2 i r (2+ϵ) ( 3 ∥△i Σi1/2 ∥2 + 1 ∥△i Σi1/2 ∥2)+ ηδ 2 i r (2+ϵ) ( 3 ∥△i Σi1/2 ∥2 + 1 ∥△i Σi1/2 ∥2)
2(1−ϵ) 2 A ⋆ F 2 B ⋆ F 2(1−ϵ)2 2 B ⋆ F 2 A ⋆ F
+ (2+ϵ)(1−η)(cid:88) ∥CTC ∥ ( 1 ∥△j Σj1/2 ∥2 + 1 ∥△j Σj1/2 ∥2 +∥△i Σi1/2 ∥2)
2(1−ϵ) i j 2 2 A ⋆ F 2 B ⋆ F A ⋆ F
j̸=i
+ η(2+ϵ) (cid:88) ∥CTC ∥ ( 1 ∥△j Σj1/2 ∥2 + 1 ∥△j Σj1/2 ∥2 +∥△i LiT ∥2).
2(1−ϵ)2 i j 2 2 A ⋆ F 2 B ⋆ F B ⋆ F
j̸=i

### Substitutingbounds(9),(11),(17),wederiveboundfor(8)as

∥(Ai Qi−Ai)Σi1/2 ∥2 ≤((1−η)2+ 2ϵη(1−η) )∥△i Σi1/2 ∥2 + η2(2ϵ+ϵ2) ∥△i Σi1/2 ∥2
t+1 t ⋆ ⋆ F 1−ϵ A ⋆ F (1−ϵ)2 B ⋆ F
+η2( δ 2 i r 2 (2+ϵ)2 (∥△i Σi1/2 ∥2 +∥△i Σi1/2 ∥2)
2(1−ϵ)2 A ⋆ F B ⋆ F
+(P −1) (cid:88)∥C i TC j ∥2 2 (2+ϵ)2 (∥△j Σj1/2 ∥2 +∥△j Σj1/2 ∥2)
2(1−ϵ)2 A ⋆ F B ⋆ F
j̸=i
+
(cid:88)2(1+
2
ϵ)2δ
2
i
r∥CTC ∥(∥△j Σj1/2 ∥ +∥△j Σj1/2 ∥ )(∥△i Σi1/2 ∥
(1−ϵ)2 i j A ⋆ F B ⋆ F A ⋆ F
j̸=i
18

<!-- Page 19 -->


### RiemannianPreconditionedLoRA

+∥△i Σi1/2 ∥ ))+2η( (1−η)δ 2 i r (2+ϵ) ( 3 ∥△i Σi1/2 ∥2 + 1 ∥△i Σi1/2 ∥2)

### B ⋆ F 2(1−ϵ) 2 A ⋆ F 2 B ⋆ F

+ ηδ 2 i r (2+ϵ) ( 3 ∥△i Σi1/2 ∥2 + 1 ∥△i Σi1/2 ∥2)
2(1−ϵ)2 2 B ⋆ F 2 A ⋆ F
+ (2+ϵ)(1−η)(cid:88) ∥CTC ∥ ( 1 ∥△j Σj1/2 ∥2 + 1 ∥△j Σj1/2 ∥2 +∥△i Σi1/2 ∥2)
2(1−ϵ) i j 2 2 A ⋆ F 2 B ⋆ F A ⋆ F
j̸=i
+ η(2+ϵ) (cid:88) ∥CTC ∥ ( 1 ∥△j Σj1/2 ∥2 + 1 ∥△j Σj1/2 ∥2 +∥△i AiT ∥2)).
2(1−ϵ)2 i j 2 2 A ⋆ F 2 B ⋆ F B ⋆ F
j̸=i
Wesimilarlyderiveboundfor∥(Bi Qi−T −Bi)Σi1/2 ∥2. Sincedist2(Fi,Fi)=tr(△i Σi△i T )+tr(△i Σi△i T ),we
t+1 t ⋆ ⋆ F t ⋆ A ⋆ A B ⋆ B
thusget
∥(Ai Qi−Ai)Σi1/2 ∥2 +∥(Bi Qi−T −Bi)Σi1/2 ∥2
t+1 t ⋆ ⋆ F t+1 t ⋆ ⋆ F
≤((1−η)2+ 2ϵη(1−η) )(∥△i Σi1/2 ∥2 +∥△i Σi1/2 ∥2)+ η2(2ϵ+ϵ2) (∥△i Σi1/2 ∥2 +∥△i Σi1/2 ∥2)
1−ϵ A ⋆ F B ⋆ F (1−ϵ)2 B ⋆ F A ⋆ F
+η2( δ 2 i r 2 (2+ϵ)2 (2∥△i Σi1/2 ∥2 +2∥△i Σi1/2 ∥2)+(P −1) (cid:88)∥C i TC j ∥2 2 (2+ϵ)2 (2∥△j Σj1/2 ∥2
2(1−ϵ)2 A ⋆ F B ⋆ F 2(1−ϵ)2 A ⋆ F
j̸=i
+2∥△j Σj1/2 ∥2)+
(cid:88)2(1+
2
ϵ)2δ
2
i
r∥CTC ∥(2∥△j Σj1/2 ∥ +2∥△j Σj1/2 ∥ )(∥△i Σi1/2 ∥
B ⋆ F (1−ϵ)2 i j A ⋆ F B ⋆ F A ⋆ F
j̸=i
+∥△i Σi1/2 ∥ ))+2η( (1−η)δ 2 i r (2+ϵ) (2∥△i Σi1/2 ∥2 +2∥△i Σi1/2 ∥2)

### B ⋆ F 2(1−ϵ) A ⋆ F B ⋆ F

+ ηδ 2 i r (2+ϵ) (2∥△i Σi1/2 ∥2 +2∥△i Σi1/2 ∥2)+ (2+ϵ)(1−η)(cid:88) ∥CTC ∥ (∥△j Σj1/2 ∥2
2(1−ϵ)2 B ⋆ F A ⋆ F 2(1−ϵ) i j 2 A ⋆ F
j̸=i
+∥△j Σj1/2 ∥2 +∥△i Σi1/2 ∥2 +∥△i Σi1/2 ∥2)+ η(2+ϵ) (cid:88) ∥CTC ∥ (∥△j Σj1/2 ∥2+
B ⋆ F A ⋆ F B ⋆ F 2(1−ϵ)2 i j 2 A ⋆ F
j̸=i
∥△j Σj1/2 ∥2 +∥△i AiT ∥2 +∥△i AiT ∥2))

## B ⋆ F B ⋆ F A ⋆ F

2ϵη(1−η) η2(2ϵ+ϵ2) η2δi 2 (2+ϵ)2
≤((1−η)2+ + + 2r )dist2(Fi,Fi)
1−ϵ (1−ϵ)2 (1−ϵ)2 t ⋆
+
(cid:88)(P −1)η2(2+ϵ)2∥C
i

## Tc

j
∥2
2dist2(Fj,Fj)
(1−ϵ)2 t ⋆
j̸=i
+
(cid:88)8η2(1+
2
ϵ)2δ
2
i
r∥CTC ∥dist(Fi,Fi)dist(Fj,Fj)+
2η(1−η)δ
2
i
r
(2+ϵ)
dist2(Fi,Fi)
(1−ϵ)2 i j t ⋆ t ⋆ (1−ϵ) t ⋆
j̸=i
2η2δi (2+ϵ) (cid:88)η(2+ϵ)(1−η)
+ 2r dist2(Fi,Fi)+ ∥CTC ∥ dist2(Fj,Fj)
(1−ϵ)2 t ⋆ 1−ϵ i j 2 t ⋆
j̸=i
+
η(2+ϵ)(1−η) (cid:80)
j̸=i

## ∥C

i

## Tc

j
∥
2 dist2(Fi,Fi)+
(cid:88)η2(2+ϵ)
∥CTC ∥ dist2(Fj,Fj)
(1−ϵ) t ⋆ (1−ϵ)2 i j 2 t ⋆
j̸=i
+
(cid:88)η2(2+ϵ)∥C
i

## Tc

j
∥
2 dist2(Fi,Fi)
(1−ϵ)2 t ⋆
j̸=i
2ϵη(1−η) η2(2ϵ+ϵ2) η2δi 2 (2+ϵ)2 2η(1−η)δi (2+ϵ) 2η2δi (2+ϵ)
=((1−η)2+ + + 2r + 2r + 2r
1−ϵ (1−ϵ)2 (1−ϵ)2 (1−ϵ) (1−ϵ)2
η(2+ϵ)(1−η) (cid:80) ∥CTC ∥ η2(2+ϵ) (cid:80) ∥CTC ∥
+ j̸=i i j 2 + j̸=i i j 2 )dist2(Fi,Fi)
(1−ϵ) (1−ϵ)2 t ⋆
19

<!-- Page 20 -->


### RiemannianPreconditionedLoRA

+ (cid:88) ( (P −1)η2∥C i TC j ∥2(2+ϵ)2 + η(2+ϵ)(1−η)∥C i TC j ∥ 2 + η2(2+ϵ)∥C i TC j ∥ 2)dist2(Fj,Fj)
(1−ϵ)2 (1−ϵ) (1−ϵ)2 t ⋆
j̸=i
+
(cid:88)8η2(1+
2
ϵ)2δ
2
i
r∥CTC ∥ dist(Fi,Fi)dist(Fj,Fj)
(1−ϵ)2 i j 2 t ⋆ t ⋆
j̸=i
Letσ denote∥CTC ∥ ,
ij i j 2
7(cid:88) 7 (cid:88) (cid:88) 7 7 49
≤((1−0.6η)2+ σ η+ σ η2)dist2(Fi,Fi)+ ( σ η+( σ + (P −1)σ2)η2)dist2(Fj,Fj)
3 ij 27 ij t ⋆ 3 ij 27 ij 9 ij t ⋆
j̸=i j̸=i j̸=i
(cid:88)
+ 0.3σ η2dist(Fi,Fi)dist(Fj,Fj)
ij t ⋆ t ⋆
j̸=i
Letσ =max(σ )overallj,whenσ,η ≤1,
ij
(cid:88)
≤((1−0.6η)2+3(P −1)ση)dist2(Fi,Fi)+ (3σ+6(P −1)σ2)ηdist2(Fj,Fj)
t ⋆ t ⋆
j̸=i
(cid:88)
+ 0.3σηdist(Fi,Fi)dist(Fj,Fj)
t ⋆ t ⋆
j̸=i
WLOGassumedist2(Fk,Fk)≥dist2(Fj,Fj)foranyj ̸=k.Thenwhenσ ≤min(1, 0.12 ),
t ⋆ t ⋆ 7P(P+1)
(cid:88) (cid:88)
((1−0.6η)2+3(P −1)ση)dist2(Fk,Fk)+ (3σ+6(P −1)σ2)ηdist2(Fk,Fk)+ 0.3σηdist2(Fk,Fk)
t ⋆ t ⋆ t ⋆
j̸=i j̸=i
≤(1−0.5η)2dist2(Fk,Fk).
t ⋆

### Therefore,

max(dist2(Fi ,Fi))≤(1−0.5η)2max(dist2(Fi,Fi)).
t+1 ⋆ t ⋆
i i
TheproofofTheorem7.4isasimplecombinationofLemmaB.2andLemmaB.3. Webuildon(Tongetal.,2021b)for
ourproof. Notein(Jiaetal.,2023),theauthorsprovideaproofforglobalconvergenceforscaledGDmethodforleast
squaresmatrixdecompositionproblem. Sincetheproofdetailthereiscloselytailedtotheobjective,westicktothelocal
convergenceproofin(Tongetal.,2021b)whichmoreresemblestheproblemweareinterestedin.

### C.SGDwithGradientScaling

Algorithm2PseudocodeofscaledGDinPyTorch.
# group trainable parameters into LoRA pairs in train.py
for LoRAA, LoRAB in pairwise(trainableparameter):
paramgroups.append({"params": [LoRAA,LoRAB], "lr": learningrate})
# apply preconditioner in optimizer.py
for group in param_groups:

### A, B = group["params"]

dA, dB = group["params"].grad
# precondition gradients
dAscaled =inverse(B.T@B+delta*torch.eye(r)).mm(dA)
dBscaled =dB.mm(inverse(A@A.T+delta*torch.eye(r)))
# update parameters
A.add_(dA_scaled, -group[’lr’])

### B.add_(dB_scaled, -group[’lr’])

pairwise:readeverytwoelementsinalist

### D.MoreonRuntimeComparison

Figure4showsruntimecomparisonforfine-tuningGPT-2modelwithLoRAtrainedwithdiffererntoptimizers,r =256is
adopted. Notethoughtheruntimegapbetweenscaledoptimizersandunscaledonesincreasescomparedtor =4shownin
Section6.2,theincrementisstillmarginal.
20

<!-- Page 21 -->


### RiemannianPreconditionedLoRA

Figure4.RuntimeforLoRAfine-tuningGPT-2mediummodelwithrankr=256withdifferentoptimizers.Ourscaledmethodsintroduce
marginalruntimeoverheadandtrainasfastasunscaledmethods.SeeSection6.3.1forexperimentaldetails.
E.SupplementaryExperimentsforLanguageModels

## E.1.Gpt-2


## E.1.1.Experimentalresultsfordifferentloraranks

ForexperimentsforvaryingLoRAranks,wefollowexactthesamesettingasinoriginalLoRAproject(Huetal.,2021).
Weexperimentwithmedium-sizeGPT-2(Radfordetal.,2019)modelwithhyperparameterslistedinTable3,wherethe
learningratesfordifferentmethodsareindividuallytunedbygridsearchexceptforAdamW,whichwefollowdefaultsetting
inLoRAreport(Huetal.,2021). Wetrainwithalinearlearningrateschedulefor5epochs. Wenotethatwealsotune
hyperparametersβ ,β forAdamW-typemethodsandfindthatlowerβ ,β valuesarebeneficialtoscaledAdamWmethod.
1 2 1 2
SeeTable4forexperimentalresults. WetestwithLoRArankr =1,4,8andmethodwithscaledgradientalwaysperforms
betterthanitsnon-scaledgradientcounterpartforallranksandonmostevaluationmetrics. Wesetregularizationfactorto
beσ =1e−6.
Method SGD scaledGD AdamW scaledAdamW
Rank 1 4 8 1 4 8 1 4 8 1 4 8

### Training

Weightdecay 0.01
DropoutProb 0.1
BatchSize 8
# Epoch 5

### WarmupSteps 500

LRScheduler Linear

### LabelSmooth 0.1

LR(tuned,×10−3) 60 90 20 30 0.2 0.5 0.8 2
AdamWβ / 0.9 0.7
1
AdamWβ / 0.999 0.8
2

### LoRAα 32


### Inference


### BeamSize 10


### LengthPenalty 0.8


### NoRepeatNgramSize 4

Table3. HyperparametersforGPT-2modelfine-tuning
21

<!-- Page 22 -->

RiemannianPreconditionedLoRA

## E2E


### Method Rank


### BLEU NIST MET ROUGE-L CIDEr


## Sgd 1 35.9 5.09 25.3 46.2 0.48

scaledGD(ours) 1 68.2 8.65 45.7 69.6 2.44

### AdamW 1 69.9 8.80 46.5 71.4 2.48

scaledAdamW(ours) 1 70.1 8.82 46.5 71.7 2.51

## Sgd 4 66.6 8.54 44.2 68.2 2.32

scaledGD(ours) 4 69.2 8.71 46.3 70.9 2.48

### AdamW 4 68.9 8.69 46.5 71.3 2.51

scaledAdamW(ours) 4 69.6 8.77 46.6 71.8 2.52

## Sgd 8 65.8 8.46 43.5 68.7 2.33

scaledGD(ours) 8 69.6 8.78 46.4 70.8 2.48

### AdamW 8 69.6 8.74 46.7 71.8 2.53

scaledAdamW(ours) 8 70.1 8.82 46.6 71.8 2.53
Table4.ExperimentsforGPT-2mediummodelonE2ENLGchallengewithdifferentLoRAranks.Ourscaledoptimizersoutperform
unscaledoptimizersforallLoRAranksbeingtestedandonmostevaluationmetrics. Moreover,scaledGDmethodbehavescloseto
AdamWmethod.SeeAppendixE.1.1forexperimentaldetails.

## E.1.2.Experimentalresultsfordifferentmodelsizes

ForGPT-2model,wealsoexperimentwithdifferentmodelsizes. LoRArankrisfixedtobe4. Weusethesametraining
hyperparametersaslistedinTable3. SeeTable5forfinalscores. Noteourscaledgradientmethodsalwaysoutperformtheir
unscaledgradientcounterpartsfordifferentmodelsizesandonmostevaluationmetrics,whichshowsthesuperiorityofthe
introducedpreconditioner. Furthermore,thereisusuallysignificantperformancegapbetweenSGDmethodandAdamW
methodwhileourscaledGDmethodisabletoobtainscorescomparabletoAdamWwithoutrequiringmomentumterms.
OurscaledGDmethodindeedclosesthegapbetweenSGDandAdamW.

## E2E

Method Model #TrainableParameters

### BLEU NIST MET ROUGE-L CIDEr


## Sgd Gpt-2S 0.15M 54.8 4.56 34.0 63.3 1.29

scaledGD(ours) GPT-2S 0.15M 68.5 8.72 45.5 69.4 2.40

### AdamW GPT-2S 0.15M 69.1 8.75 46.0 70.5 2.47

scaledAdamW(ours) GPT-2S 0.15M 69.5 8.80 46.2 70.9 2.48

## Sgd Gpt-2M 0.39M 66.6 8.54 44.2 68.2 2.32

scaledGD(ours) GPT-2M 0.39M 69.2 8.71 46.3 70.9 2.48

### AdamW GPT-2M 0.39M 68.9 8.69 46.5 71.3 2.51

scaledAdamW(ours) GPT-2M 0.39M 69.6 8.77 46.6 71.8 2.52
Table5.ExperimentsforGPT-2modelswithdifferentsizeswithLoRArankr=4onE2ENLGchallenge.Ourscaledoptimizersbehave
betterthanunscaledonesandscaledGDobtainsscorescomparabletoAdamW.SeeAppendixE.1.2forexperimentaldetails.

## E.1.3.Experimentalresultsfordifferentdatasets

WeexperimentwithalsoWebNLG(Gardentetal.,2017)andDART(Nanetal.,2021)datasetswithGPT-2medium-size
modelwithLoRArankr =4. WeuseexactlythesametraininghyperparametersaslistedinTable3. WebNLGisapopular
dataset for data-to-text evaluation introduced by (Gardent et al., 2017) which includes 22K examples from 14 distinct
categories. Amongthesecategories,fivecategoriesarepresentedonlyattesttimeandthustheevaluationisdividedinto
“seen”(S),“unseen”(U),“all”(A)threetypesdependingonwhetherthefivecategoriesareincludedintesttimeornot.
DARTisanotherdata-to-textdatasetintroducedby(Nanetal.,2021)whichinvolves82Kexamples. Theevaluationmetrics
beingusedareBLEU,MET,andTERwithhigherscoresbeingbetterforfirsttwometricsandthelowerthebetterforTER.
TheexperimentalresultispresentedinTable6andweobservethatscaledGDsignificantlyimprovesSGDperformancefor
bothdatasetsonallevaluationmetrics,andsodoesscaledAdamWforAdamW.
22

<!-- Page 23 -->

RiemannianPreconditionedLoRA

### DART WebNLG

Method BLEU↑ MET↑ TER↓

## Bleu↑ Met↑ Ter↓


## U S A U S A U S A


### Sgd 43.2 .36 .50 45.5 58.1 52.4 .36 .42 .39 .45 .36 .40

scaledGD(ours) 46.1 .38 .48 46.3 61.7 54.8 .37 .44 .41 .45 .34 .39

### AdamW 47.1 .38 .47 45.0 64.1 55.5 .38 .45 .42 .47 .32 .39

scaledAdamW(ours) 47.9 .39 .47 46.8 64.2 56.3 .38 .45 .42 .46 .32 .38
Table6.ExperimentsforGPT-2mediummodelonNLGchallengewithDARTdatasetandWebNLGdataset. Ourscaledoptimizers
improveunscaledoptimizersuniformlyonallevaluationmetricsforbothdatasets. SeeAppendixE.1.3forexperiment,datasets,and
metricdetails.

### E.2.Mistral7B

Mistral7Bisaprettynewmodelup-to-dateandthereisnowell-establishedcodebasewecanfollow. Forquickertraining,
weuse4-bitquantizedversionofMistral7BV0.1asourbasemodelandLoRAfactorsareinjectedtoeachlinearlayer
withrankr =16.Wetrainfor5totalepochswithbatchsize8. Forfine-tuning4-bitquantizedMistral7BV0.1modelfor
GLUEbenchmark,weexploitHuggingFacetransformerstrainerclass. Alltrainingargumentsaredefaultthereexceptfor
thebatchsize,trainingepoch,andoptimizer-relatedsettingswhicharecustomizedforourexperiments. SeeTable7for
traininghyperparameterchoices. Theβ’sandϵforAdamW-typemethodsaredefaultlyusedinoriginalLoRAproject(Hu
etal.,2021). Forlearningratechoices,weviewthatvaluesrangingfrom2e−5to2e−4havebeenempiricallyusedfor
fine-tuningMistral7Bforothertasks. Wefollow(Labonne,2024)andsetlr = 5e−5forAdamW-typemethods. For
largerdatasetsincludingmnli,qnli,andqqp,lr =5e−5resultsinNaNlossthuswetunelearningrateindividuallywith
gridsearchforeachmethod. SinceSGDhasneverbeenusedfortrainingMistral7B,weempiricallyfindlr =5e−3to
beareasonablelearningrate. Forlargerdatasetsincludingmnli,qnli,andqqp,westilltunethelearningratewithgrid
search. Learningratescheduler,warmupsteps,warmupratios,andmaxgradnormarealldefaultinHuggingFacetrainer
class. Weightdecayvalue0.01iswhathasbeenusedinoriginalLoRAprojectforGPT-2fine-tuning. Weusethesame
LoRA-relatedparametersandmodelquantizationconfigurationasin(Labonne,2024).
Method SGD scaledGD AdamW scaledAdamW
trainbatchsize 8
seed(default) 42
AdamW(β ,β ) / (0.9,0.999)
1 2
AdamWϵ / 1e−6
lr 5e−3 5e−5
lr(mnli) 5e−3 1e−3 5e−6 3e−5
lr(qqp) 5e−3 4e−3 5e−6 3e−5
lr(qnli) 5e−3 9e−4 1e−5
lrscheduler linear
numepoch 5
warmupsteps&warmupratios 0
weightdecay 0.01
maxgradnorm 1
LoRArank 16

### LoRAα 16

LoRAdropout 0.05

### Loadin4-bit True

4bitquantizationtype nf4
4bitdtype bfloat16
Table7. HyperparametersforMistral7Bmodelfine-tuning
23

<!-- Page 24 -->


### RiemannianPreconditionedLoRA

F.SupplementaryExperimentsforDiffusionModels

### F.1.StableDiffusion

Forourobjectgenerationexperiment,wefollowthepopularcustomdiffusionrepository(Ryu,2023). Wefollowalldefault
settingsforbothtrainingandinferencestepsexceptfortheoptimizercomponent. Weuse“aphotoof⟨V ⟩”asallobject
object
imagecaptions. Intheoriginalrepository,AdamWisusedasdefaultoptimizerwithlearningrate5e−5fortext-encoder
tuningand1e−4forU-Nettuning. ThepretrainedmodelbeingusedisStableDiffusionV1.5(Rombachetal.,2022). For
trainingprocedure,weuseconstantlearningrateschedulerwithzerolearningratewarmupsteps,whichisthedefaultsetting.
Maxtrainingstepissetto4000. Forsamplingprocedure,wesetnumberofinferencestepstobe50andguidancescaletobe
7,whichisusedasdefaultintheexperimentnotebookprovided. Figure5showsgenerationresultsforayellowchairwith
trainingimagescontainingthetargetchairincolorblue. AdamWisabletogeneratethetargetyellowchaironlyforlearning
rate1e−6whileourmethodgeneratesdesiredimagesforalllearningratesbeingtested. Figure6showsgenerationresults
fordogobject. Ourmethodgeneratesimagesbettercapturingtheprompt,i.e,adogwearingahat. Forlargelearningrate
1e−2,AdamWonlygeneratesblackimageswhilenoblackimagesareobservedforscaledAdamWgeneration,which
againverifiestherobustnessofourscaledoptimizers.
Figure5. Generationresultsforprompt“ayellow⟨V ⟩”afterfine-tuningon5bluechairimagesoftheStableDiffusionV1.5model.
chair
Wevarytext-encoderlearningrateswithU-Netlearningratefixedtodefaultvalue1e−4.Noblackimagesareobservedforourmethod’s
generationandAdamWgeneratesonlyblackimagesforlargelearningrates. Ourmethod(scaledAdamW)generatesphotosbetter
capturingthepromptandismorerobusttolearningratechanges.SeeAppendixF.1forexperimentaldetails.
Figure6.Generationresultsforprompt“⟨V ⟩wearingahat”afterfine-tuningon5dogimagesoftheStableDiffusionV1.5model.See
dog
AppendixF.1forexperimentaldetails.Ourmethod(scaledAdamW)generatesimagesbettercapturingtheprompt,i.e.,adogwearinga
hat,andismorerobusttolearningratechanges.

### F.2.Mix-of-Show

Forourexperimentforfacegenerationtasks,webaseourexperimentsonMix-of-Show(Guetal.,2023)repositorywhich
wefindabletogeneratehigh-qualityfaceimagesandisbetterforvisualizationcomparisonbetweendifferentoptimization
24

<!-- Page 25 -->


### RiemannianPreconditionedLoRA

methodsweconsider. Wefollowdefaultsettingsfortrainingandinferencein(Guetal.,2023)withtheexceptionthatwe
turnoffembeddingtuningandonlytunethetextencoderandU-NetfractionwhereLoRAparametersareinjected. The
reasonisthatwefindwithembeddingtuning, theeffectofLoRAparameterisrestrictedandthusdoesnogoodtoour
comparison. InMix-of-Show,Chilloutmix2 isusedaspretrainedmodel. LoRArankissetto4. DMP-Solver(Luetal.,
2022)isemployedforsampling. See(Guetal.,2023)formorediscussiononexperimentaldetails. Herewefirstfixstep
size5e−4forbothtextencodertuningandU-NettuningandcompareAdamWversusscaledAdamWwithdifferentLoRA
parameterfusioncoefficients. ThedefaultstepsizevalueusedforMix-of-Showis1e−5and1e−4fortextencodertuning
andU-NettuningrespectivelyanddefaultoptimizerisAdamW.SeeSectionF.2.1forexperimentalresultsfordifferent
LoRAparameterfusioncoefficients. OurscaledAdamWoptimizergeneratesvisuallybetterimagescomparedtoAdamW
optimizer. Wethentestwithvaryingstepsizesettingsanddemonstratethatourscaledgradientmethodismorerobustto
stepsizechangesinSectionF.2.2.

## F.2.1.Adamwvs. Scaledadamwwithvaryingloraparameterfusioncoefficients

WeexperimentwithPottercharacterandHermionecharacter. ForPottercharacter,weuse14Potterimagesfortraining
LoRAparameterswiththecharacternamereplacebyspecialtoken⟨V ⟩aswhathasbeenintroducedintextualinversion
potter
(Galetal.,2022),theninthesamplingprocedure,weusepromptwithspecialcharacter⟨V ⟩forgeneratingimages
potter
involving Potter character. Figure 7, 8 and 9 show the generation results for three different prompts. The above two
rowsareforAdamWoptimizerwiththefirstrowhavingLoRAparameterfusioncoefficient0.7andsecondrow1and
thethirdandfourthrowscorrespondtoscaledAdamWgeneration. LoRAparameterfusioncoefficientrepresentsαin
W =W +αABT whenmergingLoRAweights. WeobservethatourscaledAdamWmethodisabletogeneratehigher
0
qualityimagescomparedtounscaledversionforbothα=0.7andα=1. ForHermionecharacter,wetrainwith15photos
ofHermionefollowingproceduredescribedbefore. Figure10and11showthegenerationresults. Still,ourscaledAdamW
optimizerproduceshigherqualityimagescomparedtoAdamWoptimizer.
Figure7.Generationresultsforprompt“a⟨V ⟩infrontofeiffeltower”afterfine-tuningon14Potterimages.Theabovetworows
potter
arefromAdamWoptimizerandthebottomtworowsarefromourscaledAdamWoptimizer. Thefirstandthirdrowscorrespondto
LoRAparameterfusioncoefficient0.7andthesecondandfourthrowscorrespondtoLoRAparameterfusioncoefficient1.0.Ourscaled
AdamWmethodgeneratesimagesofhigherqualitycomparedtoAdamW.SeeAppendixF.2.1forexperimentaldetails.

## F.2.2.Varyingstepsizes

Herewetestwithvaryingstepsizes. NotetheMix-of-ShowrepositoryusesAdamWasdefaultoptimizerwithlearningrate
1e−5fortext-encodertuningand1e−4forU-Nettuning. SGDmethodisnotusedinoriginalrepository. Weemprically
observe that SGD requires larger learning rate compared to AdamW to generate sensible images. For this experiment,
we test with three groups of learning rates, with “Large” corresponds to 3e−1 for SGD-type methods and 5e−4 for
2https://civitai.com/models/6424/chilloutmix
25

<!-- Page 26 -->


### RiemannianPreconditionedLoRA

Figure8.Generationresultsforprompt“⟨V ⟩eatinganicecream”afterfine-tuningon14Potterimages. Theabovetworowsare
potter
fromAdamWoptimizerandthebottomtworowsarefromourscaledAdamWoptimizer.ThefirstandthirdrowscorrespondtoLoRA
parameterfusioncoefficient0.7andthesecondandfourthrowscorrespondtoLoRAparameterfusioncoefficient1.0.OurscaledAdamW
methodgeneratesimagesofhigherqualitycomparedtoAdamW.SeeAppendixF.2.1forexperimentaldetails.
Figure9. Generationresultsforprompt“⟨V ⟩”afterfine-tuningon14Potterimages.TheabovetworowsarefromAdamWoptimizer
potter
andthebottomtworowsarefromourscaledAdamWoptimizer.ThefirstandthirdrowscorrespondtoLoRAparameterfusioncoefficient
0.7andthesecondandfourthrowscorrespondtoLoRAparameterfusioncoefficient1.0.OurscaledAdamWmethodgeneratesimages
ofhigherqualitycomparedtoAdamW.SeeAppendixF.2.1forexperimentaldetails.
AdamW-typemethods;“Medium”correspondsto1e−1forSGD-typemethodsand1e−4forAdamW-typemethods;
“Small”correspondsto5e−2forSGD-typemethodsand1e−5forAdamW-typemethods. Wedon’tdifferentiatelearning
rates for U-Net and text-encoder tuning and the same learning rate is used for both. Note the default learning rate for
AdamWfallsbetweenthe“Medium”learningrateandthe“Small”learningratethusourlearningratechoicesarenot
random. Figure12,13and14showthegenerationresultsforthreedifferentprompts. Itcanbeobservedthatourscaled
optimizersaremorerobusttolearningratechanges.
26

<!-- Page 27 -->


### RiemannianPreconditionedLoRA

Figure10.Generationresultsforprompt“⟨V ⟩wearingaredhat”afterfine-tuningon15Hermioneimages.Theabovetworows
hermione
arefromAdamWoptimizerandthebottomtworowsarefromourscaledAdamWoptimizer. Thefirstandthirdrowscorrespondto
LoRAparameterfusioncoefficient0.7andthesecondandfourthrowscorrespondtoLoRAparameterfusioncoefficient1.0.Ourscaled
AdamWmethodgeneratesimagesofhigherqualitycomparedtoAdamW.SeeAppendixF.2.1forexperimentaldetails.
Figure11.Generationresultsforprompt“⟨V ⟩”afterfine-tuningon15Hermioneimages.TheabovetworowsarefromAdamW
hermione
optimizerandthebottomtworowsarefromourscaledAdamWoptimizer. ThefirstandthirdrowscorrespondtoLoRAparameter
fusioncoefficient0.7andthesecondandfourthrowscorrespondtoLoRAparameterfusioncoefficient1.0.OurscaledAdamWmethod
generatesimagesofhigherqualitycomparedtoAdamW.SeeAppendixF.2.1forexperimentaldetails.
27

<!-- Page 28 -->


### RiemannianPreconditionedLoRA

Figure12.Generationresultsforprompt“apencilsketchof⟨V ⟩”withdifferentoptimizersanddifferentlearningrates.SeeAppendix
potter
F.2.2forexperimentaldetails.DefaultoptimizerisAdamWwithdefaultlearningrate1e−4forU-Nettuningand1e−5fortext-encoder
tuning.Ourscaledoptimizersgeneratebetterqualityimagesandaremorerobusttolearningratechanges.
Figure13.Generationresultsforprompt“⟨V ⟩sitonthechair”withdifferentoptimizersanddifferentlearningrates.SeeAppendix
potter
F.2.2forexperimentaldetails.DefaultoptimizerisAdamWwithdefaultlearningrate1e−4forU-Nettuningand1e−5fortext-encoder
tuning.Ourscaledoptimizersgeneratebetterqualityimagesandaremorerobusttolearningratechanges.
28

<!-- Page 29 -->


### RiemannianPreconditionedLoRA

Figure14.Generationresultsforprompt“aphotoof⟨V ⟩”withdifferentoptimizersanddifferentlearningrates.SeeAppendixF.2.2
potter
forexperimentaldetails.DefaultoptimizerisAdamWwithdefaultlearningrate1e−4forU-Nettuningand1e−5fortext-encoder
tuning.Ourscaledoptimizersgeneratebetterqualityimagesandaremorerobusttolearningratechanges.
29

## Tables

**Table (Page 5):**

| # group trainable parameters into LoRA pairs in train.py. |
|---|
| for LoRAA, LoRAB in pairwise(trainableparameter): |
| paramgroups.append({"params": [LoRAA,LoRAB], "lr": learningrate}) |
| # apply preconditioner in optimizer.py |
| for group in param_groups: |
| A, B = group["params"] |
| dA, dB = group["params"].grad |
| # update parameter A |
| dAscaled =inverse(B.T@B+delta*torch.eye(r)).mm(dA) # precondition gradient of A |
| A_m = beta1*A_m+(1-beta1)*dA_scaled; A_m_hat = A_m/(1-beta1**t) # update first momentum of A |
| A_v = beta2*A_v+(1-beta2)*dA_scaled**2; A_v_hat = A_v/(1-beta2**self.t) # update second momentum of A |
| A.add_(A_m_hat/(sqrt(A_v_hat)+eps), -group[’lr’]) # update A |
| # update parameter B similarly |
| # ... |


**Table (Page 20):**

| # group trainable parameters into LoRA pairs in train.py |
|---|
| for LoRAA, LoRAB in pairwise(trainableparameter): |
| paramgroups.append({"params": [LoRAA,LoRAB], "lr": learningrate}) |
|  |
| # apply preconditioner in optimizer.py |
| for group in param_groups: |
| A, B = group["params"] |
| dA, dB = group["params"].grad |
| # precondition gradients |
| dAscaled =inverse(B.T@B+delta*torch.eye(r)).mm(dA) |
| dBscaled =dB.mm(inverse(A@A.T+delta*torch.eye(r))) |
| # update parameters |
| A.add_(dA_scaled, -group[’lr’]) |
| B.add_(dB_scaled, -group[’lr’]) |


**Table (Page 22):**

| Rank |
|---|
| 1 1 1 1 |
| 4 4 4 4 |
| 8 8 8 8 |


**Table (Page 22):**

| Model | #TrainableParameters |
|---|---|
| GPT-2S GPT-2S GPT-2S GPT-2S | 0.15M 0.15M 0.15M 0.15M |
| GPT-2M GPT-2M GPT-2M GPT-2M | 0.39M 0.39M 0.39M 0.39M |


**Table (Page 23):**

| DART BLEU↑ MET↑ TER↓ |
|---|
| 43.2 .36 .50 46.1 .38 .48 47.1 .38 .47 47.9 .39 .47 |
