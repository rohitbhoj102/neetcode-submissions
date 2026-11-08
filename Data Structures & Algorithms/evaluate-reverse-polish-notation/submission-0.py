class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Algortihm / Data Structure: Stack LIFO evaluation
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b/a)) # truncate towards zero
            else:
                stack.append(int(c))

        return stack[0]