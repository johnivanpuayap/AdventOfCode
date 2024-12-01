use std::collections::HashMap;
use std::collections::HashSet;
use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() -> io::Result<()> {
    let lettered_dictionary: HashMap<&str, i32> = [
        ("one", 1),
        ("two", 2),
        ("three", 3),
        ("four", 4),
        ("five", 5),
        ("six", 6),
        ("seven", 7),
        ("eight", 8),
        ("nine", 9),
    ]
    .iter()
    .cloned()
    .collect();
    
    
    // used to check if the char is a starting letter of the numbers
    let valid_letters: HashSet<char> = "otfsevn".chars().collect();
    let mut total_sum = 0;

    let path = Path::new("input.txt");
    let file = File::open(path)?;
    let reader = io::BufReader::new(file);

    for line in reader.lines() {
        let line = line?;
        let mut numbers = Vec::new();
        let mut i = 0;

        while i < line.len() {
            let char = line.chars().nth(i).unwrap();

            if valid_letters.contains(&char) {
                for (num, value) in &lettered_dictionary {
                    if line[i..].starts_with(*num) {
                        numbers.push(*value);
                        break;
                    }
                }
            } else if char.is_digit(10) {
                numbers.push(char.to_digit(10).unwrap() as i32);
            }

            i += 1;
        }

        if !numbers.is_empty() {
            total_sum += numbers[0] * 10 + numbers[numbers.len() - 1];
        }
    }

    println!("{}", total_sum);
    Ok(())
}