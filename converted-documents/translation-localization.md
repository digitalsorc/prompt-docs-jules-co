---
title: "Translation Localization"
original_file: "./Translation_Localization.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["rag", "react", "agents", "evaluation", "multimodal"]
keywords: ["cid", "exim", "virtual", "page", "item", "human", "https", "org", "scale", "doi"]
summary: "<!-- Page 1 -->

5202
yaM
03
]OR.sc[
3v54781.9042:viXra
1
A study on the effects of mixed explicit and implicit
communications in human-virtual-agent interactions

### Ana Christina Almada Campos1* and Bruno Vilhena Adorno2

1Graduate Program in Electrical Engineering, Universidade Federal de Minas Gerais, Av. Antônio Carlos 6627, Belo Horizonte, 31270-901, MG, Brazil. 2Manchester Centre for Robotics and AI, The University of Manchester, Oxford Rd,
Manchester, M13 9PL, UK."
related_documents: []
---

# Translation Localization

<!-- Page 1 -->

5202
yaM
03
]OR.sc[
3v54781.9042:viXra
1
A study on the effects of mixed explicit and implicit
communications in human-virtual-agent interactions

### Ana Christina Almada Campos1* and Bruno Vilhena Adorno2

1Graduate Program in Electrical Engineering, Universidade Federal de Minas Gerais, Av.
Antônio Carlos 6627, Belo Horizonte, 31270-901, MG, Brazil. ORCID:
https://orcid.org/0000-0002-7800-5640.
2Manchester Centre for Robotics and AI, The University of Manchester, Oxford Rd,
Manchester, M13 9PL, UK. ORCID: https://orcid.org/0000-0002-5080-8724.
*Corresponding author(s). E-mail(s): campos.aca@outlook.com;
Contributing authors: bruno.adorno@manchester.ac.uk;

### Abstract

Communication between humans and robots (or virtual agents) is essential for interaction and often
inspired by human communication, which uses gestures, facial expressions, gaze direction, and other
explicitandimplicitmeans.Thisworkpresentsaninteractionexperimentwherehumansandvirtual
agentsinteractthroughexplicit(gestures,manualentriesusingmouseandkeyboard,voice,sound,and
informationonscreen)andimplicit(gazedirection,location,facialexpressions,andraiseofeyebrows)
communicationtoevaluatetheeffectofmixedexplicit-implicitcommunicationagainstpurelyexplicit
communication.ResultsobtainedusingBayesianparameterestimationshowthatthenumberoferrors
andtaskexecutiontimedidnotsignificantlychangewhenmixedexplicitandimplicitcommunications
wereused,andneithertheperceivedefficiencyoftheinteraction.Incontrast,acceptance,sociability,
andtransparencyofthevirtualagentincreasedwhenusingmixedcommunicationmodalities(88.3%,
92%, and 92.9% of the effect size posterior distribution of each variable, respectively, were above the
upper limit of the region of practical equivalence). This suggests that task-related measures, such as
time, number of errors, and perceived efficiency of the interaction, have not been influenced by the
communication type in our particular experiment. However, the improvement of subjective measures
related to the virtual agent, such as acceptance, sociability, and transparency, suggests that humans
are more receptive to mixed explicit and implicit communications.
Keywords:Human-robotinteraction,Human-robotcommunication,Explicitandimplicitcommunications,

### Virtualagent

1 Introduction
In addition to performance indicators, those applications also require comprehensive analysis of

### Modern robots are increasingly expected to work

human-related aspects, such as preferences, satalongside humans, such as in assembly and transisfaction, and burden during the human-robot
portation [66, 47], collaboration with humans
interaction (HRI) [59, 27, 26].
through physical interactions [2], housework [4],

### Social robots motivate social interactions, and

and assistance to people with disabilities [17].
people tend to attribute human characteristics to

<!-- Page 2 -->

2
robots that communicate, cooperate, and learn Bayesian approach, which can be used to in-
[10]. Consequently, people rely on human social form future studies related to these types of
interaction models to understand and interact interactions.
with these robots [10]. Socially interactive robots,
whose main characteristic and purpose are to so-
2 Human-robot
ciallyinteract[23],canbereceptionists[24]orplay
educational and companion roles [64, 57, 50]. communication

### Given the importance of shared information

andintentionsduringcollaboration[58,6]andthe According to Mavridis [48], two aspects motivate
need for natural communication in socially inter- thedevelopmentofinteractiverobotsthatusenatactive robots [23], communication is an essential ural human communications. First, we can take
partofHRI.Robotsshouldinterprethumancom- advantage of the human interaction and teachmunications and convey information clearly and ing capabilities so robots can learn and adapt
naturally. Therefore, it is necessary to define the whileinteracting,minimizingtheneedforexperts
communication type that best suits each context, to program and reprogram the robots. Second,
considering human perceptions and communica- severalapplicationsbenefitfromthisnaturalcomtion performance and efficiency, to satisfactorily munication, such as socially interactive robots
achievetheinteractiongoalsinanatural,intuitive assisting humans.
way. Humans use several means to communicate,
To develop robots and virtual agents to in- from verbal languages and gestures to more subteract with humans, we need an extensive study tle communications, such as facial expressions,
of aspects related to their interaction and com- speech intonation, and eye gaze, which can be
munication. In their review, Natarajan et al. [54] cues for people’s internal state and be used to
included communication on the list of the grand estimateintentionsduringinteractions.Thesedifchallengesinhuman-robotcollaboration,mention- ferent communication types can be classified as
ing specifically that which modality to use is still explicit and implicit. Some authors define them
an open question. This work investigates how the based on intention: explicit communications concommunication type affects human-virtual-agent vey information deliberately (e.g., pointing and
interactions.Wecompareusingonlyexplicitcom- head gestures) whereas in implicit communicamunicationwithmixedexplicit-implicitcommuni- tions the information is inherent to the behavior
cationstoobservetheeffectsontask-andhuman- (e.g., facial expressions and eye gaze) [11, 6].
related outcomes. The goal is to provide insights, Others treat deliberate and unambiguous combasedonscientifically-soundempiricaldata,about munication as explicit (e.g., haptic signals with
human-virtual-agent interactions and experimen- predefined meanings), and communication where
tal procedures that will serve as a stepping-stone informationisincorporatedtoabehaviororaction
forfurtherworksonthedevelopmentoftechniques and for which interpretation is context-dependent
for intuitive communication in HRI. as implicit (e.g., change of direction and speed
duringmovement)[39,16].However,somemodalities can be difficult to classify under these def-
1.1 Contributions initions. For instance, people can use and alter
theintensityoffacialexpressionswhentheyknow

### The contributions of this work are:

theyarebeingobserved,thusservingasacommu-
• scientificallysoundempiricaldatashowingthat nicative act [7], which could make them explicit if
combiningexplicitandimplicitcommunications classified based on intention.
in interactions between humans and virtual Inanattempttomakethisclassificationeasier,
agents, as opposed to using only explicit com- in the present work, we define these communicamunications, can improve the acceptance, so- tion types considering what the aforementioned
ciability, and transparency of the virtual agent; definitions have in common: explicit communiand cations are directly interpreted whereas implicit
• estimation of parameters related to objective communications require more subjective inferand subjective measures obtained through a ences and interpretation. Table 1 summarizes the

<!-- Page 3 -->

3

### Experiments proposing interactions between hu-

Table 1 Definitions of explicit and implicit commans and robots or virtual agents aim to answer
munications from the literature and the present
some of these questions.
work.
Bruce et al. [12] investigated whether a more

### Explicit Implicit

expressive robot with a face producing facial ex-
Information Informationinherent pressions and head movement to indicate gaze
[11, 6] conveyed tothebehavior direction would affect people’s willingness to indeliberately
teractwithit.Intheirexperiments,thenumberof

### Information

peoplewillingtointeractwiththerobotincreased
incorporatedto
Deliberateand whenitusedfacialexpressions.Breazealetal.[11]
[39, 16] unambiguous behavior/action,with
context-dependent explored explicit and implicit communications in
interpretation a task where a person teaches the robot buttons’
Directly Subjectiveinferences names and then make it press them. They com-
Presentwork interpreted andinterpretation pared two conditions: when the robot uses only
explicit communication, such as voice to inform
itsinternalstatewhenrequested,andanotherone
definitionsofexplicitandimplicitcommunications in which the robot uses both explicit and implicit
from the literature and the present work. communications, such as voice, gaze, facial ex-
Communication modalities, such as gestures, pressions, and eye blinking to convey vivacity. In
speech,gaze,hapticandphysiologicalsignals,and both conditions, the person communicated only
facial expressions, can be explored separately in explicitlythroughvoiceandgestures.Theirstudy
HRI, enabling the robot to convey information indicates that participants had a better underand also perceive and interpret information con- standing of the robot and created better mental
veyed by humans. However, platforms combining models about it when it used the two communimultiple communication modalities to perceive cation types. Also, in the mixed explicit-implicit
and produce different explicit and implicit com- condition,thetaskexecutiontimewassmallerand
municationsmightbeusedtocreatemorecomplex errors during the task were identified faster and
systems and a richer experience. Some works better mitigated. To understand how people use
use humanoids or virtual agents with abilities and interpret seemingly unintentional cues leaked
to speak, direct their gaze, and make gestures through the robot’s gaze, Mutlu et al. [52] proand facial expressions, and systems to monitor posed a game where a person should find out
and interpret human speech, gestures, gaze di- an object the robot chooses by asking yes or no
rection, head orientation, eye movements, and questions.Intheconditionincludingimplicitcomphysiological signals to investigate physical, cog- munication,therobotglancedtothechosenobject
nitive, emotional, and behavioral aspects in HRI before answering the question. They used two hu-
[44, 70, 43]. manoidrobotsandobservedthatpeopleidentified
the correct object quicker and with fewer questions when the android robot leaked cues through
2.1 Interaction experiments and
its gaze. In a study of a long term interaction,
comparative studies Tanakaet al.[62]obtainedresultssuggestingthat
thecompanyofacommunicativerobotabletotalk
Withallthesecommunicationpossibilities,several
andnodcanimprovecognitivefunctionsandother
questions arise:
aspects of the daily life of elderly women living

## Which communication type is more appropri- alone, when compared to the same robot withate for each context? outthecommunicativefeatures.HuangandMutlu


## Does including implicit communications im- [34] showed that, when the robot uses the human

prove HRI? gaze direction to anticipate explicit commands

## Do different communication types affect hu- and act accordingly, the task is better performed

manperceptionsandbothagents’performance and the robot is perceived as more aware of the
during interaction? interaction.

## How is the robot communication interpreted?


<!-- Page 4 -->

4
Using their model for bidirectional gaze in hu- of people’s gender, age, culture, familiarity with
man and virtual agent interactions, Andrist et al. robots,andotherfactorsarealsoconcernsofHRI
[3] observed improved task performance when the studies [25, 28, 65, 67, 56].
virtual agent both produced gaze and responded Communication is essential to interaction and
tohumangaze.Participantsalsoperceivedthevir- studying it is paramount to develop better robots
tual agent as more expressive and with greater interactingwithhumans.Inthiswork,weconsider
cognitive abilities when it produced gaze, and the literature on explicit and implicit communimorecompetentwhenproducedandrespondedto cation in HRI, such as the works of Breazeal et
it. In Buschmeier and Kopp’s work [13], an at- al. [11] and Huang and Mutlu [34], to define the
tentivespeakeragent,whichestimatedthehuman hypotheses presented in the next section.
mental states during the interaction and adapted
its behavior, received more feedback signals from
3 Experimental design
thehumanandwasperceivedasanattentiveagent
by them. Iwasaki et al. [35] observed that a robot
We investigate the effects of communication type
recognizing and responding to people’s behaviors
on human perceptions and task-related outcomes
encourages them to interact with it. Che et al.
in a human-virtual-agent interaction. The liter-
[16] studied the communication effects when the
ature on HRI described in Section 2.1 suggests
navigation of one agent affects the navigation of
that combining explicit and implicit communianother(i.e.,socialnavigation).Theirexperiment
cations improve the interaction. We define two
showed that when the robot communicated its
communication configurations:
intention explicitly and implicitly and predicted

### EX: Only explicit communications from

human movements, participants navigated more
human and virtual agent.
efficiently and it increased their trust and under-
EXIM: Explicit and implicit communications
standingoftherobot,comparedtowhentherobot
from human and virtual agent.
predicted movements and communicated only explicitly,andwhentherobotexecutedonlycollision
avoidance without prediction. Zhang et al. [71]
3.1 Human-robot communication
showedthatteamperformance,trust,andanthroinfrastructure
pomorphismperceivedbythehumanareimproved
when the robot is able to understand implicit in- We used a human-robot communication infrasformation conveyed by indirect speech acts. The tructure with selected explicit and implicit comauthors also highlight that this capability can munication modalities [14]. The system is inteaffect differently depending on the context, and gratedintheRobotOperatingSystem(ROS)and
thereforeitshouldbeusedcarefully.Sixet al.[60] includes recognition and interpretation of human
evaluated the use of animation features in virtual pointing gestures and gaze direction, and a viragents in brief cognitive behavioral therapy based tual agent with voice, facial expressions, and gaze
mental health apps. In this context, their results direction.
suggestthatavirtualagentwithbodymovements In addition to the systems described in our
and facial expressions can improve user experi- previouswork[14],weincludedothercommunicaence, in contrast to a static one with blank facial tion modalities such as screen applications for the
expression. virtual agent to keep the human informed of the
It is also important to investigate how to use task progress. The human can also insert explicit
each available communication modality. The way information using mouse and keyboard. The virthe robot communicates (e.g., how it speaks and tualagentusessoundsignalstoindicatesuccesses
engagesintouchinteractions,andwhereitdirects and errors, and raises its eyebrows to implicitly
its gaze [61, 22, 32, 1, 9]) must be carefully ad- draw the person’s attention during interaction.
justed and can be influenced by the application The human location during the interaction imcontext and the general profile of people interact- plicitly indicates the current stage of the task
ing with the robot. Aspects such as the effects and if instructions were followed. Table 2 summaof robot’s conveyed mood, transparency, planning rizes the communication modalities available in
forcommunication,ethicalconcerns,andinfluence our infrastructure.

<!-- Page 5 -->

5

### H4: The virtual agent will be perceived as


### Table 2 Availablecommunicationmodalitiesfor

more sociable in the EXIM configurahuman and virtual agent.
tion than in the EX configuration.

### Human Virtual agent

H5: The virtual agent will be perceived as
voice more transparent in the EXIM config-

### Explicit gestures soundsignals

manualentries informationonscreen uration than in the EX configuration.
Lastly, we expect that the virtual agent’s greater
facialexpressions
gazedirection sociability and the better task performance when

### Implicit raiseofeyebrows

location gazedirection combining communication types will make the interaction be perceived as more efficient, resulting
in our final work hypothesis:
Since we planned an structured interaction

### H6: The perceived interaction efficiency

with well defined steps, there was a ROS node
willbegreaterintheEXIMconfiguraresponsible for integrating the individual systems
tion than in the EX configuration.
andmanagingtheinteraction.Thismanagernode
autonomously read important information and
3.3 Human and virtual agent
sentcommandsthroughROStopicstoeachofthe
othermodulestocarryontheinteraction.Wealso interaction
used cameras and markers to locate objects and
To evaluate our hypotheses, we chose to conduct
otherimportantelementsintheenvironment,such
the study in a well controlled environment, so we
asthescreenstodisplayvirtualagent.Thehuman
could isolate the factor of interest [33]. Also, to
locationwasalsoinferredusingmarkers.Giventhe
reduce the sample size needed, we decided for a
specific locations the human was instructed to be
within-subjects design, in which each participant
ateachphase,weplacedamarkeronthefloorthat
completes the task twice, one for each condition
would be occluded whenever the human reached
[33].Weproposeanactivitysimilartoagamewith
that specific location. After some camera frames
twophasesthatincludeactionspresentinrealcolwithoutdetectionofaspecificmarkeronthefloor,
laborativescenarios,suchasfollowinginstructions
we would consider that the human reached that
and pointing to objects.
location.
In the first phase, after introducing itself and
givinginstructions,thevirtualagentshowsafour-
3.2 Hypotheses
color sequence. The person should then point to
We hypothesize that the combination of explicit colored boxes in the environment in the same orand implicit communications makes the agents’ derasthesequence.Soundsignalssuggestcorrect
actions more transparent and predictable, which and wrong indications, and the screen application
isimportanttosuccessfullyachieveacollaborative showsthetaskprogress.Thecolorsequenceworks
goal. Hence, we postulate the following: as a password for the next phase, when the per-
H1: The task execution time will be son is further instructed to count the occurrence
smaller in the EXIM configuration ofsomeobjectsinimagescontainingseveralother
than in the EX configuration. items. There are four images in the workspace.
H2: The number of task errors will be Given an object shown in each corner of the comsmaller in the EXIM configuration puter screen, the person should count it on the
than in the EX configuration. respective image in the workspace and type the
If using explicit and implicit communications number of occurrences on the screen application.
makes the virtual agent more similar to human The images’ positions were chosen to encourage
agents, weexpectthat humans understanditbet- people to move their heads to look at them. In
ter and perceive it more as a social agent, making both phases, if a time limit is reached, the virthe interaction more natural and pleasant. There- tual agent finishes the task, adding the password
fore, we introduce three additional hypotheses: or filling the remaining count fields.
H3: The acceptance of the virtual agent Eachparticipantcompletedbothphasestwice,
will be higher in the EXIM configura- once for each communication configuration (EX
tion than in the EX configuration. and EXIM). Each configuration is represented by

<!-- Page 6 -->

6
the instructed location. During Phase 2 of EXIM,
if the system detects that the human is looking
at one of the images of shuffled items, the virtual
agent also looks at it and verbally suggests the
correctcountingvalue(e.g.,“[translatedfromPor-
(a) Luna (b) Sofia tuguese] I guess it is five there.”). Moreover, when
Fig. 1 Twovirtualagentscreatedtointeractwith the person opens one of the fields on the screen
people in the experiments. application to add the counting value, the virtual
agent direct its gaze to the open field.

### In the EXIM configuration, the virtual agent

a different virtual agent selected randomly by the always looks at the person’s face when speaking,
system at the beginning of the experiment, as exceptwhenitisgivingaclueonPhase2,sincein
wellas thecommunicationconfigurationorderfor thismomentitsgazeindicateswhichimage/object
each participant. The two virtual agents, Luna it refers to. Fig. 2 illustrates the interaction.
and Sofia (see Fig. 1), differ by their names, eye
colors, and voice tones. As described in [14], we
recorded audio files with selected sentences to be
3.4 Objective and subjective metrics
the virtual agents’ voices. Since participants interact with both virtual agents, there are slight The outcomes related to hypotheses H1 and
differences in the sentences for each one to help H2 are time and number of errors. The sysdifferentiate them. tem registers the interaction duration, including
On the EX configuration, the virtual agent both phases, except for initialization, verbal inusesonlyvoicewithsimulatedmouthmovements, structions, and audio file execution times. More
sound signals, and information on screen to com- specifically, the time for the phase instructions is
municate. The agent always has a neutral ex- excluded because they are only given in the first
pression, blinks periodically, and looks straight configuration. We also exclude the times for the
ahead, while the human communicates through execution of the audio files for the virtual agents’
pointing gestures in Phase 1 and manual en- voices to prevent the differences in the sentences’
tries by keyboard and mouse in Phase 2. On the length from affecting the comparison between the
EXIM configuration, along with the explicit com- two communication configurations.
munications of the EX configuration, the virtual Errorsarecountedwhenevertheindicatedcolagent uses different facial expressions according ors in Phase 1 or counting values in Phase 2 are
to the context, raises its eyebrows to call the hu- wrong. We discard system errors, such as wrong
man’s attention, and directs its gaze through the identificationofapointinggesture.Whenthetask
environment. The system also uses implicit infor- finishes due to timeout, we count one extra ermation from the location and the person’s gaze in ror for each color not added in Phase 1 and each
specific moments of the interaction. counting value not inserted in Phase 2.
During EXIM’s Phase 1, the virtual agent ThehypothesesH3toH6arerelatedtosubjeclooks at the colored box that the person should tive outcomes, namely acceptance, transparency,
indicate. If the person makes a mistake or the and sociability of the virtual agents and the perpassword is repeated on screen after some wrong ceived interaction efficiency. We measure each
indications, the virtual agent looks at the person, variable with a Likert scale [46] containing a set
raises its eyebrows, and then looks at the correct of items (sentences) that people answer with one
box again. After Phase 1 is finished, the virtual of the following options: (1) totally disagree, (2)
agent instructs the person to go to a specific disagree, (3) do not know, (4) agree, and (5) tolocation to start Phase 2. tallyagree.Therefore,wehavefiveresponselevels
In the EX configuration, Phase 2 starts only (1 to 5), and we present them to the participants
after the person’s explicit command through the always in the same order and without numbered
screen application. In the EXIM configuration, labels.
the system anticipates the explicit command and Table 3 shows the 19 items composing the
starts Phase 2 whenever it detects the person on Likert scales, translated from Portuguese. They

<!-- Page 7 -->

7

### Screen application

"Add the password:"
Environment with colored objects
Password (color sequence)
shown at the screen

### Pointing gesture

to indicate objects Virtual agent implicit
communications in
EXIM configuration
Task execution

### Objects

Screen application Fields to add the
counting values
Virtual agent implicit
communications in

### EXIM configuration

Counting images fixed in the environment Human gaze
to estimate
attention focus in
EXIM configuration

### Task execution

Fig. 2 Illustrations of the proposed interaction.
4 Methodology for
were defined according to our experiment, but inspired and adapted from works such as the ones experimental analysis
by Heerink et al. [30] and Iwasaki et al. [35]. In
most cases, the lowest response level (“totally dis- WeuseBayesianparameterestimationinourdata
agree”) indicates a more negative perception. For analysis as it provides richer information when
instance, to disagree with the first item of the compared with frequentist analyses such as null
transparency scale means that the virtual agent hypothesis significance tests, maximum likelihood
was perceived as not very transparent. On the estimation,andconfidenceinterval[41,42,69,37].
other hand, a low level response for the first item Bayesian approaches are not so common in HRI
in the acceptance scale indicates good acceptance studiesastheanalysisusingp-values[8],butthey
ofthevirtualagentbecauseitusesareversescale. allowdiscussionsbeyondtheacceptingorrejecting
Itemswithareverse scale,forwhichlowlevelsin- hypotheses dichotomy. In areas such as statistics
dicate positive perceptions, are marked with an and psychology, Bayesian methods have been dis-
(R) in Table 3. The 19 items from the table are cussed as alternatives to deal with the limitations
presentedrandomlytoeachparticipant,unlabeled
and without the reverse scale indication.

<!-- Page 8 -->

8

### Prior probability distribution


### Posterior probability distribution

Table 3 Likert scales for the measurement of human perception variables. Items marked with (R) 95% HDI
are treated with a reverse scale. The term VA is
replaced by the name of the virtual agent. Fig. 3 Example of prior and posterior probability distributions for parameter values in the

### Acceptance of the virtual agent

Bayesian estimation. The 95% HDI includes 95%

## IfoundVAintimidating.(R)

oftheposteriordistributionandthemostcredible

## IfoundVAfriendly.


## IfeltcomfortablewhileinteractingwithVA. parameter values.


## IlikedtointeractwithVA.


## IfoundunpleasanttointeractwithVA.(R)


## IwouldliketointeractmorewithVA.

Sociability of the virtual agent belief) is given by

