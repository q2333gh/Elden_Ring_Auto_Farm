import tkinter as tk
from pynput import keyboard
import time
from tkinter import font
import threading

times = 0
load_time = 0
thread = None
load_time_default = 6.0

stop_thread_flag = False

# Add a dictionary for multi-language support
lang_dict = {
    "cn": {
        "title": "艾尔登法环python自动化刷钱",
        "instructions": """
1. 在键盘设置中将ctrl设置为战技按键.\n
2. 装备大范围战技,金粪龟等.\n
3. 点击开始以后,把鼠标焦点三秒内移到艾尔登exe窗口并左键点击.
""",
        "times": "请输入刷钱次数:",
        "load_time": "请输入读图时间,默认6秒,下面输入框可以留白:",
        "start": "开始",
        "stop": "停止",
        "info": "按下停止以后,脚本还会完整跑完最后一次刷钱,请等待十秒",
        "change_lang": "切换到英文",
    },
    "en": {
        "title": "Elden Ring Python Automation for Money Farming",
        "instructions": """
1. Set ctrl as the combat skill key in the keyboard settings.\n
2. Equip large-scale combat skills, golden dung beetle, etc.\n
3. After clicking start, move the mouse focus to the Elden Ring exe window within three seconds and leftclick window.
""",
        "times": "Please enter the number of times for money farming:",
        "load_time": "Please enter the loading time, default is 6 seconds, the following input box can be left blank:",
        "start": "Start",
        "stop": "Stop",
        "info": "After pressing stop, the script will still run the last money farming in full, please wait ten seconds",
        "change_lang": "Switch to Chinese",
    },
}

# Choose the language
lang = "en"  # Change this to "cn" for Chinese


def change_language():
    global lang
    lang = "cn" if lang == "en" else "en"
    update_labels()


def update_labels():
    root.title(lang_dict[lang]["title"])
    label_instructions.config(text=lang_dict[lang]["instructions"])
    label_times.config(text=lang_dict[lang]["times"])
    label_load_time.config(text=lang_dict[lang]["load_time"])
    start_button.config(text=lang_dict[lang]["start"])
    stop_button.config(text=lang_dict[lang]["stop"])
    info_label.config(text=lang_dict[lang]["info"])
    change_lang_button.config(text=lang_dict[lang]["change_lang"])


# Rest of your code...

root = tk.Tk()
customFont = font.Font(family="Microsoft YaHei", size=14)

label_instructions = tk.Label(root, font=customFont)
label_instructions.pack()

label_times = tk.Label(root, font=customFont)
label_times.pack()
entry_times = tk.Entry(root)
entry_times.pack()

label_load_time = tk.Label(root, font=customFont)
label_load_time.pack()
entry_load_time = tk.Entry(root)
entry_load_time.pack()

start_button = tk.Button(root, command=click_start, font=customFont)
start_button.pack()

stop_button = tk.Button(root, command=stop_thread, font=customFont)
stop_button.pack()

info_label = tk.Label(root, font=customFont)
info_label.pack()

change_lang_button = tk.Button(root, command=change_language, font=customFont)
change_lang_button.pack()

update_labels()

root.mainloop()
