# Pytest Fixtures

OBS: só crie uma fixture quando tiver um código duplicado

## Books:

-   test-drive development
-   Growing object-oriented software guide by tests
-   xUnit test patterns

### O que é? Do que se alimenta:

Uma fixture é basicamente uma forma de evitar repetição de código em testes.

```python
from pytest import fixture

@fixture
def tarefas():
    return [
        ('estudar', 'feito'),
        ('dormir', 'feito'),
        ('comer', 'a feito'),
    ]
```

### Uma mensagem do passado

Ideia do Kent Beck (TDD) sobre fixtures:
"Se quisermos remover duplicação de nosso código modelo, queremos removeê-las do nosso código de teste também? Talvez."

### Todos os testes tem:

-   guiven
-   when
-   then

### Testes com 4 passos:

-   setUp
-   exercise
-   assert
-   tearDown

### Escopos: como de fato uma fixture se comporta?

Mas quais escopos existem?

-   function - antes e depois de cada função
    -   não é compartilhada
    -   default
-   class
-   module
-   package
-   session

### Faker

Faker é um duble de teste que cria objetos "de mentira" para simplificar a população de testes.

```python
fomr faker import Faker

fake = Faker()

@fixture
def cartao():
    return Cartao(nome=fake.pystr())
```

### Factory boy

O factory boy é uma forma de usar o faker para gerar objetos com dados "fakes"

```python
import factory

class CartaoFactory(factory.Factory):
    class Meta:
        model = Tarefa

    nome = factory.Faker('pystr', max_chars=10)

@fixture
def cartoes():
    return CartaoFactory.build_batch(10)
```
