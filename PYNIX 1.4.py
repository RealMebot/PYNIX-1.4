import time
import os
import random
from tkinter import E
from tqdm import tqdm
from time import sleep

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

print(" * Serving Flask app 'app'")
time.sleep(0.08)
print(" * Debug mode: off")
time.sleep(0.08)
print("\u001b[31m\u001b[1mWARNING: This LCS is based on SCU-P1150. Do not use it unless you know what you are doing.\u001b[0m")
time.sleep(0.08)
print(" * Running on all addresses (0.0.0.0)")
time.sleep(0.08)
print("\u001b[33m * Running on 127.0.0.1:8080")
time.sleep(0.08)
print(" * Running on 172.18.0.72:8080\u001b[0m")

time.sleep(1)
cls()

print("\u001b[30m\u001b[47m BOOT LOADER SELECTER (BLS)                      ")
time.sleep(0.1)
print("[1] PYNIX 1.4                                    ")
time.sleep(0.1)
print("[2] QUIT                                         \u001b[0m")
time.sleep(0.1)
print("")
a = input()
if a == "QUIT":
  cls()
  quit()
elif a == "PYNIX 1.4":
  pass
elif a == "PY":
  pass
else:
  print(f"COULD NOT FIND {a}")
  quit()
percentage_chance = 0.1
percentage_chance1 = 0.1

if random.random() < percentage_chance:
    print('''        
        ,--.!,
     __/   -*-
   .d00b.  '|`
   MMMMMM          A PROBLEM HAS BEEN DETECTED BY YOUR DEVICE/OS. PYNIX HAS SHUTDOWN UNTIL REBOOT DUE TO THE DATA BEING CORRUPT
   'MMMM' 
-------------------------------------------------------------------------------------------------------------------------------

IF THIS YOUR FIRST TIME SEEING THE SCREEN FOLLOW THE STEPS WRITIEN UNDER THIS MESSAGE:
STEP 1 DO NOT DO ANYTHING THAT MAY CORRUPT OR LOSE YOUR DATA
STEP 2 SHUT DOWN THE SYSTEM ENTIRELY TO KEEP YOUR DATA FURTHER FROM CORRUPTION
STEP 3 TURN ON THE DEVICE/SYSTEM


*** RESIEVE ERROR: 225E1X00 (STARTUP_BOOT_FAILURE)

*** ID: 88x0e44225a ADDRESS: 8424Y6H3AD44 ERROR_STATUS: to_Point/flipcounter''')

    print("YOUR SYSTEM WILL TRY TO BOOT TO PYNIX AGAIN PLEASE WAIT")
    time.sleep(3)
    print("")
    print("FAILED TO BOOT INTO PYNIX!")
    quit()
if random.random() < percentage_chance1:
    print('''        
        ,--.!,
     __/   -*-
   .d00b.  '|`
   MMMMMM          A PROBLEM HAS BEEN DETECTED BY YOUR DEVICE/OS. PYNIX HAS SHUTDOWN UNTIL REBOOT DUE TO THE DATA BEING CORRUPT
   'MMMM' 
-------------------------------------------------------------------------------------------------------------------------------

IF THIS YOUR FIRST TIME SEEING THE SCREEN FOLLOW THE STEPS WRITIEN UNDER THIS MESSAGE:
STEP 1 DO NOT DO ANYTHING THAT MAY CORRUPT OR LOSE YOUR DATA
STEP 2 SHUT DOWN THE SYSTEM ENTIRELY TO KEEP YOUR DATA FURTHER FROM CORRUPTION
STEP 3 TURN ON THE DEVICE/SYSTEM


*** RESIEVE ERROR: 225E2X11 (STARTUP_BOOT_FAILURE)

*** ID: 88x0e44225a ADDRESS: 8432Y6H3XO44 ERROR_STATUS: to_Point/flipcounter''')
    quit()
percentage_chance2 = 0.99
time.sleep(0.3)
print("")
time.sleep(0.3)
print("TYPE 'NEXT' TO CONTINUE")
if random.random() < percentage_chance2:
  x = input()
  
  if x == "adfg":
    print("ENTERING KINTOS")
    time.sleep(0.8)
    cls()

    print("              ©LAZYDEVS 2022-2022              ")
    print("     COPYRIGHT (©) 2022-2022 LAZYDEVS INC.     ")
    print("                                               ")
    jf = input(">~ ")
    if jf == "]_":
      print("""1-10 GOTO USER.INPUT(INTERFACE) = NEW TUI().INPUT
      1-20 GOTO USER.SYSTEM.[INPUT_FUNC.VARUBLE]: = NEW SYSTEM.CORE()
      1-30 GOTO USER.PLFSC.SYSTEM:[PRINT = USING.PRINT_LINE_FROM_SYSTEM_CORE]
      1-40 GOTO USER.DEFF.ARC.STRUCTURE: NEW.[USER_ LL.SYSTEM] 
      1-50 GOTO USER.LBSF.STR: NEW CONNECT:[TABLE]""")
    elif jf == "CM":
      print("             ©CHECKMATE 2022-2022             ")
      print("     COPYRIGHT (©) 2022-2022 LAZYDEVS INC.    ")
      print("                                              ")

      k = input()

      if k == "4BLUESNOW":
        print("INTERNAL / IVSC - VSC = VERTUAL SYSTEM COMMANDERS")
        print("EXTRA / EVSC")
        print("EXTERNAL / EXVSC")

        bl = input()
        if bl == "IVSC":
          print("IVSC CONNECTED")
        elif bl == "EVSC":
          print("EVSC CONNECTED")
        elif bl == "EXVSC":
          print("EXVSC CONNECTED")
        elif bl == "BBLCD":
          print("BBLCD NEEDS TO BE ACTIVATED FROM KUDO")
        else:
          print(f"KINTOS CONNECT NOT FOUND COMMAND ({bl})")
    elif jf == "CNDS":
      print("""\u001b[44m\u001b[37m\u001b[1m                         *** PYNIX 1.3 V1 ***                       \u001b[0m""")
      print("""\u001b[44m\u001b[37m\u001b[1m                      *** 768 KB SYSTEM RAM ***                     """)
      print("                        ©LAZYDEVS 2022-2022                         ")
      print("               COPYRIGHT (©) 2022-2022 LAZYDEVS INC.                ")
      print("                                                                    \u001b[0m")
    else:
      print(f"KINTOS GOTO NOT FOUND COMMAND ({jf})")
    
    
  elif x == "SKIP":
    pass
  elif x == "NEXT":
    pass
  else:
    print("KERNEL 0x001 OPERATOR. ***0x0000000")
    quit()

#memory


cls()

time.sleep(1.5)
print("")
print("Would you like to download PyNix 1.4")

startinput = input()
if startinput == "YES":
  pass
elif startinput == "NO":
  quit()
elif startinput == "Y":
  pass
elif startinput == "N":
  quit()
else:
  print(f"ERROR DEFF... {startinput}")
  quit()
for i in tqdm(range(0, 100), disable = False,
               desc ="\u001b[37mDOWNLOADING…"):
    sleep(.001)
for i in tqdm(range(0, 100), disable = False,
               desc ="\u001b[37mEXECUTING…    "):
    sleep(.001)

for i in tqdm(range(0, 100), disable=False, 
              desc="\u001b[37mMEMORYCHECK…"):
    sleep(.001)