## IfeltlikeVAunderstoodwhatIwasdoing.


## WheninteractingwithVA,IfeltlikeIwaswithareal


## P( )P( )

person. P( )= D |V V .

## SometimesIfeltlikeVAwasreallylookingatme. V |D P( )


## SometimesVAseemedtohaverealfeelings. D


## VA’sbehaviorissimilartoaperson’s.


### The Bayesian parameter estimation allows es-

Transparency of the virtual agent timating a parameter value or the magnitude of

## IunderstoodVA. an effect of interest. When there is few prior in-


## IwasabletoknowwhatVAwas“thinking.”

formation about the parameter values, we usually

## IknewwhenVAwaspayingattentiononme.


## Duringtheinteraction,VA’sintentionswerecleartome. use prior probability distributions that are vague

and uninformative so that they have minimal in-
Perceived efficiency of the interaction fluence on the estimation [42, 37]. Fig. 3 shows

## IcouldcountwithVAtohelpmeduringthetask. a uniform prior distribution, which assigns the


## VAhelpedmetoexecutethetask. same credibility for all parameter values inside


## VAgotinmyway.(R)


## VAmadenodifferencetomyperformance.(R) an interval. The Bayes’ rule provides the posterior distribution with updated credibilities for

each parameter value, which are summarized usand sometimes inadequate interpretations of p- ing measures of central tendency, such as mean,
values [40, 42, 69, 37, 38]. In the HRI context, mode, and median, and intervals such as the HDI
Baxteret al.[8]suggestwefocusonmethodsthat (Highest Density Interval).
can incrementally increase our knowledge about TheHDIincludesapercentageofthedistribuphenomenaofinterest;thatis,aBayesianperspec- tion, and the parameter values inside the interval
tive. The methods we chose to analyze our results are more credible than the ones outside of it.
are detailed below.
Therefore,the95%HDIcontains95%ofthedistribution,andparametervaluesinsideofitaremore
credible than parameter values outside of it [41]
4.1 Overview
because there is a 95% probability that the true
Bayesian methods rely on Bayes’ rule to re- parameter value is inside this interval. Also, the
allocate credibility across possibilities, using col- 95% HDI width indicates the estimation uncerlected information. More specifically, an initial tainty:thesmallertheinterval,themorepreciseis
belief on the value of a set of variables is up- the estimation and the more certain we are about
dated after collecting new data. Let P( ) be the parameter value.

## V

the prior joint probability of n parameter values The posterior distribution alone already pro-
= v ,v ,...,v without the data (initial be- vides information about the parameter value.
1 2 n

## V { }

lief), P( ) the likelihood to obtain the data Nonetheless, we can also evaluate the credibility

## D | V

given , and P( ) the data likelihood accord- of specific values such as a null value indicating

## D V D

