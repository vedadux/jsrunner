// setup for the logging through a DOM element
__lines = 0;
function log(...x)
{
  s = "";
  for (var i = 0; i < x.length; i++) 
  {  
     s += String(x[i]);
     s += (i != x.length - 1) ? " " : "\n";
  }
  var pre = document.createElement("pre"); 
  pre.id = "x" + String(__lines) + "x";
  __lines += 1;
  pre.innerText = s;
  document.getElementById("output").appendChild(pre);
  console.log(pre.innerText);
}

// setup for the exit function through a DOM element
function exit()
{
  var pre = document.createElement("pre");
  pre.id = "x" + String(__lines) + "x";
  pre.title = "done"
  document.getElementById("output").appendChild(pre);
}

