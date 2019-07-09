def combine_chars_in_pair(pair: tuple) -> str:
    return pair[0] + pair[1]

def get_num_uniq_filter(pattern: str):
    def check_if_same_uniq_chars_as_pattern(word: str) -> bool:
        return len(set(pattern)) == len(set(word))
    return check_if_same_uniq_chars_as_pattern

def get_pattern_filter(pattern: str):
    def check_if_replace_possible_w_pattern(word: str) -> bool:
        pattern_array = list(pattern)
        word_array = list(word)
        uniq_in_pattern = len(set(pattern_array))
        combined_array_pairs = zip(pattern_array, word_array)
        uniq_strs = len(set(list([combine_chars_in_pair(pair) for pair in combined_array_pairs])))
        return uniq_in_pattern == uniq_strs
    return check_if_replace_possible_w_pattern

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        uniq_func = get_num_uniq_filter(pattern)
        same_uniq_num_words = filter(uniq_func, words)
        pattern_func = get_pattern_filter(pattern)
        res = filter(pattern_func, same_uniq_num_words)
        return list(res)
        
        # then check if replacing the letters end up with the same word
