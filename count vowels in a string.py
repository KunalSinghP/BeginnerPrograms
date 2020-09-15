def get_count(input_str):
    num_vowels = 0
    input_str=input_str.lower()
    for i in input_str:
        if i=="a":
            num_vowels+=1
        elif i=="e":
            num_vowels+=1
        elif i=="i":
            num_vowels+=1
        elif i=="o":
            num_vowels+=1
        elif i=="u":
            num_vowels+=1
    # your code here
    print(num_vowels)

    return num_vowels
get_count("kunal")
