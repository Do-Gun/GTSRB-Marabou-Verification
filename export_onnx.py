import torch
from simple_cnn import SimpleCNN

model = SimpleCNN()
model.load_state_dict(torch.load("model.pt", map_location="cpu"))
model.eval()

dummy_input = torch.randn(1, 3, 32, 32)
torch.onnx.export(
    model, dummy_input, "model.onnx",
    input_names=["input"], output_names=["output"], opset_version=11
)
print("ONNX 파일 저장 완료: model.onnx")