ingtotheconsideredmodel.Then,theBayes’rule the absence of an effect. The Region Of Pracstates that the posterior credibility of (updated tical Equivalence (ROPE) is defined around the

## V


<!-- Page 9 -->

9
Accept for Unde ned decision

### Reject

practical purposes about

## Rope Rope Rope


## 95% Hdi 95% Hdi 95% Hdi

Fig. 4 Examples of possible relations between
the 95% HDI of the posterior distribution and
a ROPE around a value of interest, α , for the
0
parameter.
Fig. 5 Examples of t distributions with mean µ,
scaleτ,anddifferentnormalityparametersν.The
parametervalueofinteresttoindicateasetofval- greater ν is, the closer the t distribution is to a
ues that are practically equivalent to the one of normal distribution. The scale τ is related to the
interest [40]. When deciding about accepting or spread of the data and covers 50% of the t disrejectingaspecificvalue,Kruschke[41]proposesa tribution with ν = 1 and 68% of the distribution
decision rule, illustrated in Fig. 4, using a ROPE with ν = .
∞
around the value of interest and the 95% HDI of
the posterior distribution. If the entire 95% HDI
∆t = ∆e = 0, and positive differences (∆t > 0
is inside the ROPE, the value of interest is acand ∆e>0) favor our hypotheses.
cepted for practical purposes. Conversely, if the
We treat time and number of errors as metric
entire95%HDIisoutsidetheROPE,thevalueof
variables in interval or ratio scales and represent
interestisconsideredincredibleand,therefore,rethem using t distributions because of the heavier
jected. If none of those occur, the available data
(withhigherprobabilities)tailsthataccommodate
set is considered insufficient to make a decision
outliers better than the normal distribution [41].
about the specific parameter value. To define the
The distribution is described using mean µ, scale

### ROPEaroundthevalueofinterest,thecontextof

τ, and a normality parameter ν (0, ), all ilthe application must be taken into consideration ∈ ∞
lustrated in Fig. 5. The scale τ is related to the
for it to reflect practical equivalence. With an adspreadofthedataandν determinestheheaviness
equate ROPE, a value of interest is accepted only
ofthedistributiontails.Thegreaterνis,thecloser
when there is a sufficiently precise parameter esthet distributionistoanormaldistribution.1The
timation, which implies a sufficiently narrow 95%
goal of the Bayesian inference is to estimate the
HDI that could fit into the ROPE.
parameters µ , τ , and ν for the time differ-
∆t ∆t ∆t
ence and µ , τ , and ν for the difference in
∆e ∆e ∆e
4.2 Objective measures
the number of errors.
In our experiment, participants interact with two Since we do not have previous information
virtual agents, one for each communication con- about the parameters, all priors are broad and
figuration (EX and EXIM), resulting in measure- vague to minimally influence the estimation (e.g.,
ment pairs. One way commonly used to cancel
avoidbiasing).Therefore,bothfor∆tand∆e,the
individual variations is to take the difference be- prior distributions for the mean and scale paramtween the two observations and run the analysis eters are normal and uniform distributions [41],
with a single group [51]. For time and number of respectively. When ν > 30, the t distribution
errors, we take the differences closely approximates a normal. Hence, large differences between the normal and t distributions
∆t≜t t and ∆e≜e e , (1) occurwhenν issmall(seeFig.5),whichisconsid-

## Ex Exim Ex Exim

− − ered credible in the posterior distribution only if
smaller values for ν are more credible in the prior
respectively, between the observations in each
configuration, and ∆t and ∆e are the final measurementsassociatedwitheachparticipant.There
1Formoreaboutthescaleandnormalityparametersofthe
is no difference between the configurations when t distribution,pleaserefertoSection16.2of[41].

<!-- Page 10 -->

10
d st e a v n ia d t a io rd n They treat items together but without aggregatmean ing points into a single measure. The idea is that
mean NORMAL lower bound upper bound the measured variable is in a continuous metric
scale but cannot be accessed directly; that is, it is
alatentvariable.Therefore,thesetofitemsinthe

## Exponential


## Uniform

Likert scale is a way of accessing the latent variablethroughadiscreteandordinalresponsescale.
Fig. 6 Diagram of the Bayesian estimation for As in the metric model, using a t latent distributhe metric variables ∆t and ∆e. A t distribution tion instead of a normal makes the model more
describesthedataandweestimatetheparameters robust to outliers.
µ, τ, and ν of each variable, using the indicated For a single item with K N response levels,
priors, where x¯ and s are the sample mean and thresholds θ ,...,θ divid ∈ e the latent distri-

## 1 K 1

standard deviation, respectively. bution into K interva − ls, as shown in Fig. 7 (for

### K = 5). On the ordinal model, the probability

assigned to each response level is the cumulative
distribution,orifthesamplecontainsalotofoutprobabilityofeachinterval,calculatedasthearea
liers, rare by definition [41]. As a consequence, we
under the latent distribution between the respecuseanexponentialwithmeanof30asapriordistive thresholds, or between the outer thresholds
tributionforthenormalityparameterstoconsider
(θ and θ ) and open boundaries at and

## 1 K 1

small values in the estimation while still allowing (i.e., θ −≜ and θ ≜ ). For − a ∞ latent

## 0 K

high values. The parameters and their priors are ∞ −∞ ∞
t distribution with mean µ, scale τ, and normalillustrated in Fig. 6.
ity parameter ν, the probability of the ordinal
response y =k, with k 1,...,K , is
4.3 Subjective measures
∈{ }
We obtain the subjective measures through ques-
P(y =k µ,τ,ν,θ ,...,θ )=

## 1 K 1

tionnaires with Likert scales (see Section 3.4). | −

### Ψ (θ ) Ψ (θ ), (2)

Following Likert’s original work [46], one fre- µ,τ,ν k − µ,τ,ν k − 1
quently used way to deal with this type of data is
(cid:82)u
where Ψ (u)= f (x)dx is the cumulausing the average or the sum of the points of the µ,τ,ν µ,τ,ν
tive t function with−∞
items in a scale, and then treating this value as
an observation from each participant. There is a
discussion in the literature on whether this data f (x)=
µ,τ,ν
s s a e h n t o d u g w l e d n h e b ic r e h at t e t r e d e s a t f t s r e o d a m p a p s t l h y in e t t o e a r v v t e h a r e l a m g o e r .2 o o r L rd i s d i u n d m a e l ll m o a f e n a p d s o u i K n re t r s s - Γ Γ (cid:0) (cid:0) ν+ ν 2 1 (cid:1) (cid:1)(cid:18) τ2 1 νπ (cid:19)1 2 (cid:20) 1+ (x τ − 2ν µ)2(cid:21) − (ν+ 2 1)
2
uschke [45] show that treating ordinal data from
a single item as metric leads to systematic errors and Γ represents the gamma function Γ(w) =
(cid:82)
of false positives, failures in detecting effects, and 0 ∞zw − 1e − zdz with Re(w) > 0 [36, p. 501-507].
eventheinversionofaneffect.Theyalsoshowthat ThemodelrepresentedbyEq.2appliestoallordiusing the average points from a set of items does nal levels since Ψ µ,τ,ν ( )=0 and Ψ µ,τ,ν ( )=
−∞ ∞
not solve the problems. Since there is no consen- 1.
susintheliterature,wetreatdatafromsubjective The model has K +2 parameters: the latent
measures as ordinal. variables µ, τ, and ν and the K 1 thresholds
−
Kruschke suggests a cumulative normal model that map the latent variable into the ordinal re-
(see Chapter 23 of [41]) for the analysis of or- sponses. There are infinite possible combinations
dinal data from a single item, and Liddell and for these parameters that result in the same ordi-
Kruschke[45]extendthemodeltomultipleitems. nal probabilities, since we can “drag,” “compress,”
or “expand” the distribution, by changing the
whole set of parameters (see Fig. 7), while keep-
2Somereferencesthatdiscussthesubject,especiallyinthe ingtheprobabilitiesassociatedwitheachlevel.To
context of frequentist analyses (for example, comparing the t
solve this problem, Kruschke [41] suggests fixing
andWilcoxonsigned-ranktests)are[53,49,15,29].

<!-- Page 11 -->

11
Ordinal levels EXIMcommunicationconfigurations.Whenmealatent t distribution suring the same latent variable (e.g., acceptance)
with , , and
using the same questionnaire such as the Likert
scale shown in Table 3, we assume that the latent
1 2 3 4 5 variable for all groups have the same probabil-
Fig. 7 The probability of the ordinal response itydensityfunctionbutwithdifferentparameters.
y = k is given by the cumulative probability be- Since the thresholds are related to the way we
tween the thresholds θ k 1 and θ k on the latent t measure the variable (i.e., the sentence in the
−
distributionofmeanµ,scaleτ,andnormalitypa-

### Likert scale, such as “I found the virtual agent

rameter ν, with k 1,...,K , θ 0 = and friendly”), we assume they are the same across all
∈ { } −∞
θ K = . groups. Therefore, what differs between groups is
∞
how much people agree or disagree with the sentence and the variance of this feeling. For each
group, we consider that there are common latent

### Sample 1 Sample 2 Sample 3

µ,τ,andν forallitemsofthescale,butadifferent
set of thresholds for each item, since they access
the same latent variable in different ways [45].

### After fixing the outer thresholds of a single

1 2 3 4 5 1 2 3 4 5 1 2 3 4 5 itemoneachscaleinθ =1.5andθ =K 0.5,
Fig. 8 Examples of sample histograms of ordinal 1 K − 1 −
as suggested by Liddell and Kruschke, we need to
responses with five levels and possible adequate
estimate the remaining parameters. For multiple
latent distributions. Extreme thresholds are fixed
itemsandmultiplegroups,theprobabilityofeach
at θ =1.5 and θ =4.5.
1 4 ordinalresponsey
g
[i] oftheithitemandgthgroup
is given by [45]
the extreme thresholds, θ 1 and θ K 1 , at mean- P(y[i] =k µ ,τ ,ν ,θ[i],...,θ[i] )
ingful values with respect to the re − sponse scale, g | g (cid:16) g g (cid:17) 1 K −(cid:16) 1 (cid:17)
fi sp x e e c d ifi v c a a lu ll e y s θ a 1 n = cho 1 r .5 th a e nd es θ ti K m − a 1 ti = on K .B − y 0 d . o 5 i , n s g o it t , h t e h s e e =Ψ µg,τg,νg θ k [i] − Ψ µg,τg,νg θ k [i − ] 1 , (3)
estimatedparametersareinterpretedaccordingto whereθ[i] isthekththresholdoftheithitem(e.g.,
the meaning of the response options. Suppose we k
“I found the virtual agent friendly”), and µ , τ ,
g g
askpeopletoansweranitemstating“Ilikerobots”
and ν are the mean, the scale, and the normality
g
using a scale with five response levels, from “toparameterofthelatentvariable(e.g.,acceptance)
tallydisagree” to“totallyagree” andwithamiddle
in group g (e.g., EXIM).
answer saying “I do not know.” Fig. 8 shows ex-

### The model states that the ordinal response

a a m nd pl p e o s s o si f b h le is a to d g e r q a u m at s e fr la o t m en t t h d re is e tr p ib o u ss t i i b o l n e s s t a o m e p a l c e h s y g [i] comes from a categorical distribution with
probabilities given by Eq. 3. As mentioned beone of them, with the extreme thresholds fixed at
fore, we fix the outer thresholds only of the first
1.5and4.5.ForSample1,theanswersconcentrate
item of each scale in Table 3.3 Therefore, the
in the middle of the ordinal scale so the latent µ
goal of the Bayesian inference is to estimate the
wouldbeapproximately3,suggestingthat,onavparameters µ , µ , τ , τ , ν , and
erage, people are not certain if they like robots EX EXIM EX EXIM EX
ν of each variable (acceptance, sociability,
or not. For Sample 2, negative answers are more EXIM
transparency, and perceived efficiency) and the
frequent and the latent µ would be smaller, indi- (cid:16) (cid:110) (cid:111)(cid:17)
cating that, on average, people do not like robots. unfixedthresholds(i.e., (cid:83)n i= i 1 θ 1 [i],...,θ K [i] − 1 \
Finally, the results from Sample 3 suggest that
peopledolikerobots,withµhavingalargervalue,
sincethehigherresponselevelsaremorefrequent. 3We analyze the subjective measures considering two separate groups, instead of using the difference as we do for

### Now, suppose we want to compare a variable

timeanderrors.Thisistomaintainthemeaningofthefixed
in two different conditions (or groups), such as thresholdsandnottogeneratemoreemptyresponselevelsin
the sample data, since they cause negative probabilities, as
the acceptance of the virtual agent in EX and
discussedattheendofthissectionandinAppendixA.

<!-- Page 12 -->

12
dsteavniadtaiordn makes it more difficult to validate our work hymean potheses,sincetheeffectsizewecalculatehasτ in
mean NORMAL lower bound upper bound thedenominator,asdescribedinthenextsection.

### Therefore, our strategy to mitigate empty levels

EXPONENTIAL due to small samples is conservative.Moredetails

## Uniform

about our tests can be found in Appendix A.
5 Results
dsteavniadtaiordn dsteavniadtaiordn dsteavniadtaiordn dsteavniadtaiordn
mean mean mean mean Thirty volunteers participated in the experiments
NORMAL NORMAL NORMAL NORMAL but four were excluded due to significant devia-
Fig. 9 Bayesian estimation for the ordinal vari- tion from the experimental protocol. Volunteer 4
ables.At distributiondescribesthelatentvariable did not finish interacting with the second virtual
andweestimateitsparametersµ g ,τ g ,andν g and agent due to a technical problem, volunteer 9 did
the free thresholds θ[i] , k 1,2,3,4 , translat- not complete the questionnaire after the first ink ∈ { }
ing the latent variable into the ordinal responses teraction, volunteer 10 asked for the researchers’
of each item i in the Likert scales. The diagram help during the task, and volunteer 22 completed
shows the prior distributions for each parameter, the task atypically, hindering the objective meawhere K = 5 is the number of ordinal response sures. Therefore, the final sample size is of 26
levels in our scales. participants, summarized in Fig. 10.
5.1 Bayesian analysis results
θ[1],θ[1] with n being the number of items) Effect size is a measure quantifying the strength
a { ss 1 ocia K te−d 1} with the i items of each scale. After the ofthepresenceofaneffect.Itiscalculatedconsidestimation, we analyze the difference between the ering the null value, which represents an absence
groups EX and EXIM. of effect [18]. We calculate the effect size d obj for
Liddell and Kruschke [45] suggest using the the objective measures as
priorsshowninFig.9fortheparameters,withµ
g
(µ µ )
and τ g in the neighborhood of the data, whereas d = − 0 , (4)
obj
the free thresholds follow normal distributions τ
with considerable standard deviation.
considering the null value µ = 0 (absence of an

### There is nothing in the model to specify that 0

effect) and using the estimated mean µ and scale
the thresholds are in ascending order, i.e., θ <
1
τ of the difference between the configurations ∆t
θ < < θ . Therefore, if θ > θ , the
2 K 1 k 1 k
··· − − and ∆e, as explained in Section 4.2. Since the erprobability of the ordinal level k is negative (see
ror and time differences are defined as in Eq. 1,
Eq. 3), which violates the first probability axiom.
positive effect sizes favor hypotheses H1 and H2,

### Kruschke works around this limitation through

whereas negative effect sizes go against them. For
implementation,byconsideringonlynon-negative
the analysis of subjective measures, which estiprobabilities. However, his solution only works if
mates the parameters of each condition (i.e., EX
the data sample has at least one answer in every
andEXIM)separately,thecalculatedeffectsizeis
levelk,whichcanbedifficulttoobtainwithsmall
samples. So, together with Kruschke’s proposed
(µ µ )
implementation, we decided to add one extra ob- d sub = (cid:112) EXIM − EX , (5)
servation to each empty level we encounter in our 0.5(τ E 2 X +τ E 2 XIM )
samples, and use the updated data set in the
Bayesian inference. In our tests with simulated using the estimated mean and scale parameter
data, when we added the extra observations, we of each group (EX e EXIM) [40, 41]. Therefore,
observed that the estimations of the scale param- positive effect sizes also favor hypotheses H3 to
eterτ gavemorecredibilitytovaluesgreaterthan H6, whereas negative effect sizes go against those
the real ones. This increase in the values of τ hypotheses.

<!-- Page 13 -->

13
Age Gender Stage of education Familiarity with virtual agents
(minimum:21,maximum:61)
Female 34.6% 34.6% Yes 57.7%

### Male 11.5% No

15.4% Complete secondary education Do not know
61.5% Incomplete Bachelor's degree
F U A r p b o o m to v e 2 2 5 5 5 0 t y o e y e 5 a a 0 rs r y s o e o l a d ld rs old 23.1% 65.4% I I C C n n o o c c m m o o m m p p l l p p e e l l t t e e e e t t e e M B M P a a c h s a h D t s e e t r e l ' o s r r ' s ' d s e d d g e e r g e g r e r e e e e 30.8% 11.5% 7 3 .7 .8 % % 7.7% 34.6%
Fig. 10 Summary of the profile of the interaction experiment participants.
We define a ROPE from 0.1 to 0.1 around Time
−
the null value (d obj = d sub = 0) in the effect size Fig. 11a shows the distribution of the effect size
posterior.Thisintervalcoversvaluesuptohalfofa for the time difference ∆t, in seconds, between
small effect size, according to Cohen’s convention thetwocommunicationconfigurations.Thedistri-
[18], which is used because we do not have a clear bution is centered close to the null value, but it
understanding yet of what a significant effect size has a large 95% HDI, including almost medium
means in our context. positive and negative effect sizes (i.e., d = 0.5
obj
[18]). Positive effect sizes would favor hypothesis
H1,whereasnegativeeffectsizeswouldgoagainst
5.1.1 Implementation details
it. Therefore, this estimation does not allow us to
We generated the posterior distributions using reach a conclusion using the decision rule illus-
Markov Chain Monte Carlo (MCMC) methods tratedinFig.4aboutthetimedifferencebetween
and JAGS (Just Another Gibbs Sampler) sys- the two communication configurations.
tem.4 All scripts were written using R language
and based on examples provided in the works by

### Kruschke [41] and Liddell & Kruschke [45]. Error

The MCMC sample contains a large number Owing to two possible outliers (∆e = 11 and
−
of parameter combinations, allowing the genera- ∆e=26),5 we have made the analysis for the diftion of posterior distributions for each parameter ference in the number of errors with and without
and other distributions such as the difference be- them. The effect size distributions are shown in
tweenparametersineachgroupandtheeffectsize, Figs. 11b and 11c. With the outliers, more credcalculated using Eqs. 4 and 5. ibility is given for small values of the normality
parameter ν, increasing the weight in the tails
of the latent t distribution to try to accommo-
5.1.2 Objective measures
date the outliers. Without them, the estimations
For the sake of conciseness, we only show the ofthemeanandthescaleparameterbecamemore
distributions of the effect size for each measure. precise (narrower 95% HDI) and the effect size
For the posterior distributions of mean µ, scale posterior is slightly “compressed” to the left, re-
τ, and normality ν, please refer to the Supple- ducing the percentage of the distribution above
mentary Material accompanying the paper. The the ROPE upper limit, and giving less credibil-
Supplementary Material also shows some credible itytovaluesfavorabletoourhypothesis.However,
t distributions superimposed on the data of each again we do not have enough precision to draw
variable to check model adequacy. As there is no strong conclusions about the existence or not of
critical deviation (e.g., strong asymmetry or mul- differenceinthenumberoferrorsbetweenthetwo
timodal distribution) between the data and the communication configurations.
estimatedt distributions,weconcludethattheestimations fit the data well enough and the chosen
model is adequate.
5These two cases seem to have occurred because the participantsdidnotunderstandthatthefirstcolorshownonthe
screen(blackforoneparticipant,whitefortheother)wasalreadypartofthepasswordandkeptindicatingthenextcolor
4Formoredetails,checkChapters7and8of[41]. repeatedly,causingmultipleerrorstoberegistered.

<!-- Page 14 -->

14
d obj,∆t
(cid:1)
mo=
0.5 0.0 0.5
(cid:1)
md=
0.0209 (cid:1)
0.0209
m=
(cid:1)
0.02
3 %
34.6% 27.7%

## Hd

(cid:1)
04 375
d obj,∆e
(a)Posteriordistributionoftheeffectsize
inthetimedifference∆t(seconds).
(cid:1)
mo=
1.0 0.0 0.5 1.0 1.5
(cid:1)
md=
0.0378 (cid:1)
0.0264
m=
(cid:1)
0.0215
3 . %
38.1 0.2%

## % D

(cid:1)
0.5 485
d obj,∆e
(b)Posteriordistributionoftheeffectsize
inthedifferenceinnumberoferrors∆e.
(cid:0)
(cid:1)
1.0
(cid:0)
mo=
0.5 0.0 0.5
(cid:0)
md=
0.105 (cid:0)
0.0895
m=
(cid:0)
0.0884
%
48% 18.9%

## 95 I

(cid:0)
0507 345
(c)Posteriordistributionoftheeffectsize
in the difference in number of errors ∆e′
withoutoutliers.
Fig. 11 Results of the Bayesian inference for the objective measures (time and number of errors). The
figures show the distributions of the effect size d (Eq. 4) calculated with the null value µ =0. Mean
obj 0
(m), median (md), mode (mo), and the limits of the 95% HDI are annotated. Dashed vertical lines
indicate the ROPE, together with the percentages of the distribution below, between and above it.
5.1.3 Subjective measures indicating all the levels for which we added extra
answers.
We obtained posterior distributions for the latent

### Fig. 12a shows the effect size posterior of the

parametersofeachgroupseparatelyandthengenacceptance of the virtual agents, with its median
erated posteriors for the difference between the
(md = 0.264) indicating small to medium effects
meansandthescaleparametersofeachgroupand
(i.e., 0.2 to 0.5 [18]), but without enough pretheeffectsize.Positiveeffectsizescalculatedusing
cision to draw a conclusion using the 95% HDI
Eq. 5 favor our hypotheses, and their distribuand ROPE.6 However, 88.3% of the distribution
tions are shown in Fig. 12. Other distributions,
is above the ROPE upper limit, suggesting high
includingtheestimationsofthethresholdsθ ,and
k credibility that there is an effect favorable to our
comparisons between the data and the estimahypotheses; namely, that the EXIM virtual agent
tions are available in the Supplementary Material
is more accepted than the EX one.
accompanying the paper. As the estimations fit
the data appropriately, we conclude the model is
adequate. Sociability
For the sociability data set, we added one extra
answer only to level 1 of item 1 in group EXIM,

### Acceptance

as no participant chose that response. Again, the
When completing the questionnaire with the Lik-
95% HDI of the effect size posterior, shown in
ert scales for the acceptance of the virtual agent,

### Fig.12b,isnotnarrowenoughtoallowusastrong

no participants chose ordinal level 2 for item 4 in
conclusion, but 92% of the distribution is above
the EX group. Furthermore, no participants from
theROPEupperlimit,suggestingthattheEXIM
the EXIM group chose ordinal level 1 for items
virtual agent was perceived as more sociable than
1–3 and 5, ordinal level 2 for items 1, 2, and 4,
the one from the EX configuration.
and ordinal level 3 for item 5. Therefore, those
levels were empty in the data set and we added
oneextraanswerintheEXgroup(ordinallevel2)
and eight in EXIM group (ordinal levels 1, 2, and
3) to avoid negative probabilities, as explained in 6The width of the 95% HDI of the subjective variables is
smaller than the 95% HDI of the objective variables. Conse-
Section 4.3. Thus, the estimated scales τ acc might quently,theestimationofsubjectivevariablesismoreprecise.
be slightly greater than the real ones, especially Thisisbecauseweassumeintheordinalmodelthatthelatent
parameters are the same for all Q 4,5,6 items from the
for the EXIM group, and the effect size slightly Likertscales(i.e.,eachitemmeasur ∈ es { thesam } ephenomenon).
lower(seeAppendixAformoreinformation).The Consequently, we use all 26Q observations related to all 26
participantstoestimateµ,τ,andν,resultinginmoreprecise
Supplementary Material shows data histograms estimations.

<!-- Page 15 -->

15
d
sub,acc
(cid:1)
md=0.264
m=0.264 mo=0.258
11.3%
0.4% 8.3

## 95% Di

0.2 0.0 0.2 0.4 0.6 0.8
(cid:1)
000 31
d
sub,soc
(a) Posterior distribution of the effect size dsub,acc in the acceptanceofthevirtualagents.
(cid:1)
md=0.304
m=0.304 o=0.318
7.8%
0.3%

## Hd

0.2 0.0 0.2 0.4 0.6 0.8
(cid:1)
000 0.5 5
(b) Posteriordistributionoftheeffectsizedsub,soc inthesociabilityofthevirtualagents.
d
sub,tra
(cid:1)
md=0337
m=0339 =0.328
6.8%
0.3% 9%
5%
001 6
0.2 0.0 0.2 0.4 0.6 0.8 1.0
d
sub,eff
(c)Posteriordistributionoftheeffectsizedsub,tra inthetransparencyofthevirtualagents.
(cid:1)
md=0.153
m=0.155 mo=0.132
31.
6% %
0.5 0.0 0.5
(cid:1)
0 493
(d) Posteriordistributionoftheeffectsizedsub,eff intheperceivedefficiencyoftheinteractions.
Fig. 12 Results of the Bayesian estimation of acceptance, sociability, transparency and perceived efficiency in the two communication configurations. The figures show the distribution of the effect sizes.
Mean(m),median(md),mode(mo),andthelimitsofthe95%HDIareannotated.Dashedverticallines
indicate the ROPE, together with the percentages of the distribution below, between and above it.

### Transparency 6 Discussions

We added one extra answer on level 1 of each
6.1 Dealing with technical errors
group to overcome the lack of participant reduring the experiments
sponses in this level in item 1 for EX and item
3 for EXIM. The effect size estimation, shown in

### The system for human kinematic chain recogni-

Fig. 12c, is once again not precise to fulfill Krtion[14]sometimesfailedtodetecttheparticipant
uschke’s decision criterion, but it indicates that
andtheexperimenterintervenedtogiveadditional
the EXIM virtual agent might have been seen as
instructions or to restart the system, sometimes
moretransparentthantheEXvirtualagent,with
remotely. Also, some participants did not under-
92.9% of the distribution above the ROPE upper
stand that they would interact with two virtual
limit.
agentsandlefttheroomafterthefirstinteraction
and questionnaire. In these cases, the experimenter asked them to go back and continue. As
Perceived efficiency long as these interventions did not happen during
Finally, for the perceived efficiency dataset, we the task execution and interrupted the interacadded one extra answer in level 2 of item 3 of EX tion flow, we took note of the occurrence and
group and one in level 1 of item 3 of group EXIM let the experiment continue and the participant
because those were empty due to the lack of re- was not excluded from the analysis. We excluded
sponse. Fig. 12d shows the effect size posterior, the system initialization times and the time to
whose median (md = 0.153) indicates a less than solvetheaforementionedtechnicalproblemsinour
small effect (i.e., lower than 0.2 [18]), with 62.9% analyses.
of the distribution above the ROPE upper limit.

<!-- Page 16 -->

16
All participations were recorded with the par- Acceptance, sociability, and transparency are
ticipants’ knowledge and formal consent. After variables more related to the virtual agents,
the experiments, we watched the videos and ad- whereas time, errors, and perceived efficiency of
justed the data. For instance, for Phase 1, we the interaction depend more directly on the task.
discarded errors caused by wrong detection of Seven comments on questionnaires report difficulpointing gestures and some delay in the sound ties in understanding the task, which was also
signals indicating a correct or wrong color (some- mentioned by other participants directly to the
times, a delay happened and the participant kept experimenter, suggesting that instructions might
pointing while waiting for the sound signal, so not have been clear enough. Considering all 29
the system counted two gestures instead of one). completeparticipations,withtwointeractionsper
Errors indirectly attributed to the system limi- people,thetimelimitwasreachedandthevirtual
tations, such as when a participant points to a agent had to finish the task five times in Phase 1
second object after indicating the correct one, and eight times in Phase 2. Two of the times the
but the system fails to recognize it, were not timelimitwasreachedinPhase1andthreeofthe
discarded because these interpretations were sub- ones in Phase 2 were not considered in the analjective; therefore, we decided to follow a more ysis, since some participants were excluded from
conservative approach. the final sample for having significantly deviated
from the experimental protocol.8 The videos also
6.2 General discussion suggest that people found Phase 2 more difficult,
taking a long time to find the counting images

### TheresultsshowninSection5wereobtainedfrom

fixed in the environment and to understand what
asampleof26participants.Fromthefourparticito do. Six participants added what seems to be
pantsexcludedfromthisanalysis,threecompleted
genericvalues,suchas1forallobjects,inatleast
all the steps of the interaction and the quesoneoftheconfigurations,suggestingthattheydid
tionnaires, so they are included in the following
not understand the task or did not find the imdiscussion,whichaimstodiscusstheexperimental
ages. Two people mentioned that the space used
protocol and how it could be improved.
for the experiment was visually cluttered, which

### From the 29 participants that interacted with

might have created difficulties for participants to
both virtual agents, 21 of them said they prefind the counting images. The objective measures
ferred to interact with the EXIM virtual agent,
might have been influenced by these factors.
which combined explicit and implicit communi-

### On the EXIM configuration, we used implicit

cations. Participants smiled at or talked to the
communications not only to make Luna and Sofia
virtual agents during the interactions and most
more pleasant, sociable, and transparent. Indeed,
comments made about them were positive, either
we also hoped they would help participants duron the questionnaires or to the researcher coning the task execution, since the virtual agents
ducting the experiment. People seemed to have
looked at the correct object they believe people
positive reactions to them, which was also obwould point to in Phase 1. Moreover, they used
servedintheacceptanceanalysis.Oneparticipant
people’sgazetoestimatetheirattentionfocusand
commented
give hints with the correct answers in Phase 2. In
“I found the interaction very interfact,basedonourinterpretationoftheexperiment
esting, and, specially after interacting
recordings, we believe that at least four people
with Luna [the EXIM virtual agent], I
might not have seen the counting images and
noticedthatthesimplefactofthevirtual
addedcorrectvaluesonlytrustingtheinformation
agent to ‘look’ at my direction made a
providedbythevirtualagent.Evenwhenthesysdifference on how I felt with respect to
tem detected a wrong gaze direction, the virtual
the task.”
agent’s own gaze complemented the communica-
Another person commented that “the voice is irtion and the participant could infer which object
ritant” and another one said to the experimenter
that they did not like “these virtual agents”.7
8PleaserefertoSection5formoredetailsabouttheexclu-
7AllcommentsweretranslatedfromPortuguese. sions.

<!-- Page 17 -->

17
it was referring to. Four other people neither un- three of our six hypotheses. Variables more rederstood nor considered the virtual agent’s hint lated to the task, such as time, number of errors,
and added wrong values despite being prompted and perceived efficiency, did not seem to be afwith the correct answer. fected by the communication type. This may be
In Phase 1, the videos suggest that some par- attributed to the fact that the tasks were not
ticipants might not have seen the virtual agents’ necessarily collaborative and perhaps too simple,
implicit communications, as they did not seem making external help unnecessary to their sucto look at the screen displaying the virtual agent cessful conclusion. Our results differ from works
while executing the task. On the other hand, such as the one by Breazeal et al. [11], where
otherpeopleclearlynoticedthatthevirtualagent they observed effects on performance measures in
looked at them because they played around with ataskwherepeopleguidedtherobottopushsome
its gaze for a moment, moving their bodies to see buttons, so they needed to work together.
thevirtualagentfollowingthem..Peoplemayalso According to participants’ comments and the
not have attributed meaning to its gaze, seeing videoanalysis,ourinstructionsmaynothavebeen
it but not interpreting it. One participant seemed clear enough. From our final sample, 7.7% of the
not to have understood that one color was from errors in Phase 1 are extra errors for not finishthe password and, after the interaction, told the ing including the correct colors by pointing at the
experimenter that the virtual agent kept looking right colored boxes. In Phase 2, 16.1% of the erthe other way, without realizing it was looking at rors are due to counting values not being inserted
thecorrectobject.Afterall,itwasnotnecessarily before the timeout (see Section 3.4), indicating
a collaborative task, meaning that it did not need difficulties in completing the task. The recordings
to be done collaboratively, although the virtual also show that people might have not perceived
agent could help. We believe that these aspects some of the virtual agents’ implicit communicamayhaveinfluencedtheperceivedefficiencyofthe tions,suchasthefacialexpressionsinPhase1.All
interaction, with some people attributing little or thesefactorscouldhaveinfluencedourcomparison
no credit to the virtual agent for the completion of task-related variables. The experimental proof the tasks. tocol can be improved to tackle those problems,
for example using a more collaborative task and
giving more detailed instructions.
7 Conclusions To measure the subjective outcomes, we used
questionnaires with Likert scales. Some works
In this work, we have investigated the effects of propose models and instruments to measure peocombining explicit and implicit communications ple’s perceptions about technologies and robots
onperformanceandonpeople’sperceptionswhile [68, 5, 30], but there is no standard in the HRI
interacting with virtual agents. For that, we used area. When using Likert scales, usually a measure
acommunicationinfrastructure[14]toproposean called Cronbach’s alpha [19] is reported to evaluinteraction experiment similar to a game. Follow- atereliabilityandinternalconsistenceofthescale
ing the HRI literature, we have hypothesized that (see[31,52,20,63]),althoughthereissomediscususing explicit and implicit communications from sion about the adequacy of this measure [21, 55].
human and virtual agent would reduce time and In our work, we have not made any analysis of
number of errors in task execution and increase this type, so the adequacy of our questionnaires
acceptanceofthevirtualagent,itssociabilityand to measure the subjective outcomes needs to be
transparency, and the perceived efficiency of the evaluated in future works.
interaction. Finally,despitesomelimitationsofourresults,
With our relatively small sample of 26 valid which might have been caused by the relatively
participants, we cannot draw strong conclusions small sample with relatively little diversity, the
about the presence or absence of effects, but posterior distributions we estimated can be used
the results suggest that combining explicit and to inform prior distributions in future works conimplicit communications have improved the sub- sidering a larger population. This is one of the
jective measures related to the virtual agent (ac- reasons we chose to use a Bayesian approach to
ceptance, sociability, and transparency), favoring

<!-- Page 18 -->

18
the data analysis, so our results can more easily sample generator also does not prevent inverted
serve as a stepping stone to future research. thresholds from being generated. To solve that
Future work will focus on improving the ex- problem, Kruschke includes a condition thatif inperimental protocol, checking the adequacy of verted thresholds are generated at the kth level,
our questionnaires, and testing the hypotheses the corresponding calculated probability would
with larger and more diverse samples. Using the be zero and then the thresholds are discarded
data we collected about the participants’ age, [41, Section 23.2.1]. This implementation solution
gender, stage of education, and familiarity with works as long as there is at least one answer in
virtualagents,theinfluenceofthesefactorsinour each level of the data sample. When the data
objective and subjective measures can also be in- contains an empty level, there is nothing in the
vestigated. Our data might be used to generate mathematical model or in the implementation
new work hypotheses about these possible influ- thatpreventthegenerationofinvertedthresholds,
ences. Finally, the study can be replicated with and hence negative probabilities.
different types of agents, such as more realistic This model limitation is specially problematic
virtual agents and humanoids, and the effects of whenwehaveasmalldatasample,whichincreases
these various embodiments can be analyzed. the chance of an empty level. In his implementation,Kruschkedecidedtocompressouttheempty
8 Statements and declarations levels. For example, if there are five levels of response (1 to 5) but level 2 does no occur in the
This work was supported by the Brazilian fund- data sample, Kruschke’s implementation changes
ing agency CNPq (Conselho Nacional de Desen- the data set, considering only four levels (1 to 4).
volvimento Científico e Tecnológico) and by the Then,thisupdateddatasetisusedintheBayesian
Royal Academy of Engineering under the Re- inference. We can easily see that this change can
search Chairs and Senior Research Fellowships altertheparameterestimation;iftheoriginaldata
programme. The authors have no competing in- set, with empty level 2, came from a latent distriterests to declare that are relevant to the content bution with mean µ = 4, the compression would
of this article. shift the estimated mean to a value smaller than
4.10

### Ethics approval and consent


### BecauseKruschke’sdatacompressionstrategy

Theexperimentinvolvinghumanparticipantswas could bias our estimation and the ordinal levels
approved by the ethics committee of the Federal are related to the actual response options in the
University of Minas Gerais, and the research is questionnaires, we chose not to follow it. Thereidentified by the number 44110621.5.0000.5149.9 fore, we consider some alternatives to deal with
Informed consent was obtained from all partici- theemptylevelsproblem,summarizedinTable4.
pants included in the study. One option is to use more restricted priors for
the thresholds, more specifically by reducing the
A Ordinal model limitations standard deviation. That solves the problem of
and adjustments due to negative probabilities but also adds an estimation
bias, since restricted priors mean a strong initial
empty levels
belief about the parameter value. Another reason
againsttherestrictedpriorsisthatcenteringthem

### On the ordinal model, described in Section 4.3,

at the same values for all items already confronts
there is nothing to specify that the thresholds are
theideathatdifferentitemsaccessthesamelatent
in ascending order, that is, θ < θ < <
1 2 ··· variable through different thresholds. Therefore,
θ . However, if we have inverted thresholds
K − 1 considerable standard deviation should be used
(θ > θ ), the probability of the kth ordinal
k 1 k
−
level becomes negative, violating the first probability axiom. The MCMC posterior distribution 10WediscussedthematterwithProf.JohnKruschkeinprivate communication. According to him, to keep the original
numberoflevelsevenwhenthereareemptylevelsinthedata
sample,itwouldbenecessarytochangethemodel(usingmore
9The approval can be checked on the website https:// restrictedpriorsforthethresholds,forexample)andthemechplataformabrasil.saude.gov.br/,informingtheresearchnumber anismtoselectpossiblethresholdsduringtheMCMCsample
onoptionConfirmarAprovaçãopeloCAAEouParecer. generation.

<!-- Page 19 -->

19
Table 4 Advantagesanddrawbacksofeachmethodconsideredfortheanalysisofordinaldatacontaining
empty levels.

### Advantages Drawbacks

Keep empty levels Original data Possible negative probabilities

### Changed data

Compress empty levels No negative probabilities

### Estimation bias

Restricted prior distributions Original data

### Estimation bias

for thresholds θ No negative probabilities
k

### Changed data

Add extra data No negative probabilities
Inflated estimation of the latent
scale parameter τ
to allow greater variability. Moreover, we do not and/or scale parameter, it would be more diffihave enough knowledge to place them at different cult to interpret the estimations. Consequently,
locations for each item. following Kruschke’s suggestion [41], a better op-
Another alternative is to add extra data to tion is to fix the extreme thresholds of one of the
eliminateemptylevels,andweconsiderthreeways items considering the response levels in the quesof doing it: 1) adding one extra answer in all lev- tionnaires.Wearbitrarilychosetofixtheextreme
els, empty or not, to avoid shifting the estimation thresholds of the first item of each scale as shown
ofthemeanµ;2)addingoneextraansweronlyin in Table 3.
empty levels; 3) and adding one extra answer in Unlike the objective measures, which do not
each empty level and adding extra answers in non useanordinalmodelandforwhichwepairtheobempty levels to keep the probability (frequency of servations for each participant and use the differoccurrence)ofeachlevelasclosetotheoriginalas ence between the communication configurations,
possible, adding a maximum of K new answers in we estimate the parameters of each group sepathe data sample of each item. In our tests, when ratelyforthesubjectivemeasures.Thisisbecause
we added extra data, we observed an inflated es- considering five response levels (see Section 3.4),
timation of the scale parameter τ, with greater the difference between communication configuracredibilitygiventovalueshigherthantherealone. tions would assume values from 4 to 4, which
−
Since all aforementioned alternatives to the donothaveadirectrelationwiththeoriginalfive
solution of empty levels change the estimated dis- response options in the questionnaire. Rememtribution, a sensible choice must consider two ber that we fix the extreme thresholds in 1.5 and
main aspects: the results should be mathemati- K 0.5 to enable us to interpret the estimation
−
cal coherent (no negative probabilities) and the of the latent parameters considering the actual
effects of the change in the data sample should responseoptionspresentedtoparticipants,asdisnot favor our hypotheses (that is, we seek a con- cussed in Section 4.3 (see Fig. 8). Moreover, more
servativesolution).Usingsimulateddata,wehave levels would increase the chance of empty ones
found the best consistent results by adding ex- and require more extra data in those empty levtra data only to empty levels. With this method, els, causing more change in the final sample and
only the estimation of the scale parameter τ was the estimations.
significantly hindered, making it more difficult to
validateourhypotheses.Theparameterτ appears

