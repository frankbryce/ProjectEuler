fn main() {
    let mut np: f64 = 1.0;
    let mut dp: f64 = 1.0;
    for n in 10..100 {
        let nc: Vec<_> = n.to_string().chars().collect();
        if nc[1] == '0' { continue; }
        for d in n+1..100 {
            let dc: Vec<_> = d.to_string().chars().collect();
            if dc[0] == nc[1] {
                let n1 = nc[0] as u32 - '0' as u32;
                let d1 = dc[1] as u32 - '0' as u32;
                let diff = (n1 as f64)/(d1 as f64) - (n as f64)/(d as f64);
                if diff < 0.001 && diff > -0.001 {
                    np *= n1 as f64;
                    dp *= d1 as f64;
                    println!("{}/{} = {}/{}", n,d,n1,d1);
                }
            }
            if dc[1] == nc[0] {
                let n1 = nc[1] as u32 - '0' as u32;
                let d1 = dc[0] as u32 - '0' as u32;
                let diff = (n1 as f64)/(d1 as f64) - (n as f64)/(d as f64);
                if diff < 0.001 && diff > -0.001 {
                    np *= n1 as f64;
                    dp *= d1 as f64;
                    println!("{}/{} = {}/{}", n,d,n1,d1);
                }
            }
        }
    }
    println!("{}/{}", np, dp);
}
