import wechatsogou

gzh_list = ['后沙']
ws_api = wechatsogou.WechatSogouAPI(captcha_break_time=3)
def gzh_xx(gzh_name):
    # 调用API获取公众号信息
    try:
        gzh_info = ws_api.get_gzh_info(gzh_name)
        print("获取成功！---->")
        for k, v in gzh_info.items():
            print(k, ": ", v, '\n')
        return 
    except:
        print("获取失败")
