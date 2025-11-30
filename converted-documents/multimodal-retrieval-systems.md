---
title: "Multimodal Retrieval Systems"
original_file: "./Multimodal_Retrieval_Systems.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["llm", "rag", "evaluation", "multimodal"]
keywords: ["part", "level", "joint", "object", "pose", "point", "reconstruction", "align", "input", "dataset"]
summary: "<!-- Page 1 -->

OP-Align: Object-level and Part-level Alignment
for Self-supervised Category-level Articulated

### Object Pose Estimation

Yuchen Che1 , Ryo Furukawa2 , and Asako Kanezaki1
1 Tokyo Institute of Technology, Tokyo, Japan
cheyuchen.titech@gmail.com, kanezaki@c.titech.ac.jp
2 Accenture Japan Ltd, Tokyo, Japan
rfurukaward@gmail.com
Abstract. Category-levelarticulatedobjectposeestimationfocuseson
the pose estimation of unknown articulated objects within known categories. Despite its "
related_documents: []
---

# Multimodal Retrieval Systems

<!-- Page 1 -->

OP-Align: Object-level and Part-level Alignment
for Self-supervised Category-level Articulated

### Object Pose Estimation

Yuchen Che1 , Ryo Furukawa2 , and Asako Kanezaki1
1 Tokyo Institute of Technology, Tokyo, Japan
cheyuchen.titech@gmail.com, kanezaki@c.titech.ac.jp
2 Accenture Japan Ltd, Tokyo, Japan
rfurukaward@gmail.com
Abstract. Category-levelarticulatedobjectposeestimationfocuseson
the pose estimation of unknown articulated objects within known categories. Despite its significance, this task remains challenging due to
the varying shapes and poses of objects, expensive dataset annotation
costs,andcomplexreal-worldenvironments.Inthispaper,weproposea
novel self-supervised approach that leverages a single-frame point cloud
to solve this task. Our model consistently generates reconstruction with
a canonical pose and joint state for the entire input object, and it estimatesobject-levelposesthatreduceoverallposevarianceandpart-level
poses that align each part of the input with its corresponding part of
thereconstruction.Experimentalresultsdemonstratethatourapproach
significantly outperforms previous self-supervised methods and is comparable to the state-of-the-art supervised methods. To assess the performance of our model in real-world scenarios, we also introduce a new
real-world articulated object benchmark dataset3.
Keywords: 6DOFobjectposeestimation·Datasetcreation·Unsupervised learning
1 Introduction
Articulated objects, comprising multiple parts connected by revolute or prismatic joints with varying joint states (rotational angle of a revolute joint or
translation length of a prismatic joint), commonly exist in the real world. The
interactions between humans and these objects give rise to numerous practical
applications, such as robot manipulations and automation in industrial processes [5,25]. Therefore, pose estimation for these objects has become a crucial
problemincomputervision.Wefocusonaccomplishingthecategory-levelarticulatedobjectposeestimationthroughaself-supervisedapproach.Ourobjective
is to use a point cloud of unknown articulated objects within known categories
obtainedfromasingle-frameRGB-Dimagesegmentedbydetectionmodelssuch
3 Code and dataset are released at https://github.com/YC-Che/OP-Align.
4202
guA
92
]VC.sc[
1v74561.8042:viXra

<!-- Page 2 -->

2 Y. Che et al.

### Back-projection

w/oPose w/oShape SingleReal-time

### Method

SupervisionSupervisionFrame Inference RGB Depth Mask

### Point

PartMobility[35] ✓ ✓ Cloud n
UPPD[16] ✓ ✓ ✓ gilA

## Eap[24] ✓ ✓ ✓ P O -


### Ours ✓ ✓ ✓ ✓

Table 1: Overview of works on self-supervised Fig.1: Illustration of the articucategory-level articulated object pose estimation. lated object pose estimation.
as Mask-RCNN [9] as input. Then, we infer each part’s pose and segmentation,
each joint’s direction and pivot, as illustrated in Fig. 1. We aim to achieve this
without utilizing pose and shape annotations duringtraining.Duetothevarying
shapes, poses, and complex real-world environments, this task is ill-posed and
remains challenging.
Many works have focused on solving the aforementioned task under simpler
problem settings. Unsupervised Pose-aware Part Decomposition (UPPD) [16]
utilizes object shape annotations as a substitute for pose annotations. PartMobility[35]utilizesmultiple-framepointcloudsofthesameobjectunderdifferent
joint states. However, these methods still face limitations when confronted with
scenarios where shape information is unavailable or when dealing with singleframe data. To the best of our knowledge, Equi-Articulated-Pose (EAP) [24] is
the only work that has tackled this task with single-frame point cloud as input
and without shape or pose annotations on a synthetic dataset. EAP guides the
network to learn part-by-part reconstruction of the input shapes by combining
disentangled information, such as canonical part shapes, object structure, and
part-level poses, in a self-supervised manner. To achieve such disentanglement,
EAP extracts part-level SE(3)-equivariant shape feature of a local region, instead of object-level SE(3)-equivariant one, from an input and part-level poses.
Since part-level poses are not given in nature, EAP requires iterative updates
of such poses. It also uses an inner iterative operation, Slot-Attention [26], for
segmenting parts. These iterative operations sacrifice inference speed.
We propose Object-level and Part-level Alignment (OP-Align), a novel selfsupervisedapproachthatlearnsobject-levelalignment,part-levelalignment,and
canonicalreconstructionoftheentireobjectratherthanthepart-by-partreconstructions. The core idea is that part segmentation and part-level pose estimation should be done for objects with low object-level pose variance. Based on
this idea, we reconsider the order of the process of the part-by-part reconstruction approach (EAP) and propose a new learning strategy. In our approach, the
network first generates a reconstruction that maintains the canonical pose and
joint state for the entire input and aligns the input with the reconstruction at
theobject-leveltoreducetheoverallposevariance.Then,thenetworksegments
parts followed by aligning each part of the object-level aligned input and the
correspondingpartofthereconstructionbysimulatingjointmovement.Ourap-

<!-- Page 3 -->


### OP-Align: Object-level and Part-level Alignment 3

proach does not employ iterative operation, thus achieving real-time inference
speed. A comparison with previous works is presented in Tab. 1.
WecompareOP-Alignwithothermethodsonasyntheticdataset.Tofurther
testOP-Align’sperformance,wegenerateareal-worldRGB-Ddatasetwithmultiplecategoriesofarticulatedobjects.Experimentalresultsdemonstratethatour
approach achieves state-of-the-art performance with other self-supervised methodsandcomparableperformancewithothersupervised methodsonthesynthetic
dataset and the real-world dataset while achieving real-time inference speed.

### Our contributions are summarized as follows:


## We propose a new model designed for category-level articulated object pose

estimation in a self-supervised manner, which requires no of pose or shape
annotations.

## We generate a new real-world RGB-D dataset for the category-level articulated object pose estimation.


## We conduct experiments on a synthetic dataset and our real-world dataset.

Ourmodelachievescomparableperformancewiththestate-of-the-artsupervised methods and significantly outperforms previous self-supervised methods while achieving real-time inference speed.
2 Related Works
Category-level rigid object pose estimation: This task focuses on predictinganunknownrigidobject’sposefromimages.NOCS[39]predictstheper-pixel
coordinates in canonical space from RGB-D images. Several methods [12,13,37]
further employ CAD models from ShapeNet dataset [2] to generate shape templatesanduseiterativeclosestpoint(ICP)[34]formatchingthepose.Commonly
used backbone for this task is 3D graph convolution network (3DGCN) [22] and
PointNet++ [33]. These methods require expensive large-scale dataset annotation. Some approaches attempt to accomplish this task in a self-supervised
manner. With the CAD model available, several methods [36,38] render the
predicted pose with the CAD model as a synthetic image and compare it with
the input image. Some methods focus on the multi-view RGB images provided
cases [11,19]. Especially, SE(3)-eSCOPE [21] achieved this task with singleview input and without pose annotations or CAD models. They use the SE(3)-
equivariant backbone, Equivariant Point Net (EPN) [3], to simultaneously conduct SE(3)-invariant shape reconstruction as a reference frame, and predict the
SE(3)-equivariant pose transformation which sends input to the reconstruction.
Category-level articulated object pose estimation: This task focuses
on predicting part-level pose, part-level segmentation, and joint information for
unknown objects within known categories. Previous methods [1,14,20,41] try
to solve this task with RGB-D image or video input by directly estimating the
part-levelpose.Somemethods[18,29,31]transferthetaskintoamovableshape
reconstruction task with neural implicit representation [27,30] and predict the
pose indirectly. Some methods [8,15] parameterize the joint movement with active interaction with articulated objects. To reduce the segmentation cost, [23]

<!-- Page 4 -->

4 Y. Che et al.
uses semantic segmentation annotation and transfers it into part segmentation
to conduct semi-supervised learning. However, similar to the rigid object pose
estimation, the cost of the dataset annotation limits the application of these
methods. To solve this task in a self-supervised manner, UPPD [16] utilizes the
annotationofobjectshapeinsteadoftheannotationofobjectpose.Somemethods [10,35] used multi-view observation with the same object in different joint
states to predict the joint movement. EAP [24] solved such a task with a singleframe point cloud input and without shape or pose annotation. EAP repeats
theprocessofsegmentingeachpart,reconstructingtheper-partSE(3)-invariant
shape, and predicting the per-part pose multiple times to gain a refined pose
estimation. However, directly segmenting parts for inputs with different poses
and shapes is challenging, often resulting in poor accuracy, and the inference
speed is unsuitable for real-time applications.
Articulated Object Dataset: Synthetic datasets of articulated objects
such as Shape2Motion, SAPIEN, and PartNet [28,40,43] are commonly used in
the articulated object pose estimation. Compared to RGB-D images captured
from the real world, these datasets lack the consideration of complicated realworld environments. HOI4D [25] collects multiple articulated and rigid object
mesh data and RGB-D images in human-object interaction. However, due to
the mismatch between the depth and RGB channels, a non-negligible amount
of noise is present in their ground-truth annotation of part segmentation based
solely on the RGB channels.
3 Method
Category-levelarticulatedobjectposeestimationcanbedefinedasfollows.Given
apointcloudX R 3 × N ofanarticulatedobjectconsistingofP parts,weassign
∈
each point to a part, predict the rotation and translation for each part, and
provide the pivot and the direction for each joint. To solve this problem, our
model predicts each point’s segmentation probability W R P × N, each joint’s
∈
pivotanddirection c [i] R 3,d [i] R 3 i 1,2,...,J ,andtherotationand
{ ∈ ∈ | ∈{ }}
the translation for each part R [i] SO(3),t [i] R 3 i 1,2,...,P . During
{ ∈ ∈ | ∈{ }}
training, we assume that the number of parts P and the type of joints (revolute
or prismatic) are given. Specifically, OP-Align assumes that each joint connects
two independent parts, resulting in J = P 1 joints, which cover most of the
−
articulated object categories found in daily environments.
The pipeline of OP-Align is shown in Fig. 2. At the object-level phase, OP-
Align initially employs Efficient SE(3)-equivariant Point Net (E2PN) [44] for
object-level pose selection from a discretization of the SE(3) group, and generate canonical reconstruction. At the part-level phase, two PointNets (PNs) [32]
with shared weights perform part segmentation and joint parameters estimation separately for the input aligned with object-level pose and the canonical
reconstruction.Theobtainedjointparametersgeneratethepart-levelalignment
between the input and the canonical reconstruction, aligning each part of the

<!-- Page 5 -->

OP-Align: Object-level and Part-level Alignment 5
Object-level Phase Part-level Phase

### 𝑿 𝑹o𝑿+𝒕o


### Object-level

Aligned Input

### 𝑾x

E2PN P O os b e je S c e t l - e le c v ti e o l n N P 𝒁

### Joint

Parameters
Po

## M

se
a

## H

x
e
-p
a
o
d
o

## (𝑭

lin
eq
g
v)
{𝑹i,𝒕 Po i se |i C ∈ an 1 di , d 2 a , t … es ,60}
sthgieW
derahS
𝒂
𝒂
x
y
,
,
𝒄
𝒄
x
y
,
,
𝒅
𝒅
x
y

