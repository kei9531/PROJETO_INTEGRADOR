from pickle import FRAME
from tkinter import*
from tkinter.tix import Tree
from tkcalendar import Calendar,DateEntry
from tkinter import Tk, StringVar, ttk
import tkinter.font as tkFont
from tkinter import messagebox
from tkinter import filedialog as fd 
from turtle import bgcolor, left, update, width
from PIL import Image,ImageTk

#cores

co0 = "#2e2d2b" #Preto
co1 = "#feffff" #Branca
co2 = "#4fa882" #Verde
co3 = "#38576b" #Valor
co4 = "#403d3d" #letra
co5 = "#e06636" #Laranja
co6 = "#038cfc" #Azul
co7 = "#3fbfb9" #Verde 1
co8 = "#263738" #Verde +
co9 = "#e9edf5" #Cinza

#criando janela em branco
janela = Tk ()
janela.title("")
janela.geometry('900x600')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

#janela resizable(widht=false,height=false)

style = ttk.Style(janela)
style.theme_use("clam")

#criacao dos frames
frameCima = Frame(janela, width=900, height=50, bg=co1, relief="flat")
frameCima.grid(row=0, column=0)

frameMeio = Frame(janela, width=1050, height=303, bg=co1, pady=20, relief='raised')
frameMeio.grid(row=1, column=0, pady=1,padx=0, sticky=NSEW)

frameBaixo = Frame(janela, width=1050, height=300,bg=co1, pady=20, relief='sunken')
frameBaixo.grid(row=2, column=0, pady=0,padx=1, sticky=NSEW)

#inserir imagem-icone
app_img = Image.open ('icone.png')   
app_img = app_img.resize((45,45))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label (frameCima, image=app_img, text=" Controle de Estoque Doméstico", width=900, compound=LEFT, relief=RAISED, anchor=NW, font=('Verdana 20 bold'), bg=co1, fg=co0)
app_logo.place(x=0, y=0)     

#criando loop de entrada
l_nome = Label(frameMeio, text = "Nome",  height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4 )
l_nome.place(x=10, y=10)
e_nome = Entry (frameMeio, width=30, justify='left',relief='solid')
e_nome.place(x=130, y=11)

l_local = Label(frameMeio, text ="Sala/Área",  height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4 )
l_local.place(x=10, y=40)
e_local = Entry (frameMeio, width=30, justify='left', relief='solid')
e_local.place(x=130,y=41)

l_descricao = Label(frameMeio, text ="Descrição",   height=1,anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4 )
l_descricao.place(x=10, y=70)
e_descricao = Entry (frameMeio, width=30, justify='left', relief='solid')
e_descricao.place(x=130,y=71)

l_modelo = Label(frameMeio, text ="Marca/modelo",   height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1,fg=co4 )
l_modelo.place(x=10, y=130)
e_modelo = Entry (frameMeio, width=30, justify='left', relief="solid")
e_modelo.place(x=130,y=131)

l_cal = Label(frameMeio, text ="Data da Compra",  height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4 )
l_cal.place(x=10, y=160)
e_cal = DateEntry (frameMeio, width=12, background='darkblue', foreground='white', borderwidth=2, year = 2020)
e_cal.place(x=130, y=161)


l_valor = Label(frameMeio, text ="Valor da Compra",   height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4 )
l_valor.place(x=10, y=160)
e_valor = Entry (frameMeio, width=30, justify='left', relief="solid")
e_valor.place(x=130, y=161)

l_serial = Label(frameMeio,  text ="Número da Série",   height=1,  anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4 )
l_serial.place(x=10, y=190)
e_serial = Entry (frameMeio, width=30, justify='left', relief="solid")
e_serial.place(x=130,y=191)

#criacao dos botoes

l_carregar = Label(frameMeio, text ="Imagem do Item",   height=1,  anchor=NW, font=('Ivy 10 bold'),   bg=co1, fg=co4 )
l_carregar.place(x=10,y=220)
botao_carregar = Button(frameMeio, compound=CENTER, anchor=CENTER, text="CARREGAR".upper(), width=3, overrelief=RIDGE, font=('ivy 8'), bg=co1, fg=co2)
botao_carregar.place(x=130,y=221)

#botao inserir
img_add = Image.open('add.png')
Img_add = img_add.resize((20,20))
img_add = ImageTk.PhotoImage(img_add)
botao_inserir = Button(frameMeio, image=img_add, compound=LEFT, anchor=NW, text = "Inserir".upper(), width=95, overrelief=RIDGE, font=('ivy 8'),bg=co1, fg=co0)
botao_inserir.place(x=330, y=10)

#botao atualizar
img_update = Image.open('update.png')
img_update = img_update.resize((20,20))
img_update = ImageTk.PhotoImage(img_update)
botao_atualizar = Button(frameMeio, image=img_update, compound=LEFT, anchor=NW, text = "Atualizar".upper(), width=95, overrelief=RIDGE, font=('ivy 8'),bg=co1, fg=co0)
botao_atualizar.place(x=330, y=50)

#botao_deletar
img_delete = Image.open('delete.png')
img_delete= img_delete.resize((20,20))
img_delete = ImageTk.PhotoImage(img_delete)
botao_delete = Button(frameMeio, image=img_delete, compound=LEFT, anchor=NW, text = "Deletar".upper(), width=95, overrelief=RIDGE, font=('ivy 8'), bg=co1, fg=co0)
botao_delete.place(x=330, y=90)

#botao ver item
img_item = Image.open('item.png')
img_item = img_item.resize((20,20))
img_item = ImageTk.PhotoImage(img_item)
botao_item = Button(frameMeio, image=img_item, compound=LEFT, anchor=NW, text = "Ver Item".upper(), width=95,overrelief=RIDGE, font=('ivy 8'), bg=co1, fg=co0)
botao_item.place(x=330, y=221)

#label quantidade e valores
l_total = Label(frameMeio, width=14, height=2, anchor=CENTER, font=('Ivy 25 bold'), bg=co7, fg=co1, relief=FLAT)
l_total.place(x=450,y=17)
l_valor_total = Label (frameMeio, text="Valor Total de Todos Os Itens", anchor=NW, font=('Ivy 10 bold'), bg=co7, fg=co1)
l_valor.place(x=450, y=12)

l_qtd = Label(frameMeio, width=14, height=2 ,anchor=CENTER, font=('Ivy 25 bold'), bg=co7, fg=co1, relief=FLAT)
l_qtd.place(x=450, y=17)
l_qtd_itens = Label (frameMeio, text="Quantidade Total de Itens", anchor=NW, font=('Ivy 10 bold'), bg=co7, fg=co1)
l_qtd_itens.place(x=460, y=92)

janela.mainloop()

def mostrar():
       tabela_head= ['Item','Nome', 'Sala/Área', 'Descrição', 'Marca/Modelo', 'Data da Compra','Valor da Compra', 'Número de Série']
lista_itens = []

global tree

tree = ttk.Treeview(frameBaixo, selectmode="extended",columns=tabela_head,show="headings")