from db.db import get_connection
from psycopg2 import OperationalError, IntegrityError, ProgrammingError
import traceback
from datetime import datetime
from unique_keys import *

def new_history_price(NAME,PRICE,SOURCE,PRODUCT_ID):
    try:
        conn=get_connection()
        cursor=conn.cursor()

        h_id=get_unique_keys("HISTORY_PRICES")
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
        print(e,": There was an error inserting a new hystoric price")
        return None
    except IntegrityError as e:
        print(e,": There was an error inserting a new hystoric price")
        return None
    except ProgrammingError as e:
        print(e,": There was an error inserting a new hystoric price")
        return None
    except Exception as e:
        print(e,": There was an error inserting a new hystoric price")
        traceback.print_exc()
        return None
    
def get_history_price(product_id):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        query="""
        SELECT * FROM HISTORY_PRICES WHERE PRODUCT_ID=%s
        """
        cursor.execute(query,product_id)
        if cursor.rowcount()>0:
            list_results=cursor.fetchall()

        return list_results
    except OperationalError as e:
        print(e,": There was an error inserting a new hystoric price")
        return None
    except IntegrityError as e:
        print(e,": There was an error inserting a new hystoric price")
        return None
    except ProgrammingError as e:
        print(e,": There was an error inserting a new hystoric price")
        return None
    except Exception as e:
        print(e,": There was an error inserting a new hystoric price")
        traceback.print_exc()
        return None