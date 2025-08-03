# Exercise level: 1
import random
import string

# 1. Six character user ID
def random_user_id():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

print(random_user_id())

# 2. Generate user IDs by user input
def user_id_gen_by_user():
    length = int(input("Enter the length of each ID: "))
    count = int(input("Enter the number of IDs to generate: "))
    for _ in range(count):
        print(''.join(random.choices(string.ascii_letters + string.digits, k=length)))

# Example call (you can test by running):
# user_id_gen_by_user()

# 3. RGB color generator
def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r},{g},{b})"

print(rgb_color_gen())

# Exercise level: 2
# 1. List of hexadecimal colors
def list_of_hexa_colors(n):
    hex_colors = []
    for _ in range(n):
        color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        hex_colors.append(color)
    return hex_colors

print(list_of_hexa_colors(5))

# 2. List of RGB colors
def list_of_rgb_colors(n):
    return [rgb_color_gen() for _ in range(n)]

print(list_of_rgb_colors(3))

# 3. General color generator
def generate_colors(color_type, n):
    if color_type.lower() == 'hexa':
        return list_of_hexa_colors(n)
    elif color_type.lower() == 'rgb':
        return list_of_rgb_colors(n)
    else:
        return "Invalid color type. Choose 'hexa' or 'rgb'."

print(generate_colors('hexa', 3))
print(generate_colors('rgb', 2))

# Exercise level: 3
# 1. Shuffle a list
def shuffle_list(lst):
    random.shuffle(lst)
    return lst

print(shuffle_list([1, 2, 3, 4, 5]))

# 2. Seven unique random numbers between 0-9
def unique_random_numbers():
    return random.sample(range(10), 7)

print(unique_random_numbers())
