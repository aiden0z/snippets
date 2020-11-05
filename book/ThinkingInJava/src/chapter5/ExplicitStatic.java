package chapter5;

/**
 * Created by lxttx on 16/1/29.
 * 静态成员只会初始化一次, 第一次访问时或者创建第一个对象时被初始化, 且在非静态成员之前被初始化.
 */

class Cup {
    Cup(int marker) {
        System.out.printf("Cup(%d)\n", marker);
    }

    void f(int marker) {
        System.out.printf("f(%d)\n", marker);
    }
}

class Cups {
    static Cup cup1;
    static Cup cup2;

    static {
        cup1 = new Cup(1);
        cup2 = new Cup(2);
    }

    Cups() {
        System.out.println("Cups()");
    }
}


public class ExplicitStatic {
    public static void main(String[] args) {
        System.out.println("Inside main()");
        new Cups();
        System.out.println("////////////////");
        Cups.cup1.f(11);
        System.out.println("////////////////");
        Cups.cup2.f(22);
        System.out.println("////////////////");
        new Cups();
    }
}
