from libmyrepo.spam.models import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Enos', email='enos@test.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuario(sessao):
    usuarios = [Usuario(nome='Enos', email='enos@test.com'),
                Usuario(nome='Teteo', email='teteo@test.com')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()

