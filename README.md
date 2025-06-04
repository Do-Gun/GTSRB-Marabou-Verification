# ✅ GTSRB Marabou Verification

자율주행 차량에서 사용되는 CNN 모델의 **robustness (견고성)** 을 검증하는 프로젝트입니다.  
GTSRB 교통 표지판 데이터셋을 기반으로 간단한 CNN을 학습한 뒤,  
ONNX 형식으로 변환하여 **Marabou**로 안정성을 검증합니다.

---

## 1. 💻 가상 환경 및 Marabou 설치

```bash
# Conda 가상환경 생성
conda create -n marabou python=3.8 -y
conda activate marabou

# MarabouPy 설치
pip install maraboupy

# Marabou 소스 클론 및 빌드 폴더 생성
git clone https://github.com/NeuralNetworkVerification/Marabou.git
cd Marabou/
mkdir build
cd build

---

## 2. ㅂㅂ
