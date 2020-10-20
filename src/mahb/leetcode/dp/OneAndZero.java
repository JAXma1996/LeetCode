package mahb.leetcode.dp;


/**
 * 1和0 ，解题思路 依旧是依据DP的 寻找子问题，然后寻找递归出口。
 * 以下是基础的递归解法，寻找中间结果实现暂存。
 */
public class OneAndZero {
    public int findMaxForm(String[] strs, int m, int n) {
        return findMaxForm(strs,m,n,0);
    }
    public int findMaxForm(String[] strs, int m, int n,int index){
        // 如果 数组空了 返回
        // 如果 m 或者 n 空了 或者小于了，返回
        if (index==strs.length){
            return 0;
        }else {
            String num  = strs[index];
            int[] zeroAndOne  = getZeroAndOneNum(num);
            if (m>=zeroAndOne[0] && n>=zeroAndOne[1]) {
                return Math.max(findMaxForm(strs, m, n, index +1), findMaxForm(strs, m - zeroAndOne[0], n - zeroAndOne[1], index +1)+1);
            }
            else return findMaxForm(strs,m,n,index +1);
        }
    }
    public int[] getZeroAndOneNum(String num){
        int zeroCount = 0;
        int oneCount = 0;
        for (char i :num.toCharArray()){
            if (i=='0') zeroCount++;
            else  oneCount ++;
        }
        int[] returnArray= new int[2];
        returnArray[0]=zeroCount;
        returnArray[1]=oneCount;
        return returnArray;
    }

    public static void main(String[] args) {
        OneAndZero oneAndZero  = new OneAndZero();
        String[] testArray = {"11","11","0","0","10","1","1","0","11","1","0","111","11111000","0","11","000","1","1","0","00","1","101","001","000","0","00","0011","0","10000"};
        System.out.println(oneAndZero.findMaxForm(testArray,90,66,0));
    }
};