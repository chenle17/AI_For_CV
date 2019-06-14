import torch

def tensor():
    # requires_grad 为True追踪所有对于该张量的操作
    x = torch.ones(2, 2,requires_grad=True)
    print(x)
    print(x.grad_fn)

    y = x + 2
    print(y)
    # 结果y已经被计算出来了，所以，grad_fn已经被自动生成了。
    print(y.grad_fn)# AddBackward0
    print(y.requires_grad)

    z = y * y * 3
    print(z)# MulBackward0
    out = z.mean() # MeanBackward1
    print(out)
    print(out.requires_grad) # True

    print(r'-----------.requires_grad_(...)  改变属性')
    a = torch.randn(2, 2)
    print(a)
    print(a.requires_grad)
    a = ((a * 3) / (a - 1))
    print(a)
    print(a.requires_grad)
    a.requires_grad_(True)
    print(a.requires_grad)
    print(a.grad_fn)
    b = (a * a).sum()
    print(b)
    print(b.requires_grad)
    print(b.grad_fn)

if __name__ == '__main__':
    print('-----------------------------------tensor---------')
    tensor()
