fn simulate_robot(grid: &Vec<Vec<i32>>, start: (usize, usize), goal: (usize, usize)) {
    if let Some(path) = find_path(grid, start, goal) {
        println!("Robot path: {:?}", path);
        for (x, y) in path {
            println!("Robot moved to: ({}, {})", x, y);
        }
    } else {
        println!("No valid path for the robot.");
    }
}
