Birdsong generation project
====

# Notice

This project is work-in-process. The dataset is not open-access yet. Hense you cannot replicate this project.


# Quick execution

## Requirements

- golang 1.7.3+
- python 2.7.11
- [wavenet-tensorflow](https://github.com/ibab/tensorflow-wavenet) (automatically clone in the script)
- GPU (recommended)

## Command

```
# preparation
git clone https://github.com/shiba24/birdsong-generation-project.git
bash preparation.sh

# training  
cd tensorflow-wavenet
python train.py --data_dir=../corpus

# generation
cd tensorflow-wavenet
ython generate.py --wav_out_path=generated.wav --samples 32000 logdir/train/{DATE_HERE}/model.ckpt-{XXX}
```


# Overview

## Abstract in one sentence

Simulate bird song with WaveNet.

## Why birdsong?

Songbird is one of the most popular model animal for the neuroscientific studies of human language, vocalization, and auditory prcessing. Many laboratories around the world including molecular biology, physiology, acoustics, and ethology, are using songbird to investigate why only humans have language and what is the mechanism of language.


## Background: brief summary of previous research

### Song structure

***Birdsong*** is considered to have syntax like human language. This is typical song structure of songbirds. We can see bout of several song elements (called _syllable_ or _note_).

(figure)

And interestingly, ***the song structure is expressed as Markov model***. The transition of notes are probablistic.

(figure)


### Brain structure

This is neural pathway of vocalization (cited from [Bouhuis et al. 2010, Nature Rev. Neurosci.](http://www.nature.com/nrn/journal/v11/n11/execsumm/nrn2931.html)). The more detailed brain circuitry can be seen [here](http://web.williams.edu/Biology/Faculty_Staff/hwilliams/Finches/circuits.html) for example. 

<img src="https://github.com/shiba24/birdsong-generation-project/blob/master/images/bolhuis_2010_fig1.png" width="400px">

We can see there is brain part called _HVC_, pre-motor area. ***Neurons in HVC are firing in turn like Markov-chain.*** Each neuron shows activity phase-locked to the song, regulating the timing of each song element. HVC neurons are projecting to _RA_, motor area, and RA outputs motor signal to mustles of vocal organ for the generation of song element. There are many studies for modelling the birdsong and its neural mechanism.

(figure)


## This project

This project is only my own (not belonging to my supervisor). In one sentence: ***using WaveNet to simulate bird song.***

As mentioned above, bird song itself is thought to have Markov-Model structure and syntax like human speech. However, song itself has no semantics.

If the mechanism should be similar between such birds and humans, WaveNet ([original blog](https://deepmind.com/blog/wavenet-generative-model-raw-audio/) and [implementation of tensorflow](https://github.com/ibab/tensorflow-wavenet)) might be successful for simulating birdsong, because it is succssful in generating completely meaningless but locally speech-like sound waveform.

And if it succeed, the next step of this project would be 1. Investigating whether markov-chain structure appears in the generated song, and 2. Comparing neural firing patterns known-to-date and activated neuron pattern in the model.


## Result