## A


## P

l
a
ig
rt
n
-
m
le
e
ve
n
l
t
𝑹d,𝑹a,𝑻a Red Part Aligned

## 𝒀

ReconHead(𝒇inv) Green Part Aligned

## N


### P Part-level

Aligned Inputs
Adding
𝒀base
Rec

## C

o
a
n
n
s
o
t
n
ru
ic
c
a
t
l
ion
𝑾y
Se

## P

g
r
m
ob
e
a
n
b
t
i
a
li
t
t
i
y
on
Fig.2: Pipeline of OP-Align. At the object-level phase, for the input point cloud X,
we use the E2PN [44] backbone to predict and select object-level pose R o ,t o from
pose candidates, and generate the canonical reconstruction Y by adding a learnable
parameter called category-common base shape Y base. At the part-level phase, two
PointNets[32]withsharedweightspredictthepartsegmentationprobabilityW x ,W y,
jointstatesa x ,a y,jointpivotsc x ,c y,andjointdirectionsd x ,d yforobject-levelaligned
inputR o X+t oandreconstructionY,togeneratepart-levelalignmentR d ,R a ,T athat
aligns each part of X to the corresponding part of Y as part-level aligned inputs Z.
input with its corresponding part of the reconstruction by simulating the joint
movement.
In Section 3.1, we will introduce the concept of object-level and part-level
alignment and the required weighted point cloud distance for training. Then
we will introduce the object-level phase and part-level phase of our model in
Section 3.2 and Section 3.3.
Notice in this section, for a rank n tensor A, we denote the (i ,i ,...,i )-
1 2 n
element (a rank 0-tensor) as A . Moreover, we use NumPy [7] like no-
[i1,i2,...,in]
tation to extract a tensor from A (but each index starts from 1). For example,
A denote the i -th rank (n 1) tensor along the first axis and A denote
[i1] 1
−
[:,i2]
the i -th rank (n 1) tensor along the second axis.
2
−
3.1 Preliminaries
Expansion from rigid objects to articulated objects To solve the rigid
object pose estimation in a self-supervised manner, SE(3)-eSCOPE [21] utilizes
a SE(3)-equivariant backbone to disentangle shape and pose by generating an
SE(3)-invariant shape reconstruction and selecting SE(3)-equivariant pose from
candidates in a discretization of the SE(3) group for aligning the reconstruction
and input. They observed that poses of SE(3)-invariant reconstructions for ob-

<!-- Page 6 -->

6 Y. Che et al.
(a)
(b)
Arbitrary Holistic Object-level Red Part Green Part Part-level Category-common Canonical
Inputs Aligned Aligned Inputs Aligned Aligned Aligned Inputs Base Shape Reconstructions

### Object-level Alignment Part-level Alignment Reconstruction

Fig.3: Illustration of the object-level alignment, part-level alignment, and the reconstruction of two inputs (a) and (b). Object-level alignment aligns the inputs with the
canonical reconstructions holistically. Part-level alignment simulates joint movement
toaligneachpart.Thecategory-commonbaseshaperemainsconsistentforallinputs,
and the canonical reconstruction further fits the shape details of each input.
jectsinthesamecategoryareoftenconsistentlyaligned.However,forarticulated
objects, each part’s pose is also influenced by joint movement. This complexity
renders the reconstruction generated by the SE(3)-eSCOPE unable to maintain
consistent poses for all the parts.
To extend such an approach to articulated objects, as depicted in Fig. 3, we
use object-level alignment to reduce the overall pose variance, part-level alignment to simulate joint movement and align each part, and generate reconstruction with canonical pose and joint state for any objects. Specifically, For objectlevel alignment, we use a similar strategy with SE(3)-eSCOPE, by selecting the
posegeneratingthesmallestpointclouddistancebetweenthereconstructionand
input, among multiple pose candidates, in other words, anchors. For part-level
alignment,wecollectivelyaligneachpartoftheinputtothecorrespondingpart
ofthereconstructionbyaligningjointdirectionandpivot,thenrotate/translate
the input along the joint direction, to obtain multiple part-level aligned inputs
each of which is aligned only with the corresponding part of the reconstruction. It is essential to note that each part-level aligned input also leaves other
partsunaligned.Weusethisphenomenonandcalculateeachpoint’sdistancebetweeneachpart-levelalignedinputandthereconstructiontodeterminewhether
a point in each part-level aligned input belongs to the currently aligned part
which guides the part segmentation learning. To stabilize the reconstruction,
we add a category-common base shape as learnable parameters to represent a
common shape of all the objects in the same category.
WeightedPointCloudDistances Wecombinepartsegmentationprobability
with the point cloud distance between the part-level aligned inputs and the
reconstructiontolearnpartsegmentationandpartalignmentsimultaneously.To
achievethis,weuseweightedpointclouddistances,andlater,partsegmentation
probability will sometimes be set as weights. A commonly used point cloud
distance is the chamfer distance (CD), and we also employ the Density-awarded
Chamfer Distance (DCD) [42]. Given two point clouds P and Q, the single-

<!-- Page 7 -->


### OP-Align: Object-level and Part-level Alignment 7

directional weighted CD (L1) and DCD from P to Q with the weight w are
defined as

## P

1 | |

### CD(P,Q,w)= w min P Q ,

P [n] m 1,2,...,Q [n] − [m]
| |n=1 ∈{ | |}
X (cid:13) (cid:13) (1)
P (cid:13) (cid:13)
1 | |
DCD(P,Q,w,α)=

## P

w
[n] m 1
m
,2,
i
.
n

## ..,Q

1
−
e− α
∥
P[n]− Q[m]∥2 .
| |n X =1 ∈{ | |}(cid:16) (cid:17)
The sensitive distance range of DCD can be adjusted with the hyper-parameter
α.
3.2 Object-level phase
In the Object-level phase, OP-Align performs object-level pose selection, following a methodology similar to SE(3)-eSCOPE [21], and generate canonical
reconstruction.
By feeding the input X, E2PN [44] backbone initially outputs the SE(3)-
equivariant feature F eqv R D × 60. This feature is generated by 60 anchors rep-
∈
resenting different poses of the object. Here, 60 is the number of elements of
the icosahedral rotation group, a discretization of the 3D rotation group SO(3).
Then, we max pool F among anchor dimension to obtain a SE(3)-invariant
eqv
featuref inv R D.WeusePoseHead,consistingofmulti-layerperceptron(MLP),
∈
tooutputper-anchorrotationandtranslation (R ,t )=PoseHead(F )
[i] [i] eqv[:,i]
{ |
i 1,2,...,60 . To obtain the canonical reconstruction Y R 3 × N, we also
∈ { }} ∈
useanMLPcalledReconHeadandalearnableparameterY whichrepresents
base
the category-common base shape and is of the same size as Y. The canonical
reconstruction Y is obtained by adding the output of ReconHead and Y ;
base
Y =ReconHead(f )+Y .
inv base
We also need to select the correct object-level pose from per-anchor rotation
and translation (R ,t ) . We calculate the single-directional CD between
[i] [i]
{ }
the input transformed by the rotation and the translation of each anchor and
the reconstruction. Then we select the anchor’s rotation and translation that
minimize CD as an object-level pose;
R , t = argmin CD(R X+t ,Y,1), (2)
o o [i] [i]
i 1,2,...,60
∈{ }
where1representsthevectorwithallelementsequalto1.Noticethatwedonot
expecttheobject-levelposeR ,t obtainedheretobeaccuratebecausewehave
o o
not considered joint movement in this phase of the model. However, R , t can
o o
reduce the overall pose variance for subsequent non-SE(3)-equivariant model’s
inputs by applying R X+t as object-level aligned input.
o o
Object-level Losses We employ DCD as the object-level reconstruction loss
=DCD(R X+t ,Y,1,α )+DCD(Y,R X+t ,1,α ), (3)
o o o L o o R

## L


<!-- Page 8 -->

8 Y. Che et al.
where α =30 and α =120.

## L R

Inaddition,tworegularizationlossesareintroducedtomakereconstructions
more stable. The first one is for shape variance between category-common base
shape Y and canonical reconstruction Y and is defined by
base

## N

1

## = Y Y . (4)

L regS N [i] − base[i] 2
i=1

### X(cid:13) (cid:13)

Thesecondoneisalocaldensityregula(cid:13)rizationtoensu(cid:13)rethereconstructiondoes
not contain outliers and avoids sparse density in certain parts. It is defined by

## K

1
= Var( Y KNN(Y,k) ), (5)
regD

## L K 1 ∥ − ∥

− i=2

## X

