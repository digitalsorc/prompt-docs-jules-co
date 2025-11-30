---
title: "MM REACT Multimodal Reasoning"
original_file: "./MM_REACT_Multimodal_Reasoning.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["prompt-engineering", "llm", "rag", "chain-of-thought", "react"]
keywords: ["image", "page", "chatgpt", "you", "table", "what", "text", "total", "step", "react"]
summary: "<!-- Page 1 -->

MM-REACT : Prompting ChatGPT for Multimodal Reasoning and Action
ZhengyuanYang∗,LinjieLi∗,JianfengWang∗,KevinLin∗,EhsanAzarnasab∗,FaisalAhmed∗,
ZichengLiu,CeLiu,MichaelZeng,LijuanWang♠

### MicrosoftAzureAI

{zhengyang,lindsey.li,jianfw,keli,ehazar,fiahmed,zliu,ce.liu,nzeng,lijuanw}@microsoft.com
Visual Math and Text Reasoning Visual-Conditioned Joke/Meme Spatial/Coordinate Understanding
What is “a” in the first equation? What is the relative position of the frisbee and the man?"
related_documents: []
---

# MM REACT Multimodal Reasoning

<!-- Page 1 -->

MM-REACT : Prompting ChatGPT for Multimodal Reasoning and Action
ZhengyuanYang∗,LinjieLi∗,JianfengWang∗,KevinLin∗,EhsanAzarnasab∗,FaisalAhmed∗,
ZichengLiu,CeLiu,MichaelZeng,LijuanWang♠

### MicrosoftAzureAI

{zhengyang,lindsey.li,jianfw,keli,ehazar,fiahmed,zliu,ce.liu,nzeng,lijuanw}@microsoft.com
Visual Math and Text Reasoning Visual-Conditioned Joke/Meme Spatial/Coordinate Understanding
What is “a” in the first equation? What is funny about it? Where is the frisbee?
What is y in the last equation? What is the relative position of the frisbee and the man?
The value of “a” in the first equation “5 The humor in the comic may come from The frisbee is located at coordinates
+ a = 7” is 2. the situation, the characters, or the (63,119,133,177).
dialogue. The person is feeling unwell
The value of “y” in the last equation and is asked if they are pregnant or have The frisbee is located above the man in
“34 + y = 39” is 5. the coronavirus, which is a current and the image. The man is falling on the
relevant topic. The humor may come ground while the frisbee is in the air. The
from the absurdity of the situation or the frisbee is also closer to the top of the
unexpectedness of the question. image than the man..
Visual Planning and Prediction Multi-Image Reasoning Multi-Hop Document Understanding
What should I do after kneading the dough, before dividing it How much in total did I spend on travel? Excluding the regular cab, what is the average total fueling
into pieces? For how long? How much in total did I pay for taxes? cost?
After kneading the dough, you should You spent $1299.90 on airfare and $43.83 The average total fueling cost excluding
put it in a warm place before dividing it on an Uber ride for a total of $1343.73 on the Ford F150 (Regular Cab) is $76.55. This
into pieces, according to the recipe in travel. is calculated by taking the sum of the total
the image. fueling cost of Toyota RAV4 and Honda
You paid $323.23 in total for taxes. This Civic and dividing it by 2. ($82.56 +
You should put the dough in a warm includes $321.90 for taxes and fees for $70.55) / 2 = $76.55.
place for 1 hour. the flight purchase and $1.33 for sales
tax for the Windmill Family Restaurant.
Open-World Concept Understanding Video Summarization/Event Localization
What is the brand of these drink? Which Who are the celebrities in this image? Is it safe to eat this mushroom? Can you breakdown this video tutorial to step-by-step
one is unsweetened? instructions, with start and end time?
The brand of these Keira Knightley and Morel mushrooms are Here's a step-by-step breakdown of the
drinks is “BETTER THAN Natalie Portman are generally considered safe tutorial with start and end time.
MILK”. The unsweetened the celebrities in this to eat when properly
one is “BETTER THAN image. cooked.
MILK organic OAT

## Drink”.

…Add Lettuce Add Tomato Add Bacon …
Figure1. MM-REACTallocatesspecializedvisionexpertswithChatGPTtosolvechallengingvisualunderstandingtasksthroughmultimodalreasoningandaction. Forexample,thesystemcouldassociateinformationfrommultipleuploadedreceiptsandcalculatethetotal
travelcost(“Multi-ImageReasoning”).WeonlyhighlightkeyinformationhereandpostponefullMM-REACTresponsestoFigures4-14.
Abstract associate,andprocessmultimodalinformation,therebyfacilitatingthesynergeticcombinationofChatGPTandvarious vision experts. Zero-shot experiments demonstrate

### Wepropose MM-REACT, asystemparadigmthatinte-

