import requests
from bs4 import BeautifulSoup

url = "https://www.acmicpc.net/problem/18352"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

#print(soup.title)                                           # 페이지 제목 출력
print(soup.title.get_text(), end= '\n\n')                    # 제목에서 텍스트만 뽑아 출력

#print(soup.p)                                               # soup 객체에서 처음 발견되는 element 출력
#print(soup.find(attrs = {"id" : "problem_description"}))    # id="problem_description" 인 element를 출력

question = soup.find_all("div", {"class" : "problem-text"})
print("문제", question[0].get_text().strip(), sep= '\n\n', end= '\n\n')
print("입력", question[1].get_text().strip(), sep= '\n\n', end= '\n\n')
print("출력", question[2].get_text().strip(), sep= '\n\n', end= '\n\n')

limit1 = soup.td
print("시간 제한은 " + limit1.get_text().strip() + " 입니다.", end= '\n\n')
limit2 = limit1.next_sibling
print("메모리 제한은 " + limit2.get_text().strip() + " 입니다.", end = '\n\n')




