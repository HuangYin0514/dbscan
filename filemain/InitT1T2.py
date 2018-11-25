# -*- coding: utf-8 -*-
# @Time     : 2018/11/25 9:00
# @Author   : HuangYin
# @FileName : InitT1T2.py
# @Software : PyCharm

import numpy  as np


def initT1T2(I_CR, I_MR, T):
    n = I_MR.shape[1]
    T_MR1 = np.zeros(I_MR.shape)
    T_MR2 = np.zeros(I_MR.shape)
    for i in range(0, n):
        if I_MR[0, i] == 0 and I_MR[0, i + 1] == 0:
            T_MR1[0, i] = i * T
            T_MR2[0, i] = (i + 1) * T
        if I_MR[0, i] == 0 and I_MR[0, i + 1] != 0:
            T_MR1[0, i] = i * T
            # T_MR2[0, i + 1] = (i + 1) * T
        if I_MR[0, i] != 0 and I_MR[0, i + 1] == 0:
            # T_MR1[0, i] = i * T
            T_MR2[0, i] = (i + 1) * T
        if I_MR[0, i] != 0 and I_MR[0, i + 1] != 0:
            # T_MR1[0, i] = i * T
            T_MR2[0, i] = (i + 1) * T
    pass


def findNext()
