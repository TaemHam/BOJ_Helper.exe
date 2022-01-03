import configparser                                                         # 설정 파일 저장
import tkinter as tk                                                        # GUI 구현
import tkinter.font as tkFont
from tkinter import filedialog
from tkinter import *
import os
import sys
from bs4.element import NavigableString                                     # 웹크롤링
from bs4 import BeautifulSoup
import requests
import re
import pystray
from pystray import MenuItem as item                                        # 시스템 트레이에 최소화                               
from PIL import Image
from shutil import rmtree                                                   # 폴더 지우기
from cefpython3 import cefpython as cef                                     # HTML 불러오기
from pynput import keyboard                                                 # 핫키
                                                                            # + exe 실행 파일을 만들기 위해 pyinstaller 설치
config = configparser.ConfigParser()


def create_folder(path):
    try:
        os.makedirs(path)
    except FileExistsError:
        return

def config_generator():

    config['save'] = {}
    config['save']['path'] = os.path.expanduser('~/Documents/BOJ Helper')
    config['save']['py_name'] = 'main.py'
    config['save']['eg_exist'] = '0'
    config['save']['eg_name'] = 'i'
    config['save']['temp_exist'] = '0'
    config['save']['temp_path'] = os.path.expanduser('~/template.py')

    with open(os.path.expanduser('~\\Documents\\BOJ Helper\\config.ini'), 'w', encoding='utf-8') as config_file:
        config.write(config_file)


def main():

# -------------------------------------------기본 세팅------------------------------------------

    def start_move(event):
        global grip_x, grip_y
        grip_x = event.x
        grip_y = event.y

    def stop_move(event):
        global grip_x, grip_y
        grip_x = None
        grip_y = None

    def do_move(event):
        global grip_x, grip_y
        deltax = event.x - grip_x
        deltay = event.y - grip_y
        x = event.widget.master.winfo_x() + deltax
        y = event.widget.master.winfo_y() + deltay
        event.widget.master.geometry(f"+{x}+{y}")
    
    def config_button_on_enter(event):
        event.widget['bg'] = '#282828'

    def config_button_on_leave(event):
        event.widget['bg'] = bg_default

    def minim_on_enter(event):
        event.widget['bg'] = '#505050'

    def minim_on_leave(event):
        event.widget['bg'] = '#3C3C3C'

    def close_on_enter(event):
        event.widget['bg'] = '#D71526'

    def close_on_leave(event):
        event.widget['bg'] = '#3C3C3C'

    def close_window(event):
        root.destroy()
        cef.Shutdown()

    def close_tray_icon(icon, item):
        icon.stop()
        root.destroy()
        cef.Shutdown()

    def show_window(icon, item):
        icon.stop()
        root.after(0, root.deiconify())

    def hide_window(event):
        root.withdraw()
        icon.run()

    config.read(os.path.expanduser('~\\Documents\\BOJ Helper\\config.ini'), encoding = 'utf-8') 

    root = Tk()
    root.title("설정")
    app_width = 336
    app_height = 620
    root.geometry(f'{app_width}x{app_height}-{0}-{40}')
    root.configure(bg= '#1E1E1E', relief = 'solid', bd = 1, takefocus= True)
    root.resizable(False, False)
    root.attributes("-topmost", True)
    root.overrideredirect(True)

    icon_image= Image.open(os.path.expanduser('~\\Documents\\BOJ Helper\\favicon.ico'))
    icon_menu= pystray.Menu(item('Show', show_window, default= True), item('Quit', close_tray_icon))
    icon= pystray.Icon('BOJ Helper', icon_image, "BOJ Helper", icon_menu)

    frame_top = Frame(root, relief= 'flat', height= 30, bg= '#3c3c3c')
    frame_top.bind("<ButtonPress-1>", start_move)
    frame_top.bind("<ButtonRelease-1>", stop_move)
    frame_top.bind("<B1-Motion>", do_move) 
    frame_top.pack(fill= 'x')
    frame_top.propagate(False)

    button_close = Label(frame_top, text='\u26CC', font= tkFont.Font(size= 10), padx= 6, relief= 'flat', bg= '#3C3C3C', fg= '#C7C7C7')
    button_close.bind("<ButtonRelease-1>", close_window)
    button_close.bind("<Enter>", close_on_enter)
    button_close.bind("<Leave>", close_on_leave)
    button_close.pack(side= 'right', fill= 'y')

    button_minim = Label(frame_top, text='\u2015', font= tkFont.Font(size= 12), padx= 7, relief= 'flat', bg= '#3C3C3C', fg= '#C7C7C7')
    button_minim.bind("<ButtonRelease-1>", hide_window)
    button_minim.bind("<Enter>", minim_on_enter)
    button_minim.bind("<Leave>", minim_on_leave)
    button_minim.pack(side= 'right', fill= 'y')

    font_default = tkFont.Font(family="Consolas", size= 11)
    font_problem_button1= tkFont.Font(size= 10)
    font_problem_button2= tkFont.Font(size= 20)
    font_problem_info1= tkFont.Font(family= 'Malgun Gothic', size= 13, weight= 'bold')
    font_problem_info2= tkFont.Font(family= 'Malgun Gothic', size= 13)
    font_problem_title = tkFont.Font(family= 'Malgun Gothic', size= 20, weight= 'bold')
    bg_default = '#1E1E1E'
    font_white = '#d4d4d4'
    font_turq = '#9cdcfe'
    font_yellow = '#dcdcaa'
    font_blue = '#569cd6'
    font_lime = '#b5ce9b'
    font_orange = '#ce9178'
    font_green = '#4ec9b0'
    font_pink = '#c586c0'
    font_num1 = '#858585'
    font_num2 = '#c6c6c6'
    font_term1 = '#cccccc'
    font_term2 = '#f5f543'


