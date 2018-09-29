import requests
#设置post请求的url
url = 'https://www.douban.com/accounts/login'

#设置需要提交的参数
params = {
    'source': 'index_nav',
    'form_email': '15926488894',
    'form_password': 'hustfz23.'
}

html = requests.post(url, params)
print(html.text)

