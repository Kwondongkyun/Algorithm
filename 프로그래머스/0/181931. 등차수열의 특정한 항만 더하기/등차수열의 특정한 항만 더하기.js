function solution(a, d, included) {
    var answer = 0;
    for(let i=0;i<included.length;i++){
        answer+=(a+d*i)*included[i];
    }
    return answer;
}