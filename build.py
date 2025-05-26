import os
import subprocess
import sys

def build_exe():
    """Build the Python application to EXE"""
    print("Building Python application to EXE...")
    
    # PyInstaller command
    cmd = [
        sys.executable, "-m", "PyInstaller",
        "--onefile",
        "--console",
        "--name", "MyApp",
        "--distpath", "./dist",
        "--workpath", "./build",
        "app.py"
    ]
    
    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print("Build successful!")
        print(f"EXE location: {os.path.abspath('./dist/MyApp.exe')}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Build failed: {e}")
        print(f"Error output: {e.stderr}")
        return False

def test_exe():
    """Test the built EXE"""
    exe_path = "./dist/MyApp.exe"
    if os.path.exists(exe_path):
        print(f"Testing EXE at: {exe_path}")
        # Note: This will run interactively
        subprocess.run([exe_path])
    else:
        print("EXE not found. Build first.")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        test_exe()
    else:
        build_exe()
