repetir = "S"
#O While será responsavel pelo loop do codigo.
while repetir == "S":
    nomeCliente = input("Nome do cliente:  ")
    valorCompra = float(input("Valor da compra: "))
#Se o valor for maior que 100 Será aplicado o desconto de 10%.
    if valorCompra > 100:
        desconto = valorCompra * 0.10
#Se o valor nao for maior o else será responsavel por não aplicar o desconto.
    else:
        desconto = 0
    
    valorFinal = valorCompra - desconto

    print("\nCliente:", nomeCliente)
    print("Desconto: R$", desconto)
    print("Valor final: R$", valorFinal)
#O loop irá continuar a medida que o cliente optar pela escolha (S)
    repetir = input("\nDeseja realizar outro atendimento? (S/N): ").upper()
#Caso o cliente opte por (N) o loop será encerrado.
print("Programa Encerrao!")
