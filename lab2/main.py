from sortings import *
import random
import time
import matplotlib.pyplot as plot
import matplotlib.animation as anim
import matplotlib
matplotlib.use('Tkagg')
plot.style.use('dark_background')

if __name__ == '__main__':

    playable = True
    while playable:

        size = int(input("Enter number of integers: "))
        method = input("Enter sorting method:"
                       "\n(q)uick"
                       "\n(m)erge"
                       "\n(h)eap"
                       "\n(b)ubble"
                       "\n(c)omb"
                       "\n")

        array = [x + 1 for x in range(size)]
        random.seed(time.time())
        random.shuffle(array)

        # set the generator for the plot
        if method == "b":
            title = "bubbleSort"
            generator = bubbleSort(array)
        elif method == "m":
            title = "mergeSort"
            generator = mergeSort(array, 0, size-1)
        elif method == "q":
            title = "quickSort"
            generator = quickSort(array, 0, size-1)
        elif method == "h":
            title = "heapSort"
            generator = heapSort(array)
        elif method == "c":
            title = "combSort"
            generator = combSort(array)
        else:
            print("Incorrect value, try again!")
            continue

        # initialize figure and axis.
        fig, ax = plot.subplots()
        ax.set_title(title)

        # initialize a bar plot.
        bar_rects = ax.bar(range(len(array)), array, align="edge")

        # set axis limits
        ax.set_xlim(0, size)
        ax.set_ylim(0, int(1.07 * size))

        text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

        iteration = [0]

        def updateFigure(array, rects, iteration):

            for rect, val in zip(rects, array):
                rect.set_height(val)
            iteration[0] += 1
            text.set_text("# of operations: {}".format(iteration[0]))


        animation = anim
        animation = anim.FuncAnimation(fig, func=updateFigure,
                                  fargs=(bar_rects, iteration), frames=generator, interval=1,
                                  repeat=False)

        plot.show()

# end of __main__
