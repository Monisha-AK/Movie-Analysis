# MOVIE ANALYSIS

# Importing libraries
import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate
from datetime import datetime
import random
import time

# Importing csv files
pwd=pd.read_csv("pwd.csv",index_col='username')
movie=pd.read_csv("movie.csv",index_col='MOVIE NAME')
book=pd.read_csv("book.csv",index_col='NAME')

# Main screen
print('''
    __________________________________________________________________
                                  WELCOME !
    __________________________________________________________________
    ''')
name=(input('Enter your name to continue : '))

def main_menu():
    print('''
    1. Login using existing account
    2. Create new account
    3. Exit
    ''')
    x=int(input('Enter your choice : '))
    print()
    if x==1:
        login()
    elif x==2:
        create_account()
    else:
        print('Thank You!')
    print()

def login():
    count=0
    while count<3:
        user=input('Enter User ID : ')
        pas=input('Enter Password : ')
        if user in pwd.index:
            p=str(pwd.loc[user,'password'])
            if p==pas:
                print('Access Granted!')
                print()
                print('Welcome', name,'!')
                menu()
                break
                
            else:
                print('Wrong Password')
                print('Try Again!')
                print()
        else:
            print('Wrong User Id')
            print('Try Again!')
            print()
        count=count+1
    if count==3:
            print('Access Denied!')

def create_account():
    user1=input('Enter User ID : ')
    pas1=input('Enter Password : ')
    pwd.loc[user1]=pas1
    pwd.to_csv("pwd.csv")
    print('Account created successfully!')
    print('''
    1.Back to main screen
    2.Exit
    ''')
    y=int(input('Enter your choice : '))
    print()
    if y==1:
        main_menu()
    else:
        print('Thank You!')

def menu():
  while True:
    time.sleep(1)
    print('''
    __________________________________________________________________
                               MOVIE ANALYSIS
    __________________________________________________________________

         ************************** MENU **************************


    1. Display details of all the movies 
    2. Display details of a specific movie
    3. Add details of a movie
    4. Modify details of a movie
    5. Delete details of a movie
    6. Search movie details by genre
    7. Data visualisation
    8. Book my show
    9. Exit
    ''')

    z=int(input('Enter your choice : '))
    print()
    if z==1:
        e1()
    elif z==2:
        e2()
    elif z==3:
        e3()
    elif z==4:
        e4()
    elif z==5:
        e5()
    elif z==6:
        e6()
    elif z==7:
        e7()
    elif z==8:
        e8()
        break
    elif z==9:
        print('''
    __________________________________________________________________
                   THANK YOU FOR USING OUR APPLICATION !!!
    __________________________________________________________________''')
        break
    else:
        print('Invalid choice!')


# Display details of all the movies        
def e1():
    print('********************** MOVIE DETAILS **********************')
    print()
    print(movie)
    
# Display details of a specific movie
def e2():
    print('************ MOVIE DETAILS OF A SPECIFIC MOVIE ************')
    print()
    for i in movie.index:
        print(i)
    print()
    mov1=input('Enter the name of the movie: ')
    print()
    print(movie.loc[mov1])

# Add details of a movie
def e3():
    print('****************** ADD DETAILS OF A MOVIE ******************')
    print()
    mov1=input('Enter the movie name: ')
    date1=input('Enter the release year: ')
    genre1=input('Enter the movie genre: ')
    income1=float(input('Enter the movie income(in crores): '))
    imdb1=float(input('Enter the IMDb rating: '))
    movie.loc[mov1]=[date1,genre1,income1,imdb1]
    movie.to_csv("movie.csv")
    print('Details added successfully!')
    
# Modify details of a movie
def e4():
    print('***************** MODIFY DETAILS OF A MOVIE *****************')
    print('''
    1. Release year
    2. Movie Genre
    3. Movie Income
    4. IMDb Rating
    ''')
    a=int(input('Enter your choice you wish to modify: '))
    mov1=input('Enter the name of the movie: ')
    if a==1:
        date1=input('Enter the release year: ')
        movie.loc[mov1,'release year']=date1
    elif a==2:
        genre1=input('Enter the movie genre: ')
        movie.loc[mov1,'GENRE']=genre1
    elif a==3:
        income1=float(input('Enter the movie income(in crores): '))
        movie.loc[mov1,'INCOME(IN CRORES)']=income1
    elif a==4:
        imdb1=float(input('Enter the IMDb rating: '))
        movie.loc[mov1,'IMDB RATING']=imdb1
    else:
        print('Invalid choice')
    movie.to_csv("movie.csv")
    print('Details modified successfully!')
    
# Delete details of a movie
def e5():
    print('***************** DELETE DETAILS OF A MOVIE *****************')
    print()
    mov1=input('Enter the name of the movie : ')
    movie.drop([mov1],inplace=True)
    movie.to_csv("movie.csv")
    print('Details deleted successfully!')

# Search movie details by genre(filtering conditions)
def e6():
    print('****************** SEARCH MOVIES BY GENRE ******************')
    print()
    gen1=input('Enter the genre you wish to search: ')
    print()
    if gen1 not in (list(movie['GENRE'])):
        print(gen1,'movies not found!')
    else:
        movies=movie.loc[movie['GENRE']==gen1]
        print(movies)
        
