function solution(arr, queries) {
    var answer = [];
    for(let i=0;i<queries.length;i++){
        let min=1000000;
        for(let j = queries[i][0];j<=queries[i][1];j++){
            if(arr[j]>queries[i][2]&&arr[j]<min)
                min=arr[j];
        }
        answer.push(min===1000000?-1:min);
    }
    return answer;
}