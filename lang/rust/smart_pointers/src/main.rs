// 指针 （pointer）是一个包含内存地址的变量的通用概念。
// 这个地址引用，或 “指向”（points at）一些其他数据。Rust 中最常见的指针是第四章介绍的
// 引用（reference）。引用以 & 符号为标志并借用了他们所指向的值。
// 除了引用数据没有任何其他特殊功能。它们也没有任何额外开销，所以应用得最多。

// 智能指针（smart pointers）是一类数据结构，他们的表现类似指针，
// 但是也拥有额外的元数据和功能。智能指针的概念并不为 Rust 所独有；其起源于
// C++ 并存在于其他语言中。Rust 标准库中不同的智能指针提供了多于引用的额外功能。
// 本章将会探索的一个例子便是 引用计数 （reference counting）智能指针类型，其允许数据有多个所有者。
// 引用计数智能指针记录总共有多少个所有者，并当没有任何所有者时负责清理数据。

// 在 Rust 中，普通引用和智能指针的一个额外的区别是引用是一类只借用数据的指针；
// 相反，在大部分情况下，智能指针拥有他们指向的数据。
// 实际上 String 和 Vec<T> 都可以被称之为智能指针。

// 智能指针通常使用结构体实现。智能指针区别于常规结构体的显著特性在于其实现了
// Deref 和 Drop trait。Deref trait 允许智能指针结构体实例表现的像引用一样，
// 这样就可以编写既用于引用、又用于智能指针的代码。
// Drop trait 允许我们自定义当智能指针离开作用域时运行的代码。

// 常用的智能指针
// Box<T>，用于在堆上分配值
// Rc<T>，一个引用计数类型，其数据可以有多个所有者
// Ref<T> 和 RefMut<T>，通过 RefCell<T> 访问。（ RefCell<T> 是一个在运行时而不是在编译时执行借用规则的类型）。

use std::ops::Deref;
use std::rc::Rc;

#[derive(Debug)]
enum List {
    // 通过 Box 解决递归引用的问题，这样 Rust 能够知道每一个 List 占用多少内存空间
    Cons(i32, Box<List>),
    Nil,
}

// 实现 Deref trait 允许重载 解引用运算符（Dereference operator）
struct MyBox<T>(T);

impl<T> MyBox<T> {
    fn new(x: T) -> MyBox<T> {
        MyBox(x)
    }
}

impl<T> Deref for MyBox<T> {
    // 定义该 trait 的关联类型
    type Target = T;

    fn deref(&self) -> &T {
        &self.0
    }
}

// 实现 Drop trait，每当值离开作用域时自动执行 Drop trait 的 drop 方法
struct CustomSmartPointer {
    data: String,
}

impl Drop for CustomSmartPointer {
    fn drop(&mut self) {
        println!("Dropping CustomSmartPointer with data {}", self.data);
    }
}

// Rc<T> 类型用于实现被多个地方引用的引用类型, Rc<T> 只能用于单线程场景
// 在 Rust 中其实就是指共享同一个变量的所有权
// 比如安装 Cons 的定义以下代码无法编译，因为 b 和 c 共享了 a 的所有权，但我们可以使用 Rc<T> 实现需求
//
// let a = Cons(5,
//     Box::new(Cons(10,
//         Box::new(Nil))));
// let b = Cons(3, Box::new(a));
// let c = Cons(4, Box::new(a));
// 现在每一个 Cons 变量包含一个值和指向一个 List 的 Rc<T>。
enum RcList {
    Cons(i32, Rc<RcList>),
    Nil,
}

// 内部可变性（Interior mutability）是 Rust 中的一个设计模式，
// 它允许你即使在有不可变引用时也可以改变数据，这通常是借用规则所不允许的。为了改变数据，
// 该模式在数据结构中使用 unsafe 代码来模糊 Rust 通常的可变性和借用规则。
// Rust 所有权借用规则：
// 1. 在任意给定时刻，只能拥有一个可变引用或任意数量的不可变引用之一；
// 2. 引用必须总是有效的。
// 通过 RefCell<T> 可以在运行时检查借用规则
// 不同于 Rc<T>， RefCell<T> 代表其数据的唯一的所有权。
// 对于引用和 Box<T>，借用规则的不可变性作用于编译时。对于 RefCell<T>，这些不可变性
// 作用于 运行时。对于引用，如果违反这些规则，会得到一个编译错误。而对于 RefCell<T>
// 如果违反这些规则程序则会 panic 并退出。
// 在编译时检查借用规则的优势是这些错误将在开发过程的早期被捕获，同时对运行时没有性能影响，
// 因为所有的分析都提前完成了。为此，在编译时检查借用规则是大部分情况的最佳选择，这也正是其为何是 Rust 的默认行为。
// RefCell<T> 正是用于当你确信代码遵守借用规则，而编译器不能理解和确定的时候。
// 类似于 Rc<T>，RefCell<T> 只能用于单线程场景。如果尝试在多线程上下文中使用RefCell<T>，会得到一个编译错误。
// 选择 Box<T>，Rc<T> 和 RefCell<T> 的理由：
// Rc<T> 允许相同的数据有多个所有者，Box<T> 和 Refcell<T> 有单一所有者；
// Box<T> 允许在编译时执行不可变或可变借用检查，Rc<T> 仅允许在编译时执行不可变借用检查，RefCell<T> 允许在运行时执行不可变或可变借用检查；
// 因为 RefCell<T> 允许在运行时执行可变借用检查，所以我们可以在即使 RefCell<T> 自身是不可变的情况下修改其内部的值；
// 在不可变值内部改变值就是 内部可变性 模式。

