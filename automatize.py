# terminal: pip install pyautogui
# import pyautogui
# python.exe -m pip install --upgrade pip  --  tem q executar como adm no prompt de comando

# pip install pyautogui --user
# pip show pyautogui
# pip install pandas openpyxl numpy

# pyautogui.click -> click w/mouse
# pyautogui.write -> write a txt
# pyautogui.press -> press 1 tecl
# pyautogui.hotkey -> combine tecls
# pyautogui.scroll -> rolar
import pyautogui
import time
pyautogui.PAUSE = 0.8

pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(7)
#Fazer login
pyautogui.click(x=339, y=440)
pyautogui.hotkey("ctrl", "a")
pyautogui.write("josemario.dev@gmail.com")
#Senha
pyautogui.press("tab")
pyautogui.write("1234")
#Logar
# pyautogui.press("tab")
# pyautogui.press("tab")
pyautogui.click(x=473, y=603)

time.sleep(4)

import pandas
# pandas.read_sql_query
# pandas.read_html
table = pandas.read_csv("produtos.csv")
# print(tabela)
for rows in table.index:

    pyautogui.click(x=239, y=328)
    #str(table.lot[rows, "codigo"])
    #pyautogui.write("code")
    #pyautogui.write(str(table.lot[rows, "codigo"]))
    code = str(table.loc[rows, "codigo"])
    pyautogui.write(code)
    #pyautogui.write("index")
    pyautogui.press("tab")
    style = str(table.loc[rows, "marca"])
    pyautogui.write(style)
    #pyautogui.write("type")
    pyautogui.press("tab")
    type = str(table.loc[rows, "tipo"])
    pyautogui.write(type)
    #pyautogui.write("class")
    pyautogui.press("tab")
    category = str(table.loc[rows, "categoria"])
    pyautogui.write(category)
    #pyautogui.write("value")
    pyautogui.press("tab")
    values = str(table.loc[rows, "preco_unitario"])
    pyautogui.write(values)
    #pyautogui.write("cost")
    pyautogui.press("tab")
    costs = str(table.loc[rows, "custo"])
    pyautogui.write(costs)
    #pyautogui.write("select")
    pyautogui.press("tab")
    ps = str(table.loc[rows, "obs"])
    if ps != "nan":
        pyautogui.write(ps)
    #botão Enviar
    # pyautogui.click(x=330, y=986)
    pyautogui.press("tab")
    pyautogui.press("enter")

    #botão Limpar/Reset
    # pyautogui.click(x=499, y=990)
    # pyautogui.press("tab")
    # pyautogui.press("enter")
    pyautogui.scroll(1000)