# install libraries through pip mamanger

echo "Installing requirements"
chmod 0755 requirements.txt
python3 -m pip install -r requirements.txt
python3 -m pip install webdriver-manager