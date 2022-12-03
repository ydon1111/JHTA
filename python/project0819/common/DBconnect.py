import cx_Oracle

def excute(query, val_list = []):
    try:
        connecion = cx_Oracle.connect("scott", "tiger", "127.0.0.1:1521/orcl")
        cur = connecion.cursor()
        cur.execute(query, val_list)
        res = True
        
        if query[:6].upper() == "SELECT":
            res = []
            for data in cur:
                res.append(data)
                
        return res
    except:
        print("DB error")
        return False
    finally:
        connecion.commit()
        connecion.close()
    