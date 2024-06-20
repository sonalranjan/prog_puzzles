
// https://app.codesignal.com/arcade/intro/level-12/fQpfgxiY6aGiGHLtv

function solution(matrix) {
    m = new Map();
    for (let i = 0; i < matrix.length-1; i++) {
        for (let j = 0; j < matrix[i].length-1; j++) {
            let tmat = [matrix[i][j], matrix[i][j+1], matrix[i+1][j], matrix[i+1][j+1]].map(x => `${x}`).join('_');
            // console.log(tmat);
            m.set(tmat, 1)
        } 
    }
    return m.size;
}

