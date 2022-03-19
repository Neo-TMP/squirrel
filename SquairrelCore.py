class Squirrel:
    genus = None
    type = None
    driver = None
    current_url = None

    def __init__(self, inGenus, inType=None):
        self.genus = inGenus
        self.type = inType

    def initialize(self):
        if self.genus == 'selenium':
            import undetected_chromedriver.v2 as uc

            chrome_options = uc.ChromeOptions()

            # chrome_options.add_argument("--headless")
            chrome_options.add_argument("--disable-extensions")
            chrome_options.add_argument("--disable-popup-blocking")
            chrome_options.add_argument("--profile-directory=Default")
            chrome_options.add_argument("--ignore-certificate-errors")
            chrome_options.add_argument("--disable-plugins-discovery")
            chrome_options.add_argument("--incognito")
            chrome_options.add_argument("--user_agent=DN")
            chrome_options.add_argument('--no-first-run')
            chrome_options.add_argument('--no-service-autorun')
            chrome_options.add_argument('--password-store=basic')

            try:
                self.driver = uc.Chrome(options=chrome_options)
            except Exception as Err:
                print("ERROR ERROR ERROR")
                raise CriticalErrorInitialization(Err)

    def get(self, url):
        if self.genus == 'selenium':
            self.driver.execute_script('window.location.href = "' + url + '"');
            self.current_url = self.driver.current_url

    def close(self):
        if self.genus == 'selenium':
            self.driver.close();