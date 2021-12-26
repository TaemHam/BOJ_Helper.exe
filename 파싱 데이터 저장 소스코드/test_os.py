import os
import requests
from bs4 import BeautifulSoup

def main():

# ----------문제 번호----------

    question_number = input('\n문제 번호를 입력해 주십시오.\n').strip()

    try:
        int(question_number)
    except ValueError:
        print('\n잘못된 형식의 번호입니다.')
        return 'e'
        
    url = 'https://www.acmicpc.net/problem/' + question_number

    res = requests.get(url)
    #res.raise_for_status()
    if res.status_code == 404: 
        print("\n입력하신 번호의 문제는 존재하지 않습니다.")
        return 'e'
    
    elif res.status_code != requests.codes.ok: 
        print("\n페이지 로딩에 문제가 생겼습니다. [에러코드 ", res.status_code,"]", sep='')
        return 'e'
    
    print('\n문제를 찾았습니다!')
    
# ----------저장 경로----------

    def create_folder(directory):
        try:
            if not os.path.exists(directory):
                os.makedirs(directory)
                return
        except OSError:
            print ('\n경로를 설정하는 데 문제가 생겼습니다.\n입력하신 경로는' +  directory + '입니다.')
            return 'e'
 
    folder_path = input('\n저장경로를 입력해 주십시오.\n내 문서 폴더를 이용하시려면, \\문서 로 시작되는 경로를 입력하여 주십시오.\n')
    folder_path.rstrip('\\')
    if folder_path[:3] == '\\문서':
        folder_path = os.path.expanduser(
            '~\\Documents'
            ) + folder_path[3:]

    ask_add_folder = input('\n경로 가장 끝에 추가할 폴더 이름을 입력해 주십시오.\n문제 번호라면 \\번호 를, 필요 없다면 빈 공백을 입력해 주십시오.\n')
    if ask_add_folder:
        if ask_add_folder == '\\번호':
            folder_path += '\\' + question_number
        else:
            folder_path += ask_add_folder

    if create_folder(folder_path) == 'e':
        return 'e'

    file_path = folder_path + '\\main.py'

    with open(file_path, 'w', encoding = 'utf-8') as f:
        f.write('')

    print('\n' + folder_path + ' 경로에 파일 생성이 완료되었습니다. 즐거운 코딩 되십시오.')

if __name__ == "__main__":
    if main() == 'e':
        print('\n 에러가 발생하여 프로그램을 종료합니다.')