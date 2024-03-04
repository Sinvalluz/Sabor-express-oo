class Restaurante():
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = 'praca'
restaurante_praca.categoria = 'Goumert'

print(vars(restaurante_praca))