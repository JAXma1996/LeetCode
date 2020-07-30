package mahb.leetcode.medium;

/**
 * @ProjectName: leetCode
 * @Package: mahb.leetcode.medium
 * @ClassName: CardFlippingGame
 * @Author: mahaibin
 * @Description: ${description}
 * @Date: 2019/12/26 19:52
 * @Version: 1.0
 */
public class CardFlippingGame {
    public static int flipgame(int[] fronts, int[] backs) {
        for (int i = 0; i < fronts.length; i++) {
            int tmp = backs[i];
            backs[i] = fronts[i];
            fronts[i] = tmp;
            int flag = 1;
            for (int j = 0 ; j<i ; j++){
                if (backs[j]==backs[i]){
                    flag=0;
                }
                if (flag==1){

                }
            }
        }
        return 0;
    }

    public static void main(String[] args) {
        int[] fronts = {1,2,4,4,7};
        int[] backs = {1,3,4,1,3};
        System.out.println(flipgame(fronts,backs));
    }
}
