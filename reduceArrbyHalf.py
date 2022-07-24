class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        nw = Counter(arr)
        kr = list(nw.values())
        kr.sort(reverse = True)
        cnt = 0
        total = 0
        for freq in kr:
            if total < len(arr)//2 :
                total += freq
                cnt +=1   
            else:
                break
        
        return cnt
