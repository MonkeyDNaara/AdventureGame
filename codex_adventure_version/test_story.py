import io
import time
import unittest
from unittest.mock import patch

from story import DEFAULT_PARAGRAPH_PAUSE, get_room_text, intro_text, type_text


class StoryTests(unittest.TestCase):
    def test_intro_mentions_the_torch(self):
        self.assertIn("flame", intro_text.lower())

    def test_known_room_text_is_returned(self):
        text = get_room_text("level_1", 17, 1)

        self.assertIn("torch", text.lower())

    def test_unknown_room_returns_no_repeated_default_text(self):
        text = get_room_text("level_1", 99, 99)

        self.assertEqual(text, "")

    def test_default_paragraph_pause_is_longer(self):
        self.assertGreaterEqual(DEFAULT_PARAGRAPH_PAUSE, 0.8)

    def test_type_text_pauses_between_paragraphs(self):
        sleep_calls = []

        with patch.object(time, "sleep", side_effect=lambda delay: sleep_calls.append(delay)):
            with patch("sys.stdout", new=io.StringIO()):
                type_text("One\n\nTwo", delay=0.01, paragraph_pause=0.8)

        self.assertIn(0.8, sleep_calls)


if __name__ == "__main__":
    unittest.main()
