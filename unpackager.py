#!/usr/bin/env python3
from pathlib import Path
from shutil import copyfile, rmtree

temp_dir = 'tmp'

def expand_upkg_file(file_name, out_dir):
    import tarfile
    t_ref = tarfile.open(file_name, mode='r:gz')
    t_ref.extractall(out_dir)
    t_ref.close()

def process_asset_dir(asset_dir, out_dir_str):
    out_dir = Path(out_dir_str)
    pathname = None
    #pathname file contains actual asset name
    with (asset_dir/'pathname').open('r') as pathname_file:
        pathname = pathname_file.read()
    if pathname is not None and (asset_dir/'asset').exists():
        print(f'copying {pathname}')
        #create folder if needed
        (out_dir/pathname).parent.mkdir(parents=True, exist_ok=True)
        copyfile(asset_dir/'asset', out_dir/pathname)

def main(input_file, output_dir):
    print(f'expanding assets from {input_file}')
    expand_upkg_file(input_file, temp_dir)
    print('decoding assets')
    for sub_dir in Path(temp_dir).iterdir():
        process_asset_dir(sub_dir, output_dir)
    print('cleaning up')
    rmtree(temp_dir)
    print(f'done! assets stored in {output_dir}')

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Unpackage .UnityPackage files into raw assets.')
    parser.add_argument('input', metavar='I', help='.unitypackage file to be processed')
    parser.add_argument('--out', default='out', help='output directory')
    args = parser.parse_args()
    main(args.input, args.out)
