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

function compileBeat({ beatTempo, beatText, compilerArr, setCompilerArr }: Props): string {
  let tempo = 0;
  BeatParser({ beatText, compilerArr, setCompilerArr });
  let output = String("<!DOCTYPE html>" +
    "<html lang=\"en\">\n" +
    "<head><title>Hello Compiled Word</title></head><body>\n" +
    "<script>\n\n");
  compilerArr.reverse();
  compilerArr.forEach(e => {
    if (e && e.kind === "ISound") {
      output += `\tsetTimeout(function(){new Audio("${e.soundFileName}").play()}, ${tempo});\n`;
      tempo += beatTempo;
    } else if (e && e.kind === "ISoundSetter") {
      // Todo if we have to declare variable later
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
        <Button variant="contained" onClick={() => setOutput(compileBeat({beatTempo, beatText, compilerArr, setCompilerArr}))}>Generate</Button>
      </Grid>
      <Grid item xs={12}>
        <TextField multiline fullWidth defaultValue={output} />
      </Grid>
    </React.Fragment>
  );
}

export const MyCompiler = CompilerC;
