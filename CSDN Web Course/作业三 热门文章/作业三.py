import urllib.request as ur
import lxml.etree as le

url = 'https://so.csdn.net/so/search/s.do?p={page}&q={keyword}&t=&viparticle=&domain=&o=&s=&u=&l=&f='

def getResponse(url):
    req = ur.Request(
        url=url,
        headers={   #这一块放在最前面，不管什么请求 都用这个header
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
        }
    )
    response = ur.urlopen(req).read()   #没有最后这个read就是一个类对象 加了才是返回的字节
    return response

if __name__=='__main__':
    keyword = input('keyword')
    pn_start = int(input ('starting page'))
    pn_end = int(input ('ending page'))

    for page in range(pn_start,pn_end+1):   #range含头不含尾
        #访问一级页面
        response = getResponse(
            url= 'https://so.csdn.net/so/search/s.do?p={page}&q={keyword}&t=&viparticle=&domain=&o=&s=&u=&l=&f='.format(page=page,keyword=keyword)
        )
        #二级页面 博客的链接
        hrefs = le.HTML(response).xpath('//div[@class="limit_width"]/a/@href') #response本身是个字符对象，要转成lxml
        for href in hrefs:
            response_blog = getResponse(
                url = href,
            )
            title = le.HTML(response_blog).xpath('//h1[@class="title-article"]/text()')[0]  #response本身是个字符对象，要转成lxml

            filepath = ' blog/%s.html' %title
            with open(filepath,'wb') as f:
                f.write(response_blog)  #把拿到的response_blog往里面存
            print(title)

