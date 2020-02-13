import React, { Dispatch, SetStateAction, useEffect, useState } from 'react';
import './App.css';
import { Button, Grid, TextField } from "@material-ui/core";
import { Alert } from '@material-ui/lab';
import { MyCompiler } from "./features/Compiler";
import { BeatParser } from "./features/BeatParser";

export interface ISound {
  kind: "ISound",
  name: string,
  soundFileName: string,
  sound: HTMLAudioElement,
}

export interface ISoundSetter {
  kind: "ISoundSetter",
  varName: string,
  fileName: string,
}

function playP(sounds: (ISound | ISoundSetter)[], soundName: string, duration: number) {
  sounds.forEach(elem => {
    if (elem.kind === "ISound" && elem.name === soundName) {
      setTimeout(() => elem.sound.play(), duration);
    }
  })
}

function playAll(sounds: (ISound | ISoundSetter)[], duration: number) {
  let _duration = 0;
  sounds.forEach(elem => {
    if (elem.kind === "ISound") {
      setTimeout(() => elem.sound.play(), _duration);
      _duration += duration;
    }
  })
}

function App() {
  const [compilerArr, setCompilerArr] = useState<(ISound | ISoundSetter)[]>([]);
  const [beatTempo, setBeatTempo] = useState(600);
  const [beatText, setBeatText] = useState("A=p.mp3\n" +
    "B=p.mp3\n" +
    "C=p.mp3\n" +
    "D=p.mp3\n" +
    "D\n\tB\n\t\tC\n\t\t\tD\n" +
    "A=pff.mp3\nA\nA=p.mp3\nA\n");
  const pSound = require("./assets/p.mp3");
  const pffSound = require("./assets/pff.mp3");
  const tssSound = require("./assets/tss.mp3");
  const echSound = require("./assets/ech.mp3");

  return (
    <Grid className="mainContainer" container spacing={3}>
      <Grid item xs={12}>
        <h1>My BeatBoxPlayer</h1>
        <Alert severity="success">
          Choose A, B, C or D for each unlimited lines and click "Play All". (Optional) Define a tempo.
        </Alert>
      </Grid>
      <Grid item xs={12}>
        <TextField id="tempo" placeholder="Default Tempo: 600" type="number" onChange={e => setBeatTempo(Number(e.target.value))}/>
      </Grid>
      <Grid item xs={12}>
        <Button variant="contained" onClick={() => playP(compilerArr, 'A', beatTempo)}>A = Play P</Button>
        <Button variant="contained" onClick={() => playP(compilerArr, 'B', beatTempo)}>B = Play TSS</Button>
        <Button variant="contained" onClick={() => playP(compilerArr, 'C', beatTempo)}>C = Play ECH</Button>
        <Button variant="contained" onClick={() => playP(compilerArr, 'D', beatTempo)}>D = Play PFF</Button>
      </Grid>
      <Grid item xs={12}>
        <TextField multiline fullWidth defaultValue={beatText} onChange={e => setBeatText(e.target.value)}/>
      </Grid>
      <Grid item xs={12}>
        <Button variant="contained" onClick={() => playAll(compilerArr, beatTempo)}>Play BeatBox</Button>
      </Grid>
      <MyCompiler beatTempo={beatTempo} beatText={beatText} compilerArr={compilerArr} setCompilerArr={setCompilerArr}/>
    </Grid>
  );
}

export default App;
