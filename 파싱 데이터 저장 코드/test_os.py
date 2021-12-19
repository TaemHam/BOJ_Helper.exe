import os
import requests
from bs4 import BeautifulSoup

def main():

# -----문제 번호-----

    question_number = input('문제 번호는 무엇입니까?\n').strip()

    try:
        int(question_number)
    except ValueError:
        print('잘못된 형식의 번호입니다.')
        return

    url = 'https://www.acmicpc.net/problem/' + question_number

    res = requests.get(url)
    #res.raise_for_status()
    if res.status_code == 404: 
        print("존재하지 않는 문제 번호입니다.")
        return
    
    elif res.status_code != requests.codes.ok: 
        print("페이지 로딩에 문제가 생겼습니다. [에러코드 ", res.status_code,"]", sep='')
        return
    
# ------------------------------------------------------------------------------------

    def

    directory = input('저장 디렉토리는 어디입니까?')




    with open'''

if __name__ == "__main__":
    main()