### References

on the denominator of the effect size; therefore,
greater scales imply smaller effect sizes.
[1] AgrigoroaieR,CiocirlanSD,TapusA(2020)

### Another important aspect of the model is how

In the Wild HRI Scenario: Influence of Regthe estimations strongly depend on the value of
ulatory Focus Theory. Frontiers in Robotics
the fixed parameters. If we fix the latent mean
and AI 7(April):1–11. https://doi.org/10.

<!-- Page 20 -->

20
3389/frobt.2020.00058 [10] Breazeal C (2003) Toward sociable robots.
[2] Ajoudani A, Zanchettin AM, Ivaldi S, Robotics and Autonomous Systems 42(3-
et al (2018) Progress and prospects of 4):167–175. https://doi.org/10.1016/
the human-robot collaboration. Autonomous S0921-8890(02)00373-1
Robots 42(5):957–975. https://doi.org/10. [11] Breazeal C, Kidd C, Thomaz A, et al
1007/s10514-017-9677-2 (2005) Effects of nonverbal communication
[3] AndristS,GleicherM,MutluB(2017)Look- on efficiency and robustness in human-robot
ing Coordinated: Bidirectional Gaze Mech- teamwork. In: 2005 IEEE/RSJ International
anisms for Collaborative Interaction with Conference on Intelligent Robots and Sys-
Virtual Characters. In: Proceedings of the tems. IEEE, https://doi.org/10.1109/IROS.
2017 CHI Conference on Human Factors 2005.1545011
in Computing Systems. ACM, Denver Col- [12] Bruce A, Nourbakhsh I, Simmons R (2002)
orado USA, pp 2571–2582, https://doi.org/ The role of expressiveness and atten-
10.1145/3025453.3026033 tion in human-robot interaction. In: Pro-
[4] AsfourT,RegensteinK,AzadP,etal(2006) ceedings 2002 IEEE International Confer-
ARMAR-III: An Integrated Humanoid Plat- ence on Robotics and Automation (Cat.
formforSensory-MotorControl.In:20066th No.02CH37292), vol 4. IEEE, pp 4138–
IEEE-RAS International Conference on Hu- 4142,https://doi.org/10.1109/ROBOT.2002.
manoid Robots. IEEE, pp 169–175, https: 1014396
//doi.org/10.1109/ICHR.2006.321380 [13] Buschmeier H, Kopp S (2018) Communica-
[5] Bartneck C, Kulić D, Croft E, et al tive Listener Feedback in Human–Agent In-
(2009)MeasurementInstrumentsfortheAn- teraction: Artificial Speakers Need to Be
thropomorphism, Animacy, Likeability, Per- Attentive and Adaptive. In: Proceedings of
ceived Intelligence, and Perceived Safety the 17th International Conference on Auof Robots. International Journal of So- tonomous Agents and Multiagent Systems
cial Robotics 1(1):71–81. https://doi.org/10. (AAMAS 2018), Stockholm, Sweden
1007/s12369-008-0001-3 [14] Campos ACA, Adorno BV (2020) De-
[6] BauerA,WollherrD,BussM(2008)Human- velopment of Human-Robot Communica-
RobotCollaboration:ASurvey.International tion Technologies for Future Interaction
Journal of Humanoid Robotics 05(01):47–66. Experiments. In: 2020 Latin American
https://doi.org/10.1142/S0219843608001303 Robotics Symposium (LARS), 2020 Brazil-
[7] BavelasJB,BlackA,LemeryCR,etal(1986) ian Symposium on Robotics (SBR) and
"I Show How You Feel": Motor Mimicry as 2020 Workshop on Robotics in Education
aCommunicativeAct.JournalofPersonality (WRE). IEEE, pp 1–6, https://doi.org/10.
and Social Psychology 50(2):322–329. https: 1109/LARS/SBR/WRE51543.2020.9306965
//doi.org/10.1037/0022-3514.50.2.322 [15] Carifio J, Perla R (2008) Resolving the
[8] Baxter P, Kennedy J, Senft E, et al (2016) 50-year debate around using and mis-
From characterising three years of HRI using Likert scales. Medical Education
to methodology and reporting recommen- 42(12):1150–1152. https://doi.org/10.1111/j.
dations. In: 2016 11th ACM/IEEE Inter- 1365-2923.2008.03172.x
national Conference on Human-Robot In- [16] Che Y, Okamura AM, Sadigh D (2020) Effiteraction (HRI), vol 2016-April. IEEE, pp cient and Trustworthy Social Navigation via
391–398, https://doi.org/10.1109/HRI.2016. Explicit and Implicit Robot-Human Com-
7451777 munication. IEEE Transactions on Robotics
[9] Belkaid M, Kompatsiari K, De Tommaso D, pp 1–16. https://doi.org/10.1109/TRO.2020.
et al (2021) Mutual gaze with a robot affects 2964824, arXiv:1810.11556
human neural activity and delays decision- [17] ChenTL,CiocarlieM,CousinsS,etal(2013)
making processes. Science Robotics 6(58). Robotsforhumanity:Usingassistiverobotics
https://doi.org/10.1126/scirobotics.abc5044 to empower people with disabilities. IEEE
Robot Automat Mag 20(1):30–39. https://

