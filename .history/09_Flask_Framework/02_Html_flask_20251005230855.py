from flask import Flask
## It creates an instance of the flask class, 
## which will be your WSGI ( Web Server Gateway Interface ) application

## WSGI Application 
app=Flask(__name__)

@app.route("/")  # <-- This means "when the user visits the '/' URL"
def welcome():
    return "<html><H1>Welcome to the "
@app.route("/index")
def index():
    return 
    
# This line check if the file run directly or 
# it is imported from somewhere else 
if __name__=="__main__": 
    app.run(debug=True)