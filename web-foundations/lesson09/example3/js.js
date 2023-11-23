up = document.getElementById("btn_up");
down = document.getElementById("btn_down");
left = document.getElementById("btn_left");
right = document.getElementById("btn_right");


up.addEventListener("click",up_function)
down.addEventListener("click",down_function)
left.addEventListener("click",left_function)
right.addEventListener("click",right_function)


cell=document.getElementById("cell");
cell.style.top = "0px"
cell.style.left = "0px"

function up_function(){
    top_level = parseInt(cell.style.top)
    cell.style.top=(top_level-5)+"px";
    check()
}

function down_function(){
    top_level = parseInt(cell.style.top)
    cell.style.top=(top_level+5)+"px";
    check()
}

function left_function(){
    left_level = parseInt(cell.style.left)
    cell.style.left=(left_level-5)+"px";
    check()
}

function right_function(){
    left_level = parseInt(cell.style.left)
    cell.style.left=(left_level+5)+"px";
    check()
}
function check(){
    left_level = parseInt(cell.style.left)
    top_level = parseInt(cell.style.top)
    if ((left_level>=195) && (top_level>=15)){
        alert("In Garage!!!");
    }
}