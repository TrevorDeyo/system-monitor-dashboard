from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import psutil

app = FastAPI()

# handles PyInstaller pathing
import os
import sys

def resource_path(relative_path: str):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS  # PyInstaller temp folder
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

static_dir = resource_path("static")

app.mount("/static", StaticFiles(directory=static_dir), name="static")


@app.get("/favicon.ico")
def favicon():
    return FileResponse(resource_path("static/favicon.png"))

@app.get("/")
def read_root():
    return FileResponse(resource_path("static/index.html"))

@app.get("/stats")
def get_stats():
    stats = {
        "cpu_percent": psutil.cpu_percent(interval=0.5),
        "memory_percent": psutil.virtual_memory().percent,
        "total_processes": len(psutil.pids())
    }
    return stats

cpu_count = psutil.cpu_count(logical=True)

@app.get("/processes")
def get_top_processes(limit: int = 10, sort_by: str = "cpu"):
    processes = []

    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            info = proc.info

            # ✅ Skip System Idle Process
            if info.get('pid') == 0 or info.get('name') == "System Idle Process":
                continue

            # Normalize CPU usage like task manager
            raw_cpu = info.get('cpu_percent') or 0.0
            info['cpu_percent'] = round(raw_cpu / cpu_count, 1)
            # rounded because: "memory_percent": 0.000023897951921622
            info['memory_percent'] = round(info.get('memory_percent') or 0.0, 1)
            processes.append(info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    # sort by chosen key
    if sort_by == "memory":
        processes.sort(key=lambda x: x['memory_percent'], reverse=True)
    else:
        processes.sort(key=lambda x: x['cpu_percent'], reverse=True)

    return processes[:limit]