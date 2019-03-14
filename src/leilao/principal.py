from src.leilao.dominio import Usuario, Lance, Leilao

gui = Usuario('gui', 100.0)
yuri = Usuario('yuri', 100.0)

leilao = Leilao('celular')

lance_do_yuri = Lance(yuri, 100.0)
lance_do_gui = Lance(gui, 150.0)


leilao.grava_lances(lance_do_yuri)
leilao.grava_lances(lance_do_gui)


for lance in leilao.lances:
    print(f'O usuario {lance.usuario.nome} deu um lance de {lance.valor} no leilão de {leilao.descricao}')

#leilao.grava_lances(leilao.lances)

print(f'O menor lance foi {leilao.menor_lance} e o maior foi {leilao.maior_lance}')