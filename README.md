# 🌐 Network Speed Test – Python GUI Application

A **desktop Network Speed Test application** built using **Python and Tkinter** that measures **download speed, upload speed, and ping** in real time using **Speedtest.net servers**.

This project demonstrates practical use of **GUI programming, multithreading, real-world APIs, and clean application structure**, making it an excellent **portfolio project**.

---

## 🚀 Overview

The application provides a simple and responsive interface to test network performance without freezing the UI.  
All speed tests run in a **background thread**, while the Tkinter main thread safely updates the GUI.

---

## ✨ Key Features

- 📥 **Download Speed Monitoring** (Mbps)
- 📤 **Upload Speed Monitoring** (Mbps)
- ⏱ **Ping / Latency Measurement** (ms)
- 📊 **Live Progress Bars** for visual feedback
- 🧵 **Multithreading** to keep the UI responsive
- 🔄 Periodic updates every **2 seconds**
- 🛡 **Error handling** for unstable or lost connections
- 🪶 Lightweight, clean, and beginner-friendly design

---

## 🖥️ Tech Stack

| Technology | Purpose |
|----------|--------|
| Python 3 | Core programming language |
| Tkinter | GUI framework |
| speedtest-cli | Network speed measurement |
| threading | Background execution |
| time | Controlled update intervals |

---

## 📦 Installation & Usage

### 1️⃣ Clone the repository
```bash
git clone https://github.com/pradeepNath/Network-Speed-Test.git
cd Network_Speed_Test
```

### 2️⃣ Install required dependency
```bash
pip install speedtest-cli
```

### 3️⃣ Run the application
```bash
python Network_Speed_Test.py
```

---

## 🧠 How It Works

- The app connects to the **best available Speedtest.net server**
- Speed tests are executed in a **separate daemon thread**
- GUI updates are safely scheduled using `root.after()`
- Progress bars reflect live speed and ping values
- Measurements refresh at a configurable interval

---

## ⚠️ Notes & Limitations

- Results depend on your **ISP, network stability, and server availability**
- Speed ranges are capped for visualization purposes:
  - Speed: **1000 Mbps**
  - Ping: **500 ms**
- Designed primarily for **learning, practice, and portfolio demonstration**

---

## 🔮 Possible Enhancements

- Class-based (OOP) refactor
- Speed history logging (CSV / SQLite)
- Dark mode UI
- Server location display
- One-click speed test (single run mode)
- Packaging as `.exe` using PyInstaller

---

## 📄 License

This project is **open-source** and free to use for learning, modification, and personal projects.

---

## 👤 Author

**Pradeep Nath**  
Computer Science Student  
Aspiring AI Engineer | Python Developer  

⭐ If you like this project, consider giving it a star!
