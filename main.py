from fpdf import FPDF
import sys,os
from tkinter.filedialog import *
from tkinter import *


class Main():

    def __init__(self):
        self.screen=Tk()
        self.lignes=StringVar(self.screen)
        self.colonnes=StringVar(self.screen)
        self.format=StringVar(self.screen)
        self.images=None

    def import_files(self):
        self.images=askopenfilenames()

    def save_file(self):
        pdf=FPDF()
        for img in range(0,len(self.images)):
            image=self.images[img]
            pdf.add_page(self.format.get())
            for y in range(0,int(self.lignes.get())):
                for x in range(0,int(self.colonnes.get())):
                    pdf.image(image,x*pdf.w/int(self.colonnes.get()),pdf.h/int(self.lignes.get())*y,pdf.w/int(self.colonnes.get()),pdf.h/int(self.lignes.get()))

        chemin = asksaveasfilename(defaultextension=".pdf")
        pdf.output(chemin)
    
    def run(self):
        btn1=Button(self.screen,text="import files",command=self.import_files).pack()

        at = Label(self.screen, text = "nombres de lignes").pack()
        a=Entry(self.screen,textvariable=self.lignes).pack()

        bt = Label(self.screen, text = "nombres de colonnes").pack()
        b=Entry(self.screen,textvariable=self.colonnes).pack()

        ct = Label(self.screen, text = "format du pdf : p ou l").pack()
        c=Entry(self.screen,textvariable=self.format).pack()

        btn2=Button(self.screen,text="save pdf",command=self.save_file).pack()

        self.screen.mainloop()

if __name__=="__main__":
    main=Main()
    main.run()
