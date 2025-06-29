from db.db import get_connection
from psycopg2 import OperationalError, IntegrityError, ProgrammingError
import traceback


from psycopg2 import OperationalError, IntegrityError, ProgrammingError
from db.db import get_connection
import traceback

def update_unique_keys(table_name):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        query = """
        UPDATE UNIQUE_KEYS
        SET NEXT_ID = NEXT_ID + 1
        WHERE TABLE_NAME = %s;
        """
        cursor.execute(query, (table_name,))
        conn.commit()

        if cursor.rowcount > 0:
            return f"The NEXT_ID for '{table_name}' has been successfully incremented."
        else:
            return f"No matching table '{table_name}' found in UNIQUE_KEYS."

    except (OperationalError, IntegrityError, ProgrammingError) as e:
        print(f"{e}: There was an error updating the unique key")
        return None
    except Exception as e:
        print(f"{e}: Unexpected error updating the unique key")
        traceback.print_exc()
        return None
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def get_unique_keys(TABLE_NAME):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        query="""
        SELECT * FROM UNIQUE_KEYS WHERE TABLE_NAME=%s;
        """
        cursor.execute(query,(TABLE_NAME,))
        if cursor.rowcount<=0:
            raise ValueError("Not id getted")

        
        result=cursor.fetchone()
        next_id=result["next_id"]

        return next_id
    except (OperationalError, IntegrityError, ProgrammingError) as e:
        print(f"{e}: There was an error getting the unique key")
        return None
    except Exception as e:
        print(f"{e}: Unexpected error getting the unique key")
        traceback.print_exc()
        return None
    finally:
        cursor.close()
        conn.close()