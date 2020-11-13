from flask import Flask, render_template, request
from py_source.common.DbConn import DbConn
import py_source.hn as hn
from py_source.common.DbConn import DbConn

app = Flask(__name__)

# main
@app.route('/')
def index():
    return render_template('main.html')

@app.route('/main')
def go_main():
    return render_template('main.html')

# overweight
@app.route('/go_ov')
def go_ov():
    return render_template('happiness/ov.html')

# aca
@app.route('/aca')
def go_aca():
    return render_template('happiness/aca.html')

# etc 1(lee)
@app.route('/go_etc_1')
def go_etc_1():
    return render_template('happiness/etc_1.html')

# etc 2(kim)
@app.route('/go_etc_2')
def go_etc_2():
    return render_template('happiness/etc_2.html')

# khl
@app.route('/go_khl')
def go_khl():
    return render_template('happiness/khl.html')

# 행복도 테스트
@app.route('/go_chk_hn')
def go_chk_hn():
    city1 = hn.get_locals()        
    return render_template('happiness/chk_hn.html', city1=city1)

@app.route('/hn_city2', methods = ['GET'])
def hn_city2():
    city2 = request.args.get('city1')
    return {'city2':hn.get_city2(city2)}

@app.route('/chk_hn_dc', methods = ['GET'])
def chk_hn_dc():
    db = DbConn()
    city1 = request.args.get('city1')
    city2 = request.args.get('city2')
    
    sv_list = list()
    params = dict()
    
    params['city1'] = city1
    params['city2'] = city2
    
    for i in range(1, 11):
        index = 'sv' + str(i)
        sv_list.append(int(request.args.get(index)))
        params[index] = int(request.args.get(index))
    
    db.execute('insert into SURVEY values(S_SEQ.nextval, :sv1, :sv2, :sv3, :sv4, :sv5, :sv6, :sv7, :sv8, :sv9, :sv10, sysdate, :city1, :city2)', params)
    db.disconnect()
    
    return render_template('happiness/res_hn.html', res=hn.get_dc(city1, city2, sv_list))

# 자료 출처
@app.route('/go_source')
def go_source():
    city1 = hn.get_locals()        
    return render_template('happiness/source.html')

