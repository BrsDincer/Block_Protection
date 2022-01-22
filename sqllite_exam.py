from os import path
import sqlite3

ROOT = path.dirname(path.relpath((__file__)))

class DB_PROCESS():
    def CREATE_DB(name_of_db=str):
        try:
            con = sqlite3.connect(path.join(ROOT,name_of_db))
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS BLOCK_MAIN (keyword TEXT, chain TEXT, user TEXT)")
            con.commit()
            con.close()
        except:
            pass
        
    def ADD_DB(message_x,block_x,user_x,name_of):
        try:
            con = sqlite3.connect(path.join(ROOT,name_of))
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS BLOCK_MAIN (keyword TEXT, chain TEXT, user TEXT)")
            cur.execute("INSERT INTO BLOCK_MAIN values (?,?,?)",(message_x,block_x,user_x))
            con.commit()
            con.close()
        except:
            pass
        
    def REACH_DB(chain_code,name_of):
        try:
            con = sqlite3.connect(path.join(ROOT,name_of))
            cur = con.cursor()
            cur.execute("SELECT * FROM BLOCK_MAIN")
            get_spec = cur.fetchall()
            try:
                for x_in,chaın_code in enumerate(get_spec):
                    try:
                        if str(chain_code) == str(get_spec[x_in][1]):
                            con.commit()
                            con.close()
                            return get_spec[x_in][0]
                    except:
                        pass
            except:
                con.commit()
                con.close()
        except:
            pass
        
    def DELETE_DB(chain_code,name_of):
        try:
            con = sqlite3.connect(path.join(ROOT,name_of))
            cur = con.cursor()
            cur.execute("SELECT * FROM BLOCK_MAIN")
            get_spec = cur.fetchall()
            try:
                for x_in,chaın_code in enumerate(get_spec):
                    try:
                        if str(chain_code) == str(get_spec[x_in][1]):
                            cur.execute("DELETE FROM BLOCK_MAIN WHERE chain=?",(chain_code,))
                            con.commit()
                            con.close()
                    except:
                        pass
            except:
                con.commit()
                con.close()
        except:
            pass
        
    def EXC_DB(chain_code,new_block,name_of):
        try:
            con = sqlite3.connect(path.join(ROOT,name_of))
            cur = con.cursor()
            cur.execute("SELECT * FROM BLOCK_MAIN")
            get_spec = cur.fetchall()
            try:
                for x_in,chaın_code in enumerate(get_spec):
                    try:
                        if str(chain_code) == str(get_spec[x_in][1]):
                            cur.execute("DELETE FROM BLOCK_MAIN WHERE chain=?",(chain_code,))
                            cur.execute("INSERT INTO BLOCK_MAIN values (?,?,?)",(str(get_spec[x_in][0]),new_block,str(get_spec[x_in][2])))
                            con.commit()
                            con.close()
                    except:
                        pass
            except:
                con.commit()
                con.close()
        except:
            pass
        
        
    def READ_DB(base_name=str):
        try:
            con = sqlite3.connect(base_name)
            cur = con.cursor()
            cur.execute("SELECT * FROM BLOCK_MAIN")
            get_all = cur.fetchall()
            con.commit()
            con.close()
            return get_all
        except:
            pass
