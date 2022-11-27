use num_bigint::BigUint;
use std::mem::replace;

const PREFIX_PANDIGITAL: bool = true;
const SUFFIX_PANDIGITAL: bool = true;

fn main() {
    let mut f0 = BigUint::from(1_134_903_170_u32);
    let mut f1 = BigUint::from(1_836_311_903_u32);
    let mut pow10_ceil_exc = BigUint::from(10_000_000_000_u64);
    let mut pow10_floor_div_10e9 = BigUint::from(10_u32);
    let ten: BigUint = BigUint::from(10_u32);
    let ten_to_the_nine: BigUint = BigUint::from(1_000_000_000_u32);
    let mut k = 46;
    'outer: loop {
        k += 1;
        let f2 = &f0 + &f1;
        if k % 10000 == 0 {
            println!("{f2}: {k}");
        }
        if &f2 >= &pow10_ceil_exc {
            pow10_ceil_exc *= &ten;
            pow10_floor_div_10e9 *= &ten;
        }
        let bot10 = format!("{:09}", &f2 % &ten_to_the_nine);
        let top10 = format!("{:09}", &f2 / &pow10_floor_div_10e9);
        f0 = replace(&mut f1, f2);

        if SUFFIX_PANDIGITAL {
            let mut ar = vec![0; 9];
            for c in bot10.chars() {
                if c == '0' { continue 'outer; }
                let idx = c as usize - '1' as usize;
                if ar[idx] == 1 { continue 'outer; }
                ar[idx] = 1;
            }
        }
        if PREFIX_PANDIGITAL {
            let mut ar = vec![0; 9];
            for c in top10.chars() {
                if c == '0' { continue 'outer; }
                let idx = c as usize - '1' as usize;
                if ar[idx] == 1 { continue 'outer; }
                ar[idx] = 1;
            }
        }
        println!("{}: {k}", &f1);
        return;
    }
}

