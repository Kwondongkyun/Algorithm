function solution(a, d, included) {
    var answer = 0;
    for(let i=0;i<included.length;i++){
        answer+=(a+d*i)*Number(included[i]);
    }
    return answer;
}