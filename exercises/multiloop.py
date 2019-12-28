if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = str(input())
        count = 0
        odd_char = ""
        even_char = ""
        for j in s:
            if 0 <= count % 2 == 0:
                even_char += j
            else:
                odd_char += j
            count += 1
        print('{0} {1}'.format(even_char, odd_char))
