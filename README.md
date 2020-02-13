## Unity Unpackager Script

### Purpose
Python script to convert `.unitypackage` archives into raw assets.
Useful when trying to use a Unity asset pack in another game engine.

Developed and tested with Python 3.7.

### Usage
`./unpackager.py <UNITY_PACKAGE_FILE> --out <OUTPUT_DIR>` \
The `--out` flag is optional; it defaults to `out`.

### Methodology
`.unitypackage` files are `.tar.gz` archives containing a folder for each
asset. Each folder contains a `pathname` file and perhaps an `asset` file
containing the actual data. The `asset` file is then renamed according to
`pathname` and stored in the output directory.
