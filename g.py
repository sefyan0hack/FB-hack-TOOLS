import os
aaa=input('    \033[42m \033[91mentre name file\033[0m >> : ')
if aaa =='exit':
    os.system("clear")
    os.system("exit")
    os.system("clear")
elif aaa=='':
    os.system("clear")
    os.system("exit")
    os.system("clear")
else:
    print ("\n\n")
    print ("\t/data/data/com.termux/files/home/facebook-tols/"+aaa)
    print ("\n")
    file=open(aaa,'w')
    aa=set([])
    oio=set([])
#iio=set([112233,332211,000,445566,'$'*1,'$'*2,'$'*3,'@'*1,'@'*2,'@'*3,'€'*1,'€'*2,'€'*3,'&'*1,'&'*2,'&'*3,'¥'*1,'¥'*2,'¥'*3,'*'*1,'*'*2,'*'*3,'+'*1,'+'*2,'+'*3])
    kk=1
while True :
    b=input('  \033[4mEntre\033[0m {} : '.format(kk))
    if b=='exit' :
        file.close()
        qq=open(aaa, 'r' )
        ll=len(qq.readlines())
        print('>> {} Passwords in ---> {} '.format(ll, aaa))
        break ;
    aa.add(b)
    for i in aa:
        if len(i) >= 6 and i not in oio :
            oio.add(i)
            file.write(i)
            file.write('\n')
            #for o in iio:
             #   uau='{}{}'.format(i,o) 
              #  ubu='{}{}{}'.format(o,i,o)
               # ucu='{}{}{} '.format(i,o,i)
                #if len(uau)>= 6:
                   # file.write(uau)
                  #  file.write('\n')
               # if len(ubu) >= 6 and ubu != uau :
                   # file.write(ubu)
                   # file.write('\n')
                #if len(ucu) >= 6 and ucu != uau and ucu != ubu:
                  #  file.write(ucu)
                  #  file.write('\n')

        c=b+i
        d=i+b
        if len(c) >= 6 :
            file.write(c)
            file.write('\n') 
        if c != d and len(d) >= 6:
            file.write(d)
            file.write('\n')
    kk=int(kk)+1
