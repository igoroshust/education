n = int(input())
k = int(input())

circle = list(range(1, n + 1))
index = 0

while len(circle) > 1:
    index = (index + k - 1) % len(circle)
    circle.pop(index)
    
print(circle[0])