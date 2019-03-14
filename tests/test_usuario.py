from src.leilao.dominio import Usuario, Leilao
import pytest


@pytest.fixture
def vini():
    return Usuario('Vini', 100.0)


@pytest.fixture
def leilao():
    return Leilao('Celular')


def test_deve_subtrair_valor_da_carteira_do_usuario_quando_propor_um_lance(vini, leilao):
    vini.propoe_lance(leilao, 50.0)
    assert (vini.carteira == 50.0)


def test_deve_aceitar_lancamento_com_valor_menor_que_o_da_carteira(vini, leilao):
    vini.propoe_lance(leilao, 10.0)
    assert (vini.carteira == 90.0)


def test_deve_aceitar_lancamento_com_o_mesmo_valor_menor_que_o_da_carteira(vini, leilao):
    vini.propoe_lance(leilao, 100.0)

    assert (vini.carteira == 0.0)


def test_nao_deve_aceitar_lancamento_maior_que_o_valor_da_carteira(vini, leilao):
    with pytest.raises(ValueError):
        vini.propoe_lance(leilao, 200.0)
