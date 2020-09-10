fn main() {
    println!("Hello, world!");

    let strings: Vec<String> = vec![
        String::from("السلام عليكم"),
        String::from("Dobrý den"),
        String::from("Hello"),
        String::from("שָׁלוֹם"),
        String::from("नमस्ते"),
        String::from("こんにちは"),
        String::from("안녕하세요"),
        String::from("你好"),
        String::from("Olá"),
        String::from("Здравствуйте"),
        String::from("Hola"),
    ];

    for i in strings {
        println!("{}", i)
    }

    let mut s = String::from("foo");
    println!("{}", s);
    // 通过 push_str 更新字符串, 类似于 Vec 类型
    s.push_str("bar");
    println!("{}", s);

    // 需要注意 push_str 不需要获取所有权。比如下面的代码 push 后，s2 依然可以访问
    let mut s1 = String::from("foo");
    let s2 = "bar";
    s1.push_str(s2);
    println!("s2 is {}", s2);

    // 可以使用 + 拼接字符串，但和其他语言中有比较大的区别
    let s1 = String::from("hello ");
    let s2 = String::from("world!");
    // 下面的代码中有两点需要注意：
    // 1. 这里使用 &s2 而不是 s2。因为 + 实现的运算符重载方法参数要求是 &str，而这里&s2
    // 却是 &String 类型。这里 Rust 会用一种 解引用强制多态 的技术，将 &String 类型强制转为
    // &str 类型；
    // 2. s1 的所有权发生了变化，其后续再访问。但 s2 可以继续访问；
    let s3 = s1 + &s2;

    // s1 的所有权发生变化，不能在访问
    // println!("{}", s1);
    // s2 可以继续访问
    println!("{}", s2);
    println!("{}", s3);

    // 如果需要拼接多个字符串，更好的做法是使用format! 宏
    let s1 = String::from("tic");
    let s2 = String::from("tac");
    let s3 = String::from("toe");
    let s = format!("{}-{}-{}", s1, s2, s3);
    println!("{}", s);

    // String 底层使用 Vec<u8> 封装，也就是通过UTF8 字节存储字符串数据。
    // 所以获取长度时，是字节的长度，而不是字符的长度
    // 正因为由于是使用的字节存储的数据，所以不应该直接通过 类似 string[i] 的方式进行索引访问
    println!("{}", String::from("hello").len()); // 输出 5
    println!("{}", String::from("你好").len()); // 输出 6

    for c in "你好".chars() {
        println!("{}", c);
    }
    for b in "你好".bytes() {
        println!("{}", b);
    }
}
