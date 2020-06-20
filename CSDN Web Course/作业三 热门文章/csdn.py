import urllib.request as ur
import lxml.etree as le
import user_agent

keyword = input('请输入关键词:')
pn_start = int(input('起始页:'))
pn_end = int(input('终止页:'))

def getRequest(url):
    return ur.Request(
        url=url,
        headers={
            'User-Agent':user_agent.get_user_agent_pc(),
        }
    )

def getProxyOpener():
    proxy_address = ur.urlopen('http://api.ip.data5u.com/dynamic/get.html?order=d314e5e5e19b0dfd19762f98308114ba&sep=4').read().decode('utf-8').strip()
    proxy_handler = ur.ProxyHandler(
        {
            'http':proxy_address
        }
    )
    return ur.build_opener(proxy_handler)


for pn in range(pn_start,pn_end+1):

    request = getRequest(
        'https://so.csdn.net/so/search/s.do?p=%s&q=%s&t=blog&domain=&o=&s=&u=&l=&f=&rbg=0' % (pn,keyword)
    )
    try:
        response = getProxyOpener().open(request).read()
        href_s = le.HTML(response).xpath('//div[@class="limit_width"]/a/@href')
        for href in href_s:
            try:
                response_blog = getProxyOpener().open(
                    getRequest(href)
                ).read()
                title = le.HTML(response_blog).xpath('//h1[@class="title-article"]/text()')[0]
                print(title)
                with open('blog/%s.html' % title,'wb') as f:
                    f.write(response_blog)
            except Exception as e:
                print(e)
    except:pass



