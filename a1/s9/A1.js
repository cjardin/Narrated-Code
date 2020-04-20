//
// Author: Daniel B. Martinez
// Email: marti931@cougars.csusm.edu
// Course: CS351
// Prof: C. Jardin
// Assignment 1: Music Box - A1.js
// Note!!!: This is my first time using javasctipt, html, and css

function getInfo()
{
   var raw = $("#input_notes").val().split(/\r?\n/);

   var parsed = [];
   var i = 0;

   while(i < raw.length)
   {    
     var j = 0;

     while(j < raw[i].length)
     {
       var temp;
      
       temp = raw[i][j];

       if(temp == 'A')	
	 parsed.push(raw[i][j]);

       else if(temp == 'B')
         parsed.push(raw[i][j]);

       else if(temp == 'C')
	 parsed.push(raw[i][j]);

       else if(temp == 'D')
	 parsed.push(raw[i][j]);

       j++;
      }

    i++;	
  }

  return parsed;
}

function playAudio()
{
  parsed = getInfo();
  var offset = 1000;
  var i = 0;

  while(i < parsed.length)
  {  
    if(parsed[i] == 'A')
    {
      setTimeout( function(){ new Audio('a_note.mp3').play() }, offset * i); 
    }
    
    else if(parsed[i] == 'B')
    {  
      setTimeout( function(){ new Audio('b_note.mp3').play() }, offset * i); 
    }
    
    else if(parsed[i] == 'C')
    {  
      setTimeout( function(){ new Audio('c_note.mp3').play() }, offset * i);
    }
   
    else if(parsed[i] == 'D')
    {    
      setTimeout( function(){ new Audio('d_note.mp3').play() }, offset * i);
    }
      
    i++;
  }

  // Create compile code
  var htmlTEMPLATE = "<!doctype html>"
  htmlTEMPLATE = htmlTEMPLATE + "<html><head><\/head ><body>"
  htmlTEMPLATE = htmlTEMPLATE + "<script>\n@@@PLAY_CODE <\/script>"
  htmlTEMPLATE = htmlTEMPLATE + "<\/body ><\/html>"

  code_output = " ";
  var offset = 1000;
  var i = 0;

  while(i < parsed.length)
  {
    if(parsed[i] == 'A')
    {
      code_output = code_output + "setTimeout( function(){"
      code_output = code_output + "new Audio('a_note.mp3').play()"
      code_output = code_output + "}, " + offset + " * " + i + "); ";
    }

    else if(parsed[i] == 'B')
    {
      code_output = code_output + "setTimeout( function(){"
      code_output = code_output + "new Audio('b_note.mp3').play()"
      code_output = code_output + "}, " + offset + " * " + i + "); ";
    }

    else if(parsed[i] == 'C')
    {
      code_output = code_output + "setTimeout( function(){"
      code_output = code_output + "new Audio('c_note.mp3').play()"
      code_output = code_output + "}, " + offset + " * " + i + "); ";
    }

    else if(parsed[i] == 'D')
    {
      code_output = code_output + "setTimeout( function(){"
      code_output = code_output + "new Audio('d_note.mp3').play()"
      code_output = code_output + "}, " + offset + " * " + i + "); ";
    }

    i++;
  }

  $("#compiled_code").val(htmlTEMPLATE.replace("@@@PLAY_CODE", code_output))
}
