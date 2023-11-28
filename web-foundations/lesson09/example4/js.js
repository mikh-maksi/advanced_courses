car1_element = document.getElementById("car1");
car2_element = document.getElementById("car2");
car3_element = document.getElementById("car3");


car1_element.addEventListener("click",car1f);
car2_element.addEventListener("click",car2f);
car3_element.addEventListener("click",car3f);

function car1f(){
    alert("Не жовта");
}

function car2f(){
    alert("Жовта!!!");
}
function car3f(){
    alert("Не жовта");
}