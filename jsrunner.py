from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import sys
import os
import socket

# the program expects at least one script file
def usage():
  if len(sys.argv) < 2:
    print("usage: %s <script0>..." % sys.argv[0])
    sys.exit(-1)


# all the scripts need to be accessible
# returns the absolute script paths
def get_scripts():
  scripts = sys.argv[1:]
  for s in scripts:
    if not os.path.isfile(s):
      print("Could not read file %s" % s)
      sys.exit(-2)
  scripts = [os.path.realpath(s) for s in scripts]
  return scripts


# initialises a gecko driver
def init_driver():
  options = Options()
  profile = FirefoxProfile()
  # set some custom profile preferences here
  options.add_argument('-headless')
  driver = Firefox(executable_path='geckodriver', 
                   firefox_profile=profile, options=options)
  return driver


# build the temporary html file
def build_html(scripts):
  assert(os.path.isfile("jsrunner.html"))
  html = ""
  with open("jsrunner.html", "r") as h:
    html = h.read()
  html = html.replace("jsrunner.js", os.path.realpath("jsrunner.js"))
  stxt = "\n".join(["<script src=\"" + s + "\"></script>" for s in scripts])
  html = html.replace("<p hidden>SCRIPTS</p>", stxt)
  filename = "/tmp/jsrunner-" + str(os.getpid()) + ".html"
  with open(filename, "w") as f:
    f.write(html)
  return os.path.realpath(filename)


# get program output
def get_output(driver):
  line = 0
  while True:
    try:
      wait = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "x" + str(line) + "x")))
      title = driver.execute_script("return arguments[0].title;", wait)
      if title == "done": break
      output = driver.execute_script("return arguments[0].innerText;", wait)
      sys.stdout.write(output)
      line += 1
    except:
      print("Timeout while waiting for output")
      break
  pass


if __name__ == "__main__":
  usage()
  scripts = get_scripts()
  driver = init_driver()
  wait = WebDriverWait(driver, timeout=10)
  filename = build_html(scripts)
  driver.get("file://" + filename)
  get_output(driver)
  driver.quit()
  os.remove(filename)
  sys.exit(0)
