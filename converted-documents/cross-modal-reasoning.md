---
title: "Cross Modal Reasoning"
original_file: "./Cross_Modal_Reasoning.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["llm", "rag", "react", "agents", "fine-tuning"]
keywords: ["policy", "learning", "dwa", "expert", "algorithm", "classical", "supervisor", "robot", "navigation", "reinforcement"]
summary: "<!-- Page 1 -->

Bridging the Gap: Regularized Reinforcement Learning for Improved
Classical Motion Planning with Safety Modules

### Elias Goldsztejn1, Ronen I. Brafman2


### Abstract—Classical navigation planners can provide safe

navigation, albeit often suboptimally and with hindered human norm compliance. ML-based, contemporary autonomous
navigation algorithms can imitate more natural and humancompliant navigation, but usually require large and realistic
datasets and do not always provide "
related_documents: []
---

# Cross Modal Reasoning

<!-- Page 1 -->

Bridging the Gap: Regularized Reinforcement Learning for Improved
Classical Motion Planning with Safety Modules

### Elias Goldsztejn1, Ronen I. Brafman2


### Abstract—Classical navigation planners can provide safe

navigation, albeit often suboptimally and with hindered human norm compliance. ML-based, contemporary autonomous
navigation algorithms can imitate more natural and humancompliant navigation, but usually require large and realistic
datasets and do not always provide safety guarantees. We
present an approach that leverages a classical algorithm to
guide reinforcement learning. This greatly improves the results and convergence rate of the underlying RL algorithm
and requires no human-expert demonstrations to jump-start

### Fig.1:Arobotnavigatingautonomouslyusingasystemthat

the process. Additionally, we incorporate a practical fallback
system that can switch back to a classical planner to ensure integrates an RL-based policy, regularized with a classical
safety. The outcome is a sample efficient ML approach for planner, alongside a safety switching mechanism.
mobilenavigationthatbuildsonclassicalalgorithms,improves
them to ensure human compliance, and guarantees safety.
of a learning algorithm and the performance and safety of

## I. Introduction

its resulting navigation policy.

### The proliferation of self-driving cars by an increasing

Our main contribution is a sample-efficient learning stratnumber of companies and the ability of robots to efficiently
egy for improving classical planners and a fallback system
deliver food and supplies are clear manifestations of the
withatrainedsupervisorthatguaranteessafety.Morespecifvast improvements in autonomous navigation. Nonetheless,
ically, we suggest the following approach:
variousunresolvedchallengespersistacrossdiversedomains.
1) Train a planner using DRL with policy guidance de-
Classical planners use analytic optimization techniques
rived from a classical planner: We seed the replay
andreactiverulesforcollisionavoidanceandforfindingsafe
bufferwithexperiencesgeneratedbytheclassicalplanpaths [1]–[3]. These methods can be successful in specific
nerandregularizetheactorinanactor-criticalgorithm
domains, require no or little data, are well understood and
using the classical planner’s policy.
can lead to safe and interpretable behavior. However, they
2) Use a classical rule-based navigation policy as a
often exhibit unnatural and inefficient behaviors and poor
fallback system and train a supervisor that performs
social norm compliance [4].
minimal switching between the neural and classical
Machine learning methodologies build on the latest adplanner to ensure safety.
vancements in imitation learning (e.g., [5], [6]) and deep
While our focus is navigation planning, the above offers a
reinforcement learning (e.g., [7]–[11]) through which they
general recipe for using learning to improve classical algocan capture the intricacy of human actions and provide enrithmswhileretainingtheirrespectivebenefits.Ourapproach
hancedenvironmentalawarenessandhuman-awarebehavior.
provides safety and offers transparency at the supervisor
However, they require large and realistic datasets, and often
level.Itsrelianceongood,existingclassicalalgorithmshelps
lack safety guarantees [12]. Furthermore, because they are
jump-startthelearningalgorithm,leadingtofasterandbetter
oftenbasedonend-to-endlearning,theylackinterpretability
convergence, as our empirical evaluation clearly demonand transparency [13]. For these reasons, they can fail badly
strates.Theregularizationtermfurtherstabilizesthelearning
in unexpected ways on particular inputs [14], [15], making
processandensuresgreatertransparency,forcingittoremain
it difficult to rely on them.
in the vicinity of the well-understood classical algorithm.
This work seeks to alleviate the shortcomings of classical

### And unlike methods that rely on human demonstrations to

and learning-based methods by combining suitable compoachieve some of these effects, no human involvement is
nents of each, building on and modifying various existing
needed–asitisalreadyimplicitlypresentintheformulation
methodologies,reviewedinthenextsection.Inparticular,we
of the classical algorithm and the reward function.
exploitclassicalalgorithmstoimprovethesampleefficiency

### Relevant code and videos for this paper are available at

