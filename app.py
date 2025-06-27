from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector
from config import db_config

app = Flask(__name__)
app.secret_key = 'secret123'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/book', methods=['POST'])
def book():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    origin = request.form['origin']
    destination = request.form['destination']
    date_of_journey = request.form['date']
    seats = request.form['seats']

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    query = '''
        INSERT INTO bookings (name, email, phone, origin, destination, date_of_journey, seats)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    '''
    cursor.execute(query, (name, email, phone, origin, destination, date_of_journey, seats))
    conn.commit()
    cursor.close()
    conn.close()
    flash('Reservation done successfully!')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
