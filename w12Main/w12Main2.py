import time
def Upper():
    msg='[MJH edited {0}]'.format(time.strftime('%Y-%m-%d  %H:%M:%S'))
    fin=open('output.txt', 'r')
    fout=open('outputUpper.txt','w')
    for line in fin:
        words=line.split()
        fout.write(msg)
        fout.write('\t')
        for word in words:
            if word =="line":
                fout.write('\t')
            fout.write(word)
        fout.write('\n')
    fin.close()
    fout.close()
 
def Number():
    data=[1,2,3,4,5,6,7,8,9,10]
    fout=open('outputNumber.txt','w')
    for i in data:
        str="{0}\t".format(i)
        fout.write(str)
        if i%2==0:
            fout.write('\n')
    fout.close()


def lab12():
    Upper()
    Number()

def main():
    lab12()
    %load outputUpper.txt
    %load outputNumber.txt
  

main()
raw_input(" ")