# sqlite3 היא ספרייה המאפשרת לניהול בסיס נתונים 
# היא מאפשרת לנו ליצור בסיס מידע ולנהל אותו
#מאפשרת לשלוח שאילתות אס קיו אל לבסיס הנתונים 
import sqlite3

#לפנות לספרייה וליצור בסיס נתונים ולשמור אותו

#משתנה  שישמור על החיבור לבסיס הנתונים 
database = sqlite3.connect('booksDB.db')
#בשביל שנוכל לשלוח שאילתות לבסיס הנתונים 
#מחיקה / עדכון / שליפה של מידע 
# cursor() = מאפשרת לנו לבצע פעולות על בסיס הנתונים
action = database.cursor()
#ליצור טבלה בבסיס הנתונים 
#execute() - שולחת שאליתות לבסיס הנתונים שיבצע 
action.execute('''CREATE TABLE IF NOT EXISTS books (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      title TEXT NOT NULL,
      author TEXT NOT NULL,
      year INTEGER NOT NULL
)''')

#להוסיף ספר לטבלה 
#text = "INSERT INTO books (title,author,year) VALUES ('first book','tal',2011)"
#execute() - שולחת שאליתות לבסיס הנתונים שיבצע 
#לשלוח את השאילתה לבסיס הנתונים 
#action.execute(text)
#כששולחים שאילתה שעושה שינוי בבסיס הנתונים 
#נעשה סייב - נשמור 
#database.commit()

#מה נבקש מבסיס הנתונים כדאי לראות אם זה עבד? 
#לשמור שאילתה במשתנה 
# text = "SELECT * FROM books"
# #לשלוח אותה לבסיס הנתונים
# action.execute(text)
# #לאסוף את המידע שבסיס הנתונים החזיר מהשאילתה 
# result = action.fetchall()
# print (result)

#ליצור פונקציה - add_book
def add_book():      
      #תקלוט בעזרת 3 משתנים ואינפוט 
      #כותרת 
      mytitle = input("insert title ")
      #סופר
      myauthor = input("insert author ")
      #שנה 
      myyear = input("insert year ")
      #שאילתה להוספת הספר שהמשתמשים רוצים לבסיס הנתונים
      action.execute("INSERT INTO books (title,author,year) VALUES (?,?,?)",(mytitle,myauthor,myyear))

#לקרוא לפונקציה 
#add_book()
def show_books():
      text = "SELECT * FROM books"
      #לשלוח אותה לבסיס הנתונים
      action.execute(text)
      #לאסוף את המידע שבסיס הנתונים החזיר מהשאילתה 
      #ולשמור ברשימה של פייתון
      result = action.fetchall()
      print (result)

# פונקצייה לחיפוש לפי שם סופר 
def search():
      #1. לקלוט ולשמור שם סופר
      name = input("enter author name")
      # 2. לבקש באס קיו אל את הספרים שהסופר כתב 
      #תן לי את כל הספרים שרואי  כתב
      action.execute("select * FROM books WHERE author LIKE ?",(name,))
      #לאסוף את כל הספרים שחזרו מהשאילתה 
      result = action.fetchall()
      #לעבור על רשימה פריט פריט 
      for b in result:
         print (b[1] , " by " ,b[2] , ",year" ,b[3])
      #3.להציג יפה למשתמשים את התוצאות

#search()
  
#פונקציה שמאפשרת למחוק ספר
#פונקציה שמוחקת את כל הספרים 

def delete_books():
     #קולטים מהמשתמש תשובה אם הוא בטוח בכן/לא 
     answer = input("are you sure you want to delete all books? yes/no")
     #אם כתב כן 
     if answer == "yes":   
        #להוציא שאילתה שמוחקת את כל הספרים בטבלה 
        action.execute("DELETE FROM books")
        #לשמור את השינויים בבסיס הנתונים 
        database.commit()
        #הדפסה של תגובה למשתמשים
        print ("all books deleted")
     #אם לא אז לא עושים כלום

#delete_books()
#show_books()

def menu():
      print("==== book manager ====")
      print ("1. Delete all books")
      print ("2. Search by author")
      print ("3. Show all books")
      print ("4. Add book")
      print ("5. Exit")

while 1==1:
      menu()
      user = input("choose an option")
      if user == "1":
            delete_books()
      #חיבור של else ו if 
      elif user == "2":
            search()

      elif user == "3":
            show_books()
            
      elif user == "4":
            add_book()
      #לסגור את החיבור לבסיס הנתונים
      elif user == "5":
            print ("goodbye!")
            database.close()
      #אם לא בחרו שום מספר שבדקנו בתנאים לפני
      else:
            print ("invalid choice")