# --------------------------------------------프레임--------------------------------------------

    label_top_line = Label(root, font= tkFont.Font(family= 'Malgun Gothic', size= 10), text= 'BOJ_Helper.exe > main.py', bg= bg_default, fg= '#AAAAAA')
    label_top_line.pack(anchor= 'w')
    frame_top_line = Frame(root, bg= '#111111', height= 1)
    frame_top_line.pack(fill= 'x')
    frame_top_line = Frame(root, bg= '#151515', height= 1)
    frame_top_line.pack(fill= 'x')
    frame_top_line = Frame(root, bg= '#181818', height= 1)
    frame_top_line.pack(fill= 'x')
    frame_top_line = Frame(root, bg= '#1A1A1A', height= 1)
    frame_top_line.pack(fill= 'x')

    line_1 = Frame(root, bg= bg_default, height= 20)
    line_1.pack(fill = 'x')
    line_1.propagate(False)
    line_1_label = Label(line_1, font= font_default, text= '', bg= bg_default, fg= font_num1)
    line_1_label.pack(side= 'left')
    
    frame_line_2_top= Frame(root, relief= 'flat', height= 2, width= app_width, bg= bg_default)
    frame_line_2_top.pack(fill = 'x')
    line_2 = Frame(root, bg= bg_default, height= 16)
    line_2.pack(fill = 'x')
    line_2.propagate(False)
    line_2_label = Label(line_2, font= font_default, text= '    ', bg= bg_default, fg= font_num1)
    line_2_label.pack(side= 'left')
    frame_line_2_bot= Frame(root, relief= 'flat', height= 2, width= app_width, bg= bg_default)
    frame_line_2_bot.pack(fill = 'x')
    
    line_3 = Frame(root, bg= bg_default, height= 20)
    line_3.pack(fill = 'x')
    line_3.propagate(False)
    line_3_label = Label(line_3, font= font_default, text= '    ', bg= bg_default, fg= font_num1)
    line_3_label.pack(side= 'left')
    
    line_4 = Frame(root, bg= bg_default, height= 20)
    line_4.pack(fill = 'x')
    line_4.propagate(False)
    line_4_label = Label(line_4, font= font_default, text= '    ', bg= bg_default, fg= font_num1)
    line_4_label.pack(side= 'left')
    
    line_5 = Frame(root, bg= bg_default, height= 20)
    line_5.pack(fill = 'x')
    line_5.propagate(False)
    line_5_label = Label(line_5, font= font_default, text= '    ', bg= bg_default, fg= font_num1)
    line_5_label.pack(side= 'left')

    line_6 = Frame(root, bg= bg_default, height= 20)
    line_6.pack(fill = 'x')
    line_6.propagate(False)
    line_6_label = Label(line_6, font= font_default, text= '    ', bg= bg_default, fg= font_num1)
    line_6_label.pack(side= 'left')

    frame_line_7_top= Frame(root, relief= 'flat', height= 2, width= app_width, bg= bg_default)
    frame_line_7_top.pack(fill = 'x')
    line_7 = Frame(root, bg= bg_default, height= 16)
    line_7.pack(fill = 'x')
    line_7.propagate(False)
    line_7_label = Label(line_7, font= font_default, text= '    ', bg= bg_default, fg= font_num1)
    line_7_label.pack(side= 'left')
    frame_line_7_bot= Frame(root, relief= 'flat', height= 2, width= app_width, bg= bg_default)
    frame_line_7_bot.pack(fill = 'x')

    line_8 = Frame(root, bg= bg_default, height= 20)
    line_8.pack(fill = 'x')
    line_8.propagate(False)
    line_8_label = Label(line_8, font= font_default, text= '    ', bg= bg_default, fg= font_num1)
    line_8_label.pack(side= 'left')

    frame_eg_name_hide= Frame(root, relief= 'flat', height= 20, width= app_width, bg= bg_default)
    frame_eg_name_hide.propagate(False)
    if config['save']['eg_exist'] == '1':
        frame_eg_name_hide.pack(fill = 'x')

    frame_line_9_top= Frame(frame_eg_name_hide, relief= 'flat', height= 2, width= app_width, bg= bg_default)
    frame_line_9_top.pack(fill = 'x')
    line_9 = Frame(frame_eg_name_hide, bg= bg_default, height= 16)
    line_9.pack(fill = 'x')
    line_9.propagate(False)
    line_9_label = Label(line_9, font= font_default, text= '    ', bg= bg_default, fg= font_num1)
    line_9_label.pack(side= 'left')
    frame_line_9_bot= Frame(frame_eg_name_hide, relief= 'flat', height= 2, width= app_width, bg= bg_default)
    frame_line_9_bot.pack(fill = 'x')


    line_10 = Frame(root, bg= bg_default, height= 20)
    line_10.pack(fill = 'x')
    line_10.propagate(False)
    line_10_label = Label(line_10, font= font_default, text= '    ', bg= bg_default, fg= font_num1)
    line_10_label.pack(side= 'left')
    
    frame_temp_path_hide= Frame(root, relief= 'flat', height= 40, width= app_width, bg= bg_default)
    frame_temp_path_hide.propagate(False)
    if config['save']['temp_exist'] == '1':
        frame_temp_path_hide.pack(fill = 'x')

    line_11 = Frame(frame_temp_path_hide, bg= bg_default, height= 20)
    line_11.pack(fill = 'x')
    line_11.propagate(False)
    line_11_label = Label(line_11, font= font_default, text= '    ', bg= bg_default, fg= font_num1)
    line_11_label.pack(side= 'left')
    line_12 = Frame(frame_temp_path_hide, bg= bg_default, height= 20)
    line_12.pack(fill = 'x')
    line_12.propagate(False)
    line_12_label = Label(line_12, font= font_default, text= '    ', bg= bg_default, fg= font_num1)
    line_12_label.pack(side= 'left')
    line_13 = Frame(root, bg= bg_default, height= 20)
    line_13.pack(fill = 'x')
    line_13.propagate(False)
    line_13_label = Label(line_13, font= font_default, text= '    ', bg= bg_default, fg= font_num1)
    line_13_label.pack(side= 'left')
    line_14 = Frame(root, bg= bg_default, height= 20)
    line_14.pack(fill = 'x')
    line_14.propagate(False)
    line_14_label = Label(line_14, font= font_default, text= '    ', bg= bg_default, fg= font_num1)
    line_14_label.pack(side= 'left')
    line_15 = Frame(root, bg= bg_default, height= 20)
    line_15.pack(fill = 'x')

    line_15.propagate(False)
    line_15_label = Label(line_15, font= font_default, text= '', bg= bg_default, fg= font_num1)
    line_15_label.pack(side= 'left')
    line_16 = Frame(root, bg= bg_default, height= 20)
    line_16.pack(fill = 'x')
    line_16.propagate(False)
    line_16_label = Label(line_16, font= font_default, text= '    ', bg= bg_default, fg= font_num1)
    line_16_label.pack(side= 'left')
    line_17 = Frame(root, bg= bg_default, height= 20)
    line_17.pack(fill = 'x')
    line_17.propagate(False)
    line_17_label = Label(line_17, font= font_default, text= '', bg= bg_default, fg= font_num1)
    line_17_label.pack(side= 'left')
    line_18 = Frame(root, bg= bg_default, height= 20)
    line_18.pack(fill = 'x')
    line_18.propagate(False)
    line_18_label = Label(line_18, font= font_default, text= '    ', bg= bg_default, fg= font_num1)
    line_18_label.pack(side= 'left')
    
        
    # ---------------------------------------------------------------------------------------------

    frame_label_stt_line = Frame(line_1, bg= bg_default, height= 20, width = 32)
    frame_label_stt_line.propagate(False)
    frame_label_stt_line.pack(side= 'left')
    label_def_line = Label(frame_label_stt_line, font= font_default, text= 'def ', bg= bg_default, fg= font_blue)
    label_def_line.pack(side= 'left')
    frame_label_stt_line = Frame(line_1, bg= bg_default, height= 20, width = 72)
    frame_label_stt_line.propagate(False)
    frame_label_stt_line.pack(side= 'left')
    label_def_line = Label(frame_label_stt_line, font= font_default, text= 'makeFile ', bg= bg_default, fg= font_yellow)
    label_def_line.pack(side= 'left')
    frame_label_stt_line = Frame(line_1, bg= bg_default, height= 20, width = 24)
    frame_label_stt_line.propagate(False)
    frame_label_stt_line.pack(side= 'left')
    label_def_line = Label(frame_label_stt_line, font= font_default, text= '():', bg= bg_default, fg= font_white)
    label_def_line.pack(side= 'left')


# -------------------------------------------문제 번호------------------------------------------

    def entry_q_num_clear(event):
        if not event.widget.dirName:
            event.widget.delete(0, 'end')
            event.widget.dirName += '1'
        frame_line_2_top['bg'] = '#282828'
        frame_line_2_bot['bg'] = '#282828'
        line_2_label['fg'] = font_num2
        event.widget['bg'] = bg_default

    def entry_q_num_focus_out(event):
        if entry_q_num.get() == '':
            entry_q_num['bg'] = '#36393d'
        frame_line_2_top['bg'] = bg_default
        frame_line_2_bot['bg'] = bg_default
        line_2_label['fg'] = font_num1

    frame_label_q_num= Frame(line_2, bg= bg_default, height= 20, width = 112)
    frame_label_q_num.propagate(False)
    frame_label_q_num.pack(side= 'left')
    label_q_num = Label(frame_label_q_num, font= font_default, text= 'questionNumber', bg= bg_default, fg= font_turq)
    label_q_num.pack(side= 'left')

    frame_label_q_num_lb= Frame(line_2, bg= bg_default, bd= 1, height= 20, width = 8)
    frame_label_q_num_lb.propagate(False)
    frame_label_q_num_lb.pack(side= 'left')
    label_q_num = Label(frame_label_q_num_lb, font= font_default, text= '=', bg= bg_default, fg= font_white)
    label_q_num.pack(side= 'left')

    frame_label_q_num= Frame(line_2, bg= bg_default, height= 20, width = 8)
    frame_label_q_num.propagate(False)
    frame_label_q_num.pack(side= 'right')
    label_q_num = Label(frame_label_q_num, font= font_default, text= ')', bg= bg_default, fg= font_white)
    label_q_num.pack(side= 'left')

    frame_entry_q_num= Frame(line_2, bg= bg_default, height= 20, width = 56)
    frame_entry_q_num.propagate(False)
    frame_entry_q_num.pack(side= 'right')
    entry_q_num = Entry(frame_entry_q_num, font= font_default, bd= 0, bg= '#36393d',
                        fg= font_lime, insertbackground= font_num2, justify = 'center')
    entry_q_num.dirName = ''
    entry_q_num.bind('<FocusIn>', entry_q_num_clear)
    entry_q_num.bind('<FocusOut>', entry_q_num_focus_out)
    entry_q_num.pack(expand= True)
    frame_label_q_num= Frame(line_2, bg= bg_default, height= 20, width = 8)
    frame_label_q_num.propagate(False)
    frame_label_q_num.pack(side= 'right')
    label_q_num = Label(frame_label_q_num, font= font_default, text= '(', bg= bg_default, fg= font_white)
    label_q_num.pack(side= 'left')


