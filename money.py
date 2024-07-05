import tkinter as tk
from pynput import keyboard
import time
from tkinter import font
import threading

load_time_default = 6.0


def start_banking(times, load_time):
    # 启动软件后: 把鼠标焦点三秒内移到艾尔登exe窗口
    time.sleep(3)

    control = keyboard.Controller()
    for _ in range(int(times)):
        control.press("w")
        time.sleep(3)
        control.release("w")
        control.press("a")
        time.sleep(0.8)
        control.release("a")
        control.press("w")
        time.sleep(2.25)
        control.release("w")
        # 放战技
        control.press(keyboard.Key.ctrl)
        time.sleep(0.1)
        control.release(keyboard.Key.ctrl)
        time.sleep(2.5)
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


def get_gui_input():
    times = entry_times.get()
    load_time = entry_load_time.get()
    if load_time == "":
        load_time = load_time_default
    thread = threading.Thread(target=start_banking, args=(times, load_time))
    thread.start()


def stop_thread():
    # Stop the thread
    if thread.is_alive():
        # Terminate - may not work if the thread is stuck or not checking
        # its "stopped" status regularly
        thread._stop()


root = tk.Tk()
customFont = font.Font(family="Microsoft YaHei", size=14)
root.title("艾尔登法环python自动化刷钱")
root.geometry("600x400")  # Set the size of the window

instructions = """
1. 在键盘设置中将ctrl设置为战技按键.\n
2. 装备大范围战技,金粪龟等.\n
3. 点击开始以后,把鼠标焦点三秒内移到艾尔登exe窗口.
"""
label_instructions = tk.Label(root, text=instructions, font=customFont)
label_instructions.pack()

label_times = tk.Label(root, text="请输入刷钱次数:", font=customFont)
label_times.pack()
entry_times = tk.Entry(root)
entry_times.pack()

label_load_time = tk.Label(
    root, text="请输入读图时间,默认6秒,下面输入框可以留白:", font=customFont
)
label_load_time.pack()
entry_load_time = tk.Entry(root)
entry_load_time.pack()

button = tk.Button(root, text="开始", command=get_gui_input, font=customFont)
button.pack()

stop_button = tk.Button(root, text="停止", command=stop_thread)
stop_button.pack()


root.mainloop()
