const title=document.getElementById("title")
document.write("it works.")
function working(event) {
  console.log(event);
}
title.addEventListener("click", working);
