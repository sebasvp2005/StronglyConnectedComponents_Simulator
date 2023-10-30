from tkinter import * 
import random
from controller import *
from math import atan, cos, sin
from PIL import Image

#before run the code, execute 'pip install -r requirements.txt'

class Base():
    def __init__(self):
        self.window = Tk()
        self.window.geometry("1000x700")

class button():
        
    def __init__(self, window, x:int, y:int, width:int, height:int, img) -> None:
        self.border=Frame(window, height=height, width=width)
        self.border.config(bg='white')
        self.widget = Button(self.border, command=lambda: self.click(), border=0, image=img, height=height-4, width=width-4, compound='c', bg='#1e1e1e')
        self.x=x
        self.y=y
        self.active = False
        self.widget.place(x=0, y=0)

    def click(self):
        self.active ^= 1
        self.widget.config(bg= 'white' if self.active else '#1e1e1e')

    def set(self, a:bool):
        self.active = a
        self.widget.config(bg= 'white' if self.active else '#1e1e1e')

    def makeVisibe(self)->None:
        self.border.place(x=self.x, y= self.y)

    def makenotvisible(self)->None:
        self.border.place_forget()

    def clear(self):
        self.active = 0;
        self.widget.config(bg = '#1e1e1e')
    def isactive(self): return self.active
    

