import nibabel as nib
import os
basepath = r'D:\Python\pythonProject2'
atlasPath = os.path.join(basepath,'HarvardOxford-cort-maxprob-thr50-2mm（医学课唯一售后782878241）.nii')       #载入脑图路径

roiIndex = 17    #要取的那部分区域，光标放到mricrogl图里，上方可以得到区域
atlas_nii = nib.load(atlasPath)
atlas_arr = atlas_nii.get_fdata()   #得到脑图的区域矩阵，非像素矩阵
mask_arr = atlas_arr.copy()     #把脑图的矩阵复制给mask
mask_arr[atlas_arr != roiIndex] = 0     #在区域内的赋值1，不在区域内的复制0
mask_arr[atlas_arr == roiIndex] = 1
mask_affine = atlas_nii.affine.copy()   #把原来的仿射变换矩阵复制给mask矩阵，放射变换矩阵理解成把区域矩阵变成像素矩阵的
mask_hrd = atlas_nii.header.copy()      #header包含这个图片的元数据
mask_hrd ['cal_max'] = 1        #调整灰度值范围最大为1
mask_nii = nib.Nifti1Image(mask_arr, mask_affine, mask_hrd)
nib.save(mask_nii, os.path.join(basepath, 'roi_17'))


'''
一个nibabel图像对象是三件事情的联系：
包含图像数据的ND阵列;
（4，4） 仿射,矩阵映射数组坐标到一些RAS +世界坐标空间（ 坐标系和 仿射 ）中的 坐标 ;
以头部形式的图像元数据.
'''