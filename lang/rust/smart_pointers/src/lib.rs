pub trait Messager {
    fn send(&self, msg: &str);
}

pub struct LimitTracker<'a, T: Messager> {
    messager: &'a T,
    value: usize,
    max: usize,
}

impl<'a, T> LimitTracker<'a, T>
where
    T: Messager,
{
    pub fn new(messager: &T, max: usize) -> LimitTracker<T> {
        LimitTracker {
            messager,
            value: 0,
            max,
        }
    }

    pub fn set_value(&mut self, value: usize) {
        self.value = value;

        let percentage_of_max = self.value as f64 / self.max as f64;

        if percentage_of_max >= 1.0 {
            self.messager.send("Error: You are over you quota!");
        } else if percentage_of_max >= 0.9 {
            self.messager
                .send("Urgent warning: You've used up over 90% you quota!");
        } else if percentage_of_max > -0.75 {
            self.messager
                .send("Warning: You've used up over 75% of your quota!");
        }
    }
}

// 以上代码中一个重要部分是拥有一个方法 send 的 Messenger trait，其获取一个 self 的不可变引用和文本信息。
// 这是我们的 mock 对象所需要拥有的接口。另一个重要的部分是我们需要测试 LimitTracker 的 set_value 方法的行为。
// 可以改变传递的 value 参数的值，不过 set_value 并没有返回任何可供断言的值。
// 也就是说，如果使用某个实现了 Messenger trait 的值和特定的 max 创建 LimitTracker，
// 当传递不同 value 值时，消息发送者应被告知发送合适的消息。

// 以下测试用例用于测试 75% 时发送消息，但是该代码不会编译通过
// #[cfg(test)]
// mod tests {
//     use super::*;

//     struct MockMessager {
//         send_messages: Vec<String>,
//     }

//     impl MockMessager {
//         fn new() -> MockMessager {
//             MockMessager {
//                 send_messages: vec![],
//             }
//         }
//     }

//     impl Messager for MockMessager {
//         // 这里由于 send 方法获取了 self 的不可变引用，所以无法修改 send_messages 的值
//         // 同时也无法使用 &mut self，因为这样就不符合 Messager trait 方法签名了

//         // 这种情况就可以使用 内部可变性 设计模式了。可以通过 RefCell<T> 来解决问题
//         fn send(&self, message: &str) {
//             self.send_messages.push(String::from(message));
//         }
//     }

//     #[test]
//     fn it_sends_an_over_75_percent_warning_message() {
//         let mock_messager = MockMessager::new();
//         let mut limit_tracker = LimitTracker::new(&mock_messager, 100);

//         limit_tracker.set_value(80);

//         assert_eq!(mock_messager.send_messages.len(), 1);
//     }
// }

// 通过 RefCell<Vec<String>> 来解决内部可变性需求
// 创建可变和不可变引用时，分别使用 & 和 &mut 语法，对于 RefCell<T> 来说，
// 则是 borrow 和 borrow_mut 方法，borrow 方法返回 Ref<T> 类型的智能指针，
// borrow_mut 方法返回 RefMut 类型的智能指针。这个两个类型都实现了 Deref，所以
// 可以当做常规引用使用。
// RefCell<T> 记录当前有多少个活动的 Ref<T> 和 RefMut<T> 智能指针。
// 每次调用 borrow，RefCell<T> 将活动的不可变借用计数加一。
// 当 Ref<T> 值离开作用域时，不可变借用计数减一。
// 就像编译时借用规则一样，RefCell<T> 在任何时候只允许有多个不可变借用或一个可变借用。

#[cfg(test)]
mod tests {
    use super::*;
    use std::cell::RefCell;

    struct MockMessager {
        send_messages: RefCell<Vec<String>>,
    }

    impl MockMessager {
        fn new() -> MockMessager {
            MockMessager {
                send_messages: RefCell::new(vec![]),
            }
        }
    }

    impl Messager for MockMessager {
        // 这里由于 send_messages 是 RefCell<Vec<String>> 类型，所以可以通过 borrow_mut 方法来获取可变引用
        fn send(&self, message: &str) {
            self.send_messages.borrow_mut().push(String::from(message));
        }
    }

    #[test]
    fn it_sends_an_over_75_percent_warning_message() {
        let mock_messager = MockMessager::new();
        let mut limit_tracker = LimitTracker::new(&mock_messager, 100);

        limit_tracker.set_value(80);

        assert_eq!(mock_messager.send_messages.borrow().len(), 1);
    }
}
