from django.test import SimpleTestCase

from strings_convertions.constants import alphabet_map
from strings_convertions.views import MyRESTView

class AlphabetTestCase(SimpleTestCase):

    def map_correct_alphabet_to_digit(self):
        """Map correct alphabets to digits and ignore all non-literal symbol."""
        test_one = MyRESTView.string_processing('a')
        test_two = MyRESTView.string_processing('w')

        self.assertEqual(test_one, 1)
        self.assertEqual(test_two, 23)
        self.assertEqual(test_two, 24)
