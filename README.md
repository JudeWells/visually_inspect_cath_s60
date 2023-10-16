# visually_inspect_cath_s60
Command line python program for inspecting CATH domanin annotations
Program visualises each PDB file with domain assignments and prompts user to enter decision
which is stored in a csv file.

Domain annotation images available at: /SAN/cath/cath_v4_3_0/visualise_cath_s60.zip

RUN THE FOLLOWING COMMANDS TO GET STARTED:
```
# install matplotlib (python library used to visualise images)
pip install matplotlib

mkdir cath_domain_inspection

# make outer directory
cd cath_domain_inspection

# download images zip file from UCL CS server
scp cs:/SAN/cath/cath_v4_3_0/visualise_cath_s60.zip ./
# decompress images
unzip visualise_cath_s60.zip

# clone this repository
git clone git@github.com:JudeWells/visually_inspect_cath_s60.git

cd visually_inspect_cath_s60

# run the program
python3 visually_inspect_images.py
```
