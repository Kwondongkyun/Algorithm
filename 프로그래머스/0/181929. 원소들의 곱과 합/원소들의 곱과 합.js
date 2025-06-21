function solution(num_list) {
    var answer = 0;
    let gob=1;
    let hab=0;
    for(const num of num_list){
        gob*=num;
        hab+=num;
    }
    return gob>hab**2?0:1;
}