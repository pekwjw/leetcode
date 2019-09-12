# -*- coding:utf-8 -*-
import time
import sys
class Solution(object):
    def ambiguousCoordinates(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        s = S[1:-1]
        if len(s) <= 1:
            return []
        ans = []
        for i in range(1,len(s)):
            left,right = s[:i],s[i:]
            l = self.add_dot(left)
            r = self.add_dot(right)
            for _,tl in enumerate(l):
                for _,tr in enumerate(r):
                    result = "(%s, %s)" % (tl,tr)
                    ans.append(result)
        return ans

    def add_dot(self,s):
        if s == '0':
            return ['0']
        if s[0] == '0' and s[-1] == '0':
            return []
        if s[0] == '0' and s[-1] != '0':
            return ['0.' + s[1:]]
        if (s[0] != '0' and s[-1] == '0'):
            return [s]
        if len(s) == 1:
            return [s] 
        ans = []
        for i in range(1,len(s)):
            ans.append(s[:i] + '.' + s[i:])
        ans.append(s)
        return ans
    
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        start = time.time()
        ans = []
        dic = {word:i for i,word in enumerate(words)} 
        for cur,word in enumerate(words):
            for i in range(len(word)+1):
                left,right = word[:i],word[i:]
                if left[::-1] in dic and right == right[::-1] and cur != dic[left[::-1]]:
                    ans.append([cur,dic[left[::-1]]])
                if i!=0 and right[::-1] in dic and left == left[::-1] and cur != dic[right[::-1]]:
                    ans.append([dic[right[::-1]],cur])
        print time.time()-start
        return ans

    def palind(self,words):
        start = time.time()
        ans = []
        length = len(words)
        for i in range(0,len(words)-1):
            for j in range(i+1,len(words)):
                shun = words[i]+words[j]
                ni = words[j]+words[i]
                if shun == shun[::-1]:
                    ans.append([i,j])
                if ni == ni[::-1]:
                    ans.append([j,i]) 
        print time.time()- start
        return ans

a = Solution()
#s = sys.argv[1]
#a.ambiguousCoordinates(s)
s =  ["abcd", "dcba", "lls", "s", "sssll"]
print a.palindromePairs(s)
print a.palind(s)
