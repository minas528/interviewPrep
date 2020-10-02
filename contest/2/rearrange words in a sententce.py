'''
    https://leetcode.com/contest/weekly-contest-189/problems/rearrange-words-in-a-sentence/
    1451. Rearrange Words in a Sentence
'''
class Solution:
    def arrangeWords(self, text: str) -> str:
        txt = text.split(' ')
        arr = set()
        for word in txt:
            arr.add(len(word))
        arr = sorted(arr)
        print(arr)
        sol = []
        for length in arr:
            for h  in txt:
                if len(h) == length:
                    sol.append(h.lower())
        mels = ' '.join(sol)
        mels.upper()
        return mels.capitalize()
                    