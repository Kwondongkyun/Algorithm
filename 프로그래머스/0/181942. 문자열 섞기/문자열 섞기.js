function solution(str1, str2) {
    var answer = '';
    // for(let i=0;i<str1.length;i++){
    //     answer+=str1[i]+str2[i];
    // }
    return [...str1].map((x, idx)=>x+str2[idx]).join("");
    return answer;
}