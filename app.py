from flask import Flask, make_response, render_template, request

answers = {
    "flag1" : "haha_caesar_cipher_is_easy",
    "flag2" : "inspect_element_huh?",
    "flag3" : "bruh_i_hate_metadata",
    "flag4" : "this_is_why_we_dont_use_get",
    "flag5" : "first_time_seeing_http_headers?",
    "flag6" : "final_boss_xss"
}

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')





@app.route('/task1', methods=["GET", "POST"])
def task1():
    flag1 = request.form.get("flag1")

    if flag1 == answers["flag1"]:
        return render_template("task1.html", answer=True)
    elif flag1:
        return render_template("task1.html", answer=False)
    
    return render_template("task1.html", answer="")

@app.route('/task2', methods=["GET", "POST"])
def task2():
    flag2 = request.form.get("flag2")

    if flag2 == answers["flag2"]:
        return render_template("task2.html", answer=True)
    elif flag2:
        return render_template("task2.html", answer=False)

    return render_template("task2.html", answer="")

@app.route('/task3', methods=["GET", "POST"])
def task3():
    flag3 = request.form.get("flag3")

    if flag3 == answers["flag3"]:
        return render_template("task3.html", answer=True)
    elif flag3:
        return render_template("task3.html", answer=False)

    return render_template("task3.html", answer="")

@app.route('/task4')
def task4():
    flag4 = request.args.get("FLAG")

    if flag4 == answers["flag4"]:
        return render_template("task4.html", answer=True)
    elif flag4:
        return render_template("task4.html", answer=False)

    return render_template("task4.html", answer="")

@app.route('/task5', methods=["GET", "POST"])
def task5():
    flag5 = request.form.get("flag5")

    resp = make_response(
        render_template("task5.html", answer=True if flag5 == answers["flag5"] else False if flag5 else "")
    )

    resp.headers["FLAG"] = answers['flag5']
    return resp


@app.route('/task6', methods=["GET", "POST"])
def task6():
    flag6 = request.args.get("flag6")

    if flag6 == answers["flag6"]:
        return render_template("task6.html", answer=True)
    elif flag6:
        return render_template("task6.html", answer=False, query=flag6)

    return render_template("task6.html", answer="")





if __name__ == '__main__':
    app.run(debug=True)