package mahb.leetcode.easy;

//写一个单例模式

public class SingleInstant {
    private static SingleInstant instant =  new SingleInstant();;
    private Object Lock;
//   饿汉模式
    public static SingleInstant getHungryInstant(){
        return instant;
    }

    // 懒汉模式
    public  static SingleInstant getLazyInstant1(){
        if (instant==null){
            synchronized (SingleInstant.class){
                if (instant ==null){  // 这一步的检查是因为上一步的加入有两个线程进入了if ，所以在获取锁之后需要在判断一次
                    instant = new SingleInstant();
                }
            }
        }
        return instant;
    }
}

