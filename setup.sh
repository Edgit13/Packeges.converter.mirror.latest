figlet "Welcome"
sleep 2

echo
echo

python -m venv .venv

sleep 2
echo "Created"
sleep 2

clear
echo "Activating venv"
source .venv/bin/activate

sleep 0.5
pip install os sys

sleep 0.5
clear
echo " set uping "

cat <<EOF >run-cli-oneline.sh
#!/bin/bash
DIR="\$(cd "\$(dirname "\${BASH_SOURCE[0]}")" && pwd)"
"\$DIR/.venv/bin/python" "\$DIR/mc-converter-oneline-cli.py" "\$@"
EOF

chmod +x menu.c
chmod +x run-cli-oneline.sh
chmod +x mc-converter-oneline-cli.py
