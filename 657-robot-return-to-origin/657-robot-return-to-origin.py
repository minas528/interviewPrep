class Solution:
    def judgeCircle(self, moves: str) -> bool:
        c = Counter(moves)
        c['U'] = c.get('U', 0)
        c['D'] = c.get('D', 0)
        c['L'] = c.get('L', 0)
        c['R'] = c.get('R', 0)
        return c['U'] == c['D'] and c['L'] == c['R']