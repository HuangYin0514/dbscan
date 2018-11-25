# -*- coding: utf-8 -*-
# @Time     : 2018/11/25 10:17
# @Author   : HuangYin
# @FileName : IMR.py
# @Software : PyCharm

import numpy as np


def initIMR(I_CR, T):
    I_MR = np.zeros((I_CR.shape[0], round(I_CR.shape[1] / T)))
    for i in range(0, I_MR.shape[1]):
        k = round(i * T)
        I_MR[0, i] = I_CR[0, k]

    return I_MR
