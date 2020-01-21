#These tools are designed
#by a 14-year-old
#Moroccan Arab child who
#is my father and I
#designed the Python language
#################
import os
import sys
import time
from core import wcolors
from datetime import datetime
os .system("clear")
####################
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year
#################
def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(2. / 400)
#####################
banner_4="""
\033[38;5;196m
      :::::::::: :::::::::  :::    :::     :::      ::::::::  :::    :::
      :+:        :+:    :+: :+:    :+:   :+: :+:   :+:    :+: :+:   :+:
      +:+        +:+    +:+ +:+    +:+  +:+   +:+  +:+        +:+  +:+
\033[92m      :#::+::#   +#++:++#+  +#++:++#++ +#++:++#++: +#+        +#++:++
      +#+        +#+    +#+ +#+    +#+ +#+     +#+ +#+        +#+  +#+
      #+#        #+#    #+# #+#    #+# #+#     #+# #+#    #+# #+#   #+#
      ###        #########  ###    ### ###     ###  ########  ###    ###


"""
banner_3=''' 

          \033[93m   d888b   .d88b.   .d88b.  d8888b. db     \033[96m d888888b .d8888. d888888b
          \033[93m  88' Y8b .8P  Y8. .8P  Y8. 88  `8D 88     \033[96m   `88'   88'  YP `~~88~~'
          \033[93m  88      88    88 88    88 88   88 88     \033[96m    88    `8bo.      88
          \033[93m  88  ooo 88    88 88    88 88   88 88     \033[96m    88      `Y8b.    88
          \033[93m  88. ~8~ `8b  d8' `8b  d8' 88  .8D 88booo.\033[96m   .88.   db   8D    88
          \033[93m   Y888P   `Y88P'   `Y88P'  Y8888D' Y88888P\033[96m Y888888P `8888Y'    YP



'''
########################
banner_1=''' 

             \033[94m    __                _                 _    \033[36m
             \033[94m   / _|\033[91m __ _ \033[92m ___ \033[93m___\033[36m| |__   ___   ___ | | __
             \033[94m  | |_ \033[91m/ _` |\033[92m/ __\033[93m/ _ \\ \033[36m _ \ / _ \ / _ \| |/ /
             \033[94m  |  _|\033[91m (_| |\033[92m (_|\033[93m  __/\033[36m |_) | (_) | (_) |   <
             \033[94m  |_|  \033[91m\__,_|\033[92m\___\033[93m\___|\033[36m_.__/ \___/ \___/|_|\_\


           •ิ.•ั|•ิ.•ั|•ิ.•ั|•ิ.•ั|•ิ.•ั|•ิ.•ั|•ิ.•|ั•ิ.•ั|•ิ.•ั|•ิ.•ั|•ิ.•ั|•ิ.•ั|•ิ.•ั
'''
#######################
slowprint(banner_1)
banner="""

    \033[31m .----------------.\033[38;5;226m  .----------------.\033[92m  .----------------.
    \033[31m | .--------------.\033[38;5;226m || .--------------.\033[92m || .--------------. |
    \033[31m | |  _________   |\033[38;5;226m || |   ______     |\033[92m || |    ______    | |
    \033[31m | | |_   ___  |  |\033[38;5;226m || |  |_   _ \    |\033[92m || |  .' ___  |   | |
    \033[31m | |   | |_  \_|  |\033[38;5;226m || |    | |_) |   |\033[92m || | / .'   \_|   | |
    \033[31m | |   |  _|      |\033[38;5;226m || |    |  __'.   |\033[92m || | | |    ____  | |
    \033[31m | |  _| |_       |\033[38;5;226m || |   _| |__) |  |\033[92m || | \ `.___]  _| | |
    \033[31m | | |_____|      |\033[38;5;226m || |  |_______/   |\033[92m || |  `._____.'   | |
    \033[31m | |              |\033[38;5;226m || |              |\033[92m || |              | |
    \033[31m | '--------------'\033[38;5;226m || '--------------'\033[92m || '--------------' |
    \033[31m '----------------'\033[38;5;226m  '----------------'\033[92m  '----------------'



\033[0m
"""
########################
banner_2=''' 
\033[0m
🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻
🔵my fb:\033[4mhttps://m.facebook.com/profile.php?id
 =100036177376844\033[0m                          🔵
🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺🔺
        ◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼
        ◼ By :\033[4msefyan bn talb\033[0m
        ◼ from :\033[4mmoroco\033[0m
        ◼ virsion :\033[4m2.0\033[0m
        ◼ numbeer :\033[4m+212 632804965\033[0m
        ◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼◼


'''
########################
slowprint(banner_2)
def main():
    line_1 = wcolors.color.UNDERL + wcolors.color.backRed + wcolors.color.GREEN+'FB=TOLS'+wcolors.color.ENDC
    cmd= input ("      "+line_1+" > ")
    if cmd =='fbg':
        os.system("clear")
        time.sleep(1)
        slowprint(banner)
        print(banner_2)
        os.system("python .f.py")
        main()
    elif cmd == 'goodlist':
        os.system("clear")
        time.sleep(1)
        slowprint(banner_3)
        slowprint(banner_2)
        os.system("python .g.py")
        os.system("clear")
        print(banner_1)
        print(banner_2)
        main()
    elif cmd =='fbhack':
        time.sleep(1)
        os.system("clear")
        slowprint(banner_4)
        slowprint(banner_2)
        print ("\n")
        os.system("python2 .h.py")
        main()
    elif cmd =='exit' :
        time.sleep(1)
        os.system("clear")
        os.system("exit")
    elif cmd =='clear':
        time.sleep(1)
        os.system("clear")
        print(banner_1)
        print(banner_2)
        main()
    elif cmd =='':
        print ("\n\033[38;5;226m \tPlese enter eny thing\033[0m \n")
        time.sleep(2)
        os.system("clear")
        print(banner_1+banner_2)
        main()

    elif cmd == 'help':
        time.sleep(1)
        print ('''
\033[92m
I) tols fb groub hack

   1) rait  : fbg

   2) entre id GROUB herre :  rait heer id grooob facebook ex:981191913

   3) entre your id  herre : rait your id facebook ex:10007898997

   4) copy link

   5)send link to  (dahiya)

II) tols fb burte

   1) rait : fbhack

   2) entre id (DAHIYA) ex:1000929898735

   3) entre patch fil .txt  ex:/data/data....namefil.txt

III) tols  Goodlist

   1) rait :goodlist

   2) entre name file saved

   3) entr nem and dat and...
\033[0m
''')
        main()
    elif cmd == 'show':
        time.sleep(1)
        print('''

\033[95m
                name             Description \033[0m
             -----------     -------------------
\033[96m                help :           for helper

                fbhack :      for opem fb burte 

                fbg :          for open fb groub

                goodlist :     for open good list

                clear:        	for clear table

                exit :        	for exit en tools
\033[0m
''')
        main()

    else:
        print ("\n")
        print ("  [!] not fuond :\033[91m " +cmd)
        print ("\033[0m  {-} Please enter :  show ")
        print ("\n")
        main()
main()
