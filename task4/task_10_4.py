import numpy as np
x = np.random.randint(1, 10, size = 7)
y = np.random.randint(1, 10, size = 7)
print ("Сторені масиви чисел:", x, y)
sum_xy = np.add(x, y)
sub_xy = np.subtract(x, y)
mult_xy = np.multiply(x, y)
div_xy = np.divide(x, y)
rem_xy = np.mod(x, y)
pow_xy = np.power(x, y)
np.set_printoptions(precision=3, suppress=True)
print("Арифметичні операції:\n"
    "Додавання масивів:", sum_xy, "\n"
    "Віднімання масивів:", sub_xy, "\n"
    "Множення масивів:", mult_xy, "\n"
    "Ділення масивів:", div_xy, "\n"
    "Остача від ділення:", rem_xy, "\n"
    "Елементи першого масиву у степені елементів другого:", pow_xy, "\n"
)
newarr = np.concatenate([x,y])
min_el = newarr.min()
max_el = newarr.max()
sum_el = np.sum([newarr])
mult_el = np.prod(newarr)
print("Новий масив:", newarr,
      "\nХарактеристики масиву:",
      "\nМаксимальний елемент:", max_el,
      "\nМінімальний елемент:", min_el,
      "\nСума елементів:", sum_el,
      "\nДобуток елементів:", mult_el
)