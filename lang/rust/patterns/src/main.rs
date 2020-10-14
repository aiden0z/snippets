fn main() {
    let favorite_color: Option<&str> = None;
    let is_tuesday = false;
    let age: Result<u8, _> = "34".parse();

    // 使用 if let 表达式，如果匹配到了 Some 值
    if let Some(color) = favorite_color {
        println!("color {}", color);
    } else if is_tuesday {
        println!("Tuesday is green day!");
    } else if let Ok(age) = age {
        if age > 30 {
            println!("greate than 30");
        } else {
            println!("less than 30");
        }
    } else {
        println!("not found age")
    }

    // while let 条件循环
    let mut stack = Vec::new();
    stack.push(1);
    stack.push(2);
    stack.push(3);

    // pop 方法取出 vector 的最后一个元素并返回 Some(value)
    // 如果 vector 是空的则返回 None。while 循环只要 pop
    // 返回 Some 就一直执行其块中的代码
    while let Some(top) = stack.pop() {
        println!("found {}", top);
    }

    // for 循环也可以使用模式
    let v = vec!['a', 'b', 'c'];
    for (index, value) in v.iter().enumerate() {
        println!("{} is at index {}", value, index);
    }

    // let 也可以使用模式匹配
    let (x, y, z) = (1, 2, 3);
    println!("found x: {}, y: {}, z: {}", x, y, z);

    // 通过模式匹配参数
    // 这里实际上是使用匿名元祖结构体？
    let point = (3, 5);
    print_coordinates(&point);

    // 模式匹配分为 Refutability 可反驳的和不可反驳的
    // 可反驳的是指，匹配可能失败，比如 if let Some(x) = xx 的匹配
    // 不可反驳的是指，可以匹配任何值，也就是不管如何都会成功，比如以下模式
    // let x = 5，其中的 x 可以匹配到任何值
    // 函数参数、let 语句和 for 循环只能接受不可反驳的模式
    // if let 和 while let 表达式被限制为只能接受可反驳的模式
    // match匹配分支必须使用可反驳模式，除了最后一个分支需要使用能匹配任何剩余值的不可反驳模式

    // 所有模式语法： https://kaisery.github.io/trpl-zh-cn/ch18-03-pattern-syntax.html

    // 匹配字面值
    let x = 1;
    match x {
        1 => println!("one"),
        2 => println!("two"),
        _ => println!("anything"),
    }

    // 匹配命名变量
    let x = Some(5);
    let y = 10;
    match x {
        Some(50) => println!("Got 50"),
        Some(y) => println!("Matched, y = {:?}", y),
        _ => println!("Default case, x = {:?}", x),
    }
    println!("at the end: x = {:?}, y = {:?}", x, y);

    // 多个模式
    // 在 match 表达式中，可以使用 | 语法匹配多个模式，它代表或 (or) 的意思
    let x = 1;
    match x {
        1 | 2 => println!("one or two"),
        3 => println!("three"),
        _ => println!("anything"),
    }

    // 通过 ..= 匹配值的范围
    // ..= 语法允许匹配一个闭区间范围的值
    // 范围值允许使用数字或 char 值，因为编译器会再编译时检查范围不为空
    // char 和 数字值是 Rust 仅有的可以判断范围是否为空的类型
    let x = 5;
    match x {
        // 如果 x 是 1, 2, 3, 4 或 5，第一个分支就会匹配
        1..=5 => println!("one through five"),
        _ => println!("something else"),
    }
    let x = 'c';
    match x {
        'a'..='j' => println!("early ASCII letter"),
        'k'..='z' => println!("late ASCII letter"),
        _ => println!("something else"),
    }

    // 解构并分解值
    // 也可以使用模式来解构接头体、枚举、元祖和引用，以便使用这些值的不同部分

    // 解构结构体
    struct Point {
        x: i32,
        y: i32,
    }

    let p = Point { x: 0, y: 7 };
    // 通过解构结构体获取字段值
    let Point { x: a, y: b } = p;
    // 或
    // let Point{x, y} = p;
    assert_eq!(0, a);
    assert_eq!(7, b);

    // 还可以使用 match 匹配
    match p {
        Point { x, y: 0 } => println!("On the x axis at {} ", x),
        Point { x: 0, y } => println!("On the y axis at {}", y),
        Point { x, y } => println!("On the neither axis: ({}, {})", x, y),
    }

    // 解构枚举

    // 使用 .. 忽略剩余值
    // 对于有多个部分的值，可以使用 .. 语法来只使用部分并忽略其它值。
    struct NewPoint {
        x: i32,
        y: i32,
        z: i32,
    }

    let origin = NewPoint { x: 0, y: 0, z: 0 };
    match origin {
        // 通过使用 .. 省略不使用的值
        NewPoint { x, .. } => println!("x is {}", x),
    }

    let numbers = (2, 4, 8, 16, 32);

    match numbers {
        // 这里用 first 和 last 来匹配第一个和最后一个值。
        (first, .., last) => {
            println!("Some numbers: {}, {}", first, last);
        }
    }

    // 匹配守卫提供的额外条件
    // 匹配守卫（match guard）是一个指定于 match 分支模式之后的额外 if 条件，
    // 它也必须被满足才能选择此分支。匹配守卫用于表达比单独的模式所能允许的更为复杂的情况。
    let num = Some(4);
    match num {
        Some(x) if x < 5 => println!("less than five: {}", x),
        Some(x) => println!("{}", x),
        None => (),
    }

    // @ 绑定
    // at 运算符 (@) 允许我们在创建一个存放值的变量的同时测试其值是否匹配模式
    // 使用 @ 可以在一个模式中同时测试和保存变量值
    enum Message {
        Hello { id: i32 },
    }
    let msg = Message::Hello { id: 5 };
    match msg {
        Message::Hello {
            // 希望测试 Message::hello 的 id 字段是否位于 3..7 范围内，
            // 同时也希望将其绑定到 id_variable 变量以便分支相关联的代码
            // 可以使用它
            id: id_variable @ 3..=7,
        } => println!("Found an id in the range: {}", id_variable),
        Message::Hello { id: 10..=12 } => println!("Found an id in antoher range"),
        Message::Hello { id } => println!("Found some other id: {}", id),
    }
}

// 函数参数模式
fn print_coordinates(&(x, y): &(i32, i32)) {
    println!("current location: ({}, {})", x, y);
}
