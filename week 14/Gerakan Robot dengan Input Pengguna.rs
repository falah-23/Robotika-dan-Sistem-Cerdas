use std::io;

fn main() {
    let mut position = (0, 0); // Posisi awal robot

    loop {
        println!("Current position: {:?}", position);
        println!("Enter move (up, down, left, right) or 'exit':");

        let mut input = String::new();
        io::stdin().read_line(&mut input).unwrap(); // Membaca input dari pengguna
        let input = input.trim();

        match input {
            "up" => position.1 += 1,
            "down" => position.1 -= 1,
            "left" => position.0 -= 1,
            "right" => position.0 += 1,
            "exit" => break, // Keluar dari loop jika pengguna mengetik 'exit'
            _ => println!("Invalid input."), // Menampilkan pesan jika input tidak valid
        }
    }
}
