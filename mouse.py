import win32api, win32con
import time
def click(x,y):
#    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    time.sleep(0.005)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

time.sleep(3)
for x in range(1,5000):
   	click(1000, 500)
   	print(x)
   	time.sleep(0.005)
