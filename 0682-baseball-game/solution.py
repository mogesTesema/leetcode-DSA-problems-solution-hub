class Solution:
    def calPoints(self, operations: List[str]) -> int:
        records = []
        for oper in operations:
            if oper == "+":
                new_record = records[-1] + records[-2]
                records.append(new_record)
            elif oper == "D":
                doubled_record = records[-1] * 2
                records.append(doubled_record)
            elif oper == "C":
                records.pop()
            else:
                records.append(int(oper))
        return sum(records)
        
