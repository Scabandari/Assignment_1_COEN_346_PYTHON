
class CommandLine:

    def __init_(self):
        pass
       # self.userFinished = False

    @staticmethod
    def get_user_input(self):
        print("Use this CLI built in Python to run executables in a Linux envrionment.\n"
              " Commands take the form /path/to/exec/name/of/program param1 param2 param.....&\n"
              "Enter 'Z' or 'X' to quit")

        while not self.userFinished:
            print("user~$ ",)
            print("hopefully")