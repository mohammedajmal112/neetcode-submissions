class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs.sort(key=lambda x: len(x))
        grouped_words = {}
        for i in range(len(strs)):
            temp = list(strs[i])
            temp.sort()
            temp1 = "".join(temp)
            if temp1 not in grouped_words:
                grouped_words[temp1] = []
            grouped_words[temp1].append(strs[i])
        t = list(grouped_words.values())
        t.sort(key=lambda x: len(x))
        return t
