@app.route("/quiz",methods=['GET'])
def quiz():
    if request.method == "GET":
        if request.args.get('n') == None:
            n = 0
        else:
            n = int(request.args.get('n'))
    answer=''

    quiz_arr=[]
    quiz_arr.append({"question_arr":["Яка середня заробітна плата Python-розробника в Україні (червень, 2023)?"],"title_arr":["Зарплата розробника на Python"],"a1_arr":["$1200"],"a2_arr":["$2100"],"a3_arr":["$2700"],"a4_arr":["$3200"],"answer_arr":["$2700"],"n_right_answer_arr":["3"],"total_n":"4"})
    quiz_arr.append({"question_arr":["Яка середня заробітна плата JavaScript-розробника в Україні (червень, 2023)?"],"title_arr":["Зарплата розробника на JacaScript"],"a1_arr":["$1000"],"a2_arr":["$1500"],"a3_arr":["$2000"],"a4_arr":["$2500"],"answer_arr":["$2500"],"n_right_answer_arr":["4"],"total_n":"4"})
    quiz_arr.append({"question_arr":["Яка доля розробників в Україні пише на Python (червень, 2023)?"],"title_arr":["Доля розробників на Python"],"a1_arr":["10,2"],"a2_arr":["13,4"],"a3_arr":["15,2"],"a4_arr":["21,6"],"answer_arr":["13,4"],"n_right_answer_arr":["2"],"total_n":"4"})
    quiz_arr.append({"question_arr":["Яка доля розробників в Україні пише на JavaScript?"],"title_arr":["Доля розробників на JavaScript"],"a1_arr":["10,5"],"a2_arr":["19,1"],"a3_arr":["22,7"],"a4_arr":["32,1"],"answer_arr":["19,1"],"n_right_answer_arr":["2"],"total_n":"4"})

    if n<len(quiz_arr):
        answer = quiz_arr[n]
    else:
        answer="Over"

    return answer