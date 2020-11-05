package chapter5;

/**
 * Created by lxttx on 16/1/29.
 * 静态成员只会初始化一次, 第一次访问时或者创建第一个对象时被初始化, 且在非静态成员之前被初始化.
 */
class Bowl {
    Bowl(int marker) {
        System.out.printf("Bowl %d\n", marker);
    }

    void f1(int marker) {
        System.out.printf("f1(%d)\n", marker);
    }
}

class Table {
    static Bowl bowl1 = new Bowl(1);

    Table() {
        System.out.println("Table()");
        bowl2.f1(1);
    }

    void f2(int marker) {
        System.out.printf("f2(%d)\n", marker);
    }

    static Bowl bowl2 = new Bowl(2);
}

class Cupboard {
    Bowl bowl3 = new Bowl(3);
    static Bowl bowl4 = new Bowl(4);

    Cupboard() {
        System.out.println("Cupboard()");
        bowl4.f1(2);
    }

    void f3(int marker) {
        System.out.printf("f3(%d)\n", marker);
    }

    static Bowl bowl5 = new Bowl(5);

}


public class StaticInitialization {
    public static void main(String[] args) {
        System.out.println("Creating new Cupboard() in main");
        new Cupboard();
        System.out.println("Creating new Cupboard() in main");
        new Cupboard();
        table.f2(1);
        cupboard.f3(1);
    }

    static Table table = new Table();
    static Cupboard cupboard = new Cupboard();
}
