// // let count=creatcount();
// // let count1=creatcount();
//      function creatcount(){
//        return{
//             count:0
//             fullName: function(){
//               counter.count++;
//             }
//         }
// }
// counter1.increment()
// console.log(count)









// const test = {
//     prop: 42,
//     func: function() {
//       return this.prop;
//     },
//   };
  
//   console.log(test.func());




const o = {
    f() {
      return this.a + this.b;
    },
  };
  const p = Object.create(o);
  p.a = 1;
  p.b = 4;
  
  console.log(p.f)