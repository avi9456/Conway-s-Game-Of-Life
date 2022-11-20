import conwaysgameoflifeDisplay as cgl
import os
import List as l

print("Conway's Game Of Life\n\n")
print("\t1. random array")
print("\t2. select from built in array")
print("\t3. exit")
opt=input("select any one: ")
if opt=='3':
    os.system("clear")
    exit()
elif opt=='1':
    os.system("clear")
    size=int(input("Enter size: "))
    print("1. manual repetaion time in sec")
    print("2. default repetaion time")
    print("3. until all dead")
    opt=input("select any one: ")
    os.system("clear")
    if opt=='1':
        repet=int(input("Enter the time: "))*0.5
    elif opt=='2':
        repet=size*10*0.5
    else:
        repet=(size**size)*size
    os.system('clear')
    print("inistaing game")
    z,x,y,count,color=cgl.init(size)
    print("1. manual color")
    print('2. default color')
    opt=input("select any one: ")
    if opt=='1':
        dead=input("dead color: ")
        alive=input("alive color: ")
        color=cgl.colors(dead,alive)
    os.system('clear')
    print("setting display")
    fig=cgl.setDisplay(size)
    print("playing")
    cgl.show(int(repet),z,x,y,size,count,color,fig)
    print("Stopped")
else:
    os.system("clear")
    print("1. Static")
    print("2. Osicilated")
    opt=input("select any one: ")
    os.system("clear")
    if opt=='1':
        l.prtintStat()
        opt=input("select any one: ")
        z=l.static(opt)
    else:
        l.printDyan()
        opt=input("select any one: ")
        z=l.dynamic(opt)
    print("1. manual repetaion time in sec")
    print("2. default repetaion time")
    print("3. until all dead")
    opt=input("select any one: ")
    os.system("clear")
    if opt=='1':
        repet=int(input("Enter the time: "))*0.5
    elif opt=='2':
        repet=len(z)*10*0.5
    else:
        repet=(len(z)**len(z))*len(z)
    os.system('clear')
    print("inistaing game")
    x,y,count,color=cgl.init_select(len(z))
    print("1. manual color")
    print('2. default color')
    opt=input("select any one: ")
    if opt=='1':
        dead=input("dead color: ")
        alive=input("alive color: ")
        color=cgl.colors(dead,alive)
    os.system('clear')
    print("setting display")
    fig=cgl.setDisplay(len(z))
    print("playing\n\n")
    cgl.show(int(repet),z,x,y,len(z),count,color,fig)
    print("\n\nStopped")