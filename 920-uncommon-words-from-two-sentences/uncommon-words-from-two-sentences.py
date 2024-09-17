class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        count_dict = {}
        for x in s1.split():
            if(x not in count_dict):
                count_dict[x] = 0
            count_dict[x] += 1
        for x in s2.split():
            if(x not in count_dict):
                count_dict[x] = 0
            count_dict[x] += 1
        return [x for x, c in count_dict.items() if c == 1]
        
