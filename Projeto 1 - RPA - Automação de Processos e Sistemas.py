#!/usr/bin/env python
# coding: utf-8

# In[56]:


#!pip install pyautogui


# In[57]:


import pyautogui
import time
import pandas as pd
import pyperclip


# In[58]:


#time.sleep(5)
#pyautogui.position()


# In[59]:


pyautogui.PAUSE

pyautogui.hotkey("ctrl", "t")

pyautogui.write("https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema")
pyautogui.press("enter")
time.sleep(2)

pyautogui.click(x=621, y=375)
pyautogui.write("meu_login")
time.sleep(1.5)

pyautogui.click(x=626, y=456)
pyautogui.write("minha_senha")

pyautogui.click(x=658, y=517)
time.sleep(2)

pyautogui.click(x=468, y=372)
time.sleep(1.5)

pyautogui.click(x=1153, y=186)
time.sleep(1.5)

pyautogui.click(x=864, y=597)
time.sleep(2)

#solução para substituir um arquivo já existente no diretório e que tenha o mesmo nome 
pyperclip.copy("Compras")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
time.sleep(1.5)
pyautogui.press("tab")
time.sleep(1.5)
pyautogui.press("enter")
time.sleep(2)


# In[60]:


tabela = pd.read_csv(r"D:\Desktop\Cursos HUB\Intensivão de Python\Aula 1\Compras.csv", sep=";")

#display(tabela)

total_gasto = tabela["ValorFinal"].sum()

quantidade = tabela["Quantidade"].sum()

preco_medio = total_gasto / quantidade

#print(total_gasto)
#print(quantidade)
#print(preco_medio)


# In[61]:


pyautogui.hotkey("ctrl", "t")

pyautogui.write("https://mail.google.com/mail/u/3/?ogbl#inbox")
pyautogui.press("enter")
time.sleep(6)

pyautogui.click(x=55, y=197)
time.sleep(2)

pyautogui.write("eidos.clouds@gmail.com")
time.sleep(2)
pyautogui.press("tab")
pyautogui.press("tab")

pyperclip.copy("Relatório de Vendas")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("tab")

texto = f"""
Prezados,
Segue o Relatório de Vendas.

Total Gasto: R$ {total_gasto:,.2f}
Quantidade de Produtos: {quantidade:,}
Preço Médio: R$ {preco_medio:,.2f}

Qualquer dúvida, estarei à disposição.

Atenciosamente,
Alexandre Assis.

"""
pyperclip.copy(texto)
pyautogui.hotkey("ctrl","v")
time.sleep(3)

pyautogui.hotkey("ctrl", "enter")
time.sleep(2)

pyautogui.click(x=343, y=612)


# In[ ]:




