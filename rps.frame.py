import  tkinter as tk
import random

me_data = 0
user_data = 0

def end(window):
    window.destroy()

def old_user(window, welcome, ask_name, name, enter_button):
    name_s = name.get()

    welcome.destroy()
    ask_name.destroy()
    name.destroy()
    enter_button.destroy()

    me_data, user_data = file_data_accessing(window, name_s)
    return me_data, user_data


def file_data_accessing(window, name):

    global me_data, user_data

    fg='#153450'
    bg='#F4D6BC'
    font=('Times New Roman', 13)

    name = name + '.txt'
    try:
        with open(name, "r") as file:
            lines = file.readlines()
            if len(lines) == 2:
                me = lines[0].strip()
                user = lines[1].strip()
                me_data = int(me)
                user_data = int(user)

            display_1 = tk.Label(window, text='From our last game', fg=fg, bg=bg, anchor='center', font=font)
            display_1.grid(row=0, column=7, pady=10, sticky='nsew')

            display_2 = tk.Label(window, text='Your points %s ' % (user_data), fg=fg, bg=bg, anchor='center', font=font)
            display_2.grid(row=1, column=7, pady=10, sticky='nsew')

            display_3 = tk.Label(window, text='Your points %s ' % (me_data), fg=fg, bg=bg, anchor='center', font=font)
            display_3.grid(row=2, column=7, pady=10, sticky='nsew')

            button = tk.Button(window, text='continue', command=lambda: RPS(window, display_1, display_2, display_3, button, name), fg=fg, bg=bg, anchor='center', font=font)
            button.grid(row=3, column=8, pady=10, sticky='nsew')

            return me_data, user_data
    except FileNotFoundError:
        print("File not found")
        return 0, 0
    except Exception as e:
        print("error with the file stored data: ", e)
        return 0, 0


def RPS(window, display_1, display_2, display_3, button, name):
    display_1.destroy()
    display_2.destroy()
    display_3.destroy()
    button.destroy()

    fg='#153450'
    bg='#F4D6BC'
    font=('Times New Roman', 13)

    quit_button = tk.Button(window, text='quit', command=lambda: file_data_saving(window, name, disable), fg=fg, bg=bg, anchor='center', font=font)
    quit_button.grid(row=10, column=17, pady=10, sticky='nsew')

    option = tk.Label(window, text='Choose', fg=fg, bg=bg, anchor='center', font=('Times New Roman', 17))
    option.grid(row=3, column=7, pady=10, sticky='nsew')

    rock_button = tk.Button(window, text='rock', command=lambda: Rock(window, me_1, you_1, word2, word3, result_label, result_label1), fg=fg, bg=bg, anchor='center', font=font)
    rock_button.grid(row=4, column=3, pady=10, sticky='nsew')

    paper_button = tk.Button(window, text='paper', command=lambda: Paper(window, me_1, you_1, word2, word3, result_label, result_label1), fg=fg, bg=bg, anchor='center', font=font)
    paper_button.grid(row=4, column=7, pady=10, sticky='nsew')

    scissors_button = tk.Button(window, text='scissors', command=lambda: Scissors(window, me_1, you_1, word2, word3, result_label, result_label1), fg=fg, bg=bg, anchor='center', font=font)
    scissors_button.grid(row=4, column=11, pady=10, sticky='nsew')

    me_label = tk.Label(window, text='My point : ', fg=fg, bg=bg, anchor='center', font=font)
    me_label.grid(row=0, column=16, pady=10, sticky='nsew')

    me_1 = tk.Label(window, text=me_data, fg=fg, bg=bg, anchor='center', font=font)
    me_1.grid(row=0, column=17, pady=10, sticky='nsew')

    you_label = tk.Label(window, text='Your point : ', fg=fg, bg=bg, anchor='center', font=font)
    you_label.grid(row=1, column=16, pady=10, sticky='nsew')

    result_label = tk.Label(window, text='', fg=fg, bg=bg, anchor='center', font=font)
    result_label.grid(row=9, column=7, pady=10, sticky='nsew')

    result_label1 = tk.Label(window, text='', fg=fg, bg=bg, anchor='center', font=font)
    result_label1.grid(row=10, column=7, pady=10, sticky='nsew')

    you_1 = tk.Label(window, text=user_data, fg=fg, bg=bg, anchor='center', font=font)
    you_1.grid(row=1, column=17, pady=10, sticky='nsew')

    word = tk.Label(window, text='you chose : ', fg=fg, bg=bg, anchor='center', font=font)
    word.grid(row=6, column=3, pady=10, sticky='nsew')

    word2 = tk.Label(window, text='', fg=fg, bg=bg, anchor='center', font=font)
    word2.grid(row=8, column=3, pady=10, sticky='nsew')

    word1 = tk.Label(window, text='I chose : ', fg=fg, bg=bg, anchor='center', font=font)
    word1.grid(row=6, column=11, pady=10, sticky='nsew')

    word3 = tk.Label(window, text='', fg=fg, bg=bg, anchor='center', font=font)
    word3.grid(row=8, column=11, pady=10, sticky='nsew')

    disable = [quit_button,option,rock_button,paper_button,scissors_button,me_label,me_1,you_label,you_1,word,word2,word1,word3,result_label,result_label1]


