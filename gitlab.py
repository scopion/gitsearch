# coding: UTF-8
import requests,re,sys,os



host = "https://gitlab.com"


keywords = sys.argv[1]

#keywords = 'izhikang'
session = requests.session()
reheaders = {
    "Host":"gitlab.com",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language":"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding":"gzip, deflate",
    "Connection":"keep-alive",
}
#项目搜索API
#searchurl = "https://gitlab.com/search?utf8=%E2%9C%93&snippets=&scope=projects&search=izhikang
url = host + "/search?utf8=%E2%9C%93&snippets=&scope=projects&search=" + keywords
#获取项目搜索结果
searchhtm = session.get(url,headers=reheaders)
#print searchhtm.text

# #.encode("utf-8")
# <a class="text-plain" href="/djn123djn/izhikang_online_admin"><span class="project-full-name"><span class="namespace-name">
reg1 = re.compile(r'<a class="text-plain" href="(.*?)"><span class="project-full-name">', re.M)
code = re.findall(reg1, searchhtm.text)

#<p dir="auto">爱智康在线后台代码</p>


print code
#
for i in code:
    #print i
    history = host + i.encode('utf-8')
    print history

