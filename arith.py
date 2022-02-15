# Christopher Agou

'''
Create a function that receives a list of strings that are arithmetic problems and 
returns the problems arranged vertically and side-by-side. The function should optionally 
take a second argument. When the second argument is set to True, the answers should be displayed.
'''

def arithmetic_arranger(inp, logi = False):
    if len(inp) > 5:
        return "Error: Too many problems."
    
    top = ''
    bottom = ''
    lines = ''
    operator = ''
    total =''
    new_e = list()
    spac = ' ' * 4

    for equ in inp:
        equ = equ.split()
        new_e.append(equ)
    #print(new_e)

    for equ in new_e:

        if equ[1] == '/' or equ[1] == '*':
            
            return "Error: Operator must be '+' or '-'."

        if equ[0].isdigit() and equ[2].isdigit():
            pass
        else:
            return "Error: Numbers must only contain digits."

        if len(equ[0]) > 4 or len(equ[2]) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        tops = equ[0]
        #print(tops)
        bot = equ[2]
        #print(bot)
        operator = equ[1]
        #print(operator)
        tol_spa = max(len(tops), len(bot)) + 2
        #print(tol_spa)
        lin = '-'
        
        if operator == '+':
            tol = str(int(tops) + int(bot))
        else:
            tol = str(int(tops) - int(bot))

        line1 = tops.rjust(tol_spa)
        line2 = operator + bot.rjust(tol_spa - 1)
        #line =''
        add = tol.rjust(tol_spa)
        if equ != new_e[-1]:
            top += line1 + spac
            bottom += line2 + spac
            lines += (lin * tol_spa) + spac 
            total += add + spac
        else:
            top += line1
            bottom += str(line2)
            lines += (lin * tol_spa)
            total += add 

        if logi == True:
            arranged_problems = top + '\n' + bottom + '\n' + lines + '\n' + total
        else:
            arranged_problems = top + '\n' + bottom + '\n' + lines

    return arranged_problems


        

print(arithmetic_arranger(['3 / 855', '3801 - 2', '45 + 43', '123 + 49']))
