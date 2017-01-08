Birdsong generation project
====

# Notice

This project is work-in-process. The dataset is not open-access yet. Hense you cannot replicate this project.


## Table of Contents
 - [Quick execution](https://github.com/shiba24/birdsong-generation-project#quick-execution)
     - [Requirements](https://github.com/shiba24/birdsong-generation-project#requirements)
     - [Command](https://github.com/shiba24/birdsong-generation-project#command)
 - [Overview](https://github.com/shiba24/birdsong-generation-project#overview)
     - [Abstract](https://github.com/shiba24/birdsong-generation-project#abstract-in-one-sentence)
     - [Background](https://github.com/shiba24/birdsong-generation-project#background)
     - [About this project](https://github.com/shiba24/birdsong-generation-project#this-project)
     - [Result](https://github.com/shiba24/birdsong-generation-project#result)
     - [Discussion](https://github.com/shiba24/birdsong-generation-project#discussion)
 - [Copyright](https://github.com/shiba24/birdsong-generation-project#copyright)



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


## Background

### Song structure

***Birdsong*** is considered to have syntax like human language. This is typical song structure of songbirds. We can see bout of several song elements (called _syllable_ or _note_).

You can listen to an example of sparrow's song [here](https://soundcloud.com/shintaro-shiba/javasong).

(figure)

And interestingly, ***the song structure is expressed as Markov model***. The transition of notes are probablistic.

(figure)


### Brain structure

<img src="https://github.com/shiba24/birdsong-generation-project/blob/master/images/bolhuis_2010_fig1.png" width="400px" align="right">

This figure is neural pathway of vocalization (cited from [Bouhuis et al. 2010, Nature Rev. Neurosci.](http://www.nature.com/nrn/journal/v11/n11/execsumm/nrn2931.html)). The more detailed brain circuitry can be seen [here](http://web.williams.edu/Biology/Faculty_Staff/hwilliams/Finches/circuits.html) for example. 

We can see there is brain part called _HVC_, pre-motor area. ***Neurons in HVC are firing in turn like Markov-chain.*** Each neuron shows activity phase-locked to the song, regulating the timing of each song element. HVC neurons are projecting to _RA_, motor area, and RA outputs motor signal to mustles of vocal organ for the generation of song element. There are many studies for modelling the birdsong and its neural mechanism.

(figure)


### WaveNet

<img src="https://github.com/shiba24/birdsong-generation-project/blob/master/images/wavenet.gif" width="400px" align="right">

WaveNet is generative neural network for raw audio file. [The original paper](https://arxiv.org/pdf/1609.03499.pdf) is published by Google DeepMind team in 2016. It uses dilated convolutional neural network to generate audio wave. (GIf image cited from [Blog post of DeepMind](https://deepmind.com/blog/wavenet-generative-model-raw-audio/))

Inputs and outputs for the model are only wave. This model itself does ***NOT*** assume that the syllables expressed with Markov model.


## This project

This project is only my own (not belonging to my supervisor), combining latest machine learning result and knowledge of neuroscience about songbirds.

In one sentence: ***using WaveNet to simulate bird song.***

As mentioned above, bird song itself is thought to have Markov-Model structure and syntax like human speech. However, song itself has no semantics.

If the mechanism should be similar between such birds and humans, WaveNet ([original blog](https://deepmind.com/blog/wavenet-generative-model-raw-audio/) and [implementation of tensorflow](https://github.com/ibab/tensorflow-wavenet)) might be successful for simulating birdsong, because it is succssful in generating completely meaningless but locally speech-like sound waveform.

And if it succeed, the next step of this project would be 1. Investigating whether markov-chain structure appears in the generated song, and 2. Comparing neural firing patterns known-to-date and activated neuron pattern in the model.


### A bit detailed settings

<dl>
  <dt>Datasize</dt>
  <dd>??</dd>
  <dt>Sampling rate</dt>
  <dd>1.6 kHz</dd>
  <dt>Other settings</dt>
  <dd>will be here</dd>
</dl>


## Result

### Training epoch



### Generated sound


Listen at soundcloud https://soundcloud.com/shintaro-shiba/generated-bird-song-2

(image)


## Discussion



# Copyright

Implementation of Wavenet is done by [ibab](https://github.com/ibab). Thank you!!

All rights reserved [shiba24](https://github.com/shiba24).

 - Started this project November 2016.
 - Updated January 2017.

Any questions or comments are welcomed! Thank you.

