package main

import (
	"fmt"
	"math/rand"
)

func insertSort(array []int) {
	size := len(array)
	for j := 1; j < size; j++ {
		key := array[j]
		i := j - 1
		for i >= 0 && array[i] > key {
			array[i+1] = array[i]
			i--
		}
		array[i+1] = key
	}
}

func main() {
	s := rand.Perm(10)
	fmt.Println(s)
	insertSort(s)
	fmt.Println(s)
}
