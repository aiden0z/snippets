fn main() {
    let mut x = 5;
    println!("The value of x is: {}", x);
    x = 6;
    println!("The value of x is: {}", x);

    another_function(5);

    // 表达式会返回值
    let y = {
        let x = 3;
        x + 1
    };
    println!("The value of y is: {}", y); // output 4
    println!("The value of x is: {}", x); // output 6

    println!("The return value of function five: {}", five());
    plus_one(x);

    // 因为 if 是一个表达式，所以可以在 let 语句右侧使用
    let condition = true;
    let number = if condition { 5 } else { 6 };
    println!("The value of number is: {}", number);

    let mut counter = 0;
    // loop 循环表达式
    let result = loop {
        counter += 1;
        if counter == 10 {
            // break 后还可以接一个可以执行的表达式
            break {
                // 注意不要有分号
                counter * 2
            };
            // 或者是
            // break counter * 2
        }
    };
    println!("The result is {}", result);

    // while 循环
    let mut number = 3;
    while number != 0 {
        println!("{}!", number);
        number = number - 1;
    }

    // for 循环
    let a = [10, 20, 30, 40, 50];
    let mut index = 0;
    while index < 5 {
        println!("the value is: {}", a[index]);
        index = index + 1;
    }
    for element in a.iter() {
        println!("the value is: {}", element);
    }
    for number in (1..4).rev() {
        println!("{}!", number);
    }
}

fn another_function(x: i32) {
    println!("The value of x is: {}", x);
}

// 函数的最后一个表达式是返回值
fn five() -> i32 {
    // 注意结尾分号，是一个表达式
    5
}

fn plus_one(x: i32) -> i32 {
    x + 1
}
