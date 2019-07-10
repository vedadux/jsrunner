function main()
{
  const NUM_OUT = 10
  for(var i = 0; i < NUM_OUT; i++)
    setTimeout(function(){ log("Hello", "World"); }, i * 100);
  setTimeout(function(){exit()}, NUM_OUT * 100);
}