class Main(Base):
    def __init__(self):
        super().__init__()

        self.img = PhotoImage(width=1, height=1)
        self.window.title('Strongly-Connectec-Components')
        self.nodes=[]

        self.dimension = 0

        self.window.config(bg='#333333',)
        Label(self.window, text='Graph-components', bg='#333333', foreground='white', font=('bold', 25)).place(x=30, y=10)
        Label(self.window, text='Matriz Adyacencia', bg='#333333', foreground='white', font='bold').place(x=20, y=70)
        Frame(self.window, width=960, height=1).place(x=20, y=60)

        self.button_plus = Button(self.window, height=1, width=20 , text="+", command= lambda: self.DisplayMatrix(min(self.dimension+1, 15)))
        self.button_plus.place(x=20, y=100)
        self.button_minus = Button(self.window, height=1, width=20 , text="-", command= lambda: self.DisplayMatrix(max(self.dimension-1, 7)))
        self.button_minus.place(x=210, y=100)

        self.matrix_frame = Frame(self.window, height=400, width=500, borderwidth=1)
        self.matrix_frame.config(bg='#333333')
        self.matrix_frame.place(x=20, y=130)
        self.matrix =[[button(window=self.matrix_frame, x =  30 * j, y =20+ 25*i, height=20, width=25, img=self.img) for j in range(15)] for i in range(15)]

        #button
        self.clear_button = Button(self.window, height=1, width=5, text='clear', command= lambda: self.clear_matrix())

        self.generate_random = Button(self.window, height=1, width=8, text='randomize', command= lambda:self.randomize() )

        self.create_button = Button(self.window, height=1, width=8, text='create', command= lambda:self.draw_graph() )

        self.process_button = Button(self.window, height=1, width=8, text='process', command= lambda:self.ShowProcess() )
        self.manual_button = Button(self.window, height=1, width=8, text='manual', command=lambda: self.manual_input())


        #frames

        self.Text_Frame = Frame(self.window, height=100, width=950, bg='#333333')
        self.Text_Frame.place(x=20, y=370)
        Label(self.Text_Frame, bg='#333333' , foreground='white', font='bold',anchor=W,
                                  text='Componentes Conexas: Las  componentes  conexas  de  un  grafo  son  los  subgrafos  conexos  disjuntos  con  el  mayor número de \nvértices, que se pueden formar a partir del grafo original. Estos componentes se caracterizan por: por cada arista a,b existe camino de\n a-b y existe camino b-a'
                                  ).place(x=0, y=10)


        Label(self.window, text='Graph', bg='#333333', foreground='white', font='bold').place(x=480, y=70)
        self.graph_frame = Frame(self.window, height=200, width=500)
        self.graph_frame.place(x=480, y=100)

        self.graph_canva = Canvas(self.graph_frame, height=196, width=496, bg='#1e1e1e')
        self.graph_canva.place(x=0, y=0)


        Label(self.window, text='Components', bg='#333333', foreground='white', font='bold').place(x=480, y=320)
        self.components_frame= Frame(self.window, height=200, width=500)
        self.components_frame.place(x=480, y=350)
        self.components_canva = Canvas(self.components_frame, height=196, width=496, bg='#1e1e1e')
        self.components_canva.place(x=0, y=0)

        self.label_ans = Label(self.window, bg='#333333' , foreground='white', font='bold')
        self.label_ans.place(x=580, y=320)



        self.DisplayMatrix(7)
        self.window.mainloop()
    def manual_input(self):

        #before run the code, change the rute.
        imagen = Image.open("manual.jpg")
        imagen.show()
    
    def DisplayMatrix(self, n:int):
        if self.dimension==n:return
        self.Text_Frame.place(x=20, y=575)
        self.clear_button.place(x=20, y= n*25 + 160)
        self.generate_random.place(x=80, y= n*25 + 160)
        self.create_button.place(x=160, y= n*25 + 160)
        self.process_button.place(x = 200, y =n*25 +160)
        self.manual_button.place( x = 220, y = n*25 + 160 )
        self.dimension=n
        for i in range(15):
            for j in range(15):
                if j<n and i<n: self.matrix[i][j].makeVisibe()
                else: self.matrix[i][j].makenotvisible()
    
    def clear_matrix(self):
        for row in self.matrix:
            for cell in row: cell.clear()

    def randomize(self):
        for i in range(self.dimension):
            for j in range(self.dimension):
                if random.randint(0, self.dimension)==0: self.matrix[i][j].set(1)
                else: self.matrix[i][j].set(0)
    
    def draw_graph(self):
        self.graph_canva.delete("all")
        self.components_canva.delete("all")
        nodes =[[] for i in range(self.dimension)]
        location = [[random.randint(50, 420), random.randint(10, 170)] for i in range(self.dimension)]
        for i in range(self.dimension):
            for j in range(self.dimension):
                if i == j: continue

                if self.matrix[i][j].isactive(): 
                    nodes[i].append(j)

                    #workspace
                    dy = location[i][1] - location[j][1]
                    dx = location[i][0] - location[j][0]

                    slope = dy / dx

                    angle = atan(slope)
                    x = cos(angle)*9
                    y = sin(angle)*9

                    #check locations

                    if (dx <0 and dy < 0) or (dy >0 and dx < 0):
                        x*=-1
                        y*=-1


                    self.graph_canva.create_line(location[i][0]+7, location[i][1]+7, location[j][0]+7+x,location[j][1]+7+y, arrow=LAST, fill='white', )

        for i  in range(self.dimension):
            x,y = location[i]
            self.graph_canva.create_oval(x,y, x+15, y+15, fill='white', outline='black')
            self.graph_canva.create_text(x+7, y+7, text=f'{i+1}', fill='black')

        components = get_strongly_connectec_components(nodes)

        for group in components:
            q =[group[0]]
            v = [False] * self.dimension
            v[group[0]]=True
            while len(q):
                temp  = q.pop(0)
                for e in nodes[temp]:
                    if e==temp:continue
                    if e in group:
                        nodes[i].append(j)

                        #workspace
                        dy = location[temp][1] - location[e][1]
                        dx = location[temp][0] - location[e][0]

                        slope = dy / dx

                        angle = atan(slope)
                        x = cos(angle)*9
                        y = sin(angle)*9

                        #check locations

                        if (dx <0 and dy < 0) or (dy >0 and dx < 0):
                            x*=-1
                            y*=-1
                        self.components_canva.create_line(location[temp][0]+7, location[temp][1]+7, location[e][0]+7+x, location[e][1]+7+y, arrow=LAST, fill='white')
                        if v[e]==0: 
                            q.append(e)
                            v[e]=1

        for i  in range(self.dimension):
            x,y = location[i]
            self.components_canva.create_oval(x,y, x+15, y+15, fill='white', outline='black')
            self.components_canva.create_text(x+7, y+7, text=f'{i+1}', fill='black')



        self.label_ans.config(text=f'{len(components)}')
    def ShowProcess(self):
        n = self.dimension
        ma = [[0]*n for i in range(n)]
        for i in range(n):
            for j in range(n):
                if self.matrix[i][j].isactive(): ma[i][j]=1
                
        Process(ma)
        


