import os
import subprocess
import time

# my programs
from _1_startProgram import start_program
from _2_1_individualMailer import individual_mailer
from _2_2_ExcelMailer import excel_Mailer

program_on = True
os.system("cls")

start_program()
os.system("cls")

while program_on:
    os.system("cls")

    print("Hola!")
    print("Choose one of the actions below(1/2/3):")
    print()

    time.sleep(0.1)
    print("1. Fill the form individually")
    time.sleep(0.1)
    print("2. Fill using excel sheet")
    print()
    time.sleep(0.1)
    print("3. Close the Program")

    value = input("")

    if value == "1":
        individual_mailer()
    elif value == "2":
        excel_Mailer()
    elif value == "3":
        program_on = False
    continue


os.system("cls")
print("Thank you for using the program.")
time.sleep(1)

print("Click enter to exit!")
input()
