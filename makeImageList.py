import os
imagePath = 'C:\\dataset\\drone\\test\\images'
testList = os.listdir(imagePath)

txtfile = open("testlist.txt", 'w')

for filename in testList:
    txtfile.write('testImage\\'+filename+'\n')

txtfile.close()
