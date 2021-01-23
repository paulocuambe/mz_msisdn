# Validate Mobile numbers from Mozambique

I was given a task to create a tool that should run through CSV files and verify wich of them are valid or invalid. The main functionality of it is to perform checks on numbers, so I extracted this part of the tool and made it open source so other people can use it.

## Installation

`pip install mznumber`

## Validating Numbers

By default the validation function is setup to validate numbers in the international format.

```py
from mznumber import number_is_valid

# If the number is valid an empty array will be returned
number_is_valid("258844245708") # []

# If the number is invalid an error bag containing all errors will be returned
errors = number_is_valid("25889424570")
print(errors)
# ['The phone number must be 12 characters long. currently with 11.', "Invalid network code. Valid codes: ['82', '83', '84', '85', '86', '87']."]

```

If you want to validate numbers considering that you will only receive mozambican numbers, you can enable national formation as shown below:

```py
# If you wish you can use the national format
errors = number_is_valid("89424570", inter=False)
# ['The phone number must be 9 characters long. currently with 8.', "Invalid network code. Valid codes: ['82', '83', '84', '85', '86', '87']."]
```