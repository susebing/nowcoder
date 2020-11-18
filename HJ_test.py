"""
title:华为机试
url  :https://www.nowcoder.com/ta/huawei
"""


def test1():
    """
    计算字符串最后一个单词的长度，单词以空格隔开。
    :return:
    """
    s = input()
    print(len(s.split()[-1]))


def test2():
    """
    写出一个程序，接受一个由字母和数字组成的字符串，和一个字符，然后输出输入字符串中含有该字符的个数。不区分大小写。
    :return:
    """
    s1 = input()
    s2 = input()
    print(s1.lower().count(s2.lower()))


def test3():
    """
    明明想在学校中请一些同学一起做一项问卷调查，为了实验的客观性，他先用计算机生成了N个1到1000之间的随机整数（N≤1000），
    对于其中重复的数字，只保留一个，把其余相同的数去掉，不同的数对应着不同的学生的学号。
    然后再把这些数从小到大排序，按照排好的顺序去找同学做调查。
    请你协助明明完成“去重”与“排序”的工作(同一个测试用例里可能会有多组数据，希望大家能正确处理)。

    注：测试用例保证输入参数的正确性，答题者无需验证。测试用例不止一组。
    当没有新的输入时，说明输入结束。

    注意：输入可能有多组数据。每组数据都包括多行，第一行先输入随机整数的个数N，接下来的N行再输入相应个数的整数。
    具体格式请看下面的"示例"。
    :return:
    """
    while True:
        try:
            N = int(input())
            res = set()
            for i in range(N):
                res.add(int(input()))
            for item in sorted(list(res)):
                print(item)
        except:
            break


def test4():
    """
    •连续输入字符串，请按长度为8拆分每个字符串后输出到新的字符串数组；
    •长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。
    :return:
    """
    while True:
        try:
            s = input()
            while s:
                if len(s) > 8:
                    print(s[:8])
                    s = s[8:]
                else:
                    print(s + '0' * (8 - len(s)))
                    break
        except:
            break


def test5():
    """
    写出一个程序，接受一个十六进制的数，输出该数值的十进制表示。
    :return:
    """
    while True:
        try:
            print(int(input(), 16))
        except Exception as e:
            break


def test6():
    """
    功能:输入一个正整数，按照从小到大的顺序输出它的所有质因子（重复的也要列举）（如180的质因子为2 2 3 3 5 ）
    最后一个数后面也要有空格
    :return:
    """
    n = int(input())
    while True:
        for i in range(2, n):
            if n % i == 0:
                print(i, end=' ')
                n = n // i
                break
        else:
            print(n, end=' ')
            break


def test7():
    """
    写出一个程序，接受一个正浮点数值，输出该数值的近似整数值。如果小数点后数值大于等于5,向上取整；小于5，则向下取整。
    :return:
    """
    while True:
        try:
            print(int(float(input()) + 0.5))
        except:
            break


def test8():
    """
    数据表记录包含表索引和数值（int范围的整数），请对表索引相同的记录进行合并，即将相同索引的数值进行求和运算，输出按照key值升序进行输出。
    :return:
    """
    
    
    pass


if __name__ == '__main__':
    test8()
