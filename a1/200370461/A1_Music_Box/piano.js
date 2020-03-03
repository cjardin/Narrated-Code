// Assignment 1 - Javascript Music Box
// Name: Ezer Patlan
// Spring CS351
// CS: Programming Language
// Instructor: Cary Jardin

// eraseText function allows you to clear the text!
function eraseText() {
	// Deletes the text in the textarea
	document.getElementById("input_notes").value = "";
	// refresh the browser page
	location.reload();
}


// runPiano Function will run the main program
function runPiano() {
	// input the individual note into a json object and uploaded to the
	// VF.StaveNote function in order to print the music note notation

	// json2obj function can convert the three array list, alphabet, repeats, and speed sound
	// into a object
	function json2obj(notes_list, repeat_list, timeout_list){
		var i = 1;
		// verifying wheter there is no duplicate
		if (i == repeat_list) {
			// appending into a new array
			notes_parsed.push(notes_list)
			notes_time.push(timeout_list)
			// generating the syntax string in order to converted into a json
			var json1 = '{"keys": ["';
			var json2 = notes_list + '/4"], "duration": "q"}';
			var json3 = json1.concat(json2)
			// parse the json into a object
			const obj = JSON.parse(json3);
			// create a note using Vexflow
			var note = new VF.StaveNote(obj);
			// append the final result
			notes.push(note);
			return notes;
		} else {
				// generate the duplicate audio
				while( i <= repeat_list)
				{
				// append the input into a new array
				notes_parsed.push(notes_list)
				notes_time.push(timeout_list)
				// generating the syntax string in oreder to converted into a json
				var json1 = '{"keys": ["';
				var json2 = notes_list + '/4"], "duration": "q"}';
				var json3 = json1.concat(json2)
				// parse the json into a object
				const obj = JSON.parse(json3);
				// create a note using Vexflow
				var note = new VF.StaveNote(obj);
				
				// append the input
				notes.push(note);
				i = i + 1;
				
			}
			// return the final result
			return notes;
		}
		
	}

	// getUnique function will eliminate any duplicate in the array
	function getUnique(array) {
		var uniqueArray = [];
		// Loop through array values
		for (i = 0; i < array.length; i++) {
			// check wheter there is no duplicate
			if (uniqueArray.indexOf(array[i]) === -1) {
				// append into the array
				uniqueArray.push(array[i]);
			}
		}
		// return the result
		return uniqueArray;

	}
	// try and catch used for Error Handling
	try {

	var complete_note_list = ["A", "B", "C", "D", "E", "F", "G"];
	// delete the lines
	notes_raw = $("#input_notes").val().split(/\r?\n/);
	
	let onlyLetters = /[a-zA-Z]+/g
	let onlyNumeric = /[+-]?(\d+([.]\d*)?(e[+-]?\d+)?|[.]\d+(e[+-]?\d+)?)/g
	let onlyFloat = /[+-]?(\d+([.]\d*)?(e[+-]?\d+)?|[.]\d+(e[+-]?\d+)?)/g
	// generate an array only show the repetition
	notes_repeat = $("#input_notes").val().match(onlyNumeric).map(s => s.slice(0, 1));
	// generate an array only show the speed
	notes_timeout = ($("#input_notes").val().match(onlyFloat)).map(s => s.slice(1, 4));
	

	//////////////////////////////
	//     Error Handling      //
	/////////////////////////////
	var max_repeat_numb_notes = 9;
	// Error try and catch
	// It constrains the user to use only one note per line.

	// This for loop clean the white spaces and appends into new string array
	// empty array
	new_notes_raw = [];
	notes_letter = [];
	// for loop go through alphabet notes input
	for (m = 0; m < notes_raw.length; m++) {
		// trim every row that does have any white space
		number_rows = notes_raw[m].trim();
		if (Boolean(number_rows)) {
			// store the letter into a variable
			letter = number_rows.match(onlyLetters)[0];
			// append the letter,duplicate, and speed
			new_notes_raw.push(number_rows);
			// append the letter
			notes_letter.push(letter)
		}
	}
	
	
	// Sorting and Unique the Alphabet Notes
	sort_letters = notes_letter.sort();
	sort_uniq_letters = getUnique(sort_letters);
	

	// Debuginnin to see what is going on in the code
	/*console.log(new_notes_raw);
	console.log(notes_letter);
	console.log(sort_uniq_letters);
	console.log(complete_note_list);
	console.log(notes_repeat);
	console.log(notes_timeout);
	*/
	

	// Check the number of row per each line 
	// if there is more than one note will stop the code
	for (m = 0; m < new_notes_raw.length; m++) {
		// split the space of the input value note
		number_rows = new_notes_raw[m].split(" ").length;
		
		//console.log(number_rows)
		// if there are two or more inputs in one row
		if (number_rows > 1) {
			// Give error to the user
			throw "Please add one note per line!";
		} 

	}
	// Use the filter command to determine the difference and it is not in the notes of the alphabet
	let difference = sort_uniq_letters.filter(element => !complete_note_list.includes(element));
	//console.log(difference);
	// if there more than one in the difference array that means the user has alphabet that does not 
	// follow the alphabet notes
	if (difference.length > 0 ) {
		throw "Please use first seven letters of the alphabet!"
	}
	// Use only 1-9 repetitions
	// If statement will constraint the user and allow to use only certain number of repetitions
	if (max_repeat_numb_notes > 10){
		throw "Please use no more than 9 duplicates!"
	}

	
	
    /////////////////////
	// Reference Notes //
	/////////////////////

	// It will print the symbol note notation for the user to help follow the audio

	VF1 = Vex.Flow;
	
	// Create an SVG renderer and attach it tot he DIV element named "reference notes"
	var div1 = document.getElementById("reference_notes")

	var renderer = new VF1.Renderer(div1, VF1.Renderer.Backends.SVG);

	px1=500;
	// Size SVG
	renderer.resize(px1+100, px1/4);
	// and get a drawing context
	var context1 = renderer.getContext();
	
	context1.setFont("Times", 10, "").setBackgroundFillStyle("#eed");

	var stave1 = new VF1.Stave(10, 0, px1);

	stave1.addClef("treble");
	// Connect it to the rendering context and draw!
	stave1.setContext(context1).draw();
	// Generate your input notes
	var notes_ref = [
		new VF1.StaveNote({ keys: ["a/4"], duration: "q" }),
		new VF1.StaveNote({ keys: ["b/4"], duration: "q" }),
		new VF1.StaveNote({ keys: ["c/4"], duration: "q" }),
		new VF1.StaveNote({ keys: ["d/4"], duration: "q" }),
		new VF1.StaveNote({ keys: ["e/4"], duration: "q" }),
		new VF1.StaveNote({ keys: ["f/4"], duration: "q" }),
		new VF1.StaveNote({ keys: ["g/4"], duration: "q" })
	];	

	// Create a voice in 4/4 and add above notes
	var voice_ref = new VF1.Voice({ num_beats: 7, beat_value: 4 });
	voice_ref.addTickables(notes_ref);

	// Format and justify the notes to 400 pixels.
	var formatter1 = new VF1.Formatter().joinVoices([voice_ref]).format([voice_ref], px1);

	// Render voice
	voice_ref.draw(context1, stave1);
	

	/////////////////////
	// Real-Time Notes //
	/////////////////////

	VF = Vex.Flow;

	// Create an SVG renderer and attach it to the DIV element named "play piano".
	var div = document.getElementById("play_piano")
	var renderer = new VF.Renderer(div, VF.Renderer.Backends.SVG);

	//px = notes_letter.length * 500;
	px=1000;
	// Configure the rendering context.

	renderer.resize(px+100, px/5);
	var context = renderer.getContext();
	
	context.setFont("Arial", 10, "").setBackgroundFillStyle("#eed");
	// 13 notes = 500 px
	// Create a stave of width 400 at position 10, 40 on the canvas.
	
	var stave = new VF.Stave(10, 0, px);
	
	// Add a clef and time signature.
	
	stave.addClef("treble");
	// Connect it to the rendering context and draw!
	stave.setContext(context).draw();
	
	// empty array
	var notes_parsed = []
	var notes_time = []
	var notes=[];
	
	
	// for loop will convert the array into json to object
	for (index = 0; index < notes_raw.length; index++) {
			for (n = 0; n < notes_raw.length; n++) {
				for (i = 0; i < complete_note_list.length; i++){
					// compare if the notes are identical
					if (notes_raw[index][n] == complete_note_list[i]) {
						// call the json to object function
						notes = json2obj(notes_raw[index][n], notes_repeat[index],notes_timeout[index]);

					}
				}
				
			}
	}


	
	console.log(notes)
	
	// for loop determine whether the following notes belong to the 
	// correct audio
	timing = 0
	//index_ms_offset = 3000
	// Adding a weight to speed or slow down the audio note
	weight=30000;
	for (index = 0; index < notes_parsed.length; index++) {
		if (notes_parsed[index] == 'A') {
			// Time delay
			setTimeout( function() {
			// Play Audio	
				new Audio('media/high_a.mp3').play()
			}, weight*notes_time[index] * index)
		} else if (notes_parsed[index] == 'B' ) {	
			// Time delay
			setTimeout(function() {
			// Play Audio	
				new Audio('media/high_b.mp3').play()
			}, weight*notes_time[index] * index )
		} else if (notes_parsed[index] == 'C' ) {
			// Time delay		
			setTimeout(function() {	
			// Play Audio	
				new Audio('media/high_c.mp3').play()
			}, weight*notes_time[index] * index )
		} else if (notes_parsed[index] == 'D' ) {
			// Time delay	
			setTimeout(function() {
			// PLay Audio	
				new Audio('media/high_d.mp3').play()
			}, weight*notes_time[index] * index ) 
		} else if (notes_parsed[index] == 'E' ) {
			
			// Time Audio
			setTimeout(function() {
			// Play Audio
				new Audio('media/high_e.mp3').play()
			}, weight*notes_time[index] * index )
		} else if (notes_parsed[index] == 'F') {
			
			// Time Audio
			setTimeout(function() {
			// Play Audio
				new Audio('media/high_f.mp3').play()
			}, weight*notes_time[index] * index )
		} else if (notes_parsed[index] == 'G') {
			
			// Time Audio
			setTimeout(function() {
			// Play Audio	
				new Audio('media/high_g.mp3').play()
			}, weight*notes_time[index] * index )

		}
	}
	
	//alert(notes_parsed)
	console.log(notes);



// Create a voice in 4/4 and add above notes
var voice = new VF.Voice({num_beats: notes_parsed.length, beat_value: 4});
voice.addTickables(notes);

// Format and justify the notes to 400 pixels.
var formatter = new VF.Formatter().joinVoices([voice]).format([voice], px);

// Render voice
voice.draw(context, stave);


	// Javascript Buttons -> HTML5
	var clearBtn = document.getElementById('ClearNote');
	clearBtn.addEventListener('click', e => {
		
		const staff1 = document.getElementById('reference_notes')
		while (staff1.hasChildNodes()) {
			staff1.removeChild(staff1.lastChild);
		}

		const staff2 = document.getElementById('play_piano')
		while (staff2.hasChildNodes()) {
			staff2.removeChild(staff2.lastChild);
		}

	})
	// Generate the concatenate code for stand-alone html5
		var htmlTEMPLATE="<!doctype html>"
		htmlTEMPLATE=htmlTEMPLATE+"<html>\n<head><\/head>\n<body>\n"
		htmlTEMPLATE=htmlTEMPLATE+"<script>@@@PLAY_CODE<\/script>"
		htmlTEMPLATE = htmlTEMPLATE+"<\/body>\n<\/html>\n"


		// for loop and if statement
		// generating the code for each note and audio note
		code_output = "\n"
		timing = 0
		//index_ms_offset = 1000
		weight = 30000;
		for (index = 0; index < notes_parsed.length; index++) {
			if (notes_parsed[index] == 'A') {
				code_output = code_output + "setTimeout( function(){\n"
				code_output = code_output + "new Audio('media/high_a.mp3').play()"
				code_output = code_output + "}, " + weight + " * " + notes_time[index] + " * " + index + ");\n "
			} else if (notes_parsed[index] == 'B') {
				code_output = code_output + "setTimeout( function(){\n"
				code_output = code_output + "new Audio('media/high_b.mp3').play()"
				code_output = code_output + "}, " + weight + " * " + notes_time[index] + " * " + index + ");\n "
			} else if (notes_parsed[index] == 'C') {
				code_output = code_output + "setTimeout( function(){\n"
				code_output = code_output + "new Audio('media/high_c.mp3').play()"
				code_output = code_output + "}, " + weight + " * " + notes_time[index] + " * " + index + ");\n "
			} else if (notes_parsed[index] == 'D') {
				code_output = code_output + "setTimeout( function(){\n"
				code_output = code_output + "new Audio('media/high_d.mp3').play()"
				code_output = code_output + "}, " + weight + " * " + notes_time[index] + " * " + index + ");\n "
			} else if (notes_parsed[index] == 'E') {
				code_output = code_output + "setTimeout( function(){\n"
				code_output = code_output + "new Audio('media/high_e.mp3').play()"
				code_output = code_output + "}, " + weight + " * " + notes_time[index] + " * " + index + ");\n "
			} else if (notes_parsed[index] == 'F') {
				code_output = code_output + "setTimeout( function(){\n"
				code_output = code_output + "new Audio('media/high_f.mp3').play()"
				code_output = code_output + "}, " + weight + " * " + notes_time[index] + " * " + index + ");\n "
			} else if (notes_parsed[index] == 'G') {
				code_output = code_output + "setTimeout( function(){\n"
				code_output = code_output + "new Audio('media/high_g.mp3').play()"
				code_output = code_output + "}, " + weight + " * " + notes_time[index] + " * " + index + ");\n "
			}
		}

	// print the code
	$("#compiled_code").val(htmlTEMPLATE.replace("@@@PLAY_CODE", code_output))
	} catch(err) {
		alert("Error: " + err);
		
		
	}
	
}
