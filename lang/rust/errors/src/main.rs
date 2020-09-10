use std::fs::File;
use std::io;
use std::io::ErrorKind;
use std::io::Read;

// 返回错误，略显繁琐。rust 提供了 ? 操作符快速返回 Result::Err 类型
fn read_username_from_file() -> Result<String, io::Error> {
    let f = File::open("hello.txt");

    let mut f = match f {
        Ok(file) => file,
        Err(e) => return Err(e),
    };

    let mut s = String::new();

    match f.read_to_string(&mut s) {
        Ok(_) => Ok(s),
        Err(e) => Err(e),
    }
}

// 比上面的版本简洁很多
fn new_read_username_from_file() -> Result<String, io::Error> {
    let mut f = File::open("hello.txt")?;
    let mut s = String::new();
    f.read_to_string(&mut s)?;
    Ok(s)
}

fn main() {
    let f = File::open("hello.txt");

    let f = match f {
        Ok(file) => file,
        Err(error) => match error.kind() {
            ErrorKind::NotFound => match File::create("hello.txt") {
                Ok(fc) => fc,
                Err(e) => panic!("Problem creating the file: {:?}", e),
            },
            other_error => panic!("Problem opening the file: {:?}", other_error),
        },
    };

    // 或者通过使用闭包的方式简化代码
    let f = File::open("hello.txt").unwrap_or_else(|error| {
        if error.kind() == ErrorKind::NotFound {
            File::create("hello.txt").unwrap_or_else(|error| {
                panic!("Problem creating the file: {:?}", error);
            })
        } else {
            panic!("Problem openting file: {:?}", error);
        }
    });

    // 可以通过 wrap 或者 expect 火速处理 panic
    let f = File::open("hello.txt").unwrap();
    // expect 可以指定 panic 信息
    let f = File::open("hello.txt").expect("Failed to open hello.txt");
}
