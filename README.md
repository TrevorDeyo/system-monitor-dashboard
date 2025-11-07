# System Monitor Dashboard

A lightweight **full-stack system monitoring application** featuring:

- **FastAPI backend** for real-time system statistics
- A responsive **JavaScript frontend** with sortable tables and live charting
- **PyWebView / PyInstaller support** for native desktop packaging
- Smooth **real-time CPU & memory usage graph**
- Process list with **usage highlighting** for quick identification of heavy tasks

This project demonstrates clean service design, real-time data update handling, UI state management, and executable distribution — suitable as a **portfolio piece** and practical desktop tool.

---

## Features

| Feature | Description |
|--------|-------------|
| **Real-Time Usage Graph** | CPU and RAM usage updated smoothly over time |
| **Sortable Process Table** | Sort by PID, Name, CPU%, or Memory% |
| **Visual Alerts** | High CPU or memory usage processes are highlighted |
| **Browser-Based UI** | Accessible locally from any web browser |
| **Native App Packaging** | Runs as `.exe` on Windows without Python installed |

---

## Tech Stack

| Layer | Technology |
|------|------------|
| Backend API | **FastAPI** |
| System Metrics | **psutil** |
| Frontend | HTML, CSS, JavaScript (no framework required) |
| Charts | **Chart.js** |
| Desktop Packaging | **PyInstaller** / optional **PyWebView** |

---

## Installation

### 1. Clone the repository
```bash
git clone <your_repo_url>
cd system-monitor
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
venv\Scripts\activate    # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

---

## Running the App

```bash
python run_system_monitor.py
```

The dashboard will automatically launch at:

```
http://127.0.0.1:8000
```

---

## Build a Windows Executable (.exe)

```bash
pyinstaller --onefile --add-data "static;static" run_system_monitor.py
```

Built executable will appear in the `dist/` folder.

---

## Why This Project Is Strong for Employers

This project demonstrates:

- Ability to design and implement a full end-to-end application
- Backend API development using FastAPI
- Frontend UI state management with live data updates
- Real-time data visualization using Chart.js
- System-level interaction and performance monitoring via psutil
- Packaging and distribution of a Python application as a standalone executable
