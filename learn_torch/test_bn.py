import torch
from torch import nn
# track_running_stats=False，求当前batch真实平均值和标准差，
# 而不是更新全局平均值和标准差
# affine=False, 只做归一化，不乘以gamma加beta（通过训练才能确定）
# num_feature 为 feature map 的 channel 数目
# eps 设为0，让官方代码和我们自己的代码结果尽量接近
bn = nn.BatchNorm2d(num_features=3, eps=0, affine=False,
track_running_stats=False)
# 乘 10000 为了扩大数值，如果出现不一致。差别更明显
x = torch.rand(10, 3, 5, 5) * 10000
official_bn = bn(x)
# 把 channel 维度单独提出来，而把其他寻要求均值和标准差的维度融合到一起
x1 = x.permute(1, 0, 2, 3).view(3, -1)
mu = x1.mean(dim=1).view(1, 3, 1, 1)

# unbiased=False，求方差时不做无偏估计（除以 N-1 而不是 N），和原始论文一致
# 个人感觉无偏估计仅仅是数学上好看，实际应用中差别不大
std = xq.std(dim=1, ubbiased=False).view(1, 3, 1, 1)
my_bn = (x-mu)/std
diff = (offical_bn - my_bn).sum()
print('diff={}').format(diff)
# 差别E-5级别，可以接受