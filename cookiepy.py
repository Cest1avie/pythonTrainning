from urllib import request,error

url = "http://www.renren.com/357714202/profile"

headers = {
    "cookie":"ick_login=635771fe-a75b-4477-a57e-d668abc6af1d; anonymid=jlzveq77-et2g4v; _de=B419A0D8D79D85BD3E8B235EB1FA0289; first_login_flag=1; ln_uact=15802777589; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; id=357714202; ver=7.0; JSESSIONID=abcwoWhCUTXBS-PcmDqxw; _ga=GA1.2.420025593.1536800791; _gid=GA1.2.743210088.1536800791; depovince=HUB; _r01_=1; jebecookies=ab370cbb-6dd4-498d-b56f-435487e41645|||||; p=4f4626c6e77798a620a2a842bebd84352; t=db49bad08bf2519ce404074c942d9a992; societyguester=db49bad08bf2519ce404074c942d9a992; jebe_key=63bb79b6-360f-4c9d-a5bd-94c6e19f111d%7Ca077590d56487a97c27a766312f84bda%7C1536839619046%7C1%7C1536839688438; xnsid=2d375a10; loginfrom=null; wp_fold=0"
}

req = request.Request(url, headers=headers)

rsp = request.urlopen(req)

html = rsp.read().decode("utf-8")


with open("html1.html", "w",encoding="utf-8") as f:
    f.write(html)