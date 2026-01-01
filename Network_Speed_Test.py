"""
Network Speed Test GUI Application

- Measures download, upload speed, and ping
- Uses speedtest.net servers
- Tkinter GUI with real-time progress bars
- Background threading to keep UI responsive
"""


import speedtest
import tkinter as tk
import tkinter.ttk as ttk
import threading
import time


running=False
UPDATE_INTERVAL=2
MAX_SPEED=1000
MAX_PING=500

# -------- Getting Values -------- #
def get_download_speed(sp):
    return sp.download()/1000000

def get_upload_speed(sp):
    return sp.upload()/1000000

def get_ping(sp):
    return sp.results.ping


# -------- Running Speed Test Continuously In  Background Thread ------- #
def run_speed_check():
    global running
    sp=speedtest.Speedtest()
    sp.get_best_server()

    while running:
        try:
            download_speed = get_download_speed(sp)
        except Exception:
            download_speed = 0
        try:
            upload_speed = get_upload_speed(sp)
        except Exception:
            upload_speed = 0
        try:
            ping = get_ping(sp)
        except Exception:
            ping = 0

        root.after(0,update_gui,download_speed,upload_speed,ping)
        time.sleep(UPDATE_INTERVAL)

# --------- Updating Gui --------- #
def update_gui(download_speed,upload_speed,ping):
    download_speed_prog.set(download_speed)
    download_speed_label.config(text=f"{download_speed:.2f} Mbps")

    upload_speed_prog.set(upload_speed)
    upload_speed_label.config(text=f"{upload_speed:.2f} Mbps")

    ping_prog.set(ping)
    ping_speed_label.config(text=f"{ping:.2f} ms")


# --------- Start Speed Thread If Not Already Running --------- #
def start_test():
    global running
    if not running:
        running=True
        threading.Thread(target=run_speed_check,daemon=True).start()

# ---------- Stopping Test ----------- #
def stop_test():
    global running
    running=False

# ---------- GUI ------------ #
root = tk.Tk()
root.title("Network Speed Test")
root.geometry("400x400")
root.resizable(False,False)

download_speed_prog=tk.DoubleVar()
upload_speed_prog=tk.DoubleVar()
ping_prog=tk.DoubleVar()


download_label = tk.LabelFrame(root, text="Download Speed")
download_label.pack(fill="x", padx=5, pady=5)
ttk.Progressbar(download_label,length=250,mode="determinate",maximum=MAX_SPEED,variable=download_speed_prog).pack(pady=5)
download_speed_label=tk.Label(download_label,text="0Mbps")
download_speed_label.pack(pady=5)

upload_label = tk.LabelFrame(root, text="Upload Speed")
upload_label.pack(fill="x", padx=5, pady=5)
ttk.Progressbar(upload_label,length=250,mode="determinate",maximum=MAX_SPEED,variable=upload_speed_prog).pack(pady=5)
upload_speed_label=tk.Label(upload_label,text="0Mbps")
upload_speed_label.pack(pady=5)

ping_label = tk.LabelFrame(root, text="Ping")
ping_label.pack(fill="x", padx=5, pady=5)
ttk.Progressbar(ping_label,length=250,mode="determinate",maximum=MAX_PING,variable=ping_prog).pack(pady=5)
ping_speed_label=tk.Label(ping_label,text="0ms")
ping_speed_label.pack(pady=5)

controller_label = tk.LabelFrame(root, text="Controls")
controller_label.pack(fill="x", padx=5, pady=5)
tk.Button(controller_label,text="Start Test",command=start_test).pack(pady=5)
tk.Button(controller_label,text="Stop Test",command=stop_test).pack(pady=5)
tk.Button(controller_label,text="Exit",command=root.destroy).pack(pady=5)

root.mainloop()