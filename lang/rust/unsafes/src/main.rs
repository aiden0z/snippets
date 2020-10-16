// 通过 unsafe 开启不安全的 Rust 代码块，通常有五类可以在
// 不安全 Rust 中进行而不能用于安全 Rust 的操作
// * 解引用裸指针
// * 调用不安全的函数或方法
// * 访问或修改可变静态变量
// * 访问 union 的字段
// 在真实使用中，应该将不安全的代码进行封装，对外提供安全的 API
fn main() {
    // 不安全的 Rust 有两个被称为 裸指针 的类似引用的新类型，和引用
    // 一样裸指针是不可变或可变的，分别协作 *const T 和 *mut T
    // 这里的星号不是解引用运算符，它是类型名称的一部分。在裸指针的上
    // 下文中，不可变 意味着指针解引用之后不能直接赋值。
    // 裸指针与引用和智能指针的区别在于：
    // * 允许忽略借用规则，可以同时拥有不可变和可变的指针，或多个指向相同位置的指针
    // * 不保证指向有效的内存
    // * 允许为空
    // * 不能实现任何自动清理功能

    // 这里从保证安全的引用来创建的裸指针，可以知道这些特定的裸指针是有效，但是不能对任何裸指针做出如此假设
    let mut num = 5;
    // 下面我们可以同时创建 num 的可变裸指针和不可变裸指针，但在安全的 Rust 中是无法同时穿件可变和不可变引用的
    // 不可变裸指针
    let r1 = &num as *const i32;
    // 可变裸指针
    let r2 = &mut num as *mut i32;

    // 可以在不安全的代码块中对裸指针进行解引用
    unsafe {
        println!("r is: {}", *r1);
        println!("r is: {}", *r2);
    }

    // 但下面的裸指针不确定有效性
    let address = 0x0123456usize;
    let r = address as *const i32;
    // 以下内码允许可能会遇到 segmentation fault
    // unsafe {
    //     println!("new r is: {}", *r);
    // }

    // 如果函数或方法是不安全的，则也必须在 unsafe 代码块中调用这些函数或方法
    unsafe {
        dangerous();
    }

    let mut v = vec![1, 2, 3, 4, 5, 6];
    let r = &mut v[..];
    let (a, b) = split_at_mut(r, 3);
    assert_eq!(a, &mut [1, 2, 3]);
    assert_eq!(b, &mut [4, 5, 6]);

    // Rust 可以使用 extern 与其他语言编写代码交互，有助于创建和使用外部函数接口 （Foreign Function Interface, FFI）
    // extern 中的代码必须在 unsafe 中执行
    unsafe {
        println!("absolute value of -3 according to C: {}", abs(-3));
    }
}

unsafe fn dangerous() {}

// 下面尝试编写一个用于分割 slice 的函数
// 以下代码看起来是合理的，但却无法编译。原因是由于最后一行对同一个 slice
// 进行了两次借用，不符合 Rust 借用规则。但我们可以通过不安全代码实现该功能。
// fn split_at_mut(slice: &mut [i32], mid: usize) -> (&mut [i32], &mut [i32]) {
//     let len = slice.len();

//     assert!(mid <= len);

//     (&mut slice[..mid], &mut slice[mid..])
// }
use std::slice;

// slice::from_raw_parts_mut 函数获取一个裸指针和一个长度来创建一个 slice。
// 这里使用此函数从 ptr 中创建了一个有 mid 个项的 slice。之后在 ptr 上调用
// add 方法并使用 mid 作为参数来获取一个从 mid 开始的裸指针，使用这个裸指针并以
//mid 之后项的数量为长度创建一个 slice。
fn split_at_mut(slice: &mut [i32], mid: usize) -> (&mut [i32], &mut [i32]) {
    let len = slice.len();
    let ptr = slice.as_mut_ptr();
    assert!(mid <= len);

    unsafe {
        (
            slice::from_raw_parts_mut(ptr, mid),
            slice::from_raw_parts_mut(ptr.add(mid), len - mid),
        )
    }
}

// 使用 extern 调用 C 代码
extern "C" {
    fn abs(input: i32) -> i32;
}
