package main

import (
	"fmt"
	"math/rand"
)

func bubbleSort(s []int) {
	size := len(s)
	for i := 0; i < size; i++ {
		for j := i + 1; j < size; j++ {
			if s[i] > s[j] {
				s[i], s[j] = s[j], s[i]
			}
		}
	}
}

func bubbleSort2(s []int) {
	size := len(s)
	for i := 0; i < size; i++ {
		for j := size - 1; j > i; j-- {
			if s[j] < s[j-1] {
				s[j], s[j-1] = s[j-1], s[j]
			}
		}
	}
}

func main() {
	t1 := rand.Perm(10)
	fmt.Println(t1)
	bubbleSort2(t1)
	fmt.Println(t1)
}
