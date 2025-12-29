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

-----
# 🔐 Gerador de Senhas Seguras (Python)

Um utilitário simples para gerar senhas aleatórias e fortes, ideal para praticar Python e conceitos básicos de segurança.

## ✨ Funcionalidades
- **Tamanho configurável** da senha
- Conjunto de caracteres com **letras**, **números** e **símbolos**
- Saída direta no terminal

## 🚀 Como executar
```bash
python3 gerador_senhas.py

-----
    🧠 Como funciona
Usa string.ascii_letters, string.digits e string.punctuation como conjunto de caracteres

Seleciona caracteres com random.choice e monta a senha com ''.join(...)

⚠️ Observações de segurança
Para uso educacional. Em ambientes que exigem segurança real, considere secrets em vez de random.

🛠 Próximos passos
Validação de entrada (evitar tamanhos inválidos)

Opções de complexidade (ativar/desativar símbolos)

Uso de secrets para aleatoriedade criptográfica

Interface CLI com argparse (ex.: --length 16 --no-symbols)

Salvar em arquivo com timestamp

📚 Aprendizados
Funções e parâmetros padrão

Manipulação de strings e iteráveis

Biblioteca padrão (random, string)

Boas práticas de código e segurança
