from collections import deque

deq = deque("abcdefg")

#you can add to both side
deq.append('ADDED TO END')
deq.appendleft('ADDED TO START')

print(deq)

#you can remove from both end
deq.pop()
deq.popleft()

print(deq)

#negative for left, positive for right
deq.rotate(3)
deq.rotate(-6)

print(deq)