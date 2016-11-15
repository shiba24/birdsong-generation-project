### go installation
wget https://storage.googleapis.com/golang/go1.7.3.linux-amd64.tar.gz
sudo tar -C /usr/local -xzf go1.7.3.linux-amd64.tar.gz
export PATH=$PATH:/usr/local/go/bin
mkdir ~/go
mkdir ~/go/bin
mkdir ~/work
# export GOROOT=$HOME/go
# export PATH=$PATH:$GOROOT/bin
export GOPATH=$HOME/work


### skicka installation
go get github.com/google/skicka
skicka init
skicka -no-browser-auth ls


### downlaod data
cd birdsong-generation-project/
mkdir data
skicka download java_song data/


### install dependencies for wave resample
sudo pip install --upgrade pip
pip install --user argparse
pip install --user tqdm


### resampling data
mkdir corpus


git clone https://github.com/ibab/tensorflow-wavenet.git
go get github.com/prasmussen/gdrive
cd tensorflow-wavenet
pip install --user -r requirements.txt
cd ..




