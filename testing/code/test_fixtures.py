import pytest


@pytest.fixture
def my_fixture():
    print('my_fixture')


def test_foo(my_fixture):
    print('runing test')


@pytest.fixture
def fix1():
    print('fix1')
    yield
    # Cleanup
    print('Good bye: fix1')


def test_fix1(fix1):
    print('Running test_fix1')


@pytest.fixture
def fix2(my_fixture):
    yield
    # Cleanup
    print('Good bye: fix2')


def test_fix2(fix2):
    print('Running test_fix2')

@pytest.fixture
def some_data(my_fixture):
    print('some_data fixture')
    yield {'a': 1, 'b': 2}
    # Cleanup
    print('Good bye: fix2')


def test_some_data(some_data):
    print(some_data)
    print('Running test_fix2')



@pytest.mark.usefixtures('fix1', 'fix2')
def test_foo():
    print('Running test_foo')
