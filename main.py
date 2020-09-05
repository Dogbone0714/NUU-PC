import urllib2
import cookielib
import urllib
import re
import sys
'''模擬登入'''
reload(sys)
sys.setdefaultencoding("utf-8")
# 防止中文報錯
CaptchaUrl = "https://eap10.nuu.edu.tw/CommonPages/Captcha.aspx"
PostUrl = "https://eap10.nuu.edu.tw/DefaultSystemIndex.aspx?sys_id=S00"

# 驗證碼地址和post地址
cookie = cookielib.CookieJar()
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
# 將cookies繫結到一個opener cookie由cookielib自動管理
username = 'U0924046'
password = 'abc054015'

# 使用者名稱和密碼
picture = opener.open(CaptchaUrl).read()
# 用openr訪問驗證碼地址,獲取cookie
local = open('e:/image.jpg', 'wb')
local.write(picture)
local.close()
# 儲存驗證碼到本地
SecretCode = raw_input('輸入驗證碼： ')
# 開啟儲存的驗證碼圖片 輸入
postData = {
'__VIEWSTATE': 'dDwyODE2NTM0OTg7Oz6pH0TWZk5t0lupp/tlA1L rmL83g==',
'txtUserName': username,
'TextBox2': password,
'txtSecretCode': SecretCode,
'RadioButtonList1': '學生',
'Button1': '',
'lbLanguage': '',
'hidPdrs': '',
'hidsc': '',
}
# 根據抓包資訊 構造表單
headers = {
'Accept': 'text/html,application/xhtml xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Language': 'zh-CN,zh;q=0.8',
'Connection': 'keep-alive',
'Content-Type': 'application/x-www-form-urlencoded',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36',
}
# 根據抓包資訊 構造headers
data = urllib.urlencode(postData)
# 生成post資料 ?key1=value1&key2=value2的形式
request = urllib2.Request(PostUrl, data, headers)
# 構造request請求
try:
response = opener.open(request)
result = response.read().decode('gb2312')
# 由於該網頁是gb2312的編碼，所以需要解碼
print result
# 列印登入後的頁面
except urllib2.HTTPError, e:
print e.code
# 利用之前存有cookie的opener登入頁面