import unittest
from .searcher import PopulationSearcher


class SearcherTest(unittest.TestCase):
    def test_process_subject(self):
        cases = {
            'Чувашия': 'чувашия',
            'Республика Башкортостан': 'башкортостан',
            'Челябинская область': 'челябинская',
            'Ханты-Мансийский  АО': 'хантымансийский ао',
            'Ханты-Мансийский Автономный округ': 'хантымансийский ао',
            'Сочи': 'краснодарский',
            'Московская область': 'москва',
            'Ленинградская область': 'санктпетербург',
            'Республика Саха (Якутия)': 'якутия',
        }

        searcher = PopulationSearcher()
        for input_value, expected in cases.items():
            actual = searcher._process_subject(input_value)
            self.assertEqual(expected, actual)

    def test_process_city(self):
        cases = {
            'Соль-Илецк': 'сольилецк',
            'Старый  Оскол': 'старый оскол',
        }

        searcher = PopulationSearcher()
        for input_value, expected in cases.items():
            actual = searcher._process_city(input_value)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
