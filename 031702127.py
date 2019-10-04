＃!/ usr / bin / python
＃ -*-编码：utf-8-*-
＃ \ d {11}表示十一位数字{n}表示前面的字符还需要n个； \ d表示数字
进口重
导入 json

客户= {
    '姓名'： ' '，
    '手机'： ' '，
    “地址”：[]，
}



s =  输入（' '）

op1 = s.split（r '！'）
标签= op1 [ 0 ]   ＃提取难度标识


tel = re.findall（r ' \ d {11} '，s）   ＃发现号码
tel = tel [ 0 ]   ＃将号码转换为字符串
s = re.sub（r ' \ d {11} '，' '，s）   ＃删去号码

num = re.sub（r '，。* $ '，“ ”，s）   ＃提取人名

s = re.sub（num，' '，s）   ＃删除去人名
s = re.sub（r '，'，' '，s）   ＃删除去逗号

顾客[ '姓名' ] = NUM
客户[ '手机' ] = tel

＃一级地址
导演= [ '北京'，'上海'，'天津'，'重庆' ]
如果 “自治区” 在 S：
    first = re.sub（r '自治区。* $ '，“ ”，s）   ＃提取自治区
    首先+ =  '自治区'
    s = s.replace（first，' '，1）   ＃删去自治区
ELIF  '省' 不是 在 S：
    对于直销的导演：
        如果 direc 在 s中：
            第一=目录
            打破
        其他：
            first =  “ ”   ＃该级地址为空
其他：
    first = re.sub（r '省。* $ '，“ ”，s）
    首先+ =  '省'
    s = s.replace（first，' '，1）   ＃删除去一级地址
customer [ '地址' ] .append（第一）

＃二级
两个= [ '市'，'地区'，'盟'，'自治州' ]
为 TW 在二：
    如果 tw in s：

        秒= re.sub（tw +  '。* $ '，“ ”，s）
        秒+ = tw
        s = s.replace（second，' '，1）   ＃删除去二级地址
        打破
    其他：
        秒=  “ ”

customer [ '地址' ] .append（秒）

＃三级地址
county = [ '区'，'县'，'市'，'自治县'，'旗'，'自治旗'，'林区' ]
对于 TR 在县：
    如果 tr in s：
        第三= re.sub（tr +  '。* $ '，“ ”，s）
        第三+ = tr
        s = s.replace（third，' '，1）   ＃删除去三级地址
        打破
    其他：
        第三=  “ ”

客户[ '地址' ] .append（第三）

＃四级地址
town = [ '街道'，'镇'，'乡'，'民族乡'，'苏木'，'民族苏木' ]
对于 FR 在镇：
    如果 fr in s：
        fouth = re.sub（fr +  '。* $ '，“ ”，s）
        fouth + = fr
        s = s.replace（fouth，' '，1）   ＃删除去四级地址
        打破
    其他：
        fouth =  “ ”
customer [ '地址' ] .append（fuuth）

s = s.replace（'。'，' '，1）   ＃删除去句号
＃五级地址
village = [ '街'，'路'，'村' ]
如果标签==  ' 1 '：
    第五= s
    customer [ '地址' ] .append（第五）
elif tag ==  ' 2 ' 或 ' 3 '：   ＃继续划分五级以后的地址
    为 FV 中村：
        如果 f 在 s中：
            第五= re.sub（fv +  '。* $ '，“ ”，s）
            第五+ = fv
            customer [ '地址' ] .append（第五）
            s = s.replace（fifth，' '，1）   ＃删除去五级地址
            打破
        其他：
            第五=  “ ”
    ＃六级地址
    如果 “号” 没有 在 S：
        第六=  “ ”
    其他：
        第六= re.sub（r '号。* $ '，“ ”，s）
        第六+ =  '号'
        s = s.replace（sixre，' '，1）   ＃删除去六级地址

    customer [ '地址' ] .append（第六）

    ＃七级地址
    第七= s
    customer [ '地址' ] .append（第七）

json_str = json.dumps（客户，sure_ascii = False）
打印（json_str）
