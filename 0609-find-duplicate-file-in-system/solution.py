class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        
        def parse_content(path):
            splited_path = path.split(" ")
            root = splited_path[0]
            file_content = []

            for file in splited_path[1:]:
                file,content = file.split('(')
                file_content.append([content[:-1],file])
            
            return root,file_content






        duplicate = {}

        def add_to_duplicate(path):
           
            root,file_content = parse_content(path)

            for content,file in file_content:
                if content in duplicate:
                    duplicate[content].append(root+"/"+file)
                else:
                    duplicate[content] = [root+"/"+file]
        

        for path in paths:
            add_to_duplicate(path)
        
        final_ans = []
        for val in duplicate.values():
            if len(val) > 1:
                final_ans.append(val)
        
        return final_ans

            
