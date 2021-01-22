def number_is_valid(number: str, inter: bool = True) -> list:
    """ Verify if the given number is valid

    Args:
        number (str): The phone number to be validated
        inter (bool, optional): The number has international identification code. Defaults to True.

    Returns:
        list: return a list containing all errors identified. If the list is empty it means the number is valid.
    """
    number = number.strip()
    network_codes = ["82", "83", "84", "85", "86", "87"]
    number_size = 12 if inter else 9
    error_messages = []

    error_type = {
        "size": f"The phone number must be :attr: characters long. currently with {len(number)}.",
        "format": "The phone number must start with 258.",
        "network_code": f"Invalid network code. Valid codes: {network_codes}."
    }

    if len(number) != number_size:
        error_messages.append(
            error_type["size"].replace(":attr:", str(number_size)))

    if inter:
        number = number.replace("+", "")

        if "258" not in number[:3]:
            error_messages.append(error_type["format"])

        if number[3:5] not in network_codes:
            error_messages.append(error_type["network_code"])
    else:
        if number[:2] not in network_codes:
            error_messages.append(error_type["network_code"])

    return error_messages
