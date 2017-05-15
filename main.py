#-A command line interface that takes input statements and if those statements are of the form:
#CLI~$$$ /path/to/program/nameOfProgram param1 param2...&

#then the nameOfProgeram will be treated as an executable which will be started in a new process.
#The program will pass the parameters as arguments to the executable when a new process is created.
#Notice the & symbol which is included if the program is to be run in a background thread. If
#it's not included then the program can run i the forground and the CLI will not be available to
#take any further input until this process has finished it's lifecycle.

import os
import subprocess


userFinished = False

def get_user_input():
    print("\n\nUse this CLI built in Python to run executables in a Linux envrionment.\n"
            " Commands take the form /path/to/exec/name/of/program param1 param2 param.....&\n\n"
            "Enter 'Z' or 'X' to quit")

    global userFinished
    while not userFinished:
      #  print("user~$ ", end='')
        command = input("user~$")
        if command == 'z' or command == 'Z' or command == 'x' or command == 'X':
            userFinished = True
        else:
            tokens = command.split()
            if tokens[-1] == '&':
                del(tokens[-1])
                try:
                   subprocess.Popen(tokens)
                except:
                   print("That's not a proper CLI command")

            else:
                os.system(command)




def main():

    get_user_input()

if __name__ == "__main__":
    main()