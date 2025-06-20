from db.db import get_connection
from psycopg2 import OperationalError, IntegrityError, ProgrammingError
def new_product(NAME,PRODUCT_TYPE_ID,AMOUNT,STATUS,GRADED,GRADING_COMPANY_ID,PRICE,LAST_SOLD_PRICE,URL,DESCRIPTION):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute("SELECT NEXT_ID FROM UNIQUE_KEYS WHERE TABLE_NAME='MY_PRODUCTS';")
        id=cursor.fetchone()[0]
        query=""" 
            INSERT INTO MY_PRODUCTS (ID,NAME,PRODUCT_TYPE_ID,AMOUNT,STATUS,GRADED,GRADING_COMPANY_ID,PRICE,LAST_SOLD_PRICE,URL,DESCRIPTION)
            VALUES (%s, %s, %s, %s,%s, %s, %s, %s, %s, %s,%s);
        """
        cursor.execute(query, (id,NAME,PRODUCT_TYPE_ID,AMOUNT,STATUS,GRADED,GRADING_COMPANY_ID,PRICE,LAST_SOLD_PRICE,URL,DESCRIPTION))
        update_uk="UPDATE UNIQUE_KEYS SET NEXT_ID=(SELECT NEXT_ID+1 FROM UNIQUE_KEYS WHERE TABLE_NAME='MY_PRODUCTS') where TABLE_NAME='MY_PRODUCTS';"
        cursor.execute(update_uk,id)
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
    


