import requests
url = "https://www.google.com"
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()                 #오류가 나면 밑의 코드들 실행 안하고 멈춤
with open("my_google.html", "w", encoding = "utf8") as f:
    f.write(res.text)

####print("응답코드 :", res.status_code)    #200이면 정상

####if res.status_code == res.codes.ok: 
    ####print("정상입니다")
####else:
    ####print("문제가 생겼습니다. [에러코드 ", res.status_code, "]")
