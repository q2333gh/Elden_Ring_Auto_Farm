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
1. 将游戏设置为窗口化.\n
2. 确保键盘按键绑定: ctrl->战技按键, g->地图, f-跳跃, e->确认\n
3. 装备大范围战技,金粪龟等.\n
4. 点击开始以后,把鼠标焦点三秒内移到艾尔登exe窗口并左键点击.
""",
        "times": "请输入刷钱次数:",
        "load_time": "请输入读图时间,默认6秒,下面输入框可以留白:",
        "start": "开始",
        "stop": "停止",
        "info": "按下停止以后,脚本还会完整跑完最后一次刷钱,请等待十秒",
        "change_lang": "English / 中文",
    },
    "en": {
        "title": "Elden Ring Python Automation for Money Farming",
        "instructions": """
1. Set the game to windowed mode.\n
2. Ensure keyboard key bindings: ctrl->combat skill key, g->map, f->jump, e->confirm\n
3. Equip wide-range combat skills, golden dung beetle, etc.\n
4. After clicking start, move the mouse focus to the Elden Ring exe window within three seconds and left-click.
""",
        "times": "Please enter the number of times for money farming:",
        "load_time": "Please enter the loading time, default is 6 seconds, you can leave the following input box blank:",
        "start": "Start",
        "stop": "Stop",
        "info": "After pressing stop, the script will still complete the last money farming run, please wait for ten seconds",
        "change_lang": "English / 中文",
    },
}

# Choose the language
lang = "cn"  # Change this to "cn" for Chinese


def start_banking(times, load_time):
    # 启动软件后: 把鼠标焦点三秒内移到艾尔登exe窗口
    time.sleep(3)

    control = keyboard.Controller()
    for _ in range(int(times)):
        if stop_thread_flag:
            break
        # move
        control.press("w")
        time.sleep(3)
        control.release("w")
        control.press("a")
        time.sleep(0.85)
        control.release("a")
        control.press("w")
        time.sleep(2)
        control.release("w")

        # kill
        control.press(keyboard.Key.ctrl)
        time.sleep(1)
        control.release(keyboard.Key.ctrl)
        time.sleep(1.5)
        control.press(keyboard.Key.ctrl)
        time.sleep(1)
        control.release(keyboard.Key.ctrl)
        time.sleep(6)

        # map
        control.press("g")
        time.sleep(0.1)
        control.release("g")
        time.sleep(0.8)
        control.press("f")
        time.sleep(0.1)
        control.release("f")
        time.sleep(0.1)
        control.press("e")
        time.sleep(0.1)
        control.release("e")
        time.sleep(2.5)
        control.press("e")
        time.sleep(0.1)
        control.release("e")
        # 传送读条加载时间，可以设置稍微久一点
        time.sleep(float(load_time))


def click_start():
    global times, load_time, thread, stop_thread_flag
    stop_thread_flag = False
    times = entry_times.get()
    load_time = entry_load_time.get()
    if load_time == "":
        load_time = load_time_default
    thread = threading.Thread(target=start_banking, args=(times, load_time))
    thread.start()


def stop_thread():
    global stop_thread_flag
    stop_thread_flag = True


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


root = tk.Tk()
customFont = font.Font(family="Microsoft YaHei", size=14)
root.title(lang_dict[lang]["title"])
root.geometry("1000x550")  # Set the size of the window


change_lang_button = tk.Button(
    root, command=change_language, text="English / 中文", font=customFont
)
change_lang_button.pack()


label_instructions = tk.Label(
    root, text=lang_dict[lang]["instructions"], font=customFont
)
label_instructions.pack()

label_times = tk.Label(root, text=lang_dict[lang]["times"], font=customFont)
label_times.pack()
entry_times = tk.Entry(root)
entry_times.pack()

label_load_time = tk.Label(root, text=lang_dict[lang]["load_time"], font=customFont)
label_load_time.pack()
entry_load_time = tk.Entry(root)
entry_load_time.pack()

start_button = tk.Button(
    root, text=lang_dict[lang]["start"], command=click_start, font=customFont
)
start_button.pack()

stop_button = tk.Button(
    root, text=lang_dict[lang]["stop"], command=stop_thread, font=customFont
)
stop_button.pack()

info_label = tk.Label(root, text=lang_dict[lang]["info"], font=customFont)
info_label.pack()

root.mainloop()
