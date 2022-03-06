"""
Códigos para aprender a utilizar a investpy - Biblioteca conectada a https://br.investing.com/?ref=www

Acesso a instalar a Biblioteca = pip install investpy

Versão mais atual, porém menos estavel =  pip install git+https://github.com/alvarobartt/investpy.git@master

Paises presentes na investepy :
['argentina', 'australia', 'austria', 'bahrain', 'bangladesh', 'belgium', 'bosnia', 'botswana', 'brazil',
'bulgaria', 'canada', 'chile', 'china', 'colombia',
 'costa rica', 'croatia', 'cyprus', 'czech republic', 'denmark', 'dubai', 'ecuador', 'egypt',
  'estonia', 'euro zone', 'finland', 'france', 'germany', 'greece
', 'hong kong', 'hungary', 'iceland', 'india', 'indonesia', 'iraq', 'ireland', 'israel', 'israeli',
'italy', 'ivory coast', 'jamaica', 'japan', 'jordan', 'ka
zakhstan', 'kenya', 'kuwait', 'kuwaiti', 'latvia', 'lebanon', 'lithuania', 'malaysia', 'malta',
'mauritius', 'mexico', 'mongolia', 'montenegro', 'morocco', '
namibia', 'netherlands', 'new zealand', 'nigeria', 'norway', 'oman', 'pakistan', 'palestine',
'peru', 'philippines', 'poland', 'portugal', 'qatar', 'romania'
, 'russia', 'rwanda', 'saudi arabia', 'serbia', 'singapore', 'slovakia', 'slovenia', 'south africa',
'south korea', 'spain', 'sri lanka', 'sweden', 'switzerland', 'taiwan',
'tanzania', 'thailand', 'tunisia', 'turkey', 'uganda', 'ukraine',
'united arab emirates', 'united kingdom', 'united states', 'venezuela', 'vietnam', 'world', 'zambia', 'zimbabwe']
"""

import investpy as ip
import matplotlib.pyplot as plt

# Buscar a cotação atual da ação:

df = ip.get_stock_historical_data(stock= 'BBDC3' , country= 'brazil' , from_date= '01/01/2020', to_date= '10/01/2020')
print(df.head())

# Pesquisa livre da ação dados básicos dela:
search_result= ip.search_quotes(text= 'bradesco', products= [ 'stocks' ], countries= ['brazil'], n_results= 1)
print(search_result )

# Buscardados mais recentes da ação estudada
dados_recentes= search_result.retrieve_recent_data()
print(dados_recentes)

# Buscar dados históricos de algum periodo especifico:
historical_data= search_result.retrieve_historical_data(from_date= '01/01/2019', to_date= '01/01/2020')
print(historical_data.head())

# Descobrir moeada vinculada a ação
default_currency= search_result.retrieve_currency()
print(default_currency)

# Informações técnicas:
technical_indicators= search_result.retrieve_technical_indicators(interval= 'daily')
print(technical_indicators)