*ThisworkwassupportedbyISFGrant1651/19,theHelmsleyCharitable https://github.com/eliasgoldsztejn95
TrustthroughtheABCRoboticsCenterofBen-GurionUniversity,andthe
LynnandWilliamFrankelCenterforComputerScience. II. RELATEDWORK
1Elias Goldsztejn and 2Ronen Brafman are with the Depart-
We review previous work on classical planners for aument of Computer Science at Ben-Gurion University of the Negev.
eliasgol@post.bgu.ac.il, brafman@bgu.ac.il tonomous driving in mobile robots, reinforcement learning,
4202
raM
72
]OR.sc[
1v42581.3042:viXra

<!-- Page 2 -->

[24]. While RL is a promising approach it faces numerous
challenges, including the difficulty of defining a suitable
reward function, the need for extensive training datasets,
and concerns related to safety and interpretability [25], [26].
Techniques like inverse and safe RL and RL with demonstrations and human feedback have been developed aimed
at addressing these challenges more effectively. However, in
many domains, solutions for these issues are still elusive.

### C. Reinforcement Learning with Demonstrations

Fig. 2: All Learning is carried out in this realistic simulated
hospital with people moving according to social forces. RL with demonstrations combines elements of IL into the

### RLprocedureofferingcomplementarystrengths.ILenhances

realism, and alleviates the challenge of reward design and
especially using learning from demonstrations, as well as extensivedatasets,whileRLenhancessafetyandrobustness.
techniques for safe planning. IL can be used for the initialization of policies [27], [28]
and expert demonstrations can be included in the experience

### A. Classical Planning for Mobile Robots

replaybuffer[29],[30]tosamplebothexpertdemonstrations
Early planning algorithms for mobile robots used reactive and interactions. However, these methods can fail when
rules and analytic optimization to avoid collision and reach randomness of exploration is needed at the beginning of
targets. Important approaches include Gaussian processes training or when expert rewards are not accessible.
[16], decentralized and scalable multi-agent reciprocal op- We are specifically interested in approaches that directly
timizations [2], reactive techniques [1], spatial and temporal incorporate expert demonstrations during the training stage,
constraint-aware elastic-band methods [3], and more. Clas- explicitly integrating them into the learning process (e.g.
sical planners serve as foundational benchmarks in mobile [31]–[34]). This approach is especially useful when we seek
navigation and are commonly integrated into critical robotic a learned policy similar to that of the expert.
systems,exemplifiedbytheirinclusioninthewidelyadopted Particularly relevant is the work of [33], which uses an
ROS [17] navigation stack. Although in some environments, RL strategy that incorporates the KL divergence between
these methods can provide effective navigation, they usually imitative expert priors and the agent policy in the reward
require fine-tuning from experts and are limited by their function.Thisapproachregularizestheagent’sbehaviorwith
lack of human compliance and social norms, non-smooth the expert policy while maintaining its exploration ability.
behavior, and freezing robot problems, among others. We propose to exploit the same strategy but use classical
planners as the ”expert” prior policy. As explained before,

### B. Imitation and Reinforcement Learning

classical planners for mobile robots are competent enough
Imitation learning (IL) and reinforcement learning (RL) tobeemployedasbaselinesor,inthiscase,asexpertpriors.
are effective and popular techniques for autonomous driving Theaddedbenefitofusingavailableplannersisthatthecolthatcancreateflexible,human-compliantnavigationsystems. lection of data-sets containing human-expert demonstrations
IL uses supervised learning to map states to actions so is no longer required!
as to mimic the behavior of a demonstrator, such as a

### D. Safe Planning

human expert. Some pioneering works include using synthesized datain the formof perturbations [18],and applying Classical planners for mobile robots prioritize safety, and
command-conditionstorepresentexpert’sintentions[19].IL usewell-understoodand,therefore,trustworthysafetymechhas well-known limitations, such as dataset bias and overfit- anisms,butoftenbehavesub-optimally.WhileRLalgorithms
ting, new generalization issues, covariate shifts, and requires oftenprovideenhancedefficiency,completesafetyassurance
large amounts of data [20]. Mitigating these effects is an remains challenging, especially when using Deep RL.
ongoing area of interest. Proposed methods include utilizing Wefocusonrule-basedsystemswithfallbacklayers(e.g.,
space-time cost volumes [21], which enable interpretability [35],[36])thatassessMLplanneroutputsagainstpredefined
and faster learning. Others include combining reinforcement checks. If a plan is deemed unsafe, they can modify it, opt
learning to address the covariate shift problem [22]. for alternative policies, or employ other strategies. These
In RL, agents learn to make decisions by interacting methods ensure predictable and reliable behavior through
with an environment. Feedback is obtained in the form of explicit rules. We employ a similar approach: In critical
rewards from state-action pairs, and the primary objective is scenarios, the policy is seamlessly switched from the RL
toderiveapolicythatmaximizesthecumulativerewardover policy to the classical planner. The switching module is
time. In contrast with IL, RL has a closed-loop exploration- trained to guarantee safety while minimizing transitions
exploitation approach, which addresses the stability and betweentheMLpolicyandtheclassicalplanner.Thisallows
overfitting challenges of IL. for the utilization of an optimal, human-compliant planning
RL is used extensively for autonomous driving and nav- systemwhensafetyisassuredwhileseamlesslytransitioning
igation [7]–[11], lane following and urban driving [23], toapracticalsystemthatprioritizessafetyincriticalsettings.

<!-- Page 3 -->

Fig. 3: Framework of the learning strategy with a classical planner regularization.
Unlike[37],whichtrainstheRLalgorithmandtheswitching module in unison, We first train an RL agent, on top
of which we train a fuzzy-control supervisor. This makes
learning easier, prevents the RL policy from exploiting the
fallbackalgorithmtoomuch,andmakesformoretransparent
behavior and hence, better safety guarantees.

## Iii. Background


### A. Reinforcement Learning


### Reinforcement learning (RL) addresses the challenge of

mastering the control of a dynamic system, characterized
by a Markov decision process (MDP) denoted as M =
(S,A,Tr,r,γ), where S is the state space, A is the action Fig. 4: A supervisor selects whether to switch from the RL
space, Tr : S × A → Π(S) is the transition function, to the Classical planner in critical situations.
r :S×A→R is the reward function, and γ ∈(0,1] serves
as a discount factor. The objective in RL is to develop a
policy,describedasadistributionoveractionsconditionedon The actor aims to determine the optimal policy, while the
statesπ(a |s ),aimingtomaximizethelong-termdiscounted critic evaluates the chosen actions.
t t
cumulative reward: Drawing inspiration from [33], we impose a constraint
ensuring similarity between the actor and the expert. This
(cid:34) T (cid:35) has two advantages: (1) A simplified exploration space
(cid:88)
m
π
axE τ∼pπ(τ) γtr(s t ,a t ) (1) concentrated around the expert policy, leading to decreased
t=0 sampling complexity. (2) The policy mimics the expert,
Here,τ denotesatrajectory,p (τ)isthedistributionofthe reducing the need for a finely tuned reward function. To
π
trajectoryunderpolicyπ,andT representsthetimehorizon. implement this, we introduce a regularization term in the
The Actor-Critic (AC) method is a prominent paradigm actor loss update, defining the regularized actor loss as:
within RL, combining an actor (policy) and a critic (value
(cid:20)
function) for improved decision-making and evaluation:
L (θπ)=E −Q(s ,π(s ;θπ);θQ)
actor st∼D t t
Actor: π(a |s ;θπ) Critic: Q(s ,a ;θQ) (cid:21)
t t t t +λ·MSE(π(s ;θπ),π (s ))
t expert t

### Here,π representsthepolicyfunctionwithparametersθπ,

andQdenotestheaction-valuefunctionwithparametersθQ. Here, L (θπ) is the actor loss. Q(s ,a ;θQ) is the
actor t t

<!-- Page 4 -->

estimated action value by the critic. π (s ) represents
expert t
expert actions. λ is the regularization strength. MSE(·,·) is
the mean squared error.
This formulation encourages the actor to generate actions
that maximize expected rewards while regularizing them
towards expert actions through the MSE term. This is
particularly useful given sparse reward functions since the
expertguidesthelearnedpolicy.Inourwork,the”expert”is
the classical planner. Unlike other approaches, such as [34],
whichrelyonaspecificclassicalplannertoguidethesearch,
our method can seamlessly integrate with any expert.

### B. ”Expert” Prior


### Our method assumes access to a good analytic algorithm

for the task at hand. In robotics, the ROS platform supplies
multiple such algorithms. In particular, for navigation, we
employ the move base framework alongside the classical
local planner DWA [1], fromwhich we can derive actions at
each time step that we use to guide an AC algorithm. The
Fig. 5: Evolutionary Training Diagram for Supervisor. Iniexpert actions are remapped to an unused ROS topic, while
tialization: Generatediverse populationswithvarying fuzzy
the RL actions are mapped to control the robot.
membership values. Fitness Evaluation: Assess fitness

### Unlike approaches relying on behavioral cloning, as seen

through robot episodes, tracking critical situations and suin[22],[33],ourmethodeliminatestheneedforapreceding
pervisor activations. Selection: Select values minimizing
learning step to imitate an expert. This makes our approach
supervisor activations and critical situation occurrences.
more cost-effective and less time-consuming.

### C. Safety Protocol

<30cmthenitmovesbackward.Inaddition,ourSupervisor
Drawing inspiration from various hybrid navigation apmodule switches to a default safe policy if the distance to
proaches such as [26], [35]–[37], we formulate a practical
thenearestobstacleisbelowaparametercalledradiusbelow,
protocol that can switch between a learning-based planner
which is determined using the following simple fuzzy rules:
and a classical planner. Following [35], [36], we design this
protocolwithafocusonensuringsafetyincriticalscenarios, Algorithm 1 Fuzzy Rules for Supervisor Radius
recognizing that, in many instances, reliability and safety
if robot velocity is high then
take precedence over swift navigation.
supervisor radius is big
Similar to the approach of [36], we employ deterministic
else if robot velocity is low then
rules to determine when a switch to a safer navigation mode
supervisor radius is small
is imperative. However, we introduce a strategy to fine-tune
end if
these rules, aiming to optimize safety while minimizing the
frequencyoftransitionstothesafeplanner.Morespecifically,
we utilize fuzzy rules and refine the membership functions b) Neural Navigation Policy: The neural network rethrough a genetic algorithm with the dual objectives of ceives as input an egocentric 2D bird-eye view grayscale
minimizing both transitions and critical situations. image of the local costmap (6x6 Meters). This image is
created with a lidar sensor mounted on the robot. We also

