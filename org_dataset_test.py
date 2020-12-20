# オリジナルデータセットを読み込み用
import torch
from torch.utils import data
from torchvision import transforms, datasets


# オリジナルデータセットを読み込み用
transform = transforms.Compose([transforms.ToTensor()])
train_set = datasets.CocoDetection(root='data/coco_helmet/train',
                                annFile='data/coco_helmet/train.json',
                                transform=transform)
dataset = data.DataLoader(train_set)