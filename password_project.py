import string
import random 


uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase
digits = string.digits
special_chars = string.punctuation
class ValidationError(Exception):
    """
    Custom exception used for password generation validation errors,
    such as when the requested length is too short.
    """
    pass
def generate_password(length = 9):
    """
    Generates a random password that includes at least one uppercase letter,
    one lowercase letter, one digit, and one special character.

    Args:
        length (int): Desired length of the password. Must be at least 6.

    Returns:
        str: A randomly generated password that meets all the criteria.

    Raises:
        ValidationError: If the provided length is less than 6.
    """
    if length < 6:
        raise ValidationError("Password length should be at least 6")

    password_chars = [random.choice(uppercase), 
                      random.choice(special_chars),
                      random.choice(lowercase),
                      random.choice(digits)]

    for i in range(length - 4):
        password_chars += random.choice(uppercase + lowercase + digits + special_chars)
   
    random.shuffle(password_chars)
    password = ''.join(password_chars)

    return password
    
def password_validator(password: str):
    """
    Validates a password to ensure it meets the following criteria:
    - At least 6 characters long
    - Contains at least one uppercase letter
    - Contains at least one lowercase letter
    - Contains at least one digit
    - Contains at least one special character

    Args:
        password (str): The password string to validate.

    Raises:
        ValueError: If the password does not meet one or more criteria.
    """
    if password is None:
        raise ValueError('Validation Error: Password cannot be empty.')
    if len(password) < 6:
        raise ValueError('Sorry, your password must have a minimum length of 6 characters.')
    if not any(i in uppercase for i in password):
        raise ValueError('Sorry, your password must include at least one uppercase letter.')
    if not any(i in lowercase for i in password):
        raise ValueError('Sorry, your password must include at least one lowercase letter.')
    if not any(i in digits for i in password):
        raise ValueError('Sorry, your password must include at least one digit.')
    if not any(i in special_chars for i in password):
        raise ValueError('Sorry, your password must include at least one special character.')
    print('Password is valid')


print("=== Password Generator and Validator ===")
yes_no = input('Do you want to generate a new password? (yes/no): ')
if yes_no == 'yes':
    try:
        length = int(input('Enter the desired password length (minimum 6): '))
        print(generate_password(length))
    except ValueError:
        print('Input Error: Password length must be a number.')
    except ValidationError as e:
        print(e)
elif yes_no == 'no':
    try:
        password = input('Enter your password to validate: ')
        password_validator(password)
    except ValueError as e:
        print(e)
    
