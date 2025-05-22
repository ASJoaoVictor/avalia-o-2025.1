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
    pass

def q5():
    pass

if __name__=="__main__":
    # teste sua questão manualmente aqui
    q3()