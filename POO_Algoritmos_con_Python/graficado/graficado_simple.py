#incorporamos la libreria boke == figure: es la ventana donde vivira la grafica ; output_file:nombre del archivo ; show: abre aun servidore en html
from bokeh.plotting import figure, output_file, show

if __name__ == "__main__":
    output_file('graficado_simple.html')
    fig = figure()

    total_vals = int(input('Ingresa cuantos valores quieres graficar:'))
    x_vals = list(range(total_vals))
    y_vals = []

    for x in x_vals:
        val = int(input(f'Escribe el valor para {x} : '))
        y_vals.append(val)
    
    fig.line(x_vals, y_vals, line_width = 2)
    show(fig)