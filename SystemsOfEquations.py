import numpy as np
import math
import numpy.linalg
from tkinter import *


class Application():         

    def __init__(self, root):

        self.window = root 
        self.makeCanvas = Canvas(self.window, width = 500, height = 500, bg='chocolate')
        self.makeCanvas.place(x=0,y=0)

        # Position Entry boxes
        self.posX = 100
        self.posY = 100
        self.count = 0

        #Title
        self.title = Label(self.window, text="3 x 3 System of equations solver", width = 30, bg='chocolate', font=('Arial', 15))
        self.title.place(x=60, y = 30)

        # Values of system of equations
        self.xVal = None
        self.yVal = None
        self.zVal = None

        # Nine Entry boxes
        self.entries = np.zeros((3,3), dtype=int)

        self.matrix = [Entry(self.window, fg='black', bd=2, width=5) for x in range(9)]
        for entry in self.matrix:
            if self.count == 3:
                self.posY += 100
                self.posX = 100
                self.count = 0

            entry.place(x=self.posX, y=self.posY)
            self.posX += 104
            self.count += 1
        
        # Matrix entries
        self.yEquatesPos = 100
        self.equates = [Entry(self.window,bd=2, width=5) for x in range(3)]
        for i in self.equates:
            i.place(x=425, y=self.yEquatesPos)
            self.yEquatesPos += 100
         
        # X Labels
        self.xLabel = Label(self.window, text='X', width=3, bg='chocolate', font=('Arial',12))
        self.xLabel.place(x=90,y=450)
        self.equal1Label = Label(self.window, text='=', bg='chocolate', font=('Arial',12))
        self.equal1Label.place(x=115,y=450)
        self.value1Label = Label(self.window, text=str(self.xVal), bg='chocolate', font = ('Arial', 12))
        self.value1Label.place(x = 130, y = 450)

        # Y Labels
        self.yLabel = Label(self.window, text='Y', width=3, bg='chocolate', font=('Arial',12))
        self.yLabel.place(x=190,y=450)
        self.equal2Label = Label(self.window, text='=', bg='chocolate', font=('Arial',12))
        self.equal2Label.place(x=215,y=450)
        self.value2Label = Label(self.window, text=str(self.yVal), bg='chocolate', font = ('Arial', 12))
        self.value2Label.place(x = 230, y = 450)

        # Z Labels
        self.zLabel = Label(self.window, text='Z', width=3, bg='chocolate', font=('Arial',12))
        self.zLabel.place(x=290,y=450)
        self.equal3Label = Label(self.window, text='=', bg='chocolate', font=('Arial',12))
        self.equal3Label.place(x=315,y=450)
        self.value3Label = Label(self.window, text=str(self.yVal), bg='chocolate', font = ('Arial', 12))
        self.value3Label.place(x = 330, y = 450)
 
        # Buttons
        self.calcButton = Button(self.window, bg='green',text='Calculate', width = 8, height=1, command  = lambda: self.takeInputMatrix(self.matrix, self.equates))
        self.calcButton.place(x=140,y=400)

        self.clearButton = Button(self.window, bg='red', text='Clear', width = 8, height=1, command=self.clear )
        self.clearButton.place(x=260,y=400)

        # Matrix lines
        self.makeCanvas.create_line(70, 80, 70, 340, width=4)
        self.makeCanvas.create_line(375, 80, 375, 340, width=4)

        self.makeCanvas.create_line(68, 80, 100, 80, width=4)
        self.makeCanvas.create_line(68, 340, 100, 340, width=4)

        self.makeCanvas.create_line(345, 80, 377, 80, width=4)
        self.makeCanvas.create_line(345, 340, 377, 340, width=4)

        # Equals signs
        self.makeCanvas.create_line(390,105,410,105,width=3)
        self.makeCanvas.create_line(390,115,410,115,width=3)

        self.makeCanvas.create_line(390,205,410,205,width=3)
        self.makeCanvas.create_line(390,215,410,215,width=3)

        self.makeCanvas.create_line(390,305,410,305,width=3)
        self.makeCanvas.create_line(390,315,410,315,width=3)

    #create a function takeInput
    def takeInputMatrix(self, matrix, equates):

        valListMatrix = []
        for entry in matrix:
            valListMatrix.append(int(entry.get()))

        self.entries = np.reshape(valListMatrix,(3,3))
        

        # Equates list
        equatesList = []
        for entry in equates:
            equatesList.append(int(entry.get()))
        
        #must fill in whole matrix for this to work
        self.calcDeterminants(self.entries, equatesList)
    
        
    def calcDeterminants(self, matrix, equates):

    #DmD,DxM,DyM,DzM = np.array(matrix)
        DmD = np.array(matrix)
        DxM = np.array(matrix)
        DyM = np.array(matrix)
        DzM = np.array(matrix)

        for i in range(0, np.size(equates)):
            DxM[i][0] = equates[i]
            DyM[i][1] = equates[i]
            DzM[i][2] = equates[i]
        
        Dm = np.linalg.det(DmD)
        Dx = np.linalg.det(DxM)
        Dy = np.linalg.det(DyM)
        Dz = np.linalg.det(DzM) 
        
        # Calculate Values after getting determinants
        rX = round(Dx/Dm)
        rY = round(Dy/Dm)
        rZ = round(Dz/Dm)

        self.xVal = int(rX)
        self.yVal = int(rY)
        self.zVal = int(rZ)

        self.value1Label.config(text=self.xVal)
        self.value2Label.config(text=self.yVal)
        self.value3Label.config(text=self.zVal)

        print(self.xVal,self.yVal,self.zVal)
    
    def clear(self):
        for entry in self.matrix:
            entry.delete(0,END)
        
        for entry in self.equates:
            entry.delete(0,END)

def main():
    window = Tk()
    window.title("3x3 System of equations solver")
    window.geometry("500x500")
    window.maxsize(500,500)
    window.minsize(500,500)
    
    Application(window)
    window.mainloop()


if __name__ == "__main__":
    main()