## Iv. Architecture

incorporatethecurrentvelocityoftherobotandthelocation
The high-level architecture of the navigation algorithm of the next waypoint (which is 2 meters away) as indicated
is described in Fig. 4: A supervisor module dynamically by the global planner (a modified version of A*). While its
switches between a neural-net based policy and a classical output is the linear and angular velocity command to the
planner, effectively maintaining a balanced overall policy robot (continuous action space).
that maintains safety, robustness and efficiency in real-world We use a deep convolutional NN followed by fully conscenarios. We now describe its components in more detail. nected layers for the actor and critic networks (See Fig. 6).
Section V describes the methods used to train them. We process the image and concatenate it with velocity and
a) Supervisor: Generally, machine learning techniques waypoint vectors and, in the case of the critic, the action.
perform well in navigation, but may fail badly in certain c) Safe Policy: The policy used when switching is the
scenarios. To address this, we adopt a transparent and pure pursuit algorithm [38] with a very low, fixed linear
interpretable strategy that incorporates a rule-based safety speed(0.5m/s)towardsthenextwaypoint,30cmaway.This
mechanismdirectlyduringdeployment.First,likemanylocal straightforward algorithm is safe because of the following:
planners, if the distance of the robot to the nearest obstacle (1) The A∗ variation used in this work creates a collision-

