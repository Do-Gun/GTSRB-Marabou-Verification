# ✅ GTSRB Marabou Verification

자율주행 차량에서 사용되는 CNN 모델의 **robustness (견고성)** 을 검증하는 프로젝트입니다.  
GTSRB 교통 표지판 데이터셋을 기반으로 간단한 CNN을 학습한 뒤,  
ONNX 형식으로 변환하여 Marabou로 안정성을 검증합니다.

---

## 1. 💻 가상 환경 및 Marabou 설치

```bash
conda create -n marabou python=3.8 -y
conda activate marabou
pip install maraboupy

git clone https://github.com/NeuralNetworkVerification/Marabou.git
cd Marabou/
mkdir build
cd build
2. ⚙️ CMake 수동 설치 (sudo 없이)
bash
복사
편집
cd ~
mkdir -p local/cmake && cd local
wget https://github.com/Kitware/CMake/releases/download/v3.31.7/cmake-3.31.7.tar.gz
tar -xzf cmake-3.31.7.tar.gz
cd cmake-3.31.7

./bootstrap --prefix=$HOME/local/cmake-install -- -DCMAKE_USE_OPENSSL=OFF
make -j$(nproc)
make install
cmake --version
3. 🔧 경로 등록 (매번 수행 필요)
bash
복사
편집
export PATH=$HOME/local/cmake-install/bin:$PATH
4. 🧱 Marabou 빌드하기
bash
복사
편집
cd ~/Marabou/build
cmake ..
cmake --build . -j$(nproc)
빌드 완료 시: [100%] Built target build-tests 메시지가 출력됩니다.

5. 🧪 Marabou 환경 등록
bash
복사
편집
export PYTHONPATH=$PYTHONPATH:/home/dogun/Marabou
export JUPYTER_PATH=$JUPYTER_PATH:/home/dogun/Marabou
6. 🧬 예시 실행 (ACASXU)
bash
복사
편집
cd ~/Marabou
./build/Marabou resources/nnet/acasxu/ACASXU_experimental_v2a_2_7.nnet resources/properties/acas_property_3.txt
ACASXU 네트워크에 대한 검증이 수행됩니다.
예: Input layer size: 5. Output layer size: 5. Number of ReLUs: 300

7. 🛣️ GTSRB 모델 학습 및 검증
bash
복사
편집
# 필요한 PyTorch 버전 설치
conda install pytorch==2.4.1 torchvision==0.19.1 torchaudio==2.4.1 pytorch-cuda=12.4 -c pytorch -c nvidia

# 프로젝트 클론 및 이동
git clone https://github.com/Do-Gun/GTSRB-Marabou-Verification.git
cd GTSRB-Marabou-Verification

# 학습 및 모델 내보내기
python train_gtsrb.py
python export_onnx.py

# Marabou로 검증
python verify_marabou.py
8. 🔁 학습 건너뛰고 검증만 하려면?
bash
복사
편집
python export_onnx.py
python verify_marabou.py
📁 포함된 파일
