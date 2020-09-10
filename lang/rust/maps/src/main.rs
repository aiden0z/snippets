use std::collections::HashMap;

fn main() {
    let mut scores: HashMap<String, i32> = HashMap::new();

    scores.insert(String::from("Blue"), 10);
    scores.insert(String::from("Yellow"), 50);

    println!("{:?}", scores);

    // 使用 collect 方法
    let teams = vec![String::from("Blue"), String::from("Yellow")];
    let initial_scores = vec![10, 50];

    let scores: HashMap<_, _> = teams.iter().zip(initial_scores.iter()).collect();
    println!("{:?}", scores);

    let field_name = String::from("Key");
    let field_value = String::from("Value");
    let mut map = HashMap::new();
    // 下面的代码执行后 map 将获得 field_name 和 field_value 的所有权，导致后续不能再
    // 访问
    // 如果是讲值的引用插入 map，这些值本身就不会移动进哈希 map。
    // 但这些引用只想的值必须至少在 hash map 有效时也是有效的。这就需要引入生命周期的概念
    map.insert(field_name, field_value);
    // println!("{}", field_name);
    println!("{:?}", map);

    // 可以通过 get 来获取相应 key 的 值
    let team_name = String::from("Blue");
    // 注意 score 是一个 Option 类型，这里是 Some(10)
    // 如果没有相应的值，则返回 None
    let score = scores.get(&team_name);
    println!("{:?}", score);

    // 可以使用 for 循环
    for (key, value) in &scores {
        println!("{}, {}", key, value);
    }

    // 覆盖 hash map 中的值
    let mut scores = HashMap::new();
    scores.insert(String::from("Blue"), 10);
    // 覆盖一个值
    scores.insert(String::from("Blue"), 20);
    println!("{:?}", scores);

    // 只有在 key 没有对应值时插入
    // Entry 的 or_insert 方法在键对应的值存在时就返回这个值的可变引用，
    // 如果不存在则将参数作为新值插入并返回新值的可变引用。
    // 这比编写自己的逻辑要简明的多，另外也与借用检查器结合得更好。
    scores.entry(String::from("Yellow")).or_insert(50);
    scores.entry(String::from("Blue")).or_insert(50);
    println!("{:?}", scores);

    // 根据旧值更新一个值
    let text = "hello world worder ful world";
    let mut map = HashMap::new();
    for word in text.split_whitespace() {
        let count = map.entry(word).or_insert(0);
        // 注意返回的 count 是一个可变引用，修改了其值就修改了 map 中的值
        *count += 1;
    }
    println!("{:?}", map);
}