<!-- Page 5 -->

below. We note that similar modifications using an expert
policy can be applied to many other RL algorithms.

### Buffer Initialization. TD3 uses a policy-gradient method

to update the policy. The gradient is computed by sampling
a mini-batch of experiences from the replay buffer. E2TD3
initializes this buffer by recording experiences obtained by
executing the expert (DWA) policy with some added normally distributed noise. This data pushes the algorithm in
the general direction of the expert policy, while the use of
an initially random policy and the noise added to the expert
data provide some exploration bias.
Regularization. During learning, we augment new experiences (s,a,r,s′) with the expert recommended action a ,

### Fig.6:ActorCriticneuralnetworks.TheCostmapisencoded e

obtainingthequintuple(s,a,a ,r,s′).IntheActor’slearning
using CNN’s. The velocity (vel), waypoint, and action are e
stage, we add to the standard gradient update a regularizer
concatenated. Two fully connected neural networks output
in the form of the MSE between the current policy and the
the next action (actor) and the Q function (critic).
expert policy: λ·MSE(π (s),π (s)) (while we observed
ϕ expert
comparable results with alternative values, we opted for
free path given static obstacles. (2) The robot’s low velocity
λ=1). This has two advantages: (1) Simplified exploration
affords ample time for individuals (dynamic obstacles) to
adapt to its presence, and for A∗ to adapt to these obstacles. space, reducing sampling complexity. (2) The actor mimics
theexpertpolicy,reducingtheneedforafinelytunedreward
V. METHODS function.

### We train the neural policy and the genetic algorithm

in simulation. We use a simulation platform of a realistic Algorithm2TheExpert-EnhancedTD3(E2TD3)Algorithm
hospital [39] integrated with humans moving according to Initialize critic networks Q , Q , and actor network π
θ1 θ2 ϕ
SocialForces,asdescribedin[40].AcomputerwithAMD® with random parameters θ ,θ ,ϕ.
1 2
Ryzen 9 5900x12 CPU and GeForce RTX 4070 was used Initialize target networks: θ′ ←θ , θ′ ←θ , ϕ′ ←ϕ.
1 1 2 2
for simulation and training. We used Pytorch [41] for the InitializereplaybufferB by simulating the expert policy
implementation of the neural networks. with Gaussian noise: a=a +ϵ, ϵ∼N(0,σ).
e
The robots used in simulation and real life are differential for t=1 to T do
drive robots equipped with 2D Lidar sensors with a 3600 Select action with exploration noise: a ∼ π (s)+ϵ,
ϕ
field of view. With this sensor, a 6x6-meter egocentric ϵ ∼ N(0,σ), and observe expert action a , reward r and
e
local costmap is generated. We use move base to generate new state s′.
the global plan (which uses a variant of A*) and, from Store transition tuple (s,a,a ,r,s′) in B.
e
there extract intermediate waypoints, as well as the DWA, Sample mini-batch of N transitions (s,a,a ,r,s′)
e
recommended actions. from B.
Episodesinvolvedtherobotnavigatingbetweendesignated a˜←π (s′)+ϵ, ϵ∼clip(N(0,σ˜),−c,c).
ϕ′
hospital rooms, with simulations sped up about five-fold, y ←r+γmin Q (s′,a˜).
i=1,2 θ′
completing each episode in 8 to 14 seconds. The training Updatecritics:θ ←arg i min 1 (cid:80)N (y−Q (s,a))2.
approach, inspired by [26], separated Simulation, Robot,
i θiN i=1 θi
if t mod d then
Task environments, and the Training algorithm.
Update ϕ by the deterministic policy gradient:
A. Neural Policy Training N
1 (cid:88) (cid:12)
We use RL to develop a policy, training it for 60,000 ∇ ϕ J(ϕ)= N ∇ a Q θ1 (s,a)(cid:12) a=πϕ(s) ∇ ϕ π ϕ (s)
episodes (around 6 hours). The training process, illustrated i=1
in Fig. 3, refines the Twin Delayed DDPG (TD3) algo- +λ·MSE(π ϕ (s),π expert (s))
rithm[42],anonlinedeepRLalgorithm,throughregulariza-

### Update target networks:

tionfromanexpert,specificallytheDWAplanner.TD3uses
2 critics to mitigate overestimation bias and uses delayed θ i ′ ←τθ i +(1−τ)θ i ′
updatestostabilizetrainingbyavertingrapidpolicychanges ϕ′ ←τϕ+(1−τ)ϕ′
and reducing divergence risk. It is known to provide imend if
proved sample efficiency compared to other AC algorithms.
end for
Our modified algorithm, Expert-Enhanced TD3 (E2TD3),
usestheclassicallocalplannerDWAtomodifytwoelements
of TD3: its replay buffer initialization and its policy update Reward Function. The RL algorithm attempts to find a
step.Thepseudo-codeisshowninAlgorithm2.Thechanges policy maximizing the expected sum of discounted rewards
are highlighted by underlining them, and are explained (Eq. 1) minus the regularizing term. The reward function

