import configparser
import tkinter
import tkinter.font as tkFont
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
    config['save']['eg_exist'] = '0'
    config['save']['eg_name'] = 'i.txt'
    config['save']['temp_exist'] = '0'
    config['save']['tamp_path'] = os.path.expanduser('~\\Documents\\Github\\work\\template\\main.py')

    with open(os.path.expanduser('~\\Documents\\BOJ Helper\\config.ini'), 'w', encoding='utf-8') as config_file:
        config.write(config_file)

def config_edit():
    
    config = configparser.ConfigParser()
    config.read(os.path.expanduser('~\\Documents\\BOJ Helper\\config.ini'), encoding = 'utf-8') 

    root = Tk()
    root.title("설정")
    app_width = 300
    app_height = 540
    root.geometry(f'{app_width}x{app_height}+{100}+{100}')
    root['bg'] = '#1A1D21'
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
        x = root.winfo_x() + deltax
        y = root.winfo_y() + deltay
        root.geometry(f"+{x}+{y}")

    def close_on_enter(event):
        close['bg'] = '#D71526'

    def close_on_leave(event):
        event.widget['bg'] = '#111418'

    def close_window(even):
        root.destroy()

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
    
    
    frame_top = tkinter.Frame(root, relief= 'flat', height= 9, bg= '#111418')
    frame_top.bind("<ButtonPress-1>", start_move)
    frame_top.bind("<ButtonRelease-1>", stop_move)
    frame_top.bind("<B1-Motion>", do_move) 
    frame_top.pack(fill= 'x')

    close = Label(frame_top, text='\u26CC', font= tkFont.Font(size= 8), padx= 3, pady= 3, relief= 'flat', bg= '#111418', fg= 'snow', justify= 'center')
    close.bind("<ButtonRelease-1>", close_window)
    close.bind("<Enter>", close_on_enter)
    close.bind("<Leave>", close_on_leave)
    close.pack(side= 'right')

    font_default = tkFont.Font(family="Malgun Gothic", size= 11)

    save_btn = Label (root, text="저장", font= font_default, bg='#222529', fg = 'snow', pady= 6)
    save_btn.bind('<ButtonRelease-1>', save_status)
    save_btn.pack(side= 'bottom', fill= 'x')

    frame_margin_left= tkinter.Frame(root, relief= 'flat', bg= '#1A1D21', width= 12)
    frame_margin_left.pack(side= 'left', fill= 'y')
    frame_margin_right= tkinter.Frame(root, relief= 'flat', bg= '#1A1D21', width= 12)
    frame_margin_right.pack(side= 'right', fill= 'y')

#-------------------------------------------저장 경로------------------------------------------

    def select_path(event):
        folder_path = filedialog.askdirectory(
    	initialdir = 'path', 
     	title='저장할 폴더를 선택하세요.')
        if folder_path == '':
            return
        root.dirName = folder_path
        if len(root.dirName) > 30:
            show_folder_path = '...' + root.dirName[root.dirName.rfind('/', 0, len(root.dirName)-20):]
        else:
            show_folder_path = root.dirName
        path_text.configure(text = show_folder_path)
    
    def config_button_on_enter(event):
        event.widget['bg'] = '#111418'

    def config_button_on_leave(event):
        event.widget['bg'] = '#222529'

    frame_label_path_text = tkinter.Frame(root, relief= 'flat', bg= '#1A1D21', width= app_width, height= 18)
    frame_label_path_text.pack(anchor= 'n', pady= (14,3))
    frame_label_path_text.propagate(False)

    frame_path_text = tkinter.Frame(root, relief= 'flat', bg= '#222529', width= app_width, height= 18)
    frame_path_text.pack(anchor= 'n', padx= 2, pady= 10)
    frame_path_text.propagate(False)

    label_path_text = Label(frame_label_path_text, font= font_default, pady= 2, text = '저장 경로', bg= '#1A1D21', fg= 'snow')
    label_path_text.pack(side= 'left', padx= (0,3))

    save_path_search = Label(frame_label_path_text, font= font_default, text = '\u2D48', padx= 2, pady= 4, relief= 'flat', bg= '#222529', fg = 'snow')
    save_path_search.bind('<ButtonRelease-1>', select_path)
    save_path_search.bind("<Enter>", config_button_on_enter)
    save_path_search.bind("<Leave>", config_button_on_leave)
    save_path_search.pack(side= 'left')

    root.dirName = config['save']['path']
    if len(root.dirName) > 30:
        show_folder_path = '...' + root.dirName[root.dirName.rfind('/', 0, len(root.dirName)-20):]
    else:
        show_folder_path = root.dirName
    path_text = Label(frame_path_text, font= tkFont.Font(size= 10), text = show_folder_path, pady= 2, bg= '#222529', fg= '#A0A0A0')
    path_text.pack(anchor= 'sw')

