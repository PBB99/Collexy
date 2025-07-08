from db.db import get_connection
from psycopg2 import OperationalError, IntegrityError, ProgrammingError
import traceback
from datetime import datetime
from models.unique_keys import *

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
            raise ValueError("History Product ID not obtained")
        conn.commit()

        return f"The product {PRODUCT_ID} price has been successfully saved in the history price table"
    except (OperationalError,IntegrityError,ProgrammingError) as e:
        print(e,": There was an error inserting a new hystoric price")
        return None
    except Exception as e:
        print(e,": There was an error inserting a new hystoric price")
        traceback.print_exc()
        return None
    finally:
        cursor.close()
        conn.close()
    
def get_history_price(product_id):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        query="""
        SELECT * FROM HISTORY_PRICES WHERE PRODUCT_ID=%s
        """
        cursor.execute(query,(product_id,))
        if cursor.rowcount >0:
            list_results=cursor.fetchall()
        else:
            raise ValueError("Not Products obtained")

        return list_results
    except (OperationalError,IntegrityError,ProgrammingError) as e:
        print(e,": There was an error inserting a new hystoric price")
        return None
    except Exception as e:
        print(e,": There was an error inserting a new hystoric price")
        traceback.print_exc()
        return None
    finally:
        cursor.close()
        conn.close()