from db.db import get_connection
from psycopg2 import OperationalError, IntegrityError, ProgrammingError
import traceback
from datetime import datetime
from models.unique_keys import *
from models.hystory_prices import *

def new_product(NAME,PRODUCT_TYPE_ID,AMOUNT,STATUS,GRADED,GRADING_COMPANY_ID,PRICE,LAST_SOLD_PRICE,URL,DESCRIPTION):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        id=get_unique_keys("MY_PRODUCTS")
        
        if id is not None:
            query=""" 
            INSERT INTO MY_PRODUCTS (ID,NAME,PRODUCT_TYPE_ID,AMOUNT,STATUS,GRADED,GRADING_COMPANY_ID,PRICE,LAST_SOLD_PRICE,URL,DESCRIPTION)
            VALUES (%s, %s, %s, %s,%s, %s, %s, %s, %s, %s,%s);
        """
            cursor.execute(query, (id,NAME,PRODUCT_TYPE_ID,AMOUNT,STATUS,GRADED,GRADING_COMPANY_ID,PRICE,LAST_SOLD_PRICE,URL,DESCRIPTION))
            if  cursor.rowcount >0:
                h_id=get_unique_keys("HISTORY_PRICES")
                query2="""
            INSERT INTO HISTORY_PRICES values(%s,%s,%s,%s,%s,%s)
            """
                cursor.execute(query2,(h_id,NAME,PRICE,datetime.now(),'',1))
                if cursor.rowcount>0:
                    update_uk_hprice=update_unique_keys("HISTORY_PRICES")
                    if update_uk_hprice is not None:
                        update_unique_keys("MY_PRODUCTS")
        conn.commit()
        cursor.close()
        conn.close()
        return f"The product {id} has been successfully saved"


    except OperationalError as e:
        print(e,": There was an error inserting a new product1")
        return None
    except IntegrityError as e:
        print(e,": There was an error inserting a new product2")
        return None
    except ProgrammingError as e:
        print(e,": There was an error inserting a new product3")
        return None
    except Exception as e:
        print(e,": There was an error inserting a new product4")
        traceback.print_exc()
        return None
    


def update_product(NAME,PRODUCT_TYPE_ID,AMOUNT,STATUS,GRADED,PRICE,LAST_SOLD_PRICE):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM MY_PRODUCTS WHERE NAME='%s' AND product_type_id=%s;",(NAME,PRODUCT_TYPE_ID))
        result=cursor.fetchone()
        id=result["id"]
        if cursor.rowcount >0:
            query_up="""
                    UPDATE TABLE MY PRODUCTS SET
                    AMOUNT=%s,
                    STATUS=%s,
                    GRRADED=%s,
                    PRICE=%s,
                    LAST_SOLD_PRICE=%s
                    where id=%s
                    """
            cursor.execute(query_up,(AMOUNT,STATUS,GRADED,PRICE,LAST_SOLD_PRICE,id))
        cursor.close()
        conn.commit()
        conn.close()    
        return 
    except OperationalError as e:
        print(e,": There was an error inserting a new product")
        return None
    except IntegrityError as e:
        print(e,": There was an error inserting a new product")
        return None
    except ProgrammingError as e:
        print(e,": There was an error inserting a new product")
        return None
    except Exception as e:
        print(e,": There was an error inserting a new product")
        traceback.print_exc()
        return None

def get_product(ID):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        query="""SELECT * FROM MY_PRODUCTS WHERE ID=%s"""
        cursor.execute(query,(ID,))
        if cursor.rowcount>0:
            my_product=cursor.fetchone()
            print("Prodcut information succesfully getted")
        cursor.close()
        conn.close()
        return dict(my_product)
    except OperationalError as e:
        print(e,": There was an error getting the product")
        return None
    except IntegrityError as e:
        print(e,": There was an error getting the product")
        return None
    except ProgrammingError as e:
        print(e,": There was an error getting the product")
        return None
    except Exception as e:
        print(e,": There was an error getting the product")
        traceback.print_exc()
        return None    
       
def delete_product(ID):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        query="""
        DELETE FROM MY_PRODUCTS WHERE ID=%s;
        """
        cursor.execute(query,(ID,))
        if cursor.rowcount>0:
            print("The product:",ID," has been deleted")
        else:
            print("No rows deleted")
        return
    except OperationalError as e:
        print(e,": There was an error deleting a new product")
        return None
    except IntegrityError as e:
        print(e,": There was an error deleting a new product")
        return None
    except ProgrammingError as e:
        print(e,": There was an error deleting a new product")
        return None
    except Exception as e:
        print(e,": There was an error deleting a new product")
        traceback.print_exc()
        return None    