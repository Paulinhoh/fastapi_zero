# Introdução ao Pytest

Pytest é um framework em python dedicado a testes. Uma alternativa mais "pythonica" ao unittest.

-   Simples
-   Escalavel
-   Rico em plugins
-   Suporte ao pypy
-   Primeira release em 2009
-   Atualmente na versão 6.2.4

<!-- behave -->

### Qual a cara de um teste minimo?

```python
# tests/test_python.py

def test_meu_primeiro_test():
    assert 1==1
```

-   tests/test_pytest.py . -> para rodar os tests
-   pytest . -> outra forma de rodar os test
-   pytest -v -> (verbose) mostra os tests com mais detalhes

## Com o que vamos praticar?

Vamos fazer uma adaptação abrasileirada do BuzzFizz que a Paty Mori apresentou me um tutorial de TDD no Capiyra de 2019.

Como funciona?
Vamos pegar um número inteiro, por exemplo: "1"

-   Quando o numero for **multiplo de 3**, deve responder "**Queijo**"
-   Quando o numero for **multiplo de 5**, deve responder "**Goibada**"
-   Quando o numero for **multiplo de 3 e de 5**, deve responder "**Romeu e Julieta**"

### O teste é formado por 3 etapas (GWT - AAA):

-   guive (dados)
-   when (quando)
-   then (então)

-   arange
-   act
-   assert

**OBS:** sempre quando o erro retornado em algum test não for AssertionError o problema esta na estrutura do código não o que o test erra.

### Olhando para as respostas do resumo:

```shell
test_pytest.py .FxXs
```

**Resumo**:

-   .: passou
-   F: falhou
-   x: falha esperada
-   X: falha esperada, mas não falhou
-   s: pulou (skiped)

### Resultado dos testes:

O pytest já conta com uma ferramenta de report incluida para o formato Junit (padrão dos frameworks de teste)

```shell
pytest --junitxml report.xml
```

### Linha de comando:

**Exemplo:**

```shell
pytest -k 'goiabada' # retorna somente os testes com 'goiabada'
```

-   -v: mostra o nome dos testes execultados
-   -s: mostra as saidas no console
-   -k "nome_dos_testes": filtra os resultados
-   -x: saida rapida

-   --pdb: para debugar quando falhar

-   -m "meu_marcador": marcadores
-   -rs: mostra o motivo do teste ter skipado

## Mark: marcações, argumentos e metadados

A funcionalidade de marcação pode nos ajudar a montar "tags" ou "grupos" para testes especificos. Podemos simplificar chamadas ou rodar testes especificos para casos especificos.

```python
from pytest import mark

@mark.tag # o marcador "tag" pode ter qualquer nome
def test_meu_quinto_teste():
    assert True

# pytest -m tag -> roda todos os testes com essa "tag"
```

### Filtro por tag:

As tags podem ser filtradas pelo argumento **-m marcador** na linha de comando. Você também pode fazer a marcação invertida **-m "not marcador"**.
Assim você pode ter controle de quais testes vão ser executados de maneira simples.

### Tags embutidas:

O pytest fornece um grupo de tags que facilitam o nosso dia a dia em coisas que não são comuns em varias suites de test.

-   @mark.skip: para pular um test
-   @mark.skipf: para pular um test em determinado contexto
-   @mark.xfail: é esperado que esse teste falhe em algum context
-   @mark.usefixture: falaremos depois sobre
-   @mark.parametrize: para parametrizar testes

```shell
pytest -rs  # mostra as rasoes por exemplo de ter skipado um test
```

### Mark.parametrize:

Imagine que você gostaria de fazer uma gama de testes somente alterando os valores e checando seus resultados? O parametrize cria um esquema de "sub testes" onde cada parâmetro será executado uma unica vez, mas o teste será executado multiplas vezes.

```python
@mark.parametrize(
    'parametro,resultado_esperado',
    [(1,3),(3,5),(5,7)]
)
def test_soma_mais_2(parametro, resultado_esperado):
    assert soma_mais_dois(parametro) == resultado_esperado
```

### xfail e skipif

**xfail** e **skipif** são metadados da função que podem dizer quando algum test deve falhar, pois é esperado, e quando um teste não deve ser executado.

```python
@mark.skipif(
    sys.platform == "win32",
    reason="Não funciona no windows",
)
def test_soma_2_linux():
    numero_do_pinguim = 42
    assert soma_mais_dois(numero_do_pinguim) == 42
```

## Fixtures:

### O que são fixtures?

A fixture é basicamente uma maneira de "entar" em um contexto. Ou prover uma ferramenta que precisa ser executada "antes" dos testes.

O teste é formado por 3 etapas (GWT - AAA):

-   guive (dados)
-   when (quando)
-   then (então)

-   arange
-   act
-   assert

xUnit Patterns - Gerard Mezaros

-   setup (dados)
-   exercise (quando)
-   verify (então)
-   tearDown (desmonta tudo antes que seja tarde)

### Quais fictures temos disponiveis?

-   capsys e variações: "espiona" o stdout
-   tempdir: cria um diretorio temporario
-   caplog: "espiona" logs
-   mokeypatch: adiciona atributos e metodos a objetos em runtime
-   ...

```python
def test_output(capsys):
   print('meu print bolado')
   captured = capsys.readouterr()
   assert captured.out == 'meu print bolado\n'
```

```shel
pytest --fixtures # mostra as fixtures ja instaladas
```

### Posso criar minhas próprias fixtures?

SIIM!

```python
from pytest import fixture
from app import create_app

@fixture
def flask_app():
    return create_app()

def test_com_app(flask_app):
    ...
```
