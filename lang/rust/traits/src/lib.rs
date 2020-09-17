// trait 告诉 Rust 编译器某个特定类型有用可能与其他类型共享的功能
// 可以通过 trait 以一种抽象的方式定义共享的行为。可以使用 trait
// bounds 指定泛型是任何拥有特定行为的类型。类似其他语言中的
// interface 概念，但有所不同。
use std::fmt::Display

pub trait Summary {
    fn summarize(&self) -> String;
}

pub struct NewArticle {
    pub headline: String,
    pub location: String,
    pub author: String,
    pub content: String,
}

// 实现 trait
impl Summary for NewArticle {
    fn summarize(&self) -> String {
        format!("{}, by {} {}", self.headline, self.author, self.location)
    }
}

pub struct Tweet {
    pub username: String,
    pub content: String,
    pub reply: bool,
    pub retweet: bool,
}

// 实现 trait
impl Summary for Tweet {
    fn summarize(&self) -> String {
        format!("{}: {}", self.username, self.content)
    }
}

// 需要注意实现当前 crate 之外的 trait

// 另外可以使用 trait 作为参赛
// trait bound 语法，结合了泛型
pub fn notify<T: Summary>(item: T) {
    println!("Breaking news! {}", item.summarize());
}

// 或通过 impl Trait 方式指定
// notify(item1: impl Summary, item2: impl Summary)
// 下面的方式更为简洁
// notify<T: Summary>(item1: T, item2: T)
pub fn new_notify(item: impl Summary) {
    println!("Breaking news! {}", item.summarize());
}

// 可以指定多个 trait
// pub fn notify(item: impl Summary + Disaplay)
// pub fn notify<T: Summary + Display>(item: T)

// 如果有多个 trait 略显混乱
fn some_function<T: Display + Clone, U: Clone + Debug>(t: T, u: U) -> i32 {}

// 可以通过 where 从句简化
fn some_function_new(T, U)(t: T, u: U) -> i32 where T: Display + Clone, U: Clone + Debug {}

// 还可以返回 trait 类型
// 需要注意只能返回单一类型，无法返回多个类型，比如返回 Tweet 或 NewsArticle
fn returns_summarizable() -> impl Summary {}

// 还可以通过 trait bound 限制只为实现了某些 trait 的结构体实现方法
struct Pair<T> {
    x: T,
    y: T,
}

impl<T> Pair<T> {
    fn new(x: T, y: T) -> Self {
        Self{
            x,
            y,
        }
    }
}

// 也可以对任何实现了特定 trait 的类型有条件地实现 trait，比如
impl<T: Display> ToString for T {
}


