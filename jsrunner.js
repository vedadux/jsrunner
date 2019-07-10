// setup for the logging through a DOM element
function log(...x)
{
  s = "";
  for (var i = 0; i < x.length; i++) 
  {
    s += String(x[i]) + " ";
  }
  document.getElementById("output").innerText += s + "\n";
}

// setup for the exit function through a DOM element
function exit()
{
  document.getElementById("done").innerText = "Done!";
}


