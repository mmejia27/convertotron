import formats

def detect(fname):
    return formats.FLAC

def interaction(fname, output_formats = None, output_location = None, settings):

#    if output_location:       # Windows
#        output_formats = get_format(output_location, settings) # wmv
#
#    # file first, then      imagemagick, gstreamer(?), ffmpeg/libavcodec
#    input_format = identify(file)
#
#
#    # research gstreamer    sources and sinks
#    output_options   ::         [ (Program, Switches/Arguments, Warnings/Features Lost, Sanity Index, Description) ]
#    # Description ex:        "This extracts your subtitles"
#    output_options = []
#    for of in output_formats:
#        output_options.append(get_outputs(input_format, of, options))
#
#    # considerations for what's installed, what the user cares to install
#    map (check_installed,   output_options)
#    best = find_best (output_options)


