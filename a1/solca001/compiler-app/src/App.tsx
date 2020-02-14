import React, { useState } from 'react';
import './App.css';
import { Grid, TextField } from "@material-ui/core";
import { Alert } from '@material-ui/lab';
import { MyCompiler } from "./features/Compiler";

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

function App() {
  const [compilerArr, setCompilerArr] = useState<(ISound | ISoundSetter)[]>([]);
  const [beatTempo, setBeatTempo] = useState(600);
  const [beatText, setBeatText] = useState("A=p.mp3\n" +
    "B=tss.mp3\n" +
    "C=pff.mp3\n" +
    "D=tss.mp3\n" +
    "A\n\tB\n\t\tC\n\t\t\tD\n" +
    "A=ech.mp3\nA\nA=p.mp3\nA\n\t\t\tD");

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
        <TextField multiline fullWidth defaultValue={beatText} onChange={e => setBeatText(e.target.value)}/>
      </Grid>
      <MyCompiler beatTempo={beatTempo} beatText={beatText} compilerArr={compilerArr} setCompilerArr={setCompilerArr}/>
    </Grid>
  );
}

export default App;
