// 关联类型 （associated types) 是一个将类型占位符与 trait 相关联的方式
// 这样的方法签名中就可以使用这些占位符类型。trait 的实现者会对特定的实现在这个
// 类型的位置指定相应的具体类型。因此可以定义一个使用多种类型的 trait，知道实现此
// trait 时无需知道这些类型具体是什么。

// 一个带有关联类型的 trait 的例子是标准库提供的 Iterator trait。它有一个叫做
// Item 的关联类型来替代遍历值的类型。
// Item 是一个占位类型，同时 next 放大定义表明它返回 Option<Self::Item> 类型
// 的值。这个 trait 的实现者会指定 Item 的具体类型，然后不管实现者指定何种类型
// next 方法都会返回一个包含了此具体类型的值的 Option。
pub trait Iterator {
    type Item;

    fn next(&mut self) -> Option<Self::Item>;
}

// 接着可以为某一种结构体实现 Iterator，比如 Counter 类型

// 这里不适用泛型，是因为如果使用泛型，则需要再某一个实现中标注类型。这是因为我们也可以实现为
// Iterator<String> for Counter 或任何其他类型。通过关联类型，我们只能选择一次 Item 会是
// 什么类型。参考 https://kaisery.github.io/trpl-zh-cn/ch19-03-advanced-traits.html
impl Iterator for Counter {
    type Item = u32;

    fn next(&mut self) -> Option<Self::Item> {}
}

// trait 默认参数
// 这里的 RHS 表示默认类型参数。RHS 是一个泛型类型参数，它用于定义 add 方法中的 rhs 参数。
// 如果实现 Add trait 时不指定 RHS 的具体类型，RHS 的类型将是默认的 Self 类型，也就是在
// 其实现 Add 的类型。
trait Add<RHS = Self> {
    type Output;

    fn add(self, rhs: RHS) -> Self::Output;
}

fn main() {
    println!("Hello, world!");
}
