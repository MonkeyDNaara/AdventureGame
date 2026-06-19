import io
import time
import unittest
from unittest.mock import patch

from story import get_room_text, intro_text, type_text


class StoryTests(unittest.TestCase):
    def test_intro_exists(self):
        self.assertIn("flickers", intro_text)

    def test_unknown_room_has_no_default_text(self):
        self.assertEqual(get_room_text("main", 99, 99), "")

    def test_type_text_waits_between_paragraphs_when_wait_func_is_given(self):
        waits = []

        with patch.object(time, "sleep", return_value=None):
            with patch("sys.stdout", new=io.StringIO()):
                type_text("One\n\nTwo", wait_func=lambda prompt: waits.append(prompt))

        self.assertEqual(len(waits), 1)
        self.assertIn("Space", waits[0])


if __name__ == "__main__":
    unittest.main()
