package mahb.leetcode.easy;

/**
 * @ProjectName: leetCode
 * @Package: mahb.leetcode.easy
 * @ClassName: PeakIndexInMountainArray
 * @Author: mahaibin
 * @Description:
 *  题目 再mountain Array 中找到顶点 的下标
 *  A.length >= 3
 * There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
 * 思路最简单的就是 O(n) 的遍历,目前想到比较好的就是二分查找的log(N)的方法
 * @Date: 2019/12/17 23:13
 * @Version: 1.0
 */
public class PeakIndexInMountainArray {
    public static int peakIndexInMountainArray(int[] A) {
        //        二分法的实现
        return binarySearch(A,0,A.length-1);
    }
    public static int binarySearch(int[] A,int start ,int end){
        int i = start+(end-start)/2;
        if (A[i]>A[i+1] && A[i-1]<A[i]) {
            return i;
            //当如果再峰值的右侧
        }else if(A[i]>A[i+1] && A[i-1]>A[i]){
           return binarySearch(A,start,i);
        }else{
            return binarySearch(A,i,end);
        }
    }

    public static void main(String[] args) {
        int[] A = {1,2,3,4,5,2,1};
        System.out.println(peakIndexInMountainArray(A));
    }
}
