fn main() {
    // 使用类型注解，因为没有插入任何值，所以 rust 需要从类型注解中推断出需要的类型
    let _v: Vec<i32> = Vec::new();

    // 更常见的做法是使用初始值来创建一个 Vec，而且为了方便 Rust 提供了 vec! 宏
    // 这里的宏为什么没有像函数一样调用？
    let v = vec![1, 2, 3];
    println!("{:?}", v);

    // 必须使用 mut 关键字，因为需要插入值
    let mut v = Vec::new();
    v.push(5);
    v.push(6);
    v.push(7);
    v.push(8);
    println!("{:?}", v);

    // vector 类型离开作用域时会被丢弃，包括元素值也会被清理
    {
        let v = vec![1, 2, 3, 4];
    }

    let v = vec![1, 2, 3, 4, 5];
    let third: &i32 = &v[2];
    println!("The third element is {}", third);

    // get 方法返回 Option<&T> 类型
    match v.get(2) {
        Some(third) => println!("The third element is {}", third),
        None => println!("There is no third element"),
    }

    // 直接索引访问超过长度会触发 panic
    // let does_not_exist = &v[100];
    // 但通过 get 访问，则会返回 None
    let does_not_exist = v.get(100);
    println!("{:?}", does_not_exist);

    // 不能在相同的作用域存在可变和不可变引用
    let mut v = vec![1, 2, 3, 4, 5];
    // v 有了不可变引用
    let first = &v[0];
    // 下面的代码无法执行，因为有了不可变引用的情况下又在进行更新j
    // 这里有在进行更新，所以不行
    // 为什么第一个元素的引用会关心 vector 结尾的变化？
    // 不能这么做的原因是由于 vector 的工作方式：在 vector 的结尾增加新元素时，
    // 在没有足够空间将所有所有元素依次相邻存放的情况下，
    // 可能会要求分配新内存并将老的元素拷贝到新的空间中。
    // 这时，第一个元素的引用就指向了被释放的内存。借用规则阻止程序陷入这种状况。
    // v.push(6);
    println!("The first element is: {}", first);

    let v = vec![100, 32, 57];
    for i in &v {
        println!("{}", i);
    }
}