where KNN(Y,k) refers to the k-th nearest point from each point in Y, and we
set K =64 in this paper.
3.3 Part-level phase
Inthisphase,wefocusonsegmentingboththeobject-levelalignedinputandthe
reconstruction into parts and estimating their joint parameters. By comparing
theobtainedjointpivots,jointdirections,andjointstates,wedeterminetherelativeposetransformationstoaligneachpartoftheinputwiththecorresponding
part of the reconstruction.
OP-Align uses two PNs [32] with shared weights to process the object-level
aligned input R X+t and the reconstruction Y separately. These two PNs
o o
output the segmentation probabilities W x ,W y R P × N, joint pivots c x ,c y
∈ ∈
R (P − 1) × 3, joint directions d x ,d y R (P − 1) × 3 and per-part joint states a x ,a y
∈ ∈
R (P − 1) × 2fromeachjoint,wheresubscriptsxandyindicateoutputsfromR o X+
t and Y respectively. Here, joint state a represents joint angles for revolute
o
∗
joints and translation lengths for prismatic joints, and the dimension of the
second axis of R (P − 1) × 2 reflects the assumption that each joint connect two
parts. We define the part-level aligned inputs Z , j =1,2,...,P 1, i=1,2,
[j,i]
−
obtained by a relative transformation that aligns the i-th part connected to the
j-th joint of R X+t with the corresponding part of Y by
o o
R R ((R X+t ) c )+c (revolute joint),
Z = a[j,i] d[j] o o − x[j] y[j] (6)
[j,i]

## (R

d[j]

## ((R

o
X+t
o
) c
x[j]
)+c
y[j]

## +T

a[j,i]
(prismatic joint).
−
Here, R is a rotation matrix of the joint direction alignment that sends the
d[j]
joint direction d to d ; R d = d . R is the rotation matrix
x[j] y[j] d[j] x[j] y[j] a[j,i]
of joint state alignment, the rotation of a revolute joint with rotation angle
a a around the axis d . And T is the joint state alignment
y[j,i] x[j,i] y[j] a[j,i]
−
translation d (a a ) which represents a translation of a prismatic
y[j] y[j,i] x[j,i]
−
joint. The illustration of such alignments are shown in Fig. 4. By applying the
above equation to each part, OP-Align generates a point cloud set, part-level
aligned inputs Z = Z i 1,2 ,j 1,2,...,P 1 where each part of
[j,i]
{ | ∈ { } ∈ { − }}
the input X is aligned to the corresponding part of the reconstruction Y.

<!-- Page 9 -->

OP-Align: Object-level and Part-level Alignment 9

### 𝑹d 𝑹a 𝑻a

Joint Direction Alignment Joint State Alignment (Revolute) Joint State Alignment (Prismatic)
Fig.4: Illustration of joint direction alignment R d, joint state alignment R a that
simulatingrevolutejointmovement,andt a thatsimulatingprismaticjointmovement.
Corresponding part assignment Objects with more than two parts, such
as eyeglasses or basket, have some shared parts, each of which is connected
withmultiplejoints.Thesesharedpartsresultinthenumberofpart-levelaligned
inputs Z notnecessarilybeingthesameasthenumberofpartsP.Tocorrelate
| |
Z with part segmentation probability, we assign one part label σ(j,i) to each
pair of a joint j and a part i connected to this joint, j = 1,2,...,P 1, i =
−
1,2. We require the assignment σ to satisfy two conditions: (1) for any j
∈
1,2,...,P 1 σ(j,1)=σ(j,2) and (2) for any p 1,2,...,P there exist j
{ − } ̸ ∈{ }
and i such that σ(j,i) = p. Let σ be the assignment that minimizes the (sum
of)segmentation-weightedCDcalculatedby 1 CD(Z ,Y,W )
j i b[j,i] [j,i] x[σ(j,i)]
among all possible assignments satisfying (1) and (2). Here b denotes the

### P P [j,i]

number of times the part σ(j,i) is shared. During the inference phase, we use
the mean translation by linear interpretation and the mean rotation by the
spherical linear interpolation (SLERP) as the shared part’s pose.
Part-level Losses We employ a segmentation-weighted DCD as the part-level
reconstruction loss

## P 1 2

− 1
= (DCD(Z ,Y,W ,α )+DCD(Y,Z ,W ,α )).
L p b [j,i] x[σ(j,i)] L [j,i] y[σ(j,i)] R
[j,i]
j=1 i=1

## Xx

(7)
We also add some regularization. We assume that the mean segmentation
probabilityofeachpartexceedsthethresholdβ inthereconstructionandapply
the segmentation regularization by

## 1 P N W

= max β i=1 y[p,i] ,0 , (8)
regW
L P p=1 − P N !

## X

whereβissetto0.05.weconsiderthatthepart-levelalignedinputsofoneshared
part should coincide and introduce a regularization loss ;
regP

## L


## P 1 2

1 −

## = Z Z , (9)

L regP 2(P 1) [j,i] − [j,i] 2
− j=1 i=1
XX(cid:13) (cid:13)
(cid:13) (cid:13)
where Z indicates the mean shape of Z σ(a,b)=σ(j,i) . And since the
[j,i] [a,b]
{ | }
reconstruction should have a fixed canonical joint state, we define the recon-

<!-- Page 10 -->

10 Y. Che et al.
Table 2: Overview of the real-world dataset. The real-world dataset contains object
categories with different number of parts, number of joints, and joint types.
Training Testing Object

### Category Detection

ImageInstanceImageInstancePartJoint(prismatic)Joint(revolute)
basket 974 4 449 2 3 0 2 SAM[17]
drawer 884 4 452 2 2 1 0 SAM[17]
laptop 740 4 412 2 2 0 1 Mask-RCNN[9]
scissors 922 4 421 2 2 0 1 Mask-RCNN[9]
suitcase 813 4 381 2 2 0 1 Mask-RCNN[9]
…

### RGB-D Image &


### Segmentation Mask Basket Drawer Laptop Scissors Suitcase

Fig.5:Exampleofobjectpointcloudinthereal-worlddataset.WeuseRGB-Dimages
and object segmentation masks to back-project object point cloud.
struction Y’s joint state a as zero and apply the joint state regularization by
y

## P 1 2

1 −
= a2 . (10)
L regA 2(P 1) y[j,i]
− j=1 i=1

## Xx

Finally, since both the predicted joint pivots of the input and that of the reconstruction should be close to the object itself, we applied a regularization defined
by
=DCD(c ,Y,1,α )+DCD(c ,R X+t ,1,α ), (11)
regJ y[j] L x[j] o o R

## L

as the joint pivot regularization.
4 Real-world Dataset
To evaluate the performance of OP-Align in real-world scenarios, we introduce
our novel real-world dataset. The real-world dataset contains 5 categories of
articulated objects, basket, laptop, suitcase, drawer, and scissors, captured by ASUS Xtion RGB-D camera. For each category, we randomly select
4 objects for training and 2 objects for testing. For each object, we set 8 random joint states and captured about 30 frames of RGB-D images for each. We
also generated object segmentation masks predicted with detection models such
as Mask-RCNN [9] or Segment Anything Model (SAM) [17]. The object point
cloud can be generated by combining the depth channel of RGB-D images with
a segmentation mask. Tab. 2 and Fig. 5 show an overview of this dataset. The
annotationofthereal-worlddatasetincludeseachpart’ssegmentation,rotation,
and translation and each joint’s pivot and direction.

<!-- Page 11 -->

OP-Align: Object-level and Part-level Alignment 11
5 Experiments
Datasets: We use a synthetic dataset generated by authors of EAP [24] and
our real-world dataset for evaluation. The synthetic dataset contains laptop,
safe, oven, washer, and eyeglasses categories, selected from the mesh data
in HOI4D [25] and Shape2Motion [40] dataset. We follow EAP [24]’s authors to
render these mesh data into the partially observed point cloud, simulating the
point cloud observation from a single-view camera.
Baselines: For the synthetic dataset, we choose EAP [24] and 3DGCN [22] as
self-supervised and supervised method baselines. We also report the results of
a ICP algorithm, and NPCS [20] with EPN [3] backbone, which the authors of
EAP [24] implemented. For the real-world dataset, we trained 3DGCN [22] and
PointNet++ [33] as supervised method baselines.
Evaluation Metrics:Forthesyntheticdataset,wefollowEAP[24]andreport
themeanvaluesofsegmentationIoU,partrotationerror,parttranslationerror,
joint direction error, and the distance from a point to a line as joint pivot error.
For the real-world dataset, we follow category-level 6D object pose estimation
methods [4,6,39] and choose the mean average precision (mAP) with multiple
thresholds. An instance’s part pose is considered correct if the mean translation
androtationerrorofeachpartarebothbelowthegiventhresholds.Specifically,
we use thresholds 5,10,15cm for translation, and 5 ◦ ,10 ◦ ,15 ◦ for rotation. We
also use the same thresholds for joint pivot and direction. For part segmentation, we use the mean value of intersection over union (IoU) of each part and
thresholds of 75%,50% as metrics.
Evaluation Strategies: Because OP-Align is a self-supervised model, it only
predicts the relative poses of the input and the reconstruction instead of the
poses defined by humans. Therefore, to evaluate our model’s performance, we
needtodeterminetheposesofthereconstructionparts.Toachievethis,wefollow
EAP [24] and utilize ground truth labels from the training set. In preparation,
for each training data and each part, a relative pose between the reconstruction
and the input is obtained through Equation 6 by using a trained model, which,
in combination with the ground truth pose, derives an estimated pose of each
part of the reconstruction. We use these estimated poses to determine one common pose for each part of the reconstruction via a RANSAC-based method. For
evaluation, we use the common pose as the pose of each part of the reconstruction. See supplement material for more details. We also note that for symmetric
objectcategoriessuchasbasket,laptop,scissorsandsuitcase,thepartsegmentationiseasilyreplacedwitheachother.Foreachobject,amongallpossible
permutations of indices of segmentation labels, we choose the permutation with
thelargestmeanIoUoverparts.Theposesofpartsarealsopermutedaccording
to the chosen permutation.
Training Settings: We trained a model for each category for 20,000 iterations
with a batch size of 24. We used the Adam optimizer with a learning rate of
0.0001 and halved the learning rate every 5,000 iterations. The total loss is
defined as λ +λ +λ +λ +λ +λ +
o o p p regS regS regD regD regW regW regP regP

## L L L L L L

λ +λ , where (λ ,λ ,λ ,λ ,λ ,λ ,λ ,λ ) =
regA regA regJ regJ o p regS regD regW regP regA regJ

## L L


<!-- Page 12 -->

