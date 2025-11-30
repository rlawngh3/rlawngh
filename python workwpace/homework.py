x = int(input())

line = 1
while x > line:
    x -= line
    line += 1

top, bottom = (x, line - x + 1) if line % 2 == 0 else (line - x + 1, x)

print(f"{top}/{bottom}")
