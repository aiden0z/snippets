package chapter10;

/**
 * Created by lxttx on 16/4/6.
 * 该例子展示了外围类实现一个借口与内部类实现接口之间的区别.
 * Callee1 是常用的简单解决方案. 而 Callee2 继承自 MyIncrement ,虽然实现了 increment() 方法,但是这里和接口 Incrementable 完全
 * 没有关系,所以可以通过内部类实现 Incrementable, 有点类似于 adapter 设计模式.
 */

interface Incrementable {
    void increment();
}

class Callee1 implements Incrementable {

    private int i = 0;

    public void increment() {
        i++;
        System.out.println(i);
    }
}


class MyIncrement {
    public void increment() {
        System.out.println("other operation");
    }

    static void f(MyIncrement mi) {
        mi.increment();

    }
}

class Callee2 extends MyIncrement {
    private int i = 0;

    public void increment() {
        super.increment();
        i++;
        System.out.println(i);
    }

    private class Closure implements Incrementable {
        public void increment() {
            // 调用外围类的同名方法
            Callee2.this.increment();
        }
    }

    Incrementable getCallbackReference() {
        return new Closure();
    }

}

class Caller {
    private Incrementable callbackReference;

    Caller(Incrementable cbh) {
        callbackReference = cbh;
    }

    void go() {
        callbackReference.increment();
    }
}

public class Callbacks {
    public static void main(String[] args) {
        Callee1 c1 = new Callee1();
        Callee2 c2 = new Callee2();
        MyIncrement.f(c2);

        Caller caller1 = new Caller(c1);
        Caller caller2 = new Caller(c2.getCallbackReference());

        caller1.go();
        caller1.go();
        caller2.go();
        caller2.go();
    }
}
