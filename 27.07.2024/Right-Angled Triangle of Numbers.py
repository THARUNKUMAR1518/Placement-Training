def right_angled_triangle_numbers(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end="")
        print()

right_angled_triangle_numbers(5)
