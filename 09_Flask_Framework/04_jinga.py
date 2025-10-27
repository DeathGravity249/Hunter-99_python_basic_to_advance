from flask import Flask , render_template,request
# Hey Flask, create a new web app for me, and use this current Python file as the main module."
app=Flask(__name__)

## jinja timplate engine
'''
{{ }} expressing to print output in html 
{% .. . % } condition for loops
{# ... # this is for comments }
'''


@app.route("/")
def welcome():
    return render_template("jinja_.html")


@app.route("/form",methods=["GET","POST"])
def form():
    if request.method=="POST":
        name = request.form["name"]
        return f"Hello {name}"
    return render_template("form.html")


# The approute decorator tells the flask when someone visit
#  this url  it teel to run this function 
# if condition 
@app.route("/successif/<int:score>") 
def new_value(score):
    
    return render_template("new_result.html", results=score)



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