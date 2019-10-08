// 测试是否能从 cgo 异常中恢复
package main

/*
#include <stdio.h>

static void segfault() {
	// const char *s = "hello";
	const char *s = NULL;
	// will cause segmentfault error
	printf( "%c\n", s[1] );
}
*/
import "C"
import "fmt"
import "runtime"

func main() {
	runtime.GOMAXPROCS(1)
	defer func() {
		if err := recover(); err != nil {
			fmt.Println("recovery from C code: ", err)
		}
		fmt.Println("hello world")
	}()
	C.segfault()
}
