arr_text = ["Hello","Greatings","Buy-buy" ];

base_element = document.getElementById("base");
console.log(base_element);

d = document.createElement("div");
d.classList = "cell";
d.innerHTML = "Hello";
base_element.appendChild(d);

var n = 0;
btn = document.createElement("button");
btn.innerHTML="Next";
btn.id = "action_button";


base_element.appendChild(btn);
btn.addEventListener("click",next_function);

function next_function(){
    n +=1;
    d.innerHTML = arr_text[n];
}
