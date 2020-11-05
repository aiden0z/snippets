package chapter5;

class A {}

/**
 * 数组可变参数
 */
public class VarArgs{
    static void printArray(Object[] args) {
        for(Object obj: args) {
            System.out.println(obj + " ");
        }
    }

    static void printArgs(Object... args) {
        for(Object obj: args)
            System.out.println(obj + " ");
    }

    public static void main(String[] args) {
         printArray(new Object[]{
            new Integer(47), new Float(3.14), new Double(11.11)});

         printArray(new Object[]{"one", "two", "three"});
         printArray(new Object[]{new A(), new A(), new A()});
         printArgs("four", "five", "six");
         printArgs((Object[])new Integer[]{1, 2, 3, 4});
         printArgs();
    }
}