// 可以节后 Rc<T> 和 RefCell<T> 来拥有多个可变数据所有者
// RefCell<T> 的一个常见用法是与 Rc<T> 结合。回忆一下 Rc<T> 允许对相同数据有多个所有者，
// 不过只能提供数据的不可变访问。如果有一个储存了 RefCell<T> 的 Rc<T> 的话，
// 就可以得到有多个所有者 并且 可以修改的值了

use std::cell::RefCell;

#[derive(Debug)]
enum MutList {
    Cons(Rc<RefCell<i32>>, Rc<MutList>),
    Nil,
}

use crate::List::{Cons, Nil};
use crate::MutList::{Cons as MutCons, Nil as MutNil};
use crate::RcList::{Cons as RcCons, Nil as RcNil};

fn main() {
    // 使用 box 在堆上存储数据
    let b = Box::new(5);
    println!("{}", b);

    let list = Cons(1, Box::new(Cons(2, Box::new(Cons(3, Box::new(Nil))))));
    println!("{:?}", list);

    // Box<T> 支持解引用
    let x = 5;
    let y = Box::new(x);

    assert_eq!(5, x);
    assert_eq!(5, *y);

    let x = 5;
    let y = MyBox::new(x);

    assert_eq!(5, x);
    // 由于实现 Deref trait，所以可以解引用
    // 每次当我们在代码中使用 * 时， * 运算符都被替换成了 *(y.deref())
    // 先调用 deref 方法再接着使用 * 解引用的操作，且只会发生一次，不会对 * 操作符无限递归替换，
    // 解引用出上面 i32 类型的值就停止了
    assert_eq!(5, *y);

    let m = MyBox::new(String::from("Rust"));

    // 以下代码是可执行的，这里是由于 解引用强制多态 （deref coercions) 的原因
    // 这里使用 &m 调用 hello 函数，其为 MyBox<String> 值的引用。因为 MyBox<T> 实现了 Deref trait，
    // Rust 可以通过 deref 调用将 &MyBox<String> 变为 &String。
    // 标准库中提供了 String 上的 Deref 实现，其会返回字符串 slice，这可以在 Deref 的 API 文档中看到。
    // Rust 再次调用 deref 将 &String 变为 &str，这就符合 hello 函数的定义了。
    hello(&m);

    // 如果 Rust 没有实现解引用多态，为了使得 &MyBox<String> 类型的值调用 hello，
    // 需要编写下面的代码
    // (*m) 将 MyBox<String> 解引用为 String。接着 & 和 [..] 获取了整个 String 的字符串 slice 来
    // 匹配 hello 的签名。
    hello(&(*m)[..]);

    // 除了 Deref trait 重载不可变引用的 * 运算符
    // Rust 提供了 DerefMut trait 用于重载可变引用的 * 运算符
    // Rust 在发现类型和 trait 实现满足 3 种情况会进行解引用强制多态：
    // * 当 T: Deref<Target=U> 时从 &T 到 &U
    // * 当 T: DerefMut<Target=U> 时从 &mut T 到 &mut U
    // * 当 T: Deref<Target=U> 时从 &mut T 到 &U

    let c = CustomSmartPointer {
        data: String::from("my stuff"),
    };
    let d = CustomSmartPointer {
        data: String::from("other stuff"),
    };

    println!("CustomSmartPointers created.");

    // 使用 RcList 实现共享所有权
    // 当创建 b 时，不同于获取 a 的所有权，这里会克隆 a 所有包含的 Rc<List>，这会将引用计数从 1 增加到 2并
    // 允许 a 和 b 共享 Rc<List> 中数据的所有权。创建 c 时也会克隆 a，这会将引用计数从 2 增加为 3。
    // 每次调用 Rc::clone，Rc<List> 中数据的引用计数都会增加，直到有零个引用之前其数据都不会被清理。
    let a = Rc::new(RcCons(5, Rc::new(RcCons(10, Rc::new(RcNil)))));
    // Rc::clone 实现不像大部分类型的 clone 实现那样对所有数据进行深拷贝。Rc::clone 只会增加引用计数。
    let b = RcCons(3, Rc::clone(&a));
    let c = RcCons(4, Rc::clone(&a));

    // 可以通过 Rc::strong_count 获取引用计数
    let a = Rc::new(RcCons(5, Rc::new(RcCons(10, Rc::new(RcNil)))));
    println!("count after creating a = {}", Rc::strong_count(&a));
    let b = RcCons(3, Rc::clone(&a));
    println!("count after creating b = {}", Rc::strong_count(&a));
    {
        let c = RcCons(4, Rc::clone(&a));
        println!("count after creating c = {}", Rc::strong_count(&a));
    }
    println!(
        "count after c goes oout of scope = {}",
        Rc::strong_count(&a)
    );

    let value = Rc::new(RefCell::new(5));

    let a = Rc::new(MutCons(Rc::clone(&value), Rc::new(MutNil)));
    let b = MutCons(Rc::new(RefCell::new(6)), Rc::clone(&a));
    let c = MutCons(Rc::new(RefCell::new(10)), Rc::clone(&a));
    *value.borrow_mut() += 10;
    println!("a after = {:?}", a);
    println!("b after = {:?}", b);
    println!("c after = {:?}", c);
}

fn hello(name: &str) {
    println!("hello {}!", name);
}
