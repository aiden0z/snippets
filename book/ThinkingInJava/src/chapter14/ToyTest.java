package chapter14;

/**
 * Created by lxttx on 16/3/2.
 */

interface HasBatteries {
}

interface Waterproof {
}

interface Shoots {
}

class Toy {
    Toy() {
    }

    Toy(int i) {
    }
}

class FancyToy extends Toy implements HasBatteries, Waterproof, Shoots {
    FancyToy() {
        super(1);
    }
}


public class ToyTest {
    static void printInfo(Class cc) {
        System.out.printf("Class name: %s, is interface? [%s]\nSimple name: %s\nCanonical name : %s\n",
                cc.getName(), cc.isInterface(), cc.getSimpleName(), cc.getCanonicalName());
    }

    public static void main(String[] args) {
        Class c = null;

        try {
            c = Class.forName("chapter14.FancyToy");
        } catch (ClassNotFoundException e) {
            System.out.println("Can't find FancyToy");
            System.exit(1);
        }

        printInfo(c);

        for (Class face : c.getInterfaces())
            printInfo(face);

        Class up = c.getSuperclass();

        Object obj = null;

        try {
            obj = up.newInstance();
        } catch (InstantiationException e) {
            System.out.println("Cannot instantiate");
            System.exit(1);
        } catch (IllegalAccessException e) {
            System.out.println("Cannot access");
            System.exit(1);
        }
        printInfo(obj.getClass());
    }
}
