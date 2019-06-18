import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        # 1 input image channel, 6 output channels, 5x5 square convolution
        # kernel
        self.conv1 = nn.Conv2d(1, 6, 5)
        self.conv2 = nn.Conv2d(6, 16, 5)
        # an affine operation: y = Wx + b
        self.fc1 = nn.Linear(16 * 5 * 5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        print('input size:', x.size()) # [1, 1, 32, 32]
        # Max pooling over a (2, 2) window 无padding
        x = F.max_pool2d(F.relu(self.conv1(x)), (2, 2))
        print('pool1 size:', x.size()) # [1, 6, 14, 14]
        # If the size is a square you can only specify a single number
        x = F.max_pool2d(F.relu(self.conv2(x)), 2)
        print('pool2 size: ', x.size()) # [1, 16, 5, 5]
        x = x.view(-1, self.num_flat_features(x))
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

    def num_flat_features(self, x):
        print('size: ', x.size())# all dimensions except the batch dimension
        size = x.size()[1:]
        num_features = 1
        for s in size:
            num_features *= s

        print('num features: ', num_features)
        return num_features

if __name__ == '__main__':
    net = Net()
    print(net)

    params = list(net.parameters())# 可被学习参数（权重）列表和值
    print(len(params))
    print(params[0].size()) # conv1's .weight ##torch.Size([6, 1, 5, 5])
    # print(params[0])

    input = torch.randn(1, 1, 32, 32)
    print(input.size())
    out = net(input)
    print(out)

    net.zero_grad()
    out.backward(torch.randn(1, 10))
    print(out)

    output = net(input)
    target = torch.randn(10)
    target = target.view(1, -1)
    criterion = nn.MSELoss()

    loss = criterion(output, target)
    print(loss)

    print(loss.grad_fn)
    print(loss.grad_fn.next_functions)
    print(loss.grad_fn.next_functions[0][0])
    print(loss.grad_fn.next_functions[0][0].next_functions)
    print(loss.grad_fn.next_functions[0][0].next_functions[0][0])

    # 清除梯度
    net.zero_grad()

    print('conv1.bias.grad before backward')
    print(net.conv1.bias.grad)

    loss.backward()

    print('conv1.bias.grad before backward')
    print(net.conv1.bias.grad)

    # learning_rate = 0.01
    # for f in net.parameters():
    #     f.data.sub_(f.grad.data * learning_rate)

    print('------------update')
    optimizer = optim.SGD(net.parameters(), lr=0.01)

    optimizer.zero_grad()
    output = net(input)
    loss = criterion(output, target)
    loss.backward()
    optimizer.step()



