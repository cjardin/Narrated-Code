// Matthew Flavin
// 5/8/20
// CS 351 - Programming Languages
// Assignment 3 - Player Piano Assignment

// getNotes()
// This Function returns an array of file names to play in order
function getNotes() {

    var known_notes = [];
    var notes_to_play = [];
    var regex_has_equals = /[=]/;
    var regex_before_equals = /[^=]*/;
    var regex_after_equals = /[^=]*$/;
    var music_files = ["C_sharp_hi.mp3", "C_sharp_lo.mp3", "D_sharp_hi.mp3", "D_sharp_lo.mp3","E_hi.mp3", "E_lo.mp3", "F_sharp.mp3", "G.mp3", "Z.mp3"];

    // https://stackoverflow.com/a/9196996
    // Parse text area
    var lines = $('#notes').val().split('\n');

    // Parse text area
    for(var i = 0; i < lines.length; i++)
    {
        // https://stackoverflow.com/a/5963202
        // Clear white space
        let current_line = lines[i].replace(/\s+/g, '');

        // If current line contains equals sign
        if(regex_has_equals.test(current_line))
        {
            // Get before and after equal sign
            let prefix = regex_before_equals.exec(current_line)[0];
            let suffix = regex_after_equals.exec(current_line)[0];
            let match = false;
            let found = false;

            // Check to see if file assignment is one of files available
            for(var h = 0; h < music_files.length; h++)
            {
                if(suffix == music_files[h])
                {
                    match = true;
                }
            }

            // If not a valid file, output error and return empty array
            if (match == false)
            {
                $("#HTMLoutput").val("File: " + suffix + " is not valid! Please check your spelling and syntax.");
                notes_to_play = [];
                return notes_to_play;
            }

            // Check to see if the given assigned note already exists
            for(var j = 0; j < known_notes.length; j++)
            {

                // If exists, update it with new assignment
                if(prefix == known_notes[j].note)
                {
                    known_notes[j].file = suffix;
                    console.log("Updating Note: " + known_notes[j].note + " with file: " + suffix);
                    found = true;
                    break;
                }
            }

            // If it does not exist, add it to array of known notes
            if(found == false)
            {
                let new_note = {note:prefix, file:suffix};
                console.log("New Note: " + prefix + " New File: " + suffix);
                known_notes.push(new_note);
            }

            // Reset conditional flags
            match = false;
            found = false;
        }

        // No equals sign, find the respective file for the note and add it to the queue
        else
        {
            for(var j = 0; j < known_notes.length; j++)
            {
                if(current_line == known_notes[j].note)
                {
                    console.log("Queueing file: " + known_notes[j].file + " from note: " + known_notes[j].note);
                    notes_to_play.push(known_notes[j].file);
                    break;
                }
            }
        }
    }

    // Return queue
    return notes_to_play;
}


// playMusic()
// plays the notes from text area, parsed by getNotes()
function playMusic()
{
    let noteArray = getNotes();
    let beat_interval = 1500;
    printHTML(noteArray);

    for (i = 0; i < noteArray.length; i++)
    {
        console.log("Playing: " + noteArray[i]);
        let note = new Audio(noteArray[i]);
        setTimeout( function(){
            note.play();
        }, i * beat_interval);
    } 
}

// prints out code to paste into an HTML file to play the music
function printHTML(note_list)
{
    let output = `
    <!DOCTYPE html>
    <html>
        <body>
            <script src="https://code.jquery.com/jquery-3.4.1.js" integrity="sha256-WpOohJOqMqqyKL9FccASB9O0KwACQJpFTUBLTYOVvVU=" crossorigin="anonymous"></script>
            <script>
            function playMusic()
            {
    `;

    for(i = 0; i < note_list.length; i++)
    {
        note = note_list[i];
        output += "\n \t \tlet note = new Audio(\"" + note_list[i] + "\");";
        output += "\n \t \tsetTimeout( function(){ \n";
        output += "\t \t \tnote.play();\n";
        output += "\t \t}, ";
        output += i.toString();
        output += " * 1500);\n"
    }

    output += `
            }
            </script>

        <button type="button" onclick="playMusic()">
            Play!
        </button>
        </body>
    </html>
    `

    // Place generated code into text area HTMLoutput
    if(note_list.length > 0)
    {
        $("#HTMLoutput").val(output);
    }
}

// on button click, play music and generate code
function buttonClick()
{
    playMusic();
    printHTML();
}