from tkinter import *
import back
import sqlite3
import matplotlib.pyplot as plt
import numpy as np



def openapp():
    #affichage du graph en colonne par adresse
    def admin():
        conn = sqlite3.connect("jamel.db")
        cur = conn.cursor()
        cur.execute("SELECT COUNT(Id), address FROM jamel GROUP BY address")
        row = cur.fetchall()
        conn.close()
        objects = []
        target = []
        [objects.append(i[0]) for i in row]
        [target.append(i[1]) for i in row]
        print(len(target))
        plt.bar(np.arange(len(objects)), objects, align='center', alpha=0.5)
        plt.xticks(np.arange(len(target)), target)
        plt.show()
        pass
    #sélection des colonnes

    def get_selected_row(event):
        global selected_tuple
        index = list1.curselection()[0]
        selected_tuple = list1.get(index)
        entry1.delete(0, END)
        entry1.insert(END, selected_tuple[1])
        entry2.delete(0, END)
        entry2.insert(END, selected_tuple[2])
        entry3.delete(0, END)
        entry3.insert(END, selected_tuple[3])
        entry4.delete(0, END)
        entry4.insert(END, selected_tuple[4])
        entry5.delete(0, END)
        entry5.insert(END, selected_tuple[5])
        entry6.delete(0, END)
        entry6.insert(END, selected_tuple[6])
#commande pour voir les données
    def view_command():
        list1.delete(0, END)
        for row in back.view():
            list1.insert(END, row)
#commende pour chercher les données
    def search_command():
        list1.delete(0, END)
        for row in back.search(name_text.get(), address_text.get(), phone_number_text.get(), roomtype_text.get(),
                               noof_text.get(), amount_text.get()):
            list1.insert(END, row)
# commande ajouter le patient
    def add_command():
        back.insert(name_text.get(), address_text.get(), phone_number_text.get(), noof_text.get(), roomtype_text.get(),
                    amount_text.get())
        list1.delete(0, END)
        list1.insert(END, (
        name_text.get(), address_text.get(), phone_number_text.get(), noof_text.get(), roomtype_text.get(),
        amount_text.get()))
#commande supprimer les données
    def delete_command():
        back.delete(selected_tuple[0])
#commande mise à jour
    def update_command():
        back.update(selected_tuple[0], name_text.get(), address_text.get(), phone_number_text.get(),
                    roomtype_text.get(), noof_text.get(), amount_text.get())
# création de l'interface du programme et définir les entrées, les boutons,
    window = Tk()
    window.title("Systeme de vaccination COVID-19")
    window.configure(background="cyan")
    label1 = Label(window, text="Systeme de vaccination COVID-19", font=('none 13 bold'))
    label1.grid(row=0, column=2)

    label2 = Label(window, text="NOM ET PRÉNOM", font=('none 13 bold'))
    label2.grid(row=1, column=0)

    label3 = Label(window, text="Addresse", font=('none 13 bold'))
    label3.grid(row=2, column=0)

    label4 = Label(window, text="TÉLÉPHONE", font=('none 13 bold'))
    label4.grid(row=3, column=0)

    label5 = Label(window, text="Age", font=('none 13 bold'))
    label5.grid(row=4, column=0)

    label6 = Label(window, text="Dose", font=('none 13 bold'))
    label6.grid(row=5, column=0)

    label7 = Label(window, text="patient Id", font=('none 13 bold'))
    label7.grid(row=6, column=0)
# définir les 6 entrés 
    name_text = StringVar()
    entry1 = Entry(window, textvariable=name_text)
    entry1.grid(row=1, column=1)

    address_text = StringVar()
    entry2 = Entry(window, textvariable=address_text)
    entry2.grid(row=2, column=1)

    phone_number_text = StringVar()
    entry3 = Entry(window, textvariable=phone_number_text)
    entry3.grid(row=3, column=1)

    noof_text = StringVar()
    entry4 = Entry(window, textvariable=noof_text)
    entry4.grid(row=4, column=1)

    roomtype_text = StringVar()
    entry5 = Entry(window, textvariable=roomtype_text)
    entry5.grid(row=5, column=1)

    amount_text = StringVar()
    entry6 = Entry(window, textvariable=amount_text)
    entry6.grid(row=6, column=1)

    list1 = Listbox(window, height=20, width=59)
    list1.grid(row=1, column=3, rowspan=6, columnspan=2)
