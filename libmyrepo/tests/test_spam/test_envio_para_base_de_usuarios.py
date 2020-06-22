from unittest.mock import Mock

import pytest

from libmyrepo.spam.enviador_de_email import Enviador
from libmyrepo.spam.main import EnviadorDeSpam
from libmyrepo.spam.models import Usuario


class EnviadorMock(Enviador):
    def __init__(self):
        super().__init__()
        self.qtd_email_enviados = 0
        self.parametros_de_envio = None

    def enviar(self, remetente, destinatario, assunto, corpo):
        self.parametros_de_envio = (remetente, destinatario, assunto, corpo)
        self.qtd_email_enviados += 1


@pytest.mark.parametrize(
    'usuarios',
    [
        [Usuario(nome='Enos', email='enos@test.com'),
         Usuario(nome='Teteo', email='teteo@test.com')],
        [Usuario(nome='Enos', email='enos@test.com')]
    ]
)
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_email(
        'enos@test.com',
        'Assunto Enos,',
        'Corpo Confira tudo que é spam'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Enos', email='enos@test.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_email(
        'cabrau@test.com',
        'Assunto Enos',
        'Corpo Confira tudo que é spam'
    )
    enviador.enviar.assert_called_once_with(
        'cabrau@test.com',
        'enos@test.com',
        'Assunto Enos',
        'Corpo Confira tudo que é spam'
    )
