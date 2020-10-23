from ctypes import *

lib = CDLL("./libtest.so") 
#相同效果：lib = cdll.LoadLibrary("./test.so")
lib.show_msg(c_char_p(bytes('good',encoding="utf-8")))


lib.show_msg2.restype = c_char_p
result = lib.show_msg2(c_char_p(bytes('213213213',encoding="utf-8")))

print(str(result))