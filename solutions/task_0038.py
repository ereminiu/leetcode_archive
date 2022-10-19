class Solution:
    def countAndSay(self, n: int) -> str:
        state = '1'
        for rep in range(n-1):
            prev, cnt = state[0], 1
            new_state = ''
            for i in range(1, len(state)):
                if state[i] == prev:
                    cnt += 1
                else:
                    new_state += repr(cnt) + prev
                    prev, cnt = state[i], 1
            new_state += repr(cnt) + prev
            # print(new_state)
            state = new_state
        
        return state