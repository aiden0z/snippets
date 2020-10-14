// 在 Rust 中实现状态模式
pub struct Post {
    state: Option<Box<dyn State>>,
    content: String,
}

impl Post {
    pub fn new() -> Post {
        Post {
            state: Some(Box::new(Draft {})),
            content: String::new(),
        }
    }

    pub fn add_text(&mut self, text: &str) {
        self.content.push_str(text);
    }

    pub fn content(&self) -> &str {
        // 因为所有 content 的获取规则都保存在了实现了 State triat 的结构体中，
        // 所以这里调用 state 中值的 content 方法并传递 Post 实例作为参数。
        // 这里调用 Option 的 as_ref 方法是因为需要 Option 中值的引用而不是获取
        // 其所有权。因为 state 是一个 Option<Box<State>>, 调用 as_ref 会返回
        // Option<&Box<State>>。
        // 接着调用 unwrap 方法，这里我们知道它永远不会 panic，因为 Post 的所有方法
        // 都确保在他们返回时 state 会有一个 Some 值。
        // 接着就有了一个 &Box<State>，当调用其 content 方法时，解引用强制多态会
        // 作用于 & 和 Box，这样最终会调用实现了 State trait 的类型的 content 方法。
        // 这意味着需要为 State trait 定义增加 content，这也放置根据所处状态返回什么内容
        // 的逻辑的地方。
        self.state.as_ref().unwrap().content(self)
    }

    pub fn request_review(&mut self) {
        // 调用 take 方法将 state 字段中的 Some 取出并留下一个 None，这使得
        // 我们将 state 值移出而不是借用它。
        if let Some(s) = self.state.take() {
            self.state = Some(s.request_review())
        }
    }

    pub fn approve(&mut self) {
        if let Some(s) = self.state.take() {
            self.state = Some(s.approve())
        }
    }
}

trait State {
    fn request_review(self: Box<Self>) -> Box<dyn State>;
    fn approve(self: Box<Self>) -> Box<dyn State>;

    fn content<'a>(&self, _post: &'a Post) -> &'a str {
        ""
    }
}

struct Draft {}
impl State for Draft {
    fn request_review(self: Box<Self>) -> Box<dyn State> {
        Box::new(PendingReview {})
    }

    fn approve(self: Box<Self>) -> Box<dyn State> {
        self
    }
}

struct PendingReview {}
impl State for PendingReview {
    fn request_review(self: Box<Self>) -> Box<dyn State> {
        self
    }

    fn approve(self: Box<Self>) -> Box<dyn State> {
        Box::new(Published {})
    }
}

struct Published {}
impl State for Published {
    fn request_review(self: Box<Self>) -> Box<dyn State> {
        self
    }

    fn approve(self: Box<Self>) -> Box<dyn State> {
        self
    }

    // 需要使用生命周期标识，因为这里 self 和 post 需要有一样的生命周期
    // 这里获取 post 的引用作为参赛，并返回 post 一部分的引用，所以返回的
    // 引用的周末周期与 post 参数相关。
    fn content<'a>(&self, post: &'a Post) -> &'a str {
        &post.content
    }
}

// 以上状态模式的一个缺点是会发现一些重复逻辑。为了消除他们，可以尝试为 State
// trait 中返回 self 的 request_review 和 approve 方法增加默认实现，不过
// 这会违反对象安全性，因为 trait 不知道 self 具体是什么。我们希望将 State
// 作为一个 trait 对象，所以需要其方法是对象安全的。
// 所谓对象安全具体解释如下。
// 只有对象安全（object safe）的 trait 才可以组成 trait 对象。围绕所有使得
// trait 对象安全的属性存在一些复杂的规则，不过在实践中，值涉及两条规则。
// 如果一个 trait 中的所有方法有如下属性时，则该 trait 是对象安全的：
// * 返回值类型不为 Self
// * 方法没有任何泛型类型参数
// Self 关键字是我们要实现 trait 或方法的类型的别名。对象安全对于 trait 对象是必须
// 的，因为一旦了有了trait对象，就不再知晓实现该 trait 的具体类型是什么。如果
// trait 方法返回具体的 Self 类型，但是 trait 对象忘记了其真正的类型，那么方法
// 就不可能使用已经忘却的原始具体类型。同理对于泛型参数来说，当使用 trait 时会放入
// 具体的类型参数，此具体类型变成了实现该 trait 的类型的一部分。当使用 trait 对象
// 时期具体类型被抹去了，故无从得知放入泛型参数类型的类型是什么了。
// 一个 triat 的方法不是对象安全的例子是标准库中的 Clone trait。Clone trait 的
// clone 方法参数签名看起来像是：
// pub trait Clone {
//     fn clone(&self) -> Self;
// }
// 更多信息参考： https://github.com/rust-lang/rfcs/blob/master/text/0255-object-safety.md
