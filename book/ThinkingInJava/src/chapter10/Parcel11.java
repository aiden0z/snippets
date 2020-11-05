package chapter10;

/**
 * Created by lxttx on 16/4/6.
 * 嵌套类,声明为 static 的类
 */
public class Parcel11 {

    private static class ParcelContents implements Contents {
        private int i = 11;

        public int value() {
            return i;

        }
    }

    protected static class ParcelDestination implements Destination {
        private String label;

        private ParcelDestination(String whereTo) {
            label = whereTo;
        }

        public String readLabel() {
            return label;
        }

        public static void f() {

        }

        static int x = 10;

        static class AnotherLevel {
            public static void f() {

            }

            static int x = 10;
        }
    }

    public static Destination destination(String s) {
        return new ParcelDestination(s);
    }

    public static Contents contents() {
        return new ParcelContents();
    }

    public static void main(String[] args) {
        Contents c = contents();
        Destination d = destination("Tasmania");
    }
}
