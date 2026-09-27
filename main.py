import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Veritabanı dosyasını projenin tam içine koyuyoruz
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hastalar.db'
app.config['UPLOAD_FOLDER'] = os.path.join('static', 'kayitlar')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Kayıt klasörü kontrolü
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

class Hasta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ad = db.Column(db.String(100))
    telefon = db.Column(db.String(20))
    hikaye = db.Column(db.Text)
    remediler = db.Column(db.Text)
    ses_dosyasi = db.Column(db.String(200))

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    search = request.args.get('search')
    if search:
        hastalar = Hasta.query.filter((Hasta.ad.contains(search)) | (Hasta.telefon.contains(search))).all()
    else:
        hastalar = Hasta.query.all()
    return render_template('index.html', hastalar=hastalar)

@app.route('/ekle', methods=['POST'])
def ekle():
    ad = request.form.get('ad')
    telefon = request.form.get('telefon')
    ses = request.files.get('ses_verisi')
    
    ses_adi = None
    if ses and ses.filename != '':
        ses_adi = f"{ad}_{telefon}.webm".replace(" ", "_")
        ses.save(os.path.join(app.config['UPLOAD_FOLDER'], ses_adi))

    yeni_hasta = Hasta(
        ad=ad,
        telefon=telefon,
        hikaye=request.form.get('hikaye'),
        remediler=request.form.get('remediler'),
        ses_dosyasi=ses_adi
    )
    db.session.add(yeni_hasta)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/duzenle/<int:id>', methods=['POST'])
def duzenle(id):
    hasta = Hasta.query.get_or_404(id)
    hasta.hikaye = request.form.get('hikaye')
    hasta.remediler = request.form.get('remediler')
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)