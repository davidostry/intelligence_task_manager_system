from database.db_connection import DB_connector

db = DB_connector()
class MissionDB:

    def create_mission(self,data):
        connection = db.get_connection()
        cursor = connection.cursor(dictionary=True)

        query = """
                INSERT INTO missions(title, description, location, difficulty, importance)
                VALUES (%s, %s, %s, %s, %s);
                """
        values = (data.title, data.description, data.location, data.difficulty, data.importance)
        try:
            cursor.execute(query, values)
            connection.commit()
            return cursor.lastrowid
            
        except Exception as e:
            connection.rollback()
            raise e
        finally:
            cursor.close()
        
    def get_all_missions(self):
        connection = db.get_connection()
        cursor = connection.cursor(dictionary=True)
        try:
            cursor.execute("select * from missions;")
            result = cursor.fetchall()
            if cursor.rowcount > 0:
                return result
            else:
                return []
        except Exception as e:
            raise e
        finally:
            cursor.close()

    def get_mission_by_id(self, mission_id:int):
        connection = db.get_connection()
        cursor = connection.cursor(dictionary=True)

        query = "select * from missions where id = %s"
        try:
            cursor.execute(query, (mission_id,))
            result = cursor.fetchone()
            if cursor.rowcount == 0:
                return None
            return result
        except Exception as e:
            raise e
        finally:
            cursor.close()
    

    def count_by_status(self, status):
        connection = db.get_connection()
        cursor = connection.cursor(dictionary=True)
        query = "select count(*) where status = %s"
        try:
            cursor.execute(query, (status,))
            result = cursor.fetchone()
            if cursor.rowcount == 0:
                return None
            return result
        except Exception as e:
            raise e
        finally:
            cursor.close() 
    
    def count_open_mission(self):
        connection = db.get_connection()
        cursor = connection.cursor(dictionary=True)
        query = "select count(*) where status = "asigned"
        try:
            cursor.execute(query)
            result = cursor.fetchone()
            if cursor.rowcount == 0:
                return None
            return result
        except Exception as e:
            raise e
        finally:
            cursor.close() 
               



