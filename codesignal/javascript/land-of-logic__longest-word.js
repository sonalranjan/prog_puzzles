function solution(text) {
    let words = text.split(/[^a-zA-Z]+/).sort((x,y) => - x.length + y.length)
    // console.log(words[0])
    return words[0]     
}

