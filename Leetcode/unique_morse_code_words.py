import string

def construct_morse_table() -> dict:
    morse_in_alpha = [
        ".-",
        "-...",
        "-.-.",
        "-..",
        ".",
        "..-.",
        "--.",
        "....",
        "..",
        ".---",
        "-.-",
        ".-..",
        "--",
        "-.",
        "---",
        ".--.",
        "--.-",
        ".-.",
        "...",
        "-",
        "..-",
        "...-",
        ".--",
        "-..-",
        "-.--",
        "--.."
    ]
    alphabet = list(string.ascii_lowercase[:])
    return dict(zip(alphabet, morse_in_alpha))

def convert_char_to_morse(char: str) -> str:
    return morse_table[char]

def convert_word_to_morse(word: str) -> str:
    broken_up_morse = [ convert_char_to_morse(character) for character in word ]
    put_together_morse = ''.join(broken_up_morse)
    return put_together_morse

morse_table = construct_morse_table()

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_combos = [ convert_word_to_morse(word) for word in words]
        uniq_morse_combos = set(list(dict.fromkeys(morse_combos)))
        return len(uniq_morse_combos)
