use std::collections::HashSet;

fn main() {
    let mut l: Vec<i32> = vec![];
    let mut sum: i32 = 1000000000;
    for m1 in 1..64 {
      println!("{m1}");
      add_to(&mut l, m1);
      let mut m2 = l.iter().max().unwrap()+1;
      while m2 < 128 {
        add_to(&mut l, m2);
        m2 = l.iter().max().unwrap()+1;
        let mut m3 = l.iter().max().unwrap()+1;
        while m3 < m1+m2 {
          add_to(&mut l, m3);
          m3 = l.iter().max().unwrap()+1;
          let mut m4 = l.iter().max().unwrap()+1;
          while m4 < m1+m2 {
            add_to(&mut l, m4);
            m4 = l.iter().max().unwrap()+1;
            let mut m5 = l.iter().max().unwrap()+1;
            while m5 < m1+m2+m3-m4 {
              add_to(&mut l, m5);
              m5 = l.iter().max().unwrap()+1;
              let mut m6 = l.iter().max().unwrap()+1;
              while m6 < m1+m2+m3-m5 {
                add_to(&mut l, m6);
                m6 = l.iter().max().unwrap()+1;
                add_to(&mut l, m6);
                if l.iter().max().unwrap() < &(m1+m2) {
                  if l.iter().sum::<i32>() < sum {
                    sum = l.iter().sum::<i32>();
                    println!("################# {:?}",l);
                  }
                }
                l.pop();
                l.pop();
              }
              l.pop();
            }
            l.pop();
          }
          l.pop();
        }
        l.pop();
      }
      l.pop();
    }
}

fn add_to(l: &mut Vec<i32>, min: i32) {
    if l.len() == 0 { l.push(min); return; }
    let mut sums: HashSet<i32> = vec![0].into_iter().collect();
    for n in l.iter() {
        let mut adds: Vec<i32> = vec![];
        for s in &sums {
            if sums.contains(&(*n+s)) { panic!("bad set"); }
            adds.push(*n+s);
        }
        for a in adds {
            sums.insert(a);
        }
    }
    let mut n = min;
    loop {
        let mut can_add = true;
        for s in &sums {
            if sums.contains(&(n+s)) {
                can_add = false;
                break;
            }
        }
        if can_add { l.push(n); return; }
        n += 1;
    }
}

