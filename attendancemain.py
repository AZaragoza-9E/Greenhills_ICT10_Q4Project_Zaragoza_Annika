from pyscript import display, document
import numpy as np
import matplotlib.pyplot as plt
import logging


logging.getLogger('matplotlib').setLevel(logging.ERROR)

plt.figure()
plt.plot([0, 1], [0, 1])
plt.close()

thedays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
absences = [0, 0, 0, 0, 0]

def show(e):
    document.getElementById("result").innerHTML = ""
    theday = document.getElementById('weeks').value
    num = int(document.getElementById('absences').value)

    index = thedays.index(theday)
    absences[index] = num


    plt.figure()
    plt.plot(thedays, absences)

    plt.title("The Attendance Tracker")
    plt.xlabel("Days")
    plt.ylabel("No. of Absences")
    plt.grid('true')

    display(plt, target="result")