function solution(num_list) {
    const last=num_list.at(-1);
    const secondLast=num_list.at(-2);
    
    // if(last>secondLast)
    //     num_list.push(last-secondLast);
    // else
    //     num_list.push(last*2);
    
    return [...num_list, last>secondLast?last-secondLast:last*2];
}