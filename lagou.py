import requests
import json
import pymongo
import time

client = pymongo.MongoClient() #mongo server
jobs = client.hello.jobs #选择数据库 和 集合

#设置post请求的url
url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E6%AD%A6%E6%B1%89&needAddtionalResult=false'

headers = {
    'Accept':'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8',
    'Connection':'keep-alive',
    'Content-Length':'26',
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie':'_ga=GA1.2.1170503777.1538311454; user_trace_token=20180930204412-882150bf-c4ae-11e8-bb68-5254005c3644; LGUID=20180930204412-882154b4-c4ae-11e8-bb68-5254005c3644; _gid=GA1.2.1413214533.1538311454; hasDeliver=0; JSESSIONID=ABAAABAAAFCAAEG6B2E271F33A06B1E89E17B367792CF2B; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1538311454,1538315749; _putrc=D953495B4F3F281A123F89F2B170EADC; login=true; unick=%E6%8B%89%E5%8B%BE%E7%94%A8%E6%88%B78894; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; gate_login_token=f565b0e3a7f847ee47e99fb715b410d1ff2ab52728a6adb7c5c80ee3174cbc45; TG-TRACK-CODE=index_navigation; index_location_city=%E6%AD%A6%E6%B1%89; LGSID=20180930225330-9860228d-c4c0-11e8-a861-525400f775ce; _gat=1; SEARCH_ID=427a891354074e9ebeb58feafbe7e0c5; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1538321091; LGRID=20180930232448-f7f38c56-c4c4-11e8-a864-525400f775ce',
    'Host':'www.lagou.com',
    'Origin':'https://www.lagou.com',
    'Referer':'https://www.lagou.com/jobs/list_Python?city=%E6%AD%A6%E6%B1%89&cl=false&fromSearch=true&labelWords=&suginput=',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'X-Anit-Forge-Code':'0',
    'X-Anit-Forge-Token':'None',
    'X-Requested-With':'XMLHttpRequest'
}


for i in range(0,20):
    # 需要传递的参数
    params = {
        'first': 'false',
        'pn': '{0}'.format(str(i+1)),
        'kd': 'Python'
    }
    html = requests.post(url, data=params, headers=headers) # 返回一个response对象 html.text为str类型的json数据
    dict_data = json.loads(html.text) # 将返回的json数据解析成字典类型
    results = dict_data['content']['positionResult']['result']
    for result in results:
        job = {
            'positionName':result['positionName'],
            'workYear':result['workYear'],
            'education':result['education'],
            'companyFullName':result['companyFullName'],
            'district':result['district'],
            'salary':result['salary'],
            'companySize':result['companySize'],
            'createTime':result['createTime']
        }
        jobs.insert(job)
        time.sleep(2)
