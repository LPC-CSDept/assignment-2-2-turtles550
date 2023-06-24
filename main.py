def main():
    """
    ##################################################
    # Comlete your code here
    Use the same variables: celcius fahrenheit 
    ##################################################
    """
    # Get the temperature in Celsius from the user
    celcius = float(input("Enter the temperature in Celsius: "))

    # Convert Celsius to Fahrenheit
    fahrenheit = (celcius * 9/5) + 32

    # Display the converted temperature in Fahrenheit with two decimal places
    print("Fahrenheit: {:.2f}".format(fahrenheit))


    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return celcius, fahrenheit


if __name__ == '__main__':
    main()
