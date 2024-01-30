"""
Find Words That Can be Formed By Characters

You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.

"""
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        good_strings = []
        res = 0

        def is_good_string(vocab, word): 
            for letter in word: 
                vocab[letter] = vocab.get(letter, 0) - 1
                if vocab[letter] < 0: 
                    return False 
            return True 

        d = {}
        for char in chars: 
            d[char] = d.get(char, 0) + 1

        for word in words: 
            d_copy = d.copy()
            if is_good_string(d_copy, word): 
                res += len(word)

        return res