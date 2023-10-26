#!/usr/bin/env ruby
# A script that looks for hbt and similar patterns upto 5 letters

puts ARGV[0].scan(/hbt{2,5}n/).join
