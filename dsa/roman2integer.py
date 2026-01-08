"""
Date: Jan 8, 2026
Problem: https://leetcode.com/problems/roman-to-integer/
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        data_dic={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000,
            'IV':4,
            'IX':9,
            'XL':40,
            'XC':90,
            'CD':400,
            'CM':900
        }
        if s in data_dic:
            return data_dic[s]
        total=0
        i=0

        for i,v in enumerate(s):
            if i+1<len(s) and s[i:i+2] in data_dic:
                val=s[i:i+2]
                total=total+data_dic[val]
                i=i+1
            elif v in data_dic and i==0:
                total=total+data_dic[v]
            elif v in data_dic and (i!=0 and s[i-1:i+1] not in data_dic):
                total=total+data_dic[v]
            else:
                continue
        return total

romanInteger=Solution()
#print(romanInteger.romanToInt("I"))
#print(romanInteger.romanToInt("IV"))
#print(romanInteger.romanToInt("XVII"))
print(romanInteger.romanToInt("MCMXCIV"))
#print(romanInteger.romanToInt("LVIII"))
#1994 M = 1000, CM = 900, XC = 90 and IV = 4.
