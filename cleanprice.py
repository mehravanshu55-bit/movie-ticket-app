
def clean_price(text: str) -> float:
    """
    turn messy text price into a number.
    args:
    raw price such as "Rs. 499", "1,299.00".
    return:
    the price as a float or 0.0 if the text contain no digit at all.
    """
    has_a_digit = False
    for character in text:
        if character.isdigit():
            has_a_digit = True
            if not has_a_digit:
                return 0.0
                kept_character = ""
                  # now we are making an empty string where useful characters are kept there
                for character in text:
                    if character.isdigit() or character == ".":
                        kept_character += character
                        cleaned_text = kept_character.strip(".")
                        # we had to remove unneccesary points or decimal to avoid miss reading
                        return float(cleaned_text)
                        if __name__ == "__main__":
                            sample_price = ["Rs. 499", "1,299.00", "FREE", "$50",""]
                            for sample in sample_prices:
                                        print(f"{sample!r:>12}  ->  {clean_price(sample)}")



                        
