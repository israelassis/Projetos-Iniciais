# importação - "random para sorteio" / "string" para conjuntos de caracteres
import random
import string

def gerar_senha(tamanho=12):
    #"ascii_letters, digits e punctuation" cria o alfabeto da senha
    caracteres = string.ascii_letters + string.digits + string.punctuation
    #"random.choice" escolhe um caractere por posição / " ''.join " concatena tudo em uma unica string
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

# Programa principal

print("=== Gerador de Senhas Seguras ===")
tamanho = int(input("Digite o tamanho da senha que deseja: "))
print("Sua senha gerada é:", gerar_senha(tamanho))
