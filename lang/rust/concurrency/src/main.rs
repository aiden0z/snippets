use std::rc::Rc;
use std::sync::mpsc;
use std::sync::Arc;
use std::sync::Mutex;
use std::thread;
use std::time::Duration;

fn main() {
    let handle = thread::spawn(|| {
        for i in 1..10 {
            println!("hi number {} from spawned thread!", i);
            thread::sleep(Duration::from_millis(1));
        }
    });

    for i in 1..5 {
        println!("hi number {} from main thread!", i);
        thread::sleep(Duration::from_millis(1));
    }

    handle.join().unwrap();

    let v = vec![1, 2, 3];

    // 以下线程使用的闭包借用了主线程中的变量，但这样无法编译。
    // 因为 Rust 不知道新线程会执行多久，所以无法推断出 v 的引用是否一致有效。
    // 但如果我们使用 move 关键字，前置闭包获取其使用值的所有权，而不是由 Rust
    // 推断
    // let handle = thread::spawn(|| {
    //     println!("Here's a vector: {:?}", v);
    // });
    let handle = thread::spawn(move || {
        println!("Here's a vector: {:?}", v);
    });
    handle.join().unwrap();

    // 在 Rust 依然可以使用消息传递在线程间传递数据
    // mpsc 多个生产者，单个消费者的缩写（multiple producer, single comsumer)
    let (tx, rx) = mpsc::channel();

    // 创建一个新线程并使用 mov 将 tx 移动到闭包中，这样新创建的线程
    // 就拥有 tx 了。
    let handle = thread::spawn(move || {
        let val = String::from("hi");
        // send 方法返回一个 Result<T, E> 类型
        tx.send(val).unwrap_or_else(|error| {
            println!("found error {}", error);
        });
        // 当通过 send 发送 val 到通道后，val 的所有权以及发生变化无法再打印其值
        // println!("val is {}", val);
    });

    // rx 表示的接收端 Receiver<T> 有两个方法，recv 和 try_recv
    // recv 会阻塞线程执行直到从通道中接收一个值。
    // try_recv 不会阻塞
    let received = rx.recv().unwrap();
    println!("Got: {}", received);
    handle.join().unwrap();

    // 也可以将 rx 接收端当做一个迭代器使用
    let (tx, rx) = mpsc::channel();
    thread::spawn(move || {
        let vals = vec!["hi", "from", "the", "thread"];

        for val in vals {
            tx.send(String::from(val)).unwrap();
            thread::sleep(Duration::from_secs(1));
        }
    });
    for received in rx {
        println!("Got: {}", received);
    }

    // 可以有多个发送者
    let (tx, rx) = mpsc::channel();
    let tx1 = mpsc::Sender::clone(&tx);
    thread::spawn(move || {
        let vals = vec!["hi", "from", "the", "thread1"];
        for val in vals {
            tx1.send(String::from(val)).unwrap();
            thread::sleep(Duration::from_secs(1));
        }
    });
    thread::spawn(move || {
        let vals = vec!["more messages from thread2"];
        for val in vals {
            tx.send(String::from(val)).unwrap();
            thread::sleep(Duration::from_secs(1));
        }
    });
    for received in rx {
        println!("Got: {}", received);
    }

    // 在 Rust 中除了使用通道外，还可以使用共享内存
    // 在某种程度上，任何编程语言中的通道都类似于单所有权，因为一旦将一个值传送到
    // 通道中，将无法再使用这个值。共享内存类似于多所有权：多个线程可以同时访问
    // 相同的内存位置。之前内容中已经介绍过可以借助于智能指针实现共享所有权。
    // 但智能指针还是稍显复杂，在 Rust 中还有更优雅的做法。
    // Mutex 是一种更为场景的共享内存并发原语。

    // 不像其他语言中，Rust 中 Mutex 类型中持有值
    let m = Mutex::new(5);
    {
        // 使用 lock 方法获取锁，以访问互斥器中的数据
        // lock 方法返回 MutexGuard 的智能指针
        // MutexGuard 实现了 Deref 来指向其内部数据，也提供了一个 Drop 实现当
        // MutexGuard 离开作用域时自动释放锁。所以在这段代码结束后，会自动释放锁。
        let mut num = m.lock().unwrap();
        *num = 6;
    }
    println!("m = {:?}", m);

    let mut handles = vec![];

    // 在线程间共享 Mutex<T>
    // 以下代码无法直接编译，原因是由于 counter 会在多个线程中移动所有权，则是不允许的
    // 联想到可以使用 Rc<T> 类型来共享所有权
    // let counter = Mutex::new(0);
    // for _ in 0..10 {
    //     let handle = thread::spawn(move || {
    //         let mut num = counter.lock().unwrap();
    //         *num += 1;
    //     });
    //     handles.push(handle);
    // }

    // 但尝试 Rc<T> 发现依然不行，原因是由于 Rc<T> 不是并发安全的。
    // let counter = Rc::new(Mutex::new(0));
    // for _ in 0..10 {
    //     let counter = Rc::clone(&counter);
    //     let handle = thread::spawn(move || {
    //         let mut num = counter.lock().unwrap();
    //         *num += 1;
    //     });
    //     handles.push(handle);
    // }

    // 所幸 Arc<T> 可用，是一个安全用于并发环境的引用类型。其中
    // A 表示原子性 atomic。
    let counter = Arc::new(Mutex::new(0));

    for _ in 0..10 {
        let counter = Arc::clone(&counter);
        let handle = thread::spawn(move || {
            let mut num = counter.lock().unwrap();
            *num += 1;
        });
        handles.push(handle);
    }

    for handle in handles {
        handle.join().unwrap();
    }
    println!("Result: {}", *counter.lock().unwrap());

    // Rust 有两个概念是内嵌于语言中的 std::marker 中的 Sync 和 Send trait
    // Send 标记 trait 表明类型的所有权可以再线程间传递。

    // Sync 标记 trait 表明一个实现了 Sync 的类型可以安全的在多个线程中拥有其值的引用。
    // 换一种方式讲，对于任意类型 T，如果 &T 是 Send 的话 T 就是 Sync ，这意味着其引用
    // 可以安全的发送给另一个线程。
}
