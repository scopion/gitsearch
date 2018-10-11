# coding: UTF-8
import requests,re,sys,os



host = "https://gitee.com"
keywords = sys.argv[1]

#keywords = 'jzb'
session = requests.session()
reheaders = {
    "Host":"gitee.com",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language":"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding":"gzip, deflate",
    "Connection":"keep-alive",
}
#项目搜索API
#searchurl = "https://coding.net/api/esearch/project?q=" + keywords + "&page=1"
#https://gitee.com/search?search=jzb.com&type=project
url = host + "/search?search=" + keywords+"&type=project"
#获取项目搜索结果
searchhtm = session.get(url,headers=reheaders)
# print searchhtm.content

#.encode("utf-8")
# <a href="/iosdevhaibian/codes/25ca1dh4t90foejusrnpx">查看代码</a>


reg2 = re.compile(r'<a href="(.*?)" target="_blank"><strong>', re.M)
projectpath = re.findall(reg2, searchhtm.text)
print projectpath
for j in projectpath:
    commithistoryurl = host + j.encode('utf-8') + "/commits/master"
    print host + j.encode('utf-8')
    commithistory = session.get(commithistoryurl, headers=reheaders)
    # print commithistory.content
    reg3 = re.compile(r'<a href="(.*?)" class="commit_short_id"', re.M)
    commiturl = re.findall(reg3, commithistory.text)
    for u in commiturl:
        commit = host + u.encode('utf-8')
        print commit
        commitdetail = session.get(commit, headers=reheaders)
        # print commitdetail.text
        #<a href="/lenny902/JZB-X8/blob/20dc58d9fa984d7515d0e3a8727e042e9b2e975f/README.md" class="ui white basic button view-file">查看文件 @
        reg4 = re.compile(r'<a href="(.*?)" class="ui white basic button', re.M)
        commitfile = re.findall(reg4, commitdetail.text)
        print commitfile
        #filecontent = session.get(host + commitfile[0].encode('utf-8'), headers=reheaders).content
        for f in commitfile:
            file = host + f.encode('utf-8')
            print file
