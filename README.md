Validate Mozambican MSISDNs

## Installation

`pip install mz-msisdn`

## Validating Numbers

By default the validation function is setup to validate numbers in the international format.

```py
from mz_msisdn import mz_validator

# If the number is valid an empty array will be returned
mz_validator("258844245708") # []

# If the number is invalid an error bag containing all errors will be returned
errors = mz_validator("25889424570")
print(errors)
# ['The phone number must be 12 characters long. currently with 11.',
# "Invalid network code. Valid codes: ['82', '83', '84', '85', '86', '87']."]

```

If you want to validate numbers considering that you will only receive mozambican numbers, you can enable national formation as shown below:

```py
errors = mz_validator("89424570", nr_format="national")
# ['The phone number must be 9 characters long. currently with 8.',
# "Invalid network code. Valid codes: ['82', '83', '84', '85', '86', '87']."]
```
