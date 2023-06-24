### 본 github의 코드나 문서들은 yolov8모델을 사용하여 드론으로 촬영된 이미지를 학습하는 과정을 설명합니다.

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


## 엘리스 VSCode환경에서 아나콘다 설치
``` mkdir -p ~/miniconda3 ```

``` wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh ```

``` bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3 ```

``` rm -rf ~/miniconda3/miniconda.sh ```

``` ~/miniconda3/bin/conda init bash ```

``` ~/miniconda3/bin/conda init zsh ```