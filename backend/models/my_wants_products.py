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
        want_product_id=get_unique_keys("MY_WANTS_PRODUCTS")
        
        if want_product_id is  None:
            raise ValueError("Not product id getted from Unique Keys")
        
        query=""" 
            INSERT INTO MY_WANTS_PRODUCTS (ID,NAME,PRODUCT_TYPE_ID,AMOUNT,STATUS,GRADED,GRADING_COMPANY_ID,PRICE,LAST_SOLD_PRICE,URL,DESCRIPTION)
            VALUES (%s, %s, %s, %s,%s, %s, %s, %s, %s, %s,%s);
        """
        cursor.execute(query, (want_product_id,NAME,PRODUCT_TYPE_ID,AMOUNT,STATUS,GRADED,GRADING_COMPANY_ID,PRICE,LAST_SOLD_PRICE,URL,DESCRIPTION))
        if  cursor.rowcount <0:
                raise ValueError("Product not inserted")  
        hp_insert=new_history_price(NAME,PRICE,'',1)
                
        if hp_insert is None:
                    raise ValueError("Error inserting history price for wanted product")
        else:
                update_uk_hprice=update_unique_keys("HISTORY_PRICES")
                if update_uk_hprice is not None:
                        update_unique_keys("MY_WANTS_PRODUCTS")
                else:
                        raise ValueError("Error updating Unique Keys")
        conn.commit()
        return f"The product {want_product_id} has been successfully saved"
    except (OperationalError,IntegrityError,ProgrammingError) as e:
        print(e,": There was an error inserting a new wanted product")
        return None
    except Exception as e:
        print(e,": There was an error inserting a new wanted product")
        traceback.print_exc()
        return None
    finally:
        cursor.close()
        conn.close()
    
def update_product(AMOUNT,STATUS,GRADED,PRICE,LAST_SOLD_PRICE,wanted_product_id):
    try:
        conn=get_connection()
        cursor=conn.cursor()

        query_up="""
                    UPDATE my_wants_products SET
                    AMOUNT=%s,
                    STATUS=%s,
                    GRADED=%s,
                    PRICE=%s,
                    LAST_SOLD_PRICE=%s
                    where id=%s
                    """
        cursor.execute(query_up,(AMOUNT,STATUS,GRADED,PRICE,LAST_SOLD_PRICE,wanted_product_id))
        if cursor.rowcount<=0:
             raise ValueError("Error executing update")
        conn.commit()
        return f"Product with ID {wanted_product_id} updated successfully."
    except (OperationalError,IntegrityError,ProgrammingError) as e:
        print(e,": There was an error inserting a new wanted product")
        return None
    except Exception as e:
        print(e,": There was an error inserting a new wanted product")
        traceback.print_exc()
        return None
    finally:
        cursor.close()
        conn.close()

def get_product(wanted_product_ID):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        query="""SELECT * FROM MY_WANTS_PRODUCTS WHERE ID=%s"""
        cursor.execute(query,(wanted_product_ID,))
        if cursor.rowcount>0:
            my_product=cursor.fetchone()
            print("Prodcut information succesfully getted")
        else:
            raise ValueError("Product info not obtained")
        return dict(my_product) #retonar un diccionario clave valor del my wanted product
    except (OperationalError,IntegrityError,ProgrammingError) as e:
        print(e,": There was an error getting wanted product info")
        return None
    except Exception as e:
        print(e,": There was an error deleting a new wanted product")
        traceback.print_exc()
        return None 
    finally:
        cursor.close()
        conn.close() 
        
def get_all_products():
    try:
        conn=get_connection()
        cursor=conn.cursor()
        query="""SELECT * FROM MY_WANTS_PRODUCTS"""
        cursor.execute(query,id)
        if cursor.rowcount>0:
            my_product=cursor.fetchall()
            print("Prodcut information succesfully getted")
        else:
            raise ValueError("Product info not obtained")
        return my_product
    except (OperationalError,IntegrityError,ProgrammingError) as e:
        print(e,": There was an error deleting a new wanted product")
        return None
    except Exception as e:
        print(e,": There was an error deleting a new wanted product")
        traceback.print_exc()
        return None 
    finally:
        cursor.close()
        conn.close()  
       
def delete_product(ID):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        query="""
        DELETE FROM MY_WANTS_PRODUCTS WHERE ID=%s;
        """
        cursor.execute(query,(ID,))
        if cursor.rowcount>0:
            print("The product:",ID," has been deleted")
        else:
            raise ValueError("No rows deleted")
        return
    except (OperationalError,IntegrityError,ProgrammingError) as e:
        print(e,": There was an error deleting a new wanted product")
        return None
    except Exception as e:
        print(e,": There was an error deleting a new wanted product")
        traceback.print_exc()
        return None  
    finally:
        cursor.close()
        conn.close()  