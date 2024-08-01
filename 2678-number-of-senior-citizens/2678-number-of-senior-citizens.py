class Solution:
    def countSeniors(self, details: List[str]) -> int:
        passengers = 0
        for detail in details:
            age = int(detail[11:13])

            if age > 60:
                passengers += 1
        
        return passengers