from flask import Flask, render_template, request, session, url_for, flash, redirect
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)

app.secret_key = "manasesija"

@app.route('/')
def index():
    return render_template('index.html') 
    
@app.route('/par_mums')
def par_mums():
    return render_template('par mums.html')

@app.route('/kontakti')
def kontakti():
    return render_template('kontakti.html')
  

@app.route('/sveiciens')
def sveiciens():
    return render_template('sveiciens.html')

@app.route('/pamati_sintakse')
def pamati_sintakse():
    return render_template('pamati_sintakse.html')

@app.route('/portfolio_lapa')
def portfolio_lapa():
    return render_template('portfolio_lapa.html')

@app.route('/map')
def map_view():
    return render_template('map.html')

@app.route('/par_mums_lapa')
def par_mums_lapa():
    return render_template('par_mums_lapa.html')

@app.route('/parmums')
def parmums():
    return render_template('parmums.html')


@app.route('/adopte_miluli')
def adopte_miluli():
    return render_template('adopte_miluli.html')

@app.route('/kontaktinformacija')
def kontaktinformacija():
    return render_template('kontaktinformacija.html')


@app.route('/mainigie')
def mainigie():
    vards = "Anna"
    vecums = 20	
    vecums2 = vecums + vecums
    return render_template('mainigie.html', vards = vards, vecums = vecums,
    vecums2 = vecums2)

@app.route('/datu_tipi')
def datu_tipi():
    teksts = "Sveika pasaule!"
    skaitlis = 10
    decimals = 10.5
    saraksts = [1, 2, 3, 4, 5]
    mans_dict = {"vards": "Anna", "vecums": 20}
    mans_kopa = {1, 2, 3, 4, 5}
    return render_template('datu_tipi.html' ,teksts=teksts, skaitlis=skaitlis, 
                           decimals=decimals, saraksts=saraksts, mans_dict=mans_dict,
                          mans_kopa=mans_kopa)

@app.route('/operatori')
def operatori():
    a = 10
    b = 3
    summa =  a + b
    starpiba = a - b
    reizinajums = a * b
    dalijums = a / b
    atlikums = a % b
    vienads = (a == b)
    return render_template('operatori.html', summa=summa, starpiba=starpiba,
                           reizinajums=reizinajums,dalijums=dalijums, atlikums=atlikums,
                           vienads=vienads)

@app.route('/kontroles_strukturas')
def kontroles_strukturas():
    x = 3
    if x > 5:
         rezultats = "x ir lielāks par 5"
    else:
        rezultats = "x ir mazāks par 5"
    for_cikla_rezultats = [i for i in range(6, 31)]
    while_cikla_rezultats = []
    y = 0
    while y < 10:
        while_cikla_rezultats.append(y)
        y += 1
    return render_template('kontroles_strukturas.html', rezultats=rezultats, 
                                   for_cikla_rezultats=for_cikla_rezultats, 
                                   while_cikla_rezultats=while_cikla_rezultats)


@app.route('/funkcijas')
def funkcijas():
    def sveiciens(vards="Jānis"):
        return f"Sveiki! {vards}!"
    sveiciens1 = sveiciens()
    sveiciens2 = sveiciens("Irina")
    sveiciens3 = sveiciens1 + sveiciens2
    return render_template('funkcijas.html', sveiciens1=sveiciens1, 
                           sveiciens2=sveiciens2, sveiciens3=sveiciens3)


@app.route('/failu_apstrade')
def failu_apstrade():
    saturs= ""
    with open("teksts.txt", "r") as fails:
        saturs = fails.read()
    return render_template('failu_apstrade.html', saturs=saturs)

@app.route('/moduli')
def moduli():
    import math
    sqrt_rezultats = math.sqrt(16)
    return render_template('moduli.html', sqrt_rezultats=sqrt_rezultats)

@app.route('/oop')
def oop():
    class Persona:
        def __init__(self, vards, vecums):
            self.vards = vards
            self.vecums = vecums
            
        def sveiciens(self):
            return f"Sveiki, mani sauc {self.vards} un man ir {self.vecums} gadi."
    parsona1 = Persona("Jānis", 25)
    sveiciens = parsona1.sveiciens()
    
    return render_template('oop.html', sveiciens=sveiciens)
        



@app.route('/aiziet', methods=['POST'])
def aiziet():
    lietotajs = request.form['lietotajvards']
    return f"Paldies, {lietotajs}! Jūsu pieteikums ir saņemts."



@app.route('/majasdarbs')
def majasdarbs():
    return render_template('majasdarbs.html')

@app.route('/majasdarbs2', methods=['POST'])
def majasdarbs2():
    a = int(request.form['a'])
    b = int(request.form['b'])
    if a == b:
        rez = "Abi skaitli ir vienadi"
    elif a > b:
        rez = "Pirmais skaitlis ir lielāks"
    else:
        rez = "Otrais skaitlis ir lielāks"
    return render_template('majasdarbs.html', rez=rez)

@app.route('/aptauja')
def aptauja():
    return render_template('aptauja.html')

@app.route('/pieteikties', methods=['GET','POST'])
def pieteikties():
    if request.method == 'POST':
        lietotajvards = request.form['lietotajvards']
        parole = request.form['parole']

        conn = sqlite3.connect('datubaze.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM administratori WHERE lietotajvards = ?', 
                       (lietotajvards,))
        admin = cursor.fetchone()
        conn.close()

        if admin and check_password_hash(admin[2], parole):
            session['lietotajvards'] = lietotajvards
            return redirect(url_for('panelis'))
        else:
            flash('Nepareizs lietotājvārds vai parole!!!!')
    return render_template('pieteikties.html')

@app.route('/panelis')
def panelis():
    if 'lietotajvards' not in session:
        return redirect(url_for('pieteikties'))
    conn = sqlite3.connect('datubaze.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM lietotaji')
    lietotaji = cursor.fetchall()
    conn.close()
    return render_template('panelis.html', lietotaji=lietotaji)



@app.route('/iesniegt', methods=['POST'])
def iesniegt():
    vards = request.form['vards']
    dzimums = request.form['dzimums']
    hobiji = request.form.getlist('hobiji')
    hobiji_str = ', '.join(hobiji)
    conn = sqlite3.connect('datubaze.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO lietotaji (vards, dzimums, hobiji) VALUES (?,?,?)',
                   (vards, dzimums, hobiji_str))
    conn.commit()
    conn.close()
    
    return render_template('paldies.html')



def init_db():
    conn = sqlite3.connect('datubaze.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS lietotaji (
           id INTEGER PRIMARY KEY AUTOINCREMENT,
           vards TEXT NOT NULL,
           dzimums TEXT NOT NULL,
           hobiji TEXT
           )
''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS administratori (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        lietotajvards TEXT NOT NULL,
        parole TEXT NOT NULL
        )
''')

    cursor.execute('SELECT * FROM administratori WHERE lietotajvards = ?', ('admin',))
    if not cursor.fetchone():
       cursor.execute('INSERT INTO administratori (lietotajvards, parole) VALUES (?, ?)'
            ,('admin', generate_password_hash('admin')))
    conn.commit()
    conn.close()

init_db()

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
