#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Wed Apr  4 20:34:59 2018
##################################################

from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import iio
from gnuradio import zeromq
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import Initializer
from InputHandlerThread import InputHandlerThread

Initializer.init_path()

class top_block(gr.top_block):
    def __init__(self, samp_rate, freq, gain, if_gain, baseband_gain, bw, port):
        gr.top_block.__init__(self, "Top Block")

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = samp_rate
        self.gain = gain = gain
        self.freq = freq = freq
        self.bw = bw = bw

        ##################################################
        # Blocks
        ##################################################
        self.zeromq_push_sink_0 = zeromq.push_sink(gr.sizeof_gr_complex, 1, "tcp://127.0.0.1:1337", 10000, False, -1)
        self.pluto_source_0 = iio.pluto_source("", int(freq), int(samp_rate), int(bw), 0x8000, True, True, True, "manual", gain, "", True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.pluto_source_0, 0), (self.zeromq_push_sink_0, 0))    

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.pluto_source_0.set_params(int(self.freq), int(self.samp_rate), int(self.bw), True, True, True, "manual", self.gain, "", True)

    def get_gain(self):
        return self.gain

    def set_gain(self, gain):
        self.gain = gain
        self.pluto_source_0.set_params(int(self.freq), int(self.samp_rate), int(self.bw), True, True, True, "manual", self.gain, "", True)

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.pluto_source_0.set_params(int(self.freq), int(self.samp_rate), int(self.bw), True, True, True, "manual", self.gain, "", True)

    def get_bw(self):
        return self.bw

    def set_bw(self, bw):
        self.bw = bw
        self.pluto_source_0.set_params(int(self.freq), int(self.samp_rate), int(self.bw), True, True, True, "manual", self.gain, "", True)


if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    parser.add_option("-s", "--samplerate", dest="samplerate", help="Sample Rate", default=2000000)
    parser.add_option("-f", "--freq", dest="freq", help="Frequency", default=433920000)
    parser.add_option("-g", "--gain", dest="gain", help="Gain", default=30)
    parser.add_option("-i", "--if-gain", dest="if_gain", help="IF Gain", default=30)
    parser.add_option("-a", "--baseband-gain", dest="baseband_gain", help="Baseband Gain", default=30)
    parser.add_option("-b", "--bandwidth", dest="bw", help="Bandwidth", default=2000000)
    parser.add_option("-p", "--port", dest="port", help="Port", default=1337)
    parser.add_option("-r", "--gnuradio-dir", dest="gnuradio_dir", help="Install Directory for Gnuradio (Windows only)", default=None)
    (options, args) = parser.parse_args()
    tb = top_block(float(options.samplerate), float(options.freq),
                   int(options.gain), int(options.if_gain), int(options.baseband_gain),
                   float(options.bw), int(options.port))
    iht = InputHandlerThread(tb)
    iht.start()
    tb.start()
    tb.wait()





