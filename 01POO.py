import random

nome = str(input("Nos informe seu nome: "))
print(f"Boas vindas {nome}")

nome_pdt = str(input("Nos informe o produto desejado: "))
cor = str(input("Digite a cor do produto desejado: "))

qntdd_estq = random.randint(0,100)

if qntdd_estq == 0:
    print("O produto desejado está sem estoque. \nEstoque = 0")
    exit()
else:
    print(f"A quantidade de estoque está em {qntdd_estq}")

preco_unit = float(input("Digite o valor unitário. Ex.:(19.99): "))

qntdd_pdt = int(input('Quantos produtos você deseja levar? Digite a seguir: '))

if qntdd_pdt <= qntdd_estq:
    frete = random.randint(9,26)
    print(f"O valor do frete ficou de R${frete}")

    total1 = qntdd_pdt * preco_unit
    total2 = total1 + frete

    print(f"\nO valor total do seu produto ficou: R${total2:.2f}\n")

    print(f"Olá {nome}, suas informações sobre o produto são:\n"
          f"Nome do produto: {nome_pdt}   //   Cor: {cor}.\n"
          f"Quantidade de produtos que irá levar: {qntdd_pdt}.\n"
          f"Valor unitário: R${preco_unit:.2f}\n"
          f"O valor do frete ficou de R${frete}\n"
          f"O valor total ficou em R${total2:.2f}")

    print("\n<====================================ETAPA FINAL====================================>\n")
    print("Digite (SIM) para Confirmar ou (NAO) para Cancelar")

    confirm = str(input("Confirmar Compra: ")).lower()

    if confirm == 'sim':
        print("Compra realizada com sucesso ✅")
    elif confirm == 'nao':
        print("Compra não efetuada ❌")
    else:
        print("\n===============ERRO===============\n\n🔄 Refazer compra 🔄")

else:
    print("\n===============ERRO===============\n")
    print(f"A quantidade de produtos que você quer levar é superior à disponível ({qntdd_estq}).\n🔄 Refaça a compra 🔄")
    exit()
