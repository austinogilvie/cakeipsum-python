"""Core generation logic for cakeipsum."""

import random
from typing import List

from .words import WORDS

CAKE_IPSUM_START = "Cake ipsum dolor sit amet"
LOVE_PHRASES = [
    "I love",
    "I love",
]


class CakeIpsum:
    """A cake/dessert-themed Lorem Ipsum text generator."""

    def __init__(
        self,
        start_with_cake_ipsum: bool = False,
        love: bool = False,
    ):
        self.start_with_cake_ipsum = start_with_cake_ipsum
        self.love = love
        self._started = False

    def __repr__(self) -> str:
        return (
            f"CakeIpsum(start_with_cake_ipsum={self.start_with_cake_ipsum!r}, "
            f"love={self.love!r})"
        )

    def words(self, n: int) -> str:
        """Generate n random dessert words."""
        if n <= 0:
            return ""

        result_words: List[str] = []

        if self.start_with_cake_ipsum and not self._started:
            self._started = True
            start_words = CAKE_IPSUM_START.split()
            if n <= len(start_words):
                return " ".join(start_words[:n])
            result_words.extend(start_words)
            n -= len(start_words)

        for _ in range(n):
            if self.love and random.random() < 0.10:
                result_words.append(random.choice(LOVE_PHRASES))
            result_words.append(random.choice(WORDS))

        return " ".join(result_words)

    def sentences(self, n: int) -> str:
        """Generate n sentences (5-10 words each)."""
        if n <= 0:
            return ""

        sentences_list: List[str] = []

        for i in range(n):
            word_count = random.randint(5, 10)
            sentence_words = self.words(word_count)

            # Capitalize first letter of sentence
            if sentence_words:
                sentence_words = sentence_words[0].upper() + sentence_words[1:]

            sentences_list.append(sentence_words + ".")

        return " ".join(sentences_list)

    def paragraphs(self, n: int, length: str = "medium") -> str:
        """Generate n paragraphs.

        Args:
            n: Number of paragraphs to generate.
            length: Paragraph length - 'short' (3-5 sentences),
                   'medium' (6-11 sentences), or 'long' (12-15 sentences).

        Returns:
            Generated paragraphs separated by double newlines.
        """
        if n <= 0:
            return ""

        length_ranges = {
            "short": (3, 5),
            "medium": (6, 11),
            "long": (12, 15),
        }

        if length not in length_ranges:
            length = "medium"

        min_sentences, max_sentences = length_ranges[length]
        paragraphs_list: List[str] = []

        for _ in range(n):
            sentence_count = random.randint(min_sentences, max_sentences)
            paragraph = self.sentences(sentence_count)
            paragraphs_list.append(paragraph)

        return "\n\n".join(paragraphs_list)
