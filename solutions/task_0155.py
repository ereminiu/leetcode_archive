class MinStack:

    def __init__(self):
        self.st = []

    def push(self, val: int) -> None:
        mn = min(self.st[-1][1], val) if len(self.st) else val
        self.st.append((val, mn))

    def pop(self) -> None:
        self.st.pop()

    def top(self) -> int:
        return self.st[-1][0]

    def getMin(self) -> int:
        return self.st[-1][1]