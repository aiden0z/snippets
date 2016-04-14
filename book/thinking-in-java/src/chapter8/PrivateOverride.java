package chapter8;


/**
 * Created by lxttx on 16/4/5.
 * 只有非 private 方法才能被覆盖
 */

public class PrivateOverride {
    private void f() {
        System.out.println("private f()");
    }

    public static void main(String[] args) {
        PrivateOverride po = new Derived();
        po.f();

    }
}

class Derived extends PrivateOverride {
    public void f() {
        System.out.println("public f()");
    }
}
