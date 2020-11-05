package chapter14;

/**
 * Created by lxttx on 16/3/2.
 */

class Candy {
    static {
        System.out.println("Loading Candy");
    }
}

class Gum {
    static {
        System.out.println("Loading Gum");
    }
}

class Cookie {
    static {
        System.out.println("Loading Cookie");
    }
}

public class SweetShop {
    public static void main(String[] args) {
        System.out.println("inside main");
        new Candy();
        System.out.println("after creating Candy ");
        try {
            // 将加载 Gum 类,生成 Gum 的类对象,这个过程中会执行 static 代码
            Class.forName("chapter14.Gum");
            // Class.forName("Gum");
        } catch (ClassNotFoundException e) {
            System.out.println("Couldn't find Gum");
        }
        System.out.println("After Class.forName(\"Gum\")");
        new Cookie();
        System.out.println("After creating Cookie");

    }
}
