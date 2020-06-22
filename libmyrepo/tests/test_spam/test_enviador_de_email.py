import pytest

from libmyrepo.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'destinatario',
    ['enos@spam.com', 'foo@bar.com']
)
def test_destinatario(destinatario):
    enviador = Enviador
    resultado = enviador.enviar(
        'noreply@spam.com',
        destinatario,
        'No Reply',
        'Spam Spam spam '
    )
    assert destinatario in resultado


@pytest.mark.parametrize(
    'destinatario',
    ['', 'foo']
)
def test_destinatario_invalido(destinatario):
    enviador = Enviador
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            'noreply@spam.com',
            destinatario,
            'No Reply',
            'Spam Spam spam '
        )
