#  GTSRB Marabou Verification

자율주행 차량에서 사용되는 CNN 모델의 **robustness** 을 검증하는 프로젝트입니다.  
GTSRB 교통 표지판 데이터셋을 기반으로 간단한 CNN을 학습한 뒤,  
ONNX 형식으로 변환하여 **Marabou**로 안정성을 검증합니다.

CUDA 12.4
Python 3.8
Pytorch 2.4.1

GPU: RTX 3090

---

# 1. 가상 환경 및 Marabou 설치

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
```

---
# 2. CMake 수동 설치 

```bash
cd ~
mkdir -p local/cmake && cd local
wget https://github.com/Kitware/CMake/releases/download/v3.31.7/cmake-3.31.7.tar.gz
tar -xzf cmake-3.31.7.tar.gz
cd cmake-3.31.7
# ./bootstrap --prefix=$HOME/local/cmake-install
# make -j$(nproc)
# make install

./bootstrap --prefix=$HOME/local/cmake-install -- -DCMAKE_USE_OPENSSL=OFF
make -j$(nproc)
make install

# 설치 확인
cmake --version
```

---
## 3. CMake 경로 등록(매번 수행 필요)
```bash
export PATH=$HOME/local/cmake-install/bin:$PATH
```

---
# 4. Marabou 빌드하기
```bash
cd ~/Marabou/build
cmake ..
cmake --build . -j$(nproc)
```

---
# 5. Marabou 환경 등록 (매번 수행 필요)
```bash
export PYTHONPATH=$PYTHONPATH:/home/dogun/Marabou # 경로 수정 필요
export JUPYTER_PATH=$JUPYTER_PATH:/home/dogun/Marabou # 경로 수정 필요
```

---
# 6. 예시 실행 (ACASXU)
```bash
cd ~/Marabou
./build/Marabou resources/nnet/acasxu/ACASXU_experimental_v2a_2_7.nnet resources/properties/acas_property_3.txt
```

---
# 7. GTSRB, CNN 모델 학습 및 검증
```bash
# 모델 디렉토리 생성
mkdir -p model
cd model

git clone https://github.com/Do-Gun/GTSRB-Marabou-Verification.git .

# 검증 실행
python verify_marabou.py
```

# 7. GTSRB, CNN 모델 검증
```bash
# 모델 디렉토리 생성
mkdir -p model
cd model

git clone https://github.com/Do-Gun/GTSRB-Marabou-Verification.git .

# 검증 실행
python verify_marabou.py
```

# 8. GTSRB, CNN 모델 학습(Optional)
```bash
cd model

python GTSRB.py
python train_gtsrb.py
```



