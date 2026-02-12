class Solution:
    def removeComments(self, source: list[str]) -> list[str]:
        result = []
        in_block = False
        buffer = ""

        for line in source:
            i = 0
            while i < len(line):
                if not in_block:
                    if i + 1 < len(line) and line[i:i+2] == "/*":
                        in_block = True
                        i += 2
                    elif i + 1 < len(line) and line[i:i+2] == "//":
                        break
                    else:
                        buffer += line[i]
                        i += 1
                else:
                    if i + 1 < len(line) and line[i:i+2] == "*/":
                        in_block = False
                        i += 2
                    else:
                        i += 1

            if not in_block and buffer:
                result.append(buffer)
                buffer = ""

        return result