# Graphs of movie income
def income_graphs():
    movie_name=movie.index
    income=list(movie['INCOME(IN CRORES)'])
    colr=['#267A9E','#51A885','#F5A936','#DB7476','#986B9B']
    print('''**** Data visualisation in terms of Movie Income ****

    1. Bar graph
    2. Pie chart
    3. Back to menu
    ''')
    c=int(input('Enter your choice: '))
    if c==1:
        # bar graph
        plt.bar(movie_name,income,color=colr)
        plt.title('MOVIE INCOME')
        plt.xlabel('MOVIE NAME')
        plt.ylabel('INCOME(IN CRORES)')
        plt.xticks(rotation=90)
        plt.show()
    elif c==2:
        # pie chart
        plt.pie(income,labels=movie_name,autopct='%2.2f%%')
        plt.title('MOVIE INCOME (IN CRORES)')
        plt.show()
    elif c==3:
        menu()
    else:
        print('Invalid choice!')
    print()
    income_graphs()

# Graphs of IMBd Rating
def rating_graphs():
    movie_name=movie.index
    imdb=list(movie['IMDB RATING'])
    colr=['#267A9E','#51A885','#F5A936','#DB7476','#986B9B']
    print('''**** Data visualisation in terms of Movie IMDb Rating ****

    1. Bar graph
    2. Pie chart
    3. Back to menu
    ''')
    c=int(input('Enter your choice: '))
    if c==1:
        # bar graph
        plt.bar(movie_name,imdb,color=colr)
        plt.title('MOVIE IMDb RATING')
        plt.xlabel('MOVIE NAME')
        plt.ylabel('MOVIE IMDb RATING')
        plt.xticks(rotation=90)
        plt.show()
    elif c==2:
        # pie chart
        plt.pie(imdb,labels=movie_name,autopct='%2.2f%%')
        plt.title('MOVIE IMDb RATING')
        plt.show()
    elif c==3:
        menu()
    else:
        print('Invalid choice!')
    print()
    rating_graphs()
    
# Data visualisation
def e7():
    print('********************* DATA VISUALISATION *********************')
    print()
    print('''
    1. Data visualisation in terms of Movie Income
    2. Data visualisation in terms of Movie IMDb Rating
    ''')
    ch=int(input('Enter your choice: '))
    if ch==1:
        income_graphs()
    elif ch==2:
        rating_graphs()
    else:
        print('Invalid choice!')

# Book my show
def e8():
    print('*********************** BOOK MY SHOW ***********************')
    print()
    print(''' Ayo movie lovers! What movie do you want to watch?
    Movies available for booking:
        1. Titanic
        2. Joker
        3. Top Gun
        4. Oppenheimer
        5. Inception
    ''')
    ch=int(input('Enter the name of the movie: '))
    if ch==1:
        mov='Titanic'
    elif ch==2:
        mov='Joker'
    elif ch==3:
        mov='Top Gun'
    elif ch==4:
        mov='Oppenheimer'
    elif ch==5:
        mov='Inception'
    else:
        print('Invalid choice!')
    n=int(input('Enter the number of tickets: '))
    amt=n*300
    book.loc[mov,'SEATS']-=n
    book.to_csv("book.csv")
    print()

    d={1:'Morning show -- 10:30 am to 01:30 pm',
       2:'Evening show -- 03:00 pm to 06:30 pm',
       3:'Night show -- 09:00 pm to 12:00 am'}
    for i,j in d.items():
        print(i,':',j)
    tym=int(input('Enter your choice of timings: '))
    t=d[tym]
    print()

    print('Your total amount is Rs',amt)
    print('''1. Gpay
2. Net banking
3. Paytm
4. Debit card
5. Credit card''')
    pay=int(input('Enter the choice of mode of payment: '))
    print()
    ph_no=int(input('Enter your phone number: '))
    print('Sending OTP to your phone number... ')
    otp=random.randint(1000,10000)
    time.sleep(2)
    print('''
             +------------------------+
             |    Your OTP : ''',otp,'''   |
             +------------------------+''')
    print()
    otp1=int(input('Enter the OTP : '))
    if otp==otp1:
        pin=input('Enter your pin: ')
        print()

        w=input('Confirm your booking? (Y/N): ')
        if w=='Y' or 'y':
            cur_date=datetime.now().date()
            ctime=datetime.now().time()
            cur_time=str(ctime)[:-7]
            
            lst=[cur_date,cur_time,name,mov,ph_no,n,amt,t]
                 
            bill=pd.DataFrame(lst,index=['Date of booking','Time of booking','Name','Movie',
                'Phone number','Number of tickets booked','Total amount','Movie timings'])
            print('''
    __________________________________________________________________
                                   BILL
    __________________________________________________________________''')
            print()
            print(tabulate(bill,tablefmt='fancy_grid'))
            print()
            print(book.loc[mov,'SEATS'],'seats are left for',mov)
            print('Your booking has been confirmed!')
            print('THANK YOU FOR VISITING!   ENJOY YOUR SHOW!')

            print('''
    1.Back to menu
    2.Exit
    ''')
            u=int(input('Enter your choice : '))
            print()
            if u==1:
                menu()
            else:
                print('''
    __________________________________________________________________
                   THANK YOU FOR USING OUR APPLICATION !!!
    __________________________________________________________________''')
            
        elif w=='N' or 'n':
                menu()
            
    else:
        print('Wrong otp!')
        print('Try again!')
        print()
        e8()
        
# Calling the main menu function(main screen)
main_menu()