12 Y. Che et al.
Table 3: The mean metrics on partially observed point cloud from the synthetic
dataset. Supervision refers to the annotations used in training.
Supervision SegmentationRotationTranslation Pivot DirectionMemory Speed

### Method

PoseSegmentationJoint IoU↑ (degree)↓ ↓ ↓ (degree)↓ (GB)↓ (FPS)↑
3DGCN[22] ✓ ✓ ✓ 94.05 11.61 0.093 0.084 9.78 - -
NPCS-EPN[20] ✓ ✓ ✓ - 11.05 0.080 0.147 15.20 - -

## Icp ✓ 66.45 44.12 0.242 - - - -


## Eap[24] 68.46 10.44 0.121 0.162 23.09 9.23 <1

Ours 80.70 8.10 0.129 0.110 6.63 2.31 41

### Object-level

Aligned Input

### Part-level

Aligned Inputs

### Reconstruction

Laptop Safe Oven Washer Eyeglasses Basket Drawer Laptop Scissors Suitcase

### Synthetic Dataset Real-world Dataset

Fig.6: Visualization of object-level aligned inputs, part-level aligned inputs, and reconstructionsofOP-Alignonthesyntheticdataset(left)andtwotestinginstanceson
thereal-worlddatasetineachcategory(right).Segmentationisindicatedbycolor,and
joints are indicated by black arrow.
(10,10,100,10,10,10,10,10). We randomly sample 1024 points without RGB
information from each object as input.
5.1 Results on the Synthetic Dataset
We compare the performance of OP-Align on the partially observed point cloud
from the synthetic dataset with other methods. As the results in Tab. 3, OP-
Align exceeds other self-supervised methods by a large margin on multiple metrics. These results show that OP-Align can provide accurate joint and part pose
predictionalongwithpartsegmentation.ThevisualizationshowninFig.6(left)
demonstratesthatobject-levelalignmentcanaligntheinputwithreconstruction
holistically,andpart-levelalignmentcanaligneachpartoftheinputwiththecorrespondingpartofthereconstruction.Also,thankstotheobject-levelalignment
for reducing the pose variance, our method achieved higher part segmentation
performance when compared with EAP [24]. However, the part segmentation
performance still has room for improvement. Our assumption is that supervised
3DGCN[22]candirectlylearnsegmentationwiththegeometricfeaturefromthe
point cloud, while OP-Align leverages the difference of point distance between
each part-level aligned input and the reconstruction for the indirect learning of
segmentation probability with . Especially in the region close to the joint,
p

## L

where points of part-level aligned inputs easily overlap, the point distance had
no significant difference between each part-level aligned input, resulting in suboptimal segmentation performance. We also compared our model in terms of

<!-- Page 13 -->


### OP-Align: Object-level and Part-level Alignment 13

Table4:ThecomparisonofmAPmetricsonthereal-worlddataset.Supervision refers
to the annotations used in training.
Supervision Segmentation↑ Joint↑ Part↑

### Method

PoseSegmentationJointIoU75%IoU50%5◦5cm10◦10cm15◦15cm5◦5cm10◦10cm15◦15cm
3DGCN[22] ✓ ✓ ✓ 83.31 95.83 47.51 85.79 94.59 13.07 46.77 68.66
PointNet++[33] ✓ ✓ ✓ 19.83 42.20 21.06 57.38 75.56 4.47 23.25 39.82

### Ours 23.79 50.42 12.57 63.59 74.04 14.79 46.09 59.76

Fig.7: The comparison of mAP metrics on the real-world dataset.
inference speed and GPU memory with EAP [24]. OP-Align utilizes less GPU
memory and achieves faster inference speed.
5.2 Results on the Real-world Dataset
We conduct self-supervised training for OP-Align and compared the result with
supervised 3DGCN [22] and PointNet++ [33] on the real-world dataset. The
results are shown in Tab. 4 and Fig. 7 and the visualization is shown in Fig. 6
(right).OP-AlignachievesresultsbetterthanorcomparabletoPointNet++[33]
on all the metrics, and results comparable to 3DGCN [22] on part metrics, even
withoutanyannotations.However,similartotheresultsonthesyntheticdataset,
part segmentation learning with requires accurate point distance between
p

## L

part-level aligned inputs and the reconstruction, which is extremely challenging
in real-world environments where outliers and missing points commonly exist.
We also notice that our model still lags behind supervised methods in terms of
the joint pivot and part translation metrics, as shown in laptop and suitcase
visualization in Fig. 6. This phenomenon may be because the predicted joint
pivots by our model, while capable of achieving part-level alignment, may not
necessarily overlap with the actual joint pivots in reality. This also affects the
performance of part translation based on joint movement.
5.3 Ablation Studies
We conduct four different ablation experiments on the real-world dataset, related to the shape variance regularization , the reconstruction density regregS

## L

ularization , the segmentation regularization , and the joint pivot
regD regW

## L L

regularization , as shown in Tab. 5. Examples of the reconstructions of
regJ

## L

objects in the real-world dataset laptop category are shown in Fig. 8. As the

<!-- Page 14 -->

14 Y. Che et al.

### Segmentation↑ Joint↑ Part↑

LregSLregDLregWLregJ 50% 15◦15cm15◦15cm
(a) ✓ ✓ ✓ 51.87 42.79 35.39
(b) ✓ ✓ ✓ 50.36 51.52 32.15
(c) ✓ ✓ ✓ 39.73 32.49 27.51
(a) (b)
(d) ✓ ✓ ✓ 47.52 36.27 20.49
Full ✓ ✓ ✓ ✓ 50.42 74.04 59.76

### Fig.8: Reconstruction examples

Table 5: Results of ablation studies. of ablation model (a) and (b).
reconstructions and performance of ablation model (a) show, without , the
regS

## L

reconstructions’jointstateisnotfixed,whichresultsinahugeperformancedrop
at metrics of joint and part prediction. For ablation model (b), without ,
regD

## L

reconstruction’s points are concentrated into a small region, which affects the
overall performance of our model. For ablation model (c), without , some
regW

## L

objects are regarded as single-part objects, and we fail to generate valid joint
parameters. Finally for ablation model (d), without , joint pivot may be
regJ

## L

placed outside of the object, resulting in poor performance on both joint and
part pose metrics.
6 Failure Cases and Limitations
FailureCases:WefoundthatOP-Alignfailsforobjectsbelongingtocategories
where some parts comprise only a small fraction of the entire object and their
movementdoesnotsignificantlyaffecttheoverallshape.Forbasketcategory,as
showninFig.6,thehandlepartsaccountfor16.9%oftheentireobject(median
in the testing set) and the movement of these parts results in small changes
to the overall shape. This means that even without part-level alignment, our
canonicalreconstructionissufficientlyclosetotheoverallobject.Thisalsoleads
toourmodel’sinabilitytocorrectlysegmentpartsandpredictjointmovements.
Limitations: OP-Align requires the number of parts and joint types as known
information, which limits its ability to learn from objects in categories with
unknown joint types or variable numbers of joints and parts.
7 Conclusion
We proposed a novel approach, OP-Align, and a new real-world dataset for the
self-supervised category-level articulated object pose estimation. Our approach
achieves state-of-the-art performance among self-supervised methods and comparable performance to previous supervised methods, yet with real-time inference speed. Our future plan is to design a self-supervised universal pose estimation model, which can be trained with inner-category data and automatically
detect the number of parts, number of joints, and joint type.
Acknowledgements: We thank Ryutaro Yamauchi and Tatsushi Matsubayashi from ALBERT Inc. (now Accenture Japan Ltd.) for their insightful suggestions and support. This work was supported by JST FOREST Program,
Grant Number JPMJFR206H.

<!-- Page 15 -->

OP-Align: Object-level and Part-level Alignment 15

### References


## Abbatematteo,B.,Tellex,S.,Konidaris,G.:Learningtogeneralizekinematicmodels to novel objects. In: Proceedings of the 3rd Conference on Robot Learning

(2019)

## Chang, A.X., Funkhouser, T., Guibas, L., Hanrahan, P., Huang, Q., Li, Z.,

Savarese, S., Savva, M., Song, S., Su, H., et al.: Shapenet: An information-rich
3d model repository. arXiv preprint arXiv:1512.03012 (2015)

## Chen, H., Liu, S., Chen, W., Li, H., Hill, R.: Equivariant point network for 3d

pointcloudanalysis.In:IEEEConf.Comput.Vis.PatternRecog.pp.14514–14523
(2021)

## Chen, W., Jia, X., Chang, H.J., Duan, J., Shen, L., Leonardis, A.: Fs-net: Fast

shape-based network for category-level 6d object pose estimation with decoupled
rotation mechanism. In: IEEE Conf. Comput. Vis. Pattern Recog. pp. 1581–1590
(2021)

## Chu, R., Liu, Z., Ye, X., Tan, X., Qi, X., Fu, C.W., Jia, J.: Command-driven

articulatedobjectunderstandingandmanipulation.In:IEEEConf.Comput.Vis.

### Pattern Recog. pp. 8813–8823 (2023)


## Di,Y.,Zhang,R.,Lou,Z.,Manhardt,F.,Ji,X.,Navab,N.,Tombari,F.:Gpv-pose:

Category-level object pose estimation via geometry-guided point-wise voting. In:

### IEEE Conf. Comput. Vis. Pattern Recog. pp. 6781–6791 (2022)


## Harris,C.R.,Millman,K.J.,vanderWalt,S.J.,Gommers,R.,Virtanen,P.,Cournapeau, D., Wieser, E., Taylor, J., Berg, S., Smith, N.J., Kern, R., Picus, M.,

Hoyer, S., van Kerkwijk, M.H., Brett, M., Haldane, A., del Río, J.F., Wiebe, M.,
Peterson, P., Gérard-Marchant, P., Sheppard, K., Reddy, T., Weckesser, W., Abbasi, H., Gohlke, C., Oliphant, T.E.: Array programming with NumPy. Nature
585(7825), 357–362 (Sep 2020). https://doi.org/10.1038/s41586-020-2649-2,
https://doi.org/10.1038/s41586-020-2649-2

## Hausman,K.,Niekum,S.,Osentoski,S.,Sukhatme,G.S.:Activearticulationmodel

estimation through interactive perception. In: Proceedings of IEEE International
Conference on Robotics and Automation (ICRA). pp. 3305–3312. IEEE (2015)

## He, K., Gkioxari, G., Dollár, P., Girshick, R.: Mask r-cnn. In: Int. Conf. Comput.


