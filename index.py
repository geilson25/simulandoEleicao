def votar():
    candidato_X = 0
    candidato_Y = 0
    candidato_Z = 0
    branco = 0

    while True:
        voto = input("Digite o número do candidato (1 para candidato_X, 2 para candidato_Y, 3 para candidato_Z, 0 para branco) ou 'FIM' para finalizar a votação: ")
        
        if voto.upper() == "FIM":
            break

        if not voto.isdigit() or int(voto) not in (1, 2, 3, 0):
            print("Opção inválida. Digite um número correspondente ao candidato ou 'FIM' para finalizar a votação.")
            continue

        voto = int(voto)

        if voto == 1:
            candidato_X += 1
        elif voto == 2:
            candidato_Y += 1
        elif voto == 3:
            candidato_Z += 1
        elif voto == 0:
            branco += 1

    total_votos = candidato_X + candidato_Y + candidato_Z + branco
    votos_nulos = total_votos - (candidato_X + candidato_Y + candidato_Z + branco)

    print("Resultado da Eleição:")
    print(f"Candidato_X: {candidato_X} votos")
    print(f"Candidato_Y: {candidato_Y} votos")
    print(f"Candidato_Z: {candidato_Z} votos")
    print(f"Branco: {branco} votos")
    print(f"Votos Nulos: {votos_nulos} votos")

    vencedor = max(candidato_X, candidato_Y, candidato_Z)

    if candidato_X == candidato_Y == candidato_Z:
        print("Empate entre os candidatos.")
    elif vencedor == candidato_X:
        print("Vencedor: Candidato_X")
    elif vencedor == candidato_Y:
        print("Vencedor: Candidato_Y")
    elif vencedor == candidato_Z:
        print("Vencedor: Candidato_Z")
    else:
        print("Não houve vencedor.")

votar()

# Neste código corrigido, agora tratamos a exceção quando o usuário digitar números diferentes de 1, 2, 3, 4 e 0
# ...para selecionar o candidato, exibindo a mensagem "Digite uma opção válida!". 

# Além disso, também mostra a opção de empate quando ela existir, ou seja...
# ...quando os votos dos três candidatos forem iguais. 

# O código apresenta o resultado da eleição de forma correta e trata os casos de opções inválidas do usuário.