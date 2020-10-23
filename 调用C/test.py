import ctypes  
lib= ctypes.cdll.LoadLibrary("./libpycall.so")    
result = lib.foo(1, 3) 
print(result) 
print('***finish***')