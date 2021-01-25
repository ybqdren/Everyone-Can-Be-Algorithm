/* Create by ZhaoWen */
package binary_search

/**
实现二分查找
@parm arr 被查找的数组对象
@parm key 要查找的数字
@return 返回key的位置
*/
func binary_search(arr []int, key int) int {
	var result int
	var mid int
	var low int = 0
	var high int = len(arr) - 1

	for low < high {
		mid = (low + high) / 2

		if arr[mid] > key {
			high = mid - 1
		} else if arr[mid] < key {
			low = mid + 1
		} else if arr[mid] == key {
			result = mid
			break
		}
	}
	return result
}

/*func main(){
	var arr = []int{1,2,3,5,7,8,9,10}
	i := binary_search(arr,9)
	fmt.Println("查找到的值：",i)
}*/
