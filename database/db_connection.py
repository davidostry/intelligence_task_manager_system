import mysql.connector

class DB_connector:
    def get_connection(self):
        return mysql.connector.connect(host = "127.0.0.1",
                                       user = "root",
                                       password = "1234",
                                       port = 3306,
                                       database = "Intelligence_db")
    
    def create_database(self):
        connection = self.get_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute("create database if not exists Intelligence_db;")
        cursor.execute("use Intelligence_db;")
        connection.commit()
        cursor.close()

    def create_tables(self):
        connection = self.get_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute("""create table if not exists agents(
                                                   id int auto_increment primary key,
                                                   name varchar(50) not null,
                                                   specialty varchar(100) not null,
                                                   is_active boolean default True,
                                                   completed_mission int default 0,
                                                   failed_mission int default 0,
                                                   agent_rank enum('Junior','Senior','Commander')
                                                   );
                                                   """)
        

        cursor.execute("""create table if not exists missions(
                                                               id int auto_increment primary key,
                                                               title varchar(50) not null,
                                                               description text not null,
                                                               location varchar(50) not null,
                                                               difficulty int not null,
                                                               importance int not null,
                                                               status varchar(50) default "new",
                                                               risk_level varchar(50),
                                                               assigned_agent_id int
                                                               );
                                                               """)
    
        connection.commit()
        cursor.close()
