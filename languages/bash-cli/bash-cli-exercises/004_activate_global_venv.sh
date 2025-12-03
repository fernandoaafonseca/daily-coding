#!/usr/bin/env bash

VENV='/home/cosmo/Documents/venv/global_venv'
ACTIVATE="$VENV/bin/activate"

# Detects whether the script is being sourced (run with '.' or 'source')
# In bash, when sourced: BASH_SOURCE[0] != $0
if [ "${BASH_SOURCE[0]}" != "${0}" ]; then
    : # we are being sourced
else
    echo '❌ This script must be *sourced* to activate the venv.'
    echo '👉 Use:'
    echo "   . $0"
    echo 'or'
    echo "   source $0"
    exit 1
fi

echo '-=-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-=-=-=-=-'
echo '🖥 Starting standard virtual environment...'
echo '-=-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-=-=-=-=-'

if [ ! -f "$ACTIVATE" ]; then
    echo '❌ "activate" not found! Check the path.'
    # if sourced, use return so we don’t close the parent shell
    return 1 2>/dev/null || exit 1
fi

# Activates in the current shell
source "$ACTIVATE" || {
    echo '❌ Failed to source activate.'
    return 1 2>/dev/null || exit 1
}

echo '👾 Standard venv activated!'
echo '-=-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-=-=-=-=-'
echo '📌 venv location: '
echo '    '$VENV
echo '🧩 To see all installed packages:'
echo '    pip list'
echo '🔎 To show information about an installed package:'
echo '    pip show "package_name"'
echo '💾 To generate a requirements file:'
echo '    pip freeze > requirements.txt'
echo '📋 To install requirements:'
echo '    pip install -r requirements.txt'
echo '🔌 To deactivate the venv:'
echo '    deactivate'
echo '-=-=-=-=-=--=-=-=-=-=--=-=-=-=-=--=-=-=-=-=-'


# -----------------------------------------------------------------------------
# Alternative method for a universal venv:
#
# Create a single fixed venv, like:
#
#   /home/cosmo/.venvs/global_env
#
# Activate it and install the packages you always use
# (requests, numpy, rich, etc.).
#
# Then, inside your ~/.bashrc, add:
#
#   globalenv() {
#       . '/home/cosmo/.venvs/global_env/bin/activate'
#   }
#
# Reload:
#
#   source ~/.bashrc
#
# Now you just need to type:
#
#   globalenv
#
# from any directory in the system, and your “universal venv” becomes active.
# -----------------------------------------------------------------------------
