import luigi
import luigi.contrib.hdfs
import luigi.contrib.hadoop
import re


class InputTask(luigi.ExternalTask):
    def output(self):
        return luigi.contrib.hdfs.HdfsTarget('/input_dir/')


class UrlAccessFrequency(luigi.contrib.hadoop.JobTask):
    # regex pattern
    regex = r'GET\s(.*?)\s'

    def requires(self):
        return InputTask('/output_dir_luigi/out')

    def output(self):
        return luigi.contrib.hdfs.HdfsTarget('')

    def mapper(self, line):
        # regex search to get data
        data = re.search(self.regex, line)
        # check if data exists
        if data is not None:
            if data.groups(0) is not None:
                # print(data.group())
                url = data.groups(0)[0]
                # the pair
                yield url, int(1)

    def reducer(self, key, values):
        yield key, sum(values)
