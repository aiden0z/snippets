#[cfg(test)]
mod tests {
    #[test]
    fn it_works() {
        assert_eq!(2 + 2, 4)
    }

    #[test]
    fn another() {
        panic!("Make this eat fail");
    }

    // 还可以通过 should_panic 注解
    #[test]
    #[should_panic(expected = "Panic")]
    fn test_panic() {
        panic!("Panic")
    }

    // 还可以通过 Result<T, E> 用于测试
    #[test]
    fn test_result() -> Result<(), String> {
        if 2 + 2 == 4 {
            Ok(())
        } else {
            Err(String::from("two plus two does equal four"))
        }
    }
}
