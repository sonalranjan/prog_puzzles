function solution(inputArray) {
    rollingSum = -5000;
    for (let i = 0; i < inputArray.length-1; i++) {
            if (inputArray.at(i) * inputArray.at(i+1) > rollingSum) {
                rollingSum = inputArray.at(i) * inputArray.at(i+1);
            }
    }
    return rollingSum;
}

