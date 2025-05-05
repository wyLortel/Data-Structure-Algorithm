let a = 87;
let b = 70;
let c = 100;
let d = 55;

let average = (a + b + c + d) / 4 ;

let arr = [87 , 70 , 100 , 55];
let average2 = 0;

for (let i = 0; i < arr.length; i++){
    average2 += arr[i];
}

average2 /= arr.length;

console.log(average)
console.log(average2)