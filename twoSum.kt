class Solution {
    fun twoSum(nums: IntArray, target: Int): IntArray {
        val numMap = mutableMapOf<Int, Int>()

        for (i in nums.indices) {
            val diff = target - nums[i]

            if (numMap.containsKey(diff)) {
                return intArrayOf(numMap[diff]!!, i)
        }

        numMap[nums[i]] = i
    }
    return intArrayOf()
    }
}