### Vis. pp. 2961–2969 (2017)


## Huang, J., Wang, H., Birdal, T., Sung, M., Arrigoni, F., Hu, S.M., Guibas, L.J.:

Multibodysync:Multi-bodysegmentationandmotionestimationvia3dscansynchronization. In: IEEE Conf. Comput. Vis. Pattern Recog. pp. 7108–7118 (2021)

## Insafutdinov, E., Dosovitskiy, A.: Unsupervised learning of shape and pose with

differentiable point clouds. Adv. Neural Inform. Process. Syst. 31 (2018)

## Irshad, M.Z., Kollar, T., Laskey, M., Stone, K., Kira, Z.: Centersnap: Single-shot

multi-object 3d shape reconstruction and categorical 6d pose and size estimation.
In: Proceedings of IEEE International Conference on Robotics and Automation
(ICRA). pp. 10632–10640. IEEE (2022)

## Irshad, M.Z., Zakharov, S., Ambrus, R., Kollar, T., Kira, Z., Gaidon, A.: Shapo:

Implicitrepresentationsformulti-objectshape,appearance,andposeoptimization.

### In: Eur. Conf. Comput. Vis. pp. 275–292. Springer (2022)


## Jiang, H., Mao, Y., Savva, M., Chang, A.X.: Opd: Single-view 3d openable part

detection. In: Eur. Conf. Comput. Vis. pp. 410–426. Springer (2022)

## Jiang, Z., Hsu, C.C., Zhu, Y.: Ditto: Building digital twins of articulated objects

from interaction. In: IEEE Conf. Comput. Vis. Pattern Recog. pp. 5616–5626
(2022)

<!-- Page 16 -->

16 Y. Che et al.

## Kawana, Y., Mukuta, Y., Harada, T.: Unsupervised pose-aware part decomposition for man-made articulated objects. In: Eur. Conf. Comput. Vis. pp. 558–575.


### Springer (2022)


## Kirillov, A., Mintun, E., Ravi, N., Mao, H., Rolland, C., Gustafson, L., Xiao, T.,

Whitehead, S., Berg, A.C., Lo, W.Y., et al.: Segment anything. arXiv preprint
arXiv:2304.02643 (2023)

## Lei, J., Daniilidis, K.: Cadex: Learning canonical deformation coordinate space

for dynamic surface representation via neural homeomorphism. In: IEEE Conf.

### Comput. Vis. Pattern Recog. pp. 6624–6634 (2022)


## Li,C.,Bai,J.,Hager,G.D.:Aunifiedframeworkformulti-viewmulti-classobject

pose estimation. In: Eur. Conf. Comput. Vis. pp. 254–269 (2018)

## Li, X., Wang, H., Yi, L., Guibas, L.J., Abbott, A.L., Song, S.: Category-level

articulated object pose estimation. In: IEEE Conf. Comput. Vis. Pattern Recog.
pp. 3706–3715 (2020)

## Li,X.,Weng,Y.,Yi,L.,Guibas,L.J.,Abbott,A.,Song,S.,Wang,H.:Leveraging

se(3) equivariance for self-supervised category-level object pose estimation from
point clouds. Adv. Neural Inform. Process. Syst. 34, 15370–15381 (2021)

## Lin, Z.H., Huang, S.Y., Wang, Y.C.F.: Convolution in the cloud: Learning deformable kernels in 3d graph convolution networks for point cloud analysis. In:


### IEEE Conf. Comput. Vis. Pattern Recog. pp. 1800–1809 (2020)


## Liu, G., Sun, Q., Huang, H., Ma, C., Guo, Y., Yi, L., Huang, H., Hu, R.: Semiweakly supervised object kinematic motion prediction. In: IEEE Conf. Comput.


### Vis. Pattern Recog. pp. 21726–21735 (2023)


## Liu,X.,Zhang,J.,Hu,R.,Huang,H.,Wang,H.,Yi,L.:Self-supervisedcategorylevelarticulatedobjectposeestimationwithpart-levelse(3)equivariance.In:Int.


### Conf. Learn. Represent. (2023)


## Liu,Y.,Liu,Y.,Jiang,C.,Lyu,K.,Wan,W.,Shen,H.,Liang,B.,Fu,Z.,Wang,H.,

Yi,L.:Hoi4d:A4degocentricdatasetforcategory-levelhuman-objectinteraction.
In: IEEE Conf. Comput. Vis. Pattern Recog. pp. 21013–21022 (2022)

## Locatello, F., Weissenborn, D., Unterthiner, T., Mahendran, A., Heigold, G.,

Uszkoreit, J., Dosovitskiy, A., Kipf, T.: Object-centric learning with slot attention. Adv. Neural Inform. Process. Syst. 33, 11525–11538 (2020)

## Mescheder, L., Oechsle, M., Niemeyer, M., Nowozin, S., Geiger, A.: Occupancy

networks: Learning 3d reconstruction in function space. In: IEEE Conf. Comput.

### Vis. Pattern Recog. pp. 4460–4470 (2019)


## Mo, K., Zhu, S., Chang, A.X., Yi, L., Tripathi, S., Guibas, L.J., Su, H.: Partnet:Alarge-scalebenchmarkforfine-grainedandhierarchicalpart-level3dobject

understanding. In: IEEE Conf. Comput. Vis. Pattern Recog. pp. 909–918 (2019)

## Mu, J., Qiu, W., Kortylewski, A., Yuille, A., Vasconcelos, N., Wang, X.: A-sdf:

Learning disentangled signed distance functions for articulated shape representation. In: Int. Conf. Comput. Vis. pp. 13001–13011 (2021)

## Park,J.J.,Florence,P.,Straub,J.,Newcombe,R.,Lovegrove,S.:Deepsdf:Learning continuous signed distance functions for shape representation. In: IEEE Conf.


### Comput. Vis. Pattern Recog. pp. 165–174 (2019)


## Paschalidou,D.,Katharopoulos,A.,Geiger,A.,Fidler,S.:Neuralparts:Learning

expressive 3d shape abstractions with invertible neural networks. In: IEEE Conf.

### Comput. Vis. Pattern Recog. pp. 3204–3215 (2021)


## Qi, C.R., Su, H., Mo, K., Guibas, L.J.: Pointnet: Deep learning on point sets for

3d classification and segmentation. In: IEEE Conf. Comput. Vis. Pattern Recog.
pp. 652–660 (2017)

<!-- Page 17 -->


### OP-Align: Object-level and Part-level Alignment 17


## Qi,C.R.,Yi,L.,Su,H.,Guibas,L.J.:Pointnet++:Deephierarchicalfeaturelearning on point sets in a metric space. Advances in neural information processing

systems 30 (2017)

## Segal, A., Haehnel, D., Thrun, S.: Generalized-icp. In: Robotics: science and systems. vol. 2, p. 435. Seattle, WA (2009)


## Shi, Y., Cao, X., Zhou, B.: Self-supervised learning of part mobility from point

cloudsequence.In:ComputerGraphicsForum.vol.40,pp.104–116.WileyOnline

### Library (2021)


## Sundermeyer,M.,Marton,Z.C.,Durner,M.,Triebel,R.:Augmentedautoencoders:

Implicit3dorientationlearningfor6dobjectdetection.Int.J.Comput.Vis.128,
714–729 (2020)

## Tian,M.,Ang,M.H.,Lee,G.H.:Shapepriordeformationforcategorical6dobject

pose and size estimation. In: Eur. Conf. Comput. Vis. (2020)

## Wang, G., Manhardt, F., Shao, J., Ji, X., Navab, N., Tombari, F.: Self6d: Selfsupervised monocular 6d object pose estimation. In: Eur. Conf. Comput. Vis. pp.

108–125. Springer (2020)

## Wang, H., Sridhar, S., Huang, J., Valentin, J., Song, S., Guibas, L.J.: Normalized

object coordinate space for category-level 6d object pose and size estimation. In:

### IEEE Conf. Comput. Vis. Pattern Recog. pp. 2642–2651 (2019)


## Wang, X., Zhou, B., Shi, Y., Chen, X., Zhao, Q., Xu, K.: Shape2motion: Joint

analysis of motion parts and attributes from 3d shapes. In: IEEE Conf. Comput.

### Vis. Pattern Recog. pp. 8876–8884 (2019)


## Weng, Y., Wang, H., Zhou, Q., Qin, Y., Duan, Y., Fan, Q., Chen, B., Su, H.,

Guibas,L.J.:Captra:Category-levelposetrackingforrigidandarticulatedobjects
from point clouds. In: Int. Conf. Comput. Vis. pp. 13209–13218 (2021)

## Wu, T., Pan, L., Zhang, J., Wang, T., Liu, Z., Lin, D.: Density-aware chamfer

distance as a comprehensive metric for point cloud completion. arXiv preprint
arXiv:2111.12702 (2021)

## Xiang, F., Qin, Y., Mo, K., Xia, Y., Zhu, H., Liu, F., Liu, M., Jiang, H., Yuan,

Y., Wang, H., Yi, L., Chang, A.X., Guibas, L.J., Su, H.: SAPIEN: A simulated
part-based interactive environment. In: IEEE Conf. Comput. Vis. Pattern Recog.
(June 2020)

## Zhu, M., Ghaffari, M., Clark, W.A., Peng, H.: E2pn: Efficient se (3)-equivariant

pointnetwork.In:IEEEConf.Comput.Vis.PatternRecog.pp.1223–1232(2023)

<!-- Page 18 -->


### Supplementary Material of OP-Align:


### Object-level and Part-level Alignment for

Self-supervised Category-level Articulated Object

### Pose Estimation

