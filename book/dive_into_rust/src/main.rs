use std::rc::Rc;
use std::cell::RefCell;

pub trait Double {
    fn double(self: &Self) -> Self;
}

impl Double for i32 {
    fn double(&self) -> i32 {*self * 2}
}

fn test<'a>(arg: &'a String) -> &'static str{
    println!("found arg: {:?}", arg);
    "hello world"
}

fn main() {

    let shared_vec = Rc::new(RefCell::new(vec![1, 2, 3]));
    let shared1 = shared_vec.clone();
    let shared2 = shared1.clone();
    shared1.borrow_mut().push(4);
    println!("{:?}", shared_vec.borrow());
    shared2.borrow_mut().push(5);
    println!("{:?}", shared_vec.borrow());

    let c = String::from("haha");
    let x: &'static str = test(&c);
    println!("found result: {}", x);


    println!("size of i8 {}", std::mem::size_of::<i8>());
    println!("size of () {}", std::mem::size_of::<()>());
    println!("size of char {}", std::mem::size_of::<char>());

    let x = 1_i64;
    let mut y: u64 = 1;

    let raw_mut = &mut y as *mut u64 as *mut i64 as *mut i128;
    unsafe {
        * raw_mut = -1;
    }
    println!("{:X} {:X}", x, y);
}
