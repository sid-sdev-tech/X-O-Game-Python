ls = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
i = 0
j = 0
k = 0
print("Enter the names of two players:")
p1 = input()
p2 = input()
print(p1, "your character is 'x' to play")
print(p2, "your character is 'o' to play")

while i < len(ls):
    print(ls[i], end=" ")
    if ls[i] % 3 == 0:
        print()
    # print()
    # print(ls[i], end=" ")
    i = i + 1
p1w = '0'
p2w = '0'
while j<5:
    i=0
    k=0
    print()
    if list[0] == list[1] == 'o':
        print("Alert..!", p2, "is winning the match, if you don't choose 3rd Box..")
    elif list[1] == list[2] == 'o':
        print("Alert..!", p2, "is winning the match, if you don't choose 1st Box..")
    elif list[0] == list[2] == 'o':
        print("Alert..!", p2, "is winning the match, if you don't choose 2nd Box..")
    elif list[3] == list[4] == 'o' and list[5] != 'x':
        print("Alert..!", p2, "is winning the match, if you don't choose 6th Box..")
    elif list[4] == list[5] == 'o':
        print("Alert..!", p2, "is winning the match, if you don't choose 4th Box..")
    elif list[3] == list[5] == 'o':
        print("Alert..!", p2, "is winning the match, if you don't choose 5th Box..")
    elif list[6] == list[7] == 'o':
        print("Alert..!", p2, "is winning the match, if you don't choose 9th Box..")
    elif list[7] == list[8] == 'o':
        print("Alert..!", p2, "is winning the match, if you don't choose 7th Box..")
    elif list[6] == list[8] == 'o':
        print("Alert..!", p2, "is winning the match, if you don't choose 8th Box..")
    elif list[0] == list[3] == 'o':
        print("Alert..!", p2, "is winning the match, if you don't choose 7th Box..")
    elif list[3] == list[6] == 'o':
        print("Alert..!", p2, "is winning the match, if you don't choose 1st Box..")
    elif list[0] == list[6] == 'o':
        print("Alert..!", p2, "is winning the match, if you don't choose 4th Box..")
    elif list[1] == list[4] == 'o':
        print("Alert..!", p2, "is winning the match, if you don't choose 8th Box..")
    elif list[4] == list[7] == 'o':
        print("Alert..!", p2, "is winning the match, if you don't choose 2nd Box..")
    elif list[1] == list[7] == 'o':
        print("Alert..!", p2, "is winning the match, if you don't choose 5th Box..")
    elif list[2] == list[5] == 'o':
        print("Alert..!", p2, "is winning the match, if you don't choose 9th Box..")
    elif list[5] == list[8] == 'o':
        print("Alert..!", p2, "is winning the match, if you don't choose 3rd Box..")
    elif list[2] == list[8] == 'o':
        print("Alert..!", p2, "is winning the match, if you don't choose 6th Box..")
    elif list[0] == list[4] == 'o':
        print("Alert..!", p2, "is winning the match, if you don't choose 9th Box..")
    elif list[4] == list[8] == 'o':
        print("Alert..!", p2, "is winning the match, if you don't choose 1st Box..")
    elif list[0] == list[8] == 'o':
        print("Alert..!", p2, "is winning the match, if you don't choose 5th Box..")
    elif list[2] == list[4] == 'o':
        print("Alert..!", p2, "is winning the match, if you don't choose 7th Box..")
    elif list[4] == list[6] == 'o':
        print("Alert..!", p2, "is winning the match, if you don't choose 3rd Box..")
    elif list[2] == list[6] == 'o' and list[4] != 'x':
        print("Alert..!", p2, "is winning the match, if you don't choose 5th Box..")

    print()
    print(p1, "'s chance now..")
    p1c = int(input())
    p1c_indexn = ls.index(p1c)
    if list[p1c_indexn] != 'x' and list[p1c_indexn] == 'o':
        list[p1c_indexn] = 'o'
        print("You can't change others option here !")
    elif list[p1c_indexn] != 'x' and list[p1c_indexn] != 'o':
        list[p1c_indexn] = 'x'

    while i<len(ls):
            print(list[i], end=" ")
            # print("p1c_indexn is :", p1c_indexn)
            if ls[i]%3 == 0:
                print()
            # print("list ls has ", ls)
            i = i + 1
    print()

    if list[0] == list[1] == list[2] == 'x':
        print(p1, "is winner..")
        p1w = "Wins"
        break
    elif list[3] == list[4] == list[5] == 'x':
        print(p1, "wins..")
        p1w = "Wins"
        break
    elif list[6] == list[7] == list[8] == 'x':
        print(p1, "wins..")
        p1w = "Wins"
        break
    elif list[0] == list[3] == list[6] == 'x':
        print(p1, "wins..")
        p1w = "Wins"
        break
    elif list[1] == list[4] == list[7] == 'x':
        print(p1, "wins..")
        p1w = "Wins"
        break
    elif list[2] == list[5] == list[8] == 'x':
        print(p1, "wins..")
        p1w = "Wins"
        break
    elif list[0] == list[4] == list[8] == 'x':
        print(p1, "wins..")
        p1w = "Wins"
        break
    elif list[2] == list[4] == list[6] == 'x':
        print(p1, "wins..")
        p1w = "Wins"
        break

    if list[0] == list[1] == 'x':
        print("Alert..!", p1, "is winning the match, if you don't choose 3rd Box..")
    elif list[1] == list[2] == 'x':
        print("Alert..!", p1, "is winning the match, if you don't choose 1st Box..")
    elif list[0] == list[2] == 'x':
        print("Alert..!", p1, "is winning the match, if you don't choose 2nd Box..")
    elif list[3] == list[4] == 'x':
        print("Alert..!", p1, "is winning the match, if you don't choose 6th Box..")
    elif list[4] == list[5] == 'x':
        print("Alert..!", p1, "is winning the match, if you don't choose 4th Box..")
    elif list[3] == list[5] == 'x':
        print("Alert..!", p1, "is winning the match, if you don't choose 5th Box..")
    elif list[6] == list[7] == 'x':
        print("Alert..!", p1, "is winning the match, if you don't choose 9th Box..")
    elif list[7] == list[8] == 'x':
        print("Alert..!", p1, "is winning the match, if you don't choose 7th Box..")
    elif list[6] == list[8] == 'x':
        print("Alert..!", p1, "is winning the match, if you don't choose 8th Box..")
    elif list[0] == list[3] == 'x':
        print("Alert..!", p1, "is winning the match, if you don't choose 7th Box..")
    elif list[3] == list[6] == 'x':
        print("Alert..!", p1, "is winning the match, if you don't choose 1st Box..")
    elif list[0] == list[6] == 'x':
        print("Alert..!", p1, "is winning the match, if you don't choose 4th Box..")
    elif list[1] == list[4] == 'x':
        print("Alert..!", p1, "is winning the match, if you don't choose 8th Box..")
    elif list[4] == list[7] == 'x':
        print("Alert..!", p1, "is winning the match, if you don't choose 2nd Box..")
    elif list[1] == list[7] == 'x':
        print("Alert..!", p1, "is winning the match, if you don't choose 5th Box..")
    elif list[2] == list[5] == 'x':
        print("Alert..!", p1, "is winning the match, if you don't choose 9th Box..")
    elif list[5] == list[8] == 'x':
        print("Alert..!", p1, "is winning the match, if you don't choose 3rd Box..")
    elif list[2] == list[8] == 'x':
        print("Alert..!", p1, "is winning the match, if you don't choose 6th Box..")
    elif list[0] == list[4] == 'x':
        print("Alert..!", p1, "is winning the match, if you don't choose 9th Box..")
    elif list[4] == list[8] == 'x':
        print("Alert..!", p1, "is winning the match, if you don't choose 1st Box..")
    elif list[0] == list[8] == 'x':
        print("Alert..!", p1, "is winning the match, if you don't choose 5th Box..")
    elif list[2] == list[4] == 'x':
        print("Alert..!", p1, "is winning the match, if you don't choose 7th Box..")
    elif list[4] == list[6] == 'x':
        print("Alert..!", p1, "is winning the match, if you don't choose 3rd Box..")
    elif list[2] == list[6] == 'x':
        print("Alert..!", p1, "is winning the match, if you don't choose 5th Box..")

    print(p2, "'s chance now..")
    p2c = int(input())
    p2c_indexn = ls.index(p2c)
    if list[p2c_indexn] == 'x' and list[p2c_indexn] != 'o':
        list[p2c_indexn] = 'x'
        print("You can't change others option here !")
    elif list[p2c_indexn] != 'x' and list[p2c_indexn] != 'o':
        list[p2c_indexn] = 'o'
    print()

    while k<len(ls):
        print(list[k], end=" ")
        if ls[k]%3 == 0:
            print()
        k = k + 1
    print()
    if list[0] == list[1] == list[2] == 'o':
        print(p2, "is winner..")
        p2w = "Wins"
        break
    elif list[3] == list[4] == list[5] == 'o':
        print(p2, "wins..")
        p2w = "Wins"
        break
    elif list[6] == list[7] == list[8] == 'o':
        print(p2, "wins..")
        p2w = "Wins"
        break
    elif list[0] == list[3] == list[6] == 'o':
        print(p2, "wins..")
        p2w = "Wins"
        break
    elif list[1] == list[4] == list[7] == 'o':
        print(p2, "wins..")
        p2w = "Wins"
        break
    elif list[2] == list[5] == list[8] == 'o':
        print(p2, "wins..")
        p2w = "Wins"
        break
    elif list[0] == list[4] == list[8] == 'o':
        print(p2, "wins..")
        p2w = "Wins"
        break
    elif list[2] == list[4] == list[6] == 'o':
        print(p2, "wins..")
        p2w = "Wins"
        break

    j = j + 1

