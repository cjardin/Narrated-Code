// Matthew Flavin
// 2/19/20
// CS 351 - Programming Languages
// Assignment 1 - Player Piano
// This is my first time using JavaScript! It doesn't look as pretty as I would of liked it, but I felt I learned a lot making it!


// this will parse the notes from the text area #notes and return them in an array
function getNotes() {

    var notes_raw = $("#notes").val().split('/n');
    var parsedNotes = [];
    var tmp;

    for (row = 0; row < notes_raw.length; row++)
    {
        for(col = 0; col < notes_raw[row].length; col++)
        {
            tmp = notes_raw[row][col];

            if(tmp == "A" || tmp == "B" || tmp == "C" || tmp == "D" || tmp == "E"  || tmp == "F"  || tmp == "G"  || tmp == "H" || tmp == "Z")
            {
                parsedNotes.push(notes_raw[row][col]);
            }
        }
    }

    return parsedNotes;
}

// iterate through the array and play the appropiate .mp3 for each index
function playMusic()
{

    let noteArray = getNotes();
    let note, first;

    for (i = 0; i < noteArray.length; i++)
    {

        note = noteArray[i];
        ended = false;
        
        let beat_interval = 1500;

        switch(note)
        {
            case "A":
                setTimeout( function(){
                    new Audio("E_hi.mp3").play();
                }, i * beat_interval);
                break;

            case "B":
                setTimeout( function(){
                    new Audio("E_lo.mp3").play();
                }, i * beat_interval);
                break;  

            case "C":
                setTimeout( function(){
                    new Audio("D_sharp_hi.mp3").play();
                }, i * beat_interval);
                break;

            case "D":
                setTimeout( function(){
                    new Audio("D_sharp_lo.mp3").play();
                }, i * beat_interval);
                break; 

            case "E":
                setTimeout( function(){
                    new Audio("C_sharp_hi.mp3").play();
                }, i * beat_interval);
                break;

            case "F":
                setTimeout( function(){
                    new Audio("C_sharp_lo.mp3").play();
                }, i * beat_interval);
                break; 

            case "G":
                setTimeout( function(){
                    new Audio("G.mp3").play();
                }, i * beat_interval);
                break;

            case "H":
                setTimeout( function(){
                    new Audio("F_sharp.mp3").play();
                }, i * beat_interval);
                break;    
            case "Z":
                setTimeout( function(){
                    new Audio("Z.mp3").play();
                }, (i * beat_interval) - 300);
                break;       
        }
    }
}

// prints out code to paste into an HTML file to play the music
function printHTML()
{
    let noteArray = getNotes();
    let output = `
    <!DOCTYPE html>
    <html>
        <body>
            <script src="https://code.jquery.com/jquery-3.4.1.js" integrity="sha256-WpOohJOqMqqyKL9FccASB9O0KwACQJpFTUBLTYOVvVU=" crossorigin="anonymous"></script>
            <script>
            function playMusic()
            {
    `;

    for(i = 0; i < noteArray.length; i++)
    {
        note = noteArray[i];
        switch(note)
        {
            case "A":
                output += "\n \t \tsetTimeout( function(){ \n";
                output += "\t \t \tnew Audio(\"E_hi.mp3\").play();\n"
                output += "\t \t}, ";
                output += i.toString();
                output += " * 1500);\n"
                break;

            case "B":
                output += "\n \t \tsetTimeout( function(){ \n";
                output += "\t \t \tnew Audio(\"E_lo.mp3\").play();\n"
                output += "\t \t}, ";
                output += i.toString();
                output += " * 1500);\n"
                break;

            case "C":
                output += "\n \t \tsetTimeout( function(){ \n";
                output += "\t \t \tnew Audio(\"D_sharp_hi.mp3\").play();\n"
                output += "\t \t}, ";
                output += i.toString();
                output += " * 1500);\n"
                break;

            case "D":
                output += "\n \t \tsetTimeout( function(){ \n";
                output += "\t \t \tnew Audio(\"D_sharp_lo.mp3\").play();\n"
                output += "\t \t}, ";
                output += i.toString();
                output += " * 1500);\n"
                break;

            case "E":
                output += "\n \t \tsetTimeout( function(){ \n";
                output += "\t \t \tnew Audio(\"C_sharp_hi.mp3\").play();\n"
                output += "\t \t}, ";
                output += i.toString();
                output += " * 1500);\n"
                break;

            case "F":
                output += "\n \t \tsetTimeout( function(){ \n";
                output += "\t \t \tnew Audio(\"C_sharp_lo.mp3\").play();\n"
                output += "\t \t}, ";
                output += i.toString();
                output += " * 1500);\n"
                break;

            case "G":
                output += "\n \t \tsetTimeout( function(){ \n";
                output += "\t \t \tnew Audio(\"G.mp3\").play();\n"
                output += "\t \t}, ";
                output += i.toString();
                output += " * 1500);\n"
                break;

            case "H":
                output += "\n \t \tsetTimeout( function(){ \n";
                output += "\t \t \tnew Audio(\"F_sharp.mp3\").play();\n"
                output += "\t \t}, ";
                output += i.toString();
                output += " * 1500);\n"
                break;

            case "Z":
                output += "\n \t \tsetTimeout( function(){ \n";
                output += "\t \t \tnew Audio(\"Z.mp3\").play();\n"
                output += "\t \t}, (";
                output += i.toString();
                output += " * 1500) - 300);"
                break;
        }
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
    $("#HTMLoutput").val(output);

}

// on button click, play music and generate code
function buttonClick()
{
    playMusic();
    printHTML();
}