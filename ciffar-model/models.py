
from torch import Tensor, nn
import torch.nn.functional as F


class SimpleModel(nn.Module):
    def __init__(self, backbone: nn.Module, adapter: nn.Module, head: nn.Module) -> None:
        super().__init__()
        self.backbone = backbone
        self.adapter = adapter
        self.head = head

    def forward(self, x: Tensor) -> Tensor:
        x = x.repeat(1, 3, 1, 1)
        x = self.backbone(x)
        x = self.adapter(x)
        x = self.head(x)
        return x


class CIFAR10Model(nn.Module):
    """
    Hint: It is going to be very similar to SimpleModel
    """
    def __init__(self, backbone: nn.Module, adapter: nn.Module, head: nn.Module) -> None:
        super().__init__()
        super().__init__()
        self.backbone = backbone
        self.adapter = adapter
        self.head = head

    def forward(self, x):
        x = nn.MaxPool2d(2, 2)(F.relu(self.backbone(x)))
        #x = self.backbone(x)
        x = self.adapter(x)
        x = self.head(x)
        return x