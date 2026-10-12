class Solution:
    def intToRoman(self, num: int) -> str:
        # Mapping of values to their Roman numeral representations, including subtractive pairs
        val_map = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I")
        ]
        
        roman_chars = []
        
        for value, symbol in val_map:
            if num == 0:
                break
            # Determine how many times the current symbol fits into the number
            count = num // value
            # Append the symbol that many times
            roman_chars.append(symbol * count)
            # Reduce the number by the accounted amount
            num %= value
            
        return "".join(roman_chars)