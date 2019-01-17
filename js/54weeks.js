let year=2018, week=2;
for(let i=0;i<100;i++){
  if(week%7==0) console.log(year);
  if(year%4==0&&(year%100||year%400==0)) week++;
  year++, week++;
}
