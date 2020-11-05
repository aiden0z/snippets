package chapter22;

import java.lang.annotation.Inherited;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;

public class InheritDemo {
    // Inherited 注解用于指定子类需要同样使用父类的注解
    @Inherited
    @Retention(RetentionPolicy.RUNTIME)
    static @interface Test {
    }

    @Test
    static class Base {
    }

    static class Child extends Base {
    }

    public static void main(String[] args) {
        System.out.println(Child.class.isAnnotationPresent(Test.class));
    }
}
