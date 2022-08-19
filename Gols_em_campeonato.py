jogador=dict()
partidas=list()
aproveitamento= dict()
time=list()
while True:
    jogador['NOME']=str(input('Informe o nome do jogador: '))
    jogador['QTD DE PARTIDAS']=int(input(f"Em quantas partidas, {jogador['NOME']} esteve presente  ? "))
    partidas.clear()
    for p in range(jogador['QTD DE PARTIDAS']):
        partidas.append(int(input(f"Quantos gols foram feitos na {p+1}º partida: ")))
    jogador["GOLS / PARTIDA"]= partidas[:]
    jogador["TOTAL DE GOLS"]= sum(partidas)
    time.append(jogador.copy())
    print("="*50)

    resp= str(input(" DESEJA ADICIONAR MAIS ALGUM JOGADOR ?\n [SIM] / [NÃO]")).strip().upper()
    while resp not in 'SN':
        print("OPÇÃO INVALIDA")
        resp=str(input("SE DESEJA ADICIONAR MAIS ALGUM JOGADOR\n TECLE [SIM], CASO CONTRARIO, TECLE [NÃO]")).strip().upper()
    if resp=='N':
        break
print("=" * 50)
print(f"O JOGADOR PARTICIPOU DE {jogador['QTD DE PARTIDAS']} partidas e marcou {jogador['TOTAL DE GOLS']}gols")
print("-="*50)
while True:
    dados_jogador=int(input("Deseja mostrar dados de qual jogador ?"
                            "\nATENÇÃO."
                            "\n->O INTERVALOR DE JOGADORES SELECIONADOS É A PARTIR DE 0"
                            "\n-> DIGITE -1 SE DESEJA ENCERRAR."))
    if dados_jogador== -1:
        break
    if dados_jogador>=len(time):
        print("INTERVALO NÃO VALIDO")
    else:
        print(f"Os dados do jogador {time[dados_jogador]['NOME']}")
        for i,g in enumerate(time[dados_jogador]['GOLS / PARTIDA']):
            print(f"NA PARTIDADE {i+1}, ele fez {g} gols")

print(jogador)
print("-=" *50)
print("FIM DO PROGRAMA.")




