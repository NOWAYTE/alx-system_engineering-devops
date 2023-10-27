#!/usr/bin/env ruby
# A script that outputs [ sender ] [ receiver ] [ flags ]

puts ARGV[0].scan(/\[from:.*?\] \[to:.*?\] \[flags:.*?\]/)
