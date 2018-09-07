import wechatsogou
import datetime

nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
# 获取运行时间

with open('weixintemp.txt', 'r', encoding="utf-8") as f:
    # 读取文件头部
    lines = f.readlines()
    lines.append('\n微信公众号链接更新于：' + nowTime + '\n')

with open("2018-08-22-微信公众号.md", "w", encoding="utf-8") as f_w:
    # 写入文件头部
    for line in lines:
        f_w.write(line)

# 创建公众号字典
gzh_dict = {'海洋': {'国防科技要闻': {}, '蓝海星智库': {}, '中科院海洋科技情报网': {}, '水下无人系统学报': {}, '海洋防务前沿': {}, '防务快讯': {}, '国防网': {},
                   '装备参考': {}, '战略前沿技术': {}, '航运信息网': {}, '智汇海洋': {}, 'DeepTech深科技': {}, '知远战略与防务研究所': {}},
            '新材料': {'材料科技在线': {}, '新材料产业': {}, '材料人': {}, 'DT新材料': {}, '材料十': {}, '宽禁带半导体技术创新联盟': {}, '新材料智库': {},
                    '材料科学与工程': {}, '前沿材料': {}, '汽车材料网': {}, '中国腐蚀与防护网': {}, '全球半导体观察': {}, '印刷电子在线': {}, '半导体智库': {}, '新材料在线': {}, '大国重器': {}},
            '先进制造': {'量子位': {}, '高端装备产业研究中心': {}, '机器之心': {}, '全天候科技': {}, '199IT互联网数据中心': {}, '环球科学ScientificAmerican': {}, '增材制造产业技术创新联盟': {}, '机器之能': {}, '智能制造': {}, '军民融合科技创新资讯平台': {}, 'DeepTech深科技': {}, '战略前沿技术': {}, '先进制造业': {}, '国际安全简报': {}, '行业报告研究院': {}, '网易智能': {}, '印刷电子在线': {}, '国防科技要闻': {}, '资本实验室': {}, '工业机器人之家': {}},
            '生物': {'生物前沿聚焦': {}, '国防科技要闻': {}, '战略前沿技术': {}, '精准医药GETG': {}, '晓月无声': {}, 'DeepTech深科技': {}, '默赛尔生物医学科技': {}, '信息安全法律评论': {}, '火石创造': {}, '中国合成生物学': {}, '药渡': {}, '全球医生组织': {}, '全球企业动态': {},
                   '生物谷': {}, 'Nature自然科研': {}, '基因农业网': {}, '新叶社': {}, '社发科技': {}, '基因组编辑': {}, '生物安全情报网': {}, '艾美仕': {}, '药明康德': {}, '生物探索': {}, '生物通': {}, '易科学': {}, '奇点网': {}, '生物360': {}, '医谷': {}, '贝壳社': {}},
            '航空航天': {'空天大视野': {}, '天地一体化信息网络': {}, '宇辰网无人机资讯': {}, '无人机网': {}, '无人机': {}, '民机战略观察': {}, '星际智汇': {}, '卫星界': {}, '航空简报': {}, '航小宇': {}, '航天纵横': {}, 'IEEE电气电子工程学会': {}, '军鹰资讯': {}, '美军事进行时': {}, '装备参考': {}, '晓月无声': {}, 'DeepTech深科技': {}, '战略前沿技术': {}, '国防科技要闻': {}, '蓝海星智库': {}, '海鹰资讯': {}, '航天防务': {}, '中国指挥与控制学会': {}},
            '大数据': {'KPMG大数据挖掘': {}, 'AI科技评论': {}, 'AI科技大本营': {}, '大数据周刊': {}, 'DT数据侠': {}, '大数据文摘': {}, '大数据实验室': {}, 'DeepTech深科技': {}, 'E安全': {}, '数可视': {}, '机器之心': {}, '数据局': {}, '数据猿': {}, 'InfoQ': {}},
            '科技战略': {'创新研究': {}, 'DeepTech深科技': {}, '防务快讯': {}, '国防科技要闻': {}, '战略前沿技术': {}, '三思派': {}, '晓月无声': {}, '蓝海星智库': {}, 'IEEE电气电子工程师学会': {},
                     '经世万方经济世界': {}, '中国信息通信研究院CAICT': {}, '中国与全球化智库': {}, '凤凰国际智库': {}, '知远战略与防务研究所': {}, '海国图智日播报': {}, '军鹰资讯': {}, '人定湖学者': {}, '星际智汇': {}, '战略与政策论坛': {}},
            '其他': {'人民日报': {}, '科技日报': {}, '牛弹琴': {}, '侠客岛': {}, '特朗普推特中文': {}, '兽楼处': {}, '包邮区': {}, '老道消息': {}, '科工力量': {}, }}

# 创建公众号名称去重列表
all_gzh_list = []
for v in gzh_dict.values():
    for i in v.keys():
        if i not in all_gzh_list:
            all_gzh_list.append(i)

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
    with open("2018-08-22-微信公众号.md", "a", encoding="utf-8") as f_w:
        f_w.write(nr)


# 储存全部公众号信息
result_dict = {}
for n in all_gzh_list:
    result_dict[n] = get_gzh_xx(n)
for ly_v in gzh_dict.values():
    for gzh_k, gzh_v in ly_v.items():
        ly_v[gzh_k] = result_dict[gzh_k]

for key, value in gzh_dict.items():
    title = "\n#### " + key + '\n'
    file_add_write(title + '\n')
    for gzhk, gzhv in value.items():
        gzh_id = gzhk
        gzh_url = gzhv['profile_url']
        gzh_intro = gzhv['introduction']
        hypelink = '- [' + gzh_id + \
            '](' + gzh_url + '){:target="_blank"}' + '\n'
        jianjie = '\t>简介：' + gzh_intro + '\n'
        file_add_write(hypelink)
        file_add_write(jianjie)

file_add_write('\n')
file_add_write('------\n' + '\n')
file_add_write('欢迎推荐更多信息源 [kcdyx1@hotmail.com](mailto:kcdyx1@hotmail.com)')
print(nowTime + '微信公众号链接已更新，enjoy！:P')
