import lxml.etree as le

with open('edu.html','r',encoding='utf-8') as f:
    html = f.read() #读取
    html_x = le.HTML(html)  # 转成XML对象
    div_x_s = html_x.xpath('//div[@class="classify_cList"]')   #得到div对象
    data_s = []   #构造数据储存对象
    for div_x in div_x_s:
        category1 = div_x.xpath('./h3/a/text()')[0]         #【0】取第一个 因为重复了很多次
        category2_s = div_x.xpath('./div/span/a/text()')

        data_s.append(  #添加到字典
            dict(
            category1 = category1,
            category2_s = category2_s
            )
        )
    for data in data_s:
        print(data.get('category1'))
        for category2 in data.get('category2_s'):
            print('   ', category2)