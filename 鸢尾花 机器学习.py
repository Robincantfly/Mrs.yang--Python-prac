#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:yehao
from sklearn.datasets import load_iris
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm

iris_data=load_iris()
print("鸢尾花类别",iris_data["target_names"])
print(iris_data["target"])
print("鸢尾花属性",iris_data["feature_names"])
print(iris_data["data"])

num_samples, num_features=iris_data["data"].shape
num_classes=2
feature_names=["SL","SW","PL","PW"]

fig, ax=plt.subplots(num_features, num_features, figsize=(16,16))
markers="+o^"
for i in range(num_features):
    for j in range(num_features):
        for k in range(num_classes):
            ax[i][j].scatter(
                    iris_data["data"][(k*50):(k*50+50),i],
                    iris_data["data"][(k*50):(k*50+50),j],
                    marker=markers[k]
            )
            ax[i][j].set_title(feature_names[i]+"-vs-"+feature_names[j])
plt.show()

#保留10个用于测试的样本
x=iris_data["data"][0:(50*num_classes-10),0:2]
y=iris_data["target"][0:(50*num_classes-10)]
svm_classifier=svm.SVC(kernel="linear")
svm_classifier.fit(x,y)
predict=svm_classifier.predict(iris_data["data"][(50*num_classes-10):(50*num_classes),2:4])
print("预测类别", predict)
print("真实类别",iris_data["target"][(50*num_classes-10):(50*num_classes)])

plt.scatter(iris_data["data"][0:50,2],iris_data["data"][0:50,3],marker=markers[0])
plt.scatter(iris_data["data"][50:90,2],iris_data["data"][50:90,3],marker=markers[1])
xlim=(0,6)
ylim=(0,2)
coef=svm_classifier.coef_[0]
support_vectors=svm_classifier.support_vectors_
class_0_sv=support_vectors[0]
class_1_sv=support_vectors[1]

x=np.array([1.5,2.5])
y=(np.dot(coef,class_0_sv)-x*coef[0])/coef[1]
plt.plot(x,y)

x=np.array([3,4])
y=(np.dot(coef,class_1_sv)-x*coef[0])/coef[1]
plt.plot(x,y)
plt.title("PL-vs-PW")
plt.show()
