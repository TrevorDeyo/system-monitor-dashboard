from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import psutil

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name='static')

@app.get("/")
def read_root():
    return FileResponse("static/index.html")

@app.get("/stats")
def get_stats():
    stats = {
        "cpu_percent": psutil.cpu_percent(interval=0.5),
        "memory_percent": psutil.virtual_memory().percent,
        "total_processes": len(psutil.pids())
    }
    return stats

@app.get("/processes")
def get_top_processes(limit: int = 5, sort_by: str = "cpu"):

    processes = []

    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            info = proc.info
            # needed to round so it didn't do this "memory_percent": 0.000023897951921622
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