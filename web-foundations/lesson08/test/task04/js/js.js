arr_headers=['Рік заснування Харківського університету','Заголовок питання 2']
arr_question_text = ['В якому році заснований Харківський університет','Текст питання 2']
arr_y1 = ['1804','Віповідь 1 Питання 2'];
arr_y2 = ['1805','Віповідь 2 Питання 2'];
arr_y3 = ['1933','Віповідь 3 Питання 2'];
arr_y4 = ['1995','Віповідь 4 Питання 2'];




next = document.getElementById("next");
header = document.getElementById("header");
question_number = document.getElementById("question_number");
question_text = document.getElementById("question_text");
y1_text = document.getElementById("y1_text");
y2_text = document.getElementById("y2_text");
y3_text = document.getElementById("y3_text");
y4_text = document.getElementById("y4_text");


btn.addEventListener("click", f_out);
btn1.addEventListener("click", f_out1);
next.addEventListener("click",next_question);

function render(n){
  header.innerHTML=arr_headers[n];
  question_text.innerHTML = arr_question_text[n];
  console.log(y1);
  y1_text.innerHTML = arr_y1[n];
  y2_text.innerHTML = arr_y2[n];
  y3_text.innerHTML = arr_y3[n];
  y4_text.innerHTML = arr_y4[n];
}


function next_question(){
  console.log("Next Question");
  question_number.value = parseInt(question_number.value)+1;
  render(parseInt(question_number.value));
  right.classList.add("hidden");
}

  function f_out (){
    if (y1.checked){
      right.classList.remove("hidden");
      wrong_div.classList.add("hidden");
    }else{
      right.classList.add("hidden");
      wrong_div.classList.remove("hidden");
    }
   
    
  }
  function f_out1 (){
    answer.classList.toggle("hidden");
    btn1.classList.toggle("opend");
  }

render(parseInt(question_number.value));