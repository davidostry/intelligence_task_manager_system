from database.db_connection import DB_connector


db = DB_connector()

class AgentDB:

    def create_agent(self, agent_details):
        connection = db.get_connection()
        cursor = connection.cursor(dictionary=True)

        query = """
                insert into agents(name, specialty, agent_rank)
                values (%s, %s, %s);
                """
        values = (agent_details.name, agent_details.specialty, agent_details.agent_rank)
        try:
            cursor.execute(query, values)
            connection.commit()
            id = cursor.lastrowid
            return cursor.lastrowid
            
        except Exception as e:
            connection.rollback()
            raise e
        finally:
            cursor.close()

    def get_all_agents(self):
        connection = db.get_connection()
        cursor = connection.cursor(dictionary=True)
        try:
            cursor.execute("select * from agents;")
            result = cursor.fetchall()
            if cursor.rowcount > 0:
                return result
            else:
                return []
        except Exception as e:
            raise e
        finally:
            cursor.close()

    def get_agent_by_id(self,agent_id:int):
        connection = db.get_connection()
        cursor = connection.cursor(dictionary=True)

        query = "select * from agents where id = %s"
        try:
            cursor.execute(query, (agent_id,))
            result = cursor.fetchone()
            if cursor.rowcount == 0:
                return None
            return result
        except Exception as e:
            raise e
        finally:
            cursor.close()

    def update_agent(self, details, agent_id:int,):
        connection = db.get_connection()
        cursor = connection.cursor(dictionary=True)
        agent = details.model_dump()

        query = """
                update agents set name = %s,
                specialty = %s,
                agent_rank = %s
                where id = %s
                """
        try:
            cursor.execute(query, (agent["name"], agent["specialty"],agent["agent_rank"],agent_id))
            connection.commit()
            if cursor.rowcount == 0:
                return None
            return {"id": id, **agent}
        except Exception as e:
            print (e)
        finally:
            cursor.close()

    def deactivate_agent(self,id):
        connection = db.get_connection()
        cursor = connection.cursor(dictionary=True)
        query = "update agents set is_active = False where id = %s"
        try:
            cursor.execute(query, (id,))
            connection.commit()
            if cursor.rowcount == 0:
                return None
            return id
        except Exception as e:
            print (e)
        finally:
            cursor.close()

    def increment_completed(self,id):
        connection = db.get_connection()
        cursor = connection.cursor(dictionary=True)
        query = "update agents set completed_mission +=1 where id=%s"
        try:
            cursor.execute(query, (id,))
            connection.commit()
            if cursor.rowcount == 0:
                return None
        except Exception as e:
            print (e)
        finally:
            cursor.close()

    def increment_filed(self,id):
        connection = db.get_connection()
        cursor = connection.cursor(dictionary=True)
        query = "update agents set failed_mission +=1 where id=%s"
        try:
            cursor.execute(query, (id,))
            connection.commit()
            if cursor.rowcount == 0:
                return None
        except Exception as e:
            print (e)
        finally:
            cursor.close()

    # def agent_performance(self,id):
    #     connection = db.get_connection()
    #     cursor = connection.cursor(dictionary=True)
    #     query = "select completed_mission, failed_mission where id = %s"
    #     try:
    #         cursor.execute(query, (id,)) 

        
    




            
