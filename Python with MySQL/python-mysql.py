import mysql.connector
from difflib import get_close_matches

connection = mysql.connector.connect( 
    user='ardit700_student',
    password='ardit700_student', 
    host='108.167.140.122',
    database = 'ardit700_pm1database'
)

def translate(word):
    cursor = connection.cursor()
    cursor.execute("select * from Dictionary where expression = '%s'" %word)
    result1 = cursor.fetchall()
    cursor.execute("select * from Dictionary where expression = '%s'" %word.lower())
    result2 = cursor.fetchall()
    cursor.execute("select * from Dictionary where expression = '%s'" %word.title())
    result3 = cursor.fetchall()
    cursor.execute("select * from Dictionary where expression = '%s'" %word.upper())
    result4 = cursor.fetchall()
    cursor.execute("select expression from Dictionary")
    result5 = cursor.fetchall()
    if len(result1) > 0:
        return result1
    elif len(result2) > 0:
        return result2
    elif len(result3) > 0: 
        return result3
    elif len(result4) > 0:
        return result4
    elif len(get_close_matches(word,result5,cutoff=0.8)) > 0:
        yn = input("Did you mean %s instead? Enter Y for yes or Enter N for No: " % get_close_matches(word,result5,cutoff = 0.8)[0])
        if yn == 'Y':
            return translate(get_close_matches(word,result5,cutoff = 0.8)[0])
        elif yn == 'N':
            return "Okay, try again with a different word."
        else:
            return "We didn't understand your entry. Try again later!"
    else:
        return "The word doesn't exist.Please try again."

word = input("Enter word: ")
output = translate(word)
if type(output) == list:
    t = 1
    for item in output:
        print("Meaning ",t,": ",item[1])
        t+=1
else:
    print(output)

connection.close()