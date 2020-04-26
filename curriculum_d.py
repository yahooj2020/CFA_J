import requests
from lxml import etree
import os

def get_one_page(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre'
    }
    response = requests.get(url,headers=headers)
    html =response.text
    return html

#解析pdf文件的下载地址 迭代器,可以遍历
def parse_one_page(html):
    selector=etree.HTML(html)
    title = selector.xpath('//*[@id="main"]/article/section/div/div/ul/li/a/text()')
    links = selector.xpath('//*[@id="main"]/article/section/div/div/ul/li/a/@href')
    for i1,i2 in zip(links,title) :
        # print(len(i1),len(i2))



        response = requests.get("https://www.cfainstitute.org/"+i1)
        if response.status_code == 200:
            l_path = os.getcwd()
            with open("{0}.pdf".format(i2)) as f:

                f.write(response.content)
                f.close()
        else:
            pass






if __name__ == "__main__":
    url = 'https://www.cfainstitute.org/en/programs/investment-foundations/curriculum/download'
    html = get_one_page(url)
    parse_one_page(html)
    link = parse_one_page(html)

    print("下载完成")