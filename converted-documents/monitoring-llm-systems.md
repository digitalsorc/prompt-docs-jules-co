---
title: "Monitoring LLM Systems"
original_file: "./Monitoring_LLM_Systems.pdf"
document_type: "research"
conversion_date: "2025-11-29"
topics: ["llm", "rag", "fine-tuning", "evaluation", "multimodal"]
keywords: ["transformer", "models", "vision", "our", "vit", "small", "dwconv", "accuracy", "module", "tiny"]
summary: "<!-- Page 1 -->

Depth-Wise Convolutions in Vision Transformers for

### Efficient Training on Small Datasets


### Tianxiao Zhanga, Wenju Xub, Bo Luoa, Guanghui Wangc,∗

aDepartment of Electrical Engineering and Computer Science, University of

### Kansas, Lawrence, 66045, KS, USA

bAmazon, Palo Alto, 94301, CA, USA
cDepartment of Computer Science, Toronto Metropolitan University, Toronto, M5B
2K3, ON, Canada

### Abstract

TheVisionTransformer(ViT)leveragestheTransformer’sencodertocapture
glob"
related_documents: []
---

# Monitoring LLM Systems

<!-- Page 1 -->

Depth-Wise Convolutions in Vision Transformers for

### Efficient Training on Small Datasets


### Tianxiao Zhanga, Wenju Xub, Bo Luoa, Guanghui Wangc,∗

aDepartment of Electrical Engineering and Computer Science, University of

### Kansas, Lawrence, 66045, KS, USA

bAmazon, Palo Alto, 94301, CA, USA
cDepartment of Computer Science, Toronto Metropolitan University, Toronto, M5B
2K3, ON, Canada

### Abstract

