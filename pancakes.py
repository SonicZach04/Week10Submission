#Zachary Ball
#COP2500
#Program 8 - Pancakes
#4/4/2024

#Defining Functions

#main
def main():
    print("return_five:")
    print(return_five())
    print()

    print("pancake_printer:")
    print(pancake_printer())
    print()

    print("get_pancake_count:")
    print(get_pancake_count(2,35))
    print()

    print("get_pancakes_per_minute:")
    print(get_pancakes_per_minute(30,60))
    print()

    print("get_minutes_spent_eating:")
    print(get_minutes_spent_eating(120,2))
    print()

    print("print_pancake_count:")
    print_pancake_count(30,0.831)
    print()

    print("print_pancakes_per_minute:")
    print_pancakes_per_minute(21,49.2)
    print()

    print("print_minutes_spent_eating:")
    print_minutes_spent_eating(109.21,34.2)
    print()

    print("get_pancake_data:")
    print("%.3f"%get_pancake_data(0,20,38))
    print("%.3f"%get_pancake_data(22,0,12))
    print("%.3f"%get_pancake_data(48,56,0))
    print()

    print("print_pancake_data:")
    print_pancake_data(0,40,13)
    print_pancake_data(21,0,100)
    print_pancake_data(3,27,0)
    print()


#Other funtions
def return_five():
    return(5)

def pancake_printer():
    print("\"Pancake Breakfast with Professor Patrick!\"\n")
    return(52847)

#get functions
def get_pancake_count(minutes,pancakes_per_minute):
    count=minutes*pancakes_per_minute
    return(count)

def get_pancakes_per_minute(minutes,pancake_count):
    ppm=pancake_count/minutes
    return(ppm)

def get_minutes_spent_eating(pancake_count,pancakes_per_minute):
    minutes=pancake_count/pancakes_per_minute
    return(minutes)

#print functions
def print_pancake_count(minutes,pancakes_per_minute):
    total=minutes*pancakes_per_minute
    print("Pancakes consumed:%.3f"%total)

def print_pancakes_per_minute(minutes,pancake_count):
    ppm=pancake_count/minutes
    print("Pancakes per minute:%.3f"%ppm)

def print_minutes_spent_eating(pancake_count,pancakes_per_minute):
    minutes=pancake_count/pancakes_per_minute
    print("Minutes spent eating:%.3f"%minutes)

#data functions
def get_pancake_data(pancake_count,pancakes_per_minute,minutes):
    if(pancake_count==0):
        a=get_pancake_count(minutes,pancakes_per_minute)
        return(a)
    elif(pancakes_per_minute==0):
        b=get_pancakes_per_minute(minutes,pancake_count)
        return(b)
    elif(minutes==0):
       c=get_minutes_spent_eating(pancake_count,pancakes_per_minute)
       return(c)

def print_pancake_data(pancake_count,pancakes_per_minute,minutes):
    if(pancake_count==0):
        a=get_pancake_count(minutes,pancakes_per_minute)
        print("pancake count%.3f"%a)
    elif(pancakes_per_minute==0):
        b=get_pancakes_per_minute(minutes,pancake_count)
        print("Pancakes per minute:%.3f"%b)
    elif(minutes==0):
       c=get_minutes_spent_eating(pancake_count,pancakes_per_minute)
       print("Minutes:%.3f"%c)
    
#Running Main
main()
