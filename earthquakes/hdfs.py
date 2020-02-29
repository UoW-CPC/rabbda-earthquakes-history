import subprocess
import time

class HDFS:

    path = "";

    @classmethod
    def command(cls,args_list):
        """
        run linux commands
        """
        # import subprocess
        print('Running system command: {0}'.format(' '.join(args_list)))
        print ""
        proc = subprocess.Popen(args_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        s_output, s_err = proc.communicate()
        s_return = proc.returncode
        return s_return, s_output, s_err

    @classmethod
    def put(cls,file,path):
        (ret, out, err) = cls.command(['hdfs', 'dfs', '-put', file, path])
        if ret == 1:
            print "Error while uploading the file to HDFS: "
            print err
        else:
            print "File successfully uploaded to HDFS."


    @classmethod
    def pathValidation(cls,path):
        cls.path = path
        "HDFS status check:"
        (ret, out, err) = cls.command(['hdfs', 'dfs', '-ls', path])
        if ret ==1:
            print "HDFS path Error: "
            print err
            print "The data will be downloaded in the local machine, but may not be available through HDFS."
            print "Interrupt the application if you want to specify a valid HDFS path."
            print ""
            print "Data acquisition starts in 10 seconds."
            time.sleep(10)
        else:
            print "Valid HDFS path."
            print ""
            print "Data acquisition starts in 10 seconds."
            time.sleep(10)

    @classmethod
    def getPath(cls):
        return cls.path