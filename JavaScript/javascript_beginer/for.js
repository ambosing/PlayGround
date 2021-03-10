var even = 0;
var odd = 0;

for (var i = 1; i <= 50; i++){
    if (i % 2 == 0) even += i;
    else odd += i;
}

document.write(even + "\n");
document.write(odd + "\n");
document.write(even + odd);
