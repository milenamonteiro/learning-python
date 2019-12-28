fire = 0
while True:
    for i in range(8):
        mountain_h = int(input())  # represents the height of one mountain.
        if mountain_h > fire:
            fire = mountain_h
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    # The index of the mountain to fire on.
    print(fire)