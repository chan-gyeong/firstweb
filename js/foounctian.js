const a=document.getElementById('number'), b=document.getElementById('return');

function primnumber(num1) {
  let num2=2, i=0;
  if(num1<=1){
    b.value="1 또는 자연수가 아니다."
    return 1;
  }
  while (num1>num2) {
    if (num1%num2 == 0) {
      b.value="합성수 "+num2;
      return 0;
    } else {
      num2++;
    }
  }b.value="소수"; return 2;
}/*이 소스는 안찬경이 만들었다.*/

function count(num1){
  let num2=2, counter=0;
  while(num1>num2){
    if(primnumber(num2)==2){
      counter++;
    }
    num2++;
  }
  b.value=counter;
  return counter;
}

function nstprime(N) {
  let num=2, counter=0;
  if (N<1) {
    b.value="자연수가 아닙니다. 자연수를 입력해주세요.";
  }
  while (counter<N) {
    if (primnumber(num)==2) {
      counter++;
    }num++;
  }num--;
  b.value=num; return num;
}
