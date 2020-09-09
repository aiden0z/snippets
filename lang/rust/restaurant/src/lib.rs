mod front_of_house {
    pub mod hosting {
        pub fn add_to_waitlist() {}

        fn set_at_table() {}
    }

    // Rust 中默认所有项（函数、方法、结构体、枚举、模块和常量）都是私有的。
    // 父模块中的项不能使用子模块中的私有项，但是子模块中的项可以使用他们父模块中的项。
    // 这是因为子模块封装并隐藏了他们的实现详情，但是子模块可以看到他们定义的上下文。
    // 继续拿餐馆作比喻，把私有性规则想象成餐馆的后台办公室：餐馆内的事务对餐厅顾客来说是不可知的，
    // 但办公室经理可以洞悉其经营的餐厅并在其中做任何事情。
    pub mod serving {
        pub fn take_order() {}

        fn server_order() {}

        fn take_payment() {}
    }
}

pub fn eat_at_restaurant() {
    // 绝对路径调用
    crate::front_of_house::hosting::add_to_waitlist();

    // 相对路径调用
    front_of_house::hosting::add_to_waitlist();
}

fn another_server_order() {}

mod back_of_house {
    fn fix_incorrect_order() {
        cook_order();
        // 通过 super 来引用父模块中的函数
        super::another_server_order();
    }
    fn cook_order() {}

    // 如果我们在一个结构体定义的前面使用了 pub ，这个结构体会变成公有的，但是这个结构体的字段仍然是私有的。
    // 如果我们将枚举设为公有，则它的所有成员都将变为公有。注意和结构体的区别。枚举成员默认公有。
    #[derive(Debug)]
    pub struct Breakfast {
        // 可以通过 pub 指定某一个字段公开
        pub toast: String,
        seasonal_fruit: String,
    }

    impl Breakfast {
        pub fn summer(toast: &str) -> Breakfast {
            Breakfast {
                toast: String::from(toast),
                seasonal_fruit: String::from("peaches"),
            }
        }
    }
}

pub fn eat_at_restaurant_with_fruit() {
    let mut meal = back_of_house::Breakfast::summer("Rye");
    meal.toast = String::from("Wheat");
    println!("I'd like {} toast please", meal.toast);
    println!("{:?}", meal);

    // 但是不能更新 meal.seasonal_fruid 字段
    // meal.seasonal_fruit = String::from("blueberries");
}
