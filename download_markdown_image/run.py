#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re
import requests
import os

# 输入文件夹，即 简书导出的 .md 文件位置
INPUT_DIR = '/Users/zhangyunfei/Downloads/user-2044033-1572795291/'
# 输出文件夹，即 文章里的图片的下载后的存放位置
OUTPUT_DIR = '/Users/zhangyunfei/Downloads/output_images'


# fileName = "React-Native/ES-Lint-技术分享.md"


def ensure_dir_exist(dir_name):
    if not os.path.exists(dir_name):
        # print("{} 不存在，创建它。".format(dir_name))
        os.mkdir(dir_name)
    # else:
    #     print("{} 存在，无需新创建。".format(dir_name))


def start_a_file(a_markdown_file, output_dir):
    f = open(a_markdown_file)
    line = f.readline()
    i = 0
    while 1:
        line = f.readline()
        if not line:
            break
        i = i + 1
        ln = line[:-1]
        # print("[{}] [{}]".format(i, ln))
        process_line(ln, output_dir)
    f.close()
    return


def process_line(line, output_dir):
    if line == '':
        return
    img_list = re.findall(r"\!\[[^\]]*\]\((.+?)\)", line, re.S)
    for iu in img_list:
        img_url = iu.split('?')[0]
        print('[Process:]' + img_url)
        if img_url.startswith(('http://', 'https://')):
            download_image_file(img_url, output_dir)
        else:
            print("[ 不合法的 image url]:" + img_url)
    return


def download_image_file(url, output_dir):
    print(" # 准备下载")
    r = requests.get(url)
    img = r.content
    print(" # 准备写入")
    new_name = output_dir + "/" + os.path.basename(url)
    with open(new_name, 'wb') as f:
        f.write(img)
        print(" # 写入DONE")
    return


def walk_dir(dir_name):
    for root, dirs, files in os.walk(dir_name):
        relative_name = root.replace(INPUT_DIR, '')
        print('  root={}'.format(relative_name))
        ensure_dir_exist(OUTPUT_DIR + "/" + relative_name)
        for f in files:
            print('   file = {}'.format(f))
            if f.split('.')[-1] != 'md':
                continue
            a_markdown_file = os.path.join(root, f)
            # 生成图片存放的文件夹。
            dir_name = (a_markdown_file.split('/')[-1]).split('.')[0]
            this_file_output_dir = OUTPUT_DIR + '/' + relative_name + '/' + dir_name
            print('   this_file_output_dir = {}'.format(this_file_output_dir))
            ensure_dir_exist(this_file_output_dir)
            # 处理文件
            start_a_file(a_markdown_file, this_file_output_dir)


# filePath = INPUT_DIR + fileName
# print('filePath={}'.format(filePath))

ensure_dir_exist(OUTPUT_DIR)

# start_a_file(filePath)
walk_dir(INPUT_DIR)
