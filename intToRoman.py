# -*- coding:utf-8 -*-

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        ans = ""
        while num != 0:
            if num >= 1000:
                th = num / 1000
                ans += 'M' * th
                num = num % 1000
            elif num >= 100:
                ha = num / 100
                num = num % 100
                if ha == 9:
                    ans = ans + 'CM'
                elif ha >= 5:
                    ans = ans + 'D' + 'C'*(ha-5)
                elif ha == 4:
                    ans = ans + 'CD'
                else:
                    ans = ans + 'C' * ha 
            elif num >= 10:
                te = num / 10
                num = num % 10
                if te == 9:
                    ans = ans + 'XC'
                elif te >= 5:
                    ans = ans + 'L' + 'X' * (te-5)
                elif te == 4:
                    ans = ans + 'XL'
                else:
                    ans = ans + 'X' * te
            else:
                ge = num
                num = 0
                if ge == 9:
                    ans = ans + 'IX'
                elif ge >= 5:
                    ans = ans + 'V' + 'I' * (ge-5)
                elif ge == 4:
                    ans = ans + 'IV'
                else:
                    ans = ans + 'I' * ge

        return ans

a = Solution()
print a.intToRoman(3)
print a.intToRoman(4)
print a.intToRoman(9)
print a.intToRoman(58)
print a.intToRoman(1994)
