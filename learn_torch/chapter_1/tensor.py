import torch
import numpy as np

def gpu_cuda():
    print(torch.__version__)
    print(torch.cuda.device_count())
    print(torch.cuda.current_device())
    if torch.cuda.is_available():
        device = torch.device('cuda')
        # device = torch.device('cuda:0')
        # device = torch.device('cuda', 0)
        # device_1 = torch.device('cuda', 1)
        a = torch.empty(4,6)
        print(a)
        b = torch.ones_like(a, device=device)
        print(b)
        c = a.to(device)
        print(c)

        print('------------')
        torch.add(a, 1, out=a)
        print(a)
        print(b)
        print(c)

        print(torch.add(a, b))
        # 报错
        # RuntimeError: expected type torch.FloatTensor
        # but got torch.cuda.FloatTensor



def tensor():
    matrix_empty = torch.empty(5, 3)
    print(type(matrix_empty))
    print(matrix_empty)

    matrix_rand = torch.rand(3, 4, dtype=torch.double)
    print(matrix_rand)

    matrix_np = np.arange(0, 12).reshape((3, 4))
    print(matrix_np)

    matrix_zero = torch.zeros(2, 4, dtype=torch.long)
    print(matrix_zero)

    matrix_tensor = torch.tensor([5.5, 3], dtype=torch.long)
    print(matrix_tensor)

    numpy_tensor = torch.tensor(matrix_np, dtype=torch.double)
    print(numpy_tensor)

    new_rensor = matrix_tensor.new_ones(3,2)
    print(new_rensor)
    print(new_rensor.size())
    print(matrix_tensor)

    print('---------')

    print(matrix_rand + numpy_tensor)
    print(torch.add(matrix_rand, numpy_tensor))

    result = torch.rand(matrix_rand.size())
    print(result)
    result = torch.randn(matrix_rand.size(), dtype=torch.double)
    print(result)
    torch.add(matrix_rand, numpy_tensor, out=result)
    print(result)

    print('---')
    print(result.add_(matrix_rand))
    print(result)

    print('##########')

    print(result.view(6, 2))# numpy reshape
    print(result)
    print(result.view(-1, 3))  # numpy reshape
    print(result)

    x = torch.tensor([3.67])
    print(x)
    print(x.item())

    print('---------trans')
    a = result.numpy()# a 和 result共享内存
    print(type(a))
    print(a)
    print(result)

    result.add_(1)
    print(a)
    print(result)

    np.add(a, 1, out=a)
    print(a)
    print(result)

    result.add_(2)
    print(a)
    print(result)

    print()
    print('-------------trans_2')
    ones_np = np.ones((2,4))
    ones = torch.from_numpy(ones_np)
    print(ones_np.shape)
    print(ones_np)
    print(ones)

    np.add(ones_np, 1, out=ones_np)
    print(ones_np)
    print(ones)

    torch.add(ones, 2, out=ones)
    print(ones_np)
    print(ones)

if __name__ == '__main__':
    # print("---------tensor----------")
    # tensor()
    #
    print('---------gpu_cuda-----------')
    gpu_cuda()