<!-- Page 6 -->


### Fig.8:MeanandSTDofnumberofswitchinginstancesand

criticalsituationsacrossgenerations.WeseethattheGenetic
Fig. 7:Total reward perepisode in simulations.We compare
Algorithm finds parameters that lower these values.
a plain RL policy with a regularized RL policy using the
DWA classical planner, for two reward functions. As can be
seen, RL + DWA outperforms the plain RL policy.
A critical scenario is defined as the robot being closer to
obstacles than a fixed threshold (0.3 meters).
The supervisor module was trained for 16 generais supposed to quantify desirable properties of the selected
tions, each generation with 16 individuals. Individuals were
path. Our reward function penalizes time and collisions,
episodes of the robot moving through hospital rooms with
and rewards progress towards the waypoint. We tested the
the learned RL + DWA policy, augmented with randomized
learning with two variations. In the first one, the reward
actions. The robot would switch to a low-velocity pure
function is more dense and greedy towards the waypoint:
pursuit algorithm as a function of its velocity and proximity
(1) r(s,a)=r +r +r
timestep collision progresswaypoint
toobstacles,determinedbythecurrentvaluesoffuzzyrules.
where r = −0.5 is a penalty for each time
timestep
The fitness function was evaluated based on the number of
step, r = −vel − 1 if dist < 0.5 is a penalty
collision
switchinginstancesandcriticalsituations(extremecloseness
for the robot being close and fast towards obstacles,
toobstacles)inanepisode.AscanbeseeninFig.8,NSGA-
and r = |dist(waypoint,postion ) −
progresswaypoint t

### IIlearnedtoreducethenumberofswitchinginstanceswhile

dist(waypoint,postion )|isthedistancetraveledtowards
t+1
also reducing the number of critical situations.
the current waypoint at each time step.
The second reward function is more sparse: the robot is

## Vi. Experiments

rewarded only when it reaches the waypoint (with a margin
of error): (2) r(s,a) = r + r + r Inourstudy,weaimtoshowtheefficacyofouralgorithm,
timestep collision waypoint
where r = 10 is a reward given when the robot Regularized RL with a Supervisor, by demonstrating that it
waypoint
reaches each specific waypoint. The total reward during can: (1) be easily implemented with an accessible expert
training can be seen in Fig. 7. In both cases our approach policy (2) improve the expert policy while maintaining
shows better performance than plain RL. proximity to it (3) learn faster, and possibly reach better
cumulative rewards than plain RL (4) effectively integrate a
B. Learning Supervisor Parameters supervisormoduletodiminishunexpectedcriticalsituations,
The Supervisor is a ruled-based mechanism that switches thereby rendering it suitable for practical applications.
to a safe navigation policy as the robot nears obstacles,

### A. Simulated Experiments

adjustingitsradiusdynamicallybasedonvelocity,increasing
it with higher speeds. We define its parameters using fuzzy We first test and compare DWA, RL, RL + DWA (regrules that assign degrees of membership to variables for ularized RL), and RL + DWA + Supervisor (regularized
more flexible and nuanced decision-making compared to RL with a supervisor) in a simulated realistic hospital
deterministic rules. with dynamic people moving according to social forces,
We optimize performance by fine-tuning membership see Table I. Each algorithm was run for 1e4 timesteps
function parameters of rule variables using a genetic al- (around40episodes).Themetricsforcomparisonwere:Total
gorithm. Variables include (1) Robot velocity (low/high) Reward, Total r , Timesteps, MSE between DWA
collision
and(2)Supervisorradius(small/big).Membershipfunctions and algorithm actions (MSE(dwa,π)), and the number of
for these variables are Gaussian, centered around 0m/s, criticalsituations(Critical).AbiggerTotalRewardandTotal
1.5m/s, and 0m, 1.3m, with variable standard deviations, r are better. Smaller Timesteps, MSE(dwa,π), and
collision
learned using the NonDominated Sorting Genetic Algorithm critical situations are preferred.
(NSGA-II),Fig.5.Weoptimzetwoobjectives:(1)Minimum RL learns a decent navigation policy capable of reaching
switching. (2) Minimal critical scenarios. distinct rooms in the hospital. However, it can get stuck in
TheGeneticAlgorithmrunsepisodesoftherobotmoving localminimaincomplexsituations(narrowpassagesorsmall
inthehospitalaccordingtothelearnedRLpolicywhileusing rooms). The expert (DWA) is better than it in most metrics.
theSupervisorwithaspecificsetofparametersforthefuzzy RL+DWAalreadyshowsanimprovement(TotalReward,
rules. For each episode, the fitness function contains the r ) or similar performance (Timesteps) both over RL
collision
number of alternations and the number of critical scenarios. and DWA. Furthermore, RL + DWA stays closer to DWA

<!-- Page 7 -->

TABLEI:Performancestatisticson1e4steps(∼40episodes)pereachalgorithminsimulation.Averageand95%confidence
interval for: Total Reward, Total r , Timesteps, MSE between DWA and algorithm actions (MSE(dwa,π)), and the
collision
number of critical situations (Critical) are presented. The algorithms tested are DWA, plain RL (RL), RL with DWA
regularization (RL + DWA), and RL with regularization and supervisor module (RL + DWA + Supervisor).
PerformanceStatisticsSimulation.((2)rewardfunction)

### DWA RL RL+DWA RL+DWA+Supervisor

