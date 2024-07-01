def cadastrar_senha():
    senha = input ('DIGITE A SENHA QUE DESEJA CADASTRAR:' )
    return senha

def verificar_senha(senha_cadastrada):
    senha_digitada = input ('DIGITE A SENHA PARA VERIFICAR:')

    if senha_digitada == senha_cadastrada:
        print('SENHA CORRETA')

    else:
        ('SENHA INCORRETA, ACESSO NEGADO.')