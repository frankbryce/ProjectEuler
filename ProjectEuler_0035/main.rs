fn main() {
    let mut total = 13;  // 13 circular primes below 100
    'outer: for n in 101..1000000 {
        if !is_prime(n) { continue 'outer; }
        let nc: Vec<_> = n.to_string().chars().collect();
        for s in 1..nc.len() {
            let mut na: Vec<_> = nc[nc.len()-s..].to_vec();
            let nb: Vec<_> = nc[..nc.len()-s].to_vec();
            na.extend(&nb);
            let nt: String = na.iter().collect();
            let ntn: i32 = nt.parse().unwrap();
            if !is_prime(ntn) { continue 'outer; }
        }
        println!("Circular Prime: {}", n);
        total += 1;
    }
    println!("Total circular primes below 1 million: {}", total);
}

fn is_prime(n: i32) -> bool {
    if n <= 1 { return false; }
    if n == 2 || n == 3 { return true; }
    if n % 2 == 0 { return false; }
    for f in (3..((n as f64).sqrt() as i32 + 2)).step_by(2) {
        if n % f == 0 { return false; }
    }
    return true;
}
