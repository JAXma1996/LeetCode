package mahb.leetcode.easy;

/**
 * @ProjectName: leetCode
 * @Package: mahb.leetcode.easy
 * @ClassName: RansomNote
 * @Author: mahaibin
 * @Description:
 * Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.
 *
 * Each letter in the magazine string can only be used once in your ransom note.
 *
 * Note:
 * You may assume that both strings contain only lowercase letters.
 *
 * canConstruct("a", "b") -> false
 * canConstruct("aa", "ab") -> false
 * canConstruct("aa", "aab") -> true
 * @Date: 2019/12/18 18:19
 * @Version: 1.0
 */
public class RansomNote {
    public static boolean canConstruct(String ransomNote, String magazine) {
        //由于只是26位字母,所以可以使用一个长度26的数组存放目标字符串饿各字符位数, 复杂度为n
        int[] ransomNoteTarget = new int[26];
        char[] magazineArray=magazine.toCharArray();
        for (int i = 0; i < magazineArray.length; i++) {
            ransomNoteTarget[magazineArray[i]-'a']++;
        }
        char[] ransomNoteArray = ransomNote.toCharArray();
        for (int i=0 ;i<ransomNoteArray.length;i++){
            if((--ransomNoteTarget[ransomNoteArray[i]-'a'])<0){
                return false;
            }
        }
         return true;
    }

    public static void main(String[] args) {
        System.out.println(canConstruct("a","b")); ;
    }
}