print("----------------------")
if p1w == "Wins":
    print(p1, "is the Winner..")
elif p2w == "Wins":
    print(p2, "is the Winner..")
else:
    print("Match Draw..!!")
print("----------------------")




from tkinter import *

fnt = ('Consolas Bold Italic',18)
fnt0 = ("Consolas Italic",15)
fnt1 = ('Georgia Bold',13)
fnt2 = ('Georgia',13)
def btnpress():
    pass

base = Tk()
base.title("X-O Game GUI")
base.geometry('750x575')
base.configure(bg='#551A8B')

btn0 = Button(base,text = " ",bg = "white",font = fnt1,command=btnpress,width = '4',height = '2')
btn0.place(x =110, y =205)
#btn0.bind("<Enter>",add)
#btn0.bind("<Leave>",mouserelease)
btn1 = Button(base,text = ' ',bg = 'white',font = fnt1,command=btnpress,width = '4',height = '2')
btn1.place(x = 170,y = 205)
#btn1.bind("<Enter>",sub)
#btn1.bind("<Leave>",mouserelease)
btn2 = Button(base,text = ' ',bg = 'white',font = fnt1,command=btnpress,width = '4',height = '2')
btn2.place(x = 230,y = 205)
#btn2.bind("<Enter>",mul)
#btn2.bind("<Leave>",mouserelease)
btn3 = Button(base,text = ' ',bg = 'white',font = fnt1,command=btnpress,width = '4',height = '2')
btn3.place(x = 110,y = 260)
#btn3.bind("<Enter>",div)
#btn3.bind("<Leave>",mouserelease)
btn4 = Button(base,text = ' ',bg = 'white',font = fnt1,command = btnpress,width = '4',height='2')
btn4.place(x=170,y=260)
btn5 = Button(base,text = ' ',bg = 'white',font = fnt1,command = btnpress,width = '4',height='2')
btn5.place(x=230,y=260)
btn6 = Button(base,text = ' ',bg = 'white',font = fnt1,command = btnpress,width = '4',height='2')
btn6.place(x=110,y=315)
btn7 = Button(base,text = ' ',bg = 'white',font = fnt1,command = btnpress,width = '4',height='2')
btn7.place(x=170,y=315)
btn8 = Button(base,text = ' ',bg = 'white',font = fnt1,command = btnpress,width = '4',height='2')
btn8.place(x=230,y=315)
btn9 = Button(base,text = 'Undo',bg = 'orange',font = fnt1,command = btnpress,width = '5',height='2')
btn9.place(x=165,y=385)