TheVisionTransformer(ViT)leveragestheTransformer’sencodertocapture
global information by dividing images into patches and achieves superior performance across various computer vision tasks. However, the self-attention
mechanism of ViT captures the global context from the outset, overlooking
the inherent relationships between neighboring pixels in images or videos.
Transformers mainly focus on global information while ignoring the finegrained local details. Consequently, ViT lacks inductive bias during image
orvideodatasettraining. Incontrast,convolutionalneuralnetworks(CNNs),
with their reliance on local filters, possess an inherent inductive bias, making
them more efficient and quicker to converge than ViT with less data. In
this paper, we present a lightweight Depth-Wise Convolution module as a
shortcut in ViT models, bypassing entire Transformer blocks to ensure the
models capture both local and global information with minimal overhead.
Additionally, we introduce two architecture variants, allowing the Depth-
Wise Convolution modules to be applied to multiple Transformer blocks for
parameter savings, and incorporating independent parallel Depth-Wise Convolution modules with different kernels to enhance the acquisition of local
information. The proposed approach significantly boosts the performance of
ViT models on image classification, object detection, and instance segmentation by a large margin, especially on small datasets, as evaluated on CIFAR-
10, CIFAR-100, Tiny-ImageNet and ImageNet for image classification, and
∗Corresponding author (wangcs@torontomu.ca)
Preprint submitted to Neurocomputing November 26, 2024
4202
voN
32
]VC.sc[
4v49391.7042:viXra

<!-- Page 2 -->

COCO for object detection and instance segmentation. The source code can
be accessed at https://github.com/ZTX-100/Efficient_ViT_with_DW.
Keywords: Vision Transformers, Depth-Wise Convolutions, Small Dataset

## Introduction

Transformer models have demonstrated exceptional performance in Natural Language Processing (NLP) tasks by capturing long-range relationships
through attention mechanisms [1]. However, the direct application of Transformer models to vision tasks is less intuitive, as images are inherently interconnected, and pixels exhibit close relationships. Vision Transformer (ViT)
[2] addresses this challenge by dividing the image into fixed-size patches, linearly embedding each patch as a token. To capture 2D relationships among
image tokens, positional embedding is introduced, compensating for the loss
of 2D coordinate relationships in embedded image patches. ViT includes a
learnable class token to interact with image patch tokens for image classification.
Despite its success, ViT often requires substantial data and longer training times due to the attention mechanism’s computational demands. The
attention mechanism calculates the dot product of embeddings for each token pair, necessitating more time to learn the inductive bias that neighboring
pixels share stronger relationships. Global attention in ViTs treats all tokens
equally, neglecting the fact that neighboring image patches have higher relationships. In contrast, Convolutional Neural Networks (CNNs) naturally
possess inductive bias due to local filters. However, CNNs may have a lower
upper bound than ViTs because of their limited global view. In essence,
ViTs outperform CNNs when datasets are large enough, and training times
are sufficiently long, showcasing their superior performance under such conditions.
Image contents are inherently cohesive as a whole, and forcefully splitting
them into patches can hinder the recognition process. Moreover, treating all
patches equally in models like Vision Transformers (ViTs) sacrifices the inductive bias present in the images, requiring a more extensive training effort
to converge. While some approaches involve overlapping patches, this introduces additional computational costs without fundamentally addressing the
issue. In contrast, CNN models, by their nature, excel at filtering local pixels
in a contiguous manner, which is crucial for image recognition, particularly
2

<!-- Page 3 -->

when dealing with relatively small objects. However, the lack of global views
may restrict the performance of convolutional models, especially in scenarios
with abundant training data. The key question becomes: How can we efficiently integrate these two approaches, leveraging convolutions to support
Transformer models, ensuring rapid convergence, and achieving superior performance?
In this paper, we introduce a straightforward yet effective method to
seamlessly integrate convolutional and Transformer blocks, enabling the simultaneous learning of global and local information efficiently. Our approach
leverages Depth-Wise Convolutions [3] to capture local information, while
Transformer blocks are employed to capture global information. The Depth-
Wise Convolutions serve as a shortcut, bypassing the entire Transformer
block (attention+FFN). The final combination is achieved through summation, providing a unified representation of both Depth-Wise Convolutions
and Transformer blocks. The Depth-Wise Convolutions are applied for each
Transformer block, creating two paths after each block for the network to
choose from. This design ensures a flexible and dynamic integration of the
local and global features. Our method achieves a superior performance
improvement with only a marginal increase in parameters and computations, particularly benefiting small datasets. Our approach enables smallsize Transformer models to outperform some larger counterparts, showcasing
their effectiveness and efficiency.
In summary, our contributions are outlined below.
• We propose an efficient and effective approach to combining Depth-
Wise Convolutions and Transformer blocks, allowing simultaneous capture of local and global information with minimal additional parameters and computational load. The proposed lightweight Depth-Wise
module bypasses entire Transformer blocks to attain fine-grained details that might be missed otherwise. This module does not alter the
internal structure of MHSA and FFN, making it a plug-and-play componentthatcanbeutilizedbymostTransformermodels. Ourapproach
demonstrates superior performance in image classification, object detection, and instance segmentation.
• Wedevelopedtwotypesofarchitecturalvariants. Thefirstvariantaims
to reduce parameters and floating-point operations (FLOPs) by utilizing the Depth-Wise module to bypass multiple Transformer blocks.
3

<!-- Page 4 -->

Thesecondvariantseekstoimproveperformancebyincorporatingmultiple independent parallel Depth-Wise modules, each dedicated to enhancing local information.
• We demonstrate that certain modules are dispensable when our approach is implemented in the training of Transformer models on small
datasets. Furthermore, by applying our approach without these modules, we can reduce both parameters and FLOPs, while significantly
enhancing the performance.

## Related Work


### Vision Transformers

ViT [2] introduces the Transformer models into vision recognition by
splitting the images into fixed-size patches and then tokenizing each patch
into the token so that the image patches can be utilized in the attention
module of Transformer models. Many variations and improvements have
been proposed [4][5][6] and applied to various vision tasks such as point cloud
completion [7] and crowd counting [8]. DeiT [9] employs distillation tokens
for attention learning from the teacher models to the student models. CaiT
[10] introduces LayerScale to effectively train the ViT models with deeper
layers so that the performance of deep ViT models could be further boosted.
Hierarchical Vision Transformer architecture [11][12][13][14][15] are designed
to better suit vision tasks by reducing the size of feature maps as the network
progresses deeper, resembling the structure of CNN architectures.
To reduce the computational cost, some window-based Vision Transformer models have been proposed. Swin Transformer [16] restricts the selfattention of the tokens on small windows so that the inductive bias could
be slightly introduced while significantly reducing the computational costs
with the sacrifice of the global views. To mitigate the limitation of lacking
global views, it also incorporates a shifted window mechanism, expanding
the self-attention calculation to new shifted windows. Thus, the views of
tokens are expanded. Other works, such as [17][18][19], attempt to increase
the receptive fields with cross-window interactions so that the information
between the windows could be exchanged and the tokens could exchange the
information with other windows.
4

<!-- Page 5 -->


### Vision Transformers and Convolutions

CvT [20] designs a hierarchical Transformer architecture with a convolutional token embedding and a convolutional Transformer block utilizing a
convolution projection to project the feature maps into query, key, and value.
BoTNet [21] replaces the final three bottleneck blocks of the ResNet model
with BoT blocks that contain MHSA layers so that the self-attention layer
canaggregatetheinformationattainedbytheconvolutionallayers. LocalViT
[22] introduces the Depth-Wise Convolution into the Feed-Forward Networks
in the Transformer block to add locality into the Transformer models. CMT
[23] proposes a hybrid Transformer model to take advantage of Transformers
and CNNs for global views and local features, respectively. MobileFormer
[24] designs efficient networks to integrate MobileNet [3] and Transformer
blocks with a two-way bridge in between so that both local features and
global interactions can be effectively communicated and fused.
DHVT [25] integrates the convolutions into MLP and patch embeddings
to introduce the inductive bias into the Transformer model, and introduces a
dynamic feature aggregation module in MLP and a ”head token” in MHSA
for diverse channel representation so that the gap between the Transformer
models and CNN models could be eliminated. ViTAE [26] and its extension
model ViTAEv2 [27] utilize multiple dilated convolutions to downsample the
feature maps and aid the MHSA module to attain the locality simultaneously. Mixformer [28] parallelizes window-based self-attention and Depth-
Wise Convolution to extend the receptive fields and designs bi-directional
interactions to exchange information of channel and spatial dimensions betweenthem. DMFormer[29]proposesaDynamicMulti-levelAttentionmechanism which is comprised of Depth-Wise Convolutions with multiple kernel
sizes for various patterns and a gating mechanism for adaptability. Scope-
ViT [30] involves Depth-Wise Convolutions into Transformer architecture for
scale-aware efficient training. DctViT [31] proposes a hybrid structure with
convolutions and Transformers for higher accuracy on multiple vision tasks.
The hybrid structures are also applied to wetland classification [32], salient
object detection [33][34], referring image segmentation [35], etc.
The computational structures of some previous models focus on integrating convolutional networks into the Multi-Head Self-Attention (MHSA) or
Feed-Forward Network (FFN), making convolutional networks essential components of Transformer architectures. Additionally, the convolutional components in some of these studies are not necessarily lightweight. In contrast,
our approach aims to efficiently combine Transformer blocks with convolu-
5

<!-- Page 6 -->

tions while minimizing computational overhead. It is designed as a versatile
and straightforward module that can be easily integrated into various Vision
Transformer models.

## Methodology


### Vision Transformers

ViT [2] introduces Transformers [1] into vision tasks by splitting the images into patches which are tokenized into tokens (x). To preserve the positional relations of the image patches, learnable positional embeddings are
added to each token to learn the 2D relations of the patches. The tokens and
positional embeddings are illustrated in Eq. (1). x demonstrates the class
c
token and x indicates the positional embeddings.
p
x0 = (x ,x ,...,x ;x )+x (1)
1 2 l c p
x′n = xn +MHSA(LayerNorm(xn)) (2)
xn+1 = x′n +FF(LayerNorm(x′n)) (3)
Eqs. (2) and (3) illustrate the Multi-Head Self-Attention (MHSA) layer
andthefeed-forward(FF)layer. Theresidualconnectionandpre-LayerNorm
[36] are harnessed in both layers. The attention layer and feed-forward layer
are formed as Transformer blocks and Transformer models are comprised of
cascaded Transformer blocks. The class token is employed to classify the
image and output the result.
ViT models leverage self-attention mechanisms to compute the similarity
between each pair of patch tokens and then assign different weights to different tokens according to the similarities between the patch tokens. Nonetheless, ViT models often overlook the inductive bias inherent in images, where
neighboring pixels or patches have more relations. This oversight can lead
to slow convergence, requiring more training iterations to learn the inductive
biasanddemandinglargedatasetsforoptimalperformance. Incontrast, convolutions inherently possess an inductive bias due to local filters traversing
the image, capturing local details. Recognizing the complementary nature
of convolutions to Transformer models, particularly in scenarios with small
datasets, we propose a lightweight approach using Depth-Wise Convolutions
6

<!-- Page 7 -->

LayerNorm + + + MHSA LayerNorm FFN
DWConv
module
LayerNorm + + + MHSA LayerNorm FFN
Transformer Transformer
Block Block
DWConv
module
GELU BatchNorm DWConv
... ...
DWConv ... 1D -> 2D 2D -> 1D ...
module
Figure1: Thearchitectureofourproposedmethod. TheDepth-WiseConvolutionmodule
bypasses the entire Transformer block so that the local details can be attained and added
to the output of the Transformer block. In the DWConv module, the 1D image patch
tokens are first reshaped to 2D feature maps. If the class token exists, it would not be
involved in the DWConv module and only image patch tokens are utilized to reconstruct
the feature maps. Batch normalization and GELU activation are employed before the
Depth-Wise Convolution. Finally, the feature maps would be reshaped to 1D tokens and
added to the output of the Transformer block. The DWConv module is exploited in all
Transformer blocks.
to enhance the convergence and performance of Vision Transformer models.
This is particularly beneficial when training ViT models from scratch on
limited datasets without additional assistance.

### Our Approach

Convolutional kernels excel at capturing fine details in images, a capability lacking in ViT models. The challenge lies in determining how and where
to incorporate these kernels. To maintain a lightweight design without significantly increasing parameters and computational demands, we select Depth-
Wise Convolutions to filter the local details. We utilize the Depth-Wise Convolution as the shortcut to bypass the entire Transformer block. Since the
patch tokens are flattened to 1D, we have to reconstruct all patch tokens into
2D feature maps. The architecture of our proposed model is demonstrated
in Fig. 1. The DWConv module is harnessed in all Transformer blocks as
complementary components.
xn from Eq. (2) is used to reshape the 1D tokens to 2D feature maps.
The reshaped 2D feature maps are implemented GELU activation [37] and
7

<!-- Page 8 -->

batch normalization [38] before being fed into the Depth-Wise Convolution
(DWConv). The kernel we utilize for Depth-Wise Convolution is 3×3. The
2D feature maps are reshaped to 1D patch tokens and finally the reshaped
1D patch tokens (x n+1) and the output of the Transformer block (Eq. (3))
1d
are summed together. The summed result (x n+1) is utilized as the input
ours
to the next block. This process is illustrated below.
xn = Reshape (xn) (4)
2d 1d−>2d
x′ n = DWConv(BatchNorm(GELU(x n))) (5)
2d 2d
x n+1 = Reshape (x′ n) (6)
1d 2d−>1d 2d
x n+1 = xn+1 +x n+1 (7)
ours 1d
The DWConv modules act as “supervisors” to supervise the Transformer
blocks and they are complementary to each other. Each Transformer block is
supervisedbytheDWConvmodulestocapturedetailsthatmaybemissedby
the Transformer blocks. While the Transformer blocks play the main role in
the architecture, the proposed lightweight DWConv modules are leveraged to
retrievelocalinformation, therebyenhancingtheoverallperformance. Unlike
some hybrid models that design complex hybrid architectures, our proposed
approach demonstrates simplicity, effectiveness, and flexibility.

### Architecture Variants

In addition to the base architecture, we have designed several variants
based on the core structure, as illustrated in Fig. 2. In our base architecture,
the Depth-Wise module bypasses each Transformer block. Additional variants are designed where the Depth-Wise module bypasses more Transformer
blocks. These variants prove beneficial when working with Vision Transformers that have deeper layers, helping to reduce the number of parameters and
computational costs.
Moreover, in Transformer architectures with multiple stages, the size of
the feature maps is reduced and the dimension is increased in successive
stages. To maintain the input and output sizes of the Depth-Wise module,
werecommendlimitingthebypasswithineachstagetopreventaDepth-Wise
module from crossing stages when multiple Transformer blocks are bypassed.
8

<!-- Page 9 -->

LayerNorm

## + + Mhsa

LayerNorm

## Ffn

DWConv
module
(a)
2 blocks
Transformer Block Transformer Block +
DWConv
module
3 blocks (b)
Transformer Block Transformer Block Transformer Block +
DWConv
module
4 blocks (c)
Transformer Block Transformer Block Transformer Block Transformer Block +

### Transformer Block

Figure 2: The architecture variants of our proposed approach involve bypassing multiple
Transformer blocks. Structures (a), (b), and (c) represent the Depth-Wise module bypassing 2, 3, and 4 Transformer blocks, respectively. For Vision Transformer models with
deeper layers, bypassing additional blocks may be a beneficial strategy to reduce both
parameters and computational costs.
Alternatively, one Depth-Wise module can be used to bypass an entire stage,
ensuring that each stage has only one corresponding Depth-Wise module for
more efficient combinations.
Furthermore, the DWConv modules could operate in parallel with various kernel sizes to capture the local information independently, as illustrated
in Fig. 3. In the experiments, we leverage parallel DWConv modules with
different kernel sizes to demonstrate the performance of the variants. To
further reduce the number of parameters and computational cost, multiple
independent parallel DWConv modules could be combined with the aforementioned variants so that multiple Transformer blocks are contained by the
DWConv modules. In Fig. 3, N Transformer blocks are encompassed in the
DWConv modules and N ≥ 1.
Not modifying the structures of MHSA and FFN makes our approach
more flexible for use with most Transformer models, rather than being de-
9

<!-- Page 10 -->

1 kernel k x k
DWConv 1 1
module
xN
Transformer Block +
...
...
n kernel k x k
DWConv n n
module
Figure 3: The architecture variants of our method involve multiple DWConv modules
operating in parallel. These independent DWConv modules, each with different kernel
sizes,runconcurrentlyonTransformerblockstocapturelocaldetailssimultaneously. This
structurecanbecombinedwithpreviousvariantsshowninFig.2toincludeNTransformer
blocks in the DWConv modules.
signed for specific ones. The proposed architecture variants illustrate the
flexibility of our methods compared to some existing hybrid architectures
that combine convolutions and Transformers. The Transformers are greatly
enhanced by the proposed DWConv module with minimal overhead. Additionally, the structure can be easily modified to further enhance the performance or save the parameters and computations with different variants.

### Complexity Analysis

Our proposed approach is a lightweight module that is employed with
each Transformer block. Unlike some models inserting convolutional layers
inside the Transformer blocks, the proposed module is separable from the
Transformer block, making it a plug-and-play module applicable to most
existingVisionTransformermodels. Theincreasedparametersaredependent
onthedepthsanddimensionsoftheTransformermodels. Sinceourmoduleis
independent for each Transformer block without sharing parameters, deeper
Transformer models could have more parameters introduced. However, the
increased parameters are negligible compared to the Transformer backbone.
For instance, the ViT-Tiny model used in our experiments has 12 blocks and
a dimension of 192. With a depth-wise convolution of 3×3 kernel size, the
increased parameters for the ViT-Tiny model are approximately 12×192×
(3×3+1) = 23,040 (0.023M) which is negligible compared to the backbone
10

<!-- Page 11 -->

with around 5.5 million parameters. Moreover, since the patch size is 16 and
the images are resized to 224 and the size of the feature maps is 14×14, the
increased calculations for ViT-Tiny model could be approximately calculated
by 12 × 192 × (14 × 14) × (3 × 3) = 4,064,256 (0.004G), which is trivial
compared to the total 1.26G FLOPs. In the aforementioned calculation, the
number of parameters and calculations of BatchNorm are ignored since they
are insignificant to the model.
Intheexperiments, sometimesourmethodscouldevenreducethenumber
of parameters and FLOPs considering some modules and positional embeddings could be removed for training the small dataset when our approach is
applied to the Vision Transformer models. The increased number of parameters and FLOPs that are trivial to the models are highly dependent on the
number of layers and dimensions of the models. Additionally, they also depend on which architecture variants are employed for the Vision Transformer
models.
Some hybrid architectures merge convolutional networks into the Transformer architecture inefficiently, introducing significant parameters and computations as convolutional networks become essential components of Transformer structures. Additionally, these methods are often designed for specific
Transformer architectures, making them impractical for other Transformer
models. In contrast, our approach is designed to be easily incorporated into
various Vision Transformer models. Complexity analysis shows that our approach introduces negligible overhead, with the majority of parameters and
computations still coming from Transformer structures. However, the performance improvements are significant, especially on small datasets.

## Experiments and Results

To verify the effectiveness and efficiency of our proposed approach, we select vanilla ViT [2], CaiT [10], and Swin Transformer [16] for the experiments
on three small datasets: CIFAR10 [39], CIFAR100 [39], and Tiny-ImageNet
[40]. We also evaluated the model on a relatively large dataset: ImageNet-
1K [41]. Additionally, COCO [42] is utilized for the evaluation of object
detection and instance segmentation.

### Classification Performance on Small Datasets

CIFAR10 [39], CIFAR100 [39], and Tiny-ImageNet [40] are exploited as
small datasets for training and evaluating image classification tasks. The
11

<!-- Page 12 -->

classification accuracy is defined as the ratio of correctly classified samples
to the total number of samples. In our paper, we use Top-1 accuracy for
classification.

#### Experimental Settings

ViT. We select ViT-Tiny and ViT-Small to conduct the experiments for
all datasets. The parameter settings of ViT models are followed by [43]. The
dimensions of ViT-Tiny and ViT-Small are 192 and 384, respectively. The
MLP ratio is 4 for both models which indicates the MLP dimensions are 768
and 1536 for tiny and small models, respectively. The numbers of heads for
tiny and small models in Multi-Head Self-Attention are 3 and 6 respectively
so the dimension for each head is 64 for tiny and small models. The depths
are 12 for ViT-Tiny and ViT-Small.
CaiT. We choose CaiT-xxs12 and CaiT-xxs24 as the base models for the
experiments. The dimensions of CaiT-xxs are 192 and the number of heads
is 4. The MLP dimensions are 768 and the class depths are 2. The main
depths for CaiT-xxs12 and CaiT-xxs24 are 12 and 24, respectively.
Swin Transformer. Swin-Tiny is selected for the experiments. For
Swin-Tiny model, the drop path rate is 0.2 and the window size is 7; The
depths and numbers of heads are (2, 2, 6, 2) and (3, 6, 12, 24) for each stage,
respectively.
ExperimentalParameters. AllexperimentsareconductedusingAdamW
[44] optimizer with 300 epochs and 20 epochs warmup. The weight decay is

### The batch size for three small datasets is 128 with 4 NVIDIA P100

GPUs. The cosine decay learning rate scheduler is exploited. The base learningrateforSwin-Transformeronthreesmalldatasetsis2.5e-4, whilethebase
learning rate for other experiments on small datasets is 5e-4. The images are
resized to 224 and the patch size for both ViT and CaiT is 16.
Data Augmentation. Most regularization and augmentation settings
follow [16], including color jitter, Auto-Augment [45], random erasing [46],
MixUp [47], CutMix [48]. All experiments are trained from scratch on each
dataset without the assistance of an extra dataset.

#### Vision Transformer

The vanilla ViT model splits the image into small patches which are embedded as tokens for Transformer blocks. Since the tokens are 1-dimensional
without the 2-dimensional positional information, the vanilla ViT model utilizes a positional embedding which would be added to all tokens to learn
12

<!-- Page 13 -->

Table 1: The experimental results of ViT-Tiny and ViT-Small on small dataset (PE =

### Positional Embedding)

CIFAR-10 CIFAR-100 Tiny-ImageNet

### Model

Accuracy Params FLOPs Accuracy Params FLOPs Accuracy Params FLOPs

### ViT-Tiny 94.01 5.5M 1.26G 73.68 5.5M 1.26G 59.00 5.6M 1.26G

ViT-Tinyw/oPE 87.83(-6.18) 5.5M 1.26G 64.41(-9.27) 5.5M 1.26G 53.15(-5.85) 5.5M 1.26G
ViT-Tiny(ours) 96.41(+2.40) 5.5M 1.26G 78.05(+4.37) 5.6M 1.26G 64.10(+5.10) 5.6M 1.26G
ViT-Tinyw/oPE(ours) 96.32(+2.31) 5.5M 1.26G 77.31(+3.63) 5.5M 1.26G 63.57(+4.57) 5.5M 1.26G
ViT-Small 95.09 21.7M 4.61G 73.97 21.7M 4.61G 60.90 21.7M 4.61G
ViT-Smallw/oPE 89.27(-5.82) 21.6M 4.61G 65.68(-8.29) 21.6M 4.61G 53.98(-6.92) 21.7M 4.61G
ViT-Small(ours) 97.02(+1.93) 21.7M 4.62G 80.01(+6.04) 21.7M 4.62G 66.86(+5.96) 21.8M 4.62G
ViT-Smallw/oPE(ours) 96.96(+1.87) 21.6M 4.62G 80.14(+6.17) 21.7M 4.62G 66.59(+5.69) 21.7M 4.62G
Table 2: The ablation study of ViT-Tiny (accuracy)
Method CIFAR-10 CIFAR-100 Tiny-ImageNet
shortcut 87.50 65.10 52.15
kernel3 96.32 77.31 63.57
kernel5 96.26 78.71 63.67
kernel7 96.26 78.69 63.95
kernel3+5 96.52 78.63 64.00
kernel3+5+7 96.39 78.00 64.27
the 2-dimensional positional relationship between tokens. Since convolutions
with zero padding could encode the positional information[49], we also applied our approach to the ViT model without positional embeddings. The
experimental results are illustrated in Table 1.
From Table 1 we observe that removing the positional embeddings significantly deteriorates the performance of ViT-Tiny and ViT-Small, highlighting
the importance of positional embeddings in Vision Transformers. When our
method is applied to ViT models, there is a substantial improvement in performance, regardless of the presence of positional embeddings. For ViT-Tiny,
the increased accuracy for CIFAR-10, CIFAR-100, and Tiny-ImageNet are
around 2%, 4%, and 5%, respectively. For ViT-Small, the performance boost
for CIFAR-10, CIFAR-100, and Tiny-ImageNet are nearly 2%, 6%, and 6%,
respectively. Additionally, our method without positional embeddings even
slightly reduces the number of parameters with much better accuracy. More
importantly, theaccuracy ofViT-Tinywithour proposedDWConvsurpasses
13

<!-- Page 14 -->

Table 3: The experimental results of CaiT-xxs12 and CaiT-xxs24 on small dataset (LS =
LayerScale, TH = Talking Head, PE = Positional Embedding)
CIFAR-10 CIFAR-100 Tiny-ImageNet

### Model

Accuracy Params FLOPs Accuracy Params FLOPs Accuracy Params FLOPs
CaiT-xxs12 92.02 6.4M 1.30G 73.43 6.4M 1.30G 59.17 6.5M 1.30G
CaiT-xxs12w/o-(LS,TH,PE) 87.45(-4.57) 6.4M 1.28G 70.32(-3.11) 6.4M 1.28G 60.62(+1.45) 6.4M 1.28G
CaiT-xxs12w/o-(LS,TH,PE)(ours) 96.43(+4.41) 6.4M 1.29G 81.72(+8.29) 6.4M 1.29G 70.47(+11.30) 6.4M 1.29G
CaiT-xxs24 93.89 11.8M 2.53G 74.84 11.8M 2.53G 60.97 11.8M 2.53G
CaiT-xxs24w/o-(LS,TH,PE)(ours) 97.28(+3.39) 11.8M 2.51G 82.83(+7.99) 11.8M 2.51G 70.64(+9.67) 11.8M 2.51G
that of vanilla ViT-Small which has almost 4x the number of parameters and
FLOPsbylargemargins,demonstratingtheefficiencyandeffectivenessofour
proposed method.
Moreover, extra experiments are implemented with different kernel sizes
and parallel DWConv modules, as illustrated in Table 2. Directly applying a
shortcut connection with positional embedding without any modules to bypass the Transformer blocks significantly reduces the accuracy. The possible
reason for that might be the low-level input embeddings for the Transformers, which is different from the high-level input features attained from CNNs
[50]. Some large kernel sizes or parallel DWConv modules could boost the
performance with a slightly higher number of parameters and FLOPs.

#### CaiT

CaiT introduces LayerScale to improve the performance of deeper layer
transformer models by multiplying a learnable diagonal matrix [10] by each
residual block. The class attention is introduced before the final classifier
to convert patch embeddings into the final class embeddings. Talking heads
attention [51] is utilized in the model for further improvement of the performance. However, LayerScale [10] and talking heads attention [51] are not
necessary when our proposed approach is applied to CaiT model on a small
dataset. Moreover, talking heads attention is extremely time-consuming for
smalldatasettraininginourexperiments. ThusLayerScaleandtalkingheads
attention are removed when our method is applied to CaiT-xxs12 and CaiT-
xxs24, which is demonstrated in Table 3, where “LS”, “TH” and “PE” illustrate LayerScale, talking heads attention and positional embeddings. Similar
to the vanilla ViT model, the positional embeddings are not necessary when
our method is introduced to the small dataset training.
14

<!-- Page 15 -->

Table 4: The accuracy for different blocks bypassed by DWConv module with CaiT
Method CIFAR-10 CIFAR-100 Tiny-ImageNet
xxs12(1block) 96.43 81.72 70.47
xxs12(2blocks) 96.16 80.67 68.76
xxs12(3blocks) 95.60 79.50 67.61
xxs12(4blocks) 94.80 78.61 67.49
xxs24(1block) 97.28 82.83 70.64
xxs24(2blocks) 97.00 82.90 70.07
xxs24(3blocks) 96.84 81.90 69.57
xxs24(4blocks) 96.51 80.16 68.61
It is evident from Table 3 that removing LayerScale, talking heads attention, and positional embeddings reduces the accuracy for small datasets
except Tiny-ImageNet. When our DWConv modules are applied to CaiT
models, the accuracy is significantly boosted for small datasets. For Tiny-
ImageNet,theaccuracyofCaiT-xxs12withourproposedDWConvistremendously improved by around 11% with less number of parameters and FLOPs
since the aforementioned modules are eliminated when our approach is applied to CaiT models. Similar to ViT models, CaiT-xxs12 with our method
has much higher accuracy than the original CaiT-xxs24 and almost half of
the number of parameters and FLOPs compared to CaiT-xxs24 model. In
addition, CaiT-xxs12 with our DWConv modules even has much better performance than the original Swin-Transformer (as shown in Table 5) that has
almost 4x the number of parameters and FLOPs than CaiT-xxs12.
ToverifythearchitecturevariantthatmultipleTransformerblocksarebypassed by the proposed DWConv modules, more experiments are conducted
with CaiT, as demonstrated in Table 4. The number of blocks indicates how
many Transformer blocks are supervised by the DWConv modules in the
architecture. The performance drops when more blocks are supervised by
DWConv modules, but the accuracy is still much higher than the original
models. The variant is appropriate when the layers are deeper to reduce
the number of parameters and FLOPs while still maintaining relatively high
accuracy.

#### Swin Transformer

The architecture of Swin Transformer consists of four stages with hierarchical feature maps. The size of feature maps is reduced by 2 on each side
15

<!-- Page 16 -->

Table 5: The experimental results of Swin-Tiny on small datasets
CIFAR-10 CIFAR-100 Tiny-ImageNet

### Model

Accuracy Params FLOPs Accuracy Params FLOPs Accuracy Params FLOPs
Swin-Tiny 93.59 27.5M 4.51G 78.75 27.6M 4.51G 68.24 27.7M 4.51G
Swin-Tinyw/oshift-window 93.36(-0.23) 27.5M 4.51G 78.51(-0.24) 27.6M 4.51G 68.30(+0.06) 27.7M 4.51G
Swin-Tiny(ours) 96.92(+3.33) 27.6M 4.52G 83.92(+5.17) 27.6M 4.52G 71.96(+3.72) 27.7M 4.52G
Swin-Tinyw/oshift-window(ours) 97.18(+3.59) 27.6M 4.52G 83.38(+4.63) 27.6M 4.52G 72.36(+4.12) 27.7M 4.52G
Swin-Tinykernel3+5(ours) 97.06(+3.47) 27.7M 4.56G 83.84(+5.09) 27.8M 4.56G 72.74(+4.50) 27.8M 4.56G
by merging adjacent image patches in the following successive stage. Shifted
window-based self-attention [16] is proposed to extend the view of the tokens
instead of limiting the view of the tokens in the windows they are assigned.
In the experiments, we investigate the effectiveness of our method applied to
Swin Transformer, which is demonstrated in Table 5.
Theshiftedwindowapproachdoesnothavetoomucheffectontheperformanceofsmalldatasets. SwinTransformermodelwithourmethodhasmuch
better accuracy than the original model with negligible parameter overhead.
In addition, “kernel 3+5” means parallel DWConv modules have kernel size
3 and 5, respectively. Independent parallel DWConv modules with different
kernels increase the accuracy in some cases, but the number of parameters
and computations would be slightly increased.
We also utilize GRAD-CAM [52] to visualize the focus areas of the models, as depicted in Fig. 4. The Transformer models exhibit global views of
images, while Transformer models might overlook some objects due to a lack
of local information, especially when the objects are relatively small. With
our method, both global and local information could be captured and enhanced by each other, which could improve the performance of the models.
The convergence of our approach is significantly faster than the original
models, which is demonstrated in Fig. 5. The accuracy on val set is recorded
for each epoch on Tiny-ImageNet for all models. Our method exhibits much
higherperformanceandconsiderablyfasterconvergencespeed. Ourapproach
could reach a similar accuracy at around or less than 100 epochs while the
original models require 300 epochs to attain the same accuracy. Similar
performance curves are observed for CIFAR-10 and CIFAR-100.
16

<!-- Page 17 -->


### ViT ViT (ours) Swin Swin (ours)

Figure 4: Some Grad-CAM visualization with ViT-Tiny and Swin-Tiny models. The
vanilla Transformer models tend to capture the global information, as illustrated in the
CAM visualizations. With our method, the models are able to capture both local details
and global perspectives, particularly when dealing with smaller objects. Please note that
theoriginalimagesinthefigurearefromtheTiny-ImageNetdatasetwithalowresolution
of 64×64 pixels. Thus, they appear blurred when enlarged.

### Classification Performance on ImageNet-1K

In addition to the small datasets, we have also evaluated the models on a
relatively large dataset, ImageNet-1K [41], to further verify the effectiveness
of our approach. ImageNet-1K [41] contains nearly 1.3 million images for
training and 50k images for validation. For ImageNet-1K [41], The batch
size is 1024 with 8 NVIDIA V100 GPUs and the base learning rate is 1e-3.
We utilize CaiT [10] and Swin Transformer [16] to illustrate the performance of our approach on ImageNet. The kernel size for our method is 3×3
and the DWConv module is applied to each Transformer block. When our
approach is applied to the models, the positional embeddings and talking
heads attention in CaiT are retained for better accuracy, while LayerScale
is eliminated. For Swin Transformer, our approach is directly applied to
the model without any other changes. The experimental results are demonstrated in Table 6. We employ top-1 accuracy to measure the performance
of the models and the results of ResNet models are extracted from [54].
The performance of CaiT and Swin-Transformer on ImageNet-1K is further
boosted (up to 2%) by our method.
Moreover, in comparison to the convolutional counterparts like ResNet
17

<!-- Page 18 -->

Figure 5: The accuracy for val set during the training on Tiny-ImageNet for 300 epochs.
Thebluecurvesindicateourmethodandtheredcurvesarefromtheoriginalmodels. The
accuracy for val set is recorded for each epoch. The convergence of the models with our
approach is much faster than the original models.
[53], our approach still has superior performance with insignificant parameters and FLOPs overhead. Especially when the layers of the Transformer
models go deeper (e.g., CaiT-xxs24), the improvement is even higher on Im-
18

<!-- Page 19 -->

Table 6: The performance on ImageNet-1K

### Model Accuracy Params FLOPs Year

ResNet-18[53][54] 71.5 11.7M 1.8G 2016
ResNet-34[53][54] 76.4 21.8M 3.7G 2016

### ResNet-50[53][54] 80.4 25.6M 4.1G 2016

SE-ResNet-50[55][54] 80.0 28.1M 4.1G 2018

### DeiT-Ti[9][27] 72.2 5.7M 1.3G 2021

Visformer-Ti[56] 78.6 10.3M 1.3G 2021

### PVT-Tiny[11] 75.1 13.2M 1.9G 2021

DeiT-S[9][27] 79.9 22.1M 4.6G 2021
PVT-Small[11] 79.8 24.5M 3.8G 2021

## Msg-T[17] 80.9 28M 4.6G 2022


### DiT-B1[57] 79.9 30.3M 2.0G 2023

Visformer-S[56] 81.5 40.2M 4.9G 2021

### CaiT-xxs12 74.85 6.6M 1.3G -

CaiT-xxs24 77.66 11.9M 2.5G -

### Swin-Tiny 81.14 28.3M 4.5G -


### CaiT-xxs12(ours) 75.89(+1.04) 6.6M 1.3G -

CaiT-xxs24(ours) 79.66(+2.00) 12.0M 2.5G -
Swin-Tiny(ours) 81.73(+0.59) 28.3M 4.5G -
ageNet.
We also visualize the convergence curve of CaiT-xxs24 on ImageNet. As
illustrated in Fig. 6, the convergence rate of our approach is much faster
than the original model by a large margin when the epoch is less than 100.
This experiment indicates that our proposed approach could achieve higher
accuracy with significantly faster convergence speed on a relatively large
dataset.

### Object Detection and Instance Segmentation

In addition to Image Classification, we apply the proposed approach to
object detection and instance segmentation and conduct the experiments on
COCO dataset [42] with Mask RCNN [58] and Cascade Mask R-CNN [59].
The backbone utilized in the experiments is Swin-Tiny [16]. The models are
trained from scratch without pre-trained backbones.
19

<!-- Page 20 -->

Figure 6: The accuracy of CaiT-xxs24 for val set during the training on ImageNet for 300
epochs. Thebluecurvedemonstratesourmethod. Theconvergencerateforourapproach
is much faster than the original model.
For the experimental settings, we employ AdamW [44] as the optimizer
and the warmup iterations are 500. We utilize four NVIDIA P100 GPUs
to train the model with 2 samples for each GPU. The initial learning rate
is set at 5e-5 and the learning rate is reduced by 10 at epochs 9 and 12,
respectively. The image scale for the experiments is 1333×800. The total
epochs for the experiments are 12.
The results for the experiments of object detection and instance segmentation are illustrated in Table 7, where “Cas Mask-RCNN” stands for
“Cascade Mask-RCNN”. From the definition in COCO [42], “mAP” refers
to the average precision results that are averaged over all classes. The average precision is calculated by averaging the results over IoU thresholds from
0.5 to 0.95 with a step of 0.05. Additionally, “AP ” represents the average
50
precision computed using only the IoU threshold of 0.5 and “AP ” indicates
75
the average precision computed using only the IoU threshold of 0.75. Additionally, the visualization of the original method and our proposed approach
20

<!-- Page 21 -->

Table 7: Experiments for Object Detection and Instance Segmentation
ObjectDetection InstanceSegmentation

### Model

mAP AP50 AP75 mAP AP50 AP75

### Mask-RCNN 28.2 48.3 29.3 27.4 45.6 28.7

Mask-RCNN(ours) 30.6 50.2 32.6 28.9 47.4 30.6

### CasMask-RCNN 35.3 52.5 38.0 31.4 49.8 33.7


### CasMask-RCNN(ours) 36.2 53.0 39.1 32.1 50.6 34.5

Figure 7: The visualization of object detection and instance segmentation between the
original method (the first row) and ours (the second row) with Mask-RCNN. The results
demonstratethatourapproachbetterdetectssmallobjectsandproducesmoreaccurately
predicted boundaries for the objects.
with Mask-RCNN [58] is illustrated in Fig. 7. In Fig. 7, the first row demonstrates the visualization results of the original model and the second row
indicates the visualization results of our proposed model.
The experimental results clearly show that our approach improves the
performance of backbone networks for object detection and instance segmentation,demonstratingtheeffectivenessofourproposedmethodacrossvarious
vision tasks. The effectiveness likely stems from the fine-detailed information
captured by the proposed DWConv module. Object detection and instance
segmentation require detailed information for predicting object boundaries
and pixel-level labels, respectively. Vision Transformers might lack the ability to capture extensive fine-detailed information, especially when used as
the backbone. Our proposed DWConv module complements this limitation
with minimal overhead.
21

<!-- Page 22 -->


### Analysis

The proposed DWConv module, which bypasses the entire Transformer
block, demonstrates higher accuracy for image classification, object detection, and instance segmentation when the models are trained from scratch.
Additionally, this module enables Transformer models to achieve a much
faster convergence rate for image classification, especially on relatively small
datasets. Furthermore, our approach can significantly enhance small-size
Transformer models, even surpassing large-size original Transformer models with substantially more parameters and computations on small datasets
for image classification. Our approach illustrates both the effectiveness and
efficiency of Vision Transformer models.
Although our architecture performs well on relatively small datasets due
to the inductive bias introduced by the DWConv module, the improvement
might not be as pronounced when the dataset is relatively large. The abundant data can mitigate the drawbacks of Transformer models. In addition,
since the proposed DWConv module is lightweight and plug-and-play, it may
not show significant improvement when models have a large number of parametersandcomputations. Alargenumberofparametersandcomputations
can increase the representation ability of Transformer models and potentially
remedy the lack of inductive bias, albeit inefficiently. However, our proposed
models enhance both the effectiveness and efficiency of Transformer models,
achieving higher accuracy than some large models, despite having significantly fewer parameters and computations.
Moreover, our method may not show significant improvement for transfer
learning. One strength of our proposed approach is that our light-weight
module can be utilized in most Transformer models, potentially enhancing
performance, particularlyonsmalldatasets, whentrainingfromscratch. The
experiments in this paper are all conducted with training from scratch. The
possible reason for the lack of significant improvement in transfer learning
is that pre-trained models already possess substantial representation ability,
reducing the necessity for the inductive bias introduced by our approach.
Thus, our proposed module may not provide much additional benefit when
pre-trained models are applied to other tasks or datasets for fine-tuning.

## Conclusion

Inthispaper, wehavepresentedastraightforwardyetimpactfulapproach
that utilizes Depth-Wise Convolution modules to bypass Transformer blocks,
22

<!-- Page 23 -->

enabling Vision Transformer models to capture both global and local information with minimal overhead. Extensive experimental evaluations show
that small Transformer models, when equipped with our method, outperform
larger Transformer models with significantly more parameters and FLOPs on
small datasets for image classification. Our approach also significantly improves performance on ImageNet-1K [41] for classification and COCO [42]
for object detection and instance segmentation when trained from scratch.
Additionally, we introduce several architecture variants tailored to different
models and objectives. We anticipate that our method will inspire further
researchonVisionTransformers,particularlyinthecontextofsmalldatasets.

### Acknowledgements

The project is partly supported by the Natural Sciences and Engineering
Research Council of Canada (NSERC) under grant numbers 1-51-48183 and
1-51-48933.

### References

[1] A.Vaswani, N.Shazeer, N.Parmar, J.Uszkoreit, L.Jones, A.N.Gomez,
L(cid:32) . Kaiser, I. Polosukhin, Attention is all you need, Advances in neural
information processing systems 30 (2017).
[2] A. Dosovitskiy, L. Beyer, A. Kolesnikov, D. Weissenborn, X. Zhai,
T. Unterthiner, M. Dehghani, M. Minderer, G. Heigold, S. Gelly, et al.,
An image is worth 16x16 words: Transformers for image recognition at
scale, arXiv preprint arXiv:2010.11929 (2020).
[3] A. G. Howard, M. Zhu, B. Chen, D. Kalenichenko, W. Wang,
T. Weyand, M. Andreetto, H. Adam, Mobilenets: Efficient convolutional neural networks for mobile vision applications, arXiv preprint
arXiv:1704.04861 (2017).
[4] K. Patel, A. M. Bur, F. Li, G. Wang, Aggregating global features into
local vision transformer, in: 2022 26th International Conference on Pattern Recognition (ICPR), IEEE, 2022, pp. 1141–1147.
[5] X. Chen, Q. Hu, K. Li, C. Zhong, G. Wang, Accumulated trivial attention matters in vision transformers on small datasets, in: Proceedings of
23

<!-- Page 24 -->

the IEEE/CVF Winter Conference on Applications of Computer Vision,
2023, pp. 3984–3992.
[6] L. Zhu, X. Wang, Z. Ke, W. Zhang, R. W. Lau, Biformer: Vision transformerwithbi-levelroutingattention,in: ProceedingsoftheIEEE/CVF
conferenceoncomputervisionandpatternrecognition, 2023, pp.10323–
10333.
[7] Y. Wang, H. Zhu, G. Wang, Pst-net: Point cloud completion network
based on local geometric feature reuse and neighboring recovery with
taylorapproximation, in: 2023InternationalJointConferenceonNeural
Networks (IJCNN), IEEE, 2023, pp. 1–8.
[8] U.Sajid, X.Chen, H.Sajid, T.Kim, G.Wang, Audio-visualtransformer
based crowd counting, in: Proceedings of the IEEE/CVF International
Conference on Computer Vision, 2021, pp. 2249–2259.
[9] H. Touvron, M. Cord, M. Douze, F. Massa, A. Sablayrolles, H. J´egou,
Training data-efficient image transformers & distillation through attention, in: International conference on machine learning, PMLR, 2021, pp.
10347–10357.
[10] H. Touvron, M. Cord, A. Sablayrolles, G. Synnaeve, H. J´egou, Going
deeper with image transformers, in: Proceedings of the IEEE/CVF international conference on computer vision, 2021, pp. 32–42.
[11] W. Wang, E. Xie, X. Li, D.-P. Fan, K. Song, D. Liang, T. Lu, P. Luo,
L. Shao, Pyramid vision transformer: A versatile backbone for dense
prediction without convolutions, in: Proceedings of the IEEE/CVF international conference on computer vision, 2021, pp. 568–578.
[12] B. Heo, S. Yun, D. Han, S. Chun, J. Choe, S. J. Oh, Rethinking spatial
dimensions of vision transformers, in: Proceedings of the IEEE/CVF
International Conference on Computer Vision, 2021, pp. 11936–11945.
[13] B. Chen, P. Li, B. Li, C. Li, L. Bai, C. Lin, M. Sun, J. Yan, W. Ouyang,
Psvit: Bettervisiontransformerviatokenpoolingandattentionsharing,
arXiv preprint arXiv:2108.03428 (2021).
[14] X. Chen, Y. Qin, W. Xu, A. M. Bur, C. Zhong, G. Wang, Improving
vision transformers on small datasets by increasing input information
24

<!-- Page 25 -->

density in frequency domain, in: IEEE/CVF International Conference
on Computer Vision Workshops (ICCVW), Vol. 2, 2022.
[15] X. Chen, J. Liu, Y. Wang, M. Brand, G. Wang, T. Koike-Akino, et al.,
Superlora: Parameter-efficient unified adaptation of multi-layer attention modules, arXiv preprint arXiv:2403.11887 (2024).
[16] Z. Liu, Y. Lin, Y. Cao, H. Hu, Y. Wei, Z. Zhang, S. Lin, B. Guo, Swin
transformer: Hierarchical vision transformer using shifted windows, in:
Proceedings of the IEEE/CVF international conference on computer
vision, 2021, pp. 10012–10022.
[17] J. Fang, L. Xie, X. Wang, X. Zhang, W. Liu, Q. Tian, Msg-transformer:
Exchanginglocalspatialinformationbymanipulatingmessengertokens,
in: Proceedings of the IEEE/CVF Conference on Computer Vision and
Pattern Recognition, 2022, pp. 12063–12072.
[18] X. Chu, Z. Tian, Y. Wang, B. Zhang, H. Ren, X. Wei, H. Xia, C. Shen,
Twins: Revisiting the design of spatial attention in vision transformers,
Advances in Neural Information Processing Systems 34 (2021) 9355–
9366.
[19] Z. Huang, Y. Ben, G. Luo, P. Cheng, G. Yu, B. Fu, Shuffle transformer: Rethinking spatial shuffle for vision transformer, arXiv preprint
arXiv:2106.03650 (2021).
[20] H. Wu, B. Xiao, N. Codella, M. Liu, X. Dai, L. Yuan, L. Zhang, Cvt:
Introducing convolutions to vision transformers, in: Proceedings of the
IEEE/CVF international conference on computer vision, 2021, pp. 22–
31.
[21] A. Srinivas, T.-Y. Lin, N. Parmar, J. Shlens, P. Abbeel, A. Vaswani,
Bottleneck transformers for visual recognition, in: Proceedings of the
IEEE/CVF conference on computer vision and pattern recognition,
2021, pp. 16519–16529.
[22] Y. Li, K. Zhang, J. Cao, R. Timofte, L. Van Gool, Localvit: Bringing
locality to vision transformers, arXiv preprint arXiv:2104.05707 (2021).
25

<!-- Page 26 -->

[23] J. Guo, K. Han, H. Wu, Y. Tang, X. Chen, Y. Wang, C. Xu, Cmt:
Convolutional neural networks meet vision transformers, in: Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern
Recognition, 2022, pp. 12175–12185.
[24] Y. Chen, X. Dai, D. Chen, M. Liu, X. Dong, L. Yuan, Z. Liu, Mobileformer: Bridging mobilenet and transformer, in: Proceedings of the
IEEE/CVF Conference on Computer Vision and Pattern Recognition,
2022, pp. 5270–5279.
[25] Z. Lu, H. Xie, C. Liu, Y. Zhang, Bridging the gap between vision transformers and convolutional neural networks on small datasets, Advances
in Neural Information Processing Systems 35 (2022) 14663–14677.
[26] Y. Xu, Q. Zhang, J. Zhang, D. Tao, Vitae: Vision transformer advanced
by exploring intrinsic inductive bias, Advances in neural information
processing systems 34 (2021) 28522–28535.
[27] Q. Zhang, Y. Xu, J. Zhang, D. Tao, Vitaev2: Vision transformer advanced by exploring inductive bias for image recognition and beyond,
International Journal of Computer Vision (2023) 1–22.
[28] Q. Chen, Q. Wu, J. Wang, Q. Hu, T. Hu, E. Ding, J. Cheng, J. Wang,
Mixformer: Mixing features across windows and dimensions, in: Proceedings of the IEEE/CVF conference on computer vision and pattern
recognition, 2022, pp. 5249–5259.
[29] Z. Wei, H. Pan, L. Li, M. Lu, X. Niu, P. Dong, D. Li, Dmformer:
Closing the gap between cnn and vision transformers, in: ICASSP 2023-
2023 IEEE International Conference on Acoustics, Speech and Signal
Processing (ICASSP), IEEE, 2023, pp. 1–5.
[30] X. Nie, H. Jin, Y. Yan, X. Chen, Z. Zhu, D. Qi, Scopevit: Scale-aware
vision transformer, Pattern Recognition 153 (2024) 110470.
[31] K. Su, L. Cao, B. Zhao, N. Li, D. Wu, X. Han, Y. Liu, Dctvit: Discrete
cosine transform meet vision transformers, Neural Networks 172 (2024)
106139.
[32] A. Jamali, S. K. Roy, P. Ghamisi, Wetmapformer: A unified deep
cnn and vision transformer for complex wetland mapping, International
26

<!-- Page 27 -->

Journal of Applied Earth Observation and Geoinformation 120 (2023)
103333.
[33] Q. Wang, Y. Liu, Z. Xiong, Y. Yuan, Hybrid feature aligned network
for salient object detection in optical remote sensing imagery, IEEE
transactions on geoscience and remote sensing 60 (2022) 1–15.
[34] Y. Liu, Z. Xiong, Y. Yuan, Q. Wang, Transcending pixels: boosting
saliency detection via scene understanding from aerial imagery, IEEE
Transactions on Geoscience and Remote Sensing (2023).
[35] F. Liu, Y. Kong, L. Zhang, G. Feng, B. Yin, Local-global coordination
with transformers for referring image segmentation, Neurocomputing
522 (2023) 39–52.
[36] J. L. Ba, J. R. Kiros, G. E. Hinton, Layer normalization, arXiv preprint
arXiv:1607.06450 (2016).
[37] D. Hendrycks, K. Gimpel, Gaussian error linear units (gelus), arXiv
preprint arXiv:1606.08415 (2016).
[38] S. Ioffe, C. Szegedy, Batch normalization: Accelerating deep network
trainingbyreducinginternalcovariateshift, in: Internationalconference
on machine learning, pmlr, 2015, pp. 448–456.
[39] A. Krizhevsky, G. Hinton, et al., Learning multiple layers of features
from tiny images (2009).
[40] Y. Le, X. Yang, Tiny imagenet visual recognition challenge, CS 231N
7 (7) (2015) 3.
[41] O. Russakovsky, J. Deng, H. Su, J. Krause, S. Satheesh, S. Ma,
Z. Huang, A. Karpathy, A. Khosla, M. Bernstein, et al., Imagenet large
scale visual recognition challenge, International journal of computer vision 115 (2015) 211–252.
[42] T.-Y. Lin, M. Maire, S. Belongie, J. Hays, P. Perona, D. Ramanan,
P. Dolla´r, C. L. Zitnick, Microsoft coco: Common objects in context,
in: Computer Vision–ECCV 2014: 13th European Conference, Zurich,
Switzerland, September 6-12, 2014, Proceedings, Part V 13, Springer,
2014, pp. 740–755.
27

<!-- Page 28 -->

[43] A.Steiner, A.Kolesnikov, X.Zhai, R.Wightman, J.Uszkoreit, L.Beyer,
How to train your vit? data, augmentation, and regularization in vision
transformers, arXiv preprint arXiv:2106.10270 (2021).
[44] D. P. Kingma, J. Ba, Adam: A method for stochastic optimization,
arXiv preprint arXiv:1412.6980 (2014).
[45] E. D. Cubuk, B. Zoph, D. Mane, V. Vasudevan, Q. V. Le, Autoaugment: Learning augmentation policies from data, arXiv preprint
arXiv:1805.09501 (2018).
[46] Z. Zhong, L. Zheng, G. Kang, S. Li, Y. Yang, Random erasing data
augmentation, in: Proceedings of the AAAI conference on artificial intelligence, Vol. 34, 2020, pp. 13001–13008.
[47] H. Zhang, M. Cisse, Y. N. Dauphin, D. Lopez-Paz, mixup: Beyond
empirical risk minimization, arXiv preprint arXiv:1710.09412 (2017).
[48] S. Yun, D. Han, S. J. Oh, S. Chun, J. Choe, Y. Yoo, Cutmix: Regularization strategy to train strong classifiers with localizable features,
in: Proceedings of the IEEE/CVF international conference on computer
vision, 2019, pp. 6023–6032.
[49] X. Chu, Z. Tian, B. Zhang, X. Wang, X. Wei, H. Xia, C. Shen, Conditional positional encodings for vision transformers, arXiv preprint
arXiv:2102.10882 (2021).
[50] W. Ma, T. Zhang, G. Wang, Miti-detr: Object detection based on
transformers with mitigatory self-attention convergence, arXiv preprint
arXiv:2112.13310 (2021).
[51] N.Shazeer, Z.Lan, Y.Cheng, N.Ding, L.Hou, Talking-headsattention,
arXiv preprint arXiv:2003.02436 (2020).
[52] R.R.Selvaraju,M.Cogswell,A.Das,R.Vedantam,D.Parikh,D.Batra,
Grad-cam: Visual explanations from deep networks via gradient-based
localization, in: Proceedings of the IEEE international conference on
computer vision, 2017, pp. 618–626.
[53] K. He, X. Zhang, S. Ren, J. Sun, Deep residual learning for image
recognition, in: Proceedings of the IEEE conference on computer vision
and pattern recognition, 2016, pp. 770–778.
28

<!-- Page 29 -->

[54] R. Wightman, H. Touvron, H. J´egou, Resnet strikes back: An improved
training procedure in timm, arXiv preprint arXiv:2110.00476 (2021).
[55] J. Hu, L. Shen, G. Sun, Squeeze-and-excitation networks, in: Proceedings of the IEEE conference on computer vision and pattern recognition,
2018, pp. 7132–7141.
[56] Z. Chen, L. Xie, J. Niu, X. Liu, L. Wei, Q. Tian, Visformer: The visionfriendly transformer, in: Proceedings of the IEEE/CVF international
conference on computer vision, 2021, pp. 589–598.
[57] Y. Ma, Z. Fei, J. Huang, Dit: Efficient vision transformers with dynamic
token routing, arXiv preprint arXiv:2308.03409 (2023).
[58] K. He, G. Gkioxari, P. Dolla´r, R. Girshick, Mask r-cnn, in: Proceedings
oftheIEEEinternationalconferenceoncomputervision,2017,pp.2961–
2969.
[59] Z. Cai, N. Vasconcelos, Cascade r-cnn: Delving into high quality object
detection, in: Proceedings of the IEEE conference on computer vision
and pattern recognition, 2018, pp. 6154–6162.
29

## Tables

**Table (Page 7):**

| Transformer Transformer Block Block LayerNorm + + + MHSA LayerNorm FFN LayerNorm + + + MHSA LayerNorm FFN ... ... DWConv DWConv module module GELU BatchNorm DWConv DWConv ... 1D -> 2D 2D -> 1D ... module |  |
|---|---|
|  | GELU BatchNorm DWConv ... 1D -> 2D 2D -> 1D ... |


**Table (Page 7):**

|  |  |  |  |  |  |
|---|---|---|---|---|---|
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |


**Table (Page 7):**

|  |  |  |
|---|---|---|
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |


**Table (Page 13):**

| CIFAR-10 |  |  | CIFAR-100 |  |  |  |  |
|---|---|---|---|---|---|---|---|
| Accuracy | Params | FLOPs | Accuracy | Params | FLOPs | Accuracy | Params |
| 94.01 87.83(-6.18) 96.41(+2.40) 96.32(+2.31) | 5.5M 5.5M 5.5M 5.5M | 1.26G 1.26G 1.26G 1.26G | 73.68 64.41(-9.27) 78.05(+4.37) 77.31(+3.63) | 5.5M 5.5M 5.6M 5.5M | 1.26G 1.26G 1.26G 1.26G | 59.00 53.15(-5.85) 64.10(+5.10) 63.57(+4.57) | 5.6M 5.5M 5.6M 5.5M |
| 95.09 89.27(-5.82) 97.02(+1.93) 96.96(+1.87) | 21.7M 21.6M 21.7M 21.6M | 4.61G 4.61G 4.62G 4.62G | 73.97 65.68(-8.29) 80.01(+6.04) 80.14(+6.17) | 21.7M 21.6M 21.7M 21.7M | 4.61G 4.61G 4.62G 4.62G | 60.90 53.98(-6.92) 66.86(+5.96) 66.59(+5.69) | 21.7M 21.7M 21.8M 21.7M |


**Table (Page 13):**

| CIFAR-10 | CIFAR-100 |
|---|---|
| 87.50 96.32 96.26 96.26 96.52 96.39 | 65.10 77.31 78.71 78.69 78.63 78.00 |


**Table (Page 14):**

| CIFAR-10 |  |  | CIFAR-100 |  |  |  |  |
|---|---|---|---|---|---|---|---|
| Accuracy | Params | FLOPs | Accuracy | Params | FLOPs | Accuracy | Params |
| 92.02 87.45(-4.57) 96.43(+4.41) | 6.4M 6.4M 6.4M | 1.30G 1.28G 1.29G | 73.43 70.32(-3.11) 81.72(+8.29) | 6.4M 6.4M 6.4M | 1.30G 1.28G 1.29G | 59.17 60.62(+1.45) 70.47(+11.30) | 6.5M 6.4M 6.4M |
| 93.89 97.28(+3.39) | 11.8M 11.8M | 2.53G 2.51G | 74.84 82.83(+7.99) | 11.8M 11.8M | 2.53G 2.51G | 60.97 70.64(+9.67) | 11.8M 11.8M |


**Table (Page 15):**

| CIFAR-10 | CIFAR-100 |
|---|---|
| 96.43 96.16 95.60 94.80 | 81.72 80.67 79.50 78.61 |
| 97.28 97.00 96.84 96.51 | 82.83 82.90 81.90 80.16 |


**Table (Page 16):**

| CIFAR-10 |  |  | CIFAR-100 |  |  |  |  |
|---|---|---|---|---|---|---|---|
| Accuracy | Params | FLOPs | Accuracy | Params | FLOPs | Accuracy | Params |
| 93.59 93.36(-0.23) 96.92(+3.33) 97.18(+3.59) 97.06(+3.47) | 27.5M 27.5M 27.6M 27.6M 27.7M | 4.51G 4.51G 4.52G 4.52G 4.56G | 78.75 78.51(-0.24) 83.92(+5.17) 83.38(+4.63) 83.84(+5.09) | 27.6M 27.6M 27.6M 27.6M 27.8M | 4.51G 4.51G 4.52G 4.52G 4.56G | 68.24 68.30(+0.06) 71.96(+3.72) 72.36(+4.12) 72.74(+4.50) | 27.7M 27.7M 27.7M 27.7M 27.8M |


**Table (Page 19):**

| Accuracy | Params FLOPs |
|---|---|
| 71.5 76.4 80.4 80.0 | 11.7M 1.8G 21.8M 3.7G 25.6M 4.1G 28.1M 4.1G |
| 72.2 78.6 75.1 79.9 79.8 80.9 79.9 81.5 | 5.7M 1.3G 10.3M 1.3G 13.2M 1.9G 22.1M 4.6G 24.5M 3.8G 28M 4.6G 30.3M 2.0G 40.2M 4.9G |
| 74.85 77.66 81.14 | 6.6M 1.3G 11.9M 2.5G 28.3M 4.5G |
| 75.89(+1.04) 79.66(+2.00) 81.73(+0.59) | 6.6M 1.3G 12.0M 2.5G 28.3M 4.5G |


**Table (Page 21):**

| ObjectDetection |  |  |
|---|---|---|
| mAP | AP50 AP75 | mAP |
| 28.2 30.6 | 48.3 29.3 50.2 32.6 | 27.4 28.9 |
| 35.3 36.2 | 52.5 38.0 53.0 39.1 | 31.4 32.1 |
