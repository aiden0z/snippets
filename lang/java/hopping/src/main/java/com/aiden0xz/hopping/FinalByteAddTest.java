package com.aiden0xz.hopping;

public class FinalByteAddTest {

    public static void main(String[] args) {

        final byte a = 1;
        final byte b = 10;
        // 如果 a 和 b 非 final 则以下代码无法执行，原因是由于 jvm 会自动将 a 和 b 转为 int 类型
        // 而 int 类型相加结果是 int 无法赋值给 byte 类型
        byte c = a + b;

        System.out.printf("%s\n", Integer.toBinaryString(c));
    }

}
