function solution(inputString) {
    let extractNums = inputString.split(/[^\d]+/).filter(x => x.length > 0);
    if (extractNums.length == 0) {
        return 0;
    }
    // console.log(extractNums)
    return extractNums.map(x => parseInt(x)).reduce((x, y) => x+y);
}

