from db.db import get_connection
from psycopg2 import OperationalError, IntegrityError, ProgrammingError
import traceback


def new_entry(tableName):
    try:   
        conn=get_connection()
        cursor=conn.cursor()
        query="""
        UPDATED UNIQUE_KEYS SET NEXT_ID=NEXT_ID WHERE TABLE_NAME='%s';
        """
        cursor.execute(query,tableName)
        conn.commit()
        cursor.close()
        conn.close()
        return f"The next id of  {tableName} has been successfully updated"
    except OperationalError as e:
        print(e,": There was an error inserting a new product1")
    except IntegrityError as e:
        print(e,": There was an error inserting a new product2")
    except ProgrammingError as e:
        print(e,": There was an error inserting a new product3")
    except Exception as e:
        print(e,": There was an error inserting a new product4")
        traceback.print_exc()    