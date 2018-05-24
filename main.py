import sys
from functions import *
from node import *
from Tkinter import *
import time



if __name__ == '__main__':




    def show_entry_fields(event):
          # write = raw_input("Enter Input Please !\t")
        write = e1.get('1.0', END)[0:-1]
        query = get_input(write)
        # print query
        e2.delete('1.0', END)

        if len(query['class']) > 0 and len(query['attr']) > 0 and query['attr'] != 'none':
            f_n = 'classes/' + query['class'] + '.txt'
            input = query['attr']

        elif len(query['class']) > 0 and len(query['attr']) == 0:
            f_n = 'classes/' + query['class'] + '.txt'
            input = ''

        elif len(query['class']) > 0 and query['attr'] == 'none':
            f_n = 'ide.txt'
            input = query['class']

        elif len(query['class']) == 0:
            f_n = 'ide.txt'
            input = ''

        flag = True
        try : root = fileparse(f_n)
        except:
            # root = fileparse("ide.txt")
            print 'Not found!'
            e2.insert(END, "No match")
            flag = False

        if flag:
            root.search(e2,input)

        # e2.insert(END, "move\n")


    # def press_enter(event):
    #    var = e1.get('1.0', END)
    #    var2 = var[0:-1]
    #    print var2
    #    e1.delete('1.0', END)
    #    e1.insert(END, var2)

    master = Tk()

    # row = Frame(master)
    # master.pack(side=TOP, fill=X, padx=5, pady=5)
    # Label(master, text="First Name").grid(row=0)
    # Label(master, text="Last Name").grid(row=1)

    e1 = Text(master, height=1, width=30)
    e2 = Text(master, height=15, width=30)

    e1.grid(row=0, column=1, sticky=W, pady=4)
    e2.grid(row=1, column=1, sticky=W, pady=4)

    # Button(master, text='Show', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)
    # e1.bind('<Return>',press_enter)
    e1.bind('<KeyRelease>', show_entry_fields)

    master.mainloop()
