import investpy as ip
import matplotlib.pyplot as plt

bitcoin = ip.get_crypto_historical_data(crypto = 'bitcoin', from_date= '01/01/2021', to_date= '18/11/2021')

bitcoin.head()

