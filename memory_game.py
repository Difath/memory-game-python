from tkinter import *
from PIL import ImageTk, Image
import random
from threading import Timer
import shelve


root = Tk()
root.title("Jogo da memória")
root.config(bg="#2C3E50", padx=20, pady=20)



#DEFINE A CLASSE DAS CARTAS DO BARALHO - numero da imagem; a imagem correspondente;
#; o estado(escondido/visivel); e se o par esta feito ou nao -
class Carta:
    def __init__(self,numero, Tkimage, estado="escondido", esta_feito = False):
        self.Tkimage = Tkimage
        self.numero = numero
        self.estado = estado
        self.esta_feito = esta_feito

# CRIA O FICHEIRO DA IMAGEM DA CARTA ESCONDIDA - igual em todas - 
imagem_escondida = (Image.open(f"numeros/semFace.png").resize((75, 110)))
tk_imagem_escondida = ImageTk.PhotoImage(imagem_escondida)
            

# CRIA VARIÁVEIS NECESSÁRIAS PARA O JOGO
primeira_carta_do_par = []
segunda_carta_do_par = []
n_par_feitos = 0
jogo_a_funcionar = True
n_jogadas = 0
dificuldade = 0
total_colunas = 0 
pares = 0
baralho = []


#FUNCAO QUE CENTRALIZA AS JANELAS
def CentrarWindow(largura=None, altura=None):
    root.update_idletasks()
    if largura is None:
        largura = root.winfo_reqwidth()
    if altura is None:
        altura = root.winfo_reqheight()

    largura_screen = root.winfo_screenwidth()
    altura_screen = root.winfo_screenheight()

    x = int((largura_screen/2) - (largura/2))
    y = int((altura_screen/2) - (altura/2))
    
    root.geometry(f"{largura}x{altura}+{x}+{y}")


# CRIA O BARALHO - lista de cartas -
def Baralho(): 
    global baralho
    cartas=[x for x in range(1,41)]
    random.shuffle(cartas)
    cartas = (2*[cartas[x] for x in range(pares)])
    random.shuffle(cartas)
    for x in (cartas):
        tk_imagem_visivel = ImageTk.PhotoImage(Image.open(f"numeros/{x}.png").resize((75, 110)))
        carta=Carta(x, tk_imagem_visivel)
        baralho.append(carta)
    DesenharGUI(root, baralho)


#FUNCAO PARA GUARDAR O HIGHSCORE
def guardar_highscore():
    with shelve.open("highscore/highscore") as Ficheiro:
        Ficheiro[f"highscore{dificuldade}"] = n_jogadas


#FUNCAO PARA LER O HIGHSCORE 
def ler_highscore():
    try:
        with shelve.open("highscore/highscore") as Ficheiro:
            return Ficheiro.get(f"highscore{dificuldade}", None)
    except Exception:
        return None


# DEFINE A FUNCAO QUE RESETA O PAR - usado quando o user erra um par de cartas -
def Resetar_Par():
    global baralho, primeira_carta_do_par, segunda_carta_do_par, jogo_a_funcionar
    baralho[primeira_carta_do_par[0]].estado = "escondido"
    baralho[segunda_carta_do_par[0]].estado = "escondido"
    primeira_carta_do_par[2].config(image=tk_imagem_escondida)
    segunda_carta_do_par[2].config(image=tk_imagem_escondida)
    primeira_carta_do_par = []
    segunda_carta_do_par = []
    jogo_a_funcionar = True




# DEFINE A FUNCAO QUE MUDA CARTA - usada quando o user clica numa carta 
#de modo a mudar o seu estado (visivel/escondido) - 
def Mudar_Carta(evento):
    indexCarta = int(evento.widget.cget("text"))
    if jogo_a_funcionar:
        if baralho[indexCarta].estado == "visivel" and baralho[indexCarta].esta_feito == False:
            baralho[indexCarta].estado = "escondido"
        else:
            baralho[indexCarta].estado = "visivel" 
        if baralho[indexCarta].estado == "escondido": 
            evento.widget.config(image=tk_imagem_escondida)
        else:
            evento.widget.config(image=baralho[indexCarta].Tkimage)
        return baralho[indexCarta]  
    else:
        pass

