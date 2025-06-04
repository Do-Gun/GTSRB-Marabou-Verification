import numpy as np
from torchvision.datasets import GTSRB
from torchvision import transforms
from maraboupy import Marabou

print("[1/5] 모델 로딩 시작")
network = Marabou.read_onnx("model.onnx")
inputVars = network.inputVars[0].flatten()
outputVars = network.outputVars[0]
print("[1/5] 모델 로딩 완료")

print("[2/5] 테스트 이미지 불러오기 시작")
transform = transforms.Compose([
    transforms.Resize((32, 32)),
    transforms.ToTensor(),
])
testset = GTSRB(root="./data", split="test", transform=transform, download=True)
sample, label = testset[0]
x = sample.numpy().astype(np.float32).flatten()
print("[2/5] 테스트 이미지 로드 완료")

print("[3/5] 입력 perturbation 설정 시작")
eps = 0.001
for i, val in enumerate(x):
    network.setLowerBound(inputVars[i], max(0, val - eps))
    network.setUpperBound(inputVars[i], min(1, val + eps))
print("[3/5] perturbation 설정 완료")

print("[4/5] 예측 클래스 고정 제약 추가 중")
pred = np.argmax(network.evaluateWithoutMarabou([x])[0])
print(f"예측 클래스: {pred}")
for i in range(43):
    if i != pred:
        network.addInequality(
            [outputVars[0][pred], outputVars[0][i]],
            [1.0, -1.0],
            0.0
        )
print("[4/5] 예측 클래스 제약 설정 완료")

print("[5/5] Marabou Solver 실행 시작")
exitCode, _, _ = network.solve()
print("[5/5] Solver 종료")

if exitCode == "unsat":
    print(f"결과: Robust (클래스 {pred}는 ±{eps} 내에서 변하지 않음)")
else:
    print(f"결과: Fragile (클래스 {pred}는 ±{eps} 내에서 변경 가능함)")