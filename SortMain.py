# 团队排序算法整合项目 - 初始框架
# 项目名称：First_Main_202340140115
# 开发规范：遵循驼峰命名、注释完整、格式统一
# 排序算法函数预留区域：组内成员依次在下方添加自己的算法
# 示例格式：def 姓名首拼_算法名(参数): 如 zsBubbleSort(arr)
# 冒泡排序
# 功能：对数字数组进行升序排序
# 参数：arr - 待排序的数字数组
# 返回值：sortedArr - 排序后的升序数组
def zsBubbleSort(arr):
    # 复制原数组，避免修改原数据
    sortedArr = arr.copy()
    n = len(sortedArr)
    # 外层循环：控制排序轮数
    for i in range(n-1):
        # 内层循环：控制每轮比较次数
        for j in range(n-1-i):
            if sortedArr[j] > sortedArr[j+1]:
                # 交换相邻元素
                sortedArr[j], sortedArr[j+1] = sortedArr[j+1], sortedArr[j]
    return sortedArr

# 快速排序
# 功能：对数字数组进行升序排序
# 参数：arr - 待排序的数字数组
# 返回值：sortedArr - 排序后的升序数组
def LsxQuickSort(arr):
    # 复制原数组，避免修改原数据
    sortedArr = arr.copy()
    # 定义快速排序辅助函数
    def quick_sort(arr, low, high):
        if low < high:
            # 分区操作，返回分区点
            pivot_index = partition(arr, low, high)
            # 递归排序左半部分
            quick_sort(arr, low, pivot_index - 1)
            # 递归排序右半部分
            quick_sort(arr, pivot_index + 1, high)
    
    # 定义分区函数
    def partition(arr, low, high):
        # 选择最右边的元素作为基准
        pivot = arr[high]
        # 小于基准的元素的位置
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        # 将基准元素放到正确的位置
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
    
    # 调用快速排序函数
    quick_sort(sortedArr, 0, len(sortedArr) - 1)
    return sortedArr
# 程序运行测试入口：所有成员最终在此处调用自己的算法
if __name__ == '__main__':
    # 测试数组：统一使用该数组验证排序效果，保证一致性
    testArr = [9, 3, 7, 1, 5, 8, 2, 6, 4]
    print("原始测试数组：", testArr)
    # 成员调用自己的算法：后续在此处添加代码
    # 调用冒泡排序算法，并输出结果
    sortedArr = zsBubbleSort(testArr)
    print("冒泡排序后数组：", sortedArr)
    # 调用快速排序算法，并输出结果
    sortedArr = LsxQuickSort(testArr)
    print("廖硕兴快速排序后数组：", sortedArr)