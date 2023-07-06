import main
import unittest


class TesteMethods(unittest.TestCase):
    def test_should_reverse_sentence(self):
        texto = 'teste exercicio 01'
        expected = '01 exercicio teste'
        response = main.reverse_sentence(texto)
        self.assertEqual(response, expected)

    def test_should_remove_duplicated(self):
        texto = 'hello world'
        expected = 'helo wrd'
        response = main.remove_duplicates(texto)
        self.assertEqual(response, expected)

    def test_should_find_longest_palindroma(self):
        texto = 'babd'
        expected = 'bab'
        response = main.find_longest_palindroma(texto)
        self.assertEqual(response, expected)

    def test_should_capitalize_sentences(self):
        texto = 'oi! voce esta bem? estou, obrigado.'
        expected = 'Oi! Voce esta bem? Estou, obrigado.'
        response = main.capitalize_sentences(texto)
        self.assertEqual(response, expected)

    def test_is_polindroma_true(self):
        texto = 'abbba'
        response = main.is_polindroma(texto)
        self.assertTrue(response)

    def test_is_polindroma_false(self):
        texto = 'raceacar'
        response = main.is_polindroma(texto)
        self.assertFalse(response)

if __name__ == '__main__':
    unittest.main()