# graph et les boutons
    scrl = Scrollbar(window)
    scrl.grid(row=1, column=2, sticky='ns', rowspan=6)

    list1.configure(yscrollcommand=scrl.set)
    scrl.configure(command=list1.yview)

    list1.bind('<<ListboxSelect>>', get_selected_row)

    b1 = Button(window, text="voir tout", width=12, command=view_command, font=('none 13 bold'), relief=RAISED)
    b1.grid(row=7, column=0)

    b2 = Button(window, text="ajouter", width=12, fg="green", command=add_command, font=('none 13 bold'),
                relief=RAISED)
    b2.grid(row=8, column=0)

    b3 = Button(window, text="supprimer", width=12, fg="red", command=delete_command, font=('none 13 bold'),
                relief=RAISED)
    b3.grid(row=10, column=0)

    b6 = Button(window, text="graphe", width=12, fg="SlateBlue1", command=admin, font=('none 13 bold'),
                relief=RAISED)
    b6.grid(row=10, column=1)

    b4 = Button(window, text="chercher", width=12, command=search_command, font=('none 13 bold'), relief=RAISED)
    b4.grid(row=7, column=1)

    b5 = Button(window, text="mise à jour", width=12, fg="blue", command=update_command, font=('none 13 bold'),
                relief=RAISED)
    b5.grid(row=8, column=1)

    window.mainloop()



from tkinter import messagebox as ms
import sqlite3

# création  de base de donnée et utilisateur s'il n'existe pas dès le lacement du programme
with sqlite3.connect('quit.db') as db:
    c = db.cursor()

c.execute('CREATE TABLE IF NOT EXISTS user (username TEXT NOT NULL ,password TEX NOT NULL);')
db.commit()
db.close()


# main Classe
class main:
    def __init__(self, master):
        self.master = master
        # les variables
        self.username = StringVar()
        self.password = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()
        # Create Widgets
        self.widgets()

    # fonction connection
    def login(self):
        #Connection
        with sqlite3.connect('quit.db') as db:
            c = db.cursor()

        # recherche si le nom d'utlilisateur et mot de passe éxiste dans la base de donnée
        find_user = ('SELECT * FROM user WHERE username = ? and password = ?')
        c.execute(find_user, [(self.username.get()), (self.password.get())])
        result = c.fetchall()
        if result:
            root.destroy()
            openapp()
        else:
            ms.showerror('Oops!','pas utilisateur à ce nom')

    def new_user(self):
        # Établissement de la connection
        with sqlite3.connect('quit.db') as db:
            c = db.cursor()

        # Find Existing username if any take proper action
        find_user = ('SELECT * FROM user WHERE username = ?')
        c.execute(find_user, [(self.username.get())])
        if c.fetchall():
            ms.showerror('Erreur!', 'utilisateur existant')
        else:
            ms.showinfo('Success!', 'compte crée')
            self.log()
        # Création de nouveau compte
        insert = 'INSERT INTO user(username,password) VALUES(?,?)'
        c.execute(insert, [(self.n_username.get()), (self.n_password.get())])
        db.commit()


# connection
    def log(self):
        self.username.set('')
        self.password.set('')
        self.crf.pack_forget()
        self.head['text'] = 'LOGIN'
        self.logf.pack()
#creation du compte
    def cr(self):
        self.n_username.set('')
        self.n_password.set('')
        self.logf.pack_forget()
        self.head['text'] = 'Créer un compte'
        self.crf.pack()

    # définir les entré du programme

    def widgets(self):
        self.head = Label(self.master, text='LOGIN', font=('', 35), pady=10)
        self.head.pack()
        self.logf = Frame(self.master, padx=10, pady=10)
        Label(self.logf, text='Nom: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.logf, textvariable=self.username, bd=5, font=('', 15)).grid(row=0, column=1)
        Label(self.logf, text='mot de passe: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.logf, textvariable=self.password, bd=5, font=('', 15), show='*').grid(row=1, column=1)
        Button(self.logf, text=' connection ', bd=3, font=('', 15), padx=5, pady=5, command=self.login, bg="gold2").grid()
        Button(self.logf, text=' Crée un compte ', bd=3, font=('', 15), padx=5, pady=5, command=self.cr,
               bg="powder blue").grid(row=2, column=1)
        self.logf.pack()

# création des entrées de la première interface du programme le login et la création du compte
        self.crf = Frame(self.master, padx=10, pady=10)
        Label(self.crf, text='NOM: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.crf, textvariable=self.n_username, bd=5, font=('', 15)).grid(row=0, column=1)
        Label(self.crf, text='mot de passe: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.crf, textvariable=self.n_password, bd=5, font=('', 15), show='*').grid(row=1, column=1)
        Button(self.crf, text='Crée le compte', bd=3, font=('', 15), padx=5, pady=5, command=self.new_user).grid()
        Button(self.crf, text='retour', bd=3, font=('', 15), padx=5, pady=5, command=self.log).grid(row=2,
                                                                                                         column=1)


# création de la fenetre de l'application
root = Tk()
root.title("Vaccin COVID-19")
main(root)
root.mainloop()
