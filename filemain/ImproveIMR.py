# -*- coding: utf-8 -*-
# @Time     : 2018/11/25 22:32
# @Author   : HuangYin
# @FileName : ImproveIMR.py
# @Software : PyCharm

def ImproveIMR(I_MR, T_MR1, T_MR2, T):
    n = I_MR.shape[1]
    for j in range(1, n - 1):
        if T_MR2[0,j] != j * T and T_MR1[0,j] != (j + 1) * T:
            t_c = T_MR1[0, j + 1] - T_MR2[0, j] + 1
            if t_c < T:
                I_MR[0, j] = 0
        if (T_MR2[0, n-1] - T_MR1[0, n-1] + 1) < T:
            I_MR[0, n-1] = 0
    return I_MR
