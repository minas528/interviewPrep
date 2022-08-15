class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        x=0
        for i in s:
            x+=roman_dict[i]
        if 'IV' in s or 'IX' in s:
            x-=2
        if 'XL' in s or 'XC' in s:
            x-=20
        if 'CD' in s or 'CM' in s:
            x-=200
        return x