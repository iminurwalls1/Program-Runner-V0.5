import os
import socket
import time
import subprocess
from script_runner import run_function

running = True
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
ip = ip_address

print("//Modules loaded//")
print("")
print("")
print("PROGRAM RUNNER VERSION 0.5")
print("")
print("")
print('Type "help" for the list of commands')

def open_microsoft_edge():
    try:
        # Use the 'start' command on Windows to open Microsoft Edge
        subprocess.run(["start", "microsoft-edge:"])

    except Exception as e:
        print("An error occurred while trying to open Microsoft Edge:", str(e))


def log():
    print("")
    a = input("USERNAME: ")
    b = input("PASSWORD: ")
    print("")
    usnme = False  # Initialize the variables
    passw = False
    answr = None
    
    if a == "ADMIN":
        usnme = True
        if b == "DoBoMtC18.06.2010":
            passw = True
        elif b == "I FORGOT THE PASSWORD":
            answr = input("What is the name of the creator's computer user? ")
            if answr == "GAMEING MACHINE":
                passw = True
            else:
                passw = False 
    
    if usnme and passw:
        print("WELCOME, CREATOR")
        return True
    else:
        print("ACCOUNT DOESN'T EXIST, LOGIN FAILED: ERROR2")
        return False

# Open the file in append mode and keep it open for the duration of the program
script_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_directory, "command_log.txt")
log_file = open(file_path, "a")

def main():
    global ip
    global running
    print("")
    a = input("> ")
    
    # Record the command and its status (success or failure)
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    command_status = None

    if a == "help":
        print("\nCOMMANDS:")
        print("help - opens this help window")
        print("exit - closes the runner")
        print("log - log in if you have admin or owner permission")
        print("getMyIp - gets your local (private) IP address and shows it on the screen")
        print("runProgram - runs the imported program")
        print("openBrowser - opens mcrosoft egde")
        print("")
    elif a == "log":
        command_status = log()
    elif a == "exit":
        print("Closing...")
        running = False
    elif a == "getMyIp":
        print("LOCAL IP ADDRESS:", ip)
        command_status = "success"
    elif a == "runProgram":
        run_function()
        command_status = "success"
    elif a == "openBrowser":
        open_microsoft_edge()
    else:
        print(f"Unknown command: {a}")
        command_status = "failure"

    # Log the command along with its status, date, and time
    log_file.write(f"{timestamp} Command: {a} Status: {command_status}\n")
    log_file.flush()  # Flush the file buffer to save the data immediately

if __name__ == "__main__":
    while running:
        main()

# Close the file at the end of the program
log_file.close()
