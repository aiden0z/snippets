package main

import (
	"bytes"
	"errors"
	"fmt"
	"github.com/aiden0z/kit/structure"
)

func nanotionPriority(char rune) int {
	switch char {
	case '-', '+':
		return 1
	case '*', '/':
		return 2
	case '(', ')':
		return 3
	}
	return 0
}

var ErrNotFoundBracket = errors.New("not found closed bracket")

func ReversePolish(dal string) (string, error) {

	var rvs bytes.Buffer
	stack := structure.NewStack(10)
	for _, char := range dal {
		priority := nanotionPriority(char)
		// number will be ouput directly
		if priority == 0 {
			fmt.Printf("1 output char: %c\n", char)
			rvs.WriteString(string(char))
		} else {
			// handle nonation
			if stack.Len() == 0 || char == '(' {
				fmt.Printf("1 push char: %c\n", char)
				stack.Push(char)
			} else if char == ')' {
				nanotion, _ := stack.Peek()
				for nanotion.(rune) != '(' {
					if nanotion, err := stack.Pop(); err != nil {
						return "", ErrNotFoundBracket
					} else {
						fmt.Printf("2 output char: %c\n", nanotion.(rune))
						rvs.WriteString(string(nanotion.(rune)))
						continue
					}
				}
			} else {
				nanotion, _ := stack.Peek()
				for nanotionPriority(nanotion.(rune)) < nanotionPriority(char) {
					if nanotion, err := stack.Pop(); err == nil {
						fmt.Printf("3 output char: %c\n", nanotion.(rune))
						rvs.WriteString(string(nanotion.(rune)))
					} else {
						break
					}
				}
				fmt.Printf("1 push char: %c\n", char)
				stack.Push(char)
			}
		}
	}
	// ouput the last nonation in stack
	for {
		if char, err := stack.Pop(); err != nil {
			fmt.Printf("4 output char: %c\n", char.(rune))
			rvs.WriteString(string(char.(rune)))
		} else {
			break
		}
	}
	fmt.Println(rvs.String)
	return rvs.String(), nil
}

func main() {
	// reverse polish: a b c * + d e * f + g * +
	var test = "a + b * c + (d * e + f) * g"
	if result, err := ReversePolish(test); err != nil {
		fmt.Println(result)
	} else {
		fmt.Println(err)
	}
}
