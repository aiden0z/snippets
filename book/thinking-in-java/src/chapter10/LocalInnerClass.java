package chapter10;

/**
 * Created by lxttx on 16/4/6.
 * 局部内部类, 位于代码块里的内部类, 最典型的就是位于一个方法体里的内部类
 */

interface Counter {
    int next();
}

public class LocalInnerClass {
    private int count = 0;

    Counter getCounter(final String name) {
        // 局部内部类
        class LocalCounter implements Counter {
            // 可以使用构造器
            public LocalCounter() {
                System.out.println("LocalCounter()");
            }

            public int next() {
                System.out.println(name);
                return count++;
            }
        }

        return new LocalCounter();
    }

    Counter getCounter2(final String name) {
        return new Counter() {

            // 匿名内部类, 只有默认的构造器,不能自定义构造器
            {
                System.out.println("Counter()");
            }

            public int next() {
                System.out.println(name);
                return count++;
            }
        };
    }

    public static void main(String[] args) {
        LocalInnerClass lic = new LocalInnerClass();

        Counter c1 = lic.getCounter("Local inner"),
                c2 = lic.getCounter2("Anonymous inner");

        for (int i = 0; i < 5; i++)
            System.out.println(c1.next());

        for (int i = 0; i < 5; i++)
            System.out.println(c2.next());
    }

}
