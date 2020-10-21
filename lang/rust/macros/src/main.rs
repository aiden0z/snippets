// Rsut 提供了一个强大的宏系统，可以进行元编程（metaprogramming)。
// 宏并不产生函数调用，而是展开成源码，并和程序的其余部分一起编译。Rust
// 又有一点和 C 以及其他语言都不同。那就是 Rust 的宏会展开为抽象语法
// 树 （AST，abstract syntax tree)，而不是像字符串预处理那样直接
// 替换成代码，这样就不会产生无法预料的优先权错误。

// 定义一个简单的宏名称为 say_hello
macro_rules! say_hello {
    // () 表示此宏不接受任何参数
    () => {
        // 此宏将展开成以下代码
        println!("Hello");
    };
}

// 宏的参数使用一个美元符号 $ 作为前缀，并使用一个指示符 (designator) 来注明类型
macro_rules! create_function {
    // 此宏接受一个 ident 指示符表示的参数，并创建一个名为 $func_name 的函数
    // ident 指示符用于变量名或函数名
    // 此外有效的类型有 ident, block, stmt, expr, pat, ty, lifetime, literal, path, meta, tt, item, vis
    ($func_name: ident) => {
        fn $func_name() {
            // stringify! 宏把 ident 转换成字符串
            println!("You called {:?}()", stringify!($func_name))
        }
    };
}

create_function!(foo);
create_function!(bar);

macro_rules! print_result {
    // 此宏接受一个 expr 类型的表达式，并将它作为字符串连同其
    // 结果一起打印出来
    // expr 指示符表示表达式
    ($expression: expr) => {
        println!("{:?} = {:?}", stringify!($expression), $expression)
    };
}

// 宏在参数列表中可用用 + 来表示一个参数可能出现一次或多次
// 使用 * 来表示该参数可能出现零次或多次
// 下面的列子中，把模式这样：$(...),+ 包围起来，就可以匹配一个或多个
// 用逗号隔开的表达式。另外注意到宏定义的最后一个分支可以不用分号作为结束
// min! 将求出任意储量的参数的最小值
macro_rules! find_min {
    ($x: expr) => {
        $x
    };

    ($x: expr, $($y: expr), +) => {
        std::cmp::min($x, find_min!($($y), +))
    }
}

fn main() {
    say_hello!();

    foo();
    bar();

    print_result!(1u32 + 1);
    print_result!({
        let x = 1u32;
        x * x + 2 * x - 1
    });
    print_result!(String::from("hello"));

    println!("{}", find_min!(1u32));
    println!("{}", find_min!(1u32 + 2, 2u32));
    println!("{}", find_min!(5u32, 2u32 * 3, 4u32));
}