def Rock(window, me_1, you_1, word2, word3, result_label ,result_label1):

    global me_data, user_data

    options = (1, 2, 3)  # rock, paper, scissors
    choice = random.choice(options)
    word2.config(text='Rock')

    if choice == 3:
        user_data += 1
        me_1.config(text=me_data)
        you_1.config(text=user_data)
        word3.config(text='Scissors')
        result_label.config(text='U win')
        result_label1.config(text='ಠ_ಠ')

    elif choice == 2:
        me_data += 1
        me_1.config(text=me_data)
        you_1.config(text=user_data)
        word3.config(text='Paper')
        result_label.config(text='I win')
        result_label1.config(text='(⌐■_■)')

    else:
        me_1.config(text=me_data)
        you_1.config(text=user_data)
        word3.config(text='Rock')
        result_label.config(text='Draw')
        result_label1.config(text='(〃￣︶￣)人')

    print('rock')
    return me_data,user_data


def Paper(window, me_1, you_1, word2, word3, result_label, result_label1):
    
    global me_data, user_data

    options = (1, 2, 3)  # rock, paper, scissors
    choice = random.choice(options)
    word2.config(text='Paper')

    if choice == 1:
        user_data += 1
        me_1.config(text=me_data)
        you_1.config(text=user_data)
        word3.config(text='Rock')
        result_label.config(text='U win')
        result_label1.config(text='ಠ_ಠ')

    elif choice == 3:
        me_data += 1
        me_1.config(text=me_data)
        you_1.config(text=user_data)
        word3.config(text='Scissors')
        result_label.config(text='I win')
        result_label1.config(text='(⌐■_■)')

    else:
        me_1.config(text=me_data)
        you_1.config(text=user_data)
        word3.config(text='Paper')
        result_label.config(text='Draw')
        result_label1.config(text='(〃￣︶￣)人')

    print("paper")
    return me_data,user_data


def Scissors(window, me_1, you_1, word2, word3, result_label, result_label1):

    global me_data, user_data

    options = (1, 2, 3)  # rock, paper, scissors
    choice = random.choice(options)
    word2.config(text='Scissors')

    if choice == 2:
        user_data += 1
        me_1.config(text=me_data)
        you_1.config(text=user_data)
        word3.config(text='Paper')
        result_label.config(text='U win')
        result_label1.config(text='ಠ_ಠ')

    elif choice == 1:
        me_data += 1
        me_1.config(text=me_data)
        you_1.config(text=user_data)
        word3.config(text='Rock')
        result_label.config(text='I win')
        result_label1.config(text='(⌐■_■)')

    else:
        me_1.config(text=me_data)
        you_1.config(text=user_data)
        word3.config(text='Scissors')
        result_label.config(text='Draw')
        result_label1.config(text='(〃￣︶￣)人')

    print("scissors")
    return me_data,user_data

