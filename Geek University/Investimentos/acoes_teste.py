
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


ativos = ['BBDC3.SA', 'CASH3.SA', 'ENBR3.SA', 'HBSA3.SA', 'JBSS3.SA', 'MDIA3.SA', 'VIIA3.SA']

inicio = '2021-08-30'
fim = '2021-11-11'
precos = pd.DataFrame()

 for i in ativos:
...     precos[i] = yf.download(i, start = inicio, end = fim)['Adj Close']

normalizado = precos/precos.iloc[0]
normalizado.plot(figsize = (8,8));

plt.show ()
