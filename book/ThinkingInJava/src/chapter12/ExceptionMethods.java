package chapter12;

import java.util.*;

/**
 * Created by lxttx on 16/3/1.
 */
public class ExceptionMethods {
    public static void main(String[] args) {
        try {
            throw new Exception("My Exception");
        } catch (Exception e) {
            System.out.println(e.getMessage());
            System.out.println(e.getLocalizedMessage());
            System.out.println(e);
            e.printStackTrace(System.out);
        }
    }
}
