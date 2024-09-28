# function que verifica se o número informado está na sequência de fibonacci
def pertence_fibonacci(numero):
    # começamos a sequência com os dois primeiros números 0 e 1, como a própria definição da fibonacci
    a, b = 0, 1
    # seguimos gerando a sequência até que o valor 'b' ultrapasse o número que estamos verificando
    while b <= numero:
        # se em algum momento 'b' for igual ao número informado, então ele faz parte da sequência
        if b == numero:
            return True
        # atualizamos os valores: 'a' se torna o 'b' e 'b' passa a ser a soma de 'a' e 'b'
        a, b = b, a + b
    # se passamos por toda a sequência sem encontrar o número, então ele não faz parte
    return False

# aqui é onde definimos o número que queremos verificar; pode usar entrada de usuário, mas já vou deixar um exemplo
numero = 21  # exemplo de número, pode mudar ou usar int(input("digite um número: "))

# verificamos se o número informado pertence ou não à sequência de fibonacci e mostramos a mensagem correspondente
if pertence_fibonacci(numero):
    print(f"o número {numero} pertence à sequência de fibonacci.")
else:
    print(f"o número {numero} não pertence à sequência de fibonacci.")


# função para contar quantas vezes a letra 'a' aparece, independentemente de ser maiúscula ou minúscula
def contar_a(string):
    # para facilitar a contagem, vamos converter toda a string para minúscula; assim, não precisamos nos preocupar com 'A' ou 'a'
    string = string.lower()
    # agora usamos a função count para contar todas as ocorrências da letra 'a'
    quantidade = string.count('a')
    return quantidade

# string que queremos analisar; você pode trocar por uma entrada do usuário, mas vou deixar um exemplo claro
string = "quero muito esse estágio por favorrrrrrrr."  # pode mudar ou usar input("Digite uma frase: ")

# chamamos a função para contar e imprimimos o resultado, porque é sempre legal saber quantas vezes a letra 'a' apareceu
quantidade_a = contar_a(string)
print(f"a letra 'a' aparece {quantidade_a} vezes na string.")


# vamos agora reproduzir o trecho de código dado na pergunta e ver o que acontece no final
indice = 12  # o valor inicial do índice é 12, conforme o exemplo
soma = 0  # começamos com a soma igual a zero, porque ainda não somamos nada
k = 1  # e o 'k' começa valendo 1

# enquanto 'k' for menor que 'indice', o laço continua; estamos acumulando valores
while k < indice:
    k = k + 1  # aumentamos o 'k' em 1 a cada iteração
    soma = soma + k  # somamos o valor atual de 'k' na variável 'soma'

# mostramos qual foi o resultado final da soma depois que o laço terminou de executar
print(f"o valor final da variável SOMA é: {soma}")


# agora, vamos resolver as sequências de lógica uma por uma, porque desafios assim sempre são divertidos
# a) sequência que só tem números ímpares consecutivos
print("a) 1, 3, 5, 7, 9")  # aqui está o próximo número, que é 9

# b) sequência de números que são potências de 2
print("b) 2, 4, 8, 16, 32, 64, 128")  # o próximo é 128, basta continuar dobrando

# c) sequência dos quadrados perfeitos (0², 1², 2², etc.)
print("c) 0, 1, 4, 9, 16, 25, 36, 49")  # o próximo é 7² que dá 49

# d) sequência dos quadrados de números pares (2², 4², etc.)
print("d) 4, 16, 36, 64, 100")  # 10² é 100, então esse é o próximo

# e) sequência de fibonacci de novo, mas começando no 1
print("e) 1, 1, 2, 3, 5, 8, 13")  # o próximo é 13

# f) sequência com um padrão um pouco mais estranho, mas o próximo número é 200
print("f) 2, 10, 12, 16, 17, 18, 19, 200")  # enfim, é 200


# basicamente, meu raciocínio foi:
# 1. primeiro, ligamos o primeiro interruptor e deixamos ligado por alguns minutos (assim a lâmpada vai esquentar)
# 2. depois desligamos o primeiro e ligamos o segundo interruptor
# 3. sala das lâmpadas:
# - a lâmpada que estiver acesa agora é controlada pelo segundo interruptor
# - a lâmpada que estiver apagada mas quente foi ligada pelo primeiro interruptor
# - e a lâmpada que está apagada e fria é controlada pelo terceiro interruptor
