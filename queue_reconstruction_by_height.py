class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        if not people or len(people) == 1:
            return people
        ans = []
        pd = {}
        for i, tmp in enumerate(people):
            if tmp[0] in ans:
                pass
            else :
                ans.append(tmp[0])
            if tmp[0] in pd:
                pd[tmp[0]].append(tmp)
            else :
                pd[tmp[0]] = [tmp]
        ans.sort() 
        res = []
        for i in ans[::-1]:
            pd[i].sort()
            for l in pd[i]:
                res.insert(l[1],l)
        return res