#DEFINE A FUNCAO PRINCIPAL DO JOGO
def Jogo(evento):
    global primeira_carta_do_par, segunda_carta_do_par, n_par_feitos, jogo_a_funcionar, n_jogadas
    indexCarta = int(evento.widget.cget("text"))
    if baralho[indexCarta].estado == "visivel" and baralho[indexCarta].esta_feito == False and primeira_carta_do_par == [] and jogo_a_funcionar:
        primeira_carta_do_par = [indexCarta, baralho[indexCarta].numero, evento.widget]
        baralho[indexCarta].esta_feito = True
    elif baralho[indexCarta].estado == "visivel" and baralho[indexCarta].esta_feito == False and primeira_carta_do_par[0]!= indexCarta and jogo_a_funcionar:
        segunda_carta_do_par = [indexCarta, baralho[indexCarta].numero, evento.widget]
        if primeira_carta_do_par[1] == segunda_carta_do_par[1]:
            baralho[primeira_carta_do_par[0]].esta_feito = True
            baralho[segunda_carta_do_par[0]].esta_feito = True 
            n_par_feitos += 1
            primeira_carta_do_par = []
            segunda_carta_do_par = []
        else:
            baralho[primeira_carta_do_par[0]].esta_feito = False
            #Delay de 1 segundo para o user conseguir ver o par que errou 
            root.after(1000, Resetar_Par)
            jogo_a_funcionar = False
        n_jogadas += 1
    Verificar_Vitoria_e_jogadas(n_par_feitos)


#DEFINE A FUNCAO PARA VERIFICAR SE O USER JA GANHOU E PARA ATUALIZAR O NUMERO DE JOGADAS
# - usada sempre que o user clica numa carta -
def Verificar_Vitoria_e_jogadas(n_par_feitos):
    global n_jogadas_label
    if dificuldade == 1:
        n_jogadas_label = Label(root, text=f"Nº de Jogadas: {n_jogadas}", font=("Helvetica", 15, "bold"), padx=10, bg="#2C3E50", fg="#ECF0F1" )
        n_jogadas_label.grid(row=5, column= 0, columnspan=2)
    elif dificuldade == 2:
        n_jogadas_label = Label(root, text=f"Nº de Jogadas: {n_jogadas}", font=("Helvetica", 20, "bold"), padx=20, bg="#2C3E50", fg="#ECF0F1" )
        n_jogadas_label.grid(row=5, column= 0, columnspan=3)
    elif dificuldade == 3:
        n_jogadas_label = Label(root, text=f"Nº de Jogadas: {n_jogadas}", font=("Helvetica", 30, "bold"), padx=30, bg="#2C3E50", fg="#ECF0F1" )
        n_jogadas_label.grid(row=5, column= 0, columnspan=4)

    if n_par_feitos == len(baralho)/2:
        for widget in root.winfo_children():
            widget.destroy()
        CentrarWindow()
        vitoria = Label(root, text =" Ganhaste", font=("Helvetica", 70, "bold"), bg="#2C3E50", fg="#ECF0F1")
        vitoria.grid(row=0,column=0, columnspan=8)
        jogadas= Label(root, text=f"  Tu ganhaste com\n {n_jogadas} \njogadas!!", font=("Helvetica", 40, "bold"), pady=30, bg="#2C3E50", fg="#ECF0F1")
        jogadas.grid(row=1, column=0, columnspan=8)
        Butao_sair = Button(root, text="Sair", font= ("Helvetica", 30, "bold"), background="#E74C3C", fg="white",  padx= 60,command=root.destroy)
        Butao_sair.grid(row=2, column=0, columnspan=8)
        highscore = ler_highscore()
        if highscore is None or n_jogadas < highscore:
            guardar_highscore()

#DEFINE A FUNCAO USADA PARA MUDAR OS ATRIBUTOS DO JOGO 
# - chamada depois do user escolher a dificuldade -
def Dificuldade(evento):
    global dificuldade, total_colunas, pares
    if evento.widget.cget("text") ==  "Facil":
        dificuldade = 1
        total_colunas = 6
        pares = 12
    elif evento.widget.cget("text") == "Medio":
        dificuldade = 2
        total_colunas = 8
        pares = 16
    else:
        dificuldade = 3
        total_colunas = 10
        pares = 20
    for widget in root.winfo_children():
            widget.destroy()
    Baralho()

