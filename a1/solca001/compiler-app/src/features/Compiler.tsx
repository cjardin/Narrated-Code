import React, { Dispatch, SetStateAction, useState } from 'react';
import { Button, Grid, TextField } from "@material-ui/core";
import { ISound, ISoundSetter } from "../App";
import { BeatParser } from "./BeatParser";

export interface Props {
  beatTempo: number,
  beatText: string,
  compilerArr: (ISound | ISoundSetter)[],
  setCompilerArr: Dispatch<SetStateAction<(ISound | ISoundSetter)[]>>,
}



function compileBeatParser({ beatTempo, beatText, compilerArr, setCompilerArr }: Props): string {
  let tempo = 0;
  BeatParser({ beatText, compilerArr, setCompilerArr });
  let output = String("<!doctype html>" +
    "<html lang=\"en\">\n" +
    "<head><title>Hello Compiled Word</title></head><body>\n" +
    "<script>\n\n");
  compilerArr.reverse();
  compilerArr.forEach(e => {
    if (e && e.kind === "ISound") {
      // setTimeout( function(){new Audio('zapsplat_cartoon_rise_upwards_futuristic_002_44571.mp3').play()
      output += `\tsetTimeout( function(){new Audio("${e.soundFileName}").play()}, ${tempo});\n`;
      tempo += beatTempo;
    } else if (e && e.kind === "ISoundSetter") {
      // output += "ISoundSetter" + e.varName + " et " + e.fileName + "\n";
    }
  });

  output += "\n</script>\n" +
    "</body>\n" +
    "</html>\n";
  setCompilerArr([]);
  return output;
}


function CompilerC({ beatTempo, beatText, compilerArr, setCompilerArr }: Props) {
  const [output, setOutput] = useState("");
  return (
    <React.Fragment>
      <Grid item xs={12}>
        <Button variant="contained" onClick={() => setOutput(compileBeatParser({beatTempo, beatText, compilerArr, setCompilerArr}))}>Gen</Button>
      </Grid>
      <Grid item xs={12}>
        <TextField multiline fullWidth defaultValue={output} />
      </Grid>
    </React.Fragment>
  );
}

export const MyCompiler = CompilerC;
