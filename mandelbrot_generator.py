import numpy
import time

##from numba import autojit
import matplotlib.pyplot as plt

def mandelbrot(Re, Im, max_iter):
    c = complex(Re, Im)
    z = 0.0j

    for i in range(max_iter):
        z = z * z + c
        if(z.real*z.real + z.imag*z.imag) >=4:
            return i
    return max_iter

#resolution of the image
columns = 200
rows = 200
start = time.time()
result = numpy.zeros([rows, columns])
for row_index, Re in enumerate(numpy.linspace(-2,1, num=rows)):
    for column_index, Im in enumerate(numpy.linspace(-1,1, num=columns)):
        result[row_index, column_index]= mandelbrot(Re, Im, 100)

plt.figure(dpi=100)
#https://matplotlib.org/3.1.1/gallery/color/colormap_reference.html
plt.imshow(result.T, cmap='afmhot', interpolation='bilinear' ,extent=[-2,1,-1,1])
plt.xlabel('Re')
plt.ylabel('Im')
end = time.time()
print(end - start)
plt.savefig("mandelbrot.png")

plt.show()
