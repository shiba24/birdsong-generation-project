Birdsong generation project
====

Generating birdsongs with Wavenet!

<img src="https://github.com/shiba24/birdsong-generation-project/raw/master/images/bolhuis_2010_fig1.png" width="400px" align="right">


[Listen to natural song at soundcloud](https://soundcloud.com/shintaro-shiba/javasong)

[Listen to generated song at soundcloud](https://soundcloud.com/shintaro-shiba/generated-bird-song-2)
====


# Table of Contents
 - [Quick execution](https://github.com/shiba24/birdsong-generation-project#quick-execution)
     - [Requirements](https://github.com/shiba24/birdsong-generation-project#requirements)
     - [Command](https://github.com/shiba24/birdsong-generation-project#command)
     - [Generated song](https://github.com/shiba24/birdsong-generation-project#generated-song)
 - [Overview](https://github.com/shiba24/birdsong-generation-project#overview)
     - [Abstract](https://github.com/shiba24/birdsong-generation-project#abstract-in-one-sentence)
     - [Background](https://github.com/shiba24/birdsong-generation-project#background)
     - [About this project](https://github.com/shiba24/birdsong-generation-project#this-project)
     - [Why is this interesting?](https://github.com/shiba24/birdsong-generation-project#why-is-this-interesting)
     - [Model configuration](https://github.com/shiba24/birdsong-generation-project#model-configuration)
     - [Result](https://github.com/shiba24/birdsong-generation-project#result)
     - [Discussion](https://github.com/shiba24/birdsong-generation-project#discussion)
 - [Notice](https://github.com/shiba24/birdsong-generation-project#notice)
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
python generate.py --wav_out_path=generated.wav --samples 80000 logdir/train/{DATE_HERE}/model.ckpt-{XXX}
```


## Generated song

[Listen to natural song at soundcloud](https://soundcloud.com/shintaro-shiba/javasong)

[Listen to generated song at soundcloud](https://soundcloud.com/shintaro-shiba/generated-bird-song-2)


# Overview

## Abstract in one sentence

Simulate bird song with WaveNet.

## Background

### What is songbird?

**Songbird** is one of the best model animals for the neuroscientific studies of human language, vocalization, and auditory processing. Many laboratories around the world including molecular biology, physiology, acoustics, and ethology, are using songbird to answer the questions: ***why only humans have language?*** and ***what is the neural mechanism of language?***.

### Song structure

Bird **song** is considered to have **syntax** like human language, although it does **not** have **semantics** within itself. In most species in songbirds only male sings while few species both sexes sing. One function of their song is considered to be sexual attraction to females. Below is typical song structure of songbirds. We can see a bout of several song elements (called _syllable_ or _note_).

You can listen to an example of java sparrow's (文鳥) song [here](https://soundcloud.com/shintaro-shiba/javasong). This is visualized image, or spectrogram, of zebra finch's (錦華鳥) song. Alphabets on the spectrogram represent type of _note_. Both of java sparrow and zebra finch are songbirds.


<img src="https://github.com/shiba24/birdsong-generation-project/raw/master/images/song-label.png"> 

And interestingly, ***the song structure is expressed as finite-state automaton model, which can be regarded as high-order Markov process***. The transition of _notes_ are probablistic, and song is expressed as probabilistic finite-state transition diagram. This is considered to be in parallel with human language ([Berwick et al., 2011](http://www.sciencedirect.com/science/article/pii/S1364661311000039).) This is song expression as finite-state transition diagram. Line thickness represents the probability of transition from _note_ to _note_.


<img src="https://github.com/shiba24/birdsong-generation-project/raw/master/images/finite-state.png" > 

(Both figures cited from [Honda & Okanoya, 1999](http://www.bioone.org/doi/abs/10.2108/zsj.16.319))


### Brain structure


<img src="https://github.com/shiba24/birdsong-generation-project/raw/master/images/bolhuis_2010_fig1.png" width="400px" align="right">


Many researchers approached what is the neural mechanism enabling finite-state vocalization. And one hypothesis is _Markov chain-like representation_ within neurons in the motor areas.
The right figure is neural pathway of _vocalization_ (cited from [Bouhuis et al., 2010](http://www.nature.com/nrn/journal/v11/n11/execsumm/nrn2931.html)). The more detailed brain circuitry including _audition_ can be seen [here](http://web.williams.edu/Biology/Faculty_Staff/hwilliams/Finches/circuits.html) for example. 

We can see there is a brain region named _HVC_ (proper name), which is _pre-motor area_. Many neurons show activity phase-locked to the song. _HVC_ neurons are projecting to _RA_ (robust nucleus of arcopallium), which is _motor area_, and _RA_ outputs motor signal to mustles of vocal organ for the generation of song element.

The next figure (a) is another expression of finite-state transition of song. And (b) is a simple model of _HVC_ and _RA_ neurons. The hypothesis assumes ***neurons in HVC are firing in turn like _chain_.*** (Cited from [Katahira et al, 2007](http://link.springer.com/article/10.1007/s00422-007-0184-y))


<img src="https://github.com/shiba24/birdsong-generation-project/raw/master/images/song_and_brain.png">


There are many studies for modelling (even using neural network) the birdsong and its neural mechanism.


### WaveNet


<img src="https://github.com/shiba24/birdsong-generation-project/raw/master/images/wavenet.gif" width="400px" align="right">


***WaveNet*** is generative neural network model for raw audio file. [The original paper](https://arxiv.org/pdf/1609.03499.pdf) was published by Google DeepMind team in 2016. It uses _dilated convolutional neural network_ to generate audio wave. (Gif image cited from [Blog post of DeepMind](https://deepmind.com/blog/wavenet-generative-model-raw-audio/))

Inputs and outputs for the model are only waveform. **Hence this model itself does NOT assume that the syllables expressed with finite state, nor Markov chain.**


## This project

This project is only my own (not belonging to my supervisor), combining latest machine learning result and knowledge of neuroscience about songbirds.

In one sentence: **using WaveNet to simulate bird song.**

As mentioned above, bird song itself is thought to have Markov-Model structure and syntax like human speech. However, song itself has no semantics.

If the mechanism should be similar between such birds and humans, WaveNet ([original blog](https://deepmind.com/blog/wavenet-generative-model-raw-audio/) and [implementation of tensorflow](https://github.com/ibab/tensorflow-wavenet)) might be successful for simulating birdsong, because it is succssful in generating completely meaningless but locally speech-like sound waveform.


## Why is this interesting?

WaveNet itself doesn't use Markov property of song. It only uses information of raw waveform. Therefore, **if WaveNet succeeds in generating birdsong:**

 1. WaveNet might have an ability to embed Markov property. This is not proved explicitly if we only generate human speech with this model.

 2. Representation obtained by trained model (i.e. activation pattern of _neurons_ in the model) might be comparable with neural representation in actual brain of songbird.

 3. Similaity between human speech and birdsong as syntax could be further supported.


## Model configuration

<dl>
  <dt>Datasize</dt>
  <dd>??</dd>
  <dt>Sampling rate</dt>
  <dd>and</dd>
  <dt>Other settings</dt>
  <dd>will be here</dd>
</dl>


## Result

### Training epoch

After 2500 epoch, loss is about 1.5~2.0.

### Generated sound

[Listen to natural song at soundcloud](https://soundcloud.com/shintaro-shiba/javasong)

[Listen to generated song at soundcloud](https://soundcloud.com/shintaro-shiba/generated-bird-song-2)

It sounds like original (natural) song!! This is visualized image, or spectrogram, of song. (It tells us that the wave sound is a bit chattering, though.)


- Simulated song spectrogram

<img src="https://github.com/shiba24/birdsong-generation-project/raw/master/images/generated-song_spectrogram.png"> 


- Natural song spectrogram

<img src="https://github.com/shiba24/birdsong-generation-project/raw/master/images/javasong_spectrogram.png"> 



## Discussion

The next step of this project would be:

 1. Investigating whether markov-chain structure in the generated song is similar to that in natural song.

 2. Comparing neural firing patterns known-to-date and activated neuron pattern in the model.


### TODOs

 - generate other species songs (e.g. finches, canaries, ...)


# Notice

 - The dataset is not open-access yet. Hense you cannot reproduce this project.

 - This project is only my own, not belonging to my supervisor. All the mistakes and misunderstandings belong to myself.

 - If you are interested in this project (e.g. furthe questions, reproduce, comments and/or feedbacks), feel free to contact [me](https://github.com/shiba24)!


# Copyright

Implementation of Wavenet is done by [ibab](https://github.com/ibab).

All rights reserved [shiba24](https://github.com/shiba24).

 - Started this project November 2016.
 - Updated January 2017.

Any questions or comments are welcomed! Thank you.

