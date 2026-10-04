import unittest

from app import Figure
import unittest
from unittest.mock import patch

from app import Figure, get_figure_length_from_user


class TestFigure(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Figure("квадрат", 5)

    def test_figure_type(self):
        self.assertEqual("квадрат", self.obj.get_figure_type)

    def test_figure_length(self):
        self.assertEqual(5, self.obj.get_figure_length)

    # Додав тести: методу get_angles для квадрата, прямокутника та трикутника
    def test_get_angles(self):
        square = Figure("квадрат", 4)
        rectangle = Figure("прямокутник", 8)
        triangle = Figure("трикутник", 3)

        self.assertEqual(square.get_angles(), 4)
        self.assertEqual(rectangle.get_angles(), 4)
        self.assertEqual(triangle.get_angles(), 3)

    # Додав перевірку на невідомий тип фігури
    def test_invalid_figure(self):
        with self.assertRaises(AssertionError):
            Figure("коло", 1)

    # Додав перевірку перевірка на нульову довжину
    def test_zero_length(self):
        with self.assertRaises(AssertionError):
            Figure("квадрат", 0)

    # Додав перевірку на від'ємну довжину
    def test_negative_length(self):
        with self.assertRaises(AssertionError):
            Figure("квадрат", -5)

    # Додав тест із subTest для всіх типів Figure
    def test_all_figure_types_with_subtest(self):
        types = ["квадрат", "прямокутник", "трикутник"]
        for figure_type in types:
            with self.subTest(figure_type=figure_type):
                fig = Figure(figure_type, 10)
                self.assertEqual(fig.get_figure_type, figure_type)


    # Додав тестування функції з input() за допомогою patch
    @patch("builtins.input", return_value="15")
    def test_get_figure_length_from_user(self, mock_input):
        result = get_figure_length_from_user()
        self.assertEqual(result, 15)
        mock_input.assert_called_once_with("Введіть довжину сторони: ")

if __name__ == "__main__":
    unittest.main(verbosity=2)