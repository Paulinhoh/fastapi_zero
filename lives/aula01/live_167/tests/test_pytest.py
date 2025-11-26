from codigo.game import brincadeira
from pytest import mark, fixture
import sys

@fixture
def minha_fixture():
    """Essa fixture é top, mas só vai ser feita na proxima live"""
    return 3

@mark.smoke
def test_quando_brincadeira_receber_1_deve_retornar_1():
    """ - Brincadeira - SUT - System Under Test"""
    # Given / Arrange
    entrada = 1
    esperado = 1
    # When / Act
    resultado = brincadeira(entrada)
    # Then / Assert
    assert resultado == esperado 

    # versão pequena
    # TDD - Kent beck - One-step Test
    # assert brincadeira(1) == 1


def test_quando_brincadeira_receber_2_deve_retornar_2():
    assert brincadeira(2) == 2 


@mark.smoke
def test_quando_brincadeira_receber_3_deve_retornar_queijo():
    assert brincadeira(3) == 'queijo'


@mark.goiabada
def test_quando_brincadeira_receber_5_deve_retornar_goiabada():
    assert brincadeira(5) == 'goiabada'


@mark.smoke
@mark.goiabada
def test_quando_brincadeira_receber_10_deve_retornar_goiabada():
    assert brincadeira(10) == 'goiabada'


@mark.goiabada
def test_quando_brincadeira_receber_20_deve_retornar_goiabada():
    assert brincadeira(20) == 'goiabada'


@mark.skip(reason="Ainda não foi implementado")
def test_quando_brincadeira_receber__1_deve_retornar_None():
    assert brincadeira(-1) == None


@mark.xfail
def test_xfail1():
    assert brincadeira(20) == 'goiabada'


@mark.xfail
def test_xfail2():
    assert brincadeira(20) != 'goiabada'


@mark.xfail(sys.platform == 'win32') # espera que não funione no windows
def test_xfail_windows():
    assert brincadeira(20) != 'goiabada'


@mark.skipif(sys.platform == 'win32') # vai pular esse teste se for no windows
def test_skipif_windows():
    assert brincadeira(20) != 'goiabada'


@mark.parametrizado
@mark.parametrize(
        'entrada, esperado',
        [
            (5, 'goiabada'),
            (10, 'goiabada'),
            (20, 'goiabada'),
            (25, 'goiabada'),
            (35, 'goiabada'),
        ]
)
def test_brincadeira_deve_retornar_goiabada_com_multiplos_de_5(entrada, esperado):
    assert brincadeira(entrada) == esperado


@mark.parametrizado
@mark.parametrize(
        'entrada, esperado',
        [
            (3, 'queijo'),
            (6, 'queijo'),
            (9, 'queijo'),
            (12, 'queijo'),
            (18, 'queijo'),
        ]
)
def test_brincadeira_deve_retornar_queijo_com_multiplos_de_3(entrada, esperado):
    assert brincadeira(entrada) == esperado


def test_brincadeira_deve_escrever_entrei_na_brincadeira_na_tela(capsys):
    brincadeira(0)
    resultado = capsys.readouterr()
    assert resultado.out == 'Entrei na brincadeira!\n'


@mark.exemplo_fixture
def test_minha_fixture_em_acao(minha_fixture):
    print(minha_fixture)
