import string, random, re
from termcolor import colored
# Regex patterns
common_pattern = r"(pass(word)?|login|hello|admin|secret|welcome)"
keyboard_pattern = r"(qwerty|asdf|zxcv|uiop|hjkl|vbnm|bnm|1234|12345678|1232456789|0987654321)"
number_sequence = r"(012|123|234|345|456|567|678|789)"
letter_sequence = r"(abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz)"
repeated_chars = r"(.)\1{2,}"

weak_patterns = [common_pattern, keyboard_pattern, number_sequence, letter_sequence, repeated_chars]

# Dictionary word check
def check_dictionary_words(password: str):
    try:
        from nltk.corpus import words
        dictionary_words = words.words()
    except:
        import nltk
        nltk.download('words')
        from nltk.corpus import words
        dictionary_words = words.words()
    if password.lower() in dictionary_words:
        return True, "⚠️ Avoid using common dictionary words."
    return False, ""

# Regex pattern match check
def check_weak_pattern(password: str) -> list:
    results = []
    for pattern in weak_patterns:
        match = re.search(pattern, password.lower())
        if match:
            results.append(match.group())
    return results

# Main password strength checker
def check_password(password: str) -> str:
    score = 0
    suggestion = "Use at least"
    warnings=[]
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in string.punctuation for c in password)

    if has_lower:
        score += 20
    else:
        suggestion += " one lowercase,"

    if has_upper:
        score += 20
    else:
        suggestion += " one uppercase,"

    if has_digit:
        score += 20
    else:
        suggestion += " one digit,"

    if has_symbol:
        score += 20
    else:
        suggestion += " one symbol,"

    if len(password) >= 8:
        score += 20
    else:
        suggestion += " minimum 8 characters,"

    # Remove trailing comma
    if suggestion.endswith(","):
        suggestion = suggestion[:-1]

    # Check dictionary word
    is_dict_word, dict_warning = check_dictionary_words(password)

    # Check weak pattern
    weak_patterns_found = check_weak_pattern(password)

    # Return early if dictionary word or weak pattern
    if is_dict_word:
        warnings.append(dict_warning)

    if weak_patterns_found:
        pattern_report = ",".join(f" - {p}" for p in weak_patterns_found)
        warnings.append(f"❌ Weak pattern(s) detected: {colored(pattern_report,'red')}.")
    warning=""
    if warnings:
        warning=f"⚠ Warning\t : "+"\n\t\t   ".join(warnings)
    # Final feedback based on score
    if score == 100:
        feedback = "✅ Your Password is Hard to Crack!"
    elif 80 < score < 100:
        feedback = "✅ Your Password is Very Strong.\n🛡 Suggestion\t : " + suggestion
    elif 60 < score <= 80:
        feedback = "⚠️ Your Password is Strong.\n🛡 Suggestion\t : " + suggestion
    elif 40 < score <= 60:
        feedback = "⚠️ Your Password is Good.\n🛡 Suggestion\t : " + suggestion
    else:
        feedback = "❌ Your Password is Weak.\n🛡 Suggestion\t : " + suggestion

    return f"\n🔐 Password Score: {score}/100\nℹ️ Feedback\t : {feedback}\n{warning}",[score,feedback,warnings]

# Strong password generator
def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.SystemRandom().choice(chars) for _ in range(length))

# CLI Interaction
def main():
    while True:
        password = input("\n🔐 Enter your Password( type x for exit ): ")
        if password in ("x","exit"):
            exit()
        print(check_password(password)[0])

        ask_gen = input("🔄 Want me to generate a secure password? (yes/no): ").lower()
        if ask_gen in ("yes", "y", "ok"):
            suggestion = generate_password()
            print(f"🛡 Suggested Strong Password: {suggestion}")

if __name__ == "__main__":
    main()
