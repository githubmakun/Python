# 有一个阶梯，若每步上两阶，最后剩一阶，若每步上三阶，最后剩两阶，
# 若每步上四阶，最后剩三阶，若每步上五阶，最后剩四阶，若每步上六阶，最后剩五阶，若每步上七阶，则一阶不剩

x = 0
while x < 1000:
    if (x%2 == 1) and (x%3 == 2) and (x%4 == 3) and (x%5 == 4) and (x%6 == 5) and (x%7 == 0):
        print(x)
        x += 1
        # break
    else:
        x += 1
print("循环结束")