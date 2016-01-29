package chapter5;

/**
 * Created by lxttx on 16/1/29.
 * 在类的内部，数据成员（变量）定义的顺序决定了初始化的顺序。即使变量散布于方法定义之间，它们也会在任何方法（包括构造器）被调用之前得到初
 * 始化。在方法中，没有初始化的变量不能直接使用。
 */
class Window {
    Window(int marker) {
        System.out.println("Window(" + marker + ")");
    }
}

class House {
    Window w1 = new Window(1);

    House() {
        System.out.println("House()");
        w3 = new Window(33);

    }

    Window w2 = new Window(2);

    void f() {
        System.out.println("f()");
    }

    Window w3 = new Window(3);
}

public class OrderOfInitialization {
    public static void main(String[] args) {
        House h = new House();
        h.f();
    }

}
