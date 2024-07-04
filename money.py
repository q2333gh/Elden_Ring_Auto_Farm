#  pip install pynput
import tkinter as tk
from pynput import keyboard


# 1. 在键盘设置中将ctrl设置为战技按键
# 2. 启动软件后: 把鼠标焦点三秒内移到艾尔登exe窗口
import time
load_time=6.0

def start_program(times, load_time):
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
        # 放战记
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

def get_times():
    times = entry.get()
    start_program(times)


root = tk.Tk()
root.title("艾尔登法环python自动化")
root.geometry("400x200")  # Set the size of the window


instructions = "1. 在键盘设置中将ctrl设置为战技按键\n2. 点击开始以后,把鼠标焦点三秒内移到艾尔登exe窗口"
label_instructions = tk.Label(root, text=instructions)
label_instructions.pack()


label = tk.Label(root, text="请输入刷钱次数:")
label.pack()
entry = tk.Entry(root)
entry.pack()

# label = tk.Label(root, text="请输入读图时间,默认6秒可以不动:")
# label.pack()
# entry = tk.Entry(root)
# entry.pack()

button = tk.Button(root, text="开始", command=get_times)
button.pack()

root.mainloop()
