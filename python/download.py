import requests as rq
import sys
import urllib


help_msg = '''
download  input.txt prefix outputdir
'''

def download(url,outputdir):
    print url
    save_file_name = url.split('/')[-1]
    save_file_name = outputdir + '/'+save_file_name[:-1]
    urllib.urlretrieve(url,save_file_name)
    ''' 
    r = rq.get(url, stream=True)

    if r.ok:
        with open(save_file_name,'wb') as fd:
            for chunk in r.iter_content(1024):
                 print 'write'
                 fd.write(chunk)
    else:
        print r.text
    '''


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print help_msg
        sys.exit(2)
    input_file = sys.argv[1]
    prefix = sys.argv[2]
    outputdir = sys.argv[3]

    fo = open(input_file,"rw+")
    print prefix,outputdir
    for line in fo.readlines():
        download(prefix+line,outputdir)
        print line

