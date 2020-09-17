// trait 告诉 Rust 编译器某个特定类型有用可能与其他类型共享的功能
// 可以通过 trait 以一种抽象的方式定义共享的行为。可以使用 trait
// bounds 指定泛型是任何拥有特定行为的类型。类似其他语言中的
// interface 概念，但有所不同。

pub trait Summary {
    fn summarize(&self) -> String;
}

fn main() {
    println!("Hello, world!");
}
