fn main() {
    let mut sumn = 0;
    'outer: for n in 1000..100000 {
        'inner: for i in 1..((n as f64).sqrt() as i64 + 2) {
            let mut a = [0; 9];
            for c in n.to_string().chars() {
                if c == '0' { continue 'outer; }
                let idx = c as usize - '1' as usize;
                if a[idx] != 0 { continue 'outer; }
                a[idx] = 1;
            }
            if n%i != 0 { continue; }
            for c in i.to_string().chars() {
                if c == '0' { continue 'outer; }
                let idx = c as usize - '1' as usize;
                if a[idx] != 0 {
                    continue 'inner;
                }
                a[idx] = 1;
            }
            let j = n/i;
            for c in j.to_string().chars() {
                if c == '0' { continue 'inner; }
                let idx = c as usize - '1' as usize;
                if a[idx] != 0 {
                    continue 'inner;
                }
                a[idx] = 1;
            }
            let mut pandigital = true;
            for idx in 0..9 {
                if a[idx] != 1 {
                    pandigital = false;
                    break;
                }
            }
            if pandigital {
                sumn += n;
                println!("{} = {} * {}", n, i, j);
                continue 'outer;
            }
        }
    }
    println!("sumn = {}", sumn);
}
