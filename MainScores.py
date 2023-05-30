from flask import Flask, render_template
app = Flask(__name__, template_folder='template')
import Utils
@app.route('/')
def home():
       with open(Utils.SCORES_FILE_NAME, 'r') as f:
         score = f.readline()
         if score.isdigit()==True and not f.read(1):
            return render_template('home.html',score=score)
         else:
            error=Utils.BAD_RETURN_CODE
            return render_template('error.html',error=error)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port  =8777)
