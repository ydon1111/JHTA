import cx_Oracle

def excute(query, val_list = []):
    try:
        connecion = cx_Oracle.connect("scott", "tiger", "192.168.0.69:1521/orcl")
        cur = connecion.cursor()
        cur.execute(query, val_list)
        res = True
        
        if query[:6].upper() == "SELECT":
            res = cur.fetchall()
                
        return res
    except:
        print("DB error")
        return False
    finally:
        connecion.commit()
        connecion.close()
    