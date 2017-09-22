from os.path import join
from os import walk
import xlrd

def _get_filelist(directory):
    filelist = []
    for root, dirs, files in walk(directory, topdown=False):
        for name in files:
            filelist.append(join(root, name))
        for name in dirs:
            filelist.append(join(root, name))
    return filelist


def discover_source_type(filename):
    source_type = "unknown"
    try:
        book = xlrd.open_workbook(filename)
        if "Cross Modular Interviews" in book.sheet_names():
            sheet = book.sheet_by_name("Cross Modular Interviews")
            print(sheet.row(1))
            source_type = "Cross Modular"
        if "Help Desk" in book.sheet_names():
            sheet = book.sheet_by_name("Help Desk")
            print(sheet.row(1))
            source_type = "Cross Modular"
            source_type = "non Cross Modular"

    except xlrd.XLRDError:
        source_type = "not Excel"
    finally:
        return source_type



if __name__ == '__main__':
    a = (_get_filelist("../data"))
    for fname in a:
        print ("{0} ---> {1}".format(fname, discover_source_type(fname)))