<!-- Page 21 -->

21
doi.org/10.1109/MRA.2012.2229950 https://doi.org/10.1177/0278364916688255
[18] CohenJ(1988)StatisticalPowerAnalysisfor [27] Gombolay MC, Gutierrez RA, Clarke SG,
the Behavioral Sciences. Lawrence Erlbaum et al (2015) Decision-making authority, team

### Associates efficiency and human worker satisfaction in

[19] Cronbach LJ (1951) Coefficient al- mixed human - robot teams. Autonomous
pha and the internal structure of Robots 39(3):293–312. https://doi.org/10.
tests. Psychometrika 16(3):297–334. 1007/s10514-015-9457-9
https://doi.org/10.1007/BF02310555 [28] Guznov S, Lyons J, Pfahler M, et al (2019)
[20] Crossman MK, Kazdin AE, Kitt ER (2018) Robot Transparency and Team Orientation
The influence of a socially assistive robot Effects on Human-Robot Teaming. Internaon mood, anxiety, and arousal in children. tional Journal of Human-Computer Inter-
Professional Psychology: Research and Prac- action pp 650–660. https://doi.org/10.1080/
tice 49(1):48–56. https://doi.org/10.1037/ 10447318.2019.1676519
pro0000177 [29] Harpe SE (2015) How to analyze Likert and
[21] Dunn TJ, Baguley T, Brunsden V (2014) other rating scale data. Currents in Phar-
From alpha to omega: A practical solution macy Teaching and Learning 7(6):836–850.
to the pervasive problem of internal con- https://doi.org/10.1016/j.cptl.2015.08.001
sistency estimation. British Journal of Psy- [30] Heerink M, Kröse B, Evers V, et al (2010)
chology 105(3):399–412. https://doi.org/10. Assessing Acceptance of Assistive Social
1111/bjop.12046 Agent Technology by Older Adults: The
[22] Fiore SM, Wiltshire TJ, Lobato EJC, et al Almere Model. International Journal of So-
(2013)Towardunderstandingsocialcuesand cial Robotics 2(4):361–375. https://doi.org/
signalsinhuman-robotinteraction:Effectsof 10.1007/s12369-010-0068-5
robot gaze and proxemic behavior. Frontiers [31] HindsPJ,RobertsTL,JonesH(2004)Whose
inPsychology4(NOV):1–15.https://doi.org/ Job Is It Anyway? A Study of Human-Robot
10.3389/fpsyg.2013.00859 Interaction in a Collaborative Task. Human-
[23] FongT,NourbakhshI,DautenhahnK(2003) ComputerInteraction19(1-2):151–181.https:
A survey of socially interactive robots. //doi.org/10.1080/07370024.2004.9667343
Robotics and Autonomous Systems 42:143– [32] Hirano T, Shiomi M, Iio T, et al (2018) How
166.https://doi.org/10.1016/S0921-8890(02) DoCommunicationCuesChangeImpressions
00372-X ofHuman-RobotTouchInteraction?Interna-
[24] Gockley R, Bruce A, Forlizzi J, et al (2005) tional Journal of Social Robotics 10:21–31.
Designing robots for long-term social in- https://doi.org/10.1007/s12369-017-0425-8
teraction. In: 2005 IEEE/RSJ International [33] HoffmanG,ZhaoX(2021)APrimerforCon-
Conference on Intelligent Robots and Sys- ducting Experiments in Human–Robot Intems. IEEE, pp 1338–1343, https://doi.org/ teraction. J Hum-Robot Interact 10(1):1–31.
10.1109/IROS.2005.1545303 https://doi.org/10.1145/3412374
[25] Gockley R, Forlizzi J, Simmons R (2006) [34] Huang CM, Mutlu B (2016) Anticipatory
Interactions with a moody robot. In: Pro- robot control for efficient human-robot colceeding of the 1st ACM SIGCHI/SIGART laboration. In: ACM/IEEE International
Conference on Human-Robot Interaction - ConferenceonHuman-RobotInteraction,vol
HRI ’06. ACM Press, New York, New York, 2016-April.IEEE,pp83–90,https://doi.org/
USA, pp 186–193, https://doi.org/10.1145/ 10.1109/HRI.2016.7451737
1121241.1121274 [35] Iwasaki M, Zhou J, Ikeda M, et al (2019)
[26] Gombolay M, Bair A, Huang C, et al (2017) "That Robot Stared Back at Me!": Demon-
Computational design ofmixed-initiativehu- stratingPerceptualAbilityIsKeytoSuccessman - robot teaming that considers human ful Human - Robot Interactions. Frontiers in
factors:Situationalawareness,workload,and Robotics and AI 6(September):1–12. https:
workflowpreferences.TheInternationalJour- //doi.org/10.3389/frobt.2019.00085
nal of Robotics Research 36(5-7):597–617. [36] Jackman S (2009) Bayesian Analysis for the
Social Sciences, 1st edn. Wiley Series in

<!-- Page 22 -->

22
Probability and Statistics, John Wiley & possibly go wrong? Journal of Experimen-
Sons,Ltd,UnitedKingdom,https://doi.org/ tal Social Psychology 79(August):328–348.
10.1002/9780470686621 https://doi.org/10.1016/j.jesp.2018.08.009
[37] Kelter R (2020) Bayesian alternatives to null [46] LikertR(1932)ATechniquefortheMeasurehypothesis significance testing in biomedi- ment of Attitudes. Archives of Psychology
cal research: A non-technical introduction to [47] Ljungblad S, Kotrbova J, Jacobsson M, et al
Bayesian inference with JASP. BMC Medi- (2012) Hospital Robot at Work: Something
calResearchMethodology20(1).https://doi. Alien or an Intelligent Colleague? In: Proorg/10.1186/s12874-020-00980-6 ceedings of the ACM 2012 Conference on
[38] Kelter R (2021) Bayesian and frequen- Computer Supported Cooperative Work -
tist testing for differences between two CSCW ’12. ACM Press, New York, New
groups with parametric and nonparamet- York, USA, pp 177–186, https://doi.org/10.
ric two-sample tests. WIREs Computa- 1145/2145204.2145233
tional Statistics 13(6):1–29. https://doi.org/ [48] Mavridis N (2015) A review of ver-
10.1002/wics.1523 bal and non-verbal human-robot interactive
[39] Knepper RA, Mavrogiannis CI, Proft J, communication. Robotics and Autonomous
et al (2017) Implicit Communication in Systems63:22–35.https://doi.org/10.1016/j.
a Joint Action. In: Proceedings of the robot.2014.09.031
2017 ACM/IEEE International Conference [49] Meek GE, Ozgur C, Dunning K (2007) Comon Human-Robot Interaction. ACM, New parison of the t vs. Wilcoxon Signed-Rank
York,NY,USA,pp283–292,https://doi.org/ Test for Likert Scale Data and Small Sam-
10.1145/2909824.3020226 ples. Journal of Modern Applied Statisti-
[40] Kruschke JK (2013) Bayesian estimation su- cal Methods 6(1):91–106. https://doi.org/10.
persedes the t test. Journal of Experimental 22237/jmasm/1177992540
Psychology: General 142(2):573–603. https: [50] Meghdari A, Shariati A, Alemi M, et al
//doi.org/10.1037/a0029146 (2018) Design Performance Characteristics
[41] Kruschke JK (2015) Doing Bayesian Data of a Social Robot Companion "Arash" for
Analysis:ATutorialwithR,JAGS,andStan. Pediatric Hospitals. International Journal of
Academic Press / Elsevier, Burlington, MA HumanoidRobotics15(05):1850019.https://
[42] Kruschke JK, Liddell TM (2018) The doi.org/10.1142/S0219843618500196
Bayesian New Statistics: Hypothesis testing, [51] MontgomeryDC,RungerGC(2011)Applied
estimation, meta-analysis, and power analy- StatisticsandProbabilityforEngineers,Fifth
sisfromaBayesianperspective.Psychonomic Edition. John Wiley & Sons, Inc.
Bulletin & Review 25(1):178–206. https:// [52] Mutlu B, Yamaoka F, Kanda T, et al (2009)
doi.org/10.3758/s13423-016-1221-4 Nonverbal leakage in robots: Communica-
[43] Lazzeri N, Mazzei D, De Rossi D (2014) tion of intentions through seemingly unin-
Development and Testing of a Multimodal tentional behavior. In: Proceedings of the
AcquisitionPlatformforHuman-RobotInter- 4th ACM/IEEE International Conference on
action Affective Studies. Journal of Human- Human Robot Interaction - HRI ’09. ACM
Robot Interaction 3(2). https://doi.org/10. Press, New York, New York, USA, pp 69–76,
5898/JHRI.3.2.Lazzeri https://doi.org/10.1145/1514095.1514110
[44] Lenz A, Skachek S, Hamann K, et al (2010) [53] Nanna MJ, Sawilowsky SS (1998) Analy-
The BERT2 infrastructure: An integrated sis of Likert scale data in disability and
system for the study of human-robot in- medical rehabilitation research. Psychologiteraction. In: 2010 10th IEEE-RAS Inter- cal Methods 3(1):55–67. https://doi.org/10.
national Conference on Humanoid Robots. 1037//1082-989x.3.1.55
IEEE, pp 346–351, https://doi.org/10.1109/ [54] Natarajan M, Seraj E, Altundas B, et al

