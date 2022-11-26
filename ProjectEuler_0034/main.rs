fn main() {
    let mut tot = 0;
    let f = [1,1,2,6,24,120,720,5040,40320,362880];
    for n in 10..10000000 {
        let mut s = 0;
        for c in n.to_string().chars() {
            let d = c as usize - '0' as usize;
            s += f[d];
        }
        if s == n {
            tot += n;
            println!("{}", s);
        }
    }
    println!("total = {}", tot);
}
