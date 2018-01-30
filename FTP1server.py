import sys
# this program, FTP1server.py, serves to verify FTP commands. It does this by taking the commands via stdin and running them through
# a function, verifyCommand(command), that runs the command line thorugh a series of if-else statements that check to see if the
# command and perameters inputed are valid. if they are, the program returns a "Command ok" response, if not, it returns a response that
# notifies the user where the error originates from.


# function that reads standard input lines and passes them to  the verify command method and also both echos the input line and the verification result
def processCommands():
        for line in sys.stdin:
                commandRaw = line.splitlines(keepends = True)
                command = commandRaw[0]
                sys.stdout.write(line)
                print(verifyCommand(command))

# primary function for checking valid commands
def verifyCommand(command):
        unpackedCommand = command.split()
        vCommand = unpackedCommand[0].lower()

        # set of if-else staements that check if the first word in the input is a command and finds what command it is
        if vCommand == "user":
                if len(unpackedCommand) < 2 and command.count(' ') == 0:
                        return "ERROR -- command"
                elif len(unpackedCommand) < 2 and command.count(' ') > 0:
                        return "ERROR -- username"
                if not isAscii(getUserOrPass(command)):
                        return "ERROR -- username"
                elif isAscii(getUserOrPass(command)) and hasCRLF(command):
                        return "Command ok"
                else:
                        return "ERROR -- CRLF"
        elif vCommand == "pass":
                if len(unpackedCommand) < 2 and command.count(' ') == 0:
                        return "ERROR -- command"
                elif len(unpackedCommand) < 2 and command.count(' ') > 0:
                        return "ERROR -- password"
                if not isAscii(getUserOrPass(command)):
                        return "ERROR -- password"
                elif isAscii(getUserOrPass(command)) and hasCRLF(command):
                        return "Command ok"
                else:
                        return "ERROR -- CRLF"
        elif vCommand == "type":
                if len(unpackedCommand) != 2:
					return "ERROR -- command"
                arguement = unpackedCommand[1]
                if len(unpackedCommand) == 2 and hasCRLF(command) and  arguement[0] == 'A' or arguement[0] == 'I':
                        return "Command ok"
                elif len(unpackedCommand) == 2 and arguement[0] != 'A' and arguement[0] != 'I':
                        return "ERROR -- type-code"
                else:
                        return "ERROR -- CRLF"
        elif vCommand == "syst":
                if len(command) != 6:
                        return "ERROR -- CRLF"
                elif hasCRLF(command):
                        return "Command ok"
                else:
                        return "ERROR -- CRLF"
        elif vCommand == "noop":
                if len(command) != 6:
                        return "ERROR -- CRLF"
                elif hasCRLF(command):
                        return "Command ok"
                else:
                        return "ERROR -- CRLF"
		elif vCommand == "quit":
                if len(command) != 6:
                        return "ERROR -- CRLF"
                elif hasCRLF(command):
                        return "Command ok"
                else:
                        return "ERROR -- CRLF"
        else:
                return "ERROR -- command"


# function to find if a string token is made up of only ascii characters
def isAscii(token):
        return all(ord(letter) < 128 for letter in token)

# function to get the username or password from a string arguement representing an FTP command
def getUserOrPass(line):
        firstSpace = line.find(' ')
        username = line[firstSpace:]
        return username

# function to check if the FTP command ends in a proper CRLF
def hasCRLF(token):
        if ord(token[-2]) == 13 and ord(token[-1]) == 10:
                return True
        else:
                return False


processCommands()