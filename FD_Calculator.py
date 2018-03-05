import datetime as dt

def is_empty_string(input_value):
    if len(input_value.strip()) == 0:
        return True
    else:
        return False

def check_min_max(input, min, max, data_type):
    if (data_type == 'int' or data_type == 'float') and input >= min and input <= max :
        return True
    elif (data_type == 'string' and len(input.strip()) >= 5 and len(input.strip())<= 20):
        return True
    else:
        return False

def validate_input(input_value, data_type, min, max):

    valid_value = False

    if is_empty_string(input_value) == False:
        if data_type == 'int' and input_value.isdigit():
            input_value = int(input_value)
            valid_value = check_min_max(input_value, min, max, data_type)
        elif data_type == 'float':
            try:
                input_value = float(input_value)
                valid_value = check_min_max(input_value, min, max, data_type)
            except:
                valid_value = False
        elif data_type == 'string':
            try:
                int(input_value)
                valid_value = False
            except:
                valid_value = check_min_max(input_value, min, max,data_type)
    else:
        valid_value = False

    return { 'value' : input_value, 'valid' : valid_value}


def get_user_input(message, data_type, min_value = 1 , max_value = 30):
    user_input = input(message);
    validation_result = validate_input(user_input, data_type, min_value, max_value)

    while validation_result['valid'] == False:
        print("Invalid value. Please enter again.")
        user_input = input(message);
        validation_result = validate_input(user_input, data_type, min_value, max_value)

    return validation_result['value']


class Calculator:

    def rate_table(self):
        self.rate = 0
        if self.time in list(range(1, 3)) and self.customer_type == 1:
            self.rate = 6
        elif self.time in list(range(1, 3)) and self.customer_type == 2:
            self.rate = 6.5
        return self.rate


    def Calculator_main(self):
        self.customer_type = get_user_input("Type of Customer: Normal = 1 or SeniourCitizen = 2 --> ", 'int', 1, 2)
        self.principal_amount = get_user_input("Amount to deposit (Min: 1, Max: 10000000) --> ", 'float', 1, 10000000)
        #self.customer_name = get_user_input("Enter your name. Name should be min 5 characters and max 20 characters --> ", 'string', 5, 20)
        self.time = get_user_input("Enter the number of the years --> ",'int')
        self.frequency = get_user_input("Enter the frequency: 1 for Simple Interest,  2 for Compounded Yearly, 3 for Compounded Quartely --> ", 'int', 1, 3)

    def Interest_Earned(self, total, amount):
        self.total = total
        self.principal_amount = amount
        self.interest = self.total - self.principal_amount
        return self.interest

    def SimpleInterest(self):
        self.rate = self.rate_table()
        self.total = self.principal_amount * (1 + self.rate/100 * self.time)
        print('\nYour Maturity Value after %d year(s) will be %.2f' %(self.time,self.total))
        self.interest = self.Interest_Earned(self.total , self.principal_amount)
        print("Interest Earned will be %.2f" %self.interest)

    def Compounded(self):
        self.rate = self.rate_table()
        self.rate = self.rate/100
        if self.frequency == 2:
            n = 1
        elif self.frequency == 3:
            n = 4
        self.total = self.principal_amount * (1 + self.rate/n )** (self.time * n)
        print('\nYour Maturity Value after %d years will be %.2f' %(self.time,self.total))
        self.interest = self.Interest_Earned(self.total , self.principal_amount)
        print("Interest Earned will be %.2f" %self.interest)

    def Maturity_Value(self):
        if self.frequency == 1:
            self.SimpleInterest()
        elif self.frequency in (2,3):
            self.Compounded()


obj = Calculator()
obj.Calculator_main()
obj.Maturity_Value()





