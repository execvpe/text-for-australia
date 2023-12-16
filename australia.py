#!/usr/bin/env python3

substitutions = {
              '1': '𐌋', '2': '↊', '3': '↋',
    '4': 'Һ',           '6': '9', '7': '∠',
              '9': '6',

    'a': 'ɐ', 'b': 'q', 'c': 'ɔ', 'd': 'p',
    'e': 'ǝ', 'f': 'ɟ', 'g': 'ᵷ', 'h': 'ɥ',
    'i': 'ᴉ', 'j': 'ſ̣', 'k': 'ʞ', 'l': 'ꞁ',
    'm': 'ɯ', 'n': 'u',           'p': 'd',
    'q': 'b', 'r': 'ɹ',           't': 'ʇ',
    'u': 'n', 'v': 'ʌ', 'w': 'ʍ',
    'y': 'ʎ',

    'A': 'ꓯ', 'B': 'ꓭ', 'C': 'ꓛ', 'D': 'ꓷ',
    'E': 'ꓱ', 'F': 'ꓞ', 'G': 'ꓨ',
              'J': 'ꓩ', 'K': 'ꓘ', 'L': 'ꓶ',
    'M': 'ꟽ', 'N': 'ꓠ',           'P': 'ꓒ',
    'Q': 'Ꝺ', 'R': 'ꓤ',           'T': 'ꓕ',
    'U': 'ꓵ', 'V': 'ꓥ', 'W': 'M',
    'Y': '𑾰',

    'ä': '\u0324ɐ', 'ö': '\u0324o', 'ü': '\u0324n',

    'Ä': '\u0324ꓯ', 'Ö': '\u0324O', 'Ü': '\u0324ꓵ',

    ",": "'", ".": "˙", "(": ")", ")": "(",
    "'": ",", "?": "¿", "!": "¡",
}

def main() -> None:
    string = input()
    rot = "".join(list(map(lambda c: substitutions.get(c, c), string)))
    print(rot[::-1])

if __name__ == "__main__":
    main()