for i in tqdm(range(0, 100), disable=False,
              desc="\u001b[37mPROSESSORTESTING…"):
    sleep(.001)

print("Memory Check Complete! ( all 388000mb [\u001b[32mOK\u001b[37m] )")
time.sleep(0.1)
print("Memory Check ReCount Complete! ( all 388000kb [\u001b[32mOK\u001b[37m] )")
time.sleep(0.1)
print("Memory Check BackUp Complete! ( all 200kb [\u001b[32mOK\u001b[37m] )")
time.sleep(0.1)
print("Memory Check BackUp ReCount Complete! ( all 200kb [\u001b[32mOK\u001b[37m] )")
time.sleep(0.1)
print("Memory Check Complete! ( cashed: 8000kb est )")

#prosessor
time.sleep(0.3)
print("")
time.sleep(0.1)
print("Prosessor Testing Complete! (8 cores: 400mhz, 4 thread [\u001b[32mOK\u001b[37m] )")
time.sleep(0.1)
print("Prosessor Testing Complete! (6 cores: 350mhz, 4 thread [\u001b[32mOK\u001b[37m] )")
time.sleep(0.1)
print("Prosessor Testing Complete! (4 cores: 200mhz, 2 thread [\u001b[32mOK\u001b[37m] )")
time.sleep(0.1)
print("Prosessor Testing Complete! (2 cores: 100mhz, 2 thread [\u001b[32mOK\u001b[37m] )")
time.sleep(0.1)
print("")
time.sleep(0.1)
print("Prosessor Testing Complete! (Bits: 24bit max)")
time.sleep(0.1)
print("Prosessor Testing Complete! (architecture: Zent 2)")
time.sleep(0.1)
print("")
time.sleep(0.1)
print("Prosessor       [\u001b[32m\u001b[4mOK\u001b[0m]")
time.sleep(0.1)
print("Memory          [\u001b[32m\u001b[4mOK\u001b[0m]")
time.sleep(0.1)
print("BackUp Test     [\u001b[32m\u001b[4mOK\u001b[0m]")
time.sleep(0.1)
print("Test            [\u001b[32m\u001b[4mOK\u001b[0m]")
time.sleep(0.1)
print("IDE CONNECT     [\u001b[32m\u001b[4mOK\u001b[0m]")
time.sleep(0.1)
print("IDE OUTPUT      [\u001b[32m\u001b[4mOK\u001b[0m]")
time.sleep(0.1)
print("IDE STARTUP     [\u001b[32m\u001b[4mOK\u001b[0m]")
time.sleep(0.1)
print("IDE CORE        [\u001b[32m\u001b[4mOK\u001b[0m]")
time.sleep(0.1)
print("IDE SRFC        [\u001b[32m\u001b[4mOK\u001b[0m]")
time.sleep(0.1)
print("IDE CSFS        [\u001b[32m\u001b[4mOK\u001b[0m]")
time.sleep(0.1)
print("IDE RFSB        [\u001b[32m\u001b[4mOK\u001b[0m]")
time.sleep(0.1)
print("")
time.sleep(0.1)
print("LODAING APPLICATIONS")
time.sleep(0.1)
print("")
time.sleep(0.1)
print("/S/data/collection  COLLECTOR       0x00fna12bc3")
time.sleep(0.1)
print("/S/data/casher      datacasher      0x00bsg32be0")
time.sleep(0.1)
print("/S/data/trasher     datatrasher     0x00fy87e8df")
time.sleep(0.1)
print("/S/data/retriever   dataretriever   0x00h99a18t0")
time.sleep(0.1)
print("/S/data/sender      datarsender     0x00c7e8b1df")
time.sleep(0.1)
print("/S/dcac/collection  COLLECTOR       0x00fna12bc3")
time.sleep(0.1)
print("/S/dcac/casher      dcaccasher      0x00wdj9230t")
time.sleep(0.1)
print("/S/dcac/trasher     dcactrasher     0x00s4b82gs1")
time.sleep(0.1)
print("/S/dcac/retriever   dcacretriever   0x00sn28s829")
time.sleep(0.1)
print("/S/dcac/sender      dcacrsender     0x00c0ff41ee")
time.sleep(0.1)
print("")

time.sleep(1)

cls()
time.sleep(0.1)
print("RUNNING PYNIX 1.4")
time.sleep(0.1)
print("COPYRIGHT (C) 2022-2022, LazyDevs")
time.sleep(0.6)

print("""
oooooooooo  ooooo  oooo oooo   oooo ooooo ooooo  oooo           oo              o88   
 888    888   888  88    8888o  88   888    888  88           o888            o8888   
 888oooo88      888      88 888o88   888      888              888          o88 888   
 888            888      88   8888   888     88 888            888   ooo  o888oo888oo 
o888o          o888o    o88o    88  o888o o88o  o888o         o888o  888       o888o  
                                                                                    """)