# -------------------------------------------파일 이름------------------------------------------

    def entry_py_name_focus_out():
        entry_py_name['bg'] = '#222529'
        entry_py_name['fg'] = '#828589'
        entry_py_name.after_idle(lambda: entry_py_name.configure(validate='focusout'))

    def entry_clear(event):
        event.widget.delete(0, 'end')
        event.widget['bg'] = '#36393d'
        event.widget['fg'] = 'snow'

    frame_label_py_name = tkinter.Frame(root, relief= 'flat', bg= '#1A1D21', width= app_width, height= 18)
    frame_label_py_name.pack(anchor= 'n', pady= (4,3))
    frame_label_py_name.propagate(False)

    frame_entry_py_name = tkinter.Frame(root, relief= 'flat', bg= '#222529', width= app_width, height= 18)
    frame_entry_py_name.pack(anchor= 'n', padx= 2, pady= 10)
    frame_entry_py_name.propagate(False)

    label_py_name = Label(frame_label_py_name, font= font_default, text= '파일 이름', bg= '#1A1D21', fg= 'snow')
    label_py_name.pack(side= 'left')

    entry_py_name = Entry(frame_entry_py_name, validate= 'focusout', validatecommand= entry_py_name_focus_out, font= tkFont.Font(size= 11), bd= 0, bg= '#222529', fg= '#828589')
    entry_py_name.insert(0, config['save']['py_name'])
    entry_py_name.bind('<Button-1>', entry_clear)
    entry_py_name.pack(fill= 'both')
    

