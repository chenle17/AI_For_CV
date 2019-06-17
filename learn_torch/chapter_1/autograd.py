import torch
from torch.autograd import Variable

def tensor_gradient():
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
    print('----------out-0-------')
    print(out)
    print(out.requires_grad) # True

    print(r'-----------.requires_grad_(...)  改变属性')
    a = torch.randn(2, 2)
    print(a)
    print(a.requires_grad)
    a = ((a * 3) / (a - 1))
    print(a)
    print(a.requires_grad)
    print(a.grad_fn)
    a.requires_grad_(True)
    print(a)
    print(a.requires_grad)
    print(a.grad_fn)
    b = (a * a).sum()
    print(b)
    print(b.requires_grad)
    print(b.grad_fn)

    print('------------------------------------x grad')

    print(out.backward)
    print(x.grad)

def tensor_gradient_2():
    x = Variable(torch.tensor([[2., 5.]]), requires_grad=True)
    print(x)
    y = torch.zeros(1, 2)
    y[0, 0] = x[0, 0] * 2 + x[0, 1]
    y[0, 1] = x[0, 1] * 3 + x[0, 0]
    print(y)
    # while y.data.norm() < 1000:
    #     y = y * 2

    print(y.requires_grad)

    # gradients = torch.tensor([0.1, 1.0, 0.0001], dtype=torch.float)
    # y.backward(gradients)
    # print(x.grad)

    gradients = torch.ones(1, 2)
    print(gradients)
    y.backward(gradients)
    print(x.grad)


    print(x.requires_grad)
    print((x ** 2).requires_grad)

    with torch.no_grad():
        print((x ** 2).requires_grad)
        print(x.requires_grad)



if __name__ == '__main__':
    # print('-----------------------------------tensor_grad---------')
    # tensor_gradient()

    print('-----------------------------------tensor_grad_2---------')
    tensor_gradient_2()

