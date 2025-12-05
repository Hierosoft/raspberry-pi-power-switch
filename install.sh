#!/bin/bash
INSTALL_SRC=data
if [ ! -d "$INSTALL_SRC/etc" ]; then
    echo "Error: You must be in the same directory as the '$INSTALL_SRC' folder."
    exit 1
fi


if [ ! -d ".venv" ]; then
    sudo apt-get update
    echo "Installing precompiled Python packages (saves time if your distro has a version in the version range required by escpos or its dependencies)..."
    sudo apt-get install -y python3-rpi.gpio || exit $?
    echo "Creating .venv..."
    python -m venv .venv
fi
sed -i 's|include-system-site-packages = false|include-system-site-packages = true|g' .venv/pyvenv.cfg || exit $?

# works fine even though destination has slash:
# sudo rsync -rtv $INSTALL_SRC/ / || exit $?
cp $INSTALL_SRC/etc/systemd/system/shutdown-button.service /tmp/shutdown-button.service.tmp || exit $?
sed -i "s|/home/user|$HOME|g" /tmp/shutdown-button.service.tmp || exit $?
sudo cp /tmp/shutdown-button.service.tmp /etc/systemd/system/shutdown-button.service || exit $?

sudo systemctl daemon-reload
sudo systemctl enable shutdown-button.service || exit $?
sudo systemctl start shutdown-button.service || exit $?
