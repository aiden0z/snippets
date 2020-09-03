// 在任意给定的时间（同一个作用域内），要么只能有一个可变引用，要么 只能有多个不可变引用
// 引用必须总是有效的（避免悬垂指针）
fn main() {
    // Rust 中的每一个值都有一个被称为其 所有者（owner）的变量。
    // 值在任一时刻有且只有一个所有者。
    // 当所有者（变量）离开作用域，这个值将被丢弃。

    println!("Hello, world!");

    {
        // s 在这里无效, 它尚未声明
        let s = "hello"; // 从此处起，s 是有效的

        // 使用 s
        println!("The s value is : {}", s);
    } // 此作用域已结束，s 不再有效

    let mut s = String::from("hello");
    s.push_str(", world!");
    println!("{}", s);

    // 将 s 的移动到了 s1， s 将不再支持访问
    let s1 = s;
    println!("{},", s1);

    // 不过可以深拷贝 （克隆）s1 的数据，这会复制堆上的所有相应数据
    let s2 = s1.clone();
    println!(
        "s1 = {} address: {:p}, s2 = {}, address: {:p}",
        s1, &s1, s2, &s2
    );

    let s = String::from("hello");
    takes_ownership(s);
    // 无法再使用 s, 下面的代码无法编译
    // println!("{}", s);

    let x = 5;
    // 复制 x 的值到函数，所以后续可以继续使用
    makes_copy(x);
    // 这里可以继续使用 x
    println!("{}", x);

    let s1 = String::from("hello");
    let len = calculate_length(&s1);
    println!("The length of '{}' is {}.", s1, len);

    // 通过 mut 可以获得可变引用，但特定作用域中只能有一个可变引用
    let mut s = String::from("hello");
    let r1 = &mut s;
    println!("{}", r1);
    // 同一个作用域无法拥有第二个可变引用
    // let r2 = &mut s;
    // println!("{}, {}", r1, r2);

    // 但缺可以再不同的作用域中有多个可变引用
    let mut s = String::from("hello");
    {
        let r1 = &mut s;
        println!("{}", r1);
    } // r1 在这里离开了作用域，所以我们完全可以创建一个新的引用

    let r2 = &mut s;
    println!("{}", r2);

    // 同时，rust 不允许同时存在可变和不可变引用
    let mut s = String::from("hello");
    let r1 = &s;
    let r2 = &s;
    // 许多个不可变引用，但不能同时存在可变引用
    //  let r3 = &mut s; // 大问题
    println!("{}, {}", r1, r2);

    // 字符串 slice
    let s = String::from("hello world");
    let hello = &s[0..5];
    let world = &s[6..11];
    println!("{}, {}", hello, world);

    // 字符串字面值就是 slice
    // s 的类型是 &str，指向一个二进制程序特定位置的 slice。这也就是字符串字面值是不可以变的；
    // &str 是一个不可变引用；
    let s = "hello, world";
    println!("{}", s);

    let my_string = String::from("hello world");
    let word = first_word(&my_string[..]);
    println!("{}", word);
    let my_string_literal = "hello world";
    let word = first_word(&my_string_literal[..]);
    println!("{}", word);
    // 因为字符串字面值 就是 字符串 slice，所以可以直接传参
    let word = first_word(my_string_literal);
    println!("{}", word);

    // 也有其他类型的 slice ，比如 &[i32]
    let a = [1, 2, 3, 4, 5];
    let slice = &a[1..3];
    println!("{:?}", slice);
}

// 该函数将获得 some_string 的所有权，但参数被传递给 takes_ownership 后不能在使用
fn takes_ownership(some_string: String) {
    println!("{}", some_string)
}

// 这里因为是 i32 类型，所以会进行值复制
fn makes_copy(some_integer: i32) {
    println!("{}", some_integer)
}

// 接收引用参数，引用允许使用值但不获取所有权
// 获取引用作为函数参数成为 借用 borrowing
fn calculate_length(s: &String) -> usize {
    s.len()
}

// 不允许修改一个引用的值
// fn change(some_string: &String) {
//     some_string.push_str(", world");
// }

// 以下函数也编译不通过
// 原因是由于改返回返回的是 s 的引用，而变量 s 本身在离开 dangle 作用域后将被销魂
// 所以引用就变成了一个吴晓东额指针，rust 编译器将不允许这种情况发生
// fn dangle() -> &String {
//     let s = String::from("hello");

//     &s
// }

fn first_word(s: &str) -> &str {
    let bytes = s.as_bytes();
    for (i, &item) in bytes.iter().enumerate() {
        if item == b' ' {
            return &s[0..i];
        }
    }
    &s[..]
}
