package chapter8;

import java.util.*;

/**
 * Created by lxttx on 16/2/19.
 */

class Super {
    public int field = 0;

    public int getField() {
        return field;
    }

}

class Sub extends Super {
    public int field = 1;

    public int getField() {
        return field;
    }

    public int getSuperField() {
        return super.field;
    }

}

public class FieldAccess {
    public static void main(String[] args) {
        Super sup = new Sub();
        System.out.printf("sup.field = %d, sup.getField() = %d\n", sup.field, sup.getField());

        Sub sub = new Sub();
        System.out.printf("sub.field = %d, sub.getField() = %d, sub.getSuperField() = %d", sub.field, sub.getField(), sub.getSuperField());
    }
}
