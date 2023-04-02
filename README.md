# Install RPI

sudo addgroup --system bminotify
sudo adduser --disabled-password --system --home /var/lib/bminotify --gecos "BMI-Notify" --ingroup bminotify bminotify
sudo adduser bminotify dialout


sudo mkdir /opt/bminotify && sudo chown bminotify:bminotify /opt/bminotify
sudo -u bminotify git clone https://github.com/luukderooij/BMI-Notify.git /opt/bminotify


sudo cp -v /opt/bminotify/scripts/bminotify.service /etc/systemd/system/bminotify.service
sudo chown root:root /etc/systemd/system/bminotify.service
sudo chmod 644 /etc/systemd/system/bminotify.service


sudo apt install python3-pip
sudo -u bminotify python3 -m pip install -r requirements.txt

sudo nano /boot/cmdline.txt
remove: console=serial0,115200

sudo systemctl enable bminotify
sudo systemctl start bminotify
sudo systemctl status bminotify




# Update

sudo -u bminotify git pull