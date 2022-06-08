# reuters21578
Python script to convert the Reuters-21578 dataset into an ARFF file for MEKA.

## Original data

Download the original data from here:

http://kdd.ics.uci.edu/databases/reuters21578/reuters21578.html

And extract it.


# Install

* Clone repository

  ```bash
  git clone https://github.com/fracpete/reuters21578.git
  ```

* Change into repo

  ```bash
  cd reuters21578
  ```

* Create virtual environment

  ```bash
  virtualenv -p /usr/bin/python3 venv
  ./venv/bin/pip install .
  ```

## Generate ARFF

You can use the `reuters-generate` console script to generate the ARFF file:

```
usage: reuters-generate [-h] -t FILE -d DIR -o FILE

Generates a MEKA ARFF file from the Reuters 21578 SGML files.

optional arguments:
  -h, --help            show this help message and exit
  -t FILE, --topics_file FILE
                        the file with all the topics (one per line).
  -d DIR, --data_dir DIR
                        the directory with the .sgm files.
  -o FILE, --output_file FILE
                        the ARFF file to generate.
```
