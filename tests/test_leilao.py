from unittest import TestCase

from src.leilao.dominio import Usuario, Leilao, Lance


class TestLeilao(TestCase):
    def setUp(self):
        self.gui = Usuario('gui', 500.0)
        self.leilao = Leilao('celular')
        self.lance_do_gui = Lance(self.gui, 150.0)

    def test_deve_retornar_o_maior_e_o_menor_valor_dos_lances_que_estao_em_ordem_crescente(self):
        yuri = Usuario('yuri', 400.0)
        lance_do_yuri = Lance(yuri, 100.0)

        self.leilao.grava_lances(lance_do_yuri)
        self.leilao.grava_lances(self.lance_do_gui)

        vlr_menor_esperado = 100.0
        vlr_maior_esperado = 150.0
        self.assertEqual(vlr_menor_esperado, self.leilao.menor_lance)
        self.assertEqual(vlr_maior_esperado, self.leilao.maior_lance)

    def test_nao_deve_aceitar_um_lance_menor_que_o_ultimo_dado(self):
        with self.assertRaises(ValueError):
            yuri = Usuario('yuri', 550.0)
            lance_do_yuri = Lance(yuri, 100.0)
            self.leilao.grava_lances(self.lance_do_gui)
            self.leilao.grava_lances(lance_do_yuri)


    def test_deve_retornar_o_mesmo_valor_para_o_maior_e_menor_lance_quando_o_leilao_tiver_apenas_um_lance(self):
        yuri = Usuario('yuri', 550.0)
        lance_do_yuri = Lance(yuri, 100.0)
        self.leilao.grava_lances(lance_do_yuri)
        vlr_menor_esperado = 100.0
        vlr_maior_esperado = 100.0
        self.assertEqual(vlr_menor_esperado, self.leilao.menor_lance)
        self.assertEqual(vlr_maior_esperado, self.leilao.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_dos_lances_com_mais_de_dois_lances_que_estao_em_ordem_crescente(self):
        ceni = Usuario('ceni', 600.0)
        yuri = Usuario('yuri', 550.0)
        lance_do_ceni = Lance(ceni, 200.0)
        lance_do_yuri = Lance(yuri, 160.0)

        self.leilao.grava_lances(self.lance_do_gui)
        self.leilao.grava_lances(lance_do_yuri)
        self.leilao.grava_lances(lance_do_ceni)

        vlr_menor_esperado = 150.0
        vlr_maior_esperado = 200.0
        self.assertEqual(vlr_menor_esperado, self.leilao.menor_lance)
        self.assertEqual(vlr_maior_esperado, self.leilao.maior_lance)

    def test_deve_aceitar_apenas_um_lance(self):
        self.leilao.grava_lances(self.lance_do_gui)
        qtd_lance_esperado = 1
        self.assertEqual(qtd_lance_esperado, self.leilao.total_lances())

    def test_deve_aceitar_mais_um_lance_desde_que_o_usuario_do_ultimo_lance_seja_diferente_do_atual(self):
        yuri = Usuario('yuri', 550.0)
        lance_do_yuri = Lance(yuri, 200.0)
        self.leilao.grava_lances(self.lance_do_gui)
        self.leilao.grava_lances(lance_do_yuri)
        qtd_lance_esperado = 2
        self.assertEqual(qtd_lance_esperado, self.leilao.total_lances())

    def test_deve_ignorar_lance_atual_desde_que_o_usuario_do_ultimo_lance_seja_igual_ao_atual(self):

        lance_do_gui300 = Lance(self.gui, 300.0)
        with self.assertRaises(ValueError):
            self.leilao.grava_lances(self.lance_do_gui)
            self.leilao.grava_lances(lance_do_gui300)

