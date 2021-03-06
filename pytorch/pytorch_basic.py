import torch
import torchvision
import torch.nn as nn
import numpy as np

import torchvision.transforms as transforms

x = torch.tensor(1.0, requires_grad=True)

w = torch.tensor(2.0, requires_grad=True)

b = torch.tensor(3.0, requires_grad=True)

y = w * x + b

y.backward()

print(x.grad)
print(w.grad)
print(b.grad)

x = torch.randn(10, 3)
y = torch.randn(10, 2)

linear = nn.Linear(3, 2)
print('w:', linear.weight)
print('b:', linear.bias)

criterion = nn.MSELoss()
optimizer = torch.optim.SGD(linear.parameters(), lr=0.01)

pred = linear(x)

loss = criterion(pred, y)
print('loss:', loss.item())

loss.backward()

print('dL/dw:', linear.weight.grad)
print('dL/db', linear.bias.grad)

optimizer.step()

pred = linear(x)
loss = criterion(pred, y)
print('loss after 1 step optimization', loss.item())


