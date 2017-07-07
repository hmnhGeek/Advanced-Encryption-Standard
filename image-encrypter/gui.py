from Tkinter import *
import ttk
from tkFileDialog import *
import imageencrypt as icr
import imagefinder as imgf
import tkMessageBox as tkmb

# fonts
buttonfont = ('arial', 15)
chosenlabelfont = ('arial', 11)
normallabelfont = ('arial', 20)

#padding
normalpadding = 10

# colors
LIGHT_YELLOW = 'light yellow'
VIOLET = 'violet'
WHITE = 'white'
BLUE = 'blue'
GREEN = 'light green'
GOLDEN = 'orange'

# normal button width
WIDTH = 10

# window normal size
WINDOW_SIZE = '500x400'

class Page(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)

    def show(self):
        self.lift()


# Initialising a folderpage class here.
class folderpage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        self.var1 = IntVar()
        self.var2 = IntVar()

        self.config(background = LIGHT_YELLOW)

        self.chosen = Label(self, font = chosenlabelfont, bg = LIGHT_YELLOW, fg = GOLDEN)
        self.chosen.pack()

        choose_folder = Button(self, text = 'Choose a folder', command = self.update, font = buttonfont,
                               bg = LIGHT_YELLOW, activebackground = GREEN, activeforeground = WHITE)
        choose_folder.pack(pady = 10)

        self.password = ttk.Entry(self, show = '*', font = buttonfont)
        self.password.pack(pady = 5)

        self.encrypt = Radiobutton(self, text="Encrypt", variable=self.var2, value=1,
                                   command = self.check, font = buttonfont,
                                   bg = LIGHT_YELLOW, activebackground = VIOLET, activeforeground = WHITE)
        self.encrypt.pack( anchor = W, pady = 5, padx = normalpadding)

        self.decrypt = Radiobutton(self, text="Decrypt", variable=self.var2, value=2,
                                   command = self.check, font = buttonfont
                                   , bg = LIGHT_YELLOW, activebackground = VIOLET, activeforeground = WHITE)
        self.decrypt.pack( anchor = W, pady = 5 , padx = normalpadding)

        self.keeporg = Checkbutton(self, text="Keep Original Files", variable=self.var1, font = buttonfont
                                   , bg = LIGHT_YELLOW, activebackground = VIOLET, activeforeground = WHITE)
        self.keeporg.pack( anchor = W, pady = 5 , padx = normalpadding)
        
        self.submit = Button(self, text = 'Submit', command = self.feed_to_algo, font = buttonfont,
                             bg = LIGHT_YELLOW, activebackground = VIOLET, activeforeground = WHITE,
                             width = WIDTH)
        self.submit.pack(pady = normalpadding/2)

        self.goback = Button(self, text = 'Go Home', command = hp.show, font = buttonfont,
                             bg = LIGHT_YELLOW, activebackground = VIOLET, activeforeground = WHITE,
                             width = WIDTH)
        self.goback.pack(pady = normalpadding/2)

        self.submit.config(state = 'disabled')
        self.keeporg.config(state = 'disabled')

    def check(self):
        if self.var2.get() == 1:
            self.keeporg.config(state = 'normal')

        elif self.var2.get() == 2:
            self.keeporg.config(state = 'disabled')

    def update(self):
        try:
            directory = askdirectory()
            self.chosen['text'] = str(directory)

            if str(self.submit['state']) == 'disabled':
                self.submit.config(state = 'normal')
        except:
            pass

    def feed_to_algo(self):
        if self.password.get() != '':

            if self.var2.get() == 1:
                
                # get all the images in this folder.
                addr = self.chosen['text']
                images = imgf.findallimages(addr)

                if addr[-1] != '/':
                    addr+='/'

                for image in images:
                    try:
                        if self.var1.get() == 1:
                            icr.encrypt(self.password.get(), addr+image, True)
                        else:
                            icr.encrypt(self.password.get(), addr+image, False)
                    except:
                        tkmb.showwarning("Alert", "Unable to encrypt: File name smaller than key for: "+addr+image)
                tkmb.showinfo("Alert", "Done Encryption!!")
            else:
                addr = self.chosen['text']
                dats = imgf.findallbinaries(addr)

                if addr[-1] != '/':
                    addr += '/'

                for dat in dats:
                    try:
                        icr.decrypt(self.password.get(), addr+dat)
                    except RuntimeError:
                        tkmb.showwarning("Unable to decrypt: Different password has been set for the file: "+addr+dat)
                        continue
                tkmb.showinfo("Alert", "Done Decryption!!")
        else:
            tkmb.showwarning("Alert", "Please enter a password.")

        hp.show()

