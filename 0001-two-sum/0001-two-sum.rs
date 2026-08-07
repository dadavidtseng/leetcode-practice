use std::collections::HashMap;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut num_index_map: HashMap<i32, i32> = HashMap::new();

        for (i, &num) in nums.iter().enumerate() {
            let diff = target - num;

            if let Some(&index) = num_index_map.get(&diff) {
                return vec![index, i as i32];
            }

            num_index_map.insert(num, i as i32);
        }

        vec![]
    }
}