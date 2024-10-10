import psycopg2

class StudyManagement:
    def __init__(self, dbname, user, password, host, port):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port

    def get_db_connection(self):
        conn = psycopg2.connect(
            dbname=self.dbname,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port
        )
        return conn

    def get_student(self, student_id):
        conn = self.get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM students WHERE id = %s', (student_id,))
        student = cur.fetchone()
        cur.close()
        conn.close()
        if student:
            print(f"ID: {student[0]}, Name: {student[1]}, Course: {student[2]}")
        else:
            print("Student not found.")

    def get_discipline(self, course_number):
        conn = self.get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM disciplines WHERE course_number = %s ORDER BY day_of_week, class_number', (course_number,))
        disciplines = cur.fetchall()
        cur.close()
        conn.close()
        if disciplines:
            for discipline in disciplines:
                print(f"ID: {discipline[0]}, Discipline: {discipline[1]}, Day: {discipline[2]}, Class: {discipline[3]}, Course: {discipline[4]}")
        else:
            print("No disciplines found for the given course.")

    def get_students(self, course_number):
        conn = self.get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM students WHERE course_number = %s ORDER BY student_name', (course_number,))
        students = cur.fetchall()
        cur.close()
        conn.close()
        if students:
            for student in students:
                print(f"ID: {student[0]}, Name: {student[1]}, Course: {student[2]}")
        else:
            print("No students found for the given course.")

    def get_disciplines(self):
        conn = self.get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM disciplines ORDER BY day_of_week, class_number')
        disciplines = cur.fetchall()
        cur.close()
        conn.close()
        for discipline in disciplines:
            print(f"ID: {discipline[0]}, Discipline: {discipline[1]}, Day: {discipline[2]}, Class: {discipline[3]}, Course: {discipline[4]}")

    def put_student(self, student_name1, student_name2, course_number):
        conn = self.get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO students (student_name, course_number) VALUES (%s, %s)', 
                    (student_name1 + ' ' + student_name2, course_number))
        conn.commit()
        cur.close()
        conn.close()
        print("Student added successfully.")

    def put_discipline(self, discipline_name, day_of_week, class_number, course_number):
        conn = self.get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO disciplines (discipline_name, day_of_week, class_number, course_number) VALUES (%s, %s, %s, %s)', 
                    (discipline_name, day_of_week, class_number, course_number))
        conn.commit()
        cur.close()
        conn.close()
        print("Discipline added successfully.")

    def delete_student(self, student_id):
        conn = self.get_db_connection()
        cur = conn.cursor()
        cur.execute('DELETE FROM students WHERE id = %s', (student_id,))
        conn.commit()
        cur.close()
        conn.close()
        print("Student deleted successfully.")

    def delete_discipline(self, discipline_id):
        conn = self.get_db_connection()
        cur = conn.cursor()
        cur.execute('DELETE FROM disciplines WHERE id = %s', (discipline_id,))
        conn.commit()
        cur.close()
        conn.close()
        print("Discipline deleted successfully.")

def main():
    study_management = StudyManagement(
        dbname='study',
        user='postgres',
        password='T6s6x7c5v',
        host='127.0.0.1',
        port='5432'
    )

    print("Welcome to the Study Management System!")
    print("Available commands:")
    print("GET student <id>")
    print("GET discipline <course_number>")
    print("GET students <course_number>")
    print("GET disciplines")
    print("PUT student <first_name> <last_name> <course_number>")
    print("PUT discipline <name> <day_of_week> <class_number> <course_number>")
    print("DELETE student <id>")
    print("DELETE discipline <id>")
    print("Type 'exit' to quit.")

    while True:
        command = input("Enter command: ").strip()
        if command.lower() == 'exit':
            print("Goodbye")
            break

        parts = command.split()
        if len(parts) < 2:
            print("Invalid command. Please try again.")
            continue

        operation = parts[0].upper()
        entity = parts[1].lower()

        try:
            if operation == 'GET' and entity == 'student':
                study_management.get_student(int(parts[2]))
            elif operation == 'GET' and entity == 'discipline':
                study_management.get_discipline(int(parts[2]))
            elif operation == 'GET' and entity == 'students':
                study_management.get_students(int(parts[2]))
            elif operation == 'GET' and entity == 'disciplines':
                study_management.get_disciplines()
            elif operation == 'PUT' and entity == 'student':
                study_management.put_student(parts[2], parts[3], int(parts[4]))
            elif operation == 'PUT' and entity == 'discipline':
                study_management.put_discipline(parts[2], parts[3], int(parts[4]), int(parts[5]))
            elif operation == 'DELETE' and entity == 'student':
                study_management.delete_student(int(parts[2]))
            elif operation == 'DELETE' and entity == 'discipline':
                study_management.delete_discipline(int(parts[2]))
            else:
                print("Unknown command. Please try again.")
        except IndexError:
            print("Incorrect number of arguments for the command.")
        except ValueError:
            print("Invalid argument type. Please check the input values.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    main()