# Initialising the imagepage here.
class imagepage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        self.var3 = IntVar()
        self.var4 = IntVar()

        self.config(background = LIGHT_YELLOW)

        self.chosen = Label(self, font = chosenlabelfont, bg = LIGHT_YELLOW, fg = GOLDEN)
        self.chosen.pack()

        choose_folder = Button(self, text = 'Choose an Image or an Encrypted Image', command = self.update,
                               font = buttonfont,
                               bg = LIGHT_YELLOW, activebackground = GREEN, activeforeground = WHITE)
        choose_folder.pack(pady = 10)

        self.password = Entry(self, show = '*', font = buttonfont)
        self.password.pack(pady = 5)

        self.encrypt = Radiobutton(self, text="Encrypt", variable=self.var4, value=1, command = self.check,
                                   font = buttonfont,
                                   bg = LIGHT_YELLOW, activebackground = VIOLET, activeforeground = WHITE)
        self.encrypt.pack( anchor = W, pady = 5 , padx = normalpadding)

        self.decrypt = Radiobutton(self, text="Decrypt", variable=self.var4, value=2, command = self.check,
                                   font = buttonfont,
                                   bg = LIGHT_YELLOW, activebackground = VIOLET, activeforeground = WHITE)
        self.decrypt.pack( anchor = W, pady = 5 , padx = normalpadding)

        self.keeporg = Checkbutton(self, text="Keep Original File", variable=self.var3, font = buttonfont,
                                   bg = LIGHT_YELLOW, activebackground = VIOLET, activeforeground = WHITE)
        self.keeporg.pack( anchor = W, pady = 5 , padx = normalpadding)
        
        self.submit = Button(self, text = 'Submit', command = self.feed_to_algo, font = buttonfont,
                                   bg = LIGHT_YELLOW, activebackground = VIOLET, activeforeground = WHITE,
                             width = WIDTH)
        self.submit.pack(pady = normalpadding/2)

        self.goback = Button(self, text = 'Go Home', command = hp.show, font = buttonfont,
                                   bg = LIGHT_YELLOW, activebackground = VIOLET, activeforeground = WHITE,
                             width = WIDTH)
        self.goback.pack(pady = normalpadding/2)

        self.submit.config(state = 'disabled')
        self.keeporg.config(state = 'disabled')

    def check(self):
        if self.var4.get() == 1:
            self.keeporg.config(state = 'normal')
            
        elif self.var4.get() == 2:
            self.keeporg.config(state = 'disabled')

    def update(self):
        try:
            Image = askopenfile()
            self.chosen['text'] = str(Image.name)

            if str(self.submit['state']) == 'disabled':
                self.submit.config(state = 'normal')
        except:
            pass

    def feed_to_algo(self):

        if self.password.get() != '':
            
            if self.var4.get() == 1:
                
                # get all the images in this folder.
                addr = self.chosen['text']

                try:
                    if self.var3.get() == 1:
                        icr.encrypt(self.password.get(), addr, True)
                    else:
                        icr.encrypt(self.password.get(), addr, False)

                    tkmb.showinfo("Alert", "Done Encryption!!")
                except:
                    tkmb.showwarning("Alert", "Unable to encrypt: File name smaller than key for: "+addr)
            else:
                addr = self.chosen['text']

                try:
                    icr.decrypt(self.password.get(), addr)
                    tkmb.showinfo("Alert", "Done Decryption!!")
                except RuntimeError:
                    tkmb.showwarning("Unable to decrypt: Different password has been set for the file: "+addr)
        else:
            tkmb.showwarning("Alert", "Please enter a password.")

        hp.show()


# home page showing whether to perform action on a folder or on a file.
class homepage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.var = IntVar()
        self.config(background = LIGHT_YELLOW)
        label1 = Label(self, text = 'Perform action', font = normallabelfont, fg = BLUE, bg = LIGHT_YELLOW)
        label1.pack(pady = normalpadding)

        R1 = Radiobutton(self, text="On Folder", variable=self.var,
                         bg = LIGHT_YELLOW, value=1, command = self.setoperation_target, font = buttonfont
                         , activebackground = VIOLET, activeforeground = WHITE)
        R1.pack( anchor = W , pady = normalpadding, padx = normalpadding**2 + 8*normalpadding)

        R2 = Radiobutton(self, text="On Image", variable=self.var,
                         bg = LIGHT_YELLOW, value=2, command = self.setoperation_target, font = buttonfont
                         , activebackground = VIOLET, activeforeground = WHITE)
        R2.pack( anchor = W ,pady = normalpadding, padx = normalpadding**2 + 8*normalpadding)

    def setoperation_target(self):
        if self.var.get() == 1:
            fp.password.delete(0, END)
            fp.chosen['text'] = ''
            fp.submit.config(state = 'disabled')
            fp.show()
        elif self.var.get() == 2:
            ip.password.delete(0, END)
            ip.chosen['text'] = ''
            ip.submit.config(state = 'disabled')
            ip.show()

class MainView(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)

        '''
        Say if you defined a page class PageOne(). Initialise
        its object here. Like self.p1 = PageOne().

        self.container = Frame(self)
        self.container.pack(side = 'top', fill = 'both', expand = True)

        Then define the container here.
        self.p1.place(in_ = self.container, x = 0, y = 0, relwidth = 1, relheight = 1)

        Then show the page.
        self.p1.show()
        '''

        hp = homepage()
        fp = folderpage()
        ip = imagepage()

        global hp
        global fp
        global ip
        
        self.container = Frame(self)
        self.container.pack(side = 'top', fill = 'both', expand = True)

        hp.place(in_ = self.container, x = 0, y = 0, relwidth = 1, relheight = 1)
        fp.place(in_ = self.container, x = 0, y = 0, relwidth = 1, relheight = 1)
        ip.place(in_ = self.container, x = 0, y = 0, relwidth = 1, relheight = 1)

        hp.show()

if __name__ == '__main__':
    root = Tk()

    main = MainView(root)
    main.pack(side = 'top', fill = 'both', expand = True)

    root.wm_geometry(WINDOW_SIZE)
    root.resizable(height = 0, width = 0)
    
    root.title('AES Image Encrypter-Decrypter')

    root.mainloop()
        
        
