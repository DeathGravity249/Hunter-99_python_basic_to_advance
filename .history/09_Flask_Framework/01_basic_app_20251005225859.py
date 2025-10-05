from flask import Flask
## It creates an instance of the flask class, 
## which will be your WSGI ( Web Server Gateway Interface ) application

## WSGI Application 
app=Flask(__name__)

@app.route("/") # 
def welcome():
    return "Welcome to this Flask course . Today i am gettin" \
    "familiar with little bet of web dev , anything that is getting changed" \
    "will be automatically get added as server restart itself   "

@app.route("/index)
    
# This line check if the file run directly or 
# it is imported from somewhere else 
if __name__=="__main__": 
    app.run(debug=True)