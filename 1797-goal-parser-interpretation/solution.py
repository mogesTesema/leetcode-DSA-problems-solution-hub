class Solution:
    def interpret(self, command: str) -> str:
        left =0
        right=0
        result =""
        while(right<len(command)):
            if command[right] =="G":
                result+=("G")
                right +=1
            else:
                 if command[right] == "(":
                    left = right
                    while(command[right]!=")"):
                        right +=1
                    if right-left >1:
                        result+=("al")
                    else:
                        result+=("o")
                    right +=1
                
           
        return result

            
