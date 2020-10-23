import ctypes
import numpy as np

func = ctypes.cdll.LoadLibrary("./test.so")

a = [1.0, 2.0, 3.0, 4.0, 5.0,6.0]
arr= (ctypes.c_double * len(a))(*a) #有点类似malloc的方式生成a_arr
func.show_matrix(arr, 6, 1)



def Convert2DTo1D_numpy(arrTwo):
    rows, cols = arrTwo.shape
    arr=[]
    for i in range(rows):
        for j in range(cols):
            arr.append(arrTwo[i][j])
            #print(arrTwo[i][j])
    return arr
#先把二维numpy数组转化为一维list数组，再转化为可传入C函数的数组
arrTwo = np.array([[1.0, 2.0, 3.0, 4.0],[5.0,6.0,7.0,8.0]])
row_, col_ = arrTwo.shape
arrTwo_list=Convert2DTo1D_numpy(arrTwo)
print(arrTwo_list)
arrTwo= (ctypes.c_double * len(arrTwo_list))(*arrTwo_list)
func.show_matrix(arrTwo, row_, col_)





