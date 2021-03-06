from tkinter import * #from Tkinter import *                               # Using Tkinter for GUI properties
from tkinter import messagebox                                             # Importing MessageBox module

#from tkinter import ttk
LARGE_FONT= ("Verdana", 12)

class Application(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        container = Frame(self)

        container.pack(side="top", fill="both", expand= True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {}

        for F in (LoginPage, GuestUserPage, OrdinaryUserPage, SuperUserPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")

        self.show_frame(LoginPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        if cont == LoginPage:
            Tk.wm_title(self, "Login Page")
        elif cont == GuestUserPage:
            Tk.wm_title(self, "Guest User Page")
        elif cont == OrdinaryUserPage:
            Tk.wm_title(self, "Ordinary User Page")
        elif cont == SuperUserPage:
            Tk.wm_title(self, "Super User Page")
        else:
            Tk.wm_title(self, "DSS")

class LoginPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='red')

        self.controller = controller

        Label0 = Label(self, text='Login Page', font="Times 16 bold")
        Label0.pack(padx=15, pady=5)

        Label1 = Label(self, text='Username:')
        Label1.pack(padx=15, pady=5)

        self.entry1 = Entry(self, bd=5)
        self.entry1.pack(padx=15, pady=5)

        Label2 = Label(self, text='Password:')
        Label2.pack(padx=15, pady=6)

        self.entry2 = Entry(self, bd=5)
        self.entry2.pack(padx=15, pady=7)

        btn = Button(self, text='Check Login',
                        command=self.RegisteredUserLogin)    # Button to click to check login credentials

        btn2 = Button(self, text='Login as Guest User',
                        command=self.GuestUserLogin)      # Button to log in as a guest

        btn.pack(padx=5)
        btn2.pack(padx=6)

    def RegisteredUserLogin(self):
        username = self.entry1.get()
        password = self.entry2.get()
        if(username == 's' and password == 's'):
            self.controller.show_frame(SuperUserPage)
        elif(username == 'o' and password == 'o'):
            self.controller.show_frame(OrdinaryUserPage)
        else:
            messagebox.showinfo('Status', 'Invalid Login, Please Try Again')

    def GuestUserLogin(self):
        self.controller.show_frame(GuestUserPage)

class GuestUserPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='green')

        Label1 = Label(self, text='Welcome Guest User!', font="Times 25 bold")
        Label1.pack(padx=15, pady=5)

        fram = Frame(self)

        Labe0 = Label(self, text='What would you like to do?', font="Times 16 bold")
        Labe0.pack(padx=15, pady=5)

        but0 = Button(fram, text='Read open documents')          # Providing buttons for various GU options
        but0.pack(side=TOP, padx=5, pady=5)

        but1 = Button(fram, text='Retrieve old versions')
        but1.pack(side=TOP, padx=6, pady=5)

        but2 = Button(fram, text='Complain about documents')
        but2.pack(side=TOP, padx=7, pady=5)

        but3 = Button(fram, text='Send Taboo word suggestions to SU')
        but3.pack(side=TOP, padx=7, pady=5)

        but4 = Button(fram, text='Apply to be OU')
        but4.pack(side=TOP, padx=7, pady=5)

        fram.pack(padx=100, pady=19)

        button = Button(self, text="Visit Login Page",
                            command=lambda: controller.show_frame(LoginPage))
        button.pack()


class OrdinaryUserPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='yellow')

        Labe = Label(self, text='Correct Login, Welcome Ordinary User!', font="Times 25 bold")
        Labe.pack(padx=15, pady=5)

        fra = Frame(self)

        Labe0 = Label(self, text='What would you like to do?', font="Times 16 bold")
        Labe0.pack(padx=15, pady=5)

        but0 = Button(fra, text='Create new document', command=self.create_new_document_window )         # Providing buttons for various OU options
        but0.pack(side=TOP, padx=5, pady=5)

        but1 = Button(fra, text='Invite OUs')
        but1.pack(side=TOP, padx=6, pady=5)

        but2 = Button(fra, text='Accept or Deny invitations')
        but2.pack(side=TOP, padx=7, pady=5)

        but3 = Button(fra, text='Get info about other OUs')
        but3.pack(side=TOP, padx=8, pady=5)

        but4 = Button(fra, text='Process Complaints of OUs')
        but4.pack(side=TOP, padx=9, pady=5)

        Labe1 = Label(fra, text='Recent Documents: ', font="Times 25 bold")
        Labe1.pack(side=TOP, padx=11, pady=5)

        button8 = Button(fra, text='Document 1')
        button8.pack(side=LEFT, padx=14, pady=5)

        button9 = Button(fra, text='Document 2')
        button9.pack(side=LEFT, padx=13, pady=5)

        button9 = Button(fra, text='Document 3')
        button9.pack(side=LEFT, padx=12, pady=5)

        button10 = Button(self, text='Add Profile Picture')
        button10.pack(anchor='nw', padx=5, pady=0)
        button10.config(height='6', width='6')

        fra.pack(padx=100, pady=19)

        button = Button(self, text="Visit Login User Page",
                            command=lambda: controller.show_frame(LoginPage))
        button.pack()

    def create_new_document_window(self):
        cnd_window = Tk()
        cnd_fram = Frame(cnd_window)
        cnd_label = Label(cnd_fram, text= "Enter file name:")
        cnd_label.pack(side = LEFT)
        self.cnd_entry = Entry(cnd_fram, bd = 5)
        self.cnd_entry.pack(side = RIGHT)
        cnd_button = Button(cnd_fram, text='Submit', command=self.create_new_document)
        cnd_button.pack(side = RIGHT)
        cnd_fram.pack()
        cnd_window.mainloop()

    def create_new_document(self):
        new_file_name = self.cnd_entry.get() + ".txt"
        import os
        file_names = os.listdir("C:/Users/saddi/Desktop/CSC-322-Project/Document")
        if new_file_name in file_names:
            print(new_file_name)
        else:
            open("C:/Users/saddi/Desktop/CSC-322-Project/Document/" + new_file_name, "w")
        # while
        # try:
        #     file_name = "Untitled_" + i + ".txt"
        #     file = open(file_name, "r")
        # except:


class SuperUserPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg='yellow')

        fr = Frame(self)

        Lab = Label(self, text='Correct Login, Welcome Super User!', font="Times 25 bold")
        Lab.pack(padx=15, pady=5)

        Lab0 = Label(self, text='What would you like to do?', font="Times 16 bold")
        Lab0.pack(padx=15, pady=6)

        button0 = Button(fr, text='See taboo words')            # Providing buttons for various SU options
        button0.pack(side=TOP, padx=5, pady=5)

        button1 = Button(fr, text='Unlock Locked documents')
        button1.pack(side=TOP, padx=6, pady=5)

        button2 = Button(fr, text='Update Membership')
        button2.pack(side=TOP, padx=7, pady=5)

        button3 = Button(fr, text='Process Complaints of OUs')
        button3.pack(side=TOP, padx=8, pady=5)

        button4 = Button(fr, text='Create new document')
        button4.pack(side=TOP, padx=9, pady=5)

        button5 = Button(fr, text='Invite OUs')
        button5.pack(side=TOP, padx=10, pady=5)

        button6 = Button(fr, text='Accept/Deny invitations')
        button6.pack(side=TOP, padx=11, pady=5)

        button7 = Button(fr, text='Get info about other OUs')
        button7.pack(side=TOP, padx=12, pady=5)

        Lab1 = Label(fr, text='Recent Documents: ', font="Times 25 bold")
        Lab1.pack(side=TOP, padx=14, pady=5)

        button8 = Button(fr, text='Document 1')
        button8.pack(side=LEFT, padx=17, pady=5)

        button9 = Button(fr, text='Document 2')
        button9.pack(side=LEFT, padx=16, pady=5)

        button9 = Button(fr, text='Document 3')
        button9.pack(side=LEFT, padx=15, pady=5)

        button10 = Button(self, text='Add Profile Picture')
        button10.pack(anchor='nw', padx=5, pady=0)
        button10.config(height='6', width='6')

        fr.pack(padx=100, pady=19)

        button = Button(self, text="Visit Login User Page",
                            command=lambda: controller.show_frame(LoginPage))
        button.pack()

app = Application()
app.mainloop()
