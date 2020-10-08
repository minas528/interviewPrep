'''
    https://docs.google.com/spreadsheets/d/1V_s6TlAPXPRTRdWMz3t4YeyEmHQYThtYJFYZkVIqV0E/edit?ts=5f53ff6b#gid=61778487
    299. Bulls and Cows

    You are playing the Bulls and Cows game with your friend.

    You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess, you provide a hint with the following info:

    The number of "bulls", which are digits in the guess that are in the correct position.
    The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position. Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.
    Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.

    The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. Note that both secret and guess may contain duplicate digits.

    

    Example 1:

    Input: secret = "1807", guess = "7810"
    Output: "1A3B"
    Explanation: Bulls are connected with a '|' and cows are underlined:
    "1807"
    |
    "7810"
'''

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls, cows = 0,0
        sec , gue = {},{}
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls+=1
            else:
                if secret[i] in sec:
                    sec[secret[i]]+=1
                else:
                    sec[secret[i]]=1
                if guess[i] in gue:
                    gue[guess[i]] +=1
                else:
                    gue[guess[i]] =1
        # print(sec,gue)
        for i in set(sec.keys()&gue.keys()):
            cows+=min(sec[i],gue[i])
        return f'{bulls}A{cows}B'