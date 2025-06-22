from db.db import get_connection
from psycopg2 import OperationalError, IntegrityError, ProgrammingError
import traceback
from unique_keys import *

def new_product_type(NAME,DESCRIPTION):
    try:
        pt_id=get_unique_keys("PRODUCT_TYPE")
        if pt_id is not None:
            conn=get_connection()
            cursor=conn.cursor()
            query="""
            INSERT INTO PRODUCT_TYPE VALUES (%s,%s,%s);
            """
            cursor.execute(query,(pt_id,NAME,DESCRIPTION))
            if cursor.rowcount()>0:
                print(cursor.rowcount()," New rows inserted")
            conn.commit()
            cursor.close()
            conn.close()
        return f"The product type:{pt_id} has been succesfully inserted"
    except OperationalError as e:
        print(e,": There was an error inserting a new product type")
        return None
    except IntegrityError as e:
        print(e,": There was an error inserting a new product type")
        return None
    except ProgrammingError as e:
        print(e,": There was an error inserting a new product type")
        return None
    except Exception as e:
        print(e,": There was an error inserting a new product type")
        traceback.print_exc()
        return None

#def get_product_type(id):
