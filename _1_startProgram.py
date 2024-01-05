import subprocess
import sys
import time


def start_program():
    print("Hello!!")
    time.sleep(1)
    sys.stdout.write("Welcome to my Cold Emailer.")

    for i in range(2):
        sys.stdout.write(".")
        sys.stdout.flush()  # Force output to the console immediately
        time.sleep(0.7)  # Delay for 1 second
    subprocess.call("cls", shell=True)

    print("Click enter to proceed!")
    input()
    subprocess.call("cls", shell=True)

    # while(program_on):
    #     continue
