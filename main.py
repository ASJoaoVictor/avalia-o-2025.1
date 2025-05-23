def q1():
    """Periodicamente as crianças brasileiras devem tomar vacinas que as protegem de diversas doenças. Escrever um programa para ler o ano em que a criança toma a 1a dose e a 
    periodicidade (intervalo em anos) da vacina e exibir em que outros anos a criança deve tomar as próximas doses desta vacina, sabendo que são 4(quatro) doses ao total."""
    anoVacina = int(input("Digite o ano da primeira dose: "))
    periodo = int(input("Digite a periodicidade da vacina: "))

    for i in range(0, 4):
        anoVacina += periodo
        print(f"{anoVacina}", end=" ")

def q2():
    """Faça um programa que leia uma sequencia de números e indique se eles são primos ou não. Você deve parar ao ler o número -1."""
    num = int(input("Digite um número: "))
    while(num != -1):
        cont = 0
        for i in range(1, num+1):
            if(num % i == 0):
                cont += 1
        if(0 < cont <= 2):
            print("Primo")
        else:
            print("Não")
        num = int(input("Digite um número: "))
def q3():
    """Valquíria trabalha em uma padaria e foi roubada ontem. Seus clientes ficaram com pena e resolveram organizar uma vaquinha para comprar um novo celular para ela. 
    Escreva um programa que receba como entrada o valor doado por cada cliente, até que seja informado um valor negativo, e exiba o total arrecadado e o valor médio doado por 
    eles."""

    doacao = float(input("Digite o valor doação: "))
    pessoas = 0
    total = 0
    media = 0
    while(doacao > 0):
        pessoas += 1
        total += doacao
        media = total / pessoas
        doacao = float(input("Digite o valor doação: "))
    print(f"{total:.2f}\n{media:.2f}")


def q4():
    """A Locadora de Veículos Eudora lançou uma grande promoção esse mês: pagando apenas R$ 90 por diária, o cliente pode alugar um carro de passeio. Para cada diária, 
    o cliente recebe uma cota de quilometragem de 100 Km. Cada quilômetro a mais custará uma taxa extra de R$ 12.

Escreva um programa que receba como entrada a quantidade de dias e a quilometragem total rodada por um cliente dessa locadora e exiba o valor total a ser pago com duas 
casas decimais."""

    diaria = int(input("Digite a quantidade de dias: "))
    quilo = float(input("Digite os quilométros rodados: "))

    quiloExd = 0
    if(diaria == 0):
        print("Valor inválido")
    else:
        if(diaria * 100 < quilo):
            quiloExd = quilo - (diaria * 100)
        
        total = (diaria * 90) + (quiloExd * 12)

        print(f"{total:.2f}")
 
def q5():
    escala = input("Digite a escala de temperatura: ")
    temp = float(input(f"Digite o valor da temperatura em °{escala}: "))

    match(escala):
        case "F":
            tempC = (temp - 32) / 1.8
            tempK = (temp - 32) * (5/9) + 273.15
            print(f"{tempC:.2f} C\n{tempK:.2f} K") 
        case "C":
            tempF = temp * 1.8 + 32
            tempK = temp + 273.15
            print(f"{tempF:.2f} F\n{tempK:.2f} K")
        case "K":
            if(temp < 0):
                print("Valor de temperatura abaixo do minimo")
            else:
                tempC = temp - 273.15
                tempF = (temp - 273.15) * 1.8 + 32
                print(f"{tempC:.2f} C\n{tempF:.2f} F")

if __name__=="__main__":
    # teste sua questão manualmente aqui
    q5()