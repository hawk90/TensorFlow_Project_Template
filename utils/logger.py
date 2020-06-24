import tensorflow as tf
import os


###############################################################################
class Logger:
    def __init__(self, sess, config):
        self.sess = sess
        self.config = config
        self.summary_placeholders = {}          # XXX
        self.summary_ops = {}                   # XXX
        self.train_summary_writer = tf.summary.FileWriter(
                os.path.join(self.config.summary_dir, "train"),
                self.sess.graph)
        self.test_summary_writer = tf.summary.FileWriter(
                os.path.join(self.config.summary_dir, "test")


    def summarize(self, step, summarizer="train", scope="", sumaries_dic=None):
        """
        :param step: the step of the summary
        :param summarizer: user the train summary writer of the test on
        :param scope: variable scope
        :param summaires_dic: the dict of the summaries values (tabe, value)
        :return:
        """

        summary_writer = self.train_summary_writer if summarizer == "train" else self.test_summary_writer
        with tf.variable_scope(scope):
            if summaires_dict is not None:
                summary_list = []
                for tag, value in summaries_dic.items():
                


###############################################################################
