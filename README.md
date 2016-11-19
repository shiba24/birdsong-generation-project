Birdsong generation project
====


# Quick command 

## Notice

The dataset is not open-access yet. Hense you cannot replicate this project on your own.


## Preparetion

```
git clone https://github.com/shiba24/birdsong-generation-project.git
bash preparation.sh
```

## Training 

```
cd tensorflow-wavenet 
python train.py --data_dir=../corpus
```


# Overview

## Why birdsong?

Songbird is one of the most popular model animal for the studies of human language, vocalization, and auditory prcessing. Many laboratories around the world (actually many top universities in the US have songbird lab) in neurosciene including molecular biology, physiology, acoustics, and ethology, are using songbird to investigate why only humans have language and what is the mechanism of language.



## Brief previous research summary




## This project

This project is only my own (not belonging to my supervisor), using WaveNet to simulate bird song.

As mentioned above, bird song itself is thought to have Markov-Model structure and syntax like human speech. However, song itself has no semantics.

If the mechanism should be similar between such birds and humans, WaveNet might be successful for simulating birdsong, because it is succssful in generating completely meaningless but locally speech-like sound waveform.

And if it succeed, the next step of this project would be 1. Investigating whether markov-chain structure appears in the generated song, and 2. Comparing neural firing patterns known-to-date and activated neuron pattern in the model.




# Supplementary infomation


## Songbird Laboratories










