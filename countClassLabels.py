# 주어진 데이터셋의 클래스별 바운딩 박스의 갯수를 세고
# 클래스의 번호를 지정하면 해당 클래스가 속한 이미지의 
# 리스트를 출력해 주는 프로그램
# 이를 위해서 pandas 데이터프레임을 활용한다.

import os
import glob
import pandas as pd

# 리스트를 생성
# 이미지 파일의 경로, 레이블 파일의 경로, 클래스 번호
# 주의할 점은 하나의 이미지라 하더라도 바운딩 박스는 여러 개 일 수 있다.

imageFiles = []
labelFiles = []
classNum = []

# 경로 설정
datasetBase = 'C:\\dataset\\drone\\train'
imagePath = os.path.join(datasetBase, 'images')
labelPath = os.path.join(datasetBase, 'labels')

# os.listdir()을 사용하여 *.txt만 골라내기
filenames = [file for file in os.listdir(labelPath) if file.endswith('.txt')]
#print(filenames)

for txtfile in filenames: 
    # labels폴더에서 classes.txt를 찾으면 pass
    if txtfile=='classes.txt':
        pass
    else:
        file = open(os.path.join(labelPath,txtfile), 'r')
        fileFront = os.path.splitext(txtfile)[0]
        while True:
            line = file.readline()
            #더 이상 읽을 줄이 없으면
            if not line:
                break
            num = line.split(' ')[0]
            imageFiles.append(os.path.join(imagePath,fileFront+'.jpg'))
            labelFiles.append(os.path.join(labelPath,fileFront+'.txt'))             
            classNum.append(num)

imageFiles = pd.Series(imageFiles)
labelFiles = pd.Series(labelFiles)
classNum   = pd.Series(classNum)

df = pd.DataFrame()
df['imageName'] = imageFiles
df['labelName'] = labelFiles
df['classNum']  = classNum

# 모든 데이터를 droneData.csv파일에 저장
df.to_csv('droneData.csv')

# number plate의 클래스만 골라서 저장
df3 = df[df['classNum']=='3']
df3.to_csv('drone_class3.csv')


