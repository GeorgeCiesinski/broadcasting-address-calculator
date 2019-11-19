def my_broadcast_calc(ip, subnet):

    # Prints ip input
    print(f"The ip value is: {ip}")

    # Checks if subnet is a CIDR value and converts it to decimal ip
    if len(subnet)==1 or len(subnet)==2:
        # Calls convert_cidr, passes int of subnet
        subnet = convert_cidr(int(subnet))
        print(f"The subnet value is: {subnet}")

    # Advises if CIDR is invalid
    if subnet == None:
        print("Invalid CIDR entered. Enter a value between 0 - 32")

    # Validates IP and Subnet
    valid_ip = validate(ip)

    # Ensures subnet isn't none, then calls validate
    if subnet != None:
        valid_subnet = validate(subnet)
    else:
        valid_subnet = None

    # Checks if None returned indicating invalid IP
    if valid_ip == None:
        print("Ip is not valid")

    # Checks if None returned indicating invalid Subnet
    if valid_subnet == None:
        print("Subnet is not valid")

    # If both ip and subnet are valid, calls build_broadcast to build the broadcast address
    if valid_ip and valid_subnet:
        print("IP and Subnet are valid.")
        broadcast_address = build_broadcast(valid_ip, valid_subnet)
        print(f"The broadcast address is: {broadcast_address}")
    else:
        print("Either the IP or Subnet are invalid. Unable to calculate broadcast address.")

    

def convert_cidr(cidr):

    # Checks if CIDR is valid
    if cidr >= 0 and cidr <= 32:
        pass
    else:
        return None
    
    # Creates empty subnet string
    subnet = ""

    # Creates binary for last octet
    last_oct = "00000000"

    # Find quotient and remainder
    quotient = cidr // 8
    remainder = cidr % 8

    if quotient == 4:
        subnet = "255.255.255.255"
        return subnet
    else:
        # Adds 255 and . for each quotient
        for i in range(quotient):
            subnet += "255"
            subnet += "."

    # Splits last oct into string
    last_oct_list = list(last_oct)

    # Changes string values to 1 up to the remainder
    for i in range(remainder):
        last_oct_list[i]="1"

    # Joins list back into string
    last_oct = "".join(last_oct_list)

    # Converts binary string to integer, then converts this to string
    octet = str(int(last_oct, 2))

    # Concatenates last octet to subnet
    subnet+=octet

    # Finishes subnet by checking resulting length, and adding remaining string
    if len(subnet) < 12 and len(subnet) > 7:
        subnet += ".0"
    elif len(subnet) < 8 and len(subnet) > 3:
        subnet += ".0.0"
    else:
        subnet += ".0.0.0"

    # Returns result
    return subnet

def build_broadcast(valid_ip, valid_subnet):

    # Creates empty list
    broadcast_value = []

    # Shortens variables
    ip = valid_ip
    subnet = valid_subnet

    # Builds broadcasting address by looping and applying subnet octets to ip octets
    for i in range(4):

        # If subnet octet is 255, keep IP octet        
        if subnet[i] == 255:
            broadcast_value.append(ip[i])
        # If subnet octet is 0, use 255
        elif subnet[i] == 0:
            broadcast_value.append(255)
        # If other, call apply_subnet calculation
        else:
            result = apply_subnet(ip[i], subnet[i])
            broadcast_value.append(result)

    # Convert integers in list to string
    for i in range(4):
        broadcast_value[i] = str(broadcast_value[i])

    # Concatenate string into broadcast address
    broadcast_address = ".".join(broadcast_value)

    # Return broadcast address
    return broadcast_address

def apply_subnet(ip_octet, subnet_octet):

    # Formula to apply subnet octet to ip octet
    o = 256 - subnet_octet
    i = (ip_octet // o) + 1
    j = (o * i) - 1

    # Return resulting octet
    return j 
    
def validate(value):

    # Empty list
    valid_value = []
    
    # Splits into segments
    octets = value.split(".")

    # Checks if there are 4 segments:
    if len(octets) != 4:
        return None
    
    # Checks if segments are between 0 - 255
    for octet in octets:
        octet = int(octet)
        if octet >= 0 and octet <= 255:
            valid_value.append(octet)
        else:
            return None

    # Returns validated ip or subnet
    return valid_value


"""
PROGRAM STARTS HERE
"""

# Prompts user for input
user_input = input(
    """Please enter an IP address and subnet mask separated by comma:

Examples:
172.16.200.123, 255.255.255.0
172.16.200.123, 24: """)

# Splits user input into list containing IP and subnet
values = user_input.split(",")

# Assigns IP value
ip = values[0]

# Assigns subnet, strips white space (space after comma)
subnet = values[1].strip()

# Calls my_broadcast_calc, passes values
my_broadcast_calc(ip, subnet)
