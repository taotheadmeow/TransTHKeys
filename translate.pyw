import tkinter as tk
import sys
from cx_Freeze import setup, Executable

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        
        self.text_in = tk.Entry(self, width=100)
        self.text_in.pack(side="top", padx=10, pady=5)
        
        self.tr_button = tk.Button(self)
        self.tr_button["text"] = "Translate!"
        self.tr_button["command"] = self.get_data
        self.tr_button.pack(side="bottom", pady=5)

    def get_data(self):
        got_text = self.text_in.get()
        self.text_in.delete(0,'end')
        got_text = self.trans(got_text)
        self.text_in.insert(0, got_text)
    
    def trans(self, text):
        '''translate incorrect language change'''
        en_ = '!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:"ZXCVBNM<>?'
        th_ = '+๑๒๓๔ู฿๕๖๗๘๙๐"ฎฑธํ๊ณฯญฐ,ฅฤฆฏโฌ็๋ษศซ.()ฉฮฺ์?ฒฬฦ'
        eng = "1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./"+en_
        tha = 'ๅ/-ภถุึคตจขชๆไำพะัีรนยบลฃฟหกดเ้่าสวงผปแอิืทมใฝ'+th_
        final = ''
        for i in text:
            if i == ' ':
                final += ' '
                #finalth += ' '
            else:
                try:
                    final += tha[eng.index(i)]
                except:
                    final += eng[tha.index(i)]
        return final

base = None
if (sys.platform == "win32"):
    base = "Win32GUI"
root = tk.Tk()
root.title("TrasTHKeys")
app = Application(master=root)
app.mainloop()

##print('Type "exit" (with out quote) to end this program')
##while 1:
##    text = input('Text: ')
##    if text.lower() == 'exit':
##        break
##    print('Translated:',trans(text))
    




