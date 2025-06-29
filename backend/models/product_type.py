from db.db import get_connection
from psycopg2 import OperationalError, IntegrityError, ProgrammingError
import traceback
from models.unique_keys import *

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

def get_product_type(product_id,filter):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute("SELECT %s FROM PRODUCT_TYPE WHERE ID=%s",(filter,product_id))
        
        if cursor.rowcount()>0:
            print("Product type information getted succesfully")
            value=cursor.fetchone[filter]
            
        cursor.close()
        conn.close()
        return value
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

def delete_product_type(product_id):
    try:    
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute("Delete FROM PRODUCT_TYPE WHERE ID=%s",(product_id,))
        conn.commit()
        cursor.close()
        conn.close()
        return f"Product type {id} has been deleted"
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