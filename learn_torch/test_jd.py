import sys

def kill_matrix(matrix):
    result_num = len(matrix[0]) ** 2
    max_block = find_maxnum(matrix)

    if not max_block:
        return result_num
    else:
        matrix, result_num = kill_num(matrix)
        matrix = drop_matrix(matrix)
        return kill_matrix(matrix)

def find_maxnum(matrix):
    length = len(matrix[0])
    num_dict = {1:[], 2:[], 3:[], 4:[]}
    visited = set()

    for i in range(1,5):
        for m in range(length):
            for n in range(length):
                if matrix[m][n] == i and [m,n] not in visited:
                    num_dict[i].append([[m,n], 1])
                    visited, num_dict = find_onenum(matrix, m, n, 0, visited, num_dict)

    maxblock = [0]
    for numinfo in num_dict:
        num, pathes = numinfo

        for path in pathes:
            if path[-1] > maxblock[-1]:
                maxblock = path

    if maxblock[-1] > 2:
        return maxblock
    return None


def find_onenum(matrix, m, n, num, visited, num_dict):
    for run in [[-1,0],[1,0],[0,1],[0,-1]]:
        x, y = run
        if matrix[m][n] == matrix[m+x][n+y]:
            visited.add([m+x][n+y])
            num_dict[matrix[m][n]][-1] += 1
            visited, num_dict = find_onenum(matrix,m+x,n+y,num+1,visited,num_dict)

    return visited, num_dict

def kill_num(matrix):
    # TODO
    return matrix

def drop_matrix(matrix):
    # TODO
    return matrix




    # dp = [[0] * (length + 2) for _ in range(length + 2) ]
    #
    # for i in range(1, length + 1):
    #     for j in range(1, length + 1):
    #         center = matrix[i-1][j-1]
    #         up = matrix[i-2][j-1]
    #         left = matrix[i-1][j-2]
    #
    #         if center == up :
    #             dp[i][j] = dp[i-1][j] + 1
    #             if dp[i][j] > maxnum_num:
    #                 maxnum_num = dp[i][j]
    #                 maxnum = center
    #         if center == left:
    #             dp[i][j] = dp[i][j-1] + 1
    #             if dp[i][j] > maxnum_num:
    #                 maxnum_num = dp[i][j]
    #                 maxnum = center
    #
    #     for j in range(1, length + 1, -1):
    #
    #
    #         if center == up:
    #             dp[i][j] = dp[i - 1][j] + 1
    #             if dp[i][j] > maxnum_num:
    #                 maxnum_num = dp[i][j]
    #                 maxnum = center
    #         if center == left:
    #             dp[i][j] = dp[i][j - 1] + 1
    #             if dp[i][j] > maxnum_num:
    #                 maxnum_num = dp[i][j]
    #                 maxnum = center





while True:
    input_array = input()
    if input_array:
        sub_list = list(map(int, input_array.split()))
        matrix = [sub_list]
        for i in range(len(sub_list)):
            matrix.append(list(map(int, input().split())))

        result_num = kill_matrix(matrix)

# while True:
#     input_array = input()
#     if not input_array:
#         break
#     n, m = list(map(int, input_array.split()))
#
#     result = n
#     for _ in range(1, m):
#         n = n ** 0.5
#         result += n
#
#     sys.stdout.write('%.2f' %result )

    # '%.2f %03d' %(1213.2345, 3)
    # print(obj)实质就是调用sys.stdout.write(obj+’\n’)

    # 1. round()
    # 这个不说了，前面已经讲过了。一定要注意它不是简单的四舍五入，而是ROUND_HALF_EVEN的策略。
    #
    # 2. math模块的ceil(x)
    # 取大于或者等于x的最小整数。
    #
    # 3. math模块的floor(x)
    # 去小于或者等于x的最大整数。
    #print "round(80.23456, 2) : ", round(80.23456, 2)
# print "round(100.000056, 3) : ", round(100.000056, 3)
# print "round(-100.000056, 3) : ", round(-100.000056, 3)

# round(80.23456, 2) :  80.23
# round(100.000056, 3) :  100.0
# round(-100.000056, 3) :  -100.0