count = 0
output = 0

# Assuming these ranges in brute force approach
for xpos in range(300):
    for ypos in range(-600, 1000):
        ok = False
        highest = 0
        x = 0
        y = 0
        dx = xpos
        dy = ypos
        for t in range(1000):
            x += dx
            y += dy
            highest = max(highest, y)
            if dx > 0:
                dx -= 1
            elif dx < 0:
                dx += 1
            dy -= 1
            # Input
            if 29<=x<=73 and -248<=y<=-194:
                ok = True
        if ok:
            count += 1
            if highest > output:
                output = highest
                print(xpos,ypos,output)
print(output)
print(count)