class Process(Base):
    def __init__(self, matrix):
        super().__init__()
        self.window.geometry("600x700")
        self.window.title('Process')
        self.window.config(bg='#333333')
        

        self.main_frame = Frame(self.window)
        self.main_frame.config(bg = '#333333')
        self.main_frame.pack(fill = BOTH, expand =1)
        

        self.canva= Canvas(self.main_frame)
        self.canva.pack(side = LEFT, fill = BOTH, expand =1)

        self.scrollbar = Scrollbar(self.main_frame, orient=VERTICAL, command= self.canva.yview)
        self.scrollbar.pack(side = RIGHT, fill= Y)
        self.canva.config(bg = '#333333')
        self.canva.configure(yscrollcommand=self.scrollbar.set)
        self.canva.bind('<Configure>', lambda e: self.canva.configure(scrollregion = self.canva.bbox('all')))
        
        self.frame = Frame(self.canva)

        self.frame.config(bg = '#333333')
        

        self.canva.create_window((0,0), window = self.frame, anchor = 'nw')
        
        Frame(self.frame, bg = '#333333', width = 600, height = 40).pack()

        Label(self.frame, text="Primer paso: Se muestra la matriz de caminos:\n Agregar (si fuese necesario) el valor 1 en la diagonal de la matriz y contar la \ncantidad de 1’s en cada fila de la matriz para construir la matriz de caminos.", bg = '#333333', foreground = 'white').pack()
        Label(self.frame, text='', bg = '#333333', height = 1).pack()


        path_matrix = get_Matrix_paths(matrix)
        self.print_matrix(path_matrix, Frame(self.frame))

        Label(self.frame, text='', bg = '#333333', height = 1).pack()

        Label(self.frame, text="Segundo paso: Se ordenar por filas:\nOrdenar las filas según el número de 1’s (de mayor a menor). Si hubiesen dos filas\n que tienen la misma cantidad de 1’s, entonces se debe colocar \nprimero aquella que tiene el 1 más cercano a la primera columna.", bg = '#333333', foreground = 'white').pack()
        Label(self.frame, text='', bg = '#333333', height = 1).pack()


        yaxis,matrix_row_ordered = get_sort_rows(path_matrix)
        self.print_matrix(matrix_row_ordered, Frame(self.frame), yaxis = yaxis)
        Label(self.frame, text='', bg = '#333333', height = 1).pack()

        Label(self.frame, text="Tercer paso: Se ordenar por columnas:\nOrdenar las columnas de acuerdo al orden de las filas.", bg = '#333333', foreground = 'white').pack()
        Label(self.frame, text='', bg = '#333333', height = 1).pack()

        yaxis,ordered_matrix = get_sort_columns(matrix_row_ordered, yaxis)
        self.print_matrix(ordered_matrix, Frame(self.frame), yaxis = yaxis, xaxis=yaxis)

        Label(self.frame, text='', bg = '#333333', height = 1).pack()

        Label(self.frame, text="Cuarto paso: Se encontrar componentes conexas:\nLas componentes conexas serán aquellas que se formen con los\n bloques cuadrados diagonales formados por 1’s. ", bg = '#333333', foreground = 'white').pack()
        Label(self.frame, text='', bg = '#333333', height = 1).pack()

        components = get_Matrix_components(yaxis, ordered_matrix)

        self.Draw_components(Canvas(self.frame), ordered_matrix, components, yaxis)
        Label(self.frame, text='Los componentes son:', bg='#333333', foreground= 'white').pack()


        for comp in components:
            text =''
            for val in comp:
                text+= f'{val+1} '
            Label(self.frame, text= text, bg='#333333', foreground= 'white').pack()

        Label(self.frame, text='', bg='#333333', foreground= 'white', height = 3).pack()



  




        self.window.mainloop()


    def print_matrix(self, matrix, frame, yaxis=[], xaxis=[]):
        n = len(matrix)
        frame.config(bg = '#333333')
        frame.pack(expand=1)
        if len(yaxis)==0:
            yaxis = list(range(n))
        if len(xaxis)==0:
            xaxis = list(range(n))
        
        for i in range(n):
            for j in range(n):
                Label(frame, text = f'{matrix[i][j]}   ', bg = '#333333', foreground = 'white').grid( row = i+1, column= j+1 )
        for i in range(n):
            Label(frame, text = f'{yaxis[i]+1}   ', bg = '#333333', foreground = 'white').grid(row=i+1, column = 0)
            Label(frame, text = f'{xaxis[i]+1}   ', bg = '#333333', foreground = 'white').grid(row = 0, column = i+1)
        return
    
    def Draw_components(self, canva, matrix, components, yaxis):
        n = len(matrix)
        canva.config(width=(n+1) * 30, height = (n+1)*30, bg='#333333', highlightthickness=1, highlightbackground='#333333')
        for i in range(n):
            for j in range(n):
                canva.create_text((i+1) * 30 +3, (j+1)*30 +3, text = f'{matrix[i][j]}', fill = 'white')

        for i in range(n):
            canva.create_text(8 , (i+1) *30 + 3, text = f'{yaxis[i]+1}', fill ='white')
            canva.create_text((i+1) *30 + 3, 8,  text = f'{yaxis[i]+1}', fill ='white')
        i =0
        last = 20
        for comp in components:
            yn = xn =last
            x2 = y2 = last + len(comp) * 30
            canva.create_rectangle(xn, yn, x2, y2, outline = 'red')
            last = x2


        canva.pack()












ma = [
        [1, 1, 0, 0, 0],
        [0, 1, 1, 1, 1],
        [0, 0, 1, 0, 1],
        [1, 0, 0, 1, 0],
        [0, 0, 1, 0, 1]
        ]
Main()


