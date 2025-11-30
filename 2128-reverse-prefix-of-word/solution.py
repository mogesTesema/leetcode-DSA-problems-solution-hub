class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        stack = []
        answer = ""
        for index,elem in enumerate(word):
            if elem == ch:
                answer += elem
                while stack:
                    answer += stack.pop()
                break
            else:
                stack.append(elem)
        if not stack:
            answer += word[index+1:]
        else:
            answer = word
        return answer

        
