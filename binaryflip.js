function flip() {
    return Math.random() >= 0.5;
}

function randomNumber(n) {
    try {
        if (n > 0 && n < 1000000) {
            if (n === 1) return 0;
            const binaryNumLength = parseInt(n).toString(2).length - 1;
            let randomBinaryNumber = ''
            for (let i = 0; i < binaryNumLength; i++) {
                randomBinaryNumber += flip() ? "1" : "0";
            }
            return parseInt(randomBinaryNumber, 2).toString(10);
        } else {
            throw Error;
        }
    } catch (error) {
        console.error('Invalid input');
    }
}

console.log(randomNumber(500));
console.log(randomNumber(1));
console.log(randomNumber(1000001));
console.log(randomNumber(2));
console.log(randomNumber(500));