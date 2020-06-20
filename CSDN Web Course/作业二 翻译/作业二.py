import urllib.request as ur
import urllib.parse as up
import json

while True:
    word = input('请输入要翻译的中文')  # 输入的中文
    data = { 'kw':word }  # 将数据进行url编码
    data_url = up.urlencode(data)
    request = ur.Request(    # 构造request对象,添加访问的url接口与请求数据
    url='https://fanyi.baidu.com/sug',
    data=data_url.encode('utf‐8'),
    )
    response = ur.urlopen(request).read()  # 得到返回的response对象
    ret = json.loads(response)     # 将Json字符串转换成Python的字典
    translate = ret['data'][0]['v']    # 得到翻译结果
    print('翻译结果:',translate)