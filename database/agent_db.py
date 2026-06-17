from db_connection import DB_connector
from pydantic import BaseModel
from typing import Literal

db = DB_connector()

class AgentSchma(BaseModel):
    name : str
    specialty : str
    agent_rank : Literal['Junior', 'Senior', 'Commander']


class AgentDB:

    def create_agent(self,details: AgentSchma):
        connection = db.get_connection()
        cursor = connection.cursor(dictionary=True)

        query = """
                insert into agents(name, specialty, agent_rank) values (%s, %s, %s);
                """
        values = (details.name, details.specialty, details.agent_rank)
        try:
            cursor.execute(query, values)
            connection.commit()
            id = cursor.lastrowid
            return {"id": id, **details}
            
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

    def update_agent(self, agent_id:int, details:AgentSchma):
        connection = db.get_connection()
        cursor = connection.cursor(dictionary=True)

        query = """
                update agents set ()
                """
    
            
        
