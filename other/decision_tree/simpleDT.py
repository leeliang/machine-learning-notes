#!/usr/bin/env python
# coding: utf-8
"""
Created on 2017-08
@author: Liang
"""
from math import log
import operator
#
def calcShannonEnt(dataset):
    """
    计算数据集的熵
    输入：数据集
    输出：熵
    """
    numEntris = len(dataset)
    labelCounts = {}
    for featVec in dataset:
        currentLabel = featVec[-1] #每行数据中的最后一个数，即数据的决策结果 label
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel]+=1  #labelCounts记录了叶节点的种类（keys）和每个类的数量（values）
    #
    shannonEnt = 0
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntris
        shannonEnt -= prob*log(prob,2)
    return shannonEnt


# ###### 按某个特征分类后的数据，如特征为Long的数据：[['Coarse', 'Male'], ['Thin', 'Female'], ['Coarse', 'Female'], ['Coarse', 'Female']]



#axis = [0, ..., numFeature]  value = 某一特征的所有取值
def splitDataSet(dataSet, axis, value):
    """
    提取按某个特征划分后的数据子集
    输入：  数据集 dataSet
            特征 axis
            特征取值 value
    输出： 数据子集
    """
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reduceFeatVec = featVec[:axis]
            reduceFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reduceFeatVec)
    return retDataSet

def chooseBestFeatureToSplit(dataSet):
    """
    选择最优划分特征
    输入： 数据集
    输出： 最优特征
    """
    numFeatures = len(dataSet[0])-1
    baseEntropy = calcShannonEnt(dataSet) #原始数据的熵
    bestInfoGain = 0
    bestFfeature = -1
    for i in range(numFeatures):   #循环所有特征
        featList = [example[i] for example in dataSet]
        uniqueVals = set(featList)  #某个特征的取值，如[long,short]
        newEntropy = 0
        for value in uniqueVals:    
            subDataSet = splitDataSet(dataSet,i,value) #按某一特征的取值分类，如Long
            prob = len(subDataSet)/float(len(dataSet))
            newEntropy += prob*calcShannonEnt(subDataSet)  #计算按该特征分类的熵，如DATASET(LONG)和DATASET（Short）的熵
        infoGain = baseEntropy - newEntropy   #计算增益，原始熵-Dataset(long)的熵-Dataset(short)的熵
        if (infoGain>bestInfoGain):
            bestInfoGain = infoGain
            bestFfeature = i   #选出最优分类特征
    return bestFfeature

def majorityCnt(classList):
    """
    按包含同一 label 的数量排序
    输入： label 集
    输出： 排序后的结果
    """    
    classCount={}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote]=0
        classCount[vote]+=1
    sortedClassCount = sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]


def createTree(dataSet,labels):
    """
    递归产生决策树
    输入： 数据集
            标记集
    输出： 决策树
    """
    classList=[example[-1] for example in dataSet]  # label 集
    if classList.count(classList[0])==len(classList):
        return classList[0]
    if len(dataSet[0])==1:
        return majorityCnt(classList)
    bestFeat=chooseBestFeatureToSplit(dataSet) #选择最优特征
    bestFeatLabel=labels[bestFeat]
    myTree={bestFeatLabel:{}} #分类结果以字典形式保存
    del(labels[bestFeat])
    featValues=[example[bestFeat] for example in dataSet]
    uniqueVals=set(featValues)
    for value in uniqueVals:
        subLabels=labels[:]
        myTree[bestFeatLabel][value]=createTree(splitDataSet(dataSet,bestFeat,value),subLabels)
    return myTree


if __name__=='__main__':
    createTree(dataSet, labels)  # 输出决策树模型结果






