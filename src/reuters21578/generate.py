import argparse
import arff
import os
import traceback

from bs4 import BeautifulSoup


def generate(topics_file, data_dir, output_file):
    """
    Generates the ARFF file.

    :param topics_file: the text file with the topics
    :type topics_file: str
    :param data_dir: the directory with the .sgm files
    :type data_dir: str
    :param output_file: the ARFF file to generate
    :type output_file: str
    """
    # topics
    with open(topics_file, "r") as fp:
        topics = fp.readlines()
    topics = [x.strip() for x in topics]

    # structure
    atts = []
    atts.append(('file', 'STRING'))
    atts.append(('new_id', 'STRING'))
    atts.append(('old_id', 'STRING'))
    atts.append(('text', 'STRING'))
    for topic in topics:
        atts.append((topic, ['y', 'n']))
    relation = "Reuters-21578: '-C %d'" % len(topics)
    desc = 'Reuters 21578 dataset:\nhttp://kdd.ics.uci.edu/databases/reuters21578/reuters21578.html'
    data = []
    dataset = {
        'relation': relation,
        'description': desc,
        'attributes': atts,
        'data': data,
    }


    # read .sgm
    sgm_files = []
    for f in os.listdir(data_dir):
        if not f.endswith(".sgm"):
            continue
        fname = os.path.join(data_dir, f)
        sgm_files.append(fname)
    sgm_files.sort()

    for fname in sgm_files:
        print(fname)
        with open(fname, "r", encoding='ISO-8859-1') as fp:
            soup = BeautifulSoup(fp, 'html.parser')
            docs = soup.find_all("reuters")
            for doc in docs:
                if doc['topics'] != 'YES':
                    continue
                # topics
                topics_set = set()
                topics_tags = doc.findChildren('topics')
                if len(topics_tags) != 1:
                    continue
                topic_names = topics_tags[0].findChildren('d')
                if len(topic_names) == 0:
                    continue
                for topic_name in topic_names:
                    topics_set.add(topic_name.get_text())
                # body
                body = doc.findChildren('body')
                if len(body) > 0:
                    body_text = body[0].get_text()
                # add row
                row = []
                data.append(row)
                row.append(f)
                row.append(doc['newid'])
                row.append(doc['oldid'])
                row.append(body_text)
                for topic in topics:
                    if topic in topics_set:
                        row.append('y')
                    else:
                        row.append('n')

    # write ARFF
    with open(output_file, "wt") as fp:
        arff.dump(dataset, fp)


def main(args=None):
    """
    Uses either the provided command-line arguments or the system ones
    to generate the statistics.

    :param args: the arguments to use instead of system ones
    :type args: list
    """
    parser = argparse.ArgumentParser(
        description='Reads the Bearable App CSV output and lists medications or their changes.',
        prog="bstats-list-medications")
    parser.add_argument("-t", "--topics_file", metavar="FILE", required=True, dest="topics_file", help="the file with all the topics (one per line).")
    parser.add_argument("-d", "--data_dir", metavar="DIR", required=True, dest="data_dir", help="the directory with the .sgm files.")
    parser.add_argument("-o", "--output_file", metavar="FILE", required=True, dest="output_file", help="the ARFF file to generate.")
    parsed = parser.parse_args(args=args)
    generate(parsed.topics_file, parsed.data_dir, parsed.output_file)


def sys_main():
    """
    Runs the main function using the system cli arguments, and
    returns a system error code.
    :return: 0 for success, 1 for failure.
    :rtype: int
    """

    try:
        main()
        return 0
    except Exception:
        print(traceback.format_exc())
        return 1


if __name__ == "__main__":
    try:
        main()
    except Exception:
        print(traceback.format_exc())
