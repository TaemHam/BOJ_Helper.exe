import requests
import sys
import os
import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
from cefpython3 import cefpython as cef

def show_problem():
    def close_on_enter(event):
        event.widget['bg'] = '#D71526'

    def close_on_leave(event):
        event.widget['bg'] = '#3C3C3C'

    def close_window(event):
        event.widget.master.master.destroy()

    def control_button_on_enter(event):
        event.widget['bg'] = '#282828'
        l = event.widget.winfo_children()
        l[0]['bg'] = '#282828'

    def control_button_on_leave(event):
        event.widget['bg'] = '#252525'
        l = event.widget.winfo_children()
        l[0]['bg'] = '#252525'
    
    def next_frame(event):
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

    def prev_frame(event):
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

    problem_window = Tk()
    cef.Initialize()
    sys.exceptionhook= cef.ExceptHook

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

    button_close = Label(frame_top, text='\u26CC', font= tkFont.Font(size= 8), padx= 6, relief= 'flat', bg= '#3c3c3c', fg= '#c7c7c7')
    button_close.bind("<ButtonRelease-1>", close_window)
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
    frame_label_prev_button.bind("<ButtonRelease-1>", prev_frame)
    frame_label_prev_button.pack(fill= 'y', side= 'left')
    
    label_prev_button = Label(frame_label_prev_button, text='\u2770', font= tkFont.Font(size= 20), relief= 'flat', bg= '#252525', fg= '#c7c7c7')
    label_prev_button.bind("<ButtonRelease-1>", prev_frame)
    label_prev_button.pack(fill= 'y')

    frame_label_next_button = Frame(frame_control_panel, relief= 'flat', width= problem_window_width//2, bg= '#252525')
    frame_label_next_button.propagate(False)
    frame_label_next_button.bind("<Enter>", control_button_on_enter)
    frame_label_next_button.bind("<Leave>", control_button_on_leave)
    frame_label_next_button.bind("<ButtonRelease-1>", next_frame)
    frame_label_next_button.pack(fill= 'y', side= 'right')
    
    label_next_button = Label(frame_label_next_button, text='\u2771', font= tkFont.Font(size= 20), relief= 'flat', bg= '#252525', fg= '#c7c7c7')
    label_next_button.bind("<ButtonRelease-1>", next_frame)
    label_next_button.pack(fill= 'y')

    global current_frame
    current_frame = 0
    callable_frame = []
    for f_name in os.listdir(os.path.expanduser('~\\Documents\\BOJ Helper\\cache')):

        block_type = f_name[2:-5]
        sample_explain_num = 0
        print(block_type)
        if block_type[0] == 'q':

            frame_browser_problem = Frame(problem_window, bg= '#1e1e1e')
            frame_browser_problem.pack(fill= 'both', expand= True)

            with open(os.path.expanduser('~\\Documents\\BOJ Helper\\cache\\' + f_name), 'r', encoding='utf-8') as question_info_file:
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
            label_question_info_1_top = Label(frame_question_info_1, font= tkFont.Font(family= 'Malgun Gothic', size= 13, weight= 'bold'), text= '시간 제한', bg= '#1e1e1e', fg= '#aaaaaa')
            label_question_info_1_top.pack(anchor= 'n')
            label_question_info_1_bot = Label(frame_question_info_1, font= tkFont.Font(family= 'Malgun Gothic', size= 13), text= question_info[2], bg= '#1e1e1e', fg= '#aaaaaa')
            label_question_info_1_bot.pack(anchor= 'n')
            label_question_info_2_top = Label(frame_question_info_2, font= tkFont.Font(family= 'Malgun Gothic', size= 13, weight= 'bold'), text= '메모리 제한', bg= '#1e1e1e', fg= '#aaaaaa')
            label_question_info_2_top.pack(anchor= 'n')
            label_question_info_2_bot = Label(frame_question_info_2, font= tkFont.Font(family= 'Malgun Gothic', size= 13), text= question_info[3], bg= '#1e1e1e', fg= '#aaaaaa')
            label_question_info_2_bot.pack(anchor= 'n')
            label_question_info_3_top = Label(frame_question_info_3, font= tkFont.Font(family= 'Malgun Gothic', size= 13, weight= 'bold'), text= '정답 비율', bg= '#1e1e1e', fg= '#aaaaaa')
            label_question_info_3_top.pack(anchor= 'n')
            label_question_info_3_bot = Label(frame_question_info_3, font= tkFont.Font(family= 'Malgun Gothic', size= 13), text= question_info[4], bg= '#1e1e1e', fg= '#aaaaaa')
            label_question_info_3_bot.pack(anchor= 'n')
            
        elif block_type == 'problem':
            block_name = '문제'
            callable_frame.append(0)

            label_block_problem = Label(frame_browser_problem, font= tkFont.Font(family= 'Malgun Gothic', size= 20, weight= 'bold'), text= block_name, bg= '#1e1e1e', fg= '#aaaaaa')
            label_block_problem.pack(anchor= 'n')

            browser_frame = BrowserFrame(frame_browser_problem, f_name)
            browser_frame.pack(fill='both', expand= True)

        elif block_type == 'input':
            block_name = '입력'
            callable_frame.append(1)

            frame_browser_inoutput = Frame(problem_window, bg= '#1e1e1e')

            label_block = Label(frame_browser_inoutput, font= tkFont.Font(family= 'Malgun Gothic',  size= 20, weight= 'bold'), text= block_name, bg= '#1e1e1e', fg= '#aaaaaa')
            label_block.pack(anchor= 'n')

            browser_frame = BrowserFrame(frame_browser_inoutput, f_name)
            browser_frame.pack(fill='both', expand= True)

        elif block_type == 'output':
            block_name = '출력'

            label_block = Label(frame_browser_inoutput, font= tkFont.Font(family= 'Malgun Gothic',  size= 20, weight= 'bold'), text= block_name, bg= '#1e1e1e', fg= '#aaaaaa')
            label_block.pack(anchor= 'n')

            browser_frame = BrowserFrame(frame_browser_inoutput, f_name)
            browser_frame.pack(fill='both', expand= True)

        elif block_type == 'problem_limit':
            block_name = '제한'
            if 2 not in callable_frame:
                callable_frame.append(2)
                frame_browser_problem_info = Frame(problem_window, bg= '#1e1e1e')

            label_block = Label(frame_browser_problem_info, font= tkFont.Font(family= 'Malgun Gothic',  size= 20, weight= 'bold'), text= block_name, bg= '#1e1e1e', fg= '#aaaaaa')
            label_block.pack(anchor= 'n')

            browser_frame = BrowserFrame(frame_browser_problem_info, f_name)
            browser_frame.pack(fill='both', expand= True)


        elif block_type == 'problem_hint':
            block_name = '힌트'
            if 2 not in callable_frame:
                callable_frame.append(2)
                frame_browser_problem_info = Frame(problem_window, bg= '#1e1e1e')

            label_block = Label(frame_browser_problem_info, font= tkFont.Font(family= 'Malgun Gothic',  size= 20, weight= 'bold'), text= block_name, bg= '#1e1e1e', fg= '#aaaaaa')
            label_block.pack(anchor= 'n')

            browser_frame = BrowserFrame(frame_browser_problem_info, f_name)
            browser_frame.pack(fill='both', expand= True)

        else:
            block_name = '예제 설명'
            frame_browser_problem_sample_explain = Frame(problem_window, bg= '#1e1e1e')
            if sample_explain_num == 0:
                label_block = Label(frame_browser_problem_sample_explain, font= tkFont.Font(family= 'Malgun Gothic',  size= 20, weight= 'bold'), text= block_name, bg= '#1e1e1e', fg= '#aaaaaa')
                label_block.pack(anchor= 'n')
                callable_frame.append(3)
                sample_explain_num == 1
            browser_frame = BrowserFrame(frame_browser_problem_sample_explain, f_name)
            browser_frame.pack(fill='both', expand= True)

    problem_window.mainloop()
    cef.Shutdown()

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
                                             url='file://' + os.path.expanduser('~\\Documents\\BOJ Helper\\cache\\' + self.call_name))
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

if __name__ == '__main__':
    show_problem()

