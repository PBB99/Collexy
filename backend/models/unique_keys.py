from db.db import get_connection
from psycopg2 import OperationalError, IntegrityError, ProgrammingError
import traceback


def update_unique_keys(tableName):
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
        print(e,": There was an error updating the unique key")
        return None
    except IntegrityError as e:
        print(e,": There was an error updating the unique key")
        return None
    except ProgrammingError as e:
        print(e,": There was an error updating the unique key")
        return None
    except Exception as e:
        print(e,": There was an error updating the unique key")
        traceback.print_exc()
        return None

def get_unique_keys(TABLE_NAME):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        query="""
        ("SELECT * FROM UNIQUE_KEYS WHERE TABLE_NAME='%s';")
        """
        result=cursor.fetchone()
        id=result["next_id"]
        cursor.close()
        conn.close()
        return id
    except OperationalError as e:
        print(e,": There was an error getting the unique key")
        return None
    except IntegrityError as e:
        print(e,": There was an error getting the unique key")
        return None
    except ProgrammingError as e:
        print(e,": There was an error getting the unique key")
        return None
    except Exception as e:
        print(e,": There was an error getting the unique key")
        traceback.print_exc()
        return None
        