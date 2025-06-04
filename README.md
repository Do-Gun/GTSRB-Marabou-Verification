1. **가상 환경 및 깃 클론**

```bash
conda create -n marabou python=3.8 -y

pip install maraboupy

git clone https://github.com/NeuralNetworkVerification/Marabou.git
cd Marabou/
mkdir build 
cd build
```

1. **cmake 설치**

[제목 없음](https://www.notion.so/2085cdcbb9aa80dc809fdc018385365b?pvs=21)

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

1. **경로 등록**

```bash
# 매번 cmake 경로 수동 등록해줘야 함!!
export PATH=$HOME/local/cmake-install/bin:$PATH
```

1. **marabou 빌드하기**

```bash
cd ~/Marabou/build
cmake ..
cmake --build . -j$(nproc)
```

여기까지 완료하면 
[100%] Built target build-tests 가 나올 것임 ㅇㅇㅇ..

1. **경로 설정**

```bash
# 매번 등록 해줘야 함!!
export PYTHONPATH=$PYTHONPATH:/home/dogun/Marabou
export JUPYTER_PATH=$JUPYTER_PATH:/home/dogun/Marabou
```

1. **실행 해보기 (CLI)**

```bash
# marabou 폴더에서

build/Marabou resources/nnet/acasxu/ACASXU_experimental_v2a_2_7.nnet resources/properties/acas_property_3.txt
```

![image.png](attachment:e6c21a78-a882-4510-98c4-ca983a4f8599:image.png)

ACASXU_experimental_v2a_2_7.nnet 검증

Network: resources/nnet/acasxu/ACASXU_experimental_v2a_2_7.nnet
Number of layers: 8. Input layer size: 5. Output layer size: 5. Number of ReLUs: 300

1. 검증 모델

```bash
# 모델 

conda install pytorch==2.4.1 torchvision==0.19.1 torchaudio==2.4.1 pytorch-cuda=12.4 -c pytorch -c nvidia

파일 만들고 cd
이후 내가 올린 모델 깃 클론 내용 쭉...(가중치도 올려놨으니까 그냥 바로 verify 하면됨 ㅇㅇ... 
```
