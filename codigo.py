#1- abrir o navegador

#pyautogui = serve para permitir com que você controle o mouse e o seu teclado para fazer as automações no seu computador
import pyautogui
import time


pyautogui.PAUSE= 0.5

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

#2- acessar o link

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.write(link)
pyautogui.press("enter")    

time.sleep(2)

#3- inserir o login
pyautogui.click(pyautogui.position(x=553, y=309))
pyautogui.write("tiago@gmail.com")
pyautogui.press("tab")
pyautogui.write("suasenha")

pyautogui.press("enter")

#4- inserir os produtos
import pandas
produtos = pandas.read_csv("produtos.csv")


for linhas in produtos.index:
    
    pyautogui.click(pyautogui.position(x=570, y=232))

    #codigo
    pyautogui.write(produtos.loc[linhas, "codigo"])
    pyautogui.press("tab")

    #marca
    pyautogui.write(produtos.loc[linhas, "marca"])
    pyautogui.press("tab")

    #tipo
    pyautogui.write(produtos.loc[linhas, "tipo"])
    pyautogui.press("tab")

    #categoria
    pyautogui.write(str(produtos.loc[linhas, "categoria"]))
    pyautogui.press("tab")

    #preço
    pyautogui.write(str(produtos.loc[linhas, "preco_unitario"]))
    pyautogui.press("tab")

    #custo
    pyautogui.write(str(produtos.loc[linhas, "custo"]))
    pyautogui.press("tab")

    #obs
    obs = produtos.loc[linhas, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)
        
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)


#5- repetir a inserção ate o fim do arquivo