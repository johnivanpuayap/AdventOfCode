use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() -> io::Result<()> {
    let mut array1 = Vec::new();
    let mut array2 = Vec::new();

    // Open the file
    let path = Path::new("input.txt");
    let file = File::open(&path)?;

    // Read the file line by line
    let lines = io::BufReader::new(file).lines();
    for line in lines {
        if let Ok(line) = line {
            let numbers: Vec<&str> = line.split_whitespace().collect();
            if numbers.len() == 2 {
                array1.push(numbers[0].parse::<i32>().unwrap());
                array2.push(numbers[1].parse::<i32>().unwrap());
            }
        }
    }

    // Sort both arrays
    array1.sort_unstable();
    array2.sort_unstable();

    // Calculate the distance
    let distance: i32 = array1.iter().zip(array2.iter())
        .map(|(&a, &b)| (a - b).abs())
        .sum();

    // Print the distance
    println!("{}", distance);

    Ok(())
}