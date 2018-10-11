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
url = host + "/search?search=" + keywords+"&type=code"
#获取项目搜索结果
searchhtm = session.get(url,headers=reheaders)
#print searchhtm.content

#.encode("utf-8")

reg1 = re.compile(ur'<a href="(.*?)">[\u67e5]', re.M)
code = re.findall(reg1, searchhtm.text)

print code

for i in code:
    print i
    codeurl = host + i.encode('utf-8')
    print codeurl
    codedetail = session.get(codeurl, headers=reheaders)
    #print codedetail.text
#    <a href="/xsilen/codes/l4w13po6dug725fyra8z049/raw?blob_name=unipay_tenpay_bin_json.txt">原始数据</a>
    regname = re.compile(r'<a class=\'anchor\' name=\'(.*?)\'></a>', re.M)
    name = re.findall(regname, codedetail.text)
    print name
    for uri in name:
        oriurl = codeurl+"/raw?blob_name="+uri
        print oriurl
        oricode = session.get(oriurl, headers=reheaders)
        reg4 = re.compile(
            r'^.*?(?:ip=|host|sql|url|user|login|email|jdbc|password|passwd|pass|pwd|username|secretKey|appid|appkey|smtp.100tal.com|http|ftp|ssh|mongo|redis|hadoop|rabbitmq).*?$',
            re.M)
        result = re.findall(reg4, oricode.text)
        regip = re.compile(
            r'^.*?(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?).*?$', re.M)
        ip = re.findall(regip, oricode.text)
        for ipp in ip:
            print ipp
        for resu in result:
            print resu.encode('utf-8')

