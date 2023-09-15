import torch

ckpt_path = "ckpt.pt"
checkpoint = torch.load(ckpt_path)

for key, value in checkpoint.items():
    print(key, type(value))

