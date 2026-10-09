import itertools


chars = input("Enter characters to use (e.g., abc123): ")
pass_length = int(input("Enter the length of each password: "))
file_name = input("Enter the password file name (e.g., passwords.txt): ")


with open(file_name, 'w', encoding='utf-8') as f:
    print("\nGenerating combinations... Please wait.")
    
    # product() function saare possible combinations (with repetition) banata hai
    count = 0
    for combo in itertools.product(chars, repeat=pass_length):
        # combo ek tuple hota hai (e.g., ('a', 'b', 'c')), use join karke string banate hain
        password = "".join(combo)
        f.write(password + "\n")
        count += 1

print(f"\nSuccess! {count} combinations save ho gaye hain '{file_name}' mein.")
