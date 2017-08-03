import shutil
import os
import sys
import subprocess

# increment the version number
# see pep440 for more details
# following this scheme
# X.YaN   # Alpha release
# X.YbN   # Beta release
# X.YrcN  # Release Candidate
# X.Y     # Final release
ixnetwork_version = '0.55a17'

# comment out the following to only publish locally
sys.argv.append('--publish')

# clear out all artifacts
for path in ['dist', 'build', 'ixnetwork.egg-info']:
    if os.path.exists(path):
        shutil.rmtree(path)

# set the version number and create the universal wheel
with open('setup.py', 'r') as fid:
    setup_content = fid.read()
content = setup_content.replace('IXNETWORK_VERSION', ixnetwork_version)
with open('setup.py', 'w') as fid:
    fid.write(content)
subprocess.call([sys.executable, 'setup.py', 'bdist_wheel'])
with open('setup.py', 'w') as fid:
    fid.write(setup_content)

# if --publish is present push it to pypi otherwise install it locally
dist = './dist/ixnetwork-%s-py2.py3-none-any.whl' % ixnetwork_version
python_path = os.path.dirname(sys.executable)
subprocess.call(['%s/scripts/pip' % python_path, 'uninstall', '--yes', 'ixnetwork'])
if '--publish' in sys.argv:
     subprocess.call(['%s/scripts/twine' % python_path, 'upload', '-u', 'abalogh', '-p', 'BingBang0', dist])
     subprocess.call(['%s/scripts/pip' % python_path, 'install', '--upgrade', '--no-cache-dir',  'ixnetwork'])
else:
     subprocess.call(['%s/scripts/pip' % python_path, 'install', '--upgrade', '--no-cache-dir', dist])

print('ixnetwork client build %s complete' % ixnetwork_version)
