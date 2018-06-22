#1- Create a circle class and initialize it with radius. Make two methods getArea and getCircumference inside this class.

class Circle:
    def __init__(self,r):
        self.radius = r
        
    def getArea(self):
        self.radius = 3.14*self.radius*self.radius
        return(self.radius)

    def getCircumference(self):
        self.radius = 2*3.14*self.radius
        return(self.radius)
    
ob1 = Circle(1.21)
print("The area of the circle is : %0.2f"%(ob1.getArea()))
print("The circumference of the circle is: %0.2f"%(ob1.getCircumference()))

print("\n")
print("*"*10)
print("\n")

#2-Create a Student class and initialize it with name and roll number. Make methods to :
#1. Display - It should display all informations of the student.

class Student :
    def __init__(self,n,rn):
        self.name = n
        self.roll_num = rn

    def display(self):
        print("Student's name:",self.name)
        print("Student's roll number:",self.roll_num)

ob2 = Student('Meenal',15)
ob2.display()

print("\n")
print("*"*10)
print("\n")

#3-Create a Temprature class. Make two methods :
#1. convertFahrenheit - It will take celsius and will print it into Fahrenheit.
#2. convertCelsius - It will take Fahrenheit and will convert it into Celsius.

#(farenhiet-32)*(5/9)(celsius*(9/5))+32
class Temperature:

    def convertFahrenheit(self,celsius):
        fahrenheit = (celsius*(9/5)+32)
        return(fahrenheit)

    def convertCelsius(self,fahrenheit):
        celsius = (fahrenheit-32)*(5/9)
        return(celsius)
ob3 = Temperature()
print("temp from celsius to fahrenheit is %0.2f:"%(ob3.convertFahrenheit(12)))
print("temp from fahrenheit to celsius is %0.2f:"%(ob3.convertCelsius(53.6)))

print("\n")
print("*"*10)
print("\n")

#4- Create a class MovieDetails and initialize it with Movie name, artistname,Year of release and ratings .
#Make methods to 
#1. Display-Display the details.
#2. Update- Update the movie details.

class MovieDetails:

    def __init__(self,movie_name,artist_name,release_yr,rating):
        self.movie_name = movie_name
        self.artist_name = artist_name
        self.release_yr = release_yr
        self.rating = rating

    def display(self):
        print("MOVIE NAME:",self.movie_name)
        print("ARTIST NAME:",self.artist_name)
        print("YEAR OF RELEASE:",self.release_yr)
        print("RATINGS:",self.rating)

    def update_details(self,movie_name,artist_name,release_yr,rating):
        self.movie_name = movie_name
        self.artist_name = artist_name
        self.release_yr = release_yr
        self.rating = rating
      
ob4 = MovieDetails('Raazi','xyz',2018,7.9)
print("Movie Details:")
ob4.display()
print("\n")
print("Updated Movie Details:")
ob4.update_details('YJHD','mno',2012,8.2)
ob4.display()

print("\n")
print("*"*10)
print("\n")

#5- Create a class Expenditure and initialize it with expenditure,savings.Make the following methods. 
#1. Display expenditure and savings 
#2. Calculate total salary
#3. Display salary

class Expenditure:
    def __init__(self,expend,savings):
        
        self.expend = expend
        self.savings = savings

    def display(self):
        print("EXPENDITURE:",self.expend)
        print("SAVINGS:",self.savings)

    def t_salary(self):
        total_salary = self.expend + self.savings
        return(total_salary)
    
    def p_salary(self):
        print("SALARY:",self.t_salary())
       
ob5 = Expenditure(100,1100)
ob5.display()
ob5.p_salary()

print("\n")
print("*"*10)
print("\n")


