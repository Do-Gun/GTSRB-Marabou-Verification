import torch
import torch.nn as nn
import torch.optim as optim
from torchvision.datasets import GTSRB
from torchvision import transforms
from torch.utils.data import DataLoader
from simple_cnn import SimpleCNN

# 1. 데이터셋 로딩
transform = transforms.Compose([
    transforms.Resize((32, 32)),
    transforms.ToTensor(),
])
train_dataset = GTSRB(root="./data", split="train", transform=transform, download=True)
train_loader = DataLoader(train_dataset, batch_size=640, shuffle=True)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = SimpleCNN().to(device)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# 2. 학습 루프
for epoch in range(10):
    total_loss = 0
    for images, labels in train_loader:
        images, labels = images.to(device), labels.to(device)
        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        total_loss += loss.item()
    print(f"Epoch {epoch+1}: Loss = {total_loss:.4f}")

# 3. 모델 저장
torch.save(model.state_dict(), "model.pt")
print("✅ 모델 저장 완료: model.pt")