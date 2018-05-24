import luigi
import luigi.contrib.hadoop
import luigi.contrib.hdfs


# return the target data from HDFS
class InputData(luigi.ExternalTask):
    """
    External Task: It doesn't generate the output target on its own
                   instead relies on the execution of something outside of Luigi to produce it
    """

    # generates the Target object from the HDFS file and return it
    def output(self):
        return luigi.contrib.hdfs.HdfsTarget('/input_dir/data.txt')


# this task run a hadoop job over the target data returned by the InputData task
# writes the result into its output target
class TotalSalesPerCost(luigi.contrib.hadoop.JobTask):

    def requires(self):
        return InputData()

    def output(self):
        return luigi.contrib.hdfs.HdfsTarget('/output_dir_luigi/out.txt')

    def mapper(self, line):
        # strip of extra whitespaces, also split on tab and put the data in a array
        data = line.strip().split("\t")

        # defensive code to handle cases where data is not as expected
        # ignoring line if 6 fields are not present
        if len(data) == 6:
            # get the fields
            data, time, store, item, cost, payment = data
            yield store, float(cost)

    def reducer(self, key, values):
        yield key, sum(values)


if __name__ == '__main__':
    luigi.build([TotalSalesPerCost()], local_scheduler=True)
