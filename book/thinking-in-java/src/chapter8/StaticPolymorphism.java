package chapter8;

import java.util.*;

/**
 * Created by lxttx on 16/2/19.
 */
class StaticSuper {
    public static String staticGet() {
        return "Base staticGet()";
    }

    public String dynamicGet() {
        return "Base dynamicGet()";

    }

}

class StaticSub extends StaticSuper {
    public static String staticGet() {
        return "Derived staticGet()";
    }

    public String dynamicGet() {
        return "Derived dynamicGet()";
    }

}

public class StaticPolymorphism {
    public static void main(String[] args) {
        StaticSuper sup = new StaticSub();  // Upcase
        System.out.println(sup.staticGet());
        System.out.println(sup.dynamicGet());
    }
}
