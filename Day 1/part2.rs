use std::fs::File;
use std::collections::HashMap;
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

    // Create a HashMap to count the occurrences of each element in array2
    let mut array2_counts = HashMap::new();
    for &num in &array2 {
        *array2_counts.entry(num).or_insert(0) += 1;
    }

    // Calculate the similarity score
    let mut similarity_score = 0;
    for &num in &array1 {
        if let Some(&count) = array2_counts.get(&num) {
            similarity_score += num * count;
        }
    }

    // Print the similarity score
    println!("{}", similarity_score);

    Ok(())
}