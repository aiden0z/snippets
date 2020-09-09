#[derive(Debug)]
enum IpAddrKind {
    V4,
    V6,
}

#[derive(Debug)]
struct IpAddr {
    kind: IpAddrKind,
    address: String,
}

// 可以使得枚举成员关联到某一种类型
// 每个成员可以处理不同类型和数量的数据
#[derive(Debug)]
enum IpAddrType {
    V4(String),
    V6(String),
}

// 可以将任意类型的数据放入枚举成员中：例如字符串、数字类型或者结构体。甚至可以包含另一个枚举
#[derive(Debug)]
enum Message {
    Quit,
    Move { x: i32, y: i32 },
    Write(String),
    ChangeColor(i32, i32, i32),
}

// 还可以再枚举上定义方法
impl Message {
    fn call(&self) {
        println!("{:?}", self);
    }
}

#[derive(Debug)]
enum UsState {
    Alabama,
    Alaska,
}

// match 模式匹配
enum Coin {
    Penny,
    Nickel,
    Dime,
    Quarter(UsState),
}

fn value_in_cents(coin: Coin) -> u8 {
    match coin {
        Coin::Penny => {
            println!("Lucky penny!");
            1
        }
        Coin::Nickel => 5,
        Coin::Dime => 10,
        // 变量绑定到对应的 UsState 值
        Coin::Quarter(state) => {
            println!("State quarter from {:?}", state);
            25
        }
    }
}

fn plus_one(x: Option<i32>) -> Option<i32> {
    match x {
        None => None,
        Some(i) => Some(i + 1),
    }
}

fn main() {
    let four = IpAddrKind::V4;
    println!("{:?}", four);
    println!("{:?}", IpAddrKind::V6);

    let home = IpAddr {
        kind: IpAddrKind::V4,
        address: String::from("127.0.0.1"),
    };
    println!("{:?}", home);

    let lookback = IpAddr {
        kind: IpAddrKind::V6,
        address: String::from("::1"),
    };
    println!("{:?}", lookback);

    let m = Message::Write(String::from("hello"));
    m.call();

    // 更常用的是 Option<T> 枚举类型
    let some_number = Some(5);
    let some_string = Some("a string");
    // 如果使用 None 而不是 Some，需要高数 Rust Option<T> 是什么类型的，否则编译器
    // 无法推断出 Some 成员保存的值类型
    let absent_number: Option<i32> = None;
    println!("{:?}, {:?}, {:?}", some_number, some_string, absent_number);
    println!("{}, {}", some_string.is_some(), absent_number.is_none());

    let coin = Coin::Penny;
    println!("{}", value_in_cents(coin));
    let coin = Coin::Quarter(UsState::Alabama);
    println!("{}", value_in_cents(coin));

    let five = Some(5);
    let six = plus_one(five);
    let none = plus_one(None);
    println!("{:?}, {:?}", five, none);

    // let some_u8_value = 0u8;
    // match some_u8_value {
    //     1 => println!("one");
    //     2 => println!("two");
    //     3 => println!("three");
    //     4 => println!("four");
    //     8 => println!("8");
    //     // _ 通配符，_ 模式会匹配所有的值。通过将其放到 match 其他分支后面
    //     // 会匹配到所有之前没有指定的可能值。
    //     _ => (),
    // }

    // if let 语法
    let some_u8_value = Some(0u8);
    match some_u8_value {
        Some(3) => println!("three"),
        _ => (),
    }
    // 使用 if let 语法来省略 match 必需需要处理值
    if let Some(3) = some_u8_value {
        println!("three");
    }

    let mut count = 0;

    let coin = Coin::Quarter(UsState::Alabama);
    if let Coin::Quarter(state) = coin {
        println!("State quarter from {:?}", state);
    } else {
        count += 1;
    }
    println!("{}", count);

    let coin = Coin::Penny;
    if let Coin::Quarter(state) = coin {
        println!("State quarter from {:?}", state);
    } else {
        count += 1;
    }
    println!("{}", count);
}
