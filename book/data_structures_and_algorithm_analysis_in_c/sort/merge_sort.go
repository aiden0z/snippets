package main

import (
	"fmt"
	"math/rand"
)

func merge(s []int, p, q, r int) {
	n1 := q - p + 1
	n2 := r - q
	left := make([]int, n1)
	right := make([]int, n2)
	for i := 0; i < n1; i++ {
		left[i] = s[p+i-1]
	}
	for i := 0; i < n2; i++ {
		right[i] = s[q+i]
	}

	var i, j int
	for k := p - 1; k < r; k++ {
		if i == n1 {
			s[k] = right[j]
			j++
			continue
		} else if j == n2 {
			s[k] = left[i]
			i++
			continue
		}
		if left[i] <= right[j] {
			s[k] = left[i]
			i++
		} else {
			s[k] = right[j]
			j++
		}
	}
}

func mergeSort(s []int, p, r int) {
	if p < r {
		q := (p + r) / 2
		mergeSort(s, p, q)
		mergeSort(s, q+1, r)
		merge(s, p, q, r)
	}
}

func main() {
	s := rand.Perm(10)
	fmt.Println(s)
	mergeSort(s, 1, len(s))
	fmt.Println(s)
}
