# Continual Learning Papers

<p align="center">
  <img src="https://github.com/ContinualAI/continual-learning-papers/blob/main/logo.png" alt="ContinualAI logo"/ width="300px" align="center">
</p>

Continual Learning papers list, curated by ContinualAI. **Search among 317 papers!**
 
You can browse the list in this file or interactively on the [ContinualAI website](https://www.continualai.org/papers/).

[Join our community](https://continualai.herokuapp.com/) on Slack to stay updated with the latest Continual Learning news.  
Visit the Continua AI wiki &rarr; http://wiki.continualai.org/

## Table of contents
[Add a new paper](https://github.com/ContinualAI/continual-learning-papers#add-a-new-paper)  
[Join the ContinualAI Zotero group](https://github.com/ContinualAI/continual-learning-papers#join-the-continualai-zotero-group)  
* [List of papers](https://github.com/ContinualAI/continual-learning-papers#list-of-papers)  
    - [Applications](https://github.com/ContinualAI/continual-learning-papers#applications)
    - [Architectural methods](https://github.com/ContinualAI/continual-learning-papers#architectural-methods)
    - [Benchmarks](https://github.com/ContinualAI/continual-learning-papers#benchmarks)
    - [Bio-inspired methods](https://github.com/ContinualAI/continual-learning-papers#bioinspired-methods)
    - [Catastrophic Forgetting studies](https://github.com/ContinualAI/continual-learning-papers#catastrophic-forgetting-studies)
    - [Classics](https://github.com/ContinualAI/continual-learning-papers#classics)
    - [Continual Few-shot learning](https://github.com/ContinualAI/continual-learning-papers#continual-few-shot-learning)
    - [Continual Meta Learning](https://github.com/ContinualAI/continual-learning-papers#continual-meta-learning)
    - [Continual Reinforcement Learning](https://github.com/ContinualAI/continual-learning-papers#continual-reinforcement-learning)
    - [Continual Sequential Learning](https://github.com/ContinualAI/continual-learning-papers#continual-sequential-learning)
    - [Dissertation and theses](https://github.com/ContinualAI/continual-learning-papers#dissertation-and-theses)
    - [Generative Replay methods](https://github.com/ContinualAI/continual-learning-papers#generative-replay-methods)
    - [Hybrid methods](https://github.com/ContinualAI/continual-learning-papers#hybrid-methods)
    - [Meta Continual Learning](https://github.com/ContinualAI/continual-learning-papers#meta-continual-learning)
    - [Metrics and Evaluation](https://github.com/ContinualAI/continual-learning-papers#metrics-and-evaluations)
    - [Neuroscience](https://github.com/ContinualAI/continual-learning-papers#neuroscience)
    - [Others](https://github.com/ContinualAI/continual-learning-papers#others)
    - [Regularization methods](https://github.com/ContinualAI/continual-learning-papers#regularization-methods)
    - [Rehearsal methods](https://github.com/ContinualAI/continual-learning-papers#rehearsal-methods)
    - [Review papers and books](https://github.com/ContinualAI/continual-learning-papers#review-papers-and-books)
    - [Robotics](https://github.com/ContinualAI/continual-learning-papers#robotics)

---------------------------------------------------

## Add a new paper
The list of papers is maintained through a Zotero group. You can join the group and help us keeping it updated (see next section).  

If you don't want to join the group, you can simply open a Github issue to suggest us a new paper (or even more than one). We will take care of adding it to the list as soon as possible. 

1. Open a new Github issue.

2. Attach your bib file containing the paper you want to include in the list. If you don't have a bib file, just provide us with the link to the paper. The link should point to a location where paper metadata can be appropriately retrieved by common reference managers.

Alternatively, you can submit a Pull Request with a modification to the bibtex files directly!

## Join the ContinualAI Zotero group

You can give your contribution to the group by **adding new papers** or by helping **annotating the existing ones**.

1. Join our [Zotero group](https://www.zotero.org/groups/2623909/continual_learning_papers/)

2. To **add a new paper**

	2.1. Add it to the group folder which best represents the paper contribution. Read some advices below if you are uncertain on this. You can add the paper from your library or directly from the paper webpage through the Zotero web browser plugin. 
    
    2.2 Make sure that at least `title`, `authors`, `item type` and `publication` are specified. The `year` must be put inside `date` field.
    
    2.3 Also put a link to the paper in the `url` field. 

3. To **annotate** an existing paper

	3.1. Check the list of existing tags in `tags.csv` file. If you want to add a new tag, please add it in there and submit a Pull Request.

	3.2. Add your tags in the `Tags` tab of Zotero. Please, remember to write the tag in square brackets e.g. `[mytag]`

	3.3. Add your notes in the `Notes` tab of Zotero.

We will periodically export the bibtex to keep the list updated. In case we forgot, join the [ContinualAI Slack](https://continualai.herokuapp.com/) and complain about our behavior in the `#wiki` channel.

### Advices to add new papers in Zotero

* Check if the paper already exist by using the `Citation Key` or the title in Zotero search bar.

* Don't forget to add the publication venue (Journal, Proceedings...). Use `publication = arXiv` if the paper is a preprint.

* We use a system based on categories. This can sometimes be limiting. In general, please consider to add the paper in the category which you consider the most relevant one. You can add the paper in at most **2** categories, if you believe that both are equally relevant.

* Please, do not add new tags if a similar category already exists.

----------------------------

## List of papers

### Applications

**25 papers**

In this section we maintain a list of all applicative papers produced on continual learning and related topics.

- [The Traffic Flow Prediction Method Using the Incremental Learning-Based CNN-LTSM Model: The Solution of Mobile Application](https://www.hindawi.com/journals/misy/2021/5579451/) by Yanli Shao, Yiming Zhao, Feng Yu, Huawei Zhu and Jinglong Fang. *Mobile Information Systems*, e5579451, 2021. [experimental] 
- [Findings of the First Shared Task on Lifelong Learning Machine Translation](https://www.aclweb.org/anthology/2020.wmt-1.2) by Loïc Barrault, Magdalena Biesialska, Marta R. Costa-jussà, Fethi Bougares and Olivier Galibert. *Proceedings of the Fifth Conference on Machine Translation*, 56--64, 2020. [framework] [nlp] 
- [Continual Learning of Predictive Models in Video Sequences via Variational Autoencoders](http://arxiv.org/abs/2006.01945) by Damian Campo, Giulia Slavic, Mohamad Baydoun, Lucio Marcenaro and Carlo Regazzoni. *arXiv*, 2020. [vision] 
- [Unsupervised Model Personalization While Preserving Privacy and Scalability: An Open Problem](http://arxiv.org/abs/2003.13296) by Matthias De Lange, Xu Jia, Sarah Parisot, Ales Leonardis, Gregory Slabaugh and Tinne Tuytelaars. *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition*, 14451--14460, 2020. [framework] [mnist] [vision] 
- [Incremental Learning for End-to-End Automatic Speech Recognition](https://arxiv.org/abs/2005.04288) by Li Fu, Xiaoxiao Li and Libo Zi. *arXiv*, 2020. [audio] 
- [Neural Topic Modeling with Continual Lifelong Learning](http://arxiv.org/abs/2006.10909) by Pankaj Gupta, Yatin Chaudhary, Thomas Runkler and Hinrich Schütze. *ICML*, 2020. [nlp] 
- [CLOPS: Continual Learning of Physiological Signals](http://arxiv.org/abs/2004.09578) by Dani Kiyasseh, Tingting Zhu and David A Clifton. *arXiv*, 2020. 
- [Clinical Applications of Continual Learning Machine Learning](https://linkinghub.elsevier.com/retrieve/pii/S2589750020301023) by Cecilia S Lee and Aaron Y Lee. *The Lancet Digital Health*, e279--e281, 2020. 
- [Continual Learning for Domain Adaptation in Chest X-ray Classification](http://arxiv.org/abs/2001.05922) by Matthias Lenga, Heinrich Schulz and Axel Saalbach. *arXiv*, 1--11, 2020. [vision] 
- [Sequential Domain Adaptation through Elastic Weight Consolidation for Sentiment Analysis](http://arxiv.org/abs/2007.01189) by Avinash Madasu and Vijjini Anvesh Rao. *arXiv*, 2020. [nlp] [rnn] 
- [RATT: Recurrent Attention to Transient Tasks for Continual Image Captioning](https://proceedings.neurips.cc/paper/2020/file/c2964caac096f26db222cb325aa267cb-Paper.pdf) by Riccardo Del Chiaro, Bartłomiej Twardowski, Andrew Bagdanov and Joost van de Weijer. *Advances in Neural Information Processing Systems*, 16736--16748, 2020. [nlp] 
- [Importance Driven Continual Learning for Segmentation Across Domains](http://arxiv.org/abs/2005.00079) by Sinan Özgür Özgün, Anne-Marie Rickmann, Abhijit Guha Roy and Christian Wachinger. *arXiv*, 1--10, 2020. [vision] 
- [LAMOL: LAnguage MOdeling for Lifelong Language Learning](https://openreview.net/forum?id=Skgxcn4YDS) by Fan-Keng Sun, Cheng-Hao Ho and Hung-Yi Lee. *ICLR*, 2020. [nlp] 
- [Non-Parametric Adaptation for Neural Machine Translation](http://arxiv.org/abs/1903.00058) by Ankur Bapna and Orhan Firat. *arXiv*, 2019. [nlp] 
- [Episodic Memory in Lifelong Language Learning](http://arxiv.org/abs/1906.01076) by Cyprien de Masson D'Autume, Sebastian Ruder, Lingpeng Kong and Dani Yogatama. *NeurIPS*, 2019. [nlp] 
- [Continual Adaptation for Efficient Machine Communication](http://arxiv.org/abs/1911.09896) by Robert D Hawkins, Minae Kwon, Dorsa Sadigh and Noah D Goodman. *Proceedings of the ICML Workshop on Adaptive & Multitask Learning: Algorithms & Systems*, 2019. 
- [Continual Learning for Sentence Representations Using Conceptors](http://arxiv.org/abs/1904.09187) by Tianlin Liu, Lyle Ungar and João Sedoc. *NAACL*, 2019. [nlp] 
- [Lifelong and Interactive Learning of Factual Knowledge in Dialogues](http://arxiv.org/abs/1907.13295 https://www.aclweb.org/anthology/W19-5903) by Sahisnu Mazumder, Bing Liu, Shuai Wang and Nianzu Ma. *Proceedings of the 20th Annual SIGdial Meeting on Discourse and Dialogue*, 21--31, 2019. [nlp] 
- [Making Good on LSTMs' Unfulfilled Promise](http://arxiv.org/abs/1911.04489) by Daniel Philps, Artur d'Avila Garcez and Tillman Weyde. *arXiv*, 2019. [rnn] 
- [Overcoming Catastrophic Forgetting During Domain Adaptation of Neural Machine Translation](https://www.aclweb.org/anthology/N19-1209) by Brian Thompson, Jeremy Gwinnup, Huda Khayrallah, Kevin Duh and Philipp Koehn. *Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers)*, 2062--2068, 2019. [nlp] [rnn] 
- [Lifelong Learning for Scene Recognition in Remote Sensing Images](https://ieeexplore.ieee.org/document/8662768/) by Min Zhai, Huaping Liu and Fuchun Sun. *IEEE Geoscience and Remote Sensing Letters*, 1472--1476, 2019. [vision] 
- [Towards Continual Learning in Medical Imaging](http://arxiv.org/abs/1811.02496) by Chaitanya Baweja, Ben Glocker and Konstantinos Kamnitsas. *NeurIPS Workshop on Continual Learning*, 1--4, 2018. [vision] 
- [Toward Continual Learning for Conversational Agents](http://arxiv.org/abs/1712.09943) by  and Sungjin Lee. *arXiv*, 2018. [nlp] 
- [Toward an Architecture for Never-Ending Language Learning](https://www.aaai.org/ocs/index.php/AAAI/AAAI10/paper/view/1879) by Andrew Carlson, Justin Betteridge, Bryan Kisiel, Burr Settles, Estevam R. Hruschka and Tom M. Mitchell. *Proceedings of the Twenty-Fourth AAAI Conference on Artificial Intelligence*, 1306--1313, 2010. [nlp] 
- [Principles of Lifelong Learning for Predictive User Modeling](http://link.springer.com/10.1007/978-3-540-73078-1_7) by Ashish Kapoor and Eric Horvitz. *User Modeling 2007*, 37--46, 2009. 

### Architectural Methods

**32 papers**

In this section we collect all the papers introducing a continual learning strategy employing some architectural methods.

- [Architecture Matters in Continual Learning](http://arxiv.org/abs/2202.00275) by Seyed Iman Mirzadeh, Arslan Chaudhry, Dong Yin, Timothy Nguyen, Razvan Pascanu, Dilan Gorur and Mehrdad Farajtabar. *arXiv*, 2022. 
- [Structured Ensembles: An Approach to Reduce the Memory Footprint of Ensemble Methods](https://linkinghub.elsevier.com/retrieve/pii/S0893608021003579) by Jary Pomponi, Simone Scardapane and Aurelio Uncini. *Neural Networks*, 407--418, 2021. 
- [Continual Learning via Bit-Level Information Preserving](https://openaccess.thecvf.com/content/CVPR2021/html/Shi_Continual_Learning_via_Bit-Level_Information_Preserving_CVPR_2021_paper.html) by Yujun Shi, Li Yuan, Yunpeng Chen and Jiashi Feng. *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition*, 16674--16683, 2021. 
- [Continual Learning with Adaptive Weights (CLAW)](https://openreview.net/forum?id=Hklso24Kwr) by Tameem Adel, Han Zhao and Richard E Turner. *International Conference on Learning Representations*, 2020. [cifar] [mnist] [omniglot] 
- [Continual Learning with Gated Incremental Memories for Sequential Data Processing](http://arxiv.org/abs/2004.04077) by Andrea Cossu, Antonio Carta and Davide Bacciu. *Proceedings of the 2020 International Joint Conference on Neural Networks (IJCNN 2020)*, 2020. [mnist] [rnn] 
- [Continual Learning in Recurrent Neural Networks](https://openreview.net/forum?id=8xeBUgD8u9) by Benjamin Ehret, Christian Henning, Maria Cervera, Alexander Meulemans, Johannes Von Oswald and Benjamin F. Grewe. *International Conference on Learning Representations*, 2020. [audio] [rnn] 
- [Explainability in Deep Reinforcement Learning](http://arxiv.org/abs/2008.06693) by Alexandre Heuillet, Fabien Couthouis and Natalia Díaz-Rodr\ǵuez. *arXiv:2008.06693 [cs]*, 2020. 
- [A Neural Dirichlet Process Mixture Model for Task-Free Continual Learning](https://openreview.net/forum?id=SJxSOJStPr) by Soochan Lee, Junsoo Ha, Dongsu Zhang and Gunhee Kim. *International Conference on Learning Representations*, 2020. 
- [Bayesian Nonparametric Weight Factorization for Continual Learning](http://arxiv.org/abs/2004.10098) by Nikhil Mehta, Kevin J Liang and Lawrence Carin. *arXiv*, 1--17, 2020. [bayes] [cifar] [mnist] [sparsity] 
- [SpaceNet: Make Free Space For Continual Learning](http://arxiv.org/abs/2007.07617) by Ghada Sokar, Decebal Constantin Mocanu and Mykola Pechenizkiy. *arXiv*, 2020. [cifar] [fashion] [mnist] [sparsity] 
- [Efficient Continual Learning with Modular Networks and Task-Driven Priors](http://arxiv.org/abs/2012.12631) by Tom Veniat, Ludovic Denoyer and Marc'Aurelio Ranzato. *arXiv*, 2020. [experimental] 
- [Progressive Memory Banks for Incremental Domain Adaptation](https://openreview.net/forum?id=BkepbpNFwr) by Nabiha Asghar, Lili Mou, Kira A Selby, Kevin D Pantasdo, Pascal Poupart and Xin Jiang. *International Conference on Learning Representations*, 2019. [nlp] [rnn] 
- [Autonomous Deep Learning: Continual Learning Approach for Dynamic Environments](https://epubs.siam.org/doi/10.1137/1.9781611975673.75) by Andri Ashfahani and Mahardhika Pratama. *Proceedings of the 2019 SIAM International Conference on Data Mining*, 666--674, 2019. [mnist] 
- [Compacting, Picking and Growing for Unforgetting Continual Learning](http://papers.nips.cc/paper/9518-compacting-picking-and-growing-for-unforgetting-continual-learning.pdf) by Steven C Y Hung, Cheng-Hao Tu, Cheng-En Wu, Chien-Hung Chen, Yi-Ming Chan and Chu-Song Chen. *NeurIPS*, 13669--13679, 2019. [cifar] [imagenet] 
- [Learn to Grow: A Continual Structure Learning Framework for Overcoming Catastrophic Forgetting](https://arxiv.org/pdf/1904.00310.pdf) by Xilai Li, Yingbo Zhou, Tianfu Wu, Richard Socher and Caiming Xiong. *arXiv*, 2019. [cifar] [mnist] 
- [Towards AutoML in the Presence of Drift: First Results](http://arxiv.org/abs/1907.10772) by Jorge G. Madrid, Hugo Jair Escalante, Eduardo F. Morales, Wei-Wei Tu, Yang Yu, Lisheng Sun-Hosoya, Isabelle Guyon and Michele Sebag. *arXiv*, 2019. 
- [Continual Unsupervised Representation Learning](https://papers.nips.cc/paper/8981-continual-unsupervised-representation-learning.pdf) by Dushyant Rao, Francesco Visin, Andrei A Rusu, Yee Whye Teh, Razvan Pascanu and Raia Hadsell. *NeurIPS*, 2019. [mnist] [omniglot] 
- [A Progressive Model to Enable Continual Learning for Semantic Slot Filling](https://www.aclweb.org/anthology/D19-1126.pdf) by Yilin Shen, Xiangyu Zeng and Hongxia Jin. *Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing*, 1279--1284, 2019. [nlp] 
- [Adaptive Compression-based Lifelong Learning](http://arxiv.org/abs/1907.09695) by Shivangi Srivastava, Maxim Berman, Matthew B Blaschko and Devis Tuia. *BMVC*, 2019. [imagenet] [sparsity] 
- [Frosting Weights for Better Continual Training](https://ieeexplore.ieee.org/document/8999083/) by Xiaofeng Zhu, Feng Liu, Goce Trajcevski and Dingding Wang. *2019 18th IEEE International Conference On Machine Learning And Applications (ICMLA)*, 506--510, 2019. [cifar] [mnist] 
- [Dynamic Few-Shot Visual Learning Without Forgetting](http://openaccess.thecvf.com/content_cvpr_2018/html/Gidaris_Dynamic_Few-Shot_Visual_CVPR_2018_paper.html) by Spyros Gidaris and Nikos Komodakis. *Proceedings of the IEEE Computer Society Conference on Computer Vision and Pattern Recognition*, 4367--4375, 2018. [imagenet] [vision] 
- [HOUDINI: Lifelong Learning as Program Synthesis](http://papers.nips.cc/paper/8086-houdini-lifelong-learning-as-program-synthesis.pdf) by Lazar Valkov, Dipak Chaudhari, Akash Srivastava, Charles Sutton and Swarat Chaudhuri. *NeurIPS*, 8687--8698, 2018. 
- [Reinforced Continual Learning](http://papers.nips.cc/paper/7369-reinforced-continual-learning) by Ju Xu and Zhanxing Zhu. *Advances in Neural Information Processing Systems*, 899--908, 2018. [cifar] [mnist] 
- [Lifelong Learning With Dynamically Expandable Networks](https://arxiv.org/abs/1708.01547) by Jaehong Yoon, Eunho Yang, Jeongtae Lee and Sung Ju Hwang. *ICLR*, 11, 2018. [cifar] [mnist] [sparsity] 
- [Expert Gate: Lifelong Learning with a Network of Experts](http://arxiv.org/abs/1611.06194) by Rahaf Aljundi, Punarjay Chakravarty and Tinne Tuytelaars. *IEEE Conference on Computer Vision and Pattern Recognition (CVPR)*, 2017. [vision] 
- [Neurogenesis Deep Learning](https://www.osti.gov/biblio/1424868) by Timothy John Draelos, Nadine E Miner, Christopher Lamb, Jonathan A Cox, Craig Michael Vineyard, Kristofor David Carlson, William Mark Severa, Conrad D James and James Bradley Aimone. *IJCNN*, 2017. [mnist] 
- [Net2Net: Accelerating Learning via Knowledge Transfer](http://arxiv.org/abs/1511.05641) by Tianqi Chen, Ian Goodfellow and Jonathon Shlens. *ICLR*, 2016. 
- [Continual Learning through Evolvable Neural Turing Machines](https://core.ac.uk/reader/84859350) by Benno Luders, Mikkel Schlager and Sebastian Risi. *NIPS 2016 Workshop on Continual Learning and Deep Networks*, 2016. 
- [Progressive Neural Networks](http://arxiv.org/abs/1606.04671) by Andrei A Rusu, Neil C Rabinowitz, Guillaume Desjardins, Hubert Soyer, James Kirkpatrick, Koray Kavukcuoglu, Razvan Pascanu and Raia Hadsell. *arXiv*, 2016. [mnist] 
- [Knowledge Transfer in Deep Block-Modular Neural Networks](http://lpp.psycho.univ-paris5.fr/feel) by Alexander V. Terekhov, Guglielmo Montone and J. Kevin O'Regan. *Conference on Biomimetic and Biohybrid Systems*, 268--279, 2015. [vision] 
- [ELLA: An Efficient Lifelong Learning Algorithm](http://proceedings.mlr.press/v28/ruvolo13.html) by Paul Ruvolo and Eric Eaton. *International Conference on Machine Learning*, 507--515, 2013. 
- [A Self-Organising Network That Grows When Required](https://linkinghub.elsevier.com/retrieve/pii/S0893608002000783) by Stephen Marsland, Jonathan Shapiro and Ulrich Nehmzow. *Neural Networks*, 1041--1058, 2002. [som] 

### Benchmarks

**9 papers**

In this section we list all the papers related to new benchmarks proposals for continual learning and related topics. 

- [Is Class-Incremental Enough for Continual Learning?](http://arxiv.org/abs/2112.02925) by Andrea Cossu, Gabriele Graffieti, Lorenzo Pellegrini, Davide Maltoni, Davide Bacciu, Antonio Carta and Vincenzo Lomonaco. *arXiv*, 2021. 
- [Efficient Continual Learning with Modular Networks and Task-Driven Priors](http://arxiv.org/abs/2012.12631) by Tom Veniat, Ludovic Denoyer and Marc'Aurelio Ranzato. *ICLR*, 2021. 
- [Defining Benchmarks for Continual Few-Shot Learning](http://arxiv.org/abs/2004.11967) by Antreas Antoniou, Massimiliano Patacchiola, Mateusz Ochal and Amos Storkey. *arXiv*, 2020. [imagenet] 
- [Evaluating Online Continual Learning with CALM](https://arxiv.org/abs/2004.03340v2) by Germán Kruszewski, Ionut-Teodor Sorodoc and Tomas Mikolov. *arXiv*, 2020. [nlp] [rnn] 
- [Continual Reinforcement Learning in 3D Non-Stationary Environments](https://openaccess.thecvf.com/content_CVPRW_2020/html/w15/Lomonaco_Continual_Reinforcement_Learning_in_3D_Non-Stationary_Environments_CVPRW_2020_paper.html) by Vincenzo Lomonaco, Karan Desai, Eugenio Culurciello and Davide Maltoni. *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops*, 248--249, 2020. 
- [Stream-51: Streaming Classification and Novelty Detection From Videos](https://openaccess.thecvf.com/content_CVPRW_2020/html/w15/Roady_Stream-51_Streaming_Classification_and_Novelty_Detection_From_Videos_CVPRW_2020_paper.html) by Ryne Roady, Tyler L. Hayes, Hitesh Vaidya and Christopher Kanan. *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops*, 228--229, 2020. 
- [OpenLORIS-Object: A Robotic Vision Dataset and Benchmark for Lifelong Deep Learning](http://arxiv.org/abs/1911.06487) by Qi She, Fan Feng, Xinyue Hao, Qihan Yang, Chuanlin Lan, Vincenzo Lomonaco, Xuesong Shi, Zhengwei Wang, Yao Guo, Yimin Zhang, Fei Qiao and Rosa H M Chan. *arXiv*, 1--8, 2019. [vision] 
- [Incremental Object Learning From Contiguous Views](https://openaccess.thecvf.com/content_CVPR_2019/html/Stojanov_Incremental_Object_Learning_From_Contiguous_Views_CVPR_2019_paper.html) by Stefan Stojanov, Samarth Mishra, Ngoc Anh Thai, Nikhil Dhanda, Ahmad Humayun, Chen Yu, Linda B. Smith and James M. Rehg. *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition*, 8777--8786, 2019. 
- [CORe50: A New Dataset and Benchmark for Continuous Object Recognition](http://proceedings.mlr.press/v78/lomonaco17a.html) by Vincenzo Lomonaco and Davide Maltoni. *Proceedings of the 1st Annual Conference on Robot Learning*, 17--26, 2017. [vision] 

### Bioinspired Methods

**25 papers**

In this section we list all the papers related to bioinspired continual learning approaches.

- [A Biologically Plausible Audio-Visual Integration Model for Continual Learning](http://arxiv.org/abs/2007.08855) by Wenjie Chen, Fengtong Du, Ye Wang and Lihong Cao. *IJCNN*, 2021. 
- [Synaptic Metaplasticity in Binarized Neural Networks](https://www.nature.com/articles/s41467-021-22768-y) by Axel Laborieux, Maxence Ernoult, Tifenn Hirtzlin and Damien Querlioz. *Nature Communications*, 2549, 2021. 
- [Controlled Forgetting: Targeted Stimulation and Dopaminergic Plasticity Modulation for Unsupervised Lifelong Learning in Spiking Neural Networks](https://www.frontiersin.org/article/10.3389/fnins.2020.00007/full) by Jason M. Allred and Kaushik Roy. *Frontiers in Neuroscience*, 7, 2020. [spiking] 
- [Cognitively-Inspired Model for Incremental Learning Using a Few Examples](https://openaccess.thecvf.com/content_CVPRW_2020/html/w15/Ayub_Cognitively-Inspired_Model_for_Incremental_Learning_Using_a_Few_Examples_CVPRW_2020_paper.html) by A. Ayub and A. R. Wagner. *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops*, 2020. [cifar] [cubs] [dual] 
- [Storing Encoded Episodes as Concepts for Continual Learning](https://arxiv.org/abs/2007.06637 http://arxiv.org/abs/2007.06637) by Ali Ayub and Alan R. Wagner. *arXiv*, 2020. [generative] [imagenet] [mnist] 
- [Spiking Neural Predictive Coding for Continual Learning from Data Streams](http://arxiv.org/abs/1908.08655) by  and Alexander Ororbia. *arXiv*, 2020. [spiking] 
- [Brain-like Replay for Continual Learning with Artificial Neural Networks](https://baicsworkshop.github.io/pdf/BAICS_8.pdf) by Gido M. van de Ven, Hava T. Siegelmann and Andreas S. Tolias. *International Conference on Learning Representations (Workshop on Bridging AI and Cognitive Science)*, 2020. [cifar] 
- [Selfless Sequential Learning](https://openreview.net/forum?id=Bkxbrn0cYX) by Rahaf Aljundi, Marcus Rohrbach and Tinne Tuytelaars. *ICLR*, 2019. [cifar] [mnist] [sparsity] 
- [Backpropamine: Training Self-Modifying Neural Networks with Differentiable Neuromodulated Plasticity](https://openreview.net/pdf?id=r1lrAiA5Ym) by Thomas Miconi, Aditya Rawal, Jeff Clune and Kenneth O Stanley. *ICLR*, 2019. 
- [Continual Learning of Recurrent Neural Networks by Locally Aligning Distributed Representations](http://arxiv.org/abs/1810.07411) by Alexander Ororbia, Ankur Mali, C Lee Giles and Daniel Kifer. *arXiv*, 2019. [mnist] [rnn] [spiking] 
- [Lifelong Neural Predictive Coding: Sparsity Yields Less Forgetting When Learning Cumulatively](http://arxiv.org/abs/1905.10696) by Alexander Ororbia, Ankur Mali, Daniel Kifer and C Lee Giles. *arXiv*, 1--11, 2019. [fashion] [mnist] [sparsity] 
- [FearNet: Brain-Inspired Model for Incremental Learning](https://openreview.net/pdf?id=SJ1Xmf-Rb) by Ronald Kemker and Christopher Kanan. *ICLR*, 2018. [audio] [cifar] [generative] 
- [Differentiable Plasticity: Training Plastic Neural Networks with Backpropagation](http://proceedings.mlr.press/v80/miconi18a.html) by Thomas Miconi, Kenneth Stanley and Jeff Clune. *International Conference on Machine Learning*, 3559--3568, 2018. 
- [Lifelong Learning of Spatiotemporal Representations With Dual-Memory Recurrent Self-Organization](https://www.frontiersin.org/articles/10.3389/fnbot.2018.00078/full) by German I Parisi, Jun Tani, Cornelius Weber and Stefan Wermter. *Frontiers in Neurorobotics*, 2018. [core50] [dual] [rnn] [som] 
- [SLAYER: Spike Layer Error Reassignment in Time](http://papers.nips.cc/paper/7415-slayer-spike-layer-error-reassignment-in-time.pdf) by Sumit Bam Shrestha and Garrick Orchard. *Advances in Neural Information Processing Systems 31*, 1412--1421, 2018. 
- [Born to Learn: The Inspiration, Progress, and Future of Evolved Plastic Artificial Neural Networks](https://www.sciencedirect.com/science/article/pii/S0893608018302120) by Andrea Soltoggio, Kenneth O. Stanley and Sebastian Risi. *Neural Networks*, 48--67, 2018. 
- [Neurogenesis-Inspired Dictionary Learning: Online Model Adaption in a Changing World](https://arxiv.org/abs/1701.06106) by Sahil Garg, Irina Rish, Guillermo Cecchi and Aurelie Lozano. *IJCAI International Joint Conference on Artificial Intelligence*, 1696--1702, 2017. [nlp] [vision] 
- [Diffusion-Based Neuromodulation Can Eliminate Catastrophic Forgetting in Simple Neural Networks](http://arxiv.org/abs/1705.07241 http://dx.doi.org/10.1371/journal.pone.0187736) by Roby Velez and Jeff Clune. *PLoS ONE*, 1--31, 2017. 
- [How Do Neurons Operate on Sparse Distributed Representations? A Mathematical Theory of Sparsity, Neurons and Active Dendrites](http://arxiv.org/abs/1601.00720) by Subutai Ahmad and Jeff Hawkins. *arXiv*, 1--23, 2016. [hebbian] [sparsity] 
- [Continuous Online Sequence Learning with an Unsupervised Neural Network Model](https://doi.org/10.1162/NECO_a_00893) by Yuwei Cui, Subutai Ahmad and Jeff Hawkins. *Neural Computation*, 2474--2504, 2016. [spiking] 
- [Backpropagation of Hebbian Plasticity for Continual Learning](https://c38663e3-a-62cb3a1a-s-sites.googlegroups.com/site/cldlnips2016/CLDL-2016_paper_2.pdf?attachauth=ANoY7cpkpkdHxt2kA42TazATZVrBcNkcKZBbB_QkYQ2MQDe-Hz-inAnoBcb2Rl-6VCBWzWbjKjULT3tkSAtt1hdk66nh4Gy28ObAg7jKgLXNMzPTOYyB_roYB1nPaDNNkfQQhJJGXUdSexlxXDBUU0S) by  and Thomas Miconi. *NIPS Workshop - Continual Learning*, 5, 2016. 
- [Mitigation of Catastrophic Forgetting in Recurrent Neural Networks Using a Fixed Expansion Layer](http://ieeexplore.ieee.org/document/6707047/) by Robert Coop and Itamar Arel. *The 2013 International Joint Conference on Neural Networks (IJCNN)*, 1--7, 2013. [mnist] [rnn] [sparsity] 
- [Compete to Compute](http://papers.nips.cc/paper/5059-compete-to-compute.pdf) by Rupesh Kumar Srivastava, Jonathan Masci, Sohrob Kazerounian, Faustino Gomez and Jürgen Schmidhuber. *Advances in Neural Information Processing Systems 26*, 2013. [mnist] [sparsity] 
- [Mitigation of Catastrophic Interference in Neural Networks Using a Fixed Expansion Layer](http://ieeexplore.ieee.org/document/6292123/) by Robert Coop and Itamar Arel. *2012 IEEE 55th International Midwest Symposium on Circuits and Systems (MWSCAS)*, 726--729, 2012. [sparsity] 
- [Synaptic Plasticity: Taming the Beast](https://www.nature.com/articles/nn1100_1178) by L F Abbott and Sacha B Nelson. *Nature Neuroscience*, 1178--1183, 2000. [hebbian] 

### Catastrophic Forgetting Studies

**16 papers**

In this section we list all the major contributions trying to understand catastrophic forgetting and its implication in machines that learn continually.

- [Architecture Matters in Continual Learning](http://arxiv.org/abs/2202.00275) by Seyed Iman Mirzadeh, Arslan Chaudhry, Dong Yin, Timothy Nguyen, Razvan Pascanu, Dilan Gorur and Mehrdad Farajtabar. *arXiv*, 2022. 
- [Continual Learning in the Teacher-Student Setup: Impact of Task Similarity](http://proceedings.mlr.press/v139/lee21e.html) by Sebastian Lee, Sebastian Goldt and Andrew Saxe. *International Conference on Machine Learning*, 6109--6119, 2021. 
- [Understanding Continual Learning Settings with Data Distribution Drift Analysis](http://arxiv.org/abs/2104.01678) by Timothée Lesort, Massimo Caccia and Irina Rish. *arXiv*, 2021. 
- [Continual Learning in Deep Networks: An Analysis of the Last Layer](http://arxiv.org/abs/2106.01834) by Timothée Lesort, Thomas George and Irina Rish. *arXiv*, 2021. 
- [Wide Neural Networks Forget Less Catastrophically](http://arxiv.org/abs/2110.11526) by Seyed Iman Mirzadeh, Arslan Chaudhry, Huiyi Hu, Razvan Pascanu, Dilan Gorur and Mehrdad Farajtabar. *arXiv*, 2021. 
- [Does Continual Learning = Catastrophic Forgetting?](http://arxiv.org/abs/2101.07295) by Anh Thai, Stefan Stojanov, Isaac Rehg and James M. Rehg. *arXiv*, 2021. 
- [Sequential Mastery of Multiple Visual Tasks: Networks Naturally Learn to Learn and Forget to Forget](https://openaccess.thecvf.com/content_CVPR_2020/papers/Davidson_Sequential_Mastery_of_Multiple_Visual_Tasks_Networks_Naturally_Learn_to_CVPR_2020_paper.pdf) by Guy Davidson and Michael C Mozer. *CVPR*, 9282--9293, 2020. [vision] 
- [Understanding the Role of Training Regimes in Continual Learning](http://arxiv.org/abs/2006.06958) by Seyed Iman Mirzadeh, Mehrdad Farajtabar, Razvan Pascanu and Hassan Ghasemzadeh. *arXiv*, 2020. 
- [Dissecting Catastrophic Forgetting in Continual Learning by Deep Visualization](http://arxiv.org/abs/2001.01578) by Giang Nguyen, Shuan Chen, Thao Do, Tae Joon Jun, Ho-Jin Choi and Daeyoung Kim. *arXiv*, 2020. [vision] 
- [Toward Understanding Catastrophic Forgetting in Continual Learning](http://arxiv.org/abs/1908.01091) by Cuong V Nguyen, Alessandro Achille, Michael Lam, Tal Hassner, Vijay Mahadevan and Stefano Soatto. *arXiv*, 2019. [cifar] [mnist] 
- [A Study on Catastrophic Forgetting in Deep LSTM Networks](http://link.springer.com/10.1007/978-3-030-30484-3_56) by Monika Schak and Alexander Gepperth. *Artificial Neural Networks and Machine Learning – ICANN 2019: Deep Learning*, 714--728, 2019. [rnn] 
- [An Empirical Study of Example Forgetting during Deep Neural Network Learning](https://openreview.net/forum?id=BJlxm30cKm) by Mariya Toneva, Alessandro Sordoni, Remi Tachet des Combes, Adam Trischler, Yoshua Bengio and Geoffrey J Gordon. *International Conference on Learning Representations*, 2019. [cifar] [mnist] 
- [Localizing Catastrophic Forgetting in Neural Networks](http://arxiv.org/abs/1906.02568) by Felix Wiewel and Bin Yang. *arXiv*, 2019. [mnist] 
- [The Stability-Plasticity Dilemma: Investigating the Continuum from Catastrophic Forgetting to Age-Limited Learning Effects](http://www.pubmedcentral.nih.gov/articlerender.fcgi?artid=3732997%7B%5C&%7Dtool=pmcentrez%7B%5C&%7Drendertype=abstract http://journal.frontiersin.org/article/10.3389/fpsyg.2013.00504/abstract) by Martial Mermillod, Aurélia Bugaiska and Patrick Bonin. *Frontiers in Psychology*, 504, 2013. 
- [Catastrophic Forgetting in Connectionist Networks](https://www.cell.com/trends/cognitive-sciences/abstract/S1364-6613(99)01294-2) by  and Robert French. *Trends in Cognitive Sciences*, 128--135, 1999. [sparsity] 
- [How Does a Brain Build a Cognitive Code?](https://psycnet.apa.org/record/1980-06768-001) by  and Stephen Grossberg. *Psychological Review*, 1--51, 1980. 

### Classics

**10 papers**

In this section you'll find pioneering and classic continual learning papers. We recommend to read all the papers in this section for a good background on current continual deep learning developments.

- [Lifelong Machine Learning: A Paradigm for Continuous Learning](https://doi.org/10.1007/s11704-016-6903-6) by  and Bing Liu. *Frontiers of Computer Science*, 359--361, 2017. 
- [The Organization of Behavior: A Neuropsychological Theory](https://www.amazon.com/Organization-Behavior-Neuropsychological-Theory/dp/0805843000 https://books.google.it/books/about/The_Organization_of_Behavior.html?id=ddB4AgAAQBAJ&printsec=frontcover&source=kp_read_button&redir_esc=y#v=onepage&q&f=false) by  and D O Hebb. *Lawrence Erlbaum*, 2002. [hebbian] 
- [Pseudo-Recurrent Connectionist Networks: An Approach to the 'Sensitivity-Stability' Dilemma](http://www.tandfonline.com/doi/abs/10.1080/095400997116595) by  and Robert French. *Connection Science*, 353--380, 1997. [dual] 
- [CHILD: A First Step Towards Continual Learning](https://doi.org/10.1023/A:1007331723572) by  and Mark B Ring. *Machine Learning*, 77--104, 1997. 
- [Is Learning The N-Th Thing Any Easier Than Learning The First?](http://papers.nips.cc/paper/1034-is-learning-the-n-th-thing-any-easier-than-learning-the-first.pdf) by  and Sebastian Thrun. *Advances in Neural Information Processing Systems 8*, 640--646, 1996. [vision] 
- [Learning in the Presence of Concept Drift and Hidden Contexts](https://doi.org/10.1007/BF00116900 http://link.springer.com/10.1007/BF00116900) by Gerhard Widmer and Miroslav Kubat. *Machine Learning*, 69--101, 1996. 
- [Using Semi-Distributed Representations to Overcome Catastrophic Forgetting in Connectionist Networks](https://www.aaai.org/Papers/Symposia/Spring/1993/SS-93-06/SS93-06-007.pdf) by  and Robert French. *In Proceedings of the 13th Annual Cognitive Science Society Conference*, 173--178, 1991. [sparsity] 
- [Connectionist Models of Recognition Memory: Constraints Imposed by Learning and Forgetting Functions](https://europepmc.org/article/MED/2186426) by  and R. Ratcliff. *Psychological Review*, 285--308, 1990. 
- [The ART of Adaptive Pattern Recognition by a Self-Organizing Neural Network](https://ieeexplore.ieee.org/document/33) by Gail A. Carpenter and Stephen Grossberg. *Computer*, 77--88, 1988. 
- [How Does a Brain Build a Cognitive Code?](https://psycnet.apa.org/record/1980-06768-001) by  and Stephen Grossberg. *Psychological Review*, 1--51, 1980. 

### Continual Few Shot Learning

**8 papers**

Here we list the papers related to Few-Shot continual and incremental learning.

- [Few-Shot Continual Learning: A Brain-Inspired Approach](https://arxiv.org/abs/2104.09034) by Liyuan Wang, Qian Li, Yi Zhong and Jun Zhu. *arXiv*, 2021. 
- [Defining Benchmarks for Continual Few-Shot Learning](http://arxiv.org/abs/2004.11967) by Antreas Antoniou, Massimiliano Patacchiola, Mateusz Ochal and Amos Storkey. *arXiv*, 2020. [imagenet] 
- [Tell Me What This Is: Few-Shot Incremental Object Learning by a Robot](http://arxiv.org/abs/2008.00819) by Ali Ayub and Alan R. Wagner. *arXiv*, 2020. 
- [La-MAML: Look-ahead Meta Learning for Continual Learning](https://arxiv.org/abs/2007.13904) by Gunshi Gupta, Karmesh Yadav and Liam Paull. *arXiv*, 2020. 
- [iTAML: An Incremental Task-Agnostic Meta-learning Approach](https://openaccess.thecvf.com/content_CVPR_2020/html/Rajasegaran_iTAML_An_Incremental_Task-Agnostic_Meta-learning_Approach_CVPR_2020_paper.html) by Jathushan Rajasegaran, Salman Khan, Munawar Hayat, Fahad Shahbaz Khan and Mubarak Shah. *IEEE/CVF Conference on Computer Vision and Pattern Recognition*, 13588---13597, 2020. [cifar] [imagenet] 
- [Wandering within a World: Online Contextualized Few-Shot Learning](https://arxiv.org/abs/2007.04546) by Mengye Ren, Michael L Iuzzolino, Michael C Mozer and Richard S Zemel. *arXiv*, 2020. [omniglot] 
- [Few-Shot Class-Incremental Learning](https://arxiv.org/abs/2004.10956) by X. Tao, Hong X., X. Chang, S. Dong, X. Wei and Y. Gong. *IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*, 2020. [cifar] 
- [Few-Shot Class-Incremental Learning via Feature Space Composition](https://arxiv.org/abs/2006.15524) by H. Zhao, Y. Fu, X. Li, S. Li, B. Omar and X. Li. *arXiv*, 2020. [cifar] [cubs] 

### Continual Meta Learning

**4 papers**

In this section we list all the papers related to the continual meta-learning.

- [Online Fast Adaptation and Knowledge Accumulation: A New Approach to Continual Learning](http://arxiv.org/abs/2003.05856) by Massimo Caccia, Pau Rodriguez, Oleksiy Ostapenko, Fabrice Normandin, Min Lin, Lucas Caccia, Issam Laradji, Irina Rish, Alexande Lacoste, David Vazquez and Laurent Charlin. *arXiv*, 2020. [fashion] [framework] [mnist] 
- [Continuous Meta-Learning without Tasks](https://arxiv.org/abs/1912.08866) by James Harrison, Apoorva Sharma, Chelsea Finn and Marco Pavone. *arXiv*, 2019. [imagenet] [mnist] 
- [Task Agnostic Continual Learning via Meta Learning](http://arxiv.org/abs/1906.05201) by Xu He, Jakub Sygnowski, Alexandre Galashov, Andrei A Rusu, Yee Whye Teh and Razvan Pascanu. *arXiv:1906.05201 [cs, stat]*, 2019. [mnist] 
- [Reconciling Meta-Learning and Continual Learning with Online Mixtures of Tasks](http://papers.nips.cc/paper/9112-reconciling-meta-learning-and-continual-learning-with-online-mixtures-of-tasks) by Ghassen Jerfel, Erin Grant, Tom Griffiths and Katherine A Heller. *Advances in Neural Information Processing Systems*, 9122--9133, 2019. [bayes] [vision] 

### Continual Reinforcement Learning

**23 papers**

In this section we list all the papers related to the continual Reinforcement Learning.

- [Lifetime Policy Reuse and the Importance of Task Capacity](http://arxiv.org/abs/2106.01741) by David M. Bossens and Adam J. Sobey. *arXiv*, 2021. 
- [Unsupervised Lifelong Learning with Curricula](https://doi.org/10.1145/3442381.3449839) by Yi He, Sheng Chen, Baijun Wu, Xu Yuan and Xindong Wu. *Proceedings of the Web Conference 2021*, 3534--3545, 2021. 
- [Continuous Coordination As a Realistic Scenario for Lifelong Learning](http://proceedings.mlr.press/v139/nekoei21a.html) by Hadi Nekoei, Akilesh Badrinaaraayanan, Aaron Courville and Sarath Chandar. *International Conference on Machine Learning*, 8016--8024, 2021. 
- [Reducing Catastrophic Forgetting When Evolving Neural Networks](http://arxiv.org/abs/1904.03178) by  and Joseph Early. *arXiv*, 2019. 
- [A Meta-MDP Approach to Exploration for Lifelong Reinforcement Learning](https://papers.nips.cc/paper/8806-a-meta-mdp-approach-to-exploration-for-lifelong-reinforcement-learning.pdf) by Francisco M Garcia and Philip S Thomas. *NeurIPS*, 5691--5700, 2019. 
- [Policy Consolidation for Continual Reinforcement Learning](http://arxiv.org/abs/1902.00255) by Christos Kaplanis, Murray Shanahan and Claudia Clopath. *ICML*, 2019. 
- [Continual Learning Exploiting Structure of Fractal Reservoir Computing](http://link.springer.com/10.1007/978-3-030-30493-5_4) by Taisuke Kobayashi and Toshiki Sugino. *Artificial Neural Networks and Machine Learning – ICANN 2019: Workshop and Special Sessions*, 35--47, 2019. [rnn] 
- [Deep Online Learning via Meta-Learning: Continual Adaptation for Model-Based RL](https://arxiv.org/abs/1812.07671) by Anusha Nagabandi, Chelsea Finn and Sergey Levine. *7th International Conference on Learning Representations, ICLR 2019*, 2019. 
- [Leaky Tiling Activations: A Simple Approach to Learning Sparse Representations Online](http://arxiv.org/abs/1911.08068) by Yangchen Pan, Kirby Banman and Martha White. *arXiv*, 2019. [sparsity] 
- [Learning to Learn without Forgetting by Maximizing Transfer and Minimizing Interference](https://openreview.net/pdf?id=B1gTShAct7) by Matthew Riemer, Ignacio Cases, Robert Ajemian, Miao Liu, Irina Rish, Yuhai Tu and Gerald Tesauro. *ICLR*, 2019. [mnist] 
- [Experience Replay for Continual Learning](http://papers.nips.cc/paper/8327-experience-replay-for-continual-learning.pdf) by David Rolnick, Arun Ahuja, Jonathan Schwarz, Timothy P Lillicrap and Greg Wayne. *NeurIPS*, 350--360, 2019. 
- [Selective Experience Replay for Lifelong Learning](http://arxiv.org/abs/1802.10269) by David Isele and Akansel Cosgun. *Thirty-Second AAAI Conference on Artificial Intelligence*, 3302--3309, 2018. 
- [Continual Reinforcement Learning with Complex Synapses](http://arxiv.org/abs/1802.07239) by Christos Kaplanis, Murray Shanahan and Claudia Clopath. *ICML*, 2018. 
- [Unicorn: Continual Learning with a Universal, Off-policy Agent](http://arxiv.org/abs/1802.08294) by Daniel J Mankowitz, Augustin Žídek, André Barreto, Dan Horgan, Matteo Hessel, John Quan, Junhyuk Oh, Hado van Hasselt, David Silver and Tom Schaul. *arXiv*, 1--17, 2018. 
- [Lifelong Inverse Reinforcement Learning](http://papers.nips.cc/paper/7702-lifelong-inverse-reinforcement-learning.pdf) by Jorge A Mendez, Shashank Shivkumar and Eric Eaton. *NeurIPS*, 4502--4513, 2018. 
- [Progress & Compress: A Scalable Framework for Continual Learning](http://proceedings.mlr.press/v80/schwarz18a.html) by Jonathan Schwarz, Wojciech Czarnecki, Jelena Luketina, Agnieszka Grabska-Barwinska, Yee Whye Teh, Razvan Pascanu and Raia Hadsell. *International Conference on Machine Learning*, 4528--4537, 2018. [vision] 
- [Overcoming Catastrophic Forgetting in Neural Networks](http://arxiv.org/abs/1612.00796) by James Kirkpatrick, Razvan Pascanu, Neil Rabinowitz, Joel Veness, Guillaume Desjardins, Andrei A Rusu, Kieran Milan, John Quan, Tiago Ramalho, Agnieszka Grabska-Barwinska, Demis Hassabis, Claudia Clopath, Dharshan Kumaran and Raia Hadsell. *PNAS*, 3521--3526, 2017. [mnist] 
- [Continual and One-Shot Learning Through Neural Networks with Dynamic External Memory](https://link.springer.com/chapter/10.1007/978-3-319-55849-3_57) by Benno Lüders, Mikkel Schläger, Aleksandra Korach and Sebastian Risi. *Applications of Evolutionary Computation*, 886--901, 2017. 
- [Stable Predictive Representations with General Value Functions for Continual Learning](https://sites.ualberta.ca/ amw8/cldl.pdf) by Matthew Schlegel, Adam White and Martha White. *Continual Learning and Deep Networks Workshop at the Neural Information Processing System Conference*, 2017. 
- [Continual Learning through Evolvable Neural Turing Machines](https://core.ac.uk/reader/84859350) by Benno Luders, Mikkel Schlager and Sebastian Risi. *NIPS 2016 Workshop on Continual Learning and Deep Networks*, 2016. 
- [Progressive Neural Networks](http://arxiv.org/abs/1606.04671) by Andrei A Rusu, Neil C Rabinowitz, Guillaume Desjardins, Hubert Soyer, James Kirkpatrick, Koray Kavukcuoglu, Razvan Pascanu and Raia Hadsell. *arXiv*, 2016. [mnist] 
- [Lifelong-RL: Lifelong Relaxation Labeling for Separating Entities and Aspects in Opinion Targets.](http://www.ncbi.nlm.nih.gov/pubmed/29756130 http://www.pubmedcentral.nih.gov/articlerender.fcgi?artid=PMC5947972) by Lei Shu, Bing Liu, Hu Xu and Annice Kim. *Proceedings of the Conference on Empirical Methods in Natural Language Processing. Conference on Empirical Methods in Natural Language Processing*, 225--235, 2016. [nlp] 
- [CHILD: A First Step Towards Continual Learning](https://doi.org/10.1023/A:1007331723572) by  and Mark B Ring. *Machine Learning*, 77--104, 1997. 

### Continual Sequential Learning

**12 papers**

Here we maintain a list of all the papers related to the continual learning at the intersection with sequential learning.

- [Continual Learning for Recurrent Neural Networks: An Empirical Evaluation](https://www.sciencedirect.com/science/article/pii/S0893608021002847) by Andrea Cossu, Antonio Carta, Vincenzo Lomonaco and Davide Bacciu. *Neural Networks*, 607--627, 2021. [rnn] 
- [Continual Competitive Memory: A Neural System for Online Task-Free Lifelong Learning](http://arxiv.org/abs/2106.13300) by  and Alexander G. Ororbia. *arXiv*, 2021. 
- [Continual Learning with Gated Incremental Memories for Sequential Data Processing](http://arxiv.org/abs/2004.04077) by Andrea Cossu, Antonio Carta and Davide Bacciu. *Proceedings of the 2020 International Joint Conference on Neural Networks (IJCNN 2020)*, 2020. [mnist] [rnn] 
- [Organizing Recurrent Network Dynamics by Task-Computation to Enable Continual Learning](https://proceedings.neurips.cc/paper/2020/file/a576eafbce762079f7d1f77fca1c5cc2-Paper.pdf) by Lea Duncker, Laura N Driscoll, Krishna V Shenoy, Maneesh Sahani and David Sussillo. *Advances in Neural Information Processing Systems*, 2020. [rnn] 
- [Meta-Consolidation for Continual Learning](http://arxiv.org/abs/2010.00352) by K J Joseph and Vineeth N Balasubramanian. *NeurIPS*, 2020. [bayes] [cifar] [imagenet] [mnist] 
- [Compositional Language Continual Learning](https://iclr.cc/virtual_2020/poster_rklnDgHtDS.html) by Yuanpeng Li, Liang Zhao, Kenneth Church and Mohamed Elhoseiny. *Eighth International Conference on Learning Representations*, 2020. [nlp] [rnn] 
- [Online Continual Learning on Sequences](http://arxiv.org/abs/2003.09114) by German I Parisi and Vincenzo Lomonaco. *Studies in Computational Intelligence*, 2020. [framework] 
- [Unsupervised Progressive Learning and the STAM Architecture](http://arxiv.org/abs/1904.02021) by James Smith, Seth Baer, Cameron Taylor and Constantine Dovrolis. *arXiv*, 2019. [mnist] 
- [Toward Training Recurrent Neural Networks for Lifelong Learning](https://doi.org/10.1162/neco_a_01246) by Shagun Sodhani, Sarath Chandar and Yoshua Bengio. *Neural Computation*, 1--35, 2019. [rnn] 
- [Semi-Supervised Tuning from Temporal Coherence](https://ieeexplore.ieee.org/document/7900013) by Davide Maltoni and Vincenzo Lomonaco. *2016 23rd International Conference on Pattern Recognition (ICPR)*, 2509--2514, 2016. 
- [Self-Refreshing Memory in Artificial Neural Networks: Learning Temporal Sequences without Catastrophic Forgetting](https://doi.org/10.1080/09540090412331271199) by Bernard Ans, Stéphane Rousset, Robert M. French and Serban Musca. *Connection Science*, 71--99, 2004. [rnn] 
- [Using Pseudo-Recurrent Connectionist Networks to Solve the Problem of Sequential Learning](http://leadserv.u-bourgogne.fr/IMG/pdf/psdnet1.pdf) by  and Robert French. *Proceedings of the 19th Annual Cognitive Science Society Conference*, 1997. [dual] 

### Dissertation and Theses

**8 papers**

In this section we maintain a list of all the dissertation and thesis produced on continual learning and related topics.

- [Knowledge Uncertainty and Lifelong Learning in Neural Systems](https://www.research-collection.ethz.ch/handle/20.500.11850/523790) by  and Christian Henning. , 2022. 
- [Large-Scale Deep Class-Incremental Learning. (Apprentissage Incrémental Profond à Large ̧́helle)](https://tel.archives-ouvertes.fr/tel-03478553) by  and Eden Belouadah. , 2021. 
- [Continual Learning: Tackling Catastrophic Forgetting in Deep Neural Networks with Replay Processes](http://arxiv.org/abs/2007.00487) by  and Timoth'ee Lesort. *arXiv*, 2020. [cifar] [framework] [generative] [mnist] [vision] 
- [Continual Learning in Neural Networks](https://arxiv.org/abs/1910.02718) by  and Rahaf Aljundi. *arXiv*, 2019. [cifar] [imagenet] [mnist] [vision] 
- [Continual Deep Learning via Progressive Learning](http://researchbank.rmit.edu.au/eserv/rmit:162646/Fayek.pdf) by  and Haytham M. Fayek. *RMIT University*, 2019. [audio] [cifar] [imagenet] [sparsity] 
- [Continual Learning with Deep Architectures](http://amsdottorato.unibo.it/9073/) by  and Vincenzo Lomonaco. *University of Bologna*, 2019. [core50] [framework] 
- [Explanation-Based Neural Network Learning: A Lifelong Learning Approach](https://www.springer.com/gp/book/9780792397168) by  and Sebastian Thrun. *Springer*, 1996. [framework] 
- [Continual Learning in Reinforcement Environments](https://www.cs.utexas.edu/ ring/Ring-dissertation.pdf) by  and Mark Ring. *University of Texas*, 1994. [framework] 

### Generative Replay Methods

**7 papers**

In this section we collect all the papers introducing a continual learning strategy employing some generative replay methods.

- [Brain-Inspired Replay for Continual Learning with Artificial Neural Networks](https://www.nature.com/articles/s41467-020-17866-2) by Gido M. van de Ven, Hava T. Siegelmann and Andreas S. Tolias. *Nature Communications*, 2020. [cifar] [framework] [generative] [mnist] 
- [Complementary Learning for Overcoming Catastrophic Forgetting Using Experience Replay](http://arxiv.org/abs/1903.04566) by Mohammad Rostami, Soheil Kolouri and Praveen K Pilly. *arXiv*, 2019. 
- [Complementary Learning for Overcoming Catastrophic Forgetting Using Experience Replay](https://arxiv.org/abs/1903.04566v2) by Mohammad Rostami, Soheil Kolouri and Praveen K. Pilly. *arXiv*, 2019. 
- [Continual Learning of New Sound Classes Using Generative Replay](http://arxiv.org/abs/1906.00654) by Zhepei Wang, Cem Subakan, Efthymios Tzinis, Paris Smaragdis and Laurent Charlin. *arXiv*, 2019. [audio] 
- [Generative Replay with Feedback Connections as a General Strategy for Continual Learning](https://arxiv.org/abs/1809.10635) by Gido M. van de Ven and Andreas S. Tolias. *arXiv*, 2018. [framework] [generative] [mnist] 
- [Continual and One-Shot Learning Through Neural Networks with Dynamic External Memory](https://link.springer.com/chapter/10.1007/978-3-319-55849-3_57) by Benno Lüders, Mikkel Schläger, Aleksandra Korach and Sebastian Risi. *Applications of Evolutionary Computation*, 886--901, 2017. 
- [Continual Learning with Deep Generative Replay](http://papers.nips.cc/paper/6892-continual-learning-with-deep-generative-replay.pdf) by Hanul Shin, Jung Kwon Lee, Jaehong Kim and Jiwon Kim. *Advances in Neural Information Processing Systems 30*, 2990--2999, 2017. [mnist] 

### Hybrid Methods

**11 papers**

In this section we collect all the papers introducing a continual learning strategy employing some hybrid methods, mixing different strategies.

- [Rehearsal-Free Continual Learning over Small Non-I.I.D. Batches](https://openaccess.thecvf.com/content_CVPRW_2020/html/w15/Lomonaco_Rehearsal-Free_Continual_Learning_Over_Small_Non-I.I.D._Batches_CVPRW_2020_paper.html) by Vincenzo Lomonaco, Davide Maltoni and Lorenzo Pellegrini. *CVPR Workshop on Continual Learning for Computer Vision*, 246--247, 2020. [core50] 
- [Linear Mode Connectivity in Multitask and Continual Learning](https://arxiv.org/abs/2010.04495) by Seyed Iman Mirzadeh, Mehrdad Farajtabar, Dilan Gorur, Razvan Pascanu and Hassan Ghasemzadeh. *arXiv*, 2020. [cifar] [experimental] [mnist] 
- [Efficient Continual Learning in Neural Networks with Embedding Regularization](https://linkinghub.elsevier.com/retrieve/pii/S092523122030151X) by Jary Pomponi, Simone Scardapane, Vincenzo Lomonaco and Aurelio Uncini. *Neurocomputing*, 139--148, 2020. 
- [Efficient Lifelong Learning with A-GEM](http://arxiv.org/abs/1812.00420) by Arslan Chaudhry, Marc'Aurelio Ranzato, Marcus Rohrbach and Mohamed Elhoseiny. *ICLR*, 2019. [cifar] [mnist] 
- [Single-Net Continual Learning with Progressive Segmented Training (PST)](http://arxiv.org/abs/1905.11550) by Xiaocong Du, Gouranga Charan, Frank Liu and Yu Cao. *arXiv*, 1629--1636, 2019. [cifar] 
- [Continuous Learning in Single-Incremental-Task Scenarios](http://arxiv.org/abs/1806.08568) by Davide Maltoni and Vincenzo Lomonaco. *Neural Networks*, 56--73, 2019. [core50] [framework] 
- [Toward Training Recurrent Neural Networks for Lifelong Learning](https://doi.org/10.1162/neco_a_01246) by Shagun Sodhani, Sarath Chandar and Yoshua Bengio. *Neural Computation*, 1--35, 2019. [rnn] 
- [Continual Learning of New Sound Classes Using Generative Replay](http://arxiv.org/abs/1906.00654) by Zhepei Wang, Cem Subakan, Efthymios Tzinis, Paris Smaragdis and Laurent Charlin. *arXiv*, 2019. [audio] 
- [Lifelong Learning via Progressive Distillation and Retrospection](http://link.springer.com/10.1007/978-3-030-01219-9_27) by Saihui Hou, Xinyu Pan, Chen Change Loy, Zilei Wang and Dahua Lin. *ECCV*, 2018. [imagenet] [vision] 
- [Progress & Compress: A Scalable Framework for Continual Learning](http://proceedings.mlr.press/v80/schwarz18a.html) by Jonathan Schwarz, Wojciech Czarnecki, Jelena Luketina, Agnieszka Grabska-Barwinska, Yee Whye Teh, Razvan Pascanu and Raia Hadsell. *International Conference on Machine Learning*, 4528--4537, 2018. [vision] 
- [Gradient Episodic Memory for Continual Learning](https://arxiv.org/abs/1706.08840) by David Lopez-Paz and Marc'Aurelio Ranzato. *NIPS*, 2017. [cifar] [mnist] 

### Meta Continual Learning

**9 papers**

In this section we list all the papers related to the meta-continual learning.

- [Learning to Continually Learn](http://arxiv.org/abs/2002.09571) by Shawn Beaulieu, Lapo Frati, Thomas Miconi, Joel Lehman, Kenneth O. Stanley, Jeff Clune and Nick Cheney. *ECAI*, 2020. [vision] 
- [Continual Learning with Deep Artificial Neurons](http://arxiv.org/abs/2011.07035) by Blake Camp, Jaya Krishna Mandivarapu and Rolando Estrada. *arXiv*, 2020. [experimental] 
- [Meta-Consolidation for Continual Learning](http://arxiv.org/abs/2010.00352) by K J Joseph and Vineeth N Balasubramanian. *NeurIPS*, 2020. [bayes] [cifar] [imagenet] [mnist] 
- [Meta Continual Learning via Dynamic Programming](https://arxiv.org/abs/2008.02219) by R Krishnan and Prasanna Balaprakash. *arXiv*, 2020. [omniglot] 
- [Online Meta-Learning](http://proceedings.mlr.press/v97/finn19a/finn19a.pdf) by Chelsea Finn, Aravind Rajeswaran, Sham Kakade and Sergey Levine. *ICML*, 2019. [experimental] [mnist] 
- [Task Agnostic Continual Learning via Meta Learning](http://arxiv.org/abs/1906.05201) by Xu He, Jakub Sygnowski, Alexandre Galashov, Andrei A Rusu, Yee Whye Teh and Razvan Pascanu. *arXiv:1906.05201 [cs, stat]*, 2019. [mnist] 
- [Meta-Learning Representations for Continual Learning](http://papers.nips.cc/paper/8458-meta-learning-representations-for-continual-learning) by Khurram Javed and Martha White. *NeurIPS*, 2019. [omniglot] 
- [Learning to Learn without Forgetting by Maximizing Transfer and Minimizing Interference](https://openreview.net/pdf?id=B1gTShAct7) by Matthew Riemer, Ignacio Cases, Robert Ajemian, Miao Liu, Irina Rish, Yuhai Tu and Gerald Tesauro. *ICLR*, 2019. [mnist] 
- [Meta Continual Learning](https://arxiv.org/abs/1806.06928) by Risto Vuorio, Dong-Yeon Cho, Daejoong Kim and Jiwon Kim. *arXiv*, 2018. [mnist] 

### Metrics and Evaluations

**10 papers**

In this section we list all the papers related to the continual learning evalution protocols and metrics.

- [Continual Learning in Deep Networks: An Analysis of the Last Layer](http://arxiv.org/abs/2106.01834) by Timothée Lesort, Thomas George and Irina Rish. *arXiv*, 2021. 
- [Avalanche: An End-to-End Library for Continual Learning](http://arxiv.org/abs/2104.00405) by Vincenzo Lomonaco, Lorenzo Pellegrini, Andrea Cossu, Antonio Carta, Gabriele Graffieti, Tyler L. Hayes, Matthias De Lange, Marc Masana, Jary Pomponi, Gido van de Ven, Martin Mundt, Qi She, Keiland Cooper, Jeremy Forest, Eden Belouadah, Simone Calderara, German I. Parisi, Fabio Cuzzolin, Andreas Tolias, Simone Scardapane, Luca Antiga, Subutai Amhad, Adrian Popescu, Christopher Kanan, Joost van de Weijer, Tinne Tuytelaars, Davide Bacciu and Davide Maltoni. *CLVision Workshop at CVPR*, 2021. 
- [CLEVA-Compass: A Continual Learning Evaluation Assessment Compass to Promote Research Transparency and Comparability](https://openreview.net/forum?id=rHMaBYbkkRJ) by Martin Mundt, Steven Lang, Quentin Delfosse and Kristian Kersting. *International Conference on Learning Representations*, 2021. 
- [Online Fast Adaptation and Knowledge Accumulation: A New Approach to Continual Learning](http://arxiv.org/abs/2003.05856) by Massimo Caccia, Pau Rodriguez, Oleksiy Ostapenko, Fabrice Normandin, Min Lin, Lucas Caccia, Issam Laradji, Irina Rish, Alexande Lacoste, David Vazquez and Laurent Charlin. *arXiv*, 2020. [fashion] [framework] [mnist] 
- [Optimal Continual Learning Has Perfect Memory and Is NP-HARD](https://proceedings.icml.cc/paper/2020/file/274ad4786c3abca69fa097b85867d9a4-Paper.pdf) by Jeremias Knoblauch, Hisham Husain and Tom Diethe. *ICML*, 2020. [theoretical] 
- [Regularization Shortcomings for Continual Learning](http://arxiv.org/abs/1912.03049) by Timothée Lesort, Andrei Stoian and David Filliat. *arXiv*, 2020. [fashion] [mnist] 
- [Strategies for Improving Single-Head Continual Learning Performance](http://link.springer.com/10.1007/978-3-030-27202-9_41) by Alaa El Khatib and Fakhri Karray. *Lecture Notes in Computer Science (Including Subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics)*, 452--460, 2019. [cifar] [mnist] 
- [Towards Robust Evaluations of Continual Learning](http://arxiv.org/abs/1805.09733) by Sebastian Farquhar and Yarin Gal. *Privacy in Machine Learning and Artificial Intelligence Workshop, ICML*, 2019. [fashion] [framework] 
- [Don't Forget, There Is More than Forgetting: New Metrics for Continual Learning](http://arxiv.org/abs/1810.13166) by Natalia Díaz-Rodr\ǵuez, Vincenzo Lomonaco, David Filliat and Davide Maltoni. *arXiv*, 2018. [cifar] [framework] 
- [Three Scenarios for Continual Learning](http://arxiv.org/abs/1904.07734) by Gido M van de Ven and Andreas S Tolias. *Continual Learning Workshop NeurIPS*, 2018. [framework] [mnist] 

### Neuroscience

**7 papers**

In this section we maintain a list of all Neuroscience papers that can be related (and useful) for continual machine learning.

- [Biological Underpinnings for Lifelong Learning Machines](https://www.nature.com/articles/s42256-022-00452-0) by Dhireesha Kudithipudi, Mario Aguilar-Simon, Jonathan Babb, Maxim Bazhenov, Douglas Blackiston, Josh Bongard, Andrew P. Brna, Suraj Chakravarthi Raja, Nick Cheney, Jeff Clune, Anurag Daram, Stefano Fusi, Peter Helfer, Leslie Kay, Nicholas Ketz, Zsolt Kira, Soheil Kolouri, Jeffrey L. Krichmar, Sam Kriegman, Michael Levin, Sandeep Madireddy, Santosh Manicka, Ali Marjaninejad, Bruce McNaughton, Risto Miikkulainen, Zaneta Navratilova, Tej Pandit, Alice Parker, Praveen K. Pilly, Sebastian Risi, Terrence J. Sejnowski, Andrea Soltoggio, Nicholas Soures, Andreas S. Tolias, Darío Urbina-Meléndez, Francisco J. Valero-Cuevas, Gido M. van de Ven, Joshua T. Vogelstein, Felix Wang, Ron Weiss, Angel Yanguas-Gil, Xinyun Zou and Hava Siegelmann. *Nature Machine Intelligence*, 196--210, 2022. 
- [Neural Inhibition for Continual Learning and Memory](https://www.sciencedirect.com/science/article/pii/S0959438820301343) by  and Helen C Barron. *Current Opinion in Neurobiology*, 85--94, 2021. 
- [Can Sleep Protect Memories from Catastrophic Forgetting?](https://www.biorxiv.org/content/10.1101/569038v1) by Oscar C Gonzalez, Yury Sokolov, Giri Krishnan and Maxim Bazhenov. *bioRxiv*, 569038, 2019. 
- [Synaptic Consolidation: An Approach to Long-Term Learning](http://link.springer.com/10.1007/s11571-011-9177-6) by  and Claudia Clopath. *Cognitive Neurodynamics*, 251--257, 2012. [hebbian] 
- [The Organization of Behavior: A Neuropsychological Theory](https://www.amazon.com/Organization-Behavior-Neuropsychological-Theory/dp/0805843000 https://books.google.it/books/about/The_Organization_of_Behavior.html?id=ddB4AgAAQBAJ&printsec=frontcover&source=kp_read_button&redir_esc=y#v=onepage&q&f=false) by  and D O Hebb. *Lawrence Erlbaum*, 2002. [hebbian] 
- [Negative Transfer Errors in Sequential Cognitive Skills: Strong-but-wrong Sequence Application.](http://doi.apa.org/getdoi.cfm?doi=10.1037/0278-7393.26.3.601) by Dan J. Woltz, Michael K. Gardner and Brian G. Bell. *Journal of Experimental Psychology: Learning, Memory, and Cognition*, 601--625, 2000. 
- [Connectionist Models of Recognition Memory: Constraints Imposed by Learning and Forgetting Functions.](http://www.ncbi.nlm.nih.gov/pubmed/2186426) by  and R Ratcliff. *Psychological review*, 285--308, 1990. 

### Others

**47 papers**

In this section we list all the other papers not appearing in at least one of the above sections.

- [Dataset Knowledge Transfer for Class-Incremental Learning without Memory](https://doi.org/10.1109/WACV51458.2022.00337) by Habib Slim, Eden Belouadah, Adrian Popescu and Darian M. Onchis. *IEEE/CVF Winter Conference on Applications of Computer Vision, WACV 2022, Waikoloa, HI, USA, January 3-8, 2022*, 3311--3320, 2022. 
- [Continual Novelty Detection](http://arxiv.org/abs/2106.12964) by Rahaf Aljundi, Daniel Olmeda Reino, Nikolay Chumerin and Richard E. Turner. *arXiv*, 2021. 
- [Co\$2̂\$L: Contrastive Continual Learning](http://arxiv.org/abs/2106.14413) by Hyuntak Cha, Jaeho Lee and Jinwoo Shin. *arXiv*, 2021. 
- [Sustainable Artificial Intelligence through Continual Learning](https://arxiv.org/abs/2111.09437) by Andrea Cossu, Marta Ziosi and Vincenzo Lomonaco. *International Conference on AI for People (CAIP)*, 2021. 
- [Continual Backprop: Stochastic Gradient Descent with Persistent Randomness](http://arxiv.org/abs/2108.06325) by Shibhansh Dohare, A. Rupam Mahmood and Richard S. Sutton. *arXiv*, 2021. 
- [Continuum: Simple Management of Complex Continual Learning Scenarios](https://arxiv.org/abs/2102.06253) by Arthur Douillard and Timothée Lesort. *arXiv*, 2021. 
- [Posterior Meta-Replay for Continual Learning](https://openreview.net/forum?id=AhuVLaYp6gn) by Christian Henning, Maria Cervera, Francesco D'Angelo, Johannes Von Oswald, Regina Traber, Benjamin Ehret, Seijin Kobayashi, Benjamin F. Grewe and Joao Sacramento. *Advances in Neural Information Processing Systems*, 2021. [bayes] 
- [Rethinking the Representational Continuity: Towards Unsupervised Continual Learning](https://openreview.net/forum?id=9Hrka5PA7LW) by Divyam Madaan, Jaehong Yoon, Yuanchun Li, Yunxin Liu and Sung Ju Hwang. *International Conference on Learning Representations*, 2021. 
- [Representation Memorization for Fast Learning New Knowledge without Forgetting](http://arxiv.org/abs/2108.12596) by Fei Mi, Tao Lin and Boi Faltings. *arXiv*, 2021. [hebbian] [rnn] 
- [Neural Architecture Search of Deep Priors: Towards Continual Learning Without Catastrophic Interference](https://openaccess.thecvf.com/content/CVPR2021W/CLVision/html/Mundt_Neural_Architecture_Search_of_Deep_Priors_Towards_Continual_Learning_Without_CVPRW_2021_paper.html) by Martin Mundt, Iuliia Pliushch and Visvanathan Ramesh. *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition*, 3523--3532, 2021. 
- [Active Class Incremental Learning for Imbalanced Datasets](https://doi.org/10.1007/978-3-030-65414-6_12) by Eden Belouadah, Adrian Popescu, Umang Aggarwal and Léo Saci. *Computer Vision - ECCV 2020 Workshops - Glasgow, UK, August 23-28, 2020, Proceedings, Part VI*, 146--162, 2020. 
- [Initial Classifier Weights Replay for Memoryless Class Incremental Learning](https://www.bmvc2020-conference.com/assets/papers/0743.pdf) by Eden Belouadah, Adrian Popescu and Ioannis Kanellos. *31st British Machine Vision Conference 2020, BMVC 2020, Virtual Event, UK, September 7-10, 2020*, 2020. 
- [Long Live the Lottery: The Existence of Winning Tickets in Lifelong Learning](https://openreview.net/forum?id=LXMSvPmsm0g) by Tianlong Chen, Zhenyu Zhang, Sijia Liu, Shiyu Chang and Zhangyang Wang. *International Conference on Learning Representations*, 2020. 
- [Lifelong Machine Learning with Deep Streaming Linear Discriminant Analysis](http://arxiv.org/abs/1909.01520) by Tyler L Hayes and Christopher Kanan. *CLVision Workshop at CVPR 2020*, 1--15, 2020. [core50] [imagenet] 
- [Continual Learning with Bayesian Neural Networks for Non-Stationary Data](https://iclr.cc/virtual_2020/poster_SJlsFpVtDB.html) by Richard Kurle, Botond Cseke, Alexej Klushyn, Patrick van der Smagt and Stephan Günnemann. *Eighth International Conference on Learning Representations*, 2020. [bayes] 
- [Continual Learning Using Task Conditional Neural Networks](http://arxiv.org/abs/2005.05080) by Honglin Li, Payam Barnaghi, Shirin Enshaeifar and Frieder Ganz. *arXiv*, 2020. [cifar] [mnist] 
- [Energy-Based Models for Continual Learning](http://arxiv.org/abs/2011.12216) by Shuang Li, Yilun Du, Gido M. van de Ven, Antonio Torralba and Igor Mordatch. *arXiv*, 2020. [cifar] [experimental] [mnist] 
- [Continual Universal Object Detection](http://arxiv.org/abs/2002.05347) by Xialei Liu, Hao Yang, Avinash Ravichandran, Rahul Bhotika and Stefano Soatto. *arXiv*, 2020. 
- [Mnemonics Training: Multi-Class Incremental Learning without Forgetting](http://arxiv.org/abs/2002.10211) by Yaoyao Liu, An-An Liu, Yuting Su, Bernt Schiele and Qianru Sun. *arXiv*, 2020. [cifar] [imagenet] 
- [Structured Compression and Sharing of Representational Space for Continual Learning](http://arxiv.org/abs/2001.08650) by Gobinda Saha, Isha Garg, Aayush Ankit and Kaushik Roy. *arXiv*, 2020. [cifar] [mnist] 
- [Gradient Projection Memory for Continual Learning](https://openreview.net/forum?id=3AOj0RCNC2) by Gobinda Saha and Kaushik Roy. *International Conference on Learning Representations*, 2020. 
- [Gated Linear Networks](http://arxiv.org/abs/1910.01526) by Joel Veness, Tor Lattimore, David Budden, Avishkar Bhoopchand, Christopher Mattern, Agnieszka Grabska-Barwinska, Eren Sezener, Jianan Wang, Peter Toth, Simon Schmitt and Marcus Hutter. *arXiv*, 2020. 
- [Lifelong Graph Learning](http://arxiv.org/abs/2009.00647) by Chen Wang, Yuheng Qiu and Sebastian Scherer. *arXiv*, 2020. [graph] 
- [Superposition of Many Models into One](http://arxiv.org/abs/1902.05522) by Brian Cheung, Alex Terekhov, Yubei Chen, Pulkit Agrawal and Bruno Olshausen. *arXiv*, 2019. [cifar] [mnist] 
- [Continual Learning in Practice](http://arxiv.org/abs/1903.05202) by Tom Diethe, Tom Borchert, Eno Thereska, Borja Balle and Neil Lawrence. *arXiv*, 2019. 
- [Dynamically Constraining Connectionist Networks to Produce Distributed, Orthogonal Representations to Reduce Catastrophic Interference](https://www.taylorfrancis.com/books/9781317729266/chapters/10.4324/9781315789354-58) by  and Robert French. *Proceedings of the Sixteenth Annual Conference of the Cognitive Science Society*, 335--340, 2019. 
- [Continual Learning via Neural Pruning](http://arxiv.org/abs/1903.04476) by Siavash Golkar, Michael Kagan and Kyunghyun Cho. *arXiv*, 2019. [cifar] [mnist] [sparsity] 
- [BooVAE: A Scalable Framework for Continual VAE Learning under Boosting Approach](http://arxiv.org/abs/1908.11853) by Anna Kuzina, Evgenii Egorov and Evgeny Burnaev. *arXiv*, 2019. [bayes] [fashion] [mnist] 
- [Overcoming Catastrophic Forgetting with Unlabeled Data in the Wild](http://arxiv.org/abs/1903.12648) by Kibok Lee, Kimin Lee, Jinwoo Shin and Honglak Lee. *Proceedings of the IEEE International Conference on Computer Vision*, 312--321, 2019. 
- [Continual Learning Using Bayesian Neural Networks](http://arxiv.org/abs/1910.04112) by HongLin Li, Payam Barnaghi, Shirin Enshaeifar and Frieder Ganz. *arXiv*, 2019. [bayes] [mnist] 
- [Unified Probabilistic Deep Continual Learning through Generative Replay and Open Set Recognition](http://arxiv.org/abs/1905.12019) by Martin Mundt, Sagnik Majumder, Iuliia Pliushch, Yong Won Hong and Visvanathan Ramesh. *arXiv*, 2019. [audio] [bayes] [fashion] [framework] [generative] [mnist] [vision] 
- [Continual Rare-Class Recognition with Emerging Novel Subclasses](http://arxiv.org/abs/1906.12218) by Hung Nguyen, Xuejian Wang and Leman Akoglu. *ECML*, 2019. [nlp] 
- [Random Path Selection for Incremental Learning](http://papers.nips.cc/paper/9429-random-path-selection-for-continual-learning.pdf) by Jathushan Rajasegaran, Munawar Hayat, Salman Khan Fahad, Shahbaz Khan and Ling Shao. *NeurIPS*, 12669--12679, 2019. [cifar] [imagenet] [mnist] 
- [Improving and Understanding Variational Continual Learning](http://arxiv.org/abs/1905.02099) by Siddharth Swaroop, Cuong V Nguyen, Thang D Bui and Richard E Turner. *Continual Learning Workshop NeurIPS*, 1--17, 2019. [bayes] [mnist] 
- [Continual Learning via Online Leverage Score Sampling](http://arxiv.org/abs/1908.00355) by Dan Teng and Sakyasingha Dasgupta. *arXiv*, 2019. [cifar] [mnist] 
- [Class-Incremental Learning Based on Feature Extraction of CNN With Optimized Softmax and One-Class Classifiers](https://ieeexplore.ieee.org/document/8666123/) by Xin Ye and Qiuyu Zhu. *IEEE Access*, 42024--42031, 2019. [cifar] [mnist] 
- [Life-Long Disentangled Representation Learning with Cross-Domain Latent Homologies](http://arxiv.org/abs/1808.06508) by Alessandro Achille, Tom Eccles, Loic Matthey, Christopher P. Burgess, Nick Watters, Alexander Lerchner and Irina Higgins. *Neural Information Processing Systems (NeurIPS)*, 2018. 
- [DeeSIL: Deep-Shallow Incremental Learning](https://doi.org/10.1007/978-3-030-11012-3_11) by Eden Belouadah and Adrian Popescu. *Computer Vision - ECCV 2018 Workshops - Munich, Germany, September 8-14, 2018, Proceedings, Part II*, 151--157, 2018. 
- [A Unifying Bayesian View of Continual Learning](http://bayesiandeeplearning.org/2018/papers/74.pdf) by Sebastian Farquhar and Yarin Gal. *NeurIPS Bayesian Deep Learning Workshop*, 2018. [bayes] [cifar] [mnist] 
- [Overcoming Catastrophic Interference Using Conceptor-Aided Backpropagation](https://openreview.net/pdf?id=B1al7jg0b) by Xu He and Herbert Jaeger. *ICLR*, 2018. [mnist] 
- [Less-Forgetful Learning for Domain Expansion in Deep Neural Networks](https://www.aaai.org/ocs/index.php/AAAI/AAAI18/paper/view/17073) by Heechul Jung, Jeongwoo Ju, Minju Jung and Junmo Kim. *Thirty-Second AAAI Conference on Artificial Intelligence*, 2018. 
- [Piggyback: Adapting a Single Network to Multiple Tasks by Learning to Mask Weights](https://doi.org/10.1007/978-3-030-01225-0_5) by Arun Mallya, Dillon Davis and Svetlana Lazebnik. *ECCV*, 72--88, 2018. [imagenet] 
- [Adding New Tasks to a Single Network with Weight Transformations Using Binary Masks](http://arxiv.org/abs/1805.11119) by Massimiliano Mancini, Elisa Ricci, Barbara Caputo and Samuel Rota Bulò. *Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics)*, 180--189, 2018. [sparsity] [vision] 
- [Variational Continual Learning](https://openreview.net/forum?id=BkQqq0gRb) by Cuong V Nguyen, Yingzhen Li, Thang D Bui and Richard E Turner. *ICLR*, 2018. [bayes] 
- [Task Agnostic Continual Learning Using Online Variational Bayes](http://bayesiandeeplearning.org/2018/papers/58.pdf) by Chen Zeno, Itay Golan, Elad Hoffer and Daniel Soudry. *NeurIPS Bayesian Deep Learning Workshop*, 2018. [bayes] [cifar] [mnist] 
- [Encoder Based Lifelong Learning](http://arxiv.org/abs/1704.01920 http://dx.doi.org/10.1109/ICCV.2017.148) by Amal Rannen Triki, Rahaf Aljundi, Mathew B. Blaschko and Tinne Tuytelaars. *Proceedings of the IEEE International Conference on Computer Vision*, 1329--1337, 2017. [imagenet] [vision] 
- [Fine-Tuning Deep Neural Networks in Continuous Learning Scenarios](http://link.springer.com/10.1007/978-3-319-54526-4_43) by Christoph Käding, Erik Rodner, Alexander Freytag and Joachim Denzler. *ACCV Workshop*, 2016. [imagenet] 

### Regularization Methods

**25 papers**

In this section we collect all the papers introducing a continual learning strategy employing some regularization methods.

- [Modeling the Background for Incremental Learning in Semantic Segmentation](http://arxiv.org/abs/2002.00718) by Fabio Cermelli, Massimiliano Mancini, Samuel Rota Bulò, Elisa Ricci and Barbara Caputo. *CVPR*, 9233--9242, 2020. 
- [PLOP: Learning without Forgetting for Continual Semantic Segmentation](https://arxiv.org/abs/2011.11390) by Arthur Douillard, Yifu Chen, Arnaud Dapogny and Matthieu Cord. *arXiv*, 2020. 
- [Insights from the Future for Continual Learning](https://arxiv.org/abs/2006.13748) by Arthur Douillard, Eduardo Valle, Charles Ollion, Thomas Robert and Matthieu Cord. *arXiv*, 2020. 
- [PODNet: Pooled Outputs Distillation for Small-Tasks Incremental Learning](https://arxiv.org/abs/2004.13513) by Arthur Douillard, Matthieu Cord, Charles Ollion, Thomas Robert and Eduardo Valle. *European Conference on Computer Vision (ECCV)*, 2020. 
- [Uncertainty-Guided Continual Learning with Bayesian Neural Networks](https://openreview.net/pdf?id=HklUCCVKDB) by Sayna Ebrahimi, Mohamed Elhoseiny, Trevor Darrell and Marcus Rohrbach. *ICLR*, 2020. [bayes] [cifar] [fashion] [mnist] 
- [Continual Learning of Object Instances](http://arxiv.org/abs/2004.10862) by Kishan Parshotam and Mert Kilickaya. *CVPR 2020: Workshop on Continual Learning in Computer Vision*, 2020. [vision] 
- [Efficient Continual Learning in Neural Networks with Embedding Regularization](http://www.sciencedirect.com/science/article/pii/S092523122030151X) by Jary Pomponi, Simone Scardapane, Vincenzo Lomonaco and Aurelio Uncini. *Neurocomputing*, 2020. [cifar] [mnist] 
- [Continual Learning with Hypernetworks](https://openreview.net/forum?id=SJgwNerKvB) by Johannes von Oswald, Christian Henning, João Sacramento and Benjamin F Grewe. *International Conference on Learning Representations*, 2020. [cifar] [mnist] 
- [Uncertainty-Based Continual Learning with Adaptive Regularization](https://papers.nips.cc/paper/8690-uncertainty-based-continual-learning-with-adaptive-regularization.pdf) by Hongjoon Ahn, Sungmin Cha, Donggyu Lee and Taesup Moon. *NeurIPS*, 4392--4402, 2019. [bayes] [cifar] [mnist] 
- [Task-Free Continual Learning](https://openaccess.thecvf.com/content_CVPR_2019/papers/Aljundi_Task-Free_Continual_Learning_CVPR_2019_paper.pdf) by Rahaf Aljundi, Klaas Kelchtermans and Tinne Tuytelaars. *The IEEE Conference on Computer Vision and Pattern Recognition (CVPR)*, 2019. [vision] 
- [Learning without Memorizing](https://openaccess.thecvf.com/content_CVPR_2019/papers/Dhar_Learning_Without_Memorizing_CVPR_2019_paper.pdf) by Prithviraj Dhar, Rajat Vikram Singh, Kuan-Chuan Peng, Ziyan Wu and Rama Chellappa. *CVPR*, 2019. [cifar] 
- [Incremental Learning Techniques for Semantic Segmentation](http://arxiv.org/abs/1907.13372) by Umberto Michieli and Pietro Zanuttigh. *Proceedings - 2019 International Conference on Computer Vision Workshop, ICCVW 2019*, 3205--3212, 2019. 
- [Functional Regularisation for Continual Learning Using Gaussian Processes](http://arxiv.org/abs/1901.11356) by Michalis K Titsias, Jonathan Schwarz, Alexander G de G Matthews, Razvan Pascanu and Yee Whye Teh. *arXiv*, 2019. [mnist] [omniglot] 
- [Memory Aware Synapses: Learning What (Not) to Forget](https://openaccess.thecvf.com/content_ECCV_2018/papers/Rahaf_Aljundi_Memory_Aware_Synapses_ECCV_2018_paper.pdf) by Rahaf Aljundi, Francesca Babiloni, Mohamed Elhoseiny, Marcus Rohrbach and Tinne Tuytelaars. *The European Conference on Computer Vision (ECCV)*, 2018. [vision] 
- [Riemannian Walk for Incremental Learning: Understanding Forgetting and Intransigence](https://openaccess.thecvf.com/content_ECCV_2018/html/Arslan_Chaudhry__Riemannian_Walk_ECCV_2018_paper.html) by Arslan Chaudhry, Puneet K. Dokania, Thalaiyasingam Ajanthan and Philip H. S. Torr. *Proceedings of the European Conference on Computer Vision (ECCV)*, 532--547, 2018. 
- [Rotate Your Networks: Better Weight Consolidation and Less Catastrophic Forgetting](https://ieeexplore.ieee.org/document/8545895/) by Xialei Liu, Marc Masana, Luis Herranz, Joost Van de Weijer, Antonio M. Lopez and Andrew D Bagdanov. *2018 24th International Conference on Pattern Recognition (ICPR)*, 2262--2268, 2018. [cifar] [mnist] 
- [Online Structured Laplace Approximations For Overcoming Catastrophic Forgetting](http://arxiv.org/abs/1805.07810) by Hippolyt Ritter, Aleksandar Botev and David Barber. *arXiv*, 2018. [bayes] [mnist] 
- [Overcoming Catastrophic Forgetting with Hard Attention to the Task](https://arxiv.org/pdf/1801.01423.pdf) by Joan Serrà, D\d́ac Surís, Marius Miron and Alexandros Karatzoglou. *ICML*, 2018. [cifar] [fashion] [mnist] 
- [Overcoming Catastrophic Forgetting in Neural Networks](http://arxiv.org/abs/1612.00796) by James Kirkpatrick, Razvan Pascanu, Neil Rabinowitz, Joel Veness, Guillaume Desjardins, Andrei A Rusu, Kieran Milan, John Quan, Tiago Ramalho, Agnieszka Grabska-Barwinska, Demis Hassabis, Claudia Clopath, Dharshan Kumaran and Raia Hadsell. *PNAS*, 3521--3526, 2017. [mnist] 
- [Overcoming Catastrophic Forgetting by Incremental Moment Matching](http://arxiv.org/abs/1703.08475) by Sang-Woo Lee, Jin-Hwa Kim, Jaehyun Jun, Jung-Woo Ha and Byoung-Tak Zhang. *Advances in Neural Information Processing Systems*, 4653--4663, 2017. [bayes] [cifar] [mnist] 
- [Lifelong Generative Modeling](http://arxiv.org/abs/1705.09847) by Jason Ramapuram, Magda Gregorova and Alexandros Kalousis. *arXiv*, 1--14, 2017. [fashion] [generative] [mnist] 
- [Continual Learning in Generative Adversarial Nets](http://arxiv.org/abs/1705.08395) by Ari Seff, Alex Beatson, Daniel Suo and Han Liu. *arXiv*, 1--9, 2017. [mnist] 
- [Incremental Learning of Object Detectors without Catastrophic Forgetting](http://arxiv.org/abs/1708.06977) by Konstantin Shmelkov, Cordelia Schmid and Karteek Alahari. *Proceedings of the IEEE International Conference on Computer Vision*, 3420--3429, 2017. 
- [Continual Learning Through Synaptic Intelligence](http://proceedings.mlr.press/v70/zenke17a.html) by Friedemann Zenke, Ben Poole and Surya Ganguli. *International Conference on Machine Learning*, 3987--3995, 2017. [cifar] [mnist] 
- [Learning without Forgetting](http://arxiv.org/abs/1606.09282) by Zhizhong Li and Derek Hoiem. *European Conference on Computer Vision*, 614--629, 2016. [imagenet] 

### Rehearsal Methods

**25 papers**

In this section we collect all the papers introducing a continual learning strategy employing some rehearsal methods.

- [Continual Prototype Evolution: Learning Online from Non-Stationary Data Streams](https://openaccess.thecvf.com/content/ICCV2021/html/De_Lange_Continual_Prototype_Evolution_Learning_Online_From_Non-Stationary_Data_Streams_ICCV_2021_paper.html) by Matthias De Lange and Tinne Tuytelaars. *Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)*, 8250--8259, 2021. [cifar] [framework] [mnist] [vision] 
- [Replay in Deep Learning: Current Approaches and Missing Biological Elements](https://direct.mit.edu/neco/article-abstract/33/11/2908/107071/Replay-in-Deep-Learning-Current-Approaches-and?redirectedFrom=fulltext) by Tyler L. Hayes, Giri P. Krishnan, Maxim Bazhenov, Hava T. Siegelmann, Terrence J. Sejnowski and Christopher Kanan. *Neural Computation*, 2908--2950, 2021. 
- [Distilled Replay: Overcoming Forgetting through Synthetic Samples](http://arxiv.org/abs/2103.15851) by Andrea Rosasco, Antonio Carta, Andrea Cossu, Vincenzo Lomonaco and Davide Bacciu. *1st International Workshop on Continual Semi-Supervised Learning (CSSL) at IJCAI*, 2021. 
- [Rehearsal Revealed: The Limits and Merits of Revisiting Samples in Continual Learning](https://openaccess.thecvf.com/content/ICCV2021/html/Verwimp_Rehearsal_Revealed_The_Limits_and_Merits_of_Revisiting_Samples_in_ICCV_2021_paper.html) by Eli Verwimp, Matthias De Lange and Tinne Tuytelaars. *Proceedings of the IEEE/CVF International Conference on Computer Vision*, 9385--9394, 2021. 
- [Online Coreset Selection for Rehearsal-based Continual Learning](http://arxiv.org/abs/2106.01085) by Jaehong Yoon, Divyam Madaan, Eunho Yang and Sung Ju Hwang. *arXiv*, 2021. 
- [CALM: Continuous Adaptive Learning for Language Modeling](http://arxiv.org/abs/2004.03794) by Kristjan Arumae and Parminder Bhatia. *arXiv*, 2020. [nlp] 
- [ScaIL: Classifier Weights Scaling for Class Incremental Learning](https://doi.org/10.1109/WACV45572.2020.9093562) by Eden Belouadah and Adrian Popescu. *IEEE Winter Conference on Applications of Computer Vision, WACV 2020, Snowmass Village, CO, USA, March 1-5, 2020*, 1255--1264, 2020. 
- [REMIND Your Neural Network to Prevent Catastrophic Forgetting](http://arxiv.org/abs/1910.02509) by Tyler L. Hayes, Kushal Kafle, Robik Shrestha, Manoj Acharya and Christopher Kanan. *Proceedings of the 2020 ECCV*, 2020. 
- [CLOPS: Continual Learning of Physiological Signals](http://arxiv.org/abs/2004.09578) by Dani Kiyasseh, Tingting Zhu and David A Clifton. *arXiv*, 2020. 
- [Continual Learning with Bayesian Neural Networks for Non-Stationary Data](https://iclr.cc/virtual_2020/poster_SJlsFpVtDB.html) by Richard Kurle, Botond Cseke, Alexej Klushyn, Patrick van der Smagt and Stephan Günnemann. *Eighth International Conference on Learning Representations*, 2020. [bayes] 
- [GDumb: A Simple Approach That Questions Our Progress in Continual Learning](https://link.springer.com/chapter/10.1007%2F978-3-030-58536-5_31) by Ameya Prabhu, Philip H. S. Torr and Puneet K. Dokania. *Computer Vision – ECCV 2020*, 524--540, 2020. 
- [Graph-Based Continual Learning](https://openreview.net/forum?id=HHSEKOnPvaO) by Binh Tang and David S. Matteson. *International Conference on Learning Representations*, 2020. 
- [Brain-Inspired Replay for Continual Learning with Artificial Neural Networks](https://www.nature.com/articles/s41467-020-17866-2) by Gido M. van de Ven, Hava T. Siegelmann and Andreas S. Tolias. *Nature Communications*, 2020. [cifar] [framework] [generative] [mnist] 
- [Continual Learning with Hypernetworks](https://openreview.net/forum?id=SJgwNerKvB) by Johannes von Oswald, Christian Henning, João Sacramento and Benjamin F Grewe. *International Conference on Learning Representations*, 2020. [cifar] [mnist] 
- [Gradient Based Sample Selection for Online Continual Learning](http://papers.nips.cc/paper/9354-gradient-based-sample-selection-for-online-continual-learning.pdf) by Rahaf Aljundi, Min Lin, Baptiste Goujaud and Yoshua Bengio. *Advances in Neural Information Processing Systems 32*, 11816--11825, 2019. [cifar] [mnist] 
- [Online Continual Learning with Maximal Interfered Retrieval](http://papers.nips.cc/paper/9357-online-continual-learning-with-maximal-interfered-retrieval.pdf) by Rahaf Aljundi, Eugene Belilovsky, Tinne Tuytelaars, Laurent Charlin, Massimo Caccia, Min Lin and Lucas Page-Caccia. *Advances in Neural Information Processing Systems 32*, 11849--11860, 2019. [cifar] [mnist] 
- [IL2M: Class Incremental Learning With Dual Memory](https://doi.org/10.1109/ICCV.2019.00067) by Eden Belouadah and Adrian Popescu. *2019 IEEE/CVF International Conference on Computer Vision, ICCV 2019, Seoul, Korea (South), October 27 - November 2, 2019*, 583--592, 2019. 
- [On Tiny Episodic Memories in Continual Learning](https://github.com/facebookresearch/agem http://arxiv.org/abs/1902.10486) by Arslan Chaudhry, Marcus Rohrbach, Mohamed Elhoseiny, Thalaiyasingam Ajanthan, Puneet K Dokania, Philip H S Torr and Marc'Aurelio Ranzato. *arXiv*, 2019. [cifar] [imagenet] [mnist] 
- [Facilitating Bayesian Continual Learning by Natural Gradients and Stein Gradients](http://arxiv.org/abs/1904.10644) by Yu Chen, Tom Diethe and Neil Lawrence. *arXiv*, 2019. [bayes] 
- [Memory Efficient Experience Replay for Streaming Learning](https://github.com/tyler-hayes/ExStream. http://arxiv.org/abs/1809.05922) by Tyler L Hayes, Nathan D Cahill and Christopher Kanan. *IEEE International Conference on Robotics and Automation (ICRA)*, 2019. [core50] 
- [Experience Replay for Continual Learning](http://papers.nips.cc/paper/8327-experience-replay-for-continual-learning.pdf) by David Rolnick, Arun Ahuja, Jonathan Schwarz, Timothy P Lillicrap and Greg Wayne. *NeurIPS*, 350--360, 2019. 
- [Prototype Reminding for Continual Learning](http://arxiv.org/abs/1905.09447) by Mengmi Zhang, Tao Wang, Joo Hwee Lim and Jiashi Feng. *arXiv*, 1--10, 2019. [bayes] [cifar] [imagenet] [mnist] 
- [Selective Experience Replay for Lifelong Learning](http://arxiv.org/abs/1802.10269) by David Isele and Akansel Cosgun. *Thirty-Second AAAI Conference on Artificial Intelligence*, 3302--3309, 2018. 
- [iCaRL: Incremental Classifier and Representation Learning](http://openaccess.thecvf.com/content_cvpr_2017/papers/Rebuffi_iCaRL_Incremental_Classifier_CVPR_2017_paper.pdf) by Sylvestre-Alvise Rebuffi, Alexander Kolesnikov, Georg Sperl and Christoph H Lampert. *The IEEE Conference on Computer Vision and Pattern Recognition (CVPR)*, 2017. [cifar] 
- [Preventing Catastrophic Interference in  MultipleSequence Learning Using Coupled Reverberating Elman Networks](http://leadserv.u-bourgogne.fr/IMG/pdf/CogSci2002.Rsrn.pdf) by Bernard Ans, Stephane Rousset, Robert M. French and Serban C. Musca. *Proceedings of the 24th Annual Conference of the Cognitive Science Society*, 2002. [rnn] 

### Review Papers and Books

**22 papers**

In this section we collect all the main review papers and books on continual learning and related subjects. These may constitute a solid starting point for continual learning newcomers.

- [A Comparative Study of Calibration Methods for Imbalanced Class Incremental Learning](https://arxiv.org/abs/2202.00386) by Umang Aggarwal, Adrian Popescu, Eden Belouadah and Céline Hudelot. *arXiv*, 2022. 
- [A Comprehensive Study of Class Incremental Learning Algorithms for Visual Tasks](https://doi.org/10.1016/j.neunet.2020.12.003) by Eden Belouadah, Adrian Popescu and Ioannis Kanellos. *Neural Networks*, 38--54, 2021. 
- [Continual Learning for Recurrent Neural Networks: An Empirical Evaluation](https://www.sciencedirect.com/science/article/pii/S0893608021002847) by Andrea Cossu, Antonio Carta, Vincenzo Lomonaco and Davide Bacciu. *Neural Networks*, 607--627, 2021. [rnn] 
- [A Continual Learning Survey: Defying Forgetting in Classification Tasks](http://arxiv.org/abs/1909.08383) by Matthias De Lange, Rahaf Aljundi, Marc Masana, Sarah Parisot, Xu Jia, Ales Leonardis, Gregory Slabaugh and Tinne Tuytelaars. *IEEE Transactions on Pattern Analysis and Machine Intelligence*, 2021. [framework] 
- [Replay in Deep Learning: Current Approaches and Missing Biological Elements](http://arxiv.org/abs/2104.04132) by Tyler L. Hayes, Giri P. Krishnan, Maxim Bazhenov, Hava T. Siegelmann, Terrence J. Sejnowski and Christopher Kanan. *arXiv*, 2021. 
- [Continual Lifelong Learning in Natural Language Processing: A Survey](https://www.aclweb.org/anthology/2020.coling-main.574) by Magdalena Biesialska, Katarzyna Biesialska and Marta R. Costa-jussà. *Proceedings of the 28th International Conference on Computational Linguistics*, 6523--6541, 2020. [nlp] 
- [Embracing Change: Continual Learning in Deep Neural Networks](https://doi.org/10.1016/j.tics.2020.09.004) by Raia Hadsell, Dushyant Rao, Andrei A Rusu and Razvan Pascanu. *Trends in Cognitive Sciences*, 2020. 
- [Continual Learning for Robotics: Definition, Framework, Learning Strategies, Opportunities and Challenges](http://www.sciencedirect.com/science/article/pii/S1566253519307377) by Timothée Lesort, Vincenzo Lomonaco, Andrei Stoian, Davide Maltoni, David Filliat and Natalia Díaz-Rodr\ǵuez. *Information Fusion*, 52--68, 2020. [framework] 
- [A Wholistic View of Continual Learning with Deep Neural Networks: Forgotten Lessons and the Bridge to Active and Open World Learning](http://arxiv.org/abs/2009.01797) by Martin Mundt, Yong Won Hong, Iuliia Pliushch and Visvanathan Ramesh. *arXiv*, 32, 2020. [bayes] [framework] 
- [A Review of Off-Line Mode Dataset Shifts](https://ieeexplore.ieee.org/document/9141463/) by Carla C. Takahashi and Antonio P. Braga. *IEEE Computational Intelligence Magazine*, 16--27, 2020. 
- [Continual Learning with Neural Networks: A Review](https://dl.acm.org/doi/pdf/10.1145/3297001.3297062) by Abhijeet Awasthi and Sunita Sarawagi. *Proceedings of the ACM India Joint International Conference on Data Science and Management of Data*, 362--365, 2019. 
- [Continual Lifelong Learning with Neural Networks: A Review](http://www.sciencedirect.com/science/article/pii/S0893608019300231) by German I Parisi, Ronald Kemker, Jose L Part, Christopher Kanan and Stefan Wermter. *Neural Networks*, 54--71, 2019. [framework] 
- [Lifelong Machine Learning, Second Edition](https://www.cs.uic.edu/ liub/lifelong-machine-learning.html) by Zhiyuan Chen and Bing Liu. *Synthesis Lectures on Artificial Intelligence and Machine Learning*, 2018. 
- [Measuring Catastrophic Forgetting in Neural Networks](https://arxiv.org/pdf/1708.02072.pdf) by Ronald Kemker, Marc McClure, Angelina Abitino, Tyler L Hayes and Christopher Kanan. *Thirty-Second AAAI Conference on Artificial Intelligence*, 2018. [mnist] 
- [Generative Models from the Perspective of Continual Learning](http://arxiv.org/abs/1812.09111) by Timothée Lesort, Hugo Caselles-Dupré, Michael Garcia-Ortiz, Andrei Stoian and David Filliat. *Proceedings of the International Joint Conference on Neural Networks*, 2018. [cifar] [generative] [mnist] 
- [Incremental On-Line Learning: A Review and Comparison of State of the Art Algorithms](https://doi.org/10.1016/j.neucom.2017.06.084) by Viktor Losing, Barbara Hammer and Heiko Wersing. *Neurocomputing*, 1261--1274, 2018. 
- [A Comprehensive, Application-Oriented Study of Catastrophic Forgetting in DNNs](https://openreview.net/pdf?id=BkloRs0qK7) by B Pfülb and A Gepperth. *ICLR*, 2018. [fashion] [mnist] 
- [Avoiding Catastrophic Forgetting](https://linkinghub.elsevier.com/retrieve/pii/S1364661317300736) by  and Michael E. Hasselmo. *Trends in Cognitive Sciences*, 407--408, 2017. 
- [Lifelong Machine Learning: A Paradigm for Continuous Learning](https://doi.org/10.1007/s11704-016-6903-6) by  and Bing Liu. *Frontiers of Computer Science*, 359--361, 2017. 
- [Learning in Nonstationary Environments: A Survey](http://ieeexplore.ieee.org/document/7296710/) by Gregory Ditzler, Manuel Roveri, Cesare Alippi and Robi Polikar. *IEEE Computational Intelligence Magazine*, 12--25, 2015. 
- [Never-Ending Learning](https://dl.acm.org/doi/10.1145/3191513) by Tom Mitchell, William W Cohen, E Hruschka, Partha P Talukdar, B Yang, Justin Betteridge, Andrew Carlson, B Dalvi, Matt Gardner, Bryan Kisiel, J Krishnamurthy, Ni Lao, K Mazaitis, T Mohamed, N Nakashole, E Platanios, A Ritter, M Samadi, B Settles, R Wang, D Wijaya, A Gupta, X Chen, A Saparov, M Greaves and J Welling. *Communications of the Acm*, 2302--2310, 2015. 
- [Catastrophic Forgetting; Catastrophic Interference; Stability; Plasticity; Rehearsal.](http://www.tandfonline.com/doi/abs/10.1080/09540099550039318) by  and Anthony Robins. *Connection Science*, 123--146, 1995. [dual] 

### Robotics

**6 papers**

In this section we maintain a list of all Robotics papers that can be related to continual learning.

- [Online Continual Learning for Embedded Devices](http://arxiv.org/abs/2203.10681) by Tyler L. Hayes and Christopher Kanan. *arXiv*, 2022. 
- [Tell Me What This Is: Few-Shot Incremental Object Learning by a Robot](http://arxiv.org/abs/2008.00819) by Ali Ayub and Alan R. Wagner. *arXiv*, 2020. 
- [Online Object and Task Learning via Human Robot Interaction](https://arxiv.org/abs/1809.08722) by M. Dehghan, Z. Zhang, M. Siam, J. Jin, L. Petrich and M. Jagersand. *2019 International Conference on Robotics and Automation (ICRA)*, 2019. 
- [Towards Lifelong Self-Supervision: A Deep Learning Direction for Robotics](http://arxiv.org/abs/1611.00201) by  and Jay M Wong. *arXiv*, 2016. 
- [A Lifelong Learning Perspective for Mobile Robot Control](http://www.sciencedirect.com/science/article/pii/B9780444822505500153) by  and Sebastian Thrun. *Intelligent Robots and Systems*, 201--214, 1995. 
- [Explanation-Based Neural Network Learning for Robot Control](https://papers.nips.cc/paper/614-explanation-based-neural-network-learning-for-robot-control.pdf) by Tom M Mitchell and Sebastian B Thrun. *Advances in Neural Information Processing Systems 5*, 1993. 


