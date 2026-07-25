impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let nums_size = nums.len();

        // Iterate through every possible pairs in nums
        for i in 0..nums_size {
            for j in (i + 1)..nums_size {
                // Return result if we've found target
                if nums[i] + nums[j] == target {
                    return vec![i as i32, j as i32];
                }
            }
        }

        // Return empty result to satisfy compiler
        // Since the problem says there is guaranteed to be exactly one solution,
        // so we will never return an empty array.
        unreachable!()
    }
}