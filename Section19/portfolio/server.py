from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def index(page_name='/index.html'):
    return render_template(page_name)

def write_to_csv(data):
    email = data['email']
    subject = data['subject']
    message = data['message']
    with open('database.csv', mode='a', newline='') as database:
        csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    print('request.method: ', request.method)
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('thankyou.html')
        except:
            return 'Did not save to database!'

    else:
        return 'Something went wrong!'



