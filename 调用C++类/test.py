import ctypes  
lib = ctypes.cdll.LoadLibrary('./libpycallclass.so')   
lib.display()   
lib.display_int(10) 
