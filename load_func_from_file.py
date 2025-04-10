def load_function_from_file(filename):
    # Open the file with the correct encoding (UTF-16 in this case)
    with open(filename, 'r', encoding='utf-16') as file:
        expr_str = file.read().strip()
    
    # Optionally, remove any BOM if present
    expr_str = expr_str.lstrip('\ufeff')
    
    # Define the symbol and safely parse the expression
    x = symbols('x')
    expr = sympify(expr_str)
    
    # Convert the sympy expression into a callable function using lambdify
    f = lambdify(x, expr, modules="math")
    return f
