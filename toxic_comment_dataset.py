import torch
from torch.utils.data import Dataset

class Toxic_Comment_Dataset(Dataset):

    def __init__(self, encoding, labels):
        self.encoding = encoding
        self.labels = labels

    def __getitem__(self, index):
        item = {key : torch.tensor(val[index]) for key, val in self.encoding.items()}
        item['labels'] = torch.tensor(self.labels[index])

        return item
    
    def __len__(self):
        return len(self.labels)