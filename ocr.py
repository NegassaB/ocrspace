import requests
import configs
from pprint import pprint


class OCRSpaceLanguage:
    Arabic = 'ara'
    Bulgarian = 'bul'
    Chinese_Simplified = 'chs'
    Chinese_Traditional = 'cht'
    Croatian = 'hrv'
    Danish = 'dan'
    Dutch = 'dut'
    English = 'eng'
    Finnish = 'fin'
    French = 'fre'
    German = 'ger'
    Greek = 'gre'
    Hungarian = 'hun'
    Korean = 'kor'
    Italian = 'ita'
    Japanese = 'jpn'
    Norwegian = 'nor'
    Polish = 'pol'
    Portuguese = 'por'
    Russian = 'rus'
    Slovenian = 'slv'
    Spanish = 'spa'
    Swedish = 'swe'
    Turkish = 'tur'


class OCRSpace:
    def __init__(self, api_key, language=OCRSpaceLanguage.English):
        """ ocr.space API wrapper
        :param api_key: API key string
        :param language: document language
        """
        self.api_key = api_key
        self.language = language
        self.payload = {
            'isOverlayRequired': True,
            'apikey': self.api_key,
            'language': self.language,
        }

    def ocr_file(self, filename):
        """ OCR.space API request with local file
        :param filename: Your file path & name
        :return: Result in JSON format
        """
        with open(filename, 'rb') as f:
            r = requests.post(
                'https://api.ocr.space/parse/image',
                files={filename: f},
                data=self.payload,
            )
        return r.json()

    def ocr_url(self, url):
        """ OCR.space API request with remote file
        :param url: Image url
        :return: Result in JSON format.
        """
        data = self.payload
        data['url'] = url
        r = requests.post(
            'https://api.ocr.space/parse/image',
            data=data,
        )
        return r.json()


if __name__ == '__main__':
    chinese_ocr = OCRSpace(api_key=configs.ocr.ocr_space_api_key, language=OCRSpaceLanguage.Chinese_Simplified)
    # for url in urls[:1]:
    #     pprint(chinese_ocr.ocr_url(url))
    pprint(chinese_ocr.ocr_file(configs.general.static_dir_path+'/p1/images/shop_6120f4bac9ff619deb09b0b35ff22e24.jpeg'))
