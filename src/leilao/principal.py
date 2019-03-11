from src.leilao.dominio import Usuario, Lance, Leilao, Avaliador

gui = Usuario('gui')
yuri = Usuario('yuri')

leilao = Leilao('celular')

lance_do_yuri = Lance(yuri, 100.0)
lance_do_gui = Lance(gui, 150.0)


leilao.lances.append(lance_do_yuri)
leilao.lances.append(lance_do_gui)


for lance in leilao.lances:
    print(f'O usuario {lance.usuario.nome} deu um lance de {lance.valor} no leilão de {leilao.descricao}')

avaliador = Avaliador()
avaliador.avalia(leilao)
print(f'O menor lance foi {avaliador.menor_lance} e o maior foi {avaliador.maior_lance}')