Yuchen Che1 , Ryo Furukawa2 , and Asako Kanezaki1
1 Tokyo Institute of Technology, Tokyo, Japan
cheyuchen.titech@gmail.com, kanezaki@c.titech.ac.jp
2 Accenture Japan Ltd, Tokyo, Japan
rfurukaward@gmail.com
1 Model Details
In this section, we discuss the details of our model and its implementation.
1.1 Architecture
OP-Align model consists of the object-level phase based on E2PN [17], and the
part-level phase based on PointNet (PN) [13]. The pipeline of the object-level
phase is shown in Fig. 1, and the part-level phase is shown in Fig. 2.
Object-level Phase Fig. 1, OP-Align outputs object-level rotation and translation candidates (R ,t ) i 1,2,...,60 and also generates a canonical
[i] [i]
{ | ∈ { }}
reconstruction Y. While this approach is similar to SE(3)-eSCOPE [8], we replacethebackbonefromEPN[1]toE2PN[17]forefficiencyandalsomodifiedthe
laterstage,especiallyafterPoseHeadandReconHead.WeuseamodifiedKernel
Point Convolution (KPConv) module with only 12 anchors (discretization of S2
group) to conduct point convolution and sample points, and a symmetric kernel
forefficientfeaturegathering,whichexpandthe12anchorsinto60anchors(discretization of SO(3) group) by feature permutation. Please refer to E2PN [17]
paperformoredetails.WegenerateSE(3)-equivariantfeatureF bysuchmodeqv
ules,andmax-poolingalongtheanchordimensiontoobtainSE(3)-invariantfeaturef .WethenuseF andamulti-layerperceptron(MLP)basedPoseHead
inv eqv
to generate 60 candidate rotations and translations. In practice, the rotation is
the product of the inherent rotation matrix of each anchor R and the residanc
ual rotation matrix transformed from rotation vector predicted by PoseHead.
We follow SE(3)-eSCOPE [8] in restricting the rotation angle of the residual rotation matrix 0.2π to avoid overlapping. Plase refer to SE(3)-eSCOPE [8] for
≤
moredetails.ThereconstructionisgeneratedbyaddingtheresultofMLP-based
ReconHead and the learnable parameter, category-common base shape Y .
base
4202
guA
92
]VC.sc[
1v74561.8042:viXra

<!-- Page 19 -->

2 Y. Che et al.
3×1024

## 𝑿

K ( P 3 C 2 o , 2 n ) v {𝒕i|i∈1,2,…,60} 3×60 {𝑹i|i∈1,2,…,6 3 0 × } 3×60 𝒀 3×1024
32×512×12

### Matrix Adding

KPConv Concat 480×12 V R e o c t t a o t r io t n o Multiplication
(64, 2) 64×256×12 Matrix

### 𝒀ba 3 se ×1024

K (1 P 2 C 8 o , n 2 v ) 128×128×12 PoseHead Inher 𝑹 en a t n c R 3 o × t 3 at × io 6 n 0 ReconHead

### Matrix of Each Anchor

K (2 P 5 C 6 o , n 2 v ) 256×64×12 Permutation 512×60 512

### 𝑭eqv 𝒇inv


### Max-pooling Max-pooling


### Along Points Along Anchors

Fig.1:PipelineofOP-Align’sobject-levelphase.TheKPConv(d,s)indicatesKPConv
withdchannels,and1/spointsampleratio,andthepermutationindicatesthefeature
gathering of E2PN. By max-pooling along point dimension of feature in each sample
level, then concatenation, an SE(3)-equivariant feature F eqv can be obtained. And we
alsousemax-poolingalongtheanchordimensiontoobtainSE(3)-invariantfeaturef inv.
F eqv isusedforthepredictionofobject-leveltranslationandrotation,andf inv isused
for the canonical reconstruction. R anc refers to inherent rotation matrix of anchors,
and Y base refers to the category-common base shape.
Part-level Phase In this phase, as shown in Fig. 2, OP-Align outputs the
segmentation probability of each point W, and the joint pivot c, direction d
and states a for each joint. Joint direction d is normalized as d = 1. Joint
| |
states a is the product of the joint range, which is set as 2π for revolute joint
3
and 20cm for prismatic joint during our experiment, and predictions that have
been applied the sigmoid function and minus 0.5.
1.2 Joint Direction and Joint State Alignment
OP-Align uses R to align the joint direction, R to align the joint state of
d a
revolute joints, and T to align the joint state of prismatic joints.
a
R refers to the rotation matrix which aligns joint directions d and
d[j] x[j]
d . In practice, we calculate a rotation vector with the rotation direction of
y[j]
the cross-product of joint directions, and the rotation angle subtended by the
arc of joint directions, represented as
(d d )arccos( d ,d ). (1)
x[j] y[j] x[j] y[j]
× ⟨ ⟩
We then transform this rotation vector to the rotation matrix R .
d[j]
R istherotationmatrixrepresentingtherotationofarevolutejointwith
a[j,i]
rotation angle a a around the axis d , represents as
y[j,i] x[j,i] y[j]
−
d (a a ). (2)
y[j] y[j,i] x[j,i]
−
Similar to R , we then transform this rotation vector to the rotation matrix
d

## R .

a[j,i]

<!-- Page 20 -->

OP-Align: Object-level and Part-level Alignment 3
𝑷 3×1024 for t = 1, …, 4 256 𝑾 P×1024 𝒂,𝒄,𝒅8×J

### Softmax


### Max-pooling Repeat

Along Points Concat SegHead JointHead
256×1024 512×1024 512×1024
d1vn
o C
)215
,3 (
d1vn
o C
)652
,215(
Max-pooling
512

### Along Points

Fig.2: PipelineofOP-Align’spart-levelphase.PindicateseitherreconstructionY or
object-levelalignedinputR o X+t o.Werepeat1dimensionalconvolution,andconcat
max-pooled global feature with per-point feature multiple times. The part probability
WthenbedirectlyoutputtedbyMLP-basedSegHeadwiththeper-pointfeature.The
joint parameters a,c,d are outputted by MLP-based JointHead with the max-pooled
global feature.
1.0
0.8
0.6
0.4
0.2
0.0
0.0 0.2 0.4 0.6 0.8 1.0
Distance
ssoL
10
8
6
4
2
0
0.0 0.2 0.4 0.6 0.8 1.0
Distance
tneidarG
DCD (α=10)
DCD (α=30)

### DCD (α=60)


### DCD (α=120)


### L2 Finding Nearest Neighbor

from Reconstruction to Input

### Finding Nearest Neighbor

from Input to Reconstruction
Fig.4: Illustration
of finding nearest
Fig.3: Illustration of the loss value and gradient of DCD neighbor between full
with multiple temperature parameters α and L2 distance. reconstruction (left)
DCD focuses on the learning of relatively close points, and and partially obthe sensitive distance range can be adjusted by α. served input (right).
Finally, T is the vector
a[j,i]
d (a a ), (3)
y[j] y[j,i] x[j,i]
−
which represents a translation of a prismatic joint.
1.3 Robust Point Cloud Distance
OP-Align uses Density-awarded Chamfer Distance (DCD) [15] as the main reconstruction loss function. The value of DCD of points with distance d can be
represented as 1 e − αd2 . Here, α is a temperature hyper-parameter. As shown
−
in Fig. 3, compared to normal L2 distance, DCD focuses on the learning of relatively close points, and the sensitive distance range is adjustable. DCD is a
robust point cloud distance because of such properties.
DCD enables us to conduct training by bi-directional chamfer distance between full reconstruction and partially observed input instead of the single-

<!-- Page 21 -->

4 Y. Che et al.
Fig.5: Objects in our real-world dataset.
directionalchamferdistance,whichiscommonlyusedinpreviousworks[5,8,11].
Despite the benefits of using bi-directional chamfer distance for accurately reconstructing object shape, the main drawbacks of using bi-directional chamfer
distance between full reconstruction and partially observed input, as shown in
the red arrows of Fig. 4, can be summarised into two cases

## A partially observed input may lack corresponding points of a full reconstruction,anditaffectsfindingnearestneighborsfromthereconstructionto

the input.

## A partially observed input commonly contains outliers that affect finding

the nearest neighbors from the input to the reconstruction.
Duringtheprocessoffindingthenearestneighborfromreconstructiontoinput,
we set α = 120 to reduce the effects of case 1. During the process of finding
the nearest neighbor from input to reconstruction, we set α = 30 to reduce the
effectsofcase2sinceweexpectvalidinputpointsallcanfindthecorresponding
point in the full reconstruction, which requires a larger sensitive distance range.
2 Real-world Dataset
In this section, we discuss our Real-world Dataset.
2.1 Dataset Generation

### WeusetheASUSXtionProRGB-DcameratocapturetheRGB-Dimages.The

visualization of RGB channels of images is presented in Fig. 5. We randomly

<!-- Page 22 -->


### OP-Align: Object-level and Part-level Alignment 5

place articulated objects in different environments, and for objects in each environment, we randomly set the objects in 2 different joint states. We ensure that
at least 8 joint states exist for each object. Notice due to the difficulty of label
annotation, we exclude fully closed (0 degrees for revolute joints and 0cm for
prismatic joints) joint states and the images where at least 1 part of the object
is fully unobserved.
BesidestheRGB-Dimages,wealsogeneratetheobjectsegmentationmasks,
whichseparatearticulatedobjectsandbackgroundswithdetectionmodels[4,6].
For categories contained in COCO dataset [9], such as laptop, scissors,
suitcase, we use the pre-trained Mask-RCNN [4] model. For other categories,
such as basket, drawer, we use segment anything model (SAM) [6] with manually selected 2D bounding box as the prompts.
2.2 Label Annotation
For the part segmentation annotation, instead of generating annotation solely
based on RGB images, we conduct labeling based on the point cloud directly.
For the part pose, We generate an oriented 3D bounding box and set the orientation as part rotation and the bounding box center as part translation. For the
joint directions and pivots, we draw 3d vectors directly on the point cloud for
annotating.
3 Training Settings
In this section, we represent the details of our data pre-processing, including
data normalization during both the training and testing process and data augmentation during the training process. We also explain the implements of our
baseline models.
3.1 Data Normalization & Augmentation
We employ scaling normalization and translation normalization for the input
pointcloudduringthetrainingandtestingprocess.Noticethatsuchnormalization does not require ground truth annotation and can be easily applied.
For translation, we calculate the mean coordinates of the input point cloud
andtranslatesuchcoordinatestotheorigin.Afterthetranslationnormalization,
wecalculatethemeandistancefromeachpointtotheoriginandscalesuchmean
distance to 0.5.
We also employ various data augmentation strategies during the training
process, including random rotation and Gaussian noise. We select a rotation
matrix without any restriction and apply it to the normalized input point cloud
for random rotation. For Gaussian noise, we add noise following (0, 0.001)

## N

distribution.

<!-- Page 23 -->

6 Y. Che et al.
3.2 Implementation of Baseline Models
EAP Astheonlypreviousworkthathassimilarproblemsettingstous,weselect
EAP [11] as our self-supervised method baseline. We measured the inference
speedandGPUmemoryusageofEAPwiththeirpubliclyavailablesourcecode.
However, we decided not to conduct other experiments with their source code
and to report results from their paper, since we confronted multiple difficulties
during using the code. First, EAP’s authors did not publish both the model
code for categories with prismatic joint and the dataset of drawer category
from the synthetic dataset. Second, only the model weight of laptop category
was published among all the partially observed point cloud from the synthetic
dataset.Third,thecodequalityisnotsufficientforunderstanding.Forinstance,
it lacks an explanation for all the hyper-parameters, and the model code file
itself has been replaced for different categories.
3DGCN A commonly used backbone for the category-level 6D object pose
estimation task [2,3,16] is the 3DGCN [10] model. Weimplement this backbone
with the same architecture from it in GPV-Pose [3]. For the loss functions, we
use the cross-entropy loss for the part segmentation learning, L2 distance for
part rotation, part translation, and joint direction learning. We use the squared
distance from a point to a line for the joint pivot learning.
PointNet++ As a well-known backbone for point cloud processing, we also
implement PointNet++ [14] model. We use the same architecture from it in
VoteNet [12] and the same loss function as the 3DGCN implementation.
4 Evaluation Strategies
4.1 RANSAC-based Pose Estimation
We introduce the RANSAC-based method that we used for the common pose
estimation of the reconstruction.
First, we randomly choose four samples in the training set and calculate
the mean pose (the mean rotation and translation) of each part that has been
aligned with the corresponding part of the reconstruction. Then, we calculate
errorsbetweenthemeanposesandotherestimatedposesforeachpartfromother
samples in the training set and obtain an overall error by summing these errors
over samples and parts. We repeat the above process 100 times and choose the
mean pose for each part (of some four samples), realizing the minimum overall
error, which we set as the common pose.
4.2 Prismatic Joints
We notice that joint pivots for prismatic joints do not affect joint movement
(translation alone the joint direction). Therefore, for the drawer category from
the real-world dataset, we only evaluate the average precision (AP) of joint
direction error, instead of the AP of both joint direction and joint pivot error.

<!-- Page 24 -->


### OP-Align: Object-level and Part-level Alignment 7

Table 1: Averageprecisionresultsonthereal-worlddataset.Supervision referstothe
annotations used in training.
Supervision Segmentation↑ Joint↑ Part↑

### Category Method

PoseSegmentationJoint 75% 50% 5◦5cm10◦10cm15◦15cm5◦5cm10◦10cm15◦15cm
3DGCN ✓ ✓ ✓ 67.48 92.87 38.75 84.41 93.54 1.34 20.71 44.77

### PointNet++ ✓ ✓ ✓ 0.0 6.24 3.12 31.18 57.23 0.45 1.56 13.59

Basket Ours(SJ) ✓ ✓ 83.74 98.22 60.13 91.31 95.76 0.0 18.71 51.45
Ours(S) ✓ 76.39 91.76 0.22 67.04 75.95 0.0 10.69 32.52
Ours(J) ✓ 0.0 0.0 30.29 74.39 82.85 0.0 1.34 7.57

### Ours 0.0 0.0 0.0 0.0 0.0 0.0 1.01 2.27

3DGCN ✓ ✓ ✓ 82.52 96.90 38.27 76.32 91.15 20.80 68.36 88.50
PointNet++ ✓ ✓ ✓ 3.22 40.46 16.09 42.53 64.37 8.74 42.76 65.98
Drawer Ours(SJ) ✓ ✓ 88.74 95.17 54.71 82.76 85.52 17.93 52.18 55.86
Ours(S) ✓ 91.49 97.93 29.66 79.54 88.51 18.16 76.55 84.83
Ours(J) ✓ 6.21 78.16 46.44 73.10 81.15 24.83 66.21 71.49

### Ours 3.22 54.02 9.43 54.94 81.61 7.13 70.34 80.69

3DGCN ✓ ✓ ✓ 93.20 95.87 73.30 96.12 96.60 31.31 72.57 82.03
PointNet++ ✓ ✓ ✓ 91.99 96.84 45.63 88.35 92.23 11.89 51.94 72.57
Laptop Ours(SJ) ✓ ✓ 97.82 98.54 94.17 97.33 98.06 36.17 73.54 90.53
Ours(S) ✓ 97.57 98.54 94.66 96.60 97.33 25.73 75.24 93.20
Ours(J) ✓ 89.81 98.30 82.04 93.69 95.63 12.62 54.61 80.58

### Ours 95.39 97.33 2.91 95.63 96.36 31.80 76.46 90.05

3DGCN ✓ ✓ ✓ 76.01 94.54 43.94 85.99 97.15 1.66 22.33 50.83

### PointNet++ ✓ ✓ ✓ 0.0 17.58 19.71 57.72 83.13 0.24 2.14 5.23

Scissors Ours(SJ) ✓ ✓ 94.77 99.21 53.21 97.39 99.29 38.95 64.85 65.32
Ours(S) ✓ 99.05 99.85 43.71 94.54 99.05 24.47 48.46 52.73
Ours(J) ✓ 23.76 28.98 52.25 95.49 99.05 23.04 56.53 69.83

### Ours 11.16 45.13 46.32 95.72 99.05 33.97 65.32 71.97

3DGCN ✓ ✓ ✓ 97.36 98.95 43.31 86.09 94.49 10.24 49.87 77.17
PointNet++ ✓ ✓ ✓ 3.94 49.87 20.73 66.14 80.84 1.05 17.84 41.73
Suitcase Ours(SJ) ✓ ✓ 85.04 94.75 44.62 69.82 85.04 0.26 16.54 51.71
Ours(S) ✓ 81.10 88.45 45.67 71.39 82.15 0.26 22.31 50.39
Ours(J) ✓ 1.05 19.95 26.25 52.23 63.25 0.00 5.77 20.21

### Ours 9.19 55.64 4.20 71.65 93.18 1.05 17.32 53.81

3DGCN ✓ ✓ ✓ 83.31 95.83 47.51 85.79 94.59 13.07 46.77 68.66
PointNet++ ✓ ✓ ✓ 19.83 42.20 21.06 57.38 75.56 4.47 23.25 39.82
Mean Ours(SJ) ✓ ✓ 90.02 97.18 61.37 87.72 92.73 18.66 45.16 62.97
Ours(S) ✓ 89.12 95.31 42.78 81.82 88.80 13.72 46.65 62.73
Ours(J) ✓ 24.17 45.08 47.45 77.78 84.39 12.10 36.89 49.94
Ours 23.79 50.42 12.57 63.59 74.04 14.79 46.09 59.76
5 Experiment Results
5.1 Real-world Dataset
Besides the self-supervised learning of OP-Alignwe discussed in the main paper,
we also conduct semi-supervised, where only part of annotations are provided.
We show the visualization results of our model in a semi-supervised manner,
and the self-supervised manner in Fig. 6. The results of each category on our
real-world dataset are shown in Tab. 1 and in Fig. 7. In this section, we focus
on the comparison of semi-supervised OP-Align, self-supervised OP-Align, and
other baseline models.
Semi-supervised Learning OP-Align with joint pivot and joint direction annotation provided is indicated with Ours(J), it with part segmentation anno-

<!-- Page 25 -->

8 Y. Che et al.
Fig.6: Visualization results of semi-supervised OP-Align indicated with "ours(SJ)"
and self-supervised OP-Align indicated with "Ours" on the real-world dataset.
Fig.7: Average precision results on the real-world dataset.

<!-- Page 26 -->


### OP-Align: Object-level and Part-level Alignment 9

Fig.8: Visualization results of OP-Align on the synthetic dataset. The first row indicates object-level aligned input, the second row indicates the overlapping part-level
aligned input, and the third row indicates the reconstruction shape.
tation provided is indicated with Ours(S), and it with both part segmentation
and joint annotations provided is indicated with Ours(SJ).
The mean results demonstrate that the semi-supervised OP-Align with pose
and segmentation annotation Ours(SJ) exceeds both 3DGCN [10] and Point-
Net++ [14] on the majority of metrics, even without part pose annotations.
We also notice that even without joint annotation, the Ours(S) model can
also achieve close performance with Ours(SJ) on multiple metrics. However,
we find that OP-Align with the joint annotation Ours(J) achieves even lower
performancethantheself-supervisedoneonpartmetrics.Ourassumption,similar to the main paper, is that the joint pivot predicted by the self-supervised
model may be able to reduce the point distance between each part-level aligned
input and the reconstruction, meanwhile Ours(J) learned ground-truth joint
pivots, which reduce the point distance between the part-level aligned input
and the input object shape in the canonical joint state instead of the reconstruction. This difference may cause pose estimation inaccuracy. Overall, we
notice that for the learning of OP-Align, models with segmentation annotation
(Ours(S), Ours(SJ)) achieve higher performance than the models without it
(Ours(J), Ours).Thisdemonstratesthatourmodelcanaccuratelylocatejoint
pivots and directions without relying on any annotations once the object is correctly segmented. However, there is still significant room for improvement in
self-supervised part segmentation within our model.
5.2 Synthetic Dataset
Wepresenttheresultsofthesyntheticdatasethere.WereportEAP[11]’smean
performance from their original paper, along with the results of NPCS-EPN [7]
and ICP algorithm that EAP’s authors implemented. Besides the partially observed point cloud we discussed in the main paper, we also show the results for
the fully observed point cloud. We present each category’s evaluation of fully

<!-- Page 27 -->

10 Y. Che et al.
Table 2: Resultsonpartialobservedpointcloudfromsyntheticdataset.S, D, C, R,
treferstothepartsegmentationIoU,jointdirectionerror(degree),jointpivotserror,
mean part rotation error (degree), and mean part translation error.
Supervision HOI4DHOI4D Motion MotionMotionMotion

### Method Mean

PoseSegmentationJointLaptop Safe EyeglassesLaptop Oven Washer
3DGCN ✓ ✓ ✓ 99.28 94.11 90.37 93.74 91.45 95.32 94.05

## Icp ✓ 59.96 66.90 68.92 54.01 75.83 73.07 66.45


## S↑


## Eap 86.04 44.64 56.80 84.94 87.07 51.73 68.46


### Ours 92.38 86.14 67.08 78.62 76.18 83.81 80.70

3DGCN ✓ ✓ ✓ 1.73 4.79 12.84 7.69 11.73 16.28 9.78
NPCS-EPN ✓ ✓ ✓ 12.25 11.23 20.11 10.91 28.62 8.05 15.20

## D↓


## Eap 18.02 55.16 26.96 10.83 5.24 22.30 23.09


### Ours 1.46 1.34 3.49 2.61 9.52 21.33 6.63

3DGCN ✓ ✓ ✓ 0.014 0.024 0.112 0.068 0.130 0.096 0.084
NPCS-EPN ✓ ✓ ✓ 0.134 0.084 0.230 0.155 0.092 0.194 0.147

## C↓


## Eap 0.170 0.170 0.174 0.142 0.105 0.212 0.162


### Ours 0.080 0.066 0.049 0.167 0.135 0.162 0.110

3DGCN ✓ ✓ ✓ 2.90 5.50 16.06 13.97 17.07 16.65 11.61
NPCS-EPN ✓ ✓ ✓ 8.07 6.04 17.17 25.65 2.72 6.64 11.05
R↓ ICP ✓ 36.42 45.50 70.40 65.35 21.11 25.91 44.12

## Eap 7.71 18.65 7.13 10.64 11.30 7.21 10.44


### Ours 4.27 6.54 4.88 10.59 12.39 9.92 8.10

3DGCN ✓ ✓ ✓ 0.018 0.025 0.175 0.077 0.216 0.116 0.093
NPCS-EPN ✓ ✓ ✓ 0.048 0.028 0.066 0.275 0.028 0.034 0.080
t↓ ICP ✓ 0.293 0.264 0.155 0.266 0.247 0.229 0.242

## Eap 0.079 0.065 0.188 0.038 0.138 0.216 0.121


### Ours 0.092 0.064 0.183 0.154 0.163 0.116 0.129

Table 3: Results on fully observed point cloud from synthetic dataset. S, D, C, R,
treferstothepartsegmentationIoU,jointdirectionerror(degree),jointpivotserror,
mean part rotation error (degree), and mean part translation error.
Supervision HOI4DHOI4D Motion MotionMotionMotion

### Method Mean

PoseSegmentationJointLaptop Safe EyeglassesLaptop Oven Washer
3DGCN ✓ ✓ ✓ 96.78 97.67 81.93 91.66 94.46 93.15 92.25

## Icp ✓ 59.96 66.90 49.49 56.20 75.17 72.80 66.45


## S↑


## Eap 86.04 80.06 62.84 82.97 76.22 73.27 76.40


### Ours 90.21 72.06 66.60 81.80 90.84 75.25 79.46

3DGCN ✓ ✓ ✓ 5.62 5.15 14.01 8.87 5.85 9.85 8.44
NPCS-EPN ✓ ✓ ✓ 8.53 14.15 7.42 5.74 5.04 5.66 7.52

## D↓


## Eap 17.20 4.36 17.75 30.31 20.30 28.40 19.72


### Ours 3.23 8.21 3.28 2.46 4.41 10.47 5.18

3DGCN ✓ ✓ ✓ 0.039 0.026 0.096 0.065 0.071 0.107 0.071
NPCS-EPN ✓ ✓ ✓ 0.084 0.063 0.096 0.129 0.076 0.078 0.087

## C↓


## Eap 0.169 0.030 0.087 0.122 0.090 0.118 0.103


### Ours 0.075 0.079 0.049 0.157 0.092 0.231 0.114

3DGCN ✓ ✓ ✓ 9.21 8.45 17.63 12.54 15.71 14.03 12.44
NPCS-EPN ✓ ✓ ✓ 6.66 2.21 6.34 11.34 6.41 5.71 6.28
R↓ ICP ✓ 42.28 52.92 34.9 43.65 46.79 53.75 45.72

## Eap 4.68 11.43 10.99 8.88 5.91 13.38 9.21


### Ours 8.67 13.41 4.65 10.51 5.76 11.83 9.14

3DGCN ✓ ✓ ✓ 0.034 0.027 0.185 0.072 0.112 0.122 0.092
NPCS-EPN ✓ ✓ ✓ 0.0185 0.075 0.025 0.034 0.025 0.019 0.035
t↓ ICP ✓ 0.122 0.066 0.155 0.096 0.081 0.079 0.100

## Eap 0.024 0.052 0.070 0.043 0.061 0.062 0.052

Ours 0.069 0.082 0.184 0.164 0.123 0.110 0.122

<!-- Page 28 -->


### OP-Align: Object-level and Part-level Alignment 11

observedandpartiallyobservedpointcloudinTab.2andinTab.3respectively,
and the visualization in Fig. 8.
We note that since the data of drawer category in the synthetic dataset is
not published by EAP’s author, we do not use this category. We also note that
in EAP’s experiments, different categories of objects have varying numbers of
input points, while for OP-Align and 3DGCN we samples 1024 points for all
categories. This may lead to slight variations in the results.
FullyObservedPointCloud AstheresultsshowinTab.3,OP-Alignexceeds
other self-supervised methods by a large margin on part segmentation, joint
direction, and part rotation metrics. But compared to the partially observed
pointcloud,wecanobserveperformancedrawbacksonmultiplemetrics.Amajor
reason for this result is that a fully observed point cloud contains the points of
the object’s inner faces, which are complicated and invisible during most realworld situations. OP-Align faces difficulty in reconstructing such high variance
inner points.

<!-- Page 29 -->

12 Y. Che et al.

### References


## Chen, H., Liu, S., Chen, W., Li, H., Hill, R.: Equivariant point network for 3d

pointcloudanalysis.In:IEEEConf.Comput.Vis.PatternRecog.pp.14514–14523
(2021)

## Chen, W., Jia, X., Chang, H.J., Duan, J., Shen, L., Leonardis, A.: Fs-net: Fast

shape-based network for category-level 6d object pose estimation with decoupled
rotation mechanism. In: IEEE Conf. Comput. Vis. Pattern Recog. pp. 1581–1590
(2021)

## Di,Y.,Zhang,R.,Lou,Z.,Manhardt,F.,Ji,X.,Navab,N.,Tombari,F.:Gpv-pose:

Category-level object pose estimation via geometry-guided point-wise voting. In:

### IEEE Conf. Comput. Vis. Pattern Recog. pp. 6781–6791 (2022)


## He, K., Gkioxari, G., Dollár, P., Girshick, R.: Mask r-cnn. In: Int. Conf. Comput.


### Vis. pp. 2961–2969 (2017)


## Kawana, Y., Mukuta, Y., Harada, T.: Unsupervised pose-aware part decomposition for man-made articulated objects. In: Eur. Conf. Comput. Vis. pp. 558–575.


### Springer (2022)


## Kirillov, A., Mintun, E., Ravi, N., Mao, H., Rolland, C., Gustafson, L., Xiao, T.,

Whitehead, S., Berg, A.C., Lo, W.Y., et al.: Segment anything. arXiv preprint
arXiv:2304.02643 (2023)

## Li, X., Wang, H., Yi, L., Guibas, L.J., Abbott, A.L., Song, S.: Category-level

articulated object pose estimation. In: IEEE Conf. Comput. Vis. Pattern Recog.
pp. 3706–3715 (2020)

## Li,X.,Weng,Y.,Yi,L.,Guibas,L.J.,Abbott,A.,Song,S.,Wang,H.:Leveraging

se(3) equivariance for self-supervised category-level object pose estimation from
point clouds. Adv. Neural Inform. Process. Syst. 34, 15370–15381 (2021)

## Lin, T.Y., Maire, M., Belongie, S., Hays, J., Perona, P., Ramanan, D., Dollár, P.,

Zitnick,C.L.:Microsoftcoco:Commonobjectsincontext.In:Eur.Conf.Comput.

### Vis. pp. 740–755. Springer (2014)


## Lin, Z.H., Huang, S.Y., Wang, Y.C.F.: Convolution in the cloud: Learning deformable kernels in 3d graph convolution networks for point cloud analysis. In:


### IEEE Conf. Comput. Vis. Pattern Recog. pp. 1800–1809 (2020)


## Liu,X.,Zhang,J.,Hu,R.,Huang,H.,Wang,H.,Yi,L.:Self-supervisedcategorylevelarticulatedobjectposeestimationwithpart-levelse(3)equivariance.In:Int.


### Conf. Learn. Represent. (2023)


## Qi,C.R.,Litany,O.,He,K.,Guibas,L.J.:Deephoughvotingfor3dobjectdetection in point clouds. In: Int. Conf. Comput. Vis. pp. 9277–9286 (2019)


## Qi, C.R., Su, H., Mo, K., Guibas, L.J.: Pointnet: Deep learning on point sets for

3d classification and segmentation. In: IEEE Conf. Comput. Vis. Pattern Recog.
pp. 652–660 (2017)

## Qi,C.R.,Yi,L.,Su,H.,Guibas,L.J.:Pointnet++:Deephierarchicalfeaturelearning on point sets in a metric space. Advances in neural information processing

systems 30 (2017)

## Wu, T., Pan, L., Zhang, J., Wang, T., Liu, Z., Lin, D.: Density-aware chamfer

distance as a comprehensive metric for point cloud completion. arXiv preprint
arXiv:2111.12702 (2021)

## Zheng, L., Wang, C., Sun, Y., Dasgupta, E., Chen, H., Leonardis, A., Zhang, W.,

Chang, H.J.: Hs-pose: Hybrid scope feature extraction for category-level object
pose estimation. In: IEEE Conf. Comput. Vis. Pattern Recog. pp. 17163–17173
(2023)

<!-- Page 30 -->


### OP-Align: Object-level and Part-level Alignment 13


## Zhu, M., Ghaffari, M., Clark, W.A., Peng, H.: E2pn: Efficient se (3)-equivariant

pointnetwork.In:IEEEConf.Comput.Vis.PatternRecog.pp.1223–1232(2023)

## Tables

**Table (Page 5):**

| Parameters 𝒂x,𝒄x,𝒅x |  |  |  |  |
|---|---|---|---|---|
|  | Part-level Alignment |  | 𝑹d,𝑹a,𝑻a |  |


**Table (Page 5):**

| PoseHead(𝑭eqv) |  |
|---|---|
|  |  |


**Table (Page 19):**

| 256×64×12 |
|---|
|  |


**Table (Page 20):**

| Max-pooling Repeat Along Points Concat 256×1024 512×1024 d1vn )652 o ,215( C |  | 𝑾 𝒂,𝒄,𝒅 Softmax SegHead JointHead 512×1024 512 Max-pooling Along Points |
|---|---|---|
|  | 512×1024 |  |


**Table (Page 20):**

|  |  |  |  |  |
|---|---|---|---|---|
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |


**Table (Page 20):**

|  |  |  |  | DCD (α DCD (α | =10) =30) |
|---|---|---|---|---|---|
|  |  |  |  | DCD (α DCD (α L2 | =60) =120) |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
