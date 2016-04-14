package chapter14;

import java.util.*;
/**
 * Created by aiden on 16/4/9.
 */

class Initable {
    static final int staticFinal = 47;
    static final int staticFinal2 =
            ClassInitialization.rand.nextInt(1000);
    static {
        System.out.println("Initializing Initable");
    }
}

class Initable2 {
    static int staticNonFinal = 147;
    static {
        System.out.println("Initializing Initable2");
    }

}

class Initable3 {
    static int staticNonFinal = 74;
    static {
        System.out.println("Initializing Initable3");
    }
}

public class ClassInitialization {
    public static Random rand = new Random(47);

    public static void main(String[] args) throws Exception {

        // 通过 Initable.class 获取 Initable 的 Class 对象引用,不会使 Initable 的 Class 对象马上进行初始化

        Class initable = Initable.class;
        System.out.println("After creating Initable ref");
        // 由于 Initable.staticFinal 是一个编译期常量,所以不需要对 Initable 的 Class 对象进行初始化也可以访问
        System.out.println(Initable.staticFinal);

        // 而 Initable.staticFina2 不是一个编译期常量,所以需要对 Initable 的 Class 对象进行初始化
        System.out.println(Initable.staticFinal2);

        // Initable2.staticNonFinal 不是一个编译期常量,对其访问需要立即初始化 Initable 的 Class 对象
        System.out.println(Initable2.staticNonFinal);

        // Class.forName 会立即初始化类的 Class 对象
        Class initable3 = Class.forName("chapter14.Initable3");
        System.out.println("After creating Initable3 ref");
        System.out.println(Initable3.staticNonFinal);
    }
}
