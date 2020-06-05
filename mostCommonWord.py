import collections

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        words = []
        for p in paragraph.lower().splitlines():
            words.extend(p.split(" "))

        for i, word in enumerate(words):
            if word and not word[-1].isalpha():
                words[i] = word[:-1]

        banned = set(banned)
        counter = sorted(collections.Counter(words).items(), key = lambda x: x[1], reverse = True)
        for key, _ in counter:
            if key not in banned:
                return key

banned = ["hit"]
a = Solution()
print a.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", banned)
