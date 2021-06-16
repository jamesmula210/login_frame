from tkinter import *
import tkinter.messagebox as ms


class LoginForm(Frame):
    def __init__(self, classic):
        super(LoginForm, self).__init__(classic)
        self.username = Label(self, text = "username", font = ("Comics Sans",40))
        self.password = Label(self, text = "password", font = ("Comics Sans", 40))

        self.username_login = Entry(self)
        self.password_login = Entry(self)

        self.username_login.grid(column = 2, row=1)
        self.password_login.grid(column = 2, row = 2, sticky = E)
        self.username.grid(row = 1, sticky = E)
        self.password.grid(row = 3, sticky = E)

        self.btn = Button(self, text = "Login", command = self.login)
        self.btn.grid(colimnspan = 4)

        self.pack()

        def login(self):
            password = self.password_login.get()
            username = self.username_login.get()

            if (username == 'james' and password == 'cracker'):
                ms.showinfo("Login", 'nice to meet you')
            else:
                ms.showinfo('Login', 'login failed')

        james = Tk()
        login = LoginForm(james)
        james.mainloop()
