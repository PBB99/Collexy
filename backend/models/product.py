from db.db import get_connection
from psycopg2 import OperationalError, IntegrityError, ProgrammingError
import traceback
from datetime import datetime
def new_product(NAME,PRODUCT_TYPE_ID,AMOUNT,STATUS,GRADED,GRADING_COMPANY_ID,PRICE,LAST_SOLD_PRICE,URL,DESCRIPTION):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM UNIQUE_KEYS WHERE TABLE_NAME='MY_PRODUCTS';")
        result=cursor.fetchone()
        id=result["next_id"]
        
        query=""" 
            INSERT INTO MY_PRODUCTS (ID,NAME,PRODUCT_TYPE_ID,AMOUNT,STATUS,GRADED,GRADING_COMPANY_ID,PRICE,LAST_SOLD_PRICE,URL,DESCRIPTION)
            VALUES (%s, %s, %s, %s,%s, %s, %s, %s, %s, %s,%s);
        """
        insert=cursor.execute(query, (id,NAME,PRODUCT_TYPE_ID,AMOUNT,STATUS,GRADED,GRADING_COMPANY_ID,PRICE,LAST_SOLD_PRICE,URL,DESCRIPTION))
        if  cursor.rowcount >0:
            cursor.execute("SELECT * FROM UNIQUE_KEYS WHERE TABLE_NAME='HISTORY_PRICES';")
            result=cursor.fetchone()
            h_id=result["next_id"]
            query2="""
            INSERT INTO HISTORY_PRICES values(%s,%s,%s,%s,%s,%s)
            """
            cursor.execute(query2,(h_id,NAME,PRICE,datetime.now(),'',1))
            if cursor.rowcount>0:
                update_uk_hprice="UPDATE UNIQUE_KEYS SET NEXT_ID=NEXT_ID+1 where TABLE_NAME='HISTORY_PRICES';"
                cursor.execute(update_uk_hprice,h_id)
                if insert is not None:
                        update_uk_products="UPDATE UNIQUE_KEYS SET NEXT_ID=NEXT_ID+1 where TABLE_NAME='MY_PRODUCTS';"
                        cursor.execute(update_uk_products,id)
        conn.commit()
        cursor.close()
        conn.close()
        return f"The product {id} has been successfully saved"


    except OperationalError as e:
        print(e,": There was an error inserting a new product1")
    except IntegrityError as e:
        print(e,": There was an error inserting a new product2")
    except ProgrammingError as e:
        print(e,": There was an error inserting a new product3")
    except Exception as e:
        print(e,": There was an error inserting a new product4")
        traceback.print_exc()
    


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
        print(e,": There was an error inserting a new product1")
    except IntegrityError as e:
        print(e,": There was an error inserting a new product2")
    except ProgrammingError as e:
        print(e,": There was an error inserting a new product3")
    except Exception as e:
        print(e,": There was an error inserting a new product4")
        traceback.print_exc()


def delete_product(ID):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        query="""
        DELETE FROM MY_PRODUCTS WHERE ID=%s;
        """
        cursor.execute(query,id)
        if cursor.rowcount>0:
            print("The product:",id," has been deleted")
        else:
            print("No rows deleted")
        return
    except OperationalError as e:
        print(e,": There was an error inserting a new product1")
    except IntegrityError as e:
        print(e,": There was an error inserting a new product2")
    except ProgrammingError as e:
        print(e,": There was an error inserting a new product3")
    except Exception as e:
        print(e,": There was an error inserting a new product4")
        traceback.print_exc()    