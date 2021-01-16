### There should always be a structure to your program.
### Learn to write as much comments as possible.
### Any one can code. You can get almost anything through google. But what is actually tested is your way of thinking
### the problem. Writting comments will help in understanding.
### Always try to avoid using built in language methods and do it old fashioned way (especially when you are starting out)
def is_palindrome(input_string):
    left, right = 0, len(input_string) - 1
    while left < right:
        if not input_string[left].isalnum():
            left += 1
        elif not input_string[right].isalnum():
            right -= 1
        else:
            if input_string[left].lower() != input_string[right].lower():
                return False
            else:
                left += 1
                right -= 1
    return True
def main():
    input_string = input("  Please enter the string to check if it is a palindrome : ")
    if is_palindrome(input_string):
        print(" Correct answer !!!",input_string," is a valid palindrome. ")
    else:
        print(" ",input_string," is not a valid palindrome. ")
if __name__:
    main()
