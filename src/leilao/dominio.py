from src.leilao.excecao import LanceInvalido


class Usuario:

    def __init__(self, nome, vlr_carteira):
        self.__nome = nome
        self.__carteira = vlr_carteira

    @property
    def nome(self):
        return self.__nome

    @property
    def carteira(self):
        return self.__carteira

    def propoe_lance(self, leilao, vlr_lance):
        if self._lance_maior_que_valor_carteira(vlr_lance):
            raise LanceInvalido('O usuário não pode dar um lance maior que o valor da sua carteira')

        lance = Lance(self, vlr_lance)
        leilao.grava_lances(lance)
        self.__carteira -= vlr_lance

    def _lance_maior_que_valor_carteira(self, vlr_lance):
        return vlr_lance > self.carteira


class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor


class Leilao:

    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []
        self.menor_lance = 0.0
        self.maior_lance = 0.0

    def grava_lances(self, lance: Lance):

        if self._eh_lance_valido(lance):
            if self._nao_tem_lance():
                self.menor_lance = lance.valor
            self.maior_lance = lance.valor
            self.__lances.append(lance)
        else:
            raise ValueError('Erro no lance dado pelo usuário')

    def total_lances(self):
        return len(self.__lances)

    @property
    def lances(self):
        return self.__lances[:]

    def _nao_tem_lance(self):
        return not self.__lances

    def _usuario_lance_atual_eh_diferente_do_ultimo_lance(self, lance):
        if lance.usuario != self.__lances[-1].usuario:
            return True
        raise LanceInvalido('Um usuário não pode dar dois lances seguidos')

    def _valor_lance_atual_eh_maior_que_ultimo_lance(self, lance):
        if lance.valor > self.__lances[-1].valor:
            return True
        raise LanceInvalido('O valor do lance deve ser maior que o lance anterior')

    def _eh_lance_valido(self, lance):
        return self._nao_tem_lance() or (self._usuario_lance_atual_eh_diferente_do_ultimo_lance(
            lance) and self._valor_lance_atual_eh_maior_que_ultimo_lance(lance))
