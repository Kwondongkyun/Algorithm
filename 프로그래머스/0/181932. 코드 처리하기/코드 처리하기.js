function solution(code) {
    var answer = '';
    let mode = 0;
    
    for(let i=0;i<code.length;i++){
        if(mode===0){
            if(code[i]==="1"){
                mode=1;
                continue;
            }
            else if(i%2===0 && code[i]!=="1"){
                answer+=code[i];
            }
        }else if(mode === 1){
            if(code[i]==="1"){
                mode=0;
                continue;
            }
            else if(i%2===1 && code[i]!=="1"){
                answer+=code[i];
            }
        }
    }
    return answer === ''?"EMPTY":answer;
}