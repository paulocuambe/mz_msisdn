Validate Mozambican MSISDNs

## Installation

`pip install mz-msisdn`

## Validating Numbers

```py
from mz_msisdn import Validator 

# example with correct number
numberValidated = Validator("+258844214545")
print(numberValidated.get_errors())
# [] 

# ===

# example with incorrect number
numberValidated = Validator("+25388421454")
print(numberValidated.get_errors())
# ['The phone number must be 9 or 12 characters long.', 
# 'The phone number must start with 258.',
# 'Invalid network code. 82, 83, 84, 85, 86, 87.']
```

## Validating Numbers Using Format

If you want to validate numbers considering that you will only receive mozambican numbers, you can enable mz formation as shown below:

```py
# example with correct number
numberValidated = Validator("844214546","mz")
print(numberValidated.get_errors())
# []

# example with incorrect number
numberValidated = Validator("894214546","mz")
print(numberValidated.get_errors())
# ["Invalid network code. ['82', '83', '84', '85', '86', '87']."]
```

### get_country_code()
Description: returns the country code

```py
print(numberValidated.get_country_code())
# 258
```

### get_network_code()
Description: returns the mobile network code

```py
print(numberValidated.get_network_code())
# 84
```

### get_full_number()
Description: returns the number 

```py
print(numberValidated.get_full_number())
# 258844214545
```