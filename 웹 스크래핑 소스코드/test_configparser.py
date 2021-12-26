import configparser
import tkinter
import tkinter.font as tkFont
from tkinter import filedialog
from tkinter import *
import os
import requests
from bs4 import BeautifulSoup

config = configparser.ConfigParser()

def create_config_folder(config_path):
    try:
        os.makedirs(config_path)
    except FileExistsError:
        return

def config_generator():

    config['save'] = {}
    config['save']['path'] = os.path.expanduser('~\\Documents\\Github\\work')
    config['save']['py_name'] = 'main.py'
    config['save']['eg_exist'] = '0'
    config['save']['eg_name'] = 'i.txt'
    config['save']['temp_exist'] = '0'
    config['save']['tamp_path'] = os.path.expanduser('~\\Documents\\Github\\work\\template\\main.py')

    with open(os.path.expanduser('~\\Documents\\BOJ Helper\\config.ini'), 'w', encoding='utf-8') as config_file:
        config.write(config_file)

def config_edit():

    config.read(os.path.expanduser('~\\Documents\\BOJ Helper\\config.ini'), encoding = 'utf-8') 

    root = Tk()
    root.title("설정")
    app_width = 336
    app_height = 540
    root.geometry(f'{app_width}x{app_height}-{0}-{40}')
    root['bg'] = '#1E1E1E'
    root['relief'] = 'solid'
    root['bd'] = 1
    root.resizable(False, False)
    root.attributes("-topmost", True)
    root.overrideredirect(True)

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

    def close_on_enter(event):
        event.widget['bg'] = '#D71526'

    def close_on_leave(event):
        event.widget['bg'] = '#3C3C3C'

    def close_window(event):
        event.widget.master.master.destroy()

    def save_status(event):
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
        elif entry_eg_name.get().endswith('.txt') != True:
            entry_save = entry_eg_name.get() + '.txt'
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
        root.destroy()
    
    frame_top = Frame(root, relief= 'flat', height= 20, bg= '#3c3c3c')
    frame_top.bind("<ButtonPress-1>", start_move)
    frame_top.bind("<ButtonRelease-1>", stop_move)
    frame_top.bind("<B1-Motion>", do_move) 
    frame_top.pack(fill= 'x')
    frame_top.propagate(False)

    button_close = Label(frame_top, text='\u26CC', font= tkFont.Font(size= 8), padx= 6, relief= 'flat', bg= '#3C3C3C', fg= 'snow')
    button_close.bind("<ButtonRelease-1>", close_window)
    button_close.bind("<Enter>", close_on_enter)
    button_close.bind("<Leave>", close_on_leave)
    button_close.pack(side= 'right', fill= 'y')

    font_default = tkFont.Font(family="Consolas", size= 11)
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

#    frame_margin_left= Frame(root, relief= 'flat', bg= bg_default, width= 12)
#    frame_margin_left.pack(side= 'left', fill= 'y')
#    frame_margin_right= Frame(root, relief= 'flat', bg= bg_default, width= 12)
#    frame_margin_right.pack(side= 'right', fill= 'y')

