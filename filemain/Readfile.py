# -*- coding: utf-8 -*-
# @Time     : 2018/11/24 21:05
# @Author   : HuangYin
# @FileName : Readfile.py
# @Software : PyCharm


# f = open("Data/000/Trajectory/20081023025304.plt")
# lines = f.readlines()
# del lines[0:5]
# f.close()

import os

import numpy as np


def readfile(file_dir="Data/000/Trajectory/"):
    lines = []
    result = np.zeros((1, 4))

    files = os.listdir(file_dir)
    # files.sort()
    # print(root)  # 当前目录路径
    # print(files)  # 当前路径下所有非目录子文件
    for file in files:
        f = open("Data/000/Trajectory/" + file)
        lines += f.readlines()
        del lines[0:6]
        old_list = []
        for line in lines:
            a = line.split(",")
            if len(a) > 3:
                old_list.append([a[0], a[1], a[-2], a[-1]])
        f.close()
    result = np.concatenate((result, np.array(old_list)))
    return result

# def listdir(path, list_name):  # 传入存储的list
#     for file in os.listdir(path):
#         file_path = os.path.join(path, file)
#         if os.path.isdir(file_path):
#             listdir(file_path, list_name)
#         else:
#             list_name.append(file_path)


if __name__ == '__main__':
    lines = readfile("Data/000/Trajectory/")
    print(lines)
