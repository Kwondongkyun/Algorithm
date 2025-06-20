function solution(ineq, eq, n, m) {
    // if(ineq === "<"){
    //     if(eq==="=")
    //         return n <= m?1:0;
    //     else if(eq==='!')
    //         return n<m?1:0;
    // }
    // else if(ineq === ">"){
    //     if(eq==="=")
    //         return n >= m?1:0;
    //     else if(eq==="!")
    //         return n>m?1:0;
    // }
    if(eq!=="!")
        return eval(`${n} ${ineq}${eq} ${m}`)?1:0;
    else
        return eval(`${n} ${ineq} ${m}`)?1:0;
}