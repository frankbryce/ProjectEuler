use std::fmt;
use std::fs;

fn main() {
    let contents = fs::read_to_string("p102_triangles.txt")
        .expect("Should have been able to read the file");
    let mut vals = contents.split(|c| c=='\n' || c==',').peekable();
    let mut cnt: i32 = 0;
    while !vals.peek().is_none() {
        let s = vals.next().expect("expect mod 6 values");
        if s.len() == 0 { break; }
        let x1: f64 = s.parse().unwrap();
        let s = vals.next().expect("expect mod 6 values");
        let y1: f64 = s.parse().unwrap();
        let s = vals.next().expect("expect mod 6 values");
        let x2: f64 = s.parse().unwrap();
        let s = vals.next().expect("expect mod 6 values");
        let y2: f64 = s.parse().unwrap();
        let s = vals.next().expect("expect mod 6 values");
        let x3: f64 = s.parse().unwrap();
        let s = vals.next().expect("expect mod 6 values");
        let y3: f64 = s.parse().unwrap();
        let p1: Point = Point{ x: x1, y: y1 };
        let p2: Point = Point{ x: x2, y: y2 };
        let p3: Point = Point{ x: x3, y: y3 };
        let t: Triangle = Triangle{p1: &p1, p2: &p2, p3: &p3};
        let o: bool = contains_origin(&t);
        if o { cnt += 1; }
        println!("{t}: {o}")
    }
    println!("Total triangles containing origin: {cnt}");
}

fn contains_origin(t: &Triangle) -> bool{
    let l1: bool = origin_on_left(t.p1, t.p2);
    let l2: bool = origin_on_left(t.p2, t.p3);
    let l3: bool = origin_on_left(t.p3, t.p1);
    return l1 == l2 && l2 == l3;
}

fn origin_on_left(p1: &Point, p2: &Point) -> bool {
    if p1.y == p2.y && p1.x == p2.x {
        panic!("Line has the same coords for both points");
    }
    if p1.x == p2.x {
        return (p1.y - p2.y < 0.0) == (0.0 < p1.x);
    }
    let m: f64 = (p1.y - p2.y)/(p1.x - p2.x);
    let y_int: f64 = p1.y - m * p1.x;
    if y_int < 0.001 && y_int > -0.001 { panic!("edge case.. line contains the origin"); }
    return (p1.x < p2.x && y_int < 0.0) || (p1.x > p2.x && y_int > 0.0);
}

struct Point {
    x: f64,
    y: f64,
}

struct Triangle<'a> {
    p1: &'a Point,
    p2: &'a Point,
    p3: &'a Point,
}

impl fmt::Display for Triangle<'_> {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "({},{}),({},{}),({},{})", self.p1.x, self.p1.y, self.p2.x, self.p2.y, self.p3.x, self.p3.y)
    }
}
