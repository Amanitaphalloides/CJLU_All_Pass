def zf(inlist):
    for i in inlist:
        result = (sum(i) - max(i) - min(i))/4
        print("{:.1f}".format(result))


input_list = [[7, 8, 7.5, 8.3, 8.2, 7.8],
              [8, 8.3, 8.5, 8.8, 8.2, 7.8],
              [9, 8, 7.5, 8.3, 8.2, 8.8],
              [6, 7, 7.5, 7.3, 7.2, 7.8],
              [8, 9, 9, 8.8, 9, 10]]

zf(input_list)