TotalReward M =15.8±40.7 M =−3.2±45.8 M =53.7±37.2 M =64.8±30.9

### Totalr

collision

## M =−175.7±23.3 M =−94.0±18.3 M =−83.5±14.0 M =−89.5±18.1

Timesteps M =225.5±20.9 M =296.3±40.0 M =226.1±27.0 M =221.9±25.2
MSE(dwa,π) M =0.0% M =55.3%±12.4% M =23.2%±3.0% M =20.8%±1.0%
Critical M =4.8±3.3% M =20.4%±10.9% M =11.4%±6.2% M =3.5%±0.7%
Fig. 9: Rover Zero 3 robot navigating autonomously in different environments.
TABLE II: Performance statistics in 18 real test cases
movingaroundtherobot.Therobotnavigatedautonomously
PerformanceStatisticsReal-life using the move base plugin to generate a global plan with
DWA RL+DWA+Superv. waypoints and DWA or our algorithm to control its actions.
Time M =33.3±7.4 M =36.0±10.2 Ateachmoment,apersoncouldpressthejoystick’sX button

### NegativeScore M =13.6%±3.7% M =4.7%±2.2%

to indicate dissatisfaction and could also control the robot’s

### Interventions M =1.3±0.4 M =0.2±0.3%

movement in critical situations (Intervention).

### Wecarried18trials,9foreachalgorithm,with3different

(MSE = 23.2%) than RL (MSE = 55.3%). However, RL people recording Time, Negative Score, and Interventions.
+ DWA has a high percentage of critical situations (11.4%), The results are shown in Table II. Negative Score is the
which makes it unreliable. percentage of time of dissatisfaction with the robot’s perfor-
RL + DWA + Supervisor has the best or similar perfor- mancereflectingsuboptimaldrivingsituationslikeproximity
manceinallmetrics.Mostimportantly,itlowersthenumber to obstacles, slow movement in open areas, or significant
of critical situations (3.5%) to a lower threshold than RL + deviation from the goal.
DWA (11.4%) and even of DWA (4.5%). While DWA exhibited quicker completion times, our al-
This shows the advantage of guiding the search space of gorithm obtained a lower negative score and fewer intermachine learning algorithms when a proficient yet subop- ventions. It demonstrated faster performance in open areas,
timal expert is available. Our algorithm can be straightfor- efficientlynavigatedinclusteredspaces,maintainedagreater
wardly implemented in other AC implementations whether distancefrompeople,passedthroughdoorsmoreeffectively,
in online or offline RL, with different experts. The inclu- and avoided collisions thanks to the Supervisor module.
sion of the Supervisor module enhances its practicality and However, it tends to oscillate more due to policy switching.
reliability. This is important in real-life applications.

## Vii. Conclusion


### B. Physical Experiments


### Thisworkintroducesaframeworkthatusesawell-known,

WeperformedphysicalexperimentsusingaRoverrobotics trustworthy algorithm to help regularize the actor within an
RoverZerorobotwthaSLAMTECRPLidarS1andanIntel AC-baseddeepRLalgorithmfortheautonomousnavigation
RealSense T265 Tracking Camera. The robot’s computer of mobile robots. It then learns fuzzy rules for optimizing
(Intel NUCi7) executed the algorithms, and external control a safety module that switches between the learned policy
of the robot was established through the Master-Slave ROS and a safe but suboptimal one in critical situations. This
protocol from a separate computer. A Dualshock 3 joystick pragmaticapproachisabletoimproveaclassicalalgorithms
was connected remotely to the robot. through reinforcement learning while preserving practicality
We tested our algorithm, RL + DWA + Supervisor, using and safety. Unlike most imitation learning algorithms, it
the policy learned in simulation with no additional fine- requires no expert human input.
tuning, against DWA in various university areas (corridors, Our algorithm was able to enhance a prior algorithm
corners, entrances, hall) with static obstacles and people (DWA, here) with low training time, adopting some of

<!-- Page 8 -->

