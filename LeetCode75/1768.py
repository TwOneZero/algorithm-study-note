import itertools as it


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = ""
        zip_str = [x for x in it.chain.from_iterable(it.zip_longest(word1, word2)) if x]
        return output.join(zip_str)
