use std::io;

#[derive(Debug, Copy, Clone)]
///Тип решения квадратного уравнения
enum SquareRootResult {
    /// Unit-тип
    NoRoots,
    /// Один корень - кортежная структура
    OneRoot(f64),
    /// С-подобная структура 2 корня
    TwoRoots {root1: f64, root2: f64},
    ThreeRoots {root1: f64, root2: f64, root3: f64},
    /// 4 - корня
    FourRoots {root1: f64, root2: f64, root3: f64, root4: f64},
}

#[derive(Debug, Copy, Clone)]
/// Структура, соответствующая уравнению
struct Equation {
    /// Коэффициент A
    c_a: f64,
    /// Коэффициент B
    c_b: f64,
    /// Коэффициент C
    c_c: f64,
    /// Дискриминант
    diskr: f64,
    /// Корни
    res: SquareRootResult,
}

impl Equation {
    /// Функция вычисления корней
    fn calculate_roots(&mut self)->Vec<f64> {
        self.diskr = self.c_b.powi(2) - 4.0 * self.c_a * self.c_c;
        let mut values:Vec<f64>=Vec::new();
        if self.diskr == 0.0 {
            let rt = -self.c_b / (2.0 * self.c_a);
            if rt > 0.0 {
                values.push(rt.sqrt());
                values.push(-rt.sqrt());
            } else if rt == 0.0 {
                values.push(rt);
            }
        }
        else if self.diskr > 0.0 {
            let mut rt1 = (-self.c_b - self.diskr.sqrt()) / (2.0 * self.c_a);
            let mut rt3 = (-self.c_b + self.diskr.sqrt()) / (2.0 * self.c_a);
            if rt1 > 0.0 {
                rt1 = rt1.sqrt();
                values.push(rt1);
                values.push(-rt1);
            }else if rt1 == 0.0 {
                values.push(rt1);
            }
            if rt3 > 0.0 {
                rt3 = rt3.sqrt();
                values.push(rt3);
                values.push(-rt3);
            }else if rt3 == 0.0 {
                values.push(rt3)
            }
        }
        return values
                
    }


    /// Ввод одного коэффициента
    fn get_coef(message: &str) -> f64 {
        return loop {
            let mut input = String::new();
            println!("{}", message);
            io::stdin()
                .read_line(&mut input)
                .expect("Неверно введена строка");
            match input.trim().parse() {
                Ok(val) => {
                    break val;
                }
                Err(_) => {
                    continue;
                }
            }
        };
    }

    fn get_coefs(&mut self) -> () {
        self.c_a = Equation::get_coef("Введите коэффициент A: ");
        self.c_b = Equation::get_coef("Введите коэффициент B: ");
        self.c_c = Equation::get_coef("Введите коэффициент C: ");
    }
}

#[cfg(test)]
mod tests{
    use super::*;
    #[test]
    fn test1(){
        let mut eq = Equation {
            c_a: 1.0,
            c_b: -5.0,
            c_c: -36.0,
            diskr: 0.0,
            res: SquareRootResult::NoRoots,
        };
        eq.diskr = eq.c_b.powi(2) - 4.0 * eq.c_a * eq.c_c;
        let mut need:Vec<f64>=Vec::new();
        need.push(3.0);
        need.push(-3.0);
        assert_eq!(eq.calculate_roots(), need);
    }
    #[test]
    fn test2() {
        let mut eq = Equation {
            c_a: 1.0,
            c_b: -5.0,
            c_c: 4.0,
            diskr: 0.0,
            res: SquareRootResult::NoRoots,
        };
        eq.diskr = eq.c_b.powi(2) - 4.0 * eq.c_a * eq.c_c;
        let mut need:Vec<f64>=Vec::new();
        need.push(1.0);
        need.push(-1.0);
        need.push(2.0);
        need.push(-2.0);
        assert_eq!(eq.calculate_roots(), need);
    }
    #[test]
    fn test3(){
        let mut eq = Equation {
            c_a: -4.0,
            c_b: 16.0,
            c_c: 0.0,
            diskr: 0.0,
            res: SquareRootResult::NoRoots,
        };
        eq.diskr = eq.c_b.powi(2) - 4.0 * eq.c_a * eq.c_c;
        let mut need:Vec<f64>=Vec::new();
        need.push(2.0);
        need.push(-2.0);
        need.push(-0.0);
        assert_eq!(eq.calculate_roots(), need);
    }
}

fn main() {
    use SquareRootResult::*;
    let mut eq = Equation {
        c_a: 0.0,
        c_b: 0.0,
        c_c: 0.0,
        diskr: 0.0,
        res: SquareRootResult::NoRoots,
    };
    eq.get_coefs();
    let values_f:Vec<f64>=eq.calculate_roots();
    eq.res = {
        if values_f.len() == 2 {
            TwoRoots { 
                root1: values_f[0],
                root2: values_f[1],
            }
            
        } else if values_f.len() == 1 {
            OneRoot(values_f[0])
        } else if values_f.len() == 3 {
            ThreeRoots {
                root1: values_f[0],
                root2: values_f[1],
                root3: values_f[2],
            }
        } else if values_f.len() == 4 {
            FourRoots {
                root1: values_f[0],
                root2: values_f[1],
                root3: values_f[2],
                root4: values_f[3],
            }
        } else {
            NoRoots
        }
    };
    let text_res = match eq.res {
        NoRoots => format!("Корней нет"),
        OneRoot(rt) => format!("Один корень => {}", rt),
        TwoRoots { root1, root2 } => format!("Два корня => {} и {}", root1, root2),
        ThreeRoots { root1, root2, root3} => format!("Два корня => {}, {} и {}", root1, root2, root3),
        FourRoots { root1, root2, root3, root4 } => format!("Четыре корня => {}, {}, {}, {}", root1, root2, root3, root4),
    };
    println!("{}", text_res);
}