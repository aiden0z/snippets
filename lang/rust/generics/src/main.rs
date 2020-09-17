fn largest_i32(list: &[i32]) -> i32 {
    let mut largest = list[0];
    for &item in list.iter() {
        if item > largest {
            largest = item;
        }
    }
    largest
}

fn largest_char(list: &[char]) -> char {
    let mut largest = list[0];

    for &item in list.iter() {
        if item > largest {
            largest = item;
        }
    }

    largest
}

// 使用泛型
// fn largest<T>(list: &[T]) -> T {
//     let mut largest = list[0];

//     for &item in list.iter() {
//         // 由于 item 的 T 类型可能未实现大小比较操作
//         // 所以下面的代码会编译失败
//         if item > largest {
//             largest = item;
//         }
//     }

//     largest
// }

// 还可以使用泛型来定义结构体, 而且只使用了一个泛型
struct Point<T> {
    x: T,
    y: T,
}

// 还可以定义使用多个类型的泛型
struct PointT<T, U> {
    x: T,
    y: U,
}

fn main() {
    let number_list = vec![34, 50, 25, 25, 100, 65];

    let result = largest_i32(&number_list);
    println!("The largest number is {}", result);

    let char_list = vec!['y', 'm', 'a', 'q'];
    let result = largest_char(&char_list);
    println!("The largest char is {}", result);

    let integer = Point { x: 5, y: 10 };
    let float = Point { x: 1.0, y: 4.0 };

    let both_integer = PointT { x: 1, y: 2 };
    let both_float = PointT { x: 1.0, y: 2.0 };
    let integer_and_float = PointT { x: 1, y: 2.0 };
}
