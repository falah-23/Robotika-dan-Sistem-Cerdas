use std::collections::BinaryHeap;

#[derive(Debug, Eq, PartialEq)]
struct Task {
    priority: i32,
    description: String,
}

impl Ord for Task {
    fn cmp(&self, other: &Self) -> std::cmp::Ordering {
        other.priority.cmp(&self.priority) // Mengurutkan tugas berdasarkan prioritas (urutan descending)
    }
}

impl PartialOrd for Task {
    fn partial_cmp(&self, other: &Self) -> Option<std::cmp::Ordering> {
        Some(self.cmp(other))
    }
}

fn main() {
    let mut tasks = BinaryHeap::new(); // Heap untuk menyimpan tugas-tugas

    tasks.push(Task { priority: 2, description: "Charge battery".to_string() });
    tasks.push(Task { priority: 1, description: "Pick up package".to_string() });
    tasks.push(Task { priority: 3, description: "Deliver package".to_string() });

    while let Some(task) = tasks.pop() { // Mengambil dan mengeksekusi tugas berdasarkan prioritas
        println!("Executing task: {} with priority: {}", task.description, task.priority);
    }
}
