# Notefinder

Notefinder is a tool I hacked together to quickly translate guitar tabs to the correct note and tone.

## Usage
Place your tabs in the classic eBGDAE format in a file called tabs.txt.

Here's an input example with the tabs to Tash Sultana's - Jungle Intro:

```
e|-----------------------------------------------------14-12----12---------------------|
B|-----7-9-12---------------------------------------12-------14----14-12-14------12-14-|
G|-6-9--------11-9-11-9----9------------------11-13-------------------------13-13------|
D|----------------------11---11-9-11-9-------------------------------------------------|
A|-------------------------------------9-11-9------------------------------------------|
E|-------------------------------------------------------------------------------------|



e|-12----11-11-11-12-12-|
B|----14----------------|
G|----------------------|
D|----------------------|
A|----------------------|
E|----------------------|
```

It is important that all guitar strings are present in a neck block, and that each neck block is separated by one or more line breaks.

Then you can run `python translator.py` and the script will output the guitar neck (to preserve rhythm/tremolo/h's or p's) with the tabs replaced by the correct note and it's octave.

```
(env) F:\TabsToNotes>python mfinder.py
e|-----------------------------------------------------F#3-E3----E3---------------------|
B|-----F#2-G#2-B3---------------------------------------B3-------C#3----C#3-B3-C#3------B3-C#3-|
G|-C#2-E2--------F#2-E2-F#2-E2----E2------------------F#2-G#2-------------------------G#2-G#2------|
D|----------------------C#2---C#2-B2-C#2-B2-------------------------------------------------|
A|-------------------------------------F#1-G#1-F#1------------------------------------------|
E|-------------------------------------------------------------------------------------|



e|-E3----D#3-D#3-D#3-E3-E3-|
B|----C#3----------------|
G|----------------------|
D|----------------------|
A|----------------------|
E|----------------------|
```

The output isn't perfect, but it works for what I need it for. Feel free to create an issue or PR if you'd like to see a change.
