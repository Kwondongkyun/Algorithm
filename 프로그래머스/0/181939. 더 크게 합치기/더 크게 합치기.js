function solution(a, b) {
    var answer = 0;
    let sol1 = Number(String(a)+String(b));
    let sol2 = Number(String(b)+String(a));
    
    answer = sol1>=sol2?sol1:sol2;
    return answer;
}