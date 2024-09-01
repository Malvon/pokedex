
from tkinter import *
from tkinter import ttk

# importando pillow
from PIL import Image, ImageTk
from dados import *

################ cores ################
co0  = "#444466" # Preto
co1  = "#feffff" # Branco
co2  = "#6f9fbd" # Azul
co3  = "#38576b" # Valor
co4  = "#403d3d" # Letra
co5  = "#ef5350" # Vermelha

# creando janela
janela = Tk()
janela.title('')
janela.geometry('550x510')
janela.configure(bg=co1)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=272)

style = ttk.Style(janela)
style.theme_use("clam")

# criando frame
frame_pokemon = Frame(janela, width=550, height=290, relief='flat')
frame_pokemon.grid(row=1, column=0)

def trocar_pokemon(i):
    global imagem_pokemon, pok_imagem

    # trocando cor do fundo do frame
    frame_pokemon['bg'] = pokemon[i]['Tipo'][3]

    #tipo de pokemon
    pok_nome['text'] = i
    pok_nome['bg'] = pokemon[i]['Tipo'][3]
    pok_tipo['text'] = pokemon[i]['Tipo'][1]
    pok_tipo['bg'] = pokemon[i]['Tipo'][3]
    pok_id['text'] = pokemon[i]['Tipo'][0]
    pok_id['bg'] = pokemon[i]['Tipo'][3]

    imagem_pokemon = pokemon[i]['Tipo'][2]

    # imagem do pokemon
    imagem_pokemon = Image.open(imagem_pokemon)
    imagem_pokemon = imagem_pokemon.resize((238, 238))
    imagem_pokemon = ImageTk.PhotoImage(imagem_pokemon)

    pok_imagem = Label(frame_pokemon, image=imagem_pokemon, relief='flat', bg=pokemon[i]['Tipo'][3], fg=co1)
    pok_imagem.place(x=60, y=50)
    pok_tipo.lift()

    # pokemon status
    pok_hp['text']= pokemon[i]['Status'][0]
    pok_ataque['text']= pokemon[i]['Status'][1]
    pok_defesa['text']= pokemon[i]['Status'][2]
    pok_velocidade['text']= pokemon[i]['Status'][3]
    pok_total['text']= pokemon[i]['Status'][4]

    # pokemon habilidades
    pok_habilidade1['text'] = pokemon[i]['Habilidades'][0]
    pok_habilidade2['text'] = pokemon[i]['Habilidades'][1]

# nome
pok_nome = Label(frame_pokemon, relief='flat', anchor=CENTER, font=('Fixedsys 20'), fg=co1)
pok_nome.place(x=12, y=15)

# categoria
pok_tipo = Label(frame_pokemon, relief='flat', anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co1)
pok_tipo.place(x=12, y=50)

# categoria
pok_id = Label(frame_pokemon, relief='flat', anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co1)
pok_id.place(x=12, y=75)

# status
pok_status = Label(janela, text='Status', relief='flat', anchor=CENTER, font=('Verdana 20'), bg=co1, fg=co0)
pok_status.place(x=15, y=310)

# hp
pok_hp = Label(janela, relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_hp.place(x=15, y=360)

# atk
pok_ataque = Label(janela, relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_ataque.place(x=15, y=385)

# def
pok_defesa = Label(janela, relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_defesa.place(x=15, y=410)

# velocidade
pok_velocidade = Label(janela, relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_velocidade.place(x=15, y=435)

# total
pok_total = Label(janela, relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_total.place(x=15, y=460)

# habilidades
pok_habilidades = Label(janela, text='Habilidades', relief='flat', anchor=CENTER, font=('Verdana 20'), bg=co1, fg=co4)
pok_habilidades.place(x=195, y=310)

# habilidade1
pok_habilidade1 = Label(janela, relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_habilidade1.place(x=195, y=385)

# habilidade2
pok_habilidade2 = Label(janela, relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_habilidade2.place(x=195, y=360)

# CRIANDO BOTOES PARA POKEMON
# imagem do pokemon 1

imagem_pokemon_1 = Image.open('images/cabeca-pikachu.png')
imagem_pokemon_1 = imagem_pokemon_1.resize((40, 40))
imagem_pokemon_1 = ImageTk.PhotoImage(imagem_pokemon_1)

b_pok_1 = Button(janela, command=lambda:trocar_pokemon('Pikachu'), image=imagem_pokemon_1, text='Pikachu', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=co1, fg=co0)
b_pok_1.place(x=375, y=10)

# imagem do pokemon 2

imagem_pokemon_2 = Image.open('images/cabeca-bulbasaur.png')
imagem_pokemon_2 = imagem_pokemon_2.resize((40, 40))
imagem_pokemon_2 = ImageTk.PhotoImage(imagem_pokemon_2)

b_pok_2 = Button(janela, command=lambda:trocar_pokemon('Bulbasaur'), image=imagem_pokemon_2, text='Bulbasaur', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=co1, fg=co0)
b_pok_2.place(x=375, y=65)

# imagem do pokemon 3

imagem_pokemon_3 = Image.open('images/cabeca-charmander.png')
imagem_pokemon_3 = imagem_pokemon_3.resize((40, 40))
imagem_pokemon_3 = ImageTk.PhotoImage(imagem_pokemon_3)

b_pok_3 = Button(janela, command=lambda:trocar_pokemon('Charmander'), image=imagem_pokemon_3, text='Charmander', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=co1, fg=co0)
b_pok_3.place(x=375, y=120)

# imagem do pokemon 4 

imagem_pokemon_4 = Image.open('images/cabeca-gyarados.png')
imagem_pokemon_4 = imagem_pokemon_4.resize((40, 40))
imagem_pokemon_4 = ImageTk.PhotoImage(imagem_pokemon_4)

b_pok_4 = Button(janela, command=lambda:trocar_pokemon('Gyarados'), image=imagem_pokemon_4, text='Gyarados', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=co1, fg=co0)
b_pok_4.place(x=375, y=175)

# imagem do pokemon 5

imagem_pokemon_5 = Image.open('images/cabeca-gengar.png')
imagem_pokemon_5 = imagem_pokemon_5.resize((40, 40))
imagem_pokemon_5 = ImageTk.PhotoImage(imagem_pokemon_5)

b_pok_5 = Button(janela, command=lambda:trocar_pokemon('Gengar'), image=imagem_pokemon_5, text='Gengar', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=co1, fg=co0)
b_pok_5.place(x=375, y=230)

# imagem do pokemon 6

imagem_pokemon_6 = Image.open('images/cabeca-dragonite.png')
imagem_pokemon_6 = imagem_pokemon_6.resize((40, 40))
imagem_pokemon_6 = ImageTk.PhotoImage(imagem_pokemon_6)

b_pok_6 = Button(janela, command=lambda:trocar_pokemon('Dragonite'), image=imagem_pokemon_6, text='Dragonite', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=co1, fg=co0)
b_pok_6.place(x=375, y=285)

trocar_pokemon('Pikachu')

janela.mainloop()