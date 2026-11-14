# Helper Funciton : 
# Convert any positive or negative number (int or float) into a compact 
# human-readable string with suffixes (e.g., '1.2k', '-3.5M').
import math

def place_valid_num(num):
    sign = ("-" if num < 0 else "")
    magnitude = abs(num)
    
    if magnitude >= 1_000_000_000:
        val = math.floor((magnitude / 1_000_000_000)*100)/100
        return f"{sign}${val:.2f}B"
    elif magnitude >= 1_000_000:
        val = math.floor((magnitude / 1_000_000)*100)/100
        return f"{sign}${val:.2f}M"
    elif magnitude >= 1_000:
        val = math.floor((magnitude / 1_000)*100)/100
        return f"{sign}${val:.2f}K"
    else:
        val = math.floor(magnitude * 100)/100
        return f"{sign}${val:.2f}"


def detect_numeric_values(number):
    try:
        return int(number)
    except ValueError:
        try:
            val = float(number)
            return val if math.isfinite(val) else None
        except ValueError:
            return None


def numtostr(*numbers):
    if numbers:
        str_value_list = []
        for num in numbers:
            if not isinstance(num, (int, float, str)) or isinstance(num, bool):
                continue
                
            if isinstance(num, (int, float)):
                if not math.isfinite(num):
                    continue
                str_value_list.append(place_valid_num(num))
                
            elif isinstance(num, str):
                result = detect_numeric_values(num.strip())
                if result is not None:
                    str_value_list.append(place_valid_num(result))
                else:
                    continue
        return str_value_list
    else:
        return []