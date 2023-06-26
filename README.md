### yolov8모델을 사용하여 드론으로 촬영된 이미지를 학습합니다.

<br>
<br>

## PC 환경설정
### 1. 아나콘다(미니콘다)설치
* 다운로드 : https://docs.conda.io/en/latest/miniconda.html#windows-installers
* 프로그램 설치
* 윈도우 검색에서 anaconda prompt를 찾아서 실행
* anaconda prompt 앞에 '(base)'가 출력되고 있으면 정상 설치

### 2. 아나콘다 가상환경 설정
#### 2.1 가상환경 설치
``` conda create -n yolov8 python=3.8 ```

#### 2.2 가상환경 들어가기
``` conda activate yolov8 ```

### 3. YOLO Label 툴 설치하기
``` git clone https://github.com/heartexlabs/labelImg ```

``` cd labelImg ```

``` pip install pyqt5 lxml ```

``` pyrcc5 -o libs/resources.py resources.qrc ```

### 4. YOLO Label 툴 실행해보기
``` python labelimg.py ``` 
를 실행해서 정상적으로 동작되는지 확인

<br>
<br>

## 엘리스 VSCode환경에서 아나콘다 설치

``` mkdir -p ~/miniconda3 ```

``` wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh ```

``` bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3 ```

``` rm -rf ~/miniconda3/miniconda.sh ```

``` ~/miniconda3/bin/conda init bash ```

``` ~/miniconda3/bin/conda init zsh ```

<br>
<br>

## 데이터셋을 만드는 순서
#### 1. 이미지 촬영하기
#### 2. labelImg를 사용하여 바운딩 박스를 그려주기
#### 3. 데이터셋 나누기
* YOLOv8모델에 학습 시키기 위해 train/valid/test폴더에 각각 images, labels폴더 생성&복사
* [trainTestSplit.py파일 참조](https://github.com/venture21/yolov8_drone/blob/main/trainTestSplit.py)

## 데이터셋 YOLOv8로 학습하기
* YOLOv8패키지를 설치하고 yolov8학습하기
* [yolov8Train_test.ipynb파일 참조](https://github.com/venture21/yolov8_drone/blob/main/yolov8Train_test.ipynb)
* 이와 같이 학습하면 실행된 결과의 맨끝에 아래와 같은 결과를 확인
* [첫번째 학습 결과](https://github.com/venture21/yolov8_drone/blob/main/train1_result.png)
* numer plate가 가장 mAP가 낮게 나오는 것을 확인(Instances의 갯수도 가장 작음, 다른 클래스는 2배 이상)
* 이는 [runs/detect/predict/lables.png](https://github.com/venture21/yolov8_drone/blob/main/labels1.png)파일을 통해서도 확인 가능

## 데이터 증식하기
* 앞에 결과를 개선하기 위해 데이터를 증식하기
* 이를 위해 만들어진 Albumentations 패키지를 활용할 수 있다.
* Albumentations은 이미지를 증식해 줄 뿐만 아니라 바운딩 박스도 함께 증식한다.
* 참조 링크주소는 [Albumentations](https://albumentations.ai/docs/getting_started/bounding_boxes_augmentation/)
* 사용법에 대한 코드는 [testDataAug.ipynb](https://github.com/venture21/yolov8_drone/blob/main/testDataAug.ipynb)를 참조한다.

