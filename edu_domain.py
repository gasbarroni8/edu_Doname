import requests
from lxml import etree


for i in range(1,40):
    for x in range(1,5):
        try:
            url='http://college.gaokao.com/schlist/a{0}/p{1}/'.format(i,x)
            header={
                'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
            }
            for y in range(1,35):
                res = requests.get(url=url,headers=header).text
                try:
                    web = etree.HTML(res).xpath("/html/body/div[5]/div[5]/div[1]/dl[{}]/dd/ul/li[6]/text()".format(y))[0]
                    prin = str(etree.HTML(res).xpath("//*[@id='wrapper']/div[4]/mark/text()")[0])+'.txt'
                    with open(prin,"a") as file:
                        file.writelines(web[5:]+'\n')
                        print(web[5:])
                except IndexError:
                    pass
        except IndexError:
            pass