from db.db import get_connection
from psycopg2 import OperationalError, IntegrityError, ProgrammingError
import traceback
from datetime import datetime

def new_entry(NAME,PRICE,SOURCE,PRODUCT_ID):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM UNIQUE_KEYS WHERE TABLE_NAME='HISTORY_PRICES';")
        result=cursor.fetchone()
        h_id=result["next_id"]
        if h_id is not None:
            query="""
            INSERT INTO HISTORY_PRICES values(%s,%s,%s,%s,%s,%s)
             """
            cursor.execute(query,(h_id,NAME,PRICE,datetime.now(),SOURCE,PRODUCT_ID))
        else:
            print("History id key generator has failed")
        conn.commit()
        cursor.close()
        conn.close()
        return f"The product {PRODUCT_ID} price has been successfully saved in the history price table"
    except OperationalError as e:
        print(e,": There was an error inserting a new product1")
    except IntegrityError as e:
        print(e,": There was an error inserting a new product2")
    except ProgrammingError as e:
        print(e,": There was an error inserting a new product3")
    except Exception as e:
        print(e,": There was an error inserting a new product4")
        traceback.print_exc()    