print("YOUR VERSION OF PYNIX IS NOT ACTIVATED (TO ACTIVATE TYPE 'ACTIVATE') YOU MAY NEED TO DO THIS EVERY TIME YOU BOOT THE SYSTEM")
while True:
  e = input("\u001b[30m[\u001b[37mPYNIX1.4/USER ~ ")
  if e == "RF":
    for i in tqdm(range(0, 100), disable = False,
                 desc ="\u001b[37mOPENING…    "):
      sleep(.001)
    print("\u001b[34m                    ")
    time.sleep(0.1)
    print("\u001b[34m                    ")
    time.sleep(0.1)
    print("\u001b[34m                    ")
    time.sleep(0.1)
    print("\u001b[34m                    ")
    time.sleep(0.1)
    print("\u001b[34m                    ")
    time.sleep(0.1)
    print("\u001b[34m                    ")
    time.sleep(0.1)
    print("\u001b[34m                    ")
    time.sleep(0.1)
    print("\u001b[34m                    ")
    time.sleep(0.1)
    print("\u001b[34m                    ")
    time.sleep(0.1)
    print("\u001b[34m                    ")
    time.sleep(0.1)
    print("\u001b[34m                    ")
    time.sleep(0.1)
    print("\u001b[34m                    ")
    time.sleep(0.1)
    print("\u001b[34m                    ")
    time.sleep(0.1)
    print("\u001b[34m                    ")
    time.sleep(0.1)
    print("\u001b[34m                    ")
    time.sleep(0.1)
    print("\u001b[34m                    ")
    time.sleep(0.1)
    print("\u001b[34m                    ")
    time.sleep(0.1)
    print("\u001b[34m                    ")
    time.sleep(0.1)
    print("\u001b[34m                    ")
    time.sleep(0.1)
    print("\u001b[34m                    ")
    time.sleep(0.1)
    print("\u001b[34m                    ")
    time.sleep(0.1)
    print("\u001b[34m                    ")
    time.sleep(0.1)
    print("\u001b[34m                    ")
    time.sleep(0.1)
    print("\u001b[34m                    ")
    time.sleep(0.1)
    cls()
  elif e == "EGG":
    print("BOOTING INTO EGG")
    for i in tqdm(range(0, 100), disable = False,
                 desc ="\u001b[37mOPENING…    "):
      sleep(.001)

    cls()
    time.sleep(1)

    print("EGG")
    quit()

  elif e == "CALC":
    print("BOOTING INTO CALC")
    for i in tqdm(range(0, 100), disable = False,
                 desc ="\u001b[37mOPENING…    "):
      sleep(.001)
    def add(a, b):
        return a + b

    def subtract(a, b):
        return a - b

    def multiply(a, b):
        return a * b

    def divide(a, b):
        return a / b

    print("Select operation.")
    print("[1]Add")
    print("[2]Subtract")
    print("[3]Multiply")
    print("[4]Divide")

    while True:
        choice = input("Enter choice (Add/Subtract/Multiply/Divide): ")

        if choice in ("Add", "Subtract", "Multiply", "Divide"):
            number_1 = float(input("Enter first number: "))
            number_2 = float(input("Enter second number: "))

            if choice == "Add":
                print(number_1, "+", number_2, "=", number_1 + number_2)

            elif choice == "Subtract":
                print(number_1, "-", number_2, "=", number_1 - number_2)

            elif choice == "Multiply":
                print(number_1, "*", number_2, "=", number_1 * number_2)

            elif choice == "Divide":
                print(number_1, "/", number_2, "=", number_1 / number_2)

            else:
              print(f"COULD NOT FIND {choice}")
        else:
            print("Invalid Input")
  elif e == "TEXT EDITOR":
    print("""| FILE	| HELP |""")
    DNA = input()
    if DNA == "FILE":
      print("")
      print("HELP")
      print("LANG")
      print("VERSION")
      print("COPYRIGHT")
      print("")
      ND = input()
      if ND == "HELP":
        print("")
        print("Welcome to the PyNix 1.4 Text Editor")
        print("This is a area where you can do what ever you can think of (INCLUDING) ASCII ART (Unicode Included)")
        print("So far there is only 1 Language in the text editor (Coding)")
        print("If you want to start writing just say [Start] with the brackets")
        print("")
      elif ND == "LANG":
        print("You are right now writing in NRT or Normal Rich Text")

      elif ND == "VERSION":
        print("VERSION: 1.00")

      elif ND == "COPYRIGHT":
        print("""                                    ©LazyDevs .INC                                    
        ©LazyDevs .INC 2022-2022 COPYRIGHT AND INFRINGEMENT - LICENCED BY COSMOS .INC
        ===============================================================================================
        THIS IS NOT A REGULAR DOCUMENT AND INSTEAD A COPYRIGHT INFRINGEMENT DOCUMENT / COPYRIGHT SEAL
        """)
      else:
        print(f"!THERE IS NO SUCH THING AS {ND}!")
    elif DNA == "HELP":
      print("")
      print("Welcome to the PyNix 1.4 Text Editor")
      print("This is a area where you can do what ever you can think of (INCLUDING) ASCII ART (Unicode Included)")
      print("So far there is only 1 Language in the text editor (Coding)")
      print("If you want to start writing just say [Start] with the brackets")

    elif DNA == "[START]":
      print("")
      while True:
        input()
  elif e == "HELP":
    print(""" __          ________ _      _____ ____  __  __ ______   _______ ____    _______     ___   _ _______   __  __       _  _                                          
 \ \        / /  ____| |    / ____/ __ \|  \/  |  ____| |__   __/ __ \  |  __ \ \   / / \ | |_   _\ \ / / /_ |     | || |                                         
  \ \  /\  / /| |__  | |   | |   | |  | | \  / | |__       | | | |  | | | |__) \ \_/ /|  \| | | |  \ V /   | |     | || |_                                        
   \ \/  \/ / |  __| | |   | |   | |  | | |\/| |  __|      | | | |  | | |  ___/ \   / | . ` | | |   > <    | |     |__   _|                                       
    \  /\  /  | |____| |___| |___| |__| | |  | | |____     | | | |__| | | |      | |  | |\  |_| |_ / . \   | |  _     | |                                         
    _\/__\/_  |______|______\_____\____/|_|  |_|______|___ |_|_ \____/  |_|      |_|  |_| \_|_____/_/ \_\_ |_|_(_)  __|_|___      _______    _____ _   _  _____   
   /  ____  \|__ \ / _ \__ \|__ \           |__ \ / _ \__ \|__ \         | |        /\    |___  /\ \   / /  |  __ \|  ____\ \    / / ____|  |_   _| \ | |/ ____|  
  /  / ___|  \  ) | | | | ) |  ) |  ______     ) | | | | ) |  ) |        | |       /  \      / /  \ \_/ /   | |  | | |__   \ \  / / (___      | | |  \| | |       
 |  | |       |/ /| | | |/ /  / /  |______|   / /| | | |/ /  / /         | |      / /\ \    / /    \   /    | |  | |  __|   \ \/ / \___ \     | | | . ` | |       
 |  | |___    / /_| |_| / /_ / /_            / /_| |_| / /_ / /_         | |____ / ____ \  / /__    | |     | |__| | |____   \  /  ____) |   _| |_| |\  | |____ _ 
  \  \____|  /____|\___/____|____|          |____|\___/____|____|        |______/_/    \_\/_____|   |_|     |_____/|______|   \/  |_____/   |_____|_| \_|\_____(_)
   \________/                                                                                                                                                     
                                                                                                                                                                  """)
    print("RF -refreshes the os")
    print("CALC -calculator tool")
    print("TEXT EDITOR -text editor tool")
    print("sys info -gives info about the computer / device")
    print("sys help -help understand with the names / device specs")
    print("sys compatibility -help find if your system is compatible tool")
    print("KUDO RECOVERY -help find / recover data")
    print("DEBUG -#################################################################")
    print("KINTIC -system tester")
    print("PROTO -system tester")
    print("]? PTR -pynix base")
    
  elif e == "KUDO RECOVERY":
    A = input()
    if A == "tt_format.disk":
            for i in tqdm(range(0, 100), disable=False,
                          desc="\u001b[37mFORMATTING…"):
                sleep(.1)
            time.sleep(0.1)
            print("IDE CONNECT     [\u001b[32m\u001b[4mOK\u001b[0m]")
            time.sleep(0.1)
            print("IDE OUTPUT      [\u001b[32m\u001b[4mOK\u001b[0m]")
            time.sleep(0.1)
            print("IDE STARTUP     [\u001b[32m\u001b[4mOK\u001b[0m]")
            time.sleep(0.1)
            print("IDE CORE        [\u001b[32m\u001b[4mOK\u001b[0m]")
            time.sleep(0.1)
            print("IDE SRFC        [\u001b[31m\u001b[4mNONE\u001b[0m]")
            time.sleep(0.1)
            print("IDE CSFS        [\u001b[31m\u001b[4mNONE\u001b[0m]")
            time.sleep(0.1)
            print("IDE RFSB        [\u001b[32m\u001b[4mOK\u001b[0m]")
            time.sleep(0.1)
            print("DISKFORMAT.exe COMPLETE!")
    elif A == "tt_usertag":
          
          for i in tqdm(range(0, 100), disable=False,
                        desc="\u001b[37mCHECKINGFORMATTING…"):
              sleep(.1)
          print("DISKFORMATVERIFY.exe COMPLETE!")
          time.sleep(0.1)
          print("DISKFORMATVERIFY.exe VERIFICATION SUCCESS")
    elif A == "tt_cso":
          print("THE 'COMMAND SHELL OPERATOR' IS STILL IN DEVELOPMENT")
        
    elif A == "tt_ral":
          print("RAUS - USA")

          print("")
          print("-----------------OTHER REGION AREA LOCATORS-----------------")
          print("RAEU - EU")
          print("RAGL - GLOBAL")


    elif A == "tt_reinstall":
          print("REINSTALLING (AFTER THIS MESSAGE WILL BE A BLANK SCREEN AFTER THE BLANK SCREEN TRUN ON THE DEVICE)")
          time.sleep(4)
          cls()

          time.sleep(1)
          quit()
    elif A == "tt_BBLCD":
          print("BBLCD ACTIVATED")
    else:
      print(f"NO SUCH THING AS {A}")
  elif e == "KINTIC":
    for i in tqdm(range(0, 100), disable = False,
                 desc ="\u001b[37mOPENING…    "):
      sleep(.001)
    cls()
    print("\u001b[32m*** PYNIX BASIC 1.0***")
    print("")
    print("READY.")

    print("?SYNTAX \u001b[37m[\u001b[32mOK\u001b[37m]\u001b[32m 640K")
  elif e == "]? PTR":
    fx = input("] ~$ ")
    if fx == "? 10 GOTO SE/ tps":
      o = input()
      time.sleep(0.3)

      print("                     ")
      print(f'10 GOTO -= PRINTED "{o.upper()}"')
    elif fx == "? 10 GOTO SE/ tps un":
      o = input()
      time.sleep(0.3)

      print("                     ")
      print(f'10 GOTO -= PRINTED "{o.lower()}"')
    else:
      print("NO SUCH COMMAND")
  elif e == "PROTO":
    print("""<stringdata>APIDOCK<stringdata>
      <stringdata>APIDOCK<stringdata>
      <stringdata>APIDATA<stringdata>
      <stringdata>APIDATE<stringdata>
      <stringdata>APICLOCK<stringdata>
      <stringdata>APICHECK<stringdata>
      <stringdata>APISCAN<stringdata>
      <stringdata>APIVERIFY<stringdata>
      <stringdata>APILOCKER<stringdata>
      <stringdata>APIUNLOCKER<stringdata>
      <stringdata>APISOT1<stringdata>
      <stringdata>APISOT2<stringdata>
      <stringdata>APISOT3<stringdata>""")
  elif e == "sys info":
    print("""component speed:
CPU 1: ION 2 1100U (2 threads, 2 cores, 200mhz) CPU ARCHITECTURE: Zent 2 (1000nm)
CPU 2: ION 2 1100U (2 threads, 2 cores, 200mhz) CPU ARCHITECTURE: Zent 2 (1000nm)
RAM: ZENT 3 1550H (210mhz, 256mb)
RAM 2: ZENT 3 1550H (210mhz, 100mb)
IRAM: ZENT 3 1550H (210mhz, 32mb)
GRAPHICS: ZNG 2 5550H (188mhz, 180mb)
GRAPHICS 2: ZNG 2 5440U (172mhz, 180mb)
STORAGE: XENT 1 3225H (256mb) hdd
ISTORAGE: XENT I1 45520H (180mb) hdd

total:
400mhz clock speed, 4 cores, 4 threads, 1000nm
388mb ram
360mhz sdr graphics card clock, 360mb support
436mb storage""")  
  elif e == "sys help":
    print("""ram

ROM (can not be written in/ can't be used)
RAM (can be written in/ can be used)
RAM SRAM (user ram)
RAM DRAM (system ram)
RAM DRAM SDRAM (single contoller for the entier board)
RAM DRAM RDRAM (multi contollers for the each chip on the board)
RAM DRAM DDR (faster SDRAM but acts like RDRAM)
RAM DRAM FPM DRAM (faster DRAM but less power)
RAM DRAM CDRAM (faster faster DRAM)
RAM DRAM EDO DRAM (Early faster FPM DRAM)
RAM DRAM DDR ECC RAM (DDR RAM which detects and corrects errors)
RAM DRAM SDRAM GDDR (double data rate then DDR)

cashe (stored data for later use by user)

video ram

SDR (the first type of video ram ever)
DDR (the current and high preformance type of video ram)
GDDR (the current and best preformance type of video ram)

storage
bit

Bit
Kilobit
Kibibit
Megabit
Mebibit
Gigabit
Gibibit
Terabit
Tebibit
Petabit
Pebibit
Exabit
Exbibit
Zettabit
Zebibit
Yottabit
Yobibit

byte

Byte
Kilobyte
Kibibyte
Megabyte
Mebibyte
Gigabyte
Gibibyte
Terabyte
Tebibyte
Petabyte
Pebibyte
Exabyte
Exbibyte
Zettabyte
Zebibyte
Yottabyte
Yobibyte""")
  elif e == "sys compatibility":
    print("""CPU:
1-4 gen: 1000, 1100, 1120, 1144, 1150, 1170, 1200, 1220, 1240, 1300, 1330, 1340, 1350, 1420, 1422, 1433, 1444, 1450, 1520, 1570, 1600, 1650, 1677, 1780, 1840, 1866, 1880, 1900,
4-7 gen: 2000, 2100, 2200, 2330, 2400, 2440, 2500, 2550, 2700, 3000, 3400, 3620, 3800, 4000, 4100, 4200, 4220, 4300, 4400, 4500, 4700, 4850, 5000, 5280, 5580, 5800, 6000, 7000,
7-10 gen: 8000, 9000, 11000, 11500, 11540, 11650, 11700, 12100, 12133, 12150, 12170, 12200, 12500 , 12550, 12400

RAM:
1-5 gen: 1550H, 1550U, 1550I, 1225, 1220, 1220U, 1220H, 1440, 1450H, 1450U

GRAPHICS:
5550H, 5440U
1-4 gen: 1000, 1100, 1120, 1144, 1150, 1170, 1200, 1220, 1240, 1300, 1330, 1340, 1350, 1420, 1422, 1433, 1444, 1450, 1520, 1570, 1600, 1650, 1677, 1780, 1840, 1866, 1880, 1900,
4-7 gen: 2000, 2100, 2200, 2330, 2400, 2440, 2500, 2550, 2700, 3000, 3400, 3620, 3800, 4000, 4100, 4200, 4220, 4300, 4400, 4500, 4700, 4850, 5000, 5280, 5580, 5800, 6000, 7000,
7-10 gen: 8000, 9000, 11000, 11500, 11540, 11650, 11700, 12100, 12133, 12150, 12170, 12200, 12500 , 12550, 12400""")
  elif e == "REDOX":
    print("\u001b[34m\u001b[47m\u001b[1m| VERSION BUILD: 1.4 1h2c0 | TINKER: SCU-P1150 | CPU: 400mhz | RAM: 388mb | \u001b[0m")
    print("\u001b[32m*** REDOX MODE VERSION 0.99 2022-2022 ***")
    print("")

    f = input()
    if f == "FF01 PRINT":
      wi = input()
      print("")
      print(wi)
    elif f == "FF02 CHAR":
      print("abcdefghijklmnopqrstuvwyxzABCDEFGHIJKLMNOPQRSTUVWYXZ0123456789")
      print("""~!@#$%*()[]{}\|;:'"<>,./?""")
    elif f == "FF03 RART":
      print("\u001b[37mFF01\u001b[32m. 01 02 03 04 05 06 07 08 09")
      print("\u001b[37mFF02\u001b[32m. A1 A2 A3 A4 A5 A6 A7 A8 A9")
      print("\u001b[37mFF03\u001b[32m. B1 B2 B3 B4 B5 B6 B7 B8 B9")
      print("\u001b[37mFF04\u001b[32m. C1 C2 C3 C4 C5 C6 C7 C8 C9")
      print("\u001b[37mFF05\u001b[32m. D1 D2 D3 D4 D5 D6 D7 D8 D9")
      print("\u001b[37mFF06\u001b[32m. E1 E2 E3 E4 E5 E6 E7 E8 E9")
      print("\u001b[37mFF07\u001b[32m. F1 F2 F3 F4 F5 F6 F7 F8 F9")
    elif f == "FF04 SPEC":
      print("""CPU 1: ION 2 1100U (2 threads, 2 cores, 200mhz) CPU ARCHITECTURE: Zent 2 (1000nm)
CPU 2: ION 2 1100U (2 threads, 2 cores, 200mhz) CPU ARCHITECTURE: Zent 2 (1000nm)
RAM: ZENT 3 1550H (210mhz, 256mb)
RAM 2: ZENT 3 1550H (210mhz, 100mb)
IRAM: ZENT 3 1550H (210mhz, 32mb)
GRAPHICS: ZNG 2 5550H (188mhz, 180mb)
GRAPHICS 2: ZNG 2 5440U (172mhz, 180mb)
STORAGE: XENT 1 3225H (256mb) hdd
ISTORAGE: XENT I1 45520H (180mb) hdd

TOTAL:
400MHZ CLOCK SPEED, 4 CORES, 4 CORES, 1000NM
388MB RAM 210MHZ
360MHZ SDR GRAPHICS CARD CLOCK, 360MB SUPPORT
436MB STORAGE""")
    elif f == "FF05 EOI.AFFF R1112":
      cls()
      print('|')
      time.sleep(0.09)
      cls()
      print("/")
      time.sleep(0.09)
      cls()
      print("-")
      time.sleep(0.09)
      cls()
      print("\ ")
      time.sleep(0.09)
      cls()
      print("-")
      time.sleep(0.09)
      cls()
      print("|")
      time.sleep(0.09)
      cls()
      print('|')
      time.sleep(0.09)
      cls()
      print("/")
      time.sleep(0.09)
      cls()
      print("-")
      time.sleep(0.09)
      cls()
      print("\ ")
      time.sleep(0.09)
      cls()
      print("-")
      time.sleep(0.09)
      cls()
      print("|")
      time.sleep(0.09)
      cls()
      print('|')
      time.sleep(0.09)
      cls()
      print("/")
      time.sleep(0.09)
      cls()
      print("-")
      time.sleep(0.09)
      cls()
      print("\ ")
      time.sleep(0.09)
      cls()
      print("-")
      time.sleep(0.09)
      cls()
      print("|")
      time.sleep(0.09)
      cls()
      print('|')
      time.sleep(0.09)
      cls()
      print("/")
      time.sleep(0.09)
      cls()
      print("-")
      time.sleep(0.09)
      cls()
      print("\ ")
      time.sleep(0.09)
      cls()
      print("-")
      time.sleep(0.09)
      cls()
      print("|")
      time.sleep(0.09)
      cls()
      print('|')
      time.sleep(0.09)
      cls()
      print("/")
      time.sleep(0.09)
      cls()
      print("-")
      time.sleep(0.09)
      cls()
      print("\ ")
      time.sleep(0.09)
      cls()
      print("-")
      time.sleep(0.09)
      cls()
      print("|")
      time.sleep(0.09)
      cls()
      print('|')
      time.sleep(0.09)
      cls()
      print("/")
      time.sleep(0.09)
      cls()
      print("-")
      time.sleep(0.09)
      cls()
      print("\ ")
      time.sleep(0.09)
      cls()
      print("-")
      time.sleep(0.09)
      cls()
      print("|")
      time.sleep(0.09)
      cls()
      while True:
        f1 = input(">")
    elif f == "FF06 PEEK":
      print("001-255 SET PEEK (44523K)")
    elif f == "FF07 SETUP":
      cls()
      print('|')
      time.sleep(0.09)
      cls()
      print("/")
      time.sleep(0.09)
      cls()
      print("-")
      time.sleep(0.09)
      cls()
      print("\ ")
      time.sleep(0.09)
      cls()
      print("-")
      time.sleep(0.09)
      cls()
      print("|")
      time.sleep(0.09)
      cls()
      print('|')
      time.sleep(0.09)
      cls()
      print("/")
      time.sleep(0.09)
      cls()
      print("-")
      time.sleep(0.09)
      cls()
      print("\ ")
      time.sleep(0.09)
      cls()
      print("-")
      time.sleep(0.09)
      cls()
      print("|")
      time.sleep(0.09)
      cls()
      print('|')
      time.sleep(0.09)
      cls()
      print("/")
      time.sleep(0.09)
      cls()
      print("-")
      time.sleep(0.09)
      cls()
      print("\ ")
      time.sleep(0.09)
      cls()
      print("-")
      time.sleep(0.09)
      cls()
      print("|")
      time.sleep(0.09)
      cls()
      print('|')
      time.sleep(0.09)
      cls()
      print("/")
      time.sleep(0.09)
      cls()
      print("-")
      time.sleep(0.09)
      cls()
      print("\ ")
      time.sleep(0.09)
      cls()
      print("-")
      time.sleep(0.09)
      cls()
      print("|")
      time.sleep(0.09)
      cls()
      print('|')
      time.sleep(0.09)
      cls()
      print("/")
      time.sleep(0.09)
      cls()
      print("-")
      time.sleep(0.09)
      cls()
      print("\ ")
      time.sleep(0.09)
      cls()
      print("-")
      time.sleep(0.09)
      cls()
      print("|")
      time.sleep(0.09)
      cls()
      print('|')
      time.sleep(0.09)
      cls()
      print("/")
      time.sleep(0.09)
      cls()
      print("-")
      time.sleep(0.09)
      cls()
      print("\ ")
      time.sleep(0.09)
      cls()
      print("-")
      time.sleep(0.09)
      cls()
      print("|")
      time.sleep(0.09)
      cls()
      print("Hello, User_")
      time.sleep(0.3)
      cls()
      print("Hello, User")
      time.sleep(0.3)
      cls()
      print("Hello, User_")
      time.sleep(0.3)
      cls()
      print("Hello, User")
      time.sleep(0.3)
      cls()
      print("Hello, User_")
      time.sleep(0.3)
      cls()
      print("Hello, User")
      time.sleep(0.3)
      cls()
      print("Hello, User_")
      time.sleep(0.3)
      cls()
      print("Hello, User")
      time.sleep(0.3)
      cls()
      print("Hello, User_")
      time.sleep(0.3)
      cls()
      print("Hello, User")
      time.sleep(0.3)
      cls()
      print("Hello, User_")
      time.sleep(0.3)
      cls()
      print("Hello, User")
      time.sleep(0.3)
      cls()
      print("Hello, User_")
      time.sleep(0.3)
      cls()
      print("Hello, User")
      time.sleep(0.3)
      cls()
      print("Hello, User_")
      time.sleep(0.3)
      cls()
      print("Hello, User")
      time.sleep(0.3)
      cls()
      print("Hello, User_")
      time.sleep(0.3)
      cls()
      print("Hello, User")
      time.sleep(0.3)
      cls()
      print("Hello, User_")
      time.sleep(0.3)
      cls()
      print("Hello, User")
      time.sleep(0.3)
      cls()
      print("Hello, User_")
      time.sleep(0.3)
      cls()
      print("Hello, User")
      time.sleep(0.3)
      cls()
      print("Hello, User_")
      time.sleep(0.3)
      cls()
      print("Hello, User")
      time.sleep(0.3)
      print("""AppType: AppType::kProfile $LDefault $LSystem
AppName: AppName:: Application.PyNix
AppData: AppData:: 8yoh6n550idmy35imw
AppID: AppID:: h6dn3unpu77r8a1cx63n91sftd36jdw2

App: net —> core.pynix_1.4""")
      time.sleep(0.1)
      cls()
      print("First lets set you a name:")
      xe = input("USERNAME: ")
      xr = input("PASSWORD: ")
      time.sleep(0.5)
      cls()
      print("Your all done and setup!")
      print("if you want to view your username & password say FF08 VUAP")
      print("if you want to change your username & password say FF09 CUAP")
    elif f == "FF08 VUAP":
      print("USERNAME: ", xe)
      print("PASSWORD: ", xr)
      ew = input()
      if ew == "NEXT":
        cls()
      elif ew == "EXIT":
        cls()
      else:
        print("NOT A COMMAND")
    elif f == "FF09 CUAP":
      xe1 = input("NEW USERNAME: ")
      xr1 = input("NEW PASSWORD: ")

    elif f == "FF10 NVUAP":
      print("USERNAME: ", xe1)
      print("PASSWORD: ", xr1)
  elif e == "TIME":
      print("SHOWING TIME")
      for i in tqdm(range(0, 100), disable = False,
                   desc ="\u001b[37mCALCULATING…    "):
        sleep(.001)
      import datetime
      now = datetime.datetime.now()
      print (now.strftime("%Y-%m-%d %H:%M:%S"))
  elif e == "TEST_ controller":
        print("$include /:io/ :/root/ <data>")
        print("$include /:io/ :/root/ <string>")
        print("$include /:io/ :/root/ <tag>")
        print("$include /:io/ :/root/ <id>")
        print("$include /:io/ :/root/ <object>")
        print("$include /:io/ :/root/ <referance>")
        print("$include /:io/ :/root/ <deffine>")
        print("$include /:io/ :/root/ <local>")
        print("$include /:io/ :/root/ <array>")
        print("$include /:io/ :/root/ <boolean>")
        print("$include /:io/ :/root/ <int>")
        print("$include /:io/ :/root/ <float>")
        print("$include /:io/ :/root/ <bundle>")
        print("$include /:io/ :/root/ <path>")
        print("$include /:io/ :/root/ <if>")
        print("$include /:io/ :/root/ <then>")
        print("$include /:io/ :/root/ <else>")
        print("$include /:io/ :/root/ <or>")
        print("$include /:io/ :/root/ <start>")
        print("$include /:io/ :/root/ <end>")
        print("$include /:io/ :/root/ <pause>")
        print("$include /:io/ :/root/ <add>")
        print("$include /:io/ :/root/ <subtract>")
        print("$include /:io/ :/root/ <multiply>")
        print("$include /:io/ :/root/ <divide>")
        print("$include /:io/ :/root/ <root>")
        print("\u001b[30m[\u001b[32mOK\u001b[30m]\u001b[34m system:install/boot/install_pyro1.hydra:")
        print("\u001b[30m[\u001b[32mOK\u001b[30m]\u001b[34m system:update/boot/install_pyro1.1.hydra:")
        print("\u001b[30m[\u001b[32mOK\u001b[30m]\u001b[34m system:update/boot/install_pyro1.1.002.hydra:")
        print("\u001b[30m[\u001b[32mOK\u001b[30m]\u001b[34m system:update/boot/install_pyro1.1.277.hydra:")
        print("\u001b[30m[\u001b[32mOK\u001b[30m]\u001b[34m system:update/boot/install_pyro1.2.hydra:")
        print("\u001b[30m[\u001b[32mOK\u001b[30m]\u001b[34m system:install/boot/install_pynix.rino:from pyro:")
        print("\u001b[30m[\u001b[32mOK\u001b[30m]\u001b[34m system:read/boot/system_os.detect.rino:\u001b[30m")
        print("""[0.000000001][prototype]: data :/root/: net:: appdata(=buildroot.steriotype)

-data.session: [ i ]:

using; include #includeinimport $core(=buildroot.steriotype, system.core) <>:1:1
using; include #includeinimport $core(=buildroot.steriotype, system.data) <>:1:1
using; include #includeinimport $core(=buildroot.steriotype, system.framework) <>:1:1
using; include #includeinimport $core(=buildroot.steriotype, system.prototype) <>:1:1
using; include #includeinimport $core(=buildroot.steriotype, system.sys) <>:1:1

:: root@modules{data.sterio}; $score --(( expression ))  
[    0.000000] data-e820:  [mem 0x0000000000000000-0x000000000009fbff]
[    0.000000] data-e820:  [mem 0x000000000009fc00-0x000000000009ffff]
[    0.000000] data-e820:  [mem 0x00000000000f0000-0x00000000000fffff]
[    0.000000] data-e820:  [mem 0x0000000000100000-0x000000001ffbffff]
[    0.000000] data-e820:  [mem 0x000000001ffc0000-0x000000001fffffff]
[    0.000000] data-e820:  [mem 0x00000000fffc0000-0x00000000ffffffff]
[    0.116400]   DMA       [mem 0x0000000000001000-0x0000000000ffffff]
[    0.116500]   Normal    [mem 0x0000000001000000-0x000000001ffbffff]
[    0.116900]   node   0: [mem 0x0000000000001000-0x000000000009efff]
[    0.116900]   node   0: [mem 0x0000000000100000-0x000000001ffbffff]
######################################################################
#][source id: .start_contents::after,::before = true]""")
  elif e == "SYSTEM.OUT":
    fci = input()
    cls()
    print(fci)
  elif e == "SYSTEM.VER":
    print("""orian 0.98
leptin 0.98.125
viraton 0.98.254
viragin 0.99
velitra 0.99.124
lentayen 1.0
lopagon 1.0.1
sentara 1.0.1.122
veriox 1.0.1.244
serenta 1.0.1.982
levoxion 1.0.2
senixon 1.0.4
velixa 1.0.5
fortiox 1.1
monlitha 1.1.233
novato 1.1.235
niaro 1.2
protano 1.2.344
trinoxia 1.2.388
defoxia 1.3.2
sentoxia 1.3.98
evextio 1.3.99
sentario 1.4""")
  elif e == "Hello, World!":
      print("runtime: runtime.opntramp called file.py from 0x7fe7cf1e59a8...")
      time.sleep(0.1)
      print("""runtime stack:
  runtime: unexpected return pc for runtime.sigtramp called from 0x7fe7f6de0ee0
  stack: frame={sp:0xc0000656b0, fp:0xc000065700} stack=[0xc00005d5a8,0xc0000659a8)
  0x000000c0000655b0:  0x000000c0000655d0  0x000000c000065610 
  0x000000c0000655c0:  0x0000000000203000  0x0000000000203000 
  0x000000c0000655d0:  0x00005555573b9ae0  0x0000000000000000 
  0x000000c0000655e0:  0x0000000000004000  0x0000000000415906 <runtime.heapBits.forwardOrBoundary+0x0000000000000046> 
  0x000000c0000655f0:  0x00007fe7cfe84f00  0x0000000000000600 
  0x000000c000065600:  0x000000c000065678  0x0000000000448d85 <runtime.sigtrampgo+0x0000000000000125> 
  0x000000c000065610:  0x000000c00000001c  0x00000000005a6ee0 
  0x000000c000065620:  0x000000c000065638  0x00007fe7cfe84f00 
  0x000000c000065630:  0x00007fe7d007ffff  0x0000000000000000 
  0x000000c000065640:  0x0000000000000000  0x0000000000000000 
  0x000000c000065650:  0x0000000000000000  0x0000000000000000 
  0x000000c000065660:  0x000000c0000001a0  0x000000c000065830 
  0x000000c000065670:  0x000000c000065700  0x000000c0000656a0 
  0x000000c000065680:  0x000000000046540e <runtime.sigtrampgo+0x000000000000002e>  0x000000000000001c 
  0x000000c000065690:  0x000000c000065830  0x000000c000065700 
  0x000000c0000656a0:  0x000000c0000656f0  0x000000000046493d <runtime.sigtramp+0x000000000000003d> 
  0x000000c0000656b0: <0x000000000000001c  0x000000c000065830 
  0x000000c0000656c0:  0x000000c000065700  0x00007fe7f6dc2800 
  0x000000c0000656d0:  0x0000000000203000  0x00000000004ea908 
  0x000000c0000656e0:  0x000000c0000001a0  0x00007fe7cfe83431 
  0x000000c0000656f0:  0x000000c000065cb8 !0x00007fe7f6de0ee0 
  0x000000c000065700: >0x0000000000000007  0x0000000000000000 
  0x000000c000065710:  0x00005555573b9ae0  0x0000000000000000 
  0x000000c000065720:  0x0000000000004000  0x0000000000000029 
  0x000000c000065730:  0x0000000000000000  0x00007fe7f69bceb8 
  0x000000c000065740:  0x0000000000000000  0x0000000000203000 
  0x000000c000065750:  0x00000000004ea908  0x000000c0000001a0 
  0x000000c000065760:  0x00007fe7cfe83431  0x0000000000000001 
  0x000000c000065770:  0x00000000004e89d1  0x000000c000065cb8 
  0x000000c000065780:  0x00007fe7f6dc2800  0x00007fe7d0091000 
  0x000000c000065790:  0x00007fe7f6dc2800  0x00000000003ff9fd 
  0x000000c0000657a0:  0x000000c000065ca8  0x00000000004266e8 <runtime.inHeapOrStack+0x0000000000000028> 
  0x000000c0000657b0:  0x0000000000010246  0x002b000000000033 
  0x000000c0000657c0:  0x0000000000000000  0x0000000000000000 
  0x000000c0000657d0:  0x0000000000000000  0x0000000000000000 
  0x000000c0000657e0:  0x000000c0000658c0  0x0000000000000000 
  0x000000c0000657f0:  0x0000000000203000  0x0000000000203000 
  runtime.throw({0x4e9fc0, 0xc000056000})
      runtime/panic.go:1198 +0x71
  runtime.sigNotOnStack(0x1c)
      runtime/signal_unix.go:919 +0x65
  runtime.adjustSignalStack(0x1c, 0x5a6ee0, 0xc000065638)
      runtime/signal_unix.go:510 +0x296
  runtime.sigtrampgo(0x1c, 0xc000065830, 0xc000065700)
      runtime/signal_unix.go:450 +0x125
  runtime.sigtrampgo(0x1c, 0xc000065830, 0xc000065700)
      <autogenerated>:1 +0x2e
  runtime: unexpected return pc for runtime.sigtramp called from 0x7fe7f6de0ee0
  stack: frame={sp:0xc0000656b0, fp:0xc000065700} stack=[0xc00005d5a8,0xc0000659a8)
  0x000000c0000655b0:  0x000000c0000655d0  0x000000c000065610 
  0x000000c0000655c0:  0x0000000000203000  0x0000000000203000 
  0x000000c0000655d0:  0x00005555573b9ae0  0x0000000000000000 
  0x000000c0000655e0:  0x0000000000004000  0x0000000000415906 <runtime.heapBits.forwardOrBoundary+0x0000000000000046> 
  0x000000c0000655f0:  0x00007fe7cfe84f00  0x0000000000000600 
  0x000000c000065600:  0x000000c000065678  0x0000000000448d85 <runtime.sigtrampgo+0x0000000000000125> 
  0x000000c000065610:  0x000000c00000001c  0x00000000005a6ee0 
  0x000000c000065620:  0x000000c000065638  0x00007fe7cfe84f00 
  0x000000c000065630:  0x00007fe7d007ffff  0x0000000000000000 
  0x000000c000065640:  0x0000000000000000  0x0000000000000000 
  0x000000c000065650:  0x0000000000000000  0x0000000000000000 
  0x000000c000065660:  0x000000c0000001a0  0x000000c000065830 
  0x000000c000065670:  0x000000c000065700  0x000000c0000656a0 
  0x000000c000065680:  0x000000000046540e <runtime.sigtrampgo+0x000000000000002e>  0x000000000000001c 
  0x000000c000065690:  0x000000c000065830  0x000000c000065700 
  0x000000c0000656a0:  0x000000c0000656f0  0x000000000046493d <runtime.sigtramp+0x000000000000003d> 
  0x000000c0000656b0: <0x000000000000001c  0x000000c000065830 
  0x000000c0000656c0:  0x000000c000065700  0x00007fe7f6dc2800 
  0x000000c0000656d0:  0x0000000000203000  0x00000000004ea908 
  0x000000c0000656e0:  0x000000c0000001a0  0x00007fe7cfe83431 
  0x000000c0000656f0:  0x000000c000065cb8 !0x00007fe7f6de0ee0 
  0x000000c000065700: >0x0000000000000007  0x0000000000000000 
  0x000000c000065710:  0x00005555573b9ae0  0x0000000000000000 
  0x000000c000065720:  0x0000000000004000  0x0000000000000029 
  0x000000c000065730:  0x0000000000000000  0x00007fe7f69bceb8 
  0x000000c000065740:  0x0000000000000000  0x0000000000203000 
  0x000000c000065750:  0x00000000004ea908  0x000000c0000001a0 
  0x000000c000065760:  0x00007fe7cfe83431  0x0000000000000001 
  0x000000c000065770:  0x00000000004e89d1  0x000000c000065cb8 
  0x000000c000065780:  0x00007fe7f6dc2800  0x00007fe7d0091000 
  0x000000c000065790:  0x00007fe7f6dc2800  0x00000000003ff9fd 
  0x000000c0000657a0:  0x000000c000065ca8  0x00000000004266e8 <runtime.inHeapOrStack+0x0000000000000028> 
  0x000000c0000657b0:  0x0000000000010246  0x002b000000000033 
  0x000000c0000657c0:  0x0000000000000000  0x0000000000000000 
  0x000000c0000657d0:  0x0000000000000000  0x0000000000000000 
  0x000000c0000657e0:  0x000000c0000658c0  0x0000000000000000 
  0x000000c0000657f0:  0x0000000000203000  0x0000000000203000 
  runtime.sigtramp()
      runtime/sys_linux_amd64.s:343 +0x3d
  
  goroutine 17 [syscall, locked to thread]:
  runtime.goexit()
      runtime/asm_amd64.s:1581 +0x1 fp=0xc000064fe8 sp=0xc000064fe0 pc=0x462e41
  
  goroutine 1 [running, locked to thread]:
      goroutine running on other thread; stack unavailable""")
      print("")
      print("")
      print("")
      print("")
      time.sleep(0.5)
      for i in tqdm(range(0, 100), disable=False,
                    desc="\u001b[37mOPENINGPACKAGE…   "):
          sleep(.002)
      time.sleep(0.1)
      for i in tqdm(range(0, 100), disable=False,
                    desc="\u001b[37mFORMATTINGPACKAGE…"):
          sleep(.002)
      time.sleep(0.1)
      for i in tqdm(range(0, 100), disable=False,
                    desc="\u001b[37mLOADINGPACKAGE…   "):
          sleep(.002)
      cls()
      time.sleep(0.3)
      print("Hello, World!")
      time.sleep(60)
      quit("Prosess died ::finished =e exit code '0' ")
  elif e == "No":
    pass
  elif e == "CR: /mkdev/DISK -u MD.d":
    print("[file:] disk.space _e33ufe-20eff00000000x0028")
    time.sleep(0.07)
    print("[file:] disk.space _e33ufe-20eff00000100x2493")
    time.sleep(0.07)
    print("[file:] disk.space _e33ufe-20eff01010000x0982")
    time.sleep(0.07)
    print("[file:] disk.space _e33ufe-20eff01000010x0172")
    time.sleep(0.07)
    print("[file:] disk.space _e33ufe-20eff00001000x1267")
    time.sleep(0.07)
    print("[file:] disk.space _e33ufe-20eff00100000x1627")
    time.sleep(0.07)
    print("[file:] disk.space _e33ufe-20eff01100000x3918")
    time.sleep(0.07)
    print("[file:] disk.space _e33ufe-20eff00000010x4432")
    p = input()
    if p == "CR: /mkdev/DRR_ efi -n constructor=":
      print("LOCATION: disk.space_ /mkdev/MainDisk.drive from CRR2TN1JF0UQ7W4I90Z3X")
      print("VALUE: UNKNOWN (VALUE_NEEDED!)")
      p1 = input()
      if p1 == "CR: /mkdev/Drive -p: [NAME].user/workspace= ":
        print("DISK NAME! ~$ ")
        p2 = input()
        
        print(f"DISK NAME: {p2} ")
        cls()
        print("DISK SIZE! ~$ ")
        p3 = input("1MiB-100MiB")
        if p3 > 100:
          print("CANNOT MAKE DISK!")
          quit()
        elif p3 < 100:
          print("DISK MADE!")
        elif p3 == 100:
          print("DISK MADE!")
        else:
          print("?SYNTAX ERROR 255")
      else:
        print("?SYNTAX ERROR 255")
    else:
      print("?SYNTAX ERROR 255")
  elif e == "MD: /Disk/":
    ef = input("/Disk/ ")
    if ef == "MD: /Disk/Desktop/":
      el = input("/Disk/Desktop")
      if el == "MD: QUIT":
        quit()
      elif el == "MD: /Rn/ 10000":
        print(random.randint(1,10000))
      elif el == "MD: /Rn/ 1000":
        print(random.randint(1,1000))
      elif el == "MD: /Rn/ 100":
        print(random.randint(1,100))
      elif el == "MD: /Rn/ 10":
        print(random.randint(1,10))
      else:
        print("?SYNTAX ERROR 255")
    elif ef == "MD: /Disk/Apps/":
      print("CR0000000000000000FFX1")
  elif e == "NP":
    print("      NEST ]ONE[      ")
    exp = input()
    if exp == "Developer Mode":
      print("ENABLED")
      time.sleep(2)
      cls()
      print("      NEST ]DEV[      ")
      exr = input()
      if exr == "/System/Develop/?Finder.info/ contine.devmode = true?":
        print(f"""id: QPsSCm4l5DVB1OTNcIsacoarJf3ICsGFL9iG5fviYVGXRii77s1kmrq3k6ShcybuYyACBXRzBO1tj53icdjYHHJ5KoN1Zv4W5HDp
        user1.username: ?
        user1.password: ?
        user2.username: ADMIN
        user2.password: ············
        
        OS.version: 4.0.0 (build: A4107256, release: 2023 JAN 27)
        OS.build: eHXGvkKfcMmVrzKcPTrNm
        node: --child.scene_new()""")
        print("node: --child[of].scene = {add: part[standard].null}")
        print(f"""main.resource: APIserviceID.core_media
        main.data: APIserviceMEDIA.core_media
        main.identifier: 0x011111ff2e
        main.general.identifier: 0x011111ff2e
        main.event: scene_node.media""")
      elif exr == "terminal":
        print("\u001b[35m[==] \u001b[32m\033[1mReady")
        print("\u001b[35m[==] \u001b[33mconsole://system/config/boot/cmdp")
        extr = input("\u001b[33muser@cmdp$\u001b[37m")
        if extr == "GPU DRIVER":
          print("VERSION 1.0.0 (BETA)")
          extg = input()
          if extg == "Upgrade":
            print("*** UPGRADING *** 1.1.0 (NOTE; WHEN REBOOTING OR CLOSING THE SYSTEM YOU MAY NEED TO INSTALL THE NEW DRIVER AGAIN!)")
          else:
            print("]? UKNOWN ERROR")
        elif extr == "CPU DRIVER":
          print("VERSION 1.0.0 (BETA)")
          extg = input()
          if extg == "Upgrade":
            print("*** UPGRADING *** 1.1.0 (NOTE; WHEN REBOOTING OR CLOSING THE SYSTEM YOU MAY NEED TO INSTALL THE NEW DRIVER AGAIN!)")
          else:
            print("]? UKNOWN ERROR")
  elif e == "ACTIVATE":
    ghd = input("PUT IN ACTIVATION KEY HERE: ")
    if ghd == "000-000-0000":
      print("YOUR COPY OF PYNIX IS ACTIVATED")
    elif ghd == "111-000-0000":
      print("YOUR COPY OF PYNIX IS ACTIVATED")
    elif ghd == "001-102-3000":
      print("YOUR COPY OF PYNIX IS ACTIVATED")
    elif ghd == "025-000-0000":
      print("YOUR COPY OF PYNIX IS ACTIVATED")
    elif ghd == "000-052-0000":
      print("YOUR COPY OF PYNIX IS ACTIVATED")
    elif ghd == "000-111-1111":
      print("YOUR COPY OF PYNIX IS ACTIVATED")
    elif ghd == "000-223-0000":
      print("YOUR COPY OF PYNIX IS ACTIVATED")
    else:
      print("THE CODE IS INVALID")
  elif e == "CLEAR":
    cls()
    pass
  else:
    print(f"ERROR '{e}' IS NOT DEFINED TYPE HELP FOR COMMANDS")
