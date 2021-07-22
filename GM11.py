# -*- coding: utf-8 -*-
from typing import List, Any
import numpy as np


def GM11(x, n):
    '''
    灰色预测
    x：序列，numpy对象
    n:需要往后预测的个数
    '''
    x1 = x.cumsum()  # 一次累加
    z1 = (x1[:len(x1) - 1] + x1[1:]) / 2.0  # 紧邻均值
    z1 = z1.reshape((len(z1), 1))
    B = np.append(-z1, np.ones_like(z1), axis=1)
    Y = x[1:].reshape((len(x) - 1, 1))
    # a为发展系数 b为灰色作用量
    [[a], [b]] = np.dot(np.dot(np.linalg.inv(np.dot(B.T, B)), B.T), Y)  # 计算参数
    result = (x[0] - b / a) * np.exp(-a * (n - 1)) - (x[0] - b / a) * np.exp(-a * (n - 2))
    s1_2 = x.var()  # 原序列方差
    e = list()  # 残差序列
    for index in range(1, x.shape[0] + 1):
        predict = (x[0] - b / a) * np.exp(-a * (index - 1)) - (x[0] - b / a) * np.exp(-a * (index - 2))
        e.append(x[index - 1] - predict)
    s2_2 = np.array(e).var()  # 残差方差
    C = s2_2 / s1_2  # 后验差比
    if C <= 0.35:
        assess = '后验差比<=0.35，模型精度等级为优秀'
    elif C <= 0.5:
        assess = '后验差比<=0.5，模型精度等级为良好'
    elif C <= 0.65:
        assess = '后验差比<=0.65，模型精度等级为合格'
    else:
        assess = '后验差比>0.65，模型精度等级为不合格'
    # 预测数据
    predict: List[Any] = list()
    for index in range(x.shape[0] + 1, x.shape[0] + n + 1):
        predict.append((x[0] - b / a) * np.exp(-a * (index - 1)) - (x[0] - b / a) * np.exp(-a * (index - 2)))
    predict = np.array(predict)
    return [predict, assess]


# 读入目前已经有的数据
data = np.array([1, 66, 1, 57, 1, 139])
# 需要往后预测的数据数量
y = 3
result = GM11(data, y)
# 结果保留整数
predict = np.round(result[0], 0)
print('预测值:', predict)
print('模型精度:', result[1])
