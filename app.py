from flask import Flask, render_template, send_from_directory, request
import os
import psycopg2
from init_db import init_dba


app = Flask(__name__)
init_dba()
def get_db_connection():
    conn = psycopg2.connect(host='database',
                            database='postgres',
                            user="postgres",
                            password="admin")
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM public.themes;')
    themes = cur.fetchall()
    cur.close()
    conn.close()
    #sasha
    return render_template('index.html', themes=themes)


@app.route('/auth', methods=['post', 'get'])
def auth():
    message =''
    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')   
        conn = get_db_connection()
        cur = conn.cursor()
        try:
            cur.execute('SELECT login, password, carma FROM public.user where login = ' +'\'' + str(login) + '\' and password = '+ '\'' + str(password) + '\';')
            user = cur.fetchall()
            cur.close()
            conn.close()
            if user[0][0]==str(login) and user[0][1]==str(password):
                print('sucsess')
                return render_template('auth.html', user=user)
            else:
                print('unsucsess')
                return render_template('auth.html')
        except:
            message='такого пользователя нет'
            print('такого пользователя нет')
            return render_template('auth.html')
        
        
    return render_template('auth.html')
if __name__=='__main__':
    app.run(host='0.0.0.0')

# @app.route('/media/<path:filename>')
# def media(filename):
    # return send_from_directory(app.config['UPLOAD_FOLDER'], filename, mimetype='image/jpeg')
