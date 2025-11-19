# Uma introdução aos testes: Como fazer?

## Como um programa funciona?

    input  ->  app  ->  output

```python
# arquivo: app.py

# Faça um programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# c = 5*((f-32)/9)

# input
temperatura = float(input('Digite a temperatura em Fahrenheit: '))

# processamento
celsius = 5 * ((temperatura - 32) / 9)

# output
print(f'A temperatura em Celsius é: {celsius:2f}')
```

### Afinal o que são testes:

-   Um ciclo de feedback.
-   Uma garantia de que funciona.

"O que podemos fazer para que esse código consiga ser testado sem a nossa interferencia?"

Deconposição:

-   Basicamente, se nosso software tem 3 ou 5.000 linha. Ele é composto por diversos elementos.
-   Um software não é nada mais que um monte de blocos de código. Cada bloco executa uma função especifica de código.

Como podemos isolar isso:

-   Devemos separar as preocupações (Dijkstra).
-   Em pequenos blocos isolados, que podem ser chamados de forma independente.
-   Uma função pode ser uma forma de isolar isso.

```python
# arquivo: app.py

def conversao(temperatura):
    return 5 * ((temperatura - 32) / 9)


# input
temperatura = float(input('Digite a temperatura em Fahrenheit: '))

# processamento
celsius = conversao(temperatura)

# output
print(f'A temperatura em Celsius é: {celsius:2f}')
```

### Taxonomia dos testes:

    arranjo  ->  ação  ->  afirmação

-   Arranjo: arranjo de dados para o input.
-   Ação: ação de executar o código isolado com o arranjo de dados.
-   Afirmação: verificação que os valores arranjados, com a ação resultam no que gostaria.

Um roteiro para um teste:
-> quero afirmar que quando a função de `conversão` receber o valor 32 o resultado será 0.

```python
# arquivo: app.py

"""
Esse programa faz conversões

Testes:
>>> conversao(32)
0.0

>>> conversao(-40)
-40.0
"""

def conversao(temperatura):
    return 5 * ((temperatura - 32) / 9)


# input
temperatura = float(input('Digite a temperatura em Fahrenheit: '))

# processamento
celsius = conversao(temperatura)

# output
print(f'A temperatura em Celsius é: {celsius:2f}')
```

A palavra assert:
<b>Assert</b>, é uma palavra do inglês que se destina a "afirmação" de algo.
Algo como:

-   Afirme que a conversão de 32 graus fahrenheit é igual a 0 graus celsius.
-   Afirme que a conversão de 100 graus fahrenheit é igual a 37.77 graus celsius.

```python
# arquivo: test.py

from app import conversao

assert conversao(32) == 0.0
assert conversao(100) == 37.77

assert conversao(0) == 1, 'Deu erro!'
```

### Unittest

O python tem uma bibloteca nativa de testes. Que pode nos auxiliar para saber o que funciona e o que não funciona.

```python
#arquivo: test.py

from unittest import TestCase
from app import conversao


class TestConversao(TestCase):
    def test_deve_retornar_0_quando_receber_32(self):
        self.assertEqual(conversao(32), 0)

    def test_deve_retornar_37_77_quando_receber_100(self):
        self.assertAlmostEqual(conversao(100), 37.77, places=1)
```

### Descobrindo a cobertura de testes

Ás vezes, testamos, mas não sabemos exatamente se testamos o que precisa ser testado. Ou achamos que estamos testando algo que na realidade não estamos testando de fato. Para isso, temos a cobertura de testes

```shell
pip install coverage
python -m coverage run -m unittest test.py
coverage report
coverage html
```
