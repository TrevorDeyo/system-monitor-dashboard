import uvicorn
import webbrowser
import threading
from main import app

def start_server():
    uvicorn.run(app, host="127.0.0.1", port=8000)

if __name__ == "__main__":
    print("==========================================")
    print("   System Monitor Starting...")
    print("   Opening dashboard in your browser...")
    print("   Close this window to exit the app.")
    print("==========================================\n")

    # Start FastAPI server in the background
    server_thread = threading.Thread(target=start_server)
    server_thread.daemon = True
    server_thread.start()

    # Open browser automatically once server starts
    webbrowser.open("http://127.0.0.1:8000", new=1)

    # Keep main thread alive so closing the terminal closes the server
    server_thread.join()
