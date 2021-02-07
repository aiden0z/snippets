use std::env;
use std::error::Error;
use std::fs::File;
use std::io::prelude::*;
use std::io::BufReader;

fn count_words<R: Read>(input: &mut R) -> Result<u32, Box<dyn Error>> {
    let reader = BufReader::new(input);

    let mut wordcount = 0;
    for line in reader.lines() {
        for _word in line?.split_whitespace() {
            wordcount += 1
        }
    }
    Ok(wordcount)
}
fn main() -> Result<(), Box<dyn Error>> {
    for filename in env::args().skip(1).collect::<Vec<String>>() {
        let mut reader = File::open(&filename)?;
        let wordcount = count_words(&mut reader)?;
        print!("{} {}", wordcount, filename);
    }

    Ok(())
}
