import psycopg2  
connection = psycopg2.connect( 
    host="localhost", 
    database="task_manager", 
    user="postgres", 
    password="password", 
    port=5432 
) 
 
cursor = connection.cursor() 

def add_task(): 
    title = input("Enter task title: ") 
    description = input("Enter task description: ") 
 
    query = """ 
        INSERT INTO tasks (title, description) 
        VALUES (%s, %s) 
    """ 
 
    cursor.execute(query, (title, description)) 
    connection.commit() 
 
    print("Task added successfully!") 
 
def view_tasks(): 
    query = """ 
        SELECT id, title, description, status, created_at 
        FROM tasks 
        ORDER BY id 
    """ 
 
    cursor.execute(query) 
 
    tasks = cursor.fetchall() 
 
    if not tasks: 
        print("No tasks found.") 
        return 
 
    print("\n========== TASKS ==========") 
 
    for task in tasks: 
        print("--------------------------------") 
        print("ID:", task[0]) 
        print("Title:", task[1]) 
        print("Description:", task[2]) 
        print("Status:", task[3]) 
        print("Created:", task[4]) 
 
def update_task(): 
    task_id = input("Enter task ID: ") 
    new_title = input("Enter new title: ") 
    new_description = input("Enter new description: ") 
    query = """ 
        UPDATE tasks 
        SET title = %s, 
            description = %s,  
        WHERE id = %s 
    """ 
 
    cursor.execute( 
        query, 
        (new_title, new_description,  task_id) 
    ) 
 
    connection.commit() 
 
    if cursor.rowcount == 0: 
        print("Task not found.") 
    else: 
        print("Task updated successfully!") 
 
def delete_task(): 
    task_id = input("Enter task ID to delete: ") 
 
    query = """ 
        DELETE FROM tasks 
        WHERE id = %s 
    """ 
 
    cursor.execute(query, (task_id,)) 
    connection.commit() 
 
    if cursor.rowcount == 0: 
        print("Task not found.") 
    else: 
        print("Task deleted successfully!") 
 
def complete_task(): 
    task_id = input("Enter task ID: ") 
 
    query = """ 
        UPDATE tasks 
        SET status = 'Completed' 
        WHERE id = %s 
    """ 
 
    cursor.execute(query, (task_id,)) 
    connection.commit() 
 
    if cursor.rowcount == 0: 
        print("Task not found.") 
    else: 
        print("Task marked as completed!") 
 
def show_menu(): 
    print("\n========== TASK MANAGER ==========") 
    print("1. Add Task") 
    print("2. View Tasks") 
    print("3. Update Task") 
    print("4. Delete Task") 
    print("5. Mark Task Complete") 
    print("6. Exit") 
 
while True: 
 
    show_menu() 
 
    choice = input("Enter your choice: ") 
 
    if choice == "1": 
        add_task() 
 
    elif choice == "2": 
        view_tasks() 
 
    elif choice == "3": 
        update_task() 
 
    elif choice == "4": 
        delete_task() 
 
    elif choice == "5": 
        complete_task() 
 
    elif choice == "6": 
        print("Goodbye!") 
        break 
 
    else: 
        print("Invalid choice.") 
 
cursor.close() 
connection.close() 