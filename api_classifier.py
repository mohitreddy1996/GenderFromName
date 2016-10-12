"""
    Class which takes in name as the input and return the gender and probability.
    Using genderize API available online.
"""
import utils
import json
import logging


class Genderize:
    base_curl = """ curl 'https://api.genderize.io/?name\[0\]=___name___' -H 'Accept-Encoding: gzip, deflate, sdch, br' -H 'Accept-Language: en-US,en;q=0.8' -H 'Upgrade-Insecure-Requests: 1' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' """

    def __init__(self):
        self.flag = -1
        self.gender = "MALE"
        self.prob = 1.0
        pass

    def get_gender(self, name):
        new_curl = Genderize.base_curl.replace(utils.replace_name_util["NAME"], name)
        res = utils.robust_curl(new_curl)
        json_data = json.loads(res)
        try:
            if "gender" in json_data and "probability" in json_data:
                self.gender = json_data["gender"]
                self.flag = 0
                self.prob = json_data["probability"]
        except:
            logging.warning("Could not find the gender for the name : " + name)

        return self.flag, self.gender, self.prob
