/* Create by ZhaoWen */
package binary_search

import (
	"fmt"
	"math"
)

func addToArrayForm(A []int, K int) []int {
	var sum int
	var count int = int(math.Pow10(len(A) - 1))

	for i := range A {
		sum += A[i] * count
		count /= 10
	}
	sum += K

	fmt.Println(sum)
	fmt.Println(sum % 100 % 10)

	/**
	个 sum%100%10
	十 sum % 100/10
	百 sum%1000/100
	千 sum%10000/1000
	*/
	fmt.Println(count)

	count = 100

	//  个位
	a := sum % count % count % 10
	b := sum % count / count / 10
	count *= 10
	c := sum % count / (count / 10)
	count *= 10
	d := sum % count / (count / 10)

	fmt.Println(d, c, b, a)
	var resultArr = []int{}

	resultArr = append(resultArr, d)
	resultArr = append(resultArr, c)
	resultArr = append(resultArr, b)
	resultArr = append(resultArr, a)

	return resultArr
}
