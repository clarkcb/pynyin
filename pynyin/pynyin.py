#!/usr/bin/env python3
# -*- coding: utf-8 -*-
################################################################################
#
# pynyin.py
#
# Convert between accented and unaccented/ascii pinyin
#
################################################################################

import unicodedata

class Pynyin(object):
    def __init__(self):
        self.tone_chars = [
            '\u0304', # COMBINING MACRON
            '\u0301', # COMBINING ACUTE ACCENT
            '\u030C', # COMBINING CARON
            '\u0300'  # COMBINING GRAVE ACCENT
            ]

    def __get_combining_form(self, pinyin_str: str) -> str:
        return unicodedata.normalize('NFKD', pinyin_str)

    def __get_combined_form(self, pinyin_str: str) -> str:
        return unicodedata.normalize('NFC', pinyin_str)

    def get_tone(self, pinyin_str: str) -> int:
        """Returns the tone of the pinyin string
           Note: if the string contains more than one tone diacritic,
                 only the first is returned
        """
        combining_form = self.__get_combining_form(pinyin_str)
        combining_chars = [c for c in combining_form if unicodedata.combining(c)]
        for c in combining_chars:
            if c in self.tone_chars:
                return self.tone_chars.index(c) + 1
        return 0

    def remove_tones(self, pinyin_str: str) -> str:
        """Returns the pinyin string with all tone diacritics removed
           (leaving any non-tone diacritics such as diaeresis)
        """
        combining_form = self.__get_combining_form(pinyin_str)
        unaccented = ''.join([c for c in combining_form if c not in self.tone_chars])
        if pinyin_str == combining_form:
            return unaccented
        return self.__get_combined_form(unaccented)

    def to_ascii(self, pinyin_str: str) -> str:
        """Returns the pinyin string with all diacritics removed
           (leaving ASCII characters only)
        """
        combining_form = self.__get_combining_form(pinyin_str)
        return ''.join([c for c in combining_form if not unicodedata.combining(c)])
