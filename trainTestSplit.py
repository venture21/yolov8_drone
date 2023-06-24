import glob, os
import shutil

# 현재 디렉토리를 읽어온다.
current_dir = os.path.dirname(os.path.abspath(__file__))
print("현재 작업 디렉토리 : "+current_dir)

current_dir = 'maskDataset'

# train : valid: test ratio
# 80 : 10 : 10
valid_ratio = 10
test_ratio = 10

# Create and/or truncate train.txt and test.txt
file_train = open('train.txt', 'w')
file_test = open('test.txt', 'w')

# Populate train.txt and test.txt
counter = 1

index_test = round(100 / test_ratio)
index_valid = round((100-index_test)/valid_ratio)


def makeFileList():
    # current_dir의 jpg파일만 골라내서 train.txt, trest.txt로 파일을 생성
    for pathAndFilename in glob.iglob(os.path.join(current_dir, "*.jpg")):
        # # title은 파일명에서 확장자만 제외한 파일명, ext는 확장자
        # os.path.basename()함수는 경로+파일명 -> 파일명만 추출해내는 함수
        title, ext = os.path.splitext(os.path.basename(pathAndFilename))

        # 10번에 한번 test리스트에 추가
        if counter == index_test:
            counter = 1
            # 경로+파일명
            file_test.write(current_dir + "/" + title + '.jpg' + "\n")

        # 9번은 train리스트에 추가
        else:
            # 경로+파일명
            file_train.write(current_dir + "/" + title + '.jpg' + "\n")
            counter = counter + 1

def makeFolder():
    # train/valid/test 폴더를 생성하고, 하위에 images, labels폴더를 생성
    # 기존에 폴더가 존재하면 폴더와 그안의 모든 파일 삭제
    trainImagePath = current_dir+'/train/images'
    trainLabelPath = current_dir+'/train/labels'
    validImagePath = current_dir+'/valid/images'
    validLabelPath = current_dir+'/valid/labels'
    testImagePath = current_dir+'/test/images'
    testLabelPath  = current_dir+'/test/labels'

    if os.path.exists(trainImagePath):
        shutil.rmtree(trainImagePath)
        shutil.rmtree(trainLabelPath)
        shutil.rmtree(validImagePath)
        shutil.rmtree(validLabelPath)
        shutil.rmtree(testImagePath)
        shutil.rmtree(testLabelPath)
        print("old file is removed")

    os.makedirs(trainImagePath, exist_ok=True)
    os.makedirs(trainLabelPath, exist_ok=True)
    os.makedirs(validImagePath, exist_ok=True)
    os.makedirs(validLabelPath, exist_ok=True)
    os.makedirs(testImagePath, exist_ok=True)
    os.makedirs(testLabelPath, exist_ok=True)

def copyDataset():
    global counter

    # current_dir의 jpg파일만 골라내서 train.txt, trest.txt로 파일을 생성
    # 경로+파일명+jpg
    for pathAndFilename in glob.iglob(os.path.join(current_dir, "*.jpg")):
        # # title은 파일명에서 확장자만 제외한 파일명, ext는 확장자
        # os.path.basename()함수는 경로+파일명 -> 파일명만 추출해내는 함수
        title, ext = os.path.splitext(os.path.basename(pathAndFilename))

        #txt파일의 경로 문자열 만들기
        pathString = os.path.dirname(pathAndFilename)
        #labelFile = pathString+'/'+title+'.txt'
        labelFilename = os.path.join(pathString,title+'.txt')
        
        # 각 폴더로 파일들을 복사 : 이미지를 먼저 복사하고(images폴더로 복사), 
        # 확장자만 txt인 파일을 찾아서 labels폴더로 복사 
        
        # counter가 10이되면 test 리스트에 추가
        # counter =1 로 초기화
        if counter == index_test:
            counter = 1
            #경로+파일명을 받아와서 파일을 이동
            #print(current_dir+'/test/images/'+title+'.jpg')
            #shutil.move(pathAndFilename, current_dir+'/test/images/'+title+'.jpg')
            shutil.copyfile(pathAndFilename, current_dir+'/test/images/'+title+'.jpg')
            shutil.copyfile(labelFilename, current_dir+'/test/labels/'+title+'.txt')
  
        # counter 9가되면 valid
        elif counter == index_valid:
            shutil.copyfile(pathAndFilename, current_dir+'/valid/images/'+title+'.jpg')
            shutil.copyfile(labelFilename, current_dir+'/valid/labels/'+title+'.txt')
            counter = counter + 1

        # counter가 0~8일때는 train 리스트에 추가
        else:
            #print(current_dir+'/train/images/'+title+'.jpg')
            #shutil.move(pathAndFilename, current_dir+'/train/images/'+title+'.jpg')
            shutil.copyfile(pathAndFilename, current_dir+'/train/images/'+title+'.jpg')
            shutil.copyfile(labelFilename, current_dir+'/train/labels/'+title+'.txt')
            counter = counter + 1

#복사가 잘 됐는지 폴더별로 파일의 갯수를 확인
def checkCopy():
    trainImageList = os.listdir(current_dir+'/train/images')
    trainLabelList = os.listdir(current_dir+'/train/labels')
    validImageList = os.listdir(current_dir+'/valid/images')
    validLabelList = os.listdir(current_dir+'/valid/labels')
    testImageList = os.listdir(current_dir+'/test/images')
    testLabelList = os.listdir(current_dir+'/test/labels') 
        
    print("==============================================")
    print("Train Image : {}".format(len(trainImageList)))  
    print("Valid Image : {}".format(len(validImageList)))  
    print("Test  Image : {}".format(len(testImageList)))
    print("==============================================")

    if len(trainImageList)!=len(trainLabelList):
        print("Train Data Copy Error")
        exit(-1)
    if len(validImageList)!=len(validLabelList):
        print("valid Data Copy Error")
        exit(-1)
    if len(testImageList)!=len(testLabelList):
        print("valid Data Copy Error") 
        exit(-1) 
    print("Copy is Done")

def moveDataset():
    makeFolder()
    copyDataset()
    checkCopy()

moveDataset()
