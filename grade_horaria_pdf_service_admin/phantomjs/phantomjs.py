import os
from selenium import webdriver

#https://stackoverflow.com/questions/16927090/python-selenium-phantomjs-render-to-pdf

def download(driver, target_path):

    def execute(script, args):
        driver.execute('executePhantomScript',
                       {'script': script, 'args': args})

    # hack while the python interface lags
    driver.command_executor._commands['executePhantomScript'] = ('POST', '/session/$sessionId/phantom/execute')

    # render current page
    render = '''this.render("{}")'''.format(target_path)
    execute(render, [])


def get_pdf(url):

    driver = webdriver.PhantomJS()

    driver.get(url)

    download(driver, "media/save_me.pdf")

    pdf = open('media/save_me.pdf', 'rb')

    os.remove('media/save_me.pdf')

    return pdf
