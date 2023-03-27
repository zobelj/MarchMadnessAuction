from kenpompy.utils import login
from lib.Secrets import KENPOM_USER, KENPOM_PASS

def download_kp_summary(filename):
    print("# Getting summary data...")

    browser = login(KENPOM_USER, KENPOM_PASS)

    browser.open("https://kenpom.com/")
    browser.download_link(file=f"data/{filename}.csv", link_text="data")

    return

if __name__ == '__main__':
    download_kp_summary("summary2")

