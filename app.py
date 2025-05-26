import os
import sys
import platform
from datetime import datetime

def main():
    print("=" * 50)
    print("Python EXE Test Application")
    print("=" * 50)
    
    print(f"Platform: {platform.system()} {platform.release()}")
    print(f"Architecture: {platform.machine()}")
    print(f"Python Version: {sys.version}")
    print(f"Current Time: {datetime.now()}")
    print(f"Working Directory: {os.getcwd()}")
    
    print("\n" + "=" * 50)
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    
    print(f"\nHello {name}! You are {age} years old.")
    print("This Python script is now running as a Windows EXE!")
    
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()
