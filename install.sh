#!/bin/bash
INSTALL_SRC=data
if [ ! -d "$INSTALL_SRC/etc" ]; then
    echo "Error: You must be in the same directory as the '$INSTALL_SRC' folder."
    exit 1
fi


PI_SERVICE="shutdown-button.service"
SERVICE="$PI_SERVICE"
if [ "$1" = "--flag" ]; then
    SERVICE="shutdown-flag.service"
fi

if [ "$SERVICE" = "$PI_SERVICE" ]; then
    if [ ! -d ".venv" ]; then
        sudo apt-get update
        echo "Installing precompiled Python packages (saves time if your distro has a version in the version range required by escpos or its dependencies)..."
        sudo apt-get install -y python3-rpi.gpio || exit $?
        echo "Creating .venv..."
        python -m venv .venv
    fi
    sed -i 's|include-system-site-packages = false|include-system-site-packages = true|g' .venv/pyvenv.cfg || exit $?
fi
# works fine even though destination has slash:
# sudo rsync -rtv $INSTALL_SRC/ / || exit $?
cp $INSTALL_SRC/etc/systemd/system/$SERVICE /tmp/$SERVICE.tmp || exit $?
sed -i "s|/home/user|$HOME|g" /tmp/$SERVICE.tmp || exit $?
# sed -i "s|User=user|User=root|g" /tmp/$SERVICE.tmp || exit $?

sudo cp /tmp/$SERVICE.tmp /etc/systemd/system/$SERVICE || exit $?

sudo systemctl daemon-reload
sudo systemctl enable $SERVICE || exit $?
sudo systemctl start $SERVICE || exit $?
