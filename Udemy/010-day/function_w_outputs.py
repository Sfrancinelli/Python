# Functions with Outputs

def format_name(f_name, l_name):
    formated_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_name} {formated_l_name}"

output = format_name("SebAsTiAn", "FranCinElli")
print(output)