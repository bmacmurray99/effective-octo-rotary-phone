import sys, os
sys.path.append(os.getcwd())
from custom_modules import sqlsnake
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/', methods = ['GET','POST'] )
def dashboard():
    temp, hum  = sqlsnake.current_data()
    return render_template('dashboard.html', temp = temp, hum =hum)



#this is the post url for updating the web server with growbox data
@app.route('/update', methods = ['POST'])
def update():
    #error = None
    if request.method == 'POST':
    	#must write login function
        sqlsnake.log_data(request.form['time'],request.form['temp'],request.form['hum'],request.form['lights'],request.form['fans'])
        return "Thank You!"

    #error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid


@app.route('/analytics', methods =['GET','POST'])
def analytics():
    rowdata = sqlsnake.get_last_day()
    return render_template('charts.html',rowdata  = rowdata)





#Remote control

"""
@app.route('/control-panel' ,methods = (['GET', 'POST']))
def remote_control():
    relstates = sqlsnake.get_power_states()
    return render_template('controlpanel.html' , relstates = relstates)
"""








if __name__ == "__main__":
    app.run(debug = True)
