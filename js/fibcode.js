const com=document.getElementById('number');
let N;

function tink(){
  let i=1, num1=0/*바로 이전의 수*/, num2=1/*지금 수*/, blank=1/*num2 저장*/
  while (i<N) {
    i++;
    blank=num2;
    num2=blank+num1;
    num1=blank;
  }
  document.getElementById('result').value=num2;
}
