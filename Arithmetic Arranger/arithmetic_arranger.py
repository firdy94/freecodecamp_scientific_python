def arithmetic_arranger(problems, operation_val=False):
    if len(problems) > 5:
        return("Error: Too many problems.")
    line_1_list, line_2_list, line_3_list, line_4_list = [], [], [], []

    for problem in problems:
        problem_split = problem.split()
        val_1, operator, val_2 = problem_split
        max_len_val = max(len(val_1), len(val_2))

        if operator not in ('+', '-'):
            return ("Error: Operator must be '+' or '-'.")
        elif len(val_1) > 4 or len(val_2) > 4:
            return ("Error: Numbers cannot be more than four digits.")
        try:

            int_1 = int(val_1)
            int_2 = int(val_2)
            if operation_val == True and operator == '+':
                tot_int = int_1+int_2
            elif operation_val == True and operator == '-':
                tot_int = int_1-int_2
            else:
                tot_int = ''
        except ValueError:
            return("Error: Numbers must only contain digits.")

        else:
            line_1_list.append(val_1.rjust(2+max_len_val))
            line_2_list.append(operator+val_2.rjust(1+max_len_val))
            line_3_list.append("-"*(2+max_len_val))
            line_4_list.append(str(tot_int).rjust(2+max_len_val))

    line_1_str = "    ".join(line_1_list)
    line_2_str = "    ".join(line_2_list)
    line_3_str = "    ".join(line_3_list)
    line_4_str = "    ".join(line_4_list)

    if operation_val == True:

        arranged_prob = line_1_str+"\n"+line_2_str+'\n'+line_3_str+"\n"+line_4_str
    else:
        arranged_prob = line_1_str+"\n"+line_2_str+'\n'+line_3_str

    return arranged_prob