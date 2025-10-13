from flask import Flask , render_template,request,redirect,url_for
# Hey Flask, create a new web app for me, and use this current Python file as the main module."
app=Flask(__name__)

## jinja timplate engine
'''
{{ }} expressing to print output in html 
{% .. . % } condition for loops
{# ... # this is for comments }
'''
@app.route("/form",methods=["GET","POST"])
def form():
    if request.method=="POST":
        name = request.form["name"]
        return f"Hello {name}"
    return render_template("form.html")



# The approute decorator tells the flask when someone visit
#  this url  it teel to run this function 

@app.route("/")
def welcome():
    return render_template("index.html")

# if condition 
@app.route("/successif/<int:score>") 
def new_value(score):
    
    return render_template("new_result.html", results=score)


## creating fail url 
@app.route("/fail/<int>:score>")
def fail(score):

    return render_template("new_result.html",results=score)

@app.route("/submit", methods=["POST"])
def submit():
    if request.method == "POST":
        science = float(request.form["science"])
        maths = float(request.form["maths"])
        c = float(request.form["c"])
        data_science = float(request.form["datascience"])

        total_score = (science + maths + c + data_science) / 4
        return redirect(url_for("successess", score=total_score))




#variable rule
@app.route("/successess/<int:score>") 
def successess(score):

    if score>=50:
        status = "Pass"
        grade="A" if score>=80 else "B" if score>=60 else "C"
    else:
        status = "Fail"
        grade="F"
    
    res ={
        "Score":score,
        "Status":status,
        "Grade":grade,
        "Maximum marks ":100,
        "Percentage": f"{score}%"
    }
    return render_template("result_02.html",results=res)


if __name__== "__main__": # the main script run only if it run directly not imported form anywheref
    app.run(debug=True)