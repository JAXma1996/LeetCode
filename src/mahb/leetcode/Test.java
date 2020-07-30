package mahb.leetcode;

import java.util.Collection;
import java.util.HashMap;
import java.util.Set;

/**
 * @ProjectName: leetCode
 * @Package: mahb.leetcode
 * @ClassName: Test
 * @Author: mahaibin
 * @Description: ${description}
 * @Date: 2019/8/3 11:39
 * @Version: 1.0
 */
public class Test {

    public static void main(String[] args) {
        System.out.println(15 & 3);
        System.out.println(15 & 35);
        System.out.println(15 & 18);
        System.out.println(15 & 17);
        HashMap ne = new HashMap();
        Set keySet  = ne.keySet();
        System.out.println(Integer.toBinaryString("sdf".hashCode()));
        ne.put("test","ss");
        Collection valueSet = ne.values();
        valueSet.remove("ss");
        System.out.println(ne.size());
    }
}