# --------------------------------------------프레임-------------------------------------------

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
    
        
# ----------------------------------------------------------------------------------------------

    label_def_line = Label(line_1, font= font_default, text= 'def', bg= bg_default, fg= font_blue)
    label_def_line.pack(side= 'left')
    label_def_line = Label(line_1, font= font_default, text= 'makeFile', bg= bg_default, fg= font_yellow)
    label_def_line.pack(side= 'left')
    label_def_line = Label(line_1, font= font_default, text= '():', bg= bg_default, fg= font_white)
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

    def entry_q_num_focus_out():
        if entry_q_num.get() == '':
            entry_q_num['bg'] = '#36393d'
        frame_line_2_top['bg'] = bg_default
        frame_line_2_bot['bg'] = bg_default
        line_2_label['fg'] = font_num1
        entry_q_num.after_idle(lambda: entry_q_num.configure(validate='focusout'))

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

    entry_q_num = Entry(line_2, validate= 'focusout', validatecommand= entry_q_num_focus_out, width= 7, font= font_default, bd= 0, bg= '#36393d',
                        fg= font_lime, insertbackground= font_num2, justify = 'center')
    entry_q_num.dirName = ''
    entry_q_num.bind('<Button-1>', entry_q_num_clear)
    entry_q_num.pack(side= 'right')
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
    
    def config_button_on_enter(event):
        event.widget['bg'] = '#3C3C3C'

    def config_button_on_leave(event):
        event.widget['bg'] = '#222529'

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

    save_path_search = Label(line_4, font= font_default, text = '\u2D48', padx= 2, pady= 4, relief= 'flat', bg= '#222529', fg = 'snow')
    save_path_search.bind('<ButtonRelease-1>', select_path)
    save_path_search.bind("<Enter>", config_button_on_enter)
    save_path_search.bind("<Leave>", config_button_on_leave)
    save_path_search.pack(side= 'left') 
    label_save_path.pack(side= 'left')

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

    def entry_py_name_focus_out():
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
        entry_py_name.after_idle(lambda: entry_py_name.configure(validate='focusout'))


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
    entry_py_name = Entry(frame_entry_py_name, validate= 'focusout', validatecommand= entry_py_name_focus_out,
                          font= font_default, bd= 0, bg= '#36393d', fg= '#828589', insertbackground= font_num2, justify= 'center')
    entry_py_name.dirName = ''
    entry_py_name.insert(0, config['save']['py_name'])
    entry_py_name.bind('<Button-1>', entry_py_name_clear)
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

    def entry_eg_name_focus_out():
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
        entry_eg_name.after_idle(lambda: entry_eg_name.configure(validate='focusout'))

    def eg_exist_toggle_frame(event):
        frame_eg_name_hide.pack_forget() if frame_eg_name_hide.winfo_manager() else frame_eg_name_hide.pack(after= line_8)
        label_eg_name_bool.configure(text = 'True', width= 32) if frame_eg_name_hide.winfo_manager() else label_eg_name_bool.configure(text = 'False', width= 40)

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
    label_eg_name_bool = Label(frame_label_eg_name, font= font_default, text= eg_text_bool, bg= bg_default, fg= font_blue)
    label_eg_name_bool.bind('<ButtonRelease-1>', eg_exist_toggle_frame)
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
    entry_eg_name = Entry(frame_entry_eg_name, validate= 'focusout', validatecommand= entry_eg_name_focus_out,
                          font= font_default, bd= 0, bg= '#36393d', fg= '#828589', insertbackground= font_num2, justify= 'center')
    entry_eg_name.dirName = ''
    entry_eg_name.insert(0, config['save']['eg_name'])
    entry_eg_name.bind('<Button-1>', entry_eg_name_clear)
    entry_eg_name.pack(fill= 'both')

    frame_label_eg_name= Frame(line_9, bg= bg_default, height= 20, width = 8)
    frame_label_eg_name.propagate(False)
    frame_label_eg_name.pack(side= 'right')
    label_eg_name = Label(frame_label_eg_name, font= font_default, text= '\'', bg= bg_default, fg= font_orange)
    label_eg_name.pack(side= 'left')