def file_data_saving(window, name, disable):

    fg='#153450'
    bg='#F4D6BC'
    font=('Times New Roman', 13)

    for i in disable:
        i.destroy()

    try:
        with open(name,"w") as file:
            pass
        with open(name,"w") as file:
            me=str(me_data)
            user=str(user_data)
            file.write(me+"\n")
            file.write(user+"\n")
    except Exception as e:
        print("error while storing data : ",e)

    you = tk.Label(window, text='Your points : %s' %(me_data), fg=fg, bg=bg, anchor='center', font=font)
    you.grid(row=1, column=7, pady=10, sticky='nsew')

    me = tk.Label(window, text='My points : %s' %(user_data), fg=fg, bg=bg, anchor='center', font=font)
    me.grid(row=2, column=7, pady=10, sticky='nsew')

    done = tk.Button(window, text='Done', command= lambda : end(window), fg=fg, bg=bg, anchor='center', font=font)
    done.grid(row=3, column=7, pady=10, sticky='nsew')


def yes(window, intro, about, yes_button, no_button):
    intro.destroy()
    about.destroy()
    yes_button.destroy()
    no_button.destroy()

    fg='#153450'
    bg='#F4D6BC'
    font=('Times New Roman', 13)

    welcome = tk.Label(window, text='Good to have you back', fg=fg, bg=bg, anchor='center', font=font)
    welcome.grid(row=0, column=7, pady=10, sticky='nsew')

    ask_name = tk.Label(window, text='Please enter your username', fg=fg, bg=bg, anchor='center', font=font)
    ask_name.grid(row=1, column=7, pady=10, sticky='nsew')

    name = tk.Entry(window, fg='#202625', bg='#faddb6')
    name.grid(row=2, column=7, pady=10, sticky='nsew')

    enter_button = tk.Button(window, text='Done', command=lambda: old_user(window,welcome,ask_name,name,enter_button), fg=fg, bg=bg, anchor='center', font=font)
    enter_button.grid(row=3, column=8, pady=10, sticky='nsew')

def no(window, intro, about, yes_button, no_button):
    intro.destroy()
    about.destroy()
    yes_button.destroy()
    no_button.destroy()
    print('no')

def main():
    fg='#153450'
    bg='#F4D6BC'
    font=('Times New Roman', 13)

    window = tk.Tk()
    window.title("Rock Paper Scissors")
    window.configure(bg=bg) 
    window.geometry('700x500')

    # Configure the grid to center widgets
    for i in range(21):
        window.grid_columnconfigure(i, weight=1)

    for i in range(21):
        window.grid_rowconfigure(i, weight=1)

    intro = tk.Label(window, text='Welcome to Rock, Paper and Scissors', fg=fg, bg=bg, anchor='center',font=('Times New Roman', 15, 'bold'))
    intro.grid(row=0, column=7, pady=2, sticky='nsew')

    about = tk.Label(window, text='Are you an old user?', fg=fg, bg=bg, anchor='center',font=('Times New Roman', 13, 'bold'))
    about.grid(row=1, column=7, pady=2, sticky='nsew')
    
    yes_button = tk.Button(window, text='Yes', command=lambda: yes(window, intro, about, yes_button, no_button), fg=fg, bg=bg, height=1, width=3)
    yes_button.grid(row=2, column=5, pady=2, sticky='nsew')
    
    no_button = tk.Button(window, text='No', command=lambda: no(window, intro, about, yes_button, no_button), fg=fg, bg=bg, height=1, width=3)
    no_button.grid(row=2, column=8, pady=2, sticky='nsew')
    
    window.mainloop()

main()
