# Python utils
My open utils python scripts

Create a new virtual environment (replace 'env' with your desired environment name)
```bash
python -m venv env
# Activate the virtual environment
source env/bin/activate # MAC
.\env\Scripts\activate # WIN
```
Install requeriments
```bash
pip install -r requirement.txt
```
Bind to compare two images into one, remember to download the font you like, and add the path to the tff in the config/config.py file
```bash
python main_bind_image.py before.png after.png
```