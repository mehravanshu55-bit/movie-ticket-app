def extract_year(date_str : str) -> float:
    """pull out the year out of the datestring.

    assume the year is the first four digits that appear, which hold for
    "2026-06-09" , "2026/04/03" and joined on "2026-12-11" alike

    args:
    date_str :any text containing a year , e.g. "2026-06-04".

    returns:
    the year as an int , e.g. 2026.
    """

    digit_character = ""
    for character in date_str:
        if character.isdigit() :
            digit_character += character

            first_four_digits = digit_character[:4]

            return int(first_four_digits)

        if __name__ == "__main__":
            test_cases: list[tuple[str,int]] = [
                ("2026-06-04",  2026),
                ("2026/12/11" , 2026),
                ("joined on 2026-03-04", 2026),
            ]

            for date_text , expected_year in test_cases:
                actual_year = extract_year(date_text)
                result_lable = "PASS" if actual_year == expected_year else "fail"
                print(f"[{result_lable}] {date_text!r:<24} expected {expected_year}, got{actual_year}")



        