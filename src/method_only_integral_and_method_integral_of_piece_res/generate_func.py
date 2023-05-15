from random import *
from sympy import *

from method_only_integral_and_method_integral_of_piece_res.arrays_variable_and_symbols import *

def generate_trig_func(element):
    triganomterix_variable = randint(1, 4)
    if (triganomterix_variable == 1):
        sin = symbols(f'sin({array_coefficients_for_argument_triganometrix[element] * x})')
        array_trig.append(sin)
    elif (triganomterix_variable == 2):
        cos = symbols(f'cos({array_coefficients_for_argument_triganometrix[element] * x})')
        array_trig.append(cos)
    elif (triganomterix_variable == 3):
        tan = symbols(f'tan({array_coefficients_for_argument_triganometrix[element] * x})')
        array_trig.append(tan)
    else:
        ctg = symbols(f'ctg({array_coefficients_for_argument_triganometrix[element] * x})')
        array_trig.append(ctg)

def generate_trig_func_with_degree(element):
    triganomterix_variable = randint(1, 4)
    if (triganomterix_variable == 1):
        sin = symbols(f'sin({array_coefficients_for_argument_triganometrix[element] * x})^({array_degree_trig[element]})')
        array_trig.append(sin)
    elif (triganomterix_variable == 2):
        cos = symbols(f'cos({array_coefficients_for_argument_triganometrix[element] * x})^({array_degree_trig[element]})')
        array_trig.append(cos)
    elif (triganomterix_variable == 3):
        tan = symbols(f'tan({array_coefficients_for_argument_triganometrix[element] * x})^({array_degree_trig[element]})')
        array_trig.append(tan)
    else:
        ctg = symbols(f'ctg({array_coefficients_for_argument_triganometrix[element] * x})^({array_degree_trig[element]})')
        array_trig.append(ctg)

def generate_trig_up_func_with_degree(element):
    triganomterix_up_variable = randint(1, 4)
    if (triganomterix_up_variable == 1):
        arcsin = symbols(f'arcsin({array_coefficients_for_argument_triganometrix_up[element] * x})^({array_degree_trig[element]})')
        array_trig.append(arcsin)
    elif (triganomterix_up_variable == 2):
        arccos = symbols(f'arccos({array_coefficients_for_argument_triganometrix_up[element] * x})^({array_degree_trig[element]})')
        array_trig.append(arccos)
    elif (triganomterix_up_variable == 3):
        arctan = symbols(f'arctan({array_coefficients_for_argument_triganometrix_up[element] * x})^({array_degree_trig[element]})')
        array_trig.append(arctan)
    else:
        arcctg = symbols(f'arcctg({array_coefficients_for_argument_triganometrix_up[element] * x})^({array_degree_trig[element]})')
        array_trig.append(arcctg)

def generate_exp_func(element):
    exp = symbols(f'exp({array_coefficients_for_argument_exp[element] * x})')
    array_exp.append(exp)

def generate_logarifm_func(element):
    log = symbols(f'log{integral_base}({array_coefficients_logarifm[element] * x})')
    array_logarifm.append(log)

def generate_trig_up_func(element):
    triganometrix_up_variable = randint(1, 4)
    if (triganometrix_up_variable == 1):
        arcsin = symbols(f'arcsin({array_coefficients_for_argument_triganometrix_up[element] * x})')
        array_trig.append(arcsin)
    elif (triganometrix_up_variable == 2):
        arccos = symbols(f'arccos({array_coefficients_for_argument_triganometrix_up[element] * x})')
        array_trig.append(arccos)
    elif (triganometrix_up_variable == 3):
        arctg = symbols(f'arctg({array_coefficients_for_argument_triganometrix_up[element] * x})')
        array_trig.append(arctg)
    elif (triganometrix_up_variable == 4):
        arcctg = symbols(f'arcctg({array_coefficients_for_argument_triganometrix_up[element] * x})')
        array_trig.append(arcctg)
    
def generate_power_func(element):
    power = symbols(f'{array_coefficients_power[element]}^({array_coefficients_for_argument_power[element] * x})')
    array_power.append(power)

