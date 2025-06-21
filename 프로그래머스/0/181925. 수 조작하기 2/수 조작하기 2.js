function solution(numLog) {
    var answer = '';
    const result = numLog.slice(1).map((val, i)=>val-numLog[i]);
    for(let i=0;i<result.length;i++){
        switch(result[i]){
            case 1:
                answer+="w";
                break;
            case -1:
                answer+="s";
                break;
            case 10:
                answer+="d";
                break;
            case -10:
                answer+="a";
                break;
        }
    }
    
    
    return answer;
}