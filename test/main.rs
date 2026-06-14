// Adding a rust file for random flex that is not a flex
use std::io;

fn main() {
  let mut input = String::new();
  println!("Hello, World!");
  println!("Say something!");
  io::stdin().read_line(&mut input).expect("Failed to read a line!");
  let input = input.trim_end_matches(&['\r', '\n'][..]).to_string();
  println!("You said \"{}\"", input);
}