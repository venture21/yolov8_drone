import glob, os
import shutil
import random

# �꾩옱 �붾젆�좊━瑜� �쎌뼱�⑤떎.
#current_dir = os.path.dirname(os.path.abspath(__file__))


datasetDir = 'C:\\dataset\\drone_org'
print('Dataset Directory is '+datasetDir)

targetDir = 'C:\\dataset\\drone_new'

trainImagePath = os.path.join(targetDir, 'train','images')
trainLabelPath = os.path.join(targetDir, 'train','labels')
validImagePath = os.path.join(targetDir, 'valid','images')
validLabelPath = os.path.join(targetDir, 'valid','labels')
testImagePath = os.path.join(targetDir, 'test','images')
testLabelPath = os.path.join(targetDir, 'test','labels')

# train : test ratio
# 90 : 10
valid_ratio = 10
test_ratio = 10

# Populate train.txt and test.txt
counter = 1
index_test = round(100 / test_ratio)
index_valid = round((100-index_test) / valid_ratio)

def makeFolder():
    # train/valid/test로 나누기
    # train/
    #        images/
    #        labels/
    # valid/
    #        images/
    #        labels/
    # test/
    #        images/
    #        labels/
    if os.path.exists(targetDir):
        shutil.rmtree(targetDir)

        print("old file is removed")

    os.makedirs(trainImagePath, exist_ok=True)
    os.makedirs(trainLabelPath, exist_ok=True)
    os.makedirs(validImagePath, exist_ok=True)
    os.makedirs(validLabelPath, exist_ok=True)
    os.makedirs(testImagePath, exist_ok=True)
    os.makedirs(testLabelPath, exist_ok=True)


def moveDataset():
    global counter
    makeFolder()

    # txt => labels/
    print('run moveDataset')
    datasetFileList = []
    for filelist in glob.iglob(os.path.join(datasetDir, '*.jpg')):
        datasetFileList.append(filelist)

    # 폴더에서 읽어온 리스트를  random.shuffle함수를 이용해서 마구잡이로 섞어준다.
    random.shuffle(datasetFileList)
    print(datasetFileList)

    for pathAndFilename in datasetFileList:
    #for pathAndFilename in glob.iglob(os.path.join(datasetDir+'/export/images', '*.jpg')):
        title, ext = os.path.splitext(os.path.basename(pathAndFilename))

        labelFilename = os.path.join(datasetDir, title+'.txt')
        #print(datasetDir)
        #print(labelFilename)
        if counter == index_test:
            counter = 1
            shutil.copy(pathAndFilename, os.path.join(testImagePath, title+'.jpg'))
            shutil.copy(labelFilename, os.path.join(testLabelPath, title+'.txt'))
        elif counter == index_valid:
            shutil.copy(pathAndFilename, os.path.join(validImagePath, title+'.jpg'))
            shutil.copy(labelFilename, os.path.join(validLabelPath, title+'.txt'))
            counter = counter + 1
        else:
            shutil.copy(pathAndFilename, os.path.join(trainImagePath, title+'.jpg'))
            shutil.copy(labelFilename, os.path.join(trainLabelPath, title+'.txt'))
            counter = counter + 1


def checkCopy():
    trainImageList = os.listdir(trainImagePath)
    validImageList = os.listdir(validImagePath)
    testImageList = os.listdir(testImagePath)
    trainTextList = os.listdir(trainLabelPath)
    validTextList = os.listdir(validLabelPath)
    testTextList = os.listdir(testLabelPath)
    print(len(trainImageList), len(trainTextList))
    print(len(testImageList), len(testTextList))
    print(len(validImageList), len(validTextList))

moveDataset()
checkCopy()