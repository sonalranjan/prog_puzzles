
// https://app.codesignal.com/arcade/intro/level-12/s9qvXv4yTaWg8g4ma

function solution(text) {
    let words = text.split(/[^a-zA-Z]+/).sort((x,y) => - x.length + y.length)
    // console.log(words[0])
    return words[0]     
}

