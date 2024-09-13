# EncryptionSSH
### 1. First step remember to download
	```pip install virtualenv```
### 2. Second create a env named myenv
	```python -m venv myenv```
### 3. Then if you already installed virtualenv do this
	```virtualenv /path/to/your/virtual/environment```
### 4. Begin activate your env
#### - For Windows use
	```.\myenv\Scripts\activate```
#### - For Linux use
	```source myenv/bin/activate```
### 5. Download libraries in use
	```pip install python-dotenv```
 	```pip install pycryptodome```
	```pip install cryptography```
 And others if needed
### 6. To run a file
	```python -m <file_name>```
Remember before you run encryption.py, you must have SSH_keys inside your .ssh folder. In Windows it usually ../Users/Admin/.ssh and in Linux it often ~/.ssh. When you run encryption.py it will check if there exist SSH keys inside these folder, if yes begin encryption and delete original key inside .ssh folder, and store encrypted keys to this project. Then you can run decryption.py, It will return your key back to its orgiginal form, store them back to .ssh folder also delete encrypted keys inside this project.
