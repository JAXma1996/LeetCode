package mahb.leetcode.easy;

import java.util.HashMap;
import java.util.Map;

public class TwoSum {
    public static void main(String[] args) {
        int[] result = twoSum(new int[]{1,5,6,8,7,4,9},11);
        for (int a:result) {
            System.out.println(a);
        }
    }

    // 最直接方便解决的方法, 就是使用了遍历 实现了 n^2的解决方案
    public static int[] twoSum(int[] nums, int target) {
        int[] a = new int[1];
        for (int i = 0; i < nums.length; i++) {
            for (int j = 0; j < nums.length; j++) {
                if (j!=i && nums[i]+nums[j]==target){
                    return new int[]{i,j};
                }
            }
        }
        return null;
    }
    public static int[] twoSumWithHashMap(int[] nums, int target) {
        //用一个hash map来存放已经遍历计算过的num , 其实就是使用空间来置换时间复杂度
        Map<Integer,Integer> numsMap = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int substrattion = target-nums[i];
            if(numsMap.containsKey(substrattion)){
                return new int[]{numsMap.get(substrattion),i};
            }
            numsMap.put(nums[i],i);
        }
        return null;
    }
}
