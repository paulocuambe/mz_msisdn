"""
--------------------------------------------------------
The Validator class.
This library check numbers, based on the format of Mozambican numbers.
--------------------------------------------------------
"""

class Validator:

    __error_type = {
        "size": "The phone number must be 9 or 12 characters long. currently with {}",
        "format": "The phone number must start with {}.",
        "network_code": "Invalid network code. {}."
    }
    
    __error_messages = []

    __codes =  {
        "mz": {
            "network_code": ["82", "83", "84", "85", "86", "87"],
            "country_code": ["258"]
        }
    }
 
    def __init__(self, number, format = "mz"):
        """
            Args:
            number (str): The phone number to be validated
            format (str, optional): The number has international identification code. Defaults to international.
        """
        self.number = str(number)
        self.format = format
        self.__validate_number()
    
    def get_country_code(self):
        if len(self.number) == 9:
            return self.__codes[self.format]["country_code"][0]
        return self.number[:3] 

    def get_network_code(self):
       if len(self.number) == 9:
            return self.number[:2]
       return self.number[3:5] 
    
    def get_full_number(self):
        return self.number

    def get_errors(self):
        return self.__error_messages

    def __validate_number(self):
        """ Verify if the number is valid"""
        
        self.__remove_signal_plus()

        if not self.__is_valid_length():
           self.__error_messages.append(
            self.__error_type["size"].format(len(self.number))
           )

        if self.get_country_code() not in self.__codes[self.format]["country_code"]:
            self.__error_messages.append(
            self.__error_type["format"].format(self.__codes[self.format]["country_code"])
            )
        
        if self.get_network_code() not in self.__codes[self.format]["network_code"]:
           self.__error_messages.append(
            self.__error_type["network_code"].format(self.__codes[self.format]["network_code"])
           )
    
    def __is_valid_length(self):
        if len(self.number) in [9, 12]:
            return True
        return False
    
    def __remove_signal_plus(self):
        self.number = self.number.strip().replace("+", "")    