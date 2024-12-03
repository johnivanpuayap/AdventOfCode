use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() -> io::Result<()> {
    let path = Path::new("input1.txt");
    let file = File::open(path)?;
    let reader = io::BufReader::new(file);

    let mut values: Vec<String> = Vec::new();
    for line in reader.lines() {
        let line = line?;
        values.push(line.trim().to_string());
    }

    let mut total_sum = 0;

    for entry in values {
        let mut numbers = Vec::new();

        for char in entry.chars() {
            if char.is_digit(10) {
                numbers.push(char.to_digit(10).unwrap() as i32);
            }
        }

        if !numbers.is_empty() {
            total_sum += numbers[0] * 10 + numbers[numbers.len() - 1];
        }
    }

    println!("{}", total_sum);
    Ok(())
}