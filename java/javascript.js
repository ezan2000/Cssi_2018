console.log("Hello World" );
const name = 'Charlie';
console.log('Hello World ' + name);
const age = 16;
console.log(`You are ${age + 1 } years old`);
if(age)
{
 console.log("true");
}
else
{
console.log("false");
}

function greet(name1, name2)
{
  if(name1[0] !== 'A');
  { return;
  }


}
greet('Alice', 'Bob');

const multiplyBy3 =(x,y) => x *3;
// console.log(multiplyBy3(3));
let n = 0;
setInterval(() => {
  n+= 1;
  // console.log(n)
  ;
}, 1000); //every 1000 milliseconds execute function.
const names  = ['Alice', 'Bob', 'Charlie', 'Deborah']
for(let i = 0; i < names.length; i++)
{
  console.log(names[i]);

}
names.forEach((name)) =>
{
  console.log(`forEach: ${ name }`); 
}
