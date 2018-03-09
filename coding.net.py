#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests,sys
import ast,re

print "useage:python coding.net.py keyword"
host = "https://coding.net"

#############################################################关键字
keywords = sys.argv[1]
#keywords = 'baidu'
session = requests.session()
reheaders = {
    "Host":"coding.net",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language":"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding":"gzip, deflate",
    "Connection":"keep-alive",
}
#项目搜索API
searchurl = "https://coding.net/api/esearch/project?q=" + keywords + "&page=1"
#获取项目搜索结果
searchhtm = session.get(searchurl,headers=reheaders)

# if searchhtm.status_code != 200:
#     print "Requesting URL is with wrong response status."
#     exit()

# 将搜索结果转换成字典模式
resultdict = ast.literal_eval(searchhtm.text)  # .encode("utf-8")
# print resultdict
# 获取项目地址列表
data = resultdict.get('data')
inforlist = data.get('list')
# 匹配项目地址
for i in inforlist:
    project_path = i.get('project_path')
    # owner_user_home = i.get('owner_user_home')
    if project_path:
        # 匹配获取用户名及项目名。
        path = host + project_path #此项目的全路径
        print path
        reg1 = re.compile(r'/u/(.*?)/p', re.S)
        user = re.findall(reg1, project_path)
        reg2 = re.compile(r'/p/(.*?)$', re.S)
        projname = re.findall(reg2, project_path)
        # 获取单个项目提交历史。
        commithistoryurl = host + "/api/user/" + user[0] + "/project/" + projname[0] + "/git/commits/master/?page=1&pageSize=20"
        # print commithistoryurl
        commithistorydata = session.get(commithistoryurl, headers=reheaders)
        # print commithistorydata.text
        #获取历史提交ID
        reg3 = re.compile(r'commitId":"(.*?)",', re.S)
        historyCommitId = re.findall(reg3, commithistorydata.text)
        # print historyCommitId
        for j in historyCommitId:
            commitdiffurl = host + "/u/" + user[0] + "/p/" + projname[0] + "/git/commit/"+j+".diff"
            brourl = host + "/u/" + user[0] + "/p/" + projname[0] + "/git/commit/"+j+"?public=true"
            print "browerurl = "+brourl
            commitdetail = session.get(commitdiffurl, headers=reheaders)
            #print commitdetail.text
            #匹配多个关键字。 user login email jdbc password passwd pass pwd username.secretKey appid appkey smtp.100tal.com
            #(?:ip|host|sql|url|user|login|email|jdbc|password|passwd|pass|pwd|username|secretKey|appid|appkey|smtp.100tal.com)
            # 匹配任意一个。
            # 匹配内容很多行，要定位成单行。
            # 开头位置，任意内容，限定内容，任意内容，结束位置。
            reg4 = re.compile(r'^.*?(?:ip|host|sql|url|user|login|email|jdbc|password|passwd|pass|pwd|username|secretKey|appid|appkey|smtp.100tal.com).*?$', re.M)
            result = re.findall(reg4, commitdetail.text)
            for r in result:
                print r



        # for j in historyCommitId:
        #     commitdetailurl = host + "/api/user/" + user[0] + "/project/" + projname[0] + "/git/commit/" + j.encode("utf-8")+"?diff=&w="
        #     print commitdetailurl
        #     commitdetail = session.get(commithistoryurl, headers=reheaders)
        #     #内容很多
        #     print commitdetail.text
        #     #直接在上面内容中搜索关键字？？？？
        #     reg4 = re.compile(r'"path":"(.*?)",', re.S)
        #     filepath = re.findall(reg4, commitdetail.text)
        #     print filepath
        #     #剔除图片,css文件
        #     #遍历文件，剔除图片



            # for h in filepath:
            #     print h
            #     print h.__class__
            #     #具体文件提交历史
            #     #剔除图片
            #     filehistory = host + "/api/user/"+ user[0] + "/project/" + projname[0] +  "/git/commits/" + j.encode("utf-8")+ "/" + h.encode("utf-8")+ "?page=1&pageSize=20"
            #     print filehistory
            #     filedetail = session.get(filehistory, headers=reheaders)
            #     print filedetail.text
            #     reg5 = re.compile(r'commitId":"(.*?)",', re.S)
            #     filecommitId = re.findall(reg5, filedetail.text)
            #     for m in filecommitId:
            #         fileurl = host + "/u/"+ user[0] + "/p/" + projname[0]+"/git/commit/"+m + "?public=true"
            #         print fileurl

            #获取文件提交历史








# pre_par_html = bs4.BeautifulSoup(pre_res_html.text, "html.parser")
#
# # print search results counts
# links_sum = pre_par_html.select('div.sort-bar h3')
# links_sum = links_sum[0].string
# reg_num = re.compile("\w\d")
# rlt_count = int(reg_num.search(links_sum).group())
# print "The links results count is: %d" % rlt_count
#
# # get results page count
# if rlt_count % PAGE_RESULT_COUNT != 0:
#     page_count = rlt_count / PAGE_RESULT_COUNT + 1
# else:
#     page_count = rlt_coutn / PAGE_RESULT_COUNT
#
# # print linking contents in results with looping page's results
# page_num = 1    # page number of all pages
# rlt_num = 1     # result number of all results
# for page_num in range(1, page_count + 1):
#     # get html text from each page
#     res_html = requests.get("https://github.com/search?o=desc&p=" + str(page_num) + "&q=" + key_words + "&ref=searchresults&s=indexed&type=Code&utf8=%E2%9C%93")
#     par_html = bs4.BeautifulSoup(res_html.text, "html.parser")
#     project_info = par_html.select('p.title a')
#     index_info = par_html.select('p.title span > time')
#
#     page_rlt_num = 0     # result number of each page results
#     while (page_rlt_num < PAGE_RESULT_COUNT * 2) and (rlt_num <= rlt_count):
#         user_name = project_info[page_rlt_num].string
#         file_name = project_info[page_rlt_num + 1].string
#         file_url = GITHUB_HOST + project_info[page_rlt_num + 1]['href']
#         index_time = index_info[page_rlt_num / 2]['datetime']
#         print "%dth result list:" % rlt_num
#         print "\tindex time: %s" % index_time
#         print "\tusername/project: %s" % user_name
#         print "\tsuspected file name: %s" % file_name
#         print "\tsuspected file URL: %s" % file_url
#
#         page_rlt_num += 2
#         rlt_num += 1