### ICHR.2010.5686319 (2023) Human-Robot Teaming: Grand Chal-

[45] Liddell TM, Kruschke JK (2018) Analyzing lenges. Curr Robot Rep https://doi.org/10.
ordinaldatawithmetricmodels:Whatcould 1007/s43154-023-00103-1

<!-- Page 23 -->

23
[55] Peters GJY (2014) The alpha and the omega Stronger Perceived Capacity to Feel. Fronofscalereliabilityandvalidity.TheEuropean tiers in Robotics and AI 6(September):1–9.
Health Psychologist 16(2):56–69 https://doi.org/10.3389/frobt.2019.00088
[56] RauPP,LiY,LiD(2009)Effectsofcommu- [64] TohLPE,CausoA,TzuoPW,etal(2016)A
nicationstyleandcultureonabilitytoaccept review on the use of robots in education and
recommendations from robots. Computers in young children. Educational Technology and
Human Behavior 25(2):587–595. https://doi. Society 19(2):148–163
org/10.1016/j.chb.2008.12.025 [65] Unhelkar VV, Yang XJ, Shah JA (2017)
[57] Robins B, Dautenhahn K, Nadel J (2018) Challenges for Communication Decision-
Kaspar, the social robot and ways it may Making in Sequential Human-Robot Collabhelp children with autism - an overview. En- orative Tasks. Workshop on Mathematical
fance 1(1):91. https://doi.org/10.3917/enf2. Models, Algorithms, and Human-Robot In-
181.0091 teraction at Robotics: Science and Systems
[58] Sebanz N, Bekkering H, Knoblich G (2006) [66] UnhelkarVV,DorrS,BubeckA,etal(2018)
Joint action: Bodies and minds mov- Mobile Robots for Moving-Floor Assembly
ing together. Trends in Cognitive Sci- Lines: Design, Evaluation, and Deployment.
ences10(2):70–76.https://doi.org/10.1016/j. IEEE Robotics & Automation Magazine
tics.2005.12.009 25(2):72–81. https://doi.org/10.1109/MRA.
[59] Shah J, Wiken J, Williams B, et al (2011) 2018.2815639
Improvedhuman-robotteamperformanceus- [67] van Maris A, Zook N, Caleb-Solly P, et al
ing chaski, a human-inspired plan execution (2020) Designing Ethical Social Robots - A
system. In: Proceedings of the 6th Interna- LongitudinalFieldStudyWithOlderAdults.
tional Conference on Human-Robot Inter- Frontiers in Robotics and AI 7(January).
action - HRI ’11. ACM Press, New York, https://doi.org/10.3389/frobt.2020.00001
New York, USA, pp 29–36, https://doi.org/ [68] Venkatesh V, Morris MG, Davis GB, et al
10.1145/1957656.1957668 (2003) User Acceptance of Information
[60] Six S, Schlesener E, Hill V, et al (2025) Technology: Toward a Unified View. MIS
Impact of Conversational and Animation Quarterly 27(3):425–478. https://doi.org/10.

### Features of a Mental Health App Virtual 2307/30036540

Agent on Depressive Symptoms and User [69] WagenmakersEJ,MarsmanM,JamilT,etal
Experience Among College Students: Ran- (2018) Bayesian inference for psychology.
domizedControlledTrial.JMIRMentHealth Part I: Theoretical advantages and practical
12:e67381–e67381. https://doi.org/10.2196/ ramifications. Psychonomic Bulletin & Re-
67381 view 25(1):35–57. https://doi.org/10.3758/
[61] Takayama L, Pantofaru C (2009) Influences s13423-017-1343-3
on proxemic behaviors in human-robot in- [70] Zhang H, Fricker D, Yu C (2010) A
teraction. In: 2009 IEEE/RSJ International Multimodal Real-Time Platform for Study-
Conference on Intelligent Robots and Sys- ing Human-Avatar Interactions. In: Intertems. IEEE, pp 5495–5502, https://doi.org/ national Conference on Intelligent Virtual
10.1109/IROS.2009.5354145 Agents, pp 49–56, https://doi.org/10.1007/
[62] Tanaka M, Ishii A, Yamano E, et al 978-3-642-15892-6_6
(2012) Effect of a human-type communica- [71] Zhang Y, Ratnayake TS, Sew C, et al (2025)
tion robot on cognitive function in elderly Can you pass that tool?: Implications of Inwomen living alone. Medical Science Moni- direct Speech in Physical Human-Robot Coltor 18(9):CR550–CR557. https://doi.org/10. laboration. In: Proceedings of the 2025 CHI
12659/MSM.883350 Conference on Human Factors in Computing
[63] Tatsukawa K, Takahashi H, Yoshikawa Y, Systems. ACM, Yokohama Japan, pp 1–18,
etal(2019)AndroidPretendingtoHaveSim- https://doi.org/10.1145/3706598.3713780
ilar Traits of Imagination as Humans Evokes

<!-- Page 24 -->

1

### Supplementary Material: A study on the effects of mixed

explicit and implicit communications in human-virtual-agent
interactions, in International Journal of Social Robotics

### Ana Christina Almada Campos1* and Bruno Vilhena Adorno2

1Graduate Program in Electrical Engineering, Universidade Federal de Minas Gerais, Av.
Antônio Carlos 6627, Belo Horizonte, 31270-901, MG, Brazil. ORCID:
https://orcid.org/0000-0002-7800-5640.
2Manchester Centre for Robotics and AI, The University of Manchester, Oxford Rd,
Manchester, M13 9PL, UK. ORCID: https://orcid.org/0000-0002-5080-8724.
*Corresponding author(s). E-mail(s): campos.aca@outlook.com;

### Contributing authors: bruno.adorno@manchester.ac.uk;

This supplementary material shows the complete data from Likert scales as metric data can lead to
results of the experiment described in the main systematic false positives, fails in detection, and
paper to compare two communication configura- even inversion of effects. They argue that data
tions, EX and EXIM. It includes the posterior fromLikertscaleshouldbetreatedasordinal,and
distributions of all parameters estimated, and a that taking the average does not solve the probposterior check of model adequacy, comparing lems. An option often used in the literature is a
the data sample with the estimations. Section 1 non-parametric alternative for the t-test, such as
shows the results for the Bayesian analysis of the the Wilcoxon signed-rank test. Despite being a
objective measures, namely time and number of non-parametric test that does not assume data in
errors. The results for the Bayesian analysis of intervalorratioscale,thistestalsorequirestaking
the subjective measures, that is, acceptance, so- theaverageofthepointsintheLikertscale,which
ciability, transparency of the virtual agents and is already assuming that the data can be treated
perceived efficiency of the interaction, are shown as metric [8]. For any readers still interested in
inSection2.Forthediscussionsabouttheresults, the results employing null hypothesis significance
pleaserefertoSections5and6ofthemainpaper. tests, Section 3 shows the outcome of these for
As discussed in the main paper, we chose each of the variables we evaluated.
Bayesian methods because they provide richer information [6, 7, 10, 4], but also because of the
1 Objective measures results
subjective measures. These perceptions were assessed using Likert scales [9]. Some works suggest
For the objective measures of time and number
thatifwetaketheaverageofpointsfromtheitems
of errors, we use the metric model described in
of the scale, it can be treated as an interval scale

### Section 4.2 of the main paper. We estimate the

and tests such as the t-test can be conducted, as
mean µ, scale τ, and normality parameter ν of
long as its other assumptions hold [1, 2]. Howthe latent t distributions of the difference in time
ever, Liddell and Kruschke [8] show that treating
∆t = t t and number of errors ∆e =

## Ex Exim

−

<!-- Page 25 -->

2
e e , and calculate the effect sizes using spreadofthecloudsindicatethespreadofthedis-

## Ex Exim

−
Eq. 4 in the main paper. Also, some credible t tributions and the dashed vertical lines indicate
distributions were superimposed on the data of the estimated mean of each threshold. The exeach variable to check model adequacy. ample data sample contains more answers in the
Fig. 1 shows the results for difference in time higher response levels so the estimations of the
and Fig. 2 for the difference in the number of higher thresholds are more precise than the lower
errors, with and without outliers. We show the ones.TheellipsesonFig.4cover95%oftheclouds
posteriors for the normality parameter ν in log ofthresholdsθ (ontheleft)andθ (ontheright)
1 4
scale to ease visualization, since its distribution and the θ ellipse is larger than the θ ellipse, in-
1 4
is very asymmetric in a linear scale. Most vari- dicating that the θ posterior distribution is more
4
ation in the tails of the t distribution occur for compact, i.e., a more precise estimation.
smallvaluesofν,andvaluesgreaterthanlog(ν)= The small blue circles in Fig. 4 represent the
1.47 (ν = 30 in the original scale) represent thresholds values in each combination of paramedistributions very close to a normal [6]. ters in the MCMC (Markov Chain Monte Carlo)
sample,andtheverticalcoordinateisthemeanof
2 Subjective measures results the four thresholds in that combination. For each
step of the generated MCMC sample,2 the points
Fig. 3 shows histograms with participants’ re- are at the same height in the plot. The horizontal
sponses to each item and group for all the sub- dashed lines are related to two subsequent steps
jective measures, namely acceptance, sociability, intheMCMCsamplegeneration,steps17540and
transparency of the virtual agents, and perceived 17541,3 and the height of the lines is the mean of
efficiency of the interactions. the thresholds (black dots) in each step. During
Theordinalmodelusedforthesubjectivemea- the generation of the MCMC sample, if a higher
suresisdescribedinSection4.3ofthemainpaper. value is chosen for a threshold, all the other item
We estimate the mean µ, scale τ, and normality thresholds will need to adjust and tend to be
parameter ν of the latent t distributions, and the higher too, to keep the probability of each ordifree thresholds θ k , with k 1,...,K 1 , where nal response level, calculated as the cummulative
∈ { − }
K =5isthenumberofordinallevels.Weinterpret probability between two consecutive thresholds in
the estimation of the mean µ considering the five thelatentdistribution(seeSection4.3inthemain
ordinallevelsofresponse(seeexampleinFig.8in paper). With that, each new step tends to shift
Section 4.3 of the main paper). Remember that, the thresholds set up and right or down and left,
accordingtothemodel,theordinalresponsescale asweseebythesubsequentstepsshowninFig.4.
isawayofaccessingthelatentdistribution,which Figs. 5 and 6 show the posterior distributions
is not limited by the response options. Thus, the for the acceptance of the virtual agents. The exestimated credible values of the mean µ of the la- treme thresholds θ[1] and θ[1] of the first item

## 1 K 1

tent distribution can be lower than 1 and higher of each scale are always at 1.5−and 4.5, since they
than 5, like in some of the distributions we ob- were fixed at these values.
tained. We also calculate the difference between For the model adequacy check, we estimate
the means and scales of each condition, and the the probability of each ordinal level using the
effect sizes d sub for each variable using Eq. 5 in estimated parameters. Fig. 7 shows the final acthe main paper. ceptance data histograms (with the extra an-
Theitemthresholds,whichtranslatethelatent swersincluded,asexplainedintheSection4.3and
variable into the ordinal responses, are strongly Appendix A of the main paper) superimposed
correlated, so we present their estimations to- with the median of the estimated probability of
gether, like Kruschke [6]. 1 Fig. 4 shows example
posterior distributions of the thresholds of an
item, represented by the blue points clouds. The
2FormoreinformationabouttheMCMCsamplegeneration,
1The figures in this document containing our results were pleaserefertoChapter7of[6].
generatedusingthescriptsprovidedbyKruschkeandLiddell 3ThegeneratedMCMCsamplecontains20000combinations
[6,8]andadaptedtoourwork. ofparameters.

<!-- Page 26 -->

3

### Mean

µ∆t (cid:1)
mo=
50 0 50
(cid:1)
md=
1.38 (cid:1)
1.73
m=
(cid:1)
1.68
54.2% 45.8%
(cid:1)
Scale
3 2
(cid:0)

### Normality

md 82.4 md=143
m=83 mo=79.2 m=1.4 mo=1.56
58 2 2
40 60 80 100 120 140 160 0.0 0.5 1.0 1.5 2.0 2.5
∆t log 10 ν ∆t

### Effect size

d obj,∆t (cid:1)
mo=
0.5 0.0 0.5
(cid:1)
md= 00209
m= 0.0209
(cid:1)
0.02
34.6% 27.7%
(cid:1)
Histogram and credible distributions
0 75
Data (cid:1)
200
(cid:1)
100 0 100 200
Fig. 1 ResultsoftheBayesianinferenceofthetimedifference∆tbetweenEXandEXIMconfigurations,
inseconds.Thefirstrowshowstheposteriordistributionsofthemeanµ,scaleτ,andnormalityν (inlog
scale) of the latent t distribution. On the left of the second row is the distribution of the effect size d
obj
calculated with the null value µ = 0. Mean (m), median (md), mode (mo), and the limits of the 95%
0
HDIareannotatedinthedistributions.Dashedverticallinesindicatethenullvalueinthedistributionof
themeanµandtheROPEintheeffectsizedistributiontogetherwiththepercentagesofthedistribution
below, between and above the values associated with the ROPE and the null value. On the right of the
second row, some credible t distributions are superimposed on the data to check model adequacy, and
sample mean (x¯), median (x˜), and standard deviation (s) are shown.
eachlevelandits95%HDI.Levelsthatwereorig- because of the reasons mentioned at the begininally empty and for which we added an extra ning of this document. This test assumes that the
answer are indicated in Fig. 7 by asterisks. sample is from a symmetric population, which is
Figs. 8 to 10 show the results for the sociabil- already true for paired samples, according to Holity of the virtual agents, Figs. 11 to 13 show the lander et al [3] and Kloke and Mckean [5], so this
results for their transparency, and Figs. 14 to 16 assumption was not tested.
showthe resultsfortheperceived efficiencyofthe Table 1 shows the results for the objecinteractions. tive measures. The second column shows the
normality assumption check, using the function shapiro.test4 from package stats (version
4.0.4)forRlanguage.Adecisionwasmadeconsid-
3 Null hypothesis significance
ering a threshold of 5%, i.e., when the p-value is
tests results less than 5% the normality assumption is considered not validated and therefore a nonparametric
For the objective measures of time and number of test is used. The third column shows the tests
errors, the paired t-test was used if the normality assumption was validated, and the Wilcoxon
signed-rank test, if not. For the subjective mea-
4https://stat.ethz.ch/R-manual/R-devel/library/stats/
sures,onlytheWilcoxonsigned-ranktestwasused html/shapiro.test.html/