l0 = Label(base,text = 'X-O Game GUI',bg = "white",font = fnt0 ,width = '18')
l0.place(x=240,y=40)
l1 = Label(base,text = "Best of 5",bg = "brown",fg = 'silver',font = fnt,width = '10')
l1.place(x=130,y=160)
l2 = Label(base,text = "Player-1:- ",bg = "#BFBFBF",font = fnt0,width = '12')
l2.place(x= 330,y=180)
l3 = Label(base,text = "Player-2:- ",bg = "#BFBFBF",font = fnt0,width = '12')
l3.place(x = 330,y = 225)
l4 = Label(base,text = " Players-Score : ",bg = "brown",fg = 'silver',font = fnt,width = '16')
l4.place(x = 390 ,y = 115)
l4 = Label(base,text = "Draw :",bg = "#BFBFBF",font = fnt0,width = '12')
l4.place(x = 330 ,y = 275)

txt1 = Entry(base,font = fnt1,width = '13')
txt1.place(x = 480 , y = 182)
txt2 = Entry(base,font = fnt1,width = '13')
txt2.place(x=480,y=225)
txt3 = Entry(base,font = fnt1,width = '13')
txt3.place(x=480,y=275)
btn4 = Button(base,text = '[ RESET-GAME ]',bg = 'darkorchid2',font = fnt1,command = btnpress,width = '13',height='2')
btn4.place(x=370,y=350)
btn5 = Button(base,text = ' RESET-MATCH ',bg = 'antiquewhite3',font = fnt1,command = btnpress,width = '13',height='2')
btn5.place(x=370,y=425)

base.mainloop()

'''
ls = [1,2,3,4,5,6,7,8,9]
list = [1,2,3,4,5,6,7,8,9]
tx = ('x')
to = ('o')
#print("to has",to,type(to))
t = ('x','o')
#print("tx has ",tx,type(tx), "t has ",t,type(t))
i=0
j=0
print("Enter the names of two players:")
p1 = input()
p2 = input()

while i<len(ls):
    print(ls[i],end=" ")
    if ls[i]%3 == 0:
        print()
    #print()
    #print(ls[i],end=" ")
    i = i + 1

while j < 5:
    print(p1,"'s chance now..")
    p1c = int(input())

    i = 0
    while i<len(ls):
        p1c_indexn = ls.index(p1c)
        list[p1c_indexn] = 'x'
        print(list[i],end=" ")
        #print("p1c_indexn is :",p1c_indexn)
        if ls[i]%3 == 0:
            print()
        #print(ls[i],end=" " )
        #print("list ls has ",ls)
        i = i + 1
        print(p2, "'s chance now..")
        p2c = int(input())
        p2c_indexn = ls.index(p2c)
        list[p2c_indexn] = 'o'


    j = j + 1
'''