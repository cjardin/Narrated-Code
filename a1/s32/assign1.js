var interval;
done = false;
function load(string) {
  var letter = document.getElementById(string);
  interval = setInterval(start, 15);

  var dir = 1;
  var pos = letter.offsetLeft;
  var screenWidth = $(window).width();
  function start() {
  	letter.style.fontWeight = "bold";
    if (pos > screenWidth) letter.parentNode.removeChild(letter);
    else if (pos < 0) dir = 1;
    pos += dir;
    letter.style.left = pos + 'px';
  }

}

if(done === true){
  	window.clearInterval(interval);
}	

function rewriteMessage(string, address){
	var para = document.getElementById(address);
	para.textContent = string;
	if(string == "A"){
		para.style.color = "red";
	}else if(string == "B"){
		para.style.color = "blue";
	}else if(string == "C"){
		para.style.color = "green";
	}else if(string == "D"){
		para.style.color = "orange";
	}
	load(address);
}


function addSounds(){

	notesRaw = $("#notes").val().split(/\r?\n/);
	var notes_parsed = [];
	var count = 0;
	for(index = 0; index < notesRaw.length;index++){
		if(notesRaw[index][count] == 'A'){
			notes_parsed.push(['A',"C_64kb.mp3"]);
			count++;
		}
		if(notesRaw[index][count] == 'B'){
			notes_parsed.push(['B',"D_64kb.mp3"]);
			count++;
		}
		if(notesRaw[index][count] == 'C'){
			notes_parsed.push(['C',"Dm_64kb.mp3"]);
			count++;
		}
		if(notesRaw[index][count] == 'D'){
			notes_parsed.push(['D',"E_64kb.mp3"]);
			count++;
		}
	
	}
	return notes_parsed;
}

function playSound(){
	let notes_array = addSounds();
	var index_ms_offset = 1000;
	var count = 1;
	var textInArea = document.getElementById("notes");
	
	for(var index = 0; index < notes_array.length; index++){
		let address = "messageNote";
		let playMusic = notes_array[index][1];
		if(notes_array[index][0] == 'A'){
			setTimeout( function(){
					new Audio(playMusic).play();
					rewriteMessage("A",address);
			}, index_ms_offset * count);
		}else if(notes_array[index][0] == 'B'){
			setTimeout( function(){
					new Audio(playMusic).play();
					rewriteMessage("B",address);
			}, index_ms_offset * count);
		}else if(notes_array[index][0] == 'C'){
			setTimeout( function(){
					new Audio(playMusic).play();
					rewriteMessage("C",address);
			}, index_ms_offset * count);
		}else if(notes_array[index][0] == 'D'){
			setTimeout( function(){
					new Audio(playMusic).play();
					rewriteMessage("D",address);
			}, index_ms_offset * count);
		}
		count += 1.4;
	}
}

function printHTML(){
	let notes_array = addSounds();
	let output = `
    <!DOCTYPE html>
	<html>
		<head> 

		<script src="https://code.jquery.com/jquery-3.4.1.js"
		 integrity="sha256-WpOohJOqMqqyKL9FccASB9O0KwACQJpFTUBLTYOVvVU=" crossorigin="anonymous">
		</script>
		<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
		<script>
		function playSound(){
    `;

    for(var i = 0; i < notes_array.length; i++){
    	var notes = notes_array[i];
    	if(notes[0] == "A"){
    		output += "\n \t \tsetTimeout( function(){ \n";
            output += "\t \t \tnew Audio(" + notes[1] + ").play();\n"
            output += "\t \t}, ";
            output += (i + 1.4).toString();
            output += " * 1000);\n" 
    	}
    	else if(notes[0] == "B"){
    		output += "\n \t \tsetTimeout( function(){ \n";
            output += "\t \t \tnew Audio(" + notes[1] + ").play();\n"
            output += "\t \t}, ";
            output += (i + 1.4).toString();
            output += " * 1000);\n" 
    	}
    	else if(notes[0] == "C"){
    		output += "\n \t \tsetTimeout( function(){ \n";
            output += "\t \t \tnew Audio(" + notes[1] + ").play();\n"
            output += "\t \t}, ";
            output += (i + 1.4).toString();
            output += " * 1000);\n" 
    	}
    	else if(notes[0] == "D"){
    		output += "\n \t \tsetTimeout( function(){ \n";
            output += "\t \t \tnew Audio(" + notes[1] + ").play();\n"
            output += "\t \t}, ";
            output += (i + 1.4).toString();
            output += " * 1000);\n" 
    	}
    }

    output += `
    	}
    	</script>
    <input id = "button1" type="button" value="Play Sound" onclick = "playSound()"> </input>

	</body>
	</html>
    `
    $("#HTMLoutput").val(output);
}

