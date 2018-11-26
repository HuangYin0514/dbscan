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
    for i in range(1, n - 1):
        if I_MR[0, i] == 0 and I_MR[0, i + 1] == 0:
            T_MR1[0, i] = i * T
            T_MR2[0, i] = (i + 1) * T
        if I_MR[0, i] == 0 and I_MR[0, i + 1] != 0:
            # continue
            T_MR1[0, i] = i * T
            T_MR2[0, i] = find2(i, I_MR) * T
            # T_MR2[0, i + 1] = (i + 1) * T
        if I_MR[0, i] != 0 and I_MR[0, i + 1] == 0:
            T_MR1[0, i] = find1(i, I_MR) * T
            T_MR2[0, i] = (i + 1) * T
        if I_MR[0, i] != 0 and I_MR[0, i + 1] != 0:
            z = round(i * T)
            while I_CR[0, z] == I_MR[0, i] and z != (i + 1) * T:
                z += 1
            if z != (i + 1) * T:
                T_MR1[0, i] = z
            else:
                T_MR1[0, i] = i * T
            z = round((i + 1) * T)
            while I_CR[0, z] == I_MR[0, i + 1] and z != i * T:
                z -= 1
            if z != i * T:
                T_MR2[0, i] = z
            else:
                T_MR2[0, i] = (i + 1) * T
    return T_MR1, T_MR2


def find2(j, I_MR):
    n = I_MR.shape[1]
    j_1value = I_MR[0, j + 1]
    for i in range(j + 2, n):
        if j_1value == I_MR[0, i]:
            i += 1
            continue
        else:
            return i
    return n-1


def find1(j, I_MR):
    j_1value = I_MR[0, j]
    for i in reversed(range(1, j)):
        if j_1value == I_MR[0, i]:
            i -= 1
            continue
        else:
            return i
    return 1
