function solution(arr, queries) {
    var answer = [];
    // let num=0;
    // for(let i=0;i<queries.length;i++){
    //     num=arr[queries[i][0]];
    //     arr[queries[i][0]]=arr[queries[i][1]];
    //     arr[queries[i][1]]=num;
    // }
    for([a,b] of queries){
        [arr[a],arr[b]]=[arr[b],arr[a]];
    }
    return arr;
}