<!-- Page 27 -->

4

### Mean

µ∆e (cid:1)
4
(cid:1)
md=
mo=0.0848
2 0 2 4
(cid:1)
00774
m=
(cid:1)
0.106
54.2 5.8%
(cid:1)
Scale
1 9
(cid:0)

### Normality

md 2.97 md=0.424
m=30 mo=2.84 m=0.45 mo=0.4
14 7
2 4 6 8 0.0 0.5 1.0 1.5 2.0
∆e log 10 ν∆e
(cid:1)
0 98

### Effect size

d obj,∆e (cid:1)
1.0
(cid:1)
mo=
0.5 0.0 0.5 1.0 1.5
(cid:1)
md= 00264
m= 0.0378
(cid:1)
0.0215
38.1 30.2%
(cid:1)
Histogram and credible distributions
05 85

### Data (cid:1)

10 0 10 20 30
(a) Resultsforthedifferenceinnumberoferrors∆e.

### Mean

µ∆eʹ (cid:1)
3
(cid:1)
2
(cid:1)
mo
1 0 1 2
= (cid:1)
md
0.264 = (cid:1)
0.258
m
= (cid:1)
0.263
66 33.8%
(cid:1)
Scale
mo
1 1
1 2 3 4 5 6
τ∆eʹ
=
md
2.78 =
2.92
m
=
Normality
2.9 o
2.0 4
0.0 0.5 1.0 1.5 2.0 2.5
log 10 ν ∆eʹ
=
md
1.48 =
141
m
=
1.38
0

### Effect size

d obj,∆eʹ (cid:1)
1.0
(cid:1)
mo=
0.5 0.0 0.5
(cid:1)
md= 0.0895
m= 0.105
(cid:1)
0.0884
%
48% 18.9%
(cid:1)
Histogram and credible distributions
0 45
Data (cid:1)
8
(cid:1)
6
(cid:1)
4
(cid:1)
2 0 2 4 6
(b) Resultsforthedifferenceinnumberoferrors∆e′ withoutoutliers.
Fig. 2 ResultsoftheBayesianinferenceofthedifferenceinthenumberoferrorsbetweenEXandEXIM
configurations, with and without outliers. In each figure, the first row shows the posterior distributions
of the mean µ, scale τ, and normality ν (in log scale) of the latent t distribution. On the left of the
second row of each figure is the distribution of the effect size d calculated with the null value µ =0.
obj 0
Mean (m), median (md), mode (mo), and the limits of the 95% HDI are annotated in the distributions.
Dashed vertical lines indicate the null value in the distribution of the mean µ and the ROPE in the
effect size distribution together with the percentages of the distribution below, between and above the
values associated with the ROPE and the null value. On the right of the second row, some credible t
distributions are superimposed on the data to check model adequacy, and sample mean (x¯), median (x˜),
and standard deviation (s) are shown.

<!-- Page 28 -->

5

### Item 1 2 3 4 5 6 Item 1 2 3 4 5

1 2 3 4 5 1 2 3 4 5 1 2 3 4 5 1 2 3 4 5

### Responses EX Responses EXIM Responses EX Responses EXIM

(a) Acceptanceofthevirtualagent. (b) Sociabilityofthevirtualagent.

### Item 1 2 3 4 Item 1 2 3 4

1 2 3 4 5 1 2 3 4 5 1 2 3 4 5 1 2 3 4 5

### Responses EX Responses EXIM Responses EX Responses EXIM

(c) Transparencyofthevirtualagent. (d) Perceivedefficiencyoftheinteraction.
Fig. 3 Histograms of the ordinal responses (five levels) in each item of the Likert scale for the subjective
measures in EX and EXIM groups.
−5 0 5 10
5
4
3
2
1
Thresholds
sdlohserhT
fo
naeM
Fig. 4 Example of posterior distributions of the thresholds θ , θ , θ , and θ of an item.
1 2 3 4

<!-- Page 29 -->

6
Mean EX Scale EX Normality EX
md=5.21 md=2.51 md=109
m=5.23 mo=5.2 m=2.51 mo=2.48 m= .0 mo=1.3
4 15 1 52 01
4 5 6 7 8 1 2 3 4 5 0.0 0.5 1.0 1.5 2.0 2.5
µ τ log ν
acc,EX acc,EX 10 acc,EX
Mean EXIM Scale EXIM Normality EXIM
md=5.93 md=2.99 md=138
m=5.97 mo=5.84 m=3.02 mo=2.89 m=1.36 mo=1.37
4.9 98 20 05 0 07
4 5 6 7 8 1 2 3 4 5 0.0 0.5 1.0 1.5 2.0 2.5
µ τ log ν
acc,EXIM acc,EXIM 10 acc,EXIM

### Difference between means

µ −µ acc,EXIM acc,EX (cid:1)
md=0.718
m=0.735 mo=0.677
2.7% 97.3
0.5 0.5 1.5 2.5
(cid:1)
Difference between scales
0.0 53
τ −τ acc,EXIM acc,EX (cid:1)
md=0.486
m=0.509 mo=0.432
1 0 1 2
(cid:1)
Effect size
03 51
d sub,acc (cid:1)
md=0.264
m=0.264 mo=0.258
11.3%
0.4%
0.2 0.0 0.2 0.4 0.6 0.8
(cid:1)
0.004 531
Fig. 5 Results of the Bayesian inference of the acceptance of the virtual agents in EX and EXIM
configurations. The first two rows show the posterior distributions of the mean µ, scale τ, and normality
ν (in log scale) of the latent t distribution of each group. On the left and center of the last row are
the distributions of difference between the means and scales of the two groups, and on the right, the
distribution of the effect size d . Mean (m), median (md), mode (mo), and the limits of the 95% HDI
sub
areannotatedinthedistributions.Dashedverticallinesindicatethenullvalue(µ µ =0)inthe

## Exim Ex

−
distribution of the difference between means and the ROPE in the effect size distribution together with
the percentages of the distribution below, between and above the values associated with the ROPE and
the null value.

<!-- Page 30 -->

7
1.5 2.0 2.5 3.0 3.5 4.0 4.5
0.3
8.2
6.2
4.2

### Item 1

Thresholds
sdlohserht
fo
naeM
(cid:1)
5 0 5 10
5.4
5.3
5.2
5.1

### Item 2

Thresholds
sdlohserht
fo
naeM
.4 6.6
(cid:1)
5 0 5 10
0.5
0.4
0.3
0.2

### Item 3

Thresholds
sdlohserht
fo
naeM
.4 6.7
(cid:1)
5 0 5 10
4
3
2
1

### Item 4

Thresholds
sdlohserht
fo
naeM
8 6.4
(cid:1)
4
(cid:1)
2 0 2 4 6 8
4
3
2
1

### Item 5

Thresholds
sdlohserht
fo
naeM
2.5 5.6
(cid:1)
5 0 5 10
5
4
3
2

### Item 6

Thresholds
sdlohserht
fo
naeM
3. 6.4
Fig. 6 PosteriordistributionsofeachitemthresholdsoftheLikertscalefortheacceptanceofthevirtual
agents. Dashed lines indicate the means of the thresholds estimations.

<!-- Page 31 -->

8

### Item 1, Group EX

