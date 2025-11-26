from app import Quadro, Coluna, Tarefa
from pytest import fixture
from faker import Faker
import factory

fake = Faker()


class ColunaFactory(factory.Factory): # type: ignore
    class Meta: # type: ignore
        model = Quadro()
    nome = factory.Faker('name') # type: ignore
    tarefa = [Tarefa('A')]

class QuadroFactory(factory.Factory): # type: ignore
    class Meta: # type: ignore
        model = Quadro()
    colunas = ColunaFactory.build_batch(5)

@fixture
def factory_boy_test():
    QuadroFactory.build()

@fixture
def quadro(scope='function'):
    return Quadro()

@fixture
def quadro_parametrizado(request):
    return Quadro()

@fixture
def quadro_com_coluna(quadro):
    quadro.inserir_coluna(Coluna(fake.pystr()))
    return quadro

@fixture
def quadro_com_colunas(quadro_com_colunas):
    quadro_com_colunas.inserir_coluna(Coluna(fake.pystr()))
    return quadro_com_colunas
