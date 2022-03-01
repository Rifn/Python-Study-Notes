# 1. 打印 9 行小星星
row = 1

while row <= 9:

    col = 1

    while col <= row:

        # print("*", end="")
        print("%d * %d = %d" % (col, row, col * row), end="\t")  # 这个“\t”是在同一行打印并且
        # 间隔的意思，多加“\t”间距加大
        col += 1

    # print("%d" % row)
    print("")

    row += 1
