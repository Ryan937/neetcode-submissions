class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        if not seats or not students:
            return 0

        seats.sort()
        students.sort()

        result = 0

        for i in range(len(seats)):
            result += abs(seats[i] - students[i])

        return result