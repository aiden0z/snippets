// Rust 中的每一个引用都有其 生命周期（lifetime），也就是引用保持有效的作用域。
// 大部分时候生命周期是隐含并可以推断的，正如大部分时候类型也是可以推断的一样。
// 类似于当因为有多种可能类型的时候必须注明类型，也会出现引用的生命周期以一些不同方式相关联的情况，
// 所以 Rust 需要我们使用泛型生命周期参数来注明他们的关系，这样就能确保运行时实际使用的引用绝对是有效的。
fn main() {
    println!("Hello, world!");

    // 生命周期的主要目标是避免悬垂引用，它会导致程序引用了非预期引用的数据
    // Rust 编译器有一个借用检查器（borrow checker）用来比较作用域来确保
    // 所有的引用都是有效的。

    // 下面代码将 r 的生命周期标记为 'a 并将 x 的生命周期标记为 'b。
    // 如你所见，内部的 'b 块要比外部的生命周期 'a 小得多。
    // 在编译时，Rust 比较这两个生命周期的大小，并发现 r 拥有生命周期 'a，
    // 不过它引用了一个拥有生命周期 'b 的对象。程序被拒绝编译，
    // 因为生命周期 'b 比生命周期 'a 要小：被引用的对象比它的引用者存在的时间更短。
    // {
    //     let r;
    //     {
    //         let x = 5;
    //         // 这里无法编译通过，因为 x 在来开作用域后将被销毁；
    //         r = &x;
    //     }
    //     println!("r: {}", r);
    // }

    // 下面代码中，假设 x 拥有生命周期 'b，r 拥有生命周期 'a。
    // 这里 x 拥有生命周期 'b，比 'a 要大。
    // 这就意味着 r 可以引用 x：Rust 知道 r 中的引用在 x 有效的时候也总是有效的。

    {
        let x = 5;
        let r = &x;
        println!("r: {}", r);
    }

    let novel = String::from("Call me Ishmael. Some years ago....");
    let first_sentence = novel.split('.').next().expect("Could not find a '.'");
    let i = ImportantExcerpt {
        part: first_sentence,
    };

    println!("{:?}", i);
}

// 由于生命周期的问题以下代码无法编译，
// 因为 Rust 并不知道将要返回的引用是指向 x 或 y。
// 事实上我们也不知道，因为函数体中 if 块返回一个 x 的引用而 else 块返回一个 y 的引用。
// 当我们定义这个函数的时候，并不知道传递给函数的具体值，
// 所以也不知道到底是 if 还是 else 会被执行。我们也不知道传入的引用的具体生命周期，
// 所以也就不能像示例 10-18 和 10-19 那样通过观察作用域来确定返回的引用是否总是有效。
// 借用检查器自身同样也无法确定，因为它不知道 x 和 y 的生命周期是如何与返回值的生命周期相关联的。
// 为了修复这个错误，我们将增加泛型生命周期参数来定义引用间的关系以便借用检查器可以进行分析。
// fn longest(x: &str, y: &str) -> &str {
//     if x.len() > y.len() {
//         x
//     } else {
//         y
//     }
// }

// 可以替换为下面的版本，由于指定了生命周期参数，所以可以正常编译
// 下面的代码通过 'a 指定了 x 和 y 拥有的相同的生命周期
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() {
        x
    } else {
        y
    }
}

// 定义包含引用的结构体，不过这需要为结构体定义中的每一个引用添加生命周期注解。
// 类似于泛型参数类型，必须在结构体名称后面的尖括号中声明泛型生命周期参数，
// 以便在结构体定义中使用生命周期参数。这个注解意味着 ImportantExcerpt
// 的实例不能比其 part 字段中的引用存在的更久。
#[derive(Debug)]
struct ImportantExcerpt<'a> {
    part: &'a str,
}

// 同时使用泛型参数、trait bounds 和 生命周期语法
use std::fmt::Display;

fn longest_with_an_announcement<'a, T>(x: &'a str, y: &'a str, ann: T) -> &'a str
where
    T: Display,
{
    println!("Announcement! {}", ann);
    if x.len() > y.len() {
        x
    } else {
        y
    }
}
