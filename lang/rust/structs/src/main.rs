#[derive(Debug)]
struct User {
    // 我们使用了自身拥有所有权的 String 类型而不是 &str 字符串 slice 类型 。
    // 这是一个有意而为之的选择，因为我们想要这个结构体拥有它所有的数据，
    // 为此只要整个结构体是有效的话其数据也是有效的。
    // 当然也可以使用 &str 类型，但就需要引入生命周期管理。
    username: String,
    email: String,
    sign_in_count: u64,
    active: bool,
}

#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

// 在结构体的上下文中定义方法，且第一个参数总是 self
impl Rectangle {
    // 这里选择 &self，而不是 self，是因为这里我们不用获取所有权，只是希望
    // 读取结构体中的数据，而不是写入数据。
    // 如果想要在方法中改变调用方法的实例，需要将第一个参数改为 &mut self。
    // 通过仅仅使用 self 作为第一个参数来使方法获取实例的所有权是很少见的；
    // 这种技术通常用在当方法将 self 转换成别的实例的时候，这时我们想要防止调用者在转换之后使用原始的实例。
    fn area(&self) -> u32 {
        self.width * self.height
    }

    fn can_hold(&self, other: &Rectangle) -> bool {
        self.width > other.width && self.height > other.height
    }

    // 还可以定义不以 self 作为参赛的函数。这被称为 关联函数。他们不是结构体的实例。
    // 关联函数经常用于构造函数。

    fn square(size: u32) -> Rectangle {
        Rectangle {
            width: size,
            height: size,
        }
    }
}

// 另外还允许多个 impl 块

impl Rectangle {
    fn echo(&self) {
        println!("{:?}", self);
    }
}

fn main() {
    let user1 = User {
        email: String::from("someone@example.com"),
        username: String::from("username"),
        active: true,
        sign_in_count: 1,
    };

    // 不允许更新字段，因为 user1 未定义为 mut
    // user1.email = "x@b.com".to_string();
    println!("{:?}", user1);

    let mut user1 = User {
        email: String::from("someone@example.com"),
        username: String::from("username"),
        active: true,
        sign_in_count: 1,
    };
    // 定义为 mutable，可以更新字段
    // 同时 rust 不允许只讲某个字段设置为可变
    user1.email = "a@b.com".to_string();
    println!("{:?}", user1);

    // 结构体更新原发，通过 .. 语法指定剩余的未显示
    // 设置值的字段应有与给定实例对应字段相同的值
    let user2 = User {
        email: String::from("another@exmaple.com"),
        username: String::from("another"),
        ..user1
    };
    println!("{:?}", user2);

    // 也可以定义 元组结构体，没有具体的字段名，只有字段类型
    #[derive(Debug)]
    struct Color(i32, i32, i32);
    #[derive(Debug)]
    struct Point(i32, i32, i32);

    let black = Color(0, 0, 0);
    println!("{:?}", black);

    let origin = Point(0, 0, 0);
    println!("{:?}", origin);

    // 也可以定义 类单元结构体(unit-like structs)
    // 没有任何字段，因为类似 ()，即 unit
    // 类单元结构体常常用于想要在某个类型上实现 trait，但不需要
    // 在类型中存储数据的时候发挥作用

    let rect1 = Rectangle {
        width: 30,
        height: 50,
    };
    println!(
        "The area of the rectangle is {} square pixels.",
        rect1.area()
    );

    let rect1 = Rectangle {
        width: 10,
        height: 40,
    };
    let rect2 = Rectangle {
        width: 60,
        height: 45,
    };
    println!("Can rect1 hold rect2? {}", rect1.can_hold(&rect2));

    let squa1 = Rectangle::square(10);
    println!("Square {:?}", squa1);
    squa1.echo();
}
