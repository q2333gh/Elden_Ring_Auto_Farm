while 1:
# move
control.press("w")
time.sleep(3)
control.release("w")
control.press("a")
time.sleep(0.8)
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
time.sleep(0.2)
control.release("g")
time.sleep(0.5)
control.press("f")
time.sleep(0.1)
control.release("f")
time.sleep(0.1)
control.press("e")
time.sleep(0.2)
control.release("e")
time.sleep(0.1)
control.press("e")
time.sleep(0.2)
control.release("e")
time.sleep(6.6) # loading