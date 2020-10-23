#include "stdio.h"
int show_msg(const char* name) {
    printf("hello %s!\n", name);
    return 0;
}

char* show_msg2(char* name) {
    printf("hello %s!\n", name);
    return name;
}