from radiomics import featureextractor
import SimpleITK as sitk
import os
import pandas as pd

basePath='D:\\Python\\CourseFile\\data_part1\\brain1'
#注意python写windows文件名，不要带中文路径，而且要双斜杠

'''imageFile = os.path.join(basePath, 'brain1_image.nrrd')
maskFile = os.path.join(basePath, 'brain1_label.nrrd')
extractor = featureextractor.RadiomicsFeatureExtractor()
featureVector = extractor.execute(imageFile,maskFile)
for featureName in featureVector.keys():
    print("%s:%s" % (featureName, featureVector[featureName]))
#以上是特征值全提取

basePath='D:\\Python\\CourseFile\\data_part1\\brain1'
imageFile=os.path.join(basePath, 'brain1_image.nrrd')
maskFile=os.path.join(basePath, 'brain1_label.nrrd')
settings = {}   #进行参数修改,打印出来记得看一下
settings['binWidth'] = 25
extractor = featureextractor.RadiomicsFeatureExtractor(**settings)  #读入刚才的设置参数
featureVector = extractor.execute(imageFile,maskFile)
for featureName in featureVector.keys():
    print("%s,%s" % (featureName, featureVector[featureName]))
#以上是对setting进行修改
'''

'''basePath='D:\\Python\\CourseFile\\data_part1\\brain1'
imageFile=os.path.join(basePath, 'brain1_image.nrrd')
maskFile=os.path.join(basePath, 'brain1_label.nrrd')
extractor = featureextractor.RadiomicsFeatureExtractor()    #定义提取器对象
extractor.disableAllFeatures()      #关闭所有特征值提取
extractor.enableFeaturesByName(firstorder=['Mean', 'Skewness'])    #根据名字打开特征值,打开firstorder里面的Mean和Skewness
extractor.enableFeatureClassByName('shape')   #根据类名打开特征值,需要了解一下各种类方法
extractor.enableFeatureClassByName('glcm')
extractor.enableImageTypes(Original={}, Wavelet={},)     #定义滤波器,后续去了解一下各种滤波器
featureVector = extractor.execute(imageFile,maskFile)
for featureName in featureVector.keys():
    print("%s:%s" % (featureName, featureVector[featureName]))
'''

basePath='D:\\Python\\CourseFile2\\data_part1'
folders = os.listdir(basePath)      #把basePath文件夹展示出来
print(folders)

df = pd.DataFrame()     #建一个空的数据框架
extractor = featureextractor.RadiomicsFeatureExtractor()
for folder in folders  :    #每个文件夹
    files = os.listdir(os.path.join(basePath,folder))
    print(files)
    for file in files:      #每个文件夹里每个文件
        if file.endswith('image.nrrd'):        #如果文件结尾是image.nrrd就令imageFile=它
            imageFile = os.path.join(basePath,folder,file)
        if file.endswith('label.nrrd'):        #如果文件结尾是label.nrrd就令imageFile=它
            maskFile = os.path.join(basePath,folder,file)
        #print(imageFile,maskFile)
    featureVector = extractor.execute(imageFile,maskFile)
    df_new = pd.DataFrame.from_dict(featureVector.values()).T   #.T是转置
    df_new.columns = featureVector.keys()   #把featureVector.keys关键字名称赋给df_new的列
    df = pd.concat([df,df_new])       #把df和df_new两个数组合并起来
df.to_excel(os.path.join(basePath,'results.xlsx'))

#以上是批量处理大量的图片特征值