MM-REACT’seffectivenessinaddressingthespecifiedcagrates ChatGPT with a pool of vision experts to achieve
pabilities of interests and its wide application in different
multimodal reasoning and action. In this paper, we define
scenariosthatrequireadvancedvisualunderstanding.Furand explore a comprehensive list of advanced vision tasks
thermore, we discuss and compare MM-REACT’s system
thatareintriguingtosolve,butmayexceedthecapabilities
paradigm with an alternative approach that extends lanof existing vision and vision-language models. To achieve
guage models for multimodal scenarios through joint finesuchadvancedvisualintelligence,MM-REACTintroduces
tuning. Code,demo,video,andvisualizationareavailable
atextualpromptdesignthatcanrepresenttextdescriptions,
athttps://multimodal-react.github.io/.
textualized spatial coordinates, and aligned file names for
dense visual signals such as images and videos. MM-
REACT’spromptdesignallowslanguagemodelstoaccept, ∗EqualContribution ♠ProjectLead
1
3202
raM
02
]VC.sc[
1v18311.3032:viXra

<!-- Page 2 -->


## Introduction capability,inputargumenttype,andoutputtype,alongwith

afewin-contextexamplesforeachexpert. Additionally, a
Recentyearshaveseensignificantadvancementforcomspecialwatchwordisinstructedsuchthatwecanuseregex
putervision,thankstoimprovednetworkarchitecture[4,9,
expressionmatchingtoinvoketheexpertaccordingly.
12,28],large-scalemodeltraining[8,29,35],andotherfac-
We show MM-REACT’s representative visual undertors. However, different vision problems typically require
standing capabilities in Figure 1. For example, MM-
differentmodels,whichoftenrequiremanualselectionand
REACT could associate information from multiple upcompositionofindividualmodelsforeachusecase.Forexloaded receipts and calculate the total travel cost (“Multiample,whendeterminingifanimagecontains“people”,we
ImageReasoning”), recognizeandanswerquestionsabout
maychoosetheimagetaggingmodel[7,16,19]andcheckif
the “morel mushrooms” (“Open-World Concept Underthepredictedtaglistcontains“people”. If“people”exists,
standing”), and condense a long video into representative
wemayselectthecelebritymodel[20]tofurtherunderstand
thumbnails (“Video Summarization and Event Localizawhetheracelebrityappearsandwhohe/sheis.
tion”).Thesevisualintelligencefeaturesaresimilartothose
One research direction is to combine the vision and
foundinrecentmodels,suchasmultimodalGPT-4[23]and
language modules as one end-to-end model, such as
PaLM-E [10], but achieved via prompting instead of addi-
Flamingo [2], PaLM-E [10], to provide a dialogue-based
tional multimodal training. The MM-REACT system may
experiencetotheenduser. Thatis,theusercanusenatural
provide extra flexibility in module upgrades, and may be
languagetointeractwiththemodelaroundtheimageconeffectiveincertainvisualunderstandingtasksbybetterutitent. Thevisionmoduleencodesvisionsignalsintospecial
lizingexistingspecializedvisionexperts, suchascelebrity
text tokens or features that the language module can unrecognitionanddensecaptioning.
derstand, enablingthesystemtoutilizethelanguagemoduleforunderstandinguserqueriesandprovidingresponses.

## RelatedWork

However, these joint finetuning approaches require a large
amount of computing resources and annotated data to en-

### LLMs Prompting Methods. Large language models

ablespecificcapabilities. Inthiswork,weaimtocombine
(LLMs)[3,6]demonstrateastrongchain-of-thought(CoT)
existingindividualvisionmodelswiththelanguagemodel
capability [17,31] that could break down complex probinamoreflexiblemannertotacklecomplicatedvisualunlems into solvable intermediate steps. On the other hand,
derstandingproblems,e.g.,theonesillustratedinFigure1.
research[1,15,22]showsthatLLMs, whenequippedwith

### Largelanguagemodels(LLMs)[3,6],suchasChatGPT,

a range of external NLP tools, can effectively serve as
haveshownimpressivedialoguecapabilitywithtextasboth
action planners to select and utilize tools for probleminputandoutput. RecentNLPresearch[11,24,26,34](e.g.,
solving, such as using search or mathematical tools to ad-
REACT [34])demonstratestheeffectivenessofintegrating
dressknowledgeormathproblems.
externalNLPtools,suchassearchenginesandmathcalcu-

### Nevertheless,LLMsforreasoning[17,31]andLLMsfor

lators, withLLMsbyproperinstruction. Specifically, RE-
action [1,15,22] , when used independently, fail to solve

### ACT[34]promptsanLLMtogeneratereasoningtextsthat

complex tasks that require breaking down the problem via
breakdowncomplexproblemsintointermediatesteps,and
reasoning and solving sub-steps via planned actions. ReactiontextsthatallocateNLPtoolsforsolvingthesesteps.
centstudies[11,24,26,34]haveattemptedtomergetheac-
One example is that the LLM can suggest a text query to
tion and reasoning phases to enhance LLMs’ capabilities
amodernsearchenginetograbthelatestinternetinformain solving complicated tasks that require advanced plantion, andreturntheuserwiththeinformationthatisnotin
thepre-trainingcorpus. Inspiredbytheefficacyofreasonningandreasoning. Onerepresentativework,REACT[34],
treatsreasoningtextgenerationasanexecutableactionand
ing and acting with LLMs and NLP tools, we explore the
achievesthesynergeticcombinationofreasoningandaction
integrationofvisionexperttoolswithLLMs.
forNLPtasks. Inthiswork,weexplorehowtoextendsuch

### Tothisend,wepresentMM-REACT,asystemparadigm

intriguing properties into multimodal scenarios by modelthat composes numerous vision experts with ChatGPT for
ingthoughtandinvokingvisiontoolsasexecutableactions.
multimodal reasoning and action. To enable images and
videosasinputs,weusetheirfilepathastheinputtoChat- Vision+LLMs. Our MM-REACT is related to the pre-
GPT. The file path functions as a placeholder, allowing vious studies that extend language models to understand
ChatGPT to treat it as a black box. Whenever a specific visual inputs. The representative framework adds a viproperty such as celebrity names or box coordinates is re- sion module to project visual inputs into representations
quired, ChatGPT is expected to seek help from a specific that the language model can understand. These represenvisionexperttoidentifythedesiredinformation. Toinject tations can be either discrete text words [13,30,33,36]
theknowledgeofvisionexperts’usagesintoChatGPT,we or continuous features projected into the textual feature
add instructions to ChatGPT prompts about each expert’s space [2,10,14,18,27]. Recent vision-language studies
2

<!-- Page 3 -->

wait for user input
image caption
image as <path>
image tagging
dense caption output as text
ChatGPTresponds
observation
celebrity
receipt

## Ocr

Bing search
yes no
parse <model> and <path>
vision experts respond to user execute the action
…
Thought This is an image.
Assistant, what objects do you see in this

### Action request

image? <ImagePath>
Action execution Invoke vision experts over <ImagePath>

### Observation Image Captioning

This is an image (694 x 720) with description a basketball player in a
yellow jersey with a ball in his hand.

### Dense Captioning

thought & action request? L a i s c t lo o s f e o u b p je o c f t a d e b s a c s r k ip e t t i b o a n ll s , ( x a 1 n , d y 1 th , e x i 2 r , l y o 2 c ) a t = io ( n 6 s 3 i , n 5 3 th 5 i , s 1 i 9 m 0 a , g 6 e 6 : 3)
a basketball player in a yellow jersey (x1, y1, x2, y2) = (55, 19, 502, 700)
…

### Object Tagger


### List of object tags seen in this image:

sport, athletic game, basketball, person, sports uniform, ball,
sportswear, basketball player, basketball moves, sports equipment,
basketball court …

### Face Detection

Detected faces, and their location in this image:
man (x1, y1, x2, y2) = (365, 278, 439, 352)
man (x1, y1, x2, y2) = (548, 308, 620, 380)
Figure2. FlowchartofMM-REACTforenhancedvisualunderstandingwithChatGPT.Theuserinputcanbeintheformoftext,images,
orvideos,withthelattertworepresentedasfilepathstrings.ChatGPTisinstructedtosayspecificwatchwordsinactionrequestifavision
expertisrequiredtointerpretthevisualinputs.Regularexpressionmatchingisappliedtoparsetheexpert’snameandthefilepath,which
arethenusedtocallthevisionexpert(actionexecution). Theexpert’soutput(observation)isserializedastextandcombinedwiththe
historytofurtheractivateChatGPT.Ifnoextraexpertsareneeded, MM-REACT wouldreturnthefinalresponsetotheuser. Theright
figureshowsasingle-roundvisionexpertexecution,whichisthecomponentthatconstructsthefullexecutionflowillustratedinFigure3.
explore the chain-of-thought capability [17,31] in multi- tives. Forinstance,theimagecaptioningexpertgeneratesa
modal settings. MM-CoT [37] finetunes on the reasoning natural description, the OCR expert extracts the scene text
chain annotated in the ScienceQA [21] dataset to achieve intheimage, thecelebrityrecognitionmodelidentifiesthe
the CoT capability in the science question answering task. celebritynames,andtheobjectdetectionmodelextractsthe
KOSMOS-1 [14] and PaLM-E [10] demonstrate the zero- salientobjectwithboundingboxlocations. Atpresent,one
shotmultimodalCoTcapabilitieswithlarge-scaletraining. may have to manually decide which vision experts to employforspecificusecases,andmanuallycomposethem.In-

### Multimodal Reasoning and Action. A key distinction

stead,ourtargetistoautomatethisprocessbasedontherebetween MM-REACT and prior vision+LLM studies disquirementspresentedbytheuserqueryinnaturallanguage.
cussed above is that MM-REACT leverages LLMs’ high-

### ChatGPTisanartificialintelligencechatbotwithtextas

level planning abilities to allocate various vision experts,
bothinputandoutput,withoutvisualunderstanding. Howrather than solely using LLMs for text generation condiever, ChatGPT exhibits strong instruct learning capability,
tioned on visual inputs. MM-REACT is closely related
which motivates us to instruct ChatGPT to properly deterto the recent concurrent work of Visual ChatGPT [32]
minewhichvisionexpertshouldbeinvokedandwhichimand ViperGPT [25]. In comparison, Visual ChatGPT [32]
ageshouldbeprocessed.
primarily focuses on image generation and editing, while
our MM-REACT mainly focuses on visual understanding. Figure 2 shows the flowchart of our MM-REACT sys-
ViperGPT[25]instructsLLMstogeneratePythoncodefor tem. Thetermsthoughtandactionrequestrefertothereaaone-roundqueryanswering.Incontrast,MM-REACTisa soning and action-oriented texts generated by ChatGPT to
multi-round, dialogue-based system that may integrate the breakdowntheproblemorinvokevisionexperts. ObservastrongQAmodelasoneofitsvisionexperts. tion refers to the vision expert’s responses after the action
executionrequestedintheactionrequesttext. Next,wedetaileachstepintheflowchartasfollows.

## MM-REACT Prompting


### UserInput


### ThegoalofMM-REACTistocomposenumerousvision

expertstoempowerChatGPTwithvisualunderstanding. A As ChatGPT only accepts texts as input, the first chalvisionexpertisacomputervisionmodelthattakesanimage lengeishowtoaccommodatenon-textinputs,suchasmulas input and interprets the content from different perspec- tiple images and videos. Since most vision experts accept
3

<!-- Page 4 -->

thefilepathorURL,weusethepathstringtoindicatenon- scribed with the model name, a general description of its
textinputs. Thefilepathitselfismeaninglessandisessen- capability, the input data format, and the output informatially a placeholder. Although no visual recognition task tion. Afterdescribingeachexpert,weaddafewin-context
can be performed directly with file paths, ChatGPT may dialogue examples to enhance the performance. With the
seek help from different vision experts to understand the injectedknowledge,ChatGPTcaneffectivelyselectoneor
imagecontentfromdifferentperspectives,e.g.,identifying multiplevisionexpertstounderstandtheimagesorvideos
thecelebritynamesofthedetectedperson.Byincludingthe fromdifferentperspectives.
provided file path in its text output, ChatGPT can indicate

### Extensibility

whichimageshouldbeprocessedbythevisionexpert.
OurschemeismotivatedbyREACT,whichinvokesdif-

### ChatGPTResponse

ferent tools in the NLP field. As only the text is involved,
Given the user’s input, ChatGPT is expected to provide no specific design is required to incorporate other modaltwokindsofresponses. Thefirstistoseekhelpfromvision ities. In this work, we extend MM-REACT to the vision
experts,whilethesecondistorespondtotheuserdirectly. domain. Thekeyistoreplacethenon-textmodalitywitha
A key challenge is to set up a protocol such that we know pathstring,enablingChatGPTtoaskspecificvisionexperts
whentoinvokethevisionexpert. InspiredbyREACT[34], torecognizethevisualcontent. Therefore,wecouldfurther
we instruct ChatGPT to respond with certain watchwords, extendMM-REACTtoothermodalities,suchasspeechand
such as “Assistant, what objects are there in the image? audio. Meanwhile, we can also easily incorporate more
<filepath>”,ifaspecificvisionexpertisrequired. Inour tools by formatting their outputs in a text format. While
implementation,weusethekeyword“Assistant,”todistin- ChatGPT serves as the primary LLM in our main impleguishwhetheravisionexpertisrequired. mentation,performancecouldbefurtherenhancedthrough
Tofurtherimprovetheperformance,weencourageChat- thesimpleupgradetoamorepowerfulLLM,suchasGPT-
GPT to show the thought (reasoning) process to highlight 4[23]discussedinSection4.5.
whyanexternaltoolisrequired. Itisalsoshowntobeben-

## Experiments

eficialinNLPstudies[34]toincorporatesuchreasoning.

### ExperimentSetup


### VisionExperts

GiventheactionrequestfromChatGPT,weusethereg-

### We implement MM-REACT based on the LangChain

codebase[5]andreferenceideasfromReAct[34]. Weacular expression matching to parse the expert name and the
cessChatGPTviatheAzure“gpt-3.5-turbo”APIthathasa
filepath,andinvoketheaction(visionexpertexecution).
tokenlengthlimitof4,096, andutilizevisionexpertspub-
Theexpert’soutputcanbeindifferentformsbutisstanlicly available via the Azure Cognitive Services APIs1, indardizedintothetextformatsuchthatChatGPTcanundercludingtheonesforimagecaptioning,imagetagging,dense
stand it. For certain experts, such as the captioning model
captioning, optical character recognition (OCR), and speorthecelebritymodel,itisstraightforwardtorepresentthe
cializedrecognitionmodelsforcelebrities,receipts,etc.We
outputastext. However,thestandardizationislessintuitive
further expand the toolset with customized tools for spaforothers. Forexample, thedetectionmodeloutputsalist
tial understanding and image editing, and tools from other
ofobjectnameswithboundingboxlocations. Inthiscase,
modalitiessuchasBingsearchandPALmath.
weconcatenatealltheboxes, eachofwhichisrepresented
as <object name, x1, y1, x2, y2>, where (x1,y1), (x2,y2) 4.2.MM-REACT’sFullExecutionFlow
arethecoordinatesofthetop-leftandbottom-rightcorners,
respectively. Anadditionaltextdescriptionisaddedtoex- Figure3providesanexampletoillustrateMM-REACT’s
plainthemeaningofthelastfournumericalvalues.Insome full execution flow. We highlight the exact order to call
cases, we find ChatGPT is capable of understanding these different models (i.e., executions) with numbered blue circoordinates,e.g.,identifyingwhichobjectisontheleft. cles. The executions, highlighted by bold underlined text,
Thetext-formedoutputfromvisionexpertscanbeinter- can be either a ChatGPT call (e.g., “ChatGPT:”) or the
pretedastheobservationresultingfromChatGPT’saction execution of one or multiple selected vision experts (e.g.,
ofinvokingthevisionexpert. Combiningobservationswith “ImageCaptioning”). We add a commentary text action
thechathistory,ChatGPTcanfurtherinvokeadditionalexexecutionindashedboxestohelpunderstandthevisionexpertsorreturnthefinalanswertotheuser. Weprovideexpertexecution.Theactionexecutionisnotanactualinputor
amplesoffullexecutionflowsinSection4.2andFigure3. output in the MM-REACT flow. ChatGPT executions can
beusedtogeneratethought(reasoning)andactiontextsthat
To inject the knowledge of various vision experts’ usages, we add both instructions and in-context examples in 1https://azure.microsoft.com/en-us/products/
the prefix when prompting ChatGPT. Each expert is de- cognitive-services/vision-services
4

<!-- Page 5 -->


### PaLM-E

3 Thought 2 ChatGPT: There are two
PaLM-E Ours faces detected in the image. Q: Where is <img1> in this scene <img2>? A:
Action request 2 Assistant, are there any celebrities A stove top with a pot on it.
in this image? <ImagePath> Image1 Image2
Image1 Image2 Image1 Image2 4 Action execution 2 Invoke Celebrity Recognition
Observation 2 Celebrity Recognition
This image contains celebrities

### Ours

List of celebrities, and their
location in this image:
Where is the coffee pot in the second image?

### Kobe Bryant

Convert image to <ImagePath> and
(x1,y1,x2,y2)=(365,278,439,352)
send to ChatGPT

### Paul Pierce The coffee pot is located in the kitchen

Q: Where is <img1> in this scene <img2>? A: (x1,y1,x2,y2)=(548,308,620,380) with a stove and cabinets. It is a silver

### Where is the coffee pot in the second image?

A stove top with a pot on it. 1 Thought 1 ChatGPT: This is an image. coffee pot on a stove and its location is
5 ChatGPT: This image contains two celebrities, at (242, 230) to (295, 299).

### Action request 1 Assistant, what objects do you see

The coffee pot is located in the kitchen Kobe Bryant and Paul Pierce. They are both
in this image? <ImagePath>
with a stove and cabinets. It is a silver basketball players.
coffee pot on a stove and its location is 2 Action execution 1 Invoke vision experts, including Multi-Image Relationships

### Image Captioning, Dense

at (242, 230) to (295, 299).
Captioning, Object Tagger, Face How many championship rings did the player
Detection. on the left win in his career?

### Multi-Image Relationships

Observation 1 Image Captioning

### PaLM-E

Assistant: This is an image (694 x 6 Thought 3 ChatGPT: This question
PaLM-E Ours 720) with description a basketball requires Bing Search Given <img>. Q: I am getting just two custom pizza
player in a yellow jersey with a ball in Action request 3 Assistant, Bing search how many for me and my friend. How much should I pay in
his hand. championship rings did Kobe total? A: Let's think step by step. 1st step: 2 custom

### Bryant win in his career?

pizzas. 2nd step: 2 x $9.99. 3rd step: $19.98.
Dense Captioning <ImagePath>.
List of object descriptions, and their 7 Action execution 3 Invoke Bing Search
locations in this image:
Observation 3 Bing Search Ours
a close up of a basketball
(x1,y1,x2,y2) = (63, 535, 190, 663) Assistant: Bryant, a shooting I am getting just two custom pizza
a basketball player in a yellow jersey guard, and O’Neal, a centre, for me and my friend. How much
(x1,y1,x2,y2) = (55, 19, 502, 700) meshed into a remarkably should I pay in total?
… effective combination, and, by the
time Bryant was 23, the Lakers had
Based on the information you provided,

### Object Tagger

won three consecutive NBA
Given <img>. Q: I am getting just I am getting just two custom pizza List of object tags seen in this image: you are ordering two custom pizzas.
championships. Kobe Bryant After
two custom pizza for me and my for me and my friend. How much sport, athletic game, basketball, … The price of each custom pizza is $9.99.
winning their third title in 2002,
friend. How much should I pay in should I pay in total? So, the total cost of two custom pizzas

### Bryant and the Lakers

total? A: Let's think step by step. Face Detection would be $9.99 x 2 = $19.98
encountered difficulties. Kobe
1st step: 2 custom pizzas. 2nd step: Based on the information you provided, Detected faces, and their location in

### Bryant has won a total of 5 rings in

2 x $9.99. 3rd step: $19.98. you are ordering two custom pizzas. this image:
20 seasons… Scene Text Reasoning

### The price of each custom pizza is $9.99. man

So, the total cost of two custom pizzas (x1,y1,x2,y2)=(365,278,439,352)
would be $9.99 x 2 = $19.98 man 8 ChatGPT: Kobe Bryant won 5 championship
(x1,y1,x2,y2)=(548,308,620,380) rings in his career.

### Scene Text Reasoning

Figure 3. An example of MM-REACT’s full execution flow. The blue circles with numbered indices indicate the order in which differentmodelsarecalled(i.e., theexecutions). Theexecutions, highlightedbyboldunderlinedtext, canbeeitheraChatGPTcall(e.g.,
“ChatGPT:”)orrunningoneormultipleselectedvisionexperts(e.g.,“ImageCaptioning”).Weaddacommentarytextactionexecution
indashedboxestohelpunderstandtheexpertexecution.EachChatGPTexecutiontakestheprecedingtextasinputandgeneratesthetext
leadinguptothenextexecution(e.g.,“Thisisanimage. Assistant,what...image? <ImagePath>”forExecution1). TextsingrayrepresentMM-REACT’sthoughtsorvisionexperts’actionsandoutputs,whichareinvisibletousers. Thismultimodalreasoningandaction
processoccursbehindthescenetogatherthenecessaryinformationforgeneratingfinalresponsestousers,whichareshowninblack.
5

<!-- Page 6 -->

allocatevisionexperts (invisibletousers),orproducethe tematically evaluate the performance with concrete accuracynumbers,duetoalackofannotatedbenchmarks.Thus,
final response to users . Each ChatGPT execution takes
itisworthinvestingeffortstowardshowtoeffectivelyevalthe preceding text as input and generates the text leading
uate such system’sperformance. 2). The vision capability
uptothenextexecution(e.g.,“Thisisanimage. Assistant,
islimitedbytheintegratedvisionexperts. Ononehand,the
whatobjectsdoyouseeinthisimage? <ImagePath>”for
integrated experts may make mistakes; on the other hand,
Execution 1). ChatGPT “learns” the proper text to generthesystemmayfailifthenecessaryexpertsaremissing. 3).
atebasedontheinstructionsandin-contextexamplesinthe

### We inject the vision experts’ knowledge in the prefix, and

promptprefix,asdetailedinSection3.3. Additionalexamthusthenumberofexpertsislimitedbythecontextwindow
ples of the reasoning and execution procedures are in Fig-
(4096tokens)ofChatGPT.4). Visualsignalsareconverted
ures18-22.
totextwordsforChatGPTunderstanding,whichmightnot

### MM-REACTCapabilitiesandApplications be the optimal solution for certain vision tasks. 5). MM-


### REACT requires manual prompt engineering. We expect

