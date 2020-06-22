class EnviadorDeSpam:
    def __init__(self, sessao, enviador):
        self.enviador = enviador
        self.sessao = sessao

    def enviar_email(self, remetente, assunto, corpo):
        for usuario in self.sessao.listar():
            self.enviador.enviar(
                remetente,
                usuario.email,
                assunto,
                corpo
            )