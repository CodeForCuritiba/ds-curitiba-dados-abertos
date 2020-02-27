#!/bin/bash

figlet "Deploy 156";

mkdir _deploy;
cp -Rv *.ipynb _deploy;

pip3 install requests pytest coverage pytest-cov;

cd _deploy; 

jupyter nbconvert --to script *.ipynb;

for jupyter_script in *.py
do 
  echo "Processing ${jupyter_script}...";
  mv "${jupyter_script}" "../jupyter_generated_${jupyter_script}";
done

cd ..;

figlet "Running notebooks";
for jupyter_script in jupyter_generated_*.py
do 
  echo " * Running ${jupyter_script}...";
  python3 "${jupyter_script}";
done

figlet "Compressing";
cd clean_data;

dnf install -y bzip2;
bzip2 --best -v *;

cd ..;

figlet "Clean";
rm -f jupyter_generated_*;
rm -Rf _deploy;

echo "Processing Finished!";
