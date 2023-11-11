
// let name = '李四'

// let obj = {
//     name: '张三',
//     [name]: 123
// }

// console.log(obj)

// a1, a2, a100
let obj = {}
for (let i = 1;i<=100;i++){
    obj[`a${i}`] = i
}
console.log(obj)
