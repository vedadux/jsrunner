# JSRunner

This is a simple selenium based utility for running javascript code from the 
command line. In contrast to running javascript via v8, the environment is an
actual browser and therefore also has all of its features. To run the code in a
CLI interface, the browser is started in headless mode. Any communication with
the command line is done through the `log()` function. The output relies on the
presence of DOM elements, so any code that logs output must be placed in a 
function called `main()` to ensure that the DOM is completely loaded.

The program is terminated once the `exit()` function is called. All the output
produced thorugh the `log()` function is shown in real time in the console.

# Usage

`python3 jsrunner.py <script>...`

JSRunner accepts multiple javascript files at once. The files are added to a 
template html file and executed by the browser. The files have to be in the 
correct order if functions from one file are used in the others.

# How it works

JSRunner works through selenium which can be used to controll a web browser.
Currently, only Firefox is available through the geckodriver, and using other
browsers requires very minor modifications. Selenium is accessed through its
python API. The html file that contains the javascript is automatically 
generated at runtime and is destroyed as soon as the program finishes.
