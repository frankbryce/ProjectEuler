fn main() {
    // let ar: Vec<i64> = vec![1,8,27,64,125,216];
    // println!("OP([1,8,27,64,125,216], 1, 2) = {}", op(&ar, 1, 2));
    // println!("OP([1,8,27,64,125,216], 1, 3) = {}", op(&ar, 1, 3));
    // println!("OP([1,8,27,64,125,216], 1, 4) = {}", op(&ar, 1, 4));
    // println!("OP([1,8,27,64,125,216], 2, 3) = {}", op(&ar, 2, 3));
    // println!("OP([1,8,27,64,125,216], 2, 4) = {}", op(&ar, 2, 4));
    // println!("OP([1,8,27,64,125,216], 2, 5) = {}", op(&ar, 2, 5));
    // println!("OP([1,8,27,64,125,216], 3, 4) = {}", op(&ar, 3, 4));
    // println!("OP([1,8,27,64,125,216], 3, 5) = {}", op(&ar, 3, 5));
    // println!("OP([1,8,27,64,125,216], 3, 6) = {}", op(&ar, 3, 6));
    // println!("OP([1,8,27,64,125,216], 4, 1) = {}", op(&ar, 4, 1));
    // println!("OP([1,8,27,64,125,216], 4, 2) = {}", op(&ar, 4, 2));
    // println!("OP([1,8,27,64,125,216], 4, 3) = {}", op(&ar, 4, 3));
    // println!("OP([1,8,27,64,125,216], 4, 4) = {}", op(&ar, 4, 4));
    // println!("OP([1,8,27,64,125,216], 4, 5) = {}", op(&ar, 4, 5));
    // println!("OP([1,8,27,64,125,216], 4, 6) = {}", op(&ar, 4, 6));
    // println!("OP([1,8,27,64,125,216], 4, 7) = {}", op(&ar, 4, 7));

    let poly: Vec<i64> = vec![1,683,44287,838861,8138021,51828151,247165843,954437177,3138105961,9090909091,23775972551];
    let mut sum: i64 = 0;
    for i in 1..11 {
        let fits = op(&poly, i as usize, i+1 as usize);
        sum += fits;
        println!("op({},{}) = {}", i, i+1, fits);
    }
    println!("sum of FITs of BOPs: {}", sum);
}

fn op(ar: &Vec<i64>, k: usize, n: usize) -> i64 {
    if k > ar.len() || k < 1 || n < 1 {
        println!("op(len: {}, {},{}) called", ar.len(), k, n);
        panic!("Invalid args to op()");
    }
    if k == 1 {
        return ar[0];
    }
    if n <= k {
        return ar[n-1];
    }
    let mut aiter: Vec<i64> = vec![0; k];
    for i in 0..k {
        aiter[i] = ar[i];
    }
    let mut arec: Vec<i64> = vec![0; k-1];
    for i in 0..k-1 {
        arec[i] = aiter[i+1] - aiter[i];
    }
    for k in k..n {
        let rec = op(&arec, k-1, k);
        aiter.push(aiter[k-1] + rec);
        arec.push(aiter[k] - aiter[k-1]);
    }
    aiter[n-1]
}
