from flask import Flask, render_template, request
import requests
from livereload import Server

app = Flask(__name__)

#@app.route('/')

#def welcome():
 #   return "Hello"

@app.route('/', methods=['GET','POST'])

def facts():
    import numpy as np
    import pandas as pd
    import random
    import time
    data = pd.read_csv('facts.csv')
    df=pd.DataFrame(data , columns = ['Facts'])
    while True:
        dff=df.values.tolist()
        value=random.choices(dff)
        #print(value)
        time.sleep(10)
        return render_template('facts.html',value=value)
        #return " {} ".format(value)
       # return " {} ".format(value)
        #return [(" {} ".format(value)) , render_template('refresh.html')]
        #return " {} ".format(facts())
        #def refresh():
    #return render_template('refresh.html')
    #return " {} ".format(value)
#@app.route('/', methods=['GET','POST'])
#def refresh():
 #   return facts
#@app.route('/facts', methods=['GET','POST'])
#def refresh():
    #return render_template('refresh.html')
#def index():
 #   return 'Hello'
 #   #return render_template('index.html')



if __name__=='__main__':
    server = Server(app.wsgi_app)
    #server.serve()
    server.watch('/Views/*')
    app.run(debug=False)
    app.config['DEBUG'] = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
