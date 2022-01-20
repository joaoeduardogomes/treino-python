def aumentar(preco = 0, taxa = 0, formato = False):
    '''
    -> Calcula o aumento de um determinado preço, e retorna o resultado com ou sem formatação.
    :param preco: o preço que se quer aumentar.
    :param taxa: a porcentagem do aumento.
    :param formato: se o retorno será formatado.
    :return: o valor aumentado, formatado ou não.
    '''
    res = preco + (preco * taxa / 100)
    return res if formato is False else moeda(res)

def diminuir(preco = 0, taxa= 0, formato = False):
    res = preco - (preco * taxa / 100)
    return res if formato is False else moeda(res)

def dobro(preco = 0, formato = False):
    res = preco * 2
    return res if not formato else moeda(res)
    # 'not formato' = 'formato is False'

def metade(preco = 0, formato = False):
    res = preco / 2
    return res if not formato else moeda(res)

def moeda(preco = 0, moeda = 'R$ '):
    return f'{moeda}{preco:.2f}'.replace('.', ',')
    # O 'replace' vai substituir todos os pontos por vírgulas

def resumo(preco = 0, taxa_aumento = 10, taxa_diminuicao = 5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)

    print(f"Preço analisado: \t{moeda(preco)}")

    print(f"Dobro do preço: \t{dobro(preco, True)}")

    print(f"Metade do preço: \t{metade(preco, True)}")

    print(f"Com {taxa_aumento}% de aumento: \t{aumentar(preco, taxa_aumento, True)}")

    print(f"Com {taxa_diminuicao}% de redução: \t{diminuir(preco, taxa_diminuicao, True)}")
    print('-' * 30)