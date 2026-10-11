import pytest
from app import Figure


def test_triangle_type():
    """Проверка корректности типа фигуры через стандартный assert."""
    triangle = Figure("трикутник", 4)
    assert triangle.type == "трикутник"


def test_invalid_length():
    """Проверка выброса исключения через pytest.raises."""
    with pytest.raises(AssertionError):
        Figure("квадрат", 0)

@pytest.mark.parametrize("figure", Figure.FIGURES)
def test_allowed_figure(figure):
    assert Figure(figure, 1).type == figure

@pytest.fixture
def square():
    return Figure("квадрат", 5)

def test_square_fixture(square):
    assert square.type == "квадрат"
    assert square.length == 5

## Завдання 1: Параметризований тест для всіх дозволених фігур ##
@pytest.mark.parametrize("figure_type", Figure.FIGURES)
def test_all_allowed_figures(figure_type):
    """Перевіряє успішне створення кожної допустимої фігури зі списку Figure.FIGURES."""
    fig = Figure(figure_type, 1)
    assert fig.type == figure_type

## Завдання 2: Fixture для фігури з довжиною 10 та перевірка її властивостей ##

@pytest.fixture
def figure_len_10():
    """Створює екземпляр фігури із заданою довжиною 10."""
    return Figure("квадрат", 10)


def test_figure_len_10_properties(figure_len_10):
    """Перевіряє правильність збереження властивостей типу та довжини."""
    assert figure_len_10.type == "квадрат"
    assert figure_len_10.get_figure_length == 10

## Завдання 3: Тести для неправильних типів і некоректної довжини ##

@pytest.mark.parametrize("invalid_type", ["трапеція", "овал", "ромб", "зірка"])
def test_invalid_figure_types(invalid_type):
    """Перевіряє викид AssertionError при спробі створити фігуру недозволеного типу."""
    with pytest.raises(AssertionError):
        Figure(invalid_type, 5)


@pytest.mark.parametrize("invalid_length", [0, -1, -5, -20])
def test_invalid_figure_lengths(invalid_length):
    """Перевіряє викид AssertionError для нульової або від'ємної довжини."""
    with pytest.raises(AssertionError):
        Figure("квадрат", invalid_length)

import pytest
from app import Figure


# ==============================================================================
# Завдання 7: Маркери pytest (unit)
# ==============================================================================
@pytest.mark.unit
def test_unit_square_type():
    fig = Figure("квадрат", 4)
    assert fig.type == "квадрат"


@pytest.mark.unit
def test_unit_triangle_length():
    fig = Figure("трикутник", 7)
    assert fig.get_figure_length == 7


# ==============================================================================
# Завдання 8: Фікстура зі scope="module"
# ==============================================================================
@pytest.fixture(scope="module")
def shared_figure():
    """Створюється один раз для всього модуля тестів."""
    return Figure("прямокутник", 12)


def test_shared_figure_type(shared_figure):
    assert shared_figure.type == "прямокутник"


def test_shared_figure_length(shared_figure):
    assert shared_figure.get_figure_length == 12


# ==============================================================================
# Завдання 9: Навмисно зламаний тест
# ==============================================================================
def test_broken_intentionally():
    fig = Figure("квадрат", 5)
    assert fig.type == "коло"  # Помилка: "квадрат" != "коло"