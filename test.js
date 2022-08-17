let t = 0;
const timelist = [];
while (t < 2400) {
  timelist.push(t);
  if ((t - 50) % 100 === 0) {
    t += 50;
  } else if (t - 50 === 0) {
    t += 50;
  } else {
    t += 10;
  }
}

console.log(timelist);
