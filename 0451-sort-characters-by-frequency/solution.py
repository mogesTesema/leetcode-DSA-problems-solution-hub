class Solution:
    def frequencySort(self, s: str) -> str:
        str_frq = defaultdict()
        for char in s:
            str_frq[char] = str_frq.get(char,0) + 1
        # print(str_frq)

        str_frq = [[frq, char] for char, frq in str_frq.items()]
        str_frq.sort(reverse=True)
        answer = ""
        for frq, char in str_frq:
            answer += char*frq
        # print(answer)
        return answer
