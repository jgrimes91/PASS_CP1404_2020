original_word = "ASTRONOMER"

secret_word = original_word[-3]
secret_word = secret_word + original_word[4]
secret_word = secret_word + original_word[6]
secret_word = secret_word + original_word[-5] + " "
secret_word = secret_word + original_word[-9]
secret_word = secret_word + original_word[2]
secret_word = secret_word + original_word[0]
secret_word = secret_word + original_word[-1]
secret_word = secret_word + original_word[8]
secret_word = secret_word + original_word[3]

print(secret_word)
