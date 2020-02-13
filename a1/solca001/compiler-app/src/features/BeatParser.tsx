import React from 'react';
import { ISound, ISoundSetter } from "../App";
import { Dispatch, SetStateAction, useState } from "react";

type Props = {
  beatText: string,
  compilerArr: (ISound | ISoundSetter)[],
  setCompilerArr: Dispatch<SetStateAction<(ISound | ISoundSetter)[]>>,
}

function BeatParserC({ beatText, compilerArr, setCompilerArr }: Props) {
  function parsePlaySound(str: string) {
    if (/^[\t ]*[A-Z]$/g.test(str)) {
      const char = str.match(/[A-Z]$/g);
      if (char) {
        const find = compilerArr.find(e => {

          if (e && e.kind === "ISoundSetter" && e.varName === char[0]) {
            return e;
          }
        });
        if (find && find.kind === "ISoundSetter") {
          console.log("Last " + char[0] + " is " + find.fileName);
          const sound = require("../assets/" + find.fileName);
          const beat = new Audio(sound);
          compilerArr.unshift({ kind: "ISound", name: char[0], soundFileName: find.fileName, sound: beat });
          setCompilerArr(compilerArr);
        } else {
          // TODO Handle error
        }
      }
    }
  }

  function parseDeclareSound(str: string) {
    if (/^[A-Z]=[A-Za-z]+.mp3$/g.test(str)) {
      const char = str.match(/^[A-Z]|[A-Za-z]+.mp3$/g);
      if (char && char.length <= 2) {
        console.log("We declare: " + char[0] + " set to " + char[1]);
        compilerArr.unshift({ kind: "ISoundSetter", varName: char[0], fileName: char[1] });
        setCompilerArr(compilerArr);
      }
    }
  }

  const line = beatText.match(/[^\r\n]+/g);
  if (!line)
    return;
  line.forEach(e => {
    parsePlaySound(e);
    parseDeclareSound(e);
  });
}

export const BeatParser = BeatParserC;
