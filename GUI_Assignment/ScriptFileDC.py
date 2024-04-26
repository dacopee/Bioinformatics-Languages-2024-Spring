import pipelineParser
import subprocess

def main():
    pipelineParser.main()
    command = ["Rscript", "C:\\RIT Classes\\BIO 230 Bioinformatic Lang\\GUI Pipeline\\RCodeDCPipe.R"]
    subprocess.run(command, check=True)

if __name__ == '__main__':
    main()
    print("Script Runner Finished")
    exit