#-------------------------------------------템플릿 파일-----------------------------------------
   
    def temp_exist_toggle_frame(event):
        frame_temp_path_hide.pack_forget() if frame_temp_path_hide.winfo_manager() else frame_temp_path_hide.pack(after= line_10)
        label_temp_path_bool.configure(text = 'True', width= 32) if frame_temp_path_hide.winfo_manager() else label_temp_path_bool.configure(text = 'False', width= 40)

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
    label_temp_path_bool = Label(frame_label_temp_path, font= font_default, text= temp_text_bool, bg= bg_default, fg= font_blue)
    label_temp_path_bool.bind('<ButtonRelease-1>', temp_exist_toggle_frame)
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

    temp_path_search = Label(line_11, font= font_default, text = '\u2D48', padx= 2, pady= 4, relief= 'flat', bg= '#222529', fg = 'snow')
    temp_path_search.bind('<ButtonRelease-1>', select_template)
    temp_path_search.bind("<Enter>", config_button_on_enter)
    temp_path_search.bind("<Leave>", config_button_on_leave)
    temp_path_search.pack(side= 'left') 
    label_temp_path.pack(side= 'left')

    temp_path_dir = config['save']['temp_path']
    show_temp_path = '\'~' + temp_path_dir[temp_path_dir.find('/', 10):] + '\''
    frame_temp_path_hide['height'] = len(show_temp_path)//28 * 20 + 40
    line_12['height'] = len(show_temp_path)//28 * 20 + 20
    frame_temp_path_dir = Frame(line_12, bg= bg_default, height= len(show_temp_path)//28 * 20 + 20, width = 224)
    frame_temp_path_dir.propagate(False)
    frame_temp_path_dir.pack(side= 'left')
    label_temp_path_dir = Label(frame_temp_path_dir, font= font_default, text = show_temp_path, bg= bg_default, fg= font_orange, wraplength= 224, justify= 'left')
    label_temp_path_dir.pack(anchor= 'w', fill= 'both')

    frame_temp_path = Frame(line_13, bg= bg_default, height= 20, width = 8)
    frame_temp_path.propagate(False)
    frame_temp_path.pack(side= 'left')
    label_temp_path = Label(frame_temp_path, font= font_default, text= ')', bg= bg_default, fg= font_white)
    label_temp_path.pack(side= 'left')

    # --------------------------------------------------------------------------------------------
    
    label_def_line = Label(line_15, font= font_default, text= ' makeFile', bg= bg_default, fg= font_yellow)
    label_def_line.pack(side= 'left')
    label_def_line = Label(line_15, font= font_default, text= '()', bg= bg_default, fg= font_white)
    label_def_line.pack(side= 'left')

    # -----------------------------------------파일 만들기-----------------------------------------

    def print_error(err_text):
        err = Tk()
        err.title("백준헬퍼_에러")
        err_width = 300
        err_height = 200
        err_x = root.winfo_x() + (app_width // 2) - (err_width // 2)
        err_y = root.winfo_y() + (app_height // 2) - (err_height // 2)
        err.geometry('%dx%d+%d+%d' % (err_width, err_height, err_x, err_y))
        err['bg'] = bg_default
        err['relief'] = 'solid'
        err['bd'] = 1
        err.resizable(False, False)
        err.attributes("-topmost", True)
        err.overrideredirect(True)
            
        frame_top_err = Frame(err, relief= 'flat', height= 20, bg= '#3C3C3C')
        frame_top_err.bind("<ButtonPress-1>", start_move)
        frame_top_err.bind("<ButtonRelease-1>", stop_move)
        frame_top_err.bind("<B1-Motion>", do_move) 
        frame_top_err.pack(fill= 'x', anchor= 'n')

        frame_label_err = Frame(err, relief= 'flat', bg= bg_default, width= err_width, height= err_height)
        frame_label_err.pack()
        frame_label_err.propagate(False)

        label_err = Label(frame_label_err, text= err_text, bg= bg_default, fg= 'snow', font= font_default)
        label_err.place(anchor= 's', relx= 0.5, rely= 0.5)
        
        button_err_okay = Label(frame_label_err, font= font_default, text = '확인', padx= 5, pady= 2, relief= 'flat', bg= '#222529', fg = 'snow')
        button_err_okay.bind('<ButtonRelease-1>', close_window)
        button_err_okay.bind("<Enter>", config_button_on_enter)
        button_err_okay.bind("<Leave>", config_button_on_leave)
        button_err_okay.pack(side= 'bottom', pady= 8)

        
        err.mainloop()

    def create_file(event):
        
        q_num = entry_q_num.get()

        try:
            int(q_num)
        except ValueError:
            print_error('잘못된 형식의 번호입니다.')
            return

        url = 'https://www.acmicpc.net/problem/' + q_num

        res = requests.get(url)
        #res.raise_for_status()
        if res.status_code == 404: 
            print_error('입력하신 번호의 문제는\n존재하지 않습니다.')
            return
    
        elif res.status_code != requests.codes.ok: 
            print_error('페이지 로딩에 문제가 생겼습니다.\n[에러코드 ', res.status_code,']', sep='')
            return
    
        print_error('미완성 입니다 ㅎ')
        return 
    frame_create_btn = Frame(root, bg= '#1e1e1e', width= app_width, height= 120)
    frame_create_btn.propagate(False)
    frame_create_btn.bind('<ButtonRelease-1>', create_file)
    frame_create_btn.pack(side= 'bottom')
    frame_terminal_divider = Frame(root, bg= '#3e3e3e', width= app_width, height= 1)
    frame_terminal_divider.bind('<ButtonRelease-1>', create_file)
    frame_terminal_divider.pack(side= 'bottom')
    frame_terminal_btn = Frame(frame_create_btn, bg= '#1e1e1e', width= app_width, height= 35)
    frame_terminal_btn.bind('<ButtonRelease-1>', create_file)
    frame_terminal_btn.propagate(False)
    frame_terminal_btn.pack()
    frame_terminal_btn_margin = Frame(frame_terminal_btn, bg= '#1e1e1e', width= 20)
    frame_terminal_btn_margin.bind('<ButtonRelease-1>', create_file)
    frame_terminal_btn_margin.pack(side= 'left')
    label_terminal_btn = Label(frame_terminal_btn, font= tkFont.Font(family= 'Malgun Gothic', size= 8), text= 'TERMINAL', bg= '#1e1e1e', fg= 'snow')
    label_terminal_btn.bind('<ButtonRelease-1>', create_file)
    label_terminal_btn.pack(anchor= 'nw', pady= (9, 0))
    frame_terminal_btn_underline = Frame(frame_terminal_btn, bg= 'snow', width= 60, height= 1)
    frame_terminal_btn_underline.pack(side= 'bottom', anchor= 'sw')
    
    root.mainloop()


























########################################################################

config_file_path = os.path.expanduser('~\\Documents\\BOJ Helper\\config.ini')

if not os.path.isfile(config_file_path):
    config_path = config_file_path[:-11]
    create_config_folder(config_path)
    config_generator()

config_edit()



