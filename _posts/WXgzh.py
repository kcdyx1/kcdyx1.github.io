# !/Users/kangchen/anaconda3/bin/python
# -*- coding: utf-8 -*-
# author@康宸 find me https://github.com/kcdyx1

import os
import wechatsogou
import datetime
from gzh_dict import *
# from git import Repo

dir = "/Users/kangchen/kcdyx1.github.io"


def get_time():
    # 获取运行时间
    Time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return Time


def list_get():    # 创建公众号名称去重列表
    chuan_gzh_list = []
    for v in gzh_dict.values():
        for i in v.keys():
            if i not in chuan_gzh_list:
                chuan_gzh_list.append(i)
    print('公众号列表已生成！\n')
    return chuan_gzh_list


def ChuShiHua(shijian):
    print("微信公众号链接获取程序已启动--->")
    with open(dir + '/_posts/weixintemp.txt', 'r', encoding="utf-8") as f:
        # 读取文件头部
        lines = f.readlines()
        lines.append('\n微信公众号链接更新于：' + shijian + '\n')
    with open(dir + "/_posts/2018-08-22-微信公众号.md", "w", encoding="utf-8") as f_w:
        # 写入文件头部
        for line in lines:
            f_w.write(line)
    print('2018-08-22-微信公众号.md文件初始化完成！\n')



# 初始化搜狗微信API
ws_api = wechatsogou.WechatSogouAPI(captcha_break_time=3)


def get_gzh_xx(gzh_name):
    # 调用API获取公众号信息的函数
    gzh_info = ws_api.get_gzh_info(gzh_name)
    if gzh_info:
        return gzh_info
    else:
        print(gzh_name, "获取失败！")


def file_add_write(nr):
    # 文件追加写入内容
    with open(dir + "/_posts/2018-08-22-微信公众号.md", "a", encoding="utf-8") as f_w:
        f_w.write(nr)


def result_save(gzhlist):
    # 储存全部公众号信息
    result_dict = {}
    for n in gzhlist:
        result_dict[n] = get_gzh_xx(n)
    print('公众号链接获取完毕！\n')
    for ly_v in gzh_dict.values():
        for gzh_k, gzh_v in ly_v.items():
            ly_v[gzh_k] = result_dict[gzh_k]

    for key, value in gzh_dict.items():
        title = "\n#### " + key + '\n'
        file_add_write(title + '\n')
        for gzhk, gzhv in value.items():
            if gzhv:
                gzh_id = gzhk
                gzh_url = gzhv['profile_url']
                gzh_intro = gzhv['introduction']
                hypelink = '- [' + gzh_id + \
                    '](' + gzh_url + '){:target="_blank"}' + '\n'
                jianjie = '\t>简介：' + gzh_intro + '\n'
                file_add_write(hypelink)
                file_add_write(jianjie)
            else:
                continue
    file_add_write('\n')
    file_add_write('------\n' + '\n')
    file_add_write('欢迎推荐更多信息源 [kcdyx1@hotmail.com](mailto:kcdyx1@hotmail.com)')


def gengxin():
    all_gzh_list = list_get()
    nowTime = get_time()
    ChuShiHua(nowTime)
    result_save(all_gzh_list)
    nowTime = get_time()
    print(nowTime + '微信公众号链接已更新到文件！')
    os.system('iite')
    print(nowTime + '所有更新已经推送至github，enjoy！')
    exit()


def gitpush():
    print('开始推送最新内容到github ------> \n')
    nowTime = get_time()
    os.system('iite')
    print(nowTime + '所有更新已经推送至github，enjoy！')
    exit()


def main():
    kaishi = input(
        "你想干啥？\n------>按 1 更新微信公众号链接并推送；\n------>按 2 只推送所有更新项目;\n------>按 q 滚远点！\n你说吧：")
    if kaishi == '1':
        print("你选择了" + kaishi + '\n')
        gengxin()
    if kaishi == '2':
        print("你选择了" + kaishi + '\n')
        gitpush()
    if kaishi == 'q':
        print("再见了老铁！")
    else:
        print("\n输错啦，你个沙雕！\n重来！！！\n")
        main()


if __name__ == '__main__':
    main()
