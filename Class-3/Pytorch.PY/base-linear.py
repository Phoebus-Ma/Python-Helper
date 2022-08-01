###
# Pytorch Linear regression machine learning example.
#
# License - MIT.
###

# CPU only: [pip3 install torch torchvision torchaudio]
# CPU & GPU:[pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu113]
from turtle import color
import torch
import torch.nn as nn

# pip install matplotlib numpy
import matplotlib.pyplot as plt
import numpy as np


# Neural network class.
class NeuralNetwork(nn.Module):
# {
    def __init__(self):
    # {
        super(NeuralNetwork, self).__init__()
        self.features = nn.Linear(2, 1)
        self.sigmoid = nn.Sigmoid()
    # }

    def forward(self, x):
    # {
        x = self.features(x)
        x = self.sigmoid(x)

        return x
    # }
# }


# Main function.
def main() -> int:
# {
    torch.manual_seed(10)

    # ================== step 1: Generate data. ===========================.
    sample_nums = 100
    mean_value  = 1.7
    bias        = 1
    n_data      = torch.ones(sample_nums, 2)

    x0 = torch.normal(mean_value * n_data, 1) + bias
    y0 = torch.zeros(sample_nums)
    x1 = torch.normal(-mean_value * n_data, 1) + bias
    y1 = torch.ones(sample_nums)

    train_x = torch.cat((x0, x1), 0)
    train_y = torch.cat((y0, y1), 0)

    # ================== step 2: Select model. ============================.
    lr_net = NeuralNetwork()

    # ================== step 3: Select lose function. ====================.
    loss_fn = nn.BCELoss()

    # ================== step 4: Select model optimizer. ==================.
    lr = 0.01
    optimizer = torch.optim.SGD(lr_net.parameters(), lr = lr, momentum = 0.9)

    # ================== step 5: Train model. =============================.
    for iteration in range(1000):
    # {
        # forward.
        y_pred = lr_net(train_x)

        # calcute loss.
        loss = loss_fn(y_pred.squeeze(), train_y)

        # backward.
        loss.backward()

        # update parameters.
        optimizer.step()

        # draw.
        if 0 == (iteration % 10):

            mask    = y_pred.ge(0.5).float().squeeze()
            correct = (mask == train_y).sum()
            acc     = correct.item() / train_y.size(0)

            plt.scatter(x0.data.numpy()[:, 0], x0.data.numpy()[:, 1], c = 'r')
            plt.scatter(x1.data.numpy()[:, 0], x1.data.numpy()[:, 1], c = 'b')

            w0, w1 = lr_net.features.weight[0]
            w0, w1 = float(w0.item()), float(w1.item())
            plot_b = float(lr_net.features.bias[0].item())
            plot_x = np.arange(-6, 6, 0.1)
            plot_y = (-w0 * plot_x - plot_b) / w1

            plt.xlim(-5, 7)
            plt.ylim(-7, 7)
            lines = plt.plot(plot_x, plot_y)

            text = plt.text(-5, 5, 'Loss=%.4f' % loss.data.numpy(), fontdict = {'size': 20, 'color': 'red'})
            plt.title('Iteration: {}\nw0: {:.2f} w1: {:.2f} b: {:2f} accuracy:{:.2%}' \
                .format(iteration, w0, w1, plot_b, acc))
            
            print('Iteration: {} w0: {:.2f} w1: {:.2f} b: {:2f} accuracy:{:.2%}' \
                .format(iteration, w0, w1, plot_b, acc))

            plt.legend(['class 1', 'class 2'])
            plt.pause(1)

            if acc > 0.99:
                plt.show()
                break

            line = lines[0]
            line.remove()
            text.remove()
    # }

    return 0
# }


# Program entry.
if '__main__' == __name__:
# {
    main()
# }
