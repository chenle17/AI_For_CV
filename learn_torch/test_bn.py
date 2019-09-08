# import torch
# from torch import nn
# # track_running_stats=False，求当前batch真实平均值和标准差，
# # 而不是更新全局平均值和标准差
# # affine=False, 只做归一化，不乘以gamma加beta（通过训练才能确定）
# # num_feature 为 feature map 的 channel 数目
# # eps 设为0，让官方代码和我们自己的代码结果尽量接近
# bn = nn.BatchNorm2d(num_features=3, eps=0, affine=False,
# track_running_stats=False)
# # 乘 10000 为了扩大数值，如果出现不一致。差别更明显
# x = torch.rand(10, 3, 5, 5) * 10000
# official_bn = bn(x)
# # 把 channel 维度单独提出来，而把其他寻要求均值和标准差的维度融合到一起
# x1 = x.permute(1, 0, 2, 3).view(3, -1)
# mu = x1.mean(dim=1).view(1, 3, 1, 1)
#
# # unbiased=False，求方差时不做无偏估计（除以 N-1 而不是 N），和原始论文一致
# # 个人感觉无偏估计仅仅是数学上好看，实际应用中差别不大
# std = xq.std(dim=1, ubbiased=False).view(1, 3, 1, 1)
# my_bn = (x-mu)/std
# diff = (offical_bn - my_bn).sum()
# print('diff={}').format(diff)
# # 差别E-5级别，可以接受

import sys

# def change_nums(N, K, nums, num):
#     if K == 0:
#         return num
#
#     start, end, = 0, 1
#     while start < end and end < N:
#         while nums[start] % 3 == 0 and end < N:
#             start += 1
#             end += 1
#
#         while end < N:
#             while nums[end] % 3 == 0 and end < N:
#                 end += 1
#
#         if (nums[start] + nums[end]) % 3 == 0:
#             del nums[start]
#             del nums[end]
#             nums.append(nums[start] + nums[start])
#             return change_nums(N,K-1,nums, num+1)
#         else:
#             start += 1
#             end += 1
#
#     return num
#
#
#
# if __name__ == "__main__":
#     # 读取第一行的n
#     N,K = int(sys.stdin.readline().strip())
#     nums = list(map(int, sys.stdin.readline().strip()))
#
#     num = 0
#     for i in nums:
#         if num % 3 == 0:
#             num += 1
#
#     change_nums(N, K, nums, num)
#
# #
def run(N,M,S,D,Qi,sub_path):
    cities = {i+1:[] for i in range(N)}
    time = {}

    for path in sub_path:
        cities[path[0]].append(path[1])
        time[str(path[0])+str(path[1])] = path[2]

    min_time = float('inf')
    now_time = 0
    num = Qi[S-1]
    max_num = 0
    min_time, max_num =find_path(min_time, now_time, num,max_num, cities, time, S, D)
    print(str(min_time)+ " " + str(max_num))


def find_path(min_time, now_time, num,max_num, cities, time, S, D):
    if S == D:
        return min_time, max_num

    for i in cities[S]:
        now_time += time[str(S)+str(i)]

        # for j in range(S, i):
        num += Qi[i-1]

        if i == D and now_time < min_time:
            min_time = now_time
            max_num = num
        elif i == D and now_time == min_time and num > max_num:
            min_time = now_time
            max_num = num

        min_time, max_num = find_path(min_time, now_time, num, max_num, cities, time, i, D)

        now_time -= time[str(S) + str(i)]
        num -= Qi[i-1]


        # find_path(min_time, now_time, num, path, cities, time, S, D, now_s)
        # now_time -= time[str(S) + str(i)]

    return min_time, max_num

# 4 5 1 4
# 10 20 30 40
# 1 2 2
# 1 3 3
# 2 3 2
# 3 4 3
# 2 4 4


if __name__ == "__main__":
    # 读取第一行的n
    N, M, S, D = 4, 5, 1, 4
    Qi = [10, 20, 30, 40]
    sub_path = [[1, 2, 2]
,[1, 3, 3]
,[2, 3 ,2],
[3 ,4 ,3],
[2, 4, 4]]


    # N,M,S,D= list(map(int(sys.stdin.readline().strip().split())))
    # Qi = list(map(int, sys.stdin.readline().strip().split()))
    # sub_path = []
    # for _ in range(M):
    #     sub_path.append(list(map(int, sys.stdin.readline().strip().split())))

    run(N,M,S,D,Qi,sub_path)

#
# def sum_money(n, A, B, l_a, l_b):
#     start = 0
#     result = 0
#
#     for i in range(l_b):
#         if B[i] == 0:
#             continue
#         for j in range(start, i+1):
#             while A[j] != 0 and B[i] != 0:
#                 result += i - j
#                 A[j] -= 1
#                 B[i] -= 1
#             if B[i] == 0:
#                 break
#             if A[j] == 0:
#                 start += 1
#                 continue
#         if start == l_a:
#             break
#     print(result)
#
#
#
#
# if __name__ == "__main__":
#     # 读取第一行的n
#     # n = int(sys.stdin.readline().strip())
#     # A = list(map(int, sys.stdin.readline().strip()))
#     # B = list(map(int, sys.stdin.readline().strip()))
#     n = 0
#     A = [1, 2, 0]
#     B = [0, 0, 3]
#
#
#     l_a = len(A)
#     l_b = len(B)
#     if l_a == l_b:
#         sum_money(n, A, B, l_a, l_b)
