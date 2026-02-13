class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        random = set(ransomNote)
        magazine_set = set(magazine)

        sub_set = random.issubset(magazine_set)

        random_count= Counter(ransomNote)
        magazine_count = Counter(magazine)


        for key,val in random_count.items():
            if key not in magazine_count:
                return False
            if val > magazine_count[key]:
                return False

        return sub_set