Ordinal responses
)pseR(p
4.0
0.0
1 2 3 4 5

### Item 2, Group EX

Ordinal responses
)pseR(p
4.0
0.0
1 2 3 4 5

### Item 3, Group EX

Ordinal responses
)pseR(p
4.0
0.0
1 2 3 4 5

### Item 4, Group EX

Ordinal responses
)pseR(p
4.0
0.0
1 2* 3 4 5

### Item 5, Group EX

Ordinal responses
)pseR(p
4.0
0.0
1 2 3 4 5

### Item 6, Group EX

Ordinal responses
)pseR(p
4.0
0.0
Item 1, Group EXIM
Ordinal responses
1 2 3 4 5
)pseR(p
4.0
0.0
1* 2* 3 4 5
Item 2, Group EXIM
Ordinal responses
)pseR(p
4.0
0.0
1* 2* 3 4 5
Item 3, Group EXIM
Ordinal responses
)pseR(p
4.0
0.0
1* 2 3 4 5
Item 4, Group EXIM
Ordinal responses
)pseR(p
4.0
0.0
1 2* 3 4 5
Item 5, Group EXIM
Ordinal responses
)pseR(p
4.0
0.0
1* 2 3* 4 5
Item 6, Group EXIM
Ordinal responses
)pseR(p
4.0
0.0
1 2 3 4 5
Fig. 7 Acceptance data histograms superimposed with estimated probabilities to check model adequacy.
Each blue dot indicates the estimated median and the vertical line represents the 95% HDI. Levels that
had extra answers added are marked with an asterisk (*).

<!-- Page 32 -->

9
Mean EX Scale EX Normality EX
md=3.18 md 1.58 md=127
m=3.18 mo=3.18 m=1.6 mo=1.54 m=1.24 mo=1.41
2 7 1.0 2 0 4
2.0 2.5 3.0 3.5 4.0 4.5 0.5 1.0 1.5 2.0 2.5 3.0 0.0 0.5 1.0 1.5 2.0 2.5
µ τ log ν
soc,EX soc,EX 10 soc,EX
Mean EXIM Scale EXIM Normality EXIM
md=3.64 md=1.46 md=1.07
m=3.64 mo=3.67 m=1.46 mo=1.45 m=1.05 mo=1.43
31 12 08 07 0. 8
2.0 2.5 3.0 3.5 4.0 4.5 0.5 1.0 1.5 2.0 2.5 3.0 0.0 0.5 1.0 1.5 2.0
µ τ log ν
soc,EXIM soc,EXIM 10 soc,EXIM

### Difference between means

µ −µ soc,EXIM soc,EX (cid:1)
Difference between scales
md=0.459
m=0.463 mo=0.472
1.8% 98.2%
0.02 914
0.5 0.0 0.5 1.0 1.5
τ −τ soc,EXIM soc,EX (cid:1)
2.0
(cid:1)
mo=
1.0 0.0 0.5 1.0
(cid:1)
md= 0.116
m= 0.103
(cid:1)
0.138
(cid:1)
Effect size
07 454
d sub,soc (cid:1)
md=0.304
m=0.304 mo=0.318
7.8%
0.3%
0.2 0.2 0.4 0.6 0.8
(cid:1)
0.0 75
Fig. 8 Results of the Bayesian inference of the sociability of the virtual agents in EX and EXIM configurations. The first two rows show the posterior distributions of the mean µ, scale τ, and normality ν (in
log scale) of the latent t distribution of each group. On the left and center of the last row are the distributions of difference between the means and scales of the two groups, and on the right, the distribution
oftheeffectsized .Mean(m),median(md),mode(mo),andthelimitsofthe95%HDIareannotated
sub
inthedistributions.Dashedverticallinesindicatethenullvalue(µ µ =0)inthedistributionof

## Exim Ex

−
the difference between means and the ROPE in the effect size distribution together with the percentages
of the distribution below, between and above the values associated with the ROPE and the null value.

<!-- Page 33 -->

10
1.5 2.0 2.5 3.0 3.5 4.0 4.5
1.3
9.2
7.2
5.2

### Item 1

Thresholds
sdlohserht
fo
naeM
0 2 4 6 8 10
0.5
5.4
0.4
5.3
0.3

### Item 2

Thresholds
sdlohserht
fo
naeM
5.9
−2 0 2 4 6 8
5.3
0.3
5.2
0.2
5.1
0.1

### Item 3

Thresholds
sdlohserht
fo
naeM
5.3
0 2 4 6 8 10
0.5
5.4
0.4
5.3
0.3

### Item 4

Thresholds
sdlohserht
fo
naeM
6.5
−4 −2 0 2 4 6 8
0.4
5.3
0.3
5.2

### Item 5

Thresholds
sdlohserht
fo
naeM
3.5 5.7
Fig. 9 Posterior distributions of each item thresholds of the Likert scale for the sociability of the virtual
agents. Dashed lines indicate the means of the thresholds estimations.

<!-- Page 34 -->

11

### Item 1, Group EX

Ordinal responses
)pseR(p
6.0
3.0
0.0
1 2 3 4 5

### Item 2, Group EX

Ordinal responses
)pseR(p
6.0
3.0
0.0
1 2 3 4 5

### Item 3, Group EX

Ordinal responses
)pseR(p
6.0
3.0
0.0
1 2 3 4 5

### Item 4, Group EX

Ordinal responses
)pseR(p
6.0
3.0
0.0
1 2 3 4 5

### Item 5, Group EX

Ordinal responses
)pseR(p
6.0
3.0
0.0
Item 1, Group EXIM
Ordinal responses
1 2 3 4 5
)pseR(p
6.0
3.0
0.0
1* 2 3 4 5
Item 2, Group EXIM
Ordinal responses
)pseR(p
6.0
3.0
0.0
1 2 3 4 5
Item 3, Group EXIM
Ordinal responses
)pseR(p
6.0
3.0
0.0
1 2 3 4 5
Item 4, Group EXIM
Ordinal responses
)pseR(p
6.0
3.0
0.0
1 2 3 4 5
Item 5, Group EXIM
Ordinal responses
)pseR(p
6.0
3.0
0.0
1 2 3 4 5
Fig. 10 Sociability data histograms superimposed to estimated probabilities to check model adequacy.
Each blue dot indicates the estimated median and the vertical line the 95% HDI. Levels that had extra
answers added are marked with an asterisk (*).

<!-- Page 35 -->

12
Mean EX Scale EX Normality EX
md=3.22 md=1.42 md=125
m=3.22 mo=3.25 m=1.43 mo=1.44 m=1.21 mo=1.41
27 72 093 95 02 2
2.0 2.5 3.0 3.5 4.0 4.5 0.5 1.0 1.5 2.0 2.5 0.0 0.5 1.0 1.5 2.0 2.5
µ τ log ν
tra,EX tra,EX 10 tra,EX
Mean EXIM Scale EXIM Normality EXIM
md=3.68 md=1.29 md=108
m=3.68 mo=3.69 m=1.29 mo=1.27 m=1.05 mo=1.28
3 16 07 84 0 9
2.0 2.5 3.0 3.5 4.0 4.5 0.5 1.0 1.5 2.0 2.5 0.0 0.5 1.0 1.5 2.0
µ τ log ν
tra,EXIM tra,EXIM 10 tra,EXIM
Difference between means Difference between scales
md=0.452
m=0.459 mo=0.451
1.8% 98.2%
0.01 12
0.0 0.5 1.0 1.5
µ −µ τ −τ tra,EXIM tra,EX tra,EXIM tra,EX (cid:1)
1.5
(cid:1)
mo=
0.5 0.5 1.0 1.5
(cid:1)
md=
0.121 (cid:1)
0.128
m=
(cid:1)
0.142
(cid:1)
Effect size
0.7 429
d sub,tra (cid:1)
md=0.337
m=0.339 mo=0.328
6.8%
0.3% 9
0.0 56
0.2 0.2 0.4 0.6 0.8 1.0
Fig. 11 Results of the Bayesian inference of the transparency of the virtual agents in EX and EXIM
configurations. The first two rows show the posterior distributions of the mean µ, scale τ, and normality
ν (in log scale) of the latent t distribution of each group. On the left and center of the last row are
the distributions of difference between the means and scales of the two groups, and on the right, the
distribution of the effect size d . Mean (m), median (md), mode (mo), and the limits of the 95% HDI
sub
areannotatedinthedistributions.Dashedverticallinesindicatethenullvalue(µ µ =0)inthe

## Exim Ex

−
distribution of the difference between means and the ROPE in the effect size distribution together with
the percentages of the distribution below, between and above the values associated with the ROPE and
the null value.

<!-- Page 36 -->

13
1.5 2.0 2.5 3.0 3.5 4.0 4.5
1.3
0.3
9.2
8.2
7.2
6.2
5.2

### Item 1

Thresholds
sdlohserht
fo
naeM
0 2 4 6 8 10
5.5
0.5
5.4
0.4
5.3

### Item 2

Thresholds
sdlohserht
fo
naeM
5.9
−4 −2 0 2 4 6 8
0.4
5.3
0.3
5.2
0.2

### Item 3

Thresholds
sdlohserht
fo
naeM
.2 5.7
−4 −2 0 2 4 6 8
5.3
0.3
5.2
0.2

### Item 4

Thresholds
sdlohserht
fo
naeM
.6 3.1 5.1
Fig. 12 Posterior distributions of each item thresholds of the Likert scale for the transparency of the
virtual agents. Dashed lines indicate the means of the thresholds estimations.

<!-- Page 37 -->

14

### Item 1, Group EX

Ordinal responses
)pseR(p
6.0
4.0
2.0
0.0
1* 2 3 4 5

### Item 2, Group EX

Ordinal responses
)pseR(p
6.0
4.0
2.0
0.0
1 2 3 4 5

### Item 3, Group EX

Ordinal responses
)pseR(p
6.0
4.0
2.0
0.0
1 2 3 4 5

### Item 4, Group EX

Ordinal responses
)pseR(p
6.0
4.0
2.0
0.0
Item 1, Group EXIM
Ordinal responses
1 2 3 4 5
)pseR(p
6.0
4.0
2.0
0.0
1 2 3 4 5
Item 2, Group EXIM
Ordinal responses
)pseR(p
6.0
4.0
2.0
0.0
1 2 3 4 5
Item 3, Group EXIM
Ordinal responses
)pseR(p
6.0
4.0
2.0
0.0
1* 2 3 4 5
Item 4, Group EXIM
Ordinal responses
)pseR(p
6.0
4.0
2.0
0.0
1 2 3 4 5
Fig. 13 Transparencydatahistogramssuperimposedtoestimatedprobabilitiestocheckmodeladequacy.
Each blue dot indicates the estimated median and the vertical line the 95% HDI. Levels that had extra
answers added are marked with an asterisk (*).

<!-- Page 38 -->

15
Mean EX Scale EX Normality EX
md=3.07 md=1.97
m=3.08 mo=3.07 m=1.99 mo=1.96

## I

2 9 1 77
2.0 2.5 3.0 3.5 4.0 4.5 0 1 2 3 4 5
µ τ log ν
eff,EX eff,EX 10 eff,EX
(cid:1)
md=128
m=1.22 mo=1.44
0
0.5 0.5 1.0 1.5 2.0 2.5
Mean EXIM Scale EXIM Normality EXIM
md=3.33 md=1.29 md=0.96
m=3.33 mo=3.31 m=1.29 mo=1.32 m=098m1o=0533

## 9 I

27 89 0.7 86 0.0 4
2.0 2.5 3.0 3.5 4.0 4.5 0 1 2 3 4 5 0.0 0.5 1.0 1.5 2.0 2.5
µ τ log ν
eff,EXIM eff,EXIM 10 eff,EXIM

### Difference between means

µ −µ eff,EXIM eff,EX (cid:1)
md=0.253
m=0.256 mo=0.216
17.4%8 %
1.0 0.0 0.5 1.0 1.5
(cid:1)
Difference between scales
02 828
τ −τ eff,EXIM eff,EX (cid:1)
2
(cid:1)
mo=
1 0 1
(cid:1)
md=
0.662 (cid:1)
0.68
m=
(cid:1)
0.706
(cid:1)
Effect size
1 013
d sub,eff (cid:1)
md=0.153
m=0.155 mo=0.132
31.
6% %
0.5 0.0 0.5
(cid:1)
0 493
Fig. 14 Results of the Bayesian inference of the perceived efficiency of theinteractions inEX and EXIM
configurations. The first two rows show the posterior distributions of the mean µ, scale τ, and normality
ν (in log scale) of the latent t distribution of each group. On the left and center of the last row are
the distributions of difference between the means and scales of the two groups, and on the right, the
distribution of the effect size d . Mean (m), median (md), mode (mo), and the limits of the 95% HDI
sub
areannotatedinthedistributions.Dashedverticallinesindicatethenullvalue(µ µ =0)inthe

## Exim Ex

−
distribution of the difference between means and the ROPE in the effect size distribution together with
the percentages of the distribution below, between and above the values associated with the ROPE and
the null value.

<!-- Page 39 -->

16
1.5 2.0 2.5 3.0 3.5 4.0 4.5
1.3
0.3
9.2
8.2
7.2
6.2
5.2

### Item 1

Thresholds
sdlohserht
fo
naeM
−4 −2 0 2 4 6 8
5.3
0.3
5.2
0.2
5.1
0.1

### Item 2

Thresholds
sdlohserht
fo
naeM
.5 4.7
−6 −4 −2 0 2 4 6
5.2
0.2
5.1
0.1
5.0
0.0

### Item 3

Thresholds
sdlohserht
fo
naeM
0.8 1.6 3.6
−6 −4 −2 0 2 4 6
5.3
0.3
5.2
0.2
5.1

### Item 4

Thresholds
sdlohserht
fo
naeM
2.3 2.9 4.5
Fig. 15 Posterior distributions of each item thresholds of the Likert scale for the perceived efficiency of
the interactions. Dashed lines indicate the means of the thresholds estimations.

<!-- Page 40 -->

17

### Item 1, Group EX

Ordinal responses
)pseR(p
6.0
4.0
2.0
0.0
1 2 3 4 5

### Item 2, Group EX

Ordinal responses
)pseR(p
6.0
4.0
2.0
0.0
1 2 3 4 5

### Item 3, Group EX

Ordinal responses
)pseR(p
6.0
4.0
2.0
0.0
1 2* 3 4 5

### Item 4, Group EX

Ordinal responses
)pseR(p
6.0
4.0
2.0
0.0
Item 1, Group EXIM
Ordinal responses
1 2 3 4 5
)pseR(p
6.0
4.0
2.0
0.0
1 2 3 4 5
Item 2, Group EXIM
Ordinal responses
)pseR(p
6.0
4.0
2.0
0.0
1 2 3 4 5
Item 3, Group EXIM
Ordinal responses
)pseR(p
6.0
4.0
2.0
0.0
1* 2 3 4 5
Item 4, Group EXIM
Ordinal responses
)pseR(p
6.0
4.0
2.0
0.0
1 2 3 4 5
Fig. 16 Perceived efficiency data histograms superimposed to estimated probabilities to check model
adequacy. Each blue dot indicates the estimated median and the vertical line the 95% HDI. Levels that
had extra answers added are marked with an asterisk (*).

<!-- Page 41 -->

18
results for the comparison, considering an one- [6] Kruschke JK (2015) Doing Bayesian Data
tailedalternativehypothesissayingthatthemean Analysis:ATutorialwithR,JAGS,andStan.
(or median, for the Wilcoxon signed-rank test) is Academic Press / Elsevier, Burlington, MA
greater than zero. [7] Kruschke JK, Liddell TM (2018) The
For the t-test, the function t.test5 from Bayesian New Statistics: Hypothesis testing,
package stats (version 4.0.4) was used, and estimation, meta-analysis, and power analythe Wilcoxon signed-rank test was conducted sisfromaBayesianperspective.Psychonomic
using wilcox.exact6 function from package Bulletin & Review 25(1):178–206. https://
exactRankTests (version 0.8.32). The procedure doi.org/10.3758/s13423-016-1221-4
to calculate the Wilcoxon signed-rank test statis- [8] Liddell TM, Kruschke JK (2018) Analyzing
tics involves ordering the absolute values of the ordinaldatawithmetricmodels:Whatcould
observations and comparing them to the null possibly go wrong? Journal of Experimenvalue, indicating if they are below or above it [3]. tal Social Psychology 79(August):328–348.
Whentheobservationsareequaltothenullvalue, https://doi.org/10.1016/j.jesp.2018.08.009
theapproachappliedbythefunctionusedtocon- [9] LikertR(1932)ATechniquefortheMeasureduct the test is to discard them. The number of ment of Attitudes. Archives of Psychology
null values in the sample, which were therefore [10] WagenmakersEJ,MarsmanM,JamilT,etal
discarded when computing the test statistics, is (2018) Bayesian inference for psychology.
indicated along with the results. Part I: Theoretical advantages and practical
Table 1 shows the results for the subjective ramifications. Psychonomic Bulletin & Remeasures. view 25(1):35–57. https://doi.org/10.3758/
s13423-017-1343-3

### References

[1] Carifio J, Perla R (2008) Resolving the
50-year debate around using and misusing Likert scales. Medical Education
42(12):1150–1152. https://doi.org/10.1111/j.
1365-2923.2008.03172.x
[2] Harpe SE (2015) How to analyze Likert and
other rating scale data. Currents in Pharmacy Teaching and Learning 7(6):836–850.
https://doi.org/10.1016/j.cptl.2015.08.001
[3] Hollander M, Wolfe DA, Chicken E (2014)
Nonparametric Statistical Methods. John
Wiley & Sons, Inc.
[4] Kelter R (2020) Bayesian alternatives to null
hypothesis significance testing in biomedical research: A non-technical introduction to
Bayesian inference with JASP. BMC MedicalResearchMethodology20(1).https://doi.
org/10.1186/s12874-020-00980-6
[5] Kloke J, Mckean JW (2015) The R Series
StatisticsNonparametricStatisticalMethods

### UsingR.CRCPress-Taylor&FrancisGroup

5https://stat.ethz.ch/R-manual/R-devel/library/stats/
html/t.test.html
6https://www.rdocumentation.org/packages/
exactRankTests/versions/0.8-32/topics/wilcox.exact

<!-- Page 42 -->

19
Table 1 Resultsofnullhypothesissignificancetestsforthedifferenceintimeandnumberoferrors(with
and without outliers) between the two communication configurations.
Normality Test result
t-test
Time Shapiro-Wilk: p-value=0.9926>0.05 Teststatistics: 0.13543
−
p-value:0.5533
Wilcoxonsigned-ranktest

### Shapiro-Wilk:


### Number of errors

Teststatistics:116
p-value=1.482
×
10− 5<0.05 p-value:0.6348
Numberofnullvalues:4
t-test

### Number of errors

Shapiro-Wilk: p-value=0.4394>0.05 Teststatistics: 0.5547
without outliers −
p-value:0.7078
Table 2 Results of null hypothesis significance tests for the difference between the communication
configurations in the mean points in the scales assessing each subjective measure.
Wilcoxon signed-rank test

### Teststatistics:192

Acceptance of the virtual agent p-value:0.05121
Numberofnullvalues:3

### Teststatistics:201.5

Sociability of the virtual agent p-value:0.02642
Numberofnullvalues:3

### Teststatistics:188.5

Transparency of the virtual agent p-value:0.004566
Numberofnullvalues:5

### Teststatistics:138.5

Perceived efficiency of the interaction p-value:0.1091
Numberofnullvalues:6

## Tables

**Table (Page 8):**

|  |
|---|
|  |


**Table (Page 10):**

| standard deviation mean |
|---|
| NORMAL |


**Table (Page 10):**

| mean |
|---|
| EXPONENTIAL |


**Table (Page 12):**

| mean |
|---|
| EXPONENTIAL |


**Table (Page 15):**

| HD |  |  |  |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |


**Table (Page 15):**

|  |  |  |  |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |


**Table (Page 15):**

|  |  |  |  |  |
|---|---|---|---|---|
|  |  |  |  | 9 |
|  |  |  |  |  |
|  |  |  |  |  |


**Table (Page 15):**

|  |  |
|---|---|
|  |  |


**Table (Page 15):**

|  |  |  |  | 5 | m |
|---|---|---|---|---|---|
|  |  |  |  |  |  |
|  |  |  |  |  |  |


**Table (Page 15):**

|  |  |  |  |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |


**Table (Page 15):**

|  |  |
|---|---|
|  |  |


**Table (Page 26):**

|  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |


**Table (Page 26):**

|  |  |  |  | m |  |
|---|---|---|---|---|---|
|  |  |  |  |  |  |


**Table (Page 26):**

|  |  |  |  |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |


**Table (Page 26):**

|  |  |  |  |  |  | 0 |
|---|---|---|---|---|---|---|
|  |  |  |  |  | 2 |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  | % |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |


**Table (Page 26):**

|  |  |  |
|---|---|---|
|  |  |  |
|  |  |  |


**Table (Page 27):**

|  |  |
|---|---|
|  |  |


**Table (Page 31):**

|  |  |
|---|---|
|  |  |


**Table (Page 31):**

|  |  |
|---|---|
|  |  |


**Table (Page 31):**

|  |  |
|---|---|
|  |  |


**Table (Page 31):**

|  |  |
|---|---|
|  |  |


**Table (Page 31):**

|  |  |  |
|---|---|---|
|  |  |  |
|  |  |  |


**Table (Page 31):**

|  |  |
|---|---|
|  |  |


**Table (Page 31):**

|  |  |
|---|---|
|  |  |


**Table (Page 34):**

|  |  |
|---|---|
|  |  |


**Table (Page 34):**

|  |  |
|---|---|
|  |  |


**Table (Page 34):**

|  |  |  |  |  |
|---|---|---|---|---|
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |


**Table (Page 34):**

|  |  |  |  |  |
|---|---|---|---|---|
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |


**Table (Page 34):**

|  |  |  |  |  |
|---|---|---|---|---|
|  |  |  |  |  |
|  |  |  |  |  |


**Table (Page 34):**

|  |  |  |  |  |
|---|---|---|---|---|
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |


**Table (Page 34):**

|  |  |  |  |  |
|---|---|---|---|---|
|  |  |  |  |  |
|  |  |  |  |  |


**Table (Page 34):**

|  |  |  |  |  |
|---|---|---|---|---|
|  |  |  |  |  |
|  |  |  |  |  |


**Table (Page 34):**

|  |  |  |  |  |
|---|---|---|---|---|
|  |  |  |  |  |
|  |  |  |  |  |


**Table (Page 34):**

|  |  |  |  |  |
|---|---|---|---|---|
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |


**Table (Page 37):**

|  |  |  |  |  |
|---|---|---|---|---|
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |


**Table (Page 37):**

|  |  |  |  |  |
|---|---|---|---|---|
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |


**Table (Page 37):**

|  |  |  |  |  |
|---|---|---|---|---|
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |


**Table (Page 37):**

|  |  |  |  |  |
|---|---|---|---|---|
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |


**Table (Page 37):**

|  |  |  |  |  |
|---|---|---|---|---|
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |


**Table (Page 37):**

|  |  |  |  |  |
|---|---|---|---|---|
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |


**Table (Page 37):**

|  |  |  |  |  |
|---|---|---|---|---|
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |


**Table (Page 37):**

|  |  |  |  |  |
|---|---|---|---|---|
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |


**Table (Page 40):**

|  |  |  |  |  |
|---|---|---|---|---|
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |


**Table (Page 40):**

|  |  |  |  |  |
|---|---|---|---|---|
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |


**Table (Page 40):**

|  |  |  |  |  |
|---|---|---|---|---|
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |


**Table (Page 40):**

|  |  |  |  |  |
|---|---|---|---|---|
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |


**Table (Page 40):**

|  |  |  |  |  |
|---|---|---|---|---|
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |


**Table (Page 40):**

|  |  |  |  |  |
|---|---|---|---|---|
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |


**Table (Page 40):**

|  |  |  |  |  |
|---|---|---|---|---|
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |


**Table (Page 40):**

|  |  |  |  |  |
|---|---|---|---|---|
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
