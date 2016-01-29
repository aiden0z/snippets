package chapter5;

import java.util.*;

/**
 * Created by lxttx on 16/1/29.
 * 可以通过 `this`调用匹配的构造器，但不能同时调用两次，且只能在构造器中调用另一个构造器，且构造器调用需要置于方法的最开始处，否则编译失败。
 */
public class Flower {
    int petalCount = 0;
    String s = "initial value";
    Flower(int petals) {
        petalCount = petals;
        System.out.println("Constructor w/ int arg only, petalCount=" + petalCount);

    }

    Flower(String ss) {
        System.out.println("Contstructor w/ String arg only, s = " + ss);
        s = ss;

    }

    Flower(String s, int petals) {
        this(petals);
        // this(s);
        this.s = s;
        System.out.println("String & int args");
    }

    Flower() {
        this("hi", 47);
        System.out.println("default constrctor (no args)");

    }

    void printPetalCount() {
       //this(11);
        System.out.print("petalCount = " + petalCount + " s = " + s);
    }

    public static void main(String[] args) {
        Flower x = new Flower();
        x.printPetalCount();
    }

}
