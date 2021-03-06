# -*- coding: utf-8 -*-
# @Time     : 2018/11/24 20:44
# @Author   : HuangYin
# @FileName : main.py
# @Software : PyCharm
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
import math

if __name__ == '__main__':
    # X1, y1 = datasets.make_circles(n_samples=5000, factor=.6,
    #                                noise=.05)
    # X2, y2 = datasets.make_blobs(n_samples=1000, n_features=2, centers=[[1.2, 1.2]], cluster_std=[[.1]],
    #                              random_state=9)
    #
    # X1 = np.concatenate((X1, X2))
    from Readfile import readfile

    X = readfile()

    # plt.scatter(X[1:200, 0], X[1:200, 1], marker='o')
    from sklearn.cluster import DBSCAN

    Y = X[1:, 0:2].astype(np.float64)
    # Y = (math.pi / 180) * Y
    min_samples =24
    y_pred = DBSCAN(eps=(4 * 0.01) * (0.1) ** 3, min_samples=min_samples).fit_predict(Y)
    # 4 / 1110000
    # plt.scatter(Y[:200, 0], Y[:200, 1], c=y_pred[:200])
    # # plt.axis([0, 100, 0, 200])
    # # plt.axis('off')
    # # plt.set(gca, 'XTick', [2: 2:46])
    # plt.plot(y_pred)
    # plt.show()

    from IMR import initIMR

    T = min_samples*0.5
    I_CR = y_pred.reshape(1, -1)
    I_MR = initIMR(I_CR, T=T)
    from InitT1T2 import initT1T2

    T_MR1, T_MR2 = initT1T2(I_CR, I_MR, T=T)
    from ImproveIMR import ImproveIMR

    I_MR = ImproveIMR(I_MR, T_MR1, T_MR2, T)
    print()
