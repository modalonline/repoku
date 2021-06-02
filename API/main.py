from flask import Flask, jsonify, request
from flaskext.mysql import MySQL
import pymysql
app = Flask(__name__)
mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'basoca'
app.config['MYSQL_DATABASE_PASSWORD'] = '123456'
app.config['MYSQL_DATABASE_DB'] = 'basoca'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)

@app.route('/')
def api():
    return 'API is Active!!'

@app.route('/data')
def dataset():
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT No no, Provinsi provinsi, KabKota kabkota,Kecamatan kecamatan, Desa desa, NIK nik, Nama nama FROM dataset")
        rows = cursor.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/input', methods=['POST'])
def add_data():
    conn = None
    cursor = None
    try:
        _json = request.json
        _provinsi = _json['provinsi']
        _kabkota = _json['kabkota']
        _kecamatan = _json['kecamatan']
        _desa = _json['desa']
        _nik = _json['nik']
        _nama = _json['nama']
        _penghasilan = _json['penghasilan']
        _jmltj = _json['jmltj']
        _umur = _json['umur']
        _ibuhamil = _json['ibuhamil']
        _lansia = _json['lansia']
        _disable = _json['disable']
        _jmlmtr = _json['jmlmtr']
        _jmlmob = _json['jmlmob']
        _bpnt = _json['bpnt']
        _bst = _json['bst']
        _pkh = _json['pkh']
        if _provinsi and _kabkota and _kecamatan and _desa and _nik and _nama and _penghasilan and _jmltj and _umur and _ibuhamil and _lansia and _disable and _jmlmtr and _jmlmob and _bpnt and _bst and _pkh and request.method == 'POST':
            sql = "INSERT INTO dataset(Provinsi, KabKota, Kecamatan, Desa, NIK, Nama, PenghasilanBulanan, JumlahTanggungJawab, Umur, IbuHamil, LanjutUsia, Disabilitas, JumlahMotor, JumlahMobil, BPNT, BST, PKH) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            data = (_provinsi, _kabkota, _kecamatan, _desa, _nik, _nama, _penghasilan, _jmltj, _umur, _ibuhamil, _lansia, _disable, _jmlmtr, _jmlmob, _bpnt, _bst, _pkh)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('Data added successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/result')
def result():
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT No no, Provinsi provinsi, KabKota kabkota,Kecamatan kecamatan, Desa desa, NIK nik, Nama nama, PenerimaBansos penerima FROM result")
        rows = cursor.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/result/<string:nik>')
def getresult(nik):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "SELECT No no, Provinsi provinsi, KabKota kabkota,Kecamatan kecamatan, Desa desa, NIK nik, Nama nama, PenerimaBansos penerima FROM result where nik=%s", nik)
        row = cursor.fetchone()
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp


if __name__ == '__main__':
    app.run()