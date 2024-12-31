use std::collections::VecDeque;

// Fungsi utama untuk menemukan jalur dari titik start ke goal dalam grid
fn find_path(grid: &Vec<Vec<i32>>, start: (usize, usize), goal: (usize, usize)) -> Option<Vec<(usize, usize)>> {
    let directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]; // Arah pergerakan (kanan, bawah, kiri, atas)
    let mut queue = VecDeque::new(); // Antrian untuk BFS
    let mut visited = vec![vec![false; grid[0].len()]; grid.len()]; // Menyimpan status kunjungan setiap sel
    let mut parent = vec![vec![None; grid[0].len()]; grid.len()]; // Menyimpan jalur dari setiap sel

    queue.push_back(start);
    visited[start.0][start.1] = true;

    while let Some((x, y)) = queue.pop_front() {
        if (x, y) == goal {
            let mut path = vec![(x, y)];
            let mut current = parent[x][y];

            while let Some((px, py)) = current {
                path.push((px, py));
                current = parent[px][py];
            }

            path.reverse();
            return Some(path);
        }

        for (dx, dy) in directions.iter() {
            let nx = x as isize + dx;
            let ny = y as isize + dy;

            if nx >= 0 && ny >= 0 && nx < grid.len() as isize && ny < grid[0].len() as isize {
                let (nx, ny) = (nx as usize, ny as usize);
                if !visited[nx][ny] && grid[nx][ny] == 0 {
                    visited[nx][ny] = true;
                    parent[nx][ny] = Some((x, y));
                    queue.push_back((nx, ny));
                }
            }
        }
    }

    None
}

fn main() {
    let grid = vec![
        vec![0, 0, 1, 0, 0],
        vec![0, 1, 1, 0, 0],
        vec![0, 0, 0, 0, 0],
        vec![1, 1, 0, 1, 0],
        vec![0, 0, 0, 1, 0],
    ];

    let start = (0, 0);
    let goal = (4, 4);

    if let Some(path) = find_path(&grid, start, goal) {
        println!("Path: {:?}", path);
    } else {
        println!("No path found.");
    }
}
