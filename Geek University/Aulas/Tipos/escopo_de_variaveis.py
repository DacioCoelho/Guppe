""""
Escopo variáveis

Escopo -> Limitação de algo, de uma variável

Dosi casos de escopo:

1 - Escopo das variáveis globais;
        São reconhecidas, ou seja, seu escopo compreende, todo o programa.

2 - Escopo das variáveis locais;
        São reconehcidas apenas no bloco onde foram declaradas, ou seja,
        seu escopo está limitado ao bloco onde foi declarado

Para declarar variáveis em Python fazemos:
nome_da_variavel = valor_da_variavel

Python é uma linguagem de tipagem dinâmica. Isso significa que ao declararmos uma variável, nós
não colocamos o tipo de dado dela.
Este tipo é inferido ao atribuirmos o valor à mesma.

Exemplo em C:
int numero = 42;

Exemplo em Java:
int numero = 42;
"""

numero = 42 # Exemplo de variavel global - a partir do momento que declarei,
# ela pode ser usada em qualquer aprte do programa
print(numero)
print(type(numero))

numero = '42'
print(numero)
print(type(numero))

numero = 2
# novo = 0

if numero > 10:
    novo = numero + 10 #A variavel novo está sendo criada apenas dentro desse bloco, não faz parte do programa
                        # de forma global, só local.
    print(novo)

print(novo)