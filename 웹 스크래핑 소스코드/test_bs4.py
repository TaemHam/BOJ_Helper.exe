from bs4.element import NavigableString
import requests
import re
import os
from shutil import rmtree
from bs4 import BeautifulSoup

def create_folder(path):
    try:
        os.makedirs(path)
    except FileExistsError:
        return

cache_folder = os.path.expanduser('~\\Documents\\BOJ Helper\\cache')

if not os.path.isdir(cache_folder):
    create_folder(cache_folder)
else:
    rmtree(cache_folder)
    create_folder(cache_folder)

url = "https://www.acmicpc.net/problem/1463"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

question_number, question_title = soup.title.get_text().split(':')
question_number= question_number.strip()[:-1]
question_title = question_title.strip()

info1 = soup.td
info2 = info1.next_sibling
info3 = info2.next_sibling.next_sibling.next_sibling.next_sibling
info1 = info1.get_text()
info1 = info1[:info1.index('초')+1]
info2 = info2.get_text()
info3 = info3.get_text()
joined_str = '\n'.join([question_number, question_title, info1, info2, info3])
print(joined_str)

with open(os.path.expanduser('~\\Documents\\BOJ Helper\\cache\\0_'+ str(question_number) +'.html'), 'w', encoding = "utf8") as f:
    f.write(joined_str)

question = soup.find_all("div", {"class" : "problem-text"})
for i in range(len(question)):
    if question[i].get_text().strip() == '':
        question[i] = False
question_array = []
question_tag = ['problem', 'input', 'output', 'problem_limit', 'problem_sample_explain_', 'problem_hint']
for i in range(len(question)):
    if question[i] == False:
        question_array.append(False)
        continue
    question_array.append('''<head><style>*{color:#cccccc; background-color: #1E1E1E;}
    ::-webkit-scrollbar{width: 14px;}
    ::-webkit-scrollbar-track {background-color:#1e1e1e; border-color: #4f4f4f; border-width: 2px}
    ::-webkit-scrollbar-thumb {background-color:#4f4f4f;}
    ::-webkit-scrollbar-thumb:hover {background: #5e5e5e;}
    ::-webkit-scrollbar-button:start:decrement, ::-webkit-scrollbar-button:end:increment {width:16px;height:16px;background:#1e1e1e;}
    </style>
    <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
    <script type="text/javascript" id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script>
    </head>\n
    <body style=\'background-color: #1E1E1E\'>\n'''+ str(question[i])+ '\n</body>')

for i in range(1, len(question)):
    if question[i] == False:
        continue
    if i <= 4:
        with open(os.path.expanduser('~\\Documents\\BOJ Helper\\cache\\'+ str(i) + '_' + question_tag[i] +'.html'), 'w', encoding = "utf8") as f:
            f.write(question_array[i])
    elif 4 < i < len(question)-1:
        with open(os.path.expanduser('~\\Documents\\BOJ Helper\\cache\\'+ str(i) + '_' + question_tag[4] + str(i-4) +'.html'), 'w', encoding = "utf8") as f:
            f.write(question_array[i])
    else:
        with open(os.path.expanduser('~\\Documents\\BOJ Helper\\cache\\'+ str(i) + '_' + question_tag[5] +'.html'), 'w', encoding = "utf8") as f:
            f.write(question_array[i])