#---------------------------------------------예제 파일-----------------------------------------

    def entry_eg_name_focus_out():
        entry_eg_name['bg'] = '#222529'
        entry_eg_name['fg'] = '#828589'
        entry_eg_name.after_idle(lambda: entry_eg_name.configure(validate='focusout'))

    def eg_exist_toggle_frame(event):
        frame_eg_name_hide.pack_forget() if frame_eg_name_hide.winfo_manager() else frame_eg_name_hide.pack(after= frame_eg_exist)
        button_eg_exist.configure(text = '\u02C4') if frame_eg_name_hide.winfo_manager() else button_eg_exist.configure(text = '\u02C5')
        label_eg_exist.configure(fg = 'snow') if frame_eg_name_hide.winfo_manager() else label_eg_exist.configure(fg = '#6b7787')

    frame_eg_exist = tkinter.Frame(root, relief= 'flat', bg= '#1A1D21', width= app_width, height= 15)
    frame_eg_exist.pack(anchor= 'n', pady= (14))
    frame_eg_exist.propagate(False)
    frame_eg_exist.bind('<ButtonRelease-1>', eg_exist_toggle_frame)

    separator_eg_exist = tkinter.Frame(frame_eg_exist, bg= '#6b7787', width= app_width, height= 1)	
    separator_eg_exist.place(relx = 0.5, relwidth= 1, y= 7, anchor= 'n')

    if config['save']['eg_exist'] == '1':
        arrow_head_eg = '\u02C4'
        color_eg_exist= 'snow'
    else:
        arrow_head_eg = '\u02C5'
        color_eg_exist= '#6b7787'
    button_eg_exist = Label(frame_eg_exist, text= arrow_head_eg, font= tkFont.Font(size= 20), padx= 5, relief= 'flat', bg= '#1A1D21', fg= 'snow')
    button_eg_exist.bind('<ButtonRelease-1>', eg_exist_toggle_frame)
    button_eg_exist.place(x= 10, y= -1)

    label_eg_exist = Label(frame_eg_exist, text= '예제 파일 저장', font= font_default, padx= 5, relief= 'flat', bg= '#1A1D21', fg= color_eg_exist)
    label_eg_exist.bind('<ButtonRelease-1>', eg_exist_toggle_frame)
    label_eg_exist.place(x= 30, y= -6)

    frame_eg_name_hide = tkinter.Frame(root, relief= 'flat', bg= '#1A1D21', width= app_width, height= 18)
    if config['save']['eg_exist'] == '1':
        frame_eg_name_hide.pack(anchor= 'n') 

    frame_label_eg_name = tkinter.Frame(frame_eg_name_hide, relief= 'flat', bg= '#1A1D21', width= app_width, height= 18)
    frame_label_eg_name.pack(anchor= 'n', pady= (4,3))
    frame_label_eg_name.propagate(False)

    frame_entry_eg_name = tkinter.Frame(frame_eg_name_hide, relief= 'flat', bg= '#222529', width= app_width, height= 18)
    frame_entry_eg_name.pack(anchor= 'n', padx= 2, pady= 10)
    frame_entry_eg_name.propagate(False)

    label_eg_name = Label(frame_label_eg_name, font= font_default, text= '예제 파일 저장 이름', bg= '#1A1D21', fg= 'snow')
    label_eg_name.pack(side= 'left')

    entry_eg_name = Entry(frame_entry_eg_name, validate= 'focusout', validatecommand= entry_eg_name_focus_out, font= tkFont.Font(size= 11), bd= 0, bg= '#222529', fg= '#828589')
    entry_eg_name.insert(0, config['save']['eg_name'])
    entry_eg_name.bind('<Button-1>', entry_clear)
    entry_eg_name.pack(fill= 'both')

    #---------------------------------------------템플릿 파일-----------------------------------------

    def temp_exist_toggle_frame(event):
        frame_temp_path_hide.pack_forget() if frame_temp_path_hide.winfo_manager() else frame_temp_path_hide.pack(after= frame_temp_exist)
        button_temp_exist.configure(text = '\u02C4') if frame_temp_path_hide.winfo_manager() else button_temp_exist.configure(text = '\u02C5')
        label_temp_exist.configure(fg = 'snow') if frame_temp_path_hide.winfo_manager() else label_temp_exist.configure(fg = '#6b7787')

    def select_template(event):
        global temp_path_dir
        temp_path = filedialog.askopenfilename(
    	initialdir = 'path', 
     	title='템플릿 파일을 선택하세요.',
        filetypes= [("*.py",".py")])
        if temp_path == '':
            return
        temp_path_dir = temp_path
        if len(temp_path_dir) > 30:
            show_temp_path = '...' + temp_path_dir[temp_path_dir.rfind('/', 0, len(temp_path_dir) - 20):]
        else:
            show_temp_path = temp_path_dir
        label_temp_path_dir.configure(text = show_temp_path)

    global temp_path_dir
    temp_path_dir= config['save']['temp_path']

    frame_temp_exist = tkinter.Frame(root, relief= 'flat', bg= '#1A1D21', width= app_width, height= 15)
    frame_temp_exist.pack(anchor= 'n', pady= (14))
    frame_temp_exist.propagate(False)
    frame_temp_exist.bind('<ButtonRelease-1>', temp_exist_toggle_frame)

    separator_temp_exist = tkinter.Frame(frame_temp_exist, bg= '#6b7787', width= app_width, height= 1)	
    separator_temp_exist.place(relx = 0.5, relwidth= 1, y= 7, anchor= 'n')

    if config['save']['temp_exist'] == '1':
        arrow_head_temp = '\u02C4'
        color_temp_exist= 'snow'
    else:
        arrow_head_temp= '\u02C5'
        color_temp_exist= '#6b7787'
    button_temp_exist = Label(frame_temp_exist, text= arrow_head_temp, font= tkFont.Font(size= 20), padx= 5, relief= 'flat', bg= '#1A1D21', fg= 'snow')
    button_temp_exist.bind('<ButtonRelease-1>', temp_exist_toggle_frame)
    button_temp_exist.place(x= 10, y= -1)

    label_temp_exist = Label(frame_temp_exist, text= '템플릿 복사', font= font_default, padx= 5, relief= 'flat', bg= '#1A1D21', fg= color_temp_exist)
    label_temp_exist.bind('<ButtonRelease-1>', temp_exist_toggle_frame)
    label_temp_exist.place(x= 30, y= -6)

    frame_temp_path_hide = tkinter.Frame(root, relief= 'flat', bg= '#1A1D21', width= app_width, height= 18)
    if config['save']['temp_exist'] == '1':
        frame_temp_path_hide.pack(anchor= 'n') 

    
    frame_label_temp_path = tkinter.Frame(frame_temp_path_hide, relief= 'flat', bg= '#1A1D21', width= app_width, height= 18)
    frame_label_temp_path.pack(anchor= 'n', pady= (4,3))
    frame_label_temp_path.propagate(False)

    frame_temp_path = tkinter.Frame(frame_temp_path_hide, relief= 'flat', bg= '#222529', width= app_width, height= 18)
    frame_temp_path.pack(anchor= 'n', padx= 2, pady= 10)
    frame_temp_path.propagate(False)

    label_temp_path = Label(frame_label_temp_path, font= font_default, pady= 2, text = '템플릿 경로', bg= '#1A1D21', fg= 'snow')
    label_temp_path.pack(side= 'left', padx= (0, 3))

    temp_path_search = Label(frame_label_temp_path, font= font_default, text = '\u2D48', padx= 2, pady= 4, relief= 'flat', bg= '#222529', fg = 'snow')
    temp_path_search.bind('<ButtonRelease-1>', select_template)
    temp_path_search.bind("<Enter>", config_button_on_enter)
    temp_path_search.bind("<Leave>", config_button_on_leave)
    temp_path_search.pack(side= 'left')

    if len(temp_path_dir) > 30:
        show_temp_path = '...' + temp_path_dir[temp_path_dir.rfind('/', 0, len(temp_path_dir) - 20):]
    else:
        show_temp_path = temp_path_dir
    label_temp_path_dir = Label(frame_temp_path, font= tkFont.Font(size= 10), text = show_temp_path, pady= 2, bg= '#222529', fg= '#A0A0A0')
    label_temp_path_dir.pack(anchor= 'sw')
    
    root.mainloop()

config_file_path = os.path.expanduser('~\\Documents\\BOJ Helper\\config.ini')

if not os.path.isfile(config_file_path):
    config_path = config_file_path[:-11]
    create_config_folder(config_path)
    config_generator()

config_edit()



