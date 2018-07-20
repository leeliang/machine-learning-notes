# 目录 

* [1 绪论](#1-绪论)
	* [1.1 No Free Lunch Theorem](11-no-free-lunch-theorem) 
* [2 模型评估与选择](#2-模型评估与选择)
	* [2.1 评估方法](#21-评估方法)
	* [2.2 最终模型](#22-最终模型)
	* [2.3 性能度量](#23-性能度量)
	* [2.4 比较检验](#24-比较检验)

***

# 1 绪论
## 1.1 No Free Lunch Theorem
总误差与学习算法无关，但针对特定问题时，算法表现不同。脱离实际问题，空谈学习算法毫无意义。



# 2 模型评估与选择
## 2.1 评估方法
* 留出法（hold-out）
 
   常见做法是大约 2/3~4/5 的样本用于训练，剩余样本用于测试。
* 交叉验证法（cross validation）

	k 折交叉验证通常要随机使用不同划分重复 p 次，常见的有 10 次 10 折交叉验证。
	* 留一法（LOO, LEVAE ONE OUT）
* 自助法（bootstrapping）

	数据集较小时很有用，又称包外估计（out of bag estimate），但是改变了初始数据集的分布，可能引入估计偏差，在数据量足够时，留出法和交叉验证法更常用。
	
## 2.2 最终模型
在学习算法和参数配置已选定后，需要利用完整数据集重新训练模型，得到最终模型。

## 2.3 性能度量
* 查准率、查全率、F1

查准率为在预测为正例的结果中有多少是真正的正例，查全率为真实结果为正例的样本中有多少预测结果为正例。

![](https://github.com/leeliang/machine-learning-notes/raw/master/watermelon/equation_files/latex-image-1.jpeg)

F1 是基于查准率和查全率的调和平均数定义的，用于综合考虑查准率和查全率的度量。若对查准率和查全率的重视程度不同，则采用更一般的加权调和平均。

![](https://github.com/leeliang/machine-learning-notes/raw/master/watermelon/equation_files/latex-image-2.jpeg)

$\beta = 1$ 时退化为 F1，$\beta<1$ 时查全率影响更大，反之亦然。 



我们可根据学习器的结果对样例进行排序，排在最前面的是最可能是正例的样本，按此顺序逐个把样本作为正例进行预测，则得到了查准率和查全率的序列，以查准率为纵轴，查全率为横轴的图为P-R曲线。以 True Positive Rate 为纵轴，False Positve Rate 为横轴的图为 ROC 曲线。TPR 是真实情况为正例中有多少真正例， FPR 是真实情况为反例的样本中假正例。

![](https://github.com/leeliang/machine-learning-notes/raw/master/watermelon/equation_files/latex-image-3.jpeg)

ROC 曲线下的面积为 AUC。

## 2.4 比较检验
* 二项检验、t 检验 (一个算法检验)
* 交叉验证 t 检验 （一个数据集两个算法）
* McNemar 检验 （一个数据集两个算法、二分类问题）
* Friedman 检验和 Nemenyi 后续检验 (多数据集多算法)

## 2.5 偏差与方差
偏差-方差分解是解释学习器泛化性能的一种重要工具。泛化误差可以分解为偏差、方差和噪声之和。

![](https://github.com/leeliang/machine-learning-notes/raw/master/watermelon/equation_files/latex-image-4.jpeg)

偏差度量了偏离程度；方差度量了同样大小的训练集的变化导致的学习性能变化，刻画了数据扰动造成的影响；噪声为当前任务在任何学习算法下所能达到的泛化误差下届，刻画了问题的难度。偏差-方差分解说明泛化性能由学习算法的能力、数据的充分性以及任务的难度共同决定。


