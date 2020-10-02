'''
    https://leetcode.com/contest/weekly-contest-184/problems/html-entity-parser/
    1410. HTML Entity Parser
'''


class Solution:
    def entityParser(self, text: str) -> str:
        dur = {
            '&quot;' :'"',
            '&apos;' : "'",
            '&amp;' : '&',
            '&gt;' : '>',
            '&lt;' : '<',
            '&frasl;' : '/'                        
        }
        temp = ''
        res = ''
        flag = False
        for char in text:
            
            if char == '&':
                temp+=char
                flag = True
            elif char ==';' and flag:
                temp+=char
                flag = False
                # print(temp)
                if temp in dur:
                    # print('here')
                    res+= dur[temp]
                else:
                    res+=temp
                temp =''
            elif flag:
                temp += char
            elif not flag:
                res+=char
        return res
                