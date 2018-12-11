const a=document.getElementById('number'), b=document.getElementById('return');
var num1, num2, i;
function primnumber(N) {
  num1=N, num2=2, i=0;
  if(num1<=1){
    b.value="1 또는 자연수가 아니다."
  }
  while (num1>num2) {
    if (num1%num2 == 0) {
      b.value="합성수";
    } else {
      num2++;
    }
    console.log("^");
  }
  b.value="소수";
}/*이 소스는 안찬경이 만들었다.*/

function count() {

}
