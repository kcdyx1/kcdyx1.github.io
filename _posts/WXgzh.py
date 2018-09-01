import wechatsogou
import datetime


nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
gzh_list = ['后沙', '全球技术地图', '人民日报', '战略前沿技术', 'KPMG大数据挖掘', 'AI科技评论']
ws_api = wechatsogou.WechatSogouAPI(captcha_break_time=3)
gzh_dict = {}

with open('weixintemp.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()

with open("2018-08-21-微信公众号.md", "w", encoding="utf-8") as f_w:
    for line in lines:
        f_w.write(line)


def get_gzh_xx(gzh_name):
    # 调用API获取公众号信息
    try:
        gzh_info = ws_api.get_gzh_info(gzh_name)
        gzh_dict[gzh_name] = gzh_info
        return gzh_dict
    except:
        print(gzh_name, "获取失败")


for n in gzh_list:
    results = get_gzh_xx(n)

with open("2018-08-21-微信公众号.md", "a", encoding="utf-8") as f_w:
    for k, v in results.items():
        tiaomu = (
            '- [' + k + '](' + v['profile_url'] + '){:target="_blank"}\n')
        f_w.write(tiaomu)