# DESENHA O MENU PRINCIPAL PARA O USER ESCOLHER A DIFICULDADE.
def DesenharMenu(root):
    Inicio = Label (root, text=f"JOGO DA MEMÓRIA", font=("Helvetica", 60, "bold"), pady= 40, bg="#2C3E50", fg="#ECF0F1", padx=30) 
    Inicio.grid(row=0, column=0, columnspan= 3)
    SelecionaDificuldade = Label(root, text=f"Seleciona a Dificuldade", font=("Helvetica", 40, "bold"), bg="#2C3E50", fg="#ECF0F1")
    SelecionaDificuldade.grid(row=1, column=0, columnspan= 3)
    ButaoFacil = Button(root, text=f"Facil", font=("Helvetica", 20, "bold"), bg="#2ECC71", fg="black", padx= 9)
    ButaoFacil.grid(row=2, column=0, columnspan= 3)
    ButaoFacil.bind("<Button-1>", Dificuldade)
    DificuldadeFacil = Label (root, text=f" 6 x 4 ", font=("Helvetica", 20, "bold"), pady=20, bg="#2C3E50", fg="#ECF0F1")
    DificuldadeFacil.grid(row=2, column=1, columnspan=3)
    ButaoMedio = Button(root, text=f"Medio", font=("Helvetica", 20, "bold"), bg="#F1C40F", fg="black")
    ButaoMedio.grid(row=3, column=0, columnspan= 3)
    ButaoMedio.bind("<Button-1>", Dificuldade)
    DificuldadeMedio = Label (root, text=f" 8 x 4 ", font=("Helvetica", 20, "bold"), pady=20, bg="#2C3E50", fg="#ECF0F1")
    DificuldadeMedio.grid(row=3, column=1, columnspan=3)
    ButaoDificil = Button(root, text=f"Dificil", font=("Helvetica", 20, "bold"), bg="#E74C3C", fg="black")
    ButaoDificil.grid(row=4, column=0, columnspan= 3)
    ButaoDificil.bind("<Button-1>", Dificuldade)
    DificuldadeDificil = Label (root, text=f" 10 x 4 ", font=("Helvetica", 20, "bold"), pady=20, bg="#2C3E50", fg="#ECF0F1")
    DificuldadeDificil.grid(row=4, column=1, columnspan=3)
    CentrarWindow()

# CRIA O JOGO VISUALMENTE 
def DesenharGUI(root, baralho):
    root.config(bg="#2C3E50")
    pontuacao = ler_highscore()
    highscore = "N/A" if pontuacao is None or pontuacao > 10000 else pontuacao
    if dificuldade == 1:
        highscore_label = Label(root, text=f"Highscore: {highscore}", font=("Helvetica", 15, "bold"), padx=20, bg="#2C3E50", fg="#ECF0F1" )
        highscore_label.grid(row=5, column=4, columnspan=2)
        n_jogadas_label = Label(root, text=f"Nº de Jogadas: {n_jogadas}", font=("Helvetica", 15, "bold"), padx=10, bg="#2C3E50", fg="#ECF0F1" )
        n_jogadas_label.grid(row=5, column= 0, columnspan=2)
        
    elif dificuldade == 2:
        highscore_label = Label(root, text=f"Highscore: {highscore}", font=("Helvetica", 20, "bold"), padx=20, bg="#2C3E50", fg="#ECF0F1" )
        highscore_label.grid(row=5, column=5, columnspan=3)
        n_jogadas_label = Label(root, text=f"Nº de Jogadas:{n_jogadas}", font=("Helvetica", 20, "bold"), padx=20, bg="#2C3E50", fg="#ECF0F1" )
        n_jogadas_label.grid(row=5, column= 0, columnspan=3)
        
    elif dificuldade == 3:
        highscore_label = Label(root, text=f"Highscore: {highscore}", font=("Helvetica", 30, "bold"), padx=30, bg="#2C3E50", fg="#ECF0F1")
        n_jogadas_label = Label(root, text=f"Nº de Jogadas:{n_jogadas}", font=("Helvetica", 30, "bold"), padx=30, bg="#2C3E50", fg="#ECF0F1" )
        highscore_label.grid(row=5, column=6, columnspan=4)
        n_jogadas_label.grid(row=5, column= 0, columnspan=4)
        
    Titulo = Label(root, text="🧠 Jogo Da Memória 🧠", font=("Helvetica", 40, "bold"), bg="#2C3E50", fg="#ECF0F1")
    Titulo.grid(row=0,column=0, columnspan=total_colunas)     
    Butao_sair = Button(root, text="Sair", font= ("Helvetica", 30, "bold"), background="#E74C3C", fg="white",  padx= 60, pady= -10 ,command=root.destroy)
    Butao_sair.grid(row=5, column=0, columnspan=total_colunas)
    

    #Desenha o baralho
    contador = 0
    for fila in range(4):
        for coluna in range(total_colunas):
            if baralho[contador].estado == "escondido":
                imagem = tk_imagem_escondida
            else:
                imagem = baralho[contador].Tkimage
            label = Label(root, text=str(contador), image=imagem, bg="#2C3E50")
            label.bind("<Button-1>", Mudar_Carta, add="+")
            label.bind("<Button-1>", Jogo, add="+")
            label.grid(row=fila+1, column=coluna, padx= 20, pady=8)
            contador += 1 
    CentrarWindow()
def main():     
    DesenharMenu(root)
    root.mainloop()

if __name__ == "__main__":
    main()    