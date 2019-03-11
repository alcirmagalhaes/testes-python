from unittest import TestCase

from src.leilao.dominio import Usuario, Leilao, Lance


class TestAvaliador(TestCase):
    def setUp(self):
        self.gui = Usuario('gui')
        self.leilao = Leilao('celular')
        self.lance_do_gui = Lance(self.gui, 150.0)

    def test_deve_retornar_o_maior_e_o_menor_valor_dos_lances_que_estao_em_ordem_crescente(self):
        yuri = Usuario('yuri')
        lance_do_yuri = Lance(yuri, 100.0)

        self.leilao.grava_lances(self.lance_do_gui)
        self.leilao.grava_lances(lance_do_yuri)

        vlr_menor_esperado = 100.0
        vlr_maior_esperado = 150.0
        self.assertEqual(vlr_menor_esperado, self.leilao.menor_lance)
        self.assertEqual(vlr_maior_esperado, self.leilao.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_dos_lances_que_estao_em_ordem_decrescente(self):
        yuri = Usuario('yuri')
        lance_do_yuri = Lance(yuri, 100.0)
        self.leilao.grava_lances(lance_do_yuri)
        self.leilao.grava_lances(self.lance_do_gui)

        vlr_menor_esperado = 100.0
        vlr_maior_esperado = 150.0
        self.assertEqual(vlr_menor_esperado, self.leilao.menor_lance)
        self.assertEqual(vlr_maior_esperado, self.leilao.maior_lance)


    def test_deve_retornar_o_mesmo_valor_para_o_maior_e_menor_lance_quando_o_leilao_tiver_apenas_um_lance(self):
        yuri = Usuario('yuri')
        lance_do_yuri = Lance(yuri, 100.0)
        self.leilao.grava_lances(lance_do_yuri)
        vlr_menor_esperado = 100.0
        vlr_maior_esperado = 100.0
        self.assertEqual(vlr_menor_esperado, self.leilao.menor_lance)
        self.assertEqual(vlr_maior_esperado, self.leilao.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_dos_lances_com_mais_de_dois_lances_que_estao_em_ordem_crescente(self):
        ceni = Usuario('ceni')
        yuri = Usuario('yuri')
        lance_do_ceni = Lance(ceni, 200.0)
        lance_do_yuri = Lance(yuri, 100.0)

        self.leilao.grava_lances(self.lance_do_gui)
        self.leilao.grava_lances(lance_do_yuri)
        self.leilao.grava_lances(lance_do_ceni)

        vlr_menor_esperado = 100.0
        vlr_maior_esperado = 200.0
        self.assertEqual(vlr_menor_esperado, self.leilao.menor_lance)
        self.assertEqual(vlr_maior_esperado, self.leilao.maior_lance)


