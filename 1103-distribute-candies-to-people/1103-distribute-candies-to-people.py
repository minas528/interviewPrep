class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        round = 0
        n = num_people
        last_round_sum = (1 + n) * n // 2
        while candies - last_round_sum > 0:
            candies -= last_round_sum
            last_round_sum += n * n
            round += 1

        res = [0] * n
        for i in range(1, n + 1):
            res[i - 1] = (i + i + (round - 1) * n) * round // 2
			
            if candies - (i + n * round) > 0:
                res[i - 1] += i + n * round
                candies -= i + n * round
            else:
                res[i - 1] += candies
                candies = 0
        return res