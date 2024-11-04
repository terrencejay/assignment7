def weather():
    try: #starting try block
        temp = int(input("Enter the temperature in farenheit: ")) #asking user for information. 
    except ValueError as e: #ValueErrors ore for when users enter the wrong datatype
        print("please enter a valid number.", e) #assuming user enters letter(s) instead of integer
    else: #start of else block
        hotcold = (temp - 32) * 5/9 #Converting degrees into celcius
        result = round(hotcold) #rounding information to the nearest whole number.
        print (f"The temperature {temp} in celcius is {result}") 
    finally:
        print("Thanks for using the weather app")

weather()

