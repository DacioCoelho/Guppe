"""
Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida.

"""

s = 'FULANO'

# FATIAMENTO EM PYTHON
"""
print(s[1])
print(s[1:4]) #Intervalos sempre são abertos
print(s[-1])
print(s[:-1])
"""
while s!= '':
    print(s)
    s = s[:-1]

while s != '':
    print(s[0:])
    s = s[+1:]