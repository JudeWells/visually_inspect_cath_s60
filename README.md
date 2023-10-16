# visually_inspect_cath_s60
Command line python program for inspecting CATH domanin annotations
Program visualises each PDB file with domain assignments and prompts user to enter decision
which is stored in a csv file.

Domain annotation images available at: /SAN/cath/cath_v4_3_0/visualise_cath_s60.zip

RUN THE FOLLOWING COMMANDS TO GET STARTED:
```
mkdir cath_domain_inspection

# install Pillow (python image library)
pip install Pillow

# make outer directory
cd cath_domain_inspection
# download images zip file from UCL CS server
scp cs:/SAN/cath/cath_v4_3_0/visualise_cath_s60.zip ./
# decompress images
unzip visualise_cath_s60.zip

# run the program
python3 visually_inspect_images.py
```
