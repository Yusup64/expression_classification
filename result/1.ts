const fs = require('fs');
const path = require('path');
/* interface TrainDataChild {
    [props: string]: 
} */
type TrainData = {
    [props: string]: Array<{
        acc: number,
        class: number | string,
    }>
}
let orgData = fs.readFileSync(path.resolve(__dirname, './original_52.json'));
let data: TrainData = JSON.parse(orgData);
for (const key in data) {
    let len = data[key].length;
    let count = 0;

    data[key].forEach(item => {
        if (key == item.class) {
            count++;
        }
    });
    console.log(len, count, count / len)
}
// fs.writeFileSync(path.resolve(__dirname, './500_7.json'), JSON.stringify(data))