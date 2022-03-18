#!/usr/bin/env python3
# -*- coding=utf-8 -*-
import os


def del_s_field(filename):
    try:
        thisfile = open(filename, 'r')
        thisfile_list = thisfile.readlines()
        if os.path.isfile(filename):

            # print(thisfile_list)
            if '# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！\n' in thisfile_list:
                del thisfile_list[2:7]
                thisfile.close()
                thisfile_w = open(filename, 'w')
                thisfile_w.writelines(thisfile_list)
                thisfile_w.close()
        else:
            print('这不是文本文件')
    except Exception as e:
        pass
        print(e)
