from flask import Flask, render_template, request
import random, sqlite3

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def my_form_post():

    conn = sqlite3.connect('data.sqlite')
    cur = conn.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS Challenges (id INTEGER PRIMARY KEY, challenge TEXT)')

    record_ids = []
    cur.execute('SELECT id from Challenges')
    try:
        for record in cur:
            record_ids.append(record[0])
    except:
        print("Unable to read challenges from data.sqlite")
    rnd_index = random.choice(record_ids)

    cur.execute('SELECT challenge FROM Challenges WHERE id=?', (rnd_index,))
    record = cur.fetchone()
    challenge = record[0]

    record_ids = []
    cur.execute('SELECT id from Places')
    try:
        for record in cur:
            record_ids.append(record[0])
    except:
        print("Unable to read places from data.sqlite")
    rnd_index = random.choice(record_ids)

    cur.execute('SELECT place FROM Places WHERE id=?', (rnd_index,))
    record = cur.fetchone()
    place = record[0]

    print(challenge, place)
    return render_template('index.html', challenge = challenge, location = place)
