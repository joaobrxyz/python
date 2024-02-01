def notas(*n, sit=False):
    """
    → Função para analizar notas e situações de vários alunos.
    :param n: Uma ou mais notas dos alunos (aceita várias)
    :param sit: Valor opcional, indicando se deve ou não adicionar a situação
    :return: Dicionário com várias informações sobre a situação da turma.
    """
    nota = dict()
    nota['total'] = len(n)
    nota['maior'] = max(n)
    nota['menor'] = min(n)
    nota['média'] = sum(n) / len(n)
    if sit:
        if nota['média'] >= 7:
            nota['situação'] = 'BOA'
        elif nota['média'] >= 5:
            nota['situação'] = 'RAZOÁVEL'
        else:
            nota['situação'] = 'RUIM'
    return nota


# Programa principal
resp = notas(3.5, 10, 6.5, 0, 10, 10, 10, sit=True)
print(resp)
