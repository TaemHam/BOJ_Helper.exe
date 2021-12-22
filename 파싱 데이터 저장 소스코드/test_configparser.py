import configparser
import tkinter
from tkinter import filedialog
from tkinter import *
import os


def create_config_folder(config_path):
    try:
        os.makedirs(config_path)
    except FileExistsError:
        return

def config_generator():
    
    config = configparser.ConfigParser()

    config['save'] = {}
    config['save']['path'] = os.path.expanduser('~\\Documents\\Github\\work')
    config['save']['py_name'] = 'main.py'
    config['save']['eg_name'] = 'i'
    config['save']['template_exist'] = '0'
    config['save']['tamplate_path'] = ''

    with open(os.path.expanduser('~\\Documents\\BOJ Helper\\config.ini'), 'w', encoding='utf-8') as config_file:
        config.write(config_file)

def config_edit():
    
    config = configparser.ConfigParser()
    config.read(os.path.expanduser('~\\Documents\\BOJ Helper\\config.ini'), encoding = 'utf-8') 

    root = Tk()
    root.title("설정")
    root.geometry("540x300+100+100")
    root.resizable(False, False)
    root.dirName = config['save']['path']

    def select_path():
        folder_path = filedialog.askdirectory(
    	initialdir = 'path', 
     	title='저장할 폴더를 선택하세요.') 
        if folder_path == '':
            return
        root.dirName = folder_path
        path_text.configure(text = root.dirName)

    def save_status(event):
        config['save']['path'] = root.dirName
#        config['save']['py_name'] = 'main.py'
#        config['save']['eg_name'] = 'i'
#        config['save']['template_exist'] = '0'
#        config['save']['tamplate_path'] = ''
        with open(os.path.expanduser('~\\Documents\\BOJ Helper\\config.ini'), 'w', encoding='utf-8') as config_file:
            config.write(config_file)
        root.destroy()
        

    path_label = Label(root, text = "경로")
    path_label.pack()

    path_text = Label(root, text = root.dirName)
    path_text.pack()

    path_btn = Button(root, text = "선택하기", command = select_path)
    path_btn.pack()

    save_btn = Label (root, text="저장", bg='grey19', fg = 'snow')
    save_btn.bind('<Button-1>', save_status)
    save_btn.pack()

    root.mainloop()

config_file_path = os.path.expanduser('~\\Documents\\BOJ Helper\\config.ini')

if not os.path.isfile(config_file_path):
    config_path = config_file_path[:-11]
    create_config_folder(config_path)
    config_generator()

config_edit()