the key features of DWA while introducing new elements [22] Y. Lu, J. Fu, G. Tucker, X. Pan, E. Bronstein, B. Roelofs, B. Sapp,
to address specific scenarios demonstrating superior perfor- B. White, A. Faust, S. Whiteson, et al., “Imitation is not enough:
Robustifying imitation with reinforcement learning for challenging
mance on key measures. Additionally, the inclusion of the
drivingscenarios,”arXivpreprintarXiv:2212.11419,2022.
Supervisor module helped ensure safety at all times, making [23] A.Kendall,J.Hawke,D.Janz,P.Mazur,D.Reda,J.-M.Allen,V.-D.
it a practical and reliable algorithm. Lam,A.Bewley,andA.Shah,“Learningtodriveinaday,”inICRA,
2019,pp.8248–8254.
REFERENCES [24] J.Chen,S.E.Li,andM.Tomizuka,“Interpretableend-to-endurban
autonomous driving with latent deep reinforcement learning,” IEEE
[1] D.Fox,W.Burgard,andS.Thrun,“Thedynamicwindowapproachto TransactionsonIntelligentTransportationSystems,vol.23,no.6,pp.
collisionavoidance,”IEEERobotics&AutomationMagazine,vol.4,
5068–5078,2021.
no.1,pp.23–33,1997. [25] B.R.Kiran,I.Sobh,V.Talpaert,P.Mannion,A.A.AlSallab,S.Yo-
[2] J.vandenBerg,S.Guy,M.Lin,andD.Manocha,Reciprocaln-Body gamani, and P. Pe´rez, “Deep reinforcement learning for autonomous
CollisionAvoidance. Springer,Berlin,Heidelberg,042011,vol.70, driving: A survey,” IEEE Transactions on Intelligent Transportation
pp.3–19. Systems,vol.23,no.6,pp.4909–4926,2021.
[3] C.Ro¨smann,F.Hoffmann,andT.Bertram,“Timed-elastic-bandsfor [26] X. Xiao, B. Liu, G. Warnell, and P. Stone, “Motion planning and
time-optimal point-to-point nonlinear model predictive control,” in controlformobilerobotnavigationusingmachinelearning:asurvey,”
ECC. IEEE,2015,pp.3352–3357. AutonomousRobots,vol.46,no.5,pp.569–597,2022.
[4] C. I. Mavrogiannis, F. Baldini, A. Wang, D. Zhao, P. Trautman, [27] M.Pfeiffer,S.Shukla,M.Turchetta,C.Cadena,A.Krause,R.Sieg-
A.Steinfeld,andJ.Oh,“Corechallengesofsocialrobotnavigation: wart, and J. Nieto, “Reinforced imitation: Sample efficient deep
Asurvey,”CoRR,vol.abs/2103.05668,2021.
reinforcement learning for mapless navigation by leveraging prior
[5] Y. Pan, C.-A. Cheng, K. Saigol, K. Lee, X. Yan, E. Theodorou, and demonstrations,”IEEERoboticsandAutomationLetters,vol.3,no.4,
B.Boots,“Agileautonomousdrivingusingend-to-enddeepimitation pp.4423–4430,2018.
learning,”arXivpreprintarXiv:1709.07174,2017.
[28] X.Liang,T.Wang,L.Yang,andE.Xing,“Cirl:Controllableimitative
[6] F. Codevilla, M. Mu¨ller, A. Lo´pez, V. Koltun, and A. Dosovitskiy, reinforcement learning for vision-based self-driving,” in Proceedings
“End-to-enddrivingviaconditionalimitationlearning,”inICRA,2018, of the European conference on computer vision (ECCV), 2018, pp.
pp.4693–4700. 584–599.
[7] L. Tai, G. Paolo, and M. Liu, “Virtual-to-real deep reinforcement [29] M. Vecerik, T. Hester, J. Scholz, F. Wang, O. Pietquin, B. Piot,
learning:Continuouscontrolofmobilerobotsformaplessnavigation,” N. Heess, T. Rotho¨rl, T. Lampe, and M. Riedmiller, “Leveraging
inIEEE/RSJ,2017,pp.31–36.
demonstrationsfordeepreinforcementlearningonroboticsproblems
[8] M. Bojarski, D. D. Testa, D. Dworakowski, B. Firner, B. Flepp, withsparserewards,”arXivpreprintarXiv:1707.08817,2017.
P. Goyal, L. D. Jackel, M. Monfort, U. Muller, J. Zhang, X. Zhang, [30] A.Nair,B.McGrew,M.Andrychowicz,W.Zaremba,andP.Abbeel,
J. Zhao, and K. Zieba, “End to end learning for self-driving cars,” “Overcoming exploration in reinforcement learning with demonstra-
CoRR,vol.abs/1604.07316,2016. tions,”inICRA,2018,pp.6292–6299.
[9] H.-T. L. Chiang, A. Faust, M. Fiser, and A. Francis, “Learning [31] B. Kang, Z. Jie, and J. Feng, “Policy optimization with demonstranavigation behaviors end-to-end with autorl,” IEEE Robotics and tions,” in International conference on machine learning. PMLR,
AutomationLetters,vol.4,no.2,pp.2007–2014,2019.
2018,pp.2469–2478.
[10] Y.F.Chen,M.Everett,M.Liu,andJ.P.How,“Sociallyawaremotion [32] Y. Lu, J. Fu, G. Tucker, X. Pan, E. Bronstein, B. Roelofs, B. Sapp,
planning with deep reinforcement learning,” in IEEE/RSJ, 2017, pp. B. White, A. Faust, S. Whiteson, et al., “Imitation is not enough:
1343–1350. Robustifying imitation with reinforcement learning for challenging
[11] C. Chen, Y. Liu, S. Kreiss, and A. Alahi, “Crowd-robot interaction: drivingscenarios,”arXivpreprintarXiv:2212.11419,2022.
Crowd-aware robot navigation with attention-based deep reinforce- [33] Z. Huang, J. Wu, and C. Lv, “Efficient deep reinforcement learning
mentlearning,”inICRA,2019,pp.6015–6022. with imitative expert priors for autonomous driving,” IEEE Transac-
[12] E. Yurtsever, J. Lambert, A. Carballo, and K. Takeda, “A survey of tionsonNeuralNetworksandLearningSystems,2022.
autonomousdriving:Commonpracticesandemergingtechnologies,” [34] U. Patel, N. K. S. Kumar, A. J. Sathyamoorthy, and D. Manocha,
IEEEAccess,vol.8,pp.58443–58469,2020.
“Dwa-rl:Dynamicallyfeasibledeepreinforcementlearningpolicyfor
[13] T. Ra¨uker, A. Ho, S. Casper, and D. Hadfield-Menell, “Toward robotnavigationamongmobileobstacles,”inICRA,2021,pp.6057–
transparent ai: A survey on interpreting the inner structures of deep 6063.
neuralnetworks,”2023. [35] M. Vitelli, Y. Chang, Y. Ye, A. Ferreira, M. Wołczyk, B. Osin´ski,
[14] C. Szegedy, W. Zaremba, I. Sutskever, J. Bruna, D. Erhan, I. J. M.Niendorf,H.Grimmett,Q.Huang,A.Jain,etal.,“Safetynet:Safe
Goodfellow,andR.Fergus,“Intriguingpropertiesofneuralnetworks,” planning for real-world self-driving vehicles using machine-learned
inICLR2014,2014. policies,”inICRA,2022,pp.897–904.
[15] J.Uesato,A.Kumar,C.Szepesva´ri,T.Erez,A.Ruderman,K.Ander- [36] T.Fan,P.Long,W.Liu,andJ.Pan,“Distributedmulti-robotcollision
son,K.Dvijotham,N.Heess,andP.Kohli,“Rigorousagentevaluation: avoidanceviadeepreinforcementlearningfornavigationincomplex
Anadversarialapproachtouncovercatastrophicfailures,”CoRR,vol. scenarios,” The International Journal of Robotics Research, vol. 39,
abs/1812.01647,2018. no.7,pp.856–892,2020.
[16] P.Trautman,J.Ma,R.M.Murray,andA.Krause,“Robotnavigation [37] S.Dey,A.Sadek,G.Monaci,B.Chidlovskii,andC.Wolf,“Learning
indensehumancrowds:thecaseforcooperation,”inICRA. IEEE, whomtotrustinnavigation:dynamicallyswitchingbetweenclassical
2013,pp.2153–2160. andneuralplanning,”2023.
[17] M. Quigley, K. Conley, B. Gerkey, J. Faust, T. Foote, J. Leibs, [38] R.C.Coulteretal.,Implementationofthepurepursuitpathtracking
R.Wheeler,andA.Ng,“Ros:anopen-sourcerobotoperatingsystem,” algorithm. CarnegieMellonUniversity,TheRoboticsInstitute,1992.
inICRAWorkshoponOpenSourceSoftware,vol.3,012009.
[39] AWSRoboMaker,“AWSRoboMakerHospitalWorldROSpackage,”
[18] M.Bansal,A.Krizhevsky,andA.Ogale,“Chauffeurnet:Learningto GitHub repository, jul 2021. [Online]. Available: https://github.com/
drivebyimitatingthebestandsynthesizingtheworst,”arXivpreprint
aws-robotics/aws-robomaker-hospital-world
arXiv:1812.03079,2018.
[40] D.HelbingandP.Molna´r,“Socialforcemodelforpedestriandynam-
[19] F. Codevilla, M. Mu¨ller, A. Lo´pez, V. Koltun, and A. Dosovitskiy, ics,”PhysicalReviewE,vol.51,pp.4282–4286,May1995.
“End-to-enddrivingviaconditionalimitationlearning,”inICRA,2018,
[41] A. Paszke, S. Gross, F. Massa, A. Lerer, J. Bradbury, G. Chanan,
pp.4693–4700. T.Killeen,Z.Lin,N.Gimelshein,L.Antiga,A.Desmaison,A.Ko¨pf,
[20] F.Codevilla,E.Santana,A.M.Lo´pez,andA.Gaidon,“Exploringthe E.Yang,Z.DeVito,M.Raison,A.Tejani,S.Chilamkurthy,B.Steiner,
limitationsofbehaviorcloningforautonomousdriving,”inProceed- L.Fang,J.Bai,andS.Chintala,PyTorch:AnImperativeStyle,HighingsoftheIEEE/CVFInternationalConferenceonComputerVision, PerformanceDeepLearningLibrary. CurranAssociatesInc.,2019.
2019,pp.9329–9338. [42] S. Fujimoto, H. van Hoof, and D. Meger, “Addressing function ap-
[21] W.Zeng,W.Luo,S.Suo,A.Sadat,B.Yang,S.Casas,andR.Urtasun, proximationerrorinactor-criticmethods,”CoRR,vol.abs/1802.09477,
“End-to-end interpretable neural motion planner,” in Proceedings of 2018.
theIEEE/CVFConferenceonComputerVisionandPatternRecognition,2019,pp.8660–8669.

## Tables

**Table (Page 7):**

| PerformanceStatisticsSimulation.((2)rewardfunction) |  |  |  |  |
|---|---|---|---|---|
|  | DWA | RL | RL+DWA | RL+DWA+Supervisor |
| TotalReward | M =15.8±40.7 | M =−3.2±45.8 | M =53.7±37.2 | M =64.8±30.9 |
| Totalr collision Timesteps MSE(dwa,π) Critical | M =−175.7±23.3 M =225.5±20.9 M =0.0% M =4.8±3.3% | M =−94.0±18.3 M =296.3±40.0 M =55.3%±12.4% M =20.4%±10.9% | M =−83.5±14.0 M =226.1±27.0 M =23.2%±3.0% M =11.4%±6.2% | M =−89.5±18.1 M =221.9±25.2 M =20.8%±1.0% M =3.5%±0.7% |


**Table (Page 7):**

| PerformanceStatisticsReal-life |  |  |
|---|---|---|
|  | DWA | RL+DWA+Superv. |
| Time | M =33.3±7.4 | M =36.0±10.2 |
| NegativeScore | M =13.6%±3.7% | M =4.7%±2.2% |
| Interventions | M =1.3±0.4 | M =0.2±0.3% |