Figures4-14showtherepresentativecapabilitiesandapresearchworktoautomatethisprocess,makingthesystem
plicationscenariosthatMM-REACTdemonstrates. Specifeveneasiertodevelop.
ically, we examine MM-REACT’s capabilities in visual
math and text reasoning (Figure 4), understanding visual- 5.Conclusion
conditioned jokes and memes (Figure 5), spatial and coordinate understanding, visual planning and prediction (Fig- We have presented MM-REACT, a system paradigm
ure 6), multi-image reasoning (Figure 7), multi-hop doc- that synergizes multimodal reasoning and action to
ument understanding on bar charts (Figure 8), floorplans tackle complicated visual understanding problems. MM-
(Figure9),flowcharts(Figure10),tables(Figure11),open- REACT presents a simple and flexible way to empower
worldconceptunderstanding(Figure12),andvideoanaly- LLMswithapoolofvisionexperts.Extensivezero-shotexsis and summarization (Figure 13, 14). We provide an ex- periments demonstrate MM-REACT’s capabilities insolvampleoftheunfoldedstepsinFigure18. ing a wide range of challenging understanding tasks, such
asmulti-imagereasoning,multi-hopdocumentunderstand-

### CapabilityComparisonwithPaLM-E ing, open-world concept understanding, video summarization,andmore.


### MM-REACTisatraining-freeschemewhichcomposes

existing vision experts with ChatGPT, while PaLM-E [10] Acknowledgment
trains a vision-language model which combines an image

### WewouldliketoexpressourgratitudetoJianfengGaoforhis

encoder and a text decoder with dedicated datasets. Figvaluable suggestions, as well as to Jianwei Yang for generously
ures15-17showsourMM-REACTcanachievecompetitive
providing the image editing tool utilizing the X-Decoder frameresultstoPaLM-E.Wefurtherillustratethecompletemulwork.
timodalreasoningandactionproceduresinFigures21,22.

### References


### MM-REACTExtensibility

[1] MichaelAhn,AnthonyBrohan,NoahBrown,YevgenCheb-

### In Figure 23 and 24, we explore the enhancement of

otar, Omar Cortes, Byron David, Chelsea Finn, Keerthana

### MM-REACT’s LLM from ChatGPT (“gpt-3.5-turbo”) to


### Gopalakrishnan,KarolHausman,AlexHerzog,etal.Doasi


### GPT-4(language-only). Weaccessthelanguage-onlyGPT-

can,notasisay:Groundinglanguageinroboticaffordances.
4 via the ChatGPT website and reference the multimodal arXivpreprintarXiv:2204.01691,2022. 2
GPT-4 demo provided by OpenAI for comparison. These [2] Jean-BaptisteAlayrac, JeffDonahue, PaulineLuc, Antoine
examples demonstrate the benefit of MM-REACT’s ex- Miech,IainBarr,YanaHasson,KarelLenc,ArthurMensch,
tensibility: MM-REACT equipped with GPT-4 correctly Katie Millican, Malcolm Reynolds, et al. Flamingo: a vianswers the physics question (Figure 23), while the ver- sual language model for few-shot learning. arXiv preprint
sion with ChatGPT (GPT-3.5) fails. Furthermore, MM- arXiv:2204.14198,2022. 2
REACT is designed with the flexibility to incorporate new [3] TomBBrown,BenjaminMann,NickRyder,MelanieSubtools without training. Figure 25 provides a case study of biah,JaredKaplan,PrafullaDhariwal,ArvindNeelakantan,
Pranav Shyam, Girish Sastry, Amanda Askell, et al. Lanplugging an image editing tool from X-decoder [38] for
guagemodelsarefew-shotlearners. InNeurIPS,2020. 2
multi-round,dialogue-basedimageediting.
[4] NicolasCarion,FranciscoMassa,GabrielSynnaeve,Nicolas

### Limitations Usunier,AlexanderKirillov,andSergeyZagoruyko.End-toendobjectdetectionwithtransformers. InECCV,2020. 2

We identify the following limitations. 1). Considering [5] Harrison Chase. Langchain. https://langchain.
therecognitioncapabilityinthewild,wefindithardtosys- readthedocs.io/,2023. 4
6

<!-- Page 7 -->

Figure4.CasestudiesofMM-REACT’scapabilitiesandapplicationscenarios:visualmathandtextreasoning.
7

<!-- Page 8 -->

[6] Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, zero-shotreasoners.arXivpreprintarXiv:2205.11916,2022.

### Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul 2,3

