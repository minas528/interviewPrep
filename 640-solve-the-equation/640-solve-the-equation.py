class Solution:
    def solveEquation(self, equation: str) -> str:
        equation = equation.replace('-','+-')

        left = equation.split('=')[0].split('+')
        right = equation.split('=')[1].split('+')

        left_int = sum([int(x) for x in left if x.lstrip('-').isdigit() and x!=''])
        right_int = sum([int(x) for x in right if x.lstrip('-').isdigit() and x!=''])

        left_x = [x for x in left if not x.lstrip('-').isdigit() and x!='']
        right_x = [x for x in right if not x.lstrip('-').isdigit() and x!='']
        left_x = sum([int(x.replace('x','1')) if x.lstrip('-')=='x' else int(x.replace('x','')) for x in left_x])
        right_x = sum([int(x.replace('x','1')) if x.lstrip('-')=='x' else int(x.replace('x','')) for x in right_x])

        final_x = left_x-right_x
        final_int = (left_int-right_int)*-1

        if final_x==0 and final_int==0:
            return 'Infinite solutions'
        if final_x==0 and final_int!=0:
            return 'No solution'

        x = final_int//final_x
        return 'x=%s' %x