#--------------------------------------------저장 경로------------------------------------------

    def select_path(event):
        folder_path = filedialog.askdirectory(
    	initialdir = 'path', 
     	title='저장할 폴더를 선택하세요.')
        if folder_path == '':
            return
        root.dirName = folder_path
        show_folder_path = '\'~' + root.dirName[root.dirName.find('/', 10):] + '\''
        line_5['height'] = len(show_folder_path)//28 * 20 + 20
        frame_save_path_dir['height'] = len(show_folder_path)//28 * 20 + 20
        path_text.configure(text = show_folder_path)

    frame_save_path = Frame(line_4, bg= bg_default, height= 20, width = 64)
    frame_save_path.propagate(False)
    frame_save_path.pack(side= 'left')
    label_save_path = Label(frame_save_path, font= font_default, text = 'savePath', bg= bg_default, fg= font_turq)
    label_save_path.pack(side= 'left')
    frame_save_path = Frame(line_4, bg= bg_default, height= 20, width = 16)
    frame_save_path.propagate(False)
    frame_save_path.pack(side= 'left')
    label_save_path = Label(frame_save_path, font= font_default, text= '= ', bg= bg_default, fg= font_white)
    label_save_path.pack(side= 'left')


    frame_save_path = Frame(line_4, bg= bg_default, height= 20, width = 16)
    frame_save_path.propagate(False)
    frame_save_path.pack(side= 'left')
    label_save_path = Label(frame_save_path, font= font_default, text= 'os', bg= bg_default, fg= font_green)
    label_save_path.pack(side= 'left')
    frame_save_path = Frame(line_4, bg= bg_default, height= 20, width = 8)
    frame_save_path.propagate(False)
    frame_save_path.pack(side= 'left')
    label_save_path = Label(frame_save_path, font= font_default, text= '.', bg= bg_default, fg= font_white)
    label_save_path.pack(side= 'left')
    frame_save_path = Frame(line_4, bg= bg_default, height= 20, width = 32)
    frame_save_path.propagate(False)
    frame_save_path.pack(side= 'left')
    label_save_path = Label(frame_save_path, font= font_default, text= 'path', bg= bg_default, fg= font_turq)
    label_save_path.pack(side= 'left')
    frame_save_path = Frame(line_4, bg= bg_default, height= 20, width = 8)
    frame_save_path.propagate(False)
    frame_save_path.pack(side= 'left')
    label_save_path = Label(frame_save_path, font= font_default, text= '.', bg= bg_default, fg= font_white)
    label_save_path.pack(side= 'left')
    frame_save_path = Frame(line_4, bg= bg_default, height= 20, width = 80)
    frame_save_path.propagate(False)
    frame_save_path.pack(side= 'left')
    label_save_path = Label(frame_save_path, font= font_default, text= 'expanduser', bg= bg_default, fg= font_yellow)
    label_save_path.pack(side= 'left')
    frame_save_path = Frame(line_4, bg= bg_default, height= 20, width = 8)
    frame_save_path.propagate(False)
    frame_save_path.pack(side= 'left')
    label_save_path = Label(frame_save_path, font= font_default, text= '(', bg= bg_default, fg= font_white)
    label_save_path.pack(side= 'left')

    frame_save_path_search_margin = Frame(line_4, bg= bg_default, height= 20, width= 8)
    frame_save_path_search_margin.propagate(False)
    frame_save_path_search_margin.pack(side= 'right')
    frame_save_path_search = Frame(line_4, bg= bg_default, height= 20, width= 56)
    frame_save_path_search.propagate(False)
    frame_save_path_search.pack(side= 'right')
    save_path_search = Label(frame_save_path_search, font= font_default, text = '\U0001f50d', pady= 4, relief= 'flat', bg= bg_default, fg = 'snow')
    save_path_search.bind('<ButtonRelease-1>', select_path)
    save_path_search.bind("<Enter>", config_button_on_enter)
    save_path_search.bind("<Leave>", config_button_on_leave)
    save_path_search.pack(fill= 'both', expand= True) 

    root.dirName = config['save']['path']
    show_folder_path = '\'~' + root.dirName[root.dirName.find('/', 10):] + '\''
    line_5['height'] = len(show_folder_path)//28 * 20 + 20
    frame_save_path_dir = Frame(line_5, bg= bg_default, height= len(show_folder_path)//28 * 20 + 20, width = 224)
    frame_save_path_dir.propagate(False)
    frame_save_path_dir.pack(side= 'left')
    path_text = Label(frame_save_path_dir, font= font_default, text = show_folder_path, bg= bg_default, fg= font_orange, wraplength= 224, justify= 'left')
    path_text.pack(anchor= 'w')

    frame_save_path = Frame(line_6, bg= bg_default, height= 20, width = 8)
    frame_save_path.propagate(False)
    frame_save_path.pack(side= 'left')
    label_save_path = Label(frame_save_path, font= font_default, text= ')', bg= bg_default, fg= font_white)
    label_save_path.pack(side= 'left')


# -------------------------------------------파일 이름------------------------------------------

    def entry_py_name_clear(event):
        if not event.widget.dirName:
            event.widget.delete(0, 'end')
            event.widget.dirName += '1'
        frame_line_7_top['bg'] = '#282828'
        frame_line_7_bot['bg'] = '#282828'
        frame_entry_py_name['width'] = 240
        entry_py_name.pack(fill= 'both')
        entry_py_name['justify'] = 'right'
        event.widget['bg'] = bg_default
        event.widget['fg'] = font_orange

    def entry_py_name_focus_out(event):
        py_name_text = entry_py_name.get()
        if  py_name_text == '':
            entry_py_name.dirName = ''
            entry_py_name.insert(0, config['save']['py_name'])
        if len(py_name_text) < 7:
            frame_entry_py_name['width'] = 56
            entry_py_name['justify'] = 'center'
        else:
            frame_entry_py_name['width'] = len(py_name_text) * 8 + 2
        entry_py_name.pack(fill= 'both')
        frame_line_7_top['bg'] = bg_default
        frame_line_7_bot['bg'] = bg_default

    frame_label_py_name= Frame(line_7, bg= bg_default, height= 20, width = 64)
    frame_label_py_name.propagate(False)
    frame_label_py_name.pack(side= 'left')
    label_py_name = Label(frame_label_py_name, font= font_default, text= 'saveName', bg= bg_default, fg= font_turq)
    label_py_name.pack(side= 'left')

    frame_label_py_name_lb= Frame(line_7, bg= bg_default, bd= 1, height= 20, width = 16)
    frame_label_py_name_lb.propagate(False)
    frame_label_py_name_lb.pack(side= 'left')
    label_py_name = Label(frame_label_py_name_lb, font= font_default, text= '= ', bg= bg_default, fg= font_white)
    label_py_name.pack(side= 'left')

    frame_label_py_name_lb= Frame(line_7, bg= bg_default, bd= 1, height= 20, width = 8)
    frame_label_py_name_lb.propagate(False)
    frame_label_py_name_lb.pack(side= 'right')
    label_py_name = Label(frame_label_py_name_lb, font= font_default, text= '\'', bg= bg_default, fg= font_orange)
    label_py_name.pack(side= 'left')

    if len(config['save']['py_name']) < 7:
        frame_entry_py_name_width= 56
    else:
        frame_entry_py_name_width= len(config['save']['py_name']) * 8 + 2
    frame_entry_py_name= Frame(line_7, bg= bg_default, height= 20, width = frame_entry_py_name_width)
    frame_entry_py_name.propagate(False)
    frame_entry_py_name.pack(side= 'right')
    entry_py_name = Entry(frame_entry_py_name, font= font_default, bd= 0, bg= '#36393d', fg= '#828589', insertbackground= font_num2, justify= 'center')
    entry_py_name.dirName = ''
    entry_py_name.insert(0, config['save']['py_name'])
    entry_py_name.bind('<FocusIn>', entry_py_name_clear)
    entry_py_name.bind('<FocusOut>', entry_py_name_focus_out)
    entry_py_name.pack(side= 'right')

    frame_label_py_name_lb= Frame(line_7, bg= bg_default, bd= 1, height= 20, width = 8)
    frame_label_py_name_lb.propagate(False)
    frame_label_py_name_lb.pack(side= 'right')
    label_py_name = Label(frame_label_py_name_lb, font= font_default, text= '\'', bg= bg_default, fg= font_orange)
    label_py_name.pack(side= 'left')
    

#--------------------------------------------예제 파일------------------------------------------

    def entry_eg_name_clear(event):
        if not event.widget.dirName:
            event.widget.delete(0, 'end')
            event.widget.dirName += '1'
        frame_line_9_top['bg'] = '#282828'
        frame_line_9_bot['bg'] = '#282828'
        frame_entry_eg_name['width'] = 240
        entry_eg_name.pack(fill= 'both')
        entry_eg_name['justify'] = 'right'
        event.widget['bg'] = bg_default
        event.widget['fg'] = font_orange

    def entry_eg_name_focus_out(event):
        eg_name_text = entry_eg_name.get()
        if  eg_name_text== '':
            entry_eg_name.dirName = ''
            entry_eg_name.insert(0, config['save']['eg_name'])
        if len(eg_name_text) < 7:
            frame_entry_eg_name['width'] = 56
            entry_eg_name['justify'] = 'center'
        else:
            frame_entry_eg_name['width'] = len(eg_name_text) * 8 + 2
        entry_eg_name.pack(fill= 'both')
        frame_line_9_top['bg'] = bg_default
        frame_line_9_bot['bg'] = bg_default

    def eg_exist_toggle_frame(event):
        frame_eg_name_hide.pack_forget() if frame_eg_name_hide.winfo_manager() else frame_eg_name_hide.pack(after= line_8)
        label_eg_name_bool.configure(text = 'True') if frame_eg_name_hide.winfo_manager() else label_eg_name_bool.configure(text = 'False')

    frame_label_eg_name= Frame(line_8, bg= bg_default, height= 20, width = 104)
    frame_label_eg_name.propagate(False)
    frame_label_eg_name.pack(side= 'left')
    label_eg_name = Label(frame_label_eg_name, font= font_default, text= 'makeInputFile', bg= bg_default, fg= font_turq)
    label_eg_name.bind('<ButtonRelease-1>', eg_exist_toggle_frame)
    label_eg_name.pack(side= 'left')
    frame_label_eg_name= Frame(line_8, bg= bg_default, height= 20, width = 16)
    frame_label_eg_name.propagate(False)
    frame_label_eg_name.pack(side= 'left')
    label_eg_name = Label(frame_label_eg_name, font= font_default, text= '= ', bg= bg_default, fg= font_white)
    label_eg_name.bind('<ButtonRelease-1>', eg_exist_toggle_frame)
    label_eg_name.pack(side= 'left')
    frame_label_eg_name= Frame(line_8, bg= bg_default, height= 20, width = 8)
    frame_label_eg_name.propagate(False)
    frame_label_eg_name.pack(side= 'right')
    label_eg_name = Label(frame_label_eg_name, font= font_default, text= ')', bg= bg_default, fg= font_white)
    label_eg_name.bind('<ButtonRelease-1>', eg_exist_toggle_frame)
    label_eg_name.pack(side= 'left')


    frame_label_eg_name= Frame(line_8, bg= bg_default, height= 20, width = 56)
    frame_label_eg_name.propagate(False)
    frame_label_eg_name.pack(side= 'right')
    if config['save']['eg_exist'] == '1':
        eg_text_bool= 'True'
    else:
        eg_text_bool= 'False'
    label_eg_name_bool = Label(frame_label_eg_name, font= font_default, text= eg_text_bool, bg= bg_default, fg= font_blue, width= 40, takefocus= True)
    label_eg_name_bool.bind('<ButtonRelease-1>', eg_exist_toggle_frame)
    label_eg_name_bool.bind('<Return>', eg_exist_toggle_frame)
    label_eg_name_bool.bind("<Enter>", config_button_on_enter)
    label_eg_name_bool.bind("<Leave>", config_button_on_leave)
    label_eg_name_bool.bind("<FocusIn>", config_button_on_enter)
    label_eg_name_bool.bind("<FocusOut>", config_button_on_leave)
    label_eg_name_bool.pack(side= 'top')

    frame_label_eg_name= Frame(line_8, bg= bg_default, height= 20, width = 8)
    frame_label_eg_name.propagate(False)
    frame_label_eg_name.pack(side= 'right')
    label_eg_name = Label(frame_label_eg_name, font= font_default, text= '(', bg= bg_default, fg= font_white)
    label_eg_name.bind('<ButtonRelease-1>', eg_exist_toggle_frame)
    label_eg_name.pack(side= 'left')

    frame_label_eg_name= Frame(line_9, bg= bg_default, height= 20, width = 104)
    frame_label_eg_name.propagate(False)
    frame_label_eg_name.pack(side= 'left')
    label_eg_name = Label(frame_label_eg_name, font= font_default, text= 'makeInputName', bg= bg_default, fg= font_turq)
    label_eg_name.pack(side= 'left')
    frame_label_eg_name= Frame(line_9, bg= bg_default, height= 20, width = 16)
    frame_label_eg_name.propagate(False)
    frame_label_eg_name.pack(side= 'left')
    label_eg_name = Label(frame_label_eg_name, font= font_default, text= '= ', bg= bg_default, fg= font_white)
    label_eg_name.pack(side= 'left')

    frame_label_eg_name= Frame(line_9, bg= bg_default, height= 20, width = 8)
    frame_label_eg_name.propagate(False)
    frame_label_eg_name.pack(side= 'right')
    label_eg_name = Label(frame_label_eg_name, font= font_default, text= '\'', bg= bg_default, fg= font_orange)
    label_eg_name.pack(side= 'left')

    if len(config['save']['eg_name']) < 7:
        eg_name_entry_width = 56
    else:
        eg_name_entry_width = len(config['save']['eg_name']) * 8 + 2
    frame_entry_eg_name= Frame(line_9, bg= bg_default, height= 20, width = eg_name_entry_width)
    frame_entry_eg_name.propagate(False)
    frame_entry_eg_name.pack(side= 'right')
    entry_eg_name = Entry(frame_entry_eg_name, font= font_default, bd= 0, bg= '#36393d', fg= '#828589', insertbackground= font_num2, justify= 'center')
    entry_eg_name.dirName = ''
    entry_eg_name.insert(0, config['save']['eg_name'])
    entry_eg_name.bind('<FocusIn>', entry_eg_name_clear)
    entry_eg_name.bind('<FocusOut>', entry_eg_name_focus_out)
    entry_eg_name.pack(fill= 'both')

    frame_label_eg_name= Frame(line_9, bg= bg_default, height= 20, width = 8)
    frame_label_eg_name.propagate(False)
    frame_label_eg_name.pack(side= 'right')
    label_eg_name = Label(frame_label_eg_name, font= font_default, text= '\'', bg= bg_default, fg= font_orange)
    label_eg_name.pack(side= 'left')


#-------------------------------------------템플릿 파일-----------------------------------------
   
    def temp_exist_toggle_frame(event):
        frame_temp_path_hide.pack_forget() if frame_temp_path_hide.winfo_manager() else frame_temp_path_hide.pack(after= line_10)
        label_temp_path_bool.configure(text = 'True') if frame_temp_path_hide.winfo_manager() else label_temp_path_bool.configure(text = 'False')

    def select_template(event):
        global temp_path_dir
        temp_path = filedialog.askopenfilename(
    	initialdir = 'path', 
     	title='템플릿 파일을 선택하세요.',
        filetypes= [("*.py",".py")])
        if temp_path == '':
            return
        temp_path_dir = temp_path
        show_temp_path = '\'~' + temp_path_dir[temp_path_dir.find('/', 10):] + '\''
        frame_temp_path_hide['height'] = len(show_temp_path)//28 * 20 + 40
        line_12['height'] = len(show_temp_path)//28 * 20 + 20
        frame_temp_path_dir['height'] = len(show_temp_path)//28 * 20 + 20
        label_temp_path_dir.configure(text = show_temp_path)

    global temp_path_dir
    temp_path_dir= config['save']['temp_path']

    frame_label_temp_path= Frame(line_10, bg= bg_default, height= 20, width = 128)
    frame_label_temp_path.propagate(False)
    frame_label_temp_path.pack(side= 'left')
    label_temp_path = Label(frame_label_temp_path, font= font_default, text= 'copyTemplateFile', bg= bg_default, fg= font_turq)
    label_temp_path.bind('<ButtonRelease-1>', temp_exist_toggle_frame)
    label_temp_path.pack(side= 'left')
    frame_label_temp_path= Frame(line_10, bg= bg_default, height= 20, width = 16)
    frame_label_temp_path.propagate(False)
    frame_label_temp_path.pack(side= 'left')
    label_temp_path = Label(frame_label_temp_path, font= font_default, text= '= ', bg= bg_default, fg= font_white)
    label_temp_path.bind('<ButtonRelease-1>', temp_exist_toggle_frame)
    label_temp_path.pack(side= 'left')
    frame_label_temp_path= Frame(line_10, bg= bg_default, height= 20, width = 8)
    frame_label_temp_path.propagate(False)
    frame_label_temp_path.pack(side= 'right')
    label_temp_path = Label(frame_label_temp_path, font= font_default, text= ')', bg= bg_default, fg= font_white)
    label_temp_path.bind('<ButtonRelease-1>', temp_exist_toggle_frame)
    label_temp_path.pack(side= 'left')


    frame_label_temp_path= Frame(line_10, bg= bg_default, height= 20, width = 56)
    frame_label_temp_path.propagate(False)
    frame_label_temp_path.pack(side= 'right')
    if config['save']['temp_exist'] == '1':
        temp_text_bool= 'True'
    else:
        temp_text_bool= ' False '
    label_temp_path_bool = Label(frame_label_temp_path, font= font_default, text= temp_text_bool, bg= bg_default, fg= font_blue, width= 40, takefocus= True)
    label_temp_path_bool.bind('<ButtonRelease-1>', temp_exist_toggle_frame)
    label_temp_path_bool.bind('<Return>', temp_exist_toggle_frame)
    label_temp_path_bool.bind("<Enter>", config_button_on_enter)
    label_temp_path_bool.bind("<Leave>", config_button_on_leave)
    label_temp_path_bool.bind("<FocusIn>", config_button_on_enter)
    label_temp_path_bool.bind("<FocusOut>", config_button_on_leave)
    label_temp_path_bool.pack(side= 'top')

    frame_label_temp_path= Frame(line_10, bg= bg_default, height= 20, width = 8)
    frame_label_temp_path.propagate(False)
    frame_label_temp_path.pack(side= 'right')
    label_temp_path = Label(frame_label_temp_path, font= font_default, text= '(', bg= bg_default, fg= font_white)
    label_temp_path.bind('<ButtonRelease-1>', temp_exist_toggle_frame)
    label_temp_path.pack(side= 'left')
        
    frame_temp_path = Frame(line_11, bg= bg_default, height= 20, width = 64)
    frame_temp_path.propagate(False)
    frame_temp_path.pack(side= 'left')
    label_temp_path = Label(frame_temp_path, font= font_default, text = 'tempPath', bg= bg_default, fg= font_turq)
    label_temp_path.pack(side= 'left')
    frame_temp_path = Frame(line_11, bg= bg_default, height= 20, width = 16)
    frame_temp_path.propagate(False)
    frame_temp_path.pack(side= 'left')
    label_temp_path = Label(frame_temp_path, font= font_default, text= '= ', bg= bg_default, fg= font_white)
    label_temp_path.pack(side= 'left')
    frame_temp_path = Frame(line_11, bg= bg_default, height= 20, width = 16)
    frame_temp_path.propagate(False)
    frame_temp_path.pack(side= 'left')
    label_temp_path = Label(frame_temp_path, font= font_default, text= 'os', bg= bg_default, fg= font_green)
    label_temp_path.pack(side= 'left')
    frame_temp_path = Frame(line_11, bg= bg_default, height= 20, width = 8)
    frame_temp_path.propagate(False)
    frame_temp_path.pack(side= 'left')
    label_temp_path = Label(frame_temp_path, font= font_default, text= '.', bg= bg_default, fg= font_white)
    label_temp_path.pack(side= 'left')
    frame_temp_path = Frame(line_11, bg= bg_default, height= 20, width = 32)
    frame_temp_path.propagate(False)
    frame_temp_path.pack(side= 'left')
    label_temp_path = Label(frame_temp_path, font= font_default, text= 'path', bg= bg_default, fg= font_turq)
    label_temp_path.pack(side= 'left')
    frame_temp_path = Frame(line_11, bg= bg_default, height= 20, width = 8)
    frame_temp_path.propagate(False)
    frame_temp_path.pack(side= 'left')
    label_temp_path = Label(frame_temp_path, font= font_default, text= '.', bg= bg_default, fg= font_white)
    label_temp_path.pack(side= 'left')
    frame_temp_path = Frame(line_11, bg= bg_default, height= 20, width = 80)
    frame_temp_path.propagate(False)
    frame_temp_path.pack(side= 'left')
    label_temp_path = Label(frame_temp_path, font= font_default, text= 'expanduser', bg= bg_default, fg= font_yellow)
    label_temp_path.pack(side= 'left')
    frame_temp_path = Frame(line_11, bg= bg_default, height= 20, width = 8)
    frame_temp_path.propagate(False)
    frame_temp_path.pack(side= 'left')
    label_temp_path = Label(frame_temp_path, font= font_default, text= '(', bg= bg_default, fg= font_white)
    label_temp_path.pack(side= 'left')

    frame_temp_path_search_margin = Frame(line_11, bg= bg_default, height= 20, width= 8)
    frame_temp_path_search_margin.propagate(False)
    frame_temp_path_search_margin.pack(side= 'right')
    frame_temp_path_search = Frame(line_11, bg= bg_default, height= 20, width= 56)
    frame_temp_path_search.propagate(False)
    frame_temp_path_search.pack(side= 'right')
    temp_path_search = Label(frame_temp_path_search, font= font_default, text = '\U0001f50d', pady= 4, relief= 'flat', bg= bg_default, fg = 'snow')
    temp_path_search.bind('<ButtonRelease-1>', select_template)
    temp_path_search.bind("<Enter>", config_button_on_enter)
    temp_path_search.bind("<Leave>", config_button_on_leave)
    temp_path_search.pack(fill= 'both', expand= True) 

    temp_path_dir = config['save']['temp_path']
    show_temp_path = '\'~' + temp_path_dir[temp_path_dir.find('/', 10):] + '\''
    frame_temp_path_hide['height'] = len(show_temp_path)//28 * 20 + 40
    line_12['height'] = len(show_temp_path)//28 * 20 + 20
    frame_temp_path_dir = Frame(line_12, bg= bg_default, height= len(show_temp_path)//28 * 20 + 20, width = 224)
    frame_temp_path_dir.propagate(False)
    frame_temp_path_dir.pack(side= 'left')
    label_temp_path_dir = Label(frame_temp_path_dir, font= font_default, text = show_temp_path, bg= bg_default, fg= font_orange, wraplength= 224, justify= 'left')
    label_temp_path_dir.pack(anchor= 'w')

    frame_temp_path = Frame(line_13, bg= bg_default, height= 20, width = 8)
    frame_temp_path.propagate(False)
    frame_temp_path.pack(side= 'left')
    label_temp_path = Label(frame_temp_path, font= font_default, text= ')', bg= bg_default, fg= font_white)
    label_temp_path.pack(side= 'left')


# ------------------------------------------마지막 라인-----------------------------------------

    frame_label_end_line = Frame(line_15, bg= bg_default, height= 20, width = 32)
    frame_label_end_line.propagate(False)
    frame_label_end_line.pack(side= 'left')
    label_end_line = Label(frame_label_end_line, font= font_default, text= 'try ', bg= bg_default, fg= font_pink)
    label_end_line.pack(side= 'left')
    frame_label_end_line = Frame(line_15, bg= bg_default, height= 20, width = 8)
    frame_label_end_line.propagate(False)
    frame_label_end_line.pack(side= 'left')
    label_end_line = Label(frame_label_end_line, font= font_default, text= ':', bg= bg_default, fg= font_white)
    label_end_line.pack(side= 'left')
    frame_label_end_line = Frame(line_16, bg= bg_default, height= 20, width = 72)
    frame_label_end_line.propagate(False)
    frame_label_end_line.pack(side= 'left')
    label_end_line = Label(frame_label_end_line, font= font_default, text= 'makeFile ', bg= bg_default, fg= font_yellow)
    label_end_line.pack(side= 'left')
    frame_label_end_line = Frame(line_16, bg= bg_default, height= 20, width = 16)
    frame_label_end_line.propagate(False)
    frame_label_end_line.pack(side= 'left')
    label_end_line = Label(frame_label_end_line, font= font_default, text= '()', bg= bg_default, fg= font_white)
    label_end_line.pack(side= 'left')

    frame_label_end_line = Frame(line_17, bg= bg_default, height= 20, width = 56)
    frame_label_end_line.propagate(False)
    frame_label_end_line.pack(side= 'left')
    label_end_line = Label(frame_label_end_line, font= font_default, text= 'except ', bg= bg_default, fg= font_pink)
    label_end_line.pack(side= 'left')
    frame_label_end_line = Frame(line_17, bg= bg_default, height= 20, width = 80)
    frame_label_end_line.propagate(False)
    frame_label_end_line.pack(side= 'left')
    label_end_line = Label(frame_label_end_line, font= font_default, text= 'Exception ', bg= bg_default, fg= font_green)
    label_end_line.pack(side= 'left')
    frame_label_end_line = Frame(line_17, bg= bg_default, height= 20, width = 24)
    frame_label_end_line.propagate(False)
    frame_label_end_line.pack(side= 'left')
    label_end_line = Label(frame_label_end_line, font= font_default, text= 'as ', bg= bg_default, fg= font_pink)
    label_end_line.pack(side= 'left')
    frame_label_end_line = Frame(line_17, bg= bg_default, height= 20, width = 8)
    frame_label_end_line.propagate(False)
    frame_label_end_line.pack(side= 'left')
    label_end_line = Label(frame_label_end_line, font= font_default, text= 'e', bg= bg_default, fg= font_turq)
    label_end_line.pack(side= 'left')
    frame_label_end_line = Frame(line_17, bg= bg_default, height= 20, width = 8)
    frame_label_end_line.propagate(False)
    frame_label_end_line.pack(side= 'left')
    label_end_line = Label(frame_label_end_line, font= font_default, text= ':', bg= bg_default, fg= font_white)
    label_end_line.pack(side= 'left')


    frame_label_end_line = Frame(line_18, bg= bg_default, height= 20, width = 88)
    frame_label_end_line.propagate(False)
    frame_label_end_line.pack(side= 'left')
    label_end_line = Label(frame_label_end_line, font= font_default, text= 'printError ', bg= bg_default, fg= font_yellow)
    label_end_line.pack(side= 'left')
    frame_label_end_line = Frame(line_18, bg= bg_default, height= 20, width = 8)
    frame_label_end_line.propagate(False)
    frame_label_end_line.pack(side= 'left')
    label_end_line = Label(frame_label_end_line, font= font_default, text= '(', bg= bg_default, fg= font_white)
    label_end_line.pack(side= 'left')
    frame_label_end_line = Frame(line_18, bg= bg_default, height= 20, width = 8)
    frame_label_end_line.propagate(False)
    frame_label_end_line.pack(side= 'left')
    label_end_line = Label(frame_label_end_line, font= font_default, text= 'e', bg= bg_default, fg= font_turq)
    label_end_line.pack(side= 'left')
    frame_label_end_line = Frame(line_18, bg= bg_default, height= 20, width = 8)
    frame_label_end_line.propagate(False)
    frame_label_end_line.pack(side= 'left')
    label_end_line = Label(frame_label_end_line, font= font_default, text= ')', bg= bg_default, fg= font_white)
    label_end_line.pack(side= 'left')
    

# ------------------------------------------파일 만들기-----------------------------------------


    def save_status():
        config['save']['path'] = root.dirName
        
        if entry_py_name.get() == '':
            entry_save = config['save']['py_name']
        elif entry_py_name.get().endswith('.py') != True:
            entry_save = entry_py_name.get() + '.py'
        else:
            entry_save = entry_py_name.get()
        config['save']['py_name'] = entry_save

        if frame_eg_name_hide.winfo_manager():
            config['save']['eg_exist'] = '1'
        else:
            config['save']['eg_exist'] = '0'
        
        if entry_eg_name.get() == '':
            entry_save = config['save']['eg_name']
        else:
            entry_save = entry_eg_name.get()
        config['save']['eg_name'] = entry_save

        if frame_temp_path_hide.winfo_manager():
            config['save']['temp_exist'] = '1'
        else:
            config['save']['temp_exist'] = '0'
        config['save']['temp_path'] = temp_path_dir

        with open(os.path.expanduser('~\\Documents\\BOJ Helper\\config.ini'), 'w', encoding='utf-8') as config_file:
            config.write(config_file)

    def print_error(err_text):
        label_err['text'] = err_text
    
    def compile_complete(q_name):
        global func_id
        root.focus_set()
        root.bind('<Return>', show_problem)
        root.bind('y', show_problem)
        root.bind('n', return_to_default)
        term_line_2['height'] = 40
        label_err['text'] = '\'' + q_name + '\' 문제를 찾았습니다.\n문제를 화면에 출력하시겠습니까?(Y/N)'
        frame_button_return.pack_forget()
        frame_button_Y.pack(side= 'left')
        frame_button_N.pack(side= 'right')
        func_id = entry_q_num.bind('<FocusIn>', return_to_default, '+')

    def return_to_default(event):
        entry_q_num.unbind('<FocusIn>', func_id)
        entry_q_num.bind('<FocusIn>', entry_q_num_clear)
        label_err['text'] = ''
        frame_cmd_cursor.pack(side= 'left')
        frame_button_return.pack()
        frame_button_Y.pack_forget()
        frame_button_N.pack_forget()
        root.unbind('<Return>')
        root.unbind('y')
        root.unbind('n')
        entry_q_num.focus_set()


    def create_file(event):
        
        label_err.configure(text= '')
        frame_cmd_cursor.pack_forget()
        q_num = entry_q_num.get()

        try:
            int(q_num)
        except ValueError:
            print_error('잘못된 형식의 번호입니다.')
            return

        url = 'https://www.acmicpc.net/problem/' + q_num

        res = requests.get(url)
        if res.status_code == 404: 
            print_error('입력하신 번호의 문제는 존재하지 않습니다.')
            return
    
        elif res.status_code != requests.codes.ok: 
            print_error('페이지 접속에 문제가 생겼습니다. [에러코드 ', res.status_code,']', sep='')
            return
    
        save_status()
        if config['save']['temp_exist'] == '1':
            if not os.path.isfile(config['save']['temp_path']):
                print_error('템플릿 파일이 존재하지 않습니다.')
                return

        soup = BeautifulSoup(res.text, "lxml")
        question = soup.find_all("div", {"class" : "problem-text"})

        if frame_temp_path_hide.winfo_manager():
            shutil.copyfile(temp_path_dir, config['save']['path'] +'/'+ config['save']['py_name'])
        else:
            with open(config['save']['path'] +'/'+ config['save']['py_name'], 'w', encoding = 'utf-8') as f:
                f.write('')
        
        if frame_eg_name_hide.winfo_manager():
            sample_input = soup.find_all('pre', {'id' : re.compile("sample-input-[\d]")})
            sample_temp = ''
            for i in sample_input:
                for j in i.children:
                    if isinstance(j, NavigableString):
                        sample_temp += j.replace('\r', '') + '\n-----\n\n'
            sample_temp = sample_temp.rstrip('\n-----\n\n')
            with open(config['save']['path'] +'/'+ config['save']['eg_name'], 'w', encoding = 'utf-8') as f:
                f.write(sample_temp)


        cache_folder = os.path.expanduser('~\\Documents\\BOJ Helper\\app_cache')

        if not os.path.isdir(cache_folder):
            create_folder(cache_folder)
        else:
            rmtree(cache_folder)
            create_folder(cache_folder)
        
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
        
        with open(os.path.expanduser('~\\Documents\\BOJ Helper\\app_cache\\0_q_'+ str(question_number) +'.html'), 'w', encoding = "utf8") as f:
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
        
        for i in range(1, len(question)+1):
            if question[i-1] == False:
                continue
            if i <= 4:
                with open(os.path.expanduser('~\\Documents\\BOJ Helper\\app_cache\\'+ str(i) + '_' + question_tag[i-1] +'.html'), 'w', encoding = "utf8") as f:
                    f.write(question_array[i-1])
            elif 4 < i < len(question):
                with open(os.path.expanduser('~\\Documents\\BOJ Helper\\app_cache\\'+ str(i) + '_' + question_tag[4] + str(i-4) +'.html'), 'w', encoding = "utf8") as f:
                    f.write(question_array[i-1])
            else:
                with open(os.path.expanduser('~\\Documents\\BOJ Helper\\app_cache\\'+ str(i) + '_' + question_tag[5] +'.html'), 'w', encoding = "utf8") as f:
                    f.write(question_array[i-1])

        compile_complete(question_title)
        

# -----------------------------------------문제 불러오기----------------------------------------

    def show_problem(event):

        def close_problem_window():
            root.deiconify()
            listener.stop()
            problem_window.after(0, problem_window.destroy)

        def close_problem_window_btn(event):
            close_problem_window()
        
        def toggle_problem_window():
            global pw_state
            if pw_state == 1:
                problem_window.withdraw()
                pw_state = 0
            else:
                problem_window.deiconify()
                pw_state = 1

        def control_button_on_enter(event):
            event.widget['bg'] = '#2e2e2e'
            l = event.widget.winfo_children()
            l[0]['bg'] = '#2e2e2e'

        def control_button_on_leave(event):
            event.widget['bg'] = '#252525'
            l = event.widget.winfo_children()
            l[0]['bg'] = '#252525'

        def next_frame():
            global current_frame

            if callable_frame[current_frame] == 0:
                frame_browser_problem.pack_forget()
            elif callable_frame[current_frame] == 1:
                frame_browser_inoutput.pack_forget()
            elif callable_frame[current_frame] == 2:
                frame_browser_problem_info.pack_forget()
            else:
                frame_browser_problem_sample_explain.pack_forget()

            current_frame += 1
            if current_frame == len(callable_frame):
                current_frame = 0

            if callable_frame[current_frame] == 0:
                frame_browser_problem.pack(fill= 'both', expand= True)
            elif callable_frame[current_frame] == 1:
                frame_browser_inoutput.pack(fill= 'both', expand= True)
            elif callable_frame[current_frame] == 2:
                frame_browser_problem_info.pack(fill= 'both', expand= True)
            else:
                frame_browser_problem_sample_explain.pack(fill= 'both', expand= True)

        def next_button(event):
            next_frame()

        def prev_frame():
            global current_frame

            if callable_frame[current_frame] == 0:
                frame_browser_problem.pack_forget()
            elif callable_frame[current_frame] == 1:
                frame_browser_inoutput.pack_forget()
            elif callable_frame[current_frame] == 2:
                frame_browser_problem_info.pack_forget()
            else:
                frame_browser_problem_sample_explain.pack_forget()

            if current_frame == 0:
                current_frame = len(callable_frame)
            current_frame -= 1

            if callable_frame[current_frame] == 0:
                frame_browser_problem.pack(fill= 'both', expand= True)
            elif callable_frame[current_frame] == 1:
                frame_browser_inoutput.pack(fill= 'both', expand= True)
            elif callable_frame[current_frame] == 2:
                frame_browser_problem_info.pack(fill= 'both', expand= True)
            else:
                frame_browser_problem_sample_explain.pack(fill= 'both', expand= True)
        
        def prev_button(event):
            prev_frame()

        listener = keyboard.GlobalHotKeys({'<alt>+,': prev_frame, '<alt>+.': next_frame, '<alt>+/': toggle_problem_window, '<alt>+q': close_problem_window})
        listener.start()
        
        problem_window = tk.Toplevel(root)
        root.withdraw()

        create_folder(os.path.expanduser('~\\Documents\\BOJ Helper\\web_cache'))

        if hasattr(sys, '_MEIPASS'):
            settings = {'locales_dir_path': os.path.join(sys._MEIPASS, 'locales'),
                        'resources_dir_path': sys._MEIPASS,
                        'browser_subprocess_path': os.path.join(sys._MEIPASS, 'subprocess.exe'),
                        'log_file': os.path.join(sys._MEIPASS, 'debug.log'),
                        'cache_path': os.path.expanduser('~\\Documents\\BOJ Helper\\web_cache')}
        else:
            settings = {'cache_path': os.path.expanduser('~\\Documents\\BOJ Helper\\web_cache')}

        cef.Initialize(settings= settings)
        sys.exceptionhook= cef.ExceptHook

        global pw_state
        pw_state = 1

        problem_window.title('BOJ Helper - Problem Viewer')
        problem_window_width = problem_window.winfo_screenwidth() // 4
        problem_window_height = problem_window.winfo_screenheight()
        problem_window.geometry(f'{problem_window_width}x{problem_window_height}-{0}-{0}')
        problem_window.configure(bg= '#1E1E1E', relief = 'solid', bd = 1, takefocus= True)
        problem_window.resizable(False, False)
        problem_window.attributes("-topmost", True)
        problem_window.overrideredirect(True)

        frame_top = Frame(problem_window, relief= 'flat', height= 29, bg= '#3c3c3c')
        frame_top.pack(fill= 'x')
        frame_top.propagate(False)

        button_close = Label(frame_top, text='\u26CC', font= font_problem_button1, padx= 6, relief= 'flat', bg= '#3c3c3c', fg= '#c7c7c7')
        button_close.bind("<ButtonRelease-1>", close_problem_window_btn)
        button_close.bind("<Enter>", close_on_enter)
        button_close.bind("<Leave>", close_on_leave)
        button_close.pack(side= 'left', fill= 'y')

        frame_control_panel = Frame(problem_window, relief= 'flat', height= 35, bg= '#252525')
        frame_control_panel.propagate(False)
        frame_control_panel.pack(fill= 'x')

        frame_label_prev_button = Frame(frame_control_panel, relief= 'flat', width= problem_window_width//2, bg= '#252525')
        frame_label_prev_button.propagate(False)
        frame_label_prev_button.bind("<Enter>", control_button_on_enter)
        frame_label_prev_button.bind("<Leave>", control_button_on_leave)
        frame_label_prev_button.bind("<ButtonRelease-1>", prev_button)
        frame_label_prev_button.pack(fill= 'y', side= 'left')

        label_prev_button = Label(frame_label_prev_button, text='\u2770', font= font_problem_button2, relief= 'flat', bg= '#252525', fg= '#c7c7c7')
        label_prev_button.bind("<ButtonRelease-1>", prev_button)
        label_prev_button.pack(fill= 'y')

        frame_label_next_button = Frame(frame_control_panel, relief= 'flat', width= problem_window_width//2, bg= '#252525')
        frame_label_next_button.propagate(False)
        frame_label_next_button.bind("<Enter>", control_button_on_enter)
        frame_label_next_button.bind("<Leave>", control_button_on_leave)
        frame_label_next_button.bind("<ButtonRelease-1>", next_button)
        frame_label_next_button.pack(fill= 'y', side= 'right')

        label_next_button = Label(frame_label_next_button, text='\u2771', font= font_problem_button2, relief= 'flat', bg= '#252525', fg= '#c7c7c7')
        label_next_button.bind("<ButtonRelease-1>", next_button)
        label_next_button.pack(fill= 'y')

        global current_frame
        current_frame = 0
        callable_frame = []
        for f_name in os.listdir(os.path.expanduser('~\\Documents\\BOJ Helper\\app_cache')):

            block_type = f_name[2:-5]
            sample_explain_num = 0
            if block_type[0] == 'q':

                frame_browser_problem = Frame(problem_window, bg= '#1e1e1e')
                frame_browser_problem.pack(fill= 'both', expand= True)

                with open(os.path.expanduser('~\\Documents\\BOJ Helper\\app_cache\\' + f_name), 'r', encoding='utf-8') as question_info_file:
                    question_info = question_info_file.read().split('\n')

                frame_question_info = Frame(frame_browser_problem, bg= '#1e1e1e', height= 50)
                frame_question_info.propagate(False)
                frame_question_info.pack(fill= 'x', pady= (20,15))
                frame_question_info_1 = Frame(frame_question_info, bg= '#1e1e1e', width= problem_window_width//3, height= 50)
                frame_question_info_1.propagate(False)
                frame_question_info_1.pack(fill= 'y', side= 'left', padx= (problem_window_width//30, 0))
                frame_question_info_3 = Frame(frame_question_info, bg= '#1e1e1e', width= problem_window_width//3, height= 50)
                frame_question_info_3.propagate(False)
                frame_question_info_3.pack(fill= 'y', side= 'right', padx= (0, problem_window_width//30))
                frame_question_info_2 = Frame(frame_question_info, bg= '#1e1e1e', width= problem_window_width//3, height= 50)
                frame_question_info_2.propagate(False)
                frame_question_info_2.pack(fill= 'y')
                label_question_info_1_top = Label(frame_question_info_1, font= font_problem_info1, text= '시간 제한', bg= '#1e1e1e', fg= '#aaaaaa')
                label_question_info_1_top.pack(anchor= 'n')
                label_question_info_1_bot = Label(frame_question_info_1, font= font_problem_info2, text= question_info[2], bg= '#1e1e1e', fg= '#aaaaaa')
                label_question_info_1_bot.pack(anchor= 'n')
                label_question_info_2_top = Label(frame_question_info_2, font= font_problem_info1, text= '메모리 제한', bg= '#1e1e1e', fg= '#aaaaaa')
                label_question_info_2_top.pack(anchor= 'n')
                label_question_info_2_bot = Label(frame_question_info_2, font= font_problem_info2, text= question_info[3], bg= '#1e1e1e', fg= '#aaaaaa')
                label_question_info_2_bot.pack(anchor= 'n')
                label_question_info_3_top = Label(frame_question_info_3, font= font_problem_info1, text= '정답 비율', bg= '#1e1e1e', fg= '#aaaaaa')
                label_question_info_3_top.pack(anchor= 'n')
                label_question_info_3_bot = Label(frame_question_info_3, font= font_problem_info2, text= question_info[4], bg= '#1e1e1e', fg= '#aaaaaa')
                label_question_info_3_bot.pack(anchor= 'n')

            elif block_type == 'problem':
                block_name = '문제'
                callable_frame.append(0)

                label_block_problem = Label(frame_browser_problem, font= font_problem_title, text= block_name, bg= '#1e1e1e', fg= '#aaaaaa')
                label_block_problem.pack(anchor= 'n')

                browser_frame = BrowserFrame(frame_browser_problem, f_name)
                browser_frame.pack(fill='both', expand= True)

            elif block_type == 'input':
                block_name = '입력'
                callable_frame.append(1)

                frame_browser_inoutput = Frame(problem_window, bg= '#1e1e1e')

                label_block = Label(frame_browser_inoutput, font= font_problem_title, text= block_name, bg= '#1e1e1e', fg= '#aaaaaa')
                label_block.pack(anchor= 'n')

                browser_frame = BrowserFrame(frame_browser_inoutput, f_name)
                browser_frame.pack(fill='both', expand= True)

            elif block_type == 'output':
                block_name = '출력'

                label_block = Label(frame_browser_inoutput, font= font_problem_title, text= block_name, bg= '#1e1e1e', fg= '#aaaaaa')
                label_block.pack(anchor= 'n')

                browser_frame = BrowserFrame(frame_browser_inoutput, f_name)
                browser_frame.pack(fill='both', expand= True)

            elif block_type == 'problem_limit':
                block_name = '제한'
                if 2 not in callable_frame:
                    callable_frame.append(2)
                    frame_browser_problem_info = Frame(problem_window, bg= '#1e1e1e')

                label_block = Label(frame_browser_problem_info, font= font_problem_title, text= block_name, bg= '#1e1e1e', fg= '#aaaaaa')
                label_block.pack(anchor= 'n')

                browser_frame = BrowserFrame(frame_browser_problem_info, f_name)
                browser_frame.pack(fill='both', expand= True)


            elif block_type == 'problem_hint':
                block_name = '힌트'
                if 2 not in callable_frame:
                    callable_frame.append(2)
                    frame_browser_problem_info = Frame(problem_window, bg= '#1e1e1e')

                label_block = Label(frame_browser_problem_info, font= font_problem_title, text= block_name, bg= '#1e1e1e', fg= '#aaaaaa')
                label_block.pack(anchor= 'n')

                browser_frame = BrowserFrame(frame_browser_problem_info, f_name)
                browser_frame.pack(fill='both', expand= True)

            else:
                block_name = '예제 설명'
                frame_browser_problem_sample_explain = Frame(problem_window, bg= '#1e1e1e')
                if sample_explain_num == 0:
                    label_block = Label(frame_browser_problem_sample_explain, font= font_problem_title, text= block_name, bg= '#1e1e1e', fg= '#aaaaaa')
                    label_block.pack(anchor= 'n')
                    callable_frame.append(3)
                    sample_explain_num == 1
                browser_frame = BrowserFrame(frame_browser_problem_sample_explain, f_name)
                browser_frame.pack(fill='both', expand= True)

        problem_window.mainloop()
        cef.Shutdown()
        listener.join()

    class BrowserFrame(tk.Frame):

        def __init__(self, mainframe, call_name, navigation_bar=None):
            self.navigation_bar = navigation_bar
            self.closing = False
            self.browser = None
            tk.Frame.__init__(self, mainframe)
            self.mainframe = mainframe
            self.call_name = call_name
            self.bind("<Configure>", self.on_configure)
            self.focus_set()

        def embed_browser(self):
            window_info = cef.WindowInfo()
            rect = [0, 0, self.winfo_width(), self.winfo_height()]
            window_info.SetAsChild(self.get_window_handle(), rect)
            self.browser = cef.CreateBrowserSync(window_info,
                                                 url='file://' + os.path.expanduser('~\\Documents\\BOJ Helper\\app_cache\\' + self.call_name))
            assert self.browser
            self.message_loop_work()

        def get_window_handle(self):
            if self.winfo_id() > 0:
                return self.winfo_id()
            else:
                raise Exception("Couldn't obtain window handle")

        def message_loop_work(self):
            cef.MessageLoopWork()
            self.after(10, self.message_loop_work)

        def on_configure(self, _):
            if not self.browser:
                self.embed_browser()


# ------------------------------------------터미널 버튼-----------------------------------------

    def terminal_button_on_enter(event):
        event.widget['bg'] = '#3a3a3a'

    def terminal_button_on_leave(event):
        event.widget['bg'] = '#303030'
    

    entry_q_num.bind('<Return>', create_file)
    entry_py_name.bind('<Return>', create_file)
    entry_eg_name.bind('<Return>', create_file)
    frame_terminal = Frame(root, bg= '#1e1e1e', width= app_width, height= 150)
    frame_terminal.propagate(False)
    frame_terminal.pack(side= 'bottom')
    frame_terminal_divider = Frame(root, bg= '#3e3e3e', width= app_width, height= 1)
    frame_terminal_divider.pack(side= 'bottom')
    frame_terminal_btn = Frame(frame_terminal, bg= '#1e1e1e', width= app_width, height= 35)
    frame_terminal_btn.propagate(False)
    frame_terminal_btn.pack()
    frame_terminal_btn_margin_left = Frame(frame_terminal_btn, bg= '#1e1e1e', width= 16)
    frame_terminal_btn_margin_left.pack(side= 'left')
    label_terminal_btn = Label(frame_terminal_btn, font= tkFont.Font(family= 'Malgun Gothic', size= 8), text= 'TERMINAL', bg= '#1e1e1e', fg= 'snow')
    label_terminal_btn.pack(anchor= 'nw', pady= (9, 0))
    frame_terminal_btn_underline = Frame(frame_terminal_btn, bg= 'snow', width= 59, height= 1)
    frame_terminal_btn_underline.pack(side= 'bottom', anchor= 'sw')
    frame_terminal_btn_margin_bot = Frame(frame_terminal, bg= '#1e1e1e', width= app_width, height= 9)
    frame_terminal_btn_margin_bot.propagate(False)
    frame_terminal_btn_margin_bot.pack()

    frame_button_frame = Frame(frame_terminal, bg= '#272727', width= app_width, height= 30)
    frame_button_frame.bind('<ButtonRelease-1>', create_file)
    frame_button_frame.propagate(False)
    frame_button_frame.pack(side= 'bottom')
    frame_button_divider = Frame(frame_terminal, bg= '#000000', width= app_width, height= 1)
    frame_button_divider.pack(side= 'bottom')
    frame_button_return = Frame(frame_button_frame, bg= '#272727', width= app_width, height= 30)
    frame_button_return.propagate(False)
    frame_button_return.pack(side= 'bottom')
    label_button_return = Label(frame_button_return, font= tkFont.Font(family= 'Malgun Gothic', size= 13), text= '<Return> \u23CE', bg= '#303030', fg= font_num2, takefocus= True)
    label_button_return.bind('<ButtonRelease-1>', create_file)
    label_button_return.bind('<Return>', create_file)
    label_button_return.bind("<Enter>", terminal_button_on_enter)
    label_button_return.bind("<Leave>", terminal_button_on_leave)
    label_button_return.bind("<FocusIn>", terminal_button_on_enter)
    label_button_return.bind("<FocusOut>", terminal_button_on_leave)
    label_button_return.pack(fill= 'both', expand= True)

    frame_button_Y = Frame(frame_button_frame, bg= '#272727', width= app_width//2, height= 30)
    frame_button_Y.bind('<ButtonRelease-1>', show_problem)
    frame_button_Y.propagate(False)
    label_button_Y = Label(frame_button_Y, font= tkFont.Font(family= 'Malgun Gothic', size= 13), text= 'Y \u23CE', bg= '#303030', fg= font_num2, takefocus= True)
    label_button_Y.bind('<ButtonRelease-1>', show_problem)
    label_button_Y.bind('<Return>', show_problem)
    label_button_Y.bind("<Enter>", terminal_button_on_enter)
    label_button_Y.bind("<Leave>", terminal_button_on_leave)
    label_button_Y.bind("<FocusIn>", terminal_button_on_enter)
    label_button_Y.bind("<FocusOut>", terminal_button_on_leave)
    label_button_Y.pack(fill= 'both', expand= True)

    frame_button_N = Frame(frame_button_frame, bg= '#272727', width= app_width//2, height= 30)
    frame_button_N.bind('<ButtonRelease-1>', return_to_default)
    frame_button_N.propagate(False)
    label_button_N = Label(frame_button_N, font= tkFont.Font(family= 'Malgun Gothic', size= 13), text= 'N \u23CE', bg= '#303030', fg= font_num2, takefocus= True)
    label_button_N.bind('<ButtonRelease-1>', return_to_default)
    label_button_N.bind('<Return>', return_to_default)
    label_button_N.bind("<Enter>", terminal_button_on_enter)
    label_button_N.bind("<Leave>", terminal_button_on_leave)
    label_button_N.bind("<FocusIn>", terminal_button_on_enter)
    label_button_N.bind("<FocusOut>", terminal_button_on_leave)
    label_button_N.pack(fill= 'both', expand= True)
    
    term_line_1 = Frame(frame_terminal, bg= bg_default, height= 20)
    term_line_1.pack(fill = 'x')
    term_line_1.bind('<ButtonRelease-1>', create_file)
    term_line_1.propagate(False)
    term_line_2 = Frame(frame_terminal, bg= bg_default, height= 20)
    term_line_2.pack(fill = 'x')
    term_line_2.bind('<ButtonRelease-1>', create_file)
    term_line_2.propagate(False)
    label_err_margin= Frame(term_line_2, bg= bg_default, width= 24)
    label_err_margin.propagate(False)
    label_err_margin.bind('<ButtonRelease-1>', create_file)
    label_err_margin.pack(side= 'left')
    label_err= Label(term_line_2, font= font_default, text= '', bg= bg_default, fg= font_term1, justify= 'left')
    label_err.bind('<ButtonRelease-1>', create_file)
    label_err.pack(side= 'left')

    frame_label_cmd_line = Frame(term_line_1, bg= bg_default, height= 20, width = 28)
    frame_label_cmd_line.propagate(False)
    frame_label_cmd_line.pack(side= 'left')
    label_cmd_line = Label(frame_label_cmd_line, font= font_default, text= 'xe>  ', bg= bg_default, fg= font_term1)
    label_cmd_line.pack(side= 'left')
    frame_label_cmd_line = Frame(term_line_1, bg= bg_default, height= 20, width = 24)
    frame_label_cmd_line.propagate(False)
    frame_label_cmd_line.pack(side= 'left')
    label_cmd_line = Label(frame_label_cmd_line, font= font_default, text= 'py ', bg= bg_default, fg= font_term2)
    label_cmd_line.pack(side= 'left')
    frame_label_cmd_line = Frame(term_line_1, bg= bg_default, height= 20, width = 56)
    frame_label_cmd_line.propagate(False)
    frame_label_cmd_line.pack(side= 'left')
    label_cmd_line = Label(frame_label_cmd_line, font= font_default, text= 'main.py', bg= bg_default, fg= font_term1)
    label_cmd_line.pack(side= 'left')
    frame_cmd_cursor = Frame(term_line_1, bg= font_term1, height= 20, width = 8)
    frame_cmd_cursor.propagate(False)
    frame_cmd_cursor.pack(side= 'left')

    
    root.mainloop()

########################################################################
if __name__ == '__main__':
    config_folder = os.path.expanduser('~\\Documents\\BOJ Helper')
    
    if not os.path.isfile(config_folder + '\\config.ini'):
        create_folder(config_folder)
        config_generator()
    if not os.path.isfile(config_folder + '\\favicon.ico'):
        file= requests.get('https://docs.google.com/uc?export=download&id=1JMldwKI2ToJjyZLlq5PgWxGHjM1WGCH6', allow_redirects= True)
        open(os.path.expanduser('~\\Documents\\BOJ Helper\\favicon.ico'), 'wb').write(file.content)

    main()