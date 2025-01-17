from .polly import Polly
from .vtt import VTT


class PollyVTT:
    def __init__(self, **kwargs):
        self.polly = Polly(
            AwsRegionName=kwargs.get('AwsRegionName'),
            AwsAccessKeyId=kwargs.get('AwsAccessKeyId'),
            AwsSecretAccessKey=kwargs.get('AwsSecretAccessKey')
        )

    def generate(self, filename, format="vtt", **polly_params):
        resp, filename, length = self.polly.synthesize(filename, **polly_params)
        vtt = VTT(AudioLengthInMs=length, PollyResponse=resp, Filename=filename, Format=format)
        vtt.write()