Barham, Hyung Won Chung, Charles Sutton, Sebastian [18] Junnan Li, Dongxu Li, Silvio Savarese, and Steven Hoi.
Gehrmann, et al. Palm: Scaling language modeling with Blip-2: Bootstrapping language-image pre-training with
pathways. arXivpreprintarXiv:2204.02311,2022. 2 frozen image encoders and large language models. arXiv
[7] Tat-SengChua,JinhuiTang,RichangHong,HaojieLi,Zhip- preprintarXiv:2301.12597,2023. 2
ingLuo,andYantaoZheng.Nus-wide:areal-worldwebim- [19] Tsung-YiLin,MichaelMaire,SergeBelongie,JamesHays,
agedatabasefromnationaluniversityofsingapore. InPro- PietroPerona,DevaRamanan,PiotrDolla´r,andCLawrence
ceedingsoftheACMinternationalconferenceonimageand Zitnick. Microsoft coco: Common objects in context. In
videoretrieval,pages1–9,2009. 2 ECCV,2014. 2
[8] Mostafa Dehghani, Josip Djolonga, Basil Mustafa, Piotr [20] Ziwei Liu, Ping Luo, Xiaogang Wang, and Xiaoou Tang.
Padlewski, Jonathan Heek, Justin Gilmer, Andreas Steiner, Deeplearningfaceattributesinthewild. InProceedingsof
Mathilde Caron, Robert Geirhos, Ibrahim Alabdulmohsin, theIEEEinternationalconferenceoncomputervision,pages
etal. Scalingvisiontransformersto22billionparameters. 3730–3738,2015. 2
arXivpreprintarXiv:2302.05442,2023. 2 [21] Pan Lu, Swaroop Mishra, Tony Xia, Liang Qiu, Kai-Wei
[9] Alexey Dosovitskiy, Lucas Beyer, Alexander Kolesnikov, Chang, Song-Chun Zhu, Oyvind Tafjord, Peter Clark, and
Dirk Weissenborn, Xiaohua Zhai, Thomas Unterthiner, Ashwin Kalyan. Learn to explain: Multimodal reasoning
MostafaDehghani,MatthiasMinderer,GeorgHeigold,Syl- via thought chains for science question answering. arXiv
vain Gelly, et al. An image is worth 16x16 words: Trans- preprintarXiv:2209.09513,2022. 3
formers for image recognition at scale. arXiv preprint [22] Reiichiro Nakano, Jacob Hilton, Suchir Balaji, Jeff Wu,
arXiv:2010.11929,2020. 2 LongOuyang,ChristinaKim,ChristopherHesse,Shantanu
[10] Danny Driess, Fei Xia, Mehdi S. M. Sajjadi, Corey Jain, Vineet Kosaraju, William Saunders, et al. Webgpt:
Lynch,AakankshaChowdhery,BrianIchter,AyzaanWahid, Browser-assistedquestion-answeringwithhumanfeedback.
Jonathan Tompson, Quan Vuong, Tianhe Yu, Wenlong arXivpreprintarXiv:2112.09332,2021. 2
Huang, Yevgen Chebotar, Pierre Sermanet, Daniel Duck- [23] OpenAI. Gpt-4technicalreport. 2023. 2,4
worth,SergeyLevine,VincentVanhoucke,KarolHausman, [24] Timo Schick, Jane Dwivedi-Yu, Roberto Dess`ı, Roberta
Marc Toussaint, Klaus Greff, Andy Zeng, Igor Mordatch, Raileanu, Maria Lomeli, Luke Zettlemoyer, Nicola Canand PeteFlorence. Palm-e: An embodiedmultimodal lan- cedda, and Thomas Scialom. Toolformer: Language modguagemodel. InarXivpreprintarXiv:2303.03378,2023. 2, els can teach themselves to use tools. arXiv preprint
3,6,20,21,22 arXiv:2302.04761,2023. 2
[11] LuyuGao,AmanMadaan,ShuyanZhou,UriAlon,Pengfei [25] D´ıdac Sur´ıs, Sachit Menon, and Carl Vondrick. Vipergpt:
Liu, Yiming Yang, Jamie Callan, and Graham Neubig. Visualinferenceviapythonexecutionforreasoning. arXiv
Pal: Program-aided language models. arXiv preprint preprintarXiv:2303.08128,2023. 3
arXiv:2211.10435,2022. 2 [26] HarshTrivedi,NiranjanBalasubramanian,TusharKhot,and
[12] KaimingHe,XiangyuZhang,ShaoqingRen,andJianSun. Ashish Sabharwal. Interleaving retrieval with chain-of-
Deep residual learning for image recognition. In CVPR, thoughtreasoningforknowledge-intensivemulti-stepques-
2016. 2 tions. arXivpreprintarXiv:2212.10509,2022. 2
[13] YushiHu,HangHua,ZhengyuanYang,WeijiaShi,NoahA [27] Maria Tsimpoukelli, Jacob Menick, Serkan Cabi, SM Es-
Smith, and Jiebo Luo. Promptcap: Prompt-guided task- lami, Oriol Vinyals, and Felix Hill. Multimodal fewawareimagecaptioning. arXivpreprintarXiv:2211.09699, shot learningwith frozen languagemodels. arXiv preprint
2022. 2 arXiv:2106.13884,2021. 2
[14] Shaohan Huang, Li Dong, Wenhui Wang, Yaru Hao, [28] AshishVaswani,NoamShazeer,NikiParmar,JakobUszko-
Saksham Singhal, Shuming Ma, Tengchao Lv, Lei Cui, reit,LlionJones,AidanNGomez,ŁukaszKaiser,andIllia
Owais Khan Mohammed, Qiang Liu, et al. Language is Polosukhin. Attentionisallyouneed. InNeurIPS,2017. 2
not all you need: Aligning perception with language mod- [29] Jianfeng Wang, Zhengyuan Yang, Xiaowei Hu, Linjie Li,
els. arXivpreprintarXiv:2302.14045,2023. 2,3 KevinLin,ZheGan,ZichengLiu,CeLiu,andLijuanWang.
[15] Wenlong Huang, Pieter Abbeel, Deepak Pathak, and Igor Git: A generative image-to-text transformer for vision and
Mordatch. Languagemodelsaszero-shotplanners:Extract- language. arXivpreprintarXiv:2205.14100,2022. 2
ingactionableknowledgeforembodiedagents. InInterna- [30] ZhenhailongWang,ManlingLi,RuochenXu,LuoweiZhou,
tionalConferenceonMachineLearning,pages9118–9147. Jie Lei, Xudong Lin, Shuohang Wang, Ziyi Yang, Chen-
PMLR,2022. 2 guangZhu,DerekHoiem,etal. Languagemodelswithim-
[16] MarkJHuiskesandMichaelSLew. Themirflickrretrieval agedescriptorsarestrongfew-shotvideo-languagelearners.
evaluation.InProceedingsofthe1stACMinternationalcon- InAdvancesinNeuralInformationProcessingSystems. 2
ference on Multimedia information retrieval, pages 39–43, [31] Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten
2008. 2 Bosma,EdChi,QuocLe,andDennyZhou.Chainofthought
[17] Takeshi Kojima, Shixiang Shane Gu, Machel Reid, Yutaka promptingelicitsreasoninginlargelanguagemodels. arXiv
Matsuo, and Yusuke Iwasawa. Large language models are preprintarXiv:2201.11903,2022. 2,3
8

<!-- Page 9 -->

[32] ChenfeiWu,ShengmingYin,WeizhenQi,XiaodongWang,

### Zecheng Tang, and Nan Duan. Visual chatgpt: Talking,

drawing and editing with visual foundation models. arXiv
preprintarXiv:2303.04671,2023. 3
[33] ZhengyuanYang,ZheGan,JianfengWang,XiaoweiHu,YumaoLu,ZichengLiu,andLijuanWang. Anempiricalstudy
ofgpt-3forfew-shotknowledge-basedvqa. InProceedings
oftheAAAIConferenceonArtificialIntelligence,volume36,
pages3081–3089,2022. 2
[34] ShunyuYao,JeffreyZhao,DianYu,NanDu,IzhakShafran,

### Karthik Narasimhan, and Yuan Cao. React: Synergizing

reasoning and acting in language models. arXiv preprint
arXiv:2210.03629,2022. 2,4
[35] Lu Yuan, Dongdong Chen, Yi-Ling Chen, Noel Codella,
Xiyang Dai, Jianfeng Gao, Houdong Hu, Xuedong Huang,

### Boxin Li, Chunyuan Li, et al. Florence: A new

foundation model for computer vision. arXiv preprint
arXiv:2111.11432,2021. 2
[36] AndyZeng,AdrianWong,StefanWelker,KrzysztofChoromanski, Federico Tombari, Aveek Purohit, Michael Ryoo,
VikasSindhwani,JohnnyLee,VincentVanhoucke,etal.Socratic models: Composing zero-shot multimodal reasoning
withlanguage. arXivpreprintarXiv:2204.00598,2022. 2
[37] Zhuosheng Zhang, Aston Zhang, Mu Li, Hai Zhao,
George Karypis, and Alex Smola. Multimodal chain-ofthought reasoning in language models. arXiv preprint
arXiv:2302.00923,2023. 3
[38] XueyanZou,Zi-YiDou,JianweiYang,ZheGan,LinjieLi,

### ChunyuanLi,XiyangDai,JianfengWang,LuYuan,Nanyun

Peng,LijuanWang,YongJaeLee,andJianfengGao. Generalizeddecodingforpixel, imageandlanguage. 2022. 6,
30
9

<!-- Page 10 -->

This image is a cartoon illustration of a
squirrel holding a camera
This image is likely a comic or cartoon
illustration.

### Why would a person find this image funny?

Is there text in the image? If so, can you
The humor in this image is subjective and
read it and explain it to me?
can vary from person to person. Some
people might find the cartoon squirrel
holding a camera funny because it is a cute

### The text in the image is a conversation

and quirky illustration. Others might find it
between two people. One person says
funny because it is a humorous take on the
they don’t feel good and need to buy a
idea of a squirrel taking photos.
test. The other person asks if the first
Ultimately, the humor in this image is up
person is pregnant or has the
to the interpretation of the individual
coronavirus. The text is likely part of a
viewer. So, it depends on the person’s
comic or cartoon illustration. The image is
sense of humor and personal preferences.
tagged with “@INNA_S_ART”, which may
indicate the artist or creator of the image.

### What is funny about it?


### The humor in the comic may come from

the situation, the characters, or the
dialogue. The person is feeling unwell and
What is unusual about this image? is asked if they are pregnant or have the
coronavirus, which is a current and
relevant topic. The humor may come
The unusual thing about this image is that from the absurdity of the situation or the
a man is ironing clothes in the back of a unexpectedness of the question.
yellow taxi. This is not a common sight and However, humor is subjective and what
may be considered unusual or unique. one person finds funny, another person
may not. It is best to view the comic and
decide for yourself if it is funny.

### Visual-conditioned Joke/Meme

Figure5. CasestudiesofMM-REACT’scapabilitiesandapplicationscenarios: visual-conditionedjoke/meme. Weprovideanexample
oftheunfoldedmulti-modalreasoningandactionstepsformemeunderstandinginFigure18.
10

<!-- Page 11 -->

This image is likely a dog playing frisbee
with a man.
This image is a recipe for making bread at

### Where is the frisbee in the image?

home. The ingredients include water, salt,
flour, sugar, and yeast. The instructions
The frisbee is located at the top left include kneading the dough, dividing it
corner of the image with coordinates into pieces, and baking it on each side
(63, 119) and (133, 177). until well done. The temperature is in
Celsius.

### Where is the man in the image?

The man is located at the coordinates What should I do after kneading the
(66, 386) to (453, 604) in the image. dough, before dividing it into pieces?
What is the spatial relation between the
frisbee and the man?

### After kneading the dough, you should put

The frisbee is located above the man in it in a warm place before dividing it into
the image. The man is falling on the pieces, according to the recipe in the
ground while the frisbee is in the air. image.
The frisbee is also closer to the top of
the image than the man..
How long should I put in warm places?

### Illustration of detected

You should put the dough in a warm
bbox from MM-React
place for 1 hour.
Spatial/Coordinate Understanding Visual Planning and Prediction
Figure6. CasestudiesofMM-REACT’scapabilitiesandapplicationscenarios: spatial/coordinateunderstandingandvisualplanning
andprediction.
11

<!-- Page 12 -->

Receipt 1: Receipt 2:

### Receipt 3: Receipt 4:


### How much did I spend on grocery?

You spent $25.97 on groceries at The Shop Store #100 in Chicago, IL.

### How much did I spend on dining out?

You spent $23.45 on dining out at the Windmill Family Restaurant.

### How much in total did I spend on travel?

You spent $1299.90 on airfare and $43.83 on an Uber ride for a total of $1343.73 on travel.

### How much in total did I pay for taxes?

You paid $323.23 in total for taxes. This includes $321.90 for taxes and fees for the flight purchase
and $1.33 for sales tax for the Windmill Family Restaurant expenses.

### Multi-Image Reasoning

Figure7.CasestudiesofMM-REACT’scapabilitiesandapplicationscenarios:multi-imagereasoning.Forthemulti-imageinputsshown
above,weinputonereceiptimageatatime. OnceallfourreceiptimagesareprovidedasinputstoMM-REACT,wepromptittoanswer
questionsthatrequirereasoningovermultipleimages.
12

<!-- Page 13 -->

Figure8. CasestudiesofMM-REACT’scapabilitiesandapplicationscenarios: multi-hopdocumentunderstanding(barcharts). The
unfoldedmulti-modalreasoningandactionstepsofthisexamplearedetailedinFigure19.
13

<!-- Page 14 -->

Figure9.CasestudiesofMM-REACT’scapabilitiesandapplicationscenarios:documentunderstanding(floorplan).
14

<!-- Page 15 -->

Figure10. CasestudiesofMM-REACT’scapabilitiesandapplicationscenarios: documentunderstanding(flowchart). Weprovidean
exampleoftheunfoldedmulti-modalreasoningandactionstepsforflowchartunderstandinginFigure20.
15

<!-- Page 16 -->

Figure11.CasestudiesofMM-REACT’scapabilitiesandapplicationscenarios:documentunderstanding(table).
16

<!-- Page 17 -->


## İ

Figure12.CasestudiesofMM-REACT’scapabilitiesandapplicationscenarios:open-worldconceptunderstanding.
17

<!-- Page 18 -->

Please create a summary of the video in less than 10 sentences.
The speaker is making a BLT sandwich with grilled tomatoes and fried bacon. They are using fresh bread,
mayo, Worcester sauce, lettuce, and tomatoes. They are sprinkling salt and pepper on top. The bread can
be toasted or grilled. The speaker mentions that the few ingredients used in the sandwich will give it a lot
of flavor. The speaker mentions that the bread is important and can be toasted or grilled. The final product
is a BLT sandwich.
Can you breakdown this tutorial of making a BLT sandwich to step-by-step instructions, with start and end time?
Here's a breakdown of the start and end times for each step in the video:

## Heat a little olive oil in a pan and grill the tomatoes: 00:00:22 - 00:00:40


## Cook the bacon in a frying pan: 00:00:51 - 00:01:41


## Place the cooked bacon on a paper towel: 00:01:39 - 00:01:49


## Spread mayo and add Worcestershire sauce: 00:01:55 - 00:02:16


## Assemble the sandwich (lettuce, tomatoes, bacon): 00:02:22 - 00:03:11

a. Layer lettuce: 00:02:44 - 00:02:49
b. Add grilled tomatoes: 00:02:55 - 00:03:01
c. Place bacon on top: 00:03:15 - 00:03:27

## Sprinkle salt and pepper: 00:03:08 - 00:03:11


## Top the sandwich with the other slice of bread: 00:03:29 - 00:03:34

I am trying to create a short version of the video, can you suggest a shorter segment for each step?

### Here's a suggested shorter segment for each step:


## Heat a little olive oil in a pan and grill the tomatoes: 00:00:24 - 00:00:30


## Cook the bacon in a frying pan: 00:00:53 - 00:00:59


## Place the cooked bacon on a paper towel: 00:01:39 - 00:01:41


## Spread mayo and add Worcestershire sauce: 00:02:00 - 00:02:08


## Assemble the sandwich (lettuce, tomatoes, bacon): 00:02:44 - 00:03:01

a. Layer lettuce: 00:02:44 - 00:02:47
b. Add grilled tomatoes: 00:02:55 - 00:02:59
c. Place bacon on top: 00:03:15 - 00:03:20

## Sprinkle salt and pepper: 00:03:08 - 00:03:11


## Top the sandwich with the other slice of bread: 00:03:29 - 00:03:34


## Grill tomato 2.Fry Bacon 3.Drain Bacon 4. Spread Source

5a. Layer Lettuce 5b.Add Tomato 5c.Place Bacon 6.Sprinkle Salt/Pepper
Which segment is best for video thumbnail to attract more audience?
For a video thumbnail that attracts more audience, the segment
showing the assembled sandwich with all its layers would be the
most appealing. This image will showcase the delicious combination
of ingredients and the final result of the recipe. The suggested
segment for this is:
● Assembled BLT sandwich: 00:03:29 - 00:03:34
This segment shows the completed sandwich just before adding the
final slice of bread on top. You can take a screenshot of the
Suggested Thumbnail at 00:03:29 sandwich from this segment or create a more stylized image based
on it for your thumbnail.

### Video Summarization/Event Localization

Figure13.CasestudiesofMM-REACT’scapabilitiesandapplicationscenarios:videosummarization/eventlocalization.
18

<!-- Page 19 -->

Please create a summary of the video in less than 10 sentences.
The video is about Kobe Bryant’s final game in the NBA. He scored 60 points and led the Lakers to a victory
over the Utah Jazz. The crowd was out of their minds and the performance was considered one of the
greatest in the history of the game. Kobe was fouled and made two free throws for 60 points. The video
ends with the crowd applauding and Kobe’s final memory being a 60-point game and a victory over the
Utah Jazz. Overall, it was a magical farewell performance for one of the greatest athletes ever.
How did Kobe win the last 2 points to get 60? Explain and locate the start and end time of relevant segment in
this video.
Kobe Bryant won the last 2 points to reach 60 by making two free throws. He was fouled and went to the
free-throw line. The relevant section starts at 00:04:02 with the mention of the foul, it ends at 00:04:39
after Kobe successfully converts both free throws.
First Free throw at 00:04:11 - 00:04:15 Second Free throw at 00:04:31 - 00:04:34
I want to make a short video to highlight the long deuce by Kobe if there is any in the video. Can you tell me
roughly the start and end time of that.

### The long deuce by Kobe Bryant is mentioned at timestamp

00:03:28. The play leading up to this shot starts around
00:03:21, and the audience’s reaction to the long deuce
ends at approximately 00:03:32.

### Video Summarization/Event Localization

Figure14.CasestudiesofMM-REACT’scapabilitiesandapplicationscenarios:videosummarization/eventlocalization.
19

<!-- Page 20 -->


### PaLM-E


### Describe the following <img>: A dog

jumping over a hurdle at a dog show. PaLM-E

### Ours

Describe the following <img>: A dog

### PaLM-E Ours

Please describe the image jumping over a hurdle at a dog show.
This image is likely a dog jumping over
a hurdle in a dog agility competition.

### Ours


### Image Captioning, VQA

Please describe the image

### PaLM-E

I see (image omitted). Description: A cow sitting

### This image is likely a dog jumping over

on a rug, Joke: Why is the cow sitting on a rug?
a hurdle in a dog agility competition.
Because it wants to be a cow-ch! .. I see <img>.
Description: A donkey is carrying a dog, cat, and
Describe the following <img>: A dog

### Please describe the image

rooster. Joke: What do you call a donkey with a
jumping over a hurdle at a dog show.
rooster on his back. A rooster booster.
This image is likely a dog jumping over Ours Image Captioning, VQA
a hurdle in a dog agility competition.
Please write a joke for this image

### Why did the cat stand on the dog’s

back? Because the donkey was full! PaLM-E

### PaLM-E Ours


### Visual-Conditioned Jokes

I see (image omitted). Description: A cow sitting on a
rug, Joke: Why is the cow sitting on a rug? Because it

### PaLM-E

wants to be a cow-ch! .. I see <img>. Description: A
Q: Where is <img1> in this scene <img2>? A: donkey is carrying a dog, cat, and rooster. Joke: What do
A stove top with a pot on it. you call a donkey with a rooster on his back. A rooster
booster.

### Ours

Image1 Image2 Where is the coffee pot in the second image? Ours
The coffee pot is located in the kitchen

### Please write a joke for this image

with a stove and cabinets. It is a silver
coffee pot on a stove and its location is
I see (image omitted). Description: Please write a joke for this image
at (242, 230) to (295, 299). Why did the cat stand on the dog’s
A cow sitting on a rug, Joke: Why is
back? Because the donkey was full!
the cow sitting on a rug? Because it
Why did the cat stand on the dog’s
wants to be a cow-ch! .. I see
back? Because the donkey was full!
<img>. Description: A donkey is

### Illustration of detected

carrying a dog, cat, and rooster.
bbox from MM-React
Joke: What do you call a donkey Visual-Conditioned Jokes
with a rooster on his back. A
Multi-Image Relationships
rooster booster.
Figure 15. Comparison of MM-REACT with PaLM-E [10] on illustrated capabilities. We empirically show that text prompts are as
effectiveasexpensivejointfine-tuninginsolvingcomplicatedvisionproblems.
Visual-Conditioned Jokes
20

<!-- Page 21 -->

PaLM-E

### PaLM-E


### Given <img>. Q: How many championship rings did the

player on the left win in his career A: Let’s think step by Given <img>. Q: How many championship

### PaLM-E Ours

step 1. kobe bryant is on the left. 2. kobe bryant has won rings did the player on the left win in his
5 championship rings. career A: Let’s think step by step 1. kobe

### Ours

bryant is on the left. 2. kobe bryant has won
How many championship rings did the player on 5 championship rings.
the left win in his career?

### Ours


### Kobe Bryant won 5 championship rings in his

career. How many championship rings did the player on
the left win in his career?

### Multimodal Chain-of-Thought


### Kobe Bryant won 5 championship rings


### Given <img>. Q: How many championship

How many championship rings did the player on
in his career.
rings did the player on the left win in his
the left win in his career? PaLM-E
career A: Let’s think step by step 1. kobe

### Given <img>. Q: I am getting just two custom pizza

bryant is on the left. 2. kobe bryant has won for me and my friend. How much should I pay in Multimodal Chain-of-Thought
Kobe Bryant won 5 championship rings
5 championship rings.
total? A: Let's think step by step. 1st step: 2 custom
in his career.
pizzas. 2nd step: 2 x $9.99. 3rd step: $19.98.

### Ours


### Multimodal Chain-of-Thought

I am getting just two custom pizza for me and

### PaLM-E

my friend. How much should I pay in total?

### PaLM-E Ours

Based on the information you provided, you are Photo 1, at 10:30 am: <img1>. Photo 2, at 12:45 pm:
ordering two custom pizzas. The price of each Photo1 at 10:30am Photo2 at 12:45pm <img2>. Photo 3, at 3:45 pm: <img3>. Q: I forget,
custom pizza is $9.99. So, the total cost of two what did I have for lunch, and what time was it? A:
Photo1 at 10:30am Photo2 at 12:45pm Photo1 at 10:30am Photo2 at 12:45pm custom pizzas would be $9.99 x 2 = $19.98 Let’s think step by step. 1. you had a sandwich for
lunch. 2. it was 12:45 pm

### Scene Text Reasoning


### PaLM-E Photo3 at 4:45pm

Photo1 at 10:30am Photo2 at 12:45pm Photo 1, at 10:30 am: <img1>. Photo 2, at 12:45 Ours
pm: <img2>. Photo 3, at 3:45 pm: <img3>. Q: I

### Photo3 at 4:45pm Photo3 at 4:45pm

forget, what did I have for lunch, and what time

### I forget, what did I have for lunch,

was it? A: Let’s think step by step. 1. you had a
and what time was it?
sandwich for lunch. 2. it was 12:45 pm

### Ours

You had a sandwich for lunch at

### Photo3 at 4:45pm

I forget, what did I have for lunch, 12:45pm.
Photo 1, at 10:30 am: <img1>. Photo 2, I forget, what did I have for lunch, and what time was it?
at 12:45 pm: <img2>. Photo 3, at 3:45 and what time was it?

### End-to-End Egocentric Q&A, Dialogue

pm: <img3>. Q: I forget, what did I have You had a sandwich for lunch at
for lunch, and what time was it? A: Let’s You had a sandwich for lunch at 12:45pm.
think step by step. 1. you had a sandwich 12:45pm.
for lunch. 2. it was 12:45 pm
End-to-End Egocentric Q&A, Dialogue

### End-to-End Egocentric Q&A, Dialogue

Figure 16. Comparison of MM-REACT with PaLM-E [10] on illustrated capabilities. We empirically show that text prompts are as
effectiveasexpensivejointfine-tuninginsolvingcomplicatedvisionproblems.
21

<!-- Page 22 -->


### PaLM-E


### PaLM-E Ours

Given <img> . Q: What will the robot do next?
A: fall.

### Ours


### What will the robot do next?

I’m sorry, I cannot predict the future
actions of the robot. The image only
shows its current state.

### Given <img> . Q: What will the Physical Prediction

robot do next? A: fall. What will the robot do next?

### PaLM-E


### I’m sorry, I cannot predict the future

actions of the robot. The image only When a human asks me to do a task, I will respond
shows its current state. with the sequence of actions I would do to
accomplish the task with only the items I see.
Physical Prediction Human: Use all of the ingredients you see to make
a cake batter. 1. crack egg. 2. put egg in bowl. 3.
put flour in bowl. 4. put sugar in bowl. 5. mix. 6.

### PaLM-E Ours

put in pan. 7. bake. 8. eat. 9. clean up.

### Ours

When a human asks me to do a task, I will

### When a human asks me to do a task, I will

When a human asks me to do a task, I will respond with the sequence of actions I would
respond with the sequence of actions I would
respond with the sequence of actions I would do to accomplish the task with only the items
do to accomplish the task with only the items
do to accomplish the task with only the items I see. Human: Use all of the ingredients you

### I see. Human: Use all of the ingredients you

I see. Human: Use all of the ingredients you see to make a cake batter.
see to make a cake batter.
see to make a cake batter. 1. crack egg. 2. put
To make a cake batter using the ingredients I

### To make a cake batter using the ingredients I

egg in bowl. 3. put flour in bowl. 4. put sugar
see in the image, I would do the following:
see in the image, I would do the following:
in bowl. 5. mix. 6. put in pan. 7. bake. 8. eat.

## Gather all of the bags of flour and empty


## Gather all of the bags of flour and empty

9. clean up.
them into a large mixing bowl.
them into a large mixing bowl.

## Add any other dry ingredients, such as


## Add any other dry ingredients, such as

sugar or baking powder, to the bowl.
sugar or baking powder, to the bowl.

## Mix the dry ingredients together until they


## Mix the dry ingredients together until they

are well combined.
are well combined.

## Add any liquids, such as milk or eggs, to


## Add any liquids, such as milk or eggs, to

the bowl and mix until the batter is smooth.
the bowl and mix until the batter is smooth.

## Pour the batter into a greased cake pan


## Pour the batter into a greased cake pan

and bake according to the recipe instructions.
and bake according to the recipe instructions.
Robot Perception, Dialogue, Planning

### Robot Perception, Dialogue, Planning

Figure 17. Comparison of MM-REACT with PaLM-E [10] on illustrated capabilities. We empirically show that text prompts are as
effectiveasexpensivejointfine-tuninginsolvingcomplicatedvisionproblems.
22

<!-- Page 23 -->

Is there text in the image? If so, can you read
it and explain it to me?
Thought 2 ChatGPT: Yes, there is text in the
image.
Action 2 Assistant, what is the OCR texts in
this image? <ImagePath>

### Invoke OCR


### Observation 2 OCR


### This image contains handwritten text

Convert image to <ImagePath> and List of texts (words) seen in this
send to ChatGPT
image:

## Before …


### I don’t feel good,

Thought 1 ChatGPT: This is an image.

### I need to buy

Action 1 Assistant, what objects do you see in the test
this image? <ImagePath> NOW …
Invoke vision experts, including I don’t feel good,
image captioning, dense captioning, I need to buy
object tagger, face detection. the test

## @Inna_S_Art

Observation 1 Image Captioning

### Are you pregnant?

Assistant: This is an image (444 x 444)

### Do you have the

with description a cartoon of a man
coronavirus ?
and a woman.
ChatGPT: The text in the image is a conversation

### Dense Captioning

between two people. One person says they don’t

### List of object descriptions, and their

feel good and need to buy a test. The other
locations in this image:
person asks if the first person is pregnant or has
a cartoon of a woman with a green
the coronavirus. The text is likely part of a comic
face (x1,y1,x2,y2) = (11, 152, 108, 344)
or cartoon illustration. The image is tagged with
a cartoon of a woman with a green
“@INNA_S_ART”, which may indicate the artist or
face (x1,y1,x2,y2) = (230, 155, 328,
creator of the image.
349)
…
Why is it funny?

### Object Tagger

ChatGPT: The humor in the comic may come

### List of object tags seen in this image:

from the situation, the characters, or the
text, cartoon, animated cartoon,
dialogue. The person is feeling unwell and is
comics, human face, fiction,
asked if they are pregnant or have the
illustration, clipart, comic, funny
coronavirus, which is a current and relevant
topic. The humor may come from the absurdity
of the situation or the unexpectedness of the
ChatGPT: This image is likely a comic or question. However, humor is subjective and what
cartoon illustration. one person finds funny, another person may not.
It is best to view the comic and decide for
yourself if it is funny.
Figure18.Unfoldedmultimodalreasoningandactionstepsforexampleofvisual-conditionedjoke/memeinFigure5.
23

<!-- Page 24 -->

Excluding the regular cab, what is the ChatGPT: This image is a chart of the total
average total fueling cost?
charging cost of different electric vehicles. The
electric vehicles are Ford F150 Lightning
(Estimate), Rivian R1T/S, and Tesla Model 3
ChatGPT: The average total fueling cost excluding (Standard Range). The total charging cost of Ford
the Ford F150 (Regular Cab) is $76.55. This is F150 Lightning (Estimate) is $22.76, the total
calculated by taking the sum of the total fueling charging cost of Rivian R1T/S is $31.35, and the
cost of Toyota RAV4 and Honda Civic and dividing total charging cost of Tesla Model 3 (Standard
it by 2. ($82.56 + $70.55) / 2 = $76.55. Range) is $12.54.
Convert image to <ImagePath> and
send to ChatGPT

### Excluding Ford F150 Lightning, what is the

Thought 1 ChatGPT: This is an image. average total charging cost?
Action 1 Assistant, what objects do you see in
this image? <ImagePath>

### Invoke vision experts, including image

ChatGPT: The average total charging cost
captioning, dense captioning, object
Convert image to <ImagePath> and excluding the Ford F150 Lightning (Estimate) is
tagger.
send to ChatGPT $22.44. This is calculated by taking the sum of
Observation 1 Image Captioning the total charging cost of Rivian R1T/S and Tesla
This is an image (410 x 593) with Model 3 (Standard Range) and dividing it by 2.
description a graph of a number of cars. ($31.35 + $12.54) / 2 = $22.44.
Thought 3 ChatGPT: This is an image.

### Dense Captioning

Action 3 Assistant, what objects do you see
List of object descriptions, and their
in this image? <ImagePath2>
locations in this image:
a purple rectangular object with white Invoke vision experts, including Now how much cheaper is the average
border (x1,y1,x2,y2) = (152, 169, 245, image captioning, dense charging cost over the electric cars (including
446) captioning, object tagger. Ford F150 Lightning) than the average fueling
a purple rectangular bar chart Observation 3 Image Captioning cost over the gasoline cars (including Ford
(x1,y1,x2,y2) = (25, 135, 365, 456) This is an image (400 x 297) with F150 (Regular Cab))? Let’s think step-by-step.
… description a chart of cost comparison.

### Object Tagger Dense Captioning

List of object tags seen in this image: List of object descriptions, and their

### ChatGPT: The average charging cost over the

text, screenshot, purple, violet, graphic locations in this image:
three electric cars (including Ford F150 Lightning)
design, … a yellow rectangle with black text
is $18.66, which is calculated by taking the sum
(x1,y1,x2,y2) = (154, 12, 245, 150)
of the total charging cost of Ford F150 Lightning
Thought 2 ChatGPT: This image is likely a bar a chart of cost per charge (x1,y1,x2,y2) = (Estimate), Rivian R1T/S, and Tesla Model 3
chart or graph. (1, 1, 391, 288) (Standard Range) and dividing it by 3. ($22.76 +
…
Action 2 Assistant, what is the OCR texts in $31.35 + $12.54) / 3 = $18.66.
this image? <ImagePath> Object Tagger
Invoke OCR List of object tags seen in this image: The average fueling cost over the three gasoline
text, screenshot, line, yellow, number, cars (including Ford F150 (Regular Cab)) is

### Observation 2 OCR

… $101.07, which is calculated by taking the sum of

### This image contains text

the total fueling cost of Ford F150 (Regular Cab),

### List of texts (words) seen in this


### Toyota RAV4, and Honda Civic and dividing it by

image: Thought 4 ChatGPT: This image is likely a 3. ($130.96 + $82.56 + $70.55) / 3 = $101.07.
$130.96 chart of cost comparison.

### Ford

Action 4 Assistant, what is the OCR texts in Therefore, the average charging cost is $82.41

## F150

this image? <ImagePath> cheaper than the average fueling cost. This is
(Regular Cab) Invoke OCR
calculated by subtracting the average charging
$82.56
Observation 4 OCR cost from the average fueling cost. $101.07 -

### Toyota

This image contains text $18.66 = $82.41.

## Rav4

List of texts (words) seen in this image:
$70.55
$22.76

### Honda

Ford F150

### Civic


### Lightning

Total fueling cost
(Estimate)
$31.35

### Rivian

ChatGPT: This image is a bar chart of the total

## R1T/S

fueling cost of different cars. The cars are Ford
$12.54
F150 (Regular Cab), Toyota RAV4, and Honda Civic.

### Tesla

The total fueling cost of Ford F150 (Regular Cab) is

### Model 3

$130.96, the total fueling cost of Toyota RAV4 is
(Standard Range)
$82.56, and the total fueling cost of Honda Civic is
Total charging cost
$70.55.
Figure19.Unfoldedmultimodalreasoningandactionstepsformulti-hopdocumentunderstanding(barcharts)inFigure8.
24

<!-- Page 25 -->

Can you read the text in this flowchart and
explain it to me?
Thought 2 ChatGPT: Let me ask for more
information about the text.
Action 2 Assistant, what is the OCR texts in
this image? <ImagePath>

### Invoke OCR


### Observation 2 OCR


### This image contains text

List of texts (words) seen in this
image:
Start
Input
num1

### Input

Convert image to <ImagePath> and
num2
send to ChatGPT
num1>num2

### False

Thought 1 ChatGPT: This is an image. Display
num2
Action 1 Assistant, what objects do you see in

### Stop

this image? <ImagePath>

### True

Invoke vision experts, including image

### Display

captioning, dense captioning, object
num 1
tagger.

### Observation 1 Image Captioning

This is an image (682 x 1080) with ChatGPT: The flowchart appears to be a simple
description a diagram of a computer program that takes two inputs, num1 and num2,
program. and compares them. If num1 is greater than
num2, it displays num1. If num2 is greater than

### Dense Captioning

num1, it displays num2. The program starts with

### List of object descriptions, and their

the “Start” label and ends with the “Stop” label.
locations in this image:
a white sign with green text
(x1,y1,x2,y2) = (104, 641, 329, 748) Can you transform this flowchart into a
simple program in python?
a green text on a white background
(x1,y1,x2,y2) = (115, 948, 314, 1052)
ChatGPT: Sure, I can try to write a simple
…
program in python based on the flowchart.

### Object Tagger

List of object tags seen in this image:
text, diagram, sketch, font, design

### ChatGPT: This image is a flowchart diagram of a

computer program. The text in the image is likely
the labels for the different parts of the flowchart.
Figure20.Unfoldedmultimodalreasoningandactionstepsfordocumentunderstanding(flowchart)inFigure10.
25

<!-- Page 26 -->

…
…
…
…
Figure21.Unfoldedmultimodalreasoningandactionstepsforexampleofmulti-imagerelationshipsinFigure15.
26
…

<!-- Page 27 -->

Figure22.UnfoldedmultimodalreasoningandactionstepsforexampleofscenetextreasoninginFigure16.
27

<!-- Page 28 -->


### GPT-4 (Multimodal)

User Answer question I.1.a. Think step-by-step.

### GPT-4 To answer question I.1.a, we need to express the

temperature T(x) in every point of the conductive bar, which is
characterized by the abscissa x. We are given that T(0) = T0 and
T(L) = Tb.
For a stationary regime, the heat equation for the
one-dimensional heat conduction in the bar is:
d²T/dx² = 0
Integrating once, we get:
dT/dx = C₁
Integrating a second time:

### T(x) = C₁x + C₂

To determine the constants C₁ and C₂, we use the boundary
conditions:

### T(0) = T0, which gives C₂ = T0

T(L) = Tb, which gives C₁ = (Tb - T0) / L
Finally, the expression for T(x) is:

### T(x) = (Tb - T0) * (x / L) + T0

This represents a linear temperature profile along the conductive
bar, with a slope of (Tb - T0) / L.
Answer question I.1.a. Think step-by-step.

### Ours w/ ChatGPT Ours w/ GPT-4 (Language-only)

To answer question I.1.a, one would need to use To answer question I.1.a, we'll consider the heat
the principles of thermodynamics and heat conduction equation along the thermal conductor bar.
transfer to determine the temperature at any We're working under the assumptions of stationary
point in the conductor bar. This would likely mode and one-dimensional heat conduction with no
involve solving a differential equation to find the lateral heat exchanges.
temperature distribution along the bar. The Start with Fourier's Law of heat conduction:
solution would depend on the specific properties q = -k * (dT/dx)
of the bar, such as its length, cross-sectional area, where q is the heat flow (W/m²), k is the thermal
and thermal conductivity, as well as the conductivity (W/m·K), and dT/dx is the temperature
temperature of the bolometer and the gradient along the x-axis.
temperature of the thermostat. The solution In a stationary regime, the heat flow q is constant
would also depend on the power of the incident throughout the bar. Thus, we have:
radiation and the current of polarization. Once the -k * (dT/dx) = constant
temperature distribution is found, the Integrate the equation with respect to x:
temperature at any point in the bar can be ∫(dT/dx) dx = ∫(constant/k) dx
determined by evaluating the solution at that After integration, we get:
point. T(x) = (constant/k) * x + C
where C is the integration constant.
Apply the boundary conditions to find the constants:

### T(0) = To => C = To

T(L) = Tb => (constant/k) * L + To = Tb

### Solve for the constant:

constant = k * (Tb - To) / L
Substitute the constant back into the T(x) equation:
T(x) = (k * (Tb - To) / L) * x / k + To

### T(x) = ((Tb - To) / L) * x + To

So, the temperature T(x) at any point x along the
thermal conductor bar is given by:

### T(x) = ((Tb - To) / L) * x + To

Figure23. Casestudiesof MM-REACT’sextensibility. WiththenewreleaseofGPT-4(Language-only),wecanupgradeChatGPTin
MM-REACTtoGPT-4(Langauge-only)andfurtherimprovetheresultsofMM-REACT.InFigure26,weprovidetheunfoldedmultimodal
reasoningandactionstepsbasedonOursw/ChatGPT.
28

<!-- Page 29 -->


### GPT-4 (Multimodal)

Can you write a template for this website in HTML? Replace the joke and punchline with a real one.

### Ours w/ ChatGPT Ours w/ GPT-4 (Language-only)

Figure24. Casestudiesof MM-REACT’sextensibility. WiththenewreleaseofGPT-4(Language-only),wecanupgradeChatGPTin
MM-REACTtoGPT-4(Langauge-only)andfurtherimprovetheresultsofMM-REACT.
29

<!-- Page 30 -->

Figure 25. Case studies of MM-REACT’s extensibility. MM-REACT is designed with the flexibility to plug in new experts. In this
example,MM-REACTisenhancedwiththeimageeditingmodelfromX-decoder[38]andcanperformdialogue-basedimageediting.
30

<!-- Page 31 -->

…
Figure26.UnfoldedmultimodalreasoningandactionstepswithChatGPTtotacklephysicsprobleminFigure23.
31

## Tables

**Table (Page 1):**

| Visual Math and Text Reasoning Visual-Conditioned Joke/Meme Spatial/Coordinate Understanding What is “a” in the first equation? What is funny about it? Where is the frisbee? What is y in the last equation? What is the relative position of the frisbee and the man? The value of “a” in the first equation “5 The humor in the comic may come from The frisbee is located at coordinates + a = 7” is 2. the situation, the characters, or the (63,119,133,177). dialogue. The person is feeling unwell The value of “y” in the last equation and is asked if they are pregnant or have The frisbee is located above the man in “34 + y = 39” is 5. the coronavirus, which is a current and the image. The man is falling on the relevant topic. The humor may come ground while the frisbee is in the air. The from the absurdity of the situation or the frisbee is also closer to the top of the unexpectedness of the question. image than the man.. Visual Planning and Prediction Multi-Image Reasoning Multi-Hop Document Understanding What should I do after kneading the dough, before dividing it How much in total did I spend on travel? Excluding the regular cab, what is the average total fueling into pieces? For how long? How much in total did I pay for taxes? cost? After kneading the dough, you should You spent $1299.90 on airfare and $43.83 The average total fueling cost excluding put it in a warm place before dividing it on an Uber ride for a total of $1343.73 on the Ford F150 (Regular Cab) is $76.55. This into pieces, according to the recipe in travel. is calculated by taking the sum of the total the image. fueling cost of Toyota RAV4 and Honda You paid $323.23 in total for taxes. This Civic and dividing it by 2. ($82.56 + You should put the dough in a warm includes $321.90 for taxes and fees for $70.55) / 2 = $76.55. place for 1 hour. the flight purchase and $1.33 for sales tax for the Windmill Family Restaurant. Open-World Concept Understanding Video Summarization/Event Localization What is the brand of these drink? Which Who are the celebrities in this image? Is it safe to eat this mushroom? Can you breakdown this video tutorial to step-by-step one is unsweetened? instructions, with start and end time? |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  | Can you breakdown this video tutorial to step-by-step instructions, with start and end time? |  |  |  |  |  |
|  | The brand of these drinks is “BETTER THAN MILK”. The unsweetened one is “BETTER THAN MILK organic OAT DRINK”. |  |  | Keira Knightley and Natalie Portman are the celebrities in this image. |  |  | Morel mushrooms are generally considered safe to eat when properly cooked. |  |  |  | Here's a step-by-step breakdown of the tutorial with start and end time. |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | … |  |  |  | … |


**Table (Page 1):**

| Where is the frisbee? What is the relative position of the frisbee and the man? |  |  |
|---|---|---|
|  | The frisbee is located at coordinates (63,119,133,177). The frisbee is located above the man in the image. The man is falling on the ground while the frisbee is in the air. The frisbee is also closer to the top of the image than the man.. |  |
|  |  |  |


**Table (Page 1):**

| The humor in the comic may come from the situation, the characters, or the dialogue. The person is feeling unwell and is asked if they are pregnant or have the coronavirus, which is a current and relevant topic. The humor may come from the absurdity of the situation or the unexpectedness of the question. |  |
|---|---|
|  |  |


**Table (Page 1):**

|  |  |  |  | How much in total did I spend on travel? How much in total did I pay for taxes? |  |  |  |  | Excluding the regular cab, what is the average total fueling cost? |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|
|  | After kneading the dough, you should put it in a warm place before dividing it into pieces, according to the recipe in the image. You should put the dough in a warm place for 1 hour. |  |  |  |  | You spent $1299.90 on airfare and $43.83 on an Uber ride for a total of $1343.73 on travel. You paid $323.23 in total for taxes. This includes $321.90 for taxes and fees for the flight purchase and $1.33 for sales tax for the Windmill Family Restaurant. |  |  |  | The average total fueling cost excluding the Ford F150 (Regular Cab) is $76.55. This is calculated by taking the sum of the total fueling cost of Toyota RAV4 and Honda Civic and dividing it by 2. ($82.56 + $70.55) / 2 = $76.55. |  |
|  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |


**Table (Page 5):**

| 3 Thought 2 ChatGPT: There are two faces detected in the image. Action request 2 Assistant, are there any celebrities in this image? <ImagePath> 4 Action execution 2 Invoke Celebrity Recognition Observation 2 Celebrity Recognition This image contains celebrities List of celebrities, and their location in this image: Kobe Bryant Convert image to <ImagePath> and (x1,y1,x2,y2)=(365,278,439,352) send to ChatGPT Paul Pierce (x1,y1,x2,y2)=(548,308,620,380) 1 Thought 1 ChatGPT: This is an image. 5 ChatGPT: This image contains two celebrities, Action request 1 Assistant, what objects do you see Kobe Bryant and Paul Pierce. They are both in this image? <ImagePath> basketball players. 2 Action execution 1 Invoke vision experts, including Image Captioning, Dense Captioning, Object Tagger, Face How many championship rings did the player Detection. on the left win in his career? Observation 1 Image Captioning Assistant: This is an image (694 x 6 Thought 3 ChatGPT: This question 720) with description a basketball requires Bing Search player in a yellow jersey with a ball in Action request 3 Assistant, Bing search how many his hand. championship rings did Kobe Bryant win in his career? Dense Captioning <ImagePath>. List of object descriptions, and their 7 Action execution 3 Invoke Bing Search locations in this image: Observation 3 Bing Search a close up of a basketball Assistant: Bryant, a shooting (x1,y1,x2,y2) = (63, 535, 190, 663) a basketball player in a yellow jersey guard, and O’Neal, a centre, (x1,y1,x2,y2) = (55, 19, 502, 700) meshed into a remarkably … effective combination, and, by the time Bryant was 23, the Lakers had Object Tagger won three consecutive NBA List of object tags seen in this image: championships. Kobe Bryant After sport, athletic game, basketball, … winning their third title in 2002, Bryant and the Lakers Face Detection encountered difficulties. Kobe Detected faces, and their location in Bryant has won a total of 5 rings in this image: 20 seasons… man (x1,y1,x2,y2)=(365,278,439,352) man 8 ChatGPT: Kobe Bryant won 5 championship (x1,y1,x2,y2)=(548,308,620,380) rings in his career. |  |  |  |  |  |  |  | ChatGPT: There are two faces detected in the image. |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  | Assistant, are there any celebrities in this image? <ImagePath> |  |  |  |  |  |
|  |  |  |  |  | 4 | Action execution 2 |  | Invoke Celebrity Recognition |  |  |  |  |  |
|  |  |  |  |  |  | Observation 2 |  | Celebrity Recognition This image contains celebrities List of celebrities, and their location in this image: Kobe Bryant (x1,y1,x2,y2)=(365,278,439,352) Paul Pierce (x1,y1,x2,y2)=(548,308,620,380) |  |  |  |  |  |
|  |  | Thought 1 ChatGPT: This is an image. |  |  |  |  |  |  |  |  |  |  |  |
| 1 |  | Thought 1 |  | ChatGPT: This is an image. |  |  |  |  |  |  |  |  |  |
|  |  | Action request 1 |  |  | 5 ChatGPT: This image contains two celebrities, Kobe Bryant and Paul Pierce. They are both basketball players. How many championship rings did the player on the left win in his career? | ChatGPT: This image contains two celebrities, Kobe Bryant and Paul Pierce. They are both basketball players. |  |  |  |  |  |  |  |
| 2 |  | Action execution 1 |  | Invoke vision experts, including Image Captioning, Dense Captioning, Object Tagger, Face Detection. |  |  |  |  |  |  |  |  |  |
|  |  |  |  | Image Captioning |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | Observation 1 |  | Image Captioning Assistant: This is an image (694 x 720) with description a basketball player in a yellow jersey with a ball in his hand. Dense Captioning List of object descriptions, and their locations in this image: a close up of a basketball (x1,y1,x2,y2) = (63, 535, 190, 663) a basketball player in a yellow jersey (x1,y1,x2,y2) = (55, 19, 502, 700) … Object Tagger List of object tags seen in this image: sport, athletic game, basketball, … Face Detection Detected faces, and their location in this image: man (x1,y1,x2,y2)=(365,278,439,352) man (x1,y1,x2,y2)=(548,308,620,380) |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  | 6 | Thought 3 |  | ChatGPT: This question requires Bing Search |  |  |  |  |  |
|  |  |  |  |  |  | Action request 3 |  | Assistant, Bing search how many championship rings did Kobe Bryant win in his career? <ImagePath>. |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  | 7 |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  | Action execution 3 |  | Invoke | Bing Search |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  | Observation 3 Bing Search Assistant: Bryant, a shooting guard, and O’Neal, a centre, meshed into a remarkably effective combination, and, by the time Bryant was 23, the Lakers had won three consecutive NBA championships. Kobe Bryant After winning their third title in 2002, Bryant and the Lakers encountered difficulties. Kobe Bryant has won a total of 5 rings in 20 seasons… 8 ChatGPT: Kobe Bryant won 5 championship rings in his career. | Observation 3 |  | Bing Search Assistant: Bryant, a shooting guard, and O’Neal, a centre, meshed into a remarkably effective combination, and, by the time Bryant was 23, the Lakers had won three consecutive NBA championships. Kobe Bryant After winning their third title in 2002, Bryant and the Lakers encountered difficulties. Kobe Bryant has won a total of 5 rings in 20 seasons… |  |  |  |  |  |
|  |  |  |  |  |  | ChatGPT: Kobe Bryant won 5 championship rings in his career. |  |  |  |  |  |  |  |
|  |  |  |  |  | 8 |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |


**Table (Page 5):**

| Ours |  |
|---|---|
|  |  |


**Table (Page 5):**

|  | Based on the information you provided, you are ordering two custom pizzas. The price of each custom pizza is $9.99. So, the total cost of two custom pizzas would be $9.99 x 2 = $19.98 |
|---|---|
| Scene Text Reasoning |  |


**Table (Page 5):**

|  | Based on the information you provided, you are ordering two custom pizzas. The price of each custom pizza is $9.99. So, the total cost of two custom pizzas would be $9.99 x 2 = $19.98 |
|---|---|
| Scene Text Reasoning |  |


**Table (Page 10):**

| This image is a cartoon illustration of a squirrel holding a camera This image is likely a comic or cartoon illustration. Why would a person find this image funny? Is there text in the image? If so, can you The humor in this image is subjective and read it and explain it to me? can vary from person to person. Some people might find the cartoon squirrel holding a camera funny because it is a cute The text in the image is a conversation and quirky illustration. Others might find it between two people. One person says funny because it is a humorous take on the they don’t feel good and need to buy a idea of a squirrel taking photos. test. The other person asks if the first Ultimately, the humor in this image is up person is pregnant or has the to the interpretation of the individual coronavirus. The text is likely part of a viewer. So, it depends on the person’s comic or cartoon illustration. The image is sense of humor and personal preferences. tagged with “@INNA_S_ART”, which may indicate the artist or creator of the image. What is funny about it? The humor in the comic may come from the situation, the characters, or the dialogue. The person is feeling unwell and What is unusual about this image? is asked if they are pregnant or have the coronavirus, which is a current and relevant topic. The humor may come The unusual thing about this image is that from the absurdity of the situation or the a man is ironing clothes in the back of a unexpectedness of the question. yellow taxi. This is not a common sight and However, humor is subjective and what may be considered unusual or unique. one person finds funny, another person may not. It is best to view the comic and decide for yourself if it is funny. |
|---|
| Visual-conditioned Joke/Meme |


**Table (Page 11):**

| This image is likely a dog playing frisbee with a man. Where is the frisbee in the image? The frisbee is located at the top left corner of the image with coordinates (63, 119) and (133, 177). Where is the man in the image? The man is located at the coordinates (66, 386) to (453, 604) in the image. What is the spatial relation between the frisbee and the man? The frisbee is located above the man in the image. The man is falling on the ground while the frisbee is in the air. The frisbee is also closer to the top of the image than the man.. Illustration of detected bbox from MM-React | This image is a recipe for making bread at home. The ingredients include water, salt, flour, sugar, and yeast. The instructions include kneading the dough, dividing it into pieces, and baking it on each side until well done. The temperature is in Celsius. What should I do after kneading the dough, before dividing it into pieces? After kneading the dough, you should put it in a warm place before dividing it into pieces, according to the recipe in the image. How long should I put in warm places? You should put the dough in a warm place for 1 hour. |
|---|---|
| Spatial/Coordinate Understanding | Visual Planning and Prediction |


**Table (Page 12):**

| Receipt 1: Receipt 2: Receipt 3: Receipt 4: How much did I spend on grocery? You spent $25.97 on groceries at The Shop Store #100 in Chicago, IL. How much did I spend on dining out? You spent $23.45 on dining out at the Windmill Family Restaurant. How much in total did I spend on travel? You spent $1299.90 on airfare and $43.83 on an Uber ride for a total of $1343.73 on travel. How much in total did I pay for taxes? You paid $323.23 in total for taxes. This includes $321.90 for taxes and fees for the flight purchase and $1.33 for sales tax for the Windmill Family Restaurant expenses. |
|---|
| Multi-Image Reasoning |
|  |


**Table (Page 13):**

|  |
|---|
|  |


**Table (Page 13):**

|  |  |
|---|---|
|  |  |


**Table (Page 14):**

|  |
|---|
|  |


**Table (Page 15):**

|  |
|---|
|  |


**Table (Page 15):**

|  |  |  |
|---|---|---|
|  |  |  |


**Table (Page 15):**

|  |  |  |
|---|---|---|
|  |  |  |


**Table (Page 16):**

|  |
|---|
|  |


**Table (Page 17):**

| İ |
|---|
|  |


**Table (Page 17):**

|  |  |  |
|---|---|---|
|  |  |  |


**Table (Page 17):**

|  |  |
|---|---|
|  |  |


**Table (Page 17):**

|  |  |
|---|---|
|  |  |
|  |  |


**Table (Page 17):**

|  |  |
|---|---|
|  |  |
| İ |  |
|  |  |


**Table (Page 18):**

| Please create a summary of the video in less than 10 sentences. The speaker is making a BLT sandwich with grilled tomatoes and fried bacon. They are using fresh bread, mayo, Worcester sauce, lettuce, and tomatoes. They are sprinkling salt and pepper on top. The bread can be toasted or grilled. The speaker mentions that the few ingredients used in the sandwich will give it a lot of flavor. The speaker mentions that the bread is important and can be toasted or grilled. The final product is a BLT sandwich. Can you breakdown this tutorial of making a BLT sandwich to step-by-step instructions, with start and end time? Here's a breakdown of the start and end times for each step in the video: 1. Heat a little olive oil in a pan and grill the tomatoes: 00:00:22 - 00:00:40 2. Cook the bacon in a frying pan: 00:00:51 - 00:01:41 3. Place the cooked bacon on a paper towel: 00:01:39 - 00:01:49 4. Spread mayo and add Worcestershire sauce: 00:01:55 - 00:02:16 5. Assemble the sandwich (lettuce, tomatoes, bacon): 00:02:22 - 00:03:11 a. Layer lettuce: 00:02:44 - 00:02:49 b. Add grilled tomatoes: 00:02:55 - 00:03:01 c. Place bacon on top: 00:03:15 - 00:03:27 6. Sprinkle salt and pepper: 00:03:08 - 00:03:11 7. Top the sandwich with the other slice of bread: 00:03:29 - 00:03:34 I am trying to create a short version of the video, can you suggest a shorter segment for each step? Here's a suggested shorter segment for each step: 1. Heat a little olive oil in a pan and grill the tomatoes: 00:00:24 - 00:00:30 2. Cook the bacon in a frying pan: 00:00:53 - 00:00:59 3. Place the cooked bacon on a paper towel: 00:01:39 - 00:01:41 4. Spread mayo and add Worcestershire sauce: 00:02:00 - 00:02:08 5. Assemble the sandwich (lettuce, tomatoes, bacon): 00:02:44 - 00:03:01 a. Layer lettuce: 00:02:44 - 00:02:47 b. Add grilled tomatoes: 00:02:55 - 00:02:59 c. Place bacon on top: 00:03:15 - 00:03:20 6. Sprinkle salt and pepper: 00:03:08 - 00:03:11 7. Top the sandwich with the other slice of bread: 00:03:29 - 00:03:34 1. Grill tomato 2.Fry Bacon 3.Drain Bacon 4. Spread Source 5a. Layer Lettuce 5b.Add Tomato 5c.Place Bacon 6.Sprinkle Salt/Pepper Which segment is best for video thumbnail to attract more audience? For a video thumbnail that attracts more audience, the segment showing the assembled sandwich with all its layers would be the most appealing. This image will showcase the delicious combination of ingredients and the final result of the recipe. The suggested segment for this is: ● Assembled BLT sandwich: 00:03:29 - 00:03:34 This segment shows the completed sandwich just before adding the final slice of bread on top. You can take a screenshot of the Suggested Thumbnail at 00:03:29 sandwich from this segment or create a more stylized image based on it for your thumbnail. |
|---|
| Video Summarization/Event Localization |
|  |


**Table (Page 18):**

|  | Here's a suggested shorter segment for each step: 1. Heat a little olive oil in a pan and grill the tomatoes: 00:00:24 - 00:00:30 2. Cook the bacon in a frying pan: 00:00:53 - 00:00:59 3. Place the cooked bacon on a paper towel: 00:01:39 - 00:01:41 4. Spread mayo and add Worcestershire sauce: 00:02:00 - 00:02:08 5. Assemble the sandwich (lettuce, tomatoes, bacon): 00:02:44 - 00:03:01 a. Layer lettuce: 00:02:44 - 00:02:47 b. Add grilled tomatoes: 00:02:55 - 00:02:59 c. Place bacon on top: 00:03:15 - 00:03:20 6. Sprinkle salt and pepper: 00:03:08 - 00:03:11 7. Top the sandwich with the other slice of bread: 00:03:29 - 00:03:34 |  |  |  |
|---|---|---|---|---|
|  |  |  |  |  |
|  | 1. Grill tomato | 2.Fry Bacon | 3.Drain Bacon | 4. Spread Source |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  | 5a. Layer Lettuce | 5b.Add Tomato | 5c.Place Bacon | 6.Sprinkle Salt/Pepper |


**Table (Page 18):**

|  |
|---|
| Suggested Thumbnail at 00:03:29 |


**Table (Page 19):**

| Please create a summary of the video in less than 10 sentences. The video is about Kobe Bryant’s final game in the NBA. He scored 60 points and led the Lakers to a victory over the Utah Jazz. The crowd was out of their minds and the performance was considered one of the greatest in the history of the game. Kobe was fouled and made two free throws for 60 points. The video ends with the crowd applauding and Kobe’s final memory being a 60-point game and a victory over the Utah Jazz. Overall, it was a magical farewell performance for one of the greatest athletes ever. How did Kobe win the last 2 points to get 60? Explain and locate the start and end time of relevant segment in this video. Kobe Bryant won the last 2 points to reach 60 by making two free throws. He was fouled and went to the free-throw line. The relevant section starts at 00:04:02 with the mention of the foul, it ends at 00:04:39 after Kobe successfully converts both free throws. First Free throw at 00:04:11 - 00:04:15 Second Free throw at 00:04:31 - 00:04:34 I want to make a short video to highlight the long deuce by Kobe if there is any in the video. Can you tell me roughly the start and end time of that. The long deuce by Kobe Bryant is mentioned at timestamp 00:03:28. The play leading up to this shot starts around 00:03:21, and the audience’s reaction to the long deuce ends at approximately 00:03:32. |
|---|
| Video Summarization/Event Localization |


**Table (Page 19):**

|  |
|---|
|  |
| First Free throw at 00:04:11 - 00:04:15 |


**Table (Page 19):**

|  |
|---|
|  |
| Second Free throw at 00:04:31 - 00:04:34 |


**Table (Page 20):**

| PaLM-E |  |
|---|---|
|  |  |


**Table (Page 20):**

| Image Captioning, VQA |
|---|
| PaLM-E I see (image omitted). Description: A cow sitting on a rug, Joke: Why is the cow sitting on a rug? Because it wants to be a cow-ch! .. I see <img>. Description: A donkey is carrying a dog, cat, and rooster. Joke: What do you call a donkey with a rooster on his back. A rooster booster. Ours Please write a joke for this image Why did the cat stand on the dog’s back? Because the donkey was full! |
| Visual-Conditioned Jokes |
| PaLM-E Q: Where is <img1> in this scene <img2>? A: A stove top with a pot on it. Ours Image1 Image2 Where is the coffee pot in the second image? The coffee pot is located in the kitchen with a stove and cabinets. It is a silver coffee pot on a stove and its location is at (242, 230) to (295, 299). Illustration of detected bbox from MM-React |
| Multi-Image Relationships |


**Table (Page 20):**

| PaLM-E |  |
|---|---|
|  |  |


**Table (Page 20):**

|  |
|---|
|  |


**Table (Page 20):**

|  |
|---|
| PaLM-E |


**Table (Page 20):**

|  |
|---|
|  |


**Table (Page 21):**

| PaLM-E Given <img>. Q: How many championship rings did the player on the left win in his career A: Let’s think step by step 1. kobe bryant is on the left. 2. kobe bryant has wo 5 championship rings. Ours How many championship rings did the player on the left win in his career? Kobe Bryant won 5 championship rings in his career. |  |  |  |  |  |  |
|---|---|---|---|---|---|---|
|  |  |  | M-E Given <img>. Q: How many championship rings did the player on the left win in his career A: Let’s think step by step 1. kobe bryant is on the left. 2. kobe bryant has wo 5 championship rings. |  |  | n |
|  | 5 champ Ours |  | 5 champ |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
| Multimodal Chain-of-Thought |  |  |  |  |  |  |
| PaLM-E Given <img>. Q: I am getting just two custom pizza for me and my friend. How much should I pay in total? A: Let's think step by step. 1st step: 2 custom pizzas. 2nd step: 2 x $9.99. 3rd step: $19.98. Ours I am getting just two custom pizza for me and my friend. How much should I pay in total? Based on the information you provided, you are ordering two custom pizzas. The price of each custom pizza is $9.99. So, the total cost of two custom pizzas would be $9.99 x 2 = $19.98 |  |  |  |  |  |  |
|  |  | Based on the information you provided, you are ordering two custom pizzas. The price of each custom pizza is $9.99. So, the total cost of two custom pizzas would be $9.99 x 2 = $19.98 |  |  |  |  |
| Scene Text Reasoning |  |  |  |  |  |  |
| PaLM-E Photo1 at 10:30am Photo2 at 12:45pm Photo 1, at 10:30 am: <img1>. Photo 2, at 12:45 pm: <img2>. Photo 3, at 3:45 pm: <img3>. Q: I forget, what did I have for lunch, and what time was it? A: Let’s think step by step. 1. you had a sandwich for lunch. 2. it was 12:45 pm Ours Photo3 at 4:45pm I forget, what did I have for lunch, and what time was it? You had a sandwich for lunch at 12:45pm. |  |  |  |  |  |  |
| End-to-End Egocentric Q&A, Dialogue |  |  |  |  |  |  |
|  |  |  |  |  |  |  |


**Table (Page 21):**

| PaLM-E |
|---|
| Given <img>. Q: How many championship rings did the player on the left win in his career A: Let’s think step by step 1. kobe bryant is on the left. 2. kobe bryant has won 5 championship rings. |


**Table (Page 21):**

| Ours |  |
|---|---|
|  |  |


**Table (Page 21):**

| PaLM-E Given <i |  |
|---|---|
|  | M-E Given <i |


**Table (Page 21):**

| pizzas. 2 Ours | pizzas. 2 |  |
|---|---|---|
|  |  |  |


**Table (Page 21):**

| PaLM-E |
|---|
| Photo 1, at 10:30 am: <img1>. Photo 2, at 12:45 pm: <img2>. Photo 3, at 3:45 pm: <img3>. Q: I forget, what did I have for lunch, and what time was it? A: Let’s think step by step. 1. you had a sandwich for lunch. 2. it was 12:45 pm |


**Table (Page 21):**

|  | Photo1 at 10:30am |  |
|---|---|---|
|  |  |  |


**Table (Page 21):**

|  | Photo1 at 10:30am |  | Photo2 at 12:45pm |
|---|---|---|---|
|  |  |  |  |


**Table (Page 21):**

|  | Photo1 at 10:30am |  |
|---|---|---|
|  |  |  |


**Table (Page 21):**

|  | Photo1 at 10:30am |  |
|---|---|---|
|  |  |  |


**Table (Page 22):**

| PaLM-E Given <img> . Q: What will the robot do next? A: fall. Ours What will the robot do next? I’m sorry, I cannot predict the future actions of the robot. The image only shows its current state. |  |  |  |  |  |  |
|---|---|---|---|---|---|---|
|  |  |  | I’m sorry, I cannot predict the future actions of the robot. The image only shows its current state. |  |  |  |
| Physical Prediction |  |  |  |  |  |  |
| PaLM-E When a human asks me to do a task, I will respond with the sequence of actions I would do to accomplish the task with only the items I see. Human: Use all of the ingredients you see to make a cake batter. 1. crack egg. 2. put egg in bowl. 3. put flour in bowl. 4. put sugar in bowl. 5. mix. 6. put in pan. 7. bake. 8. eat. 9. clean up. Ours When a human asks me to do a task, I will respond with the sequence of actions I would do to accomplish the task with only the items I see. Human: Use all of the ingredients you see to make a cake batter. To make a cake batter using the ingredients I see in the image, I would do the following: 1. Gather all of the bags of flour and empty them into a large mixing bowl. 2. Add any other dry ingredients, such as sugar or baking powder, to the bowl. 3. Mix the dry ingredients together until they are well combined. 4. Add any liquids, such as milk or eggs, to the bowl and mix until the batter is smooth. 5. Pour the batter into a greased cake pan and bake according to the recipe instructions. |  |  |  |  |  |  |
|  |  |  |  | When a human asks me to do a task, I will respond with the sequence of actions I would do to accomplish the task with only the items I see. Human: Use all of the ingredients you see to make a cake batter. |  |  |
|  |  | To make a cake batter using the ingredients I see in the image, I would do the following: 1. Gather all of the bags of flour and empty them into a large mixing bowl. 2. Add any other dry ingredients, such as sugar or baking powder, to the bowl. 3. Mix the dry ingredients together until they are well combined. 4. Add any liquids, such as milk or eggs, to the bowl and mix until the batter is smooth. 5. Pour the batter into a greased cake pan and bake according to the recipe instructions. |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
| Robot Perception, Dialogue, Planning |  | gue, Planning |  |  |  |  |


**Table (Page 22):**

| PaLM-E |  |
|---|---|
|  |  |


**Table (Page 22):**

|  |  | I’m sorry, I cannot predict the future actions of the robot. The image only shows its current state. |  |
|---|---|---|---|
| Physical Prediction |  |  |  |


**Table (Page 22):**

|  |  |  | When a human asks me to do a task, I will respond with the sequence of actions I would do to accomplish the task with only the items I see. Human: Use all of the ingredients you see to make a cake batter. |  |
|---|---|---|---|---|
|  |  | To make a cake batter using the ingredients I see in the image, I would do the following: 1. Gather all of the bags of flour and empty them into a large mixing bowl. 2. Add any other dry ingredients, such as sugar or baking powder, to the bowl. 3. Mix the dry ingredients together until they are well combined. 4. Add any liquids, such as milk or eggs, to the bowl and mix until the batter is smooth. 5. Pour the batter into a greased cake pan and bake according to the recipe instructions. |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
| Robot Perception, Dialogue, Planning |  | gue, Planning |  |  |


**Table (Page 23):**

|  |  |  |  |  |
|---|---|---|---|---|
|  | Convert image to <ImagePath> and send to ChatGPT |  |  |  |


**Table (Page 23):**

|  |  | Is there text in the image? If so, can you read it and explain it to me? |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|
| Thought 2 ChatGPT: Yes, there is text in the image. Action 2 Assistant, what is the OCR texts in this image? <ImagePath> Invoke OCR Observation 2 OCR This image contains handwritten text List of texts (words) seen in this image: BEFORE … I don’t feel good, I need to buy the test NOW … I don’t feel good, I need to buy the test @INNA_S_ART Are you pregnant? Do you have the coronavirus ? |  |  |  |  |  |  |  |  |
|  |  |  | ChatGPT: Yes, there is text in the image. |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
|  |  |  | Assistant, what is the OCR texts in this image? <ImagePath> Invoke OCR |  |  |  |  |  |
| Observation 2 |  |  |  |  |  |  |  |  |
|  | Observation 2 |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |
| ChatGPT: The text in the image is a conversation between two people. One person says they don’t feel good and need to buy a test. The other person asks if the first person is pregnant or has the coronavirus. The text is likely part of a comic or cartoon illustration. The image is tagged with “@INNA_S_ART”, which may indicate the artist or creator of the image. |  |  |  |  |  |  |  |  |


**Table (Page 23):**

| Thought 2 |
|---|
| Action 2 |


**Table (Page 23):**

| <ImagePath> |
|---|
|  |


**Table (Page 23):**

| <ImagePath> |
|---|
|  |


**Table (Page 23):**

| Thought 1 ChatGPT: This is an image. Action 1 Assistant, what objects do you see in this image? <ImagePath> Invoke vision experts, including image captioning, dense captioning, object tagger, face detection. Observation 1 Image Captioning Assistant: This is an image (444 x 444) with description a cartoon of a man and a woman. Dense Captioning List of object descriptions, and their locations in this image: a cartoon of a woman with a green face (x1,y1,x2,y2) = (11, 152, 108, 344) a cartoon of a woman with a green face (x1,y1,x2,y2) = (230, 155, 328, 349) … Object Tagger List of object tags seen in this image: text, cartoon, animated cartoon, comics, human face, fiction, illustration, clipart, comic, funny |  |  |  |  |
|---|---|---|---|---|
|  |  | ChatGPT: This is an image. |  |  |
|  |  |  |  |  |
|  |  | Assistant, what objects do you see in this image? <ImagePath> Invoke vision experts, including image captioning, dense captioning, object tagger, face detection. |  |  |
| Observation 1 |  |  | Image Captioning |  |
|  | Observation 1 |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |


**Table (Page 23):**

| Thought 1 |
|---|
| Action 1 |


**Table (Page 23):**

| <ImagePath> |
|---|
|  |


**Table (Page 24):**

|  |  |  |  |
|---|---|---|---|
|  | Convert image to <ImagePath> and send to ChatGPT |  |  |


**Table (Page 24):**

| ChatGPT: The average total fueling cost excluding the Ford F150 (Regular Cab) is $76.55. This is calculated by taking the sum of the total fueling cost of Toyota RAV4 and Honda Civic and dividing it by 2. ($82.56 + $70.55) / 2 = $76.55. |  |
|---|---|
|  |  |
|  |  |


**Table (Page 24):**

|  | Thought 1 |  |
|---|---|---|
| Action 1 |  |  |


**Table (Page 24):**

|  | ChatGPT: This is an image. |  |  |
|---|---|---|---|
|  | Assistant, what objects do you see in this image? <ImagePath> Invoke vision experts, including image captioning, dense captioning, object tagger. |  |  |
| Observation 1 |  | Image Captioning |  |
|  |  |  |  |
|  |  |  |  |


**Table (Page 24):**

| Thought 3 |  |  |
|---|---|---|
|  |  |  |
| Action 3 |  |  |


**Table (Page 24):**

| ChatGPT: This is an image. |  |  |
|---|---|---|
|  |  |  |


**Table (Page 24):**

|  | Image Captioning |
|---|---|
| Observation 3 |  |
|  |  |
|  |  |


**Table (Page 24):**

|  |  | ChatGPT: This image is likely a bar chart or graph. |  |  |  |  |
|---|---|---|---|---|---|---|
|  |  | Assistant, what is the OCR texts in this image? <ImagePath> Invoke OCR |  |  |  |  |
| Observation 2 |  |  |  |  |  |  |
|  | Observation 2 |  |  |  |  |  |
|  |  |  |  |  |  |  |


**Table (Page 24):**

| ChatGPT: This image is likely a chart of cost comparison. |  |  |
|---|---|---|
|  |  |  |


**Table (Page 24):**

|  |  |
|---|---|
| Observation 4 |  |
|  |  |
|  |  |


**Table (Page 25):**

| Can you read the text in this flowchart and explain it to me? Thought 2 ChatGPT: Let me ask for more information about the text. Action 2 Assistant, what is the OCR texts in this image? <ImagePath> Invoke OCR Observation 2 OCR This image contains text List of texts (words) seen in this image: Start Input num1 Input Convert image to <ImagePath> and num2 send to ChatGPT num1>num2 False Thought 1 ChatGPT: This is an image. Display num2 Action 1 Assistant, what objects do you see in Stop this image? <ImagePath> True Invoke vision experts, including image Display captioning, dense captioning, object num 1 tagger. Observation 1 Image Captioning This is an image (682 x 1080) with ChatGPT: The flowchart appears to be a simple description a diagram of a computer program that takes two inputs, num1 and num2, program. and compares them. If num1 is greater than num2, it displays num1. If num2 is greater than Dense Captioning num1, it displays num2. The program starts with List of object descriptions, and their the “Start” label and ends with the “Stop” label. locations in this image: a white sign with green text (x1,y1,x2,y2) = (104, 641, 329, 748) Can you transform this flowchart into a simple program in python? a green text on a white background (x1,y1,x2,y2) = (115, 948, 314, 1052) ChatGPT: Sure, I can try to write a simple … program in python based on the flowchart. Object Tagger List of object tags seen in this image: text, diagram, sketch, font, design ChatGPT: This image is a flowchart diagram of a computer program. The text in the image is likely the labels for the different parts of the flowchart. |  |
|---|---|
|  | ChatGPT: Sure, I can try to write a simple program in python based on the flowchart. |
| ChatGPT: This image is a flowchart diagram of a computer program. The text in the image is likely the labels for the different parts of the flowchart. |  |


**Table (Page 25):**

| Thought 2 ChatGPT: Let me ask for more information about the text. Action 2 Assistant, what is the OCR texts in this image? <ImagePath> Invoke OCR Observation 2 OCR This image contains text List of texts (words) seen in this image: Start Input num1 Input num2 num1>num2 False Display num2 Stop True Display num 1 |  |  |  |  |
|---|---|---|---|---|
|  |  | ChatGPT: Let me ask for more information about the text. |  |  |
|  |  | Assistant, what is the OCR texts in this image? <ImagePath> Invoke OCR |  |  |
| Observation 2 |  |  |  |  |
|  | Observation 2 |  |  |  |
|  |  |  |  |  |


**Table (Page 25):**

| <ImagePath> |
|---|
|  |


**Table (Page 25):**

| <ImagePath> |
|---|
|  |


**Table (Page 25):**

| Thought 1 ChatGPT: This is an image. Action 1 Assistant, what objects do you see in this image? <ImagePath> Invoke vision experts, including image captioning, dense captioning, object tagger. Observation 1 Image Captioning This is an image (682 x 1080) with description a diagram of a computer program. Dense Captioning List of object descriptions, and their locations in this image: a white sign with green text (x1,y1,x2,y2) = (104, 641, 329, 748) a green text on a white background (x1,y1,x2,y2) = (115, 948, 314, 1052) … Object Tagger List of object tags seen in this image: text, diagram, sketch, font, design |  |  |  |  |
|---|---|---|---|---|
|  |  | ChatGPT: This is an image. |  |  |
|  |  | Assistant, what objects do you see in this image? <ImagePath> Invoke vision experts, including image captioning, dense captioning, object tagger. |  |  |
| Observation 1 |  |  |  |  |
|  | Observation 1 |  |  |  |
|  |  |  |  |  |


**Table (Page 25):**

| Thought 1 |
|---|
| Action 1 |


**Table (Page 25):**

| <ImagePath> |
|---|
|  |


**Table (Page 25):**

| ChatGPT: Sure, I can try to write a simple program in python based on the flowchart. |  |
|---|---|
|  |  |


**Table (Page 26):**

|  |  |
|---|---|
|  |  |
|  |  |
|  |  |
|  |  |


**Table (Page 26):**

|  | … |
|---|---|
|  |  |


**Table (Page 27):**

|  |  |  |
|---|---|---|
|  |  |  |
|  |  |  |
|  |  |  |


**Table (Page 27):**

|  |  |
|---|---|
|  |  |
|  |  |


**Table (Page 28):**

| GPT-4 (Multimodal) |
|---|
|  |


**Table (Page 28):**

|  |  |
|---|---|
| Ours w/ ChatGPT |  |
| To answer question I.1.a, one would need to use the principles of thermodynamics and heat transfer to determine the temperature at any point in the conductor bar. This would likely involve solving a differential equation to find the temperature distribution along the bar. The solution would depend on the specific properties of the bar, such as its length, cross-sectional area, and thermal conductivity, as well as the temperature of the bolometer and the temperature of the thermostat. The solution would also depend on the power of the incident radiation and the current of polarization. Once the temperature distribution is found, the temperature at any point in the bar can be determined by evaluating the solution at that point. |  |


**Table (Page 28):**

| Ours w/ GPT-4 (Language-only) |  |
|---|---|
| To answer question I.1.a, we'll consider the heat conduction equation along the thermal conductor bar. We're working under the assumptions of stationary mode and one-dimensional heat conduction with no lateral heat exchanges. Start with Fourier's Law of heat conduction: q = -k * (dT/dx) where q is the heat flow (W/m²), k is the thermal conductivity (W/m·K), and dT/dx is the temperature gradient along the x-axis. In a stationary regime, the heat flow q is constant throughout the bar. Thus, we have: -k * (dT/dx) = constant Integrate the equation with respect to x: ∫(dT/dx) dx = ∫(constant/k) dx After integration, we get: T(x) = (constant/k) * x + C where C is the integration constant. Apply the boundary conditions to find the constants: T(0) = To => C = To T(L) = Tb => (constant/k) * L + To = Tb Solve for the constant: constant = k * (Tb - To) / L Substitute the constant back into the T(x) equation: T(x) = (k * (Tb - To) / L) * x / k + To T(x) = ((Tb - To) / L) * x + To So, the temperature T(x) at any point x along the thermal conductor bar is given by: T(x) = ((Tb - To) / L) * x + To |  |


**Table (Page 29):**

| GPT-4 (Multimodal) |
|---|
|  |


**Table (Page 29):**

|  |
|---|
| Ours w/ ChatGPT |
|  |


**Table (Page 29):**

| Ours w/ GPT-4 (Language-only) |
|---|
|  |


**Table (Page 30):**

|  |
|---|
|  |
|  |


**Table (Page 31):**

|  |  |  |
|---|---|---|
|  |  |  |


**Table (Page 31):**

|  |  |
|---|---|
|  |  |
|  |  |


**Table (Page 31):**

| … |  |  |  |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |
|  | … |  |  |
