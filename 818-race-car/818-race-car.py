class Solution:
    def racecar(self, target: int) -> int:
        q = collections.deque([(0, 0, 1)]) # move, pos, vel
        while q:
            move, pos, vel = q.popleft()
            if pos == target:
                return move            
            # A
            q.append((move+1, pos+vel, vel*2))           
            # R, considered in 4 cases, get rid of excessive search
            if (pos > target and vel > 0) or (pos < target and vel < 0) or (pos + vel > target and vel > 0) or (pos + vel < target and vel < 0):  #reverse
                q.append((move+1, pos, -1 if vel > 0 else 1))