#!/usr/bin/env python3
# -*- coding=utf-8 -*-
from clean import del_s_field
import os
os.chdir('/root/ll')
for root, dirs, files in os.walk(os.getcwd(), topdown=False):
    for files1 in files:
        file_path = os.path.join(root, files1)
        del_s_field(file_path)

print('清理完成')